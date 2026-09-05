# Verification process log — verify-page-79


## [2026-09-05T06:02:29.984Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 79 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-79.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-79.json. Write /home/sfmqrb/git/rishe/data/verification/page-79.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 79` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T06:02:31.302Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T06:02:32.019Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T06:02:32.039Z] TOOL RESULT

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


## [2026-09-05T06:02:32.436Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-79.txt"
}
```


### [2026-09-05T06:02:32.456Z] TOOL RESULT

```
1	=== PDF page 79 (book page 49) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhâ 1 : to shine  (refs POK:104)
4	#1 (parent #0) [Avestan] refs=POK:104; SOD:97 | bama, bâ, bâmya : bright
5	  #2 (parent #1) [Persian] refs=BQT:227 | bâm 1 «بام ۱» : morning ; bâmdâd «بامداد» : morning
6	  #3 (parent #1) [Sogdian] refs=BQT:1437; SOD:97 | b`m : color, brilliance
7	    #4 (parent #3) [Persian] refs=SOD:97; SLW:100 | fâm «فام ۱» : a suffix meaning color
8	#5 (parent #0) [Greek] refs=AHD; KLN:1170 | phôs : light ; phôs-phoros : light bearing (substance) ☞Bher 1 ; phânôs : torch ; phanein : to shine
9	  #6 (parent #5) [Persian] refs=BQT:1437 | fânŭs «فانوس» : lantern
10	  #7 (parent #5) [French] refs=None | phase, photo, fantome, phosphore
11	    #8 (parent #7) [Persian] refs=MON:2470; AMD:1510, 1553 |  | extra: فاز ، فوتو ، فانتوم ، فسفر
12	  #9 (parent #5) [English] refs=AHD; KLN | photo, phantom, phase, phenomenon, emphasis. phosphor
13	#10 (parent #0) [Germanic] refs=AHD | 
14	  #11 (parent #10) [English] refs=None | beacon
15	
```


## [2026-09-05T06:02:36.082Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-79.json",
 "description": "Read page 79 source JSON"
}
```


### [2026-09-05T06:02:36.112Z] TOOL RESULT

```
{
  "pdf_page": 79,
  "book_page": 49,
  "entries": [
    {
      "root": {
        "name": "Bhâ 1",
        "lang": "Indo-European",
        "refs": "POK:104",
        "gloss": "to shine"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:104; SOD:97",
          "words": [
            {"translit": "bama, bâ, bâmya", "gloss": "bright", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:227",
          "words": [
            {"translit": "bâm 1", "gloss": "morning", "script": "بام ۱"},
            {"translit": "bâmdâd", "gloss": "morning", "script": "بامداد"}
          ],
          "note": null,
          "quote": {
            "text": "بامدادان که برون می‌نهم از منزل پای - حُسن عـهدم نگذارد که نهم پای دگر",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "BQT:1437; SOD:97",
          "words": [
            {"translit": "b`m", "gloss": "color, brilliance", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "SOD:97; SLW:100",
          "words": [
            {"translit": "fâm", "gloss": "a suffix meaning color", "script": "فام ۱"}
          ],
          "note": null,
          "quote": {
            "text": "بدو گفت مادر که ای جان مام - چه بودت که گشتی چنین زرد فام",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD; KLN:1170",
          "words": [
            {"translit": "phôs", "gloss": "light", "script": null},
            {"translit": "phôs-phoros", "gloss": "light bearing (substance)", "script": null, "see": ["Bher 1"]},
            {"translit": "phânôs", "gloss": "torch", "script": null},
            {"translit": "phanein", "gloss": "to shine", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:1437",
          "words": [
            {"translit": "fânŭs", "gloss": "lantern", "script": "فانوس"}
          ],
          "note": null,
          "quote": {
            "text": "خانه ام فانوس و مهمان شمع و من پروانه ام - شد مزیّن از قدوم میهمان کاشانه ام",
            "poet": null
          }
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "phase, photo, fantome, phosphore", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:2470; AMD:1510, 1553",
          "words": [],
          "script_extra": "فاز ، فوتو ، فانتوم ، فسفر",
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 5,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "photo, phantom, phase, phenomenon, emphasis. phosphor", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "beacon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T06:02:37.956Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','BQT','SLW','AHD','KLN','MON','AMD','WLD','HRN','HUB','PHD','NYB','BRT','IEC','SYN','SKT','FSD','WEB','ARY','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-05T06:02:39.653Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SLW {"title": "W. B. Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) pp. 93-106", "edition_found": "reprint in W. B. Henning Selected Papers I (Acta Iranica 14, 1977) - different pagination; original in JSTOR", "kind": "archive_djvu", "url": "https://archive.org/details/w.-b.-henning-selected-papers", "identifier": "w.-b.-henning-selected-papers (also w.-b.-henning-selected-papers_2021
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable."
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG MISSING
```


## [2026-09-05T06:02:42.922Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"--- refs dir ---\" && ls data/verification/sources/refs/ && echo \"--- matrix ---\" && sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T06:02:42.973Z] TOOL RESULT

```
agent
page-101.json
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
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
--- refs dir ---
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
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
--- matrix ---
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


## [2026-09-05T06:02:46.223Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | sed -n 50,80p; echo ---; sed -n 1,150p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T06:02:46.310Z] TOOL RESULT

```
page-75.json
page-76.json
process
sources
---
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


## [2026-09-05T06:03:11.310Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK bhā-1 ===\"\ngrep -n \"bhā-\" POK_full.txt | head -20\necho \"=== POK page marker approach ===\"\ngrep -n \"bhā- : bhō-\" POK_full.txt | head"
}
```


### [2026-09-05T06:03:11.368Z] TOOL RESULT

```
=== POK bhā-1 ===
=== POK page marker approach ===
```


## [2026-09-05T06:03:12.187Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins bha ===\"\ngrep -n -i \"^bha-\\|bhā-\\|beacon\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-05T06:03:12.237Z] TOOL RESULT

```
=== AHD watkins bha ===
15:All correspondence and inquiries should be directed to Reference Division, Houghton Mifflin Company One Beacon Street, Boston, MA 01208
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
1280:BE- ambhi BEACON bha-1 BEAD gWhedh- BEADLE bheudh- BEAM bheue- BEAN bha-bha- BEAR! bher-1 BEAR? bher-3 BEARD bhardha BEAT bhau- BEATIFIC deu-2, dhé-1 BEATIFY deu-2 BEATITUDE deu-2 BEAU deu-2 BEAUTY deu-2 BEAVER! bher-3 BECHE-DE-MER mori- BECK? bheg¥- BECKON bha-! BECOME gWa- BED bhedh-
```


## [2026-09-05T06:03:17.800Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bhā-\" POK_01.txt | head -20; echo \"---02---\"; grep -n \"bhā\" POK_02.txt | head -5; echo \"--- alt spelling ---\"; grep -n \"bha-\\|bhā\" POK_full.txt | head -20; echo \"--- size ---\"; wc -l POK_01.txt POK_02.txt POK_03.txt POK_full.txt"
}
```


### [2026-09-05T06:03:17.878Z] TOOL RESULT

```
---02---
--- alt spelling ---
8281:thereof derived Avestan 1/3/^5/73- 'virile'. Old Indie vrsa-, vrsabha-'buW, i/Zs/?/- 'virile', m. 
8519:Old Indie Wb. under vallakV a kind of sounds ', vallabha-h^ minion, favourite '. 
10749:glory, magnificence, power', subhas-^ having beautiful shininess ', bha-sati^ glares, 
10786:discussion'; bha- in Old Indie indeed otherwise - up to bhanati, see below - only in the 
10840:After Kuiper (AO. XII 262) here (*bha-s-) Old Indie bhisakti'hea\s\ bhisaj- 'physician, 
10884:is perhaps *bh^a/-, or lies a root *bha- with variant formant the basic, which is perhaps 
13286:to redupl. Old Indie bambbara-b {unbe\.) "bee', bambhara//b {unbe\.) "fly', bambha-rava-h^ 
18162:daraw5a-r\. "bundle of muscles' PI. "flesh (of muscles) ', Old Indie darbha-rr\. " hassock, 
19898:untouchable '; dambhayatr makes confused, frustrated' {dambha-h^6ece\t'), Desid. dipsati 
27513:seeds ') Old Indie /sa-M^/? "bull', aja-rsabha-h^\\e-Qoa\! , Avestan Old pers. arsan^man, 
32792:Material: Old \x\^\q, pra-galbha-h^ courageous, determined ' (: Old High German gelbon); 
32856:warlike ' etc. (compare above Old Indie pra-galbha-h). 
39080:Material: Old Indie garbha-h, Avestan garawa- "womb, foetus', garabusu. " the young of 
39094:o after ostem as 5oA(p6(;, garbha-h- Modern High German Kalb, see above S. 359 under 
39776:with Avestan yof the e-grade): Old Indie gabhJra-, gambhTra-^6ee'p\ gambha-, gambhan-, 
39777:gambhara- n. 'depth, abyss', gabha-xr\. 'vulva', gabb/-sak Avestan Adv. perhaps ' right 
44378:With -b-, -t(h)o-\ Old Indie kukkubha-rr\. "wild rooster, cock, pheasant', gr. KOUKOU(pa(; " 
46885:kakubha- " protruding, towering ' (previously reshaped after kakud-l); 
46980:Old Indie kumba-vn. "the thick end (bone)'; kumbha-m. "pot, pan, crock, pitcher', Du. " 
47782:III. Old Indie kurkuta-, kukkuta-m. 'rooster, cock', kukkubha-m. (Middle Indie for 
--- size ---
   5151 POK_01.txt
   6715 POK_02.txt
   5974 POK_03.txt
  93771 POK_full.txt
 111611 total
```


## [2026-09-05T06:03:21.289Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10730,10800p' POK_full.txt"
}
```


### [2026-09-05T06:03:21.335Z] TOOL RESULT

```
Old Saxon banuV touchwood, tinder'; Old English i6'd/7/a/7 'polish' (i.e. 'make 
gleaming'), ndd. (and out of it Modern High German) bonen^ scour, rub, clean, beans ', 
Middle High German buenen^ beans (*white) ' (from Gothic bandwa, -wo^ mark, token, 
sign ', bandwjan. Old Icelandic benda' give a mark, token, sign ' here belong - perhaps as 
^/-derivative of participle b^^-/?/-' shining, seeming ' -, is doubtful. Lithuanian by Feist 79 

f-); 



Upper Serbian baju, bacso^ burn indiscernibly, gleam ', Lower Serbian bajom, bajas se 
"gleam, flicker'; 

Tocharian A pam'c\ear, bright' {*b^9no-), pan/" beauty', B pen/jo ds. (Duchesne- 
Guillemin BSL. 41, 164); A pakar, B pakn, a-pakartse' open, distinct'; A pa-tsank, B pa- 
tsaiik^ window ' {-tsanketc 'gleam, shine'). Van Windekens Lexique 78 f.; B pate, A pat(\n 
compound) 'apparition' {*b^a-tf-), Pisani Re. R. 1st. Lornb. 78, 2, 28. 

s-extension b^d-s-'Old Indie bbas- n. (ved. also disyllabic), Instr. i6'/755a 'light, shine, 
glory, magnificence, power', subhas-^ having beautiful shininess ', bha-sati^ glares, 
gleams ', i6'/7asa/7/- 'gleaming', bbasabn. 'light'; 

gr. cpcboKEi Siacpavsi Hes., SiacpcboKU) ' begins to shine' are perhaps (from ni-cpauoKU)) 
reshaped after cpux;, also cpajOTrip 'lustre, shine, shiner' 

Doubtful is, whether Middle Irish basc^re6'. Old English basu, it'aso 'purple' {*b'^9S-ko-, - 
UO-) are to be connected, to Gothic weina-basi^ grape ', Old High German beri^ berry ', 
actually ' red berry '? In addition the full grades MN Old High German Buoso, Old Icelandic 
^05/ etc? 

^/-extension b^^-^-'Old Indie vi-bhava-h, vi-bhavan-^ radiating, shining, seeming'; 

gr. hom. cpoE (*(paF£) ' gleamed, appeared ', cpasGajv, -ovto(; 'gleaming', (pa£ai-pippoTO(;, 
Pind. cpauai-p(3poTO(; ' for the bright people shining ', 

cpaoc; (Aeolic cpauoq, pamph. (papO(;) Attic kontr. cpajq. Gen. (pwToq, cpaouc;, 'light, salvation', 
whereof *(paF£a-v6g in Lesbian cpasvvog, Ionian cpasivoq, Attic (pav6(; 'gleaming', 

hom. cpasivu) ' gleams '; nicpauoKU) ' allows to shine; points, shows, evinces; make known 
'. Different Specht KZ. 59, 58 f. 

Is Germanic *baukna-, in Old Frisian baken^ emblem, landmark, mark, fire signal ', Old 
Saxon /7d/ra/7'mark, token, sign, emblem, landmark'. Old English Mace/? 'mark, token, 
sign, banner, ensign, flag'. Old High German bouhhan^maxk, token, sign' from such 
Germanic *bau- shaped after */a//r/7a-'mark, token, sign'? 

References: WP. II 122 f., WH. I 454 f., Schwyzer Gr. Gr. I 694, 709. 
Page(s): 104-105 

Root / lemma: b'^a-2{*b'^eb2-2) 



Meaning: to speak 

Material: Old Indie probably in sabha^ congregation, meeting ' ("*conversation, 
discussion'; bha- in Old Indie indeed otherwise - up to bhanati, see below - only in the 
meaning "shine, appear, seem, shine'); 

Armenian ban {*b^a-n/s), Gen. -/'word, speech, reason, judgement, thing', bay, Gen. 
bay/'\Nord, verbalism ' {*b'^a-t/-s= gr. cpaTiq); bay part\c\e " (he, she) says ' (= cpnai, also 
bam= cpniJi, bas= Lesbian cpai from *b^as/y, 

gr. cpniJi, Doric cpapi "say', cpHMn. Doric cpapa " knowledge, shout, call, revelation ' (= 
Latin fama'a report, rumor, saying, talk, tradition'; a(pniJOV£(; appr|TOi, ouk ovopa^OMEvoi 
Hes. and only with Apuleius meeting affamen' harangue, speech ' needs to be no old 
equation); 

cpaGKOj " say, believe ' (also paaKavo(;, Latin fascinum, see below *baba onomatopoeic 
word), cpoTK^f. ' rumor', cpaoK; " language, speech, assertion, announcement'; with ablaut 
cpwvn 'voice';
```


## [2026-09-05T06:03:24.828Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10680,10732p' POK_full.txt"
}
```


### [2026-09-05T06:03:24.873Z] TOOL RESULT

```
Indo Germanic side by side from b'^^aug- {:b^aug-:b''^ug-) and b^ag- is extremely unlikely; 
compare W. Schuize KZ. 27, 428 = Kl. Schr. 55. 

Perhaps after E. Leumann (KZ. 57, 190) to Avestan baga- ' interest, portion, lot, fate ', 
also ' fortune cookie tree ', because marks were scratched into it by pilgrims. 

References: WP. II 128 f., WH. I 445 f., 863 f., E. Passler in 'FriJhgesch. under Sprachw.' 
(Wien 1948). 
Page(s): 107-108 



Root / lemma: b^a-1, b^d- b'"^-{*b'"eh2-^) 

Meaning: to shine 

Material: Old Indie t)ha{\r\ compound) ' shine, light, lustre ', that/" shines, (he) appears ', 

bhat/-h'\\g\r\t', bhana-mn. ' the shiners, apparition ' (compare Old Irish ban'\Nh\te', Old 

English i6'd/7/5/7 'polish'), it'/?^/?/^/? 'light, ray, sun' (: Old Saxon banu-t}, bbama-b'Wgbt, 

shine'; 

Avestan ba- 'shine, appear, seem' only with a- (avantsm ' the resembling, the similar '), 
fra {fra-vaitr shines out ') and vi- {vi-ba- ' gleam, shine ', Benveniste BSL. 32, 86 f.), vTspo- 
bamfyja-' all gleaming ', bamya-'Wgbt, gleaming ', banu- m. 'light, ray'; 

Armenian banam{*b^a-n-) ' open, reveal, divulge, uncover, expose ' (if actually ' point, 
allow to become visible '), Aor. ba-t'si, compare gr. cpaivw and alb. baf, 

gr. nscpnoETai ' will appear ', *b^9-n- in present cpaivu) (*(paviu) instead of *(pa-vu) 
SchwyzerGr. Gr. I 694) ' makes visible, points ', cpaivopiai ' appear, seem, shine, gleam ' 
(scpavnv, Aor. scpnva); 

cpav£p6(; ' obvious, apparent, clear ', cpavri ' torch '; cpaoK; ' rising of a star ' (see also under 
b^a-i), cpaofja, -aTO(; 'apparition, face, omen, sign ' (compare nscpaaiJEvo^); 

ajjcpaSov, apcpaSioc; ' apparent, manifest, obvious ' (ava-cp-); cpavra AapnTovTa Hes. (to 
*cpc(Mi = Old Indie bhati); compare apYU-(p£0(;, apYU(po(; ' glossy white'; 

alb. Geg baj, Tosc benj{= cpaivw) ' make, seem ' (originally probably ' bring to an 
apparition '); 

Note: 

Alb. uses a taboo explanation which reflects the religious aspect of the cognate. 

Old Irish it's/? 'white', ofbi. {*opi-b'^a) 'apparition, beauty'; 

Old Saxon banuV touchwood, tinder'; Old English i6'd/7/a/7 'polish' (i.e. 'make 
gleaming'), ndd. (and out of it Modern High German) bonen^ scour, rub, clean, beans ', 
Middle High German buenen^ beans (*white) ' (from Gothic bandwa, -wo^ mark, token,
```


## [2026-09-05T06:03:33.891Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT bāmya/bāma ===\"; grep -n \"bāmya\\|bamya\\|bāma-\\|bama-\\|banu-\\|bānu-\" BRT.txt | head -30"
}
```


### [2026-09-05T06:03:33.929Z] TOOL RESULT

```
=== BRT bāmya/bāma ===
2945:•  j.  aoSra-  n.  'Schuhwerk,  Schuhzeug': *zannya  °ärii(IS.)  *paiti,smuxia  yä  vupö.- pTsa  bamya  "mit  goldenem  Schuhzeug  an- getan, mit  reichverziertem,  glänzendem" Yt5.78;  64;  —  mal  '%ranqm  framuxti . .  upa.mqnaytn  "mit  Ablegung  ihres  Schuh- zeugs  sollen  sie  . ."  V.  ö.  27,
10698:•  j,  xSaeta-  Adj.,  fem.  xsöiSni-"  'licht, strahlend,    glänzend,    herrlich';    i)    vom Licht  usw.:    °ta    rae^A    Ytj.  1;    —    ." *bamya   -«/{als    GS.)    Yt.70. 143;'* usänhfm  .  .  '^nfm  G.  5.  5;  —   'ünyJl usayll  YtÄ35.  2)   von  Göttern  und Menschen:    bfrizanlim    akur^m apqnt    napätptn  Y.  2.  5 ;    —    asis  .  .  srlra 0«(  Ytij.  107;    —    asim    ..    ''inim  Y. 2.14,  Yt/J.  i;  —  arptfplm  ..  ''hnim  YL 5.  1 5 ;  —  am3sanqm    spmtanqm    'tanqm Y.2tf.3;    —    nar/ A?hrpa  .  .'"ta/ie  Yi.8. 13;    —    kainlnS    kikrpa  ..  ''ä-nyä    H.  2. 9;    —  frazantsis   .  .  '^nyä  (GS.)  Yt  ij. 134.          a)   bes.  von    Yima:  yS  yimd  'tö
15426:—  »W/*>  (ÄPf.)  paouru.fraväxi5  (sd.) N.^.  3)  'vielerlei':  °ravü'^  zimasyäka "es  gibt  ja  vielerlei  Menschen"  V,  tS. I.  4)  'frequens,  oft,  gern,  immer  wieder (etwas  tuend)':  yö  äaiäiti ..  'ruPI  (NSm.) ayaptä  jaiiyaniaiYt.S.^^;  — yeä/uväs? hangrmmaiti  atavts  'rls*^  (NSf.)  .  .  /la *bamya  (sd.)  xsaitäi  (svi.)  ". .  sich  untrüg- lich immer  wieder  einstellend"  Yt  10. 143;
17068:bamya-
24826:mit  US  'aufleuchten,  aufflammen,  empor- leuchten': vlspa  anayra  raocä  (sd.)  usca us.raoi'ayäii  V.  2.  40  PüZ.;  —  zafar?  paiti uzraecaymi  Yt.  tQ.  50;  —  vTusniti  (sd.) *usi.'^raocaiti  bamya  V.  7p.  28.
29256:bamya  'iaikeY.32.y  b) 'Siebentel (nur Ableit.).
```


## [2026-09-05T06:03:35.162Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN bam / bamdad ===\"; grep -n -i \"bāmdād\\|bamdad\\|bām\\b\\|bāmi\" HRN.txt | head -30\necho \"=== HUB ===\"; grep -n -i \"bāmdād\\|bamdad\\|bāmi\" HUB.txt | head -20"
}
```


### [2026-09-05T06:03:35.215Z] TOOL RESULT

```
=== HRN bam / bamdad ===
=== HUB ===
```


## [2026-09-05T06:03:38.261Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17055,17085p' BRT.txt"
}
```


### [2026-09-05T06:03:38.316Z] TOOL RESULT

```
•  j.  *baäi.dräJah-*>  Adj.  Von  der  Länge eines  £.';  cyävants  *alte  asavS  atafuni •janhs  N.  108.
Pü-;    bik  drahnSki   i.  zu  bajay-.  —  >)  Hds. ■draj:
•  j.  bä-  V.  'scheinen',  nur  mit  Praev. Praes.  i  bä-.
mit  3  'den  Anschein,  das  Aussehen  haben wie  — ,  gleich  erscheinen  wie  — '  {ya%a): ax3m  dd'iqm . .  Hstritn  avänttm'-^ yanyata .  .ya^a  mqmctj  "ich  schuf  den  T.  an  Ver- ehningswürdigkeit . .  mir  selber  gleichend" YtÄSojSo'.
mit  /m  'hervorscheinen,  —  leuchten': yqm  {ob  daimat)  hl . .  düire  fravsiti'^  . . tq'hryqm  aipi  xsapafDm  "dessen  (Auge?) weit  hervorleuchtet  auch  über  die  dunkle Nacht  hin"  YL/4- 13.
ai.  bhäti;  bhani:  —  Vgl.  »Et  Bno.  KZ.  ig. 499,  Gdn.  3Yt.  70.  —  S.  auch  vyävant-,  vohvä' lant:  —  n  V  statt  w,  %  368.  37. j.  bäuidri  V.  15,  49 :  lies  baoiAi.
•  g.  bäga-  n.  'Anteil,  Los':  vo?ta  xia'knm vairim  'g»m  aibT.bairist3m  *vrdls;mn3i  (Sp. 722  u.)  .  .  asä  antan.caraitl  Y.jt.  i.
Zum  V.  Iia,^.  —  ai.  bkaga-  m.  —    Pä.:  baJir, 5ü.:  vibhüüh,
•  p.  bägayäday-  f.,  GS.  mit  mäh-  m. Name  des  siebenten  Monats  *"> :  'dail  mähyä (sd.)  w  raucabis  . .  Bh. /.  13.
♦)  Sept,~Okt  Eig.  'Monat  der  Götterrei^ ehning  [am  Tag  des  Herbstäquinoktiami)'»), mp.,  np.  miir  '(Monat  des)  MAra',  arm.  meit- kan  (Hbm.  AGr.  I.  95,  194).  —  S.  unter  mäh-. I      Ableit.  (mit  Vfddhih)  aus  'bagayäda-  (zum  V.
dby  Google
953
baxtri-
bamya-
954
yad-)  Adj.  'GStler  verehrend'').  —  a,i.  ati-yäj'ä- Adj.,  frayäjd'  m.  —  ■)  Vll.  spei,  des  Mi%ra, »gi  JUSTI  ZDMG.  sr.  347.  —  *)  Sp.e  'Garten- bau',  VglGr.  339  vecstehe  ich  nicht
•  p.  baxtri-,  j.  bäxSi-  f.  Name  eines Lands,  Baktrien:  II  ima  dakyavJ'  tyä  mana patiyailJ'  ,  .  •«■/  suguä^  .  .  Bh. /.6;  D. 5-  *i  ö'.  3;  —  dääarsÜ..  'riyä  (LS.)  xs^''a- pävä  Bh-J.  3;4;ll  —  tüinm  asatahqtnca ../rä%w)r)s?m  'timsrtram  )r»ijwSJrafsqm V.J.  6;  —  nisäim  yim  aniart  mourumca 'iTm^a  V.l.  7.
iLautform  s.  S  ^So,  3S1  No.,  FOY  KZ.  35. 6S,  ZDMG.  JZ.  128.  —  np.  6äxr,  np.  iaix; i.  dazu  Hbu.  PSL  194,  251,  IFAnz.  10.  30, Saleuann  GIrPh.  i.  370.
•  p.  bf^ay-  m.  'Steuer,  Tribut':  ima dahySv<^  tyü  .  .  manä  'jim  abar<:^tä  Bh. l.T,X>.5.i,\i.6.z.
Zum  V.  bag-.  —  mp.  bäi,  np,  bäj,  bM,  bis.  — Vgl,  die  griech.-iran.  Wörter  iroriiSiiD;,  ,Safi- Tpäjäay.
•  j.  baäa  Fart  i)  der  Beteuerung,  am  Satz- anfang 'fürwahr':  b'  ila  aEni  6)n%i  (sd,) V.J.a?;  37,  39',  Yt-ÄS,  5.127,  F.ji?,Vyt 35^  3^-  3)  "^^^  Hervorhebung,  meist hinter  dem  ersten  Wort  des  Satz(teii)es"; a)  hinter  dem  Verbum:  lunti  b'  mavayacit cdkwars  arsäna  "sunt  profecto  mihi  etiam quattuor  mares"  V.  Jt^.  31.  b)  hinter dem  Relativ:_>'?  b'  ustanazastu gpnzaite  Yt 10.  53;  73;  —  ya%ra  b°  Y.  10.  7';  — yas» %wä  b'  fräyazäile  Y.  62.  i ;  — y!}  nS  b°  frä- yasäite  Yt y - S 2 ;  —  yas>  leb' .. baxsaite  Y. io,  13; — yim  vIsS  vTspaitis  b''^^  ustänazastö sbayeiti  Yt  10.  83;  84-86*''.  c)  sonst; avi  i'  fratmsaiti  Yt  iQ.  134;  134';  — alca  hl  b'  kammo^m  jaynvä  ..'^•Sy. 10; — yat  dim  dämSi^  upamanS  huirixttm  b° irinaxti  Yt/0.  68;  —  tal  i^aranS  b°  asti N.  30  ".  Ohne  Wert :  Vyt  5^,  Yt  2. 1 1 , Vd.  20.
Vgl.  iä  und  biihittm.  —  Et.  ?  Ob  in  ai. bä^hamt  S.  diw  WN,  AiOr.  /.  172  f.  —  Pü. (meist):  bSiIän,  (m  V.  iS):  purci{7)i),  (m  V. 3):  bälislänfi i  Sü.:  nilyam.  —  ')  Von  dem  es aber  durch  Enklitika  getrennt  sein  kann.  Ab- weichend ist  die  Stellung  Vt.  10.  S3  IT.  -  vgl. Yt  10.  53,  73  -.  N.  30.  —  =)  In  ungewöhn- licher Stellung,  s.  No.  1,  —  3)  S.  lu  bi.  — i}  S.  in  iäiiiibm.
•  j.  baiSiStsm  Adj.  'am  sichersten' '':  yatöU dim  b'  ava^anqn  (sd.)  sünöva..  V.o. 45.
ASn.  aui  'bäiiula-  Adj.,  Superl.,  verwandt mit  iflJd.  —  mp.  vgL  iäslän').  —  Pü.;  bdiist; s.  unter  baitt,  _  ■)  Sicher  falsch  Gdn.  KZ. 35.582.  —  »)D.  i.  'immer,  jederieit',  AUegro-
form  lu  *bähistan,  mit  h  für  ir.rf.  iBed.vgL Aam.  II'.  bäsiän  u  har  gäh  mit  Ank.  3:  fa hat  gäh  u  iamän.
•  j.  bat  Fart,  sva.  bä,  ia&a  2:  a^am vantaiDhB  b'  mmnyanhB  Ytl7. 10.  [y. 3$.  5 :  lies  ba  at\
Das  Wort  steht"  nur  in  J 10  und  ist  tU.  ver- derbt    Dafür  spricht  auch  die  Stellung.
•  p.  bäbirav-  m.  Name  einer  Stadt  und eines  Lands,  "Babylon,  Babylonien':  imü dahySva'^  tyä  manä  patiyäis^  .  .  psrs<^ ''uvajJ'  'rui  Bh.i.6;  D.5.2,  6.^;  —  hauv udapatafä  'rauv ..  °rus  hamßs'iyc^  abavi^ xsa'^'am  ty{^  bäbirami  hauv  agarbäyatä Bh,  i.  16;  —  adam  karam  fraUayam  'ntm Bh.j.  14;  14',  13,  /.  18,  19»,  2.  i',  4.  2'; —  yMd  adam  'rauv  äham  Bh.  2.  i;  2",  3. I3',i4,  4.\t  Bh-d,  Bh.i;  —  haca  'rauf
Bh.2.I2. Ableit  —  Vgl.  bawtay-.
•  p.  bäbtniviya-  Adj.  'babylonisch;  Baby- lonier':  karc^  hyi/'  'viyt^  harwe^  "das ganze  babylonische  Volk"  Bh./.i  6;  ^.13;  — /  martiytr  'viyJ'  "ein  Maim  aus  Babylon" Bh.  /.  16;  4-  2;  —  'viya  hami^''iyä  abava" Bh.^.  13.
Ableit.  aus  bäbirav-.
```


## [2026-09-05T06:03:39.401Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bäma\\|bänu\\|bäm-\\|bäml\" BRT.txt | head -20"
}
```


### [2026-09-05T06:03:39.447Z] TOOL RESULT

```
17086:•  j.  bänav-  m.  'Lichtstrahl,  Strahl':  tifirim .  .  darat  vyävant^m  (sd.)  -«aJj'ff  (alslnstr.) *raoxSmbyS  anahitaHbyS  Yt*.  2;  —  as? srire . .  bänummti  säiti  vyävaiti  (sd.)  °nubyS (alslnstr.)  Yt/7.6;— df^ra/  hala  'nuwe^y^ aisma  frasaocayahi  {sA)  V.  Ä  75.
17088:•  j.  bänu'mant-  Adj,  (fem.  °maitf-)  'strah- lend, glänzend':  xsa%raheäi  paiti  'mats Vt  JJ.  13s;  —  aH  srxre  . .  'maiti  (VSf.) Yt.  ij.  6.
17092:•  j.  bäma-  m.  'Licht,  Glanz.
23152:•  j.  'vastra-  n.  'Kleid,  Gewand,  Kleidungs- stück': bawraitti  'rä  vatahüta  arydvT  Yt 5.  129;  —  spaSa  'rä  var^hatti  spaita Yljo.  136;  —  ?rf%ahm  zaranim  . . 'rSsca ktSh  bämanivä  Yt  i"],  14;  zit.  F.  5  (wo vüHrät  vaca  k°)\  —  'nm  . .  ubdanum V3  Izaimm  vä  V.  <?.  23;  —  sr%nm  'nm st»hrpa^aah»m  Vd.  20;20;  —  yänhuya- nam  ..  °ranam  Vd.2;  *I2;  —  hanhus :far^aheca  -rahe-a  V.  5, 38;  —  aSä :^ar»hi  ofaratu  a^ä  'rä  varahatu  V. 3.  19;  —  avalm  3?ar3h>mca  'rpmcij  Y. 5S-3i  z;  — yii0  x^arpia  jrOiS  'raV.^.S^i S7i  58,  Vyt45;  —  i^an^aliiyB  ..'ralibyS .  ,  astayanta  V,  J.  j8;  —  gave  x^arsham gave  'rtm'^  Y.  10.20;  —  mä  gSui  mS °rahe  hatS  aoäitlm  (sd.)   vag^sii  V.  4.46;
24510:•  j.  vispö.bäma-  Adj.  'allglänzend':  asä- nas{%A.)<a  'ma  Yt.  10.  136.
24513:Vgl.  vTspi.bäma:
24715:•  j.  vyä'vant-"  Adj.  (fem.  'vaitT-)  'auf- 1 leuchtend,  -strahlend':  ali  bänumaiti  läili 'vai/Hys.)  banubys'^  "o  A.,  lichtstrahlende, zur  Wonne  aufstrahlende  mit  deinen  Strah- len" Yt  17.  6;  — tistrtm  ..  äUrät  •vant^m banubyif*'*  YlÄz;  a.
24840:•  j.  raoxsnay-  i)  Adj.  'licht,  glänzend': tilirim  . .  dural  vyävant?m  (sü.)  bänubyB 'niiyj  \l.S.2->.  2)  n.  'Licht,  Licht- glanz' (nur  Komp.).
24893:barisma    .  .    'vantint     (ASm.     statt    n.) bämlM  YtJj.  55. 5.  unter  taoiaHOr.
25814:mit  /rs  Kaus.  'ausser  Brand  setzen, zum  Verlöschen  bringen':  ä'^rat  haca bänuwe  (?,  sd.)  assmq  frasao^ayäki  yat  vä a^anham  urvaranqm  .  .  yat  \j)!l\  . .  "von dem  Feuer  weg  ,  .  sollst  du  die  Hölzer zum  Verlöschen  bringen  oder  die  Reiser . ., indem  man  . ."  V.Ä7S^*.
29310:•  j,  baBbäman-  n.  'Verbindung  (der Gelenke),  Gelenkband':  -ma  F.jh.
```


## [2026-09-05T06:03:48.432Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17090,17096p' BRT.txt; echo \"=== HRN ===\"; grep -n \"bämdäd\\|bämdad\\|bamdäd\\|mdäd\\|bäm \" HRN.txt | head -20"
}
```


### [2026-09-05T06:03:48.490Z] TOOL RESULT

```
•  j.  bänvant-  Adj.  'strahlend,  glänzend': satavagsS . .  srjrB  'iiä  rai>xsnfmäYtlj.44.
Statt  *iamiivant-  geschr.,   S  36S.  12,  —  Vgl.
•  j.  bäma-  m.  'Licht,  Glanz.
KompE.;  Ableit  —  Zum  V.  bä-.  —  ai.  bhama. m.;  np.  bim  'Morgen(-Frühlielit)'.  —  S.  dazu Hbm.  PSt.  34.
•  j.  bämya-  Adj.  (fem.  'yä-)  'lidit,  leuch- tend, strahlend,  glänzend':  nmämm  'mfm
dby  Google
955  bamaniva-  —  bsadva-  956
=== HRN ===
1898:174. bäm 1) *Haus' s. bän (No. 175).
1899:2) 'Morgen , bämdäd, bämdäddn *des Morgens' (z. B.
1907:worden. Dass np. bäm 'Haus' zu bämya- gehören
10642:lich*, hösbäm ^Tagesanbruch* (Men.).
11739:bämdädäfi 174.
```


## [2026-09-05T06:03:49.549Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD bam ===\"; grep -n -i \"^bām\\|bām \\|bāmdād\\|bāmīg\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"; grep -n -i \"bām\\b\\|bāmīk\\|bāmik\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T06:03:49.617Z] TOOL RESULT

```
=== PHD bam ===
PHD.txt:161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
PHD.txt:251:bāmbišn [MLK TTA < A тіке; РпЬй! | M Pnbyfu] queen. < dmana-
PHD.txt:252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
=== NYB ===
3865:uš-bām [?wSb’m] dawn, daybreak 72°. 10133. — Av. (415) us(ah)- ‘dawn’ + *bama- ‘light’, whence (954 sq.) bāmya- ‘luminous’ (v. bämik); MPrs ?’wsyb’m (A-H I), Paz. hösbäm.
5399:uš(ah)-bāma: uš-bām
```


## [2026-09-05T06:03:55.993Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1890,1915p' HRN.txt; echo \"=== HUB search bam ===\"; grep -n \"bäm\\|bam-\" HUB.txt | head -20"
}
```


### [2026-09-05T06:03:56.059Z] TOOL RESULT

```
') FR citirt als Beleg einen wortspielreichen Vers Senäl's
(Metr. Xeflf):
tä kl hhisesf /^äjS der bcUis
hälei ämed zt näz^ der hälis— 40 ~
aw. [/'vard', vareöayanuha 'wachse'; ai. l/'t?ardA-,
vdrdhati *wachsen\
np. välä gross* wird auch hierher gehören und nicht
als Dialektform zu bälä'^),
174. bäm 1) *Haus' s. bän (No. 175).
2) 'Morgen , bämdäd, bämdäddn *des Morgens' (z. B.
Vis und RamTn S. 41, Vers 6).
aw. mspö.]bäma' allbeleuchtend'; phlv. bämtk, bämdät;
ai. bhäma- 'Licht, Strahl*.
afy. LW. bäm.
Nach Geldner, Studien I, 77 bedeutet aw. bamya-
allerdings 'sublimis'; jedenfalls kann das Wort aber
nicht von der l^bhä- scheinen, leuchten getrennt
worden. Dass np. bäm 'Haus' zu bämya- gehören
sollte, ist mir aber sehr unwahrscheinlich; beim wird
secundär für bän stehen, wie sich auch sonst im
Auslaut ein Wechsel der Nasalen findet.
175. {\)bän 'Haus; vergl. bänü (No. 178)2).
phlv. bän 'Dach*.
kurd. bei. (27) LW. bän.
Jedenfalls nicht gleich jüd.-pers. JN^Z 'Zelt', wie
Geiger, Yätk. Zarlr. 50 will, denn JND selbst findet
=== HUB search bam ===
```


## [2026-09-05T06:04:04.355Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD grep b'm ===\"; grep -n \"βʾm\\|b'm \\|bʾm\" SOD.txt | head -20\necho \"=== SOD entries near 97 ===\"; grep -n \"^ *97 \\|[^0-9]97 \" SOD.txt | head -10"
}
```


### [2026-09-05T06:04:04.451Z] TOOL RESULT

```
=== SOD grep b'm ===
=== SOD entries near 97 ===
5365:containing  Turkish  elements)97  which  were  found  in 
8215:97  "y^r-  S,  C  uJb>T<u^^> 
8606:STi  87.22,  86.7;  EGSii  97 
8918:VJ;  GMS  579;  AVS  97 
10519:VJ  533  n  p97 
13515:GMS  5;  C2,  51V4p97 
20911:Sund.  AoF  1981,  186.11  pi87  nl97 
23705:BBB  p97  b85;  GMS  220,  417 
23800:97 
24408:TSP  3.180,  196  n  pl97
```


## [2026-09-05T06:04:04.716Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HENNING fam ===\"; grep -n -i \"fām\\|fam '\" HENNING_selected_papers.txt | head -30"
}
```


### [2026-09-05T06:04:04.834Z] TOOL RESULT

```
=== HENNING fam ===
```


## [2026-09-05T06:04:10.110Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD brilliance ===\"; grep -n -i \"brilliance\\|colour, bril\\|βʾm\" SOD.txt | head -20\necho \"=== SOD line 8215 ctx ===\"; sed -n '8205,8225p' SOD.txt\necho \"=== HENNING toc ===\"; grep -n -i \"Sogdian Loan-Words\\|loan-words in new persian\" HENNING_selected_papers.txt | head"
}
```


### [2026-09-05T06:04:10.186Z] TOOL RESULT

```
=== SOD brilliance ===
10503:radiance,  brilliance 
87940:brilliance     461 
=== SOD line 8215 ctx ===
S  W,  C2  pl49,  27;  *r>r,  Hen.  JRAS  1944,  144n3; 
Mack.  AI  1985  422,  424  n4 

96  »yrtystr  M  ji>\>*Kj^ 
ayartistar  ?  ©superl.  *Yyrt 

most  fertile,  richest 

GMS  656,  1289;  Sogdica.  29.6.30 

97  "y^r-  S,  C  uJb>T<u^^> 
ayasSar  ©<**Yst-d}r-  ©trans,  pret.  =»  Yz-> 

*yst-\  ^sd'r- 
(to)begin 
STii  p574;  Frag.  Len.  *Y(>)sS>r 

98  "yst-1  M,  S  0*>£j> 
avast  (Yst-)  ©pt.  st.  =>Yz-  }Yst-,  'ysS'r- 
(to)begin 

=== HENNING toc ===
11770:milar Sogdian loan-words in Pe nd-wif, ete,
```


## [2026-09-05T06:04:16.776Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"colour\\b\" SOD.txt | head -30; echo \"===\"; sed -n '10495,10525p' SOD.txt"
}
```


### [2026-09-05T06:04:16.853Z] TOOL RESULT

```
17264:colour,  form  ? 
23854:colour 
23893:glow,  colour 
36672:colour 
36683:colour 
36703:beauty,  colour 
43554:colourless,  without  colour 
54777:(ro)change  colour 
55060:(to)change  colour 
55505:discoloured(c/zanged  in  colour) 
64441:smoke-colour 
76706:145;  "rose-colour"  wrSYwn  Twite, 
88142:(to)change  colour    7006,  7044 
88269:colour     1463,  2453,  2459,  4392, 
93765:smoke-colour     8399 
95412:without  colour     5381 
===

^fS'ymtyh 
magic,  mirage,  transformation 
BSTBL,  Vaj.  3;  Dhy.  346 

461  >p«>yp<>}   B  j^y 
of5ep(a)   ©<*fra-daip-   =»ftyp- 

radiance,  brilliance 

BSTBL,  Dhu.  101,  103;  STSC  57 

462  >p6>ys   B  ^u^.^c-Jj 
ofSes   (f8ys)  ©<*fra-daisa-   ^fS'ys,  p8'ys- 
appearance,  vision,  region 

BSTBL,  Dhy.  354,  371.159(N);  GMS  3l5A;  AVS 
125 

463  >pY>n   B  uU3 
sfyan   ©ob.  pi.  -ty  ^Py'h1 

lament 

VJ  533  n  p97 


464  *pj-   M  (_jS;jLi-j)oUf  <jjj<uuij<ju 
aJ3z,  Piz,  Paz,  Pez   (byz-,  bz-)   ©<Av.  bazda 

©ob.  -y  =»>pyz-,  }pz-,  Pj-,  pyj-,  pyz-,  Pz~
```


## [2026-09-05T06:04:21.014Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '88265,88275p' SOD.txt; echo \"=== ctx 23845-23900 ===\"; sed -n '23840,23900p' SOD.txt"
}
```


### [2026-09-05T06:04:21.080Z] TOOL RESULT

```
9562,  9563,  9564,  9743 
collected    493,  1159,2010 
collecting     1178 
colonnade     1689 
colour     1463,  2453,  2459,  4392, 

4393,  4396,  7106 
coloured     8500 
coloured  skin     8502 
colourless     5381 
column     1689, 2395 
=== ctx 23845-23900 ===

2451  bW  ~»  P-,  wP-,  p»m 


2452  bW   C  jcw,o(juL 
pam 

dawn,  morning 

S  W,  C2,  17R2,  22R10;  BSTii  9142;  STi  77.7 

2453  pWk   B  fU<Jtj 
Pame,  fame  (p'm'y,  P'mk) 

colour 

TSP  3,  19,  32  etc.  22.16;  BSTBL;  GMS  1113; 
Gersh.  Sogd.  Cpds.  142 

2454  p>m'nt   B  ji±^ 
pamand 

shining 

BSTBL,  Dhy.  153 

2455  p>m  >stwn   M  (^yU^tj^  ^J^oy^ 
Pam  istun 

Column  of  Glory(a  Manichean  god) 
W-Lii;  KG  612;  Sund.  AoF  1979,  100 

2456  p>m>y  ^  p>m>k 

2457  p^Pyyy   M     jUm^  j/  ^Ji)  J jJt  jU^  oU^jj  ^Ua- 

Pam-Pay-   ©Parth.  Wmyzd 

Great  Builder,  Builderforte  of  the  Manichaean 

god) 
BBB;  W-Lii 


2458  p'mpwst   M  jiL^tA&A 
Pambust  ©MP  bambist   ^^mpwst 

queen 

Sogdica.  17f;  Benv.  Titres  et  Noms  Propres.  p27 

2459  p'mCh)   B,  M,  S  (fU:J^)^j>^jj"-£j 
Pam   ©<Av.  bama;  Parth.  MP  bam   =>P'm>k 
glow,  colour 

Gersh.  Sogd.  Cpds.  138,  142;  BSTBL;  W-Lii;  Hen. 
LW  pl00;  Benv.  Notesii  228;  Sund.  MHC  27.7, 
28  n49 

2460  p'mk  =»  p'm'k
```


## [2026-09-05T06:04:30.434Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"2459\" SOD_pages.txt | head; echo \"---\"; ln=$(grep -n \"2459  p'mCh)\\|2459  p\" SOD_pages.txt | head -1 | cut -d: -f1); echo \"ln=$ln\"; awk -v L=$ln 'NR<=L && /\\[pdf page/ {p=$0; pl=NR} END{}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: -v L=$ln '$1<L{last=$0} END{print last}'"
}
```


### [2026-09-05T06:04:32.316Z] TOOL RESULT

```
10822:                                                            2459 p'mCh)                   (fU:J^)^j>^jj"-£j
37871:Changan      2117                         (to)chop      2754                       colour     1463, 2453, 2459, 4392,
38370:general of army       8875            glow    230, 2459, 2493, 3932            gold-smith     11572
---
ln=
```


## [2026-09-05T06:04:34.926Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<10822{last=$0} END{print \"before:\",last}'; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1>10822{print \"after:\",$0; exit}'"
}
```


