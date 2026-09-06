# Verification process log — verify-page-187


## [2026-09-05T21:00:44.916Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 187 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-187.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-187.json. Write /home/sfmqrb/git/rishe/data/verification/page-187.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 187` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T21:00:46.232Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T21:00:47.082Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T21:00:47.095Z] TOOL RESULT

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


## [2026-09-05T21:00:47.634Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-187.txt"
}
```


### [2026-09-05T21:00:47.648Z] TOOL RESULT

```
1	=== PDF page 187 (book page 157) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghen : to bite, chew  (refs POK:436)
4	#1 (parent #0) [Avestan] refs=POK:436; | gnixta : chewed ; aiwi-gnixta : eaten up, eroded ☞Ambhi
5	  #2 (parent #1) [None] refs=None | 
6	#3 (parent #0) [Germanic] refs=AHD | gnag : to bite ; gnatt : a biting insect
7	  #4 (parent #3) [English] refs=None | gnaw, gnat
8	--- entry 1 ---
9	ROOT [Indo-European] Ghengh; Ksengio : to proceed, step; pace  (refs POK:438; IEC:414,571)
10	#1 (parent #0) [Avestan] refs=POK:438; KLN:639; IEC:414 | zanga : ankle ; zangô : upper part of the foot
11	  #2 (parent #1) [Persian] refs=HRN:302 | zang «زنگ» : foot (obsolete)
12	#3 (parent #0) [Persian] refs=IEC:414 | jang «جنگ» : fight ; xeng «خنگ» : (white) horse
13	#4 (parent #0) [Sanskrit] refs=IEC:414,571 | janh : dash around ; janghâ : lower leg ; xanjami : limp
14	#5 (parent #0) [Germanic] refs=KLN:639; AHD:542 | gang : going, journey, passage (a group of people going together)
15	  #6 (parent #5) [English] refs=KLN:639 | gang ; gangster
16	    #7 (parent #6) [Persian] refs=VOP:303 | gângester «گانگستر» : gangster
17	
```


## [2026-09-05T21:00:50.687Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-187.json",
 "description": "Read source JSON page 187"
}
```


### [2026-09-05T21:00:50.721Z] TOOL RESULT

```
{
  "pdf_page": 187,
  "book_page": 157,
  "entries": [
    {
      "root": {
        "name": "Ghen",
        "lang": "Indo-European",
        "refs": "POK:436",
        "gloss": "to bite, chew"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:436;",
          "words": [
            {"translit": "gnixta", "gloss": "chewed", "script": null},
            {"translit": "aiwi-gnixta", "gloss": "eaten up, eroded", "script": null, "see": ["Ambhi"]}
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
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "gnag", "gloss": "to bite", "script": null},
            {"translit": "gnatt", "gloss": "a biting insect", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "gnaw, gnat", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghengh; Ksengio",
        "lang": "Indo-European",
        "refs": "POK:438; IEC:414,571",
        "gloss": "to proceed, step; pace"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:438; KLN:639; IEC:414",
          "words": [
            {"translit": "zanga", "gloss": "ankle", "script": null},
            {"translit": "zangô", "gloss": "upper part of the foot", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:302",
          "words": [
            {"translit": "zang", "gloss": "foot (obsolete)", "script": "زنگ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:414",
          "words": [
            {"translit": "jang", "gloss": "fight", "script": "جنگ"},
            {"translit": "xeng", "gloss": "(white) horse", "script": "خنگ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:414,571",
          "words": [
            {"translit": "janh", "gloss": "dash around", "script": null},
            {"translit": "janghâ", "gloss": "lower leg", "script": null},
            {"translit": "xanjami", "gloss": "limp", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:639; AHD:542",
          "words": [
            {"translit": "gang", "gloss": "going, journey, passage (a group of people going together)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:639",
          "words": [
            {"translit": "gang", "gloss": null, "script": null},
            {"translit": "gangster", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "VOP:303",
          "words": [
            {"translit": "gângester", "gloss": "gangster", "script": "گانگستر"}
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


## [2026-09-05T21:00:51.187Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T21:00:51.227Z] TOOL RESULT

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


## [2026-09-05T21:01:02.880Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','KLN','AHD','HRN','VOP','BRT','WLD','SYN','SKT','MON','BQT','ARY','PHD','NYB','HUB','CHEUNG','FSD','WEB']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-05T21:01:03.445Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && sed -n 1,60p data/verification/page-124.json"
}
```


### [2026-09-05T21:01:04.717Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
== VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
== CHEUNG null
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
```


### [2026-09-05T21:01:04.768Z] TOOL RESULT

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
  "pdf_page": 124,
  "book_page": 94,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dhě 2",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
      "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
      ],
      "ref_check": [
        {
          "ref": "AHD:1512",
          "status": "supports",
          "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the same list Nourai cites by its 1975 New College page 1512 (roots are alphabetical over pp.1505-1550, so 'dhē-' falls in the right place); the copy on disk is the 1985 standalone reprint with different pagination."
        },
        {
          "ref": "POK:235",
          "status": "supports",
          "note": "POK_full.txt lines 22276-22510: 'Root / lemma: dʰe-2 / Meaning: to put, place, say' ... 'References: WP. I 826 ff ... Page(s): 235-239'."
        }
      ],
      "consulted": [
        {
          "src": "POK",
          "where": "pp.235-239, dʰē-2",
          "stance": "supports",
          "note": "supplies not only the root but every Iranian form of the chart: 'Avestan Old pers. data-', 'Avestan ni-δaiti- f. „laying down, putting away, hiding“', 'Avestan gao-δi- „milk container“', 'Avestan gao-δana- n. „milk container“', 'Avestan daman-, dąman- n. „site, creature“'."
        },
        {
          "src": "WLD",
          "where": "Bd. I pp.826-830 (p.828)",
          "stance": "supports",
          "note": "the parent article of Pokorny's; p.828 carries 'av. ni-δaiti- f. „das Niederlegen, Ablegen, Verbergen“', 'Ai. dhāna-m „Behälter“ ... av. gao-dana- n. „Milchgefäß“', 'av. dāman-, dąman- n. „Stätte, Wohnstätte; Geschöpf“'."
        },
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. dhē-¹",
          "stance": "supports",
          "note": "'To set, put. Contracted from *dheə.' Same gloss as Nourai's 'to do, set'."
        },
        {
          "src": "Wiktionary",
          "where": "Reconstruction:Proto-Indo-European/dʰeh₁-",
          "stance": "supports",
          "note": "'*dʰeh₁- (perfective): to do; to put, place.'"
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
          "words": "ma[n]dz-dha; ahura-mazdha",
          "verdict": "confirmed",
```


## [2026-09-05T21:01:08.398Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 436\" POK_full.txt | head; echo ---; grep -n \"Page(s): 438\" POK_full.txt | head"
}
```


### [2026-09-05T21:01:08.458Z] TOOL RESULT

```
32768:Page(s): 436 
32782:Page(s): 436 
33004:Page(s): 436-437 
---
32875:Page(s): 438 
36697:Page(s): 438-439
```


## [2026-09-05T21:01:09.598Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghengh\\|ǵʰengʰ\\|ghen-gh\\|g̑hengh\" POK_full.txt | head -20"
}
```


### [2026-09-05T21:01:09.648Z] TOOL RESULT

```
36663:Root / lemma: ghengh- 
75506:probably reshuffling from Old Irish sce/7o'- "spring' (see be\o\N ghengh-^ march, step,
```


## [2026-09-05T21:01:12.452Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32740,32800p;32860,32890p' POK_full.txt"
}
```


### [2026-09-05T21:01:12.499Z] TOOL RESULT

```
Slavic zelu-i. 'turtle, tortoise' in: 

Church Slavic zeli^vb, russ. -Church Slavic zelva, Serbo-Croatian zelva, Czech zelva, 
russ. zolvbi., poln. zd/tv. 

References: WP. I 631, Trautmann 84, Specht Indo Germanic Dekl. 120. 
Page(s): 435 

Root/ lemma: p'^eA/i? (Germanic) and p'^eZ-d'^d (Slavic) 
Meaning: to cost, pay 

Material: Gothic fra-gildan^ repay, compensate ', us-gildan^ repay'. Old Icelandic gjalda^ 
defray, pay, repay, be worth ', Old English gieldan. Old High German geltan ' defray, 
repay, serve, sacrifice' (proto Germanic *je/dd), Old Swedish gja//a ds. {*je//=>d); Gothic 
g/7dn. 'tax, interest'. Old Icelandic 5/5/0'' payment, earnings, punishment'. Old English 
gield^ payment, tribute, tax, sacrifice, oblation, brotherhood ', Old Icelandic ^/M' 
membership ', Old English glide v\. ds., glldam. ' Gildenbruder ' (out of it Middle Irish gllda 
' squire '), Middle Low German glide, out of it Modern High German Glide; Old High 
German gelt^ payment, repayment, sacrifice, oblation etc.'. Modern High German Geld, 
QoVc\\c gllstru. 'tax'. Old High German gelstar{*geld-tra-) 'sacrifice, oblation, tax'; from 
ndd. gellen =gelfen derWes Lithuanian gelluotrbe valid'; 



Old Church Slavic zledg zlesti {zladg zlasti) " repay, pay, atone' would be, if common 
origin, o'/TT^opresent besides Germanic -/opresent. 

References: WP. I 632, Trautmann 82 f. 
Page(s): 436 

Root / lemma: gheluna 

Meaning: pine-tree 

Material: Armenian ye/^/?' palate, ceiling '; 

gr. xsAOvri 'lip, upper jaw', in addition perhaps also X£TAo(; 'lip', Aeolic Y^tKKoq,, if from 
*X£AFoq (Solmsen KZ. 29, 352); 

Old Icelandic g/g/nar'p'\ne tree', Swedish ga/'g'\\\, pine tree', Danish gjce//e6s. 

References: WP. I 632. 
Page(s): 436 

Root / lemma: ghe/- 

Meaning: to call, cry 

Note: also in bird name, with -b- -b^^-and -^/-extended, compare the similar to 

onomatopoeic words ga/-, qel-. 

Material: Old \x\^\q, pra-galbha-h^ courageous, determined ' (: Old High German gelbon); 

gr. x£Ai5u)v 'swallow', older x£AT5Fu)v; the high-pitched sound coloring -/- reminds 
anlVliddle High German glTen^cvj, esp. from bird of prey', redupl. gr. KixAr), syrak. KixpAa 
'choke'; 

Note: 

Maybe alb. {* ghalandus) dalendyshe^a swallow' : Latin harundo -inisi. 'a reed; meton., for 

References: WP. I 628. 
Page(s): 428 

Root / lemma: ghen6^-{ghon6^-) 
Meaning: boil 



Material: Gr. KavGuAr) "ulcer, swelling, lump, growth', Kov9r|Aai ai avoi5na£i(; Hes.; 

Gothic gundu. " cancerous ulcer ', Norwegian dial, gundm. "scurf'. Old English gundxu. 
"pus'. Old High German gundm. "pus, pustulating ulcer'. 

References: WP. I 588. 
Page(s): 438 

Root / lemma: ghencf- and ghed- 

Meaning: to grab, grip 

Note: For concurrent the unnasalized and the nasalized root form s. Brugmann l|2 3, 293f., 

IF. 32, 321 

Material: Gr. xavSavw ( *ghend-) " take in, hold, contain, take; to be capable, able; catch', 

Aor. £xa5ov ( *ghnd-), Fut. xsicjopai {*ghend-s-), Perf. with present-meaning K£xov5a; 

alb. gjendem ( *ghend-) " be found ', gjenj, gjenj, Geg gjej^ixud' (G. Meyer BB. 8, 187, 
Alb. Wb. 140, Alb. stem III 10; gjet' find, regain ', s. Schmidt KZ. 57, 20ff.);
```


## [2026-09-05T21:01:12.550Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '36655,36710p' POK_full.txt"
}
```


### [2026-09-05T21:01:12.594Z] TOOL RESULT

```
the above equation always doubtful. 

References: WP. I 626 f., Petersson Heterokl. 155 f., nVH. I 581. 
Page(s): 434 

Root / lemma: ghengh- 

Meaning: to march, step 

Material: Old Indie 75/77/735-11. " footstep, flapping 'Jarjgha^ shank, leg, shin bone ', 

Avestan za/7^a/77 'ankle of the foot', -zangra-{\n compounds) ds., zero grade Old Indie 

jaghana-m. n. "buttock, pubic region ' : gr. Koxwvn " place between thighs' (assim. from 

*Kaxu)va); 

Old English -g/hf gait ', Middle High German g/ht' gait, journey' (proto Germanic 
*g/nxtf- from gheng-ti-), with gradation o.' Gothic gaggu.. Old Icelandic gangr. Old English 
Old High German gang^ gait ' and Germanic *gangjan \ter. (Gothic preterit gagg/da' 
walked ', Old English gengan. Middle High German gengen, gancte^ leave; wade in') and 
thereafter also *gangan, Gothic gaggan 'go' = Old Icelandic ganga {gekk). Old Saxon 
gangan {geng). Old High German gangan {giang). Old English gongan6s., wherefore Old 
High German gengi. Old English genge. Old Icelandic gengr^ feasible, able to be carried 
out', Gothic framgahts' advance'. Old Icelandic gatV incision in doorposts', gaettT door 
frame '; zero grade Old Frisian gunga 'go', Danish gynge, older gunge 'swing'; 

Lithuanian zengiu, zengti^ march, step, stride, strut ', prazanga' contravention, violation 
', zingsnis ' footstep '. 

A duplicate Aniaut (through dissimilation?) perhaps in Old Irish cingim ' march, step, 
stride, strut' (3. PI. cengait, Perf. cechaing), cymr. rhy-gyngu^ going pass ', Old Irish cing. 
Gen. cinged^\Narr\or\ gall. Cingeto-rTx, zero grade proto Celtic *kngsmn\n Old Irish ceimm 
{* kenksmen), cymr. corn, cam, bret. camm^ footstep ' {*kanksman). 

An other variant *ghenk-\s (under d/r^-s 'quick, fast') for Old High German ^5/7/ "rash, 
hasty, sudden' take into consideration. 

References: WP. I 588, WH. I 217, Trautmann 370. 
Page(s): 438-439 

Root/ lemma: ^^e/d^-and ghei^^- 

Meaning: to encircle, enclose 

Note: because of Latin hortus{see gher-4) extension from *gher-4^ caich'; 



Material: A. ghe/ti'^-{here also about the original aniaut nothing conclusive about words of 

the centum languages):
```


## [2026-09-05T21:01:19.904Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: ghen\\|Root/ lemma: ghen\\|Root / lemma: g^hen\\|lemma: ghen\" POK_full.txt | head -20; echo ---; sed -n '32980,33010p' POK_full.txt"
}
```


### [2026-09-05T21:01:19.959Z] TOOL RESULT

```
32864:Root / lemma: ghen6^-{ghon6^-) 
32877:Root / lemma: ghencf- and ghed- 
32926:Root / lemma: ghen- 
36663:Root / lemma: ghengh- 
---

Old Icelandic, Norwegian dial, gniti.. Old Swedish gnether, Swedish gnet, Danish gnid, 
Latvian gnJda' nit, louse, greedy, stingy person' (MiJhlenbach-Endzelin I 633), Lithuanian 
P'///7o'a(dissimilated from *gnindal)\ russ. gnida, sloven, gnjida, Czech hnfda, poln. gnida, 
about Latin iens, -disi. ds. compare WH. I 783f. and Specht Dekl. 44. 

^/-extensions ghneu-, ghneud!^-, ghneus-: 

Gr. xvauu) " nibble, scour, scratch, gnaw ', xvaujja " slice, tidbit ', xvaupoc; " dainty', 
Xv6o(;, xvou(; " that what can be scraped off, dust, foam, froth, underfur '; 

Old Icelandic g-nOa'rub' (also gnyia' rant, make a noise, roar', gnyr^ din, fuss, noise 
'?), Old Icelandic ^/7ai/d "noise, rattle', gnydr^nag, growl'. Old English gneaf^' stingy, 
tightfisted'. Middle Low German gnauwen' growl '; 

Lithuanian gniOsai \erm\n, pest'. Old Church Slavic ^/7^56A7b "disgusting', gngsati, 
gnusatisg'be disgusted', russ. gnus\errc\'\r\, pest', Serbo-Croatian gnus' disgust, 
repulsion, loathing, smut', Czech iinus' disgust, repulsion, loathing, smut', iinusny 
"disgusting', poln. gnusny'\6\e, blight, decay'. 

References: WP. I 584 f., WH. I 783, Trautmann 93. 



Page(s): 436-437 



Root / lemma: gher-1 

Meaning: expr. root
```


## [2026-09-05T21:01:21.278Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"gnixta\\|aiwi-gnixta\\|aiwigni\\|ni-gnixta\" POK_full.txt BRT.txt AHD_watkins1985.txt IEC.txt 2>/dev/null | head -20"
}
```


### [2026-09-05T21:01:21.348Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:01:23.489Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32920,32980p' POK_full.txt"
}
```


### [2026-09-05T21:01:23.532Z] TOOL RESULT

```
perhaps also Old Church Slavic gadati^ assume, mean' ("grasp spiritually '), russ. 
gadatb " conjecture, create, invent ', Czech hadatT advise, mean', etc. 

References: WP. I 589 f., WH. I 638, Thurneysen Gr. 353, Berneker 288 f. 
Page(s): 437-438 

Root / lemma: ghen- 

Meaning: to crack open, grind, scratch 

Material: Only in den extensions ghnegh- : ghnegh-, ghnac^h)-, ghne'h, ghneu-. 

guttural extension ghnegh-: 

Avestan aiwi-ynixta-^ gnawed, corroded '; Old Norse gnaga^ gnaw', Old English 
gnagan, g/nagan {\N\t\r\ anaptyktischem vowel), late nagands. - Besides with Indo 
Germanic ^in aniaut and Franconian cnagan, Dutch knagen6s.; 

Latvian gnega' someone who eats with long teeth ' (the softening after Endzelin Latvian 
Gr. 136 f. characteristic for scornful expressions), compare also MiJhlenbach-Endzelin 
Latvian-D. Wb. I 634. 

Dental extension ghnad[h)-: 

with intensive consonant stretch Old English gnsettm. " mosquito ', engl. gnat' 
mosquito ', ndd. gnatte'smaW mosquito ', Danish dial. gnat'smaW piece'. Middle High 
German gnaz, -/zes 'scurf, niggardliness'. Modern High German Gnatz, Gnatze'scurf, 
skin rash '; Old Icelandic ^/7p//'a "clatter, rattle, clash (of skeleton)', engl. dial, tognatter, 
Swedish gnat' Genorgel, Gezank ', gnatig' peevish, immer grumpy, surly, sullen ', 
Modern High German gnatzig' iJbellaunisch ' (compare kratzig\v\ the same meaning). 

further with dd Old Norse gnaddr' the young from animals or people ', Old Icelandic 
gnadda' murren, mit ubellaunischen Worten qualen ', Norwegian dial, gnaddra, "drone, 
grumble, growl ', ndd. gnadderig' iJbellaunisch, morose '. 

Persson Beitr. 95 f., 811. 

/■extensions ghnei-, ghneid(h)-: 



Gr. xvisi ^)am[,z\, Gpunsi (I. Gpunrsi), xviapwTspa xvocjL)[5£a]T£pa Hes.; 

Old English gnkfan'rub, grind ', Old High German gmtan. Middle Low German gnTden, 
from which probably Old Swedish gmdha, Swedish gnida, Danish gn/debomwed is; 
compare also (likewise borrowed?) the rare Old Icelandic gnida 6s.\ Old Icelandic gmsta 
tonnum^ clatter with the teeth ', Middle High German ^/7/s/ "ground', Tirol GneisV chopped 
or scraped stuff '; Norwegian dial, gnita ' |^ ^gs 9'^g^gP'"ungene^ ^ ^ jjy^ ', Middle Low 
German ^/7///e "small mosquito ', East Frisian gnid, gniV sundries, small stuff; a kind of 
small gnats ', Modern High German (SA7/i'ze "small mosquito '; 

Latvian gnJde "rough, shabby, dirty skin'; Old Church Slavic gnijQ, gniti^ blight, decay ', 
russ. gnitb, Bulgarian gnija, Serbo-Croatian gnj/'t/and gnjfliti, Czech hnfti, poln. gn/c6s.; 
Old Church Slavic gn/7b " rotten ', russ. gn/7, Serbo-Croatian gnj/'o, Czech hn/7y, poln. gn/ty 
ds.. Old Church Slavic gnojb " manure', russ. gnq/"pus\ Serbo-Croatian gnq/^ds.', Czech 
hnuj'crap, muck, manure ', poln. gndjds. 

Maybe alb. {*gno/a) njolla " stain, dirt ' common alb. gn- > nj-. 

hereupon ghriTda^ nit, louse ':
```


## [2026-09-05T21:01:38.204Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"nixta\" \"gnixta\" \"ynixta\" \"aiwi.ynixta\" \"aiwi-ynixta\"; do echo \"== $p\"; grep -n \"$p\" BRT.txt | head -8; done"
}
```


## [2026-09-05T21:01:39.329Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^ghen\\|ghen-\\. \\|ghen\\.\" AHD_watkins1985.txt | head -20; echo \"=== gnaw\"; grep -n -i \"gnaw\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T21:01:39.865Z] TOOL RESULT

