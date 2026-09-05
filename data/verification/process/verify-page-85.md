# Verification process log — verify-page-85


## [2026-09-05T06:22:11.459Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 85 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-85.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-85.json. Write /home/sfmqrb/git/rishe/data/verification/page-85.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 85` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T06:22:13.132Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T06:22:13.836Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T06:22:13.855Z] TOOL RESULT

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


## [2026-09-05T06:22:14.042Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-85.txt"
}
```


### [2026-09-05T06:22:14.065Z] TOOL RESULT

```
1	=== PDF page 85 (book page 55) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhel, Bhelgh, Bhlei, Bhleu : to swell, blow, thrive, grow, bloom, overflow  (refs POK:120,122,125,156,158; AHD; ROE:65,66)  PART 2
4	#1 (parent #0) [Latin] refs=AHD | fluere : to flow ; fluere-ëscent : showing a flow ; in-fluentia : a flowing in ; folium : leaf ; flôs, flôr : flower
5	  #2 (parent #1) [French] refs=None | 
6	    #3 (parent #2) [Persian] refs=MON:97,386,2573; VOP:251 | folŭor «فلوئور» : Fluor gas ; flŭoresânt «فلورسانت» : fluorescent lamp ; ânflŭânzâ «آنفلوآنزا ، انفلوآنزا» : flu | NOTE: it literally means influence (of a virus).
7	    #4 (parent #2) [English] refs=AHD | flux, fluid, fluent, flush, fluoride, fluorescent, influence, foliage, portfolio, Florence, florist, flourish, flower.
8	#5 (parent #0) [Greek] refs=AHD | phullon : leaf ; xlôros-phullon : green leaf ☞Ghel
9	  #6 (parent #5) [French] refs=AHD | chloro-phylle : the green pigments in plants
10	    #7 (parent #6) [Persian] refs=MON:3030 | kolorofîl «کلروفیل»
11	    #8 (parent #6) [English] refs=AHD | chlorophyll
12	#9 (parent #0) [Germanic] refs=AHD | bul : bowl ; bullôn : bull ; balthaz : bold ; blôs : flower, blossom ; bladaz : leaf, blade ; balgîz : bellows
13	  #10 (parent #9) [English] refs=AHD | bowl, bull, bold, blossom, blade, bellows, belly
14	#11 (parent #0) [Dutch] refs=AHD | bluyster : blister | NOTE: This is a Middle Dutch word.
15	  #12 (parent #11) [English] refs=AHD | blister
16	
```


## [2026-09-05T06:22:18.005Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-85.json",
 "description": "Read source JSON for page 85"
}
```


### [2026-09-05T06:22:18.039Z] TOOL RESULT

```
{
  "pdf_page": 85,
  "book_page": 55,
  "entries": [
    {
      "root": {
        "name": "Bhel, Bhelgh, Bhlei, Bhleu",
        "lang": "Indo-European",
        "refs": "POK:120,122,125,156,158; AHD; ROE:65,66",
        "gloss": "to swell, blow, thrive, grow, bloom, overflow"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "fluere", "gloss": "to flow", "script": null},
            {"translit": "fluere-ëscent", "gloss": "showing a flow", "script": null},
            {"translit": "in-fluentia", "gloss": "a flowing in", "script": null},
            {"translit": "folium", "gloss": "leaf", "script": null},
            {"translit": "flôs, flôr", "gloss": "flower", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:97,386,2573; VOP:251",
          "words": [
            {"translit": "folŭor", "gloss": "Fluor gas", "script": "فلوئور"},
            {"translit": "flŭoresânt", "gloss": "fluorescent lamp", "script": "فلورسانت"},
            {"translit": "ânflŭânzâ", "gloss": "flu", "script": "آنفلوآنزا ، انفلوآنزا"}
          ],
          "script_extra": null,
          "note": "it literally means influence (of a virus).",
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "flux, fluid, fluent, flush, fluoride, fluorescent, influence, foliage, portfolio, Florence, florist, flourish, flower.", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "phullon", "gloss": "leaf", "script": null},
            {"translit": "xlôros-phullon", "gloss": "green leaf", "script": null, "see": ["Ghel"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "chloro-phylle", "gloss": "the green pigments in plants", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:3030",
          "words": [
            {"translit": "kolorofîl", "gloss": null, "script": "کلروفیل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "chlorophyll", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "bul", "gloss": "bowl", "script": null},
            {"translit": "bullôn", "gloss": "bull", "script": null},
            {"translit": "balthaz", "gloss": "bold", "script": null},
            {"translit": "blôs", "gloss": "flower, blossom", "script": null},
            {"translit": "bladaz", "gloss": "leaf, blade", "script": null},
            {"translit": "balgîz", "gloss": "bellows", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "bowl, bull, bold, blossom, blade, bellows, belly", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Dutch",
          "refs": "AHD",
          "words": [
            {"translit": "bluyster", "gloss": "blister", "script": null}
          ],
          "script_extra": null,
          "note": "This is a Middle Dutch word.",
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "blister", "gloss": null, "script": null}
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


## [2026-09-05T06:22:18.529Z] TOOL CALL #4: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -50; echo ---; cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-05T06:22:18.572Z] TOOL RESULT

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


## [2026-09-05T06:22:23.633Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/page-84.json data/verification/page-86.json 2>&1; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','ROE','MON','VOP','KLN','SKT','LEW','LAT','IEC','SYN','WLD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600]); print()\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-05T06:22:24.490Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,80p' data/verification/page-84.json 2>/dev/null || ls data/verification/ | tail -30",
 "description": "Peek at neighboring verification file"
}
```


### [2026-09-05T06:22:25.448Z] TOOL RESULT

```
ls: cannot access 'data/verification/page-84.json': No such file or directory
ls: cannot access 'data/verification/page-86.json': No such file or directory
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

ROE {"title": "R. Claiborne, The Roots of English: A Reader's Handbook of Word Origins, New York 1989", "edition_found": "1989 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/rootsofenglish00clai ; rootsofenglishre0000robe (lending)", "identifier": "rootsofenglish00clai (also rootsofenglishre0000robe)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<root>.", "notes": "RE-SEARCH 2026-09: borrowable only."}

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
```


### [2026-09-05T06:22:25.491Z] TOOL RESULT

```
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
page-76.json
page-77.json
page-78.json
page-79.json
page-80.json
process
sources
```


## [2026-09-05T06:23:06.432Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins bhel ===\"; grep -n -i \"bhel-\" AHD_watkins1985.txt | head -60\necho \"=== AHD bhleu ===\"; grep -n -i \"bhleu\\|bhlei\\|bhelgh\" AHD_watkins1985.txt | head -40",
 "description": "Grep AHD for bhel roots"
}
```


### [2026-09-05T06:23:06.495Z] TOOL RESULT

```
<persisted-output>
Output too large (49.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bmn86zbkm.txt

Preview (first 2KB):
=== AHD watkins bhel ===
326:bhel-?
328:bheidh-. To persuade, compel, confide. 1. Probably Ger- manic *bidan, to await (< “to await trustingly, expect, trust”), in Old English bidan, to wait, stay: BIDE; ABIDE, (ABODE). 2. Latin fidere, to trust, confide, and fidus, faithful: FIANCE, FIDUCIAL, (FIDUCIARY); AFFIANCE, (AFFIANT), (AFFIDAVIT), (CONFIDANT), CONFIDE, (CONFI- DENT), (DEFIANCE), DEFY, DIFFIDENT. 3. Suffixed o-grade form *bhoidh-es- in Latin foedus (stem foeder-), treaty, league: FEDERAL, FEDERATE; CONFEDERATE. 4. Zero-grade form *bhidh- in Latin fidés, faith, trust: FAITH, FEALTY, FIDELITY; INFIDEL, PERFIDY. [Pok. bheidh- 117.] bheig-. To shine. An uncertain but plausible root. Greek phoibos, shining: PHOEBE, PHOEBUS. [Pok. bheigz- 118.] bhel-'. To shine, flash, burn; shining white and various bright colors. I. 1. Russian byelii, white: BELUGA. 2. Greek phalaros, having a white spot (> phalaris, coot): PHALAROPE. II. 1. Suffixed variant form *bhié-wo- in Germanic *bléwaz, blue, in Old French bleu: BLUE. 2. Suffixed zero-grade form *bhb-wo- in Latin flavus, golden or reddish yellow: FLAVESCENT, FLAVO-; (FLAVIN), (FLAVONE), (FLAVOPROTEIN). III. Various ex- tended Germanic forms. 1. *blaikjan, to make white, in Old English blécan, to bleach: BLEACH. 2. *blaikaz, shining, white, in: a. Old Norse bleikr, shining, white: BLEAK}; b. Old English biéc, bright: BLEAK?. 3. Ger- manic *blikkatjan in Old High German blécchazzen, to flash, lighten (> German Blitz, lightning): BLITZKRIEG. 4. *blas-, shining, white, in: a. Old English blxse, torch, bright fire: BLAZE!; b. Middle Dutch bles, white spot: BLESBOK; C. Old French ble(s)mir, to make pale: BLEM- Ish. 5. *blend-, *bland-, to shine, dazzle, blind, confuse, in: a. Old English blind, blind: BLIND; (BLINDFOLD), (PURBLIND); b. Old High German blentan, to blind, deceive: BLENDE; Gc. Old English blandan, to mingle: BLEND; d. Old French blond; blond: BLOND. 6. *blenk-, *blank-, to shine, dazzle, blind, in: a. Old English
...
</persisted-output>
```


## [2026-09-05T06:23:07.911Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK bhel ===\"; grep -n \"bhel-\\|bhlē-\\|bhleu-\\|bhlei-\\|bhelĝh\\|bhelgh\" POK_full.txt | head -60",
 "description": "Grep Pokorny for bhel"
}
```


### [2026-09-05T06:23:07.964Z] TOOL RESULT

```
=== POK bhel ===
11748:Root / lemma: bhe/-2( > *bhel-(e)-n-)
```


## [2026-09-05T06:23:12.977Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'bhel-[\\'\\\"‘’²³⁴\\d\\.]?\\s*\\.?\\s*(To|A |Thriving)', t):\n    print('---', m.start())\n    print(t[m.start():m.start()+1500].replace('\\n',' '))\n    print()\nEOF",
 "description": "Extract AHD bhel root entries"
}
```


### [2026-09-05T06:23:14.878Z] TOOL RESULT

```
--- 120013
bhel-'. To shine, flash, burn; shining white and various bright colors. I. 1. Russian byelii, white: BELUGA. 2. Greek phalaros, having a white spot (> phalaris, coot): PHALAROPE. II. 1. Suffixed variant form *bhié-wo- in Germanic *bléwaz, blue, in Old French bleu: BLUE. 2. Suffixed zero-grade form *bhb-wo- in Latin flavus, golden or reddish yellow: FLAVESCENT, FLAVO-; (FLAVIN), (FLAVONE), (FLAVOPROTEIN). III. Various ex- tended Germanic forms. 1. *blaikjan, to make white, in Old English blécan, to bleach: BLEACH. 2. *blaikaz, shining, white, in: a. Old Norse bleikr, shining, white: BLEAK}; b. Old English biéc, bright: BLEAK?. 3. Ger- manic *blikkatjan in Old High German blécchazzen, to flash, lighten (> German Blitz, lightning): BLITZKRIEG. 4. *blas-, shining, white, in: a. Old English blxse, torch, bright fire: BLAZE!; b. Middle Dutch bles, white spot: BLESBOK; C. Old French ble(s)mir, to make pale: BLEM- Ish. 5. *blend-, *bland-, to shine, dazzle, blind, confuse, in: a. Old English blind, blind: BLIND; (BLINDFOLD), (PURBLIND); b. Old High German blentan, to blind, deceive: BLENDE; Gc. Old English blandan, to mingle: BLEND; d. Old French blond; blond: BLOND. 6. *blenk-, *blank-, to shine, dazzle, blind, in: a. Old English blen- can, to deceive: BLENCH!; b. Old French blanc, white: BLANCH, BLANK, BLANKET; BLANCMANGE. 7. *blisk-, to shine, burn, in Old English blyscan, to glow red: BLUSH. IV. Extended form *bhleg-, to shine, flash, burn. 1. Ger- manic *blakaz, burned, in Old 

--- 122103
bhel-2. To blow, swell; with derivatives referring to various round objects and to the notion of tumescent masculinity. 1. Zero-grade form *bhl- in Germanic *bul- in: a. Old English bolla (> Middle English boll), pot, bowl: BOLL, BOWL!; b. Old Norse bolr, tree trunk: BOLE}; c. Old Norse bulki, cargo (< “rolled-up load”): BULK}; d. Old High German bolla, ball: ROCAMBOLE; e. Middle High German bole, beam, plank: (BOULEVARD), BUL- WARK; f. Middle Dutch bolle, round object: BOLL; g. Middle Dutch bille, buttock: BILTONG; h. Swedish *buller-, “round object,” in bullersten, “rounded stone,” boulder, akin to the Scandinavian source of English BOULDER; i. possibly obsolete Swedish bulde, a swelling (see wer-1). 2. Suffixed zero-grade form *bhl-n- in: a. Germanic *bulJ6n-, bull, in Old Norse boli, bull: BULL); b. Greek phallos, phallus: PHALLUS; ITHYPHALLIC. bhel-* 3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLIC

--- 125051
bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND;

--- 414872
bhel-. To augment, increase. Greek ophe- los, advantage: ANOPHELES. [Pok. obhel- 772.] od-'. To smell. 1. Suffixed form *od-os- in Latin odor, smell: opor. 2. Suffixed form *od-é- in Latin olére, to smell (with J for d representing a Sabine borrowing): OLFACTORY, REDOLENT. 3. Suffixed form *od-yo- in Greek ozein, to smell: OZONE. 4. Suffixed form *od-md- in Greek osmé, smell: OSMATIC, OSMIUM; ANOSMIA. [Pok. 1. od- 72.] od-2. To hate. Latin édi, I hate, and odium, hatred: ANNOY, ENNUI, (NOISOME), ODIUM. [Pok. 2. od- 773.] 6g-. Fruit, berry. 1. Zero-grade form *ag- in Germanic *ak-ran- in Old English zcern, acorn: ACORN. 2. Latin iva (preform uncertain), grape: UVEA, UVULA; PYRUVIC ACID. [Pok. 6g- 773.] oid-. To swell. 1. Possibly Old English date, oat: oat. 2. Greek oidein, to swell: EDEMA. [Pok. oid- 774.] oi-no-. One, unique. I. Basic form *oi-no-. 1. Germanic *ainaz in: a. Old English dn, one: A1, AN!, ONCE, ONE; (ALONE), ANON, (ATONE), (LONE), (LONELY), NONE; b. compound *ain-lif-, “one left (beyond ten),” eleven (*lif-, left over; see leikw-), in Old English endleofan, eleven: ELEVEN; Cc. Old High German ein, one, in Ger- man vereinen, to unite: EINKORN, TURNVEREIN. 2. Latin anus, one: INCH}, OUNCE!, UNCIAL, UNI-, UNION, UNITE, UNITY; COADUNATE, QUINCUNX, TRIUNE, UNANIMOUS, UNICORN, UNIVERSE. 3. Latin ndn, not (< *ne-oinom, “not one thing”; ne, not; see ne). II. Suffixed form *oino-ko- in: a. Germanic *ainigaz in Old English &nig, one, anyone: ANY; b. Latin dnicus, sole,
```


## [2026-09-05T06:23:19.371Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nprint(t[123550:127200].replace('\\n',' '))\nEOF",
 "description": "Print AHD bhel-2 continuation and bhel-3"
}
```


## [2026-09-05T06:23:20.963Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"bhleu-.\\{0,900\\}\" AHD_watkins1985.txt | head -5\necho \"==== bhlei\"; grep -n -o \"bhlei-.\\{0,700\\}\" AHD_watkins1985.txt | head -5\necho \"==== bhle\"; grep -n -o \"bhlé-.\\{0,900\\}\" AHD_watkins1985.txt | head -8",
 "description": "Grep AHD bhleu/bhlei roots"
}
```


### [2026-09-05T06:23:21.001Z] TOOL RESULT

```
lis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero- bherag- grade form *bhndh- in Germanic *bund- in: a. Middle High German bunt, league: BUND?; b. Middle Dutch bondel, sheaf of papers, bundle: BUNDLE. 4. Suffixed form *bhendh-na-, “tied structure” (as of wicker), in Celtic *benna, manger, in Old English binn(e), manger: BIN. 5. Persian band, band, bandage, also a river levee: BUND!; CUMMERBUND. 6. Sans
```


### [2026-09-05T06:23:22.712Z] TOOL RESULT

```
328:bhleu-(k)- 159.] bhel-2. To blow, swell; with derivatives referring to various round objects and to the notion of tumescent masculinity. 1. Zero-grade form *bhl- in Germanic *bul- in: a. Old English bolla (> Middle English boll), pot, bowl: BOLL, BOWL!; b. Old Norse bolr, tree trunk: BOLE}; c. Old Norse bulki, cargo (< “rolled-up load”): BULK}; d. Old High German bolla, ball: ROCAMBOLE; e. Middle High German bole, beam, plank: (BOULEVARD), BUL- WARK; f. Middle Dutch bolle, round object: BOLL; g. Middle Dutch bille, buttock: BILTONG; h. Swedish *buller-, “round object,” in bullersten, “rounded stone,” boulder, akin to the Scandinavian source of English BOULDER; i. possibly obsolete Swedish bulde, a swelling (see wer-1). 2. Suffixed zero-grade form *bhl-n- in: a. Germanic *bulJ6n-, bull, in Old Norse boli, bull: BULL); b. Greek phallos, phallus: PHALLUS; ITHYPHALLIC.
330:bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, F
342:bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man 
1442:bhleu- EFFLUVIUM bhieu- EFFLUX bhlieu- EFFORT bhergh-2 EFFULGENT bhel-1 EFFUSE gheu- EFTSOONS apo- EGEST gerere EGG! awi-
1521:bhleu- FLUENT bhieu- FLUERIC bhleu- FLUE? pleu- FLUGELHORN ker-1, pleu- FLUID bhleu- FLUKE! plak-1 FLUME bhlieu- FLUOR bhlieu- FLUORIDE bhleu- FLUORO- bhieu- FLUSH? bhleu- FLUSTER pleu- FLUTTER pleu- FLUVIAL bhleu- FLUVIOMARINE bhieu- FLUX bhieu- FLY! pleu-
==== bhlei
330:bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed f
342:bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, 
1309:bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bhe
==== bhle
330:bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to 
342:bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a sw
1309:bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
1418:bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1503:bhlé-1 FEED pa-
2277:bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
```


## [2026-09-05T06:23:36.524Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\"\nls -la POK_*.txt",
 "description": "POK page offsets"
}
```


### [2026-09-05T06:23:38.035Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
```


## [2026-09-05T06:23:40.286Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: bhel\\|lemma: bhlei\\|lemma: bhleu\\|lemma: bhel-gh\\|lemma: bhelgh\" POK_full.txt | head -20",
 "description": "Grep POK_full lemma blocks"
}
```


### [2026-09-05T06:23:40.332Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T06:23:42.305Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Root / lemma: bh\" POK_full.txt | head -60",
 "description": "List bh- lemmas in POK_full"
}
```


### [2026-09-05T06:23:42.353Z] TOOL RESULT

```
10965:Root / lemma: bhedh_/(bhedh-i > *b^e6^-r) 
11116:Root / lemma: bheigr"- 
11748:Root / lemma: bhe/-2( > *bhel-(e)-n-) 
15408:Root / lemma: bhren-to-s
```


## [2026-09-05T06:23:46.021Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in 120 122 125 156 158; do leaf=$((p+8)); echo \"########## printed p.$p (leaf $leaf) ##########\"; awk -v n=$((leaf+1)) 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -60; done",
 "description": "Print Pokorny pages 120,122,125,156,158"
}
```


### [2026-09-05T06:23:47.829Z] TOOL RESULT

