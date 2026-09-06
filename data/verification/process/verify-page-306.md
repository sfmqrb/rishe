# Verification process log — verify-page-306


## [2026-09-06T22:57:18.725Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 306 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-306.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-306.json. Write /home/sfmqrb/git/rishe/data/verification/page-306.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 306` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:57:20.324Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:57:21.036Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:57:21.049Z] TOOL RESULT

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


## [2026-09-06T22:57:21.349Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-306.txt"
}
```


### [2026-09-06T22:57:21.363Z] TOOL RESULT

```
1	=== PDF page 306 (book page 276) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Leig : to leap, jump  (refs POK:667)
4	#1 (parent #0) [Persian] refs=POK:667; MON:86; BQT:59 | âlîzîdan «آلیزیدن» : to jump around ; âlîz «آلیز» : a "jumping" horse | extra: آلیختن ، آلیزدن ، آلیزش
5	#2 (parent #0) [Germanic] refs=POK:667 | laik : to jump
6	  #3 (parent #2) [English] refs=None | lark : a carefree adventure
7	--- entry 1 ---
8	ROOT [Indo-European] Leigh 1 : to lick  (refs POK:668)
9	#1 (parent #0) [Avestan] refs=POK:668; KLN:886; SYN:267 | leiš, raěz, rěh : to lick
10	  #2 (parent #1) [Sogdian] refs=SOD:348 | rys : to lick
11	  #3 (parent #1) [Persian] refs=BQT:1895, HRN:212; FFD:76 | lîsîdan «لیسیدن» : to lick ; lîštan «لیشتن» : to lick | extra: لِشتن
12	#4 (parent #0) [Germanic] refs=AHD | likkon : to lick
13	  #5 (parent #4) [English] refs=None | lick
14	
```


## [2026-09-06T22:57:26.900Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-306.json && echo \"=== refs_online keys ===\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','MON','BQT','SOD','HRN','FFD','KLN','SYN','AHD','WLD','IEC','BRT','PHD','NYB','HUB','CHEUNG','ARY','SKT','FSD','WEB','MON5']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:400])\n    else: print(k,'MISSING')\n\""
}
```


