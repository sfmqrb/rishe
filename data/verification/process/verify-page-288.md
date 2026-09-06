# Verification process log — verify-page-288


## [2026-09-06T21:57:24.078Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 288 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-288.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-288.json. Write /home/sfmqrb/git/rishe/data/verification/page-288.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 288` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:57:25.841Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:57:26.512Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:57:26.526Z] TOOL RESULT

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


## [2026-09-06T21:57:26.780Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-288.txt"
}
```


### [2026-09-06T21:57:26.795Z] TOOL RESULT

```
1	=== PDF page 288 (book page 258) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kut : small, short  (refs IEC:594)
4	#1 (parent #0) [Avestan] refs=HUB:89; HRN:194; IEC:594 | ku, kva, kutaka : small ; kvataka, kautaka : child
5	  #2 (parent #1) [Persian] refs=BQT:1721; IEC:594 | kŭtâh «کوتاه» : short ; kŭdak «کودک» : child ; kŭčak «کوچک» : small
6	--- entry 1 ---
7	ROOT Kut-no -> redirect to Skeu 2
8	--- entry 2 ---
9	ROOT Kuur -> redirect to Keu 2
10	--- entry 3 ---
11	ROOT Ku-z-dho -> redirect to Skeu 2
12	--- entry 4 ---
13	ROOT Kwal -> redirect to Skwalo
14	--- entry 5 ---
15	ROOT Kwalo -> redirect to Skwalo
16	--- entry 6 ---
17	ROOT Kwalos -> redirect to Skwalo
18	--- entry 7 ---
19	ROOT [Indo-European] Kwe, Qwe, Kue, Que, Kwi 2 : and  (refs POK:635)
20	#1 (parent #0) [Avestan] refs=POK:635; KLN:1425 | ca, ča : and ; čiš-ca 1 : any, whatever ; čit 1
21	  #2 (parent #1) [None] refs=None | 
22	#3 (parent #0) [Old Persian] refs=POK:635 | câ, čâ : and ; čiy 1
23	  #4 (parent #3) [None] refs=None | 
24	#5 (parent #0) [Latin] refs=POK:635 | que : and ; semi-sque : one half more
25	  #6 (parent #5) [English] refs=KLN:1425 | sesqui- : half more ; sesqui centennial
26	
```


## [2026-09-06T21:57:29.877Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-288.json",
 "description": "Read source JSON page 288"
}
```


### [2026-09-06T21:57:29.936Z] TOOL RESULT

```
{
  "pdf_page": 288,
  "book_page": 258,
  "entries": [
    {
      "root": {
        "name": "Kut",
        "lang": "Indo-European",
        "refs": "IEC:594",
        "gloss": "small, short"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HUB:89; HRN:194; IEC:594",
          "words": [
            {"translit": "ku, kva, kutaka", "gloss": "small", "script": null},
            {"translit": "kvataka, kautaka", "gloss": "child", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1721; IEC:594",
          "words": [
            {"translit": "kŭtâh", "gloss": "short", "script": "کوتاه"},
            {"translit": "kŭdak", "gloss": "child", "script": "کودک"},
            {"translit": "kŭčak", "gloss": "small", "script": "کوچک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kut-no",
        "redirect": "Skeu 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kuur",
        "redirect": "Keu 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ku-z-dho",
        "redirect": "Skeu 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kwal",
        "redirect": "Skwalo"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kwalo",
        "redirect": "Skwalo"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kwalos",
        "redirect": "Skwalo"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kwe, Qwe, Kue, Que, Kwi 2",
        "lang": "Indo-European",
        "refs": "POK:635",
        "gloss": "and"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:635; KLN:1425",
          "words": [
            {"translit": "ca, ča", "gloss": "and", "script": null},
            {"translit": "čiš-ca 1", "gloss": "any, whatever", "script": null},
            {"translit": "čit 1", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:635",
          "words": [
            {"translit": "câ, čâ", "gloss": "and", "script": null},
            {"translit": "čiy 1", "gloss": null, "script": null}
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
          "lang": "Latin",
          "refs": "POK:635",
          "words": [
            {"translit": "que", "gloss": "and", "script": null},
            {"translit": "semi-sque", "gloss": "one half more", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:1425",
          "words": [
            {"translit": "sesqui-", "gloss": "half more", "script": null},
            {"translit": "sesqui centennial", "gloss": null, "script": null}
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


## [2026-09-06T21:57:30.552Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T21:57:30.592Z] TOOL RESULT

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


## [2026-09-06T21:57:42.584Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC grep kutaka/kautaka ===\"; grep -n -i -E 'kutaka|kautaka|kvataka' IEC.txt | head -30\necho \"=== IEC grep kut- root ===\"; grep -n -E '^k[uū]t' IEC.txt | head -40\necho \"=== HUB kutah ===\"; grep -n -i -E 'kutāh|kūtāh|kutah|kōtāh|kotah' HUB.txt | head -20\necho \"=== HRN kutah ===\"; grep -n -i -E 'kutāh|kūtāh|kutah|kotah|kūdak|kudak' HRN.txt | head -20",
 "description": "Grep IEC, HUB, HRN for kutah"
}
```


### [2026-09-06T21:57:42.674Z] TOOL RESULT

```
=== IEC grep kutaka/kautaka ===
=== IEC grep kut- root ===
8472:kut- (1), (kutik-) ‘tickle’. Cf. gudil- (gudul-) Arm. (ambig.) ktik-ktik ollam, id. (cf. gudil-); Blg. kátkam ‘fondle’; Li. kutenü, -énti (2) ‘tickle’; Latv. impers. man kut, inf: kutet ‘itch, tickle'
8473:kut- (2) ‘strong; strength'.' See kutor-
8474:kut- (3) 'diminutive'. Variant: kütoko- Av. cf. kutako "little; Per. cf. kütàh ‘short’; kucak “little; küdak ‘boy’. (Li. kūdikis, m. “child” seems to be a Slav. LW. fr. *xud-)
8475:kut- (4) (küta, is) ‘stump’ W cwt, f. and cot, pl. -iau, f. ‘tump, tail’; OCS kyta “arm, shoulder’; Cz. kýta “leg, haunch’; Big. kita ‘penis? '
8476:kut- (5) (kütos, à) ‘tassel, tuft’ Blg. kit ‘tuft of wool, fibre’; OCS cf. kytüka ‘bunch’; Cz. kytka, id.; Li. kutà, and fpl: ku- tos ‘tassel, fringe? beside kütas, m. id.
8477:kut- (6) (kūtis, à, io) ‘shelter, house’. See next Per. (?) kuc ‘household’; Hitt. kuca (queried) "wall, side’; Ligurian (in Rumansh) kuts ‘house’; a kuts “at home’; Ir. cuithe, m. ‘den, pit; OE hyó ‘harbour’; Li. kūtis, gs -ičs, & kūtē ‘stable, stall; Latv. kūts, gp kücu, f. id.
8478:kut- (7) (kütis, os, iom) “container, skin”. Cf.
8481:kut- (6) Arm. cf. (?) ktit, gs kčči, Let 'earthen pot (from *kütitis?); Gk. kütos, n. ‘hollow, belly, jar, body'; kutis, f. “box, basket'; cf. Gk. ég- kuti (“on the skin”, fr. zen Lat. cutis, f. gp *cutium 'skin"); OHG hüt, gp hütio, f. id.; adj. *with a skin'; OE hyd, f. id.; ON húð, pl. ir, f. id. beside hýði, n. ‘husk, shell’; W cwd, pl. cydau, m. ‘pouch’
8482:kut- (8) ‘grain, kernel, nut? (?) Arm. (ambig.) kut, gs kto, o-st ‘grain, kernel; OHG hodo ‘testicle’; Lat. cf. cutio, -onis, m. *woodlouse'
8483:kutokos, see kut- (3)
8484:kutor-, kutno- 'strength; strong'. Cf. WP II, 601 Hitt. kutar, ds kutani (-tt-) ‘strength’; Arm. cf. ktrič ‘brave’; Li. kutrüs ‘vigorous, active’; kùtinu, -inti, v. ‘strengthen’ beside kuntu, pf. kutau, inf. kusti “recover”
8485:kūturið ‘dawdle’ SWG haudern, id.; Li. kūturióti, id.; Latv. cf. kūtrs, adj. ‘sluggish’. Uncertainly Arm. kkrim, v. (1) wait", if for *kutur-). O-gde in Latv. kau- tra (2) ‘hesitancy’
8489:kut- — kuoit- (kuoitio, kuoitaio)
=== HUB kutah ===
6674:H. 296 s. oben p. 38. Die Etymologie von kutah kurz' (s.
6677:vorkommenden t (wie z. B. in kutah) zu erklaren sind, da
=== HRN kutah ===
```


## [2026-09-06T21:57:45.532Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 635 area: q<sup>u</sup>e ===\"; grep -n -E 'sesqui|semisque|semis-que' POK_full.txt KLN_1966.txt KLN_1971.txt SKT.txt | head -30\necho \"=== KNT čā ===\"; grep -n -E '\\bcā\\b|\\bča\\b|caiy|ciy' KNT.txt | head -30",
 "description": "Grep POK/KLN/KNT"
}
```


### [2026-09-06T21:57:45.603Z] TOOL RESULT

```
=== POK 635 area: q<sup>u</sup>e ===
KLN_1971.txt:217511:the first element in sesqui-, sesterce. Cp. also the 
KLN_1971.txt:219015:sesqui-, combining form meaning ‘one half more*. 
KLN_1971.txt:219023:sesquicentennial, adj., pertaining to a century 
KLN_1971.txt:219025:niversary. — Compounded of sesqui- and cen- 
KLN_1971.txt:219028:sesquipedalian, adj., a foot and a half long. — 
KLN_1971.txt:219029:Formed with suff. -ian fr. L. sesquipedalis , 
KLN_1971.txt:219030:which is compounded of sesqui- and pedalis , 
KLN_1971.txt:270701:zingiberene, n., a sesquiterpene hydrocarbon, 
KLN_1966.txt:34521:OHG.  sami-,  ‘half’  (cp.  e.g.  OE.  sam-ewieu, OHG.  sami-quek,  ‘half-alive’).  Cp.  hemi-  and the  first  element  in  sesqui-,  sesterce.  Cp.  also  the first  element  in  sandblind. semi-annual,  adj.,  half-yearly.  —  Compounded  of semi-  and  annual.
KLN_1966.txt:34741:sesqui-,  combining  form  meaning  ‘one  half  more’. —  L.,  contraction  of  *sem(i)sque,  ‘and  a  half (more)’,  fr.  semi-,  ‘half’  (see  semi-),  and  -que.
KLN_1966.txt:34743:sesquicentennial,  adj.,  pertaining  to  a  century and  a  half;  n.,  the  one  hundred  and  fiftieth  an¬ niversary.  —  Compounded  of  sesqui-  and  cen¬ tennial.
KLN_1966.txt:34744:sesquipedalian,  adj.,  a  foot  and  a  half  long.  — Formed  with  suff.  -ian  fr.  L.  sesquipedalis, which  is  compounded  of  sesqui-  and  pedalis, ‘pertaining  to  the  foot’.  See  pedal,  adj.
=== KNT čā ===
399:masc. kašciy, nt. cifciy, avaSciy, aniyasciy, with Sc from -s q*- and -d g*- respectively, in sandhi; no specific reason сап be assigned for the borrowing by OP of this type.
631:Before enclitics, a final nasal which would otherwise be written, is retained: (батса = gaibām-cã; zXagam-Sim, paruvam-ciy, adam-&im.
640:телу, twice in DNb 51-2, for -memiy, = ciydkaramcamary.
722:ciydkarammeciy® DNb 51, 511, for -cmeüp, = ciyükaram-ca-mauy.
783:wāipašiyam DB 1.47, but wăipašiyahyā DNb 15. t | ciyakaram DNb 50, 51, 514, but ciyăkaram DNa 1
826:DN xxix Фуат: Maciya ‘this is the men of Maka’. А?Р 9 tyam : така ‘this is the Drangians’. А?Р 14 туат : Sakü : hawmavarga ‘this is the
918:*g*id, OP -ciy, Skt. cid, Gk. тї ‘what’, Lt. quid.
1091:Av. dtar- d6r- ‘fire’, seen in the OP month-name Aciyddiya- and probably in the personal name Аспа (despite the fact that Аста was an Elamite).
1100:OP Aciyddiya-, Elam. ha-18-&-4a-ti-ia-18.
1255:OP Maka, a province, but ethnic Maciya, with palatalization because the suffix began with the palatal sound.
1256:OP Ahaufaciya ‘men of *Akaufaka’, similarly.
1333:The sandhi product of -d c- has a similar varia- tion: OP s (not attested) and remade c (§130), Med. $c; there are the following examples: pIE *ed-q*id, ОР aciy ‘then’, Av. а/с. plE *7od-q*id, ОР yaciy ‘when’, Av. yatčit. pIE *g#d-gtid, OP cišciy ‘anything’, with Med.
1335:šc; so also OP avasciy from earlier *avad-cid, OP aniyasciy from earlier *angad-cid. $106. PIE у remained unchanged in most IE languages, down into the recorded forms of the languages; exceptional combinations in which it suffered change in OP, are mentioned below. pIE *réto- ‘directed’, OP rästa- ‘straight’, Av. rasta- ‘upright’, Lt. тёсіо-. pIE *pro, ОР fra- (in cpds.), Av. fra, Skt. pra, Gk. тро. |
1379:enclitics: kamnam, jiyamnam, acc. nākam, adam- : q | kim, avakaram-ca-maiy, parwam-ciy. On [n*yà]- ; kama = |kam-ma, see $130. On pIE m, see $67; ^
1403:Note pAr. kj > pAr. ё > OP Sy, $104; pAr. fi > рії. 6; > OP sy, 580. OP Maciya- to the province-name Maka must be for *makuos, or a late formation in which *makjos did not make the second phonetic change; similarly Akaufaciya to * Akaufaka.
1405:At the end of a word, y was added in OP to a final i: thus OP party, Skt. pári, Gk. тері; OP ciy, Skt. cid, Lt. quid ($87; $84 for failure to write final d in OP); OP encl. -maty, Skt. me, Gk. шо.
1634:(2) pAr. palatalization of velars before palatal vowels, giving an alternation in OP k/c, g/j ($78.11): Maka Maciyà, kunautiy kartam car- lanaiy, kašciy cisci, drauga draujana adurujiya, pard-gmala ha"gmalà à-jamiyü.
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
1640:karam-ca-maiy DNb 27f; ciyakaram-ca-mary
1662:also hauv-maty hauv-taiy hauv-ciy.
1672:I. Doubled consonants are written single: apis + Sim = dpisim DB 1.95f; taumaniš + Saiy = taumantSaiy DNb 25f; -kam + тату in {n*ya|kama A’Sa 4. In DNb 511 ciyakaram*m"cy is twice written for -m’c'my*, = ciyakaram-ca-maty.
1801:IL. Secondary: *Akaufa-ka- in Akaufaciya-; Andma-ka-; ar-ika-, to pAr. *asra-, LAv. аюга; Атќа-Ка-, hypocoristic to a compound name; äršti- ka-, probably with vriddhi; kapauta-ka-; kdsa-ka-; ba^da-ka-; vazra-ka-; Vahau-ka-, hypocoristic to a compound name.
1894:hamarana-kara- ‘battle-making’; züra-kara- ‘evil- doing’; ddraniya-kara- 'gold-working'; ciyd- kara- ‘doing how much’, ava-kara- ‘doing that’.
1981:Akaufaciya ‘Men of Akaufaka’; Unarazmiy and -miš ‘Chorasmia’; Gadára ‘Gandaritis’; 8ata- gu’ Sattagydia’; Рала ‘the Daae’; Maka or ethnic Maciya; Saka or fem. бака Scythia’ or Хака ‘the Scythians’; Sug(u)da ‘Sogdiana’; Haraiva ‘Aria’; Hidus Sind’.
2010:57 Same as Fem. as Derivative Pl. Ethnic Masc. as Province Ethnic Province Ethnic as Province Province Babirus X Babiruviya Maka Maciya* Мастӣ Майа X Mudraya X Mudraya Yauna X Yauna Saka X Saká Saka Sug(u)da Skudra x* Sparda Spardtya Zraka x* Натайа Harawats§ Harauvatiya* Hiduš Hiduya*
2027:Nom. Sg. martiya, х$йуабтуа, Ката, baga, drauga, hamiciya, атиќа; man’s name, Kabijiya; place names and ethnics Раза, Майа, Sugda Suguda, Saka, Sparda, Mudréya, Uja боја, Yauna, Parðava, Armina, Arminiya, Asagaria, Gadāra, Márgava, Uyjiya.
2040:Nom. Pl. martiyd, z$ayatiyà, hamiciyd, anuštyā, takabard, tigrazaudà, haumavargà, paruva, Mada, Вока, Mudrüyà, Yauna, Uvjiya; with double
2089:Nom. Sg. taumd ‘family’, Мила, framand, yau- viyà, didd, Ка; Aéurd; adjectives Кай, gasla, hamiciyd. |
2238:1! Nom. hamiciya DB 2.93 is predicate to two singular masculine nouns, but is more probably plural than dual; ef. $259. ? The form karšā does not belong here, nor probably artá-cà brazmanty (if во normalized) nor tau- mani-Saty; on these words see the Lexicon s.vv. * On these forms, cf. Kent. Lg. 19.225;
2277:Ace. Nt.: apataram, aparam, суат, dargam, ragam, dar$am, duvaislam, müram, paranam, parwam, duvitiyam, -ciy, perhaps hama (DB 4.90); compounds duwiü-paranam (first part instr.), fra-haravam (first part adv.), ha-karam (first part insep. numeral), hyáparam (abl. hyà + aparam); cf. conj. yad-iy.
```


## [2026-09-06T21:57:53.422Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6650,6700p' HUB.txt\necho \"=== offsets ===\"; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['IEC','HUB','HRN','POK','KLN','BQT','MON','BRT','KNT','ARY','AHD','WLD','SYN','LEW','LAT','SKT']:\n    v=d.get(k,{})\n    print(k, {kk:v.get(kk) for kk in ('kind','url','local_file','page_offset','lookup_hint')})\n\"",
 "description": "HUB context and ref offsets"
}
```


### [2026-09-06T21:57:55.208Z] TOOL RESULT

```
Ap. t (= idg. t) = np. ^, d und y.
§ 83. Ap. t = np. t:
a) im Anlaut: tdxtan 'laufen, laufen lassen', zd. ta6
u. s. w. Vgl. H. 366—409.
b) im Inlaut nach s, s, a?, / in alien Fallen (auch wenn
Spirans und t erst nach Vokalausfall zusammengekommen
sind, wie in hist 'zwanzig aus "^vtsatj duvest zweihundert'
aus *duvesat, astar ^Maulesel' aus "^asatar = skr. agvatara-).
Nach Vokalen und tonenden Konsonanten ist t (statt
zu d zu werden, § 84) geblieben:
c) in Lehnwortern : atas 'Feuer = zd. dtars, arm. afa^
(Sebeos p. 27), auch im N. pr. Afasxoday (Mos. Kalank.)
(die echt persische Form ist d^ar); patydra 'Ungliick' = zd.
paityara- (s. oben p. 37) ; basdtan *Bosewicht' — zd. pesotanu-
(s. oben p. 30).
d) in echt persischen Wortern unter dem Einfluss der
Analogic, so im Komparativsuffix -tar in Tuhtar, bartar,
firotar u. s. w. nach Analogie von n^ktar *besser , pestar 'der
vordere* u. s. w. ; in -tan als 2. Glied von Komp. wie hartan
*hochmiithig, arm. aparfan-er, paz. awartanl 'haughtiness
Min. Gl. 22; firotan (aus firod-fan) 'humilis', paz. ertan- 189 -
*humble* Min. Gl. 72, die noch als Komp. mit tan (vgl. x"^stan
selbst', abistan *schwanger ) gefuhlt wurden ; kabutar 'Taube'
neben kafiar *Taube' (H. 842). Ueber partav *Glanz, Strahl
H. 296 s. oben p. 38. Die Etymologie von kutah kurz' (s.
oben p. 89) ist noch nicht gefunden. Aber die Frage bleibt
noch oflfen, wie die nach Vokalen im Persischen iiberhaupt
vorkommenden t (wie z. B. in kutah) zu erklaren sind, da
urspr. t nach Vokal der Kegel nach zu d werden musste.
§ 84. Ap. t wird nach Vokalen und tonenden Kon-
sonanten (r, n) im Np. zu d:
a) Ap. t zwischen Vokalen = phi. t, paz. d, np. d
(in alten Handschriften, vgl. Muwaffaq und JRAS. 1894,
p. 441 fig.)*), spater np. d'^): pidar = pidar 'Vater, ap.
pitar-; birddar = hiradar *Bruder, ap. bratar-; madar
= madar *Mutter , ap. matar- u. s. w. in zahlreichen Bei-
spielen. Im Phi. erscheint hier stets t^ ebenso im Armeni-
schen mit nur drei Ausnahmen: Hruden (Mos. Xor.) =
paz. FredUn, zd. ^ra^taona-; anusadr Salmiak' (nur bei
Cax^ax und im kleinen Wb. !), np. nOsadir A. M. p. 263,
syr. anosHdur (de Lag. G. A. 9); ardu ein Getreidemass'
(AT.) = ap. dprdpT]? Arm. Hruden (aus *Hredun) zeigt,
dass zur Zeit des Moses (5. oder 7. Jhd.) ap. t schon zu
d' geworden war. Da auch Syrer und Griechen den Namen
zd. kavata- = phi. kavdt seit 500 immer mit J {Dp, Kafid-
drjg u. s. w., BB. 4, 33) schreiben, so war der Uebergang
von ap. t zwischen Vokalen in d im 5. Jhd. vollzogen.
Vgl. auch syr. I'lin'pno (= pers. Mlladgird, Stadt im Ge-
biet von Rai) 4. Jhd., fr^^HX i. J. 485 ZDMG. 43, p. 409,
gr. ^AdaQ(iiydv(av (phi. aturpdtakan) , 'AanBfU^r^q , Mcoftbdrjg
{-ptiTjQ = zd.paiti', arm. pet) bei Pro cop (oben § 73),
=== offsets ===
IEC {'kind': 'archive_djvu', 'url': 'https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
HUB {'kind': 'archive_djvu', 'url': 'https://archive.org/details/persischestudie00hbgoog', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
HRN {'kind': 'archive_djvu', 'url': 'https://archive.org/details/grundrissderneu00horngoog', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
POK {'kind': 'archive_djvu', 'url': 'https://archive.org/details/indogermanisches01pokouoft', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
KLN {'kind': 'archive_djvu', 'url': 'https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
BQT {'kind': 'archive_djvu+local_scan_ocr', 'url': "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
MON {'kind': 'website+archive_djvu', 'url': 'https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)', 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
BRT {'kind': 'archive_djvu', 'url': 'https://archive.org/details/altiranischeswr00bartgoog', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
KNT {'kind': 'archive_djvu', 'url': 'https://archive.org/details/oldpers', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt', 'page_offset': 'leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations."}
ARY {'kind': 'local_scan_ocr', 'url': '', 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
AHD {'kind': 'archive_djvu+website+archive_restricted', 'url': 'https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
WLD {'kind': 'archive_djvu', 'url': "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
SYN {'kind': 'archive_djvu', 'url': 'https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
LEW {'kind': 'archive_djvu', 'url': 'https://archive.org/details/lateinischesetym0000aloi', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt', 'page_offset': '1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.'}
LAT {'kind': 'archive_djvu', 'url': 'https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt', 'page_offset': 'leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'."}
SKT {'kind': 'archive_djvu', 'url': 'https://archive.org/details/aconciseetymolo01skeagoog', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
```


## [2026-09-06T21:58:01.805Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB leaf 99 (p.89) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==100' HUB.txt | head -60\necho \"=== HRN leaf 215/216 (p.194) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==216' HRN.txt | head -60",
 "description": "Print HUB p.89 and HRN p.194"
}
```


## [2026-09-06T21:58:03.224Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\ni=t.find('kut- (3)')\nleaf=t[:i].count('\\f')\nprint(\"leaf(0-based)\",leaf,\"-> approx printed page\", (leaf-15)*2, (leaf-15)*2+1)\nprint(t[i-200:i+400])\nEOF",
 "description": "Locate IEC kut-(3) leaf"
}
```


### [2026-09-06T21:58:03.547Z] TOOL RESULT

```
=== HUB leaf 99 (p.89) ===
- 89 -
und Impt.) = kandol („in the past tenses'') kann
doch nur LW. sein (np. praes. kanam, perf, handam).
Die Differenz zwischen iran. han- und skr. khan ist
noch nicht befriedigend erklart.
870. Np. kamzak ist durch das Deminutivsuffix ak von
kaimz abgeleitet. Phi. kanlSak ware = np. kanlza,
Vgl. Darmesteter, Etud. iran. I, p. 288. Ueber
dial, kine s. Mann, ZDMG. 47, 705.
871. Np. hutdh oder kdtah (nach dem afgh. LW. kdtah) heisst
eigentlich 'kurz* (nicht 'klein*) und ist von np. kddak
*Kind' = phi. kotak *a child, an infant' Gl. and Ind.
201, arm. LW. kotak *der Eleine' (Beiname des armen.
Konigs Xoarov bei Faust us von Byz.) zu trennen.
Letzteres ist durch Suffix ak von *kOt = ap. ^kauta-
abgeleitet, zu dem das auf schwachster Wurzelstufe
stehende zd. ktUaka- *klein* gehSrt. Horn's Erklarung
von kodak aus ^kvataka- (vom Pronominal stamm kva-,
ku"?) ist mir unverstandlich.
872. Np. fcil^a 'irdene Krug, Kanne* = afgh. kUza an earthen
vessel for water with a spout* ist abgeleitet mittelst
des Suffixes a (= phi. ak) von kUz = arm. LW. kuz
'Krug, Kanne' = arab. LW. hOz *kleiner Krug und
geht mit diesem auf ein ap. *kuza (oder *kuja) zuriick.
Ueber zd. xawza- vgl. oben Nr. 483.
Hier fehlt np. Uui {kUz und kUza) gekriimmt' {kuz-pust
Fird. I, 503, Z. 7), afgh. ko^ (LW.?) crooked, bent*
= skr. kubja^ 'krumm, bucklig*.
873. Die Zusammenstellung setzt eine idg. Wrzl. kul-
(hochstufig ketd^ kouT) voraus, die es nicht giebt.
874. Zu streichen.
875. Dazu arm. LW. ioAai 'Berg, Woge' und nach Geiger
afgh. kvah *H6cker .
Hier fehlt np. kavl», kavHz = arab. LW. qafiz u. s. w., phi.
kapU (so zu lesen) Gl. and Ind. 197 u.s.w., arm. LW.
kapic 'ein Maass fur Getreide' etc., ap. xan/drj de La-
garde, Ges. Abh. 198.
=== HRN leaf 215/216 (p.194) ===
- 194 —
869. kenden graben', Praes. ken-em,
ap. aw. \/kan- graben'; phlv. kantan (Bund.), kandau
(AV., PPGl.), paz. /andan; ai. l/khan-, khdnati.
kurd. kendn; af/. kandal; oss. t. vergl. nijgänin
'begraben' (Urform "^Mnin^ 203); arm. vergl. akan
diOQvy/iia (H. No. 3).
Auf die mit kh anlautende Form der Wurzel gehen
np. (arab.) yendeq Graben , phlv. xantak, np. /öw«j, /an
'Haus' (No. 405) und /am 'Quelle' (No. 466) zurück;
vergl. auch feryen neu gegrabener Wasserkanal' neben
ferken etc. Auf päz. /andan ist gar nichts zu geben,
vergl. päz. /ähUan^ /m u. a. m.
J. V. Fierlinger erklärt KZ. 27, 335 das ap. aw.
kan- gegenüber ai. khan- durch Analogiebildung nach
der schwachen Wurzelstufe, Bartholomae, ib. 367
Anm. 2 durch solche nach den mit Praefixen kon-
sonantischen Auslauts zusammengesetzten Formen.
870. kentz 'Jungfrau, Mädchen', kenizek,
maz. klja (?) ').
aw. kanyä-^ kaini7i-, kainikä- 'Jungfrau, Mädchen';
phlv. kanik, phlv. päz. kaMöak bezw. kanTjak, kanlzak
(PPGL); ai. kanyä-, kanijd-.
Durch dasselbe Suffix weitergebildet wie dösüe,
nrDirn (Is. 23, 4, 12) 'Jungfrau .
871. kiitäh, küteh 'klein, kurz'; ködek 'Kind, Kleines,
Foetus, Embryo (AM.)'.
aw. kutaka- 'klein'; phlv. kütak bezw. kötak,
bei. künd, n. Jcund 'kurz, nahe' (209); afy. LW. (?)
kötah,
np. küiäh entbehrt auflfälliger Weise der Lautver-
schiebung. Für ködek ist eine Grundform *kvataka-
anzusetzen (wie dö aus dva-, tö aus tvam u. a. m.).
Zum Pronominalstamm kva-, kn-?
872. hüze 'Topf.
aw. /awza- *Topf'; arm. LW. kuz.
Da mir Geldner's Übersetzung (vergl. KZ. 25, 583
^) Dazu auch kurd. kic?
```


### [2026-09-06T21:58:05.164Z] TOOL RESULT

```
leaf(0-based) 337 -> approx printed page 644 645
udul-) Arm. (ambig.) ktik-ktik ollam, id. (cf. gudil-); Blg. kátkam ‘fondle’; Li. kutenü, -énti (2) ‘tickle’; Latv. impers. man kut, inf: kutet ‘itch, tickle'
kut- (2) ‘strong; strength'.' See kutor-
kut- (3) 'diminutive'. Variant: kütoko- Av. cf. kutako "little; Per. cf. kütàh ‘short’; kucak “little; küdak ‘boy’. (Li. kūdikis, m. “child” seems to be a Slav. LW. fr. *xud-)
kut- (4) (küta, is) ‘stump’ W cwt, f. and cot, pl. -iau, f. ‘tump, tail’; OCS kyta “arm, shoulder’; Cz. kýta “leg, haunch’; Big. kita ‘penis? '
kut- (5) (kütos, à) ‘tassel, tuft’ Blg. kit ‘tuft of wool, fibre’; OCS cf. kytük
```


## [2026-09-06T21:58:28.058Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma k?e and ===\"; grep -n -i -E 'lemma: k.?[uw]?e-?$|lemma: k.?e' POK_full.txt | head -40\necho \"--- search 'und' enclitic ---\"; grep -n -B2 -A12 'Page(s): 635' POK_full.txt | head -80",
 "description": "Find Pokorny page 635 entry"
}
```


### [2026-09-06T21:58:29.990Z] TOOL RESULT

```
=== POK_full lemma k?e and ===
9334:Root / lemma: ken-2, kens-, keni-, kenu-\ "to rub, scrape off; ashes' must have come from 
31704:Root / lemma: g(e)u-lo- : glowing coals derivded from Root / lemma: ker(9)-3\ to burn 
44482:Root / lemma: ked- 
44506:Root / lemma: keg- keng- and kek-, kenk- 
44557:Root / lemma: keid- 
44575:Root / lemma: keis- 
44587:Root / lemma: keku- 
44602:Root / lemma: keR- 
44616:Root / lemma: kelg- 
44630:Root / lemma: kel-1, kela- 
44697:Root / lemma: kel-2 
44745:Root / lemma: kel-3, kela-, A/a- extended klad- 
44927:Root / lemma: kel-5 
44963:Root / lemma: kel-6, k(e)le-, k(e)la-or 1(1-1 
45077:Root / lemma: kel-7{kol-, kj^ 
45105:Root / lemma: kel-7 
45113:Root / lemma: kelp-, l^lp- 
45133:Root / lemma: kemero- komero-, keinero- 
45157:Root / lemma: kema-, koma-, kma- {* hank-mhnos) 
45161:Root/ lemma: kema-, koma-, kma-{* hank-mh(e)nos)\ piece, derived from Root/ lemma: 
45178:Root / lemma: kem-1 
45224:Root / lemma: kem-2 
45250:Root / lemma: keng-, kenk- 
45254:Root / lemma: kenk-1 
45286:Root / lemma: kenk-2 
45309:Root / lemma: kenk-3 
45331:Root / lemma: ken-1 
45337:Root/ lemma: ken-1 \ "to press, pinch, etc' derived from Root/ lemma: gen-\ "to pinch, 
45431:Root / lemma: ken-2, kena-, keni-, kenu-; 
45687:Root / lemma: ken-3 
45722:Root / lemma: ken-4 
45748:Root / lemma: kenth(o)- 
45766:Root / lemma: kerd-1 
45792:Root / lemma: kerd-2 
45855:Root / lemma: ker(a)-3 
45913:Root / lemma: kerap-, krep- 
45980:Root/ lemma: ker-1, kor-, kr- 
45988:Root / lemma: ker-1, kor-, kr-\ "a kind of sound (hoarse shrieking, etc.), *crane' derived 
46244:Root / lemma: ker-2 
46250:Root / lemma: ker-4 
--- search 'und' enclitic ---
52369-Meaning: a kind of big fish 
52370-See also: see below under (sjk^alo-s. 
52371:Page(s): 635 
52372-
52373-
52374-
52375-Root / lemma: Icas-io-, -lo- {* IC'ehus-lo-) 
52376-
52377-Meaning: basket-work 
52378-
52379-Material: Latin qualum{quallus) 'a wicker basket' ( *kuaslom, compare the diminutive:) 
52380-
52381-quasillus, -um ' a small basket for various purposes; esp., a wool-basket ' (with emphatic - 
52382-
52383-ss-)\ 
--
52391-
52392-References: WP. I 507, Trautmann 119, WH. II 397. 
52393:Page(s): 635 
52394-
52395-
52396-
52397-Root/ lemma: k''as-. k^as- {* k'^ehus-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
52398-
52399-Meaning: to cough 
52400-
52401-Note: [addendum to S. 635] 
52402-
52403-Material: 
52404-
52405-In a- grade: 
--
53125-
53126-References: WP. I 507 f., WH. I 309 f., II 401 f., Schwyzer Gr. Gr. II 573 ff., 6482 f. 
53127:Page(s): 635-636 
53128-
53129-Root / lemma: Iced- k^od-i^k^ehutt-) 
53130-
53131-Meaning: to prick; to drill, sharpen 
53132-
53133-Note: (older keued-1) 
53134-
53135-Material: Old Icelandic ^i/a/r'quick, fast, gamy, sharp', hvQt\. ' Anreizung ', hvata, -ada^ 
53136-
53137-set in motion, hasten ', Old English /7M/^/"quick, fast, gamy'. Old Saxon hwatds.. Old High 
53138-
53139-
```


## [2026-09-06T21:58:30.801Z] TOOL CALL #11: Bash

```json
{
 "command": "pdftoppm -f 288 -l 288 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg288 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render pdf page 288"
}
```


### [2026-09-06T21:58:32.924Z] TOOL RESULT

```
total 36228
drwx------ 3 sfmqrb sfmqrb    4096 Sep  6 17:58 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     616 Sep  6 17:57 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb  541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb  729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb   97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb 2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   31044 Sep  6 17:50 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   18004 Sep  6 17:56 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb   41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb   46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb   16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb 8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb   25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb  105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb  130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 17:57 p284
-rw-rw-r-- 1 sfmqrb sfmqrb   43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  106502 Sep  6 17:48 p284_e2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb  122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb  144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb  106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69883 Sep  6 17:52 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53847 Sep  6 17:58 pg288.png
```


## [2026-09-06T21:58:39.161Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '53060,53128p' POK_full.txt",
 "description": "Read POK entry ending p.635-636"
}
```


### [2026-09-06T21:58:39.211Z] TOOL RESULT

```
References: WP. I 512, Trautmann 131 f., Schwyzer Gr. Gr. I 351 f., 589 f., WH. II 394, 
400 f., F. Sommer Zum Zahlwort, 27. 
Page(s): 643-644 

Root / lemma: Ice 1 {*k''ehu-) 

Meaning: and (end.) 

Note: from '* anyhow, somehow ', as also to Pron.-stem k^o-, k^e-oi interrogative and 

indefinite standing in same relationship, as *^e"here' to Ro-, ke-^\h\s\ With it identically 

k"e behind forms of interrogative - indefinite -stem to the strengthening of the indefinite 

mode. 

Material: Old Indie ca, Avestan ca, ap. da enclitic "and"; Lydian -/r'and'; gr. te 'and'; venet. 

-ke, lepont. -pe, piken. -p, Latin -que; ne-que= Oscan-Umbrian nep, neip^ not; and not, 

nor; rarely not even ' = Old Irish na-ch, mcymr. etc. /7ac"not' (to afrom esee below ne 

"not'), compare Latin atque^an6 in addition' {ad+ que) = Umbrian ap{e) " in which place, in 

what place, where, with, together with, in the company of, in connection with, along with, 

together, and '; Gothic n/-h {etc., see below ne) "not'; (see also Old High German etc. noh 



under */w/" but, well, now that '); Bulgarian ce' but, and, that, because ', Czech old a-ce, 

ac'W, poln. acz^ even though, although '; 

Maybe alb. Geg nuk, Tosc nuku' not ' : mcymr. etc. nac'noV. 

Maybe alb. ne se' if not', se' that'. 

the indefinite mode, mind intensifying e.g. Old Indie kas-ca, Avestan c/s-ca' wer irgend, 
welcher irgend ', in relative clause with Rel.-Pron. ya-; Avestan c/s-ca a\so " whoever it be, 
whatever, each, each one, every, everybody, every one, everything '; 

Armenian -k'e.g. o-k" whoever' (if drop of efrom */r"'e before the palatalization; with k' 
of equated with the plural); 

gr. 6a-T£ (here behind the relative; s. Schwyzer Gr. Gr. II 575 f.); 

Latin quom-que, cunque, Umbrian yC>^/r7yC>e originally '* with, together with, in the 
company of, in connection with, along with, together, and ', then with coloring of time mode 
(as in Modern High German M/e/'//77/77e/' "whoever') just generalizing, e.g. quTcumque, 
Umbrian pisipumpe 6s.\ quisque {ixom *qurqu/sque:0\d \nd'\c yah kas-ca) in sentences of 
relativen mode, (7i//S(7^e (mostly against) ' whoever it be, whatever, each, each one, every, 
everybody, every one, everything '; 

Gothic -/7, -u-h'\n fvaz-u-h, fvo-h, fva-h^ whoever it be, whatever, each, each one, 
every, everybody, every one, everything '; 

Hittite ku-is-ki{= Latin quis-que) = Lycian tf-ke; ni-ik-ku{: Latin ne-que) = Lydian n/-k. 

In similar meaning also other forms from of the stems k"'o-, k"a, k"i-. Latin quis-quam. 
Old Indie cit{cid), Avestan cil, ap. c/y generalization particle (z. B. Old Indie kas-cid^ any 
one, anybody, anything, some one, somebody, something ') = Indo Germanic *k"id\v\ 
Oscan -pfd, -pid, Umbrian -pe, -pe/{e.g. Oscan puturus-pfd^ which of both ', Umbrian 
putres-pe^ which of both ') = Armenian -c{/n-c' something '); s. also *k"ene. 

References: WP. I 507 f., WH. I 309 f., II 401 f., Schwyzer Gr. Gr. II 573 ff., 6482 f. 
Page(s): 635-636
```


## [2026-09-06T21:58:46.324Z] TOOL CALL #13: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg288.png"
}
```


### [2026-09-06T21:58:46.710Z] TOOL RESULT

```

```


## [2026-09-06T21:58:46.708Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T21:59:01.845Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('sesqui-,  combining')\nleaf=t[:i].count('\\f')\nprint(\"KLN sesqui leaf\",leaf,\"approx printed p\", (leaf-12)*2, (leaf-12)*2+1)\nEOF\necho \"=== IEC leaf 337 page numbers ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==338' IEC.txt | head -5\nawk 'BEGIN{RS=\"\\f\"} NR==338' IEC.txt | tail -5\necho \"=== IEC leaf 330 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==331' IEC.txt | head -3",
 "description": "Locate KLN sesqui page and IEC page numbering"
}
```


## [2026-09-06T21:59:02.916Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v3 کوتاه ===\"; grep -n 'کوتاه' incoming/BQT/BQT_v3_pages.txt | head -20\necho \"=== BQT v3 کودک ===\"; grep -n 'کودک' incoming/BQT/BQT_v3_pages.txt | head -20",
 "description": "Grep BQT v3 for kutah/kudak"
}
```


### [2026-09-06T21:59:03.904Z] TOOL RESULT

```
KLN sesqui leaf 757 approx printed p 1490 1491
=== IEC leaf 337 page numbers ===
type *kusdhero-, *kusdhro- in Skt. küharah, m. ‘hole, cave’; W cwthr ‘vulva, anus’
(kusimno-, see kusKimno- (kuKsimno-))
kusio 'tug, drag, strain, tease, incite' Skt. kusami, kugnami, pp. kusitah “pinch; téar; Av. kuš- *téar; kil; Per. kusam, -1idan ‘strive’; Gk. kunéo, fut. küssó & kuüso (2) 'im-
kurn- — kut-
10
kut- (8) ‘grain, kernel, nut? (?) Arm. (ambig.) kut, gs kto, o-st ‘grain, kernel; OHG hodo ‘testicle’; Lat. cf. cutio, -onis, m. *woodlouse'
kutokos, see kut- (3)
kutor-, kutno- 'strength; strong'. Cf. WP II, 601 Hitt. kutar, ds kutani (-tt-) ‘strength’; Arm. cf. ktrič ‘brave’; Li. kutrüs ‘vigorous, active’; kùtinu, -inti, v. ‘strengthen’ beside kuntu, pf. kutau, inf. kusti “recover”
kūturið ‘dawdle’ SWG haudern, id.; Li. kūturióti, id.; Latv. cf. kūtrs, adj. ‘sluggish’. Uncertainly Arm. kkrim, v. (1) wait", if for *kutur-). O-gde in Latv. kau- tra (2) ‘hesitancy’
küuo, io, eio “move, stir, sway’ (tr. & intr.). Cf. WP I, 376 and kieuuo MHG cf. hüwe, wm. ‘onset, rush"; W cf. ciw, adj. (smart, clever. Ambig.); OCS kyvajo, ati (w. instr. "move Pol. kiwać ‘wag, wave’; Cz. kyvu, kyvat ‘move, nod'; short-gde (*-u-) in OCS kvajo, kvati *wag'; Latv. küveju
=== IEC leaf 330 head ===
ow’; Gk. cf. küttaros *cell, hold, urn, pod, arch'; OE hüdern 'store- house
kudhos, io (kudh-) 'hiding; hiding-place, hollow, receptacle'. Cf. kudhoros Skt. kuhah “cheat? beside kuharah “cave, hol- low’; Gk. cf. lë-kuthos, Dor. là-, f. “oil-jar”, cf. lekuthízo ‘declaim in a hollow voice": W cwdd, m. ‘cavity, shelter; Br. küz 'hiding- place’; OHG hutta, huttea (hut, whence LWs in Du. Eng. hut, Fr. hutte); SWG Hutte *wil- low-basket'; Hotte ("back-basket', whence Fr. LW hotte); MDu. hodde "basket": EME hod *mortar-trough, hod”; Sw. hydda ‘hut’; long- gde in OE hydan, G hüten (OE: ‘hide’; G *protect")
küg- ‘cackle, guffaw’ Cz. kyhat, kyhnout, inf. ‘squawk, cackle’; OE cf. (*-ü-) hocor, n. ‘mockery’; LG huchein
```


### [2026-09-06T21:59:03.961Z] TOOL RESULT

```
=== BQT v3 کوتاه ===
91:کوتاه نگارنده باروپا وامریکا, ‎plas gat‏ چایی مجلد جاضر را از ‎date‏ ۱۹۸۳ ۱۷۲۲۱ صحیح
784:‎asl‏ طنبور بزرکی که دستهٌ کوتاهی‌داشته ‎ash‏
3908:دار بروزن ‎Lele GEL‏ یشواز آستین کوتاه
14886:را کوبند که قد کوتاهی داشته باشد و باین ‎ME‏ » بنم اول وفتح ثالی . جستنکلو
14904:‏۴ - « غك بالضم . کوتاه فربه , و بسن یکویند کس ی که مپرهای پشتتن بیرون‌آمده باشد
15917:سرچوب کوتاه تیزمیباشدو آنرا دسته چلك‌وچاليك
26458:و کوتاه گردیده باشد .
28356:‎yey‏ از کوسفند است که دست و پای او کوتاه
33678:چیز کوتاه وشخص کوتاه قد) «فرهنگه نظام» « درشیرازی و کازرونی 601( کوناه ) ,601 ‎dom‏
34317:و دام و فیره ‎٩‏ - و هر چیز ناقص و کوتاه ۳"
34339:بمعنی کوتاه استممال کنند : ممانی کلته همچون رش ‎ENN‏ « رشیدی ».
35028:چیز کوناه وناقص را گوبند ‎A‏ عموماً وآدم کوتاه
35488:‏کوتاه میباشد باندام کاسه پشت و ‎NAST‏ سفال
37478:‏وچوبدستیرا‎ - Paiste ‏کوتاه که مسافران باخود‎
37786:کوتاه ‎VY‏ - جانوری است سا
37790:‏آمده است باآنکه دست خ کوش کوتاه است له
37795:کویند که بیارکوتاه قد باشد .
37797:کوتاه ‎are‏ را کرنند که
37832:‏۴ رك : کوتاه با , کوته یاچه .
37845:۲ ولی این کلمه از هندی بتر کی رفته است . ۱ - رك : کوتاه با ء کوتله باچه.
=== BQT v3 کودک ===
2148:را بکشند وبرزها رکودکان
3998:که کودکاتر| ‎pe‏ میرسد و آنرا بعربی جدری
8862:‏خشك کرده بسورت کرد در آورده باشند و برای تغذية کودکان بکار رود .
12244:‏کودکان سازند» اطلاق شود .
13068:کودکان بررشته کشند نا در خواب ترسند ‎٩‏ -
14468:وآن‌کوه ‎bh‏ نرمی باشد که کودکان و جوانان
15129:کودکان پول در ‎OT‏ ریزند و جمم کنند , اطلاق شود . قس : قله (سبوی بز رکه ) , غله( کوزء
25809:‎OT‏ آویزند و زنان و کودکان برآن نشینند ودر
26708:۱ - بکاو ‎tte‏ دل را زغیر ‎OS gle‏ ز لهو ولمب چه بازی چ و کودکانک کاو.
28838:است که برای دفع چشم زخم ‎GL‏ سور بندند و در «نظرقربانی» کودکان گذارند ودرزمان ما
28939:۱ -«کخ صورتی باشد زشت که کودکان را بدان ترسانند . فرخی (سیستالی) گوید:
38148:کوتاء بقدر يك قبضه که کودکان و جوانان در
38911:‏همچو کاندر خواب دارد کودکان راکو کنار
41122:‏۵ - 3 : قاقا (در زبان کودکان) :
```


## [2026-09-06T21:59:16.018Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in range(750,762):\n    L=leaves[n]\n    nums=re.findall(r'\\b1[34]\\d\\d\\b',L[:300]+L[-300:])\n    print(n, nums, repr(L[:80]))\nEOF",
 "description": "Find printed page numbers in KLN near sesqui"
}
```


### [2026-09-06T21:59:17.914Z] TOOL RESULT

```
750 [] "hol,  n.,  name  of  the  Heb. -Aram,  vowel  sign  ’.' —  Aram.  s(ghbl,  lit. "
751 [] ' asXrjvT],  ‘moon’,  rel.  to  osX aq,  ‘light,  brightness, flame’,  fr.  *afcX'
752 [] '  Biblical  Heb.  samakh,  of s.m.),  used  elliptically  for  samakh  eth  yada'
753 [] 'ion  of  seven  see  prec.  word.\nseiior,  n.,  a  Spanish  title  corresponding'
754 [] 'e next  word  and  cp.  sepia.\nsepsis,  n.,  putrefaction.  —  Medical  L.,  fr.'
755 [] 'no,  ‘coin’, dimin.  formed  fr.  zecca,  ‘a  mint’,  fr.  Arab. sikkah,  ‘a  di'
756 [] 'net,  sermonette  (qq.  v.),  sermonettino (q.v.),  sermon-ic,  sermon-ic-al,  a'
757 [] '  shape’.  See  prec.  word  and  suff.  -oid. Derivative:  sesamoid-al,  adj.\nS'
758 [] 'verus.  See  severe and  -ity.\nSeville  orange,  also  Seville,  n.  —  Named  f'
759 [] 'darkness’,  Olr.  scath,  OW.  scod, Bret,  squeut,  ‘darkness’.  Cp.  shadow  a'
760 [] 'n.  F.  chantier,  ‘workshop’, fr.  F.  chantier,  ‘timberyard’,  fr.  L.  canth'
761 [] 'cepter’,  and  to  Heb. shebhet,  Tod,  staff,  club,  scepter’,  Aram,  shibhtd'
```


## [2026-09-06T21:59:30.034Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '218990,219035p' KLN_1971.txt\necho \"=== page marks in KLN_1971 near there ===\"\nawk 'NR>218800 && NR<219200 && /^[0-9]{3,4}$/ {print NR\": \"$0}' KLN_1971.txt | head -20\necho \"=== leaves ===\"; python3 -c \"\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\ni=t.find('sesqui-, combining')\nprint('leaf',t[:i].count('\\f'), 'total', t.count('\\f'))\nt2=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nprint('1966 total leaves', t2.count('\\f'))\n\"",
 "description": "Check KLN_1971 page marks"
}
```


### [2026-09-06T21:59:31.980Z] TOOL RESULT

```
Greek. See Michael Ventris and John Chad- 
wick, Documents in Mycenaean Greek (Cam- 
bridge University Press), Index, s.v. Semitic 
Loanwords. Cp. the words chiton, chrysalis , 
cumin. 

sesamoid, adj. and n. — Lit. ‘shaped like a ses- 
ame seed’, fr. Gk. a7]aapt.oet.$7)<; f ‘like sesame 
or sesame seed’, which is compounded of crijaot- 
ptov, ‘sesame’, and -oei&fc, ‘like’, fr. elSos, 
‘form, shape’. See prec. word and suff. -oid. 
Derivative: sesamoid-al , adj. 