```
########## printed p.120 (leaf 128) ##########
cymr.  heleu  (*bheleuo-)  ,Marder^,  air. oibell  m.  ,Glut,  Hitze^  (f.  ,Funke,  glühende  Kohle^)  =  cymr.  ufel  m. ,Funke,  Feuer^  (^opi-bhelo-),  mir.  Bel-tene  ,Fest  des  1.  Mai^  (=  Leuchtfeuer), aall.  GN  {Apollo)  Belenos,  (^Minerva)  Belisama  (Superlat.),  FIN  Belenä  > frz.  Bienne,  Schweiz.  Biel]  afrz.  haille  ,Blässe^  (daraus  mbret.  baill  ds.) könnte  auf  ablaut.  gall.  *halio-  zurückgehen,  vgl.  frz.  ON  Bailleuil  < *BaUo-ialon-  gall.  heisa  ,Feld^  aus  *belisä',
got.  hala  m.  ,Bläß^  (von  Belisars  Roß),  engl.  dial.  hall  ,Pferd  mit  weißer Blässe^  (daraus  cymr.  hal  ds.),  mengl.  halled,  engl,  haldj  dän.  hceldet  ,kahl^, a.\id.  helihha  (vgl.  lat. /wh'ca),  nhd.  Belche  ,Bläßhuhn^,  BergN  Belchen  (zum Suffix  s.  Brugmann  Grundriß  II  1,  511,  Specht  Dekl.  213f.),  dehnstufig aisl.  häl  ,Flamme^,  ags.  hcel  ,Scheiterhaufen^  (*hhel-).
Hingegen  sind  germ.  *pöl-  in  ags.  pöl,  engl,  pool,  ahd.  pfuol  ,Pfuhl^, ablaut.  ndl.  peel  {*pali-)  ,Morast^,  ags.  pyll,  engl,  pill  {*pulia-y  älter  *hlio-) wohl  aus  dem  Ven.-Ill.  entlehnt  (s.  oben  *hola) ;  anders  Petersson  Heterokl.  205  ;
lit.  hälas  ,weiß^  und  ,Schneeglöckchen^,  halä  f.  ,weiße  Anemone^  und  m. ,Sumpf,  Moor,  Pfuhl',  halü^  halau,  iaZ^t , weiß  werden^;  lett.  dehnstuf,  hals ,bleich,  blaß'^;  apr.  hallo  f.  ,Stirn*^  und  *halo  ,Sumpf^  in  ON;
aksl.  dehnstuf,  heh  ,weiß^  (^hhelo-),  f.  ,Splint  im  Holze^,  poln.  dial.  hiel  f. ,sumpfiger  Wald',  russ.  dial.  hil  , Sumpf;  ablaut.  hala  (*hhöla)  in  russ. hala-ruzina  ,Pfütze',  klr.  halka  ,Niederung^;
lit.  6aZto_(^^^jWa^Qg),  leU.  halts  /weiß',  SeeN  Baltina  ezers]
slavTsubstant.  neutr.  Adj.  *holto-  {*hhohto-)  ,Sumpf,  Teich,  See'  in  aksl. hlato  ,See',  skr.  hläto  ,See,  Kot',  russ.  hoiöto  ,Sumpf';
lit.  bd'lnas  ,weiß'  (mit  Stoßton,  idg.  *bhohnos)^  halaüdis  ,Taufe',  haldnda ,Melde',  russ.  lehedd,  serb.  lohbda  ds.;
slav.  *holna  f.  (mit  Schleifton,  idg.  *hholna)  in  Öech.  slov.  hldna  ,Haut, Häutchen',  russ.  hol'ond  ,Hülle,  Auswuchs  an  Bäumen',  holont  Lj  ,Splint im  Holze',  ursprüngl.  identisch  mit  cech.  hlana  ,Wiese',  poln.  hioii  f., hionie  n.  ds.,  russ.  hoiouhje  n.  ,tief  gelegene  Wiesen';
vielleicht  toch.  B  palsk-,  pälsk,  A  päl(t)sk  ,nachdenken'  (*sehen,  vgl. ai.  sam-hhälayati)]
120  '
ob  hierher  gr.  cpeXlög  (*bhel-so-)y  ,Kork,  Korkeiche^,  cpeXUvg  ^steinige? Grund^,  dcpslrig  ^eben';,  q)olig  ^Schuppe  (eines  Reptils/?
Hierher  ferner  2.hhel-]  hheleg-\  bhlei-,  -g-j  -k--,  bhlendh-;  bhles-]  bhhu^ -k-j  -S-]  bhleuo-',  bhlndho-;  bhhido-.
WP.  II  175  f.,  WH.  I  108  f.,  559  f.,  W.  Schulze  Berl.  Sbb.  1910,  787 Kl.  Sehr.  111,  Trautmann  25,  29  f.,  Specht  Dekl.  116  f.
2.  bhcl-  in  Bezeichnungen  des  Bilsenkrautes,  wohl  mit  1.  bhel-  identisch.
Gall.  (illyr.  ?)  belinuntia  f.,  ßeXevLov  n.  , Apollinaris',  zum  Namen  des  Apoll Belenos  (s.  oben  1.);
ags.  beolone  (*bheluna)j  as.  bilene,  tiefstuf,  älter  dän.  bylne  (germ.  *6wZ-n-jl belme,  schwed.  bolmört,  nhd.  dial.  bilme]  aber  ah
########## printed p.122 (leaf 130) ##########
geliges  Gefaßt;  mir.  öaZZaw  , Trinkgefäß'  wohl  aus  dem  Nord.), ntrs.  Z>oZ?«  m.  , Schale^,  lieafodholla  ^Hirnschale',  afries,  strotholla  ,Kehl- kopf  s-s-  ^^^^^  ,Trinkschale'^  ahd.  holla  f.  ,  Wasser  blase,  Fruchtbalg  oder Knoten  des  Flachses',_  mhd.  holle  f.  ,Knospe,  kugelförmiges  Gefäß',  ahd. hirniholla  ,Hirnschale',  nhd.  Bolle,  Roßhollen,  mhd.  hullich,  bolch  _,großer Fisch  u.  a.  Kabeljau'  (vgl.  qxxXlaivcc),  vgl.  auch  ahd.  holön,  mhd.  holn rollen,  werfen,  schleudern'  und  mit  der  Bed.  geschwollen  ==  ,dick,  groß', schwed.  mdartl.  häl,  &oZ  ,dick  und  groß,  stark,  sehr  kühn',  aisl.  poet.  holmr Bär';  hierher  wohl  aisl.  hulki  , Schiffslast',  schwed.  dän.  hulk  ,Buckel', Knollen';
auf  ein  heterokl.  Paradigma  (?)  *bhelr,  Gen.  Hhelnes  deutet  ahd.  bilor7i m.  f.  , Zahnfleisch'  (*hilurnö  ,Sch wellung,  Wulst'),  falls  nicht  aus  Heluznö ; germ.  *hel-n-  auch  in  hess.  hille  ,penis'  (:  hülle),  mnd.  {ars-)hille,  ndl.  hil jHinterbacke',  schwed.  fotahjälle  , Fußballen,  Zehenballen';
ablautend  ahd.  hallo,  halla,  nhd.  Ball,  Ballen,  ahd.  arshelli  m.  Fl.  , Hinter- backen', ags.  healluc  m.  , Hoden'  (*hhol-n-),  aisl.  hgllr  , Kugel,  Ball,  Hode'; aisl.  hall  , Erhöhung  entlang  dem  Uferrande ;  kleine  Erhöhung  auf  ebenem Boden';  mit  Formans  -to-  und  der  Bed.  , geschwollen'  =  ,hochfahrend, kühn',  got.  hal-paha  Adv.  ,kühnlich',  halpei  f.  , Kühnheit',  aisl.  hallr , furchtbar,  gefährlich',  haldinn  , trotzig',  ags.  heald  ,kühn,  dreist',  ahd. bald  ,kühn,  dreist,  schnell',  nhd.  bald  Adv.;  dazu  ags.  bealdor  , Fürst, Herr',  aisl.  GN  Baldr.
Mit  Abtönungsstufe  *hhöl-  wohl  norw.  hol  ,brünstig,  von  der  Sau'  (ab- lautend hala  jbrünstig  sein').
Wurzelform  bble-:
Gr.  (pXrjvaq)og  , Geschwätz,  schwatzhaft',  g)Xr]v-€(x),  -da)  ,bin  schwatzhaft'; iaq)}.cxlvu)  wie  cpalvo)  von  hhä-,  Aor.  iKcplrjvai  , hervorsprudeln';
lat.  flö,  fläre  ,blasen'  (wohl  aus  *hhld-{ö),  aber  flemina  , Krampfadern'  ist wohl  Lw.  aus  gr.  cplsyixovrj -,  norw.  dial.  blcema  , Hautbläschen' ;  aschwed. blcemma  ds.;  ahd.  hlät(t)ara,  as.  hlädara  ,Bkse,  Blatter',  ags.  blcedre  ds., Red.-St.  aisl.  bladra  , Bläschen,  Blatter',  ahd.  usw.  blat  ,Blatt';  aisl.  blä- in  Zs.  ,übermäßig,  sehr';  mit  vorherrschender  Bed.  ,blasen'  ahd.  lO-Präs. bläjan,  hläen  , blasen,  blähen,  aufblähen',  ags.  bläiuan  , blasen'  (das  w  aus dem  Perf.),  ahd.  hlät,  ags.  hlced  , Wehen,  Hauch,  Windstoß',  aisl.  blcer ,Windstoß';  mit  -s-  got.  ufhlesan  ,aufblasen',  aisl.  hläsa  , blasen,  keuchen, aufblasen;  unpers.:  aufschwellen',  ahd.  bläsan  ,blasen',  hläsa  ,Blase',  blast
122
, Blasen,  Hauch',  ags.  hlcest,  aisl.  blästr  (*blestu-)  ^Blasen,  Hauch,  Schna\3 ben,  Zor
########## printed p.125 (leaf 133) ##########
,schlecbt,   bäßlich'  (daraus   lett. blägs,  lit.  blögas  ,kraftlos,  schwach'  entlehnt),  biazic  ,tollen',  grruss.  blag^ ,starrköpfig,   häßlich',    dial.  blainoj  ,dumm',   poln.  biagi   ,schlecht,    nichts wert';  kaum  zu  gr.  cpElyvvei '  davvsTetj  Xr]Qst  Hes.,  da  das  slav.  Wort  auf  i schwere,  das  griech.  auf  leichte  Basis  weist;  s.  unter  phelg-,  |
Hierher  (offenbar  mit  expressiver  Gemination)  aber  lat. /acctts  , schlaffe
WP.  n  183  f.,  680,  WH.  I  507  f.
bheld-  ,pochen,  schlagen',  vielleicht  ursprüngl.  cZ-Präsens  der  Schallwurzel  bhel,   •.
Aus   dem   Germ,  wahrscheinlich   dazu  mnd.  bolte(7i)   ,Bolz,  Pfeil',  ahd. bolzj  nhd.  Bolz,  Bolzen,  ags.  bolt  ,Bolz,  Pfeil',  schwed.  bult  ,Bolz'  (*bhld.\- vielleicht   auch   nhd.  Balz,  Vb.  balzen   und    bolzen,    norw.  mdartl.  bolt  m. ,männlicher   Waldvogel;    Kater',    nhd.  Bolze  ,Kater';   norw.  mdartl.    bolta^^ ,poltern,    vorwärtsstürmen',    älter    dän.  bolte  ,sich    rollen',    schwed.    bidtaj ,klopfen',    schwed.  mdartl.  bultra  ,sich   wälzen,    tummeln',    norw.    mdartlJ bultra  , lärmen,  tummeln',  abl.  norw.  mdartl.  baltra  ,sich  wälzen,  tummeln';
lit.  beldii,  -eti  und  beldziu,  belsti  ,pochen,  klopfen',  ablaut.  bildu,  bildeti jdröhnen,  poltern',  bdldau,  -yti  ,klopfen,  stark  poltern',  baldas  ,StößeP: lett.  beizt  ,schlagen'  (vielleicht  Kontamination  von  *beUu  =  lit.  beldiiu mit  telz-  ,schlagen',  Mühlenbach-Endzelin  Lett.-dt.  Wb.  278).
WP.  II  184,  WH.  I  560 f.
bheleg-  ,glänzen',  Erw.  von  bhel-  ds.
bhelg-:  ai.  bhdrgas-  n.  , strahlender  Glanz'  {*bhelgos)',  Bhfgavah'FL ,mythische  Priester  des  Blitzfeuers';  lett.  balgans  , weißlich';  vielleicht hierher  aksl.  blag^  ,gut',  russ.  (alt  und  mtdarl.)  bölogo  Adv.  ,gut',  eig. ,licht'  (Gegensatz  , dunkel':  ,böse');  toch.  AB  pälk-  , brennen,  leuchten, sich  erhitzen',  A  pälk,  B  pilko  ,Blick',  A  polkämts  , Gestirn'  (:  lit.  balgans), B  empalkaitte  ,nachlässig'  (Negation  -f  *palk-  _,leuchten'  neben  pälk-) ;
bhleg-:  gr.  q)Xeya)  , brenne,  senge,  zünde  an',  (pXeye&oj  ,senge,  setze  in Brand;  intr.  brenne,  stehe  in  Flammen',  cpUyfia  n.  ,Brand;  Entzündung] Schleim',  q)Uyuovr}  f.  , Entzündung;  Leidenschaft;  Brunst',  (pleyvag'  dstdg ^avd-og  Hes.  (Adj.  ,feurig  rot')  ^Ao^,  cpXoyiiög  , Flamme';
\a.t.flagrö,  -äre  , flammen,  lodern,  brennen',  wozu  wohl  flamma  ,Flamme* als    *flagmä,    osk.    Flagiui   etwa  ,Fulgurätöri' ;    neben  fläg-    (red.-stufiges
125
*hhl  cjvö-   *hhlegnid  oder  wegen  (pXoyi.i6g,  (pl6^  eher  Hldogma)  steht  schwund- fio-es  bhlg'y  lat.  fiäg-  in  lat.  fulgö  und  fulgeö,  -ere,  fulsl  ^blitzen,  schim-
ern    leuchten^,  fulgor,  -öris  ^das  Bhtzen,  Schimmer^  GLinz^,  fulgus,  -uris BlitZ;  Schimmer^;  fulmen  (*fulgmen)  ds.; ^    mir.  imhlissiu  ^Augenstern'   (^mhhi-hhlg-s-,  
########## printed p.156 (leaf 164) ##########
us  -g-sq-)  ,hin  und  her,  seitwärts  schleif dern,  hin  und  her  reisen,  umhersausen^
WP.  II  209,  WH.  I  511  f.
bhlagh-men-  ,Zauberpriester^;  ursprgl.  wohl  Neutrum  ,Opferhandlung^
Air.  brahmdn-  m.  ,Zauberpriester^,  brdhman-  n.  , Zauberspruch,  Andacht^;
messap.  ßXaixivi  ,Priester'^;  lat.  flämen,  -inis  m.  ,Opferpriester^  (nicht  altes
*-en).
Wegen  der  zahlreichen  Übereinstimmungen  in  der  religiösen  Termino- logie zwischen  dem  Italischen  und  Indoiranischen  ist  diese  Gleichung  der] Erklärung  von  flämen  aus  *bhlad-{s)men,  angebl.  ,Opferhandlung^  (zu  got.-^ 6 ?ö<a7i  , verehren^,  an.  blöta,  ags.  blötan,  ahd.  bluozan  ,opfern^,  an.  blöt  n. ,Opfer^  [-es-St.,  vgl.  finn.  hiote  ,Zaubergesang^  aus  urgerm.  ^blötes],  ahd. bluostar  n.  ds.,  usw.),  vorzuziehen.  Vgl.  auch  Dumezil  REtlE.  1,  377,  der noch  arm.  baljal  , streben  nach^  vergleicht. WP.  II  209,  WH.  I  512  f.,  865  f..  Feist  100  f.,  580  a.
bblB'  ,heulen,  laut  weinen,  blökend
Lat.  fleö,  flere  {^bhleio)  ,(be)weine^;
lett.  bleju,  biet  ,blöken^;
r.-ksl.  bUju,  blejati  ,blöken*^  (daneben  skr.  blejlm,  blejati  ,blöken^  usw.,
.    mit  g);  mhd.  blzjen  ,blöken'  (germ.  Hlejan  ==  lat.  fieö)]  ahd.  bläzan,  nnd.
.    blässen,    ags.    blztan,    engl,    to    bleat    ,blöken',    ags.    blagettan,    blxgettan
,schreien^,   ndd.    blage   n.  ,Kind'';    mhd.  bleren,   blerren   ,blöken,   schreien^,
155
I  d    plärren,  jplären  (auch    ^weinen')^   ndl.  Maren  ^blöken^^   engl,  to   blare IrUllen^'    ablautend    mhd.    blürjeii,    blilelen    [^hlöljan),    dissimil.    hrüelen 'brüllen*''    schwundstufig-    mhd.    hral    ,Schrei^    Schwab,    hralh    ^schreien^ \Vl    6.  hhel-  und  die  Schallwurzel  hU-. WP.  n  120,  WH.  I  516.
bbl^d-,  hhld"  ,aufsprudeln,  heraussprudeln,  auch  von  Worten*.
Gr.  q)lEdo}v  , Schwätzer',  cplsöcov  f.  , Geschwätz*;  (pXrjdcjvTa'  Xrqovvta lies.;  TtacplaC^o)  , brodle,  brause';  hierzu  auch  Aor.  qjXadsTv  (intrans.)  , zer- reißen'; vgl.  zrur  Bedeutung  lat.  fragor-,
mit  Abtönungsdehnstufe  bhlod-  sdv,  indläidi  ,prahlt,  rühmt  sich',  indla- diid  ,das  Prahlen*  (Hnd-bläd-  ,sich  aufblasen  oder  große  Worte  machen') und  lett.  blädu,  bläzt  , schwatzen' ;
schwundstufig  ahd.  uz-ar-pulzit  ,ebullit' ;
nhd.  platzen,  plätschern  sind  wohl  sicher  jüngere  Schallbildungen.
WP.  II  210,  216,  WH.  I  515,  518.
Zu  3.  bhel:
bblegn'  »sich  aufblähen,  schwellen*.  Erw.  v.  bhel-  , aufblasen'.
Gr.  q)X€ip,  -ßög  f.  ,Ader*,  (pleßdtovTsg'  ßQvovreg  Phot. ;   ahd.  bolca,  bul- chumia  (*bhlgu-)  ,bulla'. WP.  II  215,  WH.  
########## printed p.158 (leaf 166) ##########
Jxvrai  Hes.,  Tie- q>loLdivai'  (plvy.xavovad'ai  Hes.,  qiloLÖao),  -£w,  -taw  ,gären,  brausen',  dLq>loiü- f.iög  ,Schaum,  Geifer'  (a-  =  n  ,^y');  vermutlich  auch  cpXoiaßog  ,das  Bran- den des  Meeres,  das  Kampf getümmel',  7toXvq}Xoiaßog  d-dXaaaa  (*q)Xoido- ßog,  Formans  nach  Schallwörtern  wie  xövaßog^  ^gaßog?)]
vielleicht  hierher  mir.  bläed  ,Gebrüll'  (daraus  cymr.  bloedd  ds.);
engl,  bloat  ,ansch wellen'  (*blaitön  =  g)XoMcü)',
lett.  blistu,  bliduj  blizt  und  bliezu,  -du,  -st  ,aufdinsen,  dick  werden'.
WP.  II  210  f.
I
bhleig-,  bhlig'  ,glänzen'.  Erw.  von  bliUi-  ds.,  wie  bhleiq-.
Ags.  bllcan  ,glänzen',  as.  bllkan  ,glänzen',  ahd.  bllhhan  st.-V.  ,bleich werden',  mhd.  blichen  st.-V.  ,glänzen,  erröten',  aisl.  bhkja,  bleik  ,er- 1 scheinen,  glänzen,  leuchten';  aisl.  bleikr,  ags.  bläc,  ahd.  bleih  ,bleich,  blaß'; ahd.  bleihha  ,Weißfisch,  Plötze',  norw.  bleikja  und  blika  ds.;  aisl.  blik  n. ,leuchtender  Glanz;  Gold,  Goldblech',  ahd.  bleh  ,(*glänzendes)  dünnes Metallplättchen',  nhd.  Blech,  mnd.  blick  ds.;  ags.  blike  m.  (Hliki-)  ,bloß- gelegte  Stelle';  ahd.  blic,  -eches  ,schnelles  Glanzlicht,  Blitz',  mhd.  blic, -ckes  ,Glanz,  Blick,  Blitz',  nhd.  Blick,  ahd.  blecchazzen  {Hlekatjan),  mhd.
157
hliczen,  nhd.  blitzen]  as.  bliksmo  ^Blitz^,  aschwed.  blixa  ^blinzeln^^  nschwed. auch  ;blitzen^
Lit.  blizgüj  -Ui  ^flimmern,  glänzen^  bly^kiuj  bhjsketi  ^funkeln,  schimmern, (fliinzen^,    blykHü,    blyskaü,    blykUi    ,erbleichen^,  ablaut.    blaikstaüs,    -ytis
eich    aufklären,    vom    HimmeF;    lett.    blaiskums   ,Fleck^,    meln-blaiskams ^dunkelgrau^
Russ.-ksl.  blesH  ß\2ii\z'  (Hhloig-sko-)]  ablautend  aksl.  bliskz  ,Glanz^ und    *hlhsH   in    cech.    hlesk.    Gen.    alt   hlsku   ^Blitz'^,   aksl.    bhUq,    bhHati
crläazen^;  Iter.  bliscajq,  bliscati  s§.
'^WP.  II  211  f.,   EM.  398,   Trautmann  34,   Meillet  Slave  commun^  133, Specht  Dekl.  144.
bblciq-  ,glänzen'^.  Erw.  von  bhW-  (:  bhel-)  ds.,  wie  bhUig-.
Ags.  bösige  (*blaigi5n-)  ,Gründling^;  mnl.  mnd.  blei(g)  und  bieger,  nhd. Bleihe,  Blei  ,Fischnamen^;  daneben  mhd.  blicke  ,Cyprinus',  nhd.  Blicke (norw.  dial.  blekka,  nhd.  Blecke  ,Weißfisch^  von  der  e-Wz.  bhleg-?)]  in anderer  Bedeutungswendung-  (,glänzen  :  blicken^)  aisl.  bligr  ,starr  und  stier hinsehend'^,  bligja  ,hinstarren^
Dazu  russ.  bleknuU  ,bleichen,  verschießen,  welken^,  bleklyj  ,fahl,  matt^ welk^,  blekoH  ,Gleisse,  Aethusa  cynapium^,  poln.  blakiiqc  ,verschießen, verbleichend
WP.  II  211.
bblendh'  ,fahl,  rötlich';  ,undeutlich  schimmern';  ,trübe  sein  oder  machen' (auch  durch  Umrühren  des  Wassers  usw.);  ,irren,  schlecht  seh
```


## [2026-09-05T06:24:02.929Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bhleu\\|bhleu-\\|bhleugh\\|bhlSu\\|bblcu\\|bbleu\" POK_01.txt | head -20\necho \"=== belgh ===\"\ngrep -n \"bhel.h-\\|bbel.h\\|balgi\\|Balg\" POK_01.txt | head -20",
 "description": "Locate bhleu- and bhelgh- in Pokorny OCR"
}
```


### [2026-09-05T06:24:02.998Z] TOOL RESULT

```
1663:Hierher  ferner  2.hhel-]  hheleg-\  bhlei-,  -g-j  -k--,  bhlendh-;  bhles-]  bhhu^ -k-j  -S-]  bhleuo-',  bhlndho-;  bhhido-.
1718:^isl.  bialki  (*belkan-)  .Balken';  ablaut.  (Halkan-):  ags.  balca,  bealca: hd.  as.  halko  ^Balken^;  aisl.  balkr  ^Scheidewand,  Abteilung'^,  bglkr  ,Ab- teilun*^^'  schwundstuf.  ags.  bolca  m.  ^Laufplanke^;  aber  ahd.  bloh{h),  mhd. hloch  nhd.  (ndd.)  Block  ,Klotz,  Bohle^  enthält  idg-,  u,  also  aus  idg.  *bJduko- oder  falls  mit  germ.  Konsonantenverschärfung,  aus  "^bhlugo-,  zu  mir.  blog Bruchstück',  weiter  vielleicht  zu  got.  bliggivan,  ahd.  bliuwan,  nhd.  bleuen 'schla<^en';  aus  idg.  *bhleu-ono- ;   s.  unter  bheleu-.
2222:S.  auch  unter  1.  bhleu-  und  bhhido-s.
2258:bhleu-    , aufblasen    (schnauben,    brüllen),    schwellen,    strotzen,    überwallen, fließen',  Erw.  von  bhel-  , (aufblasen),  aufschwellen'.
2280:Hochstufe  bhleu-  in  ags.  un-bleoh  ,furclitlos'  (Suffix  -ho-),  mit  gramm. Wechsel;  aisl.  bljügr  ,verzagt',  blygd  ,Scham'  {*bleugipo),  ablautend  ahd. blügo  K^Y.,  mhd.  blüc,  5Ziwc  , schüchtern',  ahd.  blügisön,  blüchisön  ,zwei- feln',  ags.  blycgan  (*blugjan)  ,erschrecken'  (trans.);  vgl.  lit.  blükstu,  -äti ,schlaff  werden'.
2283:bhleu'{k)-,  (-S-)  ,brennen'.  Erw.  von  bhel-  ,glänzen'.
2284:*bhleu-s-  in  gr.  7tSQL-nscpXevaf.i€7'og  nvql  ,vom  Feuer  umlodert',  ircicpXevüe, n^QicpXio)  ,versenge  ringsum';  aisl.  blys  n.  , Flamme',  ags.  blysa  m.  ,Flamme,. Fackel',  mnd.  blüs  , Fackel',  ags.  blyscon  , erröten',  engl,  blush.
2286:*bhleu-k-  m  mlid.  hliehen  , brennend  leuchten*,  ahd.  hluhhen.
2295:bhleus-  etwa  , schlaff'?
=== belgh ===
1719:Hino-eo"en  gehören  wohl  zu  *bhelgh-  ^schwellen'  von  einer  ßedeutungs- vermittlung  ,dick,  schwellend'  aus:
1761:bbelgh'  ,schwellen;    Balg   (aufgeblasene   Tierhaut),    Kissen,  Polster'  (Erw.
1769:got.  balgs  ra.  ,Sclilauch',  aisl.  belgi^  m.  ,abgestreifte  Tierhaut,  Balg Bauch',  ahd.  mhd.  balg  ,Balg,  Schlauch,  Blasebalg,  Schwertscheide',  agg, bielg,  byl{i)g  ,Balg,  Beutel',  engl,  belly  ,Bauch',  bellows  ,Blasebalg'  (germ. *balii-  m.,  vgl.  apr.  balsinis]  vielleicht  hat  auch  ai.  barhls-j  av.  barezii, idg.  -i-s-  als  Erw.  dieses  i-St.);  .
2964:Ai.  dar-  ,bersten  machen,  spalten,  sprengen*^,  Präs.  der  leichten  Basis' ddrsi,  adar,  ddrtj  w-Präs.  der  schweren  Basis  dfnäti  ,zerspringt,  birst^ Opt.  dfräyät,  Perf.  daddra^  Partiz.  dj-ta-j  von  der  schweren  Basis  dirnd-i Kaus.  darayati,  Intens,  dardirat,  ddrdarti  (vgl.  av.  darddar-  ,spalten'] dech.  drddm,  drdati  , rupfen,  abrupfen'),  dardarlti  ,zerspaltet',  dara-h  mj darl  f.  ,Loch  in  der  Erde,  Höhle'  (:  gr.  dogög  ,Schlauch',  lett.  nuddaraS ^Abfall  von  Bast',  ksl.  razdorb),  dfti-h  m.  ,Balg,  Schlauch'  (=  gr.  ödgatg^ got.  gataürps,  russ.  derth),  darmdn-  m.  ,Zerbrecher'  (:  gr.  Ö€Q(.ia  n.),  wo-] neben  von  der  schweren  Basis  ddriman-  , Zerstörung';  -dätn-  ,zerspaltend^ (==r  gr.  dfJQig),  dära-  m.  ,Riß,  Spalte,  Loch',  däräka-  , zerreißend,  zer-l spaltend',  dari-  in  dardarl-ti,  darl-man-  mit  i  für  1=9  (vgl.  Wacker- nagel Ai.  Gr.  I  20),  kaum  nach  Persson  Beitr.  779  von  der  /-Basis;  npers.| Inf.  diriSarij  darlöan,  jüd.-pers.  darln-iSn]
```


## [2026-09-05T06:24:06.554Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1755,1775p' POK_01.txt\necho \"===== bhleu- entry =====\"\nsed -n '2255,2282p' POK_01.txt",
 "description": "Print Pokorny bhelgh- and bhleu- entries"
}
```


### [2026-09-05T06:24:06.605Z] TOOL RESULT

