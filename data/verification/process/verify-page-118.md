# Verification process log — verify-page-118


## [2026-09-05T18:01:14.881Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 118 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-118.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-118.json. Write /home/sfmqrb/git/rishe/data/verification/page-118.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 118` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T18:01:16.511Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T18:01:17.181Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T18:01:17.200Z] TOOL RESULT

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


## [2026-09-05T18:01:17.533Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-118.txt"
}
```


### [2026-09-05T18:01:17.600Z] TOOL RESULT

```
1	=== PDF page 118 (book page 88) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Deph : to stamp  (refs POK:203)
4	#1 (parent #0) [Greek] refs=AHD | diphtera : prepared hide, leather used to write on | NOTE: BQT:870 indicates that this word may have been derived from Sumerian "Dub".
5	  #2 (parent #1) [Arabic] refs=HJB:329; KLN:487 | daftar : record, record book
6	    #3 (parent #2) [Persian] refs=BQT:869 | daftar «دفتر» : record book
7	  #4 (parent #1) [French] refs=KLN:452 | diphterie : membrane, a lung disease
8	    #5 (parent #4) [Persian] refs=MON:1593 | dîfterî «دیفتری» : diphtheria
9	    #6 (parent #4) [English] refs=AHD | diphtheria
10	  #7 (parent #1) [Latin] refs=AHD | litera : the text written on animal skin, letter
11	    #8 (parent #7) [English] refs=None | letter, literature
12	
```


## [2026-09-05T18:01:34.221Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-118.json && echo ---- && ls data/verification/ | head -50 && echo ---- && ls data/verification/sources/refs/ | head -80"
}
```


### [2026-09-05T18:01:34.279Z] TOOL RESULT

```
{
  "pdf_page": 118,
  "book_page": 88,
  "entries": [
    {
      "root": {
        "name": "Deph",
        "lang": "Indo-European",
        "refs": "POK:203",
        "gloss": "to stamp"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {
              "translit": "diphtera",
              "gloss": "prepared hide, leather used to write on",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "BQT:870 indicates that this word may have been derived from Sumerian \"Dub\".",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "HJB:329; KLN:487",
          "words": [
            {
              "translit": "daftar",
              "gloss": "record, record book",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:869",
          "words": [
            {
              "translit": "daftar",
              "gloss": "record book",
              "script": "دفتر"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بشوی اوراق اگر همدرس مائی - که درس عشق در دفتر نگنجد",
            "poet": "Hâfez"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "French",
          "refs": "KLN:452",
          "words": [
            {
              "translit": "diphterie",
              "gloss": "membrane, a lung disease",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1593",
          "words": [
            {
              "translit": "dîfterî",
              "gloss": "diphtheria",
              "script": "دیفتری"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "diphtheria",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "litera",
              "gloss": "the text written on animal skin, letter",
              "script": null
            }
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
            {
              "translit": "letter, literature",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
----
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
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
----
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


## [2026-09-05T18:01:36.267Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','HJB','KLN','BQT','MON','WLD','IEC','SYN','SKT','FSD','WEB','FVQ','AFM','PLA','LKT','AID','DEV','PHN','ARY','HRN','HUB','NYB','PHD']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-05T18:01:38.032Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
```


## [2026-09-05T18:01:43.969Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','HJB','KLN','BQT','MON','WLD','IEC','SYN','SKT','FSD','LKT','AID','DEV','PHN','ARY','LAT']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k,'| local:',v.get('local_file'),'| offset:',v.get('page_offset'),'| hint:',str(v.get('lookup_hint'))[:300])\n\""
}
```


## [2026-09-05T18:01:44.587Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"dep-\" POK_full.txt | head -30"
}
```


### [2026-09-05T18:01:45.945Z] TOOL RESULT

```
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== HJB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt | offset: leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== WLD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== LKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== AID | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt | offset: leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start; grep -n '^Word'.
== DEV | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt | offset: leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start.
== PHN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt | offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
== ARY | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== LAT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
```