Sesban, n. — The same as Sesbania. 

Sesbania, n., a genus of plants of the pea family 
{bot.) — ModL., fr. Arab, saysaban , fr. Pers. 
sisaban. For the ending see 1st suff. -ia. 

Sesia, n., a genus of moths {zool) — ModL., fr. 
Gk. <n?)<;, ‘moth’, which is of Semitic origin. 
Cp. Heb. sds, Aram, sasa, Arab, sus, susa h , 
Ethiop. fade. Akkad, sasu , ‘moth’. For the 
ending see 1 st suff. -ia. 

sesqui-, combining form meaning ‘one half more*. 
— L., contraction of *sem{i)sque , ‘and a half 
(more)’, fr. semi-, ‘half’ (see semi-), and - que , 
‘and’, which is cogn. with 01., Avestic ca, 
OPers. ca, Gk. rs, Phryg. xe, Goth -h, Bulg. 

OIr. - ch , ‘and’. 

sesquicentennial, adj., pertaining to a century 
and a half; n., the one hundred and fiftieth an- 
niversary. — Compounded of sesqui- and cen- 
tennial. 

sesquipedalian, adj., a foot and a half long. — 
Formed with suff. -ian fr. L. sesquipedalis , 
which is compounded of sesqui- and pedalis , 
‘pertaining to the foot’. See pedal, adj. 
sessile, adj., attached directly to the main stem 
(bot.) — L. sessilis , ‘pertaining to sitting, for 
sitting’, fr. sess-(um), pp. stem of sedere, ‘to sit*. 
See sedentary and -ile. 
=== page marks in KLN_1971 near there ===
=== leaves ===
leaf 0 total 0
1966 total leaves 902
```


## [2026-09-06T21:59:43.494Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (722,723,724,725,726):\n    print('---leaf',n, repr(leaves[n][:150]))\nEOF",
 "description": "Check KLN leaf 724 content"
}
```


### [2026-09-06T21:59:45.301Z] TOOL RESULT

```
---leaf 722 'aceae.\n|\n•t\nA\nA\n4\nrosacean,  adj.,  rosaceous.  —  See  next  word  and -an.\nrosaceous,  adj.  —  L.  rosaceus,  ‘of  roses’,  fr.  rosa. See  rose  a'
---leaf 723 ' rumpere,  ‘to  break’.  See  route  and  cp.  rut, ‘routine’.  For  sense  development  cp.  F.  routine, ‘practice,  routine’,  fr.  route,  ‘way’  '
---leaf 724 'en;  prob.  a  blend  of  rover,  ‘sea robber’,  and  ON.  rafa,  rapa,  ‘to  wander’.  The orig.  meaning  of  rove  was  ‘to  wander  about robbing’'
---leaf 725 '  to  read,  ‘red’.  See  red  and  cp. rudd,  the  fish,  ruddle,  ruddock,  ruddy.\nRudbeckia,  n.,  a  genus  of  plants  of  the  aster  fam¬ ily  '
---leaf 726 'he cud’,  fr.  ruminatus,  pp.  of  ruminari.  See  prec. word  and  -ion.\nruminator,  n.,  a  person  who  ruminates.  —  L. ruminator,  ‘one  that  '
```


## [2026-09-06T22:00:10.074Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\ngrep -ho '\"ref\": \"KLN:1[0-9]\\{3\\}\"' page-2*.json | sort -u | head -30",
 "description": "Look at prior KLN refs"
}
```


### [2026-09-06T22:00:10.125Z] TOOL RESULT

```
"ref": "KLN:1007"
"ref": "KLN:1068"
"ref": "KLN:1110"
"ref": "KLN:1288"
"ref": "KLN:1305"
"ref": "KLN:1370"
"ref": "KLN:1380"
"ref": "KLN:1386"
"ref": "KLN:1411"
"ref": "KLN:1422"
"ref": "KLN:1456"
"ref": "KLN:1539"
"ref": "KLN:1554"
"ref": "KLN:1664"
"ref": "KLN:1743"
"ref": "KLN:1757"
"ref": "KLN:1758"
"ref": "KLN:1766"
```


## [2026-09-06T22:00:13.080Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\ngrep -h -A3 '\"ref\": \"KLN:1422\"' page-2*.json | head -8\necho ---\ngrep -h -A3 '\"ref\": \"KLN:1456\"' page-2*.json | head -8\necho ---\ngrep -h -A3 '\"ref\": \"KLN:1411\"' page-2*.json | head -8",
 "description": "Inspect prior KLN ref notes"
}
```


### [2026-09-06T22:00:13.160Z] TOOL RESULT

```
       "ref": "KLN:1422",
       "status": "supports",
       "note": "Klein 1966, the leaf whose printed page number is 1422 (KLN_1966.txt leaf 755): 'serene, adj., clear, bright; calm. — L. serenus, „clear, fair, cloudless, serene‘, of uncertain origin. It possibly stands for *kseresnos and is cogn. with Gk. ξηρός, „dry‘, OI. kṣāráḥ ... OHG. serawen, „to become dry‘. Cp. elixir, xerasia, xero-.' Nourai's page number is exact; note Klein's hedge 'of uncertain origin ... possibly'."
      }
---
              "ref": "KLN:1456",
              "status": "supports",
              "note": "Klein s.v. slave (KLN_1966.txt l. 35506-7): 'OSlav. slovo, \"word\", fr. I.-E. base *kleu-, \"to hear\", whence also OI. śravas-, \"praise, glory\", Avestic sravah-, \"word\", Gk. kléos, \"fame\", L. cluere, \"to hear\", OE. hlūd, \"loud\".' Nourai's Avestan gloss 'word, speech' is Klein's."
            },
--
              "ref": "KLN:1456",
              "status": "supports",
              "note": "Klein s.v. slave (KLN_1966.txt l. 35506-7, printed p.1456): 'OSlav. Slověninŭ is a derivative of OSlav. slovo, \"word\", fr. I.-E. base *kleu-, \"to hear\" ... Accordingly the name Slav lit. means \"speaker\". For sense development cp. Church Slavic Němьci, \"Germans\", which is rel. to němъ, \"dumb\".' Nourai has transcribed Klein's page verbatim, including the ě of Slověninŭ."
---
       "ref": "KLN:1411",
       "status": "supports",
       "note": "Klein 1966 p. 1410-1411 (KLN_1966.txt leaf 749, page numeral 1410 visible on the leaf): 'seersucker, n., a kind of cotton fabric. — Hind. sirsakar, fr. Pers. shir-o-shakar, lit. „milk and sugar“.' Nourai's page number is exact."
      },
```


## [2026-09-06T22:00:28.933Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(\"total leaves\",len(leaves))\nfor n in range(333,342):\n    L=leaves[n]\n    print('---',n, repr(L[:60]), '||', repr(L[-60:]))\nEOF",
 "description": "Inspect IEC leaves around kut-"
}
```


### [2026-09-06T22:00:30.528Z] TOOL RESULT

```
total leaves 858
--- 333 ' ‘gusset’. (OCS kyla ‘hernia’ appears to be long zero-gde of' || 'ump, crook’. Cf. WP I, 350, 373 & 376. (Cf. kumb- with some '
--- 334 'ambiguity in the Celtic forms) Skt. kumpah, adj. ‘with arm c' || 'ff “bully, brawl, threaten, din, swagger’; Pol. kpac “bully�'
--- 335 '��; kpic ‘make a fool of": Ukr. kpyty ‘jeer at\nküpió (2) ‘su' || ' ‘revolving notice-board’; OCS *krügü beside korgü ‘prow’; R'
--- 336 ' korgà (“bent old woman’. Also ‘reef, sandbank’. Cf. krgos);' || 'ON hodd, f. as Go., beside MHG hürten, v. ‘hoard’. Extn. of '
--- 337 'type *kusdhero-, *kusdhro- in Skt. küharah, m. ‘hole, cave’;' || "d'; short-gde (*-u-) in OCS kvajo, kvati *wag'; Latv. küveju"
--- 338 ', et ‘frolic, fool about’; küve, f. ‘frolic’. (Variant of ty' || '3pl pf. mp. ‘retreat, escape’; Lat. cado, Gre, pf: cecídi (f'
--- 339 'all, sink, fail’; cf. caries (decay: Skt. Sadah “fall, shedd' || 'piercing"; theksi ‘thrill, shriek’; Galio-Lat. cattus ‘tomca'
--- 340 't’; MIr. catt, W cath (Ir. m., W f. *cat). (For Latv. sakts,' || 't in wood’; R suk ‘branch, knot in wood’\nkāp- ‘flow, gush, h'
--- 341 'iss, fume, rage’ Skt. sapami ‘revile beside Vedic śāpah “flo' || ' forms ambig. cf. Kot-) Skt. cf. sátruh ‘enemy’; Oss. cf. sá'
```


## [2026-09-06T22:00:37.725Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in range(300,360):\n    L=leaves[n]\n    m=re.findall(r'^\\s*(\\d{3,4})\\s*$', L, re.M)\n    h=[l for l in L.split('\\n') if '—' in l and len(l)<40]\n    if m or h: print(n, m, h[:2])\nEOF",
 "description": "Find IEC page numerals"
}
```


### [2026-09-06T22:00:39.680Z] TOOL RESULT