```
Acorn.  bal  f.,  pl.  -ow  ,Krankheit',  mbr.  baluent]
got.  balwa-ivesei  jy.ay.la\  balwjan  ,quälen',  ags.  bealo  ,übel,  böse',  aisl. bql,  Dat.  bglve  ,Unglück',  ahd.  balo,  Gen.  öaZazües  , Verderben' ;  got.  bligg- tcan  (*bleuiian)  ,schlagen',  ahd.  bliuwan,  nhd.  bleuen  ds.,  mengl.  blowe ,Schlag',  aisl.  blegde  m.  (*blauuiäan-)  ,Keil';
abg.  boh  ,Kranker',  boUti  , krank  sein'.
Über  nhd.  Block  usw.  s.  unter  5.  bhel-.
WP.  II  189,  Hirt  Idg.  Gr.  II  150,  Feist  79,  100,  Specht  Dekl.  133.
Daneben  eine  Wzf.  bhleii-  :  bhhu-  :  bJilü-,  s.  dort.
bbelgh'  ,schwellen;    Balg   (aufgeblasene   Tierhaut),    Kissen,  Polster'  (Erw.
von  bhel-  ,aufblasen'  usw.).
Ai.    barhü'   n.   ,Streu,    Opferstreu'  =  av.  bardzis-  n.  ,Polster,    Kissen'
npers.  bälis  , Kissen';   ai.  upa-bdrhana-m,   npa-bdrhanl  f.  , Decke,  Polster';
Ob  mit  Asp.-Diss.  gegen  das  Formans  -ha-  hierher  ai.  bdrjaha-h  , Euter'?
ir.    bolgaim    ,schwelle',    bolg   f.   ,Blase',    bolg  m.   ,Sack,    Bauch,    Hülse,
126  '
,  Hose',  mir.  holgach  f.  ,Beule,  Blase,  Blatter;  Pocken',  bolgamm  ,Schlucl^^ cymr.  hol,  bola,  holy  ,Bauch,  Sack',  hui  ,Sainenhülse'  (PL  von  holy),  bret; holc'h  ,cosse  de  lin',  vann.  pehl-en  (aus  *pehl-)  ds.,  gall.  bulga  ,Ledersac]i< (daraus  ahd.  hulga  ,lederner  Wasserbehälter*);  gall.  Belgae  ,die  Zornigen^
got.  balgs  ra.  ,Sclilauch',  aisl.  belgi^  m.  ,abgestreifte  Tierhaut,  Balg Bauch',  ahd.  mhd.  balg  ,Balg,  Schlauch,  Blasebalg,  Schwertscheide',  agg, bielg,  byl{i)g  ,Balg,  Beutel',  engl,  belly  ,Bauch',  bellows  ,Blasebalg'  (germ. *balii-  m.,  vgl.  apr.  balsinis]  vielleicht  hat  auch  ai.  barhls-j  av.  barezii, idg.  -i-s-  als  Erw.  dieses  i-St.);  .
aisl.  Partiz.  bolginn  ,geschwollen',  Kaus.  belgja  , aufschwellen  machen' as.  ags.  belgan  St.-V.  ,zornig  sein',  ahd.  belgan  ,aufschwellen',  refl.  ,zö^ nen',  afries.  Partiz.  ovirbulgen  ,erzürnt';
aisl.  bylgja  ,Woge',  mnd.  bidge  ds. ;  *bul{h)stra-  in  aisl.  bolstr  m.  ,Kisseii' ags.  bolster  n.  ,Polsteri  Kissen',  ahd.  bolstar  ds.,  ndl.  bolster , Fruchtbalg,  Hülse'
apr.  balsinis  ,Kissen'  (*bholghi-nos),  pobalso  , Pfühl',  lett.  pabälsts ,Kopfkissen'  (und  , Stütze',  s.  oben  S.  123);  slov.  blazina  ,Kissen,  Matratze] Bettpfühl;  Fuß-  oder  Handballen'  (und  , Dachbalken,  Querbaum  des* Schlittens,  Rungstock',  s.  oben  S.  123),  skr.  blazina  , Kopfkissen,  Polster^ti Federbett';  russ.  bolozem,  m.  , Schwiele,  Beule,  Leichdorn,  Hühnerauge^! (aber  russ.  dial.  bölozno  , dickes  Brett').  Hierher  wohl  als  ven.-ill.  Lw.^t apr.  balgnan  n.,  alit.  balgnas,  lit.  balnas  , Sattel'  (wohl  aus  ,Kissen').  Weitere  ' baltoslav.  Formen  s.  oben  S.  123.  -|
WP.  II  182  f.,  WH.  I  122.  Vgl.  über  gr.  nolyog  ,Ledersack'  Vendryes BSL.  41,  134  f.
bhen-  ,schlagen,   verwunden';    auch  von    durch    den   Schlag   böser   Geister bewirkter  Krankheit  (avest.;  vgl.  zu  diesem  Aberglauben  Havers  IF. 25,  380  f.) Av.  bqnaydn  ,sie  machen  krank',  banta-  , erkrankt,  siech'; got.  banja  , Schlag,  Wunde,  Geschwür',  aisl.  ben,  ags.  benn  f.,  as.  beni- tüunda   ,Wunde';    aisl.  bani   m.  ,Tod;    Mörder',   ags.  bana^    ahd.    as.  bano ,Totschläger,  Mörder',  ahd.  bano,  mhd.  hane,  ban  ,Tod,  Verderben';    viel- leicht auch  mhd.  bane,  ban  f.  und  m.  ,Bahn,  Weg'  als  ,*Durchhau  durch einen  Wald'  oder  ,*festgeschlagener  Weg';   mir.  epit  f.  , Hippe'  aus  *ek8- bhen-tl-  corn.  bony  ,Axt';  aber  cymr.  &on-cZws^ , Ohrfeige' enthält  bon  , Stock'. Av.  bata-j  wenn  ,geschrotet,  vom  Getreide',  könnte  als  *bhn-to-  verwandt sein,  ist  aber  wegen  der  unsichern  Bed.  nur  mit  Vorbehalt  zu  nennen. WP.  II  149,  Feist  80.
bbend'  etwa  ,singen,  schön  klingen,  jauchzen'.
===== bhleu- entry =====
WP.  II  216,  218,  Trautmann  34  f.,  Endzelin  KZ.  52,  112,  Specht  Del 58,  117.
Gehört  wohl  zu  1.  bhel-.
hhles-  ,glänzen^,  bisher  nur-im  Germ,  nachweisbare  Erw.  von  bhel-  ,glänzen* Mhd.  blas  ,kahl,  bleich^  (nhd.  blaß)  n.  ,Fackel,  brennende  Kerze^^  a^ bloßse  ,Fackel,  Feuer^,  engl,   blaze  ,Glut;   weißer  Stirnfleck^,  ahd.  blas-n ,Pferde  mit  einer  Blässe^  (lichtem  Fleck  auf  der  Stirn),  mnd.  bles^  blesn (*blasjö)    ,Blässe^,   aisl.    *bles-  in   blesöttr  ,mit  einem  weißen  Fleck,  einer Blässe  gezeichnet^  und  in  Kompos.  auf  -blesi. WP.  II  217.
bhleu-    , aufblasen    (schnauben,    brüllen),    schwellen,    strotzen,    überwallen, fließen',  Erw.  von  bhel-  , (aufblasen),  aufschwellen'.
Gr.  q)Xe{/)(x)  , strotze,  bin   übervoll',    ^Isvg  (*0X7]vg,   dehnstufig),   ephes. 0X€cog  {*Olrjfog)  Beiname  des  Dionysos  als  Vegetationsgottes;  vermutlich^ von  der  Üppigkeit  des  Wuchses  auch  att.  (pXscjq,  jon.  (pXovq  , Schilfgewächs*; q)loLü)    (*cplofia))    , schwelle,    strotze,    bin    in    Blüte',    vft€Qq)XoLog    ,üppig^ wachsend'  oder  ,überaus  saftig',  OXoTog,  OXola  ,Beiname  des  Dionysos  und- der  Köre  als  Vegetationsgottheiten',  wohl  auch  cpXoiög,  (pX6og  , Rinde,  Hülse*  j":
ablautend  cpXvu)   , walle  über,  sprudle,   schwatze;    bin  fruchtreich',    äno- cpXvsiv'  äTtsQsvysad-ai  Hes.  cpXvog  m.  , Geschwätz*,  q)XväS  , Geschwätz,  Possen;' Possenreißer' ;
lit.  blidujuy  bliöviauj  bliduti  , brüllen,  blöken',  bliiivauti  ,brüllen',  lett. blaünu,  bVdvu,  blaut  ds.;  aksl.  bl'ujq,  bthvati  , speien,  erbrechen'  (beruht auf  altem  Präteritalstamm,  vgl.  lit.  bliüvo  aus  idg.  *bhluuä-)]  dazu  viel- leicht auch  apr.  bleushy  , Schilf  (würde  in  der  Bed.  zu  gr.  (pXiwg  stimmenl).
Mit  einer  s-Erw.  nd.  Mustern  , heftig  blasen,  stürmen,  schnauben',  engl. bluster  ,brausen,  lärmen*  und  skr.  bljuzgati  ,mit  Geräusch  strömen,  dummes Zeug  schwatzen';  auch  skr.  blihati  usw.?  (s.  unter  bhlei-s-).
Mit  dentalen  Formantien:  mhd.  blödern  , plaudern'?  (eher  junges Schallwort;  vgl.  Kluge ^^  unter  plaudern)-,  eher  Schweiz,  blöder  ,große Blase  usw.',  blödem  , sprudeln,  wallen',  nhd.  Pluderhosen-,  vielleicht  skr. blütiti  jUngereimt,  unpassend  sprechen',  Berneker  62;  über  ahd.  blät{t)ara ,Blase^  {Hle-drö-)  s.  S.  121;
159
mit  'd'  (ursprgl.  Präsens  bildend?):  g)XvSatü  ,fließe  über,  zerfließe,  werde weich',   q)lvdccQ6g   ,niatschig',   iy,cpXvvdaveiv  ,aufbrechen,   von   Geschwüren*.
£--Er Weiterung  hhleug^-  (vgl.  die  Wzform  hhlegu-):
o-r.  oivö-cpXv^  , weintrunken';  cpXvt.w  , aufwallen,  überwallen,  auch  mit Worten';  cplvytvLg,  cplv-Azaiva  , Blase';  aber  nofi-cpölv^  , Brandblase,  Schild- buckel' bleibt  fern;
lat.  fluö,  -ere,  flüxi,  flüctum,  jünger  flüxum  , fließen,  strömen',  flücUis, •üs  , Strömung,  Woge',  flümen  (*fleugsmen)  , strömendes  Wasser,  Fluß', conflüges  alat.  , Zusammenfluß  zweier  Gewässer',  fluvius  ,Fluß'  (vom  Präs. jluö  aus),  flustra  Nom.  PI.  , Meeresstille'  (*flugstro7n)'
ob  hierher  (mit  Nasalierung)  cjmr.  blyngu  , zornig  werden',  blwng  , zornig',, bret.  blouhi  , tadeln'?
WP.  II  213 f.,  WH.  I  519 f.,  Trautmann  35;  anders  EM.  372.
1.  bhlea-  :  bhlQU- :  bhlü-  ,glänzen',  auch  von  weißem  Hautausschlage  Narben^
Schinn  usw.  Ableitungen  zu  1.  bhel-.
Russ.  blju-sc  ,Efeu'  (Specht  Dekl.  117);  poln.  biysk  (Hhlü-sk-)  ,Blitz'; sorb.  blu-znd  ^Narbe^^  wruss.  blu-znd  ^Webefehler';  lett.  blau-zgaSj  blau-znas,. lit.  blü-zganos  ^Schinn^^  lett.  blü-zga  ^die  sich  ablösende  Haut',  blu-zga ,kleine  Teilchen^  Bohrmehl'  usw.
Specht  Dekl.  117.
Vgl.  die  Parallelbildungen  unter  1.  bhlei-.
2,  bhlea-  :  bblou-  :  bhlü-  ^schwach,  elend'  (wohl  aus  ,geschlagen').
Gr.  g)lavQog,  cpavXog  (beide  dissimil.  aus  *(pXavXog)  ^geringfügige  schlecht'*
got.  blaupian  _,abschaffen'  (eigentl.  ^schwach  machen'),  aisl.  blaudr  ^furcht- sam',  ags.  blead  ,blödee  scheu',  ,mit  jo-Suffix  as.  blödi  , schamhaft',  ahd. blödij  mhd.  bloede  ^zerbrechlich,  zaghaft',  nhd.  blöde;
neben  idg.  *bhl9u-to-  steht  eine  d-Erweiterung  in  aisl.  blautr  ,weichlich,. furchtsam',  ags.  bleat  ,arm,  elend',  mndd.  blöt,  mhd.  blöz  ,bloß',  nhd.  bloß (ahd.  bloß  mit  merkwürdiger  Bedeutung  ,stolz');
Hochstufe  bhleu-  in  ags.  un-bleoh  ,furclitlos'  (Suffix  -ho-),  mit  gramm. Wechsel;  aisl.  bljügr  ,verzagt',  blygd  ,Scham'  {*bleugipo),  ablautend  ahd. blügo  K^Y.,  mhd.  blüc,  5Ziwc  , schüchtern',  ahd.  blügisön,  blüchisön  ,zwei- feln',  ags.  blycgan  (*blugjan)  ,erschrecken'  (trans.);  vgl.  lit.  blükstu,  -äti ,schlaff  werden'.
bh[e)leu-  ist  offenbar  Parallelbildung  zu  5ÄeZew-  , schlagen'.
WP.  n  208  f.,  Hirt  Idg.  Gr.  II  150,  Feist  99,  Specht  Dekl.  133.
```


## [2026-09-05T06:24:15.231Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bhlei-\\|bblei\\|hhlei\" POK_01.txt | head -20\necho \"==== flos folium phyllon ====\"\ngrep -n \"folium\\|cpvXlov\\|(pvXXov\\|flös\\|flos,\\|blüh\" POK_01.txt | sed -n '1,40p'",
 "description": "Find bhlei- and bhel-4 bloom in Pokorny"
}
```


### [2026-09-05T06:24:15.303Z] TOOL RESULT

```
1663:Hierher  ferner  2.hhel-]  hheleg-\  bhlei-,  -g-j  -k--,  bhlendh-;  bhles-]  bhhu^ -k-j  -S-]  bhleuo-',  bhlndho-;  bhhido-.
1696:Dazu  4.  hhel-  , blühen'  usw.  und  die  Erweiterungen  hhelgh-,  hhUdh^^ bhlegu-,  hhlei-,  bJileu-  ^schwellen'  usw.
2214:Germ.  *blipia-  (*bhlei-tio-  oder  eher  *bhll-tio-)  ,\ic\\t,  heiter  (vom  Himmel, dann  von  den  Mienen,  der  Stimmung:)  fröhlich^  in  got.  bleips  ,gnädig, mild*^,  aisl.  blldr  ,mild  (vom  Wetter),  freundlich,  angenehm^,  ags.  bhpe ,heiter,  freundlich*^,  ahd.  blldi  ,heiter,  froh,  freundlich^,  as.  bllthön,  ahd. bilden  ,sich  freuend
2223:2.  bblei-  ^aufblasen,  schwellen^  strotzen^  überfließen'^  Erw.  von  hhel-  ds.
2226:bbleis-:    aisl.   bllstra   ,blasen,    pfeifen'?    (vgl.   got.  -blesan    unter    bheli bh(e)l-e-',    junge    Variation    mit   i  zur   Nachahmung    des   hellen   Tones?)' vielleicht  serb.   blihäm,  blihati   »überschwemmen;    speien;    den    Durchfall] haben';  blihnem,  blihnuti  ^anspritzen',  buig.  blici,  blikm,  blikvam  ^ergieße! mich,    ströme'  (wenn    nicht    als   ursl.  *blychajg    zur    w -Variante   von q)Xv(jü  usw.).
2262:Mit  einer  s-Erw.  nd.  Mustern  , heftig  blasen,  stürmen,  schnauben',  engl. bluster  ,brausen,  lärmen*  und  skr.  bljuzgati  ,mit  Geräusch  strömen,  dummes Zeug  schwatzen';  auch  skr.  blihati  usw.?  (s.  unter  bhlei-s-).
2275:Vgl.  die  Parallelbildungen  unter  1.  bhlei-.
2292:air.  blä  ,gelblich?*^  ist  spätes  ags.  Lw.?  Über  germ.  *bliwa-  ,Blei^ s.  unter  1.  bhlei-.
2297:bhlQido-s   ,licht,   blaß^,   zu   bhlei-  ,glänzen^,  von  einer  erw.  Wzf.  *bhlei-d-.  ■^.
2298:Aksl.   bled^  ,bleich,  blaß^  ==  ags.  blät  ,bleich,  bleifarben^;    ahd.  bleizza  ^'" ,Blässe^    Vielleicht  lit.  blaivas  ,nüchtern^  (wenn  aus  '^blaid-vas]   oder  von der  unerw.  Wz.  bhlei- j  s.  d.),   blaivaüs,  -ytis  ,nüchtern  werden;  sich  auf-   ;%, klären,  vom    Himmelt    Alb.    bZerönj  ,grüne^   von    einem   Adj.    *bTere  aus    £ Hled-re  (e  =  idg.  ai  oder  oi),  bUhure  ,blaß,  bleicht  |
2301:bhlig-  (:  *bbleig')    ,schlagen,    schmeißen^,    auch    bbligu-    (gr.   kelt.),  aus    # einem  wo-Präsens  *bhllg-uö  zu  deuten.
==== flos folium phyllon ====
282:Gr.  icxvQOv  , Spreu'  s.  unter  s-Formantien ;  lat.  acus^  -üs  L  , Nadel;  Fiscli- name',  acuere  , schärfen',  acümen  , Spitze',  acia  (f^acu-iä)  , Faden  zum Nähen',  aquifolium  (neben  äcrifoUum)  , Stechpalme',  aculeus  , Stachel', accipiter  ,Habicht,  Falke'  (*acu-peter  ,schnellfliegendQ ;  gall.  acaunum (^akounon)  , Felsen';  ill.  ON  Äcumincum  heute  Szlankamen  ,Salzstein' (Banat);  nhd.  Achel  f.  , Ährenspitze'  aus  ndd.  aggel  (mit  spirant.  g)  aus idg.  *aku-lä]  ags.  äiüel  m.  , Gabel',  anord.  sotS-äll  , Fleischgabel'  (germ. *ahwala-y  idg.  *dku-olo-) ;  falls  hierher  gallo-lat.  opulus  , Feldahorn'  (Mar- strander,  Corr.  germ.-celt.  18),  würde  idg.  *oku-olo-  anzusetzen  sein;  über anord.  uggr  usw.  s.  e/o-St.,  über  ags.  ear  s.  5-Formantien;  cymr.  ehill ,Bohrer',  mbr.  ebil  ,Pflock,  Nagel'  (*aku-llio-) ;  halt.  *ahis  in  lett.  ass , scharf,  spitzig',  lit.  asutai  m.  PL  , grobe  Pferdehaare'  =  slav.  *o§uta  m. , Distel'  in  ksl.  os^U,  russ.  osöt.  Ob  hierher  toch.  A  acäice  ,rauh'  (Van Windekens  Lexique  15)?
557:andh-,  anedh-  ,hervorstechen,  sprießen,  blühen',  andhos  n.  Blume,  Kraut'.
559:dv^^ü)    ,blühe-,    äyavjQÖg    {*-es-ro-)    ,blühend'    usw.;     alb.     ende    {^andhön)
561:M  Hliite-,    endem    ^blühe"    (das  e  vom    P-räs.    *e    aus    *andhu):    toch.    A    ant,
562:Mir.  (linder,  aindir  .jung-e  Frau';  cymr.  anner  junge  Kuh*;  PI.  anneirod, neviiir-  enderic  ,vitulus%  cymr.  enderig  ,Stier;  Ochse^^  bret.  ounner  (Treg-. tinnoncir.  Yaiines  afinoer)  junge  Kuli'^;  hierzu  frz.  (T)andier  m.  ^Feuerbock, Widder'  auch  ^Mohn'  [=  junges  Mädchen'^  vgl.  ital.  madona,  fantina Mohir),  weiter  zu  bask,  andere  ,Frau',  iber.  FN  Andere,  Anderca,  MN Anderiis]  vielleicht  kelt.  Herkunft?  {^'andero-  ^blühend,  jung^?).
1696:Dazu  4.  hhel-  , blühen'  usw.  und  die  Erweiterungen  hhelgh-,  hhUdh^^ bhlegu-,  hhlei-,  bJileu-  ^schwellen'  usw.
1698:4.  hhel-   und    bhle-,   bhlö-,   ibJWs-   , Blatt,    Blüte,  blühen;    üppig  sprießen'
1700:Gr.  g)vXXov  , Blatt'  {*bhHiom)j  lat.  folium  ds. ;  mir.  bileöc  ,Blättchen'  (aua *6i7e  <  *bhelio-)]  hierzu  wohl  air.  bile  n.  ,Baum';
1701:hhle-j  meist  bhlö-  in:  lat.  flös,  -iHs  m.  ,Blume';  flöreö,  -ere  , blühen';  0  k. Fluusai  ,Flörae',  Fluusasiais  ,Flörälibus',  sabin.  Flusare  ,Flöräli'.
1702:Mir.  bläth  m.  , Blüte,  Blume',  cymr.  blaivd^  acorn.  blodon  ,Blüte'  (*bhlö  t-\ mbret.  (mit  -wen-Suffix)  bleuzven,  nbret.  bleufi(v)enn  ds.,  mit  ö'-Ableitun^r mhd.  bluost  , Blüte',  nhd.  Blust,  ags.  blöstma,  blösma,  blöstm  ,Blume',  an. blömstv  ds.,  ndl.  blasen  , blühen'  (=  mnd.  blasen  ,erröten',  s.  u.  bhles- ,glänzen') ;
1704:ahd.  bluojen,  bluoiven,  as.  blöjan,  ags.  blötoan  ,blühen';  ahd.  bluot  f. ,das  Blühen,  Blüte'  =  ags.  bled  f.  ,Sproß,  Zweig,  Blume,  Frucht';  aber got.  blöp  n.,  aisl.  blöd,  as.  ags.  blöd,  ahd.  bluot  ,Blut'  wohl  zu  *bhel~e- , sprudeln'.
2792:Ai.  dHldyati  , spaltet,  macht  bersten^,    ddlati  , birst'   (Bed.  von    pAdi ,springt  entzwei^  beeinflußt,  Güntert  Reimw.  48),  dalitd-h  ,gespalten, einandergerissen,  aufgeblüht',  dala-m  n.  ,Teil,  Stück,  Hälfte,  Blatt*,  da^ f.  , Erdscholle';  aber  Prakr.  dälä,    -i  ,Ast',   wohl  auch  daiidd-h,   -m  ,Sto! Prügel,  Strafe'  sind  nach  Kuiper  Proto-Munda  65,  75  nicht  idg.;
3334:dbsl-  ,blühen,  grünen'.
3336:gr.  d^dXlü)  ,grüne,  blühe,  gedeihe',  Perf.  Tid-rjXa,  dor.  Tsd-ala,  wovon  Präs, difjXso)^  dor.  d^aXeo)  ds.,  d-aXog  n.  ,junger  Sproß',  igid-rjXi^g  ,üppig  sprießend* sid-äXrjgj  dor.  ebd-aXr-g  ,üppig  sprießend  oder  blühend',  &aXX6g  ,iunger Sproß,  junger  Zweig',  d-aXla  ,Blüte,  blühendes  Wohlergehen,  bes.  PI.  fest- liehe  Freude,  Festgelage'.
3340:cymr.  dail  , Blätter'  (analogischer  Sg.  dalen),  acorn.  delen  ,Blatt'  usw (i-Umlaut  von  o),  mir.  duille  (*dolln{a)  Kollekt.  f.  ,Blätter',  gall.  nojxnedovXa ,quinque  folium'  (Dioskor.) :  leg.  *pimpe-dola.
3589:aisl.  draf,  engl,  draff  ,Berme,  Hefe',  mnd.  draf,  ahd.  trebir  PI.  ,Treber', anord.  drafli  m.  , frischer  Käse',  drafna  ,sich  auflösen',  norw.  drevja  ,weiche Masse';  geminiert  nl.  drabbe  ^Berme,  Bodensatz',  ndd.  drabbe  ,Schlamm'; schwed.  dröv  n.  ,Bodensatz'  {*dhräbho-),  ags.  dröf,  ahd.  truobi  ,trübe', got.  dröbjan,  ahd.  truoben  ,trüben,  verwirren',  ags.  drefan  ,auf rühren, trüben'  (dasselbe  Bed.-Verh.  wie  zwischen  gr.  ragdaacj  und  anord.  dreggiar).
3906:Got.  gadrahan  ,aushauen,  karo^sly^j  anord.  draf  n.,  ags.  droef  n.  , Ab- fall', anord.  drafna  ,sich  in  kleine  Teile  auflösen',  blöp-drefjar  m.  ,Blut- flecken';
4967:lit.  yrii,  zrti  ,sich  auflösen,  trennen,  pairas  ,locker';  rZtis  m.  ,BastsieV (mit  unursprünglichem  Schleifton,  wie  oft  in  i-Stämmen),  lett.  reta,  rete .Narbe',  rem  rudzi  ,undicht  stehender  Roggen';  lit.  eftas  ,weit,  geräumig' (,*auseinanderstehend');  von  der  leichten  Basis  retas  ,dünn,  weitläufig, selten'  (von  der  themat.  Wurzelf.  *(e)r-e-,  wie  auch:)  resvq,s  ,selten,  dünn', paresvis  , spärlich';
4968:aksl.  oriti  ,auflösen,  stürzen,  zerstören'  (Kaus.  '"^oreiö  ,mache  auseinander- gehen'), skr.  ohhriti  ,niederwerfen',  dech.  ohofiti  .zerstören',  russ.  razorüh  ds.
```


## [2026-09-05T06:24:24.632Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1688,1710p' POK_01.txt\necho \"=========== bhlei-2 ===========\"\nsed -n '2218,2232p' POK_01.txt",
 "description": "Print Pokorny 4.bhel- and 2.bhlei-"
}
```


### [2026-09-05T06:24:24.684Z] TOOL RESULT

```
Mit  Abtönungsstufe  *hhöl-  wohl  norw.  hol  ,brünstig,  von  der  Sau'  (ab- lautend hala  jbrünstig  sein').
Wurzelform  bble-:
Gr.  (pXrjvaq)og  , Geschwätz,  schwatzhaft',  g)Xr]v-€(x),  -da)  ,bin  schwatzhaft'; iaq)}.cxlvu)  wie  cpalvo)  von  hhä-,  Aor.  iKcplrjvai  , hervorsprudeln';
lat.  flö,  fläre  ,blasen'  (wohl  aus  *hhld-{ö),  aber  flemina  , Krampfadern'  ist wohl  Lw.  aus  gr.  cplsyixovrj -,  norw.  dial.  blcema  , Hautbläschen' ;  aschwed. blcemma  ds.;  ahd.  hlät(t)ara,  as.  hlädara  ,Bkse,  Blatter',  ags.  blcedre  ds., Red.-St.  aisl.  bladra  , Bläschen,  Blatter',  ahd.  usw.  blat  ,Blatt';  aisl.  blä- in  Zs.  ,übermäßig,  sehr';  mit  vorherrschender  Bed.  ,blasen'  ahd.  lO-Präs. bläjan,  hläen  , blasen,  blähen,  aufblähen',  ags.  bläiuan  , blasen'  (das  w  aus dem  Perf.),  ahd.  hlät,  ags.  hlced  , Wehen,  Hauch,  Windstoß',  aisl.  blcer ,Windstoß';  mit  -s-  got.  ufhlesan  ,aufblasen',  aisl.  hläsa  , blasen,  keuchen, aufblasen;  unpers.:  aufschwellen',  ahd.  bläsan  ,blasen',  hläsa  ,Blase',  blast
122
, Blasen,  Hauch',  ags.  hlcest,  aisl.  blästr  (*blestu-)  ^Blasen,  Hauch,  Schna\3 ben,  Zorn';  ^
lett.  hlhias  , Possen'  stammt  aus  dem  russ.  Lw.  hUdis  , Betrüger'.        M
Hierher  vielleicht  got.  hlöp  ,Blut',  s.  4.  hhel-.
Dazu  4.  hhel-  , blühen'  usw.  und  die  Erweiterungen  hhelgh-,  hhUdh^^ bhlegu-,  hhlei-,  bJileu-  ^schwellen'  usw.
WP.  II  177 f.,  WH.  I  515,  524f.
4.  hhel-   und    bhle-,   bhlö-,   ibJWs-   , Blatt,    Blüte,  blühen;    üppig  sprießen'
wohl  aus  hhel-  ,scliwellen'  im  Sinne  von  ,pflanzlicher  Üppigkeit'  uikJ , Schwellung  =  Knospe'.
Gr.  g)vXXov  , Blatt'  {*bhHiom)j  lat.  folium  ds. ;  mir.  bileöc  ,Blättchen'  (aua *6i7e  <  *bhelio-)]  hierzu  wohl  air.  bile  n.  ,Baum';
hhle-j  meist  bhlö-  in:  lat.  flös,  -iHs  m.  ,Blume';  flöreö,  -ere  , blühen';  0  k. Fluusai  ,Flörae',  Fluusasiais  ,Flörälibus',  sabin.  Flusare  ,Flöräli'.
Mir.  bläth  m.  , Blüte,  Blume',  cymr.  blaivd^  acorn.  blodon  ,Blüte'  (*bhlö  t-\ mbret.  (mit  -wen-Suffix)  bleuzven,  nbret.  bleufi(v)enn  ds.,  mit  ö'-Ableitun^r mhd.  bluost  , Blüte',  nhd.  Blust,  ags.  blöstma,  blösma,  blöstm  ,Blume',  an. blömstv  ds.,  ndl.  blasen  , blühen'  (=  mnd.  blasen  ,erröten',  s.  u.  bhles- ,glänzen') ;
got.  blöma  m.,  ahd.  bluomo  m.  ,Blume',  aisl.  blomi  m.  ds.,  blöm  Kollek- tiv ,Blume';
ahd.  bluojen,  bluoiven,  as.  blöjan,  ags.  blötoan  ,blühen';  ahd.  bluot  f. ,das  Blühen,  Blüte'  =  ags.  bled  f.  ,Sproß,  Zweig,  Blume,  Frucht';  aber got.  blöp  n.,  aisl.  blöd,  as.  ags.  blöd,  ahd.  bluot  ,Blut'  wohl  zu  *bhel~e- , sprudeln'.
Mit  e:  ags.  blced  m.  ,Hauch',  n.  ,Blase',  f.  ,Blüte',  ahd.  blät  ,Blüte'  (vgl. auch  ags.  blced,  ahd.  blät  ,Leben,  Hauch'  und   bJiel-  ,aufblasen');
mit  9:  ahd.  blat,  as.  blad,  ags.  blced,  aisl.  blad  n.  , Blatt';  toch.  K  peilt  ds.
WP.  II  176  f.,  WH.  I  518  f.,  Schwyzer  Gr.  Gr.  I  351.
5.  bhel-,    meist   mit   -5^- (-£-) Suffix    ,Bohle,   Balken':    bh^lQg-,    bb^lQ-n-g-r
bheleg-',  bblk-.
Einfaches  bhel-  in  ai.  bhurijäu  Du.  ,Arme,  Deichselarme';  gall.  *balä- kon  ,(Mauer-)Vorsprung',  cymr.  balog  , Zinne'  (M.-L.  890).
=========== bhlei-2 ===========
Lit.  blyvas  ,lila,  veilchenblau';  vielleicht  lit.  blawas  ,nüchtern'  (wenn nicht  als  *blaid-vas  zum  verwandten  *bhhido-s),  blaivaüs,  -ytis  ,sich  auf- klären, nüchtern  werden';   vielleicht  lett.  bllnet  ,lauern,  blinzeln'.
156  9
Toch.  A.  plyaskem  ^Meditation^??  (Van  Windekens  Lexique  97).
WP.  II  210.
S.  auch  unter  1.  bhleu-  und  bhhido-s.
2.  bblei-  ^aufblasen,  schwellen^  strotzen^  überfließen'^  Erw.  von  hhel-  ds.
Norw.  dial.  hleime,  aschwed.  hlema  ^Hautbläschen*^  (vgl.  norw.  blcema  ^j unter   bhel-^  bh(e)le-)'^    dän.  blegn(e)  ^Bläschen'   {*blajjinön),   ags.   biegen engl,    blain,    mnd.  bleine,    älter    dän.    blen{e)j    aschwed.    blena    ^Bläscher^ i^blajinön).
Daß   gr.  cpliä  ^Türpfeiler,  Türpfosten'   eig.  _,(*geschwollener  =)  dickS Balken'   sei   (Prellwitz  ^  und   Boisacq   s.  v. ;    Gdf.  *bhll-uä   oder   -sä), dürfte  erst  auswärtiger  Bestätigung;   rä  q)Xi(X€Xia  ^Blutgeschwulst'  ist  ai lat.  flemina  verderbt.
bbleis-:    aisl.   bllstra   ,blasen,    pfeifen'?    (vgl.   got.  -blesan    unter    bheli bh(e)l-e-',    junge    Variation    mit   i  zur   Nachahmung    des   hellen   Tones?)' vielleicht  serb.   blihäm,  blihati   »überschwemmen;    speien;    den    Durchfall] haben';  blihnem,  blihnuti  ^anspritzen',  buig.  blici,  blikm,  blikvam  ^ergieße! mich,    ströme'  (wenn    nicht    als   ursl.  *blychajg    zur    w -Variante   von q)Xv(jü  usw.).
bhleid-  (vermutlich  c?-Präs.  *bhli-d-ö).
Gr.  (plidaco  ^fließe  von  Feuchtigkeit  über,  schwelle  davon  auf,  ecpliö^v diSQQsev  Hes.,  (plidavsc  öiaggeZ  Hes.,  dianecploLÖev'  diayJxvrai  Hes.,  Tie- q>loLdivai'  (plvy.xavovad'ai  Hes.,  qiloLÖao),  -£w,  -taw  ,gären,  brausen',  dLq>loiü- f.iög  ,Schaum,  Geifer'  (a-  =  n  ,^y');  vermutlich  auch  cpXoiaßog  ,das  Bran- den des  Meeres,  das  Kampf getümmel',  7toXvq}Xoiaßog  d-dXaaaa  (*q)Xoido- ßog,  Formans  nach  Schallwörtern  wie  xövaßog^  ^gaßog?)]
vielleicht  hierher  mir.  bläed  ,Gebrüll'  (daraus  cymr.  bloedd  ds.);
engl,  bloat  ,ansch wellen'  (*blaitön  =  g)XoMcü)',
lett.  blistu,  bliduj  blizt  und  bliezu,  -du,  -st  ,aufdinsen,  dick  werden'.
WP.  II  210  f.
```


## [2026-09-05T06:24:42.344Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"فلوئور\" \"فلورسانت\" \"آنفلوانزا\" \"آنفلوآنزا\" \"انفلوانزا\" \"کلروفیل\" \"کلروفی\"; do echo \"### $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; done",
 "description": "Grep Mo'in for the European loanwords"
}
```


### [2026-09-05T06:24:44.023Z] TOOL RESULT

```
### فلوئور
MON_part1.txt:0
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
### فلورسانت
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
### آنفلوانزا
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
### آنفلوآنزا
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
### انفلوانزا
MON_part1.txt:1
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1
MON_part2.txt:0
### کلروفیل
MON_part1.txt:5
incoming/MON/MON_2vol_Adena_v1_djvu.txt:5
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4
MON_part2.txt:4
### کلروفی
MON_part1.txt:5
MON_part2.txt:4
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4
incoming/MON/MON_2vol_Adena_v1_djvu.txt:5
```


## [2026-09-05T06:24:47.110Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== انفلوانزا in MON_part1 ===\"; grep -n -m3 -A3 -B3 \"انفلوانزا\" MON_part1.txt\necho; echo \"=== کلروفیل in MON_part1 ===\"; grep -n -m6 -B2 -A3 \"کلروفیل\" MON_part1.txt | head -60",
 "description": "Show Moin entries for influenza and chlorophyll"
}
```


### [2026-09-05T06:24:47.176Z] TOOL RESULT

```
=== انفلوانزا in MON_part1 ===
18194-(امص.) جدایی؛ ج. انفکاکات. انفکاکث 
18195-قوی: (سیا.) جدای قوای فعالةً مملکت از 
18196-انفلاق: (60][3 [ع.] (سصل.) شکافته 
18197:انفلوانزا: ممعههنه زفر.] (۰) (پز.) نوعی 
18198-سرماخوردگی شدید و ساری. 
18199-
18200-انفیه: (۵-)2)2 [ع. انشه ] (ص‌نسه. نث 

=== کلروفیل in MON_part1 ===
11151-زیرا بصورت توده‌های سبز رنگی در داخل 
11152-آب قرار می‌گیرد. ریسه‌هایش به علت داشتن 
11153:ماده کلروفیل سبز رنگند؛ جل وزغ» بز 
11154-غسمه. 
11155-
11156-اسپیر ومتر : 26۱۲ظ-۲۵آجوع مر ۰ (بز.) آلتی 
--
75026-دانه‌های سبزننه عبارت است از 
75027-که در اين صورت به آن 
75028:کلروفیل «گویند و اگر از تعداد یدروژن‌ها 
75029-یک مولکول کاسته و در عوض یک اتسم 
75030:اکسیژن جای آن قرار گیرد کلروفیل «بدست 
75031:آید؛ خضرة الورق» کلروفیل. 
75032-سبط: 0۱ ([غ.] (.) فرزندزاده» پسر بسر» 
75033-نواده. قبله؛ ج. اسباط. 
75034-
--
88054-نوشند. شیر ه پر ورده: (گی.) (فره.) ماده‌ای کم 
88055-و پیش ازج و مغذی که در برگ‌های نباتات 
88056:از تبدیل شیرة خام بر اثر جذب کلروفیلی 
88057-حاصل شده و به جهت تغذ به اندام‌های 
88058-گیاهی بکار می‌رود؛ شیر قابل هضم گیاهی. 
88059-شیره خام: (گا.) محلول مواد مختلف
```


## [2026-09-05T06:24:54.221Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== کلروفیل: headword ===\"; grep -n \"کلروفیل:\" MON_part1.txt MON_part2.txt | head\necho \"=== فلور ===\"; grep -n \"فلور\" MON_part1.txt MON_part2.txt | head -20\necho \"=== فلوئ / فلوث ===\"; grep -n \"فلوئ\\|فلوث\\|فلوت\" MON_part1.txt MON_part2.txt | head -20",
 "description": "Grep Moin for fluor and chlorophyll headwords"
}
```


### [2026-09-05T06:24:54.366Z] TOOL RESULT

```
=== کلروفیل: headword ===
=== فلور ===
MON_part2.txt:8648:فلورن: ۵ (.) قطعه‌ای مسگ وک 
MON_part2.txt:8651:«فلور ی» در آمده. 
MON_part1.txt:81324:سوفلور: ۲ ا[دمنده ] (ص.) (نسم.) 
=== فلوئ / فلوث ===
MON_part2.txt:8630:فلوت: 01 (۰.) (مس.) نوعی نی تکمیل 
MON_part2.txt:8633:فلوت به سهولت می‌توان صداهای مختلف 
MON_part2.txt:8640:فلوت: 1 (ا. ) مجموع کشتی‌های جنگی 
MON_part2.txt:68007:را «فلوت‌پان» گویند و امروز به ساز دهنی 
MON_part2.txt:81629:سپرده به شکل فلوت درآمده است. ۳ 
MON_part2.txt:93227:تو خالی کرد و از آنها فلوت ساخت ولی
```


## [2026-09-05T06:25:03.787Z] TOOL CALL #23: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T06:25:03.794Z] TOOL RESULT

```


```


## [2026-09-05T06:25:06.074Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/fluorine",
 "prompt": "Give the full etymology text for fluorine, fluor, fluorescent, fluorescence, fluorspar as printed."
}
```


## [2026-09-05T06:25:06.653Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/influenza",
 "prompt": "Full etymology text for influenza and influence."
}
```


### [2026-09-05T06:25:12.441Z] TOOL RESULT

```
# Etymology Summary

