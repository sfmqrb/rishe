# Verification process log — verify-page-286


## [2026-09-06T21:51:58.733Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 286 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-286.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-286.json. Write /home/sfmqrb/git/rishe/data/verification/page-286.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 286` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:52:00.173Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:52:00.863Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:52:00.879Z] TOOL RESULT

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


## [2026-09-06T21:52:01.374Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-286.txt"
}
```


### [2026-09-06T21:52:01.398Z] TOOL RESULT

```
1	=== PDF page 286 (book page 256) ===
2	--- entry 0 ---
3	ROOT Kungios -> redirect to Kung
4	--- entry 1 ---
5	ROOT Kunki -> redirect to Kung
6	--- entry 2 ---
7	ROOT Kŭnos -> redirect to Keu 2
8	--- entry 3 ---
9	ROOT [Indo-European] Kup 1, Sup 2 : shoulder  (refs POK:627)
10	#1 (parent #0) [Avestan] refs=POK:627 | supti : shoulder
11	  #2 (parent #1) [Persian] refs=SYN:236; POK:627; BQT:1143; HRN:163 | soft «سُفت» : shoulder
12	--- entry 4 ---
13	ROOT [Indo-European] Kŭp 2, Kwĕp : to smoke, cook, also move violently, be agitated  (refs POK:596)
14	#1 (parent #0) [Sanskrit] refs=POK:596; SYN:188 | kapi : incense, smoke (color) ; kapila : brownish / reddish color ; kapî : brownish animal, monkey | NOTE: POK indicates that "kapi" is not verified.
15	  #2 (parent #1) [Pahlavi] refs=HRN:87; SIN:581 | kapik : monkey
16	    #3 (parent #2) [Persian] refs=BQT:1593; FSF:268; HUB:87 | kapî «کپی» : monkey | extra: کپی
17	#4 (parent #0) [Old Persian] refs=POK:597 | kupsins : mists
18	  #5 (parent #4) [None] refs=None | 
19	#6 (parent #0) [Latin] refs=POK:596; AHD:1524 | vapor : steam
20	  #7 (parent #6) [English] refs=AHD | vapor, evaporate
21	#8 (parent #0) [Latin] refs=AHD:1524 | cupere : desire
22	  #9 (parent #8) [English] refs=None | Cupid
23	--- entry 5 ---
24	ROOT [Akkadian] Kupriti : sulfur  (refs AKD:60)
25	#1 (parent #0) [Aramaic] refs=AKD:60 | gubrîtâ, kubrîtâ : sulfur
26	  #2 (parent #1) [Arabic] refs=AKD:60; BQT:1588 | kibrit : sulfur, match
27	    #3 (parent #2) [Persian] refs=BQT:1588; MON:2887 | kebrît «کبریت» : sulfur, match
28	
```


## [2026-09-06T21:52:02.927Z] AGENT

I'll start by reading the source JSON and the reference infrastructure.


## [2026-09-06T21:52:04.345Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-286.json",
 "description": "Read source JSON page 286"
}
```


### [2026-09-06T21:52:04.379Z] TOOL RESULT

```
{
  "pdf_page": 286,
  "book_page": 256,
  "entries": [
    {
      "root": {
        "name": "Kungios",
        "redirect": "Kung"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kunki",
        "redirect": "Kung"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kŭnos",
        "redirect": "Keu 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kup 1, Sup 2",
        "lang": "Indo-European",
        "refs": "POK:627",
        "gloss": "shoulder"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:627",
          "words": [
            {"translit": "supti", "gloss": "shoulder", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "SYN:236; POK:627; BQT:1143; HRN:163",
          "words": [
            {"translit": "soft", "gloss": "shoulder", "script": "سُفت"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "آن سُفت سیمینش مشکین کمند - سرش گشته چون حلقهٔ پای بند",
            "poet": "Ferdowsî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Kŭp 2, Kwĕp",
        "lang": "Indo-European",
        "refs": "POK:596",
        "gloss": "to smoke, cook, also move violently, be agitated"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:596; SYN:188",
          "words": [
            {"translit": "kapi", "gloss": "incense, smoke (color)", "script": null},
            {"translit": "kapila", "gloss": "brownish / reddish color", "script": null},
            {"translit": "kapî", "gloss": "brownish animal, monkey", "script": null}
          ],
          "script_extra": null,
          "note": "POK indicates that \"kapi\" is not verified.",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:87; SIN:581",
          "words": [
            {"translit": "kapik", "gloss": "monkey", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1593; FSF:268; HUB:87",
          "words": [
            {"translit": "kapî", "gloss": "monkey", "script": "کپی"}
          ],
          "script_extra": "کپی",
          "note": null,
          "quote": {
            "text": "بر هر دو بیشه یکی بُرز کوه - بر آن کوه کپی فراوان گروه",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:597",
          "words": [
            {"translit": "kupsins", "gloss": "mists", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:596; AHD:1524",
          "words": [
            {"translit": "vapor", "gloss": "steam", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "vapor, evaporate", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1524",
          "words": [
            {"translit": "cupere", "gloss": "desire", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Cupid", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kupriti",
        "lang": "Akkadian",
        "refs": "AKD:60",
        "gloss": "sulfur"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "AKD:60",
          "words": [
            {"translit": "gubrîtâ, kubrîtâ", "gloss": "sulfur", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "AKD:60; BQT:1588",
          "words": [
            {"translit": "kibrit", "gloss": "sulfur, match", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1588; MON:2887",
          "words": [
            {"translit": "kebrît", "gloss": "sulfur, match", "script": "کبریت"}
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


## [2026-09-06T21:52:04.863Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T21:52:04.907Z] TOOL RESULT

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


## [2026-09-06T21:52:10.878Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','BQT','HRN','HUB','AKD','MON','AHD','SIN','FSF','WLD','IEC','PHD','NYB','BRT','KNT','LKT','KLN','FVQ','AFM','PLA','ARY','SKT','LEW','LAT','AFA','TAD','ARB']:\n    v=d.get(k)\n    if v: print(k, json.dumps(v,ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-06T21:52:12.590Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
```


## [2026-09-06T21:52:20.825Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint(); print(d['BQT']['page_offset']); print(d['BQT'].get('lookup_hint'))\nprint(); print(d['SYN'].get('lookup_hint'))\nprint(); print(d['AKD'].get('lookup_hint'))\n\""
}
```


## [2026-09-06T21:52:21.216Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"supti\" POK_*.txt | head -30; echo ---; grep -n \"supti\" BRT.txt | head -20"
}
```


### [2026-09-06T21:52:22.437Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config

vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.

Organised by semantic field; Akkadian words in transliteration with Aramaic/Arabic/Persian loans. grep the word.
```


### [2026-09-06T21:52:22.491Z] TOOL RESULT

```
POK_full.txt:52059:Material: Old Indie supti-, Avestan si/yO//- 'shoulder'; alb. s^p "shoulder, back' (without 
---
26387:•  j.  suptiJIar^nga-  Adj.  'Gaugenosse,  aus dem  selben  Gau  gebürtig':  visaifivä  asii mihm  anian  hasa  'ga  (AD.)  %risd^w3 antarf  vanzäna  cähwarjsahwa  antan ht^gaiSia  pancasa^wA  antar»  Auyäyna "zwanzigfach  (bindend)  ist  M.  zwischen ein  Paar  Genossen  aus  dero  selben  Gau, . .  aus  der  selben  Gemeinde,  . .  aus  dem selben  Haus,  . .  aus  der  selben  Stube" YtiO.  116.
28907:•  j-  (1  g-t  P)  haxay- :  Ariy-,  Aai'-^^,  m. i)  'Freund,  Genosse':  ^m  °xa  (NS.)  '1/ (DS.)  *baraiti  Y.  6'2.  8;  —  aa£  aosOe  'xa •sa  (IS.)  V.  18.  a6;  F.  24;  —  yaS:a  . .  mri Aamü.äaina  Jason  brn%ra  va  'xaya  (NP.) vä  V.  4.  44;  Vyt,  10;  —  vlsaitiva  asti mi^r5  atiian  'ia  (AD.)  suptiiiannga  (sd) Yt.  JO.  116;  —  Sxstim  kqm.vaintfm  .. 'xaya    (AD.)    sraosaAe    Yt  //.  16;     16',
30467:•  j.  huyä)Tia-  Adj,  'das  Lager  teilend, Lager-,  Stubengenosse';  vlsaitivä  asti miirS  aniar»  ha!a  suptioarynga  (sd.)  .  , pama.sa%wa  autark  'na  (AD.)  \t  10.116.
```


## [2026-09-06T21:52:25.898Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52040,52075p' POK_full.txt"
}
```


### [2026-09-06T21:52:25.941Z] TOOL RESULT

```
Slavic *kvbtQ, */ri//s//" bloom, blossom' in Old Church S\aV\c pro-cvbtg, -cv/st/l\o\Ner, 
bloom, blossom'. Old Czech ktvu, kvfstr, ablaut. Old Church Slavic cvetb, Czech kveteic. 
"bloom, blossom'; besides Slavic *kvbtet/"\n russ. -Church Slavic cvbtet/" b\oom, blossom' 
and Serbo-Croatian cavtJet/^b\oorc\, blossom' (= Latvian kvitet). 

References: WP. I 469 f., Trautmann 147 f., 310 f., Osthoff ZONF. 13, 3 ff. 
Page(s): 628-629 

Root / lemma: Rup- {*Rehu-p^ 

Meaning: shoulder 

Note: (Germanic with aniaut. s-) 

common k- > sk- > s- kentum > satem. 

Material: Old Indie supti-, Avestan si/yO//- 'shoulder'; alb. s^p "shoulder, back' (without 

formant -/-); Middle Low German schuftxr\.. East Frisian, Dutch 5c/7c»/? "shoulder blade of a 

cow, a horse' ( *skuftu-). 

Note: 

Clearly alb. alb. s^p "shoulder, back' is the oldest form IE cognate while other IE forms are 

extensions with suffix -ti, -tu. 

References: WP. I 467. 

Page(s): 627 

Root/ lemma: Ruei-1, Ruei-no-{* R'^ehu-no-) Note: common Proto Germanic -u- > -u-, -y-, -
```


## [2026-09-06T21:52:26.897Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: keu\" POK_full.txt | head -40; echo ---; grep -n \"Page(s): 596\" POK_full.txt | head; echo ---; grep -n \"Page(s): 627\" POK_full.txt | head"
}
```


### [2026-09-06T21:52:26.966Z] TOOL RESULT

```
46624:Root / lemma: keuad- kud- 
46660:Root / lemma: keu-1, skeu-, lengthened grade keu- 
46749:Root / lemma: keu-2, keua- 
---
47062:Page(s): 596-597 
---
48931:Page(s): 627 
48985:Page(s): 627 
49017:Page(s): 627-628 
52073:Page(s): 627 
52338:Page(s): 627
```


## [2026-09-06T21:52:33.476Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '46995,47070p' POK_full.txt"
}
```


### [2026-09-06T21:52:33.531Z] TOOL RESULT

```
Middle Irish co/77/77 "vessel'; c^/77/77a/ "goblet, bowl', cymr. cwmm 'vaWey' (m.), bret. 
/ro/77/77 "trough' (m.); from urbrit. *kumbos der'we Old English cumb'yaWey', engl. coomb, 
combe ^bas\n, hollow, coomb, narrow valley ', whereas is gall. -rom.c^/77i6'a "valley, trough' 
Fem.; from French derives bret. /ro/r?/? "valley'; compare the unnasalized vascular names 
pam. kubun, poln. kubek, also gr. KupO(; " cup. bowl '; 

Old Icelandic aptr-huppr, Norwegian Dialectal buppan6 hump^ the hip of the cattle ', 
Modern High German humpein. Middle Low German humpelen " limp ' and in not 
especially on the bending of the body ability meaning: 

Norwegian humprw. "bumpiness, knag' (ndd. loanword), engl. hump^ hump, hunchback 
', ndd. humpei. "thick piece', bumper low hillock', Dutch homp^Vc\\ck piece of bread'; 
perhaps Modern High German (ndd.) Humpen {compare Kuppog). 

References: WP. I 370 ff., WH. I 127, 297 f., 298, 305, 306, 310 f., 859, Trautmann 121 f. 
Page(s): 588-592 

Root / lemma: {keuap-.) kuep- kuap- kup-nexi to which occasional keu(e)p-, k(e)uep- 

Meaning: to smoke; to boil; to cook 

Note: From Ai/- plural only Ar- probably through previously proto Indo Germanic 

simplification 

Material: Old Indie kupyati{= Latin cupid) " is seething, is angry ', kopa-vn. "surge, rage, 

fury', kopayati^ shakes, angers'; copati^ moves, stirs '; /ra/?/- (uncovered) "incense', 

wherefore as "* smoke-color ' kapila-, kapisa- " brownish, reddish', also kapf-xw. "ape'; 

alb. /ra/O/fe/T? "breathe heavily ' (as Lithuanian kupuoti' breathe heavily '); 

Maybe alb. keputem^ be tired', kepuV cut '. 



gr. KaiTvoq "smoke', horn, ano 5£ itJUxnv EKaTTiruaEV "exhale, breath out; give off ' : 
Kanu(; uud Konoq nv£U|ja Hes., KEKpcps teGyhke Hes., KEKacpnora Horn, "exhaling'; 
compare to dissimilation from *kuap-no-s\.o Kouvbc, Schwyzer Gr. Gr. I 302; 

Latin cupio, -ere "lust, crave' (= Old Indie kupyati), cuppedo= " a desire, wish, longing, 
eagerness, passion ', also cuppes^ lascivious, esp. of treat, delight', cuppedium^ 
snacking, tidbit'; Umbrian Cubrar^ Bonae ', sabin. cuprum^ good ' ("*worth having, 
welcome, wanted, desirable ' with passive forms -ro-as c/arus etc.); vapor^haze, mist, 
vapor', old uapos {*kuapds)\ 

Old Irish ad-cobra " wish, desire, want ' ( *-kuprat), verbal noun accobor{ *ad-kupro-) 
"wish', Thurneysen Gr. 139; 

Gothic a ffvapjan {*kudb- bes\des other *ku9p-) "choke; suppress, crush, extinguish, 
annihilate, erase ', affvapnan^ die, be extinguished ' (: ano-Kanuw), Middle High German 
verwepfen^ kahmig werden, vom Wein ', nisi. /7KayO "dropsical flesh'; 

Lithuanian kvapas'C(\. "breath, breeze, haze, mist, Wohlgeruch' (: Latin vapor), kvepiu, - 
eti^ smell ' (-e- could be Baltic ablaut neologism), kvepiu, /ri/ep//"breathe', Latvian kvept 
"smoke', kvepesP\. "breath, breeze, fume, smoke, smut', kvepeV fume ', changing 
through ablaut Lithuanian kupuoti^ breathe heavily ', Latvian kupet^ smoke; steam, raise 
dust, cause dust', kupinaties^ auiqeheu (of dough)', /r^p/ "ferment, seethe'. Old Prussian 
kups/nslog' (derivative from an es-stem as Latin vapor); 

Old Church Slavic kypljg, kypet/"bo\\, overflow', kypn, " lax, porous ', Czech kypry o\d 
"keen, eager, fresh'; kir. kvapytysa' hasten, hurry'; with (Indo Germanic) reduced i/russ. 
kopotb ( *koput-) f. "fine smut, dust', koptftb " make black with smoke, fume '; perhaps Old 
Church Slavic /ro/?/^"diir (smelling plant; s. Berneker 564). 

References: WP. I 379 f., WH. I 312 f., Trautmann 147. 
Page(s): 596-597 

Root / lemma: kei- 

Meaning: to move, go, departure, *die 

Note: 

Root/ lemma: kei-\ to move, go, departure, *die, derived from Root/ lemma: Rei-1\ to lie
```


## [2026-09-06T21:52:45.806Z] TOOL CALL #11: Bash

```json
{
 "command": "ls site/pages/286.jpg 2>/dev/null; pdftoppm -f 286 -l 286 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg286 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T21:52:47.957Z] TOOL RESULT

```
site/pages/286.jpg
total 31244
drwx------ 3 sfmqrb sfmqrb    4096 Sep  6 17:52 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     572 Sep  6 17:52 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb   97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74145 Sep  6 17:43 build278.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   31044 Sep  6 17:50 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb   41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb   46494 Sep  6 17:52 mk279.py
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
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 17:52 p284
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
-rw-rw-r-- 1 sfmqrb sfmqrb   69883 Sep  6 17:52 pg286.png
```


## [2026-09-06T21:52:50.996Z] TOOL CALL #12: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg286.png"
}
```


### [2026-09-06T21:52:51.328Z] TOOL RESULT

```

```


## [2026-09-06T21:52:51.326Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T21:53:03.082Z] TOOL CALL #13: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 286 -l 286 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg286hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg286hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.55),int(h*0.33),int(w*0.80),int(h*0.40))).save('$S/kapi_script.png')\n\""
}
```


### [2026-09-06T21:53:06.175Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T21:53:08.583Z] TOOL CALL #14: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/kapi_script.png"
}
```


### [2026-09-06T21:53:08.621Z] TOOL RESULT

```

```


## [2026-09-06T21:53:22.527Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN shoulder ===\"; grep -n \"SHOULDER\" SYN.txt | head -10; echo \"=== SYN supti ===\"; grep -n \"supti\\|sufti\\|Av. supti\" SYN.txt | head -10; echo \"=== HRN sufte/soft ===\"; grep -n -i \"suft\\|sufta\\|supti\" HRN.txt | head -20; echo \"=== HUB supti ===\"; grep -n -i \"supti\\|suft\" HUB.txt | head -20"
}
```


### [2026-09-06T21:53:22.618Z] TOOL RESULT

```
=== SYN shoulder ===
6080:yprs OF TH ‘ Ilel forms with | nal throat. Walde-P. 2.634. NED s.v. 1, etc., beside par HG | throat na ‘swvel ALG. strotte, Du. strot, M pees : 3 init, 8, 28 } ¥, ME strouten ‘bulge, 6. Lith. gerklé, ChSl. griilo, etc., “hroa - s(ro22e oe aati an once, meaning dub., | above, 1. a: ell’ (OE 8 wut), ete., Temoter root Lett. rtkle (Lith. ryklé dial. or vulgar), of, NED 5. ee but immediate | fr. the root of Lett. ri, Lith. ryt ‘swal- . 3 | connections ee of ‘throat’ doubtless | low’. Mihl.-Endz. 3.537. semantic SoU ied first to the exter- 7. Skt. and Av. words, above, 1. ‘hulge, swell’, app41e 4.330 SHOULDER 2 Goth. amsans (acc. pl.) Lith. petys Crk. dyos ON herdr, oxl Lett.  plecs, kamiésis NG  dpos a Dan.  skulder ChSi. amo, pleste Lat. aa ate Sw. azel, skuldra SCr.  rame, pleéa It. Litite OE eal, sculdor Boh. _rameno, plece aa ME _ schulder Pol. — ramie, plecy (pl.) Ep. ee NE shoulder Russ. pleéo aoe ial formnt Du. schouder Skt.  skandha-, ansa- Sitios pala OHG - scultira, ahsala (cupli-) V ‘ ysgwydd MHG | schulter, ahsel Ay. supti- (daos-) Br. skoaz NHG | schulter, achsel
=== SYN supti ===
6080:yprs OF TH ‘ Ilel forms with | nal throat. Walde-P. 2.634. NED s.v. 1, etc., beside par HG | throat na ‘swvel ALG. strotte, Du. strot, M pees : 3 init, 8, 28 } ¥, ME strouten ‘bulge, 6. Lith. gerklé, ChSl. griilo, etc., “hroa - s(ro22e oe aati an once, meaning dub., | above, 1. a: ell’ (OE 8 wut), ete., Temoter root Lett. rtkle (Lith. ryklé dial. or vulgar), of, NED 5. ee but immediate | fr. the root of Lett. ri, Lith. ryt ‘swal- . 3 | connections ee of ‘throat’ doubtless | low’. Mihl.-Endz. 3.537. semantic SoU ied first to the exter- 7. Skt. and Av. words, above, 1. ‘hulge, swell’, app41e 4.330 SHOULDER 2 Goth. amsans (acc. pl.) Lith. petys Crk. dyos ON herdr, oxl Lett.  plecs, kamiésis NG  dpos a Dan.  skulder ChSi. amo, pleste Lat. aa ate Sw. azel, skuldra SCr.  rame, pleéa It. Litite OE eal, sculdor Boh. _rameno, plece aa ME _ schulder Pol. — ramie, plecy (pl.) Ep. ee NE shoulder Russ. pleéo aoe ial formnt Du. schouder Skt.  skandha-, ansa- Sitios pala OHG - scultira, ahsala (cupli-) V ‘ ysgwydd MHG | schulter, ahsel Ay. supti- (daos-) Br. skoaz NHG | schulter, achsel
6107:Skt. cupti- (only once, RV 1.51. 5), Av. supti- (NPers. suft) : Alb. supé ‘shoulder’, MLG schuft, Du. schoft ‘but- tock, rump, shoulder (of animals)’, Walde-P. 1.467.
14532:Chl. rasypati, SCr. sipati, Boh. sypati, Pol. sypaé, Russ. sypat’ ‘pour out, shake out, strew, scatter’ : Lith. supti ‘swing, rock’, Lat. swpdre ‘throw’ (Fes- tus), cpd. dissipare ‘scatter’. Walde-P. 2.524. Trautmann 293. Ernout-M. 1005. Walde-H. 1.356 f.
16755:soukati ‘wind, twist’ (thread, wool, etc.), Russ. skatat’ ‘roll up’, skatit’ ‘roll down’ etc.; also *seu-p- in Lith. supti ‘swing, rock’,
=== HRN sufte/soft ===
3595:her n^sufte dür-l derl mesuft
6438:789. suft, sift 'Schulter .
6439:aw. supfi' 'Schulter ; phlv. suft; ai. rüpti- 'Schulter ;
6448:will); phlv. suftan (für aw. sifat'^); Bund.).
6502:Zu np. sufte^i (No. 740).
8012:924. fftisuften 'zerstreuen ; verwelken (Vis und RamTn,
8018:Verbessert aus kiisuften etc. der Wörterbücher.
8019:Vergl. np. Osuften (No. 32).
12459:gusuften 924.
=== HUB supti ===
2674:gehort jedenfalls zu suftatif pr. sunbam 'durchbohre',
2679:der Inf. np. suftan. Dazu np. sufra = afgh. LW.
5497:vi + Wzl. sci 'binden*; gusuftan 'zerstreuen, verwelken =
5498:phi. v(i)suftan Gl. and Ind. 245 ; guman Zweifel' = zd. *t?i-
6523:arisch gabh, jabh (idg. g^embh, g'^fphh) ; gusuftan 'zerstreuen*,
6526:'ksubh ; Osuftan Verwirrt werden', (isdb *Verwirrung' = phi.
8316:H. 1034; Osuftan erregt werden, phi. asdp Terwirrung',
```


## [2026-09-06T21:53:24.088Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT supti ===\"; grep -n \"supti-\\|süpti\\|supti \" BRT.txt | head -20; echo \"=== IEC ===\"; grep -n \"supti\" IEC.txt | head; echo \"=== ARY sofd ===\"; grep -n \"سفت\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T21:53:24.186Z] TOOL RESULT

```
=== BRT supti ===
=== IEC ===
=== ARY sofd ===
3710:معنی این واژه در زبان‌های ژرمنی: سوراخ کر دن؛ سفتن؛ مته.
```


## [2026-09-06T21:53:35.238Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leafof(path, needle, maxhits=6):\n    data=open(path,encoding='utf-8',errors='replace').read()\n    pages=data.split('\\f')\n    out=[]\n    for i,p in enumerate(pages):\n        if needle in p:\n            out.append(i)\n            if len(out)>=maxhits: break\n    return out\nprint('HRN 789 suft leaf', leafof('HRN.txt',\"789. suft\"))\nprint('SYN 4.30 leaf', leafof('SYN.txt',\"Skt. cupti-\"))\nprint('HRN kapik leaf', leafof('HRN.txt',\"kapik\"))\nprint('HUB kap leaf', leafof('HUB.txt',\"kapi\"))\nEOF"
}
```


### [2026-09-06T21:53:36.705Z] TOOL RESULT

```
HRN 789 suft leaf [184]
SYN 4.30 leaf [274]
HRN kapik leaf []
HUB kap leaf [97, 99, 175, 187, 236, 251]
```


## [2026-09-06T21:53:36.742Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN kapi ===\"; grep -n -i \"kapi\\b\\|kapik\\|kap.\\{0,3\\}Affe\" HRN.txt | head -20; echo \"=== HUB kapi ===\"; grep -n -i \"kapi\\|Affe\" HUB.txt | head -20; echo \"=== SIN kapi ===\"; grep -n -i \"kapik\\|kapi \\|monkey\" SIN.txt | head -20"
}
```


### [2026-09-06T21:53:38.417Z] TOOL RESULT

```
=== HRN kapi ===
=== HUB kapi ===
203:dan 'bringen' zu skr. Or-bhar 'herbeischaffen geh5rt,
3063:Hier fehlt np. kaM 'Affe JRAS. 1894, p. 480 = phi.
3064:hapik, arm. LW. kapik, skr. Icapi-. Das Wort ist
3170:kapic 'ein Maass fur Getreide' etc., ap. xan/drj de La-
3792:Dieses Kapitel von Horn's Grundriss habe ich
4168:Persisch vgl. Blochmann, JASB. XXXVII, 1, 34-38.Kapitel 1: ap. a.
4696:Kapitel 2: ap. d.
4833:Kapitel 4: ap. u nnd u.
4926:Kapitel 5: ap. ai.
4970:Kapitel 6: ap. au.
5009:Kapitel 7: ap. r (= r-Vokal)
5268:Kapitel 8: ap. y.
5418:Kapitel 9: np. v.
5609:varapanak-U *Waffenrock' 1 Kg. 17, 38, varapan *Panzer
5850:arm. armav, ;;^a:wrfa 'Schiffskapitan' aiis *naV'Xudd 'Schiffs-
5892:Kapitel 10: Kontraktion.
6180:Kapitel 12: ap. p.
6256:kaplk, arm. kapik ; kabar 'Kapernstrauch', armen. kapar, gr.
6365:Kapitel 12: ap. h.
6494:Kapitel 14 : ap. /.
=== SIN kapi ===
1388:8  Perrot  and  Hurrier,  Mat.  m6d.  et  pharmacop£e  sino-annamites,  p.  94. Cf.  also  Marco  Polo's  observation  (Yule's  edition,  Vol.  II,  p.  286)  that  the  faces of  stuffed  monkeys  on  Java  are  daubed  with  saffron,  in  order  to  give  them  a  manlike appearance.
3427:The  Persian  word  was  brought  to  China  as  late  as  the  seventeenth century  by  the  Jesuits.  Pantoja  and  Aleni,  in  their  geography  of  the world,  entitled  Cifah  wai  ki,3  and  published  in  1623,  mention  an  animal of  Borneo  resembling  a  sheep  and  a  deer,  called  pa-tsaW  ffi  ft  HI,4  in the  abdomen  of  which  grows  a  stone  capable  of  curing  all  diseases,  and highly  prized  by  the  Westerners.  The  Chinese  recognized  that  this  was a  bezoar.5  Bezoars  are  obtained  on  Borneo,  but  chiefly  from  a  monkey (Simia  longumanis,  Dayak  buhi)  and  hedgehog.  The  Malayan  name for  bezoar  is  guliga;  and,  as  far  as  I  know,  the  Persian  word  is  not  used by  the  Malayans.6  The  Chinese  Gazetteer  of  Macao  mentions  "an animal  like  a  sheep  or  goat,  in  whose  belly  is  produced  a  stone  capable
4010:than  four  Sanskrit  plant-names, —  kadara,  kadala,  kandara,  and  kandata, while  the  Tohfat  states  that  kader  is  called  kawi  in  India,  being  a  tree similar  to  the  date-palm,  the  flower  being  known  as  kaburah  (p.  197); kader,  accordingly,  is  an  Arabic  word,  while  kawi  is  the  supposed  Indian equivalent  and  may  correspond  to  Sanskrit  kapi  (Emblica  officinalis, Pongamia  glabra,  or  Olibanum).  These  examples  suffice:  the  twenty-one identifications  proposed  by  Jolly  are  not  convincing.  Many  of  these have  also  been  rejected  by  Achundow.
4011:The  Indian  loan-words  in  Persian  should  occasionally  be  made  the subject  of  an  exhaustive  study.  A  few  of  these  are  enumerated  by P.  Horn.1  Kurkum  ("saffron"),  however,  is  not  of  Indian  origin,  as stated  by  him  (cf .  above,  p.  321).  Skr.  sura,  mentioned  above,  occurs  in Persian  as  sur  ("rice-wine").  Middle  Persian  kaplk,  Persian  kabl ("monkey"),  is  derived  from  Skr.  kapi.1
5936:kapi  581 karalaka  588 karcura  544 karpasa  491,  574 karpura  585,  591 kavera  309 kaverl  309 kalinga  445  V
```


## [2026-09-06T21:53:49.650Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef page(path,i):\n    d=open(path,encoding='utf-8',errors='replace').read().split('\\f')\n    return d[i]\nprint(\"=== HRN leaf 108 (printed 87) ===\")\nprint(page('HRN.txt',108)[:2500])\nEOF"
}
```


## [2026-09-06T21:53:51.062Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef pages(path):\n    return open(path,encoding='utf-8',errors='replace').read().split('\\f')\np=pages('SIN.txt')\nfor i,x in enumerate(p):\n    if 'Middle  Persian  kaplk' in x or 'kaplk' in x:\n        print('leaf',i); print(x[:1800]); break\nEOF"
}
```


### [2026-09-06T21:53:51.228Z] TOOL RESULT

```
=== HRN leaf 108 (printed 87) ===
— 87 —
387. tes'Axt\
ap. vergl. us^tasana- *Bau; aw. tasa- *Axt*; phlv.
täsltan, tOsUar bezw. taxs° (vergl. aw. 'tmta-), syr.
LW. :it^NlO"nü *Zimmermannsaxt' (de Lagarde, Ges.
Abb. 49); ai. [/^taks^.
V
388. tis *Durst\ tisne {tesne Sahn. I, 59, 481), tisnegl, tesnegi
(AM. 40 Zeile 10), INDOnJl^^^D 'Wüste (Is. 13, 21).
g. tasne,
aw. tarsna- 'Durst*; phlv. tisn , tisnak, tisncfklh;
ai. tfsna-; arm. vergl. farsamim welken', anfarsam
nicht verwelkend* (H. No. 111).
kurd. ti, tmi; afy. tami; bei. tminacj, tünag, n. ftmi
'durstig, fun 'Durst' (396); wa/. tax, ^^'/^j sar. tür^
tiirt, si/n. täsna, täsnagl, yidg. triisna.
389. fest 'Becken, Untertasse*, teste, arab. LW. ^as^
aw. tasta^ Schaale, Tasse'; phlv. tast, arm. LW.
tust, tastak,
afy. LW. tust, bei. LW. ^äs (270), aus arab. tas^);
§i/n. sar. tödö (^tastaka-),
390. fü/ 'Speichel*, tufek{'% dehen)^ tiifke (Gazoph. s. v.
saliva), tufü, tuh, tuhü,
ai. i/^sthlv-, sthivati (vergl. Bartholomae, Ar.Forsch.
III, 34; Studien II, 42); got. speivan; arm. tüiß 'Speichel';
lat. spuö; gr. nzvo).
kurd. tef 'Speichel', tiw, tuw^ tu, tiik 'Spucken,
Speichel*; afy. tu, tük, tükal spucken*; oss. ft* (251);
wa;^. tuf cerak, sar. tu ceigao 'spucken'.
891. tek 'schnell, Lauf, tekiden, tekT,
aw. taka^ 'Lauf "'^) ; zu V^tak-, tac- wie ta/ten (No. 368).
(Metr. Hezej)
juz medh-^ fU terhencU büved Iierci nüvesem
her dem qel^i ez yäfe ü terkende sUceste Sözenl.
*) Hieraus auch arm. tas, ital. tazza, franz. lasse, nhd. Tasse
(Hübsohmann, ZDMG. 35, 129).
') Ap. takabara- etwa wie assahara- durch *auf schneUen (sc.
Rossen) reitend' zu erklären, verbietet die assyrische Version, über
welche mir Prof. Jensen freundlich das Folgende mitteilt:
nApers. takaharä = elamit. takaharrahe = assyr. sa magidüta ina
Kakkadisunu nasü — 'welche magidüta auf ihren Häuptern tragen'.
```


### [2026-09-06T21:53:52.927Z] TOOL RESULT

```
leaf 408
c.)  have  been  identified  by  me;  but  I  wish  to  draw  up  a  list  of all  Indian  drugs  or  products  occurring  in  Abu  Mansur,  regardless  of their  designations,  and  to  identify  them  with  their  Indian  equivalents. Abu  Mansur  gives  the  names  in  Arabic;  the  Persian  names  are  supplied from  Achundow's  commentary  or  other  sources.  The  numbers  in parentheses  refer  to  those  in  Achundow's  translation.
J.  Jolly  has  added  to  the  publication  of  Achundow  a  few  observations on  Indian  words  occurring  in  the  work  of  Abu  Mansur;  but  the  real Indian  plants  and  drugs  are  not  noticed  by  him  at  all,  while  his  alleged identifications  are  mere  guesswork.  Thus  he  proposes  for  armdk  or armal  Skr.  amlaka,  amlikd,  and  antra,  three  entirely  different  plants, none  of  which  corresponds  to  the  description  of  armak,  which  is  a  bark very  similar  to  kurfa  (Winterania  canella),  the  best  being  brought  from Yemen;  it  is  accordingly  an  Arabic,  not  an  Indian  plant.  Harbuwand (No.  576)  is  described  as  a  grain  smaller  than  pepper,  somewhat  yellow- ish, and  smelling  like  Aloexylon  agallochum;  according  to  Jolly,  this should  be  derived  from  Skr.  kharva-vindhya  ("small  cardamom"), but  the  question  is  not  of  cardamoms,  and  there  is  no  phonetic  coin- cidence of  the  words.  The  text  says  that  kader  (No.  500)  is  a  wholesome remedy  to  soften  the  pustules  of  small-pox.    Jolly  proposes  no  less
580
Indian  Elements  in  Persian  Pharmacology  581
than  four  Sanskrit  plant-names, —  kadara,  kadala,  kandara,  and  kandata, while  the  Tohfat  states  that  kader  is  called  kawi  in  India,  being  a  tree similar  to  the  da
```


## [2026-09-06T21:54:07.715Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaf97 head:', d[97][:200].replace('\\n',' | '))\nimport re\nfor i in (96,97,98):\n    if 'kabT' in d[i] or 'Affe' in d[i] or 'kapik' in d[i] or 'kaplk' in d[i]:\n        print('--- leaf',i,'---'); print(d[i][:2000])\nEOF"
}
```