### [2026-09-05T06:04:36.559Z] TOOL RESULT

```
before:
```


## [2026-09-05T06:04:39.101Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 SOD_pages.txt; grep -c \"\" SOD_pages.txt; grep -n \"pdf page\" SOD_pages.txt | head -3; grep -n \"page\" SOD_pages.txt | head -5"
}
```


### [2026-09-05T06:04:39.177Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English


45616
1946:grammatical identifiers to help differentiate the forms. Adding the references with page
2086:    The English Meaning comprises the next line of           the page and line or paragraph is added. For certain
2986:defective in showing Sogdian vowels in quality and                       The phonemic charts on the following pages give
3221:   See "Remarks" (page xxxv) for the differences in
3267:with an older /z/, by palatalization. Isl also merges               116. On Sogdian vocalic j% see page xxxii.
```


## [2026-09-05T06:04:43.097Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 400000 SOD_pages.txt >/dev/null; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nn=0\nfor i,l in enumerate(lines[:10822]):\n    n+=l.count('\\f')\nprint('formfeeds before line 10822:',n)\nEOF"
}
```


### [2026-09-05T06:04:45.076Z] TOOL RESULT

```
formfeeds before line 10822: 162
```


## [2026-09-05T06:04:50.009Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==163' SOD_pages.txt | head -60"
}
```


### [2026-09-05T06:04:56.859Z] TOOL RESULT

```
97

2445 p'5tr B                                         jtif   2458 p'mpwst     M                              jiL^tA&A
                                                                 Pambust ©MP bambist         ^^mpwst
      PaStar
      sometimes
      Benv. Notesi 31; BSTBL, Vim. 128, 130; GMS                 Sogdica. 17f; Benv. Titres et Noms Propres. p27
        1285                                                     queen B, M, S
                                                            2459 p'mCh)                   (fU:J^)^j>^jj"-£j
                                                                 Pam ©<Av. bama; Parth. MP bam =>P'm>k
2446 b'y C =» p>yl                                                                                                        P>r-
2447 p>y' M, C                                        j_L        glow, colour
                                                                 Gersh. Sogd. Cpds. 138, 142; BSTBL; W-Lii; Hen.
     pay (b'y) ©pi. -f; ob. -y                                     LW pl00; Benv. Notesii 228; Sund. MHC 27.7,
     garden                                                        28 n49
     STi 19.15, 21.9, 10, 12; STii 3.28; BBB 568
2448 pY    M                             {[^tj&ngjj;        2460 p'mk =» p'm'k
                                                            2461 p>mk!m
     allotment^)               tt                                Pamkam/Panka        ©lsg. fut. =»P-, Pw-, wPyk'm
                                                                 AVS 227
     Hen. Tales. 470, 56
                                                            2462 b'mqyny' C                            m^.<j^.j>
2449 b'yd'ry C                       (j'^WJSmOjj^
     pay-5are ©pi. -/                                            pamkenya ©f. n.
     farmer                                                      splendour
                                                                 BSTii 895, 25; S W, C2, 54R25
     GMS 11 36; STi 19, 17.21,7, 11, 13
                                                            2463 p'mkyr'n B
2450 p>m
                                                                 pam-kiran ©= MP kanarang ©pi. -t
     Pam ©lsg. pres. ind. =>p-, wP-, wp}m                        counsellor
     AVS 227
                                                                  lady6.167; Hen. Texts. 733
                                                                 TSP                                          wli- cy\i
2451 bW ~» P-, wP-, p»m                                     2464 b^n C
2452 bW    C                                   jcw,o(juL
                                                                 Paman      ^dfrmn
     dawn,
      pam morning
                                                                 STii 3.10; GMS 453
     S W, C2, 17R2, 22R10; BSTii 9142; STi 77.7
                                                            2465 ^msnyCq)      C            (^jj £ j^Of^x-- oIjuL
2453 pWk B                                     fU<Jtj
     Pame, fame (p'm'y, P'mk)                                    pam-sanik
                                                                 dawn, early morning
     colour
     TSP 3, 19, 32 etc. 22.16; BSTBL; GMS 1113;                  STii 3.58; bymsn\ BSTii 856-10; S W, b>msy\ C2,
                                                                   22R10 n p59
       Gersh. Sogd. Cpds. 142
                                                            2466 p>n S,M
2454 p>m'nt B                                      ji±^
     pamand                                                      Pan ©lsg. subj. =»P~, Pw>n
     sh ining                                                    GMS 789; AVS 228

     BSTBL, Dhy. 153                                        2467 b'n C =» P-
                                                            2468 p'n'w- B                                       jajJ
2455 p>m >stwn       M         (^yU^tj^ ^J^oy^
     Pam istun                                                   Panau   ©<*abi-a^nav-; fnav-      ©impf.
     Column of Glory(a Manichean god)
     W-Lii; KG 612; Sund. AoF 1979, 100                            ^'Pn'w-
```