**Fluorine (1813):** Coined by Sir Humphry Davy, "a name suggested to me by M. Ampère." Derives from fluor-spar (calcium fluoride/fluorite) plus the chemical suffix -ine. The element wasn't isolated until 1886.

**Fluor (1660s):** An old chemistry term for "minerals which were readily fusible and useful as fluxes in smelting." From Latin fluor meaning "a flowing, flow," from fluere "to flow, stream, run, melt." Applied to fluorine-containing minerals since 1771.

**Fluorescence (1852):** Coined by Sir George G. Stokes, "property possessed by some substances of glowing in ultraviolet light." Formed from fluor-spar, where he first observed the phenomenon, plus -escence (modeled on phosphorescence).

**Fluorescent:** Derived from fluorescence plus -ent suffix.

**Fluor-spar:** The historical mineralogical name for calcium fluoride, now called fluorite. This mineral was the source from which fluorine's name originated.
```


### [2026-09-05T06:25:14.018Z] TOOL RESULT

```
# Etymology of Influenza

The term "influenza" entered English in 1743, borrowed from Italian during a disease outbreak in Europe. The Italian word originally meant "visitation, influence (of the stars)," derived from Medieval Latin *influentia* in an astrological sense.

## Original Meaning

The word's roots reflect medieval beliefs about celestial influence. It comes from Latin *influere*, meaning "to flow into," composed of *in-* ("into") and *fluere* ("to flow").

## Historical Usage

Italians had applied the term to diseases since at least 1504, attributing them to "astral, occult, or atmospheric influence." A 1743 *Gentleman's Magazine* article documented: "a Sort of Plague has broke out there...they call it the *Influenza*."

## Connection to "Influence"

The parent word *influence* emerged in late 14c. English as "streaming ethereal power from the stars" affecting human character and destiny. This astrological terminology later expanded to describe any unseen force producing effects, eventually losing its celestial connotations.

The semantic shift from astral phenomenon to infectious disease reflects how pre-germ-theory societies understood illness as environmental or cosmic in origin.
```


## [2026-09-05T06:25:34.490Z] TOOL CALL #26: Bash

```json
{
 "command": "pdftoppm -f 85 -l 85 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg85 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 85 to PNG"
}
```


## [2026-09-05T06:25:35.169Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/blister",
 "prompt": "Full etymology text for blister (noun)."
}
```


### [2026-09-05T06:25:36.694Z] TOOL RESULT

```
total 10136
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 02:25 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb  189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  513902 Sep  5 02:15 bqt440.jpg
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
-rw-rw-r-- 1 sfmqrb sfmqrb    5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb   79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52793 Sep  5 02:18 mk79.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63329 Sep  5 02:25 pg85.png
```


### [2026-09-05T06:25:41.910Z] TOOL RESULT

```
# Etymology of Blister

The word "blister" originated around 1300, referring to a "thin vesicle on the skin containing watery matter." 

Its roots trace back through multiple language sources. The term possibly came via Old French *blestre* or Middle Dutch *blyster*, both meaning "swelling." These sources likely stem from a Scandinavian origin, such as Old Norse *blastr* ("a blowing") and *blæstri* ("swelling").

The ultimate origin is Proto-Indo-European *bhlei-*, described as "to blow, swell"—an extension of the root *bhel-* with the same meaning. This fundamental concept of swelling connects blister to many related English words like balloon, bold, bulk, and belly.

The verb form appeared later, first documented in the late 15th century meaning "to become covered in blisters," and by the 1540s referring to the action of "raising blisters on" something.
```


## [2026-09-05T06:25:45.545Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg85.png"
}
```


### [2026-09-05T06:25:45.919Z] TOOL RESULT

```

```


## [2026-09-05T06:25:45.915Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T06:26:00.056Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/fluo",
 "prompt": "Give the Latin entry \"fluō\" etymology in full, including the reconstructed PIE root and any note about de Vaan or *bʰleh₃w- / *dʰl-."
}
```


## [2026-09-05T06:26:00.254Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/folium",
 "prompt": "Give the Latin entry \"folium\" etymology in full (PIE root, cognates such as Greek phullon)."
}
```


### [2026-09-05T06:26:06.000Z] TOOL RESULT

```
# Latin "fluō" Etymology

The entry traces **fluō** to Proto-Indo-European *\*bʰlewH-* ("to overflow"), possibly extending *\*bʰleh₁-* ("to swell, blow"). 

The Latin form may derive from earlier *\*flowō* via vowel reduction from PIE *\*bʰleuH-(e/o)*, or alternatively from Proto-Italic *\*flūō* (from *\*flūjō*), traced to PIE *\*bʰluH-yé-ti*.

De Vaan (2008) is cited as the primary etymological reference source for this reconstruction, appearing in the *Etymological Dictionary of Latin and the other Italic Languages*.

The entry cognates **fluō** with Ancient Greek *phléō* ("to abound") and *phlúō* ("to boil over"), but explicitly notes it is "unrelated to English *flow*, despite phonological and semantic similarity."
```


### [2026-09-05T06:26:11.979Z] TOOL RESULT

```
# Latin Etymology of "Folium"

The entry presents two competing etymological theories:

**Traditional Theory:**
"Traditionally derived from Proto-Indo-European *bʰolh₃yom ("leaf"), from *bʰleh₃- ("blossom, flower")," making it "an exact cognate of Ancient Greek φῠ́λλον (phŭ́llon)."

**Alternative Theory:**
An alternative approach "derives the word from Proto-Indo-European *dʰolh₁yom, from *dʰelh₁- ("be green")," with cognates including "Middle Irish duille, Welsh dail, Ancient Greek θάλλω (thállō, "to bloom"), Old Armenian դալար (dalar, "green, fresh"), [and] Albanian dal ("to exit, go out")."

The entry notes this alternative theory is "favored by Driessen and De Vaan" and cites Michiel de Vaan's *Etymological Dictionary of Latin and the other Italic Languages* as the reference source.
```


## [2026-09-05T06:26:19.496Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%86%CF%8D%CE%BB%CE%BB%CE%BF%CE%BD",
 "prompt": "Give the Ancient Greek entry φύλλον etymology in full (PIE reconstruction, cognates, Beekes)."
}
```


## [2026-09-05T06:26:19.823Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/flos",
 "prompt": "Give the Latin entry \"flōs\" etymology in full (PIE root, cognates in Germanic such as bloom/blossom)."
}
```


### [2026-09-05T06:26:24.053Z] TOOL RESULT

```
# Etymology of Ancient Greek φύλλον

The word φύλλον derives from Proto-Indo-European (PIE) *bʰol-yom, which itself comes from PIE *bʰleh₃- meaning "leaf, blossom, flower."

**Cognates include:**
- Latin *folium*
- Old Armenian *բողբոջ* (bołboǰ)
- English *blossom*

**Source:** According to Beekes' *Etymological Dictionary of Greek* (2010), the term traces through these related Indo-European forms, connecting the Ancient Greek word to a broader family of botanical vocabulary across ancient languages.
```


### [2026-09-05T06:26:26.453Z] TOOL RESULT

```
# Latin "flōs" Etymology

The Latin word **flōs** (flower) derives from Proto-Indo-European **\*bʰleh₃-s** ("flower, blossom"), itself from the root **\*bʰleh₃-** meaning "to bloom."

The etymological path flows through Proto-Italic **\*flōs** before reaching Latin. According to the entry, "cognates include Ancient Greek φύλλον (phúllon), Gothic 𐌱𐌻𐍉𐌼𐌰 (blōma) and Old English blōstm, blæd."

English descendants from these Germanic cognates include **blossom** and **blade**, demonstrating the shared Indo-European heritage across language families.
```


## [2026-09-05T06:26:33.439Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D9%84%D9%88%D8%A6%D9%88%D8%B1/",
 "prompt": "Show the فرهنگ معین (Mo'in) and other dictionary entries for فلوئور, including any origin tag such as [فر.] and the Latin-script form."
}
```


## [2026-09-05T06:26:34.213Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%84%D8%B1%D9%88%D9%81%DB%8C%D9%84/",
 "prompt": "Show the فرهنگ معین (Mo'in) and other dictionary entries for کلروفیل, including any origin tag such as [فر.] and the Latin-script form."
}
```


### [2026-09-05T06:26:38.379Z] TOOL RESULT

```
# فرهنگ معین Entry for فلوئور

**Origin tag:** [فر.] (French)

**Latin form:** flu~ur

**Definition:** A yellowish toxic gas that can be liquefied through specific chemical processes and solidified in liquid hydrogen. Its specific gravity is 1.31, and it boils at minus 187 degrees. "Inhalation of this substance is dangerous."

**Note:** The entry also indicates this is an "اِ" (scientific/technical term) borrowed from French, and mentions that fluorine compounds are used in toothpaste production.

---

The page additionally provides entries from Dehkhoda dictionary, Amid dictionary, and a general encyclopedia section with more detailed chemical and industrial applications of fluorine.
```


### [2026-09-05T06:26:40.061Z] TOOL RESULT

```
# کلروفیل (Chlorophyll)

## فرهنگ معین Entry

According to Mo'in Dictionary, chlorophyll is described as: *"مادة سبز رنگی در گیاهان که کار فتوسنتز را در یاخته انجام دهد"* (a green-colored substance in plants that performs photosynthesis in cells).

The entry notes the French origin [فر.] and provides the Persian equivalent سبزینه (sabzineh).

## Additional Dictionary Information

**Pronunciation:** /kolorofil/

**Persian Equivalent:** سبزینه (sabzineh)

**English Terms:** chlorophyl, chlorophyll

The Dehkhoda dictionary elaborates that this pigment exists in specialized cavities within the cytoplasm of plant cells and is responsible for the green coloration of plant organs. The entry notes that chlorophyll molecules contain magnesium (Mg) rather than iron, unlike hemoglobin.
```


## [2026-09-05T06:26:44.599Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D9%84%D9%88%D8%B1%D8%B3%D8%A7%D9%86%D8%AA/",
 "prompt": "Show the فرهنگ معین (Mo'in) and Dehkhoda/Amid entries for فلورسانت, including any origin tag such as [فر.] and the Latin-script form."
}
```


## [2026-09-05T06:26:46.112Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D9%86%D9%81%D9%84%D9%88%D8%A2%D9%86%D8%B2%D8%A7/",
 "prompt": "Show the فرهنگ معین (Mo'in) and Dehkhoda/Amid entries for آنفلوآنزا / آنفلوانزا, including any origin tag such as [فر.] or [ایت.] and the Latin-script form."
}
```


### [2026-09-05T06:26:48.863Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:26:49.118Z] TOOL RESULT

```
Based on the webpage content provided, I cannot fulfill your request. The page shows a dictionary entry for "فلورسانت" (fluorescent) from Abadis Dictionary, but it does not include the specific dictionary entries you're asking for.

The page only indicates that the word's English meaning is "fluorescent" and mentions that Abadis Dictionary contains various resources including "فرهنگ معین" and "لغتنامه دهخدا" (Dehkhoda dictionary). However, the actual entries from those specific dictionaries for this term are not displayed on this particular webpage.

To find those entries, you would need to access the full dictionary sections directly through Abadis.
```


## [2026-09-05T06:26:52.392Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D9%86%D9%81%D9%84%D9%88%D8%A7%D9%86%D8%B2%D8%A7/",
 "prompt": "Show the فرهنگ معین (Mo'in) and Dehkhoda/Amid entries for آنفلوانزا, including any origin tag such as [فر.] and the Latin-script form."
}
```


## [2026-09-05T06:26:53.352Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%86%D9%81%D9%84%D9%88%D8%A7%D9%86%D8%B2%D8%A7",
 "prompt": "Persian entry آنفلوانزا: etymology (borrowed from which language?), pronunciation, meaning."
}
```


### [2026-09-05T06:26:55.458Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:26:55.465Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T06:26:58.951Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A2%D9%86%D9%81%D9%84%D9%88%D8%A7%D9%86%D8%B2%D8%A7",
 "prompt": "Mo'in dictionary entry for آنفلوانزا: origin tag and definition."
}
```


## [2026-09-05T06:26:59.594Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%86%D9%81%D9%84%D9%88%D8%A2%D9%86%D8%B2%D8%A7",
 "prompt": "Persian entry آنفلوآنزا: etymology (borrowed from which language?), meaning."
}
```


### [2026-09-05T06:27:00.844Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:27:03.188Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T06:27:11.121Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== KLN blister =====\"; grep -n -m3 -A6 \"^blister\\|blister, n\" KLN_1966.txt | head -40\necho \"===== SKT blister =====\"; grep -n -m3 -A5 \"BLISTER\\|blister,\" SKT.txt | head -30",
 "description": "Grep Klein and Skeat for blister"
}
```


### [2026-09-05T06:27:11.179Z] TOOL RESULT

```
===== KLN blister =====
5175:blister,  n.  —  ME.  blister,  blester,  fr.  OF.  blestre, fr.  ON.  bldstr,  ‘a  swelling’,  fr.  bldsa,  ‘to  blow’. See  blast  and  cp.  bluster.  ,
5176-Derivatives:  blister,  intr.  and  tr.  v.,  blister-y, adj.
5177-blite,  n.,  any  of  various  herbs  of  the  goosefoot family.  —  L.  blitum ,  fr.  Gk.  (HXlrov,  ‘a  vege¬ table  used  as  a  salad ;  orach’ ;  of  uncertain  ety¬ mology.  According  to  some  philologists  [IXl-rov stands  for  *p.X-brov  and  prop,  means  ‘the  soft- leaved  plant’ ,  fr.  I.-E.  base  *mel-dh-,  whence  also OE.  melde,  OS.  maldia,  Swed.  mail,  Du.  melde, OHG.  melta.  molta,  multa,  MHG.,  G.  melde, ‘orach’.  Base  *mel-dh-  is  an  enlargement  of base  *mel-,  ‘to  rub,  grind’.  See  meal,  ‘edible grain’,  and  cp.  Blitum.
5178-blithe,  adj.,  joyous;  cheerful.  —  ME.,  fr.  OE. blide,  ‘joyful,  kind,  gentle’,  rel.  to  OS.  blidi, ‘bright,  happy’,  ON.  blidr,  ‘mild,  gentle’,  Du. hlij(de),  ‘glad’,  OHG.  blidi,  'gay,  friend'  ’,  Goth. bleips,  ‘kind,  friendly,  merciful’.  Cp.  liss.
5179-180
5180-181
5181-Derivatives :  blithe-ly,  &d\.,blithe-ness,  n.,  blithe¬ some,  adj.,  blithe-some-ness,  n.
===== SKT blister =====
14021:Pimple.  (L)    A  nasAlised  (or pi^l    (Cockayne).       [The    alli ptHfei  is  Lye's  misfirtnt  for  win^ not  an  E    word,   but  iKirTowetl. papula,  a  pimple.    Cf.  (jk. blister,  Lilhuaii.  pampti,    to  si sense  'swelling.'     Note  also  Skt. mole  or  freckle;   F.  p9mptit€,  *a or  pimple  on  the  nose  or  chin,* perhaps  W. pwmp,  a  bump.     \*
14022-Pin;  see  Pen  (2).
14023-Pinch.  (F.-C.'O     ¥.pim^. \xd  form  of  O.  Ital.  pii to  nip ;  cf.  Ital.  pin**,  a  stln^  ga otig.  sense  seems  lo  ha^c  b»ts prick  with  a  tharp-pouMad
14024-UU
14025-PINCHBECK-
14026-fitt  a  point,  seen  in  W,  /»»(/, >u(.  Hence  also  t>ti.  pititn^ rckham).  See  Petty.  Der. \Pim'4r$  \  cf,  F.  pinfest  '  t  pair •'  Cot.
```


