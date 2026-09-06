# Verification process log — verify-page-258


## [2026-09-06T16:15:29.884Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 258 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-258.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-258.json. Write /home/sfmqrb/git/rishe/data/verification/page-258.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 258` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:15:31.428Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T16:15:32.161Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:15:32.176Z] TOOL RESULT

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


## [2026-09-06T16:15:32.406Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-258.txt"
}
```


### [2026-09-06T16:15:32.426Z] TOOL RESULT

```
1	=== PDF page 258 (book page 228) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ker 4, Kers 1, Kerb : dirt, dark, black  (refs POK:573,583)
4	#1 (parent #0) [Pahlavi] refs=POK:573 | karic : dirt, manure
5	  #2 (parent #1) [Persian] refs=POK:573; BQT:1631; MON:1281 | kareh «کَره ۱» : dirt ; čardeh «چَرده (سیاه چرده)» : a suffix indicating (dark) color | extra: چَرته ، چَرد ، چَرزه
6	#3 (parent #0) [Old Persian] refs=POK:583 | kirsman : black
7	  #4 (parent #3) [Persian] refs=BQT:1619 | kars «کَرس ( کیرس ، کیرسنه ۱)» : dirt
8	#5 (parent #0) [Sanskrit] refs=POK:583 | kršna : black
9	  #6 (parent #5) [Persian] refs=BQT:1619 | karsneh «کَرسنه ۲ (کَسنی ، کَشنک )» : a black grain
10	  #7 (parent #5) [Hindustani] refs=AHD:727 | krišna : the black one
11	    #8 (parent #7) [English] refs=AHD:727 | Krishna
12	--- entry 1 ---
13	ROOT [Indo-European] Ker 5, Kur, Kertâ : heat, fire  (refs POK:571; IEC:590)
14	#1 (parent #0) [Persian] refs=IEC:590; MON:3121 | kŭreh «کوره» : fireplace, oven, kiln
15	#2 (parent #0) [Germanic] refs=AHD:1522 | herthô : hearth
16	  #3 (parent #2) [English] refs=AHD | hearth
17	#4 (parent #0) [Latin] refs=AHD:1522 | carbô : charcoal
18	  #5 (parent #4) [English] refs=AHD | carbon, carburetor
19	  #6 (parent #4) [French] refs=AHD | 
20	    #7 (parent #6) [Persian] refs=VOP:267,278 | karbon «کربن ( کاربن )» : carbon | extra: کربنات ، کربنیک ، کربور ، کاربوراتور
21	#8 (parent #0) [Latin] refs=AHD:1522 | cremâre : to burn
22	  #9 (parent #8) [English] refs=AHD | cremate
23	#10 (parent #0) [Greek] refs=AHD:1522 | keramos : potter's clay
24	  #11 (parent #10) [English] refs=AHD | ceramic
25	  #12 (parent #10) [French] refs=None | 
26	    #13 (parent #12) [Persian] refs=VOP:211 | serâmîc «سرامیک» : ceramic
27	--- entry 2 ---
28	ROOT Kerb -> redirect to Ker 4
29	
```


## [2026-09-06T16:15:35.567Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-258.json",
 "description": "Read source JSON for page 258"
}
```


### [2026-09-06T16:15:35.671Z] TOOL RESULT

```
{
  "pdf_page": 258,
  "book_page": 228,
  "entries": [
    {
      "root": {
        "name": "Ker 4, Kers 1, Kerb",
        "lang": "Indo-European",
        "refs": "POK:573,583",
        "gloss": "dirt, dark, black"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "POK:573",
          "words": [
            {"translit": "karic", "gloss": "dirt, manure", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:573; BQT:1631; MON:1281",
          "words": [
            {"translit": "kareh", "gloss": "dirt", "script": "کَره ۱"},
            {"translit": "čardeh", "gloss": "a suffix indicating (dark) color", "script": "چَرده (سیاه چرده)"}
          ],
          "script_extra": "چَرته ، چَرد ، چَرزه",
          "note": null,
          "quote": {
            "text": "چون دست و پای پاک نبینمت جان و دل - این هردو پاک بینم و آن هردو با کره",
            "poet": "Nâser-Khosrow"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:583",
          "words": [
            {"translit": "kirsman", "gloss": "black", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1619",
          "words": [
            {"translit": "kars", "gloss": "dirt", "script": "کَرس ( کیرس ، کیرسنه ۱)"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:583",
          "words": [
            {"translit": "kršna", "gloss": "black", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:1619",
          "words": [
            {"translit": "karsneh", "gloss": "a black grain", "script": "کَرسنه ۲ (کَسنی ، کَشنک )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "Hindustani",
          "refs": "AHD:727",
          "words": [
            {"translit": "krišna", "gloss": "the black one", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:727",
          "words": [
            {"translit": "Krishna", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ker 5, Kur, Kertâ",
        "lang": "Indo-European",
        "refs": "POK:571; IEC:590",
        "gloss": "heat, fire"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:590; MON:3121",
          "words": [
            {"translit": "kŭreh", "gloss": "fireplace, oven, kiln", "script": "کوره"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "به آسانی مرا از من ربودی - درون کورهٔ غم آزمودی",
            "poet": "Moshîrî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1522",
          "words": [
            {"translit": "herthô", "gloss": "hearth", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "hearth", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1522",
          "words": [
            {"translit": "carbô", "gloss": "charcoal", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "carbon, carburetor", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "VOP:267,278",
          "words": [
            {"translit": "karbon", "gloss": "carbon", "script": "کربن ( کاربن )"}
          ],
          "script_extra": "کربنات ، کربنیک ، کربور ، کاربوراتور",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1522",
          "words": [
            {"translit": "cremâre", "gloss": "to burn", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cremate", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1522",
          "words": [
            {"translit": "keramos", "gloss": "potter's clay", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "ceramic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 10,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "VOP:211",
          "words": [
            {"translit": "serâmîc", "gloss": "ceramic", "script": "سرامیک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kerb",
        "redirect": "Ker 4"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T16:15:36.385Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:15:36.443Z] TOOL RESULT

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


## [2026-09-06T16:15:54.143Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','IEC','BQT','MON','VOP','KLN','SKT','LEW','LAT','SYN','WLD','PHD','HRN','HUB','ARY']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-06T16:15:54.537Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && sed -n '1,60p' data/verification/page-202.json",
 "description": "List verification outputs and sample"
}
```


### [2026-09-06T16:15:55.879Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
```


### [2026-09-06T16:15:56.019Z] TOOL RESULT

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
----
{
 "pdf_page": 202,
 "book_page": 172,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Gwa, Gwâ, Gwen 2",
   "verdict": "confirmed",
   "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
   "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
   "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
   ],
   "ref_check": [
    {
     "ref": "POK:463",
     "status": "supports",
     "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')",
     "stance": "supports",
     "note": "'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.')."
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, g-list (AHD_watkins1985.txt line ~539)",
     "stance": "supports",
     "note": "'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman in a. Old English cuman, to come: COME … 3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein, to go, walk, step, with basis (< *gʷm̥-ti-), a stepping, tread, base'. Same double root, same gloss."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *gam¹ (CHEUNG.txt lines 7307, 7478) and *gaH¹ (line 7054)",
     "stance": "supports",
     "note": "'*gam¹ \"to come\" … «PIE *gʷem- “to go; come” = LIV: 209 f. | Pok.: 464 f.»'; and '«PIE *gʷeH₂- “to go, stride” = LIV: 205 | Pok.: 463 f.»'. Cheung's *gam¹ article lists, as its New-Persian outcome, exactly Nourai's harvest: 'NP zamān “time” … NP gām “step, pace” … NP āmadan … NP pay(g)ām “message”, NP pay(g)ambar … NP anjuman “company, assembly, club”'."
    },
    {
     "src": "SYN",
     "where": "Buck §10.47/10.48 (SYN.txt line 17514 f.)",
     "stance": "supports",
     "note": "'2. IE *gʷem-, *gʷā-. Walde-P. 1.675 ff. … Skt., Av., OPers. gam- \"go, come\" (Skt. gacchati, Av. jasaiti, sk̑o- presents like Grk. baskō; Av. jam- without prefix mostly \"come\"; also Av., OPers. ā-jam- \"come\", whence NPers. amadan \"come\")'."
    },
    {
     "src": "KLN",
     "where": "p.318 s.v. 'come' (KLN_1966.txt line 8320, page marker 318 at the foot)",
     "stance": "supports",
     "note": "'come … fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati … Avestic jamaiti “goes” … Cp. the collateral base *gʷā- in OI. agām (aor.), Gk. ébēn (aor.), “I went”'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan / Old Persian",
     "words": "gam : to come, step; jam, jantu : to go",
```


## [2026-09-06T16:16:01.950Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 228 229 230; do echo \"===== NR=$n =====\"; awk 'BEGIN{RS=\"\\f\"} NR=='$n'' POK_02.txt | head -70; done",
 "description": "Print Pokorny leaves near p.573"
}
```


### [2026-09-06T16:16:04.269Z] TOOL RESULT

```
===== NR=228 =====
  lett. kräcu,  slav.  krakati,  vgl.  mit  -g:  gr.  tiqw^o),  anord.   hrökr);
mir.  cräin,  Gen.  cräna  ,Sau*  (,grunzend^;  urkelt.  *kräkni-)',  cercc  , Henne' (aber  cymr.  ysgrech  f.  , Schrei*  aus  ags.  *scr€Bc  , Geschrei*;  mir.  screch , Schrei'  aus  anord.  skrcekr);  abret.  corcid,  nbret.  kerc'heizj  cymr.  crychydd ,Reiher',  ir.  corr  (^kork-so-)  , Kranich* ;
apr.  kerko  f.  ,Taucher  (Vogel)',  lett.  kbrcu,  kkrt  , gackern,  rauschen,  Lärm machen*,  lit.  karkiü,  karkti  , schnarren,  krächzen,  gackern*,  lit.  kirkiil, kirkti  »kreischen  (von  der  Bruthenne)' ;  lit.  krekinuos,  -intis  »brünstig  sein (vom  Schwein)*,  lett.  krecet  »heiser  werden' ;  apr.  kracto  (lies  kraccd) »Schwarzspecht',  lit.  kräke  ds.»  lit.  kr{i)okiüj  kr(i)okti  »röcheln,  grunzen* (:  lat.  cröciö  usw.)»  kr{i)oklys  »Wasserfall',  lett.  kräcu,  kräkt  ,krächzen, schnarchen,  röcheln,  tosen';  lit.  kurkiü,  kurkti  »quarren',  lett.  kürcu,  kürkt »quarren'  (:  Siksl.  kr^kngt^;  ablautend  mit  lit.  kvärkti?)]  vgl.  Mühlenbach- Endzelin  Lett.-D.  Wh  H  296,  270»  322;
aksl.  kr^kn2ti  »krächzen*  (usw.) ;  russ.-ksl.  kreceH  »Zikade*,  russ.  krek »Aufstöhnen*,  kreöet  »Jagdfalke*,  serb.  kreka  »Geschrei  der  Hühner  oder Frösche*  (usw.)»  öech.  Skrek  »Geschrei*»  osorb.  Skrekava  »Eichelhäher*; russ.  krochdh  »Tauchergans'»  bulg.  krökon  »Rabe*»  serb.  krocem,  krhkati »krächzen*  (usw.);  russ.-ksl.  (usw.)  kracu,  krakati  ds.]  dazu  slovz.  krek (*krak^)  m.  »Rabe*.
Nasaliert:  ags.  hringan  »tönen»  rasseln»  klappern*»  engl,  to  ring  »läuten, klingen'»    anord.  hrang   n.  »Lärm'»    hringia    »läuten*,   lit.  krankiü^    kraükti
569
^krächzen,  röclielii',  krank§(Siü,  kraüksti  ds.,  russ.  krjdkath  ,krachen,  ächzen, schnarren,  krächzen';  toch.  B  krafiko  Hahn;  ai.  kruid,  krunca-,  kräunca m.  , Brachvogel*.
Mit  anl.  k-:  ai.  iäri-  f.  ,ein  Vogel*,  särikä  ,die  indische  Elster*;  arm. sareak  ,Star' ;  lit.  ädrka,  apr.  sar/ce ', Elster*,  russ.  soröka,  öech.  straka^ serh.  sräka  , Elster* ;  daneben  aksl.  svraka^  serb.  svräka  ds.,  s.  unten.
Mit  anlaut.  ku-:  alb.  sorre  (*kuerna)  ,Krähe*  (Jokl,  Mel.  Pedersen  146);
aksl.  soraka,  serb.  svräka  , Elster*.
-   B.  Auf  -g-:
Ai.  kharjati  , knarrt*,  khargdlä  ,ein  bestimmter  Nachtvogel  (Eule?)*;
gr.  y,Qd)^ü)  , krächze*,  x^a^w,  sy.Qayov,  xiKQäya  ,krächzen  (vom  Raben), schreien' ;  7(.aQayi)g '  6  iqaxög  xpöcpog  olov  Ttgiövcov  Hes. ;
anord.  hrökr,  ags.  hröc,  ahd.  hruoh  , Krähe*;  ndd.  harken,  dän.  harke ,sich  räuspern*,  Schweiz,  harchlen  , röcheln*,  anord.  hark,  skark  ,Lärm*, herkir,  skerkir  , Feuer*  (,*knisternd'),  anord.  harka  ,lärmen*,  ndd.  harken , scharren,  kratzen*,  harke  , Rechen*,  nhd.
===== NR=229 =====
  Lw.  Harke  ^  zu  ai.  kharju-  m. (unbelegt)  ,das  Jucken,  Kratzen',  khj-gala-  m.  ,Krücke'(?);
ahd.  rachisön  ,sich  räuspern',  ags.  hraca  m.,  hracu  f.  , Kehle*,  ahd.  rahho , Rachen*,  ags.  hrceca  m.  , das  Räuspern;  Speichel*,  hrcecan  ,sich  räuspern, spucken*,  anord.  hraka  m.  , Speichel';  anord.  skrcekr  m.  , Schrei'  (^skreki-)^ skrcekja,  skrcekta  , schreien*,  skrgk  n.  PI.  ,Lüge*,  skrqkva  , erdichten,  erlügen';
lit.  kregidl  , Schwalbe',  kregUi  ,grunzen*,  krogiü  , röchle,  grunze*.
3.  Labialerweiterungen:
A.  Mit  -p-:  Ai.  kfpate,  Aor.  akrapista  ,jammern';  krcchrd-  , schlimm'; n.  ,Not',  mind.  aus  *kxpsra- ;
npers.  särfäk  , Schall*,  surf  (iran.  *bdrdfa-)  , Husten* ;
lat.  crepö,  -äs  und  -is,  -äre  ,knattern,  knistern,  krachen*,  crepundia,  -örum , Klappern  als  Kinderspielzeug,  Kastagnetten'  (nach  M.  Leumann,  Gnomon 9,  240,  vielmehr  etruskisch);  EM'  268;
anord.  hrafn  ,Rabe*,  urnord.  HrabnaR,  ags.  hrcefn  ,Rabe*,  ahd.  hrahan, hram  ,Rabe*  (mhd.  auch  rappe),  as.  naht-ram  , Nachteule* ;
Mit  S-:  anord.  skrafa  , schwatzen',  skraf  (und  skrap  s.  unten)  n.  , Ge- schwätz*; anord.  skarfr  , Seerabe*,  ags.  skrcef  ds.,  ahd.  scarha,  scarva  f., scarbo  m.  ds.,  nhd.  Scharbe]   bret.  scrav  , Meervogel'  ist  germ.  Lw. ;
lett.  krepet,  krepet  , schmutzig  werden*,  krepdt  ,zähen  Schleim  aus- werfen* (aus  ,*räuspern*),  lit.  skreplenti  ds.,  lett.  kr  epalas  PI.,  lit.  skrepliaX PI.  , Schleimauswurf*,  aksl.  kropljq,  kropiti  ,bespritzen,  berprengen*  usw., russ.  kropotdt'b  ,brummen,  mürrisch  sein,  sich  sorgen*  usw.
570
Mit  -b-:  anord.  skrap  ,das  Rascheln,  Geschwätz*,  skrapa  , rascheln schwätzen' ;  lit.  skrebeti  , rascheln',  aksl.  skroboU  , Geräusch'.  Nasaliert  gr Y.qEiißala  ,Kastagnetten^
IL  i- Basis  (s)(k)erei-:
Air.  scret  f.,  nir.  scread  , Schrei'  aus  *skri-zd(h)ä',  vgl.  Persson  Beitr.  I  348-
mit  S-:  bret.  screo  (*skriuä)  , kreischender  Meervogel';
ahd.  as.  scrlan  , schreien',  ahd.  screi  n.  Schrei',  ndd.  schrewen,  ndl.  sclire&U" wen  ,schreien'  (*skraiwian),  wfläm.  schreemen,  engl,  scream  ds.  (*skraimian)-l
ohne  S-:  anord.  hreimr  , Geschrei',  anord.  hrlna  , schreien*  (vüm  Schweine)» vgl.  lett.   krina  ,Sau'    (ebenso   ir.  cräin   ds.  :  lat.    oröcio)   und   piem.   crin, (ligur.  ?)  , Schwein'.
Gutturalerweiterungen:
A.  Mit  -k- :  gr.  kqUe  ,(das  Joch)  knarrte,  kreischte* ;  lit.  kryk^ciü,  krykStil ,kreischen',  krikseti  , quaken* ;
aksl.  krikz  , Geschrei',  kricati  , schreien*;
anor
===== NR=230 =====
d.  hegri,  ags.  hrägra,  ahd.  heigaro  und  (h)reigaro,  mhd.  heiger  und reiger,  nhd,  Reiher  (*kroikro-,  *krikro-),  z.  T.  mit  diss.  Schwunde  des ersten  r;
cymr.  cryg  , heiser*,  fem.  creg,  davon  creg-yr  ,Reiher';
eine  verschiedene  Lautnachahmung  ist  bulg.  cirkam  , zwitschere,  zirpe; schreie,  spritze'  (usw.  s.  Berneker  132);
B.  Mit  -g-:  gr.  y.Qiyi^  ,das  Schwirren;  Knirschen  (der  Zähne)*,  x^tyij* ?5  yXav§  Hes.,  x^t^w,  -ngl^aL,  y.k%qlya.  , kreischen,  knurren*,  böot.  y-gidöe^v ((5(5  =  j/)   ^ysXäv^ ;
cymr.  cre  (*kr{ga),  dychre  (^dl-eks-krigä)  , Geschrei*;  abgeleitet  cre-ydä^ cre-yr  , Reiher' ;
anord.  hrzka  , knirschen*^,  lirikta  , kreischen';
mit  S-:  anord.  sAirlÄia  , Vogelschrei',  als  Verbum  ^zwitschern',  ags.  5cnc , Würger',  norw.  skrlka,  skreik  ,schreien',  as.  skrikön  ds.,  d^n.  skröekr  ,Schrei';
späte  Neuschöpfung:  nhd.  Krickente,  schwed.  krickand,  krikka  ds.,  ndl. kriek,  krekel , Grille,  Heimchen',  frz.  criquet  ds.,  ndl.  kricken,  kreken  ,Zirpen (von  der  GrilleV,  mengl.  creken  ,knarren',  engl,  creak  ds.,  frz.  ci^iquer  ds.;
mit  S-:  aksl.  skr^gati  (d.  i.  skrhg-)  ,knirschen',  skr^zht^  (d.  i.  skr^-) , Geknirsche'.
IIL  u-Basis  {s)k{o)reu--j  {s)k{o)raU'i •  1.  Lat.  corvus  (s.  oben  S.  567);  mir.  crü  ,Rabe'  {*krouos)]  ndd.  schrauen, schraulen,    norw.  skryla^  ryla    ,schreien',    norw.    dial.    sÄ;r2/ma    ,klappern, Geräusch  machen,  hell  klingen;  husten';  anord.  skraumi  , Schreier,  Häns- wurst'; nordfries.  skrummel  , Getöse,  Geräusch,  Gerücht',  nhd.  schrummeln
p
571
^donnern',    anord.    skrum   , Geschwätz;   lit.   Jcriunü,    -eti  , husten,   stöhnen'* vielleicht  auch  toch.  B  keru  ,TrommeP.
2.  Dentalerweiterungen: Mit  -d-:
Anord.  hrjöta  , brüllen,  schnarchen,  brummen',  ags.  hnitan  , schnarchen, schnauben',  ahd.  rüzan,  rüzön  , rasseln,  schnarchen,  summen';  vgl,  ags. hrot  m.  , dicke  Flüssigkeit,  Schleim',  usw.  unten  S.  537 ;
mnd.  schrüten  , schnarchen,  schnaufen,  prusten',  wfäl.  Schrute  ,Truthenne', schwed.  ski^yta  ,prahlen',  dial.  , schnarchen',  norw.  dial.  skryta  , schnauben, prusten',  skrota  (*skrutön)  , prahlen'  (vielleicht  auch  anord.  skraut  n. ,Pracht,  Schmuck',  skreyta  , schmücken',  wenn  eigentlich  ,prahlen',  vgl. norw.  skreyta  ,schmücken,  loben,  prahlen',  reyta  ds.).
Mit  idg.  -t- :  anord.  hrydja  f.  , Spucknapf',  isl.  hrodi  , Speichel',  norw. dial.  ryda,  skryda  f.  , Schleim  im  Halse'.
3.  Gutturalerweiterungen:
Mit  -k-:  lit.  krauklys  , Krähe',  kraukiü,  kraükti  ,krächzen',  ablaut. kriük-iii,  -ti  ,grunzen',  krüke  , Gegrunze';  lett.  kraüklis  m.  ,Rabe',  kraükis , Saatkrähe',  kraukät  ,husten,  Schleim  auswerfen  (vom  Vieh)';  kraüka  f. , Schleimauswurf ' ;
aksl.  kruk^  ,Rabe'  (usw.);
isl.  hrygla  , Rasseln  in  der  Kehle',  mhd.  ril(c)h
```


## [2026-09-06T16:16:14.603Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"schwarz\" POK_02.txt | sed -n '1,200p' | grep -in \"kers\\|kr̥ṣṇ\\|krsna\\|kf̄sn\\|kern\" ; echo \"---- grep kers\"; grep -n \"kers-\\|kfsn\\|krsn\\|kfsnd\\|karsna\" POK_02.txt | head -40",
 "description": "Search Pokorny for kers black"
}
```


### [2026-09-06T16:16:14.661Z] TOOL RESULT

```
11:3756:kers-    und    wohl   auch   bloßes   ker-    in  Worten   für   Farben,    bes.    dunkle, schmutzige;  krs-no-  ^schwarz^;  vgl.  auch  4.  kel-  und  6.  ker-,
12:3757:Ai.  kj-piä-  , schwarz*  =  apr.  kirsnan  ds.,  FIN  Kirsnappe  =  abg.  Sr^n^, russ.  cerem,  skr.  crn  usw.  , schwarz'  (*chrxm,  *chrsm) ;  ohne  -wo-Formans lit.  kersas  , schwarz  und  weiß  gefleckt',  kerse  , bunte  Kuh',  kerHs  ,schwarz- bunter  Ochse',  kersulis  , Ringeltaube' ;  karsis  f.  , Brassen,  Blei  (Fisch)*, Icirslys  m.  ,Asche';    die  Intonation  von  kersas  paßt  aber   nicht  zum  Ai.;
---- grep kers
3160:4.  kel-  und  käl-  in  den  Worten  für  helle  und  dunkle  Flecken,  graue  und  schwärz- liche Farbentöne;  kel-zno-  ,Fleck';  vgl.  auch  3.  ker-  und  1.  kers-.
3588:6.  ker-  und  ker-,  Farbwurzel  für  dunkle,  schmutzige  und  graue  Farbentöne ; oft  mit  -i   und  -u   erweitert;   kor-ko-  ,Kot,   Sumpf,   ker-no-   ,Eis, Schnee',  kor-men-  , Hermelin,  Wiesel';  s.  die  Erweiterungen  kerb(h)- und  kers-. Ai.  karata-  ,dunkelrot'(?),  kuruiigd-,  kuluiigd-  m. , Antilope',  kirmira-  ,bunt', kdrisa-  n.  , Auswurf,  Dünger',  kardama-  m.  , Schlamm,  Schmutz,  Dünger'; kalka-    m.    ,Kot,    Dreck',    karka-    ,weiß'   (:  mir.    corcach)-    npers.    cardeh ,schwärzlich',  kari,  karah , Schmutz',  pehl.  karic  ,Mist';  gr.  ytögvl^a , Schnupfen, Rotz',    ytOQvvaL '   ^v^ai    Hes.,    y,aQV(j,6v '   fieXav    Hes.,    y,Qovi^(xi '  ^v^at   Hes. ; über  lat.  carbö  s.  oben  unter  3.  ker- ; mir.  corcach  f.  , Sumpf  (:  ai.  kalka-,  karka-,  s.  oben); ahd.  horo.  Gen.  horaweSj  mhd.  hör,  hurwe  ,Kot,  Schmutz'  (*k2'-U')]  ags. horh.  Gen.  horwes,  ahd.  horg  ,schmutzig'  {*kr-k-u-o) ;   aisl.  horr  ra.  ,Nasen- schleim,    Schmutz';   ags.    hrot   m.    ,Rotz',   ahd.    hroz    ds.,    asächs.    hrottag ,rotzig';  ahd.  ruoz,  rouz,  mhd.  7'uoz,  ruost,  asächs.  hrot  ,Ruß';   ags.  hrum m.  ,Ruß',  asächs.  hrum,  mhd.  PN  Rum-olt-,
3601:Ai.  siras-  n.  (ved.  nur  Nom.  Akk.)  ,Kopf,  Spitze',  av.  sarah-  n.  ,Kopf'  (in der  2,  Silbe  nicht  genau  =  gr.  xeqag  aus  kerd-s  von  der  schweren  Basis; die  Red. -Stufe  der  ersten  Silbe,  statt  *saras-,  ist  erst  ind.   oder  urarisch   l aus  dem  Vorläufer  von  ai.  Gen.  slr§ndh  usw.  verschleppt).  Gen.  ai.  slrsndh, Abi.  strsatdh  (*kfsn-tos  :  gr.  -Kgäarog) ;
3615:vom  -(e)7i-St.  ker(e)n-:7igdvog  ,Helm'  (*Ä:fwo-s);  y.dgvog'  .  .  .  ßdoY^niay ftgößarov  Hes.;  -Kegvai,  yiegva  PL  ,die  beiden  Hervorragungen  an  den Knochenfortsätzen  der  Rückenwirbel'  (^kern-  oder  *kers-Ti)]  -Kgayycby ,Krabbe'  (vgl.  oben  ai.  sridga-)]  unklar  ist  die  Bildung  von  y,Egdfj,ßv^,  -vY.og , Hirschkäfer';  xdgaßog  m.  , Meerkrebs;  Käferart;  Art  Schiff'  (>  lat.  carähus ds.),  vielleicht  mit  maked.  (?)  Ableitung  (gr.  *-q)og)  zu  -mgig  , Seekrebs', s.  oben;  aber  alles  unsicher.
3620:lat.  cerebrum  ,Hirn'  (*ker9S-ro-7n,  vgl.  gr.  xa^rfpa);  cerma?  ,Nacken' (*cer5-mc-) ;  cernuus,  cernulus  , Gaukler,  der  Purzelbäume  macht,  sich  köpf, über  überschlägt'  (*kers-nouos ;  wenn  nicht  eher  Lw.  aus  der  Sprache  der gr.  Jongleure,  vgl.  yisgavi^cci),  cräbrö  ,Hornis'  (s.  unten).  Vom  (e)n-St.: cornü  ,Horn'  (der  u-St.  vielleicht  wie  gall.  Tidgvv^  ,Trompete'  durch  Ver- quickung des  n-  und  w-St.);  vgl.  auch  illyr.^ON  Tqlköqvlov  (Moesia),  PN Cornulnus  usw.  (Krähe  IF.  58,  222  f.)  aus  *Ärn-;
3646:aisl.  hirsi  (mhd.  Lw.)  m.,  ahd.   hirso  (*kers-lon-)^  hirsi  , Hirse';
3671:Die  Wz.  kerb-  sucht  Liden  Stud.  50  f.  in  air.  corbaim  , besudle,  beflecke' und  lit.  kirba  (>  lett.  Uirba)  , Sumpf,  Morast'  und  betrachtet  Herb-  als Erweiterung  der  Farbwz.  ker-  (s,  S.  583  kers-);  Mühlenbach-Endzelin  II  383.
3756:kers-    und    wohl   auch   bloßes   ker-    in  Worten   für   Farben,    bes.    dunkle, schmutzige;  krs-no-  ^schwarz^;  vgl.  auch  4.  kel-  und  6.  ker-,
3767:2.  kers-  jlaufen';  krso-s  , Wagen'.
```


## [2026-09-06T16:16:25.298Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=3570 && NR<=3600' POK_02.txt | grep -n \"^5[0-9][0-9]$\\|^ *5[0-9][0-9] *$\" ; echo \"--- context around 3588 ---\"; sed -n '3580,3600p' POK_02.txt",
 "description": "Locate page numbers around ker- color root"
}
```


### [2026-09-06T16:16:26.955Z] TOOL RESULT

```
13:573
--- context around 3588 ---
Gr.  ngdvog  m.  f.  =  lat.  cornus  (^k^nos)  .Kornelkirschbaum'.  -Agdyoy =■■  lat.  cornum  .Kornelkirsche',  lit.  *kirnas  als  Grundlage  von  Kirnis  ,deus cerasorum';  dazu  wahrscheinlich  gr.  yiigaaog  ,Kirschbaum'  (daraus  lat. cerasus\  vielleicht  thrakisch-phryg.  Wort.
Trotz  lautlicher  Übereinstimmung  bleiben  der  Bedeutung  wegen  fern: lit.  kirna  f.  .Strauchband  aus  Weiden',  kirnis  , Sumpf,  apr.  kirno  f. , Strauch',
573
ablaut.  lit.  keras  ,hoher,  verwitterter  Baumstumpf;  Staude',  kereti  ,in  die Äste  schießen',  lett.  c^rs  ,Strauch,  knorrige  BaumwurzeP,  apr.  ker-berse ,Wirsenholz'  (etwa  ,Strauchbirke'),  mit  Formans  -ba,  lit.  klrba  (daraus lett.  Uirba)  ,Sumpf,  Morast';  russ.-ksl.  k^rjh,  russ.  korh  ,Wurzel',  cech.  ker ^Strauch',  o-stufig  aksl.  (usw.)  korem,  Gen.  -ene  (en-St.)  ,Wurzel';  samt russ.  deren,  cerenök  ,Heft,  Stiel,  Griff  eines  Messers;  Pfropfreis'  usw. (s.  Berneker  146 f.);  vielleicht  zu  {s)ker-  ,schneiden'. WP.  I  411  f.,  WH.  I  221f.,  276  f.
^.  (leer-?)  kor-  ,hangen,  hängen'.
Lit.  kariüj  kdrti  ,mit  einem  Strick  erhängen',  lett.  karu,  kärt  , hängen', lit.  pakara  , Kleiderständer,  Pflock  zum  Kleideraufhängen',  lett.  pakars , Haken  zum  Aufhängen',  apr.  paccaris  ,Riemen',  lit.  pakore  , Galgen' 5 vielleicht  auch  lit.  prä-kartas , Krippe',  apr.  pracartis  ,Trog',  wenn  ursprüngl. ,vorgehängter  Futtersack' ;
dazu  vielleicht  als  Erweiterung  *krem(d)-  in  gr.  yiQSfidwvfxi  , hänge', älter  y,Ql^vr]^L  ds.  (neben  xoi^fivr]^ij  s.  Specht  KZ  59,  97),  ycQSfiafiai ,hange',  y.Qefj,a-9-Qa  ,Hängematte',  schwundstufig  xgrjfj^vög  ,Abhang'.
WP.  I  412.
6.  ker-  und  ker-,  Farbwurzel  für  dunkle,  schmutzige  und  graue  Farbentöne ; oft  mit  -i   und  -u   erweitert;   kor-ko-  ,Kot,   Sumpf,   ker-no-   ,Eis, Schnee',  kor-men-  , Hermelin,  Wiesel';  s.  die  Erweiterungen  kerb(h)- und  kers-. Ai.  karata-  ,dunkelrot'(?),  kuruiigd-,  kuluiigd-  m. , Antilope',  kirmira-  ,bunt', kdrisa-  n.  , Auswurf,  Dünger',  kardama-  m.  , Schlamm,  Schmutz,  Dünger'; kalka-    m.    ,Kot,    Dreck',    karka-    ,weiß'   (:  mir.    corcach)-    npers.    cardeh ,schwärzlich',  kari,  karah , Schmutz',  pehl.  karic  ,Mist';  gr.  ytögvl^a , Schnupfen, Rotz',    ytOQvvaL '   ^v^ai    Hes.,    y,aQV(j,6v '   fieXav    Hes.,    y,Qovi^(xi '  ^v^at   Hes. ; über  lat.  carbö  s.  oben  unter  3.  ker- ; mir.  corcach  f.  , Sumpf  (:  ai.  kalka-,  karka-,  s.  oben); ahd.  horo.  Gen.  horaweSj  mhd.  hör,  hurwe  ,Kot,  Schmutz'  (*k2'-U')]  ags. horh.  Gen.  horwes,  ahd.  horg  ,schmutzig'  {*kr-k-u-o) ;   aisl.  horr  ra.  ,Nasen- schleim,    Schmutz';   ags.    hrot   m.    ,Rotz',   ahd.    hroz    ds.,    asächs.    hrottag ,rotzig';  ahd.  ruoz,  rouz,  mhd.  7'uoz,  ruost,  asächs.  hrot  ,Ruß';   ags.  hrum m.  ,Ruß',  asächs.  hrum,  mhd.  PN  Rum-olt-,
mit  Palatal  im  Anlaut:
arm.  sarn.  Gen.  sarin  ,Eis',  sarnum  ,gefriere';
ven.-illyr.  PN  Carmö  (Steiermark),  rätoroman.  carmün  , Wiesel';  s.  unten kor-men- :
574  f
alb.  thjer-me  ,grau',  per-thjerm  ,blaßblau'  (*ker-uo-  mit  sekundärem  -meV i  surm'6  , aschfarben'  (*7m*-wo-);  s.  Jokl  M61.  Pedersen  153  ff. ;
aisl.  hjarn  n.  .gefrorener  Schnee'  (:  arm.  safn,  slav.  *serm)'^  ahd.  horl nunc,  nhd.  Hornung  , Februar';  ahd.  harmo  m.  , Hermelin'  (:  ven.-illyj.^ carmo) ;
lit.  ,sif ras  , grau,   blaugrau'  {*kf-uo-s),   sirmas  ds.   {*7cr-mo's),   lett.  sirmt ,grau'   (vgl.  ai.  syä-md-   , schwarz,    dunkel'   neben   iyä-vd-    ds.);    lit.   §irvis Jiase';  dazu  lit.  sarmä  f.  ,Reif',  lett.  sarma,  serma  ds.,  lit.  sarmuo,  Wermut , Hermelin'  (:  ahd.  harmo,   ven.-illjr.   carmö)]    h-armnonys   m.  , Wiesel',  mit' Ablaut  ostlit.  Hrmuonelis  ds.,  lett.  sermulis  m.  , Hermelin';
urslav.  *serm  in  russ.-ksl.  srem  jfiOLv.iXog' ,  aruss.  serenyj  ,weiß'  (von Pferden)  und  als  m.  sloven.  sren,  srenj  ,Raureif,  gefrorene  Schneerinde' russ.  seren  ,gefrorener  Schnee',  poln.  szron  (älter  srzon)  ,Reif'  (:  aisl.  hjarn)*
lit.  s er Jcsnas  (neben  serhstas)  , weißgrau,  schimmlig',  serknas  m.  ,Reif* ablaut.  Hrhsnas  ,Reif'  und  sirshija  Hrsnyti  ,sich  mit  Reif  bedecken';  lett. serns,  serjcsns  m.,  auch  sersni  m.  Plur.,  sersna  f.  ,Reif'  und  serstu  laiks ,Zeit,  da  der  Schnee  trägt'.
WP.  I  409,  428  f.,  Trautmann  300,  303,  Specht  Idg.  Dekl.  118  f.,  179, 199,  W.  Schulze  Kl.  Sehr.  113  u.  Anm.  1.
5.  ker-  , springen,  drehen',  s.  unter  (s)ker-.
I.  ker-y  kero-  :  krä-,  ker  ei-,  ker  eu-  ,das  Oberste  am  Körper  :  Kopf;  Hern (und  gehörnte  Tiere);  Gipfel';  sowohl  die  leichte  wie  die  schwere Basis  oft  durch  -{e)n-,  -s-,  -s-(e)-n  erweitert,  so  in  ker-n-,  ker-s-, kero-s- :  krä-s-,  kr-s(-e)-n-,  usw.
```


## [2026-09-06T16:16:39.112Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3745,3775p' POK_02.txt",
 "description": "Print Pokorny kers- entry with page markers"
}
```


### [2026-09-06T16:16:39.157Z] TOOL RESULT

```
kerno-  , Kinnbacken' ;  nur  kelt.  und  slav. ;  vgl.  2.  her-.
Cymr.  cern  , Kinnbacken^,  bret.  kern  , Mühltrichter,  Scheitel,  Tonsur', mir.  cern  ,Ecke,  Winkel'  (es  liegt  die  Vorstellung  des  Knicks  am  Kinn- backen vor);
slav.  *cerm  in:  abg.  crenovhnaja  ^^ivlai^  r.-ksl.  crSnovtm  {zuh^),  crenovithct ,^vXr]^  ,dens  molaris',  slovak.  ^ren  , Kinnbacken'  usw.
Nach  Büga  RFV.  67,  234  zu  lett.  c^rwo-Ä;(s)Zzs  ^Backenzahn',  ai.  carvati ,kauen'.
WP.  I  427,  Trautmann  129,  Specht  Idg.  Dekl.  141,  169.
ke-ro-  Farbbezeichnung?
Ai.  särd-  ,bunt,  scheckig',  dessen  -ra-  als  formantisch  erwiesen  wird durch  die  av.  Kompositionsform  *iä-(i)i-  in  säi-mu^ay-  EN  ,der  ungleich- mäßig gefärbte  Eselinnen  hat';
gr.  nrjQvlog  ,der  blaue  ^Eisvogel'  (Deminutivformans  -vXog).
"^ke-ro-  vielleicht  als  *ke[i']-ro-  zu  2.  Icei-  in  , Farbbezeichnungen' ?
WP.  I  420,  WH.  I  133.
583
kers-    und    wohl   auch   bloßes   ker-    in  Worten   für   Farben,    bes.    dunkle, schmutzige;  krs-no-  ^schwarz^;  vgl.  auch  4.  kel-  und  6.  ker-,
Ai.  kj-piä-  , schwarz*  =  apr.  kirsnan  ds.,  FIN  Kirsnappe  =  abg.  Sr^n^, russ.  cerem,  skr.  crn  usw.  , schwarz'  (*chrxm,  *chrsm) ;  ohne  -wo-Formans lit.  kersas  , schwarz  und  weiß  gefleckt',  kerse  , bunte  Kuh',  kerHs  ,schwarz- bunter  Ochse',  kersulis  , Ringeltaube' ;  karsis  f.  , Brassen,  Blei  (Fisch)*, Icirslys  m.  ,Asche';    die  Intonation  von  kersas  paßt  aber   nicht  zum  Ai.;
schwed.  norw.  harr  , Asche'  (*harzu-)]  ags.  Jieard-hara,  heardra-  m., nhd.  holL  harder,  herder  , Meer- Asche'.
WP.  I  428 f.,  Trautmann  118,  134 f.
/.  ker(s)-  , Borste,  steifes  Haar;  starren,  rauh  und  kratzig  sein'.
Ai.  *sala  in  kapucchala-  n.  ,Haar  am  Hinterhaupt';
mir.  carrach  ,schorfig,  räudig,  steinigt;  anders  oben  S.  532;
ahd.  Jiursti  ,cristas',  norw.  herren  , steif,  hart',  aisl.  herstr  ,rauh,  barsch^, mhd.  hersten  ^erstarren' ;  vielleicht  ahd.  as.  aisl.  här,  ags.  hcer  ,Haar'  von einer  s-losen  kürzeren  Wurzelf.  (Dehnstufe) ;
lit.  §erys  , Borste',  Seriüos,  sertis  , haaren,  Haare  lassen',  Hurkstüs,  siurg- zdüs  ,rauli';  ablaut.  ostlit.  §er§as  , Schauer';  lett.  sari  , Borsten';
slav.  *shrsth  {=  ahd.  hurst)  in  russ.-ksl.  shrsth  f.  , Wolle',  sloven.  srst , Tierhaar',  russ.  sersth  , Wolle',  ablaut.  russ.  söro§  m.  , rauhe  Oberfläche', abg.  v^sor^  ,rauh' ;  slav.  *shrch^  in  sloven.  srh  m.  , Schauer',  russ.-ksl. srhch^k^  ,TQaxvs\  sloven.  srhsk  , struppig'.
WP.  I  427,  Trautmann  305.
2.  kers-  jlaufen';  krso-s  , Wagen'.
Für  palatales  %  spricht  adgaai '  äfia^ac  Hes.,  das  wie  lat.  sarräcum,  serracum (ital.  -rr-  aus  -rs-)  ,ein  ausländischer  Wagen'  ein  illyr.  *sarsa  =  idg.  *Äfsä zur  Quelle  haben  könnte;
gr.  STti-novQog  ,zu  Hilfe  eilend'  (*korsos)]
lat.  curröj  -ere  , laufen'  (*krsö),  cursus  ,Lauf',  currus  , Wagen',  equirria »Wagenrennen'  {*equi-curria,  woraus  assimilatorisch  *equi-quinna  und haplologisch  equirria) ;
gall.  carros,  latinisiert  carrus  , Karren,  Wagen',  air.  mcymr.  carr,  bret. kai^r  ,biga,  vihiculum'  (*krsos)]  vgl.  mcymr.  carrawc  f.,  ncymr.  carrog , Sturzbach'  (*karsäkä  ,die  Laufende'?),  anders  oben  S.  532.
mhd.  hurren  ,sich  rasch  bewegen' ;  unsicher  ahd.  hros,  -ses,  aisl.  as.  hross, ags.  hors  , Pferd,  Roß'  (^himssa-),  and.  hers  ds.  (*herssa-),  da  das  -ss-  bei einer  auf  -s  ausl.  Wz.  höchstens  als  Konsonantenschärfung  in  einem  Kurz-
584  9
namen  verständlich  wre;  daher  eher  zu   einer   Dentalerweiterung   (:  ai. Urdati  ,hüpft,  springt')  der  nicht  palatalen  Wz.  {s)Jcer-  ,springen' ;
arm.  JcarJt  , Wagen'  ist  wohl  Lw.  aus  dem  Galatischen.
```


## [2026-09-06T16:16:46.654Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"carbö\\|carbo\\b\" POK_02.txt | head -20; echo \"=== 3. ker-\"; grep -n \"^3\\.  ker\\|3\\.  ker(3)-\\|ker(3)-\\|kerd-\\|brennen,  glühen\\|Hitze\" POK_02.txt | sed -n '1,30p'",
 "description": "Find Pokorny ker- burn entry"
}
```


### [2026-09-06T16:16:46.727Z] TOOL RESULT

```
3528:Mit  S-:  anord.  skrafa  , schwatzen',  skraf  (und  skrap  s.  unten)  n.  , Ge- schwätz*; anord.  skarfr  , Seerabe*,  ags.  skrcef  ds.,  ahd.  scarha,  scarva  f., scarbo  m.  ds.,  nhd.  Scharbe]   bret.  scrav  , Meervogel'  ist  germ.  Lw. ;
3588:6.  ker-  und  ker-,  Farbwurzel  für  dunkle,  schmutzige  und  graue  Farbentöne ; oft  mit  -i   und  -u   erweitert;   kor-ko-  ,Kot,   Sumpf,   ker-no-   ,Eis, Schnee',  kor-men-  , Hermelin,  Wiesel';  s.  die  Erweiterungen  kerb(h)- und  kers-. Ai.  karata-  ,dunkelrot'(?),  kuruiigd-,  kuluiigd-  m. , Antilope',  kirmira-  ,bunt', kdrisa-  n.  , Auswurf,  Dünger',  kardama-  m.  , Schlamm,  Schmutz,  Dünger'; kalka-    m.    ,Kot,    Dreck',    karka-    ,weiß'   (:  mir.    corcach)-    npers.    cardeh ,schwärzlich',  kari,  karah , Schmutz',  pehl.  karic  ,Mist';  gr.  ytögvl^a , Schnupfen, Rotz',    ytOQvvaL '   ^v^ai    Hes.,    y,aQV(j,6v '   fieXav    Hes.,    y,Qovi^(xi '  ^v^at   Hes. ; über  lat.  carbö  s.  oben  unter  3.  ker- ; mir.  corcach  f.  , Sumpf  (:  ai.  kalka-,  karka-,  s.  oben); ahd.  horo.  Gen.  horaweSj  mhd.  hör,  hurwe  ,Kot,  Schmutz'  (*k2'-U')]  ags. horh.  Gen.  horwes,  ahd.  horg  ,schmutzig'  {*kr-k-u-o) ;   aisl.  horr  ra.  ,Nasen- schleim,    Schmutz';   ags.    hrot   m.    ,Rotz',   ahd.    hroz    ds.,    asächs.    hrottag ,rotzig';  ahd.  ruoz,  rouz,  mhd.  7'uoz,  ruost,  asächs.  hrot  ,Ruß';   ags.  hrum m.  ,Ruß',  asächs.  hrum,  mhd.  PN  Rum-olt-,
=== 3. ker-
1271:'^ghlö-  (wie  in  gr.  xkwQÖg)  tritt  auf  in  ags.  glöm  , Zwielicht,  Dämmerun»* (doch  ist  ö  vor  m  mehrdeutig),  as.  glöian,  ahd.  gluoen  , brennen,  glühen glänzen',  aisl.  glöd  ,Glut,  glühende  Kohle',  ags.  gläd  f.  ,Glut,  Flamme, glühende  Kohle,  Kohle',  afries.  gled  ,Glut,  Brand',  ahd.  gluot  ,Glut, glühende  Kohlen';  aisl.  -glör  n.  , Glanz'  (:  %Io}q6<;),  aisl.  glöra  , funkeln'; s.  auch  unten  S.  433  ghlöu-]  ;;
2288:g^her-    ,heiß,    warm';    Adjektiv    g^hermo-    und    g"hornio-    ,warm'    und Substantiva    g^heros-,    g^boros-  n.,    g"bormo-    n.,   g^hormiiä    f., g^horno-s,  g^hrno-s,  g^hortiiä  und  ^hr^-ns-o-s  ,Hitze,  Wärme, Glut,  Brand',  usw. Ai.   hdras-\  n.   ,Glut'   (=  gr.  d-eoog,  arm.  jer),   ghfnd-   m.  ,Glut,  Hitze' (=  lat.  fornus,   aksl.   g'>^n^),   gh^nöti   ,glüht,   leuchtet',   gkarmd-  m.   ,Glut, Hitze',  av.  gardma-  ,heiß',  n.  , Hitze,  Glut',  apers.  in  garma-pada-  Monats- name,  etwa  ,*Eintritt'  der  Hitze'  (=  lat.  formus,  dt.  luarm ;    apr.  gorme) ; arm.  jer  ,Wärme,  schönes  Wetter ;    warm',  jernum  , wärme  mich',  jerm jWarm'  (=  gr.  -S'SQixög ;  vielleicht  als  *gV:her-mn-os  Ableitung  vom  wew-St.  :) jermn  Gen.  jerman  , Fieber'  (auch  gr.  ^ig^ia   f.  ,Wärme'  ursprünglich  ein Neutrum?);
2292:auch  Germ-  in  illyr.  PN,  wie  auch  wohl  im  ursprüngl.  nordillyr.  VK^ Germani  (Pokorny  ZceltPh.  21,  103 ff.);  alb.  tosk.  2/arr  , Feuer,  Hitze' {rr  aus  rm),  gheg.  zjarm  ( :  dsQi^ög),  ngroJi  ,wärme'  (*g^hre-  wie  in  aksl gr^ti  , wärmen',  lett.  gremens  , Sodbrennen');  alb.  gatse  , brennende  Kohle*. (*g^hortiä  ?) ;
2294:air.  fo-geir  ,erwärmt,  erhitzt'  usw.,  bret.  gred  m.  _, Wärme,  Hitze;  Mut* =  mir.  grith  , Sonne,  Hitze'  (*g}ihrtu-s),  mir.  gorim,  guirim  ,erhitze,  er- wärme, brenne',  nir.  gor  , Hitze;  Brüten;  Geschwür';  cymr.  gori  ,brüten', gor  ,Brut,  Eiter',  bret.  gor  ,{iQ\i)  ardent,  furoncle';  air.  gorn  ,Feuer* (==  lat.  fornus) ;  dagegen  ist  ir.  gorm  ,blau'  Lw.  aus  cymr.  gwrm  , dunkel- (blau)'  und  dieses  samt  abr.  uurm  in  Uurm-haelon  MN  ,aux  sourcils  bruns' aus  ags.  wurma  ,Purpurfarbe'  entlehnt  (Gwynn  Hermathena  20,  63 ff.);  air. goirt  jbitter'  (,*brennend  vom  Geschmack'),  wozu  air.  gorte  {*g^hortia) ,Hunger';
2299:lit.  gäras  ,Dampf;  starkes  Verlangen',  lett.  gars  ,Dampf,  Geist,  Seele', apr.  goro  f.  ,Herd',  gorme  , Hitze',  lett.  garme  ,Wärme',  apr.  garewingi Adv.  ,brünstig',  lett.  gremens  ,Sodbrennen' ;
2304:ai.  ghramsd-h  m.  , Sonnenglut,  Sonnenschein,  Helle'  =  bret.  groez,  grouez (*guhrenso-)  , Sonnenhitze',  cymr.  gtvres  , Hitze'  (zum  w  s.  Pedersen  KG.  I 108,  das  e  durch  Einfluß  von  tes  ds.);  das  i  von  air.  gris  , Feuer',  grlsaid , feuert  an,  reizt  an'  wohl  aus  *ghTenso-,  trotz  Thurneysen  Gr.  130.
2671:ß.  käi-,  k^-  ,Hitze'.
2672:Ahd.  hei  ,dürr',  gihei  n.  , Hitze,  Dürre',  arheigetun  ,verdorrten',  got.  Dat. PI.  haizam  ,den  Fackeln'  (es-St.  *hai-iz-).
2673:Mit  -d-Erw. :  ahd.  heiz,  as.  het,  ags.  hat,  aisl.  heitr  ,heiß'  (wovon  ahd. nhd.  heizen,  ags.  hcetan,  aisl.  heita  ds.);  got.  heito  f.  , Fieber';  ahd.  hizza jHitze^,  i^hitjo)  as.  hittia,  ags.  hitt  t,  aisl.  hiti  m.  ds.
2674:Mit -t-Erw. :  lit.  kaistü,  kaitau,  kaisti  ,heiß  werden',  kaiträ  , Feuerglut', kaitrüs  , Hitze  gebend',  präkaitas  m.  , Schweiß',  lett.  käistu,  käitu,  käist ,heiß  werden,  brennen'  u.  dgl.,  übertragen  lett.  kaiiinät  , ärgern,  reizen' (kalte  , Schaden,  Leid,  Gebrechen,  Plage',  vgl.  Mühlenbach-Endzelin  II  135), apr.  ankaitltai  , Angefochtene' ;
3224:lat.  caleö,  -ere  ,warm,  heiß  sein,  glühen',  calidus  ,warm,  heiß',  calor , Wärme,  Hitze';
3304:3.  kern-,  ,bedecken,  verhüllend
3566:3.  ker{p)-  , brennen,  glühen,  heizen'.
3574:lit.  kdrstas  ,heiß',  karstis  , Hitze',  lett.  kar^sts  ,heiß',  ka'rset  ,erhitzenV1 (*Ä;or-s-);  wozu  als  ,hitzig'  auch  lit.  kerHas  ,Zorn',  kerüs,  keringas  ,zorn- voll',  kiHti  zornig  ,werden' ;  wohl  zu  ai.  kusäku-  ,brennend ;  Feuer,  Sonne' und  kasäku-  ,Feuer,  Sonne'  (beide  mind.  aus  *kTsäku-]  vgl.  arm.  xarSem ,koche,  brenne'  aus  intensivem  *ä:Ä2's-);  vgl.  Mühlenbach-Endzelin  Lett.-D. Wb.  I  375,  II  164.
3601:Ai.  siras-  n.  (ved.  nur  Nom.  Akk.)  ,Kopf,  Spitze',  av.  sarah-  n.  ,Kopf'  (in der  2,  Silbe  nicht  genau  =  gr.  xeqag  aus  kerd-s  von  der  schweren  Basis; die  Red. -Stufe  der  ersten  Silbe,  statt  *saras-,  ist  erst  ind.   oder  urarisch   l aus  dem  Vorläufer  von  ai.  Gen.  slr§ndh  usw.  verschleppt).  Gen.  ai.  slrsndh, Abi.  strsatdh  (*kfsn-tos  :  gr.  -Kgäarog) ;
3649:3.  ker-  ,Schnur,  Gewebefaden;  flechten,  knüpfen';  nur  arm.  und  griech.
3674:j.  kerd-  ,gürten';  kelt.  krd-su-,  slav.  kerd-so-  , Gürtel';  nur  kelt.  und  slav.
3679:2.  kerd-  etwa  , handwerksmäßig  geschickt,  klug  berechnend'.
3692:(Icered-:)  kerd-,  kerd-,  krd-,  kred-  ,Herz'. Arm.  sirt,  Instr.  srti-v  ,Herz'  [*kerdi-)]
3737:kerd-,    krä-    ,mischen,    durcheiüanderrühreii^    z.   T.    auch    ^kochen'    (yon\ Umrühren);  kr-to-  ^gemischt''.
5422:leto-,  leti-,  leto-,  löto-  , Brunst,  Hitze,  Zorn'.
6271:russ.  dial.  mar^  , Sonnenglut ;  Schlaff  mdrevo  , Hitze,  bei  der  die  Luft  trüb weiß  ist;  Höhenrauch,  Luftspiegelung'  (*möreuom)  u.  dgl. ;  mit  '^m'br-  klr. 'rrtryj  ,neblig,  düster,  dumpfig',  mriju,  mrity  , schimmern,  dämmern,  neblig werden';
```


## [2026-09-06T16:16:50.177Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3560,3580p' POK_02.txt",
 "description": "Print Pokorny 3. ker(ə)- burn entry"
}
```