### [2026-09-05T18:01:45.992Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T18:01:49.139Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: de\" POK_full.txt | head -40; echo \"=== page 203 search\"; grep -n \"Page(s): 203\" POK_full.txt | head"
}
```


### [2026-09-05T18:01:49.210Z] TOOL RESULT

```
8831:lemma: del-5\ "long': Baltic with unexplained o'-loss (see below): Lithuanian ilgas, f. ilga, 
8851:Root/ lemma: digh-\ "goaf derived from a zero grade of Root/ lemma: dei§h-\ "to prick; 
8853:tick'. From the older root Root/ lemma: deigh-: "to prick; tick' derived Root/ lemma: aig-\ 
8945:languages. The phonetic shift da- > zero'xs a common Baltic. Compare Root/ lemma: del- 
16740:Root / lemma: deigh- 
16762:Root / lemma: deiR- 
16839:Root / lemma: dei-1, deia-, di-, dia-{*sthei- : zdhei-) 
17099:Root / lemma: deia-2{dia- dia- dh) 
17142:Root / lemma: de/c-l 
17247:as Latin dexter, -tra, -trum is a suffixed form of old PIE Root / lemma: deR-1 : "to take'. The 
17258:Root /lemma: deR-2{\ doR-, deR-) 
17312:Root/ lemma: deRn^, deRrp-t, deRu- {* due-RrQ-tj\ ten' is an extended Root/ lemma: dud(u) 
17456:Root / lemma: de/-1 
17499:Root / lemma: del-2 
17534:Root / lemma: del-3{dol^, dela- 
17677:Root / lemma: del-4 
17699:Root / lemma: del-5 
17796:Root / lemma: demel- 
17881:Root / lemma: dem-, dema- 
17966:It is a common trait of alb. and Lithuanian to drop the initial da- as in Root/ lemma: del-5\ 
17987:Root / lemma: dem-, derna-: "to build; house' derived from Root/ lemma: ghei-2. ghi-: 
17999:Root / lemma: denR- 
18005:Root/ lemma: denR-\ "to bite' derived from lllyrian derivative of Root/ lemma: gerrio'^-, 
18047:Root / lemma: dens-1 
18102:Root / lemma: dens-2 
18130:Root / lemma: deph- 
18146:It seems that Root/ lemma: deph-\ "to stamp, push' derived from Root/ lemma: d^ab^^-/, 
18154:Root / lemma: deic!^- 
18198:Root / lemma: der(ep)- 
18204:The Root/ lemma: der(ep)-\ "to see, *mirror' derived from Root/ lemma: deii(-\ "to look'. 
18216:Root / lemma: dera-, dra- 
18239:Root / lemma: dergh- 
18264:Root / lemma: deiic- 
18272:Root / lemma: deii(- : to look derived from Root / lemma: gher-3 und ghere-, ghre- : to 
18323:Root / lemma: der-1{\ dor-, deT-) or dor-: dar- 
18343:Clearly Root/ lemma: der-1{. dor-, deT-) or dor-, dor-: "hand span' derived through Root/ 
18349:derived from truncated ghesor. The source of Root / lemma: der-1 {. dor-, der-) or dor-: 
18377:meaning two hands. That means both Root/ lemma: der-1 {. dor-, der-) or dor-, dor-: 
18476:Alb. proves that from Root / lemma: der-, heavy basis dera-, dre-\ "to cut, split, skin' 
18538:Root / lemma: deru- doru-, dr(e)u-, drou- dreuQ- : dru- 
=== page 203 search
18152:Page(s): 203 
18383:Page(s): 203 
18413:Page(s): 203-204
```


## [2026-09-05T18:01:49.588Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==211 || NR==212' POK_01.txt | head -80"
}
```


### [2026-09-05T18:01:51.248Z] TOOL RESULT

```
w.,  7t(xvSa(.idTü)Q  ,Allbezwinger', der.  dfiarög  , gebändigt'  (^dm-tös),  hom.  äS(.irjTog  und  ddt.irjg^  -fjTog  ,unge- bändigt,  unverheiratet'»  ion.  Perf.  deöf.ir^^ai^  öixTjTt^  , Bändiger',  öfÄ^oig .Bändigung,  Zähmung';
Formen  mit  Wurzelvokal  o  fehlen  dem  Gr.;
200
lat.  domo  (*domä-iö  =  damäydti),  domäs  {*domä-si  =  ahd.  zamös)  ^^IJ dige,  zähme*,  Perf.  domul  (aus  *dom9-uai),  Partiz.  domitus  (nach  domx und  domitor  aus  *dmätos,  idg.  *c2m-^o-5  umgebildet),  domitor  ,Bezähmei (==  ai.  damitdr-)]  domitus,  -üs  m.  , Bändigung'  (vgl.  ai.  damitvä)]
air.  damnaim  ,binde  (fest),  bändige  (Pferde)',  Verbalnom.   damnad  u^H domnad  (wohl  =  gr.  ödfirrj^n)]  lautliche  Vermischung  mit   damnaim  a^J lat.  damnö,   der  wohl  auch   das  unlenierte  m  des  Partiz.  dammainti  entS Sprüngen   ist;    air.    dam-   ,sich    fügen,    erleiden,    gewähren'    (z.  B.    daimi^ , gesteht  zu'  Avohl  =  ai.  dämydti,  komponiert  ni-daim  _,non  patitur'j  Pei-f dämair  aus   Dehnst.   *döm-)j  mit  acZ-  ,gestehen'  (z.  B.  3.  PI.  ataimet)j  mj^ /o-  , erleiden'  (z.  B.  1.  Sg.  fo-daimim\  cymr.  addef,  bret.  aHsav  ,gestehen' acymr.    ??i    ceiw    guodeimisauch    Gl.    ,non    bene    passae',    ncymr.    go-ddef ,leiden,  erlauben',  corn.  gothaf  , ertragen',  bret.  gouzafiv,  gouzav  ds.  (aber cymr.  dofi  , zähmen',  acymr.  dometic  ,gezähmt',  ar-domaul  ,gelehrig',  cymr. döfj  bret.  cZq^, zahm'  stammen  aus  lat.  domäre,  so  daß  einheimische  Formen mit  0  dem  Kelt.  fehlten);
got.  ga-tamjan,  anord.  temja,  ags.  temian,  mnd.  temmen,  ahd.  zemmen , zähmen'  (Kaus.  *domeiö  =  ai.  damdyati)]  ahd.  zamön  ds.  (=  lat.  domä-reY anord.  tamr,  ags.  ^aw,  ahd.  zam  ,zahm'  (unklar,  ob  Rückbildung  aus  dem Verbum,  oder  ob  die  pass.  Bed.  aus  , Zähmung  =  Gezähmtes*  erwachsen ist,  so  daß  in  geschichtlichem  Zusammenhang  mit  ai.  ddma-h  »Bändi- gung').
Wegen  ai.  damya-  ,zu  zähmen'  und  ,juuger  Stier,  der  noch  gezähmt werden  soll'  und  wegen  gr.  da^ctXrig  einerseits  ,bezwingend,  bändigend' (^'Eqojg,  Anakreon),  andrerseits  ,junger  (noch  zu  zähmender)  Stier*,  avozu daf-idlr]  ,junge  Kuh',  ödixaXiq  ,ds.*;  auch  ,junges  Mädchen*,  dd^aXog  ,Kalb', ist  wohl  alb.  dente,  dhente,  ^q^.  dhent  , Kleinvieh,  Schafe'  {*dem-tä  oder *dem-to-Sj  bzw.-  *dom-tä,  -tos),  dem  ,Rind,  junger  Stier'  (=  
ai.  damya-\ sowie  auch  gall.  GN  Damona  f.  und  air.  dam  , Ochse'  (*damos),  dam allaid  , Hirsch'  (,*wilder  Ochse'),  sowie  cymr.  dafad^  a.C0Tn.  dauat,  bret. daTwat  , Schaf  (dann  =  gr.  ä-dd^aTog)  anzureihen  (ursprgl.  Bezeichnungen gezähmter  Horntiere);  lat.  damma  oder  däma  ist  wohl  aus  dem  Kelt.  oder anderswoher  entlehnt;  unklar  ist  ags.  da  f.  ,Reh'  (daraus  acorn.  da  ,dama'), engl,  doe,  alem.  te  ds.,  vgl.  Holthausen  Altengl.  etym.  Wb.  68;  aus  afrz, daim  , Damhirsch'  stammt  bret.  devi  ds.;  germ.  Lehnformen  s.  bei  Falk- Torp  u.  daadyr  m.  Lit.;  entsprechend  niederösterr.  zamer,  zamerl  ,junger Ochs'  (Much  ZfdA.  42,  167;  vorgerm.  *a  oder  *o?).
Hitt.  da-ma-a§-zi  ,bedrängt',  Prät.  3.  PI.  ta-ma-a^-sir,  Pedersen  Hitt 95  f.
WP.  I  788  f.,  WH.  1  367  f.,  861,  Meillet  BSL.  33,  110.        .         .      .
201
Wurm'?
-gpidaur.  ösf^isXiag  f.  Akk.  PL,  de^ßXsTg'  ßdelXai  Hes.;
vielleicht  alb.  dhemje  ,Raupe'  (kann  für  *dhemlie  stehen),  dhemize,  dhimize fleischmade'. *   WP.  I  790.
rfcui-  .beißen'.
\i.  ddsati  , beißt'  (*dnketi),  Perf.  daddrrisa  (danach  auch  ein  Präs.  ddmsati), '  Kaiis.  dam§dyate  , macht  beißen',  ddmsa-h  ,Biß,  Bremse*,  damiana-m  ,das Beißen',  damstra-h,  ddmsträ  , Spitzzahn,  Fangzahn'  =  av.  tiii-dqstra-  ,mit scharfem  Gebiß,  Gezähn'  (für  -dqStra-  s.  Bartholomae  Airan.  Wb.  653);
crr.  dcxKvo)  , beiße'  {*dnJc-nö),  Aor.  sda-nov  (=  Impf.  ai.  ddasam),  wozu Fut.  örj^ouat  (aber  ion.  öd^eTai),  Perf.  öiörjyfxaL,  Sedrjxwg  (sowie  öfjy^a Biß*)  ^^^  Ablautneubildung  (Schwyzer  Gr.  Gr.  I  770);  day.er6v,  rö  dd/.og beißendes  Tier' 5  dazu  wohl  ddd^  ,mit  den  Zähnen  beißend*,  vielleicht ursprgl.  ,Zahn'  oder  ,Biß'  (Liddell-Scott,  anders  Schwyzer  Gr.  Gr.  I  620, 723),  wohl  Kreuzung  von  *(5a^  , beißend'  mit  döovg,  davon  abgeleitet  död^u) (död^o)  mit  Assimil.  des  0  an  das  a),  ddax^o)  usw.  , kratze,  jucke',  ddayfiög , Kratzen';
alb.  geg.  dane  (*donk-nä),  tosk.  dare  , Zange';
ahd.  zangar  , beißend,  scharf,  mnd.  langer  ,ds.,  bissig,  kräftig,  frisch'; anord.  tgng  (Gen.  tengr  und  tangar),  ags.  tang^  tange,  ahd.  zanga  , Zange' (*don7cä),  d.  i.  ,die  zusammenbeißende';  mit  weiterer  Verschiebung  zu .zusammenkneifen,  zusammendrücken',  wohl  as.  hitengi  ,nahe  an  einen rührend',  ags.  getang  ds.,  geteng
```


## [2026-09-05T18:01:56.647Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18125,18160p' POK_full.txt"
}
```


### [2026-09-05T18:01:56.697Z] TOOL RESULT

```
Page(s): 202-203 



Root / lemma: deph- 

Meaning: to stamp, push 

Material: Armenian top'el{-em, -eci) "hit"; gr. Sscpu) "knead, drum; tumble ', argiv. 

5£cpi5aaTai 'fuller', with s-extension 5£4ju) (Aor. participle 5£itjr|aa(;) "knead; tan, convert 

hide into leather' (out of it Latin depso'to knead'), 5£ijja "tanned skin'; 5i(p9£pa "leather' 

(*5iitJT£pa); Serb, depfm, dep/'t/" bump, poke, hit', poln. deptac' tread'. 

maybe alb. debq/^drwe away' 

Note: 

It seems that Root/ lemma: deph-\ "to stamp, push' derived from Root/ lemma: d^ab^^-/, 

nasalized d^amb(h)- : "to astonish, be speechless' 

References: WP. I 786, WH. I 342, SchwyzerGr. Gr. I 298, 351. 

Page(s): 203 

Root / lemma: deic!^- 

Meaning: to wind, put together, *scratch, scrape, rub 

Material: Old Indie drbhat/ ^\o'\r\ed, patched together, winded ', participle sandrbdha-^ group 

of shrubs planted together', drbdhf-t " convolution, concatenation, daisy chain ', Avestan
```


## [2026-09-05T18:01:57.480Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=213 && NR<=214' POK_01.txt | grep -n -i -A6 -B6 \"deph\\|dephn\\|diphth\" | head -60"
}
```


### [2026-09-05T18:01:59.096Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T18:02:06.755Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"depso\" POK_01.txt | head; echo ===; grep -c $'\\f' POK_01.txt"
}
```


### [2026-09-05T18:02:08.308Z] TOOL RESULT

```
(eval):1: == not found
```


## [2026-09-05T18:02:08.316Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^diphtheria\\|^diphther\\|^letter,\\|^literature\\|^literal\" KLN_1966.txt | head -20; echo \"=== daftar/defter\"; grep -n -i \"defter\\|daftar\\|dufter\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T18:02:08.391Z] TOOL RESULT

```
11511:diphtheroid,  adj.,  of  the  nature  of  diphtheria.  — Compounded  of  diphthera  and  Gk.  -osiSv;;, ‘like’,  fr.  elSo;,  ‘form,  shape’.  See  -oid. diphthong,  n.,  union  of  two  vowels  pronounced in  one  syllable.  —  F.  diphthongize,  fr.  Late  L. diphthongus,  fr.  Gk.  ftiyUo-pfo-,  ‘having  two sounds’,  fr.  Si-  (see  di-,  ‘two’),  and  yOoyyop, ‘sound,  voice,  vowel’,  which  is  rel.  to  (pDEypa, ‘sound,  voice,  speech’,  ohevyeaffxi.  ‘to  speak loud;  to  praise,  sing’.  Cp.  monophthong, triphthong.
21917:literature,  n.  —  ME.  litterature,  fr.  L.  litteratura (literatura),  ‘writing;  grammar;  learning,  schol¬ arship’,  fr.  littera  (litera),  'letter  .  See  letter  and
=== daftar/defter
3981:aumildar,  n.,  a  revenue  collector  in  India.  — Hind.  ‘ amaldar ,  lit.  ‘one  holding  an  office’,  a hybrid  coined  fr.  Arab,  'dmal,  ‘work’  (see  au¬ mil),  and  the  Persian  agential  suff.  -dar,  meaning ‘holder,  possessor’,  which  is  rel.  to  Avestic darayeiti,  ‘holds,  supports’,  OI.  dhardyati,  of s.m.,  fr.  I.-E.  base  *dher(e)-,  ‘to  hold,  support’, whence  also  L.  firmus,  ‘firm,  steadfast,  stable, strong’.  See  firm,  adj.,  and  cp.  the  first  element in  Darius.  Cp.  also  the  second  element  in  baha- dur,  chobdar,  chokidar,  dizdar,  dufterdar,  en- amdar,  foujdar,  havildar,  jaghiredar,  jemadar, killadar,  ressaldar,  silladar,  sirdar,  subahdar, tahsildar,  talukdar,  thanadar,  zemindar, auncel,  n.,  a  weight  used  in  England  in  the  Middle Ages.  —  AF.  auncelle,  fr.  It.  lancella,  dimin.  of lance,  ‘balance’,  fr.  L.  lanx,  gen.  lands,  ‘plate, dish;  scale  of  the  weighing  machine’.  See  bal¬ ance.  The  loss  of  the  initial  l  in  E.  auncel  is  due to  the  circumstance  that  the  initial  /  in  It.  lan¬ cella  was  mistaken  for  the  It.  def.  art.  V  and consequently  dropped.
11510:Derivatives:  dip,  n.,  dipp-er,  n.,  dipp-ing,  n. diphtheria,  n.,  an  infectious  disease  character¬ ized  by  the  formation  of  a  false  membrane  in the  air  passages.  —  Medical  L.,  fr.  F.  diph¬ theric,  coined  by  the  French  physician  Pierre Bretonneau  (1778-1862)  fr.  Gk.  Si^hspa,  ‘pre¬ pared  hide,  leather,  membrane’,  w'hich  is  of  un¬ certain  origin;  it  is  possibly  rel.  to  Gk.  Sctpeiv, 86t{)£iv,  ‘to  soften’.  The  disease  was  so  called by  Bretonneau  because  it  is  characterized  by the  formation  of  a  false  membrane.  For  the ending  of  diphtheria  see  1st  suff.  -ia.  Cp.  dufter. Derivatives:  diphtheri-al,  diphther-ic,  diphther- it-ic,  adjs.
12389:duller,  n.,  a  bundle  of  sheets  of  paper  (India).  — Hind,  daftar,  fr.  Pers.  daftar,  ‘record,  office’,  fr. Arab,  daftar,  fr.  Gk.  Sup&^pa,  ‘skin,  parch¬ ment,  thin  paper’.  See  diphtheria  and  cp.  next word  and  duftery.
12390:dufterdar,  n.,  the  head  native  revenue  officer.  — Hind,  daftardar,  fr.  Pers.  daftardar,  lit.  ‘holder of  records’,  formed  fr.  daftar,  ‘record,  office’, with  suff.  -ddr,  ‘holder,  possessor’.  For  the  first element  see  prec.  word.  For  the  second  element see  aumildar  and  cp.  words  there  referred  to. duftery,  n.,  a  servant  in  an  Indian  office.  —  Hind. daftari,  fr.  Pers.  daftari,  ‘office  keeper’,  fr.  daf¬ tar,  ‘record,  office’.  See  dufter. dug.  —  Past  tense  and  pp.  of  dig. dug,  pap,  teat.  —  Rel.  to  Dan.  dsegge,  Swed. ddgga,  ‘to  suckle’,  fr.  I.-E.  base  *dhe(i)-,  ‘to suckle’.  See  fecund  and  cp.  words  there  re¬ ferred  to.
```


## [2026-09-05T18:02:19.409Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# leaf index per line\nleaf=0; res={}\ntargets={11510:'diphtheria',11511:'diphtheroid',12389:'dufter',21917:'literature'}\nfor i,l in enumerate(lines,1):\n    if i in targets: res[i]=(targets[i],leaf)\n    leaf+=l.count('\\f')\nprint(res)\nEOF"
}
```


## [2026-09-05T18:02:19.793Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^letter,  n\" KLN_1966.txt | head; echo ===; grep -n \"littera\\b\" KLN_1966.txt | head -10"
}
```


### [2026-09-05T18:02:21.117Z] TOOL RESULT

```
{11510: ('diphtheria', 248), 11511: ('diphtheroid', 248), 12389: ('dufter', 266), 21917: ('literature', 482)}
```


### [2026-09-05T18:02:21.169Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T18:02:30.239Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"letter,  n\\.\" KLN_1966.txt | head -5; echo \"---literal\"; grep -n \"^literal,\" KLN_1966.txt | head -3; echo \"---littera\"; grep -n \"litera)\" KLN_1966.txt | head -5"
}
```


### [2026-09-05T18:02:30.330Z] TOOL RESULT

```
21553:Lett,  n.,  an  inhabitant  of  Latvia.  —  The  word orig.  meant  ‘people’.  It  comes  fr.  OHG.  liuti (whence  MHG.  liute,  G.  Leute),  ‘people’,  which is  possibly  cogn.  with  Gk.  JXeu&spo?,  L.  liber, ‘free’.  See  liberal  and  cp.  eleuthero-.  Cp.  also Latvia.  For  sense  development  cp.  Dutch. Derivatives:  Lett-ic,  Lett-ish,  adjs.  and  n.’s. letter,  n.,  graphic  symbol,  character.  —  ME. lettre,  fr.  OF.  (=  F.)  lettre,  fr.  L.  litter  a,  ‘letter of  the  alphabet’  (in  pi.  ‘epistle,  document’), which  is  of  uncertain  origin.  Ernout  and  Meillet (in  DELL.,  p.  363)  point  out  that  since  the  Latin alphabet  was  borrowed  from  the  Greeks (through  the  medium  of  the  Etruscans),  it  is  not improbable  that  littera  itself  would  be  of  Greek origin.  According  to  Brdal  (quoted  by  Emout- Meillet  l.c.)  littera  would  derive  fr.  Gk.  Sicp&epa, ‘tablet’,  a  word  glossed  by  Hesychius;  for  the change  of  d-  to  /-  see  lachrymal.  Cp.  literal,  liter¬ ary,  literate,  literature,  alliteration,  belles-lettres, obliterate.
---literal
---littera
21915:Derivatives:  literari-ly ,  adv.,  literari-ness ,  n. literate,  adj.,  learned,  educated;  n.,  an  educated person.  —  L.  litteratus  ( literatus ),  ‘learned,  edu¬ cated’,  lit.  ‘one  who  knows  the  letters’,  fr.  littera (litera),  ‘letter’.  See  letter  and  adj.  suff.  -ate  and cp.  literatus.
21916:literati,  n.  pi.,  men  of  letters.  —  L.  litterati  (lite¬ rati),  pi.  of  litteratus  (literatus).  See  literatus, literatim,  adv.,  letter  by  letter;  literally.  —  L.  lit- teratim  (literatim),  formed  fr.  littera  (litera), ‘letter’,  with  adv.  suff.  Stint.  See  letter.  For  suff. - atim  see  gradatim  and  cp.  words  there  referred to.
21917:literature,  n.  —  ME.  litterature,  fr.  L.  litteratura (literatura),  ‘writing;  grammar;  learning,  schol¬ arship’,  fr.  littera  (litera),  'letter  .  See  letter  and
```


## [2026-09-05T18:02:31.707Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (247,248,249,265,266,267):\n    p=pages[n]\n    import re\n    nums=re.findall(r'\\b(4[0-9]{2}|5[0-9]{2})\\b',p[:200]+p[-200:])\n    print(n, nums[:6], repr(p[:60]))\nEOF"
}
```


### [2026-09-05T18:02:33.420Z] TOOL RESULT

```
247 [] '  go  through  the  mid¬ dle’,  fr.  dis-  and  medium,  ‘mi'
248 ['454'] 'Dionysian,  adj.,  pertaining  to  Dionysus.  —  See Dyonysu'
249 [] "t.  pi.  of SbiTEpo?,  'having  two  wings’,  fr.  Si-  (see"
265 [] 'astis  and  in  lithontriptic. drop,  tr.  and  intr.  v.  —'
266 [] '  the  stem  of  L.  dux,  gen.  duds, ‘leader’.  See  duke '
267 [] 're  referred  to.\nDerivatives:  dull,  tr.  and  intr.  v., '
```


## [2026-09-05T18:02:46.732Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"deph\\|diphther\\|diphthera\" AHD_watkins1985.txt | head -20; echo \"=== litera\"; grep -n -i \"littera\\|letter\" AHD_watkins1985.txt | head -20"
}
```


## [2026-09-05T18:02:46.757Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==905' HJB.txt | head -60"
}
```


### [2026-09-05T18:02:46.805Z] TOOL RESULT

```
363:deph-
364:LOIN. 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos, long: DOLICHOCEPHALIC, DOLICHOCRANIAL. [Pok. 5. del- 196.] del-2. To recount, count. 1. Germanic *taljan in Old English tellan, to count, recount: TELL. 2. Germanic *tal6é in: a. Old English talu, story: TALE; b. Middle Dutch dle, speech, language: TAAL. 3. Old English denominative talian, to tell, relate, probably akin to the source of Middle English talken, to talk: TALK. 4. Per- haps Greek dolos, ruse, snare: DOLERITE. [Pok. 1. del- 193.] del-3. To split, carve, cut. 1. Suffixed form *del-to- in Germanic *teldam, “thing spread out,” in Old English teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping tool (< doldre, to chisel, hew): DOLABRIFORM. [Pok. 3. del- 194.] del-*. To drip. Perhaps suffixed (stative) o-grade form *dol- in Germanic *talgaz in Middle Low German falg, talch, tallow (< “dripping fat”), perhaps akin to the source of Middle English talow, tallow: TALLOw. [Pok. 4. del- 196.] deme-'. Also dem-. House, household. 1. Suffixed re- duced o-grade form *dom-o-, dom-u-, house, in: a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJOR- DOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN?, DANGER, DoM, DOMAIN, DOMI- NATE, DOMINICAL, DOMINIE, DOMINION, DOMINO}, (DOM- INO2), DUENNA, DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE. 2. Com- pound *dems-pot-, “house-master” (*-pot-, powerful; see poti-), in Greek despotés, master, lord: DESPOT. 3. Root form *dem()-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumfté in Old Norse topt, homestead: Torr. [Pok. dem- 198.] deme-2. To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
366:diphthera, prepared hide, leather (used to write on): DIPHTHERIA. 2. Latin littera, letter (possibly borrowed from Greek diphthera in the sense of “tablet” via Etrus- can): LETTER, LITERAL, LITERARY, LITERATE, LITERA- TIM; (ALLITERATE), ALLITERATION, (ILLITERATE), OBLITERATE, TRANSLITERATE. [Pok. deph- 203.] der-', Assumed base of roots meaning “to run, walk, step.” 1. Zero-grade form “dr- in extended Germanic form “*tred- in: a. Old English tredan, to step: TREAD, TREADLE; b. Middle Low German trade, course, track: TRADE. 2. Extended form *dreb- in Germanic *frep-, “something on or into which one steps,” in: a. Old English treppe, treppe, snare: TRAP; b. Middle Low German trappe, stair: TRAP’, c. Middle Dutch trappe, stair: WENTLETRAP; d. Old French trap(pje, snare: EN- TRAP; @. Middle Dutch érippen, to stamp, trample: TRIP. 3. Nasalized Germanic root *tremp- in: a. Middle Low German trampen, to stamp, tread: TRAMP; b. Italian trampoli, stilts: TRAMPOLINE. 4. Germanic *iérott- (ex- pressive derivative of *tred-) in Old French ¢roter, to trot: TROT. 5. Root form *drd- possibly in reduplicated Germanic form *ti-trd- in Old Norse titra, to tremble: TEETER. 6. Root form *drem- in suffixed o-grade form *drom-o- in: a. Greek dromos, a running, race, race- course: -DROME, DROMOND, -DROMOUS; ANADROMOUS, LOXODROMIC, PALINDROME, PRODROME; b. Greek dro- mas, running: DROMEDARY. [Pok. 3. (der-) 204.] der-2, To split, peel, flay; with derivatives referring to skin and leather. 1. Germanic *teran in Old English teran, to tear: TEAR}. 2. Germanic *ter-t- in Old English teart, sharp, severe: TART). 3. Suffixed zero-grade form *dr-tom, “‘something separated or discarded,” in Ger- manic *turdam, turd, in Old English tord, turd: TURD. 4. Reduplicated form *de-dr-u- in Old English teée)r, eruption, skin disease: TETTER. 5. Greek derris, leather covering: DERRIS. 6. Suffixed form *der-mn in Greek derma, skin: -DERM, DERMA!, -DERMA, DERMATO-; EPI- DERMIS. 7. Perhaps extended root *drep- in the Celtic source (itself borrowed) of Late Latin drappus, cloth (> Old French drap): (DRAB!), DRAPE, TRAP?. [Pok. 4. der- 206.) derbh-. To wind, compress. Zero-grade form “drbh- in Germanic *turb- in: a. Old English turf, slab of sod or peat: TURF; b. Medieval Latin turba, turf: TURBARY. [Pok. derbh- 211.] dere-. To work. Variant form *drd- (< *draa-) in Greek dran, to do: DRAMA, DRASTIC. [Pok. dero- 212.] dergh-. To grasp. 1. Perhaps Germanic *targ- in Old French targe, shield: (TARGE), TARGET. 2. Perhaps zero-grade form *drgh- in Greek drassesthai, to grab (> drakhmé, “handful,” drachma): DRACHMA. [Pok. dergh- 212.] derk-. To see. Suffixed zero-grade form *drk-on(t)- in Greek drakén (> Latin dracé), serpent, dragon (< “mon- ster with the evil eye”): DRAGON, (DRAGOON), (DRAKE?2), RANKLE. [Pok. derk- 213.] deru. Also dreu-. To be firm, solid, steadfast; hence specialized senses “wood,” “tree,” and derivatives refer- ring to objects made of wood. 1. Suffixed variant form *drew-o- in: a. Germanic *trewam in Old English tréow, tree: TREE; b. Germanic *freuw6 in Old English tréow, pledge: TRUCE. 2. Variant form *dreu- in Germanic *treuwaz in: a. Old English tréowe, firm, true; TRUE; b. Old English tréowian, triiwian, to trust: TROW; c. Old Norse tryggr, firm, true: TRIG!; d. Germanic abstract noun *treuwithé in Old English tréowth (> Middle English tro(u)the), faith, loyalty, truth: TROTH, TRUTH; BETROTH; @. Germanic abstract noun *traustam in Old Norse traust, confidence, firmness: TRUST; f. Old Norse denominative treysta, to trust, make firm, akin to the probable source of Old French triste, waiting place (< “place where one waits trustingly”): TRYST. 3. Variant form “drou- in Germanic *traujam in Old English trég, trig, wooden board: TRAY. 4. Suffixed zero-grade form
1229:ALLEGE ag-, leg-1 ALLEGORY al-!, ger-1 ALLELOMORPH al-1 ALLERGY werg- ALLEVIATE legh- ALLEY! al-2 ALLIGATOR al-1 ALLITERATE deph- ALLITERATION deph- ALLO- al-1 ALLOCUTION tolkw- ALLOMERISM (s)mer-2 ALLOPATRIC  peter- ALLOT kleu-3 ALLOY leig-1 ALLUDE |leid- ALLUVION leu(e)-
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1741:LETHAL ol- LETHARGY |adh- LETHE ladh- LETTER deph- LETTUCE melg- LEVEL [ithra LEVER leg’h- LEVIGATE ag-, leg’h- LEVIRATE daiwer- LEVITY leg¥h- LEVo- laiwo- LEVOROTATION laiwo- LEVOROTATORY laiwo- LEX leg-1 LEXICON leg-1 LIABLE leig-1 LIBATION Iéi- LIBERAL leudh-2 LIBERATE leudh-2 LIBERTINE leudh-2 LIBERTY leudh-2 LIBIDO leubh- LIBRA fithra
1755:LITERAL deph- LITERARY deph- LITERATE deph-
1756:LITERATIM deph- LITHARGE arg-
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2402:TRANSIENT ei-1, tera-2 TRANSIT ei-1 TRANSITIVE ei-1 TRANSLATE tele- TRANSLITERATE deph- TRANSLUCENT leuk- TRANSMIT (s)meit(@)- TRANSMUTE mei-1 TRANSOM tere-2 TRANSPIRE § spirare TRANSPONTINE pent- TRANSPORT per-2 TRANSUDE sweid-2 TRANSVERSE wer-3 TRAP! der-1
=== litera
366:diphthera, prepared hide, leather (used to write on): DIPHTHERIA. 2. Latin littera, letter (possibly borrowed from Greek diphthera in the sense of “tablet” via Etrus- can): LETTER, LITERAL, LITERARY, LITERATE, LITERA- TIM; (ALLITERATE), ALLITERATION, (ILLITERATE), OBLITERATE, TRANSLITERATE. [Pok. deph- 203.] der-', Assumed base of roots meaning “to run, walk, step.” 1. Zero-grade form “dr- in extended Germanic form “*tred- in: a. Old English tredan, to step: TREAD, TREADLE; b. Middle Low German trade, course, track: TRADE. 2. Extended form *dreb- in Germanic *frep-, “something on or into which one steps,” in: a. Old English treppe, treppe, snare: TRAP; b. Middle Low German trappe, stair: TRAP’, c. Middle Dutch trappe, stair: WENTLETRAP; d. Old French trap(pje, snare: EN- TRAP; @. Middle Dutch érippen, to stamp, trample: TRIP. 3. Nasalized Germanic root *tremp- in: a. Middle Low German trampen, to stamp, tread: TRAMP; b. Italian trampoli, stilts: TRAMPOLINE. 4. Germanic *iérott- (ex- pressive derivative of *tred-) in Old French ¢roter, to trot: TROT. 5. Root form *drd- possibly in reduplicated Germanic form *ti-trd- in Old Norse titra, to tremble: TEETER. 6. Root form *drem- in suffixed o-grade form *drom-o- in: a. Greek dromos, a running, race, race- course: -DROME, DROMOND, -DROMOUS; ANADROMOUS, LOXODROMIC, PALINDROME, PRODROME; b. Greek dro- mas, running: DROMEDARY. [Pok. 3. (der-) 204.] der-2, To split, peel, flay; with derivatives referring to skin and leather. 1. Germanic *teran in Old English teran, to tear: TEAR}. 2. Germanic *ter-t- in Old English teart, sharp, severe: TART). 3. Suffixed zero-grade form *dr-tom, “‘something separated or discarded,” in Ger- manic *turdam, turd, in Old English tord, turd: TURD. 4. Reduplicated form *de-dr-u- in Old English teée)r, eruption, skin disease: TETTER. 5. Greek derris, leather covering: DERRIS. 6. Suffixed form *der-mn in Greek derma, skin: -DERM, DERMA!, -DERMA, DERMATO-; EPI- DERMIS. 7. Perhaps extended root *drep- in the Celtic source (itself borrowed) of Late Latin drappus, cloth (> Old French drap): (DRAB!), DRAPE, TRAP?. [Pok. 4. der- 206.) derbh-. To wind, compress. Zero-grade form “drbh- in Germanic *turb- in: a. Old English turf, slab of sod or peat: TURF; b. Medieval Latin turba, turf: TURBARY. [Pok. derbh- 211.] dere-. To work. Variant form *drd- (< *draa-) in Greek dran, to do: DRAMA, DRASTIC. [Pok. dero- 212.] dergh-. To grasp. 1. Perhaps Germanic *targ- in Old French targe, shield: (TARGE), TARGET. 2. Perhaps zero-grade form *drgh- in Greek drassesthai, to grab (> drakhmé, “handful,” drachma): DRACHMA. [Pok. dergh- 212.] derk-. To see. Suffixed zero-grade form *drk-on(t)- in Greek drakén (> Latin dracé), serpent, dragon (< “mon- ster with the evil eye”): DRAGON, (DRAGOON), (DRAKE?2), RANKLE. [Pok. derk- 213.] deru. Also dreu-. To be firm, solid, steadfast; hence specialized senses “wood,” “tree,” and derivatives refer- ring to objects made of wood. 1. Suffixed variant form *drew-o- in: a. Germanic *trewam in Old English tréow, tree: TREE; b. Germanic *freuw6 in Old English tréow, pledge: TRUCE. 2. Variant form *dreu- in Germanic *treuwaz in: a. Old English tréowe, firm, true; TRUE; b. Old English tréowian, triiwian, to trust: TROW; c. Old Norse tryggr, firm, true: TRIG!; d. Germanic abstract noun *treuwithé in Old English tréowth (> Middle English tro(u)the), faith, loyalty, truth: TROTH, TRUTH; BETROTH; @. Germanic abstract noun *traustam in Old Norse traust, confidence, firmness: TRUST; f. Old Norse denominative treysta, to trust, make firm, akin to the probable source of Old French triste, waiting place (< “place where one waits trustingly”): TRYST. 3. Variant form “drou- in Germanic *traujam in Old English trég, trig, wooden board: TRAY. 4. Suffixed zero-grade form
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
1741:LETHAL ol- LETHARGY |adh- LETHE ladh- LETTER deph- LETTUCE melg- LEVEL [ithra LEVER leg’h- LEVIGATE ag-, leg’h- LEVIRATE daiwer- LEVITY leg¥h- LEVo- laiwo- LEVOROTATION laiwo- LEVOROTATORY laiwo- LEX leg-1 LEXICON leg-1 LIABLE leig-1 LIBATION Iéi- LIBERAL leudh-2 LIBERATE leudh-2 LIBERTINE leudh-2 LIBERTY leudh-2 LIBIDO leubh- LIBRA fithra
```


### [2026-09-05T18:02:48.568Z] TOOL RESULT

```
  eaten  in  places  where  it  is cultivated,  as  in  Chutia  Nagpur  (ff^att^ Econ.  Did.  iii.  510  ieq.)]
1679.—".  .  .  Mango  and  Baio,  two  i of  sauces  brought  from  the  East  Indies.** — Journal  qf  Jo^  Locke,  in  Ld,  Kino's  Life ofL.,i,249.
1688.— "I  hare  been  told  that  m  in made  with  a  fishy  oompositioii,  and  it seems  most  likely  by  the  Taste;  tho'  a Gentleman  of  my  Acquaintance  who  waa very  intimate  with  one  that  sailed  often from  Tonquin  to  Japan,  from  wbeoee  tb» true  Say  comes,  told  me  that  it  was  i
SPIN,
869
STIOK'INSECT,
only  with  Wheat  and  a  sort  of  Beans  mixt with  Water  and  Balt^—Dampier,  ii.  28.
1090.—".  .  .  Bony,  the  choicest  of  aU Sawces."— Own^^on,  897.
1712. — "Hoc  leffumen  in  coquin&  Japo- mc&  utramque  repTet  paginam  ;  ex  eo  nam-
?[ae  conficitor:  turn  puis  Muo  dicta,  quae erculis  pro  con8i8tenti&,  et  butyri  loco additur,  butyrum  enim  hdc  coeld  res  ignota est;  turn  £k>oJil  dictum  embamma,  quod nisi  ferculis,  cert^  frictis  et  assatis  omni- bus affunditur."  —  Kaempferf  Amoen,  Eooot, p.  839.
1776. — An  elaborate  account  of  the  pre- paration of  Soy  is  given  by  Tkunbergy  TraveU^ E.T.  iv.  121-122  ;  and  more  briefly  by Kaempfer  on  the  page  quoted  above.
[1900.  —  '*  Mushrooms  shred  into  small pieces,  flavoured  with  shayu**  (soy). — Mrs. J^rcuer.  A  DiplcmaiisCt  Wife  xn  Japan,  i. 238.]
SPIN,  8.  An  unmarried  lady ; popular  abbreviation  of  *  Spinster.*' [The  Port,  equivalent  mlUra  (soltiera) was  used  in  a  derogatorv  sense  (Grayy note  on  Pyrard  de  Laval,  Hak.  Soc.  ii. 128).]
SPONQE-CAKE,  s.  This  well- known  form  of  cake  is  called  through- out Italy  pane  di  Spagnay  a  fact  that suggested  to  us  the  possibility  that  the English  name  is  really  a  corruption of  Spaniah-cake,  The  name  in  tfapan tends  to  confirm  this,  and  must  be our  excuse  for  introducing  the  term here.
1880.— "There  is  a  cake  called  hataJteira resembling  sponge-cake.  ...  It  is  said  to have  been  introduced  by  the  Spaniards,  and that  its  name  is  a  corruption  of  CatUlla." — Mus  Bird's  Japan,  i.  23o.
SPOTTED-DEEB,  s.  Axis  macu- latus  of  Gray  ;  [Cervus  axis  of  Blan- ford  {Mammalia,  646)]  ;  Hind,  chltal, Skt.  chitra,  *  spotted.'
1673.  — "The  same  Night  we  travelled easily  to  Megatana,  using  our  Fowling- Pieces  all  the  way,  being  here  present^ with  Rich  Gkime,  as  Peacocks,  Doves,  and Pigeons,  ChitreU,  or  Spotted  D^."— Fryer, 71.
[1677.— "Spotted  Deare  we  shall  send home,  some  oy  y«  Europe  ships,  if  they touch  her^,"— Forrest,  Botnbay  letters,  i.  140.]
1679.— "There  being  conveniency  in  this place  for  ye  breeding  up  of  Spotted  Deer, which  the  Hon'ble  Company  doe  every  yeare order  to  be  sent  home  for  His  Majesty,  it is  ordered  that  care  be  taken  to  breed  them up  in  this  Factory  (Madapollara),  to  be  sent home  accordingly." — Ft.  St.  George  ConncU
(on  Tour),  16th  April,  in  NoU*  and  JSxls,, Madras,  1871.  y
1682.— "This  is  a  fine  pleasant  situation>^ full  of  great   shady  trees,  most  of   them' Tamarins,  well  stored  with   peacocks  and Spotted  Deer  like  our  fallow-deer."— ^sc^e*^ Utary,  Oct.  16 ;  [Hak.  Soc.  i.  88].
SQUEEZE,  s.  This  is  used  in An^Io-Chinese  talk  for  an  illegal  ex- action. It  is,  we  suppose,  the  trans> lation  of  a  Chinese  expression.  It corresponds  to  the  malatoUa  of  the jyiiddle  Ages,  and  to  many  other  slang phrases  in  many  tongues.
1882.— "If  the  licence  (of  the  Hong  mer- chants) .  .  .  was  costly,  it  secured  to  them uninterrupted  and  extraordinary  pecuniair advantages;  but  on  the  other  hand  it subjected  them  to  'calls'  or  'squeeies' for  contributions  to  public  works,  .  .  .  for the  relief  of  districts  su£ferin^  from  scarcity ...  as  well  as  for  the  often  imaginary  .  .  . damage  caused  by  the  overflowing  of  th» 'Yangtse  Keang'  or  the  'Yellow  River.**' —Ths  Fanktcae  at  CanUm,  p.  36.
STATION,  s.  A  word  of  constant recurrence  in  An^lo- Indian  colloquiaL. It  is  the  usual  designation  of  the  place where  the  English  officials  of  a  district, or  the  officers  of  a  garrison  (not  in  a fortress)  reside.  a£o  the  aggregate society  of  such  a  place.
[1832.— "The  nobles  and  gentlemen  are frequently  invited  to  witness  a  'Station ball.'  .  .  ."—Mrs.  Meer  Hassan  AU,  Obser- raiions,  i.  196.]
1866.— "  And  if  I  told  how  much  I  ate  at  one Mof  ussil  etation, I'm  sure  'twould  cause  at  home  a  most extraordinary  sensation."
Trevelyan,  The  Dawk  Bungalow,  in Fraser,  Ixxiii.  p.  891. , ,       "  Who  asked  the  Station  to  dinner, and  allowed  onlpr  one  glass  of  Simkin  to each  gviest."—Ibid.  231.
STEVEDORE,  s.  One  employed to  stow  the  cargo  of  a  ship  and  to unload  it.  The  verb  estivar  [Lat. stipare]  is  used  both  in  Sp.  and  Fort, in  the  sense  of  stowing  cargo,  implying originally  to  pack  close,  as  to  press wooL  Estivaaor  in  the  sense  of  a wool-packer  only  is  given  in  the  Sp. Dictionaries,  but  no  doubt  has  l>een used  in  every  sense  of  edivar.  See Skeat,  s.v.
STICK-INSEOT,  a.  The  name commonly  applied  to  certain  or- thopterona     ins
```


## [2026-09-05T18:02:54.831Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"DUFTER\\|Dufter\\|daftar\" HJB.txt | head -20"
}
```


### [2026-09-05T18:02:54.887Z] TOOL RESULT

```
9078:DUFTERY,
9092:original  Arab,  daftar  is  from  the Greek  Sii^4pa=membranuviy  *a  parch- ment,' and  thin  'paper'  ^whence  also diphtheria),  and  was  applied  to  loose sheets  filed  on  a  string,  which  formed the  record  of  accounts ;  hence  daftar becomes  *a  register,'  a  public  record. In  Arab,  any  account-book  is  still  a daftaty  and  in  S.  India  daftar  means  a bundle  of  connected  papers  tied  up  in a  cloth,  [the  basta  of  Upper  India].
9093:o.  1590. — ''Honest  experienced  officers upon  whose  forehead  the  stamp  of  correct- ness shines,  write  the  aflrreement  upon  loose pages  and  sheets,  so  wat  the  transaction cannot  be  forgotten.  These  loose  sheets, into  which  all  sanads  are  entered,  are  called the  daftar."— ^ia,  i.  260,  and  see  BlocK- fnann*s  note  there.
9096:H.  daftarddr,  is  or  was  "the  head native  revenue  officer  on  the  Collector's and  Sub-Collector's  establishment  of the  Bombay  Presidency  "  (WUson).  In the  provinces  of  the  Turkish  Empire the  l)aftard&r  was  often  a  minister  of great  power  and  importance,  as  in  the case  of  Mahonmied  Bey  Daftardar,  in Egypt  in  the  time  of  Mahommed  'All Pasha  (see  Lan^s  Mod.  Egypins.,  ed. 1860,  pp.  127-128).  The  account  of the  constitution  of  the  office  of  Daft- arddr  in  the  time  of  the  Mongol conqueror  of  Persia,  Hulagu,  will  i)e found  in  a  document  translated  by Hammer-Purgstall  in  his  Getch.  der Goldmen  Horde,  497-601.
9097:DUFTEBY,  s.  Hind,  daftarl.  A servant  in  an  Indian  office  (Bengal), whose  business  it  is  to  look  after  the condition  of  the  records,  dusting  and binding  them  ;  also  to  pen-mending, paper-ruling,  making  of  envelopes,  &c. In  Madras  these  omces  are  done  by  a Moochy.  [For  the  military  sense  of the  word  in  Afghanistan,  see  quotation from  Ferrier  below.]
25033:Dufter,     Dufterdar, Dufterkhanna, Duftery,  Duftoree, 329a,  6.  3096,  243a
```


## [2026-09-05T18:02:56.072Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"diphthera\\|diphtera\" HJB.txt IEC.txt SYN.txt SKT.txt LKT.txt AID.txt DEV.txt PHN.txt LAT.txt 2>/dev/null | head -20"
}
```


### [2026-09-05T18:02:56.141Z] TOOL RESULT

```
IEC.txt:13806:puta, io (putil-, putīkios, io; putt-) ‘vulva; little girl; chick; youngster Skt. púta, m. dual ‘buttocks’; cf. puttika, f. ‘doll’; Lat. puta (gir, whence possibly Lat. putus ‘boy, minion’ and putillus ‘dwarf; cf. It. pulcella: Fr. pucelle ‘maiden’ in relation to pulcino, m., pulcina ‘chick’); Alb. puc, m. “tot, dwarf; MHG vut, sf., cpds: vude- ‘vulva’ beside vüdel, sf. ‘gir’; OCS püta, f. “bird? beside pütistí, m. id. (fr. *putikjo-) and pütica, f. (fr. *putikio), id.; Cz. pták, m. id. beside R ptica, f. id.; Li. pute, f. *fowl" beside putytis, gs: putyCio, m. (Cchick'; cf. Lat. püticius, m. ‘simpleton’, if fr. the sense of *'fledgeling"); Latv. putns, m. ‘bird’. (LLat. *püttus "little boy', It. putto seems to derive via Etruscan fr. Gk. pósthon, id.; for the phonol. cf. pur- pura: porphyra; littera: diphthera)
```


## [2026-09-05T18:03:02.989Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9086,9092p' HJB.txt"
}
```


### [2026-09-05T18:03:03.036Z] TOOL RESULT

```
[1787.— «* We  hare  fixed  the  produce  of each  Tine  at  4  daeki  of  wet  pepper." — PurwannaA  of  Tippoo  Sultan,  m  Logan. Maiabar,  iii.  125.]
DUCKS,  BOMBAY.  See  BUM- MELO.
1860.>-"A  fish  nearly  related  to  the  sal- mon is  dried  and  exported  in  laige  quantities from  Bombay,  and  nas  acquired  the  name  of BomtMy  Dacdn."— J/ojon,  Burmah^  273.
DUFFADAB,  s.  Hind,  (from Arabo-Pers.)  dafaddr^  the  exact rationale  of  which  name  it  is  not -easy  to  explain,  [dafdy  *a  small  body, ^  section,'  aafaddr^  *a  person  in  charge of  a  small  body  of  troops  H.  A  petty ofificer  of  native  police  (v.  bnrkon- daue,  V.) ;  and  in  regiments  of  Irregu- Lur  Cavalrv,  a  non-commissioned  officer eorresponaing  in  rank  to  a  corporal  or
1808.->"  The  pav  ...  for  the  dnffadan ouffht  not  to  exceed  86  rupees. " —  Wdlingtonf
DUFTEB,  a  Ar.— H.  dafUir. Colloqaially  'the  office,'  and  inter- changeable with  cutcherry,  except that  the  latter  gener^y  implies  an office  of  the  nature  of  a  Court.  Dafta/r- Ididna  is  more  accurate,  [but  this usually  means  rather  a  record-room where   documents   are    stored].    The
original  Arab,  daftar  is  from  the Greek  Sii^4pa=membranuviy  *a  parch- ment,' and  thin  'paper'  ^whence  also diphtheria),  and  was  applied  to  loose sheets  filed  on  a  string,  which  formed the  record  of  accounts ;  hence  daftar becomes  *a  register,'  a  public  record. In  Arab,  any  account-book  is  still  a daftaty  and  in  S.  India  daftar  means  a bundle  of  connected  papers  tied  up  in a  cloth,  [the  basta  of  Upper  India].
```


## [2026-09-05T18:03:04.237Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT daftar\"; grep -n -i \"daftar\\|defter\" LKT.txt | head -10; echo \"=== DEV/PHN diphter\"; grep -n -i \"DIPHTHERIE\\|defter\" DEV.txt PHN.txt | head"
}
```


### [2026-09-05T18:03:04.312Z] TOOL RESULT

```
=== LKT daftar
=== DEV/PHN diphter
```


## [2026-09-05T18:03:12.693Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'دفتر' in p:\n        print('leaf',i,'~printed',i+543)\nEOF"
}
```


## [2026-09-05T18:03:13.407Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دفتر\" AFM_pages.txt | head -5; echo \"=== FVQ\"; grep -n -i \"daftar\\|diphthera\" FVQ_pages.txt | head -5; echo \"=== PLA\"; ls incoming/PLA/ 2>/dev/null | head"
}
```


### [2026-09-05T18:03:14.488Z] TOOL RESULT

```
leaves 684
leaf 2 ~printed 545
leaf 28 ~printed 571
leaf 106 ~printed 649
leaf 285 ~printed 828
leaf 330 ~printed 873
leaf 525 ~printed 1068
leaf 601 ~printed 1144
leaf 632 ~printed 1175
leaf 643 ~printed 1186
```


### [2026-09-05T18:03:14.553Z] TOOL RESULT

```
=== FVQ
=== PLA
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-05T18:03:18.091Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(324,333):\n    p=pages[i]\n    print('=========== leaf',i, '~printed', i+543)\n    print(p[:1500])\nEOF"
}
```


### [2026-09-05T18:03:20.167Z] TOOL RESULT

```
=========== leaf 324 ~printed 867
      ‫ات‬

                                                                            ‫ویمعنی باری ومددکاری باشد ‪ -‬ویمعتی طلب هم‬