```
== nixta
3800:•  j.  aiwi-ynixta- Adj.  (fem.  VJ-) 'angenagt, angefressen' :7«i'  nasus  °ta  sünö  v3  k?niß.- s^arö  vayS  vä  k^m/s^i^arö  {%A.)  V.  7. 30; —  'la  V.5.34PÜZ'.
4284:•  j.  an-aiwidnixta-  Adj.  'unbelogen,  un- betrogen':  miknm  .  .  yS  narim  'ts  apa azaahat  baraiti  Yt  70,23.
4286:•  j.  an-aim.dnixtay-  Adj.  'worum  man nicht  betrogen  werden  kann' :_>'«i^^(näral. yifnahi)  däiti  paiti  vaufiS  nisrlta  'ti (NSd.)  "durch  dessen  Gewährung  das höchste  Gut  überantwortet  wird,  um  das mannichtbctrogen  werden  kann"  Y.  65.  II. :
4418:•  j.  an-ä'dnixta-  Adj.  i)  'unbelogen,  un- betrogen':     apa    haca    qzanhtbyiS    tnihra
9564:—  ycsi  nasus  aiwi.ynixta  sünS  va   'J^arö       Et.?    Vgl    üj^jo-?    —    ai.  vgl.  fyianav-  m.
11889:•  j.  taJia  Adv.  i)  'dann,  alsdann':  yat.. altma  aisa  mlirika  f  apührJm  (sd.)  tiija- ja/V.5.45;  8.'36;  —  ä^ritim  f  ..vlväla- yantu  V.Ä16;  17,  18;  —  /•  kunavd  .  . Jata  paiiyante  Ytio.  113;  —  avavat  f ya>a  cd^wärS  »niavs  Y.g.sq.  a)  es geht  ein  Satz  mit  ^«i  'wenn' voraus:  _>'«( nasus  anaiwiynixta  .  .  f  dim  .  .  %ris maygm  avakanaym  V.  1^.37.  b)  es folgt  ein  Satz  mit  yat  'wenn';  P  nS  jam- yat  avairihe  .  .  yat  bfnz?m  baräi  ai'tra viläm  Yt.io.113'*.  2)  'damals,  da": yüzsm  f  taurvayata  ibalsä  dänunqm  Yl 7J.38;  38;  —  im  Wechsel  mit  tat  (sd,); f  dim  ahurS  mazdä  avqn  (Sp.  112  m.)  .. tat  aps  uruarisla  Yt, Ä7;  — fravasayS .. yi  .  .  tatja  nijasfn  (Sp.  500  m.)  xslreiwyö *tat  ySi .  .  xitavayS  .  .  aztn  pisana  Yt.  13. 37.  a)  mit  folg.  yat  'als':  fravasayS yil  /°  sriowa  histinta  yat  *maityu  damqn dai'nt9m  Yt. /j.76,  3)  'alsdann,  ferner'; ya  haca  da^ayasnaHbyS  . .  apa.bara  (sd) aya  raiufrisf  yat  paiti.banHti  "was  man . ., damit  ist  man  r.\  ferner  {mit  dem),  was.." N._54;  —  caturqm  asvqm  *'kahmaiHi  t' */rayafvAqm  (sd.)  N.öj.  4)  'so,  derartig'; es  folgt  ya%a:  t  ayaos  (sd.)  ya%a  .  .  Yt Ä 1 4^.         Undeutlich:  k^a  nara  t°  mara
18783:Sü.:  nirgaminyak  (NP,).  —  0  Das  ä  »om  NS, •«i/j  E.  dageg.  lat.  «ö-.  —  >)  Gdn.  KZ.  sÄ  si  i. •  j.  nasav-  f.,  m.  'Leiche,  Leichnam'  (von Menschen  und  Tieren);  'Leichenteil':  nSii spsMrjtS  nsit  . .  °su/  nanm  nötl  *astara- yäti  yaica  alte  °jai^  ('Leichenteile')  ^5  sps.- birslaca . .  'tus  nanm  *3stärayantfm  äahäi Uar^Jtäitya  .  .  visps  anhul . .  p^/SJanu/ frSria  ankam  °sunqm  ('Leichen')  ys  paiti äya  zima  irfnhar^V.j.if.; — jaica  aste 'sävS  fri^yeilica  puyäica  Y.6.28;  —  iat iä  nara  yaoidayqn  anhm  .  .  yä  'säum ava.h>Tvta  ssnS  vä  paraAristahe  tnasyeke vä  V.iV.3S;  33,  97,  5.42;  — >aÄ<i  narim alavarum  .  .  'sui  (AP.)  aoi  ava  *%ravTt (Sp.8o2U.)P.2y;  — yai  aesa  'sus  anaiwi.- ynixta  sanS  vS  ..  V.J. 2^;  30; — yt . . matdayasna  ,  .  taci.apaya  (sd.)  's3um^^ frajasqn  .  .  aS^a  S/s  ayaoidya  .  .  yavat azsa  'sus  niibpnla;  us  haca  'savö  (GS.) altavat  apat  Aaca  niiläraym  (Sp.  939  o.) ,  .  pasia  'savs  (GS,)  niüjn^i  .  .  a/i yaoidya  bavaiti  V.  6.  26—32;  —  pasi'a  ., 'Säum  avaJian^mtiisA.)  sps/um  vä  raoitm vä  vfhrkim  wa  V.  5.  J;  —  nara  .  .  yä 'Säum  matgu^qtn  äp»m  ä  vä  älnm  ä  vä ,  .  frabarmti  V.  7.  25;  —  yat  .  .  mazda- yasna  . .  ätnm  nasu.paktm  /ra/asan  'sBm hqmpa^qn  'sUm  /i<lvayqn{sA.)  V.ff.j^;  — «äV  vatihs  ..  iyaöimm  v^myeiti  ydOBii^ puhrake  .  .  frä  nast>m  (sd.)  'sam  pacät  \ V.  76. 1 7 ;  —  nara  . .  yä  'säum  fraauharät  I sünS  vä  .  .  masyefu  vä  V.  7.23;  —  visp^m  j ä  ahmäi  'sunqmca  aiwi.varsianqm  (sd.)  j V.  5, 14;  —  apim  zazämi  aztm  yS  akurS\ mazdä  . .  avi  "ssm  (in  koll.  Sinn)  vazämi  1 . .  tä  ha%ra  frafrävayämi  avi  zrayn  päi- 1 Hifm  (sd.)  V.  5. 1 7  f. ;  1 5  f.  A)  Name  der  \ Leichenhexe*':  ial  .  .  'sus  upa.dvqsaitii ..  i^ari  pasca  para.iristlm  ..  us  haca  6ao%S ayät  .  .  'SUS  upa.dvqsaiti  apäx^raiibyS naHnaeibyB  *maxsi.hhrpa  arrjaitya  V.  7. I  £;  —  yat  aSe  yä  sps.jataca  .  .  coatit>m pascaüa  srvätum  .  .  'sus'  upa.dvqsaitii  .  . asnyehe  (sd.)  pascaita  anyehe  ra^ws  .  . 'SUS  upa.dvqsaiti  V,  7. 3  f. ;  —  kuha  a!tat •sus  (statt  Aide.)  '>  pirTttäne  yä  haca  irista upa  jvanifm  upa-rag^waiti  (sd.)  V.  jo.  i, *9-A1^^;  —  "/"  vä  'sui  ra/hwät  (sd.) nänAanat  Aaia  V._J.  14;  p.  40;  —  /rä  el dvqsaiti  . ,  'sui  yai  dastmim  /räihaoiÜ naum»m  paiti.rathwayHH  (sd.)  V.5.  28; 27-32",  8.  41",  70,  71,  g.  15-24  (oft);
21771:ipaläl  barSit  '^.bg;bg; — y  nasus  aiwL- ynixta  ..  aitihä  £>mU  nidai^yqn  V.  7. 30; ag;  —  neben  *yat:  yast  %ina  . ,  pahqm (sd.)  Jasaiti  vq%waits,  bsiwranqm  . .  *sica hwaifä{sd.)  tanvB  a'ha  imqm  vaSs  drm- Jayöil  Yt  13.  30.  d)  ist  das  Verbum weggelassen:  y  hsi  dahms  antarat naimai  hährahe  aratufrii  N.  jo^j  J04, 26  (Sp.  76  hl);  —  °sila  hl  anya  aya fyao%na  Jravarsta  paitita  (sd.)  hl  Ska  V. j.  a  I ;  a  1 ;  —  hävanalibya  ratufrii  . .  y *anusavanta  (sd.)N.  107.  II)temporal'' 'quando;  wenn,  wenn  erst,  sobald  als'; i)  mit  /nä.;  im  übergeordneten  Satz  Steht Ind.:  y  das^msm  fralnaoili  naum»M paiti.- rai^wayäti  V.j.aß;  28—33"'.  a)mit
== gnixta
== ynixta
3800:•  j.  aiwi-ynixta- Adj.  (fem.  VJ-) 'angenagt, angefressen' :7«i'  nasus  °ta  sünö  v3  k?niß.- s^arö  vayS  vä  k^m/s^i^arö  {%A.)  V.  7. 30; —  'la  V.5.34PÜZ'.
9564:—  ycsi  nasus  aiwi.ynixta  sünS  va   'J^arö       Et.?    Vgl    üj^jo-?    —    ai.  vgl.  fyianav-  m.
11889:•  j.  taJia  Adv.  i)  'dann,  alsdann':  yat.. altma  aisa  mlirika  f  apührJm  (sd.)  tiija- ja/V.5.45;  8.'36;  —  ä^ritim  f  ..vlväla- yantu  V.Ä16;  17,  18;  —  /•  kunavd  .  . Jata  paiiyante  Ytio.  113;  —  avavat  f ya>a  cd^wärS  »niavs  Y.g.sq.  a)  es geht  ein  Satz  mit  ^«i  'wenn' voraus:  _>'«( nasus  anaiwiynixta  .  .  f  dim  .  .  %ris maygm  avakanaym  V.  1^.37.  b)  es folgt  ein  Satz  mit  yat  'wenn';  P  nS  jam- yat  avairihe  .  .  yat  bfnz?m  baräi  ai'tra viläm  Yt.io.113'*.  2)  'damals,  da": yüzsm  f  taurvayata  ibalsä  dänunqm  Yl 7J.38;  38;  —  im  Wechsel  mit  tat  (sd,); f  dim  ahurS  mazdä  avqn  (Sp.  112  m.)  .. tat  aps  uruarisla  Yt, Ä7;  — fravasayS .. yi  .  .  tatja  nijasfn  (Sp.  500  m.)  xslreiwyö *tat  ySi .  .  xitavayS  .  .  aztn  pisana  Yt.  13. 37.  a)  mit  folg.  yat  'als':  fravasayS yil  /°  sriowa  histinta  yat  *maityu  damqn dai'nt9m  Yt. /j.76,  3)  'alsdann,  ferner'; ya  haca  da^ayasnaHbyS  . .  apa.bara  (sd) aya  raiufrisf  yat  paiti.banHti  "was  man . ., damit  ist  man  r.\  ferner  {mit  dem),  was.." N._54;  —  caturqm  asvqm  *'kahmaiHi  t' */rayafvAqm  (sd.)  N.öj.  4)  'so,  derartig'; es  folgt  ya%a:  t  ayaos  (sd.)  ya%a  .  .  Yt Ä 1 4^.         Undeutlich:  k^a  nara  t°  mara
18783:Sü.:  nirgaminyak  (NP,).  —  0  Das  ä  »om  NS, •«i/j  E.  dageg.  lat.  «ö-.  —  >)  Gdn.  KZ.  sÄ  si  i. •  j.  nasav-  f.,  m.  'Leiche,  Leichnam'  (von Menschen  und  Tieren);  'Leichenteil':  nSii spsMrjtS  nsit  . .  °su/  nanm  nötl  *astara- yäti  yaica  alte  °jai^  ('Leichenteile')  ^5  sps.- birslaca . .  'tus  nanm  *3stärayantfm  äahäi Uar^Jtäitya  .  .  visps  anhul . .  p^/SJanu/ frSria  ankam  °sunqm  ('Leichen')  ys  paiti äya  zima  irfnhar^V.j.if.; — jaica  aste 'sävS  fri^yeilica  puyäica  Y.6.28;  —  iat iä  nara  yaoidayqn  anhm  .  .  yä  'säum ava.h>Tvta  ssnS  vä  paraAristahe  tnasyeke vä  V.iV.3S;  33,  97,  5.42;  — >aÄ<i  narim alavarum  .  .  'sui  (AP.)  aoi  ava  *%ravTt (Sp.8o2U.)P.2y;  — yai  aesa  'sus  anaiwi.- ynixta  sanS  vS  ..  V.J. 2^;  30; — yt . . matdayasna  ,  .  taci.apaya  (sd.)  's3um^^ frajasqn  .  .  aS^a  S/s  ayaoidya  .  .  yavat azsa  'sus  niibpnla;  us  haca  'savö  (GS.) altavat  apat  Aaca  niiläraym  (Sp.  939  o.) ,  .  pasia  'savs  (GS,)  niüjn^i  .  .  a/i yaoidya  bavaiti  V.  6.  26—32;  —  pasi'a  ., 'Säum  avaJian^mtiisA.)  sps/um  vä  raoitm vä  vfhrkim  wa  V.  5.  J;  —  nara  .  .  yä 'Säum  matgu^qtn  äp»m  ä  vä  älnm  ä  vä ,  .  frabarmti  V.  7.  25;  —  yat  .  .  mazda- yasna  . .  ätnm  nasu.paktm  /ra/asan  'sBm hqmpa^qn  'sUm  /i<lvayqn{sA.)  V.ff.j^;  — «äV  vatihs  ..  iyaöimm  v^myeiti  ydOBii^ puhrake  .  .  frä  nast>m  (sd.)  'sam  pacät  \ V.  76. 1 7 ;  —  nara  . .  yä  'säum  fraauharät  I sünS  vä  .  .  masyefu  vä  V.  7.23;  —  visp^m  j ä  ahmäi  'sunqmca  aiwi.varsianqm  (sd.)  j V.  5, 14;  —  apim  zazämi  aztm  yS  akurS\ mazdä  . .  avi  "ssm  (in  koll.  Sinn)  vazämi  1 . .  tä  ha%ra  frafrävayämi  avi  zrayn  päi- 1 Hifm  (sd.)  V.  5. 1 7  f. ;  1 5  f.  A)  Name  der  \ Leichenhexe*':  ial  .  .  'sus  upa.dvqsaitii ..  i^ari  pasca  para.iristlm  ..  us  haca  6ao%S ayät  .  .  'SUS  upa.dvqsaiti  apäx^raiibyS naHnaeibyB  *maxsi.hhrpa  arrjaitya  V.  7. I  £;  —  yat  aSe  yä  sps.jataca  .  .  coatit>m pascaüa  srvätum  .  .  'sus'  upa.dvqsaitii  .  . asnyehe  (sd.)  pascaita  anyehe  ra^ws  .  . 'SUS  upa.dvqsaiti  V,  7. 3  f. ;  —  kuha  a!tat •sus  (statt  Aide.)  '>  pirTttäne  yä  haca  irista upa  jvanifm  upa-rag^waiti  (sd.)  V.  jo.  i, *9-A1^^;  —  "/"  vä  'sui  ra/hwät  (sd.) nänAanat  Aaia  V._J.  14;  p.  40;  —  /rä  el dvqsaiti  . ,  'sui  yai  dastmim  /räihaoiÜ naum»m  paiti.rathwayHH  (sd.)  V.5.  28; 27-32",  8.  41",  70,  71,  g.  15-24  (oft);
21771:ipaläl  barSit  '^.bg;bg; — y  nasus  aiwL- ynixta  ..  aitihä  £>mU  nidai^yqn  V.  7. 30; ag;  —  neben  *yat:  yast  %ina  . ,  pahqm (sd.)  Jasaiti  vq%waits,  bsiwranqm  . .  *sica hwaifä{sd.)  tanvB  a'ha  imqm  vaSs  drm- Jayöil  Yt  13.  30.  d)  ist  das  Verbum weggelassen:  y  hsi  dahms  antarat naimai  hährahe  aratufrii  N.  jo^j  J04, 26  (Sp.  76  hl);  —  °sila  hl  anya  aya fyao%na  Jravarsta  paitita  (sd.)  hl  Ska  V. j.  a  I ;  a  1 ;  —  hävanalibya  ratufrii  . .  y *anusavanta  (sd.)N.  107.  II)temporal'' 'quando;  wenn,  wenn  erst,  sobald  als'; i)  mit  /nä.;  im  übergeordneten  Satz  Steht Ind.:  y  das^msm  fralnaoili  naum»M paiti.- rai^wayäti  V.j.aß;  28—33"'.  a)mit
== aiwi.ynixta
3800:•  j.  aiwi-ynixta- Adj.  (fem.  VJ-) 'angenagt, angefressen' :7«i'  nasus  °ta  sünö  v3  k?niß.- s^arö  vayS  vä  k^m/s^i^arö  {%A.)  V.  7. 30; —  'la  V.5.34PÜZ'.
9564:—  ycsi  nasus  aiwi.ynixta  sünS  va   'J^arö       Et.?    Vgl    üj^jo-?    —    ai.  vgl.  fyianav-  m.
== aiwi-ynixta
3800:•  j.  aiwi-ynixta- Adj.  (fem.  VJ-) 'angenagt, angefressen' :7«i'  nasus  °ta  sünö  v3  k?niß.- s^arö  vayS  vä  k^m/s^i^arö  {%A.)  V.  7. 30; —  'la  V.5.34PÜZ'.
```


### [2026-09-05T21:01:39.916Z] TOOL RESULT

```
517:ghen-. To gnaw. Hypothetical base of various Germanic forms. 1. Germanic *gnagan in: a. Old English gnagan, to gnaw: GNAW; b. Old Norse gnaga, to bite, akin to the probable Scandinavian source of NAG!. 2. Suffixed Ger- manic form “gnag-sk- in *(g)naskon in Old High German nascon, to nibble: NOSH. 3. Perhaps related is Germanic *gnatt-, “biting insect,” in Old English gnzt, gnat: GNAT. [Pok. ghen- 436.]
518:ghend-. Also ghed-. To seize, take. 1. Germanic *getan in: a. Old Norse getfa, to get: GET; b. compound *bigetan (*bi-, intensive prefix; see ambhi), to acquire, in Old English begietan, to get, beget: BEGET; C. compound *fer-getan (*fer-, prefix denoting rejection; see per’), “to lose one’s hold,” forget, in Old English forg(iJetan, to forget: FORGET. 2. Germanic “getison, “to try to get,” aim at, in Old Swedish gissa, to guess, akin to the Scandinavian source of Middle English gessen, to guess: GuEss. 3. Basic form *ghend- in Latin prendere, prehen- dere (pre-, prae-, before; see per'), to get hold of, seize, grasp: PREHENSILE, PREHENSION, PRISON, PRIZE?, (PRIZES), (PRY2); APPREHEND, (APPRENTICE), (APPRISE), COMPREHEND, COMPRISE, EMPRISE, ENTERPRISE, (EN- TREPRENEUR), MISPRISION, PREGNABLE, REPREHEND, (REPRISAL), (REPRISE), SURPRISE. 4. Form “ghed- in Latin praeda, booty (< *prai-heda, “something seized before”; prai-, prae-, before; see per'): PREDATORY, PREY, SPREE; DEPREDATE, OSPREY. [Pok. ghend- 437.]
519:ghendh-. Abscess, boil. Zero-grade form *ghndh- in Germanic *gund- in Old English gund, pus: GROUNDSEL!. [Pok. ghendh- 438.]
520:ghengh-. To go, walk. 1. Germanic “gang-, a going, in: a. Old English gang, a going: GANG}; b. Old High Ger- man gang, a going: GANGUE. 2. Germanic “gangan, to go, walk, in Old English gangan, to go: GANGLING. [Pok. ghengh- 438.]
=== gnaw
417:ed-. To eat; original meaning “‘to bite.” See dent-. 1. Ger- manic *etan in: a. Old English etan, to eat: EAT; b. Old High German ezzen, to feed on, eat: ETCH; c. Middle Dutch eten, to eat: orT; d. Germanic compound “fra- etan, to eat up (*fra-, completely; see per’), in Old English fretan, to devour: FRET). 2. Latin edere, to eat: EDACIOUS, EDIBLE, ESCAROLE, ESCULENT, ESURIENT; COMEDO, COMESTIBLE, OBESE. 3. Zero-grade form *d- in Latin compound prandium (< *pram-d-ium), “first meal,” lunch (*pram-, first; see per’): PRANDIAL. 4. Suf- fixed form *ed-un-d in Greek oduné, pain (< “gnawing care”); ANODYNE. [Pok. ed- 287.]
492:TION), GENERIC, GENEROUS, GENRE, GENUS; CONGENER, (CONGENIAL), DEGENERATE, (ENGENDER), MISCEGENA- TION; b. Greek genos and genea, race, family: GENEAL- OGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genés, ‘‘-born’”: -GEN, -GENY. 4. Suffixed full-grade form *gen-yo- in: a. Latin genius, procreative divinity, inborn tutelary spirit, innate quality: GENIAL!, GENIUS; b. Latin ingenium (in-, in; see en), inborn character: ENGINE, INGENIOUS. 5. Suffixed full-grade form *gen-d- in Latin indigena (indu-, within; see en), born in (a place), indigenous: INDIGEN, (INDIGENOUS). 6. Suffixed full-grade form *gena-wo- in Latin ingenuus (in-, in; see en), born in (a place), native, natural, freeborn: INGENUOUS. 7. Suffixed full-grade form *gen- men- dissimilated in Latin germen, shoot, bud, embryo, germ: GERM, GERMAN?, (GERMANE), GERMINAL, GERMI- NATE. 8. Suffixed full-grade form *gena-ti- in Greek genesis, birth, beginning: GENESIS, -GENESIS. 9. Redupli- cated form *gi-gn- in: a. Latin gignere (past participle genitus), to beget: GENITAL, GENITIVE, GENITOR, GENT!, (GINGERLY); CONGENITAL, PRIMOGENITURE, PROGENI- TOR, (PROGENY); b. Greek gignesthai, to be born: EPI- GENE. 10. Suffixed zero-grade form *-gn-o- in Latin benignus (bene, well; see deu-?), good-natured, kindly, and malignus (male, ill; see mel-5), evil-natured, malevo- lent: BENIGN, MALIGN. 11. Zero-grade form *gna- becom- ing *gnda- in Latin praegnds (prae-, before; see per’), pregnant: PREGNANT!. 12. Suffixed zero-grade form *gna-sko- becoming *gnd-sko- in Latin gndsci, ndsci (present participle ndscéns, past participle gndtus, nd- tus), to be born: NAIVE, NASCENT, NATAL, NATION, NA- TIVE, NATURE, NEE, NOEL; (ADNATE), AGNATE, COGNATE, CONNATE, ENATE, INNATE, NEONATE, PUISNE, (PUNY), RENAISSANCE. 13. Suffixed o-grade form *gon-o- in Greek gonos (combining form -gonos), child, procre- ation, seed: GONAD, GONO-; ARCHEGONIUM, EPIGONE. 14. Zero-grade form *gn- in Sanskrit ja- in krmi-ja-, “produced by worms” (see k*rmi-). [Pok. 1. gen- 373.] genu-'. Knee; also angle. 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL. 2. Basic form *genu- in Latin genii, knee: GENICULATE, GENUFLECT. 3. Suffixed variant form *gon-ya- in Greek gdnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL. [Pok. 1. genu- 380.] genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN. 2. Basic form *genu- in Greek genus, chin: GENIAL. 3. Suffixed variant form *gna-dho- in Greek gnathos, jaw: GNATHIC, -GNATHOUS; CHAETOGNATH 4, Variant form “g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.] gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF!, 2. Germanic *kabraz, “gnawer,” in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Ger- manic *kéfalaz in Old English céafl, jaw, cheek: JOWL!. [Pok. geph-, gebh- 382.] ger-'. To gather. 1. Extended form *grem- in Germanic *kram- in Old English crammian, to stuff, cram: CRAM. 2. Reduplicated form *gre-g- in Latin grex (stem greg-), herd, flock: GREGARIOUS; AGGREGATE, CONGREGATE, EGREGIOUS, SEGREGATE. 3. Earliest forms “ager-, *ggor-d-, in Greek ageirein, to assemble, and aguris, agora, marketplace (> agoreuein, to speak): AGORA}; (AGORAPHOBIA), ALLEGORY, CATEGORY, PANEGYRIC. [Pok. 1. ger- 382.] ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, crooked, hooked; something bent or hooked. 1. Germanic *krdpp6n-, a hook, especially one used in harvesting grapes, in: a. Old High German krapfo, a hook: AGRAFFE; b. Old French graper, to harvest grapes, hence (back-formation) grape,
517:ghen-. To gnaw. Hypothetical base of various Germanic forms. 1. Germanic *gnagan in: a. Old English gnagan, to gnaw: GNAW; b. Old Norse gnaga, to bite, akin to the probable Scandinavian source of NAG!. 2. Suffixed Ger- manic form “gnag-sk- in *(g)naskon in Old High German nascon, to nibble: NOSH. 3. Perhaps related is Germanic *gnatt-, “biting insect,” in Old English gnzt, gnat: GNAT. [Pok. ghen- 436.]
891:réd-. To scrape, scratch, gnaw. 1. O-grade form *réd- in: a. Latin rédere, to gnaw: RODENT; CORRODE, ERODE; b. suffixed (instrumental) form *réd-iro- in Latin rés- trum, beak, ship’s bow: ROSTRUM. 2. Possibly variant form *rdd- in: a. Latin radere, to scrape: RADULA, RASH?, RASORIAL; ABRADE, CORRADE, ERASE; b. suffixed (in- strumental) form *rdd-tro- in Latin rdéstrum, a rake, with diminutive *rdsculum, whence denominative verb *ras-
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
1175:wrod-. To root, gnaw. Germanic *wrét- in Old English wr6tan, to dig up: ROOT?. [Pok. 7. ver- 1163.]
1563:GLOWER ghel-2 GLUCAGON ag- GLUCOSE dlk-u- GLUE gel-1 GLUME gleubh- GLUT gWel-3 GLUTEN gel-! GLUTEUS gel-1 GLUTINOUS  gel-1 GLUTTON gWel-3 GLYCERIN dik-u- GLYPH gleubh- GLYPTIC gleubh- GNAT ghen- GNATHIC genu-2 -GNATHOUS genu-2 GNAW ghen- GNOCCHI gen- GNOME? gno- GNOMON gno- GNOSIS gnd-
```