## [2026-09-06T21:54:09.193Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AKD kupritu ===\"; grep -n -i \"kubrit\\|kupritu\\|gubrit\\|Schwefel\" AKD.txt | head -20; echo \"=== PHD kapik ===\"; grep -n -i \"kapik\\|kabig\\|monkey\\|ape\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T21:54:09.465Z] TOOL RESULT

```
leaf97 head: — 87 — | skr. ^JfOsa^ zuriickgeht. Den Lauten nach kann das | Wort sowohl Lehnwort wie Originalwort sein. | 842. Vgl. modern asp i kdtbud *Grausehimmer, Kosen, | Np. Sprachftihrer p. 38. | Hier fehlt np. kaM 'A
--- leaf 97 ---
— 87 —
skr. ^JfOsa^ zuriickgeht. Den Lauten nach kann das
Wort sowohl Lehnwort wie Originalwort sein.
842. Vgl. modern asp i kdtbud *Grausehimmer, Kosen,
Np. Sprachftihrer p. 38.
Hier fehlt np. kaM 'Affe JRAS. 1894, p. 480 = phi.
hapik, arm. LW. kapik, skr. Icapi-. Das Wort ist
in alter Zeit aus dem Indischen entlehnt. Jetzt wird
dafur buztna, buzina etc. gebraucht.
845. Lies afgh. kon (fem. kana *taub'). Vgl. Idg. Forsch.
Ill, 169, Anm.
848. Man erwartet karg, das in den Dialekten (vgl. ZDMG.
32, 535 ; 38, 80) mit kark etc. wechselt. Dazu kas.
karged4n *Nest' (von Menschen gemacht) Shuk. p. 55.
850. Die Bedeutung von zd. kerema- ist ganz unsicher.
Ueber skr. krimi- siehe Idg. Forsch. Ill, 161.
852. Fur skr. kuksi- wie fiir lit. kmzys miisste man np.
*A:wi erwarten. Arab, kuss 'pudendum muliebre sieht
Freitag als LW. aus dem Griech. {vLvaog) an. Das
von Johansson Idg. Forsch. II, 19 angezogene afrd-
tafkmU ist nom. pi. fem. des ptc. perf. der Wurzel
fratad und heisst nicht fliessend*.
854. Hier werden kiiSt und kust, die im Phi. nebeneinander
lagen, zusammengeworfen. Vgl. oben zu Nr. 205.
856. Afgh. kasap nach Raverty.
801. Der Versuch, np. kul mit ^vXXoq {=*khlno8 oder k-lnos?,
vgl. gr. xvxkog und Xvkoc) und skr. kuni-s (= altind.
^kjrni'S?, Bechtel, Hauptprobl. p. 385, Bartholo-
mae, Idg. Forsch. Ill, 159—161) lautgesetzlich zu
vermitteln, ist weit schwerer als es zunachst erscheint.
Wir haben kein weiteres Beispiel fiir np. ul = idg.
oZ/i, eln, In oder uln,
862. Es liegt gar kein Grund vor, das gut bezeugte k von
kaldy, kulay zu verdachtigen, vgl. modern kdlay
'Krahe' bei Rosen, Np. Sprachf. p. 39, semnan. kala
*Krahe = np. kaldy ZDMG. 32, 536, kas. kelo u. s. w.
Dazu afgh. kdryg *Krahe* und weiterhin (nach Nol-
deke) gr. xo(?a| *Rabe*, hoqwvtj 'Krahe', lat. corvus
*Rabe', comix *Krahe' etc.
```


### [2026-09-06T21:54:09.519Z] TOOL RESULT

```
=== AKD kupritu ===
976:Teer  od.  ä.  :  >  wohl  aram.,  trotz  des  ',  'atränä,  'etrcinä  Teer*  O,  mit auffälligem  q,  arab.  qaträn,  qitran).  akk.  wahrsch.  Jcuprrtu^  Schwefel,
983:6)  Bab.  Exp.  Univ.  Penns.  XIV  Nr.  148,  52.  kupritu  könnte  einfach  WeiterbUdimg von  kupru  Erdpeoh,  sein.
=== PHD kapik ===
PHD.txt:6:Oxford University Press, Walton Street, Oxford OX2 6DP Oxford New York Toronto Delhi Bombay Calcutta Madras Karachi Petaling Jaya Singapore Hong Kong Tokyo Nairobi Dar es Salaam Cape Town Melbourne Auckland
PHD.txt:101:(1) -qwes»» is an ideographic spelling of wén-, present stem of didan. It consists of the letters H, Z (reduced to a shape of G), Y, T, W, N, being a (normal) Pahlavi development from the Aramaic root kzy. The infinitive (3) has the ‘phonetic com- plement’ -tx', for the -dan of didan.
PHD.txt:132:add šabyār |špy 1! N ~] grape syrup. Skaft ... read 1. = &keft; 2. cave.
PHD.txt:212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:419:kābēn [%”fyx! | N kabin] marriage-portion, dowry (assigned to the bride). kabig [Rpy&! | N kab/pi] monkey.
PHD.txt:422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:1741:egg-shaped xayagdes.
PHD.txt:1797:escape (n.) rastarih, wirég.
PHD.txt:1798:escape (v.) rastan, wiréxtan.
PHD.txt:1970:Slight parwāz, wāzišn ; (escape) wirēg.
PHD.txt:2137:grape angūr.
PHD.txt:2841:monkey kabig.
PHD.txt:3616:shape čihr, kālbod.
PHD.txt:3617:shapely wimēhgēn.
PHD.txt:4109:unassailed apetyarag.
PHD.txt:4114:unconfessed apetitig.
```


## [2026-09-06T21:54:17.400Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('AKD.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if 'kuprrtu' in p or 'kupritu' in p:\n        print('leaf',i); print(p[:3000]); print('======')\nEOF"
}
```


### [2026-09-06T21:54:19.160Z] TOOL RESULT

```
leaf 70
ffälligem  q,  arab.  qaträn,  qitran).  akk.  wahrsch.  Jcuprrtu^  Schwefel,
dann  :  >  hebr.  goprtt,  aram.  guprlta,  kuhritä,  Jcebritä  O  arab.  kibrit).
akk.  uhtdu  eine  Alkalienart  :  ;>  syr.  'aJjla,  'vhlä  Lauge.  [akk.
1)  K.  996,  Rev.  10  ff.  (Harper  VI  570).  Es  ist  hier  anscheinend  vom  Erhitzen  des 6u?'a?ZM-Steines  die  Rede.  Daraus  darf  man  vielleicht  schließen,  daß  die  Babylonier  die eigenartige  Krystallhildung  des  Berylls  gekannt  und  verwertet  haben.
2)  Wörtl.  wohl  Schmiere,  von  kapärti  bestreichen,  beschmieren;  vgl.  dazu  unten  S.66.
3)  Jedenfalls  zu  trennen  von  jüd.-aram.  qerd  Wachs  <;^  griech.  xTj^öq.
4)  Die  Stelle  2  Maik.  1,  36  ist  natürlich  für  die  Etymologie  des  "Wortes  väip»a vollständig  belanglos.  5)  Wohl  ganz  zu  trennen  von  PI.  'etrSne  Räuoherwerk.
6)  Bab.  Exp.  Univ.  Penns.  XIV  Nr.  148,  52.  kupritu  könnte  einfach  WeiterbUdimg von  kupru  Erdpeoh,  sein.
      61      
nitiru  wohl   Natron,   nur  vereinzelt   zu   belogen,   wohl,   wie   liebr.  näter, arani.  nitro,  netrö,  griech.  vItqov,  Utqov  usw.,  Natron,  <C  ägypt.  ntrj.] akk.  si];l;ii  und  sHihttu  eine  Art  Alaun  :  >>  s^^r.  SekM}  [akk.  tß-
hat  Amanhn  wahrsch.  Amon-Salz  d.  i.  als  ä(x[^oiviax6v^  Sal  amnioniacum, urspr.  Steinsalz  aus  der  Libyschen  "Wüste,  also  wohl  in  Anleluiung  an  eine ägypt.  Bez.  entstanden.]
akk.  guhlu  Spießglanz,  Antimon,  Stibium  (als  Augenschminke)  : aram.  laMft  (^  spätliebr.  Mhal  die  Augen  schminken,  sowie  arab.  liuhl O  Alkohol),  äth.  hiehel).     Urspr.  Heimat  des  "Wortes  unsicher.  akk.
sadidu  wohl  aucli  Antimon ^  (als  Augenschminke)  :  >  aram.  sodnli'i. akk.  amämfi,  gleichfalls   ein  Schmink  mittel,  aber  viell.  pflanzlicher  Her- kunft.^    Davon  die  Bez.  der  Göttin  Istar  als  Amamitu  :  >  mand.  'Anin- mzt  als  Bez.  des  Planeten  Venus.
akk.  serser{r)i(,  rote  Paste  :  >  hebr.  säscr.  akk.  stjm  Paste  :
>  wohl  syr.  .iijjü  Paste,  sowie  sajäpä  Augensalbe  O  arab.  sijöf,  sowie armen,  vereinzelt  sup'ai),  wie  auch  das  i.  d.  Bed.  bestreichen,  einsalben,  wohl erst  denom.  Verbum  säp.
16.  Himuielsknnde,  Kalender,  Zählung.
Die  sum.-akk.  Namen  der  5  den  Alten  bekannten  Planeten,  bezeichnet nach  den  mit  den  entsprechenden  Sternen  verknüpften  babyl.  Göttern 1)  Nahikt  2)  Istar  {Dilhat,  Biitt,  Istar -halckabe ,  Nana,  Amänütu^), 3)  Nergal,  4)  Marduh  {Bei),  5)  Kaimonu,  sind  hauptsächlich  nur  im  aram. Sprachlcreise,  namentlich  von  den  Harraniern  und  Mandäern,  teilweise direkt  übernommen  worden,  als  1)  Nahö  u.  ä.,  2)  'Estarcl  u.  ä.  {Dilhat  u.a., Beltt,  Kaukabtd,  Nanai,  'AmnmJt),  3)  Nerrg,  4)  Bei  (Kaukahil),  5)  Kewän  ^. Dagegen  sind  sie  zu  den  Griechen  und  Eömeru  in  der  Form  von  Über- tr
======
```


## [2026-09-06T21:54:35.527Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef show(path, needle, ctx=400, maxhits=8):\n    d=open(path,encoding='utf-8',errors='replace').read().split('\\f')\n    n=0\n    for i,p in enumerate(d):\n        if needle in p:\n            n+=1\n            m=p.find(needle)\n            print(f'--- {path} leaf {i} ---')\n            print(p[max(0,m-ctx):m+ctx].replace('\\n',' '))\n            if n>=maxhits: return\n    if n==0: print(f'{path}: NOT FOUND {needle}')\nshow('BQT_v2_pages.txt','سُفت')\nprint('#####')\nshow('BQT_v2_pages.txt','سفت',maxhits=3)\nEOF"
}
```


## [2026-09-06T21:54:36.127Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in incoming/BQT/BQT_v3_pages.txt; do echo \"== $f ==\"; grep -c \"کبریت\" $f; grep -c \"کپی\" $f; done"
}
```


### [2026-09-06T21:54:37.295Z] TOOL RESULT

```
BQT_v2_pages.txt: NOT FOUND سُفت
#####
--- BQT_v2_pages.txt leaf 99 ---
                                                     ‫چش‬  ‫داشته باشد‪ -‬وباضافت‌عتی بکسرها» چشمهاست‬                                                    ‫ي‬                ‫زخم وف‬   ‫در قهستان کهآب آلرا بجپت دفع ملخ باطراف‬            ‫جایبی که از‬     ‫»‬   ‫رشمه‬   ‫بروژن‬    ‫‌‬           ‫حشمه؟‬        ‫ی‬                                ‫و جوانب برد ‪.‬‬          ‫آنجاآب جوشد وروان شود ‪ ۵‬وسفت و سوراخ‬                                                                         ‫سوزن وحوال دوز را نز گوند ‪۰‬‬                              ‫از ولایت طوس ‪.‬‬          ‫چشمه ] تش فشان ه کذابه از آفتاب‬   ‫جشمة سو رن = کنابه ازاهاات تنگی‪-‬‬                        ‫و تنگه چشمی باشد ِ‪.‬‬            ‫ابت‬       ‫جلمه پاسی‌جمی = چشمه‬                                                       ‫تزديك
--- BQT_v2_pages.txt leaf 157 ---
 ‪۲ .‬‬                                       ‫وان الق توا‬                                                               ‫خار = بکون زای نقطه دار ‪ .‬نوعی‬  ‫سین بیاقطه و کون‬                 ‫‪۳‬‬   ‫‪-‬‬       ‫خاسپ‬                                                               ‫آبرا مانند مثقالی‬    ‫از جامهٌ کان باشد و (‪)۱‬‬ ‫بای فااسی سیب رگاویند ‪ ۰‬وآن میوه‌است که‬                       ‫سفته و بشت دار ببافند ‪ -‬و سنك پاشوبرا )<(‬                                                                ‫سر‬   ‫و کثافت را‬     ‫رم‬   ‫چرك و‬   ‫و‬   ‫‪-‬‬   ‫یز گوننه‬                      ‫دوه‬     ‫در‬                  ‫اد‬ ‫د بر وزن فاش »کسی راگوبند‬                      ‫س‬                                                       ‫گفته اند ‪.‬‬ ‫که محبت بافراط داشته باشد ‪ -‬و بمعنی خش‬  ‫®
--- BQT_v2_pages.txt leaf 276 ---
 هم‌هست ‪٩‬‏ ‪:‬‬                                            ‫وعربی وصع خوانند ‪.‬‬          ‫داغ گاز ران = نشانی‌باشد که‌بر کذار‬ ‫دال پور ببای ابجد ودال پوز‬                                              ‫پارچه کنند تا درشستن بدل نشود ‪ -‬و داغیکه‬ ‫با بای فارسی بروزن خام سوز » نوعی از وطواط‬                                                            ‫بهنج چیر نرود ‪.‬‬                        ‫اوسفتر‪-‬اشتروك را نگیوزمند ‪.‬‬                       ‫ارغول‪,‬‬                                                                               ‫ووازومنجه‌ولش ب‬                                                                                             ‫با‬      ‫داغول ‪۲‬‬ ‫دال بوده" ‪ ۰‬ودال پوزه بازبادنی‬                                                         ‫عار ومکار وحرامزاده گروایاد ‪.‬‬ ‫
```


### [2026-09-06T21:54:39.019Z] TOOL RESULT

```
== incoming/BQT/BQT_v3_pages.txt ==
2
8
```


## [2026-09-06T21:54:45.097Z] TOOL CALL #26: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\np='data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt'\nd=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nfor i,pg in enumerate(d):\n    if 'کبریت' in pg or 'کپی' in pg:\n        tag=re.search(r'\\[pdf page (\\d+)\\]',pg)\n        print(i, tag.group(1) if tag else '?', [w for w in ('کبریت','کپی') if w in pg])\nEOF"
}
```


## [2026-09-06T21:54:45.700Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T21:54:46.753Z] TOOL RESULT

```
16 17 ['کپی']
336 337 ['کبریت']
380 381 ['کبریت']
383 384 ['کپی']
385 386 ['کپی']
486 487 ['کپی']
540 541 ['کپی']
541 542 ['کپی']
662 663 ['کپی']
```


### [2026-09-06T21:54:46.792Z] TOOL RESULT

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


## [2026-09-06T21:54:51.449Z] TOOL CALL #28: Bash

```json
{
 "command": "python3 - <<'EOF'\np='data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt'\nd=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (380,385):\n    t=d[i]\n    print('======= leaf',i,'=======')\n    print(t[:2600])\nEOF"
}
```


### [2026-09-06T21:54:53.203Z] TOOL RESULT

```
======= leaf 380 =======
[pdf page 381]
aS
‏را ماست با‎ col JT te ‏آش: کیر باشد‎
‏گویند. با بمعنی‌آش است‎

کیرد = ‎ch‏ ۳ و الی‌وثالت‌وسکون
کاف » کیاهی است خاردار که ‎IGT‏ بعربی ‎CLs‏
‏و بثیرازی خارسوحك و صفاهالی هردا گوبند
و در مرب حمض(۱) الامیر خوانشد.ضماد کردن
بر ورمهای گرم تافع است .

کیروا ۱ باواو بر وزن و ‎we‏
‏کبرپاست که آشکیر باشد چه درفارسی‌بای!بجد
و ‎Jas ce aly‏ میابند چن‌انکه ماست با را
ماست‌وا هم میگو بند .

کبریت ۴ = یک اول وسکون ثانی
و ات بتحتانی رسده و بفوقالی زده ۰ گو گرد
راکوبند وآ نکرم و خشك است ددچهارم وافام
آن درک و کرد مذ کور میشود = و زر خالص را
نیز گفته‌اند . عربی‌است

کیست © بفتح اول وثانی بروزن ‎oS‏
‏رستنیی‌باشد تلخ شبیه بدستنبوی که بعربی‌حنظل
وبفارسی خربزهتلخ گویند؟ . و ‎aah‏ چارموضع
شخصی را عقرب گزید دو درم حنظل بآن شخص
دادند تا مخورد. همن که خورد درد بررطرف شد.

(۱) خم۱ : خنس

. ‏(هم)‎ b= ۱

رو اس

اکر حنظل را بمقدار ‎ety‏ ناختی سوراخ کنند
و پراز دوغن زبق ‎Wik‏ و سوراخ ‎LT‏ باخمیر
محکم بگیرند و بر بالای آنش نهند تا جوشی
چند بزند و بعد از ‎OF‏ بردارند و برموی سفید
مالند سیام کند. ‎oly‏ خضابیت آزموده؛ وبسنی
کویند کیست غیر حنظل است وآن گیاهی باشد
بغابت ‎ight‏ وزهر ‎Jee‏ را نیز کبست گویند -
و در ‎Meith fe‏ پوست نی‌شکر را گفته‌اند.

کبمتو * = بر وژن ارسطو » بمعنی
‎Sash ST‏ زه ‎AS‏ و حنظل است

کسته * = بفتح اول و ‎yt‏ و سکون
سین و فوقالی » بمعئو کبتو بائد که حنظل
وزه ‎AS‏ است .

‎SS‏ بنتح اول و سکون انی و کاف
تازی » دست را
گوبند که‌عربان
بدخوانندوبضی
کف دست را
گفته‌اند ‎٩‏ -و
باکاف فارسی پر نده

‏ایت مشهور و معروف۷ - ‎ob‏ دوقسم میباشد:

‏۴ - در زبان اکدی صورت ‎Kupritu‏ آمده و ازآنجا

‎۰81۳۵6 ‏ودر عبری‎ Bafti ‏ودرآرامی فلسطین‎ guetta ‏زبانهای‌سامی دیگررفته. درآرامی‎ ine

‏در عربی« کبربت» «معجمیات عربیه - سامیه ص ‎NAN‏

‎pS = ۳‏ = کیته (هم) :

‏کیست نام فارسی ‎he‏ است « فولری ‎TE‏ ۰۷۹۱ ۶ عقار ۱۵۸ ف »۰ معرب آن کية است

‏«عقار ۱۵۸ © اوستا -
روز من کشت ازفراق تواشب

‏۴ کست ۴ کسته ‎Cem)‏

‎«bis ۸۵۰ ‏«اسشق‎ kapast ‏پهلوی‎ .kapasti
‏دال ]دهخدا) کبست.‎ gg] ‏توش من‌شدازآن دهاات(از اندهانت‎

‏اورمزدی ‎ol?‏ فری 4۵ >.

‎oS = 8‏ کبتو (هم):

‏با ابنهمه لطافت وشیربنی‌سخن ‏ با من‌بگاه ‎Cab‏ زدن‌چونکیسته‌بی. نزاری قهستانی «رشیدی».
۲ - سراج احتمال میدهد باين ‎ine‏ «کقك » را بتسحیف خوانه‌اند «فرهنگه‌نظام».
۷ - قن : مانسکریت ‎kapinjala_‏ ( دراج (. بلوچی ‎kawinjar . kapinjar‏
‎(LS)‏ »کردی ع ‎qewgh , keu‏ قی ‎kabk sisal. kawk , kdik gus:‏ بلوچی
8 , 18۷8 . رك : اسشق ۸4۱ ‎ELT‏ پرنده‌ای از ‎tes‏ «ماکیانپا» است که بجهت استفاده

‏از کوشت

‏وی ۰ آلرا شکا رکنند .

======= leaf 385 =======
[pdf page 386]
مهو

‎ty y‏ دیگر را ‎ate‏ فی‌الحال ماده گردد و با
اوجفت شود . کوبند با خود نگامداشتن‌استخوان
او قوت باء دهد ‎٩‏ .

‏کیه ۴ - ‎ga‏ اول و ‎gl‏ مشدد و ‎wt‏
‏مشدد » شاخ و شيشه و کدوی حجامان بأشد
که بدان حجامت کنند؛ ونم اول نیز آمده‌است

‏کتابون
‏کپی ۴ = بفتح اول و کسر ثالی مشدد
وفیر مشدد , میموترا کوبند عموماً - و میمون

‏سیامرا خصوصا؟ - ویزبان علمی هدز مورا
کپی‌مبگونند؟ وآن جانوری‌است شبیه بآدمی.

‏کییدن ۰ بر وزن ‎Oded‏ | بمعنی
ربودن باشد .

‏بیان چهارم

‏در کاف تازی با تای‌فرشت

‏کت ه بنتم رل و سکون ‎Ad‏
‏پادشاهانرا گویند عموماً ۱ و تخت پادشاهان
‎sts Gees‏ مین بافته باشند -
وبمعنی کاریزهم آمده‌است چه چاهجو و کاریز کن
راکتکن میگوبند - و بمعلی نخته و چوب نیز
آمده است سیب ‎ST‏ درود گر را کتگرو کنکار
میگوبند - ‎Jol Gs‏ بمعن ی که تراباشدچنالکه
کوبند «کت گفت » بعن ی که تراگفت .

‏۱ < کیوك ‎Cea)‏
‏مانسکرت -
و رك : تاوادیا ۲:۱۹۷ » ورگ : کبی .

‏شب زمستان بودکیی سرد بافت

‏«رودکی ممرفندی ج ۳ ص ۱۰۷۷.
قاپیدن ازقاپ ‎FF‏ بمعنی ربودن .

‏که برخون ‎Sly‏ وافرت ‏ برم زی‌سراندب ‎Fe‏ سرت .

‏۴ کبه (هم) .
01 > هویشمان . ص ۸۷ > ورك :

‏مشتمل برسی ودو لغت و کنایت

‎ror‏ © بروزن خطا , بز بان زندویازند
کتابت وفرمان ونامه راگوبند .

‎aca » ۸ OLE‏ اول وضم بای ابجد
بروزن فلاطون , نام مردی - ونام زلی بوده‌است
و درفرهنکه جهالگیری و مویدالفظلا نام ‎FF‏
‎pad‏ روم‌نوشته‌اند که زن کشتاسب بودموأسفندبار
ازوست : لیکن در مجمع الفری ‎ol oor‏
معنی بجای‌بایا بجد بای‌حطی] مده‌است: الاعل .

‎gikaptk ot. ‏پارسی‎ -
Laufer, Sino _ ۹ p. 581

‏کرمکی شب تاب ناگاهی بتفت .

‏۴ رگ :کبی ‎OVO Ns‏ - قی:
۱ - قی :نیمکت :ورله: کتکارکتگر:
اسدی‌طوسی «فرهنکه نظام».

‏۷ هز ‎kata‏ . پپلوی ‎at) mamak‏ کتاب . مراسله) ‎Vy Sy?‏
‎BA‏ مسحف «کتابون *. بوستی درنامنامة ابرانی (ی۱۵۹) نوبد : > 16816200
لضت نام برادر فربدون است طبق ‎Ja‏ بندحش فصل ۳۱ بند ۸ »که فردوسی آثراکیالوش ( در
‎Jol‏ بی‌نقطه ) بجای کتابون آورده - دوم دختز پادشاه روم وزن گشتاسب و مادر اسقندیار امت که
تلم دیگرش را ‎as‏ کفته اند و فردوسی و مژلف مجمل التواريخ ( ژورنال آزباتيك ‎TID‏ ]1 ,
‎(ort ۳‏ بدین معنی آورده اند , اما پهمن نامه چاپ مول ( شاهنامةٌ فردوسی۱:16۷111)
اورا دختر پادشاه کشمیر محسوب داشته‌است .» ولی درمجمل التواریخ چاپ مرحوم بهارس۵۳ نام
دختر ملك کشمیر « کابون»آمده . ولف در قهرست شاهنامه کتابون 16208008 ضبط کرده و
گوید : دختر ‎eed‏ روم و زنک یکشناسب است . رل : مزدتسنا صس ۳۳۰ . و «کنایون » صحیح

‏بنظرمیرسد . رك: پبرنیا . داستانهای ابران قدیم ص*۱۲۰ .
```


## [2026-09-06T21:55:12.411Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d))\nfor i in range(596,606):\n    print('--- leaf',i,'---')\n    print(d[i][:900])\nEOF"
}
```


## [2026-09-06T21:55:13.101Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSF کپی ==\"; grep -n \"کپی\" FSF_pages.txt | head; echo \"== MON کبریت ==\"; grep -n \"کبریت\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T21:55:14.033Z] TOOL RESULT

```
684
--- leaf 596 ---
  ‫‪۱۳‬‬                                                                                        ‫سروشه‬

                                                         ‫و مصالع آن رو" بدو مقرر است خودهم بتدبیر‬
 ‫وح‌اول بمعنی‌سرین است که شت‌گاه‌مردمان‬            ‫=‬     ‫ومصالح آن‌روز می‌پردازد‪ .‬بنابرآن بجهت‌شرف‬
                         ‫وکفل چاربابان باشد ‪۰ ۴‬‬        ‫آن روز راعد کنند وجشن سازند » ولیزهر کدام‬
 ‫وتا‬      ‫ر‬     ‫کاله‬       ‫ك‬        ‫سر ونار‬             ‫از سروشها بمحافظت جوهری وعنصری مقرراست‬
  ‫راگوبند چه ناز بمعتی لورسته عم آمده | ت‬                ‫چنانکه خرداد بآرب مو کل است و اردیبهشت‬
