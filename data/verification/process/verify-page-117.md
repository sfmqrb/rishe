# Verification process log — verify-page-117


## [2026-09-05T17:49:41.799Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 117 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-117.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-117.json. Write /home/sfmqrb/git/rishe/data/verification/page-117.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 117` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T17:49:43.310Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T17:49:44.029Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T17:49:44.042Z] TOOL RESULT

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


## [2026-09-05T17:49:44.217Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-117.txt"
}
```


### [2026-09-05T17:49:44.230Z] TOOL RESULT

```
1	=== PDF page 117 (book page 87) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dema : to tame and domesticate animals  (refs POK:199; KLN:442)
4	#1 (parent #0) [Avestan] refs=BQT:817 | dâman 1 : domestic animals
5	  #2 (parent #1) [Persian] refs=KLN:1569; POK:199; BQT:817 | dâm «دام ۱» : domestic animals | extra: دامداری ، دامپزشکی ، دامپروری
6	#3 (parent #0) [Greek] refs=AHD | daman : to tame, conquer ; a-damas : unconquerable, hard stone
7	  #4 (parent #3) [Pahlavi] refs=BQT:159; MON:342 | almâs : hard stone
8	    #5 (parent #4) [Persian] refs=None | almâs «الماس» : diamond
9	  #6 (parent #3) [Latin] refs=AHD:364; KLN:442 | adamas, diamas : hard stone
10	    #7 (parent #6) [English] refs=None | diamond
11	#8 (parent #0) [Germanic] refs=AHD | tamaz : tame
12	  #9 (parent #8) [English] refs=None | tame
13	--- entry 1 ---
14	ROOT [Indo-European] Denk : to bite  (refs POK:201)
15	#1 (parent #0) [Avestan] refs=POK:201; BQT:884; SYN:138 | danta : tooth ; daitika : wild (biting) animals
16	  #2 (parent #1) [Persian] refs=BQT:884; BRT:653; HRN:120 | dandân «دندان» : tooth ; dandeh «دنده» : rib ; dad «دَد» : wild animal
17	#3 (parent #0) [Sogdian] refs=SOD:145 | dt : wild (biting) animal
18	#4 (parent #0) [Germanic] refs=AHD | tangus : tongs ; tanhuz : holding tight ; teng : spiky
19	  #5 (parent #4) [English] refs=None | tongs ; tough ; zinc
20	--- entry 2 ---
21	ROOT Děnu -> redirect to Dînu
22	
```


## [2026-09-05T17:49:47.425Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-117.json",
 "description": "Read source JSON for page 117"
}
```


### [2026-09-05T17:49:47.478Z] TOOL RESULT

```
{
  "pdf_page": 117,
  "book_page": 87,
  "entries": [
    {
      "root": {
        "name": "Dema",
        "lang": "Indo-European",
        "refs": "POK:199; KLN:442",
        "gloss": "to tame and domesticate animals"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:817",
          "words": [
            {"translit": "dâman 1", "gloss": "domestic animals", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "KLN:1569; POK:199; BQT:817",
          "words": [
            {"translit": "dâm", "gloss": "domestic animals", "script": "دام ۱"}
          ],
          "script_extra": "دامداری ، دامپزشکی ، دامپروری",
          "note": null,
          "quote": {"text": "پذیرندهٔ هوش و رأی و خرد - مر او را دَد و دام فرمان برد", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "daman", "gloss": "to tame, conquer", "script": null},
            {"translit": "a-damas", "gloss": "unconquerable, hard stone", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "BQT:159; MON:342",
          "words": [
            {"translit": "almâs", "gloss": "hard stone", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "almâs", "gloss": "diamond", "script": "الماس"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Latin",
          "refs": "AHD:364; KLN:442",
          "words": [
            {"translit": "adamas, diamas", "gloss": "hard stone", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "diamond", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "tamaz", "gloss": "tame", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "tame", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Denk",
        "lang": "Indo-European",
        "refs": "POK:201",
        "gloss": "to bite"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:201; BQT:884; SYN:138",
          "words": [
            {"translit": "danta", "gloss": "tooth", "script": null},
            {"translit": "daitika", "gloss": "wild (biting) animals", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:884; BRT:653; HRN:120",
          "words": [
            {"translit": "dandân", "gloss": "tooth", "script": "دندان"},
            {"translit": "dandeh", "gloss": "rib", "script": "دنده"},
            {"translit": "dad", "gloss": "wild animal", "script": "دَد"}
          ],
          "note": null,
          "quote": {"text": "هیچ کنجی بی دد و بی دام نیست - جز به خلوتگاه حق آرام نیست", "poet": "Molavî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:145",
          "words": [
            {"translit": "dt", "gloss": "wild (biting) animal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "tangus", "gloss": "tongs", "script": null},
            {"translit": "tanhuz", "gloss": "holding tight", "script": null},
            {"translit": "teng", "gloss": "spiky", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "tongs", "gloss": null, "script": null},
            {"translit": "tough", "gloss": null, "script": null},
            {"translit": "zinc", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Děnu",
        "redirect": "Dînu"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T17:49:48.142Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---\" && ls tools/",
 "description": "List verification dir and tools"
}
```


### [2026-09-05T17:49:48.181Z] TOOL RESULT

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
---
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


## [2026-09-05T17:49:51.331Z] TOOL CALL #5: Bash

```json
{
 "command": "head -100 data/verification/page-112.json",
 "description": "Sample existing verification file"
}
```


### [2026-09-05T17:49:51.371Z] TOOL RESULT

```
{
  "pdf_page": 112,
  "book_page": 82,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Deik",
      "verdict": "confirmed",
      "modern_form": "PIE *deyḱ- 'to show, point out' (Pokorny 188 deiḱ- 'zeigen'; Walde-Pokorny I 776; Watkins/AHD deik- 'to show, pronounce solemnly'; LIV² 108-109)",
      "note": "The root box is right on all three counts. Pokorny p.188 heads the entry 'deik- ,zeigen', woraus lat. und germ. z. T. ,mit Worten auf etwas hinweisen, sagen'', so the reconstruction, the label 'Indo-European' and the gloss 'to show' are exactly what the standard handbooks give. Two refinements a reader should know. (a) The root has a doublet *deig- (Pokorny: 'Daneben idg. doig- in got. taikns ... ags. tǣcan, engl. teach'); Nourai's Germanic branch (node 3) in fact belongs to that variant, and AHD explicitly files TEACH/TOKEN under 'Variant *deig-'. (b) The whole chart, including its wording, is copied from the AHD (Watkins) appendix entry deik-, which reads: 'deik-. To show, pronounce solemnly ... 1. O-grade form *doig- in: a. Germanic *taikjan, to show ... 2. Latin digitus, finger (< \"pointer\") ... 4. Agential suffix *-dik- in: a. Latin index ... b. Latin jūdex ... 6. Zero-grade form *dik- in Greek dikein, to throw (< \"to direct an object\"): DISK. [Pok. deik- 188.]' Nourai's node glosses are Watkins' glosses verbatim. That also means the chart inherits Watkins' weakest link, the Greek dikein/diskos branch (see nodes 9-12), and one plain error, 'discuss' (node 12). No Persian branch is affected by that: the Avestan → Persian dīs/dīz line (nodes 1-2) is the well-attested part.",
      "note_fa": "ریشهٔ هندواروپایی آغازین *deyḱ- «نشان دادن، نمودن» ریشه‌ای اصیل و پذیرفته‌شده است؛ پوکورنی در صفحهٔ ۱۸۸ همین صورت و همین معنی را می‌آورد («deik- ,zeigen'») و والده-پوکورنی (جلد ۱، ص ۷۷۶) و پیوست واتکینز در فرهنگ American Heritage نیز همان را دارند. پس برچسب زبانی و معنای جعبهٔ ریشه در نمودار نورایی درست است. دو نکته: نخست آنکه این ریشه گونهٔ دیگری به صورت *deig- دارد و شاخهٔ ژرمنی نمودار (گرهٔ ۳) در حقیقت از همان گونه است، نه از *deik- ساده. دوم آنکه سراسر این نمودار، حتی معناهای انگلیسی گره‌ها، واژه‌به‌واژه از مدخل deik- در پیوست واتکینز برداشته شده است؛ از این رو ضعف همان مدخل — یعنی پیوند یونانی dikein و diskos — به نمودار نورایی هم راه یافته و یک خطای آشکار («discuss» در گرهٔ ۱۲) نیز از همان‌جا آمده است. بخش ایرانی نمودار (اوستایی daēs- ← فارسی دیس/دیز) استوارترین بخش آن است.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deyḱ-"
      ],
      "ref_check": [
        {
          "ref": "POK:188",
          "status": "supports",
          "note": "POK_01.txt, form-feed leaf 197 (= printed p.188; the page numeral 189 follows inside the entry): 'deik- ,zeigen', woraus lat. und germ. z. T. ,mit Worten auf etwas hinweisen, sagen', mehrfach auch ,das Recht weisen, auf den Täter hinweisen, beschuldigen' entwickelt; Partiz. Pass. dik-tó-s; dikā ,Richtung', dik-ti- ,Anweisung', deiko-s ,Richtung'.' The page number Nourai cites is exact."
        }
      ],
      "consulted": [
        {
          "src": "WLD",
          "where": "Bd. I p.776 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt line 48927)",
          "stance": "supports",
          "note": "'deik- „zeigen\", woraus lat. und germ. z. T. „mit Worten auf etwas hinweisen, sagen\", mehrfach auch zum gerichtlichen Sinn „auf den Täter hinweisen, beschuldigen\" entwickelt.' — Pokorny's 1959 entry is a reprint of this; Pokorny himself refers to 'WP. I 776 f.'"
        },
        {
          "src": "AHD",
          "where": "AHD_watkins1985.txt line 360, s.v. deik-",
          "stance": "supports",
          "note": "'deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. ... [Pok. deik- 188.]' — Watkins' gloss and Pokorny reference are identical to Nourai's root box."
        },
        {
          "src": "IEC",
          "where": "IEC.txt line 2109, s.v. deikō",
          "stance": "supports",
          "note": "'deikó (deiKnu-, diK-) \"show, tell\". Cf. deiKs-, diK-. WP I, 776. Skt. cf. diśāmi; Oss. cf. dis, des \"marvel\", áv-disín, -desun \"show\"; Hitt. cf. tekkusami; Gk. deíknumi; Lat. dico; Osc. inf. deíkum; Go. ga-teihan \"announce\"' — Mann reconstructs the same root with the same meaning."
        },
        {
          "src": "SYN",
          "where": "SYN.txt concept 15.55 SHOW (vb.), section 1",
          "stance": "supports",
          "note": "'1. IE deik-. Walde-P. 1.776. Ernout-M. 265 ff. Walde-H. 1.348 f. Here as \"show\": Grk. δείκνυμι ... Skt. diś-, Av. diś-; cf. in secondary sense Lat. dicere \"say\" ... Goth. ga-teihan \"announce\"'. Buck adds the semantic key Nourai's chart depends on: 'it seems likely that the primary notion was \"point (as with the finger), point out\"'."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
          "words": "daěs",
          "verdict": "confirmed",
          "derivation": "Avestan daēs- 'to show' is a real, well-attested verb: Bartholomae, Altiranisches Wörterbuch cols. 671-674, lists it as 'daēs- V. \"zeigen\". Praes. daēdōiš-, (auch Pass.) disya-, (Iter.) daēsaya-, s-Aor. dāiš-, dōiš- : diš-', with the senses '1) jemandem (Gen.) etwas (Akk.) zeigen, sehen lassen; 2) jemandem (Dat.) etwas zuweisen, zusprechen; 3) jemanden unterweisen, belehren; 4) kundmachen'. It is the regular Iranian continuant of PIE *deyḱ-: Proto-Indo-Iranian *daiś- gives Vedic diśáti / dideṣṭi 'shows' and Av. daēs- exactly (the Avestan e-grade daē- < *dai- < PIE *dei-, with the palatal *ḱ appearing as Iranian s, Skt. ś — the satem outcome). Nourai's transliteration 'daěs' uses his own diacritic for the ē of daēs-; the gloss 'to show, demonstrate' is Bartholomae's 'zeigen' plus 'kundmachen'. The one imprecision is that Nourai writes the bare root without the hyphen the Iranists use.",
          "derivation_fa": "فعل اوستایی -daēs «نمودن، نشان دادن» واژه‌ای اصیل و پرکاربرد در اوستاست؛ بارتولومه در «فرهنگ ایرانی باستان» (ستون‌های ۶۷۱ تا ۶۷۴) آن را چنین ثبت کرده است: «daēs- فعل: نشان دادن»، با ستاک‌های حال daēdōiš-، disya- و daēsaya- و آاوریست dāiš-/dōiš-، و معناهای «چیزی را به کسی نشان دادن»، «چیزی را به کسی واگذاردن»، «کسی را آموختن» و «آشکار کردن». این فعل بازماندهٔ منظم ریشهٔ هندواروپایی *deyḱ- در ایرانی است: در هندوایرانی آغازین *daiś- شده و در سنسکریت diśáti و در اوستایی daēs- بازتاب یافته؛ همخوان کامی *ḱ در زبان‌های ساتم (از جمله ایرانی) به s / ś بدل شده است. ضبط نورایی («daěs») همان daēs- است با نشانهٔ ویژهٔ خودِ او برای ē. ادعای نورایی در این گره درست است.",
          "sources": [
            "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deyḱ-"
          ],
          "ref_check": [
            {
              "ref": "POK:188",
              "status": "supports",
              "note": "POK_01.txt leaf 197 (p.188), inside the deik- entry: 'Ai. dideṣṭi, diśáti, deśayati ,zeigt, weist', av. daēs- Aor. dōiš- ,zeigen' (daēsayeiti, disyeiti, daēdōišt) ,zeigen; jemandem etwas zuweisen, zusprechen''. Pokorny's page therefore does carry the Avestan verb exactly as Nourai draws it under the root."
            }
          ],
          "consulted": [
            {
              "src": "BRT",
              "where": "BRT.txt cols. 671-674 s.v. daēs-",
              "stance": "supports",
              "note": "'daēs- V. \"zeigen\". Praes. daēdōiš-, (auch Pass.) disya-, (Iter.) daēsaya-, s-Aor. dāiš- / dōiš- : diš-.' followed by the four attested senses with Yasna/Vendidad citations (Y 43.10, Y 51.2, V 5.14, Yt 11.14)."
            },
            {
              "src": "CHEUNG",
              "where": "CHEUNG.txt line 4397 ff., root *daiš¹ 'to show'",
              "stance": "supports",
              "note": "'*daiš¹ \"to show\". AVESTAN: daēs- \"to show\" || (+ *fra-) \"to show\" || (+ *ham-) \"to be told, be shown\" — Liste: 30'; Cheung's Etymological Dictionary of the Iranian Verb then traces it into MP uzdēs 'idol', handēs- 'to think', Parthian ʾdysg 'sign'. This is the current standard treatment of the verb."
            },
            {
              "src": "AHD",
              "where": "AHD_watkins1985.txt line 360 s.v. deik-",
              "stance": "silent",
              "note": "Watkins' appendix lists no Iranian reflex at all (only Latin, Greek and Germanic), so Nourai's Avestan node comes from Pokorny, not from AHD, even though he tags the Germanic/Latin/Greek nodes 'AHD'."
            }
          ]
        },
        {
          "id": 2,
          "lang": "Persian",
          "words": "dîs, dîz",
          "verdict": "plausible",
          "derivation": "The chart's two Persian forms need to be judged separately. (a) -dīs / -dēs 'resembling, having the shape of' is solidly derived from Av. daēs-: Av. daēsa- m. 'Zeichen, Omen' (Bartholomae col. 673) → Middle Persian dēs / dēsag [dys(k)] 'form, appearance' (MacKenzie, Concise Pahlavi Dictionary p.22 'dēs(ag) [dys(k)| M dys] form, appearance'; Nyberg II p.64 'dēs [dys] shape, form ... MPrs dys; NP -dēs, e.g. māh-dēs \"moon-like\" ... From daēs-') → New Persian -dīs, the bound second member of تندیس tandīs 'body-shape' = statue, طاقدیس tāqdīs 'arch-shaped' (Khosrow's throne), فرخاردیس, خایه‌دیس 'egg-shaped'. The Middle Persian ē regularly raises to New Persian ī (majhūl ē > maʿrūf ī in the eastern/modern reading), which is why the book prints dīs beside the older dēs. The same daēs- gives MP uzdēs 'idol' (lit. 'image, thing shown'), Parthian ʾdysg 'sign'. (b) دیز dīz 'black, (dark) colour', as in شبدیز šabdīz, Khosrow Parvēz's black horse (Nezāmī's line quoted by Nourai) and دیزه dīza 'dark grey (horse)', is only tentatively attached here: Moʿin's footnote at Borhān-e Qāṭeʿ p.912 reports it as Pūrdāvūd's conjecture ('شاید «دیز» از کلمهٔ daēsa- باشد … بنابراین شبدیز لغةً بمعنی شب‌نما') and has to assume an ad-hoc s > z (he adduces اسپریس/اسپریز). So 'appearance, resemblance' is confirmed, 'color' is a conjecture. Also note the older dispute the chart hides: Horn (Grundriss no. 593, p.125) derived -dēs/-dis not from daēs- at all but from Av. darəs- / Skt. dṛś- 'to see' ('-dēs, -dis, -des \"gleichend, ähnlich\": aw. darəs- \"Blick\", ai. dṛś-'), calling Av. daēsa- 'zu unsicher, um verglichen werden zu können'. Hübschmann, whose page Nourai cites, was written expressly to overturn Horn on this point, and Bartholomae, Nyberg, MacKenzie and Cheung follow Hübschmann. Modern scholarship therefore sides with Nourai — but only for dīs.",
          "derivation_fa": "دو صورتی که نورایی در این جعبه آورده باید جدا سنجیده شود. نخست «ـ دیس» (در تندیس، طاقدیس، فرخاردیس) به معنی «همانند، به شکلِ»: این جزء به‌روشنی از daēsa- اوستایی «نشانه، نمود» می‌آید که خود از مصدر daēs- «نمودن» ساخته شده؛ در فارسی میانه dēs / dēsag «شکل، صورت» شده (مکنزی، ص ۲۲؛ نیبرگ، ج ۲ ص ۶۴: «dēs … در فارسی نو ـ دیس، مانند ماه‌دیس، از daēs-») و ای مجهولِ فارسی میانه در فارسی نو به ی معروف بدل شده و «ـ دیس» به دست آمده است. از همین ریشه است uzdēs پهلوی «بت» (یعنی «نمود، تصویر») و ʾdysg پارتی «نشانه». دوم «دیز» به معنی سیاه و رنگ (در شبدیز، دیزه): این پیوند تنها گمانی است؛ معین در حاشیهٔ برهان قاطع (ص ۹۱۲) آن را از قول پورداود می‌آورد («شاید دیز از کلمهٔ daēsa- باشد … بنابراین شبدیز لغةً بمعنی شب‌نما») و ناچار است ابدال س به ز را با نمونهٔ اسپریس/اسپریز توجیه کند. نکتهٔ سوم آنکه هرن در «بنیاد ریشه‌شناسی فارسی نو» (شمارهٔ ۵۹۳، ص ۱۲۵) این «ـ دیس» را نه از daēs- بلکه از darəs- اوستایی و dṛś- سنسکریت «دیدن» می‌گرفت و daēsa- را «نامطمئن‌تر از آن» می‌دانست که بتوان سنجید؛ هوبشمان همان صفحه‌ای را که نورایی ارجاع می‌دهد برای رد نظر هرن نوشت و بارتولومه و نیبرگ و مکنزی و چونگ نیز از هوبشمان پیروی کرده‌اند. پس ادعای نورایی دربارهٔ «دیس» پذیرفتنی و امروزه پذیرفته است، ولی «دیز» با احتیاط.",
          "sources": [
            "https://en.wiktionary.org/wiki/تندیس"
          ],
          "ref_check": [
            {
```


## [2026-09-05T17:49:51.948Z] TOOL CALL #6: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T17:49:51.987Z] TOOL RESULT

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


## [2026-09-05T17:50:16.252Z] AGENT

Now let me research. Starting with the IE roots in Pokorny, Walde-Pokorny, AHD.


## [2026-09-05T17:50:18.446Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK grep dem ===\"\ngrep -n \"demā-\\|dem-, demə\\|,zähmen\\|zähmen'\" POK_01.txt | head -20\necho \"=== POK grep denk ===\"\ngrep -n \"denk-\\|denḱ-\\|deṇk\" POK_01.txt | head -20",
 "description": "Grep Pokorny for dem- and denk-"
}
```


### [2026-09-05T17:50:18.508Z] TOOL RESULT

```
=== POK grep dem ===
2872:Eine  alte  Abzweigung  unserer  Wz.  ist  demä-  , zähmen',    ursprgl.   wohl j^ns  Haus  fesseln,  domestizieren'. WP.  I  786ff.;  WH.  I  367,  369 f.,   Schwjzer  Gr.  Gr.  I  480,  524,  547 f., ^625,  Trautmann  44.
2873:tdcmO'),  domQ'f  dotnQ-  ,zähmen,  bändigen';  Partiz.  Pass.  dm-tö-s,  doms-tö-s; domo-s  und  dotno-s  ,zahmes  Tier,  zahm',  dotnio-s  ,junger,  zu  zähmen- J^  der  Stier',  domo-tor-  , Bezwinger',  domo-tu-  , Bändigung'.
2875:osset.  domun  , zähmen',  npers.  dam  ,zahmes  Tier';  nach  Pisani  Crest. Indeur.2  113  hierher  (als  *dM-sO's)  däsd-h  , Feind,  Nicht- Arier',  eigentl. , Sklave',  aber  wegen  der  Stammbildung  unglaubhaft;
2880:air.  damnaim  ,binde  (fest),  bändige  (Pferde)',  Verbalnom.   damnad  u^H domnad  (wohl  =  gr.  ödfirrj^n)]  lautliche  Vermischung  mit   damnaim  a^J lat.  damnö,   der  wohl  auch   das  unlenierte  m  des  Partiz.  dammainti  entS Sprüngen   ist;    air.    dam-   ,sich    fügen,    erleiden,    gewähren'    (z.  B.    daimi^ , gesteht  zu'  Avohl  =  ai.  dämydti,  komponiert  ni-daim  _,non  patitur'j  Pei-f dämair  aus   Dehnst.   *döm-)j  mit  acZ-  ,gestehen'  (z.  B.  3.  PI.  ataimet)j  mj^ /o-  , erleiden'  (z.  B.  1.  Sg.  fo-daimim\  cymr.  addef,  bret.  aHsav  ,gestehen' acymr.    ??i    ceiw    guodeimisauch    Gl.    ,non    bene    passae',    ncymr.    go-ddef ,leiden,  erlauben',  corn.  gothaf  , ertragen',  bret.  gouzafiv,  gouzav  ds.  (aber cymr.  dofi  , zähmen',  acymr.  dometic  ,gezähmt',  ar-domaul  ,gelehrig',  cymr. döfj  bret.  cZq^, zahm'  stammen  aus  lat.  domäre,  so  daß  einheimische  Formen mit  0  dem  Kelt.  fehlten);
2881:got.  ga-tamjan,  anord.  temja,  ags.  temian,  mnd.  temmen,  ahd.  zemmen , zähmen'  (Kaus.  *domeiö  =  ai.  damdyati)]  ahd.  zamön  ds.  (=  lat.  domä-reY anord.  tamr,  ags.  ^aw,  ahd.  zam  ,zahm'  (unklar,  ob  Rückbildung  aus  dem Verbum,  oder  ob  die  pass.  Bed.  aus  , Zähmung  =  Gezähmtes*  erwachsen ist,  so  daß  in  geschichtlichem  Zusammenhang  mit  ai.  ddma-h  »Bändi- gung').
2882:Wegen  ai.  damya-  ,zu  zähmen'  und  ,juuger  Stier,  der  noch  gezähmt werden  soll'  und  wegen  gr.  da^ctXrig  einerseits  ,bezwingend,  bändigend' (^'Eqojg,  Anakreon),  andrerseits  ,junger  (noch  zu  zähmender)  Stier*,  avozu daf-idlr]  ,junge  Kuh',  ödixaXiq  ,ds.*;  auch  ,junges  Mädchen*,  dd^aXog  ,Kalb', ist  wohl  alb.  dente,  dhente,  ^q^.  dhent  , Kleinvieh,  Schafe'  {*dem-tä  oder *dem-to-Sj  bzw.-  *dom-tä,  -tos),  dem  ,Rind,  junger  Stier'  (=  ai.  damya-\ sowie  auch  gall.  GN  Damona  f.  und  air.  dam  , Ochse'  (*damos),  dam allaid  , Hirsch'  (,*wilder  Ochse'),  sowie  cymr.  dafad^  a.C0Tn.  dauat,  bret. daTwat  , Schaf  (dann  =  gr.  ä-dd^aTog)  anzureihen  (ursprgl.  Bezeichnungen gezähmter  Horntiere);  lat.  damma  oder  däma  ist  wohl  aus  dem  Kelt.  oder anderswoher  entlehnt;  unklar  ist  ags.  da  f.  ,Reh'  (daraus  acorn.  da  ,dama'), engl,  doe,  alem.  te  ds.,  vgl.  Holthausen  Altengl.  etym.  Wb.  68;  aus  afrz, daim  , Damhirsch'  stammt  bret.  devi  ds.;  germ.  Lehnformen  s.  bei  Falk- Torp  u.  daadyr  m.  Lit.;  entsprechend  niederösterr.  zamer,  zamerl  ,junger Ochs'  (Much  ZfdA.  42,  167;  vorgerm.  *a  oder  *o?).
=== POK grep denk ===
2747:S.  auch  unter  denk-.
```


## [2026-09-05T17:50:19.896Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD dem ===\"\ngrep -n -i \"^dem\\|^denk\\|^dent\\|demə-\\|denk-\" AHD_watkins1985.txt | head -30",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-05T17:50:19.950Z] TOOL RESULT

```
=== AHD dem ===
237:deme-1. 2. Compound form *dems-pot-...
364:LOIN. 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos, long: DOLICHOCEPHALIC, DOLICHOCRANIAL. [Pok. 5. del- 196.] del-2. To recount, count. 1. Germanic *taljan in Old English tellan, to count, recount: TELL. 2. Germanic *tal6é in: a. Old English talu, story: TALE; b. Middle Dutch dle, speech, language: TAAL. 3. Old English denominative talian, to tell, relate, probably akin to the source of Middle English talken, to talk: TALK. 4. Per- haps Greek dolos, ruse, snare: DOLERITE. [Pok. 1. del- 193.] del-3. To split, carve, cut. 1. Suffixed form *del-to- in Germanic *teldam, “thing spread out,” in Old English teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping tool (< doldre, to chisel, hew): DOLABRIFORM. [Pok. 3. del- 194.] del-*. To drip. Perhaps suffixed (stative) o-grade form *dol- in Germanic *talgaz in Middle Low German falg, talch, tallow (< “dripping fat”), perhaps akin to the source of Middle English talow, tallow: TALLOw. [Pok. 4. del- 196.] deme-'. Also dem-. House, household. 1. Suffixed re- duced o-grade form *dom-o-, dom-u-, house, in: a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJOR- DOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN?, DANGER, DoM, DOMAIN, DOMI- NATE, DOMINICAL, DOMINIE, DOMINION, DOMINO}, (DOM- INO2), DUENNA, DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE. 2. Com- pound *dems-pot-, “house-master” (*-pot-, powerful; see poti-), in Greek despotés, master, lord: DESPOT. 3. Root form *dem()-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumfté in Old Norse topt, homestead: Torr. [Pok. dem- 198.] deme-2. To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
1419:DEMENT men-1 DEMETER mater- DEMILUNE leuk- DEMIT (s)meit(a)- DEMIURGE da-, werg- DEMOCRACY da- DEMOLISH mé6- DEMON da- DEMONSTRATE men-! DEMOPHOBIA da- DEMOS da- DEMOTIC da- DEMUR mere- DEN dan- DENARIUS dekm DENARY dekm DENDRO- deru DENDRON deru DENIER? dekm DENIGRATE negW-ro- DENOMINATE no-men- DENOUEMENT ned- DENOUNCE neu-! DENSE dens-2 DENTAL dent- DENTATE dent- DENTI- dent- DENTICLE dent- DENTIFRICE bhréi- DENUDE nogw- DENY ne
2336:TaaL del-2 TABES ta- TACET tak-1 TACHE dek-? TACHISM deik- TACHYLYTE leu-! TACHYPNEA pneu- TACIT tak-1 Tack! dek-2 TACT tag- TACTICS tag- TACTORECEPTOR tag- TAEL tele- TAENIA ten- TAFFETA temp- TAG! dek-2 TAHSILDAR dher-2 TAIL! dek-2 TAINT teng- Tad (s)teg- TAKE tak-2 TALE del-2 TALENT tela- TALES to- TALION tele- TALISMAN kWel-1 TALK del-2 TALLOW del-4 TAME deme-2 TAMPON tap- TANDEM to- TANG! denk- TANGENT tag- TANGIBLE tag- TANGLE? tenk-2 TANGORECEPTOR tag- TANSY dhwene- TANTALIZE tele- TANTALUS tele- TANTAMOUNT to- TANTRA ten- Tap! tap-
2361:TERRESTRIAL ters- THRESH tera-! TORTICOLLIS kWel-1, terkw- TRICERATOPS ker-1 TERRE-VERTE ters-, virére THRESHOLD tere-1 TORTUOUS terkw- TRICHINA  thrix TERRIBLE tres- THRICE trei- Tory ret- TRICHO-  thrix TERRICOLOUS ters- THRILL tere-2 TOTAL teuta- TRICHOME _ thrix TERRIER ters- THRONE dher-2 TOUGH denk- TRICHOTOMY _ trei- TERRIFIC tres- THROSTLE trozdo- TOUPEE tap- -TRICHOUS _ thrix TERRIGENOUS §ters- THROUGH tere-2 Tow! deuk- TRICHURIASIS ors- TERRITORY ters- THROW tere-1 Tow? taw- TRICLINIUM klei-, trei- TERROR tres- THRUM?2 ter- TOWN dhino- TRICORN ker-1 TERTIAN trei- THRUSH! trozdo- TOXIC tekw- TRICROTIC  kret-2, trei-
2395:TOFT deme-1 TOGA (s)teg- TOGETHER ghedh- TOIL! (s)teu- TOIL? teks- TOKEN deik- TOLA tele- TOLERATE tele- TOLL! tele- TOMB teue- TOME tem- -TOMY tem- TONE ten- TONGS denk- TONGUE dnghi TONOPLAST ten- TONSURE tem- Too de-
```


## [2026-09-05T17:50:30.915Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=2865 && NR<=2890' POK_01.txt | head -40",
 "description": "Print Pokorny dem- context"
}
```


## [2026-09-05T17:50:32.278Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK page 199 leaf ===\"\ngrep -n \"denk-\" POK_01.txt | head; echo \"---beissen---\"; grep -n \"beißen\\|,beissen'\" POK_01.txt | sed -n '1,25p'",
 "description": "Find Pokorny denk- entry"
}
```


### [2026-09-05T17:50:33.006Z] TOOL RESULT

```
K«    oromen);   aksl.  dovi^  m.  ,Haus*,    russ.  döma   ,zu  Hause'    (*(£owö[w]);
^  t     «..k-  iruss.  domovb  ,nach  Hause';  vorausgesetzt  auch  durch  ai.  dämü-nas-
Jbusgenosse'  und  arm.  tanu-ter  ,Hausherr';
ein   St.   *dmöu-  in   ion.  öfXibgj   Gen.   dficoög    »Kriegsgefangener,  Knecht', ^   1  ,Magd',  kret.  ^ivibä  f.  »leibeigene  Bevölkerung'; %■■   «r    *dm'ana-  in    av.  ddmnna-,   nmäna-  n.  ,Haus',   auch   ai.  mdna-h  ,Ge- §Uude,  Wohnung';
lit.  nämas,  PL  namai  ,Haus,  Wohnung'   ist  aus   ^damas  dissimiliert,  in ^  Kompositis  wie  namü-darys  , Hausbauer',  s.  WH.  I  861.
Air.   damnae   , Material',    cymr.    defnydd,   mbret.   daffnez  kann   ursprgl. B«aholz'  bedeutet  haben.
^  Toch.  B  tem-,  A  tam-^  AB  täm-  ,erzeug'en,  geboren  werden'  und  B  ts.am-j AB  tsäm-,   A   §am'j   säm-,   vielleicht   nach    Pedersen   Toch.  Sprachg.  2V '  hierher;  dazu  auch  B  c{o)mely  A  cmol  (*cmelu)  Geburt,  Van  Windekens Xiexique  51.
Eine  alte  Abzweigung  unserer  Wz.  ist  demä-  , zähmen',    ursprgl.   wohl j^ns  Haus  fesseln,  domestizieren'. WP.  I  786ff.;  WH.  I  367,  369 f.,   Schwjzer  Gr.  Gr.  I  480,  524,  547 f., ^625,  Trautmann  44.
tdcmO'),  domQ'f  dotnQ-  ,zähmen,  bändigen';  Partiz.  Pass.  dm-tö-s,  doms-tö-s; domo-s  und  dotno-s  ,zahmes  Tier,  zahm',  dotnio-s  ,junger,  zu  zähmen- J^  der  Stier',  domo-tor-  , Bezwinger',  domo-tu-  , Bändigung'.
Ai.  damydti  ,ist  zahm;  zähmt'  {*dm-ieti),,dämtd-  »gebändigt'  (^dm-tös)'^ Kaus.  damdyati  , band  igt,  bezwingt'  (^domeiö)^  Partiz.  damita--,  damitdr- jBändiger';  damitvä  , Bändigung',  damäydti  .bändigt'  (*domä-io  ==■  lat. domo)]  damd-h  , bändigend',  ddma-li  , Bändigung';
osset.  domun  , zähmen',  npers.  dam  ,zahmes  Tier';  nach  Pisani  Crest. Indeur.2  113  hierher  (als  *dM-sO's)  däsd-h  , Feind,  Nicht- Arier',  eigentl. , Sklave',  aber  wegen  der  Stammbildung  unglaubhaft;
gr.  d(X(.iva(xtj  ion.  -rj(.u^  Aor.  i-dd!.ia(a)aa  (für  *£-d€(.ta(ra)  , bändige',  viel- fach sekund.  umgestaltet,  wie  Saj-ivacj  usw.,  7t(xvSa(.idTü)Q  ,Allbezwinger', der.  dfiarög  , gebändigt'  (^dm-tös),  hom.  äS(.irjTog  und  ddt.irjg^  -fjTog  ,unge- bändigt,  unverheiratet'»  ion.  Perf.  deöf.ir^^ai^  öixTjTt^  , Bändiger',  öfÄ^oig .Bändigung,  Zähmung';
Formen  mit  Wurzelvokal  o  fehlen  dem  Gr.;
200
lat.  domo  (*domä-iö  =  damäydti),  domäs  {*domä-si  =  ahd.  zamös)  ^^IJ dige,  zähme*,  Perf.  domul  (aus  *dom9-uai),  Partiz.  domitus  (nach  domx und  domitor  aus  *dmätos,  idg.  *c2m-^o-5  umgebildet),  domitor  ,Bezähmei (==  ai.  damitdr-)]  domitus,  -üs  m.  , Bändigung'  (vgl.  ai.  damitvä)]
air.  damnaim  ,binde  (fest),  bändige  (Pferde)',  Verbalnom.   damnad  u^H domnad  (wohl  =  gr.  ödfirrj^n)]  lautliche  Vermischung  mit   damnaim  a^J lat.  damnö,   der  wohl  auch   das  unlenierte  m  des  Partiz.  dammainti  entS Sprüngen   ist;    air.    dam-   ,sich    fügen,    erleiden,    gewähren'    (z.  B.    daimi^ , gesteht  zu'  Avohl  =  ai.  dämydti,  komponiert  ni-daim  _,non  patitur'j  Pei-f dämair  aus   Dehnst.   *döm-)j  mit  acZ-  ,gestehen'  (z.  B.  3.  PI.  ataimet)j  mj^ /o-  , erleiden'  (z.  B.  1.  Sg.  fo-daimim\  cymr.  addef,  bret.  aHsav  ,gestehen' acymr.    ??i    ceiw    guodeimisauch    Gl.    ,non    bene    passae',    ncymr.    go-ddef ,leiden,  erlauben',  corn.  gothaf  , ertragen',  bret.  gouzafiv,  gouzav  ds.  (aber cymr.  dofi  , zähmen',  acymr.  dometic  ,gezähmt',  ar-domaul  ,gelehrig',  cymr. döfj  bret.  cZq^, zahm'  stammen  aus  lat.  domäre,  so  daß  einheimische  Formen mit  0  dem  Kelt.  fehlten);
got.  ga-tamjan,  anord.  temja,  ags.  temian,  mnd.  temmen,  ahd.  zemmen , zähmen'  (Kaus.  *domeiö  =  ai.  damdyati)]  ahd.  zamön  ds.  (=  lat.  domä-reY anord.  tamr,  ags.  ^aw,  ahd.  zam  ,zahm'  (unklar,  ob  Rückbildung  aus  dem Verbum,  oder  ob  die  pass.  Bed.  aus  , Zähmung  =  Gezähmtes*  erwachsen ist,  so  daß  in  geschichtlichem  Zusammenhang  mit  ai.  ddma-h  »Bändi- gung').
Wegen  ai.  damya-  ,zu  zähmen'  und  ,juuger  Stier,  der  noch  gezähmt werden  soll'  und  wegen  gr.  da^ctXrig  einerseits  ,bezwingend,  bändigend' (^'Eqojg,  Anakreon),  andrerseits  ,junger  (noch  zu  zähmender)  Stier*,  avozu daf-idlr]  ,junge  Kuh',  ödixaXiq  ,ds.*;  auch  ,junges  Mädchen*,  dd^aXog  ,Kalb', ist  wohl  alb.  dente,  dhente,  ^q^.  dhent  , Kleinvieh,  Schafe'  {*dem-tä  oder *dem-to-Sj  bzw.-  *dom-tä,  -tos),  dem  ,Rind,  junger  Stier'  (=  ai.  damya-\ sowie  auch  gall.  GN  Damona  f.  und  air.  dam  , Ochse'  (*damos),  dam allaid  , Hirsch'  (,*wilder  Ochse'),  sowie  cymr.  dafad^  a.C0Tn.  dauat,  bret. daTwat  , Schaf  (dann  =  gr.  ä-dd^aTog)  anzureihen  (ursprgl.  Bezeichnungen gezähmter  Horntiere);  lat.  damma  oder  däma  ist  wohl  aus  dem  Kelt.  oder anderswoher  entlehnt;  unklar  ist  ags.  da  f.  ,Reh'  (daraus  acorn.  da  ,dama'), engl,  doe,  alem.  te  ds.,  vgl.  Holthausen  Altengl.  etym.  Wb.  68;  aus  afrz, daim  , Damhirsch'  stammt  bret.  devi  ds.;  germ.  Lehnformen  s.  bei  Falk- Torp  u.  daadyr  m.  Lit.;  entsprechend  niederösterr.  zamer,  zamerl  ,junger Ochs'  (Much  ZfdA.  42,  167;  vorgerm.  *a  oder  *o?).
Hitt.  da-ma-a§-zi  ,bedrängt',  Prät.  3.  PI.  ta-ma-a^-sir,  Pedersen  Hitt 95  f.
WP.  I  788  f.,  WH.  1  367  f.,  861,  Meillet  BSL.  33,  110.        .         .      .
201
Wurm'?
-gpidaur.  ösf^isXiag  f.  Akk.  PL,  de^ßXsTg'  ßdelXai  Hes.;
vielleicht  alb.  dhemje  ,Raupe'  (kann  für  *dhemlie  stehen),  dhemize,  dhimize fleischmade'. *   WP.  I  790.
rfcui-  .beißen'.
\i.  ddsati  , beißt'  (*dnketi),  Perf.  daddrrisa  (danach  auch  ein  Präs.  ddmsati), '  Kaiis.  dam§dyate  , macht  beißen',  ddmsa-h  ,Biß,  Bremse*,  damiana-m  ,das Beißen',  damstra-h,  ddmsträ  , Spitzzahn,  Fangzahn'  =  av.  tiii-dqstra-  ,mit scharfem  Gebiß,  Gezähn'  (für  -dqStra-  s.  Bartholomae  Airan.  Wb.  653);
```


### [2026-09-05T17:50:33.081Z] TOOL RESULT

```
=== POK page 199 leaf ===
2747:S.  auch  unter  denk-.
---beissen---
1489:Mir.  brataim  ,plündere,  raube^  (dazu  bratdii  ,Lachs^)  =  cymr.  brath^^ ,stechen,  beißen,  durchbohren^;  Hhvozdh-  oder  Hhfzdh-  zu  germ.  *bruzi, in  ahd.  brort  ,Rand,  Kante^,  ags.  brord  m.  ,Spitze,  Keim,  Blatt^,  wsächs. brerd  (*brozdi-),  ags.  bryrdan  ,anstacheln,  reizen^,  aisl.  broddr  ,Spitze,  Ge- treidekeim, Schneide^,  ahd.  gibrortön  ,einfassen^;  =  baltoslav.  *bruzdä-  i^ aksl.  h'^zda,  russ.  brozde  ,Zaum^,  lit.  bruzdüklis,  alt  ,Zaum^,  heute  ,Pflockj KnebeP.  Hingegen  ist  h't.  brizgilas,  apr.  bisgelan  ,Zaum^  wohl  aus  urgerm. briidila-  (ags.  brigdds  ,Zaum^,  bregdan  ,flechten^)  entlehnt.  Anders  Speclit  '. Dekl.  142.
1611:got.  iei^an  .heißen',  aisl.  blta  .beißen;  eindringen  (vom  Schwert  u.  dgl.)', ,  as.  ags.  bitan,  ahd.  blzzan  .beißen'  (==  ai.  bhidati,  gr.  cpsldo^iai)',  Kaus. aisl.  beita  .beißen  lassen,  weiden  lassen',  ags.  bcetan  .zügeln,  jagen',  ahd. mhd.  beizen  ,ds.,  beizen',  aisl.  beizl  ,Gebiß,  Zaum'  (*baitislan),  ags.  gebößtu N.  PL,  geböetel  n.  ,Gebiß';  aisl.  biti  m..  ags.  bita  m.  .Bissen',  ahd.  bizzo  m.; bizza  f.  .Bissen.  Keil';  got.  baitrs  .bitter'  (.beißend  von  Geschmack');  ab- lautend aisl.  bitr  .beißend,  scharf,  schmerzlich',  ags.  biter,  bitter,  as.  ahd. bittar  ,beißend.  scharf,  bitter';  aisl.  beiskr  .scharf,  bitter'  (*bait-skaz);  got.
1613:iw  <    Sauerteio-'   (*bhei[d]-sto-);    ags.  hitela   ^beißend"^,    bitel  ^Käiev^y   engl.
2889:rfcui-  .beißen'.
2890:\i.  ddsati  , beißt'  (*dnketi),  Perf.  daddrrisa  (danach  auch  ein  Präs.  ddmsati), '  Kaiis.  dam§dyate  , macht  beißen',  ddmsa-h  ,Biß,  Bremse*,  damiana-m  ,das Beißen',  damstra-h,  ddmsträ  , Spitzzahn,  Fangzahn'  =  av.  tiii-dqstra-  ,mit scharfem  Gebiß,  Gezähn'  (für  -dqStra-  s.  Bartholomae  Airan.  Wb.  653);
2891:crr.  dcxKvo)  , beiße'  {*dnJc-nö),  Aor.  sda-nov  (=  Impf.  ai.  ddasam),  wozu Fut.  örj^ouat  (aber  ion.  öd^eTai),  Perf.  öiörjyfxaL,  Sedrjxwg  (sowie  öfjy^a Biß*)  ^^^  Ablautneubildung  (Schwyzer  Gr.  Gr.  I  770);  day.er6v,  rö  dd/.og beißendes  Tier' 5  dazu  wohl  ddd^  ,mit  den  Zähnen  beißend*,  vielleicht ursprgl.  ,Zahn'  oder  ,Biß'  (Liddell-Scott,  anders  Schwyzer  Gr.  Gr.  I  620, 723),  wohl  Kreuzung  von  *(5a^  , beißend'  mit  döovg,  davon  abgeleitet  död^u) (död^o)  mit  Assimil.  des  0  an  das  a),  ddax^o)  usw.  , kratze,  jucke',  ddayfiög , Kratzen';
2893:ahd.  zangar  , beißend,  scharf,  mnd.  langer  ,ds.,  bissig,  kräftig,  frisch'; anord.  tgng  (Gen.  tengr  und  tangar),  ags.  tang^  tange,  ahd.  zanga  , Zange' (*don7cä),  d.  i.  ,die  zusammenbeißende';  mit  weiterer  Verschiebung  zu .zusammenkneifen,  zusammendrücken',  wohl  as.  hitengi  ,nahe  an  einen rührend',  ags.  getang  ds.,  getenge  ,nahe  anliegend,  bedrängend',  ahd. gizengi  , reichend  bis,  nahe  rührend  an',  Adv.  gizango,  wozu  anord. tengja  (*tangjan)  .verbinden',  ags.  tengan  ,angreifen,  drängen,  vorwärts- streben', getengan  ,haften  machen,  fügen'  (ags.  intinga  m.  , matter',  sam- tinges  ,at  once',  getingaUj  st.  V.,  .drücken  an*  nach  Fick  III*  152  Neu- bildung?); daneben  im  gramm.  Wechsel  germ.  *tanhu-  ,fest  anliegend,  an- hängend, zähe'  in  ags.  töh  ,zähe';  mnd.  tä  , festhaltend*,  ahd.  zähi^  nhd.  zäh'y anord.  tä  n. , festgestampfter  Platz  vor  dem  Hause*  (finn.  Lw.  tanhua  , Pferch');
2894:vielleicht  ursprünglich  verschieden  von  der  Wz.  *d^k-  ,zerreißen*,  obwohl *denk'  vielleicht  als  nasalierte  Form  zu  *dek  und  ,beißen*  als  ,mit  den Zähnen  zerreißen*  gefaßt  werden  könnte.
```


## [2026-09-05T17:50:46.504Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT daman ===\"\ngrep -n \"dāman\\|dāmau\\|dāman-\\|dăman\" BRT.txt | head -20\necho \"=== BRT dantan ===\"\ngrep -n \"dantan\\|dantān\\|Zahn'\" BRT.txt | head -20\necho \"=== BRT daitika ===\"\ngrep -n -i \"daitika\\|daitik\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T17:50:46.586Z] TOOL RESULT

```
=== BRT daman ===
=== BRT dantan ===
12637:Ableit  aus  *dattl-  m.  'Zahn',   5.  dantan-   (Sp.
12736:•  j.dantan-m. 'Zahn':  •««J(NP.)'>F.^d.
13302:•  j.  data-  f.  'Zahn':  ymca  am  asti  'tshva arSnte  ganmSkva  (sd.)  vioänte  V.  JJ.  4.
13303:KompE.  —  Ableit.  aas  ar.  'äaiit-  m.  'Zahn', ai.  dänt-  m. ;  auffällig  ist  das  innere  ä,  wofür K  1,  L4  a  bieten;  s.  aber  Komp.  und  das nip.  Wort.  —  mp.  däl  (Bd.  14.  24).  —  Pü.: dandän.
24214:vtinito.dantan-
24215:•  j.  vi'mitö.dantan-  Adj.  'mit  ungestalten Zähnen';  ms  a%ra  . .  V5«J(NP.)  V.  2.  ag; —  mä  drvä  *tans  Yt.5.  93.
=== BRT daitika ===
3328:•  g.  aidy-S-,  j.  ai8y-ü-''  Adj.  'helfend'  sva. 1)  'nützlich',  von  Tieren:  pasukanqmcH  .. daitikanqmcit  (sd.)  'yünam  .  .  vrunS  "die Seelen  der  zahmen  und  der  nützlichen wilden  Tiere"*'  Y,_jp,  if.;  zit.  Yt /y.  154, wo    aioyunqm.        2)  'brauchbar,   tüchtig
12290:ai.  TgL  tüfnadaiti/lra-  Adj.,  mm  V.  äaJa/i 'beissl';  s.  tiädifiura:  —  *difslra-  statt  'dqSlra- nobl  in  Anletuiang  an  einen  KS.  *äSdqi 'schaifiälmig'  aus  •flSin/-  {al  iüä-dan),^  »gl. danlan-  und  tilidälä;  daitika-.  —  Npü.:  rti dan^n.
12631:•  '].,  g.  daitika-  m.  'wildes,  nichtdomesti- zirtes  Tier'*':  pasuianqmcä  .  .  'kanqmiä aidyBnqm  (sd.)  urutm  Y.^p.  2;  zit  Yt.  y. 154;  —  urunB  pasukanam  .  .  'tikanam Vt.jj.74.
12634:daitika-,  nach  Bd.  24.  9  der   der  fr,ii^  raftärän,
13113:yahmat  haca  Jräkwirisal  näfs  airyanqm °Hyunqm  ^r^m  airyanqm  'hyunqm  Yt. '^■^7)  —  ifar^Rö  .  .  yat  asti  airyanqm 'Ayunqm  Ytip.  56;  V. /^.  39;  —  iava/ftn :^arpnd  'hrähr^m  airyanqm  "AyunamYl-ig. 69;/?.  10; —  avavat  kavaSm  3^ar>ns yaha yat  iöa  anairym  °Ahus  hakat  usäi  us.frs- vayöit  (sd.)  Yl.  ip.  6  8 ;  —  taurvayeiti  anairya *'/iAävS(3isA'P.)Yt.iS.2;  —  airaityanqm tat  °Ayunqm  Vf/y^rai  uzjasaiH  N.(iS;  — aiioitaradyJ  haca  'nhubyö  Yt  i'j.  14;  — mi>r)m  .  .  yim  yazmte  daiAkupatayS  .  . aniar»  -iiihu  (AD.)  papr^täne  Yt.  10.  8; r_5.  49;  —  hasaaräis  (näml.  asH  mihrS) aiitary  °Ryu  (AD.)  Yt.  /o.  117;  —  yd  .  . karafanö  urapayeintl  (sd.)  yacä  xrata *Ju£>sc/a'irä  "Ayunqm  Y.4^'.io;  —  säsia 'rthSui  äaähupailii  *äxsta  isimnS  'lihave amtm  is^mnS  tanuye  YtJÖ^.  19;  —  sSsta 'itißaus  hams^ia%rö  Yt  13.  r8,  69,  75.  50; — fraiimatcltl!  'Xyunqm  Yt  13.  95;  *lo.  18; —  nöit  me..  ährava  . .  'iiifiava  (LS,)  earät Y.p,  34;  —  Siihqm  'hyunqm  yä  anyä rajSit  Y.ig.  18;  —  bawrSil paiti  'tJihaove Yti.ag.  a)  GS.  mit  GS.  des  Landes- namens  zur  Bezeichnung  der  Gebürtigkeit bei  EN.:  parlatgava  dazgrS^ava  apa- jTjVavi  (sd.)  'iähfus'  Ytrj.i2j;  127;  — ^rüJ  atv5jar3(^  fyultahe  tanyehe  tanyayä •tViÄÄ/ Yl  jy.  125;  125';  —  s,  noch tnzavant-  daitiksus  EN.  a)  bes.  im Gegensatz  zu  Haus,  Gemeine  und  Gau***; a)  im  gAiw.:  *S  sl  dimSnsm  vTs)m  v3 söihnrrt  vä 'Ayäm  vä  adaj  du^iäcd(sd.) .. Y.jt.  18;  —  yP  Auäänus  d^manahyä  xla- %r?m  iiSi^rahyS  vä  'AySus  vä  .  .fi-ada'iiäi (sd.)  asppmaia  Y.Jl.  16;  —  ga  JrSnKis' (sd.)  /tfiiraAyä  vä  'AySus  vä  Y.4ß.^; —  ähnlich:  patri  jfaSSuf  airyamanascä dadaiii  (sd.)  tiSil  ma  xsnäus  yä  v^rvsSnä (sd.)  ..  naida  'hy3u!  ..  sästärB  (sd.)  Y.46. 1.  b)    im  jAw.:    */ratainitm   .  .  yä
25193:*)  Sva.  daitiko;  td.;  vgl.  fam-oakai-,  —  All Raiav  dieser  Tierklasse  pit  Bd.  3.^  9  d«  Hase (xargSt).   Wdtere»  a.  unter  aidyü:  —   ••)  Hier
```


## [2026-09-05T17:50:48.562Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD dam ===\"\ngrep -n -i \"^dām\\|dām \\[\\|dad \\[\\|dandān\\|almās\\|almas\" PHD.txt PHD_mackenzie.txt | head -30\necho \"=== NYB ===\"\ngrep -n -i \"dām \\|dad \\|almās\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-05T17:50:48.637Z] TOOL RESULT

```
=== PHD dam ===
PHD.txt:189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
PHD.txt:306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
PHD.txt:603:wābar [w’Al | M wbr, (N bāwar)] truth; belief. wābarīģān [w?/yk?n' | M wbryg’n) true, trustworthy. “Аһ: trustworthiness. wabz [wpc, wpz] wasp. wačast [wcst! = Av. vwacas-tasti-] strophe (of the Gathas). watéag [wck!, (bck!) | N bacca] child, baby, cub. wad [SL Y.ÀA < A sry’; wt! | M wd, N bad] bad, evil. ^ Áh : badness, evil. маа [w?t! | M wd, N bad] wind, breath, spirit; cal. 22nd day. wadag [wtk'] evil, vile, wicked. ~ih: evil, vileness. wādām [w’t?m | N bádám] almond. wādbān [w°tp’n' | N bādbān] sail.
PHD.txt:1599:diamond almas(t).
PHD.txt:4031:tooth dād, dandān.
PHD.txt:5550:dāmādīh
PHD.txt:5551:dāmād
PHD_mackenzie.txt:850:   a-dad ['d't'], a-dadestan ['-DYNA, -d'tst'n ] illegal. unjust.
PHD_mackenzie.txt:980:almls(t) ['Im's(t l ) I (M 'rm's), N almas] steel; diamond.
PHD_mackenzie.txt:1014:Amurdad ['m(w)rdt' IN murdtid] Immortality, the sixth Amahraspand,
PHD_mackenzie.txt:1482:bamdad [b'md't' 1 M b)md)d, N ,,-,] dawn, morning.
PHD_mackenzie.txt:1811:dad [dtl I M dd, N,...,] wild animal.
PHD_mackenzie.txt:1812:IdAd [d't' I M d'd, N ,...,] law, justice; those scriptures dealing with legal
PHD_mackenzie.txt:1814:2dAd [d't IN,...,] age.
PHD_mackenzie.txt:2916: Hordad [hwrdt I M hrwd)d, N Xurdiid] Perfection, the fifth Amahra-
PHD_mackenzie.txt:7663:speckled pad.                          steel almas(t), polawad; (a.) poliiwad-
PHD_mackenzie.txt:11697:almast
=== NYB ===
887:Bagdit [bkd't'] the town of Bagdad 11721,
1227:dat [d?t'] 1. law 6413-19, 6916, 8623, 9811, — 2. age 2?9 (with the gl. hangäm). 31. 10*%. 14°. 165. 622. 104°; cas. obl. dātēh 536-22, — 3. created, pt. of dätan: dēvān ~ created by the devs 1038-10-13, — 1. Av. (726) ddta- NP ddd ‘justice, equity’. — 2. NP dad ‘life, age’. — 3. Av. (671 sq.) daēvē.dāta-. dätan [YHBWN-tn'; d’tn' 119%, 1201] dah- [always YHBWN-], lst p. sg. YHBWN-m = dahom; 3d p. sg. = 2nd p. pl. ~ -yt = dahét; lst p. pl. ~-ym = dahem; 3d p. pl. ~-d = dahénd; subju. 2nd p. sg. —-'h = dahäh 34%; imp. sg. ~ = dah; pt. = pret. pass. 3d p. sg. dāt [YHBWN-t', inser. YHBWN; d>t' 22. 922 etc.] lst sg. dāt hom 57°; 2nd p. sg. dāt h&5'1*-* 3d p. pl. dāt hend '18?, construed as an act. form 18?!; pluperf. 3d p. sg. dat estet 8712, 3d p. pl. ~ ēstēnd 94*4; opt. pass. dāt [HWH-d =] he 2%; A. to give SPrs:15; 238-21 ete. passim; apāc ~ to give back 345-6; — fräc ~ to give away 5016-1’; — v, also dröt, framān, passax", zančh. — B. 1. to put, to place,
1242:davanik [dw?nyk] transliteration of the broken pl. dawānīg of Arab dānag, -iq, a small coin: Abu (Arab) ~ “‘the father of the small coins" = he who is greedy for money, the nickname of the caliph Abu Ja‘far Mansur, the founder of Bagdad 11771. — Arab dānag is borrowed from Milr dáng (BP d?ng), Arm. lw. dang, NP dank, dän(u)g; according to FrP 29 it was 1/, of a denar, but in Islamic times 1/, of a drahm; late Greek authors Šuvaxn = 0B0X6c.
1400:duš-nam [dwán?m] abuse, invectives 15%. — = NP; duš-nam ‘ill-famed’ (SGV). duš-parg [dwáplg] unblessed, unfortu- nate, unhappy; ignoble, mean, opp. farrax" (g. v.) Mx 50?-4, Paz. dušparg, Skr dusta-samrddhi; a dušparg dz i dévq- dad Aog. 31, Skr. v. duscära. — dus-parg ‘whose parg is bad’ is a synonym of dušxvarr(ah) (a. v.), MPrth dwšfr = duš- farr (A-H III), consequently parg is a synonym of z%arrah (g.v.). The Paz.
4807:Vd. — Vendidad. Avesta Text with Pahlavi translation and commentary, and glos- l sarial index, ed. by Dastoor Hoshang Jamasp, 2 vols. Bombay 1907. Glossary of Pahlavi Vendidad by Dinshah D. Kapadia. Bombay 1953.
6339:almāst: ~
6983:almās: almäst
```


## [2026-09-05T17:51:12.780Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['BQT','MON','KLN','SOD','HRN','BRT','SYN','POK','AHD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:700]); print()\n\"",
 "description": "Check refs_online.json entries"
}
```


### [2026-09-05T17:51:14.585Z] TOOL RESULT

```
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
```


## [2026-09-05T17:51:18.332Z] TOOL CALL #14: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:817 2>&1 | head -60",
 "description": "Fetch BQT page 817"
}
```


### [2026-09-05T17:51:19.916Z] TOOL RESULT

```
no scan of BQT covers printed page 817 (see 'scans' in refs_online.json)
```


## [2026-09-05T17:51:23.303Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3\necho \"---search for 817---\"\ngrep -n \"^817$\\|۸۱۷\" BQT_v2_pages.txt | head -10\necho \"=== dam entry ===\"\ngrep -n \"دام\" BQT_v2_pages.txt | head -5",
 "description": "Explore BQT v2 pages file"
}
```


### [2026-09-05T17:51:25.061Z] TOOL RESULT

```
---search for 817---
3524:   ‫معرب نکانك ( که بغلط لکامه و لکانه‬     ‫» مصحف «نقالق» « دزی ح ‪ ۲‬ص‪۸۱۷‬‬             ‫‪ ۷‬ظ‬
30265:        ‫‪ ۹‬ت‌ رك‪:‬زهشزه‪.‬‬           ‫‪۱‬‬     ‫«منتهی‌الارب»‬   ‫زىق القمیص ‪ 4‬ره يراهن‬        ‫(‬   ‫‪٥۱‬‏‬    ‫‪۲‬‬       ‫سنون‬    ‫‪۸۱۷‬‬
=== dam entry ===
497:            ‫باد برآن کصنبند وابر‬                   ‫جال ‪ -‬بر وزن ممالط»لق دام وتلعرا‬
516:               ‫‪ - ۷‬رك ‪ :‬جالى و جاك ‪.‬‬  ‫از ( دام ) [ برای پرندکانماهی و غیرہ ]‪.‬‬
911: ‫جاوشیر » باشن قطه دار بر وزن‬                        ‫آن‌جهان‬      ‫(‪3 -)۲‬‬   ‫جاویداست که همیشه ودام‬
955:‫کشنده رشن قرشت زده » خاله وسرا ومنزرا‬            ‫وهسثه ودام )‪ ۱‬را گونند ‪ -‬وعالم آخرت را‬
1427: ‫ازانت ‪ -‬و دام قربه ابت از قرای شیراز ‪-‬‬               ‫و طاس و امثال آن ‪-‬‬               ‫زنگگ‬     ‫> صدای‬     ‫خدنگه‬
```


## [2026-09-05T17:51:29.447Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json\nd=json.load(open('refs_online.json'))['BQT']\nfor k,v in d.items(): print(k,'=',json.dumps(v,ensure_ascii=False)[:1500]);print()\n\"",
 "description": "Full BQT ref info"
}
```


### [2026-09-05T17:51:31.058Z] TOOL RESULT

```
title = "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)"

kind = "archive_djvu+local_scan_ocr"

url = "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249."

lookup_hint = "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"

local_file = ["/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"]

page_offset = "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...')."

covers_etymology = true

notes = "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, 

scans = [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, checked at pdf 150 and 500", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"}, {"volume": "5", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "first_printed": 1, "last_printed": 290, "pdf_offset": 5, "lang": "fas", "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "requires_volume": true}]

cites = "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
```


## [2026-09-05T17:51:36.338Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 272 273 274 275 276; do echo \"########## leaf $L ##########\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -60; done",
 "description": "Print BQT v2 leaves near page 817"
}
```


### [2026-09-05T17:51:38.010Z] TOOL RESULT

```
<persisted-output>
Output too large (30.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b280p057d.txt

Preview (first 2KB):
########## leaf 272 ##########
                                                                                 ‫داز شمان‬




                        ‫‪-‬‬     ‫دار کوب‬             ‫دارشعان ‪ = ۱‬باشن‌شطهدار وعین‬
                       ‫بز وزن خاکروب ‪,‬‬            ‫بی‌نقطه بورزن آبریز گان » درختی باشد سطبر‬
                        ‫بزبان ‪.‬کیلالی‌مرغی‌را‬     ‫و خاردار وپوست آن بقرفه ماندلیکن از آن‬
                       ‫کونند که بامتقاردرخت‬       ‫کت تقر وسرخ نرمیشود ‪ .‬اکرقدری ازآن‌سحق‬
                               ‫را سوراخ کند ‪.‬‬
                       ‫دار بوگاوورسیشده۔‬
                                                 ‫کنتد وما سر که سرشند وبردندان لهند درد را‬
                                                  ‫فروشاند» وقدری ازچوب آن‌زنان‌بخود ب رگبرند‬
      ‫دارکوب‬                      ‫باکاف قارسی‬     ‫قرزهدی که درشکم مرده باشد بیفتد ‪ -‬و ستبل‬
‫و مشین نقطه دار زده » امر به نگاهداشتن باشد‬       ‫هتدی را فز دارششمان خوانند و دارشیمان «م‬
               ‫بعنی نگاهدار ومحافظت کن © ‪.‬‬                          ‫کوبند بحذف شین دوم ‪.‬‬
‫دار کیسه ‪ ۱‬س بکر کاف و سکون‬                                             ‫دفار‬
                                                 ‫رلی ‪ - ۲‬باوفراای قرشت بر‬
‫بای حعلی وفتحصین بینقطه " کسه مانندی‌است‬
‫که دربعضی از درختها بهم ءیرسد ودرون‌آن پر‬        ‫وزن بتماکین » سفهوسکو ود کهکروابند که‬
                                                  ‫تن در بیش درخالپا سازند ‪ -‬و مطلق‬       ‫بجهت‬
                            ‫از یشه میباشد ‪.‬‬                          ‫تکه کاهر ا نیز کفته‌اند ‪۱‬‬
‫دار هك » بامیم بروزن آبچك » نوعی‬
                                                      ‫دار فلفل ‪ ۴‬مهعروف است گ‬
                                                  ‫‪.‬وبند‬
‫ازمروباشد وآن مروسفید است » ومروجنسی از‬
‫رباحین بود وسد بلغمی بکثاید واکثر امراض‬           ‫شکوفه وبیلرفلفل است» وبعضی کویند درخت آن‬
                            ‫بلغمی را ناقع است‪.‬‬    ‫غیر درخت قلقل باشد(‪ )۱‬وآن را فلفل درازنیز‬
...
</persisted-output>
```


## [2026-09-05T17:51:48.365Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 240<i<300:\n        # look for latin-script tokens\n        lat=re.findall(r'[A-Za-zĀ-ſƀ-ɏ]{3,}',l)\n        if 'دامن' in l or 'دامدار' in l or 'دامان' in l:\n            print(i, 'HIT', [w for w in lat][:20])\nEOF",
 "description": "Locate BQT leaf with dām entries"
}
```


### [2026-09-05T17:51:50.094Z] TOOL RESULT

```
252 HIT []
253 HIT []
275 HIT ['darn']
277 HIT []
278 HIT []
291 HIT []
292 HIT []
```


## [2026-09-05T17:51:52.561Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==278' BQT_v2_pages.txt",
 "description": "Print BQT v2 leaf 277"
}
```


### [2026-09-05T17:51:54.335Z] TOOL RESULT

```
 ‫دامن بدندا نکرفتن‬                                                                           ‫‪ ۷۱‬رس‬

                                        ‫گفته‌اند ‪. ۴‬‬     ‫دام = بروزن رام» نقیض ددباشد که‌آن‬
                                                         ‫وحشی غیر درنده است عموماً و آهوو غزال و‬
                                                         ‫لیر را(‪)۱‬گویند خصوصا ‪ - ۱‬وحشرات‌الارش‬
                                                         ‫وپرنده را هم میگوبند ‪ -‬و هرچیز که جانوران‬
‫دامگاه ستول = بمعنی دامگاه دیو‬
                                                         ‫در آن بفریب گرفتار شوند ‪ - ۴‬و نزد محققین‬
                     ‫است که عالم سفلی است ‪.‬‬
 ‫‪e‬‏ تیدام اور‬         ‫گرگ‬            ‫دامگاه‬                                             ‫بمعنی زخارف‬

        ‫است کهجهان فانی وعالم سفلی باشد ‪.‬‬                                              ‫دلیوی و آنچه‬
‫دام آشتن > کابه از بازی دادن ودام‬                                                   ‫باعثبازماندکیاز‬
                                                            ‫مبداء باشد‪ . # .‬نوعی‌دام (تور) ماهیگیری‬
          ‫‪ -‬وخلاصی از دام باشد ‪9 .‬‬           ‫سردن‬

‫دامن باغی گرفتن‪ -‬کنابهازخلوت‬
                                                         ‫دامفول‪ -‬با غين نقطه‌دار وواوه‌جهول‬
                ‫زیدن گووشه نشینی باشد ‪.‬‬                  ‫بروزن زاغنول‪ ,‬دانهاو گرهها باشد مانند گردکان‬
‫دامن بد ندان گردن = کنایه از‬                             ‫که ازاعنا کولوی مردم برمیآید ودردنمبکند‬
‫نمودن باشد د و کنایه از‬        ‫فروتنی کردن و عجز‬         ‫نورآاسلعه میکوبند‪ -‬وغول‌بیابانی رائیز گفته‌اند‬
                  ‫گرشختن هما مدهاست (‪. )۲‬‬                                         ‫واونوعی ازجن است ‪.‬‬
‫دامن بنددان گر تز بمعنی‌دامن‬                             ‫داهلث » بفتحثالث بر وزن کالك '‬
‫بدندان کردن است کنهابه از عجز و فروتنی‬                   ‫جانوران وحتی کوچك راگویند همچوخ رگوش‬
                                    ‫وگربختن باشد ‪.‬‬      ‫ورویاه وامثالآن ‪ -‬و مقنمه وسرانداز زنانرا هم‬

                                ‫‪.‬‬    ‫(‪ )۲‬چك‪ .‬چش ‪ :‬هم هت‬               ‫(‪ )۱‬چك ‪ :‬نخحیر را ‪.‬‬

  ‫» رام شدن) » بونانی ‪( 5618002‬کاو نر) ‪.‬‬               ‫رمدن‬
                                                          ‫‪ - ۱‬حندی باستان ‪( 0۳31 -‬کرا‬
   ‫)؛ در پپلوی ‪0۳84‬‬           ‫رمدن‬
                                 ‫لانبنی ‪ ( 6720۳10‬کاو نر‪ .‬ورزاو ) فس ‪ :‬استی ‪( 000۳0‬کرا‬
                     ‫(مخلوق) (اوستا ‪« )020180-‬اسشق ‪ ۰۳۵‬و ص ‪۲۷۲٩‬‏ ورك ‪ :‬مناس ‪. ۰۷۲:۲‬‬
  ‫‪ - ۴‬هندی باستان‪( 02008 -‬بند‪ .‬ریمان ‪ ,‬زنجیر) » افقانی ‪ , 0101‬ارمنی ع (‪)8‬‬
  ‫‪( 602‬تور) «امذق‪ .۱۳۰‬پهلوی ‪« 018‬مناس ‪۱۷۲‬؛ نیز تورماهیگیری ‪« :‬ماهی از دام جدا‬
  ‫شد ‪,‬روباه پیشتررفت وماهی خوردن گرفت» «سندبادنامه‪ .‬ظهیری‪ .‬طبع احمدآش ص ‪ ۸4‬طبری‬
               ‫رك ‪ :‬دامنی ‪.‬‬          ‫‪ ۰‬مازندرانی کنونی ‪ « 20062‬واژه نامه ‪. ۲۱4۰‬‬
                                       ‫‪۴‬‬                                                         ‫‪8‬‬
   ‫‪ #‬داماد ‪ -‬پهلوی )‪ , 4072‬اوستا‪( 72]200282-‬داماد)‪ ,‬هندی‌باستان ‪,۲2420۳81-‬‬
   ‫کردی ‪ › 62۷22‬اففانی‪ 0۳2‬و ‪, 128۳02‬بلوچی ‪ 012002‬و ‪ «04۵۷021‬اسدق ‪۲۳۵۰۰‬‬
   ‫‪,‬مشچه ‪20۳۵2‬؛‬
              ‫کیلگی‪ .4۳2‬اورامانی ‪« 01۷20182‬ك‪ .‬اورامان ‪ ۷۲۱۲۰‬دزفولی ‪ 010‬ک‬
   ‫مردیکه تازه جشن‌عروسی وی برپا شود ‪ ۰‬مرد تازه زن گرفته ‪.‬شوهر دختر شخص"‪ -‬شوهرخواهر‬
  ‫شخص‪ « :‬از ملطان عالم ‪ ۰.‬محم‌دین ملکشاه بدر همدان در واقعة امیر شهاب الدین قتلمش الب‬
                          ‫‪.‬‬         ‫غازی که‌داماد او بود بخواهر ‪ ....‬شنیدم» «چهارمقاله طبحم دن صه؛ ‏‬
              ‫‪#‬دامای = داهن (مخفف)‪ -‬بفتح سوم کنار پابین جامه(مقابل گریبان) ‪:‬‬
           ‫ابن کریباش کیرد آن دامن‪.‬‬                            ‫سک ودربان چوافتند غریب‬
   ‫دگلتان ‪. ۹۳۰‬‬
                                     ‫وبای کوه ‪۰‬‬   ‫دبال ‪ -‬کناره‪-‬چادربادبان کشتی‪ -‬کنارة کو‬
```


## [2026-09-05T17:52:19.565Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== leaf 340 (~883) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==341' BQT_v2_pages.txt | tail -30\necho; echo \"=== leaf 341 (~884) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==342' BQT_v2_pages.txt | tail -30",
 "description": "Print BQT v2 leaves near page 884"
}
```


### [2026-09-05T17:52:20.992Z] TOOL RESULT

```
=== leaf 340 (~883) ===
‫و خاکتر و امنال آن درآن ریزند‪ ,‬و سرکن‬                           ‫و تازبالةٌ بزرکف را نگیوزبند ‪ -‬و افير برادر‬
‫ونام «مشوقةٌ تل باشد‪» ۷‬‬        ‫گزوبند ا‬
                                      ‫تنها را ن‬                ‫فته اند ‪,‬و گاودم همان‬   ‫کوچك کرنا را گهم‬
                                                                                                           ‫است ‪.‬‬
‫وفصهٌ تل ودمن مشمور است ‪ -‬ونام بندری است‬
 ‫درهندوستان ‪ -‬وبکراول وثانی بمعنی‌من وسن‬                       ‫بروزن همراه‪ ,‬کوره زر گران‬       ‫»‬   ‫دمگاه‬

‫باشف چنانکه هر گاه گوبند *دمن بده“ هراد آن‬                     ‫وآهنگران ومسگران‌را گویند‪ .‬و کلخن حمام‌را‬

                                                           ‫(‪ )۲‬چك ‪ :‬بازا ‪.‬‬               ‫و ‪.‬‬   ‫(‪)۱‬چك‪:‬‬


        ‫نب پور‪.‬‬
              ‫ذ‪-‬‬‫‪۴‬‬                 ‫غزه ‪.‬‬     ‫دب‬    ‫‪ :‬دم غزه ‪.‬‬    ‫‪ ۴‬رك‬             ‫رك ‪:‬دمتجه ‪.‬‬
                                                                                           ‫‪۱‬‬
                             ‫‪8‬ب‪-‬ال گر کک » ذنب‌السرحان ‪:‬‬
                                                       ‫د‬                       ‫‪ - ۴‬ذلب ذب ‪.‬‬
          ‫مجره همیدون چو سیمن مطبلی ‪.‬‬                            ‫دم گرگ چون پیش چرمةً ستوری‬
  ‫“‪.‬‬     ‫داء‌غانی ‪۵‬‬    ‫«منوچهری‬

 ‫‏‪( - ٩‬عر) « دمن بکر اول سر کن درهم نشسته است ودمن بشکل است»«شرح فاموسی»‬
                                                           ‫جمع دمنه‪ ,‬آثار خانه ‪:‬‬       ‫اول و فتح دوم‬     ‫و یکر‬


         ‫آنجاست همه ربع وطلول و دمن من ‪.‬‬                         ‫و آنجا که نو بودستی ابام کذشته‬
  ‫‪ ۵‬منوچهری دامغانی ‪۳٩٩‬‏ ‪.‬‬
  ‫دمن›‬     ‫ودرقارسی سمخفف‬     ‫اس‬       ‫‪itnimaD‬‏‬       ‫نام معشوفه نل درهندی(سانکربت)‬                ‫‪9 ¥‬‬

                                                                                         ‫شده «چك ‪ ۷۳۳‬ح؛ ‪.‬‬


=== leaf 341 (~884) ===
                                                                 ‫وشغال هردو آمده است ‪ - ۴‬ک‬
‫و برمعونیییدن و رسن لبات هم هت ‪ -‬و دم‬                                ‫ومحیل وفتان باشد ‪٩‬‏ ‪۰‬‬
‫خوردن ‪ -‬و فکسشیدن ‪ -‬وطلوع صبحرا لیز‬               ‫دمنه دالی = بدااز ابجد بر وزن‬
                                    ‫کوبند ‪.‬‬       ‫پهلوانی ‪ ۰‬لته کوهنۀ وچ ده را کوبند که در‬
‫دميلث س بکر انیو سکون تحتانی‬                         ‫موراخ تنور کنند تا بخار تذور بیرون نرود ‪.‬‬
 ‫بر وزن شريك ؛ به‌منی زمین و بوم باشد ‪٩۷-‬‏‬       ‫نیم دور ‌ بکرثانی» کنایه از‬         ‫دم‬
 ‫وبسکون‌الی وفتح تحتالی» نام قریه‌است ازقرای‬
‫غزنین ‪ .‬کوبند شهاب‌الدین غوری بزخم یکی از‬
                                                                              ‫آه درد فا باشف ‪۰‬‬


                   ‫ملاحده درا نجا شپید شد ‪.‬‬      ‫آواز‬    ‫دمو ر = بفتح اول مروزن سور‬

                                 ‫(‪ )۲‬چك‪ :‬زند ویاژند ‪.‬‬               ‫)‪ ۱‬چش ‪ :‬م‬
                                                              ‫‪-‬فتوح ‪.‬‬
 ‫‏‪ - ٩‬دمندان بفتح اول و کر دوم ‪ .‬شهری بز رکٹ و وسیم بکرمان و در آن کان‬
  ‫آهن و مس و سیم وژر ونوشادر و توتیا بیار است و معدن آن بکوهی است بنام « دنباوند *ه‬
  ‫غارست‌بز رکه‬    ‫کابونه‬
                       ‫و ارتفاع آن سه فرسنك است‌وبهفت فرمنکی شهر «چواشبر» است » و در‬
  ‫و تاربك که از درون آن آوای آب بگوش رد و بخاری دود مانند برآید و بحوالی بچید ‪.‬‬
   ‫]ارابکنند‪».‬‬
             ‫وچون متکانف گردد وزیاده شود مردم شهر وحوالی بدانجا شوند ودرهرماه با دوماه نپ‬
                      ‫‪ - ۳‬اسم فاعل از «دمیدن» ‪.‬‬           ‫« معجم البلدان پنقل از ابن الفقید» ‪.‬‬
   ‫ورتك‬
      ‫‪ - ۴‬درسان کرت ‪ 261۵82012321‬نام شفالی در پنچتنترا « وبلیاه‌ز ‪٩۹4‬‏ ‪ ۳:‬ك‬
              ‫(کلیله) نیز نام شفالی دیکر بود » واسم کلیله ودمته ازنام ابن دوشفال مأخوذ است ‪.‬‬
   ‫‪۲۸۸‬‬    ‫حه‬
           ‫صهفدر‬
               ‫بق‬
```


## [2026-09-05T17:52:28.902Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 330<i<370:\n        for w in ['دندان','دنده','دد ']:\n            if w in l:\n                print(i, w, l.count(w))\nEOF",
 "description": "Find dandān leaf in BQT v2"
}
```


### [2026-09-05T17:52:32.209Z] TOOL RESULT

```
335 دد  1
341 دد  2
344 دندان 10
344 دنده 2
344 دد  1
345 دندان 34
345 دد  1
346 دندان 20
346 دد  3
347 دندان 1
347 دنده 1
348 دد  1
350 دد  2
352 دد  1
353 دد  1
360 دد  1
361 دد  2
363 دندان 1
364 دد  1
365 دنده 1
366 دد  2
```


## [2026-09-05T17:52:35.358Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==345' BQT_v2_pages.txt | tail -25\necho \"@@@@@@@@ leaf 345 @@@@@@@@\"\nawk 'BEGIN{RS=\"\\f\"} NR==346' BQT_v2_pages.txt | tail -25",
 "description": "Print BQT leaves 344-345 (dandān)"
}
```


### [2026-09-05T17:52:37.347Z] TOOL RESULT

```
‫شغنی ‪ . 020600‬سربکلی ‪ . 000201‬وخی )تمتا اسشق ‪ 4۷۵‬فریز ندی ویر نی‬
 ‫‏‪ «dandun “jili , dãndun‬هک ‪ .‬صا ‏‪ “AA‬ینانمس ‪ . 080007‬‏‪12707 gi‬‬
     ‫سرخه‌یی ‪ , 08۳0۳60‬لاسکردی ‪ 720524‬شهمبر زادی ‪ ۶ 7۳031‬که ‪ ۲.‬ص ‪. ۸۱‬‬
 ‫‪ . 1‬هريك از استخوان هکاویچکی که در داخل ازدوفك برآمده و درجاویدن و عضغ‬
                                                ‫غذاها بکار رود ‪ -‬جموعة استخوانهای مبزور ‪:‬‬
 ‫«گل ‪:‬ان ‪. ۳۳۰‬‬         ‫دندان سگم ودهان مردم بتند ‪.‬‬               ‫آنان که یکنج عافیت بنشتند‬
  ‫دندانها برچپار قس‌آند ‪ - ۱ :‬طواحن (جمع طاحنه) با ات »> که شش درالا وشش در‬

  ‫پابین‌اند و چپار دندانی کهدرءوخر فك قرار دارند نواجذ ( جمع ناجذء ) نامیده میشولد »دوعدد‬
  ‫دربلا ودو عدد دریابین » واینها پس ازهمة دندانهاي دگ اروف وعامه آنهارا دندان عقل نامند‪.‬‬
 ‫‪ - ۲‬ضواحك ( جمع شاحکه) چپار در فوق وچهاردرنحت ‪ - ۳ .‬انیاب (جمم ناب) » دو دربلا‬


                ‫ا‪22۷۵ ۰‬‬
     ‫(‪۸0۷ 2۸۵۱۵۵۸۸‬‬             ‫‏‪ msslyol‬ابر ‏‪an‬‬
       ‫‪0‬‬
                                                 ‫دهان قرار دارند نام ابا (جمع ننیه) تامیده‬

                      ‫میذود کهدو دربالا و دو درپاین جا دارند ‪,‬‬
                                                      ‫مه‪:‬‬
                                                        ‫جدرمباعی‬
                                                               ‫(ردار‬
                                                                   ‫ودندالی که بین‌ثنیه‌وناب فرا‬
                                                  ‫رباعدات) تامیده م‌شود ‪ .‬رك ‪ :‬صوبر مقایل‪:‬‬

@@@@@@@@ leaf 345 @@@@@@@@
‫از خشم‬     ‫دندان فر و ب‪-‬رکدننابه‬
                                                        ‫اریدن ‪-‬کنابه از‬      ‫زه‬ ‫دندان بخ‬
 ‫اریجد‬
     ‫وبله ورزىدن ‪ -‬واکاسزیبر‬
                           ‫وفهرداشتن ‪ -‬ک‬                 ‫سخنی است که از نهایت دشمنی و عداوت ناشی‬
‫گرفتن ‪ -‬وخام طمه‌ی ‪ -‬وافامت لمودن دکراری‬                                               ‫گردد و کفته شود ‪.‬‬
                                   ‫باشد ‪.‬‬
                                                         ‫دن ‏ کنابه‬     ‫دندان بکام قرو بر‬
‫»‪ -‬مافاء بروزن وععتی‬    ‫د ند ان فر یز ‪6‬‬
                                                         ‫ارکامیاب شدن ومستولی گردیدن ودرغضب شین‬
               ‫دندان بریزاست که خلال باشد ‪.‬‬                                                        ‫باشد ‪.‬‬

‫و معنی‬      ‫‪۰‬ن‬
             ‫دندان فبریرشو‪۱‬ز‬                             ‫دندآن تیز کردن ‪ -‬بمنی‌جبیدن‬

                                                                            ‫(‪ )۱‬چك ‪٣ :‬‏ بدان ‪.‬‬
  ‫‪ ,‬دندان فر مر»‬   ‫رکه ‪ :‬دلدان افرریز » دندان آفر‪.‬یش ‪ ,‬دندان در دز » دندان برش‬               ‫‪۱‬‬

                                              ‫آمریز ه‬    ‫‪ :‬دندان‬      ‫رکه‬     ‫‪۴‬‬            ‫دندان فرش ‪.‬‬
      ‫‪ ۴‬مخفف « دندان آپرش» («‪.‬م‪).‬‬                       ‫دقفت ‪ ۰‬دندان ابر بز ‪.«( €‬م‪۶ ).‬‬     ‫‪ ۲‬ے‬

  ‫‪۰‬‬   ‫‪ :‬دندان آفرش‬      ‫رک‬    ‫‏‪٩‬‬                 ‫‪ 4‬دندان آپریز‬        ‫‪ :‬دندان افرز‬    ‫رک‬    ‫‪۵‬‬

                                                                                           ‫دندان آیریز‪.‬‬
```


## [2026-09-05T17:52:44.156Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==345' BQT_v2_pages.txt | sed -n '1,40p'",
 "description": "Head of BQT leaf 344"
}
```


### [2026-09-05T17:52:45.854Z] TOOL RESULT

```
‫و آنر! حب‌الخطای وحب‌اللاطین خوانند ‪ ۴‬؛‬         ‫اصاری شود ‪ -‬و دام روز ششم کالون ال خر هم‬
‫یکدانگ آن مسپل رطوبات‌بود ‪ -‬وکنیاامهی‌هم‬                                                 ‫هت ‪.‬‬
‫هست‪ -‬وقسی‌از کدابان باشند که شاخ گوسفندی‬        ‫دند = بفتح اول بروزن چند» استخوان‬
   ‫رت رکی چم ک>ا‬
‫بردرخانه ویش دکان مردمان ند وشاخ رایدان‬
                                                ‫پهلو باشد ‪ - ۱‬و دروش ومسکین وبی‌چیزرالیز‬
                                                 ‫کونند ‪ -‬وبمعنی ابله و تادان ‪ - ۴‬وبی‌باك ‪-‬‬
‫شانه بعنوانی‌بکشن که ازآن‌صدای‌غریبی برآبد‬      ‫وخودکام هست‪ -‬ودزد ویی‌دبات را فیز کفهاند‬
‫و چیزی طکلنبند اگر احیاناً در دادن اهمالی‬        ‫اس‬    ‫‪ +‬و آن چوی‬     ‫وافز اری باشد جولاهگابرا‬

‫واقع شود بکارد اعحنای خود را مجروح سازند »‬      ‫دنداله‪ .‬دندانه عرض پارچه که می‌بافند و از هر‬
‫اول ام اوعی‬   ‫وشاخشانه این معنی دارد ‪ -‬وم‬       ‫و یمعدی دندان‬    ‫دندانهٌ آن تاری میگنرانند؟ ‪-‬‬
                             ‫‪.‬‬   ‫از زنبور امت‬    ‫هما هده است که بعربی‌سن‌خوانند ‪ ۳‬وھرچىزی‬

 ‫د ندار‪.‬ه «بروزن خندان» ممروف است‬                ‫عفص که دهاترا بیفشرد مافند مازو(‪ )۱‬و پوست‬
‫ونابه ازطمع ونوقع‬
                ‫که بعربی من‌خوانندا" ‪ -‬ک‬        ‫انار اومثال آن ‪ -‬و خروع چینی را نیزګوبند‬

                                                                ‫(‪ )۱‬چله ‪ :‬ماند ماز۔‬

 ‫‪ ۳۴‬كر ‪‎ :‬نادند ‪.‬‬      ‫‪ ۴‬كر ‪ :‬کند » ‪.‬لگند‬         ‫‪ ٩‬رك ‪ :‬دنده » لدان ‪.‬‬
 ‫‏‪ Croton Tiglium = ۴‬د ‪۲‬كل »هص هکرو ‪ :‬یزد ج ‪ ۱‬ص ‪. ۲-۱ : 1۰۳‬‬
  ‫در اوستا ‪,‬ومارسی باستان ‪ , * 88020 -‬حالت مفرد فاعلی اوستا ‪ 20050‬ت‪.‬‬ ‫‪۵‬‬
    ‫پارسی باستان ‪ , ۵ 80021‬فارسی دند (دندان » دنده )‪ .‬حالت مفرد مقعولنه ‪۵ 0۳6020081‬‬
  ‫« فارسی دندان ( سن ) ‪ ۰‬در اوستا حالت جمم فاعلی ‪ « 6021020‬هوبشمان‬  ‫‪00‬‬
 ‫‪ ۶‬ههلوی ‪« 0810040‬تاوادیا ‪« 820۳21 4۵۱:۷6۰‬منای‪ .۱۷۲۲‬هندی باستان‪. 4114۵ .‬‬
 ‫کردی ‪ . 0811‬استی ‪ . 860081‬بلوچی ‪ 024031‬و ‪n4‘tad,nã‘tna‘d.‬‏ منجی ‪04۳21۰‬‬
‫شغنی ‪ . 020600‬سربکلی ‪ . 000201‬وخی )تمتا اسشق ‪ 4۷۵‬فریز ندی ویر نی‬
 ‫‏‪ «dandun “jili , dãndun‬هک ‪ .‬صا ‏‪ “AA‬ینانمس ‪ . 080007‬‏‪12707 gi‬‬
     ‫سرخه‌یی ‪ , 08۳0۳60‬لاسکردی ‪ 720524‬شهمبر زادی ‪ ۶ 7۳031‬که ‪ ۲.‬ص ‪. ۸۱‬‬
 ‫‪ . 1‬هريك از استخوان هکاویچکی که در داخل ازدوفك برآمده و درجاویدن و عضغ‬
                                                ‫غذاها بکار رود ‪ -‬جموعة استخوانهای مبزور ‪:‬‬
 ‫«گل ‪:‬ان ‪. ۳۳۰‬‬         ‫دندان سگم ودهان مردم بتند ‪.‬‬               ‫آنان که یکنج عافیت بنشتند‬
  ‫دندانها برچپار قس‌آند ‪ - ۱ :‬طواحن (جمع طاحنه) با ات »> که شش درالا وشش در‬

  ‫پابین‌اند و چپار دندانی کهدرءوخر فك قرار دارند نواجذ ( جمع ناجذء ) نامیده میشولد »دوعدد‬
  ‫دربلا ودو عدد دریابین » واینها پس ازهمة دندانهاي دگ اروف وعامه آنهارا دندان عقل نامند‪.‬‬
 ‫‪ - ۲‬ضواحك ( جمع شاحکه) چپار در فوق وچهاردرنحت ‪ - ۳ .‬انیاب (جمم ناب) » دو دربلا‬
```


## [2026-09-05T17:53:03.669Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf for p.120 (leaf=printed+21 => 141) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==142' HRN.txt | head -50",
 "description": "Print Horn p.120"
}
```


### [2026-09-05T17:53:05.462Z] TOOL RESULT

```
=== HRN leaf for p.120 (leaf=printed+21 => 141) ===
- 120 —
542. de^S 'üeschäft, Mühe'.
ai. daksd' 'Tüchtigkeit, Tauglichkeit, Fähigkeit'
(Nöldeke, mündliche Mitteilung).
Die Bedeutung ^Geschäft, Mühe' passt für die
sämnitlichen bei V uliers s. v. mitgeteilten Beleg-
verse; 'finster' ist in den citirten Sähnämevers erst
künstlich hineininterpretirt.
543. deyinif de/me 'Dakhma (der Pärsen); Grab* (bei
Firdüsl auch immer nur zoroastrisch).
g. demd,
aw. da/tna-; phlv. da/mak, da^tn,
544. ded, dede 'Raubtier, wildes Tier.
aw. daitika- wildes Tier (Geldner, KZ. 28, 400;
aber sehr zweifelhaft, vergl. Baunack, Studien I,
385 folg.); phlv. dattk (ys. 39, 2 (4)), datak (AV.),
dal (Men.).
545. (\)der 'Tür*; :^n (Is. 3, 26); vergl. derbar^), derhan,
derwäze.
g. bar; Semn. bart; Käs. bar, ber; Vullers ber
wird auch dialektisch sein-).
ap. duvar- Tür*, duvarayä ; aw. dvar- ; phlv. dar,
dargas; ai. dvdr-^ duräs; arm. durn 'Tür (H. No. 86).
kurd. bar {der^ deri); af/. var; oss. dvar (114);
wa/. bär^ sar. divir, §iyn. dive, divSr, minj. labra,
546. {2)der Praeposition a) 'hinaus, draussen.
kurd. bar 'draussen ; bei. LW.(?) dar, dara 'draussen,
ausserhalb, hinaus' (72); lat. foras, foris.
Nominale von "^dvaram 'nach der Tür hin d. h.
'hinaus gebildete Praeposition. Vergl. berün (No. 252).
b) 'hinein, darin', derün.
phlv. dar, vereinzelt AV. (sonst immer pD).
An die allgemein angenommene Verkürzung aus
ender (No. 119) mag ich nicht gern glauben, ebenso
wie np. tä auch nicht aus päz. andak (s. No. 366)
Phlv. darhär? Vergl. Nöldeke, Kärnämak, 57 Note U
?) Arni. L^\ bar (Hübschmanp ZDMG. 35, 128),
```


## [2026-09-05T17:53:07.146Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT col 653 ===\"\ngrep -n \"^653\\|  653  \\| 653$\" BRT.txt | head -5\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if '653' in l[:400] or '\\n653' in l:\n        pass\n# find dąstra entry\nimport re\nfor i,l in enumerate(leaves):\n    if 'dq&tra' in l or 'dąstra' in l or 'dqstra' in l or 'dqStra' in l:\n        print('leaf',i, l[:200].replace('\\n',' '))\nEOF",
 "description": "Find Bartholomae col 653"
}
```


### [2026-09-05T17:53:09.083Z] TOOL RESULT

```
=== BRT col 653 ===
leaf 470  V.  5.  26:  hai  ut- gfriinlh  apar  i  sür  , .  ha/  api  därishih  apf  i tür;  zu  V.  iS.  30:  apf  hal  äyHilit  i  vair;  zu N.  Äcf:  pa  asräj/iinVi  apar  i  ahuitvar;  zu  V. -    -
```


## [2026-09-05T17:53:19.595Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12600,12660p' BRT.txt\necho \"=== around dantan 12730 ===\"\nsed -n '12720,12745p' BRT.txt",
 "description": "BRT context around daitika/dantan"
}
```


### [2026-09-05T17:53:19.658Z] TOOL RESULT

```
'lehren,  unterweisen',  mit  Akk.  der  Per- son: a^J  a^ä  cSii  (sd.)  aAurö  .  .  zara- 'hustnm  ataxsayaaa^^  (Augm.)*^  vJspa^ farasnt^la  Y.  iz.  5.  a)  mit  Inf.  als  Sach- objekt: kyat  mS  . .  daxsat  usyai  (sd.) *titsna.maiiis  vahistä  Y.  43.  r  5.
mit  frä  i/rS)  dnwS.;  1)  absolut:  äat hwä  a^ra  spttita  fradaxsta  tturr/a  vi.- barm  ".  .  (darüber)  belehrte  Vögel  .  ," Y./aii.  2)  mit  a)  Akk.  der  Person und  Instr.  der  Sache:  /rB  spinta  ärmait! aia  damä  /radaxlayä^  "belehre,  o  heilige Arm.,  die  Daifiäs  über  das  A^d"  V.jj. 13.  b)  Dat  der  Person  und  Akk.  der Sache:  aet^m  md^rTtn  ma  fradaxlayS^ *ainyai  pihre  vä  pu%räi  vä  .  .  VL4.  9.
Vg\.'irradaxJtar-.  —  PO.  (d1ia.]:  faiAärl,  erL: bit  gufl,  Sü.:  fratyabhifala%  pa  daxsak,  Sü.: äkntna ;  frSl  daxiaiih,  Sü. :  praaknalayä  \  J'räc daxsakm,  Sü.:  /raciinaya.  —  ')  Korr.  der  NA. —  »)  Oder  Praev.  af  —  3)  Das  Praererb  ist doppelt  gesetiL  —  4)  S.  aber  Vt.  14.  46,  wo /radaiiayBis,
•  j.  dax^a-  m.  'Brand':    *dasat  ti  mqm
avavata  'sa  (IS.)  ya%a  .  .  F.  22.
Zum  V.  dag- ;  S  5S  ^'-  —  P". :  ^daiisit ;  in  der Hds.  stellt  ptin  statt  dptin;  s.  'daxita-tio.  5.
•  g.  daxSära-  m.  'Zeichen,  Kennzeichen': ka'^ä  (sd.)    ayär}  'rä   fgrasayäi   diiä    Y.
43-1-
lEt.  vgl.  'daxlta-.  —  Pü. :  daxiak,
•  j.,  g.  'daxäta-  n.  'Zeichen,  Kennzeichen, äusseres  Merkmal':  a/  tat  mdi  'tsm  data aAyä  atjAsus  vlspä  mai^ä  (sd.)  \-J4  6;
—  yqm  xsnütpm  räniiiyä  (sd.)  da  ..  aiAf aAvsAB  't»m  davBi{%A.)'^.$i.');  —  narym . .  aiavamm  *jas»nitm  aAmya  nmäne  mat avabyS    -inbyö'-'^  ydka    äiraz-a   V.  ij.  22;
—  dttxstanqm    (s.  a)  ySi    h>nti    aaraAe
dby  Google
677
'daxSta-
daJfvah-
678
mainyJtd  'ttm  mafyäi^ia  faiti  nSüÜ^m  V. z.  39.  a)  von  sichtbaren  körperlichen Mängeln  und  Leiden:  anäisca  kannis^a ..ava  -/«(IS.)  daxstavatUa  yä  rßit  peuru.- jira  (sd.)  fradaxita  Yt  5.  93;  —  ma  a%ra fi-akavö  mä  apakavS  .  .  tnüta,iSm  anyqm •tanqm  (Gen,  part  als  Subj.)  yBt  hmti anrahe  mainySus  daxStim  (s.  o.)  V.  2.  29;
—  paityanm  fräktnntat  a?»rs  mainyus ,.  arä^wyäca  'ia**  ari^wlmla  garimäum V.J.  18;  17.  b)  von  den  periodischen 'Merkmalen'  des  weiblichen  Geschlechts  J*; «)  bei  Menschen  "Regel,  MenstiuatioD': .  .  yat  .  .  näiriiayS  n^ravaityä  daxita- vaityä  vohunavaityS  't»m  uzvfnsyäi  "wenn (man)  . .  einer  . ,  Frau  die  Regel  ver- treibt" V.  /6. 1 3  <' ;  —  mä  ..  a£a  yä  Maine tarS  't?m  parayäl  (Sp.  1 52  u.)  V.  15.  9;  9;
—  yat  hi  cti^ra  fsd.)  'AM  bavatti  yat  hs •ta  aknm  bavaili  V, /ß.  I4(?);  —  Vii  F. 14.        ß)  bei  Tieren  (nur  Komp.).
Koi^E.;  Ableit.  —  np.  vgl.  daitän  'Frau,  die die  Regel  hat'.—  Vgl.  »fradaxUa-.  —  PB.  (lu Y.  J^  V.  2,  13,  l6):  daxsai,  Sü.;  ciknam;  (zu V.  /,  75):  daitän,  (lu  Y.  ßi):  daziln  «;  5.  noch No.  2,  4.  —  ■)  Die  fem.  sult  der  neutt. FormjS  412.  %A.  —  »)  Pfl.:  aparSnia  daitän, erU:  ilakmaklar  trwel.  —  J)  Abweichend  Gdn. 3Vt  ii9i  s.  aber  V,  J.  59.  —  *)  Vi.:  ia  . . daxsai  ucvanet,  erl. ;  dai/än  nihätt  apäl  iunfl, —  S)  Die  Hds.  haben  das  Ideogramm  für yaxisn;  JD  der  Urschrift  stand  dpu«,  vgl.  zu
•  j.  'daxäta-  n.  'Gerät,  Gerätschaft':  bis hapta  äirS  'tftit  mrtbyS aiavabyS..msiri- nuyäi  "14  Feuergerätschaften'*  . ,"  V. 14.  6.
Et,?—  VgLnp.  lÄjjrj 'Geschäft'?  Mit  Voii/a- {i.  PQ.)  Teraag  ich  das  Wort  nicht  za  ver- milteln.  —  Pü.:  dojisai  (s.  'dajcila-).  —  ')  Der folg.  $  sollte  die  Aufzählung  enthalten;  er bringt  es  aber  nur  bi»  auf  6.
•  j.  daxsta'vant-  Adj.  (fem.  'vaitf-)  'Merk- male, Zeichen  (körperlichen  Gebrechens) an  sich  tragend':  ava  daxsta  'vaniaCSP.) yä  tidil  pouru.jira  (sd.)  fradaxsta  Vt.  j. 93.  a)  nur  fem.  'mit  der  Regel  be- haftet, menstruirend''';  yai  ahmi  nmane .. tairika  •vaiH  anhat  V.  5. 59;  16.1;  — yB  nairikqm  cihravaillm  'Z'aitTm  voiuna- vaitlm  ,  .  xSudrh  avi  frattlutr^zaiti  V.  18. 67;  15.7;  —  näirikaya  ..  'vaityä  V.  16. 5.  «3.   »4-
Pü.:  daxIaiSmand,  (zu  V.j):  diütäa.  —  ■)  S. lu  c&riniattl-  No.   l.
•  j.  daxämaestay- *)  f.  ein  Längenmass*' :
bis  aSavat  *'tis*'  yavat  yujyasHi  (sd.)  F. 27  a;  —  °Hm  altai  barpsma  yat paiti  sp3m franayanisma  N.  /©(?).
•}  Soviel  als  8  Hä%ra,  die  Hifle  einer  Yujya.
Et.  und  Bed.?  —  Fa.:  Iransskr.  {daxSmestS, dahncst).  —  ')  SoN./Oi  dafür  spricht  Pü. — 'i  Hds.  'maitü,   —   3)  So  aacb  Nir.  Bombay
•  ].  yB  "daiti  xraaili"  bavaiti  V.  13.  34 PüZ.
S.  lu  ^xraciti.
•  '].,  g.  daitika-  m.  'wildes,  nichtdomesti- zirtes  Tier'*':  pasuianqmcä  .  .  'kanqmiä aidyBnqm  (sd.)  urutm  Y.^p.  2;  zit  Yt.  y. 154;  —  urunB  pasukanam  .  .  'tikanam Vt.jj.74.
•)  Sva.  ravas/aräl-  (sd.).    Nach  Mi.  6t.  1 1  ist
der  Hase  {j^argöi)  der  Ralmi  der  datSn,   womit
daitika-,  nach  Bd.  24.  9  der   der  fr,ii^  raftärän,
womit  ravasiaräl-  wiedergegeben  vrird.  Weiteres
bei  aidyü:
Ableit  aus  *dattl-  m.  'Zahn',   5.  dantan-   (Sp.
ArP.  47),  bedeutet  also  zunächst  nur  'reissen-
des  Tier';   vgl.  ai.  vyäghräm  datz-ätäm  . . pra-
Ihamänt    AV.  4.  3.  4,    ferner    dam}lrin'    und
j.  liii.dqslra-,  —  mp.  dat,  np.  dad,  dada  "wildes
Tier'.     Vgl.    DsT.    6tlr.   3.  150;    falsch    Bn.
Stud.  I.  386,  Ggr.  OK.1OZ.  —  Pü,:  dailikän
(Transskr.),    Sü. : /in^/iV-j«  (daher  Gü.  'Fuss-
Soldat').
j.  ddhiili:  s.  unter  *di-  und  'dä(y'): j.  dadusaos  Vi.  14.    11:  lies  vakqm.ians,
•  j.  daSa-  Adj.  i)  'gebend,  schenkend': Ab  °ls  as»m  upa.raalaydte  (sd.)  yB  drvaite *dalaiti  P.50.       2)  'schaffend;  Schöpfer"
(sva.  da&vah'):    urva^pm  staotär^m  van- hatikam  (sd.)  '%B  aoxta  ahurS  mazda    Y. 10.  9, Zum   V.   da-;    red,  Bildung;    vgl.   Wii.   Gr.' S  114S.  4.  —  ai.  'dada-,  'dadha-  Adj.  —  Pü. : ausgelassen;  Sü.  (zu  V.):  adadäm. j.  ddiaöis  Vyt.  $0:  lies  ditöii;  i.  'dä(y); g.  dadaiti,  dada/,  daduyi  usw.,  Verbalf. :    s.
^dä:
•  j.  daiJant*  Adj.,  PPA.:  s,  'da-  mit  No.  4,
g.  daidyal,  j.  daiiya,  daHyama:  s.  'däfy)-,
•  j.  daiSyant-"  Adj.,  PPA.:  s.  'da(y): >l  Ob  für  diiy  (S  368.  9)?     Vgl.  liüayatil:
•  g.  daidyäi  Inf.  'zu  geben,  zu  gewähren': tat  vS  fiS  hazaosauhs  (sd.)  VTSpaahB  d' savB  Y.  57.  20.  \in}ncä  daidyäi  Y.JJ. 5:  s,  unter  ma/id-.]
Zum  V,  da-.  —  Pü,:  daiiin.
•  j.  daSvah-  :  dadus-,  da'^us-  Adj.  'der geschaffen   hat,   Schöpfer;    schöpferisch':
dby  Google
679
dadräna-
da%u!s  äaduiS  'daibTs  raoMli  (als  AP.) Aam.vamdimaiäf  "möchten  wir  des  schöpfe- rischen  SchSpfeis  schöpferisches  Licht  zu sehen  bekommen"  Y,  5Ä  6  (?)  '*.  A)  sonst nur  von  AhM.:  yS  '%va  ahurS  masää  Yt 5.17,  10.50,  /J.83,  75.2,4,  V.2.30,  7. 53,  22.7;  —  ahuTTm  tnazäqm  .  .  °%vSt»- A^m  rapantgm  tarlväahfm  vUpa  *vohB  Y. 70. 1 ;  6.1,  16. 4,  S,  6,  S.  2,  8,  1 5,  23,  V, iS.-j;  —  °%usS  oAuraAe  mazda  Y. /.  i, 4.7,16.3,  22.1;  Yt.  13.78,  Vyt 46;  — 'huiä  ahuräi  matääi  am^iünamla  sf>nta- nqm  Yt/J.is?;  15.44.  V.J^'.4,  Yyt  51;
—  haca  '%ulat  mazdi  Yx. $.  7; —■  ys  °%va sf^nts  mainyus  \L  10. 143;  — '^usS  'dtisö dadOibÜ  (s.  o.)  raocibls  Y,  j&6'';  — *xi»ümaine  '%usS  N.  4j.  a)  da'äusS et)  (nämt.  mä)  heisst  der  10.  Monat  im Jahr:  aiiaiilm  maihyäiryehe  (sd.)  '"^usö v>r3%rafnafu  k.3. 11.  ß)  (nämL  ayars) heisst  der  8.,  15.  und  23,  jedes  Monats: °^us3  akurake  mazds  ratvalS  . .  S.  i.  8, >S.  23°';    vgL  2.8,  IS,  23,    Y./6.  4-6;
=== around dantan 12730 ===
day-  1  I
684
•  j.  datShtLsrüta-  m.  ER  eines  Gläu- ! bigen:  Hake  asaond  YL /j.  116.
Eig.  'im  Land  berühmt'.
•  j.   daiBhuS.aiwiätar-   m.  'Eigner  des ,
Landes,  Landesherr*;  vanmm  yim  ca%ru.'\ gaosfm  . .  ake  paityänat  fräk»r>ntat  avrS ! mainyu!  araiiwyUca  daxsta  (sd.)  anair- yala  'Iura  (als  AP.)  ". .  und  nichtarische Herren  des  Landes"  V.  /.  17;  —  vpa aoia?su  ranhaya  .  .  ake  paityärim  frä- ifryrUat  anrS  mainyui  zyam'a  . .  taoiyäca (sd.)  'iura  V.l.  19. Komp.  mit  NS.  im  1.  Glied.  —  Pü.:  aitfr diAän  apar  mäminth,  (za  V.  r.  19)1  fehlt.
•  j.  daiöhu-ian-  Adj.  'der  sich  das  Land verdient,   erworben   hat":  paoiryqn   tkalsS
. .  santunamca  dahyunamca   .  .  zantusänS '/ans  (als"  AP.)  YL/j.'isi. Komp.:  dairiAa!'-'i-*'A/iii-.
•  p.  'dao-  V,  'fliessen'.    Praes.  10  äanu-.
pirävc^  näm<^  rautt^  tyt^  mudräyaiy danuvatiy'^  ". .  Nilstrom,  der  in  Ägypten fliesst"  D.  ij.  3. ai.  dhÖHT/ali  'er  rinnt' ;  np.  vgl.  äaiiidan,  — ')  Them.,  wie  ai.  dhanvati.  Doch  ist  auf  der Inschi.  nar  d"»"»  la  lesen,  es  könnte  das Wort  sonach  auch  darmlaiy  gelautet  haben.
•  p.  'dan-  V.:  s.  unter  *tan:
•  \.  danar-''  n.  'Portion':  hai  :^ar7i-}m .  .  hiat  yaom  (sd.)  frabaräti  dva  'nars tJysirinam    afva    °nar»    *xS3u4rinam    V.
Zum  V.  ai.  däyait,  gr.  äai'irai  'er  teilt  aus''). —  mp.  (Pü.)  vgl.  dänar;  s.  daiu  HoRN  NpEL lt]i.  —  ')  So  der  Bed.  wegen  wahrschein- licher als  zu  ^ää-;  doch  s.  freilich  gr.  i»'(. g.  dangrä  Y.  46.    17:  lies  danr".
•  g.  dant-  Adj.,  PPA,:  s.  'rfj-. KompE.
•  j.  danta*  Adj.    —  ?  — :    frazaintlmca  hö
vpmzyät  daar^  -10  Aizuxts  Yt  15.  40  '>. Wertlose  Stelle;  s.  No.  —  »  Der  Verfertiger des  Stucks  mag  Y.  32.  4  im  Kopf  gehabt haben,  wo  dattrö  (zu  dan/-)  in  Pü.  mit  daAiin, aber  in  Sd,  mit  jnänT  gegeben  wird.  Vermut- lich hat  er  mit  »einem  Wort  die  Bedeutung 'klug'  verknöptl  wissen  wollen.
•  j.dantan-m. 'Zahn':  •««J(NP.)'>F.^d.
KompE.  —  Vgl.  ff'ii/J-,  dairita-  und  zu  tiii.- difilra:  —  ai.  vgl  däal-  m,;  s.  zu  Suhtm-.  — ■)  Vn.  ist  das  Wort  aus  vTmildJantänS  ab- geschält.
•  j.,  g.  dam-  (:  -d»/!-)  m.  'Haus,  Wohnung' : hyat  k5i  aia  vohucä  cOiH  (sd.)  manaukä xlakröi    hSi    haurvätä    amintätä    ahmäi
sOi  dqn*'  fytitÜ  utayBitI  ". .,  dass  uns  in seinem  Reiche  Wohlfahrt  und  Unsterblich- keit, in  seinem  Hause  Kraft  und  Bestand werden  sollen"  Y. 4:5.  10;  —  s^ahmi  dqm^'^ .  .  x'aAmi  xs'd^re  Vr.  14.1;  —  at'  &Si dümqm  HwaAmi  3  dam'^  ahurä  "seine Stätten   werden   in   deinem   Hause    sein,
0  Ah"  Y.  48.  7  ;  —  taten  matdä  'i^wahml a  *dqm^'>  '>  nipAr»Ae  mans  vohB  umnascä  . . "und  das,  o  M.,  will  ich  in  deinem  Haus-*' in  Verwahr  geben:  den  guten  Sinn  und  .  ," Y.  4;^.  10;  —  ila  asti  .  .  sp>nta  ärmaitis mana  (oämL  ahurahe)  dqmi'^  Yt  i.  35; 25*;  —  äkästSng  (sd.)  mä  msqsya  ds^Jm djAvä^LP.)  Y.50. 2;  —  ySi  ..  aiamgm  va- rtdtn . .  tsi  dalvifig  dqn ''  ya  drpgvatS  datnä (Sp.  666  o.)  Y49.4.  '  a)  GS.  la&patay-  m. '(Hausherr  sva.)  gebietender  Herr,  Ge- bieter': saoiyants  dJrtg  (GS.)  patsU  spmlä dainä  urvais  *brata  *pts  va  mazda  ahurä "des  Saoiyant,  des  gebietenden  Herrn heilige  DaSita*^  wird  (ihm)  Freund,  Bruder oder  Vater  sein,  q  MAA."  Y.  4:5. 11.
KompE.  —   zFIm,  S  rS/,  403.   —    ai.  däri-
m.  (,  fiätir  dän),  arm.  tun,  gr.  iäfia  (,  Jnwonjs)
usw.;  vgl.  dii«ä«a:  —  Litt.:  IF.  8.  J36,  KZ.
^5.1111  dazu  noch  Hbm.  AGr.  7.49S,  Oldek-
BERO  SBE.  46.   176,  ZDMG.  SS-  *90.  Uhlek-
```


## [2026-09-05T17:53:32.477Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT col 653 ===\"\ngrep -n \"^653$\\|^  *653  *$\" BRT.txt | head\ngrep -n \"653\" BRT.txt | sed -n '1,20p'",
 "description": "Locate BRT column 653"
}
```


## [2026-09-05T17:53:34.069Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 4.27 tooth (leaf = 138+24 = 162) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==163' SYN.txt | head -60",
 "description": "Print Buck p.138"
}
```


### [2026-09-05T17:53:34.154Z] TOOL RESULT

```
=== BRT col 653 ===
25833:Et  und  Bed.pa).  —  I'ü.:  a/sii  (nur  wegen  des Aaklangs)}).  —  ■)  Mx.  2. 133  hat  dafür  folgende Paraphrase:  »  iai  ätt  ku  tas  \ki\  slaxm  u  apar kart  u  vek  martum  biiil  u  tar  karl  u  ^ästak hal  balak  handSxt.  —  ^'l  ay  wohl  fUr  iy,  %  368. 1 1.  VII.  ist  das  Wort  verderbt.  —  J)  Falsch Dst.  ZA.  2.  653 ;  vgl.  HoaN  NpEt  33.
27523:•  ].,  g.  zaotar- ;  zaoSr-  m. 'Priester,  Ober- pricster';  y7  (näml.  zara'husirö)  *fä  a/ä tnzü/  .  .  kaya  (Sp.  46a  m.)  S.. 33.it;  be- nutzt Yt.  4.T.  yi  °ta  sarähustrS.  A)  im jAw.  Name  des  vornehmlich  mit  dem Vortrag  der  Gä'iäs  betrauten  Oberprie- sters, der  den  Gottesdienst  zusammen  mit sieben" Unterpriestem  (s.  'raiav-),  im  Not- fall aber  auch  allein  (s.  N.  Si,  Sp.  1653  ra.) vollzieht:    'lanm    asavanim    aiahe  ratäm
27566:•  j.  'zaoöra-  n.  'Amt  des  Zaotar,  zaotar- amtliche  VenichtUQg':  zaota  (Sp.  1653  u.) anahaxiS  . .  dqkistäi . .  °r»m  raixiaiti  N. 80;  —  ''kahyäcii  nä  dahmanam  (Sp.  705  0.) •rlSu  raiu/ris  näirikasat  aptrmäyBka- keHt  yesi  vaiha  h3%anqm  . .  *'/raiauru- nss(sd.ya  N.40.
```


### [2026-09-05T17:53:35.884Z] TOOL RESULT

```
=== SYN 4.27 tooth (leaf = 138+24 = 162) ===
ut best explained as starting in a *pa-diktorika (cf. pa-dusti, etc., above), whence an abbreviated *nadtortika > pastortika, with new masc. formed from this. Miklosich 55. Meil- let, MSL 13.28. Otherwise Zubaty, Arch. sl. Ph. 18.815 f. Still otherwise M. Vey, BSL 32.66.
Pol. pasierb ‘stepson’, pasierbica ‘step- daughter (also Russ. dial. paserb), epd. of pa- (as in Lith. pa-dukra, ete., above), the second part being much disputed; taken as *serbi% by transposition from *sebrit (*sebri in OSerb. sebrii ‘free peas- ant’, Russ. sjabr ‘neighbor, friend’) : Goth. sibja ‘kinship’, by Solmsen, KZ 37.592 ff., Walde-P. 2.456; as ‘one who does not suck the same milk’ fr. the root of sorbaé, Lat. sorbére ‘suck in’ by Briick- ner 398.
Boh. new series nevlastnt otec, etc., lit. ‘not own father’, etc., from neg. ne and vlastnt ‘own’.
7. Skt. only late and rare words tata- yaviyan- ‘stepfather’ lit. ‘younger (later) father’, dvdimatura-bhratar- ‘stepbroth- er’, lit. ‘having two mothers’.
pe CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
igitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
130 2.75 ORPHAN
Goth. widuwairna Lith. naflattis, -é a eee ON = fodur-(mddur-)lauss Lett. baris 4 Lat. _ orbus, piipillus Dan. /foraldrel¢s ChSl. siril, strota It. orfano, -a Sw. férdldralést SCr. sirote ; Fr. orphelin, -e OE _stéopcild, stéopbarn Boh. _ sirotek, sirota Sp. huerfano, -a ME orphan Pol. sterota Rum. orfan, -¢ NE orphan Russ.  strota Ir. dilecta Du. —-wees Skt. (anatha-) Nir. _— dilleacht OHG weiso Av. saé W. amddifad MHG weise Br. emzivad NHG_ waise
1. Grk. dpdavés (also dpdo- in dpdo- Borns), Lat. orbus, both also adj. ‘bereft’ (either of parents or of children), Arm. orb ‘orphan’: Goth. arbi, OE ierfe, OHG arbi (NHG erbe) ‘inheritance’, Ir. orbe, orpe ‘inheritance’, Skt. arbha- ‘small, child’, etc., IE *orbho-, root con- nection dub. Walde-P. 1.183 ff. Er- nout-M. 710.
Grk. épdavds > late Lat. orphanus, whence It. orfano, Sp. huerfano, Rum. orfan, all with fem. forms in -a; OFr. or- fene (> ME, NE orphan with old spell- ing restored), dim. orfenin, Fr. orphe- lin, fem. -e. REW 6105.
2. Lat. pipillus ‘orphan, ward’, dim. of pipus ‘boy, child’ : Lat. puer ‘boy’, etc. (2.25).
3. Ir. dilecta, NIr. dilleacht, cpd. of neg. di- and slicht, NIr. sliocht ‘race, family’, hence lit. ‘without family’. Pedersen 1.84.
W. amddifad, Br. emzivad (MBr. em- dyvat ‘abandoned’), fr. *am-di-mat-, cpd. of am- ‘about’, neg. di-, the last part : Ir. maith ‘good’, hence ‘on both sides in (or simply in) mis-fortune’, ‘unfortu- nate’. Pedersen 1.487, Henry 113.
4. Goth. widuwairna, deriv. of widy- wo ‘widow’ (2.76), so ‘widow’s child’.
ON fodur-(or méddur-)lauss, lit.
```


## [2026-09-05T17:53:42.712Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==171' SYN.txt | head -70",
 "description": "Print Buck p.138"
}
```


### [2026-09-05T17:53:44.353Z] TOOL RESULT

```
eathach), deriy, of beatha (gen. beathadh) ‘life’ : béo ‘live’, etc. (4.74).
Br. loen, MBr. lozn: W. Ilwdn ‘young of animals’, Gael. loth ‘colt’, root connection obscure. Pedersen 1.135.
5. Goth. diws (renders Grk. Onptov), ON dyr, OE déor, OHG tior, etc., the general Gmc. word for ‘animal’ yg, ‘man’, but in part restricted to ‘wild animal’ (or even further specialized, as in NE deer) : Lith. dusti ‘gasp’, dvésti ‘gasp, perish’, ChSl. dychati ‘breathe’, etc., parallel to Lat. animal fr. anima. Walde-P. 1.846. Feist 121b. TFalk- Torp 172.
6. Lith. gyvolis, Lett. dztynieks, ChSI. awott (‘life’ and ‘animal’), SCr. Zivotinja, Russ. Zivotnoe, Boh. Zivocich (mostly re- placed by zvife), fr. Lith. gyvas, Lett. dzivs, Slavic Zivii ‘living’ (4.74).
7. Skt. prdnin- (‘living creature’, man or beast, but not common for latter), deriv. of prana- ‘breath’, this fr. pra- and an- ‘breathe’.
Skt. pagu- mostly ‘domestic animal’ (3.14), but also ‘animal’ in general (so RV 10.90.8 pagién vayavyan aranyan gramyadncca ‘animals of the air, the forest, and the village’, and elsewhere, ef. BR).
Skt. mrga- ‘wild animal’, esp. ‘deer’ : Av. maraya- ‘large bird’, root connection dub. Walde-P. 1.275, 284.
Av. srafstra- ‘beast of prey’, etym.? Walde-P. 1.486. Barth. 538.
Av. daitika- ‘wild animal’, deriv. of
*dant- ‘tooth’. Barth. 678.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
ANIMALS 139 3.12 MALE 3.13 FEMALE
_  Gponv, &ppnv Oidus oe Repeats OnAuKés Lat. © mds (masculus, etc.) fémina It. maschio femmina Fr. méle femelle Sp. macho hembra Rum. bdrbalesc femeiesc Ir. fer-, f trend ban- Nir.  fireann baineann W. = guryw, gwr- benyw Br. par, taro- parez Goth.’ ..:. sees ON  karl- kvenn- Dan. han- hun- Sw.  han-; sb. hane hon-; sb. hona OE hé héo ME sihe-, male female NE male, he- female Du. mannelijk; sb. mannetje vrouwelijk, wijf-; sb. vrouwtje OHG ? ? MHG ? ? NHG wmédnnlich; sb. mannchen weiblich; sb. weibchen Lith. vyri8kas (patinas sb., of birds) moteri3kas (patelé sb., of birds) Lett.  virisks (tévin¥ sb., of birds) maté, matite Chsl. ? ? SCr. muski Zenski; sb, samica Boh. samec samice Pol. samiec samica Russ. samec samka Skt. _- vrsan-, pums-, nara- -dhenu-, stri- Av. argan-, nairya- datnu-, sirt-, hairi8i-, xsafri-
3.12, 3.138. 1. ‘Male’ and ‘female’ as applied to animals are in part expressed by the same words as those applied to human beings (2.23, 2.24). Some of those, like Grk. éponv, Skt. vrsan- from the notion of emitting semen, or Grk. Bidus, Lat. fémina from the notion of giving suck, were from the beginning equally applicable to animals. Of those derived from ‘man’ and ‘woman’, many were extended to apply to animals, but others were not. Thus NHG mdnmnlich bee are used of animals (OHG, : Be words so used?), while Dan. mand- é peice, Sw. manlig, kvinlig are still
```


## [2026-09-05T17:53:53.682Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'^\\s*65[0-9]\\s*$', l, re.M):\n        nums=re.findall(r'^\\s*(6[45][0-9])\\s*$', l, re.M)\n        print(i, nums, l[:120].replace('\\n',' '))\nEOF",
 "description": "Locate BRT columns 640-659"
}
```


### [2026-09-05T17:53:55.501Z] TOOL RESULT

```
379 ['654'] �ml.  ayan)  heisst  der  13.  Monats- tag: 'ryeie  stärJ  ra^fa/ff  s^armanuhaiS S.Z.  13;  vgl.  2.13,  y.i6.4. ♦)  7:
380 ['655', '656'] Y.4i.y,  —  ä  ta  mg  altayä zao'hraya  frtmhardis  Yt.  j.  9 1 ;  —  vasas^a ta    ahura    .  .    xfagia  Y.  S.  5
381 ['658']  türa-  m.  EN.  eines  Gläubigen**: arsJatfuAatö  'rahe  aiaotas  Yt/5, 113;  — /rärazSil  'rahe  asaonS  Yl  13. 123. 
382 ['659'] va- (Sp,  166  o.):  ya^säm  Aa/ama*  ahahyJ' . .  avi^  *akunavayi^t3  Eh.  7.  7 ;  D.  6.  3,  4; —  •_)'«*  kunavahy
```


## [2026-09-05T17:53:58.105Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==379' BRT.txt | head -40",
 "description": "Print BRT leaf 378 (cols 653-654)"
}
```


### [2026-09-05T17:53:59.482Z] TOOL RESULT

```
,  464.  —  3)  Kann  auch  auf BT.  *lansra-  gehen.
•  j.  ti^'d-rö. JUnah- '^  Adj.  'der  nach  dem Dunkel  verlangt,  das  Dunkel  liebt':  'änS (NSm.)')  ya>,a  läyus'  ..  'änO  (NSm.)« ydka  disul  V.  13.  41 .
Pü.:  lärti  iämai.  —  D  Var.  'An*.  —  »)  Nach der  n-Dekl.,  S  j8fi  vgl.  haema^anfm.
•  j.  t^Oxya-  i)  Adj.  (fem.  yä-)  'dunkel, finster':  °fyam  aipi  xsapanim  Yi.  14.  13; —  'ryasäi  (GSf)'>  kala  xsafnS  "auch in  finstrer  Nacht"  Yt.  1^31,  ib'.  10;  — xfapa  vä  *'ryä  (GSf,)"  aipi.dziqnaraya YL//.  4.         3)  n.  'Dunkel'  (nur  Ableit).
Ableit.  —  Ableit  an»  /riSra-.—  Pü.:  tärti.— I)  Nach  der  (-Dekl.;  s.  anderseits  ktU<U.p<ü- manynm  und  ^^oitumaAyint.  Vgl.  den  Unter- schied iwiichen  ai.  ianyäh  und  jAw.  kainyS AP.,  sowie  S  408.  —  »)  So  J 10.
•  j.  biSrySvant-  m.  EN.  eines  Ungläu- bigen, den  Vlitäspa  besiegt:  .  .jiazata  . . viitasps . .  yat  bavani  aiwi.vanyä  'vanttm dusdaimm  Yt.5. 109;  5.31.
'/jiiyoii'ai/- Adj. 'lenebtosns'»).  —  ■)  o  »uYt. 5;  s.  auch  J  10  m  Yt  19.  87.  —  »)  Eine  An- spielung auf  dieTan/i-a-Fhilosophie  der  Inder fso  JK.  Zar.  210  No.  4)  vermag  ich  in  dem Namen    nicht    zu  erkennen;    s.  auch  zu  gan.
dby  Google
6S>
tifäyah-
65a
•  j.  t^yah-  Adj.  (fem.  •yeil-)  'der  tapfrere,  |  xiapatis  .  .  'rys  .  .  kshrpm   ra^wayäti
energischere,  heldenhaftere':  fravalayB  . yä  'yehli  (NPf.)  ahmäl  .  .  yaHa  vaca  fra tnraväire  (sd.)  Yt.  13.  64. KompE.  —  Kompar.  zu  laxma: j.  liurva  N,  6^;  lies  lüirya.
•  j.  'tiyra-  (,  p.  t^ra-)  Adj.  'spitz,  spitzig' iarsasat(sd.)/rai3raySi/'°ra{lS.)  x/a^ra
spähe  kihrpa  aurusake  .  .  äal  paiti avaiti  .  .  avi  zrayS  vourukasttn  .  .  ä  äim paüi.yq^  nisdvaraili  daevS  yS  apaoiö aspahe  kfhrpa  iümahe .  .  kam  läcit  bäzus barats  . .  'ryaica  . .  -vasca .  .'täyüitya%ö  . . a    rapi^winfm    srvämm    ä    Mm    bavatli
'.ao/ä  . .  daiüm  yim  apaohm  apa
*vairya  V.  5.  i  o ;  —  vispaca  avi  'ra  ( APn.)  j  alät  iiyeiti  Yt  Ä  1 8  -  2 1  und  2  8  f. ;  —  -nm *iumata  (sd.)  Y.3.  35;  —  arstayasai  ■  ■ ,  stänm  rasvantim  :^armat3uhant)m  yaza- huxinuta  "ra  (NP.)  Yt.JO.39;  —  'ratihö \maide  .  .  yS  pairika  Htärayäü  ya  starS astays  Yt  10.  II  i.  k^nma  patanH  aniart    tarn    asmarumca
KompA.  —  Zdu  aL  V.  ttjaie  'sticht'.  —  Pü.; ,  Vt  A>  b.    ,    ,    ,,    ,,    ,_     '      ,_     ,0  _    _ eh  («  di*  /-«.-Lesung.)  ^  I  „^   ,■  l',    ''  ''  "■  !5-  S^.   '2   27.   18.  5,  7
.  p.  =ligra-    m.^  Name    emer  Festung  m  („äjnl.  pairil-S)    ys   taurvaydti    viväiH
Armenien":  °ra*  nama'  dida  armaniyaiy Bh.  2. 8.
*)  Nach  JusTi  GlrPh.  2.  42g  "das  heutige Fort  Till  am  7y-/«.  «o  die  Strasse  nach  BitlU abzweigt".
•  p.  tigra-xauda-  Adj.  'spitzhütig,  spiu- kappig">  als  Bezeichnung  einer  Abteilung der  Sak^xi:  sakai^A.)  'da  D.6'.3.
■)  Vgl.  die  Abbildung  des  letiten  Empörers auf  der  Bahislänvci'scb.T^it  und  Uerodot /.  64.
•  j.  tiyray-  m.  'Pfeil':  ya^a  •ris  mainya- i-asa  yim  aahat  >r?xsS  (sd.)  Yl  S.  6.
Vgl.  'li-jra-.  —  np.  tir.
•  p.  tigrä-  f  Name  eines  Flusses,  Tigris : 'räm  viyatarayamO*  Bh.i.  18; S-4i — isra* Jiya*  nadriabairakyil  °ram  adilrayt^  Bh. /.  18.
Stammansatz  und  Geschlecht  unsicher.  Die Namensfoim  berohl  vll.  auf  volksctjrmologi- scher  Umgestaltung  des  nicht  iranischen Namens,  vgl,  tiira-  und  titraj/-.  Das  Mp.  hat i/iilat;  Aü.  iätlat,  Eu.  Ii^p-a.
•  j.  titarant-  Adj.,  PPA.:  s.  'tar-,
j.  änqni   N.  p^:  lies  lanüm.
•  j.  tin]a  Ad?,  'zurück':  f  avat  handag- sayaauha  (sd)  "zurück!  .  ."  Yl  ig.  50.
Vgl.  -V^.
•  j.  tiro.nakaS'wa-  m.  EN.  eiues  Gläu- bigen: 'TiwaAe  uspaliatanqin  (sd.)  salria- nam  Ytij.  126.
'Eig.  Bed.f  —  »ßra-  n.  Name  einer  GoMheit; vgl.  Tipiiärr,;  usw.;  s.  NöLDEKE  PersStud.  r. 33.  Mbm.  AGr.  I.  88.  —  *iiai^^:L-a.  n.  er- innert  an  ai.  näk^aOa-  n.
•  j.^tiätrya-  m,  Name  des  als  Gottheit
verehrten  Fixsterns  Sirius*':  k(^a  «^  ««['■rf^m.fe'' "..wie  (das  Antlitz)  des  Ti'^yyö^ uzyarät'ry^  rafvii  :^arffia»uka  ka%a  xä  stems"  Yt/o.  143.
..apqm  tachnti  navat  YtÄS;   13,  ao,  23,        Komp.    wie    aL  inmüaruh   'der  S.  genannte 28,  29,  32,  40,  4j,  55,  60,  Ny.  /.  8^  (statt'     ^"""'  "'"■  ~  '*  '^'"'"■ AS.);  Vt.(V.  22  ("ryasca):  —  "irityä  dasa'»  j.  tiSr-  fem.  Zw.:  s.  ^ray-.
Ais  srayataAai  h(üa  vourukaiat  äaf  maf/a us.fravSfite  .  .  Yt  Ä  40;  —  ~'y^e  stärS raevat5  i^armauuAatS  YtS.  o,  56,  57,  Y. I.ii,  27.2;  —  'rim  drvB.caimamm  Yt ■Kr 2,  Ny./.8.  a)  Hstryehe  a)  (nämj. mä)  heisst  der  4.  Monat  im  Jahr:  xA/aäim *mailysiümahe  (sd.)  'ryeke  da^usS  A.  3. 8.  ß)  (n�
```


## [2026-09-05T17:54:16.811Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12280,12295p' BRT.txt\necho \"=== leaf 378 head (col 651-652) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==378' BRT.txt | grep -n \"difilra\\|dqstra\\|dqSlra\\|tii\\.\\|tiii\" | head",
 "description": "Check BRT tiži-dąstra entry"
}
```


### [2026-09-05T17:54:18.535Z] TOOL RESULT

```
VgL  ttüyaritay-  EN.  —  »>  So  Yt  15.  48.  — >)  Kasuiausgang?
•  j.tizLasüra- Adj. 'mit  scharfen  Hauern  (?)': varHsahe  . .  'rahe  Yt.  14. 75.
Bed.uiidEt.Ton*«iHra-?  GDN.3YL64 "Borste', DST.  ZA.  2.  565  'griffe'.  —  Npü.!  ßr  lang, ßz  fäi.
•  j.  tizi.daä-  Adj.  (mask.  'ta-)  'mit scharfem  Gebiss':   urupii  (sd.)   'iahe  V,
Vgl.  lU  tSi.dnstra:  —  Vn.i  IB  dandSn.
•  j,  tüLdärä-  Adj.  (mask.  'ra-)  'mit selber  Schneide':  tas?m  'r»tn  tizUnlUam "eine  Axt  mit  scharfer  Schneide"  V.  74;.  7,
Po. !  lli  alAAi.
•  j.  tizi.da_sura-  Adj.  'scharfbeissend,  mit scharfem  Gebiss':  spämm  . .  'nm  V.  13.  39.
Zam  oi.  V.  fl'oioft'  •beisst'.  —  Vgl.  iarilöjiiisav- und  ai.  ddmhika-;  ferner  zu  täi.dnslra:  — Pü.:  (ef  dandän.
•  j.  tizidustra-  Adj.  'mit  scharfem  Ge- biss, Gezähn' :  vara^ahe . .  'rahe  Yt.  14. 1 5.
ai.  TgL  tüfnadaiti/lra-  Adj.,  mm  V.  äaJa/i 'beissl';  s.  tiädifiura:  —  *difslra-  statt  'dqSlra- nobl  in  Anletuiang  an  einen  KS.  *äSdqi 'schaifiälmig'  aus  •flSin/-  {al  iüä-dan),^  »gl. danlan-  und  tilidälä;  daitika-.  —  Npü.:  rti dan^n.
•  j.  tizi.bara-  Adj.  'mit  scharfer  Schneide': vadsm  'r>m  HUsnüttm  "einen  Keil  mit scharfer  Schneide  . ."  V.  14. 7.
•Aar»-  m.,  wun  V.  briy-.  —  Pü.:  IH  ad  d.
•  j.  "tizinaVant-**  Adj.  'scharf,  durch- drmgend':  "vantftn  bavShi  y^a  mi^r?m Az.6.
VgL  "tiioam-.  —  »  Korreklur  Wo.s.  Korrekt wiie  etwft  toBtHav*;  »gL  w.  Ujasvant-  Adj.
•  j.  tizi.srvä-  Adj.  (mask.  •wo-)  'mit  spitzem Gehörn':  büzahe  . .  'vake  Yt  14-  »5-
=== leaf 378 head (col 651-652) ===
```


## [2026-09-05T17:54:36.777Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 12290\nn=0\nfor i,l in enumerate(lines):\n    if i>=12289: break\n    n+=l.count('\\f')\nprint('leaf of line 12290 =', n)\nleaves=t.split('\\f')\nimport re\nprint(re.findall(r'^\\s*(6[0-9][0-9])\\s*$', leaves[n], re.M))\nprint(leaves[n][:80].replace('\\n',' '))\nEOF",
 "description": "Find BRT column for tiži-dąstra"
}
```


### [2026-09-05T17:54:38.559Z] TOOL RESULT

```
leaf of line 12290 = 379
['654']
�ml.  ayan)  heisst  der  13.  Monats- tag: 'ryeie  stärJ  ra^fa/ff  s^armanuhai
```


## [2026-09-05T17:54:38.754Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD 145 ===\"\ngrep -n \"δt \\|δʼt\\|dt \" SOD_pages.txt | head -20\necho \"--- SOD entry 145 area / wild animal ---\"\ngrep -n \"wild animal\\|جانور وحشی\\|دد\" SOD_pages.txt | head -20",
 "description": "Grep Gharib Sogdian dictionary"
}
```


### [2026-09-05T17:54:38.829Z] TOOL RESULT

```
=== SOD 145 ===
2651:Waldschmidt and W. Lentz published more texts in                 area of Chinese Turkestan, in a ruined library of a
3181:voiced stops /*&, *dt *#/, which have become spirants
4641:                                                                        310 "wSnVndt M                       J^yh^Uyb
26301:7831 ptrk'ndt M                                             of            fortress, ditch
27112:      patzman     (ptzn^n) ©elat. -dt =^pw ptzm'n                      quarrel, dispute
29553:     sar5 (srd) ©A v. sar?da\ OP Oard-, Khwar. srS             8954 srdt   C =» sr8>t
32091:                                                               9845 w^ptzm'ndt M                            Jjt>«?<J*j>,
32109:9832 w'ndt         M =» w>nt                                         TSP 2.521, 3213, 266, 301, 6.148, 14.8, 1127;
34039:      GMS 1568; wyspn+>dt BSTBL, Padm. 51; Anc.
35467:      yaxe/i ©<*yah; Av. yaskdrdt ? ©pi. -f ^y'yy                  TSP 13.17; S W, IIJ 1976, 59
45191:                                                         xxxiii/L                   lb, dt j,
--- SOD entry 145 area / wild animal ---
14183:                                                                      wild animals
14233:       wild animal
39895:wild animal  3668                         with hardship   3083                       witness     10309
39896:wild animals  3672                        with head of 8972                          wives 9961, 10370
```


## [2026-09-05T17:54:43.244Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14170,14240p' SOD_pages.txt",
 "description": "Print SOD wild animal entries"
}
```


### [2026-09-05T17:54:43.302Z] TOOL RESULT

```
     Sastpar, 5astpar (8stJ3r)                        L6-\
                                                                     TSP 3.204 n pl98; Hen. Texts. 729
     order, authority
     MDii B4 R 23; Frag. Len. 77R 5                             3659 6sny w't B, S, M                           *-o*-4
                                                                     8asne-wat =*8sn
3646 Sstp'r Ms-    B, S   j^jjTjj o^;* ^f      c~-j<o ojoS           south wind
                                                                                                               dw^ng^
 145


                                                                3672 Styst   B, S                             ahy± Ol«
        TSP 3.204; Hen. Texts. 729; Ssny wyt pYy "Wind
          god", Sund. Liste 1944, 455-7                               Satist (65tystt, Stfyst) ©pi. ob. -ry =*5t-
                                                                      wild animals
 3660 5st-     B =» 5yst-, 6st>y
                                                                      BBB p61, 512; GMS 1186; Frag. Len. 120, 5; MSP
 3661 SstNvch       M, S                            Jljb<j»
                                                                        b32, 101 elO
        5(a)/i/ostauc ©<*dusta-wauc(=dustaw(an)+auc)
          =»5stwc, 6ystwc                                       3673 5w> B,M                            (u>=* >=■** >>)j*
        poverty                                                      5wa
                                                                     two (dw>) ©<*d(u)wa ^^             5yP-, SyPty-
        GMS 119, 1080; KG 336; W-Lii: Gropp. 38; BBB
          633                                                         EGSii 139; GMS 501, 1316, 1320; S W, C2, gloss.
                                                                        199; ace. dwy, C2, 6V 13
3662 8st)wcy B                                     jlyU*^
     6ostauce/i ?
                                                                3674 dw> =* 6w>
                                                                3675 dw*psynty C                         j^^-Ji- <t>r^>>
        poor 2a.7
        Frag.                                                        dwa-pasynt/de
                                                                      bisected, halvedidivided into two parts)
3663 6st>y B                   :              <^u
     5iste (5st-) ©*dista; fdais- ©pp. ^Systk                         C2,22V12, 66V 10 n p59, 11-12
     built
                                                                3676 8wa-puxay
                                                                     dw* pwx'y C                                    o^vj->
        VJ 14b; dsty, Sund. AI 28, 1988 pl8l
                                                                     bisected, halvcdidivided into two parts)
3664 Sstw'n B, M                                    jlyli*^
                                                                     Sund. AoFiii 1975 p65, 22 p67 n50
     5(a)stwan (dstw'n) ©*dus-tuwdn            ©pi. -(•, ob.
         pi. ~ty =>cstw>n, dystw*n                              3677 dw'ryt C                            \jj>> *^ia-*r ^
                                                                     6wa-ret
       poor
       W-Lii; Frag.2a.12.21; VJ 49, 51, 77, 122; TSP                 having two faces
         2.1178, 12.21; BSTBL, Intox. 10; Tales. 486.23;             Sund. AI 1988, 181
         BSTii 885.3, 894.18; C2, 51V 6, 54R 18, 51R3,          3678 Sw'sp'rm'k     C                     ^j;*^^
         105V 6
                                                                     5wa-sfarme ^sp^rntfk
3665 dstw^      C => Sstw>n                                          bisexuaK/iavzng two kinds of pudenda)
                                                                     SCE 356
3666 Sstwc S                                       is>Jj~>*j*
     6ostauc (dstwc) ^Sst'wch                                   3679 5w>ts M                                   .jjiji
     poverty                                                         5watas (dw>ts) ©<*duwa-dasa\ Av. duvadasa;
       Hen. Tales. 486.18; C2, 51V 9; BSTii 886.9                      Oss. duvadas\ Past, dvalas ©abl. dwUsnu
                                                                     twelve
3667 dstwc      C => Sstwc
                                                                     GMS 289, 1321-2; EGSii 146; STi 33.12, 78.14;
3668 St- B, M                        ^j jlJ^ <»
     Satu ©Av. daitaka ©nom. ace. nt. -w; pi. -yst                     BBB; dw>dys, SwHs, W-Lii 548, 7, 17
       =»6tyst
                                                                3680 dw'ts   C =* 5w>ts
       wild animal
                                                                3681 5w> w'pr B                                     ofx^
       VJ 313, 949, 968; TSP; BBB 512; GMS 1169,                     5wa-wafar =^wJpr
         1172; 6ttw* TSP 9.45                                        double, twice as much
3669 St'yst =* Styst                                                 BSTBL, Dhy. 128

3670 Sts rwc     S                                              3682 dwNvystmyq C                              ^ j c.^u
                         f>jc—     jjj j ^y\ jjj j ^     }3J         6wa-wist-mik
```


## [2026-09-05T17:54:51.874Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN diamond ===\"\ngrep -n -i \"diamond\" KLN_1966.txt | head -8\necho \"=== KLN adamant ===\"\ngrep -n -i \"adamant\" KLN_1966.txt | head -8\necho \"=== KLN tame/tough/tongs/zinc ===\"\ngrep -n \"^tame\\|tame, adj\\|tongs, n\\|tough, adj\\|zinc, n\" KLN_1966.txt | head -10",
 "description": "Grep Klein for diamond/adamant"
}
```


### [2026-09-05T17:54:51.971Z] TOOL RESULT

```
=== KLN diamond ===
1567:Adam,  n., name  of  the  first  man  (Bible);  in  a  figur¬ ative  sense  it  is  used  to  denote  'human  nature, frailty’.  —  Heb.  Addm,  lit.  ‘man’,  usually  with the  def.  art.,  ha-addm,  ‘the  man’,  prop,  ‘the  one formed  from  addmdh  (i.e.  the  ground)’.  See  Gen. 2:7,  ‘The  Lord  God  formed  man  of  dust  from the  ground’.  For  the  connection  between  Heb. addmdh,  ‘ground,  earth’,  and  addm,  ‘man’,  cp. L.  homo,  ‘man’,  humdnus,  ‘human’,  which  are rel.  to  humus,  ‘earth,  ground,  soil ,  and  Gk. emx&ovioi,  ‘earthly  ones,  men’,  fr.  •/S+ow, ‘earth’. Derivatives:  Adam-ic,  Adam-ic-al,  adjs.,  Adam- ic-al-ly,  adv.,  Adam-ite,  n.,  Adam-it-ism,  n., Adam-it-ic,  Adam-it-ic-al,  adjs. adamant,  n.,  a  very  hard  stone;  adj.,  very  hard, unyielding.  —  ME.,  ‘diamond,  magnet’,  fr.  OF. adamant,  oblique  case,  fr.  L.  adamantem,  acc.  of adamds  (whence  the  OF.  nom.  adamas),  fr.  Gk. aSapa;,  ‘adamant,  the  hardest  metal,  diamond’, lit.  ‘unconquerable’,  fr.  d-  (see  priv.  pref.  a-)  and the  verb  8apav,  ‘to  tame’.  See  tame  and  cp.  dia¬ mond;  cp.  also  the  second  element  in  Hippodamia. The  sense  of  ‘load  stone,  magnet’,  arose  from  a confusion  with  L.  adamare,  ‘to  love  passionately’ .
6510:Derivative:  carbonado,  tr.  v. carbonado,  n.,  an  opaque  kind  of  diamond.  — Sp.,  lit.  ‘carbonated’,  pp.  of  carbonar,  ‘to  car¬ bonate’,  fr.  carbon,  ‘coal’,  fr.  L.  carbonem,  ace. of  carbo.  See  carbon  and  -ado. carborundum,  n.,  silicon  carbide  (SiC),  an  abra¬ sive.  —  Coined  fr.  carbon  and  corundum, carboxyl,  n.,  a  univalent  radical,  containing  car¬ bon,  oxygen  and  hydrogen  (COOH)  (chem.)  — Compounded  of  carbon,  oxygen  and  -yl. Derivatives:  carboxyl-ale,  n.  and  tr,  v.,  car- boxyl-ation,  n.
11251:diamantiferous,  adj.,  yielding  diamonds.  —  F. diamantifdre.  See  diamond  and  -ferous  and  cp. diamondiferous.
11255:—  Formed  fr.  di-,  ‘double’,  and  amine, diamond,  n.  —  ME.  diamant,  diamaunt,  fr.  OF.
11256:diamant ,  fr.  Late  L.  diamantem ,  acc.  of  diamds, which  is  a  blend  of  Gk.  xSxpxp,  ‘adamant,  dia¬ mond’,  lit.  ‘unconquerable’  and  Siacpavr;?,  ‘trans¬ parent’.  See  adament  and  diaphanous. Derivatives:  diamond,  adj.  and  tr.  v.,  diamond¬ ed,  adj.,  diamondize  (q.v.) diamondiferous,  adj.,  yielding  diamonds.  —  A hybrid  coined  fr.  diamond  and  L.  ferre,  ‘to  bear, carry’.  See  diamond  and  -ferous  and  cp.  dia¬ mantiferous.
11257:diamondize,  tr.  v.,  to  ornament  with  diamonds.
11258:—  A  hybrid  coined  fr.  diamond  and  -ize,  a  suff. of  Greek  origin.
20824:Koh-i-noor,  n.,  a  famous  diamond,  one  of  the British  crown  jewels.  —  Pers.  koh-i-nur,  lit. ‘mountain  of  light’,  prop,  a  hybrid  coined  fr. Pers.  koh,  ‘mountain’,  which  is  rel.  to  Pers. kohe,  ‘hump’,  OPers.  kaufa-,  ‘mountain’,  Aves- tic  kaofa-,  ‘mountain,  hump’,  and  fr.  Arab. nur,  ‘light’  (see  Menorah). kohl,  n.,  powder  (esp.  of  antimony),  used  by  East¬ ern  women  to  darken  the  eyelids.  —  Arab. kuhl.  See  alcohol.
=== KLN adamant ===
1527:adamant
1567:Adam,  n., name  of  the  first  man  (Bible);  in  a  figur¬ ative  sense  it  is  used  to  denote  'human  nature, frailty’.  —  Heb.  Addm,  lit.  ‘man’,  usually  with the  def.  art.,  ha-addm,  ‘the  man’,  prop,  ‘the  one formed  from  addmdh  (i.e.  the  ground)’.  See  Gen. 2:7,  ‘The  Lord  God  formed  man  of  dust  from the  ground’.  For  the  connection  between  Heb. addmdh,  ‘ground,  earth’,  and  addm,  ‘man’,  cp. L.  homo,  ‘man’,  humdnus,  ‘human’,  which  are rel.  to  humus,  ‘earth,  ground,  soil ,  and  Gk. emx&ovioi,  ‘earthly  ones,  men’,  fr.  •/S+ow, ‘earth’. Derivatives:  Adam-ic,  Adam-ic-al,  adjs.,  Adam- ic-al-ly,  adv.,  Adam-ite,  n.,  Adam-it-ism,  n., Adam-it-ic,  Adam-it-ic-al,  adjs. adamant,  n.,  a  very  hard  stone;  adj.,  very  hard, unyielding.  —  ME.,  ‘diamond,  magnet’,  fr.  OF. adamant,  oblique  case,  fr.  L.  adamantem,  acc.  of adamds  (whence  the  OF.  nom.  adamas),  fr.  Gk. aSapa;,  ‘adamant,  the  hardest  metal,  diamond’, lit.  ‘unconquerable’,  fr.  d-  (see  priv.  pref.  a-)  and the  verb  8apav,  ‘to  tame’.  See  tame  and  cp.  dia¬ mond;  cp.  also  the  second  element  in  Hippodamia. The  sense  of  ‘load  stone,  magnet’,  arose  from  a confusion  with  L.  adamare,  ‘to  love  passionately’ .
1568:adamantean
1570:adamantean,  adj.,  hard  as  adamant.  —  Formed with  suff.  -an  fr.  L.  adamanteus ,  fr.  adamds.  See prec.  word.
1571:adamantine,  adj.,  1)  made  of  adamant;  2)  like adamant ;  very  hard.  —  L.  adamantinus,  fr.  Gk; aSaiiavnvot;,  fr.  ASApag.  See  adamant  and  adj. suff.  -ine.
11256:diamant ,  fr.  Late  L.  diamantem ,  acc.  of  diamds, which  is  a  blend  of  Gk.  xSxpxp,  ‘adamant,  dia¬ mond’,  lit.  ‘unconquerable’  and  Siacpavr;?,  ‘trans¬ parent’.  See  adament  and  diaphanous. Derivatives:  diamond,  adj.  and  tr.  v.,  diamond¬ ed,  adj.,  diamondize  (q.v.) diamondiferous,  adj.,  yielding  diamonds.  —  A hybrid  coined  fr.  diamond  and  L.  ferre,  ‘to  bear, carry’.  See  diamond  and  -ferous  and  cp.  dia¬ mantiferous.
12030:ML.  domanium.  See  prec.  word  and  adj.  suff.  -al. dome,  n.,  a  building,  palace.  —  F.  dome,  fr.  It. duomo,  ‘a  cathedral  church’,  fr.  L.  domus, ‘house’  (in  domus  Dei,  ‘house  of  God’),  whence dominus,  ‘master,  lord’,  lit,  ‘master  of  the  house’, domare,  ‘to  tame’,  lit.  ‘to  accustom  to  the  house’. L.  domus  is  cogn.  with  Gk.  86po?,  OI.  damah, ‘house’,  Gk.  Stop ,<x  (prob.  for  *ddm-rgi),  ‘house, chief  room,  housetop’,  OSlav.  domu,  ‘house’, doma,  ‘at  home’,  domov,  ‘home’,  Arm.  tun  prob. for  *db(m)-m,  ‘house’,  the  first  element  in  Gk. 8Eo-7t6TY)?  (for  *dems-pota),  ‘despot’,  lit.  ‘lord of  the  house’,  Sa-ncSov  (for  *dm-pedom), ‘ground  about  a  house’,  and  in  Lith.  dim-stis (for  *drp-sto-),  ‘estate,  yard’,  and  the  second element  in  Gk.  £v-Sov  (fr.  ev,  ‘in’,  and  *dom), ‘within’,  lit.  ‘in  the  house’;  fr.  I.-E.  *dfm-, *ddm-,  *dtp-,  *dm-,  ‘house’.  These  words  pos¬ sibly  meant  orig.  ‘building’,  and  are  cogn.  with Gk.  8£peiv,  ‘to  build'.  Cp.  tame,  timber.  Cp. also  adamant,  belladofina,  dam,  ‘a  female  par¬ ent’,  dama,  dame,  daiqoiseau,  damsel,  dan,  title, danger,  daunt,  demesne,  demijohn,  despot,  dia¬ mond,  doe,  dom,  domain,  domestic,  Domicella, domicile,  dominate,  domineer,  Dominic,  domin¬ ion,  domino,  dominus,  don,  ‘title’,  donjon,  duenna, dungeon,  endo-,  duomo,  Hippodamia,  indomi¬ table,  madam,  madame,  major-domo,  vidame. Cp.  also  toft.
12963:emery,  n.,  a  hard  variety  of  corundum.  —  OF. emeril  (F.  emeri),  fr.  It.  smeriglio,  fr.  MGk. airrjpi,  fr.  Gk.  apuipic,  ‘emery  powder’,  which  is prob.  borrowed  fr.  Heb.  shamtr,  ‘adamant; emery’;  see  Jer.  17:1,  Ezek-3:9,  Zech.  7: 12.  See
=== KLN tame/tough/tongs/zinc ===
```


## [2026-09-05T17:55:00.848Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"tame,  adj\\|tame, adj\\|to  tame\\b\" KLN_1966.txt | head -10\necho \"---\"\ngrep -n \"^tame$\\|^tough$\\|^tongs$\\|^zinc$\" KLN_1966.txt | head",
 "description": "Grep Klein tame entry"
}
```


### [2026-09-05T17:55:02.599Z] TOOL RESULT

```
1567:Adam,  n., name  of  the  first  man  (Bible);  in  a  figur¬ ative  sense  it  is  used  to  denote  'human  nature, frailty’.  —  Heb.  Addm,  lit.  ‘man’,  usually  with the  def.  art.,  ha-addm,  ‘the  man’,  prop,  ‘the  one formed  from  addmdh  (i.e.  the  ground)’.  See  Gen. 2:7,  ‘The  Lord  God  formed  man  of  dust  from the  ground’.  For  the  connection  between  Heb. addmdh,  ‘ground,  earth’,  and  addm,  ‘man’,  cp. L.  homo,  ‘man’,  humdnus,  ‘human’,  which  are rel.  to  humus,  ‘earth,  ground,  soil ,  and  Gk. emx&ovioi,  ‘earthly  ones,  men’,  fr.  •/S+ow, ‘earth’. Derivatives:  Adam-ic,  Adam-ic-al,  adjs.,  Adam- ic-al-ly,  adv.,  Adam-ite,  n.,  Adam-it-ism,  n., Adam-it-ic,  Adam-it-ic-al,  adjs. adamant,  n.,  a  very  hard  stone;  adj.,  very  hard, unyielding.  —  ME.,  ‘diamond,  magnet’,  fr.  OF. adamant,  oblique  case,  fr.  L.  adamantem,  acc.  of adamds  (whence  the  OF.  nom.  adamas),  fr.  Gk. aSapa;,  ‘adamant,  the  hardest  metal,  diamond’, lit.  ‘unconquerable’,  fr.  d-  (see  priv.  pref.  a-)  and the  verb  8apav,  ‘to  tame’.  See  tame  and  cp.  dia¬ mond;  cp.  also  the  second  element  in  Hippodamia. The  sense  of  ‘load  stone,  magnet’,  arose  from  a confusion  with  L.  adamare,  ‘to  love  passionately’ .
3613:Derivatives:  ashlar-ed,  adj.,  ashlar-ing ,  n. ashore,  adv.  —  Formed  fr.  a-  ‘on’,  and  shore, ashrafi,  n.,  name  of  various  gold  coins,  esp.  a gold  coin  in  Persia.  —  Pers.,  fr.  Arab. dshraf,  lit.  ‘noble  ones’,  pi-  of  shar.f,  ‘noble’, fr.  sharafa,  ‘he  was  exalted,  he  was  noble  . See  shereef  and  cp.  words  there  referred  to. ashrama,  n„  hermitage  (Hinduism).  —  Ol.  dsrd- mah,  fr.  adnominal  pref.  d-  and  srdmah,  ‘effort, toil,  fatigue’,  whence  srdmyati,  ‘he  becomes tired’,  which  is  rel.  to  OI.  kldmyati,  kldmati,  ‘he slackens,  languishes’  and  cogn.  with  OSlav. kromiti,  ‘to  tame’,  chromii,  ‘lame’.
10276:dame,  n.,  a  noble  lady.  —  ME.  dame,  tr.  OF. (=  F.)  dame,  fr.  L.  domina,  ‘the  mistress  of  a household’,  fern,  of  dominus,  ‘lord’,  prop,  ‘own¬ er  of  the  house’,  and  rel.  to  domus,  ‘house’.  For the  form  cp.  tribunus,  fr.  tribus,  ‘tribe’.  Dominus is  only  indirectly  rel.  to  domare,  ‘to  tame’  (see dome  and  cp.  dominate);  but  was  directly  in¬ fluenced  in  meaning  by  it.  See  Walde-Pokorny,
10384:daunt,  tr.  v.  —  ME.  daunten,  fr.  OF.  danter,  don- ter  (F.  dompter),  fr.  L.  domitdre ,  ‘to  tame,  sub¬ due’,  freq.  of  domare  (pp.  domitus),  ‘to  tame, subdue,  vanquish,  conquer’,  lit.  ‘to  accustom to  the  house’,  fr.  domus,  ‘house’.  See  dome, ‘building’,  and  cp.  indomitable.  Cp.  also  tame. Derivatives:  daunt-er,  n.,  daunt-ing,  adj.,  daunt- ing-ly,  adv.,  daunt-ing-ness,  n.,  dauntless  (q.v.). dauntless,  adj.  —  Formed  fr.  the  ME.  noun  daunt, fr.  daunten  (see  daunt)  with  suff.  -less;  first  used by  Shakespeare.
11976:doe,  n.,  female  of  the  fallow  deer.  —  ME.  do,  fr.  OE. da  (whence  Dan.  daa),  prob.  a  Celtic  loan  word; cp.  Co.  da,  ‘fallow  deer’,  OIr.  dam,  ‘ox’,  dam allaid,  ‘stag’  (prop,  ‘wild  ox’),  W.  dafad,  ‘sheep', which  are  prob.  cogn.  with  Gk.  SapiaXir;;,  ‘young steer',  SapaXn),  SapaXcq,  ‘young  cow,  heifer’  (L. damma,  dama,  ‘fallow  deer,  buck,  doe',  is  prob. borrowed  fr.  Celtic);  cp.  Dama.  These  animal names  are  prob.  connected  with  I.-E.  base * doma -,  ‘to  tame’  and  orig.  denoted  ‘tamed animals’ ;  see  tame.
12030:ML.  domanium.  See  prec.  word  and  adj.  suff.  -al. dome,  n.,  a  building,  palace.  —  F.  dome,  fr.  It. duomo,  ‘a  cathedral  church’,  fr.  L.  domus, ‘house’  (in  domus  Dei,  ‘house  of  God’),  whence dominus,  ‘master,  lord’,  lit,  ‘master  of  the  house’, domare,  ‘to  tame’,  lit.  ‘to  accustom  to  the  house’. L.  domus  is  cogn.  with  Gk.  86po?,  OI.  damah, ‘house’,  Gk.  Stop ,<x  (prob.  for  *ddm-rgi),  ‘house, chief  room,  housetop’,  OSlav.  domu,  ‘house’, doma,  ‘at  home’,  domov,  ‘home’,  Arm.  tun  prob. for  *db(m)-m,  ‘house’,  the  first  element  in  Gk. 8Eo-7t6TY)?  (for  *dems-pota),  ‘despot’,  lit.  ‘lord of  the  house’,  Sa-ncSov  (for  *dm-pedom), ‘ground  about  a  house’,  and  in  Lith.  dim-stis (for  *drp-sto-),  ‘estate,  yard’,  and  the  second element  in  Gk.  £v-Sov  (fr.  ev,  ‘in’,  and  *dom), ‘within’,  lit.  ‘in  the  house’;  fr.  I.-E.  *dfm-, *ddm-,  *dtp-,  *dm-,  ‘house’.  These  words  pos¬ sibly  meant  orig.  ‘building’,  and  are  cogn.  with Gk.  8£peiv,  ‘to  build'.  Cp.  tame,  timber.  Cp. also  adamant,  belladofina,  dam,  ‘a  female  par¬ ent’,  dama,  dame,  daiqoiseau,  damsel,  dan,  title, danger,  daunt,  demesne,  demijohn,  despot,  dia¬ mond,  doe,  dom,  domain,  domestic,  Domicella, domicile,  dominate,  domineer,  Dominic,  domin¬ ion,  domino,  dominus,  don,  ‘title’,  donjon,  duenna, dungeon,  endo-,  duomo,  Hippodamia,  indomi¬ table,  madam,  madame,  major-domo,  vidame. Cp.  also  toft.
12038:domesticable,  adj.  —  ML.  domesticabilis,  fr. domesticdre.  See  next  word  and  -able, domesticate,  tr.  v.,  to  tame.  —  ML.  domesticatus , pp.  of  domesticdre,  ‘to  tame’,  lit.  ‘to  make  dom¬ estic’,  fr.  L.  domesticus.  See  domestic  and  verbal suff.  -ate.
17032:Haggai,  n.,  1)  a  prophet  who  lived  about  500 B.C.E.,  the  tenth  in  the  order  of  the  Twelve Prophets;  2)  the  Book  of  Haggai  (Bible).  — Heb.  Haggay  (whence  Gk.  ’Ayyaio L.  Aggae- us),  lit.  ‘festal,  born  on  a  feast  day’,  fr.  Heb. hagh,  ‘a  festival  gathering,  a  feast’,  from  the  stem of  hdghagh,  ‘he  made  a  pilgrimage,  celebrated  a feast’,  which  is  rel.  to  Syr.  haggi,  ‘he  made  a pilgrimage,  celebrated  a  feast’,  Aram.-Syr. haggd,  ‘a  feast’,  Arab,  hajja,  ‘he  went  on  a  pil¬ grimage’.  Cp.  hadj,  hadji. haggard,  n.,  an  untamed  hawk;  adj.,  hard  to  tame (said  of  a  hawk).  —  MF.  (=  F.)  hagard,  ‘a  hag¬ gard’,  which  is  of  Teut.  origin  and  orig.  meant ‘(a  bird)  of  the  hedge’,  i.e.  ‘a  wild,  untameable (bird)’.  Cp.  ME.  hagger,  ‘wild;  an  untamed hawk,  haggard’,  and  see  hedge  and  -ard.  Cp. also  hag,  ‘witch’.
17840:hippocras,  n.,  a  highly  spiced  wine.  —  ME.  ypo- cras,  fr.  OF.  ipocras,  ypocras  (F.  hypocras ), prop.  fr.  Hippocrates,  the  celebrated  Greek physician ;  so  called  because  the  wine  was  strain¬ ed  through  a  woolen  bag  named  Hippocrates sleeve.  The  French  spelling  hypocras  is  due  to a  confusion  with  the  numerous  words  beginning with  hypo-,  fr.  Gk.  6776,  ‘under,  below*. Hippocratic,  adj.,  of,  or  pertaining  to,  the  Greek physician  Hippocrates  (460?  —  357  B.C.E.)  — Late  L.  Hippocraticus,  fr.  L.  Hippocrates,  fr. Gk.  'Innoxparriz.  For  the  ending  see  suff.  -ic. Hippocrene,  n.,  a  fountain  on  Mt.  Helicon  sacred to  the  Muses.  —  L.,  fr.  Gk.  'hmox.prtYrl,  lit. ‘horse’s  fountain’,  which  is  compounded  of (777704,  ‘horse’,  and  xprjvr),  ‘fountain’.  See  hippo- and  crenic.  Derivative:  Hippocren-ian,  adj. Hippodamia,  n.,  daughter  of  Oenomaus,  king  of Pisa,  who  offered  her  to  the  suitor  who  should defeat  him  in  a  chariot  race  ( Classical  mythol.) —  L.,  fr.  Gk.  T7r7roSi(iEia,  fr.  17777680:1x05,  ‘tamer of  horses’,  which  is  formed  fr.  (777705,  ‘horse’, and  the  stem  of  Sapav,  ‘to  tame’.  See  hippo-  and tame  and  cp.  adamant.
19208:Derivatives:  indolent,  n.,  indolent-ly,  adv. indomitable,  adj.  —  Late  L.  indomitabilis,  ‘indo¬ mitable’,  fr.  in-,  ‘not’,  domitare,  ‘to  tame’,  and suff.  -abilis.  See  daunt,  and  -able.
---
```


## [2026-09-05T17:55:11.516Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -l KLN_1966.txt KLN_1971.txt\necho \"=== 1971 tame ===\"\ngrep -n \"tame,  adj\\|tame, adj\" KLN_1971.txt | head -5\necho \"=== 1966 sample lines near end ===\"\ngrep -c \"\" KLN_1966.txt\ngrep -n \"tongs\" KLN_1966.txt KLN_1971.txt | head -5",
 "description": "Check Klein files for tame/tongs"
}
```


### [2026-09-05T17:55:11.612Z] TOOL RESULT

```
   41262 KLN_1966.txt
  271509 KLN_1971.txt
  312771 total
=== 1971 tame ===
240763:tame, adj. — ME. tame, fr. OE. tam, rel. to ON. 
240807:men, Goth, gatamjan. See tame, adj. 
=== 1966 sample lines near end ===
41263
KLN_1971.txt:40224:tang, tunge , ‘tongs’ (lit. ‘that which bites’). See 
KLN_1971.txt:63421:‘bites’, ON. tong , OE. tang, tange, ‘tongs’. See 
KLN_1971.txt:63422:tongs and cp. the second element in carpodacus, 
KLN_1971.txt:95707:L., ‘pair of tongs, pincers’, contracted fr. 
KLN_1971.txt:95720:‘a pair of tongs’. See forceps,
```


## [2026-09-05T17:55:14.443Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '240763,240790p' KLN_1971.txt\necho \"=== tongs entry ===\"\ngrep -n \"^tongs, n\" KLN_1971.txt | head -3",
 "description": "Klein tame entry"
}
```


### [2026-09-05T17:55:14.540Z] TOOL RESULT

```
tame, adj. — ME. tame, fr. OE. tam, rel. to ON. 
tamr, OS., Dan., Swed., OFris., MLG,, MDu., 
Du. tam , OHG., MHG. zam, G. zahm , ‘tame’. 
These adjectives prob. derive from an Old Teut. 
verb attested only in OHG. zamon, MHG. 
zamen, ‘to tame’, fr. I.-E. base *doma-, *dema -, 
*dem whence also OI. damayati , damaydti , 
‘tames’, damya -, ‘a young steer’, prop, ‘an ani- 
mal that must yet be tamed’, damitd, ‘tamer’, 
damtah , ‘tamed’, ModPers. dam , ‘a tame ani- 
mal’, Gk. Sa^av, ‘to tame, subdue’, 8^73x6^, 
‘tame’, ‘a slave taken in war’ (lit. ‘sub- 

dued’), a-8^.7)?, ‘unsubdued.; unwedded’, 8ap.<£- 




TAME 



744 



Xt}?, ‘a young steer’, L. domdre , ‘to tame, sub- 
due’, Ossetic domun , ‘tamer’, OIr. damnaim , 
=== tongs entry ===
249567:tongs, n. pi. — ME. tange, tonge , fr. OE. tang,
```


## [2026-09-05T17:55:20.559Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '249567,249580p' KLN_1971.txt\necho \"=== tough ===\"; grep -n \"^tough, adj\" KLN_1971.txt | head -2\necho \"=== zinc ===\"; grep -n \"^zinc, n\" KLN_1971.txt | head -2",
 "description": "Klein tongs/tough/zinc"
}
```


### [2026-09-05T17:55:20.656Z] TOOL RESULT

```
tongs, n. pi. — ME. tange, tonge , fr. OE. tang, 
tange, rel. to OS. tanga, ON. tong, Dan. tang, 
Swed. tang , OFris. tange, MDu. tanghe, Du. 
tang, OHG. zanga, MHG., G. zange, lit. ‘that 
which bites’ (cp. OHG. zangar , ‘biting, sharp’), 
fr. I.-E. base *denk-, ‘to bite’, whence also OI. 
ddsati , ‘biter’ (for *dnketi), ‘bites’, Gk. Saxvetv, 
‘to bite’, 8a!;, ‘biting’, ‘a biting’. Alb. 

done, ‘tongs’. For sense development cp. F. 
mordache, ‘tongs’, fr. mordre, ‘to bite’. Cp. 
Dacus and the second element in Demodex, 
Mixodectes, Tridacna 

=== tough ===
250546:tough, adj. — ME. togh, tough, fr. OE. tok, for 
=== zinc ===
270647:zinc, n. — G. Zink , prop, the same as Zinke ,
```


## [2026-09-05T17:55:21.595Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON almas ===\"\ngrep -n \"الماس\" MON_part1.txt | head -10",
 "description": "Grep Mo'in for almās"
}
```


### [2026-09-05T17:55:21.656Z] TOOL RESULT

```
=== MON almas ===
1768:شرات. الماس. تیغ. تما آیگنه سیمار: 
3620:می‌شد. مصل ,مبا رک آغا» و «آغا الماس» و 
5337:مانند الماس و زمرد و غیره -بر حلقة 
16385:الماس: :0:5 (.) (زه.) یکی از 
16390:درجهٌ سختی‌اش ۱۰ می‌باشد. الماس را با 
22691:برلیان: 0 (.) (زم.) الماس تراش 
22693:تلاو به بیشتر و عرضهة به بازار. در تراش الماس 
22699:شکل‌های مسختلفی که بلور الماس در 
27543:مزین به یراق‌های طلا و دانه‌های الماس 
36375:است؛ جوزمائل» شیطان الماسی.
```


## [2026-09-05T17:55:23.822Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16378,16400p' MON_part1.txt",
 "description": "Mo'in almās entry"
}
```


### [2026-09-05T17:55:23.881Z] TOOL RESULT

```
اللهی: 212-1 (ع. ف.] (ص‌نسب.) منسوب 
به الله» خدایی. مرد کامل» رشید» از نقص 
رسته. 

الم: صهاه [ع.] (.) (مص‌ل.) دردمند شدن. 
(امص.) دردمندی. (.) درد؛ ج. آلام. 
الماس: :0:5 (.) (زه.) یکی از 
سنگ‌های کانی قیمتی که به علت سختی و 
درخشندگی و کمیابی مسقدم بر دیگر 
سنگك‌های کانی است و آن گر خالص 
است. وزن مسخصوصش ۲/۵ تا ۳/۲ و 
درجهٌ سختی‌اش ۱۰ می‌باشد. الماس را با 


المام فرهنگ فار سي معیر ۱۸۹ 


واحد وزن قبراط وزن کنند. 

المام: سقسا [ع.] (مصل.) فرود آمدن؛ 
فرو آمدن.
```


## [2026-09-05T17:55:31.841Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T17:55:31.848Z] TOOL RESULT

```


```


## [2026-09-05T17:55:35.759Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dem%CE%B7%E2%82%82-",
 "prompt": "Give the full etymology entry for PIE *demh₂- 'to tame, domesticate': the reconstruction, meaning, and the list of descendants (especially Indo-Iranian, Greek daman/adamas, Latin domare, Germanic *tamaz). Quote key lines."
}
```


### [2026-09-05T17:55:38.057Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T17:55:38.125Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%85%D8%A7%D8%B3",
 "prompt": "Give the full etymology sections for الماس in Persian and Arabic: origin, route of borrowing (Greek adamas? Syriac? Arabic al-mās?), and any Middle Persian form. Quote exact wording."
}
```


### [2026-09-05T17:55:43.640Z] TOOL RESULT

```
# Etymology of الماس (almās)

## Persian

The page provides this etymology section:

**Exact quote:** "From Middle Persian _ʾlmʾs_ (almās); see there for further information."

The article does not specify the ultimate origin (whether Greek, Syriac, or Arabic), stating only that it derives from Middle Persian with a reference to "see there for further information"—implying the detailed origin exists on the Middle Persian entry, not this page.

## Arabic

The Wiktionary entry shows Arabic as a **descendant** of Persian (listed under "Descendants"), not as an origin:

**Exact quote:** "→ Arabic: أَلْمَاس (ʔalmās)"

The article indicates Persian influenced Arabic, rather than the reverse. No separate Arabic etymology section appears on this page. The borrowing direction flows from Persian outward to multiple languages including Arabic, Russian, Turkish, and others.

The article does not discuss whether the ultimate root traces to Greek "adamas" or other ancient sources.
```


## [2026-09-05T17:55:47.721Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dem%E1%B8%A5%E2%82%82-",
 "prompt": "Full entry for PIE *demh₂- 'to tame': root, meaning, derived terms and descendants (Indo-Iranian, Greek, Latin, Germanic)."
}
```


## [2026-09-05T17:55:48.875Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Middle_Persian/almas",
 "prompt": "Etymology of Middle Persian almās 'diamond, steel': origin (Greek adamas? Aramaic/Syriac?), and descendants."
}
```


### [2026-09-05T17:55:49.593Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T17:55:50.990Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T17:55:53.876Z] TOOL CALL #48: WebSearch

```json
{
 "query": "wiktionary Middle Persian ʾlmʾs almās diamond etymology Greek adamas",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


## [2026-09-05T17:55:54.389Z] TOOL CALL #49: WebSearch

```json
{
 "query": "wiktionary Reconstruction Proto-Indo-European demh₂- to tame",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


### [2026-09-05T17:56:00.325Z] TOOL RESULT

```
Web search results for query: "wiktionary Middle Persian ʾlmʾs almās diamond etymology Greek adamas"

Links: [{"title":"ʾlmʾs - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CA%BElm%CA%BEs"},{"title":"алмаз - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D0%B0%D0%BB%D0%BC%D0%B0%D0%B7"},{"title":"الماس - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%85%D8%A7%D8%B3"},{"title":"Алмас - Wiktionary","url":"https://en.wiktionary.org/wiki/%D0%90%D0%BB%D0%BC%D0%B0%D1%81"},{"title":"алмас - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D0%B0%D0%BB%D0%BC%D0%B0%D1%81"},{"title":"አልማዝ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%8A%A0%E1%88%8D%E1%88%9B%E1%8B%9D"},{"title":"adamas - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/adamas"},{"title":"diamond - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/diamond"},{"title":"alamas - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/alamas"},{"title":"ἀδάμας - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%BC%80%CE%B4%CE%AC%CE%BC%CE%B1%CF%82"}]

Based on the search results, here's what Wiktionary shows about the etymology of Middle Persian ʾlmʾs (almās) and its connection to diamond and Greek adamas:

The Middle Persian word ʾlmʾs is usually derived from Byzantine Greek ἀδάμας (adámas), but the Greek word itself is now considered an oriental loanword. The Akkadian word 𒋤𒉘 (elmēšu, "a valuable stone, perhaps amber") provides a comparative reference.

This etymological path shows how the word traveled across languages: the term ultimately originates from ancient Near Eastern languages, was borrowed into Greek as adamas, and then passed into Middle Persian as ʾlmʾs (almās), from which it spread to many other languages including Persian, Russian, Armenian, and others referring to diamond.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-05T17:56:02.434Z] TOOL RESULT

```
Web search results for query: "wiktionary Reconstruction Proto-Indo-European demh₂- to tame"

Links: [{"title":"Reconstruction:Proto-Indo-European/demh₂- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/demh%E2%82%82-"},{"title":"Reconstruction:Proto-Celtic/damnāti - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Celtic/damn%C4%81ti"},{"title":"Reconstruction:Proto-Indo-European/dem- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dem-"},{"title":"Reconstruction:Proto-Celtic/damos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Celtic/damos"},{"title":"tame - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/w/index.php?title=tame"},{"title":"Reconstruction:Proto-Germanic/tamaz - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/tamaz"},{"title":"Reconstruction:Proto-Germanic/tamjaną - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/tamjan%C4%85"},{"title":"dem - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/dem"},{"title":"दम - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%A6%E0%A4%AE"},{"title":"Reconstruction:Proto-Indo-European/dṓm - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%E1%B9%93m"}]

The search results show information about the Proto-Indo-European root *demh₂- from Wiktionary. Here's what I found:

The Proto-Indo-European root *demh₂- means "to tame, domesticate". 

It has descendants in Proto-Indo-Aryan, such as Sanskrit दमायति (damāyáti, "to subdue, tame"). The root also produced related words in various other language families:

- Proto-Celtic words derived from *demh₂- meaning "to subdue, tame"
- Proto-Celtic *damos meaning "ox," derived from *demh₂- ("to domesticate, tame")
- English "tame" comes from Proto-Germanic *tamaz ("brought into the home, tame"), which is derived from *demh₂-
- A Proto-Indo-European causative *domh₂-éye-ti derived from *demh₂- is attested in Latin domō and Sanskrit damayati


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T17:56:08.782Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CA%BElm%CA%BEs",
 "prompt": "Full Middle Persian entry ʾlmʾs: etymology (quote exactly), meanings, descendants list."
}
```


## [2026-09-05T17:56:10.880Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%80%CE%B4%CE%AC%CE%BC%CE%B1%CF%82",
 "prompt": "Full Ancient Greek entry ἀδάμας: etymology (quote exactly, including Beekes' view on whether it is from ἀ- + δαμάζω or a foreign/Pre-Greek loan), meanings, descendants."
}
```


### [2026-09-05T17:56:14.793Z] TOOL RESULT

```
# Middle Persian Entry: ʾlmʾs

**Etymology:**
"Usually derived from Byzantine Greek ἀδάμας (adámas), but the Greek word itself is now considered an oriental loanword." The entry notes comparison to Akkadian elmēšu, meaning "a valuable stone, perhaps amber," with related forms appearing across Iranian languages including Manichaean Middle Persian, Kurdish, and Zazaki variants.

**Meanings:**
1. Steel
2. Diamond

**Descendants:**
The word proliferated widely through Classical Persian (almās), generating descendants across multiple language families:

- **Turkic languages:** Turkish (elmas), Azerbaijani (almaz), Kazakh, Kyrgyz, Bashkir, Tatar, Uzbek, Southern Altai
- **Caucasian languages:** Georgian (almasi), West Circassian, Ossetian, Bats
- **Slavic languages:** Russian (almáz), Bulgarian (elmaz)
- **Semitic languages:** Arabic (ʔalmās), Classical Syriac (ʾlmsʾ)
- **Other languages:** Romanian (almas), Swahili (almasi), Hindustani (almās)
```


### [2026-09-05T17:56:18.008Z] TOOL RESULT

```
# Ancient Greek ἀδάμας - Complete Entry

## Etymology

The word has two proposed origins:

**Traditional view:** Derived from "ἀ- (a-, 'not') + δαμνάω (damnáō, 'conquer')" suggesting "indomitable."

**Beekes' assessment:** He "remarks that semantically this is strange and the word is rather a Semitic borrowing that was adapted by folk etymology." Potential Semitic sources include Akkadian *adamu* or *elmēšu* (a valuable stone), and Middle Persian *almās*.

## Meanings (Noun)

1. Adamant—the hardest metal (probably steel)
2. A hard metal resembling gold
3. Diamond

## Meanings (Adjective)

1. (Figuratively) Fixed, unalterable
2. Not to be broken, inflexible

## Key Descendants

- **Latin:** adamās
  - **English:** adamant
  - **Romance languages:** Italian adamante, Spanish adamante, Portuguese adamante
  - **Via Vulgar Latin:** French diamant/aimant, Spanish imán, Portuguese ímã
- **Armenian:** ադամանդ (adamand)
- **Georgian:** ანდამატი (andamaṭi)
```


## [2026-09-05T17:56:22.988Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%85",
 "prompt": "Give the Persian entries for دام: all senses and their separate etymologies (livestock/tame animal; net/trap; creature). Quote the etymology lines exactly, including Middle Persian and Avestan/Proto-Iranian antecedents."
}
```


## [2026-09-05T17:56:24.608Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%AF",
 "prompt": "Give the Persian entry for دد (dad) 'wild animal': etymology exactly as written (Middle Persian dad, Avestan daitika-, Proto-Iranian), and any note on the root."
}
```


### [2026-09-05T17:56:30.047Z] TOOL RESULT

```
# Persian Entries for دام (dâm)

## Etymology 1: Snare/Trap
**Etymology line:** "From Proto-Indo-Iranian *dáHma (compare Sanskrit दामन् (dā́man, "string, cord, rope, fetter")), from Proto-Indo-European *déh₁-mn̥"

**Sense:** "snare, trap"

## Etymology 2: Livestock/Tame Animal
**Etymology line:** "From Middle Persian [script needed] (dʾm /⁠dām⁠/, "tame animal"), ultimately from Proto-Indo-European *demh₂- ("to tame, dominate")"

**Senses:** 
- "livestock"
- "any domesticated animals and livestock such as sheep, cows, goats, dogs, cats, etc"

## Etymology 3: Draughts/Checkers
**Etymology line:** "Borrowed from French dames"

**Sense:** "draughts, checkers"

---

**Note:** The entry does not provide Avestan antecedents. The Proto-Indo-European root *demh₂- is identified as the ultimate source for the livestock etymology, but no intermediate Avestan or Proto-Iranian forms are explicitly cited in the available text.
```


### [2026-09-05T17:56:30.945Z] TOOL RESULT

```
# Persian Entry for دد (dad)

**Etymology:** According to the Wiktionary source, the Persian term is "Inherited from Middle Persian [Book Pahlavi needed] (dt' /⁠dad⁠/), 𐫅𐫅 (dd /⁠dad⁠/)."

The entry notes that Middle Persian forms are provided but does not include references to Avestan or Proto-Iranian etymologies in the displayed content. The source indicates a gap where Book Pahlavi script should appear but is not yet supplied by editors.

**Meaning:** In Persian, دد (dad) is an archaic noun meaning "wild animal" or "wild beast," with the antonym being دام (dâm, meaning "tame animal/trap").
```


## [2026-09-05T17:57:02.942Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/diamond",
 "prompt": "Quote the full etymology of 'diamond', including Medieval/Late Latin diamantem, adamantem, Greek adamas, and any note on the folk-etymological origin."
}
```


## [2026-09-05T17:57:04.965Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%86%D8%AF%D8%A7%D9%86",
 "prompt": "Give the Persian entry for دندان 'tooth': full etymology exactly (Middle Persian dandān, Old Iranian, Proto-Indo-European root), and any mention of دنده 'rib'. Also note which PIE root is cited (*h₁dónts / *h₃dónts or *denḱ-)."
}
```


### [2026-09-05T17:57:08.613Z] TOOL RESULT

```
# Etymology of Diamond

The word "diamond" originated in the mid-14th century from Old French *diamant*, tracing back through Medieval Latin *diamantem* to Latin *adamantem*, ultimately deriving from Greek *adamas* (genitive *adamantos*).

**Key etymological pathway:**

The Greek *adamas* was originally "an adjective meaning 'unbreakable, inflexible,'" referring to a hypothetical hardest material. The term's origin remains uncertain, though scholars propose it may derive from *a-* (not) plus *daman* (to conquer/tame), potentially yielding "invincible."

**Folk-etymological note:**

The Vulgar Latin form *\*adiamantem* "was subsequently altered by influence of the many Greek words in *dia-*," demonstrating how the word underwent phonetic reshaping through association with common Greek prefixes.

**Semantic evolution:**

Notably, "the name has thus always been of indefinite and fluctuating sense," having referred variously to hypothetical hardest materials, metals, sapphire, magnets, steel, and emery before settling on diamond specifically.
```


### [2026-09-05T17:57:11.911Z] TOOL RESULT

```
# Persian Entry for دندان (Tooth)

## Etymology

The Persian entry traces the word through Middle Persian *dntʾn'* (dndʾn /dandān/), Old Persian *dantā*, Proto-Iranian *Hdántā*, and ultimately Proto-Indo-European *h₃dént-ō ~ *h₃dn̥t-nés*, derived from the root *h₃dent-* meaning "tooth."

The page specifies: "from [Proto-Indo-Iranian](https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language "w:Proto-Indo-Iranian language") _[\*Hdántā](/w/index.php?title=Reconstruction:Proto-Indo-Iranian/Hd%C3%A1nt%C4%81&action=edit&redlink=1 "Reconstruction:Proto-Indo-Iranian/Hdántā (page does not exist)")_, from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _\*h₃dént-ō ~ \*h₃dn̥t-nés_."

## Regarding دنده (Rib)

The provided content makes **no mention** of دنده or any connection to "rib." The entry focuses exclusively on the dental terminology and botanical sense (purging croton plant).

## PIE Root Citation

The documented root is ***h₃dónts*** (with the laryngeal *h₃*), not *h₁dónts* or *denḱ-*.
```


## [2026-09-05T17:57:33.767Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/zinc",
 "prompt": "Quote the full etymology of 'zinc': German Zink, Zinke 'prong, spike', and any PIE root given."
}
```


## [2026-09-05T17:57:34.479Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tough",
 "prompt": "Quote the full etymology of 'tough': Old English toh, Proto-Germanic *tanhu-, and any PIE root cited (e.g. *denk- 'to bite')."
}
```


### [2026-09-05T17:57:38.501Z] TOOL RESULT

```
# Etymology of Zinc

According to the Online Etymology Dictionary, zinc comes from German *Zink*, derived from *Zinke* meaning "prong, point." The term was reportedly first used by Paracelsus around 1526, applied "on analogy of the form of its crystals after smelting."

The German *Zinke* traces back to Old High German *zint* ("a point, jag"), which descends from Proto-Germanic *\*teng-* meaning "tine." The ultimate source is reconstructed as the Proto-Indo-European root *\*denk-*, which means "to bite."

The modern spelling with *-c-* dates to 1813 and reflects French influence on the word's orthography.
```


### [2026-09-05T17:57:40.285Z] TOOL RESULT

```
# Etymology of "Tough"

Based on the Online Etymology Dictionary entry:

**Old English Origin:**
"from Old English _toh_ 'strong and firm in texture, flexible without being brittle; tenacious, sticky, not easily separated'"

**Proto-Germanic:**
The word derives "from Proto-Germanic _\*tanhu-_" which appears in related Germanic languages like Middle Low German, Dutch, and German variants.

**Proposed PIE Root:**
Watkins suggests the Proto-Germanic form traces back to "PIE _\*denk-_ 'to bite,' on the notion of 'holding fast.'"

The entry notes this semantic connection—the idea that "tough" originally related to something that "bites" or "holds fast," eventually evolving to mean strong, firm, and difficult to break or overcome.
```


## [2026-09-05T17:57:49.450Z] TOOL CALL #58: Bash

```json
{
 "command": "ls site/pages/117.jpg 2>/dev/null; pdftoppm -f 117 -l 117 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg117 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 117"
}
```


## [2026-09-05T17:57:50.597Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%86%D8%AF%D9%87",
 "prompt": "Give the Persian entry for دنده: meanings and etymology exactly as written. Is it derived from دندان/tooth or from something else?"
}
```


### [2026-09-05T17:57:51.799Z] TOOL RESULT

```
site/pages/117.jpg
total 34368
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 13:57 .
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


### [2026-09-05T17:57:55.658Z] TOOL RESULT

```
# Persian Entry for دنده

**Meanings:**
1. Rib
2. Gear, gearstick

**Etymology:**

The word derives from Middle Persian *dandak, which is composed of دند (dand, meaning "tooth") plus the suffix ـه (-e). So yes, it is derived from a tooth-related root, though the modern meanings have evolved to refer to ribs and gears rather than teeth directly.
```


## [2026-09-05T17:57:59.618Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg117.png"
}
```


### [2026-09-05T17:58:00.103Z] TOOL RESULT

```

```


## [2026-09-05T17:58:00.100Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T17:58:14.864Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/demh%E2%82%82-",
 "prompt": "Quote the root, meaning, derived terms and descendants of PIE *demh₂-, especially Indo-Iranian (Sanskrit damáyati), Greek δαμάζω/δάμνημι, Latin domō, Proto-Germanic *tamaz. Any Iranian (Avestan/Persian) descendants listed?"
}
```


## [2026-09-05T17:58:15.347Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/tamaz",
 "prompt": "Quote the etymology and descendants of Proto-Germanic *tamaz 'tame'."
}
```


### [2026-09-05T17:58:21.345Z] TOOL RESULT

```
# PIE *demh₂- Root Summary

**Root and Meaning:**
The reconstructed Proto-Indo-European root is "*demh₂-," meaning "to tame, domesticate."

**Key Derived Terms:**
Notable formations include a causative/iterative form (*domh₂-éye-ti) and various nominal derivatives like *domh₂-o-s and *dm̥h₂-tó-s.

**Major Descendants:**

- **Sanskrit:** damáyati (causative form), with related words for subduing
- **Greek:** δάμαρ (dámar, "spouse"), δάμαλις (dámalis, "heifer")
- **Latin:** domō ("to tame"), domitor ("tamer")
- **Proto-Germanic:** *tamaz (ancestor of English "tame")

**Iranian Descendants:**
The page lists Middle Persian dʾm (dām, "tame animal") and Persian دام (dâm, "livestock"), though the Middle Persian entry notes "[script needed]," indicating incomplete documentation in the source material.
```


### [2026-09-05T17:58:22.176Z] TOOL RESULT

```
# Proto-Germanic *tamaz Etymology and Descendants

**Etymology:**
"From Proto-Indo-European *demh₂-" according to the Wiktionary entry, establishing the word's ancient linguistic roots.

**Descendants:**
The word spread across Germanic languages, including:
- English "tame" (via Old English and Middle English forms)
- German "zahm" (via Old High German "zam")
- Dutch "tam" and Afrikaans "tam"
- Scandinavian forms: Old Norse "tamr" became Icelandic "tamur," Faroese "tamur," Swedish "tam," and Danish "tam"
- Frisian variants in West Frisian and Saterland Frisian
- Low German "tamm" and "tahm"

The term's descendants demonstrate how this Proto-Germanic adjective meaning "tame" evolved across multiple language families over centuries.
```


## [2026-09-05T17:58:30.314Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/demh₂-' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/tamaz' \\\n 'https://en.wiktionary.org/wiki/الماس' \\\n 'https://en.wiktionary.org/wiki/ʾlmʾs' \\\n 'https://en.wiktionary.org/wiki/ἀδάμας' \\\n 'https://en.wiktionary.org/wiki/دام' \\\n 'https://en.wiktionary.org/wiki/دد' \\\n 'https://en.wiktionary.org/wiki/دندان' \\\n 'https://en.wiktionary.org/wiki/دنده' \\\n 'https://www.etymonline.com/word/diamond' \\\n 'https://www.etymonline.com/word/zinc' \\\n 'https://www.etymonline.com/word/tough' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 117, roots Dema / Denk (dâm, almâs, diamond, tame; dandân, dad, tongs/tough/zinc)' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T17:58:34.866Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f40ba55e330d3d36.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e342f4244c935d75.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1cb440938ad4053f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a981569ff2f186f9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/756538cca3516974.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/68bc844e5a63a702.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e3aad8cf0684dbbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfbbf13f5d35351a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f7b0f0ff892435e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f820945022b759a2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6e40cb236c4304e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5db54d34c3ffe35f.txt
```


## [2026-09-05T17:58:47.207Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### WLD Bd1 dema\"; grep -n \"domə-\\|domā-\\|dem[āa]-  ,zähmen\\|zähmen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -6\necho \"### WLD Bd1 denk\"; grep -n \"denk-\\|dek- .zerreissen\\|beissen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -6\necho \"### IEC domā\"; grep -n \"domā\\|damāiō\\|denk\\|donko\" IEC.txt | head -10",
 "description": "Grep Walde-Pokorny and Mann"
}
```


### [2026-09-05T17:58:47.294Z] TOOL RESULT

```
### WLD Bd1 dema
### WLD Bd1 denk
9368:Alte Beziehung von ere- „rudern“ mit cr- „in Bewegung setzen" ist denk- 
24450:Liibke Rom. et. Wb. Nr. 1917, 1918, wofiir kelt. Ursprung freilich denk- 
49501:ostfries. tage „zahe“ (iiber ahd. zahi s. aber unter *denk- „beiBen“), und 
49512:S. Zupitza Gntt. 192 m. Lit. (unter anderer Abgrenzung gegenuber *denk- 
49808:demel denk- 
49837:denk- „bei8en" ( *dank - ?). 
### IEC domā
2243:dəm- (dm-) (theme of dem-, dom-, q. v.) Av. dəma ‘dwelling’; Gk. damáo ‘tame’; Lat. (ambig.) domāre: MHG zemen (2); Go. ga- tamjan, etc.
```


## [2026-09-05T17:58:48.946Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### LKT almas/Diamant\"; grep -n -i \"almás\\|almas\\|Diamant\" LKT.txt | head -10\necho \"### AFM almas\"; grep -n \"الماس\" AFM.txt AFM_pages.txt 2>/dev/null | head -5\necho \"### PLA almas\"; grep -n -i \"almās\\|almas\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5",
 "description": "Grep Lokotsch, Addi Shir, Asbaghi for almās"
}
```


### [2026-09-05T17:58:49.042Z] TOOL RESULT

```
### LKT almas/Diamant
354:[Aus  gr.  dbdiuaq]  'Diamant',  ebenso  pers. u.  tk.;  hieraus  russ.  almaz,  klruss.  al- maz,  hahnaz,  bulg.  serb.  almaz  'dass.'. [Gorjajew  3.    Bern  SlEtWb  27.
2775:'Für  Gold  und  Diamanten  gebrauchtes Gewicht'  [aus  gr.  Kepdxiov,  dieses  nach der  Form  der  Früchte  des  Johannisbrot- baumes, Ceratonia  siliqua,  eigentlich 'Hörnchen',  benannt];  hieraus  sp.  qui- late,  pg.  quirate,  quilate;  mlat.  (bei  den Alchemisten)  carrätus,  it.  carato,  frz. carat,  rum.  carat;  dtsch.  Karat,  engl. carat;  russ.  karat.  —  [Eine  andere  Ab- leitung, die  zwar  der  ursprünglichen Schreibung  Garat  besser  gerecht  wird, aber  dennoch  mit  Rücksicht  auf  die anderen  europäischen  Formen  abgelehnt werden  muß,  gibt  aus  dem  Jüd.-Dtsch. Ave-L  IV,  302.]  [DE  327.  Eguilaz  474. Devic  DEt  85.    ML  6906.    Kluge  227.
2957:1263.  Sskr.  kuruvinda: 'Rubin',  bind,  zu  kurand,  kurund  zu- sammengezogen; hieraus  engl,  corun- dum,  dtsch.  Korund,  frz.  corindon,  sp. corindön,  corundo,  härtester  Edelstein nach  dem  Diamant;  zu  den  Korunden zählt  man  u.  a.  Rubin,  Saphir,  Amethyst.
3229:'Siegreich';  hieraus  afrz.  aumasor,  prov. almasor,  it.  (alt)  almansore  'Feldherr'. Als  N.  pr.  kommt  al-Matisür  in  der Geschichte  des  Orients  häufig  vor.  — ML  :>317.
4149:Ein  Edelstein,  der  dem  Diamanten  an Härte  nahesteht;  hieraus  aram.  sampir, hebr.  sapplr,  ar.  saflr;  aus  dem  Semi- tischen wurde  gr.  ödtT9eipoi;,  lat.  saj)- phirus  und  die  europäischen  Formen hz.  Saphir,  \i.  zafßro;  russ.  sanfir;  engl. sapphire,  dtsch.  Saphir.  —  [Der  Name des  bekaimten  humoristisch-satirischen Schriftstellers  Mor.  SAPHIR  ( 1 795— 1 858) kommt  nicht  hiervon,  sondern  ist  hebr. söcper  'Schreiber'  zu  secper  'Buch'.]
8447:almasor  1399
### AFM almas
AFM.txt:460:0 ܠ بمصر حجر الماسككة نافع 5 لعسر الولادة. 
AFM.txt:1808:(الخل ) الماسمين والورد ايضة واحمره ܒ 1 وهو الورد ومنه ܨ 
AFM.txt:3638:& 6 !7 ¿8¢0 :»ܕ ܘ] وهو الماسق 
AFM_pages.txt:288:0 ܠ بمصر حجر الماسككة نافع 5 لعسر الولادة.
AFM_pages.txt:1105:(الخل ) الماسمين والورد ايضة واحمره ܒ 1 وهو الورد ومنه ܨ
### PLA almas
2933:@W1- ”almäs: "Diamant" pers. rWi almäs <T mp. = almas. 
17783:Wo - al-mäs: "Diamant" 18 MP. almast "the hardest of the metals,
```


## [2026-09-05T17:58:59.561Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### PLA context\"; sed -n '2930,2938p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"---\"; sed -n '17780,17795p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt\necho; echo \"### LKT context\"; sed -n '348,358p' LKT.txt\necho; echo \"### WLD denk\"; sed -n '49830,49860p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Context for Asbaghi, Lokotsch, Walde-Pokorny"
}
```


### [2026-09-05T17:58:59.650Z] TOOL RESULT

```
### PLA context


3 _ 
@W1- ”almäs: "Diamant" pers. rWi almäs <T mp. = almas. 
za; gT - al-Nobaht: "Nachkommen v. == Nobaht, eine Gelehrtenfamilie". 


aTt- ämäf: "Zielscheibe; Pflug" aus dem pers. 2LT amäß 

---
sh - mazariyün: "eine Heilpflanze" pers. 12 MP.sypı x marzangös 13, 
syr. hr 14 lat. mezreon. 

Wo - al-mäs: "Diamant" 18 MP. almast "the hardest of the metals, 
possibly steel" borrowed from griech.agalas » np. almäs " diamond" 16, 


1. BQ. s. v., Muhlt s. v., Addai Scher s. v. 
2. Nyberg Bd. IIs. v. 

3. ebda. 

4. Kamäl s. v. 

5. Löw s. v. 


### LKT context
a)  Mit  wa,  einer  Beteuerungs-  u. Schvvurparlikel,  ergibt  sich  ar.  walläh 'bei  Gott'.  Diese  Schwurformel  [die übrigens  viel  häufiger  war  als  hilläh, vgl.  24.  Makäme  Hariris  I,  290  u.  291  j liegt  der  sonst  unerklärten  Formel  sp. valgame  Dios  [alt  vdlanic  Dios  im  Cid u.  noch  im  Don  Quijote,  z.  B.  Anfang des  Prölogo  zum  2.  Teil,  s.  Colecciön de  autores  espanoles  IV.  Leipzig  1891. S.  VII.],  pg.  valha-me  Dios  [alt  valhamc Dens]  zugrunde,  wobei  also  eine  volks- etymologische Angleichung  eines  ara- bischen Wortes  an  ein  spanisches  ein- getreten ist.  Im  andalusischen  Dialekt: ivärgamc  Dios!  [mit  r,  wofür  die  Volks- sprache der  südlichen  Länder  besondere Vorliebe  zeigt,  vgl.  Diez,  Grammatik der  Romanischen  Sprachen.^  I,  203 u.  401].
b)  Ar.  'alä  bäb  alläh,  wörtlich  'zum Tore  Gottes',  d.  h.  'unter  Allahs  Schulz od.  Obhut'  [vgl.  Dozy,  Suppl.  I,  125]; hieraus  prov.  alababala,  a  la  babald [Honorat,  Dict.  Proventjal-Frangais  I,  70 u.  205]  'ohne  Bedenken,  unbesorgt'.
Ebendaher  wohl  auch  rum.  alabala 'Mischmasch,  Neues'  in  der  Redensart: ce  mai  alabala?  'was  gibt  es  Neues?'
c)  Ar.  in  sä  alläh  oder  genauer  in sa'lläh,  vulgär  insalläh,  tk.  insalla  'wenn Gott  will';  hieraus  rum.  ii^ala  'mit  Gottes Hilfe'.  Statt  in  die  Konjunktion  tva gesetzt,  gibt  ica  sa'lläh  das  sp.  pg. oxalä,  ojald  'o  daß  doch'.  [So  jetzt ASIN  PALACIOS  in  Boletin  de  la  R. Academia  Espanola  VII,  cuaderno  33 (junio  de  1920);  besser  als  ML  2875, DE  326,  Eguilaz  466.]
d)  Ar.  lä  iläh  illaHläh  'es  gibt  keinen Gott  außer  Alläh'  [Kur'än,  Sure  2,  256] ist  das  islamische  Bekenntnis  zur  Ein- heit Gottes,  der  sog.  tauhid,  der  als Kriegs-  u.  Schlachtruf  gedient  haben mag.  Daraus  wurde  einerseits  sp.  leli- lies  'der  Ruf  der  Mauren,  wenn  sie  den Kampf  beginnen'  [bei  Don  Ouijote II.  Teil,  34.  Kap.,  in  der  oben  genannten Ausgabe  S.  189,  letzte  Zeile],  anderer- seits vielleicht  sp.  alarido  'Geschrei,  Ge- heul', wohl  auch  frz.  hallali,  dlsch. Halali.  [Rom  Forsch  IV,  374.  ML  4974. Löbel  EITAP  56.  ZDMG  XL,  258,  De- vic  DEt  135.
60.  Ar.  aliiias :
[Aus  gr.  dbdiuaq]  'Diamant',  ebenso  pers. u.  tk.;  hieraus  russ.  almaz,  klruss.  al- maz,  hahnaz,  bulg.  serb.  almaz  'dass.'. [Gorjajew  3.    Bern  SlEtWb  27.
61.  Tk.  altyn:
'Gold'  [Stamm  al  'rot',  s.  hier  Nr.  48], auch  altun.  Hieraus  bulg.  altzn  'dass.', serb.  alduiii-  in  Zusammensetzungen 'Gold-',  russ.  altgn,  früher  '3-,  jetzt 15-Kopekenstück'  [man  beachte  die  Ent- wertung der  ursprünglichen  Bedeutung!], klruss.  altyyi  '3-Kopekenstück'.  —  Aus dem  tk.  Deminutiv  altyngiß-  wurde  rum. alfingic  'Kapuzinerkresse,  Tropaeolum malus'  [wohl  wegen  der  roten  Blüten]. [Gorjajew  3.    Bern  SlEtWb  27/28.
62.  Pers.  alüca:
'Pflaume'  [Berge  DPersFr  39,  Deminutiv von  ala  'dass.'] ;  hieraus  russ.  alyca, hjöa  'dass.',  wohl  über  einen  tat  arischen Dialekt.    [Gorjajew  3/4.

### WLD denk

Zu den gr. Worten aber vielleicbt alb. demje „B,aupe“ (kann fiir *demlis 
stehn), dsmize , dintize „Fleischmade“ (freilicb ist idg. d anlautend im Alb. 
meist durch d-, blofi seltener durch d- vertreten, vgl. Bgm. I 2 530. Die 
Anknfipfung an ghdem- „Erde“ bei G. Meyer und Pedersen KZ. 36, 335 
befriedigt in der Bed. nicht). 

denk- „bei8en" ( *dank - ?). 

Ai. ddgati „beiBt“ (*dwketi), Pf. dadqga (danach auch ein Praes. dqgati ), 
Kaus. dqgdyaie „macht beiBen", dqca-h ,,BiB, Bremse", dqgana-m „das 
BeiBen", dqstra-h, dqsfrU „Spitzzahn, Fangzahn" = av. tizi-dqstra- „mit 
scharfem GebiB, Gezahn" (fiir - dqstra -, s. Bartholomae Airan. Wb. 653) ; 

gr. ddy.voj „beiBe" ( *dnl-no ), aor. edaxov (= Impf. ai. adagani), wozu fut. 
bg^oyai (aber jon. ba^erai), Pf. bebrjyyai, bebyx d>g, sowie bfjy/ua „Bi8" (aber 
bdyfia Nic.) mit Ablautneubildung; baxerov, to baxog „beiBendes Tier" 
(iiber dddf usw. s. *dengh „greifen, beriihren, drficken"); 

ahd. zangar „bei8end, scharf", mnd. tanger „ds., bissig, kraftig, frisch“; 
anord. tgng (gen. tengr und tangar ), ags. tang , tange, ahd. zanga „Zange“, 
d. i. „die zusammenbeiBende"; mit weiterer Yerschiebung zu „zusammen- 
kneifen, zusammendrucken" und „zusammendrangen, verbinden" (wie ai. 
sam-dag- „beiBen, zusammendriicken, dicht auf etwas liegen") wobl as. 
bitengi ,,nahe an einen rfihrend", ags. getang ds., getenge „nahe anliegend, 
bedrangend", ahd. gizengi „reichend bis, nahe rfihrend an", Adv. gizango , 
wozu anord. tengja ( Hangjan ) „verbinden“, ags. tengan „angreifen, drangen, 
vorwarts streben", getengan „haften machen, fiigen" (ags. intinga m. ..matter", 
sam-tinges „at once“, getingan , st. Y., .,driicken an" nach Fick III 4 152 Neu- 
bildung? anders fiber bitengi usw. unter dengh- „wohin reichen") ; daneben 
germ. *tanhu- „fest anliegend, anhangend, zahe" in ags. tbh „zahe“, mnd.
```


## [2026-09-05T17:59:12.389Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### WLD demə zähmen\"; grep -n \"dem[eaā9ə]*- „zahmen\\|zahmen\\|„zahm\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8\necho; echo \"### SYN tame concept\"; grep -n \"3.14 DOMESTIC\\|TAME (adj\\|4.27 TOOTH\\|TOOTH$\" SYN.txt | head -10",
 "description": "WLD dem- and Buck concepts"
}
```


## [2026-09-05T17:59:14.247Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### NYB dām/dad\"; grep -n \"^dam \\[\\|^dat \\[\\|dam \\[d.m\\]\\|'tame animal'\\|wild animal\" NYB_vol2_glossary.txt | head -10\necho; echo \"### CHEUNG dam\"; grep -n \"\\*dam\\b\\|daH-\\|to tame\" CHEUNG.txt | head -8\necho; echo \"### HRN dandan\"; grep -n \"dendän\\|dandän\\|dendan\" HRN.txt | head -8",
 "description": "Nyberg, Cheung, Horn"
}
```


### [2026-09-05T17:59:14.306Z] TOOL RESULT

```
### WLD demə zähmen
5660:des \Valdes“ (Gegensatz cendaid „zahm“ zu ccve). Thurneysen laGt in diesen 
13233:dehnstufig gr. » j/tegog „zahm, mild"' (*„gebandigt“, s. u.), ygiegig. -idog „der 
13234:zahme, veredelte Rebstock", y/uegoco „zahme, mildre" (urgr. ( 7 ); vielleicht 
30504:slav. Sippe von abg. kroitq, krotiti ,.zahmen", krohkz ,,sanft, mild, maBig' 1 , 
30705:kromyty „bandigen“, poln. s-kromie „zahmen, besanftigen“, po-s-kromic 
43184:32, 479), woran mit weiterer Yerschiebung von „matt, besclnvert"' zu „zahm. 
46733:aptilk-stu, -au, -ti „zahm sein“. Fick II 4 124, Pedersen KG. I 126, 180, 
49065:getivedic „zahm, willfahrig" in formantische Beziehung setzen ( dii-ei-to ; 

### SYN tame concept
5996:ODY; BODILY FUNCTIONS AND CONDITIONS 231 Pas 4.27 TOOTH . tunpus Lith. dantis Sous Both ee Lett. zuobs Gtk Sayre Dan. tand ChSl. zabit NG dens Sw. tand SCr. zub Lot. aente OE tap Boh. zub "4 dent ME tothe Pol. zaqb gp. dient NE tooth Russ. zub Rum. dinte Fy Du. tand Skt. dant- Ke det, far ad) OHG zan(d) Av.  datd- dantan- Nir. fiacal (a? MHG zan(t) W. oer NHG zahn la im F - + of the words for ‘tooth’ belong 2. Ir. fiacail, NIr. fiacal, deriv. of a Pe eeiiarited group. rare fec ‘tooth’ (Windisch 538), NIr.
```


### [2026-09-05T17:59:14.408Z] TOOL RESULT

```
### NYB dām/dad
1174:dak [d^k'], v. hu-däk, kār-dāk, véh-dak. dälman [d'lmn'] a raptorial bird, prob- ably the vulture 942128, — < *darnu- mani-, SW form of Av. (1683) zaranu- mani-, an epithet of the kahrkasa, v. karkas. — Phl. Vd. in à commentary on T? has ~ with the NP gl. bim ‘owl’. — NP dalman. V. Bailey, ZP 137 n. 2. dam [d’m] creation, preferably referred to Ohurmazd, but also to Ahriman: created being 637; — coll. the created beings, the created world 31?! and passim ; ~ u dahišn, v. dahišn; — pl. cas. obl. ~-ãn 7319. 7624. 7716, 7917. 8012, 8922-28, 10215. — From dà-, v. datan; Av. (736) dämi-; MPrthPrs d?m; Paz. dam, Skr. v. srsti; NP dam of animals.
1226:dat [dt'] wild animal 9725, 984, — Av. (678) daitika-; NP dad(ah).
1227:dat [d?t'] 1. law 6413-19, 6916, 8623, 9811, — 2. age 2?9 (with the gl. hangäm). 31. 10*%. 14°. 165. 622. 104°; cas. obl. dātēh 536-22, — 3. created, pt. of dätan: dēvān ~ created by the devs 1038-10-13, — 1. Av. (726) ddta- NP ddd ‘justice, equity’. — 2. NP dad ‘life, age’. — 3. Av. (671 sq.) daēvē.dāta-. dätan [YHBWN-tn'; d’tn' 119%, 1201] dah- [always YHBWN-], lst p. sg. YHBWN-m = dahom; 3d p. sg. = 2nd p. pl. ~ -yt = dahét; lst p. pl. ~-ym = dahem; 3d p. pl. ~-d = dahénd; subju. 2nd p. sg. —-'h = dahäh 34%; imp. sg. ~ = dah; pt. = pret. pass. 3d p. sg. dāt [YHBWN-t', inser. YHBWN; d>t' 22. 922 etc.] lst sg. dāt hom 57°; 2nd p. sg. dāt h&5'1*-* 3d p. pl. dāt hend '18?, construed as an act. form 18?!; pluperf. 3d p. sg. dat estet 8712, 3d p. pl. ~ ēstēnd 94*4; opt. pass. dāt [HWH-d =] he 2%; A. to give SPrs:15; 238-21 ete. passim; apāc ~ to give back 345-6; — fräc ~ to give away 5016-1’; — v, also dröt, framān, passax", zančh. — B. 1. to put, to place,

### CHEUNG dam
4650:*damH ‘to tame’ 
4652:*KHOTANESE: *dim- (dan-, dan-) ‘to tame’ = SGS: 45 
4654:*CHORESMIAN: ömy- ‘to tame’, öms- (pass./sec. inch.) ‘to be tamed’ © Samadi: 66 
4655:*NEIR: Oss. I. domyn/domd, D. demun/dend ‘to tame’ || (+ *aua-) Oss. I. 
4660:«PIE *demH»- ‘to tame’ => LIV: 116 f. | Pok.: 199 f. 
4663:Lat. domäre ‘to tame, overpower’, Olrish damnaim ‘I bind, overpower’, NHG 
4666:zähmen, Engl. to tame, etc. 
21242:BSogd. 'Bs"'c- ‘to tame, train’ || (+ *a-) CSogd. ’s’qy ‘suitable’ || (+ *pati-) BSogd. 

### HRN dandan
1221:ciinänci derd-i dendänrä senöse
5162:574. dendün 'Zahn*^), dendäne 'Mauerzinne'.
5163:aw. vTmitö.lidanfa7i'; phlv. dandän (AV., Bund.);
5167:dendäHj sar. dandän, wa/. dundäk.
10237:ci meS-l berri bedendänes dt be/te ve säk
```


## [2026-09-05T17:59:38.436Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '49770,49812p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "WLD dem- zähmen entry"
}
```


### [2026-09-05T17:59:38.490Z] TOOL RESULT

```
passae ££ , ncymr. goddef „leiden, erlauben ££ , corn, gothaf „ertragen“, bret. 
gouzauv, gouzav ds. (aber cymr. doji „ziihmen“, acymr. dometic „gezahmt ££ , 
ar-domaul „gelehrig <£ , cymr. dof, bret. doff „zahm“ stammen wohl nach 
Thurneysen aus lat. domare , so daS einheimische Formen mit o dem Kelt, 
fehlten) ; 

got. gatamjan, anord. temja, ags. temian , ahd. zemmen „zahmen“ (*do>ne>5 
= ai. damayati ), ahd. zamBn ds. (= lat. doma-re), anord. tamr, ags. tam, 
ahd. zam „zahm“ (unklar, ob Riickbildung aus dem Yerbum, oder ob die 
pass. Bed. aus „Zahmung = Gezahmtes" erwacbsen ist, so dafi in ge- 
schichtlichem Zusammenhang mit ai. dama-h „Bandigung“). 

Wegen ai. damya- „zu ziihmen ££ und „junger Stier, der noch gezahmt 
werden soll“ und wegen gr. dafifoyg einerseits „bezwingend, bandigend“ 
{"Eqcos, Anakreon), andrerseits „junger (noch zu zahmender) Stier", wozu 
baf.ia.Xg „junge Kuh“, bayaXig „ds.; auch von einer jiaoiXivog ab : u>]g'\ 
ba/uaXog „KaIb ££ (s. z. B. Fraenkel KZ. 42, 115) ist wohl auch air. dam 
„Ochse £< ( *damos ), dam allaid „Hirsch“, corn, da „dama ££ sowie cymr. dafad , 
acorn, dauat , bret. dahvat „Schaf' £ (dann = gr. a-bajuaro; ) anzureihen (ur- 
sprgl. Bezeichnungen gezahmter Horntiere; Zweifel itulBerte Yf. LEWb. 2 
u. damma oder datna , das wohl aus dem Kelt, oder anderswoher entlehnt 
ist; germ. Lehnformen s. bei Falk-Torp u. daadyr m. Lit.); entsprechend 
niederosterr. zamer, zamerl ,.junger Ochs" (Much ZfdA. 42, 167; vorgerm. 
*a oder *ot). 

Curtius 5 232, usw. 

Zusammenhang mit dem- „(bauen), Haus“ als „ans Haus gewohnen, 
domestizieren" ist sehr wahrscheinlich ; nicht als „binden“ zu xQrj-dejuvov, 
da andere Spuren einer solchen Wz. dem- fehlen (gegen Curtius aaO., 

51* 



790 


demel denk- 


y. Grienberger SBWienerAk. 142, YIII 93 f., der Hem- „bauen“ auch als 
„verbinden“ fafit, Falk-Torp u. tam ; siehe Yf. LEWb. 2 u. redimio, Boisacq
```


## [2026-09-05T17:59:39.262Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SKT diamond\"; grep -n \"DIAMOND\\|^Diamond\" SKT.txt | head -3\necho \"### SKT tongs/tough/zinc/tame\"; grep -n \"^Tongs\\|^Tough\\|^Zinc\\|^Tame\" SKT.txt | head -6",
 "description": "Skeat entries"
}
```


### [2026-09-05T17:59:39.330Z] TOOL RESULT

```
### SKT diamond
### SKT tongs/tough/zinc/tame
19122:Tame,  adj.  (E.)  M.  E.  lonw.  A.  S. tarn,  tame;  whence  tamian,  ttmian,  to lame.  -^  Da.  tarn,  Icel.  tamr^  Swed. Dan.  /am,  G.  tahm.  Allied  to  L.  domart, Skt.  dam,  Gk.  Sa>id(ir,  to  tome.  {^DAM.) See  Daunt.
19944:Tough.  (E.)  M.  E.  A tough,  •f  Du.  taai,  fludbl lough;  G-  ziihe,  O.  H.  G acious.  Pcrhapi  allied  t rend  (orig.  to  bile  ^  Gk.  9 that  whidi  resists  biting.
```


## [2026-09-05T17:59:47.176Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### ARY latin index dam/dandan\"; grep -n \"DAM\\b\\|DANDAN\\|ALMAS\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"### ARY persian\"; grep -n \"دام‌\\|دندان\" incoming/ARY/ARY_pages.txt | head -8",
 "description": "Grep Aryanpur"
}
```


### [2026-09-05T17:59:47.242Z] TOOL RESULT

```
### ARY latin index dam/dandan
3747:BODAM BUDHNA, (SANSKRIT) oy Svailee
3759:BODAM — (OLD SAXON) 4S ip-Ste
5235:PEDA LATVIAN) (93) gi 3 PATI. PADAM.
7565:TAM . (DANISH) Sails DAM HPAHLAVD) «5 hg,
7568:TAM (DUTCH) gale ’ DAMYATI, DHAMAN, DAM , DAMYA-
8119:OLD HIGH GERMAN) of gilt DAM, DAMISHN — (PAHLAVI) 15 he
8122:i *DAMP — (OLD ENGLISH) 5 pul) DAM BALUCHI) gz yh
8165:TOOTH ENGLISH) gaSi\ DAD, DANDAN (PAHLAVI) shay
8863:MALLORY & ADAM: RESG RUSCH, RISCH DUTCH) gity oe
11638:(OLD SCANDINAVIAN) 95 -th-11 KADAM, KATAM —_:(PAHLAV1) 5 3h
### ARY persian
112:کشاورزی و اهل‌سازی دام‌ها نو آوری شد و این نوآوری‌ها شهرزیستی و ازدیاد جمعیت و ایجاد
1052:ویژگی‌های ابر انسانی ضامن خوبی محصول و زایندگی دام‌ها و پر ماهی بودن رودها و فراوانی
1246:آلمانی همریشه است. همینطور واژه‌ی فارسی «دندان» با واژه‌ی آلمانی 2۸1721 همريشه است ولی
1540:- چم این واژة در زبانیونانی و لاتین: حفره» لوله حفره‌ی فک که دندان در آن قرار دارد.
6378:چم این واژه در فریزی کهن: دندان کرسی.
12982:چم این واژه در زیان‌های رومانس نرین؛ فساد دندان, ا
```


## [2026-09-05T17:59:55.299Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7560,7572p' incoming/ARY/ARY_latin_index_pages.txt\necho \"---\"\nsed -n '8160,8170p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "ARY index context"
}
```


### [2026-09-05T17:59:55.367Z] TOOL RESULT

```
alles py gent sd CJai" oe 493A) TAG gl y DAY eS ads -¥
,
[pdf page 262]
TAY L Cal ale’ pox u) pla .
TAME . ENGLISH) p58 DAMAN HAVESTAN) goa 3)
TAM . (DANISH) Sails DAM HPAHLAVD) «5 hg,
TAM (SWEDISH) (5. yo DOMUN, DOMYN — (OSSETIC) 3)
TAM NORWEGIAN) 6555 SANSKRIT) ay Sail
TAM (DUTCH) gale ’ DAMYATI, DHAMAN, DAM , DAMYA-
DAMNAID (OLD IRISH) 455-1 GREER) gli.
GODDEF, ADDEF —(WELSH) «535 DAMAN, DAMNANAI, ANATHEMA
ANSAU, DANVAT —:(BRETON) og 5. LATIN) oa
DAMASZI AAITTITE) ease DOMARE, DOMITAR, DOMO
---
. py eS il-
ye sere OTs li gliy U5 09 Sls ot pe
ae Sj ond gla aah 5 9) Sea sobs 2 Sls ot
ZAHN (GERMAN) gait DANTA, DANTAN  (AVESTAN) os!
TOTH — (OLD ENGLISH) 1S) DANTAN (OLD PERSIAN) deol, e+
TOOTH ENGLISH) gaSi\ DAD, DANDAN (PAHLAVI) shay
TAND DANISH) jails DANDAG (OSSETIC) gos!
TAND SWEDISH) ity DIDAN, DINDAN (KURDISH) 52,8
TAND NORWEGIAN) 5333 DANTAN, DATAN — (BALUCHD) ge gh
TAND DUTCH) ta DAN, SANSKRIT) 2 Sila
DZIEGNA (POLISH) iting) DANT-, DANTAM, DATAS, DANTA
```


## [2026-09-05T18:01:27.529Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### BRT daman/dami col 736\"; python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'^\\s*73[5-7]\\s*$', l, re.M):\n        print('leaf',i,re.findall(r'^\\s*(73[0-9])\\s*$',l,re.M))\n        for m in re.finditer(r'd[aä]m[ai][n\\-]', l):\n            print('   ...', l[max(0,m.start()-150):m.start()+250].replace('\\n',' '))\n        break\nEOF",
 "description": "Find Bartholomae dāman-/dāmi-"
}
```


## [2026-09-05T18:01:28.798Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 340<i<400 and 'الماس' in l:\n        print(i, l.count('الماس'))\nEOF",
 "description": "Find BQT vol1 almās page"
}
```


### [2026-09-05T18:01:29.416Z] TOOL RESULT

```
### BRT daman/dami col 736
leaf 423 ['737']
   ... d.)  huxratus. .  spmtqmlä  ärmaitim °iinm  (ASf.)  ".  .  und  an  der  heiligen  Arm., der  schaffenden"  Y.34.  10;   —   'mim  .. dby  Google 737 dämi-dät* ynm  ärmaitim  spintqm  Yi.iff.a'K         [S. noch  ^(iämay-  No.  a.) KompA.  —  Zum  V.  da-.  —  Pü.:  i/am,  Sü.: irt'i^.  —  '1  Vgl.  Y.  31.  8,  45-  4.  47-  '.  wo ßeai-'  statt  iZ/fmiij':  —  'I  Offenbar  im  Anschtuss an  Y. 
   ...  di-.  -  Pu.  (suV. /p.  15): aSm  /iil.ir,  (lu  V.  rg.  35):  danai').  —  D  NA. tiqma  dältm.  —  »)  Vgl.  za  dämi.däla: •  j.  dämLdäta-'),  dami-däta-  Adj.  (fem. VJ-)  'vom  Schöpfer  (AhM^  geschaffen'" von  Gottheiten:  aurvant»m  ^ws  (näml. Aaom^m)  °Um  Y.  io.  10';  —  mikrtm  .  . 't^/n  YLJO.61;  —  a/i"  srTi-e  'oatte  (VSf.) Yt./7.6o,  61;  —  gsusca  una  -/jYt  74.54. Pii
```


### [2026-09-05T18:01:31.040Z] TOOL RESULT

```
377 1
```


## [2026-09-05T18:01:37.606Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==378' BQT_v1_pages.txt | tail -30",
 "description": "BQT vol1 leaf 377 (p.159) almās"
}
```


## [2026-09-05T18:01:39.082Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (422,423):\n    l=leaves[i]\n    for m in re.finditer(r\"d[äa]man-\", l):\n        print(i,'>>>', l[max(0,m.start()-200):m.start()+300].replace('\\n',' '))\n        print()\nEOF",
 "description": "Bartholomae dāman- entry"
}
```


### [2026-09-05T18:01:39.177Z] TOOL RESULT

```
الوج
بلئد آشیان مبکند آن قلعه را بدین‌نام خواندند
و بکثرت استعمالالموت شده است . گوبند در
زمان سلطان ملکشاه آن قلمه را حسن صباح
کرفت و مدتهادر صرف ملاحده بود و تاریخ
کرفتن آن نیز «الموت» است .
) لنجان - بفتم اول و کسر انی‌وسکون
نون و جیم بالف کشیده و پنون دبگر زده » نام
الکه‌ایست در صفاهان که بر نخوب درآ نجاحاصل
میشود و بثه بسیار هم دارد ؟ .
النگ « بفتح اول‌بروزن بان گه «سمعئی
پناه ودبواری‌باشد که‌بواسطهُ کرفتن فلعموه‌حافظت
خود سازند - و جممی را نیز گونن دکه مردم
بیرون قلمه جابجابجهت گرفتن قلعه و مردم‌درون
قلعه بواسطٌمحافظ‌فلعه تعین کنند - و سم‌اول
بزبان تر کی سبزمزار باشد .
النگه - بنتح اول و ثانی و سکونات
و فتح کاف . شعلةٌ آنش را گود .
النی - بفئح اول و سکون انی و کس
تالك بتحتانی‌زده » چوب بازوی دروازمرا گوبشد .
الوا - بروزن حلوا , صمفی باشد بیار
تلخ‌وآ ترابعربی صبر گوبند وبهترین آن سقوطری
است و تیزمدار او بوده است » و باین دو معنی
بکسر اول عم اعده ایح انب وا ینم اول ستاره را
گوبند و بعربی ک و کب خوانند .
الوج » بنتح اود و ضم نالی وسکون
باشد بیار درشت و خشن. گنل آنکبود وتضش
سیاه هبباشد » در متکنتان و کوضتان میرون .
۴ - ازبوتانی
۴ رك : آله و آموت .
```


### [2026-09-05T18:01:40.989Z] TOOL RESULT

```
422 >>>   'von  der  Länge eines  Flusses,  so  lang  wie  die  Flüsse': aisis  bassaza  . .  sim.fi-a^anha  (sd.)  'ja»ha (APn.)'>  kvar3.bamai9ha  Y.  60. 4. Pü.:  rol  draknäk.  —   ')  Tbem. •  j.,  g.  'däman-,  d^man-''  n."  i)  im gAw.  'Stätte,  Wohnstatte'  in  eschato- logischcm  Sinn,  Plur.:  ai  hsi  'mqm  (NP.) ^■uiaAmT  a  dam  (Sp.  684  o.)  ahurä  Y. 4(9.  7  j  —  drüjh  kvS  -man  (AP.)  *haB>!ahy<'t gät  (sd.)  ".  .  zu  den  Wohnstätten  derer, die3>  .  ."  ^.46.(>.  2)  im  jAw

422 >>>   mask.  und  asaoninqm ,  fem.  Tcrbundeii ist;  I.  in  itay-  Sa.  1.  —  3)  So  ist  Sp.  517  ro. IQ  verbessern.  —  O  Pü.  bietet  ^schlich dakm;  3,  aber  Sü.  —  51  Vgl.  No.  1. •  ).  'däman-  n.  'Absicht'. :      KompE.  —  Zum  V.  'dö(y)-. I«  j,  g.   'dämay-    f.  'SchöpfuDg":    'möis \  urvag!e(sA.)  apjml  Y.  4j.  s";  —  ki'ö  °iiisls drüjs    Aunus
```


## [2026-09-05T18:01:52.012Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 374 375 376; do echo \"### leaf $L ###\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n \"الماس\\|المآس\\|الما\" ; done",
 "description": "Find almās headword in BQT vol1"
}
```


### [2026-09-05T18:01:53.708Z] TOOL RESULT

```
Exit code 1
### leaf 374 ###
### leaf 375 ###
### leaf 376 ###
```


## [2026-09-05T18:01:57.620Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 350<i<400:\n        for w in ['الماس','لماس','الماء','الم ']:\n            if w in l:\n                print(i,w)\nEOF",
 "description": "Search BQT vol1 for almās variants"
}
```


### [2026-09-05T18:01:59.632Z] TOOL RESULT

```
372 الماء
377 الماس
377 لماس
377 الم 
399 الم
```


## [2026-09-05T18:02:02.388Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==378' BQT_v1_pages.txt | grep -n -B3 -A6 \"الماس\"",
 "description": "Show almās context in BQT leaf 377"
}
```


### [2026-09-05T18:02:04.308Z] TOOL RESULT

```
14-لم ت بنم اول و ثانی و سکون میم »
15-بمعنی فوج و گروه باشد - و پفتح اول غلایست
16-که آنرا کاوری و ارزن کوبند .
17:الماس؟ - بروزن کربای . کوهریست
18-حشهور - و کنابه از تیغ وشمشیر و کاردسوتیر-
19-و آبگینه و مردم جلد و چابك باشد -وبمنی
20-فلم‌تراش هم هست - و دندانرا نی زگویند .
21-بالف کشیده ولام ۶۰ توح بفاف‌زده » نام ولایتی‌است.
22-الم‌الم بضم دوهمزه و دو لام وسکون
23-دو میم ۰ بمعنی گروء کروه وفوج فوج بود. چه
```


## [2026-09-05T18:02:09.862Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==378' BQT_v1_pages.txt | grep -n \"بوتانی\\|یونانی\\|^۴\\|^ *۴ *-\" ",
 "description": "Mo'in footnote on almās page"
}
```


### [2026-09-05T18:02:11.486Z] TOOL RESULT

```
58:۴ - ازبوتانی
59:۴ رك : آله و آموت .
```


## [2026-09-05T18:02:22.173Z] AGENT

Now I'll write the verification file.


## [2026-09-05T18:02:24.778Z] TOOL CALL #81: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg117.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/117.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T18:02:24.868Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T18:16:07.433Z] TOOL CALL #82: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/117.png",
 "description": "Confirm page image copied"
}
```


### [2026-09-05T18:16:07.479Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 64811 Sep  5 14:02 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/117.png
```


## [2026-09-05T18:17:29.772Z] TOOL CALL #83: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117 && python3 - <<'PYEOF'\nimport json,io\nd = {\n \"entry\": 0,\n \"root\": \"Dema\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *demh₂- 'to tame, domesticate (esp. break in cattle/horses)' (Pokorny 199 demə-, domə- 'zähmen, bändigen'; Walde-Pokorny I 788-790; Watkins/AHD demə-²; LIV² 116)\",\n \"note\": \"The root box is right on all three counts. Pokorny p.199 heads the entry '(demə-), domə- ,zähmen, bändigen'; Partiz. Pass. dm-tó-s, doms-tó-s; domo-s und domo-s ,zahmes Tier, zahm', domio-s ,junger, zu zähmender Stier'', so the reconstruction, the label 'Indo-European' and the gloss 'to tame and domesticate animals' are exactly the handbook gloss; Pokorny even adds that the root is 'eine alte Abzweigung' of dem- 'house', originally 'ans Haus fesseln, domestizieren', which is precisely Nourai's 'domesticate'. Two things a reader should know. (a) The whole chart is built out of the AHD (Watkins) appendix entry demə-², whose text reads 'demə-². To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *domā- in Latin domāre, to tame, subdue: DAUNT; INDOMITABLE. 3. Zero-grade form *dmə- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (demə-), domə- 199.]' — Nourai's Greek and Germanic node glosses are Watkins' words verbatim, and the DIAMOND branch is Watkins' too. (b) Nourai's own contribution is the Iranian left-hand branch, and that is where the chart is weakest: Pokorny's page does contain 'npers. dam ,zahmes Tier'' (so the Persian node is directly authorised by the cited page), but there is no Avestan word dāman- 'domestic animals', and Nourai's Avestan box conflates the *demh₂- word with the wholly different Avestan dāman- 'creature, creation, dwelling' (< dā- 'to create'). See node 1.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *demh₂- «رام کردن، اهلی کردن (جانوران)» ریشه‌ای اصیل و پذیرفته‌شده است؛ پوکورنی در صفحهٔ ۱۹۹ همین صورت و همین معنا را می‌آورد و حتی می‌افزاید که این ریشه شاخه‌ای کهن از dem- «خانه» است و نخست معنی «به خانه خو دادن، اهلی کردن» داشته است — یعنی دقیقاً همان که نورایی در جعبهٔ ریشه نوشته است. باید دانست که سراسر این نمودار — معناهای یونانی و ژرمنی و شاخهٔ diamond — واژه‌به‌واژه از مدخل demə-² در پیوست واتکینز (فرهنگ American Heritage) برداشته شده است. سهم خود نورایی شاخهٔ ایرانی است، و همانجا سست‌ترین بخش نمودار است: فارسی «دام» را خود پوکورنی در همان صفحه ذکر کرده («npers. dam ‹zahmes Tier›»)، ولی در اوستا واژه‌ای به صورت dāman- به معنی «جانوران اهلی» نداریم؛ آنچه هست dāman- «آفریده، آفرینش، جایگاه» از ریشهٔ dā- «آفریدن» است و دو واژهٔ هم‌نگاشت‌اند (نگاه کنید به گرهٔ ۱).\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/demh₂-\",\n   \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/tamaz\"\n ],\n \"ref_check\": [\n  {\"ref\":\"POK:199\",\"status\":\"supports\",\"note\":\"POK_01.txt leaf 207-208 (= printed pp.199-200): '(demə-), domə-, domə- ,zähmen, bändigen'; Partiz. Pass. dm-tó-s, doms-tó-s; domo-s und domo-s ,zahmes Tier, zahm'...' and, just above it, 'Eine alte Abzweigung unserer Wz. ist demā- ,zähmen', ursprüngl. wohl ,ans Haus fesseln, domestizieren'. WP. I 786ff.' The page number Nourai cites is exact and the gloss is Pokorny's own.\"},\n  {\"ref\":\"KLN:442\",\"status\":\"supports\",\"note\":\"Klein 1966 vol. 1 s.v. 'diamond' (D section, the printed page Nourai numbers 442; the local OCR KLN_1966.txt line 11255-11256 carries no page marks): 'diamond, n. — ME. diamant, diamaunt, fr. OF. diamant, fr. Late L. diamantem, acc. of diamās, which is a blend of Gk. ἀδάμας, ‘adamant, diamond’, lit. ‘unconquerable’ and διαφανής, ‘transparent’. See adamant and diaphanous.' Klein's cross-referenced entry 'adamant' adds 'fr. Gk. ἀδάμας ... lit. ‘unconquerable’, fr. ἀ- (see priv. pref. a-) and the verb δαμᾶν, ‘to tame’. See tame'. So the cited page does carry the root-to-diamond claim, though not a root box of its own.\"}\n ],\n \"consulted\": [\n  {\"src\":\"WLD\",\"where\":\"Bd. I pp.788-790 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt lines ~49770-49808)\",\"stance\":\"supports\",\"note\":\"'got. gatamjan, anord. temja, ags. temian, ahd. zemmen „zähmen“ (*domeyō = ai. damayati), ahd. zamōn ds. (= lat. domā-re), anord. tamr, ags. tam, ahd. zam „zahm“' and the closing paragraph 'Zusammenhang mit dem- „(bauen), Haus“ als „ans Haus gewöhnen, domestizieren“ ist sehr wahrscheinlich'. Pokorny 199 is a reprint of this page.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt line 364, s.v. demə-²\",\"stance\":\"supports\",\"note\":\"'demə-². To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *domā- in Latin domāre... 3. Zero-grade form *dmə- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (demə-), domə- 199.]' — Nourai's Greek, Latin and Germanic boxes are this entry rearranged.\"},\n  {\"src\":\"IEC\",\"where\":\"IEC.txt line 2243, s.v. dəm-\",\"stance\":\"supports\",\"note\":\"'dəm- (dm-) (theme of dem-, dom-, q.v.) Av. dəma ‘dwelling’; Gk. damáo ‘tame’; Lat. (ambig.) domāre: MHG zemen; Go. ga-tamjan, etc.' — Mann reconstructs the same root; note that the only Avestan item he can adduce is dəma 'dwelling', i.e. the HOUSE word, not an animal word.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt lines 4650-4666, root *damH 'to tame'\",\"stance\":\"partial\",\"note\":\"'*damH ‘to tame’ ... KHOTANESE: *dim- (dan-, dan-) ‘to tame’; CHORESMIAN: δmy- ‘to tame’; NEIR: Oss. I. domyn/domd, D. demun/dend ‘to tame’ ... «PIE *demH₂- ‘to tame’ => LIV: 116 f. | Pok.: 199 f.»'. Cheung's Etymological Dictionary of the Iranian Verb confirms the root for Iranian, but lists NO Avestan and no Old/Middle Persian verb — the Iranian evidence is Khotanese, Chorasmian and Ossetic only.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt line 19122, s.v. Tame\",\"stance\":\"supports\",\"note\":\"'Tame, adj. (E.) M.E. tam. A.S. tam, tame; whence tamian, temian, to tame. + Du. tam, Icel. tamr, Swed. Dan. tam, G. zahm. Allied to L. domāre, Skt. dam, Gk. δαμάζειν, to tame. (√DAM.) See Daunt.'\"}\n ]\n}\njson.dump(d, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/e0head.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 0 header"
}
```


### [2026-09-05T18:17:32.415Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:19:09.085Z] TOOL CALL #84: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nnodes=[\n{\n \"id\":1,\"lang\":\"Avestan\",\"words\":\"dâman 1\",\"verdict\":\"disputed\",\n \"derivation\":\"Avestan dāman- is a real word, but it does not mean 'domestic animals'. Bartholomae, Altiranisches Wörterbuch cols. 735-737, gives '¹dāman-, dąman- n. 1) im gAw. ‘Stätte, Wohnstätte’ ... 2) im jAw. ‘Geschöpf, Schöpfung’' and '²dāman- n. ‘Absicht’', all built on the verb dā- 'to put, to create' (PIE *dʰeh₁-), beside dāmi- f. 'Schöpfung' and dāmi-dāta- 'created by the Creator' (col. 737). That word gives Middle Persian dām 'creature, creation' — MacKenzie, Concise Pahlavi Dictionary p.24: '¹dām [dʾm | = M] creature, creation' — which MacKenzie keeps strictly apart from '²dām [dʾm | = M, N ~] tame animal' and '³dām [dʾm | P dʾmag, N ~] net, snare, trap'. The word behind Persian دام 'livestock' is the second of those, the continuant of PIE *dm̥h₂-o-/-*domh₂-o- 'tamed (animal)', and it has no Avestan attestation at all: Pokorny 199 jumps straight from Old Indic to 'osset. domun ‘zähmen’, npers. dam ‘zahmes Tier’', Cheung's Iranian verb dictionary knows *damH only from Khotanese, Chorasmian and Ossetic, and Wiktionary's *demh₂- page lists only 'Middle Persian dʾm (dām, “tame animal”) → Persian دام (dâm, “livestock”)'. Nourai's Avestan box therefore fuses two homonyms. The fusion is not his invention: Moʿin's footnote at Borhān-e Qāṭeʿ p.817 sets out the *demə- cognates (Skt damá-, Gk. δαμάλης, Lat. domāre, Ossetic domun) and then adds 'در پهلوی dām (مخلوق) (اوستا dāman-)', Nyberg (Manual of Pahlavi II s.v. dam) writes 'dam [dʾm] creation ... From dā-, v. dātan; Av. (736) dāmi-; ... NP dām of animals', and Aryanpur's index likewise files 'DĀMAN (AVESTAN)' under TAME. So Nourai is following the Persian lexicographical tradition; but modern Iranian philology (Bartholomae, MacKenzie, Cheung, Wiktionary) separates the two words, and the arrow root → Avestan dāman- 'domestic animals' cannot stand as drawn.\",\n \"derivation_fa\":\"واژهٔ اوستایی dāman- واقعی است، اما معنای آن «جانوران اهلی» نیست. بارتولومه در «فرهنگ ایرانی باستان» (ستون‌های ۷۳۵ تا ۷۳۷) آن را چنین آورده است: «¹dāman- خنثی: ۱) در گاهانی «جایگاه، جای زیست»؛ ۲) در اوستای نو «آفریده، آفرینش»» و نیز «²dāman- «قصد»»، همه ساخته از فعل dā- «نهادن، آفریدن» (هندواروپایی *dʰeh₁-)، در کنار dāmi- «آفرینش». همین واژه در فارسی میانه dām «آفریده، مخلوق» شده است؛ مکنزی (ص ۲۴) آن را از «²dām جانور اهلی» و «³dām دام و تور» به‌روشنی جدا می‌کند. واژه‌ای که پشت «دام» فارسی (جانور اهلی) است همان دومی است، بازماندهٔ *dm̥h₂-o- هندواروپایی، و هیچ گواه اوستایی ندارد: پوکورنی در ص ۱۹۹ یکراست از هندی باستان به «اُستی domun» و «فارسی نو dām ‹جانور اهلی›» می‌رود، و چونگ نیز ستاک *damH را تنها در ختنی و خوارزمی و آسی می‌شناسد. پس جعبهٔ اوستایی نورایی دو واژهٔ هم‌نگاشت را یکی گرفته است. این خلط از خودِ او نیست: معین در حاشیهٔ برهان قاطع (ص ۸۱۷) پس از برشمردن هم‌ریشه‌های *demə- می‌افزاید «در پهلوی dām (مخلوق) (اوستا dāman-)»، نیبرگ نیز dām «آفرینش» را به dā- می‌بَرَد و می‌افزاید «فارسی نو dām دربارهٔ جانوران»، و آریان‌پور هم «DĀMAN (اوستایی)» را ذیل TAME آورده است. با این همه، ریشه‌شناسی امروزی این دو را جدا می‌داند و پیکان «ریشه ← اوستایی dāman- (جانوران اهلی)» به این صورت پذیرفتنی نیست.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/demh₂-\",\"https://en.wiktionary.org/wiki/دام\"],\n \"ref_check\":[{\"ref\":\"BQT:817\",\"status\":\"partial\",\"note\":\"BQT_v2_pages.txt leaf 277 (printed p.817 — the offset printed = leaf + 540 is confirmed by the دند entry on leaf 344 = Nourai's BQT:884). The headword is 'دام = بروزن رام، نقیض دد باشد که آن وحشی غیر درنده است عموماً' and footnote 1 runs '۱ - هندی باستان damá- ... یونانی δαμάλης (گاو نر)، لاتینی domāre (گاو نر، ورزاو)، اُستی domun (رام کردن)؛ در پهلوی dām (مخلوق) (اوستا dāman-)'. So Moʿin's page does put an Avestan dāman- beside Persian دام — but he glosses the Pahlavi word 'مخلوق' (creature), not 'domestic animals', and the *demə- cognates he lists are Indic, Greek, Latin and Ossetic, never Avestan.\"}],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"BRT.txt leaf 422-423, cols. 735-737 s.v. ¹dāman-, ²dāman-, dāmay-, dāmi-\",\"stance\":\"contradicts\",\"note\":\"'¹dāman-, dąman- n. 1) im gAw. ‘Stätte, Wohnstätte’ ... 2) im jAw. ...'; '²dāman- n. ‘Absicht’. Zum V. ¹dā(y)-'; 'dāmay- f. ‘Schöpfung’'; 'dāmi-dāta- ‘vom Schöpfer (AhM.) geschaffen’ ... Zum V. dā-'. Bartholomae has no Avestan dāman- meaning 'domestic animals'; every dāman- he records belongs to dā- 'to put, create'.\"},\n  {\"src\":\"PHD\",\"where\":\"PHD.txt line 306, s.vv. ¹dām, ²dām, ³dām\",\"stance\":\"contradicts\",\"note\":\"'¹dām [dʾm | = M] creature, creation. ²dām [dʾm | = M, N ~] tame animal. ³dām [dʾm | P dʾmag, N ~] net, snare, trap.' MacKenzie lists three separate Middle Persian homonyms; only the second is the ancestor of دام 'livestock', and it is not the reflex of Av. dāman-.\"},\n  {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt line 1174, s.v. dam\",\"stance\":\"partial\",\"note\":\"'dam [dʾm] creation, preferably referred to Ohurmazd... From dā-, v. dātan; Av. (736) dāmi-; MPrthPrs dʾm; Paz. dam, Skr. v. sṛṣṭi; NP dām of animals.' Nyberg does end his entry with 'NP dām of animals', i.e. he takes the Persian animal-word as a continuation of the 'creation' word — the same conflation Nourai draws, and the strongest support the node has.\"},\n  {\"src\":\"ARY\",\"where\":\"incoming/ARY/ARY_latin_index_pages.txt [pdf page 262], index heading TAME\",\"stance\":\"supports\",\"note\":\"Aryanpur's comparative index prints under 'TAME (ENGLISH)': 'DĀMAN (AVESTAN); DĀM (PAHLAVI); DOMUN, DOMYN (OSSETIC); DAMYATI, DHĀMAN, DAM, DAMYA- (SANSKRIT); ... DOMĀRE, DOMITAR, DOMŌ (LATIN); DAMASZI (HITTITE)'. So the Persian tradition Nourai follows does posit an Avestan dāman- here — but note that its Sanskrit column equally mixes damayati with dhāman-, the same conflation.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt lines 4650-4666, *damH 'to tame'\",\"stance\":\"silent\",\"note\":\"No Avestan reflex of *damH is listed at all (only Khotanese, Chorasmian, Ossetic), so there is no Avestan verb or noun of this root for the chart to point to.\"}\n ]\n},\n{\n \"id\":2,\"lang\":\"Persian\",\"words\":\"dâm\",\"verdict\":\"confirmed\",\n \"derivation\":\"Persian دام dām 'livestock, domestic animals' continues Middle Persian dām [dʾm] 'tame animal' (MacKenzie p.24 ²dām), from Old Iranian *dāma- < PIE *domh₂-o-/*dm̥h₂-o- 'tamed (one)', the o-grade noun Pokorny reconstructs as 'domo-s und domo-s ,zahmes Tier, zahm''. The vowel is long throughout (MP dām = NP dām), and no consonant change is involved, which is why the word looks unchanged from Sasanian to modern Persian. That the chain is real, and not merely inferred, is stated in both of the references Nourai cites: Pokorny's own p.199 has 'osset. domun ‘zähmen’, npers. dam ‘zahmes Tier’', and Klein s.v. 'tame' lists among the cognates of the I.-E. base *domə-, *demə- 'ModPers. dām, ‘a tame animal’'. Wiktionary's *demh₂- article gives the same two-step route (Middle Persian dʾm 'tame animal' → Persian دام 'livestock') with no Avestan link. Semantically the word is the standing antonym of دَد dad 'wild animal' — exactly the pairing in the Ferdowsī line the chart quotes, 'مر او را دَد و دام فرمان برد', and in Borhān's own definition 'دام ... نقیض دد باشد'. The three modern compounds printed beside it, دامداری 'animal husbandry', دامپزشکی 'veterinary medicine' and دامپروری 'stock-breeding', are 20th-century Persian coinages on this دام and are correctly formed.\",\n \"derivation_fa\":\"«دام» در فارسی نو به معنی «جانوران اهلی، چارپایان» دنبالهٔ فارسی میانهٔ dām «جانور اهلی» است (مکنزی، ص ۲۴، ²dām)، و آن از ایرانی باستان *dāma- و در نهایت از *domh₂-o- هندواروپایی «رام‌شده» می‌آید — همان ستاکی که پوکورنی با معنی «جانور اهلی، رام» بازسازی کرده است. آ در سراسر این راه کشیده مانده و هیچ دگرگونی همخوانی رخ نداده، از این‌رو صورت واژه از دورهٔ ساسانی تا امروز دست‌نخورده است. هر دو مأخذی که نورایی می‌آورد همین را می‌گویند: پوکورنی در همان صفحهٔ ۱۹۹ می‌نویسد «اُستی domun ‹رام کردن›، فارسی نو dām ‹جانور اهلی›»، و کلاین ذیل tame در میان هم‌ریشه‌ها «فارسی نو dām ‹جانور اهلی›» را ثبت کرده است. ویکی‌واژه نیز همین دو گام (فارسی میانه ← فارسی نو) را بی هیچ حلقهٔ اوستایی می‌آورد. از نظر معنایی «دام» همواره در برابر «دَد» می‌نشیند — چنانکه در بیت فردوسی («مر او را دَد و دام فرمان برد») و در تعریف خود برهان قاطع («دام ... نقیض دد باشد»). سه ترکیب امروزی «دامداری»، «دامپزشکی» و «دامپروری» ساخته‌های سدهٔ چهاردهم خورشیدی بر همین «دام»اند و درست ساخته شده‌اند. ادعای نورایی در این گره درست است.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/دام\",\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/demh₂-\"],\n \"ref_check\":[\n  {\"ref\":\"KLN:1569\",\"status\":\"supports\",\"note\":\"Klein s.v. 'tame, adj.' (T section, the page Nourai numbers 1569 in the 1966 two-volume edition; KLN_1971.txt lines 240763 ff., running head 'TAME 744' in the one-volume reprint): '...fr. I.-E. base *domə-, *demə-, *dem- whence also OI. damayati, damāyáti, ‘tames’, damya-, ‘a young steer’, prop. ‘an animal that must yet be tamed’, ... ModPers. dām, ‘a tame animal’, Gk. δαμᾶν, ‘to tame, subdue’, ... L. domāre, ‘to tame, subdue’, Ossetic domun...'. Klein's page therefore carries the Persian word under this root, exactly as Nourai draws it.\"},\n  {\"ref\":\"POK:199\",\"status\":\"supports\",\"note\":\"POK_01.txt leaf 207 (printed p.199): 'osset. domun ,zähmen', npers. dam ,zahmes Tier'' — Pokorny himself puts New Persian dām 'tame animal' under demə-, domə-.\"},\n  {\"ref\":\"BQT:817\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 277 (printed p.817): headword 'دام = بروزن رام، نقیض دد باشد که آن وحشی غیر درنده است عموماً و آهو و غزال و ... را گویند خصوصاً'; footnote 1 lists 'هندی باستان damá-, یونانی δαμάλης, لاتینی domāre, اُستی domun'. Borhān/Moʿin support both the sense and the Indo-European affiliation of the Persian word.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"PHD.txt line 306 s.v. ²dām\",\"stance\":\"supports\",\"note\":\"'²dām [dʾm | = M, N ~] tame animal' — MacKenzie attests the Middle Persian ancestor with the same meaning and notes the Manichaean and New Persian continuants ('= M, N ~').\"},\n  {\"src\":\"MON\",\"where\":\"MON_part1.txt (2-vol. abridgement) s.v. دام\",\"stance\":\"partial\",\"note\":\"The abridged Moʿin available locally carries the entry but its bracketed origin tags are lost in the OCR; the full 6-vol. Farhang-e Fārsi is the source of the Borhān footnote quoted above. Recorded as partial because the Latin-script Pahlavi form could not be read in this copy.\"},\n  {\"src\":\"ARY\",\"where\":\"incoming/ARY/ARY_latin_index_pages.txt [pdf page 262], TAME\",\"stance\":\"supports\",\"note\":\"'TAME (ENGLISH) ... DĀM (PAHLAVI)' with the Sanskrit, Greek, Latin, Ossetic and Hittite cognates — Aryanpur too files Persian/Pahlavi dām under this root.\"},\n  {\"src\":\"HRN\",\"where\":\"HRN.txt, Grundriss der neupersischen Etymologie\",\"stance\":\"silent\",\"note\":\"Horn has no numbered entry for دام 'livestock' (his section around no.544 treats ded/dede 'Raubtier'); a grep for dām in the Grundriss returns only the homonym دام 'snare' contexts, so Horn is silent on this word.\"}\n ]\n}\n]\njson.dump(nodes, open(S+'e0n12.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 0 nodes 1-2"
}
```


### [2026-09-05T18:19:11.103Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:20:36.968Z] TOOL CALL #85: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nnodes=[\n{\n \"id\":3,\"lang\":\"Greek\",\"words\":\"daman; a-damas\",\"verdict\":\"plausible\",\n \"derivation\":\"Two words, two verdicts. (a) δαμάω / δάμνημι, aorist ἐδάμασ(σ)α 'to tame, subdue, break in', with δμητός 'tamed' (< *dm̥h₂-tos), δμήτωρ 'tamer', δάμαλις 'heifer', πανδαμάτωρ 'all-subduer', is the regular Greek continuant of the zero-grade *dmh₂- (Pokorny 199-200 lists the whole family; Greek, he notes, has no o-grade forms). This half is confirmed. (b) ἀδάμας, gen. ἀδάμαντος, is attested from Hesiod on for 'the hardest metal, probably steel', then for a hard bright stone and finally for the diamond; the traditional analysis, which Watkins and Klein both give and which Nourai copies, is ἀ- privative + δαμ- = 'unconquerable'. Modern Greek etymology no longer accepts that: Beekes calls the semantics strange and takes ἀδάμας for a Semitic/oriental loan reshaped by folk etymology on δαμάω, comparing Akkadian elmēšu 'a precious stone' — and Wiktionary's Middle Persian entry says the same in the other direction ('usually derived from Byzantine Greek ἀδάμας, but the Greek word itself is now considered an oriental loanword'). So the node's own internal derivation ('a-damas: unconquerable') is the 19th/20th-century handbook view that the current standard reference work rejects; the word itself and its 'hard stone' meaning are correctly given, which is why the node is graded plausible rather than disputed.\",\n \"derivation_fa\":\"در این جعبه دو واژه است و هر یک حکم جداگانه دارد. نخست δαμάω/δάμνημι «رام کردن، مهار کردن»، با δμητός «رام‌شده» (از *dm̥h₂-tos)، δμήτωρ «رام‌کننده»، δάμαλις «گوسالهٔ ماده» و πανδαμάτωρ «همه‌رام‌کن»: این بازماندهٔ منظمِ درجهٔ صفرِ *dmh₂- در یونانی است و پوکورنی (ص ۱۹۹–۲۰۰) همهٔ این خانواده را می‌آورد؛ این نیمه پذیرفتنی و درست است. دوم ἀδάμας (مضاف‌الیه ἀδάμαντος) که از هزیود به بعد به معنی «سخت‌ترین فلز، احتمالاً پولاد» و سپس «سنگ سخت درخشان» و سرانجام «الماس» به کار رفته است. تحلیل سنتی — که واتکینز و کلاین هر دو آورده‌اند و نورایی از آنان گرفته — «ا»ی نفی + δαμ- یعنی «رام‌نشدنی» است. اما ریشه‌شناسی امروزی یونانی این را نمی‌پذیرد: بیکس آن را از نظر معنایی نامعقول می‌داند و ἀδάμας را وام‌واژه‌ای سامی/شرقی می‌شمارد که با ریشه‌شناسی عامیانه به δαμάω پیوند خورده است، و اکدی elmēšu «سنگ گران‌بها» را می‌سنجد. پس خودِ واژه و معنای «سنگ سخت» درست ثبت شده، ولی تحلیل درونی «رام‌نشدنی» را پژوهش امروزی رد می‌کند؛ از این رو حکم این گره «با احتیاط پذیرفتنی» است.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/ἀδάμας\",\"https://en.wiktionary.org/wiki/ʾlmʾs\"],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 364 s.v. demə-²: '3. Zero-grade form *dmə- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND.' Nourai's two Greek words and both glosses are Watkins' words verbatim, so the reference he cites does say exactly what the box says.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 1567, s.v. adamant\",\"stance\":\"supports\",\"note\":\"'adamant, n., a very hard stone ... fr. Gk. ἀδάμας, ‘adamant, the hardest metal, diamond’, lit. ‘unconquerable’, fr. ἀ- (see priv. pref. a-) and the verb δαμᾶν, ‘to tame’. See tame and cp. diamond; cp. also the second element in Hippodamia.' Klein gives the traditional analysis Nourai reproduces.\"},\n  {\"src\":\"POK\",\"where\":\"POK_01.txt leaves 207-208 (pp.199-200)\",\"stance\":\"supports\",\"note\":\"'gr. δάμναμι, ion. -ημι, Aor. ἐδάμασ(σ)α ,bändige', vielfach sekund. umgestaltet, wie δαμνᾷς usw., πανδαμάτωρ ,Allbezwinger', δμητός ,gebändigt' (*dm̥-tos), hom. ἀδμήτος und ἀδμής, -ῆτος ,ungebändigt, unverheiratet''. Pokorny attests the verb and the privative compound type, though ἀδάμας itself is not discussed.\"},\n  {\"src\":\"WEB\",\"where\":\"Wiktionary, Ancient Greek ἀδάμας (archived)\",\"stance\":\"contradicts\",\"note\":\"'Beekes ... remarks that semantically this is strange and the word is rather a Semitic borrowing that was adapted by folk etymology', comparing Akkadian adamu / elmēšu 'a valuable stone' and Middle Persian almās. The current standard Greek etymological dictionary therefore rejects the 'unconquerable' derivation the chart prints.\"}\n ]\n},\n{\n \"id\":4,\"lang\":\"Pahlavi\",\"words\":\"almâs\",\"verdict\":\"confirmed\",\n \"derivation\":\"Middle Persian almās(t) is genuinely attested: MacKenzie, Concise Pahlavi Dictionary p.10, 'almās(t) [ʾlmʾs(t) | (M ʾrmʾs), N almās] steel; diamond' — with a Manichaean Middle Persian variant ʾrmʾs, which proves the word is pre-Islamic and that its initial al- is NOT the Arabic article but part of the borrowed stem. The source is Greek ἀδάμας (accusative ἀδάμαντα), taken into Iranian in the Parthian/Sasanian period, probably through Aramaic-Syriac mediation (Classical Syriac ʾlmsʾ); the Greek nasal-stem was reanalysed as ʾlmʾs(t), the -t of almāst being a secondary Iranian dental. The sense in Pahlavi is the Greek one, 'the hardest metal, steel', which is exactly Nourai's gloss 'hard stone' (the narrowing to 'diamond' is later, see node 5). Asbaghi's Persische Lehnwörter im Arabischen states the chain in full: 'al-mās: “Diamant” ← MP. almāst “the hardest of the metals, possibly steel” borrowed from griech. ἀδάμας » np. almās “diamond”' — i.e. Arabic أَلْماس is a loan from Middle Persian, not the other way round, so this is a Greek → Iranian → Arabic route and not an Arabic-mediated round-trip. The one caveat is the ultimate origin: Wiktionary's Middle Persian entry notes that although the word is 'usually derived from Byzantine Greek ἀδάμας', the Greek word 'itself is now considered an oriental loanword' (cf. Akkadian elmēšu), so the Greek stage may be a way-station rather than the source.\",\n \"derivation_fa\":\"صورت فارسی میانهٔ almās(t) به‌راستی گواه دارد: مکنزی در «فرهنگ کوچک پهلوی» (ص ۱۰) می‌نویسد «almās(t) [ʾlmʾs(t) | (مانوی ʾrmʾs)، فارسی نو almās] پولاد؛ الماس». وجود گونهٔ مانوی ʾrmʾs نشان می‌دهد که واژه پیش از اسلام در ایران بوده و «الـ» آغازین آن حرف تعریف عربی نیست، بلکه بخشی از خودِ ستاکِ وام‌گرفته است. خاستگاه، یونانی ἀδάμας (حالت مفعولی ἀδάμαντα) است که در دورهٔ اشکانی/ساسانی، احتمالاً به میانجی آرامی-سریانی (سریانی ʾlmsʾ)، به ایرانی راه یافته و ستاک نونی یونانی در ایرانی به ʾlmʾs(t) بازتحلیل شده است. معنای پهلوی همان معنای یونانی است، یعنی «سخت‌ترین فلز، پولاد» — دقیقاً همان «سنگ سخت» که نورایی نوشته است. اصباغی در «وام‌واژه‌های فارسی در عربی» همین زنجیره را می‌آورد: «al-mās ‹الماس› از فارسی میانهٔ almāst ‹سخت‌ترین فلزها، شاید پولاد›، وام‌گرفته از یونانی ἀδάμας؛ فارسی نو almās». پس عربی «الماس» خود وام‌واژه‌ای از فارسی میانه است و راهِ واژه یونانی ← ایرانی ← عربی است، نه معرّبی که دوباره به فارسی بازگشته باشد. تنها نکتهٔ باقی‌مانده خاستگاه نهایی است: ویکی‌واژه یادآور می‌شود که خودِ واژهٔ یونانی امروزه وام‌واژه‌ای شرقی شمرده می‌شود (سنجیدنی با اکدی elmēšu).\",\n \"sources\":[\"https://en.wiktionary.org/wiki/ʾlmʾs\",\"https://en.wiktionary.org/wiki/الماس\"],\n \"ref_check\":[\n  {\"ref\":\"BQT:159\",\"status\":\"supports\",\"note\":\"BQT_v1_pages.txt leaf 377 (printed p.159): headword 'الماس؟ - بروزن کربای، گوهریست مشهور - و کنایه از تیغ و شمشیر و کارد و تیر - و آبگینه و مردم جلد و چابک باشد - و بمعنی قلم‌تراش هم هست - و دندان را نیز گویند'; Moʿin's footnote on the same leaf begins '۴ - از یونانی ...' ('from Greek ...'), the Latin-script Greek form being lost in the Persian OCR. The cited page therefore does carry the Greek origin Nourai draws.\"},\n  {\"ref\":\"MON:342\",\"status\":\"partial\",\"note\":\"Only the 2-volume abridgement of Moʿin's Farhang-e Fārsi is on disk (MON_part1.txt line 16385): 'الماس: [origin tag illegible in OCR] (اِ.) (زه.) یکی از سنگ‌های کانی قیمتی که به علت سختی و درخشندگی و کمیابی مقدم بر دیگر سنگ‌های کانی است... درجهٔ سختی‌اش ۱۰ می‌باشد.' The entry exists with the right meaning, but the bracketed origin tag and the Latin-script Pahlavi form of the 6-volume printing (Nourai's vol.1 p.342) are not legible in this copy.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"PHD.txt line 189 / PHD_mackenzie.txt line 980, s.v. almās(t)\",\"stance\":\"supports\",\"note\":\"'almās(t) [ʾlmʾs(t) | (M ʾrmʾs), N almās] steel; diamond' — and the English-Pahlavi index (PHD.txt line 1599) 'diamond almās(t)', line 7663 'steel almās(t), pōlāwad'. Middle Persian attestation is secure.\"},\n  {\"src\":\"PLA\",\"where\":\"incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt lines 2933 and 17783\",\"stance\":\"supports\",\"note\":\"'ʾlmʾs almās: “Diamant” pers. almās < mp. = almās' and, in the main article, 'al-mās: “Diamant” ← MP. almāst “the hardest of the metals, possibly steel” borrowed from griech. ἀδάμας » np. almās “diamond”', with references to Borhān-e Qāṭeʿ, Nyberg vol. II and Addai Scher. Asbaghi confirms both the Greek source and the Middle Persian stage.\"},\n  {\"src\":\"LKT\",\"where\":\"LKT.txt line 354, no. 60 'Ar. almās'\",\"stance\":\"supports\",\"note\":\"'60. Ar. almās: [Aus gr. ἀδάμας] ‘Diamant’, ebenso pers. u. tk.; hieraus russ. almaz, klruss. almaz, halmaz, bulg. serb. almaz ‘dass.’' Lokotsch likewise derives the Arabic and Persian word from Greek ἀδάμας.\"},\n  {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt lines 6339, 6983 (index)\",\"stance\":\"supports\",\"note\":\"Nyberg's Manual of Pahlavi glossary index carries 'almāst: ~' and 'almās: almāst', i.e. the Pahlavi word is registered in the standard Pahlavi glossary as well.\"}\n ]\n}\n]\njson.dump(nodes, open(S+'e0n34.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 0 nodes 3-4"
}
```


### [2026-09-05T18:20:38.753Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:21:56.223Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nnodes=[\n{\n \"id\":5,\"lang\":\"Persian\",\"words\":\"almâs\",\"verdict\":\"confirmed\",\n \"derivation\":\"New Persian الماس almās continues Middle Persian almās(t) unchanged but for the loss of the optional final -t; the shift is purely semantic, from the Pahlavi 'steel, hardest of metals' to the modern 'diamond', a narrowing that had already taken place by the classical period (Borhān-e Qāṭeʿ p.159 still records both poles: 'گوهریست مشهور ... و کنایه از تیغ و شمشیر و کارد و تیر', i.e. 'a famous gem ... and figuratively blade, sword, knife and arrow'). From Persian the word spread outward rather than inward: Arabic أَلْماس / ماس, Classical Syriac ʾlmsʾ, Turkish elmas, Azerbaijani/Tatar almaz, Russian алмаз almáz, Georgian ალმასი almasi, Hindustani almās, Swahili almasi — Wiktionary lists all of these as descendants of Classical Persian almās. Note in particular that the Arabic form is a borrowing FROM Persian (Asbaghi, Lokotsch), so the al- of الماس must not be parsed as the Arabic definite article, even though Arabic speakers later treated it as one (hence the by-form ماس mās).\",\n \"derivation_fa\":\"«الماس» فارسی نو همان almās(t) فارسی میانه است، تنها با افتادن -t پایانیِ اختیاری؛ دگرگونی، دگرگونیِ معنایی است: از «پولاد، سخت‌ترین فلزها» در پهلوی به «الماس» در فارسی نو. این تنگ‌شدن معنا تا دورهٔ کلاسیک انجام گرفته بود، هرچند برهان قاطع (ص ۱۵۹) هنوز هر دو سوی معنا را ثبت کرده است: «گوهریست مشهور ... و کنایه از تیغ و شمشیر و کارد و تیر». از فارسی، واژه به بیرون رفت نه به درون: عربی «الماس/ماس»، سریانی ʾlmsʾ، ترکی elmas، آذربایجانی و تاتاری almaz، روسی алмаз، گرجی ალმასი، اردو almās و سواحلی almasi — ویکی‌واژه همهٔ اینها را بازماندهٔ فارسی کلاسیک almās می‌داند. نکتهٔ مهم آنکه صورت عربی خود وام‌گرفته از فارسی است (اصباغی، لوکوچ)، پس «الـ» در «الماس» حرف تعریف عربی نیست، هرچند بعدها عرب‌زبانان آن را چنین پنداشتند و صورت «ماس» را از آن ساختند. ادعای نورایی در این گره درست است.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/الماس\",\"https://en.wiktionary.org/wiki/ʾlmʾs\"],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"Nourai gives no reference for this node; it is covered by the references of its parent (BQT:159; MON:342), which were checked there.\"}],\n \"consulted\":[\n  {\"src\":\"BQT\",\"where\":\"BQT_v1_pages.txt leaf 377 (printed p.159), s.v. الماس\",\"stance\":\"supports\",\"note\":\"'الماس - بروزن کربای، گوهریست مشهور - و کنایه از تیغ و شمشیر و کارد و تیر - و آبگینه و مردم جلد و چابک باشد - و بمعنی قلم‌تراش هم هست - و دندان را نیز گویند'; Moʿin's footnote: '۴ - از یونانی ...'.\"},\n  {\"src\":\"PHD\",\"where\":\"PHD.txt line 189 s.v. almās(t)\",\"stance\":\"supports\",\"note\":\"MacKenzie's entry ends '| N almās', i.e. New Persian الماس is explicitly given as the continuant of the Pahlavi word.\"},\n  {\"src\":\"WEB\",\"where\":\"Wiktionary, Persian الماس (archived)\",\"stance\":\"supports\",\"note\":\"'From Middle Persian ʾlmʾs (almās); see there for further information', with Arabic أَلْمَاس listed as a borrowing FROM Persian (marked with the → borrowing arrow).\"}\n ]\n},\n{\n \"id\":6,\"lang\":\"Latin\",\"words\":\"adamas, diamas\",\"verdict\":\"confirmed\",\n \"derivation\":\"Latin borrowed the Greek noun whole as adamās, gen. adamantis, m. 'the hardest iron or steel; adamant', already in Ovid and Pliny. The second form Nourai prints, diamās, is Late/Vulgar Latin: a Vulgar Latin *adiamantem arose beside adamantem and was then, in Klein's words, 'a blend of Gk. ἀδάμας, “adamant, diamond”, lit. “unconquerable” and διαφανής, “transparent”'; Etymonline puts it more cautiously — the Vulgar Latin form 'was subsequently altered by influence of the many Greek words in dia-'. Whichever the mechanism, aphaeresis of the first syllable plus the dia- reshaping gives Medieval Latin diamantem, acc. of diamās, which is the immediate ancestor of Old French diamant. So Latin ends up with a doublet: learned adamās (> English adamant) and popular diamās (> French diamant, English diamond). Nourai's box is right to print both, and his gloss 'hard stone' matches the Latin sense.\",\n \"derivation_fa\":\"لاتینی واژهٔ یونانی را یکسره وام گرفت: adamās (مضاف‌الیه adamantis) «سخت‌ترین آهن یا پولاد؛ الماس»، که از اووید و پلینی به بعد گواه دارد. صورت دوم که نورایی آورده، diamās، لاتینی پسین/عامیانه است: در لاتینی عامیانه صورت *adiamantem در کنار adamantem پدید آمد و سپس، به گفتهٔ کلاین، «آمیزه‌ای شد از ἀδάμας یونانی ‹رام‌نشدنی› و διαφανής ‹شفاف›»؛ اتیمانلاین محتاطانه‌تر می‌گوید صورت لاتینی عامیانه «زیر تأثیر واژه‌های پرشمار یونانیِ آغازشونده به dia- دگرگون شد». به هر روی، با افتادن هجای نخست و بازشکل‌گیری با dia-، صورت لاتینی میانهٔ diamantem (حالت مفعولی diamās) به دست آمد که نیای بی‌واسطهٔ diamant فرانسهٔ کهن است. پس در لاتینی دوگانه‌ای پدید آمد: صورت عالمانهٔ adamās (← adamant انگلیسی) و صورت مردمیِ diamās (← diamant فرانسه، diamond انگلیسی). آوردن هر دو صورت در جعبهٔ نورایی درست است و معنای «سنگ سخت» نیز با معنای لاتینی می‌خواند.\",\n \"sources\":[\"https://www.etymonline.com/word/diamond\",\"https://en.wiktionary.org/wiki/ἀδάμας\"],\n \"ref_check\":[\n  {\"ref\":\"AHD:364\",\"status\":\"not_checked\",\"note\":\"The local AHD file is only the Watkins Indo-European appendix (pp.1505-1550 of the New College Edition), not the main dictionary; AHD:364 is the main-dictionary page for the DIAMOND family. The appendix entry demə-² does end '...Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND', which is the same claim.\"},\n  {\"ref\":\"KLN:442\",\"status\":\"supports\",\"note\":\"Klein 1966 s.v. diamond (D section = the page Nourai numbers 442; KLN_1966.txt lines 11255-11256): 'diamond, n. — ME. diamant, diamaunt, fr. OF. diamant, fr. Late L. diamantem, acc. of diamās, which is a blend of Gk. ἀδάμας, “adamant, diamond”, lit. “unconquerable” and διαφανής, “transparent”.' Klein's Late Latin diamās is precisely Nourai's second Latin form.\"}\n ],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 1567 s.v. adamant\",\"stance\":\"supports\",\"note\":\"'ME., “diamond, magnet”, fr. OF. adamant, oblique case, fr. L. adamantem, acc. of adamās (whence the OF. nom. adamas), fr. Gk. ἀδάμας'. Klein documents the learned Latin form as well as the popular one.\"},\n  {\"src\":\"WEB\",\"where\":\"Etymonline s.v. diamond (archived)\",\"stance\":\"supports\",\"note\":\"'mid-14c., from Old French diamant, from Medieval Latin diamantem (nominative diamas), from Vulgar Latin *adiamantem (which was subsequently altered by influence of the many Greek words in dia-), from Latin adamantem (nominative adamans) “the hardest metal,” from Greek adamas (genitive adamantos)'.\"},\n  {\"src\":\"WEB\",\"where\":\"Wiktionary, Ancient Greek ἀδάμας, Descendants (archived)\",\"stance\":\"supports\",\"note\":\"'Latin: adamās → English: adamant; ... Via Vulgar Latin: French diamant/aimant, Spanish imán, Portuguese ímã' — the two Latin outcomes are listed exactly as Nourai's box has them.\"}\n ]\n},\n{\n \"id\":7,\"lang\":\"English\",\"words\":\"diamond\",\"verdict\":\"confirmed\",\n \"derivation\":\"Middle English diamant, diamaunt (mid-14th c.), borrowed from Old French diamant, itself from Medieval Latin diamantem (see node 6). The modern spelling with -ond is a later English development from the -aunt/-ant ending. Etymonline notes the long semantic instability of the whole family — 'the name has thus always been of indefinite and fluctuating sense', having covered a hypothetical hardest substance, a metal, sapphire, the magnet, steel and emery before settling on the gem — which is why the Pahlavi and Latin boxes of this chart can both be glossed 'hard stone' while the English and modern Persian ends both mean 'diamond'. The chain Greek → Latin → Old French → Middle English is uncontroversial and one good source covers it.\",\n \"derivation_fa\":\"«diamond» انگلیسی از انگلیسی میانهٔ diamant/diamaunt (میانهٔ سدهٔ چهاردهم میلادی) است، وام‌گرفته از diamant فرانسهٔ کهن و آن از diamantem لاتینی میانه (نگاه کنید به گرهٔ ۶). املای امروزی با -ond تحولی درون‌انگلیسی از پایانهٔ -aunt/-ant است. اتیمانلاین یادآور می‌شود که معنای این خانواده همواره لغزان بوده است: «نام آن همیشه معنایی نامعین و متغیر داشته» و پیش از آنکه بر گوهر الماس بنشیند، بر مادهٔ فرضیِ سخت، فلز، یاقوت کبود، آهن‌ربا، پولاد و سنباده اطلاق می‌شده است — و همین است که در این نمودار جعبه‌های پهلوی و لاتینی هر دو «سنگ سخت» معنی شده‌اند ولی دو سرِ انگلیسی و فارسی نو هر دو «الماس». زنجیرهٔ یونانی ← لاتینی ← فرانسهٔ کهن ← انگلیسی میانه هیچ اختلافی ندارد. ادعای نورایی درست است.\",\n \"sources\":[\"https://www.etymonline.com/word/diamond\"],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference is given for this node; it is covered by its parent's AHD:364 and KLN:442, checked at node 6.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 11255 s.v. diamond\",\"stance\":\"supports\",\"note\":\"'diamond, n. — ME. diamant, diamaunt, fr. OF. diamant, fr. Late L. diamantem, acc. of diamās...'\"},\n  {\"src\":\"WEB\",\"where\":\"Etymonline s.v. diamond (archived)\",\"stance\":\"supports\",\"note\":\"'mid-14c., from Old French diamant ... the name has thus always been of indefinite and fluctuating sense'.\"}\n ]\n}\n]\njson.dump(nodes, open(S+'e0n567.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 0 nodes 5-7"
}
```


### [2026-09-05T18:21:58.402Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:22:50.505Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nnodes=[\n{\n \"id\":8,\"lang\":\"Germanic\",\"words\":\"tamaz\",\"verdict\":\"confirmed\",\n \"derivation\":\"Proto-Germanic *tamaz 'tame, brought into the home' is the o-grade adjective *domh₂-o- with regular Grimm's-Law d > t and the *o > a merger of Germanic: PIE *domh₂-o-s > PGmc *tamaz. It is continued by Old English tam, Old Norse tamr, Old Saxon/Old Frisian/Middle Dutch tam, Old High German zam (with the High German shift t > z), Gothic showing only the derived verb ga-tamjan 'to tame'. Watkins gives it in exactly these words: 'Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME'. Walde-Pokorny I 789 adds the caveat that it is unclear whether the adjective is a back-formation from the verb (*domeyō > Goth. ga-tamjan, ON temja, OHG zemmen) or an old passive 'that which has been tamed', comparable to Sanskrit dáma-ḥ 'taming'. Nourai's transliteration drops nothing and his gloss 'tame' is Watkins'.\",\n \"derivation_fa\":\"صورت ژرمنی آغازین *tamaz «رام، به خانه آورده‌شده» همان صفتِ درجهٔ o یعنی *domh₂-o- است با دو دگرگونی منظم ژرمنی: د هندواروپایی بر پایهٔ قانون گریم به t بدل شده و o به a. پس *domh₂-o-s ‹ *tamaz. بازماندگان آن‌اند: انگلیسی کهن tam، نورس کهن tamr، ساکسون کهن و فریزی کهن و هلندی میانه tam، آلمانی علیای کهن zam (با جابه‌جایی t ‹ z در آلمانی علیا)؛ در گوتی تنها فعل مشتق ga-tamjan «رام کردن» به جا مانده است. واتکینز دقیقاً همین را می‌گوید: «صورت درجهٔ o با پسوند، *dom-o-، در ژرمنی *tamaz، در انگلیسی کهن tam ‹اهلی›: TAME». والده-پوکورنی (جلد ۱، ص ۷۸۹) می‌افزاید که روشن نیست این صفت ساخت پسین از فعل است یا معنای مفعولیِ کهنِ «رام‌شده» دارد، سنجیدنی با dáma-ḥ سنسکریت. ضبط و معنای نورایی در این گره درست است.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/tamaz\",\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/demh₂-\"],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 364 s.v. demə-²: '1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME.' — Nourai's form and gloss verbatim; the index line 2336 confirms 'TAME demə-²'.\"}],\n \"consulted\":[\n  {\"src\":\"WLD\",\"where\":\"Bd. I p.789 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt lines ~49776-49780)\",\"stance\":\"supports\",\"note\":\"'got. gatamjan, anord. temja, ags. temian, ahd. zemmen „zähmen“ (*domeyō = ai. damayati), ahd. zamōn ds. (= lat. domā-re), anord. tamr, ags. tam, ahd. zam „zahm“ (unklar, ob Rückbildung aus dem Verbum, oder ob die pass. Bed. aus „Zähmung = Gezähmtes“ erwachsen ist...)'.\"},\n  {\"src\":\"POK\",\"where\":\"POK_01.txt leaf 208 (printed p.200)\",\"stance\":\"supports\",\"note\":\"The same Germanic list is repeated by Pokorny: 'anord. tamr, ags. tam, ahd. zam ,zahm''.\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1971.txt lines 240763 ff., s.v. tame, adj.\",\"stance\":\"supports\",\"note\":\"'ME. tame, fr. OE. tam, rel. to ON. tamr, OS., Dan., Swed., OFris., MLG., MDu., Du. tam, OHG., MHG. zam, G. zahm, “tame”. These adjectives prob. derive from an Old Teut. verb attested only in OHG. zamōn, MHG. zamen, “to tame”, fr. I.-E. base *domə-, *demə-, *dem-'.\"}\n ]\n},\n{\n \"id\":9,\"lang\":\"English\",\"words\":\"tame\",\"verdict\":\"confirmed\",\n \"derivation\":\"Old English tam 'domesticated, not wild' > Middle English tame > modern English tame; the noun-to-verb conversion 'to tame' replaced the older Old English causative temian (< PGmc *tamjaną). Nothing irregular happens: OE a before a single consonant lengthens and diphthongises in the Great Vowel Shift, giving modern /teɪm/, and the final -e is orthographic. Skeat states the whole chain and the cognates: 'Tame, adj. (E.) M.E. tam. A.S. tam, tame; whence tamian, temian, to tame. + Du. tam, Icel. tamr, Swed. Dan. tam, G. zahm. Allied to L. domāre, Skt. dam, Gk. δαμάζειν, to tame.' This is the one link in the chart that no one has ever disputed.\",\n \"derivation_fa\":\"«tame» انگلیسی از tam انگلیسی کهن «اهلی، نه‌وحشی» است که به tame انگلیسی میانه و سپس صورت امروزی رسیده؛ فعلِ برگرفته از اسم («to tame») جای فعل سببیِ کهن‌ترِ temian (از ژرمنی *tamjaną) را گرفت. هیچ بی‌قاعدگی در کار نیست: aی انگلیسی کهن پیش از یک همخوان کشیده شد و در «جابه‌جایی بزرگ واکه‌ای» به دوواکه بدل گشت و تلفظ امروزی /teɪm/ را داد؛ -e پایانی تنها املایی است. اسکیت همین زنجیره و هم‌ریشه‌ها را می‌آورد: «Tame صفت (انگلیسی): انگلیسی میانه tam؛ انگلیسی کهن tam ‹اهلی›، که از آن tamian و temian ‹رام کردن›؛ هلندی tam، ایسلندی tamr، سوئدی و دانمارکی tam، آلمانی zahm. هم‌ریشه با domāre لاتینی، dam سنسکریت و δαμάζειν یونانی». این حلقه از نمودار هیچ‌گاه محل اختلاف نبوده است.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/tamaz\"],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference given for this node; the parent's AHD citation (s.v. demə-², ending 'in Old English tam, domesticated: TAME') covers it and was checked at node 8.\"}],\n \"consulted\":[\n  {\"src\":\"SKT\",\"where\":\"SKT.txt line 19122, s.v. Tame\",\"stance\":\"supports\",\"note\":\"'Tame, adj. (E.) M.E. tam. A.S. tam, tame; whence tamian, temian, to tame. + Du. tam, Icel. tamr, Swed. Dan. tam, G. zahm. Allied to L. domāre, Skt. dam, Gk. δαμάζειν, to tame. (√DAM.) See Daunt.'\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1971.txt s.v. tame, adj.\",\"stance\":\"supports\",\"note\":\"'ME. tame, fr. OE. tam' with the full Germanic and Indo-European cognate list including 'ModPers. dām, “a tame animal”' — the same entry that authorises node 2.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt index line 2336\",\"stance\":\"supports\",\"note\":\"'TAME demə-²' — Watkins' word-index files English TAME under this root and no other.\"}\n ]\n}\n]\njson.dump(nodes, open(S+'e0n89.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 0 nodes 8-9"
}
```


### [2026-09-05T18:22:52.423Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:23:46.261Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nd={\n \"entry\":1,\n \"root\":\"Denk\",\n \"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *denḱ- 'to bite' (Pokorny 201 denk- ,beißen'; Walde-Pokorny I 790; Watkins/AHD denk- 'to bite'; LIV² 117 *denḱ-)\",\n \"note\":\"The root box itself is exactly right: Pokorny p.201 heads the entry 'denk- ,beißen'' and Walde-Pokorny I 790 has the same with the query '(*dank-?)'; Watkins gives 'denk-. To bite. ... [Pok. denk- 201.]'. Nourai's page reference is precise and the gloss is the handbook's. The problem is not the root but the left-hand branch. Pokorny's denk- entry on the very page cited contains no word for 'tooth': its Indo-Iranian material is Skt dáśati 'bites' (< *dn̥ḱeti), dáṃṣṭra- 'fang' = Av. tiži-dąstra- 'with sharp fangs'; its Greek is δάκνω, δῆγμα; its Germanic is OHG zangar 'biting, sharp', zanga 'tongs' and *tanhu- 'tough'. The tooth-word is a different formation: PIE *h₃dónts, the old participle of *h₃ed- 'to eat, bite', which Pokorny files at p.287 s.v. ed- and Watkins as a separate entry 'dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) ... [In Pok. ed- 287.]'. So the Avestan box (node 1) is hung on the wrong root; everything below it — the Persian, the Sogdian — is correct in itself, and the Germanic branch (nodes 4-5) is genuine *denḱ- material taken verbatim from Watkins. The chart is thus a valid *denḱ- tree with a *h₃dent- tree grafted onto it, the graft being the pre-laryngeal 19th-century view that 'tooth' is simply 'the biter'.\",\n \"note_fa\":\"جعبهٔ ریشه به‌خودی‌خود کاملاً درست است: پوکورنی در صفحهٔ ۲۰۱ مدخل را «denk- ‹گاز گرفتن›» عنوان کرده و والده-پوکورنی (جلد ۱، ص ۷۹۰) نیز همان را با پرسشِ «(*dank-؟)» آورده است؛ واتکینز هم می‌نویسد «denk-. گاز گرفتن ... [پوکورنی denk- 201]». پس ارجاع صفحهٔ نورایی دقیق و معنا همان معنای کتاب‌های مرجع است. مشکل در ریشه نیست، در شاخهٔ چپ است. مدخل denk- در همان صفحه‌ای که نورایی ارجاع می‌دهد هیچ واژه‌ای به معنی «دندان» ندارد: مواد هندوایرانی‌اش dáśati سنسکریت «می‌گزد» و dáṃṣṭra- «دندان نیش» برابر با tiži-dąstra- اوستایی است؛ یونانی‌اش δάκνω و ژرمنی‌اش zangar، zanga و *tanhu-. واژهٔ «دندان» ساختی دیگر است: *h₃dónts هندواروپایی، اسم فاعلِ کهنِ ریشهٔ *h₃ed- «خوردن، گاز گرفتن»، که پوکورنی آن را در صفحهٔ ۲۸۷ ذیل ed- آورده و واتکینز نیز مدخل جداگانه‌ای به آن داده است: «dent-. دندان. (در اصل اسم فاعل ed- در معنای کهن‌تر ‹گاز گرفتن›) ... [در پوکورنی ذیل ed- 287]». پس جعبهٔ اوستایی (گرهٔ ۱) بر ریشهٔ نادرست آویخته شده است؛ آنچه زیر آن است — فارسی و سغدی — به‌خودی‌خود درست است، و شاخهٔ ژرمنی (گره‌های ۴ و ۵) مواد اصیل *denḱ- است که واژه‌به‌واژه از واتکینز گرفته شده. به سخن دیگر، این نمودار درختِ درستِ *denḱ- است که درختِ *h₃dent- بر آن پیوند زده شده، و این پیوند بازماندهٔ دیدگاه سدهٔ نوزدهمی (پیش از نظریهٔ حنجری‌ها) است که «دندان» را همان «گازگیرنده» می‌دانست.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/دندان\",\"https://www.etymonline.com/word/tough\"],\n \"ref_check\":[{\"ref\":\"POK:201\",\"status\":\"supports\",\"note\":\"POK_01.txt leaf 209 (printed p.201): 'denk- ,beißen'. Ai. dáśati ,beißt' (*dn̥ḱeti), Perf. dadáṃśa ..., dáṃṣṭra-ḥ, dáṃṣṭrā ,Spitzzahn, Fangzahn' = av. tiži-dąstra- ,mit scharfem Gebiß, Gezähn' (für -dąstra- s. Bartholomae Airan. Wb. 653); gr. δάκνω ,beiße' (*dn̥k-nō) ...; ahd. zangar ,beißend, scharf' ...; anord. tǫng, ags. tang, tange, ahd. zanga ,Zange' (*donḱā), d.i. ,die zusammenbeißende'; ... daneben im gramm. Wechsel germ. *tanhu- ,fest anliegend, anhängend, zähe' in ags. tōh ,zähe''. The page is exactly Nourai's root and Germanic branch — but contains no 'tooth'.\"}],\n \"consulted\":[\n  {\"src\":\"WLD\",\"where\":\"Bd. I p.790 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt lines 49837 ff.)\",\"stance\":\"supports\",\"note\":\"'denk- „beißen“ (*dank-?). Ai. dáśati „beißt“ (*dn̥ḱeti) ... dáṃṣṭra-ḥ, dáṃṣṭrā „Spitzzahn, Fangzahn“ = av. tiži-dąstra- „mit scharfem Gebiß, Gezähn“ (für -dąstra-, s. Bartholomae Airan. Wb. 653); gr. δάκνω „beiße“ ...; ahd. zangar „beißend, scharf“ ... germ. *tanhu- „fest anliegend, anhängend, zähe“ in ags. tōh „zähe“.' Pokorny 201 is a reprint of this page; note Walde-Pokorny's own '(*dank-?)' query about the vocalism.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt line 364, s.vv. denk- and dent-\",\"stance\":\"partial\",\"note\":\"'denk-. To bite. 1. Germanic *tanhuz in Old English tōh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting ... TANG¹. 4. Germanic *teng- in Old High German zinko, spike, prong: ZINC. [Pok. denk- 201.]' — but immediately after it Watkins gives a SEPARATE entry: 'dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) ... [In Pok. ed- 287.]'. Watkins supports Nourai's Germanic branch and contradicts his Avestan one.\"},\n  {\"src\":\"IEC\",\"where\":\"IEC.txt, grep for denk-/donk-\",\"stance\":\"silent\",\"note\":\"Mann's Indo-European Comparative Dictionary has no headword for this root in the local text (searches for denk-, donko-, dn̥k- return nothing), so he cannot be brought to bear either way.\"},\n  {\"src\":\"SYN\",\"where\":\"SYN.txt leaf 171 (printed p.138), concept 3.11 ANIMAL, and leaf ~264 (p.231), concept 4.27 TOOTH\",\"stance\":\"partial\",\"note\":\"Buck treats the two families in two different concept articles: p.138 'Av. daitika- “wild animal”, deriv. of *dant- “tooth”. Barth. 678.' and p.231 (4.27 TOOTH) 'Skt. dant-, Av. dātā-, dantan-', where the tooth-word is grouped with Lat. dēns, Gk. odous, Goth. tunthus and NOT with any biting root.\"}\n ]\n}\njson.dump(d, open(S+'e1head.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 1 header"
}
```


### [2026-09-05T18:23:47.862Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:24:50.996Z] TOOL CALL #89: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nnodes=[\n{\n \"id\":1,\"lang\":\"Avestan\",\"words\":\"danta; daitika\",\"verdict\":\"disputed\",\n \"derivation\":\"Both Avestan words are real and correctly glossed, but the arrow from 'Denk: to bite' is wrong for the first and only indirectly right for the second. (a) dantan- m. 'Zahn' is in Bartholomae col. 684 ('j. dantan- m. “Zahn” ... ai. vgl. dánt- m.'), beside the Younger Avestan by-form dātā- f. 'Zahn' (col. 678, with the Pahlavi gloss 'dandān') and the compounds vī-mitō.dantan- 'with misshapen teeth' and tiži-daṇtā 'with sharp teeth'. Nourai's transliteration 'danta' is the nominative singular dantā (Moʿin, Borhān p.884 n.5, spells it out: 'حالت مفرد فاعلی اوستا dantā'). But this word is PIE *h₃dónts, gen. *h₃dn̥tés, the fossilised participle of *h₃ed- 'to eat/bite': Pokorny files it at p.287 under ed-, Watkins as a separate root dent- '[In Pok. ed- 287]', Buck under 4.27 TOOTH with Lat. dēns and Gk. odoús, and Wiktionary derives Persian دندان through 'Old Persian dantā, Proto-Iranian *Hdántā, from Proto-Indo-European *h₃dént-ō ~ *h₃dn̥t-nés'. Pokorny's p.201, the page Nourai cites, contains nothing of the kind. (b) daitika- m. is genuine and means exactly what the chart says: Bartholomae col. 677-678 'daitika- m. “wildes, nichtdomestiziertes Tier”', attested in Yasna 39.2 and Yašt 13.74 in the fixed pair pasukanąm ... daitikanąm 'of the tame and of the wild animals'. Bartholomae derives it 'Ableit. aus *danti- m. “Zahn”, s. dantan-, bedeutet also zunächst nur “reissendes Tier”', and Buck p.138 repeats him verbatim. So Nourai's parenthetical gloss 'wild (biting) animals' is Bartholomae's own reasoning — but it reaches 'bite' through the tooth-word, not through *denḱ-. Verdict: the words and glosses are right, the parent link is not.\",\n \"derivation_fa\":\"هر دو واژهٔ اوستایی اصیل‌اند و معناشان درست ثبت شده، اما پیکانی که از ریشهٔ «Denk: گاز گرفتن» به آنها کشیده شده برای اولی نادرست است و برای دومی تنها با یک واسطه درست. نخست dantan- «دندان» که بارتولومه در ستون ۶۸۴ آورده است، در کنار گونهٔ اوستای نو dātā- «دندان» (ستون ۶۷۸، با برگردان پهلوی dandān) و ترکیب‌های vī-mitō.dantan- «کج‌دندان» و tiži-daṇtā «تیزدندان». ضبط نورایی («danta») همان حالت فاعلی مفرد dantā است، چنانکه معین در حاشیهٔ برهان (ص ۸۸۴، پانویس ۵) به‌صراحت می‌نویسد «حالت مفرد فاعلی اوستا dantā». ولی این واژه بازماندهٔ *h₃dónts هندواروپایی است، یعنی اسم فاعلِ سنگ‌واره‌شدهٔ ریشهٔ *h₃ed- «خوردن، گاز گرفتن»: پوکورنی آن را در صفحهٔ ۲۸۷ ذیل ed- آورده، واتکینز مدخل جداگانهٔ dent- را با یادداشت «[در پوکورنی ذیل ed- 287]»، باک ذیل مفهوم ۴٫۲۷ «دندان» در کنار dēns لاتینی و ὀδούς یونانی، و ویکی‌واژه «دندان» فارسی را از راه «پارسی باستان dantā، ایرانی آغازین *Hdántā، هندواروپایی *h₃dént-ō» می‌گیرد. در صفحهٔ ۲۰۱ پوکورنی که نورایی ارجاع می‌دهد هیچ نشانی از واژهٔ «دندان» نیست. دوم daitika- که واقعی است و دقیقاً همان معنایی را دارد که در نمودار آمده: بارتولومه (ستون‌های ۶۷۷–۶۷۸) «daitika- مذکر: جانور وحشیِ اهلی‌نشده»، گواه در یسنا ۳۹٫۲ و یشت ۱۳٫۷۴ در جفتِ ثابتِ pasukanąm ... daitikanąm «از جانوران اهلی و از جانوران وحشی». بارتولومه آن را «مشتق از *danti- ‹دندان›، نگاه کنید به dantan-، پس در اصل تنها به معنی ‹جانور درنده›» می‌داند و باک (ص ۱۳۸) همین را عیناً تکرار می‌کند. پس توضیح داخل پرانتزِ نورایی («جانوران وحشیِ گازگیرنده») همان استدلال بارتولومه است — اما از راه واژهٔ «دندان» به «گاز» می‌رسد، نه از راه *denḱ-. حکم: واژه‌ها و معناها درست‌اند، پیوند با ریشهٔ بالادست نادرست است.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/دندان\",\"https://en.wiktionary.org/wiki/دد\"],\n \"ref_check\":[\n  {\"ref\":\"POK:201\",\"status\":\"contradicts\",\"note\":\"POK_01.txt leaf 209 (printed p.201) s.v. denk- lists only dáśati, dáṃṣṭra-/av. tiži-dąstra-, gr. δάκνω, ahd. zangar/zanga, germ. *tanhu-. No dantan-, no daitika-. Pokorny puts the tooth-word at p.287 under 'ed-' instead, and even remarks at the end of denk-: 'vielleicht ursprünglich verschieden von der Wz. *dek- ,zerreißen'', without ever bringing in 'Zahn'.\"},\n  {\"ref\":\"BQT:884\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 344 (printed p.884, the دند entry), footnote 5: 'در اوستا و پارسی باستان *dantan-، حالت مفرد فاعلی اوستا dantā، پارسی باستان *dantā، فارسی دند (دندان، دنده). حالت مفرد مفعولی dantānam ‹ فارسی دندان (سن). در اوستا حالت جمع فاعلی dantānō. «هوبشمان»'. Moʿin's page carries the Avestan form Nourai prints, with the case forms.\"},\n  {\"ref\":\"SYN:138\",\"status\":\"supports\",\"note\":\"SYN.txt leaf 171 (printed p.138), the last line of concept 3.11 ANIMAL: 'Av. daitika- “wild animal”, deriv. of *dant- “tooth”. Barth. 678.' This is literally Nourai's second word, its gloss, and his '(biting)' parenthesis — and it also shows that the correct Bartholomae column is 678, not the 653 he cites at the next node.\"}\n ],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"BRT.txt leaf 379 (cols. 677-678) s.v. daitika-, and col. 684 s.v. dantan-\",\"stance\":\"supports\",\"note\":\"'j., g. daitika- m. “wildes, nichtdomestizirtes Tier”: pasukanąmcā .. daitikanąmcā aiδyūnąm urunō Y.39.2; zit. Yt.13.154 ... Ableit. aus *danti- m. “Zahn”, s. dantan-, bedeutet also zunächst nur “reissendes Tier”; vgl. ai. vyāghrám daṃṣṭ-ātām ... ferner daṃṣṭrin- und j. tiži.dąstra-. — mp. dat, np. dad, dada “wildes Tier”.' And col.684: 'j. dantan- m. “Zahn” ... ai. vgl. dánt- m.'\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt line 364, s.v. dent-\",\"stance\":\"contradicts\",\"note\":\"'dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English tōth, tooth: TOOTH. ... 3. Full-grade form *dent- in Latin dēns (stem dent-), tooth ... [In Pok. ed- 287.]' — Watkins keeps 'tooth' and denk- 'to bite' rigorously apart, and files the tooth-word under a different Pokorny page.\"},\n  {\"src\":\"ARY\",\"where\":\"incoming/ARY/ARY_latin_index_pages.txt, index heading TOOTH\",\"stance\":\"supports\",\"note\":\"Aryanpur's index prints under 'TOOTH (ENGLISH)': 'DANTA, DANTAN (AVESTAN); DANTAN (OLD PERSIAN); DAD, DANDAN (PAHLAVI); DANDAG (OSSETIC); DĪDĀN, DINDĀN (KURDISH); DANTAN, DĀTAN (BALUCHI); DANT-, DANTAM, DATAS, DANTA (SANSKRIT)' — the Persian tradition likewise groups dad with the tooth-word, exactly as Nourai does.\"},\n  {\"src\":\"WEB\",\"where\":\"Wiktionary, Persian دندان (archived)\",\"stance\":\"contradicts\",\"note\":\"'from Middle Persian dndʾn (dandān), from Old Persian dantā, from Proto-Iranian *Hdántā, from Proto-Indo-Iranian *Hdántā, from Proto-Indo-European *h₃dént-ō ~ *h₃dn̥t-nés' — the root is *h₃dent-, not *denḱ-.\"}\n ]\n}\n]\njson.dump(nodes, open(S+'e1n1.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 1 node 1"
}
```


### [2026-09-05T18:24:53.089Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:25:56.246Z] TOOL CALL #90: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nnodes=[\n{\n \"id\":2,\"lang\":\"Persian\",\"words\":\"dandân; dandeh; dad\",\"verdict\":\"confirmed\",\n \"derivation\":\"All three Persian words descend from the Avestan box as drawn, and Moʿin's footnotes on the page Nourai cites spell out the morphology. (a) دندان dandān 'tooth': the Old Iranian n-stem *dantan- had a nominative dantā and an accusative dantānam; Persian generalised the accusative, so 'حالت مفرد مفعولی dantānam ‹ فارسی دندان' (Borhān p.884 n.5, citing Hübschmann). Middle Persian dandān [dnd'n'] is attested (MacKenzie p.24; Horn, Grundriss no.574, 'dendān “Zahn” ... aw. vīmitō.dantan-; phlv. dandān (AV., Bund.)'); the Avestan ā of the second syllable is preserved and the geminate is simplified. (b) دنده dandeh 'rib': Persian preserves the bare stem in دند dand, whose primary Borhān gloss is 'استخوان پهلو' ('rib bone'), and Moʿin derives it from the nominative — 'حالت مفرد فاعلی اوستا dantā ... فارسی دند (دندان، دنده)'. دنده is that stem with the Middle Persian diminutive/adjectival -ag (> NP -a), i.e. MP *dandag 'little tooth, tooth-like thing' > 'rib', the same image as English 'tine/prong' for a projecting bone; Wiktionary gives 'from Middle Persian *dandak, from دند (dand, “tooth”) + ـه'. (c) دَد dad 'wild animal': Avestan daitika- > Middle Persian dad [dt'] (MacKenzie p.24 'dad [dt' | M dd, N ~] wild animal'; Nyberg II s.v. dat 'wild animal 97.25, 98.4 — Av. (678) daitika-; NP dad(ah)'), whence NP دَد, with regular loss of the intervocalic -k- suffix and of the Avestan -i-. Horn's no.544 (p.120), the page Nourai cites, records the same equation but adds a warning: 'ded, dede “Raubtier, wildes Tier”. aw. daitika- wildes Tier (Geldner, KZ. 28, 400; aber sehr zweifelhaft, vergl. Baunack, Studien I, 385 folg.); phlv. datīk (Ys. 39,2), datak (AV.), dat (Mēn.)' — Horn doubted it in 1893, but Bartholomae (1904), Nyberg and MacKenzie all accept it, and the Sogdian evidence (node 3) settles it. The Molavī couplet Nourai quotes, 'هیچ کنجی بی دد و بی دام نیست', shows the dad/dām antonymy that runs through both charts on this page.\",\n \"derivation_fa\":\"هر سه واژهٔ فارسی همان‌گونه که در نمودار آمده از جعبهٔ اوستایی می‌آیند، و پانویس‌های معین در همان صفحه‌ای که نورایی ارجاع می‌دهد ساختِ صرفی آنها را روشن می‌کند. نخست «دندان»: ستاکِ نونیِ ایرانی باستان *dantan- در حالت فاعلی dantā و در حالت مفعولی dantānam بوده، و فارسی صورت مفعولی را تعمیم داده است: «حالت مفرد مفعولی dantānam ‹ فارسی دندان» (برهان قاطع، ص ۸۸۴، پانویس ۵، به نقل از هوبشمان). صورت فارسی میانهٔ dandān گواه دارد (مکنزی ص ۲۴؛ هرن، «بنیاد ریشه‌شناسی فارسی نو»، شمارهٔ ۵۷۴: «dendān ‹دندان› ... اوستایی vīmitō.dantan-؛ پهلوی dandān»). دوم «دنده»: ستاک برهنه در فارسی به صورت «دند» مانده که معنای نخست آن در برهان قاطع «استخوان پهلو» است، و معین آن را از حالت فاعلی می‌گیرد: «حالت مفرد فاعلی اوستا dantā ... فارسی دند (دندان، دنده)». «دنده» همان ستاک است با پسوند -ag فارسی میانه (‹ -هٔ فارسی نو)، یعنی *dandag «دندانک، چیز دندان‌مانند» ‹ «دنده»؛ ویکی‌واژه نیز می‌نویسد «از فارسی میانهٔ *dandak، از دند ‹دندان› + ـه». سوم «دَد»: اوستایی daitika- ‹ فارسی میانهٔ dad (مکنزی: «dad ‹جانور وحشی›»؛ نیبرگ، جلد ۲، ذیل dat: «جانور وحشی ... اوستایی (۶۷۸) daitika-؛ فارسی نو dad(ah)») ‹ «دَد» فارسی نو، با افتادن منظمِ پسوند -k- میان‌واکه‌ای و -i- اوستایی. هرن در شمارهٔ ۵۴۴ (ص ۱۲۰) — همان صفحه‌ای که نورایی ارجاع می‌دهد — همین برابری را ثبت کرده اما هشدار داده است: «اوستایی daitika- ‹جانور وحشی› (گلدنر؛ ولی بسیار مشکوک، بنگرید به باوناک)»؛ با این همه بارتولومه (۱۹۰۴)، نیبرگ و مکنزی همه آن را پذیرفته‌اند و گواه سغدی (گرهٔ ۳) پرونده را می‌بندد. بیت مولوی که نورایی آورده («هیچ کنجی بی دد و بی دام نیست») همان تقابل «دد/دام» را نشان می‌دهد که در هر دو نمودار این صفحه جاری است.\",\n \"sources\":[\"https://en.wiktionary.org/wiki/دندان\",\"https://en.wiktionary.org/wiki/دنده\",\"https://en.wiktionary.org/wiki/دد\"],\n \"ref_check\":[\n  {\"ref\":\"BQT:884\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 344 (printed p.884; offset confirmed by the دام entry at leaf 277 = Nourai's BQT:817). Headword 'دند = بفتح اول بروزن چند، استخوان پهلو باشد'; footnote 5: 'در اوستا و پارسی باستان *dantan-، حالت مفرد فاعلی اوستا dantā، پارسی باستان *dantā، فارسی دند (دندان، دنده). حالت مفرد مفعولی dantānam ‹ فارسی دندان (سن). در اوستا حالت جمع فاعلی dantānō. «هوبشمان»'; footnote 6: 'پهلوی dandān «تاوادیا»، هندی باستان dánta-، کردی danān, اُستی dændag, بلوچی ..., منجی ..., شغنی ..., سریکلی ..., وخی ...'. This page authorises dandān and dandeh precisely.\"},\n  {\"ref\":\"BRT:653\",\"status\":\"supports\",\"note\":\"BRT.txt leaf 379, which carries the running column numeral 654, i.e. cols. 653-654, s.v. tiži.dąstra-: 'j. tiži.dąstra- Adj. “mit scharfem Gebiss, Gezähn”: varəžahe .. °rahe Yt.14.15. ... *dąstra- statt *dąstra- wohl in Anlehnung an einen KS. *dąš “scharfzähnig” aus *dąnt- (ai. tīkṣṇa-dan), vgl. dantan- und tiži.daṇtā; daitika-. — Npers.: tīž dandān.' Column 653 is exactly the column Pokorny sends the reader to on p.201, and Bartholomae there cross-links dantan-, daitika- and New Persian dandān — the whole of Nourai's node in one entry.\"},\n  {\"ref\":\"HRN:120\",\"status\":\"partial\",\"note\":\"HRN.txt leaf 141 (printed p.120), no.544: 'ded, dede “Raubtier, wildes Tier”. aw. daitika- wildes Tier (Geldner, KZ. 28, 400; aber sehr zweifelhaft, vergl. Baunack, Studien I, 385 folg.); phlv. datīk (ys. 39, 2 (4)), datak (AV.), dat (Mēn.).' The cited page supports the dad ← daitika- link but flags it 'sehr zweifelhaft'; it says nothing about dandān or dandeh, which Horn treats at no.574 (p.126).\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"PHD.txt lines 306-308, s.vv. dad, dandān, dād\",\"stance\":\"supports\",\"note\":\"'dad [dt' | M dd, N ~] wild animal'; 'dandān [KKA < A kk'; dnd'n' | = M, N ~] tooth'; '³dād [d't'] tooth' (the Pahlavi reflex of Av. dātā-). All three Middle Persian links of Nourai's chain are in MacKenzie.\"},\n  {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt line 1226, s.v. dat\",\"stance\":\"supports\",\"note\":\"'dat [dt'] wild animal 97²⁵, 98⁴, — Av. (678) daitika-; NP dad(ah).' Nyberg gives the same route and, like Buck, cites Bartholomae column 678.\"},\n  {\"src\":\"HRN\",\"where\":\"HRN.txt leaf 147 (printed p.126), no.574\",\"stance\":\"supports\",\"note\":\"'574. dendān “Zahn”, dendāne “Mauerzinne”. aw. vīmitō.dantan-; phlv. dandān (AV., Bund.); ... šugni dendān, sar. dandān, waxi dundāk.' Horn's own entry for the tooth-word — the page Nourai should have cited alongside p.120.\"},\n  {\"src\":\"WEB\",\"where\":\"Wiktionary, Persian دنده (archived)\",\"stance\":\"supports\",\"note\":\"'From Middle Persian *dandak, from دند (dand, “tooth”) + ـه (-e)', meanings 'rib' and 'gear, gearstick' — Nourai's 'dandeh: rib' with the tooth etymology confirmed.\"}\n ]\n}\n]\njson.dump(nodes, open(S+'e1n2.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 1 node 2"
}
```


### [2026-09-05T18:25:58.221Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:27:12.065Z] TOOL CALL #91: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nnodes=[\n{\n \"id\":3,\"lang\":\"Sogdian\",\"words\":\"dt\",\"verdict\":\"confirmed\",\n \"derivation\":\"Sogdian δt- (transliterated 'dt' by Nourai, who does not mark the fricative) is the Sogdian cognate of Persian دَد and the direct continuant of the Avestan word. Gharib's Sogdian–Persian–English Dictionary p.145, entry 3668, reads 'δt- B, M | δatu ©Av. daitaka ©nom. acc. nt. -w; pl. -yst ⇒ δtyst | wild animal | VJ 313, 949, 968; TSP; BBB 512; GMS 1169, 1172; δttwʾ TSP 9.45', and entry 3672 gives the plural 'δtyst B, S | δatīst (δδtystt, δtyst) | wild animals'. The forms are attested in Buddhist (Vessantara Jātaka) and Manichaean (BBB) texts of the 8th-10th centuries. Phonologically the initial δ- is regular: Sogdian spirantised Old Iranian initial voiced stops (*d- > δ-, *b- > β-, *g- > γ-), so Old Iranian *daitika- > Sogdian δatu (nom.-acc. neuter in -w). The gloss 'wild (biting) animal' is Nourai carrying over Bartholomae's 'reissendes Tier' etymology; the 'wild animal' half is exactly Gharib's. This node independently confirms the Iranian antiquity of the daitika- word and thereby answers Horn's 1893 doubt (see node 2).\",\n \"derivation_fa\":\"صورت سغدی δt- (که نورایی بدون نشانهٔ سایشی «dt» نوشته است) هم‌ریشهٔ «دَد» فارسی و بازماندهٔ مستقیم واژهٔ اوستایی است. بدرالزمان قریب در «فرهنگ سغدی» (ص ۱۴۵، مدخل ۳۶۶۸) می‌نویسد: «δt- بودایی، مانوی | δatu ‹ اوستایی daitaka | حالت فاعلی-مفعولی خنثی -w؛ جمع -yst ⇒ δtyst | جانور وحشی | VJ 313, 949, 968؛ TSP؛ BBB 512؛ GMS 1169, 1172»، و در مدخل ۳۶۷۲ جمع آن را می‌آورد: «δtyst | δatīst | جانوران وحشی». این صورت‌ها در متون بودایی (جاتکهٔ وسنتره) و مانوی سده‌های هشتم تا دهم میلادی گواه دارند. از نظر آوایی، δ- آغازین کاملاً منظم است: در سغدی همخوان‌های انسدادی واکدارِ آغازینِ ایرانی باستان سایشی شده‌اند (*d- ‹ δ-، *b- ‹ β-، *g- ‹ γ-)، پس *daitika- ایرانی باستان در سغدی δatu شده است. توضیح «گازگیرنده» در معنای نورایی برگرفته از ریشه‌شناسی بارتولومه است؛ «جانور وحشی» عیناً معنای قریب است. این گره به‌تنهایی قدمت ایرانیِ واژهٔ daitika- را تأیید می‌کند و بدین‌سان به تردید هرن (۱۸۹۳) پاسخ می‌دهد (نگاه کنید به گرهٔ ۲).\",\n \"sources\":[\"https://en.wiktionary.org/wiki/دد\"],\n \"ref_check\":[{\"ref\":\"SOD:145\",\"status\":\"supports\",\"note\":\"SOD_pages.txt, the leaf whose running numeral is 145, entry 3668: 'δt- B, M | δatu ©Av. daitaka ©nom. acc. nt. -w; pl. -yst ⇒δtyst | wild animal | VJ 313, 949, 968; TSP; BBB 512; GMS 1169, 1172; δttwʾ TSP 9.45'. Nourai's SOD:145 is a PAGE number (not an entry number) and it is exact; the entry even gives the Avestan etymon Nourai draws the arrow from.\"}],\n \"consulted\":[\n  {\"src\":\"SOD\",\"where\":\"SOD_pages.txt, entry 3672 (same page) and the English index\",\"stance\":\"supports\",\"note\":\"'3672 δtyst B, S | δatīst (δδtystt, δtyst) ©pl. of -ry ⇒*δt- | wild animals | BBB p61, 512; GMS 1186; Frag. Len. 120, 5; MSP b32, 101 e10'; the English index at the back reads 'wild animal 3668 / wild animals 3672'.\"},\n  {\"src\":\"BRT\",\"where\":\"BRT.txt leaf 379 (cols. 677-678) s.v. daitika-\",\"stance\":\"supports\",\"note\":\"'Ableit. aus *danti- m. “Zahn” ... — mp. dat, np. dad, dada “wildes Tier”.' Bartholomae gives the Middle and New Persian continuants; Gharib supplies the Sogdian one, so the word is attested across the eastern and western branches.\"},\n  {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt line 1226 s.v. dat\",\"stance\":\"supports\",\"note\":\"'dat [dt'] wild animal ... Av. (678) daitika-; NP dad(ah)' — the Middle Persian form dat is spelled dtʾ, the same consonantal skeleton as the Sogdian δt, which is why Nourai's chart can print 'dt' for both traditions.\"}\n ]\n},\n{\n \"id\":4,\"lang\":\"Germanic\",\"words\":\"tangus; tanhuz; teng\",\"verdict\":\"confirmed\",\n \"derivation\":\"This box is Watkins' denk- entry copied out. (a) *tanguz (Nourai prints 'tangus', devoicing the reconstructed Germanic nominative ending -z) 'tongs, pincers' < PIE *donḱ-u-: Pokorny 201 'anord. tǫng (Gen. tengr und tangar), ags. tang, tange, ahd. zanga ,Zange' (*donḱā), d. i. ,die zusammenbeißende'', and Klein s.v. tongs says the same, 'lit. “that which bites” (cp. OHG. zangar, “biting, sharp”), fr. I.-E. base *denk-, “to bite”'. The instrument is named 'the biter'. (b) *tanhuz 'holding fast, tenacious' < *denḱ- with Verner's-Law grammatical alternation (Pokorny: 'daneben im grammatischen Wechsel germ. *tanhu- ,fest anliegend, anhängend, zähe' in ags. tōh ,zähe''); Nourai's gloss 'holding tight' is Watkins' '(< “holding fast”)'. (c) *teng- is not a free word but Watkins' stem label for the e-grade: 'Germanic *teng- in Old High German zinko, spike, prong: ZINC'; Nourai's gloss 'spiky' renders 'spike, prong'. The chart is faithful to its source; the only cosmetic slips are the -s for -z in tangus and the citation of a bare stem as if it were a word.\",\n \"derivation_fa\":\"این جعبه رونویسیِ مدخل denk- واتکینز است. نخست *tanguz (که نورایی «tangus» نوشته و -z پایانیِ حالت فاعلیِ بازسازی‌شدهٔ ژرمنی را بی‌واک آورده) به معنی «انبر، گازانبر»، از *donḱ-u- هندواروپایی: پوکورنی در ص ۲۰۱ می‌نویسد «نورس کهن tǫng، انگلیسی کهن tang/tange، آلمانی علیای کهن zanga ‹انبر› (*donḱā)، یعنی ‹آنکه به هم می‌گزد›»، و کلاین نیز ذیل tongs همین را می‌گوید: «تحت‌اللفظ ‹آنچه گاز می‌گیرد› (بسنجید با zangar آلمانی علیای کهن ‹گازگیرنده، تیز›)، از ریشهٔ هندواروپایی *denk- ‹گاز گرفتن›». یعنی این ابزار «گازگیرنده» نامیده شده است. دوم *tanhuz «سخت‌چسبنده، سرسخت»، از همان ریشه با تناوب دستوریِ قانون ورنر (پوکورنی: «در کنار آن با تناوب دستوری، ژرمنی *tanhu- ‹سخت چسبیده، چسبنده، سفت›، در انگلیسی کهن tōh ‹سفت›»)؛ معنای «holding tight» در نمودار همان «(‹ holding fast)» واتکینز است. سوم *teng- که واژهٔ آزاد نیست بلکه برچسبِ ستاکِ درجهٔ e نزد واتکینز است: «ژرمنی *teng- در zinko آلمانی علیای کهن ‹میخ، دندانه›: ZINC»؛ «spiky» در نمودار برگردان «spike, prong» است. نمودار به مأخذش وفادار است؛ تنها دو لغزش صوری دارد: -s به‌جای -z در tangus، و آوردن یک ستاکِ برهنه در جایگاه واژه.\",\n \"sources\":[\"https://www.etymonline.com/word/tough\",\"https://www.etymonline.com/word/zinc\"],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 364 s.v. denk-: '1. Germanic *tanhuz in Old English tōh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting ... TANG¹. 4. Germanic *teng- in Old High German zinko, spike, prong: ZINC. [Pok. denk- 201.]' All three of Nourai's forms and all three glosses are here.\"}],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"POK_01.txt leaf 209 (printed p.201)\",\"stance\":\"supports\",\"note\":\"'ahd. zangar ,beißend, scharf', mnd. tanger ,ds., bissig, kräftig, frisch'; anord. tǫng (Gen. tengr und tangar), ags. tang, tange, ahd. zanga ,Zange' (*donḱā), d. i. ,die zusammenbeißende' ... daneben im gramm. Wechsel germ. *tanhu- ,fest anliegend, anhängend, zähe' in ags. tōh ,zähe'; mnd. tā ,festhaltend', ahd. zāhi, nhd. zäh'.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I p.790 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt lines ~49845-49860)\",\"stance\":\"supports\",\"note\":\"The same Germanic paragraph, with the added semantic bridge 'mit weiterer Verschiebung zu „zusammenkneifen, zusammendrücken“ und „zusammendrängen, verbinden“ (wie ai. sam-daś- „beißen, zusammendrücken, dicht auf etwas liegen“)'.\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1971.txt line 249567, s.v. tongs\",\"stance\":\"supports\",\"note\":\"'tongs, n. pl. — ME. tange, tonge, fr. OE. tang, tange, rel. to OS. tanga, ON. tǫng, Dan. tang, Swed. tång, OFris. tange, MDu. tanghe, Du. tang, OHG. zanga, MHG., G. zange, lit. “that which bites” (cp. OHG. zangar, “biting, sharp”), fr. I.-E. base *denk-, “to bite”, whence also OI. dáśati ... Gk. δάκνειν, “to bite” ... For sense development cp. F. mordache, “tongs”, fr. mordre, “to bite”.'\"}\n ]\n}\n]\njson.dump(nodes, open(S+'e1n34.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 1 nodes 3-4"
}
```


### [2026-09-05T18:27:13.969Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:28:02.116Z] TOOL CALL #92: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nnodes=[\n{\n \"id\":5,\"lang\":\"English\",\"words\":\"tongs; tough; zinc\",\"verdict\":\"plausible\",\n \"derivation\":\"Three English words, two of them inherited and one a modern loan, all filed by Watkins under denk-. (a) tongs: Old English tang, tange 'pincers' (plural tonge, tange in Middle English) < PGmc *tanguz; the word has always been used in the plural in English. This is the securest of the three — Klein, Pokorny and Walde-Pokorny all agree, and the semantic motive ('the biter', cf. French mordache 'tongs' from mordre) is well documented. (b) tough: Old English tōh 'strong and firm in texture, flexible without being brittle; tenacious, sticky' < PGmc *tanhu- (with loss of the nasal before h and compensatory lengthening, OE tōh > ME tough); the attachment to *denḱ- 'on the notion of “holding fast”' is Watkins' proposal and Etymonline attributes it to him by name, so it is the standard but not an unchallenged derivation — hence the node is graded plausible rather than confirmed. (c) zinc: not inherited at all but a modern borrowing from German Zink, which is the same word as Zinke 'prong, point' (< Old High German zint 'a point, jag' < PGmc *teng-); Paracelsus is credited with the first use, c.1526, the metal being named from the shape of its crystals after smelting. English took the word in the 17th-18th centuries and respelt it with -c- in 1813 under French influence. So the chart's three English words really do go back to one Germanic box, but by three different routes — inheritance, inheritance, and a Renaissance loan from German — which the single arrow of the diagram cannot show.\",\n \"derivation_fa\":\"سه واژهٔ انگلیسی در این جعبه‌اند: دو تای آنها میراثی و یکی وام‌واژه‌ای نو، و واتکینز هر سه را ذیل denk- آورده است. نخست tongs: انگلیسی کهن tang/tange «انبر» (در انگلیسی میانه جمعِ tonge/tange) از ژرمنی *tanguz؛ این استوارترین حلقهٔ سه‌گانه است — کلاین و پوکورنی و والده-پوکورنی همداستان‌اند و انگیزهٔ معنایی («گازگیرنده»، بسنجید با mordache فرانسه از mordre «گاز گرفتن») نیز مستند است. دوم tough: انگلیسی کهن tōh «سفت و استوار در بافت، خم‌شونده بی‌آنکه بشکند؛ چسبنده» از ژرمنی *tanhu- (با افتادن خیشومی پیش از h و کشش جبرانی: tōh ‹ tough)؛ اما پیوند آن با *denḱ- «بر پایهٔ مفهومِ ‹سخت نگه‌داشتن›» پیشنهاد واتکینز است و اتیمانلاین آن را صریحاً به نام او می‌آورد، پس دیدگاه رایج است ولی بی‌رقیب نیست — از این‌رو حکم این گره «با احتیاط پذیرفتنی» است. سوم zinc: اصلاً میراثی نیست، بلکه وام‌واژه‌ای نو از آلمانی Zink است، و Zink همان Zinke «دندانه، نوک تیز» است (از zint آلمانی علیای کهن «نوک، دندانه»، از ژرمنی *teng-). نخستین کاربرد آن را به پاراکلسوس (حدود ۱۵۲۶ میلادی) نسبت می‌دهند و فلز را به سببِ شکلِ بلورهایش پس از گدازش چنین نامیده‌اند. انگلیسی این واژه را در سده‌های هفدهم و هجدهم گرفت و در ۱۸۱۳ به پیروی از فرانسه با -c نوشت. پس هر سه واژه به‌راستی به یک جعبهٔ ژرمنی بازمی‌گردند، اما از سه راه گوناگون — میراث، میراث، و وام‌گیریِ رنسانسی از آلمانی — و یک پیکانِ نمودار نمی‌تواند این تفاوت را نشان دهد.\",\n \"sources\":[\"https://www.etymonline.com/word/tough\",\"https://www.etymonline.com/word/zinc\"],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"No reference is given for this node; it is covered by the parent's AHD citation (denk-: '...: TOUGH ...: TONGS ...: ZINC'), checked at node 4.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1971.txt line 249567 s.v. tongs; line 250546 s.v. tough; line 270647 s.v. zinc\",\"stance\":\"supports\",\"note\":\"'tongs ... fr. I.-E. base *denk-, “to bite”'; 'tough, adj. — ME. togh, tough, fr. OE. tōh'; 'zinc, n. — G. Zink, prop. the same as Zinke' — Klein files all three where Nourai does.\"},\n  {\"src\":\"WEB\",\"where\":\"Etymonline s.vv. tough and zinc (archived)\",\"stance\":\"partial\",\"note\":\"tough: 'from Proto-Germanic *tanhu- ... Watkins suggests the Proto-Germanic form traces back to PIE *denk- “to bite,” on the notion of “holding fast”' — attributed to Watkins, i.e. a proposal rather than a consensus. zinc: 'from German Zink, derived from Zinke meaning “prong, point” ... first used by Paracelsus around 1526, applied “on analogy of the form of its crystals after smelting” ... The German Zinke traces back to Old High German zint (“a point, jag”), from Proto-Germanic *teng- (“tine”). The ultimate source is reconstructed as PIE *denk- “to bite.” The modern spelling with -c- dates to 1813 and reflects French influence.'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt line 19944, s.v. Tough\",\"stance\":\"partial\",\"note\":\"'Tough. (E.) M.E. tough. + Du. taai, ... G. zähe, O.H.G. [zāhi] ... Perhaps allied to [the root meaning] to bite ... that which resists biting.' Skeat already had the idea, but with 'perhaps' — the same hesitation Etymonline records.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt index lines 2361 and 2395\",\"stance\":\"supports\",\"note\":\"'TOUGH denk-' and 'TONGS denk-' in Watkins' word-index; the zinc reference is in the denk- article itself ('Germanic *teng- in Old High German zinko, spike, prong: ZINC').\"}\n ]\n}\n]\njson.dump(nodes, open(S+'e1n5.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF",
 "description": "Write entry 1 node 5"
}
```


### [2026-09-05T18:28:04.205Z] TOOL RESULT

```
ok
```


## [2026-09-05T18:28:05.865Z] AGENT

Now assembling the final file.


## [2026-09-05T18:28:12.110Z] TOOL CALL #93: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p117/'\nL=lambda f: json.load(open(S+f,encoding='utf-8'))\ne0=L('e0head.json'); e0['nodes']=L('e0n12.json')+L('e0n34.json')+L('e0n567.json')+L('e0n89.json')\ne1=L('e1head.json'); e1['nodes']=L('e1n1.json')+L('e1n2.json')+L('e1n34.json')+L('e1n5.json')\nout={\"pdf_page\":117,\"book_page\":87,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-05\",\"entries\":[e0,e1]}\np='/home/sfmqrb/git/rishe/data/verification/page-117.json'\nwith open(p,'w',encoding='utf-8') as f:\n    json.dump(out,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('nodes e0',[n['id'] for n in e0['nodes']])\nprint('nodes e1',[n['id'] for n in e1['nodes']])\nPYEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-117.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 117",
 "description": "Assemble and validate page-117.json"
}
```


### [2026-09-05T18:28:14.016Z] TOOL RESULT

```
nodes e0 [1, 2, 3, 4, 5, 6, 7, 8, 9]
nodes e1 [1, 2, 3, 4, 5]
JSON OK
nodes verified: 14/14
node verdicts: {'disputed': 2, 'confirmed': 10, 'plausible': 2}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 3, 'supports': 13, 'not_checked': 5, 'contradicts': 1}
books consulted: {'contradicts': 5, 'partial': 4, 'supports': 37, 'silent': 2} | by book: {'WEB': 8, 'KLN': 7, 'PHD': 5, 'NYB': 4, 'BRT': 3, 'ARY': 3, 'POK': 3, 'AHD': 3, 'HRN': 2, 'WLD': 2, 'SKT': 2, 'CHEUNG': 1, 'MON': 1, 'PLA': 1, 'LKT': 1, 'BQT': 1, 'SOD': 1}
```


## [2026-09-05T18:28:20.617Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'PYEOF'\nimport json\nidx=set()\nfor line in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: idx.add(json.loads(line)['url'])\n    except Exception: pass\nd=json.load(open('data/verification/page-117.json',encoding='utf-8'))\nused=set()\ndef collect(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources': used.update(v)\n            else: collect(v)\n    elif isinstance(o,list):\n        for x in o: collect(x)\ncollect(d)\nmiss=[u for u in used if u not in idx]\nprint(\"used\",len(used),\"missing\",miss)\nPYEOF",
 "description": "Check all cited URLs are archived"
}
```


### [2026-09-05T18:28:23.028Z] TOOL RESULT

```
used 12 missing []
```


## [2026-09-05T18:28:40.727Z] AGENT

Page 117 (book p. 87) verified. `data/verification/page-117.json` written; `verify_check.py 117` reports 14/14 nodes, **0 PROBLEM lines**.

**Verdicts** — roots: 2 confirmed. Nodes: 10 confirmed, 2 plausible, 2 disputed.
Ref checks: 13 supports, 3 partial, 1 contradicts, 5 not_checked (nodes Nourai gave no refs for). 37 supporting `consulted` entries across 17 books. All 12 cited URLs archived via `fetch_source.py`.

**Disputed**
- *Dema* node 1, Avestan `dâman 1` "domestic animals" — no such Avestan word. Bartholomae (cols. 735-737) has only dāman- "dwelling / creature, creation" from dā- "to create"; MacKenzie keeps ¹dām "creature" apart from ²dām "tame animal". Pokorny 199, Klein s.v. *tame* and Wiktionary all take Persian دام straight from MP dām < *demh₂-, with no Avestan link. The conflation comes from Moʿin's Borhān footnote (and is shared by Nyberg and Aryanpur), so it is traditional, not invented.
- *Denk* node 1, Avestan `danta`/`daitika` — the words and glosses are right, the parent is wrong. The tooth-word is *h₃dónts (Pokorny files it p. 287 s.v. ed-; Watkins: "dent- … [In Pok. ed- 287]"); Pokorny's p. 201 denk- entry, the page cited, contains no tooth-word at all. daitika- attaches to *dant- "tooth" (Bartholomae col. 678, Buck p. 138), not to *denḱ-.

**Plausible**
- *Dema* node 3, Greek `a-damas` — Beekes and Wiktionary reject "ἀ- + δαμ-, unconquerable" as folk etymology on an oriental loan (cf. Akk. elmēšu); δαμάω itself is fine.
- *Denk* node 5, English `tough` (with tongs/zinc) — the *denḱ- attachment of *tanhu- is Watkins' proposal, flagged as such by Etymonline and hedged by Skeat; zinc is a 16th-c. loan from German, not an inheritance.

**Extraction errors: none.** I read the printed page (image saved to `data/verification/sources/refs/ocr/BOOK/117.png`); the JSON matches it exactly, including `dâman 1`, `tangus`, `adamas, diamas` and the Sogdian `dt`.

**Reference-page findings worth noting** (all Nourai's numerals check out): BQT:817 and BQT:884 are exact (BQT vol. 2 offset here is printed = leaf + 540, not the +543 in `refs_online.json`); BQT:159, SOD:145 (a page, not an entry number), SYN:138, HRN:120 and BRT:653 (= the tiži.dąstra- column Pokorny sends you to) are all exact. Only AHD:364 and MON:342 could not be checked — the local AHD file is the Watkins appendix only, and the local Moʿin is the 2-vol. abridgement whose origin tags are lost in OCR.