## [2026-09-06T22:57:26.927Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120"
}
```


### [2026-09-06T22:57:28.858Z] TOOL RESULT

```
{
  "pdf_page": 306,
  "book_page": 276,
  "entries": [
    {
      "root": {
        "name": "Leig",
        "lang": "Indo-European",
        "refs": "POK:667",
        "gloss": "to leap, jump"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:667; MON:86; BQT:59",
          "words": [
            {"translit": "âlîzîdan", "gloss": "to jump around", "script": "آلیزیدن"},
            {"translit": "âlîz", "gloss": "a \"jumping\" horse", "script": "آلیز"}
          ],
          "script_extra": "آلیختن ، آلیزدن ، آلیزش",
          "note": null,
          "quote": {"text": "نفس چون سیر گشت بستیزد - توسن آسا بهر سو آلیزد", "poet": "Sarâj-ed-Dîn"}
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "POK:667",
          "words": [
            {"translit": "laik", "gloss": "to jump", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "lark", "gloss": "a carefree adventure", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Leigh 1",
        "lang": "Indo-European",
        "refs": "POK:668",
        "gloss": "to lick"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:668; KLN:886; SYN:267",
          "words": [
            {"translit": "leiš, raěz, rěh", "gloss": "to lick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:348",
          "words": [
            {"translit": "rys", "gloss": "to lick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1895, HRN:212; FFD:76",
          "words": [
            {"translit": "lîsîdan", "gloss": "to lick", "script": "لیسیدن"},
            {"translit": "lîštan", "gloss": "to lick", "script": "لیشتن"}
          ],
          "script_extra": "لِشتن",
          "note": null,
          "quote": {"text": "لشتند آستانت بزرگان و مهتران - چون یوز پیر لشته بلب کاسهٔ پنیر", "poet": "Sŭzanî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "likkon", "gloss": "to lick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "lick", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== refs_online keys ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
MON5 MISSING
```


### [2026-09-06T22:57:28.890Z] TOOL RESULT

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


## [2026-09-06T22:57:33.838Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','FFD','BQT','MON','SYN','KLN','AHD','WLD','IEC','BRT','HRN','HUB','PHD','NYB','SKT','ARY','CHEUNG']:\n    if k in d: print('==',k, json.dumps(d[k],ensure_ascii=False,indent=1))\n\" 2>&1 | head -200"
}
```


### [2026-09-06T22:57:35.888Z] TOOL RESULT

```
== POK {
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
== SOD {
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
== FFD {
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).",
 "covers_etymology": true,
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"
}
== BQT {
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
== MON {
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
== SYN {
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
== KLN {
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
== AHD {
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
== WLD {
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
== IEC {
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
}
== BRT {
 "title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)",
 "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/altiranischeswr00bartgoog",
```


## [2026-09-06T22:57:39.561Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full leig / leigh lemma ===\"\ngrep -n \"lemma: lei\" POK_full.txt | head -40\necho \"=== POK_02 leaf for p.667 (leaf = p - 344 = 323) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==324' POK_02.txt | head -80"
}
```


### [2026-09-06T22:57:41.432Z] TOOL RESULT

```
=== POK_full leig / leigh lemma ===
42283:liver. Old High German libera, lebaraio gr. kxua^oo, 'fat' (see Root / lemma: leip-1\ to 
54371:Root/ lemma: leid-{*lehud-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
56516:Root/ lemma: leih-1, lehk- 
56595:Root / lemma: leih-4 
=== POK_02 leaf for p.667 (leaf = p - 344 = 323) ===
ehm^  (lajiz-),   leira  [Haizön)
schwach.  Fem.  ,lehmiger  Strand'
und  apr.  layso  f.  {Haisa)  , Letten,  Ton,  Tonerde';  in  ders.  Bed.  von einer  (^-Erw.  apr.  laydis  ,Lehm*  und  alb.  leth  , feuchter  Ton*;
lit.  laistau,  -yti  ,verkleben,  mit  Lehm  oder  Kalk  verschmieren',  vgl. auch  ai.  lindu-  , schleimig,  schlüpfrig'
663
2.  als  Bezeichnung  schleimiger  Fische:
o-r.  hvevg  , Schleimfisch',  ahd.  slio,  ags.  slliv,  sleo  , Schleie',  lit.  lynas, lett.  Unis,  apr.  Unis  , Schleie',  russ.  linb  usw.  ds. ;
3.  als  Bezeichnung  des  , (schleimig)  Glatten'  :  gr.  XeTog  , glatt'  :  lat.  levis (^leiuis)  ,glatt',  gr.  liTÖg  , glatt,  schlicht',  Xiröq  und  Ug,  -xög  ,glattes  Tuch', Uoafi  Tthqa  , glatter  Fels' ;  llaTtog,  att.  llacpog  ,glatt,  gerieben'  sind  unklar ; lat.  li'fna  , Feile'  wohl  aus  *(s)li-mä  oder  *{s)lei-mä  (vgl.  ahd.  sUm  ,Schleim^, slmen  , glatt  machen,  blank  schleifen',  auch  gr.  Xel(.ia^  , Schnecke');
4.  mit  anlautendem  sl-:
kelt.  *sli-m-no-  , glitschig'  in  air.  slemun  ,glatt,  schlüpfrig*,  cymr.  llyfn , glatt,  eben',  acymr.  limnint  ,sie  glätten',  abret.  gur-limun  , glätten',  mbret. di'leffn  ,hart' ;
ags.  aisl.  nfries.  mnd.  mhd.  sllm  , Schleim'  (ahd.  slimen  , glätten');  vgl. aisl.  sly  n.  , schleimige  Wasserpflanzen';
lett.  slienas  f.  PI.  , Speichel'  (^sleinäs),  aksl.  sliny,  serb.  sUne  ,Rotz', russ.  slina  , Speichel';
5.  mit  Ic-Suffix:
gr.  Xelixa^  , nackte  Schnecke'  (daraus  lat.  llmäx  ds.)  =  russ.  slimdk  m. , Schnecke';  vgl.  apr.  slayx  m.,  lit.  sliekas  m.,  lett.  slieka  f.  ,Regenwurm' und  lett.  sliekas  f.  Fl.  , Speichel';  vielleicht  auch  lit.  seiles,  lett.  seilas  f. PI.  , Speichel'  (aus  ^sleiläs?).
6.  Erweiterungen:
(s)leib-  .schleimig,  schlüpfrig,  gleiten,  darüber  streichen,  glätten*.
Gr.  dXißqög  , schlüpfrig,  glatt'  Hes.,  dlißdc^ac  dlianeXv  Hes. ;
vielleicht  cymr.  llym  , scharf,  bret.  lemm  , scharf ;  Schneide  eines  Messers' (als  *slibsmös):,
ahd.  sllfan  ,gleiten,  ausglitschen;  glättend  schärfen',  nhd.  schleifen, mnd.  sllpen  , schleifen,  glatt  machen ;  intr.  schleichen',  ags.  tösllpan  , zer- gehen';  aisl.  sllpari  , Schleifer',  sleipr  , schlüpfrig,  glatt' =  mhd.  sleif  ds., ags.  slipor,  ahd.  sleffar  ds.,  norw.  slipra  , gleiten',  Kaus.  mnd.  slepen , schleppen,  schleifen'  (daraus  nhd.  schleppen),  ahd.  mhd.  sleif
```


## [2026-09-06T22:57:45.597Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 327 328 329 330; do echo \"###### NR=$n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_02.txt | head -60; done"
}
```


### [2026-09-06T22:57:47.275Z] TOOL RESULT

```
###### NR=327
ed.- dän.  Ortsnamenendung  -lösa,  -lese  und  (?)  abg.  les^  ,Wald' ;
abg.  leth,  Utijq  jesU  ,licet' ;  im  Balt.  nur  Diphthongformen :  lit.  lieta , Sache,  Angelegenheit'^  Lw.  aus  lett.  lieta  , Sache,  Zubehör',  und  wohl  auch lit.  Idima  , Glück',  laimüs  ,glückhaft',  laimeti  , gewinnen'.
WP.  II  394,  WH.  I  471,  Trautmann  157.
666  f
3.  le(i)-  , nachlassen*  (=  le{iy  ^gewähren',  s.  dort);  le-no-  ,matt,  sanft'.
a.  Wahrscheinlich  in  gr.  iXi-vv-w  ,bin  müßigj'raste' ;  lat.  letum  ,Tod,  Ver, nichtung'  (,*schlaff  dahinsinken',  vgl.  ,das  Leben  lassen');  lenis  , sanft  - mild'  (vielleicht  umgebildet  aus  *lenos  =)  lit.  Itnas  , ruhig,  zahm,  langsam*' lett.  l^ns  ds.,  abg.  Um  ,träge';  mit  anderen  Suffixen  lett.  le-lis  , schlaffer Mensch';  lets  , leicht,  wohlfeil',  lit.  Utas  ,blöde,  einfältig'  (ursprüngl.  ,schlaff'). lett.  laita  ,die  Faule'.
b.  Wurzclerweiterung  le[i]d-i  iQd-i gr.  Irjöstv  , träge,  müde  sein';
alb.  loth  , mache  müde^  lodhem  ,werde  müde'  (Hed-),  geg.  Iq,  tosk.  ll ,ich  lasse'  (*hd-nö)y  Partiz.  geg.  lane,  tosk.  lene  ,gelassen'  (*bdno-)j  "
lat.  lassus  ,laß,  matt,  müde,  abgespannt'  {Hdd-to-)]
got.  letan   (lailöt),  aisl.    lata,    ahd.  läzan,    as.  lätan,    ags.   lößtan  ,lassen, verlassen',   schwundstufig   got.    lats   ,träge',   aisl.    latr   ds.,   ahd.    laz  ,laß, träge,  matt,  spät'  (Superl.  lazzöst,  lezzist^  nhd.  —  aus  dem  Ndd.  —  letzter)^  ^, as.  lat , träge,  spät'  (Superl.  letisto,  lazto  , letzter',  ags.  Icet  (Superl.  Icetost,  engl.  - last)  ds. ;  Kausativ  Hatjan  ,lasse  machen,   hemmen'   in  got.   latjan  ,träge  1 machen,  aufhalten',  ahd.  lezzen  , hemmen,  aufhalten,  beschädigen,  verletzen^  ^ reflex.  ,sich  letzen  (=  sich  wobei  aufhalten),  sich  gütlich  tun',  usw.,  ags.  ~ lettan,  ne.  to   let  , hindern' ;   aisl.  Igskr  , weich,  schlaff',  mnd.  lasch,  wfries. lask  , leicht,  dünn'  (germ.  *latsktoa-);
leid-  in  lit.  leidziu,  leidmi,  leisti  ,lasse',  ablaut.  paläidas  ,lose*,  paldida ,Zügellosigkeit,    Hurerei',    lydeti    ,geleiten',    Ididoti    ,bestatten' ;    lett.  laist jlassen',  verkürzter  Imper.  lai,  Permissivpartikel  (auch  lit.  dial.  lai,  apr.  ' -lai  in  boü-lai  ,wäre').
WP.  II  394  f.,  WH.  I  767  f.,  782  f.,  787,  Trautmann  154,  Endzelin  Lett. Gr.  §  694.
leibh-  ,leben^
S.  unter  1.  leip-  ^beschmierend
leid-  , spielen,  scherzen,  necken'.
Gr.  ll^ef  Ttal^sL,  Vitovai'  nal^ovat  Hes.  (aus  *Xivöto),  vgl.  iLvöeaS-ai' änilXäad-ai  Hes.) ;  Xoidoqog  , schimpfend',  loidoqeo)  , schmähe,  schelte'  (vgl. zur  Bed.  mhd.  schimpf  , Scherz,  Kurzweil':  nhd.  Schimpf);
la
###### NR=328
t.  lüdö,  -ere,  lüsl,  -sum  , spielen,  zum  besten  halten',  lüdus  (alt  loidos) ,Spiel';
vielleicht  mir.  laidid  (*loid-)  ,treibt  an,  besingt'.
WP.  II  402,  WH.  I  829  f.
667
leJg'  ^^^  leik-  besser  oleig-jk-  .dürftige  elend;,;    Krankheit,  schlechtes Ergehend
1.  Gr.  Xoiyög  , Verderben,  Unheil,  Untergang,  Tod^,  lotyiog  , verderblich, tödlichS'  öXlyog  ,klein';
alb.  lig  ,böse,  mager',  lige  ,Bosheit,  ÜbeP;
lit.  ligä  jKrankheit^,  lett.  liga  ,schwerere  Krankheit,  Seuche^,  ablaut.  lit. päliegis  m.  ds.;
2.  arm.  ai/tat  ,arm,  dürftig,  wenig,  knapp';  Subst.  , armer  Bettler^,  aUat- anam  ,bin  oder  werde  arm;  nehme  ab,  werde  schwach'  (*ali]t-  aus  idg. *oUJco- ;  demnach  ist  auch  das  d-  von  gr.  dXlyog  wohl  alt,  die  Wz.  also  als *{o)leig-lk-  anzusetzen);  air.  llach  ,elend,  unglücklich';  apr.  licuts  ,klein'.
WP.  II  398,  Trautmann  161 ;  wohl  zu  2.  lei-.
2.  {l^ig-)f  ^^S-  ;Gestalt;  von  der  Gestalt  jemandes,  ähnlich  oder  gleich'.
Got.  leih  n.  ,Leib,  Fleisch,  Leiche',  aisl.  llk  ,Leib,  Körper,  Leiche', ags.  llc  ds.,  as.  Ukj  ahd.  llh  (Gen.  llhJiij  fem.)  ,Körpergestalt,  Aussehen, Leib,  Leiche';  got.  galeiks  ,gleich',  aisl.  gllki-j  likr  ,gleich,  gleich  gut',  ags. gelle,  as.  gilik,  ahd.  gilih,  nhd.  gleich  (, dieselbe  Gestalt  habend'),  got. hiUiks  ,wie  beschaffen,  welcher'  usw. ;  got.  leikan,  galeikan  ,gefallen', aisl.  lika  ds.,  ags.  lician  (engl,  like  ,gern  haben'),  as.  llkön  ds.,  ahd. liehen  ,ds.,  gleich  sein,  angemessen  sein',  aisl.  llkr  ,passend',  llkna  ,ver- zeihen'  (,sich  vergleichen') ;
lit.  lyg,  lygus  ,gleich',  lygti  ,gleichen',  lett.  llgt  , übereinkommen',  lldzis ,gleich',  apr.  pollgu  Adv.  ,gleich',  llgint  ,richten'  (rechtlich)  =  altlit.  liginti , Gericht  halten',  lit.  lyginti  ,vergleichen,  gleichmachen  (rechtlich)'.
WP.  II  398  f.,  Endzelin  Lett.  Gr.  508  f.
3.  leig-f  loig-  , hüpfen,  beben;  beben  machen'.
Ai.  rijati  ,macht  hüpfen,  läßt  erbeben',  rijate  ,hüpft,  bebt',  rejdyati ,macht  erzittern,  beben';
npers.  älextan  ,springen,  ausschlagen  (vom  Pferde)',  kurd.  be-lezium ,tanze',  llzim  , spiele';
gr.  sXsU^o),  iXsXi^a  ,mache  erzittern,  schwinge',  eX£XL[*y]-x-^(ov  ,Erder- schütterer'  (dazu  wohl  auch  Xiy-  ,worauf  losstürmen'  in  XiyaLvet  ,stürmt los',  Xlya '  Tax^cog) ;
air.  loig  m.  ,Kalb',  bret.  dial.  lu-e  ds..  lu  , Dummkopf,  lächerlich';  cymr. PL  lloi  ,Kälber'  (Sg.  llo)  ist  ir.  Lw. ;
got.  laikan  {lailaik)  ,hüpfen,  springen',  hi-laikan  ,verspotten',  laiks ,Tanz',  anord.  leika  {lek)  ,spielen,  züngeln  (Flamme),  fechten,  jemandem mits
###### NR=329
pielen',  leikr  ,Spiel,  Spott',  ags.  läcan  ,sich  schnell  bewegen,  spielen, fechten',  läc  ,Spiel,  Kampf,  Beute,  Gabe',  mhd.   leichen  ,hüpfen,  foppen'.
668  •
ahd.  leihj  leich  ^Spiel,  Melodie,  Gesang;  Leich',  nlid.  dial.  laich  ^lusug venerius',  mnd.  lek  ,das  Laichen,  Laich',  nhd.  Laich  (aus  dem  Germ, entl.  abg.  UH  ^Reigen');
lit.  Idigyti  ,wild  umherlaufen',  Verbalnomen  Idigymas.
WP.  II  399,  Trautmann  148.  T.
4,  lelg-,  leig-  ,binden'.
Alb.  lithj  Pass.  lidhem  ,binde,  verbinde,  gürte',  lidhe^  lidhe  ,Band, Fessel;  Garbenband,  Bruchband';
lat.  ligö,  -äre  ,binden,  zusammenbinden',  obligatio  ,Verpflichtung' ;  lietor ,Träger  der  fasces']
mnd.  lik  ,Band',  daraus  aisl.  llk  ,Saumtau',  ablautend  wohl  mhd.  geleich ,artus,  Gelenk^;  ^"^
mit  g:  klr.  polyhaty  sa  ,sich  verbinden',  zalyhdty  ,in  Bande   schlagen,  - schnüren,  anknüpfen,  in  Beschlag  nehmen',  nalyhaty  ,Zaum,  Schlinge  an-  . legen,    fesseln',   vermutlich   auch   lit.    laigönas   ,Bruder   der   Frau',    wozu Xoiycüvrlav '  cpqaTQiav  lies. ;  "f;
hitt.  li-in-ga-in  Akk.  ,Eid',  li-ik-zi  (lenkzi)  ,schwört',    3.  PI.  li-in-kdn-zi,  ""
WP.  II  400,  WH.  I  800.  :;
leigh-,  sleigh-  ,lecken';  Präsens  leigh-mi.
Ai.  Udhi,  vMhi,  lihati  .leckt',  lehd-  m.  ,Lecker',  av.  3.  PL  raezaite  ,sie lecken',  np.  Ustan  ,lecken';
arm.  lizum,  lizem,  lizanem  ,lecke' ;
gr.  Idxu)  ,lecke',  Isixrjv  ,Flechte,  Ausschlag',  li%voq  ,lecker,  naschhaft', liXVBvu)  ,belecke',  Xixavoq  , Zeigefinger'  (,Lecker') ;  ^,
lat.   lingö,   -ere,   linxl  , lecken',   ligurrio,    ligürio  ,lecke'  (vgl.  formal  air.  ^ ligur,  Corm.  ,Zuuge'),  ligula  {*ligh-la)  ,LöffeP,  wie  auch  mir.   liag,  cymr. llioy,  bret.  loa,   corn.  lo  ,Löffel'  (Heigha),  air.  ligim  ,lecke',  cymr.   Uyfu, llyw  ,lecken'   (/  ist   Hiatuseinschub,   Pedersen   KG.  I    100),    mbret.    leat ,lecken';  air.  ligur  , Zunge';
got.  bilaigön  ,belecken' ;  ablaut.  geminiert  ags.  liccian,  ahd.  lecchön,  as. likkon  ,lecken';
daneben  mit  anlaut.  s- :  aisl.  sleikja  ,lecken',  mhd.  slecken  , schlecken, naschen';  das  s-  hat  vielleicht  in  der  variierenden  Schallvorstellung  des Leckens  seinen  Grund,  wie  vielleicht  westfäl.  slappern  neben  sonstigem *lab-  ,lecken';
lit.  leziii,  lieszti  , lecken',  iter.  laizaü,  -yti  ds.,  hz-lizos  f.  PL  ,Zwischen- raum  zwischen  den  Zähnen',  lett.  laischa  ,Leckermaul^ ;  |
abg.  li^q,  lizati  ,lecken',  skr.  läznem  (*hzng)  ds.
WP.  II  400  f.,  WH.  I  800  f..  Wissmann,  Nom.  postverb.  183  f.,  Traut- mann 155  f.
I
669
leik-  ;feilbieten;  feilschen,  handelnd
Lat.  liceö,  -Bre  ,iei\  sein,  zum  Verkauf
###### NR=330
  ausgeboten  werden^,  so  und  so hoch  geschätzt  werden^,  licet  ,qs  ist  erlaubf^,  Uceor,  -eri  ,auf  etwas  bieten^, polliceri  ^(darbieten,  sich  anheischig  machen)  versprechen^,  osk.  Ukitud, Ucitud  ,licetö%'
lett.  liJcstu,  llku,  llkt  ^handelseins  werden^,  sallkt  ,ds.,  einen  Handel  ab- schließen^, nuolikums  ^Vertrag'.
WP.  II  395,  WH.  1  797.
2.  leik-  , biegend
S.  oben  S.  309  E,  wozu  ferner  der  kelt.(?)  FIN  Licus  ,Lech^  (Bayern), die  lit.  FIN  Lieke  und  Leikä,  lit.  liekna  , sumpfige  Wiese^,  lett.  liekna  ds. ; vgl.  illyr.  Epi-licus  portus,  FIN  Pacco-licus  (Bruttium),  mod.  FIN  Lika (Kroatien).
leik^-  .lassen,  zurück-,  übriglassen^;  imperfektiv  leik^ö,  perfektiv  li-n-k^ö (ursprüngl.  athematisch);  Aor.  3.  Sg.  e-lik^-e^  Ferf.  le-loik^-e; Partiz.  Perf.  lik'^tö-S',  loik'^o-s  ,übrig^;  eti-loik'Ao-s  , Überbleibsel  •, loik^-no-s-  ^Überlassung^
Ai.  rindkti  (3.  PI.  rificanti)  ,läßt,  läßt  los,  räumt  ein^,  riktd-  ,leer,  frei von  etwas*^,  ricydte  ,wird  befreit  von  etwas,  geht  verlustig^,  rtku-  ,unergiebig^, atirika-  ra.  ,Überbleibsel^,  rsknas-  n.  , ererbter  Besitz,  Eigentum^  =  av. raexnah-  ,Gut,  Schatz,  ErbteiP,  -irinaxti  ,räumt,  läßt  frei^,  npers.  rextan ,ausgießen^,  gurexten  ,entbehren^;
Sivm.' lHanem  , lasse',  Aor.  eliJc  =  eXme,  lHanim  ,werde  verlassen,  werde matt' ;
gr.  Isifttü  ,lasse^  verlasse',  Xoiftög  , übrig',  Xiy.n&vo}  ,lasse',  XLaaw^sv '  idaco- (.isv  Hes.  (wohl  mit  l,  aus  *linkVi-io)',  Xeli.if.ia  n.  »Überbleibsel',  Xelxpavov  ds. :
lat.  linquö,  -ere,  Uqul  {*loik^ai,  vgl.  ai.  ririca,  gr.  XeXoiTca,  und  bes. got.  laih),  relictus  , zurücklassen',  relicuos  ,übrig',-
air.  leicid  ,läßt,  läßt  los',  nach  Strachan  (BB.  20,  31)  aus  *link^-,  mit dem  Vokalismus  des  Fut.  und  Aor.  *ZeiÄ;^-s-;
got.  leihan,  aisl.  Ijä^  ahd.  llhan^  ags.  leon  , leihen'  (*?eiÄ;^ö),  Partiz.  as. ahd.  farliwan  , verliehen',  aisl.  leiga  , mieten',  aisl.  Zä?i,  ags.  l^n,  ahd.  lehan , geliehenes  Gut,  Lehen'  (*laihna-  =  ai.  rsknas-,  vgl.  zum  n-Formans  auch cech.  liknavy):
lit.  liekü,  alt  lieknii  (umgebildet  aus  Hink-mi),  Infin.  likti  , lassen'  und ,bleiben',  liktas  ,übrig',  liekas  , übrig  gelassen',  alt  , elfter',  pälaikas  , Übrig- gebliebenes', laXkas  , bestimmte  Zeit,  Frist'  (lett.  laiks  ,Zeit'),  laikau^  -yti , behalten  (übrig  behalten)*,  lykius  ,Rest',  a^ZyHs  , Arbeitspause';  lett.  Vieks (=  liekas)  , überzählig,  überflüssig;  unecht;  unpaar';  apr.  pollnka  ,er bleibt',  auch  altlit.  palinkt  ds. ;
670
abg.  oHUH  ^Überbleibsel^  (:  ai.  atirika-),  öech.  liknovati  se  ^sich  weigern scheuen^   zaudern,   fliehen^,    liknavy  ^fahrlässig"^   (s.  oben),  mit
```


## [2026-09-06T22:58:03.568Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 lick ===\"\ngrep -n \"^lick\" KLN_1966.txt | head -10\necho \"=== KLN leaf for p.886: floor(886/2)+12 = 455 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==456' KLN_1966.txt | grep -n -i -A12 \"^lick\" | head -40\necho \"=== SYN.txt LICK ===\"\ngrep -n \"LICK\" SYN.txt | head -20\necho \"=== AHD watkins leigh ===\"\ngrep -n -i \"^leigh\\|^leig-\\|^leig\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T22:58:05.264Z] TOOL RESULT

```
=== KLN 1966 lick ===
21366:lick.
=== KLN leaf for p.886: floor(886/2)+12 = 455 ===
=== SYN.txt LICK ===
6882:4.59 LICK (vb.)
=== AHD watkins leigh ===
```


## [2026-09-06T22:58:09.098Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN lick context ===\"\nsed -n '21360,21390p' KLN_1966.txt\necho \"=== which leaf is line 21366? ===\"\npython3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:21365])\nprint('leaf(0-based)=',t[:idx].count('\\f'))\nEOF\necho \"=== SYN 4.59 LICK ===\"\nsed -n '6875,6920p' SYN.txt"
}
```


### [2026-09-06T22:58:10.718Z] TOOL RESULT

```
=== KLN lick context ===
leave,  intr.  v.,  to  put  forth  leaves,  to  leaf.  —  ME.
leven,  fr.  lef,  ‘leaf’.  See  leaf, leaved,  adj.,  having  leaves.  —  Formed  fr.  prec. word  with  suff.  -ed.
leaven,  n.  — -  ME.  levain,  levein,  fr.  F.  levain,  fr. VL.  *levamen,  ‘something  that  raises’  (classical L.  levamen,  means  ‘alleviation,  mitigation’),  fr. levare,  ‘to  lift,  raise;  to  lighten,  alleviate,  miti¬ gate’,  fr.  levis,  ‘light’.  See  level  and  cp.  relieve. Derivatives :  leaven,  tr.  v.,  leaven-ing,  n. leban,  lebban,  also  leben,  n.,  coagulated  sour  milk (an  Arab  beverage).  —  VArab.  laban,  leben, ‘sour  milk’,  fr.  Arab,  laban,  ‘milk’,  which  is  rel. to  Heb.  labhan,  ‘white’,  lebhdnah,  poetic  name for  the  moon  (lit.  ‘the  white  one’),  libhonah, Aram. -Syr.  fbhuntd,  Arab,  luban,  ‘frankincense’ (Gk.  Xtpavo;,  Xipavorc.;,  ‘frankincense’,  are Sem.  loan  words),  Heb.  Lfbhanon,  Akkad.  Lab- nanu,  Aram.  Libhnan,  Arab.  Lubnan,  ‘Mount Lebanon’,  lit.  ‘the  white  one’;  so  called  from the  whiteness  of  its  cliffs.  Cp.  olibanum  and  the first  element  in  benzoin.
Lecanium,  n.,  a  genus  of  scale  insects  ( entomolo¬ gy ).  —  ModL.,  fr.  Gk.  Xsxaviov,  dimin.  of Xexccv7],  ‘dish,  pan’.  Seelekane  and  cp.  Lecidea. lecanomancy,  n.,  divination  by  the  inspection  of water  in  a  basin.  —  Compounded  of  Gk.  Xs- xctvrj,  ‘dish,  pan’,  and  [iavreia,  ‘oracle,  divina¬ tion’,  See  lekane  and  -mancy.
Lechea,  n.,  a  genus  of  plants,  the  pinweed  (hot.) —  ModL.,  named  after  the  Swedish  botanist Johan  Leche  (1704-64).
lecher,  n.,  lecherous,  lewd.  —  ME.  lechour.  fr. OF.  lecheur  (F.  lecheur),  ‘libertine’,  lit.  ‘licker’, fr.  techier  (F.  lecher),  ‘to  lick’,  fr.  Frankish  *lik- kon,  which  is  rel.  to  OHG.  leckdn,  ‘to  lick’.  See
lick.
lecherous,  adj.,  lustful.  —  ME.,  fr.  MF.  leche- reus,  fr.  OF.,  fr.  lecheur,  ‘libertine’.  See  prec. word  and  -ous  and  cp.  lickerish.
Derivatives:  lecherous-ly,  adv.,  lecherous-ness,  n. lechery,  n.,  lust,  lewdness. —  ME.  lecherie,  fr.  OF. lecherie,  fr.  lecheur,  ‘libertine’.  See  lecher  and  -y (representing  OF.  -ie).
Lecidea,  n.,  a  genus  of  crustacean  lichens  (but.)  — ModL.,  fr.  Gk.  Xexi;,  gen.  XsxiSo;,  dimin.  of Xsxo;,  ‘dish’.  See  lekane  and  cp.  Lecanium. lecithin,  n.,  a  waxy  substance  found  in  tissues  of the  brain  and  the  nerves  (biochem.)  —  Coined  by Gobley  fr.  Gk.  Xexi&o?,  ‘the  yolk  of  an  egg", which  is  of  uncertain,  prob.  foreign,  origin,  and chem.  suff.  -in.
lecontite,  n.,  a  hydrous  sodium  ammonium  po¬ tassium  sulfate  (mineral.)  —  Named  after  the American  scientist  John  L.  Le  Conte,  its  dis¬ coverer.  For  the  ending  see  subst.  suff.  -ite. lectern,  n.,  a  reading  desk  in  a  church.  - —  ME. lectorne,  refashioned  (after  ML.  lectdrinum,  lec- trinum)  fr.  ME.  lettorne,  let  Iron,  fr.  OF.  letrin, fr.  ML.  lectdrinum,  lectrinum,  fr.  Late  L.  lectrum, ‘reading  desk,  pulpit’,  fr.  L.  lectus,  pp.  of  legere, ‘to  read’.  See  lecture.
lection,  n.,  a  reading,  a  lesson.  —  L.  lectio,  gen. -onis,  ‘a  reading’,  fr.  lectus,  pp.  of  legere,  ‘to read’.  See  lecture  and  -ion  and  cp.  lesson,  which is  a  doublet  of  lection.
lectionary,  n.,  a  list  of  lections.  —  Ecclesiastic  L. lectionarium,  fr.  L.  lectio,  gen  .-onis,  ‘a  reading’. See  prec.  word  and  subst.  suff.  -ary.
lector,  n.,  a  reader,  esp.  in  a  church  or  in  a  uni¬ versity.  —  Late  L.  lector,  ‘reader’,  fr.  L.  lectus, pp.  of  legere.  See  lecture  and  agential  suff.  -or.
lectorate,  n.,  the  office  of  a  lector.  —  ML.  lecto- ratus,  fr.  Late  L.  lector.  See  prec.  word  and  subst. suff.  -ate.
lecture,  n.  —  ME.,  fr.  MF.  (=  F.)  lecture,  fr. ML.  lectura,  fr.  L.  lectus,  pp.  of  legere,  ‘to  gath¬ er,  collect;  to  pick  out,  choose;  to  read,  recite’ (prop,  ‘to  choose  words’),  fr.  I.-E.  base  *leg-,  ‘to pick  together,  gather,  collect’,  whence  also  Gk. X£yEiv,  ‘to  pick  out,  choose;  to  say,  tell,  speak, declare’  (prop,  ‘to  choose  words’),  (for
*Xey-cu;),  ‘speech,  diction’,  Xoyo;,  ‘word, speech,  discourse,  account,  thought,  reason’. Alb.  mb-l'ed,  ‘I  gather,  collect,  harvest’.  Cp. alexia,  Alogians,  analects,  analogue,  analogy, apologetic,  apologize,  apologue,  apology,  coil, colleague,  collect,  college,  curiologic,  Decalog, dialect,  dialogue,  diligent,  duologue,  dyslogy, eclectic,  eclogue,  elect,  election,  elegant,  eligible, elite,  epilogue,  eulogy,  florilegium,  intellect,  in¬ telligent,  lectern,  lection,  legal,  legation,  legend, legible,  legion,  legislation,  legitimate,  legume, lesson,  lexicon,  ligneous,  logic,  logos,  monologue, neglect,  negligee,  paralogy,  predilection,  prole¬ gomena,  prologue,  recollect,  religion,  sacrilege, select,  sortilege,  syllogism,  tetralogy,  trilogy.  For the  ending  of  lecture  see  suff.  -ure.
Derivatives:  lecture,  intr.  and  tr.  v.,  lectur-er,  n., lecture-ship,  n.
lecythus,  n.,  a  tall,  slender  vase  with  a  single handle  (Greek  antiq.)  —  Late  L.,  fr.  Gk.  X)]xu- Uo<;,  ‘oil  flask’,  which  is  of  unknown  origin, led,  past  tense  and  pp.  of  lead.  —  ME.  ledde,  fr.
OE.  hedde,  fr.  OE.  liedan,  ‘to  lead'.  See  lead,  v. Leda,  n.,  mother  of  Castor  and  Pollux,  Helen, and  Clytemnestra  (Greek  mythol.)  —  L.  Leda, fr.  Gk.  AvjSot,  which  prob.  derives  fr.  Lycian Lada,  and  lit.  means  ‘wife,  woman’.  Sheis  identi¬ cal  with  Latona  and  Leto  (qq.v.) lederite,  n.,  a  variety  of  sphene  (mineral.)  — Named  after  Baron  Louis  von  Lederer,  Austri¬ an  Consul  at  New  York,  in  recognition  of  his interest  in  mineralogy.  For  the  ending  see  subst. suff.  -ite.
ledge,  n.,  a  shelf  projecting  from  a  wall;  a  ridge  of rocks.  —  ME.  legge,  ‘support,  bar’,  prob.  relat¬ ed  to  ME.  leggen,  ‘to  lay’.  See  lay,  ‘to  place', and  cp.  next  word.
Derivative:  ledg-y,  adj.
ledger,  n.,  an  account  book.  —  ME.  legger,  fr. leggen,  ‘to  lay’;  cp.  the  ME.  var.  lidger,  which prob.  derives  fr.  liggen,  ‘to  lie’.  ME.  legger,  lid¬ ger  orig.  meant  ‘a  book  that  lies  permanently  in
ledger
876
tsu
the  same  place’.  See  lay,  ‘to  place",  lie,  ‘to  re¬ cline’,  and  cp.  prec.  word.
ledger,  adj.,  stationery  —  From  the  stem  of  ME. leggen,  ‘to  lay',  fr.  OE.  lecgan.  See  ledger,  n.
Ledum,  n.,  a  genus  of  plants,  the  Labrador  tea ( bot .)  —  ModL.,  fr.  Gk.  XvjSov,  the  plant  Cistus Cyprius.  See  ladanum.
lee,  n.,  1)  shelter;  2)  the  side  of  a  ship  turned away  from  the  wind.  —  ME.  lee,  ‘shelter’,  fr. OE.  hleo  (gen.  hleowes),  ‘shelter,  protection’,  rel. to  OS.  hleo,  ON.  hie,  Dan.  lx,  Swed.  la,  Du.  lij, ‘lee’,  and  to  ON.  hly,  ‘shelter,  warmth’,  hlyr, hlser,  ‘warm,  mild’,  MLG.,  Du.  lauw,  MDu.  laeu, OHG.  lao  (inflected  lower),  MHG.  la,  Idwes,  G. lau,  ‘tepid’;  prob.  fr.  I.-E.  *kleu-,  enlargement of  base  *kel~,  ‘warm’,  whence  L.  calere,  ‘to  be warm’.  See  caldron  and  cp.  lew,  luke,  ‘lukewarm’ . Derivative:  lee,  adj.
leech,  n.,  1)  physician  {archaic)',  2)  a  blood  suck¬ ing  worm.  —  ME.  leche,  fr.  OE.  lice,  ‘physi¬ cian  ;  leech’,  rel.  to  ON.  heknir,  OS.  laki,  OFris. letza,  OHG.  lahhi,  lachi,  Goth,  lekeis,  ‘physi¬ cian’,  prob.  meaning  orig.  ‘magician’,  and  cogn. with  OIr.  Haig,  ‘charmer,  exorcist,  physician’.
=== which leaf is line 21366? ===
leaf(0-based)= 470
=== SYN 4.59 LICK ===
DY; BODILY FUNCTIONS AND CONDITIONS 267
ypaw ‘gnaw, eat’, etc. Stokes 118; re- jected by Walde-P. 1.658).
W. cnot, etym.? Perh. : MIr. cndim ‘snaw, chew’, Grk. xvi ‘scrape’, etc. (Stokes. KZ 41.385, Walde-P. 1.392, both without W. cnot).
Br. danta, fr. dant ‘tooth’ (4.27).
4. Goth. beitan, etc., general Gmc. : Lat. findere, Skt. bhid- ‘split’, IE *bheid-. Walde-P. 2.138.
5. Lith. kqsti, kandu (kandis sb.), Lett. kuost, ChSl. *kqsati, late kusati, Boh. kousati, Pol. kasaé, Russ. kusat’ : Grk. xv5wv ‘tooth on a hunting spear’, xvedaé “pin, pivot’, prob. fr. an extension of the root in Grk. xvfy ‘scrape’, etc. Walde-P. 1.392 f. Berneker 601.
6. ChSl. grystz, SCr. gristi (Boh. hryztt, Pol. gryzé also ‘gnaw’ as mostly Russ. gryzt’) : Lith. grauzti, Arm. krcem ‘onaw’, Grk. Bpixw ‘gnash, grind the teeth’. Walde-P. 1.697 f. Berneker 359.
4.59 LICK (vb.)
Grk,  delxw Goth. -laigin NG Yreldeo ON sleikja Lat. —lingere Dan. — slikke . leccare Sw. slicka % lécher OE liccian Sp. lamer ME _slicke Rum. linge NE lick I. ligim Du. —_likken ue lightm OHG _ leccon Br uh u, yw MHG lecken * ‘pat NHG _lecken
ad of the words for ‘lick’ belong to oy as group, pointing to an IE of this Meaning. The others are
ae with words for ‘lip’ or ‘ap up’. iby, leigh-. Walde-P. 2.400. Er- s . 552, Walde-H. 1.806 urk Aelxo, NG rr bi
YNcldw fr, exreixw (yd » Tescue’, deriv, of EkNUTOS}
Lith.  laizyti (liezti) Lett. laizit
ChSl. lzatt
SCr.  lizati
Boh.  lizatz
Pol. lizaé
Russ.  lizat’
Skt. lih-
Ay. raéz-
ligim, NIr. lighim, W. llyfu, Uyw (non- etym. f; Pedersen 1.100); Goth.-laigon (in bi-laigon émidetxev), OE liccian, ME licke, NE lick, Du. likken, OHG leccén, MHG, NHG lecken; Lith. lezti, iter. laiZytz, Lett. laizit; ChSl. lizatz, etc., general Slavic; Skt. lih-, rih-, Av. raéz-; Arm. lizum, lizanem.
Here also prob. ON sletkja, MLG slicken (> Dan. slikke, Sw. slicka), late MHG slecken, NHG schlecken ‘eat
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
268 SELECTED INDO-EUROPEAN SYNONYMS
daintily’, fr. a parallel root form with initial s-. Falk-Torp 1063.
Here also It. leccare, Fr. lécher, either as deriv. of a VLat. *lgicare intensive to
- lingere, or else fr. the Gmc., OHG leccon,
etc. REW 5027. Gamillscheg 555. 2. Sp. lamer, Port. lamber fr. Lat.
lambere ‘lap up, lick up’ : OF l
apian OHG laffan, Grk. darrw ‘lap’. Walde-p.
2.384. Ernout-M. 519f. REW 4865,
3. Br. lipat, deriv. of borrowing fr, Fr. lippe ‘(thick) lower lip’, lUippée ‘mouthful’, ete. Henry 187,
4.61 SLEEP (vb.; sb.)
Grk.  xafebdw, xotpdopac; Goth. slépan; sléps Lith, miegoti; miegas
ixvos ON sofa; svefn Lett.  mieguot; miegs NG Koodpae (-Gyar); Dan. — sove; sdun ChSl.  stipati; stint
iavos Sw. sova; sémn SCr.  spavati; 8an, spavanje Lat. dormire; somnus OE sl@pan, swefan; sl@p, Boh. spat; spant, spdnek It. dormire; sonno swefn Pol. spac; sen, spanie Fy. dormir; sommeil ME slepe; slepe Russ. spat’; son, span'e Sp. dormir; suefio NE sleep; sleep Skt. svap-, dra-; svapna-, Rum. dormi; somn Du. zlapen; zlaap nidra- Ir. con-tulim (foaim); OHG | slafan; slaf Av. x’ap-; x*afna-
stian, cotlud MHG  slafen; slaf, swep NIr. _codlaim; codladh, NHG - schlafen; schlaf
suan W. cysgu, huno; hun,
cwsg Br. kousket, huni; kousk,
hun
Many of the words for ‘sleep’ belong to an inherited group reflecting an IE verbal root and an established substan- tive form for ‘sleep’. Others are cognate with words meaning ‘lie, rest, quiet, slack, blink’. Verb and noun are gener- ally parallel, but not in Greek or Latin, and both forms are listed. The verbal forms listed are those that mean ‘be asleep’, beside which there are distinc- tive types for ‘fall asleep’ and ‘put to sleep’. Several of the nouns are used also for ‘dream’ (4.62).
1. IE *swep-, sb. *swep-no-s, *swop- no-s, *sup-no-s. Walde-P. 2.523f. Er- nout-M. 954f. Falk-Torp 1109 f.
ON sofa, Dan. sove, Sw. sove, OF swe- fan; ChSI. sitipati, ete., general Slavic verbs; Skt. svap-, Av. x*ap-; beside forms for ‘put to sleep’, as Lat. sopire, ON svefja, OE swebban, OHG antsweb-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
jan, -swebban, MHG entsweben; or ‘fall asleep’, as ON sofna, ChSI. uszinati, ete.
```


## [2026-09-06T22:58:18.410Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lick,  tr\\|^lick,\\|lick, tr\" KLN_1966.txt | head\necho \"---- search 'liccian' ----\"\ngrep -n \"liccian\" KLN_1966.txt | head"
}
```


### [2026-09-06T22:58:18.473Z] TOOL RESULT

```
21660:Derivatives:  licit-ly,  adv.,  licit-ness,  n. lick,  tr.  and  intr.  v.  —  ME.  licken,  fr.  OE.  liccian, rel.  to  OS.  likkon,  Du.  likken,  OHG.  lecchon, MHG,  G.  lecken,  ‘to  lick’,  Goth,  bi-laigon,  ‘to lick  at’  (F.  lecher,  ‘to  lick’,  is  a  Teut.  loan  word), from  the  I.-E.  imitative  base  *leigh-,  whence  also OI.  ledht,  redid,  also  (a  later  form)  lihati,  ‘he licks’,  Avestic  raez-,  ‘to  lick’.  Arm.  lizum, lizem,  lizanem,  ‘I  lick’,  lakem,  of  s.m.,  Gk.  Xei- X«v,  ‘to  lick’,  Xev/tjv,  ‘lichen’(lit.  ‘licker’),  Xi/veu- elv,  ‘to  lick  at’,  Xi/avoq  (scil.  SaxxuXoi;),  ‘fore¬ finger’  (lit.  dicker’),  L.  lingere,  ‘to  lick’,  Lith. lieiiii,  liezti,  OSlav.  HIq,  lizati,  ‘to  lick’,  OIr.  li- gim,  ‘I  lick’,  MBret.  leaf,  ‘to  lick’,  W.  llyfu,  llyv, ‘to  lick’,  Mir.  liag,  W.  llwy,  ‘spoon’.  Cp. — with initial  s — ON.  sleikja,  MHG.  sleeken,  G. schlecken,  ‘to  lick’.  Cp.  electuary,  lecher,  lichen, ligule,  linctus,  lingula.
35536:sley,  n.,  weaver's  reed.  —  See  slay,  n. slice,  n.  —  ME.  seliee,  slice,  fr.  OF.  esclice, ‘splinter’  (whence  F.  eclisse),  back  formation  fr. esclicier,  ‘to  split,  lit’,  fr.  Frankish  sliyyan,  ‘to split’,  which  is  rel.  to  OHG.  slifan,  of  s.m.  See slit  and  cp.  slate,  ‘piece  of  rock’, slice,  tr.  and  intr.  v.  —  ME.  slicen,  fr.  MF.  escli¬ cier,  ‘to  splinter’,  fr.  OF.,  fr.  esclice.  See  slice,  n. slick,  adj.  —  ME.  slike,  ‘smooth’,  prob.  fr.  ON. slikr,  ‘smooth’,  which  is  rel.  to  OE.  slician,  ‘to make  smooth’,  OHG.  slihhan,  MHG.  slichen,  G. schleichen,  ‘to  creep,  crawl,  sneak’,  MHG.  slich, Du.  slijk,  ‘mud,  mire’,  fr.  I.-E.  base  *sleig-,  ‘to smooth,  glide,  be  muddy',  whence  also  Gk. XivSr,v,  ‘grazing  the  surface’,  XlySo;,  XiySot, ‘grindstone,  mortar’.  Base  *sleig-  is  an  enlarge¬ ment  of  base  *(s)lei-,  whence  lime,  ‘sticky  sub¬ stance’,  loam  and  slime  (qq.v.)  Cp.  sleek,  slight. Derivatives :  slick,  n.,  slick-ly,  adv.,  slick-ness,  n. slick,  tr.  v.  —  ME.  sliken,  fr.  OE.  slician,  ‘to  make smooth’.  See  slick,  adj.
---- search 'liccian' ----
21660:Derivatives:  licit-ly,  adv.,  licit-ness,  n. lick,  tr.  and  intr.  v.  —  ME.  licken,  fr.  OE.  liccian, rel.  to  OS.  likkon,  Du.  likken,  OHG.  lecchon, MHG,  G.  lecken,  ‘to  lick’,  Goth,  bi-laigon,  ‘to lick  at’  (F.  lecher,  ‘to  lick’,  is  a  Teut.  loan  word), from  the  I.-E.  imitative  base  *leigh-,  whence  also OI.  ledht,  redid,  also  (a  later  form)  lihati,  ‘he licks’,  Avestic  raez-,  ‘to  lick’.  Arm.  lizum, lizem,  lizanem,  ‘I  lick’,  lakem,  of  s.m.,  Gk.  Xei- X«v,  ‘to  lick’,  Xev/tjv,  ‘lichen’(lit.  ‘licker’),  Xi/veu- elv,  ‘to  lick  at’,  Xi/avoq  (scil.  SaxxuXoi;),  ‘fore¬ finger’  (lit.  dicker’),  L.  lingere,  ‘to  lick’,  Lith. lieiiii,  liezti,  OSlav.  HIq,  lizati,  ‘to  lick’,  OIr.  li- gim,  ‘I  lick’,  MBret.  leaf,  ‘to  lick’,  W.  llyfu,  llyv, ‘to  lick’,  Mir.  liag,  W.  llwy,  ‘spoon’.  Cp. — with initial  s — ON.  sleikja,  MHG.  sleeken,  G. schlecken,  ‘to  lick’.  Cp.  electuary,  lecher,  lichen, ligule,  linctus,  lingula.
```


## [2026-09-06T22:58:24.217Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:21659])\nprint('leaf(0-based)=',t[:idx].count('\\f'))\nEOF\nawk 'BEGIN{RS=\"\\f\"} NR==483' KLN_1966.txt | grep -n \"^[0-9][0-9][0-9]$\\|88[0-9]\\|licit\" | head -20\necho \"--- raw around ---\"\nsed -n '21640,21665p' KLN_1966.txt | grep -o \"88[0-9]\\|lichen\" | head"
}
```


### [2026-09-06T22:58:26.105Z] TOOL RESULT

```
leaf(0-based)= 476
11:897
--- raw around ---
lichen
lichen
lichen
lichen
lichen
lichen
lichen
lichen
lichen
lichen
```


## [2026-09-06T22:58:31.724Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==477' KLN_1966.txt | grep -nE \"^[0-9]{3}$|^[0-9]{3}[^0-9]\" | head -20\necho \"=== HRN 212 (leaf = printed+21 => 233) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==234' HRN.txt | head -70"
}
```


### [2026-09-06T22:58:33.586Z] TOOL RESULT

```
=== HRN 212 (leaf = printed+21 => 233) ===
— 212 —
949. (feU ^Welt\
aw. ga^^ya- 'irdisch'; phlv. getlk^).
Mot savant; die den Lautgesetzen entsprechende
neupersische Form ist gehän (No. 951).
950. ges, gesü 'Locken, öelock'.
aw. ga^sa- 'in zwei oder drei (sc. Locken) geord-
netes Haar (ZBÖL); phlv. g^s^ arm. syr. LW. ges,
ü^: *Haar\
oss. d. yesä, t. qts *Borste*.
951. gehän *Welt\ arab. LW. ßhan, jehän^),
aw. gae^ä' (gaf.&anqm); phlv. gehän, vergl. tahn.
r:} (de La gar de, Semitica I, 59).
L.
952. lfrJ)e, läwe 'Schmeichelei, Bitte', lähidefi,, laf 'Prahlerei*.
skr. l^lap' (ai. rap-), Idpati 'schwatzen', vergl.
ud + lap' 'liebkosen .
siyn. I6w-am, sar. lew-am 'reden, sprechen, sagc^n';
af/. laudal 'sagen, erzählen'.
953. leh 'Lippe*, vergl. lefj^ leföe.
Käs. lew; kauk.-bergjüd. low,
phlv. lap; lat. labium; nhd. lAppe (vgl. Kluge,
Etymolog. Wörterbuch s. v.).
kurd. liw 'Lippe'; bei. lap (216); wa;^. law^ lafc,
sangl. law,
954. listen 'lecken*, Praes. les-em, lestden.
Kää. Z. bSles,
phlv. listan, l(i)stan (AV.); ap. l/^*lais- {V^leig^h- + ,<?);
vergl. ai. [/'reh-^ rehmi, skr. teÄ-, lehnii 'ich lecke*;
arm. lizeniy lizum etc. (H. No. 123); wa/. li/'am.
^) Die Syrer schreiben nach Mitteilung des Herrn Prof. Nöldeke
gethih, und so ist also wohl auch im Pehlevl get(Ofi zu lesen. Np. geil
geht aber jedenfalls auf ein, dann allerdings falsches, phlv. ge Ik zurück.
Ist get(i)h etwa von st(Oh beeinflusst?
*) Eine persische Etymologie (von jehlden) siehe Vis und Rämln,
Seite 83 Vers 17.
```


## [2026-09-06T22:58:47.384Z] TOOL CALL #13: Bash

```json
{
 "command": "pdftoppm -f 306 -l 306 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg306 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T22:58:49.389Z] TOOL RESULT

```
total 127632
drwx------ 7 sfmqrb sfmqrb    12288 Sep  6 18:58 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   122418 Sep  6 18:55 pg303hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89589 Sep  6 18:52 pg303.png
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


## [2026-09-06T22:58:52.780Z] TOOL CALL #14: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg306.png"
}
```


### [2026-09-06T22:58:53.108Z] TOOL RESULT

```

```


## [2026-09-06T22:58:53.105Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:59:02.944Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 آلیز ===\"\ngrep -n \"آليز\\|آلیز\\|آليخ\\|آلیخ\" BQT_v1_pages.txt | head -20\necho \"=== MON parts آلیز ===\"\ngrep -n \"آليزيدن\\|آلیزیدن\\|آليز \\|آلیز \" MON_part1.txt | head -10\necho \"=== BQT v3 لیسیدن / لشتن ===\"\ngrep -n \"ليسيدن\\|لیسیدن\" incoming/BQT/BQT_v3_pages.txt | head -10\ngrep -n \"ليشتن\\|لیشتن\\|لشتن\" incoming/BQT/BQT_v3_pages.txt | head -10"
}
```


### [2026-09-06T22:59:03.033Z] TOOL RESULT

```
=== BQT v1 آلیز ===
8675:۲ - مولف منتهی الارب در ترجمةٌ « تمییج » آرد : « برانگیختن نکه را برآلیز . »
8726:4 آلوه رد4 : آله. 0 آلیز دی و آلیزدی - جفته افکندن» جتتاگ‌اداختن :
8727:نش چون مب رکشت یستیزد ‏ نوسن‌آما بهرسو آلیزد . سراچالدین «لت‌طعه».آماره مات
12359:اسکیز است که برجمتن و آلیز انداختن ستور
13748:۴ - رك : آلیز. - در بهلوی 0 «نای۲۹۵». ۲ - در بارسی باستان 110 (رك: ایمه)
=== MON parts آلیز ===
4559:(مصل.) (البخت» آلیز د» خواهد آلیخت. 
4568:آلیزیدن: 2117-10 [- 9 (مسص‌ل.) 
12977:آلیز یدن. 
=== BQT v3 لیسیدن / لشتن ===
30463:‎ob‏ لیسیدن مادر ندارد و پوستش ‎ob‏ میشود ؛
51157:تماشا وتفرج باش - ویک ‎san Syl‏ لیسیدن برف رمین را : و بای هی بر
51168:‏۴ 27 لیشتن * لبیدن . از رس پارسی باستان ‎olishtanaiy « liz‏ = فارسی‌لشتن
```


## [2026-09-06T22:59:09.860Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndef leafof(path, lineno):\n    t=open(path,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    idx=sum(len(l)+1 for l in lines[:lineno-1])\n    return t[:idx].count('\\f')\nprint('BQT_v1 8726 leaf', leafof('BQT_v1_pages.txt',8726))\nprint('BQT_v1 8675 leaf', leafof('BQT_v1_pages.txt',8675))\nEOF\necho \"--- context v1 ---\"\nsed -n '8715,8735p' BQT_v1_pages.txt\necho \"=== v3 pdf page tag near 51168 ===\"\nawk 'NR>=51100 && NR<=51175' incoming/BQT/BQT_v3_pages.txt | grep -n \"pdf page\" \nsed -n '51150,51180p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T22:59:11.718Z] TOOL RESULT

```
BQT_v1 8726 leaf 269
BQT_v1 8675 leaf 268
--- context v1 ---
رودک یگفت :
از فرارانی که خشعامار کرد زان نهان می‌مردرا بدارکرد . »
واستقصاء را درمعنیآمار( باراء بی‌نفطه) بامتسقاء بدیل کرده‌اند (ازافادات علامه‌دهشنا).
آمارگر - پهلوی 21087887 ( محاسب ) مرکب از : آعار + کر یسوند
اصاف . در قارسنامة ابن‌البلخی (ص ۷ ) ابرا تمارفر ( - ایران - آمار ۳- کر ) آمده »
و آمروز مامور احصائبه را گویند
بقیه از صفحً ۸ه
مالیدن با عالیده شدن چیزی بچیزی چنانکه اثری از آن در دومین بماند اعم ازیكك وسوخشاه
و تر » چون آب و خالك و خون واك و مش و زهر وقیر دخوی وپلیدی و جزآن , واین ضل
لازم ومتمدی آبد :
حرآنگ هکه توشنه کیتی بخون بالودی این خنجرآبگون فردوسی «لفت‌طمه».
4 آلوه رد4 : آله. 0 آلیز دی و آلیزدی - جفته افکندن» جتتاگ‌اداختن :
نش چون مب رکشت یستیزد ‏ نوسن‌آما بهرسو آلیزد . سراچالدین «لت‌طعه».آماره مات
] مارم ۱ بروژن و معثی آواره - آموخته است ۵ . #
وییعنی آعار است کهمرض استقا - ونهایت تفحص
.و تس - و ساب - و تشبم باشد ,
]ماس ؟ ‏ بسکون مين ی قطه »
بمعنی ورم باشد که برآمدگی است در انا خواء
با درد باشد خواه بی‌درد .
]ماه ۴ ه پروزن تا گاه . بمعنی آحلي
است که ورم و برآمدگی اعضا باشد .
=== v3 pdf page tag near 51168 ===
13:[pdf page 691]
47:[pdf page 692]
شش ۳۹ ‎pe‏ اول وسکون ثانی,مخقف لك ۴ & بفتح اول وسکون انی‌وکاف»
لوش است که لجن باشد و آن کل و لايه نيد" | پمعنی پاره باشد که لك ‎LS‏ بسنی پاره پاره -
و ماه است که در ته تالابها و بن حوضها بهم و بمعنی شبتم هم‌آمده است و ‎OT‏ رطوبتی باشد

‎aa‏ حواکه ی ز زه نشیند و مانند
‎S55 5 Prt}‏ . در برروی ژمین و سبزه نشیند و
ن = بفتح اول بروزن ‎ES‏ » بمعنی ف زمین را سفید کند ۵ ؛ و باين ‎gine‏ یک
تماشا وتفرج باش - ویک ‎san Syl‏ لیسیدن برف رمین را : و بای هی بر

‏بعنی زبان برچیزی مالیدن ۴ . او ‎Ht ele‏

‏۸ سح لوش : 1
صاف باشد زلال دولت تو تبره شد آب دشمتانت ز لش .
‎cle on‏ جامی > جهالگیری * .

‏۴ - لش بفتح اول لاش ۳ لاشه بمعنی جیفه » مردار ؛ جسد پیروح - کشته و پوست
‎WT‏ و کوسفند وامثالآن - سخت بکاره » تثبل - بیمار » بی‌فیرت « لفت نامه » .

‏۴ 27 لیشتن * لبیدن . از رس پارسی باستان ‎olishtanaiy « liz‏ = فارسی‌لشتن
زمان ‎laizdmiy Je‏ ۵ فارسی 162810 5 ( نظیر نوشتن : ‎(ays‏ 163810 پدید آمده
«هوبشمان ۹۵5 , پهلوی ‎lishtan‏ , 1)(5420 , ارمنی ‎lixam,;, . lizum , lizem‏
رك : اسشق ‎Sef‏ . در اراك ( سلطانآباد ) ‎leshtan‏ > مکی‌نژاد » :

‏لعتند آستانت بزرگان ومپتران چون بوز پیراشته ‎Ly‏ نیر .
سوزنی سمرفندی « جپانگیری >

‎ae ۴‏ (هم) 9 - ظ , مصحف > بشکه » (ه.م.) یشک .

‎sae‏ - بقتح اول وسوم , معرب‌آن عسکر « داثرةالمعارف امیلام *قلعه » از اينکه تشک
به + عسکر» تعریب شده بعضی حدس زده‌اند که « ش » اصلی نیست . عسکی عربی در حفبقت از
کلمه‌ای ‎olaskar ost‏ با ‎cashkar‏ ناشی شده. انجمن آرای ناصری لشکر را از « لشکه ©
```


## [2026-09-06T22:59:30.586Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==270' BQT_v1_pages.txt | tail -30\necho \"###### line 13748 context (footnote ref: آلیز)\"\nsed -n '13740,13755p' BQT_v1_pages.txt\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:13747])\nprint('leaf',t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-06T22:59:32.515Z] TOOL RESULT

```
ونجسی باشد - وبمعنی حساب هم‌هست چهآعاره
گیر محاسب وحساي کیزنده را کول ویدشی
استفصا و تبم‌هم بنظی آعده است٩‏ هه
۱ - باين معتی در دزفولی 6 کاشفری (1 : ۵۳) آماچ را درلغات نکی‌بمعنی
هدف وثشانه آورده وبدیهی‌است که دخیل است ر‌ در کتاب «اللیات‌النوائه والاستشهادات‌الستائه»
ننامده :
چونیر انداختی برروی دشمن
بر کند. نبرتو زآ نان خالد درآماچگاه
جنر رکن کاندر آ ماجش شتی. ممدیدلت‌نلمه».
بر ز کر ب رکنده‌پنداری باماج وکلند
سوزنی* لت نامد».
۴ آماج توازبلخ بود تابپنج آب پرتاب توازبلخ‌بود تابف‌طین. فرخی«لفت‌نامه».
۴ - «امیر (محمدین محمود غزنوی) . . .آواز داد . . . که او را تنپا برند؛ حلجب
کگفت ده .که همه فوم باوی خواهند رفت » وفرزندان بجمله آماده‌اند »که زشت بود باوی‌ایشان
را بردن.» «تاریخ بیهقی ٩۷۳‏ . ۵ .. < ابار پهلوی 2087 وآمار وهمار وشمار وشماره از
مصدر اوستابی 1718۴ «کانگا: فرهنك‌اوستا ۲۳۹۷ بممنی حساب ؛ اما بمعنی‌استسقاه » آماز (بازام)
صحیح است بمنی آعای؛ رك : خشعامار. درلفت فرس اسدی‌آمده (س۱۲۵) : «آعار. استفصلء بوده
رودک یگفت :
از فرارانی که خشعامار کرد زان نهان می‌مردرا بدارکرد . »
واستقصاء را درمعنیآمار( باراء بی‌نفطه) بامتسقاء بدیل کرده‌اند (ازافادات علامه‌دهشنا).
آمارگر - پهلوی 21087887 ( محاسب ) مرکب از : آعار + کر یسوند
اصاف . در قارسنامة ابن‌البلخی (ص ۷ ) ابرا تمارفر ( - ایران - آمار ۳- کر ) آمده »
و آمروز مامور احصائبه را گویند
بقیه از صفحً ۸ه
مالیدن با عالیده شدن چیزی بچیزی چنانکه اثری از آن در دومین بماند اعم ازیكك وسوخشاه
و تر » چون آب و خالك و خون واك و مش و زهر وقیر دخوی وپلیدی و جزآن , واین ضل
لازم ومتمدی آبد :
حرآنگ هکه توشنه کیتی بخون بالودی این خنجرآبگون فردوسی «لفت‌طمه».
4 آلوه رد4 : آله. 0 آلیز دی و آلیزدی - جفته افکندن» جتتاگ‌اداختن :
نش چون مب رکشت یستیزد ‏ نوسن‌آما بهرسو آلیزد . سراچالدین «لت‌طعه».
###### line 13748 context (footnote ref: آلیز)
حیاما خوانند .گرم و خشث اتتخ دردوم ؛بول
را براند .
امف » بفتح اول وسکون‌ثانی ودال‌ابجد .
بمعنی هنگام و زمان و موسم باشد .٩*‏
(۱) چك : سیوم .
۱ - پهلوی 2۱۷600 و من-وب‌بدان 21۷60016 داونوالا ۲۸۹» دراوستا 20۳۷۵۳
بمعنی تندمند , دارای تندی وئیزی. ۳ رگ : آله. ۴ - ۱1188 , ایلیا جاوززا۴
«جفری ٩۷‏ - ۹۸ پیفمبر بنی اسرائیل معاصرآحاب پادشاهاسراثبل «قاموی مقدس ۵-۱4۶ ۱4*.
۴ - رك : آلیز. - در بهلوی 0 «نای۲۹۵». ۲ - در بارسی باستان 110 (رك: ایمه)
دریبهلوی 1۳ «اونوالا ۷4 ۷ - واء‌شب‌هتی این‌شب. بای الوم والسنة واللبل. ۸ برله:
آماره. * - بونانی 2۳70670008 «اشتینگای». ۰ حز 871)2(0, 2170 »بهلوی
(06)۷ ۱۵ بمعئی همیشد . الی الاید . <ونکی ۰۰۹۸ در عربی عمعنی غابت دمنتهی شنی واجل
( برهان قاطع ۳۵ )
افمت:ج2
اهر ) - بقتح اول و انی و رای بی‌نقطه
بالف کشید» » بلفتزندوپازند (۱) شراب‌انگوری
leaf 378
```


## [2026-09-06T22:59:43.095Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part1 4550-4575 ===\"\nsed -n '4550,4575p' MON_part1.txt\necho \"=== MON 12970-12985 ===\"\nsed -n '12970,12985p' MON_part1.txt"
}
```


### [2026-09-06T22:59:43.165Z] TOOL RESULT

```
=== MON part1 4550-4575 ===
جفتکك» جفته» لکد پرانیدن ستور با دو بای 


از عقب. حست) جستن. رم » رمندن. 


الب وان ح«عَله [ ال نان - الیز بدن ] 


(مصل.) (البخت» آلیز د» خواهد آلیخت. 


بالیز آلیزنده» آليخته» آلیزش) آلیزبدن. 


الیزش: 2117-8 (امص. آلیزدن و آلبزبدن) 
عمل الرندن؛ جفتک برانی 

آلیزیدن: 2117-10 [- 9 (مسص‌ل.) 
(آلبز بده السزد» خواهد ال تنل بیالیز» 


آلیرنده» آليزیده آلیزش) جفتک زدن» 


جفته انداختن. 
=== MON 12970-12985 ===
اسکیزه: (0-)متاه [- سکیز] (امص.) 
جفته انداختن ستورء برجستن و لگد انداختن 
چارپایان. جست و خیز کردن. 
اسکیزیدن: 7-7[»ج» [- سکیزبدن ] 
(مسصل.) (اسکیزید» اسکیزد» خواهد 
اسکیز بد. بتکم اسکیز نده» اسکیزبده؛ 
اسکیزه) جفته انداختن» جفتک انداختن» 
آلیز یدن. 

کال #-21و5ه [- سگالش] (حامص.) 
اند یشه» فک تفکر» خبال. 

اسگ_سذار؛ 65-2 [ - اسگذار ‌ 
اسبگذار؟] (امر.) برید و پیکی که منزل به 
منزل فرود آید و اسب خود را عوض کند. 
کیسه و خريطةٌ حاوی نامه‌های پیکث.
```


## [2026-09-06T22:59:50.347Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD grep rys / to lick ===\"\ngrep -n \"to lick\" SOD_pages.txt | head -20\necho \"---\"\ngrep -nE \"^ *[0-9]{3,5} +ry\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T22:59:52.078Z] TOOL RESULT

```
=== SOD grep rys / to lick ===
---
28158:8470 ry»k B                                                     8480 rywsn'yrfimn B
28166:                                                                8481 rywsn^rSmncyk       S
28172:                                                                8482 rywsny^Ch) B                           jLi^p^jj
28173:8472 ry'nt B, M, S                      ^i .x-^-jl
28179:8473 ry'nttVk B                                                        Dhy. 148, 219; Frag. Len.; W-Lii
28193:8484 rywsny wn'y B                                 J'j^jj
28197:8485 ryzy M                               ^^jlys,                          ©inf. rnflc>)y =»rnp-, rpny
28202:8486 ryzycyk      M                                                         Dhu. 146
28209:8487 ryzyn'k S                       (•»csr
28217:8488 ryzynyn'k °* ryzyn*k
28563:                                                                8630 rym'ys B                                        j^^
28578:                                                                8633 rymywVk    B                         jy*-*x£ < j^-cil^
28592:                                                                8636 rymny(y)  M =» rymn'k
28594:8625 ryph MD =» ryph
28595:                                                                8638 rync'q   C, M =» rync>k(k)
28599: 8639 rync'k =* ryncwk                                                VJ 51, 76; SCE 79
28600: 8640 rync}k(k) B, S              y_jcj^.f <S>f t4?>             8650 ryp5ph B                                      jj^o*k
28616:8641 rync>kkw S                                JL+iJ^f
28622:8642 rync'kstr S                                   J-&?/             saliva                                                aOf
28628:8643 ryncq skwn    M                                 \£*£
```


## [2026-09-06T22:59:57.922Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 414 415 416; do echo \"##### leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' SOD_pages.txt | head -50; done 2>&1 | head -120"
}
```