```
300 ['526'] ['kokos, à — koleió']
301 ['327', '528'] ['kolg- — komolos (komol-)']
302 ['329', '530'] ['koməros — konsos']
303 ['531', '532'] ['kont- — koquios, io (koquius)']
304 ['533', '534'] ['koquiubhos, à — korio (koreio)']
305 ['535', '536'] ['korió — korsos']
306 ['537', '538'] ['korst- — koso, ió']
307 ['539', '540'] ['kostos, a, is — krab-']
308 ['541'] []
309 ['542', '543'] ['krad- (kradaio) — kraks-']
310 ['544', '545'] ['kram- — krauk-']
311 ['546', '547'] ['kraupio — kreko, ið']
312 ['548', '549'] ['krekos — krep-']
313 ['550', '351'] ['krequ- — kreut-']
314 ['532'] ['kreunt- — krikətos (krikit-)']
315 ['553', '554'] ['krikstio — kritrom']
316 ['335', '556'] ['kritsió — krokió']
317 ['337', '558'] ['kroK- — krous-']
318 ['339', '560'] ['krous- — krunk-']
319 ['561', '562'] ['krunk- — kruunt-']
320 ['563', '564'] ['kruuos — krkos']
321 ['565', '566'] ['krks- — krp-']
322 ['567'] []
323 ['568', '569'] ['krpàn- (krpon-) — krt-']
324 ['570', '511'] ['krtəlos, ios (krtilo-) — kseluos']
325 ['572', '573'] ['ksengið (skeng-, skng-) — kseubh-']
326 ['574'] ['kseul- (kseuel-) — ksnt-']
327 ['575', '576'] ['ksol- — ksül-']
328 ['578'] ['ksün- (skün-) — kublos, om']
329 ['379', '580'] ['kúbo — kiig-']
330 ['581', '582'] []
331 ['583', '584'] ['kūku- — kuləĝos, om (kulĝ-)']
332 ['585', '586'] ['kulik- — küm-']
333 ['587', '588'] ['kumbolos, à, ios — kunkos, à, io']
334 ['589', '590'] ['künos — kur-']
335 ['591'] []
336 ['392', '593'] ['kür- — kurn-']
337 ['594', '595'] ['kurn- — kut-']
338 ['596'] ['kut- — kuoit- (kuoitio, kuoitaio)']
339 ['598', '599'] ['kuókuo (kuuokuuo) — Kak-, Kakt-']
340 ['600', '601'] ['Kak- — Kan-']
341 ['602', '603'] []
342 ['604', '605'] ['Katoros, is — Káuos (Kouos, Kauos), à']
343 ['606'] ['Ke (Kə, k) — Keiaros']
344 ['607', '608'] ['Keiota (Keit-) — Kensos, à, us']
345 ['610'] ['Kent- — Kerdhos, à']
346 ['611', '612'] ['Kerod- — kernt-']
347 ['613', '614'] ['Keros, om, à — Kestros, om']
348 ['615', '616'] ['kët- — Kouó, ið']
349 ['617', '618'] ['Ki- — Kiros']
350 ['619', '620'] ['Kirs- — Kīuos (Kieuos)']
351 ['621', '622'] ['Kia, Kio — Klamo (Klamaio)']
352 ['623'] []
353 ['624', '625'] []
354 ['626', '627'] []
355 ['628', '629'] []
356 ['630', '631'] ['Klüsos, us — Kltos']
357 ['632', '633'] ['Kms, -Kms — Koinos, om, à, io']
358 ['634', '635'] ['Koipos — Kómos, Komn-']
359 ['636', '637'] ['Kónos, ios — Koruos, à']
```


## [2026-09-06T22:00:50.072Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(\"leaves\",len(leaves))\nfor i,L in enumerate(leaves):\n    if 'کوتاه' in L or 'کودک' in L:\n        tag=re.search(r'\\[pdf page (\\d+)\\]',L)\n        pass\n# find pdf pages 505-525\nfor i,L in enumerate(leaves):\n    m=re.search(r'\\[pdf page (\\d+)\\]',L)\n    if m and 505<=int(m.group(1))<=520:\n        print('=== leaf',i,'pdf',m.group(1))\n        print(L[:600].replace('\\n',' | ')[:600])\nEOF",
 "description": "Inspect BQT v3 pages around 1721"
}
```


### [2026-09-06T22:00:51.791Z] TOOL RESULT

```
leaves 721
=== leaf 504 pdf 505
[pdf page 505] | oc | ‏بروزن و معنی کنگاج‎ oath ‏که شین قطمدار‎ | ‏است که صلاح و مصلحت ومشورت باشد ؛ وباین‎ | weal ‏معنی با سین بی‌قطه و فتح اولهم آمده‎ | ‏و خرچنگه را یز گوبند که سرطان باشد.‎ |  | 1 ‏بنتح اول بر وزن بنگاله‎ - CLES | ‏بمعنی کنفاله است که خواستن و خواستگاری‎ | ۱ ‏وممك وبخیل‎ dandy ‏کردن - وزن فاحشه‎ | . ‏وتام کوهی باشد از خراسان‎ - |  | کفگر ۳ ‎the‏ اول ‎GB,‏ فاسی‌وسکون | تانی ورای قرشت . رستنیی باشد ممروف و ‎OT‏ | ‏بیشتر در کوهستان ‎ny)‏ و ‎LT‏ های بر که آن | خار ‎db‏ میباشد و آئرا پزند و با ماست خورنه |  | قوت ‎ck‏ دهد و عرق را خوشبوی کند و بعربی | آنرا حرشف وجناح‌الییش‌خوانن
=== leaf 505 pdf 506
[pdf page 506] | ۱۷۱۳ | زای تقظه‌دار وسکون دال بی‌قطه « سمغ ‎SST‏ | ‏است و آلراکنگری هم میگویند . خوردن آن | ‎J gel‏ وامتفراغ‌آورد و بعربی صمغ‌الحرشف | وتراب‌القی خوانند . | کنگر کیریا ‎ee‏ اول و ‎tt‏ |  | oly ‏جبرءت است از‎ alg ‏کنابه از‎ » GELS, |  | [ws |  | ‎AS‏ کندن © ‎pte‏ اول وثالك وکاف» | کنابه ازکار بی منفعت بسیار مشقت بی‌ماحصل | ‎Ty‏ وتعب کردن باشد . |  | ‏کنبگره یکی اول و ثالث بمعنی |  | ‏مردم_ هندوستان | نوازند وآن ‎er‏ | ‏است که‌بر آن‌دوتار | فولادی کشیده‌اند و بر زیر هردوسرآن چوب دو | کدو اصب کرد‌اند ۴ - و بضم اول و ‎NG‏ | ‏بلندیهای هرچیز ‎aa Ty‏ عموماً وآنچه بر سر | دبوار حمار و
=== leaf 506 pdf 507
[pdf page 507] | کفته اید . |  | کنور © بفتح اول پروزن تنور. ظرفیرا | گوین دکه ‎asl‏ خم بزرکی از کل ساخته که | غله درآن‌کنند ۱ - ویمعنی مکی وفریب ومردم | بازی دادن هم‌آمده است ۳ - وباین معنی : | پکسي اول هم هست - و بضم اول ‎gam,‏ رعد | برادر برق باشد ۴ - و ‎nh‏ معنی بفتج اول نیز | آمده است . |  | کنوده ۴ ‎JIG‏ وضم ثالی وفتح | رای قرشت » بمعنی فی‌ببنده و مردم بازی دهنده | ‎ath‏ ؛ و باین معنی بفتح اول هم‌آمده است. |  | کنور یدن ه = پفتح اول وکر اول | هردوآمده است | بمعتی‌آدم بازی دادن وفربفتن | مردم . | کنوده © بفتح اول و زای نقطمدار . | ‎de‏ برزده و حلاج ی کرده را گوید ‎٩‏ ؛ و بنم | اول و کر او
=== leaf 507 pdf 508
[pdf page 508] | ‎x ۷۷۵7‏ ۳ | هم‌آمده است ؛ وباین ‎em‏ اول‌هم کفته‌اند. |  | ‏کنیسه ۳ - بکر اول و ثالی بتستانی | رسیده و فتح سن بی ‎abet‏ , معبد ‎ApS‏ را | کون . |  | ‏گنیش؟ = ‎bee‏ ول و ثالی ‎glut‏ | ‏کشیده و بشن اقطه‌دار زده 6 بمعتی کردار است | خواء نيك باشد و خواه کردار بد (۱) |  | ‏بهم تبدیل مییابند ۱ - و نم اول وفتح تحتالیء | در عربی نامیرا گوبند که در اول آن اب یا ام | باشد همچو ابوالمعانی وام‌کلتوم . |  | ‏کنیز ه بفتح اول بروزن تمیز» معروف | است که پرستار و ‎Kies‏ زنان باشد و بعربی | جاربه خوانند ۴ - و دخثر بکر دوشیزه را نیز | ‎aT‏ - و بمعنی بن و بخ خوشة خرما ورطب |  | ‏بیان بیست*و یکم 
=== leaf 508 pdf 509
[pdf page 509] | کواده مکی |  | بمعنی اول کواده است که چوب آستان در خانه | باشد ؛ و بفتح اول هم آمده است . | کوادون ‎A‏ - بنم‌اولبروزن همایون, | ‎gle‏ است باخار شکه پوست بدن رادرثت گرداند؛ | ‎otk‏ ممنی با کاف فارسی هم‌آمده است . | کواده ۰ ‎Jol che‏ بروزن‌شراره « | بمعتی اول کوار است که سبدی باشد که میوه | و یره درآن‌کنند و برستور ‎gk‏ کرده از جایی | بجایی برئد و بمربی دوخله .کوبند *9- و خالةً | زلبور را نیز ‎Malad”‏ و ابری که درشبهای | تابتان برروی هوا بدیدآبد۴٩-‏ و ‎(Dp desea‏ | هم بنظرآمده است وآن بخاری باشد تیره وفلیظط | ملاصق زمین - و بم اول ظرف سفالین را | کوند ۱۴ و خزف را هم میگویند و به
=== leaf 509 pdf 510
[pdf page 510] | ۱۷۲۱۷ | ٩ ‏است‎ Kz se ‏خزفپا پوست‎ |  | lee ‏دان ۳ + با واو پروزن‎ ol | ‏وامثال‎ Fy ‏کشان . شخصیرا گوبند که کوسفتد‎ | ‏آن را بچرالیدن برد و پمربی او را سراج‎ | aan | Ss. ‏اول بروزن نماز‎ che ‏کواد‎ | ‏وآن‌کوزه‌ای باشد سر تنگه و کردن‎ WL, | ‏وچوبدستیرا‎ - Paiste ‏کوتاه که مسافران باخود‎ | . ۴ ‏نیز گویند که خر وکاو بدان رانند‎ |  | کواژ * = بنتح اود و سکون ‎Fl‏ | ‏که زای فارسی‌باشد ۰ طعته وسرزش راکوبند. |  | ‎Od! rs‏ = بنتح اولبروژن ملازه.بسنی | اول کواز است که تنکه مسافران باشد" - ‎poe‏ | ‏اول تخم مرغ نیم پخته را کویند و معرب آن | جوازق است ۷ - و بکسر اول چوبی که‌خروکاو | ‎ole‏
=== leaf 510 pdf 511
[pdf page 511] | کواشمه ۱ - بنم اول و فتح میم . | پمعنی کواسمه است که سهل و آسان ‎ath‏ - | و بمعنی آسانی هم هت که در مقابل دشواری | ‎cal‏ . |  | ‎AS‏ - بر وزن و معنی کوامه | است که صفت و کونه - وطرز وروش باشد . |  | ‏کواشیر ف = بفتح اول بروزن‌طباشیر» | نام جابی است که فیروزة کم رنگه و کم قیمت | از آ تجا آورند ؛ و با کاف فلوسی ‎ju‏ آمده است. |  | ‏ک و اشیهه ۴ ه بروزن وممنی تواسیمه | است که سهل وآمان وآمانی باشد . |  | ‏کوال ° بفتح اول بر وزن ‎«Shs‏ | ‏بمعتی اندوختن و جمع کردن باشد - و بمعتی | ‎gai‏ و بالیدن و افزایش کشت و.زراعت نیز آعده | است ؛ و ضم اول هم درست است . |  | ‏کوال غفچه = بمنی کولن
=== leaf 511 pdf 512
[pdf page 512] | ۱۱4 کویله |  | ‎GT‏ با بای فارسی بر وزن توب + کو بل - با بای ایجد بر وزن فوفل |  | ‏بسعنی کوه باشد که‌عربان جبل کوبند ۱ -ربلفت | کلی است که آنرا اکحوانکویند و معرب‌آن |  | ‏زند وپازند هم کوء را کوپ خوانند ۱ - ویر اقحوان است ۲ . |  | ‏کنده را نیز گوبند ۳ . ‎LT‏ - با بای فارسی بر وزن فوفل + | کوپاره ۴ - بابای فارسی بر وزث شکوفه و بهار درخت راکوبند ۷ . |  | ‏جوباره , کله و رمةٌ خر وکاو و کوسفند و سلیس کوبله ۸ ‎pa‏ اود و فتح بای ‎um!‏ |  | ‏حیوانات را گویند . و لام 6 موی سر و کل سرآدمی باشد ؛ ویفتجاول | کوپال ‎bo‏ بای فارسی بروزن ‎hoy‏ | بروزن حوصله هم‌آمده است ‎٩‏ . |  | ‏عمود و 
=== leaf 512 pdf 513
[pdf page 513] | ‎dp‏ حرخت را عم کفته‌اند ۱ - و قفل آهنین که | پرصتدوق زنند ۴ - و موی فرق سر و ‎US‏ سر | را نیز ‎a‏ ۴ -و پقتح‌اول بر وزن حوصله | ‎ole‏ است . | کوبن ۴ ‎bo‏ بای ابجد بروزن سوزن. | ‎AST‏ و مسگران باشد وبعربی‌مطراق | خوانند وآن دوقم میباشد : یکی مریم وآنرا | پتك خوانند ودبگری دراز وآنرا کزینه گویند. | ‎OST‏ نم اول.و ثانی مجهول وفتح | بای ابجد . کیاهی‌باشن شیرین که آنرا خورند ۵ | - و موحآب را ‎Va Sa‏ - و بمعنی ‎ths‏ | ‏عم کنتداد 9 ‎of,‏ دهلی ‎veh‏ دم دراز که از | چوب و گاهی ازسقال هم سازند و معر که گیران | و سرآواژه خوانان بر بیخ بغل ‎pS‏ و نوازند | و مشکی را یز کوبند که در آن دوغ ک
=== leaf 513 pdf 514
[pdf page 514] | AH | 8. ‏باشند‎ |  | کوتاه ‎VY‏ - جانوری است سا | گوزن خالهای درشت دارد و شاخ او نیز همچو | شاخ کوزن شاخ شاخ میباشد و اورا ‎ES‏ پای‌هم | ‎eae‏ با یی ای - و بمنی خر ‎ast‏ | ‏آمده است باآنکه دست خ کوش کوتاه است له | پای او . |  | کو تاه ‎Mh‏ بمعنی کوناء پای‌است | که جانور شبیه بگوزن باشد ۴ - وشخصی‌راییز | کویند که بیارکوتاه قد باشد . |  | کوتاه ‎are‏ را کرنند که | از عواقب امور نیندیشد و ‎cle‏ اندیش نباشد | وغافل و صاحب غفلت ‎ath‏ - و بخیل و مك | دا یز گنه و کون نظرحم میگوشد : |  | ‎is‏ ه بفتح اول و ثالث » بمعنی | کبوتر باشد و عربان حمام گوند ‎ny!‏ اول | هم کفته‌اند . |  | ‎hase
=== leaf 514 pdf 515
[pdf page 515] | Las | ‏کوتاه قد هستند وقد‎ Bye ‏مرخ‎ eat ‏چن‎ | ‏و ازتندی کفتار‎ cmd ‏ایشان زیاده برچهار وجب‎ | wots pe. ‏تمیتوان فهمید که چه میگویند‎ | ‏میکنند و در جزایر بحر زنگه‎ lage ‏و با آهن‎ | + ‏ه‌هست‎ |  | ‎SETS‏ - بر وزن ‎Ley‏ بلفت | زند و پازند استر را کوبند که مادرش اسب | است . |  | ‏کوج - بنتح اول- وثانی ۰ مطلق صمغ | را کوبند خواه سمع عربی باشد وخواه غیرعرمی | و ‎ule )۱( ae‏ را نیز کویند که در روز | جنک پوشند - و بضم اول وسکون ثانی بمعنی | کاج است که احول باشد ۴ ب و بمعتی اول‌باکاف |  | ‏(۱) چش : جبه . |  | ‎۷۹۲ |  | ‎. ‏هم‌آمده است‎ ww |  | ‎cs .‏ - بطم اول ‎OS‏ تانیمجهول | وجیم
=== leaf 515 pdf 516
[pdf page 516] | ۷۲۳ |  | کوچ ‎BS‏ - ازمتزل بمنزلی ‎Ko‏ | ‎dB‏ و تحوبل کردن را گوبند - و کنابه از | گربختن - وغروب کردن هم‌هست . |  | کوچ و بلوچ ۱ - سم بای ‎aml‏ | ‏ولام » این لفت از توابع است. و نام طایفه ای | ‎ach‏ ازسحرانشینان که در کوه‌های اطراف کرمان | توطن‌دارند و گویند ایتها ازعربان حجازهدرحرفت | ‎ole!‏ جنک و خونریزی ودزدی وراهزلی باشد. | ‎HSI‏ بیگانه‌ای ‎wats‏ یکدیگر را بکشند | ومال ‎Gad‏ را تاراج کنند و همچنین‌برادران | و خویشان وقرابنان و دوستان با هم‌جنگه کنند | و اين فعل را بسیار خوب دانند ؛ ویضی گنه |  | کوچه ۴ - بن اول وفتح جی‌فارسی, | راء کوچك و تک را ‎ae ag”‏ راه بز رکه | وفراخ
=== leaf 516 pdf 517
[pdf page 517] | کوداب ۱۷۲4 | مقابل پراگنده (۱) است ۱ کمبنه و دون و کم عقل وادان ‏ وکند فهمرکج | کوداب ۴ » بروزن و معنی دوشاب» طبع و ‎alee‏ را گویند - و اسب پی رکندرو | است که ‎LT‏ از شبر# انگور پزند . نی ‎LS‏ را یز ‎NS‏ | ‏کودد ۴ ‎bo‏ اول ‎gts‏ رسیده وئالت کوذر ۲ بضم اول و فتح ذال‌نقطه‌دار | ‎cm‏ برای قرشت زده » زمین دامن کوه را بوزن بوذ ۰ کوسالهرگویشد. | گونشد . ‎IT‏ بفتح اول و تالی وسکون رای | کودده ؟ ‏ بروزن مسخره » نوعی از قرشت ۰ بمعنی کبراست ۸ و ‎OT‏ رستنیی باشد | عرغایی باشد که مکان درآب سازد . خارناك که ازآن آچار ‎wh‏ و در دواها لیزیکار | ‎F‏ * تک | ‎DAES‏ مه | ‎aut | ey Gam 2 atk est 
=== leaf 517 pdf 518
[pdf page 518] | --۷۲۵-- |  | جمع کوده است که عبارت ازشهروقبه ‎Nath‏ . |  | Ye » ‏بر وزن دوشاب‎ WIS | - ‏کویند که بیار تشنه باشد و آب الدك خورد‎ | ‏و سراب را نیز کفته‌اند وآن شور زمیئی باشد‎ | ‏در صحراکه از دور باب ماند ؛ وباین‌معنی‌باکاف‎ | . ۴ ‏فارسی‌هم آمده است‎ |  | کودابین © « بن اولوخاس‌بتحتانی | رسیده و بنون زده » بمعنی کوبین باشد و آن | ظرفت ‎Woah‏ ترازوی بز رکه که از ب رکه | خرما با از لیف خرما با ‎gil‏ بافندوروغنکران | مغزهای کونته را در ‎OT‏ کنند و در شکنجه حر | ‎aT‏ تا روغن از ‎OT‏ برآید و ‎LT‏ بعریی معدل | خوانند . | کودبا ۴ - بنتم اود و ثانی و بای | ابجد بالف کشینه » آشی باشد که 
=== leaf 518 pdf 519
[pdf page 519] | کودشت » بنم اولر کسرنالك‌وسکون | شین وتای قرشت » بمعنی دسته چلك باشد و آن | دوچوب است یکی بلند بمقدار سموجب و دیگر | کوتاء بقدر يك قبضه که کودکان و جوانان در | سیر‌ها وجاها بازی کنند و هردو سرچو بکوچك | تیز میباشد وعربان چوب بز رکه را مقلاء و کوچك | را ‎Van Ka‏ . |  | کود لك - بنتح اول و ثانی و سکون | ثالث وکاف ۰ بمعنی کورژ است که میوه وبا رکیر |  | ‎Fach‏ - و نام موضمی‌هم‌هست ترديك به‌هومز- ر |  | ‏و لام جمعی از کثار باشد ۴ . |  | ‎TIS‏ ۴ - باعاف تازی(۱)بروزن | ‎Gye‏ بمعنی سخنیان و یماج باشد ؛ وباین | معنی با ‎SIE‏ فارسی و زای ‎ales‏ دار هم آمده | است . |  | ‎IW IS‏ - ینم حر 
=== leaf 519 pdf 520
[pdf page 520] | ‎gly Meee‏ ۲5 ۱۷- کوروش | ‎H‏ کود وش - درپارسی‌باستان کورو - ۰1607۷ درصيفةٌ مفرد مف کر |  | ‏حالت‌فاعلی کوروش 07558 . ودرصیغهةمفرددن کر حالت‌اضافی(مضاف‌الیه) | ‎Kéraush‏ ۰ این تام در کتببه‌های عبلامی 1-29 ؛ ودر ‎Gea‏ بابلی |  | ‎: ‏ودریونانی 5 آمده . رل‎ , 1-2-6 | ( Kent, Old Persian, p. 180). |  | ‏کوروش ‎ET ye‏ )004 -۵۲۹ ق . م. ) پسرچیش پش, سردودمان | هخامنشی است که بر آ خرین ‎oltol‏ ماد موسوم به ایشتوو 9 ‎Ishtuvigu‏ | ‏خروج کرد؛ وپادشاهی‌را ازقوم ماد بقوم‌پارسی‌منتقل‌ساخت. وی ارمستان | را مطیع کرد و با بابلیان جنگید » ‎Job‏ ولودیا ( لیدی ) را تسخیر نمود | و پادشاه کشور اخیر
```


## [2026-09-06T22:01:09.544Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py BQT:1721 --image 2>&1 | tail -40",
 "description": "Render BQT p.1721"
}
```


## [2026-09-06T22:01:13.086Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT kutaka ===\"; grep -n -E 'kutaka|kutuka' BRT.txt | head -10\necho \"=== BRT ca 'und' ===\"; grep -n -E '^ca[,.]|^ča|cis-ca|cisca|čiš' BRT.txt | head -20\necho \"=== PHD kotah/kodak ===\"; grep -n -i -E 'kōtāh|kotah|kōdak|kodak|kwtʾh|kwtk' PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n -i -E 'kōtāh|kotāh|kōtak|kotak' NYB_vol2_glossary.txt | head -10",
 "description": "Grep BRT, PHD, NYB"
}
```


### [2026-09-06T22:01:16.341Z] TOOL RESULT

```
REF: BQT:1721  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 514  OCR-lang: fas

-۱۷۹۱- کوتمیال
باشند ,38 کوننك ی « بروزن هوشنگه»یمعنی
کوتاه پا ۱ - جانوری است ماند | کدنك است . وآن جچوبی باشد که کازران بدان
گوزن خالهای درشت دارد و شاخ او نیز همچو | جامه راکوبند پمنی دقاقی کنند و آبرا كوتنك
شاخ کوزن شاخ شاخ میباشد و اورا کوتاه پای‌هم | گازر هم میگویند وبعریی مدقه خوانند.
کوبند با زیادتی تحتّانی - و بمعنی خر کوش‌هم کو توال * - با واو بروزن لوت‌مال,
آمده است باآنکه دست خر کوش کوتاه است له | انکه دارندة قلمه و شپر باشد و او را سرهتگه
پای او . هم میگوبند و بعضی کوبند این لغت هندی‌است
کوتاه پاچ - بممنی کوتاء پای‌است | و فارسیان استعمال کرده‌اند چه کوت بهندی قلعه
که جانور شبیه بگوزن باشد ۲ - وشخصی‌رانیز | است .
گوبند که سار کوتاه قد باشد . کوته با ۱ - مخفف کوتامپا است‌وآن
کوتاه نظر « شخی را کونند که جانوری باشد شبیه بگوزن و او راکوته پای هم
از عواقب امور لیندیشد و عاقبت اندیش نباشد میگوبند - وخر کوش را نیز کفته‌اند .
وغافل و صاحب غفلت باشد - و بخیل و مك کوته پاچه ۷ - مخفف کوتاء پاچه
را نیز کویند وکوته نظرهم میگویند . است که جانور شبیه بگوزن باشد .
ور ۴ - بننح اول و ثالث . بمعنی کوته پال » بابای ابجد بروزن كوچك
کبوتر باشد و عربان حمام کوبند ؛ و پشم اول | سال » بمعنشی کوته قد باشد چه بال بمعتی قد
هم کفته‌اند . وقامت هم آمده است . کوبند دریکی از جزایر
۱ - رك : کوته‌پا :کوتاه پاچه » کوته پاچه .
۲ - رك :کوتاه پا کوته پاچه . ۴ - رك :کبور .
۴ << کدنگه (ه.م.) پا کدنگه » قس : کدین , کدینه . ۵ کتوال, ازهندی
« دزی ج۲ ص ۹44 » مانسکربت ۳۵18-80812 ( محافظ قلمه ) مر کب از دو جزء : 012 و
482 در سانسکربت بمعنی قلمه و دژ نظامی «وبلیامز ۳۱۲ : ۲ ۳ 0212 ( محافظ,حامی,
تگهبان ) « وبلیامز ۹۲۲ : ۳ . پراکربت ۴۵۸ ( قلعه . ساختمان بزرککه ) کویا اين کلمهرا
لشکربان‌سبکتکین ومحمود بابران آوردند « فرهنکه نظام » ؛ بعضی ان لت رات کی‌داستهانده
چه در ترکی جغتایی کوتاوال (کوتاول) بمعنی پاسبان و نگاهبان و محافظ قلمه آمده « جشتلیی
س 2۹۳ ۰« لفت جغتای و ترکی عثمانی . شیخ سلیمان اس ۲۵۷ ۰ « بیغقی . نفیمی چ ؟صض
۲ ولی این کلمه از هندی بتر کی رفته است . ‎٩‏ - رك :کوتاه با + کوتاه پاچه.
۷ - رك :کوتاء پاچه » کوناء‌پا .
۵ کوقاه - بنم اول ( ۳۵10 , در قدیم 1۳۵1210 ) ۰ اوستا - 5۷12168 (کوچك).
پپلوی 8۳۵121 (کودك ) ۰ ارمنی ع ۴018 (كوچك ) . مرکب از : ۳۵1 ۳ پارسی بلستان
- 262018 ۰ اوستا - ۷۵۷1812 (کوچك) 2۳ ( پوند ) رك : هوبشمان ۸۷۱ ؛ افقالی
۳ اسشق - هوبشمان ۸۷۱ ؛ نیز پهلوی :[۴۵۸۵ ( قصیر ) « ازدوالا 4۹۸ * نیب رکه
کوبد: فارسی ۳۵12 از دل2۵11 ازهط؛ - 18۷2 068118 ( پعنیآنکه زور ولیرویش
کم است ) «نیب رکه س ۲۰۸ : 818۷ > کردی 4 0۸6 ( کوتاء » قصیر) ۸« ژابا ۰4۳۹۹
کیلکی 8014 ؛کم ارتفاع ‏ قصیر کم طول .. کم بلند . ضددراز : « ملك زاده‌ای را شتیدم که
کوتاه بود و حقیر و دیگر برادرش بلند و خوبروی .> «گلستان ی ۱۸ *.
```


### [2026-09-06T22:01:16.424Z] TOOL RESULT

```
=== BRT kutaka ===
5285:•  j.  araeka-  Adj.  -  ?  -,  Bez.  einer  Ameisen- art: maoirinqm  'kanam  kutakanqm  duzai- ninqm  V.  74. 5.
20075:j.  maurvay-  m.'>  'Ameise',  ein  daemscbes Tier,  von  dem  zwei  Arten  geschieden werden:  xrafstnm  ava.Janalta  moffifftn danHjtarsim  (sd.)  V.  16.  la;  —  hagvan maoirinam  danS.iarsanqm  ava.Janyat  V. 14.S1  ^o-73i  —  baiiian  maoirinqm  arai- kanqm  (sd.)  kutakanqm  duiaininqm  ava.- /anyai\:i4.$.
=== BRT ca 'und' ===
2649:•  j.  aenah'vant-  Adj.  -Gewalttat,  Frevel übend  an  — '  (Lok.):  yff  cisca  akmi  nmUne .  .  'nat^Aä  asH  masye  Y.i^.aS.
8859:gäiu*saste\t 5. 102.  a)  mit  Gen,  part: hamistayalca  .  ,  kahe  kahyäcU  drvatqm Y.  61. a,.  3)  mit  vorangehendem  Relativ und  folgendem  1)  clt  (hinter  ka-\  2)  ^a (hinter  i kay-)  'Jeder  der..,  quisquis,  qui- cunque',  nur  substantivisch;  1)  nur  gAw.: y3  dalnqm  vokB  *sänsttl  (sd.)  manatthä .  .  kas^l  Y.4p.  5;  —  «ÄJ  ahmäi  yahmai Ulla  (sd.)  iahmäicit  .  .  däyät  akurö  Y. 43- 1 ;  —  at  .  .  s?rao^  jantü  .  .  ahmäi yahmäi  vasi{%A^  Ikahmäi^i'^.  44.16;  — ^ao^anäi/.  .  pailyaogJt  {sA.)  tä  .  .  yä  Tm AuJyätSi/ (sd.)  payät  '.  käclt  (NPn.)  Y. 4tf.8.  2)  yS  lcisca'^>    ahmt   nmsne  .  .
11084:bilden,  uzw.  in  Verbindung  mit  1)  dem Pron.  intcrrog.  'kay:  cisca  "quisque"  H.  2. II   (Sp.  425  u.).  2)  demPron,  reljo-:
12404:—  aii'afitS  ahi  abatthö  tarn  yö  aAurS mazda  "V.  ig,  2q;  —  cisca  tarn  caraitis ahi  yqm..iäraitinqm..sraistqm  dädansa Vyt.57(?)*>;  — s.  noch  V.  2. 43  bei  i  und "  Bh.  4. 6,  15  bei  3.  3)  1  im  Ap.  voi dem  veraJlgemeineraden  kä  (Sp.  42a); tuvam  k3  Ayc^  aparam ..patiparsäAy'Bh. ^.6J>;  15^;  —  tuvam  kä  xsäya^iyt^  hy(^ aparam  *ahy  Bh.4, 19,  5,  14.  \  4)  sonst beliebig;  a)  an  der  Spitze  des  Satz(teil)es; o)  unmittelbar  vor  Vok.:  tvim  mazäa ahura  frs  mü  sXsä  ..Y.zS.w.  ß)  sonst: tarn  mafhanahe  pSta  nipäta  ahi  adrmqm Yt:  io.  80;  80,  29*,  V.  ig.  6,  VyL  22,  2^, —  iäm  aisqm  tbi^yatam  tum  aliqm tbalsaauhatqm  fialsä  sSndayeAiYtlo.'j6;\ 23'.  »9tJ,  78',  5-  87.  IS-  55-  b)  in andrer  Stellung;  a)  unmittelbar  vor  Vok.: aoa  nS  tarn  mi^ra  .  .  dayU  Yt.  10.  94;  Y. 37.36;  —  äatmltüm  aridvl  sUre  anakite .  .  piium  ralcaya  Yt5. 77;  —  aai  tarn sarahuitra  .  .  V.g.  12,  10.  18;  — -  3af ya/  /am  tara%uftra  .  .  V.  //.  4;  Vyt. 4-3-  ß)  sonst:  *pouru.narim  tarn  kin- näH  ..  Y.  io,  13;  —  i^a  ml  tsm  kam.- caranuha  .  .  Yt //,  60;  —  Aanalsa'  ta tarn  tat  mlzd^m  yal  ..  Y.  5p.  30;  — äa^  mqm  tQm  fiaonayeke  '^.ii.i;  V.  22. I.  9t  Vyt  13  rSt;  — •  aal  tarn  pascatta  .. V.  i".  4;  Vyt^/;  —  yat  tum  ainim  avaS- fiäiS  .  ,  H.a.  13;  — •  yaha  tarn  trftvd (sd.)  vaia/ghe  V,5. 17,  ai;  Vyt i2.
16957:i)  Villkommen  heissen',  mit  Gen.'': /rasa  fraya  vahist>tn  ä  ahüm  hnjayanti y?  . .  *sirSus!a  . .  azpmca  Al  bpnjaim  yö  .  . ahurS .  .  uäa  *äa  ti  nun  "'stracks  gehe weiter  zum  Paradies'  (so)  werden  ihn willkommen  heissen  die  Sterne . .  und  (so) werde  ich  ihn  willkommen  heissen,  ich  der Schöpfer  AAM.,  'nach  Wunsch  geh  es  dir hier,  o  Mami'"  V.  7. 52.  2)  'huldigen', mit  Gen.:  bm/ayai  ahurS  .  .  b>njay>n amisä  spMta  yeAha  (sd.)  IbArpff  huraohaya ". .  des  schöngestaltetem  Leib  huldigte j4AM.  . ."  Yt  10.  90;  —  *fraiaintlmca  .  . ye^hh  peurUsca  iftv/ayqn'^  naicisca  aitiha ydssiti  . .  "und  Nachkommenschaft  , .,  der manch  einer  huldigen  und  der  keiner wünschen  soll  .  ."  Y.6'5. 11.
18454:•  j.,  g.  nae-kay-  neg.  Pron.  interrog.  'non quisquam',  nur  substantivisch  'nemo;  nihil': %waAy3  xratsus  ylm  'Si  dabayäti  (sd.) y.43i>\  —  y3m  vä  '''üs  dänst  iil  (sd.) Y.  43-  13;  —  *frasafntlmca  .  .  yeäha pourBsta  htyjayan  'cisca  aiii/ia  yäsaili zyänäi  (sd.)  Y.  05.  1 1 ;  —  yahmat  haca °eii  bunjayai  .  .  nSit  ^usyqs  i^A^  tacö  .  . Aog.jSB.;  —  yaf  mqm  'a/  taurvaySi nsil  dafuö  nai^a  .  .  Yt  /.  6.  a)  mit Gen.  pari.:  'iil  a^arftiiam  tva  rait  .  . asayqm  (sd.)  nsit  .  .  V.^.iy,  —  yS  'Sm isaiti  hunaranqm  V.  jj.  19;  —  a^qm alnauhqm  'clt  vJdvh  aojöi  (sd.)  Y.  32. 7.  na^im,  naiHs  als  Neg.  sbes.;  vgl. auch  na^üxit  mit  No.
19037:jAw.;  zu  1);  a)  das  Verbum  ist  indi-  n"^  . .  rta^a.äm  anyqm  . .  Y.  2.  ^y-  —  es kativisch:  n°  data  aAmt  «'  asts  (sd.)  ist  eine  Verbalform  entsprechend  der  des mpntS  .  .  V.  2. 3;  —  «•  As  ao^  pairi.-  vorhergehenden  positiven  Satzes  zu  er^ z'tfSiä»»' V,ip.3;  Yt5.93;  —  n°tatii^ar»nS\gä.ta.ta:  ap)rmäyu  aAmi  n'  p?r)näyu  (sA) pairi.abaom  Yt.7p.57;  —  "^"^  ^^l  n°  pairi.-\Yt  ig.43;  —  /W  äp^m  jainti..n'  avaha Jräsa  (sd.)  .,  *p3r>saAi  . .  Y.p.  25;  —  nava\  m3r>tS  V,5.  37;  38;  —  avi  ''ainyS  *'surun- Al  asti  ciha  .  .  n°  he  asti  yaozdühnm  V.  I  vaili  n'  ainys  N.  24;  P-i?;  —  nisriti 3-39',  —  "'  '?'"  ä^ravöpührim  (sd.) '^aStaAe  ästryeiti  n'  anisriti  N.ii; —  mosu nai^a  *daste  Aapu^nm  Y.70. 15; — na!cisca\tat  äs  n'  darrf>m  Yt5.  65;  —  sumnaoiti aitiAi  (Sp.  8  o.)  yasäiti  xyänäi  n'  snähai  ,*zaeta  upa.sraotara7tqm   n°  *upajraotärS
=== PHD kotah/kodak ===
PHD.txt:426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
PHD.txt:4376:young juwün, keh, kawādak, kodak. younger keh(tar).
PHD_mackenzie.txt:3265:·kawadak [kw)tk l ] young; baby; v. kodak.
PHD_mackenzie.txt:3323:kodak [kwtk I M qwdk, N --] young, small; baby.
PHD_mackenzie.txt:5985:ass xar; wild - gor.                     baby wa~cag, kodak, kawadag.
PHD_mackenzie.txt:7584:similarity hiiwandih; v. likeness.            small gisnag, kam, keh, kodak,
PHD_mackenzie.txt:8002:write nibistan.                         young Juwan, keh, kawadak, kodak.
PHD_mackenzie.txt:9584::lkardag, kodak
=== NYB ===
6041:qwdk: kotak qyh: !kas
6696:ködak: kotak
```


## [2026-09-06T22:01:35.084Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T22:01:35.089Z] TOOL RESULT

```