## [2026-09-05T21:02:02.975Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9555,9570p' BRT.txt; echo \"=== zanga BRT\"; grep -n \"zanga-\\|zaŋga\\|zanga- \" BRT.txt | head -10"
}
```


### [2026-09-05T21:02:03.060Z] TOOL RESULT

```
A^^-  ?■  ^w  ^  T'  ^'  ^°i, '"/"'"'  ""■  J'"^^"''' '  •  J-  kui^sänay-  m.  EN.  eines  von  Haoma
dass   das  Wort  fem.  und  ntr.  war;    doch  s.  ■*  ..               ,   '            ,           .     ,        _  .
S  381.  —  s)  S.  No.  1.  —  *)  In  DsT.s  Über-  gestürzten,  den  mazrfavajwischen  Pnestern
Setzung,  Z.\.  ^,  118  wird  kihrf  ausgelassen,  feindgesinnten  Fürsten":  haomS  l>mcit yim
-~    n    Nur  in  dieser  Form;    sie  ist  auch  im  'säfrim  apa.xsai:rfmi%A.)nisähayat^'g.^^.
Aw.  die  häufigste.  »j    y>si.    ZA.  2.  93    meint:     "K.    reprisente
•  j.  k3r«ß.x''ar-  Adj,  'Leichen-,  Aas-  Aleiandre  et  l'oppression  hell^nique";  s.  auch fressend',  von  Hunden  und  Vögeln:  ydiüit  f^-  ^"^  Y'  u''""  /'^'-e  <?°<ä»<^.'"l'!  ^.  33.
,.        ,,....  ^   ,      -    Vb     "l   JfSTi  NB.  161  bemerkt  zu  jt!:    "em  Feind  des
.A«  ^J*«rf^  az'fleana«  jfi«J  va  '^ar3'  Hacma.  als  Dämon  des  Hungers".  Weiteres vayS  vä  '^ard  (NP.)  V.  6. 45 ;  46,  FrW.  // ;    ebd.
—  ycsi  nasus  aiwi.ynixta  sünS  va   'J^arö       Et.?    Vgl    üj^jo-?    —    ai.  vgl.  fyianav-  m.
vayj  va  ':e'arS  (NP.)  "wenn  der  Leichnam        Name  des  Wächters  des  bimmlischen  .S™«  -
angefressen  ist  —  aasfresseode  Hunde  oder ,     ^,^^  'Christ') ;  vgl.  lu  •*«■««-.
aasfressende  Vögel  (sinds,  die  das  tun)  — "       .    ,'         _  „,,  „  , ,
V.7.30";  39;    -   alx'ar,üma?il>y3  isA.)   •  J" .  ^'T^^f  P^',  "^^  ^.^^  ^"^^?  H^'^!*^  'l"
..äJmanam  *':^armn'^  V,?.2o.  iranischen  Sage-):  nmrt.maHä  '/ffYg.ji,
Aus    at.  Va«'^'-    (S  ^'^z).    wobei   der   NS. '  Yt.5.37.  ^5-^7, '5'38.44  ;— >'a/ Ä?(nänil.
=== zanga BRT
19240:•  j.   ni-zanga-   Adj,   'vom   Fnssknöcbel
27647:•  j.  zanga-,  zanga-  m,  'Knöchel  (des Fusses)',  von  «^»rischen  Wesen":  dastmm (bz.A^um)  zangß/n  V.Ä6S-67*,  9.23^*; —  ä  zangaiiiyascii  aps  a  xmthyasHt  äps V.ö.a?;  —  *aw(ffl»>  F-Jg-
28097:•  j.  zanga-  m.:  s.  unter  zanga-.
```


## [2026-09-05T21:02:03.422Z] TOOL CALL #17: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','POK']: print('==',k, d[k].get('page_offset'), '|', d[k].get('lookup_hint'))\n\""
}
```


### [2026-09-05T21:02:05.152Z] TOOL RESULT

```
== KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
== POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
```


## [2026-09-05T21:02:14.422Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27630,27670p' BRT.txt"
}
```


### [2026-09-05T21:02:14.466Z] TOOL RESULT

```
i)  Gegenüber  x\.  jayati  und  np.  läyad,  die ein  u.  *iäialai  verbürgen.  Es  kann  sich  aber nach  den)  Mmter  der  i-  und  u-Wuneln  schon im  Arischen  dem  nichtkomponirten  'iäjatai in  der  Komposition  ein  'i^alai  zur  Seite geslellt  haben  1  s.  dazu  Bthl.  IFAni.  ^.  14. — o>  nhd.  *iW.  Es  verhält  sich  j.  xäla-  {«i. jätä-)  EU  "M««-  wie  aj.frä/ätay  lO  j.//-flian- (flj-;  s.  ZDMG.  50.  69a  gegen  IFAni.  //.  47. —  7)  Them.  —  »)  Zu  Sj^jNo.  —  9)  S"9- I  a.  NA.  korrigitt{!)  in  'näitc.  —  ■")  s. vonScheoeder  ms.  /.  xviu.
•  j.,  g.  'zan-,  p.  *dan-  V.  'kennen'.  Praes. II  efänj;  Manä- :  zan-'^,  z?  taya-'K  — PPfP.  'Mtta-ä.         Vgl.  xs'nä:
"kennen' :  [  käram . .  Aya"  paranam  (sd.) bardiyam  adänä^  Bh.  /.  13 ;  ■—  mi^rH  zayäl (als  Praet?)*'  zara%uHnm  Y.y.  i  SüZ.
mit  ava  i)  'einer  Sache  (Akk.)  gewahr, inne  werden':  yähöit  dim  iätäUtpm  ava.- zatiqn  sBfiS  vä  ksnfijl'arU  . .  "auf  dass seber  am  sichersten  gewahr  werden  . ."  V. Ö.45.  2)  mit  praed.Akk.  'inne  werden, merken,  dass  etwas  .  .  ist':  ym  aS»m tristem  iipa.b3r>kwS.tartm  (sd.)  ava.zanan V.&2;  3.
mit  paiti  1)  'Jemanden  (Akk.)  aner- kennen, (bei  sich)  gut  aufnehmen,  will- kommen heissen':  al  mä  masä  yBzSm mazda  fräx^nim  mazdi  magai  a  paitl.- zänatä  (aPPrA.)!'  "so  nehmt  denn; Menschen,  ihr  mich  (den  Zar.)  bei  euch auf,  um,  o  M.,  für  den  grossen  Bund Unterweisung  zu  erhalten"  Y.  25. 1 1 ;  — iiS  fr'mät  kB  paiiLzanat  (n'amL  nö)  Yt.  JJ. 50; — yai  aiin  bavaiti  yasts  xmütö  fri^ö paiti.zan/S  Yt.S.^$;  V.jp.40,  Y, 57.34; —  fryafriha  faULzanta  (NSf.)  Yt.  ij. 36;  —  ihafrihä  paiti. zania  (NPf.)  buyata Yt/J.147;  —  ^ra/^B  ..  paüi.zantS  y. 57.14.  2)  'sich  Jemands  (Akk.)  an- nehmen': lg  narö  paiti. zumnti  yäAva  vir?- %ra.bao^B  {sA.)  Yty.  40.
mit  frä    'etwas    (Akk.)    ausfindig machen,  zu  ermitteln  wissen  aus  ~'  (/' mitlnstr,):  yB  ai/a  (Sp.  11  {.)pairi  an%ra frazanaiti^^  F.  5.
n.  jänati,  np.  dänad  'er  weiss'.  —  Pü. ;  da- «islan,  (ztt  Y.  39):  fäldaAiininüan,  erl.i/^C- äaiiSit  Harlan,  {für  piiili-san/a-):  palgriß;  s. noch  Na.  4.  —  >)  llTHL.  IF.  3.  80,  108.  — s)  Wie  vom  V,  'taa-.  Durch  Nominalbildungen wie  zan/aj/-,  das  zu  beiden  Verben  gehört, konnte  auch  die  Veiwendong  von  Verbal- Cornien  in  beiderlei  Bedenlungen  veranlaisl werden ;  vgl  ':arr-  No.  3,  —  3)  BtHU  ZDMG. 50.  692    und  'tan-  No.  ö.   —    O  Fü.  bat
■zantav-
1660
unklares  Wort  dafür  (aopadt),  erläutert  aber: f(ätäi  tu!  inäxl.  —  S  Them. j,  3«a»-"  f.  'Erzeugung,  Geburt'. KompE.»).  —  Ztun  V.  'm«-.   —   i)  Die  ent- sprechenden ai.  Stämme  werden  mit  'ja-  oder 'ja-  angesetzt;  s.  Lanuan  JAOS.  10.  438.
•  J.,  p.'*  zana-  m.  'Menschengeschlecht, "".asse'.
KompE.  —  Zum  V.  'eo«-.  —  aL  Jana-  m-, *Mensch;  Menschengeschlecht',  oss.  tänäg •Kind',  arm.  LW.  'san  'Art'.  —  '>  S.  zu  vispa-
•  j.  zaini'gav-  m.  EN.  eines  von  Frat»- rasyan  getöteten  Feinds  des  iranischen Volks:  yim  (näml.  wa^ä?«)  barat  fratirait iBrB  yat  drvä  'gaul  jaini  Yti^.  93,
Eig.  Bed.?>).  —  VgL  SBE.  47.  116.  —  »  S. JusTi  NB.  495 ,  wonach  man  zaeitig'  lesen müsste.     Vgl.  xainyävara-.
•  j.  zaintparSta-  Ad}.  Von  dem  kundigen erfragt,  durch  Fragen  ermittelt':  Aala.- mq'knmisA.)  'tfm,  Aa%a.mahrai  'tat,  Aala.- ma%rahe  'toAe,  Aala.ma%'ra  'ta  (VS.)  Eitr.
1-4-
*saiiü',  nur  KompA-,  tum  V.  »10«-.  —  Vgl. laL  gnäriis  und  unter  itr>d'i  Bthl.  IF.  ti. 136-
•  j.  zanga-,  zanga-  m,  'Knöchel  (des Fusses)',  von  «^»rischen  Wesen":  dastmm (bz.A^um)  zangß/n  V.Ä6S-67*,  9.23^*; —  ä  zangaiiiyascii  aps  a  xmthyasHt  äps V.ö.a?;  —  *aw(ffl»>  F-Jg-
KompE.  —  Vgl.  'sangro:  —  ai.  jäiighä-  f. 'Unterschenkel',  mp.  (Pü.)  tang,  oss.  »ÖKgä 'Unterschenkel'.  — ')  ImOegens.  va'tangra-. —  ')  Hds.  sinha,  aoa.
•  j.  zangra-,  smgra-,  ztara-'''^  m. 'Knöchel  (des  Fusses)',  von  i/a Ansehen Wesen".
KompE.  —  Vgl.  tanga-.  —  ')  S  26S.  47.  — >)  Im  Gegens.  zu  tanga—
•  j.    zanta-,    sfnta-    Adj.,    PPfP.:    s.
KompE.
•  j.  zantay-  f.  'Kennenlernen,  Kenntnis': 'ta  (LS.)  F.  20-).
KompE.—  ZumV.aian-;  kd.  mit  N0.6;  igL No.  l.  —  Pü.:  Inäienisn.  —  ')  VU,  ist  das Wort  aus  einem  Komp.  ausgelöst.
•  j.  'zantav-  m.  'Landkreis,  -bezirk,  Gau', im  Gegensatz  zu  Haus,  Gemeine  und  Land: nazdiÜim  avi  nmätumca  vjstmca  'tüm/a dahyamca  V.Ä103;  ¥.62.5,  Ytro.  18, 87;  —  nmäne  . .  vfsi  . .  'tvö  . .  datAhvB Y.g.  28;  N.  8,  *P.  ij,  Vr.  12. 5;  —  *«»ia«- ya!a   vliyafa  'tava/a  ''daAhavaca   Vr.  /2.
aby  Google
i66i
Hantav-
5;  —  Aaca  .  .  nmänat  . .  vital . .  'iaoi  , . *daiihaöt  Y. 57.14;  +N.J";  — fradaküi nmänaheca  vUaheca  *ilusca  daiiiAsusca YL5.6;  /0.17,  18,  83,  V.7.4i,42,<j.37, /O-S,  Y. /j.  I,  Vr.j.2,  N.5,  VytitT;  — paiti.p?r»ne  atsnm  mainynm  kaca  nmäna .  .  vTsa  .  .'tu  . .  *daiäAu  V.  10.  5 ;  — /ra- vaiayS yä  paoirya{%ä.)na/tar»  nmänanqmca vTsamia  'tunamca  dahyunqmca  Y.  23.  i ; Ä  7,  Yt./o,  18, /J.  150;  —  äpim  alsfmnS haväi  kaHi  najai , .  vTse  . .  'tave . .  *da»- AaiieYtiJ.66; — /rä  vä  susa  hala  "taot , .  Aa(a  daitihaot  Yt  /.  17.  a)  Gen.  mit
santu.patay-  (Stverz.) :  °Cä/  zantupaitts  Yt. JO.  83  usw.;  —  'hinqm  santupaitis  Yt iO.  18.
•)  An  Gt&sse  ond  Einwohnerinhl  zwischen VIS-  (sd.)  und  daSyav-  (sd.)  stehend.  In  SüErl. zu  Y.  7J.  I  wird  Akt  jandah  als  'Irimiannata- HärXytt^maa^  bezeichnet.  In  den  CäXäs  wird Uikra-  an  Stelle  von  t'  gebraucht  Vgl.  zur politischen  Gliederung  des  awestischen  Volks und  deren  Gegenstück  beim  vedischen  Ggr.  OK. 399,  Zimmer  AiL.  15S,  Scrrader  Reallex.  77Ö.
KompA.,  E. ;  Abieil.  —  Zuin  V.  'ain-.  —  ai.
jaHtav-    m.    ■Geschöpf;    mp.  (Pü.)  tand.    —
>)  So  T.
■  j.  ^zantav-,  g.  zJtitav-  f.'Kennenlerncn; Kunde'.
KompE.  —  Zum  V.  ':an-;  vgl.  lu  san/iiy-.
•  g.  zantu-patay- m.  'Herr,  Gebieter  eines Landbezirks,  Gaus,  Gauherr';  a)  im  eig. Sinn,  mit  Gen.  von  zaniav—,  nmänake  vä nmänü.paiti!  .  .  zanlJu^  va  'Paitis  Yt  10. 18;  83; — zaiiffus  'paittm  "^.7.^^,9-31, Vr.  J.  a ;  —  zantSuS  'iSe  YL  70. 1 7 ;  —  sait- tSui  'töii  Y.  13.\,  Yyt  16,  V. /o.  5;  — lantunqm  'paitis  {k?)  Yt/0. 18;—  zan- tiu^'paittm  näirikqm  V.  7. 42  ".  b)  von Göttern :   haema  nmsnspaite  . .  'patte  Y.
i>-a7-
mp.  (Pü.)  sandpat.  — ')  S.  tSt.  unter  daiükiipa- tay-  No.  2.
•  j.  zantu.baxta-  n.  'Be5timmung(srecht) über  den  Gau':  nöit  'Um  .  .  äsTzuste  (sd.)
```


## [2026-09-05T21:02:14.608Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==324' HRN.txt | head -80"
}
```


### [2026-09-05T21:02:16.497Z] TOOL RESULT

```
— M)2 —
237. xayltan 'hitten\ AW.-Komm., PPP. zast (kaum 2:aylt),
ap. x^jad-, jadiyamiy ^bitten'; aw. [/^jad-^ jaidyemi
'bitten.
238. ^and 'Gau, zandpat (AW.-Komm.).
aw. zantU'^ zantupaiti- 'Gau, Gauherr.
239. i^amj Tuss', AW.-Komm., Bund.; arm. LW. zangapmu
zankapan (de Lagarde, No. 752).
aw. zanga- 'Knöchel'; ai. jängha- unteres Bein*.
af/. zanymi Knie': oss. zängä 'Knie' (126).
Ein np. serjeng 'Ferse*, das de Lagarde auch
Armenische Studien No. 752 wieder anführt, giebt es
nicht; serce^ig bedeutet nur 'Fusstritt, Puff*.
240. zen 'Waffe', AW.-Komm., Men. 43, 7 (päz. zm\
zmavand (Aogem.).
aw. zaena- 'Waffe*; arm. LW. zen ottAoi/, aidrjQoq.
Für np. zm 'Sattel' scheint sich in der älteren Sprache
keine Anknüpfung zu finden; aw. zainis, phlv. zTrty
bedeutet wohl nicht 'Köcher (Geiger, Yätkär-i
Zarirän, S. 52 Note 19) und zainLparsta- ist ganz
unsicher.
241. i^tnitan 'wegnehmen'; zlmtär (ZPGL). Selten.
ap. [/^day-, adfnam 'ich nahm weg, aw. i^zay-, zinaf;
ai. i^jyä', jindti 'überwältigen, unterdrücken' (vergl.
Hübschmann, Casuslehre 192 Anm. 2, Fick'* I,
216).
```


## [2026-09-05T21:02:36.491Z] TOOL CALL #20: Bash

```json
{
 "command": "pdftoppm -f 187 -l 187 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg187 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T21:02:37.729Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^gang, \\|^gang \" KLN_1966.txt | head; echo \"--- gangster\"; grep -n \"^gangster\" KLN_1966.txt KLN_1971.txt | head; echo \"--- 1971 gang\"; grep -n \"^gang,\" KLN_1971.txt | head"
}
```


### [2026-09-05T21:02:39.028Z] TOOL RESULT

```
total 24644
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:02 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58105 Sep  5 17:02 build171.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5391 Sep  5 17:02 g2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2929 Sep  5 17:02 g3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5607 Sep  5 17:02 g4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14924 Sep  5 17:01 geus_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10247 Sep  5 17:01 ghaido_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4197 Sep  5 17:01 ghaido_low.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3293 Sep  5 17:01 n17b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17771 Sep  5 17:01 n17c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7472 Sep  5 17:01 n19.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3278 Sep  5 17:01 n5b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2334 Sep  5 17:01 n5c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  5 17:01 n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161412 Sep  5 17:01 p174hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  173427 Sep  5 17:01 p176hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53749 Sep  5 17:02 pg187.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77516 Sep  5 17:01 pg189.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T21:02:39.114Z] TOOL RESULT

```
15767:gang,  intr.  v.,  to  go,  walk  (dial.)  —  OE.  gangan. See  next  word.
15768:gang,  n.,  a  group  of  people;  a  band.  —  ME.  gang, ‘going;  passage’,  fr.  OE.  gang,  ‘going,  passage, channel’,  rel.  to  OS.,  OFris.,  Dan.,  Du.,  OHG., MHG.,  G.  gang,  ON.  gangr,  Swed.  gdng,  Goth. gagg,  ‘the  act  of  going’,  verbal  nouns  to  OE. gangan,  ON.  ganga,  Goth,  gaggan,  etc.,  ‘to  go’. These  words  derive  fr.  I.-E.  base  *ghengh-, *ghongh-,  ‘to  step’,  whence  also  OI.  jahgha, ‘shank’,  Avestic  zanga-,  ‘ankle’,  Lith.  zengiu, ‘I  stride,  step’.  The  above  words  are  not  related to  E.  go.  Cp.  gangue  and  the  second  element in  Doppelganger.
--- gangster
KLN_1971.txt:100000:gangster, n., member of a gang of roughs or 
KLN_1971.txt:195902:gangster (slang). — Of uncertain origin, 
KLN_1966.txt:15776:gangster,  n.,  member  of  a  gang  of  roughs  or criminals.  —  Formed  fr.  gang  with  suff.  -ster. gangue,  n.,  the  matrix  in  which  valuable  metals or  minerals  occur.  —  F.  gangue,  fr.  G.  Gang, ‘a  going,  walking,  passage,  vein  (of  ore)’.  See gang.
--- 1971 gang
99935:gang, intr. v., to go, walk (dial.) — OE. gangan. 
99938:gang, n., a group of people ; a band. — ME. gang,
```


## [2026-09-05T21:02:45.365Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg187.png"
}
```


### [2026-09-05T21:02:45.734Z] TOOL RESULT

```

```


## [2026-09-05T21:02:45.730Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T21:02:46.243Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport sys\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index for line 15767 (1-based)\npre='\\n'.join(lines[:15766])\nprint('leaf(0-based)=',pre.count('\\f'))\n\""
}
```


### [2026-09-05T21:02:48.103Z] TOOL RESULT

```
leaf(0-based)= 345
```


## [2026-09-05T21:03:01.758Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==346' KLN_1966.txt | grep -n -E \"^[0-9]{3}|[0-9]{3}[[:space:]]*$\" | head -20; echo \"=== first/last lines of leaf\"; awk 'BEGIN{RS=\"\\f\"} NR==346' KLN_1966.txt | head -3; echo ...; awk 'BEGIN{RS=\"\\f\"} NR==346' KLN_1966.txt | tail -3"
}
```


## [2026-09-05T21:03:01.903Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghengh\\|ĝhengh\\|kseng\\|ksengi\\|xseng\" IEC.txt | head -20"
}
```


### [2026-09-05T21:03:03.864Z] TOOL RESULT

```
4:638
5:639
=== first/last lines of leaf
.  —  Dial.  F.  gambe,  correspond¬ ing  to  F.  jambe,  fr.  ML.  gamba,  ‘leg’,  fr.  Late L.  camba,  gamba,  ‘fetlock;  hoof;  leg’,  borrowed fr.  Gk.  xap-TTr;,  ‘a  turn,  bend,  joint’,  which  is cogn.  with  L.  campus,  ‘field’.  See  camp  and  cp. gamba,  gambol,  gammon,  ‘ham’,  jamb, gamba,  n.,  an  organ  stop  (mus.)  —  Orig.  an  ab¬ breviation  of  viola  da  gamba  (q.v.);  fr.  it.  gamba, ‘leg’,  fr.  ML.  gamba.  See  prec.  word, gambade,  n.,  gambado.  —  F.  See  next  word.
gambado
Gaon
...
gannet,  n.,  the  solan  goose.  —  OE.  ganot,  ‘sea bird,  gannet’,  rel.  to  Du.  gent,  OHG.  gannasso, ganzo,  ‘gander’.  See  gander,  goose, ganoid, adj.,  1)  smooth  (said  offish  scales);  2)per- taining  to  the  Ganoidei.  • —  F.  ganolde,  com¬ pounded  of  Gk.  Y“V0S>  ‘brightness,  brilliance, splendor’,  and  -oeiS r)c;,  ‘like’,  fr.  eZSo?,  ‘form, shape’.  The  first  element  stands  for  ya-vo?  and is  rel.  to  yavo(xai  (for  ya-vo-fxat),  ‘I  am  glad,
I  rejoice’,  yalco  (for  ‘yafico),  ‘I  rejoice’.  See gaud,  ‘ornament’,  and  cp.  the  first  element  in Ganymede.  For  the  second  element  see  -oid. gantang,  n.,  a  weight  in  the  Malay  Archipelago. —  Malay  gantang.
gantlet,  also  spelled  gauntlet,  n.,  a  former  mili¬ tary  punishment  in  which  the  offender  was  com¬ pelled  to  run  between  two  files  of  men  who  struck him  with  switches,  clubs,  etc.,  as  he  passed.  — Formed  under  the  influence  of  gauntlet,  ‘glove’, fr.  earlier  gantlope,  fr.  Swed.  gatlopp,  lit.  ‘a  run¬ ning  down  a  lane’,  a  compound  of  gala,  ‘lane’, and  lopp,  ‘a  running,  course’,  which  is  rel.  to Swed.  lopa,  ‘to  run'.  The  first  element  is  rel.  to ON.  gata,  ‘road’ ;  see  gate,  ‘passage’.  For  the second  element  see  leap, gantlet,  n.,  a  glove.  —  See  gauntlet, gantry,  also  gauntry,  n.,  1)  a  wooden  frame  for barrels;  2)  a  spanning  framework.  —  OF.  gan¬ der,  chantier  (F.  chantier),  ‘timber  yard’,  fr.  L. cantherius,  ‘a  gelding;  trellis;  rafter’,  fr.  Gk. xav&TjXto?,  ‘pack  ass’.  Cp.  chantier,  shanty. Ganymede,  n.,  a  beautiful  boy,  cupbearer  to  Zeus (Greek  mythol.)  —  L.  Ganymedes,  fr.  Gk.  Favu- |j.r|87)4,  lit.  ‘rejoicing  in  his  virility’,  compounded of  yivuixat,  ‘I  am  glad,  rejoice’,  and  fXTjSea (pi.),  ‘counsels,  plans,  cunning’.  For  the  first element  see  ganoid.  The  second  element  is  rel. to  |rr)8e<jffai,  ‘to  devise,  resolve,  advise’,  p£8cov, [xe8£tuv,  ‘guardian,  ruler’  (prop.  pres,  part  of  the ancient  verb  piSeiv,  ‘to  prot
```


### [2026-09-05T21:03:03.909Z] TOOL RESULT

```
5972:Sheisdo, ið (heid-) — ghengh-
6000:$hengholos (ghenghris) — gheubo, ið
6107:WP I, 588. Cf. ghengh- Skt. jánghā ‘lower leg’; janghā-, cpds. “of feet’; Oss. zäng ‘shin; mountain-range'; Go. gagg; MHG ganc, gs ses OE gang; ON ganer, cf. ganga, sv. 7 ‘go’; gengr ‘able to walk’; Li. cf. í-Zanga ‘introduction’; Zangüs “fleet-footed?. (Isophonic: Hindi jhanjhi ‘shell’: Gk. kógkhē, id.)
7005:keng- 'seize, grip, hold; hold, hook, grapple, hobble'. Cf. knk- Av. cf. Caro ‘claw, cleft hoof; Per. Gäng ‘claws, fingers”, cf. also čängāl, čängul ‘claws, hook’; Lat. cingo, Gre “tie; gird” beside cingulum, cingula (LW in Ir. ceangal ‘tying, binding, ceanglaim, v.id., and in W cengl, f. “band; girth; hank’; cenglu “bind'); ON hinkr, n. (delay', fr. *kengro-); Sw. hink, pl. at m. “lever, bascule, well-swipe" (?); cf. also (?) OHG hinkan, ON hinka (*limp', though in view of the Swedish doublet skinka, id. usu. refd. to type kseng-, q.v.); Slovak Ciahat, Ciahnut' ‘seize’; Li. cf. kenge ‘hook’
8155:kseloksos, kseluqusos, à ‘shell, busk, bark, peeľ. Variant: skel-. Cf. WP II, 591. (Basic formula uncertain) Arm. xayax, o-st. “hide, skin’; Lat. siliqua “shell; pod, husk’; Ir. cf. scilice ‘husking of corn’; R Seluxà ‘peel, husk’; Séluxi, Soluxi, pl. ‘scab, mange’. (Lat. silex ‘flint and Ofr. scelec ‘rock’, Ir. sceilg ‘reef, cliff suggest a parallel phonology, but IE ks- is normally = Ir. c-, cf. ksengið). (Cz. šešule ‘shell, pod, husk’ suggests metathesis)
8160:ksengió (skeng-, skng-) limp, pace, amble’. Cf. WP I, 588 & II, 564 Skt. kháfijami ((limp', fr. *ksen$-); Per. cf. xing ‘white horse’; xinga, adj. ‘able-bodied’; (zero-gde in) xazidan, inf. ‘crawľ (*ksn&-); and in Gk. (variant: *sk-) skázo ‘limp’; MIr. cin- gim ‘go, walk’; 3sg. pf. cechaing; Sw. skinka, inf. ‘limp’; R Sag, m. ‘pace’; Sagàt, Sagnüt, inf. id. Gaul. cf. -cengo-, cing-, Sequanian: -cingos ('gait, path” or sim.)
8167:ksengið (skeng-, skng-) — kseubh-
15566:sken£- (skn£-) “bend, curve, hook; be bent, be crippled, hobble’. WP II, 564 Skt. kháfijami, v. ‘limp (ambig.? *kseng-); Sw. skinka, v. id.; Arm. cf. xinc, gs: xnco, ab. s. xncov, s. ‘fold, bosom, hollow’; OE scincio “renal fat”; (z-gde in) Per. xazam, -idan, v. ‘creep’; Gk. skázo, v. ‘limp’; Oss. Kádz, adj. ‘bent’; OFris. skunka, wm. ‘shank, thigh’; Du. schonk, f. *bigbone'; ON skukka, f. “fold, crease, wrinkle’: Sw. skunk, pl. ar m. id.; cf. G schunkeln, v. ‘rock’; ON skykkjum, dat. pl. as adv. ‘tottering’. Cf. skn$- as a separate entry, and WP I, 588. Per. from a variant "ksng-.
15733:sknéo, ið “bend, go, creep’. Cf. kseng- Per. xazam, -idan, v. ‘creep’; Gk. skázó, v. Jimp'; ON cf. skykkjum, adv. (from a dat. pl. ttotteringly); G cf. schunkeln, v. rock
```


## [2026-09-05T21:03:18.675Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (5972,6000,6107,8155,8160,8167,7005):\n    pre='\\n'.join(lines[:ln-1])\n    print(ln,'leaf0=',pre.count('\\f'))\nEOF"
}
```


## [2026-09-05T21:03:19.458Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6095,6115p' IEC.txt; echo \"=== ksengio ctx\"; sed -n '8150,8170p' IEC.txt"
}
```


### [2026-09-05T21:03:20.489Z] TOOL RESULT

```
5972 leaf0= 239
6000 leaf0= 240
6107 leaf0= 244
8155 leaf0= 324
8160 leaf0= 324
8167 leaf0= 325
7005 leaf0= 279
```


### [2026-09-05T21:03:20.533Z] TOOL RESULT

```
422
$hoidh- (2) (?). Cf. dheigh-, dhoigh-
Ir. cf. gaoidhean ‘bluish clay’; Li. žiedžiù, Ziésti (‘shape — clay, etc.); ZiédZius "potter: z-gde in OCS zídi wall Cz. zeť, id. beside zdit, v. “wall up?
&hol- (8holos, -es-) (1) ‘green, greenery, greenstuff. Cf. ghel-, &holtos and gheleuos. WP I, 625 Skt. harih ‘yellow’; Av. zairis, adj. id.; LLat. holus, pl. -era ‘green vegetable’; Li. žalias ‘green, raw”; žalis, io, m. ‘greenness’; Zalesos, Zalesiai “green, green mould’; žalesà, f. ‘green- ery, greens’; Latv. zaļš, adj. ‘green, raw^; OPr. zalis, zolis ‘weed’
&hol- (&holn- gheln-) (2) “gall, bile’. Cf. 2hol- (1) and ĝhel-. WP I, 624 Gk. khólos, kholë, id. cf. s-kholë “freedom from bitterness’, hence “leisure” (cf. Ks-, eKs-); e-gde in Lat. fel, gs fellis; OHG cf. galla, OE gealla; ON gall, id. (Isophones: Srb. zolja ‘wasp’; Li. Zalà ‘harm’; Av. cf. zaronu (2) 'anger)
ĉhol- (3) (?)
R zolà 'ash, ashes’; Pol. zoła ‘lye, buck’; Li. žălas ‘red-brown’
ĉholg-, see ĝhalg- and cf. WP I, 540
Sholtos, ios, io (&hlt-) “yellow, green". WP I, 625. Cf. ghel-, &hol- (1) and gheleuos Oss. zäldä ‘greensward’; OCS (and com. Sl.) zlatü ‘golden’; zlato, n. ‘gold’; Li. žaltys, gs -čio ‘adder’ beside žalsvas ‘green’; Latv. zaltis, zalktis ‘grass-snake’
$hongholos (-õlos, -ilos) “going, mobile, via-
ble; goer’. Cf. £hengh- Skt. cf. janghalah, 'swift-footed'; Arm. (?) cf. dzandzay (w. assimilated consonants? ‘shal- low’); MHG gengel ‘wide-ranging’; LG gángel ‘rocker on cradle’; ON gọngull ‘restless, mobi- le’. See next
êhonghos, à ‘going; gait, pace, stride, leg’.
WP I, 588. Cf. ghengh- Skt. jánghā ‘lower leg’; janghā-, cpds. “of feet’; Oss. zäng ‘shin; mountain-range'; Go. gagg; MHG ganc, gs ses OE gang; ON ganer, cf. ganga, sv. 7 ‘go’; gengr ‘able to walk’; Li. cf. í-Zanga ‘introduction’; Zangüs “fleet-footed?. (Isophonic: Hindi jhanjhi ‘shell’: Gk. kógkhē, id.)
423
£hor- (ghoros, à) (1) ‘shine, light, ray, beam’. Cf. gherio Slovene zor, zora ‘red of dawn’; Srb. zora ‘dawn’; Li. Zarà, id. beside (archaic) Záras ‘sun- flower’; Latv. zars (2) ‘ray, beam’
hor- (ĉhoros) (2), “line, series, troop’
Gk. khorós ‘round dance’; Li. žãras “line,
troop’; phr: sàvo Zar, “in its turn, on the
other hand’. (Isophonic: Skt. jahra ‘waterfall’) $hordh-, ghort-, see Supt. 2h-
$hornos, à, us ‘gut, string, cord". Cf. WP I, 604 Br. cf. gor, pl. goriju ‘yarn’; OHG garn; OE gearn:Du. garen, id. beside garen, adj. "of yarn, of thread’; ON garn ‘yarn’ beside gorn, pl. garnir, f. ‘gut’; Li. Zarnà ‘gut’; Latv. zarna, id. (Kinship with Lat. hernia and haru-spex uncertain)
8houono- ‘casting, pouring’. See $heu-, 8heumn-, 2huuó, etc. WP I, 563 Skt. hávanam “offering”; Arm. dzawn, i-st “gift, dedication’; Gk. khóanos ‘furnace, crucible’; khoánë ‘hopper, dish, furnace’. Alb. cf. dhun- tí ‘gift. See next
=== ksengio ctx
ksauk- ‘wild, untamed’ Lat. saucius, adj. ‘hurt, cut, drunk, disabled’; Li. cf. Siáusties, v. ‘rage’; Latv. šaust, v. ‘flog’; cf. šausis, adj. ‘wild, awful’
ksaul- (1) ‘twisted, bent; twist’, etc. Skt. khoráh ‘lame’; Cz. choulet, choulit se, inf. ‘writhe, twist’. Long z-gde in Cz. chylit se ‘de- viate'
ksaul- (2) ‘raving, mad, silly’. Cf. Ksaul-. Some of the evidence is ambig. Per. Sul ‘feeble’ beside Sür-, cpds. “mad”, cf. Sülidan, Suridan, v. ‘rave’; Arm. xawl, -i, -av "mad: MIT. suaill ‘petty’; Cz. cf. choulostivy ‘touchy’; Latv. Sauls ‘silly’ beside Sausls ‘frivolous’. The variant *Ksaul- arises in Gk. saülos 'effemi- nate, dainty’; OCS suléti, suliti si ‘swagger’. (A Slavonic isophone occurs in OCS xula 'slan- der”; po-xuljo, iti *vilify, abuse"; Srb. hulim, iti, id.; R xulit ‘blame’; xulà ‘blame’: Srb. hula *calumny?)
ksauros ‘fragile, crumbly’. Evidence ambig. Skt. khoráh “lame? is prob. fr. ksaul- (1), q. v.; Sw. skör ‘crumbly, overripe, friable’; Cz. cf. churavy, dial. chury ‘ailing’
kseió ‘tie, bind". Cf. ksetos Skt. khayami ((1) ‘fix’. For (2) ‘strike’, see quseio); Hitt. sxiya(mi), sxai 'tie; gather; pledge’; cf. sxaminan, acc. "cord": OCS šija, ‘neck’; Cz. šíje ‘nape’
kseloksos, kseluqusos, à ‘shell, busk, bark, peeľ. Variant: skel-. Cf. WP II, 591. (Basic formula uncertain) Arm. xayax, o-st. “hide, skin’; Lat. siliqua “shell; pod, husk’; Ir. cf. scilice ‘husking of corn’; R Seluxà ‘peel, husk’; Séluxi, Soluxi, pl. ‘scab, mange’. (Lat. silex ‘flint and Ofr. scelec ‘rock’, Ir. sceilg ‘reef, cliff suggest a parallel phonology, but IE ks- is normally = Ir. c-, cf. ksengið). (Cz. šešule ‘shell, pod, husk’ suggests metathesis)
kseluos ‘bent, crooked, lame’. Cf. skoluos Skt. kharvah, id.; Arm. xey, id.; Per. šal *para- lytic’; Tokh. cf. śālyi, B $walyai “left-handed; Br. (?) welš (for *chwelš? “lame, hemiplegic’; OHG scelah, gs scelawes 'crosseyed'; OE
-secol, cpds. sceolh- 'squinting; askew' (see
511
FK: EWDS: schielen). (For a parallel conso- nantism, cf. Lat. silus ‘with upturned nose?)
ksengió (skeng-, skng-) limp, pace, amble’. Cf. WP I, 588 & II, 564 Skt. kháfijami ((limp', fr. *ksen$-); Per. cf. xing ‘white horse’; xinga, adj. ‘able-bodied’; (zero-gde in) xazidan, inf. ‘crawľ (*ksn&-); and in Gk. (variant: *sk-) skázo ‘limp’; MIr. cin- gim ‘go, walk’; 3sg. pf. cechaing; Sw. skinka, inf. ‘limp’; R Sag, m. ‘pace’; Sagàt, Sagnüt, inf. id. Gaul. cf. -cengo-, cing-, Sequanian: -cingos ('gait, path” or sim.)
ksërið (1) ‘dry, parch, wither; turn dry, etc. Cf. kseros (1). WP I, 503 Skt. ksáràmi (2) ‘perish’; Arm. cf. xarem (‘sear, brand”, fr. *ksor-2); Per. cf. xirman “barn, threshing-floor'; Gk. cf. kseraino ‘dry’; Lat. seresco, Gre “dry in the sun; get dry’; Li. Seri- uos, -uotis (^wither', intrans.); Latv. seru, sert *dry (grain) in kiln?
ksérió (2) *ill-use, abuse". Cf. kseros (2) Skt. cf. ksaritah (2) 'abused'; Alb. shorr *squeeze'; Pol. szarzac, inf. “abuse, bully, tor- ment
kserom (?) “fluid? Skt. ksaram (water; Lat. (ambig.) serum ‘whey’ (equates equally with Skt. sáras, n. “fluid, water”. See seros, om)
kséros (1) ‘parched, scorched, arid". WP I, 503. Cf. kserió (1) & next Skt. ksarab ‘caustic’ beside Hindi khar, f. ‘grass’; Per. cf. xirman ‘barn, threshing-floor'; Arm. cf. xar, i-st. (hay, fr. *ksor-?); xaran, i, av ‘burn, cautery, stigma’; Gk. kserón “dry land”; kserós ‘dry’; Lat. cf. seresco ‘get dry’, beside serenus ‘dry, of weather’; Li. cf. Saras, m. ‘dry fodder’ beside šērà, id.; Latv. sers “dried corn’; cf. also sere, seris ‘sandbank’
kseros (2) (quseros ?) “sharp, harsh'. (Same as (1)? The alternative initial is suggested by Gk. psorós (rough?) Skt. khárah, kharuh 'rough, harsh'; Oss. cf. áxsálí ‘Juniper’; Tokh. A tsår, B Scire trough, hard’; R cf. Sero-xovatyj ‘rough, rugged’; Ukr. Sory, pl. ‘barbs’. Long-gde in R o-šaràšiť ‘dumbfound’
kserp- (?) ‘roughness, rough surface’ Lat. cf. (?) sirpus, scirpus ‘rush, mat, fish-
ksengið (skeng-, skng-) — kseubh-
15
20
25
```


## [2026-09-05T21:03:40.482Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^[0-9]\\{3\\}$\" IEC.txt | awk -F: '$1>5900 && $1<6200' ; echo \"=== around ksengio\"; grep -n \"^[0-9]\\{3\\}$\" IEC.txt | awk -F: '$1>8050 && $1<8300'"
}
```


## [2026-09-05T21:03:41.607Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ĝhengh\\|^&hengh\\|^£hengh\\|^ghengh\\|hengh-, \\|hengho\" IEC.txt | head -20"
}
```


### [2026-09-05T21:03:42.505Z] TOOL RESULT

```
5916:410
5929:411
5950:412
5964:413
5980:414
5989:415
6008:416
6018:417
6039:418
6051:419
6068:420
6079:421
6095:422
6108:423
6132:424
6141:425
6155:426
6165:427
6185:428
6192:429
=== around ksengio
8054:562
8061:563
8077:564
8086:565
8101:566
8109:567
8123:568
8131:569
8148:570
8158:511
8175:572
8183:573
8199:574
8209:575
8226:576
8249:578
8260:379
8275:580
8284:581
```


### [2026-09-05T21:03:42.567Z] TOOL RESULT

```
2802:dhenguho (2) ‘bang, beat, force, thrust. Variant dhengh-, cf. dhngh- (1) Ir dingim ‘thrust, crush, oppress’; ding ‘wedge’; ME dingen, sv. 3. “throw; beat’; E dial. to ding in ‘insti’; O-gde in Sw. dänga ‘strike’; ON *dengja, beside OSw. diung- (fr. *dhenguho), id.; W. R cf. djaglyj ‘strong; of uncertain mng. in Ukr. v-djahnutysja; Latv. cf. (ambig.) diedzu, diegt (2) ‘rusk’
3006:dhongheio ‘bang? Cf. dhenguho, dhengh-, dhngh- Oss. cf. dáng! 'bang'!; ON dengja; Sw. dänga, Norw. denge (“beat, hammer, sharpen by ham- mering’, etc.); cf. MHG tengeln “hammer”
5991:$hengholos (ĉhenghris) (?) ‘viable’. $&hengh- Skt. janghilah *quick'; Arm. cf. dzandzay (?) (shallow, fr. *&hengh-); Gk. cf. kegkhrís? (lit, ‘swift? as epithet of a hawk, a serpent, and a river); G Gingel (*weakling, sot Isophonic, but semantic link obscure); (Eng. gangling o- gde, appears to be a modern formation)
6000:$hengholos (ghenghris) — gheubo, ið
```


## [2026-09-05T21:03:47.831Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5978,5995p' IEC.txt"
}
```


### [2026-09-05T21:03:47.872Z] TOOL RESULT

```
40
45
414
Bhlk- Phryg. zélkia *vegetables': Blg. cf. zlak *grassy spot; R zlaki, pl. “herbs, grass?
$helmen- (ghelimen-) ‘yellowness; green- ery’. Cf. ghel-, etc.
Skt. harimán ‘yellowness’; Li. Zelmuo, eps ‘sprout’; Latv. zelmenis 'stubble-field turned over to grass’; zelme 'greensward'
&heltos (gholt-, &hlt-) “yellow, gold’. See £hel-, etc. & cf. WP I, 625 Per. zard ‘yellow’; Go. gulp (z-gde: “gold? and com. Gmc.); OCS zlato (fgold', and com. SI.); R zóloto, id.
Shelüs (&heluis, ĝheluə) ‘tortoise’. See ghelus and cf. WP I, 631 Gk. khélus; OCS zelvi (sic) beside žíly, gs Zilü- ve, id. (and *goitre"); Cz. želva, wd: LW in Li. Zelvys, id. beside Zelvé
$heluos (gheleuos, ghelsuos), variant of type gheleuos, q.v. WP I, 624 Arm. cf. (?) on-dziwy, o-st. (shoot, bud’, ? fr. *andho-^); Ir. cf. geolbhach ‘gills’; OHG (am- big.) gélo, gs gélawér, OE geolu, geolwes, adj. ‘yellow’; Li. Zelvas ‘greenish’ beside gelsvas “blond” and o-gde žalsvas ‘greenish’.
&hem- (ghom-, 8hm- with u-basis) “ground, earth; on the ground, on (to, in) the ground, down". WP I, 662 Av. zom, f.; Per. cf. zamin, id.; Hitt. cf. gimras *countryside; campaign'; Thrac. cf. zémele- “low fellow, captive, slave’; Cypro-Myc. (que- ried) kham-, cons. decl. ‘land’; Gk. cf. khamaí “on the ground’; Siculian hemitom (queried: “of clay); Lat. humus, gs -1, f. (u-basis); Umbr. cf. hun-tru ('down', fr. *&hm-tero-, compara- tive); OCS zemlja, f.; Cz. země “land, ground”, na zem ‘to the ground’; na zemi (on the. . .); R nà-zemí *down, on the ground"; Li. Zéme, beside Zémas, adj. lowlying'; Zemýn *down- ward’; Zemai “on the ground’; Zemiaü *down- ward'; Latv. zeme, beside zem, prp. “under”; zemē ‘below’; zemi, zemu, adv. lowlying'
$hengh- ‘go, pace, step’. Cf. ghongh-. WP I, 588 Skt. janh-, v. (radical: “dash along); jangha “lower leg’; jangha-, cpds. ‘quickly’; janghilah, adj. ‘quick’; Av. zafigo ‘upper of foot’; Per. jan- gam ‘fight, wage war’; Tokh. B tsánk-, tsenk-
415
‘rise’; OHG gingo, wm. ‘desire’; MHG ginge, wm. ‘demand’; (O-gde in) ON gengr, adj. “able to walk’; OCz. záhé, Cz. záhy ‘soon’; Lusat. zahi, id. beside zašo “earlier”; Li. Zengiü, “ti “go, pace, move’
$hengholos (ĉhenghris) (?) ‘viable’. $&hengh- Skt. janghilah *quick'; Arm. cf. dzandzay (?) (shallow, fr. *&hengh-); Gk. cf. kegkhrís? (lit, ‘swift? as epithet of a hawk, a serpent, and a river); G Gingel (*weakling, sot Isophonic, but semantic link obscure); (Eng. gangling o- gde, appears to be a modern formation)
$her-, gher- ‘take, get, receive; gift. See ĉhërs ‘hand’. (For gher- ‘wish’, see gherios) Skt. harah, adj. ((taking', etc.); háram ‘take, offering"; harah, ih, adj. = harah, adj.; s. “string of pearls’; haras, n. ‘grasp’; Av. zar- ‘seize, take’; zaro, obl. -àh-, n. ‘respect; Arm. dzir, gs dzri, i-st “gift”; an-dzir, adj. *'un-fruitful ; Gk. cf. synth. cpd. ktérea, pl. legacy, obsequies’; Lat. cf. hér-és, -edis, gs (heir; owner’, cf. éd- "eat?
?herdho, extn. of 2her-, q. v. ‘clasp, embrace’ Gk. cf. kérthios ‘nuthatch, creeper-bird’; Go. gaírda ‘belt’; bi-gaírdan ‘gird’; ON gjoró ‘gir- dle, girth-belt'. (G Gürte is z-gde)
gherió (£hereio) (?) “shine, appear, look’. Cf. ger-, 201-. Evidence ambiguous Lat. cf. hirquus, i, m. (hapax: “corner of the eye’. Virg. Ecl. transversa tuentibus hirquis, for *&her-oquos, w. Sabine *-e-? Cf. Cz. zrak “sight, eye’, fr. *&hor-oquos?); Li. (ambig.) Zeriu, eti (/shine'. See ĝēr-)
Sher-nigu *wash-hand basin’. See ghérs and nigu-
```


## [2026-09-05T21:04:04.337Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T21:04:04.343Z] TOOL RESULT

```


```


## [2026-09-05T21:04:06.180Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN jang\"; grep -n -i \"jang\\b\\|jang \" HRN.txt | head -15; echo \"=== HUB zang/jang\"; grep -n -i \"jang\\|zang \" HUB.txt | head -15; echo \"=== PHD jang zang\"; grep -n -i \"^jang\\|^zang\\|jang \\|zang \" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-05T21:04:06.253Z] TOOL RESULT

```
=== HRN jang
=== HUB zang/jang
4792:zu avextan 'hUngen' ; azang Talte* zu cin *Falte' von Wrzl. c7,
=== PHD jang zang
PHD.txt:412:J jad [y’t'] share, portion. Yadag [ytk! | M jdg] omen. tļadaģ [ytk'] form, property. jadag [y’tk' | M del share, portion; case, cause. jadag-g5(w) [y tkgwb'] advocate, intercessor. ~ЛЬ : intercession. jadag-wihīrih [ytkwhylyh] transformation, alteration. Jadarih [y2?lyh] maintenance. *fadisn [ytsn'] (accidental) quality, property. ~ig [-yk'] accidental, non-essential. jadiig [y?te&! | M j?dwg, N jadi] sorcerer, magician. — h: sorcery, magic. *jay [у?л | N ~] sissoo tree. jagar [yal | N jigar] liver. Jah-, v. jastan. jahišn [yhysn' | J jhysn-] chance, fortune, omen. Jahišn-ayār [yhyfn hdyb'l | N n. pr. jhiy?r] fortunate. ~ih: good fortune. jahüd [yhwt' | N juhiid] Jew. jām [y m | N ~] glass. јат [M ANE < A mn-h; ут | M Pm, N <] vessel, goblet. lfamag [y”mk! | N јата) = *jām. атар [y mk! | М ртр, N fama] clothing, garment. jang [yng | M jnng, N ~] struggle, battle, fight. Jar [ywl | M рт] time, occasion. jastan, jah- [ystn!, yh-] happen, occur, chance (to be). ~išn, v. jahišn. Jašn [yfn! | N —] celebration, festival. jaw [ŠZ < A £% | N ~] barley. Jāwēd [y wyt! | (P ywyd), N ~] eternal.
PHD.txt:426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
PHD.txt:677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
PHD.txt:4996:kulang kirrdg sett kargās karkēhan kark karm, kirm karmīr karb, kirb karafs karbunag karzang kardār
PHD.txt:5094:t fand zang zanih zandikih zandik zangīg zandag zandbed
PHD_mackenzie.txt:3249:·karzang [klcng I M kyrzng, (N xarcang)] crab; astr. Cancer.
PHD_mackenzie.txt:5768:zang [zng] ankle, shank.
PHD_mackenzie.txt:5769:zangig [zngyk' I N zangi] negro.
PHD_mackenzie.txt:9546:kabig                   '!.lQ)~       karzang              .:;\~~
PHD_mackenzie.txt:9788:anI                          §      zang                           :;~
```


## [2026-09-05T21:04:13.249Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%86%DA%AF",
 "prompt": "Give the full Persian etymology section for جنگ (jang) 'war, fight' — what Middle Persian, Proto-Iranian or PIE origin is given, and which sources are cited (Hasandust, MacKenzie, Cheung, Nourai)?"
}
```


## [2026-09-05T21:04:14.442Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%86%DA%AF",
 "prompt": "Give the Persian entry for خنگ (xang/xeng) — meanings (white horse?) and any etymology given."
}
```


### [2026-09-05T21:04:18.927Z] TOOL RESULT

```
# Persian Etymology for جنگ (jang)

## Origin Chain

The Persian word **جنگ** (jang) meaning "war, fight" traces back through:

1. **Middle Persian**: 𐫋𐫗𐫗𐫃 (jnng /ǰang/, "struggle, fight")
2. **Proto-Indo-European**: *ǵʰengʰ- (root meaning "to strike/slay")

## Cited Source

Only one reference appears in the provided material:

**MacKenzie, D. N.** (1971) - "A concise Pahlavi dictionary" (Oxford University Press), page 46, which documents the Middle Persian entry "ǰang"

## Note on Other Sources

The page does not cite Hasandust, Cheung, or Nourai for this particular entry's etymology, despite these being notable Persian etymological authorities.
```


### [2026-09-05T21:04:20.022Z] TOOL RESULT

```
# Persian Entry for خنگ

**Word:** خنگ (xing / xeng)

**Meanings:**
The entry provides two distinct etymologies with different definitions:

1. **Noun** – "horse"; also "white horse" or "gray horse"
2. **Adjective** – "dumb, stupid"

**Etymology:**
According to the source, the noun derives from Proto-Indo-European *ḱanḱest- or *kankest- (meaning "horse"). It shares cognates with Proto-Germanic *hangistaz and German "Hengst." However, the entry notes this etymology "Can this etymology be sourced?" indicating it requires verification.

The adjective etymology section contains no source information provided.

**Descendants:** The word produced Armenian խենգ (xeng) and Azerbaijani xing.
```


## [2026-09-05T21:04:28.518Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%AC%D9%86%DA%AF&action=raw\" -o jang.txt && sed -n '1,60p' jang.txt; echo \"=========== XANG\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%AE%D9%86%DA%AF&action=raw\" -o xang.txt && sed -n '1,70p' xang.txt"
}
```


### [2026-09-05T21:04:31.006Z] TOOL RESULT

```
{{also|جنګ|خنک|چنگ|خنگ|حنك|جنک|جنك}}
==Baluchi==

===Etymology 1===
{{ety|bal|:bor|fa-cls:جَنْگ|tree=1|text=++}}

====Pronunciation====
* {{IPA|bal|/d͡ʒəŋɡ/|[d͡ʒəŋɡ]}}

====Noun====
{{head|bal|noun|tr=jang}}

# [[war]]

===Etymology 2===
from {{inh|bal|ira-pro|*ǰántī}}, from {{inh|bal|iir-pro|*ǰʰánti}}, from {{inh|bal|ine-pro|*gʷʰénti||to [[slay]], [[strike]]}}. Cognate with {{cog|fa|زدن|tr=zadan}}.

====Pronunciation====
* {{IPA|bal|/d͡ʒə.nəɡ/ [d͡ʒə.nəɡ]}}

====Verb====
{{head|bal|verb|tr=janag|past stem|جت}}

# to [[hit]]
#: {{ux|bal|آئیءَ منا پہ سرگ '''جت!'''|tr=Áí'a maná pa sarag '''jat'''!|He hit me on the '''head'''!}}
# {{n-g|a [[light verb]] that derives verbs from nouns and adjectives}}

==Brahui==

===Etymology===
{{ety|brh|:bor|bal:جنگ<tr:jang>|tree=1|text=++}}

===Noun===
{{head|head=جَنْگ⁩|brh|noun|tr=jańg}}

# [[war]]

{{c|brh|War}}

==Persian==

===Etymology 1===
{{ety|fa|:inh|pal:𐫋𐫗𐫗𐫃<ts:ǰang>|tree=1}}
{{inh+|fa|pal|tr=yng|sc=Phlv}}, {{m|pal|𐫋𐫗𐫗𐫃|t=struggle, fight|ts=ǰang|sc=Mani}}).

====Pronunciation====
{{fa-IPA|jang}}

====Noun====
{{fa-regional|جنگ|جنگ|ҷанг}}
{{fa-noun|cls=جَنْگ|pl=جنگ‌ها}}

# [[war]]
#: {{coi|fa|[['''جَنْگِ''' داخِلی]]|tr='''jang'''-e dâxeli|civil war}}
# [[fight]]
# {{lb|fa|usually|_|informal}} [[dispute]], [[argument]]

=====Derived terms=====
* {{l|fa|جنگی|tr=jangi}}
* {{l|fa|جنگاور|tr=jangâvar}}
=========== XANG
{{also|خنک|چنگ|حنك|جنک|جنگ|جنك|جنګ}}
==Persian==

===Pronunciation===
{{fa-IPA|xing}}

===Etymology 1===
From {{der|fa|ine-pro|*ḱanḱest-}}, {{m|ine-pro|*kankest-|t=horse}}. Cognate with {{cog|gem-pro|*hangistaz}}, and thereby with {{cog|de|Hengst}}. {{rfv-etym|fa}}

====Noun====
{{fa-noun|cls=خِنْگ}}

# [[horse]]
#: {{syn|fa|{{fa-l|اَسْب}}}}
# [[white horse]]
#: {{syn|fa|{{fa-l|چَرْمَه}}|{{fa-l|اَلُوس}}}}
# [[gray]] horse

===Etymology 2===

====Adjective====
{{fa-adj|cls=خِنْگ}}

# [[dumb]], [[stupid]]

=====Descendants=====
* {{desc|hy|խենգ|bor=1}}
* {{desc|az|xing|bor=1}}

===Further reading===
* {{R:fa:Lazar|page=165b}}
* {{R:fa:Vullers|L|I|page=729a}}

{{C|fa|Horses}}
```


## [2026-09-05T21:04:40.227Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG gan/jan\"; grep -n \"jang\\|ǰang\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T21:04:40.268Z] TOOL RESULT

```
=== CHEUNG gan/jan
```


## [2026-09-05T21:04:41.643Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index\"; grep -n -i \"ghengh\\|ghen-\\|GNAW\\|GANG\" incoming/ARY/ARY_latin_index_pages.txt | head -20; echo \"=== ARY persian جنگ خنگ زنگ\"; grep -n \"جنگ\\|خنگ\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-05T21:04:41.696Z] TOOL RESULT

```
=== ARY latin index
12800:pn olen erly gle Ce gang 9 Cal enh cena op! slats Se dla! chasls ge Stel ;
14674:(esl gail ya" aad’ pe 44) Gangs Gasilyad ys PERSIAN) yyubb
=== ARY persian جنگ خنگ زنگ
81:در چند دهه‌ی قبل از جنگك جهانی دوم» برخی از دانشمندان اروپایی واژه‌ی» «آریایی» را نه
97:بهمین دلیل پس از شکست نازی‌ها در پایان جنگك جهانی دوم» واژه‌ی «آریایی» کمتر مورد
634:نظر شمار سخنگویان (بیش از یک میلیارد نفر) بزرگترین خانواده‌ی زبان‌های هند و اروپایی
731:سخنگویان به این زبان‌ها پیش از ۱۳۰ میلیون نفر است.
749:آثار فلسفی و تاریخ ی گوناگون. زبان یونانیکلاسیکه به ندریج تبدیل به یونانی نوین شد. سخنگویان
765:مرکزی و بخشی از امریکای شمالی بردند. امروزه شمار سخنگویان این زبان‌ها به حدود ۹۰۰ میلیون
769:۹4 نبنلت‌ها (79]ج) مردمانی جنگجو پودند که از حدود ۵۰۰ تا ۵۰ سال پیش از میلاد در
840:صربی» کرواتی» مقدونی). جمع سخنگویان به این زبان‌ها حدود ۴۵۰ میلیون نفر است.
914:(88 0۳ 8۸ 2مت 5- 070-7100 ۳3) هسند. مثلاً ویژگی‌های جنگجویان هند و
916:ویژگی‌های این جنگجویان از هند باستان گرفته تا آلمان» یونان و روم کهن چنین بوده است.
958:کشیشی و آئین‌های مذهبی بود. -تولوس هوستیلیوس (130571118 110178) که جنگاورخشن .|
962:خدایان و مظهر دين بود. «مارس» با «آریس» (۸388) خدای جنگه بود. «آبناء یا «سینرواء |
964:(روحانیون) و «کشاتریاه ۸ (جنگاوران) و «ویسیاء ۷۸/8۸ |
967:۱-روحانیون زرتشتی ۲- جنگاوران ۳- دهگانان.
985:کین‌تر همین کار را می‌کردند. مثلاً در داستان جنگ تروا آمده است که آقاممنون
1065:برده گیری جنگ و پیزووزی بر دشمن پود. نگهداری بردگان مرد مخاطراتی را بهمراه داشت. (شورش
1077:‎٩‏ رزمجویی: ویژگی دیگر هند و اروپائیان جنگاوری بود..مردمی که طی چند سده از
1079:را اشغال کردند نه تنها از پرتری فنی (اسب و ارابه) برخوردار بودند بلکه از نظر جنگجویی و
1083:می‌شد. در روم باستان» هنگام جنگ کشاورزان عادی تبدیل به سربازان ماهر می‌شدند. در اسپارت
1088:هند و اروپایی تنها بخاطر زمین و ثروت جنگ نمی‌کردند. انگیزه‌ی اصلی آنها بدست آوردن افتخار . !
```


## [2026-09-05T21:04:49.190Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON جنگ\"; grep -n \"جنگ \\[\\|جنگ(\\|(جنگ\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5; echo \"== MON خنگ\"; grep -n \"خنگ\" MON_part1.txt MON_part2.txt 2>/dev/null | head -8; echo \"== BQT خنگ\"; grep -n \"خنگ\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -10"
}
```


### [2026-09-05T21:04:49.293Z] TOOL RESULT

```
== MON جنگ
MON_part2.txt:17769:کارزار: ۲-28 کار (جنگ) + زار (س. 
MON_part2.txt:59618:(ا.) استحکامات. جر ثقیل (جنگی). تو بخانه. 
MON_part1.txt:34523:پوشش (جنگی) به رنگ پیروزه. 
MON_part1.txt:48699:جنگیدن: 1202-10 (مسص‌ل.) (جنگید» 
MON_part1.txt:59007:گیرودار؛ های‌وهوی (جنگ). 
== MON خنگ
MON_part2.txt:1641:(امص.) سخنگویی با زنان» عشقبازی. (اد.) 
MON_part2.txt:10967:سخنگو. گوینده شعر. اقرار کننده به خطای 
MON_part2.txt:25924:کلیم: «] [ع.] (ص.) سخنگو. هم سخن. 
MON_part2.txt:29134:کل زو تست بانید: رگک» گس مکر؛ خن خنگک 
MON_part2.txt:58838:مسصفع: "درو (ع.] (ص.) سخنگوی 
MON_part2.txt:62645:سخنگویی. (.) سخن» قول. فصلی از کتاب 
MON_part2.txt:72377:ناطق. سخنگوی. قوهٌ تکلم و بیان. نفس 
MON_part2.txt:89278:موی آن سفید باشد؛ اسب خنگ. 
== BQT خنگ
incoming/BQT/BQT_v3_pages.txt:15333:غمنده ۲ » بروزن زننده,بممنی‌خنگن
BQT_v1_pages.txt:944:-9811 (نتفی کردن) ۷۵1 (سخنگفتن ) آدر : آوا » آوازه‌نوا؛ واخت |
BQT_v1_pages.txt:1458:ز بان برای رسالت شایسته‌است . وچون هروی سخنگفت » وزیر گفت : این
BQT_v1_pages.txt:17254:بکی‌رااخنگهبت»ودیگربرا «سرخبت »میگفتهاند
BQT_v1_pages.txt:29400:آر خنگ۱۵ - بروزن شرمنده. بسعنی‌طننه
BQT_v2_pages.txt:4184: ‫چاره جوی » شاعر و سخنگوی باشد ‪٩٩-‬‏‬                      ‫دراز را بدست گیرنب و چوب کوتاه را بر زمین‬
BQT_v2_pages.txt:5336:    ‫بود » اکرخایه‬    ‫خنگضیف‬   ‫چرمه‪.‬‬    ‫‪« ۰‬اپ‬     ‫‪۴‬‬           ‫‪).. .‬‬    ‫(ه‬   ‫چربك‬   ‫مصحف‬       ‫‏‪- ١‬‬
BQT_v2_pages.txt:5779: ‫وستر که آبرا خنگك‬
BQT_v2_pages.txt:5812:     ‫‪ :‬خنگه‬     ‫رک‬    ‫‪۴‬‬                          ‫«چشنه»‪.‬‬     ‫‪ _ ۴‬ظ »صحف‬                               ‫جشم‬
BQT_v2_pages.txt:13540:                                                                      ‫را بادخنگوبند وخالة زکیشرتی را نیزخن (‪ | )۱‬انت ‪.‬‬
```


## [2026-09-05T21:04:55.608Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '89270,89285p' MON_part2.txt; echo \"=== BQT v2 5330-5340\"; sed -n '5325,5345p' BQT_v2_pages.txt; echo \"=== page tag\"; awk 'NR<=5336 && /\\[pdf page/ {p=$0} END{}' BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1<5336' | tail -2"
}
```


### [2026-09-05T21:04:57.322Z] TOOL RESULT

```
هدف‌گیری: [-۲ع-.۱ [ع. . ف.] (حامص.) 
به دقت نگریستن نشانه پیش از انداختن تیر و 
گلوله. 

هدم: (ع.] (مصم.) خراب کردن؛ 
ویران کردن. (امص.) خرابی» ویرانی. 
هدنگ؛: : ۱۵0208 [- - هدنج] (.) اسبی که 
موی آن سفید باشد؛ اسب خنگ. 

هد ۰4۱ (6-)۵00۵:ظ . . هدنه] (مص‌ل.) ۳ 
گرفتن. (امص.) آرامش» سکون. آشتی 
صلح؛ مق . نراع. 

هده: (60-)002 [- هوده] (.) حق؛ راست و 
درست؛؟ مقّ. بهده» هو ده. فایده. 
=== BQT v2 5330-5340
                  ‫رکه‬
                    ‫ضند‬
                      ‫غگوی‬
                         ‫چورندو را نز‬
‫چر نگ * ‪ -‬بکراول وثانی وسکون‬                          ‫را نگیوزبند‬          ‫نه‬
                                                                            ‫‪-‬و‬‫رجنمسی‬
                                                                                   ‫چد و‬
                                                                                      ‫کیرند از نق‬
‫کاف‌فارسی ‪.‬آوازی که‌سبب پی‌درپی زدن شمشیر‬                                         ‫که کرکاشی باشد ‪. ۳۴‬‬


    ‫بود » اکرخایه‬    ‫خنگضیف‬   ‫چرمه‪.‬‬    ‫‪« ۰‬اپ‬     ‫‪۴‬‬           ‫‪).. .‬‬    ‫(ه‬   ‫چربك‬   ‫مصحف‬       ‫‏‪- ١‬‬

    ‫وی وم و دست و پای و بوش وناصیه‌و دم سیاه بود نيك باشد ‪ « » .‬قابوسناهه‬                     ‫واء‬
                                                                                                ‫ورمیااننه‬
                     ‫‪ :‬مجاچنگ‪.‬‬    ‫رك‬   ‫‪_ ۴‬‬               ‫‪.‬‬   ‫>‬    ‫نوروزنامه ‪۷۱۱‬‬   ‫» تعلقات‬     ‫بنقل مینوی‬

    ‫_سم صوت ‪ .‬امروز ‪۹۲‬ز ‪.‬‬
                        ‫® ا‬                     ‫اسم فاعل از چربدن ‪ ,‬علف خوار ‪.‬‬                ‫‪۴‬‬
                                                                                    ‫بقبه از صفحهٌ ‪۳۳٩‬‏‬
    ‫ابنك شاهد افتزوحات مکه باحاء حطی‪ « :‬فنادی بمملوك وقاله جثنی بالحرمدان فقلت له ‪.‬اشان‬
=== page tag
```


## [2026-09-05T21:05:13.957Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for u in \"Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eng%CA%B0-\" \"gnaw\" \"gnat\" \"Reconstruction:Proto-Germanic/gangan%C4%85\" ; do echo \"########## $u\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$u&action=raw\" | head -60; done 2>&1 | head -160"
}
```


### [2026-09-05T21:05:16.615Z] TOOL RESULT

```
########## Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eng%CA%B0-
{{reconstructed}}
==Proto-Indo-European==
{{etymon|ine-pro|id=walk|pos=root}}

===Root===
{{ine-root}}<ref>{{R:gem:EDPG|page=166-7}}</ref><ref>{{R:ine:LIV|page=175-6}}</ref>

# to [[walk]]
# to [[step]]

====Derived terms====
{{rootsee}}

* {{l|ine-pro||*ǵʰongʰ-|pos=o-grade root present}}
** {{desc|gem-pro|*ganganą}} {{see desc}}
* {{l|ine-pro||*ǵʰengʰ-ye-ti|pos=ye-present}}
** {{desc|ine-bsl-pro|*źengjetei}}
*** {{desc|lt|žeñgti}}
* {{l|ine-pro||*ǵʰongʰ-i-s}}
** {{desc|gem-pro|*gangiz}} {{see desc}}
* {{l|ine-pro||*ǵʰongʰ-o-s}}
** {{desc|gem-pro|*gangaz}} {{see desc}}
* {{l|ine-pro||*ǵʰéngʰ-os ~ *ǵʰéngʰ-es-}}
** {{desc|iir-pro|*ȷ́ʰánǰʰas}}
*** {{desc|inc-pro|*ȷ́ánźʰas}}
**** {{desc|sa-ved|जंहस्|tr=jáṃhas}}
* {{l|ine-pro||*ǵʰéngʰ-o-s}}
** {{desc|iir-pro|*ȷ́ʰángʰas}} {{see desc}}
* {{l|ine-pro||*ǵʰéngʰ-tis}}
** {{desc|gem-pro|*ginhtiz}}
*** {{desc|gmh|gīht}}
* {{l|ine-pro||*ǵʰongʰ-tis}}
** {{desc|gem-pro|*ganhtiz}} {{see desc}}

===References===
{{reflist}}########## gnaw
==English==

===Etymology===
From {{inh|en|enm|gnawen}}, {{m|enm|gnaȝen}}, from {{inh|en|ang|gnagan}}, from {{inh|en|gmw-pro|*gnagan}}, from {{inh|en|gem-pro|*gnaganą|t=to gnaw}}, probably from {{der|en|ine-pro|*gʰnēgʰ-|t=to gnaw, scratch}}.

Cognate with {{cog|nl|knagen}}, {{cog|de|nagen}}, {{cog|da|gnave|t=to gnaw}}, {{cog|nb|gnage}}, {{cog|nn|gnaga}}, {{cog|sv|gnaga}}.

===Pronunciation===
* {{enPR|nô|a=UK}}, {{IPA|en|/nɔː/}}
* {{rhymes|en|ɔː|s=1}}
* {{enPR|nô|a=US}}, {{IPA|en|/nɔ/}}
* {{enPR|nä|a=cot-caught}}, {{IPA|en|/nɑ/}}
* {{audio|en|en-us-gnaw.ogg|a=US}}
* {{homophones|en|nor|aa=non-rhotic}}

===Verb===
{{en-verb|+|+|+,gnew<l:dialectal>|+,gnawn<l:archaic>}}

# {{lb|en|ambitransitive}} To [[bite]] something persistently, especially something tough.
#: {{ux|en|The dog '''gnawed''' the bone until it broke in two.}}
#* {{RQ:Shakespeare Richard 3|I|iv|line=25|passage=Ten thousand men that fishes '''gnaw'd''' upon}}
# {{lb|en|intransitive}} To produce excessive anxiety or worry.
#: {{ux|en|Her comment '''gnawed''' at me all day and I couldn't think about anything else.}}
# To [[corrode]]; to [[fret]] away; to [[waste]].
#* {{RQ:Heywood Royall King|sig=E4|verso=1|page=41|passage=VVots thou vvho's returnd, / The unthrift ''Bonvile'', ragged as a ſcarre-crovv / The VVarres have '''gnavv'd''' his garments to the skinne: {{...}}}}