‫باشد شبیه بماش وتارا حربی درجم ‪٩‬‏ خوانند‪.‬‬                                                                   ‫مده ‪.‬‬       ‫دسی‬          ‫نی‬    ‫صت‬


      ‫وباین ممنی باشین فرشت هم‌آمده است ‪۷‬‬
                                                                            ‫ومعاون ومدد کننده وباری دهنده؟ ‪ -‬وشاکرد‬
                                                             ‫باشد ‪.‬‬                                                    ‫باشد ‪.‬‬         ‫وزیردست‬

‫ت بفتح اول و وأو بر وزن‬                         ‫‪۸‬‬
                                                ‫دوهر‬
                                                   ‫دس‬                       ‫دست یاقتی‪ -‬کنابه از ظفر بافتن‬
‫چوبی باشد که بدان کلولة خمیر رایهن‬                           ‫پرورده‪.‬‬         ‫و مستولی گردیدن ‪ -‬ویمراد رسیدن ‪ -‬وعادت‬
                                                              ‫ند‬                                                                 ‫شدن باشد ‪.‬‬

‫ول بر وزن سلو که ‪.‬‬
                 ‫دسوك ‪-‬باضم‬                                                 ‫شستینه ‪ = ۳‬بروزن چرمینه ‪ .‬حلَهةٌطلا‬
 ‫‪ ۲‬هه‬   ‫هم‬        ‫بقتح اول‬          ‫دار يلك راکویند ‏ و‬           ‫هرم‬        ‫تان بردست کنند ‪-‬‬
                                                                                            ‫وقره و امثال آن باشد زکه‬
              ‫
=========== leaf 325 ~printed 868
                                                        ‫بیان دهم‬
     ‫تست وذو لقت و کنات‬                       ‫نقطه دار مشتمل بو‬                     ‫در دال بی نةطه مأ شن‬

                                                                                                                      ‫ھ‬
 ‫‪.‬هت‬
   ‫بج‬‫وشد‬
       ‫بد وزشت وپیل (‪ )۳‬بمعنی کره با‬                              ‫دس » بفتح‌اول وسکون‌تانی» خودآرایی‬
‫تخفیف تارا الداخته‌الد دشپیل(‪)4‬شده‌است همجو‬                       ‫وخود راساختن وآراستن ‪ -‬وصورت خوش‪ -‬وشبه‬
‫دشمن که آن دشت من بوده معنی بد دل وزشت‬                                                        ‫رظیر ومانند ‪١‬‏ باشد ‪. ۴‬‬
‫‪ ۰‬ودشنام‬         ‫دل» چه من بمحنی دل همآمده ست‬
                                                                  ‫دشل ‪ -.)۱( ۳‬نم اول بروزن مقبل »‬
‫که بمعنی دشتنام (‪)e‬‏ بوده و دشوار که دشتوار‬
           ‫و دشخوا رکه دشتخوار و مافند آن ‪. ۷‬‬                     ‫کرحهامیرا گکوبندکه در مان گوشت و پوست‬

‫دشت بدتح اول پروزن طعت ‪ ۰‬محرا‬                                 ‫دیگرمیباشد ‪ ۰‬ومعربی غدد‬                ‫ادمی )‪ (۲‬وحوانات‬

                                                                                                                          ‫خوانند ‪.‬‬
‫و ببابان باشد ‪ - ۷‬و لام ولایتی است درخراسان‬
‫مشهوریدشت بیاض ‪ -‬وصحرایی است درتر کتان‬
‫وآن بدشت قیچاق اشتهاردارد ‪ -‬و نا) شهری‌هم‬                         ‫فارسی‌بتحتانی کشیده وبلام زده ‪ ۰‬بمعنی‌دشیل(‪)۱‬‬
‫و قربه است در‬               ‫)‪(٩‬‏
=========== leaf 326 ~printed 869
          ‫تا‬                                                                                                                             ‫دشتان‬

‫تن‬       ‫سوزن کشند‬          ‫که هر‬      ‫را گوند‬            ‫تایده‬    ‫رشته‬
                                                                                             ‫وبضم اول بمعنی بد وزشت بود ‪٩‬‏ ‪.‬‬
‫کسر‬       ‫اول و‬   ‫وسم‬       ‫را همکفته‌اند ؛‬           ‫خام‬    ‫و ربمان‬
                                                                             ‫تانی‬     ‫سکون‬   ‫بقتح اول و‬             ‫‪ ۴‬ت‌‬   ‫دشتان‬

‫نزرامده‬      ‫فارسی‬      ‫باکاف‬      ‫و‬   ‫‪:‬‬     ‫است‬      ‫هم درست‬       ‫اول‬
                                                                             ‫وفوقالی‌بالف کشیده وبنون زده‪ .‬حالض‌رامی‌گوبند‬
                                                                   ‫ان‬
                                                                                               ‫یعنی زیکه خون حیضش آید ‪۰‬‬
‫‪ ۰‬رسمان‬           ‫خشکی‬       ‫‪ ۰ ۸‬بر وزن‬               ‫دشکی‬
                                                                             ‫بضم اول بروزن بدتی » زلورا‬                        ‫دشتی‬
‫خامی که زتانر سند و مردوك مانند تنضه بنخده‬                                   ‫جون‬      ‫رنگه ‪,‬‬   ‫آن کرمی باشد سیاه‬                     ‫و‬   ‫گونند‬

‫وفرموله خوانند‪.‬‬              ‫ی‬    ‫وان بفه مانندرا دب‬                ‫شود‬      ‫بر عمنوی از اعنای آدمی بح یانند خون ازان‬
      
=========== leaf 327 ~printed 870
  ‫دشيدك‬                                                                                  ‫مس‬   ‫ل‬




       ‫است » وآنرا عمود صبح هم میگوبند ‪.‬‬        ‫‪ -‬بر وزن بلنگه ‪ .‬نامشپری‬           ‫دشن‬
                            ‫دشوار ‪۴‬‬             ‫باشد ازملك ختای ‪٩‬‏ ‪ -‬و غلاف خوشة خرما‪-‬‬
‫= باواوبروزن هشیار‪ .‬بمعثی‬                                                 ‫‪8‬‬
          ‫‪¥. a‬‬                ‫‪‎‬راوخشد | ‪E‬‬        ‫وشاخیکه خوشه برآن است‪ -‬وبندیکه (‪)۱‬پیش‬
                    ‫‪۴‬‬                                                                ‫ا بندند ‪.‬‬
                                                                                             ‫ب‬
 ‫ار‬    ‫بفتح کاف‬         ‫گر‬     ‫دشوار‬             ‫= بفتح اول وثالیبروزن‌پلنگی»‬            ‫دش‬
‫بمعنی کوه‬                   ‫وسکون رای قرشت‬                 ‫دلیاوروز گار وعالم سفلی ر! گوبند ‪.‬‬
                             ‫و کوهستان باشد ‪.‬‬                  ‫‪۱‬‬                     ‫‪:‬‬
                                  ‫‪۱‬‬             ‫ذشنه = بفتح اول بر وزن تشنه ‪ .‬نوعی‬
‫بنتح شین دویم بر وزن‬        ‫دشیشاث ‏‬               ‫رمردم لار میدارند ‪.‬‬
                                                                     ‫‪۴‬تکه‬
                                                                        ‫خزنجراستبش‬
                                                                                 ‫ا‬
 ‫لطيفك ‪ .‬شب را گویند و بعربی لیل خوالند ‪.‬‬       ‫دشنة صبح ‪ -‬کنابه از روشتی صبح
=========== leaf 328 ~printed 871
                                                                   ‫بیان یدازهم‬
         ‫دال بی نقطه باغین نقطه دار مشتمل بر چهارده لفت و کنات‬                                                                        ‫در‬



‫دعدعه ‪ ۱‬ه بفتح اول و غین نقطهدار‬                                                ‫هفتح اول و سکون ثانی ‪ ۰‬زمین‬
                                                                                                          ‫دع ب‬
 ‫بروزن لخلخه » بمعنی ترس وبیم ونشوش خاطر‬                                        ‫بی‌علف بعنی زمینی که هکریکازه درآن نرسته‬
 ‫ومیل‌نمودن بچیزی باشد ‪ -‬و بکر اول والث‪,‬‬                                       ‫بواشسدر‪٩‬ب‏‪-‬ی‌موی را نیز گوبند که از کچلی‬
‫جنبالیدن انگشتان است در زبربغل ویهلوی کسی‬                                       ‫همچو کون طاس بود ‪ - ۴‬وچارضرب زده را نیز‬
                                                                                ‫و‌شخصی باشد که رش وسبیل وابرو‬
                                                                                                            ‫گفته‌اند آن‬
                                                                                    ‫داغ هم‌هست ‪۴‬‬             ‫مخ‪-‬قف‬
                                                                                                                 ‫واشد‬
                                                                                                                    ‫ومره ربااك شر‬
‫بوده‪.‬‬    ‫ار دون‬       ‫است واو ازنل‬        ‫نام
=========== leaf 329 ~printed 872
  ‫دف زدن‬                                                                                              ‫بر‬
                                                                                                       ‫‪-‬‬
   ‫هم افو اس کهرام زاو وان سا‬                                ‫وب ‪.‬‬
                                                                ‫ولای هرچیز باشد اعم ازشراب آ‬
                                                     ‫خا کدان = کنابه ازفالب آدمی‬              ‫دغل‬
 ‫دغوی = بفتح اول و ثالك و سکون‬
                                                                               ‫باشد‬   ‫وعالم سفلی‬      ‫وددا‬   ‫=‬
‫ثالی وتسنالی‪ .‬نام‌دشتی رصحرابی است که‌بر ادران‬

  ‫ببران ونه در آن دشت کعته‪ .‬شودنگدو»بند‬              ‫دغل دری = بفتح دال ابجد و رای‬
‫روزی رستم وطوی درشکار گاء] یبا دختری افتند‬           ‫بنیقطه بتحتانی زده ک»ثابه از عیب جوی وعیب‬
‫وپیش کاوی بردند و چون دختریکی از ملوکه‬                                             ‫گوی ومنافق باشد ‪.‬‬
                                                                           ‫‪9‬‬              ‫‪۱‬‬       ‫‪2‬‬
 ‫بودکاوی اورابعقد تکاح خویش درآورد و سیاوش‬           ‫بمعنی حرام‬   ‫عملی »‬   ‫بروزن‬      ‫=‬       ‫دعلی‬


 ‫ازو بهم‌رسید ‪ ۰ ۴‬ویضم ثالی نیزبهمین معنی آ‪-‬ده‬         ‫زادگی وعباری ومکاری وناراستی کردن باشد ‪.‬‬
                                           ‫‪۱‬‬   ‫انت‬   ‫دول ‪ ۰ ۴‬بفتح اول بروزن قبول ‪۰‬‬


                                               ‫هرم‬
                                 
=========== leaf 330 ~printed 873
 ‫—‬     ‫‪0‬‬   ‫= ‪۵‬‬




                                    ‫و درخانه براشند كيك‬     ‫دفز لك= بروزن ففزك » بمعنی فربه‬
                                                             ‫وبعربی‌غلیظ وضخیم‬          ‫و گنده وسطبرباشد مطلفا ‪-‬‬
                                     ‫وارشه بگریزند و هر‬                                                   ‫گونند‪۱‬‬
                                    ‫حیوانی که برگے آ برا‬
                                                                 ‫د فلت = بروزن فلك ‪ ۰‬بمعنی هدفاست‬
                                     ‫بخورد بمیرد ‪ .‬گوبند‬                                      ‫اشد ‪.‬‬
                                                                                                  ‫که نشانة تبیر‬
                                     ‫سریانی امت و بعضی‬      ‫دفلی س بکر اور و سکون انی ولام‬
                                    ‫گوبند عربی است ‪. ۴‬‬       ‫و اآنرا‬    ‫خر زهره امت‬        ‫مفتوح بتحنانی کشیده »‬

‫دفنو ك = با نون بر وزن مقاوك ‪.‬‬                                ‫بفات‬     ‫‪.‬وآن‌نبانیا مت‬    ‫هر بی سم لحمار خوانند؟‬

‫غاشبه وزین پوش راگوبند ؛ وبفقاح‌ئانی هم بادن‬                 ‫گل وی مانند گل سرخ باشد ‪ .‬گرم‬                    ‫تلح ‪.‬‬
           ‫معنی است و‪-‬بمعنی چماق هم گفته اند‪.‬‬                ‫و خشك است درسیم ‪ | .‬گربر ک آلرا بجوشانند‬


                                                 ‫بیان سیز دهم‬
                                ‫دردال بی نقطه باقاف مشتمل بر چهار لغت‬
‫ولوعی اپزارچة قیمتی‌را گویند همجح
=========== leaf 331 ~printed 874
                                                                                               ‫رت‬

‫کوسفند ازآن بغورد بجای شیر خون ازیتاش‬                 ‫دق ردن د بیعنی خواستن گودایی‬
    ‫بآربد » آولرا بعربی بقلة الغزال خوانند ‪.‬‬                                           ‫کردن باشدا ‪.‬‬
‫دق ولق ‪ -‬بفتح اول ولام » ین لقت‬                       ‫دقطاما نون ‪ £‬بفتح‌اول وسکون ثالی‬
‫از انباع است بمعنی دك ولك ‪,‬عتی‌خشك وخالی‬              ‫وطای حطی وميم (‪ )۱‬بالف کشیده و نون بواو‬
‫وحرای بعیلف ‪ -‬و سر بی موی را یز‬
                              ‫ص‬                       ‫رسیده بنون دیگر زده ‪ ۰‬بیونالی ‪ ۴‬پودنة بری‬
                                   ‫گونند ‪۰ ۳‬‬          ‫باشد و آنرا مشکطرامشیم لبز کویند ‪ .‬اکر‬


                                        ‫بیان چهار دهم‬
              ‫لفت و کنات‬               ‫در دال بی نقطه با کاف مشتمل بر سره‬


                                       ‫آمده مت‬              ‫ن»ی‬
                                                              ‫علی‬
                                                                ‫م ثا‬
                                                                   ‫بکون‬
                                                                      ‫بفتح اول وس‬             ‫دك‬
