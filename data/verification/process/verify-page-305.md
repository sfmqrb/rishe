# Verification process log — verify-page-305


## [2026-09-06T22:56:01.235Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 305 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-305.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-305.json. Write /home/sfmqrb/git/rishe/data/verification/page-305.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 305` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:56:02.412Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:56:03.385Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:56:03.401Z] TOOL RESULT

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


## [2026-09-06T22:56:03.864Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-305.txt"
}
```


### [2026-09-06T22:56:03.881Z] TOOL RESULT

```
1	=== PDF page 305 (book page 275) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Legwh : light in weight, quick in movement  (refs POK:660)
4	#1 (parent #0) [Persian] refs=IEC:700, MON:3530 | lâğar «لاغر» : lean
5	#2 (parent #0) [Avestan] refs=POK:660 | ragu, ravi : quick
6	#3 (parent #0) [Germanic] refs=AHD:1525 | lihtjaz : light in weight
7	  #4 (parent #3) [English] refs=AHD | light 2
8	#5 (parent #0) [Latin] refs=AHD:1525 | levis : of low weight ; levâr : lift ; carni-levâre : reduce weight, a feast before fasting ☞Sek
9	  #6 (parent #5) [English] refs=AHD | leaven, lever, alleviate, carnival, elevate, relieve
10	  #7 (parent #5) [French] refs=None | carnaval
11	    #8 (parent #7) [Persian] refs=VOP:269 | kârnâval «کارناوال» : carnival
12	--- entry 1 ---
13	ROOT [Indo-European] Lěi, Lôi : slime, sticky  (refs POK:662; IEC:706)
14	#1 (parent #0) [Persian] refs=IEC:706 | lây «لای» : mud, sediment | extra: گل و لای ، لایروبی
15	#2 (parent #0) [Sanskrit] refs=IEC:706 | layah : adherence
16	#3 (parent #0) [Old English] refs=AHD:1216 | slim : mud
17	  #4 (parent #3) [English] refs=AHD | slime
18	#5 (parent #0) [Latin] refs=POK:662 | limere : to smear ; lîmus : slime
19	--- entry 2 ---
20	ROOT Lei -> redirect to El 3
21	
```


## [2026-09-06T22:56:07.357Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-305.json",
 "description": "Read source JSON for page 305"
}
```


### [2026-09-06T22:56:07.414Z] TOOL RESULT

```
{
  "pdf_page": 305,
  "book_page": 275,
  "entries": [
    {
      "root": {
        "name": "Legwh",
        "lang": "Indo-European",
        "refs": "POK:660",
        "gloss": "light in weight, quick in movement"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:700, MON:3530",
          "words": [
            {"translit": "lâğar", "gloss": "lean", "script": "لاغر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "بود کو بجای تو کمتر بود - هم از رشک مهر تو لاغر شود", "poet": "Ferdowsî"}
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:660",
          "words": [
            {"translit": "ragu, ravi", "gloss": "quick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1525",
          "words": [
            {"translit": "lihtjaz", "gloss": "light in weight", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "light 2", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1525",
          "words": [
            {"translit": "levis", "gloss": "of low weight", "script": null},
            {"translit": "levâr", "gloss": "lift", "script": null},
            {"translit": "carni-levâre", "gloss": "reduce weight, a feast before fasting", "script": null, "see": ["Sek"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "leaven, lever, alleviate, carnival, elevate, relieve", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "carnaval", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "VOP:269",
          "words": [
            {"translit": "kârnâval", "gloss": "carnival", "script": "کارناوال"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Lěi, Lôi",
        "lang": "Indo-European",
        "refs": "POK:662; IEC:706",
        "gloss": "slime, sticky"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:706",
          "words": [
            {"translit": "lây", "gloss": "mud, sediment", "script": "لای"}
          ],
          "script_extra": "گل و لای ، لایروبی",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:706",
          "words": [
            {"translit": "layah", "gloss": "adherence", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old English",
          "refs": "AHD:1216",
          "words": [
            {"translit": "slim", "gloss": "mud", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "slime", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:662",
          "words": [
            {"translit": "limere", "gloss": "to smear", "script": null},
            {"translit": "lîmus", "gloss": "slime", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Lei",
        "redirect": "El 3"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T22:56:08.153Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:56:08.200Z] TOOL RESULT

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


## [2026-09-06T22:56:27.431Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -30 && python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','AHD','MON','VOP','WLD','SYN','KLN','LEW','LAT','HRN','HUB','BRT','SKT','ARY','SIN']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-06T22:56:27.882Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,60p tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-06T22:56:29.740Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_f
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnair
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = p
```


### [2026-09-06T22:56:29.881Z] TOOL RESULT

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
```


## [2026-09-06T22:56:34.636Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -m5 \"leng\\?u\\?h\\|leg.h-\" POK_full.txt | head -20; echo ---; grep -n \"660\" POK_full.txt | head -5",
 "description": "Grep Pokorny for legwh"
}
```


### [2026-09-06T22:56:34.700Z] TOOL RESULT

```
23798:Trautmann 125, MiJhlenhach-Endzelin I 509, Endzelin Latvian Gr. 358. 
29728:5. nasalized glengh- : Old High German k//ngan'r\ng, sound, clink' (without close 
55041:Unclear, whether to connect with lengh- "vilify, scold' (Osthoff MU. VI 7 ff.) 
68291:lemma: leg^h-: light (adj.), lung. 
79821:Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- 
---
33403:References: WP. I 660 f., Trautmann 91. 
33498:References: WP. I 640, WH. I 660 f., 662 f. 
36922:References: WP. I 603 f., WH. I 242 f., 660, 857. 
38281:References: WP. I 660, WH. I 608. 
54361:Page(s): 660-661
```


## [2026-09-06T22:56:35.781Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -40 POK_full.txt; echo ===; wc -l POK_full.txt POK_01.txt POK_02.txt POK_03.txt",
 "description": "Inspect Pokorny files"
}
```


### [2026-09-06T22:56:35.828Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-06T22:56:38.628Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 68280,68400p POK_full.txt",
 "description": "Print Pokorny legwh entry"
}
```


### [2026-09-06T22:56:38.692Z] TOOL RESULT

```
Page(s): 837 

Root / lemma: pl(e)u-mon-, pleu-tio- 

Meaning: lung 

Note: 

Root / lemma: pl(e)u-mon-, pleu-tio- : lung, derived from Slavic alb. prefix pe- + Root / 

lemma: leg^h-: light (adj.), lung. 

Material: Old Indie kl6man-xr\. n. 'die right lung ' (Dissim. from p- m\.o k- m) = gr. 

nA£U[JU)v " lungs ' (through support in nvsw also nv£U|JU)v); Latin pulmo, mostly PI. ' lungs ' 

(from *pelmdnesor *plum6nes)\ 

Balto-Slavic *pleutia- and *plautia- n. PI. in Lithuanian p/auc/a/ an6 Latvian plausi, 
plausas m. PI., Old Prussian p/aut/ {secondary f.) ' lungs '; Old Church Slavic p/usta and 
*pljustan. PI. (Old Russian pljuca^ lungs '), serb. pljucai. 'liver'. 

The Lunge schwimmt auf dem Wasser, also as "Schwimmer' to pleu- (pel-) "ttAeoj'. 

References: WP. II 95 f., WH. II 386 f., Trautmann 226. 
Page(s): 837-838 

Root / lemma: pleus- 

Meaning: to pluck; plucked hair, feathers, fell 

Material: Latin /7/J/77aTlaumfeder, fluff, underfur' {*plusma)\ Middle Low German vlus, 

vlusch^ fleece, fleece', nnd. vlOs(e), vlusch' tussock hair, BiJschel Wolle', Middle High 

German vlius {*flusi-) "fleece'. Modern High German Flaus, Flauscfr, Middle High German 

vlies. Modern High German Vlies, 

Old English fleos, fITesn. ds., with gramm. variation Norwegian flura ^zoiWges hair'; Old 
Icelandic /7c»sa "splinter, offal', Norwegian dial, flos, flus(k), flustrds. and " dandruff, scale 



auf dem Kopfe', as Latvian p/auskas and plaukstes' dandruff, Latvian plusnr\n Winde 
flatternde birch bark ', Lithuanian pliusinti^xub, wear out', yO/Jsa'Bastfasern' (in addition 
p//use'ree6') etc.; 

Lithuanian pluskosP\. "Haarzotten, hair', Latvian p/uskas ^Zotten, rag', ablaut, plauskas 
f. PI. "Schelfer'; Lithuanian yC>/5i/zo'//7/s"(Feder)bett, Deckbett', Old Prussian (with g- 
insertion) plauxdine "feather-bed'. 

References: WP. II 96 f., Trautmann 227. 
Page(s): 838 

Root / lemma: pleu- 

Meaning: to run, flow; to swim 

Note: probably extension from pel- "flow, swim', and originally ds. as pel(eu)- "fijllen voir 

("Uberfluft, iJberflieftend') 

Material: Old Indie /0/ai/a/e"schwimmt, hovers, flies' (= gr. ttAeu), Latin perplovere. Old 

Church Slavic plovg), yO/'5i/a/e "springt auf, hurries ' (here and in Avestan ava nifravayenta 

"sie lassen in Fluge heimkehren', usfravanfe'{6\e Wolken) steigen auf kann also ein Indo 

Germanic yOAe^- "spring' vorliegen); Kaus. p/avayat/" aWows swim, iJberschwemmt' (= serb. 

ploviti. Old High German flouwen, flewen); 

lengthened grade Old Indie /0/5i/aya//"allows swim', Avestan usfravayd/t'6aQ> er 
wegschwemmen could' (= Old Church S\av\c p/av/Jg, plaviti 'swim let, schwemmen'); 

yO/aKa-"schwimmend; m. boat, bark, type of sailboat' (= russ. plo\/)\ pluta- 
"ijberschwemmt' (= gr. ttAut6(; " washed, made clean '), pluti- f. "Uberflieflen, flood' (= gr. 
ttAuok; "the washing'), uda-pru-t- "in Wasser schwimmend'; 

arm luanam, Aor. /uap/'wasW ( *plu(")a-); 

gr. nA£(F)u) (snAsuaa, nAsuaopai) "schiffe, schwimme' (Inf. Ionian hAeeiv, nAoJaai 
"schiffen', but nAcbsiv, nAoJaai "swim'); Ionian -nkooc,, Attic nAou(; m. "Schiffahrf, (=klr. 
plo]/}, nAoTov "vessel' (= Old Icelandic /fey "ship'); nAuvw "wash' (*ttAu-v-iu); Put. nAuvu), 
Aor. Pass. snAuGnv), nAuvoq m. "Waschgrube', nAupa n. "Spulichf, nAuT6(;, hAugk; (see 
above); ttAouto^ m. "Fulle, richness '; from the lengthened grade p/ofuj- besides ttAu)£iv, 
nAwaai (see above), EnsnAwv "beschiffte', hAcjotoc; "schwimmend, fahrbar', hom. 
5aKpunAu)£iv "in Tranen swim' (from *5aKpunAcbq); 

lllyrian FIN P/ai//s.' Lithuanian sea N. Plavos, 



Latin perp/overe (Fest) "durchsickern let, leek sein', p/ovebat (Petron.), pluit, -eAe'rain'; 
pluvius, p/uor'ra\r\'; 

Old Irish /oun' trip food ', /oan, /oon'a6eps' {*ploUeno-, see below Middle Low German 
flome); Old Irish A/- 'move', Abstr. luud^ actuation ', /uud'anes = Mauerbrecher'; also cet- 
/i/o'" coitus'; e5S-cc»/77-A/-'proficisci', ess-/u-' leave, depart, entkommen', fo-/u-l\y', luamain 
"das Fliegen', A/a//? 'quick, fast', luas^ quickness '; Old Irish lu(a)ei. ' rudder, helm, 
calcaneus, tail', {*pluuia), cymr. //yw\u\er, tax, tail', acorn, /oe 'ruler'. Middle Irish /uam 
'Steuermann', cymr. llong-lywydd6s., bret. Ievier6s.\ 

Old High German causative flouwen, flewen^ rinse, wash' (= Old \v\6\c plavayati). Old 
Icelandic /7ai//77/''current', Old High German /7c>^/r7'colluvies; fat (obenschwimmend)'. 
Middle Low German flomei. ' raw Bauch- and Nierenfett', Modern High German Flom, 
Flaumru. ds.. Old Icelandic fley{= ttAoTov, *plouiom) n. 'ship'; Old Icelandic fludi. 'blinde 
cliff (i.e. 'iJberflutete'; 0: d[u]: eu)\ ple-\v\ Middle High German vleejen^ rinse '; pld[u]-\v\ 
Old Icelandic floa. Old English flowan^ overflow ', Gothic flddus{: nAwTOc;), Old Icelandic 
flodi. n.. Old High German /7^c»/ 'flood'. Old Icelandic floim. 'swamp, marsh'; 

Lithuanian causative plauju, ploviau, p/aut/^wash, rinse ', Put. plausiu ( *pldusid)\ plutis 
"offene place in Else'; yO/ei/es^oZ/'flutter'; 

Old Church S\ay\c plovg, pluti^i\o\N, schiffe', yO/^ip'schwimme', Kaus.-lter. serb. ploviti 
'schwemmen, swim', russ. /O/oi/'boat', kir. p/oi/'natatio', lengthened grade Old Church 
S\ay\c plaviti 'swim let', -5^'navigare', plavati 'swim'; serb. plutai., plutou. 'cork'; *plu-\v\ 
Inf. russ. plytb, serb. pITtr,
```


## [2026-09-06T22:56:39.494Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 66[0-3]\" POK_full.txt",
 "description": "Find Pokorny pages 660-663"
}
```


### [2026-09-06T22:56:39.543Z] TOOL RESULT

```
54361:Page(s): 660-661 
54701:Page(s): 661-662 
54838:Page(s): 662-664 
56474:Page(s): 660 
56495:Page(s): 660 
56522:Page(s): 661
```


## [2026-09-06T22:56:42.713Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 54290,54370p POK_full.txt; echo \"=== 54700 ===\"; sed -n 54690,54850p POK_full.txt",
 "description": "Print Pokorny pages 660-662 entries"
}
```


### [2026-09-06T22:56:42.784Z] TOOL RESULT

```
collect ', llgatufs^ to bring together, gather, collect ' and legumen^ legume, pod vegetable, 
bean '; 

Germanic *lekja- ' sayer of a magic spell, physician, medicine man' in Gothic lekels. Old 
Icelandic laeknir. Old English laece. Old High German lachr, in addition Old High German 
lachlnu. 'healing'. Middle High German lachenTei. ' sayer of a magic spell, witch '; Church 
Slavic Ieki3 'remedy' from Germanic; about Old Irish llalgsee below /ep-1. 

References: WP. II 422, WH. 351 ff., 779 f., 789 f. 
Page(s): 658 

Root / lemma: lehg^h- {*lehug''h- ) 
Meaning: light (adj.) 



Note: nasalized lehng^h- 

Material: 1. Old Indie laghu-, ved. raghu-'rash, hasty, light, small', Kompar. laghTyarhs-, 
Superl. laghistha-; Avestan ragu-, f. /"aiz/'agile'; Kompar. ranjyo, Superl. ranjista- (of stem 
* length-); 

zero grade Old \u6\crhant- "weak, small' ("*light'); Avestan ranjaiti, ranjaye/t/" makes 
light, agile, allows to be moved'. Old Indie rarhhate, rarjghati, larjghati^ runs, it hurries, 
jumps up, jumps about '; 

gr. sAaxuc; "small', Kompar. sAaoawv, Attic sAdTTwv (with secondary a, s. Schwyzer Gr. 
Gr. 1 , 538 and Anm. 4), Superl. zKcxY^a^oc, (£Aaxu(; from Indo Germanic *leg"'hu-, as Slavic 
lbgi>ki> and Celtic *lag-. Old Indie laghu- perhaps also or zero grade as Latin levis); 
£Aa(pp6(; "light, agile' (probably from *lng"hr6s= Old High German lungai); after Schwyzer 
Gr. Gr. 1 , 302 though contaminated from *£Aaxp6(; (= Old High German lungai) and 
*£Aa(p6(; (from *-xFo(; = Lithuanian lengvas); perhaps Ionian Awcpav " recover, relax, 
slacken, trans, ease, dismiss, set free, release '; 

lllyrian lembus ( *leng"ho-s) " light vessel ', out of it gr. A£|jpo^, Latin lembus ds.; northern 
Italy FIN Lambrus{: £Aa(pp6(;), Krahe, Gymnasium 59 (1952), 79; Note: common lllyrian 
g'^-> b-. 

Latin /ei//s" light, quick, fast ' (based on f. *leg"huRo m. *leg"'hu-s); 

Old Irish Kompar. la/g/u {and laugu) "small, bad' = mcymr. Ilei, ncymr. //a/" little, small, 
petty, puny, inconsiderable ', corn. leds. bret. -/e/in abret. nahu-lei^ nothing, in no respect, 
not at all, to no purpose, in vain ' (proto Celtic *lag-ids, Indo Germanic *leg"'h-, see above), 
Superl. Old Irish lugimem and lugam, mcymr. Ileiaf, abret. lau, mcymr. llaw^sruaW (out of it 
Middle Irish lau, lu ds.), Old Irish lagat^ smallness, littleness, slightness '; Old Irish lingim 
"spring' (preterit leblaingmih analogical imitation of p: i6>-reduplication). Old Irish leimm, 
cymr. etc. //5/77 "spring' {* Ing-smen-); 

Maybe alb. {Veiht) /e/7/e "light'. 

Gothic leihts. Old English leoht. Old Icelandic lettr. Old High German ^Z?/^/; "light'. 
Modern Dutch lichtu. " placenta, afterbirth ' {*linxta-, Indo Germanic *leng"h-to-); 

Old Saxon lungor. Old High German lungar^c^uick, fast'. Old English lungrekdM. "quick, 
fast, bald' {*lng"'hro-, see above); Old High German gilingan^ vonstatten gehen, Erfolg 
naben, gelingen ', Middle High German lingen^ progress '; 



Lithuanian lengvas, lengvus, Latvian //e^s'iiglit'; 

Old Cliurcli Slavic Ihghkh {*leg"hu-, see above) 'light', Ibgota^ lightness', Old Church 
Slavic (Je) Ibze^ it is permitted ' (Dat. Sg. to Itga), po-lbdza, /0C»-/6Z5 "benefit', russ Ibzja, 
old Ibze^ it is possible, one may ', besides Ibga, ds. (etc.). 

2. Here also names of the lung (lighter than the remaining meat parts, swim on top of 
the water): Old High German lungunP\., Old English lungen. Old Norse lungau. " lung ', 
engl. lights ' lungs of an animal (especially of a sheep or pig) ', russ. legkoje ' lungs '; 
hence also Armenian /5/7y/r'" breast' (older '* lungs '; *lng"hio-). 

References: WP. II 426 f., WH. I 788 f., Trautmann 158 f., Kuiper Nasalpras. 143. 
Page(s): 660-661 

Root / lemma: /efo^-{*/ehub'^-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: ' live ' 

See also: see below /e//?-/ "besmear'. 

Page(s): 666 

=== 54700 ===
= Germanic */a/s/z'\ess, smaller'. Old English /^s, nengl. /ess, Old Saxon /esds., 
Kompar. Old English lsessa{*laisiza). Old Frisian lessa, Superl. Old English /^s/and 
laeresU engl. least. Old Frisian /erestand lest, to Crimean Gothic llsta^ little '; Old High 
German I/so Adv. " soft, smooth, mild, gentle, easy, calm ', Middle High German Adj. and 
Adv. l/se. Modern High German lelse; Old English ge-ITslan " slip, stumble, glide, slide'; 

Lithuanian Ifesas, Latvian //'ess "lean'; Lithuanian l/esti and lystr become lean ', Latvian 
Ifestds. 

References: WP. II 387 ff., WH. I 807 f., Trautmann 154, Specht Indo Germanic Dekl. 125, 
Machek Recherches 75 ff. Probably here 1 . lehlg- and lehlk-, see below S. 676. 
Page(s): 661-662 

Root / lemma: lehi-3{*lehu^ Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: slimy; to glide 

Note: various also slei- 

Material: 

In a- grade: 

Hittite: hallna- 'clay' (Tischler 131-2) 

gr. aAivu) (-Tv- from -Tvi-) " spread, anoint, smear, rub'; about ITmussee below; 

Latin lino, -ere, levT{*lehuualj (from de-levTseevns to derive deled), inum^ daub, 
besmear, anoint, to spread or rub over ', llnio, -Treds.; 

Old Irish lenaid, Perf. /r*///" follow' (actually " stick to someone '; cymr. ca/?-///? "follow' 
better to glynu, Irish glenald^ get stuck, stick '), Old Irish lenomnalb^ a smearing on a 
writing tablet, blotting out, erasure ', abret. linom " a smearing on a writing tablet, blotting 
out, erasure, correction ', Old Irish 55-/e/75//77 "besmirch, daub, smear over'; 

Latin ITmus^ earth mud, sludge, ordure, smut' {*lolmos) = Old High German lelm^ loam, 
clay ', Modern High German Lehm, Old English /a/r?" loam, clay, humus ', Old High 
German lelme^ loam, clay ', Modern High German Leimen, ablaut. Old High German Old 
English Old Icelandic ITm " glue, calc, lime, limestone ' ("* Erdmasse zum Verkleben '); 
based on a weak es-stem *loJes-0\d Icelandic lelru. " loam, clay ' {lajlz-), leira {*laizdn). 
Fem. " loamy beach, seaside '; 



Tokharian: A, B li(ya)- 'wipe away, cleanse oneself (Adams 553). 

1. Old Indie //nat/ (gramm.), layate, ITyate ITyati^ adhere; cling or press closely, stick to '; 
Una- " nestling up, snuggling up; clinging to, adjoining '; 

and Old Prussian laysoi. {*laisa) " clay, natural dampness of earth, earth clay '; in the 
meaning from a o'-extension Old Prussian laydis^ loam, clay ' and alb. leth, /edh^damp 
clay'; 

Lithuanian laistali, -yt/" make sticky, smear with loam or lime ', compare also Old Indie 
//ncfu- "slimy, slippery '; 

2. as appellation of slimy fish: 

gr. kwzuq ' mullet ', Old High German s/Io, Old English s/fw, sleo 'tench ', Lithuanian 
lynas, Latvian l?nis. Old Prussian ///7/s "tench ', russ. //nbetc. 6s.; 

3. as appellation of '(slimy) the smooth ': gr. AsToc; " smooth ': Latin /ev/s {*leiuis) " 
smooth ', gr. Kubo, " smooth, simple, inexpensive, frugal ', Kubc, and K\c„ -^bc, " smooth 
kerchief, cloth', Aiaari nsrpa " smooth rock '; Aiano(;, Attic Aiacpot; " smooth, rub or scrape 
against ' are unclear; Latin //777a "file, tool for smoothing surfaces' probably from * (s)IT-maox 
YsJ/e/'-ma {compare Old High German s//777 'mucus', sITmen^ make smooth, rub shiningly ', 
also gr. Kz\\xa% "snail'); 

Alb. lima " file, tool for smoothing surfaces ', lemof smooth with a file ' Latin loanword. 

4. with initial sound si-: 

Celtic *s//-/77-/7c»- "slimy' in Old Irish slemun^ smooth, slippery', cymr. Ilyfn^ smooth, 
even ', acymr. limnint^be smooth', abret. gur-//mun ' smooth' , Middle Breton c//-/effn^\r\ar6'; 

Old English Old Icelandic Modern Frisian Middle Low German Middle High German s//777 
"mucus' (Old High German s//777e/7 "smooth'); compare Old Icelandic s/yn. "slimy water 
plant'; 

Latvian slienasi. PI. "saliva' {*sleinas). Old Church Slavic sliny, serb. s//>7e "snot', russ. 
s//>7a "saliva'; 

5. with A'-suffix: 



gr. A£i|ja^ " snail without covering ' (out of it Latin ITmax6s.) = russ. 5///775/r 'snail'; 
compare Old Prussian s/ayxm., Lithuanian sliekasm., Latvian sliekai. " earthworm ' and 
Latvian sliekasi. PI. "saliva'; perhaps also Lithuanian seiles, Latvian seilasi. PI. "saliva' 
(from *s/e/7as7). 

6. extensions: 

(sJ/e/b-^sWrny, slippery, glide, slide, darijber stroke, smooth'. 

Gr. 6Aipp6(; " slippery, smooth ' Hes., oAipa^ai oAiansTv Hes.; 

perhaps cymr. //y/r? "sharp', bret. /e/r7/77 "sharp; sharp side of a knife' (as *slibsm6s)\ 

Old High German sITfan^ glide, slip; sharpen smoothly ', Modern High German schleifen. 
Middle Low German sITpen^ sharpen, make smooth; intr. slink'. Old English toslTpan^ 
dissolve, melt '; Old Icelandic sITpari^ grinder', sleipr^ slippery, smooth ' = Middle High 
German s/e/f6s., Old English s//por, Old High German s/effar6s., Norwegian s//pra'g\\6e, 
slide', Kaus. Middle Low German s/epen'drag, sharpen ' (out of it Modern High German 
schleppen). Old High German Middle High German s/e/fen6s., Middle High German e/ne 
burcs/e/fen' they make to the surface of the earth immediately ', Intens. Old High German 
slipfen^ slide, hatch'. Middle High German slipfec, slipferic^ slippery '; 

besides with Germanic -it'it*-: Dutch slib, s//bbe's'\\t, slime, mud', s//bberen 'gWde, slide'. 
Middle Low German slibber, -ich^ slippery '. 

(sj/e/i'^-' slippery, glide, slide', see below the particular headword. 

Maybe alb. /edhe' fondling, caress ', /edhatoj" to caress '. 

s/eig-'sWrny, glide, slide, smooth': 

Gr. AiySnv "the grazing surface ', Kiyboq, Kiyba " clay mould, lye, used as soap, mortar'; 

Old Irish sligim, fo-sligim^ to reduce to a straight line, to make straight ', adslig^ lure, 
tempt, entice, draw ' (cymr. /////?" sugarplum ', llithio^ decoy, lure ' < *slig-t-), perhaps - as 
"stroke = hit' = Old Irish s//g/m'h\t', in addition s//ge'roa6' (?); Old Irish sliachtad^ the 
smoothness, flattening '; Old Irish s//ige"comb'; 

Old Icelandic sITkr^ smooth ', s//7r/s/e//7/7 "grindstone, whetstone'. Old High German 
s/Thhan'sWnk' (= "glide, slide'), s/e/hha'\oop, sled ', Middle Low German s//k, slick. Middle 
High German s//c/7"silt, slime, mud'; participle *slihta-^ smoothed ' in Gothic slafhts 



'simple, even ', Old Icelandic slettr^ smooth, even, straight'. Old High Germans/e/?/ 
"straight, even, evil, bad'. Modern High German scMchtan6 schlecht. Old English sliht. 
Middle English slight, sleghV smooth, even '; 

Old Bulgarian 5/6Zb/rfc "£i(; oAioGov', russ. slfzkij^ slippery', s//z6 "mucus', slfzyP\. "a 
kind of loop'. 

leip-^ besmear with fat ', see below particular headword {leip-). 

lei-t-^ glide over, touch softly, stroke ': probably Ann request', Aiaao|jai, Airoijai "bid, 
beg, ask, invoke', Kuavoc, "imploring', AiravEuu) "invoke'; Latin litare^io make an acceptable 
sacrifice, obtain favorable omens' (based on 7//5from Ann); Lithuanian /y/e// "touch', 
Latvian /a/tft' stroke, caress', Lithuanian //ec/'u, //es// "touch, betreffen'. 

Maybe alb. /ut, /us ' pray'. 

References: WP. II 389 ff., WH. I 789, 801, 802, 807 f., Trautmann 148, 162, 269, 270; 
different about 3. and 4. /e/- EM2 553 f. 
Page(s): 662-664 

Root / lemma: lehip-1 {* lehup) Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: to smear, stick 

Note: probably extension to /e/- "slimy'. 

Material: Old Indie lip- {limpati-, llpyat§) "besmear', llpt'a- " sticking, adhesive ', lepayatr 

smears ' (= Slavic leplti), /vp- "smear, stick, glue, cheat, deceive'; rip-\. "deceit; pollution '(= 

gr. Aina Akk.), lepa-vn. " the coating, the smearing, smut', repas-v\. " stain, smut', rlpra-v\.
```