====Derived terms====
{{col|en|begnaw
|forgnaw
|gnawable
|gnawer
|gnawingly
|gnaw someone's vitals
|outgnaw
|ungnawed
|ungnawn
}}

====Related terms====
* {{l|en|nag}}

====Translations====
{{trans-top|to bite something persistently}}
* Albanian: {{t|sq|bren}}
* Arabic: {{t|ar|نَخَرَ}}, {{t|ar|قَضَمَ}}
*: Egyptian Arabic: {{t|arz|قرص|tr=ʔaraṣ}}
* Armenian: {{t+|hy|կրծել}}
* Aromanian: {{t|rup|arod}}
* Asturian: {{t|ast|royer}}, {{t|ast|roer}}, {{t|ast|ñascar}}
* Azerbaijani: {{t|az|gəmirmək}}
* Bashkir: {{t|ba|кимереү}}
* Belarusian: {{t|be|гры́зці|impf}}, {{t|be|глада́ць|impf}}
* Breton: {{t+|br|krignat}}
* Bulgarian: {{t+|bg|гриза́|impf}}, {{t|bg|гло́жда|impf}}
* Burmese: {{t+|my|တွပ်}}
* Catalan: {{t+|ca|rosegar}}
* Cebuano: {{t|ceb|kitkit}}
* Cherokee: {{t|chr|ᎠᏍᎪᎩᎠ}}
* Chinese:
*: Mandarin: {{t+|cmn|啃|tr=kěn}}, {{t+|cmn|咬|tr=yǎo}}, {{t+|cmn|噬|tr=shì}}
########## gnat
{{also|gnat|Gnat|gnát}}
==English==