‫سوروبرا یزکوبند که شاخپای آن بهر طرف‬                    ‫بآرتش و مرداد براشجار وبافی سروشرابمحافظت‬
                                                       ‫آیچه در بل نام آن سروش مقرر ات ‪ -‬ونام‬
                                        ‫ماوزسیقی ‪.‬‬      ‫ن بدست‌اوست‬   ‫ان
--- leaf 597 ---
  ‫صری‬                                                                                 ‫ه‬
                                                                                      ‫ا‪۱‬‬‫‪۳۱‬‬
                                                                                         ‫‪-‬‬


 ‫سر هنګ رک بروزن‌فرهنگه ؛سردار‬                     ‫پوسندیده و برگزبده واعلی وفیس باشد چذان‬
‫پویشرو لشکر و سیاء باشد» چه هنگه بمعنی‬            ‫وعبیدب‌دار را یابه گویشد‬ ‫که هرچیز زیون و‬
‫سپاه لیز آمده است ‪ -‬و بمعنی پهلوان و مبارز‬        ‫‪ -‬و شقة حریر سفید علم را یز میگوبند ‪٩‬‏ ‪-‬‬
                                   ‫همکفته‌اند ‪.‬‬
                                                  ‫و بمعنی اصل هم آمده است چنانکه فرع‌راپابه‬
                                                                                      ‫خوانند ‪.‬‬
 ‫سرق = بفتح اول بروزن پری» سرداری‬
                                    
--- leaf 598 ---
    ‫‪-۱ ۱۳۹‬‬
‫هآممده است ‪ ۵‬و‪-‬نام ولابتی وجایی‌بیز هت‬                         ‫»ن درمچه ‪ .‬نام جانوری‬   ‫بررچوز‬  ‫س‬
      ‫ویمربی‌آور‬    ‫‪-‬‬   ‫‪۹‬‬   ‫که فارکیضرو آنجا است‬
                                                              ‫است پرنده وکوچك جثه و دراز دم که یشتر بر‬
                                  ‫و تخت راگوبند ‪.‬‬
                                                               ‫کتارهای آب شیند ودم جنباند وآنرا مرغ‌فاطمه‪.‬‬
‫سریرافراز = بزای شله دار (‪)۱‬‬                                                  ‫خوانند ورحربی صموه کوبند ‪. ۱‬‬
‫و‬      ‫و غاری که کی‬            ‫در آخر » نام شهربت‬

‫ن آن رفت و غاب شد در نواحی آن شهر‬                               ‫یه ‪ ۴‬مشسبلاخمادیار بورزن‬
                                                     ‫بدرو‬
                                             ‫‪Y۷‬‏ ‪.‬‬       ‫ات‬   ‫خلیفه » مرخ سقارا گویند» وآن پردماست که‬
‫سر 
--- leaf 599 ---
                                                                                          ‫پا احد‬

‫شنجرف سوخته است » بعنی شنجرف عملی‬                    ‫بخورند وبعد‬       ‫مات‬
                                                                         ‫منداوب‬
                                                                              ‫سبزی وتاز کی بیز‬
 ‫که آنرا اسزیماب سازند نآهنکه اکزان‬                 ‫کفش‪-‬‬     ‫سازند و‬   ‫کنند وآرد‬    ‫از رسد کی خشك‬


                                      ‫برآ ورند ‪.‬‬     ‫چبانند ‪٩‬‏ ‪-‬‬       ‫ان‬
                                                                        ‫بزدها‬
                                                                            ‫چی‬        ‫فان‬
                                                                                        ‫حناو‬
                                                                         
--- leaf 600 ---
 ‫‪۱۱۳‬‬
             ‫آمد وسزاوار گردید هم هت ‪4.‬‬         ‫سزا باشد‬          ‫دن*بیزمعنی‬
                                                                           ‫بوز‬
                                                                             ‫سز بل ‪ = ۱‬بر‬

                                                ‫کمعهافات بدی و لیکی ابستم‪-‬عونی لابق‬

                                         ‫داهم‬
                                            ‫بیان ب‬

          ‫درسین بی‌نقطه با سین بی‌نقطه مشتمل برسه لغت کونایت‬
‫کوبند ‪ ۴‬و برکه درخت آن بکرفس مانند‬              ‫‪ ۶‬سست مهار » نم اول و سکون‬
      ‫‪ -‬و رام شدن‌ومطيم | امت وآنرابشیرازی آهو دوستك خوانند‪.‬‬                ‫یم‬
                                                                             ‫طو‬‫کینا»به از رمام‬
                                                                                             ‫ا‬
‫سمعند (‪ 
--- leaf 601 ---
                                                                                          ‫‪۱۳۹‬‬

 ‫مخفف اصطرلاب است »وآن آلتی باشد از برج‬             ‫سطبو س ‪ -‬بابای ابجد بروزن‌محبوس‪,‬‬
                  ‫که بدان‪.‬ارتفاع آفتاب کیرلد ‪۲‬‬     ‫بلغت بونانی کل اارباشد ‪ - ۱‬وآنرا کلنارخوانند‬

‫بفتح اول و سکون‬        ‫سطرو نيون ‪۲‬‬
                                                                                  ‫ومعرب آن جلنار است‬
                                                             ‫سطر ال د بارای ب‬
                                                      ‫نىقطه بو‬
                                                    ‫رزن‬
‫بواو رسیده و نون مکور و تحتالی‬             ‫ناای‬
                                                           ‫افلاك ب‪.‬لغت بونالی دوابی استآنکه‬
                                                   ‫را بفارسی‬
‫بواو کشیده و بنون دبگر زده ؛ بلغت بودانی‬

--- leaf 602 ---
 ‫اه‬       ‫‪۵‬‬                                                                           ‫حواشی‬

                                                                         ‫بقبه از صفحٌ ‪۹۳۱۱‬‬
‫‪ ۵‬سمترب از را تدانتم اکزجا آورده و در اصل چه بوده‬          ‫‪۹‬‬        ‫کوهی » « منتهی‌الارب »‪.‬‬
 ‫که بدینگونه تحریف شده و مطلقاً درنظم وش فارسی من ناکنون بکلمة سمترباز و رتکیبی‬
 ‫مانتد این دربن موردی که ملف برهان قاطم میگوید برنخورده‌ام‪ « ».‬نفیسی ‪ .‬دربار‌چندلفت‬
 ‫» باید داست که سمتری بمعنیی نزدبك قول مولف در‬             ‫‪۲‬ص‪۸۲‬‬‫فارسی ‪ .‬بادتامة پور داود ج ا‬
‫ره ‪ :‬سمترباز ‪ « .‬معلوم شد که سعتر دربنلفت مجه‬                ‫نظم فارسیآمده ‪ .‬رك ‪ :‬سعتری ‪.‬‬
 ‫ممتی است‪,‬چه سمتر بمعنی تره‌ای که درویشان بانان خورند‪,‬اینجا مناسب نیت ‪« » ...‬رشیدی»‬
 ‫سمعانى كوبد ‪« :‬السمتری » هذه النسبةالى بیم‌السعتر و هوشیتی من البقول بجف وبدق بوذرعلی‬
‫الاطممة و ی کل ‪ « » ...‬انناب ورق ‪
--- leaf 603 ---
‫الفبای سفدی‬                                                    ‫برابر صفحه ‪۰4۱۱‬‬




                                               ‫‪ cC‬جر‪۶ ‎‬‬

                                               ‫رد‬
                                                 ‫‪۰‬‬


                                                 ‫کے‬   ‫‪,‬‬   ‫سے‬




                               ‫(قدیم)‬   ‫الفبای صفدی‬

    ‫‪.R ,toihtuaG iassE ed‬‬        ‫‪enneidgoS .‬‏ ‪eriammarG‬‬             ‫اقل از‬
    ‫‪Paris‬‬     ‫‪.‬‏ ‪4191 — 3291‬‬

--- leaf 604 ---
 ‫‪a‬‬

 ‫کے‪‎‬‬

‫په‪‎‬‬



 ‫‪۵‬‬

‫ما‪‎‬‬
‫‪J‬‬
‫‪4‬‬
 ‫د‪‎‬‬



                    ‫الفبای سغدى ( متأخر )‬
       ‫نقل از «بحث دربارة دسنور زبان سضدی » تاليف کوتیو‬

--- leaf 605 ---
                                          ‫بیان چهاردهم‬
              ‫بر بانزده لغت‬          ‫سین بی‌نقطه باغین نقطه‌دار مشتمل‬                ‫در‬


‫سقیین * = بفتح اول و کر بایایجد‬                         ‫ش‬
                                                        ‫شی »‬
                                                           ‫پونوثال‬
                                                                 ‫‪-‬ح او وسک‬
                                                                         ‫سفت‬
                                                                           ‫ب‬
‫بروزن پروین » بلغت بودالی نوعی ازصمن باشد‬            ‫باشد ‪- ۱‬‬     ‫و سقف خاله و کنبد و امثال آن‬
 ‫که بیرون آن سفید و دروش بسرخی مایل‌است؛‬             ‫و لوعی از عمایت طولانی و دراز را فيز گونند‬
                            ‫وبرعکس فيز گفته‌اند ‪:‬‬   ‫و آبرا بمربی ازج خوالند ‪ -‬و شاخ کاو را حم‬
 ‫قد = بصم
```


### [2026-09-06T21:55:14.085Z] TOOL RESULT

```
== FSF کپی ==
17735:                              ‫کپی (بازبر اول)‬          ‫مرا خواری از پوزش و خواهش است‬
17736: ‫میمون‪ ,‬بوزینه‪ .‬پهلوی کپیک ‪610۵‬‬                     ‫وزین نرم گفتن مراکاهش است‬
17742:            ‫ورا شیر کپی همی خواندند‬                 ‫حنظل گویند»‬         ‫رهبی‬
== MON کبریت ==
MON_part2.txt:15717:فوطی کبریت: :0 (تر. ع.] (امر.) 
MON_part2.txt:15718:جعبه‌ای که چوب کبریت‌ها را در آن نهند. 
MON_part2.txt:20075:کبریت: :۲۰۳ [معر.] (.) گوگرد. (ف.) 
MON_part2.txt:20079:خالص. کبریت نباتی: (گیا.) پنجهة گرگك. 
MON_part2.txt:36855:غایت سرخیء گوگرد سرخ؛ کبریت احمر.
```


## [2026-09-06T21:55:36.192Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(604,616):\n    t=d[i]\n    hit = 'کتف' in t or 'شانه' in t or 'دوش' in t\n    print('--- leaf',i,'hit',hit,'---')\n    print(t[:700])\nEOF"
}
```


### [2026-09-06T21:55:37.726Z] TOOL RESULT

```
--- leaf 604 hit False ---
 ‫‪a‬‬

 ‫کے‪‎‬‬

‫په‪‎‬‬



 ‫‪۵‬‬

‫ما‪‎‬‬
‫‪J‬‬
‫‪4‬‬
 ‫د‪‎‬‬



                    ‫الفبای سغدى ( متأخر )‬
       ‫نقل از «بحث دربارة دسنور زبان سضدی » تاليف کوتیو‬

--- leaf 605 hit True ---
                                          ‫بیان چهاردهم‬
              ‫بر بانزده لغت‬          ‫سین بی‌نقطه باغین نقطه‌دار مشتمل‬                ‫در‬


‫سقیین * = بفتح اول و کر بایایجد‬                         ‫ش‬
                                                        ‫شی »‬
                                                           ‫پونوثال‬
                                                                 ‫‪-‬ح او وسک‬
                                                                         ‫سفت‬
                                                                           ‫ب‬
‫بروزن پروین » بلغت بودالی نوعی ازصمن باشد‬            ‫باشد ‪- ۱‬‬     ‫و سقف خاله و کنبد و امثال آن‬
 ‫که بیرون آن
--- leaf 606 hit False ---
  ‫‪NE‬‬

                         ‫خاریشت بز ر گے تبرانداز باشد ‪.‬‬                  ‫سقر ‪. ۱‬۽ بضم اول وفتح ثالی و سکون‬
 ‫آه بفتح اول بر وزن فخری »‬                     ‫سقری‬                      ‫رای قرش(ت‪ )۱‬خ»اریشت کللان را گویند که‌خار‬
 ‫است که کفل اسب و حبوانات‬                       ‫ساغری‬        ‫مخفف‬        ‫حای خود را چون تیر اندازد ؛ و جضم اول وثالی‬
                                                                                ‫‪۱‬‬                         ‫هگفمته! ن ‪.‬د‬
                                               ‫دیگر بائد ‪٩‬‏ ‪.‬‬
                                                                         ‫سقراق ‪ = ۴‬بفتح اول بروزن چخماق‪,‬‬
 ‫سقو = بفتح اول وثال
--- leaf 607 hit True ---
                                                                                       ‫‪۱‬‬
                                                                                       ‫س‬‫ا‪6‬‬
                                                                                         ‫‪۳‬‬

‫ووش که‬
     ‫وضبوط ‪ - ۴‬د‬
               ‫وحکم م‬
                    ‫و لیظ ‪ -‬م‬                          ‫اول همآ مده است ‪۰‬‬    ‫‪ :‬ویک‬      ‫گوند ‪۱‬‬


                                                ‫سقااله > بکر اول بروزن پب‌اله؛بمعتی‬
‫سفت گر * ‪ -‬بنم اول بروزن قغلکره‬                 ‫حفال ات که ریز کوژه وسوی شکته باشد ‪۳‬‬

‫شخصی راکوبند که مروارید ومرجان وامثال را‬        ‫و داسی را بز گونن
--- leaf 608 hit False ---
 ‫=‪— 4‬‬                                                                                                      ‫سفته گوش‬
‫سید ‪ 1‬ے بکراول وفتح ثالی وسکون‬                               ‫چیز که سر آنرا ایزکرده باشند هم هست ؛‬

 ‫دال ابجد‪.‬بمعنی سپد است که زمین باشدوبعربی‬                   ‫و باين معنی بضم اول هم آمده است ‪ -‬و سخن‬
‫اکروضبند ‪ -‬و نام فرشته‌ای هم هست که‌موکل‬                     ‫تازهو نوراهم میگویند ‪ -‬و شخصی که موضمی‬

‫زمین است ‪ -‬و نام ماه دوازدهم و‪-‬ئام روز ینججم‬                 ‫و جابی ازوگرفته باشند و جایگاه دیگر باوداده‬
 ‫باشد از‪.‬الپا و ماههای شمسی؛ودرین روزفارسان‬                  ‫باشند ‪ -‬و بکسر اول » هر چیز غلیظ و سطبر‬
‫جشن کنند وعدد سازند بنا برقاعدء
--- leaf 609 hit False ---
 ‫سفد کاسه‬                                                                                                ‫ع—‬
                                                                                                          ‫\\‬‫ی‬

 ‫تقیض میاه باشد و بعربی ابیض خوانند کونابه‬                         ‫‪۰‬‬   ‫از خالی کردن و تمام کردن هم هت‬

‫چه هر گاه گویند‬         ‫از ظاهر و نمایان هم هت‬         ‫سفر نگ ‪ = ۱‬بفتح ابورلوزن‌خر چدکه‪,‬‬
‫«سفید شد» مرادآن باشد که طاهر شد و نمابان‬
                                                        ‫بمعنی تفیر باشدیعنی «مالی‌وشرحی که ربکلام‬
            ‫گردیده‌وسفید لشد؛یمنی پیدا نشد ‪.‬‬
 ‫سفیل اسفند = بکر اول و همزه‬                                   ‫سقر 
--- leaf 610 hit False ---
                                                          ‫بیان شانز دهم‬
             ‫درسین بی نقطه با قاف مشتمل بر بست و هفت لغت و ابت‬
                                                                                                   ‫سقاقلوس ‪-۱‬‬
                                                                                                    ‫جفتح اول و انی (‪)۱‬‬
                                                                                                    ‫بالف کشیده وضم قان‬
                                                                                                    ‫ولام بواورسنه وسین‬
                                                                                  
--- leaf 611 hit False ---
                    ‫کسهت‌آسمان باشد‪.‬‬
                                   ‫لاجورد ا‬                                          ‫ستسیی‬
                                                     ‫باسین بی نقطه بروزن‌قز وین»‬
‫است ‪-‬‬    ‫آزسمان‬
              ‫سقف مینا = کنابه ا‬                                        ‫نام ولایتی است غر معلوم ‪.‬‬
        ‫ره و سابه‌دار را نیز گوبند‪.‬‬
                                  ‫ورختان بز ک‬
                                            ‫د‬
                                                     ‫سقط ؟ ه بفتح‌اول وثالی‪ .‬بروزن‌ومعنی‬
 ‫سقف نیم خا نه = کنابه اآزسمان‬                                                            ‫خططرا‬
                          
--- leaf 612 hit True ---
     ‫==‬                                                                           ‫سقلاطرن‬
 ‫بلغت بونانی‌دواییاست کهآ درا محمودممی‌گویند»‬
                                                     ‫سقلا طون ‪ ۲‬ب=روزن افلاطون‪.‬بمعنی‬
 ‫وآن عصاره‌ای باشد بغایت نلخ ومهل‌صفرابود ‪.‬‬          ‫جتا‪-‬موة تخجواتیرا نیز کوبند »‬ ‫سقرلات اس‬
 ‫» دوشابآ تشندبد‬        ‫مروزن چس‬    ‫سقن س‬             ‫و بستی کوویند نام شپریست که سقرلات منوب‬
 ‫خرما راگوینده و آنراسبلان هم‌میگونندویعربی‬          ‫بآن شهر ليٿ ‪ -‬و بمعنی رنگه ولون هم آمده‬
                ‫خوانند بکر دال بی‌نقطه ‪۰‬‬      ‫دس‬     ‫است » و بسنی کویند رنگه کبود است چه‬
 ‫بنتح اول وئالی و سکون‬      ‫‪» ۱‬‬    ‫سقنقس‬
                 
--- leaf 613 hit False ---
                                                                                             ‫‪۷۱۷ 6-‬‬

‫و شروع بحر کنند تاآترمان کهاقطة خونی‬                ‫‪ ۰ ۲‬بفتح اول وض‌نانی‬           ‫سقوردیون‬
 ‫در میان قدح آب پیدا شود و بمداز زمانی آن‬            ‫وسکون واو و رای قرشت و کسردال ابجدونعتالی‬
 ‫ردد و آن شخص‬     ‫قدح پر از دل وجکر وکشش‬
                                                   ‫»لفت بودانی سیر‬
                                                                 ‫بواو کشیده و بنون زده ب‬
 ‫در حال بمیرد وچون شکم او را بشکافند جکر‬
                                                              ‫صحرایبی باشد وبعربی ثوم البری خوانند‪.‬‬
                                ‫درشکمش نباش
--- leaf 614 hit False ---
            ‫‪۱‬‬
            ‫= هی‬                                                                                                                ‫صکاد‬
‫بروزن خلاصه » نمعتی سکاسته است که‌خاریشت‬                                     ‫‌نهنده‬       ‫ت سخ‬‫سعنی‬
                                                                                                 ‫وبم‬
                                                                                                   ‫وی »‬‫نارس‬‫شم ف‬
                                                                                                              ‫اجی‬
                                                                                                     
--- leaf 615 hit False ---
      ‫رککه‬
         ‫س‬

‫ووحه‪.‬‬      ‫کنند و هروقت که خواحند صر فکننده‬                         ‫کار صازی‬    ‫و‬       ‫‪-‬‬   ‫وخواستن‬        ‫و آندیشه مند بودن‬


‫نسیك‌سر که وبا‬
             ‫معچه‬
                ‫بست‬
                  ‫تمیه‌اش سرکه با‬                                   ‫فارسی هم آمده‬             ‫واکاف‬
                                                                                                  ‫کردن هم هست ؛ ب‬
                      ‫شه ‪.‬‬ ‫آگمورا‬                                                                                      ‫است‪. .‬‬

 ‫اللوث وسکون‬    ‫سکبه = بنتم او‬                                      ‫سکالو ا‪۲‬ول=ب‌ضومرابع‌بواو کشیده‬
‫ث
```


## [2026-09-06T21:55:46.647Z] TOOL CALL #32: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1143 --image 2>&1 | tail -40"
}
```


## [2026-09-06T21:55:48.497Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if 'کپی' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print('leaf',i,'tag',m.group(1) if m else '?')\n        idx=p.find('کپی')\n        print(p[max(0,idx-500):idx+500])\n        break\nEOF"
}
```


### [2026-09-06T21:55:48.828Z] TOOL RESULT

```
no scan of BQT covers printed page 1143 (see 'scans' in refs_online.json)
```


### [2026-09-06T21:55:51.007Z] TOOL RESULT

```
leaf 360 tag ?
                      ‫سنگین را می‌کشند‪:‬‬           ‫(‪۸‬نوشیروان ‪)۵۰۲۴‬‬

               ‫رد‬
                ‫همه گنج ارجاسپ در بکاز‬                                                     ‫کاهش‬
‫آغاز کرد‬        ‫تمن‬
                  ‫خن در‬
                      ‫سکپا‬
                         ‫به‬                         ‫(اسم صمدر از کاستن)‪ :‬در بیت زیر‬
 ‫(‪)۶-۲۱۲-۷۹۷‬‬                                                            ‫به‌معنی توهین» تحقیر‪:‬‬
                              ‫کپی (بازبر اول)‬          ‫مرا خواری از پوزش و خواهش است‬
 ‫میمون‪ ,‬بوزینه‪ .‬پهلوی کپیک ‪610۵‬‬                     ‫وزین نرم گفتن مراکاهش است‬
               ‫(یادداشت‌های گات‌ها ‪:)۶۲۴‬‬            ‫(‪)۶-۲۶۲-۲۵۷‬‬

     ‫ددی بود مهتر زاسپی به تن‬                                             ‫کبست (بازبر اول دووم)‬
  ‫گشیکسورسن‬                                         ‫«حنظل» (صحاح)» «رستنی باشد تلخ شه‬
          ‫فروهشته چون م‬
            ‫ورا شیر کپی همی خواندند‬                 ‫حنظل گویند
```


## [2026-09-06T21:55:58.854Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[607])\nEOF"
}
```


## [2026-09-06T21:55:59.315Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['FSF']['page_offset']);print(d['MON'].get('page_offset'))\""
}
```


### [2026-09-06T21:56:00.817Z] TOOL RESULT

```
                                                                                       ‫‪۱‬‬
                                                                                       ‫س‬‫ا‪6‬‬
                                                                                         ‫‪۳‬‬

‫ووش که‬
     ‫وضبوط ‪ - ۴‬د‬
               ‫وحکم م‬
                    ‫و لیظ ‪ -‬م‬                          ‫اول همآ مده است ‪۰‬‬    ‫‪ :‬ویک‬      ‫گوند ‪۱‬‬


                                                ‫سقااله > بکر اول بروزن پب‌اله؛بمعتی‬
‫سفت گر * ‪ -‬بنم اول بروزن قغلکره‬                 ‫حفال ات که ریز کوژه وسوی شکته باشد ‪۳‬‬

‫شخصی راکوبند که مروارید ومرجان وامثال را‬        ‫و داسی را بز گونند که بدان غله درو کنند ؛‬
                             ‫سوراخ میکند ‪.‬‬                            ‫‪۰‬‬   ‫رضم اول همآمده ات‬

                                                ‫سفا نی » بفتح اول بروزن امالی»حشیشی‬
‫سفن ‪ = ۱‬بروز ن کفتن » بمعنی سوراخ‬
 ‫شدن باشد ‪ -‬و بمعنی‬        ‫وخ‬
                            ‫ا‬‫ر‪-‬‬
                              ‫و‪۷‬‬‫سدن‬
                                  ‫کر‬            ‫است که آلرا بعربی رعی‌الابل خوانند‪ .‬دان آن‬
             ‫تراومدن وترازش هم آمده است ‪.‬‬       ‫حلاوتی دارد ‪.‬‬   ‫همجو دانهة مورد باشد و الدك‬

 ‫م اول پروزن خفته » هریز‬      ‫سفته =‬            ‫کوبند غیر از شترهرحیوالی دیگرکه بخورد‬
 ‫سوراخ کرده راگوبند همچو مرواربد سفتهولمل‬       ‫بمیزد خصوص جانوران زهردار» وطبیخ آن‌موی‌را‬
                                                                                    ‫ام گنف« ‪:‬‬
‫سفته و مانند آن ‪ - ۸‬و حلقة طلا وشرهرا لیز‬
 ‫گفته‌اند که درکوش کنند‪ .‬وبمعنی تحفهرچیزی‬       ‫سفاهن س بفتح اول و های هوز بروزن‬
 ‫بائد کهشخص بجبت شخصی از ملکی بملك‬                       ‫فلاخن ‪ ۰‬شاه زلف و کسو را گوشد‪.‬‬
   ‫توج‬
     ‫خ‪-‬‬‫بستد‬
          ‫دیگر برسم تکلف بابناعت بفر‬            ‫سفت = منم اول و سکن ثالی‌وفوقانی»‬
‫اول بروزن هفته ‪ ,‬آست کهکی چیزی از کسی‬           ‫دوش راگوبند وبعربی کتف خوانند ‪ - ۴‬وماضی‬
 ‫بطربق عاربت با فرض با در عوض چیزی بگیرد‬        ‫سفتن هم همست که از سوراخ کردن باشد ‪- ۴‬‬
‫تا در شهری دیگر باز دهد ‪ -‬و دست لاف را‬         ‫و مضبوط و صخت لزآمده است‬                 ‫بومعنی‬
 ‫لیز کوبند و آن سودای اول‌اصناف‌وفروشندکان‬      ‫‪ -‬و هر سوراح کوچك را کویند عموما وسوراخ‬
‫باشد *‪ -۷‬و بمعنی پیکان لیر و سنان ليزه وعو‬      ‫سوزن را خصوساً ‪ -‬وبکر اول دیز بمعنی‌سطبر‬

                                       ‫‏‪ - ٩‬نهان ازآن شماید شمیر او (عدو) که دش‬
  ‫انوری‪«.‬فرهتگه نظام‪.۵‬‬        ‫يفبت نوبترکد چو پته سفال ‪.‬‬
                                                       ‫هن‬‫ز‬
   ‫‪( 11‬شانه) ش»غنی‬   ‫‪-0‬‬‫‪0‬تان‬
                          ‫پ‪10‬ا‪1‬ر‪.‬سی باس‬
                                      ‫‪ ۴‬اوستا ‪ ( 110115 -‬شانه ) » بهلوی ‪15‬‬
   ‫‪:‬ربرسن‪.4۹‬‬ ‫‪.‬لبانی ‪2‬لا‪« 5‬امشق ‪ »۹۳۷‬ورك گ‬
                                        ‫‪.‬نکلیچی ‪ 0۷15‬آ‬     ‫‪ , 10‬سریکلی ‪ 10۷65‬س‬
                                  ‫رك ‪ :‬سفتن » در بیت ذبل بپردو معنی آمده ‪:‬‬         ‫‪۴‬‬

     ‫سفت و از هر دو سفت بیرون‌جست‪.‬‬             ‫سفتة (تیر»سنان سرتیز) برسفت‌شیر و گورشت‬
   ‫| رف‬   ‫نظامی گنجوی‪«.‬هفت یبکرچاپ‌ارمضان‬

                                     ‫‪ - ۴‬درزبان کنونی یز ‪ 1665‬گویند ورك ‪ :‬سفته ‪.‬‬
                               ‫( سفتن ) ‪ -۴‬کر( یوند شفل ومبالفه )‪.‬‬        ‫ت‬
                                                                          ‫فز ‪:‬‬
                                                                             ‫س_ ا‬‫©‬
  ‫اعتقاق کلمه را‬   ‫‪.‬و‪4‬‬     ‫«اسشق ‪۰‬‬     ‫‏‪ ( sontin‬سوراخ کردن ( ‪ ۰,‬فقس ‪ 0‬فارسی سمب“‬       ‫کردی‬

             ‫‪.‬‬     ‫( از اوستا ) که هرن در اسشق هل کرده هویشمان مردود مبداند « هویشمان ‪°‬‬

           ‫‪۷‬ر‪-‬شام تابصباحلمای طبعتیز ابن کرده‌ام که گوحر مدح تو سفته‌ام‪.‬‬
                                                                       ‫ه‬

      ‫‪ ٩‬برعم نآ عتقس عمج(‪‎‬جئافس ) ‪:‬‬               ‫آن سقنجه « تفس ؟‪. ‎‬‬     ‫= معرب‬   ‫‪A‬‬

           ‫ترديك تو له مابه له نیز هیچ سفته‪.‬‬       ‫اينك رهی بمژ کان راه توباك رفته‪‎‬‬
   ‫جلاب بخاری ‪,‬لفت فر ‪۵۸4٩‬‏ ‪-‬‬
                                                                  ‫‪.‬‬   ‫رك ‪ :‬صفټ‬     ‫‪۶‬‬
```


### [2026-09-06T21:56:03.898Z] TOOL RESULT

```
484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
None
```