```


## [2026-09-06T22:01:39.903Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AA%D8%A7%D9%87",
 "prompt": "Give the full Persian etymology section for کوتاه (kutāh) 'short': Middle Persian form, Proto-Iranian/Old Iranian reconstruction, cognates, and any cited authorities (Hasandust, MacKenzie, Hübschmann, Nyberg)."
}
```


## [2026-09-06T22:01:40.921Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AF%DA%A9",
 "prompt": "Give the full Persian etymology section for کودک (kudak) 'child': Middle Persian form, Old Iranian reconstruction, Avestan cognate, and cited authorities."
}
```


### [2026-09-06T22:01:45.851Z] TOOL RESULT

```
# Persian Etymology of کوتاه (kutāh)

Based on the Wiktionary entry provided, here is the available etymological information:

**Middle Persian Origin:** The word derives "From Middle Persian [Term?] (/⁠kotāh⁠/)."

**Cognates:** The entry identifies کوتاه as cognate with:
- کودک (kudak, "child")
- کوچک (kuček, "small")

**Cited Authorities:** The etymology section references two sources:
1. Farhang-e Farsi (A Persian Dictionary) by Mohammad Mo'in
2. Nourai, Ali (2011), *An Etymological Dictionary of Persian, English and other Indo-European Languages*, page 258

**Limitations:** The provided content does not include Proto-Iranian reconstructions, Old Iranian forms, or references to scholars such as Hasandust, MacKenzie, Hübschmann, or Nyberg. The Middle Persian form itself is marked as "[Term?]," indicating incomplete documentation in this particular source.
```


### [2026-09-06T22:01:48.150Z] TOOL RESULT

```
# Persian Etymology of کودک (kudak)

**Middle Persian Origin:**
The word derives from Middle Persian *kōdak* (کودک), meaning "young, small; baby," which itself comes from Proto-Iranian *\*kawta-ka-*.

**Proto-Iranian Reconstruction:**
The term traces back to Proto-Iranian *\*kawta-* ("small, diminutive"), tentatively connected to Proto-Indo-European *\*(s)kaw-* with the sense of "small, diminutive (affectionately)."

**Avestan Cognate:**
The Avestan form *kutaka-* ("small") represents a cognate linguistic relative.

**Scholarly Authorities:**
Edelʹman's *Etymological Dictionary of Iranian Languages* (2011, vol. 4, p. 382) and Nourai's *An Etymological Dictionary of Persian, English and other Indo-European Languages* (2011, p. 258) provide the cited etymological documentation for this word's development and connections across related language families.
```


## [2026-09-06T22:01:54.135Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%86%DA%A9",
 "prompt": "Give the full Persian etymology for کوچک (kuček/kučak) 'small': proposed origins, Middle Persian form, any connection to کودک/کوتاه, and cited authorities."
}
```


## [2026-09-06T22:01:56.611Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7e",
 "prompt": "Summarize the reconstruction page for PIE *kʷe: meaning, whether it is an enclitic conjunction 'and', its relation to the interrogative stem *kʷis/*kʷo-, and the descendants listed (Indo-Iranian ca, Avestan ča, Old Persian cā, Latin -que, Greek te, Gothic -h)."
}
```


### [2026-09-06T22:01:58.649Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T22:02:00.379Z] TOOL RESULT

```
# Persian Etymology of کوچک (kuček/kučak)

**Proto-Indo-Iranian Origin:**
The word derives from Proto-Indo-Iranian *kaw- ~ *ku- ("young, small"), filtered through Proto-Iranian *kaw-ča-ka.

**Middle Persian Form:**
It comes from Middle Persian kūčak (کوچک), meaning "small," though the exact script representation requires specialized notation.

**Related Persian Terms:**
The entry notes connections to two related words:
- کودک (kudak) = "child"
- کوتاه (kutâh) = "short"

The entry states these share a common etymological thread, directing readers to کودک's entry for further details on this relationship.

**Additional Cognates:**
Related forms appear in Mazanderani پچوک (pečok, "small") and Middle Persian variants کوچ (kūč, "small") and کوک (kūk, "small, short").

**Scholarly Sources:**
The etymology cites eight academic references by linguists including H.W. Bailey, D.N. MacKenzie, and Oswald Szemerényi, establishing connections across Indo-European and Iranian language families.
```


## [2026-09-06T22:02:04.789Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-k%CA%B7e",
 "prompt": "Summarize: meaning of PIE *-kʷe, its status as enclitic conjunction 'and', relation to interrogative *kʷis, and descendants (Proto-Indo-Iranian *ča, Avestan ča, Old Persian ca, Latin -que, Ancient Greek τε, Gothic -uh, Hittite -ku/kku)."
}
```


## [2026-09-06T22:02:05.830Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sesqui-",
 "prompt": "Give the full etymology of the English combining form sesqui- and of sesquicentennial."
}
```


### [2026-09-06T22:02:11.587Z] TOOL RESULT

```
# Proto-Indo-European *-kʷe: Summary

**Meaning and Function:**
This reconstructed particle functioned as a coordinating conjunction meaning "and" and as a generalizing/distributive particle forming universal expressions from interrogatives.

**Etymology:**
Scholars propose two origins: Dunkel suggests *-skʷe derives from an old injunctive of *sekʷ- ("to follow"), while Szeremenyi proposes derivation from an instrumental *kʷe-h₁ of *kʷís ~ *kʷós, which Dunkel associates with the distributive sense of "somehow."

**Linguistic Status:**
As an enclitic conjunction, *-kʷe attached to words rather than standing independently.

**Major Descendants:**
The element survived across Indo-European branches:
- Latin: "-que" ("-ever")
- Ancient Greek: "τε" (te)
- Hittite: "-ku/kku"
- Proto-Indo-Iranian: "*-ča" (reflected in Sanskrit "-śca")
- Gothic: "-uh"
- Albanian: "s'" ("not")

The particle's wide distribution across distantly-related language families demonstrates its importance in reconstructed Proto-Indo-European grammar and its persistence through millennia of linguistic evolution.
```


### [2026-09-06T22:02:13.104Z] TOOL RESULT

```
# Etymology of Sesqui- and Sesquicentennial

## Sesqui-

The prefix comes from Latin *sesqui-*, derived from a contraction of "*semis-que-" meaning "a half in addition." It combines *semis* ("a half," related to semi-) with *-que* ("and"), an element from the Proto-Indo-European root *kwe* meaning "and, -ever." The prefix typically signifies "one half more" than a given unit. Latin *semi-* frequently underwent phonetic reduction in compounds, producing related forms like *sestertius* (a Roman coin valued at two-and-a-half units).

## Sesquicentennial

This adjective emerged in 1875, formed by combining sesqui- with centennial. It denotes "pertaining to a century and a half." The earliest documented use appears in an 1875 notice describing "a 'Sesqui-Centennial gathering'" of descendants of settlers in Pennsylvania. As a noun, the term appeared from 1880 onward, initially referencing Baltimore's celebration. An alternative form, *sesquicentenary*, is attested from 1896 in connection with Princeton's anniversary.
```


## [2026-09-06T22:02:22.352Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD kwe ===\"; grep -n -i -E \"^k[’']?we|k\\^we|kwe-\" AHD_watkins1985.txt | head -20\necho \"=== SYN and ===\"; grep -n -E 'AND \\(conj' SYN.txt | head\necho \"=== KNT lexicon ca ===\"; grep -n -E '^ca\\b|^-ca\\b|^ciy\\b|^cis' KNT.txt | head -20\necho \"=== WLD band3 index que ===\"; grep -n -E '\\bq[uv]e\\b' WLD_band3.txt | head -10",
 "description": "Grep AHD, SYN, KNT, WLD"
}
```


### [2026-09-06T22:02:22.435Z] TOOL RESULT

```
=== AHD kwe ===
650:kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
651:kwelek-
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
=== SYN and ===
=== KNT lexicon ca ===
5395:ciyăkara- (§53) adj. ‘how great’; nt. аз sb., ‘how great a thing’: *ciya(n)t-, cf. Skt. kiyat nsn. ‘how much, how many’, + kara- to root kar- ‘make’ ($160.19; Bthl. AiW 597; hardly to kara- ‘time’, cf. hakaram, as taken by MB Gr $293, Hz. ApI 101-3). ciyakaram nsn. (§259) DNa 39; ciyükaram DNb 50; ciyakaram-ca-maiy (written — : -"m*m*eur; $41, $51, $132, $138.I; Lg. 15.178, — | against Hz. ApI 240) DNb 51, 51f. 1
=== WLD band3 index que ===
```