## [2026-09-06T22:56:59.618Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"legʷh\\|leghu\\|leg[^ ]*h-\\|laghu\" IEC.txt | head -30; echo \"=== lay ===\"; grep -n \"layah\\|lay-\\|loi-\\|lei-\" IEC.txt | head -40",
 "description": "Grep Mann IEC"
}
```


### [2026-09-06T22:56:59.701Z] TOOL RESULT

```
959:blatio ‘twaddle’. Cf. blatero. For alleged *blagh-, *blegh-, *blog- see end. Lat. blatio, ire; R cf. boltát (fr. *blt-)
1208:bhelegh- (bhelugh-) (?) (a furry animal) Sk. bhaluhah ‘dog’; Lat. cf. (?) feles ‘weasel’ or *marten'; W bele *marten'; Gallo-Lat. LW in Fr. belette, id. (dim.); OHG cf. (Alem.) pilih, MHG bilch (*dormouse', said to be fr. Sl. plükhü, see FK: Bilchmaus). (Lat. feles is ambig. see dhel-)
2331:dighos (1) (dologhos and variants) "long, lasting, durable’. WP I, 813. Cf. de-/do- and legh- Skt. dirgháh; Av. daroyo; OPer. darga-; Oss. darg (beside därg, dárg-cà "length; Gk. dolikhós, en-delekhés; Hitt. dalugis; Lat. cf. in-dulgeo ‘indulge, concede’; Ir dluighe ‘separation’; Go. tulgus; OE tulge ‘firm’; OS tulgo ‘very’; OCS dlügü; Pol. długi; Srb. düg
9421:lāg- (2) ? (leg-? legh-?) Per. ray ‘meadow, slope’; ON lækt, pl. lækir, m. ‘brook’; Alb. (ambig.) log, m. ‘green, grass plot’ (but Mod. Gk. lóggos ‘thicket, wood? is said to be fr. Slav. *logü as in Cz. luh “low- land meadow’. A variant of type *lag- may arise in Srb. laz, m. ‘field’; Slovak laz *upland', Cz. iaz ‘meadow’)
9537:legh- lie". Cf. following entries and logh-
9541:leghó “lay; lie’. Cf. lëgh-, logh-. WP II, 424 Tokh. B läk, lyak-, v. ‘lie’; Hitt. cf. sa-lik(mi) lie together’; Hes. lékhomai “lie? beside Gk. ende-lekhéo ‘abide’; Alb. cf. fle ‘sleep’, if for *apo-legh-; Falisc. lecet, 3s. "Des": Mir ligim ‘lie’; Ir. leaghaim, leigim ‘lay’; W lleu, inf. “lay, set'; Go. ligan, OHG liggen, OE licgan, ON liggja, sv. 5 ‘lie’; OCS leZzo, at. and com. SI. id.; OCz. (also) tehu, léci, id. (For Ir. leigim “let, release"; Li. legti *abate', see lego)
9543:bed’. Cf. leghó, legh-, logh- Tokh. A lake, B leke “bed”; leki *lair, camp’; Gk. Iékhos, n. ‘bed’; Ir. lighe, f. ‘bed’; cf. MIr. cob-lige *lying-together'; W lle, pl. -oedd m. ‘place’; Cor. le, pl. -ow, m. and -yow ‘place’; MHG 1ége, f. ‘camp; situation, site’; ON leg, n. *burial-place'; mod. ‘womb’; lega, f. 'bed- ridden state, sickness’; Cz. cf. noc-leh, m. *night's lodging’; Li. cf. pa-legas, m. ‘peak of cap’
9545:leghs- (leks-), sigmatic extn. of legh-, see leghó, etc. Gk. (Rhodes) léskha ‘grave’; W llech (2) *skulking'; llechu, inf. ‘lurk, skulk, hide’. (For W Ilech ‘flagstone’: Ir. leac, see pleks-)
9547:(leghus, leghuis, see leguhos, and cf. elngu-
9557:leguhos, is (leghus) ‘lightweight’. WP II, 426 Skt. cf. Jaghüh, raghüh, adj. id.; Alb. leh, adj. id.; Lat. levis, id. (the Lat. form may derive from a feminine, cf. suávis in relation to type *suadus, q.v.). Verbal forms include Alb. të lehun-it “act of parturition'; Lat. levo, are be- side levigo, àre and al-levio, are. (For Skt. rá- hami “part, abandon'; Av. raz-, id. and the Per. pp. rast, see rogh-. For Ir. leigim “let, leave, emit, drop" see lég- (leg- ?))
13301:e-grade in view of Arm. herk ‘ploughed field’, see peduom); of ambig. vocalism is Skt. pade pade (“step by step”, *pedei/-oi or *podei/-oi; Gk. pédoi “on the ground"); Arm. otn, gs otin, ab. s. amb, also otk, pl. type ‘foot’; Hitt. cf. (o-gde) pat-, pata-, id.; Gk. poüs, gs podós, m., Myc. pod-, id.; cf. also ne-podes ('seals', lit. *no-feet?); Lat. cf. le-pos, -poris, m. (hare, perh. for *leguh-pods "lightfoot"); (long-gde in) Go. fotus, OHG fuos, OE fot, pl. fet, ON fótr, pl. fætr, m. d: OCS podü, m. “floor, storey”; Srb. ‘floor’; R ‘hearth, open-hearth"; Big. ‘stone floor, slab’ beside Cz. půda, f. “ground”; Li. pádas, m. ‘sole of foot’; pádis, gs: padio, m. ‘base’ (Li. pádas also “bottom, floor of hearth, threshing-floor' under infl. of Russian); Latv. pads, m. ‘clay floor
19547:-ukos, dim. extn. Cf. Skt. laghukah ‘trivial, light’; lambukah, m. “an astral yoga’; píthukah, m. ‘scalded rice; youngster’; Arm. man-uk, s. ‘child’; Gk. plat- ukós, adj. ‘broad’; OCS Iíg-ükü, adj. “light; list-ükü, m. ‘leaflet’; Li. dant-ükas little tooth"; Latv. te]-uks, m. “runt, undersized calf
=== lay ===
1402:bhloi-, see bhlós-
1409:bhlós- (bhloi-) “flower, bloom’. Cf. bhloros Lat. flos, gp. florum; Osc. cf. Fluusaí ‘to Flora’; W cf. blóen, blóyn ‘bloom’; OE blosa, id.; MHG cf. bluo, blüe, id. & Du. bloei, id. Variants: Br. bloen (‘blossom’, coll.): W bloden, pl. blodau; MHG bluost, G Bluest; Du. bloesem, beside OE blostm, blostma (*bhlot-, *bhlost-, *bhlos(t)m-); (Li. cf. bluostas “flash, blink, glimpse, nap” for iso- phonic equivalent)
2851:dhéstos, is “set, placed, fixed; setting, fixture'. See dhë- (2), etc. W des ‘system, order; Latv. dests ‘plant, seedling'; Li. cf. dëstymas “lay-out, exposi- tion’, déstyti “to set out, etc.
3787:-amos, superlative extn. in Skt. gurut-amáh, apamah ‘heaviest; hindmost’; Av. frat-omo, up-amo ‘foremost’; ap-omo ‘last’; Hitt. sept- amas ‘seventh’; Alb. i prap-ém, i pas-ém ‘hindmost’; Lat. inf-imus, post-umus ‘lowest; latest"; Osc. ness-imas, f. pl. ‘next’; Olr. ness- am ‘next’; tress-am ‘strongest’; W nes-af, elei-af ‘next; least’; Go. aft-uma “latter, last’; OE hindema ‘hindmost; MHG  zésem ("straight line”, fr. *deKsemo-); Gk. hebd-om os; OCS sedmyi; OLi. sekmas “seventh? beside art-imas “near”; OPr. sept-mas “seventh? beside ilg-imai, adv. “at length'. Cf. also Faliscan max-omo ‘Maximus’; Per. Cahar-um “4th2; Kurd. cuvar-em, id.; Per. haft-um, Kurd. hewtem *7th., etc.
4122:(gloin-, gloip-, gloist-, formulae implied for OCS glénü ‘mucus’; Slk. hlien ‘mud’; Alb. glepë ‘rheum’; and Li. glaistas ‘mortar, putty’ respectively. Cf. gloi- and derivatives)
4124:glue’. Cf. gloi- & derivs. & WP I, 620. Cf. also glot-, à, io, gleu-, glü-, etc. Lat. (ambig.) glütus ‘compact’; glüten ‘glue, solder’; Olr. (ambig.) gláed ('glue'. See gloiios) beside glaedaim ‘adhere’; gláeta (pp. :glued"); W glud ‘sticky; glue’; Br. glüd ‘glue’; OCor. glut, Cor. gloes, id.; gloeja (for gloedZa, v. *stick&); MHG kleit, gs -des “garment; animal- skin; cloth” and com. Gmc.; Li. cf. glaistas ‘smear, grease, glaze, mortar, putty’
4125:gloiobha ‘clod, sod”. Cf. gloi- and derivs. Lat. glaeba, glëba; R glyba; Pol. gleba (e for y as in ser: R syr, m. (cheese). (For the pho- nology cf. IE *quoie implied in Gk. poía, Ionic koíé: Lat. quae; OCS kaja beside m. kv)
4133:glomos, glom- ‘compact; mass’. WP I, 617. Cf. gloi-, glomb-, (glombh-) Lat. glomus (o-st. & -es-st.); Du. klam “clam- my, moist; MHG klam, adj. (1) ‘compact’; LG klamm ‘cramped’; Li. glam-oneju ‘fondle’, glam-žau, -žyti ‘squeeze’
8866:id. (and *north"); Go. cf. hlei-duma ‘left-hand’;
8933:Kloinos, om, à, is, io ‘sloping, leaning; slope, lean, incline'. WP 490. Cf. Klei-, Klit-, etc. Skt. (?) $rénih, f. "line, group, front’; OIr. MIr. Ir. cloín, clóen, claon 'sloping, bent, wrong, perverse, devious’; MIr. clóene, f. ‘slope’; Ir. claon, m. “trend, deviousness'; MW clun ‘hill;
8936:Kloit- ‘slope, lean, prop, support. Cf. Klei-, Klit-, etc. Br. klüd, m. “perch, roost'; klüsa, v. ‘squat’; OHG cf. hleitara, leitar, f. ladder’; OE hlæder, f. id.; Norw. leider, id.; Li. Slaitas ‘sloping’; m. 'slope; wastrel, wanton'; Latv. cf. sliet-enis ‘clamp, summer-house of stakes’
8937:Kloiuos ‘hill, slope’. Cf. Klei- (Kleii), Kli-, Klit-, Kloi-, etc. WP I, 490 Lat. (ambig.) clivus, 1j, m. “hill, slope’; Olr. (ambig.) clói ‘ridge’; Go. hlaiw, n. ‘hil’; MHG le, gs léwes, id.; OE hlaw, hl&w, m. n. d: Finn. LW loiva ‘hillside’
9548:leghó — lei- (lin-)
9561:lei- (lin-) “let, leave’ (as a sentence-particle). Cf. leið (4) Skt. cf. riye, mp. & rinámi, rinimi "let; release; sever; bestow’; Arm. cf. linim, inf. linel, aor.
9584:leiio, leió “pour, cast’. Cf. leið (1) and hio LLat. lio, are tr. («liquefy'. Classical liare *smooth, paste? is of ambig. origin); Ir. cf. lia, dp liaibh, m. ‘downpour’; W lli, pl. -on, s. ‘flood’; OCS lějọ, inf. lijati (pour, cast’, and com. Sl); Li. liejü, ben ‘pour, shed”; Latv. leju, liet, id.; cf. lējums, m. *outpour, down- pour” beside list, 3s., inf. Iit, v. ‘rain’. Uncer- tainly to Arm. tey, o-st. Cdownpour, if for *de-lei- ? Cf. teyaj, v. 3s “it rains")
9608:leiquo “leave, let, allow, remain”. Cf. liquos, loiquos, liqutos. WP II, 396 Skt. recàmi 'evacuate, leave’; Av. (radical) rič-, id.; Myc. leiq-, Gk. leípo, aor. élipon, id.; Arm. lkem, id.; Tokh. A cf. lek, adj. "dis, tant, apart”; Lat. cf. liqui, pf. ‘I left; MIr. lei- cim, Olr. lécim, id.; Go. leihvan ‘lend’; OE leon, MHG liben, liuhen, sv. 1. id.; ON ljá, le, wv ‘lend, grant’; OLi. liekmi, 3s li&kti, inf. likti, pf. likaü, pp liktas "leave; remain'; Li. Deko 1sg. id.; Latv. cf. lieks ‘superfluous’; Ir. cf. léic, f. ‘neglect. See next
9619:Ian (li-) (2) ‘smooth, wipe’. Cf. liio (2) and loi- Av. ri-, pres. p. rayaüit ‘besmear’; Tokh. AB lya- ‘wipe’; OLat. leo, lére, pf. levi ‘besmear, anoint’ beside e-leo, -lere ‘stain’; de-leo, -lere ‘wipe out’; cf. variant lio, litare “smooth over, paste, putty’ beside lino, pf. lini, livi & levi, sup. litum ‘smear and (prob.) polio, -lire (smooth, polish’. Px. po- as in ponere). O-gde in OCS loj, Li. lájus ‘grease’ and perh. long o-gde in Alb. Iyei, v. (smear, if from a type *loio)
9892:list- (?) “edge, border" Cf. lit- (1) and loi- sthos. WP IT, 405 Ir. líosta, m. ‘ledge’; Br. cf. lisen, pl. -nnu, f. 'cross-beam on floor of cart; OHG lista, MHG liste, wf., ON lista, f. ‘border’; G Leiste, id.; Du. lijst, f. (frame, border, taffrail', hence Fr. lisse, E *list in the phr. to list “heel over”). Gmc. LW in Latv. liste, f. “margin, compart- ment
9905:ba, ið ‘touch, affect, hurt’. Cf. leit- (1), loi- tos Gk. cf. a-liteo, a-leíto, a-litaíno ‘offend; sin, err’; Ir. cf. líathaim (‘be dismayed’, fr. *leit-); W (ambig.) llid, m. ‘anger’; llidio, denom. vb. ‘enrage; be angry”, cf. er-lidio, v. (*persecute', fr. *per-Iit-); OHG Iidan sv. 1. ((2) ‘suffer’. For Ddan (1) ‘go’ see lit- and leit- (2)); (o-gde in MHG be-leidigen Cham, hurt: G ‘insult’; Li. lyCià, lytéti touch, concern? beside liečiù, Ji&sti, id. (fr. *leit-). WP cf. IL, 394 & 415
9968:loigo, io (1) “jump, dance, play’. WP II, 399 Skt. réje, mp. (jump; sway”, w. secondary j = č); Go. laikan “jump, dance, play’; MHG lei- chen, id. (and “mount; hoax'); OE lacan, sv. 7, pf. leolc: Go. (unrecorded) *lailaik “bob, leap, fly, play, fight; ON leika “play, dance, hoax’; Sw. leka ‘play; mate”; Li. láigyti, inf. ‘frolic, rampage’. LW in Finn. loikkia “leap? beside leikkiä ‘play’. Noun forms: Go. laiks, OHG leihh; MHG leich, sm. ‘tune’; ge-leich, n. (3) ‘hoax’; OE làc, f.; OFris. lek; Sw. lek; ON leikr, m. ‘game’; leik, pl. -u, n. ‘toy’; Finn. LW leikki
9992:Skt. reknas, n. degacy'; OHG lëhan, MHG lehen, sn. “loan”; OE lan, læn id.; Li. cf. lieka- nos, fpl. ‘residue’. Finn. LW laina ‘loan’; loi- nen ‘tenant’
10000:loisthos (prob. for loidhst-, but cf. loisa) ‘track; following, behind’. WP II, 388 et seq. Gk. loisthos, -ios, adj. “left behind, last’; Go. laists, m. ‘track’ beside laistjan, v. ‘follow’; OHG leist, m. ‘footstep; cobbler's last’; lei- sten, v. “follow, perform’; OE læste, s. *cob- bler's last; læstan, v “follow, serve; do; en- dure; provide’; ON leistr. m. “foot; sock (The semantics are those of W ôl ‘track’; ad]. ‘rear’; olaf “last”, and of OCS slédü “track? and po-
10014:loitos, us (lit-) (3) ‘touch, stroke, smear. Cf. leio (2), loi-, loi- Lat. cf. (z-gde) litus, adj. “marked, smeared; adorned'; litus, gs -üs, f. “marking, smearing, adornment’; Li. lieciu, liesti, v. touch, con- cern’ beside lieta, f. “matter, concern’; Latv. laitit, v. freq. ‘massage’
10018:loi- (loios, á) (2) “layer, slice’. WP II, 406 OS leia ‘rock, schist; MHG lei, leie, f. id. (and ‘slate’); Du. lei, f. ‘slate’; R cf. s-loj “layer, stratum, seam; lamina’; Cz. sloj, id.; Pol. słój ‘grain in wood’
10024:loi- (loios, á) — londh-
11865:(2). (Celtic initial uncertain) W nawd, f. ‘nature’; adv. ‘easily’; Fris. noed (care; responsibility; risk. Phonol. ambig. *notós?); Icel. cf. naeói, if for *noeói, n. “lei- sure, rest’. (Equations uncertain)
12973:pláio (ploi-) ‘spread, flatten’. Cf. WP II, 61 and plēið Alb. cf. plojë, f. ‘carnage’; W cf. (variant) llàu, inf. (spread', if fr. a type *ploi-); ON cf. flói, m. *mudflat'; Li. ploju, ploti, v. ‘flatten, roll out, spread, thin out": Latv. plaju, plat, id.; cf. Fris. floei ‘fluke’
13042:plédh- (pledho; pledhu-) ‘fulness, flood, swarm, glut, crowd; fill, swarm', etc. (O-gde variant: plódh-). Radical plé-, see pleio, plei- etc. Gk. pléthos, gs: -eos, n., & plethüs, f. ‘crowd, rabble’; plétho, v. ‘fil’; Lat. plebs, f. & plebes, gs: -is & -ei, f. ‘rabble; swarm of bees’; Gaul. ledo, pl. ledones 'flood-tide, swell; Gallo-Lat. Jeduna, liduna, id. O-gde (*plodh-) in Sequan- ian lod (queried: ‘downpour’, in phr: samon prin — ‘summer, first storm’); Go. flódus, MHG vluot, OE flod, ON flóð ‘flood’; ON also flæða, v. id. Isophonic: MHG vlat, adj. ‘clean, neat, tidy’ and MDu. vlaeien, v. ‘clean, purify’. WP II, 63
13050:plei, plei- (radical of the following entries)
13061:pleio “overflow, abound, fil’. WP II, 63 Vedic prā- in aor. 3s. á-pràs-, id.; Av. fra- (2), id. (Justi); Arm. cf. li, adj. ‘full beside lecun, id., hence lecnem, v. ‘fill’; Gk. pléso, 1sg. fut. ‘shall fil (pres. t. pímplemi fil’); Gk-Alb. ploj, v. “fil” beside Alb. mbloj, v. id. (fr. *en- plei-); Tosk (also) mploj, v. ‘complete’; Lat. im-pleo, -ere, v. “fill up’; Ir. cf. lia, s. ‘flood’; lli, m. id. beside Iliad, lliant, m. ‘flooding, torrent", fr. *plejot- *pleiont-); Icel. flá, v. Let ‘gape’; Li. pléstu, plésti, pf: plésau, v. “be ramp- ant” beside pleciü, plesti, pf. plēčiaŭ, v. “spread?
13062:pleios, a “full, overflowing, spreading, ramp- ant; fulness, flood’. Cf. pleio. WP II, 63 Skt. praya-, cpds. *mostly-'; playah, práyah, m. “abundance; Av. frayao (comparative: 'seve- ral"); Arm. ambig. li, adj. ( full, prob. fr. *ple- tos, q.v.) beside þ-yi, gs: -vo, ab. s. -eav (“preg- nant’, fr. *en-pleto-); cf. also lir, i-st. gs: lri, s. ‘fulness’; Attic Gk. pléos, Homeric pleios “full”; pleion, pleístos ‘more; most’; Alb. (poe- tic) plo, adj. “full”; OIr. lía, Ir. lia, cmp. more: W lli, pl. op, m. “flood, stream’; Cor. cf. lyes, Br. lies, adj. “many”; ON flá, pl: flár, f. net float; mod. (also) (strip of meadow’ beside flár, adj. ‘agape’. (Arm. lir, gs: Iri, i-st. ‘fulness’ seems to represent a type *plesis)
13094:pler- (2), variant of plei-, q. v. Lat. plerus, adj. “full; most’; MIr. ler, m. “flood, ocean’; W ller, m. (2) ‘satiety’
13124:pléuoros (plouer-), variant of type plei-, q. v. (Gk. ambig.). See next Gk. (ambig.) pléres, adj. (‘teeming’, fr. *pléuor- or *pléjor-); Lat. plüres, pl. ‘many’: Olr. Ir. lór, leor, adj. ‘plentiful’; s. ‘plenty’; W llawer, prn. ‘many’; pl. -oedd, s. ‘quantity’; Cor. lower ‘many’. Uncertainly: Arm. luy, loy, s. ('wimming', assimilated fr. *pleuor- via
13875:quàlos, à, io ‘mud, filth’. Cf. WP I, 441 & IT, 53, and cf. kálos, is (1) Hitt. cf. kuwaliu (something associated w. *darkness"); Myc. qaro- (for *qwalo-) in qaro- dero *clay-beater'; Gk. pelós, (Doric -à-) ‘mud, clay’; OCS kalü, m. ‘mud’; R kal, m. ‘dung’; Slovene kala ‘morass’, kalja, f. ‘dirt’. Skt. kalah ‘black’ ambig.
16194:slaK- ‘limp, lazy” Oss. läs, adj. ‘loitering, aimless’; lásín, v. *loi- ter, creep, flop"; cf. läst, s. landslide”; W Ilag, adj. ‘slack’; llegu, inf. “flag, lag’
16284:‘smoothly’; lígdos, m. ‘crucible’; mí-ligdos *clay-moulder, spatula, trowel’; Olr. cf. slecht, adj. ‘smooth’; W llaidd, id. (& ‘soft, mild"); Cor. lyth, id. (and ‘tender, moist); Go. slaíhts, OHG, MHG slëht, MHG sicht OS sliht; ME sleght & slight; ON sléttr, adj. (“level, even, slim, smooth, simple, straight", etc.); cf. also G schlicker, m. ‘wet clay’; -ig, adj. *oozy, sloppy’; -n, v. “slip, slither; W Ilys (slime < *sligst-)
16316:sloib- ‘smooth’. Cf. slub- Lat. cf. (ambig.) lübricus, adj. ‘gliding, slip- pery; fickle; tricky’; MHG sleif, adj. id.; slei- fen, sleipfen, v. ‘make slip, drag, level’; sleife and sleipfe, f. ‘runner of sledge’; ON sleipr, adj. ‘slippery’. (Isophonic: Gk. loibé, f. “liba- tion’; Lat. fibum, n. ‘cake of honey, oil and barley used as an offering)
17212:stern- ‘spread, extended; spread, lay-out'. Cf. ster (stern-) Lat. cf. lecti-sternium, n. ‘bedspread’; Br. stern, pl. -iu, m. ‘frame, bedstead; team’; W cf. sarn, pl. -au, f. ‘paving’; sarnu, inf. (“pave”, fr. *stərn-)
17238:stib- (sthib-) “hard, stiff, firm’ Gk. stíbë, f. “hoarfrost'; Fris. stīpe, f. ‘prop’; stypje, f. id.; Li. cf. (ambig.) stybstù, stýbti, v. (rise, tower’ fr. *sthib- or *sthibh-); MHG (ambig.) cf. stift, stëft, sm. ‘thorn; stub; point’; G Blei-stift. See next
17688:stholos (st-) ‘set, lay-out, condition’. Cf. stel- (stol-) and sthálos Skt. sthálam, n. 'elevated ground, region”; Arm. tay, i, iv & i, av, s. ‘district’; t'ayem, v. ‘bury’. Ambig. cf. sthál-); Gk. stólos, m., stolé, f. equipment, equipage’; f. also: ‘robe’; stolís, f. ‘fold, wrinkle; robe, garment’; Lat. cf. stoló, gs: -onis, m. ‘sucker, shoot; blockhead’ beside stolidus, adj. *dull, stupid”; cf. also Gk. stolás, -ádos, adj. "en masse’; (long-gde in) Lat. prae-stolor, åri, v. ‘wait’; (Gmc. types stal- ambig. Cf. sthál-)
```


## [2026-09-06T22:57:00.605Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"leg.h\\|lengh\\|lehg\" AHD_watkins1985.txt | head -20; echo \"=== slime ===\"; grep -n -i \"^slei\\|slime\\|slei-\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-06T22:57:00.674Z] TOOL RESULT

```
123:A number of qualitative adjectives are at- tested that go back to the protolanguage. Some come in semantic pairs: sen-', “old,” and newo-, “new”; also sen-', “old,” and yeu-, “youthful vigor”; *tenu-, “thin” (under ten-), and tegu-, “thick”; g”era-?, “heavy,” and leg"h-, “light.” There are also the two prefixes su-, “good, well-,” and dus-, “bad, ill-,” in the Greek forms borrowed as EU- and pDys-. But normally adjectives of value judg- ments like good and bad are not widespread in the family and are subject to replacement; English good, Latin bonus, and Greek aga- thos have nothing to do with each other, and each is confined to its own branch of the family.
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
668:legwh-. Light, having little weight. 1. Suffixed form *legeh-t- in Germanic */iht()az in: a. Old English Jiht, léoht, light: LicHT?; b. Old English /ihtan, to lighten: LIGHTER?. 2. Suffixed form *legvh-u-i- in Latin levis (> Old French Jeger), light, with its derivative levdre, to lighten, raise: LEAVEN, LEVER, LEVITY; ALLEVIATE, CARNIVAL, ELEVATE, LEGERDEMAIN, LEVIGATE, (MEZZO-RELIEVO), RELIEVE. 3. Variant form *lagvh- in Old Irish /i-, small: LEPRECHAUN. 4. Nasalized form *l(e)ngeh- in Germanic *lung- in Old English lungen, lungs (from their lightness): LUNG. 5. Attributed by some to this root is Latin oblivisci, to forget, which is more likely from lei-. [Pok. legzh- 660.]
1448:ELDER? el-2 ELDEST al-3 ELECAMPANE wel-3 ELECT leg-1 ELECTUARY leigh- ELEVATE leg*h- ELEVEN oi-no- ELF albho-
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1741:LETHAL ol- LETHARGY |adh- LETHE ladh- LETTER deph- LETTUCE melg- LEVEL [ithra LEVER leg’h- LEVIGATE ag-, leg’h- LEVIRATE daiwer- LEVITY leg¥h- LEVo- laiwo- LEVOROTATION laiwo- LEVOROTATORY laiwo- LEX leg-1 LEXICON leg-1 LIABLE leig-1 LIBATION Iéi- LIBERAL leudh-2 LIBERATE leudh-2 LIBERTINE leudh-2 LIBERTY leudh-2 LIBIDO leubh- LIBRA fithra
1748:LIFT leup- LIGASE leig-1 LIGATE leig-1 LIGHT! = leuk- LIGHT2 legwh-
1750:LIGHTER? legwh- LIGNEOUS  leg-! LIGNI- leg-1 LIGNUM VITAE gWei- LIGULE dngha LIKE! [ik- LIKE? [ik- LIKELY lik- LILAC nei- LIMACINE  lei- LIME = lei- LIMICOLINE lei- LIMN leuk- LIMP kel-1, leb-1 LINDEN _ lento- LINE! lino- LINE? fino- LINEN fino- Linc! del-1 LING? lenk- LINGER del-1 LINGERIE lino- LINGO dnghi LINGUA dnghd LINGUIST dngha LINIMENT lei- LININ lino- LINK! kleng- LINK? Jeuk- LINKS kleng- LINNET fino- _ LINOLEIC ACID [ino- LINSEED lino- LINT Tino-
1772:LUNE leuk- LUNG leg¥h- LUNGE del-1
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
2269:SLAUGHTER  slak- SLAVER! |leb-1 SLAY slak- SLED sleidh- SLEDGE sleidh- SLEDGEHAMMER slak- SLEEP sléb- SLEET sleu- SLEEVE sleubh- SLEIGH sleidh- SLEIGHT slak- SLEW! sloug- SLICK lei- SLIDE sleidh- SLIGHT lei- SLIM leb-1 SLIME lei- SLING! slengWh- SLINGSHOT slengh- SLINK sleng’h- SLIP! lei-
=== slime ===
661:ladh-. To be hidden. 1. Greek léthé, forgetfulness: LETH- ARGY, LETHE. 2. Zero-grade form *ladh- (< *bdh-), with nasalized form *landh-, in Greek lanthanein (aorist lathein), to escape the notice of, with middle anthanes- thai, to forget: LANTHANUM; ALASTOR. 3. Suffixed (sta- tive) variant form */at-é- in Latin latére, to lie hidden: LATENT. [In Pok. 2. /a- 651.] laiwo-. Left. Latin Jaevus, left: LEVO-; (LEVOROTATION), (LEVOROTATORY). [Pok. laiuo- 652.] laks-. Salmon. Suffixed form */aks-o- in Germanic */ahs- az in Old High German Jahs, salmon: Lox}. [Pok. lak- 653.] laku-. Body of water, lake, sea. 1. Latin /acus, lake, pond, basin: LAKE!. 2. Greek lakkos, cistern: LACCOLITH. 3. O-grade form *loku- in Old Irish and Scottish Gaelic loch, lake: LocH, LouGH. [Pok. laku- 653.] lap-. To light, burn. Nasalized shortened form */a-m-p- in Greek lampein, to shine: LAMP, LANTERN; ECLAMPSIA. [Pok. la(i)p- 652.] las-. To be eager, wanton, or unruly. 1. Suffixed Ger- manic zero-grade form *lustuz in: a. Old English Just, lust: Lust; b. Old High German Just (> German Lust), desire: WANDERLUST; Cc. Germanic denominative verb *lustjan in Old English lystan, to please, satisfy a desire: LisT’, 2. Suffixed form */as-ko- in Latin lJascivus, wan- ton, lustful: Lascivious. [Pok. las- 654.] lat-. Wet, moist. Latin latex, liquid: LaTEx. [Pok. Jat- 654.] lau-. Gain, profit. 1. Suffixed form */au-no- in Germanic *Jaunam in Old High German J6n, reward: GUERDON. 2. Suffixed zero-grade form */u-tlo- in Latin lucrum, gain, profit: LUCRATIVE, LUCRE. 3. Suffixed variant form *low-ero- in Irish Gaelic ledr, sufficiency, enough: GA- LORE. [Pok. ldu- 655.] lé-1. To get. Contracted from “lea-. Suffixed zero-grade form *b-tr- in: a. Greek Jatreia, service (for pay), duties, worship: -LATRY; b. Greek Jatron, pay, akin to the Greek source of Latin latré, robber: LARCENY; c. Greek -/latrés, worshiper: IDOLATER. [Pok. 2. /é(i)- 665.] lé-2, To let go, slacken. Contracted from *les-. 1. Ex- tended form */éd- in: a. Germanic */étan in Old English létan, to allow, leave undone: LET!; b. Germanic deriva- tive *léthigaz, freed, in Medieval Latin /étus, litus, serf (< “free man”): LIEGE. 2. Extended zero-grade form */d- in: a. Germanic */ataz in Old English Zt, late, with its comparative lztra, latter, and its superlative Jatost, last: LATE, LATTER, LAST!; b. Germanic */atjan in Old English lettan, to hinder, impede (< “to make late”): LET?; c. suffixed form */od-to- in Latin lassus, tired, weary: LASSITUDE; ALAS. 3. Suffixed reduced form */é-ni- in Latin lénis, soft, gentle: LENIENT, LENIS, LENITIVE, LENITY. [Pok. 3. lé(i)- 666.] leb-'. Base of loosely related derivatives meaning “hang- ing loosely.” I. Variant form *lep- in Germanic */ap- in Old English lzppa, lappa, flap of a garment: Lap’. II. Nasalized form *lemb(h)-, with variant form *slemb(h)-. 1. Germanic *lemp- probably in obsolete English limphalt, lame (halt, lame; see kel-'): LIMP. 2. Germanic */ump- in: a. Dutch lomp, rag, akin to the Low German source of Middle English Jump, lump: LUMP!; b. possibly obsolete English Jump, lumpfish: LUMPFISH; Cc. German Lumpen, rags: LUMPEN. 3. Ger- manic *slimp- in Middle Dutch slim(p), slanting, bad: SLIM. 4, Middle High German slam, mud: SLUMGULLION. 5. Old Norse slambra, to strike at, akin to the Scandina- vian source of SLAM!. 6. Norwegian slumpa, to slump, akin to the Scandinavian source of sLuMpP. III. Variant *(s)lab- in Germanic *s/ab-. 1. Danish slab, mud, akin to the Scandinavian source of SLAB2. 2. Swedish slabb, slime, mud, akin to the Scandinavian source of Irish slab, mud: sLos. IV. Variants *slap-, *slep-. Germanic *slap- in: a. Low German s/app, slap: SLAP; b. Old Norse slafra, to slaver: SLAVER}. V. Variant */ab-. 1. Germanic *lab- in Old French label, ribbon, strip: LABEL. 2. Latin
669:lei-. Also slei-. Slimy. 1. Germanic *sli- with various
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
736:Latin micturire, to want to urinate (desiderative of meiere, to urinate): MICTURATE. [Pok. meigh- 713.] meik-. To mix. 1. Variant form *meig- in Greek mig- nunai, to mix: AMPHIMIXIS, APOMIXIS, PANMICTIC, PAN- MIXIS. 2. Suffixed zero-grade form *mik-sk- in Latin miscére (past participle mixtus), to mix: MEDDLE, (MED- LEY), (MELANGE), MESTIZO, MISCELLANEOUS, MISCIBLE, MIX, MIXTURE; ADMIX, COMMIX, IMMIX, MISCEGENATION, (PELL-MELL), PROMISCUOUS. 3. Possibly a Germanic form *maisk- in Old English mdsc, macs, mdx, mashed malt: MASH. [Pok. meik- 714.] mei-no-. Opinion, intention. 1. Germanic *main- in Old English *mdn, opinion, complaint (> Middle English mone, complaint): MOAN; (BEMOAN). 2. Germanic *main- Jan in Old English ménan, to signify, tell, complain of, moan: MEAN}, [Pok. mei-no- 714.] mel-1, Soft; with derivatives referring to soft or softened materials of various kinds. I. Extended form *meld-. 1. Germanic *meltan in Old English meltan, to melt: MELT. 2. Possibly Germanic *miltja- in Old English milte, spleen, and Middle Dutch milte, milt: mit. 3. Possibly Germanic *malta- in Old English mealt, malt: MALT. 4. Suffixed variant form *mled-sno- in Greek blennos, slime, also a name for the blenny: BLENNY. 5. Suffixed zero-grade form *mid-wi- in Latin mollis, soft: MOIL, MOLLIFY, MOLLUSK, MOUILLE; EMOLLIENT; 6. Possibly nasalized variant form *mlad- in Latin blandus, smooth, caressing, flattering, soft-spoken: BLAND, BLANDISH. II. Variant form *smeld-. Germanic *smelt- in: a. Middle Dutch and Middle Low German smelten, to smelt: SMELT!; b. Old High German smalz, animal fat: SCHMALTZ; C. Italian smalto, melted glass: SMALT; d. Old French esmail, enamel: ENAMEL; e. perhaps Old English smelt, smylt, a marine fish, smelt: SMELT?. III. Extended form *meldh-. 1. Germanic *mildja- in Old English milde, mild MILD. 2. Possibly Greek maltha, a mixture of wax and pitch: MALTHA. IV. Suffixed form *mel-sko- in Ger- manic *mil-sk- in Old English melfi)sc, mylsc, mild, mellow (> Middle English melsche, friable): MULCH. V. Extended form *mfk- in Greek malakos, soft: CHON- DROMALACIA, MALACOLOGY, OSTEOMALACIA. VI. Possi- bly Celtic *molto-, sheep, in Old French moton, sheep: MUTTON. VII. Suffixed zero-grade form *()ml-u- in Greek amblus, blunt, dull, dim: AMBLYGONITE, AMBLY- opiA. [Pok. 1. mel- 716.] mel-2, Of a darkish color. 1. Greek melas, black: MEL- ANO-; MELANCHOLY, PSILOMELANE. 2. Greek mullos, a marine fish: MULLET; (SURMULLET). 3. Latin mulleus, reddish purple (used only to designate a ceremonial shoe worn by Roman magistrates): MULE. 4. Perhaps Ger- manic *mal- in Middle Dutch malen, to paint: MAUL- STICK. [Pok. 6. mel- 720.] mel-3. A limb. Greek melos, limb, hence a musical member or phrase, hence music, song, melody: MELISMA; ACRO- MELIC, MELODRAMA, MELODY. [Pok. 5. mel- 720.] mel-4. Strong, great. 1. Suffixed (comparative) form *mel-yos- in Latin melior, better: (AMELIORATE), MELIO- RATE, MELIORISM. 2. Suffixed zero-grade form *m/J-to- in Latin multus (neuter multum), much, many: MOLTO, MULTI-, MULTITUDE. [Pok. 4. mel- 720.] mel-5. Bad. Latin malus, bad, and male, ill (> malignus, harmful): MAL-, MALICE, MALIGN; DISMAL, MALADY, MALEDICT, MALEFACTOR, MALEVOLENT, MALVERSATION. [Pok. mélo- 724.] mel-€, Wool. Possibly suffixed zero-grade form *ml-no- in Greek mallos, wool. [Pok. 2. mel- 719.] mel-?. To miss, deceive. Germanic *mai- in Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.] meldh-. To pray, speak words to a deity. Germanic *meld- in Old High German meldén, to proclaim, reveal: MELD}. [Pok. 1. meldh- 722.] mele-. Also mel-. To crush, grind; with derivatives referring to various ground or crumbling substances (such as flour) and to instruments for grinding or crush-
955:5. Suffixed form *lag-no- in Greek lagnos, lustful, lasciv- ious (> lagneia, lust, lasciviousness): ALGOLAGNIA. 6. Variant form */ég- in Greek légein, to leave off: CATALECTIC. [Pok. (s)lég- 959.] sleidh-. To slip, slide. 1. Germanic *s/idan, to slip, slide, in Old English s/idan, to slide: SLIDE. 2. Germanic *slid- in: a. Middle Low German sledde, a sled, sledge: SLED; b. Middle Dutch s/éde, a sled: SLEIGH; C. Middle Dutch sleedse, sleigh: SLEDGE. sleng”h-. To slide, make slide, sling, throw. 1. Germanic strong verb *slingwan and derived suffixed noun form *slingw-6- in Old Frisian slinge, sling, akin to the possi- ble source of Middle English sling, sling: SLING}; (SLING- SHOT). 2. Germanic variant strong verb *slinkan in Old English slincan, to creep: SLINK. 3. Suffixed o-grade form *slongh-ri-ko- in Latin lumbricus, intestinal worm, earthworm: LUMBRICOID. [In Pok. (sjleidh- 960, slenk- 961.] sleu-. Hypothetical base of a group of distantly related Germanic derivatives with various suffixes. 1. Germanic *slii-m- in Old English slima, sleep: SLUMBER. 2. Prob- ably Germanic *slautjan- in Old English “s/léte, sleet: SLEET. 3. Germanic *slus- in Norwegian slusk, sloppy weather, probably akin to the possible Scandinavian source of SLUSH. 4. Germanic *sleura- in Middle High German slier, mud, slime: SCHLIEREN. 5. Extended form *sleug- in Germanic ‘*sluk-, *slug- in: a. Norwegian dialectal slugg and Swedish dialectal slagga, slow-mov- ing animal or person, probably akin to the source of Middle English slugge, a sluggard, and sluggen, to be idle: SLUG?, SLUGGARD; b. Dutch /og, lazy, slack: LOGY. [Pok. (s)leu- 962.] sleubh-. To slide, slip. I. Basic form *sleubh-. 1. Ger- manic *slewb- in Old English s/éf, siif, slief, sleeve (into which the arm slips): SLEEVE. 2. Suffixed form *sleubh- ro- in Latin Jibricus, slippery: LUBRICATE, LUBRICITY, LUBRICIOUS. II. Variant Germanic form *sleup-. 1. Ger- manic *slup- in: a. Old English slypa, slyppe, slipa, slime, slimy substance: SLIP’; COWSLIP, OXLIP; b. Old English *sloppe, liquid food (perhaps > Middle English sloppe, a muddy place): sLoP!; c. Old English (ofer)slop, surplice (perhaps > Middle English sloppe, a kind of garment): SLOP?. 2. Germanic *s/aup- in Dutch sloep, sloop (< “gliding boat”): sLoop. [Pok. sleub(h)- 963.] sli-. Bluish. Contracted from *s/is-. 1. O-grade form *sloi- in Germanic *slaihw6n in Old English s/ah, sla, sloe (< “bluish fruit”): SLOE. 2. Suffixed form *sli-wo- in Latin livére, to be bluish: Livip. 3. Suffixed form *s/i-wd- in Serbo-Croatian sijiva, plum: sLivovitz. [Pok. (s)li- 965.] sloug-. Help, service. Celtic and Balto-Slavic. Suffixed form *sloug-o- in Old Irish slag, slog, army, host, whence Gaelic sluagh, army, host: SLEW!, SLOGAN. [Pok. slougo- 965.] smé-. To smear. Contracted from *smeo-. 1. Extended root *smeid- (< *smea-id-) in Germanic *smitan in Old English smitan, to daub, smear, pollute: SMITE. (2. At- tributed by some to this root, but more likely to be of unknown origin, is the Germanic root *mas-, spot, speck, in: a. Middle Dutch masel, pustule, spot, akin to the source of Middle English masel, measles-spot: MEASLES; b. Old French masere, mazre, knot in wood: MAZER.) 3. Attributed by some to this root, but perhaps distinct, is root *smik-, small, in: a. Latin mica, crumb, small piece, grain: MICA; b. Greek (s)mikros, small: MICRO-, MICRON; CHYLOMICRON, OMICRON. [Pok. smé- 966.] smeg-. To taste. Germanic *smak- in: a. Old English smzxc, flavor, taste: SMACK?; b. Middle Dutch and Mid- dle Low German smacken, to taste, make a sound with the lips while tasting food, akin to the source of SMACK!. [Pok. smeg(h)- 967.] smei-. To laugh, smile. 1. Germanic reshaped forms *smer-, *smar- in Old English smercian (with -k- forma- tive), to smile: SMIRK. 2. Germanic extended form *smil- in Swedish smila, to smile, probably akin to the Scandi-
1137:derivatives violdre, to treat with force, and violentus, vehement: VIM, VIOLATE, VIOLENT. [In Pok. 3. wei- 1123.] weik-', Clan (social unit above the household). 1. Suf- fixed form *weik-slé in Latin villa, country house, farm: VILLA, VILLAGE, VILLAIN, VILLANELLE, (VILLEIN); (BI- DONVILLE). 2. Suffixed o-grade form *woik-o- in: a. La- tin vicus, quarter or district of a town, neighborhood: (VICINAGE), VICINITY; b. Greek oikos, house, and its derivative oikia, dwelling: ANDROECIUM, AUTOECIOUS, DIOCESE, DIOECIOUS, DIOICOUS, ECESIS, ECOLOGY, ECON- OMY, ECUMENICAL, HETEROECIOUS, MONOECIOUS, PAR- IsH, TRIOECIOUS. 3. Zero-grade form *wik- in Sanskrit vis-, dwelling, house, with derivative vaisyah, settler: Vaisya. [Pok. weik- 1131.] weik-2. In words connected with magic and religious notions (in Germanic and Latin). 1. Germanic suffixed form *wih-l- in Old English wigle, divination, sorcery, akin to the Germanic source of Old French guile, cun- ning, trickery: GUILE. 2. Germanic expressive form *wikk- in: a. Old English wicca, wizard, and wicce, witch: WITCH; b. Old English wiccian, to cast a spell: BEWITCH. 3. Possible suffixed zero-grade form *wik-t- imé in Latin victima, animal used as sacrifice, victim (although this may belong to another root *(a)wek- not otherwise represented in English): vicTiM. [Pok. 1. weik- 1128.] weik-3, To be like. 1. Suffixed variant form ‘*eik-on- in Greek eikdn, likeness, image: ICON, (ICONIC), ICONO-; ANISEIKONIA. 2. Prefixed and suffixed zero-grade form *n-wik-és, not like (*n-, not; see ne), in Greek aikés, unseemly: AECIUM. [Pok. 3. weik- 1129.] weik-4. Also weig-. To bend, wind. I. Form weig-. 1. Ger- manic *wik- in: a. Old English wice, wych elm (having pliant branches): wyCH ELM; b. Swedish viker, willow twig, wand, akin to the Scandinavian source of Middle English wiker, wicker: WICKER; C. Old Norse vikja, to bend, turn, probably akin to the Scandinavian source of Old North French wiket, wicket (< “door that turns”): WICKET. 2. Germanic *waikwaz in: a. Old Norse veikr, pliant: WEAK; b. Dutch week, weak, soft: WEAKFISH. 3. Germanic *wik6n-, “a turning,” series, in Old English wicu, wice, week: WEEK. II. Form *weik-. Zero-grade form *wik- in: a. Latin vix (genitive vicis), turn, situ- ation, change: VICAR, (VICARIOUS), VICE; VICISSITUDE; b. Latin vicia, vetch (< “twining plant”): veTCH. [Pok. 4. ueik- 1130.] weik-5, To fight, conquer. 1. Germanic “wik- in Old Norse vigr, able in battle: WIGHT2. 2. Nasalized zero-grade form *wi-n-k- in Latin vincere (past participle victus), to conquer: VANQUISH, VICTOR, VINCIBLE; CONVINCE, EVICT. [Pok. 2. weik- 1128.] weip-. To turn, vacillate, tremble ecstatically. 1. O-grade form *woip- in Germanic *waif- in Old Norse veif, waving thing, flag, probably akin to the Scandinavian source of Anglo-Norman waif, ownerless property: WAIF!, (WAIVE), (WAIVER). 2. Variant form *weib- in Germanic *wipjan, to move back and forth, in: a. Old English wipian, to wipe: WIPE; b. Old French guiper, to cover with silk: GUIPURE; c. Middle Dutch and Middle Low German wippen, to swing: WHIP. 3. Perhaps suffixed nasalized zero-grade form *wi-m-p-ila- in: a. Old English wimpel, covering for the neck (< “something that winds around”): WIMPLE; b. perhaps Middle Dutch wimmel, auger (< “that which turns in boring”): WIMBLE. 4. Suf- fixed zero-grade variant form *wib-ro- in Latin vibrdre, to vibrate: VIBRATE. [Pok. weip- 1131.] weis-. To flow. I. 1. Germanic *wisdn-, waisén- in Old English wdse, mire, mud: 00ZE?. 2. Taken by many as a derivative of this root, but probably an independent Indo-European word, is the suffixed form *wis-o- in Latin virus, slime, poison: VIRUS. 3. Extended zero-grade form *wisk- possibly in Latin viscum, mistletoe, birdlime: VISCID, VISCOUS. II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words
2269:SLAUGHTER  slak- SLAVER! |leb-1 SLAY slak- SLED sleidh- SLEDGE sleidh- SLEDGEHAMMER slak- SLEEP sléb- SLEET sleu- SLEEVE sleubh- SLEIGH sleidh- SLEIGHT slak- SLEW! sloug- SLICK lei- SLIDE sleidh- SLIGHT lei- SLIM leb-1 SLIME lei- SLING! slengWh- SLINGSHOT slengh- SLINK sleng’h- SLIP! lei-
```


## [2026-09-06T22:57:20.140Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lagar\\|lāgar\\|láγar\\|lagor\\|Per. lay\\|lay ‘mud\\|lay, ‘mud\" IEC.txt | head -20; echo \"=== around 9557 ===\"; sed -n 9548,9570p IEC.txt",
 "description": "Search IEC for lagar and lay"
}
```


### [2026-09-06T22:57:20.209Z] TOOL RESULT

```
9412:lag- (1) limp, weak; be limp, slack’, etc. (Gk. ambig. Cf. slag-). Cf. WP II, 381 & 712 (For Gk. lagaíó ‘release’; lagarós ‘Hmp, loose? see slag-); Olr. laigiu, adj. “less; Ir. lag ‘weak, low, base’; lagaim, tr. ‘weaken’; intr. ‘relax, flag’; laige, f. ‘weakness, swoon’; W Ilai, adj. ‘less’; Cor. 18, id. (: Olr. laigiu, id.); LG lack, m. ‘flaw, fault; ME lack, wd: ON lakr, adj. ‘deficient’ beside lakra, v. ‘deteriorate’; G lech ‘parched’; cf. MHG lechezen, v. ‘pant, thirst’; G lechzen, id.; OFris. bi-leka, id. For Sequan- jan lagit, also written lag-, la- ‘damp; damp- ness’: W llaith, adj. & s. m. damp; moisture’. See next entry
9450:lakús, lakuos ‘lake, pool, puddle, pond’. WP II, 380 Gk. lákkos, m. ‘pit, puddle, tank’; Lat. lacus, gs. -üs, id.; Olr. lac, Ir. lag, m. *water-hole, pooľ beside (augmentative) lagán ‘puddle’; Br. Cor. cf. lagen, pl. lagennu, lagennow, f. ‘marsh, pond’; OE lagu, m. n. (lake, flood’; pl. ‘surface of the sea’); OS cf. lagu-stróm ‘waters’; ON lọgr, gs. lagar, ds legi, m. ‘sea, water; OCS loky, gs loküve, m. ‘puddle’; lokva, f. ‘rain’; Blg. lókva, Srb. lókva ‘puddle’
9470:lang- ‘drooping, sad; droop, be sad; sad- ness'. All evidence ambig. Per. ranja, ranjiš ‘sorrow, annoyance’; ranji- dan, inf. “be sad’; Gk. laggázo, laggéo ‘droop, flag’ beside lagarós, adj. ‘sunken, slack’. (For Lat. langueo, *slangu- and for Gk. lego: Alb. iodh, see slāĝ-)
9935:Inguhros ‘slight, nimble’. Cf. elnghus, elngu- hos Per. layar ‘lean’; OHG lungar ‘swift; OE lun- gre “quickly, soon'; Gk. (variant) elaphrós "lightweight, quick
10015:lõi- (1) 'sméared, sticky, greasy; smear’. WP II, 392 (Short grade in) Skt. láyah ‘adherence’; OCS (and com. Sl.) loj, m. “fat, grease’; Li. lájus, m. id.; (long-gde in Per. layi ( ‘mud’. Vowel
12972:plagoros ‘dashing, flighty; dash, flight W Iaer, pl. au. m. ‘ripple, ebb’; MHG vlacker, sm. ‘blaze, flicker’; OE flacor, s. “flight of ar- rows”
16186:slageros, ios ‘limp, weak, silly’. Cf. slagó and slágos Gk. lagarós, adj. ‘limp, slack, sunken, hollow’; W llair, m. ‘droop, limp object, satiety’; LG cf. slackern, v. “lounge, laze, slouch, slop’ be- side slackerig, adj. ‘limp, loose’
16187:slagð, ið “slacken, loose, make limp, ener- vate’. Cf. slagos, us & slagoros Gk. (ambig) lágnos (/riotous, lewd'. Cf. sIng-); OS slekkian, v. ‘blunt; OE sleacian, v. ‘retard, slacken’; E to slake — the thirst"; Du. slaken, v. ‘loosen, release’; ON. Sw. cf. slakna, intr. ‘slacken’. (EME isophone s. slake *snowflake?). Cf. WP II, 712. See next
16188:slágos, us “loose, slack, limp, weak’. Cf. slagð, slagoros OHG, MHG slahh, slach & slack, adj. limp’; OE sleac ‘sluggish; gentle’; LG & G schlack,
16190:adj. “pappy, limp'; Schlack, m. “pap; dirt; foul weather’; Schlacke, f. ‘sleet’; Icel. slakur, Sw. slak, as OHG; cf. Gk. lagarós, adj. ‘slack’ be- side (?) lágnos “lewd'; (long-gde in) Sw. sloka, v. ‘droop’; ON slókinn, m. "dot": LG slocks, m. id.; Li. slogus, adj. *onerous', beside slogà, f. (2) ‘deadweight, oppression’; cf. slogulys, m. “low spirits’; slogas, m. “load”. Cf. slóg- (1)
=== around 9557 ===
leghó — lei- (lin-)
20
25
30
35
40
45
670
hos) Lat. cf. le-pos, gs. -poris, m. ( hare, lit. *lFeghu- pods Jightfoot'?) The vocalism of Skt. la- ghüh, raghüh “light? is ambig.; that of OCS lí- gükü, id. obscure. Cf. WP II, 426 and cf. Cice- ro: lepus levipes
leguhos, is (leghus) ‘lightweight’. WP II, 426 Skt. cf. Jaghüh, raghüh, adj. id.; Alb. leh, adj. id.; Lat. levis, id. (the Lat. form may derive from a feminine, cf. suávis in relation to type *suadus, q.v.). Verbal forms include Alb. të lehun-it “act of parturition'; Lat. levo, are be- side levigo, àre and al-levio, are. (For Skt. rá- hami “part, abandon'; Av. raz-, id. and the Per. pp. rast, see rogh-. For Ir. leigim “let, leave, emit, drop" see lég- (leg- ?))
leguhtos, extn. of type leguhos, q.v. and cf. elnguhos Alb. i lehtë, adj. lightweight; OE cf. leoht, ON léttr, id.
leo, io “gather, pick, pick out, read WP II, 422 Gk. légo ‘gather, count, describe, read, say’; cf. sul-légó ‘gather’; Alb. cf. mb-ledh ('gather', fr. *kámbhi-le$-, cf. Gk. amphi-légo ‘dispute’, despite Doric -llégō); Alb. also zg-ledh, zgjedh (choose; dial. ‘read’, fr. *dis-^) and dial. g- ledh Cread" fr. *ko-1e$-); Lat. lego, ére ('gath- er, choose, read"; pf. legi); MIr. cf. de-ligim ‘separate’; W Hëu ( read, lecture’, prob. a Lat. LW); Br. (Lat. LW?) Jenn, léenn, m. (reading; cf. W lleain: Br. lenn, lenna, inf. ‘to read"; W dar-llen, id.)
lēĝð (log-, log-) ‘creep, climb, slide? OE cf. læcan (2) & (3) “link up with, emulate' beside ed-læcan ((repeat, renew’. Semantics obscure); Persian raz, s. (vineyard; grape": OCS & Slovak loza ‘vine’. See lo8-); OCS lézo, lěsti, v. ‘creep, march’; Cz. lezu, lésti, id. be- side (*-o- in) laziti (OCz.), id.; and (*-o- in) Slovak loziť, id.; Srb. laziti, inf. ‘go’; Latv. cf. lezns, adj. ‘flat’. (IsSophones: OS làknon “heal, cure, cf. E leechdom; Icel, lækur, pl. -ir ‘brook’)
lei- (lin-) “let, leave’ (as a sentence-particle). Cf. leið (4) Skt. cf. riye, mp. & rinámi, rinimi "let; release; sever; bestow’; Arm. cf. linim, inf. linel, aor.
671
3s. eye “be, become’; Hitt. lai, 3s. “releases, unharnesses'; prt. 1sg. låwun, mp 3s laittari; OCS cf. li, cj. “or; iP; Li. Latv. cf. lai... let.. ? beside Latv. leti ‘cheaply, easily; lēts ‘cheap, easy’. For the form *lin- cf. Skt. pp. rinah “van- ished’; Go. af-linnan ‘depart’; OHG bi-linnan ‘give way’; OE linnan, inf. ‘desist’; ON linna, Wk. vb. “cease”, etc. Cf. also hio (3)
(leib- *pour, libate', etc. see sleib-)
leibhó (sleibho ?) ‘graze, touch, stroke, car- ess’. (Evidence ambig. Cf. WP II 391 & 403) Gk. cf. a-leípho *embrocate'"; Lat. libo, åre (2) 'touch, try, sample, sip, taste’; dé-hbo, are (also: ‘bruise, hurt; diminish; pick out’); cf. also dé-libuo, ére, adj. -Iibütus, v. ‘daub’. (Iso- phonic: Srb. libiti se ‘be shy’ and (ambiguous- ly) OHG lib, m. n. ‘life and com. Gmc.)
leibhos (loibh-) «lean, slim’ OS lef ‘weak, ailing’, OCS libévü, libivü ‘slim, dainty’; Cz. libový, adj. ‘lean — of meat'; Li. líebas ‘lean — of horse’ beside láibas, adj. ‘lean, thin”
leidhð ‘incline, fall, descend’; (loidh-) ‘descent’. WP II, 395 MHG Die wf. ‘precipice’; OE *fidan, pp. liden incline’. The hapax ‘litar’ in Met. 26, 119 is due to confusion of líðan and lütan); Du. cf. overlijden, sv. 1. pp: -leden ‘die’; Sw. af- lida, sv. 1. id.; Li. leidZiüos, inf. léistis, refl. ‘set — of sun; descend’; leidimas ‘descent’. Cf. loidh-. (Isophonic: Li. léidZiu, OLi. léidmi, inf. leisti “release, let, issue")
leig- (pleig)? ‘rudder’ Arm. yeak, gs yeki, absg. yekav, (and yek, -i, -av), id.; Ir. cf. liagán and liogán, m. id.; W llyw, pl. -iau, m. id.; OCor. lew, pl. -yow, m. id. beside loē, pl. loeow ‘ruler’
leiĝ- (1) ‘lick’. Cf. lig- and leigh-. WP II, 400. Celt. & Sl. ambig. Arm. lezum, (aor. lezi), beside lizem, id.; Olr. & Ir. liag, f. ‘spoon’; W llwy, pl. -au, f. id.; Cz. liz, m. ‘salt-lick’; cf. OCz. lızák ‘tongue’; OCS 1170, lizati, v. (“TTick?, and com. Sl.); Li. liežiù, liēžti, id.; o-gde in Latv. laizīt, id.
leig- (2), leigio ‘creep, go’. Cf. Ioig- Skt. réjami, réje (1) ‘go’; OFris. liza ‘run, go’; Icel. cf. lík "leech-line'; o-gde in OCS l&zgo, lésti ‘creep, go’, and com. SI.
```


## [2026-09-06T22:57:21.574Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\[pdf page\\|\\[pdf page\" IEC.txt | head -3; echo \"---\"; grep -c \"\" IEC.txt; echo \"=== find page markers near 9557 ===\"; sed -n 9500,9560p IEC.txt | grep -n \"^[0-9]\\{3\\}\" | head",
 "description": "Check IEC page markers"
}
```


### [2026-09-06T22:57:21.649Z] TOOL RESULT

```
---
20499
=== find page markers near 9557 ===
12:666
20:667
34:668
41:669
56:670
```


## [2026-09-06T22:57:30.925Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=9880 && NR<=9945 && /^[0-9]{3}$/ {print NR\": \"$0}' IEC.txt; echo \"--- entry 9935 ---\"; sed -n 9930,9940p IEC.txt; echo \"=== pages near 10015 ===\"; awk 'NR>=9960 && NR<=10020 && /^[0-9]{3}$/ {print NR\": \"$0}' IEC.txt; echo \"--- 10010-10020 ---\"; sed -n 10010,10022p IEC.txt",
 "description": "Locate IEC page numbers for lagar and loi entries"
}
```


### [2026-09-06T22:57:32.889Z] TOOL RESULT

```
9883: 696
9889: 697
9903: 698
9913: 699
9930: 700
9940: 701
--- entry 9935 ---
700
Ingh-, cf. lengh-, longh-. WP I, 436 Av. (ambig.) rag- (1) “jump; Gk. lákhos, eos, n. ‘casting of lot; ON lung, n. (*warship'. Ambig. cf. elnguhis, etc.); Li. linge “steel spring’ beside linga, f. ‘sling’
Inghus, (variant of type elnguhos, elnghus,
etc.) Hom. cf. lákheia (queried: *quickly, soon?) beside Gk. elakhüs ‘diminutive’; SGer. lung ‘soft, gentle’ beside Lung, m. ‘success, ad- vancement'
Inguhes (Inguhen-) *tung(s)'. WP II, 427 Arm. langk, g. langac, abl. -awk, pl. id.; OHG lungün, pl. id.; OE lungen, f. sg. id.; ON lungu, npl. id.; OS cf. lungandia, wf. id. (and com. Gmc.)
Inguhros ‘slight, nimble’. Cf. elnghus, elngu- hos Per. layar ‘lean’; OHG lungar ‘swift; OE lun- gre “quickly, soon'; Gk. (variant) elaphrós "lightweight, quick
Inquo, aio, eio (?) ‘shine’. (Evidence ambig.) Skt. radical rak- in rākayāmi ‘relish’ beside rakah ‘symbolic sun-gem, crystal; Gk. lámpo ‘shine’; lamprós ‘bright, clear, keen’; Li. (?) linkiü, čti “wish sb. sth?; linksmas, adj. ^mer- ry’; OCz. (?) leke sé, 3s., inf. lakati sé “break, of day'
Inquos, ios, à, io “bent, turned; bend, turn, twist". Cf. lenquo, lonqueió Cz. leč, gs. -i, -e, f. ‘noose, snare’; Li. linkà ‘direction’; linke, f. ‘bend, twist’; liñkis, io, m. id. and ‘detour, bend in river’; linkstu, inf. linkti, intr. ‘bend’; Latv. līks, adj. ‘bent’; licis ‘bend in river, bay, inlet; cf. līku locu 'zig- zag
lobos “lap, flap, lobe’. WP II, 431 & 714 Gk. lobós ‘lobe’; W llof, pl. au, m. ‘growth, polypus'; MHG laffe, wf. ‘palm of the hand’; OE lzppa, wm. ‘piece, lap, lobe’; EME lap ‘lobe — of the ear; rag’; Du. lap, m. ‘rag, flap’; Norw. lapp, lappe ‘patch, piece’; Sw. lapp, m. pl. ar ‘flap, patch’; LG Lappen, id. (LW in HG); G cf. laff, adj. ‘limp; cowardly’
(lobh-, ambig. in Du. Fris. laf ‘insipid, cowardly, muggy, clumsy, stupid; G Labbe ‘hanging lip’; ON lafa, v. ‘dangie’; mod. laf, n. ‘garment’. See labh-. Long-gde in OE lefe, (fr.
701
=== pages near 10015 ===
9966: 703
9979: 704
9991: 705
10008: 706
10016: 707
--- 10010-10020 ---
loisuos, à ‘free, open; field, pasture’. (Se- mantics of types aruos & loukos, q. v.) OE læs, gs læswe, f. ‘pasture, ley’; LG lees, n. trushbed'; OCS (?) lésü “forest? (and com. SL); Li. laísvas ‘free’ beside (*-1-) lysve, f. *gar- den-bed"; liesvos, fpl. ‘stairs’. Ambiguously to OCS lěxa, f. *garden-plot'; Lusat. lécha, id. (and ‘ploughed strip) See loisa. An EME form leasow (cited by C. T. Onions, but not by S. Johnson or R. Ainsworth) is given as ‘pasture, meadow’.
loiqusos (loisquo-) “abandoned. Cf. leiqu-, liqu-, etc. OE læwsa “weak, poor’; (e-gde in OCS lixü fremaining"); Li. laiSküs, adj. ‘rancid’; Latv. laisks, adj. ‘sluggish’
loitos, om, à (1) ‘hateful, nasty; pain, harm, disgust, evi. WP II, 401 Gk. loitós, m. ‘plague’; cf. a-loitós, m. ‘rogue’; OHG leid, MHG leit, gs leides, adj. ‘repul- sive’; MHG leide, sf. ‘sorrow’; Du. leed, n. id.; OE làp, adj. 'evil'; s.n. “pain; nuisance’; OS léth, adj. & n. as OE; ON leiór, adj., leiði, m. as OE ; Sw. led, adj. “disgusting”; leda, f. “dis- gust?
loitos, us (2) ‘pouring; downpour, stream’. Cf. leiio, lio (leið (1)) Skt. rétas, n. ‘stream; libation; semen; Av. raetus, m. ‘fluid’; Lat. (ambig.) litus, gs -oris, n. ‘shore’; Li. lietüs, m. ‘rain’ beside (?) lai- tas (casting-floor of furnace’; Latv. lietus, m. as Li. (An Aeolic isophone occurs in a hapax loitos nóo “pure in mind” or sim.)
loitos, us (lit-) (3) ‘touch, stroke, smear. Cf. leio (2), loi-, loi- Lat. cf. (z-gde) litus, adj. “marked, smeared; adorned'; litus, gs -üs, f. “marking, smearing, adornment’; Li. lieciu, liesti, v. touch, con- cern’ beside lieta, f. “matter, concern’; Latv. laitit, v. freq. ‘massage’
lõi- (1) 'sméared, sticky, greasy; smear’. WP II, 392 (Short grade in) Skt. láyah ‘adherence’; OCS (and com. Sl.) loj, m. “fat, grease’; Li. lájus, m. id.; (long-gde in Per. layi ( ‘mud’. Vowel
707
ambig.); Alb. lyej, aor. leva, lyva & lyejta, v. ‘smear’; Blg. OCz. Pol. lajno, lajno, tajno ‘cowdung’; Cz. lejno, id.; Srb. cf. also po-loj ‘marsh’
loi- (loios, á) (2) “layer, slice’. WP II, 406 OS leia ‘rock, schist; MHG lei, leie, f. id. (and ‘slate’); Du. lei, f. ‘slate’; R cf. s-loj “layer, stratum, seam; lamina’; Cz. sloj, id.; Pol. słój ‘grain in wood’
loksos (variant of type luksos (2) q.v.) ‘crooked, bent’. Cf. WP I, 157 Skt. raksas, n. “injury; demon’; Gk. loxós ‘awry, crooked’; MIr. and Ir. losc (alame'. Am- big. cf. luksos); Cor. ambig. logh ‘lax’; OCS, Big. Srb. loší, loš (“bad, eviľ, fr. *loksio-); ON lọskr (‘weak, limp’ beside e-gde MHG er-lëschen ‘subside, go out from a variant *losk-, *lesk-); Li. cf. ãt-lašas “bent back’. See next, but cf. at-lósti, inf. “bend back? (!)
lokstos, a ‘athwart, crooked; thwart, cross- piece, crook, bend, fold’. Cf. loksos (Mod. Gk. lostós ‘bar’. Andrioti — the anc. Gk. fr. a type *loKstio-?); OIr. locht, f. “fault, wrong’; Li. lákstas ‘folded sheet, diploma, letter, page’; (lakstà ‘roost, perch’: Latv. lakta, f. id.? For OE læst ‘blame’; ON last, n. id. and Gk. lásthe, see Supt: L. Andrioti's derivation of lostós from loisthos is negated by the pre- sence of Blg. lost ‘bar’ as given under lakstis. Li. & Latv. ambig.)
lom-, lóm-, see lomos, lomeió, lómos
lombos, lomb- ‘hang; hanging; suspense; pendant, tag, bob, strip’. Cf. lemb-, lembh- and next Skt. lambe, mp. “hang, lag, dangle’; Hes. lóm- bai ‘child initiation, w. vows to Artemis’; lom- boi, mpi. ‘strips, strippings'; cf. lombrós, m. ('striptease' or sim.); NGer. lampen, v. “hang limp’; OE cf. lemp-healt, adj. (hapax) limp- ing; ON leppr, m. ‘rag; ringlet. (E-gde in MHG limpfen, E to limp, v. id. NB. Fr. lam- beau ‘rag’ is fr. Lat. limbellu-s, as langue fr. lingua-. Li. lámbas, m. ‘proboscis’ is an iso- phone)
```


## [2026-09-06T22:57:44.469Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in HRN.txt HUB.txt; do echo \"=== $f ===\"; grep -n -i \"lāġar\\|lagar\\|láġar\\|lāgar\\|lâgar\" $f | head -5; done; echo \"=== HRN lai ===\"; grep -n -i \"^\\s*[0-9]*\\.\\?\\s*lai\\b\\|lāi\\|lāj\" HRN.txt | head -10",
 "description": "Grep Horn/Hübschmann"
}
```


## [2026-09-06T22:57:46.088Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"لاغر\" MON_part1.txt MON_part2.txt BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/ARY/ARY_pages.txt 2>/dev/null | head -20",
 "description": "Grep Persian sources for لاغر"
}
```


### [2026-09-06T22:57:46.119Z] TOOL RESULT

```
=== HRN.txt ===
98:hier überhaupt davon zu sprechen, wenn nicht de Lagarde
232:hauptsächlich aus de Lagarde's Arbeiten geschöpft, die
492:*) de Lagarde, Persische Studien, 70 verfährt zu künstlieh.
512:Strassburger Handschrift nicht in Ordnung).de Lagarde's Erklärung (zuletzt Pers. Studien 75)
556:vergl. Talmud LW. •imnx (de Lagard e, Semitica
=== HUB.txt ===
309:entlehnt, ebenso das syr. Wort, vgl. de Lagarde, G. A.
662:148. Lies Jtori^^iq und vgl. de Lagarde, G. A. p. 73,
993:*mskart (vgl. de Lagarde, Pers. Stud. p. 75) zu-
1001:'Ente', das de Lagarde vergleicht, ist nicht verwandt
1319:stellt de Lagarde (Btrg. zur bactr. Lexic. p. 54) nebst
=== HRN lai ===
22752:lai'jbs 44.
```


### [2026-09-06T22:57:46.177Z] TOOL RESULT

```
incoming/BQT/BQT_v4_pages.txt:7778:ضعیف ترکیب و لاغرهم کفته‌اند ؛ وباین معنی ناووس *۰۱ بروزن نافوی . آتشکده
incoming/BQT/BQT_v4_pages.txt:10771:‏الاغراق کوید : « و ازاکانت الافلاك حبة ولها مدیرات ۰ فلایکون مدبرانپا عللها + اذ لاستکمل‎
incoming/BQT/BQT_v4_pages.txt:10773:۰ ‏فیکون مدیرها لوراً مجرداً قد دمیه «النور الاسقهید» ...۲ ( حکمقالاغراق مصحح «. کربین‎
incoming/BQT/BQT_v4_pages.txt:19287:«هورخش» الاعظم فی‌المتدین المبجل الذی هووجهةال الملیا علی لان‌الاغراق, فانه‌القایم علی
incoming/BQT/BQT_v4_pages.txt:22330:وه دو چیزیست که لقیض هم باغد سوای لاغر | زده/ بزبان رومی حنا را کوب وآن چیزست
BQT_v1_pages.txt:8420:آ گر مه باکاف‌فارسی بروزن لاغر»سرین
BQT_v1_pages.txt:8510:اس تب که هض لاغرباشد ٩‏ .
BQT_v1_pages.txt:8597:۲ لر - بروزن لاغر ۰ کقل و رین را
BQT_v1_pages.txt:9076:سود لاغر که ۳۹1 رزق رت
BQT_v1_pages.txt:9922:لاغر باشد ۵.
BQT_v1_pages.txt:9942:ولاغراست . « جفتائی 4 » م رکب از آت** آد بمعنی نام ومزه‌ادات منلب . مجموع کلمه می‌نم
BQT_v1_pages.txt:19909:لاغر است. و بکر ثالث هم آمده است
BQT_v1_pages.txt:23379:هاغر - بر وزن لاغر, ستوئی راکویند
BQT_v1_pages.txt:25828:- کفلهاتی گرد و یش و دم دراز بر وبال فریی و لاغر یفن
incoming/BQT/BQT_v3_pages.txt:6059:و له لاغر باشد ۱ .
incoming/BQT/BQT_v3_pages.txt:10006:‏- وبعربی مردم‌ضعیف ولاغر را گویند ۸ و کوش"
incoming/BQT/BQT_v3_pages.txt:17595:‏لاغر است .
incoming/BQT/BQT_v3_pages.txt:22504:باشد - ومردم درازوباريك ولاغررانیز گفته‌اند۴ .
incoming/BQT/BQT_v3_pages.txt:24660:باشد . خوردن آن با سکنجبین بدن را لاغر
incoming/BQT/BQT_v3_pages.txt:26611:ولاغراست گوبند : « کاله عود شکاعی» .
```


## [2026-09-06T22:57:55.217Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt && head -c 600 MON_part1.txt; echo; echo \"=== ARY ===\"; grep -n \"لاغر\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY lای ===\"; grep -n \"^لای\\|لای \" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Inspect MON and ARY"
}
```


### [2026-09-06T22:57:55.288Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی 
=== ARY ===
=== ARY lای ===
628:کیفیت والای این اثر در سطحی است که امروزه هم برای شناخت زبان سانسکریت از آن استفاده
888:لهستاتی مولای /
1055:تحت‌الشعاع قرار نمی‌داد. شاه در بالای هرم قدرت قرار داشت ولی پدر و رئیس ابل نیز هر یک
1118:[. البته ارج اجتماعی آنها با مقام والای لبیدهای باستانی قابل مقایسه نیست. متاسفانه اختراع رادیو و
1162:هجوم اعراب و استبلای طولانی آنها بر فلات ایران بزرگترین عامل دگمرگونی آوایی و
1292:متفاوتی استفاده می‌کنند. در این کناب کوشش شده است تا حد امکان املای واژه‌ها یکدست بشود.
1304:۴-املای واژه‌های هند و اروپایی نیز درکتابهای مختلف متفاوت است. در این کتاب پیشتر از
1305:طرز املای /3۳۷(/0100 08 01071007۸73 3۸8017۸7 786 استفاده شده است.
1433:لاین (712ل): 105 2 (781 86) :ما05
1733:لاین (1۸710): 58 ,۷5838 7 (۷881) ,1224 (8۸3) چیه
```


## [2026-09-06T22:58:01.074Z] TOOL CALL #20: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py; echo ===; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['MON','BQT','ARY','VOP','IEC']:\n    print(k, json.dumps(d[k],ensure_ascii=False)[:1200]); print()\n\"",
 "description": "Inspect ref_page tool and MON/BQT config"
}
```


### [2026-09-06T22:58:02.643Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-06T22:58:07.217Z] TOOL CALL #21: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['MON','BQT','ARY','VOP']:\n    v=d[k]\n    print('##',k, v.get('kind'), '| local:',v.get('local_file'))\n    print('hint:', (v.get('lookup_hint') or '')[:300])\n    print('scans:', json.dumps(v.get('scans'),ensure_ascii=False)[:800])\n    print()\n\"",
 "description": "Show MON/BQT/ARY/VOP scan config"
}
```


### [2026-09-06T22:58:09.152Z] TOOL RESULT

```
## MON website+archive_djvu | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
scans: null

## BQT archive_djvu+local_scan_ocr | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
scans: [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, chec

## ARY local_scan_ocr | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
scans: [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf", "first_printed": 1, "last_printed": 546, "pdf_offset": -1, "lang": "fas+eng", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"}]

## VOP none | local: None
hint: Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).
scans: null
```


## [2026-09-06T22:58:23.632Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index legwh/leg ===\"; grep -n -i \"LEGWH\\|LEG.H\\|LEGH\\|LEVIS\\|SLEI\\|LEI-\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Grep ARY latin index"
}
```


### [2026-09-06T22:58:23.674Z] TOOL RESULT

```
=== ARY latin index legwh/leg ===
2208:Oj egtisleisl | Ae
2431:wcesl Ag OS jT (Legh 5 j)gSi Jove) GAVO-STANA 4 (ml 6, 5 hygSs Jou) ASPO-STANA
10081:oplasaT CQL) caleghl Je sete arly gle 22 > cate 9 Sr at) STIR: pl 9 oo
13241:DELAMARRE: (LECHER) 266 SLEIKJA
```


## [2026-09-06T22:58:25.855Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v3/v4 headword لاغر ===\"; grep -n \"لاغر\" incoming/BQT/BQT_v3_pages_faseng.txt incoming/BQT/BQT_v4_pages_faseng.txt 2>/dev/null | head -20; echo \"=== لای headword ===\"; grep -n \"^لای\\|لای ـ\\|«لای»\" incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -10",
 "description": "Grep BQT for headwords"
}
```