### [2026-09-06T16:16:50.211Z] TOOL RESULT

```
isl.  hrygla  , Rasseln  in  der  Kehle',  mhd.  ril(c)heln,  nhd.  röcheln,  norw. Tugde  , Waldschnepfe';  dazu  wohl  ags.  Äro^^, Nasenschleim';
mit  Geminata  -kk- idän.  skrukke  ,glucksen',  skrokke  ,plaudern',  woneben älter  dän.  krokke  , rufen,  von  Hühnern',  mnd.  krochen  ,grunzen;  heiser schreien  (vom  Raben)'.
Mit  -k-:    ai.  krösati,   av.  xraosaiti  , kreischt,   schreit',   sa.  krösa-,   klösa- ^    m.  , Schrei,  Rufweite',  ( :  ags.  hream  ,Notruf'  aus  *hrauhma),  npers.  xurös ,Hahn';   s.  W.  Schulze  Kl.  Sehr.  166.
Mit  -g-i  gr.  y.Qavyrj,  Geschrei',  KQavyög'  dqv/.oXd'rtTov  eidog  (,Art  Specht') Hes. ;   got.  hruk  Akk.  ,das  Krähen',  hrukjan  ,krähen'.
WP.  I  413ff.,  WH.  I  275 f.,  290,  291  f.,  293,  Trautmann  128,  139f., Wissmann  Nom.  postverb.  130  f.
2.  ker-  , schneiden',  s.  unter  (s)  ker-.
3.  ker{p)-  , brennen,  glühen,  heizen'.
Ai.  küdayati  , sengt'  {*kf-d-,  d.  i.  *ker9-d-) ;  nasaliert  kundate  ,brennt' ; über  kusäku-,  kasäku-  s.  unten;
zweifelhaft  lat,  carhö,  -önis  m.  , Kohle'  (idg.  *k^r-dhö?),  von  Specht  Idg. Dekl.  266  zur  Farbwurzel  ker-  (^k;r-bhö?)  gestellt;
572  •
got.  Jiaürin.  .Kohle',  aisl.  hyrr  m,  ,Feuer'  {*}iürja',  idg.  *Kr-io-)]
ahd.  herd,  as.  herth,  ags.  heord  ,Herd' ;  ahd.  harsta  ,frixura',  gahurstit ,frixusS  mnd.  harst  ,Rost  (zum  Braten)',  ags.  hierstan  ,rösten',  hierstepanne , Bratpfanne';
lit.  kuriü,  kürii  ,heizen',  kürenti  , fortgesetzt  heizen',  kürstyti  ,schüren' lett.  kuru  (kurstu),   kurt,   frequent.   ktirstU,   kurindt  ,heizen',   aksl.    kurjq kuriti  s^  ,rauchen',    kureubje   ,Kohlenfeuer'    usw.;    halt,    kür-,    slav.  kur- müßten  hei  dieser  Deutung  Ahlautsneuhildungen   zu  *kür  aus   einer  idg.  J Red.-Stufe  o  sein;  eine  andere  Deutung  unter  {s)ker-  .schneiden';
lett.  c^ri  ,Glutsteine',  ce^ras  .Inbrunst',  ceret  ,liehen,  sehnen,  hoffen*»^ russ.  ceren  , Salzpfanne  der  Salzsiedereien',  klr.  ceren  ,Boden  des  Back- 1 und  Kochofens,  Feuerherd',  poln.  trzon  ,Herd';
lit.  kdrstas  ,heiß',  karstis  , Hitze',  lett.  kar^sts  ,heiß',  ka'rset  ,erhitzenV1 (*Ä;or-s-);  wozu  als  ,hitzig'  auch  lit.  kerHas  ,Zorn',  kerüs,  keringas  ,zorn- voll',  kiHti  zornig  ,werden' ;  wohl  zu  ai.  kusäku-  ,brennend ;  Feuer,  Sonne' und  kasäku-  ,Feuer,  Sonne'  (beide  mind.  aus  *kTsäku-]  vgl.  arm.  xarSem ,koche,  brenne'  aus  intensivem  *ä:Ä2's-);  vgl.  Mühlenbach-Endzelin  Lett.-D. Wb.  I  375,  II  164.
Eine  verwandte  Wurzelf.  krä-s-  als  , Feuerglanz,  Glut',  woraus  teils  ,rotV teils  ,leuchtend,  hell,  schön',  in  aksl.  krasa  ,venustas,  pulchritudo',  russ. krasd  , Schönheit,  Zierde,  Schmuck',  aksl.  krashn^  ,schön,  angenehm,  weiß gekleidet',  russ.  krdsnyj  ,rot,  schön',  cech.  krdsny  , schön',  alt  auch  ,licht, glänzend'  und  ,rötlich'  (usw.);  lett.  kräsus  , schön'  ist  russ.  Lw.
Ein  aus  ker-  erweitertes  *k(e)r-em-  sucht  man  in  lat.  crem��,  -äre  .ver- brennen (tr.)',  umbr.  krematra  PL  *crematra  ,Art  Gefäß  zum  Braten  des Fleisches,  Braten';
dazu  als  ,Decoct'  auch  cremor  ,der  aus  aufgeweichten  Getreidekörnern oder  sonst  aus  Pflanzen  gewonnene  Saft,  Brei' ;  ferner  gall.  ytÖQixa,  xovgfii, air.  coirm  n.,  mcymr.  cwrwf,  acorn.  corefj  coruf  ,Bier',  wozu  vielleicht ai.  karam-h{h)d-  m.  , Grütze,  Brei',  kulmäsa-  m.  .saurer  Schleim  von Früchten,  saurer  Reisschleim';  vgl.  ferner  toch.  B  kark-,  kärk-  .braten, rösten'.
WP.  I  418  f..  WH.  I  165  f..  287  f.
4.  ker-  in  Worten  für  .Kornelkirsche.  Kirsche'.
Gr.  ngdvog  m.  f.  =  lat.  cornus  (^k^nos)  .Kornelkirschbaum'.  -Agdyoy =■■  lat.  cornum  .Kornelkirsche',  lit.  *kirnas  als  Grundlage  von  Kirnis  ,deus cerasorum';  dazu  wahrscheinlich  gr.  yiigaaog  ,Kirschbaum'  (daraus  lat. cerasus\  vielleicht  thrakisch-phryg.  Wort.
```


## [2026-09-06T16:16:59.220Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ceramic\\|keramos\" AHD_watkins1985.txt | head -20; echo \"=== ker heat\"; grep -n \"^ker-\\|ker-3\\|To heat, fire\" AHD_watkins1985.txt | head -30",
 "description": "Search Watkins for ker- heat"
}
```


### [2026-09-06T16:16:59.304Z] TOOL RESULT

```
<persisted-output>
Output too large (35.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bdt4320a2.txt

Preview (first 2KB):
621:hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.]
...
</persisted-output>
```


## [2026-09-06T16:17:21.180Z] TOOL CALL #14: Bash

```json
{
 "command": "pdftoppm -f 258 -l 258 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg258 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 258"
}
```


## [2026-09-06T16:17:22.053Z] TOOL CALL #15: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1619 2>&1 | head -60",
 "description": "Fetch BQT page 1619"
}
```


### [2026-09-06T16:17:23.966Z] TOOL RESULT

```
total 11020
drwx------ 7 sfmqrb sfmqrb    4096 Sep  6 12:17 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1232 Sep  6 12:16 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb  181961 Sep  6 12:11 bqt1688_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  340758 Sep  6 12:11 bqt1709_fn2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  280452 Sep  6 12:11 bqt1709_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36354 Sep  6 12:02 c246_casaque.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13719 Sep  6 12:02 c248_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30759 Sep  6 12:02 c248_p4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2750 Sep  6 12:02 c248_persian2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3046 Sep  6 12:02 c248_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4259 Sep  6 12:13 c250_celare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7170 Sep  6 12:13 c250_kolba.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4529 Sep  6 12:13 c250_sarez.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb     724 Sep  6 12:11 drive.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4491 Sep  6 12:13 fix.py
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
-rw-rw-r-- 1 sfmqrb sfmqrb   81037 Sep  6 12:03 mk240.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80347 Sep  6 12:08 mk242.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58802 Sep  6 12:07 mk244.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p245
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:16 p249
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   30335 Sep  6 12:07 part2.py
-rw-rw-r-- 1 sfmqrb sfmqrb   38036 Sep  6 12:11 part3.py
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81026 Sep  6 12:03 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83594 Sep  6 12:03 pg239_small.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64208 Sep  6 12:04 pg247.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142780 Sep  6 12:02 pg248hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82530 Sep  6 12:05 pg249.png
-rw-rw-r-- 1 sfmqrb sfmqrb  123419 Sep  6 12:13 pg250hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89076 Sep  6 12:13 pg250.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74772 Sep  6 12:13 pg252.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68850 Sep  6 12:14 pg253.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71025 Sep  6 12:13 pg254.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55906 Sep  6 12:13 pg255.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81240 Sep  6 12:17 pg258.png
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 __pycache__
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


### [2026-09-06T16:17:31.238Z] TOOL RESULT

```
REF: BQT:1619  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 412  OCR-lang: fas

-۱۹۱۹- ۱ کرش
کرسطوس !۱ - بکر اول و نانی درهم نشته راگویند ۸
وسکون ثالث و طای حطی بواو کشیده و بین‌بی کرسی‌خالك - بنم اول وسکون‌نانی.
نفطفٌزده, بلغت‌انجیل نام باری‌تعالی‌است‌جل‌جلاله؛ . .
با اول وثانی‌مفتو علیه‌اللام را گویند کنایه ا زکر؛ خالك است که زمین باشد - و جنم
۶ وت َ سوه | اول وثانی» عاکیانی را گوبند که ازبیضه تهادن
و معنی کرسب است فی باشد وآن‌رستشی
بودکه خورند . کرسی دار مجلس طود -« کنابه
۰ از حضرت علیداللامء است .
کرسنج ۴ - بر وزن شطرنج . بمعنی از حضٌرت هوسی ۰ 3
کم همتی باشد و آن ضعف نفی است از طلب کر سیدن؟ « بفتح اول بروزن‌ترسیدن,
مراتب عالیه . بمعنی فریب دادن - و فروتنی کردن باشد ؛
کرسنه « بکر اول وثالی واسکون | و باین معتی با شین نقطه‌دار هم‌آمده استواسح
ثالك و فتح نون » چرك وریمی ر! کوبن دکه بر آنت . ْ.
روی زخم بستّه و سخت شده باشد ۴ - و بفتح کرسی رد - بفتح زای نقطه‌دار, کنایه
اول وسکون نانی وفتح ثالث ولون, نام غله‌ایست | از آفتاب عالم تاب است - و کنایه از روز هم
تیرمرنگ ۵ و طعم آن مایین ماش وعدی باشد | هن که(۱) بعربی بوم خوانند سوکنایه از کفل
آنرا مقشر کرده بگاو.دهند گاو را چاق وفربه و سرین سیم بدنان باشد .
کند و بیونانی | خوانند ؛ و باشین نقطه‌دا 8
و بیونالی ارولی خو و باشی نقطه‌دار ۹ شه - ۳ :
هم بنظرآمده است . کرسی‌شش گو کنابه از
مه ی دنیا و روزگار است باعتبار شش جهت که پیش
کر - جم اول وفتح ثانی وسین بی وزبر و بالا و چپ وراست باشد .
نقطه » چرك وریم راکوبند ‎٩‏ - وموی پیچیده وپی ۲ ۳ 0
و مجعد رانیز کفته‌اند ۷ - و در عریی بکر کرش - بذتح اول ونانی وسکون شبن
اول وسکون ثانی؛ اصل هرچیز - وبول‌وسکین | نقطه‌دار» بمعنی فریب وخدعه وچاپلوسی‌وفروتنی

() چش : و

۱ رد4 :ص ج از دباچة موّلف ی۳ و ح۱. ۴ کرت (ه.م.)* کرشغف
(و.م.) ۳ ‌ ظ . برساختهة فرقهٌ آذرکیوان ۰ ۴ کرس (ه.م.) » عوام شراز
« فرسنه > گوبند ۸« جهانگیری » ۸« رشیدی >. ۵ < کنکه « جپانگیری »<< کنا
(ص) از عبری ۴8790188 با ازآرامی 82875101882 که بنظر میرسدهردو مشق ازسانسکریت
8 (سعیاه ) باشد . این نام در فارسی ور :کشنکه ( بفتح اول ) »کشنکه ( بم‌اول).
کشنه ( نم اول ) »کشنی ( بفتح اول ) »کسنی ( بفتح اول ) »کسنکه و غیره‌آمده * فولری
11 » ۸۳۵ ۸1۵ بعد ) 1160۲ 1ز7۷ه 3۳۹ (ضش) « عقار ۹۸۵ 4

۹ < کری (ه.م.) * کرسنه (و.م.) ۰ ۷ کریس (.م.) ۰

۸ - رد : منتهی‌الارب «کری» . ‎٩‏ - از:کرس + هدن ( پسوند مصدری ) -
کربیدن * کرشیدن و رك :کری کرش .
```


## [2026-09-06T16:17:53.486Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg258.png"
}
```


### [2026-09-06T16:17:54.011Z] TOOL RESULT

```

```


## [2026-09-06T16:17:54.003Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T16:18:06.753Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg258.png')\nprint(im.size)\nim.crop((1450,850,2000,940)).resize((1650,270)).save('c258_kars.png')\nim.crop((900,480,2000,700)).resize((2200,440)).save('c258_n2.png')\n\"",
 "description": "Crop Persian boxes from page 258"
}
```


### [2026-09-06T16:18:09.832Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-06T16:18:12.295Z] TOOL CALL #18: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c258_kars.png"
}
```


### [2026-09-06T16:18:12.317Z] TOOL RESULT

```

```


## [2026-09-06T16:18:17.700Z] TOOL CALL #19: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1631 2>&1 | head -70",
 "description": "Fetch BQT page 1631"
}
```


### [2026-09-06T16:18:25.790Z] TOOL RESULT

```
REF: BQT:1631  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 424  OCR-lang: fas

۱۹۳۱ کره
خواشند ۱ - و بمعنی آرامگاه وآشیانه مرغان | و شرف انان باین فضیلت است ؛ و بفتح اول
و غیره نیز آمده است ۲ - و بفتح اول و ثالث وئانی هم آمده است.
وسکون ثانی؛دندان میان تهی وکاواك راکوبند ۳ کروی‌زده ۷ « بکر زای قطه‌دار
- و بفتح اول و نانی و ثالث , جانوری باشدسیه [ ورای قرشت و سکون ها نام یکی از خویشان
رنگه .گوبند زخم آن جانور زیاده بر زخم‌مای | افراسیاب است و او درکشتن سیاوشی سعی بسیار
است ۴ . کرده است (۷).

کوویا * - بروزن اغنیا . تخمی است گره - بفتح اول و نانی وخفای ها .
که آنرا زیرة رومی کوبند و نان خواه همان | پوست دست و پا و اعضارا کویند که بسبب کار
ات . بر روی خمیر نان پاشند و خوردن آن کردن بیار سخت شده و یدنه بته (۳) باشد -
بناشتا قوت معده دهد وکرویه(۱) و زبنان هم و بمعنی چرك هم آمده است که عربان وسخ
میگوینشش . کوند ۸ (4)- و که راز کفته‌اند ۹

کرویز ۱ - بفتح اول وسکون ثانی بر | وآن روغنی باشد که از .وغ گیرند - و بمعنی
وزن شبدیز » بمعنی نطق و ادراك کلیات باشد | حجره هم هت که خانهٌ کاروان سرا و مدرسه

() چش : کروهه . (۲) چش: - واو .. کرده است.

(۳) چش: - پینه بسته . (4) چك » چش : میگوبند .

۱« بدانکه لفظ کراع که در جمیم نخ موجوده برهان قاطم بهمین شکل وعنوان
واقم است » درین مقام بغایت نامناسب آمت » زیرا که بمعنی ی که مراد مصنف است در کتب
لغت عرب با وجود تفحص تام اصلا بنظر نرسیده ... » « چك ص ۵۸۹ ح *.

۲ - ببردش دمان تا بالبر زکوه که بوش بدانجا کنام و کروه .

فردوسی طوسی « فرهنگه نظام >.

ولی درفغرست ولف این‌کلمه نامده . ۴ کرو (ه.م.). هنینگ گوید : کر وه(68۲۷6ا)

( سوراخ » دندان فاسد ) ( امدی , ص۱۱۵) » همچنین کرو نوا ؛ شمسی فخری‌س۱۱۳؛ر4:

فولری آ1 . ص ۸۲۶ ببعد ) # سغدی :11081 - 1۳87۷۷ ( دارای دندان مجوف با فاسد ) ؛

نیز ۴۳۷۷7 (فضای خالی - شاف . رخنه) ۷۷۵۲۵۹..,8505 1088 50804120 ,۲1۵001808
2.۱80.6۰

باز چون بر گرفت دست ز روی کروه دندان و پشت چوکانت .

رودکی سمرقندی ۶ لغت فری ۶۸۲ >.

۴ - رك : رشیدی . 8 رد4 : کراویا . : ‎٩‏ -ظ . برساخته فرقهٌ
آذرکیوان ۰ ۷ - ولف در فهرست شاهنامه «گروی زره 2171 600۳۲۵12 » ضبط کرده.
نام فهرمانی تورانی :

گروی زره آنکه از کام و داد نزادست و هرکز مباد این نژاد.

« فردوسی طوسی . شاهنامهٌ بخ اج ۶ص ۰۱۹۹

۸ - چون‌دست ویای‌پاك نه‌بینمت جان ودل این هردوپاك بینم وآن هردویا کره.

ناصن خسرو بلخی ص ۳۸۶ *.
دخه بدل‌آن : هر دو پرگره . ‎٩‏ - امروزه (8676)1 تلفظ کنند .
```


## [2026-09-06T16:18:47.073Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD karic/karīč\"; grep -n -i \"karīč\\|karic\\|kalīč\\|kāhīg\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB\"; grep -n -i \"karič\\|karīč\\|karic\" NYB_vol2_glossary.txt | head -20; echo \"=== HRN kar\"; grep -n \"karah\\|kare\\b\\|čardah\\|cardeh\\|tschardeh\" HRN.txt HUB.txt | head -20",
 "description": "Grep Pahlavi/Persian refs for karič"
}
```


### [2026-09-06T16:18:47.163Z] TOOL RESULT

```
=== PHD karic/karīč
=== NYB
=== HRN kar
HUB.txt:4473:ganger', skr. pafidti-; jigar *Leber, zd. yakare^ skr. yakri-;
HUB.txt:5292:zd. yakare ; Jau *6erste' = zd. yava- ; javan, juvan 'Jung-
HUB.txt:8509:neben tak Xauf ' = zd. taka- ; jigar Xeber = zd. yakare,
```


## [2026-09-06T16:18:48.704Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC leaf ~310 (p.590)\"; awk 'BEGIN{RS=\"\\f\"} NR>=308 && NR<=313 {print \"----LEAF \"NR\"----\"; print}' IEC.txt | grep -n -i \"keru\\|kur\\|kera\\|ker-\\|590\\|589\\|591\" | head -40",
 "description": "Look at Mann IEC around p.590"
}
```


### [2026-09-06T16:18:50.436Z] TOOL RESULT

```
=== IEC leaf ~310 (p.590)
117:krek- "a raucous bird; bird-cry'. Cf. WP I, 413 & krik-, kreko, etc. Skt. cf. krakarah 'kind of heron'; Gk. kréx, gs krekós ‘landrail’; Lat. crex, gs crecis *daker- hen’; W crec ‘chirp’ beside cregyr, m. ‘heron’; Cz. krek ‘croak’; Pol. cf. krzekac ‘squawk’; Big. krec 'tree-cricket'; Latv. (*-&-) krekjs ‘nuthatch’
121:krekō, ið ‘creak, screech, grind, grate’. Cf. WP I, 463, 483 & 486 and next Skt. cf. krákşamānah, adj. ‘roaring, raging’; Gk. krëko ‘creak’; Lat. cf. crex, gs crecis “daker- hen’; MIr. crech ‘raid, foray’; W cregu ‘grow hoarse’; crec, m. ‘chirrup’; Cz. křečet, inf.
124:krekos ‘creak, screech’, etc. Cf. krekō, kreki- tos, krekoros, krek- Mir crech ‘foray’; Ir. creach ‘plunder’ (prob. here. See krek-); W crec ‘chirping’; Cor. creg, adj. ‘hoarse’; Lat. cf. crex, crecis, f. ‘daker- hen’; Cz. kfek ‘croak’; Gk. krex, gs krekós ‘landrail beside kréko, v. ‘screech’; Latv. cf. krecu, er (2) ‘croak’
130:krembo (kromb-) ‘twist, bend, turn, folg’. Cf. WP I, 276, IL, 373 & 589 & krinbos below Gk. cf. krémbolon *bobbin' (isophonic: krém- balon ‘rattle, castanet); OHG hrimfan, rim- phan, MHG rimphen ‘crease, crumple’; OE hrimpan, id.; Du. cf. rimpel ^wrinkle'; Li. cf. kremblyjs (a fungus)
```


## [2026-09-06T16:18:58.807Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kūra\\|kūrah\\|kura ‘\\|kūre\\|Pers. kūr\" IEC.txt | head -20; echo \"=== kerə burn in IEC\"; grep -n \"kerō\\|kera-\\|kerə\\|‘burn’\" IEC.txt | sed -n '1,40p'",
 "description": "Search Mann IEC for kura"
}
```


### [2026-09-06T16:18:58.879Z] TOOL RESULT

