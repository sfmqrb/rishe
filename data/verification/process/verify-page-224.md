# Verification process log — verify-page-224


## [2026-09-06T15:14:42.370Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 224 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-224.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-224.json. Write /home/sfmqrb/git/rishe/data/verification/page-224.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 224` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:14:43.872Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:14:44.581Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:14:44.594Z] TOOL RESULT

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


## [2026-09-06T15:14:44.955Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-224.txt"
}
```


### [2026-09-06T15:14:44.999Z] TOOL RESULT

```
1	=== PDF page 224 (book page 194) ===
2	--- entry 0 ---
3	ROOT I 1 -> redirect to Ei
4	--- entry 1 ---
5	ROOT [Indo-European] I 2, Io, E : pronominal stem  (refs POK:281; KNT:203)  PART 1
6	#1 (parent #0) [Avestan] refs=POK:281,285; KLN:763 | itha, itta, aěta-vant : here, there, so, thus, then
7	  #2 (parent #1) [Persian] refs=BQT:193,197; HRN:32 | îdar «ایدر» : here ; îdŭn «ایدون» : now, such
8	#3 (parent #0) [Avestan] refs=POK:283; KNT:203 | im, iyam, imam : she, he, then ; it : that ; yô : who, which, what ; ya-târa : which one (of two)
9	  #4 (parent #3) [None] refs=None | 
10	#5 (parent #0) [Germanic / Old English] refs=AHD | 
11	  #6 (parent #5) [English] refs=None | yet, yes, if
12	#7 (parent #0) [Latin] refs=AHD | îdem, iden : same ; îta-em : item
13	  #8 (parent #7) [English] refs=None | identify, identical, identity ; item, iterate
14	#9 (parent #0) [Indo-European] refs=AHD:1520,1523 | E-tero : the other ; Ke-e-tero : other time, other part, again ☞Ki 2
15	  #10 (parent #9) [Avestan] refs=KLN:545; POK:284 | a-târa : one of the two ; at-zur
16	    #11 (parent #10) [None] refs=None | 
17	  #12 (parent #9) [Latin] refs=KLN:545; POK:284 | ce-terus : the other part ; et-cĕ-terî : and other things ☞Eti
18	    #13 (parent #12) [English] refs=None | et cetera
19	
```


## [2026-09-06T15:14:48.053Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-224.json",
 "description": "Read source JSON for page 224"
}
```


### [2026-09-06T15:14:48.086Z] TOOL RESULT

```
{
  "pdf_page": 224,
  "book_page": 194,
  "entries": [
    {
      "root": {
        "name": "I 1",
        "redirect": "Ei"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "I 2, Io, E",
        "lang": "Indo-European",
        "refs": "POK:281; KNT:203",
        "gloss": "pronominal stem"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:281,285; KLN:763",
          "words": [
            {"translit": "itha, itta, aěta-vant", "gloss": "here, there, so, thus, then", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:193,197; HRN:32",
          "words": [
            {"translit": "îdar", "gloss": "here", "script": "ایدر"},
            {"translit": "îdŭn", "gloss": "now, such", "script": "ایدون"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "دل و جانم ایدر بماند همی - مژه خون دل برفشاند همی", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:283; KNT:203",
          "words": [
            {"translit": "im, iyam, imam", "gloss": "she, he, then", "script": null},
            {"translit": "it", "gloss": "that", "script": null},
            {"translit": "yô", "gloss": "who, which, what", "script": null},
            {"translit": "ya-târa", "gloss": "which one (of two)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic / Old English",
          "refs": "AHD",
          "words": [],
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
            {"translit": "yet, yes, if", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "îdem, iden", "gloss": "same", "script": null},
            {"translit": "îta-em", "gloss": "item", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "identify, identical, identity", "gloss": null, "script": null},
            {"translit": "item, iterate", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "AHD:1520,1523",
          "words": [
            {"translit": "E-tero", "gloss": "the other", "script": null},
            {"translit": "Ke-e-tero", "gloss": "other time, other part, again", "script": null, "see": ["Ki 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Avestan",
          "refs": "KLN:545; POK:284",
          "words": [
            {"translit": "a-târa", "gloss": "one of the two", "script": null},
            {"translit": "at-zur", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "Latin",
          "refs": "KLN:545; POK:284",
          "words": [
            {"translit": "ce-terus", "gloss": "the other part", "script": null},
            {"translit": "et-cĕ-terî", "gloss": "and other things", "script": null, "see": ["Eti"]}
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
            {"translit": "et cetera", "gloss": null, "script": null}
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


## [2026-09-06T15:14:48.591Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:14:48.628Z] TOOL RESULT

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


## [2026-09-06T15:14:53.728Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','KLN','BQT','HRN','AHD','WLD','BRT','IEC','SYN','LEW','LAT','SKT','MON','ARY','HUB','PHD']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print('---')\n\""
}
```


## [2026-09-06T15:14:54.005Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo === && ls data/verification/page-2*.json | tail -5"
}
```


### [2026-09-06T15:14:55.497Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
---
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
---
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
---
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
---
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
---
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
---
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
---
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
---
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
---
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
---
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
---
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
---
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
---
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
---
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
---
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
---
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
---
```


### [2026-09-06T15:14:55.540Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-06T15:14:59.855Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','KLN','AHD','BQT','HRN']:\n    v=d[k]\n    print('==',k)\n    print('offset:',v.get('page_offset'))\n    print('hint:',v.get('lookup_hint'))\n    print('files:',v.get('local_file'),v.get('local_files'))\n\""
}
```


### [2026-09-06T15:15:01.439Z] TOOL RESULT

```
== POK
offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt ['/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt']
== KNT
offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt None
== KLN
offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt']
== AHD
offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
files: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt None
== BQT
offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
files: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] None
== HRN
offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
files: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt None
```


## [2026-09-06T15:15:02.418Z] TOOL CALL #8: Bash

```json
{
 "command": "ls site/pages/224.jpg 2>/dev/null; pdftoppm -f 224 -l 224 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg224 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:15:04.486Z] TOOL RESULT

```
site/pages/224.jpg
total 2068
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:15 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    462 Sep  6 11:14 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
```


## [2026-09-06T15:15:07.949Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg224.png"
}
```


### [2026-09-06T15:15:08.328Z] TOOL RESULT

```

```


## [2026-09-06T15:15:08.322Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:15:32.339Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 28[1-6]\" POK_full.txt | head -20"
}
```


### [2026-09-06T15:15:32.389Z] TOOL RESULT

```
26183:Page(s): 281-286 
29159:Page(s): 281
```


## [2026-09-06T15:15:33.227Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=289 && NR<=290' POK_01.txt | head -120"
}
```


### [2026-09-06T15:15:34.840Z] TOOL RESULT

```
,  Gespenst',  m.  ,Unhold' av.  druj-  f.  ,Lüge,  Trug;  Verkörperung  der  Lüge';
mir.  aur-ddrack  (nachtonig  aus  *druag  =  ai.  drögha-)  , Gespenst';
as.  bidriogauj  ahd.  triogan  ,trügen',  anord.  draugr  m.  , Gespenst'^ schwundstufig  as.  gidrog  n.  , Trugbild',  mndl.  gedroch  ds.,  ahd.  gitrog  i} ,Betrug,  teuflisches  Blendwerk';  anord.  draumr^  ahd.  troum,  as.  drt engl,  dream  ,Traum'  (germ.  *drau{y)ma-  ,Trugbild').
Idg.  dhreugh-  ist  sehr  wahrscheinlich  verwandt  mit  dhuer-  , durch  Täu5 schung  zu  Falle  bringen',  indem  zur  Schwundstufe  *dhru-gh-  aus  *dhuY't sich  neue  Hochstufen  idg.  *dhreugh',  *dhrough-  einstellten.  Mit  dem  er- weiternden gh  wäre  das  von  nhd.  Zwerg  identisch,  wenn  dieses  Wort' nicht  auf  ein  verschiedenes  idg.  dhuergh- , zwerghaft,  verkrüppelt'  (s.  dort) zurückgeht.
WP.  I  874.
dhrigh'  (oder  dhreikb-)  ,Haar,  Borste'.
Gr.  d^Qi^j  tQix^g  f.  ,Haar,  Borste',  davon  d-glaaccy  att.  ^giTta  f.,  ein  Fisch mit  feinen  Gräten',  TQixiag,  'f^^X'S  ds.;
mir.  gairb-driuch  (*drigu-  oder  *driku-)  ,Borste'  (garb  ,rauh');
aus  gr.  d^Qiaaa  stammt  wohl  ital.-lombard.  trissa  ,Lota  Iota';  daraus  wohl ebenfalls  Schweiz.   Trische  (11.  Jh.  trisca)]
falls  bsl.  *draika'  ,lang  gestreckt'  als  *dhroiko-  hierher  gehört,  also  lit. driekti  ,ausdehnen,  ausziehen  (einen  Faden)',  drykti  ,in  langen  Fäden herabhängen',  slovak.  driek  m.  , Stamm',  driecny  ,stämmig',  abg.  dvbkoh , Stange',  usw.,  könnte  unsere  Wurzel  als  *dhreikh-  angesetzt  werden.
WP.  I  876,  Jud  BullGlPat.  Suisse  Rom.  11,  8  2,  Trautmann  58  f.,  Ber- neker  223,  232.
dhrono'  ,bunt'?
Für  gr.  ^QÖva  PI.  , Blumenverzierungen  in  Gewändern  (bei  den  alexan- drin. Dichtern  für  q)dQ[.i(xy,a,  Zauber-,  Heilkräuter  gebraucht),  bunte  Ge- wänder, bunte  Tiere'  erschließen  Hoff  mann  BB.  15,  86,  Liden  Stud.  67  f. eine  Grundbed.  ,bunt'.  Unter  dieser  Grundbed.  vergleicht  Liden  aaO. alb.  dre-rij  geg,  dr^-ni-  m.  , Hirsch'  (Tiere  aus  dem  Hirsch-  und  Reh- geschlecht sind  häufig  als  ,gesprenkelt,  bunt'  benannt),  wofür  eine  illyr. Gdf.  *drani-  (idg.  dhroni-)  durch  die  wohl  illjr.  Hesychglosse  aqavL^' klaq)OQ  {A-  verschrieben  für  /1-)  geboten  wird.
277
Stokes  Mel.  Kern  [RC  24,  217]  vermutet  für  d-göva  als  eigentliche  Bed. Stickerei'  wegen  mir.  druine  ds. '    AVP.  I  8'^6  f.,  WH.  I  374.
fitiüg{b)ster'  ,Tocliter';  Guttural  wie  bei  *eg{h)om  ,ich',  s.  dort.
Ai.  duhltdr-  {duhitd),  av.  dugddar-,  duySar-  (aus  *dughter-),  npers. duxtar,  duxt,  arm.  (mit  s  au
s  k  nach  w)  c?w5^r,  Gen.  dster,  gr.  &vy(XTr^Q (Akzentverschiebung  wie  in  iirjTr^Q,  aber  noch  dvyaTeqa  wie  (.irjzega),  osk. yii^iV;  Dat.  fu{u)trei  (Vetter  Gl.  29,  242),  got.  daühtar,  anord.  c^ö^^iV  (run. Nein.  PI.  dohtriR),  ahd.  ioÄ^er,  lit.  dukü,  -efs,  apr.  ducktij  aksl.  c^?>5<i,  -ere, toch.  A  ckäcar,  B  tkäcer  ,Tochter^ WP.  I  868,  WH.  I  557.
dbucn-,  dbun-  , dröhnen,  tönend
Ai.  dhvdnati  ,tÖnt,  rauscht',  dhvani-  m.  ,Laut,  Hall,  Donner,  Wort', dhvand'  m.  ^Laut,  ein  bestimmter  Wind'^  dhvanita-  n.  ,Ton,  Hall,  Donner^, dhuni-  , rauschend,  brausend,  tosend',  dhundyati  , rauscht^;
anord.  dynr  m.  ,Gedröhne',  ags.  dyne  n.  ds.,  engl.  c?m,  ahd.  tuni  ds.; anord.  dynia  (Prät.  dunda)  , dröhnen,  lärmen',  ags.  dynnan,  as.  dunnian mhd.  tünen  ,dröhnen';  germ.  Erweiterungen  davon  scheinen  anord.  dynkr ,Lärm,  Schlag',  mengl.  dunchen,  engl,  dunch  ,puffen'  und  ndd.  dunsen , dröhnen,  stampfen',  schwed.  dial.  dunsa  ,krachen,  schlagen'.
Einmischung  neuerlicher  Schallnachahmungen  kommt  für  die  germ« Worte  ebenso  wie  für  lit.  dundeti  , heftig  pochen,  dröhnen'  in  Ji'rage.
WP.  I  869.
dbuer-,  dhuerQ-  , durch  Täuschung,  Hinterlist  zu  Fall  bringen,  schädigen* ( :  dhuf- :  ditru-).
Ai.  dhvdrati  , beschädigt',  Partiz.  dhrutd-,  -dhrut  (und  -dhvft),  dhruti- f.  , Täuschung,  Verführung',  *dhvard-  , trügend'  in  dkvards-  f.  (Nom.  -äh) ,eine  Art  weiblicher  Dämonen';  dhürvati  , bringt  durch  Täuschung  zu Fall,  beschädigt'  (Tiefstufe  einer  schweren  Basis  dhuer9-),  dhurta-h  ,he- trügerisch',  m.  ,Betrüger',  dhürti-  f.  ,listige  Beschädigung' ;
lat.  fraus,  -dis  f.  , Betrug,  hinterlistige  Täuschung,  Schaden,  Strafe', frausus  sum  (Plaut.),  umbr.  frosetom  ,fraudätum*,  lat.  früstra  (jünger früsträ)  , irrtümlich,  vergeblich',  davon  früstror,  -äri  ,täusche,  hintergehe' gehören  wohl  als  c?-Erweiterung  unserer  Wurzel  hierher  (s.  darüber  unter dhreugh-)-^  unklar  ist  nur  das  a  (mot  populaire?  EM  382;  unglaubhaft WH.  I  543);
hierher  wohl  hitt.  du-wa-ar-na-ah-hu-un  (dwamahhun?)  ,ich  brach'.
WP.  I  869  f.,  874,  WH.  I  543  f.^  ^
278
f
dhu^r-,  dhuor-f  dhur-,  dhur-  ,Tür^-  neben  diesem  kons.  St.,  der  ursprüno-j ein  Plurale  und  Duale  tantum  war  (s.  u.),  stehen  zum  Teil  Avohl schon  urspi-achli  he  -o-  und  -ä- Erweiterungen  teils  mit  zu  vermuten der  kollektiver  Bed.,  teils  (als  Neutrum)  in  der  Stellung  als  2.  Kompo- sitionsglieder.
Ai.   Nom    PI.   dvnrah,  Akk.   PI.  durah,  durah,  Nom.   Du.  dvärä(u)  ,Tüpt (Verlust    der    Aspiration    ursprüngl.    in    den    5/j-Kasus   durch   Einfluß  von  M dvöu    jZwei'),    durönd-    n.    ^Wohnung-,    Heimat'    (-?io-A bleitung    vom  .Lok.  ij Du.  ar.  *dhuräu)]   o-St.    dväram   n.  (jung)   ,Tür*   in   Kompositis  satddura-  "^ n.  ,mit   100  Türen  verschlossener  Ort';   av.  Akk.   Sg.  dvardm,  Lok.  dvavd ,Tor,  Hof,  apers.  duvarayä  ,am  Tore';
arm.  PI.  dur-lc,  Akk.  z-durs  (*-ws)  ,Tür',  t   durs  ,hinaus,   draußen',  Sg. dufn,  Gen.  dran  ,Tür,  Tor,  Hof   (die  n-Dekl.  vom  Akk.  Sg.  auf  -m  aus- egangen),  dr-and  ,Türpf()Sten,  Türschwelle'  (*dhtir  -j-  *andtä,
```


## [2026-09-06T15:15:39.255Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26150,26200p' POK_full.txt && echo \"=====29100=====\" && sed -n '29120,29175p' POK_full.txt"
}
```


### [2026-09-06T15:15:39.336Z] TOOL RESULT

```
Burushashki 

Hunza h\k, Yas/nhek 

Etruscan 

Etruscan+ thu(n) 

Semitic 

East: Akkadian+ ishte:n, Central: Arabic wa:hid, Kashka-Darya iad, Saudi \Naah\d, 

Yemen/ v\/aah\d, Syrian ^a.hed, Lebanese ^ahad, Cypriot Texen, iraqi\Naah\d, Egyptian 

wa:hid, E Libyan '^ahad, N African (Darja) ^a.hed, Moroccan ^ahed, Sudanese \Naah\d, 

Nigerian \Na:\\\d, Zanzibari\Na:\\\, Maltese wieh=ed, Phoenecian+ '-h-d, Ugaritic+ ahd; 

Moabite+: Classical Hebrew+ 'ahat, Modern Hebrew 'axat, Classical Aramaic+ xadh, 

Modern Aramaic ahad, Classical Syriac+ hadh, Syriac kha, Vanhe; 

South: Old S. Arabian+ '-h-d, South Arabian (l-iarsusi) \:a:d, fSheriJ i'ad, So co tra i' ad; 

N Ethiopia Geez+ ?ah=adu, Tigre worot, Beni Amir orot, Tigrinya hade; 

S Ethiopia. Amharic and, Argobba hand, Harari ahad, E Gurage ad, Gafat+ ajja, Soddo att 

Goggot quna, Muher at, Masqan at, CW Gurage at, Ennemor Attic 

References: WP. I 95 ff., WH. I 368 f., 399 f., 409, 671 , 720 ff., 869, Trautmann 3, 65, 72, 
1 05, Schwyzer Gr. Gr. I 548, 588, 608, 61 3 f., 628 f., 651 . 
Page(s): 281-286 



Root / lemma: errto'"/-, empi- 
Meaning: a kind of mosquito or bee 
Note: With taboo variation b^ : pi 
Material: Gr. spnic;, -i5oq 'a mosquito '; 



Old High German //77i6'/ (oldest evidence impi pTano), Middle High German imbe {* embi- 
o) "swarm of bees, beehive', previously late-Middle High German "bee'. Modern High 
German Imme, changing through ablaut Old English imbe{*umbia) "swarm of bees'. 

References: WP. I 125, WH. I 57. 
Page(s):311 

=====29100=====
without; lacking experience; immune from ', Old English in sewsede^ nude ', Old High 
German amad: uomad^ after reaping, harvesting ', awahst: uowahst^ growth, 
development, increase; germ (of idea); offshoot; advancement (rank) ', " occiput, back part 
of the head or skull ', Old English dgenger\he (retreating) Querriegel ', oleccan^ flatter, 
compliment, chatter, wheedle ' from *d-lukjan\ d suffixed in Akk. Sg. the pron. Dekl., e.g. 
Gothic fvano-h, fvarjatd-h, f^ana etc. 

In Slavic *eor*d, colorless in some compounds, as Serbo-Croatian-Church Slavic y^- 
skudb besides Church Slavic skgdt "ugly' (see Berneker 441); e following the Lok. and 
with this deformed in type Old Bulgarian kamen-e and Lithuanian rankoJ-e"\n the hand'. 

References: WP. I 95 f., WH. 388, 642, Specht KZ. 62, 56, Hirt Indog. Gr. IV 54, Schwyzer 
Gr. Gr. I 434, 6483, 7221. 
Page(s): 280-281 

Root / lemma: e2, o 

Meaning: interjection (vocative) 

Material: Old Indie a emphasizing behind adverbs and nouns: "oh!'; 



gr. n " hey, hallo!, you there!', also emphasizing and questioning " really!?' n H cnibira, 
Lesbian n MCiv etc., also inri-TOi, £TT£i-r|, r|(F)£ "or', n-5r|; probably also lak. tar. eYWV-n, 
whereupon horn. Tuvr) etc.; 

Latin eh'e'\, hey, hallo!, you there!', e-castor^ by Castor', edepdr by Pollux ', edT{*e 
deive), etc.; 

Old High German ihh-a^\ Gust)', ndd. iaka, Proto Norse hait-ik-a, probably also Old High 
German nein-a^ no, nay' ; 

Lithuanian e, e, Latvian e, e, exclamation particles; 

about Slavic e- in exclamation see below S. 283; 

References: WP. I 99, WH. I 1, 389, 396, Schwyzer Gr. Gr. I 606. 
See also: s. further under ehem. 
Page(s): 281 

Root / lemma: eg- 6g- qq- 

Meaning: to say, speak 

Material: Armenian asem^say\ if s instead of c{= Indo Germanic^) is established through 

the position in the 3. Sg. *asfrom *ast= *agt, verbal noun ar-ac^ proverb '; 

gr. n " he spoke ' (the unique hom. form; from *eg-t}, wherefore is joined after hom. 1. 
Sg. Imperf. pv, 1. 3.Sg. present npi, nai (Doric nri) as neologisms after (£)(pr| : (£)(pr|v, cpHM'. 
anoi. Perf. av-wya " order, command ' (originally " I announce ' (?), ava as in avaKaA£Tv " 
shout loudly ' ), presently reshaped avcbyu); about nxciv£v £Itt£v s. EM2 30 and Liddell-Scott 
s. v.; 

Latin a{i)d^ say, speak, state ' {*agid), the prophetic god Aius Locutius, adagio, -onis,
```


## [2026-09-06T15:15:42.796Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=25800 && NR<=26183' POK_full.txt | grep -n \"Root / lemma\\|Meaning:\" | head"
}
```


### [2026-09-06T15:15:44.698Z] TOOL RESULT

```
254:This is all wrong etymology. Root / lemma: e-3, ei-, /-, fem. T-\ "this, etc. (demonstrative
```


## [2026-09-06T15:15:46.618Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: e-3\" POK_full.txt | head"
}
```


### [2026-09-06T15:15:46.667Z] TOOL RESULT

```
25715:Root / lemma: e-3, ei-, /-, fem. T-{*he-3) 
26053:This is all wrong etymology. Root / lemma: e-3, ei-, /-, fem. T-\ "this, etc. (demonstrative
```


## [2026-09-06T15:15:48.362Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25715,25800p' POK_full.txt"
}
```


### [2026-09-06T15:15:48.411Z] TOOL RESULT

```
Root / lemma: e-3, ei-, /-, fem. T-{*he-3) 
Meaning: this, etc. (demonstrative stem); one 



Note: {e, /probably originally demonstrative particle). To /-is joined the relative stem^o-. 
Summarizing representation offer esp. Brugmann Dem. 32 ff., BSGW. 60, 41 ff., Grundr. 
I|2 2, 324 ff., Pedersen Pron. dem. 31 1 ff. 
Material: A. case-by-case used forms: 

Old Indie ayam "he' = Gatha-Avestan ayam, jav. aem (after aham "T widened Aryan *a/ 
= Indo Germanic *er, Indo Germanic *e/of stem e-, as *q"'o-/of stem /("'o-, not lengthened 
grade to /■); 

Note: 

Reduplicated initial laryngeal in h2"ahre- > Avestan ae- 

Old Indie /dam " it ' (without the secondary -a/77-extension Old Indie ft, Avestan /7as 
emphasizing particle). Old Indie /ya/T? (extended from *h) = Avestan /777(i.e. /ydm), Old 
pers. /yam^ she ', Akk. Sg. m. Old Indie //775/77 (extended from */m) = Old pers. /mam {that 
after f. /mam etc.), Gen. m. n. asya, asya = Avestan a/ie, fem. Old Indie asyafi = Avestan 
a/rj/ia, Dat. m. n. asmai, asma/ = Avestan a/ima/ Gen. PI. m. n. esam = Avestan aesqm, 
Dat. Abl. PI. m. Old Indie ebfiya/i= Avestan ae/byo etc.; Gatha-Avestan as[-c/l], a each 
once n. Sg. m.; of stem a- PI. fem. Gen. Old Indie asam =Avestan arj/iqm, Dat. Abl. 
abhyati = Avestan aJbyo etc. 

Maybe alb. {a-y) ay, aj/^he', i*a-yo) ayb'she' : Old Indie ayam'he'. 

Kypr. IV ' him, her ' (seems also in piv, viv blocked, s. Schwyzer Gr. Gr. I 608''); here 
Lesbian Thessalian hom. la {*//9) " one, a single ' (originally "just this, only this'), hom. \{]q, 
\r\, thereafter also n. hom. ico?; different Schwyzer Gr. Gr. I 588 {*s{m\/as). 

Latin /is 'he', /b^'it' Nom. Sg. m. (old also /s, insehr. e/s, e/s-dem, provided either with -s 
Indo Germanic *e/= Old Indie ay-am, as one considers also for Umbrian er-eav\6 certain 
for Irish (/7)e"he' such a basic form *e/-s, or reshuffled of /5 after e//us, e{/)/}; Akk. Old Latin 
/m (= gr. iv) and em, doubled emem " the same, at the same time ' (from the parallel stem 
e-1) = Adv. em " then, at that time, in those times ' and */m in /nter-/m 'at the same time, 
meanwhile, in the meantime ', /n-de ' from that place, thence ', Dat. Abl. PI. /bus (: Old 
Indie ebhya/i); Oscan /z-/c»' he ', /d/c, fdil<^ it ' (the affix -//<, -/c\s itself the solidified adverb 
from n. */d+ */<e), Oscan is-id-um' the same ' and esfdum^s., Umbrian er-e^ he ' ers-e 
ef-e^ it ', Umbrian Dat. Sg. esme/, esm/l<. Gen. PI. Oscan e/sun-l<, Umbrian esom{= Old 
Indie esam); 



thereout a stem *eiso- would be deduced besides in Nom.-Akk.-forms, e.g. Oscan eizois^ 
with them ', Umbrian eru-ku^ with it ', however, it is to be reckoned after all with an old n. 
*ed, compare Latin ecce^ behold! lo! see! ' (probably from *ed-ke) = Oscan ekk-um ( *ed- 
ke-um) " likewise, besides, also, further, moreover, too, as well ', and perhaps Akk. med, 
ted, sed, if from *me, *te, *se+ ed, although this assumes only a more solidified adverb 
*ed, 

Italian eo, ea, in Oscan-Umbrian only in Nom. (besides Sg. m. n.) and Akk., in Latin 
mainly in almost all case oblique (only e/^sfrom *esio-s, thereafter Dat. e/ stands apart), 
e.g. Latin ea'she', eam'her', Oscan /uk, /be "she', /onc^hwn', under eam^her', have 
derived from Old Indie Nom. ay-a/r? corresponding form *e(/)om, because of their ending - 
0/77 would be perceived as Akk. and entailed eam^her' etc. 

/ambyVam 1.1. 5, 166 and 8, 44 probably spelling mistake for eam^her'. - From Latin 
here /pse'self, in person ' from *-/s-/Ose' (because of Old Latin fem. eapse), /s-Ze (however, 
ille' that, that yonder, that one; emphatically, that well-known; the former, (sometimes the 
latter)' only afterwards reshuffled ollus), compare Umbrian estu^ that of yours, that beside 
you '; 

Old Irish e{h§) "he' (probably *ei-s), see above; ed{hed) "if (from *id-a= Gothic ita, 
wherewith formal identical Old Indie /da^now, yet'; but Lithuanian fada^then' required 
because of East Lithuanian fadu an auslaut in nasal); Nom. PI. e(/7e) m. f. n. = mkymr. i/i/y 
(hwynt-wy) probably at least partly from Indo Germanic *e/(additional information by 
Thurneysen Gr. 283), Akk. Sg. bret. en'hwn, it' (prefixed), cymr. e(also), Irish -an- (also), -/ 
(suffixed after verbs; after prepositions partly also, e.g. a/r/irom *ari-en " on him ', partly 
only more as having a lasting softening effect, e.g. foirirom *uor-en). Gen. Sg. *esio, f. 
*esias "his, her', proklit. a, older partly still e, 3e\ cymr. *ei&- after the example of the 
conjugated preposition to differentiated mcymr. eidaw, f. eidi, wherewith identical Old Irish 
a "his, its' (len.) and "her' (geminated), cymr. corn, y, bret. e, etc.; about Old Irish 
accentuated ai, ^e"his, her' and Dat. PI. -ibs. Thurneysen Gr. 285; 

Gothic /is "he', Akk. in-a, neutr. //-a (see above) "if (in addition new formed plural forms: 
Gothic e/sfrom *ei-es, Akk. ins, Dat. im. Old High German Old Saxon im) Old High 
German er, ir, Akk. in-an, in, n. iz. Old Saxon in-a, n. it. Old Norse Relative particle es, er. 
Runic eR, of stem e-: Gen. Sg. Gothic m. is, f. izos. Old High German m. n. es(is), f. 
ira{iru). Old Saxon es(is), era(ira). Gen. PI. Gothic ize, izo. Old Saxon Old High German 
ira, Dat. Sg. f. Gothic izai. Old High German (with other ending) ins, m. n. Gothic imma. Old 
High German imu, imo. Old Saxon imu, of stem /-Gothic Akk. ya(Old High German sia
```


## [2026-09-06T15:15:55.418Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=25715 && NR<=26185' POK_full.txt | grep -n -i \"tero\\|ceteru\\|atara\\|itha\\|aetauuant\\|aetavant\\|yatara\\|Avestan /9a\\|thus\" | head -40"
}
```


### [2026-09-06T15:15:57.227Z] TOOL RESULT

```
115:comparative Old Indie yatara-, Avestan yatara-, gr. (Cretan gort.) oTspoc; ' one or the 
153:To e-also the comparative formation Avestan atara-^ this, the one from the two, the 
154:other', ds., alb. ya/(e)/'e "other', Umbrian e/ro- "other', Latin in ceterus' the other, the rest; 
190:tero-:0\6 Indie /-tara- 'the other' (neuiran. equivalent by Bartholomae IF. 38, 26 f.); 
214:manner, in this wise, in such a way, so, thus, accordingly, as has been said ', mcymr. 
273:D. compositions and derivatives (not classed above thus far):
```


## [2026-09-06T15:15:59.020Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=25715 && NR<=26185' POK_full.txt | sed -n '108,125p;145,200p'"
}
```


### [2026-09-06T15:16:00.494Z] TOOL RESULT

```
Old Indie yas, ya, yad, Avestan yd, gr. 6c;, ri, 6 'who, what, which, the one that', 
Phrygian \oc, (vi) ' whoever ', Slavic *Ja- in i-ze, f. Ja-zee\.c., Baltic under Slavic in the 
solidified form of adjective, e.g. Lithuanian geras-is. Old Prussian pirmann-ien, -in. Old 
Church Slavic dobry-Jb (see Berneker416 f., Trautmann 105 f.). Dubious (Lithuanian yis/"' 
what if, when ', Q>o\}(\\q, JabaT what if, when ') s. by Brugmann l|2 2, 347 f. (Lithuanian); 
Celtic by Pedersen KG. II 235, Thurneysen Gr. 323, however, cymr. 5 can not belong to it. 

comparative Old Indie yatara-, Avestan yatara-, gr. (Cretan gort.) oTspoc; ' one or the 
other of two '; compare Old Indie yavat, gr. swc;, Doric ac; (*a:Foc;) ' as long as ', Old Indie 
yad^ inasmuch, as ' = gr. 6ic, 'as'; s. Schwyzer Gr. Gr. I 528, 614 f. 

C. particles and adverbs: 

About the nominal and adverbial particle e, osee above S. 280 f. 

e-, e- Augment ('*then, at that time ') Old Indie a- (also a-, e.g. a-vrnak), Avestan a-, 
arm. e- (e.g. e-lik'= s-Ains), gr. £- (also n-, e.g. hom. nPsiSn). 

"interrogative particle'; enclitic particle of gen. and (attribute) adj. m. /(from he), f. e(from 
she). 

insecure Gothic i-bai, /-/^a interrogative particle. Old High German ibu, oba. Old Saxon 
Old Norse efW and "whether'. Old English gif, engl. if 6s.; 

about *eno-\'r\ gr. £vr| etc. see special headword. 

To e-also the comparative formation Avestan atara-^ this, the one from the two, the 
other', ds., alb. ya/(e)/'e "other', Umbrian e/ro- "other', Latin in ceterus' the other, the rest; 
Ace. n. sing, as adv. otherwise, moreover, but ', Old Church Slavic etert, jeterb "whoever', 
P\. jeterUJi) "some, few'. Lower Serbian wotery. 

Note: 

Alb. and Slavic use y- for the lost laryngeal /?-. 