### [2026-09-06T22:58:25.928Z] TOOL RESULT

```
=== BQT v3/v4 headword لاغر ===
=== لای headword ===
incoming/BQT/BQT_v4_pages.txt:11773:لای غفی هربی هم هست۱ + مهمانی ودیدن مردمان بزر که پوشند ویغیر از
incoming/BQT/BQT_v3_pages.txt:20542:لاینی ‎psyllium‏ . ۷ رل : فان . ‎nt - A‏ معنی مصحف«مسن» ‎A)‏
```


## [2026-09-06T22:58:34.623Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for w in \"لاف\" \"لاله\" \"لاغ\" \"لابه\"; do echo \"== $w ==\"; awk -v w=\"$w\" '/\\[pdf page/{p=$0} index($0,w){print p\" :: \"$0}' BQT_v4_pages.txt | head -6; done",
 "description": "Locate BQT lam-alef section"
}
```


### [2026-09-06T22:58:36.521Z] TOOL RESULT

```
== لاف ==
[pdf page 28] :: از نقل اقوال مختلی گوید : « حاسلآنکه درین لفت اضطراب بسیار واختلاف پیشمار کرده‌اند :
[pdf page 31] :: ۵ مام لاف - قابله « رشیدی > و مخقف آن ماناف (ه.م.)
[pdf page 33] :: مافاف ؟ - بروزن آلاف . ماماچه را | پمتی‌سنکی است که درهندوستان میباشد. کویند
[pdf page 40] :: وکنایه از ممشوق هم هت ۲ . از توابع کرمان ۷ - و جمع ماه باشد برخلاف
[pdf page 44] :: ماهی اشنه - بفتح همزه . نوعی از بر خلاف قیای همچو سالیان که جمع سال
[pdf page 59] :: کتب خود را در زمان ویرانی با زوال مٌّداین نوشته اند - تعداد آنها را باختلاف ز کر کرده اند
== لاله ==
[pdf page 47] :: بممنی مادر اسر اس ت که زن پدر باشد ‏ لاله زار » هر چیز را کویند که با او کندکی
[pdf page 65] :: تا مورد سبز باشد چون زمرد تا لاله سرخ باشد چون مرجان.»
[pdf page 70] :: تیفهای کوه ازو پرلاله و پرسوسن است مرزهای باغ ازو پرسنبل وسیسنیی است .
[pdf page 113] :: پزربنه جام اسرون لمل مل فروزنده چون لاله بر زردگل .>
[pdf page 131] :: خوی کرفته لاله سیرابش از اتف لبید
[pdf page 188] :: زاله بروزن لاله . ممروق است وآن | رای قرشت و دال بی‌اقطه بالف کشیده وبرای بی
== لاغ ==
[pdf page 34] :: آید ) : «و مانند این عمل را معارعه خوانند .» ( ترجمان البلاغه بخش عکسی ص۲80 الف) .
[pdf page 97] :: واهل ماوراءاانعی پم میم خوانند . در نسخهٌ ترجمان‌البلاغه مکتوب بال ۵۰۷ قمری مشك جنم
[pdf page 97] :: اول ضبط شده ( رك : ترجمان البلاغه چاپ احمد آتش » بخش عکسی ص 4۷ب و۲۵۱ الف )
[pdf page 105] :: کده (پوند مکان) . 8 رد4 : مخلگاه . ۹ - رك : مغلاغ . ۷ - رك :
[pdf page 194] :: ضعیف ترکیب و لاغرهم کفته‌اند ؛ وباین معنی ناووس *۰۱ بروزن نافوی . آتشکده
[pdf page 203] :: استادان کلام را از پايٌ بلاغت افکندن است و مجوز شدن ضم لون بجعت قافیه در حق استادان
== لابه ==
[pdf page 385] :: وآن کلابه‌ایست که بردیرارمالند و بربالای آن وق * - بنتح اول و ضم ثالی وسکون
```


## [2026-09-06T22:58:42.143Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk '/\\[pdf page/{p=$0} /لاغر/{print p\" :: \"$0}' BQT_v3_pages.txt | head -12; echo \"== لاف ==\"; awk '/\\[pdf page/{p=$0} /لاف/{print p\" :: \"$0}' BQT_v3_pages.txt | sed -n 1,12p",
 "description": "Search BQT vol3 for لاغر"
}
```