```
16015:skür- ‘cover, shell”. Cf. skuu. WP II, 548 Per. suküre, s. ‘earthen dish’; Lat. cf. ob-scü- rus, adj. ‘dark’; OHG skūra, f. ‘barn’; MHG schūr, sm. ‘shelter, protection’; Du. schuur, f., LG schür, n. id.; ON skúr, s. ‘penthouse; shell”; Li. dial, skūrà, f. “fur, pelt’. Cf. also Arm. xr-tin, adj. cpd. ‘dark, obscure’. Mod. G Scheuer, mfn. represents a type *sküuor-, see skuu- ‘cover’, but dial. Schauer occurs. (The epithetic Dio-skūroi ‘Castor and Pollux’ seems to contain the isophone *skūr- in Eng. shower: G Regen-schauer or indeed G Schauer ‘shudder’. Omitted. fr. FK: EWDS. Isophone: ON skýra, v. ‘explain’: skyrr, adj. ‘clear, bright, clever’)
=== kerə burn in IEC
289:aidhō (əidh-) ‘burn’. WP I, 5 Skt. idhé, v.; édhah, m.; Gk. aítho; MHG eiten; cf. Alb. eth *mate bull with heifer fr. *aidhsko
560:WP I, 63. Cf. oguhis Lat. anguis, cf. anguilla; Br. anv 'slowworm' (Br. -v- from -guh-, as in devi, v. ‘burn’, from dheguh-, q.v.); OCS oZ 'grass-snake"; R už ‘adder’; Li. angis, f. ‘viper’; cf. anginas “a poisonous serpent’; Latv. odze ‘viper’
788:atros; atrios “fire; fiery. WP I, 42 Av. àtars ‘fire’; atryom (“ashes? or sim.); Per. ati$; Oss. art, pl. ártütà; Arm. cf. arem ‘burn’; Lat. ater ‘black’, atrium ‘vestibule’; cf. also atr-oóx 'fiery-eyed'. (The phonology of Srb. etc. vàtra “fire? is obscure)
1029:büs- (?) ‘vapour, emission; emit. Cf. busd- Skt. cf. busáh, -ám “emission, mist, dung, chaff, curd’; busyami ‘discharge’; Per. bü ‘smell’; Lat. cf. am-büro, com-büro ‘burn’ beside bustum (“burning place for corpses’. Lat.-buro, not -üro, despite WH); OE pos *catarrh'; MHG cf. phüsen ('snort', fr. *büs-)
1414:bhlug- (1) (bhulg-?, bhlsg-?) ‘flash, gleam’. See variants, & cf. bhluk- Lat. cf. (ambig.) fulgeo, ere; OHG bluhhen ‘burn’; LG blucken
1434:bhluso, ið ‘well-up, surge’. Cf. bhluuo Gk. (ambig.) phlúð, phlúzo, id. and 'chat- ter’; Alb. m-blush, m-bush ‘fil’; MHG cf. (w. nasal infix) blunsen ‘inflate’; OE a-blysian ‘blush’; Du. blozen, id.; cf. (perh.)) OE blysian ‘blaze’ and Ger. Blüse ‘bonfire’; Li. blusines (tmeasles. Infl. of blusà: Slovak blcha, etc. (flea). (The semantics of ‘burn’ and *well-up' are difficult to differentiate. A variant *bhlüsK- is represented in Upper G plauschen *chatter")
1618:bhredho (2) “burn, roast, scorch’. Gk. prétho (1) ‘burn’; Gallo-Lat. bridum (queried: *roasting-jack); OS bradan, OFris. bréda, OHG  bratan, sv. 7, Du. braden ‘roast’; OE brædan ((2) “roast, toast; ON bræða ‘heat, melt; braó “tar”, bræði ‘passion’; Gmc. LW in Lat. bràdo ‘roast meat'; R be- redit “inflame”
2091:dáuos below Skt. daváyami ‘burn’, dàvah ‘fire’; Gk. daíó (2) ‘buro’; MIr. dom, id. (but ambig. in view of OW deifaw, Br. devi, id.)
2738:dheguhos, -es-, ios, is ‘burn, burnt matter, fire; burning” Mir. deg, dag ‘flame’; Ir. deigh, daigh ‘fire’; OCS cf. *degüti; Cz. dehet, R dégot ‘tar’; Li. degesys ‘burnt smell; degesas ‘charred spot’; degiai, pl. ‘slag’; degis, m. ‘burn’; Latv. dedzi, pl. ‘charred field”; degas, pl. 'burnt-out ruin'
2957:dhoguheið ‘make burn, heat; keep burning’. Cf. dheguh-. WP I, 849 Lat. foveo; Alb. ndez ‘ignite’ (fr. *en-dho- Buh-); Olr. cf. addoaim ‘kindle’; Ir. dóghaim, tr. & intr. ‘burn’; OHG tagen, OE dagian ‘dawn’; Li. (Zemait&) dagéju, éti “get hot, flare up’; (IE *-ó- in alleged Cz. dahnéti ‘to glow")
3770:eusó (us-) ‘burn’. Cf. us-
3961:geros, geros (1) ‘good, fit, healthy’. WP cf. I, 686 Tokh. B cf. tsarw-, v. “feel relieP;-Arm. (*-8-) kir "use utility; Myc. (?) (queried) kera- Cperquisite' = Gk. géras? See gerð 2); Gk. gerós ‘hale, fit; ON (ei kærr ‘dear, inti- mate’; cf. kerski, f. ‘cheer, fum; Li. gëras ‘good’; gêris, m. id.
5130:guég- (or guégh-) “burn, sting’. (Much ofthe evidence is ambig. cf. gio (2) and gui-, gu- heg-, the last infl. by type dheguh-). Cf. WP I, 849 ' Per. zāg, zaj ‘vitriol’; Oss. dzagw “hot poultice’; Gk. cf. Bésbion (oros) ('Vesuvius', if not a hel- lenized form of V.); Alb. cf. zegth *horsefly', zegël, id.: Ir. cf. beaghán, s. ‘sting’; OCS (am- big.) Zego, žešti ‘kindle, burn’; Cz. Ze, id. beside žeh ‘burn’; Zehrati “be angry”. Cf. (*-6-
5212:gui£0, io “burn, sting’. Cf. giĝö (2). (The Arm. and Sl. evidence is ambiguous) Arm. kcem ‘prick, sting’; kic, gs kco “bite, sting’; Alb. xixë, f. ‘spark’ (fr. *guigio); Lat. cf. (?) -villa in favilla “hot ember’; Pol. gzié sie “be in heat’; gzik 'cattle-fly'; cf. also giez, pl. gzy ‘gadfly; libido'; o-gde in Arm. kajc, i-st. ‘spark’; kez ‘brazier’; kizem ‘burn’; Alb. zeg- th, dim. ‘gadfly’; ON kveikr ‘wick’; kveikja, f. *kindling-wood'. Arm. ambig. as also Li. giež- ti, v. ‘tch’. For gaiZüs ‘sour, irascible’ see goig-. A variant occurs in Li. ZieZerka, ZieZirba “spark”, and OCS Zen Zígati ‘kindle, burn’; though the relationship, if any, w. Zego, Zesti, id. is uncertain. Cf. guheguh-, & guoi?- below.
5493:guheros “hot; heat’. WP I, 687. Cf. guhermos. (O-gde in Iran.) Skt. háras, n. (anger; Av. (o-gde) gar-, v. ‘burn’; Arm. ğer, o-st. ‘hot; Gk. théros, n. "summer, harvest’; Olr. cf. fo-gerim, v. ‘heat’; OCS cf. Zeravü *^white-hot'; Srb. Zerava "em. bere": long-gde in OCS Zarü Cheat and com. Sl.)
8599:Kauio (1) “burn, scorch, dry’. Cf. Kaustos. WP I, 376 Myc. kaw- ‘kindle’; Gk. kaio, fut. kaúso ‘kindle; shrivel; burn’; Alb. thaj ‘dry’, OHG heian, MHG heien, intr. ‘burn’; cf. G hei, adj. ‘dry’; Swiss ge-hei, adj. (2), id.: cf. G He- rauch ‘smoke from burning moor’. The se- mantics of Go. hawi, OHG houwi, etc. ‘hay’ are uncertain. See kau- ‘hit’. A variant of the above root occurs apparently in Av. saoko, saoco, m. “burning, burn, fuel
9168:Kuko, ið (or Kuqu- ?) “hurt, burn, make smart, squeeze'. Cf. WP I, 378 Skt. -Sucyàmi, pp: -Suktáh, cpds. (“feel pain, smart’; Vedic: "bur Per. cf. sūg ‘grief be- side suzidan, inf. intr. ‘burn’; sūz, s. id.; Oss. südzin, Dig. sodzun ‘burn, smart": Alb. thuk ‘squeeze, hurt’; cf. i thukët ‘compressed, com- pact; Cz. sykat (bolestí) ‘wince from pain’; sykat ‘shrink, contract; Latv. sūkstēt, inf. (burn, sting’, fr. *küksko). (LW in Arm. suk, gs sko 'grief")
11979:öd- (2) ‘eat’. Cf. éd-, etc. and od- (1) Arm. (ambig.) utem, v. ‘eat; corrode’; Lat. cf. (?) ad-oleo, Ere, v. tr. (2) ‘burn’. Unrelated to Umb. ufetu, which = Lat. orditor “let (the fire) be started"); Go. cf. fra-atjan, v. “put out to graze’; OHG azzen, id.; MHG atzen, etzen, id. beside atz, atze, s & wm. ‘fodder’; OE ettan ‘turn to pasture, of land”; ON etja, v. ‘incite; put feed to animals’; Sw. cf. åtel, m. “bait, carrion’; Latv. cf. odere, f. ‘fodder
15584:sker- (sKer-) ‘rock, reef, skerry’ Arm. cf. xarak, i, av, id. (fr. *skerək-); Ir. sceir, f. id.; MHG schëre, wf. id.; ON sker, pl. -ja, n. ‘skerry, reef; Slovene cf. čér, m. (reef, cliff, fr. *sKer-). Cf. sker, ið (skher-)
17943:sueld- “perish, decay; ruin, destruction’. Cf. suold-, suld- and suelo Go. swiltan, sv. 3., OE sweltan, ON svelta, sv. 3. id.; Sw. svälta, p. t. svalt, pp: svult, v. ‘starve’, intr.; cf. (type *sulds in) Oss. xälc (2) ruin, decay’; Arm. Kayc, gs & ab. s. Kaycu, s. ‘hunger’; Go. swulta-, cpds. ‘death’; ON sultr, m. ‘famine’; Norw. sult, s. “hunger” beside ON soltinn, OE swolten, pp. ‘perished’. (ISophonic in MHG swélzen, sv. 3. ‘burn’; E to swelter & sultry, prob. here also)
17945:sueló (1) “burn, smoulder, blaze’. WP IL, 531 Skt. svárami, v. (2) ‘shine’; svar, n. ‘sunlight’; Av. Xxwar-, v. ‘shine’; hvaro, n. ((sun': Skt. svar, svaruh 'sunshine?)); Per. (ambig.) xuval, s. (lampblack', but cf. suord-); Gk. belle & héle, f. “heat of sun: also hélé, f. id. cf. eláne, f. lamp, torch'; dial. weléna, f. beside heléne, f. ‘goddess of light’; Lat. cf. sul-phur, z-gde (sulphur, w. semantics of OE cwic-fyr *'sulphur); OE swelan, intr. ‘burn, be burned? beside swaelan, tr. ‘burn’; G schwelen, v. 'smoulder'; ON svaela, wv. ‘choke’; f. ‘dense smoke’; Li. cf. svelmē, f. ‘smoke’; Latv. svelme, f. ‘glow’; (z-gde in) Li. svýlu, svilti, v. 'smoulder'; Latv. svilstu, svilt, v. ‘glow’; Fris. svilja, v. (dry, fr. *suelið); a possible cpd. in deíle, f. “twilight. The initial (su-) is explicit in Hes. (Lacon.) wélan, acc. ‘glow’
17950:suelo "waste, consume’. Cf. suelo (1) Oss. cf. xwali, soht s. (corpse; Arm. cf. n-Koyem, v. (famish; faint w. hunger”, fr. *ni-suel-); EME sweal, v. ‘melt’; E dial. sweel away ‘die off" (isophonic in OE swælan, tr. ‘burn’); Icel. cf. sólunda, v. w. dat. tr. (^waste, consume’. Vocalism of sópa, v. sweep"); Lat. solo, are, v. (1) "lay waste’; (isophonic: Sw. svål, m. “horny skin, sward’; MHG swéllen, sv. 3. (2) *faint w. hunger?)
18115:Oss. cf. xålc, s. (2) ‘ruin, decay’, (fr. *sulds); Arm. Kayc, gs. ab. s.-u, s. (Áhunger', fr. *sulds); Go. swulta-, cpds. *death-^; OE cf. swolten, pp. ‘perished, dead": ON sultr, m. ‘famine’; sol- tinn, adj. ‘starved, dead": Norw. sult, s. *hun- ger; (e-gde in) OE sweltan, sv. 3 “perish”; Sw. svälta, ON svelta, id. beside (o-gde) svält, s. “starvation” (sulg-, see Supt: S) sundh- ‘burn’. Cf. suendh- (suondh-). WP II, 526 | Tokh. B sat, s. ‘coal’; Gk. cf. ánthrax, gs: -akos, m. ‘ember’; OCS cf. pri-svengo, -svengoti, v. “get scorched’; beside Cz. svédét, v. "ch, burn’; Pol. swedzic, wd: cf. (o-gde) swąd, m. *smell of burning, firedamp' sunmn- “hum, song’. Cf. suen-, sumnos Gk. hümnos, m. ‘song of praise, dirge'; G summen, v. “hum”; Norw. summe, id. (suo-bhi, cf. sue-bhi (suá-bhi) “by itself, of itself? Arm. cf. kav, prp. “without, except’; kavem, v. ‘forgive’; OCS (and com. Sl.) svo-boda, f. *freedom) suodhā, io ‘cleaver’ Skt. svadhá, f. id.; beside svádhitih, mf. ‘axe’; ON sveðja, f. ‘cleaver’ suoib- ‘go, depart Av. xšvaeway(eimi), v. id.; cf. xšvaewō, adj. ‘smooth’; Ir. (ambig.) saobhaim, v. tr. ‘turn, divert, pervert’; MHG sweifen, sv. 7. ‘sweep along, gambol’; sweif, sm. ‘swagger’; OE swapan, sv. 7. ‘sweep along, rush; seize’; swæp, m. ‘deceit’; ON sveipa, v. ‘sweep’; sveipr, m. (2) ‘stir; mod. sveipur, m. ‘twist, cur; Sw. svepe, v. ‘drape, wrap’; svep, m. ‘lash’. (NB. Li. dial. sviðbelis, m. ‘match — for striking fire’ is fr. G. Schwefel) suoid- (o-gde of type suid- (1), suidið, q. v. in Skt. svédāämi, v. ‘sweat; Per. xwaydan, inf. id.; OHG sweizzan, wv. id.; OE. swætan, wv. id. (Isophonic: Latv. svaidu, it, v. (2) ‘smear, anoint’). WP II, 521. Nominal: Skt. svédab “sweat; Per. xüy, id.; OHG, MHG sweiz, sm. id., OE swat, n. id. (and ‘toil, | cf. E “swot'); Du. zweet, n., ON sveiti, m. id. (and *blood"); Latv. cf. sviedri, mpl. id. WP II, 521
19593:us- (1), radical: ‘burn’. Cf. euso Skt. cf. ustah, pp. as adj. ‘burnt’; Lat. ustus,
```