‫دك رذن ‪ ۰ ۲‬با زای شله داربروزخ‬                        ‫اصیب و تقدیر باشد ‪--‬‏وگکددااوبی را لیز‬
 ‫ک رکدن ‪ .‬بمعني کدیه و کدایی کردن باشد ‪.‬‬              ‫گویند ‪ - ۴‬وبممنی محکم ومضبوط هم هست‪-‬‬

 ‫دك ر ‪ -# ۵6‬مروزن مسخره » شخصی‬
      
=========== leaf 332 ~printed 875
 ‫‪۷‬‬


‫وربی‌موی باشد ‪ .‬ابن لفت نبزاز‬
                            ‫بی‌علف ‪ - ۴‬ص‬                  ‫کدنیا ‪ » ۱‬بروزن اغنیا ‪,‬تخل خرمارا‬
           ‫‪. ۴‬‬     ‫ولق معرب‌انت‬        ‫اتباع است ودق‬                         ‫کوتد بزمان زند ویازند (‪. )۱‬‬

                                                          ‫دل وديم ؟ ‪ -‬با دال ابجد بر وزن‬
                                                         ‫ژر و سیم»‪ ۰‬اینلقت از اتباع ابسعتعنی سر‬
‫گفته‌الد ‪ -‬وبهندی بهلو بریهلو ودوش بر دوش‬                    ‫وصورت و سروروباشد » چه دك بمعئی سر ودیم‬
                                     ‫یاند ‪٩‬‏ ‪.‬‬
                                             ‫ور‬‫زکدن‬                              ‫یمعتی صورت ورو بود ‪.‬‬
                                                             ‫دك ولك = بتشدید الی ‪ ۰‬بر وزن‬
‫وپازند (‪ )۱‬بمعتی ياك شوم وطاهر گردم باشد ‪.‬‬                   ‫ومعتی دق ولق است که خشك رخالی وصحرای‬



                                                    ‫يان بدانهزم‬
                         ‫لغت‬     ‫در دال می‌نقطه باکاف فارسی مشتمل بسره‬
                    ‫وباژگونه(‪ )۲‬وتغییرحال باشد ‪.‬‬          ‫‌لجگر » مختف‬       ‫ناو‬ ‫زکر‬‫هب‬‫بگررو‬‫‪3‬‬
                                                          ‫دیکر است ‪ 4‬که بمعنی بار باشد ‪ .‬چون اضافه‬
                                                          ‫مجیزی کنند افاد‪ #‬غیربت ونکرار تفلن و تعدد‬
‫مکروحیله وفاد و اراست ‪ - 4‬وزرقلب وناسره‬
```


## [2026-09-05T18:03:32.807Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (329,330):\n    p=pages[i]\n    for j,line in enumerate(p.split('\\n')):\n        if 'دفتر' in line or 'دوب' in line or 'سومر' in line:\n            print(i,j,line)\nEOF"
}
```


## [2026-09-05T18:03:33.114Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-05T18:03:34.617Z] TOOL RESULT

```
329 51    ‫‪ - ۷‬دوب لا در زبان سومری بمعنی لوحه وخط است‪ .‬ازابن زبان وارد کدی شده‬
330 58      ‫وهم ‪,‬ونانی را ازکلمة سامی‌عاربه میدانند ‪ .‬رابطهین دفتر پارسی ب‪1‬ا‪ 01‬پارسی باستان‌و ‪۳001‬‬
```


### [2026-09-05T18:03:34.657Z] TOOL RESULT

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


## [2026-09-05T18:03:45.079Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (329,330):\n    print('======= leaf',i)\n    ls=pages[i].split('\\n')\n    print('\\n'.join(ls[40:]))\nEOF"
}
```


### [2026-09-05T18:03:46.732Z] TOOL RESULT

```
======= leaf 329

                            ‫‪.‬‬   ‫ولی‬
                                  ‫الغ»‬‫دغو‬
                                        ‫رکه‪ :‬دا‬  ‫‪۴‬‬     ‫‪ - ۱‬از‪ :‬دغل ‪-+‬ی (مصدری) ‪.‬‬
  ‫‪ ۱‬باین‬            ‫_‪:‬چنبری‪.‬‬
                           ‫‪ ۵6‬ظ‬     ‫رکه ص‪ :‬هشتاد وشش مقدمه ‪.‬‬  ‫‪۴‬‬      ‫بح ج ‪۳۴‬ص ‪ ۵ ۲‬ببعد‬

       ‫معنی در(عر)دف آ(الازت‌طرب) ازعبری «نف» مشتق از « تفف» بمعنی زد و کویید «نفی؟ ‪:‬‬
               ‫نعود آواز دف وچنگه و نی ‪.‬‬                     ‫گوش تواند کههمه عمر وی‬
   ‫‪ .‬ور که‪ :‬ی ی‬     ‫‪۱‬‬   ‫‪۶‬‬   ‫«کلتان‬

   ‫‪ - ۷‬دوب لا در زبان سومری بمعنی لوحه وخط است‪ .‬ازابن زبان وارد کدی شده‬
   ‫تا‪00‬نا و ‪PP‬‏ کردید‪ .‬واز ابن زبالها وارد آرامی شده لا گردید‪ ,‬و نیز بمعنی لوحه‬
   ‫وصفحه کرفتهشده بعدها درزبان عربی «دف» شده وبمعنی لوحه تبزیکار رفته است «فاباص‪۱۱٩ ۲‬‏‬
                   ‫بقل از«لفغات بیگانة !کدی تألیف ‪nremmiZ‬‏ « للپزیگه ص‪٩۹۱‬‏ ور کے ‪ :‬تفس ‪.‬‬
       ‫‪ - ٩‬ممنی اصلی ‪,‬نی دف (آلت موسیقی) تواختن‪. ‎‬‬                     ‫دفتن ‪.‬‬     ‫رک‪:‬‬         ‫‪۸‬‬

  ‫زا از ونالی ‪aréhthpiD‬‏ (پوست حیوانی) داسته‌اند‬              ‫‪ #‬دفر بفتح اول نوم ‪۱‬‬                       ‫‪۱‬‬
   ‫‪ °‬دارةالمعارف اسلام د‪:‬فتر» پنفل از ‪refuD:‬‏ ‪eluY te ,llenruB nosboJ_nosboH‬‬
        ‫‪۰۷.۸‬‬    ‫یه درصفحه‬

======= leaf 330




  ‫هر که ‪,‬دماری دق دارد ‪ ,‬کجا گردد سین ؟ «منوچهری دامغان ی‪٩۹۹‬‏ ‪.‬‬

                                                                                              ‫بقه ‪7‬صفحه ‪٩۹۸‬‏‬
        ‫تس‬
         ‫دند ‪.‬‬
             ‫وده ا‬
                 ‫رنامی‬
                     ‫هر ‪٩‬‏‬
                         ‫یم‌ناست آنکه در قدیم روی بوست کتات میشده ‪ ,‬کتاب را « دفت‬
  ‫‪« : 9۳۳‬کتاب را موتها برسم قدیم ‪arehthpid‬‏ (یوست) خوانند » زیرا درقدیم کاغذ (یایروس)‬
     ‫کماب بوده » روی دهامت بز ومیش می‌لوشاند و امروزه یز بسیاری از ببگانگان روی چنن‬
 ‫برخی دیکر همکامةفارسی‬                    ‫ص‪۴۲۱۱-‬‏‬
                                                ‫‪٩‬ا‪۱‬ب‪۱‬ا‪۳‬‬
                                                      ‫پوستهایی متویبند ‪٩ .‬‏ « هرردتس ‪ ۸۵ . ۷‬ق‬
     ‫وهم ‪,‬ونانی را ازکلمة سامی‌عاربه میدانند ‪ .‬رابطهین دفتر پارسی ب‪1‬ا‪ 01‬پارسی باستان‌و ‪۳001‬‬
                                                                   ‫کادی و «دیبر» پارسی نامعلوم امت ‪ .‬رك‬
                 ‫‪P.‬‬         ‫‪Lagarde,‬‬        ‫‪Gesammelte‬‬           ‫‪Abhandlungen,‬‬              ‫‪Leipzig 6‬‬
 ‫‪216-217; P.Jensen, «Elamitische‬‬                            ‫‪Eigenammen’ » Wiener Zeitschrift‬‬
 ‫‪flr die Kunde des Morgenlandes. 6 ( 1896 ).218 -219.‬‬
   ‫هبارن قاعطع ‪)۴۱۱‬‬
                  ‫(‬
```


## [2026-09-05T18:04:17.865Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA daftar\"; grep -n -i \"daftar\\|Daftar\\|dattar\" incoming/PLA/PLA_pages.txt | head -10; echo \"=== AFM\"; grep -n \"دفتر\" AFM.txt AFM_alt.txt 2>/dev/null | head -5; echo \"=== FVQ\"; grep -n -i \"daftar\" FVQ.txt | head -5"
}
```


### [2026-09-05T18:04:17.949Z] TOOL RESULT

```
=== PLA daftar
4399:2            - taftar:                  "Buch,       Heft"          = daftar           s.    daftar      5
7117:dast                                                                         124                                                   daftardär
7141:_#b>»-             dafätir:           Pl. v. wo» daftar s. daftar.
7145:2       -    daftar:            "Buch,          Liste,          Register,           Material,       Katalog,              Ausgabenbuch,
7146:        Album"           pers.        2              mp.     ro»        daftar       14         ap.      dipi     "schreiben"            od.
7149:„])s7»> - daftardär:                           "Finanzminister"                    pers.
7169:daftardäriyya                                                                125
7172:as,lys> - daftardäriyya:                                     Pl. v. bs»              daftardär.
=== AFM
AFM_alt.txt:2451:( الدستور) الدفترالذى اکل فه ا سماء اند او الذى تع فه قوانين اللاك 
=== FVQ
```


## [2026-09-05T18:04:18.880Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON دیفتری\"; grep -n \"دیفتری\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head -5; echo \"=== MON دفتر\"; grep -c \"دفتر\" MON_part1.txt MON_part2.txt 2>/dev/null"
}
```


### [2026-09-05T18:04:18.970Z] TOOL RESULT

```
=== MON دیفتری
MON_part1.txt:57506:دیفتری. 
MON_part1.txt:57509:دیفتری. 
MON_part1.txt:71297:سرخک عارض شود با دیفتری که غالباً با 
MON_part2.txt:9373:آنژین‌های دیفتروئید و دیفتری) نیز موجود 
MON_part2.txt:39289:دیفتری و غیره عارض شود و نیز در دنبالة 
=== MON دفتر
MON_part2.txt:51
MON_part1.txt:79
```


## [2026-09-05T18:04:24.293Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7140,7160p' incoming/PLA/PLA_pages.txt"
}
```


### [2026-09-05T18:04:24.339Z] TOOL RESULT

```
_#b>»-             dafätir:           Pl. v. wo» daftar s. daftar.

sb) - daffaf:                   "Tamburinschläger"                          nom.    agent.     v..       duff s. duff.

2       -    daftar:            "Buch,          Liste,          Register,           Material,       Katalog,              Ausgabenbuch,
        Album"           pers.        2              mp.     ro»        daftar       14         ap.      dipi     "schreiben"            od.
        akk. tuppi.- od. griech. Diphthera "Haut" 1°                                                        dtsch. Diphtera 1.

„])s7»> - daftardär:                           "Finanzminister"                    pers.


1.    Wahrmund             s.    v.
2.    Nyberg         Bd.        II    s.       v.
3.    Macuch         Ss.    v.
4. Muhit            s.     v.
5.    Addai         Scher        s.       v.
6.    Nyberg         Bd.        IIs.           v.
7.    Macuch         Ss.    v.
8.    Brockelmann                s.       v.
9. Muhit            s.     v.
```


## [2026-09-05T18:04:24.845Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '57500,57515p' MON_part1.txt; echo \"=== دفتر in MON\"; grep -n \"^دفتر\" MON_part1.txt | head"
}
```


### [2026-09-05T18:04:24.935Z] TOOL RESULT

```
طبقة پایین کشتی. 


خناس: ۵۵ (ع.] (ص. ۱.) شبطان» 
اهر یمن » دیو سرکش. بدکار» شبطان صفت. 
خناق: 07 [سمعر. خناکك] (.) (بز.) 
دیفتری. 

خناک: *0۸2[- خناق» معر.] (ا.) (بز.) 
دیفتری. 

ختیره: و (- خمره] (امر.) 
خمره» خم کوچکد» خمچه 

خنه: (م)همطنمد () خسم 0 و دراز 
تا هون که ور آن غله کنند . کودال 
=== دفتر in MON
13125:دفتر یک نگاه؛ مدرسه» سازمان و جز ِ 
13142:دفتر چه‌های سناسنامه. 
23440:دفتر و جز آنها را بهم بندند. هر شربت 
61985:دفتر: 7 (معر. بوست؛ نوشتن ] (ا.) عدة 
62012:دفتر خانه: (0-)202-. [سعر. ف.)] (امر.) 
62019:دفتر اسناد رسمی؛ محضر. 
62022:دفتر دار: ٩.27‏ آمعر. ف. - دفتردارنده] 
62025:دفتر. محاسب» حساندار. کسی که دفتر های 
62029:دفترداری: ٩.-087-[‏ (حامص.) عمل و 
62031:دفترهای حساب به موجب قواعد حسابداری
```


## [2026-09-05T18:04:35.414Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '61980,61995p' MON_part1.txt; echo \"======= diftari headword\"; grep -n \"^دیفتری\\|دیفتری:\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-05T18:04:35.491Z] TOOL RESULT

```
دف: 1210 [معر.] (ا.) (مست.) چنبری است 
که پوستی بر آن چسبانند و قوالان آن را با 
انگشت نوازند. 

دفتر: 7 (معر. بوست؛ نوشتن ] (ا.) عدة 
اوراقی که بهم پیوسته و در جلدی جای داده 
شده و در آن مطالب مختلف» نظم و نثر یا 
محاسیات را نوسند؛ جزوه. کتات. طومار. 
روزنامه. جایی که دییران و منشیان در آنجا به 
کارهای دفتر نوسی می بر دازند؛ کایبینه: دفتر 
وزار تی» دفتر بست (فره.)؛ ج. دفاتر. دفتر 
اخلاق: کتاب اخلاق. دفتر تجار تی: (اقتص. 
حق.) دفتری که تاجر معاملات خود را در 
آن ثبت نماید و از روی آن سود وی تعیین 
گردد. دفتر ت املاک: (حق.) اداره‌ای که 
======= diftari headword
MON_part2.txt:39289:دیفتری و غیره عارض شود و نیز در دنبالة 
MON_part1.txt:57506:دیفتری. 
MON_part1.txt:57509:دیفتری.
```


## [2026-09-05T18:04:45.232Z] TOOL CALL #34: Bash

```json
{
 "command": "sed -n '1,45p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-05T18:04:45.275Z] TOOL RESULT

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
```


## [2026-09-05T18:04:48.945Z] TOOL CALL #35: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/διφθέρα\" \\\n \"https://en.wiktionary.org/wiki/دفتر\" \\\n \"https://en.wiktionary.org/wiki/littera\" \\\n \"https://www.etymonline.com/word/diphtheria\" \\\n \"https://www.etymonline.com/word/letter\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 118, root Deph: diphthera/daftar/littera chain\" ; done"
}
```


### [2026-09-05T18:04:52.630Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f05cfb0865aeb7c7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e15ae92c582e7ce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ca5c9ae205193ae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b225553aa9a92fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06bf9da98f246191.txt
```


## [2026-09-05T18:04:55.191Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"######## diphthera\"; grep -n -i -A12 \"Etymology\" f05cfb0865aeb7c7.txt | head -60"
}
```


### [2026-09-05T18:04:55.252Z] TOOL RESULT

```
######## diphthera
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Derived terms 
--
156: Etymology
157- [ edit ] 
158-
159- The origin is uncertain, possibly from Proto-Hellenic *dipʰtʰérā . Related to διψάρα ( dipsára , “ writing-tablet; piece of leather ” ) and Mycenaean Greek 𐀇𐁇𐀨 ( di-pte-ra ) .
160-
161- Since de Saussure, connected with δέφω ( déphō ) or δέψω ( dépsō , “ to soften (with the hand) ” ) . Beekes argues that this connection and the alternation between φ ( ph ) and ψ ( ps ) point to a Pre-Greek origin. [ 1 ] 
162-
163- Compare also Akkadian 𒁾 ( ṭuppu , “ tablet, document, letter ” ) and Sumerian 𒁾 ( dub , “ tablet ” ) , Sumerian 𒁾𒊬 ( dub-sar , “ writer, scribe ” ) .
164-
165- Pronunciation
166- [ edit ] 
167-
168- IPA ( key ) : /dipʰ.tʰé.raː/ → /ðiɸˈθe.ra/ → /ðifˈθe.ra/
```


## [2026-09-05T18:04:55.853Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"######## daftar\"; sed -n '1,400p' 0e15ae92c582e7ce.txt | grep -n -i -B3 -A15 \"Arabic\\|Etymology\" | head -120"
}
```


### [2026-09-05T18:04:55.912Z] TOOL RESULT

```
######## daftar
54- Beginning
55-
56- 1 
57: Arabic 
58-
59: Toggle Arabic subsection 
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Descendants 
75-
76- 1.4 
77- References 
--
88- Declension 
89-
90- 3 
91: Egyptian Arabic 
92-
93: Toggle Egyptian Arabic subsection 
94-
95- 3.1 
96: Etymology 
97-
98- 3.2 
99- Pronunciation 
100-
101- 3.3 
102- Noun 
103-
104- 3.4 
105- References 
106-
107- 4 
108- Ottoman Turkish 
109-
110- Toggle Ottoman Turkish subsection 
111-
112- 4.1 
113: Etymology 
114-
115- 4.2 
116- Noun 
117-
118- 4.2.1 
119- Derived terms 
120-
121- 4.2.2 
122- Descendants 
123-
124- 4.3 
125- Further reading 
126-
127- 5 
128- Persian 
--
130- Toggle Persian subsection 
131-
132- 5.1 
133: Etymology 
134-
135- 5.2 
136- Pronunciation 
137-
138- 5.3 
139- Noun 
140-
141- 5.3.1 
142- Descendants 
143-
144- 5.4 
145- References 
146-
147- 6 
148- Punjabi 
--
150- Toggle Punjabi subsection 
151-
152- 6.1 
153: Etymology 
154-
155- 6.2 
156- Pronunciation 
157-
158- 6.3 
159- Noun 
160-
161- 6.3.1 
162- Declension 
163-
164- 6.3.2 
165- Related terms 
166-
167- 6.4 
168- Further reading 
--
173- Toggle Sindhi subsection 
174-
175- 7.1 
176: Etymology 
177-
178- 7.2 
179- Pronunciation 
180-
181- 7.3 
182- Noun 
183-
184- 7.3.1 
185- Declension
```


## [2026-09-05T18:05:05.513Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '200,420p' 0e15ae92c582e7ce.txt"
}
```


### [2026-09-05T18:05:05.563Z] TOOL RESULT

```
 8.3 
 Noun 

 8.3.1 
 Declension 

 8.4 
 References 

 Toggle the table of contents 

 دفتر 

 20 languages 

 Azərbaycanca 
 বাংলা 
 Deutsch 
 Eesti 
 فارسی 
 Na Vosa Vakaviti 
 Français 
 Magyar 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Malagasy 
 Polski 
 پښتو 
 Português 
 Русский 
 Sängö 
 سرائیکی 
 Shqip 
 中文 

 Entry 

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
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Arabic
 [ edit ] 

 دفتر 
 Etymology
 [ edit ] 

 Etymology tree

 Aramaic דפתרא der. 

 Proto-Hellenic *dipʰtʰérā ? 
 Ancient Greek διφθέρᾱ ( diphthérā ) bor. 
 Classical Syriac ܕܦܬܪܐ der. 

 Middle Persian dptl ( daftar ) bor. ? 
 Arabic دفتر 

 Possibly borrowed from Middle Persian dptl ( daftar ) , from Aramaic דפתרא or Classical Syriac ܕܦܬܪܐ . [ 1 ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /daf.tar/ 

 Noun
 [ edit ] 

 دَفْتَر • ( daftar )  m ( plural دَفَاتِر ( dafātir ) ) 

 register ; roster 

 notebook ; copybook ; exercise book 

 Declension
 [ edit ] 

 Declension of noun دَفْتَر ( daftar )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 دَفْتَر 
 daftar 

 الدَّفْتَر 
 ad-daftar 

 دَفْتَر 
 daftar 

 nominative

 دَفْتَرٌ 
 daftarun 

 الدَّفْتَرُ 
 ad-daftaru 

 دَفْتَرُ 
 daftaru 

 accusative

 دَفْتَرًا 
 daftaran 

 الدَّفْتَرَ 
 ad-daftara 

 دَفْتَرَ 
 daftara 

 genitive

 دَفْتَرٍ 
 daftarin 

 الدَّفْتَرِ 
 ad-daftari 

 دَفْتَرِ 
 daftari 

 dual

 indefinite

 definite

 construct

 informal

 دَفْتَرَيْن 
 daftarayn 

 الدَّفْتَرَيْن 
 ad-daftarayn 

 دَفْتَرَيْ 
 daftaray 

 nominative

 دَفْتَرَانِ 
 daftarāni 

 الدَّفْتَرَانِ 
 ad-daftarāni 

 دَفْتَرَا 
 daftarā 

 accusative

 دَفْتَرَيْنِ 
 daftarayni 

 الدَّفْتَرَيْنِ 
 ad-daftarayni 

 دَفْتَرَيْ
```


## [2026-09-05T18:05:12.077Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Persian$/,/^ Punjabi$/' 0e15ae92c582e7ce.txt | head -80"
}
```


### [2026-09-05T18:05:13.815Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Middle Persian [script needed] ( dptl /⁠daftar⁠/ ) , from Aramaic דפתרא / ܕܦܬܪܐ , from Ancient Greek διφθέρα ( diphthéra ) . The learned plural دفاتر ( dafātir ) is re-borrowed from Arabic دفاتر ( dafātir ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /daf.ˈtar/ 

 ( Dari, formal ) IPA ( key ) : [d̪äf.t̪ʰáɾ] 

 ( Dari, formal ) IPA ( key ) : [d̪äf.t̪ʰáɾ] 
 ( Kabuli ) IPA ( key ) : [d̪äf.t̪ʰáɾ] 

 ( Hazaragi ) IPA ( key ) : [d̪äf.t̪ʰáɾ] 

 ( Iran, formal ) IPA ( key ) : [d̪æf.t̪ʰǽɹ] 

 ( Tajik, formal ) IPA ( key ) : [d̪äf.t̪ʰáɾ] 

 Rhymes: -ar 

 Readings

 Classical reading ? 

 daftar

 Dari reading ? 

 daftar

 Iranian reading ? 

 daftar

 Tajik reading ? 

 daftar

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 Dari

 دفتر 

 Iranian Persian

 Tajik

 дафтар 

 دفتر • ( daftar ) ( plural دفترها ( daftar-hā / daftar-hâ ) , or دفاتر , Tajik spelling дафтар ) 

 register , account book 
 وارد دفتر کردن vâred-e daftar kardan to register, to make an entry in the account book 

 notebook , journal 
 دفتر خاطرات روزانه daftar -e xâterât-e ruzâne personal journal (literally, “ notebook of daily thoughts ”) 

 c. 1390 , Shams-ud-Dīn Muḥammad Ḥāfiẓ , “Ghazal 162”, in دیوان حافظ [ The Divān of Ḥāfiẓ ]‎ [7] : بشوی اوراق اگر همدرس مایی
که علم عشق در دفتر نباشد bišōy awrāq agar hamdars-i mā-yī
ki ilm-i išq dar daftar na-bāšad Wash away the pages if you are our classmate,
For the science of love is not in the notebooks . (Classical Persian transliteration) 

 office , office building 
 رفتم دفتر م ― raftam daftar -am ― I went to my office 

 Descendants
 [ edit ] 

 → Arabic: دَفْتَر ( daftar , “ register; notebook ” ) ( see there for further descendants )
```