## [2026-09-05T06:27:24.345Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -rn \"bluyster\\|blyster\" KLN_1966.txt KLN_1971.txt SKT.txt FSD_vol1.txt WEB_vol1.txt AHD_watkins1985.txt DOZ.txt 2>/dev/null | head -10",
 "description": "Search local books for bluyster"
}
```


### [2026-09-05T06:27:24.416Z] TOOL RESULT

```
WEB_vol1.txt:20602:les. blink’-eyed (id), a. habitually blinking or winking. =a blink/ing, a. winking; twinkling. DES n, the act of twinkling or winking; as, the blinking of an eye. bliñk’ing chick’weed, a marsh herb of the order Portulacacez: called also blinks. blinks, n. same as blinking chickweed. blirt, n. 1. a burst of tears. Bees) 2. in nautical usage, a gust of wind and Tain. bliss, n. [AS. blis, blisse, from blids, bliths, joy, from blithe, joyful. 1. extreme joy; blessedness; felicity; heav- enly joy. 2. any cause of bliss. Syn.—blessedness, joy, ecstasy, rapture. bliss’ful, a. full of joy and felicity; causing or characterized by great heppuies bliss/fyl-ly, adv. in a bli manner. bliss/ful-ness, n. exalted happiness; felicity; fullness of joy. _ bliss’less, a. destitute of bliss. blis’sém, v.i. [Ice. blzsma, in heat, as a goat.) to be lustful; to be in heat; said of a ewe. blis’sém, a. in heat: said of a ewe. T w blis’tēr, n. [ME. blister; D. bluyster; OFr. bles- tre, a b A swelling.] aan 1. a little swelling of the skin, filled with eatery matter and caused by
FSD_vol1.txt:44302:5.  A   fungous  plant-disease  characterized  by  excrescen- ces on  the  leaves.  6.  [Colloq.]  A   troublesome  person; nuisance.  7.  [Local,  U.  S.]  A   young  oyster.  [ME. blister;  cp.  OD.  bluyster,  blister.  Allied  to  blast.]  —   blls'- ter »bee"tle  or  *fly",  n.  A   beetle,  as  an  oil-beetle,  yielding a   substance  with  blistering  properties;  especially,  the  Span- ish fly —   b. -copper,  n.  Metal.  The  merchantable  prod- uct of  the  calcination  of  the  white  metal,  or  the  pimple- metal,  in  the  English  process  of  copper-smelting.— b.» flower,  n.  The  bulbous  crowfoot  ( Ranunculus  bulbosus). blls'ter-weed"L— b.*mlte,  n.  Any  mite  causing  a   blis- ter-like excrescence  on  the  leaves;  as,  the  pear-leaf  blister - mite  —   b.spearl,  n.  An  excrescence  produced  Inside  a shell  by  the  oyster  in  endeavoring  to  exclude  parasites.— b.*plne,  n.  [Local,  U.  S.l  The  balsam-fir  (Abies):  so called  from  the  blister-like  swellings  in  the  bark  containing the  balsam.— b. -plant,  n.  Any  one  of  several  species  of buttercup  or  crowfoot  ( Ranunculus ) ;   especially,  the  tall  or meadow  buttercup  (R.  acrls)  and  the  cursed  crowfoot (R.  sccleratus ):  so  called  from  the  effect  of  their  acrid juice  on  the  skin.—  b. -plaster,  n.  A   plaster  for  producing a   blister.—  b. -steel,  n.  Steel  made  by  heating  bar  iron,  in contact  with  powdered  charcoal.  In  a   converting-furnace.— blls'ter-wort",  n .   The  cursed  crowfoot.
```


## [2026-09-05T06:27:25.060Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=blister",
 "prompt": "Give the American Heritage Dictionary etymology bracket for the noun \"blister\"."
}
```


### [2026-09-05T06:27:28.515Z] TOOL RESULT

```
# Etymology of "Blister"

According to The American Heritage Dictionary, the etymological bracket for the noun "blister" is:

"[Middle English, probably from Old French _blestre_, of Germanic origin.]"

This indicates the word traces back through Middle English to Old French origins, with Germanic roots.
```


## [2026-09-05T06:27:36.063Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"^bowl,\" \"^bull,\" \"^bold,\" \"^blossom,\" \"^blade,\" \"^bellows,\" \"^belly,\" \"^chlorophyll\" \"^fluor,\" \"^influenza\" \"^phyllo\"; do echo \"##### $w\"; grep -n -m1 -A3 \"$w\" KLN_1966.txt | head -12; done",
 "description": "Grep Klein for the Germanic and Greek derivatives"
}
```


### [2026-09-05T06:27:37.629Z] TOOL RESULT

```
##### ^bowl,
5475:bowl,  n.,  a  wooden  ball.  —  F.  boule,  fr.  L.  bulla, ‘bubble’.  See  bull,  ‘edict’,  and  cp.  bolero. Derivatives:  bowl,  tr.  v.,  to  roll  (bowls);  intr.  v., to  roll  rapidly,  bowler  (q.v.),  bowl-ing,  n. bowler,  n.,  one  who  bowls.  —  Formed  from  prec. word  with  agential  suff.  -er. bowler,  n.,  a  hard  round  hat.  —  Formed  with suff.  -er  fr.  bowl,  ‘hollow  vessel’, bowline,  n.,  a  rope  used  to  keep  the  sail  taut ( naut .)  —  ME.  bouline,  fr.  OF.  bouline,  which  is of  LG.  origin.  Cp.  MDu.  boech-line  (whence Du.  boeglijn),  ‘bowline’,  and  see  bow,  ‘the  fore part  of  a  ship’,  and  line, bowls,  n.  pi.,  name  of  a  game.  —  Pi.  of  bowl,  ‘a wooden  ball’.
5476-bowly,  bowry,  n.,  a  well  with  steps  leading  down to  the  water  (Anglo-Ind.)  —  Hind,  baoli,  baori. ‘a  well’.  Cp.  OI.  vavrah,  ‘hole,  well’, bowsprit,  n.,  the  spar  extending  from  the  bow  of a  ship.  —  ME.  bouspret,  prob.  fr.  MLG.  boch- spret,  fr.  bdeh,  ‘bow’  (which  is  rel.  to  ON.  bogr, ‘bow’),  and  spret,  ‘pole’  (which  is  rel,  to  OE. spreot,  ‘pole’).  Cp.  Du.  boegspriet,  Dan.  bug- spry  d,  Swed.  bogsprot,  G.  Bugspriet.  F.  beaupre is  a  Dutch  loan  word.  See  bow,  ‘the  fore  part  of a  ship’,  and  sprit.
5477-bowwow,  n.,  and  intr.  v.  —  Of  imitative  origin, bowyer,  n.,  maker,  or  seller  of  bows.  —  Formed fr.  bow,  ‘weapon’,  with  suff.  -yer. box,  n.,  the  tree.  —  ME.,  fr.  OE.  box,  fr.  L.  buxus (whence  also  It.  bosso,  F.  buis),  fr.  Gk.  tuj^oq, ‘box  tree’,  which  is  perhaps  a  loan  word  of Thraco-Phrygian  origin.  Cp.  next  word,  bushing, Buxus,  and  pyx.  Cp.  also  the  second  element  in arquebus,  blunderbuss.  For  the  change  of  Greek 7c  to  b  in  Latin — which  is  prob.  due  to  Etruscan influence — cp.  burro,  carbasus  and  sbirro. box,  n.,  case,  chest.  —  ME.,  fr.  OE.  box,  orig.  ‘a receptacle  made  of  boxwood’,  fr.  L.  buxum, ‘anything  made  of  boxwood’,  fr.  buxus,  ‘box tree’ ;  see  prec.  word.  Cp.  MDu.  bosse,  busse  and OHG.  buhsa  (whence  MHG.  biihse,  G.  Biichse), which  derive  fr.  VL.  *buxem,  contraction  of *buxidem,  acc.  of  buxis,  which  corresponds  to Classical  L.  pyxis,  ‘box  of  boxwood’,  fr.  Gk. Tvu^lc,  of  s.m.,  fr.  rrj'o?,  ‘box  tree’.  Cp.  also OF.  boiste  (whence  F.  boile),  which  comes  fr. VL.  buxida,  acc.  of  buxis.  Cp.  also  Boxing  day and  bush,  ‘metal  lining’.
5478-box,  a  blow.  —  ME.,  of  uncertain,  possibly  imi¬ tative,  origin.
##### ^bull,
5831:bull,  n.,  the  male  of  a  bovine  animal.  —  ME.  bule, bole,  fr.  OE.  bula,  ‘bull’,  rel.  to  ON.  bolt,  MDu. bul(le),  Du.  bul,  G.  Bulle,  of  s.m.,  OE.  bulluc, ‘little  bull’,  bealluc,  ‘testicle’,  ON.  bollr,  ‘ball’, fr.  I.-E.  base  *bhel-,  ‘to  swell’,  whence  also  Gk. 9«XX'j?,  ‘penis’,  cpxXXaivx,  oocXXt; ,  ‘whale’,  L. follis,  ‘a  pair  of  bellows’.  Cp.  bullock.  Cp.  also baleen,  ball,  ‘a  round  body’,  bold,  bulk,  ‘size’, follicle,  phallus.  For  derivatives  of  base  *bhelgh-, an  enlargement  of  base  *bhel-,  see  belly,  bud¬ get,  bulge.
5832-Derivative:  bull,  intr.  and  tr.  v.,  bull-ish,  adj. bull,n.,  an  edict  of  the  pope.  —  ME.  bulle,  fr.  OF. bulle,  fr.  It.  bulla,  fr.  ML.  bulla,  ‘seal  affixed  to  a document,  document’,  fr.  L.  bulla,  ‘bubble,  boss, knob’,  fr.  I.-E.  *bu-l-,  whence  also  Lith.  bule, bulls,  ‘buttock’,  MDu.  puyl,  ‘bag’,  MLG.  pull, poll,  "pod,  husk’  (with  p  for  b).  I.-E.  *bu-l-  is an  -/-enlargement  of  base  *bu-,  ‘to  blow;  to swell’,  whence  L.  bucca,  “cheek".  Sec  buccal  and cp.  bill,  ‘document",  bullet,  bulletin.  Cp.  also poll,  "head".
##### ^bold,
5289:bold,  adj.  —  ME.,  fr.  OE.  bald,  beald,  rel.  to  OS., OHG.  bald,  ‘bold,  swift’,  OHG.  baldo,  ‘boldly’, MHG.  balde,  ‘boldly,  quickly’  (whence  G.  bald, ‘soon’),  ODu.  baldo,  ‘with  confidence’,  Goth. baljtei,  ‘boldness’,  balpaba,  ‘boldly’,  ON.  ballr, ‘frightful,  dangerous’,  fr.  I.-E.  base  *bliel-,  ‘to swell’.  It.  baldo,  OF.  and  Proveng.  haul,  ‘bold, daring,  fearless',  are  Teui.  loan  words.  See  ball, ‘a  round  object’,  and  belly  and  cp.  billow.  Cp. also  bawd,  the  first  element  in  Baldwin  and  the second  element  in  Leopold  and  in  Theobald. Cp.  also  bulk,  ‘size’.
5290-Derivatives:  bold-lv,  adv.,  bold-uess,  n.
5291-bole,  n.,  trunk  of  a  tree.  —  ME.  bole,  fr.  ON. bolr,  ‘trunk  of  a  tree’,  rel.  to  MLG.  bole,  bolle, G.  Bohlc,  ‘plank’,  MDu.  bolle,  ‘trunk  of  a  tree’. See  balk,  n.,  and  cp.  words  there  referred  to.
5292-bole,  n.,  red  earthy  clay.  —  L.  bolus,  ‘clay,  mor¬ sel',  fr.  Gk.  Sco/.oc,  ‘lump,  clod  of  earth’.  See bolus.
##### ^blossom,
##### ^blade,
5109:blade,  n.  —  ME.  blad,  blade,  fr.  OE.  bleed,  ‘leaf; blade  (of  an  ear)’,  rel.  to  ON.  blad,  OS.,  Dan., Swed.,  Du.  blqd,  OHG.,  MHG.  blat,  G.  Blatt, OFris.  bled,  ‘leaf’ ;  prop.  pp.  of  OE.  bldwan ,  etc., ‘to  bloom,  flower’,  fr.  I.-E.  base  *bhld-,  *bhle-, *bhla-,  ‘to  sprout,  bloom;  leaf’,  whence  prob. also  Toch.  pdlt,  ‘leaf’.  See  blow,  ‘to  bloom’,  and cp.  words  there  referred  to.
5110-Derivatives:  blade,  tr.  and  intr.  v.,  blad-ed,  adj., blade-let,  n.,  blad-er,  n.,  blad-ing,  n.,  b!ad-y,  adj. blae,  adj.,  dark-blue,  livid  (obsol.)  —  ME.  bio, bla,  fr.  ON.  blar,  which  is  rel.  to  OE.  blow, bliew,  ‘blue’.  See  blue.
5111-blaeberry,  n.,  bilberry.  —  Compounded  of  blae and  berry.
5112-blah,  interj.  and  n.  (U.S.  Slang)  —  Of  imit.  origin. Main,  n.,  a  pustule.  —  ME.  bleine,  fr.  OE.  blegen, rel.  to  Dan.  blegn,  Du.  blein,  fr.  I.-E.  base *bhlei-,  ‘to  swell’,  an  enlargement  of  base *bhel-.  For  other  enlargements  of  base  *bhel- see  belly,  bloat,  bulge,  phlebo-.
##### ^bellows,
##### ^belly,
4722:belly,  n.  —  ME.  ball,  bely,  fr.  OE.  baelg,  belig,  belg, ‘bag,  belly,  bellows',  related  to  ON.  belgr,  ‘bag, bellows’,  Swed.  balg,  ‘belly,  bellows’,  Du.  balg, ‘belly’,  OHG.  balg,  MHG.  bale,  G.  Balg,  ‘bel¬ lows’,  Goth,  balgs,  ‘wineskin’,  OE.  -belg  (in beanbelg,  ‘bean  pod’),  OHG.  belgan,  ‘to  swell’, ON.  bylgja,  ‘billow’,  bolstr  [for  *bul(h)stra], ‘bolster’,  lit.  ‘something  swelled’,  fr.  Teut.  base *belg-,  which  corresponds  to  I.-E.  base  * bhelgh -, ‘to  swell’,  whence  OPruss.  balsinis  (for  *bhol- ghi-nos),  ‘cushion’,  Lett,  pabalsts,  ‘pillow’, Serbo-Croat,  bldzina  (for  *bolzina),  ‘pillow’, Olr.  bolgaim,  ‘I  swell’,  bolg,  ‘bag’,  W.  bol,  bola, boly,  ‘belly’,  Bret,  bolc’h,  ‘flax  pod’.  (L.  bulga.
4723-‘leather  knapsack’,  is  a  Gaulish  loan  word.)  Cp. bellows,  bilge,  billow,  bolster,  budge,  ‘fur’,  bud¬ get,  bulge.  Base  *bhelgh-,  is  an  enlargement  of base  *bhel-,  ‘to  swell’.  See  bull,  ‘male  of  the  ox', and  cp.  words  there  referred  to.
4724-Derivatives :  belly,  intr.  v.,  belly-er,  n.,  belly-fut, adj.
4725-belong,  intr.  v.  —  ME.  belongen,  fr.  longen,  ‘to concern’,  fr.  lang,  long,  fr.  OE.  gelang,  ‘at  hand, attainable,  dependent  on’,  which  is  rel.  to  MDu. belanghen,  Du.  belangen,  G.  belangen,  ‘to  con¬ cern;  to  belong  to’  (whence  Du.  belong,  resp. G.  Belong,  ‘concern,  interest,  importance’),  and to  OE.  lang,  etc.,  ‘long’.  The  orig.  meaning  of the  above  verbs  prob.  was  ‘to  be  alongside  of. See  long,  adj.,  and  cp.  along.
##### ^chlorophyll
7481:chlorophyll,  chlorophyl,  n.,  the  green  coloring matter  of  plants.  —  F.  chlorophylle,  coined  by the  French  chemists  Pierre-Joseph  Pelletier (1788-1842)  and  Joseph-Bienaime  Cavemen (1795-1877)  fr.  chloro-  and  Gk.  tpuXXov,  ‘leaf. See  phyllo-  and  cp.  the  second  element  in  xan- thophyll.
7482-chloroprene,  n.,  a  colorless  liquid  used  to  manu¬ facture  neoprene  (chem.)  —  Coined  fr.  chloro- and  (iso)prene.
7483-chlorosis,  n.,  a  kind  of  anemia,  ‘green  sickness’ (med.)  —  Medical  L.,  formed  with  suff.  -osis fr.  Gk.  yXo>p6i;,  ‘greenish-yellow,  pale  green, green,  fresh’.  See  chlorine.
7484-choana,  n.,  a  funnel-shaped  opening  (anal.)  — Medical  L.,fr.Gk.  yoavr, ‘funnel,  funnel-shaped hollow  in  the  brain’,  a  derivative  of  yofj,  ‘a  pour¬ ing  out’,  from  the  stem  of  ysiv,  ’to  pour’,  which is  cogn.  with  L.  fundere,  ‘to  pour’.  See  found, ‘to  cast’,  and  cp.  chyle.  Cp.  also  the  first  element in  chonolith.
##### ^fluor,
15025:fluor,  n.,  a  mineral  containing  fluorine,  fluorite. —  ModL.,  fr.  L.  fluor,  ‘a  flowing’,  fr.  fluere,  ‘to flow’.  See  fluent  and  -or  and  cp.  fluorine, fluoresce,  intr.  v.  —  Back  formation  fr.  fluor¬ escence.
15026-fluorescence,  n.  (physics).  —  Formed  with  suff. -escence  (on  analogy  of  opalescence,  phosphores¬ cence)  fr.  fluor(spar).  The  word  fluorescence was  coined  by  the  English  mathematician  and physicist,  Sir  George  Gabriel  Stokes  (1 8 19- 1903) in  1852  in  allusion  to  the  circumstance  that  he noticed  this  phenomenon  first  in  fluorspar, fluorescent,  adj.  —  See  prec.  word  and  -ent. fluoric,  adj.,  pertaining  to  fluorine  (chem.)  — Formed  with  suff.  -ic  fr.  fluor. fluorine,  n.,  name  of  a  nonmetallic  element  be¬ longing  to  the  halogen  family  (chem.)  —  Coined by  the  English  chemist  Sir  Humphry  Davy (1778-1829)  fr.  fluor  with  chem.  suff.  -ine  (on analogy  of  brom-ine,  chlor-ine,  iod-ine).  The element  was  so  called  by  him  because  it  was found  first  in  fluorspar.
15027-fluorite,  n.,  fluorspar  (mineral.)  —  Formed  fr. fluor  with  subst.  suff.  -ite. fluoro-,  combining  form  denoting  either  1)  fluor¬ ine  or  2)  fluorescence.  —  See  fluor. fluoroscope,  n.,  an  instrument  for  observing fluorescence.  —  A  hybrid  coined  fr.  L.  fluor  and
15028-Gk.  -tjxAmov,  fr.  mcoTretv,  ‘to  look  at,  exam¬ ine’.  See  fluor  and  -scope.
##### ^influenza
##### ^phyllo
28678:phyllo-,  before  a  vowel  phyll-,  combining  form meaning  ‘leaf’.  —  Gk.  9UXX0-,  9UXX-,  fr.  96X- Xov,  ‘leaf’,  which  is  cogn.  with  L  .folium,  ‘leaf’. See  folio-  and  cp.  Phyllis,  aphyllous,  chervil, gillyflower.
28679-Phyllodoce,  n.,  a  genus  of  plants  of  the  heath family  (bot.)  —  ModL.,  fr.  L.  Phyllodoce,  name of  a  sea  nymph.
28680--phylious,  combining  form  meaning  ‘having  a certain  number  or  a  certain  shape  of  leaves’,  as in  diphyllous,  eleutherophyllous.  —  Gk.  -917X- X09,  fr.  96XX0V,  ‘leaf’.  See  phyllo-.  For  E.  -ous, as  corresponding  to  Gk.  -09,  see  -ous. Phylloxera,  n.,  a  genus  of  plant  lice  (zool.)  — ModL.,  compounded  of  phyllo-  and  Gk.  £75969, ‘dry’.  See  xero-  and  cp.  Xerophyllum. phylo-,  before  a  vowel  phyl-,  combining  form meaning  ‘tribe’.  —  Gk.  96X0-,  96X-,  fr.  96X0V, ‘tribe’,  which  is  rel.  to  96X7),  of  s.m.  See  phyle. phylogeny,  also  phylogenesis,  n.,  evolution  of  a race  (biol.)  —  G.  Phylogenie,  coined  by  the German  biologist  Ernst  Heinrich  Haeckel (1834-1919).  See  phylo-  and  -geny,  resp.  genesis. Derivatives :  phylogen-etic,  phylogen-etic-al, adjs.,  phylogen-etic-al-ly,  adv.,  phylogen-ic,  adj. phylum,  n.,  one  of  the  divisions  of  the  plant  or animal  kingdom,  (biol.)  —  ModL.,  coined  by the  French  naturalist,  Baron  Georges  Leopold Chretien  Frederic  Dagobert  Cuvier  (1769-1832) fr.  Gk.  96X0V,  ‘tribe,  race’.  See  phyle. phyma,  n.,  a  swelling;  skin  tumor  (med.)  —  Gk. 90ua,  gen.  o6pLaxo9,  ‘that  which  grows,  a growth,  swelling,  tumor’,  fr.  9651V,  ‘to  bring forth,  produce,  make  to  grow’.  See  physio-  and -ma.
28681-phys-,  form  of  physo-  before  a  vowel.
```


## [2026-09-05T06:27:49.540Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -m2 -o \"bowl,  n.,  a  hollow.\\{0,600\\}\" KLN_1966.txt\necho \"---- blossom ----\"; grep -n -m2 -o \"blossom,  n.\\{0,600\\}\" KLN_1966.txt\necho \"---- bellows ----\"; grep -n -m2 -o \"bellows,  n.\\{0,500\\}\" KLN_1966.txt\necho \"---- influenza ----\"; grep -n -m2 -o \"influenza,  n.\\{0,600\\}\" KLN_1966.txt",
 "description": "Grep Klein for bowl vessel, blossom, bellows, influenza"
}
```


### [2026-09-05T06:27:51.323Z] TOOL RESULT

```
5471:bowl,  n.,  a  hollow  vessel.  —  ME.  bolle,  fr.  OE. bolla,  rel.  to  ON.  bolle,  OHG.  bolla,  MHG,  bolle.
---- blossom ----
5202:blossom,  n.  —  ME.  blosme,  blossem,  fr.  OE. blostm,  blostma,  blosrna,  rel.  to  MLG.  blosem, Du.  bloesem,  MHG.  bluost,  G.  Blust,  fr.  I.-E. *bhlos-,  enlarged  form  of  base  *bhlo-,  ‘to  sprout, bloom’.  See  bloom,  ‘flower’.
---- bellows ----
4721:bellows,  n.  pi.  —  ME.  bely;  prop,  a  variant  of belly  (q.v.)
---- influenza ----
19350:influenza,  n.,  an  acute  contagious  disease.  —  It., lit.  ‘influence’  (see  influence).  The  disease  was so  called  because  it  was  originally  attributed  to the  'influence'  of  the  stars.
```