===Etymology===
From {{inh|en|enm|gnat}}, from {{inh|en|ang|gnætt|t=gnat; midge; mosquito}}, from {{inh|en|gmw-pro|*gnatt}}, {{m|gmw-pro|*gnattu}}, from {{inh|en|gem-pro|*gnattaz}}, {{m|gem-pro|*gnattuz|t=gnat}}, from {{der|en|ine-pro|*gʰneHdʰn-}}, {{m|ine-pro|*gʰneHd-||to gnaw; scratch}}, from {{der|en|ine-pro|*gʰen-|t=to gnaw; bite; scratch; grind}}. Cognate with {{cog|nds|Gnatte|t=gnat}}, dialectal {{cog|sv|gnatt|t=mosquito}}, {{cog|de|Gnatz|t=scabs; rash; scabies; stinginess}}. Related also {{m|en|gnit}} and {{m|en|gnaw}}.

{{wp}}

===Pronunciation===
* {{IPA|en|/næt/}}
** {{audio|en|LL-Q1860 (eng)-Vealhurl-gnat.wav|a=Southern England}}
* {{rhymes|en|æt|s=1}}

===Noun===
{{en-noun}}

# A biting [[insect]], especially a [[mosquito]].
#* {{quote-book|en|year=1828|author=w:Thomas Keightley|title=The Fairy Mythology|volume=I|location=London|publisher=William Harrison Ainsworth|page=293|passage=[A]nd his servant was beside him with a fan to keep away the flies and '''gnats'''.}}
# {{lb|en|informal}} An annoying person.
#* {{quote-book|en|year=1971|author=[[w:Richard Carpenter (screenwriter)|Richard Carpenter]]|title=Catweazle and the Magic Zodiac|publisher=Puffin Books|location=Harmondsworth|page=115|text="Away thou whining '''gnat''', and trouble me not!"}}

====Derived terms====
{{col|en|box the gnat
|Clear Lake gnat
|fungus gnat
|gall gnat
|gnat bug
|gnatcatcher
|gnateater
|gnatless
|gnatlike
|gnatling
|gnatproof
|gnat's
|gnat's arse,gnat's ass
|gnat's chuff
|gnat's prick
|gnat-strainer|gnat-strain|gnat-straining
|gnat's whisker
|gnatty
|gnatworm
|gnatwren
|strain at a gnat
}}

====Related terms====
* {{l|en|gnit}}

====Translations====
{{trans-top|any small insect of the order Diptera}}
* Afrikaans: {{t|af|mug}}
* Agta:
*: Dupaningan Agta: {{t|duo|rahik}}
* Arabic:
*: Egyptian Arabic: {{t|arz|برغش|m|tr=barḡaš}}
* Armenian: {{t+|hy|մոծակ}}
* Bashkir: {{t|ba|серәкәй}}
* Bengali: {{t+|bn|ডাঁশ}}
* Bikol:
*: Central Bikol: {{t+|bcl|nuknok}}
########## Reconstruction:Proto-Germanic/gangan%C4%85
{{reconstructed}}
```


## [2026-09-05T21:05:31.645Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3795,3812p' BRT.txt"
}
```


### [2026-09-05T21:05:31.688Z] TOOL RESULT

```
•  j.  aibi-gajryli  Id£  'einzustimmen  in  — (Akk.),  anzunehmen':  'ya  dai^i  vUpä humatäia  „paitijicya  dai'iii  vispä  dusma- iäcä  . .  "ich  nehme  mir  vor  anzunehmen alles  was  gut  gedacht  ist  . .,  zu  unter- lassen alles  was  übel  gedacht  ist  . ."  Y. J/.17.
Zum  V.  'gar-.  —  Pü. :  ap:  girisnJA. j.  aiaii^äld  V.  8.  4;  li«s  'galB.
•  j.  aiwLgäma-  m.  r)  'Winter';  fra  hama (stL)  iocinte  aHa  'me  V.j.io;  —  hama.. °me  "während  des  Sommers  . .  im  Winter" F.  2jb;  V.5.4a,  75.45,  "-^.46,  47,  4^'\ $0,  j/,  103'.  3)  sva,  'Jahr':  hasannm •manqm  Yt().  lo;  ig.2^,  V.  2.41.
np.  vgl.  hoH-gäitt  'Zeit',  —  Pü. :  samasfän.  — I)  S.  Var.  und  Pü.
•  j.  aibi.giya-  Adj.:  s.  unter  aibi^gaya-,
•  j.  aiwi-ynixta- Adj.  (fem.  VJ-) 'angenagt, angefressen' :7«i'  nasus  °ta  sünö  v3  k?niß.- s^arö  vayS  vä  k^m/s^i^arö  {%A.)  V.  7. 30; —  'la  V.5.34PÜZ'.
KompE.  —  PPfP.  aus  einer  idg.  Basis  gkn^k- oder  ghHä^gk.  (S  Jj  11).  mit  .  «US  idg.  >.  Vgl. ahd.,  ags.  giiagaa  'nagen',  mit  a  aus  3.  Ij. auch  Tekssun  Wurzeleiw.  136,  Siebs  KZ._;/. 321.  (Wadstein  IF./.24  lässt  das iran. Wort ausser.  Betracht.)  —  Pü.;  apariat.
•  j.  aiwri.j'zärain  Absol.  'beim  Herzu- fiiessen':  ka(,a  x3  .  .  a/iam  yiJrqm(^V.) a'  "wann  werden  die  Wasserquellen  herzu- fliessend  fliessen?"  VtÄ  42.
Zum  V.  7;"af-;  Bthl.  1F.  Jl.   H'-
•  j.  aiwi.xiöi^e  Inf.  'zu  bewohnen': to/n  vanm  kirTnava  , .  narqm  aiwixs'  , . gavqm  gävayamm  ". .  zur  Wohnung  für die  Menschen  . .  als  Stall  für  die  'l'iere" V.2.25.
Zum  V,  iay-,  —  VgL  aiwijaelan-;  wegen  xs s.  unter  iay-  No.  3-  —  Pü. ;  mattän  apar  mäniin rii.
•  p.  abi-cariS-''  n. 'Weide,  Weideland' {?)'*: äyaäanä  .  .  niyäyärayam  kära/iyä  °ris gafyamäi  mäniyamca  .  .  lyädis  gaumSla'' . .  adiR^  Bh.  1. 14.
Zum  np.  V.  iarldan  'weiden';    s.   2U  <arSiia-.
—  ■)  Lesung  und  Bed.  unsicher.  Zu  der GIrPb.  2.  417  wiederholten  Zusammenstellung des  Wortes  mit  np.  bäwr  %.  bereits  BtüL. KL.  /.  19.  Oben  nach  FOV  ZDMG.  $4.  343- S.  auch  noch  Windischmann  ZSt.  127.
•  j.  ''aiwi.didissinna-  Adj.,  PPM. :  s.  kais-.  j
•  j.  aibi-}ar9tay-  £  'Preisen,  Preisgesang':
apqm  vatfulanqm  *°nitimca\.  6-2.11,70.
6;  7^.6;  —  aya  aibigara  aya  °ia  (LS.)''
```


## [2026-09-05T21:05:34.831Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && echo \"#### zang\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B2%D9%86%DA%AF&action=raw\" | grep -n -A6 \"==Persian==\" | head -40; echo \"#### gangster fa\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%DA%AF%D8%A7%D9%86%DA%AF%D8%B3%D8%AA%D8%B1&action=raw\" | head -30"
}
```


### [2026-09-05T21:05:37.362Z] TOOL RESULT

```
#### zang
2:==Persian==
3-
4-===Pronunciation===
5-{{fa-IPA|zang}}
6-
7-===Etymology 1===
8-Cognate with {{cog|ckb|ژەنگ}}, {{cog|kmr|jeng}}, {{cog|bal|زنگ|tr=zang}}, and with Iranian borrowings in {{cog|xcl|ժանգ}}, and Caucasian languages such as   {{cog|ka|ჟანგი}}, {{m|ka|ჯანგი}}.
#### gangster fa
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
```


## [2026-09-05T21:06:10.787Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/cenk",
 "prompt": "What etymology does Nişanyan give for Turkish \"cenk\" (war)? Which Persian/Middle Persian form, and any Old Iranian/PIE root?"
}
```


## [2026-09-05T21:06:12.561Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON گانگستر\"; grep -n \"گانگستر\\|گانگ\" MON_part1.txt MON_part2.txt | head -5; echo \"== SKT gnaw/gnat/gang\"; grep -n \"^Gnaw\\|^Gnat\\|^Gang\\|^gnaw\\|^gnat\\|^gang\" SKT.txt | head -10"
}
```


### [2026-09-05T21:06:12.628Z] TOOL RESULT

```
== MON گانگستر
MON_part1.txt:3535:سعرفت» انس؛ مستق. بیگانگی» غریت. 
MON_part1.txt:6725:یگانگی کردن. (اسص.) یکك رنگی» 
MON_part1.txt:6726:یگانگی» یکدلی» یک جهتی. موافقت» 
MON_part1.txt:7297:بیگانگان. 
MON_part1.txt:7629:خود را رها کند و به سود بیگانگان دست به 
== SKT gnaw/gnat/gang
7704:gnaw,     A.  S.  gnagwt^  to  gnaw  ;
```


### [2026-09-05T21:06:14.993Z] TOOL RESULT

```
I cannot provide the etymology information you're requesting based on the content shown. The web page excerpt contains only the header, navigation menu, and footer of Nişanyan Sözlük (Nişanyan Dictionary), but does not include the actual dictionary entry for "cenk" or its etymological details.

To find the etymology of Turkish "cenk," you would need to access the full entry on the Nişanyan Sözlük website directly.
```


## [2026-09-05T21:06:19.845Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7700,7712p' SKT.txt; echo \"=== gnat\"; grep -n \"gnat,\" SKT.txt | head -3; echo \"=== gang\"; grep -n \"gang,\" SKT.txt | head -5"
}
```


### [2026-09-05T21:06:19.911Z] TOOL RESULT

```
cnick.+G.  hsasUrHt  to  cra<;kle.  O.  Gadr cnac^  to  crack,  cra^  ;  allied  to  Greek.
Onat  (£.)  A.  S.  ^rtat.  Said  to  b« named  fiom  the  whimng  of  the  wings; cf.   Iccl.  giuUa^  to  clash,  gnat,  cla&h  of
WraiMJUS-
Onavr,  (E.)    M.  E.  gnavKti.  pt.  t,  rw^
gnaw,     A.  S.  gnagwt^  to  gnaw  ;
'Mern*,ihegr-hc'mgApTeftTt  +f  ■
OlceLind^,  mod.  Iccl  «  :
Swed.  jvu^^     Without  tt  .
ftagen,  Dan.  n<?^^.  10  gunw.  .:^>vj.  ■.M^a-,
prov.  E.  nag.  to    worry.     Sec  NaQ.
nag  (i),  to  worry,  teajse.  i..Scai)d  )  ^wti.
nagga,  to  nibble,  peck ;   Daju  iwgft  kdl
nagn,  to  gnaw  ;  see  above, Gneise,  a  rock.  (G.)    G.gnrin, Qnome,  a  kind  of  sprite.    (F.  «*  Ck)
=== gnat
7701:Onat  (£.)  A.  S.  ^rtat.  Said  to  b« named  fiom  the  whimng  of  the  wings; cf.   Iccl.  giuUa^  to  clash,  gnat,  cla&h  of
=== gang
18394:I  ^ffer.     Der.  ptestgang,
```


## [2026-09-05T21:06:20.773Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gangster",
 "prompt": "Give the etymology of gangster and of gang (noun) as Etymonline states, including dates and the Old English/PIE background."
}
```


### [2026-09-05T21:06:27.359Z] TOOL RESULT

```
# Etymology of Gangster and Gang

**Gangster (1896)**
The term emerged in American English as "member of a criminal gang," formed by combining *gang* + the suffix *-ster*. An earlier political usage appeared by 1886, referring to "member of a clique in control of the local government."

**Gang (noun) - Origins**
The word traces back to Old English *gang* meaning "a going, journey, way, passage," and Old Norse *gangr* meaning "a group of men, a set." These derive from Proto-Germanic *\*gangaz*, likely from the PIE root *\*ghengh-* meaning "to step."

**Semantic Evolution**
The meaning progressed from "a set of articles taken together" (mid-14c.) to "a company of workmen" in nautical contexts (1620s), then developed disapproving connotations as "any band of persons traveling together" and eventually "a criminal gang or company" by the 1630s. By 1855, it specifically denoted "group of criminal or mischievous boys in a city."

The suffix *-ster* originally functioned as a feminine agent noun in Old English before becoming a genderless agent noun forming words like *gamester* and *roadster*.
```


## [2026-09-05T21:06:35.212Z] TOOL CALL #47: WebSearch

```json
{
 "query": "Persian \"jang\" etymology Middle Persian ǰang Parthian \"*ǰan-\" strike Hasandust ریشه جنگ"
}
```


## [2026-09-05T21:06:38.435Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -s \"https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/g%CA%B0en-&action=raw\" | head -40; echo \"###### gwhen\"; curl -s \"https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-&action=raw\" | head -30"
}
```


### [2026-09-05T21:06:42.534Z] TOOL RESULT