### [2026-09-06T22:58:43.836Z] TOOL RESULT

```
[pdf page 81] :: و له لاغر باشد ۱ .
[pdf page 133] :: ‏- وبعربی مردم‌ضعیف ولاغر را گویند ۸ و کوش"
[pdf page 243] :: ‏لاغر است .
[pdf page 308] :: باشد - ومردم درازوباريك ولاغررانیز گفته‌اند۴ .
[pdf page 339] :: باشد . خوردن آن با سکنجبین بدن را لاغر
[pdf page 365] :: ولاغراست گوبند : « کاله عود شکاعی» .
[pdf page 365] :: بسیار لاغر و ضعیف شده باشد ۴ - و ان ختك
[pdf page 365] :: ‎wry‏ ابیوردی درهجوزنك لاغری « جهانگیری».
[pdf page 380] :: ایجد ۰ بمعنی فربه باشد که درمقابللاغراست ۴
[pdf page 387] :: کتان شسته» وااگر خواهد که لاغرنشود برعکس
[pdf page 423] :: فربه باشدکه دربرابر لاغراست ۷ .
[pdf page 592] :: 2 لاغر واندك , ۷۵28 فوت » پابداری ) ( بمعنی استقامت و بابداری کم دارندء ) تم
== لاف ==
[pdf page 31] :: باشد لیکن برخلاف ‎old‏ .
[pdf page 42] :: ‏چاپ ملافیروز بکار رفته ودر برهان فاطع نوشته شده : «لفظی است درفارسی...» الجمن آرالوشته
[pdf page 66] :: ‏کلافه کرده را نیز گویند ۴ .*
[pdf page 66] :: ae . ‏اول بر وزن غلاف‎ So ۲ SES
[pdf page 81] :: که کرسته ولافر باشد . و بعضی چاروای فربه
[pdf page 89] :: است اختلاف در دال ورا شده است ۳ .
[pdf page 92] :: ‏در غلاف طولالی دراز منکون شود ‎OT,‏ غلاف را
[pdf page 127] :: صدق ‎CUS‏ - کنابه از فلك الافلا
[pdf page 140] :: واين نام را درسکه‌های امپهبدان (اخلاف ‎Gy srl (GULL‏ پهلوی وهمچنین درمسکوکات حکام
[pdf page 145] :: ‏-یگرفته ز اسان تو درمم رکه لاف‎ ۸
[pdf page 156] :: ‏طیاف « بکراول‌بروزن غلافسنگینی
[pdf page 157] :: ‏طیلافیون * ‎cee‏ او و سکون
```


## [2026-09-06T22:58:52.753Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for w in لاجورد لاله لابه لاشه; do echo \"== $w ==\"; awk -v w=\"$w\" '/\\[pdf page/{p=$0} index($0,w){print p\" :: \"$0}' BQT_v3_pages.txt | head -4; done",
 "description": "Find lam section in BQT vol3"
}
```


### [2026-09-06T22:58:54.397Z] TOOL RESULT

```
== لاجورد ==
[pdf page 10] :: لاجورد. بمعنی شابود است که هاله وطرقوخرمن
[pdf page 15] :: ‏شادودد ۴ بر وزن لاجورده بسمنی
[pdf page 28] :: ‏شاه ورث ۴ - بروزن لاجورده بمعنی
[pdf page 30] :: بر وزن لاجورد » بمعنی
== لاله ==
[pdf page 5] :: ‎۰۶۱۸۹6 ۰ ‏چند بهار . مطبع نولکتور . لکهنو‎ els ‏عجم » لاله‎ hg = F
[pdf page 35] :: ‎james‏ (۳).نامی است از اسماء ‎cyl!‏ جل‌جلاله؛
[pdf page 65] :: دای ‎cts‏ لاله راگویند ‎bea es‏ | پا اسول باعد چنانکه سدابی ‎ach OTH‏ شود.
[pdf page 65] :: آرد:« الثقر والشقایق النسمان ‎WY.‏ اینکه لاله ‎polish‏ را نعمان با تعمانی یا
== لابه ==
[pdf page 202] :: ‏حوضها وته تالابها وجویها میباشد .
[pdf page 202] :: ‏بائد که در بن و ته حرضها وتالابها میباشد .
[pdf page 212] :: که در ته حوضها و جویها و تالابها بهم رسد
[pdf page 349] :: وکردنی هرت ۸ - وشیشةٌ صلابه کرده را نیز
== لاشه ==
[pdf page 102] :: که خاکروبه و خلاشه ویلیدیها درآن ريزد ۱
[pdf page 107] :: نام ماه دهم سال است «روزنامة کیلاشهر سال اول شمارة ۲۲: زندکی وعروسی ساکنن‌جنگل»,
[pdf page 674] :: - نیز لاش لش ع لاشه . مردار . جیفه « لفت نامه * . ۵ سای ال :
[pdf page 692] :: ‏۴ - لش بفتح اول لاش ۳ لاشه بمعنی جیفه » مردار ؛ جسد پیروح - کشته و پوست
```


## [2026-09-06T22:59:03.670Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 67[0-9]\\]/{print}' BQT_v3_pages.txt | head -200",
 "description": "Print BQT vol3 pdf pages 670-679"
}
```


### [2026-09-06T22:59:05.237Z] TOOL RESULT

```
[pdf page 670]
از کناب ‎ob,‏ قاطع درعرف لام با عروف تهجی ‎se‏
‏بر بیست و دو بیان و محثوی بر سبصد و هشتاد و شش
لت و ‎elf‏

بیان اول

در لام با الف مشتمل بر هفتاد و نه ‎cab‏ و کنایت

۶ لاس ‎NTs Vegan‏ وهرزه کوبی
و پر کوبی باشد ۱ - و در عریی بمعنی نه است

که تقیضآری باشد - وبمعنی نفی‌هم‌هست‌همچو
۷ اله الا ال . 1

وتان ۴ .

ats ‏با لامبروزن پا برجاه‎ - TV YY
‏تو پرتو و ته بر نه باشد - و نام نوعی از حلوا‎
- ‏هم هست‎

لاب = پروژن باب » ‎oth‏ بونانیآفتاب
را کوبند ؟- ونام‌پسرادری‌علیه‌السلام هم‌هست ‎٩۴‏
‏و بسی کویند نام حکیمی است که اصطرلاب را
او وضع کرده است ؛ و بسی دیگر گویند نام
بسن اسطر است » و اسطر نم پادشاهی بوده از

لا ۴ 2 بروزن تابه. بمعنی سخن‌باند

- و اظهار اخلاس با نیاز تمام را کویند- وبمعنی
چرب زبانی و چاپلوسی و تملق و ‎ID‏ وعجز

و یاز و خواهش هم‌هست ۵ - و فریب و بازی
۵ ل ( لام ) - حرف بیست و هفتم از الفبای فارسی وحرف بیست وسوم آزالفبای عربی
‎(on!)‏ و در حاب جمل ‎onl Soe WIT‏ حرف به «ر * ( رلك : ص بط مقدمهةٌ ملف )

بدل شود. ۱ ۰۷۰ اسم فاعل مرخم ‎col‏ در کلمات مر کب: ‎Vege‏ ژاژلا. رك:لاییدن.
۳ _ فقه‌اللَةٌ عامیانه. رك : اسطرلاب . ۴ - از: لا (طبغه) ‎H‏ بر(بمعنی‌علی‌عربی)
+۷ (طبقه) . ۴ « لاف ‎gal.‏ ع 1818. 18۳۵(خودستابی ۰ ‎SY) fuk ۰ GG‏

زن ) ) از ‎our‏ 120 ۵ . رك : هوبشمان ‎Mov‏ و رك : اسشق ‎tat‏ : کردی 1260
( استدعا « درخواست ) « ژابا س ۳۷۵ » ورك : لابیدن .
© - تواورا کنیلابه فردا به پیش فدا داری او را تن و جان خوش .
فردوسی طوسی « لفت نامه > .

[pdf page 671]
" لایدن - ۱۸۷5
دادن را هم میگویند ۱ - و چیزی ‎jth‏ گویند
که از سر تا بیای چیزی به پیچند .

لا بیفن ۲ ه بروزن و معنی لافیدن(۱)
است که سخنان زیاده از حد خودگفتن باشد -
و بمعنی پر گوبی وهرزه کوبی هم هست.

‎SY‏ » با تحتالی بواو کشیده ۰ تردبان
وزینه پابه را وبند ۴ - وبمعنی گردنا هپت
‎OT;‏ چوبی ‎oth‏ مخروطی ومیخی کوچكك برس
‎oT‏ سب کرده‌اند و اطفال رسمانی برآن پیچند
و وعی بر زمین اندازند که مدتی چرخ زند -
و تله را نیز گویند که آلت کرفتار شدن‌حیوادات

‏و لاغ باشد که بمعنی سخره و ظرافت است.

‏لاجوده ۱ - بنتح ‎sly‏ و سکون را
و دال بی‌نقطه , سنگی‌است کبود که ازآن ‎SS‏
‏انگفتر سازند و صلابه کرده بجپت مذهبان
و نقاشان بعمل آورند و تفریج و تقویت کند
وبدختی ‎oT‏ بهتر از دزماری باشد .

‏لاجود۵ خم یت خای ‎abit‏ دار
و سکون میم . کنابه ازآسمان است و آنرا خم
لاجورد هم میگویند .

‏لاچوردی سقف © بمعنیلاجوردی
خم است که کنابه از آسمان باشد .

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
‏( برهان ‎ab‏ ۳۴۷ )

[pdf page 672]
و۱۸۷

‎Oy = ‘ey‏ شاخ » بمعنی‌جای ومقام
باشد لیکن بدون ت رکیب کفته نمیشود همجو
منگه لاخ و دیولاخ و رودلاخ یعنی جای‌منگه
‎yo ley‏ وجای رودخانه - و بمعنی بسیاروانبوه
نیزآمده است وباین ععنی عم ‎ys‏ گفته نمشود؛
و بفیر اژین سه‌محل ‎cle ye‏ دنگراستممال‌نشده
ات ؟ .

‏لاخشته ۳ - بکرنالت بروزن آغشته,
نوعی از آش آرد باشد ؛ و بسضی گویند آش‌تتماج
است +

‏لاخشه ۴ < بروزن فاحته.بمعنیلاختته
است که نوعی از آش‌آرد باشد ؛ گویندآش‌تتماج
است .
لاخه - بفتح نالث . ‎ines‏ پینه و ‎wale‏
‏باشد - ولاخه‌دوز پنبه‌دوز را گویند .

‏لاخیز * = بروزن ‎li‏ بععنی‌سپلاب

‎. ath

‏۰ - پوند مکان که با خر ‎GUIS‏ چون :

‏لاد

‏لاد © بر وزن شاد » بمعتی دیوار باشد
چه سرلاد سر دیوار و بن‌لاد ين دبوار را گوند
- و ‎ska‏ وبنای ‎dps‏ را ‎Vashi” as‏ - واصل
هرچیز را هم ‎Van Se‏ و درمقام سبب وجهت
نیز گفته میشود مثل ‎Cal‏ هرگاء گوبند « لاد
برین » مراد اين باشد که بتابرین و بدین سبب
و ازین جپت - و هرچینه و رده را نیز گویند
از ‎SIT ys‏ بر بالای هم گذارند۸ - ویممتی
دیبای نازل وتنك ولطیف وخوض قماش باشده ؛
و درعربی نیز همین معنی دارد ‎-٩*‏ و ‎Pale‏
‏میگویند وبعربی تراب ‎Waals‏ - ومخففلادن
‎Fou a‏ وآن نوعی از مشمومات است بعنی
بوی کردنیها - و نام شهر لار بوده است در قدییم
و درین زمان دال برا تبدیل یافته است ۱۴-وهر
کل و شکوفه را نیز کویند 9۴- وبمعنی] بادانی
هم آمده است که درمقابل خرابی است - وقلمه

‏را نیز گویند .

‏نمك لاخ » دیولاخ , سنگلاخ , اهرمن لاخ ۰

‏رود لاخ ‎ST.‏ لاخ , هندولاح » کلوغ لاخ و غیره پیوندد : « واین بحیرء ( پختگان ) ‎EVA‏

‏است. » « فارسنامه. این‌البلخی س ۱۵۳ ۰

‏۴ - درموارد دیگرهم آعده .)4 ‎Nee‏

‏. ورگ : دارمستتر . شبعات ج ۱ ص ۲۹۷ .

‎masse ‏لا کشت س لا کشه‎ m= P

‏لا که = لخشکه << الاخته «الطبیخ ص۷۹ »؛ نوعی رشته , رشته‌ای که لوزی برند . آش یکه

‏از ‎oT‏ پزند . رك ‎cab‏ نامه : لاخشه .

‏۴ هس لاخشته ‎(p.m)‏

‎. * ‏نامه‎ cab « ‏؛ که ازآن گل ولای خیزد‎ (os) ‏از: لا (لای) + خیز‎ O°

‎٩‏ - بچشم سریکی بنگر سح رگاه

‏۲ - بنگفتم نکو ‎Jbl.‏

‏این سخن را قوی نيامد لاد.

‏برین دولاب می دیوار و ‎Me‏ .
ناصر خرو بلخی ‎cad?‏ نامه».
ممود سمد «أت‌نامه».

‎geet ۸‏ اول. ‏ 8 پندمده‌شا نکه پند ‎wT ple‏ خاراپوشد کسی بزبرخز ولاد.

‏ناصرخرو بلخی < لفت نامه * .

‏*۶- معرب آن لان است : ركك : بتیمقالدهر چاپ دمشق ج ۶ ص ۱۶۹ ی ۱۵ .

‏۱ ره : ح۱ ‎inte‏ بمد.

‏۴- سپاهان بگودرز کشواد داد

‏قس : اسپندیاد ۳ اسفندبار .
```


## [2026-09-06T22:59:11.618Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 67[3-6]\\]/{print}' BQT_v3_pages.txt",
 "description": "Print BQT vol3 pdf pages 673-676"
}
```


### [2026-09-06T22:59:13.176Z] TOOL RESULT

```
[pdf page 673]
لادن

ان ۱ - بر وزن دادن ۰ توعی از
مشمومات است نی بوی ‎oS‏ و آن ‎aa‏
‏دوشاب ‎Le‏ میباشد ‎LT,‏ عنبر ‎he‏ گوبند ودر
دواها بکار برند و آن از زمین ‎yi,‏ حاصل
میشود باين طریق که کیاهی که از آن زمین روبد
بلادن آغشته باشد و بزآنگیاه را دوست‌میدارو
وبهنگام چرا رش و موی بدن بز بدان آلوده
میشود بعدازآن جدا میسازند. وآلچه بررش بز
آلوده باشد بهتر از آن است که بر موی ران
و اعنای ‎Ks‏ . گوبند اگر ‎nip‏ دامن زنی
که ‎dee‏ مرده درشکم داشته باشد بخور کنند ‎Be‏
‏مرده آزمشیمه بیرون آید ۴ .

لك 4 - بکس ‎dt‏ و فتح ‎Sos‏
‏باشد که از پوست ‎OT GL‏ ربسمان سازند .

لاه ‎ne‏ وزن ساده ۰ بمعتی ‎iat,‏
‏و احمق و ابله باشد ۴ - و سگه ماده را نیز
گوینه ۴ .

لارجان ه باجیم بروزن خاکدان,

۱۸۷۹

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

‎GRY‏ بفتح سین بی نقطه وکاف

‏۱ - معرب ‎oT‏ لادن . لادنة . لانن » لاتینی 120851050 , خجرتاللادن ‏ 56اه ,

‏6 با 160150 «دزی ج» ص ‎tort‏ بونانی. ‎Jadanon‏ آشوری ‎lotemy -c.ladunu‏
+ عقار ۲*۸ ف». لادن» شیر درختی است ازلوع پيچك » این شبرء اکر ازبر گهای‌درخت بزمين
فرو چکد و ‎MEL‏ در آمیزد کم ارزش تر است . در اشعار آمده : * بخیزد از ‎ole‏ لاد لادن ©
از لاد که بمعنی ‎ME‏ و کل است , همان زمین آغشته بشیره با صمغ لادن مقصود است . رك :
هرمزدتامه ۱۱۲-۱۵۸ +

‏۴ امروزه لادن تام قسمی ‎JS‏ است ‎Tropacolum majus , Capucine)‏ (
ازخانوادة 1۳0۳60186665 « دارای ‎BL‏ نازك وخزنده و بر کهای کرد و کلهای کم پر با پرپر
زرد ۰ تاریجی با قرمز و دو رلگه .

‏۴ - نه که هر زن دغا و لاده بود شیر لر هت و شیر ماده بود .

‏اوحدی « لغت نامه > .
۴ رك : لای بلاج . © « لاریجان ؛ ناحیتی است ازشمال محدود به‌آمل واز
مثرق به بندپی و از جنوب بدماوند و از مغرب به دلارستاق. این ‎aot‏ دارایآبهای فراوان و
‎daly‏ خاکهای آ تشفشانی بسیار حاصلخیز است . رل : کیهان . جغرافیای سیاسی ص ۲۹۵ ورلد:
عمج‌البلدان . ۲ رك : لغت نامه . ۷ = لاجورد ‎(ee)‏
‎Cpa) Yom ۸‏ درکیلکی ‎)las‏ ابرشم ‎cone ab‏
۵ لار یجان - رك : لارجان .

‎gy ‏رك: لابه‎ ٩

[pdf page 674]
۰ 7-۱۸۷۷ لاغوی

و راو بتحتالی رسیده » نام جانور کی‌است کوچك لاغر و پیرو زبون را گویند - و مرد؛ جمیع
وخوشآواز ‎٩‏ . حیوانات را یز کمته‌اند 6 .
‎a‏ 1

لاش ه بر وزن فاش . بزبان مرغزی ‎EY‏ « بروزن ‎«bb‏ هزلوظرافت‌وخوش
بممنی ناخت و تاراج و ‎ode‏ باشد ۴ و مرغز | طبمی باشد ‎٩‏ - و بمعنی فریب و بازی و فریب
نام جابی‌ومقامی است ۴ ب و بمعتی ضایم‌وزبون و بازی دادن و بازی کردن و مخ رکی لمودن
و فرومایه و بی اعتبار نیز گفته‌اند ۴ - وبمعنی هم‌هست - و بمعنی بددل و بددلی ودل بدکردن
هیچ باشد ۴ - وچیز اند و کم و کوچك رالیز هم‌آمده است 3
کوید .: ‎ow ge¥‏ ۷ با غين نقطهداربروزن‌ناقوی,

لاشکن - ‎GEL‏ بر وزن بادزن ۰ نم | بزبان رومی در موبدالفضلا خر کوش را کویند
کرهی است فزديك بملك روی ؛ و ‎oth‏ معتی_ | و پعربی ارنب و بخطائی توشقان خواند . کویند
بحذف شین تقطه‌دار هم آمده است . پای وی تا با زن باشدآ بستن نشود. اگرپنیرماية

لاه ‎e‏ پروژن ماشه ۰ آدم و اسب وخر | او را با مسکه وعسل ح لکنند وهرزنی که‌بخورد

٩ ‏میره یا مرغ کوچك دیگری است و با رندة کوچک ی که امروز * سسکه‎ Leb - ٩
‏موسیقی کمان‌برد‌اند.‎ MATL ‏نامیده میشود . بستی ابن کلمه را بمعنی لحنی از الحان موسیقی‎
: ‏این غلط ر اشتباهت‎ Lace ‏نیافتم . و بیت ذبل منوچهری ظاهراً‎ OT ‏ولی من شاهدی برای‎

خول طنبوره تو کوبی زند ولاسکوی از درختی بدرختی شود و گوید: آم.

اين لاسکوی مثل طنبوره, مفعول « زدن © نست, بلکه مبتدای ‎ae‏ مد است ۰ معطوف‌به‌خول,
و فاعل «شدن» « ‎cad‏ نامه > .

۴ - بدین رزمگاه اندر ‎tal‏ مباش ممان تا شو دکنج و لشکر بلاش .

فردوسی طوسی ‎cad?‏ نامه *

۴ - رك : موغز . ۴ - درین معنی شابد مخفف * لاشی" * عربی باشد «لفت
نامه ۴ . در عربی تیز لاش لاشی» « دزی ج ۷ ص ۵۰۷ ‎٩‏ :
دبر ‎als‏ که کند چرخ ‎wa‏ این‌همه را یکره ‎jae‏ ولاش .
ناصرخرو پلخی «لفت نامه * .
- نیز لاش لش ع لاشه . مردار . جیفه « لفت نامه * . ۵ سای ال :
با ‎ys LEY jhe‏ سفید برسوار ‎Ob‏ خواخم فشاند. « خافالی شروالی ‎Nay‏
‏زهزل و لاغ و آزار خیزد مزاح سرد آب رو بریزد .

ناصر خسرو بلخی > لفت نامه » .
‎Laghdds yu, - ۰‏ > لك ۱ص ۰۱ ۰ . رك : لاغون .
‎AYO‏ - بختح سوم « کردی 188067 « ژابا س ۳۷۵ ‎AS: ٩‏ و برنی 18966 .
فریزیدی ۱8987 نطنزی 1888 دکه . ۱ص ۲۹۳ ‎٩‏ . سنگری » مرخه‌یی» لاسگردی و
شهمیرزادی 12087« که . ۷ ص ۱۹4 ۰ . باريك . پاريك اندام » مقابل فربه :
توچنین فربه ‎tle ATs‏ پدرت هندوبی ‎oy‏ یکی لاغر وخشکانج وسیف؟
لبیبی « لفت نامه .

[pdf page 675]
—Navag og

دیگر آبتن شود و اکر بضود برگیرد ‎PHT‏
‏گردد ۷ .

لاغون ۳ © پروزن حامون ,بلغت‌رومی
بمعنی لاغوس باشد که خر کوش است .

لاغیفه = بروزنآدینه , درختی‌است(۱)
که آب از بالای ‎OT‏ بتدریج فرود آید و جمع
شود ؛ و ‎Sol‏ معنی بحذف نون هم بنظر آمده
است که لاغیه باشد ؛ و بجای نون تای مثلثه حم
‎ow‏ شده است که لاغبثه باشد ‎Sell‏ ۴ .

‎racy‏ © بر وزن بادیه » نباتی است
‎wh JTLT,‏ مانتد کل شبت و زنبور ع ل کل
آنرا خورد وچون‌ب ‎US‏ شاخی از آن جدا کنند
شیر بیاری از وی برآید . کرم و خشك است
درسیم » اکر از چوب آن برآبی که ماهی‌داشته
باشد اندازند ‎Lee‏ ماهیان پر روی آب ‎AL‏
‏و در عربی سخن باطل وزن بیهوده کوی را
کریند * .

‎VS‏ - بروزن‌کاف . کلامفولوعبارت

‏کشاده و خوبتتن ستایی و خودسایی باشد ۷ -
و بیحیا و بیحیاییرا نیز کوبتد .

‏لایس ۸ = بافای بتحتان ی کشیدموبین
بی‌نقطةٌ زده « لام دبوی است که مردم را در تماز
وسوسه کند ؛ و باين معنی بجای > ‎NG‏ قاف
هم بنظ‌آمده است .

‎SY‏ = بروزن ‎NE‏ بممنی ‎Ub‏ وکاسه
‎Ly‏ چوبین باشد ‎٩‏ - و لا پشت و کاسه ‎ee‏
‏را نیز گویند ‎-٩*‏ و نام رنگی است مشهور ۱۱
که درهندوستان بهم میرسد و بدان‌چیزها رنگه
کنند و آن شبنمی باشد که بر شاخهای درخت
‎LT‏ و درختهای دیگر نشیند و منجمد کردد
وآثرا بکیرند و بکوبند و بیزند ۰ ازآن رنگه
سرخی حاصل کردد که مصوران و نقاشان هم کار
کنند و غازة زنالرا نیز ‎OT‏ سازند ‎Missy‏ آن
‎wale‏ صمغ باشد » و بدان کارد وشمشیر وخنجر
‎LTE,‏ دردسته محکم کنند و بکارهای‌دیگر
نیز ‎ale‏ و هر چیز ضایم و زبون را نیز

‏(۱) لفت نامه ‎cate) br‏ او در پستی کوه باشد که ) برای تکمیل عبارت اقزوده شده.

‏۱ رك : خ رکوش . ره : لاغوس . ۴ ره : لاغیه .

‏۴ در عقار ۷۱۵ آمده : « لاعية ( با عين مهمله ) هی الحلبلاب » و بمجمية الاندلی
لختر ‎Jy‏ ( 126087101 ) و قد ‏ کرناها من اصناف البتوع .» در بسض نخ ‎ate‏ ابن الببطار
دلاغیه » آمده ‎oly‏ صحیح با عين مهمله است = ‎Buphorbe‏ )3( « عقار ۷۱۵ ف >.

‏۵ رك : منتهی‌الارب ؛ و رك : لاغ . ۲ - پهلوی ‎laf‏ ( شکایت ) « منای

‏۰ ۷:۷۷۸ ۰ کردی ‎laf‏ و ‎law‏ ( سخن بیپوده ) « ژابا ص ۳۷۵ .
- ابا ز بیم زبانم لژ دکشته ‎Slay‏ کجا شد آنیمه دعوی و لاف وآنهمه ژاژ ؟
لیسی « لفت نامه > .

‏۸ -ظ . مصحف لافیی ( لقی ککتف ... وس کننده و بدی اندازنده ‎les‏ مردم ...

‏لفس عیب کردن « منتهی.الارب * ) :

‏توگفتی که عفربت لاقیس ( لافیس ) بود بزشتی لمودار ابلیس بود +
سعدی ‎CN‏ « رخیدی » « لفت نامه > .
4 س لا وکه . *- جلد ‎Yan J je‏ جانوران. ذبل سنگه پشت . قس‌:لا2 پشت.

‎lakkha ‏متوسط‎ sae ‏از‎ , laque ‏فراسوی‎ ۰ lakxa ‏در بونانی‎ . Cea

‏کرفته شده . بضی پنداشته‌اند در قرن اول و دوم میلادی ‎bark‏ رسیده , ولی مانند کلمةٌ حندی
قلفل, ‎fe‏ پیونان رسید‌بود )353 ‎(Journal Asiatique, tome CCXXXIV, p.‏
بقلم ‎J.Filliozat‏ . و رك : دزی « لك » . ورك : ‎Laufer, Sino _ Iranica, p-585‏

[pdf page 676]
۱۸۷۹

میگویند ۱ - و درعربی بمعنی‌خاییدن وجاوبدن
باشد ۳ .*#

لا کچ ۳ - بر وزن باغچه . بسعنی
‎cls‏ باشد ‎oT,‏ آشی است ممروف .

لا کن ه بفتح ‎A‏ پروزن ‎OY‏ بمعنی
لاشکن است ۴ و آن‌کوهی باشد نزديك بملك
92 1
لا « بر وزن مال » ممروف است که
‎KS‏ و زبانگرفته بائد ‎٩‏ - و رنگه سرخ‌زا
نیز کفته اند ۱ - و بمعنی لمل هم آمده است
وآن کوهرست کرانهایه که ممدن‌آن دربدخشان
است و بعربی لعل کویند , و ‎ge‏ کویند لعل

۱ < لک < لکات « انندراج » :
با مردم ‎FED‏ بتوانی بمیامیز

معرب لال است ۷ .

‎VY‏ - بر وزن کلا + بمعنی غلام و بنده
وختمتکار باشد ۸ - و پر کوبی وهرزه چانگیر!
نیز کوبند ‎٩‏ - و گیاهی‌هم هست که‌آنرا ازجالب
مکه‌آورند وبخورآن دفع ‎cle‏ بواسیر کند *۷-
و بمعنی درخشنده هم آمده است چتانکه گوند
لژلژی ‎i WY‏ مروارید. درخشنده ‎WY‏ وداته
ات مانندکنجد - و بسنی گویند باين ععنی
و ممنی تکرار در لفی عربی است ۱۴

‎FN pe VY‏ بفتح سین بینقطه.خواجه
سرا را کونند بعنی غلامی که آلت تناسل او را

‎. ‏جز از عار بیاید زلك و لاکه‎ Sys
> ‏فرهنگگ اسدی «لفت نامه‎ Lie . Spe

‏۴ - در عربی خاییدن « لوکه » است و « لا » فسل ماضی آنست . « لفت نامه >.

‏۴ لا که لاخشه ‏ لاخشته ‏ لششه .

‏۴ ره : لاشکن .

‎Mal AS eh gy Cold ‏در اراك ( سلطانآباد) یز‎ ۰٩۳۷۹ ‏ژابا س‎ « lal ‏کردی‎ ٩

‏۲ - دو لب چو نار ‎AT‏ دور چو سوسن سرخ
دو رخ چو نار شکفته , دو لب چو ‎DY‏ لال .

‏۴ ح لمل معرب «لال» است « نغب ۱4 ‎٩‏ .

‏۸ ح لله :
‎pad‏ از روم و لجاشی‌ازحبشی

‏پردرش‌فیروز ولالا دیده‌ام.

‏عتصری بلخی « لفت نامه > .
« لال , لمل باشد * « لغت فری ‎OTN‏

‏خاقانی شروالی « لفت نامه > .

‎. ‏بدین ممنی « هرزه لا » است . سراج‌اللفات بنقل فرهنگه نظام ج ه ص م‎ - ٩
‏حکیم مومن » لفت نامه . بممنی اخیر عربی است . سراح‌اللفات بنقل‎ line : ‏رل‎ ۶

‏فرهنگه نظام چ ۵ سم 1

‏0- از عربی « ‎DD‏ لت نامه > .

‏۴- درعربی بمعن ی گیاه مذکور آمده - ‎ety‏ نه‌نه ‎ALG)‏ درنقی ) است.
۴ از : لاله ( خواجه , غلام )+ سرا (سرای) لاله سرا ‎Cem)‏
‎Oo‏ لا پشت - ‎ge‏ چیارم , (رك ‎(SV:‏ جانورست از راستة لا که پشتان ۰ بردگه

‏زرد مایل پیز با له سیاه . خوراد
وی علف و ‎aL Tin,‏ است وکاهی
نیز از حشرات تغذیه میکند . بهنگام
خطر اعنای خارچی خودرا داخل ‎BY‏
‏حیکند . تخم ‎SY‏ پشت ازپوستةآهکی

‏سفید پوشیده شده است .
```


## [2026-09-06T22:59:37.500Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 67[7-9]\\]|\\[pdf page 68[01]\\]/{print}' BQT_v3_pages.txt | grep -n \"لای\\|لا ی\" | head -40",
 "description": "Find لای entry in BQT vol3"
}
```


### [2026-09-06T22:59:39.084Z] TOOL RESULT

```
148:کزی را کویند که بر بالای دستار بتدند ۱ وآن
162:‏است و آن چهار ذرعی باشد که بر بالای دستار
252:‎ye)‏ مصتری ) ۶ لایین .
308:لاه ۴ = پر وزن ماه » بمعنی لای باشد
319:‏کفتن است حمچوهرزه لای (۷) یمنی‌هرزه گوی
320:و میلاید بعنی میگوید۷ - و بمعنی تالهکننده
333:عم ‎Chey SEB GY Ch gram is Kae‏ لای جامه
351:‏(۷) چش : هرزلای .
360:۴ -لای (کیلکی ‎(His‏ اعد تبدیل می» و «م» .
367:‏۲۷ - رك : لایدن .
371:‎Com) ‏اسم فاعل از «لاییدن»‎ - ٩
379:2-۰ : لاییدن .
381:‏0 از : لای۲-یدن ( پوند مصدری ) .
```


## [2026-09-06T22:59:41.756Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 680\\]|\\[pdf page 681\\]/{print}' BQT_v3_pages.txt | tail -80",
 "description": "Print BQT pdf pages 680-681"
}
```


### [2026-09-06T22:59:43.649Z] TOOL RESULT

```
بمقدار يك قبضه و هر دو سر چوب کوتاه تیز
میباشد ۳ .

لاه ۴ = پر وزن ماه » بمعنی لای باشد
که نوعی از ‎ab‏ ابرشمی سرخ ‎Sy‏ است.

1295 Wass ‏با نون بر‎ - ٩ ‏ور‎ oY
‏بمعنی لاهور است و آن شهری باشدممروف.*#‎
‏لاهوره « بر وزن م‌اشوره » تراشه‎

و برش خریزه و هندوانه است وآنرا بت ‎FES‏

میگویند ‎٩‏ .
‎GY‏ - کون بای حلی ‎san)‏
‏کفتن است حمچوهرزه لای (۷) یمنی‌هرزه گوی
و میلاید بعنی میگوید۷ - و بمعنی تالهکننده
وهرزه کوننده بیز گونند ۷ - و آمی ‎cab‏ معنی
هم‌هنت یعلی ‎AW‏ کن و بگوی ۷ - و نوعی از
‎Sib‏ ابرشمی‌باشد که از چینآورند ودر گجرات

. ‏چك : بسکون با‎ (A)

0

نیز بافند وآن ساده و الوان هردو میباشد ۸ -
وگل تیره وسیاه را یز گوبند که در نه حوضها
و ‎lege‏ شیند - و دردی شراب و امثال ‎AT‏
‏یز گفته‌الد - و تای کاغن و ‎Anke‏ و رسمان را
عم ‎Chey SEB GY Ch gram is Kae‏ لای جامه
و يك ‎UY‏ رسمان و بعربی طاق گویند سویمعتی
درة کوه هم‌آهده است که ‎NAG‏ بين دوکوه
باشد .

‎WY‏ ۲ - بروزن شاید » بعنی ثاله کند
وهرزه ‎WP‏ . ۱

‎Sou‏ = بروزن آینده , ناله کننده
و هرزه کوینده را کویند . ,۲

‎Aly .‏ » بروزن قایمی , جامة کوتاهیرا

‏کویند که دروشان و فقیران پوشند ؛و بسنی
‎Late‏ یتمیرا گفته‌اند خواه دروشان پوشندوخواه

‏!= بروزن ناهید » یعنی‌تاله کرد

‏(۷) چش : هرزلای .