ef/(Nom. Akk. Sg. n.): about Latin ecce, medsee above; Avestan alio the emphasis of 
the preceding word (as //, see below; Bartholomae Altiran. Wb. 67); probably also in Old 
Church S\ay\c jed-in-b, -tnb " someone ' as "*just, only one'; whether also Church Slavic 
jede, kyjb " a certain, a kind of, as one might say ' from doubled *ed-edox after ide in 
attached ending *edl (Berneker 261, disputed from Bruckner KZ. 45, 302, compare Meillet 
Slave comm.2444.) 

e<yand dd{Nc\): Old Indie aV therefore, next; and; (in subsequent clause) so', Avestan 
aa7"next, therefore, then; and; but; since ', East Lithuanian e"and but' (Old Church Slavic / 
"and' is rather *ei), Lithuanian o"and, but' = Old Church Slavic a "but'. 



e/(Lok.): gr. si "*so, if, whether ' (sT-ra " then, next ', £i-6£ " would that! ', stt-si (compare 
el. £n-n) ' after that, after, since, when ', ett-eitq "thereupon'; besides dial, ai, Lok. off. 
stem a, and n Instr. 'if; Old Church Slavic /'and, also' (compare //'and' of stem *to-\ from 
Bruckner KZ. 46, 203 placed against it = Lithuanian tel), Gothic -e/ relative particle 
(compare A'e/of stem *to- in same meaning), e.g. s5-e/'who, what, which, the one that', 
after Junker KZ. 43, 348 also Armenian Abl. -ending -e. See also under /-. 

e/77(Old Latin em, see above S. 282) lies before in gr. svGa ' there, to there, at that time 
', rel. 'where, whereto, where, whence', svGsv ' there, from there, from where' etc. 
(Schwyzer Gr. Gr. I 628); about Old Irish andsee above S. 37 and compare Cypriot av5a 
auTr|. 

e-tos. Old Indie a-tahlrom here' (see below ef/). 

/■probably in Lok. in Indo Germanic -/ further the base of the comparative formation 7- 
tero-:0\6 Indie /-tara- 'the other' (neuiran. equivalent by Bartholomae IF. 38, 26 f.); 

Latin /ferum' again, a second time, once more, anew '; further in Old Indie f-va'as' 
(compare above n-Fs 'as'); in gr. i-5£ 'and' (compare n-5£). 

i-6'^a and /-d^e: 

Old Indie f-ha, prakr. /dha, Avestan /55'here'; 

gr. i0ay£vri(; '(* born in lawful wedlock, legitimate; born here ', hence:) inborn, lawfully 
born ' (about i9aiY£vn(; s. Schwyzer Gr. Gr. I 448);
```


## [2026-09-06T15:16:23.910Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=25715 && NR<=26185' POK_full.txt | sed -n '200,285p'"
}
```


### [2026-09-06T15:16:25.574Z] TOOL RESULT

```
born ' (about i9aiY£vn(; s. Schwyzer Gr. Gr. I 448); 

Latin /bF in that place, there ' (the sound development d^ to f, /? after ubr, in auslaut 
directed after the locative the ostem), Umbrian //fe' in that place, there ', /font' in the 
same place, in that very place, just there, on the spot ' (Aryan and Italian forms could 
contain themselves also -d^e, compare Old Indie ku-ha =0\6 Church Slavic kb-de 'where' 
[alb. /r^oto 'everywhere'], sb-de'\r\ere' and Schwyzer Gr. Gr. I 627^); 

mcymr. yd, yncymr. yo'o'verbal particle, corn, yz, yth-, bret. ez-l (see Pedersen KG. II 
234, Lewis-Pedersen 243, Thurneysen Gr. 324 f.); in addition also Old Irish prefixed -id- 
from *id(h)e or* /d{h)/. 

i-t(h)-:0\6 Indie ittha, itthad'here, there', Avestan /Pa'so', Old Indie /ttham'so' and with 
-/- (-/a or-//?) Old Indie ///'so'; Latin //a 'so', /tem'a\so, likewise', Umbrian /tek' in this 
manner, in this wise, in such a way, so, thus, accordingly, as has been said ', mcymr. 



preverb yt-, ncymr. yd-, e.g. in yryd-wyf "I am'; Lithuanian dial. //" by all means; as ', /'/, yt 
" completely, very much ', Latvian //, itin " surely, just '. 

^(stressed to the strengthening of a deixis word, unstressed behind a relatively used 
word): 

Old Indie 7(also Tm), Avestan ^emphasizing postpositive, after relative in ved. yad-r, 

gr. ouTOGH, -\y (= Old Indie Tml or previously new extension from -7?), £K£ivoa-i:, el. to-T; 

Umbrian probably in yOC»-e/"interrog. adj. which? what? what kind of?; exclam., what!; 
indef. any, some; relat. who, which, what, that; interrog. in what manner? how?; relat. 
wherewith, wherefrom; indef. somehow' (etc.), Latin in utf how (interrog. and exclam); 
relat. as, in whatever way; as, as being; as when, while, since, when; where; how; o that; 
granted that; so that, namely that; final, in order that; that, to; that.. .not' (from *uta-l)\ 

Old Irish (/7)/"deixis particle and particle before relative clauses; 

Gothic -e/Relative particle in sa-ei, iz-ei, //r-e/whereas probably Indo Germanic *ei, see 
above; 

Old Church Slavic intensifying in /c»-/(see Berneker416), Old Church Slavic e-/" yes, 
indeed ' (? Berneker 296). 

Also in 1. part from Old Indie T-drg-^ looking so, resembling so ', Lithuanian y-paciaT 
particularly, specially, especially, particular: in particular, peculiarly, separately, extra, 
notably ', y-patus ' lonely, only, apart, peculiarly '. 

Doubtful, if from Indo Germanic *e/or I Old English Tdseges^ of the same day ', Tsides^Xo 
same time', TIca {*T-ITca) 'the same', wherewith perhaps Old Norse F dag ^to6ay' (although 
understood as preposition /) and refined afterwards Tgaer^ yesterday ', Tfjgrd^ a year ago, 
last year ' interrelate; 

It is unclear a/(Lok. fem. in adverbial solidification) in Old Indie a/-samah adv. 'this year', 
meaning 'just this year - the same' as gr. iu) hmciti, s. Sehuize KZ. 42, 96 = Kl. Schr. 539^, 
Holthausen KZ. 47, 310, Junker KZ. 43, 438 f., with Old Indie words also Armenian a/zm 
combined from *ai zam. The same as mentioned before Armenian demonstratives ai-s, a'h 
d, 5/-/7 contain *a/in conjunction with Pron.-stem *Ro-, *to-, "Wo- (Junker aaO.); compare 
Benveniste Origines 129 ff., Schwyzer Gr. Gr. I 548 f. 



jam{= Akk. Sg. f.): Latin /a/77" now, by now, already; of future time, immediately, 
presently, soon; henceforth; further, moreover; just, indeed ', Gothicya, Old High German 
ya" indeed '; with the ending of Lok. Sg. in *-ou- the ^-stem: *Jou, t/i/ "already' (from 
Kretschmer KZ. 31, 466 placed against it to *jeu- "new') : Lithuanian yaJ "already', Latvian 
Jau, Old Church Slavic y^ "already', zero grade Gothic Old High German Old Saxon Old 
English y^ "already' (the formation is similar to Gothic t^au, t^au-h. Old English t^ea-h. Old 
Indie /^"buf to stem *to-). 

jai{== Lok. Sg. f.): Gothic ya/" yea, in truth, indeed ', Modern High German ye (/ie/?), 
Umbrian /ie perhaps " now, by now, already; of future time, immediately, presently, soon; 
henceforth; further, moreover; just, indeed ' in ie-pru, ie-pr, but cymr. ie (disyllabic) " yes, 
indeed ' from mcymr. /-erthis (is) it'. 

D. compositions and derivatives (not classed above thus far): 

Old Indie e-sa, e-sa, e-tat, Avestan aesa-, aeta- " he himself ' ( *ei-so, -to-, while 
Armenian aidixom *ai-to-, see above; Oscan Umbrian eiso-, e/c- against it from Gen. PI. 
*eisdm)\ 

Note: 

Reduplicated initial laryngeal in h2"ahre- > Avestan ae- 

(m) Armenian i-sa, i-ta, /■/7aDemin. from *ei-Ro-, -to, -no- (Junker KZ. 43, 346 f.); 

Old Indie e-va, e-va-m'so', wherefore with the meaning-development " just in such a
```


## [2026-09-06T15:16:40.136Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^i-\\b\\|^i- \\|^e-  \\|^ei- \\|^i-\\.\" AHD_watkins1985.txt | head -20; echo \"=== search identity/item/etc\"; grep -n \"identity\\|ITEM\\|ITERATE\\|ET CETERA\\|et cetera\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T15:16:40.207Z] TOOL RESULT

```
559:i-. Pronominal stem. 1. Germanic *is-lik-, same (*lik-, like; see lik-), in Old English ilca, same: ILK. 2. Germanic *jaino-, *jeno-, in Old English geon, that: Yon. 3. Ger- manic *jend- in Old English geond, as far as, yonder: YOND, (YONDER). 4. Extended forms *ydm, *ydi, in Ger- manic */d, *jai, in Old English géa, affirmative particle, and gése, yes (see es-): YEA, YES. 5. Old English giet, gieta (preform uncertain), still: yET. 6. Old English gif (preform uncertain), if: 1F. 7. Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same: 1D, IDEM, (IDENTICAL), IDENTITY; (IDENTIFY). 8. Suffixed form *i-tero- in Latin iterum, again: ITERATE; (REITER- ATE). 9. Suffixed and extended form ‘*iéa)-em in Latin item, thus, also: ITEM. 10. Suffixed variant form *e-tero- (see ko-). [Pok. 3. e- 281.]
=== search identity/item/etc
366:diphthera, prepared hide, leather (used to write on): DIPHTHERIA. 2. Latin littera, letter (possibly borrowed from Greek diphthera in the sense of “tablet” via Etrus- can): LETTER, LITERAL, LITERARY, LITERATE, LITERA- TIM; (ALLITERATE), ALLITERATION, (ILLITERATE), OBLITERATE, TRANSLITERATE. [Pok. deph- 203.] der-', Assumed base of roots meaning “to run, walk, step.” 1. Zero-grade form “dr- in extended Germanic form “*tred- in: a. Old English tredan, to step: TREAD, TREADLE; b. Middle Low German trade, course, track: TRADE. 2. Extended form *dreb- in Germanic *frep-, “something on or into which one steps,” in: a. Old English treppe, treppe, snare: TRAP; b. Middle Low German trappe, stair: TRAP’, c. Middle Dutch trappe, stair: WENTLETRAP; d. Old French trap(pje, snare: EN- TRAP; @. Middle Dutch érippen, to stamp, trample: TRIP. 3. Nasalized Germanic root *tremp- in: a. Middle Low German trampen, to stamp, tread: TRAMP; b. Italian trampoli, stilts: TRAMPOLINE. 4. Germanic *iérott- (ex- pressive derivative of *tred-) in Old French ¢roter, to trot: TROT. 5. Root form *drd- possibly in reduplicated Germanic form *ti-trd- in Old Norse titra, to tremble: TEETER. 6. Root form *drem- in suffixed o-grade form *drom-o- in: a. Greek dromos, a running, race, race- course: -DROME, DROMOND, -DROMOUS; ANADROMOUS, LOXODROMIC, PALINDROME, PRODROME; b. Greek dro- mas, running: DROMEDARY. [Pok. 3. (der-) 204.] der-2, To split, peel, flay; with derivatives referring to skin and leather. 1. Germanic *teran in Old English teran, to tear: TEAR}. 2. Germanic *ter-t- in Old English teart, sharp, severe: TART). 3. Suffixed zero-grade form *dr-tom, “‘something separated or discarded,” in Ger- manic *turdam, turd, in Old English tord, turd: TURD. 4. Reduplicated form *de-dr-u- in Old English teée)r, eruption, skin disease: TETTER. 5. Greek derris, leather covering: DERRIS. 6. Suffixed form *der-mn in Greek derma, skin: -DERM, DERMA!, -DERMA, DERMATO-; EPI- DERMIS. 7. Perhaps extended root *drep- in the Celtic source (itself borrowed) of Late Latin drappus, cloth (> Old French drap): (DRAB!), DRAPE, TRAP?. [Pok. 4. der- 206.) derbh-. To wind, compress. Zero-grade form “drbh- in Germanic *turb- in: a. Old English turf, slab of sod or peat: TURF; b. Medieval Latin turba, turf: TURBARY. [Pok. derbh- 211.] dere-. To work. Variant form *drd- (< *draa-) in Greek dran, to do: DRAMA, DRASTIC. [Pok. dero- 212.] dergh-. To grasp. 1. Perhaps Germanic *targ- in Old French targe, shield: (TARGE), TARGET. 2. Perhaps zero-grade form *drgh- in Greek drassesthai, to grab (> drakhmé, “handful,” drachma): DRACHMA. [Pok. dergh- 212.] derk-. To see. Suffixed zero-grade form *drk-on(t)- in Greek drakén (> Latin dracé), serpent, dragon (< “mon- ster with the evil eye”): DRAGON, (DRAGOON), (DRAKE?2), RANKLE. [Pok. derk- 213.] deru. Also dreu-. To be firm, solid, steadfast; hence specialized senses “wood,” “tree,” and derivatives refer- ring to objects made of wood. 1. Suffixed variant form *drew-o- in: a. Germanic *trewam in Old English tréow, tree: TREE; b. Germanic *freuw6 in Old English tréow, pledge: TRUCE. 2. Variant form *dreu- in Germanic *treuwaz in: a. Old English tréowe, firm, true; TRUE; b. Old English tréowian, triiwian, to trust: TROW; c. Old Norse tryggr, firm, true: TRIG!; d. Germanic abstract noun *treuwithé in Old English tréowth (> Middle English tro(u)the), faith, loyalty, truth: TROTH, TRUTH; BETROTH; @. Germanic abstract noun *traustam in Old Norse traust, confidence, firmness: TRUST; f. Old Norse denominative treysta, to trust, make firm, akin to the probable source of Old French triste, waiting place (< “place where one waits trustingly”): TRYST. 3. Variant form “drou- in Germanic *traujam in Old English trég, trig, wooden board: TRAY. 4. Suffixed zero-grade form
463:eti. Above, beyond. 1. Germanic *ith- in Old Norse idha, whirlpool: EDDY. 2. Latin et, and (< “furthermore”): ET CETERA. [Pok. efi 344.]
559:i-. Pronominal stem. 1. Germanic *is-lik-, same (*lik-, like; see lik-), in Old English ilca, same: ILK. 2. Germanic *jaino-, *jeno-, in Old English geon, that: Yon. 3. Ger- manic *jend- in Old English geond, as far as, yonder: YOND, (YONDER). 4. Extended forms *ydm, *ydi, in Ger- manic */d, *jai, in Old English géa, affirmative particle, and gése, yes (see es-): YEA, YES. 5. Old English giet, gieta (preform uncertain), still: yET. 6. Old English gif (preform uncertain), if: 1F. 7. Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same: 1D, IDEM, (IDENTICAL), IDENTITY; (IDENTIFY). 8. Suffixed form *i-tero- in Latin iterum, again: ITERATE; (REITER- ATE). 9. Suffixed and extended form ‘*iéa)-em in Latin item, thus, also: ITEM. 10. Suffixed variant form *e-tero- (see ko-). [Pok. 3. e- 281.]
642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
1229:ALLEGE ag-, leg-1 ALLEGORY al-!, ger-1 ALLELOMORPH al-1 ALLERGY werg- ALLEVIATE legh- ALLEY! al-2 ALLIGATOR al-1 ALLITERATE deph- ALLITERATION deph- ALLO- al-1 ALLOCUTION tolkw- ALLOMERISM (s)mer-2 ALLOPATRIC  peter- ALLOT kleu-3 ALLOY leig-1 ALLUDE |leid- ALLUVION leu(e)-
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1693:ITEM I-
1694:ITERATE I- ITHYPHALLIC bhel-2 ITINERANT ei-1 ITINERARY el-1 Iwis_ weid-
1755:LITERAL deph- LITERARY deph- LITERATE deph-
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
2402:TRANSIENT ei-1, tera-2 TRANSIT ei-1 TRANSITIVE ei-1 TRANSLATE tele- TRANSLITERATE deph- TRANSLUCENT leuk- TRANSMIT (s)meit(@)- TRANSMUTE mei-1 TRANSOM tere-2 TRANSPIRE § spirare TRANSPONTINE pent- TRANSPORT per-2 TRANSUDE sweid-2 TRANSVERSE wer-3 TRAP! der-1
```


## [2026-09-06T15:16:58.638Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^et cetera\\|^etc\\b\\|c[eē]terus\" KLN_1966.txt | head -20; echo \"=== awk leaf 284\"; awk 'BEGIN{RS=\"\\f\"} NR==284 || NR==285' KLN_1966.txt | grep -n -i \"cetera\\|ceterus\\|atara\\|at-zur\" | head"
}
```


### [2026-09-06T15:17:00.288Z] TOOL RESULT

```
18251:etc.),  and  in  L.  decern,  ‘ten’,  which  stands  for *(d)kmtom );  see  decad,  decimal,  ten.  Accord¬ ingly  hundred  prop,  means  ‘the  great  ten’.  Cp. cent,  centenary,  century,  hecatomb,  sotnia.  Cp. also  the  second  element  in  thousand. Derivatives:  hundred,  adj.,  hundreder  (q.v.), hundred-fold,  adj.,  hundreth  (q.v.) hundreder,  hundredor,  n.,  the  chief  officer  of  a hundred  (hist.)  —  ML.  hundreddrius.  See  hun¬ dred  and  -er  (representing  L.  -arius). hundredth,  adj.  and  n.  —  Formed  fr.  hundred  with numeral  suff.  -th.
=== awk leaf 284
```


## [2026-09-06T15:17:04.127Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" KLN_1966.txt; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nprint('leaves',t.count('\\f'))\nimport re\nfor m in re.finditer(r'cetera',t,re.I):\n    print(t[m.start()-300:m.start()+300].replace('\\n',' '))\n    print('-----')\nEOF"
}
```


### [2026-09-06T15:17:05.884Z] TOOL RESULT

```
41263
leaves 902
 there  re¬ ferred  to. etatism,  n.,  state  socialism.  —  F.  etatisme,  formed fr.  etat,  ‘state’,  with  suff.  -isme.  See  prec.  word and  -ism. Etat  Major,  the  staff  of  the  army.  —  F.  etat- major,  fr.  etat,  ‘state’,  and  L.  major,  ‘greater’. See  etat  and  major,  adj. et  cetera,  ‘and  other  things’.  —  L.,  fr.  et,  ‘and’ (see  et),  and  neut.  of  ceteri,  ‘the  others’,  which is  formed  fr.  I.-E.  pron.  pref.  *ce-,  ‘there;  behold’ (see  he),  and  I.-E.  *etero-,  ‘the  other’,  whence also  Umbr.  etro-,  ‘another’,  Avestic  a-tara-, ‘one  of  the  t
-----
is  day’,  fr.  I.-E.  *kyo-,  ‘this’,  and  Gk.  zjpipa, ‘day’),  L.  cis,  citer,  citra,  ‘on  this  side’,  ce-  and -ce,  emphatic  particles  meaning  ‘here,  there’, OSIav.  si,  Lith.  sis,  ‘this’.  Cp.  him,  her,  it,  hence, here,  hither.  Cp.  also  cede,  cis-,  citra-,  cy-pres, et  cetera,  hodiernal,  sic. he,  n.,  name  of  the  5th  letter  of  the  Hebrew  al¬ phabet.  —  Heb.  he,  probably  meaning  ‘lattice window’. head,  n.  —  ME.  heved,  hed,  fr.  OE.  heafod,  rel. to  OS.  hot) id,  ON.  hofud,  Dan.  hoved,  Swed. huvud,  OFris.  haved,  hafd,  MDu.  ho  vet,
-----
```


## [2026-09-06T15:17:12.333Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\ni=t.lower().find('et  cetera,  ‘and  other  things’')\nprint(t[i-100:i+1200])\n# page/leaf\nprint('LEAF', t[:i].count('\\f'))\nEOF"
}
```


### [2026-09-06T15:17:14.372Z] TOOL RESULT

```
—  F.  etat- major,  fr.  etat,  ‘state’,  and  L.  major,  ‘greater’. See  etat  and  major,  adj. et  cetera,  ‘and  other  things’.  —  L.,  fr.  et,  ‘and’ (see  et),  and  neut.  of  ceteri,  ‘the  others’,  which is  formed  fr.  I.-E.  pron.  pref.  *ce-,  ‘there;  behold’ (see  he),  and  I.-E.  *etero-,  ‘the  other’,  whence also  Umbr.  etro-,  ‘another’,  Avestic  a-tara-, ‘one  of  the  two,  this’,  Alb.  jatere,  jatre,  ‘the other’,  OSlav.  jeteru,  iteru,  ‘some,  one’, etch,  tr.  and  intr.  v.,  to  engrave  with  acid.  —  Du. etsen,  ‘to  etch’,  fr.  G.  atzen,  ‘to  corrode’,  fr. MHG.  atzen,  etzen,  fr.  OHG.  azzon,  prop,  ‘to feed,  bait’,  causative  of  e$$an,  ‘to  eat’.  See  eat. Derivatives:  etch,  n.,  etch-er,  n.,  etch-ing,  ver¬ bal  n.
Eteocles,  n.,  son  of  Oedipus  and  Jocasta,  and king  of  Thebes  (Greek  mythology ).  —  L.,  fr. Gk.  ’ExeoxXi;?,  lit.  ‘of  true  fame’,  compounded of  izzoq,  ‘true,  real,  genuine’,  and  vXloq,  ‘fame’. The  first  element  is  rel.  to  £xupo<;,  ‘true’;  see etymon.  The  second  element  is  rel.  to  xXot6;, ‘famous’,  and  cogn.  with  L.  in-clutus,  in-clytus, of  s.m.,  OE.,  OS.  htiid,  ‘loud’.  See  loud, eternal,  adj.  — -  L.  aeternalis,  fr.  aeternus,  ‘ever¬ lasting,  eter
LEAF 296
```


## [2026-09-06T15:17:26.600Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (294,295,296,297):\n    L=leaves[n]\n    print('==LEAF',n, repr(L[:200]))\n    print('   TAIL', repr(L[-150:]))\nEOF"
}
```


### [2026-09-06T15:17:28.650Z] TOOL RESULT

```
==LEAF 294 'a).  See  -er,  suff.  denoting  connectedness, and  -y  (representing  OF.  or  F.  -ie)  and  cp.  -ry. Eryngium,  n.,  a  genus  of  plants  (bot.)  —  ModL., fr.  Gk.  TjpuyYtov,  dimin.  of  ^pu-'
   TAIL ' —  ModL., fr.  Gk.  -701;,  formed  fr.  e-stem  verbs.  Cp.  -asis, -osis,  -iasis.\neskar,  esker,  n.,  deposit  left  by  a  subglacial stream  (g'
==LEAF 295 'eol.)  —  Tr.  eiscir,  ‘a  ridge’.\nEskimo,  n.  and  adj.  —  N.  American  Indian eskimantsik,  ‘caters  of  raw  flesh’,  a  name  given by  the  Algonquians  to  the  N.  American  Indian tribes  '
   TAIL 'e’,  which  is  denominated  fr.  *ais- temos,  lit.  ‘one  who  cuts  the  ore’,  fr.  aes,  gen. aeris,  ‘ore’,  and  I.-E.  base  *tem-,  ‘to  cut’'
==LEAF 296 ',  whence also  Gk.  T^nveiv,  ‘to  cut’.  For  the  first  element see  ore,  for  the  second  see  tome.\nDerivative:  esteem,  n.\nEstella,  fern.  PN.  —  Sp.,  lit.  ‘star’,  fr.  L.  Stella, See '
   TAIL 'also  next  word. Derivatives:  eternal-ly,  adv.,  eternal-ness,  n. eterne,  adj.,  eternal  (poetic).  —  OF.,  fr.  L.  aeter¬ nus.  See  eternal.'
==LEAF 297 '\neternity,  n.  —  ME.  eternite,  fr.  F.  eternite,  fr.  L. aeternitatem,  acc.  of  aeternitas,  fr.  aeternus. See  eternal  and  -ity.\neternize,  tr.  v.,  to  render  eternal.  —  F.  eterniser'
   TAIL '  L.  Etruria,  a  name  of  uncertain etymology.\nEtruscan,  adj.  and  n.  —  Formed  with  suff.  -an  fr. L.  Etruscus,  ‘Etruscan’,  fr.  Etruria.'
```


## [2026-09-06T15:17:43.773Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor n in (178,284,438,393):\n    print('==LEAF',n, repr(leaves[n][:160]))\nEOF"
}
```


### [2026-09-06T15:17:46.054Z] TOOL RESULT

```
903
==LEAF 178 ' coeno-).  Cp.  1st  con-,  contra-, count,  ‘title  of  nobility’.  Cp.  also  y-. coma,  n.,  a  state  of  insensibility.  —  ModL.,  fr. Gk.  xolpta,  ‘a  d'
==LEAF 284 's).  According to  the  opinion  of  several  scholars  Endymion  was orig.  worshiped  as  a  solar  deity  and  his  name is  a  personification  of  the  Set'
==LEAF 438 ' —  ModL.,  fr.  Gk.  eEpeauovr),  ‘a wreath  of  olive  wound  round  with  wool’,  fr. slpo q,  ‘wool’,  which  is  rel.  to  gpiov,  ‘wool’  (see erio-) ;  s'
==LEAF 393 'cy.  —  See  prec.  word and  -ic,  resp.  also  -al.\nhierodule,  n.,  a  temple  slave  in  ancient  Greece.  — Late  L.  hierodulus,  fr.  Gk.  Eep68ouXo?,  l'
```


## [2026-09-06T15:17:56.710Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nleaves=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nfor n in range(0,903,25):\n    s=' '.join(leaves[n].split())[:60]\n    print(n, s)\nEOF"
}
```


### [2026-09-06T15:17:58.692Z] TOOL RESULT

```
0 A COMPREHENSIVE ETYMOLOGICAL DICTIONARY OF THE ENGLISH LANGU
25 is formed fr. ad- and ire, ‘to go’, fr. I.-E. base *ei-, •/-
50 ��to go round’. See ambient, andantino, adj., somewhat quick
75 erivative: atavistic-al-ly, adv. ataxia, n., irregularity of
100 ��, fr. beurre, ‘butter’. See prec. word. bevel, n., inclina
125 cabalist, n., a student of cabala. — A hybrid formed fr. cab
150 ��one who speaks (in a certain manner) ; one who deals (with
175 uff. -ite. coleo-, before a vowel cole-, combining form mean
200 ’. See quince. cotrustee, n., a joint trustee. — Formed fr. 
225 ]?, compounded of 8£xa, ‘ten’, and -ap/t]?, ft- apx'k, ‘lead
250 iculate, v. Derivative: disarticulat-ion, n. disassociate, t
275 h. A ok at, B okt. Arm. ut‘ (for *optd ), Gk. oxtoj, Alb. te
300 idnem, acc. of evacuatio, ‘an evacuating’, fr. L. evacuatus,
325 49-1919), who advocated this practice. For the ending see su
350 t, race’. See genns and verbal suff. -ate and cp. gender, v.
375 fice, expiation’, ayitjeiv, ‘to hallow’, ayv6i;, ‘holy, chas
400 — L. Horatius (see Horace); influenced in form by It. Orazio
425 ggle out of, to surmount’, fr. e- and luctari, ‘to struggle,
450 o gau- dere, ‘to rejoice'. See gaud and cp. enjoy. Cp. also 
475 ��to flow’. See -rrhea. Leucothoe, n., the daughter of Orcha
500 Yakut mamma , ‘earth’ (the mammoth was believed to root up t
525 ere referred to. midst, n. — ME. middest, midest, formed wit
550 B hem, Hitt, laman (formed with dissim¬ ilation fr. *naman),
575 OHG. ort, ‘point (esp. of a weapon or a tool), angle, edge, 
600 apilion-aceous, adj. Papilionidae, n. pi., name of a family 
625 , n. Pharisaism, n. — ModL. Pharisaismus, fr. Gk. Oapioato?,
650 , fr. L. porca (for *prkd), ‘ridge between furrows’, which i
675 Pteridin, coined fr. pter-, -ide and chem. suff. -ine ; so c
700 r. L. recuperatus, pp. of recuperare. See recuperate and -iv
725 to read, ‘red’. See red and cp. rudd, the fish, ruddle, rudd
750 hol, n., name of the Heb. -Aram, vowel sign ’.' — Aram. s(gh
775 fr. Du. slof ‘careless’, and ME. suff. -ein, -eyn, fr. OF. -
800 ic and -ics. statistology, n., the study of statistics. — A 
825 s there referred to. Cp. also monosyllable, dissyllable, tri
850 nimal’, and av-9-pcd7ro(;, ‘man’. See therio- and anthropo-.
875 gonometric, trigonometr-ic-al, adjs. trigonous, adj., having
900 r’, vojina, ‘war’, Gk. iep.ai (for ‘I as¬ pire to, tend to,
```


## [2026-09-06T15:18:31.138Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nimport re\ndef show(pat,n=1,w=700):\n    for m in list(re.finditer(pat,t))[:n]:\n        leaf=t[:m.start()].count('\\f')\n        print('### PAT',pat,'LEAF',leaf)\n        print(' '.join(t[m.start()-50:m.start()+w].split()))\n        print()\nshow(r'\\nitem,')\nshow(r'\\niterate,')\nshow(r'\\nidentity,')\nshow(r'\\nyes,')\nshow(r'\\nyet,')\nEOF"
}
```


### [2026-09-06T15:18:32.922Z] TOOL RESULT

```
### PAT \nitem, LEAF 443
nd cp. esp. the second element in Stomoisia. item, adv., likewise. — L., ‘just so, in like man¬ ner, likewise, also’, rel. to ita, ‘so’, itaque, ‘and so, accordingly, in like manner’, itidem, ‘so, just, in like manner’, idem (masc.), idem (neut.), ‘the same’. See idem and words there referred to and cp. esp. iterate. Derivatives: item, n. (q.v.), item, tr. v., item¬ ize, tr. v. item, n., detail; article. — L. item, ‘likewise’; see prec. word. The sense of the English noun arose from the circumstance that the word item was generally used to introduce all the sections of a bill, except the first, iterance, iterancy, n., the quality of being iteran
```


## [2026-09-06T15:18:42.001Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nimport re\nfor pat in [r'idem,\\s+adj', r'identity', r'Avestic\\s+i-tha', r'Avestic\\s+itha', r'\\bitha\\b', r'yes,\\s+adv', r'yet,\\s+adv', r'\\bif,\\s+conj']:\n    ms=list(re.finditer(pat,t))\n    print('PAT',pat,'hits',len(ms))\n    for m in ms[:2]:\n        leaf=t[:m.start()].count('\\f')\n        print('  LEAF',leaf,':',' '.join(t[m.start()-200:m.start()+800].split()))\n    print()\nEOF"
}
```


### [2026-09-06T15:18:44.399Z] TOOL RESULT

```
PAT idem,\s+adj hits 0

PAT identity hits 12
  LEAF 81 : . hayih, imper. sing. masc. of Phoen. -Punic hawd, resp. Heb. hdydf‘, ‘he lived'. Cp. Plautus, Poenulus, 994, 998, tool, and see Walde-Hof- mann, LEW., I, pp. 80-8 1 . — The identity of the 133 aviary Semitic bases h-w-h (h-w-') and h-y-h is illustrat¬ ed in Gen. 3 : 20, ‘And the man called his wife’s name Eve (Hawwdh), because she was the mother of all living (hay)'. See Eve. For sense de¬ velopment cp. Heb. yehi ddhdnt hammelekh Dciwidh I'o/dm: ‘Let my lord king David live for ever!’ (1 Kings 1:31; cp. Dan. 2:4 and passim), E. ‘Long live the King!’, F. ‘Vive le roi’, etc., all used as formulas of greeting. (The origin of L. ave being thus established, we shall be able to find the exact meaning of the words with which the gladiators greeted the emperor: ‘Ave, Imperator, morituri te salutant� �� (see Suetonius, Claudius 2 1). The usual rendering is: ‘Hail, E
  LEAF 410 : . ibex, ‘a kind of goat, chamois’, loan word fr. an I.-E. language spoken in the Alps, ibidem, adv., in the same place. — L., formed fr. ibi, ‘there’, and the particle of identity -Jem. The adv. ibi is rel. to Umbr. ife, ‘there, thither’, and cogn. withOI. i-hd, Avestic iSa, ‘here’, Gk. E&ayevfj?, ‘native, lawfully begotten, legitimate’ -ibility (lit. ‘here born’). All these words derive fr. I.-E. *i-dha, *i-dhe, from the pronominal base *i- ; see idem and cp. the second element in alibi; cp. also ubiety. The particle -dem in ibidem derives fr. I.-E. *dl; see de- and cp. tandem. -ibility, subst. suff. expressing ability, capacity, fitness. — L. - tbilitas , forming nouns from ad¬ jectives ending in -tbilis. See -ible and -ity and cp. -ability. ibis, n., a large wading bird. ■ — L. ibis, fr. Gk. Ifk?, fr. Egypt, hib. -ible, adj. suff. expressing ability, capacity

PAT Avestic\s+i-tha hits 0

PAT Avestic\s+itha hits 0

PAT \bitha\b hits 0

PAT yes,\s+adv hits 0

PAT yet,\s+adv hits 0

PAT \bif,\s+conj hits 1
  LEAF 413 : , etc.; 2) added to English words as in glazier, graizier, hosier, etc. See -ary and -eer and cp. -yer. Suff. -ier is of the same origin and meaning as agential suff. -er. if, conj. — ME. gif, if, fr. OE. gif, rel. to OS. ef ON. ef if, OFris. gef ef, iefi ‘if’, OHG. ibu, uba, oba, ‘if’, MHG. oba, ob , G. ob, Du. of if, whether’, Goth, ibai (interrogative particle). All these conjunctions are prob. traceable to the dative of a noun meaning ‘doubt’, and orig. meant ‘on condition that’. (Cp. ON. if, ‘doubt’, OHG. iba, ‘doubt, condition’.) igloo, iglu, n., a snowhut. — Eskimo igdlu, ‘snowhouse’. Ignatius, masc. PN. — L. Ignatius, a collateral form of Egnatius. Gk. Tyva-rioi; is borrowed from Latin. Cp. Inigo. igneous, adj., fiery. — L. igneus, ‘of fire, fiery’, fr. ignis, ‘fire’, which is cogn. with OI. agnih, OSlav. ogni, Lith. ugnis, Lett, uguns, ‘fire’. Cp
```