## [2026-09-06T16:19:04.604Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 309 310 311; do echo \"=== NR=$n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$n'' IEC.txt | cut -c1-160 | head -50; done",
 "description": "Print IEC leaves 309-311"
}
```


### [2026-09-06T16:19:06.197Z] TOOL RESULT

```
=== NR=309 ===
�boar’; Li. kiaülé ‘sow’
koulos, is, io (2) ‘round, plump; ball’. Br. kül “fat, plump'; Pol. kula "ball bullet, pommel’; Ukr. kulja “ball, globe’; Cz. koule, id.; R kuP, m.
kounā (keun-) ‘marten, sable’. (Classical forms derive fr. OPer.) Ober. (in Gk.) cf. kaunáke ‘sabie fur’; kauná- kes “fur coat; LW in Assyr. also i
koupeio, koupio ‘pile up’. See koupos Cz. kupiti, inf., id.; Li. kaupiu, -ti, id.
koupos, à ‘pile, heap, hill, mountain’. WP I, 372 Av. kaofo ‘hump; mountain'; OPer. kaufa-, id.; Alb. (ambig.) kapë, f. ‘shock of sheaves, pile, bundl
(kouros, see kauros ‘cock’)
kouiios, om ‘holding; holder, fastener’ Skt. kaviyah, am *bridle-bit'; cf. also kavah "mi. serly; Hes. koion ‘pledge, hostage'; ON cf. heyja (1) “hold; 
kouilos, om (?) ‘hollow, dome’. Cf. koiliom Gk. koilos, kóilos, adj. 'hollow'; koilía, f. id.; OLat. cf. Juno Couella ‘Juno of the Heavens’ beside coe
kouos, à ‘hollow, pit, cavity’. Hes. kóos, id.; It. covo, cova, id.; Sp. cueva, id.; Skt. cf. kav-andhah, -am “barrel, belly, trunk’; Gk. cf. kó-bath
krab- “dash, rush, attack, snatch'. (Evidence ambig. Cf. krob-) OE hrepian, hreppan ‘touch, attack’; MHG raffen, reffen ‘snatch’; ME & LG rapen ‘sna
541
reppen ‘press’; zich — ‘hurry’; cf. rap, adj. ‘nimble; ON hrapa ‘hurl, hasten, tumble’; cf. hrapaór ‘haste’; Li. cf. krabždù, -déti, int
krad- (kradāið) ‘shake, dash’. See next & cf. krd- Gk. kradáo, kradaíno, tr. ‘shake’; OE hratian ‘ush’; ON hrata, intr. ‘stagger’; hret, n. 
kradelos, à ‘shaking; shake, rattle’. Cf. krad-, (krd-) & krotolos (1) Gk. kradalós “easily shaken’; krádalos "De. branch’; OE hratele, f. 'yellowr
krádos, om, à “crust, surface’. (Evidence ambig.) Alb. krodhé “crust of bread; scab'; Go. cf. hrot, n. (roof, garret’, lit. ‘surface, top); OHG ruo
kradh- *hurt, harm'. (Evidence ambig.). Mir crád, Ir. crádh ‘torture, anguish’; crádim, cráidim, Ir. crádhaim (torture, vi: ON hræða ‘disquiet’; 
kragilis, os (kragul-) (?) (radical: krag-) W craell, f. ‘aridity’; Du. rekel (2) ‘rake, good- for-nothing'; Icel. hrókl, n. ‘aberration’. Cf. the ra
kräeg, ið ‘caw, croak’. See next Gk. krázo, pf. kekraga, id.; Lat. pro-crago, ere, pf. -cràxi 'shout'; OE cf. hrace, hracu ‘throat, gorge’: MHG rach
kra
=== NR=310 ===
gos ^a raucous bird". See above, and cf. krogió Per. (ambig.) kalāy ‘crow’; Hes. kragós, adj. ‘brawling’; cf. Gk. krázo, v. ‘caw’; G Racke
krad- (kradaio) — kraks-
10
20
25
30
35
40
45
542
“a corvine bird"; cf. rackeln, v. ‘caw’; Pol. cf. krogulec *sparrow-hawKk ; Li. krágas ‘coot, dab- chick'. Long-grade in MHG ruoch, Du. roek, OE hroc �
krak- (1) “sharp, rough, rugged? Lat. cf. craceó, ere (“grow slim, taper’. Fest.); Br. krak ‘short, sharp’; MHG rach, gs rahes *rough, steep”. (See
krak- (2) (rock, rough ground’. Cf. krok- ' (2) and krak- (1) Br. krag, pl. kragu ‘flint, pebble’; Ir. W. craig "rock beside W crag “crust, coat, shell�
krak- (krak-) (3) (?) ‘monster’ Gallo-Lat. cf. cracatius “a large fish’; Li. krake ‘kind of carp’; long-gde in Cz. krak (/sea-mon- ster', fr. *krak-
krak- (4) limb, leg, foot, step’. (Evidence ambig.) Rum. (substr. or Sl. LW?) crac ‘thigh’; cracá, f. ‘branch’; Cz. krok, m. ‘footstep’ beside (*
krak- (5) ‘raucous creature’ Blg. cf. krókon ‘raven’; Li. krakë *bee-eater'; krakis, m. id.; Latv. krakis “hag, crone'. See following entries
krakoró, ið ‘cackle, croak’. Cf. karkar-, kre- kor- Skt. (ambig.) cf. krakarah Cheron" See kreko- ro-); Lat. cracero, åre, v. ‘cackle, croak’; Slo- v
krako, ið ‘caw, croak’. Cf. krak- (5), krok-, kark-. Onomat. WP I, 414 Alb. krrok, krókem, id. (krr- an expressive variant); Lat. craco, are, id.; W crawc
kraks- (1) ‘scab, crust; scabby’, etc. W crach, m. & adj. “mange; mangy’; Cor cragh *scurf, scab; scabby’; OE cf. hrescian (que- ried: ‘flake off); 
kraks- (2)
543
Slovene krohot, m. ‘guffaw’; Latv. cf. krak&ket “crack, crash’
kram- ‘rise, go forward, be forward, be exu- berant, boast Skt. kramami ‘go, march, possess, conquer’; krame, mp. “succeed”; OS hrom-, cpds. 'exu- ber
kramb- ‘dry, hard; hardening, crust. See next Hes. krámbos ‘dry’; m. ‘shrivelling blight in grapes’; W cram 'incrustation'; cramen ‘scab’; Br. kr
kramos, à, kramn- ‘scab, crust’. Cf. krambos, knàm-. WP II, 583 W crafen ‘flake, crust’; Br. kroen, kroenn, coll. id.; (cf. W variants: crawen “crus
krank- “noise, jarring, grating, jar, grate". WP I, 414. Cf. kronk-. (The evidence is ambig., and is based on onomat.). Cf. krauk- Per. kulank ((crane" bird);
kranos, à ‘spring, source’. WP I, 488 Gk. kréne (Lesbian: -à-), id.; Alb. krue, T krua, gs kroni, kroi, id.; W c
=== NR=311 ===
rawn, Cor. croen catch, ment, pool; W cf. croni, v. ‘dam’
krap- (krapl-) EME to ravel (tuntwist, unravel. The mod. mng. contaminated by Nor. Fr. raviller “to muddle’); EMDu. ravelen, as EME, then “to tangle’; N
kram- — krauk-
15
20
25
30
35
40
45
544
krop ‘torture’; R kropát, v. ‘botch, mangle? kraps- ‘grab, snatch; rapacious; grab, sei- zure’ Br. krafa ‘seize, snatch; scratch, engrave’; kraf 
545
‘raven’. Cf. also Pol. kruczec ‘growl, rumble in bowels’; Cz. krucet ‘croak; rumble in bowels’: Li. kraukiü, ti ‘groan, creak’; Latv. cf. krauk
kraupióo ‘rouse, incite, bully’ (kroup-?) ON hreyfa ‘stir’; Pol. krupic sie ‘bicker’; Li. kraupiü, ti ‘scare; scold, bully’. Ambig: OCZ. krup�
kraus- (krausro-) ‘hard’ (krousro-?) Cf. krus-, krust- Gk. cf. kraüros “hard, brittle, coarse’; OCS. kruchü ‘chip, fragment; Cz. kruchy ‘brittle, 
krăuos, à (1) ‘mass, heap’ Olr. cró (2) “lot, dead man's property’; Li. krova, kraujà “load, pile’; Latv. cf. krāvums ‘congeries, mass’; ve
kráuos (2) ‘cover, shed, shelter, roof. WP I, 477 Olr. cr
```


## [2026-09-06T16:19:16.049Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hearth\" IEC.txt | head -20; echo \"=== Ker heat\"; grep -n \"Kerə\\|Kerta\\|Kertā\\|Kerto\\|Kertos\\|Kuro\\|Kurð\\|Kurō\" IEC.txt | head -20",
 "description": "Search IEC for hearth/Kertā"
}
```


### [2026-09-06T16:19:16.129Z] TOOL RESULT

```
287:aidhlos, aidholos, om ‘burning; consump- tion’. WP I, 5. Cf. aidhó Oss. ird (adj. 'bright); Myc. (name) Aithalos; Gk. aíthalos, aithále ‘ashes, embers’; Alb. jézull ‘embers; MIr. ael, aol ‘quicklime’ (in mod. Ir. also ‘bright colour); Br. aoled, oaled, Vannic oeled; Cor. olas; OCor. oilet; W ael- wyd (all = *hearth") beside W aeled, m. "Drei: OS éld; OE ål; ON eldr ‘fire’; OE &led, obl. &ld, id.
299:aidhst- (aidhəst-, əidh-) “heat, burning, furnace, rage'. WP I, 5, cf. aidho, aidhos Av. istyo ‘brick’; Alb. ethe ‘fever’; Lat. aestus; aestas; MIr. áith ‘kiln’; Cor. eth ‘hearth’; eth ‘vapour’; OE ast; Du. eest ‘oast’; Lusatian jest ‘foam, cf. n-e&c ‘fireplace, ovenhole', cf. *en-aidhst-)
542:angólos (angol-, angil-, angl-), is, iə “coal, coal fire’. WP I, 181 Skt. ángarab; Ir. aingeal, pl. aingle “fire, hearth, cinder; W engyl "Drei: OCS ogli ‘coal; Li. anglis; Latv: ogle, pl. id. The con- nexions of Alb. thëngjill ‘coal and OHG kol, kolo, id. with the above forms are not clear.
745:as- ('as-) radical “burnt, brown’. Cf. as20(n), asdó, asio(n) Skt. asitab "dark black’, asah ‘ashes’; Tokh. as-; Arm. (?) v-ar (i-stem: ‘inflamed’, fr. *apo- asi- (?)); Hitt. hassis; Lat. assus, beside aridus; Icel. cf. arinn, pl. arnar ‘hearth’ and cf. Sw. -os in kol-os “firedamp” (*as-)
760:āsos, à ('as-) ‘hearth, sacrificial altar’. Cf. as- Hitt. hassas; OLat. asa; Lat. āra; cf. Umb. aso, Praen. asom (pp. “burnt')
3293:(variant) thuméle ‘hearth’
5525:guhoros, is “heat, warmth; hot place, burn’. WP I, 688. Cf. guher-, etc. Lat. cf. (Isidor) forvus ‘hot’; OIr. guire, MIr. & Ir. gor, sg Br. gor m. ‘heat’; (pl. iu, m. ‘abscess’ to guhr-, q.v.); OCS gorü, s.; Cz. hof, m.f. ‘heartburn’ beside vy-hor 'burnt-out spot: OCS gorikyj ‘hot’; Li. gáras ‘heat, zeal, steam’; pra-garas ‘hell’; Latv. gars ‘spirit: steam’; OPr. goro (for *goàro 'ashpit, hearth’). Long-grade in Blg. R. gari; R u-gàr; Srb. gar
5564:guhrnos (1) 'ashpit, firepit, clay oven, earthen pot, crucible’. WP I, 687. Cf. guher-, etc. Skt. cf. ghrnáh ‘heat’; Lat. fornus, furnus ‘oven’ beside hirnea ‘earthen pot’; MIr. gorn ‘fire’. Mod: id. and ‘torch’; guirn ‘firebrand’; W gwrn “urn, cone-shaped vessel’; OCS grünü ‘cauldron’; cf. grünylí ‘foundry’; R gorn “fur- nace, forge, hearth’; Pol. cf. garn-ek, dim. ‘pot’; Cz. hrn-ec, -ek, id.; Srb. grnac. id. Cf. ON orna v. ‘warm’. (For the semantics cf. Skt. kundam ‘firepit’ and ‘pot’, and that Aus- tralian aborigines still build earth-ovens. Cf. the structure of the Sardinian nuraghi, of co- nical shape, primitive blast-furnaces?)
6177:Ion ‘fire’ (1- an indeterminate vowel, pos- sibly a ‘shva secundum"). WP I, 323 Skt. agníh; Alb. ü, gs üni “hunger” beside unë, T urë firebrand’; üth, dim. ‘ergot; unak ‘hearthstone’; Lat. ignis, gp -ium; Mir cf. an- naim, v. ‘kindle’; Gael. áin ‘heat, glow’; (un- certainly ong "Drei: OW cf. enn-ynny, W cy- nneu (?) *ignite'; beside enn-yn, m. (‘kindling, ignition’, fr. *endo-Ígn-?); Cor. cf. (?) c-cena, v. ‘ignite’; OCS (and com. Sl.) ogni, gs and ds ogni, m. ‘fire’; Li. ugnis, gs -iés, m. id.;
6186:Latv. uguns, gs id., gp ugunu, id. (Of uncer- tain provenience are MIr. indeoin, Ir. inneoin ‘anvil’; OBr. ennian, Br. annéw, id.). Extns. Seng ‘inflame’: Lat. ignio, -ire; Cz. roz-ohnit; Li. ugnytis, id. Cf. Latv. ugunot illuminate". *ígnikos “little fire’: Skt. agnikah; OCS ognici, id.; *ígnisthios: Skt. agnistháh ‘brazier’; OCS ogniste ‘hearth’; ognistü, adj. ‘aflame’; ognistvo ‘torch’; *ígniuos: Lat. ig- neus: Cz. ohňový
7286:klāt- (klat-) layer. Cf. WP I, 489. (Radical only in Baltic) W clawd, pl. clodion “patch; shingle'; Icel. hlóð, npl. & boor, fpl. s. ‘hearth? beside Hlóóyn ‘personified Earth"; Li. klótas ‘floor’; klóte ‘bedspread’; Latv. cf. klāt ‘near’. Radical in Li. Mom, inf. klóti “spread”; Latv Ka. klāt, id. (Isophonic: OE hlop **mass; com- pany, gang; booty’: MHG luot ‘mass, quanti- ty’; Li. klotis (1) ‘roof-shingle’; (2) 'success"). Variant in Li. klostis, f. 'roof-shingle'
8710:Kertos, is firm, hard, solid". Cf. kertos, kerd-. (Gmc. & Celt. ambig.) Oss. särt-, cpds. “firm-?; (Iran. LW in Tk. sert “hard, strong, severe'?); Arm. sert, Let (‘solid, firm, sincere, rich, fertile"; Ir. ceart, m. “justice, right; W certh ‘evident; MHG (?) hért, gs hérdes “earth, soil, hearth, home? (qua terra firma?); OE heoró 'hearth, home?
13301:e-grade in view of Arm. herk ‘ploughed field’, see peduom); of ambig. vocalism is Skt. pade pade (“step by step”, *pedei/-oi or *podei/-oi; Gk. pédoi “on the ground"); Arm. otn, gs otin, ab. s. amb, also otk, pl. type ‘foot’; Hitt. cf. (o-gde) pat-, pata-, id.; Gk. poüs, gs podós, m., Myc. pod-, id.; cf. also ne-podes ('seals', lit. *no-feet?); Lat. cf. le-pos, -poris, m. (hare, perh. for *leguh-pods "lightfoot"); (long-gde in) Go. fotus, OHG fuos, OE fot, pl. fet, ON fótr, pl. fætr, m. d: OCS podü, m. “floor, storey”; Srb. ‘floor’; R ‘hearth, open-hearth"; Big. ‘stone floor, slab’ beside Cz. půda, f. “ground”; Li. pádas, m. ‘sole of foot’; pádis, gs: padio, m. ‘base’ (Li. pádas also “bottom, floor of hearth, threshing-floor' under infl. of Russian); Latv. pads, m. ‘clay floor
15793:skór- ‘rubbish’. Cf. skorn- and sknt- Gk. cf. skõr (w. suppletive gs: skatós, see sknt-), n. ‘filth’; Alb. herr, m. ‘weed’; Lat. scOria, f. ‘rubbish’; MHG schuor, sm. & sf. ‘shearing, clipping; misery’; Cz. cf. škára, f. (undressed leather, w. expressive initial); Skar-edý, adj. ‘nauseous’; OCS skar-edü, adj. ‘foul, hideous’. Cf. (short vowel in) Skt. apa- skarah, ava-°, m. ‘faeces’; OE scearn, ON skarn, n. ‘dung’. (NB. The Slavonic doublet in OCS skvarü, skvara 'filth' is apparently a LW fr. scotia, cf. Cz. varhany ‘organ’ and OCS vatra ‘hearth’)
20203:uestus, à, iə ‘light, fire’. WP I, 307 Skt. vástuh, f. ‘dawn’; Gk. hestia, f. ‘hearth’, cf. es-khára, f. (hearth, altar; brazier’, if fr. *uest-°?); Lat. vesta, f. ‘goddess of fire’; cf. in-vestő, åre, v. ‘heat
=== Ker heat
8686:Kerəuos (Keruos) ‘horned; horn, horned beast’. WP I, 406. Cf. Kerod-, Ker- (2), Kro- Av. srva-, ds sraoe, pl. srvao ‘nail, horn’; srvaro “horny, horned'; Per. (alleged) surü ‘horn’; Oss. siwàá, sí ‘horn’; Hiero-Hitt. cf. name: Karhuhas ('Stag-god'. H. Bossert); Gk. kera(w)ós fhorned'; but Myc. keraa (! sic) ‘horns’; Lat. cervus ('stag'. LW in MIr. cerb, Ir. cearbh, id. on account of vocalism); Gaul. carvos, id.; W carw, Cor. carow, Br. karó & karv, pl. kerved, id.; LWs in Finn. sarvas *male deer”, sarvi “horn” and in Hung. szarvas ‘deer. *Scythian in Hes. sergoi (for *serwoi 'stags")?
8709:Kerto “hit, encounter, stab, strike’. Cf. Kerið (1), kert-, kort- Skt. Satami ‘pierce’; Lat. certo, are “fight
8710:Kertos, is firm, hard, solid". Cf. kertos, kerd-. (Gmc. & Celt. ambig.) Oss. särt-, cpds. “firm-?; (Iran. LW in Tk. sert “hard, strong, severe'?); Arm. sert, Let (‘solid, firm, sincere, rich, fertile"; Ir. ceart, m. “justice, right; W certh ‘evident; MHG (?) hért, gs hérdes “earth, soil, hearth, home? (qua terra firma?); OE heoró 'hearth, home?
8711:Kerud- (Korud-) ‘horned creature’. Cf. Ker- “head”, Kernt- etc. (Var: Kerəd-)
9131:Krt- (2) “cut, blow’. Cf. Kerto Skt. śūrtáh, -śīrtáh ‘shattered’; Arm. sartnum ‘be separated’; Per. cf. sile, sili, sīli “slap, blow’ beside süli Cplough lit. ‘cutter’ ?)
12090:OBr. ocol-, id. (beside ocol-uin, id.); OCS osla, f. id.; (Arm. radical *oK- or *aK- in c-asnum, v. ‘flare up’. Alb. éhull, m. ‘icicle’ is either from a type *oKul-, see oksul- above, or from a type *aKulos as in Lat. aculeus, cf. Alb. vjehërr ‘father-in-law’ from a type *sueKuros, q. v. and cf. eh, m. ‘cutting-edge’, fr. a type Sous, see below)
17929:suekrüs (suekrüs, KueKrüs) *mother-in-law'. Cf. sueKuros. WP II, 521 Skt. $vasrüh, id.; Per. xušū, id.; Arm. (variant) skesur & kesur, gs: skesri, ab. s. skesrav, id.; Gk. hekurá, id.; Alb. vjehërr, id.; Lat. socrus, gs. -üs, id.; W chwegr, Cor. wheger, pl. whegrow, id.; Go. swaihro, OHG swigar, MHG swiger, OE sweger, ON svzra, cf. Sw. svár-moder, id.; OCS svekry, pl. svekrüve, id. (variant consonantism); Li. cf. SeSiure, id.
```


## [2026-09-06T16:19:21.712Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"furnace\\|kiln\" IEC.txt | head -30",
 "description": "Search IEC for furnace/kiln"
}
```


### [2026-09-06T16:19:21.756Z] TOOL RESULT

```
299:aidhst- (aidhəst-, əidh-) “heat, burning, furnace, rage'. WP I, 5, cf. aidho, aidhos Av. istyo ‘brick’; Alb. ethe ‘fever’; Lat. aestus; aestas; MIr. áith ‘kiln’; Cor. eth ‘hearth’; eth ‘vapour’; OE ast; Du. eest ‘oast’; Lusatian jest ‘foam, cf. n-e&c ‘fireplace, ovenhole', cf. *en-aidhst-)
1145:bhars- (bhar-, bharis-) (1) ‘wheat, barley’. Cf. bhardhà (bharsdha). WP II, 134 Lat. far, gs. farris ‘spelt, barley, flour”; farreum ‘wheat wedding cake; drying kiln’; farr-àgo ‘mash’; Osc. far ‘food’, Umb. (‘wheat or ‘flour’, in farer opeter “of best wheat/flour'; farsio-, adj. id.); Ir. dim. bair-ín ‘cake, loaf’; Go. cf. bariz-eins, adj. "of barley’; OE bere; ON barr ‘barley’; OCS bürü beside borü (“millet or barley. Gmc. LW?); cf. Slovene bersen ‘full of corn, luxuriant’ beside bér ‘millet’. (Forms with and without -s- seem equally current, cf. Lat. far-ina ‘flour: Umb. far- beside farsio and LLat. farricus ‘of spelt’; It. farro ‘spelt’. Uncertainly: Latv. bar-iba *food")
1291:bhouos ‘construction, working, homestead’. WP II, 140. Cf. bheuo Skt. bhaváh; Arm. bov ‘furnace, forge, stove’, bovk, u-st. ‘mine’; Lat. favus ‘honeycomb, cell of h^; cf. also (?) favissae ‘basements’; MHG bou, gs. bouwes ‘homestead, building, cultivation, product; Du. bouw *construc- tion, culture'
5564:guhrnos (1) 'ashpit, firepit, clay oven, earthen pot, crucible’. WP I, 687. Cf. guher-, etc. Skt. cf. ghrnáh ‘heat’; Lat. fornus, furnus ‘oven’ beside hirnea ‘earthen pot’; MIr. gorn ‘fire’. Mod: id. and ‘torch’; guirn ‘firebrand’; W gwrn “urn, cone-shaped vessel’; OCS grünü ‘cauldron’; cf. grünylí ‘foundry’; R gorn “fur- nace, forge, hearth’; Pol. cf. garn-ek, dim. ‘pot’; Cz. hrn-ec, -ek, id.; Srb. grnac. id. Cf. ON orna v. ‘warm’. (For the semantics cf. Skt. kundam ‘firepit’ and ‘pot’, and that Aus- tralian aborigines still build earth-ovens. Cf. the structure of the Sardinian nuraghi, of co- nical shape, primitive blast-furnaces?)
6115:8houono- ‘casting, pouring’. See $heu-, 8heumn-, 2huuó, etc. WP I, 563 Skt. hávanam “offering”; Arm. dzawn, i-st “gift, dedication’; Gk. khóanos ‘furnace, crucible’; khoánë ‘hopper, dish, furnace’. Alb. cf. dhun- tí ‘gift. See next
6420:ieumos, is, io (ium-) den, cave’. Cf. ioma, ieunis Ir. uaimh, f. ‘cave, cellar; kiln’; Latv. cf. jums ‘roof, shelter, vault, clamp’; Go. (?) jumjo “pile?
6444:ieuios ‘of barley, spelt’. Cf. ieuos Skt. yávyah, id. cf. yavyá *barley-store'; Gk. zeiá 'spelt'; Li. cf. jáuja *drying-kiln'
6448:ieuos, -es-, (ieuio) “a grain (barley, spelt)'. Cf. ieuð (?). WP I, 202 Skt. yávah "a grain, esp. barley”; yavasa, npl. 'grass-fodder'; yavyah “supply of crops’; Av. yavo, gs yavahe ‘barley’; Per. jav (&-), id.; Oss. jäw, jew ‘millet’; Gk. zeá, zeiá ‘spelt’; Li. jà- vas, javai ‘cereals, grain’; cf. jáuja *drying-kiln';
8161:ksërið (1) ‘dry, parch, wither; turn dry, etc. Cf. kseros (1). WP I, 503 Skt. ksáràmi (2) ‘perish’; Arm. cf. xarem (‘sear, brand”, fr. *ksor-2); Per. cf. xirman “barn, threshing-floor'; Gk. cf. kseraino ‘dry’; Lat. seresco, Gre “dry in the sun; get dry’; Li. Seri- uos, -uotis (^wither', intrans.); Latv. seru, sert *dry (grain) in kiln?
10013:loitos, us (2) ‘pouring; downpour, stream’. Cf. leiio, lio (leið (1)) Skt. rétas, n. ‘stream; libation; semen; Av. raetus, m. ‘fluid’; Lat. (ambig.) litus, gs -oris, n. ‘shore’; Li. lietüs, m. ‘rain’ beside (?) lai- tas (casting-floor of furnace’; Latv. lietus, m. as Li. (An Aeolic isophone occurs in a hapax loitos nóo “pure in mind” or sim.)
10861:mld- (crush, pulp, powder’. Cf. following en- tries Skt. mrdā ‘loam’; Alb. cf. mullé (2) ‘rennet, cheese-culture medium; MHG mulzen, v. *kiln-dry'; Gk. cf. a-maldüno “crush”, fr. *sm-°; Sw. multna, v. ‘turn to dust’; Icel. moltna, v. “turn to pulp, get tender
13757:pun-, (oblique form of type puuər (pür-), q.v.) ‘fire’. (Gmc. ambig. See pung-) Oss. Dig. cf. funuk ‘ash, ashes’; Arm. cf. hnoc, gs: -i, ab. s. -av ‘furnace, oven’; ? OHG cf. funcho, MHG vunke, wf. 'spark'; (uncertain- ly) Latv. poss (‘tinder’, if fr. *punsos). Cf. Go. fon, gs: funins ‘fire’; ON funi, m.
13830:puuen- (pəuen, pun-) oblique stems of the following entry q.v. Cf. pun- ` Arm. cf. hnoc ‘furnace’; Oss. Dig. cf. funuk ‘ash, ashes’; Hitt. cf. pahhwenas, gs., pahh- weni & pahhuni, ds. of pahhur “fire”; Gk. cf.
18202:tākā “ground, earth’. Cf. tēkā (5). (Iran. & Alb. ambig.) Pahi. tak, s. ‘ground, bottom’; (LW in) Arm. tak, i, av, id. (and 'arse?); Hitt. cf. takan, adv. ‘to the ground’; Alb. (ambig.) tokë, f. “earth, Soil; Lat. cf. (?) -tax, gs: -tacis in for-tax, f. (“floor of furnace’. Cf. guhor-)
18274:ték- (5) ‘earth’. Cf. ták- Pahi. tak, s. ‘ground, bottom’; Per. tag, wd: (LW in) Arm. tak, i, av. id.; Hitt. tékan, gs: taknas, s. ‘earth’; takan, adv. (‘to the ground”, fr. *tokam); Alb. ambig. tokë, f. (earth, fr. *tek- or fr. *ták-, q. v.). (NB. OHG daha, f. “earth? appears to derive from *tank- or *tonk- in view of its cognate in Go. páho, note -à-, not -&-. This is confirmed by OE po, póhe, f. id. Cf. however OLat. -tax, -tacis in fortax, f. “floor of furnace?)
18434:termn- (termnos, terios) (2) ‘dry’. Variant extn. tertos. Cf. ters- (1), terĝ- (1) Alb. cf. i terëm, adj. ('dry'. Ambig. cf. terĝ-); Ir. cf. tirim, adj. id. (and 'kiln-dried"); W cf. tarn, pl. au. m. ‘wiping, drying’. Variant in Gk. (?) seirós, adj. scorching’, fr. *terjós?); and in Alb. i terté ‘dry’; Ir. cf. tiortha, adj. id.
18818:tors- o-gde of type ters-, and cf. trs- (Lat. *tors- or *trs-) & tor- (2) ‘dry; thirsty; parched; dryness, drought, kiln’ Skt. tarsah, m. ‘thirst’; Lat. torreo, ere, v. tr. ‘roast, scorch, dry’; OHG darra, f. ‘kiln, oast’; MHG darre, derre, wf. *drying-apparatus'; der- ren, wv. tr. ‘dry’. Variant in Alb. tar, v. ‘dry, roast'; OE þæran, id.
```


## [2026-09-06T16:19:27.810Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 333 334 335; do echo \"=== NR=$n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$n'' IEC.txt | cut -c1-200; done",
 "description": "Print IEC leaves 333-335"
}
```


### [2026-09-06T16:19:29.397Z] TOOL RESULT

```
=== NR=333 ===
ukáð ‘mix, confuse, disturb’; Cz. kyšu, kysat ‘ferment’; Li. kušiù, čti, intr. ‘move, stir beside kušinu, -inti ‘touch’; Latv. cf. kū- sāju, āt ‘well up, seethe’
kul-, see kulio, kulis, kulios, koul-, etc.
kul- (1) ‘dash’ Ir. cuil, f. ‘eagerness’; Du. hollen ‘dash, gal- lop”
kul- (2) “flow, stream, ditch, drain” Skt. cf. kulyá “ditch, dike'; Lat. cf. culina (2) “sink, burial ditch?
külëið “make smutty, get smutty, singe’ Skt. külayami ‘singe’; Li. küléju, éti ‘get smut- ty’; cf. küle ‘smut’
kulen(d)- ‘prickle, sting; holly’. Cf. kulis and cf. WP I, 435 Mir culenn, Ir. cuileann, id.; Gaul. colinno- (in a place-name); W celyn, Cor. kelyn, Br. kélen, id.; OE holen, id.; MHG cf. bolun- 
kulogos, om (kul$-) ‘hollow, container’. Cf. kulik- Skt. kulijam "a measure of capacity’; Lat. cf. culigna “bowl, dish’; OE holoc, holc ‘cavity’; hulc ‘ship, hulk, hut; Cz. cf. kluz, m
585
basis of zero-gde) ‘trench’; cf. EME to hulk “disembowel'; LG hólkern ‘winkle out, hook out?
kulik- ‘hollow, cavity, container”. (Variant of kulogos, q.v.). WP I, 442 Gk. külix, gs külikos ‘gobleť; cf. kúla, npl. ‘hollows of the eyes’; Li. kulíkas ‘purse, bag, scrotum’. (Th
kulind- (kulnd-) ‘curl, roll; curled creature’. Cf. kulio (2), kulos Skt. cf. kundalah ‘snake’; kundalam ‘ring’; Arm. koying, koyinc, s. ‘snail, slug’; Gk. cf. kulíndo 'rolP; külindr
kulis (kulik-) ‘gnat, fly? Lat. cf. culex, gs. -icis ‘gnat’; MIr. & mod. cuil, id. beside MIr. culicán “small fly; W cylion, coll. ‘gnats’; Cor. kelyon, id.; OHG cf. huls, gs hulis, sm. (
külis (1) and (2), see külos, om (1) and (2)
kulio “strike, beat. Cf. WP I, 437 & II 598. Cf. kulo$-, kulik- Lat. culið, ire “bang, shake"; per-culio “strike down’; Alb. n-gul, v. (‘thrust in’, fr. Sen" Li. j-kulià “hammer in"); 
kulio(n), (kulik-, kuliks-) ‘pup’ Arm. cf. kulik, id.; Alb. kulish, kélysh, id. (*kuliks-); MIr. cuilén, Ir. cuileán, id.; Br. ko- len *young of animal
kulios, io, iom, kulom “pocket, pouch, recept- acle’. WP I, 332 Skt. kulyam ‘receptacle for bones’; kulyà ‘canal’; Gk. kúla, npl. and Hes. küllia “hol- lows under the eyes'; Lat. cule
kulik- — küm-
10
15
20
25
30
35
40
45
586
-io, m. (“bag, scrotum’. Lalis), Latv. kule, f. “bag, sack’; W cwll, pl. cyllau, m. ‘stomach’. (The Gmc. evidence: MHG hol, OE hylu, ON hylr, etc. point to a form Kl-, q.v. Ir. cuile ‘ce
külos, is (1) ‘chink, crack, corner, rear, arse’. Cf. WP II, 547 Skt. külam (2) ‘rear of army”; Prakr. cf. kola "mm the rear”; Alb. kilé “ham, hock’; Lat. cülus, gs -1, m. ‘arse’
=== NR=334 ===
 ‘gusset’. (OCS kyla ‘hernia’ appears to be long zero-gde of a type kaul-, q.v.). See next
külos, à, om, io (2) 'hump, lump, pile’. Cf. WP I, 333 & 371 Skt. külam (1) 'hump'; OCS kyla (hernia, but see note on külos (1) & cf. Li. küla *swell- ing’; Latv. küle (1) ‘core of cabbage
külos, à, ios (3) ‘tuft, bunch, sheaf Ir. cúil, f. (2) ‘shock, tuft, cock’s comb’; G (short vowel) Holle, f. id.; Li. külýs, m. ‘sheaf’; Latv. kūla ‘rank grass’; kūlis ‘sheaf,
kulos, ios (4) “bent, twisted, lame’. Cf. kulio (2) Skt. cf. kunih, id. (fr. *kulnis); (Per. kul ‘crook- ed” is ambig. cf. qurtos); Arm. kuy, gs kyo “fold, pleat, strand’; Gk. kullós “b
kult-, kulter- (?). Cf. kulio (1), (2) & (3) Skt. cf. kutami, tr. ‘curve, curl’; Lat. cf. culter ‘knife’; OCS cf. klücajo, ati, denom. “dig, hoe’; Li. cf. kulteriu, ep ‘tap, hammer
(kum “towards, to”, see ku (1), and cf. ko-, kom. WP I, 326 Umb. kum. postp. ‘at, to’; Ir. (ambig.) chum (mutated: ‘towards, to"); Big. kám, id.)
küm- (?). Cf. kumb-, kumolos Alb. kum, v. ‘cram’; kümem ‘swell’; i kümur, adj. ‘chubby’; Ir. cf. cüm “body, shape’; cum-
587
aim, cümaim, v. ‘shape’; EME hum ‘arse’
kumbolos, à, ios (1) 'hump, lump, bulge; bulging vessel". WP I, 375. Cf. kumbos, kumo- los Ligurian (place-name) cf. Cumbels; Alb. (?) kümbulil, f. “plum”, the sense perh. influenced by Gk. kokk
kumbolos, om (2) *vessel'. Cf. kumbos. WP I, 375. Same as (1)? Gk. kümbalon ‘basin’; MHG cf. humpel- nache 'small boat
kumbo (kumboló) ‘resound’ Gk. cf. kümbalon (2) «cymbalon'; Alb. kum- boj ‘resound’; MLG humpeln, v. ‘sob’; Norw. (variant) humre ‘whinny’. (A variant of type *kum- appears in Alb. k
kumbos, à ‘hump, dome, hollow, basin, bel- lied pot'. (Variant: kumbhos) Ski. kumbah, -am, m. n. ‘knuckle-bone, club- head, chignon’ (variant: kumbháh “jar, pot, urn’; kumbhih, f. id.); Av
kumbulið (kumblið) lumber along, dawdle, potter MLG hümpeln ‘potter, dawdle’; LG humpeln limp’; Du. hompelen, id..; Cz. kublat *con- fuse’; kublat se ‘dally, dawdle, potter’; cf.
kumbolos, à, ios — kunkos, à, io
10
20
25
30
35
40
45
588
kubla, m. f. s. ‘idler’; Li. cf. (variant) kum- brinu, -ti, v. ‘amble along, be huddled’
(kumolos (1) and (2), see Supt: K)
kump- “bend, hump, crook’. Cf. WP I, 350, 373 & 376. (Cf. kumb- with some 
=== NR=335 ===
ambiguity in the Celtic forms) Skt. kumpah, adj. ‘with arm crooked'; MIr. comm ‘trunk, waist; W cf. cwman (2) ‘tump’; E dial. (ambig.) hum ('arse', cf. kum-); Du. (?) hom ‘milt’; Pol. kepa
(kundəlos, see kondulos)
kundos ‘stolid, stout, ponderous, stocky’ Arm. kunt & kund, gs knti & kndi, abl. -av “bald; squat, stocky’; Per. kund ‘blunt; stupid’; Hes. kundós ‘stolid, unwavering’; Fris. hont ‘
kungios, io (kungos, à) (1) ‘bulge, hump, mass'. Cf. kunkos, kunkolos & next Skt. kufijah ‘thicket’; Alb. cf. kungé ‘hump, swelling, dome'. Ambig. cf. kunk-); E hunk, hunch (according to dia
kungios (kung-) (2) (?) ‘corner’. Cf. kungios (1) Per. kunj (kung), id.; MDu. (alleged) honc ‘corner’; Du. Fris. honk, s. ‘home’. (Iso- phonic: E hunch “inspiration, idea; hunch- back’
kunkolos, is, à “ball, Jump, knob, peak’. Cf. kungios (1), kunkos, konkolos Alb. (ambig.) küngull, m. ‘marrow, pumpkin; Li. kufikulas ‘bubble’; kunkulýs, m. “bubble; post, pillar’; La
kunkos, à, io “lump, hump, bulge’. Cf. kung-, elc. Alb. (ambig.) kungë, f. id.; (R (ambig.) küca ‘heap, mass, crowd" preferably to kaukos (1), q.v); Li. cf. kunksoti, inf. ‘bulge; huddle to
589
*kunkio (?)). (The phonology of Oss. kunc, kuncä ‘bellows’ is uncertain)
kūnos ‘lump, swelling, body’. Cf. WP I, 367 Per. kün ‘arse’; Br. kin “bud, germ of wheat’; ON honn, gs hüns, m. (1) ‘knob’; Li. kūnas “body”; Latv. cf. künis (2) “abdomen
kuntsios (?), kundsios (?) ‘docked, short’. See kund- Skt. kunthah ‘blunt’; R kücyj ‘docked’; Cz. cf. kucel ‘clod, lump?
kūpā, os, is (1) ‘hollow, container, cup- shape, bonnet’. WP I, 372 Skt. kūpah ‘ditch, hollow’; Hiero-Hitt. kupas (queried: ‘tomb’); (?) Lyc. cf. gopa, gopu ‘tomb’; Myc. cf. kupera 
kūpā, os (2) ‘effervescence’. Cf. kupið (2) and kuprið. See next E (fr. Scots) hives ‘rash, eczema’; Cz. cf. ná- kyp ‘puff-pudding’
kupəlos (kupilos) ‘bulge, swelling, mass, pile; bulging, luxuriant. WP I, 373 Hes. cf. kúpalon (queried: ‘allocation, lot); Gk. cf. küpellon ‘bulging cup’; OHG hubil, MHG hübel, hubel, m. 
kupəros, å ‘hump, bulge; humped, bulging’. WP I, 373. Cf. kupolos Oss. cf. Kubír “bud; hill beside Kubár (*ball, lump’. Phonol. uncertain); Gk. küparos ‘butt’; MIr. cúar “bent; hoo
kupəst-, kupst- ‘hump, hollow’ Ir. cuas ‘hollow’; Li. kupstas ‘hillock’; kupstis, gs -čio ‘pile’
kupið (kupàio) (1) ‘browbeat, bully, bawl, - brawl
künos — kur-
10
20
25
30
35
40
45
590
Per. kübam, inf. küftan & kübidan “beat, bruise’; Gk. cf. (?) ktüápeo, synth. cpd. “crash, din’; Br. (ambig.) kia ‘jib, resist; EME to huff “bully, brawl, threaten, din, swagger’; P
```


## [2026-09-06T16:19:33.822Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==336' IEC.txt | cut -c1-400",
 "description": "Print IEC leaf 336 (p.590-591)"
}
```


### [2026-09-06T16:19:35.286Z] TOOL RESULT

```
��; kpic ‘make a fool of": Ukr. kpyty ‘jeer at
küpió (2) ‘surge, swell, stir, seethe’. WP I, 379 Skt. kupye, mp. ‘seethe, stir; desire’ beside (e- gde) Copàmi, tr. ‘stir; Av. kup-, id.; Lat. cupio, īre & Gre ‘desire’; Br. kia (ambig; suffer); EME huff, v. ‘swagger’; Norw. hovne, pp: hoven ‘swell’ beside (variant) hovere ‘exult’; OCS kypljo, kypëti ‘well up, rise, swell, abound’; Cz. kypět, inf. ʻeffervesce�
küpos (1) & (2), see küpa
küprió “shake up, stir, loosen; burst forth, effervesce, swell, be turgid’. Cf. WP I, 380 and kupið (2) Gk. kuprízo ‘blossom’; cf. küpris “Venus: love’; Umb. (?) kubra-, adj. (queried: ‘good’. E. Vetter: HbID: p. 167); Du. huiveren “shiv- er; Fris. huverje, id.; Norw. hovere ‘exult; Cz. kypřit, inf. ‘loosen’; kyprý, adj. “loose, friable’; Slovak kypret “become 
kur- (1) ‘round, curved’. Cf. kuruos, kor-. WP II, 568 Arm. (ambig.) kor (fcurved, bent; curve’. Cf. kor-); Gk. kur-tós, id. (Aeolic alleged ‘kurpós’ is a misspelling for kurtós); Ir. (ambig.) cor, m. (bend, turn’. See kor-); W côr, m. & f. (‘circle’. See kor-)
kur- (2) 'skin-covered boat, fishing-basket, creel’ Arm. kur, gs kri, i-st. ‘skiff; wooden bowl’; Gk. cf. kúrtë ‘creel’; LLat. (Gallo-Lat.) curu- cus, m. dim. ‘coracle’, cf. cur-cuma ‘straw bas- ket’; W cwrwg, pl. cyrygau ‘frame, carcase; coracle, boat’; Ir. cf. curach, m. & f. ‘coracle’
kur- (3) (kuros, om, iom, iə) ‘heat, fire, fuel, burning’. Cf. WP I, 418 Per. küre ‘fireplace, forge’; Go. haúri, n. ‘coal’; pl. haúrja ‘coalfire’; ON bert, gs hyrjar, m.
591
fire’; Li. küras ‘fuel’; kuriü, inf. kürti ‘light a fire’; Late kuru, kurt, id., beside kure 'heat- ing’; Skt. cf. külayami ‘singe’
kür- (4) ‘blind; deaf. Cf. quor- Per. kür (“blind”). But for Gk. porós: Pol. kary, see quór-. Per. -ü- is of ambig. origin); Li. cf. kuřčias, kurtas, kurtüs ‘deaf; Latv. cf. kufns, kuflis, kufls, kursls, id.; Finn. LW kuuro, id.; Est. LW kurt, gs kurdi, id.
kur- (5) (kurs-) ‘run, race, dash". WP I, 428. Cf. Kurs-. (Lat. & Gmc. are ambig.) Lat. curro, ére ‘run’; MHG hurren ‘dash, run’; OE hyrsian (queried) ‘run together’; ON (al leged) hurra “rush, rumble’; OE cf. hors, n., OFris. hors, Fris. hoars ‘horse’; Li. (*kur- in) kuriü, kort (3) ‘run, dash? beside kurnù, -éti, id.
kur- (6) (residual element of type quer- (1), q.v.) ‘do, make’ Skt. cf. kuru- (dual & plur. stem of kr- ‘do, make’); kuru! *do'!; kurvat (act. part. ‘doing’, fr. *kurunt- or *qurunt-); Li. kuriù, kürti (3) ‘build, create’; cf. küryba “creativity”
kür- (7) (residual element of type quor-, q. v.) “where, when, why'. WP I, 521-3 Alb. kur ‘when’; Lat. cür ‘why’; Ligurian (in Rumansch) cur ‘when’; Li. & Latv. kut, kur (^where'. Latv. also *whither")
küreió ‘get, acquire’. (Residual long-gde of type keuro (1), q.v.) Skt. kürayami ‘stea’; Gk. kuréo “get, find, achieve, reach"; W cf. cir, pl. -ion, m. ‘boon, benefit’; MHG hüren “hire, rent; OE hyran, id.; Du. huren, id.
kurguos (1) (? variant: kurquos in Gmc.) ‘filth, mucus, rheum’ Av. kuruyð "a disease’; Per. kiy "lippitude"; Arm. ambig. kork, i-st (“filth?. Cf. kork- (1)); OHG, OS horo, gs horawes ‘filth’; MHG be- horgen ‘defile’; OE horh, gs horwes ‘phlegm, filth’; horgian, v. ‘defile’; ON horr ‘snot’; Cz. krh, krhy, m. sg. & pl. “Tippitude?
kurguos, is (2) (?) “twist, turn, bend, bow. Cf. krgos Gk. kürbis, f. ‘revolving notice-board’; OCS *krügü beside korgü ‘prow’; R
```


## [2026-09-06T16:19:51.679Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN kur\"; grep -n \"kūra\\|kûra\\|kura 'Ofen\\|Ofen\\|Schmelzofen\" HRN.txt | head -20; echo \"=== PHD\"; grep -n -i \"kōrag\\|kūrag\\|kwlk\\|kūr \" PHD.txt | head; echo \"=== AFM كور\"; grep -n \"كور\" AFM.txt | head -20; echo \"=== PLA kur\"; grep -n \"kūr\\|Kūr\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20",
 "description": "Grep Iranian/Arabic refs for kur"
}
```


### [2026-09-06T16:19:51.768Z] TOOL RESULT

```
=== HRN kur
4003:Geldner, Studien I, 50, will auch np. cär 'Ofen* von
4732:526. däS 'Ofen*.
=== PHD
430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
=== AFM كور
1993:*< الخورة) 1 تعريب كور وهر )× 
2030:ابيض يشبه الصوف وورقها كورق التين ماثل | 
2161:وقار حيجكى 002 ܚ € .وال سود'منة ورقة كورق !÷ 46 ܕܐ العصفر له 
2628:1145 113 05 وزراتما بقو لما دستكور م 2 وهو 0 5 
2730:6 1 وهو كور اماد 
3487:إحكام ٠كل‏ ذلك نسبة الى سابور على غير القياس وهي كورة في بلاد فارس ( محيط 
3604:001 كان له مائة ولد من الذكور والاناث ٠‏ فني الليلة السابقة لليوم الذي ܐ 
3605:فيه الذكور بالاناث استوقدوا نيرا نا كثيرة وجعلوا ذاك : اليوم 3 انه 09 
3674:استعارت هي ܐܢܘܐ الفاظأ ܠܙܘ من الاراميّة منها 24 (ܩܢܢܐ) وكورتنا 
3947:* (السَجْوَري » الأحق معرب كور اي كلبي 
4140:داهر المذ كور ». ٠وعلدي‏ 0 الفارسي 2 10 ا اي الشاه لطيف او | ܐܚܐܘ 
4265:العقرب ٠و‏ بعد سنة في نفس اليوم الذكور ظهرت ثانية تلك الّة وفي فها قليل 
4852:* ( ܐܪܨ ܡܳܨ ) طائر ولم يزيدوا عليه ܐܕܚܐ فركور ܝ 
5305:0( تولّد الذكور .وأ كل ( 6 3 5( الاناث ٠‏ واليابس 
5678:الثبات قاكارة التصار سيت لاله يكور نا شتف يون راح اياي كتوق را 
6286:106 ) تعريب 3( اللبز. والمب المذكور سني به لاه 
7602:سكور 5,ه 
7992:كور 
=== PLA kur
```


## [2026-09-06T16:19:57.426Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7985,8005p' AFM.txt",
 "description": "Read AFM around كور"
}
```


### [2026-09-06T16:19:57.467Z] TOOL RESULT

```
ا 
ܗ ܙ ( 
كبتار ܢܙ ܙ 
15 ܀ ܚ ܙ 
ܢܬ )ܙ 
ܡ ܚܣ 
كنجر به"( 
كور 
كند برو )ܗܙ 
كندا وله 
ܠܥ( اسم 
كدان يمه 
7 ܘܢ 
كدلك ܨ ܙ 
6 
ل 0 


ܝ @ |{ | سد
```


## [2026-09-06T16:19:57.567Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T16:19:57.574Z] TOOL RESULT

```


```


## [2026-09-06T16:20:02.478Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%B1%D9%87",
 "prompt": "What does the Persian entry کوره say — meanings and etymology (Middle Persian, Arabic, Proto-Indo-European)? Quote the etymology section."
}
```


## [2026-09-06T16:20:02.949Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hearth",
 "prompt": "Give the full etymology of \"hearth\": Old English heorth, Proto-Germanic *hertho, PIE root. Quote it."
}
```


### [2026-09-06T16:20:07.396Z] TOOL RESULT

```
# Persian Entry for کوره

**Meaning:** The Persian noun کوره (kōra/kure) means "forge" or "furnace."

**Etymology:** Here's the exact etymology section:

> "From Manichaean Middle Persian 𐫞𐫇𐫡𐫃 (qwrg /⁠kūrag⁠/, "furnace, kiln"). A Semitic borrowing. Compare Classical Syriac ܟܘܪܐ (kūrā, "melting pot; furnace")."

The word originates from Middle Persian through a Semitic language source, not Proto-Indo-European.
```


### [2026-09-06T16:20:09.665Z] TOOL RESULT

```
# Etymology of "Hearth"

Based on the Online Etymology Dictionary, here is the full etymological path:

**Old English → Proto-Germanic → Proto-Indo-European**

The word traces back through these stages:

1. **Old English**: *heorð* meaning "hearth, fireplace, part of a floor on which a fire is made"

2. **Proto-Germanic**: *\*hertha-* meaning "burning place" (also found in Old Saxon, Old Frisian, Middle Dutch, Dutch, and German variants)

3. **Proto-Indo-European**: *\*kerta-*, derived from the root *\*ker-* (3) meaning "heat, fire"

**Direct Quote:**
"Old English _heorð_ 'hearth, fireplace, part of a floor on which a fire is made,' also in transferred use 'house, home, fireside,' from Proto-Germanic _\*hertha-_ 'burning place'"

The semantic evolution moved from the literal physical fireplace to encompassing the broader concepts of home and domestic life, reflecting the cultural importance of the hearth in ancient societies.
```


## [2026-09-06T16:20:20.189Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD kwrg\"; grep -n \"kwlk\\|kūrag\\|kwrg\" PHD.txt PHD_mackenzie.txt | head; echo \"=== NYB\"; grep -n \"kūrag\\|kwrg\\|kūr \" NYB_vol2_glossary.txt | head; echo \"=== AFA kur\"; grep -n -i \"kūrā\\|kura\\b\\|Schmelzofen\" AFA.txt | head -10; echo \"=== AKD\"; grep -n -i \"kūru\\|Ofen\\|kūrā\" AKD.txt | head -10",
 "description": "Grep for Middle Persian kurag and Semitic kura"
}
```


### [2026-09-06T16:20:20.278Z] TOOL RESULT

```
=== PHD kwrg
PHD.txt:430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
PHD_mackenzie.txt:3349:kullag [kwlk ] locust.
PHD_mackenzie.txt:3361:kurkum [kwlkwm] saffron.
PHD_mackenzie.txt:3362:kurrag [kwlk' I N -a] foal, colt.
=== NYB
=== AFA kur
=== AKD
362:Zu  Schmelzofen  s.  unten  S.  32  unter  kdru.
446:akk.  atünu,  tdünu  Ofen  :  >  aram.  'attüncl,  hdtönä  O  arab.  'attün., auch  'atCin,  äth.  "ettön).  akk.  tinüru  Ofen  :  >  aram.  tannfträ  (^
448:kuru  u.  klru  Ofen,  Herd,  Schmelzofen  (vieU.  <^sum.  gir)  :  >  hebr.  ki^(r u.  Du.  kirajim,  aram.  ktträ  O  arab.  kür  u.  klr,  äth.  kaur,  auch  armen. k'urai).  akk.  kanünu,  kinünu  Kohlenbecken,  Herd  (viell.  <^  sum.
563:dann  freilich  fi-üh,  hebr.  'ripä  backen  (>>  ägypt.  'pt  Gebäck),  ''ojy'  Bäcker, und  dann  auch  arab.  tnifan,  äth.  ntöfet  Ofen.
974:phalt^ :  >  hebr.  Icöper  Gen.  6,14,  aram.  hiprä  O  arab.  kufr,  sowie armen.  fe«pr,  falls  nicht  direkt  <[  akk.).  Ygl.  noch  unten  zu  hipr7hi. Da  akk.  Mm  Ofen  (s.  oben  S.  32)  speziell  gerade  vom  Asphalt-,  Pechofen des  Schiffers  gebraucht  wird,  wäre  es  nicht  unmöglich  daß  :  >  syr.  und jüd.-aram.  qträ^  Asphalt,  Pech  (>>  arab.  qlr  und  qär);  desgl.  dann  aber wohl  auch  aram.  gir,  gträ  Kalk  O  wohl  späthebr.  gtr,  sowie  arab.  gajjär, aber  auch  glr,  auch  südarab.  gjr  und  äth.  in  gajjara  tünchen).
```


## [2026-09-06T16:20:31.632Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%88%D8%B1%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for کوره, including any origin tag in brackets such as [ع.] or [په.]. Also quote any other dictionary entries giving the origin."
}
```


## [2026-09-06T16:20:32.336Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Krishna",
 "prompt": "Give the etymology of English Krishna: Sanskrit कृष्ण (kṛṣṇa) 'black, dark', Hindi, and any PIE reconstruction. Quote it."
}
```


### [2026-09-06T16:20:39.954Z] TOOL RESULT

```
# کوره - فرهنگ معین Entry

From **فرهنگ معین** (Mo'in Dictionary):

"ده ( ~ . دِ ) (اِمر. ) ده کم جمعیت که چندان آبادی نداشته باشد. (رِ ) (اِ. ) بخش ، قسمتی از مملکت . خره و خوره هم گفته می شود. ( ~. )(اِ. )آتشدان ، تنور، اجاق سرپوشیده"

This entry presents three main definitions: a small, sparsely populated settlement; a territorial division or region; and a heating apparatus such as a furnace or covered cooking oven.

**Other Origin References:**

The **لغت نامه دهخدا** (Dehkhoda Dictionary) notes historical linguistic connections, referencing Pahlavi "کورک" (oven/furnace), Akkadian "کورو," and comparisons to Gilaki "کوری" (clay stoves).
```


### [2026-09-06T16:20:40.073Z] TOOL RESULT

```
# Etymology of English Krishna

**Sanskrit Origin:**
The word comes from Sanskrit कृष्ण (kṛṣṇa), meaning "black" or "dark."

**Proto-Indo-European Reconstruction:**
According to the etymology tree provided, the Sanskrit term traces back through Proto-Indo-Iranian *kr̥šnás to the Proto-Indo-European root *kr̥snós, also meaning "black."

**Direct Quote:**
"Borrowed from Sanskrit कृष्ण (kṛṣṇa)."

The etymological path demonstrates that Krishna's name is fundamentally connected to the concept of darkness or blackness, reflecting descriptions of the deity in Hindu tradition.
```


## [2026-09-06T16:20:49.194Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN cardah\"; grep -n \"cardah\\|čardah\\|schwärzlich\" HRN.txt HUB.txt | head -10; echo \"=== ARY کوره / کره\"; grep -n \"کوره\\|چرده\\|کرسنه\" incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Horn/Hubschmann/Aryanpur"
}
```


### [2026-09-06T16:20:49.253Z] TOOL RESULT

```
=== HRN cardah
HUB.txt:9739:p. 97, Nr. 968. Dazu g. mam so cardah *Vollmond* ZDMG.
=== ARY کوره / کره
6482:چرد چرده (به چم ۲۳۱۸
```


## [2026-09-06T16:20:50.649Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CC%A5snos",
 "prompt": "Quote the reconstruction page for PIE *kr̥snós 'black': descendants (Sanskrit kṛṣṇa, Old Prussian kirsnan, Proto-Slavic *čьrnъ) and any notes on the root."
}
```


### [2026-09-06T16:20:52.509Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T16:20:55.479Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6455,6500p' incoming/ARY/ARY_pages.txt",
 "description": "Read Aryanpur around چرده"
}
```


### [2026-09-06T16:20:55.525Z] TOOL RESULT

```
گوتیک (0077716): 5دک پسگشت‌ها ومدررسممرلرم ای
ساکسونی کهن (2420۸0 ۰:02 85۸8۸ ار رن ۳
آلمانی کهن ((08704۸ 07 ا0): 4 ‎ )8۸35(‏ - 1
5۸8۸ 130 نققق/(ما05
آلمانی (0872/0۷): دز ان 5 (قا[٩‏ بلاه) :25/215
انگلیسی کهن (للدلا80 010): ۰ 7ت85۸ 452 ملاط
انگلیسی (6(/01757): اد رنه 8 (75ت8۸) :010/5
دانمارکی (0۸۸۷]8): 8 3 (8۸38) +57
سوئدی (7ل8(7/8075): 5۸۸ برهان قاطع : ۶۸۳۸
نروژی (۸/08۲۷501۸/4): ی لغت‌نامه دهخدا: ۸.۹۲
یادداشت:
چم این واژه در زبان‌های ژرمنی: مرهم؛ ضماد.
چم این واژه در زبان پهلوی؛ ملایم» نرم؛ لیز,
ارستایی (475374/۷): ۲13۸7180 ,۲13۸30 فریزی کهن (۸فا5ل7۶ (0): :۱
کردی (2.0/5[7)): و دش انگلیسی کهن (8۸701/370 01.0):
تخاری ۸ (۸4 (۸ل1۸7ل707): بلق6اتا 8 1807 117807701
تخاری 8 (8 7(فلق7۸ل70): ۰ کلفعا0 ۴ انگلیسی (8(015[4): 0
سانسکریت (84(/5877): دانمارکی (۵۸/88): با
ففقکلفتت ,کفنعکتین سرئدی (3780/57): انا[
ارمنی (4۸/8//14(۷): ۸51۸3۸6[ ,۲۸3 نروژی (708۷201۸(۷): بالا[11
بونانی 078810): ۰ 666108 ,1061-08 هلندی (لع07): ۳
لاتین (7100ا): اد 1 لد8 ره اسلاری کهن (۷16ه5 2770867 طا0):
ایسلندی کهن (/70104۸۸(م5 صا0): ر ۱
01 با1778 لهستانی (/۳0(5): ۰ ۴۳۵1۵60 ,8010
نورس کهن (20898 010): 11701 بآ17۷8 روسی (7535141): ند دک
[pdf page 220]
نج
چرد چرده (به چم ۲۳۱۸
چکه (2807): 00
صربی (58881۸/1): ۵۵ ۰ | پسگشت‌ها ره رش دادن
برهمی (80715(41۸00): ما0 ۶080/0
اسلوا کی (851-0140): 00 40 ۲525 :80/2
لبتوانی (1۸۸للهنا727ال): 8اه :ما05
پروسی کهن ((2-554 010): ۰ 151۸۲ 5 (قفتل) 28 0۱۵)
ایرلندی کهن (ل5ل#ا صا0): ساناح 71225 لاه
آلبانی (لماالمقلم: 587 1 (ل۷36) :00/5
9 ۷۲88 :7 ۱
9 م85 ۸/20
برهان قاطع + هم
بادداشت,
چم این واژه در زبان ارمنی؛ گردش» دَوّران.
چم این واژه در زبان بونانی و لبتوانی: دایر,
چم این واژه در زبان لاتین: کشت کردن,
پهلوی (1اماتله): ی ۹ اسلاوی کهن (16/ما5 بل#ناتل) صا0):
سانسکریت (5۸4۸/57): ادن
۸ ,1۸۸7۸ روسی (878914/۷): ادن
```


## [2026-09-06T16:21:03.601Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN ceramic\"; grep -n \"ceramic\" KLN_1966.txt | head -3; echo \"=== KLN carbon\"; grep -n \"^carbon\\|carbon, n\\.\" KLN_1966.txt | head -3; echo \"=== KLN cremate\"; grep -n \"cremate\" KLN_1966.txt | head -3; echo \"=== KLN hearth\"; grep -n \"hearth, n\" KLN_1966.txt | head -3",
 "description": "Grep Klein for the four English words"
}
```


### [2026-09-06T16:21:03.698Z] TOOL RESULT

```
=== KLN ceramic
5067:bisporous,  adj.,  having  two  spores  (bot.)  —  A hybrid  coined  fr.  L.  pref.  bi-,  ‘twice’,  and  Gk. GTiop&,  ‘sowing,  seed’  (see  bi-  and  spore).  The correct  form  is  disporous  in  which  both  elements are  of  Greek  origin.  For  the  ending  see  suff.  -ous. bisque,  n.,  unglazed  porcelain  (ceramics).  —  Cor¬ ruption  of  biscuit.
7002:ceral,  adj.,  pertaining  to  wax.  —  Formed  with adj.  suff.  -al  fr.  L.  cera,  ‘wax’.  See  cere,  n, Ceramiaceae,  n.  pi.,  a  family  of  algae  ( bol .)  — ModL.,  formed  with  suff.  -aceae  fr.  Ceramium. ceramiaceous,  adj.  —  See  prec.  word  and  -aceous. ceramic,  adj.,  i)  of  pottery;  2)  of  ceramics.  — Gk.  y.Epxjxtxop,  ‘of  pottery,  made  of  earthen¬ ware’,  fr.  xEpauop,  ‘earthen  vessel,  jar,  potter’s clay,  pottery’,  a  pre-Hellenic  word  derived  from a  language  of  Asia  Minor  and  not  cognate  with L.  cremdre,  ‘to  burn’.  See  Kretschmer,  Glotta,
7004:ceramics,  n.,  1)  the  art  of  making  pottery,  earth¬ enware,  of  porcelain,  etc.;  2)  objects  made  of any  of  these  materials.  —  See  prec.  word  and  -ics. Ceramium,  n.,  a  genus  of  red  algae  (bol.)  — ModL.,  fr.  Gk.  xepxpuov,  dimin.  of  xspajroq, ‘earthen  vessel,  jar’.  See  ceramic, cerargyrite,  n.,  a  synonym  of  hornsiher.  — Com¬ pounded  of  Gk.  x.Epa;,  ‘horn’  (see  cerato-), apvjpci;,  ‘silver’  (see  argyro-),  and  subst.  suff. -ite.
=== KLN carbon
4928:carbonate.
=== KLN cremate
7686:Cineraria,  n.,  a  genus  of  plants  of  the  aster  family (bot.)  —  ModL.,  fr.  L.  cinerarius,  ‘of  ashes’,  fr. cinis,  gen.  cineris,  ‘ashes’  (see  cinerary) ;  so  called from  the  color  of  the  down  on  the  leaves, cinerarium,  n.,  a  place  to  keep  the  ashes  of  the cremated  dead.  —  L.,  prop.  neut.  of  the  adjec¬ tive  cinerarius,  ‘pertaining  to  ashes’,  used  as  a noun,  fr.  cinis,  gen.  cineris,  ‘ashes’.  See  next word.
9625:‘I  hang  up,  suspend’,  which  is  rel.  to  xp^pv/iju, of  s.m.,  xprjpvop,  ‘precipice’,  and  perh.  cogn. with  Goth,  hramjan,  ‘to  crucify'.  Cp.  the  first element  in  cremnophobia,  cremocarp. cremate,  tr.  v.,  to  burn  to  ashes.  —  L.  crematus, pp.  of  cremare,  ‘to  consume  by  fire,  burn’,  rel. to  Umbr.  krematra,  ‘an  instrument  for  burning the  intestines’,  fr.  I.-E.  *ker-em,  an  -m-en- largement  of  base  *ker-,  ‘to  singe,  burn,  glow’, whence  also  L.  carbo,  ‘coal’,  OE.  heorp,  ‘hearth’. See  carbon,  hearth  and  verbal  suff.  -ate.  Gk. xfpocjioi;,  ‘potter’s  clay’,  is  not  cogn.  with  L. cremare  (see  ceramic).
9629:L.  crematus,  pp.  of  cremare.  See  cremate  and agential  suff.  -or.
=== KLN hearth
```


## [2026-09-06T16:21:13.484Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"carbon,  n\\|carbon, n\\|carbo,  ‘coal’\\|hearth,  n\" KLN_1966.txt | head -5; echo \"---\"; grep -n \"hearth\" KLN_1966.txt | head -8",
 "description": "Grep Klein carbon and hearth"
}
```


### [2026-09-06T16:21:13.553Z] TOOL RESULT

```
6509:carbolic,  adj.,  pertaining  to  carbon  and  oil.  — Compounded  of  L.  carbo,  ’coal’,  and  oleum , ‘oil’.  See  carbon,  oil  and  -ic. carbolize,  tr.  v.,  to  sterilize  with  carbolic  acid (chem.)  —  Formed  fr.  carbol-  and  -ize. carbon,  n.,  a  nonmetallic  clement  (chem.)  —  L. carbo,  gen.  -onis,  ‘coal,  charcoal’,  prob.  standing for  *car-dho  and  derived  fr.  E-E.  base  *ker-, ‘to  singe,  burn,  glow’.  See  hearth  and  cp.  cre¬ mate.  Cp.  also  carbonado,  Carbonari,  carbuncle. Derivatives:  carbon-ic,  adj.,  carbon-ize,  tr.  v. carbonaceous,  adj.,  1)  coaly;  2)  pertaining  to,  or containing,  carbon.  —  Formed  with  suff.  -ace- ous  fr.  L.  carbo,  gen.  -bnis,  ‘coal’.  See  prec.  word, carbonado,  n.,  a  broiled  piece  of  meat.  —  Sp.  car¬ bonado,  prop,  subst.  use  of  the  fern.  pp.  of  car- bonar.  See  next  word.
9625:‘I  hang  up,  suspend’,  which  is  rel.  to  xp^pv/iju, of  s.m.,  xprjpvop,  ‘precipice’,  and  perh.  cogn. with  Goth,  hramjan,  ‘to  crucify'.  Cp.  the  first element  in  cremnophobia,  cremocarp. cremate,  tr.  v.,  to  burn  to  ashes.  —  L.  crematus, pp.  of  cremare,  ‘to  consume  by  fire,  burn’,  rel. to  Umbr.  krematra,  ‘an  instrument  for  burning the  intestines’,  fr.  I.-E.  *ker-em,  an  -m-en- largement  of  base  *ker-,  ‘to  singe,  burn,  glow’, whence  also  L.  carbo,  ‘coal’,  OE.  heorp,  ‘hearth’. See  carbon,  hearth  and  verbal  suff.  -ate.  Gk. xfpocjioi;,  ‘potter’s  clay’,  is  not  cogn.  with  L. cremare  (see  ceramic).
17356:hearth,  n.  —  ME.  berth,  fr.  OE.  heord,  rel.  to  OS., OFris.  herth,  MDu.  hert,  Du.  hoard,  OHG.
18331:hydro,  shortened  form  of  1 )  hydropathic,  2)  hydro¬ airplane',  3)  hydraulic  power.  —  See  hydro-. Hydrohates,  n.,  a  genus  of  birds,  the  true  stormy petrel  (ornithul.)  —  ModL.,  compounded  of hydro-  and  Gk.  fiirr.c,  ‘threading  on’,  from  the stem  of  fialvav,  ‘to  go,  walk’.  See  -bates, hydrobromic,  adj.,  pertaining  to,  or  designating, an  acid,  HBr  (chem.)  —  Coined  by  the  French chemist  Joseph-Louis  Gay-Lussac  (1778-1850) fr.  hydro-  (short  for  hydrogen)  and  bromic, hydrocarbon,  n.,  a  compound  of  hydrogen  and carbon  (chem.)  —  Compounded  of  hydro-  (short for  hydrogen)  and  carbon, hydrocele,  n.,  an  accumulation  of  serous  fluid; esp.  dropsy  of  the  scrotum  (med.)  —  L.,  fr. Gk.  j Spoxr/.y;,  which  is  compounded  of  uSiop, ‘water’  (see  hydro-),  and  xfjXvj,  ‘tumor’.  See  -cele. hydrocephalic,  adj.,  pertaining  to  hydrocephalus.
---
1776:man  antiquity).  —  L.  aedilis,  fr.  aedes,  ‘a  build¬ ing,  sanctuary,  temple’,  orig.  ‘a  place  with  a hearth’,  fr.  I.-E.  base  *aidh-,  ‘to  bum’,  whence also  Gk.  aEffeiv,  ‘to  burn’,  at&pa,  ‘the  clear sky,  fair  weather’,  aE9x)p,  ‘the  upper  purer  air, ether’.  See  edify  and  cp.  ether, aegagrus,  n.,  the  wild  goat.  —  ModL.  fr.  Gk. xEyaypoc,  ‘wild  goat’,  which  is  compounded of  a (£,  gen.  alyop,  ‘goat’,  and  4ypto ‘wild’. See  aego-  and  agrio-.
5948:bustard,  n.,  a  large  bird  related  to  the  crane.  — A  blend  of  OF.  bistard  and  oustarde  (whence  F. outarde),  both  fr.  L.  avis  tarda,  lit.  ‘slow  bird'. Cp.  OProveng.  austarda,  Sp.  avetarda,  ‘bust¬ ard’,  and  see  aviary  and  tardy, bustee,  n.,  a  village,  slum  (Anglo-Ind.).  —  Hind. basti,  lit.  'an  inhabited  place',  fr.  OI.  vasati, ‘dwells’,  which  is  cogn.  with  Gk.  ecttixv,  ‘to  re¬ ceive  at  one’s  hearth",  Goth,  wisan,  OE.,  OHG. wesan,  ‘to  be’.  See  was  and  cp.  words  there  re¬ ferred  to.
6509:carbolic,  adj.,  pertaining  to  carbon  and  oil.  — Compounded  of  L.  carbo,  ’coal’,  and  oleum , ‘oil’.  See  carbon,  oil  and  -ic. carbolize,  tr.  v.,  to  sterilize  with  carbolic  acid (chem.)  —  Formed  fr.  carbol-  and  -ize. carbon,  n.,  a  nonmetallic  clement  (chem.)  —  L. carbo,  gen.  -onis,  ‘coal,  charcoal’,  prob.  standing for  *car-dho  and  derived  fr.  E-E.  base  *ker-, ‘to  singe,  burn,  glow’.  See  hearth  and  cp.  cre¬ mate.  Cp.  also  carbonado,  Carbonari,  carbuncle. Derivatives:  carbon-ic,  adj.,  carbon-ize,  tr.  v. carbonaceous,  adj.,  1)  coaly;  2)  pertaining  to,  or containing,  carbon.  —  Formed  with  suff.  -ace- ous  fr.  L.  carbo,  gen.  -bnis,  ‘coal’.  See  prec.  word, carbonado,  n.,  a  broiled  piece  of  meat.  —  Sp.  car¬ bonado,  prop,  subst.  use  of  the  fern.  pp.  of  car- bonar.  See  next  word.
7416:Derivauves:  chimer-ic,  chimer-ic-al,  adjs. chimere,  n.  —  See  chimer. chimney,  n.  —  ME.  chimenee,  fr.  OF.  cheminee (F.  cheminee),  fr.  Late  L.  (camera)  caminata, ‘(a  room)  provided  with  a  chimney',  fr.  L.  ca- minus,  ‘forge,  hearth’,  fr.  Gk.  xapivoc,  which  is rel.  to  xxpdipx,  ‘vaulted  chamber’,  fr.  I.-E.  base *qam-,  *qem-,  ‘to  bend,  vault’.  See  camera  and cp.  words  there  referred  to. chimpanzee,  n.  —  From  a  S.  African  native  word, chin,  n.  —  ME.,  fr.  OE.  cin,  rel.  to  OS.,  OHG. kinni,  ON  kinn,  MHG.  kinne,  G.  Kinn,  ‘chin’.
9625:‘I  hang  up,  suspend’,  which  is  rel.  to  xp^pv/iju, of  s.m.,  xprjpvop,  ‘precipice’,  and  perh.  cogn. with  Goth,  hramjan,  ‘to  crucify'.  Cp.  the  first element  in  cremnophobia,  cremocarp. cremate,  tr.  v.,  to  burn  to  ashes.  —  L.  crematus, pp.  of  cremare,  ‘to  consume  by  fire,  burn’,  rel. to  Umbr.  krematra,  ‘an  instrument  for  burning the  intestines’,  fr.  I.-E.  *ker-em,  an  -m-en- largement  of  base  *ker-,  ‘to  singe,  burn,  glow’, whence  also  L.  carbo,  ‘coal’,  OE.  heorp,  ‘hearth’. See  carbon,  hearth  and  verbal  suff.  -ate.  Gk. xfpocjioi;,  ‘potter’s  clay’,  is  not  cogn.  with  L. cremare  (see  ceramic).
9957:curette,  n.,  name  of  a  surgical  instrument.  —  F., fr.  curer,  ‘to  cleanse’.  See  cure,  v.,  and  -ette. Derivative :  curette,  tr.  v. curfew,  n.,  evening  signal.  —  ME.  courfew,  cor- few,  fr.  AF.  cotverfu,  covrefeu,  corresponding  to OF.  covrefeu,  lit.  ‘cover  the  fire’,  fr.  covre,  im- per.  of  OF.  covrir  (F.  couvrir),  ‘to  cover’,  and feu,  fr.  L.  focus,  ‘hearth,  fireside’,  in  Late  L..
12642:edify,  tr.  v.  —  ME.  edifien,  fr.  F.  edifier,  fr.  L. aedificare,  ‘to  erect  a  building,  to  build’,  fr. aedes  (or  aedis ),  ‘a  building,  sanctuary,  temple’, orig.  ‘a  place  with  a  hearth’,  and  -fiedre,  fr. facere ,  ‘to  make,  do’.  L.  aedes  derives  fr.  I.-E. base  *aidh-,  ‘to  burn’,  whence  also  Gk.  aM>et.v, ‘to  burn’,  aKfpa,  ‘the  clear  sky,  fair  weather’, aifhf]p,  ‘the  upper,  purer  air,  ether’,  Eh-apo?, ‘clean,  pure,  clear’,  OI.  inddhi,  ‘bursts  into ‘flame’,  idhah,  idhmah,  ‘wood  for  burning", OE.  ad,  OHG.  eit,  ‘funeral  pile,  fire’,  OIr.  aed, ‘fire’,  W.  aidd,  ‘heat,  zeal’.  Cp.  aedile,  Aethusa, Aludel,  estival,  estuary,  ether,  Ethiop,  oast.  For the  second  element  in  edify  see  -fy.
13617:into  -escere;  meaning  ‘to  begin  to  ...’.  See -esce  and  -ent. eschalot,  n.  —  See  shallot, eschar,  n.,  a  dry  crust  on  a  bum  (med.)  —  Late L.  eschara,  fr.  Gk.  irr/apa,  ‘hearth;  scar  from a  bum’.  See  scar,  ‘mark  on  the  skin’, escharotic,  adj.,  causing  an  eschar;  caustic.  — Late  L.  escharoticus,  fr.  Gk.  Err/apoixiy.oc,  fr. £<JXapa.  See  prec.  word  and  -ic. eschatology,  n.,  the  doctrine  of  the  last  things.  — Lit.  ‘the  study  of  the  last  things’,  fr.  Gk.  ea/a-rop, ‘furthest,  remotest,  last’,  and  -Xoyia,  fr.  -Xoyoc, ‘one  who  speaks  (in  a  certain  manner);  one who  deals  (with  a  certain  topic)’.  Gk.  gcr/a-ros is  a  derivative  of  if  (Boeotian  iq),  ‘out  of’ ;  see 2nd  ex-.  For  the  second  element  see  -logy. Derivatives:  eschatolog-ical,  adj.,  eschatolog- ist,  n.
```


## [2026-09-06T16:21:14.957Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%AD%CF%81%CE%B1%CE%BC%CE%BF%CF%82",
 "prompt": "Quote the etymology of Ancient Greek κέραμος 'potter's clay' — what does Beekes say? Is it Pre-Greek or from PIE *ker- 'burn'?"
}
```


### [2026-09-06T16:21:19.233Z] TOOL RESULT

```
# Etymology of κέραμος

According to the Wiktionary article, Beekes argues for a **Pre-Greek or Anatolian origin** rather than a PIE derivation. 

The exact statement reads: "Beekes argues for a Pre-Greek or Anatolian origin."

The article notes that while the word "has long been compared" to various potential sources (including Greek κεράννυμι "to mix" and Latin cremō), Beekes specifically rejected these connections in favor of a substrate origin. The etymology remains uncertain, as the article indicates the origin is "unknown."
```


## [2026-09-06T16:21:25.799Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17356p' KLN_1966.txt | cut -c1-1200; echo; echo \"=== LEW carbo\"; grep -n \"carbo, \" LEW_1910.txt | head -5; echo \"=== LEW cremo\"; grep -n \"cremo, \" LEW_1910.txt | head -5",
 "description": "Klein hearth + Walde LEW"
}
```


### [2026-09-06T16:21:25.871Z] TOOL RESULT

```
hearth,  n.  —  ME.  berth,  fr.  OE.  heord,  rel.  to  OS., OFris.  herth,  MDu.  hert,  Du.  hoard,  OHG.

=== LEW carbo
=== LEW cremo
```


## [2026-09-06T16:21:26.927Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/carbon",
 "prompt": "Give the etymology of carbon: French carbone, Latin carbo, PIE root. Also mention carburetor if present. Quote."
}
```


### [2026-09-06T16:21:32.882Z] TOOL RESULT

```
# Etymology of Carbon