## [2026-09-06T22:02:24.459Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY کوتاه ===\"; grep -n 'کوتاه' incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY کودک ===\"; grep -n 'کودک' incoming/ARY/ARY_pages.txt | head -10\necho \"=== MON کوتاه ===\"; grep -n 'کوتاه' MON_part2.txt | head -5; grep -n 'کوتاه' MON_part1.txt | head -5",
 "description": "Grep ARY and MON"
}
```


### [2026-09-06T22:02:24.553Z] TOOL RESULT

```
=== ARY کوتاه ===
=== ARY کودک ===
2920:۲ / بابا (واژه‌ی کودکانه به چم"پدر")
9335:چم اين واژه در زبان آلمانی: کودکك.
12291:۱ واژه‌های فارسی " کودک" و "کوچکه" هم از همین ریشه‌اند. .
13333:۰ | لالايي لای لای (به چم "آواز برای خواباندن کودک»)
13360:۳ واژه‌ی کودکانه‌ی آلالا" و "لالاکردن" نیز از همین واجريشه است.
13651:۱ این واژه‌ی کودکانه تقریاً در تمام زبان‌های هند و اروپایی وجود دارد و رابطه‌ی آن پا آمادر" و پستان "تیه"
14193:ا ۳ واژه هائی مانند"ممه" و پا تس" چون کودکانه یاکم کاربرد هستند کمتر در نوشتار به کار می‌روند و شاید به همین
=== MON کوتاه ===
119:دمب رگ کوتاه است. درازی ب رگ آن بین 
941:سر کوتاه عضلةٌ دو سربازویی می‌چسیند. 
2109:کوتاه چاق. 
2639:پیچ: قسمی غلیان که بجای نی کوتاه چوبی؛ 
4291:ی یت توت آن کوتاهتر از حروف 
631:ای (کوتاه) 
1318:قسمی جامه؛ لباده. جبةٌ آستین کوتاه. قسمت 
1406:رفتن آب. کوتاه شدن جامةً تازه بس از 
8366:کوتاه کردن» تلخیص, ایجاز» اجمال. 
8372:(ق.) از روی اختصار» به کوتاهی» بدون
```


## [2026-09-06T22:02:33.374Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY ctx 12291 ===\"; sed -n '12280,12295p' incoming/ARY/ARY_pages.txt\necho \"=== AHD kwo- ===\"; grep -n -o -E 'kwo-\\. Stem of relative[^]]*\\]' AHD_watkins1985.txt | head -3\ngrep -n 'kwo-' AHD_watkins1985.txt | head -5",
 "description": "ARY context and AHD kwo-"
}
```


### [2026-09-06T22:02:33.455Z] TOOL RESULT

```
=== ARY ctx 12291 ===
انگلیسی کهن (لل8لا80 صا0): پسگشت‌ها کب
: 507 1 روم
انگلیسی (69701/877): با( را
دانمارکی (0۸(/880): 07 1 (813037) ,254 (073)
ا: سوئدی (۵775:0/371): 0 2 (813021) اد سا
4 نروژی (0/3850140/: لا( 139 نا
هلندی (4ل070): ۳0 8 (811087) بر
ً اسلاوی کهن (۷12ما5 86اب( صا0): 5 (8[11087) ۸
۱ لد ۱ برهان قاطع + ۱۷۲۴۱
: لهستانی (5/ا۸0): ا ادا
یادداشت:
۱ واژه‌های فارسی " کودک" و "کوچکه" هم از همین ریشه‌اند. .
۲- رابطه‌ی واژه‌های ابرانی و سانمکریت این فهرست با دیگر واژه‌های آن احتمالی است و لذا جلو واجریشه‌ی هند
و اروپایی (شاید) آورده‌ام.
ِْ
۱ اوستایی (483740۷): 01۸ انگلیسی کهن (80/0//37 10۱0 018۸0
=== AHD kwo- ===
166:Stockbreeding and animal husbandry were an important part of Indo-European eco- nomic life. The names for all the familiar domesticated animals are present throughout the family: gvou-, “cow and bull,” owi-, “sheep,” ag“h-no-, ‘lamb,’ aig- and ghaido-, “goat,” sd-, “swine,” and porko-, “farrow.” The domestic dog was ancient (kwon-); its name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?.
433:ekwo-. Horse. Possibly originally derived from kwon-. 1. Latin equus, horse: EQUESTRIAN, EQUINE, EQUITANT, (EQUITATION); EQUISETUM. 2. Greek hippos, horse: EO- HIPPUS, HIPPOCAMPUS, HIPPOGRIFF, HIPPOPOTAMUS. [Pok. ekuo-s 301.]
655:kwo-. Also ki-. Stem of relative and interrogative pro- nouns. 1. Germanic *hwa-, hwi- in: a. personal pronouns *hwas, *hwasa, *hwam in Old English hwd, hwes, hwem, who, whose, whom: WHO, WHOSE, WHOM; b. pro- noun *hwat in Old English hwet, what: WHAT; c. adverb *hwi in Old English hwy, why: wHy; d. relative pronoun *hwa-lik- (*lik-, body, form; see lik-) in Old English hwilc, hwelc, which: WHICH; e. adverb *hwo6 in Old English hii, how: How!; f. adverb *hwan- in (i) Old English hwenne, hwanne, when: WHEN (ii) Old English hwanon, whence: WHENCE; g. adverb *hwithré in Old English hwider, whither: WHITHER; h. adverb *hwar- in Old English hwér, where: WHERE. 2. Germanic *hwatha- raz in: a. Old English hwether, hwether, which of two, whether: WHETHER; NEITHER; b. Germanic phrase *aiwo gihwatharaz, “ever each of two” (*aiwo, *aiwi, ever; see aiw-; *gi- from *ga-, collective prefix; see kom), in Old English €ghwether, &ther, either: EITHER. 3. Latin gui, who (genitive plural guérum): QUA, QUIB- BLE, QUORUM. 4. Latin quid, what, something: HIDALGO, QUIDDITY, QUIDNUNC, QuIP. 5. Latin quam, as, than, how, in quasi (quam + si, if; see swo-), as if: QUASI. 6. Latin quod, what: QUODLIBET. 7. Latin quot, how Many: QUOTE, QUOTIDIAN, QUOTIENT; ALIQUOT. 8. Latin quom, when: QUONDAM. 9. Latin quem, whom: CON- QUIAN. 10. Latin quantus, how great: QUANTITY. 11. Latin gudlis, of what kind: QuALITY. 12. Latin ut, that: (uT). 13. Latin uter, either of two: NEUTER. 14, Latin ubi, where, and ibi, there: ALIBI, UBIQUITY. 15. Persian chiz, thing: CHEESE, [Pok. k¥o- 644.] kwon-. Dog. 1. Greek kudn, dog: CYNIC; CYNOSURE, PROCYON, QUINSY. 2. Suffixed zero-grade form “kwn-to- in Germanic *hundaz in: a. Old English hund, dog: HOUND; b. Old High German Aunt (> German Hund), dog: DACHSHUND; c. Dutch hond, dog: KEESHOND. 3. Nominative form *kw6o in Welsh ci, dog: CORGI. 4. Variant *kan-i- in Latin canis, dog: CANAILLE, CA- NARY, CANICULA, CANINE, CHENILLE, KENNEL}, [Pok. Ruon- 632.]
877:puk-2, Bushy-haired. Suffixed form *puk-so- in: a. Ger- manic *fuhsaz, fox, in Old English fox, fox: Fox; b. Ger- manic feminine *fuhsdn- in Old English fyxe (> Middle English fixen), she-fox: VIXEN. This root is in part a taboo deformation of wikwo- and wip-é-. [Pok. pik- 849.]
1057:swo-. Pronominal stem; so. Derivative of s(w)e-. 1. Ger- manic *swa- in: a. Old English swd, so: sol; b. Germanic compound *swa-lik-, “so like,” of the same kind (*/ik-, same; see lik-), in Old English swylc, such: sucH. 2. Ad- verbial form *swai in Latin si, if, in quasi (quam, as; see kWo- + si, if): NISI, QUASI. [In Pok. 2. seu- 882.] s(w)okwo-. Resin, juice. Variant form *sokvo- in Greek opos (< *hopos), juice: opruM. [Pok. s(wekvo-s 1044.] swombho-. Spongy. Germanic *swamba- in: a. Middle Low German sump, swamp: SUMP; b. Low German zwamp, swamp, akin to the Low German source of swamp. [Pok. suomb(hjo-s 1052.]
```


## [2026-09-06T22:02:40.792Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nawk 'NR>12180 && NR<12300' ARY_pages.txt | grep -n 'pdf page'\nsed -n '12200,12292p' ARY_pages.txt | head -60",
 "description": "Find ARY entry context"
}
```


### [2026-09-06T22:02:42.313Z] TOOL RESULT

```
31:[pdf page 411]
56:[pdf page 412]
90:[pdf page 413]
اسپانیایی ((52۸7/8): ه 3 هلندی (9ع007)+ 1000
ایتالیایی (7ل4لق7): " اه اسلاوی کهن (70ها5 بل#ناتله 2ا0):
۳ رومانی (/۸(4۸(/14ن#): ادا 6۸۸
اش پرتغالی 00011 ۲۸3۸ لهستانی (034): 610۸
گرتبکه هرهم تناها روسی (584(7): یدا ان ۱
ایسلندی کهن (/(5(701047/14 00): چکه (280[1): 717۸۸ ۱
100 صربی (۷ل1۸ق588): ۸شاج
ساکسونی کهن (/54200۸0 ۰:00 130810 برهمی ((80775۸414): 1۸۸
فریزی کهن (/(۳8/314 0ا0): اسلراکي (81.01434): 1۸
0 ,132۷80 لیتوانی (ل4ا هلا 7 لام مها
آلمانی کهن ((48ل087 لالز (ا۵): لترنی (لتی) (774(1ا): مها ُ
[pdf page 411]
۲ | کندن
پسگشت‌ها کت ۲ 3213 8000
ی 0 هقه رهوج لابدنه
0 (70ه58۸) ای ال 4 (38۸40) . 9 ,24/20
0 818 :ما02 برهان قاطع : ۱۸۸۴ :۳
اوستایی (4۸887۸۷)+ -۸ اه ۹:۵
پارسی باستان (۳8۸۵۸۷ صاه): سا آرمنی (۸/۸48(]40). هام۸
پهلری (41ل۳4): ۳۸۵۲۲۸۸۲ ,ان 010ها .
اوستی (0538112): لانشن پسگشت‌ها شتا ادا
کردی (/7373۸310131:0080/31) ,)1052۸0 4 ونم
افغانی (پشتر) (/(۸۳077۸): 0 (016) اد ده ۲12
,110 ,1۸0۸ 2 010 مرک 0۱3۱
سانسکریت (84(5877): برهان قاطع + ۱۷۰۷
بادداشت:
۱ واژه‌های این فهرست با واژه‌های انگلیسی 2۸18۷ و آلمانی 1و واژه‌های اسکاندنیاوی همريشه آنها
شباهت دارنسد ولی ظاهراً ایسن واژه‌ها از یک واجریشه‌ی هند و اروپایی دیگر (۳0738817) آرده‌اند
( 1(
۲- بازگشت به پانوشت ۳016032۷ در صفحه‌ی ۹۳۴
۳ رابطه‌ی واژه‌های هند و ابرانی این فهرست با واجریشه‌ی هند و اروپایی فرق احتمالی است و بهمین دلیل در جلو
آن (شاید) بکار رفته است.
اوستایی (48537۸): ۸ 1610۸ ,361105 ,1610152
ش7118 وناب افغانی (پشتو) (۸701۸۸1): 1
پهلوی (۲1شاننمه): ۹1 سانسکریت (6۸(97077).
کردی (080157): ۸ بش18 ,3۳۷2 ب317۷۸ (260
[pdf page 412]
|
ا
۱ کرتا» کوته / ۴۱۳
ارمنی ((4/8014): 8 178 اسلاوی کهن (ع1/ها5 7-86 010):
یرنانی (076870): 7 0
لانین (710ها): 11 لهستانی (۳0/5[7): ام زان
فرانسه (۳2۸27): 0 چکه (۲280/7): 4 25
اسپانیایی (5۳۸۸/34): ل ال زارد بوهمی (8017814421): ,25
ایعالیایی (لغلمل7): 20 اسلوا کی (81.044): 4 8205
رومانی (۸44(7/۸۸ت#): 108 لیترانی ((فاامتان ۰7 ۴۵۸ شتا
پرتغالی (00/717017885): 002 پروسی کهن (/(4ا۶5ت۲۸ ۰۰:02 01787
گونیکه (0077//0): دادن گالی (تلقلاتامه): اند ید
ابسلندی کهن (/(0/0414لم5 00): ولزی (7]قل): 0 ,۲۷
114 آلبانی (/۸8۸(14): ۸ ولآ
ساکسونی کهن ((240 2ا0): ۰ 13۷/28 هتیت (07]77178: ای
فریزی کهن (۸ا5ل77 0): 1
آلمانی کهن ((ل0279 04اب 17/230:)010 پسگشت‌ها انش رت
آلمانی (/05840): ۳0 8 ۶۵0908
انگلیسی کهن (20/05 0ا0): 41 (۲۲178233) :8/7
: 17۷۷۸ 4 (0۵0) :م۸2
انگلیسی (701/874(ق): رن 0 ۲۲۲5۵۸۵ 8 ل2اقل هط
دانمارکی (0۸7/84): 10 ۵ (۲/58۵) :547
سرئدی (38:۵/57): 3 9 (۵۸2:) ری ادا
```


## [2026-09-06T22:02:58.951Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT: search 'und' enclitic ca entry ===\"; grep -n -E \"ca\\b.*Konjunkt|Konj.*'und'|enklit\" BRT.txt | head -20\necho \"=== BRT cit ===\"; grep -n -E \"^\\s*[•*]?\\s*j\\., ?g\\. ca\\b|\\bcit\\b.*Partikel\" BRT.txt | head -10\necho \"=== KNT ca lexicon ===\"; grep -n -E 'ca\\s+(encl|conj)|conj\\. ‘and’|encl\\. conj' KNT.txt | head -10\necho \"=== LEW que ===\"; grep -n -E '^que\\b|^-que|^sesqui' LEW_1910.txt LAT.txt | head -10",
 "description": "Grep BRT, KNT, LEW, LAT for ca/que"
}
```


### [2026-09-06T22:02:59.076Z] TOOL RESULT

```
=== BRT: search 'und' enclitic ca entry ===
2249:enkl.:  enklitisch.
3374:'sd.)  sacinte  "ija  aiwi.game  V.  5. b)  'drum,  so  —  denn',  vor  Imp., Inj.,  Konj.,  Opt  und  Inf.:  tsmca..  laibyo dat  sarim  °%a  Asm  foraSua  %wa  xra^toä ^-  53-3'  —  "^'i  ^^'  västs  (sd.)  xsmat anyö  'äa  möi  sqs/a  (sd.)  veAs  vastrya  Y. 2ij.i;  3l.iS,34-7i —  °^«  «f  ii  humayd.- tara  anAm  Vr,  72.4;  4;  ~  "'ia  tu  n9 gayasca..Rya  y,4'-S'> — "^^  »■'  sasdyai (sd.)  usia  V.57. 16.  4)  anschliessend 'und';  a)  ein  Nomen:  i^a  i  Aaiiyaisd.) nare  "'^ä  jsnayö  Y.  5_J,6  3\  b)   einen
4977:Yt.  10.  46.  a)  mit  relativischeni.  An- schluss:  °vä  (APn.)  j>ä  näiryi-  yä  fu'irahe "das  der  Frau  .  ."  N.  5^;  —  'v3.  (APf.) ^1  anyä  srävaydij  "die  andern  (näml. Gä'^Ss)  .  ."  N.46;  —  naicis  "vat  y3  spsn- iahe  Yt.i5.3t?).  3)  auf  ein  Relativum als  dessen  Korrelat,  a)  adjektivisch:  dva aurvanta  . .  aom  .  .  aurvanhm  yS  anhat äsus. .  aom  ,  .  aurvanhm  yö  , .  urvaisayat YL5.131;  /.24,  14-^9',  —  i^y  '^"J  ^'"^^ 3s  .  .  yat  mS  fravaocö  .  .  Y.ig.i;  Yt  5. 41,  Vr.  20.  i  f.*,  G.  2.8;  —  xfä^r^meä  'val .  .  yä  .  .  rämqmcä  (sd.)  dät  Y.2p.  10; °va  (IS.)  daxita  daxstavanta  yä  nditpom ßra{sA.)/raäaxsta\t.5.')^;  —  'vä(lS.)i^ wanarthii  yä  .  .  manta  .  .  Y.  33.  6 ; 'vaiiiha  drüjB  .  .  yä  .  .  upa.dvqsaiti  V, 17;  17;  —  Aaca  'vai/ihai  Jahikayäi  .  . yä  .  .  upa.baraiti  (sd.)  Yt.  17. 58;  —  nsU 'va  (APf.)  zaoira  ..  yä  ..  framthar>nii Yt5.93;  I4.\i\  —  *'va}ika  (APf.)  > va^ays  .  .  yä  .  .  anhan  Y.  2j.  1 ;  —  •; (APn.)  dämqn  . .  yi  A^nti  . .  Vr.  7.4;  — •w7(/  uroaikis  (sd.)  ya  ta  . .  didirszd  Y. 44--ii;—''*'vä  (NPf.)  dakyäve^  tyä  dura- yt^v<^uS  adärayj'  \i.6.ä,;  —  mat  'vaby5 (DP.)  daxstäbyö  ydäsa  aHrai'a  "mit  den Zeichen,  wie  ein  Priester  (sie  hat)"  V.  /j. 22.  a)  das  Substantiv  ist  aus  dem Relativsatz  heraus  zu  ergänzen:  yä  tu haßi  (sd.)  'vi  (APf'>,  näml.  asll)  yä  da alis..\.43.\.  b)  substantivisch:  'tat yäsqs  hyal  vS  istä  (sd.)  vakishm  Y.  4g. 12;  —  've  (als  AP.)  aifi  (sd.)  dat^ants . .  ysi  . .  dniihiti  Yt.  10.4s ;  45;  "*  °z'J»V aibt  ySng  dainll  nSit  Jyatius  (sÄ). .  Y.  J2. 15;  —  'valsqmca  päi^B  paniö  yim  (statt AP.)  isMiH  mhmJrufdYK.  /O.45,  4)  auf den  Inhalt  eines  Konjunktions-  oder  Re- lativsatzes, a)  adjektivisch:  'va^  ayapl>m dazdi  mi  .  .  ydha  azgm  häcayene  . .  Yt.5. 18;  130,  p.i7f.,  75.3,  77.25;—  'vaÄeca paiti  yqiiahe  ya^  he  da%ai  .  .  Yt  16. 6 f.  b)    substantivisch:    'val   h!   as/t
6926:'  stets:  x^ai''a>n  tyaf'  hacä  'müxam  taumSy.l parübartam  äha'  Bh./.14;  10,  12,  13;  — '  hacä  pamriyatJ'  hyä  "mäxain  taumä  xsä- \ydhiyä  (sd.)  äht^  Bh. /,3;^f7ia-w  tysm \  'mSxam  *gU^avä  aväsiäyam  Bh.  1.  14; 1 14.  b)  im  Aw.  a)  notwendig,  sofern !  enklitische  Kasusformen  fehlen:  kii^ü I  drujwi  nis  °mal  ä  nts  näs'ijinä  (sd.)  \.44- j  13*>;  —  xrapaiil {s^.)  'mat  hyat  aibl  Y. \40.  i*';J5.S^'.  ß)  sonst  beliebig:  dazdi i  -makfin  (statt  Dat)  tat  äyapUm  ■  .  _f«:^a I  faän . .  Yt/o.33*>;  —  xsa>röi  höi  haun-atu '  amirftätä  'mäi  sU'i  dqn  (sd.)  t^-TÜ  Uta- [yain  y.45-io9i;  4y.i'°i;  —  pfrM,l(sd.)- j  ca  na  yä  tat  'mä  (Akk.) "  "'  parst.l  V, I4J.  10"';  —  ahmäi  paoiryö  äjasat  virf- I  "kraytiS  .  .  viitahe  k>hrpa  Yt  14.  2. '■  [N. /oj:  lies  hama^  Vgl  zu  vayam. '      KompA.;  Ableit.  — iFlex.s.S42J'J>-  —  ai..ij™i:/,
11099:hochtonige  Wörter  dazwischen  stehen,  die nicht  zu  dem  mit  i'J  angeschlossenen  Skttt eil gehören.  Enklitika  trennen  nicht,  s.Y.jg.3 tSp.  569  o.),  41--  4  (Sp.  5Ö7  n.);  vgl.  Yt.  /.  i9(Sp. 573  u.).  —  3I  c'H  iwischen  iwei  verbundenen Duilen  verknüpft  nicht  diese  untereinander, sondernbeideiusunmeniUcinGlied  mit  einem oder  mehr  andern;  s.  Bthl.  BU.  /O.  268.  So  Y. 30.  II,  3/.  4,  Vr.  p.  5.  —  4>  Man  erwartete iu/rtumniafias^a  V  ffsaniühi.  —  J)  Man  ver- langte vircAuilniH  .  ,  vätäM  kyal .  .  earaii.  — <'1  5.  dazu  Cld.  KZ.  30.  545,  31.  157,  Proa. 43.  —  7>  oSäi  und  Uubyä^  gehören  als  Eweiles Glied  Eusammen,  s.  Sp.  5JÖ  m.  —  S>  Man  sollt« yat  haemim  gavafa  r"  .  .  erwarten.  —  9>  Für Stellen  wie  Y.  9.  18,  Yt.  fj.  1,  19.  67  nsw. ist  Bildung  von  Gruppen  anzunehmen,  deren Glieder  iT.  asynibetisch  aneinander  gereiht sind.  Im  Folgenden  werden  nur  diese  Gruppen berückiichiigt.  Doch  ist  begreiflicher  Weise die  Grenze  nicht  überall  mit  Sicherheit  lu bestimmen;  s.  i,  B.  Y.  5/.  7,  Sp,S7i  o.  (vgl. dagegen  Y.  44.  6),  Yt.  //.  14,  Sp.  570  m.  — ■o)  Nach  Ausweis  des  Metrums  Glosse.  — ■')  Man  tivanei  yaniyai^  xia^r^m.  —  '»)  Von denen  in  Strophe  1  d  :  yaifä  . .  die  Rede  ist. —  ij)  Normal  wäre  ainraiS  m'.  —  ■«)  Statt des  regelrechten  aSilra  aparäJim^m.  —  <i)  tä ist  enklitisch;  vgL  No,  2.
11275:einleitend,  'wie':  aä:ä  aäiä  c°  ahurd  .  . zardkiuitrim  aoax^ayaas  .  .  ahä  a'ia  c* zardi:ultrS  daiväis  sanm  vyämrvTtä  .  , dha  *az?mclt..  "so,  so  wie  Ah. . .  lehrte,  .  . so,  so  wie  Zar.  . .  entsagte,  . .  so  . .  auch ich  ..  Y.  72.  sf.  2)  enklit,  eine  parti- zipiale  Erläuterung  anschliessend:  ya>a  nö äaAqm  ..*vastS{sA.)  urvanB ..vakuts  ar^Aui (näml.  tiS  aigkaiy^  äküsc'  Shüire . . Jassn- tarn  "auf  dass  unsre  Seelen  .  .  seien  .  ., soll  uns  das  Paradies  zu  teil  werden,  in- dem wir  von  der  Offenlegung  weg  zu den  d^urischen  Räumen  gelangen"  \,6o. ii">.         [N.  A4:  lies  nSit\
14319:kyat  .  .  frqlta  Y.  43-^4-  zu  3)  /aiti aile  mihra  tava  yat  akurake  mazdä  V. 4.i.  II)  schwachtonige  (enklitische) Formen  stehen  i)  hinter  dem  ersten  Wort des  Satz-  oder  Versteils,  von  dem  sie  aber a)  durch  ein  oder  auch  zwei  andere Enklitika  getrennt  sein  können;  3)  unregel- mässig und  selten  in  andrer  Stellung. 1)  Akk,;  a)  II  imAp.;  zu  i):  a^ura^mazda äw»3ffi"  dauäa  biyl^  Bh.4.10,  16;  — tyi^  matiä  kartam,  varnavatäm  huväm Bh.4'6;  —  unsicher:  ♦•  nüram  %uväm vamavatäm    Bh.  4.  10.  b)    im   Aw.;
14351:—  Pa.!  tö;  s.  ferner  No.  i  f.,  i^i.,  17.  — '■'}Vä.:aparliimt  «berSü.;  te.  —  ')  H k.  tanfyä gegen Pt4;  IFAni./.9.  Pü.i  0 /ä.  S.N0.3.— })  Wie  No.  3.  —  4>  An  der  ParillelsUlle  Bh. 4.  17  >teht  cf'uri^maidätaiy  Ji^lä  ÜySfi, woraus  sich  für  %m/äm  die  Schwachtonigkeit ergibt;  vgl.  No.  9.  —  S)  Hd.  yavai  ä.  —  <•)  Da tai  und  lU  enklitisch  genommen  werden können. —  7)  St™  steht  hier  nicht  hinter  dem ersten  Wort  der  Verszeile,  wohl  aber  des Salses,  der  mit  tat  beginnt;  s.  No.  8.  -~ 1)  Vor  ial  ist  eine  Pause  anzunehmen;  s. Bthl.  AF.  2.  35  und  No.  7.  —  9)  ^wqm  ist hier  sicher  ebenso  schwachtonig  gesprochen worden  wie  das  Toransgehende  It;  vgl.  No.  4, 13.—  "■>  Vgl.  PiscHEL  ZDMG.jj.  714,  Dbr. AiS.  aos;  a.  No.  u  f.  —  ")  Vgl.  iStV.  33.3, wo  äal  mqm  lüm  ^bilaiyöü.  -^  > ')  Vgl.  die ParalMstellc  Y.  i.  aa,  wo  vö  statt  te.  vS  ist Gen.-DBt  undAkk.'euch'.  Wahrscheinlich  ist der  Gebraach  von  ar.  'tai  als  Akk.  durch  *^at veranlasst  worden.  —  'Sl  Schwachlonig  so  gut, wie  %u>ä  des  folgenden  Sattes;  s.  No.  9.  — 14)  Pü. :  äyiSn,  Sü.:  sampräfnuhi  \  daher  DST. 2A.  r.  24S-  19  'venue  (yaili,  localif)';  s.  No. 15.  —  '5)  Pü.:  krs  mal  estft,  SQ.:  präflo  'sli; daher  Dax.  ZA.  /.  284.  j»  'vient';  s.  No.  14.
14353:—  t9)  Die  NA.  zerlegt  falsch.  Wir  haben hier  keine  Verse.  —  '9)  Anfrällig.  Ist  vakü xh&r>m  lasammenzu nehmen?  —  ">)  Wenn man  &a.  Ha,  lai  enklitisch  nehmen  darf.
18437:g.  tat-nä  nsn. :  s.  Dntec  nar^ ♦  j.,  g.  na-  enkL  Pron.  1.  Pere.  Du.  und Plur.;  die  Formen  stehen  i)  hinter  dem ersten  Wort  des  Sau-  oder  Versteils,  von dem  sie  aber  a)  durch  ein  oder  auch zwei  andere  enklitische  Wörter  getrennt sein  können;  a)  selten  in  abweichender Stellung.  I)  g.,  j.  na  Akk.-Gen.-Dat  Du.; zu  l) :  mainya  .  .  yayä  spanyA  (sd.)  üttl mravai  yJm  angrSm  nötj  na  (Gen.)  mana . .  naSiä  varana  (sd.) . .  halaintl  Y.  45-  2 ;  — yal  na  (Akk.)  nOit  nijanat  .  .  Aaosrava Yt/5.  3i(?);  —  yai  ahi  paurvajtalmat aat  mqm  avi  nmaiiaya  (sd.) . .  *aia  *na''> (Dat)  äx/ta  (sd.)  6uyan  *yaha  *na^^  buyai hvayaonänAS  fantänö  .  .  ahmai  .  .  *fra- mainyai  (sd.)  Yt  16.  it.  II)  g.  na  Akk. Plur.;  zu  i):  il/d  nS  a/a  fa^B  .  .  aTai- /»y  (sd.)  Y.J4, 11;  —  aia  ni  %razdüm Y.34.T,  verwendet  X.$8.y,  —  ävil  na antan  ASnta  . .  rätayS  (sd.)  Y.33.  7;  — y!  na  frtsü! . . pä^g  stsSit  Y. 43 . 3 ;  46".  1 8 ;
19394:—  manS  J'ur<^tnasds  upasiam  baratuv . .  Uta  imam  dahySum  . .  pätuv  D.  4. 3 ;  — vas^i  (^urJ'mazdäkJ'  manacS  däray<^- vaAaui"D.4.2;  —  iya*  mana  kartam  utä fyc^maiy  /iS'ö*  kartam  X.7.4;  —  avam käram  .  .  hyj*  mana  naiy  gaubataiy*^ Eh.2. 6,  j,3,  14;  2.14.  zu  1  b):  J'urt^- masda  ya'ha  avaina*  imäm  bümim  *yau- d<rHm  (sd.)  pasüvt^dim  martä  fräbart^ mam  (s.  i  i  b)  . .  D.  61 4 ;  — pasavo^  dahyUui mana  abavJ'  Bh.j.  a,  4,  iz.  zu  3): kari^  hy<^  hamüi'iyc^  mana  naiy  gau- &ataiy*'>  Eh.  2.  7,  10.  b  n)  im  jAw.; zu  I  a):  Hat . ,  mana  asti  vjjaymift^m  . . attivam  asti  vJmamiiftim  Yt  /.  a;  — s.  noch  bei  a.  zu  1  b):  mana  raya  .  . pawasla  staorüta  upairi  tarn  vTcarmta Yt  5.  89;  /.  a6  (?).  zu  a):  ya%a  .  . Os  zaofff  mana  yat  ahurakt  matda  Yt ig.  8a;  V.  ig.  14;  —  ar»hu^  y3  mana yai  ahurahe  mazdä  P.  40;  —  zugleich zu  1  a):  manada  yatmm  yat  ahurahe mazda  a^rasca  P.Jp.  11)  schwach- tonige  Formen  stehen  a)  enklitisch i)  hinter  dem  ersten  Wort  des  Satz-  oder Versteils,  von  dem  sie  aber  a)  durch  ein andres  enklitisches  Wort  getrennt  sein können;  a)  hinter  einem  Praenomen; 3)  selten  in  anderer  Stellung;  b)  pro- klitisch5>;  das  hochbetonte  Wort,  an  das sie  sich  anschliessen,  hat  keine  bestimmte Stellung.  I)  Akk,;  a)  im  Ap.;  zu  a  1): avada  mam  cita  amanayJ"  Eh.  2. 6;  — y^a  mam  kame^  Bh.4.4;  D. ö. 4, 17-3)
20429:•  j.  tat,  g.  möi  Part.,  hinter  dem  ersten Wort  des  Satz(tei1)es,  von  dem  es  aber a)  durch  ein  andres  enklitisches  Wort  ge- trennt sein  kann;  wir  können  es  in  der  Über- setzung überall  weglassen,  z.  T.  aber  auch mit  'mir'  oder  durch  das  Pron.  poss. 'mein'  wiedergeben:  tmaj  mi  stävilt?m iyao^nim  .  .  v?n3inti  Yt  ly.  59;  —  ha im  baya  ahunake  vairyehe  . .  satim  patti anyaliqm  ra%wqm  Y,  jp.  5;  —  yat  tm sUHS  '.  haäntt  Yt  &  i; — vaiS .  .ySi  mSt ahm^i  siraohm  (fo«(sd.)  Y.  4:5.  5;  — yAya möi  asäl  hacä  vaAUbm  . .  valda  mazdä
21893:yantaHbyd  Y.  20. 3;  —  yülmäkim  . .  yat amflanqm  spmtanqm  ahmäifm  .  .yat  sao!- yafttqmY.t4.i,Vi.s.i,Yt3.it  3)soost; uzw.  a)  notwendig,  wenn  enklitische  Kasus- fonnen  fehlen:  Aya^  x/mä  (Instr.)  ux%aii dlätUähi  (sd)  pamrvTm  Y.43.11;  — äröi  (sd)  £1  xima  matdä  aia  akurä  . . zastaiita  (sd)  Y.50.  s;  —  3/j  dasfa  n3 iim  yamm  yS  yBsmat  parB  fravistö  (sd.) Y.68.  21.  b)  beliebig:  täis  yül  lyao- '^anäi/{sd.)  as>m  xÜmaibya  daduyi  Y. 46. 15;  —  tava  ..yaväkwti^^  ..yülmä-
21955:•  j.,  g.  'va-  enkl.  Pron.  1.  Pers.  Plur.;  die Formen  stehen  i)  hinter  dem  ersten  Wort des  Vers-  oder  SaUteils,  von  dem  sie aber  a)  durch  em  oder  auch  mehrere enklitische  Wörter  getrennt  sein  können; a)  selten  in  anderer  Stellung.  1)  g.  vh Akk.;  zu  1):  at  va  yazäi  stavas  mazdä ahurä  hadä  asä  . .  Y.50. 4;  8',  gl.  2;  — täii  vä  yasnäii  paitl  stavas  (sd.)  ayen- V-  50.  9 ;  —  mal  va  padäU  (sd.)  . .  patri- Jasai  Y.  50. 8;  —  tjm  *vä''>  ahüm  dr?g. vants  .  .  daOtä  nai^at  (sd.)  Y.  J/,  ao;  litf V,  5.  6  2 ;  —  yä  vS  .  .  *namqm  dadäl  . . hyat  vä  dadat  täis  vi  yaxamaide  V.  ^. 4; — yS  vi  mazda  ahurit  pairf.jasäiisA,) Y.  28.  a;  —  Kng  därayö  (sd.)  ySt  v  ä  daibi- sifUlY. 32.1; — yim  vh  *naeat  dänst  iti
23055:Zum  V,  '■iiarn:  —  Vü.:  fa  an  i  Shrmazd  x'a- iiiJA  varälSr  i  amik  daJie.  —  i)  NA.  11»«- t/nyi,  s.  aber  Prol,  XXVK  a.  —  »)  Vgl-  iSt. Gdn.  GlrPh.r.  31.  Docli  können  Zeile  c  und d  der  Strophe  keine  Gegenüberstellung  ent- halten, da  son»l  itatt  nä  die  nichtenklitische Form  stehen  mülsle.     iKonstr.  a.  Sp.  715  m.
23621:•  g.  vä,  j.  vo  Part.,  hinter  dem  ersten Wort  des  Satzes,  von  dem  es  aber  a)  durch ein  enklitisches  Wort  getrennt  sein  kann; kaum  übersetzbar:  yaiht  V5  masanasca  . . srayanas{sd.ya  carskirsmahl  Y .  ^8.  ^\  — aat  vB  yahm  ySi  mazdayasna  ct^qm  fra- 'iwfrtsana  V.  7.  71".  a)  tSm  xl  vS *sp3rfäa  *nivaranT  {sA.)  Y.5,9-4.
28178:—  anijai/i  zi..  ali'a  asff.itGiti/ . .  H.i.  5; V.5,42;  —  in  unrcgelmässiger  Stellung": ^wä paiti  zt  Aaxxnm  (sd.)  daiüe  vaAisttm Yt.  10.  80.  a)  im  Nachsatz:  yasca tili  tiiyas^a  sadirra  frabaral  dazat  si mqm  . .  P.  22;  —  yat  ^riilm  dali'ayasnd hnntat  ava  AB  miryjite  anamätö  sf  al^S ^■7-ZTy  39;  —  y^  anAat  ä'^rava  frä zl  dvqsaiti  .  ,  druxl  V.  5.  aS;  —  y&i  zl (s.  Anh.  2)  azim  nSil  daioyqm . .  tiärim . . AamaAe  zl  ml  iha  ayqn  .  .pairika  .  .parlit pairiirt>m(sd.)a»AvqmavaMsiiyst..ti/tryB zl  (zu  I ) . .  avqm  pairikqm  adanzayeiti  Yt ^■5*~SS-  S.  noch  Anhang.  Anhang. 3l  hinter  Konjunktionen;  nur  b)  im  jAw.; i)  yat  zi;  zu  i:  yai  zi . .  airyä  datrihävö tistryeAe . .  aiwi.sacyar)s  daitim  yasmmca . . mit  . .  Yt.  8.  56.  2)  y^i  zi,  yetU  zi (Sp.  i239f.);  zu  I):  azfm  datqm  ..  asS ramS.daitlm  (sd.) .  .yeuti  si, ,  nlit  daioyqm ..vispB  anhuS . .  airyamm  vaijS  fräsm-St V./.i;  Y.7/.is,Yt.Ä52,/j.i2;  — zu*)' yeßti  zi  mä  masyaka  .  .  yazayanta  .  .  ari mqm  az-i.baioryqm  dasanqm  aspanqm  aojs YiS.74;  II,  ff.*3,  /o.sS,'74-  gAw.  at zi  und  'yezl  sbcs.
28610:schwachtonigen  (enklitischen)  Formen, die  für  alle  Geschlechter  und  Zahlen  (doch ' s.  III)  gelten'*;  sie  stehen  hinter  dem  ersten Wort  des  Satz(teil)cs  oder  Vers  (teil  J  es,  von  ■ dem  sie  aber  (a)  durch  ein  oder  auch  zwei ' andere  Enklitika  getrennt  sein  können;! andere  Stellung  ist  selten  (Pj'\  I)  Gen.- 1 Dal.  p.  saiy,  g.  Asi,  j.  Äl,  ksi^,  sl;  den' adnominalen  Gen.  übersetzen  wir  mit  I 'sein,  ihr';  a)  Im  Ap.;  nur  auf  ein  Nomen  ' zurückweisend,  Sing.:  <^ura*ma$äa  .  . hauv  d3rayi/'va^um  xiäyähiyam  adadii' hausaiy  xsah'^am  fräbart^  Xi.4.1;  — /ravartil' . .  anayai-J  abiy  mäm  adamsaiy Uta  nsham  ulä  gaulä  .  .frajanatn  utasaiy *fsam  avajam  Bh,  2.  13;  —  ci^'a'tax- mam  .  .  anay<^  abiy  mäm  pasäva''  laiy utJ  mlham  ulä  gauia  fräjanam  uläiaiy »-s'am  avajam  Bh.  2. 14;  5.  i;  —  dadarsis nämü"  pärsa^  . .  avä^äsaiy  a%aham  Bh. j.  31  2.  7,  10;  — gaumätam  ..  ut3  tyailaiy fratamS  marüyä  anuHyä  äha''tä  Bh.  /.  13; 2.13,  j.7,8,  II.  b)  im  gAw.;  nur  Sing.; I)  auf  ein  Nomen  zurückweisend: mazdam  ahurim  al  ^^/(mask.)  vaAming äimäHl  garB  (sd.)  nTdJml  Y.  45-  8;  43-  8, 46.1z;  —  «^  spintB  at  ASi  dStnam 'kwaAmiä  dam(sd.)  ahurä  Y.48-T,  45-A',
28653:Stellen rind:  V,p.33,  t6.S.  i8.  io(s.No.  13), Y.  ig.  6,  N,  4S{f:  s-  No.  n\  N.7;  s.  noch No.  H.  —  J)  Nur  P.  4S  """1  N.  /04.  —  *)  Pii.  r e  an  i  j^is.  —  5)  Hds.  ahiaki;  Pü.:  ffön.  — *)  Hdi.  äki,  ähi;  i.  ä  No.  18.  —  7)  Im  Aind. «liide  allerdingi  das  hinter  dem  Relalivum ttehende  Wort  belont  sein  1  d»  ist  aber  - ncDD  anders  die  Überlierening  Glauben  ver- dient -  jnng,  wie  lal.  quicumque,  ubicamque uiw.  zeigen.  —  8)  So  bei  der  Annahme,  dass dal  nachgesetite  JrM  enklitisch  war;  s.  Sp. 687  0.  —  9)  Hds.  'halnaimäl.  Prolilise  ist doch  schwerlich  aninnehmen.  —  <o)  le  aus dem  vorhetgehenden  Sati  wiederholt ;  s.  No.  1.
30621:iratß  t/ dva/sj  (sd.),  h' dimä  *mfr)%yaos  \.ox\'\gt  (enklitische)  Formen;  nur  Gen.- mazistg  Y.  5^-  S ;  —  a/  a/iwa  k'  mainyüm  Dat.  ASi,  hl,  i!:  s.  Sp.  1 7  3  3  ra.  und  1 7  2  5  m. sara>uströ  i-fr^ntl (S-p.  1361  o.)  Y.  4 J.  >6;  unter  'Anhang".
=== BRT cit ===
=== KNT ca lexicon ===
5168:ula (for шй, $36.I) conj. ‘and’ (52911-00): Av. ula, Skt. ш, Gk. Hom. -úre ‘like’, pIE *ute (hardly both -@ and - in Aryan, despite Mt. MSLP 19.57-8, MB Gr. 5151). Correlative with preceding -сӣ, DB 1.66f (cf. Gk. тё xai); ша... шб ‘both ... and’ DB 1.34f, 41, 461; 2.74, 88f; 5.19f, 35; DNb 30, 37, 40f, 43, 45; XPf 19f; XPh BAL.
5376:-cé (i.e. -cd) enel. conj. ‘and’: GAv. -@, LAv. -€a, Skt. ca, Gk. тє, Lt. -que, pIE уш, ~... -cé ‘both ... and’ DB 1.65, DNb 32; cà .. . -cã ula ‘both ... and... and’ DB 1.66-7. -cé DB 1.65 ter, 66, 66f; DPd 9f; DNb 32 bis; XPh 41, 51, 54. -ca-maiy DNb 28, 51, 52 (§51).
5864:-vä encl. conj. ‘or’ (8133, $291.11); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
=== LEW que ===
LAT.txt:106:que con-grutf et in—gruG alent rien k faire avec ruo, et que
LAT.txt:233:que le fait, pour un mot, de n'avoir pas de correspondant
LAT.txt:258:que lat. cSdo ou rumfS ne se laisse rapprocher avec certitude
LAT.txt:260:que ces verbes doivent %tre d'origine indo-europ6enne.
LAT.txt:576:que les trop brfeves et trop rares indications de ce Dic-
LAT.txt:635:que nourrl d'une ferme doctrlne.
LAT.txt:820:que par un d 4 biteur"; et l'on comprend que ab ait pu parfois servir 4 intro¬
LAT.txt:1008:que 1'itymologie populaire avait rapprochis (cf .adoleo ); et l'on peut
LAT.txt:1207:que le vocalisme en est hors des alternances employdes par la morpholo-
LAT.txt:1222:que spec-ies est kspek-, etc.; on a aussi acta. Le present aceo et l'ad-
```


## [2026-09-06T22:03:09.427Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"j\\., ?g\\. c[aä]\\b\" BRT.txt | head -10\necho \"---cisca---\"\ngrep -n -E \"cisca|čisča|cis-ca\" BRT.txt | head -5\necho \"--- 'und' Partikel ---\"\ngrep -n -E \"Partikel.*'und'|'und',? ?(auch|Partik)\" BRT.txt | head -10\necho \"--- column 425 leaf ---\"\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"cisca  \\\"quisque\\\"\")\nif i<0: i=t.find('cisca')\nprint('leaf', t[:i].count('\\f'))\nprint(t[i-2500:i+300])\nEOF",
 "description": "Locate Bartholomae ča entry"
}
```


### [2026-09-06T22:03:11.333Z] TOOL RESULT

```
---cisca---
2649:•  j.  aenah'vant-  Adj.  -Gewalttat,  Frevel übend  an  — '  (Lok.):  yff  cisca  akmi  nmUne .  .  'nat^Aä  asH  masye  Y.i^.aS.
8859:gäiu*saste\t 5. 102.  a)  mit  Gen,  part: hamistayalca  .  ,  kahe  kahyäcU  drvatqm Y.  61. a,.  3)  mit  vorangehendem  Relativ und  folgendem  1)  clt  (hinter  ka-\  2)  ^a (hinter  i kay-)  'Jeder  der..,  quisquis,  qui- cunque',  nur  substantivisch;  1)  nur  gAw.: y3  dalnqm  vokB  *sänsttl  (sd.)  manatthä .  .  kas^l  Y.4p.  5;  —  «ÄJ  ahmäi  yahmai Ulla  (sd.)  iahmäicit  .  .  däyät  akurö  Y. 43- 1 ;  —  at  .  .  s?rao^  jantü  .  .  ahmäi yahmäi  vasi{%A^  Ikahmäi^i'^.  44.16;  — ^ao^anäi/.  .  pailyaogJt  {sA.)  tä  .  .  yä  Tm AuJyätSi/ (sd.)  payät  '.  käclt  (NPn.)  Y. 4tf.8.  2)  yS  lcisca'^>    ahmt   nmsne  .  .
11084:bilden,  uzw.  in  Verbindung  mit  1)  dem Pron.  intcrrog.  'kay:  cisca  "quisque"  H.  2. II   (Sp.  425  u.).  2)  demPron,  reljo-:
12404:—  aii'afitS  ahi  abatthö  tarn  yö  aAurS mazda  "V.  ig,  2q;  —  cisca  tarn  caraitis ahi  yqm..iäraitinqm..sraistqm  dädansa Vyt.57(?)*>;  — s.  noch  V.  2. 43  bei  i  und "  Bh.  4. 6,  15  bei  3.  3)  1  im  Ap.  voi dem  veraJlgemeineraden  kä  (Sp.  42a); tuvam  k3  Ayc^  aparam ..patiparsäAy'Bh. ^.6J>;  15^;  —  tuvam  kä  xsäya^iyt^  hy(^ aparam  *ahy  Bh.4, 19,  5,  14.  \  4)  sonst beliebig;  a)  an  der  Spitze  des  Satz(teil)es; o)  unmittelbar  vor  Vok.:  tvim  mazäa ahura  frs  mü  sXsä  ..Y.zS.w.  ß)  sonst: tarn  mafhanahe  pSta  nipäta  ahi  adrmqm Yt:  io.  80;  80,  29*,  V.  ig.  6,  VyL  22,  2^, —  iäm  aisqm  tbi^yatam  tum  aliqm tbalsaauhatqm  fialsä  sSndayeAiYtlo.'j6;\ 23'.  »9tJ,  78',  5-  87.  IS-  55-  b)  in andrer  Stellung;  a)  unmittelbar  vor  Vok.: aoa  nS  tarn  mi^ra  .  .  dayU  Yt.  10.  94;  Y. 37.36;  —  äatmltüm  aridvl  sUre  anakite .  .  piium  ralcaya  Yt5. 77;  —  aai  tarn sarahuitra  .  .  V.g.  12,  10.  18;  — -  3af ya/  /am  tara%uftra  .  .  V.  //.  4;  Vyt. 4-3-  ß)  sonst:  *pouru.narim  tarn  kin- näH  ..  Y.  io,  13;  —  i^a  ml  tsm  kam.- caranuha  .  .  Yt //,  60;  —  Aanalsa'  ta tarn  tat  mlzd^m  yal  ..  Y.  5p.  30;  — äa^  mqm  tQm  fiaonayeke  '^.ii.i;  V.  22. I.  9t  Vyt  13  rSt;  — •  aal  tarn  pascatta  .. V.  i".  4;  Vyt^/;  —  yat  tum  ainim  avaS- fiäiS  .  ,  H.a.  13;  — •  yaha  tarn  trftvd (sd.)  vaia/ghe  V,5. 17,  ai;  Vyt i2.
16957:i)  Villkommen  heissen',  mit  Gen.'': /rasa  fraya  vahist>tn  ä  ahüm  hnjayanti y?  . .  *sirSus!a  . .  azpmca  Al  bpnjaim  yö  .  . ahurS .  .  uäa  *äa  ti  nun  "'stracks  gehe weiter  zum  Paradies'  (so)  werden  ihn willkommen  heissen  die  Sterne . .  und  (so) werde  ich  ihn  willkommen  heissen,  ich  der Schöpfer  AAM.,  'nach  Wunsch  geh  es  dir hier,  o  Mami'"  V.  7. 52.  2)  'huldigen', mit  Gen.:  bm/ayai  ahurS  .  .  b>njay>n amisä  spMta  yeAha  (sd.)  IbArpff  huraohaya ". .  des  schöngestaltetem  Leib  huldigte j4AM.  . ."  Yt  10.  90;  —  *fraiaintlmca  .  . ye^hh  peurUsca  iftv/ayqn'^  naicisca  aitiha ydssiti  . .  "und  Nachkommenschaft  , .,  der manch  einer  huldigen  und  der  keiner wünschen  soll  .  ."  Y.6'5. 11.
--- 'und' Partikel ---
--- column 425 leaf ---
leaf 338
Smavantaslä (Sp.  567  a)  buyamä  rapsUca  tä  HS  dan- gStncS  ustäca  (ßp.  568  m.)  Y.4i-4',  —  *i)mS janhtntu  yahmat  haca  ..snatiat,.  'hriiatca (sd.)  &ia  .  .  gStd  apajasat  .  .  aß  paurva 7'aMaKyai(sd.)  ..  aidaca (sd.)  ila  ..  sadayät V.2.22— 24;  —  hö  vTsp>m  ahüm  ..va?nai .  .  darfsta  ddiat  * amir^x^äntim  vispqm ..galiqm  Yt /p.94;  —  (Vnam  ..  sqm' .  . yazamaUe  yä  ni  baraitl  yäslä  tsi  gmi  . . tä  yasamaide  Y.  38. 1 ;  —  kyatca  mSt  tnraos ..at..\. 43.12;—  prssa^a  na  ..  Y.  43- 10;  —  avavaitya  ..ya^a  im  sk  astica  im xä  avaiti..Y.i9.T,  —  *vJsqs  *tac'a'^>  i'taä Mäm^lf  . .  vJsmte  "und  diese  zwanzig Namen  .."  Yt. /.  19;  —  dasa  ..  msrfhö sayana  dva  hamina  talla  fanii  sarata  .  . V.  J.3;  2.41;' JÄ65  (/ijÄi),  YL/5.  51 ifaifa),    Y.  19.  10  f.  {fltiaica),  8.  4,    ig.  6
(yascd),  V,?.  70,  ij.4  (ymca);  —  iäsca imä  nämSnJs  "so  lauten  die  Namen" Vt  /.  15;  75.  49;  —  Hsca  caraitis  ahi yqm  ..  H.2.  io(?).  Anhang.  Ellipse ist  anzunehmen  für  gAw.:  vaidä  tat  ya ahmT  .  ,  anales  (sd)  tna  kamnafsva  (sd.) hyatlä  iamnänä  (sd.)  ahmT  "ich  weiss  das, weshalb  ich  , .  nichts  vermag;  nur  wenig Herden  sind  mein,  (deshalb  ist  es  so) und  weil  ich  nur  wenig  Leute  habe"  Y. 46. 2.  C)  In  der  Bedeutung  unsres 'auch';  ca  folgt  dem  angeknüpften  Satz- teil, bz.  dessen  erstem  Wort.  B)im  Aw.; 'auch'  hat  den  Sinn  von  i)  'ebenso,  eben- falls, nicht  minder' :  ^<«ji  mi^r>m..yazai vasram  .  .  yasäi  Aojoörpmi^a  yat  attt  . . Yt  6'.  5;  —  mai  vi  padäis{si.)  . .  paiti- fasai  .  ■  al  va  aridrahyala  n>manha  at vi  ..  AunarptatäY-SO.S;  —  tara^uänm ..hyathei  Im  caratasca{Sf.$(>$M.)aodiir?f^ä sSiS?na  vazä  V.jr.ia.  a)  Ellipse  liegt  vor in  gAw.:  vahiSta  tstii' {sA)  , .  tara%usttake .  .  yezT  hsi  dat  ayaptä  . .  ahurö . .  hvaivhf- vlm  (sd)  yaZcä  hsi  dabm  .  .  ". .  des  Z.: dass  ihm  nämlich  AA. ..  die  Herrlichkeiten verleihen  wird  . .  (So)  auch  denen,  die . ." Y,  $3.  I.  a)    'überdies,    ausserdem':
kanyä  jndat.fiüryä  . .  ya  vupa.taurvairica nqma  ".  .  3.  .  .,  die  auch  den  Namen  V. fuhrt"  Yty.  142.  3)  'sogar,  selbst', zur  Hervorhebung  eines  besondcm  Teils des  zuvor  genannten  Ganzen:  yaism  iivTs- tyinhB  (sd.)  Jsd  xldhrimca  savankqm  Y. 28,  9.  D)  M  dient  dazu,  Indcfinita  zu
bilden,  uzw.  in  Verbindung  mit  1)  dem Pron.  intcrrog.  'kay:  cisca  "quisque"  H.  2. II   (Sp.  425  u.).  2)  demPron,  reljo-:
yS vahyS ..dazd! yasca  h5i  varäi  rädat(sA.) ". .  quicunque , ."  Y.  51. 6.  3)  dem  Pron. rel.  und  dem  Pron.  interrog.'.Ji7>^:  a)y5  a/äi 'quicunque'  Y.9. 28;  usw.  (Stverz,  Sp.  426 o.).  b)yeiti  (sd.)  catica  'quo
```


## [2026-09-06T22:03:27.666Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"kva\\b.*'wo'|k[uū]\\b.*Adv.*wo|Adv\\. 'wo'\" BRT.txt | head -10\necho \"--- search kudra/kva ---\"\ngrep -n -E \"kva  |kudra\" BRT.txt | head -8",
 "description": "BRT check ku/kva 'where'"
}
```


### [2026-09-06T22:03:27.731Z] TOOL RESULT

```
9625:•  g.  (,  j.)ku'dä  Adv. 'wo?':  k'  ahmvokuül mang  xsa^rsmcä  "wo  (sonst)  ist  Gerechtig- keit und  guter  Sinn  und  Herrschgeivalt?"
9643:•  j.  ku'*a  Adv.  1)  'wie?':  k-'  nanm  asa- vatum  yaozdaküni  V.ig.12;  12*,  70.1, It.i'*,  J2,  a',  Yt.^.4',  SO.121;  —  k°  /iTs awm  Jijffnav<lni\.ig.\2,Yti~.^T.  a)mit li  (sd.)"';  i°  tg  v>rttyqn  alte  yBi  mazda- yasna  V.5.  10,  39,  45,  6.6,  36,  28,  tV,  i, 4,  73.  y-29.  35.  36.  J546.  Jö-i;  —  aal yimS  mqsta  k'  ti  as?m  vanm  k}r>naväne V.  2. 31;  22.6'.  A)  frageeinleitend,  mit Z^':  k*  ti  aae  masdayasna  aihm  ätnm aiii  baran  ava  . .  'Svie?  sollen  die  M.  das Feuer  (wieder)  hinbringen  zu  .  .?"  V.  5. 41.  z)  'wohin?*:  i°  actqm  baoiö  (sd.) jamiti  V. /j.  50;  —  i'  altdöa  , .  masyäka hqm.valnantei  . .  nanm  a^avatum  "Wohin (sva.  an  wen) . .  sollen  sich  die  Menschen wenden?  ..  An  einen  Gläubigen"  V.fj.  i.
9645:•  j.,  g.  ku'ShiÄ  Adv.  1)  'wo?,  wohin?': •^rä  ^wJ  xldisra  masdä  "wo  ist  dein Reich,  o  M.r  Y.5/.  4;  4*  (im  Wechsel mit  kB);  —  °är3  nsmdi  (sd.)  aymT  Y. 4^j.i;  —  ''^rä  (statt  LS.)  oci"»  kahmäi vanaitam  (sd.)  dadi  Y.44-I5-  a)  'ob wohl?',  frageeinleitend:   "Sz-n  6avät  hits.-
--- search kudra/kva ---
2447:lausgesprochenen)  Gegensatz;  a}  adjekti- \Tsch,  mehrfach  sva,  'dieser  mein,  unser" ahmäicä  ahuyi  manaüyäicil  'Tilr  das  Leben hier  und  für  das  geistige"  V.  40. 2 ;  —  ahyil anhSus  asti<atö  manhrahasca  Y.  43. 3 ;  J2. '3.  34-6j  45-3t4i  —  aAe.'a  anhius  .  . ■ .  manahyeheta  ankiul  Vyt  $2;  —  ahum Tütümca  gaf^anqm  yaozdatlr?m  anham dämanqm  Vi.  70. 92J  —  aisqm  atthunqm hstam  Vyt.  JO;  —  kva  ..  aiiika  zimS  "wo auf  der  Erde  hier"    V._j.i,7;  15,  18,  34,
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2550:äJffj  ti  'take  paiti  ..  V.22.2f.;  —  Da.'  aoAvo  (Stvetx.)  yal  as/tainti  Y.i^.6  \isw.; in  Verbindung  mit  anya-  Du.  (s.  i  b):  —  'tagsam  sünam  ..yimpasuiJiaurvamca.. asUm^mastrrfttqm  vispacayö*>nastr?inqm  i  V./^J.S;  —  'farahqm  urvaranqm  yat  ätri.- amqsta  fsd.)  ''i^arö.cikaya  *°le  anye  cika- ■  ciirranqm  V,4',75;  —  'ttm  ratümca  .. yatö  "wenn  einer  ,  .  und  wenn  einer  ,  .  \yim  maiaydhanmaim  A.j.3(?).  b)  sub- vcrletzt,  so  sollen  sie  dies  und  jenes  . ."  stasA\v\&c\\- 'ta(^T>.)äb3r3ta*sraosiivariza F,_jc  b)  adjektivisch:  j'iT/fl/ire'a/ara.-  vicarayaDm  "die  beiden,  der  .^.  und  der iri^yeiti  kva  "tarn  xsapan»m  . .  *vanAaiti  Sr.  .  ."  N.  jcf ;  —  cval  'te  (ADn.)  stai- "wenn  ein  Gläubiger  stirbt,  wo  weilt  asi\tiüa  bar>iis^a  ..  nasus  .,  fräsnaoiti dem  Tä^  (des  Todes)  . ."  H.  2.  i;  — yö  "..  die  beiden,  das  Bett  und  das  Polster .." . .  upairi  kunanm  (sdL)  manö  baräi  i-up^m  V.  7.9;  — ■  azim  °ta  (APn.)  zaota  zlsJi  (sd.) 'tfm  paiti  zmämm  aUariin  uri'a  kllayäi  ..  /rasrao^r?mca  /ragl>r>mca  . .  Vr._j.7; (sd.)  "wenn  einer  . .,  so  . .  während  der  —  't^m  nitamim  As'>rjm  '^rivacahim  (sd.) ganzen  Zelt  (seiner  Cberhebung)  .  ."P.  "id  minimum  Aj^/um:  triverbe"  F.  27b; J7.  a)  wo    wir   'solch'   brauchen:  yö  —  haomü  kutö  .  .  ava    'te  ahuta  .  .  "ge-
2732:(AD.)  baom  Y.7.2; —  Aa  »i?  bara  'm (AP.)  bansmaca  U.io^;  —  'masca  bam- maca  N.  7/T.;  —  *kava  °ma  (IS.)  Aava bansmana  N.  108-,  — ■  °m>m  aSaya  b^nlsm Y.62.^;   —  yü  °md  (AP.)''  asaya   barat  * V.Ä79;    —    *kva    a/Sqm  (AP.)  ^'mim^    ' paiti.barat    N. /oj;    — ■    cvat    nä    nit?ma 'mähe  patti.barS  ratufri^  "wie  viel  Brenn-    _  .  .
2960:'9Zi  46;  —  aAy3  veha  'iö  vidi  (sd.) fftanatjM  Y.4ff.  i ;  —  me/u  t/it  paiti  aiin- ttaot   "Sarshai   kva  Aisra  V.  2. 5  PüZ.  (?)
4570:—  vjfTirayru/m  ..yat  asti  °rf  ahutia  airya- mana  ". .  zwischen  dem  A/i.-  und  dem  Airy.- Gebet"  Vr.  24-i;  —  ''v  *am7sSsi!a  spmts saosyantasca  P.^f;^o,_ji(?);  —  'n  pitan i^A.)  puknmla  Yt.J0.117;  117,  116^;  — ' 'n  urvaitya  (sd.)  V.4-3— 4*;  —  ävis  iiä. "rs  hsiiiü . . rätttyl(%d.)  '^■33-T,  —  cvai  'rj *mr3us. .  "wie  viel  im  Kreis  der  Männer . ." V.5.27;  —  yim  'r»  vastnm  frajasäi  (sd.) 'V.i0.i6;i6;yd.ij.i4.  aa) unräumlich: ; \'it/iaiy()xsäydi^iyä  agarbäyam  "rimä  haina-  \ raim  "diese  9  Könige  nahm  ich  in  diesen Schlachten  gefangen"  Bh.  4. 3.  ß)  zeit-  j lieh:  *kva  altqm^aEsnmn  paiH.barat1  "r?, akuna  *airyamana  "wann  soll  man  das  1 Brennholz  herzubringen?  Zwischen  (der  | Rezitation)  des  Ah.-  und  des  .,4»>/, -Gebets"  |
4632:pataha  yat  'n  vä  aai  -w  v,l  .  ."  N. S3.  2)  Praen.  a)  mit  Akk.  'innerhalb, in,  unter,  zwischen';  a)  räumlich,  auf  die Frage  wo?  und  wohin?:  i  °r  tmä  äahyäve^ martiya''  kyi^  . .  "innerhalb  dieser  Län- der . ."  Bh.  /.  8 ;  —  I  avaiy  °r ''  didsm  frii- Aayam  {sd.)  Bh.  2, 13;  —  T;/  ja/W  (sd-) var?zäne  V.ij.iy;  —  'rt  daifiAu  pi}p?r?- tane  Yt  70.8,  J5.49;  49';  —  yS  vJräsaili 'r)  räiia  rJsmana  Yt.  7^47;  —  tiisiltm (sd.)  yim  'rp  mSurunua  büx'aimca  V.  /.  7 ; ■ —  yßi  'r)  v^rxika  *as  *mars}a  (sd.)  V. j8.  70  PüZ.;  —  'rj  sqm  asmanimca  "zwi- schen Himmel  und  'Erde"  Y.6Ä  15;  Yt. ÄS,  /O.95,  y,i3',  43,  44; — hax3or)mia , .  'n  mäti/Dtnla  Avan^a  Yt  ö.  5 ;  —  ..  */ra- hinein  (sd.)  *'r?i'>  airsatca  bammaca  H.öS; —  Vii^raymm ..yat  asH  "n  ahuna  atrya- mana  ". .  zwischen  dem  AA.-  und  dem  Airy.- Gebet"  Vr.  24.1, ;  —  -/-j  ''am?sSsca  spnitS saosyaiitas^a  P.3<i,30,ji{?);  —  'rv  pitan {zd.)  puhnmca  Yt. /0.117;  117,  116';  — °r>  urvaitya  (sd.)  ^",4.3—4*;  —  ävis  tui 'rs  Asnta . . rä/ayy(sd.)  Y._J3.7;  —  ä'at 'r.> *ii?rsus. .  "wie  viel  im  Kreis  der  Männer . ." V.5.27; — yim  'n  vastmii  fraJasäHsd.) V.j6'.i6ji6;Vd.y./4.  aa)  unräumlich: \'h/iaiyiixsilyahiyJ  agarbäyam  °r  ima  Aattia- rana  "diese  9  Könige  nahm  ich  in  diesen Schlachten  gefangen"  Bh.  4. 3,  ß)  zeit- hch:  *kva  aitqm  *agsm3m  paiti.barälf  °r) oAuna  ''airyamana  "wann  soll  man  das Brennholz  herzubringen?  Zwischen  (der Rezitation)  des  AA.-  und  des  ^;>f', -Gebets"  I
5034:•  p.  ava'dä  {'da')  '\  j.  ava'8a  Adv.  i)  'dort, da':  \ patigrabanä  näma"  vardanam  . .  "da kamaranam  akunaus  Bh,  j.  ij  7,  9,  10, 2.6— 11^  16; — imaiy  martiyä  tyaiy  *ada- kly(sA.)  'da  aha''ta  Bh.4. 18;  j.  18',  2.  3, 6,J.4, 11,5.4;  —  didä  ..  'dasim  aväjanam Bh,  /.  13;  5. 1,  J.8'';  II  —  kva  .  .  °äa  bä  , . asne  hamsrihät  "wo  .  .  ?  .  .  dort  . ."  H.  2. 20,  *Vyt.54;  Yt6'.47>  Jp- 93>  N./5,  2^'; —  ''ha  agtaha  altahe  syao%nahe  ,  .  V.  4. 50.  a)  II  halä  avadas<^'''>  'von  da  aus': kami  udapatalä  bäbirauv  dubälJ"  namä" dahyäu/  halä  av  hauv  udapatata  Bh._j. 13;  J,  11;  —  hauv  . .  aÜyavaf"  paisiya- ^uvSdiim  haiä  av'  käram  *äyasatä  hyä''- param  *aif..  Bh.j.7  I ,  a)  'dorthin,  da- hin': U  raxa  rtSma!'  vardanam . .  'da  hauv .  .  *ä//Bh._y.6;  1. 19,  2.13;  — fravaSayS
```


## [2026-09-06T22:03:30.612Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%88%D8%AA%D8%A7%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for کوتاه, including any bracketed origin tag such as [په.] or [پهلوی], and the Dehkhoda entry's etymological remarks if present."
}
```


### [2026-09-06T22:03:37.782Z] TOOL RESULT

```
# فرهنگ معین Entry for کوتاه

According to Moein's dictionary, the entry states:

"[ په . ] (ص . ) قصیر، کم طول ، کوچک"

The bracketed notation [په.] indicates a Pashto origin tag.

## Dehkhoda's Etymological Remarks

Dehkhoda's entry includes significant etymological analysis tracing the word's roots:

"در اوستایی واژه ای شبیه kutaka به معنای کوچک دیده می شود" and notes that in Pahlavi "k–tak به معنای کودک ( کوچک ) آمده است," establishing that the root *kut-* existed in pre-Islamic Iranian languages with the meaning of "smallness" or "being small."

The entry concludes that while the word appears in Chagatai Turkish, this represents borrowing from Persian rather than an original Turkish term.
```


## [2026-09-06T22:04:00.874Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AA%D8%A7%D9%87' --note 'page 288, root Kut, Wiktionary kutāh: MP kōtāh, cognate with kudak/kuček' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AF%DA%A9' --note 'page 288, root Kut, Wiktionary kudak: MP kōdak < PIr *kawta-ka-, Av. kutaka-, Edelman ESIJa IV 382' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%86%DA%A9' --note 'page 288, root Kut, Wiktionary kuček: MP kūčak < PIr *kaw-ča-ka, PIIr *kaw-/*ku-' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-k%CA%B7e' --note 'page 288, root Kwe: PIE enclitic *-kʷe and, descendants ca/ča/-que/te/-uh' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/sesqui-' --note 'page 288, Latin/English node: sesqui- < *semis-que, sesquicentennial 1875' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%A9%D9%88%D8%AA%D8%A7%D9%87/' --note 'page 288, Persian node: Mo?in and Dehkhoda on کوتاه, Av. kutaka, Phl. kotak' 2>&1 | tail -2",
 "description": "Archive web sources"
}
```


## [2026-09-06T22:04:03.349Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\ngrep -l 'empty' page-28*.json | head -3\npython3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('/home/sfmqrb/git/rishe/data/verification/page-28*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            if not n.get('words'):\n                print(f, n.get('id'), n.get('lang'), n.get('verdict'))\n                print('  ', n.get('derivation','')[:200])\nEOF",
 "description": "Check how prior pages handled empty nodes"
}
```


### [2026-09-06T22:04:06.200Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/10ce3c6182961a94.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/95f2b1cdf77dd3b3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/269f8f1f76cff5a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/85f43f0b3b227930.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6bbe15ee5a898084.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/310861213eba449a.txt
```


### [2026-09-06T22:04:08.084Z] TOOL RESULT

```
page-282.json
page-283.json
/home/sfmqrb/git/rishe/data/verification/page-280.json 4 French confirmed
   The box is a pass-through with no word printed: the intended form is French élixir, attested from the 13th c. in alchemical Latin/French texts and taken from Medieval Latin elixir, itself from Arabic 
/home/sfmqrb/git/rishe/data/verification/page-282.json 3 Hindustani confirmed
   An empty pass-through box: the Persian compound šīr-o-šakar was carried into Hindustani (Hindi-Urdu) as sīrsakar / śīrśakar, the name of the puckered striped cloth, during the Mughal period, and it is
/home/sfmqrb/git/rishe/data/verification/page-283.json 8 French plausible
   Empty pass-through box for French calibre, first attested in the mid-16th c. (perhaps already late 15th c.) in the sense 'internal diameter of a gun barrel', the form from which English caliber and Pe
/home/sfmqrb/git/rishe/data/verification/page-283.json 13 Arabic plausible
   An empty pass-through box standing for the Arabic form of the name. Arabic does have القوقاز al-Qawqāz (and the older جبل القبق Jabal al-Qabq) for the Caucasus, and it is ultimately the Graeco-Latin n
```


## [2026-09-06T22:04:16.733Z] TOOL CALL #43: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T22:04:16.775Z] TOOL RESULT

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


## [2026-09-06T22:05:29.417Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK kut small ===\"; grep -n -E 'lemma: kut|kut-.*klein|kutaka' POK_full.txt POK_01.txt POK_02.txt | head -10\necho \"=== WLD band3 kutaka/kutah ===\"; grep -n -i -E 'kutaka|kūtāh|kutah' WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt | head -10\necho \"=== AHD kut ===\"; grep -n -o -E '\\bkut-[^.]{0,40}' AHD_watkins1985.txt | head -5\necho \"=== SKT sesqui ===\"; grep -n -i 'sesqui' SKT.txt FSD_vol4.txt WEB_vol1.txt LEW_1910.txt LAT.txt | head -10\necho \"=== PHD hec ===\"; grep -n -E 'hēč|hec\\b|hyc' PHD_mackenzie.txt | head -5\necho \"=== PHD kotah ===\"; grep -n -i -E 'kotah|short' PHD_mackenzie.txt | head -8",
 "description": "Final greps for POK/WLD/AHD/SKT/PHD"
}
```


### [2026-09-06T22:05:30.936Z] TOOL RESULT

```
=== POK kut small ===
=== WLD band3 kutaka/kutah ===
=== AHD kut ===
943:kut-no- in Latin cunnus, vulva (< “sheath”):
=== SKT sesqui ===
LAT.txt:16911:digitellus a.): grande joubarbe; sesquidigitus: un doigt et deai
LAT.txt:16912:(cf. sesquipes) ; SSdigitus surnoa roaain, "qui a six doigts"; inter-
LAT.txt:24232:secher par la cuisson, cuire k sec"; cf. Caton, Agr.106,1 sesquilibram
LAT.txt:38492:Composes: semodius (v.s&mi-)} M.L.9709-10, sesqui-, tri-, decem¬
LAT.txt:46960:sesqui-pedalis )•
LAT.txt:48422:(sesqui-, sexcu- tardif); decuplus, centuplus, quincuplus, septuplus
LAT.txt:51340:7,«8 fili Potoni, sesquisenex puerum, cf.W. Schulze, Lat.Sigenn .,
LAT.txt:57129:sescuncia, sescuplus, et sesquiplex, sesquiplaris, Sesculixes, ses¬
LAT.txt:57130:quipes, sesquipedalis "d'un pied et demi", sesqueopus "un travail
LAT.txt:57131:et demi; moitie plus d^uvrage", Pl.Capt.7aS, sesquisenex (Papin.):
=== PHD hec ===
1340:axezidan ['hycytn'] = axistan.
1341:axistan, axez- ['hstn', )hyc- I M )xyst, )xyz-] rise, stand up.
5373:wihez- [wyhyc- I M whyz-] move, progress.
5374:wihez(ag) [wyhyc(k )] movement, progression.
=== PHD kotah ===
46:THE need for even a short Pahlavi-English dictionary has been
260:forms respectively. Thus OLE (= oy) is a form of shorthand for
2105:   .....-daft [dwSdpt 1] ill-breathing, short of breath.
2399: -mand [-m)nd] deficiency, shortcoming.
2524:gisnag [gInk I P gyIng] short, small.
3344:kiik [kwk'] small, short.
6126:breath damisn, wad, wen; short of --   buttock kun.
7561:sepulchre astodiin.                       short gisnag, kiik.
```


## [2026-09-06T22:05:38.698Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57110,57140p' LAT.txt\necho \"=== LAT -que headword ===\"; grep -n -E '^-?que[ ,:]|que \\(encl|enclitique' LAT.txt | head -10",
 "description": "LAT sesqui and que"
}
```


### [2026-09-06T22:05:38.766Z] TOOL RESULT

```
Le groupe de similis a un autre vocalisme.
semen: v.sero.
sSml-: demi, moitie. N'est employe que comme premier tene de
juxtaposes ou de composes du type semianimis, semideus, semiuocalis,
semiuir, etc., dont un grand nombre a.pp arti enn ent k la langue litte-
raire, et sont faits sur le modele de mots grecs en V]|xt. —, procede
de composition qui s'est surtout d^velopp^ dans la latinite imperiale.
L'i de semi- peut s'elider devant la voyelle initiale du second
terme: sem-esus, sem-uncia', sem is et semissis de *sem( i) -as (s) "moitie
de 1'unite, demi", "demi-as", monnaie de cuivre pesant six onces
(unciae); en banque "interet d'un demi pour cent par mois". Semis
est quelquefois traite comme adjectif: semissem panem Petr.(>4,lj;
le plus souvent, il est considere comme un adverbe invariable, cf.
Pali.Jan.10,3 duobus semis pedibus. II a survecu dans certains dia-
lectes italiens, cf.M.L.7811 et 7813, semissis. Semis- est r^duit
a ses- dans sestertius : — dicitur quarta pars denarii quo tempore
is decussis ualebat, i.e. dupondius et semis tertius, P.F.453,3; dans
sSsqui (de *semisque) employe seul par Cic^ron, Or.56,188, mais
seulement usit 4 dans le derive tardif sesquatus, ou en composition:
sescuncia, sescuplus, et sesquiplex, sesquiplaris, Sesculixes, ses¬
quipes, sesquipedalis "d'un pied et demi", sesqueopus "un travail
et demi; moitie plus d^uvrage", Pl.Capt.7aS, sesquisenex (Papin.):
'sesquiuolus adj. compose tardif qui d^signe 1'ecureuil; etc.
Semi- se reduit a se- par haplologie dans semodius, semestris
de sem(im) odius, sem( imj estris', sur semodius a ete forme selibra
(que Martial scande selibra) ; simbella est issu sans doute de *semi-
(li) bella > *sem(i)-bella > simbella avec fermeture de e devant1e
groupe m + b, cf. simplex de *sem-plex', de meme sinciput (v. ce mot).
A cote de semis, apparait dans les Gloss. une forme *semus, dans
semum: r)p,iTxevov CGL II 183,3, avec un derive sematum ibid. II 181,
45 et Diom.; ces formes sont confirmees par 1 'ombrien semu "medio"
=== LAT -que headword ===
106:que con-grutf et in—gruG alent rien k faire avec ruo, et que
233:que le fait, pour un mot, de n'avoir pas de correspondant
258:que lat. cSdo ou rumfS ne se laisse rapprocher avec certitude
260:que ces verbes doivent %tre d'origine indo-europ6enne.
576:que les trop brfeves et trop rares indications de ce Dic-
635:que nourrl d'une ferme doctrlne.
820:que par un d 4 biteur"; et l'on comprend que ab ait pu parfois servir 4 intro¬
1008:que 1'itymologie populaire avait rapprochis (cf .adoleo ); et l'on peut
1207:que le vocalisme en est hors des alternances employdes par la morpholo-
1222:que spec-ies est kspek-, etc.; on a aussi acta. Le present aceo et l'ad-
```


## [2026-09-06T22:06:40.959Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD hec/anything ===\"; grep -n -E '^he[cč]|hē[cč]|\\bhec\\b' PHD.txt | head -5\ngrep -n 'ec [' PHD_mackenzie.txt 2>/dev/null | head -3\ngrep -n -E 'nothing|any(thing)?, ' PHD_mackenzie.txt | head -5\necho \"=== TLM ca ===\"; grep -n -E '^ca\\b|^-ca\\b|ciy' TLM.txt | head -8\necho \"=== NYB enclitic ===\"; grep -n -E '\\-i[cč]\\b|ciyon|čē' NYB_vol2_glossary.txt | head -5",
 "description": "Check PHD, TLM, NYB"
}
```


### [2026-09-06T22:06:41.051Z] TOOL RESULT

```
=== PHD hec/anything ===
668:  -ih [)Pkyh] company, assistance.
1711: . tand [end I = M, N,...,] how many, much?; so many, much; some, a few.
5229:was [KBD < A kbyr; ws I = 1'1, N bas] much, many, enough.
5921:agriculture warz.                         any, not....., ee.
6806:hit pahikaftan, zadan.                         how many, much cando
=== TLM ca ===
225:13.  ft'itiy  Darayavaus  Xsaya^iya  naiy  aha  martiya  49)naiy Parsa  naiy  Mada  naiy  amaxam  taumaya  kasciy  hya  avam  Gau- 50)matam  tyam  magum  xsa0ram  dltam  caxriva  karasim  haca darsma"2  a-51)tarsa  karam  vasiy  avajaniya  hya  paranam  Bardi- yam  adana  avahyar-52)adiy  karam  avajaniya  matyamam  xsnasa- tiv  tya  adam  naiy  Bard-53 )iya  amiy  hya  Kuraus  pu0ra  kasciy naiy  adarsnaus  cisciy  0astana-54)iy  pariy  Gaumatam  tyam magum  yfita  adam  arasam  pasava  adam  Aura-55  )maz[d]am  pati- yavahyaiy3  Auramazdamaiy  upastam  abara  Bagayadais  56)mahya X   raucabis  0akata  ahan  ava0a  adam  hada  kamnaibis  martiyai- bi-57)s  avam  Gaumatam  tyam  magum  avajanam  uta  tyaisaiy fratama  mar-58)tiya  anush'a  ahaDta  Sika[ya]uvatis  nama4  dida Nisaya  na-59)ma  dahyaus  Madaiy  avadasim  avajanam  xsa0ram- sim  adam  adlnam  va-60)sna  Auramazdaha  adam  xsayatfiya abavam  Auramazda  xsa0ram  mana  fr-61)abara
226:14.  0atiy  Darayavaus  xsayatfiya  xsa0ram  tya  haca  amaxam ta-62)umaya  parabartam  aha  ava  adam  patipadam  akunavam adamsim  ga0a-63)va5  avastayam  yaftl  paruvamciy  ava 0a  adam akunavam  ayadan-64)a  tya  Gaumata  hya  magus  viyaka11  adam niya0rarayam  karahya  abi-65)caris6  gaiflamca  maniyamca  v‘0abai- sacaa7 *  tyadis  Gaumata  h[ya]  66)magus  adlna  adam  karam  gaflava avastayam  Parsam[c]a  Madam[c]-67)  a   uta  aniya  dahyava  ya0a paruvamciy  ava&i  adam  tya  paraba[rta]-68)m  patiyabaram  vasna
234:ca,  Foy.  Formerly  vifcubis,  Gray,  Bartholomae.  vMbis,  ed.  See  voc.
468:8.  0atiy  Darayavaus  xsaya-46)0iya  vasna  Aura[mazdaha  ap]i- maiy  aniyasciy  vasiy  astiy  karta-4T)m  ava  ahyaya  d[i]p[iy]a  naiy nipistam  avakyaradiy  naiy  n-48)ipistam  mat[ya  hya  apa]ram imam  dipim  patiparsatiy  avah-49)ya  paruv  0a [day a3  tya]  mana kartam  nais[im]  ima4  varnavataiy  d-50)uruxtam  maniyaftaiy]5
724:3.  0atiy  Xsayarsa  xsayafliya  vasna  12)Auramazdaha  imam  du- var0im  visadahyum1  13)adam  akunavam  vasiy  aniyasciy  naibam2 14)kartam  ana  Parsa  tya  adam  akunavam  15)utamaiy  tya  pita akunaus  tyapatiy  ka-16)rtam3  vainataiy  naibam  ava  visam  vasna A-17)uramazdaha4  akuma
725:4.  0atiy  Xsayarsa  18)xsaya0iya5  mam  Auramazda  patuv  uta- mai-19)y  xsa0ram6  uta  tya  man  a   kartam  uta  tyamai-20)y  pi0ra7 8 kartam  avasciy  Auramazda  patuv.
759:12)pit[20]a  mam  Auramazda  patu[21]v  hada  baga-13)ibis  uta t[22]yamaiy  kartam  uta  tyamai[23]y  14)pi0ra  Darayavahaus XShy[24]a  kartam  avasciy  15)Auramaz[25]da  patuv  hada  bagaibis
827:riy1  Mftda  Uvaja  Parflava  [Harai]-23)va  Baxtris  Suguda  Uvara- [zm]-24)is  Zranka2  Harauvatis  ©atagu[s  Gan]-25)dara  Hindus  Saka Haumavar[ka3  Sa]-26)ka  Tigraxauda  Babir[us  A]-27)0ura  Ara- baya  Mudraya  [Armina]  28)Katpatuka  Sparda  Yauna  Saka  tyai[y ta]-29)radraya  Skudra  Yauna  Takabara  Pun[tiy]-30)a4  Kusiya Maciya  Karka
=== NYB enclitic ===
262:aeürénitan [>c*lynytn'] to make ineffec- tive: bé acdrénét (sc. your work) with the explanation akartārēh-ic 6 šmāh dahét he will create ineffectiveness for you, he will make your work inefficacious 45?. — Den. of a-cär, v. car. V.s.v. axtäyisneh.
264:adak [DYN], with encl. ’DYN-m = adak-im, 'DYN-š = adak-iš etc. (DYN-n — adak-in HajB:5, v. -n); 'DYN-e — adak-ic, then, by then, at that moment; in that case, this being so: 1. at the beginning of a sentence 28°. 2975 sq. 37— 61 passim, etc.; u ~ 399. 5421; u m-ic 377; — placed after the first w. of a sentence: api-$ ~ 417-8; 5022, 4118; v. also below. — 2. ~ ka at the time when 3615. 4117. 4415, — 3. introducing the apodosis a) after hakar HajB:9-10; 19'-5 and passim; b) after ka HajB:5; 183-1? and passim; ~ ka...
267:m-ic 5525-26; han katärcihe ke hac den ākāh, ~ 6716; har martom kē ..., ~-is 909; 5 kē.. up the thread of a narrative after a lengthy gualification: pas hac matani... —-išan 4018-19; 807-5; 871-2, — OP adakiy;
333:äivenak [’dwynk'] kind, sort, species, genus 478, 3917, 7611, 8028, 9417-20, 1083.10; nature 100!4; — manner: pat han =, pat én ~ in this, in such a manner; being in such a state; thus: 1129-21, 3416, 8519; the thing (event, situation) being so, connected with ditan 21. 322, 917.27, ]]6.14, 123. 1215; with āšnūtan 814, — cë ~ A813, pat ce ~ 1620.21, 788 how?; pat ciš-ic ~ ma 708, pat hec ~ ... ne 792-3 in no way, by no means; pat han ~ ka griyét so that he is weeping 11"; — pat ~ i guaršet like the sun 441?; pat Susr ~ some- thing like a sperm 95!7; pat ēzanišn ~ by (means of) killing 103%; har 2 — in both respects 110%, — MPrs ’ywyng (S, A-H JI), yng (List 80); Paz. dina, ŠGV àinaa, Skr. v. prakära, SGV also vidhà, riti. [MPrth ”dyng, List 79, NP Ginah ‘mirror’ seems to go back to *ä- dayana-]. — Note: — NP ädinah ‘Friday’, for Islamic (yaumu-)l-jum'a, cannot be etymologically connected with ātvēnak, as Markwart has it (v. above s.v. ātvēn); it probably goes back to MIr *atēnak < Olr *ati-ayana- (OP ati-ay- ‘to go along’), ci MPrs 'dyn ‘entrance’ (S, A-H II), with secondary lengthening of the initial a-: *ādēnay ‘congregation’. — V. also ham-ātvēnak.
374:amah [LNH, Prth LN] pers. pron. Ist. p. pl. 1. cas. rect. we: —-ic... āyēm 913-14; to —-ic dāt hem we have been created by thee 397; ētšān (v.s.v. 04) ~ hem ke 5778; - an, ~ an: v. lan. — 2. cas. obl. us: a) dir. obj.: —-ic äkäh framāi kartan please let us know 11%; — martoman 11%; ~ (twice) proleptic obj. of zanišn 409-7; — b) virtual dat.: franāmišn ~ we must proceed 405; ~ ap i tē pat kar ne apāyet we have no need of your water 14?3; 191-2; — c) the agent of a pret. pass.: pas =: framāt HajB:11; HajA: 5.10 (Prth LN); ~ ētēn āšnūt ku 34, ete.; - d) i ~ our: dar i ~ 39, etc.; e) after a prep.: andar, apük, o ~. — Av. (295 sg.) gen. ahmākom, OP amāzam; MPrthPrs ’m’h; Paz. ema; NP ma. V. also -màn.
```


## [2026-09-06T22:06:48.794Z] AGENT

Now I'll write the verification file.


## [2026-09-06T22:11:40.137Z] TOOL CALL #47: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-288.json <<'JSONEOF'\n{\n  \"pdf_page\": 288,\n  \"book_page\": 258,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kut\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Proto-Iranian *kawta- 'small' (whence *kawta-ka-); no Proto-Indo-European root *kut- 'small, short' is reconstructed outside Mann\",\n      \"note\": \"The word-family is real and Iranian; the label 'Indo-European' is what over-reaches. Nourai's only reference, Mann's IEC, is in fact the ONE dictionary that sets up an IE root here: IEC p.594 'kut- (3) \\\"diminutive\\\". Variant: kūtoko- Av. cf. kutako \\\"little\\\"; Per. cf. kūtāh \\\"short\\\"; kucak \\\"little\\\"; kūdak \\\"boy\\\"', and even Mann has no non-Indo-Iranian cognate, since he himself throws out the one candidate ('Li. kūdikis, m. \\\"child\\\" seems to be a Slav. LW. fr. *xud-'). Pokorny has no root *kut- 'small' (his only kut- is *kut-no- in Lat. cunnus, semantically unrelated), Walde-Pokorny's index is silent, and Watkins/AHD has nothing. Modern Iranian etymology (Edel'man, ESIJa IV 382, followed by Wiktionary) reconstructs Proto-Iranian *kawta- 'small, diminutive', only tentatively attached to PIE *(s)kaw-. So the root box is right about the meaning and about the group of words it heads, but the reconstruction is Iranian, not securely Indo-European, and the shape *kut- is Mann's zero-grade abstraction from Av. kutaka-.\",\n      \"note_fa\": \"این خوشه واژگانی از دید ایرانی درست است ولی برچسب «هندواروپایی» گزافه است. تنها مأخذ نورایی، فرهنگ مان (IEC) ص ۵۹۴، خودْ یگانه فرهنگی است که در اینجا ریشه‌ای هندواروپایی می‌سازد و حتی او هم جز صورت‌های هندوایرانی هم‌ریشه‌ای نمی‌آورد. پوکورنی و والده‌ـپوکورنی و واتکینز چنین ریشه‌ای ندارند. ریشه‌شناسی امروزی (ادلمان، فرهنگ ریشه‌شناختی زبان‌های ایرانی، ج۴ ص۳۸۲) صورت ایرانی آغازین *kawta- «کوچک» را بازسازی می‌کند و پیوند آن را با هندواروپایی *(s)kaw- تنها با احتیاط می‌پذیرد. پس معنی و مجموعهٔ واژه‌ها درست است، اما بازسازی *kut- ساختهٔ مان از روی صورت اوستایی kutaka- است و ایرانی است نه هندواروپایی.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AF%DA%A9\",\n        \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%86%DA%A9\",\n        \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AA%D8%A7%D9%87\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"IEC:594\", \"status\": \"supports\", \"note\": \"Page number exact. IEC.txt leaf 337 carries the running head 'kurn- — kut-' and the printed numerals 594/595: 'kut- (3) \\\\'diminutive\\\\'. Variant: kūtoko- Av. cf. kutako \\\"little; Per. cf. kūtàh \\\\'short\\\\'; kucak \\\"little; küdak \\\\'boy\\\\'. (Li. kūdikis, m. \\\"child\\\" seems to be a Slav. LW. fr. *xud-)'. Nourai's root name, gloss and the whole Avestan+Persian word list come straight from this one paragraph.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW, whole text\", \"stance\": \"silent\", \"note\": \"grep -n -E 'lemma: kut' POK_full.txt returns nothing; Pokorny reconstructs no root *kut- 'small/short'. The only kut- shape in the IE literature is *kut-no- (Lat. cunnus), semantically unrelated.\"},\n        {\"src\": \"WLD\", \"where\": \"Band 3 Wortregister; Bd. I/II page files\", \"stance\": \"silent\", \"note\": \"grep -i -E 'kutaka|kūtāh|kutah' over WLD_band3.txt and WLD_Bd1_pages.txt / WLD_Bd2_pages.txt finds nothing: Walde-Pokorny never treats the Avestan/Persian family.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, appendix\", \"stance\": \"silent\", \"note\": \"The only kut- in AHD_watkins1985.txt is 'kut-no- in Latin cunnus, vulva (< \\\"sheath\\\")' (under the (s)keu- family); there is no root meaning 'small, short'.\"},\n        {\"src\": \"ARY\", \"where\": \"printed p.413 (ARY_pages.txt pdf page 412), entry «کوتاه / کوته»\", \"stance\": \"supports\", \"note\": \"Aryanpur gives کوتاه/کوته its own root-entry with cognates across Germanic/Slavic/Baltic and the footnote 'واژه‌های فارسی «کودک» و «کوچک» هم از همین ریشه‌اند', citing برهان قاطع ۱۷۲۴ — i.e. he groups exactly the three Persian words Nourai groups, and (like Nourai) claims IE status.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ku, kva, kutaka; kvataka, kautaka\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Only ONE of these five forms is attested Avestan. (a) kutaka- 'small' is genuine: Bartholomae cites it from Vidēvdād 14.5, 'maoirinąm ... kutakanąm duzaininąm' \\\"of small, ill-born ants\\\" (AiW s.vv. araēka-, maurvay-); it is the zero-grade *kut-a-ka- of Proto-Iranian *kawta-. (b) kautaka is NOT an Avestan word: it is Hübschmann's reconstruction, and he sets it up for Old Persian, not Avestan — Persische Studien no. 871 derives MP/NP kōdak 'child' by suffix -ak from *kōt = ap. *kauta-, 'zu dem das auf schwachster Wurzelstufe stehende zd. kutaka- \\\"klein\\\" gehört'. Modern work agrees with the shape (Proto-Iranian *kawta-ka- > MP kōdak, per Edel'man ESIJa IV 382) but not with the Avestan label. (c) kvataka is likewise unattested: it is Horn's reconstruction (Grundriss no. 871: 'Für kōdek ist eine Grundform *kvataka- anzusetzen (wie dō aus dva-, tō aus tvam)'), and Hübschmann rejects it outright — 'Horn's Erklärung von kodak aus *kvataka- (vom Pronominalstamm kva-, ku-?) ist mir unverständlich'. MacKenzie's Pahlavi kawādak [kw'tk'] 'young; baby' shows the shape is at least a real Middle Persian variant, but it is Middle Persian, not Avestan. (d) ku and kva ARE Avestan words, but they mean 'where?/how?/whither?', not 'small': Bartholomae has 'g. kudā Adv. \\\"wo?\\\"', 'j. kuθa Adv. 1) \\\"wie?\\\" 2) \\\"wohin?\\\"', 'j., g. kuθra Adv. \\\"wo?, wohin?\\\"', and kva likewise 'wo' (e.g. 'kva ... aiŋhā ziṇō \\\"wo auf der Erde hier\\\"'). They appear in this box only because Horn floated the pronominal stem kva-/ku- as the source of *kvataka-, a suggestion nobody has followed since 1895. So: the arrow root→Avestan is sound for kutaka-, and kautaka is a legitimate (if mislabelled) reconstruction; kvataka is a rejected one, and the gloss 'small' on ku, kva is simply wrong.\",\n          \"derivation_fa\": \"از این پنج صورت تنها یکی اوستایی گواهی‌شده است. kutaka- «کوچک» راستین است و بارتولومه آن را از وندیداد ۱۴٫۵ («maoirinąm ... kutakanąm») می‌آورد؛ این صورت ستاک بی‌درجهٔ *kut-a-ka- از ایرانی آغازین *kawta- است. kautaka واژهٔ اوستایی نیست، بلکه بازسازی هوبشمان است و او آن را برای پارسی باستان (*kauta-) می‌نهد نه اوستایی؛ ریشه‌شناسی امروزی (ادلمان) نیز *kawta-ka- ایرانی آغازین را می‌پذیرد ولی برچسب اوستایی را نه. kvataka نیز بازسازی هرن است («برای kōdek باید صورت اصلی *kvataka- نهاد») که هوبشمان آشکارا رد کرده و آن را «برای من نامفهوم» خوانده است؛ هرچند مکنزی صورت پهلوی kawādak «خردسال، نوزاد» را ثبت کرده که نشان می‌دهد این شکل در فارسی میانه واقعی است. سرانجام ku و kva در اوستا قید پرسشی به معنی «کجا؟ چگونه؟» هستند نه «کوچک»؛ حضورشان در این جعبه تنها بازتاب حدس هرن دربارهٔ ستاک ضمیری kva-/ku- است. پس ادعای بنیادی (kutaka- «کوچک») درست است اما معنی‌گذاری ku و kva خطاست و kvataka را پژوهش امروزی نمی‌پذیرد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AF%DA%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HUB:89\", \"status\": \"partial\", \"note\": \"HUB.txt leaf 99 = printed p.89, entry 871: 'Np. kutāh oder kōtah (nach dem afgh. LW. kōtah) heisst eigentlich \\\\'kurz\\\\' (nicht \\\\'klein\\\\') und ist von np. kōdak \\\\'Kind\\\\' = phl. kōtak \\\\'a child, an infant\\\\' Gl. and Ind. 201, arm. LW. kotak \\\\'der Kleine\\\\' ... zu trennen. Letzteres ist durch Suffix ak von *kōt = ap. *kauta- abgeleitet, zu dem das auf schwachster Wurzelstufe stehende zd. kutaka- \\\\'klein\\\\' gehört. Horn's Erklärung von kodak aus *kvataka- (vom Pronominalstamm kva-, ku-?) ist mir unverständlich.' The page therefore supplies Nourai's kautaka (as OP *kauta-) and kutaka-, but labels neither Avestan-plus-child, and explicitly rejects kvataka and the pronominal stem.\"},\n            {\"ref\": \"HRN:194\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 215 = printed p.194, entry 871: 'kūtāh, kūteh \\\\'klein, kurz\\\\'; kōdek \\\\'Kind, Kleines, Foetus, Embryo (AM.)\\\\'. aw. kutaka- \\\\'klein\\\\'; phlv. kūtak bezw. kōtak ... Für ködek ist eine Grundform *kvataka- anzusetzen (wie dō aus dva-, tō aus tvam u. a. m.). Zum Pronominalstamm kva-, ku-?' This is exactly where Nourai's kvataka and his ku, kva come from; Horn's own question mark shows he offered it as a guess.\"},\n            {\"ref\": \"IEC:594\", \"status\": \"supports\", \"note\": \"Mann p.594 s.v. kut- (3) gives 'Av. cf. kutako \\\"little\\\"' — the only Avestan form he cites, and he prefixes it with 'cf.', i.e. he too treats it as a comparandum rather than the etymon.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW s.vv. araēka-, maurvay- (BRT.txt ll. 5285, 20075); s.vv. kudā, kuθa, kuθra (ll. 9625, 9643, 9645)\", \"stance\": \"partial\", \"note\": \"Confirms kutaka-: 'maoirinqm kutakanqm duzaininqm V. 14.5'. Contradicts the gloss on ku/kva: 'g. (, j.) kudā Adv. \\\\'wo?\\\\'', 'j. kuθa Adv. 1) \\\\'wie?\\\\' ... 2) \\\\'wohin?\\\\'', 'j., g. kuθra Adv. \\\\'wo?, wohin?\\\\''; kva likewise appears only as the local adverb ('kva .. aiŋhā zimō \\\"wo auf der Erde hier\\\" V. 3.1'). Bartholomae has no Avestan kvataka- or kautaka-.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.51 (PHD_mackenzie.txt ll. 3265, 3323)\", \"stance\": \"partial\", \"note\": \"'kawadak [kw'tk'] young; baby; v. kodak' and 'kodak [kwtk' | M qwdk, N ~] young, small; baby'. MacKenzie's kawādak is the real form behind Horn's *kvataka-, but it is Middle Persian; MacKenzie offers no Avestan antecedent, and he has no kōtāh at all (his words for 'short' are gišnag and kūk [kwk'] 'small, short').\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt ll. 6041, 6696)\", \"stance\": \"supports\", \"note\": \"'qwdk: kōtak' and 'kōdak: kōtak' — Nyberg reads the Pahlavi spelling kwtk' as kōtak/kōdak, the direct continuation of *kawta-ka-.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"kŭtâh «کوتاه»; kŭdak «کودک»; kŭčak «کوچک»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"کودک kūdak is the clean case: Proto-Iranian *kawta-ka- > Middle Persian kōdak (spelled kwtk', MacKenzie p.51 'young, small; baby'; Nyberg reads the same graph kōtak), whence New Persian kūdak with the regular MP ō > NP ū raising and intervocalic -t- > -d- voicing; Armenian borrowed it as kotak 'the little one' (a byname of king Xosrov in Faustus of Byzantium), which dates the Middle Iranian form to the 4th–5th c. کوچک kūčak has the same base with a different suffix, Proto-Iranian *kaw-ča-ka > MP kūčak, beside MP kūč, kūk 'small, short' (MacKenzie kūk [kwk'] 'small, short'); the -č- is the palatal suffix, not a development of -t-. کوتاه kūtāh is the problem child: its -t- survives intervocalically where Middle Persian normally voices it (whence kūdak), and both Horn and Hübschmann say so — Horn: 'np. kūtāh entbehrt auffälliger Weise der Lautverschiebung', Hübschmann p.189: 'Die Etymologie von kutah \\\"kurz\\\" (s. oben p.89) ist noch nicht gefunden', and on p.89 he separates kūtāh from kōdak altogether, suggesting the Afghan (Pashto) loan kōtah kept the t. Nyberg instead analysed it as kōt + āh 'whose strength is little'. Mo'in, Dehkhoda, Aryanpur, Mann and Wiktionary all nonetheless keep the three words together, so the chart's grouping is the mainstream Persian view — but with Hübschmann's dissent on kūtāh unresolved, and the arrow drawn from an 'Avestan' box whose forms are mostly reconstructions.\",\n          \"derivation_fa\": \"«کودک» روشن‌ترین حلقه است: ایرانی آغازین *kawta-ka- > فارسی میانه kōdak (نوشتار kwtk'؛ مکنزی: «خردسال، کوچک، نوزاد») > فارسی نو کودک، با تحول قاعده‌مندِ ō فارسی میانه به ū و نرم‌شدن t میان دو واکه به d؛ ارمنی نیز آن را به‌صورت kotak «کوچک» وام گرفته که کهنگی صورت ایرانی میانه را نشان می‌دهد. «کوچک» همان ستاک است با پسوند دیگر: ایرانی آغازین *kaw-ča-ka > فارسی میانه kūčak، در کنار kūk «کوچک، کوتاه» در فرهنگ مکنزی. «کوتاه» دشواری دارد، زیرا t میان دو واکه در آن نرم نشده است؛ هرن می‌گوید «کوتاهِ فارسی نو به‌طور شگفت‌آوری دگرگونی آوایی ندارد» و هوبشمان (ص ۱۸۹) می‌نویسد «ریشه‌شناسی کوتاه هنوز یافته نشده است» و در ص ۸۹ آن را از کودک جدا می‌کند؛ نیبرگ آن را kōt+āh تحلیل کرده است. با این‌همه معین (حاشیهٔ برهان قاطع ص ۱۷۲۱)، دهخدا، آریان‌پور و ویکی‌واژه هر سه واژه را هم‌ریشه می‌دانند؛ پس گروه‌بندی نورایی دیدگاه رایج فارسی است، اما با تردید هوبشمان دربارهٔ «کوتاه».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AA%D8%A7%D9%87\",\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AF%DA%A9\",\n            \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%86%DA%A9\",\n            \"https://abadis.ir/fatofa/%DA%A9%D9%88%D8%AA%D8%A7%D9%87/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1721\", \"status\": \"supports\", \"note\": \"Page number exact: BQT vol. 3, printed p.1721 = PDF page 514 (BQT_v3_pages.txt leaf 513; neighbouring running heads ۱۷۱۳ on pdf 506, ۱۷۱۷ on pdf 510, ۱۷۲۳ on pdf 516 confirm printed = pdf + 1207). Rendered with tools/ref_page.py BQT:1721 --image. Mo'in's etymological footnote 5 on that page: «۵ کوتاه - بضم اول ( kōtāh, در قدیم kūtāh ) . اوستا kutaka- (کوچك). پهلوی kōtak (کودك). ارمنی kotak (كوچك). مرکب از kōt + ... رك: هوبشمان ۸۷۱ ... نیز پهلوی kōtāh (قصیر) ... نیبرگ گوید: فارسی kōtāh از kōt+āh ... (یعنی آنکه زور و نیرویش کم است) «نیبرگ ص ۲۰۸» ... کردی kurt/kōt (کوتاه، قصیر)». The page thus carries exactly the Avestan kutaka- / Pahlavi kōtak / New Persian کوتاه، کودک chain Nourai draws, and cites Hübschmann no. 871 = Nourai's HUB:89.\"},\n            {\"ref\": \"IEC:594\", \"status\": \"supports\", \"note\": \"Mann p.594: 'Per. cf. kūtāh \\\\'short\\\\'; kucak \\\"little; küdak \\\\'boy\\\\'' — all three Persian words of this box, with Nourai's glosses (Mann's 'boy' becomes Nourai's 'child').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 871, p.194\", \"stance\": \"supports\", \"note\": \"'kūtāh, kūteh \\\\'klein, kurz\\\\'; kōdek \\\\'Kind\\\\' ... aw. kutaka- \\\\'klein\\\\'; phlv. kūtak bezw. kōtak' — Horn puts the same three-way group (minus kūčak) under one entry, while flagging 'np. kūtāh entbehrt auffälliger Weise der Lautverschiebung'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no. 871 (p.89) and § 83 d (p.189)\", \"stance\": \"contradicts\", \"note\": \"'Np. kutāh ... heisst eigentlich \\\\'kurz\\\\' (nicht \\\\'klein\\\\') und ist von np. kōdak \\\\'Kind\\\\' ... zu trennen'; and p.189 'Die Etymologie von kutah \\\\'kurz\\\\' (s. oben p. 89) ist noch nicht gefunden. Aber die Frage bleibt noch offen, wie die nach Vokalen im Persischen überhaupt vorkommenden t (wie z. B. in kutah) zu erklären sind, da urspr. t nach Vokal der Regel nach zu d werden musste.' Hübschmann keeps kōdak in the family but takes kūtāh out of it.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p.51 and English index\", \"stance\": \"partial\", \"note\": \"Has 'kodak [kwtk' | M qwdk, N ~] young, small; baby' and 'kawadak', but no Pahlavi kōtāh; for 'short' MacKenzie gives 'gisnag, kuk' and 'kūk [kwk'] small, short'. So the Pahlavi ancestor of کودک is documented, that of کوتاه is not.\"},\n            {\"src\": \"MON\", \"where\": \"فرهنگ معین s.v. کوتاه (via abadis.ir); Dehkhoda on the same page\", \"stance\": \"supports\", \"note\": \"Mo'in tags the word «[ په . ] (ص.) قصیر، کم طول، کوچک» — [په.] = پهلوی, i.e. inherited from Middle Persian, not borrowed; Dehkhoda's article notes 'در اوستایی واژه‌ای شبیه kutaka به معنای کوچک دیده می‌شود' and that Pahlavi 'kōtak به معنای کودک (کوچک) آمده است', adding that the Chaghatai form is a loan from Persian, not the other way round.\"},\n            {\"src\": \"ARY\", \"where\": \"printed p.413, entry «کوتاه / کوته», footnote 1\", \"stance\": \"supports\", \"note\": \"'واژه‌های فارسی «کودک» و «کوچک» هم از همین ریشه‌اند' — Aryanpur groups precisely Nourai's three words and cross-refers to برهان قاطع ۱۷۲۴.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 7,\n      \"root\": \"Kwe, Qwe, Kue, Que, Kwi 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE enclitic *-kʷe 'and' (and the generalizing particles *kʷid / *kʷis built on the same interrogative-indefinite stem *kʷo-/*kʷi-)\",\n      \"note\": \"Pokorny 635-636 has the entry verbatim: 'Root / lemma: kʷe 1. Meaning: and (encl.). Note: from \\\"anyhow, somehow\\\", as also to Pron.-stem kʷo-, kʷe- ... Material: Old Indic ca, Avestan ca, ap. ca enclitic \\\"and\\\"; Lydian -k; gr. te; venet. -ke, lepont. -pe, piken. -p, Latin -que ...'. Nourai's five head-forms are transcription variants of one thing: Kwe/Qwe/Kue/Que are just ways of writing *kʷe (q = kʷ, u = w), and 'Kwi 2' covers the *kʷid/-kʷis end of the same article, which Pokorny treats in the same paragraph ('Latin quis-quam, Old Indic cit (cid), Avestan cit, ap. ciy generalization particle ... = Indo Germanic *kʷid'). Language label 'Indo-European' and gloss 'and' are both right. Modern handbooks (Wiktionary's *-kʷe, after Dunkel and Szemerényi) agree, differing only on whether *-kʷe is an old instrumental *kʷe-h₁ of *kʷis or an injunctive of *sekʷ- 'to follow'; that dispute does not touch any arrow on this chart.\",\n      \"note_fa\": \"پوکورنی در صفحهٔ ۶۳۵–۶۳۶ همین مدخل را دارد: «ریشهٔ kʷe ۱، معنی: و (پی‌بست)» با مواد سنسکریت ca، اوستایی ča، پارسی باستان -cā و لاتینی -que. پنج صورتی که نورایی در سرِ جعبه آورده تنها گونه‌های نگارشی یک چیزند (q همان kʷ و u همان w)، و «Kwi 2» به بخش *kʷid/*kʷis همان مقاله بازمی‌گردد که پوکورنی در همان بند می‌آورد (اوستایی čit، پارسی باستان -ciy). برچسب زبانی و معنی هر دو درست است. پژوهش امروزی (ویکی‌واژه به پیروی از دانکل و سه‌مه‌رنی) نیز همین را می‌گوید و اختلاف تنها بر سرِ خاستگاه دورترِ خودِ *-kʷe است که به هیچ‌یک از پیکان‌های این نمودار آسیب نمی‌زند. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-k%CA%B7e\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:635\", \"status\": \"supports\", \"note\": \"Exact. POK_full.txt, 'Root / lemma: kʷe 1 (*kʷehu-) / Meaning: and (encl.) ... References: WP. I 507 f., WH. I 309 f., II 401 f., Schwyzer Gr. Gr. II 573 ff. / Page(s): 635-636'. The same printed page 635 also carries '(s)kʷalo-s' — which is why the six redirects on this book page (Kwal, Kwalo, Kwalos → Skwalo) sit next to this entry.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"WP. I 507 f. (cited by Pokorny at the foot of the article)\", \"stance\": \"supports\", \"note\": \"Pokorny's own reference line 'WP. I 507 f.' shows Walde-Pokorny treats *kʷe at Bd. I 507-508; POK 635-636 is the 1959 revision of that article.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kʷo-\", \"stance\": \"partial\", \"note\": \"'kwo-. Also ki-. Stem of relative and interrogative pronouns ... [Pok. kʷo- 644.]' — Watkins folds the material into the pronominal stem and has NO separate entry for the enclitic *-kʷe, so AHD neither confirms nor denies Nourai's separate root box.\"},\n        {\"src\": \"KLN\", \"where\": \"Klein 1966-67 p.1425 s.v. sesqui-\", \"stance\": \"supports\", \"note\": \"'-que, \\\\'and\\\\', which is cogn. with OI., Avestic ca, OPers. ca, Gk. τε, Phryg. κε, Goth -h, Bulg., OIr. -ch, \\\\'and\\\\'.' Klein lines up precisely the Avestan / Old Persian / Latin trio that Nourai draws as three branches.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ca, ča; čiš-ca 1; čit 1\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PIE *-kʷe > Proto-Indo-Iranian *-ča by the satem palatalization of the labiovelar before the front vowel *e (the same change that gives Skt. ca, and that is still visible in the Gathic long form -cā beside Younger Avestan -ča). Bartholomae's article documents all three uses Nourai lists: the plain connective 'und', the 'auch' sense, and the indefinite-forming use — 'ča dient dazu, Indefinita zu bilden, u. zw. in Verbindung mit 1) dem Pron. interrog. ka-: cisca \\\"quisque\\\"'; hence čiš-ča 'whoever, whatever, everyone' = the interrogative čiš (nom. sg. of ka-) + enclitic -ča, e.g. 'yō cisca ahmi nmāne' Y. 19.28. čit (with -t from PIE *-d) is the parallel generalizing particle *kʷid, used chiefly after ka- (Bartholomae: 'mit vorangehendem Relativ und folgendem 1) cit (hinter ka-)'), e.g. kahmāi-cit, kas-cit. Nourai's two transcriptions 'ca, ča' are the same word in the older and newer conventions, not two words; the trailing '1' on čiš-ca and čit is his homonym index.\",\n          \"derivation_fa\": \"*-kʷe هندواروپایی آغازین در هندوایرانی آغازین بر اثر کامی‌شدن (پالاتالیزاسیون) واکِ لبی‌ـکامی پیش از واکهٔ پیشین *e به *-ča بدل شد؛ همین دگرگونی صورت سنسکریت ca را نیز پدید آورده و در اوستایی گاهانی -cā در برابر اوستایی نو -ča هنوز دیده می‌شود. بارتولومه هر سه کاربردی را که نورایی آورده ثبت کرده است: پیوندی «و»، معنی «نیز»، و ساختِ نامعین: «ča برای ساختن نامعین‌ها به کار می‌رود، از جمله با ضمیر پرسشی ka-: cisca \\\"quisque\\\"». پس čiš-ča «هرکه، هرچه» از čiš (فاعلیِ ka-) و پی‌بست -ča ساخته شده، و čit با -t از *-d هندواروپایی همان ذرهٔ تعمیم *kʷid است (kahmāi-cit، kas-cit). دو نگارش ca و ča یک واژه‌اند نه دو واژه. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-k%CA%B7e\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:635\", \"status\": \"supports\", \"note\": \"'Material: Old Indie ca, Avestan ca, ap. ca enclitic \\\"and\\\"' and, further down, 'the indefinite mode, mind intensifying e.g. Old Indie kas-ca, Avestan cis-ca \\\"wer irgend, welcher irgend\\\" ... Avestan cis-ca also \\\"whoever it be, whatever, each, each one, every\\\"' and 'Old Indic cit (cid), Avestan cit, ap. ciy generalization particle ... = Indo Germanic *kʷid'. Every word in Nourai's box is on Pokorny's page 635-636.\"},\n            {\"ref\": \"KLN:1425\", \"status\": \"supports\", \"note\": \"Page number exact: KLN_1966.txt leaf 757, calibrated from leaf 749 = printed pp.1410-11 (s.v. seersucker) and leaf 755 = p.1422 (s.v. serene), so leaf 757 = pp.1425-26. Klein s.v. sesqui-: 'fr. semi-, \\\\'half\\\\' (see semi-), and -que, \\\\'and\\\\', which is cogn. with OI., Avestic ca, OPers. ca, Gk. τε, Phryg. κε, Goth -h, Bulg., OIr. -ch, \\\\'and\\\\'.' Klein is Nourai's source for putting the Avestan and Old Persian boxes on the same chart as Latin -que.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. ča (the article whose §D is quoted at BRT.txt l. 11084, with Stellenverzeichnis at Sp. 425-426)\", \"stance\": \"supports\", \"note\": \"'D) ča dient dazu, Indefinita zu bilden, uzw. in Verbindung mit 1) dem Pron. interrog. ka-: cisca \\\"quisque\\\" H. 2.11 (Sp. 425 u.)'; the same article documents the connective ('anschliessend \\\\'und\\\\'') and the 'auch' sense, and lists čiš-ča attestations (Y. 19.28 'yō cisca ahmi nmāne', H. 2.10, Vyt. 57).\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. -cā (KNT.txt l. 5376)\", \"stance\": \"supports\", \"note\": \"'-cā (i.e. -cā) encl. conj. \\\\'and\\\\': GAv. -cā, LAv. -ča, Skt. ca, Gk. τε, Lt. -que, pIE *kʷe' — Kent explicitly writes the Gathic long -cā beside the Younger Avestan -ča that Nourai gives as two forms.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"An empty box, and empty in the printed book too: pdf p.288 (book p.258) shows a plain rectangle to the right of the Avestan box with no language header, no reference and no word, joined to it by an arrow. There is nothing to verify. From its position (the slot where Nourai normally puts the Middle/New Persian continuation of an Avestan form) he evidently meant the Iranian descendant of the enclitic — Middle Persian -(i)č, which Nyberg's glossary documents in adak-ič 'then also', amāh-ič 'us too', čiš-ič, hēč, and which survives in New Persian هیچ hič and the -ی/-چ of چه — but he left the box blank. The extraction is faithful to the page.\",\n          \"derivation_fa\": \"این جعبه در خودِ کتاب نیز تهی است: در صفحهٔ ۲۵۸ چاپی مستطیلی بی‌نام‌زبان، بی‌مأخذ و بی‌واژه در کنار جعبهٔ اوستایی دیده می‌شود. پس چیزی برای راستی‌آزمایی نیست. از جای آن پیداست که نویسنده بازماندهٔ ایرانیِ همان پی‌بست را در نظر داشته است، یعنی -(i)č فارسی میانه (در adak-ič، amāh-ič، čiš-ič، hēč نزد نیبرگ) که در فارسی نو در «هیچ» و «چه» بازمانده است، ولی جعبه را ناتمام رها کرده. خطای خوانش اسکن نیست؛ استخراج با صفحهٔ چاپی مطابق است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book (refs=None in the extraction, and the rendered page confirms the rectangle is blank).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.vv. adak, amah, āyēnak\", \"stance\": \"silent\", \"note\": \"Nyberg records the Middle Persian reflex of the enclitic throughout ('adak, with encl. ... 'DYN-c = adak-ič, then, by then'; 'amāh-ič'; 'pat čiš-ič ~ mā, pat hēč ~ ... nē in no way'), but there is no form in Nourai's box to match it against.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, e.g. s.v. kas ~-iz [-c] 'anybody'\", \"stance\": \"silent\", \"note\": \"MacKenzie writes the same enclitic -iz/-c ('kas ... ~-iz [-c] anybody, (with a negative) nobody'), again with nothing in the chart box to compare.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Old Persian\",\n          \"words\": \"câ, čâ; čiy 1\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Persian writes the enclitic conjunction with a long vowel, -cā, an Old Persian innovation beside Gathic -cā / Younger Avestan -ča; Kent's lexicon entry is exactly Nourai's box: '-cā (i.e. -cā) encl. conj. \\\\'and\\\\': GAv. -cā, LAv. -ča, Skt. ca, Gk. τε, Lt. -que, pIE *kʷe'. It is attested in the Achaemenid inscriptions from Darius on, both singly and in the correlative pair '-cā ... -cā \\\"both ... and\\\"' (DB 1.65-67, DNb 32, DPd 9f, XPh 41, 51, 54), and in sandhi forms such as -ca-maiy (DNb 28, 51, 52). čiy is the second word of the box: OP -ciy, the generalizing particle continuing PIE *kʷid, as Kent states in the grammar — 'pIE *kʷid, OP -ciy, Skt. cid, Gk. τί \\\"what\\\", Lt. quid' — and as seen in the texts in kaš-ciy, ciš-ciy, avaš-ciy, aniyaš-ciy, paruvam-ciy (Kent §130: 'OP cišciy from *kʷid-kʷid', 'avasciy from earlier *avad-cid'). The final -y is the automatic Old Persian addition to a word-final -i (Kent §105: 'OP ciy, Skt. cid, Gk. τί'). Nourai's 'câ, čâ' are again one word in two transcriptions.\",\n          \"derivation_fa\": \"پارسی باستان پی‌بست پیوندی را با واکهٔ بلند می‌نویسد: -cā، که نوآوریِ پارسی باستان در برابر -cā گاهانی و -ča اوستایی نو است. مدخل واژه‌نامهٔ کنت دقیقاً همان جعبهٔ نورایی است: «-cā پی‌بستِ پیوندی «و»: اوستایی گاهانی -cā، اوستایی نو -ča، سنسکریت ca، یونانی τε، لاتینی -que، هندواروپایی *kʷe». این صورت از داریوش به بعد در سنگ‌نبشته‌ها گواهی شده، هم تنها و هم در جفتِ همبسته «-cā ... -cā» (بیستون ۱٫۶۵–۶۷، نقش رستم b ۳۲). واژهٔ دوم، -ciy، ذرهٔ تعمیم و دنبالهٔ *kʷid هندواروپایی است («هندواروپایی *kʷid، پارسی باستان -ciy، سنسکریت cid، یونانی τί، لاتینی quid» به گفتهٔ کنت) و در kaš-ciy، ciš-ciy، avaš-ciy، paruvam-ciy دیده می‌شود؛ -y پایانی افزودهٔ خودکارِ پارسی باستان بر -i پایانی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-k%CA%B7e\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:635\", \"status\": \"supports\", \"note\": \"Pokorny 635-636 lists 'ap. ca enclitic \\\"and\\\"' in the Material section (the OCR prints it 'ap. da'), and further on 'Old Indic cit (cid), Avestan cit, ap. ciy generalization particle (z. B. Old Indic kas-cid \\\"any one\\\") = Indo Germanic *kʷid' — both of Nourai's Old Persian words.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. -cā (KNT.txt l. 5376) and §§ 87, 105, 130 (ll. 918, 1333-35, 1405)\", \"stance\": \"supports\", \"note\": \"Lexicon: '-cā ... encl. conj. \\\\'and\\\\': GAv. -cā, LAv. -ča, Skt. ca, Gk. τε, Lt. -que, pIE *kʷe. -cā ... -cā \\\\'both ... and\\\\' DB 1.65, DNb 32'. Grammar: '*kʷid, OP -ciy, Skt. cid, Gk. τί \\\\'what\\\\', Lt. quid' and 'pIE *kʷid-kʷid, OP cišciy \\\\'anything\\\\''.\"},\n            {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon, texts of DB and XPh\", \"stance\": \"supports\", \"note\": \"The inscriptional text as printed by Tolman shows the forms in situ: 'kasciy', 'cisciy', 'paruvamciy', 'aniyasciy', 'avasciy' (DB 1.49-53, 1.63; XPh 13-14, 19), i.e. the enclitic actually written on the monuments.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW, ča article, §3 'im Ap.'\", \"stance\": \"supports\", \"note\": \"Bartholomae treats the Old Persian enclitic within the same ča article and quotes Old Persian sandhi forms ('3) ča im Ap. vor dem verallgemeinernden kā (Sp. 422): tuvam kā hya aparam ...'), confirming the Avestan and Old Persian forms are one and the same particle.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"The second empty box, again blank on the printed page: a rectangle to the right of the Old Persian box, no language header, no reference, no word, reached by an arrow from Old Persian. Nothing to verify. As with node #2 the slot is where the later Persian reflex would go (Middle Persian -(i)č, New Persian هیچ hič, چه če), but Nourai left it empty; the JSON reproduces the page correctly.\",\n          \"derivation_fa\": \"دومین جعبهٔ تهی، که در صفحهٔ چاپی نیز تهی است: مستطیلی در سمت راست جعبهٔ پارسی باستان، بی‌نام زبان و بی‌مأخذ و بی‌واژه. چیزی برای راستی‌آزمایی نیست. مانند گرهٔ ۲، جای بازماندهٔ متأخرِ فارسی است (فارسی میانه -(i)č، فارسی نو «هیچ» و «چه») که نویسنده آن را پر نکرده است. استخراج با صفحهٔ چاپی مطابقت دارد و خطای خوانش نیست.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is printed in the box (refs=None; confirmed on the rendered page image of pdf p.288).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. adak\", \"stance\": \"silent\", \"note\": \"The Middle Persian continuation is well documented ('adak-ič, then, by then'), but the chart box supplies no form to test.\"},\n            {\"src\": \"KNT\", \"where\": \"Old Persian lexicon\", \"stance\": \"silent\", \"note\": \"Kent has no post-Achaemenid material; nothing in his lexicon corresponds to a blank descendant box.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"que; semi-sque\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin -que 'and' is the direct and uncontroversial reflex of PIE *-kʷe: Italic kept the labiovelar, spelled qu-, so *-kʷe > -que, exactly parallel to Oscan-Umbrian -pe/-p (with the p-treatment) and to Latin ne-que = Osc.-Umbr. nep. Pokorny 635 lists it: 'venet. -ke, lepont. -pe, piken. -p, Latin -que; ne-que = Oscan-Umbrian nep'. The second form is different in kind: 'semi-sque' is not an attested Latin word but a reconstruction, printed here without an asterisk. Ernout-Meillet s.v. sēmi- give the derivation: 'sēmis et sēmissis de *sem(i)-as(s) \\\"moitié de l'unité\\\"... Semis- est réduit à ses- dans sestertius ... dans sēsqui (de *semisque) employé seul par Cicéron, Or. 56, 188, mais seulement usité dans ... sescuncia, sescuplus, sesquiplex, sesquipes, sesquipedalis \\\"d'un pied et demi\\\"'. Klein gives the same with the syncope marked: 'L., contraction of *sem(i)sque, \\\"and a half (more)\\\", fr. semi-, \\\"half\\\", and -que, \\\"and\\\"'. So the chain is sēmis 'a half (as)' + -que 'and' > *sēmisque > (syncope of -i-, then -mis- > -s-) sēsqui-, the same reduction that gives sēstertius from sēmis tertius. Nourai's gloss 'one half more' is Klein's. Verdict plausible rather than confirmed only because the box presents a reconstructed pre-form as if it were a Latin word.\",\n          \"derivation_fa\": \"-que لاتینی «و» بازتاب مستقیم و بی‌مناقشهٔ *-kʷe هندواروپایی است: در ایتالیایی آغازین واکِ لبی‌ـکامی نگاه داشته شد و با qu- نوشته شد، درست همان‌گونه که در اسکی‌ـاومبریایی به -pe/-p بدل شد (لاتینی ne-que در برابر اسکی nep). پوکورنی در ص ۶۳۵ همین را می‌آورد. اما صورت دوم از گونهٔ دیگری است: «semi-sque» واژهٔ گواهی‌شدهٔ لاتینی نیست بلکه بازسازی است که در کتاب بی‌ستاره چاپ شده. ارنو و مه‌ییه ذیل sēmi- می‌نویسند: «sēsqui (از *semisque) که سیسرون آن را تنها به کار برده است». کلاین نیز همان را با نشان‌دادن حذف واکه می‌آورد: «لاتینی، ادغام‌شدهٔ *sem(i)sque «و نیمی (بیشتر)» از semi- «نیم» و -que «و»». پس زنجیره چنین است: sēmis «نیم» + -que > ‏*sēmisque > sēsqui-، همان کاهشی که sēstertius را از sēmis tertius پدید آورده است. حکم «با احتیاط پذیرفتنی» تنها از آن روست که جعبه یک صورت بازسازی‌شده را همچون واژهٔ واقعی لاتینی نشان داده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/sesqui-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:635\", \"status\": \"supports\", \"note\": \"Pokorny 635-636 s.v. kʷe 1 lists 'Latin -que' among the direct reflexes and adds 'compare Latin atque \\\"and in addition\\\" (ad + que) = Umbrian ap(e)'. Pokorny does not mention sesqui-/*semisque, so the second word of the box is not covered by this reference.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. sēmi- (LAT.txt ll. 57125-57131)\", \"stance\": \"supports\", \"note\": \"'Semis- est réduit à ses- dans sestertius: — dicitur quarta pars denarii ... i.e. dupondius et semis tertius, P.F. 453,3; dans sēsqui (de *semisque) employé seul par Cicéron, Or. 56,188 ... sescuncia, sescuplus, et sesquiplex, sesquiplaris, sesquipes, sesquipedalis \\\"d'un pied et demi\\\"'. Confirms both the reconstruction *semisque and that the surviving Latin form is sesqui-, not *semisque.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966-67 p.1425 s.v. sesqui-\", \"stance\": \"supports\", \"note\": \"'sesqui-, combining form meaning \\\\'one half more\\\\'. — L., contraction of *sem(i)sque, \\\\'and a half (more)\\\\', fr. semi-, \\\\'half\\\\' (see semi-), and -que, \\\\'and\\\\'.' Nourai's gloss 'one half more' is Klein's wording verbatim.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde 1910, searched for the headwords que / sesqui\", \"stance\": \"silent\", \"note\": \"grep -n -E '^que|^sesqui' LEW_1910.txt returns nothing usable; the 1910 OCR does not yield the entry, so no independent confirmation from Walde on disk.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"sesqui-; sesqui centennial\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English sesqui- is a learned borrowing straight from the Latin combining form: taken over unchanged into scientific and chronological English (sesquipedalian, sesquioxide, sesquicentennial), with the meaning 'one and a half times, one half more' inherited intact from Latin sesqui- < *sēmisque. Klein: 'sesqui-, combining form meaning \\\"one half more\\\". — L., contraction of *sem(i)sque ...' and 'sesquicentennial, adj., pertaining to a century and a half; n., the one hundred and fiftieth anniversary. — Compounded of sesqui- and centennial'. The English compound is American and datable: first attested 1875, in a notice of a 'Sesqui-Centennial gathering' of the descendants of Pennsylvania settlers, as a noun from 1880 (of Baltimore's anniversary); the rival form sesquicentenary appears 1896 for Princeton. Note the chart prints 'sesqui centennial' as two words; the word is written solid (or hyphenated in the earliest attestations), and Klein has it solid — a typographic slip in the book rather than a claim about the language.\",\n          \"derivation_fa\": \"پیشوند sesqui- در انگلیسی وام‌واژه‌ای دانشورانه است که یکراست از صورت ترکیبی لاتینی گرفته شده و بی‌هیچ دگرگونی آوایی در واژه‌های علمی و تقویمی به کار می‌رود (sesquipedalian، sesquioxide، sesquicentennial)، با همان معنی «یک‌ونیم برابر، نیمی بیشتر». کلاین می‌نویسد: «sesqui-، صورت ترکیبی به معنی \\\"نیمی بیشتر\\\" — لاتینی، ادغام‌شدهٔ *sem(i)sque» و «sesquicentennial ... مرکب از sesqui- و centennial». این ترکیب انگلیسی زادهٔ آمریکاست و نخستین گواهی آن به سال ۱۸۷۵ بازمی‌گردد («گردهمایی Sesqui-Centennial» نوادگان مهاجران پنسیلوانیا) و از ۱۸۸۰ همچون اسم به کار رفته است. تنها نکتهٔ خرد آنکه کتاب «sesqui centennial» را جدا چاپ کرده، حال آنکه واژه پیوسته نوشته می‌شود؛ این لغزش چاپی است نه ادعای زبانی. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/sesqui-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1425\", \"status\": \"supports\", \"note\": \"Page exact (KLN_1966.txt leaf 757 = printed pp.1425-26; calibrated against leaf 749 = p.1410-11 s.v. seersucker and leaf 755 = p.1422 s.v. serene). Both of Nourai's English words stand there: 'sesqui-, combining form meaning \\\\'one half more\\\\'. — L., contraction of *sem(i)sque, \\\\'and a half (more)\\\\'...' and 'sesquicentennial, adj., pertaining to a century and a half ... Compounded of sesqui- and centennial.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"grep -i 'sesqui' SKT.txt returns nothing; Skeat's concise edition has no sesqui- entry, so it neither supports nor contradicts.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, vols on disk\", \"stance\": \"silent\", \"note\": \"grep -i 'sesqui' over FSD_vol4.txt and WEB_vol1.txt returns nothing (the relevant alphabetical stretch is not in the volumes held locally).\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.vv. sesqui-, sesquicentennial, sesquipedalian, p.1425\", \"stance\": \"supports\", \"note\": \"Klein also gives the sibling formation 'sesquipedalian ... fr. L. sesquipedalis ... sesqui- and pedalis', showing the combining form is productive in English exactly as the chart says.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-288.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 288",
 "description": "Write and validate page-288.json"
}
```