## [2026-09-06T21:56:20.033Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD kwep ===\"; grep -n -i \"kwep\\|kw ep\\|vapor\" AHD_watkins1985.txt | head -20; echo; echo \"=== KLN vapor/cupid ===\"; grep -n \"vapor\\b\" KLN_1971.txt | head -5; grep -n \"^Cupid\\|Cupid,\" KLN_1971.txt | head -5"
}
```


### [2026-09-06T21:56:20.110Z] TOOL RESULT

```
=== AHD kwep ===
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
1144:*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: WIND2; b. Old Norse vinda, to wind: WINDLASS. 2. Germanic causative *wandjan in: a. Old English wendan, to turn to: WEND; b. Dutch wenden, to turn: WENTLETRAP. 3. Germanic *wandr6n, to roam about, in: a. Old English wandrian, to wander: WANDER; b. German wandern, to wander: WANDERLUST. 4. Germanic *wanduz in Old Norse véndr, a supple twig: WAND. 5. Germanic *wandljaz, “wan- derer,” perhaps in Latin Vandalus, a Vandal: VANDAL. [Pok. 1. uwendh- 1148.] weng-. To bend, curve. 1. Germanic *wink- in Old Eng- lish wincian, to close the eyes (< “to bend down the eyelids”): WINK. 2. Germanic *winkja in Old English wince, a reel, roller: WINCH. 3. Germanic *winkil- in Old English -wincel, spiral shell: PERIWINKLE!. 4, Germanic *wankil-, *wankul- in: a. Old English wencel, youth, maid (< “inconstant one’): WENCH; b. Old English wancol, inconstant, unsteady: wonky. 5. Germanic *wankj- in: a. Old French gauchir, to turn aside: GAUCHE; b. Anglo-Norman *wencir, to turn aside, avoid (> Middle English wincen, to kick): w1NcE. [Pok. we-n-g- 1148.] wep-. Bad, evil. From earlier *awep-. Suffixed zero-grade form *up-elo- in Germanic *ubilaz, evil, in Old English yfel, evil: EVIL. [wépnam. Weapon. Germanic root. 1. Old English wé- P(e)n, weapon: WEAPON. 2. Old Norse vapn (plural vdpn), weapon: WAPENTAKE.] wer-', High raised spot. 1. Suffixed form *wer-d- in Germanic *wartén- in Old English wearte, wart: WART. 2. Possibly Germanic *war- in obsolete Swedish var- bulde, “pus swelling” (bulde, swelling; see bhel-2), akin to the source of WARBLE2. 3. Latin varius (genitive plural variérum), spotty, speckled, changeable: (VAIR), VARIE- GATE, (VARIETY), VARIOLA, VARIORUM, VARIOUS, VARY; (MINIVER). 4. Latin varix, varicose vein: VARIX. 5. Suf- fixed and extended zero-grade form *wrsu-ko- in Latin verriica, a wart: VERRUCA. [Pok. 2. wer- 1151, 2. ud- 1108.] wer-2. To raise, lift, hold suspended. Earlier form *ower-. 1. Basic form *awer- in Greek aeirein, to raise, and Greek artéria, windpipe, artery: AORTA, ARSIS, ARTERIO-, ARTERIOLE, ARTERY. 2. Possibly referred to this root (obscure basic form *dwer-) is Greek aér (> Latin aer > Italian aria), air: AERIAL AERO-, AIR, ARIA, MALARIA. 3. Related to Greek aér, air, is Greek aura (< zero-grade form *aur-), breath, vapor: AURA. [Pok. 1. wer- 1151.] wer-3, Conventional base of various Indo-European roots; to turn, bend. I. Root *wert-, to turn, wind. 1. Germanic *werth- in: a. Germanic variant *warth- in (i) Old Eng- lish -weard, toward (< “turned toward”): -WARD (ii) Germanic *inwarth, inward (*in, in; see en), in Old English inweard, inward: INWARD; b. perhaps Germanic derivative *werthaz, “toward, opposite,” hence “equiv- alent, worth,” in Old English weorth, worth, valuable, and derivative noun weorth, wierth, value: WORTH}; STALWART. 2. Germanic *werthan, to become (< “to turn into”), in Old English weorthan, to befall: worTH?. 3. Zero-grade form *wrt- in Germanic *wurth- in Old English wyrd, fate, destiny (< “that which befalls one”): WEIRD. 4, Latin vertere, to turn, with its frequentative versare, to turn, and passive versari, to stay, behave (< “to move around a place, frequent”): VERSATILE, VERSE}, VERSION, VERSUS, VERTEBRA, VERTEX, VERTIGO, VOR- TEX; ADVERSE, ANNIVERSARY, AVERT, BOULEVERSE- MENT, CONTROVERSY, (CONVERSE!), CONVERT, DEXTRORSE, DIVERT, EVERT, (EXTROVERSION), EXTRO- VERT, INTRORSE, INTROVERT, INVERT, MALVERSATION, OBVERT, PERVERT, PROSE, RETRORSE, REVERT, SINIS-
1165:wet-'. To blow, inspire, spiritually arouse. Related to wé-. 1. Lengthened-grade form *w6t- in Germanic suffixed form *wéd-eno-, *wéd-ono-, “raging,” “mad,” “inspired,” hence “spirit,” name of the chief Teutonic god, in: a. Old English Woéden, Woden: WoDEn; b. Old English Wod- nesdxg, ““Woden’s day”: WEDNESDAY; Cc. Old Norse Odhinn, Odin: Opin; d. Old High German Wuotan (> German Wotan), Wotan: WoTAN. 2. Lengthened variant form *wdt- in Latin vdtés, prophet, poet: vaTic. 3. Suf- fixed variant form *wat-no- in Latin vannus, a winnow- ing fan: FAN!, vAN3. 4, Oldest basic form *awet- becoming *awet- in suffixed form *awet-mo- in Greek atmos (< *aetmos), breath, vapor: ATMOSPHERE. [Pok. udé- 1113.]
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
2445:VAIR wer-1 VaisyA_ weik-1 VALE! wel-3 VALEDICTION deik- VALENCE wal- VALET upo VALETUDINARIAN wal- VALHALLA kel-2, wele-2 VALIANT wal- VALID wal- VALKYRIE wele-2 VALLATION walso- VALLEY wel-3 VALONIA gWele-2 VALOR wal- VALUE wal- VALVE wel-3 VAMOOSE wadh-2 VAMP! ped-1 vaAN3 wet-1 VANADIUM wen-1 VANDAL wendh- VANE pan- VANG pag- VANILLA wag- VANIR wen-! VANISH eu-2 VANITY eu-2 VANQUISH welk-5 VAPID kwép- VAPOR kwép- VAQUERO wak- VARA wa- VARIEGATE wer-1 VARIETY wer-1 VARIOLA wer-! VARIORUM wer-! VARIOUS wer-1 VARIX wer-1 VARLET upo VaRUNA wel-1 VARUS wa- VARVE kwerp-

=== KLN vapor/cupid ===
12401:‘sublimed vapor’, a derivative of at&eiv, ‘to 
22199:meaning ‘vapor’. — Gk. AxfxtSo-, drqxtS-, fr. 
22200:Axp,k, gen. Axfxl&o<;, ‘steam, vapor’, rel. to Ax|x6s, 
22207:meaning ‘vapor*. — Gk. Atjxo-, Atjx-, fr. Axp. 6 $, 
22208:‘steam, vapor’, contraction of Aerpt6<;, which 
5172:Cupid. 
61688:Cupid, n., the god of love in Roman mythology. 
61705:Cupid and -ity.
```


## [2026-09-06T21:56:22.099Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kupsins\\|kupsin\" POK_0*.txt POK_full.txt | head; echo \"---WLD I 467---\"; grep -n \"supti\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head; echo \"---WLD kuap---\"; grep -n \"kupsins\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head"
}
```


### [2026-09-06T21:56:22.168Z] TOOL RESULT

```
---WLD I 467---
29417:Ai. cupti-, av. supti- „Schulter“; alb. sup (G. Meyer Alb. Wb. 396, Pedersen 
---WLD kuap---
23949:naties „aufgehn (vom Teig)“, kupt „garen", apr. kupsins „Yebel“ (Ab-
```


## [2026-09-06T21:56:37.509Z] TOOL CALL #38: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\np='data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt'\nd=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nfor i,pg in enumerate(d):\n    if 'supti-' in pg and 'cupti' in pg:\n        m=re.search(r'\\[pdf page (\\d+)\\]',pg); print('supti leaf',i,m.group(1) if m else '?')\n        j=pg.find('cupti'); print(pg[max(0,j-600):j+400].replace('\\n',' '))\n    if 'kupsins' in pg:\n        m=re.search(r'\\[pdf page (\\d+)\\]',pg); print('kupsins leaf',i,m.group(1) if m else '?')\n        j=pg.find('kupsins'); print(pg[max(0,j-900):j+300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T21:56:39.295Z] TOOL RESULT

```
kupsins leaf 388 ?
d. huap „dropsical flesh".   Dagegen ags. hoppian mhd. hopfen, hupfen „hiipfen“ (Yoreen Ltl. 154)                             ,   zu keubQi)- „Kvfhoxav“\ auch ags. hopian mnd. hopen „hoffen" (Fick III 4                                                 ,   93, Falk-Torp u. haab) bleibt fern (von Weigand-Hirt als „aufspringen, erwarten, hoffen" mit dem vorigen verbunden; unsicher). Auch got. hopun „sich riihmen, prahlen", ags. hwopan „drohen“ ist in der Bed. nicht glaub- haft zu vermitteln, s. Feist Got. Wb. 152 f., und sdmmt im Ausl. nicht.   Lit. Jcvapas „Hauch, Dunst, Wohlgeruch" (: lat. vapor), Jevepiu, -eti „duften“ (-e- kann bait. Ablautneubildung sein), kvepiii ,kv?pti „hauchen“, lett. Jcvepl „qualmen“, kvepes PI. „Hauch, Qualm, Dampf, RuB", kvepet „rauchern“, lit. kupuoti „schwer atmen", lett. kupet „rauchen, dampfen, stieben", kupi-  naties „aufgehn (vom Teig)“, kupt „garen", apr. kupsins „Yebel“ (Ab- leitung von einem es-St. wie lat. vapor) s. Trautmann Apr. 365; zur bait. Sippe uberhaupt a. Leskien Abl. 333. Aksl. kypljq, kypeti „\vallen, uber- laufen" (usw., s. Berneker 677), kypn „locker, poros", cech. kypry alt „strebsam, emsig, frisch"; klr. kvapyty sa „sich sputen, eil
supti leaf 475 ?
lg. kukavica „Kuckuck“,                             lett.  sei'b.    kukavica, russ. kukiisa usw. ds., r. kukovdtb usw. „ wie ein Kuckuek rufen“.   Ygl. Curtius 5 152, Fick I 4 21 und fiber nhd. Gauch usw., lit. gegide usw. „Kuckuck“ auch Meillet Msl. 12, 213ff., Suolabti Dt. Yogeln. 4f.  kudh- „Mist, Kot“.    Gr. vo-xv&a'               vog      apodsvpa Hes.,                     y.vkkm deog'       dvooopov Hes., y.vdvov „oueQ/ua u           Hes.:     lit.   siidas ,        lett.   suds „Mist, Kot‘\                Fick I 4 426. Boisacq u. y.vdvov.   kup- „Schulter“ (germ, mit anl. s-).    Ai. cupti-, av. supti- „Schulter“; alb. sup (G. Meyer Alb. Wb. 396, Pedersen KZ. 36, 337) „Schulter, Riicken“ (ohne formantisches -t-)\ mnd. schuft m., ostfries., ndl. schoft „Vorderschulterblatt einer Kuh, eines Pferdes“ *skuftu -).                                                                       (     Bezzenberger BB. 1, 341, Bartholomae Stud. II 15, Fick I 4 46, 209, III 4 470.    Dagegen got.
```


## [2026-09-06T21:56:46.259Z] TOOL CALL #39: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-06T21:56:46.300Z] TOOL RESULT

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
```


## [2026-09-06T21:56:52.430Z] TOOL CALL #40: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%81%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%BE%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/%D9%83%D8%A8%D8%B1%D9%8A%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%A8%D8%B1%DB%8C%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/vapor\" \\\n \"https://en.wiktionary.org/wiki/cupio\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%AA%E0%A4%BF\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 286 verification\"; done 2>&1 | tail -30"
}
```


### [2026-09-06T21:57:02.211Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%B3%D9%81%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/cfdefe1e3cef4e2a.txt
### https://en.wiktionary.org/wiki/%DA%A9%D9%BE%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/34469241666eda5f.txt
### https://en.wiktionary.org/wiki/%D9%83%D8%A8%D8%B1%D9%8A%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/33ccbafff13d2f83.txt
### https://en.wiktionary.org/wiki/%DA%A9%D8%A8%D8%B1%DB%8C%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/79c7b20bba013b98.txt
### https://en.wiktionary.org/wiki/vapor
/home/sfmqrb/git/rishe/data/verification/sources/web/d5463b66e4ae8987.txt
### https://en.wiktionary.org/wiki/cupio
/home/sfmqrb/git/rishe/data/verification/sources/web/9334e8741e99f0d2.txt
### https://en.wiktionary.org/wiki/%E0%A4%95%E0%A4%AA%E0%A4%BF
/home/sfmqrb/git/rishe/data/verification/sources/web/9791cae960fca70d.txt
```


## [2026-09-06T21:57:05.185Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"===== سفت =====\"; grep -n -A30 \"^Persian\" cfdefe1e3cef4e2a.txt | head -60"
}
```


### [2026-09-06T21:57:05.235Z] TOOL RESULT

```
===== سفت =====
```


## [2026-09-06T21:57:05.897Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"===== کپی =====\"; sed -n '1,200p' 34469241666eda5f.txt | grep -n \".\" | sed -n '40,160p'"
}
```


### [2026-09-06T21:57:05.958Z] TOOL RESULT

```
===== کپی =====
64: 1.1.1 
65: Pronunciation 
67: 1.1.2 
68: Noun 
70: 1.1.2.1 
71: Alternative forms 
73: 1.1.2.2 
74: Derived terms 
76: 1.2 
77: Etymology 2 
79: 1.2.1 
80: Pronunciation 
82: 1.2.2 
83: Noun 
85: 1.2.2.1 
86: Alternative forms 
88: 1.3 
89: References 
91: Toggle the table of contents 
93: کپی 
95: 10 languages 
97: فارسی 
98: Magyar 
99: Kurdî 
100: Lietuvių 
101: Malagasy 
102: Nederlands 
103: Polski 
104: پنجابی 
105: Română 
106: Русский 
108: Entry 
110: Discussion 
112: English 
114: Read 
116: Edit 
118: View history 
120: Tools 
122: Tools
124: move to sidebar 
125: hide 
127: Actions
129: Read 
131: Edit 
133: View history 
135: General
137: What links here 
138: Related changes 
139: Upload file 
140: Permanent link 
141: Page information 
142: Cite this page 
143: Get shortened URL 
145: Print/export
147: Create a book 
148: Download as PDF 
149: Printable version 
151: In other projects
153: Appearance
155: move to sidebar 
156: hide 
158: From Wiktionary, the free dictionary
160: See also: کتي and کتی 
162: Persian
163: [ edit ] 
165: Etymology 1
166: [ edit ] 
168: Etymology tree
170: Proto-Indo-European *ḱe ? 
171: Proto-Indo-European *ḱóm 
172: Proto-Italic *kom 
173: Proto-Italic *kom- 
174: Latin co- 
176: Proto-Indo-European *h₃ep- der. 
177: Proto-Italic *opis 
178: Latin ops 
180: Latin cōps 
182: Proto-Indo-European *-(i)yós 
183: Proto-Italic *-ijos 
184: Proto-Italic *-ios 
185: Old Latin -ios 
186: Latin -ius 
187: Latin -ia 
189: Latin cōpia bor. 
190: French copie bor. 
191: Persian کپی 
193: Borrowed from French copie .
195: Pronunciation
196: [ edit ] 
198: ( Iran, formal ) IPA ( key ) : [kʰo.pʰíː] 
200: Readings
```


## [2026-09-06T21:57:10.215Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '200,300p' 34469241666eda5f.txt"
}
```


### [2026-09-06T21:57:10.260Z] TOOL RESULT

```
 Readings

 Iranian reading ? 

 kopi

 Noun
 [ edit ] 

 کپی • ( kopi ) 

 copy (both the activity and the result)
 Synonym: رونوشت ( runevešt ) 

 Alternative forms
 [ edit ] 

 کاپی ( kâpi ) ( from English ) 

 Derived terms
 [ edit ] 

 کپی کردن ( kopi kardan ) 

 Etymology 2
 [ edit ] 

 Inherited from Middle Persian [script needed] ( kpyk' /⁠kabīg⁠/ , “ monkey ” ) , from Sanskrit कपि ( kapi , “ ape, monkey ” ) . Akin to Old Armenian կապիկ ( kapik ) ; an Iranian borrowing.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ka.ˈpiː/ , /kap.ˈpiː/ 

 ( Dari, formal ) IPA ( key ) : [kʰä.pʰíː] , [kʰäp.pʰíː] 

 ( Dari, formal ) IPA ( key ) : [kʰä.pʰíː] , [kʰäp.pʰíː] 
 ( Kabuli ) IPA ( key ) : [kʰä.pʰíː] , [kʰäp.pʰíː] 

 ( Hazaragi ) IPA ( key ) : [kʰä.pʰí] , [kʰäp.pʰí] 

 ( Iran, formal ) IPA ( key ) : [kʰʲæ.pʰíː] , [kʰʲæpʰ.pʰíː] 

 ( Tajik, formal ) IPA ( key ) : [kʰä.pʰí] , [kʰäp.pʰí] 

 Rhymes: -iː 

 Readings

 Classical reading ? 

 kapī, kappī

 Dari reading ? 

 kapī, kappī

 Iranian reading ? 

 kapi, kappi

 Tajik reading ? 

 kapi, kappi

 Noun
 [ edit ] 

 کپی • ( kapi or kappi ) 

 ape , monkey 
 Synonyms: میمون ( meymun ) , بوزینه ( buzine ) 
 c. 1030 , Farrukhī Sīstānī , “Qaṣīda 171”, in دیوان فرخی سیستانی [ Dīvān of Farrukhī ]‎ [1] : شیری که پیل بشکند از بیم تیغ تو
اندر ولایت تو چو کپی رود ستان šērē ki pīl biškanad az bēm-i tēġ-i tu
andar wilāyat-i tu čū kappī rawad sitān Out of fear for your blade, the lion that brings down elephants
Walks feebly like the monkey in your domain. (Classical Persian transliteration) 

 Alternative forms
 [ edit ] 

 کبی ( kabi, kabbi ) 

 References
 [ edit ] 

 Steingass, Francis Joseph ( 1892 ), “ کپی ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 

 MacKenzie, D. N. ( 1971 ), “kabīg”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=کپی&oldid=92020754 "

 Categories : Persian terms derived from the Proto-Indo-European root *h₃ep- 
 Persian terms derived from the Proto-Indo-European word *ḱe 
 Persian terms borrowed from French 
 Persian terms derived from Proto-Indo-European 
 Persian terms derived from Proto-Italic 
 Persian terms derived from the Proto-Indo-European word *ḱóm 
 Persian terms derived from Old Latin 
 Persian terms derived from French 
 Persian terms derived from Latin 
 Persian terms with IPA pronunciation
```


## [2026-09-06T21:57:11.441Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Middle Persian\\|Etymology\\|shoulder\\|Avestan\\|Proto-Iranian\" cfdefe1e3cef4e2a.txt | head -40"
}
```


### [2026-09-06T21:57:11.489Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:57:23.953Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c cfdefe1e3cef4e2a.txt && head -40 cfdefe1e3cef4e2a.txt; echo \"=== kapi skt ===\"; grep -n -i \"Etymology\\|monkey\\|uncertain\\|Mayrhofer\\|Proto-Indo\" 9791cae960fca70d.txt | head -30"
}
```


### [2026-09-06T21:57:24.023Z] TOOL RESULT

```
2536 cfdefe1e3cef4e2a.txt
URL: https://en.wiktionary.org/wiki/%D8%B3%D9%81%D8%AA
FETCHED: 2026-09-06T21:56:55Z
STATUS: 200
TITLE: سفت - Wiktionary, the free dictionary

سفت - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

=== kapi skt ===
62: Etymology 
96: Etymology 
193: Etymology
208: monkey , ape 
277: Devanagari script form of kapi ( “ monkey ” ) 
320: Etymology
323: A foreign Wanderwort , likely borrowed from a western substrate . The same Wanderwort may be reflected in Hebrew קוֹף ( qōf ) , Akkadian uqūpu , Egyptian gfj , Middle Persian [script needed] ( kpyk' /⁠kabīg⁠/ ) , Ancient Greek κῆπος ( kêpos , “ long-tailed monkey ” ) , and Proto-Germanic *apô ( “ ape, monkey ” ) .
337: ape , monkey 
461: hi:Monkeys
```


## [2026-09-06T21:57:36.021Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/vapor\" \\\n \"https://www.etymonline.com/word/cupid\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1up-\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%81%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/kapi\" \\\n \"https://en.wiktionary.org/wiki/sup\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 286 verification\"; done 2>&1 | tail -20"
}
```


### [2026-09-06T21:57:40.515Z] TOOL RESULT

```
### https://www.etymonline.com/word/vapor
/home/sfmqrb/git/rishe/data/verification/sources/web/0b637c2ac78c192c.txt
### https://www.etymonline.com/word/cupid
/home/sfmqrb/git/rishe/data/verification/sources/web/5ada6a9755940215.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1up-
/home/sfmqrb/git/rishe/data/verification/sources/web/267eb2619aed5a87.txt
### https://en.wiktionary.org/wiki/%D8%B3%D9%81%D8%AA%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/a0e876251d9a66c2.txt
### https://en.wiktionary.org/wiki/kapi
/home/sfmqrb/git/rishe/data/verification/sources/web/d81d410d6acea66c.txt
### https://en.wiktionary.org/wiki/sup
/home/sfmqrb/git/rishe/data/verification/sources/web/7338c45a36e0dfcc.txt
```


## [2026-09-06T21:57:44.621Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== vapor etymonline ==\"; grep -n -i \"vapor (n\" -A12 0b637c2ac78c192c.txt | head -30; echo; echo \"== cupid ==\"; grep -n -i \"cupid\" -A10 5ada6a9755940215.txt | head -25; echo; echo \"== PIE kup- ==\"; wc -c 267eb2619aed5a87.txt; grep -n -i \"shoulder\\|Avestan\\|supti\\|does not exist\\|Wiktionary does not\" 267eb2619aed5a87.txt|head"
}
```


### [2026-09-06T21:57:44.709Z] TOOL RESULT

```
== vapor etymonline ==
23: vapor (n.) 
24-
25- "exhalation of moisture; any visible diffused substance; the stuff of mists and clouds;" late 14c., vapour , "steam, moisture arising from heated matter; fumes from incense," from Anglo-French vapour , Old French vapor "moisture, vapor" (13c., Modern French vapeur ) and directly from Latin vaporem (nominative vapor ) "a warm exhalation, steam, heat," which is of unknown origin.
26-
27- Figurative of anything unsubstantial. The scientific sense of "gaseous form of a substance" is from mid-17c. Also see vapors .
28- also from late 14c. 
29-
30- Entries linking to vapor 
31-
32- vapors 
33-
34: "fit of fainting, hysteria, etc.," 1660s, as a disease of nervous disability supposedly caused by a vapor (n.) or combination of them, in that word's sense in old physiology and medicine, "gas or exhalation generated in the stomach or other organs and affecting the brain" (late 14c.). Hence, by early 18c. "depression of spirits." Century Dictionary (1895) describes it as "a term much affected in the eighteenth century, but now rarely used." Also, in early 17c., "a hectoring, bullying style of language."
35-
36- dumps (n.) 
37-
38- "low spirits; dull, gloomy state of mind," 1520s, plural of dumpe "a fit of musing," of uncertain origin, possibly from Dutch domp "haze, mist," from Middle Dutch damp "vapor" (see damp (n.)). Compare vapors under vapor .
39-
40- The application of this term to an affection of the mind is a part of the medical theory which attributed all disorders of the frame to a humour falling on the part affected, and regarded mental disorders especially as produced by a vapour rising from the stomach into the brain. [Hensleigh Wedgwood, "A Dictionary of English Etymology," 1859]
41-
42- evaporation 
43- vaporetto 
44- vaporize 
45- vaporous 
46- vapour 

== cupid ==
1:URL: https://www.etymonline.com/word/cupid
2-FETCHED: 2026-09-06T21:57:38Z
3-STATUS: 200
4:TITLE: Cupid - Etymology, Origin & Meaning
5-
6:Cupid - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
--
21: Origin and history of Cupid 
22-
23: Cupid 
24-
25: Roman god of passionate love, late 14c., from Latin Cupido , personification of cupido "desire, love, passion," from cupere "to desire" (see cupidity ). Identified with Greek Eros . Cupid's bow as a shape, especially of lips, is from 1858.
26- also from late 14c. 
27-
28: Entries linking to Cupid 

== PIE kup- ==
173 267eb2619aed5a87.txt
```


## [2026-09-06T21:57:51.579Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== wikt vapor Latin ==\"; grep -n -B3 -A8 \"Proto-Italic \\*kwapos\\|kʷap\\|uapos\\|vapōs\" d5463b66e4ae8987.txt | head -40; echo; echo \"== wikt cupio ==\"; grep -n -B2 -A10 \"Proto-Indo-European\" 9334e8741e99f0d2.txt | head -40"
}
```


### [2026-09-06T21:57:51.645Z] TOOL RESULT

```
== wikt vapor Latin ==

== wikt cupio ==
165- [ edit ] 
166-
167: From Proto-Italic *kupjō . According to the LIV, from Inherited from Proto-Indo-European *kup-yé-ti , from *kwep- ( “ to smoke, boil, move violently ” ) . If this theory is accepted, the term has an exact parallel in Sanskrit कुप्यति ( kupyati , “ to become agitated, bubble up ” ) . [ 1 ] De Vaan, however, explains the word as a derivative of an athematic i-present *kup-i- of the same root. [ 2 ] Schrijver, who also adopts the i-present explanation, suggests that the full-grade of the suffix of this i-present (e.g. a form of the shape *kup-ey- ) could explain the forms with the long vowel ī , such as cupīvī . Schrijver does, however, also mention a possible alternative explanation—that the perfect form was created analogically after fourth conjugation terms such as audīvī . [ 3 ] Weiss alternatively suggests that perfect forms in -īvī spread across verbs with similar semantics, all pertaining to the notion of "seeking." For instance, compare arcessō ( “ to summon, invite ” ) , arcessīvī ; petō ( “ to ask, beg ” ) , petīvī ; and quaerō ( “ to search ” ) , quaesīvī . [ 4 ] Cognate with Lithuanian kūpėti ( “ to boil over ” ) and Old Church Slavonic кꙑпѣти ( kypěti , “ to boil ” ) .
168-
169- Pronunciation
170- [ edit ] 
171-
172- ( Classical Latin ) IPA ( key ) : [ˈkʊ.pi.oː] 
173-
174- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈkuː.pi.o] 
175-
176- Verb
177- [ edit ] 
--
782- Retrieved from " https://en.wiktionary.org/w/index.php?title=cupio&oldid=91189872 "
783-
784: Categories : Latin terms derived from the Proto-Indo-European root *kwep- 
785- Latin terms derived from Proto-Italic 
786- Latin terms inherited from Proto-Italic 
787: Latin terms derived from Proto-Indo-European 
788: Latin terms inherited from Proto-Indo-European 
789- Latin 3-syllable words 
790- Latin terms with IPA pronunciation 
791- Latin lemmas 
792- Latin verbs 
793- Latin terms with quotations 
794- Latin terms with usage examples 
795- Latin third conjugation verbs 
796- Latin third conjugation verbs with perfect in -īv- 
797- Latin third conjugation verbs with perfect in -i- 
798- Latin words in Meissner and Auden's phrasebook
```


## [2026-09-06T21:57:57.560Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Latin$/,0' d5463b66e4ae8987.txt | head -40"
}
```


## [2026-09-06T21:57:58.393Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vapor\" LEW_1910.txt | head -8; echo ---; grep -n \"vapor\" LAT.txt | head -8"
}
```


### [2026-09-06T21:57:59.255Z] TOOL RESULT

```
 Latin
 [ edit ] 

 Etymology
 [ edit ] 

 From Proto-Italic *kwapōs , of uncertain ultimate origin, but possibly related to Ancient Greek καπνός ( kapnós , “ smoke ” ) and Proto-Indo-European *kʷep- ( “ to smoke, boil, move violently ” ) , [ 1 ] via an older form *quapor that eventually lost its velar. [ 2 ] 

 Pronunciation
 [ edit ] 

 ( Classical Latin ) IPA ( key ) : [ˈwa.pɔr] 

 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈvaː.por] 

 Noun
 [ edit ] 

 vapor   m ( genitive vapōris ) ; third declension 

 steam , exhalation , vapour ; smoke 

 warm exhalation, warmth , heat 

 ardour of love , warmth

 Declension
 [ edit ] 

 Third-declension noun.

 singular

 plural

 nominative 

 vapor 

 vapōrēs
```


### [2026-09-06T21:57:59.304Z] TOOL RESULT

```
---
```


## [2026-09-06T21:58:03.787Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== Arabic كبريت ===\"; grep -n -B4 -A14 \"Etymology\" 33ccbafff13d2f83.txt | sed -n '1,80p'"
}
```


### [2026-09-06T21:58:03.843Z] TOOL RESULT