**Origin Chain:** The term "carbon" traces back through French to Latin and ancient Indo-European roots.

**French:** Lavoisier coined the French term *charbone* in 1787, which was adopted into English in 1789.

**Latin:** The French word derived from Latin *carbonem* (nominative *carbo*), meaning "a coal, glowing coal; charcoal."

**Proto-Indo-European:** The Latin root traces to the PIE root *\*ker-* (3), signifying "heat, fire."

**Quote:** The element is described as a "non-metallic element occurring naturally as diamond, graphite, or charcoal" that originated from "Latin *carbonem* (nominative *carbo*) 'a coal, glowing coal; charcoal.'"

---

**Carburetor:** This device emerged later, in 1866, deriving from "carburet" (1795), itself formed from the "carb-" combining form of carbon plus a chemical suffix, referring to "a compound of carbon and another substance."
```


## [2026-09-06T16:21:36.995Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17355,17360p' KLN_1966.txt | cut -c1-1500; echo \"=== LEW\"; grep -n \"carbö\\|carbo\\b\" LEW_1910.txt | head -8; grep -n \"cremö\\|cremare\\|cremo\" LEW_1910.txt | head -8",
 "description": "Klein hearth full + LEW greps"
}
```


### [2026-09-06T16:21:37.071Z] TOOL RESULT

```
Derivatives:  heart,  tr.  and  intr.  v.,  heart-ed,  adj., heart-ed-ly,  adv.,  heart-en,  tr.  and  intr.  v.,  heart- en-er,  n.,  heart-y,  adj.,  heart-i-ly,  adv.,  heart-i- ness,  n.,  heart-less,  adj.,  heart-less-ly,  adv.,  heart- less-ness,  n.
hearth,  n.  —  ME.  berth,  fr.  OE.  heord,  rel.  to  OS., OFris.  herth,  MDu.  hert,  Du.  hoard,  OHG.
herd,  MHG.  hert,  G.  Herd,  ‘hearth’,  fr.  Teut. base  *her-,  corresponding  to  I.-E.  base  *ker-, ‘to  singe,  bum,  glow’,  whence  also  Goth,  hauri, ‘coal’,  ON.  hyrr,  ‘fire’,  OI.  kudayati,  kulayati, ‘singes’,  OSIav.  kurjq,  kuriti  s^,  ‘to  smoke’, Lith.  kuriii,  kiirti,  Lett,  kuru,  kurt,  ‘to  heat’, Lith.  kdrStas,  ‘hot’,  katstis,  ‘heat’,  Lett,  karsts, ‘hot’,  kafst,  ‘to  grow  hot’,  and  prob.  also  L. carbo,  ‘coal,  charcoal’ ;  see  carbon.  Cp.  cremate, heat,  n.  —  ME.  hete,  Fr.  OE.  hxtu,  hxto,  rel.  to OS.  hittia,  ON.  hiti,  Dan.  hede,  Swed.  hetta, OFris.  hete,  Du.  hitte,  OHG.  hizzea,  hizza, heizi,  MHG.,  G.  hitze,  ‘heat’,  OE.  hxda,  ‘hot weather’,  Goth,  heito,  ‘fever’,  and  to  OE.  hat, etc.,  ‘hot’,  see  hot.  It.  izza,  ‘wrath,  anger’,  is  a Teut.  loan  word.
heat,  tr.  and  intr.  v.  —  ME.  heten,  fr.  OE.  hxtan, ‘to  heat’,  fr.  hxtu,  ‘heat’.  See  heat,  n. Derivatives:  heat-ed,  adj.,  heat-ed-ly,  adv.,  heat¬ er,  n.,  heat-ing,  n.
heath,  n.  —  ME.  heth,  fr.  OE.  hied,  ‘heath  (land); heath  (the  plant),  heather’,  rel.  to  OS.  hetha, ON.  heidr,  Dan.  hede,  Swed.  hed,  ‘heath’,  OHG. heida,  ‘heather’,  MHG.,  G.,  Du.  heide,  ‘heath; heather’,  Goth,  haipi,  ‘field’,  and  cogn.  with Gaulish  ceto-  in  Gaulish-Latin  place  names  like Cetobriga,  etc.,  and  with  OIr.  dad,  OW.  colt, W.  coed,  OCo.  cuit,  Bret,  coet  (for  *kaito-), ‘wood,  forest’,  but  L.  bucetum,  ‘cow  pasture’, is  not  cognate.  Cp.  heathen,  heather. Derivative:  heath-y,  adj.
heathen,  n.  —  ME.  hethen,  fr.  OE.  hxden,  adj. and  n.,  rel.  to  OS.  hethin,  adj.,  ON.  heidinn,  adj., OFris.  hethen,  adj.,  MDu.  heidijn,  heiden,  Du. heiden,  n.,  OHG.  heidan,  MHG.  heiden,  adj., OHG.  heidano,  MHG.  heiden,  G.  Heide,  n., ‘heathen’,  Goth,  haipnd,  ‘heathen  woman’. These  words  prob.  meant  orig.  ‘dwelling  on  the heath’.  See  prec.  word  and  cp.  hoyden. Derivatives:  heathen,  adj.,  heathenish  (q.v.), heathenism,  heathenize,  heathenry  (qq.v.) heathendom,  n.  —  ME.,  fr.  OE.  hxdendom,  ‘pa¬ ganism’,  fr.  hxden.  See  prec.  word  and  -dom. heathenesse,  n.,  heathenism  {archaic).  —  ME. hethenesse,  fr.  OE.  hidennes,  lit.  ‘heathenness’. See  heathen  and  -ness.
=== LEW
```


## [2026-09-06T16:21:46.533Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT carbo\"; grep -n \"carbō\\|carbo :\" LAT.txt | head -5; echo \"=== LAT cremo\"; grep -n \"cremō\\|cremo :\" LAT.txt | head -5; echo \"=== SKT ceramic/carbon\"; grep -n \"^carbon\\|Ceramic\\|ceramic\" SKT.txt | head -5",
 "description": "Ernout-Meillet and Skeat greps"
}
```


### [2026-09-06T16:21:46.605Z] TOOL RESULT

```
=== LAT carbo
=== LAT cremo
=== SKT ceramic/carbon
2985:carbonado,  broiled  meat  (! Span,  carbonado,  rneat   broiled  o*tr —  Span,  carbon,  coal;  stc  abo^c.
```


## [2026-09-06T16:21:47.246Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cremate",
 "prompt": "Give the etymology of cremate: Latin cremare, PIE root *ker- (3) heat/fire. Quote."
}
```


### [2026-09-06T16:21:51.787Z] TOOL RESULT

```
# Etymology of Cremate

The word **cremate** is a back-formation from "cremation" (1851). It derives from Latin *cremare*, meaning "to burn, consume by fire," which traces back to the Proto-Indo-European root *\*ker-* (3), signifying "heat, fire."

**Quote:** "to burn, consume by fire" (also used of the dead), from PIE *\*krem-*, extended form of root *\*ker-* (3) "heat, fire."

This root appears across multiple Indo-European languages, including Sanskrit, Lithuanian, Old Church Slavonic, and Germanic languages, all relating to concepts of burning, heating, or fire.
```


## [2026-09-06T16:21:55.849Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"carbo\" LAT.txt | head -5; echo \"--- LEW\"; grep -n -i \"carbo\" LEW_1910.txt | head -5; echo \"--- LAT cremo\"; grep -n -i \"cremo\\|cremare\" LAT.txt | head -5",
 "description": "Case-insensitive grep for carbo"
}
```


### [2026-09-06T16:21:55.925Z] TOOL RESULT

```
7686:br&sas: carbones CGL III 598,7. Germanique. M.L.ia7G.
9154:Dionysius candenti carbone sibi adurebat capillum ; Verr.3,5,163, can¬
9855:carbo, -bnis m.: charbon de bois, produit de la combustion, souvent
9857:ardet dicitur; cum autem exstincta fuerit, carbo nominatur et Varr.
9858:R.R.1,7,8. De la: carbdnSrius, carbonesco (b.lat.). - Ancien, usuel.
--- LEW
11143:scarbon IT 500 scarp, scarpf IT 500 scart I 316 sceffil IT 484 scéhan I 127 sceidan II 494 scélah IT 492 scelifa II 486 scélo I 195 scepfan II 484 scéranl 170, IT 499, 505, 583 scerian I 170 scerdo I 166 scérf I 172 skéri IT 495 scérm I 274 scérn II 502 scéron IT 502 scérran I 173 skerti I 174 SCE&80, scéssoOn IT 494 sciba I 219, 357 skivaro I 134, 219 scidon IT 494 scilling II 487 sciluf IT 496 skinan II 485 scintula II 488 sciozan I 185, If 618 scira I 314 scirbt I 172, II 500 scirm I 274 seit IT 494 scwura IT 196 scizzan II 494 scobar I 311 scolan II 492 scont I 187 scorf II 501
--- LAT cremo
14308:Venant. Fort, et dans les gloses. Cf. peut-etre cremor. M.L.2294.
14451:cremo, -as, -aul, -atum, -are: bruler (noter le "pleonasme "igni
14452:cremare, dans CAsar BG I 4,1). Transitif, se dit snrtout des cadavres.
14466:cremor,- 5 rls m.: bouillie, d^coction. Atteste depnis Piante jns-
14470:apparenti? A cremo (cf. clamor, cl 5 * 5 ).
```


## [2026-09-06T16:21:57.885Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%B3%D9%86%D9%87",
 "prompt": "Is there a Persian entry کرسنه? What meaning and etymology (bitter vetch, Arabic كرسنة, Aramaic, Akkadian)? Quote whatever is there."
}
```


### [2026-09-06T16:21:59.691Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T16:22:03.517Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9855,9862p' LAT.txt; echo \"===\"; sed -n '14451,14462p' LAT.txt",
 "description": "Read Ernout-Meillet carbo and cremo entries"
}
```


### [2026-09-06T16:22:03.576Z] TOOL RESULT

```
carbo, -bnis m.: charbon de bois, produit de la combustion, souvent
joint A cinis , different de pruna, cf. Serv., Ae.11,788, pruna quamdiu
ardet dicitur; cum autem exstincta fuerit, carbo nominatur et Varr.
R.R.1,7,8. De la: carbdnSrius, carbonesco (b.lat.). - Ancien, usuel.
Panroman. M.L.1674-1676. Diminutif: carbunculus: morceau de charbon;
carboncle (sorte de sable); escarboucle; charbon (maladie = avGpa^)
M.L. 1677, et celt.: iri. carmocol; d'ou carbunculo = avOpaxito, et ses
derives.
===
cremo, -as, -aul, -atum, -are: bruler (noter le "pleonasme "igni
cremare, dans CAsar BG I 4,1). Transitif, se dit snrtout des cadavres.
Ancieh et nsuel. M.L.2309.
Derives et composes: cremium (snrtout an pl.): fagots ponr alInner
le fen, brontilles. Mot rustique, Colnm.12,19,3, tenuibus admodum
lignis, quae cremia rustici appellant, fornacem incendemus. Peut-etre
influence par gremia, de gremium "brass^e de bois"; cremdbilis; crema¬
tio, cremator; con-, de-, ex-, re-cremdre; turicremus (poet.).
Peut-etre d'un elargissement en -em- de la racine attest^e par
v-.isl. hyrr "fen", got. hauri "charbon", lit. kuriu, kurti "faire dn fen"
(v. sl. kuriti "chauffer" est un cansatif secondaire). Le mot semble
osco-ombrien, car 1'oabrien a le noa d 1 instrument krematra qui semble
```


## [2026-09-06T16:22:03.953Z] TOOL CALL #50: WebSearch

```json
{
 "query": "كرسنة kirsinna bitter vetch Aramaic Akkadian etymology Persian کرسنه"
}
```


### [2026-09-06T16:22:13.586Z] TOOL RESULT

```
Web search results for query: "كرسنة kirsinna bitter vetch Aramaic Akkadian etymology Persian کرسنه"

Links: [{"title":"كرسنة - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%83%D8%B1%D8%B3%D9%86%D8%A9"},{"title":"A DICTIONARY OF MODERN WRITTEN ARABIC - Page 23","url":"http://alhassanain.org/english/?com=book&id=1094&page=23"},{"title":"كرسنة In English - Translation and Meaning in English Arabic Dictionary of All terms Page 1","url":"https://www.almaany.com/en/dict/ar-en/%D9%83%D8%B1%D8%B3%D9%86%D8%A9/"},{"title":"Kersha","url":"https://en.wikipedia.org/wiki/Kersha"},{"title":"Bitter vetch","url":"https://en.wikipedia.org/wiki/Bitter_vetch"},{"title":"Studies in the Grammar and Lexicon of Neo-Aramaic - On the Origin of Some Plant Names in Ṣūrayt/Ṭūrōyo in Ṭūr ʿAbdīn","url":"https://books.openbookpublishers.com/10.11647/obp.0209/ch11.xhtml"},{"title":"Garshuni","url":"https://en.wikipedia.org/wiki/Garshuni"},{"title":"كرسنة - Translation Arabic English | arabdict Dictionary & Translator","url":"https://www.arabdict.com/en/english-arabic/%D9%83%D8%B1%D8%B3%D9%86%D8%A9"},{"title":"Phenotypic Diversity and Abiotic Stress Tolerance Among Vicia ervilia (L.) Willd. Accessions","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11990473/"},{"title":"Identification of Vicia ervilia Germplasm Resistant to Orobanche crenata","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7697931/"}]

Based on the search results, here's what I found about the etymology and linguistic connections for كرسنة (kirsinna/kirsanna) - bitter vetch:

## Etymology

The word has two possible explanations: it may come from Sanskrit कृष्ण (kṛṣṇa, "black"), making it a doublet of كُشْنَى (kušnā), which comes via Classical Syriac ܟܘܫܢܐ (kūšnā) and also appears in Akkadian as kiššanu. Alternatively, it may derive from Classical Syriac ܟܱܪܣܴܢܳܐ (karsānā, karsannā, "ventrose") connected to Proto-Semitic *kariś- ("paunch"), referencing the flatulence caused by eating this plant.

## Related Languages

The word is cognate with Old Armenian քրսամն (kʻrsamn), Armenian քուռուշնա (kʻuṙušna), Azerbaijani kürüşnə, and kürişnə.

## Botanical Reference

Kirsinna/kirsanna refers to a variety of vetch (botanical term). More specifically, bitter vetch refers to Vicia ervilia, an ancient grain legume crop of the Mediterranean region.

The search results provide documented etymological connections across Aramaic, Akkadian, Sanskrit, and Armenian languages, though the exact origin remains somewhat debated among scholars.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T16:22:26.671Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt; echo \"=== چرده\"; grep -n \"چرده\" MON_part1.txt MON_part2.txt | head -10; echo \"=== کوره\"; grep -c \"کوره\" MON_part1.txt MON_part2.txt",
 "description": "Grep Mo'in for چرده and کوره"
}
```


### [2026-09-06T16:22:26.739Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
=== چرده
MON_part1.txt:50136:چرد: 9:0 (- چرده - چرته] (ا.) رنگ» 
MON_part1.txt:50142:چرده: 4 [- چرته - چرد] (.) رنگ» 
MON_part1.txt:81876:سیاه‌چرده: (ند. 60۲۳02)66706-.5 (ص‌ مر .) 
MON_part1.txt:81904:چرده. (کذ.) بی آبرو» بی‌عزت. (کد.) 
=== کوره
MON_part1.txt:26
MON_part2.txt:31
```


## [2026-09-06T16:22:28.552Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%B1%D8%B3%D9%86%D8%A9",
 "prompt": "Quote the full etymology section of Arabic كرسنة (kirsinna) — Sanskrit kṛṣṇa, Syriac kūšnā, Akkadian kiššanu, Syriac karsānā, Proto-Semitic *kariś-, and the descendants (Persian, Armenian, Azerbaijani)."
}
```


### [2026-09-06T16:22:36.071Z] TOOL RESULT

```
# Etymology of Arabic كرسنة (kirsinna)

The word derives from multiple ancient language sources with interconnected etymological paths:

**Primary sources:** "From Aramaic כַּרְשִׁינָא (karšinnā) or Hebrew כַּרְשִׁינָה (karšīna)."

**Sanskrit connection:** The term traces to "Sanskrit कृष्ण (kṛṣṇa, 'black')" and represents "a doublet of كُشْنَى (kušnā)."

**Syriac pathway:** The etymology includes "Classical Syriac ܟܘܫܢܐ (kūšnā), also in Akkadian /⁠kiššanu⁠/" and alternatively "Classical Syriac ܟܪܣܢܐ (karsānā, karsannā, 'ventrose')."

**Proto-Semitic root:** The term connects to "Proto-Semitic *kariś- ('paunch')" due to digestive effects from consuming this plant.

**Related descendants:** Cognate forms appear across languages including Old Armenian քրսամն (kʻrsamn), Armenian քուռուշնա (kʻuṙušna), and Azerbaijani kürüşnə and kürişnə variants.

The word ultimately refers to bitter vetch (*Vicia ervilia*), with its name derived from the plant's notable physiological effects.
```


## [2026-09-06T16:22:40.471Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '50130,50150p' MON_part1.txt; echo \"=== کوره in part2\"; grep -n \"کوره\" MON_part2.txt | head -12",
 "description": "Read Mo'in چرده and find کوره"
}
```


### [2026-09-06T16:22:40.540Z] TOOL RESULT

```
چرخیدن: 6۳-0 (مص‌ل.) (چرخمد» 
چرخد» خواهد چرخید» بچرخ» چرخنده؛ 
چر خند۵. م. چرخاندن» چرخانیدن). ج 
زدن» چرخ خوردن» دور خود یا چیزی 
گردیدن؛ گرد گردیدن. 

چرد: 9:0 (- چرده - چرته] (ا.) رنگ» 
لون (مخصوصاً در چارپایان). 

چرد: 5:74 (.) جایی که چارچوب در خانه 
را بر آن کار گذارند؛ آستانه. 

چرده: 4 [- چرته - چرد] (.) رنگ» 
لون (عموما). رنگ چهره و پوست؛» ساه 
چر د9. 

چرس: 5 (.) سند» زندان. شگنحه» 
۳ 

جر س. 5 اقس. جر؛ چجریدن ] (.) 
چراگاه چهار پایان. 
=== کوره in part2
5267:کوره‌یزی (قاجار به). 
6686:لیکورهایی که راهبان مصرف می‌کنند بکار 
10642:(ص‌فا.) آنکه در کوره‌های آجریزی خشت 
18588:کسی که کاشی سازد؛ آنکه کاشی در کوره 
20013:کسر: ۲:9 [- کوره» ع. کبر. - قبر - 
21069:نیز مواد سوخت را در تنور و کوره ریزند. 
24376:کوره‌های دوب آهن و دیگر فلزات است. 
24378:کوره‌های مخصوص با جریان هوای کم 
25099:(00۳05) در کوره سدست می‌آبد) در 
27912:کوره: (۵-):۳ [- کورة: معر. خره] (ا.) 
27915:کوره: و 4 . کور] (.) آتشگاه 
27917:و کچ و امثال آن پزند. از کوره بدر (در)
```


## [2026-09-06T16:22:43.071Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27905,27930p' MON_part2.txt",
 "description": "Read Mo'in کوره entries"
}
```


### [2026-09-06T16:22:43.118Z] TOOL RESULT

```
تکریم سح ۰۵ به خا کث افتادن. 

کو ره. تاه )۱۸۳۷۸۱ )1( زمینی را 
گویند که آن را سیلاب کنده باشد و بدان 
سبب گودی‌ها در آن بهم رسیده و پر کل و 
لای باشد. سبلاب. 

کوره: (۵-):۳ [- کورة: معر. خره] (ا.) 
شهر ستان ناحبه» ج. . کور. 

کوره: و 4 . کور] (.) آتشگاه 
آهنگری و مسگری. جابی که در آن خشت 
و کچ و امثال آن پزند. از کوره بدر (در) 
بردن: (عم.) بسیار عصبانی کردن. از کوره 
در کردن کسی را: (عم.) عصبانی کردن. از 
کوره در رفتن: (عم.) سیار عصبانی شدن. 
کوره‌یزخانه: (۰-۳22-00)0 (امر.) جایی 
که در آن خشت خام را پزند و آجر کنند و 
با گچ و آهک در آن پزند. 

کوره‌ده: "اده-.: (امر.) ده کوچک و کم 
اباد. 

کوره‌راه: ۲-۱ (امر.) راهی که ناراست و 
ی
```


## [2026-09-06T16:22:57.311Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c $'\\f' MON_part1.txt MON_part2.txt; grep -n \"pdf page\" MON_part1.txt | head -3; awk 'BEGIN{RS=\"\\f\"} {n++} END{print \"leaves:\",n}' MON_part1.txt",
 "description": "Check MON page markers"
}
```


### [2026-09-06T16:22:58.998Z] TOOL RESULT

```
MON_part2.txt:0
MON_part1.txt:0
leaves: 1
```