### [2026-09-06T22:59:59.687Z] TOOL RESULT

```
##### leaf 414
347

8612 rwz- C                   j^^Je* <o\ZjjjT <jsJ>-             8626 ryj M                                     rync'q
                                                                                                     (iij'J^^J^^^jjJ
                                                                      rez =»ryz, ryz
     roz
     (/o)desire, (/cOwish                                             desire, wish
     GMS 379; STii 1.78; C2, 94V12, 51V24; AVS 138                    GMS 66; BBB 538, 567, 585, 679 bH Sund. 1994,
                                                                        45.18
8613 rwzywn'y B                          alyj-x^^b.
     rozyone =*rwsywny                                           8627 ryj-    M                         J^l^y-i^bjjjl
     desirable, suitable                                              rez =*ryz-, ryz-
     BSTBL, Dhy. 215; GMS 1114; Lentz. STii p604                      (to)desire, (/o)be desirable
                                                                      BBB 605, 3sg. subj. rypt
8614 rwzny C                                          j^-'_^
     rozne ©pres. part.
     desiring                                                    8628 ryk B                   (& J <&j:J^->)<*ik <•*><* jj>
                                                                      rik ©<OP arika
      C2, 48V 18                                                      wicked

8615 rwzty> C                                       jjjT<J~-          VJ 1097; Sogdica. 4
     roztya ©f. n.; pi. rwztyt
     desire                                                     8629 rym B, M, C             ^ cS ^ ,,/lb .oiliT
                                                                     rem (rymh) ©Parth. MP rem
      C2, 51V29, 60R22, 61V28, 69V26 pi. 40R13                       dirt, dirty, impurity
8616 rwzy'kh    B                            J^Ij^'sjjI *J~*          BSTBL, Vim. 43, 72, 207, Dhu. 24, 37, 151, 153,
     rozyak ©MP rwzdyh*          ^'rwytky*                              240; Frag. Len. 93.9; BBB 583, 587; C2 gloss.
     wish, desire                                                       61R25
      TSP 2.344, 345; Hen. Texts. 719; Sogdica. p47.3
                                                                8630 rym'ys B                                        j^^
8617 rxmyh =» rxmy(y)                                                rimes, rymls ? (rymys)
8618 rxmy(y) M                                    *jAaJ>IiJ\          blame
     raxme (rxmyh) ^rym'k                                             TSP 7.103, 119; S W, IIJ 1976, 70
     rest, remainder                                            8631 rym'ys- B, S                               frfj*^
     BBB p65.530, 576, Sric                                          rimes, rymis ?
8619 rxn- C, S               j^b * jUl *y>- «, i&^cJSjr               0<?)blame
     raxn ©perf. rxndyr~ =*ryn-                                       TSP 2.340, 633, 652, 7.110 n pl73; Frag. Len.
     (/o)dare                                                          40.5, 8, 11; perf. rm*yStd}r-, TSP 2
     BSTi 134; C2, 25R3-4, 17V1, 2, 24V15, 56R19;               8632 rynVystk B                  J*j^*jj*<J*j^{s*z~>J£'
       MSP M34, 135; CII 1990 G8 n p69                               rimeste ?

8620 rxsynyt}yr-kyrd S                               JjjuCl           blameworthy, reprehensible
     (o)raxsinder-kird ©MP Hxyndrgyrd                                 BSTBL, Intox. 13
     Alexandria
                                                                8633 rymywVk    B                         jy*-*x£ < j^-cil^
      KG 359 pl89; Hen. JRAS 1944, 141 n 2                           rem-xware
8621 rxwsn-      S                                                   dirt-eater
     r(u)xusn ©nom. ob. -ny\ abl. -«* =»rwxsn-                       TSP 2.415
                                                       «j-J->
     Iight                                                      8634 rymh B ^ rym
##### leaf 415
                                                                                                                          348

  rync*k
 8639 rync'k =* ryncwk                                                VJ 51, 76; SCE 79
 8640 rync}k(k) B, S              y_jcj^.f <S>f t4?>             8650 ryp5ph B                                      jj^o*k
      rincak, rince (rync'q) ©<*r(a)nj; A v. rdnjyah                   ripa/o6P ©<Av. rapiOwa
        Khwar. rnc\ Khot. raysga; Pasht. rangai                        noon
        =>ryncyk                                                       BSTBL, Dhu. 909; GMS 293; Ben v. Et. Oss. 31 n;
       child, small, little                                              Bailey. Asica. 23
       TSP 3.198, 12.31, 35; VJ 950; SCE 24, 281, 316,          8651 ryph S                                    ^^J\ iy& ^
         399; BSTBL, Dhu. 79; MDiii pl28; MSP; STi;
                                                                       rep, ref (ryPh) ©<*rafya
         STii 4.45; C2, 69V17; rynck, BBB; TSP 16.34;                  defectivness
           rynckk, SCE 303; pi. -*, VJ 390, 1245; STii                 MDii p43.14; KG 555; Gersh. Advice.
^          1.83; KG 504; voc. -\ STi 31.6; rync, Frag. Len.     8652 RYPW       B, S                            (y) ^ < Jyt»
           14 V2; rynck "short" GMS 1241; Hen. Tales.                 Pewar, prewar (prywr) ©Idg. =»Pryywr
           482 n5; Gersh. AHM 215; Bailey. Prolexis. 182;
                                                                      ten thousand, myriad
           Mayrhofer. EWA     III, 31-32
                                                                      GMS 362; VJ pi 19; TSP; BSTBL pl30; SCE p69;
8641 rync>kkw S                                JL+iJ^f
     rincaku (ryncqw) ©<ryncwk                                          STii 9.14.15; RYPW -kyy Dhy. 329 "by
     small, light                                                       myriads" MDii p211; Frag. Len. 82 al6, 93.26
                                                                                                                >U«I
      MDii A- 10, 3; C2 p95.5, 48V5                             8653 ryr'kh M
                                                                     ri/erSk ©Past, lara-, Heb. rir
8642 rync'kstr S                                   J-&?/             saliva                                                aOf
                                                                                                               jS i jU*
     rincakstar =»ryncwkstr
     smaller                                                         Sogdica. 5.10
     MSP bl85                                                   8654 rys- B                                 t^J<jt,,ll,l
                                                                     res ©<*raiz% Av. raez-, Khot. rriys-, Yaghn. les
8643 ryncq skwn    M                                 \£*£
     rincak-(a)skon
     childhood                                                           )lick rysyt-
                                                                      (to©pL
                                                                      VJ 990; AVS 125
     GMS 635 n 2
                                                                8655 rysk S, M
8644 ryncqw       C =¥ rync*kkw
                                                                      ri/ese =^ryz}kh
8645 ryncwk     B                       •Jl^tS^J' «£*                 rice
     rincu/ak (rync'k)                                                Anc. Lett. 5.10 p33 n 9; Hen. Texts. 724 n 1;
     child, little, light
                                                                       Sogdica. 45.2b
     TSP 6.185, 198, 12.55; Hen. Texts. 733; Tales. 482         8656 rystr M, C                            j&£ tjS^/
           n 5; Gersh. AHM   215, <*ranjuka
                                                                      ri/estar ©<*rynckstr =»rync}k(k)
8646 ryncwkstr M                                     J<£r*            smaller, less, least
     rincuk-star =*rystr, ryncwk, rync'kstr                           W-Lii 547.6; BBB pl34; GMS 464, 1241, 1288;
##### leaf 416
                                                                                                               ryz^stny
 349

 8660 ryt                                     lSjj^j**         8671 ryys-    M                                (ukJ)d>J*j\
      ri/et (ryyt) ©Yaghn. rit ©ob. -y =»ryth                       res
      face                                                          OcOtear apart
      TSP 5.32, 12.18; Sogdica. 5.5; Hen. JRAS 1944,                Hen. JRAS 1944, 143.23; AVS 128
         143.19; GMS 29; KG 2327; Frag. Len. 33.4;             8672 ryyt    M =4 ryth
        W-Li b71; BBB b22; STii 2.10, 4.5; BSTi 150,
                                                               8673 ryz B, S                 (^j:J^->)J?*<jjJ <J-*lj>-
         165-6; C2, 55R22, 60R10, 68R27; MSP b29, 60,               rez (ryz) =»ryz, ryj
         ryt% TSP 8.107                                             wish, desire, demand
8661 ryt'ngm'ny M                                    jAju*          VJ 165, 54b, 883; SCE 30, 532; TSP 2.662, 733,
     ret-angmane (ryth'nkm'ny)                                        899, 901, 904; BSTBL pl30; MDii Nov. 5.9,
     face to face
                                                                      pl70; MSP bl41; STii 9.16, ryzK Vim. 112;
     BSTBL, Dhy. 189; GMS 1037 "openly"                               Hen. LW 99; TSP 2.109
```