```
=== Arabic كبريت ===
58-
59- Toggle Arabic subsection 
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
74- Derived terms 
75-
76- 1.3.3 
--
84-
85- Toggle Egyptian Arabic subsection 
86-
87- 2.1 
88: Etymology 
89-
90- 2.2 
91- Noun 
92-
93- 2.3 
94- References 
95-
96- 3 
97- Hijazi Arabic 
98-
99- Toggle Hijazi Arabic subsection 
100-
101- 3.1 
102: Etymology 
103-
104- 3.2 
105- Pronunciation 
106-
107- 3.3 
108- Noun 
109-
110- 4 
111- South Levantine Arabic 
112-
113- Toggle South Levantine Arabic subsection 
114-
115- 4.1 
116: Etymology 
117-
118- 4.2 
119- Pronunciation 
120-
121- 4.3 
122- Noun 
123-
124- Toggle the table of contents 
125-
126- كبريت 
127-
128- 13 languages 
129-
130- العربية 
--
225- Arabic Wikipedia has an article on: كبريت 
226-
227- Wikipedia ar 
228-
229: Etymology
230- [ edit ] 
231-
232- Borrowed from Aramaic כִּבְּרִיתָא ( kiḇrīṯā ) / ܟܶܒܪܺܝܬܳܐ ( kĕḇrīṯā , “ sulfur ” ) , from Akkadian 𒆠𒀀𒀭𒀀𒇉 ( kibrītu , “ sulfur; firebrand ” ) .
233-
234- Pronunciation
235- [ edit ] 
236-
```


## [2026-09-06T21:58:11.069Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Persian$/,0' 79c7b20bba013b98.txt | head -40"
}
```


### [2026-09-06T21:58:12.728Z] TOOL RESULT

```
 Persian
 [ edit ] 

 کبریت 

 Etymology
 [ edit ] 

 Borrowed from Arabic كِبْرِيت ( kibrīt , “ sulfur, match ” ) , from Aramaic כִּבְּרִיתָא ( kiḇrīṯā ) / ܟܶܒܪܺܝܬܳܐ ( kĕḇrīṯā , “ sulfur ” ) , from Akkadian 𒆠𒀀𒀭𒀀𒇉 ( kibrītu , “ sulfur; firebrand ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /kʰib.ˈriːt/ 

 ( Dari, formal ) IPA ( key ) : [kʰɪb.ɾiːt̪] 

 ( Dari, formal ) IPA ( key ) : [kʰɪb.ɾiːt̪] 
 ( Kabuli ) IPA ( key ) : [kʰɪb.ɾiːt̪] 

 ( Hazaragi ) IPA ( key ) : [kʰib.ɾit̪] 

 ( Iran, formal ) IPA ( key ) : [kʰʲeb.ɹiːt̪ʰ] 

 ( Tajik, formal ) IPA ( key ) : [kʰib.ɾit̪] 

 Rhymes: -iːt 

 Readings

 Classical reading ? 

 kibrīt

 Dari reading ? 

 kibrīt

 Iranian reading ?
```


## [2026-09-06T21:58:18.216Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD suft ==\"; grep -n \"suft\\|shoulder\" PHD.txt | head -10; echo; echo \"== NYB suft ==\"; grep -n \"suft\" NYB_vol2_glossary.txt | head -10; echo; echo \"== MON سفت ==\"; grep -n \"^سفت\\|سفت:\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-06T21:58:18.308Z] TOOL RESULT

```
== PHD suft ==
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
364:frég [plyk! | M pryyg] shoulder(-blade).
572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
655:wistardan, wistar- [wstl-tn! | N gustardan] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bile. wišād [SLYTWNt', Р! | M wid, N gušād] open, wide, loose. wišādan, *wišāy- [SLYTWN-tn! < A У šrh; wPtn! | M шурап, (wys?h-), N gušādan, gušāy-) open, loose, free. wišād-dar [.SL Y TWNt! BBA] hospitable. wišād-dwārišnīh [zP??! dzb?lšnyh) going about ‘open’, i.e. without kustīg, or šabīg. | wišān- [w®n- | = P] shake down. *wišāy-, v. wišādan. wiškar [zo£hl | N bisgar(d)] hunting-ground, wilderness. wiškīdan, wiškin(n)- [wfkytn!, wškn-] divide, separate. ~išn: separation. wiskofag [wskwpk' | N biškēfa] blossom. wiškuftan, wiSk6f- [vvškup-tn! | J guškuftn, gwškwß-] blossom; hatch. wišūb-, —išn(-īģ), v. wišuftan. wišoūmand [w%wmnd] poisonous, venomous. wišūdag [wiwtk' | (M ghwdg)] abortion, daevic creature. wišūdan [wswtn'] bear daevic offspring. wišuftan, wišūb- (zfwp-tn! | M wiwb-, N *gusuftan] disturb, destroy. ~isn: destruction. ~1&п16 : destructible. *wixSay- [whsd-} forgive, forbear. ~iSn(ih): forbearance. ~išnīg : forbearing. lwiyaban [20(у) р?п! | Р шуп, N bīābān] desert. *wiyābān [wyd’p’n'] astray, wandering; deluded. ~ih: delusion, deception. wiyaban|garih [wyd"Pnklyh] deception. ~ig [-vk'] wandering, itinerant. wiyāftan, *wiyüb- [wd ptn! | M wy’b-] open (the mouth). wiyan [wyd?n! | M wy’n, N giyān] tent. wiyiz- [wydwe-] loosen, undo. *wiyufs- [wdwps-] make merry. ~išn: merry-making. ~iìšnīg : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-ytn'] tremble, quake. -išn: quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption.
1047:bore suftan.
3123:pierce suftan.
3641:shoulder dēš, suft; ~-blade frég, šānag.
5499:suft suftan sanj-, sūz- sozag sózan sozisnig sozián sug südomand sūdabgār sūd sūdan sūdagīh sūdag sūdmand panjāhx geg

== NYB suft ==
690:*asiftan ['syptn'] *āsēp-, to light, to set on fire, to set fire to: ātaxš apar ~ 4816; the house pat äsepisn äsift estet is all ablaze 4429-22, _ The sense is clear, and the reading fairly certain; I have no evident etymology to propose. Cf, how- ever, NP äsuftah 'fire-brand' (< *äsiftah with -2- > -u- because of the labial ?).
757:āšuft-kārēh [’swptk’lyh] subversion, up- heaval 1081. — From äsuftan äsöp-, v. äsöp and cf visuftan; MPrth ’syft (A-H III). Ghilain 95; Bailey, BSOS VI, 1930, 73.
7015:äsuftah: äsiftan

== MON سفت ==
MON_part2.txt:12206:سفت. ضح.- در عربی بدین معنی نیأمده. 
MON_part2.txt:28215:سفت نشود. کوکو (به سبب مخلوط شدن با 
MON_part2.txt:38907:سفتی قادل تو جه وا کشت ونان ورم 
MON_part2.txt:39659:سفته. (کد.) تصنیفی بکر؛ و _ 
MON_part2.txt:66781:سفت شلد ۵ بر با سل ۵. 
MON_part2.txt:69897:سفت و سخت و خشک می‌باشد. 
MON_part2.txt:70595:سفتولی شکل و مجوف که در اعمال 
MON_part1.txt:40463:سفتادن» سقوط کردن فرو افتادن. (مص م.) 
MON_part1.txt:41949:سفت کردن. سخت و درشت ساختن. سجن 
MON_part1.txt:78023:سفت! 0۱ (ص.) ستر» غلبظ. محکم)
```


## [2026-09-06T21:58:19.804Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY سفت ==\"; grep -n \"سُفت\\|سفت (\" incoming/ARY/ARY_pages.txt | head; echo \"== IEC kup shoulder ==\"; grep -n \"cupti\\|kup-.*Schulter\\|supti\" IEC.txt | head"
}
```


### [2026-09-06T21:58:19.867Z] TOOL RESULT

```
== ARY سفت ==
== IEC kup shoulder ==
```


## [2026-09-06T21:58:28.894Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '78015,78035p' MON_part1.txt; echo \"=== part2 12200 ===\"; sed -n '12200,12212p' MON_part2.txt"
}
```


### [2026-09-06T21:58:28.954Z] TOOL RESULT

```
سفار تخانه 
سفال سازند؛ سفالی» کوزه سفالی. 

تفا هت : اقطقاهه [ع. سفاههة ] (مسص‌ل.) 
بیخردی کردن» بیعقلی نمودن. (اسص.) 
بیخردی» کم عقلی. 

سفت! 0۱ (ص.) ستر» غلبظ. محکم) 
استوار» مضصوط. سفت و سخت: سار 


سفت؛ (50]1)56]0 (.) دوش کتف. 
سفت؛ 00: [- سفتن ] (مص‌خم.) سوراح 
کردن. [- سفته] (اسف.) سوراخ شده. (.) 
سوراح کوچک مخصوصاً سوراخ سوزن. 
سفت زل: 50022097 [- سفت‌زننده] 
(ص‌فا.) (عم.) کسی که در مباشرت قوی 
بود» آنکه به نیرو جماع کند. 
سفت‌کاری: [-۰.12(حامض.) (بنا.) 
محکم کاری اساس بنا به وسیلاً آجر و 
=== part2 12200 ===

فشرشت: 12:32 (.) ششمین صورت از 
صور هشتگانهٌ حروف جمل شامل: ق ر ش 
اس ۰ 

ثرص: ۰:۰:(ص.) (عم.) مسحکم؛ استوار. 
سفت. ضح.- در عربی بدین معنی نیأمده. 
فرص: مر (ع.] (.) گرده. جرم. فرص 
آفتاب (خورشید): گرد خورشید. قرص 


زر: (کد.) آفتاب. قرص زر مغربی: (کد.) 
آفتاب. قرص سیمین: ( کذ.) آفتاب و ماه.
```


## [2026-09-06T21:58:30.058Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kupos\\|kup-\\|kupti\" IEC.txt | head -12; echo \"=== IEC kwep ===\"; grep -n \"kuepos\\|kuapos\\|kwapos\\|kuepo\" IEC.txt | head -8"
}
```


### [2026-09-06T21:58:30.114Z] TOOL RESULT

```
8414:küpió (2) ‘surge, swell, stir, seethe’. WP I, 379 Skt. kupye, mp. ‘seethe, stir; desire’ beside (e- gde) Copàmi, tr. ‘stir; Av. kup-, id.; Lat. cupio, īre & Gre ‘desire’; Br. kia (ambig; suffer); EME huff, v. ‘swagger’; Norw. hovne, pp: hoven ‘swell’ beside (variant) hovere ‘exult’; OCS kypljo, kypëti ‘well up, rise, swell, abound’; Cz. kypět, inf. ʻeffervesce’; Latv. kūpu, inf. kupt & kūpēt, kūpst ‘ferment, smoulder, work — as yeast’; Li. cf. kūpsoti, inf. ‘puff oneself up’. Cf. (short grade) Pol. kiep, inst. sg. kpem "Tool
=== IEC kwep ===
8488:kuapos, à (kuuap-) ‘exhalation, vapour’. Cf. kuëp-. WP I, 379 Gk. kápos, id.; kapúo, v. ‘exhale’; Alb. (?) vapë ‘sultriness’; Umb. cf. vapu-tu ‘with in- cense’; Lat. cf. vapor, vapidus; Li. kvüpas
```


## [2026-09-06T21:58:44.437Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFA kibrit ==\"; grep -n -i \"kibrit\\|Schwefel\" AFA.txt | head -10; echo; echo \"== FVQ kibrit ==\"; grep -n -i \"kibrit\\|sulphur\\|brimstone\" FVQ.txt | head -10; echo; echo \"== LKT kibrit ==\"; grep -n -i \"kibrit\\|Schwefel\" LKT.txt | head -10; echo; echo \"== KLN cupid ==\"; sed -n '61686,61710p' KLN_1971.txt; echo; echo \"== IEC shoulder sup ==\"; grep -n \"supti\\|kupti\\|'shoulder'\" IEC.txt | head -10"
}
```


### [2026-09-06T21:58:44.556Z] TOOL RESULT

```
== AFA kibrit ==
5521:vsAj^ir »der Schwefel'* bt zunächst ans lA^j-As entlehnt

== FVQ kibrit ==