‏۱ - فی: پهلوی ‎rapak‏ (در ‎karth‏ _ ۲80816 بمعنی فرباد » ‎(ols‏ » منانسکریت
‎lap.‏ ( وژوزکردن » پر کوبی کردن ) , ق1218 ( ناله کردن » فربادکردن ) ‎By‏ : نیب رکه
ص۱۹۱ ؛کردی 161۲10 12۷20 ( تهاضا کردن » درخواست کردن ) « ژابا س ۳۷۹ > .

‏۴ « اما عاقلتر ازو در جوال‌افتمال غماز و ‎plas‏ شدماند و بسحال وعشوه و لاوة ایشان

‏مقرو رگشته .» « راحةالسدور راوندی بتقل لفت نامه > .
۴ -لای (کیلکی ‎(His‏ اعد تبدیل می» و «م» .

‏ی لاو ‎(Cem)‏
‏۵ رك : لاهور (هم)

‎٩‏ - جمم که چون خربزه است تا لبری چون خورند

‏۲۷ - رك : لایدن .

‏:۰ - اکسون زرنگار فلك را چوآستر

‎Com) ‏اسم فاعل از «لاییدن»‎ - ٩

‏بشکن و پیدا شود ‎cond‏ لاهوره‌ای .

‏مولوی بلخی رومی « ‎Cad‏ نامه » .

‏بر ابر ‎pine‏ این ‎SY‏ ساده یبن .
سیف اسفرنگگ « لفت نامه > .
2-۰ : لاییدن .

‏0 از : لای۲-یدن ( پوند مصدری ) .
۵ لاهور = لاوهور ‏ لهاور. شپری با کستان » کرسی‌پنجاب 6 دارای ۷۲۰۰۰٩سکنه.‏
```


## [2026-09-06T22:59:55.656Z] TOOL CALL #31: Bash

```json
{
 "command": "ls site/pages/305.jpg 2>/dev/null; pdftoppm -f 305 -l 305 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg305 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 305"
}
```


### [2026-09-06T22:59:57.520Z] TOOL RESULT

```
site/pages/305.jpg
total 127784
drwx------ 7 sfmqrb sfmqrb    12288 Sep  6 18:59 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   774972 Sep  6 18:54 afm143.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1046357 Sep  6 18:54 afm144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1012 Sep  6 18:57 agents.txt
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
-rw-rw-r-- 1 sfmqrb sfmqrb    24759 Sep  6 18:56 pg295_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80086 Sep  6 18:56 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56184 Sep  6 18:39 pg296.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130247 Sep  6 18:41 pg297hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60960 Sep  6 18:39 pg298.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99543 Sep  6 18:52 pg299hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61588 Sep  6 18:56 pg301.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91158 Sep  6 18:59 pg302.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122418 Sep  6 18:55 pg303hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89589 Sep  6 18:52 pg303.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58313 Sep  6 18:59 pg305.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50721 Sep  6 18:58 pg306.png
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


## [2026-09-06T23:00:01.580Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg305.png"
}
```


### [2026-09-06T23:00:01.909Z] TOOL RESULT

```

```


## [2026-09-06T23:00:01.906Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T23:00:16.461Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 305 -l 305 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg305hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg305hi.png'); print(im.size)\nW,H=im.size\n# latin node entry0: approx y 0.30-0.35 of page, x 0.22-0.55\nim.crop((int(0.20*W),int(0.295*H),int(0.58*W),int(0.345*H))).save('p305_lat0.png')\nim.crop((int(0.20*W),int(0.555*H),int(0.42*W),int(0.605*H))).save('p305_lat1.png')\nim.crop((int(0.40*W),int(0.195*H),int(0.80*W),int(0.245*H))).save('p305_empty.png')\n\"",
 "description": "Crop high-res regions of page 305"
}
```


### [2026-09-06T23:00:20.537Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-06T23:00:22.814Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p305_lat0.png"
}
```


### [2026-09-06T23:00:22.831Z] TOOL RESULT

```

```


## [2026-09-06T23:00:26.862Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p305_lat1.png"
}
```


### [2026-09-06T23:00:26.877Z] TOOL RESULT

```

```


## [2026-09-06T23:00:32.517Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p305_empty.png"
}
```


### [2026-09-06T23:00:32.585Z] TOOL RESULT

```

```


## [2026-09-06T23:00:32.582Z] INPUT

[Image: original 2040x330, displayed at 2000x324. Multiply coordinates by 1.02 to map to original image.]


## [2026-09-06T23:00:36.520Z] TOOL CALL #37: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T23:00:36.529Z] TOOL RESULT

```


```


## [2026-09-06T23:00:40.894Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%BA%D8%B1",
 "prompt": "Give the full Persian etymology section for لاغر (lāḡar) 'lean, thin': proposed origins, Middle Persian form, PIE root, and any cited sources (Hasandust, Cheung, MacKenzie)."
}
```


## [2026-09-06T23:00:43.143Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81le%E1%B8%B5%CA%B7%CA%B0-",
 "prompt": "What is the reconstructed PIE root for 'light (in weight)' — give the headword form, meaning, and descendants including Avestan, Latin levis, Proto-Germanic, Sanskrit laghu."
}
```


### [2026-09-06T23:00:45.088Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T23:00:48.606Z] TOOL RESULT

```
# Persian Etymology of لاغر (lāġar)

## Origins and Development

The word لاغر descends from **Middle Persian *lāgar**, inherited from **Old Persian *lagrah**. These trace back through **Proto-Iranian *Hlagráh** to **Proto-Indo-Iranian *Hlagʰrás**, ultimately deriving from the **Proto-Indo-European root *h₁lengʷʰ-** meaning "lightweight."

## PIE Root Structure

The complete PIE formation was *h₁ln̥gʷʰrós, combining the root *h₁lengʷʰ- with the suffix *-rós.

## Cognates

The entry notes relationships with **Northern Kurdish lawaz** and **Gurani لاواز (lāwāz)**, reflecting the shared Indo-European heritage.

## Cited Sources

The etymology references two scholarly works:

1. **Mann, Stuart E.** (1984–1987), *An Indo-European Comparative Dictionary*, Hamburg: Buske
2. **Nourai, Ali** (2011), *An Etymological Dictionary of Persian, English and other Indo-European Languages*

These sources support the reconstructed proto-language forms and the semantic trajectory from "lightweight" to "thin/lean."
```


## [2026-09-06T23:00:53.212Z] TOOL CALL #40: WebSearch

```json
{
 "query": "wiktionary Reconstruction Proto-Indo-European h₁lengʷʰ- light in weight",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


## [2026-09-06T23:00:55.007Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/carnival",
 "prompt": "Give the full etymology of 'carnival', including Medieval Latin carnelevamen/carnelevarium, Italian carnevale, the folk-etymology 'carne vale', and dates."
}
```


### [2026-09-06T23:01:00.741Z] TOOL RESULT

```
Web search results for query: "wiktionary Reconstruction Proto-Indo-European h₁lengʷʰ- light in weight"

Links: [{"title":"Reconstruction:Proto-Germanic/lungô - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/lung%C3%B4"},{"title":"Reconstruction:Proto-Indo-European/h₁lengʷʰ- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81leng%CA%B7%CA%B0-"},{"title":"light - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/light"},{"title":"Reconstruction:Proto-Indo-European/h₁léngʰus - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81l%C3%A9ng%CA%B0us"},{"title":"Reconstruction:Proto-Celtic/ɸlengeti - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Celtic/lengeti"},{"title":"lung - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/w/index.php?title=lung"},{"title":"lev - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/w/index.php?title=lev"},{"title":"levis - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/levis"},{"title":"User:Sobreira/PIE adjectives - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/User:Sobreira/PIE_adjectives"},{"title":"User:Sobreira/PIE roots h - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/User:Sobreira/PIE_roots_h"}]

Based on the search results, I found information about this Proto-Indo-European root in Wiktionary.

The Proto-Indo-European root *h₁lengʷʰ- means "light in weight; nimble". This root appears across multiple language families and has various descendants, including:

- English "light" (in the sense of low weight), which derives from Proto-Germanic *linhtaz or *līhtaz, which in turn comes from this PIE root
- The word "lung," which comes from Proto-Germanic *lungô meaning "the light organ"
- Latin "levis" (light/lightweight), which derives from Proto-Italic *leɣʷis, from the PIE form *h₁léngʰus


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-06T23:01:02.099Z] TOOL RESULT

```
# Etymology of Carnival

**Origin and Development:**
The word "carnival" entered English around 1540, derived from French *carnaval*, which came from Italian *carnevale* meaning "Shrove Tuesday." The Italian term evolved from older forms such as Milanese *carnelevale* and Old Pisan *carnelevare*, literally meaning "to remove meat."

**Linguistic Components:**
The term combines Latin *caro* (flesh, originally "a piece of flesh") with *levare* (to lighten, raise, or remove). These roots trace back to Proto-Indo-European origins: *sker-* meaning "to cut" and *legwh-* meaning "not heavy, having little weight."

**Folk Etymology:**
A popular but disputed explanation suggests the Medieval Latin phrase *carne vale*—interpreted as "'flesh, farewell!'"—influenced the word's meaning and form.

**Semantic Evolution:**
By the 1590s, "carnival" was used figuratively to describe "feasting or revelry in general." The modern American sense of "a circus or amusement fair" developed later, appearing in written records by 1926.
```


## [2026-09-06T23:01:10.902Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81leng%CA%B7%CA%B0-",
 "prompt": "Give the root form, meaning, derived terms and full descendant list — especially Proto-Indo-Iranian/Avestan ragu, Latin levis/levāre, Proto-Germanic *linhtaz/*lį̄htaz, Sanskrit laghu/raghu, and any Persian descendants."
}
```


## [2026-09-06T23:01:12.730Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%DB%8C",
 "prompt": "Give the Persian entry for لای — all senses ('mud, silt, sediment' etc.) and its etymology, including any Middle Persian or PIE reconstruction and cited sources."
}
```


### [2026-09-06T23:01:18.780Z] TOOL RESULT

```
# Proto-Indo-European Root *h₁lengʷʰ-

## Root Form
**\*h₁lengʷʰ-**

## Meaning
The root conveys two related senses: 1) "to move lightly, effortlessly" and 2) "lightweight." Its antonym is \*gʷerh₂-.

## Selected Derived Terms
The entry documents 54 categories of derived terms, including:
- \*h₁léngʷʰ-e-ti (thematic root verb)
- \*h₁lengʷʰ-to-s (yielding Albanian lehtë, Germanic descendants)
- \*h₁léngʷʰ-isth₂-o-s (producing Ancient Greek ἐλάχιστος)
- \*h₁léngʷʰ-yōs ~ \*h₁ln̥gʷʰ-is-és (Celtic and Greek comparatives)

## Major Descendants
The documented lineage includes Sanskrit raṃháyati, Avestan frarəṇjaiieiti, Latin-related forms, Ancient Greek elắssōn/elắttōn, Old Irish laigiu, Welsh llai, Old Armenian lanǰkʻ, Tocharian B lankᵤtse, and Illyrian lembus.

The Wiktionary entry emphasizes these are **reconstructed terms** based on comparative evidence rather than directly attested forms.
```


### [2026-09-06T23:01:20.514Z] TOOL RESULT

```
# Persian Entry for لای (lây)

## Senses

The word has three distinct etymologies in Persian:

**Etymology 1:** An alternative form of لا (lâ), meaning "fold, ply, etc."

**Etymology 2:** The primary sense referring to "dreg, sediment, dreck, mud" or "valley between mountains." This entry notes: "Compare لجن (lajan, 'mud on the bottom; blockhead, stupid fellow'), and Icelandic leðja."

**Etymology 3:** Derived from the stem of نالیدن (nâlidan), meaning "to complain, to moan, to groan," this sense denotes "one who complains, lamenter."

## Etymology and Sources

The Wiktionary entry explicitly states the Etymology 2 section is "missing or incomplete" and requests additional information. No Middle Persian or Proto-Indo-European reconstructions are provided in this source document.

The entry references two historical lexicographic sources:
- Steingass, Francis Joseph (1892), *A Comprehensive Persian–English dictionary*
- Vullers, Johann August (1856–1864), *Lexicon Persico-Latinum etymologicum*

However, these sources are cited but not quoted in the content provided.
```


## [2026-09-06T23:01:30.003Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/slime",
 "prompt": "Give the full etymology of 'slime': Old English slim, Proto-Germanic form, PIE root and cognates (Latin limus, linere)."
}
```


## [2026-09-06T23:01:31.432Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/limus",
 "prompt": "Give the Latin entry for līmus 'mud, slime': etymology, PIE root, and relation to linō/linere 'to smear'. Also note any separate limus 'askew'."
}
```


### [2026-09-06T23:01:37.473Z] TOOL RESULT

```
# Etymology of Slime

**Old English Origin:**
The word derives from Old English *slim*, meaning "soft mud."

**Proto-Germanic Form:**
It comes from Proto-Germanic *\*slimaz*, which also produced Old Norse *slim*, Dutch *slijm* ("slime, phlegm"), and German *Schleim* ("slime"). This form likely relates to Old English *lim* ("birdlime; sticky substance").

**PIE Root:**
The ultimate source is the Proto-Indo-European root *\*(s)lei-*, described as meaning "slimy, sticky, slippery."

**Cognates:**
The document provides extensive cognates across Indo-European languages:
- **Latin**: *limus* ("slime, mud, mire") and *linere* ("to daub, besmear")
- **Sanskrit**: *linati* ("sticks, stays, adheres")
- **Russian**: *slimak* ("snail")
- **Greek**: *leimax* ("snail") and *limne* ("marsh, pool, lake")
- **Old Irish**: *sligim* ("to smear")
- **Welsh**: *llyfn* ("smooth")

The semantic thread connecting these cognates revolves around adhesiveness, moisture, and slipperiness—core qualities associated with slimy substances.
```


### [2026-09-06T23:01:39.968Z] TOOL RESULT

```
# Latin *Līmus* Entries

## Mud/Slime (Etymology 2)

The noun *līmus* meaning "mud, slime, muck" derives from uncertain origins, "maybe from Proto-Indo-European *h₂leyH- ('to smear')" or related to slime concepts. Cognates include Greek *límnē* (marsh/lake), Sanskrit *lināti* (adheres/slips), and English *slime*.

The entry does not explicitly relate this sense to *linō/linere* 'to smear,' though the proposed PIE root *h₂leyH-* shares the smearing semantic domain.

## Askew/Sidelong (Etymology 1)

A separate adjective *līmus* means "sidelong, askew, aslant, askance." Its etymology states it "Possibly from Proto-Italic *līmos* ('oblique'), with no known cognates outside of Italic," potentially deriving from PIE *Heh₃l-* ('to bend').

## Key Distinction

These represent distinct etymologies: the mud sense traces to smearing-related roots, while the adjective reflects an "oblique" or "bent" semantic path—two separate Latin words sharing identical forms.
```


## [2026-09-06T23:01:46.075Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ragu\\|rəvī\\|rävi\\|rawi\" BRT.txt | head -20",
 "description": "Grep Bartholomae for ragu"
}
```


### [2026-09-06T23:01:46.123Z] TOOL RESULT

```
3834:Bed.  nach  ai.  aihidhSna-  n.;  s.  Haug Essaus' i8i,  Gdn.  KZ.  ij.  189,  FrMöller  WZKM. l.  161.  DST.  ZA.  3,  95  lisst  ia  nnberfick- sichtigL  —  Pü,!  afiat  rawiitü/i.
5914:•  j.  asmaniva-  n.,  Plur.  Bezeichnung  ge- wisser Teile  des  (tierischen)  Unterleibs'': hazanrtm  anumayanqm  frävinuyät  vTspa- nam:a  aSaSsam  fasvam  'vä  (AP.)  zaoira iire  . ,  frabarBil  bszva  aiwyS  . .  frabarnit ". .  und  von  all  diesen  Tieren  soll  man die  A.  sammt  Z.  dem  Feuer . ,  darbringen, die  Vorderfiisse  aber  soll  man  den  , , Wassern  darbringen"  V.1S.70.
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
7038:satz'so,  dann;  da.' -.yezi ('wenn') aAipaurva.- naem3l  3'  mqm  avi.rimilnaya  (sd.)  Yt.16. 2;  a.  3-3,  Y.2.43,  ^'.36,  103,  /ö'.ii,Nik. 3,  Vd.  13';  —  yat  ('wenn')  yave  dayat ä'  datva  y^ism  (sd.)  V.J. 32;  321,  H.  2". 13,  N.  IJ2;  —  3at  (s.  8)  yat  apö  uzbargnte .  .  a°  fraiasinti  . .  fravasayö  Yt.  13.65; V.  Ä40,  i7.4;  —  yat  ("als')  mqm  tura pazdayatita  .  .  3'  az3m  tanüm  aguze  .  . \3at  (s.  3)  mqm  fraguzayanta  ..Yt  i7.  55^'; — yas}  tat  nmäfum  äk^rstmn  .  .  «7°  mqm tnairyö  akasat  dai  (s.  2)  .  .  fräksrmaot V.  22.  i£;  —  3at  (s.  8)  yat  miirtm  .  . /radaöqm   .  .   a°  dim  danqm  ,  .  Yt.  10.  i ;
7265:13,  N.  Ö2;  —  äat  (s.  8)  yat  äpd  udiannte .  .  ä'  fralasinH  .  .  fravalayS  Yt  JJ.  65; V,  ^,40,  ^7.4;  —  yat  ('als')  mqm  Iura pazdayaiita  . .  ä°  azsm  tanüm  aguze  . . äat  (s.  3)  mamfraguzayanta  ..  Yt  i;.  553'; — yas)  Uli  mnärom  äktrirum  .  .  ü°  mam mairyd  äkasat  äat  (s.  2)  .  .  fräkirmaot V.  22.  if;    —    äat  (s.  8)  yat  mi>r)m   .  .
7779:g.  Hyä  Y.  47.»:  s.  '«.  II  2  1. j.  ^^m,  lii'um:  s.  nrävi-  mit  No.  1.
7817:•  g.  a^nman-  n.  'Stetigkeit;  Unaufhörlich- keit': al  kahrplm  utayäitJs  äadät  armaiti^ 'mä  (AP.)'*  "und  Arm.  verlieh  den  Leibern Dauer  und  Stetigkeit"  Y.jo.;.  a)  LS. °m7nT  als  Adv.  'stets,  ewiglich;  unaufhör- lich"'; yi  'mSnl  mazdn  srävi  ahurd  "der ewiglich  MAk.  heisst"  Y.  45. 10;  —  yaii' gqm  karaps  usixscä  (sd.)  alhmUi  däii yücä    kavä   *'mJnI^^    urüdSyatä  (sd.)    Y.
8242:Ableit.  aas  *iii%j-S-,  S  26S.  32.  —  Pü.:  ä»  i iiisr  -  mai  -  ia  .,  aiäv  J'räi  hambarim  rawisnih harn  *parsind,  mit  der  Erl.i):  *gffwlnd hl  eiak fa  dißkar  e  ya:fnd*.  —  i)  Vgl.  PÜ.  lU  N.  ö-'-
8244:pü.:  ä%  (in  Aw.-Buchst.)  rawiinlh,  erl.:  mazg 'Hirn'.
8641:•Z)m  utäiSta  (sd.)  V. /5.3  s  f. Zum  V.  datz..  —  ai,  vgl.  uddriikä-  f.  'Ter- mite'. —  Pü,i  uidakisi.  —  ')  Ao  V.  3.  9  an- geglichen, statt  Tfldaeia  'durch  Erdabi  ragung'. —  '1  ^g.  'welche  durch  Erdauficbüttang  auf- geschüttet werden';  s.  zAusdr.  yr-ii^ii-  No.  1.
9008:24  genannten  Bergs,  anj^ebl.  idiidräsfi,  den man  für  idenlkch  hielt,  s.  vunStackelber<i WZKM.  12.  239. •  j.,  g.  ka'iH  Adv.  1)  "wie?,  in  welcher Weise':  "^il  '>,wä  mazda  xlnaoiiii  {%A^  V. 4O.  1;  —  °^ff  zaoia  gidh  /rasrävayätti N'.W;  Vyt.j/C?);  —  -^d  ffjv7w»»  ^/-a.- iri^j-S  Oa  ..  ii/aJasJ  "wie  ists  geschehen, dass  du  . .  gestorben,  wie  dass  du  .  ." K.  2.  16;  16;  —  °ä(7'>  ajfiirS  daxsära fiiasaysi  dlsil  "durch  welches  Zeichen "' willst  du  die  Tage  kund  machen  für  dte Befragung?"  Y,4j.  7".  a)  als  Indefini- tum,  a)  mit  vorausg.  ja^a  und  folg.  ca  "wie, in  welcher  Weise  auch  immer':  hvqm  anu usiim  zaos?mca  yaiia  "iiaca  hs  zaosö  "nach seinem  Willen  und  Gefallen,  wie  immer sein  Gefallen  war"  V.2. 11;  Yt/fj.82,  N. _J7.  b)  mit  Neg.  und  folg.  cina  'nicht irgendwie':  *'mä',a  ^'i^aäna  paitt.Jime  (.sä.) Vr.22.3.  2)  'wie  so?,  was  ist,  heissi das?,  was  hat  man  darunter  zu  verstehen? (die  Antwort  wird  mit  ya'^a  eingeleitet) °>a  alvö.gäimi  ra>a  '^ripai^m  "'wie  so eine  Schrittlänge?'    'Drei  Fuss'."   V.  5. 8;
9063:mit  7'i  'durch  Graben  beseitigen,  ab- tragen; zerstören':  yasca  .  .  daxmatiqm avavanhm  maz3  vtkanayät  ya>a  .  .  V.  7. 51 ; — yat  b.J  paiti  fra!st.>m  daxma  uzdaSza (sd.;  lies  vrd')  vJkanü  (3SPA.)  yahmya  . . "an  welchem  Ort  man  am  meisten  die  D. durch  Abtragung  zerstört,  wo  .  ."  V.  y. 13;  —  yat  bü  paiti  fraüittnt  vikmte (3SPM.)  .  .gjmam  V..J.Z2;  —Wäyadanä (sd.)  tyä  gauiii'ätJ'  . .  viyakai'  (3SPrA.) Bh. /.  14;  —  kyt^  aparam  imilm  dipim vaitnhy  ..  maty^  (sd.)  vikanähy^^  Bh. 4.  15;  16;— _jW;>  imrim  dipim  ..vainähy '.■ikanähidisi^  Bh.  4- 1 7  II  ■
9875:mit^a  'aus  dem  Versteck  hervorholen': äai  mam  fraguzayanta  . .  "da  holten  mich aus  dem  Versteck  . ."  Yt. /".  55.
10492:Zum  V.  grai->).—  ai.  vgl.  ^t-M-  f.  'GrifP.  — .  i^  iat/  h<nä..i4  ^.''sfjUh  x'ähiad pa  drS'Jhi. Pü.!    an  i  dräi   a/ar  rawisiiiA  isle pa  mänsr;,
14107:•  g.  *dragu-däyah- '>  Adj.  (auch  fem,) 'für  den,  die  Armen  sorgend':  apasca  va .  .  ag»nyä  (sd.)  'yaahB  (APf.)  vlspB.paitXs Y.38.  5.
14229:Pü.!  druit  rawiimh,  Sö.!  TÜpapr<^lH^.
14978:•  j.  paitt.parStay-  f.  'Erfragung,  Erkun- dung (durch  Fragen)"':  daidi  ahmsk»m.. vanaintimca  uparatätam .  .'tlmla  mahrahe spsntahe  Yt  lo.  33.
15838:•  j.  "parStay-  f.  '(gegenseitige)  Befragung, Disputation':  yS  .  .  gaot)ma?ie  (sd.)  parSyä HSit  avaiti  \t13.16.  LS.  'ta  als  Int sbes.
15857:airya  daiAhärö  Yt  Ä  58 ;  N.  6^7  (?) ;  —  caiti m  airoAe  'srö  *ui0>ra  barät  "Srie  viel  Z. soll  man  bei  einem  Opfeitiei  bringen?" N.  65;  —  ni}itpanis(a  (statt  IS.,  lies  pasvaT) . .  irista  (sd.)  . .  ratufris  N.  56;  — yi  'süm 'ata  finacUi  (sd.)  S.-iS;  —  Aasat^r^m aimmayanqm  /räviiruyät  (sd-)  FUpanqmät aBaiiqm  par.qm  ..   WlS.JO.  [N.  65:
16245:Pü.:  /ttr  rawisHih.  —   0  So  NA.  la  V.  rS.21, Pt  4  lu  Y.  6z.   \0.  —  >)  VgL  IQ  feuru-nttr-.
```


## [2026-09-06T23:01:47.616Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hragu%C5%A1",
 "prompt": "Give the Proto-Iranian reconstruction for 'swift/light', its PIE source and descendants including Avestan ragu-."
}
```


### [2026-09-06T23:01:49.865Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T23:01:58.804Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && head -3 aiw.txt; echo ...; grep -n \"ragu\\b\\|ragu-\\|rəvī\\|rǝvī\" aiw.txt | head -20",
 "description": "Check alternative Bartholomae OCR"
}
```


### [2026-09-06T23:01:58.861Z] TOOL RESULT

```
Google 


...
59689:•  g.  *dragu-däyah- '>  Adj.  (auch  fem,)
```


## [2026-09-06T23:02:04.677Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"schnell.*leicht\\|leicht.*schnell\\|rənjy\\|ranjy\\|ranjist\\|rgnjist\" BRT.txt | head -20",
 "description": "Grep Bartholomae for ragu gloss"
}
```


### [2026-09-06T23:02:04.727Z] TOOL RESULT

```
25445:•  j.  ranjiSta-  Adj.  (fem.  •/«-)  'der  sich am  leichtesten  bewegt,  der  flinkste';  /ra- vaiii  yazamaide  . .  rtvls  . .  °ia  Yt  JJ.  75 —  fravasayS .  .ya  .  .'tä  fravaamnanqm Yt  13.  26;  —  mtrrjohe  .  .  vän^nahe  . . yB  vayam  asH  äsiUs  HS  fravasimnanam
25447:•  j.  ranjyö  Adv.  'leichter,  fliDker*:  r* ^vazainte  (/?)'>  m^B  "flmker  fahren  sie dahin,  die  sich  an  dir  berauschen"  Y. 10. 19.
```


## [2026-09-06T23:02:10.338Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 25400,25450p BRT.txt",
 "description": "Print Bartholomae region around ragu"
}
```


### [2026-09-06T23:02:10.388Z] TOOL RESULT

```
d-Part  (S  309.  5)  aus  Praes.  7  (Int)  des  V. rak'^'t,  —  Pü.r  Aa  Aal  räsßk  rel,  erL:  kaS  vic!r i  ritt  afar  hinind  al  ri!  iavil.  —  ■] No.  I.
•  j.  r5r«äyant-  Adj.,  PPA.:^  s.  raA-  mit No.  I.
•  j.  räs-  V.,  nur  mit  ava  'hioabreichen, -gehen'.     Praes.  30  (Iter.)  rOsaya-,
räzan-  1516
yat  alsqm  *fndt/aya  (sd.)  . .  *v>r3syanlqm nSij  ava-aräsayS^  dhatri  Aar3%raiibyB  "dass sie  (die  GUrtelschnur)  ihnen  . .  nicht  über den  Rocksaum  hinabreiche"  N.6'5.
Et.?  avaar'  weist  auf  /r- 1),  —  Pfl.:  ka..ftl
afie  ränai  bavät.  —   0  Ein  Versuch  bei  Cld.
KZ.  33.  4Ö4-
•  j,  rasant-  Adj.  (fem.  'saintl-)  -  ?  - : ahm  'saintim  dar7yö.vär)%manfm  Y.52.  i ; —  vanuAif'a  a%ä  vanuhilca  asayS  .  . 'sainfT/  dary/B.värJ^manB  Y.  52.  3,
Ableit.  (raiifs/ät-).  —  PQ.:  *rai  tstimiA'),  Sü.: foArasfhiiah',  vgl.  zu  riaqs/üt',  —  1)  Hds.  rada statt  rdda.
•  p.  rasta-  Adj.  (fem.  Uä-)  '(bereit  ge- macht', vom  Weg  sva.)  gebahnt,  vorge- zeichnet'; fia^im  tyäm  °täm  mä  avarüd^ fsd.)  D.6.6.
PPfP.  lum  V.  rörf-i).  —  mp.,  np.  räsl  'recht' (worin  ir.  VJj/a-  und  *räiia-  lusunmengeitoasen sind).—  >)  Falsch  neueidingsFitMOLlBKWZKM. //.  304,  Salemann  GlrPb.  /.  298.
g.  räsH:  s.  rA-.
•  j.  räz-  V.  'gehen',  Praes.  a  rata-, 30  (Kaus.)  r.isaya-''>.  —  Int  räsayqn.
Kaus.  'gehen  lassen,  miltere':  s.  Inf. mit  z/r 'hin  und  her  gehen':  v»nr%rayn»m
.  .  yB  vXräsaiti  anian  rSsta  rasmana  ä!a
paraia  p»r»saite  Yt.  i4-  47-
np.  gUT-äsTdan*}  'einherstoliiren' ;  TgL  aoifc. siaagim  'Weg'  (»pet.  'Greniweg')»,  air.  iligc ■Strasse'J);  t.  dam  IF.  6.  307  und  %  ^.  — Npü.:  ki  ia  mänand pahlttiiän,  —  •)  Nur  im Inf.  —  ")  Mit  PraeT.,  vgL  vJ-rätaiä.  —  »  iBed. vgl.  gr.  o?/io(  usw.,   lat.  iter,  nhd.  gleit,  gang
j.   vi  rasa   N,  S4:    liei   väuräia;    1.  unter
•  g.  räzan- :  räsn-,  j.,  g.  räzar-,  j.  rataA- n.  i)  'Gebot,  Satzung,  Anordnung':  kat tei  °zarS  "was  ist  deine  (des  AA^  Satzung?" Y.J^ia'';  —  data  ..  'SStigiSS.)  voAb sahU  (sd.)  manaaAä  Y.  ^o.  6,  a)  im Gegensatz  zu  staoma-  (sd.)  "vom  Ritus gebotene,  vorgeschriebene  Handlung,  reli- giöser Brauch':  staemaca  'zar>ca  (AP.) barsntu  da^uJS  aAurai  matdai  .  .  "die rituellen  Gesänge  und  Bräuche  .  ."  Yt. 17.157.  3)  'festgesetzte  Gebühr,  Ent- lohnung (im  Jenseits)':  sraidyai  (sd.)  matda fravaecä  ya  vidayat  asi/  •htam  "tu  kund . .  was  von  Gebühren  A.  verteilen  wird" Y.,j^.ia«.
KompE.  —  Zum  ai.  V.  rä/'aä,  —  Vgl.  ifrfti- rät;  —  aL  VgL  räjäni  RV.  «x  49.  4.  —  PO, : Vü-AÜH,  äramn;  I.  oOch  No.   1,  3>  —  ■)  Pü.
dby  Google
r^yant-
1528
CiL  :  kör  u  dätai/än  t  ti  kaiär  /  —  >)  Pn. :  lässt die  Worte  ans.
•  j.  räzayan  Inf.'»  'gehen,  ergehen  zu  lassen, emittere':  hmyaogsi  vaü  r"  "so  (soll)  er mit  lauter  Stimme  den  Ruf  ergehen  lassen' V.Äioo.
Zum  Praes.  30  (Kans.)  des  V.  rät- ;  g  s«.  t  c
—  Pü.:  /a  buland  rasiSttiA  göoiistt  e  äraiet.  — >)  Im  SiDD  der  sSKonj.
•  j.,  g,  räzar-  n.:  s.  unter  räxan-.
•  \.  räsah-  n.:  s.  unter  räxan-. KompE.
•  g.  raäayetähe  Inf.  'zu  schädigen',  insbcs. in  eschatologischem  Sinn,  'den  Schaden zu  schaffen"',  mit  Akt.:  yam  xsnBfym ränSibyä  (sd.)  da  ..f  ärigvanlim  savayS afavaram  "welche  Belohnung  . .  (nämlich) den  Schaden  fiir  den  ZJrxfjgenossen,  den Nutzen  fiir  den  ^Äanhänger" ''  V.j/.  9; —  ohne  Obj.:  atcä  ahmäi  vannsi  .  . nidsum  asim  sBiäyät /iaesai  {sd.)  r'  drvxl
Zum  Praes.  30  des  V.  ra?-.  —  Pü. :  rrienetii^), Sü.  (zu  V.  5/):  chtdayel  dutgalimatäm  lädkam hayäl  punyälmanäm.  —  'i  VgL  rai-  a.  — >)  Darin  besteht  eben  die  BeloUnang;  die Infinitive  all  Objekt.
•  j.  räÖta-  Adj.,  PPfP.:  s.  ras-.  a)  ASn. •ttm  als  Adv.  'in  gerader  Richtung,  ge- rades Wegs':  r°  ahmäi  naire ..  tniisrU  maE- haium  (sd.)  äcaraiti  Yt.  so.  1 37 ;  F.  ly.
lat  rtdus.  —  VgL  tasSa-.  —  S.  auch  vx  räsla-,
—  Pü. ;  raiitlai.
•  j.  riStara.va}-3nti-  m.  EN.  eines  Gläu- bigen'*; avarfiraiavÄff  '-/mtsU*'  asacnö "des  A.,  Sohns  des  R.  . ."  Yt  13.  loö.
Aus  der  Fügung  'räilar>  (VS.)  vaiinlSÜ  'Ge- bieter, Leiter  dei  Festet'  hervorgegangen; vgl.  avartgav:  'rastar-  m-,  »om  ai.  V.  räjali ; vgl.  ai.  räffrd-  n.;  *vayjntT-{.  (iBild.  s.  Bthl, IF.  r.  300),  lu  ai.  väghät'i)  m.,  Ut.  vmei.  — 1)  Nicht  Titel,  vfic  West  SBE.  4/.  87  wilL  — »)  Nach  der  ^-Deklination.  —  »  Gdn.  VSt.  2. S4  'Priester',  MMüllek-Oldenberg  SBE.  ja. 46:  'suppliant,  worabipper,  iavoking,  sacri- ficer".
•  j.  räätem  Adv.:  s.  rästa-.
g.  räSnqm  Y.  J4,  la:  ».  räcait:
•  j.  'räna-  n.  'Treffen,  Kampf,  Streit', Plur.:  «äV  si  aAmi  paiti  nairi  dva  *mainyu •na  ava.stät9hat  'Svegen  dieses  Manns werden  die  zwei  Geister  nicht  in  Kampf (mit  einander)  eintreten"  V.  7. 52.
KompE.  —  aL  rina-  m.,  n.  'Kampf').  — VgL  hamanum-,  haviirii^a;  räna-,  —  Pü.: faliär;  .  daiu  die  ErL:  iul  aAramatt  iangik*)
afar  ne  *daket  'd.  h.  AJiraraan  wird  ihm  keine Not  bereite»'.  VgL  auch  PüEtL  zu  Y.  47. 6  d : akranän  räi  lü  patkär  'der  Gläitbigea  wegen ist  kein  Streit'.  —  ')  Von  räna-  in.  'Lust' etjrmologisch  verschieden,  entgegen  Jubti PrJ.  88.  239.  —  =)  Oder  upäh  (DsT.)f
•  j,  Väna-  Adj.  "wild  (,  nicht  domestidrt)', von  Tieren":    bQ^ahe   k>hrpa    'nahe   Yt
14-2$.
Aus  ar.  *rana..  %  3^3.  I  (,  8).  —  ü.  vgL  ärana- Adj.  'nicht  heimisch'.  —  Npü. :  fitäx  tan,  erl. : ba  latt  i  guiäda.  —  »  Vgl.  Yt  74.  33.
•  j.  ranjiSta-  Adj.  (fem.  •/«-)  'der  sich am  leichtesten  bewegt,  der  flinkste';  /ra- vaiii  yazamaide  . .  rtvls  . .  °ia  Yt  JJ.  75 —  fravasayS .  .ya  .  .'tä  fravaamnanqm Yt  13.  26;  —  mtrrjohe  .  .  vän^nahe  . . yB  vayam  asH  äsiUs  HS  fravasimnanam
Superl.  zu  ra-jeni:  —  ai.  vgL  lighi}tha-  Adj.  — Npu.j  fehlt.
•  j.  ranjyö  Adv.  'leichter,  fliDker*:  r* ^vazainte  (/?)'>  m^B  "flmker  fahren  sie dahin,  die  sich  an  dir  berauschen"  Y. 10. 19.
ASn.  aas  *r>njyah'  Adj.,  Kompar.  in  rajoB-. —  VgL  aj.  rä;hiyai;  laghiyat-  Adj.;  li>w. ranjk  'leicht'  (Gewicht),  tlink*  (Ross).  —  Pä.r ii^i.  —  >)  Fehlt  wegcD  des  vonasgehendea •//;  vgl.  vorher.
•  g.  r»ma-  m.  'Grausamkeit',  insbes.  gegen- über dem  Rind :  nl  aisfinB  nl  äyätam  paiH -mptn  pain  *sy5düm  (sd.)  Y.  4&.  t,  — a  ma  (näml.  das  Rind)  adtmS  haxasia •mB'^  ähisSyä  (sd.)  darjicä  bvüca  (sd.) Y.  29. 1.
Et?*)  —  VgL  räma-,  mit  dem  et  luiammes- gehÖrL  —  Pü.  (lu  Y.  48):  arali  'Neid'  - Sü.:  ö-fyalumanusyah-ili.'a  Y.  ig): relaiÖH,  erL; kum  apalmätt  iuitan  am  ähökeiül,  aber  Sü. ; trfyäbth.  —  ■)  Ist  hier  nach  Ausweis  des MetniDiE  eine  in  den  Text  geratene  Glosse.  — a)  VgL  Gdn.  KZ.  30.  531. j.  rivT':  s.  unter  ratav.
```


## [2026-09-06T23:02:17.228Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ragav\\|raga%\\|ragu\" BRT.txt | head -20",
 "description": "Grep Bartholomae for ragav"
}
```