## [2026-09-06T16:23:07.240Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN Schmutz\"; grep -n \"Schmutz\" HRN.txt | head -15; echo \"=== HUB Schmutz\"; grep -n \"Schmutz\" HUB.txt | head -10; echo \"=== MON کره چرک\"; grep -n \"کره:\" MON_part2.txt | head -20",
 "description": "Grep Horn/Hubschmann/Mo'in for dirt words"
}
```


### [2026-09-06T16:23:07.311Z] TOOL RESULT

```
=== HRN Schmutz
794:lat. Inf um; air. loth 'Schmutz'; lit. lutyna-Sy lutgn^
5695:rim *Schmutz\
8043:927»»*« gil 'Schmutz. Lehm'.
8208:947. güh *Schmutz, Kot'.
8209:aw. güd-a- in güSö.lvareta- *im Schmutz kriechend*,
=== HUB Schmutz
7219:Ind. 89, 92 = zd. pa&ana-; guh *Koth, Schmutz, phi. guh
=== MON کره چرک
15460:۳ ص ۱۹۵؛ فرع. سج.) قوت مفکره: (فد. 
22152:کرکره: (۵-)۵۲۲۵۲۸ (۱.) قسمی برد چوبی 
22617:کره: «ها() چ رکد» وسخ. پوست دست و 
22631:کره: (1۵۳)۵ [- کرو - کری] (.) خاناة 
22635:کره: (9)9:ه [- معر. کرج] (ا.) زنگار 
22639:کره: (6-)121۲2 [ع. کرة] (.) بار» دقعه 
22645:کره: (معما (ع. کرة] (.) گوی (اعم از 
22657:کره: 10۳ [ع.] (مسص م.) نایسند داشتن» 
52034:مذاکره: (16۲6-) ۱2102211۵۲2 [ع. مداکرة] 
56275:مستکره: ۱( [ع.) (امف.) زشت 
56277:مستکره: ۱۱05۳۵ [ع.] (افا.) زشت و 
63872:مکره: دا [ع.] (افا.) اکراه نماینده» 
65882:مناکره: (ع۲ع)مفقنهه [ع. منا کرة5] 
78992:نکره: (۵-)د۵۵۲ه [ع. . نکر ة (رص.) ناشناس. 
82557:نیم‌کره نیمکره: (۵-)0۲۵-.۲ [ف. غ.]
```


## [2026-09-06T16:23:09.898Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22615,22625p' MON_part2.txt",
 "description": "Read Mo'in کره entry"
}
```


### [2026-09-06T16:23:09.947Z] TOOL RESULT

```
آنچه که به شکل گوی بود. 

کره: «ها() چ رکد» وسخ. پوست دست و 
پا و اعضا که به سیب کار کردن بسیار سخت 
گردد و پینه بندد. 

کر ۵: (ند. -1۵۲۵)۲27 ((.) چربیی که از چرخ 
کردن شیر در چرخ‌های کره گیری حاصلن 
شود و یا پس از قلم زدن دوغ جمع گردد و 
آن را جمع کنند و به مصرف رسانند. گاهی 
نیز کره را از خامه تهیه کنند بدین طریق که
```


## [2026-09-06T16:23:19.508Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3",
 "prompt": "Quote the etymology of Sanskrit कृष्ण (kṛṣṇa) 'black': the Proto-Indo-Iranian and PIE reconstruction, and cognates such as Old Prussian kirsnan, Old Church Slavonic črъnъ, Lithuanian keršas."
}
```


## [2026-09-06T16:23:21.254Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ceramic",
 "prompt": "Give the etymology of ceramic: Greek keramikos, keramos 'potter's clay', and what it says about the PIE root or possible non-IE/Pre-Greek origin. Also mention French céramique if present. Quote."
}
```


### [2026-09-06T16:23:25.562Z] TOOL RESULT

```
# Etymology of Sanskrit कृष्ण (kṛṣṇa)

**Proto-Indo-Iranian and PIE Origin:**
The word derives from "Proto-Indo-Iranian _[\*kr̥šnás](/wiki/Reconstruction:Proto-Indo-Iranian/kr%CC%A5%C5%A1n%C3%A1s)_ ("black"), from Proto-Indo-European _[\*kr̥snós](/wiki/Reconstruction:Proto-Indo-European/kr%CC%A5sn%C3%B3s)_ ("black")."

**Selected Cognates:**

The article lists several related words across ancient languages:

- **Old Prussian:** "kirsnan" (black)
- **Old Church Slavonic:** "чрънъ" (črŭnŭ, "black")
- **Lithuanian:** "kir̃snas"

Additional cognates include Russian чёрный (čórnyj), Bulgarian черен (čeren), Polish czarny, and Czech černý—all meaning black or dark-colored variations of the same ancient root.
```


### [2026-09-06T16:23:29.095Z] TOOL RESULT

```
# Etymology of Ceramic

The word **ceramic** derives from Greek *keramikos*, stemming from *keramos*, meaning "potter's earth; tile; earthen vessel." As the source notes, this Greek root "perhaps from a pre-Hellenic word."

## Uncertain Origins

Scholars disagree on the ultimate source. The document indicates: "No certain etymology" exists. Some propose connections to Latin *cremare* ("to burn"), though this is disputed. Beekes finds a link to *kerasai* ("to mix") "semantically not very convincing" but acknowledges semantic merit in proposed connections to verbs meaning "to burn, glow." The consensus suggests this technical term may have "Pre-Greek (or Anatolian)" origins rather than Indo-European roots.

## French Influence

The modern spelling was influenced by French *céramique* (1806). The related noun *ceramics*, referring to "art of making things from clay molded and baked," was first documented in 1857.
```


## [2026-09-06T16:23:36.561Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/کوره\" \\\n \"https://www.etymonline.com/word/hearth\" \\\n \"https://en.wiktionary.org/wiki/Krishna\" \\\n \"https://en.wiktionary.org/wiki/كرسنة\" \\\n \"https://en.wiktionary.org/wiki/κέραμος\" \\\n \"https://en.wiktionary.org/wiki/कृष्ण\" \\\n \"https://www.etymonline.com/word/carbon\" \\\n \"https://www.etymonline.com/word/cremate\" \\\n \"https://www.etymonline.com/word/ceramic\" \\\n \"https://abadis.ir/fatofa/کوره/\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 258, roots Ker 4 / Ker 5\" 2>&1 | tail -2\ndone",
 "description": "Archive all web sources"
}
```


### [2026-09-06T16:23:44.183Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4c4f1183017a2476.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fece17790dbc610e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ea65b2ead42a81c6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/18090bdd08b4ff94.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/535099b6d7f55eba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f0651ea6fd49163.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3f6709cee4c53ef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c01dbcc6f354fb4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/52c202875cc56450.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/698d706611840b9b.txt
```


## [2026-09-06T16:24:48.471Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c258_n2.png"
}
```


### [2026-09-06T16:24:48.610Z] TOOL RESULT

```

```


## [2026-09-06T16:24:48.608Z] INPUT

[Image: original 2200x440, displayed at 2000x400. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:24:54.316Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT kirs\"; grep -n -i \"kirs\\|black\" KNT.txt | head -15; echo \"=== BRT\"; grep -n -i \"kirsna\\|karsna\" BRT.txt | head -5; echo \"=== NYB dung\"; grep -n -i \"dung\\|Mist\" NYB_vol2_glossary.txt | head -8",
 "description": "Kent / Bartholomae / Nyberg checks"
}
```


### [2026-09-06T16:24:54.402Z] TOOL RESULT

```
=== KNT kirs
4941:azíaina- adj, with kdsaka-, ‘turquois’ (so Bleichsteiner, WZKM 37.103-4, and Konig, Burg- bau 63-4, but considered dubious by Hinz, ZDMG 95.235-6; hardly ‘gray amber’, with Hz. AMI 3.05—7, ApI 232; not ‘hematite’, with Scheil 21.29- 30): Av. arSaéna- ‘dark-colored’, borrowed in Gk. Порто “Atevos ‘Black Sea’ (‘in-hospitable’, by Gk. popular etymology, and euphemistically changed to Еф о), from neg. a- + z&atna-, cf. Av. xSaéta- ‘shining’ (§102, 5147.1). azšaina nsm. DSf 39.
=== BRT
4764:•  j.  a-maräant-*'  Adj.  (fem.  °santT-)  nicht sterbend;  unsterblich':  yat  kirsnavqn  .  . ahüm  .  .  'hnhm  Yt  ig.  ii;  —  yaj  k)T}- naot .  .  *'/an/a  (AD.)  fasu  vlra  Y.p.4;  — bun  ga?SsA  *°sanlii  yä  a^ahe  Vt  /p.  1 2 ;  —
7538:•  j.  'äzäta-  m.  FJ<I.  eines  Gläubigen:  'Iahe karsnayanahe  asaonB  Yt/J,  108.  I
9152:—  afrin>in  ifmiavät  Az,  2;  Vyt.  J  (wo k^rjnofilAi);  —  va!s  paoirlm  miirsm k^rmaoiti  V.J.3;  —  iian  (sd.)  hä  iiisläta iiryatii>  Yt.  10.  109;  —  ^fö  0ng  /rS.ga pa^mSng  hucistöis  (sd.)  *carat  (Konj.)9> ; \.4li.a,\  —  k(ii:a..  zarjm  (sd.)  (ar,l»r'>' kaca  xsmal  Y.  44. 1 7.  a)  mit  Adv,  statt Akk.:  II  ya^äsäm  hacärnJ"  d^ahyJ'  ara^^J *aJh/riavaya"li '^  Bh.  j.  S;  —  <iai  yimd ara'ia  k^rjfiaat ya'>a..'V.-J.$2.  h)  mit Inf.  als  Obj.:  yaf  kirsnaot..  c^airyqn  (sd.) 3far?i>m  ajyamnum  Y.'y.4; 75,16  {k}rma-\ rJni).  S- S.  2a)  mit  sksfuiem  'etwas' (Akk.)  zerbrechen,  zerstören';  shnd?m  (sd.) sl  mauö  k^nnüi'A  Y.  i/.  28.  b)  ;  mit züre^  'Jemandem  (Akk.)  Unrecht  tun': naiy  "sakurim  .  .  zür,^  (sd.)  akunavam Bh,4. 13.  c)  mit  ntazdam  Med.  'sich etwas  (Akk.)  ins  Gedächtnis  rufen,  recor- dari':  inasdqmcä  büirüä  (s.  bei  5)  ktrshul ,  .  xrapaitl  (sd.)  hyat  ahmat  aibi  Y. 40.  1 .  3a)  'Jemanden,  etwas  (Akk)  iiin- schaffea  zu  -,  verbringen,  versetzen  in  -'; a)  mit  Lok.  des  Ziels:  II  pasäva^dis a''ura^mazd<l  maiiä  dastayi  (sd.)  akunaus Bh,  4. 4,  1-)  mit  Lok.  eines  Nom.  act. zur  Umschreibung  des  Verbs:  vispqm  .  . taiiüm  ayao^dsta  (sd.)  k)rJiiaoiti  V.<V,4o;
9170:(blossem)  Opt,  'machen,  bewirken,  dass . .': yö  kirsnavat  yim  yazaite  mi^nm , .  xsttBlä albHtS  hyät  "der  bewirkt,  dass  M.,  den er  verehrt,  zufrieden,  ungekränkt  ist"  Vt. lo.iao.  Unklar:    ksr^take  Vyt.47;  —
9314:'"f  ^V  ~  ""'■"'"'^ -iT' ^^'  l,^^"  .         or    '•  J-   karsna-   m.   EN.   eines  Gläubigen: Ableit.  —  ai.  vgl.  kalpa-  m.  'Ritus'.   —    Pfi. :  i         ■      +  ,  ^        i     /  j  i        ■•       ,    « j
=== NYB dung
19:The delay, however, has not been without its advantages, I think. During these ten years I have had time to scrutinize the texts to the last letter and to deepen my understanding of them. I have been able to correct mistakes and premature emendations. The long list of corrigenda is an evidence of this.
909:band [bnd] tie, band, bond; fetters 919. 34! (81? probably mistaken for bry<n> = brin, cf Mx ch. 279; Paz. is wanting); ~ + zēndān imprisonment, captivity 9°; ~ the snare of Death 6514-18; ca rād ka menčyan u gētīkān dänisn u kār-ākāhēh har 2 band 6 tč [i.e. xrat] patvast why are knowledge and skill of both the heavenly and the earthly beings (so) closely tied up with (dependent on) thee [the Wisdom]? 8811-12; the Skr. v. joins band with the preceding har 2: dvdvapi bandhau, but this is contradicted by 12017-18; cigön martömäan i andar gété band 6 mēnēyān patvast estet as men in this world are closely tied up with the heavenly beings. — Av. (926 sq.) banda- ; MPrth. bnd; bndys?n ‘prison’ (MHC); MPrs bnd (A-H II), bn = bann (S, A-H I), bnyst’n = bannistän < band- (A-H I); Paz. NP band. V. bastan.
1084:the apodosis: hakar ... šdyčt, amäh-ic 1122-233, ka-c tō dit ..., adak-ic to ... 759-19; 468; 5526. — 305: the ideogr. MH is a mistake for -ey = -ci.— 1. Av. OP «ca,
1113:— -küi < *käya- ‘regard, look’, cf Skr cäyati, -te ‘to notice, to observe, to be- hold’, käya- ‘goal, aim’ (not to be con- founded with käya- ‘body’); root kä-, v. ākāh, nikäh, and gukäi, in which the same alternations in the final are ob- served. — Neriosengh mistook the last element of —, which he found in the form -käh, for käh- ‘to diminish’, Paz. xäh-, hence his reading casm-xdhisn(itar) ; Skr. v. adarsaniyaltara).
1178:damistän [dmst?n'] winter 3711 and often; a dev 8573, 8612; created by the devs 103’; — year 778. — SW form of Av. (1699 sq.) zyam-, zom- (v. hazangrö-zim) + -stän; MPrs dmyst’n (A-H I); Paz. damastan ; but NP NW form: zamistän.
1272:dev [SYD’] demon, devil, of individual evil beings: Az, Damistän, Fraizist, Hesm, Zešt, v. these ws.; — commonly in pl.: ~ cas. rect. 1924, 451, 6917, used as voc. 4915; cas, obl. —-àn [ŠYD*-n', usually ŠYD*-n'] passim, used as cas. rect. 61?. 762; ~-dn ~ the supreme devil 4215; ~-dn dāt, v. dat. — Av. (667 sqq.) dačva-, OP daiva-; common Milr and NP.
1365:druyist [drwdst'] safe and sound, whole; right, exact, accurate: P2:9.10 (twice). 1418, 2222 etc. passim. — The letters are unmistakable in P2. Av. (782) drva- (= druva-); OP durwa- ‘firm, secure’, sup. *druvista-, whence in SW druyist
1607:Kurd. gewr ‘grey, iron grey, black- brown’ or ‘mottled’ (Kurdoev). On the other hand, the other great authority, al- Birüni, gives the name in the form dyzh-k’w (Chronol. 1043), evidently the copyist’s mistake for dbrh-k'w = BP davr-gäv, and in fact BdA 2295 (= BdJ 771° just quoted for gefr-) has as first element [ddpwl! for] davr (q.v.) In BdA 103° = BdJ 354, BdAntiā 7618 transliterates it gfr, but the authority of this text is poor.
```


## [2026-09-06T16:25:02.460Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN black\"; grep -n \"15\\.65\\|BLACK\" SYN.txt | head -5; echo \"=== WLD Bd1 kers\"; grep -n \"kers-\\|kṛṣṇá\\|kirsnan\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8; echo \"=== WLD Bd1 ker brennen\"; grep -n \"brennen, glühen, heizen\\|418\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5",
 "description": "Buck and Walde-Pokorny checks"
}
```


### [2026-09-06T16:25:02.543Z] TOOL RESULT

```
=== SYN black
25867:15.65 Buack
26646:2. Grk. uédas, xedauvds ‘black’ (15.65), also ‘dark’ in color,
26664:Br. du ‘black’ (15.65), also ‘dark’, as glas du ‘dark green’.
26675:6. Skt. krsna-, gyama ‘black’ (15.65), also ‘dark’ in color.
26708:15.65 BLACK
=== WLD Bd1 kers
25608:sich iiberschlagt" ( *kers->tovos ; wenn nicht eher Lw. aus der Sprache der 
25637:crdbro; sie ist nicht naher an kers- ..starren 1- , sondern an yjgag usw. anzu- 
26002:..Haar“ und — doch s. vielmehr kers- „Borste“ — dt. Haar usw.), betrach- 
26004:serf/s usw. (s. kers- ,.Borste“) ; beides vernachlassigt den Begriff des 
26376:harsk und *kers- „Borste“): ai. knsaka- „brennend; Feuer, Sonne -1 und ka- 
26877:qerno- — kers- 
26928:Verwandtschaft von kers- ,,starren“ mit ker- „das oberste am Korper ‘ 
26931:2. kers- „laufen; AVagen“. 
=== WLD Bd1 ker brennen
979:mann Arm. Gr. I 418); umbr. eiscurent (Bugge KZ. 30, 40) „arcessierint“ 
2157:Falk-Torp (418 f-, 1484) u. liorg (Lit.) reiht an air. cam auch schwed. har 
3244:KZ. 40, 418). Ganz fragliclies aus deni Arm. bei Pedersen KZ. 39, 399, 
8282:PI. „Eingeweide“ s. Berneker 434 f. m. Lit., aucli Schulze KZ. 40, 418 
8784:Curtius 347 f., Robert Noms des oiseaux 13ff. (Lit.), Meillet Et. 418.
```


## [2026-09-06T16:25:06.807Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26870,26890p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== WLD ker Farbe (I 428f)\"; grep -n \"Farbwurzel\\|kf-9no-\\|krs-no\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8",
 "description": "Read Walde-Pokorny kers- entry"
}
```


### [2026-09-06T16:25:06.868Z] TOOL RESULT

```
ursprgl. Bed. ist, als „Baum mit roten Beeren" zum Wieselnamen *kor- 
men-, sofern dieser auf die rotliche Sommerfarbe des Tieres gehn konnte? 
Unsicher ist auch der Yergleich von ai. kramuka- m. „BetelnuBbaum und 
andere Pflanzen", krmuka- m. „ein Baum" (Uhlenbeck aaO.). Gall. ON. 



qerno- — kers- 


427 


Cormiliae , heute Cormeilles , frz. cormil , cormier „Spierlingsbaum“ (ala kelt. 
Lw. von B. bei Pick II 4 91 mit den bait, verglichen) werden von Schuchardt 
ZfromPh. 24, 412. Meyer-Liibke Rom. et. Wb. Nr. 2072 vielmehr aus gr. 
xofxago g „Erdbeerbaum“ hergeleitet (dessen Deutung aus *y.oQ/uaQog , siehe 
Niedermann bei Boisacq 488 Anm. 1, unsicher ist). 

qerno- „Kinnbacken“. 

=== WLD ker Farbe (I 428f)
30701:qr(o)sqo-, -u kros-no-, krs-no-, -na 
30735:kros-uo-, krs-no-, -na „Quelle, flieBendes Wasser" ?
```


## [2026-09-06T16:25:10.290Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kirsnan\\|Kirsnappe\\|krs-no-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head; echo \"---\"; grep -n \"kirsnan\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt WLD_band3.txt | head",
 "description": "Search WLD for kirsnan"
}
```


### [2026-09-06T16:25:10.354Z] TOOL RESULT

```
26981:Ai. krkna- „schwarz“ = apr. kirsnan ds., lett. Kirsna „Name eines FlfiB- 
30701:qr(o)sqo-, -u kros-no-, krs-no-, -na 
30735:kros-uo-, krs-no-, -na „Quelle, flieBendes Wasser" ? 
---
```


## [2026-09-06T16:25:14.558Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26970,27000p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== WLD ker Farbwurzel dirt (I 409/428)\"; grep -n \"cardeh\\|karic\\|karah\\|Farbentone\\|Farbtone\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8",
 "description": "Read WLD kers- black and search for Persian forms"
}
```


### [2026-09-06T16:25:14.629Z] TOOL RESULT

```
Anwendung von knrsiu „kamme, kammle“ (Bed.-Parallelen bei Lager- 
crantz aaO.); endlich ai. kfiitha „Ziel, Grenzpunkt, Gipfel; Bennbahn" 
(Bezzenberger BB. 16, 120), da zu kastha- n. „IIolz9tfick, Holzscheit“ als 
„holzerner Pfahl (meta), Grenzpfahl u. dgl.“, s. Johansson IF. 14, 314 f., 
auch Petersson Stud, zu Fortunatovs Regel 38, 36 (mit Lit. auch fiber die 
unannehmbare Verbindung von kudha als „Blickpunkt !< mit ai. caksate „sie 
sehen“, gr. xey.uao, aksl. Lazuli „zeigen“). 

1. qers- und wohl auch bloBes qer- in Worten ffir Farben, bes. dunkle, 
schmutzige. 

Ai. krkna- „schwarz“ = apr. kirsnan ds., lett. Kirsna „Name eines FlfiB- 

chens“ (etwa „Schwarzwasser“) = abg. cr~om, russ. ierem , skr. crn usw. 
„schwarz“ ( *t : brxm . *cb rsm; s. Berneker 169 m. Lit.); ohne -wo-Formans 
lit. kersas „schwarz und weiB gefieckt“, kt'rse „bunte Kuh“, kersis „schwarz- 

bunter Ochse“, kermlis „Ringeltaube“; karsts „Brassen. Blei (Fisch)‘ f , 

kirstTjs „Asche“, schwed. norw. Iiarr „Asche £t (Liden PBrB. 15, 509 f.; 

fiber ags. henrd-ham , hearch a, nhd. holl. harder , herder ; ,Meer-Asche“, 
Schroder GRM 1, 588, s. aber Kluge 8 191). 

Auf kttrzeres qer- bezieht man (s. bes. Liden Stud. 51, Zupitza Gutt. 109, 
Petersson LUA. 1916, 36ff., Scheftelowitz IF. 33, 167, Persson Beitr.): 

Ai. karuta- „dunkelrot“, kiirtmgd -, kulm.iqd- m. „Antilope“ (aber abg. 
krara usw. „Kuh“ bleibt bei terms usw.. ker- ,.oberstes am Kbrper“; r. kon, 
„Masern“ wohl zu sqer- „schneiden“), kirmira- ,,bunt“ ( l;at mam -, kalmasa- 
„Fleck, Schmutz, Sfinde“ wohl zu qel-\ Lanka „Auswurf, Lunger', karda- 
=== WLD ker Farbwurzel dirt (I 409/428)
9485:erebli-, orobh- in Worten fiir dunkelrotliche, briiunliche Farbentone 
25753:3. ker- 1. fur undeutliche graue Farbentone. 2. Reif, Frost, frieren. Letz- 
27012:mhd. hurmen siehe aber unter kormno- „atzende Fliissigkeit"), np. cardeh 
27013:„schwarzlich“, kari, karah „Schmutz“, pehl. karic „Mist“; ai. kalkd-h 
27735:und schwiirzliche Farbentone. 
39246:schiedenheit des Farbtones konnte beim bekannten Schwanken des Idg. 
53860:triiben, schmutzigen Farbentonen usw.; verbal: Bodensatz und Schlamm
```


## [2026-09-06T16:25:21.100Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26708,26730p' SYN.txt | cut -c1-400",
 "description": "Read Buck 15.65 BLACK"
}
```


### [2026-09-06T16:25:21.172Z] TOOL RESULT

```
15.65 BLACK
is Goth. swarts Lith. juodas Grk. pednss prec ON svartr Lett. sates NG pe get Dan. _ sort ChSl. Griintt iat. aler; Sw. svart SCr. crn It nero OE blac, sweart Boh. éerny ir. now 5 ME blak, swart Pol. czarny Sp. ‘wl NE black Russ. ternyj Rum. al Du. zwart Skt.  krgna-, ¢yama- i ane oe suarz Ay. sdma-, sydva- Nir. swarz W. a NHG schwarz r
Words for ‘black’ in part reflect such votions 8 ‘dirty’, ‘smoky’, ‘blackened by fire’(?). Some belong to inherited groups containing words applied to various colors, the primary sense of which is obscure. Some old words for ‘black’ that were replaced by others survived in the sense of ‘ink’ (18.58).
1, Grk. pétas (NG perdu ‘ink’, peda- yos ‘blue-black, livid’) : Lett. melns ‘black, dirty’, Skt. mala- ‘dirt, filth’, malina- ‘dirty’, etc. (15.88).
Grk, xedawds : Skt. kalanka- ‘spot, blemish’, kalana- ‘spot, dirt’, Swiss helm ‘white spot on the forehead of cattle’, ete. Walde-P. 1.440 f. Boisacq 480.
Byz., NG padpos, late Grk. pavpés, for duaupds ‘dim, faint, hardly seen’ (: ON meyrr ‘tender, soft’, Russ. smuryj ‘dark- gtey’, chmuryj ‘overcast, cloudy, sullen’, ete. Walde-P, 2,223).
2. Lat. ater, Umbr. atru, adro ‘atra’, Ss blackened, burned by fire’ : Bee aM fire’, Arm. airem ‘kindle, (3 Bs - vatra ‘fire’, etc. Walde-P. 298 tout-M. 83 f. Walde-H. 1.75f.,
Lat, miger (> Romance words) ?
aed Walde-P. 2.322. Emout-M. 671. Goth : dub, NIr. dubh, W., Br. du: ; cufs, ON daufr, etc. ‘deaf’, Grk. blind, dark’, rS¢os ‘smoke, vapor, » thd ‘smoke, burn slowly’, fr. ~ extension of *dheu- seen also fuscus ‘dark’, etc., 15.68). 1’, here prob. fr. ‘confused,
at,
i lack, da;
dimmed by vapor’ or the like. Walde-P. 1.840. Pedersen 1.116.
4, Goth. swarts, ON svarir, etc., gen- eral Gmc. (NE swart only rhet., poet., or dial.) : Lat. sordés ‘filth’, sordidus ‘dirty’ (15.88), sudswm, a kind of dark color. Walde-P. 2.535. Falk-Torp 1109. Ernout-M. 958, 991.
OE blec, ME blak, NE black (as sb. OE blac, OHG blach, OS blak ‘ink’), etym. disputed, prob. : OHG ODlecchen, MHG blecken ‘be visible, let see’, OHG blanc ‘shining white’, Du. blaken ‘burn, glow’, Lat. flagrdre ‘flame, burn’, Grk. gdéyw ‘burn, blaze’, etc., with develop- ment of ‘black’ fr. ‘burnt’ or ‘shining black’(?). Walde-P. 2.215. Falk-Torp 87. NED s.v.
5. Lith. juodas: Lett. juods ‘evil spirit, wood or field demon’; but further connection? Mithl.-Endz. 2.125.
Lett. melns : Grk. pédas (above, 1).
6. ChSI. ériint, etc., general Slavic : OPruss. kirsnan, Skt. krsna- ‘black’, fur- ther, Lith. kergas ‘black and white’, kersé ‘spotted cow’, etc., Sw., Norw. harr ‘ashes’. Walde-P. 1.428. Berneker 169 f.
7. Skt. eyama-, Av. sama- (s- fr. sy-), beside syava = Skt. cydva- ‘dark-brown’ : Lith. Sémas ‘blue-gray’, Syvas ‘gray (of horses)’, OPruss. sywan, ChSI. sivi, Russ. sivyj ‘gray’, OE hewen ‘blue’, etc. (15.67).
Skt. krsna-, above, 6.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1056 SELECTED INDO-EUROPEAN SYNONYMS 15.66 RED Grk. — épvOpéds Goth. raups Lith. raudonas NG KOoxxtvos ON rauodr, rjodr Lett. sarkans Lat. ruber (rufus, russus) Dan. rd ChSl.  Giiminy, (Giveni, It. TOsso Sw. rod ritdrit) : Fr, rouge OE réad, réod SCr.  crven Sp. rojo ME reed Boh. — éerveny Rum. rosiu NE red Pol. —czerwony Ir, derg, ritiad Du. rood Russ. krasnyj NIr.  dearg, ruadh OHG ra
The majority of the words for ‘red’ be- long to an inherited group pointing to an TE word for ‘red’. Several of the others are derived from names of vegetable or animal sources of red dye; some from ‘rosy’ or ‘glowing’.
```


## [2026-09-06T16:25:39.078Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"kers-[^.]*\\. [^[]*\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -5; echo \"---\"; grep -o \"ker-1[^[]*\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -3",
 "description": "Grep Watkins for kers- root"
}
```


### [2026-09-06T16:25:39.168Z] TOOL RESULT

```
kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.]
kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.]
---
ker-1. Horn, head; with derivatives referring to horned animals, horn-shaped objects, and projecting parts. I. Zero-grade form *kr-. 1. Suffixed form *kr-n- in: a. Ger- manic *Aurnaz in (i) Old English horn, horn: HORN, (HORNBEAM) (ii) German Horn, horn: ALPENHORN, ALT- HORN, FLUGELHORN, HORNBLENDE; Db. Latin cornd, horn: CORN2, CORNEA, CORNEOUS, CORNER, CORNET, CORNICULATE, CORNU; BICORN, CADUCICORN, CAPRI- CORN, CLAVICORN, CORNIFICATION, LAMELLICORN, LON- GICORN, TRICORN, UNICORN. 2. Suffixed and extended form *krs-n- in Germanic *hurznuta in Old English hyrnet, hornet: HORNET. 3. Suffixed form *kr-ei- in: a. Germanic *hraina- in Old Norse hreinn, reindeer: REINDEER; b. Germanic *hrinda- in Old High German hrind, ox (> German Rinder, cattle): RINDERPEST. 4. Suffixed extended form *kros-no- in Greek kranion, skull, upper part of the head: CRANIUM; MIGRAINE, OLECRANON. 5. Suffixed form *kr-a- in: a. Greek karé, kara, head: CHARIVARI; CHEER; b. Greek karoun, to stupefy, be stupefied (< “to feel heavy-headed”): ca- ROTID; c. Greek kardton, carrot (from its hornlike shape): CARROT. 6. Possibly extended form *kri- in Greek krios, ram: CRIOSPHINX. II. Suffixed form *ker-wo-. 1. Latin cervus, deer: CERVINE, SERVAL. 2. Latin cervix, neck: CERVIX. III. Extended and suffixed form *keru-do- in Germanic *herutaz in: a. Old English heorot, hart, stag: HART; b. Dutch hart, deer, hart: HARTEBEEST. IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; CERATODUS, (CERATOID), CHELIC- ERA, CLADOCERAN, KERATIN, RHINOCEROS, TRICERA- Tops. 2. Persian sar, head: SIRDAR. 3. Suffixed form *keras-ro- in Latin cerebrum, brain: CEREBELLUM, CERE- BRUM, SAVELOY. V. Extended o-grade form *koru-. 1. Greek Rorumbos, uppermost point (< “head”): CoR- yMB. 2. Greek koruphé, head: CORYPHAEUS. 3. Suffixed form *koru-do- in Greek korudos, crested lark: coRY- DALIS. 4. Suffixed form *koru-ndé in Greek koruné, club, mace: CORYNEBACTERIUM. [Pok. 1. ker- 574.]
ker-1. 1. Latin scribere, to scratch, incise, write: SCRIBBLE, SCRIBE, SCRIPT, SCRIPTORIUM, SCRIPTURE, SERIF, SHRIVE; ASCRIBE, CIRCUMSCRIBE, CONSCRIPT, DESCRIBE, INSCRIBE, MANUSCRIPT, POSTSCRIPT, PRESCRIBE, PRO- SCRIBE, RESCRIPT, SUBSCRIBE, SUPERSCRIBE, TRAN- SCRIBE. 2. Greek skariphos, scratching, sketch, pencil: SCARIFY}, [Pok. 4. sker-, Section II. 945.]
```