## [2026-09-05T18:05:21.963Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### littera wiktionary\"; grep -n -A20 \"Etymology\" 6ca5c9ae205193ae.txt | grep -v \"^\\s*$\" | sed -n '1,60p'"
}
```


### [2026-09-05T18:05:23.535Z] TOOL RESULT

```
#### littera wiktionary
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.4 
74- Further reading 
75-
76- 2 
77- Interlingua 
78-
79- Toggle Interlingua subsection 
80-
81- 2.1 
82- Pronunciation 
--
96: Etymology 
97-
98- 3.3 
99- Pronunciation 
100-
101- 3.4 
102- Noun 
103-
104- 3.4.1 
105- Usage notes 
106-
107- 3.4.2 
108- Declension 
109-
110- 3.4.3 
111- Derived terms 
112-
113- 3.4.4 
114- Descendants 
115-
116- 3.5 
--
134: Etymology 
135-
136- 4.3 
137- Noun 
138-
139- 4.3.1 
140- Declension 
141-
142- 4.3.2 
143- Derived terms 
144-
145- 4.4 
146- References 
147-
148- Toggle the table of contents 
149-
```


## [2026-09-05T18:05:23.780Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### etymonline diphtheria\"; sed -n '1,120p' 9b225553aa9a92fc.txt | grep -n -i -A8 \"diphtheria (n\" ; echo \"#### etymonline letter\"; grep -n -i -A10 \"letter (n\" 06bf9da98f246191.txt | head -40"
}
```


### [2026-09-05T18:05:23.855Z] TOOL RESULT

```
#### etymonline diphtheria
23: diphtheria (n.) 
24-
25- infectious disease, formerly frequently fatal, 1857, from French diphthérie , coined 1855 by physician Pierre Bretonneau (1778-1862) from Greek diphthera "prepared hide, leather," which is of unknown origin; the disease so called for the tough membrane that forms in the throat.
26-
27- Bretonneau's earlier name for it was diphthérite (1821), which had been Englished as diphtheritis (1826). Related: Diphtheritic .
28- also from 1857 
29-
30- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
31-
#### etymonline letter
56: letter (n.1) 
57-
58- c. 1200, "graphic symbol, alphabetic sign, written character conveying information about sound in speech," from Old French letre "character, letter; missive, note," in plural, "literature, writing, learning" (10c., Modern French lettre ), from Latin littera (also litera ) "letter of the alphabet," also "an epistle, writing, document; literature, great books; science, learning;" a word of uncertain origin.
59-
60- According to Watkins, perhaps via Etruscan from Greek diphthera "tablet" (with change of d- to l- as in lachrymose ), from a hypothetical root *deph- "to stamp." In this sense it replaced Old English bocstæf , literally "book staff" (compare German Buchstabe "letter, character," from Old High German buohstab , from Proto-Germanic *bok-staba-m ).
61-
62- Latin littera also meant "a writing, document, record," and in plural litteræ "a letter, epistle, missive communication in writing," a sense passed through French and attested in English letter since early 13c. (replacing Old English ærendgewrit "written message," literally "errand-writing"). The Latin plural also meant "literature, books," and figuratively "learning, liberal education, schooling" (see letters ).
63-
64- The custom of giving the school letter as an achievement award in sports, attested by 1908, is said to have originated with University of Chicago football coach Amos Alonzo Stagg. Earlier in reference to colleges it meant "university degree or honor that adds initials to a name" (1888). Expression to the letter "precisely" is from 1520s (earlier after the letter , mid-14c.). Letter-quality (adj.) "suitable for (business) letters" is from 1977. For letters patent (with French word order) see patent (n.).
65- also from c. 1200 
66-
--
69: "write in letters," 1660s, from letter (n.1). Earlier it was used in a now obsolete sense "instruct" (mid-15c.). Related: Lettered ; lettering .
70- also from 1660s 
71-
72: letter (n.2) 
73-
74- "one who lets" in any sense, c. 1400, agent noun from let (v.).
75- also from c. 1400 
76-
77- Entries linking to letter 
78-
79- lachrymose (adj.) 
80-
81- also lacrymose , 1660s, "tear-like," from Latin lacrimosus "tearful, sorrowful, weeping," also "causing tears, lamentable," from lacrima , lacryma "a tear," a dialect-altered borrowing of Greek dakryma "a tear," from dakryein "to shed tears, weep, lament with tears," from dakry "a tear" (reconstructed in Watkins to be from PIE *dakru- "tear;" see tear (n.1)).
82-
--
138: "elegant literature, literature as fine art," 1710, French, literally "fine letters," from belles, plural of belle, fem. of beau "fine, beautiful" (see beau) + lettres, plural of lettre "letter" (see letter (n.)). The literary equivalent of beaux arts; its boundaries never have b
139-
140- brief 
141-
142- genitive brevis), noun derivative of adjective brevis "short, little" (from PIE root *mregh-u- "short") which came to mean "letter..., summary," specifically a letter of the pope (less ample and solemn than a bull), and thus came to mean "letter of authority...In German, Brief has become the general word for "an epistle or letter."...
143-
144- chi 
145-
146- 22nd letter of the Greek alphabet, representing a -kh- sound (see ch)....The letter is shaped like an X, and so the Greek letter name was used figuratively to signify such a shape or arrangement...things placed crosswise;" khiastos "arranged diagonally; marked with an X;" khiazein "to mark with an 'X', to write the letter...
147-
148- epistle
```


## [2026-09-05T18:05:28.426Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/From Wiktionary, the free dictionary/,0' 6ca5c9ae205193ae.txt | sed -n '1,60p'"
}
```


### [2026-09-05T18:05:31.104Z] TOOL RESULT

```
 From Wiktionary, the free dictionary

 See also: litera 

 Finnish
 [ edit ] 

 Etymology
 [ edit ] 

 Internationalism , ultimately from Latin littera .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈlitːerɑ/ , [ˈlit̪ːe̞rɑ̝] 

 Rhymes: -itːerɑ 

 Syllabification ( key ) : lit‧te‧ra 

 Hyphenation ( key ) : lit‧te‧ra 

 Noun
 [ edit ] 

 littera 

 identification letter , ordinal letter 
 Synonym: järjestyskirjain 
 ( numismatics ) a letter used to distinguish different banknotes , coins , etc. of the same denomination 

 ( rail transport ) identification code of a class of rolling stock 

 ( finance ) denomination ( of a stock certificate ) 

 ( accounting ) phase of a project , etc. ( in billing, invoicing, etc.; any unit which may be billed for, often as part of a larger project ) 

 ( historical ) a free (train) ticket or ticket rebate offered to military transportation or to conscripts 

 Declension
 [ edit ] 

 Inflection of littera ( Kotus type 12/ kulkija , no gradation)

 nominative

 littera 

 litterat 

 genitive

 litteran 

 litteroiden 
 litteroitten 

 partitive
```


## [2026-09-05T18:05:33.231Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Latin$/,/^ Portuguese$|^ Spanish$/' 6ca5c9ae205193ae.txt | sed -n '1,45p'"
}
```


### [2026-09-05T18:05:34.760Z] TOOL RESULT

```
 Latin
 [ edit ] 

 Alternative forms
 [ edit ] 

 lītera 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *h₂leyH- der. 
 Old Latin leitera 
 Latin lītera der. ? 

 Proto-Hellenic *dipʰtʰérā ? 
 Ancient Greek διφθέρᾱ ( diphthérā ) bor. 
 Etruscan [Term?] bor. ? 

 Latin littera 

 Unknown. Two possibilities include:

 From earlier lītera , the existence of which is disputed, [ 1 ] with lengthening of the consonant (sometimes called the littera rule [ 2 ] ), from Old Latin leitera (attested ca. 122 BC, [ 3 ] argued by Ernout & Meillet to be a false etymological attraction to lino [ 4 ] ), from a plural form of earlier adj. *lei-tos (cf. opera from opus ), related to Latin linō ( “ smear ” ) and Proto-Italic *linō ( “ smear ” ) , [ 5 ] ultimately from Proto-Indo-European *h₂leyH- ( “ smear ” ) . A variation of this is to reconstruct the PIE root as *leyt- ( “ to scratch ” ) . [ 6 ] 

 However, De Vaan points out that the past participle from lino is actually litus with a short i and, lacking any other traces of *leitos, says the scenario is "morphologically unconvincing". [ 1 ] 
 Alternatively, perhaps via Etruscan [Term?] from (or related to, as if from a common source) Ancient Greek διφθέρᾱ ( diphthérā , “ leather; writing material ” ) which is claimed by Hesychius to be used to name tablets as well, [ 4 ] of unknown ultimate origin.

 Pronunciation
 [ edit ] 

 ( Classical Latin ) IPA ( key ) : [ˈlɪt.tɛ.ra] 

 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈlit.te.ra] 

 Noun
 [ edit ] 

 littera   f ( genitive litterae ) ; first declension 

 letter (of the alphabet )

 ( metonymic ) handwriting
```


## [2026-09-05T18:05:53.013Z] TOOL CALL #44: Bash

```json
{
 "command": "ls site/pages/118.jpg 2>/dev/null; pdftoppm -f 118 -l 118 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg118 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T18:05:53.903Z] TOOL CALL #45: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/دیفتری/\" --note \"page 118 node 5: Persian دیفتری, Mo'in origin tag\" ; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/diphtheria\" --note \"page 118 node 6: English diphtheria\""
}
```


### [2026-09-05T18:05:55.260Z] TOOL RESULT

```
site/pages/118.jpg
total 34584
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 14:05 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18289 Sep  5 13:48 c_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13620 Sep  5 13:48 c_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10949 Sep  5 13:48 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15141 Sep  5 13:51 c_hektaton.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb    18737 Sep  5 13:51 c_kent.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10687 Sep  5 13:48 c_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    24046 Sep  5 13:38 latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62837 Sep  5 13:37 mk108.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40927 Sep  5 13:43 mk109.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63862 Sep  5 13:46 mk110.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48342 Sep  5 14:00 mk113.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61685 Sep  5 14:01 mk114.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60434 Sep  5 14:01 mk115.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63543 Sep  5 13:30 pg109.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6518 Sep  5 13:38 pg110_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36325 Sep  5 13:32 pg110_yeth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46559 Sep  5 13:32 pg110_zbn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72718 Sep  5 13:38 pg111.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50381 Sep  5 13:37 pg112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65357 Sep  5 13:45 pg113.png
-rw-rw-r-- 1 sfmqrb sfmqrb   117231 Sep  5 13:48 pg114_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1253 Sep  5 13:48 pg114_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11671 Sep  5 13:48 pg114_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83933 Sep  5 13:46 pg114.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163144 Sep  5 13:51 pg115_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70699 Sep  5 13:51 pg115.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64811 Sep  5 13:57 pg117.png
-rw-rw-r-- 1 sfmqrb sfmqrb    42354 Sep  5 14:05 pg118.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


### [2026-09-05T18:06:09.367Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/24cef44cc01ba530.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0166c4af8e0b265a.txt
```


## [2026-09-05T18:06:12.230Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg118.png"
}
```


### [2026-09-05T18:06:12.735Z] TOOL RESULT

```

```


## [2026-09-05T18:06:12.732Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T18:06:30.170Z] TOOL CALL #47: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T18:06:30.241Z] TOOL RESULT

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


## [2026-09-05T18:06:30.662Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 -c \"\nimport json,glob\nfor f in ['data/verification/page-114.json','data/verification/page-113.json']:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if n['verdict']=='transcription_suspect':\n                print(f, n.get('words'), n.get('error_in'), n.get('book_prints'), n.get('correct_form'))\n                print('  ', n['derivation'][:300])\n\""
}
```


### [2026-09-05T18:06:32.465Z] TOOL RESULT

```
data/verification/page-114.json dah; yâcdah; sîkdah; šâncdah; navasdah book sîkdah; navasdah sîcdah (sēzdah); navâcdah (navazdah)
   Middle Persian continues the Old Iranian numerals with the regular loss of final syllables: *dasa > dah (intervocalic -s- > -h-), and the teens *aēva-dasa, *θri-dasa, *xšvaš-dasa, *nava-dasa > yāzdah, sēzdah, šānzdah, nōzdah. Nourai's spellings with ⟨c⟩ are Book-Pahlavi transliterations, where ⟨c⟩ s
```


## [2026-09-05T18:06:44.895Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD daftar/dptl\"; grep -n -i \"daftar\\|dpt\" PHD_mackenzie.txt | head -10; echo \"### NYB\"; grep -n -i \"daftar\\|dptl\" NYB_vol2_glossary.txt NYB.txt 2>/dev/null | head -10; echo \"### HRN\"; grep -n -i \"daftar\\|defter\" HRN.txt | head -10; echo \"### HUB\"; grep -n -i \"daftar\" HUB.txt | head"
}
```


### [2026-09-05T18:06:44.999Z] TOOL RESULT

```
### PHD daftar/dptl
1832:daftan, dam- [dptn , dm- I M dm-, N dam-idan] breathe, blow.
1835:daftar [dptll N ,...,] register, account-book.
2105:   .....-daft [dwSdpt 1] ill-breathing, short of breath.
5764:zandbed [zndpt I M zndbyd] headman of a district, tribe.
5906:account-book daftar.                      age dad, -siilagih; old -- pirih,
7410:rabbit xargos.                                 register daftar.
10440:daftar                              ~"'QY           gow-l
### NYB
NYB_vol2_glossary.txt:2551:(Sitz.ber. d. Kön. bay. Ak. d. Wiss. 1890, 2. Bd, 43-84). Hübschmann read the three ws. myhk' [ZY] *plzyn 221 in one: mšk*plzyn, and identified it (AG 192) with Arm maškapačen (P‘aust. Buz. p.78; there in pl.), also maškavarzan (ibd. p. 240), or maš(k)aperčan (Sebčos, not accessible to me), translating them 'the tent of the Great King'. However, these ws., which are manifestly identical but re- present a foreign term imperfactly re- produced, signify ‘accounts’ (mask 'lea- ther’ being the material used for such documents); Nor Bargirk* explains it by the terms hisäb, daftardär, daftarxäneh, and the passages quoted above refer to the regimental treasurer or treasury forming part of the field army. The w. mask (of Ass. origin) never signifies ‘tent’, only ‘skin, leather’. The semantic con- nection between méxak ‘headquarter’ and mex ‘pole’ is obvious.
### HRN
4841:Zusammenhang mit dtwän, defter (phlv. daftar nur in
### HUB
2087:halte. Np. daftar, arab. LW. daftar, diftar — gr.
10377:daftar 60.
```


## [2026-09-05T18:06:46.657Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SKT letter/literal\"; grep -n \"^LETTER\\|^LITERAL\\|^LITERATURE\" SKT.txt | head; echo \"### SKT diphtheria\"; grep -n -i \"diphther\" SKT.txt | head; echo \"### DEV/PHN/LKT diphter\"; grep -n -i \"diphter\\|diphth\" DEV.txt PHN.txt LKT.txt LAM.txt DOZ.txt 2>/dev/null | head"
}
```


### [2026-09-05T18:06:46.771Z] TOOL RESULT

```
### SKT letter/literal
### SKT diphtheria
### DEV/PHN/LKT diphter
```


## [2026-09-05T18:06:53.602Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2080,2095p' HUB.txt; echo \"=== leaf of line 2087\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(t,1):\n    if i==2087: print('leaf',leaf,'printed ~',leaf-10)\n    leaf+=l.count('\\f')\nEOF"
}
```


## [2026-09-05T18:06:54.849Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4835,4850p' HRN.txt; echo \"=== PHD leaf\"; python3 - <<'EOF'\nt=open('PHD_mackenzie.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(t,1):\n    if i in (1832,1835): print(i,'leaf',leaf)\n    leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-05T18:06:55.648Z] TOOL RESULT

```
schen Formen zum Praesensstamm iran. zdna- = np.
dana- gehSren. Vgl. dazu unten Nr. 793.
538. Np. ddh nach Vullers = 'ancilla, serva, famula.
540. Arm. dpir setzt phi. diplr voraus und macht mir
Horn's phi. dipivar nicht wahrscheinlich. F r. M u 1 1 e r
fuhrt (WZKM. 7, 376) np. dwdn ^Tribunal' auf phi.
*attvdn = arm. atean zuruck, was ich nicht fur richtig
halte. Np. daftar, arab. LW. daftar, diftar — gr.
SKp^iga (Noldeke).
541. Armenische Frauennamen mit duxt sind haufig, nur
gerade Tigranaduxt kommt meines Wissens nicht vor.
542. Zu skr. daksa- gehSrt daksina- *tuchtig, recht* = zd.
dasina-. Also ware skr. daksa- = zd. *dasa' = np.
das (nicht daooS), Vgl. Fr. Muller, WZKM. 8, 94.
546. Np. dar 'hinein, in' aus andar wie darun aus andarUft,
darx^'ar aus andarx^ar. Vgl. deutsch raus = heraus,
=== leaf of line 2087
leaf 70 printed ~ 60
```


### [2026-09-05T18:06:57.465Z] TOOL RESULT

```
d(i)blr (Inschr.); arm. LW. dpir^ talm. ^''Dl, daßtiQ
(LXX).
Die Form np. diiwer der Wörterbücher, die zu päz.
diwcr (Men.) stimmt, wird durch den Reim bezüglich
ihres e beseitigt (debtr reimt auf plr, Vfs und Rcämln,
S. 23, V. 6, auf gir Sahn. III, 1452 Vers 142)2). Den
Zusammenhang mit dtwän, defter (phlv. daftar nur in
späten Kolophonen) hat bereits de Lagarde (Ges.
Abh. 216) erkannt.
54 L diiy^ter, du/t 'Tochter'.
aw. diiydar- 'Tochter'; phlv. dtt/t^ vergl. arm.
Tif/rana]du/t; ai. dtihitdr-; arm. ditstr (Jl. No. 87).
kurd. du/t, ditt; af/. lär; wa/. da yd, sangl. da/,
minj. loyda.
*) In Vis und Rämln findet sich am Versende auch däyeyän
*Aniuie* (z. B. S. 20 Vers 13, 21 Vers 2 v. u., 22 Vers 5 v. u.), mit
=== PHD leaf
1832 leaf 44
1835 leaf 44
```


## [2026-09-05T18:07:11.182Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('PHD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'daftar' in p and 'register' in p:\n        print('leaf',i, p[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T18:07:12.944Z] TOOL RESULT

```
leaf 44 BrAy                                 23                             dahlbed elrAy [cl'" I P cr'g, N ,...,] lamp. eli [MN
leaf 150                     ENGLISH-PAHLAVI INDEX                                        129  prove uzmudan.
```


## [2026-09-05T18:07:13.302Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WLD Bd1 786\"; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# printed = leaf(1-based) - 9  => leaf = printed+9\nfor pr in (786,):\n    for lf in (pr+8,pr+9,pr+10):\n        p=pages[lf-1]\n        print('--- leaf',lf,'printed?',lf-9)\n        print(p[:900])\nEOF"
}
```


### [2026-09-05T18:07:15.141Z] TOOL RESULT

```
### WLD Bd1 786
leaves 895
--- leaf 794 printed? 785
                                                     ,




                                         dek-, dak-,’ dek
                                              7
                                                                 dekm
                                                                    o                                   785

von *dek- mit *deilc- „zeigen“ (ebenfalls mit ausgestreckter Hand) macht
dieselben Yoraussetznngen.


dek-, dek- oder (wegen des Aind.) dek-                          (:   dole-,        dek-) „reiBen, zerreiBen,
        zerfasern".
  Ai. daga „die am Ende eines Gewebes hervorragenden Zettelfaden,
Fransen"; got. tagl n. „einzelnes Haar“, anord. tagl n. „die Haare im
Pferdeschwanz" ags. tcegl (engl. tail ) „Schwanz“, ahd. sagal „Schwanz,
Stachel, mannliches Glied, Rute“; got. tahjan „reiBen, zerren", distahjan
„zerstreuen“, isl. tceja, tabi „karden“, no
--- leaf 795 printed? 786
786                                              deg-   — dem-, dema-
dt.Hand wobei de-kmt entweder als „zwei Hande“ oder „Hand“ seiber als
                ,



                       s. z. B. Thurneysen KZ. 26, 310 Anm. t,
*(d)komt aufgefaBt wird,                                          Brug-
mann aaO. 4, Pedersen KZ. 38, 410, Hirt IA. 8, 59 f., Zupitza Gutt. 183,
Stewart BB. 30, 229, v. Blankenstein IP. 21, 109 (auch unter *kom)
   Hierher idg. *k m t 6 m „bundert“ aus ** (d')kmtom ai. eat ant, av. satam,    :




gr. E-xazuv lat. centum air. cet, cymr. cant bret. leant, corn, cans, got. hund,
                     ,                ,                          ,

ahd. hunt „100‘ c anord. hund -rad ,,Gro61mndert“ (120), lit. Simtas, lett. simts
                             ,


(Miihlenbach-Endzelin III 841), aksl. szto (zur Entlebnungsfrage s. Brugmann
41, Einzelheiten ebda. 40    46).   
--- leaf 796 printed? 787
                   ;                   :                                                  ;




                                           dem-, dema-                                787

eine Folgerung aus dem Kaus. zdhmen), wozu dehnatufig got. gatemiba
Adv. „ziemend“, mnd. betame „passend“, ahd. gizdmi „ziemend, angemessen"
und tiefstufiges Abstr. ahd. zumft, mhd. zumft, zunft „Schicklichkeit, Regel,
Yerein, Zunft“.
   Gr. depco „baue“, von der set-Basis ppp. dedpppevog, dor. (Pindar) veo-
dpaxog „neugebaut", depag n. „Kdrperbau, Gestalt" (/usao-dpr) att. inschr.    ,


-pvt) „der die Mitte des Gebaudes iiberspannende Querbalken" konnte auch
fem. eines -dm-os sein).
   Aber depviov, meist PL, „Bettgestell" (Meister BB. 11, 176) wohl mit
xQtj-de/ivov „Kopfbinde“ zu deco „binde" (Pedersen KG. I 167    von den           ;


verbindenden Brettern oder Gurten?)
  ro- St. aisl. tirnbr ,,Bauh
```


## [2026-09-05T18:07:22.695Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[794]\nimport re\ni=p.find('dep')\nprint(p[1000:3000])\nEOF"
}
```


### [2026-09-05T18:07:24.452Z] TOOL RESULT

```
                            ,