## [2026-09-06T23:00:07.185Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\necho \"=== grep لیس / لیسیدن ===\"\ngrep -n \"ليسيدن\\|لیسیدن\\|ليسي\\|لیسی\" FFD_pages.txt FFD_pages_faseng.txt | head -20\necho \"=== printed 76 = pdf 81 -> \\f block 81 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==81' FFD_pages_faseng.txt | head -60"
}
```


### [2026-09-06T23:00:08.853Z] TOOL RESULT

```
=== grep لیس / لیسیدن ===
ugrep: warning: FFD_pages_faseng.txt: No such file or directory
196:۷ واو فارسی امروزء ۷انگلیسی
197:۷ واو عربی و ۷ انگلیسی
215:معادل انگلیسی برخی از اصطلاحات
2065:«لیسیدن).
2482:۹ 2 : (ريشه < لیسیدن + لشتن) ۷۶
=== printed 76 = pdf 81 ->  block 81 ===
awk: cannot open "FFD_pages_faseng.txt" (No such file or directory)
```


## [2026-09-06T23:00:12.476Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\nls\nsed -n '2055,2075p' FFD_pages.txt\necho \"=== 2475-2490 ===\"\nsed -n '2475,2492p' FFD_pages.txt\npython3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (2065,2482):\n    idx=sum(len(l)+1 for l in lines[:ln-1])\n    print(ln,'leaf(0-based)=',t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-06T23:00:14.095Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
بالیدن.

لرزیدن
لرزید < فارسی میانه 1272۵» مادةٌ ماضی جعلی و از مادةٌ مضارع ساخته شده است.
لرز + فارسی میاته 1372 + ایرانی باستان ۲۵۲2-۵*. برای 2 آرای.
[pdf page 81]
وا فعلهای قارسی دری
دا 2 لشت.
لشت « ایرانی باستان 715-1۵*. برای 1۵ -> آراست. 7:2* صورت اصلی کل* است. 7
َ پیش از ۲ به 5 بدل شده است. ریشهٌ 72* صورت ضعیف ريشةٌ 7۵2* است» به معنی
«لیسیدن).
لیس + ایرانی باستان 1۵12-2*. برای 2 -> آرای. «س» در «لیس» به جای 2 آمده است.
ماندن
ماند < فارسی میانه 13324 < ایرانی باستان ۳30-12:*. برای 1۵ -* آراست. ريشهٌ
به معنی «صبرکردن» است.
مان < فارسی میانه 832 < ایرانی باستان 038-8*. برای 2 آرای.
«ماندن» فارسی دری و 38420 فارسی میانه جانشین دو ريشةٌ ایرانی باستان
شده‌اند» یکی 337 به معنی «صبرکردن» و دیگر 8 ج 0039۵ 930۵ که اسم
است و در فارسی دری «مان» شده» در ایرانی باستان به عنوان مادهٌ جعلی و با معتی
«سکونت کردن» به کار برده شده است.
مانست-
=== 2475-2490 ===
40 ۱۴ ۱۷
[pdf page 95]
تچ فعلهای فارسی دری
:۳۱ 6 : (ريشه < ترک کردن) ۵۷ ۷۲
12 : ۴۱ ۵۷
۰ ۵2 : (ريشه - بافتن + رشتن) ۵۶
: داقسنادم: ۳۴۵ (ريشه < بافتن -ه رشتن
۹ 2 : (ريشه < لیسیدن + لشتن) ۷۶
۴۵
۱ 2رزه ۱ : ۵۶
۵۶۵
۱ هن : ۷۶
2 : ۴۵ استراحت کردن) ۲۵
0 (ريشه < استراحت کردن
14 ۴۴ (ر مه
8 1372-2: ۷۵
۴۳۵
8 ۵۶
2065 leaf(0-based)= 80
2482 leaf(0-based)= 94
```


## [2026-09-06T23:00:30.538Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT raez ===\"\ngrep -n \"raēz\\|raez\\|raöz\\|raez-\" BRT.txt | head -20\necho \"=== PHD lystn / listan ===\"\ngrep -n -i \"lis\\|lišt\\|lyst\" PHD.txt | head -20\necho \"=== CHEUNG raiz ===\"\ngrep -n -i \"raiz\\|\\*rai\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T23:00:30.612Z] TOOL RESULT

```
=== BRT raez ===
24794:•  j.  raez-  V.  'lecken,  leckend  verzehren*. Praes.   1  rau-.
=== PHD lystn / listan ===
9:First published 1971 Reprinted 1971 Reprinted (with corrections) 1986
13:THE need for even a short Pahlavi-English dictionary has been obvious for many years, particularly to would-be students of the language. The glossarial part of Professor H. S. Nyberg’s Manual of Pahlavi is still eagerly awaited, five years after the publication of Part I, although the ‘archaistic’ tradition of transcription followed therein is no longer universally acceptable. With the partial material at present available, every serious student still has to compile his own dictionary, a formidable task with Pahlavi and made more so by the plethora of different systems of transcription in print. The present dictionary, admittedly introducing yet another transcription, is intended first to relieve the stranger to Pahlavi of the necessity of covering what is now well-travelled ground—the commonest 4,000 simple words— without a unified map, and secondly to urge the practical value of this ‘Sasanian’ transcription for his journeying further. To have included etymologies and textual references would have changed the emphasis of the work, turning it from a map to a historical atlas-cum-gazetteer, besides retarding its appearance unduly. Such a complete dictionary of Pahlavi is nowhere within sight and must remain so until many more texts are adequately edited.
14:For his good counsel on what to include in the dictionary I am most grateful to my friend Dr. P. Gignoux of Paris, for without him many common words would have slipped through my net. Most of the labour of compiling the English index, which will surely be appreciated, was undertaken by my wife. The debt I owe to the teaching of the late Professor W. B. Henning, in connection with Pahlavi and all things Iranian, cannot be expressed in words.
19:ADDENDA ET CORRIGENDA DICTIONARY ENGLISH-PAHLAVI INDEX APPENDIX
24:ALMOST every published list of Pahlavi words contains a number of entries of doubtful nature, the uncertainty lying either in their form, their meaning, or even, occasionally, their very existence. The purpose of this dictionary is to provide the student with a representative vocabulary of Pahlavi in which such uncertain words have been reduced to a minimum and marked. It differs from its predecessors in that the Pahlavi words are given in a phonemic transcription representing, as far as it is deducible from the evidence, the pronunciation they would have had in the third century of our era, the period of the rise of the Sasanian empire. The reasons for this departure from the 'archaistic' tradi- tion of Pahlavi studies I have given elsewhere.! If one reason stands out it is that of practicality, as most corroborative evidence comes from this period.
29:been adopted, eclectically, and grateful acknowledgement is hereby made to all whose discoveries have been assimilated within. Nevertheless, I must retain responsibility for the choice as a whole and for readings and interpretations unclaimed or un- published elsewhere.
31:'The script of the Pahlavi books derives ultimately from that of the official Aramaic of the Achaemenian empire. In the course of time, however, a high degree of ambiguity has developed in the script. Table I shows the development of the letters from Imperial Aramaic (with the transliteration and names of letters commonly used by Semitists), through the distinct forms used in the Parthian and Persian inscriptions of the third century A.D., and the archaic manuscript forms of the Psalter fragment (about seventh century),! to those of the Zoroastrian books. In addition to the multiple values of the letters listed, some of them may represent combinations of letters in certain contexts, e.g. - or 35 for 3+».
59:The orthographic principles followed, in seemingly haphazard permutation, in the writing of Pahlavi, besides the ideographic, include the phonetic (within the limits of the alphabet), the his- torical, the pseudo-historical, and. others so indeterminable as scarcely to merit the name. The establishment of the original spelling of a word, therefore, very seldom reveals its pronuncia- tion. To determine this it is necessary to examine all the available comparative evidence.
60:Since the discovery of the Iranian material written in the near- phonetic Manichaean script it has become possible to establish a hypothetical phonemic system for Middle Persian and Parthian of the third century A.D. far more accurate than before, when only the remoter evidence of Old Iranian, New Persian, and loanwords in other languages (particularly Armenian) was available. A description of this phonemic system has been given in my article cited above. Within its terms all the entries in this dictionary are transcribed.
69:In seeking an unknown word, or one known only in another transcription, it may be necessary first to find it in the Pahlavi key. The English-Pahlavi index is intended to serve as an aid to memory, and for tracing synonyms, etc., but is emphatically not an English-Pahlavi dictionary.
76:(ii) verbal nouns formed from the present stems by the suffix -išn [-sn'] and their derivatives in -išnīg [-#yh'], -išnīh [-5nyh], which are all listed under the verb.
122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
156:Amend English-Pahlavi Index and Pahlavi Key accordingly.
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
248:bālist [b°lyst' | (M Bryst)] highest; summit; astr. exaltation. ~ih: highness, exaltedness. ~ig [-yk'] on high, exalted.
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
366:fréstádan / frestidan, frést- [SDRWN-(y)tn' < A w šdr; plyst2tn!, -ytn! | M pryst-d, N firistádan] send.
367:fréstag [plystk! | M prystg, (N firista)] apostle, angel.
=== CHEUNG raiz ===
492:*saucé ‘to burn, light", *rai9! / *frait/9 ‘to die, decompose’, *caud / *paud ‘to run’. 
516:defecate’ < *‘to flow’, *tarp ‘to steal’ < *‘to enjoy’ and *rai ‘to die’ < *‘to pass’. 
6317:verbs are contaminated with the *rai$ forms ? 
6697:cannot be established, perhaps it is another "Reimbildung", viz. with *rai0!. 
12787:*PARTHIAN: ryz- ‘to pour’. On ryz- ‘to fall (of leaves)’ see *raiz’. > Ghilain: 94 | 
12817:verb has been contaminated with *raiz?. 
12873:*Hraiz 189 
12901:Sariq. rizd ‘pain’ (rather *raiš ?) || (+ *pati-) Yghn. d’ris-/drista ‘to tear, to be torn 
12913:*Hraiz ‘to shake’ 
12915:*PARTHIAN: 0 On ryzynd see *raiz?. 
13447:Ile Rather *Hraiz ?) || (+ *а-) Oss. І. arzzyn/araezt, D. ar&zumarzzt ‘to be 
20199:*raié ‘to leave, let, abandon’ 
20237:308 *raip ? 
20267:*raip ? ‘to smear’ 
20291:*rai§ ‘to suffer (damage, illness)’ 
20309:‘illness, disease’, ? Sariq. rizd ‘pain’ (rather *rais ?) || (+ *upa-) Pash. bréx (m.) 
20322:*rai0! ‘to lead, go forth; [euphem.] die, pass away’ 
20346:*rai02 ‘to mix, mingle, pervade’ 
20360:310 *raizl 
20403:*raiz ‘to lick 
20427:*raiz3 311 
20447:*raiz? ? ‘to jump’ 
20469:*raiz? ‘to fall (out), drop’ 
20694:© This Ir. root may be related to *Hraiz. The initial /- found in the Wir. forms is 
28207:its rise is that it denotes the physical state (Kellens, l.c.), cf. *raiš. Since both 
37585:*rai-, 306 
55097:*mard, *raic, *raz (S.V.), 
55122:*Hrab/f , *raic? (s.v.) 
55479:*rais (s.v.), *saiH (s.v.), *tap 
55745:(s.v.), *mraH (s.v.), *raic
```


## [2026-09-06T23:00:34.130Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20395,20480p' CHEUNG.txt"
}
```


### [2026-09-06T23:00:34.175Z] TOOL RESULT

```
comparison is therefore meaningless. 


*PIE— => LIV: — | Pok.: 
*REFERENCES: IIFL II: 236a; EVS: 20b, 69b; DKS: 23b f. 


„1 ç A a 
*raiz ‘to lick 
*AVESTAN: YAV. riz- ‘to lick = Liste: 58 
MED. Intens.: pres. IND. 35р. Y Av. (“)raGrizaite (N 68) 


«MIDDLE PERSIAN: BMP Is- /Iis-/ ‘to lick’ 
Pret.: IND. 3sg. BMP Ist /list/ 


*KHOTANESE: rri$- ‘to lick’? © SGS: 116 

*SOGDIAN: BSogd. rys- (inch.) ‘to lick’ 

Inf.: BSogd. rys’ty 

*NWIR: Widely attested: NP listan/lés-, Kurd. (Sor.) lēsīn, listin/les-, Abz., Abyan. 
lesta/les-, Anar. lesse/les-, Bakht. listan/lés-, Gz. les-/lesa (intr.), les-/les(a) (tr.), 
Khuns. Iis-/Iisa, list, Nn. leste/les-, Qohr. lisada/lis-, Siv. Irs-/I1se, Varz. lese/les- ‘to 
lick’ || + *a-) Kurd. (Kurm.) alastin, aléstin/alés- ‘to lick’ 

*NEIR: Sangl. l&s-/let, Ishk. les-/list, Wa. lix-/lixt, Yzgh. yiz- ‘to lick’ (with sec. g- ?) 
|| (+ *ni-) M. neriz-/norizd, Yi. nariz-/norizd- ‘to lick’, ? Wa. narizm ‘stuffed calf? 


*raiz3 311 


*MISC: Par. Jis-/lust, Orm. las- ‘to lick’ 

*SANSKRIT: reh, Ich ‘to lick’ (RV) = EWAia II: 463 

© The unexpected /- found in many Iranian cognate forms is a notorious problem, cf. 
Asatrian 1988: 172 f. 

*PIE *Jeig®- ‘to lick" = LIV: 404 | Pok.: 668 

*IE COGNATES: Gr. aixo, Lat. lingo, OCS liZo, Lith. lieZü, Arm. liz(an)em, Goth. 
bi-laigon, OE liccian, Engl. to lick, etc. 

*REFERENCES: IIFL I: 269b, 400a; IIFL II: 401a, 233a; EVS: 38a; WIM I: 71; DKS: 364a; WIM II/1: 79; 
WIM Ш: 112; Vahman — Asatrian 1991: 112; Werba 1997: 229; Steblin-Kamenskij 1999: 226, 249; 
Cabolov 2001: 72; Lecoq 2002: 121, 123, 126, 133 (passim) 


*raiz? ? ‘to jump’ 

*NWIR: Kurd. (Kurm.) Jistin, laystin/liz- ‘to play; to dance’, (caus.) Iistandin/listin- 
‘to let play, dance’ || (+ *a-) NP aléxtan/aléz- ‘to jump, kick out’, Khor. alij, aliz 
‘jumping up of animals’ || (+ *ui- ? or sec. ?) Zaz. weristis/werzen-, Gil. (Rsht.) 
viriStoen/viriz- ‘to stand up’ 

