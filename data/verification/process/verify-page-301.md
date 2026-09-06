# Verification process log — verify-page-301


## [2026-09-06T22:49:05.652Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 301 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-301.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-301.json. Write /home/sfmqrb/git/rishe/data/verification/page-301.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 301` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:49:07.183Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:49:07.833Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:49:07.851Z] TOOL RESULT

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


## [2026-09-06T22:49:08.397Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-301.txt"
}
```


### [2026-09-06T22:49:08.417Z] TOOL RESULT

```
1	=== PDF page 301 (book page 271) ===
2	--- entry 0 ---
3	ROOT [Turkish] Lâjîn : name of a Turkish tribe  (refs MON6:1773)
4	#1 (parent #0) [Persian] refs=MON6:1773; KLN:137 | Lâjîn «لاجین» : name of a Turkish tribe ; Lâj-vard «لاجورد ۱» : a city in Turkestan recorded by Marco Polo ☞Kwer ; lâjvard «لاجورد ۲» : lapis lazuli from city of Lâjvard, its blue color | extra: لاژورد، لاجوردین
5	  #2 (parent #1) [Arabic] refs=PLA:240; AFM:141; AHD:737 | al-lâzaward : lapis lazuli
6	    #3 (parent #2) [Latin] refs=KLN; AHD; KGW:108 | lazulum : (stone of) lazuli ; azzurum : the blue color of lapis lazuli | NOTE: The initial "L" was mistaken for the definite article and consequently dropped in some words
7	      #4 (parent #3) [English] refs=AHD; KLN; WEB | lapis lazuli ; azure ; azulene
8	--- entry 1 ---
9	ROOT Lak -> redirect to Lěk
10	--- entry 2 ---
11	ROOT Lakat -> redirect to Lěk
12	--- entry 3 ---
13	ROOT Lakt -> redirect to Lěk
14	--- entry 4 ---
15	ROOT [Indo-European] Lakti, Ljakti : stick, club  (refs WLD2:443)
16	#1 (parent #0) [Avestan] refs=WLD2:443; SYN:525; BRT:1236 | yaxšti, yaxštay : branch, twig ; thri-yaxštay : with three branches
17	  #2 (parent #1) [None] refs=None | 
18	#3 (parent #0) [Sanskrit] refs=WLD2:443 | yaštih : branch, stick
19	  #4 (parent #3) [Hindustani] refs=HJB:510 | lathi : stick, club
20	    #5 (parent #4) [English] refs=KLN:868 | lathi : stick, club
21	
```


## [2026-09-06T22:49:12.514Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-301.json",
 "description": "Read source JSON page 301"
}
```


### [2026-09-06T22:49:12.551Z] TOOL RESULT

```
{
  "pdf_page": 301,
  "book_page": 271,
  "entries": [
    {
      "root": {
        "name": "Lâjîn",
        "lang": "Turkish",
        "refs": "MON6:1773",
        "gloss": "name of a Turkish tribe"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON6:1773; KLN:137",
          "words": [
            {"translit": "Lâjîn", "gloss": "name of a Turkish tribe", "script": "لاجین"},
            {"translit": "Lâj-vard", "gloss": "a city in Turkestan recorded by Marco Polo", "script": "لاجورد ۱", "see": ["Kwer"]},
            {"translit": "lâjvard", "gloss": "lapis lazuli from city of Lâjvard, its blue color", "script": "لاجورد ۲"}
          ],
          "script_extra": "لاژورد، لاجوردین",
          "note": null,
          "quote": {
            "text": "قدرش مروتی است بر این سقف لاجورد ـ فرش رفوگریست بر این فرش باستان",
            "poet": "Khâqânî"
          }
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "PLA:240; AFM:141; AHD:737",
          "words": [
            {"translit": "al-lâzaward", "gloss": "lapis lazuli", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": "KLN; AHD; KGW:108",
          "words": [
            {"translit": "lazulum", "gloss": "(stone of) lazuli", "script": null},
            {"translit": "azzurum", "gloss": "the blue color of lapis lazuli", "script": null}
          ],
          "script_extra": null,
          "note": "The initial \"L\" was mistaken for the definite article and consequently dropped in some words",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD; KLN; WEB",
          "words": [
            {"translit": "lapis lazuli", "gloss": null, "script": null},
            {"translit": "azure", "gloss": null, "script": null},
            {"translit": "azulene", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Lak",
        "redirect": "Lěk"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Lakat",
        "redirect": "Lěk"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Lakt",
        "redirect": "Lěk"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Lakti, Ljakti",
        "lang": "Indo-European",
        "refs": "WLD2:443",
        "gloss": "stick, club"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "WLD2:443; SYN:525; BRT:1236",
          "words": [
            {"translit": "yaxšti, yaxštay", "gloss": "branch, twig", "script": null},
            {"translit": "thri-yaxštay", "gloss": "with three branches", "script": null}
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
          "lang": "Sanskrit",
          "refs": "WLD2:443",
          "words": [
            {"translit": "yaštih", "gloss": "branch, stick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Hindustani",
          "refs": "HJB:510",
          "words": [
            {"translit": "lathi", "gloss": "stick, club", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:868",
          "words": [
            {"translit": "lathi", "gloss": "stick, club", "script": null}
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


## [2026-09-06T22:49:13.125Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:49:13.164Z] TOOL RESULT

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


## [2026-09-06T22:49:42.611Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['MON','KLN','PLA','AFM','AHD','KGW','WEB','WLD','SYN','BRT','HJB','POK','LKT','TTS','IEC','SKT','FSD','LEW','LAT','RCH','AID','SIN','ARY','BQT']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-06T22:49:42.754Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -50; ls /home/sfmqrb/git/rishe/tools/",
 "description": "List verification dir"
}
```


### [2026-09-06T22:49:44.454Z] TOOL RESULT

```
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "covers_etymology": true, "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.", "
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== KGW {"title": "J. Ibrahim, Kulturgeschichtliche Wortforschung: Persisches Lehngut in europäischen Sprachen, Wiesbaden 1991", "edition_found": null, "kind": "google_books_preview", "url": "https://books.google.com/books?id=OUtZZNSUi3cC (partial preview) ; HathiTrust uc1.b3624504 search-only", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": "Google Books limited preview only (index pages).", "notes": "RE-SEARCH 2026-09: preview only (Google Books partial view usable for spot checks); no PDF on the author's site jamshid-ibrahim.net; purchase from Harrassowitz."}
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword bold at line start; e
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online a
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}
== TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books.", "notes": "Open full text (public domain). OCR rough (Fraktur +
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leave
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.", "notes": ""}
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_
== RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 = p.242, leaf 587 = p.494); weakly detected, verify by grepping the page number. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are Persian/Arabic in script (poorly 
== AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in bold at line start; grep -n '^Word'.", "notes": ""}
== SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sections are numbered with plant/product names in caps; grep the Persian/Chinese word or the page number.", "notes": ""}
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
```


### [2026-09-06T22:49:44.489Z] TOOL RESULT

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
```


## [2026-09-06T22:49:47.707Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T22:49:47.748Z] TOOL RESULT

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


## [2026-09-06T22:49:48.915Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-259.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:4000])\n\"",
 "description": "Sample a verified page"
}
```


### [2026-09-06T22:49:50.598Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Kerd 1, Kred",
 "verdict": "confirmed",
 "modern_form": "PIE *ḱḗr, oblique stem *ḱr̥d- (root *ḱerd-) 'heart'; with the compound *ḱred-dʰeh₁- 'to place one's heart, trust'",
 "note": "Pokorny p.579 bottom–580 heads the entry exactly '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’', so Nourai's headword 'Kerd 1, Kred', the language label 'Indo-European' and the gloss 'heart' all reproduce his source correctly; AHD (Watkins) has 'kerd-1. Heart. [Pok. kered- 579.]'. The one substantive caveat concerns the 'kred-' half: Pokorny himself (p.580) says the kred-dhē- 'believe' group is 'nicht hierher' (not to be connected with 'heart'), and Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree; modern standard works (Watkins/AHD, de Vaan 2008 s.v. crēdō, Wiktionary) do connect it, analysing *ḱred-dʰeh₁- as 'to place one's heart'. Nourai therefore follows the newer, now dominant, view — but not the page of Pokorny he cites. The Iranian branch has a further complication that the chart passes over: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, Av. zərəd-, PII *ȷ́ʰā́rd) where *ḱ- is expected, 'unexplained voiced aspiration' (Wiktionary), 'mit init. as if fr. IE gh, due to a blend with some other word' (Buck 251).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *ḱḗr (ستاک غیرفاعلی *ḱr̥d-، ریشهٔ *ḱerd-) به معنی «دل، قلب» است و پوکورنی در ص ۵۷۹–۵۸۰ سرواژه را دقیقاً «kerd-, kērd-, kr̥d-, kred-: Herz» آورده؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ محل بحث بخش kred- است: خودِ پوکورنی در ص ۵۸۰ پیوند kred-dhē- «باور داشتن» را با «دل» رد می‌کند و باک و کلاین و ارنو–مه‌یه نیز همین نظر را دارند، اما واتکینز (AHD)، دِ وان و ویکی‌واژه آن را می‌پذیرند و *ḱred-dʰeh₁- را «دل نهادن» می‌دانند؛ یعنی نورایی از دیدگاه نو پیروی کرده است نه از صفحه‌ای که به آن ارجاع داده. نکتهٔ دیگر آنکه در هندوایرانی به جای *ḱ- انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-، اوستایی zərəd-) که هنوز توضیح قطعی ندارد.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r",
  "https://en.wiktionary.org/wiki/credo%23Latin",
  "https://www.etymonline.com/word/heart"
 ],
 "ref_check": [
  {
   "ref": "POK:579",
   "status": "supports",
   "note": "Pokorny IEW p.579 (bottom) – 580, read in POK_02.txt leaf 239–240 (awk 'BEGIN{RS=\"\\f\"} NR==239'): '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’. Arm. sirt … gr. καρδία (att.), κραδίη (hom.) … lat. cor (aus *cord) … got. hairto, ahd. herza, ags. heorte, anord. hjarta n. ‘Herz’ (*ḱērd-on-)'. Exactly Nourai's root name and gloss."
  },
  {
   "ref": "SYN:251",
   "status": "supports",
   "note": "Buck, Selected Synonyms p.251 = §4.44 HEART (SYN.txt leaf 289, page number '251' printed in the running head above '4.44 HEART'): 'Most of the words for ‘heart’ belong to an inherited group … 1. IE *ḱerd-, etc., with gradation. Walde-P. 1.423 ff. Ernout-M. 219 f.'"
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. kerd-1 (AHD_watkins1985.txt line 621)",
   "stance": "supports",
   "note": "'kerd-1. Heart. 1. Suffixed form *kerd-en- in Germanic *hertōn- in Old English heorte, heart: HEART. 2. Zero-grade form *kr̥d- in: a. Latin cor (stem cord-), heart … b. suffixed form *kr̥d-yā in Greek kardia … 3. Possibly *kred-dhə-, “to place trust” … in Latin crēdere, to believe. [Pok. kered- 579.]' — the whole chart in one entry."
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny I 423 f. (cited by POK and by Buck 4.44; only Band III index available locally, WLD_band3.txt line 2965 'kerd- 423')",
   "stance": "supports",
   "note": "Both Pokorny and Buck refer the 'heart' root to WP. I 423 f.; the local library holds only the Register volume, whose index line points to that page."
  },
  {
   "src": "IEC",
   "where": "Mann, s.vv. Kerd- and Kr̥d- (IEC.txt lines 8676, 9088)",
   "stance": "supports",
   "note": "'Kerd- (Kerdis, ā, io) “heart, core, centre”. Cf. Kr̥d-. WP I, 424' and 'Kr̥d- (Kr̥ds, Kr̥diiom, iio) “core,
```


## [2026-09-06T22:50:00.983Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN lazuli/azure ===\"; grep -n -i \"lazuli\\|lazur\\|azzur\\|^azure\\|lāzaward\\|lazaward\" KLN_1966.txt | head -40\necho \"=== KLN lathi ===\"; grep -n -i \"lathi\" KLN_1966.txt | head -20",
 "description": "Grep Klein for lazuli, azure, lathi"
}
```


### [2026-09-06T22:50:01.056Z] TOOL RESULT

```
=== KLN lazuli/azure ===
4204:azotite,  n.,  salt  of  nitrous  acid  ( chem .)  —  Formed fr.  azote  with  subst.  suff.  -ite. azulene,  n.,  blue  hydrocarbon  (chem.)  —  Formed with  suff.  -ene  fr.  Sp.  azul,  ‘blue’.  See  next  word, azure,  adj.  —  ME.  asur,  fr.  OF.  azur,  fr.  Med. Lat.  azur  a  (whence  also  Ital.  azzurro,  Sp.  azur, azul.  Port,  azul),  fr.  Arab,  al-lazaward,  fr.  Pers. lajwdrd.  Tapis  lazuli’;  so  called  from  Lajward, a  place  in  Turkestan,  mentioned  in  Marco Polo’s  Travels.  The  initial  /  was  mistaken  for  the definite  article  and  consequently  dropped  in  the Romanic  languages.  Cp.  azulene.  Cp.  also lapis  lazuli.
10036:Cyanea,  n.,  a  genus  of  jelly  fishes  ( ichthyoid  — ModL.,  fr.  Gk.  xuaveo?,  ‘dark  blue’,  fr.  xuavo?, ‘the  dark  blue  color'.  See  next  word, cyanic,  adj.,  1)  of  blue  color;  2)  pertaining  to,  or containing,  cyanogen.  —  Formed  with  suff.  -ic fr.  Gk.  xuavop,  ‘dark  blue  enamel,  lapis  lazuli, the  dark  blue  color’,  a  foreign  word  connected with  Hitt.  kuwanna(n)-,  ‘copper,  copperblue;  or¬ namental  stone’.
20738:kiwi,  n.,  a  flightless  bird  of  New  Zealand;  ap¬ teryx.  —  Maori,  of  imitative  origin, klaprothite,  n.,  a  synonym  of  lazulite  (mineral.)  — Named  after  the  German  mineralogist  Martin Heinrich  Klaproth  (1743-1817).  For  the  ending see  subt.  suff.  -ite.
21138:lapis  lazuli,  an  azure  blue  stone.  —  ML.,  fr.  L. lapis,  ‘stone’,  and  gen.  of  ML.  lazulum,  ‘lapis lazuli-,  fr.  Arab,  lazaward.  See  lapidary,  adj., and  azure.
33725:Derivative:  Sapphic,  n.,  a  Sapphic  verse, sapphire,  n.  —  ME.  safir,  saphir,  fr.  OF.  safir  (F. saphir ),  fr.  L.  sapphirus ,  fr.  Gk.  uarrcpeipoi;,  fr. Heb.  sappir,  sapphire;  lapis  lazuli’,  which  some scholars  derive  fr.  OI.  sani-priydm,  ‘sapphire’, lit.  'dear  to  the  planet  Saturn’,  fr.  Sani,  ‘Saturn’, and  priydh,  'dear'.  See  free.  Cp.  zaffer. sapphirine,  adj.,  of  sapphire;  sapphire-like.  —  L. sapphirinus,  fr.  Gk.  oampEupivoi;,  fr.  aden- cpsipo?,  ‘lapis lazuli'.  See  prec.  word.  For  the  end¬ ing  see  adj.  suff.  -ine  (representing  Gk.  -ivop). Derivative;  sapphirine,  n. sapr-,  form  of  sapro-  before  a  vowel, sapremia,  sapraemia,  n.,  a  diseased  condition  in which  putrefying  matter  is  present  in  the  blood (med.)  —  Medical  L.,  coined  by  Matthews  Dun¬ can  in  1880  fr.  Gk.  aotupoc,,  ‘rotten,  putrid’,  and al[vx,  'blood'.  See  sapro-,  hemal  and  1st  -ia. sapro-,  before  a  vowel  sapr-,  combining  form meaning  'putrid'.  —  Gk.  a: cirpo-,  aomp-,  fr. acazpoz,  ‘rotten,  putrid’,  rel.  to  of) 7rctv,  ‘to  rot’. See  sepsis.
40705:ultramarine,  n.,  a  pure  blue  pigment,  orig.  ob¬ tained  from  powdered  lapis  lazuli.  —  Refash¬ ioned  fr.  It.  oltramarino,  ‘from  beyond  the  sea’, fr.  ML.  ultramarinus  (see  ultramarine,  adj.);  so called  because  the  lapis  lazuli  had  to  be  import¬ ed  from  ‘beyond  the  sea’,  i.e.  Asia.
=== KLN lathi ===
21214:lathee,  n.  —  See  lathi.
21216:Derivatives:  lather,  intr.  and  tr.  v.,  to  cover  with lather,  lather-er,  n.,  lather-y,  adj. lather,  n.,  one  who  puts  up  laths.  —  Formed  fr. lath  with  agential  suff.  -er. lathi,  also  lathee,  n.,  a  heavy  wooden  staff  bound with  iron  (India).  —  Hind,  lathi,  fr.  Prakrit  lat- thi,  ‘staff,  stick,  rod,  club’,  which  is  rel.  to  OI. yaftih  of  s.m.,  Avestic  yaxshti-,  ‘branch’, lathyrism,  n.,  a  morbid  condition  caused  by  the use  of  meal  from  the  seeds  of  certain  species  of Lathyrus  ( med .)  —  Formed  from  next  word  with suff.  -ism.
22337:lure,  n.,  a  bait.  —  ME.,  fr.  MF.  hire  (F.  leurre ), ‘lure,  decoy,  bait’,  fr.  OF.  loirre,  fr.  Frankish *lopr,  which  is  rel.  to  MLG.  loder,  OHG,  MHG. luoder,  G.  Luder,  ‘lure,  decoy,  bait;  carrion’, and  to  OE.  Indian,  OS.  lathian,  ON.  lada,  OFris. lathia,  MDu.  laden,  OHG.  ladon,  MHG.,  G. laden,  Goth,  lapon,  ‘to  call,  summon,  invite’, lure,  tr.  and  intr.  v.,  to  allure;  to  entice.  —  F.
```


## [2026-09-06T22:50:03.166Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT yaxsti ===\"; grep -n \"yaxšti\\|yaxsti\\|yaxst\\|jaxšti\" BRT.txt | head -30\necho \"=== HJB lathi ===\"; grep -n -i \"lattee\\|lathi\\|lāṭhī\\|LATTY\" HJB.txt | head -20",
 "description": "Grep Bartholomae and Hobson-Jobson"
}
```


### [2026-09-06T22:50:03.253Z] TOOL RESULT

```
=== BRT yaxsti ===
14655:•  j.  Sri.yaxätay-",  itryaxStay-'*  m.,  Plur. 'drei  Zweige':  yS  paoiryS  bar?sma  frasttn- nata  'tfi^a  pancayaxstlila  .  .  "der  zuerst als  £.  spreitete  drei  Zweige"  und  fünf Zweige  . ."  Y.57. 6;  —  •ti/ca  F.4g.
14718:•  j.  OxyaxStay-  f.:  s.  unter  %ri.yaxstay:
15246:•  j.  panc£a.yax§tay-  m.,  Plur.  'fünf  Zweige' ; yS paoiryB  bansma  fraslinnata  'iryaxstlsca (sd.)  UJsca  Y.57.6.
16985:—  sraostm  . ,  yS  paoirys  'ma  frastn-mata %ryaxstlli!a  panca.yaxltT^a  Aapta.yaxällca nava.yaxitii^a  ox^nosca  mathydi.patti^tä- nasca  Y.5J.6; — yaj  'ma  a^.dräjS yave.- frä^S  .  .  yat  masyS  aBakmät  °ma  N.  70;
18654:•  j.  nava.yaxstay-  m.,Pliu-.  'neun  Zweige': yl}  paoiryS  barpstna  frastinnata  'hryaxs- iJ/ca  (sd.)  . .  'tdfa  Y.57. 6.
29626:j  •  j.  haradräi  Inf  'zu  wachen  über  — ,  Acht Jzu  haben  auf  — ':  'rai  asahe  gaehanqm Y-55-3;  V.7y.39;  —  gae'iäica  tanvasiS  . . niiatahantayaicä  'räica  aiwyaxstraica  Y. 5Äa,  71.  11;  Yt.5.6.
=== HJB lathi ===
2672:Bamboos  are  sometimes  popjularly distinguished  (after  a  native  idiom) as  male  and  female ;  the  latter  em- bracing all  the  common  species  with hollow  stems,  the  former  title  being applied  to  a  certain  kind  (in  fact,  a  sp. of  a  distinct  genus,  Dendrocalamvs 8trtctu8)y  which  has  a  solid  or  nearly solid  core,  and  is  much  used  for bludgeons  (see  LATTEE)  and  spear- shafts.  It  IS  remarkable  that  this popular  distinction  by  sex  was  known to  Obesias  (c.  B.C.  400)  who  says  that the  Indian  reeds  were  divided  into male  and  female,  the  male  having  no ivrepiittriip.
3723:[BLATTY,  adj.  A  coTT.ol'mlayail, •foreign'  (see  BILAYUT).  A  name applied  to  two  pknts  in  S.  India, the  SoMMToJbia  acida,  and  HydroUa zeylanica  (see  Mad.  Admin,  Man.  Gloss. 8.  v.).  In  the  old  records  it  is  applied to  a  kind  of  cloth.  Owen  (JVarmiitw,  i. 349)  iises  Blat  as  a  name  for  the  land- wind  in  Arabia,  of  which  the  origin  is perhaps  the  same.
3724:[1610.— "Blatty,  the  corge  Rs.  060."— Danvers,  LetUrs,  i.  72.]
13117:LATTEE,  s.  A  stick ;  a  bludgeon, often  made  of  the  male  bamboo  (pen- drocalamta  stricttu),  and  sometimes bound  at  short  intervals  with  iron rings,  forming  a  formidable  weapon.
13121:LATTEEAL,  s.  Hind.  Idthlydly  or, more  cumbrously,  Idthitodldy  *  a  dub- man,'  a  hired  rufl^n.  Such  gentry were  not  many  years  ago  entertains in  scores  by  planters  in  some  parts  of Bengal,  to  maintain  by  force  their claims  to  lands  for  sowing  indigo  on.
16380:Platty  Plain,  a  ballad  by  Sir  W. Jones;   in  Life  ana    Worl-x, ed.  1807,  ii.  508. 1804.  —  "Give  orders  that  a  palanquin may  be  made  for  me ;  let  it  be  very  light, with  the  pannels  made  of  canvas  instead  of wood,  and  the  poles  fixed  as  for  a  dooley. Your  Bengally  palanqnina  are  so  heavy that  they  cannot  be  used  out  of  Calcutta. —  Wellington  (to  Major  Shaw),  June  20.
25776:L&th,  Lathi,  5096, 5lOa
25778:Lattee,  510a
25779:Latteeal,Lattaa],5106
```


## [2026-09-06T22:50:17.288Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef leaf_of(path, lineno):\n    txt=open(path,encoding='utf-8',errors='replace').read()\n    lines=txt.split('\\n')\n    upto='\\n'.join(lines[:lineno])\n    return upto.count('\\f')\nfor ln in [4204,21138,21214,21216]:\n    print(ln, 'leaf', leaf_of('KLN_1966.txt',ln))\nEOF",
 "description": "Compute Klein leaf numbers"
}
```


## [2026-09-06T22:50:18.080Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13110,13130p' HJB.txt; echo \"---- LATH ----\"; grep -n \"^LATH\\|^L&TH\\|Lath,\" HJB.txt | head",
 "description": "Read Hobson-Jobson LATTEE entry"
}
```


### [2026-09-06T22:50:19.248Z] TOOL RESULT

```
4204 leaf 84
21138 leaf 465
21214 leaf 466
21216 leaf 466
```


### [2026-09-06T22:50:19.303Z] TOOL RESULT

```
[1861-62. —  "  The    pillar   (at   Besarh)    is known  by  the  people  as  Bhlm-Sen-lA-Uit  and Bkhn-Sen-ha-aamd."  —  Cunningham,    Arch. I  Rep.  i.  61.]    '      '
LATE  RITE.
510
LAW-OFFICER,
LATEBITE,  s.  A  term,  firat  used by  Dr.  Francis  BucbAnan,  to  indicate a  reddish  brick-like  argillaceous  forma- tion much  impregnated  with  iron peroxide,  and  hardeniiur  on  exposure to  the  atmosphere,  which  is  found  in places  all  over  South  India  from  one coast  to  the  other,  and  the  origin  of which  geologists  find  very  obscure.  It is  found  in  two  distinct  t^es  :  viz. (1^  Hiah-level  LcUeritej  capping  especi- ally the  trap-rocks  of  tne  Deccan, vMi  a  bed  from  30  or  40  to  200  feet in  thickness,  which  perhaps  at  one time  extended  over  the  greater  part  of Peninsular  India.  This  is  founa  as  far north  as  the  Bajmahal  and  Monghyr hills.  (2).  Louf-Uvel  Laterite,  form- ing comparatively  thin  and  sloping bwis  on  the  plains  of  the  coast.  The origin  of  both  is  re^irded  as  being,  in the  most  probable  view,  modified  vol- canic matter ;  the  low-level  laterite having  undergone  a  further  rearrange- ment and  deposition ;  but  the  matter is  too  complex  for  brief  statement  (see Netoboldy  m  J,R,A,S.^  vol.  viii. ;  and the  Manual  of  the  GeoL  oflfidia^m.  xlv. 'Seqq.j  348  seqq.),  Mr.  King  ana  others liave  found  flint  weapons  in  the  low- level  formation.  Laterite  is  the  usual material  for  road-metal  in  S.  India, iis  knnknr  (q-v.)  is  in  the  north.  In Ceylon  it  is  called  cabook  (q.v.).
1800. — "  It  is  diffused  in  immense  masses, without  any  appearance  of  stratification, and  is  placed  over  the  granite  that  forms the  basis  of  MtUaycUa,  ...  It  very  soon becomes  as  hard  as  brick,  and  resists  the air  and  water  much  better  than  any  brick I  have  seen  in  India. . .  .  .  As  it  is  usually cut  into  the  form  of  bricks  for  building,  in several  of  the  native  dialects  it  is  called  the brick-stone  (IticaeulUe)  rt/LolBkY^.  vetttttal]. .  •  .  The  most  proper  Enjglisn  name  would be  Laterite,  from  jLattritUf  the  appellation that  may  be  given  it  in  science." — Buchanan^ ifyiore,  Ac.,  li.  440-441.
I860.— "Natives  resident  in  these  locali- ties (Oalle  and  Colombo)  are  easily  recognis- able elsewhere  by  the  general  hue  of  Uieir dress.  This  is  occasioned  by  the  prevalence along  the  western  coast  of  latsnte,  or,  as the  Singhalese  call  it,  cabook,  a  product  of disintegrated  gneiss,  which  being  subjected to  detrition  communicates  its  hue  to  the soil."— TViiium/'*  Ceylon^  i.  17.
LATTEE,  s.  A  stick ;  a  bludgeon, often  made  of  the  male  bamboo  (pen- drocalamta  stricttu),  and  sometimes bound  at  short  intervals  with  iron rings,  forming  a  formidable  weapon.
The  word  is  Hind,  l^tki  and  latht^  Mahr. laththa.  This  is  from  Prakrit  latthly for  Skt.  yaskti^  *a  stick,'  according'  to the  Prakrit '  grammar  of  Vavaruchi (ed.  Coiodly  ii.  32);  see  also  Lanm^ Inditutionu,  Ling.  Praknt,  195.  Jtj^ Idthi^  us  la  hhatngy  is  a  Hind,  proverb (cuj'iis  baculum  eQut  bubalus\  equivalent to  the  "good  old  rule,  the  simple plan."
1880. — "  The  natives  use  a  very  dangenras weapon,  which  they  have  been  forbidden by  Government  to  carry.  I  took  one  as  a curiosity,  which  had  been  seised  on  a  man in  a  fight  in  a  village.  It  is  a  very  heavy Iftthi,  a  solid  male  oamboo,  5  feet  5  indies long,  headed  with  iron  in  a  most  formidable manner.  There  are  6  jagged  semicircolar irons  at  the  top,  each  2  inches  in  length, 1  in  height,  and  it  is  shod  with  iron  bands 16  inches  deep  from  the  top,"— ^Vanderirngt of  a  PUgrim,  1. 133.
1878. — "After  driving  some  6  miles,  we came  upon  about  100  men  seated  in  rows on  the  roadside,  all  with  lattlM."- ZA/e  ta tJu  Mo/ussa,  i.  114.
LATTEEAL,  s.  Hind.  Idthlydly  or, more  cumbrously,  Idthitodldy  *  a  dub- man,'  a  hired  rufl^n.  Such  gentry were  not  many  years  ago  entertains in  scores  by  planters  in  some  parts  of Bengal,  to  maintain  by  force  their claims  to  lands  for  sowing  indigo  on.
1878.— "Doubtless  there  were  hired  lat- tials  ...  on  both  sides."— Life  in,  the Mofum/f  ii.  6.
LAW-OFFIOEB.  This  was  the official  designation  of  a  Mahommedan officer  learned  in  the  (Mahommedan) law,  who  was  for  many  years  of  our Indian  administration  an  essential functionary  of  the  judges'  Courts  in  the districts,  as  well  as  of  the  Sudder  or Courts  of  Review  at  the  Presidency.
It  is  to  be  remembered  that  the  law administered  in  Courts  under  the  Com- pany's  government,  from  the  assump- tion of  the  Dewanny  of  Beiu^al,  Bahar, and  Orissa,  was  the  Mahommedan law ;  at  first  by  the  hands  of  native Oazeefl  and  Mufties,  with  some  super- intendence from  the  higher  European servants  of  the  Company ;  a  superin- tendence which,  wnile  undergoing sundry  vicissitudes  of  system  during the  next  30  years,  developed  gradually into  a  European  judiciary,  which  again was  set  on  an  extended  and  quasi-per- manent footing  by  Lord  ComwaUis'fl Qovemment)  in  I^gulation  IX  of  1793
LAW-OFFICER,
511
LAW-OFFICER.
(see  ADAWLUT).  The  Mahoinmedan law  Gontmued,  however,  to  be  the professed  basis  of  criminal  juris- prudence, though  modified  more  and more,  as  years  went  on,  by  new  Begn- lations,  and  by  the  recorded  construc- tions and  circular  orders  of  the  superior Courts,  until  the  accomplishment  of the  ffteaX,  changes  which  followed  the Mutiny,  and  the  assumption  of  the •direct  government  of  India  by  the €rown  (1868).  The  landmarks  of •cliakige  were  (a)  the  enactment  of  the Penal  Code  (Act  XLV.  of  1860),  and (6)  that  of  the  Code  of  Criminal  Pro- cedure rAct.  XXV.  of  1861X  foUowed by  (c)  the  establishment  of  the  High Court  (July  1,  1862),  in  which  be- came merged  both  the  Supreme  Court with  its  peculiar  jurisdiction,  and  the
Suondam-Company's)  Sudder  Courts Review  and  Appeal,  civil  and •criminal  (Dewanny  Adawlvt,  and Nizamat  Adawlut).
Hie  authoritative  exposition  of  the Mahommedan  Law,  in  aid  and  guid- .ance  of  the  English  judges,  was  the function  of  the  Mahommedan.  Law- oiftcer.  He  sat  with  the  judge  on  the bench  at  Sessions,  i.e.  in  the  hearing of  criminal  cases  committed  by  the magistrate  for  trial ;  and  at  the  end •of  the  trial  he  gave  in  his  written record  of  the  proceedings  with  his Futwa  (q.y.)  (see  Regn.  IX.  1793, .sect.  47),  wnich  was  his  judgment .as  to  tne  guilt  of  the  £u»;u£ed,  as  to the  definition  of  the  crime,  and  as  to its  appropriate  punishment  according to  Mahommedan  Law.  The  indg^ was  bound  attentively  to  consider  the JuttM^  and  if  it  seemed  to  him  to  be consonant  with  natural  justice,  and alao  in  conformity  with  the  Mahom- medan Law,  he  passed  sentence  (save in  certain  excepted  cases)  in  its  terms, And  issued  his  warrant  to  the  magis- trate for  execution  of  the  sentence, tinlesB  it  were  one  of  death,  in  which case  the  proceedings  had  to  be  referred to  the  Sudder  Nizamut  for  confirma- tion. In  cases  also  where  there  was disagreement  between  the  civilian judge  and  the  Law-ofiicer,  either  as  to finding  or  sentence,  the  matter  was referred  to  the  Sudder  Court  for  ulti- mate decision.
---- LATH ----
```


## [2026-09-06T22:50:31.167Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (83,84,85,465,466,467):\n    L=leaves[i]\n    print('=== leaf',i,'len',len(L))\n    print(repr(L[:300]))\n    print('...')\n    print(repr(L[-300:]))\nEOF",
 "description": "Print Klein leaf edges for page numbers"
}
```


### [2026-09-06T22:50:33.122Z] TOOL RESULT

```
=== leaf 83 len 11962
'd  intr.  v.  —  OE.  awsecnan,  fr.  a- ‘on’,  and  wsecnan,  ‘to  waken’.  See  waken. Derivatives:  awaken-er,  n.,  awaken-ing,  adj.  and n.,  awaken-ing-ly,  adv.\n135\naward,  tr.  v.  —  AF.  awarder,  formed  —  with change  of  prefix  —  fr.  ONF.  eswarder,  which corresponds  to  OF.  esg'
...
'it.  ‘without  life’; coined  by  the  French  chemist  Antoine-Laurent de  Lavoisier  (1743-94)  in  I77<J  ft-  priv.  pref.  a- and  Gk.  Ttor,,  ‘life’  (see  zoo-  and  cp.  azoic);  so called  by  him  because  this  element  is  incapable of  supporting  life.\nDerivatives:  azot-ic,  adj.,  a'
=== leaf 84 len 11370
'zorite  (q.v.),  azot-ize , tr.  v.\nazote,  n.,  a  whip.  —  Sp.,  fr.  Arab,  as-saut,  lit., ‘the  whip’,  fr.  as-,  assimilated  form  of  al-,  ‘the’, and  saut,  ‘whip’,  which  is  rel.  to  Heb.  shot, Aram,  shotd,  Syr.  shutd,  Ethiop.  saut,  ‘whip’, Heb.  shuts  ‘to  rove  about’,  Akk'
...
'asin.\nback  formation  (philol.)  —  Coined  by  the  English lexicographer  and  linguist  Dr.  (later,  Sir  James) Murray  (1837-1915).\nbackgammon,  n.  —  Prop,  a  game,  in  which  the pieces  are  put  back ;  compounded  of  back,  ‘the hinder  part  of  the  body’,  and  gammon,  ‘game’, ba'
=== leaf 85 len 11450
'cksheesh,  backshish.  —  Variants  of  baksheesh, backward,  backwards,  adv.  —  Formed  fr.  back, adv.  (see  back,  ‘the  hinder  part  of  the  body’), and  -ward,  resp.  -wards.\nDerivative:  backward,  adj. backwardation,  n.,  postponement  of  delivery ( London  Stock  Exchange).  —  A  hy'
...
're,  ‘to  gape,  yawn’.  Cp.  OProv- eng.  badalhar,  It.  badigliare,  sbadigliare,  ‘to\nyawn’,  which  also  derive  fr.  VL.  bataeulare,  and see  bay,  ‘part  in  the  wall’, bain-marie,  n.  double  pan  for  holding  food.  — F.,  ‘water  bath’,  fr.  ML.  balneum  Mariae,  lit. ‘bath  of  Ma'
=== leaf 465 len 11987
'adj.,  and  verbal  suff. -ate.\nDerivatives:  lapidat-ion,  n.,  lapidat-or,  n. lapidification,  n.,  the  state  of  being  converted  into stone.  —  See  next  word  and  -ation. lapidify,  tr.  v.,  to  convert  into  stone;  intr.  v.,  to  be converted  into  stone.  —  F.  lapidifier,  fr.  '
...
"flattery’,  laskrudu,  ‘loving dainties',  Czech  and  Slovak  laska,  ‘love’,  Pol. laska,  ‘favor’,  OIr.  lainn  (for  *las-nis),  ‘greedy’, Goth,  lustus,  OE.  lust,  ‘lust’.  Cp.  list,  ‘to  please’, lust.  Cp.  also  lares,  larva.\nDerivatives:  lascivious-Iy ,  adv.,  lascivious-ness, n.\nla"
=== leaf 466 len 11622
'ser,  n.  —  Coined  from  the  initials  of  Light  Am¬ plification  (by)  Stimulated  Emission  (of)  Radia¬ tion.\nlash,  tr.  v.,  to  bind.  —  ME.  lasshen,  ‘to  lace’,  fr.\nMF.  lachier,  lacier,  fr.  OF.  See  lace,  v. lash,  adj.,  soft  and  watery.  —  OF.  lasche  (F. lache),  ‘loose’,'
...
'eir  rank  ( Roman  antiq.)  —  L.  Idti- cldvus,  ‘a  broad  purple  stripe  (on  the  tunic)’.  See latitude  and  clavicle.\nlatifundium,  n.,  a  large  landed  estate.  —  L.,  com¬ pounded  of  latus,  ‘broad’,  uni  fundus,  ‘bottom, foundation,  estate’.  See  latitude  and  fund.\nLatin,  adj'
=== leaf 467 len 12176
'.  —  ME.,  fr.  L.  Latinus,  ’Latin’,  prop, ‘pertaining  to  Latium’,  fr.  Latium,  name  of  a district  of  Italy  in  which  Rome  was  situated.  Ac¬ cording  to  P.P.  Persson  Latium  stands  for  *stll- t-iorti  and  lit.  means  ‘the  flat  or  plain  land’  (in contradistinction  to  th'
...
"he  laurustine.  —  See  prec.  word, lautarite,  n.,  calcium  iodate  (mineral)  —  G.  Lau- tarit, named  after  the  Oficina  Lautaro  inChile.The ending  -it  goes  back  to  Gk.  -irr,z ;  see  subst. suff.  -ite.\nlava,  n.  —  It.,  orig.  ‘torrent,  stream',  fr.  Neapoli¬ tan  lave,  fr.  L"
```


## [2026-09-06T22:50:41.831Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in range(460,472):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', leaves[i])\n    print(i, nums)\nfor i in range(80,90):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', leaves[i])\n    print(i, nums)\nEOF",
 "description": "Find printed page numbers in Klein leaves"
}
```


### [2026-09-06T22:50:43.437Z] TOOL RESULT

```
460 ['857']
461 ['858', '859']
462 ['860', '861']
463 ['862', '863']
464 ['864', '865']
465 ['866', '867']
466 ['868']
467 ['869', '870']
468 ['871', '872', '873']
469 ['874']
470 ['875', '876']
471 []
80 ['130', '131']
81 ['132', '133']
82 ['134']
83 ['135', '136', '137']
84 []
85 ['140', '141']
86 ['142', '143']
87 ['144', '145']
88 ['146']
89 ['148', '149']
```


## [2026-09-06T22:51:03.785Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nL=leaves[83]\nfor m in re.finditer(r'(?m)^\\s*(\\d{2,4})\\s*$', L):\n    print(m.group(1), m.start(), 'ctx:', repr(L[max(0,m.start()-120):m.start()+120]))\nprint('LEN', len(L))\nEOF",
 "description": "Locate page numbers within Klein leaf 83"
}
```