## [2026-09-06T16:25:47.062Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg258.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/258.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/258.png",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-06T16:25:47.123Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 81240 Sep  6 12:25 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/258.png
```


## [2026-09-06T16:34:53.924Z] TOOL CALL #70: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk258.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\nPOK573 = (\"POK_02.txt line 3588, on the leaf whose running page numbers are 573/574: \"\n          \"'6. ker- und kerə-, Farbwurzel für dunkle, schmutzige und graue Farbentöne; oft mit -i und -u \"\n          \"erweitert; kor-ko- „Kot, Sumpf“, ker-no- „Eis, Schnee“, kor-men- „Hermelin, Wiesel“; s. die \"\n          \"Erweiterungen kerb(h)- und kers-.' The same paragraph reads '... npers. čardeh „schwärzlich“, \"\n          \"karī, karah „Schmutz“, pehl. karič „Mist“ ...'\")\nPOK583 = (\"POK_02.txt line 3756, with the page marker '583' printed on the line immediately above: \"\n          \"'1. kers- und wohl auch bloßes ker- in Worten für Farben, bes. dunkle, schmutzige; kr̥s-no- \"\n          \"„schwarz“; vgl. auch 4. kel- und 6. ker-. Ai. kr̥ṣṇá- „schwarz“ = apr. kirsnan ds., FlN Kirsnappe \"\n          \"= abg. črъnъ, russ. čërnyj, skr. crn usw. „schwarz“'\")\nPOK571 = (\"POK_02.txt line 3566 ff., leaf carrying the page marker 572: '3. ker(ə)- „brennen, glühen, heizen“. \"\n          \"Ai. kūḍayati „sengt“ (*kr̥-d-) ... zweifelhaft lat. carbō, -ōnis m. „Kohle“ (idg. *kr̥-dhō?) ... \"\n          \"got. haúri „Kohle“, aisl. hyrr m. „Feuer“ (*hūrja-, idg. *kr̥-io-); ahd. herd, as. herth, ags. heord \"\n          \"„Herd“ ... lit. kuriù, kùrti „heizen“ ... Ein aus ker- erweitertes *k(e)r-em- sucht man in lat. cremō, \"\n          \"-āre „verbrennen (tr.)“, umbr. krematra'\")\nWATKINS4 = (\"AHD_watkins1985.txt, k-list: 'ker-4. Heat, fire. 1. Suffixed form *ker-tā in Germanic *herthō in \"\n            \"Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr̥- in: a. Latin carbō, charcoal, ember: \"\n            \"CARBON, CARBUNCLE; b. extended form *krem- in Latin cremāre, to burn: CREMATE. 3. Possibly \"\n            \"suffixed and extended form *kerə-mo- in Greek keramos, potter's clay, earthenware: CERAMIC. \"\n            \"4. Possibly variant extended form *krās- in Russian krasa, beauty. [Pok. 3. ker(ə)- 571.]'\")\nWATKINSKERS = (\"AHD_watkins1985.txt, k-list: 'kers-1. Dark, dirty. 1. Suffixed form *ker(s)-no- in Russian \"\n               \"chérnyi, black: CHERNOZEM. 2. Suffixed zero-grade form *kr̥s-no- in Sanskrit kr̥ṣṇa-, black, \"\n               \"dark: KRISHNA. [Pok. kers- 583.]'\")\nWLD428 = (\"WLD_Bd1_1930_dli_70244_djvu.txt lines 26978-27013 (Bd. I 427-429): '1. qers- und wohl auch bloßes \"\n          \"qer- in Worten für Farben, bes. dunkle, schmutzige. Ai. kr̥ṣṇá- „schwarz“ = apr. kirsnan ds., lett. \"\n          \"Kirsna „Name eines Flüßchens“ = abg. črъnъ, russ. čerenъ, skr. crn usw. „schwarz“' and, in the \"\n          \"shorter qer- paragraph, '... np. čardeh „schwärzlich“, karī, karah „Schmutz“, pehl. karič „Mist“'\")\nBUCK1565 = (\"SYN.txt line 26708 ff., Buck §15.65 BLACK, sub-paragraph 6: 'ChSl. črъnъ, etc., general Slavic : \"\n            \"OPruss. kirsnan, Skt. kr̥ṣṇa- „black“, further, Lith. keršas „black and white“, keršė „spotted cow“, \"\n            \"etc., Sw., Norw. harr „ashes“. Walde-P. 1.428. Berneker 169 f.' Buck's Iranian row for „black“ has \"\n            \"only Av. sāma-, syāva- — no *kirsman\")\nIEC590 = (\"IEC.txt leaf 336 (printed p. 590, running head 'kūnos — kur-'): 'kur- (3) (kuros, om, iom, iə) \"\n          \"„heat, fire, fuel, burning“. Cf. WP I, 418 — Per. kūre „fireplace, forge“; Go. haúri, n. „coal“; pl. \"\n          \"haúrja „coalfire“; ON hyrr, gs hyrjar, m. „fire“; Li. kūras „fuel“; kuriù, inf. kūrti „light a fire“; \"\n          \"Latv. kuru, kurt, id., beside kure „heating“; Skt. cf. kūlayāmi „singe“'\")\nKLNHEARTH = (\"KLN_1966.txt line 17357, s.v. hearth: 'hearth, n. — ME. herth, fr. OE. heorð, rel. to OS., OFris. \"\n             \"herth, MDu. hert, Du. haard, OHG. herd, MHG. hert, G. Herd, „hearth“, fr. Teut. base *her-, \"\n             \"corresponding to I.-E. base *ker-, „to singe, burn, glow“, whence also Goth. hauri, „coal“, ON. hyrr, \"\n             \"„fire“, OI. kūḍayati, kūlayati, „singes“, OSlav. kurjǫ, kuriti sę, „to smoke“, Lith. kuriù, kùrti, \"\n             \"Lett. kuru, kurt, „to heat“ ... and prob. also L. carbo, „coal, charcoal“; see carbon. Cp. cremate'\")\nKLNCREMATE = (\"KLN_1966.txt line 9625, s.v. cremate: 'L. crematus, pp. of cremāre, „to consume by fire, burn“, \"\n              \"rel. to Umbr. krematra ... fr. I.-E. *ker-em, an -m- enlargement of base *ker-, „to singe, burn, \"\n              \"glow“, whence also L. carbo, „coal“, OE. heorþ, „hearth“. ... Gk. κέραμος, „potter's clay“, is not \"\n              \"cogn. with L. cremare (see ceramic)'\")\nKLNCERAMIC = (\"KLN_1966.txt line 7002, s.v. ceramic: 'Gk. κεραμικός, „of pottery, made of earthenware“, fr. \"\n              \"κέραμος, „earthen vessel, jar, potter's clay, pottery“, a pre-Hellenic word derived from a language \"\n              \"of Asia Minor and not cognate with L. cremāre. See Kretschmer, Glotta ...'\")\nKLNCARBON = (\"KLN_1966.txt line 6509, s.v. carbon: 'L. carbo, gen. -ōnis, „coal, charcoal“, prob. standing for \"\n             \"*car-dho and derived fr. I.-E. base *ker-, „to singe, burn, glow“. See hearth and cp. cremate'\")\nLATCARBO = (\"LAT.txt line 9855, Ernout-Meillet s.v. carbo: 'carbo, -ōnis m.: charbon de bois, produit de la \"\n            \"combustion, souvent joint à cinis ... Ancien, usuel. Panroman. M.L.1674-1676.' — the article gives \"\n            \"the Romance descendants and the diminutive carbunculus but offers NO Indo-European etymology\")\nLATCREMO = (\"LAT.txt line 14451, Ernout-Meillet s.v. cremo: 'cremo, -ās, -āuī, -ātum, -āre: brûler ... Peut-être \"\n            \"d'un élargissement en -em- de la racine attestée par v.isl. hyrr „feu“, got. hauri „charbon“, lit. \"\n            \"kuriu, kurti „faire du feu“ (v. sl. kuriti „chauffer“ est un causatif secondaire). Le mot semble \"\n            \"osco-ombrien, car l'ombrien a le nom d'instrument krematra'\")\nAKD32 = (\"AKD.txt line 448 (Zimmern, Akkadische Fremdwörter, p. 32): 'kūru u. kīru Ofen, Herd, Schmelzofen \"\n         \"(viell. < sum. gir) : > hebr. kūr u. Du. kīrajim, aram. kūrā (> arab. kūr u. kīr, äth. kaur, auch \"\n         \"armen. kʿurai)'\")\nBQT1619 = (\"data/verification/sources/refs/ocr/BQT/1619 (tools/ref_page.py BQT:1619 = BQT_v3_picofile.pdf p.412): \"\n           \"'کرس - ب[ض]م اول و فتح ثانی و سین بی نقطه، چرک و ریم را گویند - و موی پیچیده و مجعد را نیز گفته‌اند' \"\n           \"(footnote 6: 'کری (ه.م.) * کرسنه (و.م.)'); and 'کرسنه - بکسر اول و ثانی و سکون ثالث و فتح نون، چرک و \"\n           \"ریمی را گویند که بر روی زخم بسته و سخت شده باشد ... و بفتح اول و سکون ثانی و فتح ثالث و لون، نام غله‌ایست \"\n           \"تیره‌رنگ و طعم آن مابین ماش و عدس باشد ... آنرا مقشر کرده بگاو دهند گاو را چاق و فربه کند و بیونانی \"\n           \"اروبی [ὄροβος] خوانند'\")\nBQT1631 = (\"data/verification/sources/refs/ocr/BQT/1631 (tools/ref_page.py BQT:1631 = BQT_v3_picofile.pdf p.424): \"\n           \"'کره - بفتح اول و ثانی و خفای ها. پوست دست و پا و اعضا را گویند که بسبب کار کردن بسیار سخت شده و پینه \"\n           \"بسته باشد - و بمعنی چرک هم آمده است که عربان وسخ گویند' with footnote 8 = exactly Nourai's shāhed: \"\n           \"'چون دست و پای پاک نه‌بینمت جان و دل این هردو پاک بینم و آن هردو با کره. ناصر خسرو بلخی ص ۳۸۶'\")\nMONKAREH = (\"MON_part2.txt line 22617: 'کره: (اِ.) چرک، وسخ. پوست دست و پا و اعضا که به سبب کار کردن بسیار سخت \"\n            \"گردد و پینه بندد.'\")\nMONCARDEH = (\"MON_part1.txt lines 50136, 50142: 'چرد: [= چرده = چرته] (اِ.) رنگ، لون (مخصوصاً در چارپایان)' and \"\n             \"'چرده: [= چرته = چرد] (اِ.) رنگ، لون (عموماً). رنگ چهره و پوست؛ سیاه‌چرده.'\")\nMONKUREH = (\"MON_part2.txt lines 27912-27917: two headwords — 'کوره: [= کورة: معرب خُره] (اِ.) شهرستان، ناحیه، \"\n            \"ج. کُوَر' and 'کوره: [... کور] (اِ.) آتشگاه آهنگری و مسگری. جایی که در آن خشت و گچ و امثال آن پزند.' \"\n            \"The lexicon OCR has no page markers, so MON's own p. 3121 could not be checked, only the wording\")\nVOPNOTE = (\"Mahshid Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi, Alborz 1371/1992. refs_online.json records \"\n           \"kind='none': re-searched archive.org, ketabnak, noorlib and the open web in 2026 — no scan, no ebook, \"\n           \"no catalogue record with a copy. Not consultable\")\n\ndata = {\n \"pdf_page\": 258,\n \"book_page\": 228,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- ENTRY 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Ker 4, Kers 1, Kerb\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱers- / *kr̥snós 'black' (Pokorny 583 '1. kers-'), alongside Pokorny's loose colour-root '6. ker-, kerə-' for dark, dirty and grey shades (Pokorny 573), of which kers- and kerb(h)- are the -s- and -bh- extensions\",\n \"note\": (\n   \"The root box checks out on both cited pages and the three names are not arbitrary: they are Pokorny's own \"\n   \"cross-references. Pokorny 573 heads '6. ker- und kerə-, Farbwurzel für dunkle, schmutzige und graue \"\n   \"Farbentöne ... s. die Erweiterungen kerb(h)- und kers-', and Pokorny 583 heads '1. kers- und wohl auch bloßes \"\n   \"ker- in Worten für Farben, bes. dunkle, schmutzige; kr̥s-no- „schwarz“'. So 'Ker 4' = Pokorny's 6. ker-, \"\n   \"'Kers 1' = Pokorny's 1. kers-, and 'Kerb' = the kerb(h)- extension Pokorny names on p.573 and discusses on \"\n   \"p.567 ('Die Wz. kerb- sucht Liden ... und betrachtet kerb- als Erweiterung der Farbwz. ker- (s. S. 583 \"\n   \"kers-)'). The numbering itself is Nourai's own homonym numbering, not Pokorny's. The gloss 'dirt, dark, \"\n   \"black' is exactly what the two articles say. Two reservations. (i) Modern handbooks keep only the tight, \"\n   \"well-attested item *kr̥snós 'black' (Skt. kr̥ṣṇá-, OPruss. kirsnan, Proto-Slavic *čьrnъ, Lith. kir̃šnas); the \"\n   \"grab-bag of 'dirt' words Pokorny assembles under 6. ker- (Skt. kárīṣa-, kardama-, kalka-, OHG horo, ags. \"\n   \"hrot, npers. karah) is not maintained as one root by Kroonen or de Vaan and is partly onomatopoeic or \"\n   \"substrate. (ii) The chart's one real error is node 3: Nourai read Pokorny's 'apr. kirsnan' (altpreußisch = \"\n   \"Old Prussian) as an Old Persian word and mis-copied it as 'kirsman'.\"),\n \"note_fa\": (\n   \"جعبهٔ ریشه درست است و هر سه نامی که نورایی آورده از خود پوکورنی گرفته شده است: در صفحهٔ ۵۷۳ مدخل «۶. ker- و \"\n   \"kerə-، ریشهٔ رنگ برای رنگ‌های تیره، چرکین و خاکستری» آمده و همان‌جا دو گسترش kerb(h)- و kers- معرفی شده، و در \"\n   \"صفحهٔ ۵۸۳ مدخل «۱. kers- ... kr̥s-no- «سیاه»» با نمونهٔ سنسکریت kr̥ṣṇá- ثبت است. پس Ker 4 همان ۶. ker-، Kers 1 \"\n   \"همان ۱. kers- و Kerb همان kerb(h)- است؛ شماره‌گذاری از خود نورایی است. معنای «چرک، تیره، سیاه» نیز درست \"\n   \"برگردانده شده. دو نکته: نخست آنکه ریشه‌شناسی امروزی تنها صورت استوار *kr̥snós «سیاه» را نگاه می‌دارد و \"\n   \"خوشهٔ واژه‌های «چرک» که پوکورنی زیر ۶. ker- گرد آورده در کتاب‌های نو (کرونن، دِ فان) ریشهٔ یگانه شمرده \"\n   \"نمی‌شود؛ دوم آنکه گرهٔ ۳ («پارسی باستان kirsman») خطای خود نورایی است: پوکورنی apr. kirsnan یعنی «پروسی کهن \"\n   \"kirsnan» نوشته و نورایی apr. را «پارسی باستان» خوانده است.\"),\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/कृष्ण\",\n   \"https://en.wiktionary.org/wiki/Krishna\",\n   \"https://en.wiktionary.org/wiki/كرسنة\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:573\", \"status\": \"supports\", \"note\": POK573 + \" — the page underwrites the root box and nodes 1 and 2 word for word.\"},\n   {\"ref\": \"POK:583\", \"status\": \"partial\", \"note\": POK583 + \" — the page supports the name 'Kers 1' and node 5 (Skt. kr̥ṣṇá-), but it contains no Iranian form whatever, so it cannot support node 3.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 427-429 (djvu lines 26978-27013)\", \"stance\": \"supports\", \"note\": WLD428 + \" — Walde-Pokorny is Pokorny's source and prints the same two paragraphs; 'apr.' = altpreußisch is unambiguous here.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, k-list\", \"stance\": \"supports\", \"note\": WATKINSKERS},\n   {\"src\": \"SYN\", \"where\": \"Buck §15.65 BLACK, §6\", \"stance\": \"supports\", \"note\": BUCK1565}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"karic : dirt, manure\", \"verdict\": \"plausible\",\n \"derivation\": (\n   \"Pokorny 573 lists 'pehl. karič „Mist“' in the same breath as the New Persian forms, so the citation is exact. \"\n   \"The word (Book Pahlavi <krc>, read karič/karīč) is a -č-suffixed noun on the Iranian colour/dirt stem *kar- \"\n   \"'dark, dirty, filthy', the same stem seen in Skt. kárīṣa- n. 'dung, manure' which Pokorny prints two lines \"\n   \"earlier in the same article. The reservation is one of attestation, not of derivation: neither MacKenzie's \"\n   \"Concise Pahlavi Dictionary (1971) nor Nyberg's Manual of Pahlavi glossary has the word, and Pokorny takes it \"\n   \"over unchanged from Walde-Pokorny I 428f., which in turn rests on the 19th-century Pahlavi materials of Horn \"\n   \"and Salemann. So the form is real in the literature but its textual base is a single old chain.\"),\n \"derivation_fa\": (\n   \"پوکورنی در صفحهٔ ۵۷۳ درست همین صورت را آورده است: «pehl. karič „Mist“» یعنی فارسی میانهٔ karič «سرگین، پِهِن». \"\n   \"این واژه ساخت اسمی با پسوند -īč/-ēč بر ستاک ایرانی *kar- «تیره، چرکین» است، همان ستاکی که در سنسکریت kárīṣa- \"\n   \"«سرگین» نیز دیده می‌شود و پوکورنی دو سطر بالاتر در همان مدخل آورده. یک احتیاط لازم است: این واژه نه در فرهنگ \"\n   \"پهلوی مکنزی هست و نه در واژه‌نامهٔ نیبرگ؛ پوکورنی آن را بی‌کم‌وکاست از والده-پوکورنی (جلد ۱، ص ۴۲۸) گرفته و آن \"\n   \"هم از داده‌های هرن و زالمان سدهٔ نوزدهم. پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"POK:573\", \"status\": \"supports\", \"note\": POK573 + \" — 'pehl. karič „Mist“' is verbatim Nourai's node.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, k- section (PHD.txt line 430, kūč(ak) … kurrag)\", \"stance\": \"silent\", \"note\": \"The whole ku-/ka- run is present (kulāčag, kulāf, kulang, kullag, kumig, kundāg, kundur, kurkum, kurrag) but there is no karič/karīč and no word for 'dung' in this shape.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\", \"note\": \"grep for 'karič|karīč|karic' in NYB_vol2_glossary.txt returns nothing.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 428f.\", \"stance\": \"supports\", \"note\": WLD428 + \" — this is where Pokorny's 'pehl. karič' comes from.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"kareh «کَره ۱» : dirt ; čardeh «چَرده (سیاه چرده)» : a suffix indicating (dark) color\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n   \"kareh کَره 'grime': confirmed on all three cited references. Pokorny 573 has 'npers. karī, karah „Schmutz“'; \"\n   \"Borhān-e Qāṭeʿ p.1631 defines کره as 'the skin of the hands, feet and limbs that has grown hard and callused \"\n   \"from much work — and it also means čerk (grime), which the Arabs call wasaḵ', and its shāhed is precisely the \"\n   \"Nāṣer-e Khosrow line Nourai reproduces; Moʿin repeats the same definition. The word is the New Persian \"\n   \"continuation of the Old Iranian stem *kar- 'dirty' with the common NP -ah/-eh nominal suffix. Note, however, \"\n   \"that Pokorny sets 'npers. karah' and 'pehl. karič' side by side as parallel formations on the stem, not one \"\n   \"from the other, so the chart's arrow #1 → #2 (NP from MP karič) is a simplification: NP kareh cannot lose a \"\n   \"final -č by any regular rule; it is a sister formation. čardeh چرده: Pokorny 573 does print 'npers. čardeh \"\n   \"„schwärzlich“', so Nourai's ref is faithful, but two things weaken the node. Moʿin glosses چرده simply as \"\n   \"'colour, hue (in general); the colour of face and skin', the 'dark' sense coming only from the compound \"\n   \"سیه‌چرده; and an initial č- cannot arise from a k- by any regular Persian sound law (Iranian k does not \"\n   \"palatalise before a), so čardeh's membership in this root is a comparison of Walde-Pokorny's, not a \"\n   \"demonstrated derivation. The variants چَرته، چَرد، چَرزه of the chart are exactly Moʿin's cross-references \"\n   \"(چرد [= چرده = چرته]).\"),\n \"derivation_fa\": (\n   \"«کَره ۱» به معنی چرک و وسخ: هر سه ارجاع نورایی درست است. پوکورنی (ص ۵۷۳) «npers. karī, karah „Schmutz“» آورده، \"\n   \"برهان قاطع (ص ۱۶۳۱) می‌نویسد «کره ... پوست دست و پا و اعضا را گویند که بسبب کار کردن بسیار سخت شده و پینه بسته \"\n   \"باشد ـ و بمعنی چرک هم آمده است که عربان وسخ گویند» و شاهد آن همان بیت ناصر خسرو است که نورایی نقل کرده؛ معین \"\n   \"نیز همین تعریف را دارد. «کره» دنبالهٔ ستاک ایرانی باستان *kar- «چرکین» با پسوند اسم‌ساز -ه فارسی نو است، اما \"\n   \"پوکورنی karah فارسی و karič پهلوی را در کنار هم و به‌عنوان دو ساخت هم‌عرض آورده، نه یکی برآمده از دیگری؛ پس \"\n   \"پیکان کتاب (پهلوی ← فارسی) ساده‌سازی است. دربارهٔ «چرده»: پوکورنی آن را به معنی «سیاه‌گونه» زیر همین ریشه ثبت \"\n   \"کرده، ولی معین آن را تنها «رنگ، لون (عموماً)» می‌داند و معنای تیرگی تنها از ترکیب «سیه‌چرده» می‌آید؛ افزون بر \"\n   \"این تبدیل ک ایرانی به چ در آغاز واژه پیش از «ا» قاعده‌مند نیست. پس این بخش گره با احتیاط پذیرفتنی است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:573\", \"status\": \"supports\", \"note\": POK573 + \" — both words of the node, karah and čardeh, stand in this one sentence.\"},\n   {\"ref\": \"BQT:1631\", \"status\": \"supports\", \"note\": BQT1631},\n   {\"ref\": \"MON:1281\", \"status\": \"partial\", \"note\": MONCARDEH + \" Moʿin has چرده and its variants چرد/چرته exactly as the chart's extra script line, but glosses it 'colour in general', not 'dark colour'; and the OCR of Moʿin carries no page numbers, so p.1281 itself could not be verified.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part2 s.v. کره\", \"stance\": \"supports\", \"note\": MONKAREH},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 428f.\", \"stance\": \"supports\", \"note\": WLD428},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for 'Schmutz' gives nos. 927 gil, 947 gūh, 5695 rīm — no entry for karah/kareh or čardeh; Horn has no article on either word.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\", \"note\": \"grep for 'cardah|čardah|schwärzlich' in HUB.txt returns nothing relevant (only 'mām so cardah „Vollmond“' in a different, Semitic context, p.97).\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 220], headword 'چرد چرده'\", \"stance\": \"silent\", \"note\": \"Aryanpur does have a چرد/چرده entry, but the Latin-script cognate columns of this scan are OCR noise ('پسگشت‌ها' block unreadable), so nothing can be quoted from it.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Old Persian\", \"words\": \"kirsman : black\", \"verdict\": \"transcription_suspect\",\n \"derivation\": (\n   \"There is no Old Persian word kirsman, and Pokorny 583 — the very page Nourai cites — shows where the form \"\n   \"comes from: 'Ai. kr̥ṣṇá- „schwarz“ = apr. kirsnan ds.' Here 'apr.' is Pokorny's abbreviation for altpreußisch, \"\n   \"Old Prussian, and kirsnan is the accusative singular of the Old Prussian adjective *kirsnas 'black' (Elbing \"\n   \"vocabulary; also the river-name Kirsnappe which Pokorny cites in the same line). Nourai read 'apr.' as 'Old \"\n   \"Persian' and copied the word with -m- for -n-. The controls are unanimous: Kent's Old Persian lexicon has \"\n   \"nothing of the kind; Bartholomae's Altiranisches Wörterbuch has karsna- only as the personal name of a \"\n   \"believer (Yt. 13.108), not an adjective 'black'; and Buck §15.65 and Walde-Pokorny I 428 both print 'OPruss. \"\n   \"kirsnan'. The printed page 228 of the book itself reads 'Old Persian … kirsman : black', so the extraction is \"\n   \"faithful and the error is the author's.\"),\n \"derivation_fa\": (\n   \"واژه‌ای به نام kirsman در پارسی باستان وجود ندارد. در همان صفحهٔ ۵۸۳ پوکورنی که نورایی به آن ارجاع داده آمده \"\n   \"است: «Ai. kr̥ṣṇá- „schwarz“ = apr. kirsnan ds.»؛ در اینجا apr. کوتاه‌نوشت altpreußisch یعنی «پروسی کهن» است و \"\n   \"kirsnan صورت رایی صفت پروسی کهن *kirsnas «سیاه». نورایی apr. را «پارسی باستان» خوانده و نون را میم نوشته است. \"\n   \"شاهدها یک‌دست‌اند: واژه‌نامهٔ پارسی باستان کنت چنین واژه‌ای ندارد، بارتولومه karsna- را تنها نام خاص یک مؤمن \"\n   \"(یشت ۱۳٫۱۰۸) ثبت کرده، و باک (§۱۵٫۶۵) و والده-پوکورنی نیز «پروسی کهن kirsnan» نوشته‌اند. تصویر صفحهٔ ۲۲۸ چاپی \"\n   \"نشان می‌دهد که خودِ کتاب «Old Persian … kirsman» چاپ کرده است؛ پس خطای چاپی/خوانشِ خودِ نورایی است، نه خطای \"\n   \"استخراج داده.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"Old Persian [POK:583] kirsman : black\",\n \"correct_form\": \"Old Prussian kirsnan (acc. sg. of *kirsnas) 'black'\",\n \"sources\": [\"https://en.wiktionary.org/wiki/कृष्ण\"],\n \"ref_check\": [{\"ref\": \"POK:583\", \"status\": \"contradicts\", \"note\": POK583 + \" — the page has 'apr. kirsnan' (Old Prussian), not an Old Persian 'kirsman'; there is no Iranian form on the page at all.\"}],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon\", \"stance\": \"silent\", \"note\": \"grep of KNT.txt for 'kirs' returns nothing; the only 'dark-colour' item in the lexicon is axšaina- 'turquoise, dark-coloured' (DSf 39), which is unrelated.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. ~455 (BRT.txt line 9314)\", \"stance\": \"contradicts\", \"note\": \"'karsna- m. EN. eines Gläubigen' — Avestan karsna- is a proper name only, with no adjectival sense 'black'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §15.65 BLACK, §6\", \"stance\": \"contradicts\", \"note\": BUCK1565},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 428\", \"stance\": \"contradicts\", \"note\": WLD428}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"kars «کَرس ( کِرس ، کِرسنه ۱)» : dirt\", \"verdict\": \"plausible\",\n \"derivation\": (\n   \"The word is real and the reference is exact: Borhān-e Qāṭeʿ p.1619 has 'کرس … چرک و ریم را گویند' ('grime and \"\n   \"pus'), with cross-references to کری and کرسنه, and on the same page 'کرسنه ۱ … چرک و ریمی را گویند که بر روی \"\n   \"زخم بسته و سخت شده باشد' ('the pus that has dried hard on a wound'). What fails is the arrow: node 3, its \"\n   \"drawn parent, does not exist, and Pokorny 583 (the kers- 'black' article) contains no Iranian material to \"\n   \"which kars could attach. If kars belongs anywhere in this chart it belongs with kareh and Pahlavi karič under \"\n   \"Pokorny's 6. ker- 'dirt' on p.573 — which is in fact how Borhān itself groups it, sending the reader from \"\n   \"کرس to کری and کرسنه ۱, all three 'grime, pus' words. Transcription note: the printed page 228 has «کَرس \"\n   \"( کِرس ، کِرسنه ۱)» with a kasra under the kāf; the JSON renders that kasra as a yāʾ, giving «کیرس ، کیرسنه ۱».\"),\n \"derivation_fa\": (\n   \"خودِ واژه درست است و ارجاع نیز دقیق: برهان قاطع (ص ۱۶۱۹) می‌نویسد «کرس … چرک و ریم را گویند» و در همان صفحه \"\n   \"«کرسنهٔ ۱ … چرک و ریمی را گویند که بر روی زخم بسته و سخت شده باشد». آنچه نادرست است پیکانِ نمودار است: گرهٔ \"\n   \"پدر (پارسی باستان kirsman) اصلاً وجود ندارد و در صفحهٔ ۵۸۳ پوکورنی هیچ صورت ایرانی نیامده است. اگر «کرس» جایی \"\n   \"در این نمودار داشته باشد، جایش کنار «کره» و پهلوی karič زیر ریشهٔ ۶. ker- «چرک» در صفحهٔ ۵۷۳ است — چنان‌که خودِ \"\n   \"برهان هم خواننده را از «کرس» به «کری» و «کرسنهٔ ۱» می‌فرستد. یک نکتهٔ خوانشِ اسکن: در صفحهٔ چاپی «کَرس ( کِرس ، \"\n   \"کِرسنه ۱)» با کسره آمده، ولی در فایل استخراج‌شده کسره به «ی» بدل شده است.\"),\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"BQT:1619\", \"status\": \"supports\", \"note\": BQT1619 + \" — 'dirt' is exactly Borhān's gloss for کرس.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi\", \"stance\": \"silent\", \"note\": \"grep of MON_part2.txt for a headword 'کرس:' returns only مذاکره/مستکره/نکره type Arabic entries; Moʿin has no independent کَرس 'grime' article in this OCR.\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny 583 and 573\", \"stance\": \"partial\", \"note\": POK583 + \" — no Iranian material on 583; the only Persian 'dirt' words Pokorny knows (karī, karah) are on 573 under 6. ker-.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss\", \"stance\": \"silent\", \"note\": \"no entry for kars in HRN.txt (grep 'Schmutz' gives only gil, gūh, rīm).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Sanskrit\", \"words\": \"kršna : black\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Sanskrit कृष्ण kr̥ṣṇá- 'black, dark' is the textbook reflex of the root: PIE *kr̥s-nó- (zero grade of *ḱers- \"\n   \"with the -no- adjective suffix) > Proto-Indo-Iranian *kr̥šnás > Skt. kr̥ṣṇá-, with the regular ruki change of \"\n   \"*s to ṣ after r̥. Its exact cognates are Old Prussian kirsnan, Proto-Slavic *čьrnъ (OCS črъnъ, Russian \"\n   \"čërnyj), and, without the -no- suffix, Lith. keršas 'black-and-white, piebald'. Pokorny 583 opens the article \"\n   \"with this very equation, and Watkins puts Sanskrit kr̥ṣṇa- under 'kers-1. Dark, dirty ... Suffixed zero-grade \"\n   \"form *kr̥s-no-'. Nourai's transliteration 'kršna' simply drops the vocalic-r̥ and retroflex diacritics.\"),\n \"derivation_fa\": (\n   \"سنسکریت कृष्ण (kr̥ṣṇá-) «سیاه، تیره» بازتاب کتابیِ همین ریشه است: هندواروپایی آغازین *kr̥s-nó- (پایهٔ صفر ریشهٔ \"\n   \"*ḱers- با پسوند صفت‌ساز -no-) ← هندوایرانی آغازین *kr̥šnás ← سنسکریت kr̥ṣṇá-، با تبدیل قاعده‌مند s به ṣ پس از \"\n   \"r̥ (قاعدهٔ ruki). هم‌ریشه‌های دقیق آن پروسی کهن kirsnan، اسلاوی آغازین *čьrnъ (روسی čërnyj) و لیتوانیایی keršas \"\n   \"«ابلق» است. پوکورنی در صفحهٔ ۵۸۳ مدخل را با همین معادله آغاز می‌کند و واتکینز نیز kr̥ṣṇa- را زیر «kers-1، تیره، \"\n   \"چرکین» می‌آورد. ادعای نورایی درست است؛ تنها آوانویسی «kršna» نشانه‌های r̥ و ṣ را ندارد.\"),\n \"sources\": [\"https://en.wiktionary.org/wiki/कृष्ण\"],\n \"ref_check\": [{\"ref\": \"POK:583\", \"status\": \"supports\", \"note\": POK583 + \" — 'Ai. kr̥ṣṇá- „schwarz“' is the first word of the article's evidence.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kers-1\", \"stance\": \"supports\", \"note\": WATKINSKERS},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 428\", \"stance\": \"supports\", \"note\": WLD428},\n   {\"src\": \"SYN\", \"where\": \"Buck §15.65 BLACK, §6\", \"stance\": \"supports\", \"note\": BUCK1565}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"karsneh «کَرسنه ۲ (کَسنی ، کَشنک )» : a black grain\", \"verdict\": \"plausible\",\n \"derivation\": (\n   \"کرسنه ۲ is bitter vetch, Vicia ervilia, and Borhān-e Qāṭeʿ p.1619 describes it exactly as Nourai does: 'a \"\n   \"grain of dark colour whose taste is between mung bean and lentil ... they husk it and give it to cattle to \"\n   \"fatten them, and in Greek it is called orobos'. Moʿin's own etymological footnote on that page is Nourai's \"\n   \"unnamed authority: he derives the word from Hebrew כרשינה / Aramaic כרשינא 'both of which appear to derive \"\n   \"from Sanskrit kr̥ṣṇa (black)', and lists the Persian variants کشنکه، کشنه، کشنی، کسنی، کسنکه — precisely the \"\n   \"چَسنی/کَشنک of the chart. So the Sanskrit → Persian link is Moʿin's, not Nourai's invention. But it is a \"\n   \"borrowing route, not a descent: Skt. kr̥ṣṇa- would have reached Persian only through Aramaic karšinnā / \"\n   \"Hebrew karšīnā and Arabic كرسنة kirsinna, so the arrow should carry two Semitic way-stations. And modern \"\n   \"Semitists offer a rival etymology that has nothing to do with Sanskrit: Wiktionary (s.v. كرسنة) sets beside \"\n   \"the Sanskrit account a derivation from Classical Syriac ܟܪܣܢܐ karsānā 'ventrose', from Proto-Semitic *kariś- \"\n   \"'paunch', from the flatulence the plant causes, and links the doublet كشنى kušnā < Syriac kūšnā, Akkadian \"\n   \"kiššanu. Hence 'plausible', with the route corrected.\"),\n \"derivation_fa\": (\n   \"«کَرسنهٔ ۲» همان گیاه Vicia ervilia (ماشک تلخ) است و برهان قاطع (ص ۱۶۱۹) دقیقاً همان‌گونه که نورایی آورده \"\n   \"تعریفش می‌کند: «نام غله‌ایست تیره‌رنگ و طعم آن مابین ماش و عدس باشد … آن را مقشر کرده به گاو دهند … و به یونانی \"\n   \"اُروبوس خوانند». حاشیهٔ ریشه‌شناختی معین بر همان صفحه سرچشمهٔ ناگفتهٔ نورایی است: معین واژه را از عبری כרשינה \"\n   \"یا آرامی כרשינא می‌داند «که به نظر می‌رسد هر دو مشتق از سانسکریت kr̥ṣṇa (سیاه) باشد» و گونه‌های فارسی کشنکه، \"\n   \"کشنه، کشنی، کسنی، کسنکه را برمی‌شمارد — یعنی همان «کَسنی، کَشنک» نمودار. پس پیوند سانسکریت ← فارسی از معین است، \"\n   \"اما این وام‌گیری است نه تبار مستقیم: راه آن سانسکریت ← آرامی/عبری ← عربی «کِرسِنّة» ← فارسی است. افزون بر این، \"\n   \"سامی‌شناسان امروز ریشه‌شناسی رقیبی نیز پیش می‌نهند: سریانی ܟܪܣܢܐ karsānā «شکم‌برآمده» از سامی آغازین *kariś- \"\n   \"«شکم» (به سبب نفخی که این دانه می‌آورد). بنابراین ادعا با احتیاط پذیرفتنی است.\"),\n \"sources\": [\"https://en.wiktionary.org/wiki/كرسنة\"],\n \"ref_check\": [{\"ref\": \"BQT:1619\", \"status\": \"supports\", \"note\": BQT1619 + \" Moʿin's footnote 5 on the same page reads: 'از عبری … یا از آرامی … که بنظر میرسد هر دو مشتق از سانسکریت … (سیاه) باشد. این نام در فارسی: کشنکه، کشنه، کشنی، کسنی، کسنکه و غیره آمده' — i.e. Borhān+Moʿin support both the gloss and the Sanskrit connection, but via Hebrew/Aramaic.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein, s.v. orobus / ervil\", \"stance\": \"silent\", \"note\": \"Klein has no article connecting Semitic karšinnā with Sanskrit; the Greek plant name ὄροβος that Borhān gives is treated separately.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitāb al-alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\", \"note\": \"the OCR of AFM.txt in the k- run (lines 7985-8005) is unreadable noise; no usable entry for كرسنة could be located.\"},\n   {\"src\": \"MON\", \"where\": \"Moʿin's footnote in BQT p.1619\", \"stance\": \"supports\", \"note\": \"see ref_check — Moʿin explicitly proposes Sanskrit kr̥ṣṇa 'black' as the ultimate source, through Hebrew/Aramaic.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Hindustani\", \"words\": \"krišna : the black one\", \"verdict\": \"plausible\",\n \"derivation\": (\n   \"Hindi/Urdu कृष्ण (Kr̥ṣṇa) is the name of the dark-complexioned eighth avatar of Viṣṇu, literally 'the black \"\n   \"one'. The reference is faithful in substance — the AHD's own IE appendix (Watkins) lists KRISHNA under \"\n   \"'kers-1. Dark, dirty ... Suffixed zero-grade form *kr̥s-no- in Sanskrit kr̥ṣṇa-'. The reservation is on the \"\n   \"word 'Hindustani' as an intermediate stage: Hindi कृष्ण is a tatsama, a learned re-borrowing of the Sanskrit \"\n   \"word in unchanged shape, not an inherited Middle-Indic descendant (the inherited Prakrit form would be \"\n   \"kaṇha-, as in Kanhaiyā); and Wiktionary derives English Krishna straight from Sanskrit ('Borrowed from \"\n   \"Sanskrit कृष्ण (kr̥ṣṇa)'), without a Hindi way-station. So the node is a real link in the transmission of the \"\n   \"name to Europe but is not a separate etymological step.\"),\n \"derivation_fa\": (\n   \"کْریشْنا در هندی/اردو (कृष्ण) نام هشتمین اوتار ویشنو و به‌لفظ «سیاه» است. ارجاع نورایی در گوهر درست است: پیوست \"\n   \"ریشه‌های هندواروپاییِ همان فرهنگ (واتکینز) واژهٔ KRISHNA را زیر «kers-1، تیره، چرکین … صورت پایهٔ صفر *kr̥s-no- \"\n   \"در سنسکریت kr̥ṣṇa-» می‌آورد. اما «هندوستانی» به‌عنوان مرحلهٔ میانی جای درنگ دارد: कृष्ण هندی «تتسمه» است، یعنی \"\n   \"وام‌گیری دوبارهٔ عالمانهٔ همان صورت سنسکریت، نه دنبالهٔ ارثیِ هندی میانه (صورت ارثی پراکریت kaṇha- است، چنان‌که \"\n   \"در «کنهیا»)؛ و ویکی‌واژه Krishna انگلیسی را یکراست از سنسکریت می‌گیرد. پس این گره پلی در راه انتقال نام به \"\n   \"اروپاست، نه گامی ریشه‌شناختی جداگانه.\"),\n \"sources\": [\"https://en.wiktionary.org/wiki/Krishna\", \"https://en.wiktionary.org/wiki/कृष्ण\"],\n \"ref_check\": [{\"ref\": \"AHD:727\", \"status\": \"not_checked\", \"note\": \"AHD New College Edition p.727 (the main-dictionary page with the headword Krishna) is not accessible: refs_online.json records the New College scans on archive.org as lending-only and HathiTrust as search-only. The same book's IE appendix, which is on disk as Watkins 1985, does carry KRISHNA under kers-1: \" + WATKINSKERS}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kers-1\", \"stance\": \"supports\", \"note\": WATKINSKERS},\n   {\"src\": \"HJB\", \"where\": \"Yule & Burnell, Hobson-Jobson\", \"stance\": \"silent\", \"note\": \"grep of HJB.txt finds no headword article for Krishna (the name occurs only in passing in other entries), so Hobson-Jobson does not document the Anglo-Indian route.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"Krishna\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"English Krishna is a direct scholarly borrowing of the Sanskrit name, current in English from the late 18th \"\n   \"century, when Wilkins's Bhagavad-Gītā (1785) and the Asiatick Researches made the Sanskrit epics available; \"\n   \"the -sh- spelling renders Sanskrit ṣ. Wiktionary: 'Borrowed from Sanskrit कृष्ण (kr̥ṣṇa)'. The AHD lists the \"\n   \"headword and derives it from Sanskrit kr̥ṣṇaḥ 'black', and its IE appendix carries KRISHNA as the English \"\n   \"yield of *kr̥s-no-, so the whole chain root → Skt. kr̥ṣṇá- → English Krishna is the standard one.\"),\n \"derivation_fa\": (\n   \"«کریشنا»ی انگلیسی وام‌گیری مستقیم و عالمانهٔ همان نام سنسکریت است که از اواخر سدهٔ هجدهم میلادی، پس از ترجمهٔ \"\n   \"بهگودگیتا به دست ویلکینز (۱۷۸۵) و انتشار Asiatick Researches، در انگلیسی رواج یافت؛ نگارش sh برابرنهاد ṣ \"\n   \"سنسکریت است. ویکی‌واژه می‌نویسد: «وام‌گرفته از سنسکریت कृष्ण». فرهنگ American Heritage نیز واژه را از \"\n   \"kr̥ṣṇaḥ سنسکریت «سیاه» می‌داند و در پیوست ریشه‌ها آن را دستاورد انگلیسیِ *kr̥s-no- می‌شمارد. پس زنجیرهٔ ریشه ← \"\n   \"سنسکریت ← انگلیسی که نورایی کشیده استاندارد است.\"),\n \"sources\": [\"https://en.wiktionary.org/wiki/Krishna\"],\n \"ref_check\": [{\"ref\": \"AHD:727\", \"status\": \"not_checked\", \"note\": \"New College Edition p.727 not accessible (lending-only scans); the appendix of the same dictionary, on disk as Watkins 1985, does list KRISHNA under kers-1: \" + WATKINSKERS}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kers-1\", \"stance\": \"supports\", \"note\": WATKINSKERS},\n   {\"src\": \"KLN\", \"where\": \"Klein, A Comprehensive Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"Klein carries no Krishna headword (grep of KLN_1966.txt returns nothing); proper names of this kind are outside his scope.\"}\n ]\n})\n\ndata[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- ENTRY 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Ker 5, Kur, Kertâ\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ker(ə)- 'to burn, glow, heat' (Pokorny 571-572 '3. ker(ə)-'; Watkins/AHD 'ker-4. Heat, fire'; Mann IEC 590 'kur- (3) heat, fire, fuel, burning')\",\n \"note\": (\n   \"Both cited references check out and, unusually, the three names of the box are each traceable to one of them. \"\n   \"'Ker 5' = Pokorny's '3. ker(ə)- „brennen, glühen, heizen“' on p.571, the page Nourai cites. 'Kur' = Mann's \"\n   \"headword 'kur- (3) „heat, fire, fuel, burning“' on IEC p.590, again exactly the cited page. 'Kertâ' = the \"\n   \"suffixed form *ker-tā that Watkins reconstructs for Germanic *herthō 'hearth' ('ker-4. Heat, fire. 1. \"\n   \"Suffixed form *ker-tā in Germanic *herthō in Old English heorth, hearth ... [Pok. 3. ker(ə)- 571]'), which is \"\n   \"also what AHD:1522, the page number on four of the nodes, refers to. The gloss 'heat, fire' is Watkins's own \"\n   \"wording. Two of the eight branches, however, do not survive checking: the Persian kūreh (node 1), which is a \"\n   \"Semitic loanword rather than an inherited Iranian word, and Greek keramos (node 10), which Klein, Chantraine \"\n   \"and Beekes treat as Pre-Greek. Latin carbō (node 4) is accepted by Watkins and Klein but called \"\n   \"'zweifelhaft' by Pokorny himself and left without an IE etymology by Ernout-Meillet.\"),\n \"note_fa\": (\n   \"هر دو ارجاع ریشه درست است و هر سه نامِ جعبه را می‌توان در همان منابع یافت: «Ker 5» همان مدخل «۳. ker(ə)- \"\n   \"«سوختن، گداختن، گرم کردن»» پوکورنی در صفحهٔ ۵۷۱ است؛ «Kur» همان سرواژهٔ «kur- (3) «گرما، آتش، سوخت»» در \"\n   \"فرهنگ تطبیقی مان (IEC) صفحهٔ ۵۹۰؛ و «Kertâ» همان صورت پسوندی *ker-tā است که واتکینز برای ژرمنی *herthō \"\n   \"«اجاق» بازسازی می‌کند و در پیوست AHD (ص ۱۵۲۲، همان شماره‌ای که بر چهار گره آمده) ثبت است. معنای «گرما، آتش» \"\n   \"نیز عین واژگان واتکینز است. با این همه دو شاخه از هشت شاخه در بررسی نمی‌مانند: «کوره»ی فارسی (گرهٔ ۱) که \"\n   \"وام‌واژه‌ای سامی است نه واژه‌ای ارثی ایرانی، و keramos یونانی (گرهٔ ۱۰) که کلاین، شانترن و بیکس آن را \"\n   \"پیش‌یونانی می‌دانند. carbō لاتین (گرهٔ ۴) را واتکینز و کلاین می‌پذیرند ولی خود پوکورنی «مشکوک» خوانده و \"\n   \"ارنو-مه‌یه هیچ ریشهٔ هندواروپایی برایش نمی‌آورد.\"),\n \"sources\": [\n   \"https://www.etymonline.com/word/hearth\",\n   \"https://www.etymonline.com/word/cremate\",\n   \"https://www.etymonline.com/word/carbon\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:571\", \"status\": \"supports\", \"note\": POK571 + \" — p.571-572 alone underwrites the root box and nodes 2, 4 and 8.\"},\n   {\"ref\": \"IEC:590\", \"status\": \"supports\", \"note\": IEC590 + \" — the printed page number 590 stands at the foot of that leaf and the running head is 'kūnos — kur-'; the entry supports both the root name 'Kur' and node 1's Persian word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, k-list, s.v. ker-4\", \"stance\": \"supports\", \"note\": WATKINS4},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 418 (cited by Mann as 'WP I, 418' and by Pokorny as 'WP. I 418 f.')\", \"stance\": \"supports\", \"note\": \"Both Pokorny 572 ('WP. I 418 f., WH. I 165 f., 287 f.') and Mann IEC 590 ('Cf. WP I, 418') refer the article back to Walde-Pokorny I 418, the parent article for this root.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. hearth (p.719) and cremate\", \"stance\": \"supports\", \"note\": KLNHEARTH},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. cremo\", \"stance\": \"supports\", \"note\": LATCREMO}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"kŭreh «کوره» : fireplace, oven, kiln\", \"verdict\": \"disputed\",\n \"derivation\": (\n   \"Nourai's reference is faithful — Mann, IEC p.590, really does open 'kur- (3) „heat, fire, fuel, burning“' \"\n   \"with 'Per. kūre „fireplace, forge“' beside Gothic haúri 'coal', ON hyrr 'fire' and Lith. kūras 'fuel' — but \"\n   \"Mann stands alone, and modern Iranian scholarship derives the word the other way. The Persian کوره continues \"\n   \"Middle Persian kūrag, attested in Manichaean script as 𐫞𐫇𐫡𐫃 (qwrg) 'furnace, kiln', and that MP word is a \"\n   \"Semitic loan: compare Classical Syriac ܟܘܪܐ kūrā 'melting pot, furnace', Jewish Aramaic kūrā, Hebrew kūr, all \"\n   \"from Akkadian kūru / kīru 'Ofen, Herd, Schmelzofen' (Zimmern, Akkadische Fremdwörter p.32, who traces the \"\n   \"same Akkadian word onward to Arabic kūr/kīr and Armenian kʿurayk). Dehkhodā's article on کوره cites both the \"\n   \"Pahlavi kūrak and the Akkadian kūru. The technical, metallurgical meaning ('smith's and coppersmith's \"\n   \"furnace; the kiln in which brick and plaster are fired', so Moʿin) is itself typical of Mesopotamian craft \"\n   \"vocabulary borrowed into Iranian. Nourai's own gloss is right; his ancestry is not. Note that a homophone \"\n   \"کوره 'district, province' (Moʿin: معرب خُره) is a quite different word, the Arabicised form of Persian \"\n   \"khurra/khōrag, which Nourai rightly keeps out of the chart.\"),\n \"derivation_fa\": (\n   \"ارجاع نورایی امانت‌دارانه است: مان در فرهنگ تطبیقی هندواروپایی (ص ۵۹۰) زیر مدخل «kur- (3) «گرما، آتش، سوخت»» \"\n   \"به‌راستی «Per. kūre „fireplace, forge“» را در کنار گوتی haúri «زغال» و لیتوانیایی kūras «سوخت» آورده است. اما \"\n   \"مان در این داوری تنهاست و ایران‌شناسی امروز راه را وارونه می‌بیند: «کوره»ی فارسی دنبالهٔ فارسی میانهٔ kūrag \"\n   \"است که در خط مانوی به‌صورت qwrg «کوره، آتشدان» گواهی شده، و همین واژهٔ فارسی میانه خود وام‌واژه‌ای سامی است: \"\n   \"بسنجید با سریانی کلاسیک kūrā «بوتهٔ ذوب، کوره»، آرامی یهودی kūrā و عبری kūr، همه از اکدی kūru/kīru «تنور، \"\n   \"اجاق، کورهٔ ذوب» (تسیمرن، وام‌واژه‌های اکدی، ص ۳۲، که همین واژه را تا عربی kūr/kīr و ارمنی دنبال می‌کند). \"\n   \"دهخدا نیز در مدخل «کوره» هم پهلوی کورک و هم اکدی kūru را یاد کرده است. معنای فنی و ریخته‌گرانهٔ واژه (به \"\n   \"گفتهٔ معین: «آتشگاه آهنگری و مسگری؛ جایی که در آن خشت و گچ و امثال آن پزند») خود نشانهٔ وام‌گیری از \"\n   \"واژگان پیشه‌وری بین‌النهرین است. معنایی که نورایی داده درست است، ولی تبارنامه‌اش نادرست؛ پژوهش امروزی این \"\n   \"پیوند هندواروپایی را رد می‌کند.\"),\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/کوره\",\n   \"https://abadis.ir/fatofa/کوره/\"\n ],\n \"ref_check\": [\n   {\"ref\": \"IEC:590\", \"status\": \"supports\", \"note\": IEC590 + \" — Mann does list Per. kūre under an IE root, so Nourai copied his source correctly.\"},\n   {\"ref\": \"MON:3121\", \"status\": \"partial\", \"note\": MONKUREH + \" — Moʿin confirms the gloss ('the fire-place of the smith and the coppersmith; the place in which they bake brick and gypsum') but gives no Indo-European derivation, only a cross-reference to کور.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter p.32 (AKD.txt line 448)\", \"stance\": \"contradicts\", \"note\": AKD32 + \" — an Akkadian → Aramaic/Hebrew → Arabic (and Iranian) route for exactly this word.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, k- section\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary has kulāčag, kulāf, kulang, kumig, kundur, kurkum, kurrag but no kūrag; the Manichaean MP qwrg is documented instead in Durkin-Meisterernst's dictionary, which Wiktionary cites.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part2 s.v. کوره (two homographs)\", \"stance\": \"partial\", \"note\": MONKUREH},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for 'Ofen' gives only no. 526 dāš 'Ofen' and a remark on čār; Horn has no article on kūra, i.e. he does not claim an Iranian etymology for it either.\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny 571-572, 3. ker(ə)-\", \"stance\": \"silent\", \"note\": POK571 + \" — Pokorny's article has Gothic haúri, ON hyrr and Baltic kur-/Slavic kur- but names no Persian form at all, and he warns that the Baltic and Slavic kūr-/kur- forms would have to be 'Ablautsneubildungen' for the connection to hold.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Germanic\", \"words\": \"herthô : hearth\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Proto-Germanic *herþō (AHD 1975 spells it 'herthô') 'burning place, hearth' < PIE *ker-tā, a -tā- derivative \"\n   \"of *ker(ə)- 'to burn': the PIE *k gives Germanic h by Grimm's law and the *-t- is protected from the law by \"\n   \"the preceding consonant/accent (Verner). Pokorny 572 lists 'ahd. herd, as. herth, ags. heord „Herd“' among \"\n   \"the reflexes of 3. ker(ə)-, and Watkins reconstructs '*ker-tā in Germanic *herthō'. Klein s.v. hearth gives \"\n   \"the whole set: OS/OFris. herth, MDu. hert, Du. haard, OHG herd, G Herd, 'fr. Teut. base *her-, corresponding \"\n   \"to I.-E. base *ker-, „to singe, burn, glow“'.\"),\n \"derivation_fa\": (\n   \"ژرمنی آغازین *herþō (که در چاپ ۱۹۷۵ فرهنگ American Heritage «herthô» نوشته شده) به معنی «جای سوختن، اجاق»، \"\n   \"از هندواروپایی آغازین *ker-tā، ساختی با پسوند -tā- بر ریشهٔ *ker(ə)- «سوختن». ک هندواروپایی بنا بر قانون گریم \"\n   \"در ژرمنی به h بدل شده است. پوکورنی در صفحهٔ ۵۷۲ صورت‌های «ahd. herd، as. herth، ags. heord „Herd“» را زیر \"\n   \"همین ریشه آورده و واتکینز نیز «*ker-tā در ژرمنی *herthō» بازسازی می‌کند. کلاین در مدخل hearth همهٔ گونه‌ها را \"\n   \"می‌آورد و آن‌ها را «از پایهٔ ژرمنی *her-، برابر پایهٔ هندواروپایی *ker- «سوزاندن، گداختن»» می‌داند. ادعای \"\n   \"نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/hearth\"],\n \"ref_check\": [{\"ref\": \"AHD:1522\", \"status\": \"supports\", \"note\": WATKINS4 + \" — the first branch of the article is exactly this node.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny 572\", \"stance\": \"supports\", \"note\": POK571},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. hearth\", \"stance\": \"supports\", \"note\": KLNHEARTH},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 418\", \"stance\": \"supports\", \"note\": \"Referenced as the parent article by both Pokorny ('WP. I 418 f.') and Mann ('Cf. WP I, 418') for this whole root, Germanic *herþō included.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"hearth\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Old English heorð 'hearth, fireplace, part of a floor on which a fire is made', also transferred 'house, \"\n   \"home, fireside' > Middle English herth > modern hearth; the modern spelling with -ear- reflects the ME \"\n   \"lengthening, the pronunciation /hɑːθ/ the later shortening. Etymonline: 'Old English heorð ... from \"\n   \"Proto-Germanic *hertha- „burning place“ ... from PIE *kerta-, from root *ker- (3) „heat, fire“'. Klein's \"\n   \"article is identical in substance.\"),\n \"derivation_fa\": (\n   \"انگلیسی کهن heorð «اجاق، آتشدان، بخشی از کف خانه که آتش بر آن می‌افروزند» و در کاربرد مجازی «خانه، کاشانه»، \"\n   \"که در انگلیسی میانه herth و در انگلیسی نو hearth شده است. اتیمآنلاین می‌نویسد: «انگلیسی کهن heorð … از ژرمنی \"\n   \"آغازین *hertha- «جای سوختن» … از هندواروپایی *kerta-، از ریشهٔ *ker- (3) «گرما، آتش»». مدخل کلاین نیز در \"\n   \"گوهر همین است. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/hearth\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": WATKINS4 + \" — 'in Old English heorth, hearth: HEARTH'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. hearth\", \"stance\": \"supports\", \"note\": KLNHEARTH},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. hearth\", \"stance\": \"supports\", \"note\": \"Skeat gives the same Germanic set (A.S. heorð, Du. haard, G. Herd) without dispute; no rival etymology is recorded anywhere for this word.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"carbô : charcoal\", \"verdict\": \"plausible\",\n \"derivation\": (\n   \"Latin carbō, carbōnis m. 'charcoal, glowing coal' is put under this root by Watkins ('Zero-grade form *kr̥- \"\n   \"in ... Latin carbō, charcoal, ember') and by Klein ('prob. standing for *car-dho and derived fr. I.-E. base \"\n   \"*ker-, „to singe, burn, glow“'), which is what Nourai's AHD:1522 says. But the connection is weaker than the \"\n   \"chart's plain arrow suggests. Pokorny prints it with an explicit hedge — 'zweifelhaft lat. carbō, -ōnis m. \"\n   \"„Kohle“ (idg. *kr̥-dhō?)' — and adds that Specht assigned the word instead to the colour-root ker-, i.e. to \"\n   \"the root of the first entry on this very page; the two competing suffix reconstructions (*kr̥-dhō vs *kr̥-bhō) \"\n   \"are themselves a sign of uncertainty, since neither -dhō- nor -bhō- is a productive Latin noun suffix. \"\n   \"Ernout-Meillet's article gives only the Romance descendants and offers no Indo-European etymology at all.\"),\n \"derivation_fa\": (\n   \"carbō لاتین (مضاف‌الیه carbōnis) «زغال، اخگر» را واتکینز زیر همین ریشه می‌آورد («صورت پایهٔ صفر *kr̥- در لاتین \"\n   \"carbō») و کلاین نیز آن را «احتمالاً از *car-dho و از پایهٔ هندواروپایی *ker- «سوزاندن، گداختن»» می‌داند؛ پس \"\n   \"ارجاع AHD:1522 امانت‌دارانه است. اما پیوند سست‌تر از آن است که پیکان ساده در نمودار می‌نماید: پوکورنی خود آن \"\n   \"را با قید «مشکوک» آورده است («zweifelhaft lat. carbō … idg. *kr̥-dhō؟») و می‌افزاید که اشپشت این واژه را به \"\n   \"ریشهٔ رنگ ker- می‌بندد، یعنی به همان ریشهٔ مدخل نخست همین صفحه. دو بازسازی رقیب پسوند (*kr̥-dhō در برابر \"\n   \"*kr̥-bhō) خود نشانهٔ تردید است، زیرا هیچ‌یک پسوند زایای اسم‌ساز لاتین نیست. ارنو-مه‌یه نیز هیچ ریشهٔ \"\n   \"هندواروپایی برای آن نمی‌آورد. پس ادعا با احتیاط پذیرفتنی است.\"),\n \"sources\": [\"https://www.etymonline.com/word/carbon\"],\n \"ref_check\": [{\"ref\": \"AHD:1522\", \"status\": \"supports\", \"note\": WATKINS4 + \" — 'Zero-grade form *kr̥- in: a. Latin carbō, charcoal, ember: CARBON, CARBUNCLE'.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny 571 (POK_02.txt line 3569)\", \"stance\": \"partial\", \"note\": POK571 + \" — Pokorny's own wording is 'zweifelhaft lat. carbō ... von Specht Idg. Dekl. 266 zur Farbwurzel ker- (*kr̥-bhō?) gestellt', i.e. he is not sure the word belongs here at all.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. carbo (LAT.txt line 9855)\", \"stance\": \"silent\", \"note\": LATCARBO},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. carbon\", \"stance\": \"supports\", \"note\": KLNCARBON}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"carbon, carburetor\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Both are French-mediated chemical coinages on Latin carbō. Lavoisier and his collaborators coined French \"\n   \"carbone in the Méthode de nomenclature chimique (1787) for the newly isolated element, from Latin carbōnem \"\n   \"'charcoal'; English took it over in 1789. Carburetor is a two-step derivative of the same base: carburet \"\n   \"'a compound of carbon with another substance' (1795, from carb- + -uret), whence carburettor / carburetor \"\n   \"of the fuel-air device in 1866. Etymonline gives exactly these dates.\"),\n \"derivation_fa\": (\n   \"هر دو واژه برساخته‌های شیمیایی‌اند که از راه فرانسه بر پایهٔ carbō لاتین ساخته شده‌اند. لاووازیه و همکارانش در \"\n   \"«روش نام‌گذاری شیمیایی» (۱۷۸۷) واژهٔ فرانسوی carbone را برای عنصر تازه‌شناخته از carbōnem لاتین «زغال» ساختند و \"\n   \"انگلیسی آن را در ۱۷۸۹ گرفت. carburetor نیز دو گام بعدتر ساخته شده است: نخست carburet «ترکیب کربن با مادهٔ \"\n   \"دیگر» (۱۷۹۵، از carb- و پسوند -uret) و سپس در ۱۸۶۶ carburettor برای دستگاه آمیزندهٔ سوخت و هوا. \"\n   \"اتیمآنلاین همین تاریخ‌ها را می‌آورد. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/carbon\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": WATKINS4 + \" — 'Latin carbō, charcoal, ember: CARBON, CARBUNCLE'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. carbon (KLN_1966.txt line 6509)\", \"stance\": \"supports\", \"note\": KLNCARBON},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. carbonado (SKT.txt line 2985)\", \"stance\": \"partial\", \"note\": \"'carbonado, broiled meat (Span.) — Span. carbonado, meat broiled over — Span. carbon, coal' — Skeat has the Romance family but, being a concise dictionary of native and older borrowings, no article on the 18th-century chemical term carbon.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"An empty pass-through box: the French link between Latin carbō and Persian کربن is carbone, the element name \"\n   \"coined by Lavoisier's commission in 1787 (Méthode de nomenclature chimique) on Latin carbōnem, together with \"\n   \"its family carbonate, carbonique, carbure and carburateur — the very four words the Persian box below lists \"\n   \"as کربنات، کربنیک، کربور، کاربوراتور.\"),\n \"derivation_fa\": (\n   \"این جعبه واسط است و واژه‌ای در آن نیامده: حلقهٔ فرانسویِ میان carbō لاتین و «کربن» فارسی همان carbone است که \"\n   \"کمیسیون لاووازیه در ۱۷۸۷ در «روش نام‌گذاری شیمیایی» از carbōnem لاتین ساخت، همراه با خانوادهٔ آن carbonate، \"\n   \"carbonique، carbure و carburateur — یعنی درست همان چهار واژه‌ای که در جعبهٔ فارسیِ زیر آن به‌صورت «کربنات، \"\n   \"کربنیک، کربور، کاربوراتور» فهرست شده است.\"),\n \"sources\": [\"https://www.etymonline.com/word/carbon\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"partial\", \"note\": WATKINS4 + \" — Watkins goes straight from Latin carbō to English CARBON without naming the French stage, which is however uncontroversial (Etymonline: 'French carbone, coined 1787 by Lavoisier ... from Latin carbonem').\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. carbon\", \"stance\": \"partial\", \"note\": KLNCARBON + \" — Klein too goes directly from Latin, the French stage being taken for granted for a Lavoisier coinage.\"},\n   {\"src\": \"PHN\", \"where\": \"Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc\", \"stance\": \"silent\", \"note\": \"Pihan covers only orientalisms in French; a Latin-based chemical coinage such as carbone is outside his scope, as expected.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"karbon «کربن ( کاربن )» : carbon\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"A 20th-century French loanword. Persian کربن karbon reproduces French carbone [kaʁbɔn]; the variant کاربن \"\n   \"kārbon shows the alternative rendering of the first syllable, and the derivatives listed in the chart settle \"\n   \"the route beyond doubt: کربنات < carbonate, کربنیک < carbonique (an English source would give 'carbonic'), \"\n   \"کربور < carbure, and above all کاربوراتور < carburateur, which can only be French (English carburetor would \"\n   \"have given *کاربورتور). The word entered Persian with the European chemical nomenclature through the Dār \"\n   \"al-Fonūn curriculum and its French-based textbooks from the later 19th century onward.\"),\n \"derivation_fa\": (\n   \"وام‌واژه‌ای فرانسوی از سدهٔ بیستم. «کربن» فارسی برابر carbone فرانسوی است و گونهٔ «کاربن» تلفظ دیگرِ هجای نخست \"\n   \"را نشان می‌دهد. مشتقاتی که خودِ نمودار آورده راه وام‌گیری را قطعی می‌کند: «کربنات» از carbonate، «کربنیک» از \"\n   \"carbonique (اگر از انگلیسی می‌آمد «کربنیک» نمی‌شد بلکه صورت carbonic را بازمی‌تاباند)، «کربور» از carbure و \"\n   \"از همه گویاتر «کاربوراتور» از carburateur که جز از فرانسه نمی‌تواند آمده باشد. این واژه‌ها همراه با \"\n   \"نام‌گذاری شیمیایی اروپایی و از راه کتاب‌های درسی فرانسوی‌بنیادِ دارالفنون از اواخر سدهٔ سیزدهم خورشیدی وارد \"\n   \"فارسی شدند. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/carbon\"],\n \"ref_check\": [{\"ref\": \"VOP:267,278\", \"status\": \"not_checked\", \"note\": VOPNOTE + \". VOP (Moshiri's dictionary of European words in Persian) is however precisely the right kind of reference for this claim, and the Persian derivatives listed in the box independently confirm the French route.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi (vol. 4 covers foreign compounds)\", \"stance\": \"silent\", \"note\": \"the two-part OCR of the lexicon volumes on disk has no کربن headword; Moʿin's foreign-word volume, where it would stand with a [فر.] tag, is not in this scan.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā-ye Hend-o-Orupāyi\", \"stance\": \"silent\", \"note\": \"Aryanpur treats inherited Iranian vocabulary, not modern European loans; no کربن entry.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 8, \"lang\": \"Latin\", \"words\": \"cremâre : to burn\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Latin cremāre 'to burn, consume by fire', used above all of burning the dead, from an -em- enlargement of the \"\n   \"root: PIE *k(e)r-em- > Latin crem-ā-re. Pokorny 572 states it in those terms — 'Ein aus ker- erweitertes \"\n   \"*k(e)r-em- sucht man in lat. cremō, -āre „verbrennen (tr.)“, umbr. krematra' — and Watkins has 'extended form \"\n   \"*krem- in Latin cremāre, to burn: CREMATE'. Ernout-Meillet agree and add the Italic argument: 'Peut-être d'un \"\n   \"élargissement en -em- de la racine attestée par v.isl. hyrr „feu“, got. hauri „charbon“, lit. kuriu, kurti \"\n   \"„faire du feu“. Le mot semble osco-ombrien, car l'ombrien a le nom d'instrument krematra'.\"),\n \"derivation_fa\": (\n   \"cremāre لاتین «سوزاندن، به آتش سپردن» — به‌ویژه دربارهٔ سوزاندن مردگان — از گسترش -em- بر همین ریشه ساخته شده \"\n   \"است: هندواروپایی *k(e)r-em- ← لاتین crem-ā-re. پوکورنی در صفحهٔ ۵۷۲ همین را می‌گوید: «صورت گسترش‌یافتهٔ \"\n   \"*k(e)r-em- از ker- را در lat. cremō، -āre «سوزاندن» و umbr. krematra می‌جویند». واتکینز نیز «صورت گسترده \"\n   \"*krem- در لاتین cremāre» می‌آورد. ارنو-مه‌یه همین را می‌پذیرند و دلیل ایتالیکی می‌افزایند: «شاید از گسترشی \"\n   \"با -em- بر ریشه‌ای که در ایسلندی کهن hyrr «آتش»، گوتی hauri «زغال» و لیتوانیایی kuriu, kurti «آتش افروختن» \"\n   \"گواهی شده است. این واژه اسکی-اومبریایی می‌نماید، زیرا اومبریایی نام ابزار krematra را دارد.» ادعای نورایی \"\n   \"درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/cremate\"],\n \"ref_check\": [{\"ref\": \"AHD:1522\", \"status\": \"supports\", \"note\": WATKINS4 + \" — 'extended form *krem- in Latin cremāre, to burn: CREMATE'.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny 572\", \"stance\": \"supports\", \"note\": POK571},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. cremo (LAT.txt line 14451)\", \"stance\": \"supports\", \"note\": LATCREMO},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cremate\", \"stance\": \"supports\", \"note\": KLNCREMATE}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 9, \"lang\": \"English\", \"words\": \"cremate\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"English cremate is a back-formation from cremation (1851), itself from Latin cremātiō, -ōnis, and formally \"\n   \"from Latin cremātus, past participle of cremāre; the verb spreads with the cremation movement of the 1870s \"\n   \"(the Cremation Society of England, 1874). Klein: 'cremate, tr. v., to burn to ashes. — L. crematus, pp. of \"\n   \"cremāre ... See carbon, hearth and verbal suff. -ate.'\"),\n \"derivation_fa\": (\n   \"فعل cremate در انگلیسی برساختهٔ پس‌گرد (back-formation) از اسم cremation (۱۸۵۱) است، و آن خود از cremātiō \"\n   \"لاتین؛ از دید صرفی نیز بر پایهٔ cremātus، اسم مفعول cremāre، ساخته شده است. رواج فعل با جنبش مرده‌سوزی دههٔ \"\n   \"۱۸۷۰ (تأسیس انجمن مرده‌سوزی انگلستان در ۱۸۷۴) همراه است. کلاین می‌نویسد: «cremate … از crematus لاتین، اسم \"\n   \"مفعول cremāre … بنگرید به carbon و hearth و پسوند فعلی -ate». ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/cremate\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": WATKINS4 + \" — 'Latin cremāre, to burn: CREMATE'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cremate (KLN_1966.txt line 9625)\", \"stance\": \"supports\", \"note\": KLNCREMATE},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. cremo\", \"stance\": \"supports\", \"note\": LATCREMO + \" — the derivatives listed include cremātiō, cremātor, the direct sources of the English words.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 10, \"lang\": \"Greek\", \"words\": \"keramos : potter's clay\", \"verdict\": \"disputed\",\n \"derivation\": (\n   \"Ancient Greek κέραμος 'potter's clay, earthenware, jar, tile' is where the chart's root fails. Watkins, \"\n   \"Nourai's own source, already flags it: 'Possibly suffixed and extended form *kerə-mo- in Greek keramos'. \"\n   \"Klein rejects it outright: κέραμος is 'a pre-Hellenic word derived from a language of Asia Minor and not \"\n   \"cognate with L. cremāre', citing Kretschmer in Glotta; and he repeats the warning under cremate ('Gk. \"\n   \"κέραμος „potter's clay“ is not cogn. with L. cremare'). Beekes reaches the same conclusion for a different \"\n   \"reason, arguing for a Pre-Greek or Anatolian substrate origin and finding the old comparisons — both with \"\n   \"κεράννυμι 'to mix' and with Latin cremāre — unconvincing; Etymonline reports 'No certain etymology' and \"\n   \"'perhaps from a pre-Hellenic word'. The morphology is against the IE account too: -αμος is not a Greek \"\n   \"suffix that forms nouns of this type from verbal roots. So the arrow root → keramos should be deleted, \"\n   \"though nodes 11-13 below it stand on their own.\"),\n \"derivation_fa\": (\n   \"یونانی باستان κέραμος «گِل کوزه‌گری، سفال، خُم، سفالینه» همان‌جاست که ریشهٔ نمودار فرومی‌ماند. خودِ واتکینز، \"\n   \"که مأخذ نورایی است، با قید «possibly» آن را آورده است. کلاین یکسره ردش می‌کند: κέραμος «واژه‌ای پیش‌یونانی \"\n   \"برگرفته از زبانی در آسیای صغیر است و با cremāre لاتین هم‌ریشه نیست» (به استناد کرچمر در مجلهٔ Glotta)، و همین \"\n   \"هشدار را در مدخل cremate تکرار می‌کند. بیکس نیز به همان نتیجه می‌رسد و خاستگاه آن را زیرلایهٔ پیش‌یونانی یا \"\n   \"آناتولیایی می‌داند و مقایسه‌های کهن — چه با κεράννυμι «آمیختن» و چه با cremāre — را نااستوار می‌شمارد. \"\n   \"اتیمآنلاین هم می‌نویسد «هیچ ریشه‌شناسی قطعی وجود ندارد». صرف واژه نیز با تحلیل هندواروپایی نمی‌خواند، زیرا \"\n   \"-αμος پسوند اسم‌ساز یونانی برای ساخت چنین نام‌هایی از ریشهٔ فعلی نیست. پس پژوهش امروزی این پیکان را رد \"\n   \"می‌کند؛ هرچند گره‌های ۱۱ تا ۱۳ زیر آن به‌خودی‌خود درست‌اند.\"),\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/κέραμος\",\n   \"https://www.etymonline.com/word/ceramic\"\n ],\n \"ref_check\": [{\"ref\": \"AHD:1522\", \"status\": \"partial\", \"note\": WATKINS4 + \" — the branch is present, but Watkins himself writes 'Possibly suffixed and extended form *kerə-mo-', a hedge the chart's plain arrow drops.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ceramic (line 7002) and cremate (line 9625)\", \"stance\": \"contradicts\", \"note\": KLNCERAMIC + \"; and \" + KLNCREMATE},\n   {\"src\": \"POK\", \"where\": \"Pokorny 571-572, 3. ker(ə)-\", \"stance\": \"silent\", \"note\": POK571 + \" — Pokorny's article names no Greek word at all; κέραμος is simply absent from it, so POK:571 does not support this branch even indirectly.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC 590, kur- (3)\", \"stance\": \"silent\", \"note\": IEC590 + \" — Mann's article likewise lists no Greek reflex.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"ceramic\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Whatever the ultimate origin of κέραμος, the step drawn here is right: English ceramic (1850s) is Greek \"\n   \"κεραμικός 'of pottery, made of earthenware' (from κέραμος), its modern spelling shaped by French céramique \"\n   \"(1806); the plural noun ceramics 'the art of making things from baked clay' follows in 1857. Klein: 'ceramic, \"\n   \"adj. — Gk. κεραμικός, „of pottery, made of earthenware“, fr. κέραμος'.\"),\n \"derivation_fa\": (\n   \"هر خاستگاهی که κέραμος داشته باشد، این گام درست است: ceramic انگلیسی (میانهٔ سدهٔ نوزدهم) از κεραμικός یونانی \"\n   \"«سفالی، از جنس سفال» (مشتق از κέραμος) گرفته شده و املای امروزی‌اش را از céramique فرانسوی (۱۸۰۶) دارد؛ اسم \"\n   \"جمع ceramics «هنر ساختن اشیای سفالین» در ۱۸۵۷ پدید آمده است. کلاین می‌نویسد: «ceramic، صفت — یونانی \"\n   \"κεραμικός «سفالی» از κέραμος». ادعای نورایی در این گره درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/ceramic\"],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": WATKINS4 + \" — 'Greek keramos, potter's clay, earthenware: CERAMIC'; the Greek→English step is not in doubt, only the PIE parentage of keramos.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ceramic\", \"stance\": \"supports\", \"note\": KLNCERAMIC + \" — Klein supports the Greek→English step while denying the IE root.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary s.v. ceramic\", \"stance\": \"supports\", \"note\": \"Webster likewise derives ceramic from Gk. keramikos, keramos 'potter's clay', with no further ancestry claimed.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 12, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Another empty pass-through box, and the only node on the page with no reference at all. The intended French \"\n   \"link is céramique, attested from 1806 as an adjective and from the 1830s-40s as a noun for the art and its \"\n   \"products; it was formed on Greek κεραμικός by the neo-classical scholarly vocabulary of the period and is \"\n   \"the immediate source both of the modern English spelling and of the Persian word below.\"),\n \"derivation_fa\": (\n   \"این نیز جعبهٔ واسط و بی‌واژه است و تنها گره این صفحه است که هیچ ارجاعی ندارد. حلقهٔ فرانسویِ مورد نظر \"\n   \"céramique است که از ۱۸۰۶ به‌صورت صفت و از دههٔ ۱۸۳۰-۱۸۴۰ به‌صورت اسم برای این هنر و فرآورده‌هایش گواهی شده \"\n   \"است؛ این واژه را واژگان عالمانهٔ نوکلاسیک آن دوره بر پایهٔ κεραμικός یونانی ساخت و همان است که هم املای \"\n   \"امروزی واژهٔ انگلیسی و هم واژهٔ فارسیِ زیر آن از آن گرفته شده‌اند.\"),\n \"sources\": [\"https://www.etymonline.com/word/ceramic\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book; the French stage is nevertheless well documented — Etymonline s.v. ceramic: 'the spelling influenced by French céramique (1806)'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ceramic\", \"stance\": \"partial\", \"note\": KLNCERAMIC + \" — Klein derives the English word straight from Greek without naming the French stage.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary s.v. ceramic\", \"stance\": \"partial\", \"note\": \"Webster likewise gives only the Greek source; the French intermediary is documented by Etymonline and by the French lexicographical tradition.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"serâmîc «سرامیک» : ceramic\", \"verdict\": \"confirmed\",\n \"derivation\": (\n   \"Persian سرامیک serāmik is a 20th-century loan from French céramique, and the initial s- proves it: French \"\n   \"céramique is pronounced [seʁamik], whereas an English or German source would have given a k- initial \"\n   \"(*کرامیک), as in the older learned Persian rendering of Greek κ. The stress-final -ik reproduces French \"\n   \"-ique, the standard Persian adaptation of that suffix (cf. کلاسیک, تکنیک, پلاستیک). The word came in with \"\n   \"the industrial-technical vocabulary of the Pahlavi period.\"),\n \"derivation_fa\": (\n   \"«سرامیک» فارسی وام‌واژه‌ای سدهٔ بیستمی از céramique فرانسوی است و «س» آغازین گواه قاطع آن است: céramique در \"\n   \"فرانسه [seʁamik] تلفظ می‌شود، حال آنکه اگر از انگلیسی یا آلمانی می‌آمد با «ک» آغاز می‌شد (*کرامیک)، چنان‌که \"\n   \"برگردان‌های عالمانهٔ کهن‌تر κ یونانی در فارسی نشان می‌دهد. پایانهٔ -یک نیز برابرنهاد همیشگی پسوند فرانسوی \"\n   \"-ique در فارسی است (مانند کلاسیک، تکنیک، پلاستیک). این واژه با واژگان صنعتی-فنی دوران پهلوی وارد فارسی شد. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/ceramic\"],\n \"ref_check\": [{\"ref\": \"VOP:211\", \"status\": \"not_checked\", \"note\": VOPNOTE + \". As with کربن, VOP is the right sort of authority for a European loan into Persian; the phonetic shape of the Persian word independently confirms the French route.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi\", \"stance\": \"silent\", \"note\": \"no سرامیک headword in the two-part OCR of the lexicon volumes on disk; the word would belong in Moʿin's volume of foreign words, which is not in this scan.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ceramic\", \"stance\": \"supports\", \"note\": KLNCERAMIC + \" — establishes the Greek → French/English base from which the Persian word was taken.\"}\n ]\n})\n\ndata[\"entries\"].append(e1)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-258.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\n"
}
```