© The evidence for this root is limited to some modern Wir. languages. The initial 1- 
is rather atypical for an Ir. word: it could suggest borrowing, but perhaps in this case 
it is due to the influence of Pers. larzidan ‘to shake, tremble’ (*rarz) ? An IE 
provenance for this root, which is solely continued in a few modern Ir. languages, is 
conceivable, but difficult to establish. A connection with Goth. laikan ‘to jump, 
hop’, OE läcan ‘to jump’, Lith. láigyti ‘to walk, run around wildly’, is mentioned by 
Lehmann 1986: 225a; Fraenkel I: 330b f. (and also cited in EWAia II: 459 s.v. rej 
*zittern, beben"). 

*PIE ? c» LIV: 405 | Pok.: 667 f. 

*REFERENCES: Christensen, Contributions I: 59; DKS: 364a; Monchi-Zadeh 1990: 8; Paul 1998: 318b; 
Cabolov 2001: 593 


*raiz? ‘to fall (out), drop’ 

*PARTHIAN: ryz- ‘to fall (of leaves)’ = Ghilain: 94 | DMMPP: 304a 

Pres.: IND. 3pl. ryzynd. © On the interpretation of this form see Henning, l.c. 

*SOGDIAN: BSogd. ryz ‘to drop’ (GMS: §900A) || (+ *aua-) MSogd. ’wryz ‘to drop’ 
Inf.: BSogd. ryz’y || (+ *aua-) Pres.: IND. 3sg. MSogd. ’wryzt (Cosmog.: 307); Partic.: pres. Iter. MSogd. 
"wryzyh ‘dropping’ (Sogdica: 31) 

*CHORESMIAN: ryz- ‘to fall ош” = Samadi: 176
```


## [2026-09-06T23:00:57.856Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24780,24805p' BRT.txt\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:24793])\nprint('leaf',t[:idx].count('\\f'))\nEOF\necho \"=== HUB p.95 (leaf = printed+10 => 105) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==106' HUB.txt | head -50"
}
```


### [2026-09-06T23:00:59.615Z] TOOL RESULT

```
•  j.  rae'vant-  Adj.  'reich;  prächtig,  prunk- voll'; a)  von  a)  Menschen  und  ß)  Göttern: o)  virahe  ifhrpa  °vais  Yt  14,  a  7 ;  —  mos- yanqm  ..  'valqm  V.20.1;  Vyt,_57(?);  — naiüa  äV"  °va  maiya  (statt  NS.?)  JäiUi Yti4.36;  F.  77.  ß)  ahuräi  matdai..
'vaitl  i^arsnattuhaitj  (Stverz.)  Y. /2.  i ; usw.;  —  valmca  .  .  •vanhm  Yt  J5. 42;  — tistrJm  (Stverz.)  stänm  'vaiitpm  :^anna*3u- hant»m  YtÄ.  2;usw.;  —  salavaisS  °vä Haoma  betrauten  Unterpriesters  {ratav):\:^ar»narguha  YtÄ3a;  —  manh^m  gao- ^'rahe'^'>  (näml. -f  aiV/m)  yat  haom?mca\H%r?m  'vanttm  :i^  ar>ttamthant»m  Yt.7,  5;
dby  Google
m85
raevas^idra-
'raeSa-
1486
U  (n'äml.  haemahc)  nlre  . .  i^a  'vants  an- jahe  Y.  JO.  17.  b)  sonst:  haSumi  'vä
sfannanuA^  Ytig.6i;  —  haaumatttpm 'vanUm  V,  /.  13,  /(?.  39;  —  kainXnS  .  . snzvai^ys  'vat  et^nm  (sd.)  azataya  Yt. 5.64;  —  u^irS  .  .  °va  hntS  amavä  Yt. 14. 13.  A)  Name  eines  Bergs*':  akmai haca  garays  fraoxsyaii  .  .  'väsca  gairÜ Yt/p.  6;  —  'vantjm  gairTin  S.  2.  9;  — 'vantaAe'''  garSts  matäaiätahe  Ny.  5.  6.
*)  Er  liegt  nach  Bd.  13.  18  in  ^"arJjin  und Ist  der  Sitz  des  fiHTijBfeuers;  s.  noch  Bd. /■?.  34. KompA.;  Ableit.  —  Aus  »r,  ^nHy/iani; S  ^I-  —  ai.  tniänt-  Adj.;  mp.  vgl.  revand Name  eines  Bezirks  in  Apariahr;  s.  Mar- QOART  Eransahr  74.  —  Pü,:  räyömaitd,  Sü.: suddkimäii,  fddhimin.  —  ')  Them.
•  j,  raevas-^idra-  Adj.  (fem.  'rä-)  'von reicher  Herkunft,  von  vornehmer  Abstam- mung': kainlnB..äsaiayh  'roj'J  H.2.9".
Komp.:  rafvant-\-i',  S  JO^II.3.  —  Pü.;  räyo- mand  IS-xmai.  —   i)  Vgl.  Yt,  5.  64.
•  j.  raevas'tama-  Adj.  'der  reichste': zarahustnm  .  .  hatqm  •tmm  Yt.  7J.  151; — yat  kiranaoiti  ärifaol  kavat.masd  (sd.) mand  yäha  -mahe'it  ".  .  wie  (den  Sinn) selbst  des  reichsten"  Y.  ;o,  13.  a)  mit ralm  als  Akk.  der  Beziehung:  zara^u/fr^m .  .  yal  as  .  .  racm  'mS  Yt.  ig.  79.
Superl.  aus  racvanl-,  —  Pü.:  räyömand,  Sü.: *lddhimatiartth.
•  j.  raez-  V.  'lecken,  leckend  verzehren*. Praes.   1  rau-.
vTspanam  (als  Obj.)  si  *ava.sras(intam paraca  adayamananqm  dafva  *ralzaiie '' . "alles  was  (davon)  abtrieft  und  verschüttet wird,  (das)  lecken  die  D.  auf"  N.  öri''>.
ai.  rrhmi,  Uhmi  'ich  lecke',  rp.  Uilan;  s.  noch JüSTi  DL.  igoi.  1063,  —  Pü.:  mfndSi  (3P.) •sie  lecken'.  —  ')  S  /fy-  2;  Hds.  •za?ii.  vg!. IF-  5-  37f-  —  ''  Vgl.  iSi,  Bthl. IF. 5. 369. — 3)  So,  mit  1,  gegenüber  np.  Ihad.  Auf  i  geht auch  X  in  PDw.  l.xam  -ich  lecke',  vgl.  /oj 'Durst'  und  np.  HS  usw.
•  j.  raes-  V.  'Schaden  tun,  —  nehmen'. Praes.  26  ralsya-  (trans.),  3^  irisya- (trans.,  intrans.),  30  (Kaus.)  ralfaya-.  — PPfP.  irisia-  (sbes.).  —  [S.  noch  '^irlrls,
i)  'leibhchen  Schaden  tun',  absol.  und mit  Akk. :  mä  ..  kaine  . .  garsw>m  raiia- ySi  yesica  . .  kaine  . .  ganw^m  irilyäti  . . ^jr^fya  (sd.)  iri/yeifi  V.  15.  n  f.;  —  mäca
. .  vTmäoasal  vTmalayanta . .  mS^a  ^hr?tu (sd.)  irisyät  V,  7.38;  38; — yai  nSij  ipS .  .  pasüm  va  tianm  va  ral^at ,.  paoirim pasBm  avaynat  paoirXm  nanrn  ra^a^  V, 13.  31  f.;  Vyt.44(ivo*j^ya^).  3  a)  'leib- lichen Schaden  nehmen,  leiblich  geschä- digt werden':  yai  nsit  spa  .  .  maeje  va .  .  paihyäite  ahmat  haca  irisynt  yest  tat paiti  irisyeiti  V./j.  37f ; /j.  4; — apanm (sd.)..ni^it  iiim  ava'^a  iri/yqn  "..so  wer- den sie  keinen  Schaden  nehmen"  V,  75. 48'';  —  yen  ..  spana  aoaityö.a/>Aar>%nm (sd.)  irisyqn  para  allqm  iriHintam  raisS äkam  ..'V. 15.33;  '12,  16,  Vyt.44;  — para  hi  irisints  rals>m  Hkayat  V,  /j, 16,  7.38  (wo  irissnlsY^.  b)  'peku-
niären Schaden  erleiden':  allö  galhanqm *iriiintinqmi'>  ragie  (sd.)  N.  2,
mit  a  dnwS.s:   ya^a  nSit  aiti(sd.)  ni- läitica  *airi/yq  (3PKA.)*'  N.  Öji?).
ai.  risyixii  'ei  tut,  nimmt  Schaden',  refäyali 'er  tut  Schaden',  ri}/iiA;  mp.  resilan.  —  Pü. : reiitan,  zu  3  a  erl. :  api  murtan.  —  ■>  Pü. : ku  ne  an  i  pas  Ö  i  pis  etön  relet.  —  ')  S.  zu hindav-  Nu.  I.  —  J)  Hds.  'hntanqm.  —  4)  Hd». airiyq.
"  J,  'raesa-  m.,  raesah-  n.  'Schädigung'; A)  körperliche  Schädigung  überhaupt; a)  in  Bezug  auf  den  Fötus;  yeHi^a  . .  kaine . .  3^atö  garnuim  irisyeiti  .  .  ptinbyS  (sd.) irisintqtn  ralli  Hkain  baoiiS.varltahe  ci- %aya  V.  75. 1 3.  b)  in  Bezug  auf  Hunde: yS  süne  piilrtm  jainti  ..  us  va  hl  gaohm 'hwirisaiti  apa  va  ks  pathyqm  kintUaiti . .  cikayat  sBnahe  °l5  (ASn.)  baob5.varHahe üfhaya  V.ij.io;  'Vyt.44;  —  ym..spiina ahaiiyS.at»/iar3^r>m  (sd.J  irisyqn  para  as- iqm  iriHntqm  'h  cikaen  baoZs.var^iahe Hhaya   V,  75.  22,  40.  2)  Rechtsaus-
druck fiir  jede  einem  Menschen  indirekt diu'ch  Fahrlässigkeit  zugefügte  körperliche Schädigung,  fahrlässigeKörperverletzung*': yai  .  .  vlmaaascit  vtmahayänie  .  .  yai "k^ritu  (sd.)  iriSyat  para  hi  trismtB  'stm cikayat  bao'üö.varstaht  a^aya  V.  7.  38;  — yezi  .  .  apirmäyüks  doaityS.ajiharihnm (sd.)  iriiyäi  para  hl  iriüntS  °s)m  Hkayal bao*>S.varstahe  ii'haya  Y.15.16;  —  nabä- nazdistim  h!  .  .  para  .  .  *'/aäi ''  *aowa- oaityacd  *ästäraiti  (sd.)  N.  g.  B)  peku-
;niäre;  damnum:  also  gafhanam  *iris'inti- I  nqm  ■«  (als  AP.) ''  (näml. :  pa'iti  Hkayatf) \  "der  (ihn  durch  sein  Weggehen  verursache hat,)  soll   den  Schaden  des  geschädigten
leaf 812
=== HUB p.95 (leaf = printed+10 => 105) ===
— 95 —
ksl. glava 'Kopf ', arm. glux 'Kopf etc. Zu merdle vgl.
Vullers, Grammatica linguae persicae p. 235, wo die
Formen auf le als Formen des Tat-Dialectes bezeichnet
sind. Darauf verweist auch Mann, ZDMG. 47, 705.
931. Np. gumaStan = pfiz. gumdrdan = phi. gumdrtan
'einsetzen, bestimmen, beauftragen, betrauen' Min. Gl.
93, Bdh. Gl. 225, afgh. gumdrql to consign*, arm.
LW. gumar-el 1) sammeln*, 2) 'schicken, iibergeben,
einsetzen* zeigt nirgends den Anlaut t?- und hat jeden-
falls mit ap. *m-inar = skr. vi-smar nichts zu thun.
932. Np. guman = ap. ^mmOna^ (statt zd. *vfmanah'),
Vgl. unten Nr. 965.
934. Vgl. KZ. 33, 165. Dazu nun auch afgh. yand^ql *Ekel
empfinden, nicht leiden, nicht mOgen' (Geiger). Afgh.
ganda 'stinkend' finde ich nicht bei Raverty.
935. Skr. gddhUma^ wird volksetymologische Anlehnung
von ^gandhUma- an die Composita mit gd- *Kuh* sein
{go-dhuma- gleichsam *Kuhrauch'; vgl. unsern Pflanzen-
namen Erdrauch, gr. xanvog^ mnvioc).
936. Dazu arm. LW. gund 'Kugel', gndak *Kugel, Ball,
KnoUen'. Ich halte die Etymologic fiir richtig.
937. Hochst unsicher.
938. Unsicher.
Hierher nach Fr. Miiller, WZKM. 8, 189 guvdrtdan ver-
dauen' = phi. gukar-Uan zu skr. vi-kar umwandeln .
940. Arm. vkay gehdrt nicht zu np. guvdh, vgl. meine
Abhandlung *Arisches und Armenisches*, Idg. Forsch. 4,
p. 119.
941. Ich fasse gosdla *Kalb* als Compos, von go- = np.
gav, gav *Kuh' und sdla *Jahrling (von sal *Jahr ab-
geleitet wie in den Zusammensetzungen mit Zahl-
wortern -sdla = jahrig' ist), also = 'Kuh-jahrling,
vgl. unser 'Jahrlingskalb'. Kurd. LW. gilsile ZDMG.
38, 85.
^4. Np. gost 'Fleisch' = ap. *gausta-?
946. Arm. goin ist Lehnwort, aber aus anderen Griinden.
Ebenso arm. gunak =n np. guna* Afgh. yuna f. 'Haare
[
```


## [2026-09-06T23:01:08.183Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"listen\\|lestan\\|l(i)stan\\|lisidan\\|lesam\" HUB.txt | head -20\necho \"--- 954/955 notes ---\"\ngrep -n \"^95[3-6]\\.\\|^ 95[3-6]\\.\" HUB.txt | head"
}
```


### [2026-09-06T23:01:08.241Z] TOOL RESULT

```
3395:nachfolgende richtige Erklarung von np. lesam auch
3399:lesam umgestaltet wurde. Vgl. Fr. M tiller, WZKM.
8376:^) Vgl. auch ^y^z. farman-nyoxs 'listening to commands* Shk. 244.
--- 954/955 notes ---
3389:953. Np. lab 'Lippe' = paz. law, phi. lap Shk. 257, bal.
3394:954. Die Ansetzung eines ap. lais ist falsch, durch die
```


## [2026-09-06T23:01:11.127Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3385,3410p' HUB.txt\npython3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:3393])\nprint('leaf',t[:idx].count('\\f'))\nEOF"
}
```


### [2026-09-06T23:01:13.344Z] TOOL RESULT

```
scheint, zu Inl 'to perform, pronounce, utter, give',
das Geiger freilich zur Wrzl. skr. da 'geben' stellt
und von lavdql reden, aussagen' trennt. Die ganze
Zusammenstellung ist wohl nicht besonders sicher.
953. Np. lab 'Lippe' = paz. law, phi. lap Shk. 257, bal.
lap setzt ein iranisches lap- voraus, wahrend lat.
labium und deutsch Lippe auf leh- zuriickgehen. Doch
deutet np. lafSa *dicke Lippe' vielleicht auf alteres lah-
Kurd. /^w? Xippe' bei Socin, kurd. Samml. II, 335.
954. Die Ansetzung eines ap. lais ist falsch, durch die
nachfolgende richtige Erklarung von np. lesam auch
iiberfliissig: idg. lig^h = iran. ap. lis bildete den Inf.
*listanaiy = np. listan, das Praesens Haizamiy = np.
*lezam, das nach dem Muster von nivistan : niv^am zu
lesam umgestaltet wurde. Vgl. Fr. M tiller, WZKM.
6, 351.— 97 -
957. Np. maz Treude, Vergniigen* wird auf ap. ^maza- oder
"^maja- = skr. ^magha- oder *maha- (vgl. KZ. 25,
100 flg.) zuriickgehen und mit Noldeke zu skr. mah
*sich ergotzen , mahina- *fr6hlich, lustig' (von idg. meg^h)
zu stellen sein. Ueber die urspriinglichen Beziehungen
von skr. mdh gross (= zd. maz-) zu skr. mah 1) *sich
ergStzen, 2) schenken' (vgl. skr. mqh 'hingeben,
schenken', maghd- *Gabe, Geschenk' = idg. meg^h)
lasst sich verschieden urtheilen. Vgl. BQhtlingk's
Sanskrit wb. s. v. mah, Whitney, die Wurzeln, Ver-
leaf 106
```


## [2026-09-06T23:01:26.038Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD lick ===\"\ngrep -n \"lick\\]\" PHD.txt PHD_mackenzie.txt | head -10\ngrep -n \"lys\\b\\|/līs/\\|lis-, list\\|listan\" PHD_mackenzie.txt | head -10\necho \"=== NYB glossary lick ===\"\ngrep -n -i \"to lick\\|lick'\" NYB_vol2_glossary.txt | head -10\necho \"=== AHD watkins leigh ===\"\ngrep -n -i \"leigh\" AHD_watkins1985.txt | head -10\necho \"=== AHD watkins leig / laikan ===\"\ngrep -n -i \"laikan\\|^leig\" AHD_watkins1985.txt | head -10\necho \"=== IEC leigh ===\"\ngrep -n \"^leig\\|^leigh\\|^lighō\\|^ligh\" IEC.txt | head -20"
}
```


### [2026-09-06T23:01:26.143Z] TOOL RESULT

```
=== PHD lick ===
1231:aspres ['splys IN .....] race-course.
=== NYB glossary lick ===
=== AHD watkins leigh ===
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
951:slak-. To strike. 1.Germanic *slahan in Old English sléan, to strike, kill: sLay. 2. Germanic suffixed form *slag-j6- in Old English slecg, hammer: SLEDGEHAMMER. 3. Germanic suffixed form *slah-tram in Old Norse sidtr, butchery, “striking,” probably akin to the Scandinavian source of Middle English slaughter, killing: SLAUGHTER. 4. Germanic *slag- in: a. Old High German slag (> German Schlag), a blow: scHLOocK; b. Middle Dutch slag, a blow: ONSLAUGHT; C. probably Middle Low Ger- man slagge, metal dross (< “that which falls off in the process of striking”): SLAG. 5. Germanic suffixed length- ened-grade form *slégiz in Old Norse sl@gr, clever, cunning (< “able to strike”): SLEIGHT, SLY. [Pok. slak- 959.]
955:5. Suffixed form *lag-no- in Greek lagnos, lustful, lasciv- ious (> lagneia, lust, lasciviousness): ALGOLAGNIA. 6. Variant form */ég- in Greek légein, to leave off: CATALECTIC. [Pok. (s)lég- 959.] sleidh-. To slip, slide. 1. Germanic *s/idan, to slip, slide, in Old English s/idan, to slide: SLIDE. 2. Germanic *slid- in: a. Middle Low German sledde, a sled, sledge: SLED; b. Middle Dutch s/éde, a sled: SLEIGH; C. Middle Dutch sleedse, sleigh: SLEDGE. sleng”h-. To slide, make slide, sling, throw. 1. Germanic strong verb *slingwan and derived suffixed noun form *slingw-6- in Old Frisian slinge, sling, akin to the possi- ble source of Middle English sling, sling: SLING}; (SLING- SHOT). 2. Germanic variant strong verb *slinkan in Old English slincan, to creep: SLINK. 3. Suffixed o-grade form *slongh-ri-ko- in Latin lumbricus, intestinal worm, earthworm: LUMBRICOID. [In Pok. (sjleidh- 960, slenk- 961.] sleu-. Hypothetical base of a group of distantly related Germanic derivatives with various suffixes. 1. Germanic *slii-m- in Old English slima, sleep: SLUMBER. 2. Prob- ably Germanic *slautjan- in Old English “s/léte, sleet: SLEET. 3. Germanic *slus- in Norwegian slusk, sloppy weather, probably akin to the possible Scandinavian source of SLUSH. 4. Germanic *sleura- in Middle High German slier, mud, slime: SCHLIEREN. 5. Extended form *sleug- in Germanic ‘*sluk-, *slug- in: a. Norwegian dialectal slugg and Swedish dialectal slagga, slow-mov- ing animal or person, probably akin to the source of Middle English slugge, a sluggard, and sluggen, to be idle: SLUG?, SLUGGARD; b. Dutch /og, lazy, slack: LOGY. [Pok. (s)leu- 962.] sleubh-. To slide, slip. I. Basic form *sleubh-. 1. Ger- manic *slewb- in Old English s/éf, siif, slief, sleeve (into which the arm slips): SLEEVE. 2. Suffixed form *sleubh- ro- in Latin Jibricus, slippery: LUBRICATE, LUBRICITY, LUBRICIOUS. II. Variant Germanic form *sleup-. 1. Ger- manic *slup- in: a. Old English slypa, slyppe, slipa, slime, slimy substance: SLIP’; COWSLIP, OXLIP; b. Old English *sloppe, liquid food (perhaps > Middle English sloppe, a muddy place): sLoP!; c. Old English (ofer)slop, surplice (perhaps > Middle English sloppe, a kind of garment): SLOP?. 2. Germanic *s/aup- in Dutch sloep, sloop (< “gliding boat”): sLoop. [Pok. sleub(h)- 963.] sli-. Bluish. Contracted from *s/is-. 1. O-grade form *sloi- in Germanic *slaihw6n in Old English s/ah, sla, sloe (< “bluish fruit”): SLOE. 2. Suffixed form *sli-wo- in Latin livére, to be bluish: Livip. 3. Suffixed form *s/i-wd- in Serbo-Croatian sijiva, plum: sLivovitz. [Pok. (s)li- 965.] sloug-. Help, service. Celtic and Balto-Slavic. Suffixed form *sloug-o- in Old Irish slag, slog, army, host, whence Gaelic sluagh, army, host: SLEW!, SLOGAN. [Pok. slougo- 965.] smé-. To smear. Contracted from *smeo-. 1. Extended root *smeid- (< *smea-id-) in Germanic *smitan in Old English smitan, to daub, smear, pollute: SMITE. (2. At- tributed by some to this root, but more likely to be of unknown origin, is the Germanic root *mas-, spot, speck, in: a. Middle Dutch masel, pustule, spot, akin to the source of Middle English masel, measles-spot: MEASLES; b. Old French masere, mazre, knot in wood: MAZER.) 3. Attributed by some to this root, but perhaps distinct, is root *smik-, small, in: a. Latin mica, crumb, small piece, grain: MICA; b. Greek (s)mikros, small: MICRO-, MICRON; CHYLOMICRON, OMICRON. [Pok. smé- 966.] smeg-. To taste. Germanic *smak- in: a. Old English smzxc, flavor, taste: SMACK?; b. Middle Dutch and Mid- dle Low German smacken, to taste, make a sound with the lips while tasting food, akin to the source of SMACK!. [Pok. smeg(h)- 967.] smei-. To laugh, smile. 1. Germanic reshaped forms *smer-, *smar- in Old English smercian (with -k- forma- tive), to smile: SMIRK. 2. Germanic extended form *smil- in Swedish smila, to smile, probably akin to the Scandi-
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1448:ELDER? el-2 ELDEST al-3 ELECAMPANE wel-3 ELECT leg-1 ELECTUARY leigh- ELEVATE leg*h- ELEVEN oi-no- ELF albho-
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1742:LICH GATE [k- Lick leigh- LICORICE dik-u-, wrad- LID. klei-
2269:SLAUGHTER  slak- SLAVER! |leb-1 SLAY slak- SLED sleidh- SLEDGE sleidh- SLEDGEHAMMER slak- SLEEP sléb- SLEET sleu- SLEEVE sleubh- SLEIGH sleidh- SLEIGHT slak- SLEW! sloug- SLICK lei- SLIDE sleidh- SLIGHT lei- SLIM leb-1 SLIME lei- SLING! slengWh- SLINGSHOT slengh- SLINK sleng’h- SLIP! lei-
=== AHD watkins leig / laikan ===
=== IEC leigh ===
9568:leig- (pleig)? ‘rudder’ Arm. yeak, gs yeki, absg. yekav, (and yek, -i, -av), id.; Ir. cf. liagán and liogán, m. id.; W llyw, pl. -iau, m. id.; OCor. lew, pl. -yow, m. id. beside loē, pl. loeow ‘ruler’
9570:leig- (2), leigio ‘creep, go’. Cf. Ioig- Skt. réjami, réje (1) ‘go’; OFris. liza ‘run, go’; Icel. cf. lík "leech-line'; o-gde in OCS l&zgo, lésti ‘creep, go’, and com. SI.
9582:leigho, io ‘lick’. (Variant of type leig- (1), q. v.). Cf. WP II, 400 Skt. ledhimi, lidhemi, id.; Gk. leikho, id. (Sl. Celt. & Balt. ambig.), cf. (infixed) Lat. lingo, Gre Ir. (zero-gde) lighim; W Ilyaf; MHG l&cken, id. (from *lig-. W & Ir. ambig.) See next
9583:leiguis, leiĝus ‘tongue’. WP I, 792, cf. also II, 400. See leig- (1), lig- Arm. lezu, gs lezvi, absg lezvav, id.; Ararat Arm. lizu, id.; OIr. & mod. Ir. liag, f. ‘spoon’; W llwy, f. id.; Cz. liz, gs -u, m. 'salt-lick'; Big. cf. lézvije 'knife-blade, cutting-edge'; Li. liežuvis, gs -io, m. ‘tongue’; Latv. cf. lize *baker's peel (*-i-)
```


## [2026-09-06T23:01:36.738Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nfor n in 404 405; do echo \"###### leaf $n (printed ~$((n-5)))\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' WLD_Bd2_pages.txt | head -45; done"
}
```


### [2026-09-06T23:01:38.154Z] TOOL RESULT

```
###### leaf 404 (printed ~399)
                                                      leig-, loig-                                             399

Letterk. 25, 267, 285 f.   (wenigstens fiirs Germ, ist von „Gestalt^‘ auszu-
gehn, ga-leiJcs also „von gleicher Gestalt'^; allerdings kann die Bed. „Ge-
stalt‘‘ ihrerseits aus „Ebenbild“ gewonnen werden), auch Falk-Torp u. lig I,

lig Adj., -lig (mit tTbersicht anderer Deutungen der germ. Sippe).
     Ganz    fraglich     sucht    Fick aaO., Uhlenbeck Ai. Wb. 261) eine
                                     man        (so
nas. Wzf. in        ai.                                   av. hapto-tringa- m.
                          Irnga- n. „Kennzeichen, Abzeichen^^,
„(mit 7 Merkmalen =) das Siebengestirn“. In cymr. cyffelyh „ahnlich^‘ ist
kein Hig-uo- verbaut (gegen Stokes IF. 2, 168. Fick 11^ 251; vielmehr ^kom
+  cymr. hafal „similis“ mit A:!f-Suffix s. Pedersen KG. I 280, II 33, 128)
und air. adlaic „angenehm erwiinscht (Stokes IF. 2, 168, Fick 11^251,
unter HigiV^yni-) entspricht weder in Form nocli Bed. Eine Wzf. auf Tenuis
ist uberhanpt unerwiesen; gr. dUyxiog „ahnlicli“ (Persson, Boisacq) ist ganz

unklar. und weder fiir *Jeiq- „Gesicht, Wange“ (s. Berneker 720 gegen
Ehlenbeck Ai. Wb. 261), noch fiir ^leiq- „feilbieten“ (als „sich beim Handel
vergleichen'*?? s. Yf.LEWb.^ u. licet) liegt von seiten der Bed. Gleichsetzung
mit    "^leig-   nahe.


. leig-, loig- jjhiipfen, beben; beben machen“.
     Ai.   rejati   „macht      hiipfen,         laBt     erbeben^',            rejate    „hupft,   bebt,   zuckt’S
rvjdyati ,,macht          erzittern,        beben'^,               ausschlagen
                                                           npers. alU/tan „springen,
(vom Pferde)‘‘, kurd. be-lesntm „tanze“, llzim „spiele“ (eine Variante auf
q in ai. rcka-h „Froscb‘' als „HupfeP'? z. B. Persson Beitr. 151, der wohl
mit Unreclit an ?.tx£ori^eiv oxigrdv Hes. anreiht);
                                       '



   gr.                   „mache erzittern, scliwinge'^, eXeU^'^yyy&cDv „Erder-
schiitterer”; (dazu stellt Hoffmann /Ypa;- 41, Persson Beitr. 151 wohl auch
My- „worauf          losstiirmen^'         in    Xiyaivet'    .   .    .   tj   d^emg ecpooga^ Xiya* xayecog^
              und iihnlichen Hesychglossen): Holthausen IF. 25, 148 gr.
           nal^et
Xiyvvg „Qualm, Rauch“ nach dem Verhaltnis \oti filmtis 'dvvoj^ ai. dhtinoti                  :




###### leaf 405 (printed ~400)
400                                      leig-j leig*   — leigh-
  Ir.                    lem ds. gehoren hierher und sind als *loigo- Be-
        Ideg „Kalb", bret.
weis    fiir  bzw. e/o-Yokalismus unserer Wz., s. Pedersen KGr. II 22 f.
               o-,
und Hap- „Kub‘'; daher muB idg. Hoig- angesetzt werden und wird germ.
laikan wohl nach Brugmann BP. 32, 193 Perfekt-, bzw. Iterativvokalismus
ins Praesens verschleppt zu haben.                      —
                                           Fiir eine Wzf. auf -g- hat man
auBer abg. lik^ noch ai. reka- m. (unbelegt) „Frosch^‘ als ,, Springer*' geltend
gemacht (Uhlenbeck Ai. Wb. s. v.; ganz fragwiirdig.

4, leig-, leig- „binden".
   Alb.      pass, Videm „binde, verbinde, giirte", Vide, Vide „Band, Fessel;
Garbenband, Bruchband" {g; G. Meyer BB. 8, 186, Wb. 245); lat. Ugo-^ -are
jjbinden, zsbinden" (s. auch Yf. LEW^b.^ s. v.); mnd. Uk „Band", aisl. Ilk
„Saumtau“ (Liden Uppsalastudier 88), ablautend wohl mhd. geleich „artus,
Gelenk"; mit g klr. polyliaty ba „sich verbinden", mlyMti/ „in Bande
schlagen, schniiren, ankniipfen, in Beschlag nehmen", nahjhaiy „Zaum,
Schlinge anlegen, fesseln" (Zupitza Gutt. 197, Berneker 717), vermutlich
auch (wie gr. Ttevd^egog „Yater der Frau" zu Hhendh- „binden") lit. Jaigd-
vas „Bruder der Frau" (Wiedemann BB. 27, 212), wozu koiycoviiav^ <PQ(x-
TQiav Hes. (Hoffmann Mitt. d. schles. Yer. f. Yolksk. 13                   —
                                                             14, 183f., Citat
nach Berneker aaO.).
   Aber nir. leac (air. Hccc) „aa act or deed, which binds the persons indis-
solubly" (von Stokes IF. 2, 169, Fickll^ 251 als Hignd angereiht) fordert
eine auf Tenuis schlieBende ^Yz. und ist identisch mit air. lecc „Stein" in
der Bed. „feste Grundlage eines Yertrages" (Thurneysen briefl.).

leigh- „lecken".
  Ai.    ledhi, rfdhi,   lihati    „leckt",       lehd- m. „Lecker“,       av. 3. pi. raemite
(Bartholomae IF. 5, 369)          „sie lecken", np. liMan           „lecken" (usw., s. Bartho-
lomae Airan. Wb. 1485, Brugmann I^ 428)                     :   arm, (Hiibschmann Arm. Stud.
I 32, Arm. Gr. I 452) liziim, liseni, lizanem „lecke";                 gr. leiyco „lecke“, Xei-
       „Flechte, Ausschlag"       dazu Yf. LEWb.^ u. delictus, Boisacq s. v.),
                                   (s.

Xr/yog „lecker, naschliaffc", Xiyvevco ,,belecke", Xtyavog „Zeigefinger“ („Lek“
ker"); lat. lingo, -ere, linxi „lecken", ligurrio, ligurio „lecke" (vgl. formal
ir. ligiir,  Corm, ,,Zunge"), ligida (^ligh-ld) „Loffel", wie auch mir. liag,
cymr. llivy, bret. Joa, corn, lo „Loffel" {^leigha, Strachan Phil. Soc. 1893,
May 5 [lA. 4, 103], Pick II ^ 241, Pedersen KG. I 101; aber ksl. hzica,
russ. lozka „Loffel", aus deren Stamm wort H^ga nach G. Meyer Alb. Wb.
250, IF. 2, 368 alb. Vugs „L5ffel" entlehnt ist, bleiben trotz Pedersen und
```


## [2026-09-06T23:01:46.299Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T23:01:46.306Z] TOOL RESULT

```


```


## [2026-09-06T23:01:50.029Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lark",
 "prompt": "Give the full etymology of \"lark\" (both the bird and the noun/verb meaning frolic, carefree adventure), including any mention of Old Norse leika, Middle English laik, dialectal lake 'to play', Gothic laikan, and PIE root."
}
```


## [2026-09-06T23:01:51.933Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%DB%8C%D8%B3%DB%8C%D8%AF%D9%86",
 "prompt": "Give the Persian entry لیسیدن: etymology, Middle Persian form, Proto-Iranian root, Proto-Indo-European root, and any related forms such as لیستن/لشتن."
}
```


### [2026-09-06T23:01:57.123Z] TOOL RESULT

```
# Etymology of "Lark"

## The Bird (lark n.1)

The songbird term originates from Old English *lawerce* (late OE *laferce*), deriving from Proto-Germanic *\*laiw(a)rikon*. This root appears across Germanic languages: Old Saxon *lewerka*, Dutch *leeuwerik*, and German *Lerche*. The ultimate origin remains unknown. Medieval forms suggest "a contracted compound, perhaps meaning 'treason-worker,'" though this interpretation lacks folkloric support.

## The Frolic/Adventure (lark n.2)

This playful meaning emerged in 1811 as slang with uncertain origins. It may derive from *skylark* (1809), sailors' terminology for "play rough in the rigging of a ship." Alternatively, it could represent a dialectal English variant of *lake/laik* meaning "to play, frolic," originating from Old Norse *leika* "to play." This Norse term traces back to Proto-Indo-European *\*leig-* (3) "to leap." The word *lake* characterizes Northern English vocabulary and represents the opposite of work, though lacking play's broader semantic range.

The verb form *larked* (meaning "to play tricks, frolic") appeared in 1813, spawning related forms like *larking* (1813) and *larky* (by 1841).
```


### [2026-09-06T23:01:57.866Z] TOOL RESULT

```
# Persian Entry: لیسیدن (lēsīdan)

## Etymology
The word derives "Ultimately from Proto-Indo-European *leyǵʰ- ('to lick')" with cognates including Old Irish *ligid*, Latin *lingō*, and English *lick*.

## Middle Persian Form
The document does not provide a Middle Persian form for this entry.

## Proto-Iranian Root
Not explicitly stated in the provided content.

## Proto-Indo-European Root
*leyǵʰ-* ("to lick")

## Related Forms
Alternative spellings listed include:
- لستن (lestan)
- لشتن (leštan)
- لیشتن (lištan)

The entry presents conjugations for both literary Iranian Persian and colloquial Tehrani dialects, with the present stem لیس (lis) and past stem لیسید (lisid).
```


## [2026-09-06T23:02:02.855Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyǵ%CA%B0-",
 "prompt": "Give the reconstruction, gloss, and descendants of this PIE root, especially Proto-Iranian/Avestan/Persian and Proto-Germanic forms."
}
```


## [2026-09-06T23:02:04.481Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/laikan%C4%85",
 "prompt": "Give the Proto-Germanic reconstruction *laikaną: gloss, etymology (PIE root), and descendants including Old Norse leika, Gothic laikan, Old English lācan."
}
```