```
Web search results for query: "Persian "jang" etymology Middle Persian ǰang Parthian "*ǰan-" strike Hasandust ریشه جنگ"

Links: [{"title":"(PDF) From Middle to New Persian: written materials from Northern Iran and Khorasan","url":"https://www.researchgate.net/publication/353096921_From_Middle_to_New_Persian_written_materials_from_Northern_Iran_and_Khorasan"},{"title":"Persian Online – Grammar & Resources » Middle Persian","url":"https://sites.la.utexas.edu/persian_online_resources/history-of-the-language/middle-persian/"},{"title":"(PDF) The Origins of Middle Persian Zamān and Related Words: A Controversial Etymological History","url":"https://www.academia.edu/35233437/The_Origins_of_Middle_Persian_Zam%C4%81n_and_Related_Words_A_Controversial_Etymological_History"},{"title":"A note on Pahlavi lexicography: Middle Persian hassār, hassārīh | Bulletin of SOAS | Cambridge Core","url":"https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/note-on-pahlavi-lexicography-middle-persian-hassar-hassarih/E7145667DAE023A76FA973F2ED3FF545"},{"title":"PERSIAN LANGUAGE i. Early New Persian - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/persian-language-1-early-new-persian/"},{"title":"Pahla","url":"https://en.wikipedia.org/wiki/Pahla"},{"title":"A new etymological dictionary of Persian language – Bibliographia Iranica","url":"https://www.biblioiranica.info/a-new-etymological-dictionary-of-persian-language/"}]

I found some relevant results about Persian etymology and Hasandust's work. The search results reference Mohammad Hassandust's Etymological Dictionary of Persian, published in 2015 by the Academy of Persian Language and Literature in five volumes. The first result also mentions that Hasandust 1393 (likely the Persian calendar year equivalent to 2015) contains relevant information for a possible Iranian etymology.

However, the search results don't contain specific details about the etymology of the Persian word "jang" (جنگ - meaning "war/battle") or its connection to Middle Persian ǰang, Parthian "*ǰan-" meaning "strike," as you mentioned in your query. While the results show that Hasandust's etymological dictionary is the most comprehensive work covering Persian lexicon of both Iranian and non-Iranian origin with over 5500 entries, the specific etymological details you're looking for aren't available in these search results.

To get more detailed information about the specific etymology of "jang," you would likely need to access Hasandust's dictionary directly or search for more specialized academic sources on Persian historical linguistics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-05T21:06:44.861Z] TOOL RESULT

```
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1104 cp1104, Varnish XID 951471214<br>Upstream caches: cp1104 int<br>Error: 404, Not Found at Sat, 05 Sep 2026 21:06:44 GMT<br><details><summary>Sensitive client information</summary>IP address: 187.15.139.107</details></code></p>
</div>
###### gwhen
{{reconstructed}}
==Proto-Indo-European==
{{etymon|ine-pro|id=strike|pos=root}}

===Root===
{{ine-root|impf}}<ref>{{R:ine:IEW|head=g{{sup|u̯}}hen-(ə)-|pages=491-493}}</ref><ref name="LIV">{{R:ine:LIV|head=*g{{sup|u̯}}ʰen-|pages=218-219}}</ref><ref>{{R:ira:Cheung:2007|head=*ǰan|pages=224-225}}</ref>

# to [[strike]], [[slay]], [[kill]]
#: {{synonyms|ine-pro|*bʰerH-|*bʰeyh₂-|*dʰebʰ-}} (''See also'' [[Thesaurus:gʷʰen-]])

====Derived terms====
{{rootsee}}

* {{l|ine-pro||*gʷʰén-dʰe-ti|pos=dʰ-present}}
** {{desc|itc-pro|alt=*fendō}}  {{q|or < {{l|ine-pro||*gʷʰn̥dʰi|t=strike!|pos=pr.ipv.sg.}}}}<ref>{{R:itc:EDL|head=-fendō|pages=210-211}}</ref>
*** {{desc|la|*fendō}}<ref name="Sihler">{{R:Sihler 1995|section=218}}</ref> {{see desc}}
* {{l|ine-pro|[[*gʷʰénti|*gʷʰén-ti]] ~ *gʷʰn-énti|pos=athematic root present}}
* {{l|ine-pro||*gʷʰén-ye-ti|pos=ye-present}}<ref>{{R:xcl:Martirosyan|head=*ǰinǰ-|page=559}}</ref><ref name="Sihler" />
** {{desc|sqj-pro|alt=*gānja|unc=1}}
*** {{desc|sq|gjuaj|t=to hunt}}<ref name="LIV" /> {{q|or < {{l|ine-pro|*h₁eyǵʰ-}} or {{l|ine-pro|*seh₂ǵ-}}}}
** {{desc|hyx-pro|-}}
*** {{desc|xcl|ջնջեմ}} {{see desc}}
** {{desc|ine-bsl-pro|*genˀtei}} {{see desc}}
** {{desc|grk-pro|alt=*kʷʰéňňō}}<ref>{{R:grc:Beekes|head=θείνω|pages=536-537|volume=I}}</ref>
*** {{desc|grc|θείνω|t=to strike|unc=1}} {{q|or secondarily formed from a thematic root present}}

* {{l|ine-pro|[[*gʷʰegʷʰóne|*gʷʰe-gʷʰón-e]] ~ gʷʰe-gʷʰn-ḗr|pos=reduplicated stative}}

* {{l|ine-pro|*gʷʰn̥sḱéti|*gʷʰn̥-sḱé-ti|pos=sḱe-present}}<ref name="LIV" />
```


## [2026-09-05T21:06:59.556Z] TOOL CALL #49: Bash

```json
{
 "command": "grep -l '\"lang\": null' data/verification/page-1*.json | head -3; echo ---; python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('data/verification/page-1*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if not n.get('words'):\n                print(f, json.dumps(n,ensure_ascii=False)[:700]); raise SystemExit\nEOF"
}
```


### [2026-09-05T21:08:09.578Z] TOOL RESULT

```
data/verification/page-137.json
data/verification/page-121.json
data/verification/page-171.json
---
data/verification/page-101.json {"id": 5, "lang": "Arabic", "words": "", "verdict": "plausible", "derivation": "Pass-through node: Arabic zumurrud زُمُرُّد 'emerald' does go back to Greek smaragdos, but not directly: Wiktionary derives Arabic zumurrud from Persian zumurrud (< Middle Persian ʾwzmbwlt /uzumburd/ < Greek), i.e. Persian is the intermediary into Arabic rather than the reverse; another route often cited is Syriac zmaragdā. Arabic zabarjad 'peridot' is a doublet. The chart's Greek → Arabic → Persian ordering reverses the direction Wiktionary/MacKenzie give, so the Arabic node's parent is right in substance (Greek origin) but its child edge is not.", "derivation_fa": "این جعبهٔ گذرا برای عربی است: «زُمُرُّد» عربی
```


## [2026-09-05T21:08:13.020Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\nc=0\nfor f in ['data/verification/page-137.json','data/verification/page-121.json','data/verification/page-171.json']:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if n.get('lang') in (None,'') and not n.get('words'):\n                print(f, json.dumps(n,ensure_ascii=False)[:1200]); c+=1\n                if c>1: raise SystemExit\nEOF"
}
```


### [2026-09-05T21:08:14.704Z] TOOL RESULT

```
data/verification/page-137.json {"id": 6, "lang": null, "words": "", "verdict": "unverified", "derivation": "There is nothing to verify: on the printed page (p.107 = pdf 137) the box hanging to the right of the Old Persian box is a completely EMPTY double-ruled rectangle — no language label, no reference, no word, no gloss. It mirrors the position of the filled Persian box that hangs to the right of the Pahlavi box above it, so it is almost certainly an unfinished or accidentally blanked frame left in the author's drawing (the same kind of stray empty frame occurs elsewhere in the book). The extraction is faithful: the JSON's node #6 with lang null and an empty word list is exactly what the page shows.", "derivation_fa": "چیزی برای بررسی نیست: در صفحهٔ چاپی ۱۰۷ (برگ ۱۳۷ پی‌دی‌اف) قابی که در سمت راستِ خانهٔ «پارسی باستان» آویخته است کاملاً خالی است — نه نام زبانی دارد، نه ارجاعی، نه واژه‌ای و نه معنایی. جای آن درست قرینهٔ خانهٔ «فارسی» است که در بالا از «پهلوی» آویخته؛ پس به احتمال بسیار قابِ ناتمام یا سهواً خالی‌مانده‌ای در نقشهٔ خودِ مؤلف است. خوانش اسکن درست است و داده‌ها همان چیزی را نشان می‌دهند که در کتاب چاپ شده: خانه‌ای تهی.", "sources": [], "ref_check": [{"ref": "None", "status": "not_checked", "note": "t
data/verification/page-121.json {"id": 9, "lang": null, "words": "", "verdict": "unverified", "derivation": "An empty box: on the printed page (pdf 121 = book p.91) the arrow out of the Old Persian box points to a rectangle with no language label, no reference and no words — a layout artefact of Nourai's chart software, probably a slot he meant to fill with the New Persian or English continuation of asā-dāru 'ebony' (compare the parallel empty Germanic box, #13, which at least keeps its label). There is nothing to verify; the extraction is faithful to the page.", "derivation_fa": "این جعبه در صفحهٔ چاپی خالی است: نه نام زبان دارد، نه ماخذ، نه واژه. پیداست که نورایی جایی برای ادامهٔ asā-dāru گذاشته و آن را پر نکرده است. چیزی برای راستی‌آزمایی وجود ندارد؛ خوانش اسکن نیز با صفحه مطابق است.", "sources": [], "ref_check": [{"ref": "None", "status": "not_checked", "note": "the node carries no references in the book."}], "consulted": [{"src": "BOOK", "where": "printed page pdf 121 (book p.91), copied to data/verification/sources/refs/ocr/BOOK/121.png", "stance": "silent", "note": "the box is empty on the page itself."}]}
```


## [2026-09-05T21:08:37.813Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T21:08:37.856Z] TOOL RESULT

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


## [2026-09-05T21:08:47.339Z] TOOL CALL #52: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg187.png data/verification/sources/refs/ocr/BOOK/187.png && for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eng%CA%B0-\" \\\n \"https://en.wiktionary.org/wiki/gnaw\" \\\n \"https://en.wiktionary.org/wiki/gnat\" \\\n \"https://en.wiktionary.org/wiki/%D8%AC%D9%86%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%86%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\" \\\n \"https://www.etymonline.com/word/gangster\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 187 (Ghen / Ghengh): root and node verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-05T21:08:52.167Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5afb260891ca219c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/043d1356bece707c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0bd96ed4b8bb3cfb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b53a2012db6d1b45.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0f7d41918e60fa01.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4113893625ad2bc6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f4a4c4d0f4d87ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c814f97ef4387c1d.txt
```


## [2026-09-05T21:08:59.502Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 gnagan/ghenĝh\"; grep -n \"ghengh\\|g̑hengh\\|gnagan\\|zanga\\|ynixta\\|gnixta\" incoming/WLD/WLD_Bd1_pages.txt | head -15"
}
```


### [2026-09-05T21:08:59.550Z] TOOL RESULT

```
=== WLD Bd1 gnagan/ghenĝh
55567:  Av. aiwiynixta „angenagt, angefressen“ (Bartholomae ZfdYYf. 4, 252
55568:Air. \Yb. 89); an.gnaga „nagen", ags. gncigan ahd. gnagan, ginagan imit                              ,
55872:588                                                             ghengh-   — ghe(n)dh-
55880:ghengh- „schreiten; Schritt, Sehenkelspreize, Schamgegend“.
55881:  Ai. jamhas- n. Schritt, Flfigelschlag“, jmgha „Unterschenkel“, av. zanga-
74638:   ahd. zangar „bei8end, scharf", mnd. tanger „ds., bissig, kraftig, frisch“;
74639:anord. tgng (gen. tengr und tangar              tange, ahd. zanga „Zange“,
```


## [2026-09-05T21:09:00.276Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB zang\"; grep -n \"^zang\\|zang \" NYB_vol2_glossary.txt | head -8; echo \"=== NYB jang\"; grep -n \"^jang\\|ǰang\" NYB_vol2_glossary.txt | head -8"
}
```


### [2026-09-05T21:09:00.344Z] TOOL RESULT

```
=== NYB zang
1094:the ground 28%, — V. pad, dö-päd. MPrth cwhrb’d (MHC), MPrs tsb’y; Paz. cthārpāē, . pl. ctharwaéq; NP c(ah)ärpä, -và. cahar-zang [4-zng] having four legs, of demoniac beings: gurg 1 ~ 1028. — Ren- ders Av. (578) ca0waro.zangra-; v. zang and cf dö-zang.
1327:dö-zang [2-zng] a biped, of demoniac beings, pl. cas. obl. —-an 46!!. — V. zang and cahür-zang; renders Av. (966) bi- zangra-.
4497:zang [zng] ankle, shank 333. 4611, 98%. 1028. — Av. (1660) zanga-, zanga- ‘ankle’ ; v. dö-zang and cahär-zang.
5476:zanga, zonga-: zang
=== NYB jang
```


## [2026-09-05T21:09:08.138Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=55540 && NR<=55600' incoming/WLD/WLD_Bd1_pages.txt | grep -n \"pdf page\\|^5[0-9][0-9]\\|ghne\\|ghen\" ; echo \"---\"; sed -n '55550,55572p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== 588 region\"; sed -n '55872,55890p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-05T21:09:10.037Z] TOOL RESULT

```
7:1.    ghen- „sich freundlich benehmen"?
10:584                                                                 ghen-
16:2.    ghen- „zernagen, zerreiben, kratzen“, aucb „KIeines, BiBchenA
17:     Nur in den Erweiterungen ghnegh- ghnogh- (auch ghndd(h)-l)                          :
21:ghnei -, ghneu-.
22:     Gutturalerweiterung: ghnegh- (nach Persson Wzerw. 136 A                                                                                I
---


Letzteres nickt nacli Bezzenberger bei Pick II 4 110, Pedersen KGr. I 96
zu gr. yavv/nai ,.sich freuen“, yavog „Freude“ s. u. *gau- „sich freuen“.

2.    ghen- „zernagen, zerreiben, kratzen“, aucb „KIeines, BiBchenA
     Nur in den Erweiterungen ghnegh- ghnogh- (auch ghndd(h)-l)                          :



ghnei -, ghneu-.
     Gutturalerweiterung: ghnegh- (nach Persson Wzerw. 136 A                                                                                I




Beitr. 811     redupliziertes ghnc-gh-).
  Av. aiwiynixta „angenagt, angefressen“ (Bartholomae ZfdYYf. 4, 252
Air. \Yb. 89); an.gnaga „nagen", ags. gncigan ahd. gnagan, ginagan imit                              ,
                T
anaptyktischem Y okal s. Sehatz abd. Gr. S. 61), erst im 11.— 12. Jlidt.
nagan ds. Sehatz aaO. 290). — Daneben mit idg. g im Anlaut andfrk. cm-
gan ndl. knagen ds.
=== 588 region
588                                                             ghengh-   — ghe(n)dh-

  absl. gqzvica , vimen“, slov. goz „Riemen“, serb. giizva ,,vimen, Plechte aus
schlanken Reisern, Bauwinde, Eruckel, Wiede“, russ. guzb „Kummetriemen,
Tau, Seil‘‘, cech. houzev, poln. gnzwy pi. „lederne Kappe am Dreschflegel“.
Petersson IP. 24, 265.


ghengh- „schreiten; Schritt, Sehenkelspreize, Schamgegend“.
  Ai. jamhas- n. Schritt, Flfigelschlag“, jmgha „Unterschenkel“, av. zanga-
                                       .,