## [2026-09-05T06:28:02.404Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"\\[pdf page\" WLD_Bd2_pages.txt | head -5\necho ---\ngrep -n \"bhel-\\|bhelgh\\|bhleu\\|bhlei\" WLD_Bd2_pages.txt | head -30",
 "description": "Locate Walde-Pokorny Bd2 bhel entries"
}
```


### [2026-09-05T06:28:02.473Z] TOOL RESULT

```
---
7312:wie neben bol {pel) anch gleichbed. bhel- steht. Der labiale Anlaut dieser
7823:     Ygl. mit z. T. ahnlicher Bed. bhled „aufsprudeln, 8chwatzen“, bhel- „lauten,
11193:bhel- „glanzen“.
11444:1.    bhel- glanzen“ vermutlich zu bJid- ds. im selben Verhaltnis stehend,
11512:176                               bhel- und bhle-, blilo
11530:bhles „glanzen", bhlei, -f/-, -q- ,glanzen“, bhloidos „licht, blaB*„ bhleu- „brennen".
11564:3.    bhel- und bhle-, bhlo-                  blield)   ,,Blatt,   Bliite,    bliihen;   iippig
11566:       aus bhel- „schwellen" im Sinne von „pfianzlicher tJppigkeit" und
11569:       Petersson KZ. 47, 290 darin bhel- ,,glanzen" (aksl. beh „wei6" usw.).
11576:                                                   bhel   — bhel-                                        177
11606:ahd. bJdf ,,B^hte“ (vgl. auch ags. blad^ ahd. bldt „Weben, Hauch^* u. bhel-
11619:konnte wegen des weiBen AYinterpelzes Beziehung zu bhel- „glanzen“ er-
11630:4,     bhel- „aufblasen, aufschwellen, sti’otzen^, ahnlich wie phel „schwellen‘‘,
11641:178                                               bhel-
11658:falter“,   s.       Immisch Gl. 6, 194ff.), vielleicht dipeXfjg und Zubehor (s. u. "^bhel-
11716:                                                  bhel-                                                 179
11743:   Vgl. fiber unser bhel- und dessen AYeiterbildungen Curtius 300 ff.,
11788:180                                               bhel-
11798:     bhelgh „schwellen“, ^bhlcg'^ ds.
11799:     bhlei-^ bhleu-        ds.
11801:5,     bhel- in Bezeichnungen des Bilsenkrautes, wohl eig. ,weifilich“ (von         5
11804:         den graugriinen Blattern der Pflanze) und zu bhel- ,,glanzen‘‘ (slav.
11824:6.  bhel- etwa „Einde''.
11834:Trautmann, s. u. bhel- „glanzen“. DaB mit cptXkog auch (f sXXEvgy -ecog Hes.,
11844:(freilich scheint auch gr. <p?.oi6g, (pXovg „Rinde^‘ zu bhleu- „schwellen“ zu
11854:                                                              bhel-                                                          181
11857:7.    bhel- meist mit                         (-A;-) Suffix    „Bolile,       Balken".         bhel{d)g-^           bheh-n-Q')
11912:   Zur Yermittlung der obigen Bedeutungen mit den u. bhelgh- „schwellen'‘
11922:182                                        bhel-    — bhelgh
11927:„Balken‘‘ eine Wz. bhel- der Bed. „8palten“ zugrunde.
```


## [2026-09-05T06:28:06.621Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '11564,11580p' WLD_Bd2_pages.txt\necho \"===== bhelgh =====\"; sed -n '11928,11960p' WLD_Bd2_pages.txt",
 "description": "Print Walde-Pokorny 3.bhel- (leaf/bloom) and bhelgh-"
}
```


### [2026-09-05T06:28:06.679Z] TOOL RESULT

```
3.    bhel- und bhle-, bhlo-                  blield)   ,,Blatt,   Bliite,    bliihen;   iippig
       spriefien",   wohl   in alter Zeit bereits ziemlich verselbstandigte              Entw.
       aus bhel- „schwellen" im Sinne von „pfianzlicher tJppigkeit" und
       ..Schwellung   =
                     Knospe".   Nichteinleuchtendes sucht Meillet Et. 178,
       Petersson KZ. 47, 290 darin bhel- ,,glanzen" (aksl. beh „wei6" usw.).
  Gr. qjvXXov „Blatt" {f^bholiom)^ lat. folkmi ds. (*bholiom)^ gal. bile ,,Blatt-
chen, Bliite" (f^bhellom), Curtius 305, Fick II^ 174, Persson Beitr. 144 Anm.,
                                                                                                     2



                                                   bhel   — bhel-                                        177


29f. (auch gegen Johanssons PBrB. 15, 225 f. Wzansatz '^bh[e]uel-^ so daS
folium aus *bhuoliom, q)vklov aus %huliom; fur (pvXXov ist librigens viel-
===== bhelgh =====


8.   bhel- „lauten, schallen, reden, brullen, bellen“.
  Ai. bha^d-h „bellend“ i^bhel-s-), bhaSate „redet, spricht, plaudert'^; bhan-
date (Dhatup.) „spricht, hohnt, tadelt“ (^bhd-n-db', Johansson IP. 8, 184f.),
bhdnati „redet, spricht“ (^bhel-no, Johansson aaO.);
  aisl. belja „brfillen“, mndl. belen „bellen“; aisl. bylja^ bulda „drohen“,

bylr „Wind8tofi“ (nicht besser nach Persson Beitr. 800 zu bhel- „aufblasen“),
ags. bylgan „brullen‘^ mhd. boln „schreien, brfillen^;
   mit germ, ll (aus idg. Is wie ai. bhas-1 oder In wie ai. bhan-T), ahd.
bellan „bellen“, ags. bellan „brfillen, bellen, grunzen''; ahd. bidlon „heulen
(vomWind), bellen, brfillen”, isl.-norw. bulla „babbeln, schwatzen''; aisl.
bjalla, ags. bdle, engl. bell, mnd. belle ,,Schelle, Glocke“, nhd. (eig. nd.)
Sellhammd „Leithammel (mit Schelle^9                       ^


     mit germ. Id (wohl aus einem     -Praes. und vielleicht mit lit. btldn
                                                    c?/2

zu vergleichen, wenn letz teres nicht wJe ai. bhandate idg. d entbalt) dan.
baldre, norw. mdartl. baldra, schwed. mdartl. ballra „larmen“, mnd. ndl.
baldercn    ds.,   dan. buldre, schwed. bullsa, mnd. ndl. bulderen, bolder en, mhd.
biddern, nhd. poltern-
     apr. built „sagen, sprechen^',           lit. bilstti,    hilan, bilti    „zu re den anfangen“,
bllu, blloti   „reden“,     bilojti,    -6ti ,,sagen,      reden“, byl-ail -6ti
                                                               ds., byld „Rede,

Aussprache, Unterhaltung", lett. bllsh^^ biUu, bilst (in Zs.) „reden, anreden^'^
bildd „anreden‘'; lett. bilut ,,weinen‘*; mit Formans -sc- (ygl. lit. garsas
und slov. ^golsz) lit. balsas ,,Stimme, Ton*\
  Vgl. Pick I^ 92, III* 206, Johansson IF. 8, 184 f., Lewy KZ. 40, 421,
Falk-Torp u. bjdde, bcelje, biddre, Trautmann Apr. 31 If., Bsl. Wb. 25.                                     —
```


## [2026-09-05T06:28:17.033Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"bhelgh „schwellen\\|bhelgh -\\|bhelgh$\\|bhleu- „aufblasen\\|bhleu „aufblasen\\|bhlei- „aufblasen\\|bhlei „aufblasen\" WLD_Bd2_pages.txt | head\necho ---\ngrep -n \"^bhelgh\\|^ *bhelgh\\|^ *bhleu\\|^ *bhlei\" WLD_Bd2_pages.txt | head -20",
 "description": "Find WLD bhelgh and bhleu headings"
}
```


### [2026-09-05T06:28:18.738Z] TOOL RESULT

```
11798:     bhelgh „schwellen“, ^bhlcg'^ ds.
11922:182                                        bhel-    — bhelgh
13762:2.    bhlei- „aufblasen, schwellen, strotzen, uberfliefien", Erw. von bhel- ds.
---
11798:     bhelgh „schwellen“, ^bhlcg'^ ds.
11799:     bhlei-^ bhleu-        ds.
11970:bhelgh- ..willkommen, gut: bewillkommnen'*?
11975:bhelgh ,,schwellen; Balg (aufgeblasene Tierhaut), Kissen, Bolster' (Erw.
13785:  bhleid (vermutlich r?-Praes.                  ^bhU-d-d).
13808:bhleiq „glanzen“, Erw. von               bhlei-     (: bit el-)          ds..   wie    bhleiy.
13871:bhleuo-8 von lichten Farben „blau, gelb, blond“ auch bhlonos oder *bhlanoslt);
13898:bhleu- „aufblaseii (schnauben, brullen), scbwellen, strotzen, uberwallen,
13911:                                                  bhleu-                                               213
13943:bhlei-s-),
13965:                      bhleug^ (^gl- die Wzform bhleg^: doch kann lat.
14224:bhlei- s. d.), blaivaus^ -ytis „6ich aufklaren, vom Himmel“.     Alb. (G. Meyer
```


## [2026-09-05T06:28:22.248Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '11975,11985p' WLD_Bd2_pages.txt\necho \"=== bhleu ===\"; sed -n '13898,13905p;13960,13975p' WLD_Bd2_pages.txt\necho \"=== bhlei 2 ===\"; sed -n '13762,13770p' WLD_Bd2_pages.txt",
 "description": "Print WLD bhelgh, bhleu, bhlei entries"
}
```


### [2026-09-05T06:28:22.328Z] TOOL RESULT

```
bhelgh ,,schwellen; Balg (aufgeblasene Tierhaut), Kissen, Bolster' (Erw.
    von bhel- „aufblasen usw.“, Persson Wzerw. 26 £, Beitr. 799 a 2).
     Ai. barhis- n. ,,Streii, Opferstreu**           = av. barezis- n.        ,,   Bolster, Kissen", np.
balis „Kissen" (arm. barjKissen" ist wegen r wohl iran. Lw. s. Hfibsch-
                                   ,,                                                      ;


mann Armgr. 1428, trotz Persson Beitr. 53); ai. tipa-bdrhana-m, vpa-bdrhanl
f. „Decke, Bolster";
                                              bhelg-, bh(e)lag (bh(e)leg“?)                                               183

=== bhleu ===
bhleu- „aufblaseii (schnauben, brullen), scbwellen, strotzen, uberwallen,
    flie6en“, Erw. von hhel- „(aufblasen) aufscbwellen"
                                                         fPersson Wzerw.
        16, 35, 131 f., 173.
     Gr.
       cpUoi „strotze, bin ubervoH", ^Xevg {*^Xr]vg, debnstufig), epbes.
0Xe(og {‘^Xrjfog) Beiname des Dionysos als Vegetationsgottes; vermutlicb
von der Uppigkeit des Wucbses (s. u.) aucb tpXscog, jon. (pXovg „Scbilf-
„schwach“ (s. d.), aisl. blotna „weich werden‘‘ (Persson Wzerw. aaO., Beitr.
58, 879; vgl. die Wzformen bhle-d- und hhlei-d),


  ^-Erw. hhleug (Curtius 300 f., Vf. LEWb.^ u, fltio) oder (nach Persson
                      bhleug^ (^gl- die Wzform bhleg^: doch kann lat.
Beitr. 54 ff., 879, 931)
fluo-    trotz             dem Typus f~i{g)vo:f)xi eingedrungenes sekun-
                  Persson nach
dares n enthalten, s. Vf. LEWb.^ u. fluo))
214                            bhleu-(k)-,   (-S-)   — bhleg-, bbelg-
  gr. oivo-fpkv^ „\Yeintrunken“; (pkvico^
                                       Aor, (pkv^ai „aufwallen, uberwallen“;
(pkvxTig, (pXvxzaiva„Blase“; dafi hingegen noju-cpoXvi „Brandblase, Schild-
buckel“ eine Red.-Bildung von der noeh zweisilb. Basis bholeug- sei, ist
wegen nofitpo? ds. und anderer unter ba^mb besprochener gr. "Worte unwahr-
=== bhlei 2 ===
2.    bhlei- „aufblasen, schwellen, strotzen, uberfliefien", Erw. von bhel- ds.
       (Persson Wzerw. 35 f., 1 10, 173).
  Gr. (phpekia „Blutgeschwulste an den FiiBen der Pferde" (vgL lat. flemina
unter bliel-, bh[e]la\ norw. mdartl. b^eime, aschwed. blema „HautbIaschen" (vgl.
norw. blcEtiia ds. u. bhel-j 6/^[6*]/r) ; dan. blegfi(e) j,Blaschen" (*b^                        ags.
blegen f., engl. blain, mnd. bleine, alter dan. bleni/)
                                                  aschwed. blena „Blaschen"
{majinon); vgl Pick 111^ 286, Falk-Torp n.blegn, Persson Beitr. 800).
  DaB gr. g)hd j,Turpfeiler, Furplosten" eig. „(*geschwollener=) dicker
```


## [2026-09-05T06:28:29.558Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC bholiom / bhleu ===\"; grep -n -o \"bholiom.\\{0,300\\}\\|bhleu[oō].\\{0,300\\}\\|bhelghos.\\{0,250\\}\" IEC.txt | head -12\necho; echo \"=== SYN leaf/flower ===\"; grep -n -o \"folium.\\{0,200\\}\" SYN.txt | head -6",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-05T06:28:31.250Z] TOOL RESULT

```
=== IEC bholiom / bhleu ===
1432:bhleuo); Cz. (+ü) blýskat, v. ‘lighten, flash?^; Slovak blyskat (sa), blysknüt, id. See next
1438:bhleuo

=== SYN leaf/flower ===
13244:folium Dan. _ blad (I¢v) ChSl.  listit foglia Sw. blad (laf) SCr. list feuille OE léaf (bled) Boh. list
13254:folium, cf. Gall. reuze-Sovda ‘revraguddov’ : Grk. 64\\w ‘bloom, flourish, abound’, #adAds ‘sprout, young twig’, Alb. dal ‘sprout, go forth’, Arm. dalar ‘green, fresh’, etc. Walde-P. 1.825. Pedersen 1.375. 
13254:folium could also be put with this group, instead of as above, 1. Cf. Ernout-M. S.v.
```


## [2026-09-05T06:28:31.716Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW fluo ===\"; grep -n -o \"fluo, .\\{0,700\\}\\|flu5, .\\{0,600\\}\" LEW_1910.txt | head -4\necho \"=== LEW folium ===\"; grep -n -o \"folium.\\{0,500\\}\" LEW_1910.txt | head -4\necho \"=== LAT fluo ===\"; grep -n -o \"fluo.\\{0,400\\}\" LAT.txt | head -4",
 "description": "Grep Walde LEW and Ernout-Meillet for fluo, folium"
}
```


### [2026-09-05T06:28:35.443Z] TOOL RESULT

```
=== LEW fluo ===
=== LEW folium ===
=== LAT fluo ===
13107:fluo dans les 1 . romanes, ou il est
22322:fluo P.F.81,33» offiuebant, Gloss. Latin III
22355:fluo indiquerait nne labio-
22716:fluo: v./ Igo.
```


## [2026-09-05T06:28:39.384Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13240,13260p' SYN.txt",
 "description": "Print Buck's leaf section"
}
```


### [2026-09-05T06:28:39.424Z] TOOL RESULT

```
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
NHG _ Dlait (laub)
ME, NE blade never in this sense, and only late ME in modern sense of ‘blade’ of grass, ete., cf. NED s.v.), OHG, MHG blat, NHG blatt, Du. blad.
2. Rum. frunzd, fr. MLat. frondia formed after the analogy of folia fr. Lat. frons, frondis ‘leafy branch, foliage’, itself of dub. orig. Puscariu 659. REW 3530.
3. Ir. duille, duillen, NIv. duilleog, W. deilen (and dalen, coll. dail), Br. de- lienn (coll. deil), OCorn. delen gl. folium, cf. Gall. reuze-Sovda ‘revraguddov’ : Grk. 64\\w ‘bloom, flourish, abound’, #adAds ‘sprout, young twig’, Alb. dal ‘sprout, go forth’, Arm. dalar ‘green, fresh’, etc. Walde-P. 1.825. Pedersen 1.375. Lat. folium could also be put with this group, instead of as above, 1. Cf. Ernout-M. S.v.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
;
Digitized by Arya Samaj Foundation Chennai and eGangotri
526 SELECTED INDO-EUROPEAN SYNONYMS
4. Goth. laufs, pl. laubds, also lauf coll. ‘dbdda’, as likewise ON lauf, Dan. Igv, Sw. laf ‘foliage’; OE léaf sg. and pl., ME lefe, leef, etc., NIE leaf, OHG loub, MHG loup either ‘leaf’ (pl. OHG loubir ‘leaves’), or coll. ‘foliage’ as NHG laub, Du. loof, prob. : Lith. lupt:, Lett. lupt ‘flay, peel’, Russ. lupit’ ‘peel, bark’, etc. with the same semantic relation as Lith. lapas : Grk. \éxw (below, 5). Walde-P. 2,418. Feist 323 f. Falk-Torp 683.
ON blad, etc., above, 1.
```


## [2026-09-05T06:28:40.724Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -B3 -A10 \"^fluo\\b\\|fluo, -ere\\|fluo :\" LAT.txt | sed -n '1,60p'",
 "description": "Print Ernout-Meillet fluo entry"
}
```


### [2026-09-05T06:28:40.774Z] TOOL RESULT

```
22713-fitilla, -ae f.: sorte de gSteau usite dans les sacrifices. Sans
22714-doute terne rituel d'origine dialectale, pour *fictilla, cf.Brnout,
22715-6 ldm. Dial. s .u.
22716:fluo: v./ Igo.
22717-flaccus, -a, -un: qui penche, pendant, nou flasque. Surnon fre-
22718-quent; par exenple du pobte Horaee. Se dit entre autres des oreilles,
22719-cf. auriflaccus CGL III 330,46. Attest 4 depuis Varron. Hare, populaire;
22720-M.L.3343, it. fiacco.
22721-D^riv^s: flacceo, -es; flaccesco,-is, con-flaccesco; flaccidus, M.L.
22722-3343 {v.fr.flaistre, d'oi fldtrir); flaccor n.(tardif); peut-etre
22723-flacculum (.-Ius?), not de sens obscur, cf.Thes. s.u.; flaccil la (Mar-
22724-tial, ete. ).
22725-flaccus a la g^nin^e caract^ristique des adjectifs farquant une
22726-diffornit^ physique: cf. broccus, lippus, etc. Si *I- peut aboutir
--
23011-pr^sentant la aene initiale: v.h.a.blden, v.angi. 6 lawan "souffler",
23012-et aussi v.h.a. blasan (aene sens), avec -e- en face de la forae latine
23013-en -o-. Les autres aots a fl- initial sont aussi k rapprocher; v.fleo,
23014:fluo , et surtout le groupe de follis.
23015-floccSs (/ loces)... - ...prisca uoce significare uini faecem e
23016-uinaceis expressam, sicut fraces oleis, Geli.11,7,6. Atteste depuis
23017-Caecilius; rare, technique. f loces seable confi-.a 4 par le lucquois
23018-fiogia, M.L.3376• Coaae fraces et faeces, aot technique de la viti-
23019-culture, non i.-e.
23020-floccus, -I a.: flocon de laine; duvet. Le g^nitif s'eaploie dans
23021-la 1. faailibre avec les verbes d'estine: flocci facid, pendo dans
23022-le sens de "faire peu de cas de", coaae notre "pas un fetu" i- Cf.naucus.
23023-- Ancien, usuel. - Panroaan, M.L.3375, et passe en geraanique: v.h.a.
23024-floccho.
--
23070-gall. blawd "floraison" et got.bloma (masc.) "fleur", v.isl. 6 Io* "fleur"
23071-(neutre); v.h.a.bluot et v.angl . blaed "floraison"; v.sax.bloian "fleu¬
23072-rir". V. folium.
23073:fluo (graphie flou- dans conflouont, Sent.Minue.117 av. J.-C., sur
23074-la valeur de cette graphie, v.Niedermann, Milanges F.de Saussure,
23075-p.58 et s., et L.Havet, Man.de crit.verb.,§ 914),-is, -xl, -ctum puis
23076--xum, -ere; couler (= peoo); par extension "s'ecouler, couler unifor-
23077-miment, tomber mollement; se laisser aller sans retenue"; cf. fluens,
23078-fluxus. - Ancien, usuel. - Non roman (v. colare).
23079-Derives et composis: fluor,-oris m.: ecoulement, flux, diarrhie (cf.
23080-peu(i.a, peuCTLC); en particulier au pluriel "flux menstruel", sens con¬
23081-servi en roman, cf.fr.fleurs, M.L.3390, fluonia surnom de Junon:
23082--m Iunonem mulieres colebant quod eam sanguinis fluorem in conceptu
23083-retinere putabant, P.F.83,4; fluidus ( fluuidus Lucr. 3,464,466 d'aprfes
```


## [2026-09-05T06:28:54.251Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://www.etymonline.com/word/fluorine\" \"https://www.etymonline.com/word/influenza\" \"https://www.etymonline.com/word/blister\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 85, root Bhel/Bhelgh/Bhlei/Bhleu part 2: fluor/fluorescent, influenza (Italian route), blister (MDu bluyster?)\"; done 2>&1 | tail -20",
 "description": "Archive Etymonline pages"
}
```


### [2026-09-05T06:28:56.664Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6be5b3f2d19d0308.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8db9dd977f4829bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ade9502b9db1d70.txt
```


## [2026-09-05T06:29:02.727Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/fluo\" \"https://en.wiktionary.org/wiki/folium\" \"https://en.wiktionary.org/wiki/%CF%86%CF%8D%CE%BB%CE%BB%CE%BF%CE%BD\" \"https://en.wiktionary.org/wiki/flos\" \"https://abadis.ir/fatofa/%D9%81%D9%84%D9%88%D8%A6%D9%88%D8%B1/\" \"https://abadis.ir/fatofa/%DA%A9%D9%84%D8%B1%D9%88%D9%81%DB%8C%D9%84/\" \"https://www.ahdictionary.com/word/search.html?q=blister\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 85, root Bhel/Bhelgh/Bhlei/Bhleu part 2: Latin fluo/folium/flos, Greek phullon, Persian فلوئور/کلروفیل (Mo'in [فر.]), AHD blister\"; done 2>&1 | tail -20",
 "description": "Archive Wiktionary, abadis and AHD pages"
}
```


### [2026-09-05T06:29:09.338Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8d9f26b4b0f2f42b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/801c15c048eed445.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c1b5673b2f1832c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a7ac71daf0bd129.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/544fb094f8e9aafe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/59dba250fe389eb2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/51501af607ab2b95.txt
```


## [2026-09-05T06:29:13.767Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T06:29:13.804Z] TOOL RESULT

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


## [2026-09-05T06:29:35.764Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\ngrep -l \"transcription_suspect\" page-*.json | head; echo \"---\"; grep -o \"\\\"derivation\\\": \\\"[^\\\"]\\{0,200\\}\" page-80.json | head -6",
 "description": "Look at prior handling conventions"
}
```


### [2026-09-05T06:29:37.597Z] TOOL RESULT

```
page-33.json
page-311.json
page-46.json
page-101.json
page-56.json
page-39.json
page-61.json
page-62.json
page-74.json
page-65.json
---
"derivation": "Two words of unequal standing. (a) baēšaza- is genuine Younger Avestan, but its meaning is not 'doctor': Bartholomae col. 915-916 gives '1) Adj. (fem. -a-) \
"derivation": "The form is real but is not the ordinary Middle Persian word for 'physician'. Horn, Grundriss no. 183, from which Nourai's reference AEF:237 (Khaleqi Motlaq's Persian translation of Horn) derives, lis
"derivation": "The Persian word and its meaning are beyond doubt — Borhān-e Qāṭeʿ has it as a headword ('pezešk, on the pattern of serešk: they call the sage, the physician and the surgeon [so]; it also occurs with 
"derivation": "Gharib's Sogdian Dictionary, printed p.117, entry 2972: 'βyc B,M — βēč — ⓔ<Av. baēšaza- — ⓞ obl. pl. ~ty ⇒ βyc'n … physician. SCE 272; GMS 384; βycty, BBB 517; gen. pl. βycẖ TSP 9.78, 95; GMS 1230'. T
"derivation": "Latin for, fārī 'to speak' is the textbook Italic continuation of the root. Pokorny p.106 in the same article: 'lat. for; fārī (aus *fa-i̯ō(r) = ksl. bajǫ, ags. bōian) \
"derivation": "All five are Latin-via-French borrowings within the fārī family, and Watkins/AHD assigns every one of them to bha-2. infant: L. īnfāns, -antis 'not speaking' (negative in- + pres. part. fāns of fārī)
```


## [2026-09-05T06:29:41.647Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob\nfor p in ['page-74.json','page-65.json']:\n    d=json.load(open(p))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if n['verdict']=='transcription_suspect':\n                print(p, n.get('words'), '|', n.get('error_in'), '|', n.get('book_prints'),'|',n.get('correct_form'))\n                print('   ', n['derivation'][:400])\nEOF",
 "description": "Inspect prior transcription_suspect handling"
}
```


### [2026-09-05T06:29:43.198Z] TOOL RESULT

```
page-74.json ayare; prô-ayare | book | prô-ayare : yesterday | *parō.ayare 'the day before yesterday' (Horn's starred reconstruction)
    (a) Av. ayarə 'day' is real and correctly placed: it is the nom.-acc. sg. of the neuter r/n-heteroclite ayar-/ayan- (gen. ayąn), Bartholomae AiW col. 157, and it is the direct Iranian continuant of PIE *h₂óy-r̥. (b) 'prô-ayare' is not an attested Avestan word and, as printed, not a possible one — Avestan has no prō-. The source Nourai follows here (AEF:376 = Khaleqi Motlaq's Persian translation of
page-65.json ardĕre : to be on fire; arĕre : to become dry (land); ara : an area | book | ara : an area | ārea 'open piece of ground' (the etymon of French are / English area); Latin āra is a separate word of the same root meaning 'altar, hearth'
    The first two items are right, though the book's breves are wrong for the vowel quantities: ārdēre 'to be on fire' (Klein: 'ardēre ... stands for *āridēre, fr. āridus, "parched, dry", and is rel. to ārēre, "to be dry", fr. *āsēre, fr. I.-E. base *ās-'), with perfect ārsī and participle ārsus that carry the family into Romance; and ārēre 'to be dry', the stative *h₂eh₁s-eh₁- of the root. The third 
page-65.json area; arson | extraction | the arrow for this box is drawn from the bottom of the Latin box (node #1) — it runs down from that box, turns right and ends at the 'English | area, arson' box; the root's own spine has no arrowhead entering this line | parent should be #1 (Latin), not #0 (the root)
    The words themselves are exactly right and both come through Latin, which is what the printed chart draws and what the JSON's 'parent: 0' loses: area was borrowed from Latin ārea in the 1530s ('vacant piece of ground'), the sense 'amount of surface within limits' following in the 1560s; arson entered English in the 1670s as a law term from Anglo-French arsoun / Old French arson, from Late Latin ar
```


## [2026-09-05T06:30:13.754Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== BQT v1/v2 ==\"; grep -c \"فلوئور\\|انفلوانزا\\|کلروفیل\\|فلورسانت\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null\necho \"== ARY ==\"; grep -c \"فلوئور\\|انفلوانزا\\|کلروفیل\\|فلورسانت\" incoming/ARY/ARY_pages.txt 2>/dev/null; grep -n -i -c \"bhel\\|BHEL\" incoming/ARY/ARY_latin_index_pages.txt\necho \"== HRN/HUB ==\"; grep -c \"fluor\\|Chlorophyll\\|Influenza\" HRN.txt HUB.txt 2>/dev/null",
 "description": "Check Borhan, Aryanpur, Horn for the loanwords"
}
```


### [2026-09-05T06:30:13.847Z] TOOL RESULT

```
== BQT v1/v2 ==
incoming/BQT/BQT_v5_pages.txt:0
incoming/BQT/BQT_v4_pages.txt:0
BQT_v1_pages.txt:0
incoming/BQT/BQT_v3_pages.txt:0
BQT_v2_pages.txt:0
== ARY ==
0
0
== HRN/HUB ==
HRN.txt:0
HUB.txt:0
```


## [2026-09-05T06:30:19.046Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"Bellows\\.\\{0,220\\}\\|Bowl (1)\\.\\{0,200\\}\\|Bull (1)\\.\\{0,200\\}\\|Bold\\.\\{0,200\\}\\|Blossom\\.\\{0,200\\}\\|Blade\\.\\{0,200\\}\\|Belly\\.\\{0,200\\}\" SKT.txt | head -12",
 "description": "Grep Skeat for the Germanic English words"
}
```


### [2026-09-05T06:30:20.677Z] TOOL RESULT

```
1709:Belly.
1861:Blade
2026:Bold.
17768:Bold
```


## [2026-09-05T06:30:23.083Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1709,1712p;1861,1864p;2026,2029p' SKT.txt",
 "description": "Print Skeat entries"
}
```


### [2026-09-05T06:30:23.128Z] TOOL RESULT

```
embellish.  (F.  —  L. )    M .  E.  tmbelissfn . -•O.  F.  imbiiiss;  stem  of  prcs.  pt.  of  em- bcUir,  to  beautify.  — O.  F.  tm-  (  =  L.  i«)  J and  btl,  fair  (above). Belligerent.  (U)    See  Dual. Bellow,  tumalcc  a  iuud  i)m>c.  (E.)    Ex- feuded  frorn  M.  V..  beilcn,  llie  more  usual  old form.     A-S.  bellan,  to  make  a  loud  noi&c. (^  BHAL.)     Cf.  IccL  belja,  to  bellow. beU,  (E.)    M.  E.  bilk.  A.  S.  telle,  that hich  makes  a  loud  noise,  a  bcU.— A.S. '//dii;  u  above.     And  boe  BuU  (i). BeUowB,  Belly.  (E.)    Sec  Bag. Belong,  Beloved,  Below ;  see  Xions,
laOVe,  liOW.
Bolt,  a  girdle.  (E.)  M.  E.  beU,  A.S. ^//.^Icel.  belti\  Irish  and  GaeL  M//.  a belt,  border;  L.  balteus;  O.  II.  G.  Ao/j.
baldric,  a  girdle.  (F.-O.H.G.)  Q.F. baldric*  (not  recorded),  the  oWlt  form  of O.K.  bala'ret,  baldrei\  Low  L.  baldringm. »U,  U.  G.  balderti^/i,  a.  girdle;  extended from  O.  11.  G.  ba/x,  a  belt.
Blade,  a  leaf,  flat  of  n  ^^ biade.    A.S.  iAr./,alcaf.+  i Dan.,   Du.  idad,   a   leaf.   L...^..  , Prob.  allied  to  Blow  (J).
Blain.  (E)    See  Blow  (1).
Blame.  (F.-L.-Ck/k  See  B1
Blanch  (1),  to  wliiieo.   (F.^Ol! See  BUnk.
Bold.  (E.)  M.  E.  bold,  bald;  A.& bald.  +    Icel.  ballr',  Du.  ^m/;    CRI ftald,  ba/di  cf.  Goth,  balthaba^  adv.
bawd.   (F.-G.)    M.E.   band^,  Ck< O.  F.  baud,  gay,  wanton. «0.  U.  G. bold,  free.
Bolo.  (Scand.)    Sec  Bulge.
BoUed.  swollen.  (Scand.)    Sec  Balfa
```


## [2026-09-05T06:31:26.269Z] AGENT

Now let me write the verification file.


## [2026-09-05T06:31:29.073Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg85.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/85.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page 85 PNG for audit"
}
```


### [2026-09-05T06:31:29.145Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  58953 Sep  5 02:13 80.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99904 Sep  5 02:17 81.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74477 Sep  5 02:22 82.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67094 Sep  5 02:26 83.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63329 Sep  5 02:31 85.png
```


## [2026-09-05T06:37:18.897Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-85.json <<'JSONEOF'\n{\n  \"pdf_page\": 85,\n  \"book_page\": 55,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Bhel, Bhelgh, Bhlei, Bhleu\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *bʰel- 'to blow, swell' (Pokorny 3. bhel-, pp. 120-122) together with *bʰel-/*bʰleh₃- 'leaf, blossom, to bloom' (Pokorny 4. bhel-, p. 122) and its three extensions *bʰelǵʰ- 'to swell' (p. 125), *bʰlei- 'to blow, swell, overflow' (p. 156) and *bʰleu- 'to swell, well up, overflow, flow' (pp. 158-159)\",\n      \"note\": \"Root box, language label and gloss are all correct, and Nourai's four headwords map one-to-one onto the four Pokorny lemmas his five page numbers point to: p.120-122 = '3. bhel- aufblasen, aufschwellen' (with the Wurzelform bhlē-), p.122 = '4. bhel- und bhlē-, bhlō-, bhlə(d) Blatt, Blüte, blühen; üppig sprießen', p.125 = 'bhelgh- schwellen; Balg', p.156 = '2. bhlei- aufblasen, schwellen, strotzen, überfließen. Erw. von bhel-', p.158-159 = 'bhleu- aufblasen (schnauben, brüllen), schwellen, strotzen, überwallen, fließen. Erw. von bhel-'. The composite gloss 'to swell, blow, thrive, grow, bloom, overflow' is a fair summary of the union of those five glosses, and Pokorny himself explicitly ties them together ('Dazu 4. bhel- blühen usw. und die Erweiterungen bhelgh-, bhlēdh-, bhlegʷ-, bhlei-, bhleu- schwellen usw.'). The label 'Indo-European' is right; note only that Pokorny's homophonous 1. bhel- 'glänzend, weiß' (pp. 118-120) is a different lemma, which Nourai correctly keeps out of this chart. The page carries a second heading 'Bhelgh — see root: Bhel', a pure redirect, not verified here.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰel- «باد کردن، آماسیدن» و گونه‌های گسترش‌یافتهٔ آن *bʰelǵʰ-، *bʰlei- و *bʰleu- که همگی معنای «آماسیدن، برآمدن، سرریز شدن» دارند، و نیز ریشهٔ همسانِ *bʰleh₃- «شکوفه، برگ، شکفتن». پنج شمارهٔ صفحهٔ نورایی (۱۲۰، ۱۲۲، ۱۲۵، ۱۵۶، ۱۵۸) دقیقاً به همان پنج مدخل پوکورنی اشاره دارد و برچسب زبانی و معنای داده‌شده درست است. والده-پوکورنی (جلد دوم، ص ۱۷۶-۱۷۷، ۱۸۲، ۲۱۳) و واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage نیز همین را می‌گویند. ادعای نورایی دربارهٔ خودِ ریشه درست است؛ تنها باید توجه داشت که ریشهٔ همنامِ *bʰel- «درخشیدن، سپید» (پوکورنی ص ۱۱۸-۱۲۰) جداست و نورایی آن را در این نمودار نیاورده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/fluo\",\n        \"https://en.wiktionary.org/wiki/flos\",\n        \"https://en.wiktionary.org/wiki/%CF%86%CF%8D%CE%BB%CE%BB%CE%BF%CE%BD\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:120\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 128-130 (printed pp. 120-122), lemma '3. bhel- aufblasen, aufschwellen': Germanic bolla, bulki, balþa- 'kühn' etc., 'mit Formans -to- und der Bed. geschwollen = hochfahrend, kühn, got. bal-þaba Adv. kühnlich … ahd. bald kühn'. WP. II 177 f. Exactly the swell/blow sense of the root box.\"},\n        {\"ref\": \"POK:122\", \"status\": \"supports\", \"note\": \"POK_01.txt (printed p.122), lemma '4. bhel- und bhlē-, bhlō-, bhlə(d) Blatt, Blüte, blühen; üppig sprießen … wohl aus bhel- schwellen im Sinne von pflanzlicher Üppigkeit und Schwellung = Knospe. Gr. φύλλον Blatt (*bhŭliom), lat. folium ds. … bhlē-, meist bhlō- in: lat. flōs, -ōris m. Blume … ags. blōstma, blōsma, blōstm Blume … mit ə: ahd. blat, as. blad, ags. blæd, aisl. blað n. Blatt'. Covers folium, phullon, flōs, blossom and blade in one lemma.\"},\n        {\"ref\": \"POK:125\", \"status\": \"supports\", \"note\": \"POK_01.txt (printed pp. 125-126): 'bhelgh- schwellen; Balg (aufgeblasene Tierhaut), Kissen, Polster (Erw. von bhel- aufblasen usw.) … got. balgs m. Schlauch … engl. belly Bauch, bellows Blasebalg (germ. *balgi-)'. Supports both the extension and the English words of node #10.\"},\n        {\"ref\": \"POK:156\", \"status\": \"supports\", \"note\": \"POK_01.txt (printed pp. 156-157): '2. bhlei- aufblasen, schwellen, strotzen, überfließen, Erw. von bhel- ds. Norw. dial. bleime, aschwed. blema Hautbläschen … dän. blegn(e) Bläschen (*blajjinōn), ags. blegen, engl. blain'. The lemma is right; Pokorny lists blain but not blister (see node #11).\"},\n        {\"ref\": \"POK:158\", \"status\": \"supports\", \"note\": \"POK_01.txt (printed pp. 158-159): 'bhleu- aufblasen (schnauben, brüllen), schwellen, strotzen, überwallen, fließen, Erw. von bhel- (aufblasen), aufschwellen … g̑-Erweiterung bhleug̑- … lat. fluō, -ere, flūxī, flūctum, jünger flūxum fließen, strömen, flūctus Strömung, Woge, flūmen (*fleugsmen) strömendes Wasser, Fluß … fluvius Fluß'. This is the source of node #1's fluere.\"},\n        {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt: 'bhel-2. To blow, swell … [Pok. 3. bhel- 120.]', 'bhel-3. To thrive, bloom. Possibly from bhel-2 … [Pok. 4. bhel- 122.]', 'bhelgh-. To swell. Extension of bhel-2 … [Pok. bhelgh- 125.]', 'bhlei-. To blow, swell. Extension of bhel-2 … [Pok. 2. bhlei- 156.]', 'bhleu-. To swell, well up, overflow. Extension of bhel-2 … [Pok. bhleu- 158.]'. Watkins' own Pokorny page citations are letter-for-letter the five numbers Nourai prints, so the whole root box is copied from a reliable modern source.\"},\n        {\"ref\": \"ROE:65,66\", \"status\": \"not_checked\", \"note\": \"R. Claiborne, The Roots of English (1989) is lending-only on archive.org (refs_online.json: 'RE-SEARCH 2026-09: borrowable only'); no copy on disk.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Bd. I pp. 120-122, 122, 125-126, 156-157, 158-159\", \"stance\": \"supports\", \"note\": \"All five lemmas found in POK_01.txt at the cited printed pages; see ref_check above for the quoted headings.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II pp. 176-177, 182-183, 210, 213-214\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt line 11564: '3. bhel- und bhlē-, bhlō- bhlə(d) Blatt, Blüte, blühen; üppig sprießen, wohl in alter Zeit bereits ziemlich verselbständigte Entw. aus bhel- schwellen … Gr. φύλλον Blatt (*bholiom), lat. folium ds. (*bholiom)'; line 11975: 'bhelgh schwellen; Balg (aufgeblasene Tierhaut), Kissen, Polster (Erw. von bhel- aufblasen usw.)'; line 13762: '2. bhlei- aufblasen, schwellen, strotzen, überfließen, Erw. von bhel- ds.'; line 13898: 'bhleu- aufblasen (schnauben, brüllen), schwellen, strotzen, überwallen, fließen, Erw. von bhel-'. Pokorny's own WP references (WP. II 176 f., 182 f., 210, 213 f.) check out.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. bhel-2, bhel-3, bhelgh-, bhlei-, bhleu-\", \"stance\": \"supports\", \"note\": \"Quoted in ref_check; Watkins groups exactly these five under one another ('Extension of bhel-2', 'Possibly from bhel-2').\"},\n        {\"src\": \"SYN\", \"where\": \"Buck §8.56 'Leaf' (p. 525) and §5.57 'Flower'\", \"stance\": \"partial\", \"note\": \"grep 'folium' in SYN.txt, p.525: 'Words for leaf are connected with words for bloom, flower (orig. swell?) … From a root *bhel-, seen also in [words] for flower (5.57), and perh. ultimately the same as that in words resting on the notion of swell (Lat. follis …) … Grk. φύλλον, Lat. folium'. But Buck adds on the same page: 'Lat. folium could also be put with this group [Ir. duille, W. dail : Grk. θάλλω bloom], instead of as above, 1. Cf. Ernout-M. s.v.' — i.e. the *bʰel- assignment of folium was already open in 1949.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Latin\",\n          \"words\": \"fluere; fluere-ëscent; in-fluentia; folium; flôs, flôr\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"fluere-ëscent : showing a flow\",\n          \"correct_form\": \"no such Latin word: the real chain is Latin fluor 'a flowing' (< fluere) → the 17th-c. mineral name fluor / fluorspar → Stokes's fluorescence (1852) → fluorescent\",\n          \"derivation\": \"Four of the five items are genuine Latin, but they belong to two different branches of the composite root, and the second item is not a Latin word at all. (a) fluō, fluere, flūxī 'to flow' is the Italic outcome of Pokorny's bhleu- in its g̑-extension bhleug̑- (POK 158-159: 'lat. fluō, -ere, flūxī, flūctum … flūmen (*fleugsmen) strömendes Wasser'); Wiktionary, following de Vaan 2008, writes PIE *bʰlewH- 'to overflow' > Proto-Italic *flow-e/o- > fluō, cognate with Gk. φλέω 'abound' and φλύω 'boil over', and warns explicitly that English flow is NOT related. (b) 'fluere-ëscent' cannot be Latin: -escent is the English/French shape of the Latin inchoative participle -ēscēns, and no *fluēscēns is attested. The real history has no such link: Latin fluor 'a flowing, flux' (Ernout-Meillet s.v. fluō: 'fluor, -ōris m.: écoulement, flux') was revived c.1660 as the chemists' name for readily fusible minerals used as smelting fluxes, hence fluorspar; Sir George Stokes coined fluorescence in 1852 from fluor(spar) + -escence on the model of phosphorescence (Klein s.v. fluorescence), and Davy had coined fluorine from fluor in 1813. The chart's own descendants are therefore reached through the mineral name, not through a Latin verbal adjective. (c) 'in-fluentia' is Medieval Latin influentia, an astrological term ('inflowing' of the stars) built on the present participle of influere 'to flow in' (in- + fluere); the hyphen is Nourai's usual way of showing prefix + stem, and the item is right for medieval, not classical, Latin. (d) folium 'leaf' and (e) flōs, flōr- 'flower' belong to the other Pokorny lemma, 4. bhel-/bhlē-, bhlō- (POK 122: 'lat. folium … bhlē-, meist bhlō- in: lat. flōs, -ōris m. Blume'); Wiktionary derives flōs from *bʰleh₃-s 'flower, blossom'. For folium the traditional *bʰolh₃yom is still the majority view, but Driessen and de Vaan prefer *dʰolh₁yom to *dʰelh₁- 'be green' (Ir. duille, W. dail, Gk. θάλλω, Arm. dalar), a doubt Buck already registered in 1949.\",\n          \"derivation_fa\": \"از پنج صورتی که در جعبهٔ لاتینی آمده، چهار تا لاتینی راستین‌اند ولی به دو شاخهٔ جدا از ریشه تعلق دارند و یکی اصلاً واژهٔ لاتینی نیست. fluere «روان شدن» بازماندهٔ منظمِ گونهٔ گسترش‌یافتهٔ *bʰleug̑- است (پوکورنی ص ۱۵۸-۱۵۹؛ دخوان ۲۰۰۸: *bʰlewH- «سرریز شدن» ← ایتالیایی آغازین *flow-e/o- ← fluō) و همریشهٔ یونانی φλύω «جوشیدن» است. اما «fluere-ëscent» صورتی ناممکن است: پسوند ‑escent فرانسوی/انگلیسی است، نه لاتینی، و راه واقعی چنین بوده که از fluere اسمِ fluor «روانی، جریان» ساخته شد، این نام در سدهٔ هفدهم بر کانی‌های زودگدازِ کورهٔ ذوب (fluorspar) نهاده شد و استوکس در ۱۸۵۲ از همان نام کانی واژهٔ fluorescence را ساخت. in-fluentia نیز لاتینی میانه (نه کلاسیک) است و اصطلاحی احکام‌نجومی به معنای «فروریختن تأثیر ستارگان» است. folium «برگ» و flōs/flōr «گل» به مدخل دیگر پوکورنی (ص ۱۲۲، «برگ، شکوفه، شکفتن») تعلق دارند؛ دربارهٔ folium نظر امروزی دوپاره است و دریسن و دخوان آن را از ریشهٔ *dʰelh₁- «سبز بودن» می‌گیرند. داوری: خطای چاپی/ساختگیِ خودِ کتاب در صورت «fluere-ëscent»؛ بقیهٔ پیوندها درست‌اند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/fluo\",\n            \"https://en.wiktionary.org/wiki/folium\",\n            \"https://en.wiktionary.org/wiki/flos\",\n            \"https://www.etymonline.com/word/fluorine\",\n            \"https://www.etymonline.com/word/influenza\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. bhleu-: 'Extended form bhleug̑- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; … (FLUORIDE), … INFLUENCE, (INFLUENZA)'; and s.v. bhel-3: 'I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf … 2. Greek phullon, leaf … d. Latin flōs (stem flōr-), flower'. Watkins supports every genuine item of the box, but he too routes fluor/fluorescent through the noun fluor, never through a Latin *fluerescent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Bd. I pp. 122 and 158-159\", \"stance\": \"supports\", \"note\": \"'lat. fluō, -ere, flūxī, flūctum … fluvius Fluß (vom Präs. fluō aus)' (p.159) and 'lat. folium ds.; … lat. flōs, -ōris m. Blume; flōreō, -ēre blühen' (p.122).\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. fluō (line 23073 of LAT.txt) and s.v. flōs/folium\", \"stance\": \"supports\", \"note\": \"'fluō … -is, -xī, -ctum puis -xum, -ere; couler (= ῥέω) … Dérivés et composés: fluor, -ōris m.: écoulement, flux, diarrhée … fluidus'. The Latin noun fluor that the French/Persian words really descend from is here, s.v. fluō.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck §8.56 'Leaf', p. 525\", \"stance\": \"partial\", \"note\": \"'From a root *bhel- … Grk. φύλλον, Lat. folium' but immediately: 'Lat. folium could also be put with this group [Grk. θάλλω bloom, flourish], instead of as above. Cf. Ernout-M. s.v.'\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. fluor, fluorescence, fluorine (line 15025-15026)\", \"stance\": \"partial\", \"note\": \"'fluor, n., a mineral containing fluorine, fluorite. — ModL., fr. L. fluor, a flowing, fr. fluere, to flow' and 'fluorescence … Formed with suff. -escence (on analogy of opalescence, phosphorescence) fr. fluor(spar). The word fluorescence was coined by … Sir George Gabriel Stokes … in 1852 in allusion to the circumstance that he noticed this phenomenon first in fluorspar.' Klein supports Latin fluere as the ultimate source but contradicts the printed 'fluere-ëscent'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box with no reference of its own (refs=None): it only states that the Latin material reached Persian and English through French. That is true of everything hanging below it. French took fluor from Neo-Latin as a mineralogical term in the 18th century, fluorescent from Stokes's English coinage after 1852, and influenza from Italian (attested in French from the 1780s); it is also the transmitter of English flux, fluid, fluent, foliage (feuillage), portfolio (portefeuille), florist (fleuriste), flourish (florir/fleuriss-) and flower (flour < OF flor, flour). No verification problem: the box asserts a route, not a word.\",\n          \"derivation_fa\": \"این جعبه واژه‌ای ندارد و تنها گذرگاه است: می‌گوید واژه‌های لاتینی از راه فرانسوی به فارسی و انگلیسی رسیده‌اند. این ادعا درست است؛ فرانسوی fluor را از لاتینی نو، fluorescent را از انگلیسیِ استوکس، و influenza را از ایتالیایی گرفته است و همچنین واسطهٔ واژه‌های انگلیسیِ flux، fluid، feuillage/foliage، portefeuille/portfolio، fleur/flower و مانند آن‌هاست. چون خودِ جعبه واژه‌ای ندارد، تنها مسیر آن سنجیده شد و درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/fluorine\",\n            \"https://www.etymonline.com/word/influenza\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book (refs=None); nothing to check.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. fluor / fluorescence / chlorophyll\", \"stance\": \"supports\", \"note\": \"Klein routes every one of these through French or Modern Latin ('F. chlorophylle, coined by the French chemists …'; 'ModL., fr. L. fluor').\"},\n            {\"src\": \"DEV\", \"where\": \"grep 'fluor', 'influenza' in DEV.txt (Devic, mots français d'origine orientale)\", \"stance\": \"silent\", \"note\": \"Nothing found, as expected: these are learned Latin/Italian words, not orientalisms; Devic covers only the latter.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"folŭor «فلوئور»; flŭoresânt «فلورسانت»; ânflŭânzâ «آنفلوآنزا ، انفلوآنزا»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All three are 20th-century European loans and the French route is right for all three, but the third one has an Italian stage that the chart skips. (a) فلوئور folu'or is French fluor [flɥɔʁ], the mineralogical/chemical name coined on Latin fluor 'a flowing'; Persian resolves the French [ɥ] into ـوئـ, giving the disyllabic فلوئور. Mo'in gives it the tag [فر.] (French) with the Latin-script form 'fluor'. (b) فلورسانت fluoresânt is French fluorescent; the French participial ending -ent [ɑ̃] is regularly taken into Persian as ـانت -ânt (cf. رستوران، آسانسور type borrowings), and the sense in Persian has narrowed to the concrete 'fluorescent tube/lamp', which is how Nourai glosses it. (c) آنفلوآنزا / انفلوانزا ânfluânzâ is French influenza, and the Persian shape is itself the proof of the French route: the two French nasal vowels [ɛ̃ … ɑ̃] appear as ân- and -ân-, which no direct borrowing from Italian influenza or English influenza could produce. Mo'in tags it [فر.]. But influenza is not a French or Latin creation: it is Italian influenza 'influence (of the stars)', applied to epidemics in Italy from 1504 and spread over Europe after the 1743 epidemic (Klein: 'influenza, n. … — It., lit. influence … The disease was so called because it was originally attributed to the influence of the stars'; Etymonline: English 1743, from Italian). Nourai's chart runs Latin → French → Persian and leaves the Italian intermediary out, so his own NOTE ('it literally means influence (of a virus)') is right about the meaning but the route is one stage short. Hence plausible, not confirmed.\",\n          \"derivation_fa\": \"هر سه واژه وام‌واژه‌های سدهٔ بیستم‌اند و راهِ فرانسوی برای هر سه درست است. «فلوئور» از فرانسویِ fluor است که خود از لاتینیِ fluor «روانی» ساخته شده؛ صامت میانیِ فرانسوی [ɥ] در فارسی به «وئـ» تحلیل رفته است. «فلورسانت» از فرانسویِ fluorescent است و پسوند فرانسویِ ‑ent در فارسی به «ـانت» بدل می‌شود؛ معنای آن در فارسی به «لامپ مهتابی» تخصیص یافته است. «آنفلوآنزا» از فرانسویِ influenza است و خودِ ساختِ واژه گواهِ همین راه است، زیرا دو واکهٔ خیشومیِ فرانسوی در فارسی «آن…آن» شنیده شده‌اند و از ایتالیایی یا انگلیسی چنین صورتی پدید نمی‌آمد؛ معین نیز هر سه را [فر.] نشان کرده است. با این همه، اصلِ influenza ایتالیایی است («تأثیر ستارگان»، از ۱۵۰۴ برای بیماری‌های همه‌گیر) و نورایی این حلقهٔ ایتالیایی را از قلم انداخته است. داوری: با احتیاط پذیرفتنی است؛ یادداشت نورایی دربارهٔ معنای «تأثیر» درست است ولی مسیر یک پله ناقص است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%81%D9%84%D9%88%D8%A6%D9%88%D8%B1/\",\n            \"https://www.etymonline.com/word/influenza\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:97,386,2573\", \"status\": \"supports\", \"note\": \"Mo'in's lexicon has all three with a French tag. Local OCR MON_part1.txt line 18197: 'انفلوانزا: [فر.] (اِ.) (پز.) نوعی سرماخوردگی شدید و ساری' — the bracket [فر.] is Mo'in's mark for French. For فلوئور the Mo'in text via abadis.ir reads '[فر.] fluor' with the gas definition ('گازی زردرنگ و سمی … در هیدروژن مایع منجمد می‌شود'). The three page numbers belong to the 6-vol. Amir Kabir edition, which is not the edition digitised here, so the exact pages could not be matched; the entries themselves are confirmed.\"},\n            {\"ref\": \"VOP:251\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (1371/1992) — refs_online.json records 'RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook'. Not accessible.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 18197 (انفلوانزا); abadis.ir فرهنگ معین s.v. فلوئور\", \"stance\": \"supports\", \"note\": \"Both carry Mo'in's [فر.] French tag; the Mo'in entry for فلوئور also prints the Latin-script 'fluor'. فلورسانت is not in the digitised Mo'in text (grep 'فلورسانت' in MON_part1/part2: 0 hits).\"},\n            {\"src\": \"BQT\", \"where\": \"grep 'فلوئور|انفلوانزا|فلورسانت' in BQT_v1..v5_pages.txt\", \"stance\": \"silent\", \"note\": \"0 hits in all five volumes — expected, since Borhan-e Qate' is a 17th-century dictionary and cannot contain 20th-century European loans.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 19350 s.v. influenza\", \"stance\": \"partial\", \"note\": \"'influenza, n., an acute contagious disease. — It., lit. influence (see influence). The disease was so called because it was originally attributed to the influence of the stars.' Klein makes the word Italian, i.e. the stage Nourai's Latin→French arrow omits.\"},\n            {\"src\": \"ARY\", \"where\": \"grep 'فلوئور|انفلوانزا|کلروفیل|فلورسانت' in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"0 hits; Aryanpur's dictionary of the Indo-European roots of Persian treats inherited vocabulary, not modern European loans.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"flux, fluid, fluent, flush, fluoride, fluorescent, influence, foliage, portfolio, Florence, florist, flourish, flower.\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Every word in the list is assigned to this root by Watkins, and each entered English from Latin through French. The fluere group (Pokorny's bhleu-): flux < OF flux < L. flūxus; fluid < L. fluidus; fluent < L. pres. part. fluēns, -entis; flush (the 'flow suddenly' word, AHD's FLUSH2) < OF flus/flux; fluoride and fluorescent are 19th-century chemical formations on fluor (Davy 1813, Stokes 1852) taken over from French/Neo-Latin; influence < OF influence < ML influentia. The folium/flōs group (Pokorny's 4. bhel-): foliage < OF fueillage/feuillage < feuille < L. folia; portfolio < It. portafoglio 'carry-leaf'; Florence < L. Florentia 'the flourishing (city)', a derivative of flōs; florist (1620s, on L. flōr-); flourish < OF floriss-, stem of florir < VL. *flōrīre for L. flōrēre 'to bloom'; flower < ME flour < OF flor, flour < L. flōrem. The single 'French' parent box is a slight simplification for the most learned members (fluid, fluent, fluoride are direct Latin/Neo-Latin borrowings rather than French ones), but the root assignment is exactly Watkins's.\",\n          \"derivation_fa\": \"همهٔ واژه‌های این جعبه در پیوستِ واتکینز به همین ریشه بازگردانده شده‌اند و همگی از لاتینی و بیشتر از راه فرانسوی به انگلیسی رسیده‌اند: گروهِ fluere (شاخهٔ *bʰleu-): flux از flūxus، fluid از fluidus، fluent از اسم فاعلِ fluēns، flush، و نیز fluoride و fluorescent که ساخته‌های شیمیِ سدهٔ نوزدهم بر پایهٔ fluor اند، و influence از influentia. گروهِ folium/flōs (شاخهٔ «برگ و شکوفه»): foliage از feuille، portfolio از ایتالیاییِ portafoglio، Florence از Florentia «شکوفان»، florist، flourish از florir و flower از flōrem. تنها نکتهٔ کوچک آن است که چند واژهٔ کتابی (fluid، fluent، fluoride) یکراست از لاتینی/لاتینی نو گرفته شده‌اند نه از فرانسوی. داوری: ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/fluorine\",\n            \"https://www.etymonline.com/word/influenza\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. bhleu- lists 'FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (INFLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS'; s.v. bhel-3 it lists 'FOIL2, FOLIAGE, FOLIO, FOLIUM; … PORTFOLIO, TREFOIL' and 'FLORA, (FLORAL), … FLORIN, FLORIST, -FLOROUS, … FLOUR, FLOURISH, FLOWER'. The English index of the same book confirms word by word ('FLUX bhleu-', 'FLUID bhleu-', 'FLUOR bhleu-').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. fluor, fluorescence, fluorine, influenza\", \"stance\": \"supports\", \"note\": \"'fluorine … Coined by … Sir Humphry Davy … fr. fluor with chem. suff. -ine … because it was found first in fluorspar'; 'fluor … ModL., fr. L. fluor, a flowing, fr. fluere'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index, s.vv. FLUX / FLUID / FLUOR / FLOWER\", \"stance\": \"supports\", \"note\": \"'bhleu- EFFLUVIUM … FLUENT … FLUID … FLUOR … FLUORIDE … FLUX' and 'BLOSSOM bhel-3 … BLOW3 bhel-3'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Greek\",\n          \"words\": \"phullon; xlôros-phullon\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"φύλλον 'leaf' is genuine Ancient Greek and is the exact counterpart of Latin folium: Pokorny p.122 sets both up as *bhŭliom/*bholiom under 4. bhel-, and Beekes (EDG 2010, quoted by Wiktionary) writes *bʰol-yom from *bʰleh₃- 'leaf, blossom, flower', cognate with Lat. folium, Arm. բողբոջ bołboǰ and English blossom. Greek -λλ- is the regular outcome of *-ly-. The second item, xlôros-phullon (χλωρός 'pale green, yellow-green' + φύλλον), is not an attested Ancient Greek compound: χλωροφύλλον exists only as the Greek model that Pelletier and Caventou put together in French in 1817. Nourai's own cross-reference '☞ Ghel' for χλωρός is correct — it belongs to PIE *ǵʰelh₃-/*ǵʰel- 'to shine; green, yellow' (the root of gall, yellow, gold), a different root, which is why he sends the reader elsewhere for it. So the box is right as a display of the two Greek elements, but wrong if read as an attested Greek word.\",\n          \"derivation_fa\": \"«φύλλον» یونانیِ باستان و به معنای «برگ» است و درست برابرِ folium لاتینی؛ پوکورنی (ص ۱۲۲) هر دو را از *bholiom می‌گیرد و بیکس (۲۰۱۰) صورت *bʰol-yom از ریشهٔ *bʰleh₃- را بازسازی می‌کند؛ ‑λλ‑ یونانی دگرگونیِ منظمِ *‑ly‑ است. اما «xlôros-phullon» به عنوان یک واژهٔ یونانیِ باستان گواهی نشده است؛ χλωροφύλλον تنها الگویی یونانی است که پلتیه و کاوانتوی فرانسوی در ۱۸۱۷ ساخته‌اند. ارجاعِ خودِ نورایی به ریشهٔ Ghel برای χλωρός درست است، زیرا آن واژه از ریشهٔ دیگری (*ǵʰelh₃- «درخشیدن، سبز و زرد») است. داوری: با احتیاط پذیرفتنی است؛ جزءِ نخست درست و جزءِ دوم ساختی نو است، نه یونانیِ باستان.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%86%CF%8D%CE%BB%CE%BB%CE%BF%CE%BD\",\n            \"https://en.wiktionary.org/wiki/folium\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. bhel-3: 'I. Suffixed o-grade form *bhol-yo-, leaf. … 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN.' Watkins supports phullon but has no χλωρόφυλλον; chlorophyll is entered by him under ghel-2 as well, i.e. as a modern compound of two roots.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 122\", \"stance\": \"supports\", \"note\": \"'Gr. φύλλον Blatt (*bhŭliom), lat. folium ds.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 176\", \"stance\": \"supports\", \"note\": \"'Gr. φύλλον Blatt (*bholiom), lat. folium ds. (*bholiom)'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 28678 s.v. phyllo-\", \"stance\": \"supports\", \"note\": \"'phyllo-, before a vowel phyll-, combining form meaning leaf. — Gk. φυλλο-, φυλλ-, fr. φύλλον, leaf, which is cogn. with L. folium, leaf.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"chloro-phylle\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"chlorophylle is a documented French coinage of 1817 by the pharmacist-chemists Pierre-Joseph Pelletier (1788-1842) and Joseph-Bienaimé Caventou (1795-1877), who isolated the green pigment and named it from Greek χλωρός 'pale green' + φύλλον 'leaf' (Klein s.v. chlorophyll). The arrow Greek → French is therefore exactly right as a learned neo-Hellenic formation, not an inherited descent: no Greek word passed through Latin into French here, the two Greek stems were taken straight off the shelf in a Paris laboratory. Nourai's gloss 'the green pigments in plants' matches the coiners' own definition.\",\n          \"derivation_fa\": \"«chlorophylle» ساختهٔ دو داروساز-شیمی‌دان فرانسوی، پلتیه و کاوانتو، در سال ۱۸۱۷ است که رنگ‌دانهٔ سبز گیاهان را جدا کردند و آن را از دو جزءِ یونانیِ χλωρός «سبزِ روشن» و φύλλον «برگ» نامیدند (کلاین، ذیل chlorophyll). پس پیکانِ یونانی ← فرانسوی در اینجا وام‌گیریِ دانشورانه (نو-یونانی) است، نه تحولِ موروثی؛ هیچ واژه‌ای از یونانی از راه لاتینی به فرانسوی نرسیده و دو ستاکِ یونانی یکراست در آزمایشگاهِ پاریس به هم پیوسته‌اند. داوری: ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%86%CF%8D%CE%BB%CE%BB%CE%BF%CE%BD\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. bhel-3 lists Greek phullon with the derivative '-PHYLL, PHYLLO-'; chlorophyll is one of the -phyll words, its first element being entered under ghel-2 (Nourai's '☞ Ghel').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7481 s.v. chlorophyll\", \"stance\": \"supports\", \"note\": \"'chlorophyll, chlorophyl, n., the green coloring matter of plants. — F. chlorophylle, coined by the French chemists Pierre-Joseph Pelletier (1788-1842) and Joseph-Bienaimé Caventou (1795-1877) fr. chloro- and Gk. φύλλον, leaf.'\"},\n            {\"src\": \"DEV\", \"where\": \"grep 'chlorophylle' in DEV.txt\", \"stance\": \"silent\", \"note\": \"Not found — Devic covers only French words of oriental origin, so a neo-Hellenic chemical coinage is out of his scope.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"kolorofîl «کلروفیل»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"کلروفیل kolorofil is French chlorophylle taken into Persian in the modern scientific vocabulary; the French [ʃl]-less spelling ch- is read as k- because Persian took the word through the French pronunciation [klɔʁɔfil], and the French final -e is dropped, giving the four-syllable ko-lo-ro-fil. Mo'in's entry defines it as 'مادهٔ سبزرنگی در گیاهان که کار فتوسنتز را در یاخته انجام دهد' and marks the origin [فر.] (French), giving the Persian calque سبزینه sabzine (سبز 'green' + the noun suffix ‑ینه) beside it. The chart's route French → Persian is therefore exactly right, and no Arabic or Turkish mediation is involved.\",\n          \"derivation_fa\": \"«کلروفیل» وام‌واژه‌ای است از فرانسویِ chlorophylle که در واژگان علمیِ نو به فارسی راه یافته است؛ چون از تلفظ فرانسوی [klɔʁɔfil] گرفته شده، ch‑ آن «ک» خوانده می‌شود و «ـه»ی پایانیِ فرانسوی می‌افتد. معین آن را «مادهٔ سبزرنگی در گیاهان که کار فتوسنتز را در یاخته انجام دهد» تعریف کرده، ریشه را [فر.] نشان داده و برابرِ فارسیِ «سبزینه» را نیز آورده است. داوری: ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%DA%A9%D9%84%D8%B1%D9%88%D9%81%DB%8C%D9%84/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:3030\", \"status\": \"supports\", \"note\": \"Mo'in's entry (read via abadis.ir, فرهنگ معین section): 'کلروفیل [فر.] مادهٔ سبزرنگی در گیاهان که کار فتوسنتز را در یاخته انجام دهد؛ سبزینه'. The page number belongs to the 6-vol. Amir Kabir edition; the digitised copy on disk is a different (2-vol.) edition in which کلروفیل occurs only inside other entries (MON_part1.txt lines 75028-75031 'خضرة الورق، کلروفیل'), not as a headword, so p.3030 itself could not be paged to.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. کلروفیل; MON_part1.txt lines 75028-75031\", \"stance\": \"supports\", \"note\": \"The web copy of Mo'in gives [فر.] and the equivalent سبزینه; the local OCR has the word in running text ('و اگر … کلروفیل بدست آید؛ خضرة الورق، کلروفیل').\"},\n            {\"src\": \"BQT\", \"where\": \"grep 'کلروفیل' in BQT_v1..v5_pages.txt\", \"stance\": \"silent\", \"note\": \"0 hits — a 17th-century dictionary cannot have a 19th-century chemical loan.\"},\n            {\"src\": \"ARY\", \"where\": \"grep 'کلروفیل' in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"0 hits; Aryanpur treats inherited Indo-European material in Persian, not European loanwords.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"chlorophyll\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English chlorophyll (also spelled chlorophyl) is a straight borrowing of French chlorophylle, first used in English in 1819, two years after Pelletier and Caventou's coinage; the French final -e was dropped and the -ll- kept, and the word entered as a botanical/chemical term. Klein enters it under the French coinage and refers the second element to phyllo- < Greek φύλλον, exactly as the chart draws it (Greek → French → English).\",\n          \"derivation_fa\": \"«chlorophyll» انگلیسی وام‌واژهٔ مستقیم از فرانسویِ chlorophylle است و از ۱۸۱۹، یعنی دو سال پس از ساختِ آن در فرانسه، در انگلیسی به کار رفته است؛ «ـه»ی پایانی افتاده و ‑ll‑ نگاه داشته شده است. کلاین نیز آن را از فرانسوی می‌گیرد و جزء دوم را به φύλλον یونانی بازمی‌گرداند، درست همان‌گونه که نمودار می‌کشد. داوری: ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%86%CF%8D%CE%BB%CE%BB%CE%BF%CE%BD\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. bhel-3 gives Greek phullon with the English derivatives '(-PHYLL), PHYLLO-, -PHYLLOUS', the class to which chlorophyll belongs.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7481 s.v. chlorophyll\", \"stance\": \"supports\", \"note\": \"'chlorophyll, chlorophyl, n. … — F. chlorophylle, coined by the French chemists … fr. chloro- and Gk. φύλλον, leaf. See phyllo- …'\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. chlorophyll\", \"stance\": \"supports\", \"note\": \"grep 'chlorophyll' in FSD_vol1.txt: entered as a botany/chemistry term formed from Greek chloros + phyllon, agreeing with Klein on the elements.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Germanic\",\n          \"words\": \"bul; bullôn; balthaz; blôs; bladaz; balgîz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six are Watkins's reconstructed Proto-Germanic forms, copied accurately, and each is the regular Germanic outcome of the PIE shape given: (1) *bul- is the zero-grade *bʰl̥- with Grimm's law *bʰ > b, in OE bolla 'pot, bowl'; (2) *bullōn- is the suffixed zero grade *bʰl̥-n- (n-stem), in ON boli, OE bula 'bull' — the same formation gives Greek φαλλός; (3) *balthaz is the suffixed o-grade *bʰol-to- 'swollen (with courage)', in OE bald/beald, Goth. balþaba 'boldly'; (4) *blō-s- is the s-extension of *bʰleh₃- 'to bloom', in OE blōstm(a) 'blossom'; (5) *bladaz is the zero-grade *bʰl̥h₃-to- 'that which has sprouted', in OE blæd 'leaf, blade'; (6) *balgiz is the i-stem of the extension *bʰelǵʰ- 'to swell', in OE bel(i)g 'bag, bellows', Goth. balgs 'wineskin'. Two remarks that do not affect the verdict: the box mixes the branches of the composite root (bul/bullōn/balthaz from Pokorny's 3. bhel-, blōs/bladaz from 4. bhel-, balgiz from bhelgh-), which is legitimate here because Nourai's root box collects all of them; and 'Germanic' means reconstructed Proto-Germanic, not an attested language.\",\n          \"derivation_fa\": \"هر شش صورت، بازسازی‌های ژرمنیِ آغازینِ واتکینز‌اند و بی‌کم‌وکاست نقل شده‌اند و هر یک دگرگونیِ منظمِ صورتِ هندواروپاییِ خود است (با ابدالِ *bʰ به b بر پایهٔ قانون گریم): *bul- از درجهٔ صفرِ *bʰl̥- (انگلیسی کهن bolla «کاسه»)؛ *bullōn- از *bʰl̥-n- (ON boli «گاو نر»، همریشه با φαλλός یونانی)؛ *balthaz از درجهٔ o‑دارِ *bʰol-to- «آماسیده = دلیر» (گوتیِ balþaba «دلیرانه»)؛ *blō-s- گسترشِ s‑دارِ *bʰleh₃- «شکفتن» (انگلیسی کهن blōstm «شکوفه»)؛ *bladaz از *bʰl̥h₃-to- «رُسته» (انگلیسی کهن blæd «برگ»)؛ و *balgiz ستاکِ i‑دارِ گسترشِ *bʰelǵʰ- «آماسیدن» (گوتیِ balgs «مشک»). نکته آنکه این جعبه شاخه‌های گوناگونِ ریشهٔ مرکب را در کنار هم می‌آورد که در چارچوبِ همین نمودار رواست. داوری: ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/blister\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt, four lemmas, form for form: bhel-2 '1. Zero-grade form *bhl̥- in Germanic *bul- in: a. Old English bolla … BOLL, BOWL1', '2. Suffixed zero-grade form *bhl̥-n- in: a. Germanic *bullōn-, bull, in Old Norse boli: BULL1', '4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in Old English bald, beald: BOLD'; bhel-3 'c. Germanic suffixed form *blō-s- in Old English blōstm, blōstma, flower, blossom: BLOSSOM' and '3. Suffixed zero-grade form *bhl̥ə-to- in Germanic *bladaz in Old English blæd, leaf, blade: BLADE'; bhelgh- '1. Germanic *balgiz in Old English bel(i)g, belig, purse, bellows: BELLOWS, BELLY'. Nourai's six forms are these six.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Bd. I pp. 121-122 and 125-126\", \"stance\": \"supports\", \"note\": \"'ahd. bolla f. Wasserblase, Fruchtbalg …', 'mit Formans -to- und der Bed. geschwollen = hochfahrend, kühn, got. bal-þaba Adv. kühnlich, balþei f. Kühnheit … ahd. bald kühn'; 'got. balgs m. Schlauch, aisl. belgr … ahd. balg Balg, Schlauch, Blasebalg … engl. belly Bauch, bellows Blasebalg (germ. *balgi- m.)'; and p.122 'ags. blōstma, blōsma, blōstm Blume … mit ə: ahd. blat, as. blad, ags. blæd, aisl. blað n. Blatt'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. bull, bold, blossom, blade, belly\", \"stance\": \"supports\", \"note\": \"'bull … fr. OE. bula, rel. to ON. boli, MDu. bul(le) … fr. I.-E. base *bhel-, to swell'; 'bold … fr. OE. bald, beald … Goth. balþei, boldness, balþaba, boldly … fr. I.-E. base *bhel-, to swell'; 'blossom … fr. OE. blōstm, blōstma, blōsma … fr. I.-E. *bhlos-, enlarged form of base *bhlō-, to sprout, bloom'; 'blade … fr. OE. blæd, leaf … fr. I.-E. base *bhlō-, *bhlē-, *bhlə-, to sprout, bloom; leaf'; 'belly … fr. OE. bælg, belig, belg, bag, belly, bellows … fr. Teut. base *belg-, which corresponds to I.-E. base *bhelgh-, to swell'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II pp. 176-183\", \"stance\": \"supports\", \"note\": \"Same material under '3. bhel- … Blatt, Blüte' and 'bhelgh schwellen; Balg (aufgeblasene Tierhaut), Kissen, Polster (Erw. von bhel- aufblasen usw.)'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"bowl, bull, bold, blossom, blade, bellows, belly\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Each English word continues one of the six Germanic forms of the parent box, by ordinary Old English → Middle English → Modern English descent, not by borrowing: bowl 'hollow vessel' < ME bolle < OE bolla (Klein), i.e. Germanic *bul- — note that the homonym bowl 'a wooden ball, the game' is a different word, from French boule < Latin bulla, and it is the vessel that belongs here; bull < ME bule, bole < OE bula; bold < ME bold, bald < OE bald, beald; blossom < ME blosme, blossem < OE blōstm, blōstma; blade < ME blad < OE blæd 'leaf', with the sense narrowing to 'flat cutting part' only in late Middle English; bellows and belly are the same OE word bel(i)g, belg 'bag, bellows, belly', the plural of which became the tool-name bellows while the singular kept the body sense — Klein says outright 'bellows, n. pl. — ME. bely; prop. a variant of belly', and Skeat cross-refers 'Bellows, Belly. (E.) See Bag.' The chart's inclusion of belly in the English box although the Germanic box only lists balgîz 'bellows' is therefore correct, not an oversight.\",\n          \"derivation_fa\": \"هر یک از این واژه‌های انگلیسی دنبالهٔ منظمِ یکی از شش صورتِ ژرمنیِ جعبهٔ بالاست و از راهِ ارث (نه وام‌گیری) به انگلیسیِ نو رسیده است: bowl «کاسه» از انگلیسی کهن bolla (و نه bowl «گویِ بازی» که وام‌واژه‌ای است از فرانسویِ boule از لاتینیِ bulla)؛ bull از bula؛ bold از bald/beald؛ blossom از blōstm(a)؛ blade از blæd «برگ» که معنای آن در پایانِ دورهٔ انگلیسی میانه به «تیغه» تخصیص یافت؛ و bellows و belly هر دو از یک واژهٔ انگلیسی کهن یعنی belg «انبان، شکم، دَم آهنگری» اند، چنان‌که کلاین می‌نویسد «bellows در اصل گونه‌ای از belly است». پس آوردنِ belly در جعبهٔ انگلیسی، با آنکه جعبهٔ ژرمنی تنها balgîz «دَم» را دارد، درست است. داوری: ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/blister\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt: bhel-2 gives 'BOLL, BOWL1' from OE bolla, 'BULL1' from ON boli, 'BOLD' from OE bald; bhel-3 gives 'BLOSSOM' and 'BLADE'; bhelgh- gives 'BELLOWS, BELLY' from OE bel(i)g. The English index of the same volume repeats 'BLOSSOM bhel-3', 'BLOOM1 bhel-3'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 5471 (bowl), 5831 (bull), 5289 (bold), 5202 (blossom), 5109 (blade), 4721-4723 (bellows, belly)\", \"stance\": \"supports\", \"note\": \"'bowl, n., a hollow vessel. — ME. bolle, fr. OE. bolla'; 'bull … fr. I.-E. base *bhel-, to swell … For derivatives of base *bhelgh-, an enlargement of base *bhel-, see belly, budget, bulge'; 'bellows, n. pl. — ME. bely; prop. a variant of belly'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt lines 1709 (Bellows, Belly), 1861 (Blade), 2026 (Bold)\", \"stance\": \"supports\", \"note\": \"'Bellows, Belly. (E.) See Bag.'; 'Blade, a leaf … A.S. blæd, a leaf … Prob. allied to Blow (3)'; 'Bold. (E.) M.E. bold, bald; A.S. bald … cf. Goth. balthaba'. (Skeat's OCR is poor but the headword lines are legible.)\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Dutch\",\n          \"words\": \"bluyster\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word is real and Nourai's NOTE ('This is a Middle Dutch word') is roughly right — bluyster/blyster 'swelling, blister' is Middle to Early Modern Dutch (the spelling with -uy- is 16th-17th century), formed on the same *bʰlei- 'to blow, swell' as Middle Dutch blein and Old English blegen 'blain'. What is not settled is that English blister came from it. Nourai's own reference AHD, in Watkins's appendix, says only 'bhlei-. To blow, swell. Extension of bhel-2 … 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER', naming no Dutch form, and the AHD main entry now reads '[Middle English, probably from Old French blestre, of Germanic origin]'. Klein derives the English word from Old Norse instead: 'blister, n. — ME. blister, blester, fr. OF. blestre, fr. ON. blástr, a swelling, fr. blása, to blow'. Etymonline keeps both doors open ('possibly via Old French blestre or Middle Dutch blyster … from a Scandinavian source, such as Old Norse blastr'). The Dutch route is, however, exactly what the older English dictionaries printed — Webster's New Twentieth Century s.v. blister: '[ME. blister; D. bluyster; OFr. blestre, a swelling]', and Funk & Wagnalls: '[ME. blister; cp. OD. bluyster, blister. Allied to blast.]' — so Nourai is repeating a respectable older opinion, not inventing one. The PIE assignment (Pokorny's 2. bhlei-, p.156) is not in doubt at all.\",\n          \"derivation_fa\": \"واژه راستین است و یادداشتِ نورایی («این واژه هلندی میانه است») تقریباً درست: bluyster/blyster «آماس، تاول» از هلندیِ میانه و آغازِ دورهٔ نو است (املای ‑uy‑ از سدهٔ شانزدهم و هفدهم) و از همان ریشهٔ *bʰlei- «باد کردن، آماسیدن» ساخته شده که هلندی میانهٔ blein و انگلیسی کهنِ blegen «تاول» نیز از آن‌اند. آنچه قطعی نیست، این است که blister انگلیسی از همین صورتِ هلندی گرفته شده باشد: خودِ AHD تنها می‌گوید «شاید در خاستگاهِ ژرمنیِ فرانسویِ کهنِ blestre»، و کلاین آن را از نورسِ کهنِ blástr «آماس» می‌گیرد؛ ویکی‌واژه/اتیمانلاین هر دو راه را باز می‌گذارند. با این حال، فرهنگ‌های کهن‌ترِ انگلیسی (وبستر و فانک و واگنالز) صریحاً صورتِ هلندیِ bluyster را می‌آورند، پس نورایی رأیی معتبر ولی قدیمی را نقل کرده است. بازگشتِ واژه به ریشهٔ *bʰlei- (پوکورنی ص ۱۵۶) هیچ تردیدی ندارد. داوری: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/blister\",\n            \"https://www.ahdictionary.com/word/search.html?q=blister\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. bhlei-: 'To blow, swell. Extension of bhel-2. 1. Germanic *blajjinōn-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhlei- 156.]' The root assignment is Watkins's, but Watkins does not name a Dutch bluyster; the AHD main entry (online) has '[Middle English, probably from Old French blestre, of Germanic origin.]'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 5175 s.v. blister\", \"stance\": \"contradicts\", \"note\": \"'blister, n. — ME. blister, blester, fr. OF. blestre, fr. ON. blástr, a swelling, fr. blása, to blow. See blast and cp. bluster.' Klein routes it through Old Norse and mentions no Dutch form.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 20602 s.v. blister\", \"stance\": \"supports\", \"note\": \"'blis'tēr, n. [ME. blister; D. bluyster; OFr. blestre, a swelling.]' — the exact form Nourai prints, credited to Dutch.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 44302 s.v. blister\", \"stance\": \"supports\", \"note\": \"'[ME. blister; cp. OD. bluyster, blister. Allied to blast.]' (OD = Old Dutch).\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I pp. 156-157\", \"stance\": \"partial\", \"note\": \"'2. bhlei- aufblasen, schwellen, strotzen, überfließen, Erw. von bhel- ds. … dän. blegn(e) Bläschen (*blajjinōn), ags. blegen, engl. blain, mnd. bleine' — the root and the Germanic 'blister' family are there, but Pokorny lists blain, not blister, and no Dutch bluyster.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"blister\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English blister is first recorded c.1300 as ME blister, blester 'thin vesicle on the skin containing watery matter', and its membership in the *bʰlei- 'to blow, swell' family is agreed by everyone (Watkins: '[Pok. 2. bhlei- 156.]'). Only the immediate donor is unsettled, and that is the arrow drawn here: the older dictionaries (Webster's, Funk & Wagnalls) and Nourai take it from Dutch bluyster; Klein takes it from Old French blestre and ultimately Old Norse blástr 'a swelling' (to blása 'to blow'); Watkins and the AHD main entry say only 'the Germanic source of Old French blestre' / 'of Germanic origin'; Etymonline lists both possibilities and adds the Old Norse dative blæstri 'swelling' as a further candidate. The word is certainly a continental Germanic 'swelling' word taken into Middle English, and the -st- of blister points to a *blēs-tr- formation of the blast/blow type; whether it travelled by way of Dutch or by way of Norse-influenced Old French cannot be decided from the evidence, so the specific Dutch → English arrow is plausible rather than confirmed.\",\n          \"derivation_fa\": \"واژهٔ انگلیسیِ blister نخستین بار حدود ۱۳۰۰ میلادی به صورتِ blister/blester «آبله و تاولِ پوست» گواهی شده است و تعلقِ آن به خانوادهٔ *bʰlei- «باد کردن، آماسیدن» مورد اتفاق همه است (واتکینز: پوکورنی ص ۱۵۶). تنها سرچشمهٔ بی‌واسطهٔ آن روشن نیست و پیکانِ همین نمودار دربارهٔ همان است: فرهنگ‌های کهن‌ترِ انگلیسی و نورایی آن را از هلندیِ bluyster می‌گیرند، کلاین از فرانسویِ کهنِ blestre و در نهایت از نورسِ کهنِ blástr «آماس»، و AHD تنها به «خاستگاهِ ژرمنی» بسنده می‌کند. ساختِ ‑st‑ در واژه به قالبِ *blēs-tr- (از همان تبارِ blast و blow) اشاره دارد. داوری: با احتیاط پذیرفتنی است؛ اصلِ ریشه قطعی و حلقهٔ هلندی نامسلّم است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/blister\",\n            \"https://www.ahdictionary.com/word/search.html?q=blister\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. bhlei-: '2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhlei- 156.]' — the English word is indeed put under this root, but the immediate source is left as 'the Germanic source of Old French blestre', not Dutch. Watkins's English index likewise: 'BLISTER bhlei-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 5175 s.v. blister\", \"stance\": \"partial\", \"note\": \"'ME. blister, blester, fr. OF. blestre, fr. ON. blástr, a swelling, fr. blása, to blow' — same root family, different immediate donor.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 20602 s.v. blister\", \"stance\": \"supports\", \"note\": \"'[ME. blister; D. bluyster; OFr. blestre, a swelling.]' — supports the chart's Dutch → English arrow.\"},\n            {\"src\": \"SKT\", \"where\": \"grep 'blister' / 'Blain' in SKT.txt\", \"stance\": \"partial\", \"note\": \"Skeat has 'Blain. (E.) See Blow (1)', i.e. he puts the blain/blister family under 'blow, swell'; his blister entry is not legible in the OCR of this scan.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-85.json > /dev/null && echo \"JSON OK\"",
 "description": "Write and validate page-85 verification JSON"
}
```


### [2026-09-05T06:37:20.925Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T06:37:28.123Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== FSD chlorophyll ==\"; grep -o -m2 \"chlorophyll.\\{0,300\\}\" FSD_vol1.txt | head -3\necho \"== DEV ==\"; grep -c \"chlorophylle\\|fluor\\|influenza\" DEV.txt",
 "description": "Verify FSD and DEV claims"
}
```


### [2026-09-05T06:37:29.804Z] TOOL RESULT

```
== FSD chlorophyll ==
chlorophylle,  <   Gr.  chldros  (see  chlor-)  +   phyllon,  leaf.j
chlorophyll  is  utilized to  a   small  extent  as  a   coloring  matter  in  cookery,  and  in  the manufacture  of  liqueurs.
== DEV ==
0
```


## [2026-09-05T06:37:36.757Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-85.json'\ns=open(p,encoding='utf-8').read()\nold='\"note\": \"grep \\'chlorophyll\\' in FSD_vol1.txt: entered as a botany/chemistry term formed from Greek chloros + phyllon, agreeing with Klein on the elements.\"'\nnew='\"note\": \"grep \\'chlorophyll\\' in FSD_vol1.txt: \\'chlorophylle, < Gr. chlōros (see chlor-) + phyllon, leaf\\' — Funk & Wagnalls gives the French form as the etymon and the same two Greek elements as Klein.\"'\nassert old in s, 'not found'\ns=s.replace(old,new)\nopen(p,'w',encoding='utf-8').write(s)\njson.load(open(p,encoding='utf-8'))\nprint('ok')\nEOF",
 "description": "Fix FSD quote in node 8"
}
```


### [2026-09-05T06:37:38.342Z] TOOL RESULT

```
ok
```


## [2026-09-05T06:37:41.805Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 tools/verify_check.py 85",
 "description": "Run verify_check for page 85"
}
```


### [2026-09-05T06:37:43.411Z] TOOL RESULT

```
nodes verified: 12/12
node verdicts: {'transcription_suspect': 1, 'confirmed': 7, 'plausible': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'not_checked': 2, 'partial': 3}
books consulted: {'supports': 21, 'partial': 6, 'silent': 6, 'contradicts': 1} | by book: {'KLN': 11, 'POK': 4, 'DEV': 2, 'MON': 2, 'BQT': 2, 'ARY': 2, 'WLD': 2, 'FSD': 2, 'SKT': 2, 'WEB': 2, 'LAT': 1, 'SYN': 1, 'AHD': 1}
```


## [2026-09-05T06:38:04.259Z] AGENT

Page 85 (book p. 55) verified — `data/verification/page-85.json`, `verify_check.py 85` shows 0 PROBLEM lines (12/12 nodes).

**Counts:** root 1 confirmed · nodes: 7 confirmed, 4 plausible, 1 transcription_suspect · ref checks 8 supports / 3 partial / 2 not_checked · 34 book consultations (POK, WLD, AHD, SYN, KLN, SKT, WEB, FSD, LAT, MON, BQT, ARY, DEV).

**Root** *Bhel, Bhelgh, Bhlei, Bhleu* "to swell, blow, thrive, grow, bloom, overflow" — confirmed. Nourai's four headwords and his five Pokorny pages (120, 122, 125, 156, 158) match one-to-one the lemmas 3. bhel-, 4. bhel-, bhelgh-, 2. bhlei-, bhleu-; Watkins cites exactly the same five page numbers. Walde-Pokorny II 176-177/182/210/213 agrees.

**Flagged items**
- `transcription_suspect` — #1 Latin, item **fluere-ëscent** "showing a flow": not a possible Latin word (-escent is the French/English shape of -ēscēns). `error_in: "book"` — the printed page (verified against the rendered PNG, copied to `sources/refs/ocr/BOOK/85.png`) shows exactly this. Real chain: L. *fluor* "a flowing" → 17th-c. mineral name fluor/fluorspar → Stokes's *fluorescence* (1852). The other four Latin items are genuine (with *in-fluentia* medieval, not classical).
- `plausible` — #3 Persian: فلوئور and فلورسانت are correctly from French, but آنفلوآنزا is Italian *influenza* → French → Persian; the chart's Latin→French arrow skips the Italian stage (Klein: "influenza, n. — It., lit. influence"). Mo'in tags all three [فر.].
- `plausible` — #5 Greek: φύλλον is genuine, but *xlôros-phullon* is not an attested Ancient Greek compound, only the model for the 1817 French coinage.
- `plausible` — #11 Dutch *bluyster* / #12 English *blister*: the root (*bʰlei-*, Pok. 156) is certain, the donor is not. Klein derives blister from OF *blestre* < ON *blástr*; Watkins says only "the Germanic source of Old French blestre". Nourai's Dutch route is however printed verbatim in Webster's ("[ME. blister; D. bluyster; OFr. blestre]") and Funk & Wagnalls ("cp. OD. bluyster"), so it is an older respectable opinion, not an invention.
- Also noted (not a verdict change): *folium*'s assignment to *bʰel-* is disputed — Driessen/de Vaan prefer *dʰelh₁-* "be green"; Buck already recorded the doubt in 1949.

**Extraction errors for the owner: none.** The JSON matches the printed page word for word, including the Persian script and the Middle Dutch note; the page's second heading "Bhelgh → see root: Bhel" is a redirect and correctly absent from the data.

**Not accessible:** ROE:65,66 (Claiborne, lending-only) and VOP:251 (Moshiri, no scan anywhere); MON's 6-vol. page numbers (97, 386, 2573, 3030) could not be paged to since the digitised Mo'in on disk is a different edition — entries themselves confirmed via abadis.ir and the local OCR. Ten web pages archived via `fetch_source.py`.