anord. hundari , ahd. huntari n. „Hundertschaft, Gau“, aksl. sztorica ,,Hundert-
schaft“,lit. simteriopas „hundertartig“, s. zur Bildung Brugmann Distr. 26 f.,

auch iiber lat. decu-riu, d. abl. semenies, umbr. teqtiries und gegen Schulzes
aaO. Ansatz eines idg. *cleku- fur decu-ria got. tigu- (umbr. tekvias osk.                         ,


dekkviarim ist unklarer Bed., s. zu ersterem Laird Cl. Phil. 1, 334).

deg- „packen“?
      Got. tekan „beriihren“, anord. taka, engl. take „nehmen“; lit. dagf/s, lett. dad-
zis „Klette“ („*die packende, nicht loslassende“?), auch „Distel“ (nicht zu
*dhag- „wetzen“; auch kaum zu dheig- „stechen“ mit sekundarem Abl. *dh;>g-
auf Grand von *dhe[i]g-, Reichelt KZ. 39, 12).                          Lewy PBrB. 32, 148 Anm. 4,
KZ. 40, 563 Anm. 1                   (lat.   digitus ist fernzuhalten,      s.   Yf. LEWb. 2   s. v.,   des
gleichen      Zackc usw., s. u. dek- „rei6en‘-); unsicher. Gehort lit. dagijs zu
                    dt.
d'egti „brennen“? Ygl. Wz. clheg"h~ „brennen“ u. Miihlenbach-Endzelin I 429.

   Zupitza KZ. 37, 390 halt *deg- fiir eine idg. Anlautvariante neben *teg-
oder *tag in lat. tango usw.: alb. ndod, ndodeni „befinde mich gerade, zu-
fallig" (G. Meyer Alb. Wb. 301, zwischen beidenWzln schwankend) ware, da
dem Yelar von lit. dagf/s widersprechend, dann der letztern \Vzl. zuzuteilen.
tekan nicht zu tango mit Riickverwandlung von p zu t in der Zs. *at-pekan
(Hirt Abl. 30; lautlich zwar unanstoBig trotz Uhlenbeck PBrB. 27, 132).


deg(h)- oder dheg(h)- „eintauchen, trinken"??
      Air. deug,           mir. nir. deoch       „Trank“ (zl-St. nach Pedersen KG. II 88, vgl.
auch        I
        366, 503) lit. dazas „Tunke, Farbe“, dazyti „eintauchen, netzen,
                                 :



farben"? B. bei Fick II 4 146.


deph- „stampfen, stoBen, kneten“.
   Gr. deyco „knete, walke“, mit s-Erw. deyxo (aor. ptc. deyr/aa?) „knete;
gerbe“ (daraus lat. depso ), deya „gegerbte Haut“ (da
```


## [2026-09-05T18:07:31.796Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[794][2900:3600])\nprint('####### next leaf head')\nprint(pages[795][:700])\nEOF"
}
```


### [2026-09-05T18:07:33.371Z] TOOL RESULT

```
 mit s-Erw. deyxo (aor. ptc. deyr/aa?) „knete;
gerbe“ (daraus lat. depso ), deya „gegerbte Haut“ (dapdega „zubereitete Tier-
        £
haut ‘? Boisacq 191 m. Lit.; formantisch sehr bedenklich); arm. top'el (- etn                             ,


-eci) „schlagen“; serb. depam, depati „ stoBen, schlagen'                        1
                                                          d'epiti, d'epnuti pf. ds.  ,


(Petersson IvZ. 47, 285).
      Die von Fick I 4 453 mit               decpco verbundenen anord. Ufa, mhd. zipfett
„trippeln“,               ahd. zispan, zabalon, nhd. zappetn (die auf eine Gdbed. „mit
dem FuBe stampfen" wiesen)     siehe vielmehr u. dai-, da-p-, dd-s - „teilen“
(Fi
####### next leaf head
                   ;                   :                                                  ;




                                           dem-, dema-                                787

eine Folgerung aus dem Kaus. zdhmen), wozu dehnatufig got. gatemiba
Adv. „ziemend“, mnd. betame „passend“, ahd. gizdmi „ziemend, angemessen"
und tiefstufiges Abstr. ahd. zumft, mhd. zumft, zunft „Schicklichkeit, Regel,
Yerein, Zunft“.
   Gr. depco „baue“, von der set-Basis ppp. dedpppevog, dor. (Pindar) veo-
dpaxog „neugebaut", depag n. „Kdrperbau, Gestalt" (/usao-dpr) att. inschr.    ,


-pvt) „der die Mitte des Gebaudes iiberspannende Querbalken" konnte auch
fem. eines -dm-os sein).
   Aber depviov, meist
```


## [2026-09-05T18:07:55.907Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SYN letter\"; grep -n \"18.5[0-9] \\|LETTER (of the alphabet)\\|WRITE\" SYN.txt | head -10; echo \"### LAT littera\"; grep -n \"^littera\\|litera,\" LAT.txt | head -5; echo \"### FSD diphtheria\"; grep -n -i \"diphtheria,\" FSD_vol2.txt FSD_vol1.txt 2>/dev/null | head -3"
}
```


### [2026-09-05T18:07:56.021Z] TOOL RESULT

```
### SYN letter
31433:18.51 Write
31434:18.52 Reap
31435:18.53 Lerrer (of the Alphabet) 18.54 Letrer (= Epistle) 18.55 TABLET
31436:18.56 PAPER
31437:18.57 Pen
31438:18.58 Ink
31439:18.59 Penci
31445:18.66 AuTHor, WRITER 18.67 Portr
32310:18.51 WRITE
32330:18.52 READ
### LAT littera
3455:litteram efferebantur ): ami (de); subst. anicus, amica, ce dernier, dans
8861:litteraires ne connaissent que le deponent, e.g. Lex XII Tab., 1,3 citAe
11597:littera terminari, uelut... x^P^^C charta. - Panroman. M.L.1866. Iri.
17651:litteralenent "chef de piuda", kindins "Tiyepujov", litt^raleaent "chef
31947:litterae tuae partim laeta, partim tristia continent, Plin.J., Ep.
### FSD diphtheria
FSD_vol1.txt:16687:sj'mptoms,  as  quinsy,  diphtheria,  croup,  etc.  [L.  <   onp»).  point,  sting.l ango,  choke.] — an'gl-na  pec'to-rls,  neuralgia  of  the  heart:  an'glc*,  r.  [Rare.]  I./.  To  make  angular;  maKe  pisen; breast-pang. — Vincent’s  a.f  a   disease  or  the  throat  similar  an  angle;  drive  Into  a   corner,  as  a   billiard-ball.  11.  t.  o to  diphtheria,  but  occasioned  by  a   different  microbe,  the  ’   fio  Into  a   corner;  to  turn  at  an  angle.
FSD_vol1.txt:16694:as,  anglno-us  diphtheria,  an'gl-nalt;  an'gl-noscj.— an"gl-no-pho'bl-a,  n.  Dread  of  an  attack  of  angina pectoris.
FSD_vol1.txt:58525:Am.]  A   two- wheeled  carriage  used  In  Buenos  Aires, car'rled,  1   kar'id;  2   e&r'id,  pa.  1.  Mil.  Held  in  a   posi- tion known  as  carry:  said  of  arms.  2.  [Scot.]  Beside oneself;  transported;  rapt;  absent-minded;  distraught, car'ri-er,  1   kar'i-ar;  2   cSrii-er,  n.  1.  One  who  or  that which  carries.  Specif.;  (1)  A   person  or  company  that  under- takes to  carry  or  makes  a   business  of  carrying  persons  or goods  for  hire,  as  a   railroad  company,  expressman,  etc. (2)  One  who  or  that  which  carries  or  delivers  messages, letters,  newspapers,  etc.  (3)  A   carrier-pigeon.  (4)  A   con- duit. (5)  [Austral.]  A   water-bag,  as  for  transportation  on a   pack-animal.  (6)  Mach.  Something  that  conveys,  drives, moves,  or  supports  something  else,  (a)  A   lathe-dog  or ■•driver.  (6)  A   roller  carrying  the  material  in  a   carding-  or scribbllng-ma chine,  (c)  A   device  for  holding  or  carrying spools  or  bobbins,  as  In  a   braiding-machine,  (d)  An  auto- matic hoist  or  elevator,  (e)  The  part  of  a   magazine  gun that  brings  the  cartridge  to  the  oreech  of  the  barrel.  (7) Elec.  Same  as  proof-plane.  (8)  A   material  used  as  an Intermediary  or  vehicle,  as:  (a)  A   catalytic  agent  acting  to transfer  an  element  between  compounds,  as  a   carrier  of  hy- drogen. (6)  One  of  the  materials  used  as  a   base  to  receive the  coloring-matter  In  making  certain  coloring-substances. (9)  A   carrying-vessel  between  a   fishing-fleet  and  the  market. 2.  [U.  S.|  Anything  of  a   kind  that  will  bear  transportation withoutinjury.  3.  One  who  carries  in  his  system  virulent bacteria  of  a   disease,  as  typhoid  fever.  or  diphtheria,  that may  be  conveyed  to  others  while  he  himself  is  immune  or has  himself  recovered  from  the  disease ;   also,  any  other  me- dium, as  an  animal,  that  causes  like  dissemination.  4.  A hanger  or  supporting  piece,  as  In  car-building,  car'ry-ert- — car'rl-er*blrd",  n.  1.  A   carrier-pigeon.  2.  A   pelican. — c.«pIgeon,  n.  A   domestic  pigeon,  having  a   slender  form  and great  powers  of  flight,  trained  to  convey  from  one  place  to another  written  messages  fastened  upon  Its  neck,  wing,  or leg;  a   homing  pigeon.  See  Ulus,  under  pigeon. — c.*rlngs, n.  pi.  Metal  rings  for  supporting  the  breech-pln  of  a   gun while  loading. — c. -shell,  n.  A   xenophorold  univalve  that attaches  shells,  corals,  stones,  or  other  foreign  substances to  Its  shell. — common  c.,  a   person  or  company  that  under- takes to  carry  persons  or  goods  for  pay  when  called  to  do so,  whether  by  land  or, by  water,  and  that  is  liable  for  all loss  or  damage  during  .transportation  except  such  losses  as arise  from  natural  causes.
```


## [2026-09-05T18:07:57.007Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY دفتر\"; grep -n \"دفتر\" incoming/ARY/ARY_pages.txt | head -5; echo \"### ARY latin index\"; grep -n -i \"diphther\\|littera\" incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-09-05T18:07:57.084Z] TOOL RESULT

```
### ARY دفتر
### ARY latin index
```


## [2026-09-05T18:08:03.377Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"diph'the-ri-a\\|diph-the'ri-a\\|diphthe'ri\" FSD_vol1.txt | head -3; echo \"###\"; grep -n -o \"diphtheria[^.]\\{0,200\\}\\[[^]]*\\]\" FSD_vol1.txt | head -5"
}
```