### [2026-09-06T22:51:05.483Z] TOOL RESULT

```
135 169 ctx: 'nd  wsecnan,  ‘to  waken’.  See  waken. Derivatives:  awaken-er,  n.,  awaken-ing,  adj.  and n.,  awaken-ing-ly,  adv.\n135\naward,  tr.  v.  —  AF.  awarder,  formed  —  with change  of  prefix  —  fr.  ONF.  eswarder,  which corresponds  t'
136 6158 ctx: 'ter,  n.,  name  of  a  kind  of  carpet.  — Named  after  Axminster,  England,  where  it  was orig.  made.\naxo-\nazyme\n136\n137\naxo-,  before  a  vowel  ax-,  combining  form  mean¬ ing  ‘axis’.  —  Gk.  ai;-,  fr.  a^cov,  ‘axis,  axle’. S'
137 6162 ctx: '  n.,  name  of  a  kind  of  carpet.  — Named  after  Axminster,  England,  where  it  was orig.  made.\naxo-\nazyme\n136\n137\naxo-,  before  a  vowel  ax-,  combining  form  mean¬ ing  ‘axis’.  —  Gk.  ai;-,  fr.  a^cov,  ‘axis,  axle’. See  '
LEN 11962
```


## [2026-09-06T22:51:19.936Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nimport re\ntxt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint('n leaves',len(pages))\n# find the page tagged 443\nfor i,p in enumerate(pages):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if i<3: print(i, repr(p[:200]))\nEOF\ngrep -n \"yaxšti\\|yaxsti\\|yaští\\|yasti\\|laktí\\|lakti\\|ljakti\" WLD_Bd2_pages.txt | head -30",
 "description": "Explore WLD Bd2 pages file"
}
```


### [2026-09-06T22:51:21.728Z] TOOL RESULT

```
n leaves 725
0 ''
1 ''
2 ''
29464:   ai.   yasti-h „Stab,           Stock'^     (av.yaxMi- „Zweig“), pali yatthi und latthi^
```


## [2026-09-06T22:51:25.056Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '29430,29500p' WLD_Bd2_pages.txt",
 "description": "Read WLD Bd2 context around yasti"
}
```


### [2026-09-06T22:51:25.107Z] TOOL RESULT

```
die Yerbreitung des Wortes in alien nord. Sprachen schon in alten Quellen
und seine Yerwendung in vielfach konkreten Bedeutungsverzweigungen, die
gar nicht auf Entlehnung hinzudeuten scheinen; vgl. femer anord. lurlcr
als Beiname, norw. lurk „schwerfalliger, plumper Mensch'‘, schwed. lurk
„Tolper‘ (Bed. wie dt. Bengel)^ ags. Lure als Mannername, nach Torp aaO.
auch tirol. lorgk, lorh „mythischer Riese“,
   Liden Arm. St. 62 f. vermutet als Gdbed. des kelt.-germ. Wortes „ge-
glattetes Stiick Holz“, so dafi zu Herg- „glatt“                         (s. d.).



Ins „Laus‘*          {Idiisl Ijii-sT).

   Aisl. lus,        PI. „Laus“, ags, lus^ PI. lys f., ahd. lus, nhd. Laus\
                           lyss     f.

ncymr.       llet<€n    (acymr. leu-esicc „von- Lausen zerfressen"), pi. llau^
                        „Laus''
acorn, lowen^ ncorn. Zwa«, PL loiv^ bret. laouen (kelt. Gdf. lous^ irrig Peder-
sen KG. I 305). Pick II* 256; Palk-Torp u. lus mit Ubersicht der ver-
suchten (durchweg unbefriedigenden) Wzankniipfungen.            Schulze SBAk.
Berlin 1912, 581 vergleicht unter einem Anlaute Ij- auch ai. yu-kd, pali
/Z-Z:a   =
       prakr. ad, lit. w-ZJ, slav. v^’§^ ,,Laus“; vgl. dieselbe noch der Be-
statigung bediirftige lautliche Annahme unter Hdmo-^ Ijakti^                                   unan-
nehmbar Maring Pad. Anz. 1911 Kr, 12 (11) (warum lit. jeknos                        :   lit.   loma^
slav. jama lit. u-U, slav. vz-si mit so verschiedener Entw. ?).
                 :




l(j)akti- „Stab“.
   Schulze      SBAk. Berlin 1912, 581              vereinigt unter einem solchen Anlaute
   ai.   yasti-h „Stab,           Stock'^     (av.yaxMi- „Zweig“), pali yatthi und latthi^
prakr. lafthi          und slav.         osih (pshm „stimulus“), das dann von ak- jjScharf^
zu trennen ware ; ?,           s.    u. lus   „Laus“.
                                                         s.

sa-, sa- „satt; sattigen^'.
     Ai. asi-n-vd-, dsinvan „uner8attlich“                     (sefczfc   ein Praes. *s9-neti-mi^ ^3-
nu-6 voraus);
  gr. dexai „8attigt 8ich“ (Hesiod; ^so-io)^ djusvai (Horn.) „sich satfcigea**^
(entweder als *de/ievai inf. praes. zu aezatj oder inf. des Wzaorists mit ver-
schleppter Hochstufe der Wz, oder mefrischer Dehnung fiir *dju€vai^                                 s.   Solm-
sea Unters. 93 f.), aor.               atyai „satfcigen“      und „satt werdea“,           fut. doeiv        usw.,
€(o/iev          (^fjojUEV^    Konj. Aor.; jon.        Form gegeniiber den vorgenannten mit
aol. d),          dialog      {^n-Sd-tos)   „iinersattlich“,    lakon.     dddd'     ivdeia^     ddrjv       (iiber
c/

abrjv H. 5, 203   Schulze Qu. ep. 452, Solmsen Unters. 93 Anm. 4)
                              s.                                         boot.
dddv „bi3 zur Sattigung, genug“ (Akk, des auch in lak. d-ctdd sfeeckendeii
add „Sattigung“);            „sich iibersatt essend; zehrend*^, aol. daa, jon.
dori „Ubersattigung, UberdruB, Kummer"^ (nach Solmsen Beitr. 242 f. aus
^sj~sa mit Formans -sa und analogischer Bewahrung des zwischenvokalischen
o nach             dm-oa, dox-oa),          wo von jon. dodojaai „bin satt,           ekie     mich% dodco
^iibersattige^, aodQog (Sappho), doiqQog (Hrdt.) „verachtlich;                             Ekel erregeud"';
     lat.                                               s. Lit. bei Yf. LEWb.^ 680,
                 satis „genug‘‘ (ursprl. subst. „Sattigung’‘,
Osthoflf          MU. 6, 240 f., 251, aber nach Brugmann IF. 27, 251 wohl fiber die
Mittelstufe adjektivischer                  Yerwendung adverbiell            ei’starrt;    sat   kann dann
als    "^sati       das Neutrum des adjektivisch gewordenen satis                           sein,   auf       dem
auch der Komp. sutius und sd{i)tietdSj syllabisch dissimiliert satids „Safetigung,
hinreichende Menge, UberdruB^^ beruhen.
  satur „satt“ (ro-Erweiterung eines i^-St., vgl.                         lit.   solds);
     air. sdiih „Sattheit‘'; saithech „satt'";

     got. d. sg. sopa (noin. "^sop n. oder "^sops m.) „Sattigung''                         wo von gasdpjan
„sattigen^‘ == ags. gesMan ds. got. saps^ anord. sadr, as. sad, ahd. sat „satt”,
ags. seed „8att,       fiberdrfissig'^ engL sad „betrfibt, ernst'^ (vgl. zur Bed. gr.
```


## [2026-09-06T22:51:35.684Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))['WLD'];print(json.dumps(d,ensure_ascii=False,indent=1))\n\"\necho \"==== page tag near line 29464 ====\"\nawk 'NR>=29200 && NR<=29470 && /pdf page/' refs/incoming/WLD/WLD_Bd2_pages.txt | tail -5\ngrep -n \"pdf page\" refs/incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1>29000 && $1<29600' | head",
 "description": "Find WLD page tags"
}
```


### [2026-09-06T22:51:37.166Z] TOOL RESULT

```
{
 "title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32",
 "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)",
 "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
 ],
 "page_offset": "Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).",
 "lookup_hint": "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.",
 "notes": "Tried IA (several queries), Google Books API (quota exceeded / not full view), HathiTrust (blocks automated access, 403). Band 2 (1927) is US public domain; Band 1 (1930) became US PD in 2026, so HathiTrust full view may exist - check manually at https://catalog.hathitrust.org/Search/Home?lookfor=walde+pokorny+vergleichendes. || UPDATE 2026-09: Bände I and II obtained in full from the Digital Library of India scans on archive.org (open, OCR layer in the _text.pdf).",
 "cites": "volume (WLD1 / WLD2) and page of Walde–Pokorny"
}
==== page tag near line 29464 ====
```


## [2026-09-06T22:51:41.769Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\ntxt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# find leaf number containing 'l(j)akti'\nidx=[i for i,l in enumerate(lines) if 'akti- „Stab' in l or 'lakti' in l.lower()]\nprint(idx)\nupto='\\n'.join(lines[:29464])\nleaf=upto.count('\\f')+1\nprint('leaf(1-based)',leaf,'printed page',leaf-5)\nleaves=txt.split('\\f')\nprint(repr(leaves[leaf-1][:400]))\nEOF",
 "description": "Compute WLD Bd2 printed page for l(j)akti"
}
```


### [2026-09-06T22:51:43.594Z] TOOL RESULT

```
[29461]
leaf(1-based) 448 printed page 443
"                                           lorga, lorgi-   — l(j)akti-                           443\n\nlat.lavdre hergeleitet wird. Lii bei Osthoff MU, YI 3f., Boisacq s. v.,\ndazu noch Franck -van Wijk 372, Kluge® s, v.\n\nlorga, lorgi- „8tock, Kniittel^.\n  Air. lorg „clava“, nir. lorg „a club“, mir, lurga „Schienbein'‘, acorn, lorch\n„baculus“, bret. lorc'henn „I)eichsel“ (aus dem Kelt, stammt ags. l"
```