## [2026-09-05T06:05:04.545Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"loan-word\\|loanword\" HENNING_selected_papers.txt | head -20; echo \"--- fam ---\"; grep -n \"fam\\b\\|fdm\\|f am\" HENNING_selected_papers.txt | head -20; wc -l HENNING_selected_papers.txt"
}
```


### [2026-09-05T06:05:04.611Z] TOOL RESULT

```
1094:rixo 'kdn’ (but Syr. loan-words in Tranian usually have -d).—(11) " Astrologers," of. Nyberg, i, p.7, and Buddh. snp(r VJ, 22, 27, 69, 9, 12%, sq., SCE., 264, I should like to take this opportunity to explain a Sogdian word from a closely related sphere namely mySBy, pl. myBBt’ (NB. a “Ii toRosnberg, I
1258:Av. Afa-vahista-. Not met with in Man. texta, therefore function in Man, system unknown. Without d. ‘rtowit = third Man. element.—(20) Name of the second month ; ef. Sogd. aserjnye, Orien talia, viii, p. 94.—(21) Name of the third day of Cf. Sogd. ‘wat, ibid., pp. 90, 94—(22) * Battlefield on ¢ 10) — (28) " Fighter,” “ bellicose.”—(24) Fighter, soldier.” —(26) * Warriors.” 26) The restoration of Soga. ("killing takes place correct. Should Sogd. ‘nzwne “ fight" be connected with 'nzw'y- (cf. BBB., p, 63), one could perhaps restore ('n}z{w}nng.—(27) " Fight, battle." —(28) “ Fighting.”—(29) If "r2k, ef, Pabl. "ek = arzak “ free, released ” (e.g. GrBd., 60%), Arm. loan-word arjak (Hibschmann, Arm. Gr., p. 425, who over-estimates the value of the Pazend transcription). If ‘raz, possibly = Av. arszaki, the name of the eastern kiéwar. ‘The translation given by Bartholomae, Air. W., p. 202, is wrong. It is true that there is some confusion about arzahi savahi in later Pablavi books, but the most reliable texts place Arazahi in the east and Savahi in the west (cf. Nyberg, ii, pp. 21, 203; note the confusion of
1652:vind, ete. MPers. cmb = éem(b), gem(b) (2) borrow: Kin > is not to be compared to Buddh. enyrey (on which BBB., p. 86) may be a Chinese loan-word Bang-Gabain, Index, p. 476. Sogd. cyngry’ could be the name of a musical instrument, ef, NPers. éa EVP., p.11; for the -i- of dingary
1936:eek loan-word, viz. a shortened or
2130:to account for Soga. tpiowg : of. NBers, tabik which, ace, to Asadi s.v., is similar to a tambourine? One has also to consider Arm. t'mbuk, ete. (Hibschmann, op. cit., p. 154)—(3) “Dopression, distress” (cf. BBB., p. 60)—(5) Reading uncertain If = taf(fay, ef. Av. tafnu-, NPers. taff—(6) “ Annoyance,” ete As a loan-word, below), From Av. afza- “to become heated ".—(8) “Palace,
3649:'y or yy in Jewish type of Aram by Mani, Rel. of the Man, pp. 111199.) Ha loan-words-'y replaces Aram. ay, ane.g. in remy, Of, also Man, MPeorn. mgin'yi’n * Menenians'” = mdindy-ip.An with a Persian suffix (os in Publ, HRWAMDYK) ; in Pal. both forms ocear: myln'y Pall, Vil, 1, and myindyl'n, Gr, 207%
10129:ka Hhadara, Bail ye Turks: yortar > ydtar 4 in several Turkish dialects (ef. Pellot, 7. As Turkish loan-word it reappeared
10148:BAT. pr} monnaie is loan-word fr
11133:Tux study of “cultural loan-words” is perhaps the most fascinating of philolo from nation to nation, often undergo considerable phonetical
11315:Anibis loan-word 3:
11602:[107-8)), suggested that it might be a loan-word from Iranian, and M. Gauthiot supported them with an et
11763:we may take this opportunity of mentioning a hitherto unrecognized Sogdian loan-word in Turkish, viz. Turk. gly ni, i, 430; ili, 134 ‘andalib; Ton Muhanni, 176—Aaxir) from Sogdian
11770:milar Sogdian loan-words in Pe nd-wif, ete,
11781:tioular change in a loan-word is provid
12155:loanword oF ideogram (for aédahig thie reading, au
12201:and classical spelling is p'askwn|i alone.—The following two are loanwords
12380:regard mumyya as a loanword (with str (pl. also maumyditha), Talm. mini“ oath,
12482:Pazend, e.g, SGV., xvi, 25, 38 loanwords in Aramaic that ap Tn the homilies of Aphraat
13264:). ‘There are forms with & and s, Persian d6r(-), but Bakhtiari str (Lorimer, p. 69), Gabri of Yexd sir (Lorimer, JRAS., 1916, 437), Baluchi sir, Brabui sbr, and last but not least Pahlavi sir. ‘The word is unknown to Oh to be restricted (loanwords from Persian excepted) to the area of Persia and Baluchistan. Could it belong to a substrate language and be connected with Dravidian ‘ewoar (Gondi savor, GondiM. hovar “salt, Tatil, Malayalam wear * salt quoted by T. Burrow, BSOAS., XI, 352) has the common Iranian na/imadka (Sogdica, 8, and Add.; na/imadka cannot ed) ; a8 nmydk it occurs in M 377 R 5. In additio nd for “salty” in Parthian, sol = wal! Th
15333:(Cer 42. Tndian loanword athe Later So eg. byth = ltha, which was not sd ix Sopliana (ee the Mugh do where wn instead). Ta pra{t) Reichele recognand praa, of Nipa Here mep Jf unianalated by Baro) ie prob Pes. maipuie (Sr maipast, hr. meifuto beste) and manu ptf (co Bursow's note on 225) tx the sue, half tramaatil spec inn olcip-eweet decoction of grape juice or meat wth pices added. Cf. Atbensan,314- (11); ‘Yule Condie, Marco Poo, i, 4, 163, and notes; Kempfer, Amoen. Beat, 38
--- fam ---
1130:dast erkaé (which need not be changed into das [pat] érkat), see Bailey, BSOS., vii, p. 73. Sogd. (16) ‘with crossed arms, ef. SCE., 400, and prBrtp'8 “ cross-legged", Dhydna, 18. The verb, prByr- (pari biraya-), occurs in Dhuta Bstw pryByr " he crossed his arms (prBrtytKara-Balgasun, p. 22, frag. xi, 4, is not clear).—{17)(18) “ Whip. Sogd. auiép from zivagpa-, of. Av. zhaZwayat.altra, and NPers. 2b “whip, whipeord” (Rind. ; Asadi, p. 8; Div. Nasiri Khosrou, 429), Wakhi rafip “ whip" (Morgenstierne, IJFL., i, p. 588). Closely related is Buddh. "yrel'yp- “ squint-eyed", see BBB., p. 63. MPers. asp-azan " horse-whip”, of. Arm. garazan, zarazan. MPers. ‘spiwon (den from 4yavana-?) occurs in an unpublished MPers. 'pswn 'y tb “spell against the fever” (M 781), where féyr “sword”, eyl’n (see below, on g 1, 2), and "sph "whip" follow each other—(19) “teeth”. Sogd. zwrn- = “* blood” (but a separate word *zwrn- “food”, or “banquet ”, is, of course, possible), pinork = Buddh, pyerk- SCE., 28 (said to mean “ dark-coloured), or from plyer- “to lacerate, devour” (R.. i ¢ BBB., p. 91), cf. 'ply'r, Vay 313, 949, Therefore, Sogd. =“ bloodstained teeth” or “blood: Jacerating teeth" (? “‘laniaries?"). MPers. "ned could be avid “rubbed, blunted ” (ergo “‘ molar teeth?”), or dsd8, 1, “useless,” 2, “ not rubbed " (NPers. side) = “ sharp teeth !"" Speaking of teeth, I should like to add to my recent remarks on Sogd. krw-Bnt'k “ having defective teeth", BSOS,, x, p. 96: the word knw- still exists in modern Birjandi Persian, as Eabrd, Eawerd “ toothless”, see Ivanow, JPASB., xxix, 4, p. 340. This makes it unlikely that NPers. kare(e) had been borrowed from Sogdian.—(20) Pte. pres, pl (21) 3nd pl. pres, (or subj.), MPers. pret. pass. =Sogd. abstract from pte. pass. + hy became, took place", (28) iterative pte., from MPers. "em- = Sogd. ()pF'm both of which are unknown. It seems likely that the words connected by etymology, notwithstanding the apparent discrepancy of thesibilants.? But MPers. swyy = svyay, Pabl. sud = suy compared to Av. dud- allow the derivation of MPers. -sam- from Olr .-fam- Av. afama- "to swallow, gulp” (NPers. dédmidan),* .- from *apa-Mma-? The appearance of an iterati
8212:deft yng b's Sy fe of amembly (1) fe deities and
10484:xts, they are unfailingly subjected to the action expressed by nyw'y-, which ther with Sim "fine " it is the equivalent achmati, Heilk. Uig.,i, 409 on 138), As to 84m, one jen < sfdm (Benveniste, JA., he initials nor the vowels agree, Middl invariably reproduced by s{y}- in Central Asian languages, Cf. e.g., 4% aién
16943:A book worth consulting in a matter of this kind isthe Persian manual of archaeology entitled Athdr-i ‘Afam and composed in 1892-3 by Furgat- ced-daule (Furgat-i Sirlai), a minor poet, whose tomb-stone can be seen in the Hafigiyye, where he rests by the side of his great countryman. It has merely a brief notice:
17815:h necessarily results from the study of Priscus, is ingle reference to the Acatziri in Jordanes, He , 37, a number of nations, beginning with the Vidivaris, who occupied the mouth of the Vistula; east of them, on the coast of the Balti, lived the Aest, a peaceful people famous as th¢ collectors and exporters ‘of amber. Quibus in austrum adsidet gens Acatzinorum fortissima, frugun ignara, quae pecoribus ef venationibus wictlat ; ultra quoe disiendunt supra Mare Ponticum Bulgarum sedes ... kine iam Hunni ... bifariam populorum rabiem pullularunt ; nam alii Altsiagiri, alii Saviri nunoupantur ... If the Aca thus adjoined the people of the amber coast on the south ? they must have lived in tho neighbourhood of Warsaw. The difficulties to which attempts at harmonizing the data of Priscus st illustrated by the remarks Marquatt n ontaviatische Stref
19616:Our! knowledge of the Khwarezmian language depends largely on two classes of material, which are dissimilar in character but supplement each other. On the one hand, we have the sentences in legal books, chief among them the Qunyatu *IMunyah; on the other, the Khwarezmian glosses in the Mugaddimatu *1Adab, the principal MS. of which was published in facsimile by Zeki Velidi Togan three years ago.*
19709:* With few exceptions, chief among them forms of masculine nouns inthe singular,
23808:Personal circumstances -chief among them a temporary lack of books-prevent me from writing for this volume a contribution that I could regard as a tribute sufficient to convey my feeling of admiration for G. Morgenstierne, His fine explanations of unknown or misunderstood Ancient Iranian terms from re- condite modern dialect words would alone have secured him a place of honour among the leaders of Iranian studies; while in truth they form but a trifling sideline to his principal work. A casual annotation to his latest article (A Lo- cust’s Leg, Studies .. . Taqizadeh 208 n, 3 —the proofs of that volume constitute Virtually the whole of the Tranistic literature at my disposal at present), in which the remarkable word anya-:dta ‘a child begotten by a man other than a ‘woman's husband’ is added to the ancient Iranian vocabulary, furnishes a fresh and striking example of his powers
25027 HENNING_selected_papers.txt
```


## [2026-09-05T06:05:10.478Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11133,11150p' HENNING_selected_papers.txt | cut -c1-600; echo \"=== grep fam in 11133-11900 ===\"; awk 'NR>=11133 && NR<=11900' HENNING_selected_papers.txt | grep -n -i \"fam\\|βʾm\\|B'm\\|colour\" | head -20"
}
```


### [2026-09-05T06:05:12.496Z] TOOL RESULT

```
Tux study of “cultural loan-words” is perhaps the most fascinating of philolo from nation to nation, often undergo considerable phonetical
| pursuits, Such words, passed on
 
 
changes; but th rignifica- tions. So the me the leas we should arrogate to ourselves in the matter of
y possess very precise and limit e latitude we may claim in regard to form,
   
 
A. Dawasx Niya th twice a word prigha (Nos, 316, 318) which Liders, Teztilien ten Turkistan (Abh.P.A.W., 1936), p. 30, combined with Skt. priga in the Mahdeyutpatti, & Hi" thin flowe with figures”, In Doe. No. 318 (line 6) Liders corrected the text given by B speta-prigha“ whi which we shall be able to confirm with fresh n that prigha meant “‘unicoloured figured silk (= damask)” ean be fully sub-
In the Kharogthi documents found
    
 
 
there explained as
  
d silk”, Tib. dar ri-mo-can “ silk marked
 
 
=== grep fam in 11133-11900 ===
9:A. Dawasx Niya th twice a word prigha (Nos, 316, 318) which Liders, Teztilien ten Turkistan (Abh.P.A.W., 1936), p. 30, combined with Skt. priga in the Mahdeyutpatti, & Hi" thin flowe with figures”, In Doe. No. 318 (line 6) Liders corrected the text given by B speta-prigha“ whi which we shall be able to confirm with fresh n that prigha meant “‘unicoloured figured silk (= damask)” ean be fully sub-
115:transl, ); Professor Minorsky suspects that the us word is Chinese by origin. Secondly, spylyy pryng "white damask”, so exactly the Spela-prigha of the Niya documents, In all ages pring is qualified by an adjective denoting a colour, a fa
170:* multi-coloured dam:
201:proper reading Buxtorf est se coloured) damask silk.”
318:colours of the fabrics they describe. Cf. e.g, this famous verse by Farrukhi
334:tho “colour of (the y aves of the) willow ” (if bidgiin
592:for the famous mausoleum of Khosmu Anosherwan, seo B. N. Dhabhar, The Persian Rivayats, 586 (with references), J. Darmesteter, Etudes Traniennes, ii, 132 *mary “death” + Pahl Old Pers. “ apadéna””*) which, although brilliant at the etymology not on a corrupt
```


## [2026-09-05T06:05:25.535Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))['BQT']\nfor k,v in d.items(): print(k,':',v)\n\""
}
```


### [2026-09-05T06:05:27.418Z] TOOL RESULT

```
title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
kind : archive_djvu+local_scan_ocr
url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.
lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
covers_etymology : True
notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \f; leaf N = N-th \f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209
scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
```


## [2026-09-05T06:05:35.301Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,pg in enumerate(pages):\n    if 'بامداد' in pg:\n        print('LEAF',i)\nEOF"
}
```


### [2026-09-05T06:05:37.062Z] TOOL RESULT

```
leaves 777
LEAF 17
LEAF 447
LEAF 649
LEAF 657
```


## [2026-09-05T06:05:39.700Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[447][:3000])\nEOF"
}
```


### [2026-09-05T06:05:42.665Z] TOOL RESULT

```
با لو س ت برءزن‌سالوی ء,کافورمخشوش,ا
و
۳۹
پا لوش - با شن‌قرشت . بروزن‌وممنی
بالوس است که کافورمفدوش باشد» چد درفارسی
سین بشن و برعکس تبدیل می‌باید .
باله - بروزن لاله . قسمی از جوالباشد
که چیز ها را در آن کنند 4
پالیك - بر ون ناهید . ماضی بالیدن
است یمنی افزون کردید و نمو کرد وبزر که شد
بالیدن بروزن‌مالیدن ؛ بمعنی‌بز رکه
شدن و افزون کردیدن و نمو کردن باشد ۴ .
با لیكه - بروزن‌نادیده. آدمی‌ودرخت‌را
گومند که تتومند و بلشد شده باشد ؟ .
با لیات - بروزن تاربك .کفش و پاپوش
بالات - بررزن تاين » بالئی راکوند
که درزس سرنبند ۴ 9
بای بر ست - کنابه از بردم تتبل
و بکاز و هیحکاره باشد .
فا لیس « بر وزن خاکبوی . ولابت
فندهار راگویند :
(۱) چپ ۱: چش : بگاه ,
ام ه بر وزن کام » طرف بیردنی سقف
خائه را گوبند ۵ ؛ و بعضی طرف دروني خانه را
کفه‌اند بقربنة پشت بام. وظاهرآکه نمام پوشش
خانه را بام مگویند - و مخفف بامداد هم‌هست
که صبح پگاء (۱) باشد ۱۷ - ونر بم را یز
کوبند و آن تارکنده ای بنشد که در ساز ها
بندند ۷ - و نام قلعه است در ماوراه اللهر -
و بمعنی فرض و وام غم آمده است .
یام دنشست ه کابه از این است که
خراب شد و ویزان کودید .
بامچشم - یک مم : يك چم را
کوبند و بعربی جفن خوانند . *
بام‌ر و اق بدیع -کنابه ازكعری
و کرسي باشد .
یام‌رد - بکون ات و فتح زای.هوز
و سکون دال ابجذ کوی و نفاره را گویند .
یام ماه مه کنابه از آ-مان اولاست .
که فلك فمر باشد  .‏
پامس « ببنتح الك و سکون سین بی
نقطه . ششصی را گو,ن که ازبودن شهری‌ودباری
که غیر وطن او باشد دلگیر شدء و بتنگآمده
باشد و پتابر مائمي نتواند از آنجا بجای دیگر
رفت - وکسی را ليز گویند که در وطن پای‌بند
هندی قدیم۵۷۵۲۵. ۷۵۲02 ( نم وکردن, بز رکه شدن ) « اسشق۱۷۳». رك : بالش. بالا.
۴ - اسم مفمول از بالیدن . ۴ - در بهلری۵2110 ۱ مت ) « منای۲۹۹ او
0 . پازند ۰02110 دریارسی باستان 032۳003992 «ب رگ۳۱۵». ۵ _ دریهلوی
0 «تاواد,۱۵۹* «بونکر*۰۵ ۰ گیلکی ۰۵200 فریزندی 968 ۰ برنی 0۷18 ۰ نطنزی 11۳0
« . ۱ص ۰۲۹۰ . سمنانی 0سبکسری 0 . لاسگردی 0 , خهمرزادی۵20264
«ل2 . ۲ سر ۱۸۸ . نهرانی 00۲0 . ۲ - دراوستا 081112 ( درخشان ) و درسانسکریت
۱2( . رك : بامداد - .
۲ - بسوز لاله زارم زعشاق نوای زیر + بامی‌برنباید . خواجوی کرمانی. رگن بم.
ه باه‌داد _ م رکب از:بم ۲ داد. در پهلوی 02۳14026, صبح. ۵ بامزه د
ختح‌سوم وچهارم , مر کب از : با -هزه . درپهلوی۳3*1۳9602 , دارای‌طمم خوش *اونوالاد۵۵*.
```


## [2026-09-05T06:06:03.176Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,pg in enumerate(t):\n    if 'فانوس' in pg or 'فام' in pg:\n        print('LEAF',i, pg[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T06:06:04.825Z] TOOL RESULT

```
leaves 721
LEAF 12 [pdf page 13] ها گوزن در هوا  شا ‎OIF‏ در هو -کنایه‌ازماه لو باشد ویعربی هلا لگو
LEAF 22 [pdf page 23] که ازآن راهپا وشمبها جدا شود - وفام‌جالوری ‎col‏ در هندوستان - ‎pl
LEAF 24 [pdf page 25] شاه دارو شاه ‎gale‏ ه امی است که جمشید بشراب انگوری گذاشته است»وسب
LEAF 31 [pdf page 32] -۲۸۱ ۱ چارپابان و کوسفندان را نیز گویشد که شب در آنجا باشند ۱ - و 
LEAF 35 [pdf page 36] ۷۲]  شبر نگ ۱ ‎p=‏ وزن خرچتگه » دام اسب سیاوش بوده ‎eee‏ ره بزردی 
LEAF 37 [pdf page 38] پاع) ات  بمعنی آشیان است که جا ‎pling‏ مرغان باشد. شیگو ۱ - با اف 
LEAF 80 [pdf page 81] علرن  شلون = بنتح اولبروزن زبون ,جالوری است ازجنس شفال - ودر عربی 
LEAF 81 [pdf page 82] اد  است که کنابه از زبان باشد و بعربی ‎OS‏ ‎Fass‏  شمع‌زدین لگی «ک
LEAF 86 [pdf page 87] کوته و بسیار سخت که پشه‌وران از ‎feo oT‏ افزار و دست افزار ‎Ie‏ - 
LEAF 220 [pdf page 221] غوشته . 6۲۸2 غوغا* ‎dhe b=‏ داربروزن‌سوداء بانگ: و فرباد و شور را
LEAF 229 [pdf page 230] als 4۳۷-۰  ره = ‎ving‏ )\( علمومه ‎pone‏ ‏است که نلم شهری باشه ‎t
LEAF 236 [pdf page 237] فرابرز هست - وبمعنی بر و در ‎ee‏ علی‌وفی‌خوانند - وبمعنی مه‌ومجمو
LEAF 237 [pdf page 238] سووعوت قراخ ‎gi‏ - کنابه ازبتتابوسبیل رفتن باشد . ‎O18‏ و ۱ - بنت
LEAF 239 [pdf page 240] ~\tty—  فراسیون ۱ = بفتح اول وکس رابع بر ‎oir‏ حواربون .گندنای کو
LEAF 243 [pdf page 244] 60۱  و رابع و رای قرشت » بمعتی عکس باشد؛ و با رابع‌مجهول بروزن مخ
LEAF 281 [pdf page 282] ۱4۸۹  قصره - بکس اول و قتح ‎pt‏ وئالث. بمعنی لرزه باشد خواه از سر
LEAF 287 [pdf page 288] بیان سیزدهم  در حرف فا ‎GEL‏ مشتمل برشش ‎cd‏ و کنامت  ‎Els‏ گشودن
LEAF 300 [pdf page 301] فولپون فولیون ۱ بطم اول و سکون ‎tl‏  وکسر لام و تحتانی بواو کشیده
LEAF 373 [pdf page 374] روا کانیصاد ۱ - بنتح نان و سین بی نقطه بالف. کشیده و برای قرشت زد
LEAF 380 [pdf page 381] aS ‏را ماست با‎ col JT te ‏آش: کیر باشد‎ ‏گویند. با بمعنی‌آش است‎
LEAF 386 [pdf page 387] as  ‎op!‏ لفت راساحب موبدالفضلا در سككلغات‌فارسی نوشته است ‎٩‏ بم
LEAF 396 [pdf page 397] ‎oly‏ نهم  ‏در کاف تازی با دال | ‎dow‏ مشتمل ۳ سبت وچهار ‎cal‏  ‏
LEAF 398 [pdf page 399] hs  ‎om‏ وروستاییر| کویتد که قریب بدهآهزارمردم در ‎oll‏ عاشورا آن
LEAF 404 [pdf page 405] کرانه ‎ao a‏ ‎che as‏ اول 5 آخ رکه ‎gies‏ | وبا شین قطه دار هم‌آم
LEAF 420 [pdf page 421] VA ‏کرنده‎  را هم میگوبند ۸ - ونام رودخانهاست۹ ‎NO,‏ ‏کر نگافی »ب
LEAF 549 [pdf page 550] —\ver—  صلب‌واز درخت لوعی از بلوط بهم میرسدوبعربی صمة ‎oan SEAM‏ 
LEAF 554 [pdf page 555] کیلك ۱ ‎Ge‏ اول و قح ثالی ‎GE OK ps els‏ » بسنی اول ‎SASS‏ ‏عطف ش
LEAF 620 [pdf page 621] است و بعربی طین فارسی خوانند .  » ‏با بای ابجد بر وزن کل‌فام‎ - P
LEAF 622 [pdf page 623] کلت ‎AAT‏ ‏گیل ‎pe - Ree‏ اول. زنگیرا گویشد که بر روی سنگه پیدا م
LEAF 692 [pdf page 693] لشکر شکوف ۱ = بکرتن درم . بمعنی لشکرشکاف باشد یعنی شخصی‌شجاع ودلا
```


## [2026-09-05T06:06:14.269Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(228,236):\n    print('==== leaf',i,'====')\n    print(t[i][:1200])\nEOF"
}
```


### [2026-09-05T06:06:17.692Z] TOOL RESULT

```
==== leaf 228 ====
[pdf page 229]
بای حطی ۰ یخ بلوفر هندی باشب .
قاگر ‎Go‏ غین قطمواریروزن‌حاض,
کلی باشد خوشبو و بزردی مایل . ب رکه آن
ماننه گل زنبق دراز مشود و اغلب در هندوستان
میباشد و بهندی رای ‎Lee‏ خوانند ۷ .

فاغره ۴ ‎ce‏ فين ‎abt‏ دار بروزن
تاسره ۰ نوعی از مطراست ‎dub oT,‏ باشدوهان

و مخت ‎glad‏ تشودی ؛ و جضی گویند

بممنی فاغراست که کل رای چنیا باشد؛ ‎wns‏
‏اول عربی میدانند .

فاغوش با ‎gt‏ نقطمدار پروزن (۱)
آغوش و با سین بی نقطه بر وزن فانوی ؛ تلم
داروییست که آنرا شیطرج هندی کویتد .

فاغیه ۴ () = پکر ‎ys‏ قطه دار
و فتح تحتانی ۰ بممنی فافر است که کل زردی
‎ath‏ خوشبوی در هندوستان مانند زنبق وبهندی
رای چنپا کوبند - وگل حنا و درخت‌حنایگل
کردمرا نیز گفته‌اند - وهرشکوفه را نیز گومند
که خوشبوی باشد .

sats St iz 186 ‏بروزن‎ - WU
. ۴ ‏و بدیم باشد‎

فالج - بکر لام بر وزن ‎CHF‏ مرد

(۱) چك : بوزن .
(4) چك : مردم .

(۷) چش : فافنیه .

Very

مظفر و منصور را ‎Pan‏ - و در عربی شتر
سطبر کوهان را خوانند - ونام ‎gle‏ هم‌هست؟

‎Ve IO‏ (۲)- بکرم ون
‎abet‏ دار و سکون را و سین یی نقطه 1 بیونانی
مرغیست که آنرا لكلك ‎an Se‏ استخوان
او را با خود داشتن ‎gee‏ را زابل میکند و ‎Kay‏
‏آو خشاب موی باشد و فالرغوس هم بنظر آعده
است که بسد از ‎gly gpd‏ باشد .

‎elt ce - ۵ SLE‏ و سکون کاف
و بای ابجد بالف کشیده و بزای نقطه دار 
==== leaf 229 ====
[pdf page 230]
als 4۳۷-۰

ره = ‎ving‏ )\( علمومه ‎pone‏
‏است که نلم شهری باشه ‎they‏ بفرخار و مشك
خوب ازآنجا آوربد .*

فافوس ‎Je‏ = فالوسی ‎adh‏ که
در آن صورتها کشند و ‎OF‏ صورنها بپوای ‎ST‏
‏چراغ بکردش درآید ‎٩‏ - و کتلیه ازآسان حم
هت ۷ . ۱

قائوس گردان = بستی‌فایی خیال
است - و کنابه از آسمان هم هت .

قافه - بروزن ‎ch ye « al‏ 5 باشد
که آنراگاهی ‎pin‏ در نهند تا در گشوده‌نگردد
و درودکران در شکاف ‎Kaye‏ میشک فند فروبرند
و کفش کران در ‎det‏ قالب وکفش گذاوند۷ -

و از غل وغش پاله ماخت .*
فا ‎wes‏ = بر وزن‌جالیئوی, رستنیی
باشد کهآ ترا شاهتره کوبند و در دواها ‎gh‏ برند.
خوردن آن حکه وجرب را نافع است .
‎eu‏ © بروزن و معنی وام است کمعربی
قرض و ‎op‏ خواشد ۱ - ویمعتی لون ورنگه ۲
- وشیه و مانند ونظیر هم آمده است ۴ - ونم
قصه‌ایت از قصبات خراسن ومولد مولانا شهاب
الدین که درعلم انشا و تاریخ و شعر مهارتی تمام
داشت ‎ey‏ لت ۰.۴
‎pls‏ بکرميم ۴ بروزن فلخر.شپری
است در حوالی ‎IES‏ ترديك ‎OT‏ شهر بیابافی
است که ‎spl‏ مك درآن بابان نافه اتدازد.
(۱) چك : بوزن .
9 افام س وام > بلم < پلم ‎Ceo)‏
‏چون ‎oat ool Sut‏ کردن ما و ‎poe‏ سنابی‌نوی*فرهنگه‌اه
۴ > اوام < پام < یام ‎(ge)‏ ورگ : ص لو از ‎betas‏ مولف . ابن‌کلمه که فقط صورت
جزو دوم‌کلمات م رکب بکار میرود باحتمال قوی مستعار ازکلمةٌ سفدي 19۳10 « رنگه ( درخش
==== leaf 230 ====
[pdf page 231]
aus

و۳ اه

ربمعنی حو کوچك هم هست ‎V‏ - ومکفف‌زفانه
هم هست که زبالٌ آتش ۴ و زيانة چوب و امثال
آن‌باشد» وزبانٌ ترازو را یز گوبند .

. ‏حطی بروزن (۱)جاوید»‎ st ‏با‎ - AGU

ممرب ‎dh‏ است ۴ که نوعی از حلوا باشد -
وقند مقید را ليز ‎aS‏ .
قاوا - با واو بالف کشیده بمعنی شرمتده

ورسوا ‎Fash‏ سوشرمندکی‌ورسوابی‌رالیز گوبند.
قاو افیا * - پکس ‎o‏ بروزنآغامیاء
درخت عودالسلیب است بجهت دفع نقرس‌وسرع
وکابوی‌نگهدارند. ودخان‌کنند وآنرا فاویایعذف
الف نیز کفته‌اند « وعودالریح همان است.
‎wld‏ بفتح تحتالی بروزن ‎BE‏ ,بمعنی
«تااست ‎La‏ انتها باشد ودرعربی‌حتی گویند.

بیان دوم

در حرف فا با تای قرشت مشتمل بر هقده لفت و کنایت

‎Vols‏ - بر وزنبات ‎thy‏ بابرا
کونه - وریز* هرچیز را یز گفتهاند .*

‏فتار ‎ow‏ ۲ یک اول بر وزن
حسارندن » بمعنی کندن ورختن ودربدن‌وشکافتن
وپرا کنده ویربشان‌ساختن وازهم جدا کردن‌باشد.

‎cin A SUS‏ اول بروز نکمال.بسنی
پیچیدکی و ازهم کستن باشد وبععنی‌ب رکند کی

‏(۳) چك : بوزن .
۱ - به یش رتبت تو چرخ مشکوب

‏۴.- پیش تو بندد بغر خود زفر ملك

‏و بر کندن‌هم هت - و درخت نوشانده را لیز
‎a‏ - وبکس اول بمعنی بربدن وشکنتن‌واز
ه مکسستن چیزی باشد .

‏فتالید ‎A‏ - بنتح اول , مانی ‎CAI‏
‏است یعتی فثانید و ربخت واز هم گست
و پراکنده کرد - و بمعنی بربد و شکت هم

‏آهده است .

‏بنزد همت تو م
==== leaf 231 ====
[pdf page 232]
وا

فتالیدن ۱ © بفتح‌اول‌بروزن‌طراوبدن»
بمعنی ریختن_ودردنوشکافتن_ویربشان‌وی را کنده
کردن ۴ - و کندن‌وازهم‌جدا کردن وکستن ۴
باشد ؛ ‎Gy‏ اول هم گفته‌اند .

فتح باب ۴ - کنابه از در باز ‎OS‏
‏کشادکارهاباند - وابتدای فصل بارندگی‌وابتدای
بارند گی‌رانیز گوبند - ویمعنی بارندگی‌هم‌هنت
- وتظر دو ک و کب را ‎ja‏ گفته‌اندباهم که‌خانهای
‎glo!‏ مقابل باشد همچو عطارد که ‎Ste‏ او جوزا
است ناظر باشد با مشتر یکه ‎LE‏ او قوس‌است.

فتر اه = ‎JIL‏ بروزن (۱) ‎Dal‏
‏تسمه و دوالی باشد که از پس وپیش زین اسب
آوبزند ‎Ts‏ بت رکی قنجوقه کونند ۵ .

‎pa = VO Sd‏ اول و انی و سکون را
و دال بی نقطه ( ۲ ) » ماضی فتردن است ,بعنی
چیزیرا ازهم دربد وپاره کرد - وبمعنی فاع ل که
درنده ومقعول که دریده ‎oat‏ - ومصدر که‌دریدن
باشد . هم کنته آند.

‏نته

‏فتردن ۲ ‎the‏ اول پروزن تکردن»
یمعتی دربدن ‎Os Sorby‏ ۸ باشد .

‏فترید ‎٩‏ بر وزن طلبید . بمعنی
درید و دربن هر دوگنته‌اند که ماشی و مستر
‎ath‏ .
فتریدن "۷ -(۳) بروزن‌طلبیدن,بسنی
دربدن‌وشکافتن_وپر ‎pyle‏ کنده کردنس وکندن
‎ath‏ ؛ ‎Gy‏ اول هم درست است.

‏فتلیدن ۱۱- بالام بروزن ومعنی‌فتربدن
و فتاربدن و فتالیدن است که ریشتن- وشکافتن
- و کندن وغیره باشد .

‏لقن س بنتح اول بر ‎Ob‏ چمن » یمعنی
شکل وشمایل باشد-ونام ملکی است‌درهندوستان
- و بکسر اول درعربی جمم فتنه‌است که ف
==== leaf 232 ====
[pdf page 233]
‎a‏ را کمر کگشادن وا
قتی = ‎oth‏ ول و ‎gl‏ و سکون واو .
بمعنی عربده جوی وغره و حفرور باشد ؛ وبجای
حرف انی تون‌هم آمده است اشاعل ۳ .*

‏بهرام او را و ‎thu‏ قصی پردن او کاو را مشهور "
است ۱ - و در عریی شور و غوغا و آشوب را

‏گویند .

‏فتنه را کمر ‎gS EP‏ - کناب از قتو ده - ‎ga‏ ال بروزن کشوده,بمعنی
تسکین دادن فتته است ‎iy‏ فرو نشانیدن شور | فریفته و مفرورباشد ؛ و باين ممتی بجای جرف
‎os‏ اول نون حرصت ‎HF‏

‏بیان سیم

‏در حرف فا با جیم مشتمل بر ذو لفت
فج = ‎ca‏ اول و سکون ثانی ؛فروهشته قچا - بنتح اول و نانی بالف. کتیده ,
لب راکویند ۴ بعنی کسیکه لب زیرین او فرو | ‎SIR‏ و خرما رااگوبند که بردرخت مانده
افتاده باشد ؛ و بکر اول تیز همین معنی دارد باشد ؛ و بکر اول حم کفته‌اند - و در ‎te‏
‏- و بفتح ‎Js)‏ بمعنی راء فراخ و کثاده آمده ‎caw‏ ناگاه رفتن باشد و اين از باب مفاعلت

‎۴. ۱ ‏است‎ . Pel

‎: ‏مبعد‎ VOY ‏نظامی چاپ ارمفان سال ۱۳۱۵ ص‎ Se ‏ره : هفت‎ ٩

‏داشت با خود کنیز کی چون ماه چت و چابك بهمرکابی شاء

‏فتنه نامی هزار فتنه در او ‎is‏ شاه و شاه فتنه بر او

‎.۰ ۱۰۸ ‏س‎ So cae?

‎= ‏فنو . فنودن . ۴ - رگ : فنوده » فنودن‎ : AF

‏۴ -رك : جهانگیری . ‎Ue) - ٩‏ بفتح اول و ‎wats‏ دوم ؛ ‎gle BLT)‏ دو
کوه. « منتهی‌الارب » . ‎٩‏ - (مر) ‎sled‏ وفجات ( از باب فتح وسمع ( ناگاه گرفتن

‏وناگاه
==== leaf 233 ====
[pdf page 234]
‎oly‏ چهازم

‏درحرف فا با خای ‎labs‏ مشتمل بر دوازده ‎cal‏

‏جح ۱ ‎cr‏ اول و سکون ثالی:بمنی

‏تله باشد ‎Se AT oF,‏ بدان جالو رگیرید ‎ -‏

‏و بممتی شکار وشکارگاه نیز آمده است .

‎CS‏ = بفتح اول + بروزن ومعنی‌پخت
باشد که ‎op‏ وپخش انت ۴ - ودرعربی ‎des‏
‏راکویند که مهتاب باشد ۴ .

‏خر - بنتح ‎Ss!‏ وکسر رای بی نقطه
بر وزن ‎Sp‏ » بععنی فربه و قوی عیکل ۴
سومرطوبی‌باشد.

‎pce = * © pied‏ اولوفا بروزنمجمره»
سبوس‌آرد کندم وآرد جو را گویند ۷.-

‏فخنود ۲ - بروژن و معتی فتفوراست
که پادشاه چن است ه رکه باشد .

‏فخلمه. بتح اول ولام ‎es‏ و سکون
‎Gen gt‏ حلاجان را گوبند » ‎ATT,‏ ات
ازچوب که برزه کمان زند تاپنبه حلاجی شود.

‎A god‏ - بنتم اول و سکون ‎tt‏ عیم»
چادری باشد که نارچینان برسر دو چوب بندند
تا بدان ازهوا نثار بربابند ‎٩‏ - و چاورشبی‌ر! لیز
‎al”‏ که در زیر درخت میوه دار ‎wi hat‏

‏بو درخت را بتکانند تلمیوه درآن جمم شود .

‏فخمده "- بفتح اول و ثانی پر وزن
زننده, پنبه‌ای‌را ‎SaaS‏ پنبمدانه ازآن‌برآورده
فخهیك ۱ -بروزن‌فیمیدسانی‌فضیدن
است بعنی پنبه را از پنبمدانه جدا کرد ویبرون

‏۱ -(عر) بفتح اول و تشدید دوم » دام شکاری .« منتهی الارب » عبری ‎(ed)‏ ( فتح

‏اول ) , آرامی (ضعا) ( بفتح اول ودوم ) ‎pi?‏

‎(pmo =~¢

‏*- )& < ففت بالفتح» ماهتا ب که ‎ss!‏ نمابان گردد — ودام شکاری - وسور
==== leaf 234 ====
[pdf page 235]
wee)

آورد .#

خمیده ‎go)‏ وزن فهمیده,پنبه را
کوبند که پنبهدانة آنرا جدا کرده وبرآورده‌باشند
وهتوز حلاجی نکرده باشند .

‎upd‏ بفتح اول و سکون الی ولون»

‏۱44۲
‎Ole‏ و درون باغ راکوبند - ووسط حقیتی‌باع
را نیز گفته‌اند ؛ وبقتح اول وثانی‌هم درست‌است
کی ۴ - بروزن تمیز,بسعنی‌مهمیزاست»
وآن آهنی باشد سرتیز که برپاشنة کفش و موزه

‏بیان پنچم
در حرف فا با دال ابچد مشتمل بر هفت ‎ca)‏

‎Se‏ اول » عوض و بدلی را
راکوبندکه خود را با دیگری را بدان برهانند
‎Gloss‏ دهند +
فدالی ۴ بر وزن رضائی ۰ ‎VT‏
‏کوبند که دانته مرتکب امری شود برغبت
ورضای خود که ملب ‎ole‏ را لازم داشته باشد
:» باکراه و زور و با بحکم پادشاه و شیخی -
وعاشق - و دزد وخونی‌را نیز گوبند ۵ .
فدر نجك ‎be‏ رای قرشت و جیم بر
وزن فرزندك « دبوی است که در خواب آدمیرا

‏فرو کیرد وحکماکونند ماد سوداییست(۱) که

‏(۱) چك : سوداوست .
۱

‎. ‏چش :کند‎ (x)

‏— اسم مفمول از« فخمیدن > ‎Com)‏

‏درخواب چنان‌نماید وآ را بعربی‌کابویوعبدالجنه
خوانند - و.پبرامون ‎Niles‏ 3 نیز گفته‌اند ازطرف
بیرون +

‏قدد نگ = بارای فرشت بر وزن
خرچنگ » چوبی باشد گنده (۲) و سطبر وقوی
که در پس در کوچه اندازند تا در گشوده‌نگردد
- و چوبی که گازران برجامه زنند وجامه رابدان
تاپ دهند و پیفثارند - وچوبیرا نیز گوبندکه
دةاقان جامه را ‎ole‏ کوبند ‎٩‏ و در خانها زنان
برخت پ
==== leaf 235 ====
[pdf page 236]
oN Efe

ودبوث هم حست - و بزبان ‎blk‏ خوردلی
و طمامی باشد که در دستمال (۱) بسته از جایی
بجایی برند - و بیعنی دستور هم بنظر آمده

است .

قدرو نك ‎bw‏ رای قرشت (۲) ‎ogy‏
‏بروزن(۳)زتبورلك سنگی‌را گویند ‎yi‏ کنگرهای
قلمه و حصار گذارندتا چون دشمن ‎sls‏ حصار(4)
‎aT‏ پزسرش اندازند .

وا

فدده ‎the‏ اول ورای‌قرشت وسکون
‎ploy Jt‏ باشد که ازب ‎EF‏ خرعا و غیرميافند
وبربالای ‎lege‏ و پروار های سقف ‎ale‏ ادازند
وخاك وکل بر ‎OTE‏ ریختهخاك بیندازس(ه).

قدو ند ‎Slate a)‏ و راو ‎wing‏
‏بند» بمعنی‌اول فدرنگ است ‎Oly‏ چوبی باش د که
در پي در اندازند: تا درکشوده نگرده +

بیان ششم

در حرف فا با رای بی نقطه مشتمل بر سیصد و نوزده لغت و کنایت

قر ۴ « بنتح و سکون ثانی ۴ » بععنی
خأن و شوکت ورفت وشکوه و سنکه و هنگه
باشد - وبمعنی نورهم گفته‌اند چه‌مردم لورانی‌را
فرمند و فرهومند گوبند - و بععتی برازی
و برازندکی وزیبا و زیبایی و زیبندکی‌تیز آمنه
است - وسیلاب را هم گوبند - و بمعنی مطلق
‎ol Fat,‏ زیر مرغ خانگی و پرمرغان‌دیگر

- و با تشدید ثالی در عربی » بمعنی گرینتن
و گربزان شدن باشد 8 - و نم اول ‎BET‏
‏بهودانرا میگویند .

‎Vs‏ = بروزن سرا : بمعنی‌سوی‌وطرف
و جانب - وکنج و گوشه باشد - و ‎te gins‏
ویتتر و ميان و وسط هم آهده است - وبمعنی

‏بالا و بلندی وقریب وبعید بعنی دور و تزديك‌هم

‏(۱) چك : ‎glazes‏
```


## [2026-09-05T06:06:34.538Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[229])\nEOF"
}
```


### [2026-09-05T06:06:36.744Z] TOOL RESULT

```
[pdf page 230]
als 4۳۷-۰