## [2026-09-05T18:08:04.350Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '/^18.53 LETTER/,/^18.54/p' SYN.txt | head -60; echo \"=== try grep\"; grep -n \"18.53\" SYN.txt | head"
}
```


### [2026-09-05T18:08:05.130Z] TOOL RESULT

```
###
```


### [2026-09-05T18:08:06.957Z] TOOL RESULT

```
18.53 LETTER (of the Alphabet)
Grk.  -ypéypa Goth. baka Lith. raidé, litara NG -ypépa ON (bak) stafr Lett. burts
Lat. littera Dan. _bogstav ChSl. (ktiniga)
It. lettera Sw. bokstaf SCr. _slovo
Ty, lettre OE (b6c) staf Boh.  pismeno Sp. letra ME lettre, bocstaf Pol. litera
Rum. litera NE letter Russ. bukva
Ir. liter Du. letter Skt. aksara-, varna- NI. litir OHG  buohstab
W. Ulythyren MHG buochstap
Br, lizerenn NHG _buchstabe
Words for ‘letter’ (of the alphabet) are of diverse origin, but here again the Latin word has been widely borrowed.
1. Grk. ypéupa : ypadw ‘write’ (18.51).
2. Lat. littera (> Romance words), early leitera, orig. dub. Ernout-M. 557f. Walde-H. 1.814 f.
3. Ir. liter, NIr. litir, W. Uythyren,
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1286 SELECTED INDO-EUROPEAN SYNONYMS
Br. lizerenn (W., Br. with singulative suffix, the simple form is ‘epistle’), fr. Lat. littera.
4, Goth. boka, in pl. ‘writing, book’ : ON bok, OF bac, etc. ‘book’ (18.61).
ON stafr, OE stef, lit. ‘staff, stick’, prob. orig. applied to the perpendicular line which forms the basis of most runes (cf. ON ranasiafr, OF rinsief), whence transferred to the Latin letter, esp. in epd. with ‘book’, ON bokstafr, Dan. bogstav, Sw. bokstaf, OE bocstef, early ME bocstaf, OHG buohstab, etc. Falk- Torp 89f. Kluge-G. 83.
MBE lettre, NE, Du. letter, fr. Fr. lettre (above, 2).
5. Lith. raidé (now the preferred word, cf. NSB s.v. litara) beside raida ‘development’, both neologisms and ap- parently based on riedéiz ‘roll’ (cf. NSB israida ‘development’, <isriedéti ‘roll out’).
Lith. tara, litera, through Pol. litera, fr. Lat. littera.
Lett. burts, orig. ‘magic sign’ = Lith. burtas ‘lot’, pl. ‘sorcery’ : Lett. burt, Lith. burti ‘enchant, bewitch’, etc. (22.42). Miihl.-Endz. 1.355.
6. ChSI. kiiniga in pl. as ‘letters’ (Lk. 23.38, but could be simply ‘writing’ as elsewhere), usually ‘writing, book’ (18.61).
SCr. slovo = ChSL., etc. slovo ‘word’ (18.26).
Boh. pismeno : psati ‘write’ (18.51).
Pol. litera, fr. Lat. littera (above, 2).
Russ. bukva, new sg. based on Russ.- ChSl. dat. pl. bukvami% (gen. bukouit) : ChSl. *buky, pl. bukdiv ‘writing, letter’ (18.54).
7. Skt. aksara-, lit. ‘imperishable, un- alterable’ (ksr- ‘flow, melt away, wane, perish’), hence, as an unalterable ele- ment of speech, ‘speech-sound, letter, syllable, vowel, word’.
Skt. varna-, lit. ‘covering, exterior, form’ (:vr- ‘cover’), whence ‘sort, category’ and gram. ‘speech-sound, let- ter, vowel, word’.
18.54 LETTER (= Epistle)
=== try grep
31435:18.53 Lerrer (of the Alphabet) 18.54 Letrer (= Epistle) 18.55 TABLET
32358:18.53 LETTER (of the Alphabet)
32398:Grk. ypdupara, pl. of ypaupa ‘letter’ (18.53), but NG sg. ypduua ‘letter’ in both senses (ypdéupara ‘letters’ and ‘litera- ture’).
32399:2. Lat. litterae, pl. of littera ‘letter’ (18.53). Hence It. dial. littere, OFr. lettres in this sense. But sg. It. lettera,
32407:NIr. litir (also, and earlier only, ‘letter’ of the alphabet), W. llythyr, Br. lizer (whence new singulative forms for ‘let- ter’ of the alphabet, 18.53), fr. Lat. littera. Pedersen 1.234.
32411:OE stafas, pl. of stef ‘letter’ (18.53), prob. so used by the influence of Lat. litterae. Cf. also OHG buohstaba ‘lit- terae., i.e. ‘writings’ (Tat. 88.13, 104.4,
32418:ChSl. buktéivi, also ‘writing, docu- ment’, pl. of *buky, fr. the Gme. word, Goth. boka ‘letter’, pl. ‘writing, book’, etc. (18.53, 18.61). Berneker 99. Sten- der-Petersen 450 ff.
```


## [2026-09-05T18:08:16.401Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m5 -A4 \"دیفتری\" 24cef44cc01ba530.txt | head -60; echo \"SIZE:\"; wc -c 24cef44cc01ba530.txt"
}
```


### [2026-09-05T18:08:16.469Z] TOOL RESULT

```
1:URL: https://abadis.ir/fatofa/دیفتری/
2-FETCHED: 2026-09-05T18:06:08Z
3-STATUS: 200
4:TITLE: دیفتری - معنی در دیکشنری آبادیس
5-
6:دیفتری - معنی در دیکشنری آبادیس 
7-
8- دیکشنری مترجم بپرس 
9-
10: دیفتری
11- /difteri/
12-
13- معنی انگلیسی : diphtheria 
14-
--
19: دیفتری. [ ت ِ ] ( فرانسوی ، اِ ) بیماری مسری ناشی از زهر باسیلی موسوم به باسیل لوفلر ( بنام ف. لوفلر ). از علائم آن تولید غشاء کاذب در حلق و حنجره و قصبةالریه است. کمون بیماری دو تا پنج روز است و با تزریق سروم شامل ضدسم و پنی سیلین معالجه میشود. برای پیشگیری آن پادگن ( واکسن ) یا مایه مخصوص هست. آزمون «شیک » استعداد گرفتن آن را نشان میدهد. ( از دائرة المعارف فارسی ). 
20-
21- فرهنگ فارسی
22-
23- ( اسم ) ورم غشائ مخاطی یا غشائ کاذب و آن بیماری است که در گلو پدید آید و حلق و حنجره و قصبه الریه را مبتلا کند و در محل بروز پرده ای سفید بنام غشائ کاذب آشکار شود . این بیماری بسیار ساری و بومی است و بداسطه باسیل لفر به انسان سرایت میکند . 
SIZE:
11176 24cef44cc01ba530.txt
```


## [2026-09-05T18:08:29.683Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A6 \"Borrowed\\|New Latin\\|French\" 0166c4af8e0b265a.txt | grep -i -m6 -B1 -A3 \"diphth\" | head -30"
}
```


### [2026-09-05T18:08:29.732Z] TOOL RESULT

```
216-
217: French diphthérie bor. 
218- English diphtheria 
219-
220: From French diphtérie (later for a while also spelled diphthérie ) in 1857, which was coined in 1855 with the suffix -ie to replace -ite in the previous term diphtérite for the disease because it affects more than one part of the body. The previous term (later for a while also spelled diphthérite ) was coined in 1817 by Pierre Bretonneau using Ancient Greek διφθέρα ( diphthéra , “ prepared hide, leather ” ) in reference to the tough membrane that forms in the throat.
221:Bretonneau perhaps coined and used the Latin term diphtheritis (with its close imitation of Greek spelling typical of Neolatin) even earlier than the French term diphtérite , which follows the French habit of sometimes spelling t for the Latin transliteration th of Greek θ (but not, for example, in thermomètre ).
222-
223- Pronunciation
224- [ edit ] 
--
327-
328- German: Diphtherie   (de)   f 
--
410: “ diphtérie ”, in Trésor de la langue française informatisé [ Digitized Treasury of the French Language ], 2012 
411-
```


## [2026-09-05T18:08:31.628Z] TOOL CALL #63: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg118.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/118.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-05T18:08:31.739Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r-- 1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T18:08:44.001Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor fn,targets in [('AHD_watkins1985.txt',[363,366]),('SYN.txt',[32358]),('IEC.txt',[13806]),('HJB.txt',[9091]),('incoming/PLA/PLA_pages.txt',[7145])]:\n    t=open(fn,encoding='utf-8',errors='replace').read().split('\\n')\n    leaf=0\n    for i,l in enumerate(t,1):\n        if i in targets: print(fn,i,'leaf',leaf)\n        leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-05T18:08:46.958Z] TOOL RESULT

```
AHD_watkins1985.txt 363 leaf 40
AHD_watkins1985.txt 366 leaf 41
SYN.txt 32358 leaf 1379
IEC.txt 13806 leaf 562
HJB.txt 9091 leaf 381
incoming/PLA/PLA_pages.txt 7145 leaf 138
```


## [2026-09-05T18:13:26.219Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_DIPH = \"https://en.wiktionary.org/wiki/διφθέρα\"\nW_DAFTAR = \"https://en.wiktionary.org/wiki/دفتر\"\nW_LITT = \"https://en.wiktionary.org/wiki/littera\"\nE_DIPH = \"https://www.etymonline.com/word/diphtheria\"\nE_LETT = \"https://www.etymonline.com/word/letter\"\nW_DIPHT = \"https://en.wiktionary.org/wiki/diphtheria\"\nAB_DIF = \"https://abadis.ir/fatofa/دیفتری/\"\n\nPOK_NOTE = (\"Pokorny IEW 203 (POK_full.txt line 18130ff., 'Root/lemma: deph-, Meaning: to stamp, push', \"\n            \"'Page(s): 203'): 'gr. δέφω \\\"knead, drum\\\" … with s-extension δέψω … \\\"knead; tan, convert hide into \"\n            \"leather\\\" (out of it Latin depso) … διφθέρα \\\"leather\\\" (*διψτερα)'. Exactly Nourai's root name, \"\n            \"language label, page and (abbreviated) gloss.\")\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Deph\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *deph- 'to stamp, pound, knead' (Pokorny IEW 203; Walde-Pokorny I 786; Watkins/AHD deph- 'to stamp')\",\n  \"note\": (\n    \"The root box is right in every particular: Pokorny's lemma is deph- 'stampfen, stoßen, kneten' on p. 203 of \"\n    \"the IEW, which is what 'POK:203' claims, and Watkins prints it as 'deph-. To stamp.' The root is thinly \"\n    \"attested (Armenian topʿel 'hit', Greek δέφω/δέψω 'knead, tan', Serbo-Croatian depati 'shove', Polish deptać \"\n    \"'tread'), and its Greek members are the whole basis of this chart. Two cross-cutting caveats affect the \"\n    \"whole page. (1) The attachment of διφθέρα to the root is not secure: Walde-Pokorny I 786 already added \"\n    \"'(διφθέρα \\\"zubereitete Tierhaut\\\"? … formantisch sehr bedenklich)', and Beekes (EDG) argues from the \"\n    \"φ/ψ alternation that διφθέρα is Pre-Greek; Pokorny 1959 and Watkins keep it under deph-. (2) The route \"\n    \"Greek → Arabic → Persian drawn for daftar is one of two competing scholarly reconstructions. Nöldeke, \"\n    \"Hübschmann (Pers. Stud. 60) and Moʿin's footnote in Borhan-e Qateʿ take New Persian دفتر as an Arabic \"\n    \"loan from Greek; Asbaghi (PLA 124) and Wiktionary make Middle Persian daftar (from Aramaic דפתרא, itself \"\n    \"from διφθέρα) the source of the Arabic. Both routes end at διφθέρα, so Nourai's arrow is defensible but \"\n    \"compresses an Aramaic (and probably a Middle Persian) stage. The chart's own NOTE about Sumerian dub is \"\n    \"a faithful report of Moʿin, who cites Zimmern for Sum. dub 'tablet' > Akk. ṭuppu > Aramaic; modern \"\n    \"scholarship keeps that comparison alive only as an alternative to, not a component of, the IE derivation.\"),\n  \"note_fa\": (\n    \"ریشهٔ هندواروپایی آغازین *deph- «کوبیدن، فشردن، ورز دادن» در فرهنگ پوکورنی (ص ۲۰۳) و در پیوست ریشه‌های \"\n    \"واتکینز/AHD آمده است؛ نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است. بازتاب یونانیِ آن δέφω/δέψω \"\n    \"«ورز دادن، دباغی کردن» است و از همین‌جا διφθέρα «پوست دباغی‌شده» را مشتق دانسته‌اند. دو نکتهٔ کلی دربارهٔ همهٔ \"\n    \"این صفحه: نخست آنکه انتساب διφθέρα به این ریشه قطعی نیست — والده‑پوکورنی (ج۱ ص۷۸۶) آن را «از نظر ساخت \"\n    \"بسیار مشکوک» خوانده و بیکس آن را واژه‌ای پیشایونانی می‌داند؛ دوم آنکه راه «یونانی ← عربی ← فارسی» برای «دفتر» \"\n    \"تنها یکی از دو دیدگاه است: نولدکه و هوبشمان و حاشیهٔ معین بر برهان قاطع آن را وام عربی می‌دانند، ولی اسباغی و \"\n    \"ویکی‌واژه فارسی میانهٔ daftar (از آرامی דפתרא) را سرچشمهٔ صورت عربی می‌شمارند. در هر دو دیدگاه سرچشمهٔ نهایی \"\n    \"همان διφθέρα یونانی است.\"),\n  \"sources\": [W_DIPH, W_LITT, E_LETT],\n  \"ref_check\": [\n    {\"ref\": \"POK:203\", \"status\": \"supports\", \"note\": POK_NOTE}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 786 (WLD_Bd1_pages.txt leaf 795)\", \"stance\": \"partial\",\n     \"note\": \"'deph- „stampfen, stoßen, kneten“. Gr. δέφω „knete, walke“, mit s-Erw. δέψω … „knete; gerbe“ (daraus lat. depso), δέψα „gegerbte Haut“ (διφθέρα „zubereitete Tierhaut“? Boisacq 191 m. Lit.; formantisch sehr bedenklich)'. Confirms the root and its gloss, but explicitly doubts διφθέρα.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 pp. 11-12 s.v. deph- (AHD_watkins1985.txt leaves 40-41)\", \"stance\": \"supports\",\n     \"note\": \"'deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek diphthera, prepared hide, leather (used to write on): DIPHTHERIA. 2. Latin littera, letter (possibly borrowed from Greek diphthera in the sense of \\\"tablet\\\" via Etruscan) … [Pok. deph- 203.]' — the whole left half of Nourai's chart in one entry.\"},\n    {\"src\": \"POK\", \"where\": \"IEW p. 203 s.v. deph-\", \"stance\": \"supports\",\n     \"note\": \"See ref_check; Pokorny's own reference line is 'WP. I 786, WH. I 342, Schwyzer Gr. Gr. I 298, 351.'\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n  \"id\": 1,\n  \"lang\": \"Greek\",\n  \"words\": \"diphtera\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"diphtera\",\n  \"correct_form\": \"diphthera (διφθέρα)\",\n  \"derivation\": (\n    \"The word is Ancient Greek διφθέρα diphthérā 'prepared hide, tanned skin, leather (used to write on)', already \"\n    \"Mycenaean di-pte-ra (PY Ub 1318). Watkins derives it from a suffixed *deph-s-ter- of the root, i.e. *diph-ther-a \"\n    \"< δέψω 'to knead, tan' + the instrument/result suffix -τηρ/-τερα, with the regular *-ps-t- > -φθ- development \"\n    \"assumed by Pokorny ('*διψτερα'). Semantically 'the worked/tanned thing' > 'hide' > 'writing skin, parchment', \"\n    \"the sense Herodotus 5.58 uses when he says the Ionians called books διφθέραι because they wrote on goat- and \"\n    \"sheep-skins. BUT the form printed here is 'diphtera', one letter short of the standard transliteration \"\n    \"diphthera; the printed page (pdf 118, book p. 88) shows 'diphtera', so the extraction is faithful and the \"\n    \"dropped h is Nourai's own misprint (he spells the English derivative 'diphtheria' correctly two boxes below). \"\n    \"On substance the derivation is only plausible, not certain: Walde-Pokorny I 786 calls the connection \"\n    \"'formantisch sehr bedenklich', and Beekes (EDG, cited by Wiktionary) treats the φ ~ ψ alternation of \"\n    \"διφθέρα ~ διψάρα as a Pre-Greek signature. The chart's NOTE ('BQT:870 indicates that this word may have been \"\n    \"derived from Sumerian \\\"Dub\\\"') accurately reports Moʿin, who cites Zimmern for Sumerian dub 'tablet' > \"\n    \"Akkadian ṭuppu > Aramaic; that is a genuine alternative (Wiktionary lists Akk. ṭuppu and Sum. dub as \"\n    \"comparanda) but is incompatible with, not supplementary to, the IE derivation Nourai draws.\"),\n  \"derivation_fa\": (\n    \"διφθέρα ی یونانی «پوستِ دباغی‌شده، چرمی که بر آن می‌نوشتند» است و در یونانی مۆکنایی هم به صورت di-pte-ra گواهی \"\n    \"شده. واتکینز آن را از ستاک *deph-s-ter- می‌داند، یعنی از δέψω «ورز دادن، دباغی کردن» به‌علاوهٔ پسوند -τερα، با \"\n    \"تحول *-ps-t- به -φθ-؛ تحول معنایی از «چیز پرداخته» به «پوست» و سپس «پوستِ نوشتاری» است، همان که هرودت (کتاب ۵ \"\n    \"بند ۵۸) می‌گوید یونیان کتاب را διφθέρα می‌خواندند چون بر پوست بز و میش می‌نوشتند. اما صورت چاپ‌شده در کتاب \"\n    \"«diphtera» است که یک «h» کم دارد؛ تصویر صفحهٔ ۸۸ چاپی نشان می‌دهد استخراج درست انجام شده و این خطای چاپی خودِ \"\n    \"نورایی است. از نظر ریشه‌شناسی نیز این انتساب قطعی نیست: والده‑پوکورنی آن را «از نظر ساخت بسیار مشکوک» می‌خواند و \"\n    \"بیکس آن را واژه‌ای پیشایونانی می‌داند. یادداشت نمودار دربارهٔ «دوب» سومری نیز نقل درستِ حاشیهٔ معین است، ولی آن \"\n    \"فرضیه جایگزینِ اشتقاق هندواروپایی است نه مکمّل آن.\"),\n  \"sources\": [W_DIPH, E_DIPH],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. deph- (pp. 11-12): 'Suffixed form *deph-s-ter- in Greek diphthera, prepared hide, leather (used to write on): DIPHTHERIA.' Note that Watkins spells it diphthera, not diphtera.\"},\n    {\"ref\": \"BQT:870\", \"status\": \"supports\",\n     \"note\": \"The NOTE's own citation. BQT_v2_pages.txt leaf 329 (printed 869), Moʿin's footnote 7: «دوب dub در زبان سومری بمعنی لوحه و خط است. از این زبان وارد اکدی شده ṭuppu … و از این زبانها وارد آرامی شده … نقل از «لغات بیگانهٔ اکدی» تألیف Zimmern»; the continuation on leaf 330 (printed 870) adds «برخی دیگر همان کلمهٔ فارسی و هم یونانی را از کلمهٔ سامی عاریه می‌دانند».\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 203 s.v. deph-\", \"stance\": \"supports\",\n     \"note\": \"'δίφθέρα \\\"leather\\\" (*διψτερα)' listed under deph- with no query.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p. 786\", \"stance\": \"partial\",\n     \"note\": \"'(διφθέρα „zubereitete Tierhaut“? Boisacq 191 m. Lit.; formantisch sehr bedenklich)' — the connection is printed with a question mark and called morphologically very dubious.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. puta (col. ~1094, IEC.txt leaf 562)\", \"stance\": \"partial\",\n     \"note\": \"Mann uses 'littera: diphthera' as a standard example of an Etruscan-mediated Greek→Latin phonological correspondence ('for the phonol. cf. purpura: porphyra; littera: diphthera'), i.e. he takes the Greek word as the model of the Latin one but says nothing about its own IE source.\"},\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p. ~453 s.v. diphtheria (KLN_1966.txt leaf 248)\", \"stance\": \"contradicts\",\n     \"note\": \"'Gk. διφθέρα, \\\"prepared hide, leather, membrane\\\", which is of uncertain origin; it is possibly rel. to Gk. δέρειν, δέψειν, \\\"to soften\\\"' — Klein declines to put it under an IE root.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2,\n  \"lang\": \"Arabic\",\n  \"words\": \"daftar\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Arabic دَفْتَر daftar 'register, roster, account-book, notebook' (pl. دَفَاتِر dafātir) is universally agreed to go \"\n    \"back to Greek διφθέρα, but not by the direct Greek→Arabic hop Nourai draws. The Greek word passed into \"\n    \"Imperial Aramaic דפתרא / Classical Syriac ܕܦܬܪܐ (the ordinary chancery word for a parchment register in the \"\n    \"Sasanian and early Islamic Near East); from there it reached both Middle Persian dptl /daftar/ and Arabic. \"\n    \"Wiktionary, following the standard handbooks, marks the Arabic as 'possibly borrowed from Middle Persian dptl \"\n    \"(daftar), from Aramaic דפתרא or Classical Syriac ܕܦܬܪܐ'; Asbaghi's Persische Lehnwörter im Arabischen enters \"\n    \"daftar as a Persian loanword in Arabic. Phonetically the Aramaic/Iranian route explains the form well: Greek \"\n    \"-θ- is rendered by Aramaic/Iranian t, the initial di- is shortened to da-, and the Greek feminine ending -α is \"\n    \"dropped, giving the Arabic quadriliteral pattern faʿlal (daftar), from which Arabic then built dafātir, \"\n    \"daftardār etc. Nourai's arrow is therefore right about the ultimate source and about the sense development \"\n    \"('prepared hide' > 'parchment sheet' > 'file of sheets on a string' > 'register'), but it skips the Aramaic \"\n    \"(and probably the Middle Persian) link; the Arabic is a cultural loan of the 7th-8th c. dīwān administration, \"\n    \"not a direct classical borrowing.\"),\n  \"derivation_fa\": (\n    \"«دفتر» عربی (جمع: دفاتر) بی‌گمان سرانجام به διφθέρα ی یونانی می‌رسد، ولی نه با آن پرشِ مستقیمی که نورایی \"\n    \"کشیده است. واژهٔ یونانی نخست به آرامی דפתרא و سریانی ܕܦܬܪܐ رفت — که در دیوان‌های ساسانی و صدر اسلام واژهٔ \"\n    \"معمولِ «دفترِ پوستی» بود — و از آنجا هم به فارسی میانه (dptl / daftar) و هم به عربی راه یافت. ویکی‌واژه صورت \"\n    \"عربی را «احتمالاً وام‌گرفته از فارسی میانهٔ daftar، از آرامی» می‌داند و اسباغی نیز آن را در شمار وام‌واژه‌های \"\n    \"فارسی در عربی آورده است. از نظر آوایی: θ یونانی در آرامی و ایرانی به t بدل شده، di- آغازی به da- کوتاه شده و \"\n    \"پایانهٔ مؤنث یونانی -α افتاده است، چنان‌که واژه در قالب چهارحرفی «فَعْلَل» جای گرفته و از آن دفاتر و دفتردار \"\n    \"ساخته شده. بنابراین ادعای نورایی دربارهٔ سرچشمه و تحول معنایی («پوست دباغی‌شده» ← «برگ پوستی» ← «برگ‌های \"\n    \"به‌نخ‌کشیده» ← «دفتر ثبت») درست است، اما حلقهٔ آرامی (و به احتمال زیاد فارسی میانه) را حذف کرده است.\"),\n  \"sources\": [W_DAFTAR, W_DIPH],\n  \"ref_check\": [\n    {\"ref\": \"HJB:329\", \"status\": \"supports\",\n     \"note\": \"Hobson-Jobson s.v. DUFTER (HJB.txt leaf 381 ≈ printed p. 329; the book's index line reads 'Dufter, Dufterdar … 329a, b'): 'The original Arab. daftar is from the Greek διφθέρα = membranum, \\\"a parchment,\\\" and thin \\\"paper\\\" (whence also diphtheria), and was applied to loose sheets filed on a string, which formed the record of accounts; hence daftar becomes \\\"a register,\\\" a public record.' This is Nourai's arrow verbatim, including the gloss 'record, record book'.\"},\n    {\"ref\": \"KLN:487\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 s.v. dufter (KLN_1966.txt leaf 266 ≈ printed pp. 489-490; the cited 487 is within the two-page-per-leaf tolerance of this scan): 'dufter, n., a bundle of sheets of paper (India). — Hind. daftar, fr. Pers. daftar, \\\"record, office\\\", fr. Arab. daftar, fr. Gk. διφθέρα, \\\"skin, parchment, thin paper\\\". See diphtheria.' Note Klein has Arabic → Persian, as Nourai does.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 p. 124 s.v. daftar (PLA_pages.txt leaf 138)\", \"stance\": \"contradicts\",\n     \"note\": \"'daftar: \\\"Buch, Liste, Register, Material, Katalog, Ausgabenbuch, Album\\\" pers. … mp. daftar … ap. dipi \\\"schreiben\\\" od. akk. tuppi- od. griech. Diphthera \\\"Haut\\\"' — Asbaghi's whole book is Persian loanwords IN Arabic, so he reverses Nourai's arrow, though he keeps Greek diphthera as one of three candidate ultimate sources.\"},\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p. ~453 s.v. diphtheria\", \"stance\": \"supports\",\n     \"note\": \"Cross-reference 'Cp. dufter' at the end of the diphtheria entry ties the Arabic word to the same Greek etymon.\"},\n    {\"src\": \"FVQ\", \"where\": \"grep -n -i 'daftar' FVQ_pages.txt / FVQ.txt\", \"stance\": \"silent\",\n     \"note\": \"Jeffery has no entry: daftar is not a Qurʾānic word, so his Foreign Vocabulary of the Qurʾān does not treat it.\"},\n    {\"src\": \"AFM\", \"where\": \"grep 'دفتر' AFM_pages.txt / AFM_alt.txt\", \"stance\": \"silent\",\n     \"note\": \"Addi Shir has no headword دفتر (the string occurs only inside the definition of الدستور, 'الدفتر الذي…'), i.e. he does not class it as a Persian arabicism.\"},\n    {\"src\": \"LKT\", \"where\": \"grep -n -i 'daftar|defter' LKT.txt\", \"stance\": \"silent\",\n     \"note\": \"Lokotsch's dictionary of European words of oriental origin has no daftar/defter entry in the OCR text.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3,\n  \"lang\": \"Persian\",\n  \"words\": \"daftar «دفتر»\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"New Persian دفتر daftar 'account book, register, notebook; office' is the word Ḥāfeẓ uses in the couplet \"\n    \"printed in the box ('بشوی اوراق اگر همدرس مائی / که درس عشق در دفتر نگنجد'). The word certainly belongs to the \"\n    \"διφθέρα family; what is disputed is whether Persian got it from Arabic (Nourai's arrow) or gave it to Arabic. \"\n    \"(a) FOR Nourai: Hübschmann, Persische Studien no. 540 (p. 60) writes flatly 'Np. daftar, arab. LW. daftar, \"\n    \"diftar — gr. διφθέρα (Nöldeke)', i.e. NP daftar is an Arabic loanword; Moʿin tags the headword دفتر in his \"\n    \"Farhang as [معر.] 'arabicized'; Klein (s.v. dufter) likewise has 'Pers. daftar, fr. Arab. daftar, fr. Gk. \"\n    \"διφθέρα'. (b) AGAINST: MacKenzie's Concise Pahlavi Dictionary p. 23 lists 'daftar [dptl] register, \"\n    \"account-book' as a genuine Middle Persian word, and Wiktionary derives NP daftar directly from that MP form \"\n    \"(< Aramaic דפתרא < διφθέρα), making Arabic the borrower; Horn (Grundriss no. 540) qualifies this by noting \"\n    \"that Pahlavi daftar occurs 'nur in späten Kolophonen', i.e. only in late colophons, which is why the older \"\n    \"school treated the New Persian word as an Arabic re-import. Either way the word is a Greek-Aramaic culture \"\n    \"word that reached Persian through the Near-Eastern chancery tradition; and the learned plural دفاتر dafātir \"\n    \"in Persian is unambiguously borrowed back from Arabic, so at least a partial Arabic-mediated round trip is \"\n    \"real. Verdict: compatible with, but not identical to, the modern consensus.\"),\n  \"derivation_fa\": (\n    \"«دفتر» فارسی (در بیت حافظِ چاپ‌شده در همین جعبه: «بشوی اوراق اگر همدرس مائی / که درس عشق در دفتر نگنجد») بی‌شک \"\n    \"از خانوادهٔ διφθέρα است؛ آنچه محل اختلاف است جهت وام‌گیری است. در تأیید نورایی: هوبشمان در «مطالعات فارسی» \"\n    \"(ش ۵۴۰، ص ۶۰) صریحاً می‌نویسد «فارسی نو daftar وام‌واژهٔ عربی است، از عربی daftar/diftar، از یونانی διφθέρα \"\n    \"(به نقل از نولدکه)»؛ معین نیز در فرهنگ فارسی سرواژهٔ «دفتر» را با نشانِ [معر.] یعنی معرّب آورده است. در ردّ آن: \"\n    \"مکنزی در فرهنگ کوچک پهلوی (ص ۲۳) daftar [dptl] «دفتر ثبت، دفتر حساب» را واژه‌ای اصیل در فارسی میانه ثبت کرده و \"\n    \"ویکی‌واژه «دفتر» فارسی نو را دنبالهٔ همان صورت پهلوی (از آرامی דפתרא) می‌داند و عربی را وام‌گیرنده می‌شمارد؛ هرن \"\n    \"هم یادآور می‌شود که daftar پهلوی «تنها در ترقیمه‌های متأخر» دیده می‌شود، و همین سبب شده پیشینیان صورت فارسی نو \"\n    \"را معرّبِ بازگشته بدانند. جمعِ «دفاتر» در فارسی به‌یقین وام مستقیم از عربی است. ادعای نورایی با احتیاط \"\n    \"پذیرفتنی است.\"),\n  \"sources\": [W_DAFTAR, AB_DIF],\n  \"ref_check\": [\n    {\"ref\": \"BQT:869\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qateʿ ed. Moʿin, printed p. 869 = BQT_v2_pages.txt leaf 329 (the leaf carries the دفتر article and its footnotes; the estimated +543 offset in refs_online.json is ~3 leaves too high here — for this stretch printed ≈ leaf + 540). Moʿin's footnote there: «دفتر … را از یونانی diphthéra (پوست حیوانی) دانسته‌اند … دائرةالمعارف اسلام «دفتر»؛ نقل از Hobson-Jobson, Burnell et Yule: Dufter», continuing on p. 870 «از آنجا که در قدیم روی پوست کتابت می‌شده، کتاب را دفتر نامیده‌اند … هرودتس V. 58 … رابطهٔ بین دفتر پارسی با dipi پارسی باستان و ṭuppu اکدی و «دبیر» پارسی نامعلوم است». This is exactly Nourai's source and his gloss 'record book'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien no. 540, p. 60 (HUB.txt leaf 70)\", \"stance\": \"supports\",\n     \"note\": \"'Np. daftar, arab. LW. daftar, diftar — gr. διφθέρα (Nöldeke).' Hübschmann states Nourai's chain (Greek > Arabic > New Persian) in one line.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss no. 540 s.v. dibīr (HRN.txt line 4841)\", \"stance\": \"partial\",\n     \"note\": \"'Den Zusammenhang mit dīwān, defter (phlv. daftar nur in späten Kolophonen) hat bereits de Lagarde (Ges. Abh. 216) erkannt.' Horn knows a Pahlavi daftar but says it appears only in late colophons — a caution against an inherited Iranian pedigree.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 23 (PHD_pages.txt leaf 44)\", \"stance\": \"contradicts\",\n     \"note\": \"'daftar [dptl] register, account-book' is entered as a Middle Persian word, which supports the rival view that Persian did not need to borrow it from Arabic.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. دفتر (MON_part1.txt line 61985)\", \"stance\": \"supports\",\n     \"note\": \"«دفتر: [معر. … پوست، نوشتن] (اِ.) عدهٔ اوراقی که بهم پیوسته و در جلدی جای داده شده…» — Moʿin's own dictionary tags it معرّب (arabicized) and glosses the source sense as 'hide, writing', i.e. Greek διφθέρα via Arabic.\"},\n    {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary, note on mškʾplzyn\", \"stance\": \"partial\",\n     \"note\": \"Nyberg mentions Armenian maškapačen glossed by Nor Bargirkʿ with 'hisāb, daftardār, daftarxāneh' and stresses that 'mask \\\"leather\\\" being the material used for such documents' — independent confirmation of the 'leather > account-document' semantics behind the word.\"},\n    {\"src\": \"ARY\", \"where\": \"grep 'دفتر' incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n     \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry for دفتر (it treats inherited vocabulary, not loanwords).\"}\n  ]\n})\n\nN.append({\n  \"id\": 4,\n  \"lang\": \"French\",\n  \"words\": \"diphterie\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"French diphtérie (Nourai's 'diphterie' is the accentless spelling; the form was also written diphthérie for a \"\n    \"while) is a 19th-century medical coinage, not an inherited word. Pierre Bretonneau (1778-1862), physician at \"\n    \"Tours, first named the disease diphthérite / diphtérite in 1821 (Traité de la diphthérite), directly on Greek \"\n    \"διφθέρα 'prepared hide, membrane', because of the tough false membrane that forms in the throat; in 1855 the \"\n    \"suffix -ite was replaced by -ie, giving diphtérie, on the ground that the disease is not confined to one \"\n    \"organ. Nourai's gloss 'membrane, a lung disease' captures the motivation (membrane) but is imprecise about \"\n    \"the pathology: diphtheria is an infection of the pharynx, larynx and trachea, not of the lungs.\"),\n  \"derivation_fa\": (\n    \"«diphtérie» فرانسوی (نورایی آن را بدون علامتِ زیر و زبر «diphterie» نوشته است) واژه‌ای است پزشکی و ساختهٔ سدهٔ \"\n    \"نوزدهم، نه واژه‌ای موروثی. پی‌یر برُتونو (۱۷۷۸–۱۸۶۲)، پزشک شهر تور، این بیماری را در ۱۸۲۱ diphthérite نامید و \"\n    \"مستقیماً از διφθέρα ی یونانی «پوست، پرده» گرفت، چون در گلوی بیمار پرده‌ای سفت (غشای کاذب) پدید می‌آید؛ در ۱۸۵۵ \"\n    \"پسوند -ite به -ie بدل شد و صورت diphtérie ساخته شد، زیرا بیماری تنها یک اندام را درگیر نمی‌کند. معنایی که \"\n    \"نورایی داده («پرده، بیماری ریوی») انگیزهٔ نام‌گذاری را درست بازتاب می‌دهد ولی از نظر پزشکی دقیق نیست: دیفتری \"\n    \"بیماری حلق و حنجره و نای است، نه ریه.\"),\n  \"sources\": [W_DIPHT, E_DIPH],\n  \"ref_check\": [\n    {\"ref\": \"KLN:452\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 s.v. diphtheria (KLN_1966.txt leaf 248, whose running number in the OCR is 454, so printed pp. 453-454 — Nourai's 452 is within the ±2 tolerance of this two-pages-per-leaf scan): 'Medical L., fr. F. diphthérie, coined by the French physician Pierre Bretonneau (1778-1862) fr. Gk. διφθέρα, \\\"prepared hide, leather, membrane\\\" … The disease was so called by Bretonneau because it is characterized by the formation of a false membrane.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. I s.v. angina (FSD_vol1.txt line 16687)\", \"stance\": \"partial\",\n     \"note\": \"F&W treats diphtheria throughout as a throat disease ('symptoms, as quinsy, diphtheria, croup'; 'Vincent's angina, a disease of the throat similar to diphtheria'), i.e. it does not support Nourai's 'lung disease'.\"},\n    {\"src\": \"DEV\", \"where\": \"grep -i 'diphter|diphth' DEV.txt\", \"stance\": \"silent\",\n     \"note\": \"Devic's dictionary of French words of oriental origin has no entry — correctly, since diphtérie is a Greek-based neologism, not an orientalism.\"},\n    {\"src\": \"PHN\", \"where\": \"grep -i 'diphter|diphth' PHN.txt\", \"stance\": \"silent\",\n     \"note\": \"Pihan likewise has no entry.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5,\n  \"lang\": \"Persian\",\n  \"words\": \"dîfterî «دیفتری»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Persian دیفتری difterī is a 20th-century loan straight from French diphtérie, taken over with the rest of \"\n    \"European medical vocabulary through the Dār al-Fonūn and the early Pahlavi-era medical schools; the Persian \"\n    \"spelling with ی for French -ie and the stress on the final syllable are the normal treatment of French \"\n    \"medical nouns in -ie (cf. آنژین, پنومونی). Dehkhoda's Loghatnāme marks the word «(فرانسوی، اِ)» — 'French, \"\n    \"noun' — and defines it as the infectious disease caused by the Loeffler bacillus 'whose symptoms include the \"\n    \"production of a false membrane in the pharynx, larynx and trachea', which is exactly Nourai's route and gloss. \"\n    \"The word did not come through Arabic; the older Persian/Arabic name for the disease is خناق (which Moʿin's \"\n    \"dictionary glosses simply as 'دیفتری').\"),\n  \"derivation_fa\": (\n    \"«دیفتری» وام‌واژه‌ای است از فرانسویِ diphtérie که در سدهٔ چهاردهم خورشیدی همراه با دیگر اصطلاحات پزشکی اروپایی \"\n    \"(از راه دارالفنون و مدارس پزشکی) وارد فارسی شد. نگارش پایانهٔ -ie فرانسوی با «ی» و تکیه بر هجای آخر، شیوهٔ \"\n    \"معمول فارسی در برخورد با نام‌های پزشکی فرانسوی است (مانند آنژین، پنومونی). دهخدا این واژه را با نشانِ «(فرانسوی، \"\n    \"اِ)» آورده و آن را «بیماری مسری ناشی از زهر باسیلی موسوم به باسیل لوفلر … از علائم آن تولید غشاء کاذب در حلق و \"\n    \"حنجره و قصبةالریه است» تعریف کرده — دقیقاً همان مسیر و همان معنایی که نورایی نشان داده است. این واژه از راه \"\n    \"عربی نیامده؛ نام کهن‌ترِ همین بیماری در فارسی و عربی «خناق» است. ادعای نورایی درست است.\"),\n  \"sources\": [AB_DIF, W_DIPHT],\n  \"ref_check\": [\n    {\"ref\": \"MON:1593\", \"status\": \"partial\",\n     \"note\": \"The printed Moʿin vol. 2 page could not be paged to directly (the local MON OCR, MON_part1/part2.txt, has no دیفتری headword — only cross-references, e.g. «خناق … (بز.) دیفتری» at MON_part1.txt line 57506, and «آنژین‌های دیفتروئید و دیفتری» in part 2). Moʿin's practice is to tag such words [فر.] (French), and the Dehkhoda entry archived from abadis.ir gives «(فرانسوی، اِ)», so the substance of the citation is confirmed even though the page itself was not read.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, cross-references (MON_part1.txt line 57506; MON_part2.txt lines 9373, 39289)\", \"stance\": \"supports\",\n     \"note\": \"«خناق: [معر. خناک] (اِ.) (پز.) دیفتری» — Moʿin uses دیفتری as the modern equivalent of the old Arabic-Persian خناق, showing the word is the current medical term, i.e. a European loan.\"},\n    {\"src\": \"ARY\", \"where\": \"grep 'دیفتری' incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n     \"note\": \"Aryanpur's Indo-European-roots dictionary has no entry for this modern loanword.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6,\n  \"lang\": \"English\",\n  \"words\": \"diphtheria\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"English diphtheria is first attested in 1857, taken from French diphtérie/diphthérie (Bretonneau 1855) — \"\n    \"though formally it is the Modern/Medical Latin form diphtheria, since English kept the Greek-style -th- \"\n    \"spelling and the Latin -ia ending rather than French -ie; Bretonneau's earlier diphthérite had already been \"\n    \"Englished as diphtheritis (1826). The word therefore reaches English exactly as Nourai's arrow says, \"\n    \"French → English, with Medical Latin as the formal intermediary. Watkins files DIPHTHERIA under deph-, which \"\n    \"is why the node carries 'refs=AHD'.\"),\n  \"derivation_fa\": (\n    \"واژهٔ انگلیسی diphtheria نخستین بار در ۱۸۵۷ به کار رفته و از فرانسویِ diphtérie/diphthérie (ساختهٔ برتونو در \"\n    \"۱۸۵۵) گرفته شده است؛ هرچند از نظر صورت، شکل لاتینِ نو (پزشکی) diphtheria است، زیرا انگلیسی املای یونانی‌مآبِ \"\n    \"-th- و پایانهٔ لاتینی -ia را نگه داشته و پایانهٔ فرانسوی -ie را نپذیرفته است. صورت پیشین برتونو، یعنی \"\n    \"diphthérite، پیش‌تر در ۱۸۲۶ به انگلیسی diphtheritis درآمده بود. پس پیکان نمودار (فرانسوی ← انگلیسی) درست است، \"\n    \"با لاتینِ پزشکی همچون واسطهٔ صوری. واتکینز نیز DIPHTHERIA را ذیل ریشهٔ deph- آورده و ارجاع AHD در همین جعبه به \"\n    \"همان است.\"),\n  \"sources\": [E_DIPH, W_DIPHT],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. deph-, and the English index of the same volume: 'DIPHTHERIA deph-' (AHD_watkins1985.txt line 1429).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p. ~453 s.v. diphtheria\", \"stance\": \"supports\",\n     \"note\": \"'diphtheria, n., an infectious disease characterized by the formation of a false membrane in the air passages. — Medical L., fr. F. diphthérie, coined by the French physician Pierre Bretonneau…' Klein makes Medical Latin the formal intermediary, as here.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, vol. I, s.v. angina and carrier\", \"stance\": \"supports\",\n     \"note\": \"The word is current English medical vocabulary in the 1913 F&W ('anginous diphtheria'; 'virulent bacteria of a disease, as typhoid fever, or diphtheria').\"},\n    {\"src\": \"SKT\", \"where\": \"grep -i 'diphther' SKT.txt\", \"stance\": \"silent\",\n     \"note\": \"Skeat's Concise (1911) has no entry for this technical term.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7,\n  \"lang\": \"Latin\",\n  \"words\": \"litera\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Latin littera (with the by-form lītera that Nourai prints) 'letter of the alphabet', plural litterae \"\n    \"'epistle, document, literature', is of genuinely uncertain origin, and the derivation from Greek διφθέρα is \"\n    \"one of two standing hypotheses, not an established fact. It goes back to Michel Bréal, is reported \"\n    \"sympathetically by Ernout-Meillet (DELL 363) — 'since the Latin alphabet was borrowed from the Greeks through \"\n    \"the medium of the Etruscans, it is not improbable that littera itself would be of Greek origin' — and is the \"\n    \"version Watkins adopted for the AHD appendix that Nourai cites: 'Latin littera, letter (possibly borrowed \"\n    \"from Greek diphthera in the sense of \\\"tablet\\\" via Etruscan)'. The sense 'tablet' for διφθέρα is attested \"\n    \"only in a gloss of Hesychius; the phonetics require an Etruscan intermediary (Etruscan had no voiced stops \"\n    \"and no /f/-θ contrast of this kind), with d- > l- as in Latin lacrima < Greek dakruma, and the geminate -tt- \"\n    \"by the 'littera rule'. The rival etymology connects it with linō 'smear' via an Old Latin leitera (attested \"\n    \"c. 122 BC), but de Vaan calls that 'morphologically unconvincing' because the participle of linō is litus \"\n    \"with short i. Buck (Selected Synonyms 18.53) simply says 'Lat. littera (> Romance words), early leitera, \"\n    \"orig. dub.' Nourai's gloss 'the text written on animal skin, letter' overstates the case, since it presents \"\n    \"the disputed Greek etymology as the word's meaning; but the arrow itself is a legitimate scholarly position, \"\n    \"and it is the one his own reference (AHD) takes.\"),\n  \"derivation_fa\": (\n    \"لاتینی littera (با گونهٔ lītera که نورایی چاپ کرده) «حرف الفبا» و در جمع litterae «نامه، سند، ادبیات»، \"\n    \"ریشه‌ای به‌راستی نامعلوم دارد و اشتقاق آن از διφθέρα ی یونانی یکی از دو فرضیهٔ رایج است، نه واقعیتی مسلم. این \"\n    \"فرضیه از میشل برئال است، ارنو و مِیه (ص ۳۶۳) آن را با نظر موافق نقل کرده‌اند — چون الفبای لاتین از راه اتروسکی \"\n    \"از یونانی گرفته شده، بعید نیست خود واژهٔ littera هم یونانی باشد — و واتکینز نیز در پیوست AHD (همان مرجعی که \"\n    \"نورایی به آن ارجاع داده) همین را پذیرفته است. معنای «لوح» برای διφθέρα تنها در فرهنگ هسیخیوس گواهی شده، و از \"\n    \"نظر آوایی به واسطهٔ اتروسکی نیاز است، با ابدال d- آغازی به l- همانند lacrima لاتینی از dakruma یونانی، و \"\n    \"مضاعف‌شدن -tt-. فرضیهٔ رقیب واژه را با linō «اندودن» و صورت لاتینی کهن leitera پیوند می‌دهد، ولی دِ فان آن را \"\n    \"«از نظر صرفی ناپذیرفتنی» می‌خواند. باک نیز کوتاه می‌نویسد «اصل آن مشکوک است». معنایی که نورایی داده («متنی که \"\n    \"بر پوست جانور نوشته می‌شد») همان فرضیهٔ محل مناقشه را در جامهٔ معنا عرضه می‌کند، ولی خودِ پیکان دیدگاهی \"\n    \"پذیرفتنی و با احتیاط درست است.\"),\n  \"sources\": [W_LITT, E_LETT],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. deph-, sense 2 (AHD_watkins1985.txt line 366): '2. Latin littera, letter (possibly borrowed from Greek diphthera in the sense of \\\"tablet\\\" via Etruscan): LETTER, LITERAL, LITERARY, LITERATE, LITERATIM; (ALLITERATE), ALLITERATION, (ILLITERATE), OBLITERATE, TRANSLITERATE. [Pok. deph- 203.]' Note Watkins' hedge 'possibly', which Nourai's chart drops.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. letter (KLN_1966.txt line 21553)\", \"stance\": \"partial\",\n     \"note\": \"'L. littera … which is of uncertain origin. Ernout and Meillet (in DELL., p. 363) point out that since the Latin alphabet was borrowed from the Greeks (through the medium of the Etruscans), it is not improbable that littera itself would be of Greek origin. According to Bréal … littera would derive fr. Gk. διφθέρα, \\\"tablet\\\", a word glossed by Hesychius; for the change of d- to l- see lachrymal.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 18.53 'Letter (of the Alphabet)', p. 1285 (SYN.txt leaf 1379)\", \"stance\": \"partial\",\n     \"note\": \"'2. Lat. littera (> Romance words), early leitera, orig. dub. Ernout-M. 557f. Walde-H. 1.814 f.' — Buck records the word but declares the origin doubtful.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. puta (col. ~1094)\", \"stance\": \"supports\",\n     \"note\": \"Mann cites 'littera: diphthera' alongside 'purpura: porphyra' as a model of Etruscan-mediated Greek-to-Latin borrowing, i.e. he treats the equation as established enough to use as a phonological parallel.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8,\n  \"lang\": \"English\",\n  \"words\": \"letter, literature\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"The English end of the chain is uncontroversial whatever the origin of littera. LETTER: Latin littera > Old \"\n    \"French letre/lettre (10th c.) > Middle English lettre (c. 1200) 'graphic symbol, alphabetic sign', later also \"\n    \"'epistle' from the Latin plural litterae; it displaced Old English bōcstæf (cf. German Buchstabe). \"\n    \"LITERATURE: Latin litterātūra 'writing, grammar, learning' (a derivative of littera) > Old French litterature \"\n    \"> Middle English litterature, at first 'book-learning', narrowing to the modern sense of a body of writing \"\n    \"only in the 18th c. Watkins lists both LETTER and LITERATURE (with LITERAL, LITERATE, LITERATIM, ALLITERATION, \"\n    \"OBLITERATE, TRANSLITERATE) under deph-, so the node's empty refs field is covered by the AHD reference of its \"\n    \"parent.\"),\n  \"derivation_fa\": (\n    \"حلقهٔ انگلیسیِ این زنجیره، جدا از اینکه خاستگاه littera چه باشد، محل اختلاف نیست. «letter»: از لاتینی littera \"\n    \"به فرانسوی کهن letre/lettre (سدهٔ دهم میلادی) و از آنجا به انگلیسی میانه lettre (حدود ۱۲۰۰ م.) به معنی «حرف \"\n    \"الفبا»، و سپس با تأثیر جمعِ لاتینیِ litterae به معنی «نامه»؛ این واژه جایگزین bōcstæf انگلیسی کهن شد (همریشه با \"\n    \"Buchstabe آلمانی). «literature»: از لاتینی litterātūra «نوشتن، دستور زبان، دانش» — مشتق از littera — به \"\n    \"فرانسوی کهن و سپس انگلیسی میانه، نخست به معنی «دانشِ کتابی» و تنها در سدهٔ هجدهم به معنای امروزی «ادبیات». \"\n    \"واتکینز هر دو واژه را ذیل ریشهٔ deph- آورده است، پس نبودِ ارجاع در این جعبه با ارجاع AHD جعبهٔ مادر پوشیده \"\n    \"می‌شود. ادعای نورایی درست است.\"),\n  \"sources\": [E_LETT, W_LITT],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"The node carries no reference of its own; the chain is covered by the parent's AHD citation, whose index lists 'LETTER deph-' (AHD_watkins1985.txt line 1741) and 'LITERAL deph- LITERARY deph- LITERATE deph-' (line 1755).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. letter and literature (KLN_1966.txt lines 21553, 21917)\", \"stance\": \"supports\",\n     \"note\": \"'letter, n., graphic symbol, character. — ME. lettre, fr. OF. (= F.) lettre, fr. L. littera'; 'literature, n. — ME. litterature, fr. L. litteratura (literatura), \\\"writing; grammar; learning, scholarship\\\", fr. littera (litera), \\\"letter\\\".'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 18.53 and 18.54\", \"stance\": \"supports\",\n     \"note\": \"'ME lettre, NE, Du. letter, fr. Fr. lettre (above, 2)'; and at 18.54 'Lat. litterae, pl. of littera \\\"letter\\\" (18.53). Hence It. dial. littere, OFr. lettres in this sense.'\"}\n  ]\n})\n\ndoc = {\n  \"pdf_page\": 118,\n  \"book_page\": 88,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [entry]\n}\n\nwith io.open('data/verification/page-118.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 -m json.tool data/verification/page-118.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 118"
}
```