## [2026-09-06T15:18:56.425Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==54' HRN.txt | head -60"
}
```


### [2026-09-06T15:18:58.326Z] TOOL RESULT

```
— 32 —
öi und vei sind im Neupersischen zwei Doubletten
ohne jede Bedeutungsnüance ; vei wird dann auch im
Sinne des lat. -plex verwendet.
öweste (nnoziN) siehe unter pest (No. 316).
137. 7? 'dieser in Ider *hier, Jdrä (unbelegt), tderi (Näs.
Xosr.), erä 'desshalb*, edün, Uün (Kasan: etün s. v.
häla) so', Im jetzt', Ime jetzt', esän 'diese' ^).
Tat. i 'dieser'; mäz. ai; Käs. l (kann m mit Verlust
des Nasals sein), e\zün (= tu sän) s. v. cunin,
ap. ai'ta- 'dieser'; aw. ae-m-, ae4ad; phlv. e, ecand
(vd. 7 (27) 61., Var. WH-cawrf; Ganj-I ääyagän 1),
etar^ etün, päz. ercf, ^säw; ai. e-sa-, e-^arf.
kurd. ai 'dieser, ijsäl; oss. a«/; bei. e, f (170).
Auf a/-^a- wird auch das sog. yäi isäret oder
yäi t'arif zurückgeführt (Salemann-Shukovski,
Neup. Grammatik § 19); doch scheint es mir besser,
dasselbe mit dem e des unbestimmten Artikels (yäi
validet) zu identificiren, wie dies nach mündlicher Mit-
teilung Prof. Nöldeke's schon vor Jahren Ewald
gethan hat.
138. ei 'o!'
aw. äi o!'; phlv. ai (vd. 19 (32); N:n vd. 18 (48));
skr. di.
139. ec jemand, etwas', s. hec (No. 1114).
140. Irmän {*er?nan^) 'Gast'^).
aw. airyaman- N. pr. eines Genius; phlv. ermän^
ermänik^ ermämh (Aw.-Komm.); ai. aryamän- 'Busen-
freund, Kamerad'.
Wenn aw. "^a^d^ra- wirklich einmal Teuer' bedeutet
») Fr. Müller (WZKM. 5, 185) will np. esän auf es\än d. i.
aw. aßsqm-\-än zurückführen.
*) Auch die indische Aussprache lautet irmän statt ermän,
wie zu erwarten wäre. Im Allgemeinen werden im indischen
Persisch die Majhlilvokale in den Worten richtig sein, in denen sie
sich erhalten haben, doch yersagt die indische Tradition auch in
vielen Fällen.
^) Vergl. Spiegel, Arische Periode, 103; die Bedeutung *Diener*
ist mir zweifelhaft.
```


## [2026-09-06T15:19:14.450Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='BQT_v1_pages.txt'\nleaves=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(leaves))\nfor n in range(410,420):\n    L=leaves[n]\n    print('==LEAF',n,'==')\n    print(L[:600])\nEOF"
}
```


### [2026-09-06T15:19:16.108Z] TOOL RESULT

```
777
==LEAF 410 ==
اهزون
اهز ون - ختح اول بر وذن محزون »
بازاینده و متروترا گوبند وحربی عقیمه‌خوانند .
اهلث « بروزن مك . آحك را گویشه
و حربی کلس و نوره خواشد .
انامه - بر وزن شهنامه . بمعنی کر
وفر وخودآرابی و خودنمابی - و دولتسوعشق-
و رسوابی باشد - و عرچیزیرا نیز گوبند که زود
از دست برود واز اشفاع باژ ماند و شکسته‌شود .
" آهنوخوشی ۴ - بنتح اود وسکون
شانی و ضم نون و واو ساکن و خای نقطه دار
. مفتوح و واو محدوله وشین فرشت بتحتانی‌رسیده»
اهل حرفت را گویند. واین چهارم قسم است از
افسام مردم که جمشید قرار داده بود و آن چنان
ایت که جمشید طوایف انام را برچهارفم کرد :
اول راکاتوزی ۴ نامیدو فرمود که در کوهها وغار
ها ععق کن
==LEAF 411 ==
۱ اهور * - بنتع اول و ثالث و سکون
ثانی و زای نقطمدار ۰ نلم تیرآندازی بوده بفایت
قادرانداز در زمان انوشیروان » کوبند باسیف ذو
بزن (۱) همراه شده بود . بادشاه حبشهرابيك‌تبر
بر روی نخت کشت و ملکش راگرفت .
اهون - بفتح اول وثانی بواو رسیده
و ون زده ۰ مخف آحون است که رخنهة کوه
و غار و امثال آن باشد ۷ .
اهون بر < بننم بای ابجدوسکون‌رای
قرشت . نقب‌زننده و چام‌جوی را گوینه و بعربی
نغاب خوانند, و بضم بای‌ابجد هم آعده‌است ۷
اهیا نه عه با بای حطی بروزن شهدانه.
اهود - بروزن رهبر . ممنوقومطلوب | مخفف آخیانه است که شفیقه وکاسة سر-ودماغ.
را کونند . ۶ و حلفوم بلشد ۵ .
نمی پذیرد .
اهنو3 ۲ - بنتم اول و تاك و دابع
==LEAF 412 ==
ابا
جه 0 ده
ایا - بختح اول و ثالیبالف کشیده .بمعنی
و کاهی‌درمقام حسرت‌وافوی هم استعمال مشود .
ایاد - بروزن بهار . نام ماه سیم بهار
است ازمامرومیان » وبودن آفتاب در برججوزا-
و ترجه حساب هم هست چه ابار گیر محاسب
و حماب گیرنده را گونند ۲
ایارده ۴ » بکر اود و رایع و فتح
دال ایجد . یر وچگونگی کتاب زند (۱)است
بملت مفان؟ بعنی آتش‌پرستان,بنی آنرا کتاب
- اباشاه عحمود کشوز گشای
آسمانی میداننده و شثح اول وسکون رایع عم
ایاده - بروزن شراره . بنعنی باوهباشد
که دست برنجن است و آن حلقه‌ای بود ارطلا
وشرمو غیر آن که زدان در دستء با ی کنند ۵ -
و دفتر وحسایی را نز گویند که زر های‌پرا کند*
دیرانیرا در آن نوسند و م
==LEAF 413 ==
۱۳ات ایدغ
ایاره گیر ۱ -بر وزن کنار هگیر ».
محاسب و نوبسنده را گویند .
ایاد ۴ ه بر وزن نماز , دام غلام تراد
سلطان محمود غز نوی بوده -
ابادي - بررزن لمازی » برقع سیاعی
ست که زنان بریشت چشم بندند ۴ .
" ایا ؟ « بروزن ممای » بمعنی ایاز
است که نام غلام سلطان محمود باشد .
ایاسه « بفتم اول و رایع ۰ بمعت یآرزو
و اثتیاق باشد - و حلقه و فلايی را نیز کوبند
که حلفه را بر نوار بهن نصب کرده باشند و سد
از بار کردن آن نوار رابربالای بار اندازندوقلاب
ایاسی « بروزن خلاصی . بمعنی آبازی
باشد که نوعی از برقع سیاه است که زنان بر
روی کشند ؟ .
اباع* - بر وزن دساغ » کاسه وییاله
شرایخوری را گویند .
اثیك ه با بای ابب‌دیر
==LEAF 414 ==
ایا - بروزن وممنی زبرا و ازبرای‌آن
و از ایشجهت باشد .
ایر اف ۴ - بکر اود و سکون ثانی
و ثالث بالف کشده ویفای زده ۰ نام عدر اردااست
که پارسیان‌اورا پیعمبر
میدانتها ند و
ابسر آن ٩‏ -
بر وزن ببران . نام
هوشنگ ین سيامك
باشد - و ولاسته عرای
| بد‌ماهید - با عیم بالف کشده بروزث
مرخرامد» بلفت سر‌بانی درختی است که بدن‌آن
مانندیشم است» وخاصیت‌ریآ نس ت که شکم ,بندد.
اف فا بکراولبروزن بی‌بند »یممنی
اند است وآن عددی باشد مجهول که بده ؛, سد»
و آنرا بعربی بضم خوانند ۱ .
ایدون ؟ « بفتح اول ؛ بروزن «مسنی
اکنون است که این زمانرالحال باشد - وبکسر
اول بمعنی. اشجنین و اینجا و این زمان وایشدم
و این ساعت بود ‏
ایدی «
==LEAF 415 ==
وه آبرسا
اول نیشاپور است ۷ . از پادشاهان بابل هم بوده است
ار ج ‏ بکسراول و سکون ثانی‌مجهول الیرسا « بکس اول و سکون انیوثاك
و #الك مقتوح بجیم زده ؛ نام پس فربدون است | و سین بی‌فقطٌبالف کشیده » بیونانی ۴ قوس‌رفزح
توا فلك آفتاب را یز کویند؟ . - وناییکی را کوبند وفام یخ‌سوسن ۴ آسمان کون هم‌هست
سس ۰اه
٩‏ پهلوی 50205 - 8640 . شتر(< شهر) بسمنی کشور ومملکت بوده که بمدها از وسمت
مفپوم آنکاسته شده واین‌لفت م رکب‌بدمنی مملکت ابران استممال شده. راد: شمارٌ هفت وهفت
کر نظامی بقلم ۳ از و هت ؛ یاقوت در ممجم اللان گوید : بلاذری گوید : خرا-ان
دارای چهار ربم است : ربع اول ابران‌شهپر است و آن شامل‌ییثابور و فهتا
==LEAF 416 ==
و چون کل آن زرد و سفیدو کبود میباشدبنایر
آن ایرسا نامیده‌اند چه شبیه بقوی‌فزح است .
بیوایی ٩‏ طلق و زر ورق دا کوبند و بثیرازی
برقك خوانند .
ایر قان - با قاف بروزن میهمان .بلغت
روغی حنا را کوبتد و آن ب رکه درختی باشد که
" یکوبند و خمی رکنند و بردست و پای بندند .
"فر گه ه یک اولو سکون تانی‌وئاك
و کاف‌فارسی » بلفت زند وپازند )٩(‏ بمعنی مردم
باشد چه ابر گان مردمانر| کوبند ۴ . ۱
ار گان - باکاف‌فارسی بروزن‌میهمان,
بلت‌زند و پازند (۱)بممنی مردمان با دکهجمع
مردم است ؟ .
ایرمان ؟ » بروژن و هعتی‌میهمان‌است
اما میهمان طفیلی که برفافت باران و دوسثان
یجایی برند با خرد بی آنکه اورا طلبیده باشند
پرود - و شخص
==LEAF 417 ==
ایقفه ه با فا بررزن و معلی ابفده‌است
که بهوده گو و سبکار باشد که حرزه چانه
۱9۳۳
اون بکر او وسکون انی وفاف
بواو وسیده و بنون زده ؛ بلفت رومي کلی است
بغات بدیوی و کنده و بعربی‌وردالمنتن‌خوانند .
رنگ آن برنگ گل سرخ ماند .
ابگ ب بکسراول وسکون ثانی و کاف
فارسی » ولاتی است است از ولابات فارسی 6
ایگ بادن هایگ معلوم. و بای ایجد
پالف کشیده و واو مفتوح بنون زده » نام کتابی
است در مذحب فان و ار ان درتتانن موباین
معنی‌بجای بای ایجد میم وبجای واو دال هم‌بنظر
آمده است وافاعلم 9
ایگر - بفتح اول و سکون انی و کاف
فارسی مغنوح بر‌ای فرشت‌زده ۰ درامی‌است که به
اکر شپرت دارد و عربی وج و بیونانی افارون
خوانند . سقی
==LEAF 418 ==
ابلا
ومردمان و جماعت را نیز گویند - وهیل را هم
مبگوبند که له صفارباشد - و بکر اولوفتح
انی مشدد گا و کوهی باشد . گوشد چون سمار
شود بیتی خود را برسوراخ مارنهد و بنفم. مار
را بجاب خود کشد چنانکه مقناطیس آهن را ,
چون مار را بخورد شفا بابد » و بعربی‌بقرالوحش
خوانند ؛ و بضی کویند اب لکوسفند کوهی است
وخون او علاج کی‌است که زهربوی داده‌باشند,
و نم اول هم کفته‌اند
از تر کستان .
یلاق - بروزن قیماق » نام شهربست‌از
ختا (۱) و فلماق ۴ - و نامدرختی هم‌هست ۰۴
ا یلاوس « یک اول وضم واووسکون
سین‌بی‌قطه ۰ بلفت یونالی ۴ قسمی‌از قولنج‌است
و آن مهلك میباشد .
ابلاو ل بفتح اول و کر واو بروزن
جربادل , نام کوهی است و کو
==LEAF 419 ==
دنق
و نام ییت النفدس هم‌هست - وبسینی کوبند تام
عبت ان رت رادم کر از
فتحهایعبرخطاب. ومعنی آن‌سدیق اکبرباشد.
ایم « بروزن جیم » مردی را گوبند که
زنش مرده باشد ۱ .
) ثمد ‌ِ بروژن‌ایسد .کاوآهن‌را گوبنده
و آن اعنی است که زمین را بدان شدبار کنند
و بمتی کویند ایمد چوبی است که کاو آهن‌رابر
آن صب کنند و زمین را بنافند و آنراجربی
سنه خوانند ؟ .
اهر - بنتح اول بر وزن خنجر , آهن
سرنیزی را کوبند که‌برچوب قلبه‌صب کنندوبدان
زمین را ثبار کنند » و بکسر اول عم آعده
ت 9
ایمه - بفتح‌اول بروزن خیمه » بمعنی
اکنون و این دم باشد - وهرزه و یاوه وییهوده
را لیز کویند - و بکس اول بمعنی اینچنین
وهمجنین است 9
اینت ‏ بکسر او
```


## [2026-09-06T15:19:25.988Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nleaves=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor n,L in enumerate(leaves):\n    if 'ایدر' in L or 'ایدون' in L or 'ایدن' in L:\n        for m in re.finditer('ایدر|ایدون',L):\n            print(n, '|', ' '.join(L[max(0,m.start()-120):m.start()+260].split()))\n        print('---')\nEOF"
}
```


### [2026-09-06T15:19:27.815Z] TOOL RESULT

```
---
---
237 | ت که شکوفه‌ای درنهایت سرخی مي باشد . بر ورمهای صللب طلا کنند افع آ ید . آذون » بر وزن هامون . بمعنی آن چنان باشد چنانکه ایدون بمشنی چنن است . آ ذییش - بکس ثالث و سکون تحتالی رشن‌فرشت ۰ چوبی را کوین که بر آمتانهٌ در خاده اسنوار کنند - وبمعنی ریز چوب وخس وخاشالك هم آمده است . آی *ه بر وژن د معنی آبین است که زب و زشت و آراش - و رسم و قاعده وفانون باشد - و بمعنی آآت ی که روغرا از د
---
---
---
---
288 | ان , بمعنی دودمان و خاندان باشد - و بمعنی سزاوار و حستحق حم آمده است ؛ و در موّبد الفضلاء با ذال نقطه دار نوشته اند * . ایدرم * ه بکس اول بروزن اسپرم . نام کتلب شاکمونی ۷ و او باعتفاد کف ند پیغمس صاحب کتاب است » و معنی این لفت باعتفاد او اول و آخر کتابها باشد . اير - یسکون ثانی بروزن صبر » حص‌ون البلدان) ۸۵25 و ۸۵216 « لت نامه *. ۴ - مصحف کلب « انشوسا » و < انشا » صت ۸ لغت ناهد
---
---
---
414 | س ت که شکم ,بندد. اف فا بکراولبروزن بی‌بند »یممنی اند است وآن عددی باشد مجهول که بده ؛, سد» و آنرا بعربی بضم خوانند ۱ . ایدون ؟ « بفتح اول ؛ بروزن «مسنی اکنون است که این زمانرالحال باشد - وبکسر اول بمعنی. اشجنین و اینجا و این زمان وایشدم و این ساعت بود ‏ ایدی « بفتح اول و سکون ثالیر کسر نالث و سکون تحتالی , بمعنی نیز باشد کهعربی اضا خوانند و ظاهرا درین ممنی با لغت اندی صحیف‌خوا
---
---
---
---
---
---
---
---
---
---
---
```


## [2026-09-06T15:19:56.838Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 216 217 218 219; do echo \"=== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KNT.txt | head -50; done"
}
```


### [2026-09-06T15:19:58.331Z] TOOL RESULT

```
=== leaf 216
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
naiba- adj. ‘beautiful, (religiously) good’, re- .
placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
naucaina- adj. ‘of cedar’: NPers. nóZ, пдѓап ‘pine cone’; therefore naucaina- ‘pine-cone-shaped’ ($147.11), appropriate to the cedar (König, Burg- bau 53-4; Hz. AMI 3.58). naucaina nsm. DSf 30f. |
nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
7 ыйсы аЙ eet NUI ШЕЛ, АМАА а аз an ШО. Дені. Zr é
DD де 5... anes
LEXICON
‘corpse’, Lt. acc. nec-em ‘destruction’, nocet ‘harms’, pIE *nek- (887).
vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
Nadi"labaira- sb. ‘Nidintu-Bel, a Baby- lonian rebel: Elam. nu-ti-ut-be-ul, Akk. ni-din-ti- йе] (§75.V, §76.V, $107). Naditabaira пзш. DB 1.77, 92f; 2.1; 4.12; DBd 1. Naditabairam asm. DB 1.80, 84; 24, 5. Naditabairahyà gsm. DB 1.85, 89, 95.
napüt- sb. ‘grandson’: Av. Skt. napat-, Lt.’
nepos, pIE *nepot- (875.1, §110, $142). napa nsm. (§124.5, §188.1) AmH 4; DB 1.3; DBa 4; А:Ра 16°.
Nabukudracara- sb. ‘Nebuchadrezzar’, son of Nabonidus; name assumed by the rebels Nidintu- Bel and Arkha: Elam. nab-ku-tur-ra-sir, Akk. nabu-kudurri-ugur (82, 833, §75.V, $128, §163.- VD. Nabukudracara nsm. DB 3.80f, 89; 4.14, 29f; DBd 3f; written Nabukuracara ($52.V) DBi 5f. Nabuk*dracara (822) DB 1.78f, 84, 93.
Nabunaita- sb. ‘Nabonidus’, last king of the New Babylonian Empire, 556-39. в.с: Elam. na- bu-ni-da, Akk. nabü-na'id; Gk. Aaßivnros (Hat. 1.74, ete.). Nabunailahyà gsm. DB 1.79. Na- bunaitahya (§36.1Vb) DB 3.81; 4.14, 30; DBd 5f; DBi 7f.
niman- sb. ‘name’: Ау. náman-, NPers. пат, Skt. náman-, Lt. nomen, pIE *nómen-, cf. Gk. буора, NEng. name ($109, $110, 5155.11). See also Andmaka-. náma^, suffixless lsn. used with mase. and nt. generic nouns to denote specification ($112, $187, §251C, §312): DB 1.28, 30, 36, 37, 74, 77, 92; 2.8f, 9, 14°, 19, 22, 29, 38, 49, 65, 79, 82, 95; 3.5, 12, 13, 22 bis, 31, 34, 44, 51, 56, 78, 84; 4.8, 10, 12f, 15f, 18, 20, 23, 26, 29, 83 bis, 84 bis, 85, 86°; 5.5, 8, 27; DSe 45°; DSf 31, 46; Юле 9; XPf 18, 19; А?Не 14f; A?Pa 19, 20; Sa 2f. nama, either asn. *ndmá ог lsn. лата” (with lengthened grade), specialized for similar use with fem. generic nouns because of similarity of end- ing ($67.1T, $187, §249L, $312; cf. Tm. Lex. 105,
193
with lit.; not with Foy, KZ 35.11, 37.505, IF 12.172n, nor with Debrunner, IF 52.153): DB 1.58, 58f; 2.271, 39, 44, 52, 59, 72; 3.11, 23, 61, 66, 12, 19; 54°.
nay- vb. ‘lead’: Av. nayeitt, Skt. náyati. Conj., §213. anaya imf. DB 2.88; 3.88°; 5.12. [ajnaya" 3d pl. imf. ($232.11) DB 5.28. anayatá imf. mid. as pass. ($235.П) DB 1.82, 2.73; 5.26". Some or all of these are possibly ànay-, from à + nay-. | fra- + nay- ‘lead forth, provide’: fránayam Ist sg. imf. ($226.11) DB 1.87.
nar- sb. ‘man’: Av. Skt. nar-, Gk. дир, cf. Lt. Ner-6; i
=== leaf 217
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
nij- verbal prefix ‘away’: sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niş- ($120); with verb ay- ‘go’.
nipadiy phrasal adv. and prep., ‘on the track of, close after’: prep. ni- + loc. padiy, to pad- ‘foot’ ($76.11, $136, $140, $191.1V). тарайту adv. DB 2.73; prep. with acc. DB 3.73.
nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
194 OLD PERSIAN
niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
niyaSadayam, see had-.
Nisdya- sb. ‘Nisaya’, a district in Media: Elam. nu-is-fa-ja, Akk. ni-is-sa-a-a (5116). Per- haps from ni- ‘down’ + sdya-, to root Av. st- say- Tie’, Skt. §-, Gk. кт. ‘Ties’, pIE *kei-. Nisdya nsm. DB 1.58. |
niXadayam, see had-.
nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
pä- vb. ‘protect’: Av. pà-, pres. рйи, РЫ. pátan, Skt. pà-, pres. pati (ablaut, §122). See also zíacapüvan-. apayaiy lst sg. imf. mid. (Ву. BSLP 33.2.151-2; Kent, Lg. 9.42; S71, $214, $233.1II; wrongly to Skt. pt- ‘swell’, Wb. ЖА 41.820-1) XPf 39. padiy 2d sg. imv. (5208, §237.1) DPe 21f. pätwv (§208, $297.IT) AsH 12, 14; DPd 16; DPh 10; DNa 52; DSe 50; DSf 57; DS} 6°; D8n 2°; роз 7°; DSt 8°; ОН 8; XPa 18, 20; XPb 28; ХРе 12, 15; XPd 18; ХР 45, 48; XPg 13; XPh 57; Хе 5^; XV 25f; А:Ра 226; D'Sa 3; A?Hb^; A?He 19. pätw 3d pl. іту. (§237.1T) A'Sa 5°; A’Sd 4; А?На 6°; A?Pa 25. pála пзш. past ptc. pass. (§242.IT) DPe 22. pati- + pã- mid. ‘protect one’s self against’, with Ласа + abl.: райїрауаш@ (828; not wrongly written, despite MB Gr. §69) 2d sg. imv. mid. ($71, §214, 5297.11) DB 4.38.
paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
paišiyā- sb. ‘script, written text’: deriv. of pai- (§89, §144.V). See also Parsiyduvada-. ри nsf. DB 4.91 (conj. of Kent, JAOS 62.268).
PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps, 
=== leaf 218
with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and Sacred Writings’ (on Pasargadae, ef. also Kónig, RuID 66; but Hz. ApI 275-6, modifying his view ш AMI 1.86n, takes prior element to be pati-, pati- becoming pa&-, with epenthesis; Bthl. AiW 907-8 normal- izes Piši- after the Akk., but gives no etymology). Paisiydwddim asf. DB 3.42. Parsilydluvadayd absf. DB 1.36f.
pa|camàm] adj. ‘fifth’, asf.: wrong restoration of Wb. at DB 5.8 (ef. Kent, JNES 2.109).
pal- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. vérerat, Lt. рені ‘seeks’, pIE *pet-.
ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
66): udapalatà imf. mid. (§84, 8213, 5285.П) DB 1.36, 38, 74, 78; 2.10, 14f; 3.24, 79.
patiy adv., prep., prefix ($140.I, $1911): Av. рай, Gk. (dial.) rori, pIE *poti, cf. pIE *proti in Skt. prát, Gk. Hom. троті, classical rpés (cf. Lg. 20.9-10).
(1) Adv. ‘thereto, again’: DB 2.37, 48, 57; 3.04, 71. pati-maty ($186) DNb 32f.  nai-pati-mà ($133, 5186) DNb 20. yadi-patiy (8136) DNa 38. (ya-patiy XPa 15; XPf 40f.
(2) Prep. (8271) with ace.: DB 52 ‘during’; DNb 22 ‘against? (Hz. ApI 273 reads par[slaiy ‘in court’, sb. to root fraé-); postposed DB 2.62 ‘on’. Encl., with ace. ‘during’ DB 1.20 (8133, $136); with inst. ‘near, at’ DB 2.16°, 3.26; with loc. ‘on, upon’ DB 2.76, 91; 3.52, 92. Ву. BSLP 42.2.70 takes all these as adverbs except DB 2.62, DNb 22.
(3) Prefix with verbs avahya-, ay-, ziay-, jan-, рӣ-, fraf-, d-bar-, zbü-; prior element in nouns palikara-, Patigraband-, perhaps Pátisuvari- and
"* 2 - -
also patiš, patisam.
patikara- sb. ‘picture, (sculptured) likeness’: .
РМ. patkar-, NPers. pátkür-;.pati- + kara- to root
as sata jeu iit И ЗАК
pores agent iain ee Seeman Re NE SS a cet ras ЧЕК ЧАС ve NEMPE
LEXICON 195
kar- ($143.V). patikaram asm. DSn 1°. palikara apm. DB 4.71, 78, 77; DNa 41.
Patigraband- sb. ‘Patigrabana’, a town in Parthia: Elam. pat-t-ig-rdb-ba-na; from pati- + root grab- + suffix (833, $103.IV, §147.1). Pati- graband nsf. DB 3.4f.
Я patipadam phrasal adv. ($191.17) ‘on its base, in its own place’: pati- ($186, $1401) + aec. padam (see pada-; 76.111, $122). DB 1.62.
palis prep. with acc. ‘against’: pati- + adv. -s, ef. Lt. ex, abs, ops- in os-lendó, sups- in sus-tined, Skt. nt and nis, Gk. ато iy, audi audis. See also patisam. DB 1.93; 2.33, 38, 43f, 52f, 58, 67; 3.36, 43, 65.
patisam adv. ‘in addition’: extension of patiš, ef. for formation Ose. per-um ‘without’ to (Lt.) per, and for meaning Gk. трд ё ‘and besides’, Lit. atque from *ad-que ‘and thereto’ (OP patiy, Gk. тро, Lt. ad agree in marking something as an ad- dition). patišam DB 4.89 (p* probable but not certain KT); (раат DB 4.90 (restoration of Konig, Klotho 4.45; see also Kent, JAOS 62.267- 8).
Pàtiwvari- adj. ‘Patischorian’ ($167): Elam. ba-ul-ti-i$-mar-ri4$, АКК. pa-id-di-if-hu-ri-i$, Gk. (рі) llaracxopes. Perhaps pAr. *pati-, with vriddhi ($126), + *suára- ‘(of the plain) before the Hvara Mts.’ ($117), with combination (8$140.VI) of sandhi forms (so Hz. ApI 183-4, who however disregards the d in the penult of the OP). Ран паті nsm. DNe 1.
. раві- sb. ‘path, way’ (676.1, §152.1, $179. III): Av. pab- patá-, Skt. panthan- path-. райт asf. DNa 58.
pad- sb. ‘foot’: Av. Skt. pad-, Gk. roô-, Lt. ped- ($142); in mipadiy, cf. also pada-, páda-, pasti-.
pada- sb. 'footing, step, station': Av. paóa- ‘foot (as measure)’, Skt. padd- ‘step, footstep, place’, Gk. aé&ov ‘ground’; extension of pad- ($143.- П). In Garmapada-, patipadam; see also pad-, рӣйо-.
рӣйа- sb. ‘foot’: LAv. páóa- ‘step, pace’, Skt. pida- ‘foot’, Gt. fotu-, extension of stem in pIE nom. *pdd-s, acc. *pod-m, seen in Gk. Dor. тах ($76.11, §122, $126, $148.П). Cf. also pad-, pada-. püdaibiyà idm. ($189) DNb 41.
par- vb. ‘communicate’: Av. *par- ‘hindureh-, hintibergehen’ (ВЕ. AYW 851), Gk. weipw 
=== leaf 219
‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte. pass. ($242.1) DNb 54 (dubious con]. of Kent, Lg. 15.167, 178-4).
ipara- adj. ‘later’, possibly in hyáparam (q.v.) : Av. para- ‘farther’, Skt. pára- ‘distant’, Gk. qépav ‘beyond’.
nara prep. with acc. ‘beyond’ (§32, $63.1): Av. pard ‘before’, Skt. purds ‘before’, Gk. таро ‘before’; DPe 15; DPh 5; DH 4, See also para- dayadàm, paradraya.
parü postpos. with acc. ‘along’, and verbal prefix ‘forth’ ($132.3): Av. ?pará ‘before’, Skt. purá ‘before, formerly’, Gk. rapá ‘alongside’: in avapard and with ay-, ar-, gam-, bar-.
parauvaty lsn. as sb. ‘in the east’: руи] "Ре 15, a misreading for pr? : d*r^ ye (uninseribed space between r* and y*) = para : dra ya; seeunder paradraya.
paradayadám sb. asf., perhaps ‘pleasant re- treat’ ($55.II, §148.1V): Аа 3. Possibly mis- written руат“ for p'rud*iljme = paridai- dam, Av. patridaéza- ‘Umwallung, Ummauerung' (Bthl. AiW 865), borrowed in Gk. тарабено ‘park’, cf. JAOS 51.229; or for p'r*d'id^am* = paradidam, from ?para ‘beyond’ + didá- ‘wall’ (q.v.), as ‘that which is beyond or behind the wall’ (ef. Scheil 21.93; Bv. BSLP 30.1.67 j'vadiy paradayadám ‘paradis de vie’).
paradraya phrasal adv. ‘across the sea’ ($44, $191.[V): рата ‘beyond’ + acc. draya ‘sea’. DNa 28f; DSe 29°; XPh 24. paradraiya (848) A?P 24 (Hz. ApI 142). As two words, para draya DPe 15 (Cameron, JNES 2.307-8).
parana- adj. ‘former’: deriv. ($147.11) of stem in OP ?para, para (cf. ВЕШ. AiW 854), Av. рагі, рагб, Skt. рига ‘formerly’ (hardly to be normal- ized parna-, with MB Gr. $267, to Gt. faírneis ‘old’). See also dumlaparanam. — paranam asn. as adv. ‘formerly’ DB 1.51, D'Sb 3.
pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
196 OLD PERSIAN
pariyana- sb. ‘superiority’: deriv. ($147.IT) of pariy, in meaning seen in Ау. pairi ‘vorne, über ... hin’, Skt. pári as prefix ‘much, excessively’, cf. Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, Sen 250). pariyanam nsn. DNb 52.
paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
paruva- adj. ‘being before in time or place’ (§35.1[): Av. paurva-, Skt. pürva-, pIE *pruos (868, $150), ef. Gk. Ion. трохоѕ ‘early’. See also paruviyata, paruviyaüd. parwā npm. ‘former’ DB 4.51. parwam asn. as adv. ‘formerly’ DB 1.9; DBa 15f; DSe 43°, 47; XPh 36, 39; paruvam- ciy DB 1.63, 67, 69.
parwnyata, adv. with preceding hacd, ‘from long ago’: *paruviya- (ie. *parvya-, deriv. of paruva-), Av. paouruya-, Skt. pürvyd-, + adv. suffix -la^, Av. -£ó, Skt. -tas, Gk. -ros, Lt. -tus asin funditus, pIE *-los ($191.11). C£. also paruviyatà. DB 1.7, 8, 45; DBa 11, 12.
[paruv|iyafà adv. ‘at first attempt’: *paruviya- (see paruviyala) + adv. suffix -0à, Av. -fa, Skt. -ihà ($191.ID). DSj 3 (conj. of Brandenstein, WZKM 39.49-51; ef. note ad loc.).
paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
Parga- sb. ‘Parga’, a mountain in Persia: Elam. par-rak-qa, NPers. Purg ($30). Parga лет. DB 3.44. |
partara- sb. ‘battle’ (as in Elam. and АКК. versions): extension of -r/n- s
```