### [2026-09-06T22:11:42.776Z] TOOL RESULT

```
JSON OK
nodes verified: 8/8
node verdicts: {'disputed': 1, 'plausible': 2, 'confirmed': 3, 'unverified': 2}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'partial': 1, 'supports': 9, 'not_checked': 2}
books consulted: {'partial': 3, 'supports': 12, 'contradicts': 1, 'silent': 7} | by book: {'BRT': 3, 'PHD': 3, 'NYB': 3, 'KNT': 3, 'KLN': 2, 'HRN': 1, 'HUB': 1, 'MON': 1, 'ARY': 1, 'TLM': 1, 'LAT': 1, 'LEW': 1, 'SKT': 1, 'FSD': 1}
```


## [2026-09-06T22:11:52.617Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntail -6 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url'), '->', d.get('file') or d.get('path'))\n\"\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg288.png data/verification/sources/refs/ocr/BOOK/288.png\nls -la data/verification/sources/refs/ocr/BOOK/288.png",
 "description": "Verify archived URLs and copy page image"
}
```


### [2026-09-06T22:11:54.603Z] TOOL RESULT

```
https://archive.org/download/persischestudie00hbgoog/persischestudie00hbgoog_djvu.txt -> data/verification/sources/web/393ceb6e058071c1.txt
https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D9%86%D9%87 -> data/verification/sources/web/ccde76dd87c36607.txt
https://www.etymonline.com/word/penalty -> data/verification/sources/web/fff60cb0f7522ebe.txt
https://archive.org/download/altiranischeswr00bartgoog/altiranischeswr00bartgoog_djvu.txt -> data/verification/sources/web/eed804f5e79019df.txt
https://en.wiktionary.org/wiki/%D5%BA%D5%A1%D6%80%D5%AB%D5%BD%D5%BA -> data/verification/sources/web/835f8a8c4e4812ed.txt
https://en.wiktionary.org/wiki/%CF%80%CE%BF%CE%B9%CE%AD%CF%89 -> data/verification/sources/web/9186adca41a977f7.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 53847 Sep  6 18:11 data/verification/sources/refs/ocr/BOOK/288.png
```


## [2026-09-06T22:12:00.742Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in '%DA%A9%D9%88%D8%AA%D8%A7%D9%87' '%DA%A9%D9%88%D8%AF%DA%A9' '%DA%A9%D9%88%DA%86%DA%A9' 'k%CA%B7e' 'sesqui' 'abadis.ir/fatofa'; do\n  printf '%s: ' \"$u\"; grep -c \"$u\" data/verification/sources/web/index.jsonl\ndone\ngrep -o '\"url\": \"[^\"]*\"' data/verification/sources/web/index.jsonl | grep -E 'kutah|sesqui|abadis|k%CA%B7e|%DA%A9%D9%88' | tail -10",
 "description": "Check index for new URLs"
}
```