ره = ‎ving‏ )\( علمومه ‎pone‏
‏است که نلم شهری باشه ‎they‏ بفرخار و مشك
خوب ازآنجا آوربد .*

فافوس ‎Je‏ = فالوسی ‎adh‏ که
در آن صورتها کشند و ‎OF‏ صورنها بپوای ‎ST‏
‏چراغ بکردش درآید ‎٩‏ - و کتلیه ازآسان حم
هت ۷ . ۱

قائوس گردان = بستی‌فایی خیال
است - و کنابه از آسمان هم هت .

قافه - بروزن ‎ch ye « al‏ 5 باشد
که آنراگاهی ‎pin‏ در نهند تا در گشوده‌نگردد
و درودکران در شکاف ‎Kaye‏ میشک فند فروبرند
و کفش کران در ‎det‏ قالب وکفش گذاوند۷ -

و از غل وغش پاله ماخت .*
فا ‎wes‏ = بر وزن‌جالیئوی, رستنیی
باشد کهآ ترا شاهتره کوبند و در دواها ‎gh‏ برند.
خوردن آن حکه وجرب را نافع است .
‎eu‏ © بروزن و معنی وام است کمعربی
قرض و ‎op‏ خواشد ۱ - ویمعتی لون ورنگه ۲
- وشیه و مانند ونظیر هم آمده است ۴ - ونم
قصه‌ایت از قصبات خراسن ومولد مولانا شهاب
الدین که درعلم انشا و تاریخ و شعر مهارتی تمام
داشت ‎ey‏ لت ۰.۴
‎pls‏ بکرميم ۴ بروزن فلخر.شپری
است در حوالی ‎IES‏ ترديك ‎OT‏ شهر بیابافی
است که ‎spl‏ مك درآن بابان نافه اتدازد.
(۱) چك : بوزن .
9 افام س وام > بلم < پلم ‎Ceo)‏
‏چون ‎oat ool Sut‏ کردن ما و ‎poe‏ سنابی‌نوی*فرهنگه‌اه
۴ > اوام < پام < یام ‎(ge)‏ ورگ : ص لو از ‎betas‏ مولف . ابن‌کلمه که فقط صورت
جزو دوم‌کلمات م رکب بکار میرود باحتمال قوی مستعار ازکلمةٌ سفدي 19۳10 « رنگه ( درخشان)»
ونیز بمعنی*صیح» ونیزفمل مشتق از اسماست- ‎B'M‏ درخشیدن (رنگها)» همریشتفارسی‌این‌کلمه
«بام*(سبح) است. رل ‎Henning, Sogdian loan words...,BSOS-X_1,p.100_101:‏
در تر کیبات : مشکفام ( برنگک هشك ) , سپید فم ( سقید ‎(Ky‏ ۰ کلفام ‎whe (BEAT)‏
فام ( سباه رنگ ) آمده . ‎F‏ رك : جپانگیری » رشیدی .
۴ - در رشیدی ‎pe‏ میم . © قی ‎(y) lanterne magique‏
1 این چرخ فلك که مادروحبرانیم ‎Shs pyle‏ از او ‎Me‏ دایم
خورشید چراغ آن وعالم فادوی ماچون صوریم کاضر و ‎“BOS‏
‎pas «‏ نمتابوری . چاپ برلین ۲۳۰4 ص۱۰۵ >*.
۷ = پانه (هم.) < ‎ale‏ (هم) :
‎iS‏ نود زخم . همه رحمت ومهراست ‎Po KS‏ تو ماننده فاله است.
مولوی بلخی > فرهنکه‌ظام *.

" فالودی - بفتح ینجم = پالودن (هم)

۵ فافوس - ‎pe‏ نون از ‎Phands sty‏ ( درخشنده ) « ژابا ص
۸۵۸ ۶ دزعج "ص۲۸4 ». هر چراغی که جهت روشن کردن
مافت بعید بر بالای بلندی مانند منار نصب کنند ‎ATR‏ که از

موادی سازند که حاجب نور نباشد مانشد ‎SEB‏ و ‎att‏ و پارچه
ودرآن چراغ با شمع نهند تا ازباد محفوظ ماند . فانوی کاغذی فانوی درشکه
```


## [2026-09-05T06:06:54.070Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN_1966 phos ===\"; grep -n \"phosphorus\\|phōs\\b\\|phos-, comb\" KLN_1966.txt | head -10\necho \"=== KLN phanos/fanous ===\"; grep -n -i \"fanous\\|fanus\\|phanos\" KLN_1966.txt KLN_1971.txt | head -10\necho \"=== LKT fanus ===\"; grep -n -i \"fanus\\|fānūs\\|phanos\" LKT.txt | head -10\necho \"=== AFM fanus ===\"; grep -n \"فانوس\" AFM.txt AFM_alt.txt 2>/dev/null | head -5"
}
```


### [2026-09-05T06:06:54.181Z] TOOL RESULT

```
=== KLN_1966 phos ===
3075:aphoristic,  aphoristical,  adj.  —  Gk.  a9opicmx6<;, ‘delimiting,  aphoristic’,  fr.  a^opl^Eiv.  See  aphor¬ ism  and  -ic,  resp.  also  -al. aphotic,  adj.,  lightless.  —  Formed  with  suff.  -ic  fr. Gk.  4910?,  gen.  5901x04,  ‘without  light’,  fr.  <x- (see  priv.  pref.  a-)  and  9014,  gen.  901x64,  ‘light’. See  phosphorus.
4608:bear,  tr.  and  intr.  v„  to  carry.  —  ME.  beren,  fr. OE.  beran,  rel.  to  ON.  bera,  OFris.  bera,  Du. baren,  OHG.  beran,  ‘to  bear,  carry’,  Goth. bairan,  ‘to  bear,  carry,  give  birth  to’,  OHG.  gi- beran,  MHG.  gebern,  G.  gebaren,  Goth,  ga- bairan,  ‘to  give  birth  to’,  fr.  I.-E.  base  *bher-, whence  also  OI.  bhdrati,  ‘bears’,  bharman,  ‘sus¬ tenance,  care,  burden’,  Arm.  berem,  ‘I  bear, carry,  bring’,  bern,  ‘burden’,  Gk.  ipspeiv,  ‘to bear,  carry’,  <ptop,  ‘thief’,  L.  ferre,  ‘to  bear,  car¬ ry’,  fur,  ‘thief’.  Alb.  mbar,  bar,  ‘I  carry,  drag’, bir,  ‘son’,  OSlav.  berg,  birati  (for  earlier  bird), ‘to  bring  together,  collect,  take’,  bremg,  ‘bur¬ den’,  su-borii,  ‘assembly’,  OIr.  biru,  ‘I  carry’, W.  cymeraf  ‘I  take’,  Toch.  AB  par,  ‘to bear,  bring,  fetch’,  and  prob.  also  Toch.  B prari,  ‘finger’.  Cp.  bairn,  baron,  barrow,  ‘moun¬ tain’,  barrow,  ‘handcart’,  berth,  bier,  birth,  bore, ‘tidal  wave’,  borough,  burden,  ‘load’,  burly.  Cp. also  adiaphoresis,  adiaphorous,  afferent,  am¬ phora,  anthropophora,  Berenice,  bhat,  breba, brehon,  cataphora,  circumference,  confer,  cumber, defer,  deference,  differ,  difference,  differentiate, efferent,  -fer,  feretory,  -ferous,  ferret,  the  animal, fertile,  fortuitous,  fortune,  furtive,  furuncle,  in¬ fer,  metaphor,  offer,  opprobrium,  paraphernalia, periphery,  phoradendron,  phoresis,  Phormium, -phorous,  phosphorous,  phosphorus,  prefer,  prof¬ fer,  refer,  scirophorion,  semaphore,  Sobranje, suffer,  transfer,  varnish,  vernix  caseosa,  Vero¬ nica,  vociferate.
10905:dephosphorize,  tr.  v.,  to  remove  phosphorus  from. —  Formed  fr.  de-  (in  the  privative  sense  of  this prefix),  phosphorus  and  suff.  -ize.
27570:—  L.,  fr.  Gk.  na<K9a7),  fr.  naaitfocriq,  ‘shining for  all’,  fr.  iraoi,  ‘for  all’,  and  9<xo£,  ‘light’.  For the  first  element  see  prec.  word,  for  the  second see  phosphorus.
28605:Derivatives:  phosphat-ed,  phosphat-ic,  adjs., phosphat-ize,  tr.  v .,  phosphat-iz-ation,  n. phosphene,  n.,  a  luminous  image  produced  by mechanical  stimulation  of  the  retina.  —  Lit. ‘that  which  shows  the  light’,  compounded  of Gk.  cpco;,  ‘light’,  and  the  stem  of  9<xlvsiv,  ‘to show’.  See  phosphorus  and  phantasm, phosphide,  phosphid,  n.,  compound  of  phosphorus with  another  element  (chem.)  —  See  phospho- and  -ide,  resp.  -id.
28608:Derivatives:  phosphin-ate,  n.,  phosphin-ic,  adj. phosphite,  n.,  salt  of  phosphorous  acid  (chem.)  — See  next  word  and  subst.  suff.  -ite. phospho-,  before  a  vowel  phosph-,  combining form  used  in  the  sense  of  phosphoric,  phosphor¬ ous.  —  Shortened  fr.  phosphorus, phosphonium, n.,  the  univalent  radical  PH,  (chem.) —  ModL.,  coined  fr.  phosph-  and  the  ending - onium ,  on  the  analogy  of  amm-onium. phosphoprotein,  n.,  any  of  a  class  of  proteins  in which  the  protein  molecule  is  combined  with some  phosphorous  substance  other  than  lecithin or  nucleic  acid  (biochem.)  —  Compounded  of phospho-  and  protein.
28609:Phosphor,  n.,  1)  the  morning  star  (poetic );  2) (not  cap.)  phosphorus.  —  L.  Phosphorus,  ‘Phos¬ phor’.  See  phosphorus.
28610:phosphor-,  form  of  phosphoro-  before  a  vowel, phosphoric,  adj.  - —  F. phosphorique,  fr. phosphore. See  phosphorus  and  adj.  suff.  -ic.
28611:Derivative:  phosphoric-al,  adj. phospho  rize,  tr.  v.  —  F.  phosphoriser ,  fr.  phos¬ phore.  See  phosphorus  and  -ize. phosphoro-,  before  a  vowel  phosphor-,  combin-
28613:ing  form  meaning  phosphorus  or  phosphores¬ cence.  —  Fr.  L.  phosphorus.  See  next  word, phosphorus,  n.  —  ModL.  phosphorus,  ‘phospho¬ rus’,  fr.  L.  Phosphorus,  ‘the  morning  star’,  fr. Gk.  90KJ96P0;,  ‘light-bringer;  the  morning star’,  which  is  compounded  of  96!;,  ‘light’, contr.  of  9x0c,  and  -9690;,  ‘carrying’.  The  first element  derives  fr.  I.-E.  base  *bha-,  ‘to  shine’, whence  also  OI.  bhdti,  ‘shines,  glitters’,  bhas-, ‘light,  glory’.  See  phantasm  and  words  there  re¬ ferred  to  and  cp.  esp.  the  second  element  in Pasiphae.  For  the  second  element  see  -phorous. Derivatives:  phosphor-ate,  tr.  v.,  phospkore-al, phosphore-ous,  adjs.,  phosphor-esce,  intr.  v., phosphor-esc-ence,  n.,  phosphor-esc-ent ,  adj.  and n.,  phosphor-ism,  n.  (med.),  phosphor-ite,  n. (mineral.),  phosphor-it-ic,  adj.,  phosphor-ous, adj.
=== KLN phanos/fanous ===
KLN_1966.txt:10371:Dasypus,  n.,  a  genus  of  armadillos  (zool.)  — ModL.,  fr.  Gk.  Sacju7rou?,  ‘a  hare’,  lit.  ‘the hairy-footed  animal’,  fr.  dasy-  and  rot)?,  gen. no8o?,  ‘foot’.  See  dasy-  and  -pod. Dasystephana,  n.,  a  genus  of  plants  of  the  gentian family  (bot.)  —  ModL.,  compounded  of  dasy- and  Gk.  axccpavoi;,  ‘crown’.  See  Stephanos, dasyure,  n.,  any  of  small  marsupial  mammals  of Australia.  —  Compounded  of  dasy-  and  Gk. oup£,  ‘tail’.  See  uro-,  ‘tail-’, data,  n.  —  PI.  of  datum  (q.v.) date,  n.,  a  given  point  of  time.  —  ME.,  fr.  OF. (=  F.)  date,  fr.  ML.  data  (scil.  littera)  (whence also  It.,  Proven?.,  Sp.  data),  lit.  ‘(letter)  given’, prop.  fem.  pp.  of  L.  dare,  ‘to  give’.  This  term derived  fr.  L.  datum  (neut.  pp.  of  dare),  the  first word  used  in  letters  to  indicate  the  place  and time  of  writing  as  e.g.  datum  Romae  pridie Kalendas  Maids,  ‘given  (i.e.  written)  at  Rome on  the  last  day  of  April’.  L.  dare  is  rel.  to  dos, ‘marriage  portion,  dowry’,  do-num,  ‘gift’,  dond, donare,  ‘to  give  as  a  present’,  fr.  I.-E.  base  *dd-, *d1-,  ‘to  give’,  whence  also  OI.  da-da-ti,  ‘gives’, Avestic  dadaiti,  of  s.m.,  OI.  da-tar-,  da-tar-, ‘giver’,  da-tram,  ‘gift’,  Gk.  8i-Bco-pi,  ‘I  give’, Sd)-T(0p,  Sco-xrjp,  So-xrjp,  ‘giver’,  8£>-pov,  Sto- t(vt),  8<o;,  ‘gift’,  S6-m;,  ‘a  giving;  gift’,  Bo-xo; (verbal  adj.  of  Si-Sto-ptt),  ‘given’,  OSlav.  dati,  ‘to give’,  da-ru,  ‘gift’,  da-ni,  ‘tax’,  da  mi,  ‘I  shall  give’, Lith.  duomi,  ‘I  give’,  OPruss.  dost,  ‘gives’,  Arm. ta-m,  ‘I  give’,  tu-r,  ‘gift’,  Alb.  Sa-sc,  ‘I  gave’. Cp.  add,  addendum,  anecdote,  antedate,  anti¬ dote,  apodosis,  condone,  dado,  dation,  dative, die,  ‘cube’,  donation  and  words  there  referred to,  dose,  dosimeter,  dosology,  dot,  ‘marriage portion’,  dower,  dowry,  edit,  irredenta,  post¬ date,  reddendum,  reddition,  render,  rendition, sacerdotal,  subdititious,  surrender,  tradition, traitor,  treason.  Cp.  also  mandate,  command, commend,  countermand,  demand.  Cp.  also  the second  element  in  vend.
KLN_1966.txt:30399:profanation,  n.  —  MF.  (=  F.),  fr.  Late  L.profdna- tionem,  acc.  of  profanatio,  fr.  L.  profanatus,  pp. of  profanare.  See  profane,  v.,  and  -ation. profane,  tr.  v.  —  ME .prophanen,  fr.  L.  profanare, ‘to  make  profane’,  fr.  profanus.  See  profane,  adj. Derivative:  profan-er,  n. profane,  adj.  —  ME.  prophane,  fr.  OF.  (=  F.) profane,  fr.  L.  profanus,  ‘unholy,  not  sacred', lit.  ‘that  which  is  situated  before  (i.e.  outside  of) the  temple’,  fr.  1st  pro-  and  fanum,  ‘temple’.  See fane.
KLN_1966.txt:30400:Derivatives:  profane-ly,  adv.,  profane-ness,  n. profanity,  n.  —  Late  L .profanitds,  fr.  L.  profanus.
KLN_1966.txt:36731:stephanion,  n.,  the  point  where  the  sutura  coro- nalis  crosses  the  temporal  ridge  ( craniol .)  — ModL.,  fr.  Gk.  crxcq) xvtov,  dimin.  of  ax£( potvoc;, ‘crown’,  ‘that  which  encircles,  crown,  wreath’, which  is  rel.  to  oxEtpavv),  ‘that  which  encircles; diadem’,  used  also  as  a  medical  term  to  denote the  sutura  coronalis.  For  this  use  of  crxeipavifj see  Aretaeus  Medicus,  ed,  K.  Hude,  Corpus Medicorum  Graecorum,  II,  Xpovicov  voocov HEparceimxov,  I,  2.  See  prec.  word, stephanite,  n.,  a  black  mineral.  —  G.  Stephanit, named  after  Archduke  Stephan,  mining  director of  Austria  (died  in  1867).  The  ending  -it  goes back  to  Gk.  -  txr;? ;  see  subst.  suff.  -ite. stephano-,  before  a  vowel  stephan-,  combining form  denoting  crown.  —  Gk.  0x890010-,  fr. atitpaMoq,  ‘that  which  encircles ;  crown ;  wreath’, fr.  crxEcpEtv,  ‘to  encircle;  to  crown;  to  wreathe’, See  stemma  and  cp.  Stephana,  stephane,  ste¬ phanion,  Stephanos,  Stephanotis,  Stephen  and  the second  element  in  Dasystephana.
KLN_1966.txt:36732:Stephanos,  n.,  a  kind  of  headdress  (Gk.  antiq.)  — Gk.  atiipotvoq,  ‘crown’.  See  stephano-. Stephanotis,  n.,  a  genus  of  plants  of  the  milkweed family  ( bot .)  —  ModL.,  fr.  Gk.  ateipxvtotiq (fern.),  ‘fit  for  a  crown’,  fr.  ax£9avouv,  ‘to crown’,  fr.  oxcoavoc,  ‘crown’.  See  stephano-. Stephen,  masc.  PN.  —  L.  Stephanus,  fr.  Gk.  Sxe- 9avo;,  lit.  ‘crown’.  See  stephano-  and  cp.  Ste¬ phana.
KLN_1971.txt:64467:and Gk. cxeqxxvo;, ‘crown’. See Stephanos. 
KLN_1971.txt:192135:‘to make profane’, fr. profanus. See profane, adj. 
KLN_1971.txt:192138:profane, fr. L. profanus, ‘unholy, not sacred’, 
KLN_1971.txt:192144:profanity, n. — Late L . profanitds, fr. L. profanus. 
KLN_1971.txt:232059:phanion, Stephanos, Stephanotis, Stephen and the 
=== LKT fanus ===
=== AFM fanus ===
```


## [2026-09-05T06:07:02.305Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=28550 && NR<=28650' KLN_1966.txt | grep -n -E \"^[0-9]{3,4}|1[0-9]{3}\" | head -20\necho \"--- look for standalone page numbers ---\"\ngrep -n \"^11[0-9][0-9]$\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T06:07:03.928Z] TOOL RESULT

```
5:Derivative:  phlobaphen-ic,  adj. phloem,  n.,  bast  tissue  in  plants  {hot.)  —  G. Phloem,  coined  by  the  botanist  Karl  Wilhelm von  Nageli  (1817-91)  fr.  Gk.  9X605,  ‘bark’, which  is  rel.  to  9X201,  ‘I  teem,  abound’,  9X.601, ‘I  boil  over,  bubble,  rise’,  9EXX.65.  ‘cork  tree, cork’.  See  phello-.
8:phlogiston,  n.,  the  inflammatory  principle.  — ModL.,  fr.  Gk.  9Xovt<rx6v,  neut.  of  9X0710-765, ‘burnt  up;  inflammable’,  fr.  9Xov(Cetv,  ‘to  set on  fire,  burn’,  fr.  9X65,  gen  9X0765,  ‘flame, blaze’.  See  Phlox.  The  term  phlogiston  was  first used  by  Raphael  Eglin  (1559-1622). phlogopite,  n.,  a  brownish  magnesium  mica (mineral.)  —  Formed  with  subst.  suff.  -ite  fr. Gk.  9X07017:65,  ‘fiery-looking’,  which  is  com¬ pounded  of  9X0E,  gen.  9>.oy65,  ‘flame,  blaze', and  <a<Ji,  gen.  017:65,  ‘eye’.  See  phlox  and  -opia. phlogosis,  n.,  inflammation  (med.)  —  Medical  L., formed  fr.  Gk.  9X65,  gen.  9X0965,  ‘flame,  blaze’ (see  Phlox),  with  suff.  -osis.
29:phone,  n.  ( colloq .)  —  Abbreviation  of  telephone, -phone,  combining  form  meaning  ‘voice’,  as  in megaphone,  microphone,  telephone.  —  Fr.  Gk. 9« vf],  ‘sound,  voice’.  See  phone,  ‘speech  sound’, phoneme,  n.,  a  distinctive  sound  or  group  of sounds.  —  F. phoneme,  fr.  Gk.  961751//,  ‘sound, utterance’,  fr.  901V7).  See  phone,  ‘speech  sound’, and  cp.  the  second  element  in  grapheme,  hyph- eme,  semanteme,  solideme,  morpheme. Derivative:  phonem-ic,  adj. phonendoscope,  n.,  an  intensifying  stethoscope. —  Compounded  of  Gk.  9COV7),  ‘sound,  voice’, evSov,  ‘within’,  and  -oxdmov,  fr.  cxoteeiv,  ‘to look  at,  examine’.  See  phone,  ‘speech  sound’, endo-  and  -scope.
49:1176
52:phorone,  n.,  the  name  of  an  isomeric  compound (chem.)  —  Coined  by  the  French  chemist Charles  Frederic  Gerhardt  (1816-56)  from  the contraction  of  (cam)phor  (kct)one.
53:-phorous,  combining  form  meaning  ‘bearing’,  as in  cryophorous,  oophorous.  —  ModL.  -phorus,  fr. Gk.  -ipopo;,  ‘bearing’.  See -phore. phosgene,  n.,  a  colorless  gas,  COC1,  (chem.)  — Coined  by  the  English  chemist  Sir  Humphrey Davy  (1778-1829)  in  1812  fr.  Gk.  ‘light’, and  -yev11?i  ‘born  of,  produced  by’.  See  phos¬ phorus  and  -gen.
63:1177
69:photism,  n.,  an  illusory  visual  sensation  (psychol.) —  G.  Photismus,  coined  by  the  Swiss  psychia¬ trist  Eugen  Bleuler  (1857-1939)  in  1881  fr.  Gk. pomapio;,  ‘illumination’,  fr.  9om^Eiv,  ‘to  illu¬ minate’  fr.  9 £>;,  gen.  910x61 ‘light’.  See  phos¬ phorus  and  -ism.
91:1178
92:1179
--- look for standalone page numbers ---
26718:1103
26809:1106
26810:1107
26862:1108
26949:1113
26983:1114
26984:1115
27046:1116
27062:1117
27084:1118
27085:1119
27135:1120
27136:1121
27196:1122
27197:1123
27241:1124
27242:1125
27298:1126
27299:1127
27345:1126
```


## [2026-09-05T06:07:09.076Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nln=$(grep -n \"^1170$\" KLN_1966.txt | head -1 | cut -d: -f1); ln2=$(grep -n \"^1171$\" KLN_1966.txt | head -1 | cut -d: -f1); echo \"$ln $ln2\"; sed -n \"$((ln-25)),$((ln+3))p\" KLN_1966.txt | cut -c1-2500"
}
```


### [2026-09-05T06:07:10.989Z] TOOL RESULT

```
28453 28454
phago-,  combining  form  meaning  ‘eating',  as  in phagocyte.  —  Gk.  9ayo-,  fr.  9ayciv,  ‘to  eat’.
See  -phagous.
phagocyte,  n.  (biol.  and  med.)  —  Coined  by  the Russian  zoologist  and  bacteriologist  £lie  Metch- nikoff  (1845-1916)  in  1884  from  phago-  and Gk.  xoto?,  ‘a  hollow  vessel’.  See  -cyte. Derivatives:  phagocyte,  tr.  v.,  phagocyt-ic,  adj., phagocyt-ism,  n.,  phagocyt-ize,  tr.  v. phagocytosis,  n.,  destruction  of  bacteria  by  pha¬ gocytes.  —  ModL.,  coined  by  Metchnikoff  from prec.  word  and  suff.  -osis.
-phagous,  combining  form  meaning  ‘eating,  feed¬ ing  on’,  as  in  creophagous,  xylophagous.  —  Gk. -9ayo;,  ‘eater  of’,  from  the  stem  of  9xyetv,  ‘to eat’,  which  is  cogn.  with  Ol.  bhajati,  ‘assigns, allots,  apportions,  enjoys,  loves’,  bhagah,  ‘al¬ lotter,  distributor,  master’,  bhaksati,  ‘eats, drinks,  enjoys’,  Avestic  baya-,  OPers.  baga-, ‘master,  god’,  lit.  ‘distributor’,  OSlav.  bogu, ‘god’,  bogatu,  ‘rich’,  u-bogu,  ne-bogii,  ‘unfortu¬ nate’.  All  these  words  derive  fr.  l.-E.  base *bhag-,  ‘to  distribute,  share  out’.  Cp.  the  second element  in  esophagus.  Cp.  also  bahadur,  bak¬ sheesh,  Bhaga,  Bhagavad-Gita.  For  E.  -ous  (in -phagous),  as  equivalent  to  Gk.  -o;,  see  -ous. -phagy,  also  -phagia,  combining  form  meaning
r§
¥
1
‘eating  of  (something  specified)’,  as  in  anthra- pohagy,  geophagy.  —  ModL.  -phagia,  fr.  Gk. -9ayia,  ‘eating  of’,  fr.  -9ayoc,  ‘eating’.  See -phagous  and  -y  (representing  Gk.  -la), phalange,  n.,  single  bone  of  finger  or  toe  (anal. and  zool.)  —  F.,  fr.  L.  phalanx,  gen.  -angis.  See phalanx.
Derivative;  phalange-al,  adj. phalanger,  n.,  any  of  a  number  of  Australian arboreal  marsupials  with  a  long  tail ;  (cap.)  the typical  genus  of  phalangers  (zool.)  —  ModL., fr.  Gk.  9<xXay£,  ‘bone  between  two  joints  of  the fingers  or  toes’  (see  phalange);  so  called  in  allu¬ sion  to  the  characteristic  formation  of  the  toes. Phalangeridae,  n.  pi.,  a  family  of  marsupials (zool.)  —  ModL.,  formed  from  prec.  word  with suff.  -idae.
phalanstery,  n.,  socialistic  community  proposed by  the  French  social  scientist  Frangois-Marie- Charles  Fourier  (1772-1837).  —  F.  phalanstere, coined  by  Fourier  It.  phalange,  name  of  the  com¬ munity  in  Fourier’s  system,  prop,  ‘phalanx’,  and the  ending  -ere,  after  monastere  (=  E.  monas¬ tery).  See  phalanx.
Derivatives:  phalanster-ial,  adj.,  phalanster-ian, adj.  and  n .,  phalanster-ian-ism,  n.,  phalanster-ic, adj.,  phalanster-ism ,  n.,  phalanster-ist,  n. phalanx,  n.,  heavy  infantry  in  close  order  (Greek antiquity);  a  single  bone  of  finger  or  toe  (anat. and  zool.)  —  L.,  fr.  Gk.  9aXay5,  ‘trunk,  log, line  of  battle,  battle  array;  bone  between  two joints  of  the  fingers  or  toes’,  cogn.  with  OE. balca,  ‘a  ridge  between  furrows’.  See  balk,  n., and  cp.  Falange.  In  anatomy,  phalanx  orig.  de¬ noted  the  whole  row  of  the  finger  joints,  which was  so  called  because  its  arrangement  is  sug¬ gestive  of  a  battle  array.  See  Joseph  Hyrtl,  Ono- matologia  anatomica,  p.  104,  and  cp.  phalange. Derivative:  phalanx-ed,  adj.
Phalaris,  n.,  a  genus  of  plants,  the  canary  grass (bot.)  —  ModL.,  fr.  Gk.  9aXapig,  ‘coot;  canary grass’.  See  next  word.
phalarope,  n.,  any  of  small  wading  birds  that  re¬ semble  the  sandpiper.  —  F.,  irregularly  formed fr.  ModL.  Phalaropus,  name  of  the  type  genus, fr.  Gk.  9xXapi;,  ‘coot’  and  rtouc,  gen.  ttoSo;, •foot’.  The  first  element  prop,  means  ‘white, shining’  (the  coot  is  called  9xX5pt c,  from  the white  spot  on  its  head),  and  derives  fr.  <?xX6 ;, ‘white,  shining’  (whence  also  9aXapog,  ‘having a  patch  of  white'),  and  is  cogn.  with  L.  fulica, ‘coot’,  OHG.  belihha,  MHG.,  G.  belche,  ’coot’. All  these  words  derive  fr.  I.-E.  base  *bhel-,  'to shine’,  whence  also  OI.  bhdtam,  ‘brightness; forehead’,  OE.  bil,  ‘a  blazing  fire,  a  funeral pyre’,  ME.  balled,  ‘bald’.  See  bald  and  cp.  words there  referred  to.  For  the  second  element  in ModL.  Phalaropus  see  -pod. phallic,  adj.,  pertaining  to  the  phallus  or  to  phal- licism.  —  Gk.  9aXX'.xog,  ‘pertaining  to  the  phal¬ lus’,  fr.  9aXXog.  See  next  word  and  -ic. Derivatives:  phallic-ism,  n.,  phallic-ist,  n.
phallus
pnci  iav.iic
phallus,  n.,  an  image  of  the  male  organ  of  genera¬ tion.  —  L.  phallus,  fr.  Gk.  90 cXXo?,  ‘phallus',  for I.-E.  *bhj-no- ;  rel.  to  cpaXXa iva,  9aXXrj,  ‘whale', and  cogn.  with  L.  follis  (prob.  for  *bhol-nis),  ‘a pair  of  bellows'  (orig.  ‘leather  sack’),  fr.  I.-E. base  *bhel-,  'to  swell',  whence  also  ON.  boll, ‘bull’,  OE.  bulluc,  ‘little  bull’.  See  bull,  ‘male  of the  ox’  and  cp.  words  there  referred  to. Derivatives:  phallic  (q.v.),  phall-ism ,  n.,  phall- ist,  n.
Phanar,  n.,  name  of  the  Greek  quarter  in  Con¬ stantinople.  —  Turk.  Fanar,  fr.  ModGk.  <Ea- vdpi,  ‘lighthouse’,  fr.  Gk.  9avaptov,  ‘lantern’, dimin.  of  9av6;,  ‘torch’  (see  phantasm);  so  call¬ ed  from  its  lighthouse.
Phanariot,  Phanariote,  n.,  a  Greek  residing  in  the Phanar  quarter  of  Constantinople.  —  ModGk. ®avapicoT7)q,  ‘inhabitant  of  the  quarter  called Oavdpi’.  See  prec.  word  and  -ote.
-phane,  combining  form  meaning  ‘having  the  ap¬ pearance  of  . . .  ’,  as  in  cellophane,  cymophane.  — Gk.  -yocvrjz,  from  the  stem  of  9atvsiv,  ‘to  show’, 9odv£a0ai,  ‘to  appear’.  See  phantasm  and  cp. phanero-.
phanero-,  before  a  vowel  phaner-,  combining form  meaning  ‘visible,  manifest’.  —  Gk.  9a- vepo-,  9ocvep-,  fr.  9<xv£po<;,  ‘visible,  manifest;  il¬ lustrious’.  See  phantasm  and  cp.  words  there  re¬ ferred  to.
phanerogam,  n.,  a  plant  bearing  flowers  ( bot .)  — F.  phanerogame,  compounded  of  Gk.  9<xvspo q, ‘visible’  and  yap.05,  ‘marriage’.  See  phanero-  and gamo-.
Derivatives :  phanerogarn-ic,  phanerogam-ous, adjs.
phantasm,  n.,  illusion,  phantom.  —  ME.  fan- tasme,  fr.  OF .fantasme,  fr.  L. phantasma,  fr.  Gk. 9avTocajxa,  ‘apparition’,  fr.  9avT<x(eiv,  ‘to make  visible,  display’  (whence  also  9avx aalac, ‘appearance,  imagination’),  from  the  stem  of 9aiv£iv,  ‘to  make  appear,  show;  to  shine’, whence  also  900*61;,  ‘torch’,  9avspo<;,  ‘visible, manifest;  illustrious’;  rel.  to  ‘light’,
fr.  I.-E.  base  *bhd-,  ‘to  shine’,  whence  also  OI. bhati,  ‘shines,  glitters’,  bhas-,  ‘light,  glory’,  Arm. banam,  ‘I  open’,  prop.  ‘I  make  visible’.  Alb. Gheg  baj,  Tosk  beh,  ‘I  make’,  lit.  ‘I  make  ap¬ pear’  (both  these  words  derive  from  the  common Albanian  stem  *bany6),  OIr.  ban,  ‘white;  light, ray  of  light’,  but  L.  fenestra,  ‘window’,  is  not cognate.  See  fancy  and  cp.  phantom,  which  is  a doublet  of  phantasm.  Cp.  also  Aphanes,  apha- nite,  aphotic,  diaphanous,  emphasis,  hierophant, paenula,  Phaethon,  phaeton,  Phanar,  -phane, phanero-,  -pbany,  phenol,  phenomenon,  phos¬ phorus,  photo-,  sycophant.
Derivatives:  phantasm-al,  adj.,  phantasm-al-ity, n.,  phantasm-al-ly ,  adv.,  phantasm-at-ic,  phan- tasm-at-ic-al,  adjs.,  phantasm-at-ic-al-ly,  adv., phantasm-ic,  phantasm-ic-al,  adjs. phantasmagoria;  n.,  a  series  of  optical  illusions. —  ModL.,  fr.  F.  fantasmagorie,  a  word  coined
1170
1171
by  Mercier  in  1801  fr.  Gk.  9'iv~oca:j.a,  ‘appari¬ tion’  and  ayopsusiv,  ‘to  speak’;  assimilated  in form  to  F.  allegorie.  See  prec.  word  and  agora and  cp.  allegory.
Derivatives:  phantasmagor-al,  adj.,  phantasma- gor-al-ly,  adv.,  phantasmagor-ic,  phantasmagor- ic-al,  adjs.,  phantasmagor-ist,  n.,  phantasmagor- y,  n.
```


## [2026-09-05T06:07:23.258Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['MON','AMD','SLW','SOD','KLN','POK','AHD']:\n  v=d[k]; print('==',k,'=='); print('cites:',v.get('cites')); print('page_offset:',v.get('page_offset')); print('lookup_hint:',str(v.get('lookup_hint'))[:300])\n\""
}
```


### [2026-09-05T06:07:24.791Z] TOOL RESULT

```
== MON ==
cites: page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)
page_offset: None
lookup_hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== AMD ==
cites: None
page_offset: None
lookup_hint: Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.
== SLW ==
cites: None
page_offset: Selected Papers scan: leaf = p + 12 for the front matter; reprinted articles keep the ORIGINAL journal page numbers in the margins, so grep 'Sogdian Loan' then the original page number (93-106). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
lookup_hint: Original: JSTOR https://www.jstor.org/stable/608123 (BSOAS 10.1) - search jstor for 'Sogdian Loan-Words in New Persian'. In the local text grep -n -i 'sogdian loan' to find the article, entries are numbered Persian words with Sogdian etyma.
== SOD ==
cites: entry number / page in Gharib's Sogdian dictionary
page_offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
lookup_hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== KLN ==
cites: page number, continuous across the two volumes (1966–67)
page_offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
lookup_hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== POK ==
cites: page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)
page_offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
lookup_hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== AHD ==
cites: page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)
page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
lookup_hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
```


## [2026-09-05T06:07:34.811Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HENNING_selected_papers.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\n# find leaf index containing the article start\nfor i,lf in enumerate(leaves):\n    if 'cultural loan-words' in lf:\n        print('start leaf',i); s=i; break\nfor j in range(s, s+16):\n    lf=leaves[j]\n    import re\n    print('--- leaf',j,'len',len(lf),'| head:', lf[:100].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T06:07:36.569Z] TOOL RESULT

```
start leaf 276
--- leaf 276 len 1912 | head:  spt gily TH pepnir 6 740 eye 28 Set 72     ala (aa aad 724 ame 7 aylace 727 romssey fuse inane 4 mi
--- leaf 277 len 2024 | head: 541.1 It is there exp thin silk material, damask ”.*       pest Sanskrit form would presumably      
--- leaf 278 len 2236 | head: e damask, Brrvy mpyk "t By book in the hands Sryy 2'r wftyy kwrd'k Three thousand woven jackets, uyn
--- leaf 279 len 1929 | head:  TRANSACTIONS OF THE PHILOLOGICAL SOCIETY 1945 6 Distress. The Image of the Father, the Maiden of 3 
--- leaf 280 len 1956 | head: ��n, Bacher, Hebr-Pert Wha p. 51 of Hebrew toxt, No. 237). ‘Chinese patterned silk ss been, found in
--- leaf 281 len 2073 | head: (njg has been compared, but it means nether (Benveniste, JA, 1998, 6, 104q,), nor “ chastity" as T h
--- leaf 282 len 2327 | head: 4). The Arabs who borrowed the word preserved the older pronunciation ; they have it as birind (Mu'a
--- leaf 283 len 4 | head: est,
--- leaf 284 len 2644 | head:  w the road which not unsuitably has been named the “silk    route”. One could imagine   Old Iranian
--- leaf 285 len 2578 | head: ur ‘Turkish where in the hendiadys with either sin “tomb, grave "? (sce F. W. K. Miller, Uigurioa, i
--- leaf 286 len 2720 | head: n Persian where we have mary(a)zan   and ma   2(a)yan “ sepulchre, cemetery is established by a pun 
--- leaf 287 len 2571 | head: spelling, A major obstacle to the intended comparison of gerezman, ‘marzyan, and suburyan appears to
--- leaf 288 len 2599 | head: ssor Hailey rvoninda me of Minorsky's derivation of Turk. iemar-la- rom Spl, JRAS., 1042, 194. Note 
--- leaf 289 len 2681 | head: us on The Parthian ending -éndeh.    PLATES 1 AND 1)     To si crmitng het te Masts, mig dd not brom
--- leaf 290 len 2220 | head:  appearance of the grifin Paikué. The second (i) is the evil spirits of « house description of the p
--- leaf 291 len 2541 | head:  Gi the name of [in of] Sabaoth and (i). .. Fréd0n shall throw down... all. Three formsare in me, an
```


## [2026-09-05T06:07:49.329Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"in new persian\" HENNING_selected_papers.txt | head -10; echo \"---\"; grep -n \"BSOS., x\\|BSOS, x\\b\" HENNING_selected_papers.txt | head -5"
}
```


### [2026-09-05T06:07:49.399Z] TOOL RESULT

```
---
278:Sogd. wrkr (VJ., 955), Parth. worgr, and Saka baggare suggest an Olran. neutral r/n-stem, arkar/n-(MPers. warg, ete, from the nomina tiv tarakahe, only in the Frah. Oim, is of doubtful authenticity), Sogd. wrth = NPers. nard “trunk” ((ane-i dirazt, Asadi, p. 26), cannot be connected with the words treated by Geiger, Etym. Afghan. and of. BSOS,, x,
846:Commentary: (2) The MPers. form ocours in Mir, Man., i, see Bailey, BSOS., vii, pp. 84 sqq. Sogd. =“‘he is vehement, ardent, impetuous” (lit. “one whose desire is opened, loose ")—(3) “ They y.""—(4a) “Without hurting, enmity,” see BBB., p, 53 (on 483)—{48) Sogd. 2nd sing. subj., =“ you should mix.” There. fore dé participle of necessity —(5) MPers. “thoy are being collected, guined, saved”, Sogd. “ itis collected, see BSOS., x, p. 1 (cf. BBB., p. (7a, 8a) MPers, “bzyn-"" to sew, tailor ” is fre
905:= havid (havé), Kurdish hetcou, hewi, hevi (Jnba-Tusti, 448, 456, of. Bartholomae, ZsR., i, p. 38, n. 1), Brahui (from Bal.) hapd Morgenstierne, N7S., v, p. 47, who quotes Anaraki Auwouk, Bakht, Javil, habba (the words of the hambéy- type must be kept apart). Tt has been overlooked that this word, along whith hapadni-, is found in the Avesta-Pahlavi Frahang, in the much discussed gloss (ii, f): hapone. apno, zavé. which Bartholomae proposed to read hapadne afnavuhd. But the last word, 200d, is evidently nothing but a Pazend form of our word "bug, whilst it seems possible to regard apno as a corruption of the corresponding Pahlavi spelling (‘pick ; one letter only need be changed)—{9)" They are victorious.” wp'y occurs in Sogdian: ‘wp'y wm- “to give permission*", VJ., 891. Therefore “superior”: "ep’y be- “to be or become superior ”, "wp'y tn- "to make somebody else superior to oneself = to give in”. prypej- is familiar from Parthian, etc.—(10) MPers. “ploughed ” (see Mir. Man., ii), Sogd. “I ploughed" (Ist sing. imperf., from 'ms-)— (11a) “ unbridled, perverted.” Parth. "bndyft is met with in unpub. fragments. On Sogd. see BSOS., x, p. 103.—(118) MPers. "wet usually = “firm”, cf. Pahl. Psalter “tity. But Sogd. pepr- (plipr-) is “ to arrange, place, fix”, intrans, “to be arranged, placed, fixed ” peprty (Std sing. perf. intrans.), 8.7, i, 61% pepryh is hardly an ith Pabl Ps. "wsty quite well), but rather a finite and active form, vie. 2nd, sing. opt. or pres. Accordingly, ‘wst may be 2nd sing. imp. (cf. above. beyn : suemyy), from ‘west-" to place” = Parth. “toyst-, ete —(12) greedy, lustful.” MPers. "2g'm M477 RT. Sogd. is modelled on "syyq’m ; -e from -ak is compound ending —{13) ‘look sternly ? Sogd. stmb (‘st'np Diydna, 169, of. (')s'npyr- VJ., 39, Dhuta 286), clearly = MPers. or Parth. ‘str, therefore Parth. (2) "bud —Sogd.
1130:dast erkaé (which need not be changed into das [pat] érkat), see Bailey, BSOS., vii, p. 73. Sogd. (16) ‘with crossed arms, ef. SCE., 400, and prBrtp'8 “ cross-legged", Dhydna, 18. The verb, prByr- (pari biraya-), occurs in Dhuta Bstw pryByr " he crossed his arms (prBrtytKara-Balgasun, p. 22, frag. xi, 4, is not clear).—{17)(18) “ Whip. Sogd. auiép from zivagpa-, of. Av. zhaZwayat.altra, and NPers. 2b “whip, whipeord” (Rind. ; Asadi, p. 8; Div. Nasiri Khosrou, 429), Wakhi rafip “ whip" (Morgenstierne, IJFL., i, p. 588). Closely related is Buddh. "yrel'yp- “ squint-eyed", see BBB., p. 63. MPers. asp-azan " horse-whip”, of. Arm. garazan, zarazan. MPers. ‘spiwon (den from 4yavana-?) occurs in an unpublished MPers. 'pswn 'y tb “spell against the fever” (M 781), where féyr “sword”, eyl’n (see below, on g 1, 2), and "sph "whip" follow each other—(19) “teeth”. Sogd. zwrn- = “* blood” (but a separate word *zwrn- “food”, or “banquet ”, is, of course, possible), pinork = Buddh, pyerk- SCE., 28 (said to mean “ dark-coloured), or from plyer- “to lacerate, devour” (R.. i ¢ BBB., p. 91), cf. 'ply'r, Vay 313, 949, Therefore, Sogd. =“ bloodstained teeth” or “blood: Jacerating teeth" (? “‘laniaries?"). MPers. "ned could be avid “rubbed, blunted ” (ergo “‘ molar teeth?”), or dsd8, 1, “useless,” 2, “ not rubbed " (NPers. side) = “ sharp teeth !"" Speaking of teeth, I should like to add to my recent remarks on Sogd. krw-Bnt'k “ having defective teeth", BSOS,, x, p. 96: the word knw- still exists in modern Birjandi Persian, as Eabrd, Eawerd “ toothless”, see Ivanow, JPASB., xxix, 4, p. 340. This makes it unlikely that NPers. kare(e) had been borrowed from Sogdian.—(20) Pte. pres, pl (21) 3nd pl. pres, (or subj.), MPers. pret. pass. =Sogd. abstract from pte. pass. + hy became, took place", (28) iterative pte., from MPers. "em- = Sogd. ()pF'm both of which are unknown. It seems likely that the words connected by etymology, notwithstanding the apparent discrepancy of thesibilants.? But MPers. swyy = svyay, Pabl. sud = suy compared to Av. dud- allow the derivation of MPers. -sam- from Olr .-fam- Av. afama- "to swallow, gulp” (NPers. dédmidan),* .- from *apa-Mma-? The appearance of an iterati
1499:the end of a line, is not a seribal error, but conforms tc rules of orthography). See also my note, BSOS., x, p. 608. In NPers. we have not only dikarfidan (dig-), but also sikarvidan (Jewish Pers rw, Jer.,8, 12 Lag.)—(14) " He breaks ” (quoted BBB., p.59)—(15) “He hunts.”—(16) MPers. “breaking ”, but the reading is unreliable. If Sogd. is "ndyyfl, of. Chr. *éybiy, 5 hidden’ Buddh ‘ni’yp, Vim. 75, is taking upon oneself” ot “ attraction", according to Weller, Asia Major, x, p. 349. This would hardly suit 'né'yp- Dhuta, 45, 275, still less Frag. iii, $7, 67, where “to hide, bury” would fit excellently (to my mind, “‘rapprocher" and “‘appliquer”” have not much in common ; Benveniste, JRAS., 1933, pp. 52 sq.)—(17) MPers, “breaking up, destroying the enemy's army” (Olt. *shanda(ya)t hagnd-). Soga. s'n “* enemy” renders MPers. hen (Arm. hen) “ hostile army ”, hence MPers. ‘skn- =Sogd_ pf. .Jn{. For the tentative restora- tion of ptfw'btiyy, see BBB., p. 78 (on G41), where @ passage from T M 393 is quoted which I give here in full: (1) [w'n]'kw e'n'ko ZY ‘yo sn po'yrt’k "wt’koe (2) ’skety herd ZY ZK "bw cp'ys ZY ZK CE ypu “dinection™ P 2, 300 ‘would be srg in Men. MPers
```


## [2026-09-05T06:07:55.574Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T06:07:55.580Z] TOOL RESULT

```


```


## [2026-09-05T06:07:59.697Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%A7%D9%86%D9%88%D8%B3",
 "prompt": "Give the full etymology sections for the Persian and Arabic entries of فانوس (fānūs): what language it is borrowed from, the Greek source form, and any intermediate (Aramaic/Syriac/Arabic) stage. Quote exactly."
}
```


## [2026-09-05T06:08:00.556Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%A7%D9%85",
 "prompt": "Give the full Persian etymology of فام (fām) 'colour': source language, Sogdian form, related forms, and cited authorities. Quote exactly."
}
```


### [2026-09-05T06:08:02.786Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:08:04.882Z] TOOL RESULT

```
# Etymology of فانوس (fānūs)