## [2026-09-06T15:20:15.405Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==227' KNT.txt | head -60"
}
```


### [2026-09-06T15:20:17.147Z] TOOL RESULT

```
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32.
Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado.
(1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm. DSf 50, 54. Майа] ipm. DB 2.23. MddatSuva lpm. DB 2.23.
(2) ‘Media’: Мада пзш. DB 1.15°, 41; 2.7; DPe 10; DNa 22; DSe 21°; Рб 8°; XPh 19. Madam asm. DB 1.47; 2.22, 28f, 48f, 68, 65 bis; 3.32f; 4.20. Méddam-ca DB 1.66f. Madaiy lsm. DB 1.84, 59; 2.15, 17, 22, 28, 66 bis, 72, 92; 3.77; DBe 10f.
tman- vb. ‘think’: Av. man-yele, Skt. mán- yale, Gk. utuova ‘(I bave thought of,) I desire’, Lat. memini ‘I remember’, pIE *men-. See also manah-. maniyary lst sg. mid. (§214, 5238.1) DNb 38. amaniyazy lst sg. imf. mid. (8214, 6233.11) DSI 3f. mantydhaiy 2d sg. subj. mid. (831, $222.11, §234.1) DB 4.39 (manl. . .); DPe 20 (maniydhay, $27, 552.11); DNa 38 (maniya- [...); XPh 47 (maniyaty, without the h*: $27, $52.VI, Lg. 13.302; Hz. AMI 8.66, ApI 243-4). maniyál|taty) sub). mid. (5222.1) DB 4.50.
^man- vb. ‘remain’: Av. man-, iterative pres. manaya- (8123, $215), Gk. pvo, Lt. maneo; prob- ably specialization of pIE *men- ‘think’ (see ‘man-) in meaning ‘remain thinking. amdnaya imf. DB 2.48, 63; amünaiya ($48) DB 2.28.
mana'uwin- adj. ‘mindful, wilful, hot-tem- pered’: from manah- + -win- (§155.V), cf. Lg. 15.170, JNES 4.47 (Hz. ApI 242 otherwise, wrongly). manauvis (remade from -07, $187) пэш. DNb 13.
manah- sb. ‘thinking power, power of will’ (Jn. Iran. Rel. $70; Kent, JNES 445-7, 232): Av. manah-, Skt. mánas-, Gk. дё ‘courage’, pIE *menos *menes- (5124.4, 4156.1). Decl., $185.I. See also manawin-, and -manis- with reduced grade in second syllable, in Ardumuni&, Harā- manik, perhaps [manis-. тапа&-са (8105) asn.
DNb32. manahà isn. (JNES 4.45; wrongly gen., Hz. ApI 240-2 and Sen 235) DNb 14.
méaniya- sb., probably ‘personal property’ in the houses; nt. adj. as collective sb., from тӣпа-, GAv. demüna-, Ау. nmana- ‘abode, house’ ($126), extension of root seen in Skt. dáma- ‘house’, Gk. 0óuos, Lt. domus. For varying views, see Tm. Lex. 116, with lit.; Gray, JAOS 21.17, 33.281-3; Bthl. AiW 1168; MB Gr. §261; Fay, JAOS 34.330-1. méaniyam-cé asn. DB 1.65.
+mamaita, see Atamatta-.
тауйта- sb. ‘doorknob’: Skt. maytikha- ‘peg’, perhaps to Skt. mi- (pres. minétz) ‘fix (as in the earth) ($100, 5148.11); ef. Hz. Ар] 258-9. mayüxa пзш. DPi; XPi.
mar- vb. ‘die’: Av. mar-, pres. miryeite ($122, $214), Skt. mriydte, Lt. moritur, pIE *mer-. See also uvdmarsiyu-, marika-, maria-, martiya-. amarijalü imf. mid. (835.1, $285.II) DB 1.43.
marika- sb. ‘person of lower rank, subject’, as shown by АКК. *"gal-la ‘menial’: contracted ($23.1) for *mariyaka-, deriv. of stem in Skt. (Vedic) márya- ‘young man, stallion’, ef. Skt. maryakd- ‘little man (said of a bull among cows)’, Phi. mérak (from *maryaka), Gk. шера ‘boy, girl’ (from *merjak-); ultimate root pIE *mer-, OP mar- (5122, 5146.11). Cf. Hz. ApI 251-3, Bv. TPS 1945.43-4. татка узш. DNb 50, 55, 59°.
Müru- sb. ‘Maru’, a town in Media (ef. König, RulD 71): Elam. ma-ru-i$, АКК. ma-ru-’. Mälrulš nsm. DB 2.22.
M árgava- adj. ‘Margian’: adj. to Margu-, with vriddhi ($126, $143.11, V, VI). Малаа nsm. DB 3.12; 4.24.  Mürgavaibis ipm. DB 3.16.
Margu- sb. ‘Margiana’, a province of the Persian Empire: Elam. mar-ku-i$, АКК. mar-gu-’, Gk. Mapyos, Мару:аиу (S31, $153.1). See also Márgava-. Margué пэт. DB 2.7; 3.11. Mar- gum asm. DB 4.25. Margaw lsm. ($114) DB 4.25; DBj 5f.
marta- ріс. as ad]. ‘dead’: Av. marata-,-N Pers. murd, Skt. mrid-, Gk. Вротос (for *Sparós, with vowel assimilat
```


## [2026-09-06T15:20:23.183Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor pat in [r'\\niyam','ima- pron','aita-','^i- pron','yatara','ya-tara']:\n    for n,L in enumerate(leaves):\n        if re.search(pat,L,re.M):\n            print(pat,'-> leaf',n)\n    print()\nEOF"
}
```


### [2026-09-06T15:20:25.105Z] TOOL RESULT

```
\niyam -> leaf 101


aita- -> leaf 45
aita- -> leaf 64
aita- -> leaf 70
aita- -> leaf 185
aita- -> leaf 187
aita- -> leaf 199
aita- -> leaf 216


yatara -> leaf 99
yatara -> leaf 136
yatara -> leaf 152
yatara -> leaf 209
```


## [2026-09-06T15:20:31.770Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n,L in enumerate(leaves):\n    ms=re.findall(r'(?:LEXICON\\s+(\\d{3})|(\\d{3})\\s+OLD PERSIAN)',L)\n    if ms and 195<=n<=240:\n        print(n, ms)\nEOF"
}
```


### [2026-09-06T15:20:33.912Z] TOOL RESULT

```
209 [('281', '')]
213 [('', '190')]
215 [('', '192')]
217 [('', '194')]
218 [('195', '')]
219 [('', '196')]
222 [('199', '')]
223 [('', '200')]
225 [('', '202')]
227 [('203', '')]
```


## [2026-09-06T15:20:46.653Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n,L in enumerate(leaves):\n    if n<190 or n>235: continue\n    for m in re.finditer(r'\\bi-\\s+pron|\\bima-|\\biyam\\b|\\bimam\\b|\\byatara-|\\bya-\\b.{0,20}pron|\\bhya-\\b',L):\n        print(n,'|',' '.join(L[max(0,m.start()-150):m.start()+250].split()))\n    \nEOF"
}
```


### [2026-09-06T15:20:48.636Z] TOOL RESULT

```
190 | ticle extracted by wrong di- vision from pAr. *azham T’, perhaps even in pIE times, and therefore *-om from *ej(h)om; seen in OP tuvam (cf. adam T’), iyam, imam, patisam, cf. Skt. fuvám тубт imám ete. ama- sb. ‘offensive power’, see ArSdama-. amaxamaté, DB 4.92, read by KT, and ap- parently corresponding to Elam. ‘were pleased (at the inscription)’ (cf. Wb. KIA 72n, quoting vari- ant interpretatio
190 | extracted by wrong di- vision from pAr. *azham T’, perhaps even in pIE times, and therefore *-om from *ej(h)om; seen in OP tuvam (cf. adam T’), iyam, imam, patisam, cf. Skt. fuvám тубт imám ete. ama- sb. ‘offensive power’, see ArSdama-. amaxamaté, DB 4.92, read by KT, and ap- parently corresponding to Elam. ‘were pleased (at the inscription)’ (cf. Wb. KIA 72n, quoting vari- ant interpretations): p
196 | .e. idä) adv. ‘here’: GAv. idà, LAv 1ба OLD PERSIAN Skt. thd, Gk. adv. ending -6e, pIE *:-dhe (676.11, $191.11), formed on pronominal root seen in OP iyam, Skt. ayám тубт idám, Lt. is ea id. DB 1.29; DSf 37, 38, 40, 48, 45f; DSo 4°; XPb 24. ima- demonst. ad]. and pron. ‘this’: Av. ima-, , Skt. ima-; stem extracted from Ar. *im-am = асе. *i-m -+ enel. -am (q.v.; wrongly Mt. MSLP 19.49- 52). Decl.,
196 | he (676.11, $191.11), formed on pronominal root seen in OP iyam, Skt. ayám тубт idám, Lt. is ea id. DB 1.29; DSf 37, 38, 40, 48, 45f; DSo 4°; XPb 24. ima- demonst. ad]. and pron. ‘this’: Av. ima-, , Skt. ima-; stem extracted from Ar. *im-am = асе. *i-m -+ enel. -am (q.v.; wrongly Mt. MSLP 19.49- 52). Decl., $199. imam asm. DPa 6; DPe 21; D8d 3; D8n 1°; XPa 12; ХР]; A'I (as nsm., §56.V); D’Sa 1°; A
196 | l root seen in OP iyam, Skt. ayám тубт idám, Lt. is ea id. DB 1.29; DSf 37, 38, 40, 48, 45f; DSo 4°; XPb 24. ima- demonst. ad]. and pron. ‘this’: Av. ima-, , Skt. ima-; stem extracted from Ar. *im-am = асе. *i-m -+ enel. -am (q.v.; wrongly Mt. MSLP 19.49- 52). Decl., $199. imam asm. DPa 6; DPe 21; D8d 3; D8n 1°; XPa 12; ХР]; A'I (as nsm., §56.V); D’Sa 1°; A'Ba 3, 4°, 5? (as asn., §56.V); A?Ha 5, 7
196 | n OP iyam, Skt. ayám тубт idám, Lt. is ea id. DB 1.29; DSf 37, 38, 40, 48, 45f; DSo 4°; XPb 24. ima- demonst. ad]. and pron. ‘this’: Av. ima-, , Skt. ima-; stem extracted from Ar. *im-am = асе. *i-m -+ enel. -am (q.v.; wrongly Mt. MSLP 19.49- 52). Decl., $199. imam asm. DPa 6; DPe 21; D8d 3; D8n 1°; XPa 12; ХР]; A'I (as nsm., §56.V); D’Sa 1°; A'Ba 3, 4°, 5? (as asn., §56.V); A?Ha 5, 7 (as asn.); A
196 | d]. and pron. ‘this’: Av. ima-, , Skt. ima-; stem extracted from Ar. *im-am = асе. *i-m -+ enel. -am (q.v.; wrongly Mt. MSLP 19.49- 52). Decl., $199. imam asm. DPa 6; DPe 21; D8d 3; D8n 1°; XPa 12; ХР]; A'I (as nsm., §56.V); D’Sa 1°; A'Ba 3, 4°, 5? (as asn., §56.V); A?Ha 5, 7 (as asn.); A®Pa 22 (as nsf., §56.V). imaiy npm. DB 434, 80, 82. imaiy apm. DB 4.31; imai-vä ($136) DB 4.71, 73, 77. imaisám
196 | ; A?Ha 5, 7 (as asn.); A®Pa 22 (as nsf., §56.V). imaiy npm. DB 434, 80, 82. imaiy apm. DB 4.31; imai-vä ($136) DB 4.71, 73, 77. imaisám gpm. DB 4.87. imam ast. AsH 10f, 13; DB 4.42, 48, 54, 57, 70, 73, 77, 89 (те Cameron; for imäm, §52.V]); DPd 15, 18; DPe 24; DNa 1f, 32, 53; DSe 1f; DSf 1; DSt 1; DZe 1, 8, 12; DE 2; XPa 1; XPb 2; ХРе 1; XPd 1f; ХРЇ 1f; XPh 1, 58; XE 3; XV 2, 24; A!Pa 2°; Ае 4f (a
```


## [2026-09-06T15:21:01.537Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in range(185,215):\n    L=leaves[n]\n    ms=re.findall(r'(?:LEXICON\\s+(\\d{3})|(\\d{3})\\s+OLD PERSIAN)',L)\n    print(n, ms, ' '.join(L.split())[:60])\nEOF"
}
```


### [2026-09-06T15:21:03.219Z] TOOL RESULT

```
185 [] ugh not mentioned in the Behistan inscription, must have fol
186 [] � asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; 
187 [] t built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta
188 [] ’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadt
189 [] n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-
190 [] . Skt. apa, Gk. and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, 
191 [] formed like Gk. &exero to root *segh-, ёттєтө to root *pet- 
192 [] -, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *a
193 [] t’). - LEXICON ч. Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerx
194 [] пат. AsH 1, 5; DB 1.4f; DBa 6; DSf 13; XPf 19, 20; A’Pa 20 (
195 [] 's avabäštā adj. apm. 'thus standing". avadà (ie. avadá) adv
196 [] 3. asmanam (853) A?Pa 3. ašnaiy adv. ‘near’, lsn. of ašna- ‘
197 [] �; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 
198 [] DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43
199 [] by Hz, ApI 71-2). ufraSa- ufrasta- adj. ‘well punished": u- 
200 [] B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vri
201 [] to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54
202 [] om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2). акша aor. mi
203 [] ted by the OP writing. регу. of Iran. root *kas- (89.V, §87,
204 [] , 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21, 181 28, 29, 
205 [] sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 
206 [] n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (con
207 [] 3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&
208 [] Skt. jū- ‘press for- ward, impel quickly, excite, promote’, 
209 [('281', '')] it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 
210 [] 1) XPh 23. tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) Am
211 [] word of uncertain meaning, Sb 3. Sanuvaniya- sb. ‘bowman’: d
212 [] fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wa
213 [('', '190')] 5-6). Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 52
214 [] Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42. Daha- adj. ‘
```


## [2026-09-06T15:21:21.782Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (228,229):\n    print('==LEAF',n)\n    print(' '.join(leaves[n].split())[:2500])\n    print()\nEOF"
}
```


### [2026-09-06T15:21:24.044Z] TOOL RESULT

```
==LEAF 228
so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a province: Elam. mu-is-sa-ri-ia, АКК. mi-sir (S6, §76.V). (1) ‘Egyptian’: Mudrdya nsm. А?Р 19. Mudráyà npm. DSf 50f, 52, 55. (2) ‘Egyptians’, as province: Mudräyā npm. DPe 11f. (3) ‘Egypt’: Mudráya nsm. DB 1.15, 27°; DNa 27; DSe 26°; DSm 7^; XPh 28. Mudrüyam asm. DB 1.32, 33; DZe 8. Mudrayé absm. DSf 41; DZe 11. Mudrüyaty lsm. DZe 9. ya- rel. pron. ‘who, which’, generalized by enel. -ciy (ef. Hz. ApI 355-6): Av. Skt. ya-, Gk. ds, pIE %0-. See also уйй, уада, yada-, yadry, yaniy, уйй. ya-ciý nan~ ($105, $130, $197) РМ 57. ya-ciy asn. DNb 35, 86 204 Yautiyd- sb. ‘Yautiya’, a district in Persia: Elam. 4a-t-t-1a-18, АКК. 1-0-0-ја. Yautiya nsf. DB 3.23. yaud- vb. ‘be in commotion’, present stem yauda-: Av. yaoz- ‘boil up’ (§88), pres. yaoza- (Hz. AMI 8.67, ApI 362-5); not to Av. yaod- ‘fight’, Skt. yudh-, because of the difference in the present stem (Av. yüióyeiti, Skt. yüdhyati; JAOS 58.116). ayauda imf. (5213) XPh 31f (not dyauda пзш. ‘rebellion’, as taken by Henning, BSOS 10.505, which is refuted by Akk. version). ayauda" 3d pl. imf. (5232.П) DSe 33°. yau[da*- tim] asf. pres. pte. act. ($190.1, $240) DNa 32. | Yauna- adj. 'Ionian'; pl., also a province of the Persian Empire; mase. sg. as sb., ‘Ionia’, а province: Elam. (2)-a-u-na, Akk. ja-ma-nu, Gk. Tovia. (1) ‘Ionian’: Yauna nsm. A?P 26. Yaund npm. DSf 33f, 48; as nam. (556.1) А?Р 23. (2) ‘Ionians’, as province: Yauná npm. DPe 12{; DNa 29; DSe 271°; DSm 10°; XPh 23. (3) ‘Tonia’: Yauna nsm. DB 1.15; DNa 28; DSm 8°. Yaund absm. DSf 42. yaumant- adj. ‘trained, skilled’: adj. to *yauman-, with vriddhi (5126, $152.T, ў}155.Ш), from root seen in Skt. уйин ‘harnesses, fastens’, ef. Hz. ApI 365-6 (not with Sen 249, ‘agile’, from *yduman-aina-, fem. -2). See also ayáu- mani-. yüumainii пзш. (with epenthesis, $127; Lg. 15.173) DNb 40. уашлуй- sb. ‘canal’ (§48): NPers. Joi ^water- course, canal’, cf. perhaps Skt. (Vedic) yavyd isf. ‘stream, river’; perhaps deriv. (§144.V) of root ay-/i-/yà- ‘go’ (JAOS 62.271). yauviyd nsf. DZe 10. yaunydm asf. Оле 8f, 12. yaka- sb. (§6, $143.IV) a kind of wood (oak, Scheil 25.28, but if so, not cognate, Bv. BSLP 30.1.01; Afghan cypress, Kónig, Burgbau 54-61; mulberry, Wb. AfOF 7.42; teak, Hz. AMI 3.61-2; certainly not ‘timber’ in general, as taken by Gray, AJP 53.68). yaka nsf. DSf 34. yacty, see ya-. yaté conj. and prep.; perhaps уй isn. or уй! absn. of ya- + -tă as in сий, q.v. (wrongly Sen 11). (1) Соп]. ($2

==LEAF 229
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39. lwadé- conj. ‘where’: GAv yada, Skt. yada; probably rel. nt. pAr. #00 + postpos. 4. уайд- tya XPh 35f ($133, $296; cf. yaa tya ХР 29); yadàyà XPh 39 (perhaps error in writing, §55.1; but ef. Hz. AMI 8.66, ApI 358, Nyberg Rel. 477-8). *Yadd- sb. ‘Yada’, probably ‘Anshan’ (as shown by the Elam. translation 3.3 an-za-an.mar, read by Cameron; cf. §166.n2): not an abstract yadà- ‘loyalty’ to root yad- (q.v.), as commonly taken (wrongly also Foy; KZ 35.43; Hüsing, ОГЛ Ы LEXICON | 205 8.513-6; Hz. ApI 244-9; Nyberg, Rel. 477-8). Yadayd absf. ($141, $175) DB 3.26. yadiy conj. ^if, when’: Av. yetéi, Skt. yddi: per- haps pAr. nt. rel. *iad + deietic 4. Syntax $297. (1) Sf, with subj.: DB 4.38f, 54, 57, 721, 77; DPe 19, 22; DNa 38 (yadi-patiy), DNb 29 (yadi- và; cf. Hz. ApI 359); XPh 47 (yadi-maniyáty; 841, $92. VI); with opt., DNb 20f; with pres. ind., ОХЬ 25 (yadi-và). (2) ‘when’, with imf. ind., DB 1.38, DSf 11; ‘whenever’, with pres. ind., DNb 38f, 39. yàna- sb. ‘favor, boon’: Av. yand-; deriv. of ‚ yam-, probably *ya- from *m-, with lengthening and suffix -na- (5147.1). yànam asm. DPd 21, 23°; XSe 4°. yaniy соп]. ‘where, whereon’: lsn. *ya^mi (= Skt. ydsmi-n, Av. yahmy-a ‘where’) to relative stem ya-, with -n- after isn. *yand, cf. isn. lyand to tya- (hardly yanazy, loc. formed on stem yana- extracted from isn. *yand, as taken by Bthl. Ат 1262; not miswritten for tyanaty, as taken by Müller, WZKM 7.112; other theories in Tm. Lex. 120 s.v.). Syntax $296. XV 22. yam- vb. ‘stretch, reach out’: Av. yam- pres. yasaiti, Skt. yam-, pres. ydechati, OP pres. yasa-, pIE *im-ske-. See also уйпа-. а + yam- ‘reach out for, (mid.) take as one's own’: ãyasatā imf. mid. (§97, $215, $235.IT) DB 147; 34, 49f. ай- + yam- ‘reach beyond, present, read aloud to’: [аја] уа (823.T, $140.IIT, $220) imf. pass. DB 4.91 (conj. of Kent, JAOS 62.268; for -i-, ef. niyasaya, below). ni- + yam- ‘reach out and down; (caus.) set down’: niyasaya imf. caus. (823.I, $140.IIT, $215) DNb 5, 46, 49 (In. JAOS 38.123-4; MB Gr. $199; Johnson, Gr. $4780; Hz. ApI 359-61). уйа con]. ‘as long as’, isn. of *ydva-, exten- sion of pIE rel. */o-, pAr. *ia-, cf. Skt. ydvat, Av. yavala, Gk. dos (from *ayos); hardly from* yàva! à = G
```


## [2026-09-06T15:21:38.589Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for pat in \"aetauuant\" \"aētauuaṇt\" \"aetavant\" \"yatāra\" \"yatara\" \"atāra\" \"iθa\" \"i0a\"; do echo \"### $pat\"; grep -o -m3 -n \".\\{120\\}$pat.\\{200\\}\" BRT.txt | head -3; done"
}
```


### [2026-09-06T15:21:40.612Z] TOOL RESULT

```
### aetauuant
### aētauuaṇt
### aetavant
### yatāra
### yatara
### atāra
### iθa
### i0a
```


## [2026-09-06T15:21:43.387Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c BRT.txt && head -c 1500 BRT.txt && echo && grep -c \"aeta\" BRT.txt; grep -o -n \".\\{80\\}aēta.\\{150\\}\" BRT.txt | head -5"
}
```


### [2026-09-06T15:21:43.467Z] TOOL RESULT

```
4803500 BRT.txt
Google
This  is  a  digital  copy  of  a  book  that  was  prcscrvod  for  gcncrations  on  library  shclvcs  bcforc  it  was  carcfully  scannod  by  Google  as  pari  of  a  projcct
to  make  the  world's  books  discoverablc  online.
It  has  survived  long  enough  for  the  Copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject
to  Copyright  or  whose  legal  Copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books
are  our  gateways  to  the  past,  representing  a  wealth  of  history,  cultuie  and  knowledge  that's  often  difficult  to  discover.
Marks,  notations  and  other  maiginalia  present  in  the  original  volume  will  appear  in  this  flle  -  a  reminder  of  this  book's  long  journcy  from  the
publisher  to  a  library  and  finally  to  you.
Usage  guidelines
Google  is  proud  to  partner  with  libraries  to  digitize  public  domain  materials  and  make  them  widely  accessible.  Public  domain  books  belong  to  the public  and  we  are  merely  their  custodians.  Nevertheless,  this  work  is  expensive,  so  in  order  to  keep  providing  this  resource,  we  have  taken  Steps  to prcvcnt  abuse  by  commercial  parties,  including  placing  lechnical  restrictions  on  automated  querying. We  also  ask  that  you:
+  Make  non-commercial  use  ofthefiles  We  designed  Google  Bo
94
```


## [2026-09-06T15:21:48.086Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o -n \".\\{60\\}aeta.\\{160\\}\" BRT.txt | head -12"
}
```


### [2026-09-06T15:21:48.155Z] TOOL RESULT

```
2551:^aöinahe  , ,  V.  frajasqn  .  .  ava  °tim  nasupiknn  lanaeta 8. 100;  —  ä^ravamm  yaoida'i^ö  (sd.)  . .  . .  apa  'tarn  disiam  (sd.)  baray^n  apa  -t?m Hahmiii  natre  ".  .  einem  solchen  Mann  aa/jnjni  (iariy;
2559:tae^va  äaxmagh'a,gaonaAe^a  (sd.)  ..  N.f*j;  "/(?);  —  saetari frV  paiii  3ya  ztma  bavainii  V.7.54;  ■ — \gätava  .  .  *'oa'>  ,  ,  N.  A;  —  yetiie  '6a "le  malsma  .  .  yaiibyö  .  .  /rasnayiinte  V. ;  mazda
2561:  lässt"  V.  ^'.23;  —  bei  rela-,°ö(J  a^ia  yä  kaine  aetakmut  puir-at  *mi- tivisch  angeschlossenem  Nomen:  yat  °te\mar?x^iliti  —  '^hat<anta  .  .  7>)r?zyqn  .  . yei  mazdayasna  . .  taH.apaya  nasHum  fra- '
2805:es  heiligen  Rechts, zi  asti  äiiiya  kata  (statt  NS.)  aetake  yat:  djg  jjjren  Leib  verwirkt  haben  -;  wo  ist irisiahe  ".  .  so  (wie  beschrieben)  ist  die  der  .  ."  V.  \J.  9". vorschriftsmässige  Kammer
3038:i.i^;  F. 7;  —  °y?mäi  vimanö.- wtLchstn':  j'ovanam  ..  aetavat  karstanam' AJtn  V.J.  7;  15;  —  'yanqm  ma^ranqm altavat  °tanam  "Getreide  ..  so  viel  vom  Vt.  10.  20;  —  -yqm  ifaaiirim  (sd.)  YL gesäten,  s
6594:  *ayqn  aivyästis  (sd.)  ar^Aat 'H.g;  — , paoiryeAe  pascaeta  * Aaza>irS.z7mahe  *iwa- ' rvsS(sd.)  as  V.2.19PÜZ.; —  al  aipi trns anhaitl  ustä  (sd.)  V.^o.ii;  —  negirt: V.^/.S,  s.  oben.  a)  mit  DaL:  uSa  m a
7211:  yakmi  faiti  "pamfäd (sd.)  sptntasca  mainytd  anrasca  aetahmt paiti  at  'te  Ytip.  45f.;  —  ätari  .  . .  .  matsAänS  altat  si'arMiS  hangsrrfiitne  yat •öwYt.  75.47;  —  äat  vö  kascH  maiyänqm sharing  'tun  
8965:e  yat  irisiahe  V. 5. 10;  —  ci-ants i  aukpn  aäe  'ta  aetalte  yat  irisiahe  "wie gross  sollen  die  Kammern  für  den  Leich- nam sein?"  V.J.  ii'>;  —  also  ..  asii däitys  kata  (statt  NS.)  ..  iristake  V.5.
12463:W.  11.  ig— 12. 1; Yt.  7^.  89;  —  us»M^lala  masyäka  staeta ahm  . .  nTsta  (sd.)  'va  \.  18.16;  —  'va apa.dvaraia  Ytj.  7;  —  vil  apqm  ^a patmtu  vT  'väahs  vT  'vaysil  (NPf.)  Y. 70. 1 ;  —  paitistätSe  t>
12778:,  Y./^.ia,  14,  N.i^;  —  *tanu.pn%B . zaota  dakma  u^.sraetarö  yezi  -im  tatm.- fmh»m  *v^an .  .yezi  äat  'im  tiBii  ianu.- p»r3k»m  *v^ar3  N._yß;  vgL  jdi';  —  miinm ,.yai  Vä  'im  aiwi.druzaiti ..  nmünB.paiti
12847:  fest  im  Gedächtnis  behalten, immer  daran  denken':  siaeta  yemya  .  . dadräna^*  paid/äna  Y.55.6; — yal  dim (nämt,  ahutum  vairTm)  .  .  aakus  .  .  asa- xtai  (sd.)  *sa^qs  dadrän5'°'^  ..  Y.  sg. 10.  3)    
14891: tl  aStahe  'ti  V.22.  2f.'3>;  — iat  astahe  'ti  ..  azaeta  (Sp.  2240.)  V. iK  68**;  —  ait»)n>m  ijaoiinanqm  .  . altahe  'ti  .  .  duye  saite  upaeananqm  upä- «3(V  (Sp.  224  m.)  V.  4.  2o'4).  '4)  zur Bez
```


## [2026-09-06T15:21:55.485Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"aetavant\" \"aetavat\" \"yatära\" \"yatara\" \"atära\" \"aiara\" ; do echo \"### $p\"; grep -o -n \".\\{70\\}$p.\\{170\\}\" BRT.txt | head -4; done"
}
```


### [2026-09-06T15:21:58.313Z] TOOL RESULT

```
### aetavant
### aetavat
3038:rätava  V.i.i^;  F. 7;  —  °y?mäi  vimanö.- wtLchstn':  j'ovanam  ..  aetavat  karstanam' AJtn  V.J.  7;  15;  —  'yanqm  ma^ranqm altavat  °tanam  "Getreide  ..  so  viel  vom  Vt.  10.  20;  —  -yqm  ifaaiirim  (sd.)  YL gesäten,  soviel  vom  w
### yatära
4190:t"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"
12778:rö . .  myazä»m ^yBi.dim  harfkäna  (sd.)  Y.  Ä  2 ;  —  tni\nm . .  yatära  vä  'im  paurva  fräyazäiti  Yt  lo. 9;  18;  — yirnl!  kur^naol yaia  -im  *jiasat< (sd.)  ahurB  ,  .  V.  2. 3a;  —  psurvS  .  ,  yat< 'im  usla  uzävqnayat  (sd.)
15728:^ uifhistaiti  "qui  prior  surgit"  V.iS.a6;  26, Yt  14.  44');  —  yatära  (sÄ)  vä  als  °rva'> (^Pm.) /räyatmU  Yt.rj.47;  lO.g  (NSf.); —  yahmal  hala  'rvS'ä  snao%S  (sd.)  .  . inalzät  V.2.  32;  —  'rvai'>  (NPol)  täyüm . .  bU^ySima
17573:•  j.  fraxänio-,  fraSnin-'*  Adj.  'providus, sorglich,  besorgt':  yatära  va  dim  paurva fräyatsiti  fraoni  °tii  (ASn.)  avi  manö *zrasdätsil  atfuhyat  (sd.)  haca  Yt.  10.  9"; —  yahmäi  'ni  avi  manB  mihrB  jasaitt avai^he  "welche
### yatara
### atära
4190:"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"
12778:ö . .  myazä»m ^yBi.dim  harfkäna  (sd.)  Y.  Ä  2 ;  —  tni\nm . .  yatära  vä  'im  paurva  fräyazäiti  Yt  lo. 9;  18;  — yirnl!  kur^naol yaia  -im  *jiasat< (sd.)  ahurB  ,  .  V.  2. 3a;  —  psurvS  .  ,  yat< 'im  usla  uzävqnayat  (sd.)
15728: uifhistaiti  "qui  prior  surgit"  V.iS.a6;  26, Yt  14.  44');  —  yatära  (sÄ)  vä  als  °rva'> (^Pm.) /räyatmU  Yt.rj.47;  lO.g  (NSf.); —  yahmal  hala  'rvS'ä  snao%S  (sd.)  .  . inalzät  V.2.  32;  —  'rvai'>  (NPol)  täyüm . .  bU^ySima
17573:  j.  fraxänio-,  fraSnin-'*  Adj.  'providus, sorglich,  besorgt':  yatära  va  dim  paurva fräyatsiti  fraoni  °tii  (ASn.)  avi  manö *zrasdätsil  atfuhyat  (sd.)  haca  Yt.  10.  9"; —  yahmäi  'ni  avi  manB  mihrB  jasaitt avai^he  "welche
### aiara
8743:stsm  paityämraot  ¥.27.4;  F.5;  — vXspäyämca  "tatim  .  .  'tätfm  aiararum yazamaide  Vt.iS.a;  —  vahistimla  ahütn .  .  vlspäyümca  HSs  (statt  Akk.)  P,  48;  — .  sadr>m  urvistnmla  (sd.)  ,  .  -tatsm  nimra- vaite tistryö  .  .  ust
12376:. .  X. z.  i;  3.  $;  —  '>'«*  maiia  iariam idä  Uta  'yJ'maiy  apaiaram  iartam  av(^ visam  X.  2.  3;  —  'y^patiy  (sd.)  kartam vainataiy  naibam  (sd.)  ovo'  visam  .  .  X. 7.  3 ;  —  'yaiy  paruvä  xiaya%iya  yata  aAä" avaijilm  .
14018:.  statt  Dat)  vorlügen',  mit  wie  ?Adv.-  dahyauva  vasiy  (sd.)  aiara^  Bh.  ;.  10;  — MnAio\g.^vc.'B.eAe.:ÄauvMSrahyaara>il  i,„.j,„  dahySum  .  .  pstuv  hacä  hainäyä adurujiy^:  adam..  Bh./.ii.  3)  'Je-  j,ai,j  .^,j*  D.4-3;  Bh.^
16803:  absolut:  taünef  .  .  bartntö  (NP.)  «ä"? maiy  ufastam(Stvaz.)  aiara^Sh.i.9usv.;i  ^asiamianti  vasMtd  .  ,  Yt.  10.  20;  — — yaha  ml  barm  upasiam  Yt  13.  t;  5. 63; —  barimnö  vä  vazfituUS  vä  N.  ^',  — hä  mihara  aamala..iA
```