### [2026-09-06T22:12:02.365Z] TOOL RESULT

```
%DA%A9%D9%88%D8%AA%D8%A7%D9%87: 2
%DA%A9%D9%88%D8%AF%DA%A9: 1
%DA%A9%D9%88%DA%86%DA%A9: 1
k%CA%B7e: 4
sesqui: 1
abadis.ir/fatofa: 273
"url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%D9%BE%D9%87%D8%B1/"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7ep-"
"url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%B1"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7ey-"
"url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AA%D8%A7%D9%87"
"url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AF%DA%A9"
"url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%86%DA%A9"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-k%CA%B7e"
"url": "https://www.etymonline.com/word/sesqui-"
"url": "https://abadis.ir/fatofa/%DA%A9%D9%88%D8%AA%D8%A7%D9%87/"
```


## [2026-09-06T22:12:20.180Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-288.json` written; `python3 tools/verify_check.py 288` reports **8/8 nodes, 0 PROBLEM lines**.

**Page 288 (book p. 258) — 2 real entries (Kut, Kwe) + 6 redirects skipped**
- Node verdicts: confirmed 3, plausible 2, disputed 1, unverified 2 (the two genuinely blank boxes)
- Root verdicts: Kut = plausible, Kwe = confirmed
- Ref checks: supports 9, partial 1, not_checked 2 (the two blank boxes carry no refs)
- Books consulted: 14 (BRT, PHD, NYB, KNT, KLN, HRN, HUB, MON/Dehkhoda, ARY, TLM, LAT, LEW, SKT, FSD)