## [2026-09-06T22:51:49.599Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1236\" BRT.txt | head -20\necho \"---- yax ----\"\ngrep -n \"yax\\|jax\" BRT.txt | head -40",
 "description": "Find Bartholomae column 1236 / yaxšti"
}
```


### [2026-09-06T22:51:49.662Z] TOOL RESULT

```
---- yax ----
2923:•  Jt  g.  ao5ista-  Adj.  (fem.  °ta-)  "der  stärkste ; sehr  stark':  uyranqm  °to  Yt  ig.  38;  — iCfrpm  'um  bavähi  Az.j;  —  w/ra  ^aja- maide  'tä  {/ravasayd)  yazamaide  Yt  y. 75;  —  •/a«tfM  «A'  'Um  (statt  NS.)  Yt /Q.141; —  hitqnt  Avö  °tö  Y.29.3;  5.15, 'N't  10,98;  —  srao-hm  ,  ,  yünam  'tim  Y. ,T7-'3i  —  f ravasayd  . .  yä  °ta  vazintqm \x,  13.  a6;  17;  —  yei  hyqn  *asti.aoJaT?ha (sd.)  'ta  YtÄss; —  k»m  'ta  mahrka.. Oi'sd  (sd.)  yaxäite  V.  //.  2.  a)  ASn.  -tim als  Adv, ;  'bmca  . .  vaRiye,t»napiea  (sd.)  V. 3.30.
2937:•  j.  aoSa-  m.  'Quelle"',  nur  in  upa  'liailu raahaya  (sd.)  "an  der  Quelle  der  R": yatäl  ahi  upa  'laf^u  ranhayh  . .  upa sanaie{sd.)  ratahaya  Yt  J2.  i8£  a)  als Name  eines  Landes*':  x^asJasam  asav- hqmHa  ..  frä^w^rmm  ..  upa  '%al^  raa- hayä  yö  asarB  (sd.)  atwyaxiayänti  " . .  schuf ich  (das  Land)   UAR. . ."  V./.19.
3964:aiwyaxätar-
5014:•  ').  a-vadö.urvatay-  Adj.  'der  einen  Ver- trag durch  das  (blosse)  Wort  abzuschliessen nicht  quaÜfizirt  ist' "';  myazdava  ratus amyaxdavatum  ratunafm  'vaitlm  aaste antarf  masdayasnäii  ".  .  macht  (erklärt) der  Ä. . .  den  . .  Laien  für  unfähig,  durch das  (blosse)  Wort  einen  Vertrag  abzu- schliessen" A.J.8.
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
5218:—  t^m  yaxata  kutaosa  vJsS 'vi  naoiaranqm   :
5308:•  j.  a-ratu'fri-  Adj.  'der  nicht  r.  ist,  die Ratav  nicht  befriedigt,  es  ihnen  nicht  zu Dank  macht,  gegen  ihren  Willen  ver- stösst':  äahms  zaota  dahmS  upa.sraolärü vispe  ratu/ryö  tanupirii^ö  zaota  tarnt- p>r3%5  upü.sraotltrS  vupe  '/ryüti.^i);  — yai  ig  däiti  dalätH  ^rafufrÜ . .  yesi  aal hSnDit  däiti  daoäiti  '/ris'ü.io^;  wo,  loi'^, S03, 104,55,  *55  ■';  — yi  ^ri/*Aa>räricS yätayeinle  ratufryS  yai  Hat  (ä-ri/)  nSii *Aa>r.'rtci>  yataytinti  'fryO  N.  S8;  gj,  gi, 9-',  93>  95;  —  y^i  •  ■  »o  ratu/ryö  yezi *aai  .  .  uva  -/ryJ  (ND.)  ü.$4;  —  yai arastnm  (sd.)  .  .  pairi.iioa  .  .  °/rya  pasca vä  pars  vä  pairi.ä6a  °/ryS  ii.32;  —  yä yastam  *yazfnti..  nva  *ratu/rya  Aam.srul.- väcayala  (sd.)  ^yax^nti  *«va  *'fiya  (ND.)'' N.  24',  — yö  aiwyänhayäiti  kar>tSsca  °/ryS pasca  aiitiySstim  nitaohydti  ratufrys  N. tV^.  a)  mit  Gen.  dessen,  wodurch  (und wofür)  man  ar.  ist  oder  wird:  yasnahe advakt  (sd.)  ratu/ris  'frii gä'iianqm  N.22; —  kaithqm  ml  gä'^anqm  srutanqm  °/rii3 yä  ^maizö  vä  . .  *srävayeiti  aetaesqm  vacqm "fris  "mit  welchen  aufgesagten  G.  verstbsst
6592:—  its/i"'  i?  Ad^m  jräid  aiaurune  .  . Yti'ia  ra^aistaraAe  ..\'.ij.44.  4)  mit Instr.  'zusimmea  sein  mit  — ',  sva.  'etwas zu  eigen  haben.  Jemand  zu  eigen  sein'; B)  im  Aw.:  ratUa  ..  ysi  (NDf.)  ,4?« (statt  Du.)  k}krpa  sraista  (ISf.)  *zazäite (Sil.)  Vt.5.34;  —  ujÄ"*  zl  ana  avc u.\'Mi/a  tsdO/a^a^u/..  V./ij.iO.  S)  mit a)  dem  LS,  eines  Nom.  act.'",  b)  einem Absolutiv,  c)  einem  Infinitiv  im  Sinn  von a)  ilal.  'stare  lavorando',  engl,  'to  be labouring',  ß)  (nur  bei  a)  ital.  'esser  in , lavoro'.  a)  LS.  A)  ||  im  Ap.:  «)  ^adakiy aJam  asnaiy  (sd.)  äham  abiy  ''uvajam ".,  1  wastaarching.."Bh.2. 3; — lyaxnahyä mühyS  14  raocabis  'kakatä  (sd.,  auch fdSt.)  <7-4i»*  ". .  stavano  passando"  Bh.  i. \\;  usw.  B)  im  Awr.:  ß)  aisamcTi  ä ahml  >ii>akml  .  .  vTiiiiBi  (sd.)  ai^T  Y.J2. 8.  b)  Absol.  B)  im  Aw.:  yesi  ahi g-if?  ii?r^3m  (sd.)  V.  sr.  5;  — yesi  anhat Hfiirtjin  vn  . .  aiitii.vantim  (sd.)  vä  V.  7. la;  —  ya^a  na  sat>mea  .,  *parsanqm (sd.)  *nijat3m  hyat  YtTj.yi;  —  yezicä ttasui  nar)m  *3stärayantJm  (sd.)  S»h3t'°* V.  1.4;  — yezi  *hisku  hiskväi  sralsyäntTm  i (sä)  ./«Ä<i/">  V.A'.34.  c)  Inf.  B)^im Aw.:  yims  asti  l>pri%e  (sd.)  xi'airayS  V. 1', 7;  —  iJtar/  vSi  (sd.)  masda  ahurahyS^ aAl\.^O.y,  3;  —  iäis  ä  mazda  vlävalsam  \ ^ti'i'i  (sd.)  ahlX. 34.11;  —  kasluscu'n''i\ a.\'iiu/ig  iJi^?(sd.)  auhai  isväcil  fias  paraos\ aks  är?gi'äitlY.47-A>  — y'^a  nS  ankam  1 (3PKPfA.)">    *Jafd  (sd)    manh  Y.&o.iir
7121:yöpaoiryö  barpsma /rasürmala  >ryaxäTs7a  |  '%re/rabaröis"V.  ig.  24;  Vr.  j.  14  PüZ.  (wo
7133:fraiatimea  .  .  g}us  *vTmitim  N.  tf5(?);  — hat  drajo  haca  ''iirat . .  apat  . ,  baraimn /rast jiryiltV. 3.1(1;  17,  16.^,  l-J.a,;-^  aal tum  nisAioOis  apasca  .  .  yazimnö  'tarimca H.  2. 1 3 ;  —  (7/;»«  ä  va  °trpm  ä  vä  V.  7. *S;  5-37.  *.i04-io6,  Y.7.12,  2.12;  — '^/r  .  ,  aiwyö  V, /<S'.  70;  —  yoi  nmaiia hamiaräntaki  'trimca  bansmaca  tastaca haomaca  hävanaca  V.5,39;  40;-—  'trsm yaxaita  bansma  st}r>na3a  V.  12. 2 ;  J.  1 5, Vt.;2.3,  A.4.5,  Y.f?.s6.  b)  von  dem beim  Gottesdienst  (im  atas  dan  'Feuerbe- liäiter')**'  dämmenden  Feuer:  Hat  ätra- vaxsake  (sd.;  nämL  kairim  atthat)  yat '■tr>mca  aiwi.vaxsayät  ''^rasca  Hlr5  iiraxtis yaoida'^al  N.  Jj;  ffi;  —  aal  frahratarS Isd.)  yat    'Tirasca    alfqm    %raxlim  yaoz-
7184:•  j.  ätarä-äSra-  Adj.  'dem  Feuer  {Älar)  \  Träger  sva.  'zu  Ätar  m  Beziehung  gesetzt, entstammt':  'rJtca  yazati ..'rSsca  V<w-«k/|  stehend':  aat  As  (näml.  naire)'^  nama yaxamaide  Yt-iO.!.  Wradai%yä    StrsMüm    vä  ätrg.ci>nm  va
7563:aL  äsli',  mp.  ähislani^,  s.  No.  S).  —  FB.:  ni- iaslaii,  (lu  Y.  6S)\  apar  an  i  amäk  yaxiSn iiiSliü,  erl.:  fföS  däi-e;  s.  noch  No.  8.  — »  S  '4^-  —  '>  Doch  s.  No.  3.  —  J)  NA.  'inli (aber  •fnti  tu  Vt.  //.  1 1).  —  «)  Theni.  —  5)  Vgl. Dbr.  AiS.  391  und  unter  'iad-  mit  tit,  itiaex ■fl*-  I  5,  —  6)  5  i2ii.  _  7)  Vgl.  noch  ifl*- No.  3.  —  8)  PQ. ;  ßa  draj  i  tbSr  Su  Shrmazd  . . äAii/  (in  Aw.-Buchst)  ifiiJ.
10564:•  j.  xumbya-'*  m.  ER  eines  Gläubigen: fra'jaxSt:is  "ythe  asaonS  Yt./J.i38.
10834:mit /ff  A/  'die  Herrschaft  führen  über  — (Gen.)':  adamsäm  *patiyaxsayaiy'''>  D.  6.  3. mit  Jrä  'die  Herrschaft  begründen,  ent- falten':   yö  ava'iät  fraxlayeite  "der    von
10838:li.  kfayati  'ec  herrscht,  besitzt',  np.  iäyad  'es geziemt';  5.  daiu  Hbm.  PSt.  34.  —  Pa.;  fäti- isihimtan,  pälixiäk  bntan,  fa  pilixiäMh,  (zu F.  J  h):  iämai  j^atälih.  —  ")  So  besser  als S  310.  14.  —  '>  S.  axiyanl-,  axsj/amna:  ~~ 3)  Statt  ahyä  yrkyä.  —  4)  Hds,  iaxsaSe;  aber Pu.:  pilixiäh.  —  s)  NA.  vashxi'%  s.  aber  Y, 50.  9,  31,  19,  33.  15.  —  6)  Unthem.  — 7)  So  nach  Fov  KZ,  Jj.  49;  die  Ausg.  hat faäyaxsaiy.
10864:a)  alkoholische,  'Wein',  Plur.:  ya  *°efra''> *yat  vä  yatanii  yat  vä  * hant-rat^winti "den  Wein  wenn  sie  opfern  oder  mischen" N,  61.  b)  'Samenfliisstgkeit,  semen  virile': a/ra»Aarpzat  {&A.)  pairi  °ärät  V,  JÖ'.  16; —  sonst  Flur. ;  aridvXm  ..  yä  . .  arsnam °ärä  yaoläa^iaUi  Y.  ö'^.  2,  5;  F.^g;  — yaäsa  . .  arsäns  avi  'dra  xsakriiva  Aam.- vjrmavainti  (sd.)  V.  iJ.  32;  —  ya^  nä :^aptS  °dra  fräraobayeite  V.  18.  46;  —  yO näirikqm .  .'drS  avi  ^frarshamaitt  V.  i$.  7, 8;  JA  67,  Nik.i; — yai  maryß  niaslm 'dra avi  fraahfnzaiü  yat  vS  masyS  masySnqm 'dranqm  (als  Obj.)  *pairi  gmrvayäti  V.Ä  3  %  \ — /a^j^J  (statt  NSf.)''rfnl  hqm.rafiwayeiti (sd.)  dahmanqm  adahmanqmca  V.^iV.  6z; N.Ji;  — fravasayö  ..  ya  avam  *°orqtn^'> aiwyax^ayänti  yam  . .  zara^ustrahe  Yt 13.  62*>.
11753:—  tä  xsapanB  yä  *ß'äM  Y.öa.io;  — .  a)  adjektivisch;  a)  im  gAw.:  däidl  .  . ätiti  tä  ^ao^na  .  .  yä  anhus  . .  v»rft- '  tarn  aslm  vaahsus  äyaptä  (sd.)  manatgAs yäii  V.J5. 1;  4.41;  —  yat  ta  sravA  drm-  Y.  25.  7.  B)imjAw.:  *us  ^täai  späna jayqri  yä  pagurva  ,  .  'S,  4,  45;  —  ta  fryi  pat»titi  pasus.haurvqmca  . .  V.  /J.  4a;  43; , .  tä  isuds  .  .  ta  rätayo  *yam  (APn.)  —  pqscaUa  ava  ta  aiü  maya  ..  V.g.ii; oAurS  . .  frävavaca  Y.ö^.g; —  tä  daiA-\^2.  a)  mit  relativischem  Anschluss"; MävS  ..  nijayntnte .  .ydhra  /r<Mir!Hnti  ..^  k)  yai  %Pi}K.:  gavöi  aääisizA.)  iäis  ^ao- /mvafayuYtij.^Si  —  yasf  tarn  dahyüm  .'haiiäis  yäis  vahiitäis  Y.J5.4,  b)  im äcaraiti  yaia  {'wo')  huh3r?ts  *baraite  Yt-ijAiw.:  ttm  ratüm  yaxamaide  yim  zara- 10.112;  —  tä  (statt  NPf.)  daiMävS  ti  "ä-usinm  Y.70.IJ  i';  —  i?m  aküm  paik- ^hamtTT^e  yd^a  duzh?nni5  *baraite  mi~  yäite  yim  aiaoiiqm  V. 18.^6;  76,  5.62; ärff  Yt  10.  48;  41.  b)  substantivisch,  —  upa  tarn  ear?lqm  yqm  datvyqm  Yt  /'/. a)  im  gAw.:  «m  (ASm.)  ..  mimaysff  y!  77;  —  tqm  krhrffm  yqm  iristake  V.$.i; qnm3til(sd.)  mazda  srävl  ahursY.4$.io;  —  täia  vt'hü  yaxamaide  yä  antarpsta  Yt 9;  —  alca  töi  (NPm.)  vaim  hyäma  (Sp.  I3.\^y,~- tä  fravaiay5..aojiita  fuiiti  yä '75  0-)  y^^  ■  ■  ^^fDnaoit  . .  Y.30.  9;  —  paoiryanqm lialsanqm  Yt/J.17,  b)  sub- ai  tSi  at?h>n  saosyaiits  .  .  yH  .  .  htüänti  stantivisch;  A)imgAw.:(i//(i/  msi  daxstfm Y.dS.xi;  —  talcit  . .  ySi  /iisitms  \.  data:  ahyl  ar)ASu£  vTspä  atag^ä  (sd.)  Y. 32. 11;  —  t^ng  tfarayS (sd.)  yöi  vä  daibi-  34.6;  —  tatcä  .  .  'kwaAml  *ä  dqm{sA.) Alt/r  Y.  32.1;  44.11,  13;  —  maf  täis  nipäail:  man5  vofia  urunas^a  ..Y.4g.\o; vispais  yöi  .  .  marintl  Y.43. 14;  —  tal  —  yä  tat  upä.jamyjmä :  tavacä  haxfmä v»myädyäi  kyai  msi  mraota  (sd.)  i-aktstim  ,  asaAyl'ä  Y.  40.  a ; — y.J  tat  upä.jamyämä : 43. 1 1 ;  J/.  5 ;  —  vaida  tat  y''  "Ami  .  .  \  tavatä  sarSm  asafiyä/ä  Y.  4l-  6;  —  ta/a analiS  (sd)  Y.46',2;  —  ta  (APn.)  hwa'  vupä .  .htvaAml ..  xia%r?i  ä  voya'i  ra  (%A.) p^rysä  ..ya  aX  aiil(Sp.  14$  ZD.)  ..Y. 31.  i^l^Y.  34. 10;  —  tat  vJ  nJ  Aasaas Jr^Aj  (sd.)
12620:Koi^E.;  Ableit.  —  np.  vgl.  daitän  'Frau,  die die  Regel  hat'.—  Vgl.  »fradaxUa-.  —  PB.  (lu Y.  J^  V.  2,  13,  l6):  daxsai,  Sü.;  ciknam;  (zu V.  /,  75):  daitän,  (lu  Y.  ßi):  daziln  «;  5.  noch No.  2,  4.  —  ■)  Die  fem.  sult  der  neutt. FormjS  412.  %A.  —  »)  Pfl.:  aparSnia  daitän, erU:  ilakmaklar  trwel.  —  J)  Abweichend  Gdn. 3Vt  ii9i  s.  aber  V,  J.  59.  —  *)  Vi.:  ia  . . daxsai  ucvanet,  erl. ;  dai/än  nihätt  apäl  iunfl, —  S)  Die  Hds.  haben  das  Ideogramm  für yaxisn;  JD  der  Urschrift  stand  dpu«,  vgl.  zu
13309:amavani^m  'k»m  7yaxatum  Yt  10.25; asTiii  vaauhlm  .  .  amavaitfm  'kam Yt/7.1.
14328:/«%««»  Y.p,  19;  i9ffiS;  —  ana  äwal yasna  yaxäm  YLJ7.61';  —  kasp  %wam\ paoiryS  haotna  . .  hunuta  Y.  p.  3 ;  —  kana  , %wqm  yasna  yassane  Yt.5,  90,  15.  54;  —  ' kana  hwä  yaitia  ..  Yt./j.  54;  Vyt.21;  —  j az)m  'hwä  yasna  yasäfu  Vyt.20;  20;  — toi  äyapt^m, yas)  ^wä yäsämaAiYt  10. 33; 30,  5.90,  17.61,  Y.  Ö2. 1;  —  _>'öi  äioÄ vaffun  . .  Yl  io.  9a;  —  _)'o/  äai  J  dtdvllma Y,  öl?.  I ;  Yl  75. 30;  —  _>wji  %w3  didvalSa Y.J.  ai; — ^aäo  %wqi»  mit  taurvayät . . Yt./5.s6;  —  t^a  %wa  haxsöit  gjul vakwa  Y.63. 10;  10,  Vyty,  22,  45,  Any. 2^;  —  afii  %wä  3l>ayai  avairiAeYt.  lo.jy, 78;  — _/rJ  äwam  xadaraAa paiti  uzuxiäne Yt/9.  50;  48;- —  a/a  .  ,,  dansäma  haiS, pairi  %wa  Jamyama,  kamtm  hwä  haxma (sd.)  Y.  60.  la;  —  aoxtSJtamana  %wä yasna  ..yassi  Yt  /o.  31 ;  56,  Y.p.  27;  — aurvantsm  %tffS  ..iayS  tatasatY. 10.10;  10; —  yaskgm  %wqm  paiHsanhämi  V.20.7; 7";  — yaaamaiäe  %wa  aAuräne  Y .  68.  ^ (vgl.  6,  Sp.  787  o.);  Y.li.  10;  — yatayania %wqni  matdayasna  Yt.  10. 1  ig;  12.1';  — _fra  ff  kfhrpgmla  .  .yaoidäiäni;  ktnnaomi hwqm^^  hacaLpuhram  V, 2/.  6;  ■ —  b^a\ &a  histahe..,  iä^a  %wqm  tarasla  äahsns\ .  .  j^anha  bairydnte  V,^,  29;  verwendet Yyt.41';  —  /?  als  Akk.'"»:  . .  kuha  ti assm  biiazüni  V,  22.  6"*;  —  SU  aitike fraca  stuyl  . .  yezi  tl  aidhe  avil.urSrao%a (sd.)  Y./.ai'".  2)  Abi;  nur  b  i)   im
14655:•  j.  Sri.yaxätay-",  itryaxStay-'*  m.,  Plur. 'drei  Zweige':  yS  paoiryS  bar?sma  frasttn- nata  'tfi^a  pancayaxstlila  .  .  "der  zuerst als  £.  spreitete  drei  Zweige"  und  fünf Zweige  . ."  Y.57. 6;  —  •ti/ca  F.4g.
14718:•  j.  OxyaxStay-  f.:  s.  unter  %ri.yaxstay:
15246:•  j.  panc£a.yax§tay-  m.,  Plur.  'fünf  Zweige' ; yS paoiryB  bansma  fraslinnata  'iryaxstlsca (sd.)  UJsca  Y.57.6.
15741:—  lim  al  yasnanqm  °tätä  yaxamaid!  V. jy.  2;  —  at  rätqm  (sd.)  tarahuitrS  .  . äadaitl  °tät?m  manavhascä  vaahsui  masdai
15781:yaxamaide  'rfmca  *upam3m?a  nu^amitnca fr&ttmamla  'rySÜa  yasna  ufamaca  . .  Yt iJ.iZ;  —  tara'^ustraie..yS ..'ryö  ikaisö dahytinqm  ¥1,^.90;  89^,97,  io.i3%9o;
16985:—  sraostm  . ,  yS  paoirys  'ma  frastn-mata %ryaxstlli!a  panca.yaxltT^a  Aapta.yaxällca nava.yaxitii^a  ox^nosca  mathydi.patti^tä- nasca  Y.5J.6; — yaj  'ma  a^.dräjS yave.- frä^S  .  .  yat  masyS  aBakmät  °ma  N.  70;
17008:•  j.  barasmö.zasta-  Adj.  (fem.  '/ä-) 'Barvsmanistengel)  in  der  Hand  habend, mit  B.  in  der  Hand'-,  yas^  Sics  . .  Jrä- yaxäile  . .  'iS  Y.  62.  i;  \.  3.1;  —  *yim aiwitö  mazdayama  histmta  'ta  Yt,  5.  98; —  'ta  (NSf.)  .  .  mittum  harat  .  .  ar^ävl sara  Yt5. 127.
17809:•  j.,  g.''  fravaäay-  f.  ^Fravasay*'>,  Be- zeichnung für  das  dem  Gläubigen  eigene Unsterbliche,  das  Element,  das  schon  vor setner  Geburt  vorhanden  war  und  ihn  über- dauert. So  lang  der  Gläubige  lebt,  wacht seine  Fr.  als  Schutzgeist  Über  ihn.  Die Gesammtheit  der  Fr.  der  Gläubigen  aber spielt  eine  ähnliche  Rolle  wie  die  indischen pitärah,  die  römischen  ««««■:  'sayö  hütti^ Aatqm..aigAu^qm..bUsyantqin{Sf.^^i  m.) a!'aanqmYt.i3.2\;—ä  hätqmca  anhusqfnca zätanqmca  azätanqinca  asaonqm  ilajasmiu °sayd  Y.  öj.  6;  —  aat  anyaisqm  'say!> jvanqm  narqm  aiaonqm  aojyehfi .  ,  ya^a iristanqm  "aber  im  übrigen  sind  die  Fr. der  lebenden  Gläubigen  stärker  als  die der  gestorbenen"  Yl;_j.  17;  —  vispäbyö asaonibyS  *nbyS  y3  irlrüu/qm  .  .  yasia jvantqm  .  .  yäsca  narqm  azätanqm  Y. 24-5;  —  vispanqmca  änhqm  alaonqm asaoninqmla  ila  yaxamatde  °stm  Yt,  ij. 148';  —  neben  'aAs-,  *da?nä-  usw.; alaonqm  aiaoninqmla  ahümla  dafaqtnca baoiasca  urvarumca  °slmca  Y.  26'.  4;  — gai^ssca  asdsbJlca  us'tänqsca  kahrpasca Uvlilsca  baohasia  urvämmca  'sTmca  Y. 55,  I ;  —  xardkuitrahe  . .  'Am  . .  sravä  . . dainqm  . .  varvtifmca  tkais»nca  Y.  16. 2 ; —  manä  . .  dalnä  . .  urunS . .  'say!)  (als  AP.)
17821:yemi  , ,  imat  am>ia  spptita  .  .  imat  asäu- nqm  varguAls  °iays  (VP.)  Wjra  aiiuihüra Y.  65. 1 2 ;  Ny.  /.  I ;  —  aora  varmkis  upa.- sa^a  .  .  äps  .  .  urvarä  .  .  tüäunqm  fra- vasays  Yt  13. 147;  1. 9,  10. 100,  H.  34,  y, 79,  FrW. /.  3;  —  jamyqn  i^ra  asäunqm .  ,  'iaylf  asöis  basfaza  hacimnä  . .  istSe *vadhar»Aqm  paitiHätSe  ätaranqm  Y.  60. 4;  —  qpqmea  .  .  urvaranqmca  .  ,  asao- nqmla  'hnqm  yasnsm  Vr. 21.  \;  —  yS nä  his  hubinta  *barat  jva  a?aonqtn *says  (als  AP.)  sästa  .  .  hö  anhaiti  za- sulttmS  Yt  /J.  1 8 ;  —  fravasayS  .  .  yä a/raourvisvat  k?r»navainti  irsm  yahmya jaanti  Yt.  y.  26;  —  -says  . .  ya  ahurahe xsayats  dasinqm  upa  yü&yänti  yezi  aim bavaiti  ^alavaxsnuiW.  13. 63  ;  — frasüSTnii uyrä  asäunqm  'fayS  paoirij'  pouru^sata .  .  pouruAatanra  .  .  pouruiasvanS  apitii ashntnä  haväi  käcil  näfäi  . .  tä  yü^yeinti pfianähu  have  asahi  Yt  l^.  65if.;  —  "sayS .  .ya  avai  trayS  aiwyaxsayänti  yat  vouru- kahm  ..yä  ave  strjui  atwyäxsayeinti yqm ^haptöiringS  ..ya  avqm  k^hrpim  aiwyäxsa- yänti  yqm  .  .  hnsäspahe  .  .  ya  avqm *x^rqm  (sd)  aiwyäxSayänti  yqm . .  tara- 'huStrahe  navaca  navaitlsla  navaca  sota nava^a  hatattra  navasSs^a  baevqn  Yt  13. 59—62;  —  "iayS  .  .  yä  vts^&a  ävayänli hamaspa>:maedaim  paiti  ratüm  äat  a^ra vtcar?nii  dasa  pairi  xsa/nö  Yt/J.  49;  — asSunqmcä  'HbyS  yä  nS  iltä  urvSibys  Y. 5Ö.  2 ;  —  asäunqm  '/is  narqmcä  näiri- nqmcä  yazamaidl  Y.^7. 3;  —  °fayS  yä paeirya  (sd.)  anhan  Y.  23.  \;  —  äyeseyesti "vTspaya  asavane  'se"  Y,  2_j.  3;  —  vTspä °iayS  (als  AP.)  asäunqm  yazamaide  ädah- *yunqmca ..  'say5 ..*u%dahyunqmla . .  °iayS.. narqmca  ..'^ayD  ..näirinqmfa  ..  °sayS  yaza- maide  Vr.l6.  2;  7.  i,  10.2,  16.  i;  —  nabä- nazdiäanqm  para.iristanqm  aliirapaitinqm a!>iryanqm  narqm..näirinqm  'iayff  yaza- maide  Y.  26.  T,  8  ff.";  —  a/äunam  "sayd .  .  nmänyä  visya  zantumä  däAyumä  zara- ^ustrSJpmä  Y.  ly.  18;  —  airyanqm'  .  . /ßityanqm'  .  .  sairimanqm'  .  .  säininqm' . .  dahfnqm' . .  vTspanqm'  dakyunqm  narqm .  .  näirinqm  .  .  °sayö"  yasamaide  Yt  13. 143—145;  —  fä  'sayU  .  .  aoßstA  hittti  .  . ya  paoiryanqm  tkaihnam  ya  vä  narqm azätanqm  /rais.car>^rqM  saoiyantqm  Yt. y.i7;'Y./.i8',  23.2,  24.5;  —'  vjipä .  .  'Iay3  .  .  yä    haca   gayät    mariihnai   ä
18295:Fnuen;  3)  'nyä  näiryi  usimman&S  aJao- fiyä,  3)     '«vi    näiryä    ''frayax^ntahe
18654:•  j.  nava.yaxstay-  m.,Pliu-.  'neun  Zweige': yl}  paoiryS  barpstna  frastinnata  'hryaxs- iJ/ca  (sd.)  . .  'tdfa  Y.57. 6.
19253:•  j.  iiiiaofaar^tayae-::!!  Inf.  '(und)  Acht zu  haben  auf  — ,  zu  wachen  über  — ':  frada- hai  nmanahaa . .  hani^räila  aiwyaxitraica nipsiayaüa  'ya^a  Yt.j.6;  Y. 77.11;  — mit  Akk.:  gaihiscä  tanvaiüä  nipätayaica 'yaica  Y.5Ä  a.
19372:mä  apalma*paurväpaySit(Sp.S'jo\L)  mäK. *»iaSa(sd.)  ia^anna  *paiti.Jime{s6.)  Vr.22. 2; —  ma  dim  mntyä  ä%ravan»m  ..tim  dim mruyä  ä^ravarum  . .  yn .  .Y.1S.1  —6;  — ma  hrayam  vahiStanqm  atwt^yS  buyata  . . %rayqm  acistanqm  amihyj  buyata  V.  t8. 17;  —  ma  mihrake  . .  vaFfai  jasaima Yt  10,  98;  98;  —  mä  buyh  aurvaiqm yaxta  ma*  . .  Y.  11.  7;  g.  29';  —  ma x/ayamna  jasSit  atrrm  ma'  .  ,  Y.g.zyi 'S-49i —  "»ä  mqm  ..fraspaysis  tiX>%.li8\ Yt.  8.  593,  FrD.  4J,  Vyt  12*,  j-j,  J7 ;  — ma  Bs*^  mi ankam  sao^ranqm  vindita yä ..mä  fiarB pairi/ta.xsulrif  mai . .Yt IJ.S4',
19648:•  j.  (3.)matJyöi.paitiStiina-  Adj.  'bis  zur Mitte  des  Beins  reichend,  so  gross,  dass es  bis  zur  Mitte  des  Beins  geht':  yS  paoiryS bansma  frastprmata  %tyaxitls{^^ca  .  . äxlnaiea  maihfSifaitiitänqsla  ". .  bis  zum Knie  und  bis  zur  Mitte  des  Beins  reichende (Zweige)"  Y.57.6.
19661:I)  NA.  auch  '5iz: ■  j.  maiSyöi-äam-')  m.  Name  der  Gott- heit der  zweiten  Jahreszeit  und  des  an deren  Ende  gefeierten  fünftägigen  Fests*' (mit  dem  letzten,  60.  als  Haupttag):  "Imtim vSstrSMätainlm  (sd.)  asavanim  asahe  ratüm Vr.  2.  3;  Y.  2. 9;  —  'make  V3strd4a(ainyeh4 Vr.i.3;  A.j.3i  —  'ümäi'^  Y./.9;  — bityeht^a  nä  myaxdahe  (^äiti  (sd.)  . .  yat s'fmahe'^  A._j.  8;  —  xivaltim  's>mahe'''> tistryeke  dai:u^S  "60  [Tage  sinds  bis  zum (Haupt)tag]  des  M.  [tm  Monat]  des  Tiitrya [am  Tag]  des  Schöpfers"  A.  j.  8.
19731:tSm  Vi  ala  mjAmaiäl  *htiJtaxaim  (sd.)  Y. 4lS-  ij;  —  sptutjm  ai  %wa  maxdä  nOngkl oAwa  hyat  . .  "als  den  Heiligen  erkannte ich  dich  da,  o  AfAi^  als  . ."  Y.4j.  5; —  atfmcti  akyä  masda  ^wam  mfAAr foMtrDim  vaBi»m{sA.)  Y.2g.  10;  —  matdä yasmmla  vakm^mcä  vafditim  amshmaidl (Angm.)  Y.J5.  7;  —  Xmatyi^  ..  avaiya pama  *^adayä^  (ad.)  ^a*  mana  kartam mailitn  vamavätaiy  tlurvxtam{sA^  *mam- yataiy  Bh.^8; — pass.:  lUAi  aysm  angrS (sd.)  *maüiyae(Kony)  Y.  44. 1 2,  a)  zum praed.  Aide  tritt  der  In&nitiv  'sein':  al ^wä  m^hJ^paaurvlm  .,*yaxüm{sA.)  stSt manaifÄa  Y.JJ.S.  6) Med. 'sich halten fQ[  — ,  sich  voilcommen  wie  — ,  sibi  videri' mit  piaed.  Nom.  eines  Fait  sva.  'glauben, vermeinen  zu  — ':  nmati^m  hs  mariyaZla paraJahlf  "der  mag  ein  Haas  zu  ver- schenken glauben"  V.  /<?.  a8;  — yS  *main~ yäU'^  davayänti  (Sp.  680  o.)  ^rava- n^mta..  Y.i0.i$;  — yS,.na^a  mai^ett jaynvä  "der  . .  und  nicht  geschlagen  zu hai>en   vermeint"   Yljo.  71.  7)    mit
19924:«L  minati  'er  mindert'  (usw.).  —  Pü. ;  vinäsisti 'Zerstörung';  vgl.  'vmilay-.  —  ')  Unsicher. j.  mayludivanam  N.  63 :   lies  myaxdoüanqm (soT).
20767:nalmanam  vätS ..bao^lm  vTbaraiti  aAmät.. Y.S.So;  — ■  die  Beziehung  ist  ungenau: j>a  ^ifanhe  [az-ä]''  ya,  nairyä  yä  .  ,  ya ,.  ya  haca  dafvayasnaiibyS..apa.öara  aya (Sp,  7  u.)  ratu/ris  N.  5^;  —  yS ..  draoiiS zinäl..nsit  aAmi  (Sp.  7  o.)  mnane..  Y.ll. 5f.  ß)  adjektivisch;  wie  eben;^^../iai'ffip»( vanäaita  masyS  ,.  äbys  {Sp.  7  o.)  iattubyS.. Y.70.8*'; — NSm.mit«a(s.Sp.  iaooo.):^i' «a  ^f/  frayaxaite  .  .  aAmäi  .  .  Yt.  13. 51.  d)    aSa-  (Sp.  14111.);    nur  b)    im
20810:monstratives Korrelat;  A)  das  Relativ  be- zieht sich  auf  ein  Nomen,  das  j)  voraus- geht; a)  im  gAw.;  das  Relativ  ist  a) substantivisch;  zu  i):  mainya  .  .  yS  ä nürSmHt  ..  Anmd  Y.^;.  7;^2.  8,  jtf.  i;  — ahSm  yS  vaahju!  manaijks  Y-SJ.  s;  — manash  kyai  (NSn.)  vahi!t>m  Y.  28. 9;  — vali  srBidyHi (sd.)  hyat  mar?taiibyS  vakil- t?mY.45.s;35.  5: —  s.  noch  >a/ No.  i ;  — padai/{s±)  yä  (SPrt.)/rasrBtä  Tiayä  Y.50. 8; —  mTid?m  yehyä  ta  da%r>m  Y.34-  '3; 31.  5,  48.  T,  —  yax  cahyä  xiaya%ä  (sd.) yehyä  mä  äi%isi^A)  dvar'kaY.48.^;  — uiä  arfm-pikwä  x/apäciJ  y  ä  (tiVi)  manaa- "hn/isd.)  lazdönnkvantitn  Y.44.S; — katao- Ür3hö(sA.)  vTspäffAo ..aifm  vohä  mana^hä
20821:. ,  yS  anhat  .  .  mq^rvm  p^nsB  .  .  yB apivatäite  dainaya  V.  g,  3;  —  yvJnB yB  nB  Auhiylqm  bamt  Yt  15. 40 ;  —  at . .  yas»  tat  nmämm  äksr^rum  V,  22.  i ;  — itita  tlyB ..  vasöjxsa'hrö  aki  Y.5.  25;  V. 7.53; —  tum  .  .  y5  aoJiStB  yS^  ..yB\as\ vpTphrajqstimB  aiavai'"^  mainivä  dämqtt ^■9-  '5i  —  *if  'Vo\i.  bezogen:  nara  yd mqm  ^aiwi.v^risyelii  V.^.  26;  —  die  Be- ziehung ist  ungenau;  vtspe  drvantö  tanu.- drujS  ye  ad;>r?ig.tiaisij(ad.)  "V.JÖ.  18;  18*; —  NDm.:  pdyO  %wBrpilära  ya  vispa %ui3r?satB  damqn  Y.  57.  3 ;  —  staomt  mal- Itmia  vänmca  y3  te  A)Arp?m  vaxsayatD Y.  jo.  3;  Yt/_5, 13;  —  vayaiibya  patarg- taiibya  (sd.)  yö  parmlnB  fravatante  Yt.  10. 119;  —  s,  noch  unter  NPm.;  —  NPm.; amisanqm  spfnianqm  ysi  ai>-yajanhS  Y. 2Ö.3;  Yt  J?.83f.S  Vr.j;.i2';  —  yaxa- maide  vlspil  ..  yazata  . .  yBi  vaahuOanAö Y.  16.  9;  G.  2.  6,  Yt  12.  38ff.5,  13.  9,  ig. 18;  —  ratavB  ysi  h»tUi  .  .  Y./.io;  10, 7/.7£',  10,  A.3.  I,  Yt  ig.  18;  —  t/iaisa- nqm  .  .  yBi  aiäi  vaonarf  Y.  26.  4;  Yt 13.  150';  —  spänB  yBi  hiltittte  at^arB V.  13.  28;  14. 17;    —    datva  .  .  yBi  para
```


## [2026-09-06T22:51:58.054Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"'Zweig'\\|„Zweig\\|Zweig'\" BRT.txt | head -20\necho \"=== columns near ===\"\ngrep -n \"^12[23][0-9]$\\|  12[23][0-9]  \" BRT.txt | head -20",
 "description": "Grep Bartholomae for Zweig"
}
```


### [2026-09-06T22:51:59.991Z] TOOL RESULT

```
17935:•  ].  tra-spanysi-  m.  'Schössling,  Zweig' varihayamtha  . .  vup^sca  paiti  . .  varsajil . .  *yJ  .  .  fraväxss  Y.  lO.  g.
21067:•  j.  yaxltay-  m.  'Zweig'.
22435:np,  bär  'Zweig'  (rfoRN  GlrPh.  /  b,  170);  gol. vgl,  wandus  'Rute'.  —  ■)  So  nach  JusTI  ZDMG. 50.  663,  53.  9z,  GIrPh.  2.  426.  Dagegen neuerdings  Fov  ZDMG.  54.  356,  55.  509.
22992:KompA.i  s.  aucb/rJ.wjvjfl-.  —  mp.  iiori 'Haar', ai.  vääa-  m.  'Zweig';  a.  Bthl.  IF.p.  252  (be- stritten von  Uhlenbsck  WAiSpr.  277,  wotu PBrB.  21.  106,  LtDiN  Sind.  48,  Yt.  5.  77).—
=== columns near ===
20894:folgendem  hyatclt  (Sp.  593  u.);  nur  a)  im gAw.;  zu  I  2  k:  at  tä  vaxfyä  .  .  yä (NPn.)  Mazdä%a(sd.)  hyafcit  vjdul!  Y.jo. I,  b)  Einmal  findet  sich  im  jAw.  die Verbindung  _>'(j-  kvant-  im  Sinn  von  'wenig, gering":  kä  fraiüitill  yat  kvai  (sd.)  N. 103.  c)  Einmal  ist  im  gAw.j'J  NSm.  im Sinn  von  'o  dass  (ich) . ."  zum  Ausdruck  des Bedauerns  gebraucht;  der  übergeordnete Satz  fehh:  aica  gSus  urvä  raox/3{sd.):  y) analsim  xsqnm}nl(sd.)  rädern  *'yi  *mä  va- Sfftiiisd.) . .  y.  2g.  9.  IIA)  zur  Anknüpfung einer  nominalen  Ergänzung  oder  Erläute- rung an  ein  vorausgehendes  substantivisches Nomen.  Jeweils  unter  o)  sind  die  Stellen au^eführt,  an  denen  das  Relativ  einem vorausgehenden  Demonstrativ  entspricht; Stverz.  unter  dem  Demonstrativ.  a)  im gAw.;  ich  verzeichne  hier  nur  solche Stellen,  wo  das  Relativ  nicht  nominati- visch ist  oder  sein  kann^*';  vgl.  dagegen zB.  Y.  2^9  (Sp.  1207U.),  3g.  4  (Sp. m.)  und  B  I  (Sp.  1225  o.);  a)  ASm.: yf  mSi  .  ,  vao^äi  . .  mqhnm  ytm  kauf- vatätB  Y.  31.  6;  —  vahUfym  %wä  .. yStit  hasaoAm  ahunm  yOsä  (sd.)  Y.  28. 8.  b)  ASf.:     ka%ä    .  .    yaol  dalnam
20926:5.  aber  Vai.  —  '7)  Pö.!  mal  ai;  s.  No.  4.  — "»)  Wie  No.  14-  —  "1  Aus  dem  gAw.  her- übergenoromen.  —  "»)  Die  3.  Person  hinter iura  ist  aufmiig;  es  lind  wohl  ursprüng- lich nicht  EU  einander  gehörige  Stücke  zu- sammen geschweisst;  s.  No.  23.  Unrichtig Sp.  Gramm,  d.  alttoktr.  Spr.  313;  s.  V.  ,9. 25.  —  ">  Wo  yöi  auf  (iPf.  und  GPn.  bezogen ist;  S  rfl6  Bern.  Die  Stellen  sind  einander sehr  ähnlich.  S.  übrigens  No.  24.  —  »»)  Das mask.  Relativ  bezieht  sich  auf  Nomina  mask. und  neutr.  Geschlechts;  s.  No.  14.  —  'i)  yn; auf  gaf%aHiim  GPf.  bezogen.  Vermatlich weil  zwei  ursprünglich  nicht  zusammengehörige Stellen  verknüpft  sind;  s.  No.  14,24.  —  >4)Man verlangte  NPn.;  die  GP.  der  Stamme  auf  -a und  -ö  haben  gleichen  Auslaut;  s.  auch  No. 21,  23.  —  'S)  Geringe  Stelle.  —  '*)  So  F  I ; ti\.  yim.  Anffällige  Bildung;  auf  ar.  */<im nicht  zurückführbar.  —  '7)  Hds.  yaki,  was nicht  richtig  sein  kann.  —  iS)  Ob  I^f.?;  aber die  Fanktion  U(  steta  genetivisch.  Vtl.  geht ye>ikc,yfht^  auf  die  ar-Jonirtiforra  zu'^jjjJi. — •9)  Vgl.  n  B  A  1,  sp.  1223  o.        ^1  Pü. ;  mal;  s.
21075:1238
21195:•  j.'yat  g.'ßyat''  I)  Part  zur  Anknüpfung einer  nominalen  Ergänzung  oder  ETläute- rung  an  ein  vorausgehendes  Nomen  *', sofern  'i  nicht  als  neutraler  Nom.  oder Akk.  Sing.  genommeD  werden  kann  (vgl. Sp.  1233  ö.  unter  b);  die  Fälle,  wo  ein Pron. dem.  vorausgeht,  sind  unter  n)  eingestellt a)  NSm.;  a)  ;  aild  zl  asti  .  .  balsa^BAimd y  *mai:r3m.ipmt3m.baisatyS  V.  7.  44;  s. b  o.  b)  ASm,,  n.:  vacim  y  frsdat.- gaifh?m  S.  2.  18;  —  puhrtm  y  pouru- !aspake'^\,^.\%\  105; — xrvant3m..pantqm .  .  y'  oitasca  baobanhasca  vl.urvistlm  H. 2.  17;  —  ahm  (ASn,)  at  vakiltsm  yam- maidi  hyat  sraist>m  hyat  sp}nt>m  aims>m (ASm.)^^a/  raocSntahvat  hyat  *vlspä.vohü Y.^7.4]>.  n):  ttm  ..y  *mq%r3m.spsn-
21246:Aus  dem  Zusammenhang  gerissene,  un- deutliche, verderbte  oder  wertlose  Stellen: y    iri^näaAe  . .  sät>m    da%aiti    urvangm P.  Jj;  — y'  Aanjasatite  aat  ..y  yasanii  y' va  Aqm.rag%wayanti  . ,  y  . .  ndit  viritmti ^/•"''»j..  N.  tfa"'; — y  As  avai  pounm ubjyaite   V.7. 5a  PüZ.;    —    y    Al  a^ra daxstim  bavaiti  Y.  16. 14;  14;  —    aal  y . .  barät  aal  y  ('wenn')  . .  baraite  pascaita .  .  urvasma  (sd.)  dalsayeni  V.^S;    —  y paili.baränti    N.  54  (s.  N.  54    mit  paiti.- barmti,   Sp.  12560.);  —  femer  Y.  rp.  14, Y.y.z,  <V.74PUZ.,  Ytj.2,  75.52,  FrW. ■y.2,  N.+4.  6s  2.,  3.St,  S3,  Vyt  43.  5'< Vd.  -',  10,  13,  18,  20.        yä&a  yat  (ausser zu  Y.  ig.  10)  und  yatcit  sbes. ASr.  »Msya;  ''Aya-.  —  S.  ^yal.  —  ai.  yät  Konjn. —  PS. :  (meist)  ta,  ti;  (auch)  iu  -  iB.  Y.  ig.  5, V.  5.  41  -,  Äi'Ä-i  -  iB.  Vt  r.  6,  Y.  jtf.  I  -, /aiiä  -  iB.  Y.  43. 8,  N.  2/  -,  und  weggelassen ; (vereinielt):  AaJtar  -  V,  31.  9  -,  läk  ta  -  Y. 46.  6  ~,    eten  -  Y.  5/.   14;    s.  noch  zu  fara ahmät  yat,    vhpitn  ä  atmä£  yat  und  No.  2  f., Sf,  9.     —     ')   Vgl.  Sp.  1227    No.  I,  2.    — »)  Pii.;  /flj  . .  pcs  I5tl^\   —  3)  Hds.  yi;  Pü.: ka.  —  4)  S  504  n.  2;   vgl.  N0.8.  —  5)  Hds. yCK%   Pü,:  ta;    !.  No.  4-    —    *'  Pä.:/a/  hat uziiüimh.  —  7)  Do«  erste  Mal,  vor  *aiis.vtiö. iu!,  tA\t yas/a  in  den Hd«,  —  *)  $^0^11.46; vgl.  No.  4-  —  »  Fehlt  hier  in  den  Hdi.    Pü. lässt   es   überall   weg.    —    ">i   Hds.  yäl.    — ")  Vgl.  N.  6f,  Sp.  1262  o.
21793:NSm.  aus>'fl-;  s.  '>*.  —  Pü. :  j.  —  •)  VII,  eine  Kon- tamination aus  anhUus yat{^^i3^\v,^)astvatS und  aahiui  yö  astvi  (Sp.  1232  o.l.  —  >)  Man beachte,  dass  regelmässiges  yö  (Sp.  1222  m.) vorhergeht  —  i)  Geringe  Stelle.
26767:kein  sein  könnender  Mensch.  S.  daiu  Den.  —  >*  ^'^  yoi^^nä  (Sp.  1237  o.)  dasiml VglS.  2.  461.  ;'''?"'  Y.  21.V.  9'>;  —  vaDCä  .  .  Oud^m  (sd.)
```


## [2026-09-06T22:52:04.906Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21055,21090p' BRT.txt",
 "description": "Print Bartholomae yaxštay entry context"
}
```