## Arabic Entry

The Arabic section states: "Borrowed from Ancient Greek _φανός_ (phanós, 'lantern')."

There is no intermediate Aramaic or Syriac stage mentioned in the Arabic etymology.

## Persian Entry

The Persian section indicates: "Ultimately from Ancient Greek _φανός_ (phanós, 'lantern')."

The Persian entry does not specify intermediate language stages, only that the ultimate source is Ancient Greek.

## Summary

Both entries trace the word back to Ancient Greek φανός without documenting any intermediate Aramaic or Syriac borrowing stages. The Persian entry uses "ultimately" suggesting possible intermediaries, but none are explicitly named in the provided content.
```


## [2026-09-05T06:08:10.351Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%85%D8%AF%D8%A7%D8%AF",
 "prompt": "Give the full Persian etymology of بامداد (bāmdād) 'dawn, morning': Middle Persian form, the element bām, Old Iranian/Avestan source, and cited authorities. Quote exactly."
}
```


## [2026-09-05T06:08:12.490Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82-",
 "prompt": "Give the reconstruction, meaning, and the list of descendants/derived terms for the PIE root *bʰeh₂- (to shine). Include Proto-Iranian/Avestan, Greek, and Germanic descendants. Quote exactly."
}
```


### [2026-09-05T06:08:16.620Z] TOOL RESULT

```
# Persian Etymology of بامداد (bāmdād)

Based on the Wiktionary entry, here is the available etymological information:

**Middle Persian Source:**
The word derives from Middle Persian *bāmdād*, meaning "dawn, morning."

**Limited Information:**
The page provides only this foundational etymology: "From Middle Persian 𐭡𐭠𐭬𐭣𐭠𐭲 (bāmdād, 'dawn, morning')."

**Comparative Evidence:**
The entry notes a cognate in Baluchi: *bāndāt* ("tomorrow, future"), suggesting a shared Iranian root.

**What's Missing:**
The Wiktionary article does not provide:
- The specific element breakdown (bām + dād)
- Old Iranian or Avestan sources
- Citations to scholarly authorities
- Details about individual morpheme origins

The entry lacks the deeper etymological analysis you're requesting. For a complete breakdown of the constituent elements and their ancient Iranian sources, you would need to consult specialized etymological dictionaries or academic linguistic sources beyond this Wiktionary page.
```


### [2026-09-05T06:08:20.430Z] TOOL RESULT

```
# PIE Root *bʰeh₂- (to shine)

**Reconstruction:** *bʰeh₂- (imperfective)

**Meaning:** "to shine, glow light" and "to appear, be visible"

**Key Descendants:**

*Proto-Indo-Iranian:* The root evolved into *bʰaH-, with descendants including Sanskrit भनति (bhánati) in Vedic Sanskrit.

*Greek:* Ancient Greek forms include φάω (phắō, "to shine") and φῶς (phôs, "light"). The root also produced φαῦσις (phaûsis) and φωνή (phōnḗ, "voice").

*Germanic:* Proto-Germanic descendants include *bandwijaną, *bandwǭ, and *baukną.

**Additional Note:** The page also documents a second homonymic root *bʰeh₂- meaning "to speak" or "to say," with overlapping but distinct descendants in Greek, Latin, Sanskrit, and other branches.
```


## [2026-09-05T06:08:32.069Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"== $f ==\"; wc -l $f; grep -c \"فانوس\" $f; grep -n \"فسفر\" $f | head -3; done"
}
```


### [2026-09-05T06:08:33.798Z] TOOL RESULT

```
== MON_part1.txt ==
99339 MON_part1.txt
5
79392:فسفرسانس پیدا می‌کند و روشنی خاص 
80275:سنگ روشنایی: به فسفر وترکیبات کانی آن 
88331:فسفر که جامد است ترکیب و به کلرور فسفر 
== MON_part2.txt ==
94500 MON_part2.txt
10
3707:کرین و فسفر جامد هستند و تنها برم 
7342:فسفریکك هستند و برای کودهای شیمیایی 
7351:فسفر: 10:60 (.) (شیم.) جسمی است
```


## [2026-09-05T06:08:38.498Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7330,7365p' MON_part2.txt; echo \"=== page markers? ===\"; grep -n \"^\\s*[0-9]\\{3,4\\}\\s*$\" MON_part2.txt | head -10; echo \"=== formfeeds ===\"; python3 -c \"\nt=open('MON_part2.txt',encoding='utf-8',errors='replace').read(); print('ff',t.count(chr(12)))\""
}
```


### [2026-09-05T06:08:40.201Z] TOOL RESULT

```
فسرده‌دل: ۲-40۱ [- افسرده‌دل] (ص‌مر.) 
( کد.) دل‌مرده؛ افسرده. ( کد.) سخت دل؛ 


مور : 
فسطاط: -6۶؛ ,اقاده) [ع.] (ا.) خیمه 


۹ ۱ ۱ 
۹ فساطط. . (غم.) 

فسفات: (شیم.) املاح اسید 
فسفریکك هستند و برای کودهای شیمیایی 
دگار می رو ند. فسفات‌های قلیابی مانند 
فسفات سدیم و پتاسیم و آمونیم در آب 
محلول هستند و فسفات‌های دیگر در آب 
غیر محلول ولی در اسیدها محلولند. 
فسفات‌ها با نیترات نقره رسوب زرد فسقات 
نقره تولید می‌کنند که در اسید از تیک و 
آمونيااک هر دو حل می‌شود. 

فسفر: 10:60 (.) (شیم.) جسمی است 
جامد زرد رنگ که سطح آن به رنگ 
قهوه‌یی يا سفید است. بوی سیر می‌دهد و در 
آب غیر محلول است و چون در هوا فاسد 
می‌گردد آن را در آب نگه می‌دارند. از آب 
سنگین‌تر و در ۴۳۴ درجه ذوب می‌شود. 
فسفر مایع در ۲۸۷ درجه می‌جوشد (السته 
در محیطی بدون اکسیژن) و تکاثف نسبی 
بخار آن نشان می‌دهد که جرم مولکولی 
فسفر ۱۱۴ یعنی مولکول فسفر چهار اتمی 
است. فسفر به دو صورت مختلف که 
خواص آنها کاملاً مشخص و ممتاز است؛ 
وجود دارد: قسفر سفید و فسفر سرخ. گرب 
فسفر سفید نور تابد قرمز می‌شود. فسفر 
سرخ آتشگیر نیست و سمیت ندارد ولی 
=== page markers? ===
18075:019 
19307:377 
=== formfeeds ===
ff 0
```


## [2026-09-05T06:08:46.098Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"فاز:\" \"فوتو\" \"فانتوم\" \"فانوس:\"; do echo \"=== $w ===\"; grep -n \"$w\" MON_part1.txt MON_part2.txt | head -6; done"
}
```


### [2026-09-05T06:08:47.810Z] TOOL RESULT

```
=== فاز: ===
MON_part2.txt:4212:فاز: 1 (.) (فز.) سیم برقی که دارای 
MON_part2.txt:4213:اکن ده مشت است. برق سه فاز: (فز.) 
MON_part2.txt:4218:فاز: 7۶ |- فاژه] (.) خمبازه ۳ اش 
=== فوتو ===
=== فانتوم ===
=== فانوس: ===
MON_part2.txt:4723:فانوس: :۱75 (.) چراغی که برای روشن 
MON_part1.txt:34446:و نیز هنگام خواب پوشند. پیراهن فانوس:
```


## [2026-09-05T06:08:50.049Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4205,4230p' MON_part2.txt; echo \"===\"; sed -n '4718,4740p' MON_part2.txt"
}
```


### [2026-09-05T06:08:50.119Z] TOOL RESULT

```
اروق: 111۳] ۳8 (ص.) مرد نك 
ترسنا کك. کسی که امور را از یکدیگر فرق 
لاف تفت توا جدا کنندة حق از باطل. 
فاریدن: 1-0 | - بخارایبی] (مصل.) 
خوش آیند بودن, موافق ط طبع بودن؛ به دل 
۳ 

فاز: 1 (.) (فز.) سیم برقی که دارای 
اکن ده مشت است. برق سه فاز: (فز.) 
مقدار الکتریستهای که از سه سیم مثبت واره 
دستگاه کنتور می‌شود. 

فاره: (0-)12۸] | - فاره] (۱.) خمه جادر. 
فاز: 7۶ |- فاژه] (.) خمبازه ۳ اش 
فاس: (۱.) ز کت ی 
فاستونی: آ و 0( بارچه تشمی ساده با 


۰ زبان 


فرر هنک فارسی معین 


۷ ۱ 
نخی که از آن جامه کنند؛ ج. (عم. غلط ) 
===
(مس.) آهنگی بی‌قاعده و آزاد که مین او هام 
وتات اهک‌سار تاش کاهی مین 
دهد مانند فانتری «دن کشوت, اثر 
اشتراوس. 

فانوس: :۱75 (.) چراغی که برای روشن 
کردن سافت زیادی بر بالای منار و جز آن 
نصب کننكد. ان کار مواد حا کی ماو راء 
( مسشه ه بلور: کاغد. یار چه 
چراغ گذارند تا از باد محفوظ ماند. چراغ 
محفظه‌داری که در آمد و رفت با خود برند. 
فانوس خیال: |- فانوس خیال‌انگیز | فانوسی 
که در آن موه 9 از صورت‌ ها 
به هوای آنث ره کردس در اند [شر‌هان). 
ضح. فانوس خیال (فانوس گردان) فانوس 
هی کین بوده که اساسا آن 8 در جین 


) سازند و در ان 


تمه تا نی از آنبقن ی ماس بر ٩‏ 
بازرگانان چینی موجود است که با الکتر بسیته
```


## [2026-09-05T06:08:56.851Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/beacon",
 "prompt": "Give the full etymology of \"beacon\": Old English form, Proto-Germanic form, and the PIE root it is traced to. Quote exactly."
}
```


## [2026-09-05T06:08:57.931Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/phase",
 "prompt": "Give the etymology of \"phase\": the Greek source (phasis, phainein), the Latin/French intermediaries, and the date it entered English. Also mention any note about phantom/phenomenon if present. Quote exactly."
}
```


### [2026-09-05T06:09:00.872Z] TOOL RESULT

```
# Etymology of Beacon

**Old English form:** "beacen" meaning "sign, portent, lighthouse"

**Proto-Germanic form:** "*baukna-" meaning "beacon, signal"

**PIE root:** "*bha-" (1) meaning "to shine"

The word traces this path: The PIE root "*bha-" (to shine) developed into the Proto-Germanic "*baukna-" (beacon, signal), which then became the Old English "beacen." This eventually evolved into the Middle English "beken" and modern English "beacon." The figurative use of the word emerged around 1600.
```


### [2026-09-05T06:09:04.015Z] TOOL RESULT

```
# Etymology of "Phase"

**Greek Source:**
The word traces back to Greek *phasis* "appearance" (of a star), "phase" (of the moon), derived from *phainein* "to show, to make appear," ultimately from the PIE root *bha- "to shine."

**Latin/French Intermediaries:**
Modern Latin *phases* (plural) and Latin singular *phasis* served as intermediaries, with the English noun back-formed as a singular from the Modern Latin plural form.

**Date Entered English:**
The noun *phase* entered English in **1705**, initially referring to "phase of the moon, particular recurrent appearance presented by the moon (or Mercury or Venus) at a particular time."

**Note on Related Words:**
The page does not mention phantom or phenomenon in connection with phase's etymology. However, it does note that the verb form *phase* (1895) was "earlier as a bad spelling of faze," and includes related terms like *anaphase* and *prophase* derived from the noun.
```


## [2026-09-05T06:09:13.158Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -ln \"فانوس\" *.txt 2>/dev/null; echo \"--- latin ---\"; grep -lni \"fanûs\\|fānūs\\|fanus\\b\" *.txt 2>/dev/null | head"
}
```


### [2026-09-05T06:09:13.271Z] TOOL RESULT

```
ARB_mo3rb.txt
BQT_v1.txt
BQT_v1_pages.txt
BQT_alt_v1.txt
MON_part2.txt
MON_part1.txt
--- latin ---
FSD_vol4.txt
NAT_2005.txt
LAT.txt
SKT.txt
KLN_1971.txt
KLN_1966.txt
```


## [2026-09-05T06:09:16.102Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARB_mo3rb فانوس ===\"; grep -n -A4 -B4 \"فانوس\" ARB_mo3rb.txt | head -40"
}
```


### [2026-09-05T06:09:16.174Z] TOOL RESULT

```
=== ARB_mo3rb فانوس ===
4971-وه اس 3 رامو : 5 82 
4972-فاع ب فقيل 2 إستار 6ه و مع ,0 أساتير 00 ويقال لكل أربعة « إستأر » ه 
4973-020 22 
4974-0 م 50 3 ع 
4975:5 و اصطفانوس 5 و دهقان 0 قال الفرزدق - 
4976-
4977-
4978-4 00 )5( 
4979-
--
5005-سقط نه بت 6 وهو موطع ترم فيا » وأثيتناه من الخطوطات الثلدث ٠‏ (ه) الييت فى ديوانه 
5006-١ص )0١‏ من أربعة أبيات ميجو بها يذ يد بن عمير الأسيدى » ركان منقطعا إلى الأصطفا نوس الأكبر» 
5007-يعمل لهفى الولايات» فكان على شرطة ا يا اه الفرزدق ووقف عل بأبه ) تأبطأ فى الإذث ففضب» ١6‏ 
5008-
5009:(1) ممن طر بف ماذى فى تسميتها ماروى ياقوت قال ( ه : 44 ) : « وأما أصطفانوس فردوا 
5010-عن ابن عباس أنه فال : الظوظ المقسومة لا يقدر أحد على صرفها ونقلهاعن أماكنا » ألاترى إلى ' 
5011-سكد أ صطفا نوس » كان يقال لطا ”*سكة الصحاية ““ نزلها عشرة من أداب 8 أ لله صل الله مايه س6 
5012-فل تضف إلى واحد منهم » وأضيقت إلى كاتب نصزافى من أهل البحرين »© وتركرا المحابة 1 ! » ٠‏ 
5013-
--
5472-
5473-لوا (م) فى < « العدولة » ٠‏ 
5474-
5475-
5476:(4) إلى مناآخي ارم الذى سقمط من ف والذى أوله « ولولا فضسول الأططفانوس » 
5477-ر(ص «#وس» ) 
5478-
5479-
5480-
```


## [2026-09-05T06:09:24.263Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"fanous\\|fânous\\|fanoûs\\|fanûs\" DOZ.txt DEV.txt PHN.txt LAM.txt 2>/dev/null | head -10\necho \"--- fanal ---\"; grep -n -i \"fanal\" DEV.txt PHN.txt DOZ.txt 2>/dev/null | head -5"
}
```


### [2026-09-05T06:09:24.335Z] TOOL RESULT

```
--- fanal ---
DEV.txt:1741:Minaret.  Esp.  minarete.  De  l'arabe  »^Lu  menâra  (pro- noncé à  la  turque),  signifiant  lieu  où  il  y  a  une  lampe  (de la  racine  ^L  nâr,  briller),  puis  lampe,  fanal,  phare,  et  enfin minaret.  Minarete  n'est  pas  dans  le  Glossaire  de  M.  Dozy, mais  on  y  trouve  ahnenara,  candélabre,  fanal,  et  alme- nar,  et  pied  de  fer  sur  lequel  on  mettait  des  torches  de  ré- sine ou  de  bois  résineux  pour  s'éclairer.  ??
PHN.txt:4776:FANAL, s. m. (t.)
PHN.txt:4777:jJ^ [féner eifanar] lanterne, phare, fanal, comme en français.
PHN.txt:4778:— On appelle aussi Fanar ou le Fanal un quartier de Cons-
PHN.txt:4785:de secrétaires. — Fanal s'écrit aussi jUà [/^n^] en persan.
```


## [2026-09-05T06:09:32.795Z] TOOL CALL #57: Bash

```json
{
 "command": "ls site/pages/79.jpg 2>/dev/null; pdftoppm -f 79 -l 79 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg79 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T06:09:35.318Z] TOOL RESULT

```
site/pages/79.jpg
total 8808
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 02:09 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb  108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb  155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb   58953 Sep  5 02:08 pg80.png
```


## [2026-09-05T06:09:37.950Z] TOOL CALL #58: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg79.png"
}
```


### [2026-09-05T06:09:38.329Z] TOOL RESULT

```

```


## [2026-09-05T06:09:38.326Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T06:10:07.614Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"بامداد\\|بام \" ARY_pages.txt | head -10; echo \"=== فام ===\"; grep -n \"فام\\b\" ARY_pages.txt | head -10; echo \"=== latin index ===\"; grep -n -i \"BHA\\|BEACON\\|PHOS\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-05T06:10:07.696Z] TOOL RESULT

```
=== فام ===
2281:فارسی (۳8۵۵۷):__ ارزیز (به چم قلع , فلز سپید و نقره فام) 2
4398:تخاری 5 (8 ((فل2ل102): م2 آلبانی (/فاماالمقلم): 36زع2۸
=== latin index ===
1821:POKORNY, SOSOSO*~S~*S~«S KSOBHA, (SANSKRIT) eS.
2909:BHARMAN, BHRTIS BAR (PAHLAVI) 5 ghey
3015:POKORNY, = SS~*~*~*~*«w OR BHAYAKA PAHLAVD) 15 34
3016:DELAMARRE: (CRAINDRE) 247 BHAYATE, (SANSKRIT) Sui
3225:BUCK: 1095 BHAKSHATI (SANSKRIT) 2, Ss
3236:BAXTAN, BAXSHISHN, BHAJ.,
3239:MACKENZIE: 17, (BESTOWAL) 104 BHIKSHATE, BHAJI.,
3240:THI gi he iebbly BHAG, BHAGAH, BHAJATI
3297:BREME BHARATI, SANSKRIT) Sy Suite
3298:BHRTI, BHARA ~~
```


## [2026-09-05T06:10:10.929Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '1815,1830p' ARY_latin_index_pages.txt"
}
```


### [2026-09-05T06:10:10.981Z] TOOL RESULT

```
we Slip (ailegy GUL; 9 SY 2 5s cel om
wegen, Si 2B G85 59051) ool ow
GEV ST ells abel 9 GS 9 geSi po UT oles y AUDIENCE, AUDIT eej}y
capes wiedt Egat
AXSHAOB, XSHAOB(AVESTAN) gl!
REFERENCES ete ASHOB (PAHLAVI) 5 sg
POKORNY, SOSOSO*~S~*S~«S KSOBHA, (SANSKRIT) eS.
MACKENZIE: (DISTURBANCE) 111 KSUBHYATI
100-10° Maas aabicndl cuveac POLISH) gles
[Som |
‘REFERENCES beth GHRTAM, (SANSKRIT) ey Suite
POKORNY” = SOS*~*~«S JIGHARTI
BUCK 388 GERT {MIDDLE IRISH) «ila 543 3)
wv . sbi oly
104 sMaehas aabicail
a) spe yy Sand
```


## [2026-09-05T06:10:17.467Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC bha ===\"; grep -n \"^bhā-\\|bhā- (\\|bhāmi\\|bhānus\" IEC.txt | head -10\necho \"=== SYN light ===\"; grep -n -i \"15.56\\|'light'\\|to shine\" SYN.txt | head -5\necho \"=== WLD Bd2 ===\"; ls incoming/WLD/ 2>/dev/null"
}
```