== LKT kibrit ==
2329:'Steuer  oder  Taxe,  die  an  den  Fiskus  zu zahlen  ist';  hieraus  mlat.  cahalla  'Steuer', prov.  sp.  gabela,  pg.  gabella,  frz.  gabelle 'Warensteuer',  it.  gabella  'dass.',  von Neapel  südwärts  und  siz.  'Miet-  und Pachtvertrag'  [z.  B.  der  Verlrag,  durch den  die  Schwefelminen  Siziliens  an  einen Unternehmer  gabelloto  verpachtet  wer- den: gewöhnlich  gegen  20''/o  vom  Werte des  gewonnenen  Schwefels,  vgl.  Globus LXVII,  154],  rum.  havalea  'Abgabe, Arbeitsdienst'  [wohl  durch  Kontamination mit  ar.  Jiawäla  'Auftrag,  Bürgschalt, Wechsel',  s.  auch  Löbel  EITAP  52] ;  russ. kabala  'Schuldbrief,  Verschrei bung,  be- sonders zur  Leibeigenschaft',  klruss.  Ä:«- bala  'Verschreibung  zum  Leibeignen', zakabalyty  'zu  seinem  Untertanen  ma- chen'. Mitar.  Art.  ergibt  sich  sp.  alcabala 'Verkaufsgebühr',  pg.alcai^ala  'Eingangs- steuer'. Aus  dem  It.  wurde  serb.  poln. gabela'ZoU,  Steuer'.  —  [Ableitung  auslat. gabulum  <^  ags.  gafol  vom  Vb.  gifan, wie  Diez  Wb  der  rom.  Spr.  150  vorschlug, ist  abzulehnen,  da  lautlich  fast  unmög- lich.] [DE  GREGORIO  in  StGUtH.  Mikl SlEtWb  107.  Bern  SlEtWb  464.  DE  74 u.  75.  Eguilaz  121.  RomForsch  IV,  589. XXII,  629.    ML  6893.
2748:1171.  Ar.  kibrit:
2749:'Schwefel'  [Fremdwort  aus  dem  aram. kehribä  <^  ass.  kuprltu  'Schwefel',  dieses möglicherweise  aus  kupru,  s.  hier  Nr.  727, vgl.  ZAkkF W  60] ;  hieraus  mit  ar.  Art. sp.  alcrebite  'dass.';  in  der  Bedeutung 'Schwefel-,  Streichhölzchen'  tk.  kibrit; hieraus  rum.  chibrit  'dass.',  chibritelnifa. —  DE  95.
2880:[Über  aram.  kuhlä  vielleicht  aus  ass. guhlu  ZAkkFW"  61]  'Spießglanzpulver (Schwefelblei)  zum  Färben  der  Augen- brauen, Wimpern  und  Lider'  [über  den Gebrauch  und  die  Zusammensetzung  der orientalischen  Augenschminke  vgl.HlLLE in  ZDMG  V,  236/242];  noch  im  16. Jahrhundert  ist  das  hieraus  entstandene Wort  Alcohol  in  der  Alchemie  der  ge- läufige Ausdruck  für  'trockenes,  feines Pulver',  erst  später  wurde  es  zur  Be- zeichnung des  Weingeistes  benutzt.  Die einzelnen  Formen  sind:  sp.  pg.  alquifol, alcofol,  alcofor,  alcohol,  kat.  alcofoll, frz.  alquifoux,  coheul,  alcohol,  it.  alcool, rum.  alcool;  ndl.  alkohol,  engl,  alcohol, dtsch.  Alkohol;  russ.  alkogoV.  —  [Pers. und  tk.  heißt  die  Augenschminke  übrigens sürme,  subst.  Inf.  des  tk.  Vbs.  siirmek 'glätten'  vom  Slamme  seb,  sit<>,  süp  'glatt,
3180:1374.  Arain.  makkasitä: 'Schwefelkies' [vielleicht  wegen  der Spren- kelung  nach  syr.  kessä  'Spreu'  so  ge- nannt; im  übrigen  ist  das  Wort  noch nicht  erklärt],  hieraus  ar.  markasitä Bezeichimng  der  'Kiese'  mit  Ausnahme derer  von  Antimon  und  Wismuth  [vgl. kulil,  hier  Nr.  1227,  und  itmld,  hier Nr.  918]  und  ferner  sp.  kat.  marcasita, marquesita,  pg.  marcasita,  marquezita [Constancio  Dice  677  c],  frz.  marcassite, it.  marcassita;  engl,  marcasite,  dtsch. Markasit  'rhombische  Modifikation  des Eisenkieses'.  (Devic  DEt  157.  Eguilaz 444.  A.  Sadebeck,  Über  den  Namen , Markasit".    Im  Neuen  Jahrbuch  für
3478:'Stinkend,  faulend';  hieraus  siz.  »HmiiM« 'stinkendes  Wasser,  das  aus  den  Schwefel- quellen herausflie.ßl'.    [GrSVociSic  241.
3851:'Rotes  Schwefelarsenik'  [eigentlich  'Höh- lenpulver', aus  ra%"'Pulver',  ^är'Höhle', weil  man  das  Arsenik  aus  Minen  ge- wann]; hieraus  s^.rejalgar,  pg.resalgar, rosalgar,  it.  risigallo,  risogello,  (alt)  Pisa risalgado;  dtsch.  Realgar  'Rauschgelb', engl,  realgar  'red  orpiment'  [<;^  frz.  or- piment  <^  lat.  auri  piymentmn].  [DE 332/333.    Eguilaz  482.    ML  7011.

== KLN cupid ==
Derivative: cupell-ation , n. 

Cupid, n., the god of love in Roman mythology. 

— L. Cupido , personification of cupido, ‘desire, 
love’, fr. cupidus, ‘longing, desirous, eager’, fr. 
cupid, cupere , ‘to desire’, which is prob. cogn. 
with OI. kupyati, ‘bubbles up, becomes agitated’, 
OSlav. kypljQ, kypeti, ‘to boil’, Lith. kUpu, kupeti, 
‘to boil over’, Lett, kupu, kupet, ‘to smoke, 
steam’, Lith. kvepiit, kvipti, ‘to breathe, exhale 
fragrance’, kupuoti , ‘to breathe with difficulty’, 
Gk. xocttvoc; (for *xFoc7uv6<;), ‘smoke, vapor’, 
Goth, af-hapjan, ‘to put out, extinguish’, af- 
hapnan, ‘to go out, be extinguished’. Cp. concu- 
piscence, covet. Cp. also acapnia. Cp. also vapor. 

cupidity, n. — F. cupidite , fr. L. cupiditdtem , acc. 
of cupiditas, desire, longing’, fr. cupidus. See 
Cupid and -ity. 

cupola, n., a small dome. — It., fr. Late L. cupula, 
‘a little tub’, dimin. of L. cupa . See cup and 
cp. cupel. 


== IEC shoulder sup ==
```


## [2026-09-06T21:58:57.486Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"supti\\|süpti\\|snpti\\|sapti\" BRT.txt | head -20; echo \"---\"; grep -n \"'Schulter'\\|„Schulter\" BRT.txt | head -20"
}
```


### [2026-09-06T21:58:57.590Z] TOOL RESULT

```
25203:.  .  asäi  'vS  yaisa  (Sp.  28  m.)  . .  *vS  vi- va^aYt.ij.gg; — yo..havaiibya  bSzulya tanuye  'vs  agsisii!(sd.)  Yt.  i_3.  107;  —  'vasai x^äiir3m(sd.)ca  ..  qzasca  dui3%r3mla  Y.  8. 8;  ~-  yasca  ml  aibm  nar>tn  ^>j(sd.)  avi ava.gsnptim  °vBhu  paiti  uzbärayat  V.  18. 10;  Vtj.  4(?); —  aca  n6  Jamyai  'vaiAhe ".  .  zur  Freiheit'  Yt.  10.  5.
26387:•  j.  suptiJIar^nga-  Adj.  'Gaugenosse,  aus dem  selben  Gau  gebürtig':  visaifivä  asii mihm  anian  hasa  'ga  (AD.)  %risd^w3 antarf  vanzäna  cähwarjsahwa  antan ht^gaiSia  pancasa^wA  antar»  Auyäyna "zwanzigfach  (bindend)  ist  M.  zwischen ein  Paar  Genossen  aus  dero  selben  Gau, . .  aus  der  selben  Gemeinde,  . .  aus  dem selben  Haus,  . .  aus  der  selben  Stube" YtiO.  116.
28907:•  j-  (1  g-t  P)  haxay- :  Ariy-,  Aai'-^^,  m. i)  'Freund,  Genosse':  ^m  °xa  (NS.)  '1/ (DS.)  *baraiti  Y.  6'2.  8;  —  aa£  aosOe  'xa •sa  (IS.)  V.  18.  a6;  F.  24;  —  yaS:a  . .  mri Aamü.äaina  Jason  brn%ra  va  'xaya  (NP.) vä  V.  4.  44;  Vyt,  10;  —  vlsaitiva  asti mi^r5  atiian  'ia  (AD.)  suptiiiannga  (sd) Yt.  JO.  116;  —  Sxstim  kqm.vaintfm  .. 'xaya    (AD.)    sraosaAe    Yt  //.  16;     16',
30467:•  j.  huyä)Tia-  Adj,  'das  Lager  teilend, Lager-,  Stubengenosse';  vlsaitivä  asti miirS  aniar»  ha!a  suptioarynga  (sd.)  .  , pama.sa%wa  autark  'na  (AD.)  \t  10.116.
---
```


## [2026-09-06T21:58:57.958Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A12 \"^vapor, n\" KLN_1971.txt | head -20"
}
```


### [2026-09-06T21:58:58.009Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:59:07.843Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"chulter\" BRT.txt | head -20"
}
```


### [2026-09-06T21:59:07.899Z] TOOL RESULT

```
6147:VgL  1«,  axilla,  ahd.  ahsala;  Hbm.  IF.  *  u8. —  PÜ.:  ai  Cin  Aw.-Bacbst),  mit  der  Eil.: eigSn  anäatk  su/l  u  vor  'd.  h.  (das)  mischen Schulter  und  Brost".
7086:•  j.  ä.gao§Ö.-masah-  Adj.  'des  Grösse zum  Ohr  geht,  so  gross  wie  man  es  beim Ohr,  dh.  über  der  Schulter  trägt':  alsma- nqmcil . .  'sSbii  qxmS.fianS.masSbÜ  sasts.- /rilnB.masibJ^  {xiAa^.  siati)  A..9.5.
12558:•  j.  daoä-  m.  'Oberarm,   Schulter":    "Ä
12561:dsi   ■Schulter'.  —   t)  Wo  pü.  auigefttllen   ist
26385:•  j.  suptay-  f.  'Schulter*:  haoyqm  (bz.  dasi- lum,  sd)  'tim  V.i'.46-47',p.  17*.
27510:•)  Das  »on  der  linken  Hüfte  über  die  rechte Schulter  lief  und  insbetondere  «um  Tragen  des Köchen  dienie:  TgL  auf  der  Inschrift  toq  Ba- Aiitän  die  Figur  dei  hinter  dem  KOnig  ctehen- den  renere.
```


## [2026-09-06T21:59:20.746Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (272,273,274,275):\n    t=d[i]\n    print('--- leaf',i,'---', repr(t[:120]))\n    print('   tail:', repr(t[-160:]))\nEOF"
}
```


### [2026-09-06T21:59:22.431Z] TOOL RESULT

```
--- leaf 272 --- '. 1.629.\nIt. strozza (whence strozzare ‘throttle’), fr. a Langobard form like MLG strozze (below, 5).\nFr. gorge, above, '
   tail: '? Walde-P. 1.178. Ernout-M. 1123.\nGrk. duos, NG also vapos (v from forms of the article); Lat. wmerus (> It. omero, Sp. hombro, Rum. umér), Umbr. ose ‘in umero�'
--- leaf 273 --- '��: : Ae ave Ae a amsans (acc. pl.);\n2. It. spalla, Fr. épaul ete ’ paule (Sp. espalda ee 4.19), fr, Lat. spatula ‘flat '
   tail: ' armus, 4.31.\nChSl. pleste, SCr. pleéa, Boh, plece, Pol. plecy (pl.), Russ. pleco, prob, fr.\n*plet-yo- : Lith. platus, Grk. TAarbs ‘broad, flat’, but could also'
--- leaf 274 --- ' be fr, *nlek- tyo- : Lett. place ‘shoulder blade’, plahy ‘become flat’, Grk. r\\aé ‘flat surface’, etc., in either case '
   tail: 'in. 1).\nlov, in part ‘upper arm’ 3, Grk. Bpaxe™ Tim. 75a; but also\nly generic (of : t ith subordina ie avr, aaxus, xelp ‘shoulder, upper\narm, elbow, forearm, ha'
--- leaf 275 --- 'nd’), an old comparative of Bpaxts ‘shor t?, to be un- derstood as first applied to the upper arm as ‘shorter’ than the '
   tail: 'boog Skt.  aratni- OHG  e()linbogo Av. aradna- MHG e(2)lenboge NHG ellenbogen\nCC-0. In Public Domain. Gurukul Kangri Collection, Haridwar\nDigitized by Arya Sama'
```


## [2026-09-06T21:59:36.182Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('data/verification/page-2*.json'))[-6:]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if not n.get('words'):\n                print(f, json.dumps(n,ensure_ascii=False)[:900]); print()\nEOF"
}
```


### [2026-09-06T21:59:38.061Z] TOOL RESULT

```
data/verification/page-279.json {"id": 2, "lang": null, "words": "", "verdict": "unverified", "derivation": "An empty box on the printed page: on the 200/600-dpi render of pdf page 279 (copied to data/verification/sources/refs/ocr/BOOK/279.png) a wide, completely blank rectangle is drawn to the right of the Avestan šaēiti/šōiθra box, with the arrow from it, but it carries no language label, no reference and no word. The extraction is faithful (lang null, refs null, words []). Nothing can be verified. What Nourai must have meant to put there is the Persian continuation of šōiθra-, i.e. MP šahr 'land, country; city' > NP شهر (MacKenzie: 'šahr [štr' | M šr, N ~] land, country; city'), which is the one well-known New Persian reflex of this root.", "derivation_fa": "این جعبه در صفحهٔ چاپی کاملاً خالی است: در تصویر صفحهٔ ۲۷۹ پی‌دی‌اف مستطیلی پهن و بی‌متن در کنار جعبهٔ اوستایی رسم شده است، بدون نام زبان، بدون مأخذ و بدون واژه

data/verification/page-280.json {"id": 4, "lang": "French", "words": "", "verdict": "confirmed", "derivation": "The box is a pass-through with no word printed: the intended form is French élixir, attested from the 13th c. in alchemical Latin/French texts and taken from Medieval Latin elixir, itself from Arabic al-iksīr, through the Latin translations of Arabic alchemy made in Spain in the 12th c. Devic p.108-109, the reference Nourai cites, is precisely the article 'Elixir' and gives the Spanish, Portuguese and Italian cognates alongside the French word.", "derivation_fa": "این خانه در کتاب خالی چاپ شده و تنها حلقهٔ میانجی است؛ واژهٔ مورد نظر فرانسوی élixir است که از لاتینی میانه elixir و آن از عربی الإکسیر گرفته شده، از راه ترجمهٔ متون کیمیای عربی در اسپانیای سدهٔ دوازدهم میلادی. ارجاع نورایی به دویک ص ۱۰۸ دقیقاً همین مدخل است.", "sources": ["https://www.etymonline.com/word/elixir"], "ref_check": [{"ref": "DEV:108", "

data/verification/page-282.json {"id": 3, "lang": "Hindustani", "words": "", "verdict": "confirmed", "derivation": "An empty pass-through box: the Persian compound šīr-o-šakar was carried into Hindustani (Hindi-Urdu) as sīrsakar / śīrśakar, the name of the puckered striped cloth, during the Mughal period, and it is from that Hindustani form, not directly from Persian, that the English word was taken by the East India trade. Klein (p. 1410-1411, s.v.) writes 'seersucker, n., a kind of cotton fabric. — Hind. sirsakar, fr. Pers. shir-o-shakar, lit. „milk and sugar“'; Etymonline dates the English borrowing to 1722 'from Hindi sirsakar, said to be an East Indian corruption of Persian shir o shakkar'. The Persian → Hindustani → English route drawn here is therefore exactly the standard one.", "derivation_fa": "این جعبه خالی است و تنها حلقهٔ واسط را نشان می‌دهد: ترکیب فارسی «شیروشکر» در دورهٔ گورکانیان به هندی–اردو راه یافت و

data/verification/page-283.json {"id": 8, "lang": "French", "words": "", "verdict": "plausible", "derivation": "Empty pass-through box for French calibre, first attested in the mid-16th c. (perhaps already late 15th c.) in the sense 'internal diameter of a gun barrel', the form from which English caliber and Persian کالیبر come. Klein has it from Italian calibro, which is the arrow Nourai draws; but Lokotsch (no. 1030) makes French calibre a direct or Spanish-mediated taking from Arabic qālib, and Barnhart holds that the Italian and Spanish forms are too late to be intermediaries, so that the word may have been shaped in French itself (from Medieval Latin qua libra). The node's existence is certain; only the Italian → French step is uncertain.", "derivation_fa": "خانهٔ واسطهٔ بی‌واژه برای فرانسویِ calibre که از میانهٔ سدهٔ شانزدهم میلادی (شاید از اواخر سدهٔ پانزدهم) به معنای «قطر درونی لولهٔ سلاح» گواهی شده و سرچشمهٔ c

data/verification/page-283.json {"id": 13, "lang": "Arabic", "words": "", "verdict": "plausible", "derivation": "An empty pass-through box standing for the Arabic form of the name. Arabic does have القوقاز al-Qawqāz (and the older جبل القبق Jabal al-Qabq) for the Caucasus, and it is ultimately the Graeco-Latin name; so a Latin/Greek → Arabic step is possible in principle. But nothing in the local library or in Wiktionary documents an Arabic transmission specifically to the Persian form قفقاز, and the medieval Arabic geographers' usual word is al-Qabq, not Qafqāz. The likelier immediate transmitter of the modern Persian form is Ottoman Turkish/Russian (see node 14). The box is therefore possible but undocumented.", "derivation_fa": "خانهٔ واسطهٔ بی‌واژه که جای صورت عربی نام را نگاه می‌دارد. در عربی «القوقاز» (و در متون کهن‌تر «جبل القبق») به‌کار رفته و در نهایت همان نام یونانی‑لاتینی است، پس گامِ لاتینی/یونانی ← عربی از
```


## [2026-09-06T21:59:41.579Z] TOOL CALL #63: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T21:59:41.615Z] TOOL RESULT

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


## [2026-09-06T21:59:50.021Z] TOOL CALL #64: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7ep-\" \\\n \"https://en.wiktionary.org/wiki/kabig\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 286 verification\"; done 2>&1 | tail; echo; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg286.png data/verification/sources/refs/ocr/BOOK/286.png && ls -la data/verification/sources/refs/ocr/BOOK/286.png"
}
```


### [2026-09-06T21:59:52.866Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7ep-
/home/sfmqrb/git/rishe/data/verification/sources/web/572910534271dd68.txt
### https://en.wiktionary.org/wiki/kabig
/home/sfmqrb/git/rishe/data/verification/sources/web/4ca5310d49ba35db.txt
### https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B4
/home/sfmqrb/git/rishe/data/verification/sources/web/00af144fca24970c.txt

-rw-rw-r-- 1 sfmqrb sfmqrb 69883 Sep  6 17:59 data/verification/sources/refs/ocr/BOOK/286.png
```


## [2026-09-06T21:59:55.381Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 572910534271dd68.txt && grep -n -i \"smoke\\|Derived terms\\|Latin\\|Sanskrit\" 572910534271dd68.txt | head -20"
}
```


### [2026-09-06T21:59:55.431Z] TOOL RESULT

```
171 572910534271dd68.txt
```


## [2026-09-06T22:00:48.311Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD shoulder ==\"; grep -o \"Shoulder[^.]\\{0,80\\}\" AHD_watkins1985.txt | head -5; grep -n \"SHOULDER \" AHD_watkins1985.txt | head -3; echo \"== KNT kupsins/kup ==\"; grep -n -i \"kupsin\\|mist\\|fog\" KNT.txt | head -5; echo \"== SYN monkey/ape ==\"; grep -n \"4.30\\|MONKEY\\|APE\\b\" SYN.txt | head -5; grep -o \"kapi[^ ]\\{0,20\\}\" SYN.txt | head -5"
}
```


### [2026-09-06T22:00:50.022Z] TOOL RESULT

```
== AHD shoulder ==
Shoulder
== KNT kupsins/kup ==
4941:azíaina- adj, with kdsaka-, ‘turquois’ (so Bleichsteiner, WZKM 37.103-4, and Konig, Burg- bau 63-4, but considered dubious by Hinz, ZDMG 95.235-6; hardly ‘gray amber’, with Hz. AMI 3.05—7, ApI 232; not ‘hematite’, with Scheil 21.29- 30): Av. arSaéna- ‘dark-colored’, borrowed in Gk. Порто “Atevos ‘Black Sea’ (‘in-hospitable’, by Gk. popular etymology, and euphemistically changed to Еф о), from neg. a- + z&atna-, cf. Av. xSaéta- ‘shining’ (§102, 5147.1). azšaina nsm. DSf 39.
== SYN monkey/ape ==
4922:2. Lat. piscis, Ir. tasc, NIr. zasg, Goth. fisk, etc., all the Gme. words, root connection? Walde-P. 2.11. Po- korny, KZ 54.307. Cuny, Mélanges Glotz, 268 f.
5008:3.76 MONKEY
5195:4.29 Turoar 4.30 SHovutprer
5547:Sp. espalda(s) fr. Lat. spatula ‘flat piece, shoulder blade, shoulder’ (as Fr. épaule, etc. 4.30), dim. of spatha ‘spattle, sword’ (fr. Grk. oman ‘flat blade’), whence Rum. spatd ‘shoulder blade’, pl. spate ‘back’. REW 8128, 8180.
5561:Pol. plecy ‘shoulder’ (4.30), used in phrases for ‘carry on the back’, etc.
kapi-
kapi-
kapila-
kapice,
kapija
```


## [2026-09-06T22:00:52.793Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('SYN.txt',encoding='utf-8',errors='replace').read()\ni=d.find('3.76 MONKEY')\nprint(d[i:i+2500])\nEOF"
}
```


### [2026-09-06T22:00:54.458Z] TOOL RESULT

```
3.76 MONKEY
Grk. —_xl8nxos Goth. Lith. bezdzioné NG E itie patpod ON apt Lett. pertik'is Lat.  simia Dan. abe ChSl. (pitikit) It. scimmia Sw. ape SCr. majmun, opica Fy. singe OE apa Boh. opice
Sp. mono ME ape Pol.  matpa Rum. maimu(d NE monkey (ape) Russ. obez’jana Ir. es atte Du. aap Skt. kapi- NIr. apa OHG affo Av. was
W. epa MHG aff
Br. marmouz NHG affe
Here is understood the generic name for the simians, NE: monkey in current popular usage, but formerly and still sometimes ape, though the latter now generally denotes the tailless species. Cf. NED s.v. ape.
1. Grk. wi@nxos, etym.? Walde-P. 2.186. This is the generic term, while kiros, xjBos (cf. below, 6) is specific. Cf. Aristot. HA 502° 6 pev xijBos ai@nxos éxwv obpav.
Byz. pipe : wipéopar ‘mimic’.
NG paupod, fr. Turk., Arab. maimin. Lokotsch 1365.
2. Lat. stmia (>It. scimmia, Fr. singe), deriv. of stmus, loanword fr. Grk. otés ‘snub-nosed’. First used as a nickname and prob. based on the name ZYuyuslas, Simia. Kretschmer, KZ 33, 563.
Olt., OFr. maimon, Rum. maimuté, also OIt. monna, Sp. mono, -a, fr. Arab. maimin. Lokotsch 1865. REW 5242.
3. NIr. apa, W. ab (arch.), fr. ME ape, OF apa (below, 4), W. epa late loan- word fr. NE ape.
Br. marmouz, fr. OF r. marmot or mar- mouset, both used for ‘monkey’ (also
‘small child’, etc.), history dub. Henry 196. REW 5587. Gamillscheg 593.
4. ON api, OF apa, OHG affo, etc., the general Gme. word, orig. unknown, perh. Celtic. Walde-P. 1.51 ff.
From Gme. come the Slavic forms, Boh. op, opice, SCr., ORuss. opica, etc. Stender-Petersen 361.
NE monkey, prob. fr. a MLG moneke (Moneke as name attested), dim. of the word that appears as Sp. mono, etc. (above, 2). NED s.v.
5. ChSl. (late) pitikd fr. Grk. riOnxos.
Boh. opice, etc. from Gme. (above, 4).
Russ. obez’jana (> Lith. bezdZioné), fr. Turk. ebuzine. Lokotsch 556.
Lett. pertik’is, fr. Esth. pertik (or con- versely?). Miithl.-Endz. 3.210.
SCr. majmun fr. Turk., Arab. mat- mun.
Pol. matpa fr. NHG maul-affe. Briickner 320.
6. Skt. kapi- : kapila- ‘brownish, red- dish’, fr. ‘smoke-colored, Grk. xamvés, etc.? Walde-P. 1.379. Prob. source of Egypt. gephi, Grk. xios, xfBos, etc. Schrader, Reallex. 1.16.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
ANIMALS
3.77 ELEPHANT
189
Goth. ..- Lith. dramblys
grk.  Prkeas ON ue ae elefants
" erégas 7 Dan. elefant is) eee ve elephantus, elephas Sw elefant Bes Bie Tt elefante OE elpend, ylp Co) slon rr Aéphant ME __
```


## [2026-09-06T22:01:17.247Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('SYN.txt',encoding='utf-8',errors='replace').read()\ni=d.find('Skt. cupti-')\nseg=d[i-3000:i+1500]\nimport re\nprint([m for m in re.findall(r'\\n\\s*(\\d{3})\\s*\\n', seg)])\nj=seg.find('4.30 SHOULDER')\nprint(seg[max(0,j-200):j+300])\nEOF"
}
```


### [2026-09-06T22:01:19.315Z] TOOL RESULT

```
['236']
nt’.
1, IE *om(e)so-s, root connection? Walde-P. 1.178. Ernout-M. 1123.
Grk. duos, NG also vapos (v from forms of the article); Lat. wmerus (> It. omero, Sp. hombro, Rum. umér), Umbr. ose ‘in umero���: : Ae ave Ae a amsans (acc. pl.);
2. It. spalla, Fr. épaul ete ’ paule (Sp. espalda ee 4.19), fr,
```


## [2026-09-06T22:09:02.709Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk286.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 286,\n \"book_page\": 256,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 3,\n   \"root\": \"Kup 1, Sup 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ḱup- 'shoulder' (Pokorny 627 ḱup-, with s-initial in Germanic; the satem forms show *ḱ > s)\",\n   \"note\": \"Pokorny 627 has exactly this root: 'Root/lemma: ḱup- … Meaning: shoulder … Note: (Germanic with anlaut. s-) … Material: Old Indic supti-, Avestan supti- \\\"shoulder\\\"; Alb. sup \\\"shoulder, back\\\" (without formant -t-); MLG schuft, EFris./Dutch schoft \\\"shoulder blade of a cow, a horse\\\" (*skuftu-). References: WP. I 467.' Nourai's double heading 'Kup 1, Sup 2' is his way of covering both the plain lemma and the s-initial variant Pokorny mentions, so root, language label (Indo-European) and gloss ('shoulder') are all correct. The one thing to keep in mind is that the s- of Indo-Iranian supti- is not Pokorny's Germanic s-mobile but the regular satem outcome of palatal *ḱ.\",\n   \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ هندواروپایی آغازین *ḱup- «شانه، کتف» است؛ پوکورنی در صفحهٔ ۶۲۷ همین سرواژه را با معنی «Schulter» آورده و مادهٔ آن را سنسکریت śupti-/cupti-، اوستایی supti-، آلبانیایی sup و آلمانی میانهٔ سفلی schuft می‌شمارد و به والده–پوکورنی جلد ۱ ص ۴۶۷ ارجاع می‌دهد. عنوان دوگانهٔ نورایی («Kup 1, Sup 2») ناظر بر همان نکتهٔ پوکورنی است که این ریشه در ژرمنی با s- آغازین ظاهر می‌شود؛ اما باید توجه داشت که s در صورت‌های هندوایرانی حاصل قانون کام‌شدگی (satem) و بازتاب *ḱ است، نه s متحرک ژرمنی. در مجموع ادعای نورایی دربارهٔ ریشه، نام زبان و معنی درست است.\",\n   \"sources\": [],\n   \"ref_check\": [\n    {\"ref\": \"POK:627\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (searched 'Page(s): 627'): 'Root / lemma: Ḱup- (*ḱehu-p-) | Meaning: shoulder | Note: (Germanic with anlaut. s-) … Material: Old Indic supti-, Avestan supti- \\\"shoulder\\\"; alb. sup \\\"shoulder, back\\\" (without formant -t-); Middle Low German schuft … Dutch schoft \\\"shoulder blade of a cow, a horse\\\" (*skuftu-). References: WP. I 467. Page(s): 627'. Exactly the root, the language label and the gloss Nourai prints.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 467 (WLD_Bd1_1930_dli_70244_djvu.txt line 29417 / WLD_Bd1_pages.txt leaf 475)\", \"stance\": \"supports\",\n     \"note\": \"'kup- \\\"Schulter\\\" (germ. mit anl. s-). Ai. çupti-, av. supti- \\\"Schulter\\\"; alb. sup … \\\"Schulter, Rücken\\\" (ohne formantisches -t-); mnd. schuft m., ostfries., ndl. schoft \\\"Vorderschulterblatt einer Kuh, eines Pferdes\\\" (*skuftu-)' — Pokorny's source, same content.\"},\n    {\"src\": \"SYN\", \"where\": \"§4.30 SHOULDER, p. 236 (SYN.txt leaf 274)\", \"stance\": \"supports\",\n     \"note\": \"Buck's table for 4.30 SHOULDER lists 'Skt. skandha-, aṃsa- (çupti-) … Av. supti- (daoš-)', and the discussion adds 'Skt. çupti- (only once, RV 1.51.5), Av. supti- (NPers. suft) : Alb. supé \\\"shoulder\\\", MLG schuft, Du. schoft … Walde-P. 1.467.' The printed page number 236 stands in the same column, confirming Nourai's SYN:236.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, k- section\", \"stance\": \"silent\",\n     \"note\": \"Watkins' 1985 appendix has no root for 'shoulder' of this shape (grep 'Shoulder' returns only the English gloss line); the root is one of the ones Watkins dropped as too thinly attested. No contradiction, simply absent.\"},\n    {\"src\": \"IEC\", \"where\": \"IEC.txt\", \"stance\": \"silent\",\n     \"note\": \"grep 'supti', 'cupti', 'kupti' in Mann's Indo-European Comparative Dictionary returns nothing; Mann has no entry for this root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"supti\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan supti- (stem suptay-) f. 'shoulder' is a real, attested Younger Avestan word: Bartholomae's Altiranisches Wörterbuch has 'j. suptay- f. \\\"Schulter\\\": haoyąm (bzw. dašinəm) °tīm V. 8.46-47', i.e. 'the left (resp. right) shoulder' in Vendidad 8.46-47. It continues PIE *ḱup-ti- with the regular satem development *ḱ > Proto-Iranian s (as in Skt. śupti-/çupti- with palatal ś from the same *ḱ), plus the abstract/body-part suffix *-ti-. Sanskrit śupti- occurs only once (RV 1.51.5), so the Avestan word is in fact the better-attested of the two Indo-Iranian forms. Nourai's arrow root → Avestan is therefore correct, only note that the Avestan form is the *attestation* of the Indo-Iranian outcome, not a step of derivation additional to Sanskrit.\",\n     \"derivation_fa\": \"واژهٔ اوستایی supti- (ستاک suptay-، مؤنث) به معنی «شانه، کتف» واژه‌ای گواهی‌شده در اوستای نو است؛ بارتولومه در «فرهنگ ایرانی باستان» آن را چنین آورده: «suptay- f. \\\"Schulter\\\"» با شاهد وندیداد ۸:۴۶–۴۷ («شانهٔ چپ/راست»). این صورت بازماندهٔ هندواروپایی *ḱup-ti- است: ḱ کامی هندواروپایی در شاخهٔ ساتم به s بدل شده (در سنسکریت به ś: śupti-) و پسوند *-ti- بر ستاک افزوده شده است. پس پیکان نورایی از ریشه به اوستایی درست است؛ تنها باید دانست که صورت اوستایی گواهِ برایند هندوایرانی است، نه حلقه‌ای جدا پس از سنسکریت.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:627\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt, lemma ḱup- p.627: 'Material: Old Indic supti-, Avestan supti- \\\"shoulder\\\"'. The Avestan word is named in the root article itself.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"s.v. suptay- (BRT.txt line 26385, AiW col. ~1585)\", \"stance\": \"supports\",\n       \"note\": \"'• j. suptay- f. \\\"Schulter\\\": haoyąm (bz. dašinəm, sd) °tīm V. 8.46-47, p. 17*.' — Younger Avestan, feminine, 'shoulder', attested Vendidad 8.46-47. (Bartholomae's separate lemma supti.δarəna- 'Gaugenosse' at line 26387 is a different word and must not be confused with it.)\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 467\", \"stance\": \"supports\",\n       \"note\": \"'Ai. çupti-, av. supti- \\\"Schulter\\\"; alb. sup … (Bezzenberger BB. 1, 341, Bartholomae Stud. II 15)'.\"},\n      {\"src\": \"SYN\", \"where\": \"§4.30 SHOULDER, p. 236\", \"stance\": \"supports\",\n       \"note\": \"'Skt. çupti- (only once, RV 1.51.5), Av. supti- (NPers. suft)'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"soft «سُفت»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian سُفت suft/soft 'shoulder' continues Old Iranian *supti- through Middle Persian suft: MacKenzie's Concise Pahlavi Dictionary p.79 gives 'suft [swpt' | N ~] shoulder', the Book-Pahlavi spelling <swpt'> showing the -pt- cluster still intact, and the '| N ~' meaning the New Persian form is identical. The only changes on the way are the loss of the Old Iranian stem-final -i and the ordinary NP raising/lowering of the short vowel (suft ~ soft); the cluster -ft- is preserved exactly as in MP haft > NP haft. Horn's Grundriss no. 789 states the chain in one line: 'suft, sift \\\"Schulter\\\". aw. supti \\\"Schulter\\\"; phlv. suft; ai. çupti- \\\"Schulter\\\"'. Mo'in's footnote to Borhan-e Qateʿ s.v. سفت gives the same series (Avestan supti- 'شانه', Pahlavi suft, Albanian sup) and adds the modern Pamir cognates (Shughni, Sarikoli, Yidgha). Nourai's arrow Avestan → Persian is thus right in substance, with the usual shorthand that the Persian in fact descends from the Old Iranian form of which Avestan supti- is the attestation, via the Middle Persian stage. The homophone سُفتن 'to pierce' (MP suftan, sumb-) is a different root and is kept apart by Borhan itself, which lists 'دوش' and 'ماضی سفتن … سوراخ کردن' as separate senses.\",\n     \"derivation_fa\": \"«سُفت» فارسی نو به معنی «دوش، کتف» دنبالهٔ ایرانی باستان *supti- است و از راه فارسی میانه (پهلوی) suft به فارسی رسیده؛ مکنزی در «فرهنگ کوچک پهلوی» ص ۷۹ می‌آورد: «suft [swpt'] shoulder» و با نشانهٔ «N ~» می‌گوید صورت فارسی نو همان است. تنها دگرگونی‌ها افتادن -i پایانِ ستاک ایرانی باستان و نوسان واکهٔ کوتاه (suft ~ soft) است؛ خوشهٔ -ft- دست‌نخورده مانده است. هرن در «مبانی ریشه‌شناسی فارسی نو» شمارهٔ ۷۸۹ (ص ۱۶۳) همین زنجیره را می‌دهد: «suft, sift \\\"شانه\\\"؛ اوستایی supti؛ پهلوی suft؛ سنسکریت śupti-». حاشیهٔ معین بر برهان قاطع ذیل «سفت» نیز همین صورت‌ها را با هم‌ریشه‌های پامیری (شغنی، سریکلی، یدغه) می‌آورد. پس ادعای نورایی درست است، با این یادآوری که واسطهٔ راستین فارسی میانه است و اوستایی تنها گواه صورت ایرانی باستان است. «سُفتن» به معنی «سوراخ کردن» واژه‌ای جداست و نباید با آن آمیخته شود.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SYN:236\", \"status\": \"supports\",\n       \"note\": \"Buck §4.30 SHOULDER p.236: 'Skt. çupti- (only once, RV 1.51.5), Av. supti- (NPers. suft) : Alb. supé …' — the New Persian word is named in the same breath as the Avestan one.\"},\n      {\"ref\": \"POK:627\", \"status\": \"partial\",\n       \"note\": \"POK p.627 lists the Indo-Iranian and Germanic material but names no New Persian form; it supports the root and the Avestan word, not the Persian step specifically.\"},\n      {\"ref\": \"BQT:1143\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ (BQT_v2_pages.txt leaf 607, printed ≈1143): 'سفت = بضم اول و سکون ثانی و فوقانی، دوش را گویند و بعربی کتف خوانند' ('suft: the shoulder, in Arabic katif'), with Moʿin's footnote 4 giving 'اوستا supti- (شانه)، پهلوی suft' plus Shughni/Sarikoli/Yidgha and Albanian sup. Note: the OCR page numbering of this scan runs a few leaves off, but the entry is the one Nourai cites.\"},\n      {\"ref\": \"HRN:163\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss der neupersischen Etymologie, no. 789 on printed p.163 (HRN.txt leaf 184 = 163+21): '789. suft, sift \\\"Schulter\\\". aw. supti \\\"Schulter\\\"; phlv. suft; ai. çupti- \\\"Schulter\\\"'. Exactly Nourai's chain.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 79 s.v. suft\", \"stance\": \"supports\",\n       \"note\": \"MacKenzie: 'suft [swpt' | N ~] shoulder' (immediately before 'suftan, sumb- … pierce, bore'), and in the English index 'shoulder dōš, suft'. Confirms the Middle Persian link Nourai leaves implicit.\"},\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. سفت۲\", \"stance\": \"supports\",\n       \"note\": \"'سفت۲ (suft) (.) دوش، کتف' with the Pahlavi transliteration in Moʿin's usual brackets; the neighbouring entries سفت۱ 'ستبر، غلیظ، محکم' and سفت۳ '= سفتن، سوراخ کردن' show that Moʿin, like Borhan, keeps the three homophones apart.\"},\n      {\"src\": \"HUB\", \"where\": \"HUB.txt\", \"stance\": \"silent\",\n       \"note\": \"Hübschmann's Persische Studien has no note on Horn no. 789; searched 'supti', 'suft' — the only hits (gusuftan, āsuftan) belong to the unrelated verb root.\"},\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt\", \"stance\": \"silent\",\n       \"note\": \"Nyberg's glossary has no suft 'shoulder' (only āsuftan/āšuft-kārīh from a different root); his corpus simply does not contain the word.\"}\n     ]\n    }\n   ]\n  },\n\n  {\n   \"entry\": 4,\n   \"root\": \"Kŭp 2, Kwĕp\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *kʷep- / *kʷap- / *kup- 'to smoke, boil, cook; be agitated'\",\n   \"note\": \"Pokorny 596-597 gives '(keu̯ap-:) ku̯ep-, ku̯ap-, kup- … Meaning: to smoke; to boil; to cook', with Skt. kupyati 'is seething, is angry', Lat. cupiō and vapor, Gk. kapnós, Lith. kvãpas, OCS kypěti; Watkins/AHD prints 'kʷēp-. To smoke, cook, move violently, be agitated emotionally' — which is word-for-word the gloss Nourai puts in his root box, so his AHD:1524 citation is the source of his wording. Root, language label and gloss are all right. Both authorities hedge: AHD calls it a 'hypothetical base of possibly related words', because the Latin and Greek reflexes need irregular treatments of the labiovelar.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kʷep- / *kʷap- / *kup- «دود کردن، جوشیدن، پختن؛ برآشفتن» است. پوکورنی در صفحه‌های ۵۹۶–۵۹۷ آن را با همین معنی می‌آورد و سنسکریت kupyati «می‌جوشد، خشمگین می‌شود»، لاتینی cupiō و vapor، یونانی kapnós، لیتوانیایی kvãpas و اسلاوی کهن kypěti را زیر آن می‌گذارد. واتکینز در پیوست ریشه‌های هندواروپاییِ فرهنگ American Heritage عیناً همان تعریفی را دارد که نورایی در جعبهٔ ریشه نوشته است («to smoke, cook, move violently, be agitated emotionally»)، پس عبارت نورایی از همان‌جا گرفته شده. ادعای نورایی دربارهٔ ریشه، نام زبان و معنی درست است؛ تنها باید افزود که هر دو مرجع این ریشه را «فرضی» می‌خوانند، زیرا بازتاب‌های لاتینی و یونانی آن به تحول‌های نامنظمِ همخوان لبی‌کامی نیاز دارند.\",\n   \"sources\": [W + \"cupio\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:596\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt, block ending 'References: WP. I 379 f., WH. I 312 f., Trautmann 147. Page(s): 596-597': 'Root / lemma: (keu̯ap-:) ku̯ep-, ku̯ap-, kup- … Meaning: to smoke; to boil; to cook'. Exactly the root and gloss of the box.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kʷēp-\", \"stance\": \"supports\",\n     \"note\": \"'kʷép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kʷap-… a. Latin vapor…: VAPOR; EVAPORATE; … c. Greek kapnos, smoke: ACAPNIA. [Pok. kʷēp- 596.]' — Nourai's root gloss is a verbatim copy of this line.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 379 f. (WLD_Bd1_pages.txt leaf 388)\", \"stance\": \"supports\",\n     \"note\": \"The Walde-Pokorny article behind POK 596: 'Lit. kvãpas \\\"Hauch, Dunst, Wohlgeruch\\\" (: lat. vapor) … lit. kupuoti \\\"schwer atmen\\\", lett. kupēt \\\"rauchen, dampfen\\\" … apr. kupsins \\\"Nebel\\\" (Ableitung von einem es-St. wie lat. vapor)'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. kʷapos and kūpiō (2)\", \"stance\": \"supports\",\n     \"note\": \"'kʷapos, ā (kʷuap-) \\\"exhalation, vapour\\\". Cf. kʷēp-. WP I, 379 Gk. kápos, id.; kapúō, v. \\\"exhale\\\"; Alb. (?) vapë \\\"sultriness\\\"; Umb. cf. vaputu \\\"with incense\\\"; Lat. cf. vapor, vapidus; Li. kvãpas' and 'kūpiō (2) \\\"surge, swell, stir, seethe\\\". WP I, 379 Skt. kupye … Lat. cupiō … \\\"desire\\\"'.\"},\n    {\"src\": \"SYN\", \"where\": \"§3.76 MONKEY p.188\", \"stance\": \"partial\",\n     \"note\": \"Buck cites the root only for the colour words: 'Skt. kapi- : kapila- \\\"brownish, reddish\\\", fr. \\\"smoke-colored\\\", Grk. kapnós, etc.? Walde-P. 1.379.' — with a question mark.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"kapi; kapila; kapî\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Three words with three different standings. (a) kapi- 'incense, smoke-colour': Pokorny prints it as 'kapi- (unbelegt) \\\"incense\\\"', i.e. unattested — the chart's own NOTE ('POK indicates that \\\"kapi\\\" is not verified') reproduces this correctly, and it is really a form posited only to explain the colour adjectives. (b) kapila-, kapiśa- 'brownish, reddish': Pokorny and Buck both derive these from that posited *kapi- as '*smoke-coloured' (< *kʷap- 'smoke'), and this is unobjectionable in itself, though it rests on the unattested noun. (c) kapí- m. 'ape, monkey' (RV 10.86.5, the Vṛṣākapi hymn): Pokorny adds it to the same article ('also kapí- m. \\\"ape\\\"') on the strength of the colour link, and Buck §3.76 repeats it with a question mark, adding that Skt. kapi- is 'prob. source of Egypt. gephi, Grk. kēpos, kēbos'. Modern Indo-Aryan etymology reverses this: kapí- is treated as a culture word/Wanderwort of non-Indo-European origin — Wiktionary (following Mayrhofer) says 'a foreign Wanderwort, likely borrowed from a western substrate. The same Wanderwort may be reflected in Hebrew קוֹף (qōf), Akkadian uqūpu, Egyptian gfj, Middle Persian kabīg, Ancient Greek κῆπος, and Proto-Germanic *apô.' Since the whole Persian branch of this chart hangs on the 'monkey' word, the node has to take the worse verdict: the derivation of kapí- 'monkey' from *kʷep- 'to smoke' is rejected by current scholarship, even though the colour words may indeed belong there.\",\n     \"derivation_fa\": \"سه واژه با سه وضع متفاوت. نخست kapi- «بخور، رنگِ دود»: پوکورنی خودِ آن را «unbelegt» یعنی بی‌گواه می‌خواند و یادداشت خودِ نمودار نیز همین را بازتاب می‌دهد؛ این صورت تنها برای توجیه صفت‌های رنگ فرض شده است. دوم kapila- و kapiśa- «خرمایی، سرخ‌فام»: پوکورنی و باک این‌ها را از همان *kapi- به معنی «دودرنگ» می‌گیرند و این استنباط فی‌نفسه پذیرفتنی است، هرچند بر نامی بی‌گواه استوار است. سوم kapí- «بوزینه، میمون» (ریگ‌ودا ۱۰:۸۶:۵): پوکورنی آن را نیز به همین ریشه می‌بندد و باک با علامت پرسش تکرارش می‌کند و می‌افزاید که سنسکریت kapi- «احتمالاً سرچشمهٔ gephi مصری و kēpos یونانی است». اما ریشه‌شناسی امروزی هندوآریایی این را وارونه می‌داند: kapí- واژه‌ای فرهنگی و «واژهٔ سرگردان» (Wanderwort) غیرهندواروپایی است که با عبری qōf، اکدی uqūpu، مصری gfj، فارسی میانه kabīg، یونانی kēpos و ژرمنی آغازین *apô یک خانواده را می‌سازد (ویکی‌واژه به پیروی از مایرهوفر). چون کل شاخهٔ فارسیِ این نمودار به واژهٔ «میمون» بسته است، حکم بدترِ گره را می‌گیریم: پژوهش امروزی پیوند kapí- را با ریشهٔ «دود» رد می‌کند.\",\n     \"sources\": [W + \"%E0%A4%95%E0%A4%AA%E0%A4%BF\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:596\", \"status\": \"supports\",\n       \"note\": \"POK p.596: 'Old Indic kupyati (= Latin cupiō) \\\"is seething, is angry\\\", kopa- m. \\\"surge, rage, fury\\\" … kapi- (unbelegt) \\\"incense\\\", wherefore as \\\"*smoke-color\\\" kapila-, kapiśa- \\\"brownish, reddish\\\", also kapí- m. \\\"ape\\\"'. All three of Nourai's words, and the '(unbelegt)' that his NOTE reports.\"},\n      {\"ref\": \"SYN:188\", \"status\": \"supports\",\n       \"note\": \"Buck §3.76 MONKEY, printed p.188 (the page number stands in the same column; the next section 3.77 ELEPHANT opens p.189): '6. Skt. kapi- : kapila- \\\"brownish, reddish\\\", fr. \\\"smoke-colored\\\", Grk. kapnós, etc.? Walde-P. 1.379. Prob. source of Egypt. gephi, Grk. kēpos, kēbos, etc.' Buck supports Nourai — but with a question mark, and with the loan direction opposite to the modern one.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 379 f.\", \"stance\": \"supports\",\n       \"note\": \"The Walde-Pokorny article Buck and Pokorny both cite for this equation (WP I 379) is the one containing lit. kvãpas : lat. vapor and the Indic kup-/kap- material.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, s.v. kʷapos / kūpiō (2)\", \"stance\": \"partial\",\n       \"note\": \"Mann keeps the verbal and 'vapour' material ('Skt. kupye … Lat. cupiō'; 'Gk. kápos … Lat. vapor') but lists no kapi- 'monkey' under either lemma — the animal name is left out of the Indo-European comparison.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kʷēp-\", \"stance\": \"partial\",\n       \"note\": \"Watkins keeps only the Latin and Greek reflexes (cupere, vapor, vapidus, kapnos) under kʷēp-; no Sanskrit kapi- of any sense is admitted.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"kapik\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian kapīk / kabīg 'monkey' (Book Pahlavi <kpyk'>) is well attested; MacKenzie's Concise Pahlavi Dictionary p.49 has 'kabīg [kpyk' | N kab/pi] monkey' and the English index 'monkey kabīg'. It is not an inherited Iranian word but an early loan from Indic: Hübschmann, Persische Studien p.87, says of Horn's list 'Hier fehlt np. kabī \\\"Affe\\\" JRAS. 1894, p. 480 = phl. kapik, arm. LW. kapik, skr. kapi-. Das Wort ist in alter Zeit aus dem Indischen entlehnt' ('the word was borrowed from Indic in early times'); Laufer, Sino-Iranica p.581 states it flatly: 'Middle Persian kapīk, Persian kabī (\\\"monkey\\\"), is derived from Skr. kapi.' Phonetically Skt. kapí- was taken as *kapi- and given the ordinary MP nominal suffix -īk/-īg (<-k'>), the same suffix as in MP mardōmīg etc.; the Old Armenian loan կապիկ kapik, borrowed from Middle Iranian, preserves the intervocalic -p- and thus dates the borrowing before the MP lenition p > b in <kabīg>. Nourai's arrow Sanskrit → Pahlavi is exactly the received view; only the direction of his upper arrow (root → Sanskrit) is at issue (node 1).\",\n     \"derivation_fa\": \"فارسی میانه kapīk / kabīg «میمون» (املای پهلوی کتابی <kpyk'>) واژه‌ای گواهی‌شده است؛ مکنزی در «فرهنگ کوچک پهلوی» ص ۴۹ می‌آورد: «kabīg [kpyk'] monkey» و در نمایهٔ انگلیسی «monkey kabīg». این واژه ایرانیِ موروثی نیست، بلکه وام‌واژه‌ای کهن از هندی است: هوبشمان در «مطالعات فارسی» ص ۸۷ می‌نویسد «np. kabī \\\"میمون\\\" = پهلوی kapik، وام‌واژهٔ ارمنی kapik، سنسکریت kapi-؛ این واژه در روزگار کهن از هندی وام گرفته شده است»؛ و لاوفر در Sino-Iranica ص ۵۸۱ صریحاً می‌گوید «فارسی میانه kapīk و فارسی kabī از سنسکریت kapi گرفته شده‌اند». از نظر آوایی kapí سنسکریت به‌صورت *kapi- گرفته شده و پسوند رایج اسمی فارسی میانه ‎-īk/-īg‎ بر آن افزوده شده است؛ وام‌واژهٔ ارمنی کهن կապիկ kapik که p میان‌واکه‌ای را نگاه داشته نشان می‌دهد وام‌گیری پیش از نرم‌شدن p به b در kabīg رخ داده است. پس پیکان نورایی از سنسکریت به پهلوی دقیقاً دیدگاه پذیرفته‌شده است.\",\n     \"sources\": [W + \"%DA%A9%D9%BE%DB%8C\", W + \"kabig\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:87\", \"status\": \"not_found\",\n       \"note\": \"Horn's Grundriss p.87 (HRN.txt leaf 108 = 87+21) contains entries nos. 387-391 — teš 'Axt', tiš 'Durst', tešt 'Becken', tuf 'Speichel', tek 'schnell' — nothing about monkeys; and Hübschmann's note on the same printed page 87 of his own book says the word is MISSING from Horn ('Hier fehlt np. kabī \\\"Affe\\\"'). Nourai's 'HRN:87' is almost certainly a slip for the HUB:87 he cites on the next node (Moʿin's footnote in Borhan s.v. کپی likewise cites 'هوبشمان ص ۸۷', not Horn).\"},\n      {\"ref\": \"SIN:581\", \"status\": \"supports\",\n       \"note\": \"Laufer, Sino-Iranica, printed p.581 (SIN.txt leaf 408-409; the index entry 'kapi 581' confirms the page): 'Middle Persian kapīk, Persian kabī (\\\"monkey\\\"), is derived from Skr. kapi.'\"}\n      ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 49 s.v. kabīg\", \"stance\": \"supports\",\n       \"note\": \"'kabīg [kpyk' | N kab/pi] monkey' — MacKenzie normalises the older reading kapīk as kabīg and gives the New Persian reflex kabī/kapī.\"},\n      {\"src\": \"HUB\", \"where\": \"p. 87 (HUB.txt leaf 97)\", \"stance\": \"supports\",\n       \"note\": \"'Hier fehlt np. kabī \\\"Affe\\\" JRAS. 1894, p. 480 = phl. kapik, arm. LW. kapik, skr. kapi-. Das Wort ist in alter Zeit aus dem Indischen entlehnt. Jetzt wird dafür buzīna, būzina etc. gebraucht.'\"},\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt\", \"stance\": \"silent\",\n       \"note\": \"Nyberg's Pahlavi glossary has no kapik/kabīg; the word does not occur in his selection of texts.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"kapî «کپی»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian کَپی / کَپّی kapī, kappī 'ape, monkey' is the direct continuation of MP kabīg: the MP suffix -īg loses its -g in New Persian (the regular MP -īg > NP -ī, as in MP mardōmīg > NP mardumī), giving kapī, with an expressive geminate variant kappī and the by-form کبی kabī with the lenited stop. Wiktionary states it exactly so: 'Inherited from Middle Persian kpyk' /kabīg/, \\\"monkey\\\", from Sanskrit कपि (kapi, \\\"ape, monkey\\\"). Akin to Old Armenian կապիկ (kapik); an Iranian borrowing.' The word is a Shāhnāma word — Nourai's quotation 'بر هر دو بیشه یکی بُرز کوه / بر آن کوه کپی فراوان گروه' is genuine Ferdowsī, and Noushin's Vāzhe-nāmak s.v. کپی glosses it 'میمون، بوزینه. پهلوی کپیک kapīk' with the Shāhnāma line 'ورا شیر کپی همی خواندند'. Borhan-e Qateʿ, printed p.1593, has 'کپی: بفتح اول و کسر ثانی مشدد و غیر مشدد، میمون را گویند عموماً و میمون سیاه را خصوصاً', i.e. both kapī and kappī, and Moʿin's footnote there cites Hübschmann p.87 and Laufer, Sino-Iranica p.581 — the very two references Nourai uses. Modern Persian has replaced the word with میمون/بوزینه, as Hübschmann already noted in 1895.\",\n     \"derivation_fa\": \"«کَپی / کَپّی» فارسی نو دنبالهٔ مستقیم فارسی میانهٔ kabīg است: پسوند ‎-īg‎ فارسی میانه در فارسی نو ‎g‎ پایانی را از دست می‌دهد (مانند mardōmīg > مردمی) و kapī به دست می‌آید؛ گونهٔ مشدد kappī حالت تأکیدی است و «کبی» گونه‌ای با ابدال p به b. ویکی‌واژه همین را می‌گوید: «موروث از فارسی میانهٔ kabīg \\\"میمون\\\"، از سنسکریت कपि kapi». این واژه شاهنامه‌ای است؛ بیتی که نورایی آورده («بر هر دو بیشه یکی بُرز کوه / بر آن کوه کپی فراوان گروه») از فردوسی است و نوشین در «واژه‌نامک» ذیل «کپی» می‌نویسد «میمون، بوزینه. پهلوی کپیک kapīk». برهان قاطع در صفحهٔ ۱۵۹۳ می‌آورد: «کپی: بفتح اول و کسر ثانی مشدد و غیر مشدد، میمون را گویند عموماً و میمون سیاه را خصوصاً»، و حاشیهٔ معین در همان‌جا به هوبشمان ص ۸۷ و لاوفر ص ۵۸۱ ارجاع می‌دهد — یعنی همان دو مأخذی که نورایی به کار برده است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%DA%A9%D9%BE%DB%8C\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1593\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ vol. 3, printed p.1593 = pdf p.386 of BQT_v3 (BQT_v3_pages.txt leaf 385, the printed number matching the +1207 offset exactly): 'کپی: بفتح اول و کسر ثانی مشدد و غیر مشدد، میمون را گویند عموماً و میمون سیاه را خصوصاً … وآن جانوری است شبیه بآدمی', with Moʿin's footnotes '= کبی (هم)', 'هویشمان [= هوبشمان] ص ۸۷' and 'پارسی kapīk … Laufer, Sino-Iranica p. 581'.\"},\n      {\"ref\": \"FSF:268\", \"status\": \"supports\",\n       \"note\": \"Noushin, Vāzhe-nāmak (FSF_pages.txt leaf 360): 'کپی (بازبر اول): میمون، بوزینه. پهلوی کپیک kapīk (یادداشت‌های گات‌ها ۶۲۴)', followed by the Shāhnāma citation 'ورا شیر کپی همی خواندند'.\"},\n      {\"ref\": \"HUB:87\", \"status\": \"supports\",\n       \"note\": \"Hübschmann, Persische Studien p.87: 'np. kabī \\\"Affe\\\" … = phl. kapik, arm. LW. kapik, skr. kapi-'. The New Persian word is the headword of the note.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 49 s.v. kabīg\", \"stance\": \"supports\",\n       \"note\": \"'kabīg [kpyk' | N kab/pi] monkey' — MacKenzie explicitly gives the New Persian reflex as kabī/kapī.\"},\n      {\"src\": \"SIN\", \"where\": \"p. 581\", \"stance\": \"supports\",\n       \"note\": \"'Middle Persian kapīk, Persian kabī (\\\"monkey\\\"), is derived from Skr. kapi.'\"},\n      {\"src\": \"MON\", \"where\": \"MON_part2.txt\", \"stance\": \"silent\",\n       \"note\": \"Moʿin's Farhang-e Fārsi entry for کپی could not be isolated in the OCR of the lexicon volumes (the string is swamped by modern کپی 'copy' < French copie); his etymological note on the word is the one printed in the Borhan footnote quoted above.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur's Indo-European roots dictionary has no entry for کپی (searched the Persian headword); expected, since he treats only inherited Indo-European vocabulary and this is an Indic loan.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Old Persian\", \"words\": \"kupsins\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"There is no Old Persian word kupsins. The form comes from Pokorny p.597, where the Baltic paragraph of the root article ends 'Old Prussian kupsins \\\"fog\\\" (derivative from an es-stem as Latin vapor)' — Walde-Pokorny I 379-380 has the German original, 'apr. kupsins \\\"Nebel\\\" (Ableitung von einem es-St. wie lat. vapor)', where apr. = altpreußisch, Old Prussian. Nourai has read the abbreviation 'apr.'/'Old Prussian' as 'Old Persian' and moved a Baltic word into the Iranian column; the gloss 'mists' is a faithful rendering of 'Nebel', which is why the mistake is invisible from the gloss alone. kupsins is in fact the accusative singular of Old Prussian *kupsis (Elbing Vocabulary/Trautmann, Altpreußische Sprachdenkmäler 365), an -s-stem derivative built like Latin vapor. Kent's Old Persian lexicon has nothing of the kind, and the Old Persian corpus contains no word for 'mist' at all. Checked against the printed page (render of pdf p.286 at 200 dpi, copied to data/verification/sources/refs/ocr/BOOK/286.png): the book itself prints 'Old Persian / POK:597 / kupsins : mists', so this is Nourai's own error and the extraction is faithful.\",\n     \"derivation_fa\": \"چنین واژه‌ای در پارسی باستان وجود ندارد. صورت kupsins از صفحهٔ ۵۹۷ پوکورنی آمده است؛ آنجا در بند بالتیکِ همین ریشه می‌خوانیم «apr. kupsins \\\"Nebel\\\"» و در والده–پوکورنی جلد ۱ ص ۳۷۹–۳۸۰ نیز همین عبارت با توضیح «(Ableitung von einem es-St. wie lat. vapor)». کوته‌نوشت apr. یعنی altpreußisch «پروسی باستان» (زبانی بالتیک)، نه پارسی باستان؛ نورایی این کوته‌نوشت را «Old Persian» خوانده و واژه‌ای بالتیک را به ستون ایرانی برده است. معنی «مه» (mists) ترجمهٔ درست Nebel است و از همین رو خطا از روی معنی پیدا نمی‌شود. kupsins در واقع صورت رایی مفردِ *kupsis پروسی باستان است (تراوتمان، Altpreußische Sprachdenkmäler ۳۶۵) و مانند vapor لاتینی از ستاک ‎-s-‎ ساخته شده. در واژه‌نامهٔ پارسی باستانِ کنت هیچ واژه‌ای از این دست نیست. با نگاه به صفحهٔ چاپی (تصویر صفحهٔ ۲۸۶ پی‌دی‌اف، نگه‌داشته در data/verification/sources/refs/ocr/BOOK/286.png) روشن شد که خودِ کتاب «Old Persian … kupsins : mists» چاپ کرده است: پس خطای چاپی/خوانشِ خودِ نورایی است و استخراج داده درست انجام شده.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"Old Persian ⌷ POK:597 | kupsins : mists\",\n     \"correct_form\": \"Old Prussian kupsins 'fog, mist' (altpreußisch; Pokorny 597, WP I 379 f.)\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:597\", \"status\": \"contradicts\",\n       \"note\": \"POK_full.txt, lemma ku̯ep- pp.596-597: '…changing through ablaut Lithuanian kupuoti \\\"breathe heavily\\\", Latvian kupēt \\\"smoke; steam\\\", kupinaties \\\"rise (of dough)\\\", kupti \\\"ferment, seethe\\\", Old Prussian kupsins \\\"fog\\\" (derivative from an es-stem as Latin vapor)'. The page Nourai cites has the word — but as Old Prussian, in the Baltic paragraph, not as Old Persian.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 379 f. (WLD_Bd1_pages.txt leaf 388)\", \"stance\": \"contradicts\",\n       \"note\": \"'lett. kupēt \\\"rauchen, dampfen, stieben\\\", kupinaties \\\"aufgehn (vom Teig)\\\", kupt \\\"gären\\\", apr. kupsins \\\"Nebel\\\" (Ableitung von einem es-St. wie lat. vapor) s. Trautmann Apr. 365' — 'apr.' = altpreußisch, Old Prussian.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon pp.164-215\", \"stance\": \"silent\",\n       \"note\": \"Searched KNT.txt for 'kupsin', 'mist', 'fog': no Old Persian entry of this shape or meaning exists; the corpus has no word for 'mist'.\"},\n      {\"src\": \"BRT\", \"where\": \"BRT.txt\", \"stance\": \"silent\",\n       \"note\": \"Bartholomae's Altiranisches Wörterbuch (which covers Old Persian as well as Avestan) has no kupsin-/kupsins.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": null, \"words\": \"\",\n     \"verdict\": \"unverified\",\n     \"derivation\": \"An empty box. On the render of pdf page 286 (200 dpi, copied to data/verification/sources/refs/ocr/BOOK/286.png) a wide blank rectangle is drawn to the right of the 'Old Persian kupsins' box, joined to it by an arrow, with no language label, no reference and no word inside; the extraction is faithful (lang null, refs null, words []). Nothing can be verified. Since the parent box is itself a misplaced Old Prussian word (node 4), there is no Iranian or Persian continuation that could have been meant to stand here; the likeliest explanation is that Nourai left the slot open for a Persian reflex he never found, exactly because none exists.\",\n     \"derivation_fa\": \"این خانه در کتاب کاملاً خالی است: در تصویر صفحهٔ ۲۸۶ پی‌دی‌اف (نگه‌داشته در data/verification/sources/refs/ocr/BOOK/286.png) مستطیلی پهن و بی‌متن در کنار جعبهٔ «Old Persian kupsins» رسم شده و پیکانی آن دو را به هم می‌پیوندد، اما نه نام زبانی در آن هست، نه مأخذی و نه واژه‌ای؛ استخراج داده درست انجام شده است (زبان و مأخذ و واژه هر سه تهی). چیزی برای راستی‌آزمایی نیست. چون جعبهٔ مادر خود واژه‌ای پروسی باستان است که به‌اشتباه در ستون ایرانی نشسته (گرهٔ ۴)، هیچ دنبالهٔ ایرانی یا فارسی‌ای برای این خانه متصور نیست؛ به گمان قوی نورایی جای بازتاب فارسی را باز گذاشته و هرگز آن را نیافته، زیرا چنین بازتابی وجود ندارد.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book (refs None in the extraction, and the printed box has no book icon).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon\", \"stance\": \"silent\",\n       \"note\": \"No Old Persian word for 'mist/fog' exists that could descend into a Persian form here.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary\", \"stance\": \"silent\",\n       \"note\": \"No Middle Persian reflex of a *kup-s- 'mist' stem; the MP words for 'mist/fog' are mēġ and dūd.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Latin\", \"words\": \"vapor\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Latin vapor, -ōris m. 'steam, warm exhalation, heat' is old (Plautus, Ennius) and the older spelling uapōs is transmitted (Priscian), which shows an original s-stem *kʷap-ōs-. Pokorny p.596 puts it under the root: 'Latin … vapor \\\"haze, mist, vapor\\\", old uapos (*kʷapōs)'; Watkins/AHD has 'Zero-grade form *kʷap-, becoming *kʷap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE'; Mann's IEC lemma 'kʷapos, ā \\\"exhalation, vapour\\\"' collects Gk. kápos, Alb. vapë, Umbrian vaputu, Lat. vapor, Lith. kvãpas. The reservation, which is why this is 'plausible' and not 'confirmed', is phonetic: Latin normally gives qu- (or c- before back vowels), not v-, for PIE *kʷ, so the derivation needs a special loss of the labiovelar's velar element (assumed via *quapor > *vapor, possibly dissimilatory before the following labial). Wiktionary therefore says 'From Proto-Italic *kʷapōs, of uncertain ultimate origin, but possibly related to Ancient Greek καπνός and PIE *kʷep- … via an older form *quapor that eventually lost its velar', and Etymonline calls Latin vapor 'of unknown origin'. So the arrow is the standard handbook derivation, but hedged by every modern authority.\",\n     \"derivation_fa\": \"واژهٔ لاتینی vapor «بخار، دم گرم، گرما» کهن است (پلاؤتوس، انیوس) و صورت کهن‌ترِ uapōs نیز نقل شده که بر ستاک ‎-s-‎ آغازینِ *kʷap-ōs- گواهی می‌دهد. پوکورنی در ص ۵۹۶ آن را زیر همین ریشه می‌آورد: «lat. vapor \\\"Dunst, Dampf\\\"، کهن uapos (*kʷapōs)»؛ واتکینز نیز «صورت درجهٔ صفرِ *kʷap- … لاتینی vapor» را ذیل kʷēp- می‌گذارد و مان در «فرهنگ تطبیقی هندواروپایی» سرواژهٔ kʷapos «دم، بخار» را با یونانی kápos، آلبانیایی vapë، اومبریایی vaputu و لیتوانیایی kvãpas می‌سازد. تنها اشکال، آوایی است و از همین رو حکم «با احتیاط پذیرفتنی» است: در لاتینی بازتاب عادی *kʷ هندواروپایی qu- است نه v-، و برای این واژه باید افتادن عنصر کامیِ همخوان لبی‌کامی را (از راه *quapor > vapor، شاید ناهمگونی در برابر لبیِ پس از آن) فرض کرد. ویکی‌واژه می‌گوید «از ایتالیایی آغازین *kʷapōs، با خاستگاه نهایی نامعلوم، شاید مرتبط با kapnós یونانی و *kʷep- هندواروپایی» و اتیمانلاین آن را «با خاستگاه ناشناخته» می‌خواند.\",\n     \"sources\": [W + \"vapor\", \"https://www.etymonline.com/word/vapor\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:596\", \"status\": \"supports\",\n       \"note\": \"POK p.596: 'Latin cupiō, -ere \\\"lust, crave\\\" (= Old Indic kupyati) … vapor \\\"haze, mist, vapor\\\", old uapos (*kʷapōs)'.\"},\n      {\"ref\": \"AHD:1524\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. kʷēp-: '2. Zero-grade form *kʷap-, becoming *kʷap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus …; c. Greek kapnos, smoke: ACAPNIA.' (The 1985 standalone edition is unpaginated in the way the 1975 New College appendix was; the content of p.1524 of that appendix is this k-section.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"IEC\", \"where\": \"Mann, s.v. kʷapos\", \"stance\": \"supports\",\n       \"note\": \"'kʷapos, ā (kʷuap-) \\\"exhalation, vapour\\\". Cf. kʷēp-. WP I, 379 Gk. kápos, id.; kapúō, v. \\\"exhale\\\"; Alb. (?) vapë \\\"sultriness\\\"; Umb. cf. vaputu \\\"with incense\\\"; Lat. cf. vapor, vapidus; Li. kvãpas'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 379 f.\", \"stance\": \"supports\",\n       \"note\": \"'Lit. kvãpas \\\"Hauch, Dunst, Wohlgeruch\\\" (: lat. vapor)' — the Latin word set beside the Baltic one under the same root.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. Cupid (cross-reference 'Cp. also vapor')\", \"stance\": \"supports\",\n       \"note\": \"Klein groups vapor with cupere under the same Indo-European material ('Gk. καπνός (for *kʷapnos), \\\"smoke, vapor\\\" … Cp. also vapor').\"},\n      {\"src\": \"LEW\", \"where\": \"LEW_1910.txt\", \"stance\": \"silent\",\n       \"note\": \"The OCR of Walde's 1910 Lateinisches etymologisches Wörterbuch on disk returns no hit for 'vapor' (the v- section is missing/illegible in this scan), so it could not be used.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"vapor, evaporate\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English vapour/vapor is first recorded in the late 14th century, in the medical-physiological sense 'moisture arising from heated matter, fumes from incense'; Etymonline: 'late 14c., vapour, \\\"steam, moisture arising from heated matter; fumes from incense\\\", from Anglo-French vapour, Old French vapor \\\"moisture, vapor\\\" (13c., Modern French vapeur) and directly from Latin vaporem (nominative vapor)'. The scientific sense 'gaseous form of a substance' is a mid-17th-century specialisation. Evaporate is a 15th-century learned borrowing of Latin ēvapōrāre 'to disperse in vapour' (ē- 'out' + vapōrāre, denominative of vapor), so both English words go back to the Latin noun exactly as the chart draws. Watkins lists both under the root: 'EVAPORATE kʷēp-', 'VAPOR kʷēp-'.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی vapour/vapor نخستین بار در اواخر سدهٔ چهاردهم میلادی و در معنای پزشکی–طبیعیِ «بخارِ برخاسته از مادهٔ گرم‌شده» ثبت شده است؛ اتیمانلاین می‌نویسد: «از انگلونورمن vapour و فرانسوی کهن vapor (سدهٔ سیزدهم، فرانسوی امروز vapeur) و نیز مستقیماً از لاتینی vaporem». معنای علمی «حالت گازی یک ماده» تخصیصی است از میانهٔ سدهٔ هفدهم. evaporate وام‌واژه‌ای دانشورانه از سدهٔ پانزدهم است از لاتینی ēvapōrāre «به بخار پراکندن» (پیشوند ē- «بیرون» + vapōrāre از vapor). پس هر دو واژهٔ انگلیسی درست همان‌گونه که نمودار نشان می‌دهد به اسم لاتینی بازمی‌گردند و واتکینز نیز هر دو را ذیل ریشهٔ kʷēp- فهرست کرده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/vapor\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. kʷēp-: 'Latin vapor, steam, vapor: VAPOR; EVAPORATE'; and in the word index 'EVAPORATE kʷēp-' and 'VAPOR kʷēp-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, s.v. Cupid (cross-ref) and vapor\", \"stance\": \"supports\",\n       \"note\": \"Klein's Cupid article closes 'Cp. concupiscence, covet. Cp. also acapnia. Cp. also vapor.', placing English vapor in the same etymological family.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\",\n       \"note\": \"The 1911 Concise edition's entry could not be retrieved from the OCR text on disk; no evidence either way from Skeat.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Latin\", \"words\": \"cupere\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin cupiō, cupere 'to long for, desire' is the securest reflex of the root, because it matches Sanskrit kupyati 'seethes, is agitated' form for form: both continue a *kup-ye/o- present built on the zero grade *kup- of *kʷep-. Pokorny p.596 prints the equation explicitly: 'Latin cupiō, -ere \\\"lust, crave\\\" (= Old Indic kupyati)'; Watkins: 'Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE'; Wiktionary: 'From Proto-Italic *kupjō. According to the LIV, inherited from Proto-Indo-European *kup-yé-ti, from *kʷep- \\\"to smoke, boil, move violently\\\" … the term has an exact parallel in Sanskrit कुप्यति (kupyati). De Vaan, however, explains the word as a derivative of an athematic i-present *kup-i- of the same root.' The semantic bridge is the physical 'boil, seethe, be agitated' > emotional 'burn with desire', the same shift seen in Skt. kopa- 'rage' and OCS kypěti 'boil'. Note that in the zero grade *kup- the labiovelar loses its labial element before u, which is why cupere shows c- while vapor shows v-.\",\n     \"derivation_fa\": \"لاتینی cupiō, cupere «آرزو کردن، خواستن» استوارترین بازتاب این ریشه است، زیرا مو‌به‌مو با سنسکریت kupyati «می‌جوشد، برمی‌آشوبد» برابر می‌افتد: هر دو ادامهٔ ستاک حال *kup-ye/o- بر درجهٔ صفرِ *kup- از ریشهٔ *kʷep- هستند. پوکورنی در ص ۵۹۶ همین برابری را صریح می‌آورد: «lat. cupiō, -ere \\\"lust, crave\\\" (= ai. kupyati)»؛ واتکینز نیز «صورت پسوندیِ *kup-yo- در لاتینی cupere» را می‌آورد. ویکی‌واژه به نقل از LIV همین را می‌گوید و می‌افزاید که دِ فان آن را ستاک حالِ ‎i‎‌دارِ *kup-i- از همین ریشه می‌داند. پل معنایی از «جوشیدن، برآشفتن» جسمانی به «سوختن در آرزو» عاطفی است، همان تحول معنایی که در kopa- سنسکریت «خشم» و kypěti اسلاوی کهن «جوشیدن» دیده می‌شود. نکتهٔ آوایی آنکه در درجهٔ صفر (*kup-) عنصر لبیِ همخوان لبی‌کامی پیش از u می‌افتد و از این رو cupere با c- آغاز می‌شود حال آنکه vapor با v-.\",\n     \"sources\": [W + \"cupio\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1524\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. kʷēp-: '1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE.' Exactly Nourai's arrow, and the English derivative Cupid is named in the same line.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"p. 596\", \"stance\": \"supports\",\n       \"note\": \"'Latin cupiō, -ere \\\"lust, crave\\\" (= Old Indic kupyati), cuppēdō \\\"a desire, wish, longing\\\" … also cuppes \\\"lascivious\\\", cuppedium \\\"snacking, tidbit\\\"'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, s.v. kūpiō (2)\", \"stance\": \"supports\",\n       \"note\": \"'kūpiō (2) \\\"surge, swell, stir, seethe\\\". WP I, 379 Skt. kupye … beside … Av. kup-, id.; Lat. cupiō, -īre & -ere \\\"desire\\\" … OCS kypljǫ, kypěti \\\"well up, rise, swell, abound\\\"'.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein, s.v. Cupid\", \"stance\": \"supports\",\n       \"note\": \"'fr. cupiō, cupere, \\\"to desire\\\", which is prob. cogn. with OI. kupyati, \\\"bubbles up, becomes agitated\\\", OSlav. kypljǫ, kypěti, \\\"to boil\\\", Lith. kūpu, kupėti, \\\"to boil over\\\" … Gk. καπνός (for *kʷapnos), \\\"smoke, vapor\\\", Goth. af-hapjan …'.\"},\n      {\"src\": \"LAT\", \"where\": \"LAT.txt (Ernout-Meillet)\", \"stance\": \"silent\",\n       \"note\": \"Searched for 'vapor'/'cupio' in the OCR of Ernout-Meillet on disk: no readable hits (the scan's text layer is defective in this part of the alphabet).\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"Cupid\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English Cupid (late 14th c.) is Latin Cupīdō, the personification of the common noun cupīdō 'desire, love, passion', itself formed on cupidus 'longing, eager' from cupiō, cupere. Klein s.v.: 'Cupid, n., the god of love in Roman mythology. — L. Cupīdō, personification of cupīdō, \\\"desire, love\\\", fr. cupidus, \\\"longing, desirous, eager\\\", fr. cupiō, cupere, \\\"to desire\\\"'; Etymonline agrees: 'Roman god of passionate love, late 14c., from Latin Cupido, personification of cupido \\\"desire, love, passion\\\", from cupere \\\"to desire\\\"'. The god was identified with Greek Eros. Watkins names CUPID among the English descendants of *kup-yo- in the same entry as cupere, so the chart's Latin → English arrow is the standard account.\",\n     \"derivation_fa\": \"«کیوپید» انگلیسی (اواخر سدهٔ چهاردهم میلادی) همان Cupīdō لاتینی است، یعنی شخصیت‌بخشیِ اسم عام cupīdō «آرزو، عشق، شور» که خود از صفت cupidus «آرزومند، مشتاق» و آن از فعل cupiō, cupere ساخته شده است. کلاین ذیل همین مدخل می‌نویسد: «Cupid: خدای عشق در اساطیر روم — از لاتینی Cupīdō، شخصیت‌بخشی cupīdō \\\"آرزو، عشق\\\"، از cupidus، از cupere \\\"خواستن\\\"»؛ اتیمانلاین نیز همین را می‌آورد و می‌افزاید که این خدا با اروسِ یونانی یکی دانسته شده است. واتکینز نیز CUPID را در همان مدخلِ cupere در شمار بازماندگان انگلیسیِ *kup-yo- آورده است. پس پیکان لاتینی ← انگلیسی در نمودار همان روایت پذیرفته‌شده است و ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/cupid\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference in the book (refs None); the parent node's AHD:1524 covers it, since Watkins lists CUPID under kʷēp-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, s.v. Cupid\", \"stance\": \"supports\",\n       \"note\": \"'Cupid, n., the god of love in Roman mythology. — L. Cupīdō, personification of cupīdō, \\\"desire, love\\\", fr. cupidus, \\\"longing, desirous, eager\\\", fr. cupiō, cupere, \\\"to desire\\\" …'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kʷēp-\", \"stance\": \"supports\",\n       \"note\": \"'*kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE.'\"}\n     ]\n    }\n   ]\n  },\n\n  {\n   \"entry\": 5,\n   \"root\": \"Kupriti\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Akkadian kibrītu (older reading kuprītu) 'sulphur, brimstone'\",\n   \"note\": \"The root box reproduces Zimmern, Akkadische Fremdwörter p.60, which Nourai cites: 'akk. wahrsch. kuprītu Schwefel, dann: > hebr. gop̄rīt, aram. guprītā, kubrītā, kebrītā (> arab. kibrīt)', with the footnote 'kuprītu könnte einfach Weiterbildung von kupru \\\"Erdpech\\\" sein' — 'probably', and possibly a derivative of kupru 'bitumen'. So the language label (Akkadian) and the gloss ('sulfur') are right, and the whole chain of the chart is Zimmern's. The reservation is the shape of the head-form: modern Assyriology normalises the word as kibrītu (so the CAD, and Wiktionary's Akkadian entry 𒆠𒀀𒀭𒀀𒇉 kibrītu 'sulfur; firebrand'), not kuprītu; Zimmern's kuprītu was a reading meant to tie the word to kupru 'bitumen'. Nourai's 'Kupriti' is therefore a real but superseded form, which also makes the vowel of the Aramaic/Arabic forms easier to explain (kibrītu > kibrītā > kibrīt directly, with no u/i alternation to account for).\",\n   \"note_fa\": \"جعبهٔ ریشه دقیقاً برگردانِ صفحهٔ ۶۰ کتاب تسیمرن «وام‌واژه‌های اکدی» است که خودِ نورایی به آن ارجاع می‌دهد: «اکدی، به احتمال، kuprītu \\\"گوگرد\\\"، و از آنجا > عبری gop̄rīt، آرامی guprītā، kubrītā، kebrītā (> عربی kibrīt)»، با این پانوشت که «kuprītu شاید تنها ساختی برگرفته از kupru \\\"قیر\\\" باشد». پس نام زبان (اکدی) و معنی (گوگرد) درست است و کل زنجیرهٔ نمودار از تسیمرن گرفته شده. تنها اشکال در صورتِ سرواژه است: آشورشناسی امروزی این واژه را kibrītu می‌خواند (فرهنگ آشوری شیکاگو، و مدخل اکدیِ ویکی‌واژه: kibrītu «گوگرد؛ مشعل»)، نه kuprītu؛ خوانشِ kuprītu را تسیمرن برای پیوند دادن واژه به kupru «قیر» پیشنهاد کرده بود. بنابراین «Kupriti» صورتی واقعی اما کهنه و کنارگذاشته‌شده است؛ با خوانش امروزی، واکهٔ صورت‌های آرامی و عربی نیز آسان‌تر توضیح داده می‌شود.\",\n   \"sources\": [W + \"%D9%83%D8%A8%D8%B1%D9%8A%D8%AA\"],\n   \"ref_check\": [\n    {\"ref\": \"AKD:60\", \"status\": \"supports\",\n     \"note\": \"Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, printed p.60 (AKD.txt leaf 70, the running number '61' following immediately): 'akk. wahrsch. kuprītu Schwefel, dann: > hebr. gop̄rīt, aram. guprītā, kubrītā, kebrītā (> arab. kibrīt)', footnote 6 'kupritu könnte einfach Weiterbildung von kupru Erdpech, sein.' Word for word the root box and the whole chart.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1171\", \"stance\": \"supports\",\n     \"note\": \"'Ar. kibrīt: \\\"Schwefel\\\" [Fremdwort aus dem aram. kebrītā < ass. kuprītu \\\"Schwefel\\\", dieses möglicherweise aus kupru, s. hier Nr. 727, vgl. ZAkkFW 60]; hieraus mit ar. Art. sp. alcrebite \\\"dass.\\\"; in der Bedeutung \\\"Schwefel-, Streichhölzchen\\\" tk. kibrit; hieraus rum. chibrit.' Lokotsch cites the very page (ZAkkFW 60) Nourai cites.\"},\n    {\"src\": \"BQT\", \"where\": \"vol. 3 printed p.1588, Moʿin's footnote 4\", \"stance\": \"supports\",\n     \"note\": \"'در زبان اکدی صورت Kupritu آمده و ازآنجا [به] زبان‌های سامی دیگر رفته. در آرامی gubrita … در عبری Gofrit … در عربی «کبریت» («معجمیات عربیه ـ سامیه» ص ۱۸۸)' — Moʿin repeats Zimmern's kuprītu and the same chain.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt line 5521)\", \"stance\": \"supports\",\n     \"note\": \"'كبريت \\\"der Schwefel\\\" ist zunächst aus [dem Aramäischen] entlehnt' — Fraenkel makes Arabic kibrīt an Aramaic loan, the middle link of the chart.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\",\n     \"note\": \"Searched FVQ.txt for 'kibrit', 'sulphur', 'brimstone': no entry — the word is not Qurʾānic, so Jeffery does not treat it.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Aramaic\", \"words\": \"gubrîtâ, kubrîtâ\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The Aramaic forms are real and stand exactly where the chart puts them: Zimmern p.60 lists 'hebr. gop̄rīt, aram. guprītā, kubrītā, kebrītā' as the Semitic descendants of the Akkadian word, and Wiktionary gives Jewish Babylonian Aramaic כִּבְּרִיתָא (kibrīṯā) and Syriac ܟܶܒܪܺܝܬܳܐ (keḇrīṯā) 'sulfur', from Akkadian kibrītu. The two variants Nourai prints reflect the two treatments of the initial stop in the Aramaic dialects (voiced g- in the Palestinian/Targumic tradition, matching Hebrew gop̄rīṯ, versus k- in the Babylonian and Syriac tradition); the -ā is the ordinary Aramaic determinate-state ending added to the borrowed noun, and the -īt- is simply the Akkadian feminine formation -ītu taken over unchanged. Moʿin's footnote in Borhan-e Qateʿ p.1588 gives the same set of forms, citing the Arabic-Semitic comparative dictionary he used.\",\n     \"derivation_fa\": \"صورت‌های آرامی واقعی‌اند و درست همان‌جا می‌نشینند که نمودار نشانشان می‌دهد: تسیمرن در ص ۶۰ «عبری gop̄rīt، آرامی guprītā، kubrītā، kebrītā» را بازماندگان سامیِ واژهٔ اکدی می‌شمارد، و ویکی‌واژه آرامی بابلیِ یهودی כִּבְּרִיתָא و سریانی ܟܶܒܪܺܝܬܳܐ «گوگرد» را از اکدی kibrītu می‌گیرد. دو گونه‌ای که نورایی چاپ کرده بازتاب دو رفتار با همخوان آغازین در گویش‌های آرامی است: g واک‌دار در سنت فلسطینی–ترگومی (همسان با gop̄rīṯ عبری) در برابر k در سنت بابلی و سریانی. پایانهٔ ‎-ā‎ همان نشانهٔ حالت معرفهٔ آرامی است که بر اسم وام‌گرفته افزوده شده، و ‎-īt-‎ نیز همان پایانهٔ مؤنث اکدی ‎-ītu‎ است که دست‌نخورده انتقال یافته. حاشیهٔ معین بر برهان قاطع (ص ۱۵۸۸) نیز همین مجموعهٔ صورت‌ها را می‌آورد.\",\n     \"sources\": [W + \"%D9%83%D8%A8%D8%B1%D9%8A%D8%AA\"],\n     \"ref_check\": [\n      {\"ref\": \"AKD:60\", \"status\": \"supports\",\n       \"note\": \"Zimmern p.60: 'akk. wahrsch. kuprītu Schwefel, dann: > hebr. gop̄rīt, aram. guprītā, kubrītā, kebrītā (> arab. kibrīt)'. Both of Nourai's Aramaic variants are in the list.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, AFA.txt line 5521\", \"stance\": \"supports\",\n       \"note\": \"Fraenkel's article on كبريت states that the Arabic word 'ist zunächst aus [dem Aramäischen] entlehnt' — presupposing exactly this Aramaic stage.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1171\", \"stance\": \"supports\",\n       \"note\": \"'Fremdwort aus dem aram. kebrītā < ass. kuprītu \\\"Schwefel\\\"'.\"},\n      {\"src\": \"BQT\", \"where\": \"vol. 3 p.1588, Moʿin's footnote\", \"stance\": \"supports\",\n       \"note\": \"'در آرامی gubrita' — the g-form; the note also gives the Hebrew Gofrit and Palestinian-Aramaic form.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Arabic\", \"words\": \"kibrit\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic كِبْرِيت kibrīt 'sulphur' (later also 'match') is a loan from Aramaic kibrīṯā/keḇrīṯā, itself from Akkadian: Wiktionary states 'Borrowed from Aramaic כִּבְּרִיתָא (kiḇrīṯā) / ܟܶܒܪܺܝܬܳܐ (kĕḇrīṯā, \\\"sulfur\\\"), from Akkadian 𒆠𒀀𒀭𒀀𒇉 (kibrītu, \\\"sulfur; firebrand\\\")'; Fraenkel's Die aramäischen Fremdwörter im Arabischen treats it under the Aramaic loans; Lokotsch no.1171 says the same and traces the Spanish alcrebite (with the Arabic article) to it. The word is not from an Arabic triliteral root — the pattern kiCCīC with four consonants k-b-r-t is not a native Arabic noun pattern, which is precisely the formal sign of the borrowing (Arab lexicographers nevertheless treat it as a quadriliteral). The sense 'match, lucifer' is a modern extension, from the sulphur head of the match, and it is that extended sense that Persian and Turkish share. Nourai's Aramaic → Arabic arrow is the standard account.\",\n     \"derivation_fa\": \"عربی «کِبریت» (گوگرد؛ و در دورهٔ جدید «چوب کبریت») وام‌واژه‌ای از آرامی kibrīṯā / keḇrīṯā است که خود از اکدی گرفته شده؛ ویکی‌واژه می‌نویسد: «وام‌گرفته از آرامی כִּבְּרִיתָא، از اکدی kibrītu \\\"گوگرد؛ مشعل\\\"». فرنکل نیز در «وام‌واژه‌های آرامی در عربی» آن را در شمار وام‌های آرامی می‌آورد و لوکوچ (شمارهٔ ۱۱۷۱) همین را می‌گوید و alcrebite اسپانیایی را (با حرف تعریف عربی) از آن می‌گیرد. این واژه از ریشهٔ سه‌حرفی عربی ساخته نشده است؛ وزن kiCCīC با چهار همخوان k-b-r-t وزن اسمی بومی عربی نیست و همین نشانهٔ صوریِ وام‌گیری است، هرچند لغویان عرب آن را رباعی شمرده‌اند. معنای «چوب کبریت» گسترشی نو است، از سرِ گوگردیِ چوب، و همین معنای گسترده است که فارسی و ترکی نیز دارند. پیکان آرامی ← عربی در نمودار همان روایت پذیرفته‌شده است.\",\n     \"sources\": [W + \"%D9%83%D8%A8%D8%B1%D9%8A%D8%AA\"],\n     \"ref_check\": [\n      {\"ref\": \"AKD:60\", \"status\": \"supports\",\n       \"note\": \"Zimmern p.60: '… aram. guprītā, kubrītā, kebrītā (> arab. kibrīt)' — the arrow into Arabic is drawn by Zimmern himself.\"},\n      {\"ref\": \"BQT:1588\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ vol. 3, printed p.1588 = pdf p.381 of BQT_v3 (leaf 380; the +1207 offset matches the printed number): 'کبریت … گوگرد را گویند … عربی است' ('kibrīt … they call sulphur … it is Arabic'), with Moʿin's footnote 4 tracing the word Akkadian > Aramaic/Hebrew > Arabic.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, AFA.txt line 5521\", \"stance\": \"supports\",\n       \"note\": \"'كبريت \\\"der Schwefel\\\" ist zunächst aus [dem Aramäischen] entlehnt'.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1171\", \"stance\": \"supports\",\n       \"note\": \"'Ar. kibrīt: \\\"Schwefel\\\" [Fremdwort aus dem aram. kebrītā < ass. kuprītu \\\"Schwefel\\\"] … hieraus mit ar. Art. sp. alcrebite; in der Bedeutung \\\"Schwefel-, Streichhölzchen\\\" tk. kibrit; hieraus rum. chibrit.'\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\",\n       \"note\": \"No entry; the word does not occur in the Qurʾān.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitāb al-alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\",\n       \"note\": \"No headword كبريت (searched AFM.txt/AFM_pages.txt) — consistent with the word being an Aramaic, not a Persian, loan in Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"kebrît «کبریت»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian کبریت kebrīt 'sulphur; match' is a straightforward Arabic loan of the Islamic period, taken with the Arabic form unchanged (only the vowel is read in the Persian way, kibrīt > modern Tehran kebrit). Wiktionary: 'Borrowed from Arabic كِبْرِيت (kibrīt, \\\"sulfur, match\\\"), from Aramaic כִּבְּרִיתָא, from Akkadian kibrītu'; Borhan-e Qateʿ p.1588 says so in as many words — 'کبریت … گوگرد را گویند … عربی است' — using the inherited Persian word گوگرد gōgerd as its gloss, which shows that kebrīt was felt as the foreign term; Moʿin's Farhang-e Fārsi marks it '[معر.]' (muʿarrab, i.e. an Arabicised foreign word) and glosses it 'گوگرد'. This is therefore not a Persian → Arabic → Persian round trip: the word entered Persian from Arabic and had never been Persian before. The modern sense 'match' followed the Arabic and Ottoman development in the 19th century (cf. Turkish kibrit, whence Romanian chibrit).\",\n     \"derivation_fa\": \"«کبریت» فارسی نو (گوگرد؛ چوب کبریت) وام‌واژه‌ای عربی از دورهٔ اسلامی است که صورت عربی را بی‌تغییر گرفته و تنها واکه به شیوهٔ فارسی خوانده شده (kibrīt > کِبریتِ امروزی). ویکی‌واژه می‌نویسد: «وام‌گرفته از عربی كِبْرِيت، از آرامی כִּבְּרִיתָא، از اکدی kibrītu». برهان قاطع در ص ۱۵۸۸ خود صریح می‌گوید «کبریت … گوگرد را گویند … عربی است» و برای معنی کردنش واژهٔ موروثی فارسی «گوگرد» را به کار می‌برد، که نشان می‌دهد کبریت واژه‌ای بیگانه احساس می‌شده است؛ معین نیز در «فرهنگ فارسی» آن را با نشانهٔ [معر.] (معرّب) می‌آورد و «گوگرد» معنی می‌کند. پس این واژه رفت‌وبرگشت فارسی ← عربی ← فارسی نیست، بلکه از عربی به فارسی آمده و پیش از آن فارسی نبوده است. معنای «چوب کبریت» در سدهٔ نوزدهم به پیروی از عربی و ترکی عثمانی پدید آمد (ترکی kibrit و از آن رومانیایی chibrit).\",\n     \"sources\": [W + \"%DA%A9%D8%A8%D8%B1%DB%8C%D8%AA\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1588\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ vol. 3 p.1588: 'کبریت = بکسر اول و سکون ثانی … گوگرد را گویند و آن گرم و خشک است در چهارم … و زر خالص را نیز گفته‌اند. عربی است.' Borhan itself declares the word Arabic; Moʿin's footnote adds the Akkadian-Aramaic prehistory.\"},\n      {\"ref\": \"MON:2887\", \"status\": \"supports\",\n       \"note\": \"Moʿin, Farhang-e Fārsi (MON_part2.txt, ک section): 'کبریت: [معر.] (.) گوگرد' — the tag [معر.] = معرّب marks it as an Arabicised (i.e. borrowed, non-Persian) word; the same volume also has 'فوطی کبریت' and 'کبریت احمر'. The exact printed page could not be read off the OCR, but the entry Nourai cites is this one.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. کبریت\", \"stance\": \"supports\",\n       \"note\": \"'کبریت: [معر.] (.) گوگرد. (ف.) … کبریت نباتی: (گیا.) پنجهٔ گرگک' — Moʿin's origin tag [معر.] agrees with the Arabic route.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1171\", \"stance\": \"supports\",\n       \"note\": \"Lokotsch's article carries the word from Aramaic through Arabic into Spanish, Turkish and Romanian; the Persian shares the Arabic form and the 'match' sense with Turkish.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur's Indo-European roots dictionary has no کبریت — as expected for a Semitic loanword.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n       \"note\": \"No entry for كبريت (searched PLA_pages.txt / the djvu text): Asbaghi lists Persian loans IN Arabic, and this word is not one, confirming that the direction is Arabic → Persian and not the reverse.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-286.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk286.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-286.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 286"
}
```


### [2026-09-06T22:09:06.394Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk286.py", line 197, in <module>
    "id": 5, "lang": null, "words": "",
                     ^^^^
NameError: name 'null' is not defined
```