„Knochel des FuBes“ von ahurischen YVesen        -zangrn- (in Zs.) „ds. (von        ',


daevischen Wesen), schwundstufig ai. jaghana- m. n. „Hinterbacke, Scham-
gegend“ gr. xo/covg „Stelle zwischen den Schenkeln“ (ass. aus *y.ayd>va,
                      :
```


## [2026-09-05T21:09:20.634Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WEB gnaw\"; grep -n -i \"gnaw (nô)\\|gnaw, v\\|gnat (nat)\\|gnat, n\" WEB_vol1.txt | head -5; echo \"== FSD vol2 gnaw/gnat\"; grep -n -i \"^gnaw\\|^gnat\\|^gang\" FSD_vol2.txt | head -8; echo \"== FSD vol1\"; grep -n -i \"^gnaw\\|^gnat\\|^gang\" FSD_vol1.txt | head -8"
}
```


### [2026-09-05T21:09:20.766Z] TOOL RESULT

```
== WEB gnaw
79645:gall gnat (nat), same as gall midge.
82578:gnat (nat), n. [ME. gnat; AS. gnæt, a gnat.) 1. any of seyeral small, two-winged inse
== FSD vol2 gnaw/gnat
29862:Ganglionic,  gan'-  gang^sa',!  gntj’sa':  2   giing'sa',  k,  A   gong  or  drum  of  bronze ^   used  by  tbe  Igorots.  It  fa  about  Id  ‘
29880:gang'way",  1   Kiuj'we'; g gilnghva', «.  1.  A pas.sagcway,
29891:GangHon-eelia.
29934:gang'plank",  etc.  See  gang,  n.  ffan'ohl,  n.“  One  of  the  Gawjfdef.
29935:Gang-pur',  1   gun-pilr':  2   Kflrig-pur',  n.  A   native  state  m   <ja-nol'dc-l,  1   ge-nol'di-al;  2   ea-n6l'de-I.  n.  pi.  Jck.  A   large Ghutia  Nagpur,  British  India,  3,484  sq.  m.;  capital,  huadl.  divi.ston  of  fishes,  especially  a   8ubela.ss  having  a   contractile
33349:gnat*,  l   nat;2n5t,  71.  1.  A   small  nemocerous  two-winged fly  having  long  many-jointed  antenn®,  often  plumo.se in  the_  male,  as  a   buffalo-gnat,  gall-gnat,  or  turkey-gnat; especially,  a   blood-sucking  culicid  with  aquatic  larva; a   mosquito.  St-  Any  small,  worthless  thing.  Chaucer C.T.  11. 5,929, 17,204.  [   <   AS.gmct.]—  blackgnat (Angling) an  artificial  black  fly  tvith  dark  gray  wings.—  gnat'catch"» er,  71.  A   small  American  polloptl- llne  sylvlold  bird,  related  to  the kinglets,  having  a   graduated  tall and  the  wings  not  longer  than  the tail,  as  the  blue-gray  gnatoatcher  ,
33356:gnat**,  71.  A   bird,  the  knot  {Triuga.  canutus).
33357:gnat'eatch'tor,  gnat'fluw"er,  etc.  See  under  gnat*,  n.
== FSD vol1
42426:gnat  cat  cher
81668:gnath'I-on  *§*... go'nl-on  §  
81955:gnath'ic*
```


## [2026-09-05T21:10:53.072Z] TOOL CALL #57: Bash

```json
{
 "command": "grep -o \"AHD:[0-9]*\" data/extracted/batch/page-1*.json | sed 's/.*AHD/AHD/' | sort | uniq -c | sort -rn | head -25"
}
```


### [2026-09-05T21:10:53.125Z] TOOL RESULT

```
      6 AHD:1517
      5 AHD:1152
      4 AHD:579
      4 AHD:389
      4 AHD:240
      3 AHD:539
      3 AHD:370
      3 AHD:227
      3 AHD:183
      3 AHD:1511
      3 AHD:1115
      2 AHD:952
      2 AHD:854
      2 AHD:782
      2 AHD:74
      2 AHD:707
      2 AHD:542
      2 AHD:522
      2 AHD:452
      2 AHD:427
      2 AHD:352
      2 AHD:33
      2 AHD:228
      2 AHD:201
      2 AHD:156
```


## [2026-09-05T21:10:54.706Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==324' HRN.txt | head -2; echo \"--- leaf 300 header\"; awk 'BEGIN{RS=\"\\f\"} NR==300' HRN.txt | head -2; echo \"--- leaf 290\"; awk 'BEGIN{RS=\"\\f\"} NR==291' HRN.txt | head -4"
}
```


### [2026-09-05T21:10:56.500Z] TOOL RESULT

```
— M)2 —
237. xayltan 'hitten\ AW.-Komm., PPP. zast (kaum 2:aylt),
--- leaf 300 header
- 278 —
aw. gairi- *Berg'; ai. f]firi' 'Berg': ksl. gora,
--- leaf 290
— 2f)9 —
42. azg (d. i. azak) 'Ziege (PPÖl.).
ai. ajd' *Bock , ajd- 'Ziege' ; lit. osys, lett. aßs *Ziegen-
bock*, ozMi *Ziege'. Dazu wohl auch arm. aic (H. No. 16),
```


## [2026-09-05T21:11:11.286Z] AGENT

Now I'll write the verification file.


## [2026-09-05T21:17:42.866Z] TOOL CALL #59: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-187.json <<'JSONEOF'\n{\n  \"pdf_page\": 187,\n  \"book_page\": 157,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ghen\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *gʰen- 'to gnaw, bite, scratch, grind' (Pokorny 436-437 ghen-2 'aufbrechen, zerreiben, kratzen'; Watkins/AHD ghen- 'to gnaw')\",\n      \"note\": \"The root box is right on all three counts, and the page it cites is the right page. Pokorny's second ghen- runs pp.436-437 and is glossed 'zernagen, zerreiben, kratzen' ('to crack open, grind, scratch'); Watkins in the AHD appendix condenses this to 'ghen-. To gnaw' and cites '[Pok. ghen- 436.]', which is exactly Nourai's 'Ghen : to bite, chew / POK:436'. One qualification that Nourai does not make: the bare root is never attested — Pokorny writes 'Nur in den Erweiterungen ghnegh-, ghnad(h)-, ghnei-, ghneu-' ('only in the extensions'), so *gʰen- is an abstraction from a family of *gʰn- extensions, and the two branches Nourai draws come from two different extensions: the Avestan word from the guttural extension *gʰneǵʰ- and the gnat-word from the dental extension *gʰnad(h)-. The chart is otherwise a faithful and rather elegant reduction of the Pokorny article: both of the branches Nourai keeps (Avestan aiwi-γnixta-, Germanic gnag-/gnatt-) are the first two items Pokorny himself lists.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *gʰen- «جویدن، گاز گرفتن، خراشیدن» واقعی است و ارجاع نورایی هم درست: پوکورنی در صفحات ۴۳۶–۴۳۷ مادّهٔ دوم ghen- را با معنای «شکافتن، ساییدن، خراشیدن» آورده و واتکینز در پیوست فرهنگ American Heritage همان را «to gnaw» می‌نویسد و به «Pok. ghen- 436» ارجاع می‌دهد. تنها نکته‌ای که نورایی نگفته این است که خودِ ریشه هرگز به‌تنهایی گواهی نشده؛ پوکورنی تصریح می‌کند که این ریشه «تنها در گسترش‌های ghnegh-، ghnad(h)-، ghnei-، ghneu-» دیده می‌شود. بنابراین دو شاخهٔ نمودار در حقیقت از دو گسترش متفاوت‌اند: واژهٔ اوستایی از *gʰneǵʰ- و واژهٔ ژرمنی gnatt از *gʰnad(h)-. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/gnat\",\n        \"https://en.wiktionary.org/wiki/gnaw\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:436\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt: 'Root / lemma: ghen- / Meaning: to crack open, grind, scratch / Material: Only in den extensions ghnegh- : ghnegh-, ghna(dh)-, ghnei-, ghneu- ... References: WP. I 584 f. ... Page(s): 436-437'. The lemma begins on p.436, so Nourai's POK:436 is exact.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"pp.436-437, ghen-2\",\n          \"stance\": \"supports\",\n          \"note\": \"'Guttural extension ghnegh-: Avestan aiwi-γnixta- \\\"gnawed, corroded\\\"; Old Norse gnaga \\\"gnaw\\\", Old English gnagan ...' and 'Dental extension ghnad(h)-: ... Old English gnætt m. \\\"mosquito\\\", engl. gnat'. Both of Nourai's branches, in Pokorny's own order.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I p.584, '2. ghen-'\",\n          \"stance\": \"supports\",\n          \"note\": \"the parent article: '2. ghen- „zernagen, zerreiben, kratzen“, auch „Kleines, Bißchen“. Nur in den Erweiterungen ghnegh-, ghnogh- (auch ghnad(h)-), ghnei-, ghneu-.' (grep 'ghne' in incoming/WLD/WLD_Bd1_pages.txt, line 55553).\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. ghen-\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985.txt line 517: 'ghen-. To gnaw. Hypothetical base of various Germanic forms. 1. Germanic *gnagan ... 3. Perhaps related is Germanic *gnatt-, \\\"biting insect\\\" ... [Pok. ghen- 436.]' — Nourai's gloss 'to bite, chew' is Watkins's 'to gnaw'.\"\n        },\n        {\n          \"src\": \"Wiktionary\",\n          \"where\": \"s.v. gnat, etymology\",\n          \"stance\": \"supports\",\n          \"note\": \"'from Proto-Indo-European *gʰneHdʰn-, *gʰneHd- (to gnaw; scratch), from Proto-Indo-European *gʰen- (to gnaw; bite; scratch; grind)' — the modern reconstruction keeps both the root and Nourai's gloss.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"gnixta; aiwi-gnixta\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word Nourai is after is Younger Avestan aiβi.γnixta- (Bartholomae writes it aiwi-γnixta-), a past passive participle glossed 'angenagt, angefressen' = 'gnawed at, eaten away', attested at Vidēvdād 7.30 and 8.34 of a corpse that dogs or carrion-birds have been at (yezi nasuš aiβi.γnixta sūnō vā ... 'if the corpse has been gnawed by dogs or ...'), with the negated an-aiβi.γnixta- at Vd 3.37 and 7.29; the Pahlavi version renders it aparīat. Morphologically it is *gʰni-ǵʰ-ta-: the zero grade of the guttural extension *gʰneǵʰ- of *gʰen-, with the initial *gʰn- appearing as Avestan γn- and the root-final palatal *ǵʰ devoiced to -x- before the participial -ta-. Bartholomae states the derivation in those terms — 'PPfP. aus einer idg. Basis ghneĝh- oder ghn̥əĝh- ..., mit x aus idg. ĝh. Vgl. ahd., ags. gnagan \\\"nagen\\\"' — which is precisely the arrow Nourai draws, and is why the same root box legitimately also carries the Germanic gnag- branch. What is not right is the first word of the box: a simplex 'gnixta : chewed' does not exist in Avestan. Bartholomae's Wörterbuch has only the two compounds aiβi.γnixta- and an-aiβi.γnixta-; Pokorny too cites only 'Avestan aiwi-γnixta-'. Nourai has back-formed the participle from the compound in order to have a base form to hang the prefixed one on, which is a licit abstraction but should not be read as an attested Avestan word — hence 'plausible' rather than 'confirmed' for the node as printed.\",\n          \"derivation_fa\": \"واژهٔ اوستایی درست aiβi.γnixta- (به نوشتِ بارتولومه aiwi-γnixta-) است؛ صفت مفعولی به معنای «جویده‌شده، خورده‌شده» که در وندیداد ۷٫۳۰ و ۸٫۳۴ دربارهٔ نعشی به کار رفته که سگ یا مرغِ مردارخوار آن را جویده است، و صورت منفی آن an-aiβi.γnixta- در وندیداد ۳٫۳۷ و ۷٫۲۹ آمده؛ ترجمهٔ پهلوی آن aparīat است. ساخت آن *gʰni-ǵʰ-ta- است: پایهٔ صفر از گسترشِ کامیِ *gʰneǵʰ- که خودْ گسترشِ ریشهٔ *gʰen- است؛ gʰn- آغازین در اوستایی γn- شده و ǵʰ پایانی پیش از پسوند -ta- بی‌واک و به x بدل گشته است. بارتولومه دقیقاً همین را می‌گوید («صفت مفعولی از پایهٔ هندواروپاییِ ghneĝh- یا ghn̥əĝh-، با x از ĝh هندواروپایی؛ سنجیده شود با ahd.، ags. gnagan «جویدن»») و همین است پیوندی که نورایی رسم کرده. اما واژهٔ نخستِ خانه پذیرفتنی نیست: صورت سادهٔ gnixta در اوستایی گواهی نشده است و نه بارتولومه و نه پوکورنی جز همان دو صورتِ مرکب چیزی نیاورده‌اند؛ نورایی آن را از مرکب بازسازی کرده است. پس ادعای اصلی درست، ولی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/gnaw\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:436\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny pp.436-437 s.v. ghen-, guttural extension: 'Avestan aiwi-γnixta- \\\"gnawed, corroded\\\"; Old Norse gnaga \\\"gnaw\\\", Old English gnagan, gnagan ...'. Pokorny lists only the prefixed form, not a simplex.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 89 (BRT.txt line 3800)\",\n              \"stance\": \"partial\",\n              \"note\": \"'j. aiwi-γnixta- Adj. (fem. -ā-) \\\"angenagt, angefressen\\\": yezi nasuš °ta sūnō vā kǝrǝfš.xᵛarō vayō vā kǝrǝfš.xᵛarō V.7.30; — °ta V.8.34' and, in the etymology line, 'PPfP. aus einer idg. Basis ghneĝh- oder ghn̥əĝh- ..., mit x aus idg. ĝh. Vgl. ahd., ags. gnagan \\\"nagen\\\" ... — Pü.: aparīat.' Supports the derivation but has no simplex γnixta- (only an-aiwi.γnixta-, col. 116).\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p.584\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. aiwiγnixta „angenagt, angefressen“ (Bartholomae ZfdWf. 4, 252; Air. Wb. 89); an. gnaga „nagen“, ags. gnagan, ahd. gnagan, ginagan' — the Avestan and the Germanic word in one breath, exactly Nourai's two branches.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"pp.436-437\",\n              \"stance\": \"supports\",\n              \"note\": \"see ref_check.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"There is nothing to verify. On the printed page (book p.157 = pdf 187) the arrow leaving the Avestan box runs right across the chart into a plain double-ruled rectangle that carries no language label, no reference, no word and no gloss — the same kind of stray, unfilled frame that occurs elsewhere in Nourai's charts (compare the empty boxes on pdf pp.121 and 137). Its position mirrors the filled 'English' box that hangs off the Germanic box just below it, so it was presumably meant to hold the English or Persian continuation of the Avestan participle and was never filled in. The extraction is faithful: the JSON's node #2 with lang null and an empty word list is exactly what the page shows. Page image copied to data/verification/sources/refs/ocr/BOOK/187.png.\",\n          \"derivation_fa\": \"چیزی برای بررسی نیست: در صفحهٔ چاپی ۱۵۷ (برگ ۱۸۷ پی‌دی‌اف) پیکانی که از خانهٔ «اوستایی» بیرون می‌آید به قابی دو خطّی می‌رسد که کاملاً تهی است — نه نام زبان دارد، نه ماخذ، نه واژه و نه معنا. جای آن قرینهٔ خانهٔ «انگلیسی» است که در ردیف پایین از خانهٔ «ژرمنی» آویخته؛ پس پیداست که نورایی جایی برای ادامهٔ واژهٔ اوستایی گذاشته و آن را پر نکرده است. چنین قاب‌های ناتمامی در جاهای دیگر کتاب هم هست (برگ‌های ۱۲۱ و ۱۳۷). خوانش اسکن درست است و داده‌ها همان تهی‌بودن را ثبت کرده‌اند.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"the node carries no references in the book.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BOOK\",\n              \"where\": \"printed page pdf 187 (book p.157), copied to data/verification/sources/refs/ocr/BOOK/187.png\",\n              \"stance\": \"silent\",\n              \"note\": \"the box is empty on the page itself; the extraction reproduces it faithfully.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"gnag; gnatt\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both forms are standard Proto-Germanic reconstructions and both are Watkins's, on the very page Nourai's bare 'AHD' points to. *gnagan- 'to gnaw' (Nourai's 'gnag') continues the guttural extension *gʰneǵʰ- of the root, with Grimm's Law turning *gʰ- into Germanic *g- and the medial *-ǵʰ- into *-g-; it yields Old English gnagan, Old Norse gnaga 'to bite' (source of English nag), Old High German gnagan, Dutch knagen and German nagen (with early loss of the g- and, in Franconian/Dutch, a k- variant that Pokorny already notes). *gnatt-/*gnattaz 'biting insect' (Nourai's 'gnatt') belongs to the parallel dental extension *gʰnad(h)- with intensive gemination, giving Old English gnætt, Low German gnatte 'small mosquito', Danish dialectal gnat, MHG gnaz / NHG Gnatz 'scurf, skin rash'. The one hedge worth recording is that Watkins writes 'Perhaps related is Germanic *gnatt-' rather than asserting it; Pokorny and Walde-Pokorny put it under the same root without the qualification, and Wiktionary follows them (*gnattaz < *gʰneHdʰn- < *gʰen-). Nourai's glosses 'to bite' and 'a biting insect' are Watkins's own words.\",\n          \"derivation_fa\": \"هر دو صورت بازسازی‌های پذیرفتهٔ ژرمنی آغازین‌اند و هر دو در همان مدخلی آمده‌اند که ارجاع AHD نورایی به آن اشاره دارد. *gnagan- «جویدن» (همان gnag نورایی) دنبالهٔ گسترشِ کامیِ *gʰneǵʰ- است؛ بر پایهٔ قانون گریم، gʰ آغازین هندواروپایی در ژرمنی g شده و ǵʰ میانی نیز g، و برآیند آن انگلیسی باستان gnagan، نورس باستان gnaga، آلمانی علیای باستان gnagan و آلمانی امروز nagen است. *gnatt-/*gnattaz «حشرهٔ گزنده» (همان gnatt) از گسترشِ دندانیِ *gʰnad(h)- با مشدّدشدنِ تشدیدی است و انگلیسی باستان gnætt، آلمانی پستِ gnatte و آلمانی Gnatz را می‌دهد. تنها نکتهٔ احتیاطی آن است که واتکینز دربارهٔ *gnatt- می‌نویسد «شاید مربوط باشد»، حال آنکه پوکورنی و والده-پوکورنی و ویکی‌واژه بی‌تردید آن را زیر همین ریشه می‌آورند. معنای‌هایی که نورایی داده عیناً واژه‌های واتکینز است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/gnat\",\n            \"https://en.wiktionary.org/wiki/gnaw\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins's IE appendix (AHD_watkins1985.txt line 517): 'ghen-. To gnaw. Hypothetical base of various Germanic forms. 1. Germanic *gnagan in: a. Old English gnagan, to gnaw: GNAW; b. Old Norse gnaga, to bite ... 3. Perhaps related is Germanic *gnatt-, \\\"biting insect\\\", in Old English gnæt, gnat: GNAT. [Pok. ghen- 436.]' — Nourai's node is a transcription of items 1 and 3.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"pp.436-437\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old Norse gnaga \\\"gnaw\\\", Old English gnagan ... Besides with Indo-Germanic k in anlaut Franconian cnagan, Dutch knagen' and, under the dental extension, 'with intensive consonant stretch Old English gnætt m. \\\"mosquito\\\", engl. gnat ... Middle High German gnaz, -tzes \\\"scurf\\\", Modern High German Gnatz'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p.584\",\n              \"stance\": \"supports\",\n              \"note\": \"'an. gnaga „nagen“, ags. gnagan, ahd. gnagan, ginagan ... Daneben mit idg. k im Anlaut andfrk. cnagan, ndl. knagen ds.'\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"s.v. gnat / gnaw\",\n              \"stance\": \"supports\",\n              \"note\": \"gnaw '< Proto-Germanic *gnaganą (to gnaw), probably from PIE *gʰnēgʰ-'; gnat '< Proto-Germanic *gnattaz, *gnattuz (gnat), from PIE *gʰneHdʰn- ... from *gʰen-'. Neither hedges as Watkins does.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"gnaw, gnat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are inherited, not borrowed, and the chain is short and uncontroversial. Old English gnagan (strong verb, past gnōg) > Middle English gnawen, gnaȝen > Modern English gnaw, keeping the now-silent initial g- of the spelling after the gn- cluster was simplified to /n/ in early Modern English (compare gnash, gnarl). Old English gnætt 'gnat, midge, mosquito' > Middle English gnat > gnat, with the same orthographic fossil. Skeat gives 'Gnaw (E.) M.E. gnawen ... A.S. gnagan, to gnaw' and 'Gnat (E.) A.S. gnæt'; Webster's Second and Funk & Wagnalls both stop at 'ME. gnat; AS. gnæt'. The node carries no reference of its own because the derivation from the Germanic box above it is the whole content.\",\n          \"derivation_fa\": \"هر دو واژه میراثی‌اند نه وام‌واژه، و زنجیره کوتاه و بی‌مناقشه است. انگلیسی باستان gnagan (فعل قوی، گذشته gnōg) به انگلیسی میانه gnawen/gnaȝen و از آن به gnaw امروزی رسیده؛ g آغازینِ خوشهٔ gn- در آغاز دورهٔ نو ساقط شده ولی در املا بازمانده است (مانند gnash و gnarl). همچنین انگلیسی باستان gnætt «پشه» به انگلیسی میانه gnat و سپس gnat رسیده، با همان بازماندهٔ املایی. اسکیت می‌نویسد «Gnaw (E.) M.E. gnawen … A.S. gnagan» و «Gnat (E.) A.S. gnæt»، و وبستر و فانک و واگنالز نیز به همان AS. gnæt بسنده کرده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/gnaw\",\n            \"https://en.wiktionary.org/wiki/gnat\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"the node carries no references in the book; it inherits AHD from its Germanic parent.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SKT\",\n              \"where\": \"s.v. Gnaw, Gnat (SKT.txt lines 7701-7706)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gnaw, (E.) M.E. gnawen ... A.S. gnagan, to gnaw' with Icel./Swed./Dan. cognates and the note that prov. E. nag belongs here; 'Gnat (E.) A.S. gnæt.'\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"vol. 1 s.v. gnat (WEB_vol1.txt line 82578)\",\n              \"stance\": \"supports\",\n              \"note\": \"'gnat (nat), n. [ME. gnat; AS. gnæt, a gnat.] 1. any of several small, two-winged inse[cts] ...'\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"vol. II s.v. gnat (FSD_vol2.txt line 33349)\",\n              \"stance\": \"supports\",\n              \"note\": \"'gnat, n. 1. A small nemocerous two-winged fly ... [< AS. gnæt.]'\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"s.v. gnaw\",\n              \"stance\": \"supports\",\n              \"note\": \"'From Middle English gnawen, gnaȝen, from Old English gnagan, from Proto-West Germanic *gnagan, from Proto-Germanic *gnaganą'.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Ghengh; Ksengio\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *ǵʰengʰ- 'to walk, to step' (Pokorny 438-439 ghengh- 'to march, step'; Watkins/AHD ghengh- 'to go, walk'; LIV 175-6; Kroonen EDPG 166-7). The second name 'Ksengio' is not a standard root but S. E. Mann's lemma ksengiō (IEC 571) = the *(s)keng- 'crooked, limping' family (Pokorny 930).\",\n      \"verdict_note\": \"\",\n      \"note\": \"Half the box is solid and half is Mann. *ǵʰengʰ- 'to walk, step' is entirely standard: Pokorny gives 'Root/lemma: ghengh-, Meaning: to march, step ... Page(s): 438-439' (so POK:438 is exact), Watkins has 'ghengh-. To go, walk. [Pok. ghengh- 438.]', Klein p.639 s.v. gang gives 'I.-E. base *ghengh-, *ghongh-, \\\"to step\\\"', and Wiktionary reconstructs *ǵʰengʰ- 'to walk, to step' on LIV and Kroonen. Nourai's IEC references are equally exact: Mann's lemma 'ĝhengh- \\\"go, pace, step\\\"' stands on p.414 of the Indo-European Comparative Dictionary and his 'ksengiō (skeng-, skng-) \\\"limp, pace, amble\\\"' on p.571 (the OCR of the running page number there reads '511', an obvious misprint for 571 between 570 and 572). The problem is the second half of the root box. 'Ksengio' is not a received Indo-European root at all — it is Mann's private lemma for what Pokorny (p.930) and Wiktionary treat as *(s)keng- 'crooked, to limp' (Gk. skázō, Skt. khañjati, Sw. skinka), a family that has nothing to do with *ǵʰengʰ- except a superficial resemblance of shape and of gloss. Nourai has merged the two into one root box so that Sanskrit khañjāmi and Persian خنگ can hang off the same tree as Avestan zanga- and English gang. Everything in the chart that comes from *ǵʰengʰ- checks out; everything that comes from Mann's ksengiō is at best Mann's own opinion, and one node (Persian jang) is contradicted by the phonology of Persian itself. Hence 'plausible' rather than 'confirmed' for the root box as printed.\",\n      \"note_fa\": \"نیمی از این خانه استوار است و نیمی دیگر تنها رأی مان (Mann). ریشهٔ *ǵʰengʰ- «گام برداشتن، رفتن» کاملاً پذیرفته است: پوکورنی آن را در صفحات ۴۳۸–۴۳۹ با معنای «گام زدن» آورده (پس POK:438 دقیق است)، واتکینز «to go, walk» می‌نویسد، کلاین در ص ۶۳۹ ذیل gang «پایهٔ هندواروپایی *ghengh-، *ghongh- «گام برداشتن»» می‌گوید و ویکی‌واژه نیز بر پایهٔ LIV و کرونن همین را بازسازی کرده است. ارجاع‌های IEC هم درست‌اند: مدخل ĝhengh- در ص ۴۱۴ و مدخل ksengiō در ص ۵۷۱ فرهنگ مان است (شمارهٔ صفحه در متن اسکن‌شده «۵۱۱» خوانده شده که آشکارا خطای نویسه‌خوانی برای ۵۷۱ است). اما نیمهٔ دوم خانه ایراد دارد: «Ksengio» ریشه‌ای شناخته نیست، بلکه نامی است که مان به خانوادهٔ *(s)keng- «کج، لنگیدن» (پوکورنی ص ۹۳۰؛ یونانی skázō، سنسکریت khañjati) داده است و این خانواده جز شباهت ظاهری هیچ پیوندی با *ǵʰengʰ- ندارد. نورایی این دو را در یک خانه درآمیخته تا خنگ فارسی و khañjāmi سنسکریت را نیز به همان درخت اوستایی zanga- و انگلیسی gang بیاویزد. آنچه از *ǵʰengʰ- می‌آید درست است؛ آنچه از ksengiōی مان می‌آید در بهترین حالت رأی شخصی اوست و یکی از خانه‌ها (جنگ فارسی) با آواشناسی خودِ فارسی ناسازگار است. پس ادعای نورایی دربارهٔ این ریشه با احتیاط پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eng%CA%B0-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:438\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 36663: 'Root / lemma: ghengh- / Meaning: to march, step / Material: Old Indic jaṁhas- n. \\\"footstep, flapping\\\", jaṅghā \\\"shank, leg, shin bone\\\", Avestan zangam \\\"ankle of the foot\\\", -zangra- (in compounds) ds. ... Old English gang ... References: WP. I 588, WH. I 217, Trautmann 370. Page(s): 438-439.'\"\n        },\n        {\n          \"ref\": \"IEC:414\",\n          \"status\": \"supports\",\n          \"note\": \"IEC.txt (page marker '414' at line 5980): 'ĝhengh- \\\"go, pace, step\\\". Cf. ĝhongh-. WP I, 588 — Skt. janh-, v. (radical: \\\"dash along\\\"); jaṅghā \\\"lower leg\\\"; jaṅgha-, cpds. \\\"quickly\\\"; janghilaḥ, adj. \\\"quick\\\"; Av. zaŋgō \\\"upper of foot\\\"; Per. jangam \\\"fight, wage war\\\"; Tokh. B tsánk-, tsenk- \\\"rise\\\" ... Li. žengiù, -ti \\\"go, pace, move\\\".' Every Avestan, Sanskrit and Persian word of Nourai's chart, including the odd 'zangô' and 'jang', is copied from this one paragraph.\"\n        },\n        {\n          \"ref\": \"IEC:571\",\n          \"status\": \"supports\",\n          \"note\": \"IEC.txt line 8160, under the page marker OCR'd '511' but standing between 570 (line 8148) and 572 (line 8175), i.e. p.571: 'ksengiō (skeng-, skng-) \\\"limp, pace, amble\\\". Cf. WP I, 588 & II, 564 — Skt. kháñjāmi (\\\"limp\\\", fr. *ksenĝ-); Per. cf. xing \\\"white horse\\\"; xinga, adj. \\\"able-bodied\\\"; (zero-gde in) xazidan, inf. \\\"crawl\\\" ... Gk. skázō \\\"limp\\\"; MIr. cingim \\\"go, walk\\\"; Sw. skinka, inf. \\\"limp\\\".' Nourai's second root name and the words xeng and xanjami come from here.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"pp.438-439, ghengh-\",\n          \"stance\": \"supports\",\n          \"note\": \"see ref_check; Pokorny keeps *(s)keng- 'schief, krumm' (p.930) strictly separate from ghengh-, and mentions Old Irish cingim under ghengh- only as a possible dissimilated doublet ('A duplicate Anlaut (through dissimilation?) perhaps in Old Irish cingim').\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I p.588\",\n          \"stance\": \"supports\",\n          \"note\": \"'ghengh- „schreiten; Schritt, Schenkelspreize, Schamgegend“. Ai. jaṁhas- n. „Schritt, Flügelschlag“, jaṅghā „Unterschenkel“, av. zanga- „Knöchel des Fußes“ von ahurischen Wesen, -zangra- (in Zss.) „ds.“ (von daevischen Wesen), schwundstufig ai. jaghana- ...'\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. ghengh-\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985.txt line 520: 'ghengh-. To go, walk. 1. Germanic *gang-, a going, in: a. Old English gang, a going: GANG; b. Old High German gang, a going: GANGUE. 2. Germanic *gangan, to go, walk, in Old English gangan, to go: GANGLING. [Pok. ghengh- 438.]' — no Iranian or Sanskrit material, and nothing about fighting.\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"p.639 s.v. gang (n.)\",\n          \"stance\": \"supports\",\n          \"note\": \"'These words derive fr. I.-E. base *ghengh-, *ghongh-, \\\"to step\\\", whence also OI. jaṅghā, \\\"shank\\\", Avestic zanga-, \\\"ankle\\\", Lith. žengiu, \\\"I stride, step\\\". The above words are not related to E. go.'\"\n        },\n        {\n          \"src\": \"Wiktionary\",\n          \"where\": \"Reconstruction:Proto-Indo-European/ǵʰengʰ-\",\n          \"stance\": \"supports\",\n          \"note\": \"'*ǵʰengʰ- : to walk, to step' with *ǵʰéngʰ-o-s > Proto-Indo-Iranian *ȷ́ʰángʰas (Skt. jaṅghā, Av. zaŋga-) and *ǵʰongʰ-o-s > Proto-Germanic *gangaz; references Kroonen EDPG 166-7 and LIV 175-6. No 'ksengio' anywhere in the family.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"zanga; zangô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Younger Avestan zaŋga-, zaṅgā- m. 'Knöchel (des Fusses)', the ankle or lower leg — Bartholomae col. 1660 — used of ahuric (good) creatures, while the daēvic counterpart is zaŋgra- (col. 1660, 'von daēvischen Wesen'), whence the Avestan compounds bi-zangra- 'two-legged' and caθwarō.zangra- 'four-legged'. It continues *ǵʰéngʰ-o-s (Proto-Indo-Iranian *ȷ́ʰángʰas), with the regular Indo-Iranian palatalisation of PIE *ǵʰ to *ȷ́ʰ and its Iranian outcome z-, exactly as Sanskrit shows the same stem as jaṅghā́ 'lower leg'; the -ng- is the nasal of the root. Nourai's second entry, 'zangô : upper part of the foot', is not a second Avestan lexeme: it is Mann's citation form on IEC p.414, 'Av. zaŋgō \\\"upper of foot\\\"', i.e. the nominative singular zaŋgō of the same zaŋga- (Avestan -as > -ō), and his rendering 'upper of foot' is a looser gloss of Bartholomae's 'Knöchel des Fußes'. So the box holds one word in two shapes, and the derivation from the root is textbook.\",\n          \"derivation_fa\": \"اوستایی جوان zaŋga-، zaṅgā- (مذکر) به معنای «قوزک پا، ساق»؛ بارتولومه در ستون ۱۶۶۰ آن را «Knöchel (des Fusses)» معنی کرده و می‌افزاید که این واژه دربارهٔ آفریدگان اهورایی به کار می‌رود، حال آنکه برای موجودات دیوی صورت zaŋgra- را دارند (از همین‌جاست bi-zangra- «دوپا» و caθwarō.zangra- «چهارپا»). این واژه دنبالهٔ *ǵʰéngʰ-o-s است: ǵʰ هندواروپایی در هندوایرانی به ȷ́ʰ کام‌شده و در ایرانی z گشته است، چنان‌که در سنسکریت همان ستاک jaṅghā́ «ساق» را می‌بینیم. صورت دومِ خانه، zangô، واژهٔ جداگانه‌ای نیست بلکه همان صورتِ فاعلیِ مفرد zaŋgō است که مان در ص ۴۱۴ فرهنگ خود با معنای «رویهٔ پا» آورده و نورایی از او گرفته است. پس ادعای نورایی درست است، تنها با این تذکر که هر دو واژه یکی‌اند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eng%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:438\",\n              \"status\": \"supports\",\n              \"note\": \"'Avestan zangam \\\"ankle of the foot\\\", -zangra- (in compounds) ds.' — Pokorny pp.438-439.\"\n            },\n            {\n              \"ref\": \"KLN:639\",\n              \"status\": \"supports\",\n              \"note\": \"Klein p.639 s.v. gang: 'I.-E. base *ghengh-, *ghongh-, \\\"to step\\\", whence also OI. jaṅghā, \\\"shank\\\", Avestic zanga-, \\\"ankle\\\"'.\"\n            },\n            {\n              \"ref\": \"IEC:414\",\n              \"status\": \"supports\",\n              \"note\": \"Mann p.414 s.v. ĝhengh-: 'Av. zaŋgō \\\"upper of foot\\\"' — the source of Nourai's second form and of its gloss.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1660 (BRT.txt line 27647)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. zaŋga-, zaṅgā- m. \\\"Knöchel (des Fusses)\\\", von ahurischen Wesen ... KompE. — Vgl. zaŋgra-: — ai. jāṅghā- f. \\\"Unterschenkel\\\", mp. (Pü.) zang, oss. zängä \\\"Unterschenkel\\\".' Bartholomae gives no separate zaŋgō.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p.588\",\n              \"stance\": \"supports\",\n              \"note\": \"'av. zanga- „Knöchel des Fußes“ von ahurischen Wesen, -zangra- (in Zss.) „ds.“ (von daevischen Wesen)'.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Part II glossary s.v. zang, dō-zang, cahār-zang\",\n              \"stance\": \"supports\",\n              \"note\": \"'zang [zng] ankle, shank ... — Av. (1660) zanga-, zaṅgā- \\\"ankle\\\"'; 'dō-zang [2-zng] a biped ... renders Av. (966) bi-zangra-'; 'cahār-zang [4-zng] having four legs, of demoniac beings ... Renders Av. (578) caθwarō.zangra-'. Nyberg cites Bartholomae's column 1660 for the Avestan word.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"zang «زنگ» : foot (obsolete)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan/Old Iranian *zanga- 'ankle, shank' passes regularly into Middle Persian zang [Book Pahlavi zng] 'ankle, shank' — MacKenzie, Concise Pahlavi Dictionary p.98, and Nyberg's glossary, which cites it from the Bundahišn and the Zand and expressly refers it to 'Av. (1660) zanga-'. The word survives in the Pahlavi numeral compounds dō-zang 'biped' and cahār-zang 'quadruped' (Nyberg), which render Avestan bi-zangra- and caθwarō.zangra-, and it was borrowed into Armenian as zangapan / zankapan 'legging, greave'. Horn's entry no. 239 on the page Nourai cites is exactly this word: 'zang \\\"Fuss\\\", AW.-Komm., Bund.; arm. LW. zangapan, zankapan ... aw. zanga- \\\"Knöchel\\\"; ai. jaṅghā- \\\"unteres Bein\\\"'. In New Persian the word is indeed obsolete — Wiktionary's Persian زنگ covers only the homonyms 'rust' and 'bell', and MacKenzie, unlike his entry zangīg 'negro | N zangi', gives zang no New Persian continuation — so Nourai's own '(obsolete)' is the right label. Horn also warns, on the same page, against a supposed NP sar-jang 'heel' cited by de Lagarde: 'Ein np. serjeng \\\"Ferse\\\", das de Lagarde ... wieder anführt, giebt es nicht'.\",\n          \"derivation_fa\": \"«زنگ» به معنای «پا/ساق» بازماندهٔ ایرانی باستان *zanga- است که در فارسی میانه به‌صورت zang (به خط پهلوی zng) درآمده؛ مکنزی در ص ۹۸ فرهنگ پهلوی آن را «ankle, shank» معنی کرده و نیبرگ در واژه‌نامهٔ خود آن را از بندهش و زند شاهد آورده و صریحاً به «اوستایی (ستون ۱۶۶۰) zanga-» ارجاع داده است. این واژه در ترکیب‌های پهلویِ dō-zang «دوپا» و cahār-zang «چهارپا» (برابرِ اوستایی bi-zangra- و caθwarō.zangra-) زنده مانده و به ارمنی نیز به‌صورت zangapan «ساق‌پوش» وام رفته است. مدخل شمارهٔ ۲۳۹ هرن در همان صفحه‌ای که نورایی نشانی داده دقیقاً همین است: «zang «پا»، از تفسیر پهلوی اوستا و بندهش؛ وام ارمنی zangapan؛ اوستایی zanga- «قوزک»؛ سنسکریت jaṅghā- «ساق». در فارسی نو این واژه متروک است — ویکی‌واژه ذیل «زنگ» تنها همنام‌های «زنگار» و «ناقوس» را آورده و مکنزی هم برخلاف zangīg برای zang دنبالهٔ فارسی نو نمی‌دهد — پس قید «(obsolete)» نورایی درست است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%DA%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:302\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss p.302, entry no. 239 (HRN.txt leaf 324): '239. zang \\\"Fuss\\\", AW.-Komm., Bund.; arm. LW. zangapan, zankapan (de Lagarde, No. 752). — aw. zanga- \\\"Knöchel\\\"; ai. jaṅghā- \\\"unteres Bein\\\". np. zānū \\\"Knie\\\": oss. zängä \\\"Knie\\\" (126).' Precisely Nourai's arrow, page and gloss.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"p.98 s.v. zang\",\n              \"stance\": \"supports\",\n              \"note\": \"'zang [zng] ankle, shank.' (PHD_mackenzie.txt line 5768). Note that the adjacent entry zangīg is given as '| N zangi' while zang has no New Persian equivalent — MacKenzie treats the word as Middle Persian only.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Part II glossary s.v. zang\",\n              \"stance\": \"supports\",\n              \"note\": \"'zang [zng] ankle, shank 33³, 46¹¹, 98³, 102⁸. — Av. (1660) zanga-, zaṅgā- \\\"ankle\\\"; v. dō-zang and cahār-zang.'\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"s.v. زنگ (Persian)\",\n              \"stance\": \"silent\",\n              \"note\": \"the Persian entry has only 'rust' (cognate with Kurdish ژەنگ/jeng, Armenian ժանգ) and the 'bell' homonym; no 'foot' sense is listed, confirming that the word is dead in the modern language.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1660\",\n              \"stance\": \"supports\",\n              \"note\": \"Bartholomae's own entry already records the Middle Persian outcome: 'mp. (Pü.) zang'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"jang «جنگ» : fight; xeng «خنگ» : (white) horse\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both words are real Persian words with the glosses given, but neither derivation survives inspection, and the first is refuted by Nourai's own chart. (1) جنگ jang 'fight, war' does go back to Middle Persian ǰang (Book Pahlavi yng, Manichaean jnng) 'struggle, battle, fight', MacKenzie p.46 — but its initial ǰ- makes descent from *ǵʰengʰ- impossible for a Persian word: PIE *ǵʰ becomes Indo-Iranian *ȷ́ʰ and then Iranian z-, which is exactly why the same chart's Avestan zaŋga- and Persian زنگ zang have z-. A Persian reflex of *ǵʰengʰ- would have to be *zang, not jang. The ǰ- points instead either to a north-western (Parthian) form or to the wholly different root *ǰan- 'to strike, slay' (PIE *gʷʰen-, Cheung EDIV 224-5 *ǰan; Av., OP jan-, NP zadan), Parthian regularly keeping ǰ where Persian has z. Wiktionary and MacKenzie take جنگ no further back than MP ǰang and give it no PIE root; the equation with 'to step' is Mann's alone ('Per. jangam \\\"fight, wage war\\\"', IEC 414) and is semantically as weak as it is phonologically impossible. (2) خنگ xang/xeng 'white or grey horse' is well attested — Borhān-e Qāṭeʿ glosses it with چرمه 'white horse' and Moʿin, defining هدنگ, writes 'اسبی که موی آن سفید باشد؛ اسب خنگ' — but its origin is unsettled: Mann puts it under ksengiō 'limp, pace, amble' (IEC 571, 'Per. cf. xing \\\"white horse\\\"'), which requires an unexplained leap from limping to a coat colour, while Wiktionary derives it from PIE *ḱanḱest-/*kankest- 'horse' (cognate with Proto-Germanic *hangistaz, German Hengst) and itself tags that etymology {{rfv-etym}}, i.e. unsourced. Since the node's worse word is the flatly contradicted one, the node is disputed.\",\n          \"derivation_fa\": \"هر دو واژه فارسی‌اند و معنای‌هاشان درست است، اما هیچ‌یک از دو ریشه‌یابی برجای نمی‌ماند و نخستین آن‌ها با خودِ نمودار نورایی نقض می‌شود. ۱) «جنگ» به فارسی میانهٔ ǰang (پهلوی کتابی yng، مانوی jnng) «نبرد، پیکار» می‌رسد (مکنزی، ص ۴۶)؛ اما ج آغازین آن اجازه نمی‌دهد که از *ǵʰengʰ- آمده باشد: ǵʰ هندواروپایی در هندوایرانی ȷ́ʰ و در ایرانی z می‌شود — درست به همان دلیل که در همین نمودار zaŋga- اوستایی و «زنگ» فارسی با ز آمده‌اند. بازتاب فارسیِ *ǵʰengʰ- می‌بایست *zang باشد نه jang. این ج یا نشانهٔ صورتی شمال‌غربی (پارتی) است یا از ریشهٔ یکسره دیگری، یعنی *ǰan- «زدن، کشتن» (هندواروپایی *gʷʰen-؛ چونگ، فرهنگ افعال ایرانی، صص ۲۲۴–۲۲۵؛ اوستایی و پارسی باستان jan-، فارسی «زدن»)، چراکه پارتی ج را نگاه می‌دارد آنجا که فارسی ز دارد. ویکی‌واژه و مکنزی «جنگ» را جز تا ǰangِ فارسی میانه پی نگرفته‌اند و هیچ ریشهٔ هندواروپایی برایش نیاورده‌اند؛ برابرنهادن آن با «گام برداشتن» تنها رأی مان است. ۲) «خنگ» (اسب سفید یا خاکستری) به‌خوبی گواهی شده — برهان قاطع آن را با «چرمه» معنی کرده و معین در تعریف «هدنگ» می‌نویسد «اسبی که موی آن سفید باشد؛ اسب خنگ» — ولی ریشه‌اش قطعی نیست: مان آن را ذیل ksengiō «لنگیدن، گام زدن» می‌آورد که جهش معناییِ توجیه‌نشده‌ای می‌طلبد، و ویکی‌واژه آن را از *ḱanḱest- «اسب» (هم‌ریشه با Hengst آلمانی) می‌گیرد ولی خود آن را «نیازمند سند» نشانه‌گذاری کرده است. پژوهش امروزی ادعای نورایی را دربارهٔ «جنگ» رد می‌کند و دربارهٔ «خنگ» بلاتکلیف می‌گذارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AC%D9%86%DA%AF\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D9%86%DA%AF\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"IEC:414\",\n              \"status\": \"partial\",\n              \"note\": \"Mann p.414 s.v. ĝhengh- does contain 'Per. jangam \\\"fight, wage war\\\"', so the jang half of the node is copied accurately from the cited page. But xeng is NOT on p.414: it stands on p.571 under the separate lemma ksengiō ('Per. cf. xing \\\"white horse\\\"'), which Nourai cites only in the root box. Mann himself gives no argument for either link.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"p.46 s.v. jang\",\n              \"stance\": \"partial\",\n              \"note\": \"'jang [yng | M jnng, N ~] struggle, battle, fight.' MacKenzie confirms the Middle Persian ancestor and its continuation in New Persian, but offers no Indo-European etymology.\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"s.v. جنگ (Persian) and خنگ (Persian)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"جنگ: 'from Middle Persian 𐫋𐫗𐫗𐫃 (ǰang, \\\"struggle, fight\\\")', citing MacKenzie 1971 p.46 — and no further; the related Balochi verb جنگ janag 'to hit' is instead traced 'from Proto-Iranian *ǰántī, from Proto-Indo-Iranian *ǰʰánti, from Proto-Indo-European *gʷʰénti (to slay, strike)', which is the root that the ǰ- actually fits. خنگ: 'From Proto-Indo-European *ḱanḱest-, *kankest- (horse). Cognate with Proto-Germanic *hangistaz, and thereby with German Hengst. {{rfv-etym}}' — a different origin from Mann's, and itself flagged as unsourced.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"grep 'jang', 'ǰang' in CHEUNG.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"Cheung's Etymological Dictionary of the Iranian Verb has no entry for a verbal root *ǰang-; the noun jang is not treated, which is itself evidence that it is not derived from a step/walk verb. (His *ǰan 'to strike' is cited by Wiktionary as the reference for PIE *gʷʰen-.)\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"s.v. هدنگ (MON_part2.txt line 89277)\",\n              \"stance\": \"supports\",\n              \"note\": \"for the meaning of خنگ only: 'هدنگ ... (ا.) اسبی که موی آن سفید باشد؛ اسب خنگ' — Moʿin uses اسب خنگ as the standard gloss 'white-haired horse'. He gives no etymology there.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. II, footnote column (BQT_v2_pages.txt line 5336)\",\n              \"stance\": \"supports\",\n              \"note\": \"the Borhān column pairs خنگ with چرمه 'white horse' and Moʿin's footnote cites Qābusnāma and Nowruznāma on the coat markings; the OCR of this page is badly broken, so only the equation خنگ = چرمه could be read with confidence.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"grep 'jang' in HRN.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"Horn's Grundriss has no entry for jang at all — he does not derive it from zang or from any IE root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"janh; janghâ; xanjami\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The first two words belong here, the third does not. jáṅghā 'lower leg, shank' is the standard Sanskrit reflex of *ǵʰéngʰ-o-s (Proto-Indo-Iranian *ȷ́ʰángʰas), the exact cognate of Avestan zaŋga- — Pokorny 438 'Old Indic jaṅghā \\\"shank, leg, shin bone\\\"', Walde-Pokorny I 588 'jaṅghā \\\"Unterschenkel\\\"', Klein p.639 'OI. jaṅghā, \\\"shank\\\"'; the o-grade jaghána- m./n. 'buttock, pubic region' belongs to the same set. Nourai's 'janh : dash around' is not a Sanskrit word but Mann's citation of the root abstracted from the neuter s-stem jáṃhas- 'footstep, flapping (of wings)' — Mann writes 'Skt. janh-, v. (radical: \\\"dash along\\\")', and Wiktionary's *ǵʰéngʰ-os ~ *ǵʰéngʰ-es- gives Vedic जंहस् jáṃhas directly. The third word, 'xanjami : limp', is khañjāmi / khañjati 'to limp' and belongs to a different family: Mann himself files it not here but on p.571 under ksengiō ('Skt. kháñjāmi (\\\"limp\\\", fr. *ksenĝ-)'), and Pokorny puts it with *(s)keng- 'schief, krumm' (p.930), alongside Greek skázō and Swedish skinka. Its presence in this box is a consequence of Nourai's merged root name 'Ghengh; Ksengio'; a reader who takes the box at face value will conclude that khañjati descends from *ǵʰengʰ-, which no standard authority holds.\",\n          \"derivation_fa\": \"دو واژهٔ نخست به‌جای خودند و سومی نه. jáṅghā «ساق پا» بازتاب معیارِ سنسکریتِ *ǵʰéngʰ-o-s (هندوایرانی *ȷ́ʰángʰas) و هم‌ریشهٔ دقیق zaŋga- اوستایی است؛ پوکورنی در ص ۴۳۸، والده-پوکورنی در ج ۱ ص ۵۸۸ و کلاین در ص ۶۳۹ همین را می‌گویند، و jaghána- «سرین» نیز از همین دسته با پایهٔ o است. اما «janh» واژه‌ای سنسکریت نیست؛ ستاکی است که مان از اسم خنثای jáṃhas- «گام، بال‌زدن» انتزاع کرده و در ص ۴۱۴ چنین آورده است: «Skt. janh-, v. (radical: dash along)». واژهٔ سوم، xanjami، همان khañjāmi/khañjati «لنگیدن» است و به خانوادهٔ دیگری تعلق دارد: خودِ مان آن را نه اینجا بلکه در ص ۵۷۱ ذیل ksengiō آورده و پوکورنی آن را در ص ۹۳۰ زیر *(s)keng- «کج، لنگ» کنار skázō یونانی و skinka سوئدی نهاده است. آمدنِ آن در این خانه پیامد درآمیختنِ دو نام ریشه در جعبهٔ بالاست. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eng%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"IEC:414\",\n              \"status\": \"supports\",\n              \"note\": \"Mann p.414: 'Skt. janh-, v. (radical: \\\"dash along\\\"); jaṅghā \\\"lower leg\\\"; jaṅgha-, cpds. \\\"quickly\\\"; janghilaḥ, adj. \\\"quick\\\"' — the source of Nourai's first two words and of the gloss 'dash around'.\"\n            },\n            {\n              \"ref\": \"IEC:571\",\n              \"status\": \"supports\",\n              \"note\": \"Mann p.571 s.v. ksengiō: 'Skt. kháñjāmi (\\\"limp\\\", fr. *ksenĝ-)' — the source of the third word, and evidence that Mann keeps it apart from ĝhengh-.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"pp.438-439 (ghengh-) and p.930 ((s)keng-)\",\n              \"stance\": \"partial\",\n              \"note\": \"under ghengh-: 'Old Indic jaṁhas- n. \\\"footstep, flapping\\\", jaṅghā \\\"shank, leg, shin bone\\\", ... zero grade Old Indic jaghana- m. n. \\\"buttock, pubic region\\\"'. Sanskrit khañj- is not in this article; Pokorny treats it under the separate root *(s)keng- 'crooked, to limp'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p.588\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ai. jaṁhas- n. „Schritt, Flügelschlag“, jaṅghā „Unterschenkel“ ... schwundstufig ai. jaghana- m. n. „Hinterbacke, Schamgegend“' — no khañj-.\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"Reconstruction:Proto-Indo-European/ǵʰengʰ-\",\n              \"stance\": \"supports\",\n              \"note\": \"'*ǵʰéngʰ-os ~ *ǵʰéngʰ-es- > Proto-Indo-Iranian *ȷ́ʰánǰʰas > Proto-Indo-Aryan *ȷ́ánźʰas > Vedic Sanskrit जंहस् (jáṃhas)' and '*ǵʰéngʰ-o-s > Proto-Indo-Iranian *ȷ́ʰángʰas'. Confirms janh/jaṅghā, and lists nothing from the khañj- family.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"gang\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *gangaz m. 'a going, journey, way' (with the verbal noun beside *gangan- 'to go'), from the o-grade *ǵʰongʰ-o-s of the root, Grimm's Law turning *ǵʰ- into Germanic *g- and *-ǵʰ- into *-g-. Its descendants are Gothic gagg, Old Norse gangr, Old English, Old Saxon, Old Frisian, Old and Middle High German gang, Dutch and German Gang, all 'the act of going, passage'; from the same stem come the iterative *gangjan- (Gothic gaggida, OE gengan) and the derived *ginhtiz > MHG gīht 'gait, journey' (< *ǵʰengʰ-tis). Klein and Watkins both give exactly this box: Klein p.639 lists the whole Germanic set as verbal nouns to 'OE. gangan, ON. ganga, Goth. gaggan ... \\\"to go\\\"', deriving them from '*ghengh-, *ghongh-, \\\"to step\\\"', and Watkins has 'Germanic *gang-, a going'. The one thing Nourai's gloss slips on is the parenthesis '(a group of people going together)': that sense is not Germanic at all — it belongs to the later English history of the word (see node #6) and Old Norse gangr 'a group of men' — so the parenthesis should sit one box to the right.\",\n          \"derivation_fa\": \"ژرمنی آغازین *gangaz «رفتن، سفر، گذرگاه» (در کنار فعل *gangan- «رفتن»)، از پایهٔ o یعنی *ǵʰongʰ-o-s؛ بنا بر قانون گریم، ǵʰ آغازین به g و ǵʰ میانی نیز به g بدل شده است. بازماندگان آن گوتی gagg، نورس باستان gangr، انگلیسی باستان و ساکسونی باستان و آلمانی علیای باستان gang و آلمانی امروز Gang است، همه به معنای «رفتن، گذر». کلاین در ص ۶۳۹ همهٔ این مجموعه را «اسم‌های فعلیِ ساخته‌شده از gangan انگلیسی باستان، ganga نورسی و gaggan گوتی» می‌شمارد و از پایهٔ «*ghengh-، *ghongh- «گام برداشتن»» می‌گیرد، و واتکینز نیز «Germanic *gang-, a going» دارد. تنها لغزش نورایی آن پرانتزِ «گروهی که با هم می‌روند» است: این معنا ژرمنی نیست بلکه از تاریخِ بعدیِ واژه در انگلیسی (و نورسیِ gangr «دستهٔ مردان») برخاسته و می‌بایست یک خانه جلوتر می‌نشست. در باقی موارد ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gangster\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0eng%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:639\",\n              \"status\": \"supports\",\n              \"note\": \"Klein p.639 s.v. gang, n.: 'ME. gang, \\\"going; passage\\\", fr. OE. gang, \\\"going, passage, channel\\\", rel. to OS., OFris., Dan., Du., OHG., MHG., G. gang, ON. gangr, Swed. gång, Goth. gagg, \\\"the act of going\\\", verbal nouns to OE. gangan, ON. ganga, Goth. gaggan, etc., \\\"to go\\\". These words derive fr. I.-E. base *ghengh-, *ghongh-, \\\"to step\\\".'\"\n            },\n            {\n              \"ref\": \"AHD:542\",\n              \"status\": \"supports\",\n              \"note\": \"a body-page citation of the American Heritage Dictionary (New College Edition), not an appendix page — p.542 is where GANG stands in the G-section, and its etymology there points to the appendix root ghengh-. The corresponding appendix entry, on disk as AHD_watkins1985.txt line 520, reads 'ghengh-. To go, walk. 1. Germanic *gang-, a going, in: a. Old English gang, a going: GANG; b. Old High German gang, a going: GANGUE ... [Pok. ghengh- 438.]'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"pp.438-439\",\n              \"stance\": \"supports\",\n              \"note\": \"'with gradation o: Gothic gagg n., Old Icelandic gangr, Old English Old High German gang \\\"gait\\\" and Germanic *gangjan iter. ... and thereafter also *gangan, Gothic gaggan \\\"go\\\" = Old Icelandic ganga ... Old English -giht \\\"gait\\\", Middle High German gīht \\\"gait, journey\\\" (proto Germanic *ginχti- from gheng-ti-)'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, s.v. ghengh-\",\n              \"stance\": \"supports\",\n              \"note\": \"see ref_check; Watkins's gloss for the Germanic stem is 'a going', without any 'group of people' element.\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"Reconstruction:Proto-Indo-European/ǵʰengʰ-\",\n              \"stance\": \"supports\",\n              \"note\": \"derived terms include '*ǵʰongʰ-o-s > Proto-Germanic *gangaz', '*ǵʰongʰ-i-s > *gangiz', '*ǵʰongʰ-tis > *ganhtiz', '*ǵʰéngʰ-tis > *ginhtiz > Middle High German gīht', and the o-grade root present *ǵʰongʰ- > *ganganą.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"gang; gangster\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English gang 'a going, journey, way, passage' gives Middle English gang and modern gang; the modern dominant sense grew in three steps that Etymonline dates precisely — 'a set of articles taken together' (mid-14c.), 'a company of workmen' in nautical use (1620s), then 'a band of persons acting together for a criminal purpose' (1630s), reinforced by Old Norse gangr 'a group of men, a set', with 'group of criminal or mischievous boys in a city' by 1855. gangster is a straightforward American derivative of 1896, gang + the agent suffix -ster (originally an Old English feminine agent suffix, later genderless, as in gamester, roadster); an earlier political sense 'member of a clique controlling the local government' is on record from 1886. Klein states both halves on the page Nourai cites: 'gang, n., a group of people; a band. — ME. gang, \\\"going; passage\\\", fr. OE. gang' and 'gangster, n., member of a gang of roughs or criminals. — Formed fr. gang with suff. -ster.' Klein also notes on the same page the point Nourai's chart implicitly makes: 'The above words are not related to E. go.'\",\n          \"derivation_fa\": \"انگلیسی باستان gang «رفتن، سفر، گذرگاه» به انگلیسی میانه gang و از آن به gang امروزی رسیده است. معنای غالبِ امروزی در سه گام پدید آمده که واژه‌نامهٔ Etymonline تاریخ‌گذاری‌شان کرده است: «مجموعه‌ای از اشیای گردآمده» (میانهٔ سدهٔ ۱۴)، «گروه کارگران» در کاربرد دریانوردی (دههٔ ۱۶۲۰) و سپس «دستهٔ تبهکاران» (دههٔ ۱۶۳۰)، با تقویت از سوی gangr نورسی «دستهٔ مردان»؛ معنای «دستهٔ پسران شرور شهری» از ۱۸۵۵ گواهی شده است. gangster واژه‌ای امریکایی از ۱۸۹۶ است: gang به‌علاوهٔ پسوند فاعلیِ -ster (که در انگلیسی باستان پسوند فاعلیِ مؤنث بوده و بعدها بی‌جنسیت شده، مانند gamester و roadster). کلاین در همان ص ۶۳۹ هر دو را می‌آورد و می‌افزاید که این واژه‌ها با فعل go خویشاوند نیستند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gangster\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:639\",\n              \"status\": \"supports\",\n              \"note\": \"Klein p.639: 'gang, n., a group of people; a band. — ME. gang, \\\"going; passage\\\", fr. OE. gang ...' and, a few lines below on the same page, 'gangster, n., member of a gang of roughs or criminals. — Formed fr. gang with suff. -ster.' (KLN_1966.txt leaf 346 = printed pp.638-639, lines 15768 and 15776).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"s.v. gangster (with gang, n.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gangster (1896) ... member of a criminal gang, formed by combining gang + the suffix -ster ... Gang (noun): Old English gang \\\"a going, journey, way, passage\\\", and Old Norse gangr \\\"a group of men, a set\\\" ... from Proto-Germanic *gangaz, likely from the PIE root *ghengh- \\\"to step\\\".'\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"vol. II, gang- entries (FSD_vol2.txt lines 29862-29934)\",\n              \"stance\": \"supports\",\n              \"note\": \"Funk & Wagnalls carries the whole gang- family (gangway 'a passageway', gangplank, 'See gang, n.'), showing the older 'going, passage' sense still current in the 1913/1940 lexicon.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"grep '^gang' in SKT.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"Skeat's Concise has no separate gang entry (only 'Der. presto-gang' at line 18394); nothing for or against.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"gângester «گانگستر» : gangster\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"گانگستر gāngester is a twentieth-century loanword, not an inherited form, so the arrow English → Persian is a borrowing rather than a descent — a point worth making, because the chart's shape makes it look as if the word came down the same line as زنگ zang. Persian took it from English gangster (1896), almost certainly through the American gangster films and the press of the 1930s-40s, the same wave that brought فیلم, کاباره and دلار. The vocalisation is the regular European-loan pattern of that period: English /æ/ in the stressed first syllable is rendered by Persian ā (hence گانگ- gāng-, not گنگ-), the -ng- is kept as نگ, and the final -ster becomes -ster/-estar with the epenthetic vowel Persian inserts in a final consonant cluster. Nourai's reference is to Mahshid Moshiri's dictionary of European words in Persian, which is the right kind of source for this word; the word itself is unremarkable and is not in dispute.\",\n          \"derivation_fa\": \"«گانگستر» وام‌واژه‌ای از سدهٔ بیستم است، نه صورتی میراثی؛ پس پیکانِ «انگلیسی ← فارسی» در اینجا وام‌گیری است نه تبار، و این نکته اهمیت دارد چون شکل نمودار چنین می‌نماید که این واژه از همان راهی آمده که «زنگ» آمده است. فارسی آن را از gangster انگلیسی (۱۸۹۶) گرفته، به احتمال بسیار از رهگذر فیلم‌های گانگستری امریکایی و مطبوعات دههٔ ۱۳۱۰–۱۳۲۰ خورشیدی، در همان موجی که «فیلم» و «کاباره» و «دلار» را آورد. آوانویسی آن الگوی معمول وام‌واژه‌های اروپاییِ آن دوره است: /æ/ انگلیسی در هجای نخست به «آ» بدل شده (گانگ-، نه گنگ-)، خوشهٔ -ng- به «نگ» مانده و -ster پایانی با واکهٔ میانجی به «-ستر» درآمده است. ماخذی که نورایی داده (فرهنگ واژه‌های اروپایی در فارسی، مهشید مشیری) دقیقاً از همان گونه‌ای است که برای چنین واژه‌ای باید بود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gangster\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"VOP:303\",\n              \"status\": \"not_checked\",\n              \"note\": \"Mahshid Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (Alborz 1371/1992) has no copy anywhere online: data/verification/sources/refs_online.json records kind 'none' with the note 'Searched archive.org, ketabnak, noorlib, web: not found ... Purchase second-hand only.' Nothing on disk to check.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"grep 'گانگستر' in MON_part1.txt, MON_part2.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"no hit; Moʿin's volume 4, which collects the foreign compounds and would be the place for this word, is not among the OCR files on disk (only the lexicon volumes are).\"\n            },\n            {\n              \"src\": \"Wiktionary\",\n              \"where\": \"en.wiktionary.org page گانگستر\",\n              \"stance\": \"silent\",\n              \"note\": \"the page does not exist (HTTP 404), so Wiktionary offers no independent check; the English entry gangster gives the 1896 American origin that the Persian word borrows.\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"s.v. gangster\",\n              \"stance\": \"supports\",\n              \"note\": \"for the donor form and its date: 'Gangster (1896) ... emerged in American English as \\\"member of a criminal gang\\\", gang + -ster', which fixes the earliest possible date for the Persian borrowing.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-187.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 187"
}
```


### [2026-09-05T21:17:45.552Z] TOOL RESULT

```
JSON OK
nodes verified: 11/11
node verdicts: {'plausible': 2, 'unverified': 1, 'confirmed': 7, 'disputed': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 11, 'not_checked': 3, 'partial': 1}
books consulted: {'partial': 3, 'supports': 25, 'silent': 7, 'contradicts': 1} | by book: {'Wiktionary': 7, 'WLD': 4, 'POK': 4, 'BRT': 3, 'SKT': 2, 'FSD': 2, 'NYB': 2, 'PHD': 2, 'MON': 2, 'Etymonline': 2, 'BOOK': 1, 'WEB': 1, 'CHEUNG': 1, 'BQT': 1, 'HRN': 1, 'AHD': 1}
```


## [2026-09-05T21:17:46.227Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)