### [2026-09-06T23:02:17.273Z] TOOL RESULT

```
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
7038:satz'so,  dann;  da.' -.yezi ('wenn') aAipaurva.- naem3l  3'  mqm  avi.rimilnaya  (sd.)  Yt.16. 2;  a.  3-3,  Y.2.43,  ^'.36,  103,  /ö'.ii,Nik. 3,  Vd.  13';  —  yat  ('wenn')  yave  dayat ä'  datva  y^ism  (sd.)  V.J. 32;  321,  H.  2". 13,  N.  IJ2;  —  3at  (s.  8)  yat  apö  uzbargnte .  .  a°  fraiasinti  . .  fravasayö  Yt.  13.65; V.  Ä40,  i7.4;  —  yat  ("als')  mqm  tura pazdayatita  .  .  3'  az3m  tanüm  aguze  .  . \3at  (s.  3)  mqm  fraguzayanta  ..Yt  i7.  55^'; — yas}  tat  nmäfum  äk^rstmn  .  .  «7°  mqm tnairyö  akasat  dai  (s.  2)  .  .  fräksrmaot V.  22.  i£;  —  3at  (s.  8)  yat  miirtm  .  . /radaöqm   .  .   a°  dim  danqm  ,  .  Yt.  10.  i ;
7265:13,  N.  Ö2;  —  äat  (s.  8)  yat  äpd  udiannte .  .  ä'  fralasinH  .  .  fravalayS  Yt  JJ.  65; V,  ^,40,  ^7.4;  —  yat  ('als')  mqm  Iura pazdayaiita  . .  ä°  azsm  tanüm  aguze  . . äat  (s.  3)  mamfraguzayanta  ..  Yt  i;.  553'; — yas)  Uli  mnärom  äktrirum  .  .  ü°  mam mairyd  äkasat  äat  (s.  2)  .  .  fräkirmaot V.  22.  if;    —    äat  (s.  8)  yat  mi>r)m   .  .
8641:•Z)m  utäiSta  (sd.)  V. /5.3  s  f. Zum  V.  datz..  —  ai,  vgl.  uddriikä-  f.  'Ter- mite'. —  Pü,i  uidakisi.  —  ')  Ao  V.  3.  9  an- geglichen, statt  Tfldaeia  'durch  Erdabi  ragung'. —  '1  ^g.  'welche  durch  Erdauficbüttang  auf- geschüttet werden';  s.  zAusdr.  yr-ii^ii-  No.  1.
9008:24  genannten  Bergs,  anj^ebl.  idiidräsfi,  den man  für  idenlkch  hielt,  s.  vunStackelber<i WZKM.  12.  239. •  j.,  g.  ka'iH  Adv.  1)  "wie?,  in  welcher Weise':  "^il  '>,wä  mazda  xlnaoiiii  {%A^  V. 4O.  1;  —  °^ff  zaoia  gidh  /rasrävayätti N'.W;  Vyt.j/C?);  —  -^d  ffjv7w»»  ^/-a.- iri^j-S  Oa  ..  ii/aJasJ  "wie  ists  geschehen, dass  du  . .  gestorben,  wie  dass  du  .  ." K.  2.  16;  16;  —  °ä(7'>  ajfiirS  daxsära fiiasaysi  dlsil  "durch  welches  Zeichen "' willst  du  die  Tage  kund  machen  für  dte Befragung?"  Y,4j.  7".  a)  als  Indefini- tum,  a)  mit  vorausg.  ja^a  und  folg.  ca  "wie, in  welcher  Weise  auch  immer':  hvqm  anu usiim  zaos?mca  yaiia  "iiaca  hs  zaosö  "nach seinem  Willen  und  Gefallen,  wie  immer sein  Gefallen  war"  V.2. 11;  Yt/fj.82,  N. _J7.  b)  mit  Neg.  und  folg.  cina  'nicht irgendwie':  *'mä',a  ^'i^aäna  paitt.Jime  (.sä.) Vr.22.3.  2)  'wie  so?,  was  ist,  heissi das?,  was  hat  man  darunter  zu  verstehen? (die  Antwort  wird  mit  ya'^a  eingeleitet) °>a  alvö.gäimi  ra>a  '^ripai^m  "'wie  so eine  Schrittlänge?'    'Drei  Fuss'."   V.  5. 8;
9063:mit  7'i  'durch  Graben  beseitigen,  ab- tragen; zerstören':  yasca  .  .  daxmatiqm avavanhm  maz3  vtkanayät  ya>a  .  .  V.  7. 51 ; — yat  b.J  paiti  fra!st.>m  daxma  uzdaSza (sd.;  lies  vrd')  vJkanü  (3SPA.)  yahmya  . . "an  welchem  Ort  man  am  meisten  die  D. durch  Abtragung  zerstört,  wo  .  ."  V.  y. 13;  —  yat  bü  paiti  fraüittnt  vikmte (3SPM.)  .  .gjmam  V..J.Z2;  —Wäyadanä (sd.)  tyä  gauiii'ätJ'  . .  viyakai'  (3SPrA.) Bh. /.  14;  —  kyt^  aparam  imilm  dipim vaitnhy  ..  maty^  (sd.)  vikanähy^^  Bh. 4.  15;  16;— _jW;>  imrim  dipim  ..vainähy '.■ikanähidisi^  Bh.  4- 1 7  II  ■
9875:mit^a  'aus  dem  Versteck  hervorholen': äai  mam  fraguzayanta  . .  "da  holten  mich aus  dem  Versteck  . ."  Yt. /".  55.
14107:•  g.  *dragu-däyah- '>  Adj.  (auch  fem,) 'für  den,  die  Armen  sorgend':  apasca  va .  .  ag»nyä  (sd.)  'yaahB  (APf.)  vlspB.paitXs Y.38.  5.
14978:•  j.  paitt.parStay-  f.  'Erfragung,  Erkun- dung (durch  Fragen)"':  daidi  ahmsk»m.. vanaintimca  uparatätam .  .'tlmla  mahrahe spsntahe  Yt  lo.  33.
15838:•  j.  "parStay-  f.  '(gegenseitige)  Befragung, Disputation':  yS  .  .  gaot)ma?ie  (sd.)  parSyä HSit  avaiti  \t13.16.  LS.  'ta  als  Int sbes.
17908:•  g.  fsrasä-,  fr°  f.  i)  'Frage':  ahya  'ssm (AS.):  iahmäi  vXviduye{%A.)  va^i  ai  a.. mtam(sA.)  "auf  seine  Frage:  "Wofür  .  .? 'Bei ..'"  V.43-  9''-  2)  'Fragen,  Befragung Über-'  (auf  mit  LoL):  ia^5  (sd.)  ayärS ..'sayäi  lifsä  aibJ  %iWäka ga/knAa  lanusica
17909:■  "..  für  die  Befragung  über  das  Deine  und dich  selbst?"  Y.  43.  7  ">,  3)  'Sichbcraten- lassen  von  — '  (Gen.):  y5i  asru/ßt/ (sd.) pgnnäafß  nl^il  aiahya  advvyeintl  (sd) *hatSna  nSi£  'saya  (IS.p'  vaahSus  cSxnarS mananhs  "die . .  nicht . .  noch  darum  Sorge tragen,  sich  von  VM.  beraten  zu  lassen" Y.  44. 13"-
20912:Nominativ  oder  dem  ihm  gleichen  Akku-' 12; —  Hat  mqm  fraguzayanta  ysi  i
21651:■ber   <'  uich  uf  Lbertragung   bemhen.    -    *mainy3iü matdä  'paounilm  ipmtokyä  aiä
22443:Eig,  'weben',  mit  Übertragung  auf  die  künal- liche  Fügung  der  Worte  (s,  ai,  väyali);  »gl, va/mi-.  —  Vgl.  np.  iJ/ad  'er  webt'.  —  Pü. (dRn.):  ^^eitnisnO,  eil :  pa  ^ii  därisit  und  ö x'i!  iuniin;  j^m  D  iülaa,  erl. ;  fa  s^esiA  ittälan; x'isenTia« ').  —  ')  an  d  da'  ist  doch  wohl  alter Fehler  für  anddda',  d.i.  AandÜ',  s.  np.  an- disldan;  vgl,  DsT,  ZA.  /.  147.  der  sich  lu Unrecht  durch  das  Ideogramm  für  ^U  be- irren lasst;  s.  seine  eignen  Bemerkungen ZA.  2.  120  No.  13;  ferner  IF,  //.  144  und sonst.  Falsch  Mills  G.  397,  514,  ZDMG, 52-  439-
29132:♦)  Der  M^ra  (sd.)  lerfillt  in  iwei  Teile,  den eigentlichen  M.,  den  AHM.  spontan  ofTenbart hat,  and  den  H.,  der  auE  besondere  Befragung mitgeteilt  oder  von  Sehern  erschaut  worden  ist, daher  letzlerer  die  Bezeichnungen  taini.parila- 'vom  Kundigen  (d.  i.  Zarii%Hllra)  erfragt'  und upaiti.^lubyd  gtripta-  'von  den  Sehern  wahr- genommen' führL  Vgl.  ha^a.däla-  und  West SBE.  J/.  4  (lu  mp.  hätakmänsrlk),    Gdn.  GIrPh.
```


## [2026-09-06T23:02:28.064Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%DB%8C%D9%87",
 "prompt": "Is there a Persian entry for لایه? Also report anything on Persian کارناوال if linked. Mainly: does Wiktionary list Persian کارناوال as a borrowing from French carnaval?"
}
```


## [2026-09-06T23:02:29.212Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/laya",
 "prompt": "Give the Sanskrit entry लय (laya): meanings ('adherence, clinging, dissolution, rest'), and its etymology — from the root ली (lī) 'to cling, adhere, dissolve'."
}
```


### [2026-09-06T23:02:32.656Z] TOOL RESULT

```
# Response

Yes, there is a Persian entry for **لایه** on Wiktionary. According to the page, it is a noun meaning "layer" (and obsoletely, "adhesive mud; sediment"). The pronunciation varies by dialect: "lāya" in Classical/Dari Persian, "lâye" in Iranian Persian, and "loya" in Tajik.

Regarding **کارناوال**: The provided content does not include any information about this Persian word or whether Wiktionary documents it as a French borrowing. I cannot address that part of your question based on the material supplied.
```


### [2026-09-06T23:02:35.693Z] TOOL RESULT

```
# Sanskrit Entry: लय (laya)

## Meanings

Based on the Wiktionary content provided, the Sanskrit word लय (laya) carries these primary senses:

1. **"dwelling, house, residence"** — referenced in the Old Javanese section as borrowed from Sanskrit
2. **"destruction"** — listed among meanings including "extinction, dissolution, destruction, death, calamity, misfortune, defeat"

## Etymology

The document indicates that लय (laya) derives from Sanskrit roots, though the specific root ली (lī) meaning "to cling, adhere, dissolve" is not explicitly detailed in this Wiktionary entry. The entry confirms the word's Sanskrit origin but doesn't provide the detailed etymological breakdown you've requested.

The entry demonstrates the word's widespread influence across multiple languages, inherited through Proto-Malayo-Polynesian and other language families, suggesting an ancient and significant term in Indo-Aryan linguistic history.
```


## [2026-09-06T23:02:42.980Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT carnival ===\"; grep -n -A3 \"^Carnival\\|Carnival,\" SKT.txt | head -20; echo \"=== SKT slime ===\"; grep -n -A3 \"^Slime\" SKT.txt | head -12; echo \"=== SKT light adj ===\"; grep -n -A4 \"Light (2)\\|^Light (2)\" SKT.txt | head -14",
 "description": "Grep Skeat"
}
```


### [2026-09-06T23:02:43.067Z] TOOL RESULT

```
=== SKT carnival ===
=== SKT slime ===
=== SKT light adj ===
```


## [2026-09-06T23:02:46.659Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in SKT.txt KLN_1966.txt KLN_1971.txt; do echo \"=== $f carnival ===\"; grep -n -i \"carnival\" $f | head -4; echo \"=== $f slime ===\"; grep -n -i \"slime, sb\\|slime,\\|OE\\. slim\\|slim, \" $f | head -4; done",
 "description": "Grep Klein and Skeat for carnival/slime"
}
```


### [2026-09-06T23:02:48.329Z] TOOL RESULT

```
=== SKT.txt carnival ===
3023:carnivaL  (F.-Iial.-L.)  F.  eama- vol,  Shrovetide.  —  Ilal.  camevaU,  earnavaJi, the  last  three  dnys  l>cforr  I^nt  —Low.  L. carrultrvale,  earmlcvamtn,  removal  ol  flt-nh, fjhrovctidc.  —  L.rflrfftf-m,  aoc  of  cofv,  HcsU; and  ieuare,  to  lif^,  remove,  take  away; from  Intij,  light.
23451:Frtfukfrom  Italian  from  IjUim:  alarm {•.lanim),  alert,  apaitnunt,  arcade,  artii>an, nbum,  battalion,  bulletin,  cab  (i),  cabbage ;!>,  cape  (i),  capriole,  carnival,  cascade, ftfique.  cassock,  cavalcade,  cavalier,  cavalry, Hadel,  colonel,  colonnade,  compliment, DiDpoat,  concert,  concordat,  corporal  (,1), inridor,  cortege,  costume,  countertenor, ttiraos.  douclie.  ducal.  e>cort,  esplanade, icade.  florin,  fracas,  fugue, gabion,  gambol, Viproviae,  incatoadiiie,  infantry,  lavender, Itestring,  macaroon  ?,  manage,  manege, ben.  mizcn,  (.mizzcn),  modeU  motet, msket,  niche,  ortolan,  paladi'i,  palette, ftUet  (3),  parapet,  partisan  \\)t  pastel, rruke,  pilaster,  piniiacc,  piston,  pomade ^mmoile),  pontoon,  ix>puUce,  porcelain, D&lillion.  preconcert,  rtpnsal,  revolt,  rocket 1),  aalad,  sallct,  salmagundi,  saveloy  (ccr* pifts),  scamper,  Bentinel?,  sentry  1,  somer- lult    (Somerset),    sonnet,    spinet,    squad.
=== SKT.txt slime ===
11915:Moslem,  a  Mussulman.  (Arab.)  Arab. moslim,  *a  mnsulmao,  a  true  believer  in the  Mohammedan  faith ; '  Richardson.  Cf. Arab.  mtualUm,  oat  who  aoqniesces.  A mussuiman  is  one  who  professes  ii/dm, i.  e.  submission  to  the  will  of  God  and  to the  orthodox  faith. —  Arab,  sa/ama,  to  sub- mit %  The  E.  words  mosUm,  mussuiman, islam,  and  talaam  are  all  from  the  &ame Arab,  root  satama,  to  submit.
17502:Slim.  (Du.)  Orig.  sense  *slepl thaice  weak,  poor,thiu,  bad,  slight;  p^ slim,  crafty.  — O.  Du.  slim,  ■*'>.  end Dan.  Swed.  slem,  worthless :  IcxL  ti vile;  G.  schlimm,  bad,  cunning.  Cf. E.  slam,  the  slope  of  a  hill,  tall  and Prob.  from  the  same  root  aa  si^, slender.
17510:>t  pp.  i&/«i.+Da,  jlifjKft,  Icel.  tUppa^ i,  tiippa,  G.  s<hluftnt  all  weak  verbs ; 0  Icel.  iUppii  (pt.  t.  iUipp\  Dan.  j/f>/V. trong  verbt ;  nl&o  Goth,  siiupan,  pt.  t, 'A  PP-  ^^«A""'  *o  s^ip  °^  creep  into, uom  ^SARP.  to  gliue;  sec  Serpent. ^ipp^r,  A  loo«L*  shoe  ruily  slipped 'r-Xt  from  A.  S.  //i/or,  slipiicry, \td  -y.  Aj»d  fccc  ticevf. ;>(0.  »  puddle.  (E.)  M.E.  iUpp€, .  —  A.  o.  tloppt^  slyppt,  the  iloppy ippiog*  of  a  cow,  as  in  cA-shppc  (cow- »}  ;  iTfto  A,  S.  slyptt  a  W^cid  substAJice. ,  sense  'a  ilipoery  place;'  cf.  Icel. [^liroy  ofTal  of  tish,  siepja,  slime,  Irish zniic.  t>c«  further  below. V  (')>  ■  loo&e  garment  (Scand.) ihppt.  •  Iccl.  slffppr,  a  slop,  lone gown. « Icel.  slupp-.  stem  of  pt.  t.  pH a,  to  slip.  So  named  from  its  trailing ground.  So  also  Dan.  ihib^  a  train, v^ahi^  to  trail;  G.  jchleppe,  train, I.  to  trait  Conopve  Sloeve, rdpo,  an  incline.  (^)  M.  £.  tlopa ■tiepf,  on  the  slope,  ready  to  sHp.»A.  S. Up,  pL  t.  of  slipan^  to  slip.  Cf.  prov,  E. b/r,  slippenr,  from  Icel.  sUipr.  slippery, •loveii.  (I)(j )  O.Dii.//(j/;j/iv/;aKlovcn, ilh  M.  E  iiiftix  -OH  (.  *  K.  -rtr/i.  I„  -ojrttj) ; )u.  iUj,  caiclcsb;  x/t*/^  sb.,  neglect,  an  old Upper.  The  ba^c  is  Low  G.  slup-,  u  seen I  Lioth.  ilt/p~am,  pp.  of  iliupan,  to  slip. If.  Iriah  slapach,  slovenly. BUt  rE.)  M.  E.  iiitten,  weak  verb  j Din  s/i/tn.  strong  verb.  »  A.  S  sUtafi,  to lil»  rend ;  pt.  t.  sttit,  pp.  tliten.  +  Iccl. B|||L  Swed.  //ifa,  Don.  x/r^/,  to  rend  ;  Du. ^^BC  to  wear  out :  O.  H.  G.  sHsan,  G. Wmaet,  to  slit,  uhiiitfttt  to  alice.  Cf. Itt.  nuik^  lo  injure.
23536:wer,  ruffle,  selvage  (selvedge),  sheer  (j), (a)  (scate),  skipper,  slim,  iloop,  sloven,
=== KLN_1966.txt carnival ===
6570:carnival,  n.  —  F.  carnaval,  fr.  It.  carnevale,  fr. ML.  came,  vale,  ‘O  flesh,  farewell1.’.  See  carnal and  vale,  interj.
41005:vale,  n.,  valley.  —  ME.,  fr.  OF.  (=  F.)  val,  ‘val¬ ley’,  fr.  L.  valles,  later  vallis  (for  *wal-nis), which,  together  with  vallum  (for  *wal-nom), ‘wall’,  prob.  derives  fr.  I.-E.  base  *wal-,  *wel-, ‘to  turn,  bend,  twist,  roll’.  See  volute  and  cp. vail,  ‘to  lower’,  valley,  vallum,  vaudeville,  venda- val,  avale,  Convallaria.  Cp.  also  2nd  helo-. vale,  interj.  and  n.,  farewell.  —  L.  vale,  sing, imper.  of  valere,  ‘to  be  strong,  be  well’.  See valiant  and  cp.  the  first  element  in  next  word  and the  second  element  in  carnival, valediction,  n.,  farewell.  —  Fr.  L.  valedict-(um), pp.  stem  of  valedicere,  ‘to  say  farewell’,  which  is compounded  of  valere,  ‘to  be  strong,  be  well’, and  dicere,  pp.  dictus,  ‘to  say,  tell’.  See  valiant and  diction  and  cp.  prec.  word, valedictory,  adj.,  saying  farewell.  —  Formed with  adj.  suff.  -ory  fr.  L.  valedict-(um),  pp.  stem of  valedicere.  See  prec.  word.
=== KLN_1966.txt slime ===
5163:blenheim  spaniel.  —  See  prec.  word;  so  called because  originally  bred  at  Blenheim. blenno-,  before  a  vowel  blenn-,  combining  form meaning  ‘mucus’.  —  Fr.  Gk.  JJXevvo c,  or  fiXivva, ‘slime,  mucus’,  of  uncertain  etymology;  (IXevvop possibly  stands  for  *piXs8-a-voi;,  and  is  rel.  to lisXSetv,  ‘to  melt’,  and  cogn.  with  L.  mollis  (for *moldwis),‘ soft’.  See  mollify  and  cp.  words  there referred  to.  Cp.  also  blenny. blennorrhea,  blennorrhoea,  n.,  excessive  discharge of  mucus  ( med .)  —  Medical  L.,  compounded  of blenno-  and  -rrhea.
7867:yXoia,  ‘glue’,  yXotoc;,  ‘anything  sticky’,  yXtvr;, of  s.m.,  OSlav.  glenii,  ‘slime,  mucus’,  glina, ‘clay’,  Russ,  glej,  ‘clay’,  Lett,  glive,  ‘slime,  mu¬ cus’,  OIr.  glenim,  ‘I  cleave,  adhere’.  Cp.  clam, ‘to  smear’,  clammy,  cleave,  ‘to  stick,’  clever, clevis,  cliff,  climb,  clote.  Cp.  also  glioma,  and the  second  element  in  neuroglia.  For  derivatives of  I.-E.  *gleit-,  a  -/-enlargement  of  base  *glei-, see  glue.  Derivatives:  day,  tr.  v.,  clay-ey,  adj. claymore,  n.,  a  large  double-edged  sword  former¬ ly  used  by  the  Scottish  Highlanders.  —  Gael. claidheam  mor,  lit.  ‘a  big  sword,  fr.  claidheamh, ‘sword’,  and  mor,  ‘great’.  The  first  word  is rel.  to  W.  cleddyf,  OIr.  claideb,  and  cogn.  with Gk.  xXaSos,  ‘young  branch  or  shoot’,  L.  clddes, ‘disaster’,  fr.  I.-E.  *qelad-,  a  -d-cn'argcment  of base  *qeld-,  *qola-,  ‘to  strike,  beat,  break’.  See holt  and  cp.  dado-.  Gael,  mor,  ‘great’,  is  rel.  to W.  mawr,  ‘great’,  and  cogn.  with  OE.  mire, OHG.  mari,  ‘famous’.  See  more.
11242:Dialister,  n.,  a  genus  of  parasitic  bacteria  (bac¬ terial.)  —  ModL.,  formed  fr.  dia-  and  Gk.  fjXia- TTjp,  ‘filter’,  which  is  rel.  to  SXf),  ‘slime,  mud’, and  cogn.  with  OI.  surah,  ‘intoxicating  drink’, sura,  ‘brandy’,  Lith.  sula,  Lett,  sula,  ‘sap’, OPruss.  sulo,  ‘curdled  milk’,  OHG.  sullen, MHG.  siiln,  G.  suhlen,  OE.  syljan,  sylian,  ‘to make  muddy  or  dirty’.  All  these  words  derive fr.  I.-E.  base  *su-l-,  enlargement  of  base  *seu-, ‘to  rain;  sap’,  whence  Gk.  Seiv,  ‘to  rain’,  Sex 8;, ‘rain’.  See  hyeto-.
14433:‘the  pine  tree’,  nfcov,  ‘fat,  wealthy’,  map,  ‘fat, tallow’,  mixeXr),  ‘fat’,  Trtacra  (for  *irixia),  ‘pitch’, L.  pinguis,  ‘fat’,  pituita,  ‘slime,  phlegm,  viscous moisture’,  L.  pix,  ‘pitch’,  opimus,  ‘fat,  fertile, rich’,  which  also  derive  from  enlargements  of base  *poi-,  *pt-.  Cp.  pay,  ‘to  coat  with  pitch’, pimelosis,  pinguid,  pip,  pitch,  ‘a  resinous  sub¬ stance’,  pituitary  and  the  second  element  in propionic.  Cp.  also  pine,  the  tree,  and  words there  referred  to.
=== KLN_1971.txt carnival ===
40015:carnival, n. — F. carnaval, fr. It. carnevale, fr. 
40019:Derivative: carnival(l)-er, n. 
258761:the second element in carnival, 
=== KLN_1971.txt slime ===
30697:‘slime, mucus’, of uncertain etymology; [}X£wo<; 
48439:of s.m., OSIav. glenu, ‘slime, mucus’, glina, 
48440:‘clay’, Russ, glej, ‘clay’, Lett, glive, ‘slime, mu- 
70287:T7jp, ‘filter’, which is rel. to uXir], ‘slime, mud’,
```


## [2026-09-06T23:02:56.530Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN light adj ===\"; grep -n -A6 \"^light, adj\" KLN_1971.txt | head -20; echo; echo \"=== KLN slime ===\"; grep -n -A5 \"^slime, n\" KLN_1971.txt | head -14; echo; echo \"=== KLN leaven ===\"; grep -n -A5 \"^leaven, n\" KLN_1971.txt | head -12",
 "description": "Grep Klein 1971 headwords"
}
```


### [2026-09-06T23:02:56.613Z] TOOL RESULT

```
=== KLN light adj ===
137590:light, adj., not dark, bright. — ME. liht, light, fr. 
137591-OE. leoht, rel. to OS., OHG. Iioht, OFris. liacht, 
137592-MHG. lieht , G. licht , ‘bright’, and to OE. leoht, 
137593-‘light’ (n.). See light, ‘brightness’. 
137594-
137595-Derivatives: light-ish, adj., light-ly , adv., light- 
137596-ness y n. 
--
137598:light, adj., not heavy. — ME. liht , light, fr. OE. 
137599-leoht , liht, rel, to OS. liht-, ON. lettr, Dan. let , 
137600-Swed. Idtt. OFris., MLG., MDu., Du. licht , 
137601-OHG. liht i, liht, MHG. lihtejiht, G. leicht, Goth. 
137602-leihts, ‘light’, fr. I.-E. base *le(n)g w h-, ‘light, 
137603-easy, agile, nimble’, whence also L. levis , ‘light’. 
137604-See lever and cp. words there referred to. Cp. 

=== KLN slime ===
224085:slime, n. — ME. slim, fr. OE. slim, which is rel. 
224086-to ON. slim , Dan. slim, Du. slijm, MHG. slim , 
224087-G. Schleim, ‘slime’, OHG. slimen , ‘to make 
224088-smooth’, fr. I.-E. base *(s)lei-, ‘slime, slimy, 
224089-sticky, dauby, slippery’, whence also Russ. 
224090-slimak, ‘snail’ (lit. ‘the slimy animal’), OSlav. 

=== KLN leaven ===
135488:leaven, n. — ME. levain, l e vain, fr, F. levain, fr. 
135489-VL. *levdmen, ‘something that raises’ (classical 
135490-L. levamen , means ‘alleviation, mitigation’), fr. 
135491-levdre, ‘to lift, raise; to lighten, alleviate, miti- 
135492-gate’, fr. levis, ‘light’. See level and cp. relieve. 
135493-Derivatives: leaven , tr. v., leaven-ing , n.
```


## [2026-09-06T23:03:04.073Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT levis ===\"; grep -n -B2 -A8 \"levis, -e\" LAT.txt | head -30; echo; echo \"=== LAT limus ===\"; grep -n -A8 \"^limus\\|limus, -i\" LAT.txt | head -20",
 "description": "Grep Ernout-Meillet"
}
```


### [2026-09-06T23:03:04.141Z] TOOL RESULT

```
=== LAT levis ===

=== LAT limus ===
34012:limus, -I m.(linum n., Varr.Grom.): limon, boue, vase. - Depuis
34013-Plaute. Panroman, M.L.505O.
34014-Derivds et composes: limosus, M.L.5054; illimis: sans vase, linpide
34015-(Ov.; cf. gr. o. 7 t:t|Xo£), i l limatus (Coi.); oblino,-as: couvrir de fange;
34016-llni-genus,-cola (Aus.).
34017-Cf. v.isl.s I in, v.h.a.sZt* "boue", et sans doute gr.Xeipnw "prairie
34018-huaide", Xetp,a^ (meae sens), Xl,|iVT] "narais".
34019:limus, -a, -um ( limus semble la forme ancienne; linis dans Amm.
34020-Mare. «0,9,8, provient peut-etre de ce que linis a dtd pris pour un
34021-nom. dans une expression comme linis [scii.ocwlis] aspicere): oblique.
34022-Attestd depuis Plaute. Se dit uniquement de 1 'oeil. et du regard, cf.
34023-Varr., Men.360 ap.Non.133,89, neque post respiciens, neque ante pro¬
34024-spiciens, sed limus intra limites culinae . Substantive dans limus
34025-et limum, cf.Tiro ap.Geli. 18 , 3 , 3 , licio transuerso quod limum appellatur
34026-cincti erant; Vg.Ae.13,130 et Serv. ad 1 . Derive: limulus.
34027-Rapprochement incertain avec limen, limes, sublimis. Aucune dty-
```