## [2026-09-06T22:09:11.257Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && sed -i 's/\"id\": 5, \"lang\": null,/\"id\": 5, \"lang\": None,/' mk286.py && python3 mk286.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-286.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 286"
}
```


### [2026-09-06T22:09:13.472Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 10, 'disputed': 1, 'transcription_suspect': 1, 'unverified': 1, 'plausible': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 19, 'partial': 1, 'not_found': 1, 'contradicts': 1, 'not_checked': 2}
books consulted: {'supports': 26, 'silent': 16, 'partial': 2, 'contradicts': 1} | by book: {'WLD': 4, 'PHD': 4, 'KLN': 4, 'MON': 3, 'IEC': 3, 'LKT': 3, 'BRT': 2, 'HUB': 2, 'NYB': 2, 'AHD': 2, 'ARY': 2, 'KNT': 2, 'AFA': 2, 'SYN': 1, 'SIN': 1, 'LEW': 1, 'SKT': 1, 'POK': 1, 'LAT': 1, 'BQT': 1, 'FVQ': 1, 'AFM': 1, 'PLA': 1}
```


## [2026-09-06T22:09:22.859Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"AFM kibrit:\"; grep -c \"كبريت\\|کبریت\" AFM.txt AFM_pages.txt; echo \"PLA:\"; grep -c \"كبريت\\|kibrit\\|Kibrit\" incoming/PLA/PLA_pages.txt incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo \"ARY kabrit/kapi:\"; grep -c \"کبریت\" incoming/ARY/ARY_pages.txt; grep -c \"کپی\" incoming/ARY/ARY_pages.txt; echo \"NYB kapik:\"; grep -c \"kapik\\|kabig\\|kabīg\" NYB_vol2_glossary.txt; echo \"SKT vapor:\"; grep -n \"^vapour\\|Vapour\\|vapour,\" SKT.txt | head -3"
}
```


### [2026-09-06T22:09:22.958Z] TOOL RESULT

```
AFM kibrit:
AFM_pages.txt:2
AFM.txt:2
PLA:
incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt:0
incoming/PLA/PLA_pages.txt:0
ARY kabrit/kapi:
0
0
NYB kapik:
0
SKT vapor:
1096:Atmosphere.  (Gk.)  LU.  'a  sphere  of air  round  the  earth.*  Coined  from  uxfuj-, for  (iT^iJr,  vapour,  air :  and  Sphere.
2332:Perhaps  related  to  G.  brudeJn,  br^dtM,  to bubble  (whence  to  give  off  steam,  coofose) ; a.  brodel,  broifem,  vapour,  allied  to  E. Breath  (Schclcr).  Cf.  F.  btvuUhrJ,  a mist,  fog.  %  We  also  find  >N.brxKh^  tumult, broiheii.  a  tempest ;  Gael.  brei,^hUadh,  titf- moil.  broigiuk,  noise  (pcrhft[>.s  unrelated). Broker.  <E.)  SceBrooku)- Bronchial.  (Gk.)  Gk.  Bfiyx****  neol. pi.,  the  ramifications  of  the  windpipe.— Gk.  ^p6yxot,  ihe  windpipe  ;  cf.  fipnyx*^-  ' gill.  Allied  to  Gk.  a^x'"*'  ^^  ^<^^-  ^*'* brvrKk't'tis;  (rom  0p6yxof. Bronze.  (F.-ltal.-Teat)  SeeBrown. Brooch.  (F.-L.)  Named  from  the  pin which  fastens  iL  M.  E.  brockr,  a  pin,  yejL brooch.  —  F.  brocht,  a  spit,  point.  —Low  L bnvfa,  a  pointed  stick.  — L.^/vrinttj,  ashaip tooth,  pomt  Cf.  Gael.  bn>ff,  to  goad.^r^, on  awl ;  \V.  procio^  to  stab.
4669:Damp.  <E.)  Cf.  M.  E.  dam/tm,  I focate.  Not  in  A.  S.  +  On  damp,  if steam ;  r>an.  damp,  G.  damp/,  ti Swcd.  damb,  dust.  Allic^l  lo  Gk. vapour,  Skt.  dkiipa^  iDcenae. Sec  Dust.
```


## [2026-09-06T22:09:29.395Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if 'كبريت' in p or 'کبریت' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        j=max(p.find('كبريت'),p.find('کبریت'))\n        print('leaf',i,'tag',m.group(1) if m else '?')\n        print(p[max(0,j-600):j+400].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-06T22:09:30.956Z] TOOL RESULT

```
leaf 140 tag ?
لاوم( - ومعنى ¥ الماذب ٠‏ ويرادفة 6 :)10 ` القاطع : « قيل ان ܦ صمغ ܣܨ الرومي وهو في بلاد البلغار: وقيل صمغ الدَوْم ٠‏ وقيل ضرب من الاؤلو يوجد في سواحل بجر المغرب ٠وقيل‏ صمغ شجر يشبه شجر الفستق يشتعل بالنار مثل الكبريت ولهذا قيل له سيّد الكباريت ٠‏ وقيل يأبع من ܐܐܟ في بلاد الروس واول مسا يضر به اللهواء يحمد مثل المرمر وهذا الحكهر باء اقيق ويقال له بالعربّة مصباح الروم ٠‏ وقيل اله من انواع ܝ  -:‏ 50 ܟܗܪܒ̄ܐ نكر 2 ) الذل الطغيد المخضر 6 6 ٠ 1‏ 0 ير اراس لاحرؤة 4 او لآ حرظوم ل وهو معرب عن كوب , والثلاهر ان الكلمة من موافتات اللغات وهر حه كمط" بالارامية ( ¥+ 9 ] ܐܟ ) ܕ ܟܘܦܐ بالسريانّة الدارجة وكرب بالتركّة والك
---
leaf 154 tag ?
ل ܕܙܘ | شت الصحاج :« والذي تراه كالطر يق من النمل نفسها ٠»‏ والنمل اذا جاء منها واحد في 39 0 ܕܟܐ ܨ ܠܐܝܐ والميّة. ܢ الواضح : معربان عن ÷ ن اي ` الأو $ 6 نات 98 7( 3:77 ونون يقترن 391 ܕܐ لهُ بالتركية « اغسطوس كلى ܙܝ ܐܥ كل ».وان كان زهره ابيض قيل له « اق كل » وان كان اي ` كل 0 ل داوس 03 قوي © |( الأزهري : ولا أدري 355 ام لا ܐܝܝ وهو فارسي 209 نسْرين ويقال له ;± « وان كلى ومصر 0 ( ܬܐܨ ) ܘܬܒܘ ܐܝܬ ذات طعم جامض حاد ورف تكبريت الدخان وملح 57 00 في البرهان القاطع :« النشادر ضر بان معدلي 0-0 فالمعدلي. مصلل عله في 5 من جبال سمرقند وفي 55035 - | بر دمندان في كمان اذ يخْرج من تلك المغارة جار نظير الدخان فيجمد في اطراف 0 مثل ܠ وهو نادر عزيز الوجود . والمصنوع يعمل من سواد الدخان الجتمع في ١تون‏ الام وهو نافع من < العين ومن الدمعة 3 وهو 5 نشادر بالتركة والكردنة و ط18ط11311131 باأروسة 1 1 ܐܳܢ ܝܨ ܝ 5 واصل العنى فيه | ܐܨ ܟ 0
---
```


## [2026-09-06T22:09:43.257Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-286.json'\nd=json.load(open(p,encoding='utf-8'))\nold_afm=\"No headword كبريت (searched AFM.txt/AFM_pages.txt) — consistent with the word being an Aramaic, not a Persian, loan in Arabic.\"\nnew_afm=\"No headword كبريت in Addi Shir's list of Persian words Arabicised (searched AFM.txt / AFM_pages.txt): the string occurs only twice, in passing inside other articles (s.v. كهربا, 'يشتعل بالنار مثل الكبريت ولهذا قيل له سيّد الكباريت', and s.v. نشادر). Its absence as a headword is itself evidence that the word is an Aramaic and not a Persian loan in Arabic.\"\nold_skt=\"The 1911 Concise edition's entry could not be retrieved from the OCR text on disk; no evidence either way from Skeat.\"\nnew_skt=\"Skeat's Concise Etymological Dictionary has no headword 'vapour' in the OCR on disk (grep finds the word only inside other articles, e.g. s.v. Atmosphere 'ἀτμός, vapour, air'); no evidence either way from Skeat.\"\ns=json.dumps(d,ensure_ascii=False,indent=1)\nassert old_afm in s and old_skt in s\ns=s.replace(old_afm,new_afm).replace(old_skt,new_skt)\nio.open(p,'w',encoding='utf-8').write(s)\njson.load(open(p,encoding='utf-8'))\nprint('ok')\nEOF\npython3 tools/verify_check.py 286"
}
```


### [2026-09-06T22:09:44.940Z] TOOL RESULT

```
ok
nodes verified: 14/14
node verdicts: {'confirmed': 10, 'disputed': 1, 'transcription_suspect': 1, 'unverified': 1, 'plausible': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 19, 'partial': 1, 'not_found': 1, 'contradicts': 1, 'not_checked': 2}
books consulted: {'supports': 26, 'silent': 16, 'partial': 2, 'contradicts': 1} | by book: {'WLD': 4, 'PHD': 4, 'KLN': 4, 'MON': 3, 'IEC': 3, 'LKT': 3, 'BRT': 2, 'HUB': 2, 'NYB': 2, 'AHD': 2, 'ARY': 2, 'KNT': 2, 'AFA': 2, 'SYN': 1, 'SIN': 1, 'LEW': 1, 'SKT': 1, 'POK': 1, 'LAT': 1, 'BQT': 1, 'FVQ': 1, 'AFM': 1, 'PLA': 1}
```


## [2026-09-06T22:10:06.387Z] AGENT

Page 286 (book p. 256) verified — `data/verification/page-286.json` written, `verify_check.py 286` reports 0 PROBLEM lines.

**Counts** — 14/14 nodes: 10 confirmed, 1 plausible, 1 disputed, 1 transcription_suspect, 1 unverified. Roots: 2 confirmed, 1 plausible. Ref checks: 19 supports, 1 partial, 1 not_found, 1 contradicts, 2 not_checked. 45 `consulted` entries across 23 books.

**Flagged items**
- **transcription_suspect — Kŭp 2, node #4 "Old Persian kupsins : mists"**: there is no such Old Persian word. Pokorny 597 / Walde-Pokorny I 379 f. read `apr. kupsins "Nebel"` — *apr.* = altpreußisch, **Old Prussian** (acc. sg. of an s-stem, Trautmann Apr. 365). Nourai read the abbreviation as "Old Persian" and moved a Baltic word into the Iranian column. `error_in: book` — the printed page (render saved to `data/verification/sources/refs/ocr/BOOK/286.png`) shows "Old Persian … kupsins : mists", so the extraction is faithful.
- **disputed — Kŭp 2, node #1 Sanskrit kapi / kapila / kapî**: Pokorny and Buck (§3.76, p.188) do put kapí- "monkey" under the "smoke/brown" root, but modern Indo-Aryan etymology treats kapí- as a non-IE Wanderwort (Heb. qōf, Akk. uqūpu, Egypt. gfj, Gk. κῆπος, PGmc *apô). kapi- "incense" is unattested (Pokorny's "unbelegt", which the chart's own NOTE reports correctly); kapila-/kapiśa- "brownish" may well belong there.
- **not_found ref — Kŭp 2, node #2 `HRN:87`**: Horn p. 87 has entries 387–391 (t-words), nothing about monkeys; Hübschmann p. 87 says the word is *missing* from Horn. Almost certainly a slip for HUB:87 (Moʿin's footnote in Borhan s.v. کپی likewise cites "هویشمان ص ۸۷").
- **plausible root — Kupriti**: Zimmern AKD:60 does read "akk. wahrsch. kuprītu Schwefel", but modern Assyriology normalises the etymon as **kibrītu** (CAD; Wiktionary), so Nourai's head-form is real but superseded. The rest of the chain (Aramaic gubrītā/kubrītā → Arabic kibrīt → Persian کبریت) is confirmed by Wiktionary, Fraenkel, Lokotsch no. 1171 and Moʿin's footnote at BQT 1588.
- **plausible — Latin vapor**: Pokorny/Watkins/Mann/Klein derive it from *kʷap-, but *kʷ > Latin v- is irregular; Wiktionary ("uncertain ultimate origin") and Etymonline ("of unknown origin") hedge.

**Extraction issue for the owner (minor)**: node #3 of Kŭp 2 — the printed Persian box shows **two** script forms, «کَپی ، کَپّی» (Borhan p. 1593 gives both مشدد and غیر مشدد readings), but the JSON keeps only `کپی` in `script` and `script_extra`.

Reference hits confirmed exactly as cited: POK:627, POK:596/597, SYN:236 (§4.30 SHOULDER) and SYN:188 (§3.76 MONKEY), HRN:163 (no. 789 suft), HUB:87, SIN:581, BQT:1143, BQT:1588 and BQT:1593 (all three page numbers land on the right leaves), FSF:268, AKD:60, AHD:1524. 10 web pages archived via `fetch_source.py`.