### [2026-09-06T22:52:04.953Z] TOOL RESULT

```
iehf :   als5  nä  yd  'ryö  V-  5,  39,  40,  42,
ai^hä  z»md  vt^pSJ^mfm'a (sd.) huiiSj3mSJ»m»m  a  V.  j,  1 5 ;  5.  46.
Saperl.  ans  'yaa:dälä.iam-  Adj.,  im  Antchlnts an  den  AS.  gebildet.  —  Pü. :  ysidätr  tamtktwn, mit  der  ErL:  hai  hijcr.
•  j.  yaozdäiti  In£  'rituell  zn  reinigen,  zu purifi^ren':  kat  tu  vtutra  hqmyüta  pasca y  framäiti  (sA)  V.5. 57;  58.
Znm  V.  yaoidä- ;  »gl  yasidÄlay-.  —  Pü,  j  pas ka  yoidasr  fräc  last.
•  j.  yaozdäitim  Inf.  'rituell  zu  reinigen, zu  purifiziren':  t6a  iristahe  tanüm  ava.- hiiia  .  .  isaita  mi  y  .  .  yesi  dim  nöit yaazäa^m/t  (sd.)  V.S.ioo.
Zum  V.  yaaidä-;  vgl.  yanldälay-  und  *aiilim. —  Pü. :  i^ähel  e  man  yiiidiirih,  erL :  kum  a/i lÖiit.
•  j.  yaozdäSra-  n-  i)  'Heilmachung,  Ver- voUkommDung':  kahmili  a^m  daöqtn  vT- rayam  Htiin  .  .  havaheca  urunS  'r>m  Yt. 8. 15.  2) 'rituelle  Reinigung,  Purißkation': *nm  srävayJi/ (sd.)  aarähustra  V.  11.  2;  — vastranqm  •ranqm  Vd.  20;  —  mit  Akk, verbunden:  yai  M'an  usuxiyeiti  bvati^A^ tqm..'r}m  Yt^fj.a;  j»;  —  iwS«  nänm.. yaczda^äni  kuia  niirikqm  . .  °r?m  baräi
'däni  (AD.)  ganmojkaratia  " Y.  und  G' V.  i4. 7">.
Zum  V.  yaoija-.  —  Vgl  ya^^ana-.  —  Pa.: yäidJK,  Ttaniskr.  —  ')  Vgl.  ätrjm  fairi-yoMäa- %3Ht>m  V.  I.  1.  —  =)  Zu  BB.  /a  167.
•  j.  S-  yaozdäh-  Adj.  (auch  fem,)  'voll- bringend, vollkommen  machend',  mit  Akk. verb. :  vanhuya  HstdÜ. .  'da  (NSf.)  ma^äi *'aipj.zq'inn  vahistä  gav5i  VfmyStqm  (sd.) "der  guten  Lehre;  sie,  die  beste,  vollbringt für  den  Menschen  die  künftige  Geburt . ." Y.  4S.  5 ;  —  'da  masyai  aipi^q'iim  vahista hä  °dii  . .  yä  dama  mäsdayainii  y3  kvqm tttikvqm  yaoidilite  humataiua  .  .  ".  .  sie vollbringt  (die  künftige  Geburt),  die  maid. Religion  (fUr  den),  der  ,  ."  V.5.  ai.
Zum  V.  ya,'Sd.i-.  —  Pü.  (zu  Y.  4^}:  yöidäsrU i  "lartumJti  f-ai  kal  :  ii-ün  pahlum,  erL  :  p<is haczlyün  aiinäslh  fnhltm,  (lu  V.5):  y^ätrii iailan  maritim  fikih  pa  ravän  pai  kac  täyihi
•  j.  yaxltay-  m.  'Zweig'.
KompE.    —   sä.  yasiay.  m.  *Stib'').    —    Pü.: tat.    —    '1  Nach  dem  «.  Won  muss  dai  in Grunde   liegende    arische   1/   gehabt   haben; Aw.  xit  ist  also  sekundär,  TgL  %  S6  aE. j-,  g.  yat-  V.  'sich  in  Bewegung  setzen'.
"wie  soll  ich  den..  Mann  purifiziren,  wieiPraes.  a  ydta-,    24  yataya-,    30  (Kaus.) die  Purifikation  der  Frau  besorgen?"  "^ .\yätaya-\  Perf.  i  yayai-iyaa-'^. rp.ia.  a) 'Reinigung  von  einer  Schuld  J       i)  'sich  in  Bewegung  setzen',  Perf,  'in
EntsUndigung' " :    »ava  he  asti  Hia  (sd.)  ,  Bewegung  %t\i^:  yayata  dunmqn  yayata..
Uiflitized  by  VjOOQ  IC
H37
yat-  I  a
yaSät
1238
upa.ap3m  i&A.)  "agitatur nebula,  agitatur.." V.2/,a'';  zitF.^g;  —  y^'  fl yaltatari {3D.)  F.  4g^';  —  ^yastuuiha  {Mq\%.) F.2^«>;  —  j'a«»/(NS.?)  F.^f.^';  —  imh yaetusT^^^  zao%rA  "diese  OpfergUsse,  die im  Gang  sind"  Vr.  ;/,  3.  a)  'sich  rühren sva.  emsig  tätig  sein,  eifrig  sich  bemühen um  -'  (Lok.):  vaiahu^  sraose  ..  h^la  ioa y!H"^wä  (NS-)'*  *'«■/«  ". .  und  der  soll  hier emsig  tätig  sein"  Y.27, 6; — ySt  vJyöP>7mä (iPPfA.)  das3m!  stütqm  "indem  wir  (viel- mehr) uns  beeifem,  euch  Lobgesänge  dar- zubringen" Y.aiy.  9";  verwendet  j/.  9,  wo yH  vS yaSima"'.  a)  Kaus.;  a)  'in  Gang
setzen  sva.  zur  Verwendung  bringen':  yezt "Siris  *Aa^rän^S  yätayante . . yezi  äal  (^ris) nBii  *halir>'iiuff  yäiayanli  "wenn  sie  drei {Bansman-Zvitigt)  zugleich  zur  Verwen- dung bringen  .  ."  N.  tyii''';  —  yai  'irü *hairäkafibis  ''yiltayeinti  ,  .  yesi  äat  %ris nöit  [är/V]  *Aa^räkagiHs  yatayänti  N. t??'"'.  b)  'betreiben,  sich  befassen mit  — ,  sich  beöeissigen' :  tum  ts  datrihävi tiipahi  yi  hub>r>inm  yätayeiti  (statt  Plur.) mi%rahe  "du  schirmst  dann  die  iJinder, wenn  sie  sich  der  guten  Pflege  des  M. befleissigen"  Yt. /o.  78.  3)  3SPfA.  mit zurückweisendem  tai  (Sp.  616  u.)  'es  ist dazu  gekommen  sva.  man  hat  es  dazu gebracht,  es  reicht  dazu'"':  dätaca pas3us  *gjr>bu} . .  yai  tatyayata  navättat yayata  hurayäscit  .  ,  ".  ,  wenn  es  dazu reicht;  oder  aber,  wenn  es  nicht  dazu reicht,  .  ."  A..j.3">;  4*,  5".
mit  Jrä  i)  'sich  heranbewegen,  herzu- kommen'; yüi  uva^bya  snai^Iidya  frä- yaiayeinti  vaz»mna  . .  Y.57.a9'3>;  —  wnA (sd.)  lai  äs  .  .  yat  fräyalayai  .  .  aoi  zqm Yt.5.  65.  2) 'Jemanden  (Akk.)  angehen um  — '  (Akk.):  aom  iianm  ..yü  nä  masist>m yasfum yazäite  kaiiU>m  ^yasnät  fräyattli'*- *ahma  *ya  amis}  spmts  "den  .  .  Mann, der  (uns)  das  grösste  Opfer  spendet,  (dabei aber)  uns,  die  ASp.,  um  das  geringste  für sein  Opfer  angeht"  Yt/.  a4(?),
mit  hawi\  s.  " hqm.yaztäifhö.
ai.  yäta/i  'et  scUicssl  an'  (usw.),  yälayali,  yel- ire.—  Pü.:  Terschieden,  s.No.zET.  —  »  Vor Kons,  aach  mit  oi,  %  79/.  1.  —  '}  Pü. ;  rimii-i aiorpa  raaiiin.  —  J)  Pd.:  kakar  an  mal  esifl. —  *)  Them-i  Hds.  'Uta.  Pü.:  fehlt.  — S)  Pn.:  mal  {estit).  —  6)  Pii.i  kac  IS.  Sind  die Worte  y'  a'  einer  verlorenen  Gä%ä  entDom men  ?  —  7)  Pö, :  il  S  i  1  smäi  ayäUiärlA  daht
itäyitärän;   s.  mber  No.  8.  —  8)  Pü. :  i?  man
lial  Imäk  otai  istet;  s.  aber  No.  7.  —  9)  Pü. : haiar  j  afi  kam  hakatün  raminfnd,  erU :  3  lik räsi  ape  girind;  s.  noch  No.  lO.  —  ■")  Pü. : hakar  3  fia  katanbi  5  kam  därind,  ert. :  J  läk rast  ape  gircnd;  s.  noch  No.  9.  —  ")  Vgl. liilava,  —  <>>  Pu.:  kakar  tuvätilk,  Sü.:  yadi  tat prjflam,  Npü. :  har  fäi  an  das/^äA  alt,  — ■J>  Pü.:  if  ,./räc  rasa.^tt}  FiL:/rä^  Aar» rasim.  Lesung  des  Worts  unsichet.  DsT.  ZA. 2.  342  lässt  y  J'räy  aus.
j.  yata-  Adj.,  PPfP.:  s.yam-. KompE.
•  j.  *yatay-"  f.  'Sichhalten  an  — ,  Sich- richten nach  -':  °t5  (LS.)"  paurmeibya ydia  rdi!a2s'ta  "indem  ersieh  an  die  beiden Vorausgehenden  hält,  (ist  der  Hund)  wie der  Krieger"  V.  y.45(?)-
Zum  V.  yaai:  -~  Vgl.  apayat/e,  apayetli.  — ai.yätay  t.  'Feslbaltung'.  —  Pü.:  ra//.lr  d  pis, erl.:  viHn  iiwa.—  -')  S0I.4,  Kl.  'HK.ra/lö. Aber  ein  dem  np.  ta/lan  entsprechende» Verbam  fehlt  dem  Aw.  Also  ist  ra/tS  der Pü.  zu  danken,  deren  raj'ISr  zeigt,  doss  man yal5  mit  a/ili  i^ay-)  verband;  vgl.  Sp.  Komm. /.  3lS.     Wie   soltle  die  Lesung  j'a/d  entstan-
•  j.  ya'tira-  Adj.  (fem.  •/-.!-)  'welcher  von beiden':  °t!irö  pourvö  fräyazSUe  .  .  alärS (sd.)  . .  Yt  14.  44;  —  'rS  paurvS  .  .  'rS paurvo  ..  ahmst..  V.iS.i6;~-t,ira  (NSL, näml.  daiäiuf)  vä  dim  paurva  fräyazäiti ..  iltara^ra  ..  Yt  /O.g;  —  yafara  (NPm.) vä  dispaurva/räyawnte..  atara^ra  ..  Yl 13-  AI-
Kompar.  aus  ya- ').  —  U.  vgl  yalarä-  Adj.  — Pd. :  aiir  i  ki.  —  ')  Zum  ä  s.  kaiära-.
•  p.  yad-  V.;  s.  unter  yat-.
•  g.  ya'dä  (,  j.  ya'^ä)  Adv.  und  Konjn. i)  zeitlich  'wann,  wenn  erst',  mit  fiit.  Konj.:
y-  als'qm  ka?nii  (sd.)  jamaitl  .  .  at  .  .  Y. 30. 8 ;  —  y'  assil  mahyä  vas3  xsayä  (sd.) at  ..  Y.jo.  9;  —  in  indirekter  Frage: p^rjsil  avai  yti^ä  kvs  yS  .  .  >wävqs  (sd.) ..y  hv3  auhatX.  31. 16.  a)  bedingend 'wenn,  sofern',  mit  Konj.:  y  as?m  z?vim (sd.)  aahtn  .  .  Y.  ?/.  4.
```


## [2026-09-06T22:52:22.519Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 525 ===\"\npython3 - <<'EOF'\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint(len(leaves))\n# leaf = printed + 24\nfor n in (548,549,550):\n    L=leaves[n]\n    print('=== leaf',n,'->p',n-24)\n    print(L[:1500])\nEOF",
 "description": "Read Buck p.525"
}
```


### [2026-09-06T22:52:24.215Z] TOOL RESULT

```
=== SYN 525 ===
1545
=== leaf 548 ->p 524

CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
1. Grk. addat, fr. *&pAax- (beside *arodx-, *a¢hox-in Hom. Sk, Att. &dob) : Lith. vilkti, velku, ChSl. vlésti, vléka ‘draw’ (9.33). Hence NG aidaxt. Walde-P. 1.306.
2. Lat. sulcus (> It. solco, Sp. surco) : Grk. &xw ‘draw’ (9.33), ddxés ‘track,
See eee A
Ee
SS eS
ek ae ed
To I
1 made by the ybnot ‘furrow 5 B07. races © ih ‘plow’. Walde-P. 2. plows 999
renout °* ‘er use ‘heaped-up pra _ sill n, 10 a ‘heap up earth’, earth’ fr. iiic orig. Hence used for the prob: af ‘ea between furrows, then for es ‘gel, REW7797a. Gamill- the abe furrow’ in OFT. and still in | use more widespread than stllon tas linguistique, Carte 1234), fr. a ca word represented by W. rhych, ete. (below; 8). REW 7299. Gamill- scheg 736. Bloch 2.204. Rum. braadd, fr. Slavic (below, 6). 3. Ir. elrech, Nir. eitre, W. rhych, OBr. rec : OF furh, ete. (below, 4). Pedersen 1.122. Thurneysen, Kelto- rom. 74 f. Nir. clais, also ‘groove, trench’ as
Ir. class : claidim ‘dig’ (8.22).
, Boh. kopati, Pol. kopaé
noma fo k ny kapas ‘grave, 5; Kameros (UPS grave’, Grk. oxdme-
Tuncare ‘root up, tear out, pluck’, fr. an : reu-in Lith. rauts
Walde-P. 2.353. Er.
AGRICULTURE, VEGITATION
Digitized by Arya Samaj Foundation Chennai and eGangotri
497
Br. ero, erv = OCorn., W. erw ‘field’ : OHG ero ‘earth’, etc. (1.21). Walde-P. 1.142. Pedersen 1.63.
4, ON for, OE, OHG furh, etc., gen- eral Gme. : Lat. porca ‘ridge between furrows’, W. rhych ‘furrow’, etc., perh. Skt. pargan
=== leaf 549 ->p 525
 sapd ‘hoe’, MLat. sappa (8.25).
3. Ir. claidim (NIr. claidhim ‘ex- cavate’, W. claddu ‘bury’, old ‘dig’; now for ‘dig’ W. cloddio, fr. clawdd ‘mine, quarry’, arch. ‘ditch’), Br. klaza : Lat. cladés ‘injury’, -cellere ‘strike’, etc. fr. an extension of *kel- in words for ‘strike, cut, etc.’. Walde-P. 1.489. Walde-H. 1.225.
Nix. romharaim (W. arch. rhyforio), fr. NIr. romhar, MIr. ruamor ‘effossio’ : ChSl. ryti ‘dig’ (below, 6). Walde-P. 2.352. Stokes 234. Otherwise Loth, RC 34.146 f. (taking as epd. of ro- and mor-, mar- : Fr. marre ‘hoe’, Lat. marra, but this is not a Gallic word, cf. Walde- H. 2.43),
W. palu, fr. pal ‘spade’ (8.23).
Br. kava, fr. kao, kav ‘cellar, cave’, fr. Fr. cave ‘cellar’ (Lat. cavus ‘hollow’, ef. Sp. cavar ‘dig’, above). Henry 54, 56.
8.23 SPADE
Grk, dyn, oxadgetor(?) Goth. i a. kasiklis = drvapt, mwarédrvapo ON pall, reka ae ee Z t. pala Dan. spade Chl. rylo ay lie Sw. spade SCr. aSov, lopata oa i hi OE spadu, pal Boh. _ryé, lopata oe ; yy i ME spade Pol. _—rydel Tipe ee lai NE spade Russ, zastup, lopata oe rame, laige Du. spade Skt. khanitra-
Tr, ramhan, laighe OHG - sciwvala(?) Av. kastra- Me pal, rhaw MHG grabeschit ;
r. pal NHG  spaten (grabscheit)
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
4. Goth. graban, OF grafan, et general Gme. : Lett. grebt ‘scrape, hol. low out’, ChSI. po-greti ‘bury’, ete. In *ghrebh-, Walde-P. 1.653 f. Peist 919¢
ME 
=== leaf 550 ->p 526
the same word. sometimes exp (that this was properly a 1, Grk. a a ‘shovel’ is indicated ‘spade’ Be at 76 epyadetov ev @ dpbT- bythe dear and by audpa ‘trench’, Tov ce ut’), prob. : ChSl. jama it, et wee 1.198. Solmsen, os 9 i an, fr. the root of oxarTw, gor, boxagn? ‘dig’ (8.22), 1s the common- est word for a digging tool, but whether ‘spade’, ‘hoe’, OF ‘mattock’ is not clear. In modern Greece the common dig- ging tool has been the roama, a kind of heavy hoe (8.25). For the true spade, only recently introduced, ¢7vap, also and orig. ‘shovel’ (8.24), is commonly used. But a more distinctive term has also been coined, namely zarédtvapo, epd. with first part : rar ‘step on, tread’, hence ‘shovel that one pushes with the foot’, an excellent description. Ci. Russ. zastwp (below, 6). ; Gl, Mozpoy is often translated eee but was some kind of a Od. 22455 and rvinn Gee. Hom. pov Ditt. Syll. ), the source of NG slide’ (10.42). Prob. : eo: Up, level off”. Walde-P. oh : Mihl.-Endz. 2.490, (8.24) Bags more persistent iT. “pag-sla- : pangere Meee 8 SK in’. Gre via, Emout-M, 793° 77UHE Bix’, with oe fr. late Lat. vanga § ssbar’, a loanword He ee (Gme.2) r ut source * 4drnout-M. 1072.
2879, Bo
» Lat, Be ‘shovel’
Weertain REW 9137
CULTURE, VEGETATION
igitized by Arya Samaj Foundation Chennai and eGangotri
499
Fr. béche, OF r. besche, back-formation fr. OF r. beschier ‘dig up’, deriv. of a bessos ‘hoe’, Fr. dial. besse, this fr. a VLat. *bissus ‘double’(?). Wartburg 1.381, 382f. Gamillscheg 9
```


## [2026-09-06T22:52:34.462Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"yaxšti\\|yaxsti\\|yasti-\\|yasti\\b\" SYN.txt | head -20\necho \"=== STICK section ===\"\ngrep -n \"STICK\\|STAFF\\|POLE, POST\\|CLUB\" SYN.txt | head -20",
 "description": "Search Buck for stick/staff section"
}
```


### [2026-09-06T22:52:34.529Z] TOOL RESULT

```
13237:gkt, oaya : ChS. véja, etc. (above, 7). Ae yarsti- (in epds. pri-yaxsti-, etc.)
13240:VEGETATION 525 = Skt. yasti- ‘staff, stick’, root connec- tions dub. Walde-P. 1.443. Barth. 809, 1236.
=== STICK section ===
34634:as- ‘throw’. Uhlenbeck 19. Walde-P. | 298 ff. Macdonell-Keith, 2.591 f. with 1.134. refs. Geiger, Ostiranische Kultur 441 ff. 20.22 CLUB Grk.  pdradov, kopbyn, EbAov Goth. (¢riu) Lith. kuoka, kilé NG  pérado, parcobxa ON klumba, klubba, kylfa, Lett. vale Lat. clava, fistis rudda ChSl.  dritkolt It. mazza Dan. ikfélle SCr.  buzdovan Fr. massue Sw. klubba Boh. _ palice, obuSek Sp. porra OE sdagol, cycgel Pol. patka Rum. mdciucé ME _clubbe (kuggel) Russ. bulava, dubyna ir. lorg NE club (cudgel) Skt. vadha-, vadhar, gada- Nir. —_ lorg, lorgaid Du. knots Ay. vazra-, vadar, gasa- W. wb OHG = kalbo Br. bataraz MHG kolbe, kiule NHG keule
```


## [2026-09-06T22:52:36.816Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13200,13250p' SYN.txt",
 "description": "Read Buck p.525 branch section"
}
```


### [2026-09-06T22:52:36.869Z] TOOL RESULT

```
3. Lat. ramus (> It., Sp. ramo, or, as orig. coll., It., Sp. rama; dim. forms > Fr. rameau, Rum. ramurd) : radix ‘root’, etc. (8.54). Ernout-M. 849. REW 1033, 7055.
Fr. branche (> ME braunche, NE branch; also Norm. Fr. form > Br. brank), fr. late Lat. branca ‘paw of an animal’ (> Rum. dbrincd, It. branca
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
im eeeees
SSRN
524. SELECTED INDO-EUROPEAN SYNONYMS
nae
ms : <000 ood » 3 melt pth dete itp aS
BY }!
- ‘paw, claw’), orig.? REW 1271. Wart- burg 1.498. Gamillscheg 139 f.
Rum. cracé, fr. Slavic, cf. Bulg. krak, kraka ‘leg, foot’, SCr. krak ‘long leg’, etc., also in ChSI. dligo-krakiu ‘sort of insect’ (lit. ‘long-leg’). Tiktin 429. Ber- neker 571 f.
4, Ir. craib, NIr. craobh (also a ‘tree’, as in Gael.), etym.? Macbain 104.
Ir. gésca, géc, NIr. géag, W. cangen, caine, Lith. Saka, Russ. suk (ChSI. sqkit ‘twig’, Boh. suk ‘knot’ in wood), Skt. gakha-, Arm. car: Skt. cafku- ‘peg’, Lith. Saknis, Lett. sakne, OPruss. sagnis ‘root’, Goth. hoha, Ir. cécht ‘plow’ (forked stick’), etc. Walde-P. 1.335. Pedersen 1.126, 494.
Br. barr ‘top’ (12.83), also ‘branch’ (as ‘tip’, cf. Du. tak, below, 5).
Br. brank, fr. a dial. form of Fr. branche (above, 8).
5. Goth. asts, OHG ast, etc., above, 1.
ON kvistr, mostly ‘small branch, twig’ (Dan. kvist, Sw. qvist ‘twig’), ME twist, twyste (cf. NED s.v.), cf. ON hkvisl ‘fork, branch’ (of a river, etc.), fr. Gmc. twis- (Goth. twis- ‘apart’), IE *dwis in Lat. bis, early Lat. duis ‘twice’: IE dwou- ‘two’ (cf. below, OE twig, etc.). Walde-P. 1.820. Falk-Torp 607 f.
ON grein, Dan., Sw. gren: Sw. gren ‘fork between two branches’, Sw. dial. grena ‘spread the legs’, MHG griten, id., Goth. grips ‘step’, etc., connections out- side Gmc. uncertain, but semantic development clearly ‘fork, angle’ > ‘branch’. Falk-Torp 345. Walde-P. 1.652.
OE itelga, OHG zwelge (with zw- for z fr. zwig), MHG zelge, zelch (ON talga ‘thin limb, long arm’, rare) : ON telgja ‘whittle’, Ir. dlongim, dluigim ‘split’,
Lith. dalgis ‘scythe’. Walde-P. 1.812. Falk-Torp 1252.
OE bag, boh, ME bow(e), NE bough, same word as OE bég ‘shoulder’ : OHG
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
buog ‘shoulder’, Skt. bahu-, Gri. 7
‘ ? Xus arm’, etc. (4.31). Early ang usual specialization to ‘bough’ of a tree. NED s.v. bough, sb.
OE twig, twigge (ME, NE twig ‘smal] branch, twig’, but in OR general ‘branch’, cf. Gospels, Mk, 13.28, Mt. 24.32, of the branches of the fig tree also Jn. 12.13 palm-treowa twigu), Dit twijg, OHG zwig (mostly ‘twig’, of. Graff 5.729; but also ‘branch’, ef, Tatian 116.4, 5), MHG zuice (likewise mostly ‘twig, sprout, cutting’), NHG 2weig, all derivs. of IE *dwi-, *dwei-- *dwou ‘two’, like ON kvistr, etc., above. Here also OHG zuog, OS tg, with vowel from the numeral. Walde-P. 1.819, Note the opposite tendencies of usage in Eng- lish (‘branch’ > ‘twig’) and German (‘twig’ > ‘branch’).
ME braunche, NE branch, fr. Fr, branche (above, 3).
Du. tak, fr. MDu. tacke, tac ‘point, branch’ = MHG zacke, NHG zacken ‘point, prong’, NE tack, etc. root con- nection dub. Franck-v. W. 685. Walde-P. 1.785.
6. Lith. Saka, above, 4.
Lett. zars, prob. : Lith. Zaras ‘beam of light’ (Lalis), Zéréti ‘shine, glitter’, ete. Cf. the opposite semantic development in OE beam, NE beam for ‘beam of light’ (NED s.v.19). Miihl.-Endz. 4.691.
7. ChSl. vélvi, Boh. vétev, Russ. velv’ : Lith. vytis ‘osier’, Lett. vitvols, OPruss. witwan, ON vidir, OHG wida ‘willow’, etc., formations of IE *wei- in ChSl. vé&ja, Skt. vayd- ‘branch’, Ir. fé ‘rod, measuring-rod’, Lat. viere ‘plait, Wealey Lith. vyti ‘twist’, ChSl. vité ‘wind, twist, ete. Jokl, Arch. sl. Ph. 29.44, Walde-P. 1.224, 225.
SCr. (Bulg., Slov.) grana, Ukr. hranok (Russ. granka ‘tuft, wisp’) : Russ. gra” ‘facet, limit’, granica ‘frontier’, Pol.
4 ‘beard '496, Berneker 346.
es h. “haluz, Ukr. hdtudz, oe liu, a *galq-2t : ae puss “Oy ‘bough’ Boh. hil ‘staff, gol fa (r m. kolr ‘branch’, root con-
Briickner
+t etC.y en Berneker 292, 326. D
3, oe suk, above, 4, g, Skt. cakha, above, 4
gkt, oaya : ChS. véja, etc. (above, 7). Ae yarsti- (in epds. pri-yaxsti-, etc.)
AGRICULTURE, ’ ll t rer. edge, etc., a _ hear e tpoint’ : ON gren, potio i ‘bearded’,
igitized by Arya Samaj Foundation Chennai and eGangotri
VEGETATION 525 = Skt. yasti- ‘staff, stick’, root connec- tions dub. Walde-P. 1.443. Barth. 809, 1236.
Av. frasparaya-, lit. ‘that which shoots forth’ (epd. of fra = Skt. pra, and sparaya : Skt. spurj- ‘burst forth, roar’) and fravazs- (cpd. of fra and vazés- ‘srow’) in this sequence, Yasna 10.5, are taken as ‘branch’—‘twig’ by Darmesteter and Mills (also frasparaya rendered by cakha- in Skt. translation), but as ‘twig’—‘stem, branch’ by Barth. (fras- paraya- rendered by spik ‘twig’ in Pah- lavi translation). Barth. 991, 1003.
8.56 LEAF
$iddov Goth. Jlaufs Lith. Jlapas
"taro ON laufsblad (lauf, blad) Lett. lapa folium Dan. _ blad (I¢v) ChSl.  listit foglia Sw. blad (laf) SCr. list feuille OE léaf (bled) Boh. list
.  hoja ME _leef Pol. lise
. frunzd (foate) NE leaf Russ. list duille Du. . blad (loof) Skt. parna-, patira- duilleog, bileog OHG  blat, loub Av. varaka- deilen, dalen MHG Dlat, loup
delienn
Words for ‘leaf? are connected with words for ‘bloom, flower’ (orig. ‘swell’?), for ‘peel, strip off’, and for ‘wing, feather’, the last reflecting the notion of lightness, fluttering. os From a root *bhel-, seen also in SS for ‘flower’ (5.57), and perh. ulti- Rv y the same as that in words resting f 4 notion of ‘swell’ (Lat. follis leath- eh a8 ae ‘phallic emblem’, 1 UC), Wal Rut-M. 374 Walden 1 cae Talk op 79, ae ee
Gtk. $6Xop:
: At. foglia, Fr. feuille, Sp. nape a a the last mostly ‘leaf’ of .) Gae eae of grass, ete . 60, Nir. bileog: 3 Be og; ON blad Hea, On ed laufsblas, Dan., Sw. ut rare in this sense,
```


## [2026-09-06T22:52:56.008Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA lazward ===\"; grep -n \"لازورد\\|lāzaward\\|lazward\\|lāžward\\|Lasurstein\\|Lapislazuli\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== AFM ===\"; grep -n \"لازورد\\|اللازورد\" AFM_pages.txt | head -20",
 "description": "Grep Asbaghi and Addi Shir for lazward"
}
```


### [2026-09-06T22:52:56.066Z] TOOL RESULT

```
=== PLA lazward ===
13463:a)             -    läzward:              "Lapislazuli"                        pers.           >.)        lazward         3,
13465:          Lapislazuli:                   Lasurstein,                   blauer        Halbedelstein             pers.             >      ar.       > lat.
13472:          Lasurit:             "blaues              Mineral,            das    den        Lasurstein           od.    Lapislazuli             bildet"
13476:G,»,Y              - lazwardi:                 "lasurblau",
=== AFM ===
878:سطوح ٠‏ زهره لازوردي الاون ورقة طويل ساقة واوراقة مرة ويقال له بالتركية قويون
3605:(اللازورد) 3 0
```


## [2026-09-06T22:52:58.457Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON لاجورد ===\"; grep -n \"لاجورد\\|لاژورد\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20\necho \"=== LKT lasur ===\"; grep -n -i \"lāzaward\\|lazaward\\|lasurstein\\|azur\\b\\|1300\\.\" LKT.txt | head -20",
 "description": "Grep Mo'in and Lokotsch"
}
```


### [2026-09-06T22:52:58.539Z] TOOL RESULT

```
=== MON لاجورد ===
MON_part1.txt:3242:آسمان؛ لاجوردی» کود. مائند آسمان؛ 
MON_part1.txt:32756:پنجرة لاجورد: (کد.) آسمان. مثل پنجرة: 
MON_part1.txt:49427:جادر لاجورد: را 
MON_part1.txt:71395:است از طلا و لاجورد که بر روی عروس 
MON_part1.txt:81270:لاجوردی است. اصل این کونه سوسن از 
MON_part1.txt:91749:طاق لاجوردی: (کد.) آسمان. طاق مدنی: 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3242:آسمان؛ لاجوردی» کود. مائند آسمان؛ 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:32756:پنجرة لاجورد: (کد.) آسمان. مثل پنجرة: 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:49427:جادر لاجورد: را 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:71395:است از طلا و لاجورد که بر روی عروس 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:81270:لاجوردی است. اصل این کونه سوسن از 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:91749:طاق لاجوردی: (کد.) آسمان. طاق مدنی: 
MON_part2.txt:2807:شکفتن گل. غمز؛ٌ لاجوردی: (کد.) نازها و 
MON_part2.txt:11555:(کد.) قاش زین. ه لاجوردی: (کن.) 
MON_part2.txt:18621:آبی فیروزه‌بی باز با لاجوردی پر رنگ بود. 
MON_part2.txt:20268:نیلی» لاجوردی» آسمانی. )1( رنگ آنتم: 
MON_part2.txt:20269:سبر با نبلی» لاجوردی. جامهٌ کبود بوشیدن: 
MON_part2.txt:22649:لاجورد(ی): (کد.) آسمان. کرة وهم‌سوز: 
MON_part2.txt:37754:تکفا لا ور دز حجر لاجورده ححر 
MON_part2.txt:37755:اللاجورد. لاژورد؛ لازورد» لاجسورد 
=== LKT lasur ===
3029:1300.  Pers.  lälä:
3053:JJJJ^_  Pers.  läzwärd : 'Lasurstein,  lasurfarben',  also  'blau' [vielleicht  aus  sskr.  rägävarta,  aus  rägä 'König',  s.  hier  Nr.  1692,  und  ävarta 'Locke,  gekräuseltes  Haar',  also  'Königs- locke', d.  h.  Haarschmuck  des  Königs  ; doch  wird  das  Wort  auch  als  'Quirl- edelstein' gedeutet],  ar.  läzwardi  'lazur- ähnlich';  hieraus  mit  Abfall  des  als Artikel  betrachteten  l  it.  azzurro,  azzuolo 'dunkelblau',  lapis  lazzuli  'Lasurstein', prov.  frz.  azur,  kat.  sp.  pg.  azul,  rum. azur  'blau',  azuriü  'hinnnelblau',  mlat. lazulum  [woraus  mgr.  XaZ:oüp;ov,  \dla- poc];  dtsch.  azur,  Lasur,  lasurblau, ndl,  azuur,  lazuur,  engl,  azure;  russ. lazur ,  bulg.  lazur,  poln.  Cech.  lazur 'das  Himmelblau'.  [DE  229.  Eguilaz 326.    ML  4959.    Gorjajew  180.
5653:iafewi  1327 Zaf  1287 lag^m  1288 JlaÄ;  1295 lakordija  1297 /a/a  1299 Za/^  1300 Zo?o  1299 ?ai<^«  2127 lazur  1311 ie/-*;  2132
```


## [2026-09-06T22:53:09.156Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA context ===\"; sed -n '13450,13485p' incoming/PLA/PLA_pages.txt\necho \"=== PLA page tag ===\"; awk 'NR<13470 && /pdf page/' incoming/PLA/PLA_pages.txt | tail -3",
 "description": "Read Asbaghi lazward entry"
}
```


## [2026-09-06T22:53:10.243Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM context ===\"; sed -n '3595,3620p' AFM_pages.txt\necho \"=== AFM page tags ===\"; awk 'NR<3610 && /pdf page/' AFM_pages.txt | tail -3",
 "description": "Read Addi Shir lazaward entry"
}
```


### [2026-09-06T22:53:10.855Z] TOOL RESULT

```
=== PLA context ===
             s. v.
       al-Mu°arrab                    Ss.       Vs
       Bartholomae                    s.        v.
       Muhit s. v.,                     Addai           Scher           s. v.
lädan                                                                          240                                                                 ladg


©>V - 1ädan:                   "Ladanumt                     pers. >                griech >           lat.
      \

a)         -       läranf:          ägypt.           Ar.     lärang           = ar.        näranf         a. v.      2,