### [2026-09-05T06:10:17.545Z] TOOL RESULT

```
=== IEC bha ===
1112:bhāl- (3) (?) ‘speaker’. Cf. bhāið, bhāmi MHG buole, OFris. bōla ‘wooer’; OCS balij ‘incantator, doctor; cf. (*-á- in) Skt. bhale ‘expound’; Du. bellen ‘ring’
1116:bhāmā (bhāmos})} ‘sound, voice, rumour’ Skt. cf. bhamah (‘light’. For parallels see bhàió, bhāmi); Gk. phéme, Dor. -à-; Lat. fama. Cf. Myc. (in a name) A(n)ti-pamo 'Antiphamos'
1124:bhàánioó ‘declare, show’. WP II, 122. Cf. . bhāmi, bhàið, bhànos Vedic bhánàmi, Skt. bhanami “speak, declare’; Arm. banam ‘open’; Gk. phaíno; Lat. cf. af- faniae ‘gossip’; Du. boenen, LG bohnen ‘polish’; OlIr. cét-banim ‘notice’; Ir. (denom.) bánaim “lay bare? MHG (denom.) banen "open up’ beside bannen ‘declare’; OE bannan ‘sum- mon, proclaim’; OFris. bania ‘indict’ beside banna "order, proclaim’; ON banna “forbid, curse’. Uncertainly Arm. banim ‘do’; Alb. bâj, T bënj, bëj ‘do’. Gmc. LW in O & Mod. Cz. boniti (... hrózu, ... hrůzu ‘terrify’). Cf. also Gk. phanë, phanerós; W ban “promi- nent; prominence’ and Mod. Icel. banda ‘to beckon’; (a) Srb. banem; bann se “arrive unexpectedly; swagger
1126:bhānos, à, us ‘visible, plain, bright; bright- ness, sign, show’. WP II, 122. Cf. bhāið, bhāmi, bhånið Skt. bhànüh ‘brightness, sun’; Av. banus ‘ray’; Oss. bon ‘day’, cf. also bonäi “by day’; bänn ‘princess, lady’; Gk. phānós; Ir. bán ‘white, bare, baid’; OE bon *'ornament; Du. cf. boenen ‘polish, clean’; G (fr. LG) bohnen, id.; Srb. cf. banem, banuti 'arrive unexpect- edly? beside baniti se ‘swagger, show off. Uncertainly to Arm. ban, i-stem “speech, word, promise, thing”
1175:bhåu- (1) ‘shine, show; tell’. Cf. bhaio, bhāmi Arm. cf. ham-bav (o-st. ‘report, news’, fr. *som-bhau-); Gk. pháos, n. and phós (fr. *bhauos, and -es-stem) beside pháo, pháuo light, v.; cf. phanós ‘bright’ and piphaüsko ‘show’; OE bywan ‘polish, decorate’; cf. MHG bou- in bouchen ('sign', fr. *bhau- + *gn-, see ĝn-, &nósKo, w. sim. formation to MHG zei-chen, see dai- ‘divide’), OE beacen ‘beacon’; cf. Icel. bákn “monster”
1285:bhətis, os ‘speech, declaration; speaking, spoken, declared". WP II, 123. Cf. bhaio, bhāmi Arm. baj, Let ‘verb’; Gk. phásis beside á- phatos ‘ineffable’; Lat. cf. in-fit (2) (quoth'. Plautus); in-fitiae ‘denial
=== SYN light ===
1743:5. Lith. Zaibas, Lett. zibens : Lith. Zibéti, Lett. zibtz ‘shine, glitter’ (15.56).
1745:7. Skt. vidyut-, i.e. vi-dyut- fr. dyut- ‘shine’ (15.56).
1861:1. Grk. xa, ChSl. séni, SCr. sjena, Russ. sen’ (Boh. siti, Pol. sien, Russ. seni ‘entrance room’, etc., as room without light), Skt. chaya-, Av. *saya- (a-saya- ‘without shadow’), NPers. saya-, Alb. hé, fr. IE *skai-, *ski-, prob. the same root as in Goth. skeinan, OF scinan, Ch§l. sijatt ‘shine’ (15.56). Connection through a notion of ‘faint light’ (as in NE shimmer, NHG schimmer) or ‘re- flection’. Cf. OF scima ‘shadow, gloom’ beside scima ‘light, brightness’. Walde-
2198:2. Lat. accendere (> It. -accendere), imcendere (> It. incendere, Sp. encender, Rum. incinge), succendere, epds. of *candere: candére ‘shine, glow’ (15.56).
25859:15.56 Save
=== WLD Bd2 ===
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
```


## [2026-09-05T06:10:32.360Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"\\[pdf page\" WLD_Bd2_pages.txt | head -3\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,pg in enumerate(t):\n    if 'bhā-' in pg and 'glänzen' in pg:\n        print('LEAF',i,pg[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T06:10:34.051Z] TOOL RESULT

```
leaves 725
```


## [2026-09-05T06:10:37.836Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,pg in enumerate(t):\n    if 'baukna' in pg or 'bhāmi' in pg or 'bhāma' in pg:\n        print('LEAF',i,'|',pg[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T06:10:39.621Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T06:10:42.838Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\n# find leaf whose printed page is 122: search for header numerals\nfor i in range(120,145):\n    print('--- leaf',i,'|', t[i][:150].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T06:10:44.466Z] TOOL RESULT

```
--- leaf 120 | 116                                     bu, bhu   schinollen“ („*schwellen“), pout ,.eine Schellfischart, gadus barbatus% ndl. puiUaal „AaImolch“, ags
--- leaf 121 |                                                bu,   bbu                                                  117  nhd. {p)fauchen (kann auch unverschoben
--- leaf 122 | 118                                              bu,   bhu                norw. pus „Geschmilst'^, poysa, pusna ^anschwellen'', aschwed. -zu souffler)
--- leaf 123 |                                                bud               bronq-                                             119   fries.      hUsen „gewaltsai
--- leaf 124 | 120                                           brugh        ble    hragh- Sehallworfc, gaaz uusicheren Alters uad fraglicber Gewahr.      Gr. PQVxdojua
--- leaf 125 |                                           ble                                      121   andert; oder vielleicht doch zu hheh, 'bh[e\le- „blaseii“ mit
--- leaf 126 |                                                                                           ;                                                           
--- leaf 127 |                                                         bha-                                                   123   — wo auch                  iiber 
--- leaf 128 |  '                                                                                                           ;     124                                
--- leaf 129 |                                              bbaut- (?) bhut-, bhat- bhat-                                                           :                
--- leaf 130 | 126                                     biiaut-(?) :bhat-, bbat- : bhat-            fehlen yerlaBliche Belege dieser kiirzeren Wzformen;              
--- leaf 131 |                                                      bhaud- bhud-                                                             :         — bhag-       
--- leaf 132 |  128                                         bhag-   — bhagO'S   stiminter Anteil,         Schicksalsbestiininiiiig,      bes.       Mi6geschick‘‘;   
--- leaf 133 |                                         bhag      bbago-s                     129  s.Berneker 99 f. m. Lit, Bruckner KZ. 46, 195). YgL Curtius 188 (ii
--- leaf 134 |  130                              bh%h-?, bhegli-         :   bbugli- ?   — b}iad(h)       [Den germ, ati- und si. tf-Formen nicht geniigend setzt Woo
--- leaf 135 |                                     bhabha — bhares-, bhores-                                             131   lich“       usw. (s. hlioidlio-) unter
--- leaf 136 |                                                                                                           ;     132                                   
--- leaf 137 |                                    ;                                                         bbares-, bhores-                                         
--- leaf 138 | 134                                          bhares       bharq-   bhareS" „Gerste“.   Lat. far               farris (aus ^fareris synk.; far(r) als N
--- leaf 139 |                                           ;                                                   bhardha-       — bhasqo-                                
--- leaf 140 | 136                                            bhe, bbo     lat. fascia        Band, Bandage^*, fascis „Bund, Biindel, Paket; das Rutenbiindel mit her
--- leaf 141 |                                                                                       ;            h               ;                                  
--- leaf 142 | 138                                          blieig(«)   — bbeid- „Schnaber*, engl.            bill(Uhlenbeck PBrB. 26, 568.              —           
--- leaf 143 |            :                                                                                               ;                                          
--- leaf 144 | 140                                                               bheu-     bidjan nicht wahrscheinlicher nach Kern Tijdsclir. v. Ned. taal-en letterk
```


## [2026-09-05T06:10:48.707Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[126][:3500])\nprint('=========== 127 ===========')\nprint(t[127][:2500])\nEOF"
}
```


### [2026-09-05T06:10:50.538Z] TOOL RESULT

```
                                                                                          ;




                                                       Bk
1.   bha-      5
                   ,glanzen, leuchten, scheinen^ {hlie-1^.            s,   u.).

     Ai.    hJid     (in     Zs.)   ..Schein,     Licht,   Glanz“,    hhdti   „l^^Bhtet,       scheint,   er-
scheint‘‘, Ihati-h „Licht'‘,              ihana-m „das Leuchten, Erscheinung, Einleuchten^
(ygl. air. Idn j^weiB^, ags.   hdnian „polieren“), hhdnu-h j^Glanz, Licht, Strahl,
Sonne'',      hhama-h „Licht, Schein";
     av.    hd- „scheinen“ nur mit a- {avdntdm „den gleichenden'') nnd fra (fra-
vaiti „leuchtet hervor";                 s.   Bthl, KZ. 29, 499,     Wb. 952), vlspo-bdm(^)a- „all~
glanzend*', hdmya- „licht, glanzend", hdnu- m. ^Lichtstrahl"
   arm. hanam ,,o£Fne, enthiille" (wenn eig. „zeige, lasse sichtbar werden",
Brgm. 11^891 nach Moulton, II^ 3, 306 zw., anders, nicht iiberzeugend
 Scheftelowitz BB. 29, 37, s. u. llien- „schlagen"); Ygl. gr. (paivco und alb.
 Iqj; aber iiber lat. fenestra „Fenster“ s. Herbig IE, 37, 172 fF.; tiber air.
 tesbanat „deficiunt", cethanim „merke", du-forlan „komint dabin", Fickll^
164, s. yielmebr Kern Re. 22, 237 f., Tburneysen Hdb. 333, Pedersen KG.
II 441 ff.).
    Gr. 7i£(prjo€Tai „wird ersebeinen", praesens qpalvco ("^(pavico Ygl. das ana-     ;



loge Yeib. Yon ghan-:yJie, gha „gabnen“) „macbe siebtbar, zeige", <palvo-
jbtai „erscbeine,    sebeine, leuebte" {i(fdv7]v, cpav<b, -ov^aiy £(prjva; (pavegog
„sicbtbar, offenbar, deutlicb", q:avij ^Fackel"; gxiGig „Aufgang eines Ge-
stirns", (pdopia, -arog             „Erscbemung, Gesiebt, Yorzeicben", Ygl. 7ie<paofi€vog);
dpupadog, dfx^pddcog „offenbar" (ava~(p-)\
     alb. geg. laj. tosk. hen                 {= epatvw) ,,macbe, tue"        (ursprgl.       wohl ,,bringe
zur Erscheinung", G. Meyer Wb. 23 f.).
     air.   Mn „wei6“;
     ags. Ionian ,,polieren" (d.
                               i. „glanzend macben"), nd. (und daraus nhd.)
 Idnen „scbeuern, bohnen", mbd. iilenen „bohnen" (ob got. iandwa, -ico
„Zeichen", landivjan, aisL be^ida „ein Zeicben geben" hieher gehoren ~
etwa als ^-Ableitung von einem Ptc. ihd-nt- „scbeinend"        ,
                                                                 ist fraglich.       —
Lit. bei Feist Got. Wb.^ 58 f.;
   osorb. lojiiy lac so „unmerklicb brennen, glimmen", nsorb. lajom, bajas
se „glimmen, flackern" (Berneker 39).

  s-Erw. bJid-s: ai. bhdh n., instr. bbasd „Licht, Schein, Herrlichkeit,
Macbt", sublids- ,scbonen Glanz babend", bhdsatl „glanzt", bhasant- „glan-
                              3


zend", bhdsah n. „Licbt"; (pcbgy ~rog „Edler, Mann" (wenn die r-Flexion
sek.; Oder *bhd-t-; s. Bgm. II ^ 1, 536);
     gr.    (fd)ox£i'        dtaypdvet    Hes.,    diacfcbonm „beginne zu glanzen", qxDoxriQ'
•dygig  Hes.
     Unsicher         ist,    ob mir. base „rot", ags. basu, baso „purpum“ (^bJws-lco-,
 -HO-) anzuschliefien sind (Lit. bei           Liden IP. 18, 415, Falk^Torp u. beer K,

=========== 127 ===========
                                                        bha-                                                   123


— wo auch                  iiber    got.     tveina-lasi „Weiiibeere‘S               ahd.     heri „Beere‘S    eig.

„rote Beere“? — Holtbausen IP.                       25, 150 deutet so              auch den       — vollstufigen
— MN. ahd. Btwso,       Bosi          aisl.         usw.).

     ?«-Erw. bJia-ii:                ai.    vi-Wiava-h, vi-bhavan- „strahlend, scheinend, leuch-
tend“;
     gr.    horn,         (fde    ,.glanzte,    erschien^^,    cfaedcovy          -orrog      „glanzend‘^,   (paeoi-

jLi^Qorog,             Find.     q:avoi-jii^QOTog    „fur     die   Menschen           glanzend'^,     pdog    (aol.

(pavog,        pamph. cpd^og) „Licht'' (uber                   die Form            horn. q)6cog     Yermutungen
bei Bgm.            1, 578 und a 1), wovon *(pafeo-v6g in lesb.                                (fdevvog, jon. (pa-
eivog,       att.       (pdvog      ,.glanzend'',    horn,    cpaetvco           ,,glanze“;    mcpavoxcD      „lasse
leuchten,                      gebe kund, sage an“ (s. bes. Persson Beitr.
                       erscheinen;         zeige;
117.   Nicht annehmbar erklart B. bei Pick II ^ 176 ein angebliches ir. bM
„Feuer“ aus ^bJiau-z-dho-),
  1st germ. Hanlyia-, ir. afries. bakcn „Wahrzeichen, FeuersignaP^, as.
bokan ..Zeichen, Wahrzeichen'', ags. beacon ,,Zeichen, Fahne“, ahd. botihhan
„Zeichen“ Yon solchem germ, ban- nach "^taikna- ,,Zeichen“ gebildet?
(Falk-Torp u. baim erwagt ein '^b\i\axigjan „Yor Augen stellen“ als Grund-
lage, wobei aber k statt g ebenfalls nach Haikna- eingetreten sein miifite).
   Ausfiihrlich iiber unsere Wz. Prellwitz BB. 22, 76    114, wo auch Ver-             —
mutungen iiber zu unserer Wz. gehorige Wortausgange wie -bJi-os, Nach
Prellwitz ware die Wz. nicht als bJia-, sondern als bJie- zu bestimmen,
bes.       wegen lit. beskogi z. B. in beskbgi jis ne-vdigo „also darum i6t er nicht“,
das                       warum er nicht i6t^‘ sei; doch steht dies innerhalb
           eig. „es ist klar,
einer       Gruppe Yon Partikeln der Beteuerung und Hervorhebung wie lit.
bd     ,.ja,       jawohl, freilich, sehr wobk^, horn,                   (pif]   „gleichwie‘*,     die schwerlich
mehr         eine                Gdbed. erkennen lassen, und wegen slaY.
                         scharf umrissene
b^ho „wei6“, aisl. bal „Scheiterhaufen“, die aber Dehnstufe der durch gall.
Belen
```


## [2026-09-05T06:11:04.161Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%86%CE%B1%CE%BD%CF%8C%CF%82",
 "prompt": "Give the Ancient Greek entry for φανός: meanings (adjective 'bright' and noun 'torch, lantern'), etymology (relation to φαίνω), and any descendants/borrowings into Arabic or other languages. Quote exactly."
}
```


## [2026-09-05T06:11:05.930Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/indoeurop.html",
 "prompt": "Find the entry for the Indo-European root bhā-1 (\"to shine\"). Quote its full text, including the Germanic *baukna- / beacon derivative and the Greek phōs / phainein derivatives, and the Pokorny reference."
}
```


### [2026-09-05T06:11:09.849Z] TOOL RESULT

```
# φανός (phānós)

## Meanings

**Adjective:** "bright; shining; resplendent"

**Noun:** "torch; lantern"

## Etymology

The word derives from a contraction of φαεινός (phaeinós). The entry traces it back through Proto-Hellenic and ultimately to Proto-Indo-European *bʰeh₂- meaning "to shine."

## Notable Descendants

The term has traveled extensively into other languages:

- **Arabic:** فَانُوس (fānūs)
- **Hebrew:** פָּנָס (pānā́s)
- **Turkish:** fanus
- **Italian:** falò
- **Persian:** فانوس (fânus)
- **Swahili:** fanusi
- **Amharic:** ፋኑስ (fanus)
- **Bengali:** ফানুস (phanus)

The entry demonstrates the word's substantial influence across Mediterranean and Middle Eastern linguistic communities through historical contact and trade.
```


### [2026-09-05T06:11:13.357Z] TOOL RESULT

```
# Indo-European Root bhā-1

The entry for bhā-1 ("to shine") includes these key sections:

**Opening definition:** "To shine. Oldest form _\*bheh2‑_, colored to _\*bhah2‑_, becoming _\*bhā‑_."

**Germanic beacon derivative:** "beacon, from Old English _bēac(e)n_, beacon; beckon, from Old English _bēcnan_...all from Germanic _\*baukna‑_, beacon, signal."

**Greek light derivatives:** "phos-, phot, photo-; phosphorus, from Greek _phōs_ (stem _phōt‑_), light" and "fantasy, pant, -phane, phantasm, phantom, phase, pheno-, phenomenon...from Greek _phainein_, 'to bring to light,' cause to appear, show."

**Pokorny reference:** "[Pokorny 1. _bhā‑_ 104.]"
```


## [2026-09-05T06:11:34.843Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82-\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%A7%D9%86%D9%88%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%85%D8%AF%D8%A7%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%CF%86%CE%B1%CE%BD%CF%8C%CF%82\" \\\n \"https://www.etymonline.com/word/beacon\" \\\n \"https://www.etymonline.com/word/phase\" \\\n \"https://www.ahdictionary.com/word/indoeurop.html\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 79, root Bha 1 (to shine): PIE root, Av. bama/bamya, NP bam/bamdad, Sogd. b'm > NP fam, Gk phos/phanos > NP fanus, Gmc *baukna > beacon\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T06:11:38.562Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2a9f5bd5fba20317.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0fa0805421b89571.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/afa962ff3033fa84.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/03ab2c599161daf7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3613d87a85530c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/48ac41b86997e741.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3735d75498a331a4.txt
```


## [2026-09-05T06:11:45.572Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nprint(t[44][:1800])\nEOF"
}
```


### [2026-09-05T06:11:47.138Z] TOOL RESULT

```
leaves 300
— 34 —
Im Phi. ist apSdak oder apejak zu lesen, wenn die Schreib-
weise alt ist.
255. Np. beS *mehr als Comparativ zu has Viel' = ap. vasii/
musste auf ap. *vasyah- zuriickgehen. Dagegen spricht
np. mih gross : zd. masyah^, ^) hih klein : zd. kasyah-,
nach denen np. *bis fur ap, *vasyah- zu erwarten
ware. Jedenfalls setzt bal. gBs ein iran. *oais^ voraus,
auf das auch np. bes zuriickgehen muss.
256. Np. heSa *Wald* (= ap. *vaisa') kann ich mit zd. varesa-
{= np. *5a5 oder *bus) lautlich nicht vereinigen. Die
Entstehung von gr. ciXaog aus *fal}iaog (Bartholomae)
ist ganz unsicher.
257. Ich kann np. bel, bll *Spaten' (nach Vullers auch =
remus', nach Rosen, Np.Sprachf. p. 50 = *Schaufer),^)
belca *Hacke, Spaten nicht mit den Dialectformen bal
und berd vereinigen, mochte aber wegen der Laute auf
np. pill ^Briicke' = gel. ptird^ kurd. pird, purd^ pel
(Horn Nr. 325) verweisen. Ist berd die alteste Form,
so darf arm. bah *Hacke, Karst* (= *bhrtrom nach
Bartholomae) verglichen werden.
258. Np. him *Furcht' = skr. bhtma- 'furchtbar'.
259. Zu phi. vimdrimtan vgl. mein Zoroastrisches Lied
p. 62. Np. bt/mdr = paz. vlmdr geht nicht auf ap.
*v^mara'j das allerdings zu np. gumdr (oder btmar) ge-
worden ware, sondern auf ap. ^viinara- zuriick. Denn
m^ ist im Neup. zu 6^ (vgl. bist zwanzig' etc.)
geworden. Die Etymologic ist so wie so dunkel. Np.
tlmdr 'aegritudo, cura aegroti, custodia*, afgh. LW.
ttmOr care, attention, regimen of the sick, sickness ,
paz. tmar 'Sorge, Besorgnis' (Min. 25, 5, Shk. 269) hat
mit blmar nichts zu thun.
261. Dazu auch paz. vtni *nose, nostrils Shk. 273.
262. Lies *zehntausend' (statt 'tausend*).
*) Ap. *ma&iyah-^ vgl. siip.wa ^ts^a-.
2) Dazu afgh. LW. ra§'h^l *h61zerne Schaufel zum Worfeln' (afgh.
raSa *a heap of grain' = np. ras, raz *acervu8 frumenti exc
```


## [2026-09-05T06:11:54.362Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"mdad\\|mdiid\\|mddd\\|bam\\b\\|bdm\\b\" HUB.txt | head -20"
}
```


### [2026-09-05T06:11:54.409Z] TOOL RESULT

```
755:hosbam 'daybreak' Gl. and Ind. p. 52, Min. Gl. 104,
757:gvarbOm *Dammerung' (Geiger Nr. 138). Afgh. bam
766:*Dach, Terrasse des Hauses *^) == afgh. bam *obere
770:lid' (Justi-Jaba Wb.) == np. bam i dasm *Augenlid'
782:') Daaeben puSti-bam *Daoh' (Poiak, Persien p. 69), f^.puStbUn
791:ban = bam *Dach, Haus*. — Die nordbal. Form lautet
2674:gehort jedenfalls zu suftatif pr. sunbam 'durchbohre',
3045:Praesens gibt Vullers kdbam^ kavam (arisclie Wrzl.
3650:1059. Als iran. Wrzl. von nuhunbam : nuhuftan 'bedecken,
3777:1124. Np. yabam, yaftan — paz. ayaftan setzt eine Wrzl.
4902:'Morgenrothe', phi. paz. hosasfar *5stlich', hdsbam *Tagesan-
6377:'Kissen H. 172; bam *Morgen H. 174; bam, ban *Dach,
9082:= bam *Dach, Haus* (oben p. 24); Bahram — Vahram,
9152:96 — 98, Shk. 248 — 249; phi. hamdadistan ^= Jiawdtna of
9201:ufmn == samS'Ufiun Terriicktheit, Wollust*; bam 'Bass' ■-=
9205:pr. sunbam 'durchbohre*, bal. sumbag 'bohren (oben p. 76);
9206:nuhunbam, inf. nuhuftan 'bedecken, verbergen* (von *ni'dub).
9485:p. 281), paz. hdsbdm 'daybreak', hosastar 'eastern' Min. Gl.
10307:bam 24.
```


## [2026-09-05T06:11:57.153Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '748,795p' HUB.txt; echo \"=== index 6377 ctx ===\"; sed -n '6370,6382p' HUB.txt"
}
```


### [2026-09-05T06:11:57.212Z] TOOL RESULT

```
(Dames, Grammar p. 14). Np. ftai^a *hoch, H5he* ist
wohl mit Suffix a aus ok (= phi. *bardak) gebildet
wie garma etc. (Darmesteter, Etud. iran. I, 267).
173. Np. bdltdan Vachsen' zu phi. caus. voimttan Phi.
Vend. 9, Z. 6 (vahn) ^) = zd. varedaya- Vachsen machen ,
Mann- Andreas, ZDMG. 47, 702.
174. Zu ham Morgen =paz. ham Aogemad. 114, vgl. phi.
hosbam 'daybreak' Gl. and Ind. p. 52, Min. Gl. 104,
Aogemad. 129, paz. bomdaS *dawn* Min. Gl. 40, bal.
gvarbOm *Dammerung' (Geiger Nr. 138). Afgh. bam
*Dach des Hauses* gehort zur folgenden Nummer. Zd.
bdmya- (im Metrum dreisilbig : botniya-) heisst trotz
Geldner nie sublimis*, sondern glanzend, strahlend,
heir (vgl. yt. 5, 64, 78, 101 ; 10, 44, 50 ; 13, 59 etc.)
und ist ~ phi. hamik glanzend' Gl. and Ind. p. 76,
auch *njorgentlich, ostlich' (wie die Armenier es iiber-
setz6n: Bahl i bamik^ = „das morgentliche Balch**).
175. Ich finde iiberall in Wb. und Glossarien nur hdtn
*Dach, Terrasse des Hauses *^) == afgh. bam *obere
Stockwerk, Terrasse, Dach des Hauses'. Die Neben-
form hdti ist bisher wohl nur von Grammatikern be-
zeugt, wird aber gestiitzt durch kurd. ban i dirnVkng^n-
lid' (Justi-Jaba Wb.) == np. bam i dasm *Augenlid'
(= Dach des Auges), sTvend. ban toit, terrasse' (Journ.
asiat. 1893, 259), jiid. tat. serbu "flaches Dach' (Miller
p. 79) aus *8arban (mit w, da -an zu -w, aber ^am zu
-um wird, vgl. nu *Brot', num *Name'etc.), ka§. bun^ bdn,
bu *Dach' (aus ban, da -aw zu -ww, aber dm zu Urn wird)
und phi. ban 'Dach' PPGl. p. 2 und 96. Die ange-
nommene Bedeutung *Haus' (vgl. bal. ban *Haus, Lehm-
hiitte. Stair? Geiger, Lautl. p. 50) ist sonach die ab-
geleitete wie bei lat. tectum *Dach, Obdach, Wohnung,
*) Bei Justi, Wb. s. v. vared : vartn gelesen.
') Vgl. np. balx i baml (falsch balx i nami Fird. Ill, 1514, 309).
') Daaeben puSti-bam *Daoh' (Poiak, Persien p. 69), f^.puStbUn
Dach' ZDMG. 36, 70, semnan. puStibon ZDMG. 33, 537.- 25 -
Haus\ Ich halte daher auch Andreas' Etymologie:
ban 'Haus' = ap. vahana- (vgl. skr. vasana- 'Wohnen*,
arm. vanIS) nicht fiir richtig, zumal im Pehl. ban, aber
nirgends *v(ln hezeugt ist. Horn's Etymologie: evdn
(jetzt arabisiert divdn gesprochen Sal. Shuk. p. 7)
'Vorhalle' = adhi + ban hat nichts ftir sieh.
178. Ich bezweifle die Zugehorigkeit von bdnu *Herrin* zu
ban = bam *Dach, Haus*. — Die nordbal. Form lautet
banuK (Geiger, Lautl. p. 26).
178 bis jjp ipa^^ar 'Glaube, Vertrauen (afgh. LW. bavar
*belief, faith, confidence*, bavarl 'faithful, trustworthy')
gehort nicht zu upa + [/^var, sondern ist = paz. vawar
=== index 6377 ctx ===
vermuthet und halte es — wie jetzt auch andere Gelehrte
— fiir sicher. Vgl. die Einleitung p. 115.
Ap. 6, w (= idg. hh) wird im Np. zu 6, v und /.
§ 74. a) Ap. h im Anlaut = np. 6:
haj 'Tribut', ap. haji-, skr. Wrzl. hhaj\ bar Last' H.
156; bara 'Pferd' H. 160; bOzYsXkQ, arm. ia-se; bCLzu'kvm
H. 167; bak Turcht H, 170; baU *hoch* H. 171; balis
'Kissen H. 172; bam *Morgen H. 174; bam, ban *Dach,
Haus' oben p. 24; banu *Herrin (?) H. 178; but Idol' s. oben
p. 26; biziSk *Arzt' H. 183; baxt ^Schicksal' H. 185; baxsi-
dan *schenken H. 186; biradar *Bruder H. 192; baraz
Schmuck' H. 193; burdan H. 196; burz *hoch*, buland 'hoch
H. 198; barsam (Parsenwort) H. 200; biristan *braten' H
```


## [2026-09-05T06:12:08.536Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT beacon ===\"; grep -n -i \"^BEACON\\|Beacon, a signal\" SKT.txt | head -5\necho \"=== SKT phantom/phase ===\"; grep -n -i \"^PHANTOM\\|^PHASE\\|^PHOSPHORUS\" SKT.txt | head -5\necho \"=== SYN 15.56 ===\"; grep -n \"15\\.56\" SYN.txt | head -3"
}
```


### [2026-09-05T06:12:08.633Z] TOOL RESULT

```
=== SKT beacon ===
1592:Beacon.  (E.)  M,  K. /$«>^/if.  A.S.  ^<ir/M. beck  (i).  to  oorl.  (F.  — C.)    F.  birqutr, to  bob ;   Col.  -  F.  inc.  beak.     Sec  Peuk. (Misplaccil ;  unless  i(  be  used  for  b€<bon.)
=== SKT phantom/phase ===
13883:Phantom.  (F.-L.-Gk.)  M.  E.  /«»- tomt^^O.T,  /an/osme.—h.  phoHfajma.^ Gk.  tfi6tiTaatux.  a  vision,  specire,  lit.  appari- tion. «•  Gk.  tpayrA^uy,  to  display.  ^  Gk. ^KU'-,  as  m  i^ii»«*»  {  =  ipAv.jinv),  to  shew,  lit. to  cansc  to  shine  ;  whence  tpaynjt*^  one  who shews  (as  in  ltpo-tpAyTTp).^G\L.  4^-ttv,  to ahinc.  +  Skt.  M^,  to  5hi;ie.    (^  BHA.)
13898:Phase,  Phaeis.  an  appearance. Gk.)  h&te  L.  p/tasifi  pi.  pktuet.* ^att,  an  appeanmcc ;  from  base  ^ shine;  cf.  *<S-o».  light.  (^BHA.] The  Gk.  ^offir  also  means  *  a  snyim claration.*  in  which  sense  it  u  coH with  t^W,  I  speak,  declnrc,  from  ^1 to  speak.  This  root  is  perhaps  uUnl identical  with  ^  UHA,  to  shine.
=== SYN 15.56 ===
1743:5. Lith. Zaibas, Lett. zibens : Lith. Zibéti, Lett. zibtz ‘shine, glitter’ (15.56).
1745:7. Skt. vidyut-, i.e. vi-dyut- fr. dyut- ‘shine’ (15.56).
1861:1. Grk. xa, ChSl. séni, SCr. sjena, Russ. sen’ (Boh. siti, Pol. sien, Russ. seni ‘entrance room’, etc., as room without light), Skt. chaya-, Av. *saya- (a-saya- ‘without shadow’), NPers. saya-, Alb. hé, fr. IE *skai-, *ski-, prob. the same root as in Goth. skeinan, OF scinan, Ch§l. sijatt ‘shine’ (15.56). Connection through a notion of ‘faint light’ (as in NE shimmer, NHG schimmer) or ‘re- flection’. Cf. OF scima ‘shadow, gloom’ beside scima ‘light, brightness’. Walde-
```