## [2026-09-06T23:03:08.994Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A10 \"^lino,\\|lino, -is\\|lino,-is\" LAT.txt | head -25; echo \"=== leuis ===\"; grep -n \"leuis, -e\\|^leuis\" LAT.txt | head -5",
 "description": "Grep Ernout-Meillet for lino and leuis"
}
```


### [2026-09-06T23:03:09.061Z] TOOL RESULT

```
34110:lino, -is, leul (et liul forme secondaire creAe d'apros le type
34111-s ino/s iui), litum, linere (atteste depuis Naevius); et Unio, -is,
34112-llnlul, -Itum, -Ire ( 4 poq. imp^r., Coi. Pali. Plin.Vitr., d'aprbs poli&t):
34113-enduire. - Terme technique, ainsi que les composes; a peine repr 4 sente
34114-en roman, M.L.50C3.
34115-A lino se rattachent: litus,-us m.(Plin.); litura: enduit, d'ou
34116-"rature, correction" et "taebe"; litUrdrius : qui a des ratures; li¬
34117-turo, -Ss (tardif).
34118-De linio derivent: linimen, linimentum, linitus,-us: liniment,
34119-enduit; linitor : XP 1 ' 0 ' 1 ’ 1 '!^ de linio,-as, linidtura, xP^^tC» Gloss.
34120-Philox.
=== leuis ===
33361:leuis, -e: leger (sens physique et moral), oppose i grauis, e.g.
33419:leuis, -e : poli, lisse (s^ppose a asper, comme lenis, mais cdui-
33918:leuisticum, Veg. Vet.3,53, 3 , cf. M.L.5038, et en lubestica: v.angl.
```


## [2026-09-06T23:03:17.446Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 33361,33380p LAT.txt; echo \"=== SYN light ===\"; grep -n -i \"15\\.8[0-9].*LIGHT\\|LIGHT (IN WEIGHT)\\|light in weight\" SYN.txt | head -6; echo \"=== SYN mud ===\"; grep -n -i \"^MUD\\|1\\.21[0-9].*MUD\\|MUD, MIRE\" SYN.txt | head -6",
 "description": "Print E-M levis and grep Buck"
}
```


### [2026-09-06T23:03:17.524Z] TOOL RESULT

```
leuis, -e: leger (sens physique et moral), oppose i grauis, e.g.
Pl., Tri.684, Lucr.3,335sqq., 5,474sqq., Cic.Agr. 9, 17,45; Deiot. 8 , 5 ,
avec des formations paralleles leuitas: grauitds; leuo: graub; leuiter:
grauiter, etc. Correspond pour le sens exactement au gr.xou<po£. — Usite
de tout temps. Panroman, sauf roumain. M.L.S004.
D 4 riv 4 s et composes: leuiculus : futile, de peu de poids; leuenna,
doublet vulgaire de leuis (Lab 4 rius ap. Geli.16,7,11 hominem leuennam),
qui semble avoir reyu une finale 4 trusque; leuitas (= xoucpOTrqS );
subleuis (Gloss.); leuo,-as ( = >toucpl.^oo) : i° alleger (quelque chose
a quelqu'un, l. onus, paupertatem alicui; ou quelqu'un de quelque
chose: l. aliquem aliqua re, ou alicuius rei ) par suite "soulager"
et dans 1 1 argot, comme notre "soulager" et "soulever" franyais,
"derober", sens conserve dans certaines langues romanes, cf.M.L.
s.n., et atteste en latin meme par le derive leuator que Petr., 140,15,
emploie dans le sens de "voleur a la tire"; 9 C soulever, lever, 41 ever;
sens qui apparait a 1 'epoque imperiale: Coi. 9,13,1, apis se confestim
leuat sublimius, et qui a persiste dans les 1 . romanes, M.L.5000.
De la leuamen "allfegement" (seul sens atteste dans la litterature,
ou le mot a une couleur po 4 tique; mais les 1 . romanes attestent un
sens concret et teehnique de "levain", M.L.4998), leudmentum n.:
=== SYN light ===
16375:burden’, etc.), all orig. ‘light in weight’ (15.82), with development of ‘easy’ through phrases ‘light work’, etc.
16873:Lat. levare, deriv. of levis ‘light? (15.82) and mostly ‘lighten, relieve’ but also ‘raise, lift’ in poetry and post-Aug. prose. Hence in this sense (or fr. sub- levdre) It. (sol)levare, Fr. (sou)lever, deriv. Sp. levantar. REW 5000.
26640:3. NIr. éadtrom, ‘light’ in weight (15.82), also ‘light’ in color (Dinneen McKenna), doubtless after the double use of NE light in which two different words are merged.
27170:15.82 LIGHT (in Weight)
27173:1. IE *legvh- and *leng’h- in words for ‘light in weight’ and ‘light, quick in movement’. Walde-P. 2.426. Ernout- M. 542 (assuming two orig. different groups, but this not called for). Walde- H. 1.788 f, Falk-Torp 637.
=== SYN mud ===
878:20 SELECTED INDO-EUROPEAN SYNONYMS 1.214 MUD k. 6 Goth. fant Lith. purvas ee es ON letr Lett. dubl’z (pl.) Lat. lutum, limus Dan. mudder,dynd (smuds) ChSl.  brinije
881:Where several words are entered for the same language, they may be in part somewhat differentiated in application (‘deep mud, mire’, ‘mud’ such as dredged from the bottom of a river, ‘mud’ in the roads, etc.) or in local preference (cf. NHG kot, dreck, etc.).
903:Sw. gyltja (esp. ‘deep mud, mire’), fr. the root of gjuta, Dan. gyde, Goth. giu- tan, etc. ‘pour’, like OE gyte ‘pouring, flood’. Hellquist 315.
7113:ChSl. (late) lajino (pl. lajtna ‘bricks’), SCr. dial. lajno, Boh. lejno, Pol. tajno : Skt. Iz- ‘cling to, adhere, lie upon’, Grk. adtvw ‘anoint’, Lat. linere ‘daub, smear’, limus ‘slime, mud, mire’, ete. Berneker 687. Briickner 306.
7115:Russ. kal = SCr. kao ‘mud, excre- ment’ (not popular), ChSl. kali ‘mud, mire’, prob. : Grk. xn\ts ‘spot’, Ir. caile id., Skt. kala- ‘blue-black’, Walde-P. 1.441.
27038:1. TE *let-, *slei- (with various forma- tions) in words for ‘slimy, slippery’ sub- stances, and in vbs. for ‘slip, smear, stick, etc.’, cf. Lat. limus ‘mud, mire’, OE lam, OHG leim ‘clay’, ON, OE slim ‘slime’, etce.; Grk. atv ‘smear, anoint’, Lat. linere ‘smear’, etc. Walde-P. 2.389 ff. Ernout-M. 542. Walde-H. 1.782. Falk-Torp 1061 f.
```


## [2026-09-06T23:03:26.444Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 27170,27200p SYN.txt",
 "description": "Print Buck 15.82"
}
```


### [2026-09-06T23:03:26.492Z] TOOL RESULT

```
15.82 LIGHT (in Weight)
rAagpbs (KoDpos) Goth. _ lethts oe Reiss ON lair Lat, levis ; Dan. let it.  leggiero (lieve) Sw. latt rr Léger OE leoht Sp. _legero (leve) ME light Rum. wusor NE light Ir &romm Du. Licht Nir.  éadlrom OHG lihti VW.  ysgafn MHG_ liht(e) Br. skaziv NHG leicht Words for ‘light’ in weight are com-
monly used also for ‘light, nimble’ in movement, and in one case the latter sense is clearly the earlier. But the great majority belong to an inherited group used in both senses.
1. IE *legvh- and *leng’h- in words for ‘light in weight’ and ‘light, quick in movement’. Walde-P. 2.426. Ernout- M. 542 (assuming two orig. different groups, but this not called for). Walde- H. 1.788 f, Falk-Torp 637.
Grk. éhagpds, NG pop. also ddadpés, thagpts; Lat. levis (> It. lieve, Sp. leve; oe ae old tugor with suffix -gor, cf. er 1844; VLat. *levidrius > Fr. 5003-4). a leggiero, Sp. legero. REW sae % oth. lethis, OE léoht, etc.,
me.; Lith. lengvas; ChSI.
Lith. lengvas Lett.  viegls ChSl. Ligitkit SCr. lak Boh. lehky Pol. = lekki Russ. legkij Skt. _—_ laghu- Av. auetee
liguku, etc., general Slavic; Skt. raghu-, laghu- (Av. ragu- ‘quick’); Alb. lehté; here also with different meaning Grk. éehaxts ‘little, paltry’, Ir. laigiu, MW Ulez ‘less’, OHG lungar ‘quick’, etc.
2. Grk. xoidos (rarely of weight, most- ly ‘light, nimble, vain, etc.’), etym.? Boisaecq 504.
3. Ir. &romm, NIr. éadirom, neg. of tromm ‘heavy’ (15.81).
W. ysgafn, Br. skafv, skant : Ir. sca- man ‘lung’ (cf. NE lights ‘lungs’ and the related lung), etym. dub. Walde-P. 2.601. Pedersen 1.76. Stokes 308.
4, Lett. viegls : Lith. viglas or vigrus ‘quick, lively’, Slov. vegati ‘waver’, Skt. vij- ‘gush, heave, be agitated’, etc. Miihl.-Endz. 4.654. Walde-P. 1.234.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1074 SELECTED INDO-EUROPEAN SYNONYMS
15.83 WET, DAMP
Grk. dypés, vorepéds Goth. (natjan, vb.) Lith.  Slapias, drégnas NG bypés, Bpeyutvos (vorepds) ON vdir, vokr Lett.  slapjs, mikls, mit Lat. «tmidus, madidus, Dan. vaad, fugtig drégns aT, tividus , Sw. vdt, fuktig ChSl. mokri, It. bagnato, umido OE wel, fiht SCr. _ mokar, vlazan Fr. moutllé, humide, ME wel, moyste Boh. mokry, olhky moite NE wel, damp, moist Pol. mokry, wilgotny Sp. mojado, hiimedo Du. nat, vochtig Russ. mokryj, syroj, vlaSnys Rum. ud, wmed OHG naz, fihti Skt. drdra- oreete Ir. Sliuch MHG naz, viuhte Av. napta- Nir. fliuch NHG _zass, feucht W. guwlyb, lazth
Br. gleb, leiz
It is impossible to draw a sharp line between ‘wet’ and ‘damp’. The dis- tinction according to the degree of wet- ness, a8 in the current use of NE wet and damp, holds also in the main for the Gme. and Balto-Slavic words. But elsewhere this is ignored, and where sev- eral words are in use, as in Latin and the Romance languages, the choice depends on the kind of object described, the ground, a rag, etc., whether naturally wet or made wet, etc., all too diverse and complicated to be noted here.
Apart from the inherited group, the words are connected with others for ‘water’, ‘bathe’, ‘leak’, ‘melt’, ‘vapor’, ‘soften’, ‘mire, filth’(?).
1. TE *weg-. Walde-P. 1.248. Er- nout-M. 1123. REW 4233, 9030.
Grk. iypés; Lat. amidus, and (by as- sociation with humus ‘earth’) hiimidus (> It. umido, Rum. umed, Fr. humide, Sp. himedo), and tvidus, whence tidus (> Rum. ud); ON vokr.
2. Grk. (Hom.) véris, Att. vorepés, beside vorts ‘moisture’, vé7os ‘south wind’ (= ‘damp’), prob. : Arm. nay ‘wet, liquid’, Lat. natare ‘swim’, fr. an extension of the root *(s)na- in Grk. vaxw, Lat. nare (cf. Umbr. veskla snata ‘vessels for liquids’), Skt. sna- ‘swim’, etc. Walde-P. 2.692 f.
NG Speyuévos, pple. of Bpexw ‘wet, moisten’, intr. ‘rain’, class. Grk. ‘wet,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
steep’, pass. ‘get wet, be rained on): Bpoxy ‘rain’, Lett. mdarga ‘gentle rain’, etc. Walde P. 1.280.
3. Lat. madidus, fr. madére ‘be Wet, drip with’ : Grk. padéw ‘be moist, fall off (of hair)’, Ir. maidim ‘break out, go to pieces’, etc. Walde-P. 2.231. Ernout- M. 579. Walde-H. 2.6 f.
It. bagnato, pple. of bagnare ‘bathe, wet, moisten’ (VLat. balneare fr. balnea, earlier balineum ‘bath’, fr. Grk. Bada- vetoy). Trnout-M. 101. REW 913.
Fr. mouillé, Sp. mojado, pple. of Fr. mouiller, Sp. mojar ‘wet, moisten’, fr. a VLat. *mollidre, fr. mollis ‘soft’. REW 5646.
Fr. moite, OF r. moiste (> ME moyste,
NE moist), prob. fr. “muscidus for Lat. miucidus ‘moldy’ blended with musteus ‘musty’. REW 5711. Gamillscheg 618. Bloch 2.71. _ 4. In. fliuch, W. gwlyb, MBr. gloeb, Br. gleb, perh. : Lat. liquidus ‘liquid’, etc., root *wleik-(?). Walde-P. 2.397. Pe- dersen 1.60. Stokes 285. Walde-H. 1.812. ;
```


## [2026-09-06T23:03:28.265Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk '/\\[pdf page/{p=$0} /leg[^ ]*h.*leicht|ragu|lengh-/{print p\" :: \"substr($0,1,180)}' WLD_Bd2_pages.txt 2>/dev/null | head -10; echo \"=== files ===\"; ls",
 "description": "Grep Walde-Pokorny Bd2"
}
```


### [2026-09-06T23:03:30.107Z] TOOL RESULT

```
 ::    Ai. pracna-, av. frahia- m. „Befragung, Frage‘-, arm. harm „Braut,
 :: „Arschbacke“; mit einer Ubertragung aus „cunnus“ (wie aisl. ref-keif
 :: (wenn erst mit sekundarer Ifasalubertragung aus andern Nomina auf -7I,
 :: bhred(h?) „waten", im Bsl. auch mit ahnlichen Bed.-Ubertragungen wie
 :: s,   u. lengh-.
 :: . leg I, II. S. auch u. legy:h- „leicht".
 :: 2.    lengh- .,lugen“.
 ::  s.   dariiber u.    legV:h-          „leicht‘').
 :: leg^h- „leicbt in Bewegung und Gewicht“, verbal „sich leicht, flink be-
 :: iiay;^dva) s. u. *lengh- „wornacb ]angen“), apr. lunkis „Winkel“, lett, Mn-
=== files ===
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
```


## [2026-09-06T23:03:37.044Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk '/\\[pdf page/{p=$0} /leg\\^h- „leicbt in Bewegung/{print p; f=1} f&&c<40{print substr($0,1,200); c++}' WLD_Bd2_pages.txt | head -45",
 "description": "Print Walde-Pokorny legwh entry"
}
```


### [2026-09-06T23:03:38.947Z] TOOL RESULT

```
leg^h- „leicbt in Bewegung und Gewicht“, verbal „sich leicht, flink be-
    wegen“, nasaliert (u. zw. vermutlich zunachst im Ifasalpraesens) length-.
    Ausfuhrlich Osthoff MU. VI 1— 70 m. Lit., wo auch gegen die nicht
     iiberzeugenden Versuche von Zerlegung in zwei ursprgl. verschiedene
       Sippen.
   Ai. laghii-^ raghil- „rasch, leicht, gering“, Komp. IdgJiiyams-^ Sup. IdgJiistha-;
av. raqii-^         f.   rdvi „flink'',   Komp. rdnjyo^ Sup. rdnjista- (erweisen nicht zu-
verlassig       den Positiv und fur ai, lagh- a aus n)
                  fiir

   ai. rJidnt- „schwach, klein'^ („*leicht“; nicht zu av. ordyayit- „entsetzlich”,

dt. arg^ Uhlenbeck Ai.Wb. s. v., Wood Min. 21, 39); av. ronjaiti^ ronjayeiti
„macht leicht, flink, laSt sich bewegen^^, ai. rdmhate^ rd^aghati^ Id'ioghati
„rinnt, eilt, springt auf, springt uber“;                        arm. arag^ erag „schneir^, iran. Lw.
   gr. elayvg „gering'‘,              Komp. eXdoocov^ att. iXavtaiv (a nach rayvg                          :   ^aaocov)^
Sup     iXdxicfrog {iXaxvQ aus idg.          wie si. Ihgzli^ und kelt. ^lag-; ai.
laghil- vielleicht ebenso, oder hochstufig wie lat. levis\ s. zuletzt Giintert
Abl. 61); eXacpQog „leicht, flink“ (wohl aus ^Ing^hros       ahd. lungar)    Ost-       =                        ;


hoff 63 tritt fiir ^l^q^hrds eln) ; fraglich Xoxpdv „8ich erholen, ausruhen,
nachlassen, trans. erleichtern, entlassen, befreien^ (Bed.-Parallelen bei Ost-
hoff 3f. s. eine andere Deutung u. Idhh „Iaben“);
              ;


                                            dem Gewichte, aber auch der
   alb. Veli^ Vehete „leicht'*; lat. levis „leicht
Bewegung nach*‘ (beruht auf dem f.           zum m. Hegfhii-S] nicht erst
nach gravis und brevis nasallos geworden; s. Yf. LEWb.^ s. v.);
   air.       Komp. laighi (und higu) „kleiner, schlechter“ == mcymr. llei^ ncymr,
llai „minor‘',            corn, le ds.      bret. -lei      in abret. nahn-lei „nihilominus^‘                        (urk.
*Iag-‘ios^        idg.                s. o.),    Sup.   Ingimem und Ingarn^ mcymr. lleiaf
                                                         air.