### [2026-09-06T16:34:53.952Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk258.py (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:34:59.144Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk258.py && python3 -m json.tool data/verification/page-258.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 258",
 "description": "Generate and validate page-258.json"
}
```


### [2026-09-06T16:35:01.763Z] TOOL RESULT

```
written
JSON OK
nodes verified: 21/21
node verdicts: {'plausible': 6, 'transcription_suspect': 1, 'confirmed': 12, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'partial': 4, 'contradicts': 1, 'not_checked': 5}
books consulted: {'silent': 22, 'supports': 24, 'contradicts': 5, 'partial': 7} | by book: {'KLN': 13, 'MON': 6, 'POK': 6, 'WLD': 5, 'HRN': 3, 'AHD': 3, 'LAT': 3, 'PHD': 2, 'ARY': 2, 'SYN': 2, 'SKT': 2, 'WEB': 2, 'NYB': 1, 'HUB': 1, 'KNT': 1, 'BRT': 1, 'AFM': 1, 'HJB': 1, 'AKD': 1, 'PHN': 1, 'IEC': 1}
```


## [2026-09-06T16:35:24.395Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-258.json` written; `verify_check.py 258` reports 21/21 nodes, 0 PROBLEM lines.

**Page 258 (book p. 228) — 2 entries, 21 nodes, 1 redirect skipped**

- Root verdicts: confirmed 2/2. Both root boxes are traceable to their cited pages: POK 573 "6. ker-, kerə-, Farbwurzel für dunkle, schmutzige … s. die Erweiterungen kerb(h)- und kers-" + POK 583 "1. kers- … kr̥s-no- 'schwarz'" (so Ker 4 / Kers 1 / Kerb are Pokorny's own cross-references); and POK 571 "3. ker(ə)- brennen, glühen, heizen" + Mann IEC 590 "kur- (3) heat, fire, fuel, burning" (so Ker 5 / Kur / Kertâ = Pokorny + Mann + Watkins's *ker-tā).
- Node verdicts: confirmed 12, plausible 6, disputed 2, transcription_suspect 1.

Flagged items:
- **transcription_suspect — Ker 4, node 3 "Old Persian kirsman: black"**: no such Old Persian word. POK 583, the cited page, reads "Ai. kr̥ṣṇá- = **apr. kirsnan**" — *apr.* = altpreußisch, Old Prussian. Nourai read "apr." as Old Persian and wrote -m- for -n-. Kent has nothing; Bartholomae has karsna- only as a personal name; Buck §15.65 and Walde-Pokorny I 428 both print "OPruss. kirsnan". `error_in: book` — the printed page shows "Old Persian … kirsman", so the extraction is faithful.
- **disputed — Ker 5, node 1 "Persian کوره kūreh"**: Mann IEC 590 really does list "Per. kūre 'fireplace, forge'" (ref faithful), but modern scholarship makes it a Semitic loan: Manichaean MP *qwrg* kūrag < Syriac kūrā < Akkadian kūru/kīru "Ofen, Herd, Schmelzofen" (Zimmern AKD p.32; Dehkhoda cites both Pahlavi kūrak and Akkadian kūru).
- **disputed — Ker 5, node 10 "Greek keramos"**: Klein calls it "a pre-Hellenic word … not cognate with L. cremāre"; Beekes Pre-Greek/Anatolian; Watkins himself only says "Possibly"; Pokorny 571 has no Greek form at all.
- Notable plausibles: čardeh (node 2) — Pokorny does list it, but Mo'in glosses چرده as "colour in general" and k- > č- is not a regular Persian change; kars (node 4) — word real in BQT 1619 but its drawn parent is the phantom node 3; karsneh (node 6) — Mo'in's own footnote in BQT 1619 derives it from Skt kṛṣṇa *via* Hebrew/Aramaic, and Wiktionary offers a rival Semitic etymology (Syriac karsānā < *kariś- "paunch"); carbō (node 4 of Ker 5) — Pokorny calls it "zweifelhaft", Ernout-Meillet give no IE etymology.

Extraction errors for the owner to fix:
- Entry 0 node 4 `script`: JSON has «کَرس ( کیرس ، کیرسنه ۱)»; the printed page has «کَرس ( کِرس ، کِرسنه ۱)» — a kasra rendered as ی (two occurrences).

Not consultable: VOP (Moshiri) for the two modern French loans — no scan exists anywhere; AHD:727 (New College main dictionary) — lending-only, but the same book's appendix (Watkins 1985) does carry KRISHNA under "kers-1. Dark, dirty". Page image archived at `data/verification/sources/refs/ocr/BOOK/258.png`; 10 web sources archived via `fetch_source.py`.