## [2026-09-06T15:22:18.568Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs 2>/dev/null; SP=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 224 -l 224 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf $SP/pg224hi && python3 - <<EOF\nfrom PIL import Image\nim=Image.open(\"$SP/pg224hi.png\")\nprint(im.size)\nw,h=im.size\n# node10 region approx fractions from 1545x2000 view: x 840..1110 /1545, y 1055..1150/2000\nbox=(int(0.54*w),int(0.525*h),int(0.74*w),int(0.578*h))\nim.crop(box).save(\"$SP/c224_n10.png\")\nbox2=(int(0.20*w),int(0.27*h),int(0.42*w),int(0.34*h))\nim.crop(box2).save(\"$SP/c224_n1.png\")\nEOF\nls -la $SP/c224_n10.png $SP/c224_n1.png"
}
```


### [2026-09-06T15:22:21.900Z] TOOL RESULT

```
(3400, 4400)
-rw-rw-r-- 1 sfmqrb sfmqrb 3402 Sep  6 11:22 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb 4744 Sep  6 11:22 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c224_n1.png
```


## [2026-09-06T15:22:23.671Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c224_n10.png"
}
```


### [2026-09-06T15:22:23.689Z] TOOL RESULT

```

```


## [2026-09-06T15:22:39.880Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c224_n1.png"
}
```


### [2026-09-06T15:22:39.895Z] TOOL RESULT

```

```


## [2026-09-06T15:22:51.044Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD edar/edon\"; grep -n -i \"ēdar\\|edar \\|ēdōn\\|edon\\b\\|ed-ar\" PHD.txt PHD_mackenzie.txt | head -20; echo \"### NYB\"; grep -n -i \"ētar\\|ētūn\\|edar\\|edon\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T15:22:51.118Z] TOOL RESULT

```
### PHD edar/edon
PHD_mackenzie.txt:979: Aleksandar ['Ikmdll M 'lxsyndr, N Iskandar] Alexander (of Macedon).
PHD_mackenzie.txt:2190:edar [LTME < A I-tnh I M )ydr, N --] here.
PHD_mackenzie.txt:2191:edon [)ytwn l I N idun] thus, so.
PHD_mackenzie.txt:6988: likewise hamedon, hamgonag.                mihr.
PHD_mackenzie.txt:7604:sisvmbrium sisimbar.                          so edon, hamgonag, oh, Owon.
PHD_mackenzie.txt:7783:testing uzmiiyisn.                        thus edon, oh.
PHD.txt:189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
### NYB
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
1413:duxt [dwht'; BRTH] daughter 2%. 917, 1518.25 259, 261, 11629; with the indef. art. duxt-ē [BRTH-y] 14%; cas. obl. duxtar [dwhtl] 152°; 6 duxt [BRTH] 957; hac pus tài ~ both sons and daughters 24?3, Av. (748) dugedar-, duydar- nom. dugodā, duyča; MPrs dwat (dwxš, v. Benveniste, BSL 47, 1951, 21; KZSPrs 1. 26 dwhSy); NP duxtar, archaic also duzt.
1704:Götarzön [gwtleyn'] patron. of Gētarz (Lat. Gotarzes) 115%. — Cat. 54-55. The patron. suff. -én, as against common -dn, is exceptional; or -in?
2016:homānāk [hwm’n’k] like, similar, re- sembling: nézak ~ like a javelin 8517; 8515, 864. 10427; pūt hangošitak (q. v.) ~ 7613; 865; 6 ~ 119-120 passim; kanik-& i 6 kanikän ne ~ à maiden who does not look like maidens 754; ētūn ctgēn
2017:vat... ~ like a wind 717; ētēn ~ cigón + subst. like, as 7123. 86%; 6% ētūn ~ cigon ke ... he resembles one who 6974; ēgēn
2080:Hušētar [hwšytl] the first of the three still unborn sons of Zartuxšt who will appear in the trimillenial apocalyptic period: 7114. 9619.17.39. — Paz. Hušečar; from Av. (384) Uxsyat.orata-.
2081:Hušētarmāh [hwšytlm”h] the second ap- ocalyptic son of Zartuxšt who will appear after Hušētar: 7114, 988-14.16, 999. 11017. — Paz. Huseöarmäh; from Av. (384) Uz- šyat.nomah-, cf the spelling ?wšytnms DkM 44! (-ms inverse spelling of -mah).
2277:ke [MNW] with encl. MNW-m = ké-m, MNW- = kē-š ete.; MNW-c = ké-c: A. interrog. pron. who? whom ?: én rētak kē hast? 161”; emphasized kē hàn he? who art thou, say? 561%; as cas. obl.: kē pat panāh kunom? 749; ke ax"eš hom? to whom do I belong? 624; én zanišn ké (ag.) kart? who made this deadly shot? 323; — gen. + ke: En pus + kē hast? whose son is this? 1621; or hàn 4 ke: ruvan... hàn t kē...? whose soul? 31?3; — governed by a prep.: hac ke? nazd ke? tài ke? ete. ; — indirect interrogation may be introduced by ku: gob ku to hac fradandän i ke hah 1517-18; without kū: (én-ic dine) hac pusa- ran...ı man ke zīvēt u kë mīrēt 219-19; nē (Gkah hom) i ke hàn 574. — B. rel. pron. who, which ; with pronominal antecedents : man ke, tē ke, šmāh ke, či ke, čišan ke, -$...ke, han (kas) ke, har (hàn) ke; hec (kas) ke both in a positive (6417-18) and a negative (11817-18) sense; 1. used as cas. rect. and cas. obl: (subj.) asvdr-é nest ke ... ētūn cigon to 1519-316; (dat.) (Kävul) ke Mihr u Mah pat pušt hah K. over which Sun and Moon keep guard 317%; (agens) Krisäsp ke Dahāk vanit K. by whom D. was vanquished 1064-5; — its syntactic function may be marked by an enclitic referring to the antecedent: (hu- nušk + Gana Menoi) kē-š ciš-ic pat poc nest (the progeny of the Evil Spirit) for whom there is nothing to furnish an ex- cuse 1021-?; but dastavar ké-§ guft ku there was a theologian who said 1018, also but ké-§ guft ki someone has said (taught) that 103? ; Gišān kē-šān Yam kirrenit those by whom Y. was cut to pieces 10145; — the gen. is regularly ex-
2333:etc.; — b) consecutive: so that, mostly eton ... ku 2%, 32, 1119, 7118 ete.; ögön ku 811; viyāk hàn ogon ne būt ku that place was not such that ... HajB: 9; with vbs.: ētūn kunom ku I shall see to it that ... 62. 205-5; &ön būt <ku> it so happened that 1419-11; cf et bavét kū this much will come true that 5320; 7726-27; —
2335:adak-ic though . . . yet 5525-26; — d) after all vbs. of saying, feeling, judging and the like: göbet ku, api-$ guft ku he says, he said that, passim; very often intro- ducing direct speech, and serving as a quotation mark; often anticipated by čton: amäh čton äsnüt ku we have heard that 34; api-män eton sahist ku and it seemed to us that 89-7; ētūn ménés ku you may well think that 3312; äfrinv kart" ku prayed saying: "... P2:5; kū or ku tdi after framütan (g.v.); ku mà hakar after tarsitan (g. v.); pat én ku to the purport: “‘. . .” 922; pat én kar frestit ku sent you with orders to ask: “...” 1312; o Säsän dāt hend ku patmoc were given to S. (with the message): ''dress yourself up!" 218. — e) én ku, et ku the fact is that ..., passim; kū alone intro- duces explanatory glosses: ,,that is to say" 162. 375-8 and passim; pat späsdäreh én ku tuvān kartan ku it is through grati- tude that one can attain that ... 6511-12; fraytst kū, v. s. v. frayist. — 5. a dependent question, whether introduced or not by an interrogative, is preceded by kū placed immediately after the governing vb.: tà
2532:ménitan [mynytn'], opt. 2nd p. sg. meneš 3312, to think, with kū that, often ētūn ~ ku: 40° ete. (as to 469 sq. v. s. v. matar); parenthetically ménam this is my opinion 56%; imp. men! just think! lo and behold! 5815; — with an obj.: ahlä- yéh ~ to think righteousness, that which is righteous in an absolute sense 7873, opp. mitöxt (q. v.) ~; veh martom ~ to think well of, to be well disposed towards men 781, opp. tar (g. v.) ~; mēnam tē rād nēvakēh I mean well for thee 4721; et i tē
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
4286:Xion [hywn'] Turkish peoples in Central Asia and East Iran, pl. cas. obl. ~-dn, 18-30 passim. 613-22. — Av. (1858) hyao- na-; Paz. hayün Skr. v. turuska-samüha (Aog.); cf NP hayün a dromedary used by express messengers; Chin Hiung-nu = Huns.
4382:xučš [NPŠH; hwyš] 1. refl. pron. self, valid for all persons, a) referring to the agent = the logical subj.: -š ~ hécak hac cäh ul hixt he himself hauled up 1519; b) as an obj.: ~ hac ranj äsän kartan to relieve oneself of trouble 1313-14; c) after a prep.: vinäskäreh andar ~ bē guft 3474; (šmāh) ~ rād 45°; d) as a refi. poss. pron.: 4 ~, passim, e.g. hac avatdi i avēš 51"; ruvün i ~ rädY F:2; hac har i ~ F:3; or ~ alone, or kan i ~, both placed before their subst.: pat ~ casm 80%; hac ~ xünak ŠPrs: 10; api-š ~ GfrinY kart" and he praised himself Pl: 10-11; hàn i ~ xvatāt 5%; also fravahr ēt i ~ 88%; har kas õi i dit ētūn döst bavet cigon i ~ everyone will be as friendly to the other as to himself 10412-15; e) as an attr.: ~ Zartuxšt 5228; — emphatic form ~-tan or (659. 928) tan 4 ~ (v. tan): ~-tan u asvārān ranjak mā dārēt 8? ; —-tan o marg
5140:dugedar-, duydar-: duxt Duydö.vä-: Dugdäv
5848:’ydr: ētar
6545:ēdar: ētar ēdun: &tön ēmā: amāh ēmēk: ēv-mēk ēra: ēr ēranaga: ērānak www .parsianjoman. org | vll
6658:Huščšar: Hušētar
6659:Husésarmah: Hušētar- māh
7132:ēšar: ētar aštin: eton ēvār: ēvārak
```


## [2026-09-06T15:23:03.122Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HUB\"; grep -o -n \".\\{80\\}[iī]dar.\\{200\\}\" HUB.txt | head -6; echo \"### ARY latin index\"; grep -n -i \"idar\\|idun\" incoming/ARY/ARY_latin_index_pages.txt | head; echo \"### ARY fa\"; grep -n \"ایدر\\|ایدون\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-06T15:23:03.220Z] TOOL RESULT

```
### HUB
### ARY latin index
4502:FADAR (OLD SAXON) oS gp-St PIDAR, PITAR, PIT, PID
### ARY fa
```


## [2026-09-06T15:23:12.150Z] TOOL CALL #47: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:23:12.158Z] TOOL RESULT

```


```


## [2026-09-06T15:23:15.807Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%AF%D8%B1",
 "prompt": "Give the full Persian entry: etymology of ایدر (idar), meaning, Middle Persian antecedent, related forms, and any cited sources."
}
```


## [2026-09-06T15:23:16.803Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ceterus",
 "prompt": "Give the Latin entry for ceterus: etymology (PIE reconstruction, components), meaning, and descendants including et cetera."
}
```


### [2026-09-06T15:23:23.080Z] TOOL RESULT

```
# Latin Entry: Ceterus

**Etymology:**
From Proto-Italic *ke-eteros*, combining *ke* ("here") and *eteros* ("other"). The Proto-Indo-European reconstruction traces to *h₁éteros* ("other") with the suffix *-teros*.

**Meaning:**
The adjective signifies "the other, remainder, rest" and conveys "besides" or "also." It functions as a first/second-declension adjective with feminine *cētera* and neuter *cēterum* forms.

**Notable Derivatives:**
The most prominent descendant is *et cētera* (literally "and the other things"), commonly abbreviated as "etc." in modern English usage. Another derived phrase is *cēterīs paribus* ("all other things being equal"), frequently used in economics and philosophy.
```


### [2026-09-06T15:23:24.540Z] TOOL RESULT

```
# Persian Entry: ایدر (idar)

**Etymology:**
The word derives from Middle Persian *𐫀𐫏𐫅𐫡* (ʾydr /ēdar/), combining *𐫀𐫏𐫅* (ʾyd /ēd/, "this") with *𐫡* (*r), tracing back to Old Persian *𐎡𐎭𐎠* (i-d-a, "here") and Proto-Indo-Iranian *Hidʰá.

**Meanings:**
The adverb carries three distinct senses:
1. "here" (synonym: اینجا - īnjā)
2. "now" (synonyms: حالا - hālā, اکنون - aknūn)
3. "behold"

**Related Forms:**
Cognate words appear across related languages, including Northern Kurdish *here* and Central Kurdish *ئێرە* (êre), both demonstrating metathetic variation. Hindustani cognates include इधर/ادھر (idhar, "here") and उधर/ادھر (udhar, "there").

**Pronunciation:**
Classical and Dari forms: /ʔeː.ˈdar/ or /ʔiː.ˈdar/; Iranian formal: [ʔiː.d̪æɹ]; Tajik: [ʔe.d̪äɾ]

**Sources:**
Referenced in Hayyim's *New Persian–English dictionary* (1934) and Steingass's *Comprehensive Persian–English dictionary* (1892).
```


## [2026-09-06T15:23:40.903Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/yes",
 "prompt": "Etymology of \"yes\": Old English gese/gise, its components, and the pronominal *i-/ja- element. Also note any mention of \"yea\"."
}
```


## [2026-09-06T15:23:41.347Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/yet",
 "prompt": "Etymology of \"yet\": Old English giet/gieta, proposed origins, and whether it is connected to a pronominal stem *i-."
}
```


### [2026-09-06T15:23:47.455Z] TOOL RESULT

```
# Etymology of "Yes"

## Origin and Components

The word "yes" traces back to Middle English *yis*, derived from Old English *gise*, *gyse*, or *gese* meaning "so be it!" This term combines two elements:

1. **"Gea/ge"** - meaning "so" (related to "yea")
2. **"Si"** - meaning "be it!" reconstructed from Proto-Germanic *\*sijai-*

The deeper root is the Proto-Indo-European optative stem *\*si-* from the root *\*es-* meaning "to be."

## Relationship to "Yea"

According to the source, "yes" was "originally stronger than simple *yea*." The entry notes that "yea" derives from Old English *gea* or *ge*, meaning "so, yes," ultimately tracing to Proto-Germanic *\*ja-* or *\*jai-* and the pronominal stem *\*i-* from PIE *\*yam-*.

## Historical Usage

Shakespeare primarily used "yes" as a response to negative questions, while the repetition "yes, yes" expressing impatience appears by the mid-15th century. The noun form emerged around 1712, followed by verb uses beginning in 1820.
```


### [2026-09-06T15:23:49.737Z] TOOL RESULT

```
# Etymology of "Yet"

The word "yet" traces back to Middle English, derived from Old English *get* and *gieta*. According to the Online Etymology Dictionary, it originally meant "till now, thus far, earlier; at last; additionally, in addition to."

## Origins and Connections

The term is classified as an Anglo-Frisian word with cognates in Old Frisian (*ieta*) and Middle High German (*ieuzo*). Its ultimate origin remains uncertain, though scholars have suggested a possible connection to the Proto-Indo-European pronominal stem *\*i-*.

## Usage Development

As an adverb, "yet" expresses continuance of a former state (as in "while we were yet sinners") or reference to the present moment (as in "are we there yet?"). The word later developed into a conjunction around 1200, introducing "an additional and somewhat adversative fact or circumstance."

Notably, related Germanic languages express this meaning through different etymological roots—specifically descendants of Proto-Germanic *\*noh-* (such as German *noch*), which derives from a different Proto-Indo-European source (*\*nu-qe-*, meaning "and now").
```


## [2026-09-06T15:24:02.358Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%A9y",
 "prompt": "Summarize the Proto-Indo-European pronoun *éy / *h₁e: its meaning, stem alternants (e-, ey-, i-), derived terms, and descendants in Indo-Iranian, Latin, Germanic. Note any Pokorny page reference."
}
```


## [2026-09-06T15:24:04.854Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%DB%8C%D8%AF%D9%88%D9%86/",
 "prompt": "Quote the فرهنگ معین (Mo'in) and لغت‌نامه دهخدا entries for ایدون, including any bracketed origin tag such as [په.] and the glosses."
}
```


### [2026-09-06T15:24:10.751Z] TOOL RESULT

```
# Proto-Indo-European Pronoun *ís / *h₁e

## Meaning
This pronoun functioned as a "this" demonstrative and third-person pronoun, meaning "he" or referring to a mentioned entity.

## Stem Alternants
The entry documents three major competing reconstructions showing different stem forms:
- Andrew Sihler's system uses *ís (masculine nominative singular)
- Donald Ringe proposes *éy for the masculine nominative
- Robert Beekes reconstructs *h₁e with the laryngeal prefix

Additional stem variations include *i- and *ey-, reflecting different phonological environments and case formations.

## Key Derived Terms
Notable formations include:
- "Which" relative pronoun derivatives
- *óynos formations meaning "one"
- Demonstrative compounds like *éteros ("the other of two")

## Indo-European Language Descendants

**Indo-Iranian:** Sanskrit íti ("thus"), Avestan ūitī/uiti

**Latin:** ita ("thus"), item ("likewise"), iste ("that"), ipse ("self")

**Germanic:** Reflexes through Proto-Germanic *ja

**Greek:** Ancient Greek ei ("if") and related demonstrative particles

## Reference
Julius Pokorny's etymological dictionary includes this entry on page 281 of volume 1.
```


### [2026-09-06T15:24:12.717Z] TOOL RESULT

```
# Entries for ایدون (Eidun)

## فرهنگ معین (Mo'in Dictionary)
**Origin tag:** [په.] (Pahlavi)

**Definition:** "( اِ ) [ په . ] (ق . ) ۱ - این چنین ، این گونه . ۲ - اکنون ، الحال ."

This translates as: (1) "this manner, this kind" (2) "now, at present"

## لغت‌نامه دهخدا (Dehkhoda Dictionary)

**Origin:** The entry traces the word through multiple classical Persian sources, noting its Pahlavi root *ātōn* (meaning "thus" or "in this manner") and its Old Iranian ancestry from *āytōnā* and Avestan *aēitōnənt*.

**Core meaning:** "اینچنین. اینچنین و بدین طریق. همچنین" — "thus, in this manner and way, likewise"

The dictionary provides extensive poetic examples from classical poets like Roudaki, Ferdowsi, and others demonstrating its consistent usage meaning "in this manner" or "thus."
```


## [2026-09-06T15:24:20.555Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"#### SKT et cetera / item / identity / yes / yet / if\"; python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'Etcetera',r'ETCETERA',r'et cetera',r'\\bITEM\\b',r'\\bIDENTITY\\b',r'\\bYES\\b',r'\\bYET\\b',r'\\bIF\\b, conj']:\n    ms=list(re.finditer(pat,t))\n    print('##',pat,len(ms))\n    for m in ms[:2]:\n        print('  ',' '.join(t[max(0,m.start()-100):m.start()+450].split()))\nEOF"
}
```


### [2026-09-06T15:24:23.116Z] TOOL RESULT

```
#### SKT et cetera / item / identity / yes / yet / if
## Etcetera 0
## ETCETERA 0
## et cetera 0
## \bITEM\b 0
## \bIDENTITY\b 0
## \bYES\b 0
## \bYET\b 0
## \bIF\b, conj 0
```