### [2026-09-06T23:02:09.407Z] TOOL RESULT

```
# Proto-Germanic *laikaną

**Gloss:** "to jump, play, move, swing about"

**Etymology:** Derived from Proto-Indo-European *leyg- meaning "to jump around, bounce, shake, tremble."

**Key Descendants:**
- **Old Norse:** leika (modern Icelandic leika, Swedish leka, Danish lege)
- **Gothic:** laikan
- **Old English:** lācan (evolving into Middle English laken, modern English "lake")
- **Old High German:** possibly *leihhan (becoming German laichen)

The verb represents a strong class 7a conjugation pattern, with past tense forms like *lelaik showing characteristic Germanic reduplication.
```


### [2026-09-06T23:02:09.489Z] TOOL RESULT

```
# PIE Root *leyǵʰ- (to lick)

## Reconstruction and Gloss
The reconstructed Proto-Indo-European root is **\*leyǵʰ-**, classified as an "imperfective" verb meaning "to lick."

## Key Descendants

**Proto-Iranian/Persian:**
- Proto-Indo-Iranian: \*láyȷ́ʰati
- Proto-Iranian: \*láyjati (with further descendants documented)

**Proto-Germanic:**
- \*likkōną (from the nasal-infix present formation)
- \*laigōną (from the eh₂ye-iterative formation)
- Gothic: \*laigōn
- Old Norse: sleikja (attested in Faroese and Icelandic as well)

**Other Notable Descendants:**
- Sanskrit: लिह् (lih, "to lick, taste, eat")
- Latin: lingō (via Proto-Italic \*lingō)
- Ancient Greek: λεῖξαι (leîxai)
- Lithuanian: laižýti; Latvian: làizît

The root exhibits multiple formations including thematic presents, athematic presents, s-aorists, nasal-infix presents, and iterative/causative derivations across Indo-European language families.
```