### [2026-09-05T18:13:28.250Z] TOOL RESULT

```
written
JSON OK
nodes verified: 8/8
node verdicts: {'transcription_suspect': 1, 'plausible': 3, 'confirmed': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'partial': 1, 'not_checked': 1}
books consulted: {'supports': 10, 'partial': 7, 'contradicts': 3, 'silent': 8} | by book: {'KLN': 5, 'IEC': 2, 'MON': 2, 'ARY': 2, 'FSD': 2, 'SYN': 2, 'POK': 1, 'WLD': 1, 'PLA': 1, 'FVQ': 1, 'AFM': 1, 'LKT': 1, 'HUB': 1, 'HRN': 1, 'PHD': 1, 'NYB': 1, 'DEV': 1, 'PHN': 1, 'SKT': 1}
```


## [2026-09-05T18:13:45.747Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\np='data/verification/page-118.json'\nd=json.load(open(p,encoding='utf-8'))\nn=d['entries'][0]['nodes']\nn[0]['derivation']=n[0]['derivation'].replace(\"already \\nMycenaean di-pte-ra (PY Ub 1318)\",\"already Mycenaean di-pte-ra\").replace(\"already Mycenaean di-pte-ra (PY Ub 1318)\",\"already attested in Mycenaean Greek as di-pte-ra\")\nn[3]['derivation']=n[3]['derivation'].replace(\n \"first named the disease diphthérite / diphtérite in 1821 (Traité de la diphthérite), directly on Greek\",\n \"first named the disease diphtérite / diphthérite (Etymonline dates that coinage to 1821, Wiktionary to 1817), directly on Greek\")\nassert 'di-pte-ra' in n[0]['derivation'] and 'PY Ub' not in n[0]['derivation'], n[0]['derivation'][:400]\nassert 'Traité' not in n[3]['derivation']\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write('\\n')\nprint('ok')\nPYEOF\npython3 -m json.tool data/verification/page-118.json >/dev/null && python3 tools/verify_check.py 118"
}
```


### [2026-09-05T18:13:47.707Z] TOOL RESULT

```
ok
nodes verified: 8/8
node verdicts: {'transcription_suspect': 1, 'plausible': 3, 'confirmed': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'partial': 1, 'not_checked': 1}
books consulted: {'supports': 10, 'partial': 7, 'contradicts': 3, 'silent': 8} | by book: {'KLN': 5, 'IEC': 2, 'MON': 2, 'ARY': 2, 'FSD': 2, 'SYN': 2, 'POK': 1, 'WLD': 1, 'PLA': 1, 'FVQ': 1, 'AFM': 1, 'LKT': 1, 'HUB': 1, 'HRN': 1, 'PHD': 1, 'NYB': 1, 'DEV': 1, 'PHN': 1, 'SKT': 1}
```


## [2026-09-05T18:14:06.224Z] AGENT

Page 118 (book p. 88) done — `data/verification/page-118.json`, `verify_check.py 118` shows 0 PROBLEM lines.

**Counts** — 1 entry (root *Deph*, POK:203), 8 nodes: 4 confirmed, 3 plausible, 1 transcription_suspect. Root: confirmed. Ref checks: 8 supports, 1 partial, 1 not_checked. 19 different books consulted.

**Flagged items**
- **#1 Greek `diphtera`** — transcription_suspect, `error_in: "book"`. The printed page really shows "diphtera"; the extraction is faithful, the dropped *h* is Nourai's misprint for διφθέρα / *diphthera* (he spells English "diphtheria" correctly two boxes down). Page PNG saved to `data/verification/sources/refs/ocr/BOOK/118.png`.
- Also on #1 (recorded in `derivation`, not a separate verdict): the *deph-* → διφθέρα link is asserted by Pokorny 203 and Watkins but **doubted by Walde-Pokorny I 786** ("formantisch sehr bedenklich") and rejected by Beekes (Pre-Greek). Nourai's NOTE about Sumerian *dub* is a faithful report of Moʿin (BQT footnote citing Zimmern), but that theory is an *alternative* to the IE derivation, not a supplement.
- **#2 Arabic `daftar` / #3 Persian `daftar`** — plausible, not confirmed. Both routes end at διφθέρα, but the chart's direct Greek→Arabic→Persian hop is only one of two schools: Hübschmann (Pers. Stud. 60, "Np. daftar, arab. LW. … gr. διφθέρα (Nöldeke)"), Klein and Moʿin's [معر.] tag back Nourai; MacKenzie (MP `daftar` [dptl], p. 23), Asbaghi (PLA 124, Persian→Arabic) and Wiktionary route it Greek → Aramaic דפתרא → MP → Arabic. The Aramaic stage is missing in every version of the chart.
- **#7 Latin `litera`** — plausible. The Bréal/Ernout-Meillet/Watkins Etruscan-mediated derivation from διφθέρα is a real hypothesis (and is what Nourai's own AHD citation says: "*possibly* borrowed"), but Buck calls the origin "dub." and de Vaan leaves it unknown; Nourai's gloss "the text written on animal skin" presents the disputed etymology as the word's meaning.

**Extraction errors for the owner:** none — the JSON matches the printed page exactly (words, glosses, refs, and the Hāfez couplet).

**Two small offset notes for the reference tooling** (not data errors): for Borhan-e Qateʿ vol. 2 in this stretch printed page ≈ leaf + 540, not +543 (دفتر with Moʿin's footnotes is leaf 329 = p. 869); and Klein 1966's two-page-per-leaf mapping drifts to ≈ p/2 + 22 around pp. 450–490, so KLN:452 and KLN:487 both check out.