a)             -    läzward:              "Lapislazuli"                        pers.           >.)        lazward         3,
          lazulith:                "Blauspat"              (pers.            ladschuward)              4
          Lapislazuli:                   Lasurstein,                   blauer        Halbedelstein             pers.             >      ar.       > lat.
          lasieren:                mit     Lasur          versehen                   pers.      —>lat.         roman.            us
          Azur:          "das       Himmelsblau,                  Himmelsbläue"                        pers.         Dar.       >frz.        u.
          Azurlejos:                "bunte            (bes.       blaue)            in    Spanien         hergestellte
          Wandfliessen"<                             pers.        >ar.         >».
          Azuri:          Bez.          für     italien.               Sportmannschaften,                     eigentlich          "die       Blauen"
          (nach          der       Farbe        der       Sportbekleidung)                           pers.        > ar. >             it.
          Lasurit:             "blaues              Mineral,            das    den        Lasurstein           od.    Lapislazuli             bildet"
          <T pers.> ar.> lat.                                          >
           %

G,»,Y              - lazwardi:                 "lasurblau",



      Br
     -.
aIy-               lakiyya:             "Lack,         Flüssigkeit,                  die       an   der    Luft      bei       dünnem       Auftragen
          zu       einem       festhaltenden                     Schutzfilm               wird"            hindustan            >> pers,          B>   ar.   6,


=== PLA page tag ===
```


### [2026-09-06T22:53:12.578Z] TOOL RESULT

```
=== AFM context ===
ܘܚܐܘ الرفيع القدر ويطلق على الاك التهار المار وهو كنية عندهم عن ملك الاوك .
وار بعة من 46 دولتهم الثانية لُيَُوا به وهم كيكاوس وكيخسرو وكيتباد وى
هراسب ثم ; بق الغلبة على ܬܝܟ ܨ الدولة الثانية فقيل لهم ܫ
وهو جمع ‏ قي ( البيعان القاطع )
(اتكال) الة معوجة ܝ تهدم 0 ܟܒ 7 فارسّة فاذا صح
ذلك ك1 ادن 1 لشات :0600
+« ( الكلحَة ) كيل معروف لاهل العراق وهى 0 ܝܫܐ 0:00 ܦ
والفارسى ܝ ܨ ܟܝܠܐ :
لكا ) المطكى فارسيّة كنا
05
(اللازورد) 3 0
ال 1 الطرة معرب ليت
ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 +
وبرادفة ܐܐܐܠ 4 (١‏ فرد ܀ \ ) ܕܝܢ 13100 ا 0 صل
< 1 ® ܐܪܝܐ من ܥ ܢ ® طلق 3 على الفك
ܨ
* (اللَج) الياعة الكثيرة ومعظم الماء تعريب 3 وهو اليش البالغ عدده
قات العك قر وتلق @) علي كل ما بلغ عدده مائة الف
([35) .27 ܥ وهو ضرب من الطيوب مر 3 ܨ العود ܕ ܐܫܡ
والمسك واللادن والكافورܒܝ <
(اللاخشة ) الاإطربة وهي طعام كاخيوط من الدقيق . واللاخوشة ܕ )ܪܫܐ
ܬܰܝܨܳܐ رهى .7 اك
15063 21411 30 54890
)1:00 واللكن لغة فيه تعريب لَكَن ومنة السر 0 ܝܐ 6(
والكردي 1:3 ¢ 2
+ ( اللقّازق ) ويقال ثقائق اسم لأحد الأمعاء وبه سي معى | ام ابعشو و ܐܠܨ .
=== AFM page tags ===
```


## [2026-09-06T22:53:22.064Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nupto='\\n'.join(lines[:3605])\nprint('leaf(0-based ff count)',upto.count('\\f'))\nleaves=txt.split('\\f')\nprint(len(leaves))\nimport re\nprint(repr(leaves[upto.count('\\f')][:300]))\nEOF\nhead -3 AFM_pages.txt",
 "description": "Compute AFM leaf for lazaward"
}
```


### [2026-09-06T22:53:23.999Z] TOOL RESULT

```
leaf(0-based ff count) 142
198
'\u202b 1\nܢ ܐܟܟ - + 97 315 355 :انث كك بالقارشئة\nܘܚܐܘ الرفيع القدر ويطلق على الاك التهار المار وهو كنية عندهم عن ملك الاوك .\nوار بعة من 46 دولتهم الثانية لُيَُوا به وهم كيكاوس وكيخسرو وكيتباد وى\nهراسب ثم ; بق الغلبة على ܬܝܟ ܨ الدولة الثانية فقيل لهم ܫ\nوهو جمع \u200f قي ( البيعان القاطع )\n(اتكال) الة معوجة ܝ ته'
8
0
ܥܝ
```


## [2026-09-06T22:53:31.375Z] TOOL CALL #31: Bash

```json
{
 "command": "sed -n 1,80p tools/ref_page.py; ls data/verification/sources/refs/ | grep -i afm",
 "description": "Inspect ref_page.py and AFM files"
}
```


### [2026-09-06T22:53:31.430Z] TOOL RESULT

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
    else:
        print(f"no scan of {abbr} covers printed page {page} (see 'scans' in refs_online.json)"); return 1
    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
    if not os.path.exists(pdf):
        print("PDF not found:", pdf); return 1
    lang = scan.get("lang", "fas")
    out_dir = os.path.join(OCR, abbr + vol)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"{page:04d}")
    png, txt = base + ".png", base + ".txt"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
    if not os.path.exists(txt):
        # try the PDF's own text layer first; fall back to tesseract
        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
        text = r.stdout if len(r.stdout.strip()) > 80 else ""
        if not text:
            env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
            text = r.stdout
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
```


## [2026-09-06T22:53:38.195Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && mkdir -p ocr/AFM && pdftoppm -f 143 -l 143 -r 300 -png -singlefile AFM.pdf ocr/AFM/0141_try143 && ls -la ocr/AFM/",
 "description": "Render AFM page image"
}
```


### [2026-09-06T22:53:45.304Z] TOOL RESULT

```
total 3540
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  6 18:53 .
drwxrwxr-x 12 sfmqrb sfmqrb    4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb 1512597 Sep  5 16:42 0120.png
-rw-rw-r--  1 sfmqrb sfmqrb     598 Sep  5 16:43 0120.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1090365 Sep  5 16:42 0123.png
-rw-rw-r--  1 sfmqrb sfmqrb    1396 Sep  5 16:42 0123.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  992286 Sep  6 18:53 0141_try143.png
-rw-rw-r--  1 sfmqrb sfmqrb    2726 Sep  6 17:24 39.vision.txt
```


## [2026-09-06T22:53:47.306Z] TOOL CALL #33: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/0141_try143.png"
}
```


### [2026-09-06T22:53:48.149Z] TOOL RESULT

```

```


## [2026-09-06T22:53:48.147Z] INPUT

[Image: original 2913x4900, displayed at 1189x2000. Multiply coordinates by 2.45 to map to original image.]


## [2026-09-06T22:54:07.016Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM && mv 0141_try143.png 0141.png && cat > 0141.vision.txt <<'EOF'\n[Addi Shir, Kitab al-Alfaz al-Farisiyya al-Mu'arraba, printed page ١٤١ = 141 (AFM.pdf page 143), read from the page image.]\n\nEnd of باب الكاف, then:\n\nباب اللام\n\n( اللَازْوَرد )  معدن مشهور تعريب لاژورد\n( اللَتُّ )  الفأس العظيمة معرّب لَتّ\n( اللِجَام )  تعريب لِكَام وهو بالارامية ... وبالحبشية leguâm ويرادفهُ اليونانيّ χαλινός (فرنكل ص:١٠٠). وعندي انّ اللفظة ساميّة الأصل وانّما الفارسيّة اخذتها من الارامية ...\n* ( اللُّجّ )  الجماعة الكثيرة ومعظم الماء تعريب لَك ...\n* ( اللَخْلَخَة )  فارسيّتهُ لُخْلَخَه وهو ضرب من الطيوب مركب من العود والعنبر والمسك واللادن والكافور\nEOF\nls -la; echo OK",
 "description": "Save AFM vision transcription"
}
```


## [2026-09-06T22:54:07.130Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T22:54:08.801Z] TOOL RESULT

```
total 3544
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  6 18:54 .
drwxrwxr-x 12 sfmqrb sfmqrb    4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb 1512597 Sep  5 16:42 0120.png
-rw-rw-r--  1 sfmqrb sfmqrb     598 Sep  5 16:43 0120.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 1090365 Sep  5 16:42 0123.png
-rw-rw-r--  1 sfmqrb sfmqrb    1396 Sep  5 16:42 0123.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  992286 Sep  6 18:53 0141.png
-rw-rw-r--  1 sfmqrb sfmqrb     903 Sep  6 18:54 0141.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2726 Sep  6 17:24 39.vision.txt
OK
```


### [2026-09-06T22:54:08.806Z] TOOL RESULT

```


```


## [2026-09-06T22:54:13.873Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%AC%D9%88%D8%B1%D8%AF",
 "prompt": "Give the full Persian entry: etymology of لاجورد / لاژورد (lājvard), Middle Persian forms, any place-name or Sanskrit rājāvarta derivation, descendants (Arabic لازورد, Latin, etc.), and cited sources."
}
```


## [2026-09-06T22:54:15.749Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/azure",
 "prompt": "Full etymology of azure, and of lapis lazuli / lazuli if shown: the Persian, Arabic, Medieval Latin chain, the loss of initial l-, and any mention of Lajward place in Turkestan/Badakhshan."
}
```


### [2026-09-06T22:54:22.117Z] TOOL RESULT

```
# Etymology of Azure

**Origin Chain:** Azure traces back through Old French *azur* (12c.) to Medieval Latin *lazur/lazuri*, which derived from Greek *lazour*, ultimately from Persian *lajward*. The term references "Lajward, a place in Turkestan mentioned by Marco Polo, where the stone was collected."

**Loss of Initial L-:** A crucial linguistic shift occurred when Medieval Latin *lazur* underwent "a false separation" in Old French, as though "the -l- were the French article l'," effectively dropping the initial consonant.

**Lapis Lazuli Connection:** The related term *lapis lazuli* (early 15c.) combines Latin *lapis* ("a stone") with Medieval Latin *lazuli* (genitive of *lazulum*), tracing to Arabic *lazuward*. This blue-hued mineral became the primary pigment source for the color azure in medieval art.

The word's journey reflects trade routes and linguistic evolution across Persian, Arabic, Greek, Latin, and Romance languages, with the color name originating from both a geographic location and the precious stone sourced there.
```


### [2026-09-06T22:54:22.625Z] TOOL RESULT

```
# Persian Entry: لاجورد (lājvard)

## Etymology

The word is "usually considered to be from the place name _لاژورد_ (Lāžvard) in Badakhshan where the stone was mined."

The first component derives from Proto-Indo-European *ǵʰelh₃- ("green"), cognate with Old Irish _glas_.

The second component traces to Proto-Iranian *varta- ("stone"), related to Wakhi _wurt_, Northern Kurdish _ber_, and ultimately Proto-Indo-European *wel- ("to press together").

## Definitions

1. **Mineralogy**: lapis lazuli
2. **Color**: azure (the deep blue of the stone)

## Alternative Forms

- لاژورد (lāžvard, lāžavard)
- لازورد (lāzvard, lāzavard)

## Notable Descendants

**Arabic**: لازورد (lāzaward)
- **Latin**: lazulum, lazurium, azzurum, azura
- **English**: lapis lazuli, azure
- **Italian**: azzurro
- **French**: azur
- **Spanish**: azul
- **Russian**: лазурь (lazúrʹ)

**Turkish**: lacivert (from Ottoman Turkish)

**Sanskrit**: राजावर्त (rājāvarta), लाजवर्त (lājavarta)

## Cited Historical Sources

A 982 CE text, the _Hudūd al-'Ālam_, documents the term: "and in Badakhshan there are mines of silver, gold, ruby, and lapis lazuli."
```


## [2026-09-06T22:54:40.258Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/lathi",
 "prompt": "Give the full English entry etymology for lathi (Hindi लाठी), including Prakrit and Sanskrit yaṣṭi antecedents, dates of borrowing into English, and any cited sources."
}
```


## [2026-09-06T22:54:42.774Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AF%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A4%BF",
 "prompt": "Give the full Sanskrit entry for यष्टि (yaṣṭi): meanings, etymology (any Proto-Indo-Aryan/Proto-Indo-Iranian reconstruction, comparison with Avestan yaxšti-), and descendants (Prakrit, Hindi लाठी)."
}
```


### [2026-09-06T22:54:44.573Z] TOOL RESULT

```
Based on the Wiktionary content provided, I can only offer limited etymological information:

The entry states that "lathi" is "Borrowed from Hindi लाठी (lāṭhī)." However, the webpage does not include details about Prakrit or Sanskrit antecedents, specific dates of English borrowing, or additional scholarly sources beyond this basic etymology statement.

The article references the Oxford English Dictionary but does not elaborate on the fuller etymological chain you've requested. To obtain comprehensive information about the word's progression through Prakrit (yaṣṭi) and Sanskrit origins, along with documented borrowing dates and academic sources, you would need to consult the OED directly or specialized historical linguistics resources.
```


### [2026-09-06T22:54:50.521Z] TOOL RESULT

```
# Sanskrit Entry: यष्टि (yaṣṭi)

## Etymology

**Etymology 1** derives from a probable misreading of इष्टि (iṣṭi), meaning "impulse, seeking, sacrificing."

**Etymology 2** has unknown origins with "multiple unconvincing theories proposed." One theory suggests contamination with लकुट (lakuṭa, "club"), potentially connecting to Ashokan Prakrit *laṣṭi and modern descendants.

## Meanings

The primary sense encompasses "any support": staff, stick, wand, rod, mace, club, or cudgel. Extended meanings include pole, pillar, perch, stalk, stem, branch, twig, sword blade, thread, string, pearl necklace, licorice, sugarcane, and creeping plants.

## Descendants

- **Pali**: yaṭṭhi
- **Marathi**: यष्टी (yaṣṭī)
- **Hindi**: लाठी (lāṭhī)
- **Bengali**: লাঠি (laṭhi)

## Comparative Evidence

The entry notes "late Avestan ẏaxšti" as a cognate, with modern Iranic forms like Pashto laṧta ("rod") likely borrowed from the Prakrit form rather than inherited.
```


## [2026-09-06T22:55:01.378Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB azure ===\"; grep -n -i \"lazuli\\|azure, n\\|^azure\\|azulene\" WEB_vol1.txt | head -10\necho \"=== SKT azure ===\"; grep -n -i \"^AZURE\\|lazuli\" SKT.txt | head -10\necho \"=== FSD azure ===\"; grep -n -i \"az-ure\\|lazward\\|lajward\" FSD_vol1.txt | head -10",
 "description": "Grep Webster, Skeat, Funk-Wagnalls for azure"
}
```


### [2026-09-06T22:55:01.474Z] TOOL RESULT

```
=== WEB azure ===
14451:2. the universal remedy of Paracelsus. — 4-zot/ic, a. pertaining to azote; formed or con- sisting of azote; nitric. [Rare.} A z az’ö-tīite, n. {Gr. a priv., and zdein, to live.) a salt of nitrous acid; a nitrite. = az/6-tize, v.t.; azotized, pl., Pp.: azotizing, Ppr. to impregnate with nitrogen or azote; to nitrogenize. az-6-tom/e-tér, n. [azo-, and Gr. metron, a f measure.] an instrument for measuring the or. ° proportion of nitrogen in a substance; a ni- trometer, s å-zō' tous, a. same as nilrous. i S az-o-ti/ri-a, n. [azo-, and L. urina, urine.) a pathological condition characterized by an excess of nitrogenous matter in the urine. Azrael, n. [Heb. Azsraél, help of God] the angel of death, who, in ancient Jewish and Moslem helicf, parts the soul from the body. Aztec, a. {a native name.] 1. of or pertaining to the Aztecs, a people with an advanced civilization living in Mexico at the time of the Spanish invasion under Cortes in 1519, 2. their language. Az/tec, n. a member of the Aztec people. Az/tec-an, a. 1. Aztec. 2. Nahautlan. aztle’jo (i-thi-la’ho), n. [Sp.] a kind of richly decorated tile. _ A-zam/bre (4-thim/bra), n. [Sp.] a Spanish liquid measure of between two and three quarts. az/are (or a/zure), a. (ME. azure; OFr. azur; LL. azura; Ar. lazivard; Per. lazhward, azure; the initial / lost through confusion with the definite article, Fr. l’, le, etc.] 1. sky-blue; resembling the color of the clear blue sky. 2. cloudless; like the clear sky. azare o ī’zūre), n. 1. the clear blue color of the sky. Her eyes a bashful azure. —Tennyson. 2. any of various blue pigments, as that made of lapis lazuli. 3. the clear sky. [Poet.] 4. the lapis lazuli. (Obs.] 5. in heraldry, blue: in engraving it is rep- resented by parallel horizontal lines, az/are, v.t. to color blue. a-zZu/ré-ous, a. of a clear blue color. az/uare stone, lazulite or azurite. az/a-rine, a. azure. az/i-rine, n. 1. the blue roach, a fish common in Europe. 2. the blue wren of Australia. az/i-rite, n. 1. a blue ore of copper, basic copper carbonate, 2CuCO:Cu(OH)z. 2. a semiprecious gem made from this ore. az/iirn (or a/ziirn), a. of a blue color. [Obs.} az-y-gom/a-tous, a. [Gr. a priv., and sygoun, to yoke.] without zygomatic arches. az/y-g0s, n. in anatomy, an azygous part. a:zy’g0-spore, n. [Gr. a priy., and zygon, a yoke, and sporos, a sowing.] in botany, a par- thenogenetic spore resembling a zygospore. az/y-gous, a. (Gr. azygos, unmatched; a priv., È and zygoun, to yoke.| in anatomy, a term ap- 7 plied to certain parts or organs which have no mates or are not found in pairs, as certain muscles, veins, bones, etc. az/yme, az'ym, n. [Gr. azymos, unleavened; a priv., and symé, leaven. unleavened bread. a-zym/ic, a. pertaining to unleavened bread. Bry me n. in church history, one of a sect ` of Christians who administered the Eucharist with unleavened bread; also, a term applied by the Greeks in the eleventh century to the a, atins. g az/y-mous, a. (Gr. azymos, unleavened; a priv. and symeé, leaven.] unleavened; PELRA
20971:eee Spar; azure spar; lazulite.
105461:lapis lazuli; (a) an azure-blue, opaque, semi- precious stone, a mixture of various minerals; (b) its color, 7
106188:esus: John xi; (b) the diseased beggar in esus’ parable of the rich man and the beg- gar: Luke xvi. 19-31. 7, 2. {often l-] any horribly diseased beggar, especially a leper. la/zir-wort, n. laserwort. | laze, v.i.; lazed, pt., pp.; lazing, ppr. [back-for- mation from lazy.] to be lazy or idle; to loaf. laze, v.l. to spend (time, etc.) in idleness (often with away). > la/zi-ly, eae. in a lazy manner; sluggishly. 1a4’zi-ness, n. the state or quality of being lazy; indisposition to action or exertion; indolence, laz/a-li, n. lapis lazuli. laz’ū-lī finch, a bird of brilliant blue coloring, Passerina amæna, common to western North America. laz/a-lite, n. [from ML. lasulum, azure; and ite.) a glassy, azure-blue mineral, hydrous aluminum phosphate, with varying amounts of iron and magnesium. 1a’zy, a.; comp. lazier; superl. laziest, [Early
=== SKT azure ===
1261:Axure,  blue.  (F.  —  Arab.)  M.E  asur, ature.  —  O.  F.  atur,  ft£ure  ;  a  corrupted form,  standing  for  laxur,  which  was  mis- taken for  I'atur,  as  if  the  initial  /  indicated the  def.  article.  —  Low  L.  iatur,  an  azure coloured  stone,  also  called  laptj  lazuli.^ Arab.  Idjward,  lapis  InzuU,  a  blue  colour. So  called  from  the  mine*  of  Lojwurd,  where the  lapis  tozuU  was  found  (Marco  Pulo, ed.  Yule).
3269:azure.    i^L.)       L.  <^ruUus, Perhaps  for  ctgiuius*,  from
=== FSD azure ===
```


## [2026-09-06T22:55:04.236Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK lakti/yaxsti ===\"; grep -n \"lakti\\|yaxšti\\|yaxsti\\|yaṣṭi\\|yasti-\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt 2>/dev/null | head -20\necho \"=== IEC ===\"; grep -n -i \"^Lakti\\|^L(j)akti\\|Ljakti\\|yasti\" IEC.txt | head -10\necho \"=== WLD band3 register ===\"; grep -n \"lakti\\|yasti\\|yaxsti\" WLD_band3.txt | head -10",
 "description": "Grep Pokorny, Mann, WLD index"
}
```


### [2026-09-06T22:55:04.325Z] TOOL RESULT

```
=== POK lakti/yaxsti ===
POK_full.txt:68154:Lithuanian plaku, plakti^hW, chastise, castigate', plokisxw. 'Rutenstreich'; Old Church 
=== IEC ===
=== WLD band3 register ===
```


## [2026-09-06T22:55:17.904Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON context ===\"; sed -n '37745,37765p' MON_part2.txt\necho \"=== BQT v3 ===\"; grep -n \"لاجورد\\|لاژورد\\|لازورد\" incoming/BQT/BQT_v3_pages.txt | head -20",
 "description": "Read Mo'in lajvard and grep Borhan v3"
}
```


### [2026-09-06T22:55:17.971Z] TOOL RESULT

```
=== MON context ===
در طبقات سنگ‌های دگرگونی شدة زمین 
یافت می‌شود. چون سختی جالب توجه (در 
دود سسختی ششه) و رک تین 
خوشرنگی دارد در جواهرسازی به عنوان 
نگین انگشتری بکار می‌رود. همچنین آن را 
کوبیده بصورت گرد (پودر) درمی آورند و 
به عنوان رنگ آبی در نقاشی بکار می‌بر ند 
و در لباسشویی هم جهت خوش رنگ 
کردن پارچه‌های سفید بکار برده می‌شود؛ 
تکفا لا ور دز حجر لاجورده ححر 
اللاجورد. لاژورد؛ لازورد» لاجسورد 
نشف لاخوود کاس رم کونهاي 
لاجورد معدنی که از تجزیه و تخریب 
سنکت لا جورد در برخی معادن تا فتکت 
کاشان و قم لش ی ان اب کون 
لاجورد نرم و شیه خاک‌های رستی است و 
سختی اولی خود رابه کلی از دست داده 
است و در بازار نیز بنام لاجورد عر صه 


۲ ۵ ۱ 
=== BQT v3 ===
294:لاجورد. بمعنی شابود است که هاله وطرقوخرمن
721:‏شادودد ۴ بر وزن لاجورده بسمنی
1770:‏شاه ورث ۴ - بروزن لاجورده بمعنی
1927:بر وزن لاجورد » بمعنی
6617:خبز خوانند ۴ - و لاجورد کم رنگگ ‎Ny‏
10310:‏طاق یلو فر ی = بسنیانلاجوردی
10438:‏است ۳ , وآ نکلی ‎ath‏ لاجوردی و دراز شکل
13470:بروزن آفت ‎IS‏ است لاجورد رنگه و(۲) دراز
28285:باتی است ‎nh‏ ذرعی و ساق و بر کش باريك و ‎AS‏ لاجوردی است و
31154:‎gine gag PIES‏ کرلاجورد
32893:نیز هست که کل آن لاجوردی میشود.
49655:لاجورد هم میگویند .
49657:‏لاچوردی سقف © بمعنیلاجوردی
49660:‏لاچور دنه خم یمعنی لاجوردی
49691:1 * لاژوزد > لازورد ( ممرب ) ‎lazulite = lazuli‏ ( فر ) ‎٩-۲ ces yy‏
49692:« لازورد © . ۲ - ام هندی هبل است « فپرست مخزن‌الادوبه » س آلاچی«لمت ‎Maal‏
49829:و ممنی لاجورد است و آن سنگی است کبود که
49831:که ‎Ly‏ او ساقط شود نیم درم لاجورد راباروفن
49861:عمج‌البلدان . ۲ رك : لغت نامه . ۷ = لاجورد ‎(ee)‏
50129:عنبر و مشك وسپند سوخته و لیل ولاجورد که
```


## [2026-09-06T22:55:19.459Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC lakti ===\"; grep -n -i \"lakti\\|ljakti\\|iakti\" IEC.txt | head\necho \"=== AHD watkins ===\"; grep -n -i \"lazuli\\|azure\" AHD_watkins1985.txt | head\necho \"=== ARY لاجورد ===\"; grep -n \"لاجورد\\|لاژورد\" incoming/ARY/ARY_pages.txt | head",
 "description": "Grep Mann, Watkins, Aryanpur"
}
```


### [2026-09-06T22:55:19.531Z] TOOL RESULT

```
=== IEC lakti ===
9447:lakstis, à (lakt-) ‘stick, stem, branch, bar. Cf. variant slaKtis Prakritic, Pali latthi ‘stick’ (cf. Skt. lakutah *cudgel); Arm. laxt, Let ‘stick; cudgel’; Gk. laktis, gs -os, f. ‘pestle’; Alb. las&, Ilasë ^wash- ing-stick'; Sw. läckt, pl. -er, m. ‘stick, slat, lath’; Blg. lost, m. Char, bolt. LW in Mod. Gk. lostós, id.); Li. lakstà, laktà ‘perch’; Latvian laksts, m. ‘shoot, sucker’ beside lakta “perch?
9512:làt- (1) (?) (lata, latis) ‘lath, stave’. Cf. lak- stis, slaktis Lat. làta (ath. For *lata assula Ainsworth); Pol. 1ata (2), id.; Cz. lat', f. id.; Li. Jotà, id. (The background of OE lætt; ME laththe, OHG latta, beside MHG lade, laden, all in ` sense of ‘lath’, is obscure. It. latta, Fr. latte are fr. Gmc. W llath & Ir. slat, f., Olr. slatt derive from a type *slaktis, q. v.)
9516:latis ‘rod, iath’, etc. See lät- (1) and cf. lak- stis, slaktis. WP II, 443 | (Ir. lait, f. ‘ʻa land-measure, 172 yds’, but OE 1260, ON láð, LLat. leta, fr. Gmc. represent a type *létà)
12993:plakstið (plaktið, plaksið) ‘slap, bang’. Cf. plak-, plaks-, etc. Variant plaksko
13003:plaktos, is, ios, iə “blow, bang’. Cf. plak-, plaks-, etc. Alb. plasë, f. (crack, chink, burst, bang’, fr. *plaktio); Icel. cf. fletta, v. ‘strip’; Sw. flättja, f. (“frivolity?: Alb. plasë) beside (LW fr. LG) Sw. fläkt ‘breeze’; Li. plaktas, m. ‘hammer’; plakte, f. ‘thrashing’
=== AHD watkins ===
=== ARY لاجورد ===
```


## [2026-09-06T22:55:35.078Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%D8%A7%D8%AC%DB%8C%D9%86/",
 "prompt": "What do the Persian dictionaries (فرهنگ معین, لغت‌نامه دهخدا) say about لاجین (lâjin)? Is it a Turkish word/name, a tribe name, a personal name, or 'falcon'? Quote the entries."
}
```


## [2026-09-06T22:55:36.204Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=lapis+lazuli",
 "prompt": "Give the American Heritage Dictionary etymology for lapis lazuli (and azure if present): the Latin, Arabic, Persian chain."
}
```


### [2026-09-06T22:55:41.254Z] TOOL RESULT

```
# Lapis Lazuli Etymology

According to the American Heritage Dictionary, the word traces back through this linguistic chain:

**"Latin _lapis_, stone + Medieval Latin _lazulī_, genitive of _lazulum_, lapis lazuli (from Arabic _lāzaward_, from Persian _lājward_)."**

The entry shows the term's journey: Persian *lājward* → Arabic *lāzaward* → Medieval Latin *lazulum* → combined with the Latin word for stone (*lapis*) to form the complete phrase in Medieval Latin.

The dictionary does not provide an etymology for "azure" in this entry.
```


### [2026-09-06T22:55:43.279Z] TOOL RESULT

```
Based on the webpage content provided, I can only find one definition for لاجین (lâjin):

**"قبیله ایست از ترکان نواحی بلخ"** (It is a tribe from the Turks of the Balk region)

The page does not include entries from فرهنگ معین (Farhang-e Moein) or لغت‌نامه دهخدا (Dehkhoda Dictionary) for this term. While the website mentions these dictionaries as part of its available resources, their specific definitions for لاجین are not displayed in this content. According to what's shown, the term refers to a tribal group rather than being a personal name, falcon, or standalone word.
```


## [2026-09-06T22:56:00.780Z] TOOL CALL #46: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%AC%D9%88%D8%B1%D8%AF' --note 'page 301, root Lajin/lajvard: Persian lājvard etymology (place-name in Badakhshan), descendants Arabic lāzaward > Latin > azure' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/azure' --note 'page 301, node #3/#4: azure < OF azur < ML lazur < Pers. lajward; loss of l- as French article; lapis lazuli' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%AF%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A4%BF' --note 'page 301, entry 4 nodes #1/#3/#4: Sanskrit yaṣṭi, unknown origin, Av. yaxšti cognate, Hindi लाठी descendant' ; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%84%D8%A7%D8%AC%DB%8C%D9%86/' --note 'page 301, root: لاجین = a Turkic tribe of the Balkh region (Dehkhoda)' ; python3 tools/fetch_source.py 'https://www.ahdictionary.com/word/search.html?q=lapis+lazuli' --note 'page 301, node #2/#3: AHD etymology lapis lazuli < ML lazulum < Arabic lāzaward < Persian lājward'",
 "description": "Archive web sources"
}
```