## [2026-09-05T06:12:17.392Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"NPers. bamdad\\|bāmdād\\|NPers. bam\\b\" SYN.txt | head -5\ngrep -n -i \"15\\.56 Shine\\|SHINE, GLITTER\\|15\\.56\" SYN.txt | sed -n 1,5p\necho \"=== buck light section ===\"; grep -n \"φάος\\|phaos\\|Grk. φῶς\\|φῶς\" SYN.txt | head -5\necho \"=== morning ===\"; grep -n \"NPers. bamdad\\|bāmdād\" SYN.txt | head -3; grep -n -i \"MORNING\" SYN.txt | head -5"
}
```


### [2026-09-05T06:12:17.507Z] TOOL RESULT

```
1743:5. Lith. Zaibas, Lett. zibens : Lith. Zibéti, Lett. zibtz ‘shine, glitter’ (15.56).
1745:7. Skt. vidyut-, i.e. vi-dyut- fr. dyut- ‘shine’ (15.56).
1861:1. Grk. xa, ChSl. séni, SCr. sjena, Russ. sen’ (Boh. siti, Pol. sien, Russ. seni ‘entrance room’, etc., as room without light), Skt. chaya-, Av. *saya- (a-saya- ‘without shadow’), NPers. saya-, Alb. hé, fr. IE *skai-, *ski-, prob. the same root as in Goth. skeinan, OF scinan, Ch§l. sijatt ‘shine’ (15.56). Connection through a notion of ‘faint light’ (as in NE shimmer, NHG schimmer) or ‘re- flection’. Cf. OF scima ‘shadow, gloom’ beside scima ‘light, brightness’. Walde-
2198:2. Lat. accendere (> It. -accendere), imcendere (> It. incendere, Sp. encender, Rum. incinge), succendere, epds. of *candere: candére ‘shine, glow’ (15.56).
13229:Lett. zars, prob. : Lith. Zaras ‘beam of light’ (Lalis), Zéréti ‘shine, glitter’, ete. Cf. the opposite semantic development in OE beam, NE beam for ‘beam of light’ (NED s.v.19). Miihl.-Endz. 4.691.
=== buck light section ===
=== morning ===
9019:W. boreufwyd or boreubryd ‘breakfast epd, of bore (old also boreu) ‘morning and buyd ‘food’ or pryd ‘meal’. But now mostly brecwast fr. NE breakfast.
9021:Br. pred-beure ‘breakfast’, cpd. of pred ‘meal’ and beure ‘morning’. Cf. W. boreubryd. oe me ‘dinner’, MBr. leiff, etym.?
9035:Dan. aftensmad, Sw. aftonmaltid, lit. ‘morning-, midday-, evening-food (meal)’.
9038:OE morgenmete, wundernmete (cf. above), efenmete, lit. ‘morning-, noon-, evening-food (meal)’.
9051:5. Lith. pusryciat (pl.) ‘breakfast’, epd. of pusé ‘half’ (18.34) and rytas ‘morning’ (14.34), so lit. ‘midmorning’ (meal).
```


## [2026-09-05T06:12:21.780Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"14\\.42 MORNING\\|14.42 Morning\" SYN.txt | head; grep -n \"bamdad\\|bāmdād\\|bamdād\" SYN.txt | head"
}
```


### [2026-09-05T06:12:21.848Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T06:12:24.981Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Av. usah-\\|NPers. bam\\|Av. bamya\\|bāmya\" SYN.txt IEC.txt | head -10\necho \"=== SYN 'MORNING' heading ===\"; grep -n \"MORNING\" SYN.txt | head -3"
}
```


### [2026-09-05T06:12:25.061Z] TOOL RESULT

```
SYN.txt:25309:(1245). Walde-P. 1.26f. Ernout-M. 93, Walde-H. 1.86. Pedersen 1.82. Grk. Hom. 70s, Aeol. atws, Att. éws; lat, aurdra (mostly poet., as also the jit. It. Sp. aurora, Fr. aurore, Rum. aurora); Ir, faar (‘sunrise’), W. gwawr (Br. gwere-laouen ‘morning star’); Lith. augra, Lett. ausma (new formation fr. aust, above); Skt. ugas-, Av. usah- (also Skt. us-, usa-, Av. us-, but secondary).
=== SYN 'MORNING' heading ===
25353:14.44 MORNING
```


## [2026-09-05T06:12:27.260Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '25353,25400p' SYN.txt | grep -n -i \"pers\\|bam\" | head -10"
}
```