(aber mir. lug-leuyinecli                 „springend wie If enthalt lug ,,Luchs?'‘ S. 412),
mbret.         laii      „klein,    schlecht''    (daraus mir. Imi^ la             ds.,     s.   Pokorny KZ. 45,
74 gegen Osthoff). air. lagat ,,parvitas‘-'; air. lingim „spri‘nge“ (wegen des
Praet. leblamg von Osthoff 21 ff. vielmehr auf eine Wz. mit anl. bjp zuriick-
gefuhrt, doch eher mit erst analogischer Kachahmung der p ?>-Redupli-                                  :
```


## [2026-09-06T23:03:46.980Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"leg\\^h- „leicbt in Bewegung\" WLD_Bd2_pages.txt; awk 'NR<=  '\"$(grep -n 'leg\\^h- „leicbt in Bewegung' WLD_Bd2_pages.txt | cut -d: -f1)\"' && /\\[pdf page/{p=$0} END{}' WLD_Bd2_pages.txt >/dev/null; L=$(grep -n 'leg\\^h- „leicbt in Bewegung' WLD_Bd2_pages.txt | cut -d: -f1); head -$L WLD_Bd2_pages.txt | grep -n \"\\[pdf page\" | tail -2; echo \"=== lei- schleimig ===\"; grep -n \"schleimig\\|lei-.*schleim\" WLD_Bd2_pages.txt | head -8",
 "description": "Find WLD page numbers"
}
```


### [2026-09-06T23:03:48.728Z] TOOL RESULT

```
28296:leg^h- „leicbt in Bewegung und Gewicht“, verbal „sich leicht, flink be-
=== lei- schleimig ===
4974:und andem K6rnem‘\ picckala-, picchild- „schleimig, schliipfrig'^, Pick I*
4976:um als *piska fiir die Sippe von piscis eine Gdbed. „schleimig“ zu er-
16588:.,woriiber streichen, auf schliipfrigem, schleimigem gleiten oder gleiten
16610:in Beziehung stehenden ^juvx-o-og „schleimig'-, s. Johansson KZ. 30, 421,
16741:seits j.schleimig, Schleim^', andrerseits ,,gleiten, dariiber streichen, schliefen“.
25716:3. lei-    „schleimig,              glitschig,   durch Nasse glitschiger Boden, ausgleiten,
25718:        fahren   :    andrerseits schleimig             = klebrig^*, vielfach auch slei-.               Gleich-
25751:verschmieren”, vgl. auch ai. lindu- „schleimig, schliipfrig'^ (WoodKZ. 45, 61).
```


## [2026-09-06T23:03:53.985Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n 25716,25760p WLD_Bd2_pages.txt | cut -c1-200",
 "description": "Print Walde-Pokorny lei-3"
}
```


### [2026-09-06T23:03:54.031Z] TOOL RESULT

```
3. lei-    „schleimig,              glitschig,   durch Nasse glitschiger Boden, ausgleiten,
        woruberhinsclileifen oder -streichen, auch glattstreifen, glattend woriiber
        fahren   :    andrerseits schleimig             = klebrig^*, vielfach auch slei-.               Gleich-
        heit mit lei-^ „gie6en, flieBen, tr5pfeln‘‘ unter                     dem gemeinsamen Be-
        deutungselement des J^assen                      ist    mindestens ganz zweifelhaft (s, Vf.
        LEWb.^ u. Uhd): s. auch lei „sich ducken“, wo Lit. zu den verschie-
     denen Vermittlungsversuchen zu andern Wzln, lei,
                                      KZ. 32, 287 Anm.) „bestreiche, salbe“;
   Gr. a)uv(x> {-Iv- aus -Tv?-, Solmsen
lat.     -ere^ Jevl {*leiHai^ Sommer Hdb.^ 74: von de-levi scheint dcleo aus-
gegangen, s. u. del- spalten“), lltum „beschmieren, bestreichen“, linio, -Ire
ds., poliOj -Ire„(durch Dariiberstreichen) glatten, polieren^; air. lenaid,^ Pf.
rolil            (eigentlich „klebt an einem‘‘; cymr. can-lijn „folgen“ will
         j,folgen"‘
Pedersen KG. II 539 lieber zu glynn, ir. glenaid „steckenbleiben, an-
haften^‘ stellen), air, lenomnaih „lituris“, abret. linom „litura“, aslenaim
„besudle, oblino“ (s. Pedersen KG. II 565; B. bei Fick II ^ 251 erwagt fiir
die kelt. Worte ohne Kot die GLlipnami von der Erw.                 als „woran             ;


kleben^^ wohl auch                  ai.                        „schmiegt sich
                                          linati (gramm.), lay ate       llyate, Ityati
an, liegt an, bleibt stecken, versteckt sich, verschwindet“ (letztere Bed.
vermag Zugehorigkeit zu lei- „sich ducken“ nicht ausreichend zu stiitzen),
llna^ j^sich anschmiegend, anliegend^S    Curtins 365 f.
   Lat. Iwitis „Bodenschlamm, Kot, Schmutz“ (^loimos^ vgL z. B. Solmsen
KZ. 38, 453) — ahd. leuyi „Lehm“ (genaue Ubersetzungsbelege bei Schulze
KZ. 45, 55), nhd. (in nd. Ltf.) LeluUy ags. lam „Lehm, Humus“, ahd. leime
„Lehm“, nhd. Leinicn, abl. ahd. ags. aisl. llm „Leim, Kalk‘‘ („*Erdmasse
zum Verkleben'O; auf einem e5-St. Holes- beruht aisl. leir n. „Lehm‘‘ (lajis-),
leira schw. Fern. „lehmiger Strand“ und apr. (Trautmann Apr. 368) layso f.
.jLetteii, Ton, Tonerde^; in ders. Bed. von einer ^Z-Erw. apr. laydis „Lehm“
und alb. Ve^ „feuchter Ton, Erde, wie sie nach Austrocknung einer Regen-
pfiitze librigbleibt^' (Stamm Ved-\ G. Meyer BB. 14, 54, Falk-Torp u. lim^
Trautmann aaO.); wozu lit. laistau^ -yti „verkleben, mit Lehm oder Kalk
verschmieren”, vgl. auch ai. lindu- „schleimig, schliipfrig'^ (WoodKZ. 45, 61).
Als Bezeichnung schleimiger Fische linh „Schleie‘‘ (usw. s. Berneker 722 f.),
    Walde, Etymologisches Worterbuch. H.                                                       26
390                                                 lei-



lit.    lynas^   lett.   Imis^   apr. Unis „Schleie*^ (s. Boisacq 565 und Berneker
aaO., gegen Uhlenbecks              KZ. 39, 259 f. Deutung von lim aus Hipnh zu
skr. lipan^              „A.sche‘^, woruber s. Berneker 723) uud gr. hvsvg „Schleim-
```


## [2026-09-06T23:04:01.924Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lever",
 "prompt": "Give the etymology of 'lever' and mention related words alleviate, elevate, relieve, leaven — do they all come from Latin levare / levis, PIE *legwh-?"
}
```


## [2026-09-06T23:04:04.467Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B1%D9%86%D8%A7%D9%88%D8%A7%D9%84/",
 "prompt": "What do Persian dictionaries (فرهنگ معین، دهخدا، عمید) say about کارناوال — its meaning and its stated origin (French)?"
}
```


### [2026-09-06T23:04:08.321Z] TOOL RESULT

```
# Etymology of "Lever" and Related Words

**Origin of Lever:**
The word "lever" comes from Old French *levier* (12c.), meaning "a lifter" or "crowbar," derived from the verb *lever* meaning "to raise." This traces back to Latin *levare* "to raise," rooted in the adjective *levis* meaning "light in weight." Ultimately, these descend from the Proto-Indo-European root *legwh-, meaning "not heavy, having little weight."

**Related Words:**
Yes, all the words you mentioned share this common etymological ancestry:

- **Alleviate/Alleviation**: Formed from the Latin root *levare*
- **Elevate/Elevation**: Also derived from *levare*
- **Relieve**: Traces to the same Latin source
- **Leaven**: Connected through the PIE root *legwh-

The document confirms that *legwh- "might form all or part of" numerous English words, explicitly listing all four terms you mentioned alongside many others like "elevator," "levity," "relevant," and "relief."

This linguistic family reflects the conceptual connection between "lightness" and "raising" or "lifting" — ideas embedded in the root sense of making something lighter or less burdensome.
```


### [2026-09-06T23:04:10.854Z] TOOL RESULT

```
# Persian Dictionary Definitions of کارناوال

**Dehkhoda Dictionary** describes it as a joyful procession ("کاروان شادی") originating from French, noting it was adopted in Iran following European tradition but later abandoned.

**Farhang-e Moein** defines it as "a procession occurring at specific times yearly with comical clothing for entertainment and amusement."

**Farhang-e Amid** characterizes it as "a traditional European ceremony held at particular seasons where masked and costumed participants dance and perform while moving through streets."

All three sources acknowledge the **French origin** of the term. The dictionaries consistently emphasize the procession element—groups moving through streets in costumes and masks—along with associated entertainment, dance, and festive atmosphere.
```


## [2026-09-06T23:04:25.957Z] TOOL CALL #67: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%BA%D8%B1|page 305, root Legwh, node 1: Persian لاغر etymology (MP *lāgar < PIE *h₁ln̥gʷʰrós); note it cites Mann and Nourai himself' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81leng%CA%B7%CA%B0-|page 305, root Legwh: PIE *h₁lengʷʰ- \"light in weight, move lightly\", descendants' \\\n 'https://www.etymonline.com/word/carnival|page 305, Legwh nodes 5-7: carnival < Fr carnaval < It carnevale < Old Pisan carnelevare (caro + levare)' \\\n 'https://www.etymonline.com/word/lever|page 305, Legwh node 6: lever/leaven/alleviate/elevate/relieve all from Lat. levare/levis, PIE *legwh-' \\\n 'https://www.etymonline.com/word/slime|page 305, root Lei nodes 3-4: OE slim > slime, PGmc *slimaz, PIE *(s)lei-' \\\n 'https://en.wiktionary.org/wiki/limus|page 305, Lei node 5: Latin līmus \"mud, slime\" < PIE *h₂leyH-; separate līmus \"askew\"' \\\n 'https://en.wiktionary.org/wiki/%D9%84%D8%A7%DB%8C|page 305, Lei node 1: Persian لای \"dreg, sediment, mud\"; etymology incomplete on Wiktionary, cf. Icelandic leðja' \\\n 'https://en.wiktionary.org/wiki/%D9%84%D8%A7%DB%8C%D9%87|page 305, Lei node 1: Persian لایه \"layer; (obsolete) adhesive mud, sediment\"' \\\n 'https://en.wiktionary.org/wiki/laya|page 305, Lei node 2: Sanskrit लय laya senses' \\\n 'https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B1%D9%86%D8%A7%D9%88%D8%A7%D9%84/|page 305, Legwh node 8: Persian کارناوال in Dehkhoda/Moin/Amid, all give French origin' \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-06T23:04:33.061Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4c8b58671f75acc1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a0b73b534d6e8cc7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb1b4b76585eeaec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/692bed016b55edb0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a5c57d2bd3c28fab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/64b7776d26d5f89b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0b4f9954f1fd87de.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bdd55cce9d5ad206.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/626b1e984fb0af7e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/58d8e782c0b6eb90.txt
```


## [2026-09-06T23:04:56.285Z] TOOL CALL #68: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg305.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/305.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page image for audit"
}
```


### [2026-09-06T23:04:56.356Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T23:04:57.875Z] AGENT

Now I'll write the verification file.


## [2026-09-06T23:10:28.169Z] TOOL CALL #69: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-305.json",
 "content": "{\n  \"pdf_page\": 305,\n  \"book_page\": 275,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Legwh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₁lengʷʰ- / *h₁legʷʰ- 'light in weight; to move lightly, nimbly' (Pokorny leg̑ʷh- 660; Watkins legwh-)\",\n      \"note\": \"Root, language label and gloss are all correct. Pokorny p. 660-661 heads the entry 'lehgʷh- ... Meaning: light (adj.), Note: nasalized lehngʷh-'; Walde-Pokorny II 426 glosses it 'leicht in Bewegung und Gewicht' — literally Nourai's double gloss 'light in weight, quick in movement'. Buck 15.82 phrases it identically: 'IE *legvh- and *leng'h- in words for ‘light in weight’ and ‘light, quick in movement’'. Modern laryngeal notation is *h₁lengʷʰ-. Layout note: on the printed page an entirely EMPTY box (no language label, no words) hangs off the Avestan node by an arrow; it carries no content and the extraction correctly omits it — a printing/layout artifact, not a missing node.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₁lengʷʰ- «سبک، سبک‌وزن؛ چابک‌جنبش». پوکورنی (ص ۶۶۰) آن را leg̑ʷh- «سبک» و والده‑پوکورنی (ج ۲ ص ۴۲۶) «سبک در حرکت و وزن» آورده‌اند و باک (بند ۱۵٫۸۲) نیز همین دو معنا را کنار هم می‌گذارد؛ بنابراین نام ریشه، برچسب زبانی و معنای پیشنهادی نورایی هر سه درست است. صورت امروزی با حنجره‌ای آغازین *h₁lengʷʰ- نوشته می‌شود و گونهٔ خیشومی‌شدهٔ آن (*h₁ln̥gʷʰ-) در واژه‌هایی مانند «ریه» (lung) و «لاغر» بازتاب یافته است. ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81leng%CA%B7%CA%B0-\",\n        \"https://www.etymonline.com/word/lever\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:660\", \"status\": \"supports\", \"note\": \"Pokorny p. 660-661 (POK_full.txt l. 54300 ff.): 'Root / lemma: lehgʷh- ... Meaning: light (adj.) ... Note: nasalized lehngʷh-'; page tag 'Page(s): 660-661'. Material opens 'Old Indie laghu-, ved. raghu- ... Avestan ragu-, f. rəvī'. Exactly the root Nourai draws.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 426 (WLD_Bd2_pages.txt l. 28296)\", \"stance\": \"supports\", \"note\": \"'leg^h- „leicht in Bewegung und Gewicht“, verbal „sich leicht, flink bewegen“, nasaliert ... length-.' — Nourai's gloss is a translation of this line.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 30 s.v. legwh- (AHD_watkins1985.txt l. 668)\", \"stance\": \"supports\", \"note\": \"'legwh-. Light, having little weight. ... [Pok. legzh- 660.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 15.82 LIGHT (in Weight) (SYN.txt l. 27173)\", \"stance\": \"supports\", \"note\": \"'1. IE *legvh- and *leng’h- in words for ‘light in weight’ and ‘light, quick in movement’. Walde-P. 2.426.'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann col. 700 s.v. leguhos / lṇguhros\", \"stance\": \"supports\", \"note\": \"Mann sets up 'leguhos, is (leghus) ‘lightweight’. WP II, 426' with Skt. laghuh, raghuh, Lat. levis, and separately 'ṷnguhros ‘slight, nimble’'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"lâğar\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP لاغر lāḡar 'lean, thin, emaciated' is referred by Mann (IEC col. 700) to the nasalised r-stem *l̥ngʷʰ-ro- 'slight, nimble' of this root, the same formation as Gk. ἐλαφρός 'light, nimble' and OHG lungar 'swift': PIE *h₁ln̥gʷʰ-ró- > PIr. *Hlagra- > MP *lāgar > NP lāḡar, the semantic step being 'light (in weight)' → 'thin, lean' (compare the reverse of Pers. فربه farbeh 'fat', with which Mo'in explicitly contrasts it). The chain is phonologically awkward on two counts and that is why the verdict is not 'confirmed': (a) Old Iranian merged PIE *l into *r (hence the regular Avestan reflex ragu-, not *lagu-), so an inherited word could not keep initial l-; (b) the غ (ḡ/γ) for an expected -g- is likewise irregular. Neither Horn nor Hübschmann has the word, MacKenzie has no Pahlavi *lāgar, and Mo'in's footnote in Borhan-e Qate' gives only Iranian-dialect cognates (Kurdish, Natanzi, Sangsari, Lasgerdi, Shahmirzadi lāġer), which prove the word is old and widespread in Iranian but say nothing about its ultimate origin. Wiktionary's chain (MP *lāgar < OP *lagrah < PIr. *Hlagráh < PIE *h₁ln̥gʷʰrós) reproduces exactly this reconstruction but cites Mann and Nourai himself, so it is not independent confirmation.\",\n          \"derivation_fa\": \"«لاغر» را مان (فرهنگ تطبیقی هندواروپایی، ستون ۷۰۰) از گونهٔ خیشومی‌شدهٔ ریشه، یعنی *h₁ln̥gʷʰ-ró- «سبک، چابک»، می‌گیرد؛ همان ساختی که یونانی elaphrós و آلمانی باستان lungar از آن است: هندواروپایی *h₁ln̥gʷʰ-ró- ← ایرانی باستان *Hlagra- ← فارسی میانهٔ *lāgar ← فارسی نو «لاغر»، با تحول معنایی «سبک‌وزن» ← «باریک‌اندام». دو اشکال آوایی هست که پذیرش قطعی را دشوار می‌کند: نخست آنکه در ایرانی باستان l هندواروپایی به r بدل شده (چنان‌که صورت درست اوستایی ragu- است، نه *lagu-)، پس واژه‌ای موروثی نمی‌توانست «ل» آغازین را نگاه دارد؛ دوم آنکه «غ» به‌جای گِ میانوندی نیز بی‌قاعده است. هرن و هوبشمان این واژه را ندارند، مکنزی صورت پهلوی نیاورده، و حاشیهٔ معین بر برهان قاطع (ص ۱۸۷۷) تنها هم‌ریشه‌های گویشی (کردی، نطنزی، سنگسری، لاسگردی، شهمیرزادی lāġer) را می‌آورد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%BA%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:700\", \"status\": \"supports\", \"note\": \"Mann col. 700 (IEC.txt l. 9935, between the printed page markers '700' at l. 9930 and '701' at l. 9940): 'ṷnguhros ‘slight, nimble’. Cf. elnghus, elnguhos — Per. lāγar ‘lean’; OHG lungar ‘swift’; OE lungre ‘quickly, soon’; Gk. (variant) elaphrós ‘lightweight, quick’.' This is precisely Nourai's arrow.\"},\n            {\"ref\": \"MON:3530\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Farsi is only online as entry text (vajehyab/abadis) without the print pagination, and the local MON_part1/part2 OCR of the Persian is unusable gibberish; the 6-volume page 3530 could not be located. Grep of MON_part1.txt / MON_part2.txt for لاغر returned nothing.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, printed p. ~1877 (BQT_v3_pages.txt, pdf page 674), footnote 11\", \"stance\": \"partial\", \"note\": \"Mo'in's footnote on لاغر: 'بفتح سوم ، کردی lāġer ، ژابا ص ۳۷۵ ... نطنزی lāġer ... سنگسری ، سرخه‌یی ، لاسگردی و شهمیرزادی lāġer ... باریک ، باریک اندام ، مقابل فربه' with the Labibi verse. Confirms the word and its meaning and its spread over Iranian dialects, but offers no Pahlavi form and no IE etymology.\"},\n            {\"src\": \"HRN\", \"where\": \"grep 'lagar/lāgar/lâgar' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for lāġar (the only hits are the scholar's name 'de Lagarde').\"},\n            {\"src\": \"HUB\", \"where\": \"grep 'lagar' in HUB.txt\", \"stance\": \"silent\", \"note\": \"Hübschmann, Persische Studien: no entry (again only 'de Lagarde').\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"silent\", \"note\": \"No Pahlavi *lāgar / lagr is recorded; the MP link in the chain is a reconstruction, not an attestation.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Avestan\",\n          \"words\": \"ragu, ravi\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. ragu- (masc./neut.) 'swift, nimble, light', fem. rəvī, is the direct Iranian reflex of PIE *h₁lengʷʰ-u-: PIE *l > Indo-Iranian/Iranian *r (hence Skt. has both laghú- and the older raghú-), and the labiovelar *gʷʰ gives Av. -g- before -u-, while in the feminine *h₁l̥gʷʰ-u-ih₂ the -gu- was resolved to -v- (rəvī). The comparative and superlative built on the nasal grade *h₁lengʷʰ- are Av. rənjyō 'more nimbly' and rənjišta- 'nimblest', both in Bartholomae. The gloss 'quick' Nourai gives is Bartholomae's and Buck's 'flink / quick'.\",\n          \"derivation_fa\": \"اوستایی ragu- «تند، چابک، سبک» و مؤنث آن rəvī بازتاب مستقیم *h₁lengʷʰ-u- هندواروپایی در ایرانی است: l هندواروپایی در هندوایرانی به r بدل شده (از همین‌رو سنسکریت هم raghú- کهن و هم laghú- را دارد) و در صیغهٔ مؤنث *-gu- به -v- بدل شده و rəvī به دست آمده است. بارتولومه (فرهنگ ایرانی باستان) صورت‌های تفضیلی rənjyō «چابک‌تر» و عالی rənjišta- «چابک‌ترین» را از همین ستاک می‌آورد و ذیل rəvī به ragav- ارجاع می‌دهد. باک نیز صریحاً می‌نویسد «Av. ragu- ‘quick’». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81leng%CA%B7%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:660\", \"status\": \"supports\", \"note\": \"Pokorny 660 (POK_full.txt l. 54303): 'Avestan ragu-, f. rəvī ‘agile’; Kompar. ranjyo, Superl. ranjista- (of stem *length-)' — both of Nourai's words, with his gloss.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. ~1508, 1516 (BRT.txt ll. 25445, 25447 and the cross-reference line)\", \"stance\": \"supports\", \"note\": \"'j. ranjišta- Adj. (fem. -ya-) „der sich am leichtesten bewegt, der flinkste“'; 'j. ranjyō Adv. „leichter, flinker“'; and the cross-reference 'j. rəvī: s. unter ragav-' — i.e. Bartholomae files rəvī under the stem ragu-/ragav-, exactly as Nourai pairs them.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 426\", \"stance\": \"supports\", \"note\": \"'av. ragu-, f. rāvi „flink“, Komp. rənjyō, Sup. rənjišta-'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 15.82\", \"stance\": \"supports\", \"note\": \"'Skt. raghu-, laghu- (Av. ragu- ‘quick’)'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"lihtjaz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PGmc *līht(j)az 'light, not heavy' < PIE suffixed *h₁legʷʰ-t- (with the nasal variant *h₁lengʷʰ-to- giving Goth. leihts). The *-gʷʰt- cluster gave Germanic *-ht-, and the pre-consonantal nasal was lost with compensatory lengthening (*linhtaz > *līhtaz), whence Goth. leihts, ON léttr, OE lēoht/liht, OHG līhti, Ger. leicht. Nourai's 'lihtjaz' is verbatim Watkins's reconstruction *liht(j)az, the j-stem variant that underlies the OE adjective liht and the verb līhtan 'to lighten'.\",\n          \"derivation_fa\": \"ژرمنی آغازین *līht(j)az «سبک» از صورت پسوندی *h₁legʷʰ-t- هندواروپایی است. خوشهٔ *-gʷʰt- در ژرمنی به -ht- بدل شده و «ن» پیش‌از‑همخوان در گونهٔ خیشومی *linhtaz افتاده و واکهٔ پیشین کشیده شده است (*līhtaz)؛ بازتاب‌های آن گوتی leihts، نورس باستان léttr، انگلیسی باستان lēoht/liht و آلمانی leicht است. صورتی که نورایی می‌آورد (lihtjaz) عیناً بازسازی واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81leng%CA%B7%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1525\", \"status\": \"supports\", \"note\": \"Watkins s.v. legwh- (AHD_watkins1985.txt l. 668): '1. Suffixed form *legʷh-t- in Germanic *liht(j)az in: a. Old English liht, léoht, light: LIGHT²; b. Old English lihtan, to lighten: LIGHTER².' Nourai's 'lihtjaz' is this form; AHD:1525 is the corresponding page of the 1975 New College appendix.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. light, adj., not heavy (KLN_1971.txt l. 137598)\", \"stance\": \"supports\", \"note\": \"'ME. liht, light, fr. OE. leoht, liht, rel. to OS. liht-, ON. lettr ... Goth. leihts, ‘light’, fr. I.-E. base *le(n)gʷh-, ‘light, easy, agile, nimble’, whence also L. levis.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 426-427\", \"stance\": \"supports\", \"note\": \"The Germanic material (Goth. leihts, ahd. līhti etc.) is filed under leg^h- with the nasalised length- variant.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 15.82\", \"stance\": \"supports\", \"note\": \"'Goth. leihts, OE léoht, etc.' listed as the Germanic branch of IE *legvh-.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"light 2\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English light² 'not heavy' (as opposed to light¹ 'brightness', from PIE *leuk-) continues ME liht < OE lēoht/liht < PGmc *līht(j)az of the parent node. Nourai's numbering 'light 2' correctly keeps it apart from the homonym; the two are separate words in every modern dictionary (Klein prints two consecutive headwords 'light, adj., not dark' and 'light, adj., not heavy'), and Watkins likewise sends LIGHT¹ to leuk- and LIGHT² to legwh-.\",\n          \"derivation_fa\": \"انگلیسی light² «سبک» دنبالهٔ انگلیسی میانهٔ liht و انگلیسی باستان lēoht/liht است، از ژرمنی *līht(j)az گرهٔ بالادست. این واژه با هم‌آوای خود light¹ «روشنایی» (از ریشهٔ *leuk-) یکی نیست؛ شمارهٔ ۲ که نورایی گذاشته دقیقاً همین تفکیک را نشان می‌دهد و کلاین نیز دو سرواژهٔ جداگانه ثبت کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lever\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins index (AHD_watkins1985.txt l. 1748): 'LIGHT¹ leuk- / LIGHT² legwh-' — the English word 'light 2' is assigned to this root, as Nourai draws it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. light, adj., not heavy (KLN_1971.txt l. 137598)\", \"stance\": \"supports\", \"note\": \"Separate headword from 'light, adj., not dark, bright' (l. 137590), derived 'fr. I.-E. base *le(n)gʷh-'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 15.82\", \"stance\": \"supports\", \"note\": \"Table lists 'OE leoht / ME light / NE light' under IE *legvh-.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"levis; levâr; carni-levâre\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"levâr : lift\",\n          \"correct_form\": \"levāre\",\n          \"derivation\": \"Lat. levis 'light, of low weight' < *legʷh-u-i- (Watkins) — Ernout-Meillet: 'leuis, -e: léger (sens physique et moral), opposé à grauis'; it must be kept apart from the homonym lēvis 'smooth, polished', which belongs to the *(s)lei- root of entry 1. The second word is the misprint: the book prints 'levâr : lift' (verified on the printed page, high-resolution render of PDF p. 305), which is Nourai's misprint for the verb levāre 'to raise, lighten' — the very next line of the same box prints carni-levâre with its -e intact, and Watkins gives 'levis ... with its derivative levāre, to lighten, raise'. The extraction is faithful to the page; the error is the author's. Third word: Medieval Latin carnelevāre / carnelevāmen 'the removing of meat', from carō, carn- 'flesh' (Nourai's ☞Sek cross-reference, PIE *(s)ker- 'to cut') + levāre 'to take away, lift', the name of the days before the Lenten fast — Nourai's gloss 'reduce weight, a feast before fasting' is loose but the sense is right ('put away the meat').\",\n          \"derivation_fa\": \"لاتینی levis «سبک» از *legʷh-u-i- هندواروپایی است؛ ارنو و مه‌یه آن را «léger، در برابر grauis» می‌آورند و باید از هم‌آوای آن lēvis «صاف، صیقلی» (که به ریشهٔ *(s)lei- مدخل دوم همین صفحه می‌رود) جدا شود. واژهٔ دوم غلط چاپی است: کتاب «levâr : lift» چاپ کرده که خطای خودِ نورایی برای فعل levāre «برداشتن، سبک کردن» است — در همان کادر، سطر بعد carni-levâre را با «ـه» پایانی درست چاپ کرده و واتکینز نیز «levis ... با مشتق آن levāre» می‌نویسد؛ پس خطا از کتاب است نه از خوانش اسکن. واژهٔ سوم، لاتینی میانه‌ای carnelevāre «برداشتن گوشت» از carō/carn- «گوشت» (همان ارجاع ☞Sek نورایی) و levāre است، نام روزهای پیش از روزهٔ بزرگ مسیحیان. خطای چاپی کتاب.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lever\",\n            \"https://www.etymonline.com/word/carnival\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1525\", \"status\": \"supports\", \"note\": \"Watkins s.v. legwh- (AHD_watkins1985.txt l. 668): '2. Suffixed form *legʷh-u-i- in Latin levis (> Old French leger), light, with its derivative levāre, to lighten, raise: LEAVEN, LEVER, LEVITY; ALLEVIATE, CARNIVAL, ELEVATE ... RELIEVE.' Confirms levis, levāre and the carnival link; the printed 'levâr' is the book's own slip for levāre.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. leuis (LAT.txt l. 33361 ff.)\", \"stance\": \"supports\", \"note\": \"'leuis, -e: léger (sens physique et moral), opposé à grauis ... leuo, -as (= κουφίζω): 1° alléger ... 2° soulever, lever, élever ... De là leuamen ... les l. romanes attestent un sens concret et technique de “levain”'. Note also the SEPARATE headword at l. 33419 'leuis, -e: poli, lisse' — the homonym that belongs to the other root.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. carnival (SKT.txt l. 3023)\", \"stance\": \"supports\", \"note\": \"'F. carnaval, Shrovetide. — Ital. carnevale ... — Low L. carnelevale, carnilevamen, removal of flesh, Shrovetide. — L. carn-em, acc. of caro, flesh; and levare, to lift, remove, take away; from levis, light.' Exactly Nourai's carni-levāre.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 15.82 (SYN.txt l. 16873)\", \"stance\": \"supports\", \"note\": \"'Lat. levare, deriv. of levis ‘light’ (15.82) and mostly ‘lighten, relieve’ but also ‘raise, lift’ ... Hence It. (sol)levare, Fr. (sou)lever.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. carnival (KLN_1966.txt l. 6570)\", \"stance\": \"contradicts\", \"note\": \"Klein gives the folk etymology: 'F. carnaval, fr. It. carnevale, fr. ML. carne, vale, “O flesh, farewell!”'. Modern scholarship (Skeat, Etymonline) rejects this in favour of carnelevare/carnelevamen, i.e. Nourai's side.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"leaven, lever, alleviate, carnival, elevate, relieve\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six are Latin-via-French derivatives of levis/levāre and are listed together under legwh- by Watkins. leaven < ME levain < OF levain < VL *levāmen 'that which raises' (Klein). lever < OF levier/leveor 'lifter', from lever < levāre. alleviate < LL alleviāre (ad- + levāre). elevate < L ēlevāre (ex- + levāre). relieve < OF relever < L relevāre 'raise again, lighten'. carnival < F carnaval < It. carnevale < Old Pisan carnelevare (see node 5); it entered English c. 1540 and reached 'feasting, revelry in general' by the 1590s.\",\n          \"derivation_fa\": \"هر شش واژه مشتقات لاتینیِ levis/levāre هستند که از راه فرانسه به انگلیسی رسیده‌اند و واتکینز همه را ذیل همین ریشه فهرست کرده است: leaven از انگلیسی میانهٔ levain، از فرانسهٔ کهن levain، از لاتینی عامیانهٔ *levāmen «آنچه برمی‌آورد»؛ lever از فرانسهٔ کهن levier «اهرم» از فعل lever؛ alleviate از لاتینی متأخر alleviāre؛ elevate از ēlevāre؛ relieve از relevāre؛ و carnival از راه فرانسهٔ carnaval و ایتالیایی carnevale (نک. گرهٔ پیشین) که حدود ۱۵۴۰ میلادی وارد انگلیسی شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lever\",\n            \"https://www.etymonline.com/word/carnival\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. legwh- lists exactly 'LEAVEN, LEVER, LEVITY; ALLEVIATE, CARNIVAL, ELEVATE, LEGERDEMAIN, LEVIGATE, (MEZZO-RELIEVO), RELIEVE' — Nourai's six are a subset.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. leaven (KLN_1971.txt l. 135488)\", \"stance\": \"supports\", \"note\": \"'ME. levain, fr. F. levain, fr. VL. *levāmen, “something that raises” ... fr. levāre, “to lift, raise; to lighten, alleviate”, fr. levis, “light”. See level and cp. relieve.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. carnival (SKT.txt l. 3023)\", \"stance\": \"supports\", \"note\": \"Gives the French–Italian–Low Latin route to levare and levis, as above.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"French\",\n          \"words\": \"carnaval\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Fr. carnaval 'carnival, Shrovetide' does go back to Latin carnelevāre, but not directly as the chart's arrow (Latin → French) suggests: it was borrowed in the 16th century from Italian carnevale (older Milanese carnelevale, Old Pisan carnelevare), the Italian syncope carne-levale > carnevale > carnaval producing the French form. The step is thus Latin → Italian → French, and the -a- of carnaval reflects the Italian variant carnavale. Nourai's chart collapses the Italian stage; the ultimate etymon is correct, the route is abbreviated. He gives no reference for this node.\",\n          \"derivation_fa\": \"فرانسوی carnaval سرانجام به لاتینی carnelevāre بازمی‌گردد، اما نه به‌طور مستقیم چنان‌که پیکان نمودار می‌نماید: این واژه در سدهٔ شانزدهم میلادی از ایتالیایی carnevale (صورت‌های کهن‌تر: میلانی carnelevale، پیزایی کهن carnelevare) وام گرفته شده و «ا» در carnaval بازتاب گونهٔ ایتالیایی carnavale است. پس مسیر درست لاتینی ← ایتالیایی ← فرانسوی است و نورایی مرحلهٔ ایتالیایی را حذف کرده است؛ ریشهٔ نهایی درست ولی راه وام‌گیری کوتاه‌شده است. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/carnival\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai cites no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. carnival (SKT.txt l. 3023)\", \"stance\": \"partial\", \"note\": \"'carnival. (F.-Ital.-L.) F. carnaval, Shrovetide. — Ital. carnevale, carnavali ... — Low L. carnelevale' — Skeat's own label 'F.-Ital.-L.' shows the Italian stage that the chart omits.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. carnival (KLN_1966.txt l. 6570)\", \"stance\": \"partial\", \"note\": \"'F. carnaval, fr. It. carnevale' — agrees on the Italian intermediary, but derives the Italian from the folk-etymological 'carne, vale'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"kârnâval\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP کارناوال kārnāvāl is a 20th-century loan from French carnaval, taken over with the French stress-less vowels rendered by Persian long ā (car-na-val > kār-nā-vāl) — the ordinary treatment of French loanwords in Persian of the Pahlavi period. Dehkhoda glosses it 'کاروان شادی' and marks it French, noting that the practice was briefly imitated in Iran and then dropped; Mo'in and Amid likewise define it as a European seasonal procession in costume and masks and label the word French. This is a modern European loan, not an Arabic-mediated one, and the chart's French → Persian arrow is exactly right.\",\n          \"derivation_fa\": \"«کارناوال» وام‌واژه‌ای است که در سدهٔ چهاردهم خورشیدی از فرانسویِ carnaval گرفته شده و واکه‌های کوتاه فرانسوی در آن به الف کشیدهٔ فارسی بدل شده‌اند (car-na-val ← کار-نا-وال)، همان رفتار همیشگی فارسی با وام‌واژه‌های فرانسوی. دهخدا آن را «کاروان شادی» معنی کرده و فرانسوی دانسته است، و معین و عمید نیز آن را جشن و دستهٔ خیابانیِ اروپایی با جامه و نقاب تعریف کرده و منشأ فرانسوی را ثبت کرده‌اند. پس وام‌گیری مستقیم از فرانسه است و پیکان نمودار درست است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B1%D9%86%D8%A7%D9%88%D8%A7%D9%84/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"VOP:269\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (1371/1992) is recorded in refs_online.json as kind 'none' — no copy found on archive.org, ketabnak, noorlib or the open web, so p. 269 could not be consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. کارناوال, via abadis.ir\", \"stance\": \"supports\", \"note\": \"Mo'in defines it as a yearly procession in comical costume for entertainment and marks the word as French; Dehkhoda on the same page: 'کاروان شادی' — از فرانسه.\"},\n            {\"src\": \"ARY\", \"where\": \"grep of ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary does not treat modern European loanwords such as کارناوال (grep returns nothing; the Persian OCR of this book is in any case very poor).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Lěi, Lôi\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *(s)lei- / *leyH- 'slimy, sticky; to smear' (Pokorny 3. lei- 662-664; Watkins lei- 'Also slei-. Slimy.'; modern notation *h₂leyH-/*sleyH-)\",\n      \"note\": \"Both parts of the root name are real headwords: Pokorny's 3. lei- 'slimy; to glide' (pp. 662-664, 'Note: various also slei-') is the e-grade, and Mann's lōi- (1) 'smeared, sticky, greasy; smear' (col. 706-707) is the o-grade — so 'Lěi, Lôi : slime, sticky' with refs POK:662 and IEC:706 is accurate on both counts. Modern handbooks write the root with a laryngeal (*leyH-/*h₂leyH-) and are less sure that the s-mobile forms and the non-s forms are one root; that is a notational, not a substantive, difference from Nourai's chart.\",\n      \"note_fa\": \"هر دو نامی که نورایی برای ریشه آورده سرواژهٔ واقعی‌اند: پوکورنی «lei- ۳» را در صص ۶۶۲–۶۶۴ با معنی «لعابی، لغزنده» و با یادداشت «گاه slei- نیز» آورده (درجهٔ e)، و مان در ستون ۷۰۶–۷۰۷ «lōi- (۱)» را با معنی «آغشته، چسبناک، چرب؛ اندودن» ثبت کرده است (درجهٔ o). پس هم نام ریشه، هم معنای «لجن، چسبناک» و هم هر دو ارجاع (POK:662 و IEC:706) درست است. ریشه‌شناسی امروزی این ریشه را با حنجره‌ای *leyH-/*h₂leyH- می‌نویسد و در یکی‌بودن گونه‌های با s و بدون s کمی محتاط‌تر است؛ این اختلاف نگارشی است نه محتوایی. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/slime\",\n        \"https://en.wiktionary.org/wiki/limus\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:662\", \"status\": \"supports\", \"note\": \"Pokorny (POK_full.txt l. 54710 ff.): 'Root / lemma: lehi-3 ... Meaning: slimy; to glide ... Note: various also slei-' with 'Page(s): 662-664'. Latin lino/linere, līmus, OE slīm and Skt. līnāti/layate all stand there.\"},\n        {\"ref\": \"IEC:706\", \"status\": \"supports\", \"note\": \"Mann col. 706-707 (IEC.txt l. 10015, between the printed page markers '706' at l. 10008 and '707' at l. 10016): 'lōi- (1) ‘sméared, sticky, greasy; smear’. WP II, 392 (Short grade in) Skt. láyah ‘adherence’; OCS ... loj, m. ‘fat, grease’; ... (long-gde in) Per. lāyi ‘mud’. Vowel ambig.' — this single column is the source of BOTH Persian and Sanskrit nodes.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 389-390 (WLD_Bd2_pages.txt l. 25716 ff.)\", \"stance\": \"supports\", \"note\": \"'3. lei- „schleimig, glitschig, durch Nässe glitschiger Boden, ausgleiten ... andrerseits schleimig = klebrig“, vielfach auch slei-.' Contains lat. lino -ere lēvī litum, lat. līmus, ai. līnāti/layate, ags. slīm.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. lei- (AHD_watkins1985.txt ll. 669-671)\", \"stance\": \"supports\", \"note\": \"'lei-. Also slei-. Slimy. 1. Germanic *sli- ... a. Old English slim, slime: SLIME ... 2. Suffixed form *lei-mo- in Latin limus, slime ... 4. Extended form *(s)leiə- in: a. nasalized zero-grade form *li-n-ə- in Latin linere, to anoint: LINIMENT. [Pok. 3. lei- 662.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt l. 27038)\", \"stance\": \"supports\", \"note\": \"'1. IE *lei-, *slei- (with various formations) in words for ‘slimy, slippery’ substances ... cf. Lat. limus ‘mud, mire’, OE lam, OHG leim ‘clay’, ON, OE slim ‘slime’ ... Lat. linere ‘smear’. Walde-P. 2.389 ff.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"lây\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP لای lāy 'mud, silt, sediment, lees' (whence the collocations the chart quotes, گل و لای 'mud and silt' and لایروبی 'dredging') is attached by Mann alone to the o-grade *lōi- of this root, alongside OCS/Lith. loj/lájus 'fat, grease' — and Mann himself flags the reconstruction with 'Vowel ambig.', i.e. he cannot decide the grade. Borhan-e Qate' (ed. Mo'in) defines لای exactly as the chart does — 'گل تیره و سیاه ... که در ته حوضها و جویها نشیند - و دردی شراب' ('dark mud that settles at the bottom of pools and channels; the lees of wine') — and gives no etymology at all; the derivative لایه is recorded by Wiktionary with the obsolete sense 'adhesive mud, sediment'. Wiktionary's entry for لای leaves the etymology of this sense explicitly 'missing or incomplete' and only compares Icelandic leðja (which does belong to this root, cf. OHG letto 'clay'). No Middle Persian form is attested, and the same problem as with لاغر applies — a native Iranian word should not begin with l-. So: a semantically perfect but formally unproven equation, resting on one comparatist.\",\n          \"derivation_fa\": \"«لای» به معنی «گِل، لجن، دُرد، رسوب» (از همین‌جاست «گل و لای» و «لایروبی» که در نمودار آمده) را تنها مان به درجهٔ o همین ریشه، یعنی *lōi-، می‌بندد، در کنار اسلاوی کهن loj و لیتوانیایی lájus «پیه، چربی» — و خود او هم در برابر آن نوشته است «واکه مبهم است». برهان قاطع با حاشیهٔ معین همان معنایی را می‌دهد که نمودار آورده («گل تیره و سیاه ... که در ته حوضها و جویها نشیند ـ و دردی شراب») ولی هیچ ریشه‌شناسی به دست نمی‌دهد، و ویکی‌واژه بخش ریشه‌شناسی این معنی را ناقص می‌داند و تنها ایسلندی leðja را برای مقایسه می‌آورد. صورت فارسی میانه‌ای هم گواهی نشده و همان اشکال «ل» آغازین که در «لاغر» بود اینجا نیز هست. پس برابرنهاد از نظر معنایی بی‌نقص اما از نظر آوایی اثبات‌نشده است؛ با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%DB%8C\",\n            \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%DB%8C%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:706\", \"status\": \"supports\", \"note\": \"Mann col. 706-707 (IEC.txt l. 10015): 'lōi- (1) ‘sméared, sticky, greasy; smear’ ... (long-gde in) Per. lāyi (‘mud’. Vowel ambig.)' — supports the arrow, but with Mann's own caveat about the vowel grade.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, printed p. ~1885 s.v. لای (BQT_v3_pages.txt, pdf page 680)\", \"stance\": \"partial\", \"note\": \"'و گل تیره و سیاه را نیز گویند که در ته حوضها و جویها نشیند — و دردی شراب و امثال آن نیز گفته‌اند' — confirms the word and Nourai's gloss 'mud, sediment' precisely; Mo'in's footnotes on this page give an etymology only for the homonym لاییدن 'to babble' (MP rāpak, Skt. lap-), none for لای 'mud'.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"No entry for lāy 'mud' (grep of HRN.txt).\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"silent\", \"note\": \"No Middle Persian *lāy is recorded, so the NP word has no attested MP ancestor.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"layah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Skt. layáḥ m. is the o-grade action noun of the root lī- (līnāti, láyate, līyate) 'to cling, stick fast, adhere, nestle up to; to dissolve, melt away'; the sense Nourai gives, 'adherence', is the primary one in Monier-Williams ('the act of clinging or sticking to'), and it is the sense Mann prints in the very column Nourai cites. Walde-Pokorny II 389 files the same verb here — 'ai. līnāti (gramm.), layate, līyate, līyati \"schmiegt sich an, liegt an, bleibt stecken\"' — beside Lat. linere and Gk. ἀλίνω, so the derivation from this root is standard, not Nourai's invention. (The other, later senses of laya — 'dissolution, destruction; rest, musical tempo' — come from the 'melt away' branch of the same verb.)\",\n          \"derivation_fa\": \"سنسکریت layáḥ اسم مصدر با درجهٔ o از ریشهٔ lī- (līnāti، láyate، līyate) «چسبیدن، پیوستن، فروماندن؛ گداختن و از میان رفتن» است؛ معنایی که نورایی می‌آورد («چسبندگی») همان معنی نخست در مونیر‑ویلیامز است و همان است که مان در ستون ۷۰۶ می‌نویسد. والده‑پوکورنی (ج ۲ ص ۳۸۹) همین فعل سنسکریت را در کنار لاتینی linere و یونانی alínō ذیل همین ریشه آورده است، پس این استخراج در ریشه‌شناسی رایج پذیرفته است. معناهای دیرتر laya («انحلال، نابودی، ضرب موسیقی») از شاخهٔ «گداختن» همان فعل‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/laya\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:706\", \"status\": \"supports\", \"note\": \"Mann col. 706-707 (IEC.txt l. 10015): 'lōi- (1) ... (Short grade in) Skt. láyah ‘adherence’' — word, gloss and root exactly as Nourai draws them.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II 389 (WLD_Bd2_pages.txt l. ~25735)\", \"stance\": \"supports\", \"note\": \"'ai. līnāti (gramm.), layate, līyate, līyati „schmiegt sich an, liegt an, bleibt stecken, versteckt sich, verschwindet“, līná- „sich anschmiegend, anliegend“' — filed under lei- 3.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny 662-663 (POK_full.txt l. 54728)\", \"stance\": \"supports\", \"note\": \"'1. Old Indie līnati (gramm.), layate, līyate līyati “adhere; cling or press closely, stick to”; līna- “nestling up, snuggling up; clinging to, adjoining”.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt l. 7113)\", \"stance\": \"supports\", \"note\": \"'ChSl. lajino ... : Skt. lī- ‘cling to, adhere, lie upon’, Grk. ἀλίνω ‘anoint’, Lat. linere ‘daub, smear’, limus ‘slime, mud, mire’' — the same family.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Old English\",\n          \"words\": \"slim\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE slīm 'soft mud, slime' < PGmc *slīmaz (ON slím, MDu. slijm, MHG slīm, Ger. Schleim), from the s-mobile form *slei- of this root: the root-final laryngeal/-i- gives Germanic ī, and the -m- is the same *-mo- suffix seen in Lat. līmus < *loi-mo-. Nourai's gloss 'mud' is Etymonline's and the OED's rendering of OE slīm. Watkins assigns OE slim to lei- and Klein derives it 'fr. I.-E. base *(s)lei-, slime, slimy, sticky, dauby, slippery'.\",\n          \"derivation_fa\": \"انگلیسی باستان slīm «گِل نرم، لجن» از ژرمنی آغازین *slīmaz است (نورس باستان slím، هلندی میانه slijm، آلمانی Schleim) و به گونهٔ s-دار همین ریشه (*slei-) بازمی‌گردد؛ واکهٔ کشیدهٔ ī از حنجره‌ای پایانی ریشه پدید آمده و پسوند -m- همان *-mo- است که در لاتینی līmus (< *loi-mo-) نیز دیده می‌شود. معنایی که نورایی می‌دهد («گِل») همان برگردان انگلیسی باستان در اتیمانلاین و آکسفورد است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/slime\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1216\", \"status\": \"supports\", \"note\": \"AHD:1216 is the main-dictionary page for SLIME in the 1975 New College edition; the corresponding root entry, Watkins s.v. lei- (AHD_watkins1985.txt l. 671), reads '1. Germanic *sli- with various extensions in: a. Old English slim, slime: SLIME'. Word, language and root as drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. slime, n. (KLN_1971.txt l. 224085)\", \"stance\": \"supports\", \"note\": \"'ME. slim, fr. OE. slim, which is rel. to ON. slim, Dan. slim, Du. slijm, MHG. slim, G. Schleim, “slime”, OHG. slimen, “to make smooth”, fr. I.-E. base *(s)lei-, “slime, slimy, sticky, dauby, slippery”.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 389\", \"stance\": \"supports\", \"note\": \"OE/ON slīm is listed among the s-mobile continuants of lei- 3.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt l. 27038)\", \"stance\": \"supports\", \"note\": \"'ON, OE slim ‘slime’' cited under IE *lei-, *slei-.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"slime\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Modern English slime continues ME slim directly from OE slīm of the parent node, with the regular Great Vowel Shift of ME ī > /aɪ/ and the orthographic final -e; the meaning has narrowed from 'soft mud' to 'viscous, unpleasant substance' but the word has never been borrowed or reformed.\",\n          \"derivation_fa\": \"انگلیسی امروزی slime دنبالهٔ مستقیم انگلیسی میانهٔ slim از انگلیسی باستان slīm گرهٔ بالادست است؛ ī انگلیسی میانه در «جابه‌جایی بزرگ واکه‌ها» به /aɪ/ بدل شده و «ـه» پایانی تنها املایی است. معنی از «گِل نرم» به «مادهٔ چسبناک و ناخوشایند» باریک شده، ولی واژه هرگز وام‌گرفته یا بازساخته نشده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/slime\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins index (AHD_watkins1985.txt l. 2269): 'SLIME lei-'; the root entry ends the chain '...Old English slim, slime: SLIME'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. slime, n. (KLN_1971.txt l. 224085)\", \"stance\": \"supports\", \"note\": \"'ME. slim, fr. OE. slim' — the same unbroken chain.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"silent\", \"note\": \"The concise Skeat's OCR (SKT.txt) breaks up in the sl- range; no usable 'slime' headword could be read (the surrounding entries slim, slip, slit are there).\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"limere; lîmus\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"limere : to smear\",\n          \"correct_form\": \"linere\",\n          \"derivation\": \"The second word is right: Lat. līmus m. 'mud, slime, mire' < *loi-mo-, cognate with OHG leim / Ger. Lehm 'loam' and OE lām — Ernout-Meillet, 'limus, -i m.: limon, boue, vase ... Cf. v.isl. lím, v.h.a. slīm \\\"boue\\\", et sans doute gr. λειμών, λίμνη'. The first word is a misprint: Latin has no verb *limere 'to smear'; the verb is linere (linō, lēvī, litum, linere) 'to daub, besmear, anoint', the nasal-infix present *li-n-H- of this very root. That this is the intended word is certain because Nourai cites POK:662, and Pokorny p. 662 prints 'Latin lino, -ere, levī ... \"daub, besmear, anoint\"' immediately before līmus. The printed page of the book (high-resolution render of PDF p. 305) plainly reads 'limere', so the extraction is faithful and the slip is the author's — probably a contamination with the unrelated Latin līmāre 'to file' (from līma 'file') or a simple n/m misreading of his source.\",\n          \"derivation_fa\": \"واژهٔ دوم درست است: لاتینی līmus «گِل، لجن، لای» از *loi-mo- و هم‌ریشه با آلمانی کهن leim / آلمانی Lehm «رُس» و انگلیسی باستان lām؛ ارنو و مه‌یه می‌نویسند «limus, -i m.: limon, boue, vase» و ایسلندی کهن lím و یونانی límnē را برای مقایسه می‌آورند. اما واژهٔ نخست غلط چاپی است: در لاتینی فعلی به شکل *limere با معنی «اندودن» وجود ندارد؛ فعل درست linere است (linō, lēvī, litum, linere) «اندودن، مالیدن»، یعنی همان صورت حال با میان‌وند خیشومی *li-n-H- از همین ریشه. اینکه مقصود همین بوده مسلّم است، چون خود نورایی به پوکورنی ص ۶۶۲ ارجاع می‌دهد و پوکورنی درست پیش از līmus «Latin lino, -ere, levī» را آورده است. تصویر پرتفکیک صفحهٔ ۳۰۵ نشان می‌دهد که کتاب «limere» چاپ کرده؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن (احتمالاً آمیختگی با līmāre «سوهان زدن» یا بدخوانی n/m).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/limus\",\n            \"https://www.etymonline.com/word/slime\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:662\", \"status\": \"partial\", \"note\": \"Pokorny 662 (POK_full.txt l. 54722-54725) has BOTH of Nourai's meanings but not his first form: 'Latin lino, -ere, levī ... līnio, -īre “daub, besmear, anoint, to spread or rub over”' and 'Latin līmus “earth mud, sludge, ordure, smut” (*loimos) = Old High German leim “loam, clay”'. The page supports the arrow; it contradicts the printed spelling 'limere'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. lino and s.v. limus (LAT.txt ll. 34110, 34012)\", \"stance\": \"partial\", \"note\": \"'lino, -is, leuī ... litum, linere (attesté depuis Naevius) ... enduire' — the verb is linere, never *limere; and 'limus, -ī m.: limon, boue, vase. - Depuis Plaute ... Cf. v.isl. lím, v.h.a. slīm “boue”, et sans doute gr. λειμών ... λίμνη “marais”.' Note that E-M's separate headword 'limus, -a, -um: oblique' is a different word, not relevant here.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. lei- (AHD_watkins1985.txt l. 671)\", \"stance\": \"partial\", \"note\": \"'2. Suffixed form *lei-mo- in Latin limus, slime ... 4. Extended form *(s)leiə- in: a. nasalized zero-grade form *li-n-ə- in Latin linere, to anoint: LINIMENT.' Both of Nourai's intended words, again spelled linere.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 389 (WLD_Bd2_pages.txt l. ~25724)\", \"stance\": \"partial\", \"note\": \"'lat. linō, -ere, lēvī ... lītum „beschmieren, bestreichen“' and 'Lat. līmus „Bodenschlamm, Kot, Schmutz“ (*loimos) = ahd. leim „Lehm“'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt l. 27038)\", \"stance\": \"partial\", \"note\": \"'cf. Lat. limus ‘mud, mire’ ... Lat. linere ‘smear’' — the same pair, correctly spelled.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T23:10:28.201Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-305.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T23:10:31.297Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-305.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 305",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-06T23:10:34.096Z] TOOL RESULT

```
Exit code 1
Expecting ',' delimiter: line 232 column 452 (char 31237)
```


## [2026-09-06T23:10:37.931Z] TOOL CALL #71: Bash

```json
{
 "command": "sed -n 232p data/verification/page-305.json | cut -c400-520",
 "description": "Inspect broken line"
}
```


### [2026-09-06T23:10:37.970Z] TOOL RESULT

```
e verb here — 'ai. līnāti (gramm.), layate, līyate, līyati "schmiegt sich an, liegt an, bleibt stecken"' — beside
```


## [2026-09-06T23:10:44.774Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\np='data/verification/page-305.json'\ns=open(p,encoding='utf-8').read()\ns=s.replace('layate, līyate, līyati \"schmiegt sich an, liegt an, bleibt stecken\"','layate, līyate, līyati «schmiegt sich an, liegt an, bleibt stecken»')\ns=s.replace('v.h.a. \\\\\"slīm\\\\\" \\\\\"boue\\\\\"','v.h.a. slīm «boue»')\ns=s.replace('v.h.a. \"slīm\" \"boue\"','v.h.a. slīm «boue»')\nopen(p,'w',encoding='utf-8').write(s)\nEOF\npython3 -m json.tool data/verification/page-305.json > /dev/null && echo \"JSON OK\"",
 "description": "Fix stray quotes in JSON"
}
```


### [2026-09-06T23:10:46.634Z] TOOL RESULT

```
Exit code 1
Expecting ',' delimiter: line 291 column 598 (char 37802)
```


## [2026-09-06T23:10:49.244Z] TOOL CALL #73: Bash

```json
{
 "command": "sed -n 291p data/verification/page-305.json | cut -c540-700",
 "description": "Inspect next broken line"
}
```


### [2026-09-06T23:10:49.289Z] TOOL RESULT

```
 Nourai cites POK:662, and Pokorny p. 662 prints 'Latin lino, -ere, levī ... "daub, besmear, anoint"' immediately before līmus. The printed page of the book (h
```


## [2026-09-06T23:10:52.602Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 - <<'PY'\np='data/verification/page-305.json'\ns=open(p,encoding='utf-8').read()\ns=s.replace(\"'Latin lino, -ere, levī ... \\\"daub, besmear, anoint\\\"'\",\"'Latin lino, -ere, levī ... «daub, besmear, anoint»'\")\nopen(p,'w',encoding='utf-8').write(s)\nPY\npython3 -m json.tool data/verification/page-305.json > /dev/null && echo \"JSON OK\"",
 "description": "Fix remaining stray quotes"
}
```


### [2026-09-06T23:10:54.292Z] TOOL RESULT

```
JSON OK
```


## [2026-09-06T23:10:56.286Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 tools/verify_check.py 305",
 "description": "Run verify_check for page 305"
}
```


### [2026-09-06T23:10:59.640Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'plausible': 3, 'confirmed': 8, 'transcription_suspect': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'not_checked': 3, 'partial': 1}
books consulted: {'partial': 8, 'silent': 7, 'supports': 21, 'contradicts': 1} | by book: {'SYN': 7, 'KLN': 7, 'WLD': 5, 'SKT': 4, 'BQT': 2, 'HRN': 2, 'PHD': 2, 'LAT': 2, 'HUB': 1, 'BRT': 1, 'MON': 1, 'ARY': 1, 'POK': 1, 'AHD': 1}
```


## [2026-09-06T23:11:17.058Z] AGENT

Page 305 (book p. 275) verified — `data/verification/page-305.json` written, `verify_check.py 305` reports 13/13 nodes, **0 PROBLEM lines**.

**Counts:** roots 2 confirmed · nodes 8 confirmed, 3 plausible, 2 transcription_suspect · ref_check 10 supports / 1 partial / 3 not_checked · consulted 21 supports / 8 partial / 7 silent / 1 contradicts.

**transcription_suspect (both `error_in: "book"` — the extraction is faithful):**
- **Legwh / Latin node 5** — page prints `levâr : lift`; correct form is Latin **levāre** (the next line in the same box prints `carni-levâre` correctly; Watkins: "levis … with its derivative levāre"). Nourai's misprint.
- **Lěi, Lôi / Latin node 5** — page prints `limere : to smear`; Latin has no *limere*, the verb is **linere** (linō, lēvī, litum). Pokorny 662 — the page Nourai himself cites — prints "lino, -ere". Nourai's misprint (līmus 'slime' on the same line is correct).

**plausible (not disputed, but under-supported):**
- Persian **لاغر lāḡar** — rests on Mann IEC:700 alone (*l̥ngʷʰ-ro-); initial l- and the غ are irregular for an inherited Iranian word, no attested MP form, Horn/Hübschmann/MacKenzie silent, Mo'in's Borhan footnote gives only dialect cognates. Wiktionary's identical chain cites Mann **and Nourai himself**, so it is not independent.
- Persian **لای lāy** — again Mann IEC:706 alone, and Mann flags it "Vowel ambig."; Borhan confirms the sense exactly but gives no etymology; Wiktionary's etymology section is explicitly incomplete.
- **French carnaval** — right etymon, abbreviated route: it came Latin → **Italian carnevale** → French (Skeat labels it "F.-Ital.-L."), not Latin → French as drawn.

**Extraction errors for the owner:** none. Two notes: (a) MON:3530 and VOP:269 are unreachable (Mo'in's print pagination isn't online and the local OCR is gibberish; Moshiri's VOP has no copy anywhere) — recorded as `not_checked`; (b) an entirely **empty box** hangs off the Avestan node on the printed page — no label, no words, a layout artifact; the JSON correctly omits it.

Also worth flagging: **Klein contradicts Nourai on *carnival*** (he gives the folk etymology ML *carne, vale* "flesh, farewell"), but Skeat and Etymonline back Nourai's *carnelevāre*. Page image saved to `data/verification/sources/refs/ocr/BOOK/305.png`; 10 web pages archived via `fetch_source.py`.