### [2026-09-06T22:56:05.700Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/99fe23bd844c35b4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f77e16d0f30789b0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bae91eabfe459dda.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d762aace69b42b88.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06c6b710c62c2a70.txt
```


## [2026-09-06T22:56:09.639Z] TOOL CALL #47: Bash

```json
{
 "command": "pdftoppm -f 301 -l 301 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg301 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 301"
}
```


### [2026-09-06T22:56:12.055Z] TOOL RESULT

```
total 127548
drwx------ 7 sfmqrb sfmqrb    12288 Sep  6 18:56 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   774972 Sep  6 18:54 afm143.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1046357 Sep  6 18:54 afm144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      980 Sep  6 18:55 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    26688 Sep  6 18:20 ary377_bot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71464 Sep  6 18:20 ary377_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71267 Sep  6 18:19 ary378_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25966 Sep  6 18:19 ary378_top_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332775 Sep  6 18:33 bqtv2_289_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9689 Sep  6 18:33 bqtv2_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   726576 Sep  6 18:33 bqtv2_n289.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb    28249 Sep  6 18:25 build290a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63778 Sep  6 18:33 build290b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68833 Sep  6 18:30 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2612 Sep  6 18:28 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13418 Sep  6 18:28 c_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8430 Sep  6 18:28 c_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11245 Sep  6 18:28 c_katrang.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6717 Sep  6 18:28 c_katvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28872 Sep  6 18:28 c_katvar_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18514 Sep  6 18:52 crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14732 Sep  6 18:27 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    51742 Sep  6 18:33 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50446 Sep  6 18:33 mk292b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41011 Sep  6 18:29 mk294.py
-rw-rw-r-- 1 sfmqrb sfmqrb    45170 Sep  6 18:47 mk297.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67312 Sep  6 18:51 mk298.py
-rw-rw-r-- 1 sfmqrb sfmqrb    44967 Sep  6 18:51 mk299.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50897 Sep  6 18:54 mk300.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:33 p290
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:53 p295
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:49 p296
-rw-rw-r-- 1 sfmqrb sfmqrb     9447 Sep  6 18:41 p297_av2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8787 Sep  6 18:41 p297_cav.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2803 Sep  6 18:41 p297_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8189 Sep  6 18:41 p297_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5216 Sep  6 18:55 p303_n18b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7082 Sep  6 18:55 p303_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7046 Sep  6 18:55 p303_n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28862 Sep  6 18:27 pg289_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91779 Sep  6 18:26 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   187988 Sep  6 18:19 pg290hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36312 Sep  6 18:20 pg294_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77133 Sep  6 18:28 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56184 Sep  6 18:39 pg296.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130247 Sep  6 18:41 pg297hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60960 Sep  6 18:39 pg298.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99543 Sep  6 18:52 pg299hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61588 Sep  6 18:56 pg301.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122418 Sep  6 18:55 pg303hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89589 Sep  6 18:52 pg303.png
-rw-rw-r-- 1 sfmqrb sfmqrb   132637 Sep  6 18:38 sns_n155.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129771 Sep  6 18:38 sns_n156.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   130970 Sep  6 18:38 sns_n90.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   531356 Sep  6 18:38 sns_n90_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   124445 Sep  6 18:38 sns_n92.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   522585 Sep  6 18:38 sns_n92_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   495290 Sep  6 18:38 sns_n92_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   351684 Sep  6 18:35 tad_n59.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   342929 Sep  6 18:35 tad_n59_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   242025 Sep  6 18:34 tad_n60_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   282364 Sep  6 18:34 tad_n60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   335678 Sep  6 18:34 tad_n60_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   276093 Sep  6 18:34 tad_n61.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332662 Sep  6 18:34 tad_n62.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 18:35 tad_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   265879 Sep  6 18:35 tad_n65_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


## [2026-09-06T22:56:15.899Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg301.png"
}
```


### [2026-09-06T22:56:16.325Z] TOOL RESULT

```

```


## [2026-09-06T22:56:16.323Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:56:26.306Z] TOOL CALL #49: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob,os\nfor p in sorted(glob.glob('data/extracted/batch/page-*.json'), key=lambda x:int(x.split('-')[-1][:-5]))[:400]:\n    pg=int(p.split('-')[-1][:-5])\n    d=json.load(open(p))\n    for i,e in enumerate(d['entries']):\n        for n in e.get('nodes',[]):\n            if not n.get('words') and n.get('lang') is None:\n                v='data/verification/page-%d.json'%pg\n                if os.path.exists(v):\n                    vd=json.load(open(v))\n                    for ve in vd['entries']:\n                        if ve.get('entry')==i:\n                            for vn in ve['nodes']:\n                                if vn['id']==n['id']:\n                                    print(pg,i,n['id'],vn.get('verdict'),'|',vn.get('derivation','')[:200])\nEOF",
 "description": "Find how empty nodes were verified before"
}
```


### [2026-09-06T22:56:28.106Z] TOOL RESULT

```
62 0 5 unverified | An empty pass-through box. The printed page (pdf p. 62, rendered at 450 dpi) really does show a blank rectangle drawn to the right of the 'Avestan arânte / aram, arem' box, with the connecting arrow, 
80 1 2 unverified | There is nothing to verify: the printed page really does show an empty box here. On the rendered page (pdftoppm -r 200 of pdf p.80, saved as data/verification/sources/refs/ocr/BOOK/80.png) the box to 
86 0 2 unverified | Pass-through/empty node: on the printed page (book p. 56 = pdf p. 86) an arrow leaves the Avestan box and ends in a large box that is completely blank — no language header, no word, no reference. The 
95 1 5 confirmed | Empty box. On the printed page (pdf 95, book p.65) an arrow leaves the Old Persian box and ends in an empty framed box in the Persian column, with no language label, no reference and no words — the Pe
121 0 9 unverified | An empty box: on the printed page (pdf 121 = book p.91) the arrow out of the Old Persian box points to a rectangle with no language label, no reference and no words — a layout artefact of Nourai's cha
137 0 6 unverified | There is nothing to verify: on the printed page (p.107 = pdf 137) the box hanging to the right of the Old Persian box is a completely EMPTY double-ruled rectangle — no language label, no reference, no
171 0 5 unverified | Empty pass-through box: on the printed page (pdf p. 171) the box to the right of 'Avestan / Old Persian zana 1' is drawn but contains no language label and no words, so there is no derivation to check
180 0 12 unverified | A blank box. The printed page (pdf p.180, kept at data/verification/sources/refs/ocr/BOOK/180.png) shows a genuinely empty double-ruled rectangle to the right of the 'Old Persian ud-zma, uzma' box, wi
187 0 2 unverified | There is nothing to verify. On the printed page (book p.157 = pdf 187) the arrow leaving the Avestan box runs right across the chart into a plain double-ruled rectangle that carries no language label,
189 1 2 unverified | Empty pass-through box: on the printed page (pdf p. 189, book p. 159; see data/verification/sources/refs/ocr/BOOK/189.png) the box to the right of the Avestan box is drawn but left completely blank — 
190 1 4 unverified | A blank double-bordered box that the Avestan node arrows into on the printed page (verified on the 400 dpi render of pdf p.190). It carries no language label and no words, so there is no derivation cl
192 0 20 unverified | A completely blank rectangle to the right of the second Avestan box (âzŭtay, zav 2), reached by an arrow from it on the printed page (checked on the page image). It has no language header and no words
193 0 6 unverified | An empty box hanging off the Avestan node on the printed page (top right of the first tree; no language label, no words; see the archived page image data/verification/sources/refs/ocr/BOOK/193.jpg). I
203 0 2 unverified | Empty pass-through box. On the printed page (pdf p. 203, book p. 173; see data/verification/sources/refs/ocr/BOOK/203.png) the large rectangle to the right of the Avestan/Old Persian box is drawn but 
203 2 2 unverified | Empty pass-through box: on the printed page (data/verification/sources/refs/ocr/BOOK/203.png) the rectangle to the right of the Avestan box in the Gwadh chart is drawn but left blank — no language, no
204 3 2 unverified | An empty pass-through box: the printed page (PDF 204) shows a blank rectangle drawn to the right of the 'Old Persian gabawo' box, with no language label, no reference and no word in it — evidently a s
206 0 7 unverified | Empty box. The printed page (PDF p.206 = book p.176, image copied to data/verification/sources/refs/ocr/BOOK/206.png) shows a wide rectangle to the right of the žayâi box with no language label, no re
206 1 2 unverified | Empty box. On the printed page (book p.176 / PDF p.206, image at data/verification/sources/refs/ocr/BOOK/206.png) the frame to the right of the ni-γrā-ire box is drawn but blank — no language, no refe
207 1 2 unverified | Empty pass-through box. On the printed page (pdf p. 207, book p. 177; see data/verification/sources/refs/ocr/BOOK/207.png) the wide rectangle to the right of the Avestan box in the Gwelbh chart is dra
210 0 7 unverified | An empty box. On the printed page (p. 180) the box to the right of 'Old Persian | gar: to devour' carries no language label, no word and no reference — it is a blank continuation cell of the chart's g
214 0 21 unverified | Blank box in the printed chart (p.184), drawn to the right of the Old Persian ni-kan/vi-kan box with an arrow from it; it carries no language label or word. Nothing to verify. The box was missing from
224 1 4 unverified | A completely blank box on the printed page (page 224 of the PDF, book p.194): no language header, no reference, no word — only the empty rectangle, drawn to the right of the Avestan pronoun box #3. Th
224 1 11 unverified | A blank box on the printed page — a narrow empty rectangle to the right of the Avestan a-tāra box, with no language header, no reference and no word. The extraction is faithful; there is nothing to ve
227 0 7 unverified | An empty box. On the printed page (pdf 227 = book p.197, copied to data/verification/sources/refs/ocr/BOOK/227.png) the arrow leaving the third Avestan box runs right across the chart into a plain dou
231 0 6 unverified | There is nothing to verify: on the printed page (PDF p. 231 = book p. 201, image saved at data/verification/sources/refs/ocr/BOOK/231.png) the box to the right of the 'čanah, činah, činman' box is dra
234 4 10 unverified | Blank box in the printed chart (p.204), drawn to the right of the Avestan čagad/čageman/čagvah box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the ext
248 0 5 unverified | Empty pass-through box: the chart draws an arrow from the Avestan box to a framed rectangle that carries no language label, no reference and no words. The printed page confirms this is how the book it
249 2 5 unverified | An empty pass-through box hanging from the (mis-labelled) 'Old Persian queke'. Because its parent is in fact Old Prussian queke, whose only relatives are Latvian caka 'knobbed cudgel' and, per Walde-P
263 0 8 unverified | An empty box in the printed chart: the rectangle to the right of the Avestan čevîšî node carries no language label, no word and no reference (confirmed on the page image, site/pages/263.jpg). Nourai's
263 0 10 unverified | A second empty box in the printed chart, drawn to the right of the mislabelled 'Old Persian' node and carrying no language, word or reference (checked on the page image). As with node 8 the box was ne
264 0 5 unverified | Empty pass-through box: on the printed page (site/pages/264.jpg) an arrow runs from the 'Old Persian caune' box to a blank framed box at the right margin with no language label, no reference and no wo
267 0 7 unverified | Blank box in the printed chart (p.237), drawn to the right of the Avestan zî / nôit-zî box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extraction 
269 0 2 unverified | Empty box. The printed page (pdf 269, book 239) really does show a blank rectangle to the right of the Avestan box, joined to it by an arrow, with no language label, no reference and no word — see dat
270 0 10 unverified | An empty box on the printed page (checked on the 300-dpi render, copied to data/verification/sources/refs/ocr/BOOK/270.png): the rectangle drawn to the right of the Pahlavi du-srav box carries no lang
272 0 5 unverified | Empty pass-through box: on the printed page an arrow leaves the 'Old Persian slaunis' box and ends in a wide, completely blank rectangle to its right (verified on the 200 dpi render of pdf page 272). 
275 6 2 unverified | Blank box in the printed chart (p.245), drawn to the right of the Avestan srî/srîra/sra-yah box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extrac
276 2 21 unverified | Blank box in the printed chart (p.246), drawn to the right of the Avestan xrŭ/xrŭra/xrŭždra box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extrac
279 1 2 unverified | An empty box on the printed page: on the 200/600-dpi render of pdf page 279 (copied to data/verification/sources/refs/ocr/BOOK/279.png) a wide, completely blank rectangle is drawn to the right of the 
286 4 5 unverified | An empty box. On the render of pdf page 286 (200 dpi, copied to data/verification/sources/refs/ocr/BOOK/286.png) a wide blank rectangle is drawn to the right of the 'Old Persian kupsins' box, joined t
288 7 2 unverified | An empty box, and empty in the printed book too: pdf p.288 (book p.258) shows a plain rectangle to the right of the Avestan box with no language header, no reference and no word, joined to it by an ar
288 7 4 unverified | The second empty box, again blank on the printed page: a rectangle to the right of the Old Persian box, no language header, no reference, no word, reached by an arrow from Old Persian. Nothing to veri
289 1 7 unverified | An empty box, empty in the printed book too: the render of pdf p.289 (200 dpi, copied to data/verification/sources/refs/ocr/BOOK/289.png) shows a wide blank double-ruled rectangle to the right of the 
289 1 10 unverified | A second empty box, blank on the printed page as well: on the render of pdf p.289 a plain double-ruled rectangle stands to the right of the 'Pahlavi pari-sp' box, joined by an arrow, with no language 
289 1 12 unverified | The third empty box on this chart, blank in the book as well: on the render of pdf p.289 a plain rectangle stands to the right of the 'Avestan kaěš / fra-kaěš, vi-kaěš' box, joined by an arrow, with n
298 0 8 unverified | An empty box, empty in the printed book as well: the 200-dpi render of pdf p.298 (copied to data/verification/sources/refs/ocr/BOOK/298.png) shows a wide blank double-ruled rectangle at the right of t
298 0 10 unverified | A second empty box, blank in the printed book too: the render of pdf p.298 (data/verification/sources/refs/ocr/BOOK/298.png) shows a wide double-ruled rectangle to the right of the 'Old Persian KNT:20
```


## [2026-09-06T22:57:11.642Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN ===\"; grep -n -i \"lāzward\\|lazward\\|lajward\\|läzward\\|lâjvard\\|lazur\" HRN.txt | head\necho \"=== HUB ===\"; grep -n -i \"lazward\\|läzward\\|lazur\\|lajward\" HUB.txt | head\necho \"=== TTS lacin ===\"; grep -n -i \"lačin\\|lacin\\|laczin\\|lätschin\\|Falke\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -10\necho \"=== RCH ===\"; grep -n -i \"lajward\\|lazward\\|lajwardi\" RCH.txt | head",
 "description": "Grep Horn, Hübschmann, Vámbéry, Richardson"
}
```


### [2026-09-06T22:57:11.752Z] TOOL RESULT

```
=== HRN ===
=== HUB ===
=== TTS lacin ===
1500:thun.  So  uig.  cag.  alkus=^  ein  Falke  mit  röthlichem  Ge- 
=== RCH ===
```


## [2026-09-06T22:57:23.294Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"lacin\\|laczin\\|latschin\\|lačyn\\|lakin\\|lâcin\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -10\necho \"=== BQT v3 lajvard entry ===\"; sed -n '49685,49700p' incoming/BQT/BQT_v3_pages.txt; echo \"-----\"; sed -n '49820,49840p' incoming/BQT/BQT_v3_pages.txt",
 "description": "Grep Vámbéry and read Borhan v3 lajvard"
}
```


### [2026-09-06T22:57:23.370Z] TOOL RESULT

```
=== BQT v3 lajvard entry ===
‏۴ - بر سرلور عشق بینی تاج ابر آن دم که عشق بینی لاج .

‏مولوی بلخی رومی . مثنوی « لفت نامه * .
‎ya 6۵‏ لاء :
نمی ترسم ز دشمن وز ‎ALS‏ که باشد دشمنش همچون سگه لاج.
مولوی بلخی رومی . مثئوی « لفت نامه ».
1 * لاژوزد > لازورد ( ممرب ) ‎lazulite = lazuli‏ ( فر ) ‎٩-۲ ces yy‏
« لازورد © . ۲ - ام هندی هبل است « فپرست مخزن‌الادوبه » س آلاچی«لمت ‎Maal‏
‏( برهان ‎ab‏ ۳۴۷ )
[pdf page 672]
و۱۸۷

‎Oy = ‘ey‏ شاخ » بمعنی‌جای ومقام
باشد لیکن بدون ت رکیب کفته نمیشود همجو
منگه لاخ و دیولاخ و رودلاخ یعنی جای‌منگه
‎yo ley‏ وجای رودخانه - و بمعنی بسیاروانبوه
-----
نام کوهی است در طبرستان . گویند در آن‌کوه
چشمه است که هرقطرء ای که از ‎OT‏ میچکد
ستکه میکردد ®

‎SY‏ = کون زای فارسی : نام دهی
است از مضافات جام که از دارالملک خراسان
‎Vet‏ .

‏لاژّوده ۷ -با زای فارسی + پر وزن
و ممنی لاجورد است و آن سنگی است کبود که
تفاشان ومصوران بکاربرند . گوبند اگرزنی‌خواهد
که ‎Ly‏ او ساقط شود نیم درم لاجورد راباروفن
زیت آميخته بخود بر کیرد بچه سلامت بماند
تا بظپور آیٌد .

‏لاس م بر وزن طای . ابریشم فرومابه
باشد 4 - و جنسی از ابرشم نیز هت ۸ -
و ابریشم پاك نکرده را هم میگونند ۸ - ومادة
هرحیوانی‌باشد عموماً ‎ey - ٩‏ مادء را گویند
‎Abe‏
```


## [2026-09-06T22:57:37.904Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'NR<49692 && /pdf page/{p=$0} END{}' BQT_v3_pages.txt >/dev/null\ngrep -n \"pdf page\" BQT_v3_pages.txt | awk -F: '$1<49692' | tail -2\ngrep -n \"pdf page\" BQT_v3_pages.txt | awk -F: '$1>49692' | head -2\necho \"=== context above footnote ===\"; sed -n '49660,49692p' BQT_v3_pages.txt",
 "description": "Locate BQT v3 pdf page for lajvard"
}
```


### [2026-09-06T22:57:39.998Z] TOOL RESULT

```
49585:[pdf page 670]
49629:[pdf page 671]
49694:[pdf page 672]
49793:[pdf page 673]
=== context above footnote ===
‏لاچور دنه خم یمعنی لاجوردی
سقف است که کنابه ازآسمان باشد .

‎ge‏ ۷ - بر وزن کاچی , قاقله باشد
‎Je WT,‏ وهیل نیز گوبند و داخل ادوبهُ حاره
در طعامکنند.

‎EY‏ « بروزن ‎Gale ch‏ رشوت است
- و بمعنی برهنه و عربان باشد ‏ - وسگه‌عاده
را یز کویند ۵ ۱
لاچ ‎be‏ جیم فارسی» بمعنی‌بازی وفریب
() چش : لایدن .
‎٩‏ - بلابه گت شبی میرمجلی نو شوم شنم برغبت خوبشش کمین غلام وشد .
‎bile «‏ شیرازی صس ۱۱ > .
۴ از : لاب ( لابه )-یدن ( پسوند مصدری ) ؛ لابه کردن :
بدار دیا چون برفروخت ‎ST‏ ظلم سکار آن بجهنم همی‌خورد چو ظلیم
چوخون ورب بپالوده خیره از مردم بدوزخ اندرلاید که‌خون‌دهندش وریم.
سوزنی سمرقندی ۶ لفت نامه *.
دراوراق مانوی ( پارنی ) ‎PB‏ ( نامیدن . دعاکردن 1 درخواست کردن ‎ )‏ پارسی ‎she‏ (پهلوی)
۵ قاری : لابه ‎(Henning , A list of Middle Persian ... , 8505 , IX,‏
‎ae .) 1, ۲ 4‏ 167-800 , سریکلی ‎lew_am‏ (گفتگ و کردن + سخ نکفتن ) « اسشق

‏۲
‏۴ - دست و زبان بدو ترسد کس را آری بماه بر نرسد لاتو .
فرخی سیستالی « لفت ‎fab‏
‏۴ - بر سرلور عشق بینی تاج ابر آن دم که عشق بینی لاج .

‏مولوی بلخی رومی . مثنوی « لفت نامه * .
‎ya 6۵‏ لاء :
نمی ترسم ز دشمن وز ‎ALS‏ که باشد دشمنش همچون سگه لاج.
مولوی بلخی رومی . مثئوی « لفت نامه ».
1 * لاژوزد > لازورد ( ممرب ) ‎lazulite = lazuli‏ ( فر ) ‎٩-۲ ces yy‏
« لازورد © . ۲ - ام هندی هبل است « فپرست مخزن‌الادوبه » س آلاچی«لمت ‎Maal‏
```


## [2026-09-06T22:57:55.865Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AID lathi ===\"; grep -n -i \"lathi\\|Lattee\" AID.txt | head\necho \"=== WEB lathi ===\"; grep -n -i \"lathi, n\\|la/thi\\|lathee\" WEB_vol1.txt | head\necho \"=== FSD lathi ===\"; grep -n -i \"lathi\" FSD_vol3.txt | head\necho \"=== SKT lathi ===\"; grep -n -i \"lathi\" SKT.txt | head",
 "description": "Grep Whitworth, Webster, FSD, Skeat for lathi"
}
```


### [2026-09-06T22:57:55.955Z] TOOL RESULT

```
=== AID lathi ===
4067:Lattee.  See  Ld(hi.
=== WEB lathi ===
7088:2. in psychoanalysis, having the libido de- pendent upon another instinct. : x an”a-coe-n0/sis, n. [L., from Gr. anako from enakoinoun, to make common. of rhetoric by which a speaker asks ion of the point in debate by appeal his opponents or the audience. an’a-c0-la/thi-a, n. [Gr. enako.
=== FSD lathi ===
33275:lathing, reenforcing concrete lu building construotlon, etc —
252348:limb, and short cup, os Nareiaaua triandrm and N calathinua
=== SKT lathi ===
```