## [2026-09-06T23:02:16.471Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY لیسیدن ===\"\ngrep -n \"ليسيدن\\|لیسیدن\\|ليس\\b\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY آلیز ===\"\ngrep -n \"آليز\\|آلیز\\|آليخ\\|آلیخ\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY latin index LEIGH / LEIG ===\"\ngrep -n -i \"LEIGH\\|LEIG-\\|LEIKW\\|leigh\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== SKT lick / lark ===\"\ngrep -n \"^LICK\\|^Lick\\|lick,\" SKT.txt | head -5\ngrep -n \"^LARK\\|Lark,\" SKT.txt | head -5"
}
```


### [2026-09-06T23:02:16.564Z] TOOL RESULT

```
=== ARY لیسیدن ===
8910:انگليسي (57/ت2۸/0): 30710270 ,۸01070 برهان قاطع : ار ۲
13479:لیسیدن, لشتن / ۴۵۵
=== ARY آلیز ===
1933:آلیز آلیزیدن» آلیختن(به چم *جفتک انداختن») / ۶۹
=== ARY latin index LEIGH / LEIG ===
=== SKT lick / lark ===
2012:Boat.  (E.)  M.  E.  boot.  A.  S.  bat.  + Icel.  b<Ur\  Swcd.  bAt\  Dn.  bcof\  Kuss. bof  ;  W.  boii;  Gael.  b4ta,  a  boat.  fl.  The orig.  boat  was  prob.  a  bat,  i.e.  slick,  branch, Stem  of  a  tree:  cf.  Gael,  and  Irish  ^M. staff,  stick,  pole,  branch,  bat.     Sec  Bat.
8000:Grig,  a  small  eel,  a  cricket  (Scand.) Weakened  form  of  ertck,  still  preserved  in criik-ii;  cf.  Lowl.  Sc  tritk,  a  lick,  loose. —Swed.  dial,  krik,  AraJt,  a  creeping  crea- ture. —  Swed.  dial,  kraka^  to  creep ;  cf.  G. kritcken,  to  creep.  ^  In  phr.  *aa  merry as  a  grig*  grig  is  lor  Greek  (Troil.  i,  i. 118);  Merygreek  \»  a  chamcicr  in  UiUH'a KuisSer  Doister ;  from  L.  gnKmrit  to  liv« like  Greeks,  i.e.  luxuriously.
9879:Iiombeiit.  flickering.  (L.) flame.***  L.  lambent-,  stem  of  pres lambcrc,   lo    lick,    sometimes    appli flaiue»t«f*Gk.  Aiirr«r.  to  lick.     All Lap  u  V
10957:malinger,  to  feign  sickix Coined  from   F.  malin foimerly  ugly,  loathfiome- badly;  O.  F-  kamgrt, dated. —  L.  male,  adv..  badly of  trggr,   lick,   ill  (whence  O. with  added  h  and  h).
17482:Sleek,  Slick,  smooth,  glossy.  (Scand.) M.  E-  slyk,  slikt.  —  Icel.  sUkr^  sleek,  smooth. Allied  to  Da.  slijk,  G.  scMUk,  grease ;  from the  Low  G.  strong  verb  sliktn  (pt.  t.  skik^ pp.  /^im)— G.  ukliiehen  (pt.  t.  */(>A\  to slink,  crawl,  move  as  if  through  mire :  see Blink.  Orig.  sense  'greasy,*  like  soft  mud.
```


## [2026-09-06T23:02:26.222Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '1925,1940p' ARY_pages.txt\necho \"===\"\nsed -n '13470,13488p' ARY_pages.txt\necho \"=== find printed 69 and 455 ===\"\ngrep -n \"\\[pdf page 6[89]\\]\\|\\[pdf page 70\\]\\|\\[pdf page 45[456]\\]\\|\\[pdf page 457\\]\" ARY_pages.txt | head"
}
```


### [2026-09-06T23:02:26.291Z] TOOL RESULT

```
۳ 8۸13۲1۸۹7 معتقد است که شاید این واژه با واژه‌ی لاتین ۸011۸(آب) همریشه باشد. ۱
۴ ۳0۴018۷9 فقط واژه‌های ایرانی و ارمنی و یونانی این فهرست را از واجریشه‌ی -3۷80* می‌داند و بقیه را از
واجریشه‌ی -12* می‌داند.
د- 05۸31۸35 بیشتر واژه‌های این فهرست را از واجریشه‌ی -/08* پا -01308* مي‌داند.
پندار نویسنده‌ی کتاب حاضر این است که این واژه‌ها به احتمال زیاد همه از یک واجریشه‌اند ولی برای آگاهی
خواننده» جلر واژه‌های مشکوکك (شاید) آورده است.
[pdf page 68]
نج
آلیز آلیزیدن» آلیختن(به چم *جفتک انداختن») / ۶۹
کردی (015): 85-18571011 ,ل#13ا1 لیتوانی (/(م/ههنا بل 7ال): ,شا
سانسکریت (887۸758:)54۸43777 ب8۸[۸71 کشا
بونانی 08570): زیم 8 ایرلندی (37ل#)): 06
گونیکه (00777/0): قالش رالشاتشآ برتونی (886700): ره
ایسلندی کهن ((۷210۸/14(م5 ا0):
3 ادها پسگشت‌ها شنت دی
آلمانی کهن (05724۸ 10لا صا0): ۸008
===
انگلیسی (ب8اا0/(ق): 126 فرهنگ معین + ۳۶۳۱
دانمارکی (0۸/3): ان برهان قاطع + ۱۹۰۷
یادداشت:,
چم این واژه در زبان لاتین؛ بازو
چم این واژه در زبان آلمانی فرودین و لنونی: جست و خیز
چم این واژه در زبان لیتوانی: فراری
چم این واژه در زبان پروسی کهن: شلوار ۰
[pdf page 454]
1
لیسیدن, لشتن / ۴۵۵
| پم‌انکایسی سرواژای نارس ۹
اوستایی (4۲837/400): ۸۸۹2۸۲78 8۸82 انگلیسی (8۸701/54): 1
پارسی باستان (۳87401 صا0): هلندی (017677): 1
ولا ۸7 19137۸3۷* ان اسلاوی کهن (10/ا5 70761 0):
پهلری (14۲7لم۳۸): ۰ 87۸0۲] ,138717۸ 0 ,172۸7
کردی (99ا0820: ۰ 8718لل۸ ,112قشله سای (۷تقلزه: 11733805 12۸6
سانسکریت (7ل54۸5): روسی (/(۸ا85لا): ند وی
7 ,اش دتانا 111۸7 صربی (/55781۸2): 1171
ارمنی (4ط4/8۷4): ۰ 112826 ,112119 بوهمی (1ف3078(41): 11
=== find printed 69 and 455 ===
1931:[pdf page 68]
1958:[pdf page 69]
1989:[pdf page 70]
13477:[pdf page 454]
13506:[pdf page 455]
13543:[pdf page 456]
13573:[pdf page 457]
```


## [2026-09-06T23:02:35.212Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '1932,1960p' ARY_pages.txt\necho \"======\"\nsed -n '13478,13508p' ARY_pages.txt"
}
```


### [2026-09-06T23:02:35.265Z] TOOL RESULT

```
نج
آلیز آلیزیدن» آلیختن(به چم *جفتک انداختن») / ۶۹
کردی (015): 85-18571011 ,ل#13ا1 لیتوانی (/(م/ههنا بل 7ال): ,شا
سانسکریت (887۸758:)54۸43777 ب8۸[۸71 کشا
بونانی 08570): زیم 8 ایرلندی (37ل#)): 06
گونیکه (00777/0): قالش رالشاتشآ برتونی (886700): ره
ایسلندی کهن ((۷210۸/14(م5 ا0):
3 ادها پسگشت‌ها شنت دی
آلمانی کهن (05724۸ 10لا صا0): ۸008
1 مالقا 6 :۸045 ۸ لها
آلمانی ( م7( 025). ۱۳1 برهان قاطع : ۵۸
انگیسی کهن (57/ا800 صا0): 16 لفت‌نامه دهخدا: اند
نها
بادداشت: ۱
معنی این واژه در کردی؛ بازی,
معنی این واژه در ایرلندی: گرساله, :
معنی این واژه در گوتیکه: جست و خیز کردن» رقصیدن.
معنی اين واژه در انگلیسی کهن و آلمانی کهن؛ پریدن.
معنی این واژه در آلمانی:(ماهی) تخم ریزی کردن» بچه آوردن,
معنی این واژه در سانسکریت: لرزیدن.
سانسکر بت (8۸(/50/7): ۳ رومانی (0۸4۸1۸۸): ه ۸
لانین (710): ,۸1۸778۸ بشآ۸1۸780 آلمانی کهن (05724۸2 ۲۲۵07 0ل۵):
اناد با پدبا با ۰ 11828۸
فرانسه (۳6۸/2/7)+ ده ان انگلیسی کهن (34ا۷0ل8 طا: 11۸۳306
اسپانیایی (4ل62۸//3): ۸2۸ انگلیسی (87لا8۸0): وش انا
ابتالیایی (2ال7۸): ۸۸ اسلاوی کهن (عآلاها5 7707 ص0):
[pdf page 69]
0 پسگشت‌ها انشهیدت دید
روسی (805540۷): 1۸7116۸ 0 20000
======
1
لیسیدن, لشتن / ۴۵۵
| پم‌انکایسی سرواژای نارس ۹
اوستایی (4۲837/400): ۸۸۹2۸۲78 8۸82 انگلیسی (8۸701/54): 1
پارسی باستان (۳87401 صا0): هلندی (017677): 1
ولا ۸7 19137۸3۷* ان اسلاوی کهن (10/ا5 70761 0):
پهلری (14۲7لم۳۸): ۰ 87۸0۲] ,138717۸ 0 ,172۸7
کردی (99ا0820: ۰ 8718لل۸ ,112قشله سای (۷تقلزه: 11733805 12۸6
سانسکریت (7ل54۸5): روسی (/(۸ا85لا): ند وی
7 ,اش دتانا 111۸7 صربی (/55781۸2): 1171
ارمنی (4ط4/8۷4): ۰ 112826 ,112119 بوهمی (1ف3078(41): 11
یرنانی 0882/0): ۰ 116330 ,181077810 اسلواکی 81.07490): ول ۱
لاتین (7100ل): لیترانی ((4ا(هنا 7 7ا):
30 ,116183785 ,11۳6585 0 با 155۲۲۲
فرانسه (//۳7/2۸): 1 لتونی (لنی) (/47۳4): 132710 ,217لشآ
ایتالپایی (0غلله7): 1 ایرندی کهن (84ل#ا 2ا0): 11 :
رومانی (27ا 1۸4۸۸ #): دای ۹
پرتغالی (ظ۳0/7170188): 1 پسگشت‌ها 5
گونیکه (0077110): 2117 ۳۳ ۱
ایسلندی کهن ((54(70/0۸۸ ضا0): 3 (11۳6) +7 لفط ۱
51۸ 6 (۸0388) م۸2
ساکسونی کهن (/(54200 ۰:01 1216608 207 2
آلمانی کهن (/027040 07 ]با 2ا0): 6 (۲360) :0/105
: ۲ 10 9 (16ا) +7
ات آلمانی 084490): ۰ 10 برهان قاطع : ۹۵
انگلیسی کهن سماامیم: نات
اوستایی (4837(۷): ۸73۸۸ ,۸17۸1۸1488 پهلو: ی (اامابزهم: 8۸۸۸ بقلقال۸ مقاق۸ه
پارسی پاستان (4(۷اق۶87 ۵12): ۰ ۸۱/25۸ اوستی (03387/6): 1۸
[pdf page 455]
۶ | ملد
کردی (7ل60(15): هلا ,۵۳۵ ,28 انگلیسی کهن (8۸01/3/1 صا0): 18
```


## [2026-09-06T23:02:48.189Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"l[iī]stan[^]]\\{0,60\\}\" PHD.txt PHD_mackenzie.txt | head\necho \"--- NYB ---\"\ngrep -o \"l[iī]stan[^ ]\\{0,40\\}\\|lick[^ ]\\{0,20\\}\" NYB_vol2_glossary.txt | head\necho \"--- NYB lys ---\"\ngrep -n \"lecken\" NYB_vol2_glossary.txt | head\necho \"--- FRS لیسیدن/لشتن ---\"\ngrep -n \"لشتن\\|ليشتن\\|لیشتن\" FRS.txt FSF.txt | head"
}
```


### [2026-09-06T23:02:49.918Z] TOOL RESULT

```
--- NYB ---
licking
listan
listan
--- NYB lys ---
--- FRS لیسیدن/لشتن ---
```


## [2026-09-06T23:02:52.139Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"listan\" NYB_vol2_glossary.txt | head\necho \"---\"\ngrep -n \"licking\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-06T23:02:52.198Z] TOOL RESULT

```
4525:Zavalistan [z’w’lst’n'] country in Eastern Iran, Arab Zäbulistän, Yagut 2,904 sq.; it extended from Balkh in the north, and
4527:Zavalistan
---
2265: kiitak [k'tk'] game, frolicking 522°. — Arm- lw. katak; from Av. (462) ka- ‘to desire’, pt. käta-; v. Benveniste, TPhS 1945, 73; Bailey BSOAS XIII, 1950, 396, n.
```


## [2026-09-06T23:02:58.043Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"l[iīı]s-[^]]\\{0,50\\}\\|lick[^a-z][^]]\\{0,40\\}\" PHD.txt | head -10\necho \"--- index 'lick' ---\"\ngrep -o \"lick[^A-Za-z][^.]\\{0,60\\}\" PHD.txt PHD_mackenzie.txt | head -10"
}
```


### [2026-09-06T23:02:59.973Z] TOOL RESULT

```
lis- tag.
--- index 'lick' ---
```


## [2026-09-06T23:03:06.169Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^loig\\|^leig- (1)\\|^leig- (3)\\|^laikō\\|^laika\" IEC.txt | head -10\necho \"--- IEC context 9560-9585 ---\"\nsed -n '9560,9585p' IEC.txt\necho \"=== SYN leap/jump ===\"\ngrep -n \"10.43 LEAP\\|LEAP (vb\" SYN.txt | head"
}
```


### [2026-09-06T23:03:06.241Z] TOOL RESULT

```
9968:loigo, io (1) “jump, dance, play’. WP II, 399 Skt. réje, mp. (jump; sway”, w. secondary j = č); Go. laikan “jump, dance, play’; MHG lei- chen, id. (and “mount; hoax'); OE lacan, sv. 7, pf. leolc: Go. (unrecorded) *lailaik “bob, leap, fly, play, fight; ON leika “play, dance, hoax’; Sw. leka ‘play; mate”; Li. láigyti, inf. ‘frolic, rampage’. LW in Finn. loikkia “leap? beside leikkiä ‘play’. Noun forms: Go. laiks, OHG leihh; MHG leich, sm. ‘tune’; ge-leich, n. (3) ‘hoax’; OE làc, f.; OFris. lek; Sw. lek; ON leikr, m. ‘game’; leik, pl. -u, n. ‘toy’; Finn. LW leikki
9969:loigo- (2) *evil'. Cf. lig-, (olig-). WP II, 398 Per. riy “hate, malice" (ambig. cf. uroig-); Gk. loigós, m. 'destruction, death, evil, pla- gue’; OE lac, f. ‘strife, battle; sacrifice; MHG geleich (2) ‘setback’; Li. cf. pá-liegis, io, m. “Invalid, sick person’ beside liegstu, liegti "be seriously ill’. Cf. also OE cpd. ag-læc “distress?
9973:loigó, ið — loiquno-
--- IEC context 9560-9585 ---
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
leidhos
leib- — leil-
10
15
20
25
30
35
40
45
672
leigho, io ‘lick’. (Variant of type leig- (1), q. v.). Cf. WP II, 400 Skt. ledhimi, lidhemi, id.; Gk. leikho, id. (Sl. Celt. & Balt. ambig.), cf. (infixed) Lat. lingo, Gre Ir. (zero-gde) lighim; W Ilyaf; MHG l&cken, id. (from *lig-. W & Ir. ambig.) See next
leiguis, leiĝus ‘tongue’. WP I, 792, cf. also II, 400. See leig- (1), lig- Arm. lezu, gs lezvi, absg lezvav, id.; Ararat Arm. lizu, id.; OIr. & mod. Ir. liag, f. ‘spoon’; W llwy, f. id.; Cz. liz, gs -u, m. 'salt-lick'; Big. cf. lézvije 'knife-blade, cutting-edge'; Li. liežuvis, gs -io, m. ‘tongue’; Latv. cf. lize *baker's peel (*-i-)
leiio, leió “pour, cast’. Cf. leið (1) and hio LLat. lio, are tr. («liquefy'. Classical liare *smooth, paste? is of ambig. origin); Ir. cf. lia, dp liaibh, m. ‘downpour’; W lli, pl. -on, s. ‘flood’; OCS lějọ, inf. lijati (pour, cast’, and com. Sl); Li. liejü, ben ‘pour, shed”; Latv. leju, liet, id.; cf. lējums, m. *outpour, down- pour” beside list, 3s., inf. Iit, v. ‘rain’. Uncer- tainly to Arm. tey, o-st. Cdownpour, if for *de-lei- ? Cf. teyaj, v. 3s “it rains")
leikos, om, iom “turn, feature, face'. (Seman- tics of volutum: vultus, cf. also It. volta “time, turn") W llwyg, pl. -au, od m. ‘turn’; denom. vb. IIwygo, inf. id.; Srb. lik ‘form, image’ beside lice, n. ‘face’; OCS lices-, cpds. id. beside likü-, in cpds. likü-stviti, v. ‘jump’; likü-stvije, n. "dance": Cz. lice, R licó “face”
=== SYN leap/jump ===
17371:688 SELECTED INDO-EUROPEAN SYNONYMS 10.48 JUMP, LEAP (vb.)
```


## [2026-09-06T23:03:22.956Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyg-",
 "prompt": "Is there a PIE root *leyg- meaning \"to jump, hop, shake, tremble\"? Give its gloss and descendants (Proto-Germanic, Indo-Iranian, Persian)."
}
```


## [2026-09-06T23:03:24.649Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%84%DB%8C%D8%AE%D8%AA%D9%86",
 "prompt": "Is there an entry for Persian آلیختن (ālēxtan)? Give etymology and meaning if present."
}
```


### [2026-09-06T23:03:28.246Z] TOOL RESULT

```
# Proto-Indo-European Root *leyg-

Yes, there is a PIE root **\*leyg-** with multiple related meanings.

## Primary Gloss
The root carries these senses: "to jump around, run around; to play, frolic; to shake, jitter; to dance."

## Key Descendants

**Proto-Germanic:**
- \*laikaną (from the o-grade form \*lóyg-e-ti)

**Proto-Indo-Iranian:**
- \*ráyǰati, which develops into Sanskrit réjati/réjate

**Persian:**
- آلیختن (âlixtan), via the Proto-Iranian form

The documentation notes that "to shake, jitter" forms connect semantically with dancing, while the "jump" and "frolic" meanings show related conceptual territory across descendant languages.
```


### [2026-09-06T23:03:29.813Z] TOOL RESULT

```
# Persian آلیختن (ālēxtan)

Yes, there is an entry for this Persian verb.

**Etymology:** The word derives from Proto-Indo-European *lig-e-ti, from the root *leyg- meaning "to jump, play." It shares cognates with Northern Kurdish lîstin, Lithuanian láigyti, and Swedish leka.

**Meanings:** The verb has two primary definitions:
1. "to leap"
2. "to kick"

The present stem is **آلیز** (âliz), and it's pronounced /ʔaː.leːx.ˈtan/ in Classical Persian.
```


## [2026-09-06T23:03:39.744Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/lark' --note 'page 306, root Leig, English lark <- ON leika, PIE *leig- \"to leap\"' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%84%DB%8C%D8%B3%DB%8C%D8%AF%D9%86' --note 'page 306, root Leigh 1, Persian lisidan; alt forms لستن/لشتن/لیشتن; PIE *leyǵʰ-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ley%C7%B5%CA%B0-' --note 'page 306, root Leigh 1 = PIE *leyǵʰ- \"to lick\"' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/laikan%C4%85' --note 'page 306, root Leig, Germanic laik = PGmc *laikaną' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyg-' --note 'page 306, root Leig = PIE *leyg- \"to jump, play\"' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A2%D9%84%DB%8C%D8%AE%D8%AA%D9%86' --note 'page 306, root Leig, Persian alixtan, present stem aliz' 2>&1 | tail -3"
}
```


### [2026-09-06T23:03:43.899Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e94aed14d9e6ade3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/131f4997202a8721.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/00249560f9f9e9e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65a91f8adffab6b4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/66d69d6e359070b2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/247fd36c62d505bc.txt
```


## [2026-09-06T23:03:48.046Z] TOOL CALL #45: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-06T23:03:48.094Z] TOOL RESULT

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


## [2026-09-06T23:09:00.935Z] TOOL CALL #46: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-306.json <<'JSONEOF'\n{\n  \"pdf_page\": 306,\n  \"book_page\": 276,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Leig\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *leyg- / *loyg- 'to jump around, hop, shake, tremble; to play, dance'\",\n      \"note\": \"Pokorny I 667 sets up '3. leig-, loig- \\\"hüpfen, beben; beben machen\\\"' and lists under it exactly the two branches Nourai draws: 'npers. ālextan \\\"springen, ausschlagen (vom Pferde)\\\", kurd. be-lezium \\\"tanze\\\", līzim \\\"spiele\\\"' and 'got. laikan (lailaik) \\\"hüpfen, springen\\\", laiks \\\"Tanz\\\", anord. leika \\\"spielen\\\"'. Watkins/AHD has the same root as 'leig-3. To leap, tremble. O-grade form *loig- in Germanic *laik-' with the explicit derivative LARK(2) from Old Norse leika. Language label 'Indo-European' and the gloss 'to leap, jump' are both right; the fuller gloss also covers 'shake, tremble' (Skt. rejati 'macht hüpfen, lässt erbeben'), which is the sense that ties the Indo-Aryan forms in. The one caveat, raised by Cheung 2007 (*raiz2 ? 'to jump'), is that the Iranian branch is attested only in modern West Iranian and its IE provenance is 'conceivable, but difficult to establish'.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *leyg-/*loyg- به معنی «جَستن، جفتک انداختن، لرزیدن، بازی کردن» است. پوکورنی (ص ۶۶۷، مدخل «3. leig-, loig-») همین دو شاخه‌ای را که نورایی رسم کرده زیر این ریشه آورده است: از سویی فارسی «آلیختن» (springen, ausschlagen vom Pferde) و کردی lîzim «بازی می‌کنم»، و از سوی دیگر گوتی laikan «جستن» و نورس کهن leika «بازی کردن». واتکینز نیز در پیوست ریشه‌های هندواروپایی همین ریشه را با همین معنی و با اشتقاق انگلیسی lark آورده است. پس نامِ ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است؛ تنها تذکار امروزی از آنِ چونگ (۲۰۰۷) است که شاخهٔ ایرانی را تنها در زبان‌های ایرانی نو یافته و اثبات هندواروپایی‌بودن آن را دشوار می‌داند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyg-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/laikan%C4%85\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:667\", \"status\": \"supports\", \"note\": \"POK_02.txt \\\\f-block 328 (printed p.667, running head '667' precedes the entry): '3. leig-, loig- \\\"hüpfen, beben; beben machen\\\". Ai. rijati \\\"macht hüpfen, läßt erbeben\\\" ... npers. ālextan \\\"springen, ausschlagen (vom Pferde)\\\" ... got. laikan (lailaik) \\\"hüpfen, springen\\\", laiks \\\"Tanz\\\" ... WP. II 399'. Exactly Nourai's root, gloss and both daughters.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p.399 (WLD_Bd2_pages.txt leaf 404)\", \"stance\": \"supports\", \"note\": \"'3. leig-, loig- \\\"hüpfen, beben; beben machen\\\". Ai. rejati ... npers. alīxtan \\\"springen, ausschlagen (vom Pferde)\\\", kurd. be-lesnim \\\"tanze\\\", līzim \\\"spiele\\\"' — Pokorny's source text, same content.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. leig-3 (AHD_watkins1985.txt line 671)\", \"stance\": \"supports\", \"note\": \"'leig-3. To leap, tremble. O-grade form *loig- in Germanic *laik- in: a. Old English -lāc ...: WEDLOCK; b. Old Norse leika, to play: LARK2. [Pok. 3. leig- 667.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. loigo, io (1) (IEC.txt line 9968)\", \"stance\": \"partial\", \"note\": \"'loigo, io (1) \\\"jump, dance, play\\\". WP II, 399. Skt. rēje ... Go. laikan \\\"jump, dance, play\\\"; OE lācan; ON leika \\\"play, dance\\\" ... Li. láigyti' — the Germanic side confirmed; Mann lists no Persian form under this root.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"s.v. *raiz2 ? 'to jump' (CHEUNG.txt line 20447)\", \"stance\": \"partial\", \"note\": \"'*raiz2 ? \\\"to jump\\\" ... (+ *ā-) NP alēxtan/alēz- \\\"to jump, kick out\\\", Khor. alij, aliz \\\"jumping up of animals\\\" ... A connection with Goth. laikan \\\"to jump, hop\\\", OE lācan ... is mentioned by Lehmann 1986: 225a ... PIE ? LIV: 405 | Pok.: 667 f.' — same route, but Cheung marks the root itself doubtful.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"âlîzîdan «آلیزیدن»; âlîz «آلیز»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The old verb is NP ālēxtan (آلیختن), pres. stem ālēz-/ālīz- (آلیز), 'to leap, to kick out (of a horse)' — Old Iranian *ā- 'up, out' + a stem *laiz-/*raiz- 'jump', with the regular Middle→New Persian change *-z-t- > -xt in the past stem (like rēxtan : rēz-). آلیزیدن and آلیزدن are the expected late Persian re-formations of the infinitive on the present stem ālīz- (exactly as لیسیدن is built on لیس-), and آلیزش is the verbal noun in -iš; the noun آلیز 'a jumping/kicking horse' is the bare present stem used as an agent noun. Pokorny 667 cites 'npers. ālextan \\\"springen, ausschlagen (vom Pferde)\\\"' under leig-, and Wiktionary gives آلیختن (present stem آلیز) 'to leap, to kick' from PIE *leyg-, cognate with Kurmanji lîstin and Swedish leka, so the arrow root→Persian is the standard view. The reservation is Cheung 2007, who files these forms under a query-marked *raiz2 '?to jump' known only from modern West Iranian (Kurdish listin/lîz-, Khorasani alij/aliz) and warns that the initial l- is 'rather atypical for an Ir. word' and that an IE provenance is 'difficult to establish'. Nourai's gloss 'to jump around' is a little loose: Borhan-e Qāṭeʿ and Moʿin define آلیزدن/آلیزیدن specifically as جفته/جفتک انداختن, a beast kicking out with its hind legs, which is also Pokorny's 'ausschlagen (vom Pferde)'.\",\n          \"derivation_fa\": \"فعل کهن «آلیختن» است با ستاک حال «آلیز»، به معنی «جفتک انداختن، برجَستن (ستور)»؛ از ایرانی باستان *ā- (پیشوند «بر، بیرون») + ستاک *laiz-/*raiz- «جَستن». دگرگونی آوایی -z-t- به -xt در ستاک گذشته همان قاعدهٔ آشنای فارسی است (مانند ریختن : ریز-). «آلیزیدن» و «آلیزدن» مصدرهای نوساختهٔ فارسی دری‌اند که بر ستاک حال آلیز- ساخته شده‌اند (درست مانند «لیسیدن» بر «لیس-»), و «آلیزش» اسم مصدر با پسوند -ِش است؛ «آلیز» نیز همان ستاک حال است که در معنی «اسب جفتک‌انداز» به کار رفته. پوکورنی (۶۶۷) و والده-پوکورنی (ج۲ ص۳۹۹) و آریان‌پور (ص۶۹) و ویکی‌واژه همگی این واژه‌ها را زیر همین ریشه آورده‌اند، پس ادعای نورایی با احتیاط پذیرفتنی است؛ اما چونگ (۲۰۰۷) ریشهٔ ایرانی *raiz² «جستن» را با علامت پرسش می‌آورد و می‌گوید شواهد آن تنها از زبان‌های ایرانی نوِ غربی است و «ل» آغازین برای واژه‌ای ایرانی نامعمول است. یادآوری: معنی دقیق واژه در برهان قاطع و معین «جفته/جفتک انداختن» است، نه صرفاً «این‌سو و آن‌سو جستن».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D9%84%DB%8C%D8%AE%D8%AA%D9%86\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leyg-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:667\", \"status\": \"supports\", \"note\": \"POK_02.txt \\\\f-block 328 (p.667), under '3. leig-, loig-': 'npers. ālextan \\\"springen, ausschlagen (vom Pferde)\\\", kurd. be-lezium \\\"tanze\\\", līzim \\\"spiele\\\"'. Pokorny gives the ā-prefixed verb, i.e. the source of Nourai's āliz-.\"},\n            {\"ref\": \"BQT:59\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt \\\\f-block 269 = printed p.59 (offset leaf−210 verified here): 'آلیزدن و آلیزیدن - جفته افکندن، جفتک انداختن: نفس چون سیر گشت بستیزد ـ توسن‌آسا بهر سو آلیزد. سراج‌الدین' — the headword, the gloss and the very verse Nourai prints. No etymological footnote of Moʿin's attaches to it.\"},\n            {\"ref\": \"MON:86\", \"status\": \"partial\", \"note\": \"The 6-vol Amir Kabir Farhang-e Fārsi is not online, so the page cannot be checked; the 2-vol Adena condensation (MON_part1.txt lines 4553-4568) has 'آلیختن [= آلیزیدن] (مص‌ل.) (آلیخت، آلیزد، خواهد آلیخت... آلیزش) ... جفتک، جفته، لگد پرانیدن ستور با دو پای از عقب. جستن، رمیدن' and separate entries آلیزش, آلیزیدن — the words and glosses are Moʿin's, the page number is unverifiable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.399\", \"stance\": \"supports\", \"note\": \"'npers. alīxtan \\\"springen, ausschlagen (vom Pferde)\\\", kurd. be-lesnim \\\"tanze\\\", līzim \\\"spiele\\\"' under 3. leig-, loig-.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *raiz2 ? 'to jump' (CHEUNG.txt line 20447)\", \"stance\": \"partial\", \"note\": \"'(+ *ā-) NP alēxtan/alēz- \\\"to jump, kick out\\\", Khor. alij, aliz \\\"jumping up of animals\\\"'; but 'The evidence for this root is limited to some modern WIr. languages ... An IE provenance ... is conceivable, but difficult to establish.'\"},\n            {\"src\": \"ARY\", \"where\": \"p.69 (ARY_pages.txt, block tagged [pdf page 68]/[pdf page 69])\", \"stance\": \"supports\", \"note\": \"Headword 'آلیز، آلیزیدن، آلیختن (به چم «جفتک انداختن») / ۶۹' with cognate columns Kurdish lîstin/be-lezim, Lithuanian, Sanskrit, Gothic, Old Icelandic, Old English, Old High German, and the note 'معنی این واژه در گوتیکه: جست و خیز کردن، رقصیدن' — an independent modern Persian handbook grouping exactly as Nourai does; it cites برهان قاطع ص۵۸.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. loigo, io (1)\", \"stance\": \"silent\", \"note\": \"Mann lists the Germanic, Sanskrit and Lithuanian material but no Persian ālēxtan.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Germanic\",\n          \"words\": \"laik\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *laikaną 'to jump, play, move, swing about' — the o-grade *loyg-e-ti of the root, with the regular Grimm shift *g > k. It is a strong class-7 verb with reduplicated preterite (*lelaik), whence Gothic laikan (pret. lailaik) 'to leap, dance', Old Norse leika 'to play', Old English lācan 'to move quickly, play, fight', Old High German leih 'melody, lay' (noun *laikaz > Gothic laiks 'dance', ON leikr 'game'). Nourai's citation form 'laik' is the bare Germanic stem rather than a full infinitive, but the form and gloss are right.\",\n          \"derivation_fa\": \"صورت ژرمنی آغازین *laikaną «جستن، بازی کردن، جنبیدن» است که از درجهٔ o ریشه (*loyg-e-ti) ساخته شده؛ g هندواروپایی بنا بر قانون گریم در ژرمنی به k بدل شده است. این فعل از دستهٔ قوی ردهٔ ۷ با ماضی مضاعف (*lelaik) است و بازماندگان آن گوتی laikan «جَستن، رقصیدن»، نورس کهن leika «بازی کردن»، انگلیسی کهن lācan و اسم‌های گوتی laiks «رقص» و نورس leikr «بازی» است. نورایی صورت را کوتاه‌شده «laik» نوشته که همان ستاک ژرمنی است نه مصدر کامل؛ اما صورت و معنی درست است و پوکورنی و واتکینز هر دو آن را تأیید می‌کنند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/laikan%C4%85\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:667\", \"status\": \"supports\", \"note\": \"POK_02.txt p.667-668: 'got. laikan (lailaik) \\\"hüpfen, springen\\\", bi-laikan \\\"verspotten\\\", laiks \\\"Tanz\\\", anord. leika (lek) \\\"spielen\\\" ... ags. lācan \\\"sich schnell bewegen, spielen, fechten\\\", läc \\\"Spiel, Kampf\\\" ... ahd. leih, leich \\\"Spiel, Melodie\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leig-3\", \"stance\": \"supports\", \"note\": \"'O-grade form *loig- in Germanic *laik- in: a. Old English -lāc ...; b. Old Norse leika, to play'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. loigo, io (1)\", \"stance\": \"supports\", \"note\": \"'Go. laikan \\\"jump, dance, play\\\"; MHG leichen; OE lācan, sv. 7, pf. leolc ... ON leika \\\"play, dance\\\" ... Noun forms: Go. laiks, OHG leihh ... ON leikr, m. \\\"game\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.400\", \"stance\": \"supports\", \"note\": \"'daher muß idg. *loig- angesetzt werden und wird germ. laikan wohl ... Perfekt-, bzw. Iterativvokalismus ins Praesens verschleppt haben.'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"lark\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The 'frolic' noun lark (1811, first as sailors' and street slang) is standardly derived from northern English dialectal lake/laik 'to play, frolic' (Middle English laike), a Norse loan from Old Norse leika = Germanic *laikaną, with an intrusive -r- of the type found in southern English spellings of dialect words. Watkins/AHD states this route outright, listing LARK(2) under leig-3 via 'Old Norse leika, to play'. Etymonline, however, calls the word 'of uncertain origin' and prefers, or at least allows, a shortening of skylark (1809), the sailors' term for playing about in the rigging; the OED likewise leaves it open. So the arrow Germanic laik → English lark is the AHD view, not a settled one. Note also that this is a different word from lark 'the songbird' (OE lāwerce, PGmc *laiwarikōn), whose origin is unknown and unconnected.\",\n          \"derivation_fa\": \"واژهٔ lark به معنی «شیطنت، خوش‌گذرانی، ماجراجویی بی‌خیال» نخستین بار در ۱۸۱۱ در زبان عامیانهٔ ملوانان و کوچه‌وبازار انگلیسی دیده می‌شود. ریشه‌شناسی رایج آن را از گویشیِ شمال انگلستان lake/laik «بازی کردن» می‌داند که خودْ وام‌واژه‌ای است از نورس کهن leika، یعنی همان *laikaną ژرمنی؛ «ر» میانی افزودهٔ گویش‌های جنوبی است. واتکینز در پیوست ریشه‌های هندواروپایی همین راه را قطعی می‌گیرد و LARK را زیر leig-3 از نورس leika می‌آورد. اما اتیمآنلاین و فرهنگ آکسفورد ریشه را «نامطمئن» می‌خوانند و احتمال کوتاه‌شدن skylark (۱۸۰۹، اصطلاح ملوانان برای بازی در طناب‌های کشتی) را نیز پیش می‌کشند. پس پیکان «ژرمنی laik ← انگلیسی lark» دیدگاه واتکینز است و پذیرفتنی، ولی نه اجماعی. ناگفته نماند که این واژه با lark «چکاوک» (انگلیسی کهن lāwerce) که ریشه‌اش ناشناخته است هم‌ریشه نیست.\",\n          \"sources\": [\"https://www.etymonline.com/word/lark\"],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the node carries no citation in the book; Nourai's source for the arrow is evidently AHD, whose leig-3 entry lists LARK2 among the derivatives.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leig-3 and the English index (AHD_watkins1985.txt line 671)\", \"stance\": \"supports\", \"note\": \"'b. Old Norse leika, to play: LARK2. [Pok. 3. leig- 667.]'\"},\n            {\"src\": \"WEB\", \"where\": \"Etymonline s.v. lark (n.2), used as the modern proxy\", \"stance\": \"partial\", \"note\": \"'1811, of uncertain origin ... perhaps a shortening of skylark (1809), sailors' slang for \\\"play rough in the rigging\\\" ... or a dialectal survival of lake/laik \\\"to play, frolic\\\", from Old Norse leika, from PIE *leig- (3) \\\"to leap\\\"'. Same chain offered, but as one of two options.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt, grepped '^LARK', 'Lark,'\", \"stance\": \"silent\", \"note\": \"Skeat's Concise has no separate entry for lark 'frolic' in this OCR (the 1911 text treats only the bird).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Leigh 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *leyǵʰ- (also *sleyǵʰ-) 'to lick'\",\n      \"note\": \"Pokorny I 668: 'leigh-, sleigh- \\\"lecken\\\"; Präsens leigh-mi. Ai. lēḍhi, rēḍhi, lihati \\\"leckt\\\" ... av. 3. Pl. raēzaite \\\"sie lecken\\\", np. līstan \\\"lecken\\\" ... got. bilaigōn \\\"belecken\\\"; ablaut. geminiert ags. liccian, ahd. lecchōn, as. likkon \\\"lecken\\\"'. Watkins/AHD s.v. leigh- 'To lick' [Pok. leigh- 668] and Klein s.v. lick ('I.-E. imitative base *leigh-') give the same root; Buck 4.59 LICK (p.267) lists 'IE *leigh-. Walde-P. 2.400' with Av. raēz- in the table. Nourai's root name, language label ('Indo-European') and gloss are all correct, and the numeral '1' distinguishes it from Pokorny's homophonous leiĝh- entries. The Persian and Sogdian branches are known in modern Iranian scholarship as Proto-Iranian *raiz- 'to lick' (Cheung 2007), with an unexplained but pan-Iranian l- for r- in the western forms.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *leyǵʰ- (با گونهٔ آغازینِ s-دار *sleyǵʰ-) به معنی «لیسیدن» است؛ پوکورنی آن را در صفحهٔ ۶۶۸ آورده و می‌نویسد: «سنسکریت lēḍhi/lihati، اوستایی raēzaite (سوم شخص جمع)، فارسی نو līstan، گوتی bilaigōn، انگلیسی کهن liccian». واتکینز، کلاین (ذیل lick) و باک (بخش ۴٫۵۹ ص۲۶۷) نیز همین ریشه را با همین معنی می‌آورند. بنابراین نام ریشه، برچسب «هندواروپایی» و معنای «لیسیدن» در نمودار نورایی درست است و شمارهٔ ۱ آن را از ریشه‌های هم‌آوای دیگر جدا می‌کند. در ایران‌شناسی امروزی این ریشه به صورت ایرانی آغازین *raiz- بازسازی می‌شود (چونگ ۲۰۰۷) و بدل شدن r آغازین به l در شاخهٔ غربی هنوز توضیح قطعی ندارد.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ley%C7%B5%CA%B0-\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:668\", \"status\": \"supports\", \"note\": \"POK_02.txt \\\\f-block 329 (printed p.668, the numeral '668' stands at the head of the block): 'leigh-, sleigh- \\\"lecken\\\"; Präsens leigh-mi. Ai. lēḍhi, rēḍhi, lihati \\\"leckt\\\", lehá- m. \\\"Lecker\\\", av. 3. Pl. raēzaite \\\"sie lecken\\\", np. līstan \\\"lecken\\\" ... WP. II 400 f.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p.400 (WLD_Bd2_pages.txt leaf 405)\", \"stance\": \"supports\", \"note\": \"'leigh- \\\"lecken\\\". Ai. lēḍhi, rēḍhi, lihati \\\"leckt\\\", lehá- m. \\\"Lecker\\\", av. 3. pl. raēzaite (Bartholomae IF. 5, 369) \\\"sie lecken\\\", np. līštan \\\"lecken\\\" (usw., s. Bartholomae Airan. Wb. 1485)' — note WP prints the Persian as līštan, Nourai's very form.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leigh- (AHD_watkins1985.txt line 671)\", \"stance\": \"supports\", \"note\": \"'leigh-. To lick. 1. Greek leikhein ... 2. Zero-grade form *lig- in Germanic *likkōn ... [Pok. leigh- 668.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann s.v. leigho, io 'lick' (IEC.txt line 9582)\", \"stance\": \"supports\", \"note\": \"'leigho, io \\\"lick\\\". (Variant of type leig- (1)). Cf. WP II, 400. Skt. lēḍhmi, lihémi; Gk. leikho; Lat. lingo; Ir. lighim; MHG lecken.'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 4.59 LICK, p.267 (SYN.txt line 6882)\", \"stance\": \"supports\", \"note\": \"'IE *leigh-. Walde-P. 2.400 ... Skt. lih-, rih-, Av. raēz-; Arm. lizum, lizanem' with the language table listing 'Av. raēz-' and 'Skt. lih-'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"leiš, raěz, rěh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Only the middle form is really Avestan. Bartholomae, Altiranisches Wörterbuch col. 1485, has 'j. raēz- V. \\\"lecken, leckend verzehren\\\", Praes. 1 rau-', attested in the Nirangistan passage 'daēva *raēzaite' (\\\"the daevas lick up whatever drips and is spilled\\\"); Cheung 2007 cites the same verb as Young Avestan riz- with the middle intensive present (ā)raērizaite (N 68). So 'raěz' is correct, with the expected Avestan diphthong ai > aē before z from *raiz-. 'rěh' is not Avestan but Sanskrit/Old Indic: Horn (Grundriss no. 954) writes 'ai. √reh-, rehmi; skr. leh-, lehmi \\\"ich lecke\\\"', and Bartholomae in the same column adduces 'ai. rēḍhmi, liḍhmi'. 'leiš' is likewise not an Avestan word: it is Nourai's rendering of the s-extended stem that Horn set up as 'ap. √*lais- (√leiĝh- + s)' — precisely the reconstruction Hübschmann (Persische Studien no. 954, p.96) rejected: 'Die Ansetzung eines ap. lais ist falsch'. The three forms are therefore a conflation of one Avestan, one Old Indic and one (rejected) Old Persian citation form under a single 'Avestan' label; the derivation of the box from the IE root is right, the labelling is not.\",\n          \"derivation_fa\": \"از سه صورتی که در این خانه زیر برچسب «اوستایی» آمده، تنها صورت میانی اوستایی است. بارتولومه در فرهنگ ایرانی باستان (ستون ۱۴۸۵) می‌آورد: «raēz- (اوستایی نو) به معنی لیسیدن، با لیسیدن خوردن»، با شاهدی از نیرنگستان (daēva raēzaite «دیوان آنچه را چکیده و ریخته است می‌لیسند»)؛ چونگ نیز همین فعل را با صورت riz- و ماضی نقلی میانهٔ (ā)raērizaite ثبت کرده است. دیفتونگ ai ایرانی باستان در اوستایی پیش از z به aē بدل شده، پس raēz- < *raiz- کاملاً منظم است. اما «rěh» اوستایی نیست، سنسکریت است: هرن (بند ۹۵۴) می‌نویسد «ai. √reh-, rehmi» و بارتولومه نیز «rēḍhmi, liḍhmi» را می‌آورد. «leiš» هم اوستایی نیست؛ همان ستاک s-دار است که هرن آن را «پارسی باستان *lais- (از √leiĝh- + s)» بازسازی کرد و هوبشمان در «مطالعات فارسی» (بند ۹۵۴، ص۹۶) صریحاً ردش کرد: «فرض کردن ap. lais نادرست است». پس پیوند این خانه با ریشهٔ هندواروپایی درست است، ولی برچسب «اوستایی» بر هر سه صورت خطاست: یکی اوستایی، یکی سنسکریت و یکی بازسازی مردود پارسی باستان است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ley%C7%B5%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:668\", \"status\": \"partial\", \"note\": \"Pokorny p.668 has 'av. 3. Pl. raēzaite \\\"sie lecken\\\"' — supports raěz, but he gives the Sanskrit forms as 'ai. lēḍhi, rēḍhi, lihati' and has nothing corresponding to an Avestan 'leiš'.\"},\n            {\"ref\": \"KLN:886\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 21660 (the leaf whose running heads bracket pp. 885-886), s.v. 'lick, tr. and intr. v.': '... from the I.-E. imitative base *leigh-, whence also OI. lēḍhi, rēḍhi, also (a later form) lihati \\\"he licks\\\", Avestic raēz-, \\\"to lick\\\", Arm. lizum ...'. Klein has Av. raēz- exactly, and 'rēḍhi' as Old Indic, not Avestan.\"},\n            {\"ref\": \"SYN:267\", \"status\": \"supports\", \"note\": \"Buck p.267, section 4.59 LICK: the language table gives 'Skt. lih-' and 'Av. raēz-', and the discussion 'IE *leigh-. Walde-P. 2.400 ... Skt. lih-, rih-, Av. raēz-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1485 (BRT.txt \\\\f-block 812, running head 1486)\", \"stance\": \"supports\", \"note\": \"'j. raēz- V. \\\"lecken, leckend verzehren\\\". Praes. 1 rau-. vīspanąm ... daēva *raēzaite \\\"alles was (davon) abtrieft und verschüttet wird, (das) lecken die D. auf\\\" N. ... ai. rēḍhmi, liḍhmi \\\"ich lecke\\\", np. lēstan.' Also the footnote 'So, mit l, gegenüber np. līsad'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *raiz1 'to lick' (CHEUNG.txt line 20403)\", \"stance\": \"supports\", \"note\": \"'*raiz1 \\\"to lick\\\". AVESTAN: YAv. riz- \\\"to lick\\\"; MED. Intens.: pres. IND. 3sg. YAv. (ā)raērizaite (N 68) ... PIE *leigʰ- \\\"to lick\\\" | LIV: 404 | Pok.: 668.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.400\", \"stance\": \"supports\", \"note\": \"'av. 3. pl. raēzaite (Bartholomae IF. 5, 369) \\\"sie lecken\\\"'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no. 954, p.96 (HUB.txt \\\\f-block 106)\", \"stance\": \"contradicts\", \"note\": \"On the 'leiš' form: 'Die Ansetzung eines ap. lais ist falsch, durch die nachfolgende richtige Erklärung von np. lēsam auch überflüssig: idg. ligʰ = iran. ap. lis bildete den Inf. *listanaiy = np. listan, das Praesens *laizāmiy = np. *lēzam ...'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"rys\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Buddhist Sogdian rys- (i.e. rēš-) 'to lick', an inchoative present in -s- built on the Old Iranian stem *raiz-; Sogdian preserves the original r- that western Iranian replaced with l-, and Old Iranian *ai regularly gives Sogdian ē (written y). Gharib's Sogdian Dictionary no. 8654 sets it out with the etymology and the parallel Khotanese and Yaghnobi forms; the infinitive rysʼ(ty) and a plural rysyt- are attested in the Vessantara Jātaka (VJ 990) and the Vimalakīrtinirdeśa Sūtra fragment. So the arrow Avestan/Old Iranian → Sogdian is correct as a sister descent (Sogdian does not descend from Avestan, but from the same Old Iranian stem, which is how Nourai's charts uniformly use the Avestan box).\",\n          \"derivation_fa\": \"سغدی بودایی rys- (خوانش rēš-) «لیسیدن» است؛ ستاکی است با پسوند آغازیِ -s- که بر ستاک ایرانی باستان *raiz- ساخته شده. سغدی «ر» آغازین اصلی را نگه داشته، حال آنکه فارسی و کردی آن را به «ل» بدل کرده‌اند؛ نیز دوواکهٔ ai ایرانی باستان در سغدی به ē بدل شده و با y نوشته می‌شود. بدرالزمان قریب در «فرهنگ سغدی» (شمارهٔ ۸۶۵۴، ص۳۴۸) همین ریشه‌شناسی را می‌آورد و صورت‌های خُتنی rriś- و یغنابی les را کنار آن می‌گذارد؛ شاهدها از ویسنتره‌جاتکه (بند ۹۹۰) است. پس پیکان نمودار درست است، با این تصریح که سغدی فرزند اوستایی نیست بلکه خواهر آن است و هر دو از یک ستاک ایرانی باستان می‌آیند — همان قراردادی که نورایی در سراسر کتاب به کار می‌برد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ley%C7%B5%CA%B0-\"],\n          \"ref_check\": [\n            {\"ref\": \"SOD:348\", \"status\": \"supports\", \"note\": \"SOD_pages.txt \\\\f-block 415, whose printed page number 348 is stamped in the corner: entry '8654 rys- B ... rēs ©<*raiz-, Av. raēz-, Khot. rriś-, Yaghn. les ... (to) lick ... pl. rysyt- ... VJ 990; AVS 125'. Nourai's SOD:348 is the printed page and it says exactly what the arrow says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *raiz1 (CHEUNG.txt line 20403)\", \"stance\": \"supports\", \"note\": \"'SOGDIAN: BSogd. rys- (inch.) \\\"to lick\\\". Inf.: BSogd. rysʼty' — same form, same root, plus the label 'inchoative' for the -s- present.\"},\n            {\"src\": \"POK\", \"where\": \"p.668, s.v. leigh-\", \"stance\": \"silent\", \"note\": \"Pokorny cites Sanskrit, Avestan and New Persian for the Iranian side but no Sogdian.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"lîsîdan «لیسیدن»; lîštan «لیشتن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The inherited pair is لیشتن/لِشتن (līštan/leštan) 'to lick', past stem, beside the present stem لیس- (lēs-). Hübschmann (Persische Studien no. 954, p.96) gives the classic account, and it is the one Moʿin reprints verbatim in his footnote to Borhān-e Qāṭeʿ: Old Iranian *liz-/*laiz- formed the infinitive *listanaiy > NP listan and the present *laizāmiy > *lēzam, which was then remodelled to lēsam on the pattern of nivištan : nivēsam, giving the -s- of لیس-. Cheung 2007 confirms the Middle Persian stage from the books: BMP lys- /līs-/ 'to lick', pret. lyst /līst/, whence NP listan/lēs-, Kurdish (Sorani) lēsīn, listin/lēs-, Bakhtiari listan/lēs-. لیسیدن is then the ordinary late New Persian re-formation of the infinitive on the present stem (lēs- + -īdan), which is why it and not لیشتن is the living word. Abolqāsemi (Feʿl-hā-ye Fārsi-ye Dari p.76) states the same in Persian terms: لشت < Old Iranian *laiz-ta-, لیس < *raiz-a-, with r > l and z > s. The one point every source flags is the l- for expected r- (Av. raēz-, Sogd. rys-), which Cheung calls 'a notorious problem'; it does not affect the root assignment.\",\n          \"derivation_fa\": \"جفت اصیل این فعل «لیشتن/لِشتن» (ماضی) در کنار ستاک حال «لیس-» است. هوبشمان در «مطالعات فارسی» (بند ۹۵۴، ص۹۶) توضیح کلاسیک را داده و معین همان را عیناً در حاشیهٔ برهان قاطع نقل کرده است: ایرانی باستان *liz-/*laiz- مصدر *listanaiy ساخته که فارسی «لستن/لشتن» شده، و صورت مضارع *laizāmiy که باید *lēzam می‌شد، به قیاس «نوشتن : نویسم» به «لیسم» بدل گشته و «س» امروزی از همین‌جاست. چونگ (۲۰۰۷) مرحلهٔ فارسی میانه را از متون پهلوی تأیید می‌کند: lys- /līs-/ «لیسیدن» با ماضی lyst /līst/. «لیسیدن» مصدر نوساختهٔ فارسی دری است که بر ستاک حال لیس- با پسوند -یدن ساخته شده و چون زنده و پرکاربرد بوده جای «لیشتن» کهن را گرفته است. ابوالقاسمی در «ماده‌های فعل‌های فارسی دری» (ص۷۶) همین را می‌گوید: «لشت < ایرانی باستان *laiz-ta-، لیس < *raiz-a-، ر پیش از z به ل بدل شده». تنها گره ناگشوده، بدل شدن «ر» آغازین به «ل» است (اوستایی raēz-، سغدی rys-) که چونگ آن را «مشکلی مشهور» می‌نامد؛ ولی در تعیین ریشه خللی وارد نمی‌کند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%84%DB%8C%D8%B3%DB%8C%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ley%C7%B5%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1895\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ vol. 3, OCR file incoming/BQT/BQT_v3_pages.txt at [pdf page 692] (printed ≈1897, i.e. Nourai's 1895 within the ±2 drift of this scan), Moʿin's footnote 4: «لیشتن ـ لیسیدن. از ریشهٔ پارسی باستان liz، *lishtanaiy = فارسی لشتن، زمان حال *laizāmiy ... فارسی lēsam (نظیر نوشتن : نویسم) پدید آمده «هوبشمان ۹۵۴»، پهلوی lishtan ... ارمنی lizum، lizem، lixam» — and immediately after it the Sūzani verse «لشتند آستانت بزرگان و مهتران ـ چون یوز پیر لشته بلب کاسهٔ پنیر» that Nourai prints in this very box.\"},\n            {\"ref\": \"HRN:212\", \"status\": \"supports\", \"note\": \"HRN.txt \\\\f-block 234, page header '— 212 —', no. 954: 'listen \\\"lecken\\\", Praes. lēs-em, lestīdan. ... phlv. listan, l(i)stan (AV.); ap. √*lais- (√leiĝh- + s); vergl. ai. √reh-, rehmi, skr. leh-, lehmi \\\"ich lecke\\\"; arm. lizem, lizum etc.' — Horn's page 212 is exactly the entry for this verb.\"},\n            {\"ref\": \"FFD:76\", \"status\": \"supports\", \"note\": \"Abolqāsemi, Māde-hā-ye Feʿl-hā-ye Fārsi-ye Dari, incoming/FFD/FFD_pages.txt at [pdf page 81] = printed p.76 (printed = pdf − 5): «لشت < ایرانی باستان *laiz-ta- ... *raiz- صورت اصلی *laiz- است، r پیش از z به l بدل شده ... به معنی «لیسیدن». لیس < ایرانی باستان *raiz-a- ... «س» در «لیس» به جای z آمده است». The book's own index (pdf p.95) lists «(ریشه ← لیسیدن + لشتن) ۷۶».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no. 954, p.96 (HUB.txt \\\\f-block 106)\", \"stance\": \"supports\", \"note\": \"'idg. ligʰ = iran. ap. lis bildete den Inf. *listanaiy = np. listan, das Praesens *laizāmiy = np. *lēzam, das nach dem Muster von nivistan : nivēsam zu lēsam umgestaltet wurde.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *raiz1 'to lick'\", \"stance\": \"supports\", \"note\": \"'MIDDLE PERSIAN: BMP lys- /līs-/ \\\"to lick\\\"; Pret.: IND. 3sg. BMP lyst /līst/ ... NWIR: NP listan/lēs-, Kurd. (Sor.) lēsīn, listin/lēs- ... © The unexpected l- found in many Iranian cognate forms is a notorious problem.'\"},\n            {\"src\": \"ARY\", \"where\": \"p.455 (ARY_pages.txt, block tagged [pdf page 454])\", \"stance\": \"supports\", \"note\": \"Headword «لیسیدن، لشتن / ۴۵۵» with columns: اوستایی RAĒZ / RAĒZAITE, پارسی باستان *LAIZĀMIY / *LISTANAIY, پهلوی LISTAN, ارمنی lizum/lizem, لاتین LINGŌ, انگلیسی کهن LICCIAN — an independent modern Persian handbook reproducing the same chain.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, grepped for lis-/līstan\", \"stance\": \"silent\", \"note\": \"The Concise Pahlavi Dictionary does not carry the verb (its ~4000-word core omits it); the Middle Persian evidence comes from Cheung's reading of the books instead.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary), grepped 'listan', 'lick'\", \"stance\": \"silent\", \"note\": \"Not in the glossary — it covers only the texts edited in Part I.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.400\", \"stance\": \"supports\", \"note\": \"'np. līštan \\\"lecken\\\" (usw., s. Bartholomae Airan. Wb. 1485)' — Walde-Pokorny prints Nourai's spelling līštan for the Persian.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"likkon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"West Germanic *likkōn 'to lick', a geminated (expressive) weak verb built on the zero grade *ligʰ- of the root, with *gʰ > g > k and the -kk- doubling typical of this affective verb (Pokorny calls it 'ablaut. geminiert'). It yields Old Saxon likkon, Old High German lecchōn (> German lecken), Middle Dutch likken and Old English liccian; beside it stands the non-geminate iterative *laigōn seen in Gothic bi-laigōn 'to lick at'. Old French lechier 'to lick' is a Frankish loan from the same verb, whence English lecher. Nourai's citation form 'likkon' is precisely Watkins's reconstruction.\",\n          \"derivation_fa\": \"صورت ژرمنی غربی *likkōn «لیسیدن» است؛ فعلی ضعیف با همخوان مضاعف که بر درجهٔ صفر ریشه (*ligʰ-) ساخته شده: gʰ هندواروپایی بنا بر قانون گریم به g و سپس در این ساخت به k بدل شده و دوگانگیِ -kk- ویژگی همین فعل عاطفی است (پوکورنی می‌نویسد «ablaut. geminiert»). بازماندگان آن ساکسونی کهن likkon، آلمانی علیای کهن lecchōn (> آلمانی lecken)، هلندی میانه likken و انگلیسی کهن liccian است؛ در کنار آن صورت غیرمضاعف *laigōn در گوتی bi-laigōn «لیسیدن» دیده می‌شود. فرانسهٔ کهن lechier نیز وام‌واژه‌ای از همین فعل فرانکی است که واژهٔ انگلیسی lecher از آن آمده. صورتی که نورایی نوشته (likkon) دقیقاً همان بازسازی واتکینز است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ley%C7%B5%CA%B0-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. leigh- (AHD_watkins1985.txt line 671): 'leigh-. To lick. ... 2. Zero-grade form *lig- in Germanic *likkōn in: a. Old English liccian, to lick: LICK; b. Old French lechier, to live in debauchery: LECHER. [Pok. leigh- 668.]' — Nourai's 'likkon' is verbatim Watkins.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p.886 s.v. lick (KLN_1966.txt line 21660)\", \"stance\": \"supports\", \"note\": \"'ME. licken, fr. OE. liccian, rel. to OS. likkon, Du. likken, OHG. lecchon, MHG, G. lecken, \\\"to lick\\\", Goth. bi-laigon, \\\"to lick at\\\" (F. lecher ... is a Teut. loan word), from the I.-E. imitative base *leigh-'.\"},\n            {\"src\": \"POK\", \"where\": \"p.668\", \"stance\": \"supports\", \"note\": \"'got. bilaigōn \\\"belecken\\\"; ablaut. geminiert ags. liccian, ahd. lecchōn, as. likkon \\\"lecken\\\"'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. leigho, io\", \"stance\": \"partial\", \"note\": \"'MHG lecken, id. (from *lig-)' — Mann gives the same zero-grade source but cites the German rather than the reconstructed *likkōn.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"lick\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English liccian 'to lick' > Middle English licken > Modern English lick; a straight inherited descent within English from West Germanic *likkōn, with no borrowing at any stage. The Old English geminate -cc- palatalises to /k/ (not /tʃ/) because it stands before a back vowel in the infinitive, giving the modern /lɪk/. Sense-development is minimal ('pass the tongue over'); the figurative 'defeat, thrash' is a 16th-century English innovation not relevant to the chart.\",\n          \"derivation_fa\": \"انگلیسی کهن liccian «لیسیدن» < انگلیسی میانه licken < انگلیسی امروز lick؛ زنجیره‌ای کاملاً ارثی و بدون وام‌گیری، مستقیماً از *likkōn ژرمنی غربی. همخوان مضاعف -cc- در انگلیسی کهن چون پیش از واکهٔ پسین مصدر آمده، به /k/ بدل شده نه به /tʃ/، و تلفظ امروزی /lɪk/ از همین‌روست. تحول معنایی در کار نیست؛ معنی مجازی «شکست دادن» نوآوری قرن شانزدهم انگلیسی است و به نمودار ربطی ندارد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ley%C7%B5%CA%B0-\"],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the node carries no citation in the book; the parent Germanic box cites AHD, whose leigh- entry names LICK as the English derivative of *likkōn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p.886 s.v. lick\", \"stance\": \"supports\", \"note\": \"'lick, tr. and intr. v. — ME. licken, fr. OE. liccian ... from the I.-E. imitative base *leigh-'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leigh-; English index 'Lick leigh-' (AHD_watkins1985.txt line 1742)\", \"stance\": \"supports\", \"note\": \"'a. Old English liccian, to lick: LICK'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.59 LICK, p.267\", \"stance\": \"supports\", \"note\": \"'Goth. bi-laigon, OE liccian, ME licke, NE lick, Du. likken, OHG leccōn, MHG, NHG lecken' listed as the Germanic members of the *leigh- group.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-306.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 306"
}
```


### [2026-09-06T23:09:03.091Z] TOOL RESULT

```
JSON OK
nodes verified: 8/8
node verdicts: {'plausible': 3, 'confirmed': 5}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'partial': 2, 'not_checked': 2}
books consulted: {'supports': 19, 'partial': 3, 'silent': 5, 'contradicts': 1} | by book: {'WLD': 4, 'CHEUNG': 4, 'IEC': 3, 'AHD': 3, 'ARY': 2, 'HUB': 2, 'POK': 2, 'KLN': 2, 'WEB': 1, 'SKT': 1, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'SYN': 1}
```


## [2026-09-06T23:09:23.756Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-306.json` written; `verify_check.py 306` reports 8/8 nodes, 0 PROBLEM lines.

**PDF page 306 (book p. 276) — 2 entries, 8 nodes**

Verdicts: roots 2 confirmed; nodes 5 confirmed, 3 plausible, 0 disputed, 0 transcription_suspect.
Ref checks: 10 supports, 2 partial, 2 not_checked (nodes with no citation). Books consulted: POK, WLD (Bd I/II), AHD/Watkins, IEC (Mann), SYN (Buck), KLN, SKT, BRT, CHEUNG, HUB, HRN, FFD, BQT, MON, ARY, SOD, PHD, NYB.

Key findings:
- **Leig** (POK:667) and **Leigh 1** (POK:668) both check out verbatim against Pokorny's printed pages; WLD II 399/400 and Watkins confirm both.
- **BQT:59** is exact (vol. 1, leaf 269): آلیزدن/آلیزیدن «جفته افکندن» with the same Sarāj-ed-Dīn verse Nourai prints.
- **BQT:1895** is exact (vol. 3, pdf p. 692 ≈ printed 1897, within the scan's ±2 drift): Moʿin's footnote «لیشتن ـ لیسیدن … *lishtanaiy … هوبشمان ۹۵۴» plus the same Sūzani verse. **HRN:212** (no. 954) and **FFD:76** likewise land on the right pages. **SOD:348** is entry 8654 `rys- … <*raiz-, Av. raēz- … (to) lick` — precisely the arrow.

Three `plausible` (no disputes):
- **Leig #1 Persian ālīzīdan/ālīz** — Pokorny, Walde-Pokorny, Aryanpur p.69 and Wiktionary all put آلیختن/آلیز under this root, but Cheung 2007 files it as a query-marked `*raiz² ? 'to jump'` attested only in modern West Iranian, with the l- "atypical" and an IE provenance "difficult to establish". Also Nourai's gloss "to jump around" is loose — the sources all say specifically "kick out (of a horse)".
- **Leig #3 English lark** — AHD/Watkins asserts ON leika → LARK²; Etymonline (and OED) call it "of uncertain origin", allowing a shortening of *skylark*.
- **Leigh 1 #1 Avestan "leiš, raěz, rěh"** — only `raēz-` is Avestan (BRT col. 1485; Cheung's YAv. riz-, ā-raērizaite N 68). `rěh` is Sanskrit reh-/leh- (Horn no. 954, Bartholomae), and `leiš` is Horn's Old Persian `√*lais-` which Hübschmann (Pers. Stud. no. 954) explicitly rejected. Mislabelling in the book, not a misreading — the derivation from the IE root stands.

No extraction errors: the printed page (rendered at 200 dpi) matches `data/extracted/batch/page-306.json` in every word, script string and quote, including the parenthetical آلیختن and لِشتن in `script_extra`.

Six web pages archived via `fetch_source.py` (Etymonline lark; Wiktionary لیسیدن، آلیختن، *leyg-، *leyǵʰ-، *laikaną).