## [2026-09-06T15:24:26.628Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 SKT.txt; echo; echo \"---\"; python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nprint(len(t))\nfor pat in [r'[Ii]dentity',r'[Ii]terate',r'cetera',r'\\bYet,',r'\\bYes,',r'\\bIf,']:\n    ms=list(re.finditer(pat,t))\n    print('##',pat,len(ms))\n    for m in ms[:2]:\n        print('  ',' '.join(t[max(0,m.start()-150):m.start()+400].split()))\nEOF"
}
```


### [2026-09-06T15:24:29.149Z] TOOL RESULT

```
This  is  a  digital  copy  of  a  book  that  was  preserved  for  generations  on  library  shelves  before  it  was  carefully  scanned  by  Google  as  part  of  a  project to  make  the  world's  books  discoverable  online.
It  has  survived  long  enough  for  the  copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject to  copyright  or  whose  legal  copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books are  our  gateways  to  the
---
2620367
## [Ii]dentity 2
   e foot (whence the sen.4cs of foot-stool, gallery to sit in, Arc, must have been evoUc<), since there can be no doabi as to the identity of the L. and Gk, words). — Gk. «u9i-. crude form of woCif foot. See Voo^. ^ C^ I PEWET. t)u. puyt^ 'a pue/ Hexlum; borrowed from F. puyt. Pewet, Peewit, the Upwiim. (E.) Also puH (PhiUips). Named msm its pljiinUve cry; sec Peevish. Pewter. (F. - E. ?) M. E. pmtir. - O. F. prutre. Ptautrt, piautrt, a kind of metal (Ro<)aefort). I
   excise (i), flout, sconce (1). I German from Fretuh from Latin; < coLshicT. Frcneh from Law Latin from Latin- cadef, identity, mai^tift. meuageut, m«i\t\,\ tanTowftV,WL\p«V^^»'»**.w>,cioc^ooc« I/ixlian from Lou Lafm Jr^n falchion. Frtneh from ftaJimm frtm from Latin : medal. Proven^ from I.atim : Fretuh from Prffoenfol from 10^ barnacles, corsair. Italian from Latin ] allegnM^ a\>\\ude., bellaiinnna, brrre, brc*coal^' VI. DISTRIBUTION OF WORDS, ETC. ti1ettiiite,ditto.do(;e,
## [Ii]terate 1
   s, oblique (a rare word>. The ori^;. sense of tiiptis is 'bent;' cf. Russ. luka, a bend, Lithnin. hnkti, to bend. (^ I-AK.) Obliterate ; see Lioiment. Oblivion i,F. - L,^ F. oblivion. * L. Rcc. P^iitticHtm, foi^el fulness. — U ^Uu- isei, to forget. Perhaps from ol, over; iiiuscett*^ to grow livid or dark, from base of /im-iJus, livid ; see Itlvid. Oblong: see Long (i). Obloquy ; sec ZioqaaotooB. Obnoxious ; sec Noxioaa. Oboe ; see hautboy, nmler Altitude. ObolUB, a small U
## cetera 0
## \bYet, 0
## \bYes, 0
## \bIf, 7
   to (F.-O.H.G.) Sec Blow(i). •pcslc iDJoriousty. (L.— — Gk. $^aaif>yf^itt¥, .^GIcffAdfT^iy^oT, adj.. sj^ieak* for SKotf.; from /JAdi^ir, If, to bun : and ^i7/«7, 1 uv ; s<c Fame. r.-L.-Gk.) M.E. ^Al- io blame. *L. 6/as- lU. abo to b1«me.-Gk. See Blow (I). [t) Sec Bleat. [iy SeeBlow(i). (»). Sec Blow. (I) Bflberry. l<t),and OV See Blink. to deceive. (Sciind.) to ^Mr, to dim. •Swed. /pjr augu, to ciuiver [jbcforc the tyt<; i^iu of a beat of sinimjcr ; cf. \.tHra, to bl
   plot. (F.«L) U. EL €kmfekt.^ O. y. «I«/Mrf. a bead^bcK. «rcatJi.-.O.F. «U/tr/, Keatl'dreia. » O. F. cMmfe, a cope ; Mvohapenm. «Op« (If, a hood, cape. (F.-LowL.) M4 E. /jr/V. varioitt of rd/v. a ope ; see Oapa ■bore. (For the «. cf Icel. Jt,i/>a.) oaOApo. (F. *L.) M. E. esca/^n - C). I', tuafer (K. ^chaffer), to escape, lit. Ui slip out of one'i cajjc. » L. «x ra//a» oat <tf one'* ctjic: trc Capo (t) above. •CMpe; ktiOrl Utt /xi-tf/V (ftUive). OAX>a (j), twratllan') j w
```


## [2026-09-06T15:24:36.354Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['LEW_1910.txt','LAT.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print('=====',f,len(t))\n    for pat in [r'c[eē]terus',r'\\bitem\\b',r'\\biterum\\b',r'\\bidem\\b']:\n        ms=list(re.finditer(pat,t))\n        print('##',pat,len(ms))\n        for m in ms[:2]:\n            print('  ',' '.join(t[max(0,m.start()-200):m.start()+400].split()))\nEOF"
}
```


### [2026-09-06T15:24:38.699Z] TOOL RESULT

```
===== LEW_1910.txt 619063
## c[eē]terus 0
## \bitem\b 0
## \biterum\b 0
## \bidem\b 1
   at, mate, mates II 82 maze IT 7 mba (alter tosk.) I 483 mbaj, mban, mbar (tosk.) J 483 mbars I 457 mberatessse, mberat (alter) J 457 mbese II 161 mbi, mbe I 36 mbl’ed I 780 mbl'ete IT 62 mbl’oda, mbl’idem I 780 122 mbram, mbrapen I 681 mbrat (tosk.) I 457 mbret I 683 mbreme I 681 mbruj, mbriin I 334 mbit, mbis I 259 mejk (sudgeg.) 1508 mejton II 56 mek., mekan I 508 mekem, meke I 508 metene, metéze IT 123 meté (tosk.) IT 123 mel’k (tosk.) I 508 mengi IT 28 mes IT 58 mesin I 460 megaster, megaster IT 55, 471 meme IT 21 mén (tosk.) IT 33 mendafse IT 49 menge II 34 mengere IT 28 ment IT 30 merkos
===== LAT.txt 4601625
## c[eē]terus 2
   io m.n.; aliae f. A cote de aliud, la langue vulgaire a cre4 un n. alium, d'aprbs alterum. Sens: "autre" en pariant de plus de deux. Il arrive quelquefois que la dis- tinction entre alius et alter et ceterus ne soit pas rigoureusement observ^e: alius, alii (pl.) traduisent aXXoC, aXXot. et 6 aXXoc, ol aXXoi,, T<Sr., Hau.456 ut alia (= cetera) omittam-, T.L.7,36 alia multitudo (= & ccXXoe orpaxos de Xen., Cyr.6,4,1) terga uertit; et l'on trouve aussi alius en corr^lation avec alter, comae en grec exepo£ p,ev ...ocXXo£ 8e.. . Alius r4p£te sert a opposer un individu ou un groupe k d'autres indivi
   eruix. cesso, -as, -are; cf. cedo. 409 ceueo -cessC, -is, -Ini, -Ituta, -ere: n'existe qu'en composition dans ar-cessS (?) in-cesso. D6sid£ratif, qu'il fant sans doate rattacher k cedb "s 1 avancer". ceterus, -a, -umr qui reste, restant, d'o 4 au pl. ceteri,-ae,-a "tous les autres, ceux qui restent”. Difffere peu dans 1 'usage de reli¬ quus, e.g. Cic.,Rep.6,17, qui globus reliquos bmnis complectitur, sum¬ mus ipse deus arcens et continens ceteros-, toutefois semble plus comprehensif, cf. Cic., Verr.5,87, erant perpauci reliqui, ceteri dimissi. - Ceteri designe un enseable par opposition k alii
## \bitem\b 28
   ad, in, apud, penes; ainsi Scaurus, GLK, VII 30,18 (d'apres Varron): ad et apud ac- cusatiuae sunt praepositiones, ut "accede ad me"; "qui domi nati sunt apud ne" (cf.Servius, Ae.1,34); et VII 31,7: item uitiose dicitur "senatum habere apud aedem Apollinis" quod "in aede Castoris" dici oportet); et Ulpien, Dig.50,16,63: "penes te" amplius est quam "apud te"; nam "apud te" est quod qualiterqualiter a te teneatur; "penes te" est quod quodam modo possidetur; cf.P.F.30,19. Reguliorement construit avec l'accusatif et employe - le plus souvent pres de noms de personnes (cf. toutefois apud aedem SC
   ce par d'autres adverbes a. adeo, a. certe, a. etiam, a. omnino, a. u§ro, a. contra, a. potius, a. for¬ tasse, a. denique, a. postremo, a. summum. iog auunculus Renforce de la particule -em (cf. ita, item), j .1 a donne autem: d’autre part, or. Conjonction qui se place generalement aprbs le pre- mier mot de la phrase, et qui correspond pour le sens au gr. 8s. Cic. se sert de quidem...autem pour rendre 1 'opposition p,ev...8e. S'emploie aussi, dans la 1. parlee, pour reprendre, sur le ton interrogatif, une affirmation contre laquelle on proteste, cf. Ter.Ad.940 fac: promisi ego illis. - Promist
## \biterum\b 12
   po ( *cappo? ), -Onis m.: chapon. La forme derivee en -o, -onis est la plus recente, non attest^e avant Martial. Cf. Charis. GLK I 103,36, capo dicitur nunc sed Varro de Semone latino (frg.105 G.S.) "iterum" ait "ex gallo gallinaceo castrato fit capus". L'existence de capus "tete" a peut-etre contribui a la dispa- rition de capus. Diminutif: capunculus (tardif). Martial, 3,58,38 scande la premifere syllabe longue; sans doute faut - il lire cappo, avec geminee expressive, comme 1’indiquent les derives romans: seul le campidanien kaboni remonte 1 capo ; les autres formes, it . cappone , fr. chap
   ob le sens propre du suffixe marquant opposition de deux est perdu) et av. at ara-. D'autre part, il existait, de ce aene demonstratif a deux themes, un d 4 riv 4 * itero-, que le latin conserve dans iterum (v. ce mot). Il se trouve ainsi que ceterum et iterum appartiennent a un meme groupe de aots indo-europeen. Le sens de: opposition de deux, est net dans ceterum, ceteri qui marque opposition d'un groupe k un autre. - Sur la particule qui en latin precfede *etero-, on ne peut faire que des hypothbses inconsistantes; cf. ceu. cetus, -i m.: 1° catace, thon; 4° la Baleine (constellation). Empru
## \bidem\b 64
   mme le note Probus, GLK IV 150,9, il.y a des cas ou la distinction entye et in est peu sensible; cf.Thes. I 485,35sqq. Lucilius, 1134, distingue ad et apud: sic xitem>apud se longe ali[u\d est, neque idem ualet ad se: \ intro nos uocat ad sese, tenet int<us apud se>; et Servius, Ae. I 34, apud semper in loco significat; ad, et in loco et ad locum. Du sens de "dans la direction de, vers" sont issues diverses accep- tions d^rivees, ainsi: "en vue de, pour" ( aptus ad, natus, idSneus ad); "aupres de, c.-A-d. en comparaison de, en proportion de"; "apprOchant", d'ovi "environ" (par ex. dans 1'emplo
   rosus " 7 ioXuxaAxoc", aerarius "concernant le bronze, ou la monnaie, le tresor"; et peut-etre aerdnis"i qu'on lit dans Isid., Or.13,1,53, ceruinus est color equi, quem uulgo gauranem dicunt. Aeranem idem vulgus uocat, quod in modum sit aerei aesculus - s« - coloris; mais dans le lib.Gloss. le mot est doune sous la forme aeramen, cf.Thes.s.u. et Sofer, 31 et suiv. M.L .343 (ae- et *aramen); aeramentum (v.Lofstedt, Phil. Comm. z. Peregr .Aeth., p. «31); aerugo (avec un doublet aeruca, -ae): rouille de cuivre, vert-de-gris; cf. ferrugo, lanugo, robigo; d'ou aeruginosus; les formes romanea remont
```


## [2026-09-06T15:24:45.559Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('LAT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('ceterus, -a, -umr')\nprint(' '.join(t[i-200:i+2200].split()))\nEOF"
}
```


### [2026-09-06T15:24:47.682Z] TOOL RESULT

```
eruix. cesso, -as, -are; cf. cedo. 409 ceueo -cessC, -is, -Ini, -Ituta, -ere: n'existe qu'en composition dans ar-cessS (?) in-cesso. D6sid£ratif, qu'il fant sans doate rattacher k cedb "s 1 avancer". ceterus, -a, -umr qui reste, restant, d'o 4 au pl. ceteri,-ae,-a "tous les autres, ceux qui restent”. Difffere peu dans 1 'usage de reli¬ quus, e.g. Cic.,Rep.6,17, qui globus reliquos bmnis complectitur, sum¬ mus ipse deus arcens et continens ceteros-, toutefois semble plus comprehensif, cf. Cic., Verr.5,87, erant perpauci reliqui, ceteri dimissi. - Ceteri designe un enseable par opposition k alii: Sali.Iu.74,1, ceteri formidine, pars ad Romanos, alii ad regem Bocchum profugerant ; aussi est-il souvent joint k omnes, cuncti. Le neutre 9'emploie adver- bialenent: ceterum, cetera "du reste” et depuis Salluste^ surtout dans Tite Live, ”«ais” (cf. pour le sens gr. aXXa, 'nxXXa, xa Xchtox), (de)cetero, ceteroqui(n). - Ancien, usuel et classique. Non ronan. Comprend 6videmment le mot qui se retrouve en ombrien, avec le sens de "alter”: etru "altero”, etram "alteram", etraf "alteras", etc., en face de lat. alter et de osq. alttram, etc.; c’est le deriv 4 en *-tero~, *-tro- des th&mes du demonstratif i.-e. *e- et *i-’, il se retrouve dans v. sl . jeteru "quelqu'un" (ob le sens propre du suffixe marquant opposition de deux est perdu) et av. at ara-. D'autre part, il existait, de ce aene demonstratif a deux themes, un d 4 riv 4 * itero-, que le latin conserve dans iterum (v. ce mot). Il se trouve ainsi que ceterum et iterum appartiennent a un meme groupe de aots indo-europeen. Le sens de: opposition de deux, est net dans ceterum, ceteri qui marque opposition d'un groupe k un autre. - Sur la particule qui en latin precfede *etero-, on ne peut faire que des hypothbses inconsistantes; cf. ceu. cetus, -i m.: 1° catace, thon; 4° la Baleine (constellation). Emprunt latinis 4 au gr. xo xrjTOS; assimile aux themes en -o-, il a pris le genre mas cui in ou anime (cf. fucus = to cfCxoc). Ancien (Pl.). Vg. transerit la forme grecque, Ae. 5,844, immania cete. D6riv6s latins: cetarius,-a,-um et cStdrius m., cgtdriun, n.; cf. cStdriae tabernae: tavernes de pecheurs de thons, deforme par l'6ty- mologie populaire en cretariae tabernae; cetosus (Arien.). ceu: particule marquant la coaparaison, qui s'emploie seule ou en correlation avec ita, sic, etc. Archalque; attest^e en po6sie depuis En
```


## [2026-09-06T15:24:56.648Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\n# find page tag mapping\nfor n,L in enumerate(leaves[:140]):\n    m=re.search(r'\\[pdf page (\\d+)\\]',L)\n    if n in (100,110,120,130): print(n, m.group(0) if m else None, ' '.join(L.split())[:80])\nEOF"
}
```


### [2026-09-06T15:24:58.394Z] TOOL RESULT

```
leaves 895
100 None 92 aldh- — albho- aldh- „Trog; Welle". Altn. ahla f. „Welle, Wellental"; norw. d
110 None Brugmann IF. 37, 155 will auch lat. acquus und gr. alrcog, ahtvg, ahpa aus idg. 
120 None ) 112 ek-{?), eko mit gramm. Wechsel anord. eim-yrja, ags. cem-yrie (engl. ember
130 None 122 epi, opi, pi Froehde BB. 21, 330; Hirt IF. 37, 228, wonach wohl urgr. >)- (n
```


## [2026-09-06T15:25:02.523Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (103,104):\n    print('==LEAF',n)\n    print(' '.join(t[n].split())[:1800]); print()\nEOF"
}
```


### [2026-09-06T15:25:05.364Z] TOOL RESULT

```
==LEAF 103
E. e, o adnominale und adverbale Partikel, etwa „nahe bei, dieht bei, zu- sammen mit“, auBerhalb des Arisehen und teilweise auch schon in diesem in der Bed. verblassend, im Germ, mit nicht mehr verfolgbarer Bed.-Entw. zum Sinne „unter, nach, hinterher, re-, zuriicb, wieder, weg“ gelangt. Ygl. bes. Schulze Qu. ep. 498 ff., Kretschmer KZ. 36, 268 (beide uber gr. d-, das sie aber noch aus *so- herleiten), Brugmann Album Kern 29ff., IF. 15, 103, KYG. 464, IF. 19,379 Anm.; 21,8; Grdr.II 2 2, 816 ff., IF. 28, 29 1 ff. 29, 231 ff.; 35, 95f., BSGW. 1913, 159, Bechtel ; Lexil. 152. Verwandt mit dem Pron.-St. e-, o-, entweder als dessen Ausgangspunkt oder, was bes. fur die langvokalischen e, o naheliegt, als eine Instrumentalbildung davon. Ai. a, av. ap. a „an, hinzu“ z. B. a-gam- „herankommen“, als Post- position mit Akk. „zu — hin“, mit Loc. „auf, in, zu — hin“, mit Abl. „von — weg“ (diese Begriffe des Zieles und des Ausgangspunktes „waren nicht durch den Sinn des Adverbs an sich, sondern durch den Kasussinn des Substantivs erzeugt“, was schon ein Yerblassen der eigentlichen Bed. der Partikel erweist; Zusammenhang zwischen der Yerbindung mit dem Abl. und der germ. Bed. „nach, zuriick“, bes. der von ahd. amaht utcilo nimmt , freilich Bechtel aaO. an); a vielleicht verbaut in den Dativen wie ai. asuray-a (vgl. auch av. ahuraui). Mit ai. a-da „empfangen“, a-da- „emp- fangend; in Besitz bekommend“ vgl. ai. dayadd- m. „Erbenff>fanger“ ( da yd „Antesl. Erbteil"), gr. yygcoazyg „wer ledig gewordenen Besitz (ro xygov) zu eigener Nutzung oder zur Yerwaltung bekommen hat (*-co-dza, vgl. ai. Ptc. a-tha-), (*hcro- — yfjQO--\-e-d „empfangend“). In adj. lat. litres „Erbe“ Zs. hat ar. a den Begriff der Annaherung, z. B. ai. a-nTln- „schwarzlich“ (ebensowohl gr. d>-%Qog „blaB, gelblich“, wohl 

==LEAF 104
; ; gr. e- wohl in IDiloj neben (H).o > gr. co in yyowaxi); (s. o.; wegen der Zusammenfiigung ist ursprunglich o hier freilich nicht ganz zweifelsfrei, trotz des e von litres, cbygog (s. o.), vielleicht in ojgvouat (docb s. u. reu „brullen“), sebr fraglicb in tbxeavog (s. u. kei- „liegen“ ; gr. i] wohl in y-ftaiog (s. o.; f/gefia „ruhig“ kann aber metr. Dehnung fur sein, Boisacq 329 Anm. 1 vielleicht in ifideog (s. Bechtel aaO.; gegen Prellwitz IvZ. 47, 299 f. nicht mit >)- aus urgr. a-, wie auch seine andern Beispiele ynedavog und vneoycpavoz ausscheiden). Ein italischer, infolge der Znsammensetzung erhaltener Rest scheint lat. tttor usw., s. u. ei- „gehn“; aber omitto oportet enthalten lat. ob (s. Vf. oitor, LEWb. 2 unter o- und auch fiir idoneus ist kein *id-r> „dazu“ als Grund- , lage anzuerkennen. Fiir < ist c-briiis tetymologisch dunkel), kein sichererer und edfirus, emollis kein Beleg gegen Niedermann Mel. Meillet 98f.). i Ahd. fimuht „deliquium, Ohnmacht“, uteilo „expers“, ags. in lewa-de „un- bekleidet“ is. o. ahd. am (id, nomad „Nachmahd“, dualist, nowahst „incremen- ) ; tum“, „Hinterkopf“, ags. ogengel „der (zuriickgehende) Querriegel“ (Belege s. hei Grimm Gr. II 695 ff., 774 des Neudrucks; J. Schmidt KZ. 26, 42, Leh- mann Praef. uz 138 ff., Fick III 4 23, 28, Bechtel aaO.i, oleccan „schmeieheln“ aus *o-lakjanl 3 angehangt im Ace. sg. der pron. Dekl., z. B. got. hano-h, harjntU-h, pana usw. Im Slav. *r oder *r> farblos in einigen Zs. wie skr.-ksl. ja-slcuds nehen ksl. skajlz „hiiBlich“ Berneker 441; Slav, jazda „das Fahren, Reiten“ (s. ist keine Zs. von V mit scd- „sitzen“, s. d.). Ob das nehen der Praep. ob, obz stehende o unser idg. 6 war, ist nicht sicher. c hinter dem Loc. und mit diesem verwachsen im Typus abg. kamen-e und lit. rahkoj-e faber lett. e-dze
```


## [2026-09-06T15:25:13.230Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (105,106,107,108):\n    s=' '.join(t[n].split())\n    print('==LEAF',n, s[:900]); print()\nEOF"
}
```


### [2026-09-06T15:25:14.879Z] TOOL RESULT

```
==LEAF 105 ) e-, i-, t-, a 97 hypr. iv „eum, eam“ (scheint auch in plv, vtv verbaut, (wenn nicht l v) s. Brugmann BSGW. 60, 74) lesb. thess. horn, la „una“ (urspriinglich ; „gerade die, nnr die"), hom. lyg, Ifj, darnach auch m. hom. to) (in dortgn. noch im urspriinglichen anaphorisclien Sinne; Lit. bei Boisacq 231 f., 378;. alb. e „eum, earn", i „ei“ (d. p.), i „eos, eas“, u „eis“. lat. is, auch Is, inschr. eis, eis-dem entweder mit -s id (n. sg. m. alt , ausgestattetes idg. *ei — ai. ay-am wie Sommer Gl. 5, 258 Hdb. 2 417 auch , fur umbr. er-e und bestimmter fur ir. lie „er" eine solche Gdf. *ei-s er- wagt, oder Umbildung von is nach eiins, e/i'fi), acc. altlat. im und cm, gedoppelt emem „eundem“ ( vie turrem fiir turrim, s. Lindsay-Nohl 503, Skutsch Gl. I, 306 ff., Sommer Gl. 5, 253 f.; unterstiitzt durch die eo-, ed- Kasus; fiir einen idg. Acc. *e-m fehlen Anhaltspunkte) Adv. cm „tum“ = und *im 

==LEAF 106 98 e-, i-. I-, a m. f. n. = mkymr. ivy huynt-uy wohl wenigstens zum Teil aus idg. *ei ( (Naheres bei Thurneysen und Pedersen), acc. sg. bret. en „ihn, es“ (infigiert), c. e (ebenso \ ir. -an- (ebenso), -i (suffigiert hinter Yerben; hinter Praep. teils ebenso, z. B. airi, teils nur mehr als Mouillierung nach- wirkend, z. B. foir), gen. sg. *esio, f. esias „eius“ in air. ai, tie (a aus e in unbetonter Stellung), proklit. a, alter z. T. noch e, ce, cymr. *cid- nach dem Yorbild der konjugierten Praepositionen zu me. eidaw, f. eidi differen- ziert, womit identiscli air. a „sein“ (len.) und „ibr“ (geminierend), cymr. corn, y, bret. e; usw., s. Brugmann, Thurneysen, Pedersen aaO. Got. is „er“, acc. in-a, neutr. it-a (s. o.) „es“ (dazu neugebildete Pluralformen vom St. i- got. eis, acc. ins, dat. ini, ahd. as. im), ahd. ir (Isid.),in-an, in, %, as. in-a, it, woneben mit (urspriinglichem? s. o.) 

==LEAF 107 ; ) e-, i-, 1-, a 99 Zu e- auch die Komparativbildung av. atara- „dieser, der von beiden“, aksl. efen, jeten „irgendwer“, pi. jderi(ji) „einige“, nsorb. ivotery ds., alb. jatere (G. Meyer Alb. Wb. Jokl IP. 36, 115) „anderer“, umbr. etro- 162, „anderer“, lat. in ceterus „der andere oder ubrige“ (s. Yf. LEWb. 2 s. v.). *e (instr.) ai. a hervorhebend hinter Adv. und Nomina : (s. Brugmann II 2 2, 327, 816); gr. y hervorhebend und fragend „wirklich“ (auch in ij-rot, msi-y i] hom. ye aus *>;-££, ij-pev , — »}-<?£, ij-dy), womit identisch dor. usw. rj ahd. -« in ihha „ich (gerade)“, nein-n „nein“ u. a.; lat. wohl in e- ,.e!“ ; castor u. dgl. (auch equideml s. Yf. LEWb. s. v.). 2 *ed (n. a sg. n.) iiber lat. ecce, : med s. o. av. at zur Hervorhebung des ; vorhergehenden Wortes (wie it_, s. u. Bartholomae Altiran. ; r b. 67); wohl W auch in aksl. jcd-im „einer“ als „*gerade, nur einer“, so daB *e

==LEAF 108 too e-, i-. I-, a lat. iterum „zum andern, zum zweiten Male“ (Fick III 4 27, Falk-Torp , 458 u. ide sucht eine Entsprechung auch in got. idreiga „Reue“, anord. idrask „bereuen“, idur-mmttr „VersmaB mit wiederkehrenden Reimsilben“, s. u. *ati, *eti, kaum mit Recht); ferner in ai. i-va „wie“ (vgl. oben fj-fi „wie“); in gr. l-de „und“ (vgl. *i-dha : ai. i-lici, prakr. idha, av. ida „hier“, gr. Idayevgg „(*hier geboren“, daher :) eingeboren, rechtmaBig geboren“ (l&aiysvgg wollen Fick und Bechtel Lexil. 172 als davon verschiedenes Wort fassen, doch nur mit Hilfe von Textanderungen; Brugmann BPhW. 1919, 136 deutet auch emxaQQo&og von zur Hilfe herbeieilenden Gottern als ^eji-tda-ggodog „nach hierher, aus dem Jenseits auf diese Erde niedSreilend)“, lat. ill „da, dort“ (die Lautentwicklung dh zu f, b nach ubl; im Auslaut nach den Locativen der o-St. gerichtet), umbr. ife „ibi, eo“, ifont „ibidem
```


## [2026-09-06T15:25:30.332Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'zur\\s+Hervorhebung', t):\n    leaf=t[:m.start()].count('\\f')\n    print('leaf',leaf,'|',' '.join(t[max(0,m.start()-400):m.start()+300].split()))\n    print()\nEOF"
}
```


### [2026-09-06T15:25:32.442Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:25:35.185Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in range(292,300):\n    s=' '.join(leaves[n].split())\n    m=re.search(r'\\b(28[0-9])\\b',s)\n    print('==',n,'|', s[:100],'...')\nEOF"
}
```


### [2026-09-06T15:25:36.990Z] TOOL RESULT

```
== 292 | guhno- (zu ai. ä-hands- jSchwellend, üppig' s. guhen- ,schwellen'); gr. 6- wohl in d-yteXlw ,treibe  ...
== 293 | nn Dem. 32 ff., BSGW. 60, 41 ff., Grundr. IP 2, 324 ff., Pedersen Pron. dem. 311 ff. A. Kasuell verw ...
== 294 | rde und eam usw. nach sich zog; tarn bei Varro 1. 1. 5, 166 und 8, 44 wohl Schreibfehler für eam. —  ...
== 295 | av. ?/ö, gr. b'g, rj, d ,welcher', phryg. log (vi) ,wer immer', slav. *ia- in i-ze, L ja-ze usw., ha ...
== 296 | ,wenn'; aksl. i ,und, auch' (vgl. ti ,und' vom St. *to-; von Brückner KZ. 46, 203 dagegen = lit. tei ...
== 297 | ), aksl. e-i ,ja, wahrlich' (? Berneker 296). Auch im 1. Gliede von ai. i-drg- ,so aussehend, so gea ...
== 298 | tätspronomina so-in , derselbe hier', do-in , derselbe da', no-in .derselbe dort' (,gerade der. ein  ...
== 299 | Lauten nach teil- weise Nachfolger von idg. obhi (s. unter epi); ^ot. bi, ahd. usw. bi, bi ,auf — hi ...
```


## [2026-09-06T15:25:40.518Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nleaves=open('POK_01.txt',encoding='utf-8',errors='replace').read().split('\\f')\ns=' '.join(leaves[296].split())\ni=s.find('Hervorheb')\nprint(s[:60])\nprint('...')\nprint(s[max(0,i-900):i+600] if i>=0 else 'NOT FOUND; searching atara')\nj=s.find('atara')\nprint('---atara---')\nprint(s[max(0,j-500):j+700] if j>=0 else 'no atara')\nEOF"
}
```


### [2026-09-06T15:25:42.571Z] TOOL RESULT

```
,wenn'; aksl. i ,und, auch' (vgl. ti ,und' vom St. *to-; von
...
NOT FOUND; searching atara
---atara---
no atara
```


## [2026-09-06T15:25:45.801Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nleaves=open('POK_01.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (294,295,296):\n    s=' '.join(leaves[n].split())\n    for pat in ['atara','ceterus','Hervorh','jeter','283','284','285']:\n        j=s.find(pat)\n        if j>=0:\n            print(n,pat,'::',s[max(0,j-350):j+450])\n            print()\nEOF"
}
```


### [2026-09-06T15:25:47.939Z] TOOL RESULT

```
294 283 :: ts), vgl. umbr. estu ,istumj ista'; air. e [he) ,er^ (wohl *ei-s), s. oben; ed (Jied) ,es^ (aus *ic?-ä = got. ita, womit formell identisch ai. idä ,jetzt'; aber lit. tadä ,dann' erfordert wegen ostlit. tadii einen Auslaut auf Nasal); Nom. PI. e (he) m. f. n. = • mkymr. wy (hwynt-wy) wohl wenigstens zum Teil aus idg. *ei (Näheres bei Thurneysen Gr. 283), Akk. Sg. bret. en ,ihn, es' (infigiert), cymr. e (ebenso), ir. -a n- (ebenso), -i (suffigiert hinter Verben; hinter Präp. teils ebenso, z. B. airi aus *ari-en ,auf ihn', teils nur mehr als Mouillierung nach- wirkend, z. B. foir aus *uor-en), Gen.* Sg. *esio, f. *esiäs ,eius', proklit. a, älter z. T. noch e, os; cymr. *eid- nach dem Vorbild der konjugierten Präpo- sitionen zu mcymr. eidatv, f. eidi differenziert, womit identisch air. a ,sein

294 285 ::  aus *uor-en), Gen.* Sg. *esio, f. *esiäs ,eius', proklit. a, älter z. T. noch e, os; cymr. *eid- nach dem Vorbild der konjugierten Präpo- sitionen zu mcymr. eidatv, f. eidi differenziert, womit identisch air. a ,sein' (len.) und ,ihr' (geminierend), cymr. com. y, bret. e, usw.; über air. be- tontes äi, ae ,eius' und Dat. PI. -ib s. Thurneysen Gr. 285; got. is ,er', Akk. in-a, neutr. it-a (s. o.) ,es' (dazu neugebildete Plural- formen: got. eis aus *ei-eSj Akk. ins, Dat. im, ahd. as. im), ahd. er, ir, Akk. 283 in-an, in; n. iz-, as. in-a, n. it'^ anord. Relativpartikel es, er, run. eR- vom St. e-: Gen. Sg. got. m. w, f. i^o», alid. m. n. es(is), L ira({ru), as. es(is)^ eraijra)] Gen. PI. g'ot. ize, 22;o, as. ahd. iro] Dat. Sg. f. got. izai, ahd. (mit anderer Endang) iru-^ m. n. got. imma, 

295 ceterus ::  bulg. e-to ,da' (usw., s. Berneker 259f.); 284 unsicherer got. i-haif i-ba Fragepartikel, ahd. ibu, ola, as. anord. ef q^c und ,wenn^, ^S^- 9^/^ engl, if ds. ; über *eno- in gr. evt] usw. siehe besonderes Stichwort. Zu e- auch die Komparativbildung av. atära- , dieser, der von beideu' ds., alb. jdt{e)re , anderer', umbr. etro- , anderer^, lat. in ceterus ,der andern oder übrige', aksl. eterh, jetei-b ,irgendwer', PL jeteri(ji) ,einige', nsorl> lüötery. ed (Nom. Akk. Sg. n.): über lat. ecce, med s. oben; av. at zur Hervor- hebung des vorhergehenden Wortes (wie ü, s. unten ; Bartholomae Altiran Wb. 67); wohl auch in aksl. jed-im, -tm , einer' als ,*gerade, nur einer*» ob auch ksl. jede, kyjb ,quidam' aus gedoppeltem *ed-ed oder nach id^^ im Ausgang gerichtetem *ed? (Berneker 261, bestritten

295 jeter :: i-ba Fragepartikel, ahd. ibu, ola, as. anord. ef q^c und ,wenn^, ^S^- 9^/^ engl, if ds. ; über *eno- in gr. evt] usw. siehe besonderes Stichwort. Zu e- auch die Komparativbildung av. atära- , dieser, der von beideu' ds., alb. jdt{e)re , anderer', umbr. etro- , anderer^, lat. in ceterus ,der andern oder übrige', aksl. eterh, jetei-b ,irgendwer', PL jeteri(ji) ,einige', nsorl> lüötery. ed (Nom. Akk. Sg. n.): über lat. ecce, med s. oben; av. at zur Hervor- hebung des vorhergehenden Wortes (wie ü, s. unten ; Bartholomae Altiran Wb. 67); wohl auch in aksl. jed-im, -tm , einer' als ,*gerade, nur einer*» ob auch ksl. jede, kyjb ,quidam' aus gedoppeltem *ed-ed oder nach id^^ im Ausgang gerichtetem *ed? (Berneker 261, bestritten von Brückner KZ. 45, 302, vgl. Meillet Slave comm.« 444.) * ed und öd 

295 284 :: , ja'; arm. e-t'e (neben t'e) ,'daß, wenn'; gr. i-yd-eg, i-ytsl, e-y.eXiog (nehen v-slvog) ; osk. e-tantOy umbr. e-tantu ,tanta', osk. päl. e-co ,hic', osk. exo- (*e-ke-so) ,hic'; aksl. (j)e-se ,ecce' (neben se ds.), aruss. ose, russ. e-to ,da, dahier', e-tot ,der hier, dieser' (neben tot ,jener') ; serb. bulg. e-to ,da' (usw., s. Berneker 259f.); 284 unsicherer got. i-haif i-ba Fragepartikel, ahd. ibu, ola, as. anord. ef q^c und ,wenn^, ^S^- 9^/^ engl, if ds. ; über *eno- in gr. evt] usw. siehe besonderes Stichwort. Zu e- auch die Komparativbildung av. atära- , dieser, der von beideu' ds., alb. jdt{e)re , anderer', umbr. etro- , anderer^, lat. in ceterus ,der andern oder übrige', aksl. eterh, jetei-b ,irgendwer', PL jeteri(ji) ,einige', nsorl> lüötery. ed (Nom. Akk. Sg. n.): über lat. ecc

296 285 :: ig geboren' (über id^aiysvyjg s. Schwyzer Gr. Gr. I 448); lat. ibl ,da, dort' (die Lautentwicklung dh zu f, b nach ubl; im Auslaut nach den Lokativen der o-St. gerichtet), umbr. ife ,ibi, eö', ifont , ibidem' (die ar. und ital. Formen könnten an sich auch -dhe enthalten, vgl. ai. ku-ha = aksl. kz-de ,wo', sb-de ,hier' und Schwyzer Gr. Gr. I 627*); 285 nicymr. yd, y ncymr. ydd Verbalpartikel, com. yz, yth-, bret. ez-? (s. Pedersen KG. II 234, Lewis-Pedersen 243, Thurneysen Gr. 324 f.); dazu auch air. infigiertes -id- aus *id(h)e oder Hd{h)i. i'tih)''. ai. itthä, itthäd ,bier, dort', av. ipU ,so', ai. itthdm ,so' und jjiit -t- {-t9 oder -<i?) ai. iti ,so'; lat. ita ,so', item , ebenso, ebenfalls', umbr. itek ,itaS mcymr. Präverb yt-, ncymr. yd-, z. B. in 2/^ yd-wyf ,ich bin'; lit. dial. it ,
```


## [2026-09-06T15:26:06.618Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-06T15:26:06.671Z] TOOL RESULT

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


## [2026-09-06T15:26:12.128Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-202.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:1500])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2000])\n\""
}
```


### [2026-09-06T15:26:14.086Z] TOOL RESULT

```
{"pdf_page": 202, "book_page": 172, "verified_by": "claude-opus-5", "verified_on": "2026-09-05"}
{
 "entry": 0,
 "root": "Gwa, Gwâ, Gwen 2",
 "verdict": "confirmed",
 "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
 "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
 "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده 
{
 "id": 1,
 "lang": "Avestan / Old Persian",
 "words": "gam : to come, step; jam, jantu : to go",
 "verdict": "confirmed",
 "derivation": "Indo-Iranian inherits PIE *gʷem- as the root gam- (Skt. gam-, Av. gam-, OP gam-). In Avestan the root appears in two guises that Nourai lists side by side: (a) gam- proper, in the perfect and in nominal derivatives (gāman-, gata-), and (b) jam-, the regular Avestan outcome of the full-grade *gʷem- (PIE labiovelar *gʷ- > Indo-Iranian *ǰ before front vowel of the thematic/subjunctive stems: *gʷem-e-ti > Av. jamaiti 'goes'), beside the inchoative present jasaiti < *gʷm̥-sk̑e-ti. jantu- is the tu-stem *gʷem-tu- 'a going, coming' (= Skt. gántu-, Lat. adventus), which Pokorny prints on the same page. Old Persian has the root only in compounds (ā-gam-, ham-gam-, parā-gam-), and there too the reflexes with j- (ājamiyā 'may he come') alternate with the g- of the participles (paragmatā, hangmatā). Nourai's glosses 'to come, step' / 'to go' are correct.",
 "derivation_fa": "ریشهٔ هندواروپایی *gʷem- در هندوایرانی به‌صورت gam- بازمانده است (سنسکریت gam-، اوستایی gam-، پارسی باستان gam-). در اوستایی دو گونه در کنار هم دیده می‌شود که نورایی هر دو را آورده است: نخست gam- که در ستاک‌های اسمی و کامل می‌ماند (gāman-، gata-)، و دوم jam- که پیامد آوایی قانونمند *gʷ- در ایرانی است (واک‌گونهٔ لبی‌کامی هندواروپایی پیش از واکهٔ پیشین به ǰ بدل می‌شود: *gʷem-e-ti > اوستایی jamaiti «می‌رود»)؛ ستاک حال آغازی نیز jasaiti < *gʷm̥-sk̑e-ti است. jantu- همان ستاک tu-دار *gʷem-tu- «رفت، آمد» است (هم‌ریشه با gántu- سنسکریت و adventus لاتین) که پوکورنی در همان صفحهٔ ۴۶۵ آورده. در پارسی باستان این ریشه تنها با پیشوند به‌کار رفته (ā-gam-، ham-gam-، parā-gam-). ادعای نورایی در این گره درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-",
  "https://en.wiktionary.org/wiki/آمدن"
 ],
 "ref_check": [
  {
   "ref": "POK:463",
   "status": "supports",
   "note": "POK_02.txt p.464-465 (the continuation of the entry that begins
```


## [2026-09-06T15:26:21.475Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/if",
 "prompt": "Etymology of \"if\": Old English gif, Proto-Germanic reconstruction, and whether it is connected to a pronominal stem or to a noun meaning \"doubt\"."
}
```


## [2026-09-06T15:26:22.456Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/identity",
 "prompt": "Etymology of \"identity\": Latin identitas, idem, and the pronominal root is/id. Also mention \"item\" and \"iterate\" if present."
}
```


### [2026-09-06T15:26:27.837Z] TOOL RESULT

```
# Etymology of "If"

The word "if" has an interesting linguistic history. According to the Online Etymology Dictionary, it originates from Old English *gif*, where the initial *g* was pronounced similarly to Modern English *-y-*.

The term traces back to Proto-Germanic **\*ja-ba**, appearing in related forms across Germanic languages like Old Saxon *ef*, Old Norse *ef*, and German *ob*.

## Two Competing Theories

Scholars disagree on the word's ultimate origin:

1. **Pronominal theory**: Some etymologists, including Watkins, suggest it derives from a PIE pronominal stem *\*i-*.

2. **Doubt-based theory**: Klein and the OED propose an alternative explanation: "it probably originally from an oblique case of a noun meaning 'doubt'" — a theory supported by related forms like Old High German *iba* ("condition, stipulation, doubt") and Old Norse *if* ("doubt, hesitation").

The noun usage of "if" became established around the 1510s, while related words like "iffy" (meaning uncertain) emerged in American English around 1937.
```


### [2026-09-06T15:26:28.806Z] TOOL RESULT

```
# Etymology of "Identity"

The word "identity" traces back to c. 1600, derived from French *identité* and Medieval Latin *identitatem*, both meaning "sameness." 

The ultimate root is Latin *idem* (neuter), meaning "the same." This comes from *id* ("it, that one") combined with a demonstrative suffix *-dem*, with origins in the Proto-Indo-European pronominal stem *\*i-*.

An earlier English form, *idemptitie* (1560s), came directly from Medieval Latin *idemptitas*.

**Modern usage developments:**
- "Identity crisis" is recorded by 1954
- "Identity theft" appears by 1995
- "Identity politics" is attested from 1985, popularized by the Combahee River Collective Statement (1977)

The related verb *identify* emerged in the 1640s with the sense "regard as the same," evolving by 1769 to mean "determine the identity of" and by 1780 to include psychological associations with identity.
```


## [2026-09-06T15:26:36.328Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%AF%D8%B1' --note 'page 224, root I 2 Io E, node 2: Persian ایدر idar \"here\" < MP ēdar < ēd + -r, OP idā' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ceterus' --note 'page 224, nodes 9/12: Latin ceterus < Proto-Italic *ke-eteros, PIE *h1e-teros; et cetera' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/yes' --note 'page 224, node 6: English yes = OE gese, gea (< PGmc *ja- < pron. stem *i-) + si (*es-)' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/yet' --note 'page 224, node 6: English yet, OE giet, preform uncertain, possibly PIE pronominal *i-' 2>&1 | tail -3"
}
```


### [2026-09-06T15:26:39.673Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f6112cae84182aa9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c364664646fe64e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc1d5a8f83a29f46.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6181db1d30de2f3d.txt
```


## [2026-09-06T15:26:46.072Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/if' --note 'page 224, node 6: English if, OE gif, PGmc *ja-ba; Watkins pron. stem *i- vs Klein/OED noun \"doubt\"' 2>&1|tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/identity' --note 'page 224, node 8: identity/identify < L. idem < id + -dem, PIE pron. stem *i-' 2>&1|tail -2; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%A9y' --note 'page 224, root box: PIE pronominal stem *éy/*h1e (Pokorny 281)' 2>&1|tail -2; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A7%DB%8C%D8%AF%D9%88%D9%86/' --note 'page 224, node 2: Moin and Dehkhoda on ایدون [په.] اینچنین / اکنون' 2>&1|tail -2"
}
```


### [2026-09-06T15:26:50.447Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b7efb83526d0b251.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d4a27f2bac704e4d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/486e8a364c6027a8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/17850f37663bec45.txt
```


## [2026-09-06T15:26:54.320Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg224.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/224.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-06T15:26:54.397Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T15:27:07.789Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'\\nyea,',r'\\nyes,',r'\\nyet,',r'\\niterate,',r'\\nidentity,',r'\\nidem,',r'\\nita\\b']:\n    ms=list(re.finditer(pat,t))\n    print('##',pat,len(ms))\n    for m in ms[:1]:\n        print('  leaf',t[:m.start()].count('\\f'),':',' '.join(t[m.start():m.start()+650].split()))\nEOF\necho \"=== IEC etero ===\"; grep -o -n \".\\{60\\}etero.\\{200\\}\" IEC.txt | head -4"
}
```


### [2026-09-06T15:27:09.715Z] TOOL RESULT

```
## \nyea, 0
## \nyes, 0
## \nyet, 0
## \niterate, 0
## \nidentity, 0
## \nidem, 0
## \nita\b 0
=== IEC etero ===
14041: Pol. czy ‘whether, or’. (Cpd. w *-ne, *-n, cf. Lat. quin, cetero-quin, Olr. ceni, cin ‘though not’, etc.). Reduplicated in Av. CiCa, beside CisCit; Arm. Cik ‘there is not; Hitt. *kwitkwit beside kwitki, non-selective prn. ('anything'; kwitki fr. *quid-ghi); Alb. c
```


## [2026-09-06T15:27:14.382Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'yea,\\s+adv',r'yes,\\s+adv',r'yet,\\s+adv',r'iterate,\\s+intr',r'identity,\\s+n',r'\\biterum\\b']:\n    ms=list(re.finditer(pat,t))\n    print('##',pat,len(ms))\n    for m in ms[:1]:\n        print('  leaf',t[:m.start()].count('\\f'),':',' '.join(t[max(0,m.start()-20):m.start()+700].split()))\nEOF"
}
```


### [2026-09-06T15:27:17.634Z] TOOL RESULT

```
## yea,\s+adv 0
## yes,\s+adv 0
## yet,\s+adv 0
## iterate,\s+intr 1
  leaf 39 : . Cp. avocado, alliterate, intr. v., to use alliteration. — ML. al- Uterdtus, pp. of alliterdre, "to begin with the same letter’, fr. ad- and L. littera, ‘letter’. See letter and verbal suff -ate. Derivatives: alliteration (q.v.), alliterat-ive, adj., alliterat-ive-ly, adv. alliteration, n., repetition of the same letter in several words of a sentence. — ML. alliteratio, gen. -dnis, from alliteratus, pp. of alliterdre. See prec. word and -ion. Allium, n., a genus of herbs of the lily family ( hot .) — L. alium, allium, ‘garlic’, prob. cogn. with OI. dtuh, alukdm, ‘bulb’. Accordingly alium would lit. mean ‘the bulbous plant’. T
## identity,\s+n 1
  leaf 412 : identity and -fy. identity, n. — F. identite, fr. Late L. identitdtem, acc. of identitas, ‘identity’, lit. ‘sameness’, fr. L. idem, ‘the same’; see idem and -ity. Late L. identitas is prop, a loan translation of Gk. rau- totyjp, ‘identity’, which is formed with suff. -xvjp (= L. -tas), fr. tgc’jto, contraction of to auxo, ‘the same' (= L. idem). ideo-, combining form meaning ‘idea’. — F. ideo-, fr. Gk. ESea, ‘form, idea’. See idea, ideogram, n., symbol used in writing. — Com¬ pounded of ideo- and Gk. ypxpipia, ‘that which is written, a written character, letter'. See -gram, ideograph, n., an ideogram. — Compounded of ide
## \biterum\b 1
  leaf 443 : say again’, fr. iterum, ‘again’, which stands for i-terum and prop, is the neuter of *i-teros, com¬ parative formed from the pronominal base *i- whence also OI. i-tarah, ‘the other’. For other derivatives of <he I.-E. pronominal base *i- see idem, for the comparative suff. see -ther, for the ending of iterate see verbal suff. -ate. iteration, n. — - L. iterdtid, gen. onis, ‘repetition’, fr. iteratus, pp. of iterate, ‘to repeat’. See iterate and -ion. iterative, adj. — F. iteratif (fern, iterative), fr. Late L. iterdtivus, fr. L. iteratus, pp. of iterare, ‘to repeat’. See iterate and -ive. Derivatives: iterative-ly, adv., it
```


## [2026-09-06T15:27:31.505Z] TOOL CALL #74: Bash

```json
{
 "command": "grep -h -o '\"ref\": \"KLN:[0-9]*\", \"status\": \"[a-z_]*\", \"note\": \"[^\"]\\{0,220\\}' data/verification/page-1[0-9][0-9].json 2>/dev/null | head -8; echo ===; python3 - <<'EOF'\nimport glob,json\nfor f in sorted(glob.glob('data/verification/page-2*.json'))[:60]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            for rc in n.get('ref_check',[]) or []:\n                if rc.get('ref','').startswith('KLN'):\n                    print(f.split('/')[-1], rc['ref'], rc['status'], rc['note'][:200])\nEOF"
}
```


### [2026-09-06T15:27:33.080Z] TOOL RESULT

```
Exit code 1
"ref": "KLN:275", "status": "supports", "note": "Klein, Comprehensive Etymological Dictionary (KLN_1966.txt leaf 155, in the 'chemo-…chicanery' block; the scan's rough offset formula puts the leaf at printed ≈ 286, so Nourai's p.275 is a few pages out or from another p
"ref": "KLN:399", "status": "supports", "note": "Klein 1966, leaf 220 of KLN_1966.txt (leaf 221 carries the printed numerals 401–403, so leaf 220 = pp. 399–400), s.v. 'Dan': '…rel. to Heb. dīn, \
"ref": "KLN:399", "status": "supports", "note": "Klein leaf 220 s.v. Dan: 'Aram. dūn, dīn … Heb. and Aram. dīn, \
"ref": "KLN:399", "status": "supports", "note": "Klein leaf 220 s.v. Dan: 'Aram. midhīnāh, \
"ref": "KLN:399", "status": "partial", "note": "Klein leaf 220 s.v. Dan has every Hebrew form Nourai gives ('Heb. Dan, lit. \
"ref": "KLN:419", "status": "supports", "note": "Klein 1966, leaf 231 of KLN_1966.txt (the leaf carries the printed numerals 420, 421, so the entry begins on p. 419), s.v. Delilah: '…from the base of d-l-l, \
"ref": "KLN:419", "status": "contradicts", "note": "The cited page gives 'Arab. dalla, \
"ref": "KLN:419", "status": "supports", "note": "Klein leaf 231 s.v. Delilah: 'Heb. Dəlīlāh, lit. \
(eval):1: == not found
```


## [2026-09-06T15:27:40.715Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nleaves=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in list(range(293,300))+list(range(400,415)):\n    L=leaves[n]\n    nums=re.findall(r'(?<![\\d,.])\\b([3-9]\\d\\d)\\b(?![\\d])',L)\n    print(n, nums[:12], '|', ' '.join(L.split())[:50])\nEOF"
}
```


### [2026-09-06T15:27:43.441Z] TOOL RESULT

```
293 ['540'] | similated fr. *f£pfo<;), Gk. aprjv, Gortyn. Faprjv
294 ['541', '701'] | a). See -er, suff. denoting connectedness, and -y 
295 ['542', '543'] | eol.) — Tr. eiscir, ‘a ridge’. Eskimo, n. and adj.
296 ['544', '343'] | , whence also Gk. T^nveiv, ‘to cut’. For the first
297 [] | eternity, n. — ME. eternite, fr. F. eternite, fr. 
298 ['548', '549', '779', '848', '300', '300'] | See prec. word. Etta, fern. PN. — Orig. used only 
299 ['550', '551'] | in and cp. words there referred to. For the ending
400 ['743', '744', '745'] | — L. Horatius (see Horace); influenced in form by 
401 ['746'] | r, gen. horiri, ‘to urge, incite, encourage, exhor
402 ['747', '879', '748', '749'] | . Cp. the second element in dachshund, keeshond.Cp
403 [] | uge-ous-ness, n,, hug-y, adj. huggermugger, adv., 
404 ['750', '751'] | b-, ’to bend, curve', whence also OI. kumbhdh, ‘po
405 ['752', '753', '665', '666', '754', '755'] | Formed fr. husk with adj. suff. -y. Derivatives: h
406 ['815', '825', '756'] | drogen (chem.)\ 4) short for hydroid (zool.) — Gk.
407 ['757'] | (fr. L. -dsns). hydroxide, n., a compound containi
408 ['758', '759', '760'] | out hymns. See prec. word and -graphv. hymnology, 
409 ['715', '761', '762'] | ed by James Braid of Manchester (1795-1861) fr. hy
410 ['704'] | sub, of s.m. See hypo- and cp. hypso-. Cp. also th
411 ['764', '765', '801'] | e. -ic, adj. suff. meaning ‘pertaining to; of the 
412 ['500', '894', '766', '767', '671'] | d in imitation of Gk. -txa (neut. pi. of the adj. 
413 ['768', '769'] | — Gk. t8to7raff£<.a, ‘a disease having its own ori
414 ['770', '771'] | -ilitatem, acc. of -ilitas; formed from adjectives
```


## [2026-09-06T15:28:55.406Z] TOOL CALL #76: Bash

```json
{
 "command": "SP=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 - <<EOF\nfrom PIL import Image\nim=Image.open(\"$SP/pg224hi.png\"); w,h=im.size\nim.crop((int(0.20*w),int(0.465*h),int(0.42*w),int(0.525*h))).save(\"$SP/c224_n7.png\")   # Latin idem\nim.crop((int(0.22*w),int(0.575*h),int(0.50*w),int(0.635*h))).save(\"$SP/c224_n12.png\")  # Latin ce-terus\nEOF\necho ok"
}
```


### [2026-09-06T15:28:57.133Z] TOOL RESULT

```
ok
```


## [2026-09-06T15:29:00.377Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c224_n7.png"
}
```


### [2026-09-06T15:29:00.388Z] TOOL RESULT

```

```


## [2026-09-06T15:29:00.407Z] TOOL CALL #78: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c224_n12.png"
}
```


### [2026-09-06T15:29:00.418Z] TOOL RESULT

```

```


## [2026-09-06T15:29:23.851Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport glob,json\nfor f in sorted(glob.glob('data/verification/page-*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            if not (n.get('words') or '').strip():\n                print(f.split('/')[-1], n['id'], n.get('lang'), n.get('verdict'), '|', (n.get('derivation') or '')[:180])\nEOF"
}
```


### [2026-09-06T15:29:25.970Z] TOOL RESULT

```
<persisted-output>
Output too large (29.7KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bwebnatks.txt

Preview (first 2KB):
page-101.json 5 Arabic plausible | Pass-through node: Arabic zumurrud زُمُرُّد 'emerald' does go back to Greek smaragdos, but not directly: Wiktionary derives Arabic zumurrud from Persian zumurrud (< Middle Persian 
page-103.json 5 Latin confirmed | The empty pass-through box is Latin byssus, -ī f. 'fine linen, byssus', borrowed from Greek βύσσος with the ordinary Latin rendering of upsilon by y and of the Greek nominative -os
page-105.json 2 French plausible | An empty pass-through box, and a reasonable one: French soja (also soya) is a borrowing of the Dutch word, spread through botany — Linnaeus' binomial Dolichos soja / Glycine soja i
page-105.json 1 Mongolian disputed | An empty pass-through box asserting Mongol transmission of the Chinese word into Persian. The idea is superficially attractive — the Ilkhanid period is exactly when the Chinese loa
page-105.json 9 Aramaic confirmed | An empty pass-through box, and the crucial one for this branch: the Iranian word reached Arabic through Aramaic, not directly. The Aramaic form is שְׁרָגָא šərāgā, Classical Syriac
page-107.json 6 Greek confirmed | Pass-through node: the Greek box is printed empty in the book (only the header 'Greek  SKT:87'), so the extraction is faithful — no word was lost. The word Nourai means is Byzantin
page-112.json 6 French confirmed | A pass-through node with no word printed: it stands for the French forms that carried the Latin dic- family into Persian, i.e. dictée (feminine past participle of dicter, itself fr
page-112.json 10 French plausible | Another empty pass-through box, standing for French disque, the immediate source of Persian دیسک. Two corrections to the arrow as drawn. First, French disque did not come from Gree
page-113.json 4 French confirmed | Empty pass-through box: French is only the transmitting stage between the Latin words of #3 and the Persian loans of #5. The relevant French forms are docteur (Old French doctour, 
...
</persisted-output>
```


## [2026-09-06T15:29:35.867Z] TOOL CALL #80: Bash

```json
{
 "command": "head -20 /home/sfmqrb/git/rishe/data/verification/agent/charts/page-225.txt 2>/dev/null || echo \"no chart 225\""
}
```


### [2026-09-06T15:29:35.908Z] TOOL RESULT

```
=== PDF page 225 (book page 195) ===
--- entry 0 ---
ROOT [Indo-European] I 2, Io, E : pronominal stem  (refs POK:281)  PART 2
#1 (parent #0) [Indo-European] refs=POK:73,75,281,286 | Au 3, Auo, Oi-no : one, this one ; Uě, Uo : or
  #2 (parent #1) [Avestan / Old Persian] refs=POK:73,75,286; BQT:2417; KNT:164 | ava 2, aiva, aěva, aeva, aivaka : one ; aeva-data, aeva-dasa : eleven ☞Dekm ; aiva-čiy : nothing ☞Kwo ; va, vâ : or
    #3 (parent #2) [Pahlavi] refs=BQT; SNS:91; GPL:41 | ěvak, yak : one ; yâcdah : eleven ; hěč : nothing ; ayâb, ayâ, ayâo : or
      #4 (parent #3) [Persian] refs=BQT:2417,2446; SNS:86,91 | yak, yek «یک» : one ; yâzdah «یازده» : eleven ; hîč «هیچ» : nothing, no ; yâ «یا» : or
  #5 (parent #1) [Avestan / Old Persian] refs=POK:74 | uta, utâ, uiti : and
    #6 (parent #5) [Sogdian] refs=SOD:72 | `ty : and
    #7 (parent #5) [Pahlavi] refs=SNS:256 | ud : and
      #8 (parent #7) [Persian] refs=BQT:2242; SNS:256; TZF:20; MON:4921 | o, va «وُ ، وَ» : and | NOTE: The Arabic "va" pronunciation has influenced the Persian pronunciation
  #9 (parent #1) [Old Persian / Sanskrit] refs=POK:75,286; BQT:199; TZF:13; SOD:85,220 | aina, ěna, aita, aěta : this one, this ; ima, imam : this
    #10 (parent #9) [Sogdian] refs=SOD:85,220 | `yd : this ; mw : this
    #11 (parent #9) [Pahlavi] refs=MON:345,421 | ěn : this ; im : this
      #12 (parent #11) [Persian] refs=MON; TZF:13 | în «این» : this ; em «اِم (امروز، امشب، امسال)» : this
  #13 (parent #1) [Germanic] refs=AHD | ainaz, ainigaz : one
    #14 (parent #13) [English] refs=None | one, an, none, eleven, alone, any
  #15 (parent #1) [Latin] refs=AHD | ŭnus : one ; ne-ŭllus : not any, null ☞Ne 1
    #16 (parent #15) [English] refs=None | union, onion, ounce, inch, unique, unite, unit, universe ; null
--- entry 1 ---
```


## [2026-09-06T15:38:28.289Z] TOOL CALL #81: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk224.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_POK = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%A9y\"\nW_IDAR = \"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%AF%D8%B1\"\nW_CET = \"https://en.wiktionary.org/wiki/ceterus\"\nE_YES = \"https://www.etymonline.com/word/yes\"\nE_YET = \"https://www.etymonline.com/word/yet\"\nE_IF = \"https://www.etymonline.com/word/if\"\nE_ID = \"https://www.etymonline.com/word/identity\"\nABADIS = \"https://abadis.ir/fatofa/%D8%A7%DB%8C%D8%AF%D9%88%D9%86/\"\n\ndoc = {\n \"pdf_page\": 224,\n \"book_page\": 194,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 1,\n   \"root\": \"I 2, Io, E\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₁e- / *h₁ey- / *h₁i- (Pokorny 'e-3, ei-, i-, fem. ī-'), the anaphoric-demonstrative pronominal stem 'this, he/it', with the relative stem *i̯o- attached to it; Pokorny IEW 281-286, Watkins/AHD 'i-. Pronominal stem'.\",\n   \"note\": \"The root box is exactly right. Pokorny's entry 'e-3, ei-, i-, fem. ī- (*he-3): dieser usw. (Demonstrativstamm); einer' runs from p.281 to p.286 — Nourai's POK:281 is the first page of it — and Watkins' AHD appendix heads the same material 'i-. Pronominal stem ... [Pok. 3. e- 281.]'. Nourai's three-part name 'I 2, Io, E' renders the three ablaut/stem shapes Pokorny prints in his lemma (i-, the relative i̯o- which Pokorny explicitly attaches to i-, and e-); the language label 'Indo-European' and the gloss 'pronominal stem' are Watkins' own wording. Modern reconstructions differ only in notation (Sihler *ís, Ringe *éy, Beekes *h₁e). The page as a whole is sound Indo-European handbook material; the two things that are wrong on it are both single ghost-forms produced by misreading a source: 'at-zur' in node #10 (a piece of Pokorny's German sentence 'av. aṭ zur Hervorhebung ...') and 'iden' in node #7 (a misprint for the neuter idem).\",\n   \"note_fa\": \"جعبهٔ ریشه درست است. مدخل پوکورنی با عنوان «e-3, ei-, i-» یعنی ستاک ضمیری/اشاری هندواروپایی آغازین دقیقاً از صفحهٔ ۲۸۱ آغاز می‌شود و تا ۲۸۶ ادامه دارد؛ واتکینز در پیوست ریشه‌های AHD همین ماده را «i-. Pronominal stem» نامیده و به پوکورنی ۲۸۱ ارجاع داده است. سه نامی که نورایی آورده (I 2، Io، E) همان سه گونهٔ ستاک است: i-، ستاک موصولی *i̯o- که پوکورنی آن را وابستهٔ همین ریشه می‌داند، و e-. بنابراین ادعای نورایی دربارهٔ خود ریشه درست است؛ تنها دو صورت در این صفحه ساختگی است: «at-zur» در گرهٔ ۱۰ و «iden» در گرهٔ ۷.\",\n   \"sources\": [W_POK],\n   \"ref_check\": [\n    {\"ref\": \"POK:281\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 293 begins the entry (German original) 'e-3, ei-, i-, fem. ī- ... dieser usw. (Demonstrativstamm); einer', and the entry's 'Page(s): 281-286' block in POK_full.txt confirms the span; the reference line is 'WP. I 95 ff., WH. I 368 f., 399 f., 409, 671, 720 ff., 869'. Nourai's p.281 is the opening page, exactly as cited.\"},\n    {\"ref\": \"KNT:203\", \"status\": \"partial\",\n     \"note\": \"Kent's Lexicon p.203 (KNT.txt leaf 227-228, the leaf carrying the running head 'LEXICON 203' and ending just before the '204' numeral) closes with 'ya- rel. pron. “who, which”, generalized by encl. -ciy: Av. Skt. ya-, Gk. hós, pIE *i̯o-'. That supports the 'Io' half of the root name, but the Old Persian demonstrative entries Nourai also needs ('idā adv. “here” ... formed on pronominal root seen in OP iyam, Skt. ayám ... Lt. is ea id' and 'ima- demonst. adj. and pron. “this”') stand on pp.173-174 (leaves 196-197), not on p.203.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 97-100 (WLD_Bd1_pages.txt leaves 105-108, printed pp. 97-100)\", \"stance\": \"supports\",\n     \"note\": \"The Walde-Pokorny entry that Pokorny's 'WP. I 95 ff.' points to is headed 'e-, i-, ī-, ā' and gathers exactly the same material: Lat. is/eis-dem, Goth. is/it-a, av. atāra-, lat. ceterus, lat. iterum, *i-dha (ai. ihá, av. iδa 'hier').\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. 'i-' (AHD_watkins1985.txt line 559)\", \"stance\": \"supports\",\n     \"note\": \"'i-. Pronominal stem. ... 7. Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same ... 10. Suffixed variant form *e-tero- (see ko-). [Pok. 3. e- 281.]' — same root, same gloss, same Pokorny page.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ceterus\", \"stance\": \"supports\",\n     \"note\": \"'c'est le dérivé en *-tero-, *-tro- des thèmes du démonstratif i.-e. *e- et *i-' — Ernout-Meillet operates with the same two-stem demonstrative *e-/*i- that Nourai's box calls 'I 2, Io, E'.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/éy\", \"stance\": \"supports\",\n     \"note\": \"Modern reconstruction of the same stem ('*ís / *h₁e', stem alternants *i-, *ey-), with descendants Skt. íti, Av. uiti, Lat. ita, item, iste, ipse, PGmc *ja, Gk. ei; the page cites Pokorny vol. 1 p.281.\"}\n   ],\n   \"nodes\": []\n  }\n ]\n}\n\nN = doc[\"entries\"][0][\"nodes\"]\n\nN.append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"itha, itta, aěta-vant : here, there, so, thus, then\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two of the three forms are genuine Avestan and are drawn from exactly the pages Nourai cites. (a) iθa 'so, thus' is Pokorny's *i-t(h)- formation on p.285: 'ai. itthā, itthād „hier, dort“, av. iθa „so“, ai. ittham „so“ und mit -t- ai. iti „so“; lat. ita „so“, item „ebenso“' — i.e. the stem *i- plus the adverbial extensions -dh- and -t-. (b) aētauuaṇt- 'so much, so great' is the -vant- adjective of the demonstrative aēta- 'this' (*ei-to-, Pokorny 285 'ai. e-ṣa, e-tát, av. aēṣa-, aēta- „er selbst“'), attested e.g. Vd. 3.7 'aētauuat karštānam' ~ 'so viel vom Gesäten' (Bartholomae). (c) 'itta', however, is not an Avestan word: what stands beside iθa on Pokorny 285 is Old Indic itthā / ittham / iti and Latin ita, so Nourai has taken an Indic (or Latin) form into an Avestan box. The gloss 'here, there' likewise belongs strictly to the *i-dhe formation — Av. iδa, OInd. ihá 'here' — which is what Klein p.763 s.v. ibidem prints, not to iθa 'so'. The node is therefore right in substance (all these forms do continue the root box) but imprecise in labelling.\",\n \"derivation_fa\": \"دو صورت از سه صورت این گره اوستایی اصیل است: iθa «چنین، این‌گونه» که پوکورنی در صفحهٔ ۲۸۵ ذیل ساخت *i-t(h)- آورده است، و aētauuaṇt- «این‌قدر، چنین بسیار» که صفت پسونددار -vant- از ضمیر اشارهٔ aēta- «این» است (بارتولومه، ذیل aētauuant-). اما «itta» واژه‌ای اوستایی نیست؛ آنچه در همان صفحهٔ پوکورنی در کنار iθa آمده صورت‌های سنسکریت itthā / ittham / iti و لاتین ita است؛ نورایی صورتی هندی را در جعبهٔ اوستایی نشانده است. معنای «اینجا، آنجا» نیز به ساخت *i-dhe تعلق دارد (اوستایی iδa، سنسکریت ihá) که کلاین در صفحهٔ ۷۶۳ ذیل ibidem آورده، نه به iθa. در کل، ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_POK],\n \"ref_check\": [\n  {\"ref\": \"POK:281\", \"status\": \"supports\", \"note\": \"The opening page of the root entry, which Nourai repeats here as the general reference for the Avestan branch.\"},\n  {\"ref\": \"POK:285\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 296 (carrying the printed numeral 285): 'i-t(h)-: ai. itthā, itthād „hier, dort“, av. iθa „so“, ai. ittham „so“ und mit -t- ... ai. iti „so“; lat. ita „so“, item „ebenso, ebenfalls“'. Exactly Nourai's 'itha ... so, thus' — and it also shows that his 'itta' is the Old Indic, not an Avestan, form.\"},\n  {\"ref\": \"KLN:763\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 410 (= printed pp.762-763; leaf 409 carries 761/762 and leaf 411 carries 764/765) s.v. ibidem: '... cogn. with OI. i-há, Avestic iδa, “here”, Gk. ἰθαγενής ... All these words derive fr. I.-E. *i-dha, *i-dhe, from the pronominal base *i-; see idem'. Nourai's page number is exact.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. aētauuant- (BRT.txt line 3038)\", \"stance\": \"supports\",\n   \"note\": \"'... aetavat karstanam ... altavat °tanam „Getreide .. so viel vom gesäten, soviel vom ...“ Vd. 3.7; 15' — Avestan aētauuaṇt- 'so much, so great' is real and is the -vant- derivative of aēta-.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.173 (KNT.txt leaf 196)\", \"stance\": \"supports\",\n   \"note\": \"'idā adv. “here”: GAv. idā, LAv. iδa, Skt. ihá, Gk. adv. ending -θε, pIE *i-dhe ... formed on pronominal root seen in OP iyam, Skt. ayám ... Lt. is ea id' — confirms the 'here' sense in Old Iranian, and confirms that its Avestan shape is iδa, not iθa.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 100\", \"stance\": \"supports\",\n   \"note\": \"'*i-dha : ai. i-há, prakr. idha, av. iδa „hier“, gr. ἰθαγενής' — the same double formation (-dh- for 'here', -t(h)- for 'thus') that Nourai has merged into one box.\"}\n ]\n})\n\nN.append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"îdar «ایدر» : here ; îdŭn «ایدون» : now, such\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"ایدر īdar/ēdar 'here' and ایدون īdūn/ēdōn 'thus, so; now' are the classical Persian continuations of Middle Persian ēdar [LTME] 'here' and ēdōn [ʾytwn] 'thus, so' (MacKenzie 1971), which are built on the Middle Persian demonstrative ēd 'this' — itself from Old Iranian *aita- (OP aita-, Av. aēta-) — plus the local suffix -ar and the manner-suffix -ōn (< Old Iranian *-āuuana-, cf. Pahlavi ēwōn, čigōn). The Old Persian adverb idā 'here' (Av. iδa) of the same root family reinforced the form. Horn's Grundriss no. 137 (p.32) sets the whole cluster out under the demonstrative ī 'dieser': 'ī „dieser“ in īdar „hier“, īdrā, īderī (Nāṣ. Xosr.), erā „desshalb“, edūn, īdūn ... „so“, īm „jetzt“ ... ap. aita- „dieser“; aw. aē-m-, aē-tat̄; phlv. ē, ēčand, ētar, ētūn'. Nourai's gloss 'now, such' for īdūn is not his invention: Borhan-e Qateʿ (and Mo'in after it) gives precisely the two senses, 'اکنون ... و بکسر اول بمعنی اینچنین'. The chart's Ferdowsi verse ('دل و جانم ایدر بماند همی') is a normal Shahnameh attestation of ایدر 'here'.\",\n \"derivation_fa\": \"«ایدر» و «ایدون» دنبالهٔ فارسی دری ی فارسی میانهٔ ēdar «اینجا» و ēdōn «چنین» هستند (مکنزی، فرهنگ کوچک پهلوی: edar «here»، edon «thus, so») که هر دو بر پایهٔ ضمیر اشارهٔ پهلوی ēd «این» ساخته شده‌اند؛ ēd خود از ایرانی باستان *aita- (پارسی باستان aita-، اوستایی aēta-) می‌آید و پسوندهای ‌-ar (جای) و -ōn (گونگی، همانند چیگون و ایون) بدان پیوسته است. هرن در صفحهٔ ۳۲ و شمارهٔ ۱۳۷ دقیقاً همین زنجیره را می‌آورد: ī «این» > īdar، īdūn، با صورت‌های پهلوی ētar و ētūn و اصل اوستایی/پارسی باستان. معنای دوگانهٔ «اکنون» و «این‌چنین» برای ایدون همان است که برهان قاطع و فرهنگ معین می‌دهند. ادعای نورایی درست است.\",\n \"sources\": [W_IDAR, ABADIS],\n \"ref_check\": [\n  {\"ref\": \"HRN:32\", \"status\": \"supports\",\n   \"note\": \"Horn, Grundriss der neupersischen Etymologie, p.32 (HRN.txt \\\\f-leaf 54, headed '— 32 —'), entry no.137: 'ī „dieser“ in īdar „hier“, īdrā (unbelegt), īderī (Nāṣ. Xosr.), erā „desshalb“, edūn, īdūn (Kasan: etūn ...) „so“, īm „jetzt“, īme „jetzt“, ēšān „diese“ ... ap. aita- „dieser“; aw. aē-m-, aē-tat̄; phlv. ē, ēčand ..., ētar, ētūn'. This is Nourai's arrow verbatim, including the Avestan aēta- source.\"},\n  {\"ref\": \"BQT:193,197\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qateʿ vol. 1, in the ای‌- run (BQT_v1_pages.txt leaf 414, printed p.194 by the volume's leaf/page anchor, i.e. inside the pp.193-197 span Nourai cites): 'ایدون — بفتح اول، بروزن و بمعنی اکنون است که این زمان را الحال باشد — و بکسر اول بمعنی اینچنین و اینجا و این زمان ... و این ساعت بود' — which is Nourai's gloss 'now, such' word for word. The ایدر headword falls on the immediately preceding page but is illegible in this scan's OCR.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. edar / edon (PHD_mackenzie.txt lines 2190-2191)\", \"stance\": \"supports\",\n   \"note\": \"'edar [LTME < A ltnh | M ʾydr, N --] here.' and 'edon [ʾytwn | N idun] thus, so.' — the Middle Persian stage Nourai's arrow jumps over, and MacKenzie himself equates ēdōn with New Persian īdūn.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, index (NYB_vol2_glossary.txt lines 5848, 6545)\", \"stance\": \"supports\",\n   \"note\": \"The glossary index cross-refers 'ʾydr: ētar' and 'ēdar: ētar / ēdun: ētōn', i.e. Nyberg lemmatises the same pair ētar 'here' / ētōn 'thus'.\"},\n  {\"src\": \"MON\", \"where\": \"فرهنگ معین s.v. ایدون (via abadis.ir)\", \"stance\": \"supports\",\n   \"note\": \"'(اِ) [په.] (ق.) ۱ - این چنین، این گونه. ۲ - اکنون، الحال.' — Mo'in tags the word [په.] = Pahlavi and gives both senses; Dehkhoda's entry adds the Pahlavi ētōn and an Old Iranian antecedent.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"ایدر (Persian)\", \"stance\": \"partial\",\n   \"note\": \"'From Middle Persian ʾydr (ēdar), from ʾyd (ēd, “this”) + -r, from Old Persian idā (“here”), Proto-Indo-Iranian *Hidʰá'; senses 'here, now, behold'. Same root family as Nourai's box, but it makes the immediate preform the *i-dhə adverb (Av. iδa) rather than aēta-, where Horn prefers ēd < aita-.\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien, grep 'īdar/idar'\", \"stance\": \"silent\", \"note\": \"No entry for ایدر or ایدون in Hübschmann's Persische Studien (nothing returned by the grep).\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha (Persian headword index and Latin index)\", \"stance\": \"silent\", \"note\": \"Neither ایدر/ایدون nor 'idar/idun' occurs; Aryanpur does not treat these archaic adverbs.\"}\n ]\n})\n\nN.append({\n \"id\": 3,\n \"lang\": \"Avestan\",\n \"words\": \"im, iyam, imam : she, he, then ; it : that ; yô : who, which, what ; ya-târa : which one (of two)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All four items belong to the root box, but the labels and glosses are loose. im is the enclitic accusative 'him/it' of the anaphoric stem i-; iiam / iyam is the feminine nominative 'this (one)' (OP iyam, Skt. iyám); imąm / imam is the accusative of the demonstrative ima- 'this', a stem which Kent shows was itself abstracted from the accusative *i-m + enclitic -am. So the gloss 'she, he' should be 'this (one)', and 'then' does not belong here at all — that sense sits with the particle aṯ̄ / aδa. iṯ̄ is the neuter 'it, that' (= Goth. ita, Lat. id), correctly glossed. yō 'who, which' and yatāra- 'which of two' belong to the relative stem *i̯o-, which Pokorny explicitly derives from this root ('To i- is joined the relative stem *i̯o-'), yatāra- being the same *-tero- contrastive suffix that produces atara- in node #10; both are genuine Avestan (Bartholomae cites yatāra- vā dim paurva frāyazāiti 'whichever of the two worships him first', Yt 10.9). Nourai's arrow — pronominal stem > these Avestan pronouns — is standard doctrine.\",\n \"derivation_fa\": \"هر چهار صورت به همین ریشه بازمی‌گردند ولی برچسب معنایی آنها دقیق نیست. im صورت پیوستهٔ رایی از ستاک i- است؛ iyam نهادی مؤنث «این» (پارسی باستان iyam، سنسکریت iyám) و imąm رایی ضمیر اشارهٔ ima- «این» است؛ پس معنای درست «این» است نه «او/او (مؤنث)»، و معنای «آنگاه» از آنِ حرف aṯ̄/aδa است. iṯ̄ همان خنثای «آن، آن را» است (هم‌ریشه با گوتی ita و لاتین id). yō و yatāra- به ستاک موصولی *i̯o- تعلق دارند که پوکورنی صریحاً آن را وابستهٔ همین ریشه می‌داند؛ yatāra- با همان پسوند تقابلی *-tero- ساخته شده که در atara- (گرهٔ ۱۰) دیده می‌شود و در اوستا از جمله در یشت ۱۰، بند ۹ آمده است. در مجموع ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_POK],\n \"ref_check\": [\n  {\"ref\": \"POK:283\", \"status\": \"supports\",\n   \"note\": \"POK_01.txt leaves 294-295 (carrying the printed numerals 283 and 284): the case-forms section gives 'ai. iyám = av. īm (d.i. iyəm), ap. iyam „sie“, Akk. Sg. m. ai. imám = ap. imam', and leaf 295 opens with 'av. yō, gr. ὅς, ἡ, ὅ „welcher“ ... komparativ ai. yatara-, av. yatara- „einer von beiden“'. Every form in Nourai's box is on this page-spread.\"},\n  {\"ref\": \"KNT:203\", \"status\": \"partial\",\n   \"note\": \"Kent's p.203 (KNT.txt leaf 227-228) ends with 'ya- rel. pron. “who, which” ...: Av. Skt. ya-, Gk. hós, pIE *i̯o-', which covers yō; but the im/iyam/imam material is in Kent's Lexicon at pp.173-174 ('idā adv. “here” ...' and 'ima- demonst. adj. and pron. “this”: Av. ima-, Skt. ima-; stem extracted from Ar. *im-am = acc. *i-m + encl. -am'), so half of the citation is misplaced.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. yatara- (BRT.txt lines 12778, 15728, 17573)\", \"stance\": \"supports\",\n   \"note\": \"'yatāra vā dim paurva frāyazāiti' Yt 10.9, 18 ('welcher von beiden ihn zuerst verehrt') — Avestan yatāra- 'which of the two' is well attested, exactly Nourai's gloss.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon pp.173-174 and p.203\", \"stance\": \"supports\",\n   \"note\": \"'ima- demonst. adj. and pron. “this”: Av. ima-, Skt. ima-' and 'ya- rel. pron. “who, which”: Av. Skt. ya-, Gk. hós, pIE *i̯o-'; Kent glosses ima- 'this', not 'she, he'.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 97-98\", \"stance\": \"supports\",\n   \"note\": \"The same case-forms are collected there ('lat. is ... got. is „er“, acc. in-a, neutr. it-a „es“'), i.e. Nourai's 'it : that' is the neuter of the anaphoric stem.\"}\n ]\n})\n\nN.append({\n \"id\": 4,\n \"lang\": None,\n \"words\": \"\",\n \"verdict\": \"unverified\",\n \"derivation\": \"A completely blank box on the printed page (page 224 of the PDF, book p.194): no language header, no reference, no word — only the empty rectangle, drawn to the right of the Avestan pronoun box #3. The extraction is faithful to the page. There is nothing to verify; the derivatives that would have stood here are given in PART 2 of the same root (book p.195 = PDF page 225, nodes #9-#12: Old Persian aina, ēna, aita, aēta / ima, imam > Pahlavi ēn, im > Persian این).\",\n \"derivation_fa\": \"این جعبه در صفحهٔ چاپی (ص ۱۹۴ کتاب) کاملاً خالی است: نه نام زبان، نه واژه، نه ارجاع. پس خوانش اسکن درست است و چیزی برای ارزیابی وجود ندارد. دنبالهٔ این شاخه در بخش دوم همین ریشه (ص ۱۹۵ کتاب) آمده است: ima/imam و aita/aēta > پهلوی ēn، im > فارسی «این».\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book.\"}],\n \"consulted\": [{\"src\": \"BOOK\", \"where\": \"printed page 194 (PDF 224), rendered at 400 dpi\", \"stance\": \"silent\", \"note\": \"The rectangle is printed empty; nothing was lost in extraction.\"}]\n})\n\nN.append({\n \"id\": 5,\n \"lang\": \"Germanic / Old English\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"A header-only pass-through box (language + 'AHD', no forms), standing for the Germanic stage between the PIE stem and the English words of node #6. What Watkins puts there is: Germanic *is-lik- > OE ilca 'same'; *jaino-/*jeno- > OE geon 'that'; *jend- > OE geond 'yonder'; the extended forms *iām, *iāi > Gmc *jā, *jai > OE gēa 'yea' and gēse 'yes'; OE gīet 'still'; OE gif 'if'. The Germanic reflex of the stem is regularly *j- before a front vowel (PIE *i̯- > Gmc *j-, later OE ġ- spelled g- and pronounced /j/), which is why the English descendants all begin in y- (or, in 'if', in a lost initial /j/).\",\n \"derivation_fa\": \"این جعبه تنها سربرگ دارد (زبان + ارجاع به AHD) و گذرگاهی است میان ریشهٔ هندواروپایی و واژه‌های انگلیسی گرهٔ ۶. واتکینز در همین جایگاه صورت‌های ژرمنی *is-lik- (> ilca)، *jaino- (> geon)، *jend- (> geond) و *jā/*jai (> gēa، gēse) را می‌آورد. دگرگونی آوایی کلیدی این است که *i̯- هندواروپایی در ژرمنی به *j- بدل می‌شود و در انگلیسی کهن با g نوشته و /j/ خوانده می‌شود؛ از همین روست که بازمانده‌های انگلیسی با y آغاز می‌شوند. ادعای نورایی درست است.\",\n \"sources\": [E_YES],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. 'i-': '1. Germanic *is-lik- ... in Old English ilca, same: ILK. 2. Germanic *jaino-, *jeno-, in Old English geon, that: YON. 3. Germanic *jend- in Old English geond ...: YOND. 4. Extended forms *iām, *iāi, in Germanic *jā, *jai, in Old English gēa ... and gēse, yes ...: YEA, YES. 5. Old English giet ... 6. Old English gif ...'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 284-286\", \"stance\": \"supports\",\n   \"note\": \"'unsicherer got. i-bai, i-þa Fragepartikel, ahd. ibu, oba, as. anord. ef „ob und wenn“, ags. gif, engl. if' and 'jai (= Lok. Sg. f.): got. jai „yea, in truth“, nhd. ye (jeh)' — the Germanic branch of the root, with Pokorny's own 'unsicher' on the 'if' words.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1966 leaf 413 s.v. 'if'\", \"stance\": \"partial\",\n   \"note\": \"Klein assembles the same Germanic family (OE gif, OS ef, ON ef, OHG ibu/oba, Goth. ibai) but concludes 'All these conjunctions are prob. traceable to the dative of a noun meaning “doubt”', not to the pronominal stem.\"}\n ]\n})\n\nN.append({\n \"id\": 6,\n \"lang\": \"English\",\n \"words\": \"yet, yes, if\",\n \"verdict\": \"plausible\",\n \"derivation\": \"These are Watkins' three English derivatives under 'i-', but each is qualified in the modern literature. 'yes' < OE gēse/gīse 'so be it', a compound of gēa 'yea' (< PGmc *ja- < the pronominal stem, so this half is secure) and sī 'be it!' (< PIE *h₁es- 'to be'); only the first element belongs to this root. 'yet' < OE gīet, gīeta, with Old Frisian ieta, MHG ieuzo; AHD itself brackets the reconstruction ('preform uncertain'), and Etymonline calls the ultimate origin uncertain with only a possible link to the pronominal stem. 'if' < OE gif < PGmc *ja-ba: Watkins takes the first element as *i-, but Klein and the OED prefer an oblique case of a noun 'doubt' (ON if, OHG iba 'doubt, condition'), and Pokorny himself writes 'unsicherer got. i-bai ... ags. gif, engl. if'. So the arrow is the standard AHD one, but two of the three words rest on a reconstruction that its own authors flag as uncertain.\",\n \"derivation_fa\": \"این سه واژه همانی است که واتکینز ذیل ریشهٔ i- می‌آورد، اما هر سه قید و شرط دارد. yes از انگلیسی کهن gēse است، مرکب از gēa «آری» (از همین ستاک ضمیری) و sī «باد» (از ریشهٔ *h₁es- «بودن»)؛ پس تنها نیمی از آن به این ریشه می‌رسد. دربارهٔ yet (انگلیسی کهن gīet) خود AHD می‌نویسد «preform uncertain» و اتیمانلاین نیز پیوند آن را با ستاک ضمیری تنها احتمالی می‌داند. دربارهٔ if نیز کلاین و فرهنگ آکسفورد آن را از حالت مائل اسمی به معنای «شک، شرط» (نروژی کهن if) می‌دانند و پوکورنی نیز آن را «نامطمئن» می‌خواند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [E_YES, E_YET, E_IF],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The English box carries no reference of its own; it inherits the 'AHD' of its parent box #5, which does list YEA/YES, YET and IF under 'i-'.\"}],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. 'i-' §§4-6\", \"stance\": \"partial\",\n   \"note\": \"'4. ... in Old English gēa ... and gēse, yes (see es-): YEA, YES. 5. Old English giet, gieta (preform uncertain), still: YET. 6. Old English gif (preform uncertain), if: IF.' — Watkins does put all three here, but flags 'yet' and 'if' as of uncertain preform and sends 'yes' partly to *es-.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1966 leaf 413 s.v. 'if'\", \"stance\": \"contradicts\",\n   \"note\": \"'All these conjunctions are prob. traceable to the dative of a noun meaning “doubt”, and orig. meant “on condition that”. (Cp. ON. if, “doubt”, OHG. iba, “doubt, condition”.)'\"},\n  {\"src\": \"Etymonline\", \"where\": \"yes / yet / if\", \"stance\": \"partial\",\n   \"note\": \"'yes' = gēa + sī (< *es- 'to be'); 'yet' — 'ultimate origin remains uncertain, though scholars have suggested a possible connection to the PIE pronominal stem *i-'; 'if' — two competing theories, Watkins' *i- vs Klein/OED's noun 'doubt'.\"}\n ]\n})\n\nN.append({\n \"id\": 7,\n \"lang\": \"Latin\",\n \"words\": \"îdem, iden : same ; îta-em : item\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The derivation is sound but one form is a misprint. Latin īdem (masc.) / idem (neut.) 'the same' is the anaphoric is, id plus the identity-particle -dem (AHD: 'Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same'); item 'likewise, also' is the same stem with the same particle on the adverb ita 'so' — Watkins reconstructs '*i(tə)-em in Latin item', which is exactly what Nourai's display form 'îta-em' is meant to show (it is a reconstruction, not an attested Latin spelling), and Klein s.v. item says it is 'rel. to ita “so”, itaque ..., itidem ..., idem'. But the second form printed in the box, 'iden', is not a Latin word: it is a typographic slip (m read/set as n) for the neuter idem, the very form AHD prints beside 'is, he'. The 400 dpi rendering of the printed page shows 'îdem, iden : same', so the extraction is faithful and the error is the book's.\",\n \"derivation_fa\": \"خود اشتقاق درست است ولی یک صورت غلط چاپ شده است. لاتین īdem (مذکر)/idem (خنثا) «همان» از ضمیر is، id به‌علاوهٔ جزء تأکیدی -dem ساخته شده و item «همچنین» همین ساخت را بر قید ita «چنین» دارد؛ بنابراین «îta-em» صورت بازساختهٔ *i(tə)-em است نه صورتی مضبوط. اما «iden» واژهٔ لاتین نیست و خطای چاپی کتاب به‌جای idem است (تبدیل m به n). تصویر صفحهٔ چاپی با دقت ۴۰۰ نقطه در اینچ نشان می‌دهد که خود کتاب «îdem, iden» چاپ کرده؛ پس خطا از کتاب است نه از خوانش اسکن.\",\n \"error_in\": \"book\",\n \"book_prints\": \"îdem, iden : same\",\n \"correct_form\": \"īdem, idem\",\n \"sources\": [E_ID],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. 'i-': '7. Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same: ID, IDEM, (IDENTICAL), IDENTITY; (IDENTIFY). ... 9. Suffixed and extended form *i(tə)-em in Latin item, thus, also: ITEM.' — both of Nourai's lines, and the correct spelling idem.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"KLN_1966 leaf 443 s.v. item\", \"stance\": \"supports\",\n   \"note\": \"'item, adv., likewise. — L., “just so, in like manner, likewise, also”, rel. to ita, “so”, itaque ..., itidem ..., idem (masc.), idem (neut.), “the same”. See idem ... and cp. esp. iterate.'\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. autem\", \"stance\": \"supports\",\n   \"note\": \"'Renforcé de la particule -em (cf. ita, item)' — Ernout-Meillet analyses item the same way, as the adverb plus the particle -em.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 285\", \"stance\": \"supports\",\n   \"note\": \"'lat. ita „so“, item „ebenso, ebenfalls“' stand in the *i-t(h)- paragraph of this very root.\"}\n ]\n})\n\nN.append({\n \"id\": 8,\n \"lang\": \"English\",\n \"words\": \"identify, identical, identity ; item, iterate\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are learned Latinisms of the 16th-17th centuries and all go back to the Latin box above. identity < French identité < Late Latin identitātem (a calque on Greek tautotēs) from idem 'the same'; identical and identify < Medieval Latin identicus / identificāre on the same base. item is Latin item taken over unchanged, its English noun sense arising because 'item' introduced each successive article of a bill or inventory. iterate < Latin iterāre 'to repeat', from iterum 'again', which Klein analyses as 'i-terum, prop. the neuter of *i-teros, comparative formed from the pronominal base *i-, whence also OI. i-tarah “the other”' — the same *-tero- suffix as in the Avestan and Latin forms of nodes #9-#12.\",\n \"derivation_fa\": \"هر پنج واژه وام‌واژه‌های عالمانهٔ لاتینی در انگلیسی سدهٔ شانزدهم و هفدهم‌اند. identity از فرانسهٔ identité و لاتین متأخر identitātem (گرته‌برداری از یونانی tautotēs) از idem «همان»؛ identical و identify نیز از لاتین میانه identicus و identificāre. item عیناً واژهٔ لاتین است و معنای اسمی آن («قلم، فقره») از آنجا آمده که در صورتحساب‌ها هر بند با item آغاز می‌شده است. iterate از لاتین iterāre از iterum «دوباره» است که خود خنثای *i-teros ، صفت تفضیلی از همین ستاک ضمیری با پسوند *-tero- است — همان پسوندی که در atara- اوستایی و ceterus لاتین دیده می‌شود. ادعای نورایی درست است.\",\n \"sources\": [E_ID],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The English box has no reference of its own; the parent Latin box cites AHD, whose 'i-' entry lists ID, IDEM, (IDENTICAL), IDENTITY, (IDENTIFY), ITERATE, (REITERATE) and ITEM as the English derivatives — exactly Nourai's five.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"KLN_1966 leaf 412 s.v. identity; leaf 443 s.v. item, iterate\", \"stance\": \"supports\",\n   \"note\": \"'identity, n. — F. identité, fr. Late L. identitātem ... fr. L. idem, “the same”'; 'iterate ... fr. iterum, “again”, which stands for i-terum and prop. is the neuter of *i-teros, comparative formed from the pronominal base *i-, whence also OI. i-tarah, “the other”. For other derivatives of the I.-E. pronominal base *i- see idem'.\"},\n  {\"src\": \"Etymonline\", \"where\": \"identity\", \"stance\": \"supports\",\n   \"note\": \"'The ultimate root is Latin idem (neuter) “the same” ... from id (“it, that one”) combined with a demonstrative suffix -dem, with origins in the PIE pronominal stem *i-.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, index\", \"stance\": \"supports\",\n   \"note\": \"The reverse index lists 'ITEM  i-' and 'ITERATE  i-' and 'REITERATE  i-'.\"}\n ]\n})\n\nN.append({\n \"id\": 9,\n \"lang\": \"Indo-European\",\n \"words\": \"E-tero : the other ; Ke-e-tero : other time, other part, again (see Ki 2)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"This is Watkins' own sub-lemma. *e-tero- is the contrastive *-tero- ('one of two') formation on the e-grade of the pronominal stem — Pokorny p.284: 'Zu e- auch die Komparativbildung av. atāra- „dieser, der von beiden“ ..., alb. jāt(e)re „anderer“, umbr. etro- „anderer“, lat. in ceterus „der andere oder übrige“, aksl. eterŭ, jeterŭ „irgendwer“'. *ke-etero- is the same word with the deictic particle *ke- ('here, this') prefixed, and Watkins files it under the demonstrative root ko-/ki- — which is exactly why Nourai's box carries the cross-reference to his root 'Ki 2'. Nourai's two AHD page numbers (1520 for i-, 1523 for ko-) are for the 1976 appendix, whose ordering (i- a few pages before ko-) matches.\",\n \"derivation_fa\": \"این گره دقیقاً زیرمدخلی از پیوست ریشه‌های واتکینز است. *e-tero- ساختی است با پسوند تقابلی *-tero- («یکی از دو») بر گونهٔ e- ستاک ضمیری؛ پوکورنی در صفحهٔ ۲۸۴ همین را می‌گوید و اوستایی atara-، اومبریایی etro- و لاتین ceterus را زیر آن می‌آورد. *ke-etero- همان واژه است با حرف اشارهٔ *ke- «اینجا، این» در آغاز؛ واتکینز آن را ذیل ریشهٔ ko-/ki- می‌آورد و از همین روست که نورایی به ریشهٔ «Ki 2» ارجاع داده است. ادعای نورایی درست است.\",\n \"sources\": [W_CET],\n \"ref_check\": [\n  {\"ref\": \"AHD:1520,1523\", \"status\": \"supports\",\n   \"note\": \"The 1976 New College appendix (pp.1505-1550) is not open online, but its text is that of Watkins 1985, where s.v. 'i-' §10 reads 'Suffixed variant form *e-tero- (see ko-)' and s.v. 'ko-' §II.1 reads 'Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin cēterus (neuter plural cētera), the other part, that which remains: ET CETERA.' Nourai's glosses ('the other'; 'other time, other part, again') are Watkins' words verbatim, and the two page numbers stand in the right order for the alphabetical run i- ... ko-.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 284 (POK_01.txt leaf 295, printed numeral 284)\", \"stance\": \"supports\",\n   \"note\": \"'Zu e- auch die Komparativbildung av. atāra- „dieser, der von beiden“ ..., umbr. etro- „anderer“, lat. in ceterus „der andere oder übrige“, aksl. eterŭ, jeterŭ „irgendwer“'.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 99\", \"stance\": \"supports\",\n   \"note\": \"The same sentence in Walde-Pokorny: 'Zu e- auch die Komparativbildung av. atara- „dieser, der von beiden“, aksl. eterŭ, jeterŭ ..., umbr. etro- „anderer“, lat. in ceterus „der andere oder übrige“.'\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ceterus\", \"stance\": \"partial\",\n   \"note\": \"Confirms *-tero- on the demonstrative *e-/*i- ('c'est le dérivé en *-tero-, *-tro- des thèmes du démonstratif i.-e. *e- et *i-'), but on the prefixed particle is agnostic: 'Sur la particule qui en latin précède *etero-, on ne peut faire que des hypothèses inconsistantes.'\"},\n  {\"src\": \"Wiktionary\", \"where\": \"ceterus\", \"stance\": \"supports\",\n   \"note\": \"'From Proto-Italic *ke-eteros, combining *ke (“here”) and *eteros (“other”) ... PIE *h₁éteros' — the modern form of the same analysis.\"}\n ]\n})\n\nN.append({\n \"id\": 10,\n \"lang\": \"Avestan\",\n \"words\": \"a-târa : one of the two ; at-zur\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The first word is right and the second is a ghost. Avestan atāra- 'the one of the two, this one' is the *-tero- contrastive of the e-grade stem, and it is precisely the form both of Nourai's references put here: Pokorny 284 'Zu e- auch die Komparativbildung av. atāra- „dieser, der von beiden“' and Klein 545 s.v. et cetera 'I.-E. *etero-, “the other”, whence also Umbr. etro-, “another”, Avestic a-tara-, “one of the two, this”'. 'at-zur', by contrast, is not a word in any Iranian dictionary — and its origin is visible on the very page Nourai cites: two lines below the atāra- sentence, Pokorny 284 continues 'eḍ (Nom. Akk. Sg. n.): über lat. ecce, med s. oben; av. aṯ̄ zur Hervorhebung des vorhergehenden Wortes (wie iṯ̄, s. unten; Bartholomae Altiran. Wb. 67)'. Nourai (or an assistant) read the German string 'av. aṯ̄ zur ...' — 'Avestan aṯ̄, [used] for the emphasis of the preceding word' — as if 'at zur' were an Avestan lexeme, and printed it as 'at-zur'. Walde-Pokorny I 99 has the identical sentence. The 400 dpi rendering of book p.194 shows 'at-zur' with no gloss, so the extraction is faithful; the error is the book's. The form that should stand there is the Avestan emphasising particle aṯ̄ 'then, but' (AiW col. 67).\",\n \"derivation_fa\": \"واژهٔ نخست درست است و دومی واژه‌ای ساختگی. اوستایی atāra- «یکی از آن دو، این‌یک» همان ساخت پسوندی *-tero- است و هم پوکورنی (ص ۲۸۴) و هم کلاین (ص ۵۴۵) دقیقاً همین را می‌آورند. اما «at-zur» در هیچ فرهنگ ایرانی نیست؛ خاستگاهش در همان صفحهٔ پوکورنی پیداست: دو سطر پایین‌تر آمده «av. aṯ̄ zur Hervorhebung des vorhergehenden Wortes» یعنی «اوستایی aṯ̄ برای تأکید واژهٔ پیشین»؛ نورایی عبارت آلمانی «aṯ̄ zur» را به خطا واژه‌ای اوستایی پنداشته و «at-zur» چاپ کرده است (همین جمله در والده‌پوکورنی، جلد یک، ص ۹۹ نیز هست). تصویر صفحهٔ چاپی نشان می‌دهد که خود کتاب «at-zur» بی‌معنا چاپ کرده؛ پس خطا از کتاب است نه از خوانش اسکن، و صورت درست حرف تأکیدی aṯ̄ است.\",\n \"error_in\": \"book\",\n \"book_prints\": \"a-târa : one of the two / at-zur\",\n \"correct_form\": \"atāra- 'the one of two'; the second line should not exist — it is Pokorny's German 'av. aṯ̄ zur Hervorhebung ...' (the particle aṯ̄)\",\n \"sources\": [W_CET],\n \"ref_check\": [\n  {\"ref\": \"KLN:545\", \"status\": \"supports\",\n   \"note\": \"KLN_1966.txt leaf 296 (= printed pp.544-545; the leaf carries the numeral 544 and leaf 295 carries 542/543) s.v. 'et cetera': '... and I.-E. *etero-, “the other”, whence also Umbr. etro-, “another”, Avestic a-tara-, “one of the two, this”, Alb. jatere, jatre, “the other”, OSlav. jeteru, iteru, “some, one”.' Nourai's page number and his gloss are exact — but Klein has no 'at-zur'.\"},\n  {\"ref\": \"POK:284\", \"status\": \"partial\",\n   \"note\": \"POK_01.txt leaf 295 (printed numeral 284) gives atāra- exactly as Nourai does ('av. atāra- „dieser, der von beiden“'), so it supports the first word; it also contains, two lines later, the German phrase 'av. aṯ̄ zur Hervorhebung des vorhergehenden Wortes (wie iṯ̄ ...; Bartholomae Altiran. Wb. 67)' out of which Nourai's non-existent 'at-zur' was manufactured.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. I 99 (WLD_Bd1_pages.txt leaf 107)\", \"stance\": \"partial\",\n   \"note\": \"'Zu e- auch die Komparativbildung av. atara- „dieser, der von beiden“ ... lat. in ceterus' — supports atāra-; and the same page has the identical trap sentence 'av. aṯ̄ zur Hervorhebung des vorhergehenden Wortes (wie iṯ̄, s. u. Bartholomae Altiran. Wb. 67)'.\"},\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch (grep 'atāra', 'at-zur')\", \"stance\": \"silent\",\n   \"note\": \"The Google OCR of Bartholomae is too corrupt to isolate the atāra- column, and no string resembling 'at-zur' occurs anywhere in it; Bartholomae's aṯ̄ is at col. 67, the column both Pokorny and Walde-Pokorny cite.\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ceterus\", \"stance\": \"supports\",\n   \"note\": \"'il se retrouve dans v. sl. jeteru “quelqu'un” ... et av. atara-' — independent confirmation of Avestan atāra- as the Iranian member of *e-tero-.\"}\n ]\n})\n\nN.append({\n \"id\": 11,\n \"lang\": None,\n \"words\": \"\",\n \"verdict\": \"unverified\",\n \"derivation\": \"A blank box on the printed page — a narrow empty rectangle to the right of the Avestan a-tāra box, with no language header, no reference and no word. The extraction is faithful; there is nothing to verify. Nourai's layout leaves it empty because the Iranian *-tero- comparative has no New Persian continuation to put there (Persian expresses 'the other of two' with دیگر, from a different root).\",\n \"derivation_fa\": \"این جعبه در صفحهٔ چاپی خالی است و نام زبان و واژه و ارجاع ندارد؛ خوانش اسکن درست است و چیزی برای ارزیابی نیست. علت خالی ماندنش آن است که صفت تفضیلی *-tero- در ایرانی دنباله‌ای در فارسی نو ندارد (فارسی برای این معنا «دیگر» را از ریشه‌ای دیگر به‌کار می‌برد).\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book.\"}],\n \"consulted\": [{\"src\": \"BOOK\", \"where\": \"printed page 194 (PDF 224), rendered at 400 dpi\", \"stance\": \"silent\", \"note\": \"The rectangle is printed empty; nothing was lost in extraction.\"}]\n})\n\nN.append({\n \"id\": 12,\n \"lang\": \"Latin\",\n \"words\": \"ce-terus : the other part ; et-cĕ-terî : and other things (see Eti)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Latin cēterus 'the other, the remaining' continues *ke-etero-, the deictic particle *ke- prefixed to *e-tero-, as Klein p.545 and Watkins (s.v. ko-) both state; the Umbrian cognate etru 'altero' shows the same *-tero- without the particle. The famous phrase is et cētera 'and the other things', et being the conjunction from PIE *eti 'over, beyond' — hence the chart's cross-reference to Nourai's root 'Eti', which matches AHD's own 'eti. Above, beyond ... Latin et, and (< “furthermore”): ET CETERA'. Nourai's citation form 'et-cĕ-terî' is however the masculine plural cēterī 'and the others', which does not fit his gloss 'and other things': the phrase (and the source of English etc.) is the neuter plural cētera. Klein's wording, 'et ... and neut. of ceteri', is very likely what Nourai compressed into the wrong form. Also, only Klein/Watkins are confident about the prefix: Ernout-Meillet says of the ce- that 'on ne peut faire que des hypothèses inconsistantes'.\",\n \"derivation_fa\": \"لاتین cēterus «دیگر، باقی» دنبالهٔ *ke-etero- است، یعنی حرف اشارهٔ *ke- به‌علاوهٔ *e-tero- — همان که کلاین در صفحهٔ ۵۴۵ و واتکینز ذیل ko- می‌گویند؛ هم‌ریشهٔ اومبریایی etru «دیگری» همین ساخت را بدون حرف اشاره نشان می‌دهد. عبارت مشهور et cētera «و دیگر چیزها» است که et در آن از *eti «فراتر، علاوه بر» می‌آید و از همین رو نورایی به ریشهٔ «Eti» ارجاع داده است. ولی صورتی که آورده (et-cĕ-terî) جمع مذکر cēterī است و با معنای «و دیگر چیزها» نمی‌خواند؛ صورت درست جمع خنثای cētera است. افزون بر آن، ارنو-مییه دربارهٔ جزء نخست (ce-) می‌گوید فرضیه‌ها سست است. پس ادعای نورایی در اصل درست ولی در صورت مضبوط لغزش‌دار است.\",\n \"sources\": [W_CET],\n \"ref_check\": [\n  {\"ref\": \"KLN:545\", \"status\": \"supports\",\n   \"note\": \"KLN_1966.txt leaf 296 (printed pp.544-545) s.v. 'et cetera': 'L., fr. et, “and” (see et), and neut. of ceteri, “the others”, which is formed fr. I.-E. pron. pref. *ce-, “there; behold” (see he), and I.-E. *etero-, “the other” ...' — exactly Nourai's analysis, including the *ce- prefix, and note Klein's 'neut. of ceteri', which is where the wrong form cēterī probably comes from.\"},\n  {\"ref\": \"POK:284\", \"status\": \"supports\",\n   \"note\": \"POK_01.txt leaf 295 (printed 284): 'umbr. etro- „anderer“, lat. in ceterus „der andere oder übrige“' — Latin ceterus is filed under this root on the cited page.\"}\n ],\n \"consulted\": [\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. ceterus\", \"stance\": \"partial\",\n   \"note\": \"'ceterus, -a, -um: qui reste, restant, d'où au pl. ceteri ... Comprend évidemment le mot qui se retrouve en ombrien ... etru “altero” ...; c'est le dérivé en *-tero-, *-tro- des thèmes du démonstratif i.-e. *e- et *i-; il se retrouve dans v. sl. jeteru ... et av. atara-. ... Sur la particule qui en latin précède *etero-, on ne peut faire que des hypothèses inconsistantes.' Supports the stem, doubts the *ke-.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ko- §II.1 and s.v. eti\", \"stance\": \"supports\",\n   \"note\": \"'Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin cēterus (neuter plural cētera), the other part, that which remains: ET CETERA'; and 'eti. Above, beyond ... 2. Latin et, and (< “furthermore”): ET CETERA. [Pok. eti 344.]' — note Watkins' 'neuter plural cētera', the correct form.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"ceterus\", \"stance\": \"supports\",\n   \"note\": \"'From Proto-Italic *ke-eteros ... The most prominent descendant is et cētera (literally “and the other things”)' — neuter plural, confirming that the phrase is cētera, not cēterī.\"}\n ]\n})\n\nN.append({\n \"id\": 13,\n \"lang\": \"English\",\n \"words\": \"et cetera\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English et cetera (and its abbreviation etc.) is the Latin phrase taken over whole, current in English from the 14th century in legal and scribal use, where it closed an enumeration; the modern spelling and the pronunciation with /s/ follow ecclesiastical Latin. It is the direct descendant of node #12 and needs no further sound change; Klein and Watkins both put it here.\",\n \"derivation_fa\": \"عبارت انگلیسی et cetera (و کوتاه‌نوشتِ etc.) عیناً همان عبارت لاتین است که از سدهٔ چهاردهم میلادی در متن‌های حقوقی و دفتری انگلیسی برای پایان دادن به فهرست به‌کار می‌رفته است؛ هیچ دگرگونی آوایی در کار نیست و تلفظ با /s/ از لاتین کلیسایی می‌آید. ادعای نورایی درست است.\",\n \"sources\": [W_CET],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The English box carries no reference; it inherits KLN:545 from its parent, and Klein's headword there is precisely 'et cetera'.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"KLN_1966 leaf 296 s.v. et cetera\", \"stance\": \"supports\",\n   \"note\": \"'et cetera, “and other things”. — L., fr. et, “and” ... and neut. of ceteri, “the others”' — Klein's gloss is word for word Nourai's.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ko- and eti\", \"stance\": \"supports\",\n   \"note\": \"ET CETERA is the English derivative listed under both *ke-etero- (ko-) and Latin et (eti).\"}\n ]\n})\n\nimport io, os\np = \"/home/sfmqrb/git/rishe/data/verification/page-224.json\"\nwith io.open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"wrote\", p, os.path.getsize(p))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk224.py"
}
```


### [2026-09-06T15:38:31.028Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-224.json 50695
```


## [2026-09-06T15:38:35.569Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-224.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 224"
}
```


### [2026-09-06T15:38:37.491Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 4, 'confirmed': 5, 'unverified': 2, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'partial': 2, 'not_checked': 5}
books consulted: {'supports': 24, 'partial': 7, 'silent': 5, 'contradicts': 1} | by book: {'KLN': 5, 'WLD': 4, 'AHD': 4, 'LAT': 4, 'BRT': 3, 'Wiktionary': 3, 'POK': 3, 'KNT': 2, 'BOOK': 2, 'Etymonline': 2, 'PHD': 1, 'NYB': 1, 'MON': 1, 'HUB': 1, 'ARY': 1}
```


## [2026-09-06T15:38:59.593Z] AGENT

Done. `data/verification/page-224.json` written; `verify_check.py 224` reports **13/13 nodes, 0 PROBLEM lines**.

**Page 224 (book p.194) — root `I 2, Io, E` [Indo-European] "pronominal stem", PART 1**

- Root: **confirmed** — Pokorny IEW 281–286 *e-3, ei-, i-* (entry opens exactly on p.281); Watkins/AHD "i-. Pronominal stem [Pok. 3. e- 281]".
- Node verdicts: confirmed 5, plausible 4, transcription_suspect 2, unverified 2 (the two blank boxes, #4 and #11 — printed empty, extraction faithful).
- Ref checks: 12 supports, 2 partial, 5 not_checked (nodes with no refs of their own).

Flagged items:
- **#10 `at-zur` (Avestan) — transcription_suspect, error in the BOOK.** Not a word in any Iranian dictionary. Origin located: on the cited page Pokorny 284 (and Walde-Pokorny I 99) reads "av. aṯ̄ **zur** Hervorhebung des vorhergehenden Wortes" — Nourai read the German "aṯ̄ zur" as a lexeme. The other word in the box, `a-târa`, is fully confirmed (POK 284, KLN 545).
- **#7 `iden` (Latin) — transcription_suspect, error in the BOOK.** Misprint (m→n) for the neuter `idem`, which is what AHD prints ("Latin is, he (neuter id), and idem"). The derivation itself (īdem, item < *i- + -dem / *i(tə)-em) is sound.
- **#12** `et-cĕ-terî` glossed "and other things" is the wrong Latin form (masc. pl. cēterī); the phrase is neuter pl. **et cētera** — marked plausible, likely a compression of Klein's "and neut. of ceteri".
- **#1** "itta" is not Avestan (Pokorny 285 has it as OInd. itthā/ittham/iti, Lat. ita) → plausible. **#3** glosses loose (ima- = "this", not "she, he"; "then" belongs to the particle aṯ̄) → plausible. **#6** yet/if rest on preforms AHD itself flags "uncertain"; Klein/OED derive *if* from a noun "doubt" → plausible.

No extraction errors: every form in the JSON matches the 400 dpi rendering of the printed page (checked crops of nodes 1, 7, 10, 12; page image saved to `data/verification/sources/refs/ocr/BOOK/224.png`).

Notable ref findings: Nourai's page numbers are unusually accurate here — **KLN:545** = Klein's *et cetera* entry (leaf 296 = printed 544/545) and **KLN:763** = Klein's *ibidem* entry (leaf 410), both verbatim matches; **HRN:32** is Horn's entry no. 137 giving īdar/īdūn < ī/ēd, phlv. ētar, ētūn, ap. aita-, aw. aē-ta- — Nourai's arrow verbatim; **BQT** gives ایدون as "اکنون … اینچنین", i.e. his gloss "now, such" word for word. **KNT:203** is only *partial* on two nodes: Kent p.203 has `ya- rel. pron.` (covers "yô") but the OP `ima-`/`idā` entries are on pp.173–174. Eight web pages archived via `fetch_source.py`.