## [2026-09-06T22:57:59.628Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"L[aá]thi\\b\\|Lathi\\.\" AID.txt | head; echo \"---\"; grep -n -B2 -A6 \"^Lattee\" AID.txt | head -30; echo \"=== search Lathi entry ===\"; grep -n \"athi\" AID.txt | head -20",
 "description": "Find Whitworth lathi entry"
}
```


### [2026-09-06T22:57:59.695Z] TOOL RESULT

```
---
4065-Iidthi&l.  Another  form  of  Ld{hi- wdld.
4066-lidthiwdld.  [From  Idthi  and  wdld> q.v.]  A   man  armed  with  a   club  ; particularly  such  persons  employed by  landowners  to  support  their  cause in  quarrels  about  crops,  boundaries, etc.
4067:Lattee.  See  Ld(hi.
4068-Laukik.  [Sanskrit  laukika,  from  lok, q.v.]  Worldly,  secular ;   applied  to some  classes  of  Brahman  to  denote their  inferiority  to  others  called Vaidik.
4069-Laund.  [Hindustani.]  An  inter- calary month.  See  Adhika.
4070-Laundi.  [Hindustani.]  A   slave-girl.
4071-laawdd.  [Mardthi.]  An  arbiter,  an umpire  ;   the  name  of  some  arbitra-
4072-LEFT
4073-tion  courts  lately  established  in Poona  and  some  other  districts  to decide  civil  claims  without  the  ex- pense of  resorting  to  the  courts  estab- lished by  government.  The  lawdd courts  are  thus  described  in  the Bombay  Administration  Report  for 1876-77  :   ‘A  set  of  rules  has  been framed  defining  the  constitution and  function  of  the  courts.  The members  are  drawn  for  the  most part  from  the  class  of  pleaders, traders,  and  retired  government officials.  They  agree  to  serve  as arbiters  in  turn  for  a   week  at  a   time. They  receive  no  remuneration.  The arrangements  of  the  court  are  in the  hands  of  a   secretary,  who,  in each  week,  chooses  two  members to  act  as  umpires.  Each  court  has a   staff  of  clerks  and  messengers. To  meet  this  expense  fees  are charged.  But  these  are  very  mode- rate, amounting  to  not  more  than one-third  of  the  cost  in  the  ordinary subordinate  civil  courts.’
=== search Lathi entry ===
1058:BhAmtyA.  [Marathi.]  The  name  of a   caste  said  to  have  come  to  the Deccan  from  the  Telugu  country  ; they  are  professional  thieves ;   they never  commit  burglary  or  violent crime,  but  are  most  expert  pick- pockets ;   they  carry  in  their  mouths a   minute  curved  knife  for  cutting open  bags  and  pockets  ;   the  gum and  the  inside  of  the  cheek  are hardened  with  salt  to  make  a   recep- tacle for  the  knife.
2492:Ghdt.  [Hindi.]  A   landing-place, steps  on  the  bank  of  a   river  for bathing  on,  a   wharf.  Also  a   moun- tain pass  ;   or  mountains  themselves, especially  the  ranges  of  southern India  known  as  the  Western  and Eastern  Ghdts.
2532:Ghuslkh&nd.  [Hindustdni,  from ghusl ,   bathing,  and  the  Persian khdnah ,   a   house.]  A   bathing-room  ; that  part  of  a   palace,  often  consisting of  many  elaborately  ornamented chambers  and  passages,  used  for bathing.
2545:community,  Originally  the  offspring of  Portuguese  fathers  and  Indian mothers,  but  now  marrying  only among  themselves.  They  speak Marathi  and  Portuguese,  and  ob- serve the  Roman  Catholic  religion. They  are  much  employed  as  domes- tic servants,  and  also  as  clerks.
2633:Gudhi.  [Marathi.]  A   pole  erected in  front  of  a   house  on  the  first  day of  the  year  (ist  Chaitra  sudh)  to represent  the  banner  of  Indra ; thence  the  festival  of  the  new  year.
3108:place,  particularly  a   pilgrimage  on a   fixed  day  recurring  annually  or  at longer  intervals.  Jdtrds  are  usually made  the  occasions  of  fairs  and various  amusements,  as  well  as  of visiting  the  temple,  bathing  in  the holy  water,  etc.
3469:Kardo.  [Hindi.]  The  practice  of marrying  a   widow  to  her  deceased husband’s  younger  brother  ;   it  is common  among  the  Jilt,  Gujar,  and Ahir  tribes.  The  same  practice  is known  in  different  parts  as  urhari, bathi,  and  dharichd.
4708:Mughal  Fathin.  [Hindustani.]  A game  like  draughts,  played  with
6045:Sangar.  [Marathi,  from  fan,  hemp.] The  name  of  a   caste  ;   they  weave coarse  woollen  cloth  and  blankets.
6239:6ety&.  [Marathi,  from  set/i.]  A   super- intendent of  traffic  in  a   commercial town.  The  office  is  hereditary,  but Setyds  have  ceased  to  render  formal service.  See  Settlement.
6817:ThAnedAr.  The  Marathi  form  of ThAnAdAr.
6987:U dhadj amdbandi.  [Marathi  udhad \ in  the  lump.]  A   jamdbandi  or settlement  made  in  the  lump,  the
7202:Wdghyd.  [Marathi.]  The  tiger- god,  Wdghdewa.  Some  devotees  of Khanclobd  call  themselves  by  this name.  *
7434:Bathi.  See  under  Kardo.
```


## [2026-09-06T22:58:03.850Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4058,4068p' AID.txt",
 "description": "Print Whitworth lathi entry"
}
```


### [2026-09-06T22:58:03.891Z] TOOL RESULT

```
Larin.  The  name  of  a   coinage  of  the Adil  Shdhi  kings  ;   the  coins  are sections  of  a   wire.  The  name-  is referred  to  Laristan  in  Persia.
Lascar.  [Hindustdni  Ioshkar.]  An •   army,  a   camp  ;   also  a   band,  a   gang ; a   gang  of  labourers,  the  crew  of  a
tASH
ship,  etc.  Thence  it  has  come  to  be used  also  for  a   single  member  of such  a   gang,  a   sailor,  a   tent-pitcher, etc.
Iiashkar.  [Hindustani.]  An  army, a   camp.  See  Lascar.  The  new capital  of  Gwalior  is  called  the  lash- kar  from  its  having  grown  up  round Sindhia’s  camp.
lidt.  [Hindi.]  A   column,  a   pillar ; especially  the  ancient  inscribed single  pillars  found  in  northern India,  such  as  Asoka’s  pillar  on the  ridge  at  Delhi ;   others  are  at Firuzdbdd  and  Allahdbdd,  and  there is  one  called  Bhimldt  in  the  Bhdld- ghdt  district ;   these  are  monoliths  ; there  is  a   ld$  of  wrought  iron  inscribed with  Sanskrit  near  the  Kutb  mindr.
lidthl.  [Hindustani.]  A   stick,  a club,  a   bludgeon ;   often  a   bamboo heavily  ringed  and  ferruled.
Iidthi&l.  Another  form  of  Ld{hi- wdld.
lidthiwdld.  [From  Idthi  and  wdld> q.v.]  A   man  armed  with  a   club  ; particularly  such  persons  employed by  landowners  to  support  their  cause in  quarrels  about  crops,  boundaries, etc.
Lattee.  See  Ld(hi.
Laukik.  [Sanskrit  laukika,  from  lok, q.v.]  Worldly,  secular ;   applied  to some  classes  of  Brahman  to  denote their  inferiority  to  others  called Vaidik.
```


## [2026-09-06T22:58:35.410Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob,collections\nc=collections.Counter()\nfor f in glob.glob('data/verification/page-2[5-9]*.json'):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            for x in n.get('consulted') or []:\n                c[x.get('src')]+=1\nprint(c.most_common(50))\nEOF\nmkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg301.png data/verification/sources/refs/ocr/BOOK/301.png && echo copied",
 "description": "Check consulted src conventions and copy page image"
}
```


### [2026-09-06T22:58:37.175Z] TOOL RESULT

```
[('KLN', 299), ('MON', 140), ('PHD', 138), ('POK', 133), ('BRT', 113), ('WLD', 113), ('HRN', 110), ('AHD', 107), ('SKT', 106), ('CHEUNG', 100), ('ARY', 89), ('NYB', 86), ('BQT', 83), ('Wiktionary', 81), ('HUB', 77), ('LKT', 70), ('SYN', 68), ('IEC', 60), ('LAT', 51), ('KNT', 40), ('Etymonline', 33), ('WEB', 32), ('FSD', 30), ('PLA', 27), ('FVQ', 26), ('SOD', 24), ('HJB', 24), ('AFM', 17), ('AFA', 15), ('DEV', 15), ('BOOK', 14), ('LEW', 12), ('TAD', 11), ('PHN', 9), ('ISS_alt_DKS', 8), ('WEB-Etymonline', 7), ('AKD', 6), ('RCH', 5), ('FFD', 5), ('Dehkhoda', 5), ('FSF', 5), ('WEB-Wiktionary', 4), ('FRS', 4), ('HENNING', 3), ('TLM', 3), ('SIN', 2), ('IRANICA', 2), ('OED (2005 revision, quoted verbatim at languagehat.com/pagoda)', 2), ('ARB', 2), ('Wiktionary (web)', 2)]
copied
```


## [2026-09-06T22:59:57.223Z] AGENT

Now I'll write the verification file.


## [2026-09-06T23:05:20.212Z] TOOL CALL #57: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk301.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_LAJVARD = \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%AC%D9%88%D8%B1%D8%AF\"\nW_YASTI = \"https://en.wiktionary.org/wiki/%E0%A4%AF%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A4%BF\"\nETY_AZURE = \"https://www.etymonline.com/word/azure\"\nABADIS_LAJIN = \"https://abadis.ir/fatofa/%D9%84%D8%A7%D8%AC%DB%8C%D9%86/\"\nAHD_LAPIS = \"https://www.ahdictionary.com/word/search.html?q=lapis+lazuli\"\n\nKLN_AZURE = (\"Klein 1966 p.137 (KLN_1966.txt line 4204 = leaf 84; the running head of the preceding leaf reads \"\n             \"'axo- / azyme / 136 / 137', so the azure entry stands on the spread pp.136-137): \"\n             \"\\\"azure, adj. - ME. asur, fr. OF. azur, fr. Med. Lat. azura (whence also Ital. azzurro, Sp. azur, azul, \"\n             \"Port. azul), fr. Arab. al-lazaward, fr. Pers. lajward, 'lapis lazuli'; so called from Lajward, a place \"\n             \"in Turkestan, mentioned in Marco Polo's Travels. The initial l was mistaken for the definite article \"\n             \"and consequently dropped in the Romanic languages.\\\"\")\n\nentry0 = {\n  \"entry\": 0,\n  \"root\": \"Lâjîn\",\n  \"verdict\": \"disputed\",\n  \"modern_form\": \"Persian/Turkic لاجین Lāčīn ~ Lājīn, a Turkic tribal name (Turkic lačın 'falcon') — a real word, but NOT the source of لاژورد lāžvard 'lapis lazuli', which is from the Badakhshan place-name Lāžvard\",\n  \"note\": (\"Nourai puts a Turkish tribal name at the head of the lapis-lazuli family. The word itself is real: \"\n           \"Dehkhoda (abadis.ir s.v. لاجین) glosses it 'قبیله‌ای است از ترکان نواحی بلخ' ('a tribe of the Turks of the \"\n           \"Balkh region'), which is exactly the gloss in the root box, and Mo'in's a'lam volume (MON6:1773) is \"\n           \"presumably where Nourai read it. What no source supports is the arrow out of it. Every independent \"\n           \"authority derives Persian لاژورد/لاجورد from the place where the stone was mined: Klein p.137 ('so called \"\n           \"from Lajward, a place in Turkestan, mentioned in Marco Polo's Travels'), Skeat s.v. Azure ('the mines of \"\n           \"Lajwurd, where the lapis lazuli was found'), Webster s.v. azure, AHD s.v. lapis lazuli, Lokotsch no.1311, \"\n           \"and Wiktionary, which identifies the place as Lāžvard in Badakhshan (the Sar-e Sang mines; Hudūd al-ʿĀlam, \"\n           \"982 CE: 'and in Badakhshan there are mines of silver, gold, ruby and lapis lazuli') and analyses the \"\n           \"toponym itself as Iranian, its second element Proto-Iranian *varta- 'stone'. Lokotsch adds the older \"\n           \"alternative that the word is Sanskrit rājāvarta 'king's curl' (also a name of lapis lazuli). Lāǰīn 'Turkic \"\n           \"tribe' and lāžvard 'lapis lazuli' are two unrelated words that merely share the sequence lāǰ-/lāž-; the \"\n           \"language label 'Turkish' is doubly wrong for the family, since Turkish lacivert is itself a loan FROM \"\n           \"Persian. Root verdict: disputed.\"),\n  \"note_fa\": (\"نورایی نام یک قبیلهٔ ترک، «لاجین»، را سرِ خانوادهٔ «لاجورد» گذاشته است. خودِ واژه واقعی است: دهخدا \"\n              \"«لاجین» را «قبیله‌ای است از ترکان نواحی بلخ» معنی کرده و ظاهراً نورایی آن را از جلد ششم فرهنگ معین \"\n              \"(اعلام) گرفته است. اما پیوندِ این نام با «لاژورد» در هیچ منبعی نیامده: کلاین (ص۱۳۷)، اسکیت، وبستر، \"\n              \"فرهنگ American Heritage، لوکوچ (شمارهٔ ۱۳�११) و ویکی‌واژه همگی «لاژورد» را از نام جایی در بدخشان \"\n              \"(معدن‌های سرِ سنگ) می‌دانند که سنگ لاجورد از آنجا می‌آمد؛ حدودالعالم (۳۷۲ ق/۹۸۲ م) هم از «معدن‌های سیم و \"\n              \"زر و لعل و لاجورد» بدخشان یاد کرده است. ویکی‌واژه خودِ آن نام‌جای را ایرانی می‌داند و جزء دوم آن را با \"\n              \"ایرانی *varta- «سنگ» می‌سنجد؛ لوکوچ نیز فرضِ کهن‌ترِ برگرفتگی از سنسکریت rājāvarta «طرّهٔ شاه» را نقل \"\n              \"می‌کند. پس «لاجین» و «لاژورد» دو واژهٔ بی‌ربط‌اند که تنها آغازشان شبیه است و برچسب «ترکی» هم درست نیست، \"\n              \"چون lacivert ترکی خود وام‌واژه‌ای از فارسی است. داوری: پژوهش امروزی ادعای نورایی را رد می‌کند.\"),\n  \"sources\": [W_LAJVARD, ABADIS_LAJIN, ETY_AZURE, AHD_LAPIS],\n  \"ref_check\": [\n    {\"ref\": \"MON6:1773\", \"status\": \"not_checked\",\n     \"note\": (\"Mo'in vols 5–6 (a'lam / proper names) are neither on disk nor online (refs_online.json: only the \"\n              \"lexicon vols are readable through vajehyab/abadis, and the archive.org copy is a 2-vol abridgement), \"\n              \"so p.1773 could not be opened. The gloss is however corroborated independently: abadis.ir s.v. لاجین \"\n              \"gives 'قبیله ایست از ترکان نواحی بلخ'.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"Dehkhoda\", \"where\": \"abadis.ir s.v. لاجین\", \"stance\": \"partial\",\n     \"note\": \"'قبیله ایست از ترکان نواحی بلخ' — confirms that لاجین is a Turkic tribal name, but says nothing that links it to لاجورد.\"},\n    {\"src\": \"KLN\", \"where\": \"p.137 s.v. azure (KLN_1966.txt line 4204)\", \"stance\": \"contradicts\",\n     \"note\": KLN_AZURE + \" — Klein's ultimate source is the PLACE Lajward, not a tribe.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1311 (LKT.txt line 3053)\", \"stance\": \"contradicts\",\n     \"note\": (\"\\\"Pers. läzwärd: 'Lasurstein, lasurfarben', also 'blau' [vielleicht aus sskr. rägävarta, aus rägä \"\n              \"'König' … und ävarta 'Locke' … doch wird das Wort auch als 'Quirledelstein' gedeutet], ar. läzwardi …\\\" \"\n              \"— Lokotsch knows only a Sanskrit or Iranian origin, no Turkic tribe.\")},\n    {\"src\": \"TTS\", \"where\": \"Vámbéry 1878 (TTS_vambery1878_uoft_djvu.txt), grep 'lacin|laczin|latschin|lačyn'\", \"stance\": \"silent\",\n     \"note\": \"No entry for lačın/lāčīn found in the OCR of Vámbéry's Turko-Tatar etymological dictionary; the Turkic word for 'falcon' could not be located there.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. لاجورد (Persian)\", \"stance\": \"contradicts\",\n     \"note\": \"\\\"usually considered to be from the place name لاژورد (Lāžvard) in Badakhshan where the stone was mined\\\"; second element from Proto-Iranian *varta- 'stone'.\"}\n  ],\n  \"nodes\": []\n}\n\nentry0[\"nodes\"] = [\n {\n  \"id\": 1,\n  \"lang\": \"Persian\",\n  \"words\": \"Lâjîn; Lâj-vard; lâjvard\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"Three separate Persian words are put in one box. (a) لاجین Lāǰīn is genuinely the name of a Turkic tribe \"\n    \"(Dehkhoda: 'قبیله‌ای است از ترکان نواحی بلخ'), and as such is simply the root word repeated in Persian dress — \"\n    \"that step is unobjectionable. (b) لاجورد Lāǰvard as a toponym and (c) لاجورد lāǰvard 'lapis lazuli, the colour \"\n    \"azure' are the two the chart wrongly hangs on it. The oldest Persian shape is لاژورد lāžvard with Persian ž \"\n    \"(Borhan-e Qate' s.v. لاژورد: 'با زای فارسی، بر وزن و معنی لاجورد است و آن سنگی است کبود که نقاشان و مصوران بکار \"\n    \"برند'); لاجورد is the ج-spelling and لازورد the form re-imported from Arabic (Mo'in's footnote to that Borhan \"\n    \"entry: 'لاژورد > لازورد (معرّب)'). Klein p.137 and Skeat s.v. Azure derive the stone-name from the place: 'so \"\n    \"called from Lajward, a place in Turkestan, mentioned in Marco Polo's Travels' (Polo, Bk I, describes the azure \"\n    \"mine of Badashan) — i.e. the mines of Sar-e Sang in Badakhshan, already named in the Hudūd al-ʿĀlam of 982 CE. \"\n    \"Wiktionary makes the toponym itself Iranian, its second element Proto-Iranian *varta- 'stone'; Lokotsch no.1311 \"\n    \"reports the competing derivation from Sanskrit rājāvarta 'king's curl'. Neither route passes through a Turkic \"\n    \"tribe, so the arrow Lâjîn → Lâj-vard/lâjvard is unsupported. The word for the stone is metonymic ('(stone) of \"\n    \"Lāžvard') and then became a colour term ('azure'), whence لاجوردین/لاجوردی 'azure-coloured' in the box's extra \"\n    \"script, as in Khāqānī's line quoted by Nourai ('این سقف لاجورد' = the azure vault of heaven).\"),\n  \"derivation_fa\": (\n    \"در این جعبه سه واژهٔ جدا کنار هم نشسته‌اند. «لاجین» به‌راستی نام قبیله‌ای ترک است و تکرارِ همان سرواژه در فارسی \"\n    \"است؛ ایرادی ندارد. اما «لاجورد» (نام‌جای) و «لاجورد» (سنگ کبود و رنگ آن) را نمی‌توان به آن بست. صورت کهن‌تر \"\n    \"فارسی «لاژورد» با زای فارسی است — برهان قاطع: «لاژورد، با زای فارسی، بر وزن و معنی لاجورد است و آن سنگی است کبود \"\n    \"که نقاشان و مصوران بکار برند» — و «لازورد» صورتِ معرّب است که دوباره به فارسی بازگشته (حاشیهٔ معین بر همان مدخل: \"\n    \"«لاژورد > لازورد (معرّب)»). کلاین (ص۱۳۷) و اسکیت نام سنگ را از نام‌جای «لاژورد» می‌دانند، یعنی معدن‌های سرِ سنگِ \"\n    \"بدخشان که مارکوپولو و پیش از او حدودالعالم از آن یاد کرده‌اند؛ ویکی‌واژه خودِ نام‌جای را ایرانی می‌شمارد (جزء \"\n    \"دوم آن هم‌ریشه با ایرانی *varta- «سنگ») و لوکوچ فرضِ سنسکریت rājāvarta را نقل می‌کند. پس تحول معنایی «نام معدن ← \"\n    \"سنگِ آن ← رنگ کبود» درست است، ولی پیوند با قبیلهٔ «لاجین» را هیچ منبعی تأیید نمی‌کند و ریشه‌شناسی عامیانه می‌نماید.\"),\n  \"sources\": [W_LAJVARD, ABADIS_LAJIN, ETY_AZURE],\n  \"ref_check\": [\n    {\"ref\": \"MON6:1773\", \"status\": \"not_checked\",\n     \"note\": \"Mo'in vol. 6 (a'lam) is not available on disk or online; only the lexicon volumes are readable (vajehyab/abadis), and they carry لاجورد without any Turkic-tribe etymology.\"},\n    {\"ref\": \"KLN:137\", \"status\": \"partial\",\n     \"note\": KLN_AZURE + \" — Klein supports the Persian word and its meaning, and the place-name Lajward, but derives the stone-name from that PLACE, not from a tribal name; he says nothing of Lâjîn.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', vol. 3 scan (incoming/BQT/BQT_v3_pages.txt, pdf leaves 671–673), s.v. لاژورد and Mo'in's footnote 1\", \"stance\": \"partial\",\n     \"note\": \"Entry: 'لاژورد، با زای فارسی، بر وزن و معنی لاجورد است و آن سنگی است کبود که نقاشان و مصوران بکار برند'; Mo'in's footnote: 'لاژورد > لازورد (معرّب) lazuli = lazulite (فر)'. Confirms lāžvard > Arabic lāzvard; no Turkic tribe.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. لاجورد (MON_part2.txt lines 37745-37756)\", \"stance\": \"partial\",\n     \"note\": \"'… حجر لاجورد، حجر اللاجورد. لاژورد، لازورد، لاجورد …' with a mineralogical description and the use of the powdered stone as blue paint; Mo'in's lexicon entry gives no Turkic-tribe origin.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Azure (SKT.txt line 1261)\", \"stance\": \"partial\",\n     \"note\": \"'Arab. lájward, lapis lazuli, a blue colour. So called from the mines of Lajwurd, where the lapis lazuli was found (Marco Polo, ed. Yule).' — place-name, not tribe.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie, grep 'lazward|lajward|lazur'\", \"stance\": \"silent\",\n     \"note\": \"Horn has no entry for lāžvard/lāzvard; the word is not treated in his Grundriss.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien, grep 'lazward|lazur|lajward'\", \"stance\": \"silent\",\n     \"note\": \"Hübschmann does not treat the word.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. لاجورد (Persian)\", \"stance\": \"contradicts\",\n     \"note\": \"Alternative forms لاژورد/لازورد; 'usually considered to be from the place name لاژورد (Lāžvard) in Badakhshan where the stone was mined'; descendants Arabic لازورد, Latin lazulum/azzurum, Turkish lacivert.\"}\n  ]\n },\n {\n  \"id\": 2,\n  \"lang\": \"Arabic\",\n  \"words\": \"al-lâzaward\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Persian لاژورد lāžvard was taken into Arabic as لازورد lāzaward (with the article al-lāzaward). Two regular \"\n    \"adaptations: Arabic has no ž, so Persian ž → z; and the Persian final cluster -žv-/-zw- is broken by an \"\n    \"anaptyctic -a- (lāz-a-ward), the normal Arabic treatment of Persian consonant groups. Addi Shir's dictionary of \"\n    \"Persian loanwords in Arabic gives it as the very first entry of باب اللام, p.141: '(اللازورد) معدن مشهور تعريب \"\n    \"لاژورد' — 'a well-known mineral, Arabicised from lāžward'. Asbaghi p.240 lists 'lāzward: \\\"Lapislazuli\\\", pers. \"\n    \"lazward' with the further route 'pers. > ar. > lat.' for Lapislazuli, Lasurstein, Azur, Lasurit. The word is \"\n    \"current in Arabic mineralogical and medical writing from the early ʿAbbasid period and came back into Persian as \"\n    \"لازورد, so this is a Persian → Arabic → Persian round trip as well as the source of the European words.\"),\n  \"derivation_fa\": (\n    \"«لاژورد» فارسی به عربی رفت و به صورت «لازورد» (با ال تعریف: اللازورد) درآمد. دو دگرگونی آوایی منظم رخ داده: \"\n    \"عربی «ژ» ندارد، پس ژ به ز بدل شده؛ و خوشهٔ همخوانی پایانی با افزودن واکهٔ میانجی شکسته شده (lāz-a-ward)، که شیوهٔ \"\n    \"معمول تعریبِ خوشه‌های فارسی است. أدّي شير در «الألفاظ الفارسیة المعرّبة» ص۱۴۱، نخستین مدخلِ بابُ اللام، می‌نویسد: \"\n    \"«(اللازورد) معدن مشهور تعریب لاژورد». اسبغی نیز در ص۲۴۰ آن را وام‌واژهٔ فارسی در عربی می‌داند و مسیر «فارسی ← \"\n    \"عربی ← لاتین» را برای Lapislazuli و Azur ثبت کرده است. این واژه سپس به صورت معرّبِ «لازورد» به فارسی بازگشته \"\n    \"است، یعنی وام‌گیریِ دوسویه. ادعای نورایی در این حلقه درست است.\"),\n  \"sources\": [AHD_LAPIS, W_LAJVARD],\n  \"ref_check\": [\n    {\"ref\": \"PLA:240\", \"status\": \"supports\",\n     \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, p.240 (incoming/PLA/PLA_pages.txt line 13463, running head 'lādan 240 ladġ'): 'lāzward: \\\"Lapislazuli\\\" pers. lazward'; below it 'Lapislazuli: Lasurstein, blauer Halbedelstein pers. > ar. > lat.' and 'Azur: \\\"das Himmelsblau\\\" pers. > ar. > frz.'\"},\n    {\"ref\": \"AFM:141\", \"status\": \"supports\",\n     \"note\": \"Addi Shir p.141 (= AFM.pdf page 143; printed number ١٤١ read on the page image, saved as data/verification/sources/refs/ocr/AFM/0141.png with a transcription in 0141.vision.txt): first entry of باب اللام — '(اللازورد) معدن مشهور تعريب لاژورد'.\"},\n    {\"ref\": \"AHD:737\", \"status\": \"supports\",\n     \"note\": \"The page number (New College ed. 1975, p.737) cannot be checked locally — only Watkins's IE-roots appendix is on disk — but the content is exactly AHD's: online AHD s.v. lapis lazuli, 'Latin lapis, stone + Medieval Latin lazulī, genitive of lazulum, lapis lazuli (from Arabic lāzaward, from Persian lājward)'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p.868 s.v. lapis lazuli (KLN_1966.txt line 21138, leaf 465 = pp.866-867)\", \"stance\": \"supports\",\n     \"note\": \"'lapis lazuli, an azure blue stone. — ML., fr. L. lapis, \\\"stone\\\", and gen. of ML. lazulum, \\\"lapis lazuli\\\", fr. Arab. lazaward. See lapidary, adj., and azure.'\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. azure (WEB_vol1.txt line 14451)\", \"stance\": \"supports\",\n     \"note\": \"'[ME. azure; OFr. azur; LL. azura; Ar. lazward; Per. lazhward, azure; the initial l lost through confusion with the definite article, Fr. l', le, etc.]' — Arabic lazward from Persian lazhward.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1311 (LKT.txt line 3053)\", \"stance\": \"supports\",\n     \"note\": \"'Pers. läzwärd … ar. läzwardi \\\"lazurähnlich\\\"; hieraus mit Abfall des als Artikel betrachteten l …' — the Arabic form is the pivot between Persian and the European words.\"}\n  ]\n },\n {\n  \"id\": 3,\n  \"lang\": \"Latin\",\n  \"words\": \"lazulum; azzurum\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Arabic (al-)lāzaward entered Medieval Latin in the 12th–13th c. through the Arabic-to-Latin translation movement \"\n    \"and the pigment trade, as lazur / lazurium, latinised with a diminutive-looking -ulum as lazulum; the phrase \"\n    \"lapis lazulī 'stone of lazulum' (genitive) is first quoted in English from the early 15th c. Alongside it stands \"\n    \"the l-less family: in Romance the initial l- was reanalysed as the article (Italian l'azzurro, Old French l'azur), \"\n    \"giving Med. Lat. azura / azzurum, Italian azzurro, Old French azur, Spanish/Portuguese azul, whence the chart's \"\n    \"note, which is exactly Klein's wording: 'The initial l was mistaken for the definite article and consequently \"\n    \"dropped in the Romanic languages.' Skeat s.v. Azure says the same ('O.F. azur, a corrupted form, standing for \"\n    \"lazur, which was mistaken for l'azur, as if the initial l indicated the def. article'), as does Webster and \"\n    \"Lokotsch no.1311. 'azzurum' is the Italianate Medieval-Latin spelling (Wiktionary lists Latin lazulum, lazurium, \"\n    \"azzurum, azura among the Arabic word's descendants); Klein cites the same form as Med. Lat. azura. Both words in \"\n    \"the box are therefore Medieval, not Classical, Latin — a distinction Nourai's flat 'Latin' label hides.\"),\n  \"derivation_fa\": (\n    \"«اللازورد» عربی در سدهٔ ۱۲–۱۳ میلادی، از راه نهضت ترجمهٔ عربی به لاتینی و نیز تجارت رنگ‌دانه، وارد لاتینیِ \"\n    \"میانه شد: lazur/lazurium و با پسوندنمای -ulum به شکل lazulum، و ترکیب lapis lazulī «سنگِ لاجورد». در کنار آن \"\n    \"خانوادهٔ بی‌«ل» پدید آمد: در زبان‌های رومی، «ل» آغازین را حرف تعریف پنداشتند (ایتالیایی l'azzurro، فرانسهٔ کهن \"\n    \"l'azur) و آن را انداختند؛ نتیجه azzurum/azura در لاتینی میانه، azzurro ایتالیایی، azur فرانسوی و azul اسپانیایی \"\n    \"است. یادداشتِ خودِ نورایی در این جعبه عیناً سخن کلاین است و اسکیت، وبستر و لوکوچ نیز همین را می‌گویند. تنها نکته \"\n    \"آنکه هر دو واژه لاتینیِ میانه‌اند نه لاتینیِ کلاسیک، و برچسبِ سادهٔ «Latin» این تمایز را می‌پوشاند. ادعای نورایی \"\n    \"درست است.\"),\n  \"sources\": [ETY_AZURE, AHD_LAPIS, W_LAJVARD],\n  \"ref_check\": [\n    {\"ref\": \"KLN\", \"status\": \"supports\",\n     \"note\": KLN_AZURE + \" and p.868 s.v. lapis lazuli: 'ML., fr. L. lapis … and gen. of ML. lazulum … fr. Arab. lazaward.'\"},\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD online s.v. lapis lazuli: 'Latin lapis, stone + Medieval Latin lazulī, genitive of lazulum, lapis lazuli (from Arabic lāzaward, from Persian lājward)' — the Medieval Latin lazulum of the box.\"},\n    {\"ref\": \"KGW:108\", \"status\": \"not_checked\",\n     \"note\": \"J. Ibrahim, Kulturgeschichtliche Wortforschung (Wiesbaden 1991) is not on disk; refs_online.json records it as Google-Books limited preview / HathiTrust search-only, so p.108 could not be opened.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Azure (SKT.txt line 1261)\", \"stance\": \"supports\",\n     \"note\": \"'M.E. asur, azure. — O.F. azur, a corrupted form, standing for lazur, which was mistaken for l'azur, as if the initial l indicated the def. article. — Low L. lazur, an azure coloured stone, also called lapis lazuli.'\"},\n    {\"src\": \"WEB\", \"where\": \"s.v. azure and lazulite (WEB_vol1.txt lines 14451, 106188)\", \"stance\": \"supports\",\n     \"note\": \"'LL. azura; Ar. lazward; Per. lazhward … the initial l lost through confusion with the definite article'; 'lazulite, n. [from ML. lazulum, azure; and -ite]'.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1311 (LKT.txt line 3053)\", \"stance\": \"supports\",\n     \"note\": \"'hieraus mit Abfall des als Artikel betrachteten l it. azzurro, azzuolo \\\"dunkelblau\\\", lapis lazzuli \\\"Lasurstein\\\", prov. frz. azur, kat. sp. pg. azul … mlat. lazulum [woraus mgr. λαζούριον]'.\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. azure\", \"stance\": \"supports\",\n     \"note\": \"'Old French azur (12c.), from Medieval Latin lazur/lazuri … a false separation in Old French, as though the -l- were the French article l'; lapis lazuli (early 15c.) = Latin lapis + Medieval Latin lazuli, genitive of lazulum, from Arabic lazuward.'\"}\n  ]\n },\n {\n  \"id\": 4,\n  \"lang\": \"English\",\n  \"words\": \"lapis lazuli; azure; azulene\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"azure: Middle English asur/azur, from Old French azur (12c.), from Med. Lat. lazur with the l- lost as described \"\n    \"in the parent box; first as the name of the stone/pigment, then of its colour, and in heraldry the tincture \"\n    \"'blue'. lapis lazuli: taken directly from the Medieval Latin phrase in the early 15th c. and still written as \"\n    \"Latin. azulene: a modern chemical coinage (the deep-blue hydrocarbon C10H8) — but Klein is explicit that it is \"\n    \"'Formed with suff. -ene fr. Sp. azul, \\\"blue\\\"', i.e. it reaches English through Spanish azul, not straight from \"\n    \"Latin, so the single arrow Latin → English compresses one step here. Webster gives the same chain for azure and \"\n    \"adds the mineral names azurite and lazulite (the latter '[from ML. lazulum, azure]'), and Wiktionary lists \"\n    \"English lapis lazuli and azure among the descendants of Persian لاژورد. The English half of the chart is \"\n    \"uncontroversial.\"),\n  \"derivation_fa\": (\n    \"azure از انگلیسی میانه asur/azur و آن از فرانسهٔ کهن azur (سدهٔ ۱۲ م) و آن از lazur لاتینیِ میانه است، با افتادن \"\n    \"«ل» آغازین که آن را حرف تعریف پنداشته بودند؛ نخست نام سنگ و رنگ‌دانه بود و سپس نام رنگ کبود و در نشان‌شناسی \"\n    \"«آبی». lapis lazuli در آغاز سدهٔ ۱۵ م یکجا از عبارتِ لاتینیِ میانه گرفته شده و هنوز هم به همان صورت لاتینی نوشته \"\n    \"می‌شود. اما azulene (نام هیدروکربنِ آبی‌رنگ) بنا بر تصریح کلاین از azul اسپانیایی + پسوند -ene ساخته شده، یعنی \"\n    \"از راه اسپانیایی به انگلیسی رسیده و پیکان یگانهٔ «لاتین ← انگلیسی» در این مورد یک حلقه را جا انداخته است. \"\n    \"وبستر همین زنجیره را برای azure می‌آورد و azurite و lazulite را هم می‌افزاید. این بخش از نمودار درست است.\"),\n  \"sources\": [ETY_AZURE, AHD_LAPIS, W_LAJVARD],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD online s.v. lapis lazuli gives the Latin/Arabic/Persian chain for the English headword.\"},\n    {\"ref\": \"KLN\", \"status\": \"supports\",\n     \"note\": \"KLN_1966 p.137: 'azure, adj. — ME. asur, fr. OF. azur …'; p.868 'lapis lazuli … ML., fr. L. lapis … fr. Arab. lazaward'; and, on the same p.137, 'azulene, n., blue hydrocarbon (chem.) — Formed with suff. -ene fr. Sp. azul, \\\"blue\\\"' — azulene therefore via Spanish.\"},\n    {\"ref\": \"WEB\", \"status\": \"supports\",\n     \"note\": \"Webster's New Twentieth Century (WEB_vol1.txt lines 14451, 105461, 106188): 'az/ure … [ME. azure; OFr. azur; LL. azura; Ar. lazward; Per. lazhward, azure; the initial l lost through confusion with the definite article]'; 'lapis lazuli; an azure-blue, opaque, semi-precious stone'; 'lazulite … [from ML. lazulum, azure]'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"Etymonline\", \"where\": \"s.v. azure\", \"stance\": \"supports\",\n     \"note\": \"Old French azur < Med. Lat. lazur < Persian lajward; 'lapis lazuli (early 15c.)'.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Azure (SKT.txt line 1261)\", \"stance\": \"supports\",\n     \"note\": \"'M.E. asur, azure. — O.F. azur … Low L. lazur, an azure coloured stone, also called lapis lazuli.'\"},\n    {\"src\": \"KLN\", \"where\": \"p.137 s.v. azulene\", \"stance\": \"partial\",\n     \"note\": \"'azulene, n., blue hydrocarbon (chem.) — Formed with suff. -ene fr. Sp. azul, \\\"blue\\\". See next word [azure].' — Klein routes azulene through Spanish, not directly from Latin as the chart's arrow implies.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. لاجورد, descendants\", \"stance\": \"supports\",\n     \"note\": \"English 'lapis lazuli, azure' listed among the descendants of the Persian word via Arabic and Latin.\"}\n  ]\n }\n]\n\nWLD_QUOTE = (\"Walde-Pokorny II 443 (incoming/WLD/WLD_Bd2_pages.txt, leaf 448, running head 'lorga, lorgi- — \"\n             \"l(j)akti-  443'): \\\"l(j)akti- „Stab“. Schulze SBAk. Berlin 1912, 581 vereinigt unter einem solchen \"\n             \"Anlaute ai. yaṣṭi-ḥ „Stab, Stock“ (av. yaxšti- „Zweig“), pali yaṭṭhi und laṭṭhi, prakr. laṭṭhi und \"\n             \"slav. ostъ (ostьnъ „stimulus“), das dann von ak- „scharf“ zu trennen wäre; ?\\\"\")\n\nBRT_QUOTE = (\"Bartholomae, Altiranisches Wörterbuch col. 1236 (BRT.txt line 21067; the next running head on the same \"\n             \"leaf reads '1237 … 1238', and Buck 8.55 independently cites 'Barth. 809, 1236'): \\\"• j. yaxštay- m. \"\n             \"'Zweig'. KompE. — ai. yaṣṭay- m. 'Stab'. — Pü.: tāk. — 1) Nach dem ai. Wort muss das zu Grunde liegende \"\n             \"arische i̯ gehabt haben; Aw. xš ist also sekundär, vgl. § 86 aE.\\\"\")\n\nSYN_QUOTE = (\"Buck, Selected Synonyms §8.55 BRANCH, p.525 (SYN.txt lines 13237-13240): \\\"Av. yaxšti- (in cpds. \"\n             \"θri-yaxšti-, etc.) = Skt. yaṣṭi- 'staff, stick', root connections dub. Walde-P. 1.443. Barth. 809, 1236.\\\"\")\n\nentry4 = {\n  \"entry\": 4,\n  \"root\": \"Lakti, Ljakti\",\n  \"verdict\": \"disputed\",\n  \"modern_form\": \"No such Indo-European root is recognised today; Walde-Pokorny II 443 prints 'l(j)akti- \\\"Stab\\\"' only as a report of Schulze's 1912 conjecture, and closes it with a question mark\",\n  \"note\": (\n    \"The citation itself is exact: WLD II 443 does head an entry 'l(j)akti- „Stab“', which is where Nourai's double \"\n    \"headword 'Lakti, Ljakti' comes from. But three things must be said. (1) The gloss there is only 'Stab' (stick); \"\n    \"'club' is Nourai's addition — the neighbouring entry on the same page, 'lorga, lorgi- „Stock, Knüttel“' (Ir. lorg \"\n    \"'clava'), is the 'club' one. (2) Walde-Pokorny are not asserting a root: they are reporting W. Schulze's 1912 \"\n    \"proposal (SBAk. Berlin 1912, 581) of a special initial l(j)- that would unite Skt. yaṣṭi- / Av. yaxšti- with Pali \"\n    \"laṭṭhi, Prakrit laṭṭhi and Slavic ostъ, and they end the paragraph with a bare '?'. (3) Pokorny's own IEW (1959) \"\n    \"dropped the entry altogether — a grep of the full text for 'lakti', 'yaxšti', 'yaṣṭi' returns nothing — and \"\n    \"Watkins/AHD has no such root either. Buck 8.55 (p.525) says flatly of the Avestan-Sanskrit pair 'root connections \"\n    \"dub.' Mann (IEC) does keep 'lakstis (lakt-) \\\"stick, stem, branch, bar\\\"' with a reference to WP II 443, but his \"\n    \"material is the l- group only (Pali laṭṭhi, cf. Skt. lakuṭaḥ 'cudgel', Arm. laxt, Gk. laktis 'pestle', Lith. \"\n    \"laktà) — he does not put Skt. yaṣṭi-/Av. yaxšti- under it. Modern Indo-Aryan scholarship (Wiktionary s.v. यष्टि, \"\n    \"with Turner and Mayrhofer behind it) calls yaṣṭi- of unknown origin, 'multiple unconvincing theories proposed', \"\n    \"and explains the l- of the Middle Indic forms as contamination with lakuṭa- 'club'. So the words in the chart are \"\n    \"indeed related to one another, but the reconstructed root that heads them is a discarded conjecture: disputed.\"),\n  \"note_fa\": (\n    \"ارجاع نورایی دقیق است: والده–پوکورنی در جلد دوم ص۴۴۳ مدخلی با سرواژهٔ l(j)akti- «Stab» دارند و «Lakti, Ljakti» \"\n    \"برگردانِ همان است. اما سه نکته هست. نخست آنکه معنای آنجا تنها «چوب‌دست» است و «گرز/چماق» افزودهٔ نورایی است؛ \"\n    \"مدخلِ همسایه در همان صفحه یعنی lorga «چوب، چماق» است. دوم آنکه والده–پوکورنی خود این را ریشه نمی‌دانند، بلکه \"\n    \"پیشنهاد ویلهلم شولتسه (۱۹۱۲) را گزارش می‌کنند که با فرضِ آغازهٔ ویژهٔ l(j)- می‌خواست یَشتی سنسکریت و یخشتیِ \"\n    \"اوستایی را با laṭṭhi پالی و پراکریت و ostъ اسلاوی یکی کند، و پاراگراف را با علامت پرسش می‌بندند. سوم آنکه پوکورنی \"\n    \"در فرهنگ ۱۹۵۹ این مدخل را یکسره کنار گذاشته و واتکینز نیز چنین ریشه‌ای ندارد؛ باک (§۸٫۵۵) می‌گوید پیوندِ ریشه‌ایِ \"\n    \"این واژه‌ها «مشکوک» است و ویکی‌واژه یَشتی را «ناشناخته‌ریشه» می‌خواند و «ل»ِ صورت‌های هندی میانه را نتیجهٔ آمیختگی \"\n    \"با lakuṭa «چماق» می‌داند. پس واژه‌های نمودار با یکدیگر هم‌ریشه‌اند، ولی ریشهٔ بازسازی‌شده‌ای که بر سرشان نشسته \"\n    \"فرضیه‌ای متروک است؛ پژوهش امروزی آن را نمی‌پذیرد.\"),\n  \"sources\": [W_YASTI],\n  \"ref_check\": [\n    {\"ref\": \"WLD2:443\", \"status\": \"supports\",\n     \"note\": WLD_QUOTE + \" — the headword, the volume and the page are all correct; only the gloss 'club' and the status of the entry as a real root are Nourai's own.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 1959, full text (POK_full.txt / POK_01-03), grep 'lakti', 'yaxšti', 'yaṣṭi', 'yasti-'\", \"stance\": \"silent\",\n     \"note\": \"No entry and no mention: Pokorny did not carry Schulze's l(j)akti- over from Walde-Pokorny into the IEW.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins, AHD Dictionary of Indo-European Roots 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\",\n     \"note\": \"No root of this shape; grep for 'lazuli|azure' and for lakt- yields nothing relevant.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.vv. lakstis and latis (IEC.txt lines 9447, 9516)\", \"stance\": \"partial\",\n     \"note\": \"'lakstis, à (lakt-) \\\"stick, stem, branch, bar\\\" … Prakritic, Pali laṭṭhi \\\"stick\\\" (cf. Skt. lakutah \\\"cudgel\\\"); Arm. laxt … Gk. laktis … Li. lakstà, laktà \\\"perch\\\"' and 'latis \\\"rod, lath\\\" … WP II, 443' — Mann keeps a *lakt- 'stick', but with the l- forms only and with Skt. lakuṭa- as the comparandum; Skt. yaṣṭi-/Av. yaxšti- are absent.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §8.55 BRANCH, p.525\", \"stance\": \"partial\",\n     \"note\": SYN_QUOTE + \" — Buck accepts the Avestan–Sanskrit equation but calls the root connection dubious.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. यष्टि (Sanskrit), Etymology 2\", \"stance\": \"contradicts\",\n     \"note\": \"'unknown origins with multiple unconvincing theories proposed'; one theory 'suggests contamination with लकुट (lakuṭa, \\\"club\\\"), potentially connecting to Ashokan Prakrit *laṣṭi and modern descendants' — i.e. the l- is secondary, not inherited from a root *l(j)akti-.\"}\n  ],\n  \"nodes\": []\n}\n\nentry4[\"nodes\"] = [\n {\n  \"id\": 1,\n  \"lang\": \"Avestan\",\n  \"words\": \"yaxšti, yaxštay; thri-yaxštay\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"The Avestan words are real and exactly as given: Younger Avestan yaxšti- (stem yaxštay-) m. 'branch, twig', and \"\n    \"the compound θri.yaxštay- of the barsom bundle. Bartholomae col. 1236: 'j. yaxštay- m. \\\"Zweig\\\"… ai. yaṣṭay- m. \"\n    \"\\\"Stab\\\"', with the note that, to judge by the Sanskrit word, the underlying Aryan form had *y- and that Avestan \"\n    \"-xš- is secondary (the Avestan reflex of the cluster that Sanskrit shows as -ṣṭ-, cf. Skt. yaṣṭi- : Av. yaxšti-, \"\n    \"the same correspondence as in Skt. -ṣṭ- / Av. -xšt- elsewhere). The compound appears at Yasna 57.6, in the \"\n    \"sequence θri.yaxštīšca pança.yaxštīšca hapta.yaxštīšca nava.yaxštīšca — 'three-twig, five-twig, seven-twig, \"\n    \"nine-twig (barsom)' — so Bartholomae glosses θri.yaxštay- as a plural 'drei Zweige' ('three branches'), not \"\n    \"adjectivally 'with three branches' as the chart has it; a small looseness in Nourai's gloss. The node is marked \"\n    \"plausible rather than confirmed only because of the parent: the word is certain, the equation with Sanskrit \"\n    \"yaṣṭi- is certain (Bartholomae, Buck 8.55), but its descent from a root with initial l- is the discarded Schulze \"\n    \"conjecture discussed at the root box; and Bartholomae's own note that the Aryan initial was *y- pulls against it.\"),\n  \"derivation_fa\": (\n    \"واژه‌های اوستایی درست‌اند: در اوستای نو yaxšti- (ستاک yaxštay-) به معنی «شاخه، ترکه» و ترکیبِ θri.yaxštay- دربارهٔ \"\n    \"دستهٔ برسم. بارتولومه در ستون ۱۲۳۶ می‌نویسد: «yaxštay- مذکر، «شاخه» … سنسکریت yaṣṭay- «چوب‌دست»» و می‌افزاید که \"\n    \"بنا بر گواهیِ واژهٔ سنسکریت، صورت آریاییِ زیرین باید *y- داشته باشد و -xš- اوستایی ثانوی است (برابرِ -ṣṭ- سنسکریت). \"\n    \"ترکیب در یسنِ ۵۷٫۶ همراهِ «پنج‌شاخه، هفت‌شاخه، نه‌شاخه» آمده و بارتولومه آن را جمعِ «سه شاخه» معنی کرده است، نه \"\n    \"صفتِ «دارای سه شاخه» چنانکه نورایی نوشته؛ خطای کوچکی در معناکردن. داوری «با احتیاط پذیرفتنی» است، نه به سببِ خودِ \"\n    \"واژه — که قطعی است — بلکه به سببِ ریشهٔ پدر: انتسابِ آن به ریشه‌ای با «ل» آغازین همان فرضِ متروکِ شولتسه است و \"\n    \"یادداشت خودِ بارتولومه دربارهٔ *y- آغازین با آن نمی‌خواند.\"),\n  \"sources\": [W_YASTI],\n  \"ref_check\": [\n    {\"ref\": \"WLD2:443\", \"status\": \"supports\",\n     \"note\": WLD_QUOTE + \" — 'av. yaxšti- „Zweig“' stands there in parentheses beside the Sanskrit word, exactly as the chart has it.\"},\n    {\"ref\": \"SYN:525\", \"status\": \"supports\", \"note\": SYN_QUOTE},\n    {\"ref\": \"BRT:1236\", \"status\": \"supports\", \"note\": BRT_QUOTE}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1236 (yaxštay-) and cols. 1236 f. for the compounds\", \"stance\": \"supports\",\n     \"note\": BRT_QUOTE + \" The compounds are at BRT.txt lines 14655 ('θri.yaxštay- m., Plur. \\\"drei Zweige\\\"… Y.57.6'), 15246 ('pança.yaxštay- m., Plur. \\\"fünf Zweige\\\"') and 18654 ('nava.yaxštay- … \\\"neun Zweige\\\"').\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §8.55 BRANCH, p.525\", \"stance\": \"supports\",\n     \"note\": SYN_QUOTE},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 443\", \"stance\": \"supports\",\n     \"note\": \"Av. yaxšti- 'Zweig' is cited there, but only inside the report of Schulze's conjecture.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. यष्टि, comparative evidence\", \"stance\": \"partial\",\n     \"note\": \"'The entry notes \\\"late Avestan ẏaxšti\\\" as a cognate, with modern Iranic forms like Pashto laṧta (\\\"rod\\\") likely borrowed from the Prakrit form rather than inherited.' — the cognation is accepted, the root is not.\"}\n  ]\n },\n {\n  \"id\": 2,\n  \"lang\": None,\n  \"words\": \"\",\n  \"verdict\": \"unverified\",\n  \"derivation\": (\n    \"An empty pass-through box. The printed page really is blank here: the 200-dpi render of pdf p.301 (copied to \"\n    \"data/verification/sources/refs/ocr/BOOK/301.png) shows an arrow leaving the Avestan yaxšti box and ending in a \"\n    \"wide double-ruled rectangle that carries no language header, no reference and no word. The extraction is \"\n    \"faithful — it recorded the box with lang=null, refs=null and an empty word list. There is nothing to verify.\"),\n  \"derivation_fa\": (\n    \"این جعبه تهی است. تصویر صفحهٔ چاپی (برگ ۳۰۱ پی‌دی‌اف، نگهداری‌شده در \"\n    \"data/verification/sources/refs/ocr/BOOK/301.png) نشان می‌دهد که پیکانی از جعبهٔ اوستاییِ yaxšti بیرون می‌آید و به \"\n    \"مستطیلی کاملاً خالی می‌رسد که نه نام زبان دارد، نه ارجاع و نه واژه. خوانشِ داده‌ها درست است و همین تهی‌بودن را \"\n    \"ثبت کرده؛ چیزی برای راستی‌آزمایی وجود ندارد.\"),\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the printed chart.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BOOK\", \"where\": \"pdf p.301 = book p.271, 200-dpi render, data/verification/sources/refs/ocr/BOOK/301.png\", \"stance\": \"supports\",\n     \"note\": \"The rectangle to the right of the Avestan box is drawn but completely blank — a layout artefact of Nourai's chart, not an extraction error.\"}\n  ]\n },\n {\n  \"id\": 3,\n  \"lang\": \"Sanskrit\",\n  \"words\": \"yaštih\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Sanskrit यष्टि yaṣṭí- f., nom. sg. yaṣṭíḥ — Nourai's 'yaštih' is that nominative with the retroflex ṣ flattened \"\n    \"to š. Monier-Williams and Wiktionary give the range 'any support: staff, stick, wand, rod, mace, club, cudgel; \"\n    \"pole, pillar, perch; stalk, stem, branch, twig', so both of the chart's glosses ('branch, stick') are in the \"\n    \"word. Walde-Pokorny II 443 quote it in exactly this form ('ai. yaṣṭi-ḥ „Stab, Stock“') and Buck 8.55 equates it \"\n    \"with Av. yaxšti-. What is not established is the parent: Wiktionary's Sanskrit entry says the origin is unknown, \"\n    \"with 'multiple unconvincing theories', and Buck says 'root connections dub.', so descent from an Indo-European \"\n    \"*l(j)akti- is at best one abandoned proposal. Note also that the chart draws yaṣṭi- and Av. yaxšti- as two \"\n    \"independent branches of the root, whereas they are simply the Indo-Aryan and Iranian reflexes of one \"\n    \"Indo-Iranian word.\"),\n  \"derivation_fa\": (\n    \"سنسکریت यष्टि (yaṣṭí-)، فاعلیِ مفرد yaṣṭíḥ؛ آنچه نورایی «yaštih» نوشته همین است با سادهٔ‌سازیِ «ṣ» واکاکامی. \"\n    \"مونیه‌ویلیامز و ویکی‌واژه معناهای «چوب‌دست، عصا، گرز، تیرک، ستون، ساقه، شاخه و ترکه» را می‌دهند، پس هر دو معنایی \"\n    \"که در نمودار آمده در واژه هست. والده–پوکورنی نیز آن را دقیقاً به همین صورت نقل کرده‌اند و باک آن را با yaxšti- \"\n    \"اوستایی برابر می‌داند. آنچه اثبات نشده پدرِ آن است: ویکی‌واژه ریشهٔ yaṣṭi- را ناشناخته می‌داند و باک پیوندِ \"\n    \"ریشه‌ای را «مشکوک» می‌خواند؛ پس برآمدن از *l(j)akti- هندواروپایی تنها یک فرضِ کنارگذاشته است. نکتهٔ دیگر آنکه \"\n    \"نمودار، yaṣṭi- سنسکریت و yaxšti- اوستایی را دو شاخهٔ جدا از ریشه کشیده، حال آنکه این دو بازتابِ هندوآریایی و \"\n    \"ایرانیِ یک واژهٔ هندوایرانی‌اند.\"),\n  \"sources\": [W_YASTI],\n  \"ref_check\": [\n    {\"ref\": \"WLD2:443\", \"status\": \"supports\",\n     \"note\": WLD_QUOTE + \" — 'ai. yaṣṭi-ḥ „Stab, Stock“' is the very word of this node.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SYN\", \"where\": \"Buck §8.55 BRANCH, p.525\", \"stance\": \"partial\",\n     \"note\": SYN_QUOTE + \" — the word and its Avestan equation are accepted, the root is called dubious.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. lakstis (IEC.txt line 9447)\", \"stance\": \"contradicts\",\n     \"note\": \"Mann's *lakt- 'stick' collects Pali laṭṭhi with Skt. lakuṭaḥ 'cudgel', Arm. laxt, Gk. laktis, Lith. laktà — and pointedly omits Skt. yaṣṭi-, i.e. he does not derive yaṣṭi- from this root.\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.510 s.v. LATTEE\", \"stance\": \"supports\",\n     \"note\": \"'This is from Prakrit laṭṭhi, for Skt. yaṣṭi, \\\"a stick\\\", according to the Prakrit grammar of Vararuchi (ed. Cowell ii.32); see also Lassen, Institutiones Ling. Prakrit. 195.'\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. यष्टि (Sanskrit)\", \"stance\": \"partial\",\n     \"note\": \"Meanings 'staff, stick, wand, rod, mace, club … stalk, stem, branch, twig'; descendants Pali yaṭṭhi, Hindi लाठी; etymology 'unknown origins'.\"}\n  ]\n },\n {\n  \"id\": 4,\n  \"lang\": \"Hindustani\",\n  \"words\": \"lathi\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Hindi/Urdu लاठी lāṭhī 'a stick, a club, a bludgeon, often a solid male-bamboo staff ringed and ferruled with \"\n    \"iron' (Whitworth, Anglo-Indian Dictionary, s.v. Lāthī). Hobson-Jobson p.510 s.v. LATTEE states the descent that \"\n    \"the chart draws: 'The word is Hind. lāṭhī and laṭhī, Mahr. laṭhṭhā. This is from Prakrit laṭṭhi, for Skt. yaṣṭi, \"\n    \"\\\"a stick\\\", according to the Prakrit grammar of Vararuchi (ed. Cowell ii.32).' Phonetically: Skt. yaṣṭi- gives \"\n    \"Middle Indic yaṭṭhi (so Pali) by assimilation of the cluster -ṣṭ- to -ṭṭh-; Prakrit substitutes l- for y- (per \"\n    \"Vararuchi's rule; modern accounts, e.g. Wiktionary, prefer contamination with lakuṭa- 'club'), giving laṭṭhi; \"\n    \"New Indo-Aryan then degeminates -ṭṭh- > -ṭh- with compensatory lengthening of the preceding vowel, laṭṭhi > \"\n    \"lāṭhī. The chart's arrow Sanskrit → Hindustani is right, only compressed: it passes through Middle Indic.\"),\n  \"derivation_fa\": (\n    \"هندی/اردو لاٹھی (lāṭhī) به معنی «چوب‌دست، چماق»، بیشتر عصایی از خیزرانِ توپُر که با حلقه‌های آهنی بسته شده است \"\n    \"(ویتورث، فرهنگ انگلیسی–هندی، ذیل Lāthī). هابسن–جابسن در ص۵۱۰ همان مسیری را می‌دهد که نمودار کشیده است: «این واژه \"\n    \"هندیِ lāṭhī و laṭhī و مراتیِ laṭhṭhā است، و آن از laṭṭhiِ پراکریت است در برابرِ yaṣṭiِ سنسکریت «چوب»، بنا بر \"\n    \"دستورِ پراکریتِ ورَرُچی». از نظر آوایی: خوشهٔ -ṣṭ- سنسکریت در هندیِ میانه به -ṭṭh- همگون شده (پالی yaṭṭhi)، در \"\n    \"پراکریت «ی» آغازین به «ل» بدل شده (به گفتهٔ پژوهش‌های امروزی بر اثر آمیختگی با lakuṭa «چماق»)، و سرانجام در \"\n    \"هندیِ نو همخوانِ مشدّد ساده و واکهٔ پیشین کشیده شده است: laṭṭhi > lāṭhī. پیکانِ «سنسکریت ← هندی» درست است، فقط \"\n    \"مرحلهٔ هندیِ میانه را در خود فشرده کرده.\"),\n  \"sources\": [W_YASTI],\n  \"ref_check\": [\n    {\"ref\": \"HJB:510\", \"status\": \"supports\",\n     \"note\": \"Hobson-Jobson (2nd ed. 1903) p.510, s.v. LATTEE (HJB.txt line 13117; the page number 510 is printed in the running head 'LATERITE. 510 LAW-OFFICER'): 'LATTEE, s. A stick; a bludgeon, often made of the male bamboo (Dendrocalamus strictus), and sometimes bound at short intervals with iron rings … The word is Hind. lāṭhī and laṭhī, Mahr. laṭhṭhā. This is from Prakrit laṭṭhi, for Skt. yaṣṭi, \\\"a stick\\\" …'. The index confirms 'Lāth, Lathi, 509b, 510a'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary, s.v. Lāthī (AID.txt line 4064)\", \"stance\": \"supports\",\n     \"note\": \"'Lāthī. [Hindustani.] A stick, a club, a bludgeon; often a bamboo heavily ringed and ferruled.' — the node's gloss 'stick, club' verbatim; 'Lattee. See Lāthi.'\"},\n    {\"src\": \"KLN\", \"where\": \"p.868 s.v. lathi\", \"stance\": \"supports\",\n     \"note\": \"'Hind. lathi, fr. Prakrit latthi, \\\"staff, stick, rod, club\\\", which is rel. to OI. yaṣṭih of s.m., Avestic yaxshti-, \\\"branch\\\".'\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. यष्टि, descendants\", \"stance\": \"supports\",\n     \"note\": \"Descendants include Hindi लाठी (lāṭhī) and Bengali লাঠি (laṭhi), from the Prakrit form.\"}\n  ]\n },\n {\n  \"id\": 5,\n  \"lang\": \"English\",\n  \"words\": \"lathi\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"An Anglo-Indian borrowing of Hindi lāṭhī, taken over in British India in the 19th century for the iron-bound \"\n    \"bamboo staff carried by watchmen, hired strong-arm men (lāṭhīwālā, Hobson-Jobson's LATTEEAL) and later by the \"\n    \"police; Hobson-Jobson quotes it from 1878 ('about 100 men seated in rows on the roadside, all with lattīs') and \"\n    \"1880 ('a very heavy lāthi, a solid male bamboo, 5 feet 5 inches long, headed with iron'). Klein p.868 — the page \"\n    \"Nourai cites — has the whole chain in one line: 'lathi, also lathee, n., a heavy wooden staff bound with iron \"\n    \"(India). — Hind. lathi, fr. Prakrit latthi, \\\"staff, stick, rod, club\\\", which is rel. to OI. yaṣṭih of s.m., \"\n    \"Avestic yaxshti-, \\\"branch\\\".' English spellings lathi/lathee both occur; the modern derivative is lathi charge. \"\n    \"Nothing here is in doubt.\"),\n  \"derivation_fa\": (\n    \"وام‌واژه‌ای انگلیسی–هندی از هندیِ lāṭhī که در سدهٔ نوزدهم در هندِ بریتانیایی وارد انگلیسی شد، برای همان عصای \"\n    \"خیزرانِ آهن‌بسته که پاسبانان و «لاٹھی‌والا»ها و بعدها پلیس به کار می‌بردند؛ هابسن–جابسن نمونه‌های ۱۸۷۸ و ۱۸۸۰ را \"\n    \"نقل می‌کند. کلاین در همان ص۸۶۸ که نورایی به آن ارجاع داده، تمامِ زنجیره را در یک سطر آورده است: «lathi، همچنین \"\n    \"lathee: عصای سنگینِ چوبی با بندِ آهنی (هند) — از هندیِ lathi، از پراکریتِ latthi «چوب، عصا، چماق»، هم‌ریشه با \"\n    \"yaṣṭiḥ سنسکریت و yaxšti- اوستایی «شاخه»». املای lathi و lathee هر دو رایج است. در این حلقه تردیدی نیست.\"),\n  \"sources\": [W_YASTI],\n  \"ref_check\": [\n    {\"ref\": \"KLN:868\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 p.868 (KLN_1966.txt line 21216, leaf 466, whose printed page number '868' is on the leaf): 'lathi, also lathee, n., a heavy wooden staff bound with iron (India). — Hind. lathi, fr. Prakrit latthi, \\\"staff, stick, rod, club\\\", which is rel. to OI. yaṣṭih of s.m., Avestic yaxshti-, \\\"branch\\\".' Also 'lathee, n. — See lathi.' (line 21214).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.510 s.vv. LATTEE, LATTEEAL\", \"stance\": \"supports\",\n     \"note\": \"Anglo-Indian usage with quotations of 1878 and 1880; 'LATTEEAL, s. Hind. lāṭhiyāl … \\\"a clubman\\\", a hired ruffian.'\"},\n    {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary, s.vv. Lāthī, Lattee\", \"stance\": \"supports\",\n     \"note\": \"The word is listed as an Anglo-Indian word: 'Lāthī. [Hindustani.] A stick, a club, a bludgeon'; 'Lattee. See Lāthi.'\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. lathi (English)\", \"stance\": \"supports\",\n     \"note\": \"'Borrowed from Hindi लाठी (lāṭhī)', citing the OED.\"}\n  ]\n }\n]\n\nout = {\n  \"pdf_page\": 301,\n  \"book_page\": 271,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [entry0, entry4]\n}\n\nwith open(\"data/verification/page-301.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk301.py && python3 -m json.tool data/verification/page-301.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 301",
 "description": "Write and validate page-301 verification"
}
```


### [2026-09-06T23:05:23.003Z] TOOL RESULT

```
written
JSON OK
nodes verified: 9/9
node verdicts: {'disputed': 1, 'confirmed': 5, 'plausible': 2, 'unverified': 1}
root verdicts: {'disputed': 2}
ref checks: {'not_checked': 3, 'partial': 1, 'supports': 14}
books consulted: {'partial': 7, 'silent': 2, 'contradicts': 2, 'supports': 21} | by book: {'Wiktionary': 6, 'SKT': 3, 'KLN': 3, 'WEB': 2, 'LKT': 2, 'Etymonline': 2, 'SYN': 2, 'HJB': 2, 'AID': 2, 'BQT': 1, 'MON': 1, 'HRN': 1, 'HUB': 1, 'BRT': 1, 'WLD': 1, 'BOOK': 1, 'IEC': 1}
```


## [2026-09-06T23:05:28.973Z] TOOL CALL #58: Bash

```json
{
 "command": "grep -n \"۱۳\" data/verification/page-301.json | head -5",
 "description": "Find the mangled numeral"
}
```


### [2026-09-06T23:05:29.018Z] TOOL RESULT

```
13:      "note_fa": "نورایی نام یک قبیلهٔ ترک، «لاجین»، را سرِ خانوادهٔ «لاجورد» گذاشته است. خودِ واژه واقعی است: دهخدا «لاجین» را «قبیله‌ای است از ترکان نواحی بلخ» معنی کرده و ظاهراً نورایی آن را از جلد ششم فرهنگ معین (اعلام) گرفته است. اما پیوندِ این نام با «لاژورد» در هیچ منبعی نیامده: کلاین (ص۱۳۷)، اسکیت، وبستر، فرهنگ American Heritage، لوکوچ (شمارهٔ ۱۳�११) و ویکی‌واژه همگی «لاژورد» را از نام جایی در بدخشان (معدن‌های سرِ سنگ) می‌دانند که سنگ لاجورد از آنجا می‌آمد؛ حدودالعالم (۳۷۲ ق/۹۸۲ م) هم از «معدن‌های سیم و زر و لعل و لاجورد» بدخشان یاد کرده است. ویکی‌واژه خودِ آن نام‌جای را ایرانی می‌داند و جزء دوم آن را با ایرانی *varta- «سنگ» می‌سنجد؛ لوکوچ نیز فرضِ کهن‌ترِ برگرفتگی از سنسکریت rājāvarta «طرّهٔ شاه» را نقل می‌کند. پس «لاجین» و «لاژورد» دو واژهٔ بی‌ربط‌اند که تنها آغازشان شبیه است و برچسب «ترکی» هم درست نیست، چون lacivert ترکی خود وام‌واژه‌ای از فارسی است. داوری: پژوهش امروزی ادعای نورایی را رد می‌کند.",
66:          "derivation_fa": "در این جعبه سه واژهٔ جدا کنار هم نشسته‌اند. «لاجین» به‌راستی نام قبیله‌ای ترک است و تکرارِ همان سرواژه در فارسی است؛ ایرادی ندارد. اما «لاجورد» (نام‌جای) و «لاجورد» (سنگ کبود و رنگ آن) را نمی‌توان به آن بست. صورت کهن‌تر فارسی «لاژورد» با زای فارسی است — برهان قاطع: «لاژورد، با زای فارسی، بر وزن و معنی لاجورد است و آن سنگی است کبود که نقاشان و مصوران بکار برند» — و «لازورد» صورتِ معرّب است که دوباره به فارسی بازگشته (حاشیهٔ معین بر همان مدخل: «لاژورد > لازورد (معرّب)»). کلاین (ص۱۳۷) و اسکیت نام سنگ را از نام‌جای «لاژورد» می‌دانند، یعنی معدن‌های سرِ سنگِ بدخشان که مارکوپولو و پیش از او حدودالعالم از آن یاد کرده‌اند؛ ویکی‌واژه خودِ نام‌جای را ایرانی می‌شمارد (جزء دوم آن هم‌ریشه با ایرانی *varta- «سنگ») و لوکوچ فرضِ سنسکریت rājāvarta را نقل می‌کند. پس تحول معنایی «نام معدن ← سنگِ آن ← رنگ کبود» درست است، ولی پیوند با قبیلهٔ «لاجین» را هیچ منبعی تأیید نمی‌کند و ریشه‌شناسی عامیانه می‌نماید.",
178:          "derivation_fa": "«اللازورد» عربی در سدهٔ ۱۲–۱۳ میلادی، از راه نهضت ترجمهٔ عربی به لاتینی و نیز تجارت رنگ‌دانه، وارد لاتینیِ میانه شد: lazur/lazurium و با پسوندنمای -ulum به شکل lazulum، و ترکیب lapis lazulī «سنگِ لاجورد». در کنار آن خانوادهٔ بی‌«ل» پدید آمد: در زبان‌های رومی، «ل» آغازین را حرف تعریف پنداشتند (ایتالیایی l'azzurro، فرانسهٔ کهن l'azur) و آن را انداختند؛ نتیجه azzurum/azura در لاتینی میانه، azzurro ایتالیایی، azur فرانسوی و azul اسپانیایی است. یادداشتِ خودِ نورایی در این جعبه عیناً سخن کلاین است و اسکیت، وبستر و لوکوچ نیز همین را می‌گویند. تنها نکته آنکه هر دو واژه لاتینیِ میانه‌اند نه لاتینیِ کلاسیک، و برچسبِ سادهٔ «Latin» این تمایز را می‌پوشاند. ادعای نورایی درست است.",
```


## [2026-09-06T23:05:37.030Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-301.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        print(e['entry'], n['id'], n.get('lang'), '|', (n.get('derivation_fa') or '')[:60])\nEOF",
 "description": "Check node ordering of Persian texts"
}
```


### [2026-09-06T23:05:38.967Z] TOOL RESULT

```
0 1 Persian | در این جعبه سه واژهٔ جدا کنار هم نشسته‌اند. «لاجین» به‌راستی
0 2 Arabic | «لاژورد» فارسی به عربی رفت و به صورت «لازورد» (با ال تعریف: 
0 3 Latin | «اللازورد» عربی در سدهٔ ۱۲–۱۳ میلادی، از راه نهضت ترجمهٔ عرب
0 4 English | azure از انگلیسی میانه asur/azur و آن از فرانسهٔ کهن azur (س
4 1 Avestan | واژه‌های اوستایی درست‌اند: در اوستای نو yaxšti- (ستاک yaxšta
4 2 None | این جعبه تهی است. تصویر صفحهٔ چاپی (برگ ۳۰۱ پی‌دی‌اف، نگهدار
4 3 Sanskrit | سنسکریت यष्टि (yaṣṭí-)، فاعلیِ مفرد yaṣṭíḥ؛ آنچه نورایی «yaš
4 4 Hindustani | هندی/اردو لاٹھی (lāṭhī) به معنی «چوب‌دست، چماق»، بیشتر عصایی
4 5 English | وام‌واژه‌ای انگلیسی–هندی از هندیِ lāṭhī که در سدهٔ نوزدهم در
```


## [2026-09-06T23:05:46.602Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport io\np='data/verification/page-301.json'\ns=io.open(p,encoding='utf-8').read()\nbad='لوکوچ (شمارهٔ ۱۳�११)'\nimport re\nnew,n=re.subn(r'لوکوچ \\(شمارهٔ ۱۳[^)]*\\)','لوکوچ (شمارهٔ ۱۳۱۱)',s)\nprint('replaced',n)\nio.open(p,'w',encoding='utf-8').write(new)\nEOF\npython3 -m json.tool data/verification/page-301.json >/dev/null && echo \"JSON OK\" && grep -o \"لوکوچ (شمارهٔ ۱۳۱۱)\" data/verification/page-301.json && python3 tools/verify_check.py 301",
 "description": "Fix mangled Persian numeral and re-check"
}
```


### [2026-09-06T23:05:49.124Z] TOOL RESULT

```
replaced 1
JSON OK
لوکوچ (شمارهٔ ۱۳۱۱)
nodes verified: 9/9
node verdicts: {'disputed': 1, 'confirmed': 5, 'plausible': 2, 'unverified': 1}
root verdicts: {'disputed': 2}
ref checks: {'not_checked': 3, 'partial': 1, 'supports': 14}
books consulted: {'partial': 7, 'silent': 2, 'contradicts': 2, 'supports': 21} | by book: {'Wiktionary': 6, 'SKT': 3, 'KLN': 3, 'WEB': 2, 'LKT': 2, 'Etymonline': 2, 'SYN': 2, 'HJB': 2, 'AID': 2, 'BQT': 1, 'MON': 1, 'HRN': 1, 'HUB': 1, 'BRT': 1, 'WLD': 1, 'BOOK': 1, 'IEC': 1}
```


## [2026-09-06T23:06:08.918Z] AGENT

Page 301 (book p. 271) verified — `python3 tools/verify_check.py 301` shows **0 PROBLEM lines** (9/9 nodes).

**Counts** — roots: 2 disputed. Nodes: 5 confirmed, 2 plausible, 1 disputed, 1 unverified. Ref checks: 14 supports, 1 partial, 3 not_checked.

**Disputed / flagged**
- ROOT *Lâjîn* (Turkish, "name of a Turkish tribe") — the tribe name لاجین is real (Dehkhoda: «قبیله‌ای است از ترکان نواحی بلخ»), but nothing derives لاژورد from it. Klein 137, Skeat, Webster, AHD, Lokotsch 1311 and Wiktionary all derive Pers. lāžvard from the Badakhshan **place-name** Lāžvard (Sar-e Sang mines; Hudūd al-ʿĀlam 982); Lokotsch adds the Skt *rājāvarta* alternative. "Turkish" is also the wrong label (Turkish *lacivert* is a loan from Persian).
- Entry 0 #1 (Persian *Lâjîn; Lâj-vard; lâjvard*) — same reason: the words and the place→stone→colour shift are right, the arrow from the tribe name is not; KLN:137 supports only the place-name route (marked `partial`).
- ROOT *Lakti, Ljakti* (IE, WLD2:443) — the citation is exact ("l(j)akti- „Stab“", WLD II 443, leaf 448), but WLD merely reports Schulze 1912 and ends with "?"; Pokorny 1959 dropped it, Watkins has no such root, Buck 8.55 says "root connections dub.", Mann's *lakt- excludes yaṣṭi-, and Wiktionary makes Skt yaṣṭi- of unknown origin with the l- from contamination with *lakuṭa*. Also "club" is Nourai's addition (WLD glosses only "Stab").
- Entry 4 #1 Avestan and #3 Sanskrit are `plausible`: the words and the yaxšti-/yaṣṭi- equation are certain (BRT col. 1236 — Buck independently cites "Barth. 809, 1236"), only the parent root fails.

**No extraction errors.** The JSON matches the printed page exactly, including node #2 of entry 4, which is a genuinely blank box in the book (page image saved to `data/verification/sources/refs/ocr/BOOK/301.png`). Minor book-side looseness only: Bartholomae glosses θri.yaxštay- as the plural "drei Zweige" ('three branches'), not "with three branches"; and azulene comes via Spanish *azul* (Klein), not straight from Latin.

New files: `data/verification/page-301.json`; `data/verification/sources/refs/ocr/AFM/0141.png` + `0141.vision.txt` (Addi Shir p.141 = AFM.pdf p.143, "(اللازورد) معدن مشهور تعريب لاژورد"); `.../ocr/BOOK/301.png`; 5 archived web sources via `fetch_source.py`.