**Disputed**
- *Kut* → Avestan node #1 (`ku, kva, kutaka; kvataka, kautaka`): only `kutaka-` is attested Avestan (Vd. 14.5, Bartholomae). `kautaka` is Hübschmann's Old Persian `*kauta-`, `kvataka` is Horn's reconstruction which Hübschmann calls "mir unverständlich"; `ku`/`kva` are Avestan interrogative adverbs "where/how", not "small".

**Other flags (not `disputed`, but worth the owner's eye)**
- Root *Kut* marked plausible: IEC (Mann) p.594 is the **only** book that reconstructs an IE root here; Pokorny, Walde-Pokorny and Watkins are silent, and modern work (Edel'man ESIJa IV 382) makes it Proto-Iranian `*kawta-`, not PIE.
- Persian node #2 plausible: Hübschmann p.89/189 separates کوتاه from کودک and calls its etymology "noch nicht gefunden" (unvoiced -t- after a vowel is irregular); Mo'in/Dehkhoda/Aryanpur/Mann keep the three together.
- Latin node #5 plausible: `semi-sque` is a reconstruction (*sem(i)sque, Klein; *semisque, Ernout-Meillet s.v. sēmi-) printed without an asterisk.

**Extraction errors: none.** Both empty boxes (#2, #4) are blank on the printed page — verified against the rendered image, copied to `data/verification/sources/refs/ocr/BOOK/288.png`. The book prints "sesqui centennial" as two words (book's typography, not a misread).

**Reference-locator note for the owner:** two offsets in `refs_online.json` are wrong and cost time — IEC is `leaf ≈ p/2 + 40` (leaf 337 = pp. 594-595, running head "kurn- — kut-"), not `p/2 + 15`; and KLN_1966's anchor "leaf 748 = p.1469" is off by ~30 leaves (leaf 749 = pp. 1410-11 s.v. *seersucker*, leaf 757 = pp. 1425-26 s.v. *sesqui-*). With the corrected offsets, IEC:594, KLN:1425 and BQT:1721 all turn out exact.