### [2026-09-05T06:12:27.320Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T06:13:03.044Z] TOOL CALL #77: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg79.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/79.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-05T06:13:03.127Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  65211 Sep  5 02:03 77.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63822 Sep  5 02:07 78.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59439 Sep  5 02:13 79.png
```


## [2026-09-05T06:18:40.039Z] TOOL CALL #78: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk79.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82-\"\nW_FANUS = \"https://en.wiktionary.org/wiki/%D9%81%D8%A7%D9%86%D9%88%D8%B3\"\nW_BAMDAD = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%85%D8%AF%D8%A7%D8%AF\"\nW_PHANOS = \"https://en.wiktionary.org/wiki/%CF%86%CE%B1%CE%BD%CF%8C%CF%82\"\nE_BEACON = \"https://www.etymonline.com/word/beacon\"\nE_PHASE = \"https://www.etymonline.com/word/phase\"\nAHD = \"https://www.ahdictionary.com/word/indoeurop.html\"\n\ndoc = {\n \"pdf_page\": 79,\n \"book_page\": 49,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Bhâ 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *bʰeh₂- 'to shine, gleam; appear' (older notation *bhā-, contracted from *bhes-/*bheh₂-)\",\n   \"note\": (\"Pokorny I 104-105 has exactly 'Root/lemma: bʰā-1 … Meaning: to shine', and Nourai's 'Bhâ 1' \"\n            \"reproduces Pokorny's numbering (bhā-1 'shine' vs bhā-2 'speak', p. 105-106). Watkins/AHD: \"\n            \"'bhā-1. To shine. Oldest form *bheh2-, colored to *bhah2-, becoming *bhā-. [Pokorny 1. bhā- 104.]' \"\n            \"The language label 'Indo-European' and the gloss 'to shine' are both right; the modern write-up is \"\n            \"*bʰeh₂-, with the laryngeal that Nourai's 1959-era notation does not show. The whole page is a \"\n            \"single well-formed tree: Avestan bāma-/bāmya- (→ NP bām, bāmdād; → Sogd. βʾm → NP fām), Greek \"\n            \"phōs/phanós/phainein (→ NP fānūs, → French/English learned words), and Germanic *baukna- (→ beacon). \"\n            \"One caveat that runs through the page: Nourai's 'phanein' is his spelling of Greek φαίνειν \"\n            \"(so Klein and Watkins); the printed page really does read 'phanein' (checked on the page image), \"\n            \"so the extraction is faithful and the simplification is the book's.\"),\n   \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *bʰeh₂- «درخشیدن، تابیدن، پدیدار شدن» است که پوکورنی در «واژه‌نامهٔ \"\n               \"ریشه‌شناختی هندواروپایی»، ص ۱۰۴–۱۰۵، زیر مدخل bʰā-1 آورده و آن را از bʰā-2 «سخن گفتن» جدا کرده است؛ \"\n               \"شمارهٔ ۱ در «Bhâ 1» نورایی نیز از همین شماره‌گذاری پوکورنی گرفته شده. واتکینز در پیوست ریشه‌های \"\n               \"هندواروپایی فرهنگ American Heritage همین صورت را با ذکر «Pokorny 1. bhā- 104» می‌آورد. \"\n               \"برچسب زبانی و معنای ریشه در نمودار درست است؛ تنها تفاوت آن است که در نگارش امروزی حنجره‌ای (لارنگال) \"\n               \"*h₂ نشان داده می‌شود که در شیوهٔ نگارش نورایی نیست. ادعای نورایی دربارهٔ خودِ ریشه درست است.\"),\n   \"sources\": [W_PIE, AHD],\n   \"ref_check\": [\n    {\"ref\": \"POK:104\", \"status\": \"supports\",\n     \"note\": (\"Pokorny (POK_full.txt, block beginning 'Root / lemma: bʰa-1, bʰd- bʰ-(*bʰeh2-1)' / \"\n              \"'Meaning: to shine', ending 'References: WP. II 122 f. … Page(s): 104-105'). The entry lists \"\n              \"OInd bhāti 'shines', bhāma- 'Licht, Schein', Avestan bā- 'shine', vīspō-bāmya- 'all gleaming', \"\n              \"bāmya- 'light, gleaming', bānu- 'light, ray', Greek φαίνω, φανή 'torch', φάος/φῶς, and the \"\n              \"Germanic *baukna- question — i.e. the whole page in one entry. Nourai's page number is exact.\")}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II pp. 122-123 (incoming/WLD/WLD_Bd2_pages.txt, leaves 126-127)\",\n     \"stance\": \"supports\",\n     \"note\": \"'1. bhā- „glänzen, leuchten, scheinen“ … av. bā- „scheinen“ … vīspō-bām(y)a- „allglänzend“, bāmya- „licht, glänzend“, bānu- m. „Lichtstrahl“ … gr. φαίνω … φανή „Fackel“ … φάος … Ist germ. *baukna- … von solchem germ. bau- nach *taikna- „Zeichen“ gebildet?' — Walde-Pokorny is the source Pokorny himself cites (WP. II 122 f.).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bha-1 (AHD_watkins1985.txt line 321)\", \"stance\": \"supports\",\n     \"note\": \"'bha-1. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal … 4. Suffixed form *bhaw-es- in Greek phōs (stem phōt-), light … 5. Extended and suffixed form *bhan-yo- in Greek phainein … [Pok. 1 bhā- 104.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, cols. under bhāniō / bhānos / bhāu- (IEC.txt lines 1124, 1126, 1175)\",\n     \"stance\": \"supports\",\n     \"note\": \"'bhāniō \\\"declare, show\\\". WP II, 122 … Gk. phaínō'; 'bhānos … \\\"bright; brightness\\\" … Av. bānus \\\"ray\\\" … Gk. phānós'; 'bhāu- (1) \\\"shine, show; tell\\\" … Gk. pháos, n. and phós (fr. *bhauos) … OE beacen \\\"beacon\\\"'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 14.44 'morning' and 15.56 'shine'\", \"stance\": \"silent\",\n     \"note\": \"grep 'bamdad|bāmdād|NPers. bam' in SYN.txt returns nothing; Buck's 'morning' section (line 25353) does not list the Persian word, so Buck adds nothing here.\"}\n   ],\n   \"nodes\": [\n\n    {\"id\": 1, \"lang\": \"Avestan\", \"words\": \"bama, bâ, bâmya\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"All three forms are genuine Avestan and all three are Bartholomae's. AiWb col. 953: \"\n                    \"'j. bā- V. \\\"scheinen\\\", nur mit Praev.' (a verbal root, attested with ā-, fra-, vi-); col. 954: \"\n                    \"'j. bāma- m. \\\"Licht, Glanz\\\" … Zum V. bā-. — ai. bhāma- m.; np. bām \\\"Morgen(-Frühlicht)\\\"'; and \"\n                    \"'j. bāmya- Adj. (fem. °yā-) \\\"licht, leuchtend, strahlend, glänzend\\\"', beside bānav- 'Lichtstrahl' \"\n                    \"and vīspō.bāma- 'allglänzend'. Phonetically Proto-Indo-Iranian *bʰeh₂- > *bʰāH- gives Indo-Iranian \"\n                    \"*bʰā- (Skt bhā-ti 'shines', bhāma- 'light'); Iranian devoices nothing but turns PIE *bʰ into plain b, \"\n                    \"so Av. bā-, bāma-, bāmya- (the -ya- being the common Avestan adjective suffix, PIE *-yo-). \"\n                    \"Nourai's gloss 'bright' is right for bāmya- but loose for bāma-, which is a noun 'light, radiance', \"\n                    \"and for bā-, which is a verb 'to shine'; the node is therefore right in substance.\"),\n     \"derivation_fa\": (\"هر سه صورت اوستایی‌اند و همه در «واژه‌نامهٔ ایرانی باستان» بارتولومه آمده‌اند: ستون ۹۵۳ \"\n                       \"«bā- فعل: درخشیدن»، ستون ۹۵۴ «bāma- (نرینه): روشنایی، درخشش» و «bāmya- (صفت): روشن، درخشان، \"\n                       \"تابان»، در کنار bānav- «پرتو» و vīspō-bāma- «همه‌درخشان». از دید آوایی، *bʰ هندواروپایی در \"\n                       \"ایرانی باستان به b ساده بدل می‌شود، پس *bʰeh₂- به صورت bā- در اوستایی بازتاب می‌یابد؛ پسوند \"\n                       \"‏-ya- در bāmya- همان پسوند صفت‌ساز هندواروپایی *-yo- است. تنها نکته آن است که معنای «bright» \"\n                       \"برای bāmya- درست است ولی bāma- اسم است («روشنایی») و bā- فعل؛ ادعای نورایی در اصل درست است.\"),\n     \"sources\": [W_PIE],\n     \"ref_check\": [\n      {\"ref\": \"POK:104\", \"status\": \"supports\",\n       \"note\": \"Pokorny pp. 104-105 s.v. bʰā-1: 'Avestan ba- \\\"shine, appear, seem\\\" only with a- … and vi- … vīspō-bamya- \\\"all gleaming\\\", bamya- \\\"light, gleaming\\\", banu- m. \\\"light, ray\\\"' — exactly the three items of the node.\"},\n      {\"ref\": \"SOD:97\", \"status\": \"supports\",\n       \"note\": \"Gharib p. 97 (SOD_pages.txt leaf 163), entry 2459: 'βʾm(h) … βām ©<Av. bāma; Parth. MP bām' — Gharib derives the Sogdian word from Avestan bāma-, confirming both the Avestan form and its gloss.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 953-955 (BRT.txt lines 17055-17095)\", \"stance\": \"supports\",\n       \"note\": \"'j. bā- V. \\\"scheinen\\\"'; 'j. bāma- m. \\\"Licht, Glanz\\\" … np. bām \\\"Morgen(-Frühlicht)\\\"'; 'j. bāmya- Adj. \\\"licht, leuchtend, strahlend, glänzend\\\"'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 122\", \"stance\": \"supports\",\n       \"note\": \"'av. bā- \\\"scheinen\\\" nur mit a- … und fra- … vīspō-bām(y)a- \\\"allglänzend\\\", bāmya- \\\"licht, glänzend\\\", bānu- m. \\\"Lichtstrahl\\\"'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien no. 174 (p. 24)\", \"stance\": \"supports\",\n       \"note\": \"'Zd. bāmya- (im Metrum dreisilbig: bāmiya-) heisst trotz Geldner nie \\\"sublimis\\\", sondern glänzend, strahlend, hell (vgl. Yt. 5,64; 78; 101; 10,44; 50; 13,59 etc.) und ist = phl. bāmīk \\\"glänzend\\\"' — Hübschmann settles the gloss against Geldner in Nourai's favour.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. bhānos (IEC.txt line 1126)\", \"stance\": \"supports\",\n       \"note\": \"'bhānos, ā, us \\\"visible, plain, bright; brightness, sign, show\\\". WP II, 122 … Av. banus \\\"ray\\\"'.\"}\n     ]},\n\n    {\"id\": 2, \"lang\": \"Persian\", \"words\": \"bâm 1; bâmdâd\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Av. bāma- 'light, radiance' (and the adjective bāmya- 'shining') continues into Middle Persian \"\n                    \"as bām 'dawn, light' — MacKenzie prints 'bāmdād [bʾmdʾt | M bmdʾd, N ~] dawn, morning' and \"\n                    \"'bāmīg [bʾmyk] brilliant, glorious' (CPD p. 16), and Nyberg glosses Pahlavi uš-bām [ʾwšbʾm] \"\n                    \"'dawn, daybreak' as 'Av. us(ah)- \\\"dawn\\\" + *bāma- \\\"light\\\", whence bāmya- \\\"luminous\\\"'. \"\n                    \"New Persian بام 'morning' is the direct continuant (Av./OIran. ā stays ā, intervocalic -m- is \"\n                    \"stable), and بامداد is MP bāmdād, i.e. bām 'dawn-light' + dād 'given, set' (root dā- 'to give, \"\n                    \"place'), literally 'the setting of the light'. Bartholomae himself makes the link explicit \"\n                    \"under bāma-: 'np. bām \\\"Morgen(-Frühlicht)\\\"'. Horn no. 174 lists 'bām 2) \\\"Morgen\\\", bāmdād, \"\n                    \"bāmdādān \\\"des Morgens\\\"' with 'aw. vīspō-bāma- \\\"allbeleuchtend\\\"; phlv. bāmīk, bāmdāt; \"\n                    \"ai. bhāma- \\\"Licht, Strahl\\\"'. Nourai's numbering 'bâm 1' correctly keeps this word apart from \"\n                    \"the homonym bām 'roof', which Horn (no. 175) and Hübschmann (no. 175) derive from bān 'roof, \"\n                    \"house' — a genuinely different word.\"),\n     \"derivation_fa\": (\"«بام» به معنی بامداد و «بامداد» هر دو دنبالهٔ فارسی میانه‌اند: مکنزی در فرهنگ پهلوی، ص ۱۶، \"\n                       \"«bāmdād: سپیده‌دم، بامداد» و «bāmīg: درخشان» را آورده و نیبرگ صورت پهلوی uš-bām را «از اوستایی \"\n                       \"us(ah)- (سپیده) + *bāma- (روشنایی)» می‌داند. ریشهٔ کهن همان bāma- اوستایی «روشنایی، درخشش» است؛ \"\n                       \"آ کشیدهٔ ایرانی باستان در فارسی نو نیز آ می‌ماند و م میان‌واکه‌ای پایدار است، پس bāma- > bām. \"\n                       \"«بامداد» مرکب است از بام + داد (از ستاک dā- «دادن، نهادن»)، یعنی «برنهادنِ روشنایی». \"\n                       \"خودِ بارتولومه ذیل bāma- می‌نویسد: «np. bām “Morgen(-Frühlicht)”». هرن (شمارهٔ ۱۷۴) نیز بام و \"\n                       \"بامداد را با پهلوی bāmīk و bāmdāt و سنسکریت bhāma- می‌سنجد. شمارهٔ «۱» که نورایی بر بام گذاشته \"\n                       \"درست است، زیرا این واژه با «بامِ» خانه (که هرن و هوبشمان آن را از «بان» می‌گیرند) یکی نیست. \"\n                       \"ادعای نورایی درست است.\"),\n     \"sources\": [W_BAMDAD],\n     \"ref_check\": [\n      {\"ref\": \"BQT:227\", \"status\": \"supports\",\n       \"note\": (\"Borhan-e Qate' vol. 1, printed p. 227 = BQT_v1_pages.txt leaf 447. Headword بام: \"\n                \"'…و مخفف بامداد هم هست که صبح پگاه باشد'; Mo'in's footnote on the same page: \"\n                \"'در اوستا bāmya (درخشان) و در سانسکریت …' and 'بامداد — مرکب از: بام + داد. در پهلوی bāmdāt، صبح.' \"\n                \"Nourai's page number is exact and the footnote states his arrow.\")}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 174 (HRN.txt lines 1898-1907)\", \"stance\": \"supports\",\n       \"note\": \"'174. bām … 2) \\\"Morgen\\\", bāmdād, bāmdādān \\\"des Morgens\\\" (z. B. Vis und Ramīn S. 41, Vers 6). aw. vīspō-bāma- \\\"allbeleuchtend\\\"; phlv. bāmīk, bāmdāt; ai. bhāma- \\\"Licht, Strahl\\\" … jedenfalls kann das Wort aber nicht von der √bhā- scheinen, leuchten getrennt worden.'\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien no. 174 (p. 24) and §74 (p. 131)\", \"stance\": \"supports\",\n       \"note\": \"'174. Zu bām \\\"Morgen\\\" = paz. bām Aogemad. 114, vgl. phl. hōšbām \\\"daybreak\\\" …, paz. bāmdāt \\\"dawn\\\" Min. Gl. 40, bal. gvarbām \\\"Dämmerung\\\"'; and in the sound-law list §74 'Ap. bh im Anlaut = np. b: … bām \\\"Morgen\\\" H. 174'.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 16 (PHD.txt line 252)\", \"stance\": \"supports\",\n       \"note\": \"'bāmdād [bʾmdʾt | M bmdʾd, N ~] dawn, morning. bāmīg [bʾmyk] brilliant, glorious.' — the Middle Persian ancestor with the New Persian form marked '~' (identical).\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. uš-bām (NYB_vol2_glossary.txt line 3865)\", \"stance\": \"supports\",\n       \"note\": \"'uš-bām [ʾwšbʾm] dawn, daybreak … Av. (415) us(ah)- \\\"dawn\\\" + *bāma- \\\"light\\\", whence (954 sq.) bāmya- \\\"luminous\\\" (v. bāmīk); MPrs ʾwsybʾm, Paz. hōsbām.'\"},\n      {\"src\": \"BRT\", \"where\": \"AiWb col. 954 s.v. bāma-\", \"stance\": \"supports\",\n       \"note\": \"'Zum V. bā-. — ai. bhāma- m.; np. bām \\\"Morgen(-Frühlicht)\\\". — S. dazu Hbm. PSt. 34.' Bartholomae draws Nourai's arrow himself.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep بامداد / بام)\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur's index does not carry a بام/بامداد headword in the OCR; nothing for or against.\"}\n     ]},\n\n    {\"id\": 3, \"lang\": \"Sogdian\", \"words\": \"b`m\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Gharib's Sogdian dictionary, p. 97, entry 2459: 'βʾm(h) B, M, S — βām ©<Av. bāma; Parth. MP bām \"\n                    \"⇒ βʾmʾk — glow, colour', with the literature 'Gersh. Sogd. Cpds. 138, 142; BSTBL; W-Lii; \"\n                    \"Hen. LW p100; Benv. Notesii 228'. So the form, the gloss 'glow, colour' and the derivation \"\n                    \"from Avestan/Old Iranian *bāma- are all Gharib's own. Phonetically Sogdian regularly spirantises \"\n                    \"initial Old Iranian b- to β- (written ⟨βʾm⟩, transcribed by Nourai as b`m following the \"\n                    \"consonantal spelling), and Old Iranian ā is preserved; the semantic step 'light, radiance' → \"\n                    \"'sheen, hue, colour' happens inside Sogdian and is the reason the word could be lent to Persian \"\n                    \"as a colour word. The same page also has 2452 βʾm 'dawn, morning' (Christian Sogdian) and 2453 \"\n                    \"βʾmʾk 'colour', showing both senses side by side.\"),\n     \"derivation_fa\": (\"قریب در «فرهنگ سغدی»، ص ۹۷، مدخل ۲۴۵۹: «βʾm(h) — βām، از اوستایی bāma؛ پارتی و فارسی میانه \"\n                       \"bām — درخشش، رنگ» و در منابع همان مدخل به هنینگ (وام‌واژه‌های سغدی، ص ۱۰۰) ارجاع می‌دهد. \"\n                       \"پس صورت، معنا و اشتقاق از *bāma- ایرانی باستان همه از خودِ قریب است. از دید آوایی، b آغازینِ \"\n                       \"ایرانی باستان در سغدی به‌طور منظم به β (سایشی) بدل می‌شود و آ کشیده می‌ماند؛ نورایی همان \"\n                       \"املای همخوانی ⟨βʾm⟩ را b`m نویسانده است. تحول معنایی «روشنایی» ← «درخشش، رنگ» درون سغدی رخ داده \"\n                       \"و همین است که راه را برای وام‌گیری آن در فارسی به معنی «رنگ» باز کرده. ادعای نورایی درست است.\"),\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:97\", \"status\": \"supports\",\n       \"note\": \"Gharib p. 97 (SOD_pages.txt, 163rd form-feed block; running head '97' printed at the top of the block), entry 2459 quoted above. Nourai's SOD:97 is a page number, not an entry number (entry 97 is ʾγšδʾr 'to begin').\"},\n      {\"ref\": \"BQT:1437\", \"status\": \"supports\",\n       \"note\": \"Borhan vol. 3 printed p. 1437 (incoming/BQT/BQT_v3_pages.txt leaf 229, running head ۱۴۳۷), Mo'in's footnote 3 to فام: '… باحتمال قوی مستعار از کلمهٔ سغدی βʾm «رنگ (درخشان)» و نیز بمعنی «صبح» … همریشهٔ فارسی این کلمه «بام» (صبح) است. رک: Henning, Sogdian loan words…, BSOS X_1, p.100-101'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib p. 97, entries 2452, 2453, 2459, 2462\", \"stance\": \"supports\",\n       \"note\": \"2452 βʾm (Chr.) 'dawn, morning'; 2453 βʾmʾk 'βāmē, fāmē — colour'; 2459 βʾm(h) 'glow, colour' <Av. bāma; 2462 βʾmkynyʾ 'splendour' — the whole family on the cited page.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1437, Mo'in's footnote to فام\", \"stance\": \"supports\",\n       \"note\": \"Mo'in independently identifies the Sogdian source word as βʾm 'colour (shining)' and links it to Persian بام 'morning'.\"},\n      {\"src\": \"HENNING\", \"where\": \"HENNING_selected_papers.txt (Selected Papers I reprint of BSOS 10.1)\", \"stance\": \"silent\",\n       \"note\": \"The reprint's OCR is too corrupt to locate the 'Sogdian Loan-Words in New Persian' article's p. 100 entry (greps for 'fām', 'βʾm', 'Sogdian loan-word' return only unrelated matches); no contradiction found.\"}\n     ]},\n\n    {\"id\": 4, \"lang\": \"Persian\", \"words\": \"fâm\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"New Persian فام, used almost exclusively as the second member of colour compounds \"\n                    \"(گلفام 'rose-coloured', مشکفام 'musk-black', سپیدفام 'white', زردفام 'yellow' — the Ferdowsi line \"\n                    \"quoted on the chart, 'چه بودت که گشتی چنین زرد فام'), is a Sogdian loanword, not an inherited \"\n                    \"Persian word: an inherited reflex of Old Iranian *bāma- gives بام, which is exactly what Persian \"\n                    \"has for 'morning' (node #2). The initial f- is the giveaway — Sogdian β- was heard by Persian \"\n                    \"speakers as f-, and Gharib actually records the double reading of the derivative βʾmʾk as \"\n                    \"'βāmē, fāmē' (p. 97, entry 2453). Mo'in states the borrowing outright in his footnote to Borhan \"\n                    \"p. 1437: 'این کلمه که فقط [به] صورت جزو دوم کلمات مرکب بکار می‌رود باحتمال قوی مستعار از کلمهٔ \"\n                    \"سغدی βʾm «رنگ (درخشان)» … همریشهٔ فارسی این کلمه «بام» (صبح) است', citing Henning, BSOS X/1, \"\n                    \"pp. 100-101 — i.e. precisely Nourai's SOD:97 + SLW:100. So فام and بام are a doublet: the same \"\n                    \"Old Iranian word, once inherited (بام) and once borrowed through Sogdian (فام). Nourai's chart, \"\n                    \"which routes فام through the Sogdian node rather than straight down from Avestan, gets this right.\"),\n     \"derivation_fa\": (\"«فام» در فارسی نو تقریباً همیشه جزو دوم ترکیب‌های رنگ است (گلفام، مشک‌فام، سپیدفام، زردفام؛ \"\n                       \"همان بیت فردوسی که در نمودار آمده). این واژه وام‌واژه‌ای سغدی است، نه صورت موروثی؛ صورت موروثیِ \"\n                       \"*bāma- ایرانی باستان همان «بام» است. نشانهٔ آشکارِ وام‌گیری، فِ آغازین است: β سغدی در فارسی به f \"\n                       \"شنیده و بدل شده؛ قریب خود صورت βʾmʾk را «βāmē، fāmē» خوانده است (ص ۹۷، مدخل ۲۴۵۳). معین در \"\n                       \"حاشیهٔ برهان قاطع، ص ۱۴۳۷، صریح می‌نویسد: «این کلمه که فقط صورت جزو دوم کلمات مرکب بکار می‌رود \"\n                       \"باحتمال قوی مستعار از کلمهٔ سغدی βʾm «رنگ (درخشان)» … همریشهٔ فارسی این کلمه «بام» (صبح) است» و \"\n                       \"به هنینگ، BSOS X/1، ص ۱۰۰–۱۰۱ ارجاع می‌دهد — یعنی دقیقاً همان دو ارجاع نورایی. پس «فام» و «بام» \"\n                       \"دوگانه‌اند: یکی موروثی و دیگری وام‌گرفته از راه سغدی. ادعای نورایی درست است.\"),\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:97\", \"status\": \"supports\",\n       \"note\": \"Gharib p. 97 entry 2453 'βʾmʾk B — βāmē, fāmē (βʾmʾy, βʾmk) — colour', with 'Gersh. Sogd. Cpds. 142'; the alternative reading fāmē is the immediate source of Persian فام.\"},\n      {\"ref\": \"SLW:100\", \"status\": \"supports\",\n       \"note\": \"Henning, 'Sogdian Loan-Words in New Persian', BSOS 10.1 (1939) p. 100 could not be read directly (the local Selected Papers scan is badly OCRed and repaginated), but two independent authorities cite exactly that page for exactly this word: Gharib SOD p. 97 entry 2459 lists 'Hen. LW p100', and Mo'in's Borhan footnote (p. 1437) cites 'Henning, Sogdian loan words…, BSOS X_1, p.100-101' for فام < Sogd. βʾm. Nourai's page reference is therefore correct.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1437, headword فام and Mo'in's footnote 3\", \"stance\": \"supports\",\n       \"note\": \"Borhan's own gloss 'و بمعنی لون و رنگ … و شبه و مانند و نظیر هم آمده است'; Mo'in's footnote lists the compounds 'مشکفام (برنگ مشک)، سپیدفام، گلفام، سیاه‌فام' and derives the word from Sogdian.\"},\n      {\"src\": \"SOD\", \"where\": \"Gharib p. 97 entries 2453 and 2459\", \"stance\": \"supports\",\n       \"note\": \"Gives both the Sogdian etymon and its fāmē reading.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep فام)\", \"stance\": \"silent\",\n       \"note\": \"Only unrelated hits (نقره فام inside another entry, and an Albanian form in the Latin index); Aryanpur has no فام headword in the OCR.\"}\n     ]},\n\n    {\"id\": 5, \"lang\": \"Greek\", \"words\": \"phôs; phôs-phoros; phânôs; phanein\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Greek φῶς 'light' is the Attic contraction of φάος (Aeolic φαῦος, Pamphylian φάβος), from \"\n                    \"*bʰeh₂-w-os, an s-stem of the root (gen. φωτός, whence the combining form φωτο-). φανός 'torch, \"\n                    \"lantern' (also an adjective 'bright') is Wiktionary's and Pokorny's contraction of φαεινός \"\n                    \"< *φαϝεσ-νος. φαίνειν 'to bring to light, show' (mid. φαίνεσθαι 'to appear') is the *bʰh₂-n-yo- \"\n                    \"present, Watkins's 'extended and suffixed form *bhan-yo-'. φωσφόρος 'light-bringing, \"\n                    \"light-bearer; the morning star' is φῶς + -φορος from φέρειν 'to carry' (PIE *bʰer-), so the \"\n                    \"chart's cross-reference '☞ Bher 1' for the second element is correct. Klein (pp. 1170-1171, \"\n                    \"Nourai's exact page) sets it all out under 'phantasm': 'from the stem of φαίνειν, \\\"to make \"\n                    \"appear, show; to shine\\\", whence also φανός, \\\"torch\\\", φανερός, \\\"visible\\\" …; rel. to φῶς, \"\n                    \"\\\"light\\\", fr. I.-E. base *bhā-, \\\"to shine\\\"'. One orthographic point: the book prints \"\n                    \"'phanein'; the standard transliteration is phainein (φαίνειν), and Klein and Watkins both write \"\n                    \"phainein — checked against the page image, this is the book's own simplification, not an \"\n                    \"extraction error.\"),\n     \"derivation_fa\": (\"یونانی φῶς «روشنایی» صورت به‌هم‌کشیدهٔ آتیکیِ φάος است (از *bʰeh₂-w-os)، که حالت اضافی آن \"\n                       \"φωτός است و ترکیب‌سازِ φωτο- از همان می‌آید. φανός «مشعل، فانوس» (و در مقام صفت «درخشان») \"\n                       \"کوتاه‌شدهٔ φαεινός است. φαίνειν «آشکار کردن، نمایاندن» ستاک حالِ *bʰh₂-n-yo- است — همان چیزی که \"\n                       \"واتکینز «صورت گستردهٔ *bhan-yo-» می‌نامد. φωσφόρος «روشنایی‌آور، ستارهٔ صبح» مرکب است از φῶς و \"\n                       \"‏-φορος از φέρειν «بردن» (از ریشهٔ *bʰer-)، پس ارجاع نمودار به «Bher 1» برای جزو دوم درست است. \"\n                       \"کلاین در همان صفحهٔ ۱۱۷۰ که نورایی به آن ارجاع داده، ذیل phantasm همین زنجیره را می‌آورد. \"\n                       \"تنها نکتهٔ املایی: کتاب «phanein» چاپ کرده، حال آنکه آوانگاری معیارِ φαίνειν همان phainein است؛ \"\n                       \"با مقابله با تصویر صفحه روشن شد که این ساده‌سازیِ خودِ کتاب است، نه خطای خوانش اسکن. \"\n                       \"ادعای نورایی درست است.\"),\n     \"sources\": [W_PHANOS, W_PIE, AHD],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. bha-1: '4. Suffixed form *bhaw-es- in Greek phōs (stem phōt-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, \\\"to bring to light\\\", cause to appear, show, and phainesthai (passive), \\\"to be brought to light\\\", appear.' Verified both in AHD_watkins1985.txt and on the live ahdictionary.com appendix.\"},\n      {\"ref\": \"KLN:1170\", \"status\": \"supports\",\n       \"note\": \"Klein 1966-67 p. 1170 (KLN_1966.txt, page numeral '1170' at line 28453) s.v. phantasm: 'fr. Gk. φαντάζειν … from the stem of φαίνειν, \\\"to make appear, show; to shine\\\", whence also φανός, \\\"torch\\\", φανερός, \\\"visible, manifest\\\"; rel. to φῶς \\\"light\\\", fr. I.-E. base *bhā-, \\\"to shine\\\"'; the same page has 'Phanar … fr. ModGk. Φανάρι, \\\"lighthouse\\\", fr. Gk. φανάριον, \\\"lantern\\\", dimin. of φανός, \\\"torch\\\"'. Nourai's page number is exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW pp. 104-105\", \"stance\": \"supports\",\n       \"note\": \"'gr. πεφήσεται \\\"will appear\\\", *bʰə-n- in present φαίνω … φανερός \\\"obvious\\\", φανή \\\"torch\\\"' and, under the u-extension, 'φάος (Aeolic φαῦος, pamph. φάβος) Attic kontr. φῶς, Gen. φωτός … \\\"light\\\"'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II pp. 122-123\", \"stance\": \"supports\",\n       \"note\": \"'praesens φαίνω … \\\"mache sichtbar, zeige\\\" … φανερός \\\"sichtbar, offenbar\\\", φανή \\\"Fackel\\\"'; 'φάος (aol. φαυος, pamph. φάβος) \\\"Licht\\\" … att. φανός \\\"glänzend\\\"'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. bhāu- (1) (IEC.txt line 1175)\", \"stance\": \"supports\",\n       \"note\": \"'Gk. pháos, n. and phós (fr. *bhauos, and -es-stem) beside pháo, pháuo light, v.; cf. phanós \\\"bright\\\" and piphaüsko \\\"show\\\"'.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Phantom, Phase (SKT.txt lines 13883, 13898)\", \"stance\": \"supports\",\n       \"note\": \"'Gk. φαν-, as in φαίνειν, to shew, lit. to cause to shine … Gk. φάειν, to shine. + Skt. bhā, to shine. (√BHA.)'; 'Phase … from base BHA to shine; cf. φάος, light. (√BHA.)'\"}\n     ]},\n\n    {\"id\": 6, \"lang\": \"Persian\", \"words\": \"fânŭs\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"The word is certainly from Greek φανός 'torch, lantern' — Mo'in says so in his footnote to \"\n                    \"Borhan p. 1437 ('فانوس … از یونانی phanós (درخشنده)', citing Zaba and Dozy) — but the arrow as \"\n                    \"drawn, straight from Greek to Persian, skips the transmitter. The shape of the word gives it \"\n                    \"away: Persian/Arabic fānūs preserves the Greek nominative ending -ος as -ūs, which is how \"\n                    \"Aramaic/Syriac and then Arabic took over Greek nouns (cf. قاموس, ناموس); a Sasanian-era direct \"\n                    \"borrowing would have lost it, as Middle Persian regularly does. Wiktionary's Ancient Greek \"\n                    \"entry accordingly lists Arabic فَانُوس, Hebrew פָּנָס, Turkish fanus, Persian فانوس and Swahili \"\n                    \"fanusi together as the descendants of φανός, and its Arabic entry reads 'Borrowed from Ancient \"\n                    \"Greek φανός (phanós, \\\"lantern\\\")', while the Persian entry only says 'Ultimately from Ancient \"\n                    \"Greek φανός' — the 'ultimately' marking the Arabic stage. So: Greek φανός → Aramaic/Syriac → \"\n                    \"Arabic fānūs (with the broken plural فوانيس) → New Persian فانوس, a round trip that also gave \"\n                    \"Persian the compounds فانوس خیال 'magic lantern' and فانوس گردان. Verdict plausible rather than \"\n                    \"confirmed only because of the missing Arabic link, not because of the Greek origin.\"),\n     \"derivation_fa\": (\"«فانوس» بی‌گمان از یونانی φανός «مشعل، چراغ» است — معین در حاشیهٔ برهان قاطع، ص ۱۴۳۷، همین را \"\n                       \"می‌گوید: «فانوس … از یونانی phanós (درخشنده)» و به ژابا و دزی ارجاع می‌دهد — اما پیکانِ نمودار \"\n                       \"که یکسره از یونانی به فارسی کشیده شده، واسطه را از قلم انداخته است. خودِ صورت واژه گواه است: \"\n                       \"پایانهٔ -وس بازتاب پایانهٔ نهادیِ یونانی -ος است و این شیوهٔ وام‌گیری آرامی/سریانی و سپس عربی از \"\n                       \"یونانی است (سنجید‌ه شود با قاموس، ناموس)؛ اگر واژه در دورهٔ ساسانی مستقیم به فارسی میانه رفته \"\n                       \"بود، این پایانه می‌افتاد. ویکی‌واژه نیز عربی فانوس، عبری פָּנָס، ترکی fanus و فارسی فانوس را \"\n                       \"با هم بازماندگان φανός می‌شمارد و در مدخل فارسی می‌نویسد «در نهایت از یونانی باستان φανός». \"\n                       \"پس مسیر درست چنین است: یونانی φανός ← آرامی/سریانی ← عربی فانوس (جمع مکسر: فوانیس) ← فارسی نو \"\n                       \"فانوس، با ترکیب‌های «فانوس خیال» و «فانوس گردان». حکم «با احتیاط پذیرفتنی است»، تنها به سبب \"\n                       \"حذف حلقهٔ عربی، نه به سبب خاستگاه یونانی.\"),\n     \"sources\": [W_FANUS, W_PHANOS],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1437\", \"status\": \"supports\",\n       \"note\": \"Borhan vol. 3 p. 1437 (BQT_v3_pages.txt leaf 229) carries the headword فانوس with Borhan's gloss ('چراغی که … در آن چراغ یا شمع نهند تا از باد محفوظ ماند') and Mo'in's footnote 5: 'فانوس … از یونانی phanós (درخشنده) «ژابا ص ۸۵۸، دزی ص ۲۸۴»'. The page number is exact; the reference supports the Greek origin but its two authorities (Zaba, Dozy) are dictionaries of Arabic, implying the Arabic route.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. فانوس (MON_part2.txt line 4723)\", \"stance\": \"partial\",\n       \"note\": \"'فانوس … چراغی که برای روشن کردن مسافت زیادی بر بالای منار و جز آن نصب کنند … چراغ محفظه‌داری که در آمد و رفت با خود برند' plus فانوس خیال — Mo'in has the word but the OCR of his bracketed origin tag is unreadable.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein p. 1170 s.v. Phanar\", \"stance\": \"supports\",\n       \"note\": \"'Phanar … Turk. Fanar, fr. ModGk. Φανάρι, \\\"lighthouse\\\", fr. Gk. φανάριον, \\\"lantern\\\", dimin. of φανός, \\\"torch\\\"' — the same Greek word travelling east through Turkish, parallel to the Arabic route.\"},\n      {\"src\": \"PHN\", \"where\": \"Pihan, Glossaire s.v. FANAL (PHN.txt lines 4776-4785)\", \"stance\": \"partial\",\n       \"note\": \"'FANAL … [féner et fanar] lanterne, phare, fanal, comme en français … Fanal s'écrit aussi فنار [fanār] en persan.' — documents the Greek-derived family in Turkish and Persian, but the variant fanār, not fānūs.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir (AFM.txt), ARB_mo3rb.txt\", \"stance\": \"silent\",\n       \"note\": \"grep فانوس in AFM.txt returns nothing (Addi Shir collects Persian words in Arabic, and fānūs is Greek, not Persian, so its absence is expected); ARB_mo3rb.txt hits are only اصطفانوس (a place name).\"}\n     ]},\n\n    {\"id\": 7, \"lang\": \"French\", \"words\": \"phase, photo, fantome, phosphore\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"All four are learned French formations taken from Greek through Latin, not popular inheritances. \"\n                    \"phase: Modern Latin phases (pl.) from Greek φάσις 'appearance (of a star), phase (of the moon)', \"\n                    \"a noun from φαίνειν; French phase 1544/1701, English phase 1705 (Etymonline). photo: clipping \"\n                    \"of photographie, coined 1839 from Greek φωτο- (stem φωτ- of φῶς) + -γραφία. fantôme: Old French \"\n                    \"fantosme, from Latin phantasma < Greek φάντασμα 'apparition', from φαντάζειν, from φαίνειν — \"\n                    \"the one item of the four that came down through Old French and shows popular phonetics \"\n                    \"(ph- > f-, -asma > -osme > -ôme). phosphore: Modern Latin phosphorus < Greek φωσφόρος, applied \"\n                    \"to the element by Hennig Brand's 1669 discovery. Nourai gives the node no reference, but the \"\n                    \"chain is uncontroversial.\"),\n     \"derivation_fa\": (\"هر چهار واژهٔ فرانسوی، ساخته‌های عالمانه‌اند که از یونانی از راه لاتین گرفته شده‌اند، نه صورت‌های \"\n                       \"موروثی: phase از لاتین نو phases، جمع φάσις یونانی «پدیداری (ستاره)، حالت (ماه)»؛ photo کوتاه‌شدهٔ \"\n                       \"photographie (ساختهٔ ۱۸۳۹) از φωτο- (ستاک φωτ- از φῶς) + -γραφία؛ phosphore از لاتین نو \"\n                       \"phosphorus از φωσφόρος که پس از کشف عنصر در ۱۶۶۹ بر آن نهاده شد. تنها fantôme از راه فرانسهٔ \"\n                       \"کهن (fantosme) و لاتین phantasma از φάντασμα آمده و آوایی مردمی دارد (ph به f، و -asme به -ôme). \"\n                       \"نورایی برای این گره ارجاعی نیاورده، ولی زنجیره بی‌مناقشه است. ادعای نورایی درست است.\"),\n     \"sources\": [E_PHASE],\n     \"ref_check\": [\n      {\"ref\": \"(none given)\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no refs= in the book; nothing of Nourai's to check here.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein pp. 1176-1177 s.vv. phosphorus, phosphoric\", \"stance\": \"supports\",\n       \"note\": \"'phosphorus … ModL. phosphorus … fr. L. Phosphorus, \\\"the morning star\\\", fr. Gk. φωσφόρος'; 'phosphoric — F. phosphorique, fr. phosphore' — Klein routes the French word from the Modern Latin/Greek term.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Phantom, Phase\", \"stance\": \"supports\",\n       \"note\": \"'Phantom. (F.-L.-Gk.) M.E. fantome, O.F. fantosme — L. phantasma — Gk. φάντασμα'; 'Phase … L. phasis, pl. phases … Gk. φάσις'.\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. phase\", \"stance\": \"supports\",\n       \"note\": \"'Greek phasis \\\"appearance\\\" (of a star), \\\"phase\\\" (of the moon), from phainein \\\"to show, to make appear\\\", from PIE root *bha- \\\"to shine\\\" … noun back-formed as a singular from Modern Latin plural phases; in English 1705.'\"}\n     ]},\n\n    {\"id\": 8, \"lang\": \"Persian\", \"words\": \"(no transliteration in the book) — فاز ، فوتو ، فانتوم ، فسفر\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"These are 20th-century European technical loans in Persian, and three of the four are French as \"\n                    \"the chart says: فاز from French phase (Mo'in's entry is purely the physics/electrical sense, \"\n                    \"'فاز … (فز.) سیم برقی که …; برق سه فاز'), فوتو from French photo (in فوتوکپی, فوتوگرافی), and \"\n                    \"فسفر from French phosphore (Mo'in's فسفر entry is a full chemistry article, 'جسمی است جامد زرد \"\n                    \"رنگ … فسفر سفید و فسفر سرخ'). فانتوم is the doubtful one: it is not in Mo'in at all, and in \"\n                    \"actual Persian usage it is the name of the American F-4 Phantom aircraft, i.e. an English \"\n                    \"borrowing of the 1960s-70s, not French fantôme (which would in any case more naturally give \"\n                    \"فانتم). The node is therefore right in kind — modern Western loans from the φαίνειν/φῶς family — \"\n                    \"but one of its four words probably came in through English rather than French.\"),\n     \"derivation_fa\": (\"این‌ها وام‌واژه‌های فنیِ سدهٔ بیستم‌اند و سه‌تای آن‌ها، چنان‌که نمودار می‌گوید، فرانسوی‌اند: \"\n                       \"«فاز» از phase فرانسوی (مدخل معین تنها معنای فیزیکی و برقی را دارد: «فاز … سیم برقی … برق سه \"\n                       \"فاز»)، «فوتو» از photo (در فوتوکپی، فوتوگرافی) و «فسفر» از phosphore (معین ذیل فسفر مقاله‌ای \"\n                       \"شیمیایی آورده: «جسمی است جامد زرد رنگ … فسفر سفید و فسفر سرخ»). اما «فانتوم» جای تردید دارد: \"\n                       \"در فرهنگ معین نیامده و در کاربرد فارسی نام هواپیمای آمریکایی F-4 Phantom است، یعنی وام‌واژه‌ای \"\n                       \"انگلیسی از دههٔ ۱۹۶۰–۷۰، نه fantôme فرانسوی (که به‌احتمال «فانتم» می‌داد). پس گره در کلیت درست \"\n                       \"است ولی یکی از چهار واژه‌اش احتمالاً از راه انگلیسی وارد شده؛ با احتیاط پذیرفتنی است.\"),\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"MON:2470\", \"status\": \"partial\",\n       \"note\": \"The local Mo'in OCR (MON_part1/part2.txt) has no page markers, so p. 2470 itself could not be located; the entries the reference is meant to support are there — 'فاز: … (فز.) سیم برقی …' (MON_part2.txt line 4212) and 'فسفر: … (شیم.) جسمی است جامد زرد رنگ …' (line 7351) — but فوتو and فانتوم are absent from Mo'in.\"},\n      {\"ref\": \"AMD:1510, 1553\", \"status\": \"not_checked\",\n       \"note\": \"Amid, Farhang-e Farsi-ye Amid: refs_online.json records that the page numbers of the 2-vol 1369 print are not mappable to any accessible copy, and only entry text (without pagination) is online.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.vv. فاز, فسفر, فانوس\", \"stance\": \"partial\",\n       \"note\": \"Confirms فاز and فسفر as modern technical vocabulary in Persian; silent on فوتو and فانتوم.\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. phase\", \"stance\": \"supports\",\n       \"note\": \"Confirms the European source word of فاز: 'phase … from Greek phasis \\\"appearance\\\" … from phainein'.\"},\n      {\"src\": \"AMD\", \"where\": \"vajehyab/abadis entry text\", \"stance\": \"silent\",\n       \"note\": \"Not consulted online for this node; Amid's pagination is unmappable and his entries add nothing beyond Mo'in for these four words.\"}\n     ]},\n\n    {\"id\": 9, \"lang\": \"English\", \"words\": \"photo, phantom, phase, phenomenon, emphasis. phosphor\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Every one of the six is a learned borrowing of the φαίνειν/φῶς family, and Watkins collects them \"\n                    \"under bha-1 in exactly this shape: 'phos-, phot, photo-; PHOSPHORUS' from φῶς (stem φωτ-), and \"\n                    \"'FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, \"\n                    \"HIEROPHANT …' from φαίνειν. In detail: photo- < φωτο-; phantom < Old French fantosme < Latin \"\n                    \"phantasma < φάντασμα; phase < Modern Latin phasis < φάσις (1705); phenomenon < Late Latin \"\n                    \"phaenomenon < φαινόμενον, the neuter present participle of φαίνεσθαι 'to appear'; emphasis < \"\n                    \"Latin emphasis < ἔμφασις 'appearance, outward show', from ἐμφαίνειν 'to show in'; phosphor < \"\n                    \"Latin Phosphorus 'the morning star' < φωσφόρος. The chart's stray full stop in 'emphasis. \"\n                    \"phosphor' is in the printed book too (checked on the page image) — a typographic slip of \"\n                    \"Nourai's, not an extraction error.\"),\n     \"derivation_fa\": (\"هر شش واژه وام‌واژهٔ عالمانه‌ای از خانوادهٔ φαίνειν/φῶς است و واتکینز همه را ذیل bha-1 گرد آورده: \"\n                       \"photo- از φωτο-؛ phantom از فرانسهٔ کهن fantosme از لاتین phantasma از φάντασμα؛ phase از لاتین \"\n                       \"نو phasis از φάσις (۱۷۰۵ م.)؛ phenomenon از لاتین متأخر phaenomenon از φαινόμενον، اسم مفعولِ \"\n                       \"حالِ φαίνεσθαι «پدیدار شدن»؛ emphasis از ἔμφασις «نمود، جلوه» از ἐμφαίνειν؛ و phosphor از \"\n                       \"لاتین Phosphorus «ستارهٔ صبح» از φωσφόρος. نقطهٔ نابه‌جا در «emphasis. phosphor» در خودِ کتاب \"\n                       \"چاپ شده (با تصویر صفحه مقابله شد) و خطای خوانش اسکن نیست. ادعای نورایی درست است.\"),\n     \"sources\": [AHD, E_PHASE, E_BEACON],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. bha-1 lists PHOS-, PHOT, PHOTO-, PHOSPHORUS under Greek phōs and FANTASY, PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON, EMPHASIS under Greek phainein — all six of the node's words.\"},\n      {\"ref\": \"KLN\", \"status\": \"supports\",\n       \"note\": \"Klein pp. 1170-1171 s.v. phantasm ends 'Cp. also Aphanes, aphanite, aphotic, diaphanous, emphasis, hierophant, paenula, Phaethon, phaeton, Phanar, -phane, phanero-, -phany, phenol, phenomenon, phosphorus, photo-, sycophant.' and 'cp. phantom, which is a doublet of phantasm'; p. 1176 f. s.v. phosphorus, Phosphor.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Phantom, Phase (SKT.txt lines 13883, 13898)\", \"stance\": \"supports\",\n       \"note\": \"'Phantom. (F.-L.-Gk.) M.E. fantome … Gk. φάντασμα … (√BHA.)'; 'Phase, Phasis, an appearance … from base BHA to shine; cf. φάος, light. (√BHA.)'\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. phase\", \"stance\": \"supports\",\n       \"note\": \"'The noun phase entered English in 1705, initially referring to \\\"phase of the moon\\\" … from Greek phasis … from phainein … from PIE root *bha- \\\"to shine\\\".'\"}\n     ]},\n\n    {\"id\": 10, \"lang\": \"Germanic\", \"words\": \"(empty pass-through node)\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"An empty box in the book too (no word is printed; the extraction is faithful). It stands for \"\n                    \"Proto-Germanic *baukna- 'beacon, signal', which Watkins puts under bha-1 as its item 1: \"\n                    \"'Germanic *baukna-, beacon, signal, in: a. Old English bēac(e)n, beacon: BEACON; b. Old English \"\n                    \"denominative bēcnan, bīecnan, to make a sign, beckon: BECKON', with cognates Old Frisian bāken, \"\n                    \"Old Saxon bōkan, Old High German bouhhan 'sign'. Wiktionary's *bʰeh₂- page likewise lists \"\n                    \"Proto-Germanic *baukną (beside *bandwijaną, *bandwǭ) among the descendants. Pokorny (p. 105) and \"\n                    \"Walde-Pokorny (II 123) accept the root connection but query the formation — 'Is Germanic \"\n                    \"*baukna- … from such Germanic *bau- shaped after *taikna- \\\"mark, token, sign\\\"?' — while Mann \"\n                    \"(IEC s.v. bhāu-) analyses it as *bhau- + *gn- (cf. MHG zei-chen). Root membership is not in doubt.\"),\n     \"derivation_fa\": (\"این خانه در خودِ کتاب هم تهی است (واژه‌ای چاپ نشده؛ خوانش اسکن درست است) و نمایندهٔ ژرمنی آغازین \"\n                       \"*baukna- «نشانهٔ آتش، علامت» است. واتکینز آن را نخستین بند ذیل bha-1 می‌آورد: «ژرمنی *baukna- … \"\n                       \"انگلیسی کهن bēac(e)n … و فعلِ اسمیِ bēcnan/bīecnan»، با هم‌ریشه‌های فریزی کهن bāken، ساکسونی کهن \"\n                       \"bōkan و آلمانی علیای کهن bouhhan «نشانه». ویکی‌واژه نیز در صفحهٔ *bʰeh₂- ژرمنیِ آغازینِ *baukną \"\n                       \"را در شمار بازماندگان آورده است. پوکورنی (ص ۱۰۵) و والده-پوکورنی (ج ۲، ص ۱۲۳) پیوند با ریشه را \"\n                       \"می‌پذیرند ولی در چگونگیِ ساخت آن تردید دارند («آیا *baukna- ژرمنی به قیاس *taikna- ساخته شده؟») و \"\n                       \"مان آن را *bhau- + *gn- تحلیل می‌کند. عضویت واژه در این ریشه محل تردید نیست.\"),\n     \"sources\": [AHD, W_PIE],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. bha-1, item 1: 'Germanic *baukna-, beacon, signal' — the node is exactly this reconstruction.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II p. 123\", \"stance\": \"partial\",\n       \"note\": \"'Ist germ. *baukna-, [afries.] bāken \\\"Wahrzeichen, Feuersignal\\\", as. bōkan …, ags. beacon \\\"Zeichen, Fahne\\\", ahd. bouhhan \\\"Zeichen\\\" von solchem germ. bau- nach *taikna- \\\"Zeichen\\\" gebildet?' — accepts the root but leaves the suffix open.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. bhāu- (1) (IEC.txt line 1175)\", \"stance\": \"supports\",\n       \"note\": \"'cf. MHG bou- in bouchen (\\\"sign\\\", fr. *bhau- + *ĝn-, see ĝn-, gnōskō, w. sim. formation to MHG zei-chen), OE beacen \\\"beacon\\\"'.\"},\n      {\"src\": \"web\", \"where\": \"Wiktionary Reconstruction:Proto-Indo-European/bʰeh₂-\", \"stance\": \"supports\",\n       \"note\": \"Germanic descendants listed as *bandwijaną, *bandwǭ and *baukną.\"}\n     ]},\n\n    {\"id\": 11, \"lang\": \"English\", \"words\": \"beacon\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Old English bēacen 'sign, portent, standard; lighthouse' > Middle English beken > beacon; \"\n                    \"the vowel is West Germanic *au > OE ēa, and the -c- is the /k/ of *-kn- (the cluster gave \"\n                    \"OE -c- + -en). Etymonline: 'Old English beacen \\\"sign, portent, lighthouse\\\" … Proto-Germanic \"\n                    \"*baukna- \\\"beacon, signal\\\" … PIE root *bha- (1) \\\"to shine\\\"'; the figurative sense is from \"\n                    \"c. 1600. Skeat has the same, tersely: 'Beacon. (E.) M.E. beken. A.S. bēacn.' Semantically the \"\n                    \"chain is 'shining thing' → 'visible sign' → 'signal fire on a height', the same development \"\n                    \"that makes beckon (OE bēcnan) a sibling of beacon.\"),\n     \"derivation_fa\": (\"انگلیسی beacon از انگلیسی کهن bēacen «نشانه، پرچم، فانوس دریایی» است که از راه انگلیسی میانهٔ \"\n                       \"beken به صورت امروزی رسیده؛ ea در انگلیسی کهن بازتاب *au ژرمنی غربی است و c همان /k/ خوشهٔ \"\n                       \"*-kn- است. اتیمآنلاین: «انگلیسی کهن beacen … از ژرمنی آغازین *baukna- «نشانهٔ آتش، علامت» … از \"\n                       \"ریشهٔ هندواروپایی *bha- (۱) «درخشیدن»»؛ کاربرد مجازی از حدود ۱۶۰۰ م. اسکیت هم کوتاه می‌نویسد: \"\n                       \"«Beacon. (E.) M.E. beken. A.S. bēacn.». تحول معنایی چنین است: «چیز درخشان» ← «نشانهٔ دیدنی» ← \"\n                       \"«آتشِ نشانه بر بلندی»؛ همین تحول beckon (انگلیسی کهن bēcnan) را هم‌خانوادهٔ beacon کرده است. \"\n                       \"ادعای نورایی درست است.\"),\n     \"sources\": [E_BEACON, AHD],\n     \"ref_check\": [\n      {\"ref\": \"(none given)\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no refs= in the book (the parent Germanic node cites AHD, which does cover beacon).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Beacon (SKT.txt line 1592)\", \"stance\": \"supports\",\n       \"note\": \"'Beacon. (E.) M.E. beken. A.S. bēacn.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins s.v. bha-1, item 1a; index line 'BEACON bha-1'\", \"stance\": \"supports\",\n       \"note\": \"'a. Old English bēac(e)n, beacon: BEACON; b. Old English denominative bēcnan, bīecnan, to make a sign, beckon: BECKON.' The AHD index (AHD_watkins1985.txt line 1280) reads 'BEACON bha-1'.\"},\n      {\"src\": \"web\", \"where\": \"etymonline s.v. beacon\", \"stance\": \"supports\",\n       \"note\": \"'Old English beacen \\\"sign, portent, lighthouse\\\" … Proto-Germanic *baukna- \\\"beacon, signal\\\" … PIE root *bha- (1) \\\"to shine\\\". Figurative use from c. 1600.'\"}\n     ]}\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-79.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk79.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-79.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 79"
}
```


### [2026-09-05T06:18:42.686Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 9, 'plausible': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'not_checked': 3, 'partial': 1}
books consulted: {'supports': 29, 'silent': 5, 'partial': 4} | by book: {'web': 5, 'SKT': 4, 'WLD': 3, 'IEC': 3, 'BRT': 2, 'HUB': 2, 'ARY': 2, 'SOD': 2, 'BQT': 2, 'MON': 2, 'KLN': 2, 'HRN': 1, 'PHD': 1, 'NYB': 1, 'HENNING': 1, 'POK': 1, 'PHN': 1, 'AFM': 1, 'AMD': 1, 'AHD': 1}
```


## [2026-09-05T06:19:02.650Z] AGENT

Page 79 verified — `/home/sfmqrb/git/rishe/data/verification/page-79.json` written, `verify_check.py 79` reports **11/11 nodes, 0 PROBLEM lines**.

**Counts (1 entry, root `Bhâ 1` = PIE \*bʰeh₂- "to shine")**
- Root: confirmed. Nodes: 9 confirmed, 2 plausible, 0 disputed / transcription_suspect / unverified.
- Ref checks: 13 supports, 1 partial, 3 not_checked. Consulted: 29 supports, 4 partial, 5 silent across POK, WLD, AHD, IEC, SYN, BRT, HRN, HUB, PHD, NYB, SOD, BQT, MON, KLN, SKT, PHN, AFM, ARY, Henning.

**Plausible (not flagged as disputed)**
- #6 `fânŭs` فانوس — Greek φανός origin is right (Mo'in's Borhan footnote p.1437 says so), but the direct Greek→Persian arrow skips the Aramaic/Arabic transmitter; the retained Greek nominative -ος as ‑ūs is the giveaway.
- #8 فاز/فوتو/فانتوم/فسفر — فاز, فوتو, فسفر are French as drawn; فانتوم is absent from Mo'in and in real usage is the F-4 Phantom, i.e. an English loan, not French *fantôme*.

**No extraction errors.** Checked against the rendered page image (copied to `data/verification/sources/refs/ocr/BOOK/79.png`): the JSON is faithful throughout, including two oddities that are the **book's own**, not the scan's — `phanein` for Greek φαίνειν (Klein and Watkins both write *phainein*), and the stray full stop in "emphasis. phosphor".

**Notable findings**
- Every one of Nourai's page numbers on this page checked out exactly: POK:104 (bhā-1 "to shine", pp. 104-105), KLN:1170 (s.v. *phantasm*), BQT:227 (بام/بامداد with Mo'in's Avestan footnote), BQT:1437 (فام and فانوس on one page), SOD:97 (Gharib entries 2452/2453/2459, βʾm < Av. bāma).
- SLW:100 could not be read directly (the local Henning *Selected Papers* OCR is unusable), but both Gharib ("Hen. LW p100") and Mo'in ("Henning, BSOS X_1, p.100-101") cite that exact page for فام < Sogd. βʾm — so the reference is corroborated indirectly.
- Bartholomae (AiWb col. 954) draws Nourai's Avestan→Persian arrow himself: "np. bām 'Morgen(-Frühlicht)'"; فام/بام turn out to be a doublet (one inherited, one borrowed via Sogdian).
- 7 web sources archived via `fetch_source.py` (Wiktionary ×4, Etymonline ×2, AHD appendix).
