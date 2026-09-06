# Verification process log — verify-page-275


## [2026-09-06T21:12:41.349Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 275 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-275.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-275.json. Write /home/sfmqrb/git/rishe/data/verification/page-275.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 275` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:12:42.971Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:12:43.647Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:12:43.664Z] TOOL RESULT

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


## [2026-09-06T21:12:43.901Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-275.txt"
}
```


### [2026-09-06T21:12:43.928Z] TOOL RESULT

```
1	=== PDF page 275 (book page 245) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kost : bone, rib, side of anything  (refs POK:616; AHD:1524)
4	#1 (parent #0) [Pahlavi] refs=BQT:1643; AEF:261 | kost : side ; uparô-kušta-pâma : protection for the sides ☞Upo,Pa
5	  #2 (parent #1) [Persian] refs=BQT:261, 1643, 1649 | kostî «کستی» : side, also a belt ; košti «کشتی» : belt, wrestling (by grabbing the opponent's belt) ; bargostovân «برگستوان» : armor (worn to protect the sides)
6	#3 (parent #0) [Latin] refs=AHD | costa : rib, side
7	  #4 (parent #3) [French] refs=AHD:327 | cotelette : cutlet (originally from rib meat)
8	    #5 (parent #4) [Persian] refs=None | kotlet «کتلت» : cutlet
9	    #6 (parent #4) [English] refs=None | cutlet
10	  #7 (parent #3) [English] refs=None | coast
11	--- entry 1 ---
12	ROOT Kot -> redirect to Ket
13	--- entry 2 ---
14	ROOT Kou -> redirect to Keu 3
15	--- entry 3 ---
16	ROOT [Sanskrit] Kram, Krâmati : to walk, to step  (refs BQT:724; MON:1406; HRN:104)
17	#1 (parent #0) [Avestan / Old Persian] refs=FFD:50 | xram : to step, walk
18	  #2 (parent #1) [Pahlavi] refs=FFD:50 | a-xrâm : to walk flauntily
19	    #3 (parent #2) [Persian] refs=MON:1406; FFD:50; BQT:724 | xarâmîdan «خرامیدن» : to walk flauntily | extra: خرام، خرامان
20	--- entry 4 ---
21	ROOT Krâmati -> redirect to Kram
22	--- entry 5 ---
23	ROOT Kred -> redirect to Kerd 1
24	--- entry 6 ---
25	ROOT [Indo-European] Krei : shine, glow, beauty  (refs POK:618)
26	#1 (parent #0) [Avestan] refs=POK:618; KLN:371 | srî, srayan : beauty ; srîra : beautiful ; sra-yah : more beautiful, better ☞Yah 5 ; sra-ěšta : most beautiful, best ☞Ištâ
27	
```


## [2026-09-06T21:12:47.798Z] TOOL CALL #3: Bash

```json
{
 "command": "wc -l data/verification/agent/charts/page-275.txt && echo \"---JSON---\" && python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-275.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1))\n\" | head -300"
}
```


### [2026-09-06T21:12:49.479Z] TOOL RESULT

```
26 data/verification/agent/charts/page-275.txt
---JSON---
{
 "pdf_page": 275,
 "book_page": 245,
 "entries": [
  {
   "root": {
    "name": "Kost",
    "lang": "Indo-European",
    "refs": "POK:616; AHD:1524",
    "gloss": "bone, rib, side of anything",
    "note": "AHD claims that this may be related to the root \"Ost:bone\"."
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Pahlavi",
     "refs": "BQT:1643; AEF:261",
     "words": [
      {
       "translit": "kost",
       "gloss": "side",
       "script": null
      },
      {
       "translit": "uparô-kušta-pâma",
       "gloss": "protection for the sides",
       "script": null,
       "see": [
        "Upo",
        "Pa"
       ]
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Persian",
     "refs": "BQT:261, 1643, 1649",
     "words": [
      {
       "translit": "kostî",
       "gloss": "side, also a belt",
       "script": "کستی"
      },
      {
       "translit": "košti",
       "gloss": "belt, wrestling (by grabbing the opponent's belt)",
       "script": "کشتی"
      },
      {
       "translit": "bargostovân",
       "gloss": "armor (worn to protect the sides)",
       "script": "برگستوان"
      }
     ],
     "note": null,
     "quote": {
      "text": "درخرابات نبینی که ز مستی همه سال - راهب دیر ترا کُشتی و زنّار دهد",
      "poet": "Sanâî"
     }
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Latin",
     "refs": "AHD",
     "words": [
      {
       "translit": "costa",
       "gloss": "rib, side",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "French",
     "refs": "AHD:327",
     "words": [
      {
       "translit": "cotelette",
       "gloss": "cutlet (originally from rib meat)",
       "script": null
      }
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
      {
       "translit": "kotlet",
       "gloss": "cutlet",
       "script": "کتلت"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 4,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "cutlet",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 3,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "coast",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    }
   ]
  },
  {
   "root": {
    "name": "Kot",
    "redirect": "Ket"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Kou",
    "redirect": "Keu 3"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Kram, Krâmati",
    "lang": "Sanskrit",
    "refs": "BQT:724; MON:1406; HRN:104",
    "gloss": "to walk, to step"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan / Old Persian",
     "refs": "FFD:50",
     "words": [
      {
       "translit": "xram",
       "gloss": "to step, walk",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Pahlavi",
     "refs": "FFD:50",
     "words": [
      {
       "translit": "a-xrâm",
       "gloss": "to walk flauntily",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 2,
     "lang": "Persian",
     "refs": "MON:1406; FFD:50; BQT:724",
     "words": [
      {
       "translit": "xarâmîdan",
       "gloss": "to walk flauntily",
       "script": "خرامیدن"
      }
     ],
     "script_extra": "خرام، خرامان",
     "note": null,
     "quote": {
      "text": "چند خرامی و تکبّر کنی - دولت پارینه تصوّر کنی",
      "poet": "Sa`dî"
     }
    }
   ]
  },
  {
   "root": {
    "name": "Krâmati",
    "redirect": "Kram"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Kred",
    "redirect": "Kerd 1"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Krei",
    "lang": "Indo-European",
    "refs": "POK:618",
    "gloss": "shine, glow, beauty"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:618; KLN:371",
     "words": [
      {
       "translit": "srî, srayan",
       "gloss": "beauty",
       "script": null
      },
      {
       "translit": "srîra",
       "gloss": "beautiful",
       "script": null
      },
      {
       "translit": "sra-yah",
       "gloss": "more beautiful, better",
       "script": null,
       "see": [
        "Yah 5"
       ]
      },
      {
       "translit": "sra-ěšta",
       "gloss": "most beautiful, best",
       "script": null,
       "see": [
        "Ištâ"
       ]
      }
     ],
     "note": null,
     "quote": null
    }
   ]
  }
 ]
}
```


## [2026-09-06T21:12:56.627Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','BQT','AEF','MON','HRN','FFD','KLN','WLD','BRT','PHD','NYB','IEC','SYN','HUB','CHEUNG','ARY','SKT','FSD','WEB','KNT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


## [2026-09-06T21:12:56.892Z] TOOL CALL #5: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T21:12:58.461Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


### [2026-09-06T21:12:58.491Z] TOOL RESULT

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


## [2026-09-06T21:13:25.617Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-06T21:13:25.653Z] TOOL RESULT

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


## [2026-09-06T21:13:26.390Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py && echo \"=== fetch_source ===\" && sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-09-06T21:13:26.443Z] TOOL RESULT

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
=== fetch_source ===
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


## [2026-09-06T21:13:32.709Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','BRT','PHD','NYB','HRN','HUB','FFD','BQT','MON','IEC','SYN','LEW','LAT','SKT','CHEUNG','ARY','WLD']:\n    v=d.get(k) or {}\n    print('==',k, '| offset:', v.get('page_offset'), '| local:', v.get('local_file'), '| hint:', (v.get('lookup_hint') or '')[:300])\n\""
}
```


### [2026-09-06T21:13:35.018Z] TOOL RESULT

```
== POK | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== AHD | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== BRT | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HRN | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== HUB | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== FFD | offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] | hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
== BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON | offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== IEC | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== LEW | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt | hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== LAT | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt | hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== SKT | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== CHEUNG | offset: None | local: None | hint: 
== ARY | offset: printed page = pdf page + 1 | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== WLD | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
```


## [2026-09-06T21:13:38.738Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: kost\" POK_full.txt\necho \"--- around 616 ---\"\ngrep -n \"Page(s): 61[5-9]\" POK_full.txt | head -40"
}
```


### [2026-09-06T21:13:38.794Z] TOOL RESULT

```
48137:Root / lemma: kost- 
--- around 616 ---
48110:Page(s): 615-616 
48212:Page(s): 616-617 
48258:Page(s): 617-618 
48339:Page(s): 618-619
```


## [2026-09-06T21:13:40.240Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: k̑rei\\|lemma: krei\\|lemma: (s)krei\\|lemma: k̂rei\" POK_full.txt | head -20\necho \"=== all lemmas w page 617-620 ===\"\ngrep -n -B30 \"Page(s): 61[7-9]\" POK_full.txt | grep \"lemma:\" | head -40"
}
```


### [2026-09-06T21:13:40.305Z] TOOL RESULT

```
48281:Root / lemma: krei-1 
48306:Root / lemma: krei-2, kreig-, kreik- 
=== all lemmas w page 617-620 ===
48228-Root / lemma: kred- : beams, roof, derived from a suffixed Root / lemma: kra[u]- : kreu- : 
48312-Root / lemma: krek-1 {-k-7)
```


## [2026-09-06T21:13:42.368Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '48130,48165p' POK_full.txt\necho \"=========== krei-1 ===========\"\nsed -n '48275,48345p' POK_full.txt"
}
```


### [2026-09-06T21:13:42.444Z] TOOL RESULT

```
References: WP. I 464, WH. I 280. 
Page(s):616 



Root / lemma: kost- 

Meaning: leg; bone 

Material: Latin costai. " rib '; Old Bulgarian kostbi. "bone' (Serbo-Croatian kost^ rib '). 

assumption of a k- prefixe (to Latin c»5 etc.) is incredible. 

Maybe alb. Geg koc, Tosc /rc»5-/re "bone, leg bone', kashte^ straw, *bone? ' (common alb. 
diminutive -kS) 

References: WP. I 464, WH. I 281. 
Page(s):616 

Root / lemma: krat- 

See also: see above S. 584 under kert-. 

Page(s):616 

Root / lemma: krafuj- : krau- : kru- 

Meaning: to heap up, put together; heap; roof, cottage, shed 

Note: 



Root / lemma: krafu]-. krau-. kru-\ to heap up, put together; heap; roof, cottage, shed, 
=========== krei-1 ===========
Meaning: " onomatopoetic word ' 

See also: see above S. 569 under ker-1. 

Page(s):618 

Root / lemma: krei-1 

Meaning: to touch, brush 

Material: Old Icelandic hnna^ have an effect, seem ', Old English asachs. Old High 

German hnnan^ touch, stripe' (/7C>- pre sent); after Wissmann Nom. postverb. 152 ff. here 

Old English hrenian^ give off a smell ', Old Frisian strong. V. hrena' sense a smell '; Old 

English Old Icelandic hrJm, Middle High German rJm ' hoarfrost '; 



Lithuanian krenat ' skimmings, cream' (' was man abstreift, abschopft '), Latvian kreju, 
kreju, kr'ief skim, remove the cream from the top of milk ', kreimsm. " skimmings' (from 
the verb krejums ' was man abstreifen kann '); 



besides with Germanic p. asachs. hripo. Old High German hnfo " hoarfrost '. 

References: WP. I 478, Trautmann 141. 
Page(s):618 

Root / lemma: krei-2, kreig-, kreik- 

See also: see above S. 567 ff. under ker-1. 

Page(s):618 

Root / lemma: krek-1 {-k-7) 
Meaning: to hit 

Material: Gr. KpsKw 'hit, beat; weave, strike a stringed instrument with the plectron, of any 
sharp noise ', (Of. Old Norse hrse// {*hrah'\\az) 'weaver's sley'. Old English hrsege/' dress', 
'garment', perh. Lett, krekis 'shirt'.) 



KpoKP) " EinscmagTaaen^eweDe ', Kpo^ ds., KpoKouv "to weave', KpoKU(;, -u5o(; f. "flock, 
tuft of wool'; 

Old Icelandic hrgell{ *hrarjhila2) "a weaver's reed ', Old English hreol{ *hrehula^ " 
windlass, reel '; Old English hraeglu. "dress, garment ', engl. rail. Old Frisian hreil. Old 
High German hregilu. " a garment, the skin, hide, fell '; 

Latvian kr^kls " shirt '; 

if the Latvian word has received a second Arthrough West Indo Germanic influence, it 
can also be followed by the Slavic family: russ. kresu, kresatb b " mit dem Feuerstahl 
Feuer schlagen ', kir. kresaty, kresnufyl\re hit', dial, "hew, hit, strike ', Serbo-Croatian 
kresem, kresat/l'\re hit; scabble, cut or chisel stone roughly; branch cut off the branch ' 
(etc., s. Berneker611). 

Maybe alb. kr/smen. "strike, shot ' a Slavic loanword. 

References: WP. I 483 f. 
Page(s): 618-619 

Root / lemma: krek-2, kfk- 

Meaning: roe; slimy stuff in water 

Material: Old Icelandic hrognu.. Old High German (h)rogan, rogen^ spawn, fish eggs,
```


## [2026-09-06T21:14:01.657Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"srira\\|srīra\\|sraesta\\|sraēšta\\|sraeSta\" POK_full.txt | head -20\necho \"=== POK_02 real page 616-619 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR>=272 && NR<=276 {print \"### leaf \" NR; print}' POK_02.txt | head -200"
}
```


### [2026-09-06T21:14:03.226Z] TOOL RESULT

```
51898:srayah-, Superl. Old Indie srestha- {srai'stha-), Avestan sraesta-. Old Indie sreman-m. " 
=== POK_02 real page 616-619 ===
### leaf 272
,  WH.  I  314,  859.
jco  kOf  kak(k)-f  ku(r)kur-   u.  dgl.   als   Nachahmung   des  Naturlautes  der Hühner;  Worte  ohne  nachweisbare  ältere  Geschichte.
I.  Gr.  y,aycxdßr]  f.,  Kaytytaßig  f.  ,Rebhuhn',  ytax-naßll^siv  vom  Naturlaut  der Rebhühner  (ebenso  das  entlehnte  lat.  cacabäre),  xaxxd^etv  , gackern';
lat.  cacilläre  ,gackern  (von  der  Henne)';
ndd.  kakkeln  ,gackern',  nl.  kokkelen  ,kollern  (vom  Hahn)',  woneben ahd.  gackizön  ,gackern  (von  der  ein  Ei  legenden  Henne)',  nhd.  gackern, dial.  gaggezen,  nhd.   Gockel  (s.  auch  unter  ghegh-).
II.  Lat.  coco  coco  ,Naturlaut  der  Hühner'  (Petron  59,  2),  franz.  coq  ,Hahn', dän.  kok,  schwed.  mdartl.  kokk  ,Hahn',  anord.  (afrz.  Lw.)  kokr,  ags.  cocc, nl.  alt  cocke  ds. ;  aksl.  kokotT>  ,Hahn',  kokoh  ,Henne',  russ.  kokotdth ,gackern'  usw.
III.  Ai.  kurkuta-,  kukkuta-  m.  ,Hahn',  kukkubha-  m.  (mind.  für  */cwr- kubha-)  , Fasan' ;  lat.  cücurriö,  -Ire  ,kollern'  (vom  Hahn),  cücuru  Inter- jektion; nhd.  kikeriki  (älter  kükerukü,  kükerlüküh),  md.  kuckern,  kockern, köcken  ,krähen^;  lit.  kakarykü  ,kikeriki',  klruss.  usw.  kukuriku  ds.,  serb. kukitrijeSem-,  -ijekati,   russ.    kukorekath   usw.   ,krähen',   gr.   xovql^w  ds.
IV.  Gr.  y,ULQQog,  y,Ly,y.ög  ,Hahn'  Hes. ;  osk.  cicirrus,  Cognomen  des  Messius, wohl  , Kampfhahn'.
WP.  I  455  f.,  WH.  I  126,  212,  242,  300.
koksä  jKörperteilbenennung'  (arisch  auch  *kokso-s).
Ai.  kdk§ä  f.,  kaksa-  m.  , Achselgrube,  Gurtgegend  der  Pferde',  av.  kasa- m.  , Achsel'  (erweist  -ks-)]
lat.  coxa  f.  , Hüfte';
air.  coss  f.  ,Fuß',  abrit.  Aq'/svrd-Y.o^og  etwa  ,  Weiß  fuß'  (aber  cymr.  coes ,Bein'  ist  aus  dem  Lat.  entlehnt) ;
ahd.  hähsina  ,Kniebug  des  Hinterbeins',  mhd.  hehse,  nhd.  Hachse,  Hesse, bair.  Haxn.
WP.  I  456  f.,  WH.  I  188,  283,  858.
kolQ-  :  klö-  , spinnen'  ?
Gr.  y,Xd)d-cji),  nXcodKü)  ,spinne',  xAw^w  eig.  ,die  Spinnerin',  xkiüOxrjQ,  -fJQog ,Faden,  Spindel';
39*
612
lat.  colus
### leaf 273
j  -üs  oder  -l  , Spinnrocken'.
Gegen  Verbindung  von  colus  mit  k^el-  ,sich  drehend  herumbewegeu' spricht,  daß  der  Rocken  sich  nicht  dreht.
Formell  kann  xAw^w  ein  cZÄ-Präs.  von  einer  schweren  Basis  koh- :  klö^ sein  (*klö-dh-ö  oder  koh-dho) ;  Verwandtschaft  zunächst  mit  K&la^oq  ,Korb' (,*Geflecht')  wäre  denkbar.
WP.  I  464,  WH.  I  250.
U kolsmo-s,  kolsmä  ,Halm,  Rohr*.
Gr.  yidlauogj  v.al&iiri  ,Rohr*  (aus  xoA-  assimiliert?);
lat.  culmus  ,Halm*;  [^;
ahd.  halnij  halam,  anord.  halmrj  ags.  healm  ,Halm';  :/.
apr.  salme  ,StrohS  lett.  salms  , Strohhalm';  "*f
aksl.  slama  {*solmä,  idg.  *kold-mä\   russ.   solöma,   serb.   släma  ,Stroh*;
toch.  A  kulmämts-  , Schilf  (?).
Aus  gr.  KdXa^og  entlehnt  sind  ai.  kaldma-  m.  ,eine  Reisart,  Schreibrohr* und  lat.  calamus  ,Rohr',  woraus  wieder  cjmr.  usw.  calaf  ,Rohr'.
Beziehung  zu  kel-  etwa  ,dünner  Schaft,  Pfeil,  steifer  Halm'  ist  er- wägenswert (S.  552f.),
WP.  I  464,  WH.  I  136,  303  f.,  Trautmann  298.
kol(fi)i-  ,Leim'.  .,1
Gr.  y,6lXä  ,Leim'  (*xdAjia);  'i
mndl.  mnd.  lielen  , kleben'  (*haljan)]
aksl.  klejhj  klejh  ,Leim'  (urslav.  Formen  *k^lej'b,  k^hjh,  k^le,  s.  Berneker 659  f.);  lit.  klejai  ,Leim'  ist  Lw.  aus  dem  Slav. ;  slav.  -^l-  Reduktionsstufe zu  -ol-.
WP.  I  464,  Trautmann  144  f.
koli-  ,junger  Hund,  Tierjunges' :  s.  S.  550  unter  kel-  , rufen'.
kom  Adverb  (Präfix  und  Präp.  oder  Postpos.)   ,so  an  etwas   entlang,   daß Berührung  damit  stattfindet:  neben,  bei^  mit'.  .
Gr.  Y,oiv6g  ,gemeinsam'  aus  *xo^t-td-g  {^-iö-s  ,gehend');
ligur,  FIN  Com-heranea,  ven.  PN  Com-petalis,  hispan.  ON  Com-plütumj Com-pleutica  (ligur.?  veneto-illyr. ?) ;
lat.  cum  ,mit,  bei',  Präp.  und  (nach  Pron.)  Postposition  beim  Abi.  (=  Instr.), als  Präfix  com-^  woraus  con-  und  vor  v-  (wie  im  Kelt.)  und  Vokalen  meist  co- CÖ-;  auch  cöram,  das  nach  palam^  dam  aus  co-öro-  ,vor  dem  Angesicht  befind* lieh'  umgebildet  ist ;  osk.  com,  con  Präp.  ,mit'  beim  Abi.  (=  Instr.),  com-,"* küm-  Präf.  ,mit'  (Ableitung  comono,  Lok.  comenei  ,comitium'  aus  *kom'no-)f umbr.  com  ,mit',  Präp.  (nur  bei  Pronomina  Postpos.)  beim  Abi.  (=  Instr.),  "J
-^^
*
613
stets  Postpos.  in  der  Bed.  ,juxta,  apud,  ad*,  ebenfalls  beim  Abi.  (=  Instr.), präf.  Icum-^  com-  (co-  wieder  vor  v-:  coaertu,  Jcuve
### leaf 274
üu)]  falisk.  cuncajptum jConceptum*,  volsk.  co-uehriu  Abi.  , curia'  (*ko-mrio-,  vgl.  lat.  curia  wohl aus  *co-mria)'j
ital.  Komparativ  auf  -t{e)ro-^  das  Beisammen  von  zweien,  das  Gegen- über bezeichnend,  in  lat.  contra  ,gegenüber,  dagegen,  gegen*  cont7'ö-versia, osk.  contrud  , contra*;
air.  CO  n-  ,mit*,  Präp.  beim  Dat.  (=  Instr.),  Präfix  gall.  com-,  air.  com- (proklit.  con-)j  cymr.  cyf-,  cyn-j  corn.  kev-]  Schwund  des  -m  vor  w-,  z.  B. cymr.   cy-ioir,   abret.  Jceuuir-gar,   gall.    Covlrus  MN,   cymr.   cy-wely   ,Bett*;
davon  verschieden  air.  co  ,zu,  bis*,  Präp.  m.  Akk.  co  a  chele  ,zu  seinem Genossen*  =  cymr.  bw-y  gilydd  ,(von  einem)  zum  andern*,  also  mit  ur- sprüngl.  kV:j  *kom-dho-s  ,verstehend*  ist  vielleicht  die  Grundlage  von  air. cond  ,Sinn,  Verstand*  (=  aksl.  sQ-d^  ,Urteil*) ;
alb.  ke-  ==  lat.  co(my]
für  Heranziehung  auch  des  germ.  Präfixes  ga-  spricht  dessen  Grundbed. ,mit*,  vgl.  z.  B.  got.  ga-juka  ,conjunctus,  Genosse*,  ga-mains  ,com-münis*, ga-qiman  ,con-venire'  und  ähnliche  Übereinstimmungen;  germ.  g-  aus  %- im  unbetonten  Präfix;  der  Nasal  schwand  vor  der  Vereinigung  mit  Verben und  nach  deren  Vorbild  auch  in  etwa  überkommenen  älteren  Nominal- kompositis  wie  gamains  (man  beachte  die  Vortonigkeit  der  Partikel  auch in  letzteren);  unzweideutiges  *kom  steckt  in  afränk.  ham-edii  ,coniürätöres* ;
aksl.  sg-d^  ,Urteil'  s.  oben.
Verwandtes  kmta  ,neben,  entlang,  abwärts^,  mit*  in:
gr.  xaTff,  yiccTa  Präp.  beim  Akk.  ,entlang,  über  —  hin,  durch  —  hin,  an,  bei', beim  Gen.  ,über  —  hin,  entlang,  abwärts*,  beim  Gen.  (==  Abi.)  ,von  etwas her  herab*,  auch  Präfix;
air.  cet-j  vortonig  ceta-  i^ktrita)]  in  cet-huith  ,Sinn*  und  auch  sonst  mit dem  Verbum  Subst.;  acymr.  cant,  mcymr.  can,  gan,  acorn.  cans,  bret.  gant ,mit,  bei,  längs';
hitt.  kat-ta  {a  aus  t/x?),  Postpos.  mit  Dat.  ,unter,  unten  an,  bei,  mit*, mit  Abi.  ,von,  aus  —  herab*;  kat-ta-an  ds.,  dazu  auch(?)  enklit.  -kdn, Pedersen  Hitt.  158  f.
WP.  I  458  ff.,  WH.  I  251  ff.,  857,  Schwyzer  Gr.  Gr.  II  473  ff.,  irrig ZceltPh.  22,  325  ff.
konQzno-,  knämo-  oder  kenQzao-  , Schienbein,  Knochen*.
Gr.  xrrjij^r]  f.  , Schienbein,  Radspeiche*,  y,vr]fj,tg,  -Töog  f.  (äol.  y,väf.iYv  Akk. yivdfÄiösg  Nom.  PL)  ,Be
### leaf 275
inschiene*;
air.  cnäim  ,Bein,  Knochen*  (ob  gr.  kelt.  -nä-  =  idg.  n,  d.  i.  -eW9-,  oder =  idg.  -wä-,  d.  i.  Vollstufe  der  2.  Silbe  sei,  ist  unentschieden) ;
614  f
mit  Vollstufe    der    1.  Silbe   (kon[d]mä)   und   Assim.   von    -nm-  zu   -mm.**' (daraus  z.  T.  -m-) :  .L.
ahd.   hamma  , Hinterschenkel,  Kniekehle^  ags.  hamm  ,Kniekehle',  aisl hgm  f.  , Schenkel  (an  Tieren)'.
Unsicher  ist,  ob  die  Bed.  von  hom.  yf,v7]ixög  , Bergwald,  bewachsener Berghang*  (,*Wade  des  Berges'?)  durch  ndd.  hamm  ,Bergwald'  als  alt erwiesen  wird,  da  letzteres  vielleicht  als  umzäuntes  Waldstück  mit  mnd harn  ,eingefriedetes  Stück  Land',  ndd.  hamme  ,umzäuntes  Feld'  (s.  Äem- ,zusammendrücken')  zu  verbinden  ist.
WP.  I460f.
konk-  ,in  Zweifel  sein,  schwanken,  in  Sorge,  Angst  sein^
Ai.  sdjdkate  ,schwankt,  zweifelt,  ist  besorgt,  fürchtet',  sardkita-  ,besorgt ängstlich  vor',  §a7dkä  »Besorgnis,  Furcht,  Verdacht,  Zweifel' ;
lat.  cünctovy  -an  ,zaudernd,  zögern'  (*concitor  Frequentativ,  vgl.  ai. saTdkita-) ;
anord.  hcetta  ,riskieren'  (*hanhatjan),  hcetta  , Gefahr',  Jiäski  ds.  (*Aan- h{a)skan-).
Über  ahd.  hähan  , hängen'  usw.  s.  S.  566  unter  kenk-  ,schwanken'.
WP.  I  461.
konkbo-  ,Muschel'?
Ai.  SaTdkhd-  m.  ,Muschel,  Schläfe';
gr.  y.6yxog,  xd/x^  ,Muschel,  Hohlmaß';  v,öx^og,  Y,o%Viag  ,Muschel,  Schnecken- haus, Schnecke',  vielleicht  aus  *xo/xA-;
lat.  congius  ,Hohlmaß  für  Flüssigkeiten'  ist  höchstwahrscheinlich  gr.  Lw. ; unsicher  lett.  sence  ,Muschel',  da  zence  die  richtigere  Form  scheint. WP.  I  461  f.,  WH.  I  260,  J.  B.  Hofmann  Gr.  etym.  Wb.  151.
kop{h)elo-s  oder  kap(h)elo-s  ,Karpfenart'.
Ai.  saphara-  m.  ,Cyprinus    sophore'  =  lit.  säpalas   ,C7prinus    dobula'. gr.  TiVftQLvog   , Karpfen',   vielleicht    nach    xsarQivog,    Kogayuvcg,    igv-d^Qivog usw.  umgebildet;  v-  eventuell  volksetymologisch  nach  KvTTQog,  da  *y.07tQlvog an  ytÖTtQog  denken  ließe.
WP.  I  457,  WH.  I  171,  Trautmann  299.
kopso-  ,Amsel'  (:  Srop-  ,Schallwurzel?').
Gr.  KÖyj-ixog  ,Amsel',  y,6aav-cpog  (diss.  aus  *Y.o\p-vq>og)  ds. ; russ.-ksl.  (us
### leaf 276
w.)  kos^  ,AmseF.  —  Meillet  legt  (MSL  18,  171)  unter  An- nahme von  idg.  k-  (das  in  kosi,  wegen  des  folgenden  s  als  k  festgehalten
r
615
sei)  eine  Schallwurzel  kop-  zugrunde :  ksl.  so'pg  ,spiele  die  Flöte*,  abg.  so^phch ^(xblrixYiq^ ,  russ.  sofUh   ,keuclien'    usw.    und   ai.    sdb-d-a-    m.  ,Laut,   Schall, Rede,  Wort*  (zum  -cZ-Suffix  in  Worten  für  Lärm  s.  Brugmann  II*  1,  467), Sdpati  ,verflucht',  -te  ,beteuert,  gelobt*. WP.  I  457,  Trautmann  299.
iorkä  (krokä?),  -Ja  ,Kies,  Kiesel*?
Ai.  sdrkarä  {sdrkara-h)  ,Gries,  Kies,  Geröll,  Sandzucker*; gr.   y.Q6y.ri,    yiQOiidXT]   ,Kieselstein* ;    vielleicht   hat   ein   HoQy.dXa  :  sarkarä erst  nach  x^^xw  ,schlage*  Umstellung  zu"  TCQOxdXrj  erfahren. WP.  I  463.
kormen-  ,Wiesel*,  s.  oben  unter  6.  ker-,
iormno-,  krmno-  ,ätzende,  beißende  Flüssigkeit,  Lauge,  Harn*.
Mhd.  hurmen  , düngen*  (ursprüngl.  wohl  mit  Jauche),  nhd.  harrij  härm, ahd.  karan  ,Harn*;
lit.  Sdrmas  ,Asclienlauge*,  lett.  särms  ,Lauge*,  apr.  (mit  der  Ablautstufe von  mhd.  hurmen)  sirmes  (für  *sirmis)  , Lauge*.
WP.  I  463,  Trautmann  300.
kormo-  ,Qual,  Schmerz,  Schmach*.
Av.  fsardma-  m.  , Scham  (gefühl  vor)*,  mpers.  sarm  ds. ;
aisl.  harmr  ,Betrübnis,  Kummer,  Harm,  Kränkung*,  ags.  hearm  m. jKummer,  Schmerz,  Schade*,  as.  härm  , Schmerz,  Kränkung*,  mnd.  härm , Schmerz*,  ahd.  har{a)m  ,Leid,  Harm,  Schimpf*,  nhd.  Harm,  ags.  hearm, as.  härm  »schmerzlich,  verletzend*;
abg.  sram^  , Scham*.
WP.  I  463,  Trautmann  299.
koro-s,  korio-s  ,Krieg,  Kriegsheer*;  korio-no-s  , Heerführer*.
1.  Ohne  formantisches  -to-,  -la- :  lit.  käras  , Krieg*  und  dehnstufig  apers. kära-  m.  ,Kriegsvolk,  Heer;  Volk*,  npers.  kär-zar  , Schlachtfeld*.
2.  Gr.  ycoigavog  (aus  *KoiQOvog)  ,Heerführer,  König,  Herr*  (Ableitung  von *y(,oTQog  aus  ^xögiog  mit  Formans  -no-',  ebenso  aisl.  herjann  , Heervater* als  Beiname  Odins  von  harja-  ,Heer*  aus;  ytoLgaviw  ,befehlige;  herrsche*, %OLQavla  , Herrschaft*,  vgl.  vom  unerweiterten  *xor(>o-  EN  wie  KoLgöfxaxog (Boisacq  s.  v.) ;
mir.  cuire  m.  , Schar,  Menge*,  gall.  Tri-,  Petru-corii  Völkernamen  (,die drei-,  vierstämmigen*);
got.  harjis,  aisl.  herr,  ags.  here  ,Heer*,  ahd.  as.  herl  ,Heer,  Menge*,  PN altgerm.  Hari-gasti  (Dat.),  vielleicht  Göttername  (Neckel  KZ.  60,  284);
616
lit.  kärias  ,HeerS  häre  ,KriegS  harys  ,KriegerS  lett.  har'^  ,Krieg,  Heer', apr.  kargis
```


## [2026-09-06T21:14:11.505Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '51870,51930p' POK_full.txt\necho \"=== lemma header ===\"\nawk 'NR<=51898 && /Root \\/ lemma:/ {l=NR\": \"$0} END{}' POK_full.txt\ngrep -n \"Root / lemma:\" POK_full.txt | awk -F: '$1<51898' | tail -3\ngrep -n \"Page(s):\" POK_full.txt | awk -F: '$1>51898' | head -3"
}
```


### [2026-09-06T21:14:13.190Z] TOOL RESULT

```
Material: Old Indie srambhate, participle srabdha- {W\Vc\ v'h and other preposition) .) ' trust, 

count on ', nisrmbha- ' appearing surely '; 



Old Irish crabud' devoutness, ascetic' {*Rrdo'"itu-s) m.; cymr. crefydd {x^e^^ creddyf) 
"faith, belief would have attributed eto c/ieo'i/ 'believe'. 

References: WP. I 478, Kuiper Nasalpras. 146. 
Page(s):617 

Root / lemma: Rred- 

See also: see above S. 579 f. under Rered-. 

Page(s):618 

Root / lemma: Rrei- 

Meaning: to appear, show oneself 

Material: Old Indie sn-i. "beauty, splendor, satisfaction, richness, glory, magnificence', 

Avestan s/7"-' beauty'. Old Indie 5/7-/a- 'beautiful, lovely, superb, pretty, splendid', a-snra-^ 

ugly, not good looking ', Avestan 5/7?5- "beautiful', Kompar. Old Indie sreyas-, Avestan 

srayah-, Superl. Old Indie srestha- {srai'stha-), Avestan sraesta-. Old Indie sreman-m. " 

decoration, preference ', Avestan srayan-n. "beauty'. Adj. "beautiful'. Old Indie sr/yase Dat 

n. "beautiful'; 

horn. poet. Kpsiwv "noble, princely, ruler' (supu Kpsiojv, Kpsiouaa) Kpsojv Pind. Aiseh., 
nachhom. EN Kpsouaa (*Kp£[i]-ovT- participle " shining out ' (?), stands perhaps as 
comparative for Kpsiov-). 

References: WP. I 478, Schwyzer Gr. Gr. I 526. 
Page(s):618 



Root / lemma: /(re- Rrei- ^- 

See also: see above S. 574 ff. under Rer-1. 

Page(s):617 



Root / lemma: Rre- 

See also: see above S. 578 under Rer-4. 

Page(s):617 



Root / lemma: Rrus- 
Meaning: shank, leg 
=== lemma header ===
51860:Root / lemma: Rra- 
51882:Root / lemma: Rred- 
51888:Root / lemma: Rrei- 
51909:Page(s):618 
51917:Page(s):617 
51925:Page(s):617
```


## [2026-09-06T21:14:35.549Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT srira/sraesta ===\"\ngrep -n -i \"srira\\|sraesta\\|srae5ta\\|srlra\\|sraesta-\\|srayah\\|srayan\" BRT.txt | head -30"
}
```


### [2026-09-06T21:14:35.608Z] TOOL RESULT

```
=== BRT srira/sraesta ===
2872:aoxta  zaraiiuitrö:  mmö  /taomifi  "drauf, sprach  Z.:  'Verehrung  dem  .ff.'"  Y.(j.i6, 3,  /£>.  17;  -1.2,  Az.  I,  Yl  /.  5,  21,  j.  2, 5.83,  91,  95,  i<.io,  77.54.  V.  2.  40,  42,' 3.  26,  Vyt  24,  54,  Vd.  12,  20;  —  ,7a/! Aim  aoxta  p»r>sö  yö  narl  asaonö  un'a:\ as.'a  ..  "und  es  sagte,  ihn  fragend  ..: 'Und  wer  ..'"  H.  2. 10;  —  äal  aoxta  akurö  \ ..  yimii:  yima  srira  "und  es  sprach  Ah.^ zu  y.:  'y.  . .'"  V.2.22; — yö  naire  aoxte (3SP0.-  M  ml  aä  (sd.)  F.^d;  N.;,^,! tft;  —  aojUa  (jSPr.)"  ../raiaoitrazibya  ..: aiayata  . .  Vyt, //;  —  at  Aöi  aoß  (iSPr.) zara'httströ  paourvTm  "Drauf  sagte  ich zu  ihm  ersthch:  ^Zar.  (bin  ich)'"  Y.  43. 8.  a  )    mit    uili  (sd.):    mi^rim  .  .  yö
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
5386:•  j.  auruäa-  Adj.  'weiss',  1)  von  Tieren: pttsüm  .  .  'hm  vH  vohu.gaon^m  vä  "ein weisses  oder  schwarzes  Schaf  Yt.ÄsS; —  aspa/ie  ktkrpa  'iahe .  .  aspahe  kihrpa sämahe  "in  Gestalt  eines  weissen  Rosses . .  in  Gestalt  eines  schwarzen  Rosses"  Vt. Ä  18-21";  —  aurvants  'la  raoxsna  fnl- ä)r»sra  Y. 57, 37;  YL  JO.  136.  z)  sonst: srlra  i-a  auhtn  blzava  'h  (ND.)  Yt.5.7;
5754:•  j.  asö.söidra-  n.,  Plur.  'Stätten  und Wohnplätze'(?)":  kaia  xi..  yzarqm  atwi- yzanm  srirasca  'rasca'>  gaoyaoiliS^a  ilta- cin/ls  (sd.)  YtÄ42.
5880:•  j.  asp5.stao/ah-  Adj.  (fem.  °ye/tJ-) 'starker,  umfangreicher  als  ein  Pferd, Pferdeleib"':  xä  'yehls  apam  \'t.8.$,A2; —  srira  vü  ar»)im  b.lzava  aurusa  "ythTs'^
6091:—  kadä  vatds  yezT  <ahyä  xlayaüa  (sd.) masda  °sa  (Vok.)  ".  .  o  M.  und  Asa" Y.4<?,g;  i^.  18, 50. 9;  —  atvs  staoiä  aojäi (sd.)  mazda..  'sa  Y.50,11;  2,  6,8,  2Ä  i, 34.T,  —  hvö  zi  "Sil  .  .  ahamMs  (sd.) urväkS  masds  Y.44.2;  18;  —  ara' (sd.) sf  xsmä  mazda  °s3  ahurä^^''  hyal  .  . yoorjaaäa  (sd.)  Y.  50.  5;  —  in  GHapt: masda  aAura  .  .  fava/ä  haxamS  (sd.) -sahyala  \.4a.ii.;  41.6; —  *aAura.mazda °ia  (Vok.)  srira  Y.j'5.3;  —  masdai  ahurai 'säila  vahistai  Y.  JJ.  j ;  4/.  i .  «)  in dualiscjiei  Verbindung  mit  ahura-:  yöi  vS syaoianäissärMil{%d.)aAurff*asa*Aisvä^''''> axhai/ ..  Y.51.3  (s.c).  b)  neben  VoAu- ManaA:  yäcS  vehü  uxoa  fral%  (sd.)  ma- nauAä  yOcs  °sa  (Instr.)  aahlus  Y.  44-  8; '31  —  yf  «""'^  "^  (Instr.)  tmüi  hvö *mainyJus  a  vaMstat  kaya{iA.)..  Y.S3.6; 4g,$;  —  %wavas  . ,  masda  hadtmsi  (sd.) -ia  vohulä  yyas  manavkä  Y.  44-  9 ;  2Ä  5 ;
7655:•  j,  »radva-fana-  Adj,,  nur  fem,  'ni-  'deren Brüste  in  die  Höhe  stehen,  mit  straffen Brüsten':   kainTiiö  hhrpa  sriraya  .  .  'r/yä
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
8705:—  'saiihqm  para  frSritSii  FrW.  /0,4i ;  — ytzi  xsapsAva  mpr^ncaiie  (sd.)  'lakva bisazyat  V.  l'7.3J  —  uü'  (LS.).  A)  als weibliche  Gottheit  gedacht:  'sqm  (AS.) sriram  yazamaide  'säuAfm  . .  xsSi'inJm ravaLaspqm  .  ,  "säPikem  .  .  nvim  ranjat.- aspqm . .  avqm  'sqm . .  G.  5. 5.  a)  Name der  fünften  und  letzten  der  (priester- lichen) Tages  abteilungen*';  vupim  paiti "sauham  ä  kB  vaxsat  "immer  in  der Morgenfrühe  bis  Sonnenaufgang"  V.  /y. I.  3)  mit  süra-  Adj.  Name  des dritten  Abschnitts  der  Nacht**':  hö tiurr/ö  (j'S  parö.dars)  väHm  baraili  upa 'iaukim  yqm  särqm  V,  iS.  15;  —  'sqm särqm  V.2j\}.
10303:—  upäai  hi  (näml.  der  Hündin)  °iBm baraym  .  .  V.  jj.43;  —  ma  °tSm  nipail- yavuka  (sd.)  Yt/7,57;  — yats  {sA.)  °lus .  .  x^ar^^a  .  .  V.5.55;  —  star»tasca  -tui anyfma  ..  avar?tä  YLJ7.  7;  —  agsqm 'tava  (NP.)  kistmte  husiania  .  .  zaran- yapaxsta.pmSnkS  'S.t.i'j.f);  —  ya'ia  nä fryS  .  .  slanta  °tul  (AP.)  sayamanS  (sd.) V.^.25;  —  'tu  (AS.)  ^x^ainUtarftu  tnai bariziia  . .  nisirinuyät  V.  /4. 1 4 ;  Yt  ?.  i  o  2 ; — aisam  vantsnks  °A(/(  AP.)  paiti  *äak»ute (sd.)  ysi  srira   banzis.havanis  Yt, /7,  10;
10698:•  j,  xSaeta-  Adj.,  fem.  xsöiSni-"  'licht, strahlend,    glänzend,    herrlich';    i)    vom Licht  usw.:    °ta    rae^A    Ytj.  1;    —    ." *bamya   -«/{als    GS.)    Yt.70. 143;'* usänhfm  .  .  '^nfm  G.  5.  5;  —   'ünyJl usayll  YtÄ35.  2)   von  Göttern  und Menschen:    bfrizanlim    akur^m apqnt    napätptn  Y.  2.  5 ;    —    asis  .  .  srlra 0«(  Ytij.  107;    —    asim    ..    ''inim  Y. 2.14,  Yt/J.  i;  —  arptfplm  ..  ''hnim  YL 5.  1 5 ;  —  am3sanqm    spmtanqm    'tanqm Y.2tf.3;    —    nar/ A?hrpa  .  .'"ta/ie  Yi.8. 13;    —    kainlnS    kikrpa  ..  ''ä-nyä    H.  2. 9;    —  frazantsis   .  .  '^nyä  (GS.)  Yt  ij. 134.          a)   bes.  von    Yima:  yS  yimd  'tö
10762:•  j.  'xSa*r5.k8r»ta-  Adj.  'fiir  den,  die Herrscher  erbaut,  fürstlich';  *antarp.anhm nmänake  srirahe  'tahe  Yt  i-].  60.
11356:paitis  , .  zbayeiti  . .  yim  *driyBsat  . .  sba- yäti  Yt  10.  84;  —  %wqm  yazSnte  .  .  dai- AAu.paiays  . .  '^wqm  naraHt  ySi  taxma Jai'jyhnte  Yt  5.  85  f;  —  haraiti  bars  .  . kä  Aama  päirisSite  frSpayä  (sd.)  . ,  M3r?- fiaaS  gairis  . .  AämS  hasHt  päirisaile  .  . "das  jy.-Gebirg  . ,  umlagert  . . ;  . .  das  Z.- Gebii^,  auch  das  umlagert  . ."  Yt  ig.  i; y- 69;  —  Vlspe  ,.  tirKtnti  pfnmne  {%äj) avaia  mävayaiit.-tprisantu  Yt  14.38;  — *daSinqtn..Äaoyqm  h! paiayqm ..  dumtnüit Af  upa.%w^r^saym'V.i3.ai.;^vlsfe  haoma . . yaicit . .*upa  *dintäku{sA.)  V./0.17J  — Aazaignrn  maoirinqm  d3nS.karSanqm  ava.- jartyat  duye  hazanre  anyalsamat'-'^  V.  18. 73i  73i  —  ^y^  *gr}Amö  ä.ASi^Si  (sd.) «r  ksvayas^l  xratül  «r  dadat  ".  .  Gr., de^leichen  (sva,  und)  die  K.  richten  .." Y.  J2.  14; —  aSavatca  alsasät  ästärayeite (sd.)  N.72; — nava..anaiwyasHi  kunämi; hinti  (Sp.  370  o.)  .  .  mävayacit  ca^warS arsäna  V.lS.^j;  —  ksnti  anyäsät'^  (Sp. 137  in.)  asäs^a  /äi^ris^a  srIras/a..Y.l.2o; —  aam^i  akyS  . .  %wam  tUSökj  , .  vai- <hm  (sd.)  Y.  ig.  10;  —  mainya  .  .  yS  ä narSm(,sd.)ät.,Aäi>0  Y.^i.y  i — in  auffälliger Stellung:  mUca  paslaSa  mazdayasna  vXmä- oasHt*^  vTmSoayanta  "nicht  sollen  sie  dann auch  bei  M.  als  Ärzte  praktiziren"  V.  7, 38;  38,  40;  —  hinter  ula^^:  iavaj  aiwi.- vanyä  .  .  ta^ryävanttm  , .  ptiatamca  .  . Uta  anyäscit'^  ..  kyaon&tgkB  Wtig.ST, 89;  —  hasannm  aspä  uta  äsitqmHt /rastUntim  Yt  18.  5 ».  a)  Bei  hypotak- tischer Saufiigung  steht  das  mit  /■■  hervor- gehobene Wort  jeweils  an  zweiter  Stelle*', U2W.  a)  des  Hauptsatzes;  b)  im  Aw.: Sfit  MOra^uslrS  da^äU  sanm  vyämrvUä .  .  flS-a  *aspm^  .  .  vlinruyg  Y.  12.  6\  — ya'ha    . .    kvarsxiatä^m    .  .  fraca    Siti  .  .
12424:oAurischta  Religion :  kahmät  paoiryS  mal-  \ yänqm  , ,  frada^ayS  'nqm  ,  .1  . .  yimäi .  .  fradaisalm  °nqm  .  .  äai  hi  mraom  . . vUanha  ml  minlff  b^ntala  (sd)  "nayäi (als  Gen.)  äat  . .  pailyaoxta  yimS  .  .  nSit dato  ahmt  . ,  tnirstl!  b3r?tala  'nayäi  V. 2.1  ff.;  Ytn.  14;  —  vXltäspaht.  .yS  batuUa upastaca  vTsata  .  .  •nayä  Yt  13.  99;  — ya%a  axsm  Asüyene .  .  zara%uänm  anu- matSe  'nayäi  anuxtie  'nay3i  anu.värltSe •nayäi  Yt.  j,  18;  Y.t?.  7;  —  hutaosqm  .  . yä  rrn  °nam . .  zraiia  (sd.)  dät  apica  aotaf Yt  ().26;'Vyt.  Jo(?);  —  ks  .  .  'nam  .  . vJbarat  aitaisva  vanfsva  ySyimö  ktnrtaoi^ .  .  vTs  iarsipia  V.  2. 42 ;  —  satö  .  .  zara- huiirS  .  .  ita  apam  vTjasaiH  .  .  °na  .  . vlspais  avi  karsvqn  Yt  jj.  94; —  mi^nm . .  yahmi  vyane  (sd.)  °nayäi  (als  Gen.) srirayai  p}r>^u.fräkaysi  . .  Yt  10.  64;  — sraoi^m  .  .  yB  damsJisS  *°nayä  Y. 57.23;
12441:asahya  axäyai  (sd.)  ggnedim  Y.  37, 17;  — aiäunqm  . .  uruns  .  .  kudüJiatanqmAt  .  . yailqm  vahehl^  'na  vanainti  va  vSnghm va  vaonarS  va  H.  3g.  z;  —  karapanS kavayasca  .  .  ySng  ^S  urva  ::^a!^a  xrao- dat  (sd.)  'na  Y.46.11;  —  Ö  dngvats *tnandaHg  *9r?tael  (sd.)  haihim  yehya urvü  xraodaiti , .  Y.  ji,  13;  —  tsm  *vä ahsm  dtTgvantS  .  .  'na  nailal  (sd.)  Y.^y/. so;  zT.  verwendet  V.f.  fia;  s.  a;  —  ySi .  .  aiäm>m  vandtn  (sd.)  . .  töi  daoiStig dqn  yS  drsgvats  °na  ",.  die  —  in  AnDaiva Haus  fUr  das  Ich  des  ^rv^enossen!"  Y. 4^.  4*>.  a)  im  jAiv.:  alaonqm ..  ahümla 'nam/ai*  iaooasäi  urvänsmca  fravaiSmia yagamaide  Y.  a6.  4;  —  asni  iyazamaide\ manä  . .  °nä  [yazamaidi]  saoryantqm  yaaa- vtaide  Yt  13.  7^;  —  aisS  zT  växs . .  a  va^S ahunB  vaityS . .  uruna^a  'tiaca  (IS.)  span- vanti  (sd.)  H.  J.  4;  —  'nqm  .  .  yaoldai- är/a  dha  zl  aifihä  asH  yaosdaitis  kahmai- Ht  ..  havaya  tnsvS  'naya  yl  hvqm  'nqm yaozdaite  humataisla  ..  V.  10.  19*';  —  um vä  ahOm  drvaniö  *^a  *'na  msirtnttyJJ [a/isiäi  a/fuhe]  V.  5. 6a;  —  aiiihä  dim vütaya  fr-Jmita  (sd.)  salayeiti  ya  hava 'naT>  kaininS  k>hrpa  srlrayh  .  .  aat  Alm aoxta  ..yS  nars  asaonü  urva  alca  Karditis ahi  ..?  äat  hl paiH.aoxta  ya  hava  'na  .. az?m  ba  U  ahmt  .  .  yä  hava  'na  *:^ai- paihejanvö  {sd.Y'  H.2.9— 11; — arahvam 'nqm  V.^.ai  PüZ.s),  io.  19  PüZ.
13262:I  des  Inhalts  (?) :  srira  doonifi  dacjnäna  dü-
13739:•  j.  dürätsüka-  Adj.  'von  fem  — ,  fern- hin leuchtend':  srlra  daaiiiti  (Sp.  725  o.) dacmäna  'ka  (APn.)  Vt/o.  107.
13985:V.  bring  ein  Tor  an,  ein  Uchtes,  innen eigenlichtiges"  V.s.30;  38;  —  b^a  iha kistahe  aiiythe  °r>  (LS.)  srayanS  ^anrUls (sd.)  pinsimnaisuia  "wahrlich,  du  sollst künftig  stehen  an  eines  anderen  Tür  dich lehnend  .."  V.J.  29;  —  II  'rayamaiyiXSi.Y> basit^  adäriy  haruv^Hm  kärO^  avaina* "an  meinem  Tor"  wurde  er  gefesselt  in Verwahr  gebracht,  alles  Volk  konnte  ihn sehen"  Bh.  2. 13,  14.  a)  'Pass'  im  Ge- birge*: upa  °r>m  xsa'hrB.sukjm  apaiiS.- t>m»m  ka^haya  (sd.)  YtJ.  54.
14850:udapatats  pärsaiy  ". .  der  lehnte  sich  als zweiter  in  Persien  gegen  mich  auf"  Bh-J.  5. mit  US  i)  'hervorgehen,  nasci',  von «futschen  Tieren:  *us  *täeil  vshrka  patmti V.y.43;42.  2)  iniÄiÄ^scher  Art  "heraus- gehen aus  -'  {kaca  mit  Abi.  oder  Instr.): äa^  uspatai  fraarase  srayanhat  haca  Yt. ^9-  57-  3)  I^aus.  'herausgehen  machen aus  — ':  uspataymi  attrsm  mainyäm  »rrjata haca  dtiiafiha  Yt  ig.  44.
15059:•  j.  paiti-srira-  m.  EN.  eines  Gläubigen":  '"^J^Y-^P- 43.;^ usmänaraheca    pailataahs    'rahe    Yt.  y.       *    °"  ""  *"""
16944:•  j.  barö.srayan-  Adj.  'Schönheit  inne habend',  mit  taira-  m.  'Bergspitze,  Gipfel', Name  eines  Bei^  oder  Gcbirgstodts'*: ahmat  haia  garayö  fraox^an  .  .  tairasca Van^'CNSm.)  '>  Yt  jg.  6.
19190:p.  mya%'Srayani :  s.  unter  stay-.
20116:•  j,  'masan-  n.  'Grösse,  Eedeutendheit': "sanaca  (IS.)  vatvhanaca  srayanaca  (sd.) V.J.  22,  Yt/p.  sS,  K.i.\z,  H.J.6,  2.  II, *P.  42.  a)  Plur. 'Glosstaten':  li^ra  vö buyäryS  'sänh  (NP.)''  H%ra  vS  zavanif.- sav^(s±)  Ny.j.ii.
20118:•  j.  'masan-  Adj.  'gross,  bedeutend':^ffi>,*? .  ,  'sä/ias^ä  (GS.)  vauhänasiä  srayanascJ (sd.)  carpktnmahi  Y.  3Ä4.
20830:—  N.-APn,:  vjspi..yä  h?nti  haptöMars- vShva  Yt.  6.  3;  —  dama  .  .  ya  k?nti  sp?n- tahe  mainySus  Yt,  6.  a ;  —  draomJbyS  .  , y  ä  aism3  . .  drävayäi  Y.  57.  a  5 ;  —  ASm, ; ../anal  azim  srvar»m yim  (s.II)  asps^anm .  .  yim  upairi  *vis  ''raooai  yim  upairi ktnsäsp»  .  .  pitam  pacata  Y,  5. 1 1 ;  Yt /4.  7,  9,  70.66;  —  va^am yim  (&,'n.)  vär?- hrayrum  yim  öarat  .  .  %raltaonl!  yim^ barat  ..  Ytig-^it;  8.6,  77.15,  '4-39*. 48,  ig.  35,  81;  —  mi'^rfm  ..yim  yazsnte daiAhupatayB  YL  /0.8;  11,47,  66,  68,83  f.^ 88,  89,  103,  109,  123,  8.  5,  36,  41,  44', 48,  7_5. 147,  Aog.  77;  —  spänam  ..yim (s.  II)  vavkäpar^m  yim  ..  duzak^m  nama aojaite  V.13.  2;  6,  18. 15;  —  ASf.:  avqm vanqm  yqm(s.11)  salnahe  yS  hiStaüe  mai- äüw  srayanhö  ..yqm  upairi  urvaranqm  .. taoxma  nt^ayal  yx.  12.  17;  —  arltis  ..yqm *ai9hyeiti  avi.mi%riS  Yt/o.  20;  21,  5.  6;
20897:srira  ustavaitica  ya  *süra  Yt. /p.  67;  — gäui ya  ca?9rat3haxl ya  .  .  frasarsta  Yt. jo.  38;  —  alis  (Stverz.)  vavuAi  yä  hr>- zaiti  Yt/7.  25  usw.;  V, //,  9';  —  hutaosa yä  pourubrä%ra  YLJ5. 35;  —  aß  ya awzdänva  nqma  Yt  rp.  6  2 .  o)  aisa  druxs yä  iMSUs  Y.j.i  usw.;  —  a^sa  ya  kaine V.  J5.9— 14*;  —  *avau  pairika  ya  dui- yäirya  Yt*.  54;  —  ha  druxf  ya  nasus V.^t.is  usw.;  5.21, /Ä  31.  c)N.-ASn.; zrayS  yat  kqsaSm  Yt. /p.  66;  —  »o»  asti .  .  ahm  yat  vahtstim  Yt.  ;.  25 ;  —  yS  .  . staoia  as»m  yat  vahisttm  YL  J7. 18;  Y.lQ. %y. 18.16;  —  'kvan  yat  amshm  Y\.  (j. 4; ig.  65;  —  haicS  ksrmaoiti yat  avästnm  V. i3.%\;  —  aoinmän3Myim  (als  APn.)  «"iM- paihitn  Yt5.63;  62;  —  äyapDm  ya^  ahu- 39*
21828:—  -malte  x/dire  .  .  nSil  saurva  änha nSii  rnfry%yu/  Y.  g.  5;  —  'mJi  srirai  .  . paoiryB  masyänqm  aptrise  aam  yS  ahurl V.  2.  2;  9,  23,  75.39;  —  äat  'ms  varsm (sd.)  kirmaot  V.  2. 33';  39;  —  aisqm atnanhqm  vlvanhusS  trOvl  'masct{  "zu diesen  Frevlem  gehört,  wie  bekannt,  auch y.,  der  Sohn  des   Vtv."  Y.32.&.
22475:masaaa/a   'hanaia  (IS.)    srayanaca   (sd.)
22479:•  j.  'vaBhan-  Adj.  gut':  yeähE  vJ  masä- nas/ä  'Aätias^ä  (GS.)  srayanas{&A.)iä  iar>- k^nmahl  H.$8.^.
22510:•  j.  vaDhänam  Absol.  'beimAnhaben,  Sich- ' kleiden  in— '(Akk.):  ar3dvtm..yä  hiitaite\ fravai^iimna  (Sp.  1 3 1 7  u.) . .  kainira  JbÄrpa srlrayä .  .frazuitm  a^tm  V  pouru.paxStsm ". .  in  einen  kostbaren  Mantel  gekleidet . ." Yt5. 126.
```


## [2026-09-06T21:14:36.756Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD kust ===\"\ngrep -n \"^kust\\|^kustīg\\|^kōst\\|kust \" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD axram ===\"\ngrep -n -i \"xrām\\|xram\\|axrām\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T21:14:36.827Z] TOOL RESULT

```
=== PHD kust ===
PHD.txt:430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
PHD.txt:1331:kustagbed,
PHD.txt:5024:1 ?kust kūstan kustag kustagbed kof
PHD_mackenzie.txt:3363:lkust [kwst ] side, direction; district.
PHD_mackenzie.txt:3365:2kust [/lwst l I Ar. qust] costus.
PHD_mackenzie.txt:3366:kustag [kwstk l I M kwstg] = lkust.
PHD_mackenzie.txt:3368:kustig [kwstyk I N -i] sacred girdle.
PHD_mackenzie.txt:3370:kustan, kus- [NKSWN-tn' < A .y nks; kws-tn' I M kwft, kwf·, N ._]
PHD_mackenzie.txt:9572:kustan                                          kor                              '\\~
=== PHD axram ===
PHD.txt:161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
PHD.txt:3813:step up abar Áxramidan.
PHD.txt:3842:stride (v.) āxrāmīdan.
PHD.txt:3855:strut āxrāmīdan.
PHD_mackenzie.txt:678:  - Axramidan: step up.
PHD_mackenzie.txt:1342:AxrAmidan, Axram- [)hl'm-ytn I M )xr)m-, N xiram-idan] stride, strut.
PHD_mackenzie.txt:7668:spell afson, marig, nerang, sraw,      step up abar dxramidan.
PHD_mackenzie.txt:12333:axistan                 \\~         axramidan                ,\~
```


## [2026-09-06T21:14:48.422Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT headwords srira/sraesta/srayah/sri ===\"\ngrep -n \"^•.*sr[il]ra-\\|^•.*srae5ta\\|^•.*sraeSta\\|^•.*sraesta\\|^•.*srayah\\|^•.*srayan-\\|^•.*sri-\\|^•.*srT-\\|^•.*srl-\" BRT.txt | head -30\necho \"=== BRT xram ===\"\ngrep -n \"^•.*xram\\|xram-\\|'xram\" BRT.txt | head -20"
}
```


### [2026-09-06T21:14:48.534Z] TOOL RESULT

```
=== BRT headwords srira/sraesta/srayah/sri ===
11489:•  j.  fiü  Adv.  'wie,  in  welchem  Mass':  ca  T-z^  —  'i-antim  </my;T(Akk.dcrBMiehung) asti  mas\S..ait3m  dätiin  . .  upairi  anyii^\sri-änim  ..  V.ö'.i;  7.45;  —  'vat  drsjo sravaii .  .  V.5.22.  ■upa.mqnaym    V.5.53;  53.         A)    Neutr,
15059:•  j.  paiti-srira-  m.  EN.  eines  Gläubigen":  '"^J^Y-^P- 43.;^ usmänaraheca    pailataahs    'rahe    Yt.  y.       *    °"  ""  *"""
16944:•  j.  barö.srayan-  Adj.  'Schönheit  inne habend',  mit  taira-  m.  'Bergspitze,  Gipfel', Name  eines  Bei^  oder  Gcbirgstodts'*: ahmat  haia  garayö  fraox^an  .  .  tairasca Van^'CNSm.)  '>  Yt  jg.  6.
23805:•  '].  vouru.kaäa-'>  Adj.  'mit  weit(ausge- dehncjen  Buchten',  nur  mit  srayah-  n. Name  eines  grossen  Sees,  der  in  der  Vor- stellung mit  dem  Weltozean  zusammen- floss**;  ^'däfl  zraye  'hm  upairi  anyä  äpd "wie  das  Zr.V.  die  übrigen  Gewässer  Über- 1 (trifft)"  V.5.  23;  — ya^a  zrayJ  -um  apB asti  hanjaymarum  "wie  das  ZrV.  der Sammelort   des  Wassers  ist"  V,  2/.  4;  —
27205:•  j.,  g.srae5ta-Adj.(fem.'/J-)'derschönste'; x)  fürs  Gesicht:  yim  as}m  vTspake  anASus . .  'tsm  dääar?sa  Y.p.  i;  —  yqm  . .  cäräi- tinqm  kikrpa  °tqm  dädarssa  H.  2. 10;  — /^»(NDf.) hm  h'hrpa  'ta  (ISf.) *?<w5/;ff  (sd.) VtJ.  54;  —  iihrpa  avavalS  *sraya  (sd.) yaä^a  damqn  •/Jj/H.a.g;  Yt/0.143;  — 'tarn  a/  tut  kihrpSm  k»hrpqm  avaidaya- mahl  Y.36.  6;  —  yaj  asti  batori/  'ta  Yt 5.129.  3)  fiirs  Gehör:  ye^Ae  aum frSyS  (sd.)  . .  °t»m  susruye  väHm  Yt  //,
27305:•  j.  sray-,  p.  ^'ay-  V,  'lehnen'.  Fraes. I  sray- :  srl-,  z  sraya-,  7  sr3ray-^\  %''äray''> IQ  srinav;  siriaav-'*:srinu;  sirinv-'^;  Perf. I  s-tsray-{i)i\  —  PPfP.  srHa-,
27321:•  j,'srayan-  n.  'Schönheit?:  Ä  asti  masyS vanhs  srays  (sd.)  aOtm  dit)m  . .  upairi anyaii  sraväil  masana/a  vai^Aana/a  °ya- ««(IS.)/«  V.5.23;  —  Ä/Ä  Sic?«  /aiana ava  »lasaiiaca  vanhanaca  °yanaca .  .ya'ha yat  ml  st^ayehi  "Jeder  hat  dich  gern  ge- habt wegen  jener  (deiner)  Schöne  imd  . ., so  wie  du  mir  erscheinst"  H.  2. 1 1 ;  —  ka aiva    als.itüitis    yä    dasa    anyastam    .  .
27334:•  j.  srayah-  Adj.  'der  schönere':  cä  aUi masyS  vanhs  'yS  aSstn  dätim  yim  vjdsyüm .  .  iipairi  anyäis  sraväÜ  "um  wie  viel ; grösser,  besser,  schöner  ist  dies  Gesetz  . .  1 als  die  andern  Lehren"  V.5.  22;  —  imat\ vaahs  imat  'yS  yj^a  tum  .  .  valaahe  V.  | 5.  a  I ;  —  yalca  ahmst  asti  mazyö  .  . '. vatfhS  . .  'yd  . .  parS.ar?jaslar3m    tat  .  .
=== BRT xram ===
10588:Ableil.  ^  Zum  V.  xram-.  —  Pü.  (ra  V.): *xrPsa(UU,  (»u  F.):  xrßsoi,  erl.:  öh  bavH  ka viif;  hal  fas  tuiirad.  —  ■)  Ein  strafrechtliches Delikt,  wie  aus  F.  hervorgehl;  s.  auch  A.  J. 13.  —  ")  Hds.  xisyö.  —  i)  Haplol.  für  'yqya.
```


## [2026-09-06T21:14:49.197Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG xram ===\"\ngrep -n -i \"xram\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T21:14:49.249Z] TOOL RESULT

```
=== CHEUNG xram ===
488:= Ir. *xramH / *gam! / *dram ‘to go, run, walk’. In several cases this may be 
20506:also be interpreted differently: /axramed/ ‘he strides’, s.v. *xrämH. > DMMPP: 34b 
28680:arisen from *xramH. 
29015:*xramH ‘to tread, stride, go’ 
29021:Pres.: IND. 3sg. ВМР ’hl’mydyt /axraméd/ (MX ii,145) 
34850:*hl’m- /axram-/, 449 
56743:*xramH, *zuar 
58072:*xramH 
58239:*sparH, *xramH
```


## [2026-09-06T21:14:54.302Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29010,29070p' CHEUNG.txt\necho \"=== ctx 28660-28690 ===\"\nsed -n '28660,28690p' CHEUNG.txt"
}
```


### [2026-09-06T21:14:54.361Z] TOOL RESULT

```
«PIE? > LIV: — | Pok.: 571 
REFERENCES: Lambton 1938: 74b; Nyberg П: 219b; DKS: 93a; Werba 1997: 172; Lecoq 2002: 608b, 
630b 


*xramH ‘to tread, stride, go’ 

*MIDDLE PERSIAN: (+ *4-) BMP ’hl’m- /axräm-/ ‘to stride to’. Ф The MMP form, 
*xr’m- cited in Nyberg IL, l.c., MacKenzie, Pahlavi: 14, et al., is not mentioned in 
DMMPP. 

Pres.: IND. 3sg. ВМР ’hl’mydyt /axraméd/ (MX ii,145) 

*SOGDIAN: BSogd. xr’m ‘to come’ 

Pres.: IMPV. 2sg. BSogd. xr’m 

*NWIR: NP xiramidan ‘to stride’ 

*NEIR: Wa. Car(a)m-/carn- ‘to go in, enter’ 

*SANSKRIT: kram ‘to stride, go’ (RVH 

9 The IE origin of the common IIr. root *kramH- cannot be ascertained, lacking 
convincing IE cognate forms. 


«PIE? = LIV: 369 f. | Pok.: — 
REFERENCES: Horn 1893: 104; Nyberg П: 39b; DKS: 308b; Werba 1997: 278; Steblin-Kamenskij 1999: 
136 


*xr3š ‘to scratch’ 


*SOGDIAN: MSogd. хгу$ (caus.) ‘to irritate’ 
Partic.: pres. BSogd. yr’nsn’y ‘irritable, annoyed’ (SCE 407) 


*CHORESMIAN: (+ *upa-) bxr’h- ‘to be abraded’ = Samadi: 31 

*NEIR: Pash. garg- ‘to scratch, scrape’ (Cheung 2004: 129) 

emisc: NP xirasidan/xiras- ‘to scratch (a wound)’ 

The forms may be expressive, similar to Engl. scratch, NHG kratzen, etc. 
“PIE LIV: — | Pok.: 


450 *xsaH 


*xsaH ‘to explore, research’ 

*AVESTAN: xsä- ‘to explore, research’ = Liste: 16f. 

Aor. them.: INJ. Zeg OAv. axso (Y 46.2), SUBJ. med. 1sg. OAv. xsai (Y 28.4); Perf.: IND. med. 3sg. 
YAv. caxse (Y 65.9) 


*KHOTANESE: (+ *pati-) pacas- ‘to confess’ = SGS: 63 
=== ctx 28660-28690 ===
IND. 3sg. intr. SSogd. xrt ‘he left? (Nov2 R.12), 2pl. tr. CSogd. "xyrd'rtt (C2 68V.25); Partic.: pres. 


444 *xard 


BSogd. ’’x’yrn’k (Dhy. 100, Dhy. 246), BSogd. ’’x’yrn’y (Dhy. 288, Dhy. 297, Dhy. 311), BSogd. 
"erg wv (Dhy. 245); Inf.: BSogd. cnn ’’x’yr (Pl 24V.882) 

*CHORESMIAN: x’r- ‘to pass, go past’, x’ry- (caus.) ‘to let (it) go past, pass’ 
= Samadi: 231 

*NWIR: Kurd. her- ‘to go’ 

*NEIR: Oss. I. хага, D. xærdæ ‘(upward) slope’ (+ *ni-) ? Sh. nixar0-/nixuxt ‘to fall 
into ruins, sink’, nixár0-/nixáxt (caus.) ‘to destroy’ (why -0- ?) 

*MISC: Par. har-/hari ‘to be lost’ 

© This root appears to be exclusively Iranian, possibly abstracted or secondarily 
arisen from *xramH. 


“PIE LIV: —| Pok.: 
*REFERENCES: JIFL I: 260a; EVS: 51b; Asatrian — Livshits: 94; Abaev, Slovar’ IV: 178 f. 


*xard ‘to defecate’ 

*KHOTANESE: samkhal- ‘to be tainted, smeared; to taint, smear’. % The unusual 
preverb sam- is perhaps a Skt. contamination/loan (SGS: 242) or a (sandhi ?) variant
```


## [2026-09-06T21:15:09.804Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10570,10592p' BRT.txt\necho \"=== grep xram- headword ===\"\ngrep -n \"xram\" BRT.txt | head -20"
}
```


### [2026-09-06T21:15:09.868Z] TOOL RESULT

```
•  j.  xnad^aiti-  f.  EN.  einer  Pairika,  die  | K^rjsäspa  verRihite";  pairikqm  yam  *°/;''  | yH  upaahacat  k.>ns3spjttt  V. /.9j — janäi^ pairikam  yam  'ti  V.  ig.  5.
Et,?*VII.  nichtiran.  Wort;  s,No.2,3.  —  Pü.: f-irli  tSmatlh  an  i  Hzdfs  pnyaslaklh.  —  1)  Sie  ' [jilt  als  rf(i«isches  faityäta  von  Vait/r^ta  \ (Kabulislan);  s.  dazu  DsT.  ZA.  2.  10.  —  »)  NA.  , '/e;  s.  aber  V.  tg.  5  No.  4.  Das  Wort  wird nicht  Sektirt.  I
•  g.  (,  j.)  xraod-  V,  '(sich)  ängstigen', Praes.   i  xraed-,
i)  'ängstigen':  karapanö  kavayascä  .  . ySiig  :^3  umä  £'a?:ä  xraodat  (3SKA.) äami  ". .  die  ihre  eigene  Seele  und  ihr eigenes  Ich  ängstigen  wird"  Y.  46. 11;  — s.  xraodat.',  2)  'sich  ängstigen,  bangen
vor    — '    (Abi.):    dr?gvalS  .  .  yehyä    urvä xraodaitl  (3SKA.)  anvats  p?r»tii  äka  (sd.) ". .  des  Seele  bangen  wird  vor . ,"  Y.  5/.  1 3. Pu. :  xröiiiii  ('Geschrei')  dilan.
•  j.  xraodaturvan-''  Adj.  'den  seine  Seele ängstigt'  sva.  'des  Seele  sich  ängstigt'; isanJtaitya  ml  vTspö  avhus  astitä  isas?m jit.as>m  (sd)  'va  ptsSJanus  "in  Kürze würden  mir  bei  der  ganzen  Menschheit ..  die  Seelen  voll  Angst,  die  Leiber  dem Gericht  verfallen  sein"  V.  5.4.
-xr^-nianl-  Adj.,  PPA.:  S.  xiaod-.—  Pü.i  xrS- siin  dät  Ö  rm-Sa,  erl. :  tiiSän  ruvän  hai  garSI- män  *xrisilak  u  *aiiää/ai')  bat  hlnd  t.  — »  Das  Wort  ist  im  Anschluss  an  Y.5/.  13  b gebildet.  —  ')  S.  10  tmya.
•  j.  y5  "daiü  xraoiJi"  bavaiti  V.  13.  34 PüZ.
If'.Tl  Hb.  91  vermutet:  j'öaJfl//j'^j-r<i/«JAroa/(/. Bei  DsT.  ZA.  3.  50  fehlt  die  SlcUe.
•  j.p  g.  xraos-  V.  'schreien'.  Praes.  2 xraosa-,  26  xraosya-.  —  PPfP.  'xrusla-.
mit  Akk.    'anschreien,   durch  Schreien
erschrecken':  yö  g^wqm  .  .  janaiti  vil vayeiti  vä  xraosyäti  vä  pazdayäti  (sd.)  vä
V.15.S.
mit  upti  "aufschreien'  vor  Angst  oder Schmerz;  zaRyUca  vispinhd  xraosmtqm upi  "und  dem  Verderben  preisgegeben sollen  sie  alle  aufschreien"  Y.  5J.  8.
mit  pa-  'durch  Anschreien,  Beschwören vertreiben':  paxrusta  kl  kaxuli  (sd.) paxrusta'  ..  V. 21.17.
mit  /rä  'anschreien,  durch  Anschreien einschüchtern':  avaizS  d?m  .  .  fraca  xrae- syöil'-''  fraca  syasjayeil  (sd.)  A.J.  13.
aL  krfiati ,  kruftäi  ,  mp.  xrösTmlan ;  np.  vgl. xiiröildan  (wozu  GlrPh.  /  b.  136).  —  PÜ.  (ju V.  /5)i  *xiSsciütan,  (luV.l:  xröiiiiiömand,  (zu \.ii):pa  a/iF  X'viiiii ;  SB.  (lu  A.)i  ältaiayi- tum.  —  ')  Oder  xiaitsöi/,  Lesung  unsicher.
•  j.  xraosya-  m.  'Schreien';  a)  zum  Zweck des  Erscl^eckens,  'Anschreien'":  *'yj  F. 2jb">.  b)  aus  Angst  'Angstgeschrei': «i'iV  /li  anyä  urva  haom  urväntm  .  . bq^aiti  °yäca  (LS.)^'  voyaca  *aiihe  ". .  (bei sva.)  trotz  ihrem  (der  Seele)  Angst-  und Wehgeschrei"  V. /j.9'(?),
Ableil.  ^  Zum  V.  xram-.  —  Pü.  (ra  V.): *xrPsa(UU,  (»u  F.):  xrßsoi,  erl.:  öh  bavH  ka viif;  hal  fas  tuiirad.  —  ■)  Ein  strafrechtliches Delikt,  wie  aus  F.  hervorgehl;  s.  auch  A.  J. 13.  —  ")  Hds.  xisyö.  —  i)  Haplol.  für  'yqya.
•  j.  xraosyö.tara  Adv.  'unter  ärgerem Angstgeschrei':  'ra/a  na  ahtmlt  voyS.- laraca  kvS  urva  pariliti  par^.asnäi  atiuhe ya'^a  ..  "unter  noch  ärgerem  Angstgeschrei und  unter  grösserem  Wehklagen  geht  seine Seele  weg  zum  künftigen  Leben,  als  .  ." V.y.8.
ISn.  aus  '•lata-  Adj.,  Kompar.  aus  xniayn-  m.. eig.  'was  noch  mehr  Wehgeschrei  ist';  aulTili. Bildung.  —  l'u. :  *3nsJlailar.
•  '}.,  g.  xraozdilta-  Adj.  (fem.  'tu-)  'der härteste,  festeste' 1  mainyui  spSni^tB  yS  't7ng asJnS vastd(sd.)Y.30.$.  a)  vonjIMra und  dessen  Fravasay''>:  ahurahe  mazds sraSslahe^a  "taheca  xra'^wislaAe^a  Y.  /.  i ; —  fravaslm  avqm  yam  ahurahe  masdä .  .  sraSilamea  'tarnca  xrä^wÜlamla  Y. 26.2.        ■
Supetl.  10  xriii.lrii-  .\dj.;  vgl.  xriu^idyah:  — Pü.;  saxtl-m,  (zu  Y.  jo):  ioxl;  Sü,:  i;idha. larah.  —  •)  VII,  durch  Y.  y3.  5  veranlasst.
=== grep xram- headword ===
2820:Hauses  für  seinen  Bedarf  wegnähme"  V.  st^r^'iwaia  snai>i/a  rixram^rttim  :far}m
10588:Ableil.  ^  Zum  V.  xram-.  —  Pü.  (ra  V.): *xrPsa(UU,  (»u  F.):  xrßsoi,  erl.:  öh  bavH  ka viif;  hal  fas  tuiirad.  —  ■)  Ein  strafrechtliches Delikt,  wie  aus  F.  hervorgehl;  s.  auch  A.  J. 13.  —  ")  Hds.  xisyö.  —  i)  Haplol.  für  'yqya.
```


## [2026-09-06T21:15:28.039Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN xiram ===\"\ngrep -n -i \"xiram\\|hiram\\|ynram\\|chiram\" HRN.txt | head -20\necho \"=== HRN leaf for p.104 (leaf 125) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==126' HRN.txt | head -60"
}
```


### [2026-09-06T21:15:29.615Z] TOOL RESULT

```
=== HRN xiram ===
=== HRN leaf for p.104 (leaf 125) ===
1-4 -
Hüb.sohniann. Zr»Mü. :>. 42o.
47<.». '/jtjeffte *^'e^tÄ'i>.-T. jiüoklich". ver^l. fer[jriijeste.
aw. ''h*'i:t.<t'i'. Yrr^'l. aj'i^f't'. p^hlv. 4/a^ (Gemme
.J».v. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).
471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
itürk. /itnL'für. v.-ii:]. NOMtrkt: bei Uübschmann.
<>^at't. Elvi]]., r!^. l:'.:'.!. //tC'.ni, /i'Uc,
aw. vt-ri:l. x'^i^Ot*-: fthlv. /iff«ir id. i. ;frt<tef^) bezw.
/'td'iiw ai. Ytriji. >cj*iiid' Selbst I-Hrstininiung'.
LW. kiipi. ;f<^'r: af;. x'*'inii Oss. ;rwföi: bei. /*«*'*»
n. /»»(t*'!. /i '<»>'// i'..«oi.
Die Diirchsichtiirktrit Jt.-s Zusammenhanges mit l'^</*'
hat wohl Jas d i:eschützt : als Grundform ist etwa *?**
aw. /'adöffii' löder */»iit)'.*y'i-| anzusetzen. Nöldeic ^'
G^'A. l^SJ. .>. t«»:;i« bezweifelt die Richtigkeit 4^*^
EtvmoloKit' vielleicht nicht mit L'nreeht.
Fr. Müllers Erklärung jWZKM. 5. 6b) aus av^
*/ atö.ui/fio nach tiunem Willen sich bewegend*
schon an .>icii wenig Überzeugendes, ganz abgesehe
von der falschen awesti:?chen Xominativbildung.
47:i. yJrätnJden 'schreiten, ^ehen".
ai. l h'ntut'. knlwftfi. hrt'n/Uitr 'gehen, schreiten'.
In der Bedeutung angenehm, erfreuend* etc. ist,
wie schon Vullers gesehen hat. /jrüm ursprünglich
yu/rem. eine Ansicht, der auch Xöldeke beipflichtet
(mündliche Mitteilung».
47o. y/fi' 'Esel*, yj^ryö^ *Hase' (^^ *Eselsohr K /ercür, /«fr^^fAr«?
u. a. m.
aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
kurd. ier, liar (GuränT): SLfy./ar: oss. /ßräg, x^*'^9
(2i)7); bei. n. ffar, /ar, LW. har^) (192); wa/. ;rwr,
«ar. cer, üer, sangl. //tr, minj. xara.
*j Vcrgl. Ilorn, ZDMG. 44, 675, No. 134.
•; Vcrgl. Barthol oniao, ZDMG. 44, 550.
```


## [2026-09-06T21:15:36.831Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 474 / xiram ===\"\ngrep -n \"474\\.\" HUB.txt | head\necho \"=== FFD خرام ===\"\ngrep -n \"خرام\" incoming/FFD/FFD_pages.txt | head -20"
}
```


### [2026-09-06T21:15:36.889Z] TOOL RESULT

```
=== HUB 474 / xiram ===
1870:474. Vgl. ZDMG. 46, 234. Dazu arm. xarbzak 'Melone' (nur
2817:1894, 474.
=== FFD خرام ===
1377:خرامیدن
1378:«خرامید» ماد ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
1379:: «خرام» < فارسی میانه 337370 < ایرانی باستان 3+737-8*. برای ۵ > آرای. 3
```


## [2026-09-06T21:15:39.120Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN costa/cutlet/coast ===\"\ngrep -n \"^cutlet,\\|^coast,\\|^costal,\\|^costa\\b\\|^cotelette\" KLN_1966.txt | head\necho \"=== KLN 1971 ===\"\ngrep -n \"^cutlet\\|^coast\\b\\|^costal\" KLN_1971.txt | head\necho \"=== SKT ===\"\ngrep -n \"^COAST\\|^CUTLET\\|^COSTAL\" SKT.txt | head"
}
```


### [2026-09-06T21:15:39.216Z] TOOL RESULT

```
=== KLN costa/cutlet/coast ===
8031:coast,  n.  —  ME.  cost,  fr.  OE.  coste  (F.  cote), ‘rib,  coast’,  fr.  L.  costa,  ’rib,  side',  which  is  cogn. with  OSlav.  kosti,  ’bone’.  Cp.  Rum.  coasra,  It., OProveng,  costa,  ‘rib,  coast’,  Sp.  cuesta,  'hill, mount,  slope’,  costilla,  ‘rib’,  which  all  derive fr.  L.  costa.  Cp.  accost,  costal,  costalgia,  cos¬ tard,  costermonger,  costrcl,  cuesta,  cutlet,  inter¬ costal.
10034:cutlet,  n.  —  F.  cotelette,  lit.  ‘a  little  rib’,  a  double dimin.  of  cote,  ‘rib’,  fr.  OF.  coste,  fr.  L.  costa, ‘rib,  side’.  See  coast  and  cp.  costal.  Cutlet  was prob.  influenced  in  form  by  cut. cuttlefish,  cuttle,  n.  —  ME.  cotul,  codul,  fr.  OE. cudele,  ‘cuttlefish’,  rel.  to  dial.  Norw.  kaule  (for *kodle),  lit.  ‘pouch  fish’,  and  to  OE.  codd,  ‘bag, shell,  husk’.  See  cod,  ‘a  small  bag’, cutty,  adj.,  short  (Scot,  and  dial.)  —  Formed  fr. cut  with  adj.  suff.  -y.
=== KLN 1971 ===
49620:coast, n. — ME. cost , fr. OF. coste (F. cote), 
49627:costal. 
49631:coast, intr. and tr. v. — ME. costeyen, costien, 
49636:coast. — A hybrid formed fr. E. coast with -al, 
57870:costal, adj., pertaining to a rib or ribs. — F., fr. 
57872:coast and adj. suff. -al and cp. coastal. Cp. also 
62366:cutlet, n. — F. cotelette, lit. ‘a little rib’, a double 
142564:coast of Norway. — Du. maelstrom (now maal- 
187143:coast of the Baltic Sea. — Fr. Slav, po more , ‘by 
195431:coast. 
=== SKT ===
4131:COSTAL.
```


## [2026-09-06T21:15:55.760Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN leaf 197 head ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==197' KLN_1966.txt | head -8\necho \"=== KLN leaf 198 head ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==198' KLN_1966.txt | head -8\necho \"=== KLN Creon/Ahura/srira ===\"\ngrep -n -i \"srira\\|Avestic sri\\|Kreion\\|kreion\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T21:15:57.687Z] TOOL RESULT

```
=== KLN leaf 197 head ===
iddle’;  all  these
words  are  cogn.  with  L.  cor,  ‘heart’.  Cp.  also Heb.  lebh,  ‘heart’,  and  lebh  yam,  ‘the  midst  (lit. the  heart)  of  the  sea’,  lebh  ha'eldh,  ‘the  midst  of the  terebinth’,  Akkad,  libbu,  ‘heart;  middle’. Derivative:  core,  tr.  v.
core-,  combining  form  denoting  the  pupil  of  the eye.  —  Gk.  xopyj,  ‘girl;  pupil  of  the  eye’.  See Cora.
Coregonus,  n.,  a  genus  of  salmonid  fishes  (ich¬ thyoid  —  ModL.,  compounded  of  core-  and Gk.  y tavta,  ‘angle’.  See  -gon.
coreligionist,  n.  —  See  co-,  religion  and  -ist.
Corema,  n.,  a  genus  of  plants  of  the  crowberry family  (hot.)  —  ModL.,  fr.  Gk.  xoprjpa,  ‘a broom’,  a  derivative  of  xopsiv,  ‘to  sweep  out’, fr.  xopop,  ‘broom,  besom’,  which  is  of  unknown etymology;  so  called  from  its  bushy  aspect. For  the  ending  see  suff.  -ma.
Coreopsis,  n.,  a  genus  of  yellow  colored  plants.  — ModL.,  compounded  of  Gk.  xopi 5,  ‘bug’  and oija?,  ‘sight,  appearance’ ;  see  coriander  and  -op- sis.  The  name  Coreopsis  was  given  to  this  genus in  allusion  to  the  seeds  which  look  like  bugs.
corespondent,  n.,  a  joint  respondent,  esp.  in  a divorce  suit  (law).  —  Formed  fr.  co-  and  res¬ pondent.
=== KLN leaf 198 head ===
rnel  tree'.  Sec  cornel, cornute,  cornuted,  adj.  —  L.  cornutus,  ‘horned’, fr.  cornu,  ‘horn’.  See  corn,  'a  horny  induration’, cornwallite,  n.,  a  basic  copper  arsenate  {mineral.)
—  Named  after  Cornwall  in  England.  For  the ending  see  subst.  suff.  -ite.
coroa,  n.,  a  former  Portuguese  gold  coin.  — Port.,  lit.  ‘a  crown’,  fr.  L.  corona.  See  crown, corody,  corrody,  n  ,  an  allowance  of  food  ( old law).  —  ML.  corrodium,  corredium,  ‘provision’. See  curry.
corolla,  n.,  the  whole  of  the  petals  of  a  flower ( bot .)  —  L.  corolla,  ‘little  crown,  garland’,  .di¬ min.  of  corona,  ‘crown’.  See  crown.
Derivatives:  coroll-ate,  adj.,  coroll-at-ed,  adj. corollary,  n.,  1)  a  proposition  proved  from  an¬ other  that  has  been  proved;  2)  an  inference; 3)  a  result.  —  L.  corollarium,  ‘garland  given  as a  present’,  fr.  corolla,  ‘little  crown,  garland; gift,  present,  gratuity’.  See  prec.  word  and  subst. suff.  -ary.
Derivatives:  corollari-al,  adj.,  corollari-al-ly, adv.
corona,  n.,  a  crown.  —  L.  corona,  ‘garland, wreath,  crown’,  fr.  Gk.  xoptov/j,  ‘any  thing  curved ; a  wreath,  garland’.  See  crown, coronach,  n.,  a  dirge.  —  Gael,  corranach,  fr.  Mir. com-,  ‘with’  (see  com-),  and  ranach,  ‘a  roaring, weeping’,  fr.  ran,  ‘to  roar,  weep’, coronal,  adj.,  pertaining  to  a  crown.  —  L.  cord- nalis,  ‘pertaining  to  a  crown’,  fr.  corona.  See corona  and  adj.  suff.  -al.
Derivative:  coronal-ly,  adv. coronal,  n.,  circlet,  diadem.  —  L.  coronalis,  ‘per¬ taining  to  a  crown'.  See  coronal,  adj. coronary,  adj.,  1)  pertaining  to  a  crown;  2)  en¬ circling;  3)  pertaining  to  either  of  the  two  ar¬ teries  supplying  the  heart  tissues.  —  L.  coro- narius,  ‘pertaining  to  a  crown’,  fr.  corona.  See corona  and  adj.  suff.  -ary. coronate,  tr.  v.,  to  crown.  —  L.  coronatus,  pp.  of coronare,  ‘to  crown’,  fr.  corona.  See  corona  and verbal  suff.  -ate.
=== KLN Creon/Ahura/srira ===
36511:sri,  also  shri,  adj.,  fortunate,  prosperous  (said esp.  of  divinities,  kings  and  heroes).  —  OI.  srih, ‘beauty,  splendor,  well-being,  dignity,  happi¬ ness’,  rel.  to  Avestic  sri,  ‘beauty’,  OI.  srirdh, Avestic  srira-,  ‘beautiful’,  and  cogn.  with  Gk. xpeiojv,  xp £<ov,  ‘lord,  master’, sruti,  also  shruti,  n.,  revealed  literature,  esp.  ap¬ plied  to  parts  of  the  Vedas  and  the  Upanishads (Hinduism).  —  OI.  snitih,  ‘the  act  of  hearing; what  is  heard’,  rel.  to  OI.  srutdh,  ‘what  has  been heard’,  and  cogn.  with  Gk.  xX£o<;,  ‘fame,  news’, xXox6?,  ‘heard,  loud,  famous’,  L.  in-clutus,  ‘fa¬ mous’,  OS.,  OE.  hliid,  ‘loud’.  See  loud  and  cp. words  there  referred  to.
```


## [2026-09-06T21:15:57.701Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins kost ===\"\ngrep -n \"^kost-\\|^ost-\\|kost-\" AHD_watkins1985.txt | head -20\necho \"=== AHD watkins krei ===\"\ngrep -n \"^krei-\\|^kreiə\\|^kreu\\|krei-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T21:15:57.762Z] TOOL RESULT

```
=== AHD watkins kost ===
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1378:CLUMP gel-1 CLUTCH! gel-1 CLUTTER gel-1 CLYSTER kleu-2 co- kom COADUNATE oi-no- COAGULUM_ ag- COAL g(e)u-lo- COALESCE al-3 COARCTATE ar- coasT kost- COBALT ku- cocciD kokkos coccus kokkos COCHINEAL kokkos COCHLEA konk(h)o- cock? ku- COCKAIGNE kak-2 COCKCHAFER gep(h)-
1395:costa kost- COSTARD kost- COSTREL kost- cot? ku-
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1682:INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
2294:STEP- (s)teu- STEPHANOTIS stebh- STERCORACEOUS  sker-4 STERE ster-1 STEREO- ster-1 STEREOBATE gWa- STERIGMA ster-! STERILE ster-5 STERN! | ster-1 STERN? sta- STERNOCOSTAL kost- STERNUM Ster-2 STERNUTATION _pster- STEROPE ster-3 STERTOR pster- STET sta- STEVEDORE steip- STEWARD wer-4 STICH steigh- STICHOMETRY steigh- STICHOMYTHIA  steigh-
=== AHD watkins krei ===
643:kreus-*
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
646:kreue-2. To push, strike. 1. Germanic *hrewwan in Old
647:kreup-
1253:APO- apo- APOCALYPSE kel-2 APOCOPE skep- APOCRINE krei- APOCRYPHA krau- APODAL ped-! APODICTIC deik- APODOSIS do- APOGEE gé APOLOGUE leg-1 APOLOGY leg-! APOMIXIS meik- APONEUROSIS (s)neau- APOPHYGE bheug-! APOPLEXY plak-2 APOSIOPESIS sWi- APOSTASY sta- APOSTLE stel- APOSTROPHE! streb(h)- APOTHECARY dhé-1 APOTHECIUM dhé-1 APOTHEOSIS dhés- APOTROPAIC trep-2 APPALL pel-2 APPANAGE pa- APPARATUS pere-1 APPAREL pere-! APPEAL pel-6 APPEASE pag- APPEND (s)pen- APPENDIX (S)pen- APPETITE pet- APPLE abel- APPLY plek- APPOGGIATURA ped-1 APPOSITE apo- APPOSITION apo- APPRAISE per-6 APPRECIATE per-6 APPREHEND ghend- APPRENTICE ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1399:CRANIUM ker-1 CRANK! ger-2 CRASH? ker-4 CRATE kert- CRATER kere- CRAW gWere-4 CRAWL! gerbh- CRAYFISH gerbh- CREATE ker-3 CREATINE kreue-1 CRECHE ger-2 CREDENCE kerd-1 CREDIBLE kerd-1 CREDIT kerd-1 CREDO kerd-1 CREDULOUS_ kerd-1 CREEK ger-2 CREEP ger-2 CREMATE ker-4 CREODONT kreue-1 CREOLE ker-3 CREOSOTE kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX ker-1 CRIPPLE ger-2 CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1468:EPIBOLY gWele-1 EPIC wekw- EPICARDIUM kerd-1 EPICENE kom EPICRITIC krei- EPIDEMIC da- EPIDERMIS der-2 EPIDIDYMIS dwo- EPIDOTE do- EPIGASTRIUM gras- EPIGEAL gé EPIGENE gene- EPIGONE gene- EPIGRAM gerbh- EPIGRAPH gerbh- EPILEPSY (s)lag- EPILOGUE leg-1 EPIMYSIUM mis- EPIPHANY bha-1 EPIPHYSIS bheue- EPISCOPAL spek- EPISODE en, sed-2 EPISTASIS sta- EPISTAXIS stag- EPISTEMOLOGY sta- EPISTLE  stel- EPISTYLE sta- EPITAPH dhembh- EPITASIS ten- EPITHELIUM dhé@(i)- EPITHET dhé-1 EPITOME tem- EPOCH segh- EPODE wed-2 EPONYM nd-men- EPONYMOUS nd-men- EPOS wekw-
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1486:EXxO- eghs EXOCRINE krei- EXODUS sed-2 EXOERGIC werg- EXONERATE en-es- EXOPHTHALMOS okw- EXORDIUM ar- EXOSTOSIS ost- EXOTERIC eghs EXOTIC eghs EXPAND pete- EXPATRIATE peter- EXPECT spek- EXPECTORATE peg- EXPEDITE ped-! EXPEL pel-6 EXPEND (s)pen- EXPERIENCE per-4 EXPERIMENT per-4 EXPERT per-4 EXPIATE pius EXPIRE spirare EXPLAIN pele-2 EXPLETIVE pela-1 EXPLICATE plek- EXPORT per-2
1595:HEM! kem-2 HEMATOCRIT krei- HEMERALOPIA amer- HEMI- sémi- HEMISTICH  steigh- HEMOPTYSIS spyeuU- HEMORRHOID sreu- HEMP kannabis
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
1674:IN-2 en INAMORATA amma INAUGURATE aug-! INCANDESCE kand- INCANTATION kan- INCARCERATE cGarcer INCARNATE sker-1 INCENDIARY kand- INCENSE kand- INCENTIVE kan- INCEPTION kap- INCERTITUDE krei- INCEST kes-2 INCH! i-no- INCHOATE kagh-
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
2187:RIDDLE! = krei- RIDDLE? ar-
```


## [2026-09-06T21:16:17.359Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Creon\\|Creon,\" KLN_1966.txt | head -5\necho \"--- leaf of Creon ---\"\nawk 'BEGIN{RS=\"\\f\"} /Creon/{print \"leaf \" NR; }' KLN_1966.txt | head -3\necho \"--- leaf of sri entry (line 36511) ---\"\nawk 'BEGIN{RS=\"\\f\"} /rel.  to  Avestic  sri/{print \"leaf \" NR}' KLN_1966.txt | head -3\necho \"--- leaf 197/198 printed page numbers ---\"\nawk 'BEGIN{RS=\"\\f\"} NR>=196 && NR<=199 {print \"### leaf \" NR; print substr($0,length($0)-300)}' KLN_1966.txt"
}
```


### [2026-09-06T21:16:19.217Z] TOOL RESULT

```
9640:Creon,  n.,  brother  of  Jocasta  and  brother-in-law of  Oedipus;  he  was  king  of  Thebes  ( Greek  my- thol.)  —  Gk.  Kpeuv,  fr.  xpetov,  a  var.  of  xpsicov, ‘ruler,  lord,  master’,  which  is  cogn.  with  OI. sriyas-,  Avestic  srayah-,  ‘better’, creophagous,  adj.,  flesh-eating.  —  Gk.  xpeoepiyop, compounded  of  xpeap,  ‘flesh’,  and  -<pi'(oz,  ‘eat¬ ing’.  See  creosote  and  -phagous. creosote,  n.,  an  oily  liquid  obtained  from  tar.
--- leaf of Creon ---
leaf 206
--- leaf of sri entry (line 36511) ---
leaf 797
--- leaf 197/198 printed page numbers ---
### leaf 196
  sense  develop¬ ment  cp.  Avestic  zlrlbaya,  ‘middle’,  OSlav. srudice,  ‘heart’,  sreda,  ‘middle’,  Russ,  serdee, ‘heart’,  sereda,  ‘middle’;  Wednesday  (i.e.  middle of  the  week)’,  Lith.  sirdis,  ‘heart’,  W.  craidd, ‘heart;  center’,  Bret,  kreiz,  ‘m
### leaf 197
rn’,  and cdpiae,  gen.  of  copia,  ‘plenty’.  See  corn,  ‘horny induration’,  and  copious, cornucopiate,  adj.,  resembling  a  cornucopia.  — Formed  fr.  prec.  word  with  adj.  suff.  -ate. Cornus,  n.,  a  genus  of  plants,  the  dogwood  and the  cornel  (hot.)  —  L..  ‘co
### leaf 198
 -ion). For  the  change  of  Latin  a  (in  rdptus)  to  f  (in cor-reptus)  see  accent  and  cp.  words  there  re¬ ferred  to.
correspond,  intr.  v.  —  F.  correspondre,  fr.  ML. corresponded,  fr.  cor-  and  L.  responded,  ‘to answer’.  See  respond.
Derivatives:  correspond-ence,  n
### leaf 199
phee,  n.,  a  ballet  dancer.  —  F.  coryphee,  fr.  L.
coryphaeus.  See  prec.  word.
Coryphodon,  n.,  a  genus  of  extinct  mammals (palconrol.)  —  ModL.,  compounded  ofxrjp’j^r,, ‘head,  top,  summit',  and  o8e!>v,  gen.  o86vto?, tooth’.  Sec  coryphaeus  and  odonto-. coryza,  n
```


## [2026-09-06T21:16:53.662Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB kust ===\"\ngrep -n \"^kust\\|kustīk\\|kustik\\|kustīg\\|kust \" NYB_vol2_glossary.txt | head -20\necho \"=== HRN kusti/kost ===\"\ngrep -n -i \"kustl\\|kusti\\|kustik\\|Gürtel\\|kost'\" HRN.txt | head -30"
}
```


### [2026-09-06T21:16:53.722Z] TOOL RESULT

```
=== NYB kust ===
366:akustan [’kwstn'] to hang, to suspend, pt. ākust 2027. 328. — Ps. 136? *kwsty; MPrs ”gwst (S); MPrth abstr. ’gwsigyft (S).
2355:kust [kwst'] side, direction; region, dis- trict 113-115.117 passim; pat [kwst! + 1] aside 14%. — Paz. kūst, cf MPrt kws ‘country, countryside’ (A-H TIT); Arm. lw. ko?s ‘side’, kust ‘the waist, the belly’ = NP kust.
2356:kustak [kwstk'], with indef. art. ~-é [kwstk +1], = kust 616. 79-15, 819, 133. 176.10, 77183139; pl. ~-ihā 112!; weighing scale 7219. — MPrs kwstg (S); Paz. kūsta.
2357:kustik [kwstyk] the sacred thread worn by the Zoroastrians (tied round the waist) 2521, - MPrs kwštyh (S; NW form); Paz. NP kusti. V. Modi, Ceremonies 183—190.
2358:kuštan [kwštn', NKSWN-tn'], pres. pass. 3d p. sg. kwšhyt' = kusihet 981-3 used as an opt. (hence the neg. mā), but the form is obscure, one would expect the imp. kušēt: to kill, to slaughter 258. 275, 3214. 9413, 10715; perf. pass. kust hat 981. — = NP; Av. (432) fra-kaoš-, pres. -kuša-; MPrs kwst (pt.), kwš-, Verbum 168.
3070:patkust [p'tkwst] district, province Pl: 8. — The reading is unambiguous and already established by Herzfeld. The form commonly met with in BP is p'tkws = pätkös; MPrthPrs p’dgws, MPrs also p’ygws; Paz. pad-kés (Mx 135). Cf kust, kustak.
3071:*pat-kust [PWN kwst'] 5" is possibly the irregular spelling of the pt. of a vb. *patkustan "to come into contact with, to join side by side with (hac): api-š hac Vahram u Anähit ~ and it (the planet Jupiter) has joined side by side with Mars and Venus; but the construction is strange, and this guess is only proposed faute de mieux.
3199:the virtual dir. obj. which grammatically ought to be the formal subj. of a pret. pass. (mixed act.-pass. construction): Sähpuhr varzēkar ~ frac xuand 15” sq.; api-§ han zan ~ ne ēzat 10°? ; cand dastava- ran... u dānākān i Bran šahr ~ bē kust 10718-14. — OP rād- ‘reason, cause’ in radiy postpos. 'on account of', avahya- rüdiy ‘for this reason’; MPrth r’d, MPrs ry; Paz. NP rd.
3788:Pärsikän ... fréstit thou hast been sent by the Persian king 1319-1? (for frēstīt he); cē-šān tö-c kust 27° (for kust he; or perhaps an absolute clause: after thy having been slain by them); but kē tē dat he? by whom hast thou been created? 577-5; eoordinated with another pers. pron.: man u to āzmāyišn kuném 4); to an [LK 'NH] ... barom (for barém) ‘thou and I (we) shall...” 5319-20-24), v. s. v. arža- nikenitan; — 2. dir. obj.: né tčy-ic pat depahr därem 21%; mā ziön . . . to dzanénd 2612, 2912; tài to giram (v. gir-) 35°; etc.; — 3. to, for, against thee: har vat kas to nē tuvan kartan is not able to do thee any harm 6!9-%; tē ce vinās jasi estet? what sin has befallen thee? (v. jastan) 1211, 5317; nē tö u ne héc dam i man ästisn nē būt hah there would have been no permanence for thee, nor for any crea- ture of mine 3515-16; beginning the sentence and taken up later by the independent form of the encl. pron.: töy-ic kë vat hah at tar menčt 331^; — 4. agent: to nē dānā- kihä kart 419-11; to amāh-ic dat hem 39"; tē zat mar 1 Tür 99??; ete.; — 5. gen. a) dam i to 335; b) det. rel. attr.: 6 õi % tē pusar 51%; et i to pus 5218-14-15; eto.; c) tē brat 2211 etc.; to mät 227%; to pus 5116; — 6. with prep.: apar tē, hac tē, 6 to, pat to, tē rād. — 51% ZK-p tw: read an-ip to as a sort of ethic dat.: ‘thou mayest understand’ or the like, with an empha- sizing tē, v. lan B; v. further s. v. -p. — < tava, Av. (787) gen. of (786 sqq.) Owa-, OP 0uva- ; the cas. rect. Av. (661) tvēm < tuvam — OP, which would have develop- ed into *tū in Milr, has been absorbed by to, as far as we can judge. MPrthPrs tw, with -c: twy(y)c; Paz. 0o, Ou, tu (0 has no etymological value); NP tū. Cf -t and at.
6023:kwštyh: kustik
6278:xistan: axistan makas: *macah pätkös: pätkust razmik āyozišn: äyöz- *takile: kurušk
6702:kusti: kustik
7247:kustah: kostan
7248:kustan: köstan kušūftan, kušūf-: višuf-
=== HRN kusti/kost ===
960:5) Bei. LW. C?) ähihjag, n. ähenjuy *ßaiid, Gürtel' (U).- 15 -
7446:854. UuHt *Seite, Flanke', hu^Vl^ kustl 'Gürtel', vergl.
7454:kurd. LW. (?) kustin 'tödton*; bei. L\V. (?) kuäag,
7473:») Syr. LW. J^D^'ID, J^nDD, p^DDIp; ai'ab. LW. kustij (de
7474:Lagarde, Ges. Abb. 59, 60); bei. LW. kustl (143). — Aber nicht gehört
7536:866. {\)kemer 'Gürtel', kemra^),
7537:aw. kamara- 'Gürtel*; phlv. kamar,
7538:LW. kurd. kemer 'Gürtel*, af/. kamar; oss. LW. d.
7539:kamdri Trauengürtel'.
9548:1105. heiuymi 'Gürtel*.
9550:ana- 'Gürtel' (de Lagarde, Ges. Abh. 89).
16278:kuStifii 856.
19362:kustin 855.
```


## [2026-09-06T21:16:55.204Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB kusti ===\"\ngrep -n -i \"kusti\\|Gürtel\" HUB.txt | head -20\necho \"=== barguStuwan ===\"\ngrep -n -i \"bargustuwan\\|bargustavan\\|gustuwan\\|barkustuwan\" HRN.txt HUB.txt PHD.txt NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T21:16:55.274Z] TOOL RESULT

```
=== HUB kusti ===
=== barguStuwan ===
```


## [2026-09-06T21:17:01.072Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7440,7480p' HRN.txt\necho \"=== which printed page? ===\"\nawk 'BEGIN{RS=\"\\f\"} /854\\.  *[Uu]/{print \"leaf \" NR}' HRN.txt | head"
}
```


### [2026-09-06T21:17:02.964Z] TOOL RESULT

```
853. kcs 'Achselhöhle' i).
aw. kasa- 'Achselhöhle'; phlv. kas; ai. kdksa- 'Gurt-
gegend (der Zugtiere), Achselgrube*.
bei. LW. kaB^ kos 'Gurt, Riemen, Achselgrube' (130);
WiX/. kal 'Achselgrube'.
ij Di..l. xen (;Vuller.s).— 191 -
854. UuHt *Seite, Flanke', hu^Vl^ kustl 'Gürtel', vergl.
hergustvuan (No. 205) ; kusftgir 'Ringkämpfer (AM. 2()6
Zeile 8).
phlv. ktist^ kustak 'Seite*, kusttk^),
855. kuSten 'tödten', nt^^t^lD (Qiss. Dan.).
aw. l/ftaos-, kusaiti 'tödten'; phlv. kustan, vergl. asö]-
kvs (für aw. asavaynya-, vd. 5 (47)); skr. KÄö5-, kusnäti
'zerreissen' (?).
kurd. LW. (?) kustin 'tödton*; bei. L\V. (?) kuäag,
n. ßusay 'todten, scli lachten (207).
856. feesß/ ^Schildkröte ; Krebs (Zodiac, Sahn. I, 77 Vers
285)', keseto (dial.).
aw. kasyapu' 'Schildkröte' oder *Krebs' (Geldner,
KZ. 25, 503, 5()6j ; skr. (Brhm.) kagydpa- 'Schildkröte .
af/. kasy 'Schildkröte'; bei. käsib (190).
857. Ä-e«efc 'Elster .
Toniaschek, Painirdialokte S. 771, veigkM'cht aw.
karsiptan-^ phlv. kars{i)ft (L)eutun*i: nicht sicher), wa/.
karjöpc, sar. karjopc, si;'n. ksebc 'ElstiM-'.
858. kiSver^ kesver 'Ph-dteil'.
aw. karsvar- 'Weltteil'; phlv. kisvar^).
859. kesläen ziehen'.
aw. [/^km's-, karsayefi^); phlv. kasttan; ai. 1. [/^kars-,
• kdrsati, karmyati 'ziehen, schleppen'.
kurd. kisän ziehen'; af>'. k/dl; bei. kasay, n. /i'asay
'ziehen, abziehen, herausziehen' (19:^); arm. LW. (?)
Karsem 'ziehen*.
») Syr. LW. J^D^'ID, J^nDD, p^DDIp; ai'ab. LW. kustij (de
Lagarde, Ges. Abb. 59, 60); bei. LW. kustl (143). — Aber nicht gehört
dazu lat. c^ista *Rippe*, das Meringer, Sitzb. WAW. CXXV, *Beitr. z.
indg. Decl.*, 42, mir nicht einleuchtend, zu ai. dbthi- 'Knochen* stellt.
') Eine Volksetymologie in 'Selections of Zätsparnm* (West
P. T. I) 7, 9.
») Aw. [/has- will Hübschmann ZDMG. 44, 558 ausser Betracht
lassen.800. kef \Schaiiin'.
=== which printed page? ===
leaf 213
```


## [2026-09-06T21:17:17.886Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"205\\. \" HRN.txt | head -10\necho \"---\"\ngrep -n \"bergustvuan\\|bergustuvan\\|bergustvan\\|gustvuan\\|gustuvan\" HRN.txt | head"
}
```


### [2026-09-06T21:17:17.945Z] TOOL RESULT

```
2179:205. bergustuwän 'Panzer, Pferdepanzer'.
11123:205. vadrak 'Otter -).
---
7447:hergustvuan (No. 205) ; kusftgir 'Ringkämpfer (AM. 2()6
```


## [2026-09-06T21:17:20.509Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2175,2200p' HRN.txt\necho \"=== leaf ===\"\nawk 'BEGIN{RS=\"\\f\"} /205\\.  *bergustuw/{print \"leaf \" NR}' HRN.txt"
}
```


### [2026-09-06T21:17:22.528Z] TOOL RESULT

```
204. bevf/er 'Glück'.
SiW.*uparö.kara- {wergl.uparö.kairga-), deLagarde,
Beitr. z. altbaktr. Lex. 71, von Geldner, 3 Yasht 12,
gebilligt.
205. bergustuwän 'Panzer, Pferdepanzer'.
Etwa *uparö,kustapäna'; phlv. vergl. kustak \Seite'.
Vergl. np. kust (No. 854).
Im Gersäspnäme (Macan, 2103, Vers 9 v. u.) steht
die kürzere Form kustuwän (Text gustuwän), worauf
mich Herr Prof. Nöldeke aufmerksam macht.
206. bern 'Egge'.
Nur aufgenommen, weil G. Meyer (albanes. Wörter-
buch, S. 44) np. bern 'Egge als Etymon der entlehnten
*) Phlv. vrejan ist nur fehlerhafte Schreibung; np. biristen ist
durchaus nicht ungebräuchlich, wie Fr. Müller (WZKM. 5, 185) nach
V
Vullcrs meint. Ich citire nur Sahn. I, S. 20, Vers 8.^ - 48 —
slavischen Wortgruppe alb. braus *Egge*, serb. brana,
poln: brona, russ. borona, ngr. ößdpva etc. annimmt.
Das neupersische Wort ist aber ganz unsicher; die
Wörterbücher (ausser dem FS.) überliefern nur die
Form bezen, im Gacophylacium und bei Woliaston
fehlt es.
207. burnäf bernä Müngling', burnm 'Jugend, Kindheit',
Njm5 Is. 3, 4, 5, wumaj wernä, purnäk (unbelegt);
vergl. arab. LW. burnäj, barnaj, eine Dattelart (de
=== leaf ===
leaf 69
```


## [2026-09-06T21:17:41.103Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 برگستوان ===\"\ngrep -n \"برگستوان\\|برگستون\" BQT_v1_pages.txt | head\necho \"=== BQT v3 کستی ===\"\ngrep -n \"کستی\" incoming/BQT/BQT_v3_pages.txt | head\necho \"=== BQT v3 کشتی ===\"\ngrep -n \"کشتی\" incoming/BQT/BQT_v3_pages.txt | head -5\necho \"=== BQT v2 خرام ===\"\ngrep -n \"خرامیدن\\|خرامان\" BQT_v2_pages.txt | head"
}
```


### [2026-09-06T21:17:41.209Z] TOOL RESULT

```
=== BQT v1 برگستوان ===
=== BQT v3 کستی ===
21566:‏فندق شکستی - کنابه ‎Hy jt‏ دادن
31945:و در عرف ابشان زنار خوانند ومعر بآ نکستیج
31946:است؛ و کستین هم بنظ‌آمده است که مد از
31948:کستیمه ۴ ‎Jol che‏ بروزن‌پمتیمه,
31967:‎bd‏ من رن اکنون کز دستهای بسته باچون ‎gis pels‏ بای دگرفت کستی.
31968:کتی زرتشتیان را « بند ‎5st op‏ گویند و معرب آن « کستیج» و ‎a”‏
31971:‏این کستی از ۷۲ نخ از پشم سفید کوسفند تهیه میگردد و ‎OT‏ باید
31975:‏کهنبار که اعباددیتی ‎JL‏ باشد. کستی را ‎wh‏ سه‌پار بدور کمربندند واین
31977:هرزرتشتی پس از من هفت سالگی موظف است ت که کستی را بدور ‎PS‏
31983:‏کستی ۱ . نم ‎Jal‏ بر وزن ستی ۰
=== BQT v3 کشتی ===
3293:‎ath‏ - و شکافتن کشتی ‎OT‏ دربا را .
3978:«احن التقاسیم. مقدسی.چاپ‌لیدن ص۳۱؛ باد موافق « بادی که‌اعد کشتی رالی باشد و کشتیرا
3979:_مخصوساً کشتی های شرامی را- بطرف «قصد مافران سوق دهد:
14076:کشتی باشد - و درعربی ‎OT‏ و دوائی را گویند
14790:‏پیر کشتی ریخت موت از حباك».
=== BQT v2 خرام ===
4162:                                           ‫باشد ‪.‬‬        ‫دانثور ‪ ,‬خصی رگاوبن که خرامان و از روی‬
6710:                                                          ‫‪۷‬ف‬‫خرامیدن همهت بعنی بخرام ر‬
6783: ‫خرامان‬     ‫روائی »‬   ‫پر ورن‬    ‫‪۳‬‬       ‫جمانی‬
6947:                          ‫شده را نیز گویند ‪.‬‬       ‫خرامان براه رفتن باشد ‪ -‬و بمعنی میل کردن‪-‬‬
10152: ‫جلبهالی الاوعال من خرخیز اولی‪,‬هلانهم اليه‌اقرب ولم بجلب من‌العراق وخرامان وقدقبل‌فیه ایض‬
10636:                                            ‫در فرهن‬              ‫‪-‬‬    ‫‪۵‬‬          ‫کین رك‪ :‬خرامیدن‪.‬‬
11205:‫ثالك وفتح فوقالی» بمعنی خرام وخرامیدن باشد‬        ‫ی‬               ‫رن رک‬                ‫کی‬
11217:‫خشرین «بروزن‌بروین؛ بمعنی‌خرامیدن‬                 ‫بفتح اول و کرنالی وسکون‬              ‫«‬       ‫خرش‬
20257:                                                                                        ‫بنشاط و خرامان باشد» و‬
24971: ‫باشد» وایشالر! ازاین جهت‌رند خوانند که منکر‬                                                  ‫خرامیدن را نیزکوبند ‪.‬‬
```


## [2026-09-06T21:17:47.889Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v3 page tag before line 31945 ===\"\nawk 'NR<=31990 && /\\[pdf page/{p=NR\": \"$0} END{print p}' incoming/BQT/BQT_v3_pages.txt\ngrep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | awk -F: '$1<31990' | tail -3\necho \"=== v3 lines 31940-31995 ===\"\nsed -n '31940,31995p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T21:17:49.564Z] TOOL RESULT

```
=== v3 page tag before line 31945 ===
31941: [pdf page 436]
31799:[pdf page 434]
31849:[pdf page 435]
31941:[pdf page 436]
=== v3 lines 31940-31995 ===
‎+ ‏ره : رشیدی‎ N°
[pdf page 436]
-۱16۳- کط

نیز گوین د که کشتی ‎ALS‏ خراسان ب رکمبندهد
و در عرف ابشان زنار خوانند ومعر بآ نکستیج
است؛ و کستین هم بنظ‌آمده است که مد از
تحتالی ‎Og‏ باشد .
کستیمه ۴ ‎Jol che‏ بروزن‌پمتیمه,
خاری راکوبندکه شتر آلرا برخبت ‎we‏
‏کسری ۴ = پکس اول وسکون شا
و رای قرشت بتحتانی کشیده » دام اوتیان
عادلاست؛ و هرباك ازپادشاهان عجم رابیز کسری
میکفته‌اد ۰
‎fas‏ + ینم اول وسکون ثالی وطای

۱ -کتی = کشتی . ازپپلوی ‎sel kostik‏ است ‎Ls.‏ اخبر ‎We‏ در گزارش‌پهلوی
اوستا و در کتابهای پهلوی بمعنی کمربند منصوص زرتشتبان استبمال‌شده, ازآ نجمله درتفسیر بند
۲ ف گرد ٩۱وبندهای ‎ALY‏ فر‌گرد ‎VA‏ وندیداد وضل ۲4 بند ۲۲ وصل ۳۰ بند. *۳بندهش.
‎LS‏ مزبور از مادة 6050 ‎gies‏ است که در پهلوی بممنی ‎ghee‏ + سوی » جالب و ‎AT‏ است ودر
پارسی نیز کشت وکست بهمین‌معنیآمده, چنانکه درلاتینی 60508 و در انگلیسی 00854 و در
‎YT‏ 1516 و در فراسوی 6۵46 از همین ماده است . لمت کشتی (مصارعه) ‎BART yy‏
از همین ربشه است . بنابرین کشتی کرفتن عبارتست از مصارعةٌ دوتن با ‎BFS 9 SS‏
هم برای غلبه برطرف . در اشعار پارسی کتی بهردومعنیآمده. کمال اسماعیل اصفهان یگوید:

کردون که دایم آرد هر سختبی برویم آورده از طرفها در کار بنده سستی

‎bd‏ من رن اکنون کز دستهای بسته باچون ‎gis pels‏ بای دگرفت کستی.
کتی زرتشتیان را « بند ‎5st op‏ گویند و معرب آن « کستیج» و ‎a”‏
‏«کنتکه » و « کشنیج» است. [ رك : تفس ]. در زبان لیتوالی ‎justa‏
‏بمعنی کمربند است ومااین‌کلمه قرابت دارد «لوروزنامه. تعلیقات ‎Ve‏
‏این کستی از ۷۲ نخ از پشم سفید کوسفند تهیه میگردد و ‎OT‏ باید
بدست زن موبدی بافته شود. ۷۲ نخ به ‎٩‏ رشته فسمت شده ۰ هر رشته
دارای ۱۲ نخ‌است. عدد ۷۲ اشاره است به ۷۷ فصل سنا که مهمترین
قسمت اوستاست ۰ ۱۲ اشاره است بدوازه ماه سال. و ‎٩‏ اشاره است به ‎٩‏
‏کهنبار که اعباددیتی ‎JL‏ باشد. کستی را ‎wh‏ سه‌پار بدور کمربندند واین
نیزبمدد سه اسل مزدینا : منش نيك »کوش نيك وکنش ‎Cas‏ ميباشد.
هرزرتشتی پس از من هفت سالگی موظف است ت که کستی را بدور ‎PS‏
‏بندد : رگ : مزدیتا ص ۲۷۵۷-۷4۳ .

‏رستنیی ‎ath‏ بیاهی ماب لکه مربان صی‌الراعی
خوانند .

‏کستی ۱ . نم ‎Jal‏ بر وزن ستی ۰
بسن کختيباشد و آن چنان اس که د و کس‌بر
هم چیبند و یکدیگر را بر زمين زنشد و ‎Jel‏
‏این لفت کستی است چه از کستن مشتق است که
بمعنی کوفتن باشد و چون در فارسی سی‌بی‌قطه
و شین‌قطه‌دار بهم تبدیل می‌بابند بناب رآ نکشتی
خوانند - و بمعنی زنار هم آمده است و آن
‎gly‏ باشد که ترسایان و هندوان بر ‎PF‏
‏بندند و کاهی برکردن هم افکتند - ورمتاترا

‏۴ - در رشیدی بهمین معنی آمده و محشی رشیدی نوشته : « در سرا جکستبنه بنون
بجای میم آورده . ظ . مصحف «کسیمه ‏ (هم) . ۴ - معرب « خسرو؟ .
۴ قنط ‎Ay)‏
```


## [2026-09-06T21:18:14.814Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v1 گستوان ===\"\ngrep -n \"گستوان\\|گستوا\" BQT_v1_pages.txt | head\necho \"=== v1 page tags near 261 ===\"\ngrep -n \"\\[pdf page 48[0-9]\\]\" BQT_v1_pages.txt | head\necho \"=== v3 pdf page 442 (p.1649?) کشتی ===\"\nawk '/\\[pdf page 442\\]/,/\\[pdf page 443\\]/' incoming/BQT/BQT_v3_pages.txt | head -60"
}
```


### [2026-09-06T21:18:16.601Z] TOOL RESULT

```
=== v1 گستوان ===
18847:بر گستوان  *‏ منم کاف فارسیو تای
=== v1 page tags near 261 ===
=== v3 pdf page 442 (p.1649?) کشتی ===
[pdf page 442]
Vea

کشتو )= ‎ce‏ اولبروزن ‎lay‏
‏نیم پخته و نیم‌ری (۱) را کویند .

کشتو زد © بروزن مفلوك » پمعنی ‎AY‏

پشت وکاسه پشت و کشف باشد .

کشقه - بکسر اولبروزن رشته ؛بمعنی ۰

کاشته و زراعت شده باشد ۴ - ‎Ty‏ و زردآلو
وامرود وشفتالو و امثال آنرا نیز گویندکه ‎Sls‏
‏آنها را برآورده و خشك کرده باشند ۴ - وبفتح
اول کاج و لوچ را کونند ؛ وبا کاف فارسی هم

() چش : - وئیم رس ۰

.» ‏نیز کوبند . « جهانگیری‎ ge TS

کاشتن .

۴ - ثتاگوی نوا بی تو دل از غم

سوزنی سمرفندی « فرهنگه نظام *.
۴ ح کتی (هم) :

در خرایات تبینی کهزمستی همه سال

را هب دیر ترا کشتی و زنار دهد .

‎JE?‏ غزئوی ۰ ‎dp‏ ص
‎Nes‏

‎wT e‏ (هم)

‏آمده است .

‎A‏ ه نم اول » بمعتی زنار باشد
و ‎oT‏ رسمانی است که ترسایان ‎ay AR,‏
‎stay‏ وگاهی بر گردن هم اندازند ۴ - ویمعتی
‎al‏ دوکس برهم چنبند و خواهند یکدییگر
را بر زمین زنشد مشپور است ‎٩‏ - و خطاب از
کشتن همهت" - ویفتح اول سفینه رااگوبند ۷
- و پیاله‌ای که بشکل سفینه‌سازند ۸ - ویک
اول. خطاب اززراعت کردن باشد ‎٩‏ یعتی زراعت

‏۴ - اسم مقعول ازه کشتن >

‎. ‏نیم است چون امرو دکشته‎ ot

‎Cea) ) ‏ازه کشتن > ( بالضم‎ ole ode ‏دوم ثخص‎ - ٩

‏۷ - دراصل بفتح ‎Js]‏ درپهلوی1) 6850 «تاوادبا۱۹۲: ‎ey‏ ولی‌امروزه‌بکر اول‌تلفظشود:

‏کشتی ‎(oh) HES‏ ای باد شرطه برخیز

‎iS gS angeS: By ۸
```


## [2026-09-06T21:18:26.593Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v1 برگستوان context ===\"\nawk 'NR<=18847 && /\\[pdf page/{p=NR\": \"$0} END{print p}' BQT_v1_pages.txt\nsed -n '18840,18880p' BQT_v1_pages.txt"
}
```


### [2026-09-06T21:18:28.316Z] TOOL RESULT

```
=== v1 برگستوان context ===

بر گست باکاف فارسی بروزن‌بدمست:
بمعنی بر گس ام ت که مماذاله وخدا تکندباشد,
و بهمین معنی با بای فارسی هم آعده است ۴ .
بر گستان ۴ با سین بی نفطه بروزن
انکشتان » مخفف ب رکگنوان باشد وآن پوششی
است که در روز جنگه پوشند و بر اسب هم
پوشانند .
بر گستوان  *‏ منم کاف فارسیو تای
فرشت » پوششی باشد که در روز جنک بوشند
و اسب را تيز بوشانند .
بر گس د پروزن مدرسه ؛بمعنی‌پوشیده
ر پنهان باشد .
بی کی
بر گ کار دو فی « دواییست کهآ نرا
شیرازی آ هودوستك و بعربی حزا کویند»یکر
حای ی نقطه و زای نقطه‌دار بالف کشده .
بر کم باکاف‌بروزن مرهم » بازداشتن
و منم را گوینن - و باژد ارنده ر منم کننده را
نیز کفته‌اند - و امر بدینععنی هم‌هست عنی‌منع
کن و بازدار » و باين معنی بجای حرف ثانی‌زای
بر کفك » بر وزن فرزند » امرد خیم
تنومند را گویند - و بمعنی رشوت و بار» حم
اضتت. انیت
بر کنه یقح اول و او نون وسکون
ثافی » درهم کوفته شدء هر چیزرا کوبندبتخضیص
عطر دات ۰ وبکسر اولهم امه و
ب رک نیل بانون بروزن م رکه فیل»
تهند و بعربی وسمه گویند .
ک9 6 هت بروژن انوه , نام شهری‌است
از عراق که آئر! برقو گویند ۷ .
بر که اد شیر - تام شهرست‌ازولات
فاری ۳ ۹
بر که لا جو درد « کنابهاز آسمان‌است.
بر کی » بنتم اود و انی و کاف نازی
بئحتانی رسیده » کلاه درازی باشد که زاحدان بر
سر گذارند و بمربی‌برنی خوانند ۷ » وباینممنی
گرچه نامردم است آن تا کس
اش کی فک رگ
۷ رك : ابر
* - حاجت بکلاه بر کی داشتدت یست
درویش صفت باش و کلاه تتریدار.سعدی.
```


## [2026-09-06T21:18:33.868Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -3 BQT_v1_pages.txt | cat -A | head -3\ngrep -c \"pdf page\" BQT_v1_pages.txt\nawk 'BEGIN{RS=\"\\f\"} /بر گستوان/{print \"leaf(0-based)=\"NR-1}' BQT_v1_pages.txt"
}
```


### [2026-09-06T21:18:35.562Z] TOOL RESULT

```
^LM-[M-1 M-[M-5 M-[M-1! M-[M-1$
7 M-YM-^EM-YM-^HM-YM-^E M-[M-3 M-YM-^DM-XM-'M-YM-^E$
M-YM-^E M-[M-1 0 M-YM-^H M-XM-7M-YM-^B M-XM-5M-YM-^AM-XM-1M-XM-1M-XM-1M-YM-^FM-[M-^LM-XM-'M-XM-9M-XM-/M-XM-1M-[M-^LM-XM-1M-YM-^EM-XM-'M-XM-1M-YM-^HM-[M-^L$
0
leaf(0-based)=481
```


## [2026-09-06T21:18:42.564Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /خرامیدن/{print \"leaf(0-based)=\"NR-1}' BQT_v2_pages.txt | head\necho \"=== leaf 181 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==182' BQT_v2_pages.txt | head -70"
}
```


### [2026-09-06T21:18:44.347Z] TOOL RESULT

```
leaf(0-based)=115
leaf(0-based)=182
leaf(0-based)=192
leaf(0-based)=423
leaf(0-based)=424
leaf(0-based)=434
leaf(0-based)=438
leaf(0-based)=450
=== leaf 181 ===
                                                                                                 ‫‪۷ ۲۳‬‬


              ‫اهبه اآزسمان باشد ‪.‬‬
                                ‫خراب اکمتن ک‬                  ‫اول ‪ »,‬دمعثی مشرق‬    ‫م‬   ‫‪-‬‬   ‫خراسان!‬


‫تح اول بورزن لواش ‪.‬‬
                  ‫«‬                 ‫خر اش‬                     ‫امت که در مقابل مغرب با ‪ -‬و نام ولابتی‬
                                        ‫‪۲ ٩‬‬       ‫‪۰‬‏‬




 ‫‪-‬‬    ‫کردن‬      ‫وفبمعنی رخنه‬       ‫رحنه باشف‬           ‫نجعي‬    ‫آن ولات در مشرق‬         ‫وون‬
                                                                                         ‫مشهور چ‬    ‫هم هست‬
‫و تایکار‬    ‫و از کار افشاده وسقط شده‬      ‫‪-‬‬   ‫و خراشدن‬        ‫فاری و عراق واقم است بنا بران بدین نام‬
 ‫و دوستده‬      ‫زده‬   ‫خف‬   ‫و موه‬     ‫‪۴‬‬         ‫ا‬   ‫آهده‬
                                                                ‫ازموسیقی‪.‬‬    ‫خوانده‌اند ‪ -‬ونام نفمه‌ای هم هت‬

                                        ‫را نگیوزیند ‪.‬‬         ‫دروژن بداختر» موذیات‬
                                                                                 ‫حر استر ‪ /‬ب‬
‫= بر وزن ترآشیدن ›‬                ‫حر اشیدن‬                    ‫راکوبند مطلقاهم‌چو ماروعقرب وزنبور رموزچه‬
                                                                                                ‫وامثال آن ‪.‬‬
           ‫بمعنی ریش کردن ومجروح ساختن باشد ‪.‬‬
 ‫‪ ۰‬معرب‬        ‫طین‬
                 ‫ازن‬
                   ‫لو‬‫سبر‬
                       ‫حراطین =‬
                                                               ‫‪-‬نابه آاسزمان‬
                                                                           ‫خر اس خر اب ک‬
 ‫خراتین امت و آن کرمی باشد که در گل نرم‬
 ‫تکون پیدا کند و بعربی حمرالارض گوبند جم‬                       ‫به‌عنی خراس‬     ‫جر اس خسسان ‪-‬‬
                                         ‫‪ - ۱‬دریپلوی ‪(0252۲2۷۲‬مشرق) «میناه‪: › ۲: ۳۱‬‬
               ‫دروباش و جپان را میخور آسان‬                           ‫خوشا جابا بر و بوم خراسان‬
               ‫خراسان آن بود کزوی خورآسد‬                              ‫زبان پپلوی هر کو شناسد‬
               ‫کجا ازوی خورآبد سوی ابران ‪.‬‬                          ‫خورآسان رابودمعنی‪ :‬خورآبان‬
     ‫«وس ورامن ص ‪۱۷۱‬؟‪.‬‬
      ‫ورك ‪ :‬اسفا ‪ ۲ :۱‬ص ‪ « ۹۷۱.۰‬خراسان " تفسیره‌المشرق » « مفاتیج‌العلوم خوارزمیس‬
     ‫»رات ‪,‬‬ ‫ه‬     ‫بانا»ن‬   ‫طهست‬
                              ‫‪:‬براشهر (بشابور ‪۰‬ف‬    ‫‪ ۲‬؛ خراسان قدیم شامل چهاربخش‌بوده ا‬
      ‫پوشنگه » بادغیس » طوس) ‪ -‬مروشاهجان » سرخس » دا » ابیورد ‪ .‬مروالرون » طالقان آمل‬
     ‫‪,‬کگوانان » طخارستان علیا ‪ ,‬خت ‪ ,‬اندرآبه » بامیان » بفلان ‪ ۰‬والج » روستای بیل ‏‬  ‫فارباب ز‬
     ‫‪۰‬لم » سمدگان ‪ -‬ماوراءالنپر( بخارا ‪ ۰‬چاچ » طراز‬  ‫بدخشان ن‪۰‬رمن ‪ ۰‬چنانیان‪ .‬طخارستان سفلی خ‬
     ‫‪ ,‬اشروسنه ‪ ۰‬سیام » فرغانه و سمرفند ) « معجم‌البلدان »‬             ‫تان‬
                                                                         ‫فی»‬
                                                                           ‫نشد» صفد ‪ ۰‬هو کس ‪.‬رنو‬
     ‫خراسان کنونی ازشمال محدود است بماوراءاللهر ‪ ۰‬از مشرق بهربرود ودشت ناامید » از جنوب‬
     ‫بکرمان واز مغرب بعراق عجم و استراباد ‪ .‬طول آن ازشمال بجنوب بکرمان اوز مغرب بعراق‬
     ‫عجم و استراباد ‪ .‬طول آن ازشمال بجنوب ‪ ۰۰۸‬واز مشرق بمغرب *‪ ۸4‬کیلومتر و ماحت آن‬
      ‫کشف رود ورود‬‫گکارن و‬  ‫نزديك به ‪ ۰۰۰۰۲۳‬کیلومتر ھربح است ‪ .‬رودهای مهمی مانند اترك و‬
       ‫‪.‬معیت‌خراسان قرب ‪۰۰۰۰۰۳۴۱۰۱‬‬  ‫"یبشرم (قراسو ) درآن جاری است وبمصرف زراعت میرسد ج‬
     ‫است ‪ .‬کرسی‌آن مشهد وشهرهای‌آن ‪ :‬سرخس ‪ ,‬دره گز ‪ ۰‬فوچان » بجنورد ‪ ۰‬نیشابور ‪ ,‬جوین ‪۰‬‬
     ‫ولشن‬
        ‫سبزوار » اسفراین * جام » باخرز خوواف » تربت حیدری ‪ :‬ترشیز ‪ ۰‬فردوی ( تون ) گ‬
           ‫(طبس) » قاینات » شاهرود » سمنان وداعفان امت ‪.‬ک«یهان ‪ .‬جفرافیای سیاسی ‪.* ۹۷۱-۰۱۲‬‬
                     ‫‪ - ۴‬پپلوی ‪ , 7(8)05]۵۳5‬اوستا ‪ « 3615]8۳6-‬اسفا ‪ ۲ :۱‬ص ‪٩ ۰۸‬‏ ‪.‬‬
                                                       ‫‪ = ۴‬غراش ( ه‪ .‬م) «اسفا ‪ ۲ :۱‬ص ‪. ۰۷۰‬‬
         ‫ببر دو رخافت هست خراش ‪.‬‬                               ‫‪ ۴‬ت اکر چه لطف دارد تقش‬
      ‫رکوید‌سمرقندی‪ « .‬لغت فرس‪۵*۲‬؟‪.‬‬
                      ‫یدن ( یوند مصدری ) = غراشیدن («‪.‬م‪).‬‬                   ‫‪.‬م(‪) .‬‬
                                                                                 ‫«راش‬
                                                                                    ‫‪ -‬از خ‬
```


## [2026-09-06T21:18:49.051Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==183' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-06T21:18:51.309Z] TOOL RESULT

```
  ‫واح‬   ‫جع‬                                                                                               ‫خرافات‬

 ‫خوش راهم کنته‌انده ‪ -‬ویمعنی شادی وشادمالی‬                                                         ‫حنایقبطیه ‪٩‬‏‬
 ‫هم‌آمده است‪ -‬وبمعنی‌مهمالی وضیافت! ‪-‬ومرردة‬                ‫خر افات = بفتح اول و بافا(‪ )۱‬بر‬
                      ‫‪.‬‬    ‫بمهمالی طلبیدن همهت‬
                                                        ‫وامربوط را‬
                                                                 ‫‪.‬خنان پریشان ن‬
                                                                              ‫وزن کرامات م‬
 ‫خراهر ود ‪ -‬نوعی از امرود برزکه‬                            ‫گوند عربی‬           ‫اول همآمده است‬      ‫گوبند ؛ وم‬

         ‫)‪ (4‬می هزه باشد ‪۱‬‬          ‫ناهموار(‪ )۳‬و زشت‬                                                     ‫است ؟ ‪.‬‬
‫‪ ۰‬خرامقان = بفتح اول مویم وقاف بر‬                          ‫خراك ‪ = ۴‬بفتح اول بروزت هلاك »‬

‫وزن قرابتان » رستنیی باشد مانند سنبلالطیب ‪.‬‬             ‫صدا و خراخری که بسبب کلو فشردن از کلو‬
‫مایل است و بخ آن هم‬             ‫اما رنگگ آن ببزی‬        ‫با درهنگام خواب از بینیآدمی برمی‌آبد ؛ وبا‬
‫بسنبل میماند وبوی ستبل‌لیز دارد وطبیعت آن‌هم‬                                            ‫مشدید ثالی همکفته‌اند ‪.‬‬
‫ادوكلی ‏‬
       ‫زديك امت بسنبل و درطعم وحیلان‬                       ‫بروزن‌نظام ‪ ۰‬رفتاری‌را گونند‬        ‫س‬   ‫خرام‬
                                               ‫باشد ‪.‬‬
                                                           ‫که از روی جاز و سر کشی و زببابی باشد ‪- ۴‬‬
 ‫ارمین "د راه رفتن بناز وتف‬   ‫خ‬                            ‫وخوش رو وجمیل و زدان خوش‌صورت وشکیلرا‬
                      ‫وزیبایی باشد ‪. ۸‬‬                     ‫)‪(1‬‬       ‫و خبرهای‬    ‫دز کفته‌اند ‪ -‬ونوید ومدگالی‬



        ‫(‪ )۳‬چش‪ :‬اهنوار ‪.‬‬                  ‫‏(‪ )٩‬چك‪ .‬چش ‪ :‬چیزهای‪.‬‬                      ‫وفا‪.‬‬   ‫چش ‪:‬‬   ‫(‪)۱‬‬



                                                                             ‫(‪ )4‬چك چش ‪ + :‬و ‪.‬‬

                                             ‫‪ « 661۲۵۳۵۲ ۱‬لك س ‪۱٩۲‬‏ رك‪ :‬خراتین ‪.‬‬
 ‫«خرافة» کنمامة‪ .‬آلچه‌چیده شودموه ‪ 4‬ونام‌مردی یری زاده ازقسلة عذرة و اوآ لجه ازیر بان مل وش‬

   ‫هن احد بت‬        ‫و گفتندی‬   ‫آبرا بدروغ می‌داشتند وهر سخن اورا پاور نداشتندی‬              ‫شل مبکرد »‪ .‬ومردم‬

  ‫‪۴‬‬           ‫» ‪۳‬‬   ‫ظ منتهی‌الارب‬       ‫لب‬    ‫خرافات حکات‌ای‬         ‫خرافة ‪ ۰‬ای هی‌حد بت مستملح کذب ‪ ۰‬و‬

                                                                                ‫«خراخر («‪.‬م‪۰ ).‬‬     ‫فی‪ :‬خرخر‬

                                            ‫در فرهن‬              ‫‪-‬‬    ‫‪۵‬‬          ‫کین رك‪ :‬خرامیدن‪.‬‬
  ‫گها خرام را بمعنی وعد ونوید‪( .‬و مانند آن)‬


  ‫ضبط کرده‌اند ولی اشمار ذبل تاصرخرو وبض شعراء دیگر شان میدهد که خرام بمعنی وفای‬
                                                 ‫بوعد و دمرقابل نوید استعمال میشده» له بمعنی وعد ‪:‬‬
             ‫را ‪.‬‬     ‫امش‬
                        ‫خشرمر‬
                            ‫آراسته با‬                                 ‫چون داد توبند رلج و دشواری‬
   ‫«اسرخسرو »‬
             ‫نوبدی که آ را لباشد خرامی ‪.‬‬                              ‫نوبدت دهد هر زمالی بقردا‬
   ‫‪« .‬ملقات دبوان ناصرخسرو ص ‪۵۹5 ۵‬‬              ‫ناسر خرو‬

 ‫‏‪ - ٩‬اسدی کوید ‪ « :‬خرام ‪ ۰‬کس دیگر بمهمالی بردن بود بعد از نوید ‪ .‬فرخی (سیستالی) گفت‪:‬‬
             ‫و آمده تازه روی وخوش بخرام‬                               ‫نويف‬    ‫داده‬   ‫دولت او را بملك‬

  ‫«لغت فرس‪۷۳۳٩‬‏ ‪.‬‬
  ‫‪ - ۲‬از‪ :‬خرام ( ه‪.‬م‪) .‬ب‪+۳‬دن ( یوند مصدری)؛ جزو اول‌هندی باستان ‪)۲ 130۳_2‬‬
                                                                                     ‫داسفا! ‪ ۲ :‬ص ‪ ۹۳‬و‪.٩۹‬‏‬
                    ‫دولت بارینه تصور کنو‬                             ‫‪ - ۸‬چند خرامی وتکبر کنی‬
```


## [2026-09-06T21:19:05.205Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON خرامیدن ===\"\ngrep -n \"خرامیدن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== MON کستی/کشتی(کمربند) ===\"\ngrep -n \"کستیج\\|کستی\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T21:19:05.289Z] TOOL RESULT

```
=== MON خرامیدن ===
MON_part2.txt:9444:فیربدن: ۱1-0 (مصل.) خرامیدن باناز. 
MON_part2.txt:48851:(مص‌ل.) به ناز حرکت کردن؛ خرامیدن» 
MON_part2.txt:52740:خرامیدن به ناز. 
MON_part2.txt:72012:رفتن: با دلبری و طنازی رفتن» خرامیدن. به 
MON_part2.txt:72134:نخوت خرامیدن. فخر کردن» مباهات 
MON_part2.txt:73658:خرامیدن به نازء گراز بدن. خم شدن. مانده 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:9444:فیربدن: ۱1-0 (مصل.) خرامیدن باناز. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:48851:(مص‌ل.) به ناز حرکت کردن؛ خرامیدن» 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:52740:خرامیدن به ناز. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:72012:رفتن: با دلبری و طنازی رفتن» خرامیدن. به 
=== MON کستی/کشتی(کمربند) ===
MON_part2.txt:22987:کستی: آا:ه۲ [- کشتی - معر. کستیج - 
MON_part2.txt:22997:سال باشند.) کستی را را باید ۳ بار دور کمر 
MON_part2.txt:23003:موظف است که کستی رابه دور کمر نندد. 
MON_part2.txt:23339:کشتی: 05۱7 (.) کستی. گلاو بز شدن دو 
MON_part2.txt:23343:گسترند و کستیگیران روی آن کشستی 
MON_part2.txt:32762:کستی: آ-۵251 (حامص.) رشتی» ناز سایی؛ 
MON_part2.txt:48919:(مص م.) سانب: طورون تا کستی::عشسات 
MON_part2.txt:59158:رای کستین ضودداری کردن. (امسص.) 
MON_part1.txt:25476:بند زبان: کستی. بند ساعت: بندی از چرم يا 
MON_part1.txt:71604:بندند؛ کستی؛ کشتی. کمرندی که ذمیان
```


## [2026-09-06T21:19:06.747Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW costa ===\"\ngrep -n \"^costa\" LEW_1910.txt | head\necho \"=== LAT costa ===\"\ngrep -n \"^costa\" LAT.txt | head\necho \"=== IEC kost ===\"\ngrep -n \"^kost-\\|^kostā\\|^kosta\" IEC.txt | head\necho \"=== SYN BONE/RIB ===\"\ngrep -n \"^4\\.16 BONE\\|4\\.46 RIB\\|RIB$\" SYN.txt | head"
}
```


### [2026-09-06T21:19:08.602Z] TOOL RESULT

```
=== LEW costa ===
=== LAT costa ===
14191:costa, -ae f.: i° cote, orax 0 T); 3° cot 4 , flanc. Atteste depuis Plaute.
77111:costad britt., 288.
77112:costad iri., 1171.
=== IEC kost ===
=== SYN BONE/RIB ===
5449:4.16 BONE Goth. Lith. kaulas k gaeor ON bein Lett. kauls Gr OKKaNO Dan. ben, knogle ChSl.  kostt NG 0s Sw. ben SCr.  kost oe 0ss0 OE ban Boh.  kost’ be 08 ME bone Pol. kosé g — fueso NE bone Russ. kost’ an os. Du. been, knok Skt. asthi- Ir. a OHG bein Av. ast- Tr, ond MHG bein v. Cae NHG  knochen (-bein) Br. ask + from the inherited group, words NHG knochen, fr. MHG knoch knoche, ne ‘knuckle, knot’, this with dim. MLG
```


## [2026-09-06T21:19:16.091Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT costa ===\"\nsed -n '14191,14205p' LAT.txt\necho \"=== SYN bone discussion ===\"\nsed -n '5449,5470p' SYN.txt\necho \"=== SYN RIB ===\"\ngrep -n \"4\\.4[0-9] RIB\\|RIB Goth\" SYN.txt | head"
}
```


### [2026-09-06T21:19:16.167Z] TOOL RESULT

```
=== LAT costa ===
costa, -ae f.: i° cote, orax 0 T); 3° cot 4 , flanc. Atteste depuis Plaute.
Panronad, M.L.3379.cotti die
- 361 -
De meme que latus, le mot a du s'employer a basse epoque comae ad-
verbe ou preposition avec le sena de "i c6te de, auprbs", cf. M.L.
s.u.; le v.fr. encoste remonte a in costa. - In costa a sana doute 6t6
abreg6 en costa, coaae ad-, dS-latus en latus.
Derives: costalis (v6g.); costatus: Varr. R.R.5,5,8 [houes]; corpore
bene costato, d’ou costatum, M.L.3380; costula M.L.338oa.
II n'y a aucun aot identique ailleurs. Mada la forne rappelle celle
de v.sl. kostt "03", et ce mot lui-meme est ins 6 parable du groupe de
lat. os (y. ce mot), akr. asthi , etc. 11 y aurait donc ici une sorte de
pr 4 fixe *k- aemblable k celui qui figure dans caper, capra. Cf. A. Meillet,
Roczn. Slaw. 9,74.
costum, -I n.{costus, costcs f.): costus, piante. Emprunt au gr.
=== SYN bone discussion ===
4.16 BONE Goth. Lith. kaulas k gaeor ON bein Lett. kauls Gr OKKaNO Dan. ben, knogle ChSl.  kostt NG 0s Sw. ben SCr.  kost oe 0ss0 OE ban Boh.  kost’ be 08 ME bone Pol. kosé g — fueso NE bone Russ. kost’ an os. Du. been, knok Skt. asthi- Ir. a OHG bein Av. ast- Tr, ond MHG bein v. Cae NHG  knochen (-bein) Br. ask + from the inherited group, words NHG knochen, fr. MHG knoch knoche, ne ‘knuckle, knot’, this with dim. MLG
for ‘bone’ come by eeualizetion. Sem or through terms denoting a particular hone, esp. ‘knuckle-bone’, or by exten- sion of ‘hollow stalk’, to the long bone of arm or leg, or by extension of the hard ‘kernel’ of fruits to the analogous parts of the body.
1, IE *ost-, etc. Ernout-M. 716.
Grk. dcréov; Lat. os, gen. ossis, also ossu, ossum (> It. osso, Sp. hueso, Fr., Rum, os); W. asgwrn, Br. askourn, Corn. ascorn; Skt. asthi-, gen. asthnas, Ay, ast-, asti-; Arm. oskr; Alb. asht. Here also ChS]. kosti, etc.? See below, 6.
2, NG xéxcado neut., fr. Grk. xéox- kahos ‘kernel of the pine cone’, deriv. of xoxxos ‘kernel, grain, seed’.
3. Ir, cnaim, NIr. cnaimh : Grk. nun ‘leg between knee and ankle’, ee a at the back of the 1.59, , ieee : ae a Pedersen Fenttelele? of ‘bone’ through
4, ; ee cae 8 ban, etc., general ‘ m for ‘bone’ now only
i cpds, as el , 7 \- ie 3 Scure, FalleTorp 60, ); origin ob-
Walde-P. 1.185 f.
knokel ‘bone, knuckle’ (> Dan. knokkel, knogle ‘bone’), ME knokel, NE knuckle, NHG knéchel ‘knuckle’: ON knjikr ‘round summit’, Lith. gniaudzti ‘close the fist’, etc. Walde-P. 1.582. Falk-Torp 69. The meaning ‘knuckle’ is the more general and earlier, whence ‘bone’ only by later extension (not ‘knuckle’ from ‘bone’, asin NED).
5. Lith. kaulas, Lett. kauls, OPruss. acc. kaulan : Grk. xavddés, Lat. caulis ‘stalk’, Ir. cuaille ‘post, stake’, also Skt. kulya- ‘canal, channel, ditch’ (hence neut. kulya- ‘receptacle for bones’, rarely ‘bone’, no direct connection with the Baltic use), with common notion ‘long, hollow shape’. Walde-P. 1.332. Doubt- less applied first to the long bone of arm or leg. Cf. Lat. caulis used by Pliny of the ‘bony part of an ox’s tail’; also the use of ON leggr (4.35).
6. ChSl. kostt, etc., general Slavie : Lat. costa ‘rib’. Further analysis of both as k-ost-, with relation to IE *ost- (above, 1) is attractive but dub. Walde-P. 1.186. Ernout-M. 225, 716. Berneker 582 f.
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
208 SELECTED INDO-EUROPEAN SYNONYMS 4.162 RIB tk.  wAeupdv Goth. .... Lith. Sonkaulis ne seat ON rif Lett. riba Lat. costa Dan. ribben’ ChSl.  rebro It. costa Sw. revben SCr. __rebro Fr. cole OE rib Boh. ebro Sp. costilla ME rib Pol. zebro Rum.  coastd NE rib Russ. ebro Tr. asna Du. rib Skt. parcu-, prsti- NIr.  ecasna OHG rippa Av. parasu- . asen MHG rippe Br. kostezen NHG rippe
The largest group of words for ‘rib’ is connected with words for ‘cover with a roof’, ‘a roof’ and were evidently applied to the plural ‘ribs’ as forming a sort of roof over the interior of the thorax. Some are connected with words for ‘bone’. The secondary use as ‘side’, etc. is widespread.
1. Grk. wAevpéy, etym.? Boisacq 794.
2. Lat. costa (> It. costa, Fr. céte, Rum. coastd; Sp. cueste as ‘rib’ replaced by deriv. costilla) : ChSl. kostt ‘bone’ (4.16). Walde-P. 1.464. Ernout-M. 225. Walde-H. 1.281.
3. Ir. asna, NIr. easna, W., Corn. asen: Grk. écréov ‘bone’ etc. (4.16). Pedersen 1.85.
(source of Fr. cété ‘side’), deriv. of Lat, costa (above, 2). Henry 77.
4. ON rif, OE rib, OHG rippa, ete. general Gmc. (but Dan., Sw., rev ag ‘rib’ replaced by Dan. ribben, Sw. revben, epds. with ben ‘bone’) : ChSl. rebro ‘rib’, etc. general Slavic, fr. the root seen in Grk. épé¢w ‘roof over’, dpodos ‘roof’, ete. Walde-P. 2.371. Falk-Torp 896.
5. Lith. Sonkaulis, cpd. of Sonas ‘side’ and kaulas ‘bone’.
=== SYN RIB ===
```


## [2026-09-06T21:19:17.097Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON کستی entry ===\"\nsed -n '22980,23010p' MON_part2.txt\necho \"=== MON کشتی ===\"\nsed -n '23335,23350p' MON_part2.txt"
}
```


### [2026-09-06T21:19:17.172Z] TOOL RESULT

```
=== MON کستی entry ===
فرش‌ها و سکه‌های کم یور در ایران 
باستان بدین کتابت صورت می‌گرفته. (گیا.) 
پربوز. 
کستته: (0-)1۵5-۱۵۸ (امف.) کو فته» کو فته شده. 
(۱.) غلةٌ کوفته که هنوزش پاکك نکرده باشند 
یعنی از کاه جدا نشده باشد. ( گیاء) سرخ مرد» 
عصی الراعی» هفت‌بند. 
کستی: آا:ه۲ [- کشتی - معر. کستیج - 

کتتستک کستکك: کشتیج] )٩(‏ کمربندی است 
زردشتبان را و آن از ۲ نح از شم سفید 
گوسفند تهیه می‌گردد و بدست زن موبدی 
بافته شود. ۷۲ نخ به " رشته قسمت شده» 
هر رشته دارای ۲ ۱ نخ است. عدد ۲ اشاره 
است به ۲ ۷ فصل سنا که مهمترین قسمت 
اوستا است. ۲ ۱ اشاره است به ۲ ۱ ماه سال» 
7 اشاره است به ۲ گهنبار. (که اعیاد دینی 
سال باشند.) کستی را را باید ۳ بار دور کمر 
پیچید و اين نیز به عدد ۲ اصل مزدیسنا 
(منش نیکك» گوش نیک و کنش نیک) 


9 
موظف است که کستی رابه دور کمر نندد. 
کشتی» مصارعت. 

کس ده: ۱05-001 [- کس‌دهنده] (رص‌فا.) 
زنی که از راه نامشروع با مردان رابطه دارد؛ 
روسیی» فاحشه. 

کسر: ۹ اع (مسص م.) شکتت» خرد 
=== MON کشتی ===
سفنه سازند. (کد.) آفتاب؛ خورشید. (کذ.) 
ماه نو ء هلال. 


کشتی: 05۱7 (.) کستی. گلاو بز شدن دو 
تن با یکدیگر برای زورآزمایی و زمین زدن. 
ترکیات اسمی: تشکك کشتی: ( کشتی) 
تشکی که بر کف زورخانه یا جای دیگر 
گسترند و کستیگیران روی آن کشستی 
گیرند. خاک کشتی: (کشتی) سابقاً معمول 
بود برای کشتی‌های خارج از زورخانه زمین 
را هموار می‌کردند و در آن خاک نرم 
مسی‌ریشتد که آن را «خاک کشستی: 
ش. کمتا جنانکه امروزه تشکك کشتی 
می‌آنداز ند (ه ۲۰۵ ۴)اشتک کشتی:( کی ) 
سابقاً پهلوانان نامی که ناچار بوده‌اند در ایام
```


## [2026-09-06T21:19:41.974Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY کشتی / کستی / خرام / کتلت ===\"\ngrep -n \"کشتی\\|کستی\\|خرام\\|کتلت\\|برگستوان\" incoming/ARY/ARY_pages.txt | head -20\necho \"=== ARY latin index KOST/KRAM/KREI ===\"\ngrep -n -i \"kost\\|kram\\|krei\\|costa\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-06T21:19:42.037Z] TOOL RESULT

```
=== ARY کشتی / کستی / خرام / کتلت ===
=== ARY latin index KOST/KRAM/KREI ===
2457:KOST (BOHEMIAN) soa » ASTI, AST: AVESTAN) glo)
2458:KOST :(SLOVAK) Sil AST, ASTAG, :(PAHLAVI) ole
2473:AMINDAROV: 2 KOST (RUSSIAN) yy
2474:iF rgb dy KosT “\czECH) Se
2475:KosT SERBIAN) «ype
5523:TANC, TANAKTI, TANAW, TAKRAM. TAT AFGHAN) (24) gil
12095:HOUWAN . KOFTAN, KOSTAN, KOB
12407:BRYW (WELSH) ($315 KRAMARTS  :(TOKHARIAN A)A 55
12739:KREIS NORETON) 332 -HUARTA i
```


## [2026-09-06T21:19:47.901Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=2458 && /\\[pdf page/{p=$0; n=NR} END{print n\": \"p}' incoming/ARY/ARY_latin_index_pages.txt\nsed -n '2450,2480p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-06T21:19:49.808Z] TOOL RESULT

```
2445: [pdf page 87]
T ontons: (STEEL) 866 STAAL (DUTCH) gaca
SKEAT: _ GTEEL) 600 -STAKLA, (OLD PRUSSIAN) oS yo3.4
tt 1gbG oly STACLAN
lendloal
king gh So Sorte tgngh 90519 ool
GAS, gas se 5 gh 2g Sade 92 03)9 gal
yg 23 SOL; 22 FY cel
KOST (BOHEMIAN) soa » ASTI, AST: AVESTAN) glo)
KOST :(SLOVAK) Sil AST, ASTAG, :(PAHLAVI) ole
KAULAS LITHUANIAN) | ¢\ 3 ASTUXAN, ASTAXVAN
ASIL HOLD IRISH) pS $34) STAG HOSSETIC) gong)
ASKOURN (BRETON) 3 3p SUQAN, HESTI KURDISH) 53,5
AST, ASKTE = — (ALBANIAN) ,g\T ASTHI, (SANSKRIT) 2 Sie
HASTAI (HITTITE) <0 ‘ASTHNAS
OSKR ARMENIAN) «+!
‘REFERENCES cathy OsTEON GREEK) by
Poko, —=~SO*~C~*~CS~S~«S 0S, 08S, OSSEUM LATIN) eV
BARNHART: (OSSEOUS) 739 OS, (FRENCH) 4s
DELAMARRE: (8) 106 HUESO (SPANISH) glist
MACKENZIE: n osso AITALIAN) g\ds\
BUCK: , 207 os x(RUMANIAN) gles,
ONIONS: (OSSEOUS) 635 osso (PORTUGUESE) 5 »
SKEAT: (OSSEOUS) 416 Kosé POLISH) lg)
AMINDAROV: 2 KOST (RUSSIAN) yy
iF rgb dy KosT “\czECH) Se
KosT SERBIAN) «ype
L
[pdf page 88]
vv
AG | lysed
: fetta
```


## [2026-09-06T21:19:59.047Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/costa#Latin\" \\\n \"https://www.etymonline.com/word/coast\" \\\n \"https://www.etymonline.com/word/cutlet\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%B4%D8%AA%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%B3%D8%AA%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D9%85%DB%8C%D8%AF%D9%86\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 275 verification (Kost / Kram / Krei)\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T21:20:03.445Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/costa#Latin
/home/sfmqrb/git/rishe/data/verification/sources/web/95291d23b7d61b2c.txt
### https://www.etymonline.com/word/coast
/home/sfmqrb/git/rishe/data/verification/sources/web/edaa137aab5811da.txt
### https://www.etymonline.com/word/cutlet
/home/sfmqrb/git/rishe/data/verification/sources/web/68eca68795c63612.txt
### https://en.wiktionary.org/wiki/%DA%A9%D8%B4%D8%AA%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/3e4a8157ed6c5c06.txt
### https://en.wiktionary.org/wiki/%DA%A9%D8%B3%D8%AA%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/b8dc9e393c675d5f.txt
### https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D9%85%DB%8C%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/b157d86b115b4b36.txt
```


## [2026-09-06T21:20:06.516Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## costa Latin\"; grep -n -A25 -i \"^Latin\" 95291d23b7d61b2c.txt | head -60\necho \"########## coast etymonline\"; sed -n '1,80p' edaa137aab5811da.txt | grep -n -i -A6 \"coast (n\" | head -40"
}
```


### [2026-09-06T21:20:06.585Z] TOOL RESULT

```
########## costa Latin
########## coast etymonline
23: coast (n.) 
24-
25- early 14c., "margin of the land;" earlier "rib as a part of the body" (early 12c.), from Old French coste "rib, side, flank; slope, incline;" later "coast, shore" (12c., Modern French côte ), from Latin costa "a rib," perhaps related to a root word for "bone" (compare Old Church Slavonic kosti "bone," and PIE root *ost- ), but de Vaan dismisses this and calls it "an isolated word without etymology."
26-
27- Latin costa developed a secondary sense in Medieval Latin of "the shore," via notion of the "side" of the land, as well as "side of a hill," and this passed into Romanic (Italian costa "coast, side," Spanish cuesta "slope," costa "coast"), but only in the Germanic languages that borrowed it is it fully specialized in this sense (Dutch kust , Swedish kust , German Küste , Danish kyst ).
28-
29- French also used this word for "hillside, slope," which led to the English verb meaning "a slide or sled down a snowy or icy hillside," first attested 1775 in American English. Expression the coast is clear (16c.) is an image of landing on a shore unguarded by enemies; to clear the coast (1520s) was to make it suitable for landing.
--
34: late 14c., "to skirt, to go around the sides, to go along the border" of something (as a ship does the coastline), from Anglo-French costien , from the French source of coast (n.).
35-
36- The meaning "sled downhill," first attested 1834 in American English, is a separate borrowing or a new development from the noun. In bicycle-riding, "descend a hill with the feet off the pedals," from 1879. Of motor vehicles, "to move without thrust from the engine," from 1896; figurative use, of persons, "not to exert oneself," by 1934. Related: Coasted ; coasting .
37-
38- "Coasting" consists in throwing the legs up over the handles and allowing the bicycle to rush of its own impetus down hill. It can only be done with safety where the road is perfectly smooth, hard, and free from obstructions; but, under such conditions, bicycle coasting affords one of the most glorious and exhilarating of sensations, and, next to ballooning, its motion most nearly resembles the flight of a bird. [Harper's Weekly, Dec. 20, 1879]
39-
40- The reckless coasting down the long hills on the route was scarcely more defensible. Speeds of 25 to 30 miles an hour were reached in some instances. The common road is not the proper place for such exhibitions, especially in populous centres. The risk is altogether too great, both for occupants of the vehicle and for other frequenters of the highway. [account of an automobile race on the streets of New York in The Horseless Age, June 1896] 
--
47: 1570s, "come side-by-side or face-to-face with," for any reason, from French accoster "move up to, come alongside" (Old French acoster ), from Late Latin accostare "come up to the side," from assimilated form of Latin ad "to" (see ad- ) + costa "a rib, side" (see coast (n.)). Now usually in the sense "approach and speak to" (1610s). Also picked up as the verb for a prostitute's solicitation of a customer (1812). Related: Accosted ; accosting .
48-
49- Infamous houses, he states, are in all parts of the metropolis, but most numerous in small streets, leading from public thoroughfares. "Some of them adjoin churches, chapels, and even the courts of law. There is one locality in which vicious women accost persons as they issue from the door of a chapel on the Sabbath. In another situation, the officiating clergyman while in the pulpit, is in a position to witness the proceedings in a contiguous brothel." [Michael Ryan, M.D., "Prostitution in London," 1839]
50-
51- coast guard (n.) 
52-
53: also coast-guard , 1827, a guard stationed on a coast, originally to prevent smuggling, later serving as a general police force for the coast; see coast (n.) + guard (n.).
54-
55- coastal 
56- coaster 
57- coastline 
58- costa 
59- costal 
--
75: "large variety of apple," late 14c., coster; late 13c. in Anglo-Latin, perhaps from Anglo-French or Old French coste "rib" (from Latin costa "a rib;" see coast (n.)), if the notion is "a large apple with prominent 'ribs,' " i.e. one having a shape more like a green pepper than a 
76-
77- slide 
78-
79- Middle English sliden, "glide, move smoothly and easily over a surface," also "to fall, lose one's balance through slipping," from Old English slidan (intransitive, past tense slad, past participle sliden) "to glide, slip, fall, fall down;" figuratively "fail, lapse morally, err;
80-
```


## [2026-09-06T21:20:17.391Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## کشتی\"; grep -n -i \"etymolog\" -A12 3e4a8157ed6c5c06.txt | head -80"
}
```


### [2026-09-06T21:20:17.442Z] TOOL RESULT

```
########## کشتی
73: Etymology 1 
74-
75- 2.1.1 
76- Pronunciation 
77-
78- 2.1.2 
79- Noun 
80-
81- 2.1.2.1 
82- Derived terms 
83-
84- 2.1.2.2 
85- Descendants 
--
88: Etymology 2 
89-
90- 2.2.1 
91- Pronunciation 
92-
93- 2.2.2 
94- Noun 
95-
96- 2.2.2.1 
97- Derived terms 
98-
99- 2.2.2.2 
100- Descendants 
--
103: Etymology 3 
104-
105- 2.3.1 
106- Pronunciation 
107-
108- 2.3.2 
109- Adjective 
110-
111- 2.3.3 
112- Noun 
113-
114- 2.4 
115- References 
--
123: Etymology 
124-
125- 3.2 
126- Pronunciation 
127-
128- 3.3 
129- Noun 
130-
131- 3.3.1 
132- Declension 
133-
134- 3.4 
135- Further reading 
--
143: Etymology 1 
144-
145- 4.1.1 
146- Pronunciation 
147-
148- 4.1.2 
149- Noun 
150-
151- 4.1.2.1 
152- Declension 
153-
154- 4.2 
155: Etymology 2 
156-
157- 4.2.1 
158- Pronunciation 
159-
160- 4.2.2 
161- Noun 
162-
163- 4.2.2.1 
164- Declension 
165-
166- 4.2.2.2
```


## [2026-09-06T21:20:19.942Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n \"Middle Persian\\|kust\\|Proto-Iranian\\|wrestling\\|girdle\\|kustīg\" 3e4a8157ed6c5c06.txt | head -40"
}
```


### [2026-09-06T21:20:19.988Z] TOOL RESULT

```
328: From Middle Persian 𐭪𐭱𐭲𐭩𐭪𐭩 ( kštyky /⁠kaštīg⁠/ , “ boat, ship ” ) .
331:Particularly: “Not listed in etymological dictionaries. Is this a loanword from some unknown language or is it natively derived from Proto-Iranian? Note the similarity with Sanskrit काष्ठ ( kāṣṭha , “ wood ” ) .”
424: Borrowed from Parthian *kuštīg , from Proto-Iranian *kušti- , a t-extension of Proto-Iranian *kuši- ( “ side (of the body) ” ) , from Proto-Indo-European *kuḱis ( “ (female) pubic hair; vulva ” ) , from *kew-k- , from *kew- ( “ to be concave or convex ” ) . [ 1 ] Doublet of کستی ( kosti , “ sacred Zoroastrian waist-girdle ” ) , which was inherited, [ 2 ] as well as with کس ( kos , “ vulva ” ) ; outside of Iranian, cognate with Sanskrit कुक्षि ( kukṣi , “ belly, interior, womb ” ) and Lithuanian kūšỹs ( “ pubic hair; vulva ” ) .
460: wrestling 
474: Bengali: কুস্তি ( kusti ) 
476: → Gujarati: કુસ્તી ( kustī ) 
482: → Kannada: ಕುಸ್ತಿ ( kusti ) 
486: → Marathi: कुस्ती ( kustī ) 
693: Borrowed from Classical Persian کشتی ( kuštī ) . Cognate with Marathi कुस्ती ( kustī ) .
709: wrestling 
760: Persian terms inherited from Middle Persian 
761: Persian terms derived from Middle Persian 
771: Persian terms derived from Proto-Iranian
```


## [2026-09-06T21:20:51.698Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nsed -n '415,445p' data/verification/sources/web/3e4a8157ed6c5c06.txt\necho \"=== references section ===\"\ngrep -n -A12 \"^ References\" data/verification/sources/web/3e4a8157ed6c5c06.txt | head -40"
}
```


### [2026-09-06T21:20:51.755Z] TOOL RESULT

```
 Shahmukhi script: کَشتی ( kaśtī ) 

 Etymology 2
 [ edit ] 

 Persian Wikipedia has an article on: کشتی (ورزش) 

 Wikipedia fa 

 Borrowed from Parthian *kuštīg , from Proto-Iranian *kušti- , a t-extension of Proto-Iranian *kuši- ( “ side (of the body) ” ) , from Proto-Indo-European *kuḱis ( “ (female) pubic hair; vulva ” ) , from *kew-k- , from *kew- ( “ to be concave or convex ” ) . [ 1 ] Doublet of کستی ( kosti , “ sacred Zoroastrian waist-girdle ” ) , which was inherited, [ 2 ] as well as with کس ( kos , “ vulva ” ) ; outside of Iranian, cognate with Sanskrit कुक्षि ( kukṣi , “ belly, interior, womb ” ) and Lithuanian kūšỹs ( “ pubic hair; vulva ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /kuʃ.ˈtiː/ 

 ( Iran, formal ) IPA ( key ) : [kʰoʃ.t̪ʰiː] 

 Rhymes: -iː 

 Readings

 Classical reading ? 

 kuštī

 Iranian reading ? 

 košti

 Noun
=== references section ===
115: References 
116-
117- 3 
118- Punjabi 
119-
120- Toggle Punjabi subsection 
121-
122- 3.1 
123- Etymology 
124-
125- 3.2 
126- Pronunciation 
127-
--
551: References
552- [ edit ] 
553-
554- ^ Edelʹman, D. I. ( 2011 ), Etimologičeskij slovarʹ iranskix jazykov [ Etymological Dictionary of Iranian Languages ] (in Russian), volume 4, Moscow: Vostochnaya Literatura, pages 411-2 
555-
556- ^ Chehabi, Houchang ( 2018 ), “Wrestling in the Shahnameh and Later Persian Epics”, in The Layered Heart: Essays on Persian Poetry ‎ [1] , →ISBN , pages 241—242 
557-
558- Punjabi
559- [ edit ] 
560-
561- Etymology
562- [ edit ] 
563-
```


## [2026-09-06T21:20:56.144Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DA%AF%D8%B3%D8%AA%D9%88%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ku%C5%A1ti\" \\\n \"https://en.wiktionary.org/wiki/%D9%83%D8%AA%D9%84%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/c%C3%B4telette\" \\\n \"https://en.wiktionary.org/wiki/%F0%90%AC%99%F0%90%AC%AD%F0%90%AC%8D%F0%90%AC%AD%F0%90%AC%80\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 275 verification (Kost/Krei nodes)\" 2>&1 | tail -1; done"
}
```


### [2026-09-06T21:21:01.489Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DA%AF%D8%B3%D8%AA%D9%88%D8%A7%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/d737443648507f18.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ku%C5%A1ti
/home/sfmqrb/git/rishe/data/verification/sources/web/50583c67b7641e59.txt
### https://en.wiktionary.org/wiki/%D9%83%D8%AA%D9%84%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/0dce9104c0df76e9.txt
### https://en.wiktionary.org/wiki/c%C3%B4telette
/home/sfmqrb/git/rishe/data/verification/sources/web/c038084345c76c49.txt
### https://en.wiktionary.org/wiki/%F0%90%AC%99%F0%90%AC%AD%F0%90%AC%8D%F0%90%AC%AD%F0%90%AC%80
/home/sfmqrb/git/rishe/data/verification/sources/web/053bbb95e1034d96.txt
```


## [2026-09-06T21:21:07.979Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"##### برگستوان\"; grep -n -i \"from \\|Middle Persian\\|Etymology\" d737443648507f18.txt | head -20\necho; echo \"##### Proto-Iranian kušti\"; grep -n -i \"kuši\\|kušti\\|Descend\\|Persian\" 50583c67b7641e59.txt | head -20\necho; echo \"##### کتلت\"; grep -n -i \"French\\|Etymology\\|Borrow\" 0dce9104c0df76e9.txt | head -20\necho; echo \"##### côtelette\"; grep -n -i \"diminutive\\|côte\\|Etymology\" c038084345c76c49.txt | head -20\necho; echo \"##### Avestan srira\"; grep -n -i \"Etymology\\|Proto-Iranian\\|Sanskrit\\|beautiful\" 053bbb95e1034d96.txt | head -20"
}
```


### [2026-09-06T21:21:08.069Z] TOOL RESULT

```
##### برگستوان

##### Proto-Iranian kušti

##### کتلت

##### côtelette
4:TITLE: côtelette - Wiktionary, the free dictionary
6:côtelette - Wiktionary, the free dictionary 
62: Etymology 
82: Etymology 
89: côtelette 
171: Etymology
174: Etymology tree
197: French côtelette 
199: From Middle French costelette ( “ little rib ” ) , a diminutive of Old French coste ( “ rib, side ” ) , from Latin costa .
206: Audio ; “ une côtelette ” : ( file ) 
219: côtelette   f ( plural côtelettes ) 
267: “ côtelette ”, in Trésor de la langue française informatisé [ Digitized Treasury of the French Language ], 2012 
272: Etymology
275: From Middle French costelette ( “ little rib ” ) , a diminutive of Old French coste ( “ rib, side ” ) , from Latin costa .
280: côtelette   f ( plural côtelettes ) 
284: Retrieved from " https://en.wiktionary.org/w/index.php?title=côtelette&oldid=89783067 "
311: Pages with etymology trees 
312: French entries with etymology trees 
344: côtelette 

##### Avestan srira
```


## [2026-09-06T21:21:13.785Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in d737443648507f18 50583c67b7641e59 0dce9104c0df76e9 053bbb95e1034d96 b8dc9e393c675d5f; do echo \"### $f $(wc -c <$f.txt)\"; head -30 $f.txt | tr '\\n' ' ' | cut -c1-400; echo; done"
}
```


### [2026-09-06T21:21:15.735Z] TOOL RESULT

```
### d737443648507f18 174
URL: https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DA%AF%D8%B3%D8%AA%D9%88%D8%A7%D9%86 FETCHED: 2026-09-06T21:20:58Z STATUS: -1 TITLE:   FETCH FAILED: HTTP Error 404: Not Found

### 50583c67b7641e59 165
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/ku%C5%A1ti FETCHED: 2026-09-06T21:20:58Z STATUS: -1 TITLE:   FETCH FAILED: HTTP Error 404: Not Found

### 0dce9104c0df76e9 150
URL: https://en.wiktionary.org/wiki/%D9%83%D8%AA%D9%84%D8%AA FETCHED: 2026-09-06T21:20:59Z STATUS: -1 TITLE:   FETCH FAILED: HTTP Error 404: Not Found

### 053bbb95e1034d96 186
URL: https://en.wiktionary.org/wiki/%F0%90%AC%99%F0%90%AC%AD%F0%90%AC%8D%F0%90%AC%AD%F0%90%AC%80 FETCHED: 2026-09-06T21:21:01Z STATUS: -1 TITLE:   FETCH FAILED: HTTP Error 404: Not Found

### b8dc9e393c675d5f 150
URL: https://en.wiktionary.org/wiki/%DA%A9%D8%B3%D8%AA%DB%8C FETCHED: 2026-09-06T21:20:03Z STATUS: -1 TITLE:   FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T21:21:24.317Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nhead -3 data/verification/sources/web/b157d86b115b4b36.txt\ngrep -n -i \"Middle Persian\\|Proto-Iranian\\|Etymology\" data/verification/sources/web/b157d86b115b4b36.txt | head -20\necho \"=== retry katlet ===\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%DA%A9%D8%AA%D9%84%D8%AA\" --note \"page 275 Persian katlet\" 2>&1 | tail -1"
}
```


### [2026-09-06T21:21:26.720Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%A7%D9%85%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-06T21:20:03Z
STATUS: 200
62: Etymology 
134: Etymology
137: Etymology tree
212: Pages with etymology trees 
213: Persian entries with etymology trees 
214: Persian entries with etymology texts 
=== retry katlet ===
/home/sfmqrb/git/rishe/data/verification/sources/web/7b1af2fdb120c0a3.txt
```


## [2026-09-06T21:21:29.602Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '130,175p' b157d86b115b4b36.txt\necho \"##### katlet\"; grep -n -i \"French\\|Etymology\\|Borrow\\|cutlet\" 7b1af2fdb120c0a3.txt | head -20"
}
```


### [2026-09-06T21:21:29.659Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *k⁽ʷ⁾rḗmH-ti ~ *k⁽ʷ⁾rémH-n̥ti ? 
 Proto-Indo-Iranian *krā́mHti 
 Persian خرامیدن 

 Inherited from Proto-Indo-Iranian *krā́mHti .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xa.raː.miː.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [xä.ɾɑː.miː.d̪än] 

 ( Dari, formal ) IPA ( key ) : [xä.ɾɑː.miː.d̪än] 
 ( Kabuli ) IPA ( key ) : [xä.ɾɑː.miː.d̪än] 

 ( Hazaragi ) IPA ( key ) : [xä.ɾɔː.mi.d̪än] 

 ( Iran, formal ) IPA ( key ) : [xæ.ɹɒː.miː.d̪æn] 

 ( Tajik, formal ) IPA ( key ) : [χä.ɾɔ.mi.d̪än] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 xarāmīdan

 Dari reading ? 

 xarāmīdan

 Iranian reading ? 

 xarâmidan
##### katlet
62: Etymology 
139: Etymology
142: From French côtelette (“cutlet”).
185: cutlet 
191: Categories : Persian terms derived from French
```


## [2026-09-06T21:21:36.635Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=1379 && /\\[pdf page/{n=NR;p=$0} END{print n\": \"p}' incoming/FFD/FFD_pages.txt\nsed -n '1370,1390p' incoming/FFD/FFD_pages.txt\necho \"=== KNT old persian xram / kust ===\"\ngrep -n -i \"xram\\|kust\" KNT.txt | head"
}
```


### [2026-09-06T21:21:38.841Z] TOOL RESULT

```
1375: [pdf page 55]
خیز + فارسی میانه 82 < ایرانی باستان 8۵12-2*. برای 2 > آرای.

خاییدن
«خایید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خای چ ایرانی باستان 304-2 برای 3 > آرای. ريشةٌ 40 به معنی «جویدنُ» است.
[pdf page 55]
وا فعلهای فارسی دری
خرامیدن
«خرامید» ماد ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
: «خرام» < فارسی میانه 337370 < ایرانی باستان 3+737-8*. برای ۵ > آرای. 3
پیشوند فعلی است. ۳370 صورت بالاندةٌ ريشهٌ 77870 است و 77870(«گامبرداشتن» معنی
می‌دهد.
خریدن
خرید < فارسی میانه 7770 < ایرانی باستان 3۳7-1۵*. برای 14 -> آراست. 77 صورت
ضعیف 727 است و آن به معنی «خریدن» است.
خر + فارسی‌میانةٌ مانوی 37. 77 در فارسی‌میانهٌ مانوی و «خر» در فارسی دری‌به این
سبب به وجود آمده‌اند که تصور شده «خرید» مادهٌ ماضی جعلی است و با حذف ۲4مادة
مضارع به وجود می آید. مادةٌ مضارع 3374 در فارسی میانه 778 است» از ایرانی باستان
8 83 نشاته‌ای بوده که برای ساختن ماده مضارع از ريشه به کار می‌رفته است ->
بریدن,
خزیدن
=== KNT old persian xram / kust ===
```


## [2026-09-06T21:21:49.118Z] TOOL CALL #55: Bash

```json
{
 "command": "pdftoppm -f 275 -l 275 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg275 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T21:21:52.499Z] TOOL RESULT

```
total 23036
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:21 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     396 Sep  6 17:19 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb   97300 Sep  6 17:16 build270.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb  157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65729 Sep  6 17:10 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44171 Sep  6 17:16 pg277.png
```


## [2026-09-06T21:21:57.138Z] TOOL CALL #56: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg275.png"
}
```


### [2026-09-06T21:21:57.643Z] TOOL RESULT

```

```


## [2026-09-06T21:21:57.639Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T21:22:12.692Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg275.png')\nprint(im.size)\nim.crop((1350,2250,2000,2530)).resize((1300,560)).save('p275_krei_empty.png')\nim.crop((520,480,1000,800)).resize((1440,960)).save('p275_pahlavi.png')\n\"\nls -la p275_krei_empty.png p275_pahlavi.png"
}
```


### [2026-09-06T21:22:15.091Z] TOOL RESULT

```
(2550, 3300)
-rw-rw-r-- 1 sfmqrb sfmqrb  5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb 53703 Sep  6 17:22 p275_pahlavi.png
```


## [2026-09-06T21:22:17.306Z] TOOL CALL #58: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p275_pahlavi.png"
}
```


### [2026-09-06T21:22:17.334Z] TOOL RESULT

```

```


## [2026-09-06T21:22:22.243Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p275_krei_empty.png"
}
```


### [2026-09-06T21:22:22.260Z] TOOL RESULT

```

```


## [2026-09-06T21:22:32.973Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW costa ===\"; grep -n \"costa\" LEW_1910.txt | head -5\necho \"=== SKT coast/cutlet ===\"; grep -n \"^COAST\\|^CUTLET\\|COAST\\.\\|CUTLET\\.\" SKT.txt | head\ngrep -n -i \"coast,\" SKT.txt | head -3\necho \"=== FSD/WEB coast ===\"; grep -n -i \"L\\. costa\" FSD_vol1.txt | head -3"
}
```


### [2026-09-06T21:22:33.057Z] TOOL RESULT

```
=== LEW costa ===
=== SKT coast/cutlet ===
8122:Guinea.  (African,^  First  coined  (4 African  gold  from  the  Guimea  coast,  aa 1 66 J.  Der.  piinea/tnt)/.  ^  Thtgninet' pig  is  from  ^.  America;  so  that  it  my mean  Guiana  fig.
16143:—  O.  F.  riviere,  (F.  riviire.)  The  same as  Span.  riUra,  a  shore,  strand,  sea  coast, Ital.  riviera,  bfaore,  bank,,  also  a  river; Low  L.  riparia.  (i)  shore, iiank,  (2^  river.
=== FSD/WEB coast ===
```


## [2026-09-06T21:22:35.097Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/kostism\" --note \"page 275 kusti\" 2>&1 | tail -1\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kost-\" --note \"page 275 PIE kost\" 2>&1 | tail -1\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/kost%C4%AB\" --note \"page 275 MP kusti\" 2>&1 | tail -1"
}
```


### [2026-09-06T21:22:41.708Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b737eb13493dfe9f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1cbc89864f4822f5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a231efd5ad3c3828.txt
```


## [2026-09-06T21:22:44.646Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in b737eb13493dfe9f 1cbc89864f4822f5 a231efd5ad3c3828; do echo \"### $f $(wc -c <$f.txt)\"; sed -n '1,6p' $f.txt; done"
}
```


### [2026-09-06T21:22:47.355Z] TOOL RESULT

```
### b737eb13493dfe9f 141
URL: https://www.iranicaonline.org/articles/kostism
FETCHED: 2026-09-06T21:22:40Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found### 1cbc89864f4822f5 166
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/kost-
FETCHED: 2026-09-06T21:22:41Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found### a231efd5ad3c3828 136
URL: https://en.wiktionary.org/wiki/kost%C4%AB
FETCHED: 2026-09-06T21:22:41Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T21:22:53.819Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '1,6p' 95291d23b7d61b2c.txt\ngrep -n -i \"Proto-Italic\\|de Vaan\\|Old Church Slavonic\\|isolated\\|Etymology\" 95291d23b7d61b2c.txt | head -20"
}
```


### [2026-09-06T21:22:53.870Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/costa#Latin
FETCHED: 2026-09-06T21:20:01Z
STATUS: 200
TITLE: costa - Wiktionary, the free dictionary

costa - Wiktionary, the free dictionary 
62: Etymology 
97: Etymology 1 
103: Etymology 2 
120: Etymology 
140: Etymology 1 
152: Etymology 2 
158: Etymology 3 
172: Etymology 
195: Etymology 1 
207: Etymology 2 
232: Etymology 
264: Etymology 
290: Etymology 
313: Etymology 1 
325: Etymology 2 
339: Etymology 1 
354: Etymology 2 
481: Etymology
558: Etymology 1
570: Etymology 2
```


## [2026-09-06T21:22:56.321Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk 'NR>=470 && NR<=520' 95291d23b7d61b2c.txt | head -50"
}
```


### [2026-09-06T21:22:57.824Z] TOOL RESULT

```
 From Wiktionary, the free dictionary

 See also: Costa , cósta , costá , costà , costâ , and cô ta 

 English
 [ edit ] 

 English Wikipedia has an article on: costa 

 Wikipedia 

 Etymology
 [ edit ] 

 Unadapted borrowing from Latin costa ( “ a rib ” ) . Doublet of coast .

 Pronunciation
 [ edit ] 

 ( Received Pronunciation ) IPA ( key ) : /ˈkɒ.stə/ 
 Audio ( Southern England ) : ( file ) 

 ( General American ) IPA ( key ) : /ˈkɑ.stə/ 

 Rhymes: -ɒstə 

 Noun
 [ edit ] 

 costa ( plural costas or costae ) 

 ( anatomy ) Synonym of rib .

 ( botany , zootomy ) A riblike part of a plant or animal , such as a midrib of a leaf or a thickened vein or the margin of an insect wing .
 ( entomology ) The vein forming the leading edge of most insect wings .
 Synonym: C 

 Derived terms
 [ edit ] 

 basicosta 
 costapalmate 
 costiferous 
 costiform 
 costovertebral 
 subcosta 

 Related terms
 [ edit ]
```


## [2026-09-06T21:23:01.032Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n \"Latin$\" 95291d23b7d61b2c.txt | head\nawk '/^ Latin$/{f=NR} END{}' 95291d23b7d61b2c.txt\ngrep -n -A20 \"^ Latin *$\" 95291d23b7d61b2c.txt | sed -n '1,60p'"
}
```


### [2026-09-06T21:23:03.083Z] TOOL RESULT

```
1:URL: https://en.wiktionary.org/wiki/costa#Latin
918: Latin
227: Latin 
228-
229- Toggle Latin subsection 
230-
231- 8.1 
232- Etymology 
233-
234- 8.2 
235- Pronunciation 
236-
237- 8.3 
238- Noun 
239-
240- 8.3.1 
241- Inflection 
242-
243- 8.3.2 
244- Derived terms 
245-
246- 8.3.3 
247- Descendants 
--
918: Latin
919- [ edit ] 
920-
921- Etymology
922- [ edit ] 
923-
924- Of uncertain origin. The term is traditionally compared with Old Church Slavonic кость ( kostĭ ) . [ 1 ] For instance, Derksen considers their kinship to be "quite possible." [ 2 ] However, the connection is complicated if the Proto-Slavic term is derived from a pre-form *Host- , as such a term would not produce the Latin word. For this reason, De Vaan rejects the connection between the Slavic and Latin terms. [ 3 ] 
925-
926- Pronunciation
927- [ edit ] 
928-
929- ( Classical Latin ) IPA ( key ) : [ˈkɔs.ta] 
930-
931- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈkɔs.ta] 
932-
933- Noun
934- [ edit ] 
935-
936- costa   f ( genitive costae ) ; first declension 
937-
938- ( anatomy ) a rib
```


## [2026-09-06T21:23:12.958Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80\" --note \"page 275 Sanskrit sri, Krei root\" 2>&1 | tail -1\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%A4%E0%A4%BF\" --note \"page 275 Sanskrit kramati\" 2>&1 | tail -1"
}
```


### [2026-09-06T21:23:15.497Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4700a71bbaff5e2d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/80ffe871f7bb589d.txt
```


## [2026-09-06T21:23:19.005Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### sri\"; grep -n -i \"Proto-Indo-Iranian\\|Avestan\\|Proto-Indo-European\\|beauty\" 4700a71bbaff5e2d.txt | head -12\necho \"### kramati\"; sed -n '1,5p' 80ffe871f7bb589d.txt; grep -n -i \"Proto-Indo\\|Avestan\\|Etymology\\|stride\" 80ffe871f7bb589d.txt | head -12"
}
```


### [2026-09-06T21:23:19.063Z] TOOL RESULT

```
### sri
273: light , lustre , radiance , splendour , glory , beauty , grace , loveliness 
476: Proto-Indo-European *ḱreyH- der. ? 
477: Proto-Indo-Iranian *ćriHrás 
481: Inherited from Proto-Indo-Aryan *śriHrás with apocopation , from Proto-Indo-Iranian *ćriHrás . Compare Avestan 𐬯𐬭𐬍𐬭𐬀 ( srīra ) . Doublet of श्रील ( śrīlá ) and श्रीर ( śrīrá ) 
488: light , lustre , radiance , splendour , glory , beauty , grace , loveliness 
926: From Proto-Indo-European *ḱerh₂- ( “ to mix ” ) . Cognate with Ancient Greek κεράννυμι ( keránnumi , “ mix, blend ” ) , κρᾱτήρ ( krātḗr , “ mixing bowl, cup-shaped basin; crater ” ) ; English rear . 
954: Mallory, J. P. with Adams, D. Q. ( 2006 ), The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World (Oxford Linguistics), New York: Oxford University Press, →ISBN , pages 258, 259 
1001: Sanskrit terms derived from Proto-Indo-Iranian 
1003: Sanskrit terms derived from Proto-Indo-European 
1005: Sanskrit terms inherited from Proto-Indo-Iranian 
1018: Sanskrit terms inherited from Proto-Indo-European 
### kramati
URL: https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%A4%E0%A4%BF
FETCHED: 2026-09-06T21:23:15Z
STATUS: -1
TITLE:
```


## [2026-09-06T21:24:17.812Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 27205 27321 27334; do echo \"--- line $L leaf:\"; awk -v L=$L 'BEGIN{RS=\"\\f\"} {n+=gsub(/\\n/,\"\\n\")+0} ' /dev/null; done\nawk 'BEGIN{RS=\"\\f\"} /sraeSta-Adj|srae5ta-Adj/{print \"sraesta leaf(1-based)=\"NR}' BRT.txt\nawk 'BEGIN{RS=\"\\f\"} /srayan-  n\\.  .Schönheit|srayan-  n\\./{print \"srayan leaf=\"NR}' BRT.txt\nawk 'BEGIN{RS=\"\\f\"} /srayah-  Adj/{print \"srayah leaf=\"NR}' BRT.txt\necho \"=== numbers on that leaf ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==880 || NR==881 {print \"### leaf \"NR; print substr($0,1,200)}' BRT.txt"
}
```


### [2026-09-06T21:24:19.821Z] TOOL RESULT

```
--- line 27205 leaf:
--- line 27321 leaf:
--- line 27334 leaf:
sraesta leaf(1-based)=890
srayan leaf=894
srayah leaf=894
=== numbers on that leaf ===
### leaf 880
 die  Hds.,  beion- ders  L4  und  K  1  bieten  oft  h,  S.  an  lunT-.  — >)  Theio.  —  3)  Es  handelt  sieb  nm  das SagäJd;  s.  Gaa.  OK.  264,  Dst,  ZA.  ».  XL  — A)  Ober  Züchtung
### leaf 881
sein'. Praes.  3  sp^nza-.
mit  Inf:  y!  ,  .  dtmanakya  xh'i-rsm  .  . asil /rada>iJi  (sd.)  aspir?zai3  Y.^^/.  16. aL  vgl.  sffhäyati   'er   begehrt    eifrig  nach  -' (Dat.),  mp.  apl  spu
```


## [2026-09-06T21:24:26.373Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==890 || NR==894 {print \"### leaf \"NR; print $0}' BRT.txt | grep -oE \"\\b1[6-8][0-9][0-9]\\b\" | sort -u | head -20"
}
```


### [2026-09-06T21:24:28.136Z] TOOL RESULT

```
1607
1640
```


## [2026-09-06T21:24:34.729Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} NR==473{print $0}' WLD_Bd1_pages.txt | grep -n -i \"kost\\|costa\" | head\necho \"=== p478 krei ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==487{print $0}' WLD_Bd1_pages.txt | grep -n -i \"sriras\\|srira\\|sraesta\\|kreion\\|sr[il]-\" | head"
}
```


### [2026-09-06T21:24:37.114Z] TOOL RESULT

```
65:   Lat. costa          „Rippe“; abg. hosts „Knochen“                            (skr. host     „Rippe“).        S. Yf.
=== p478 krei ===
```


## [2026-09-06T21:24:43.484Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"sriras\\|srlras\\|sraesta\\|sra§sta\\|sraë\" WLD_Bd1_pages.txt | head\ngrep -n \"kreion\\|xpsuov\\|Kpsiwv\" WLD_Bd1_pages.txt | head\nawk 'BEGIN{RS=\"\\f\"} NR>=485 && NR<=490 {print \"### leaf \"NR; print substr($0,1,300)}' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T21:24:45.226Z] TOOL RESULT

```
### leaf 485
                                                   i




476                                                      kueig^h-         — qneug-
                                     lat. Worten kann (vgl. Yf. LEWb.
                                                                      2
  Yon den       
### leaf 486
                                                qra*n-, qru-   — krapo-                                    477

qra x u-, qru- „aufeinander, auf einen Haufen legen, zudecken, verbergen“
      (Beziehung zu sqer-, sqeren- „drehcn“ als „dariiber wolben“ ist nicbt
          zu stutzen).
 
### leaf 487
478                                                krabh-     — qreu-, qreua-

flechtr             als      ursprgl. Bed. (Pick III 4 106. Falk-Torp u. ruf I)                                      ware an sich
ganz fraglich und ist, da                          (s)ge>--   ,   drehen, flcchten'' Vela
### leaf 488
                                                                                                                                                 :,




                                                          krabh-        — qreu-, qreua-                                                       479

### leaf 489
                                                                                       ;




480                                                                                   qreu-


andrerseits                         „gerinnen“        — gefrieren, Eisscholle“ ein sehr einfacher Be-
   
### leaf 490
                                       qreut        qreup-                                       481


vom Pferde", (^xqovociv^w, Bechtel Lex. 205, der -oy- aus -ova- ablehnt,
legt die kiirzere Wzf. qreu- zugrunde), xooiog „abgebrochen, von Bausteinen,
denen ein Stuck abgeschlagen ist" ( *xqovoios
```


## [2026-09-06T21:24:49.713Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} NR==487 || NR==488 {print}' WLD_Bd1_pages.txt | grep -n -i \"krei\\|schön\\|sri\\|Schon\" | head -20"
}
```


### [2026-09-06T21:24:51.427Z] TOOL RESULT

```
33:krei- etwa „hervorleuchten, sich hervortun‘\
34:      Ai. Crt-               f.   j.Schonbeit, Pracht, Zierde, Wohlgefallen, Wohlfahrt, Reich-
36:tum, Herrlichkeit, MajestaV, av. srt- ,,Schonbeit \ ai. crJ-ld- „schon, herrlich“,
37:u-crtra- ,,unschon“, av. .‘trim- „schon“, Komp. ai. creyas-, av. era yak-, Sup.
39:av. sruyun- n. ..Schonheit"', Adj. .,sehon‘, ai. c riyase Dat. n. „sch6n“.                                                               Horn,
```


## [2026-09-06T21:25:21.259Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC kost ===\"; grep -n -i \"^kost\\|kostis\\|kostā\" IEC.txt | head -5\necho \"=== IEC krei/sri ===\"; grep -n \"^k̑rei\\|^krei-\\|^k̑rī\" IEC.txt | head -5\necho \"=== SOD xram ===\"; grep -n -i \"xr’m\\|xram\" SOD.txt SOD_pages.txt 2>/dev/null | head -5\nmkdir -p ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg275.png ocr/BOOK/275.png && ls -la ocr/BOOK/275.png"
}
```


### [2026-09-06T21:25:23.253Z] TOOL RESULT

```
=== IEC kost ===
7739:kostos, à, is (combings, fibre, grass, tress, bristle’. Cf. kes-, kos-, koso Gk. kóstos 'prickly-leaved spice-plant, burr or thistle’; kostai, pl. ʻa barbed fish'?); cf. Hes. kóstai, fpl. “barley? beside Gk. akosté, id.; kósta, npl. (perh. "linchpins"); Alb. kashtë ‘straw’; Ir. cuise ‘meadow-grass’; ON haddr ‘tress’ beside (e-gde) OE heorde ‘hards of flax’; Pol. cf. kost-rzewa ‘fescue’; Blg. koSC- riàva «timothy-grass'; Cz. cf. kostrbaty 'shag- gy’; koště, n. ‘broom for sweeping’; Li. cf. kastuvas ‘currycomb’. (LW in Lat. costus, costum ‘amōmum hirsutum, zedoary’, fr. Gk.). Here also prob. W. Cor. cos, f. ‘itch’
7740:kosthios, (kost-) (?) ‘wood, stem, base, leg, bone”. Cf. WP I, 456 & 464 Skt. (alleged) kasthah (^wood, timber’: Hind. kath, Romani kast, id.); Hes. (Epirot? Illy- rian?) káston, n. id. (Athamantes — Hes.); Ir. cos, f. “leg, foot, stem, trunk'; OCS kosti, f. Cbone’ and com. Sl.)
7745:kostos, a, is — krab-
8756:Kostos ‘disciplined’, etc. See Kes-mi and Kéns-mi Skt. Sistah Ceducated etc.); Lat. castus (1) ‘chaste, pure’; Alb. cf. archaic pp. tháshun ‘said’
9731:bright; brightness', etc. Cf. louk-, luk-, etc. WP II, 408-411 Arm. (vowel ambig.) lusat ‘illumination’; Osc. in Lat. Loucetius (epithet of Jove); Gaul. leucetio-, loucetio- (in names); W Hugas, f. (*daybreak, fr. *leukostis or *loukost-) beside llugaint, m. (Cglitter', from a type *leukonti-, *louk-); Go. liuhap, n. “light; OHG lioht, OE leoht, id. Cf. Hitt. lukkitti, a. adv. ‘next day, tomorrow”
=== IEC krei/sri ===
=== SOD xram ===
SOD.txt:21038:oxramande 
SOD.txt:35193:xram    ©<Skt.  kram 
SOD_pages.txt:9670:                oxramande
SOD_pages.txt:15647:     xram      ©<Skt. kram                                            4186 yr'nsn'y       B
-rw-rw-r-- 1 sfmqrb sfmqrb 80338 Sep  6 17:25 ocr/BOOK/275.png
```


## [2026-09-06T21:25:31.347Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15640,15655p' SOD_pages.txt\nawk 'NR<=15647 && /\\[pdf page/{n=NR;p=$0} END{print n\": \"p}' SOD_pages.txt\nsed -n '9665,9675p' SOD_pages.txt"
}
```


### [2026-09-06T21:25:34.025Z] TOOL RESULT

```
                                                                      4185 yr'ns-     B
                                                                                                                              i^jjJ^^i^f-
      SCE 446v Benv. Notesiv 515                                            Yrans
                                                                            (to)gct ©mcd.
                                                                                    angry pass. =*yr'nd-
4173 yrW       M -» yrS'k                                                   BBB 644; Frag. 2a.l0
4174 yr'm-      B, S                      O"^*' j*~ i0*£ *— *$ _>*-
     xram      ©<Skt. kram                                            4186 yr'nsn'y       B
                                                                           yransne        ©pres. part,             IjU i^jL-^aC- <
      OcOmove, Uo)go
                                                                            annoyed, angry, irritable
      VJ 849, 951, 1388, 1430; Hen. Tales. 476, 12, 13,                     GMS 893; SCE 407
        18
                                                                      4187 yr'ns B
4175 yr'm'k     B, S                   (j>> >^ j-OJ* «^j>                  yrans ©<*gran0iya ? Khot. grantha; Bal.
      yrame (yr'nVy, yr}myy)         ©<Av. grzhma-, Parth.                                                   ((?&)* J *
: 
                oxar ©impf. wyxr =»}wyr-                                       Sund. MSP p42,b!67
                (ro)leave, (to)abandon
                STii 5.16; STSC 45; S W, C2 gloss, n p72                  2045 >wx(y)    M                             J><jy£*J«
                                                                               ux(e) ®<*axu; Av. a(r\)hu =>cn}wxy, s'twx
           2036 Nvxr'mnty C                               ^     ,S j           heart, mind
                oxramande




 mm
```


## [2026-09-06T21:26:25.172Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خرامیدن:\" MON_part1.txt MON_part2.txt | head -5\ngrep -n \"خرام:\" MON_part1.txt MON_part2.txt | head -5\ngrep -n \"خرامان:\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T21:26:25.266Z] TOOL RESULT

```
MON_part1.txt:55802:خرامیدن: 0۲0-7 [هند ] (مص‌ل.) 
MON_part2.txt:20154:کبک خرام: صجمجطام1 .. [- 
MON_part2.txt:49624:محشرخرام: [ع. ف.] (ص‌مر.) 
MON_part1.txt:55793:خرام: -۲6 و0۲5۲ (.) رفتار آهسته از روی 
MON_part1.txt:91959:غلمان. طاوس مشرق‌خرام: (کت.) آفتاب؛ 
MON_part1.txt:55800:خرامان: 20۲500-7 (ص‌فا.) رونده با ناز و 
MON_part1.txt:77508:جبلی. سرو خرامان: (کد.) معشوق خوش قد
```


## [2026-09-06T21:26:27.756Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '55793,55810p' MON_part1.txt"
}
```


### [2026-09-06T21:26:27.805Z] TOOL RESULT

```
خرام: -۲6 و0۲5۲ (.) رفتار آهسته از روی 
ناز» سرکشی» زیبایی و وقار. وفای به وعد؛ 
مت. نوید. به مهمانی بردن شخصی پس از 
نوید. کسی که مأمور همراهی مهمان به خانة 
میزبان است. (افا.) در ترکیب به معنی 
رخرامنده) آید: خوش خرام. 

خرامان: 20۲500-7 (ص‌فا.) رونده با ناز و 
تکبر و تبختر. (حا.) در حال خرامیدن. 
خرامیدن: 0۲0-7 [هند ] (مص‌ل.) 
(خرامید» خرامد؛ خواهد خرامید» بخرام» 
خرامنده» خرامان» خرامیده) راه رفتن از 


روی نازه تکبر» زیبایی و وقار. 
خراید: 0( [غ. خرائد] (ا.) ج. 
خریده. لوّلوُهای ناسفته. دوشیزگان» تا 
شرمگین.
```


## [2026-09-06T21:26:32.593Z] AGENT

Now I have everything I need. Writing the verification file.


## [2026-09-06T21:36:00.677Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build275.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nS_COSTA = W + \"costa#Latin\"\nS_COAST = \"https://www.etymonline.com/word/coast\"\nS_CUTLET = \"https://www.etymonline.com/word/cutlet\"\nS_KOSHTI = W + \"%DA%A9%D8%B4%D8%AA%DB%8C\"\nS_XARAM = W + \"%D8%AE%D8%B1%D8%A7%D9%85%DB%8C%D8%AF%D9%86\"\nS_COTEL = W + \"c%C3%B4telette\"\nS_KATLET = W + \"%DA%A9%D8%AA%D9%84%D8%AA\"\nS_SRI = W + \"%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80\"\n\ndata = {\n \"pdf_page\": 275,\n \"book_page\": 245,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0 Kost\ne0 = {\n \"entry\": 0,\n \"root\": \"Kost\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *kost- 'bone' (Pokorny 616 kost- 'leg; bone'; Watkins/AHD 'kost-. Bone. Probably related to ost-'), attested only in Latin costa 'rib' and Slavic *kostь 'bone'\",\n \"note\": \"The root box itself is real: Pokorny p. 616 has 'kost- : leg; bone' with exactly two witnesses, Lat. costa 'rib' and OCS kostь 'bone' (WP. I 464, WH. I 281), and Watkins lists 'kost-. Bone.' with Lat. costa. Two caveats. (1) The chart's own note ('AHD claims that this may be related to the root Ost:bone') is Watkins's 'probably related to ost-', but Pokorny on the same page calls it flatly untenable ('assumption of a k- prefix (to Latin os etc.) is incredible'); Buck 4.16 s6 calls the k-ost- analysis 'attractive but dub.'; Ernout-Meillet accept it after Meillet; Wiktionary reports that de Vaan rejects the Latin-Slavic equation altogether, leaving costa, in Etymonline's summary, 'an isolated word without etymology'. (2) No Iranian or Indic form belongs to this root in any Indo-Europeanist source: Pokorny, Walde-Pokorny, Watkins, Mann and Buck all list only Latin + Slavic (+ possibly Alb. kockë, Ir. cos). The whole Pahlavi/Persian branch of this chart comes from Mo'in's footnote in Borhan-e Qate' (BQT 1643 n.1), not from the IE literature, and Nourai's other cited authority for it, Horn (= AEF), explicitly denies it. The gloss 'side of anything' is a Latin/Romance semantic development (costa 'rib' > 'side' > 'coast'), not a PIE meaning.\",\n \"note_fa\": \"ریشهٔ *kost- در پوکورنی (صـ ۶۱۶) و در فهرست ریشه‌های هندواروپایی واتکینز (AHD) واقعاً وجود دارد، امّا گواهانِ آن تنها دو تاست: لاتینی costa «دنده» و اسلاوی کهن kostь «استخوان»؛ نه در زبان‌های ایرانی و نه در هندی بازماندهٔ مطمئنی ندارد. خودِ پوکورنی تحلیلِ *k- + ost- را — همان که یادداشتِ نمودار از AHD نقل می‌کند — «باورنکردنی» می‌خواند، و دِ‌فان (۲۰۰۸) پیوند لاتینی و اسلاوی را نیز رد می‌کند و costa را واژه‌ای تنها و بی‌ریشه‌شناسی می‌داند. معنیِ «پهلوی هر چیز» تحول معنایی لاتینی-رومانیایی است، نه معنای هندواروپایی آغازین. پس ریشه با احتیاط پذیرفتنی است، ولی شاخهٔ ایرانیِ این نمودار (بندهای ۱ و ۲) از آنِ این ریشه نیست و از حاشیهٔ معین بر برهان قاطع گرفته شده است.\",\n \"sources\": [S_COSTA, S_COAST],\n \"ref_check\": [\n   {\"ref\": \"POK:616\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt L.48137 'Root / lemma: kost- | Meaning: leg; bone | Material: Latin costa \\\"rib\\\"; Old Bulgarian kostь \\\"bone\\\" ... assumption of a k- prefixe (to Latin os etc.) is incredible. References: WP. I 464, WH. I 281. Page(s):616' - the root, the page and the gloss are Nourai's, but Pokorny's material is Latin + Slavic only and he rejects the k-ost- analysis the chart's note repeats.\"},\n   {\"ref\": \"AHD:1524\", \"status\": \"supports\",\n    \"note\": \"Nourai's page is the 1976 AHD appendix (not open online); the same entry in Watkins 1985 (AHD_watkins1985.txt L.644) reads 'kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.]' - root name, gloss, the Ost- remark and the Latin/French/English branch all match; no Iranian.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 464 (WLD_Bd1_pages.txt leaf 473)\", \"stance\": \"supports\",\n    \"note\": \"'Lat. costa \\\"Rippe\\\"; abg. kostь \\\"Knochen\\\"' - Walde-Pokorny I 464, the source Pokorny cites; again only Latin and Slavic.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kost-\", \"stance\": \"supports\", \"note\": \"see ref_check AHD:1524.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.16 BONE s6 and 4.162 RIB s2\", \"stance\": \"partial\",\n    \"note\": \"'ChSl. kostĭ, etc., general Slavic : Lat. costa \\\"rib\\\". Further analysis of both as k-ost-, with relation to IE *ost- ... is attractive but dub.' and 'Lat. costa (> It. costa, Fr. côte, Rum. coastă ...) : ChSl. kostĭ \\\"bone\\\"'. Buck's word for 'rib' in Iranian is Av. parəsu-, not anything kost-like.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. costa (LAT.txt L.14191)\", \"stance\": \"partial\",\n    \"note\": \"'Il n'y a aucun mot identique ailleurs. Mais la forme rappelle celle de v.sl. kostĭ \\\"os\\\", et ce mot lui-même est inséparable du groupe de lat. os, skr. asthi ... Il y aurait donc ici une sorte de préfixe *k- semblable à celui qui figure dans caper, capra' - accepts the k-ost- analysis Pokorny rejects, and knows no cognate outside Latin/Slavic.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. kosthios (kost-) (IEC.txt L.7740)\", \"stance\": \"partial\",\n    \"note\": \"'kosthios, (kost-) (?) \\\"wood, stem, base, leg, bone\\\". Cf. WP I, 456 & 464 ... Ir. cos \\\"leg, foot\\\"; OCS kostĭ \\\"bone\\\" and com. Sl.' - Mann's family has no Latin costa and no Iranian member.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index p. 87-88 (headword استخوان)\", \"stance\": \"partial\",\n    \"note\": \"Aryanpur files Slavic KOST (Russian/Czech/Serbian/Polish/Slovak/Bohemian) under Persian استخوان with Av. asti/ast, Pahl. ast/astag, Skt asthi, Gk osteon, Lat. os - i.e. with *ost-, and lists no Persian کست/کشتی anywhere in the family.\"},\n   {\"src\": \"Wiktionary/de Vaan\", \"where\": \"en.wiktionary 'costa' (Latin) / Etymonline 'coast'\", \"stance\": \"contradicts\",\n    \"note\": \"'Of uncertain origin. The term is traditionally compared with Old Church Slavonic кость ... For this reason, De Vaan rejects the connection between the Slavic and Latin terms'; Etymonline: 'de Vaan dismisses this and calls it \\\"an isolated word without etymology\\\"'.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"kost; uparô-kušta-pâma\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Pahlavi word is real: MacKenzie 51 '1kust [kwst'] side, direction; district' (also kustag, kustīg 'sacred girdle'), Nyberg II 138 'kust [kwst'] side, direction; region, district ... Paz. kūst, cf. MPrt kws \\\"country\\\"; Arm. lw. kołs \\\"side\\\"'. The second entry is not a Pahlavi word at all but Horn's reconstruction: Horn no. 205 (Grundriss p. 48) explains NP bergustuwān 'Panzer, Pferdepanzer' as 'Etwa *uparō-kustapāna-; phlv. vergl. kustak \\\"Seite\\\". Vergl. np. kust (No. 854)', i.e. Old Iranian upari- 'over, above' + kusta- 'side' + pāna- 'protection' (Nourai's own cross-references, Upo and Pa, show this is what he means). What is NOT supportable is the arrow from PIE *kost-. It comes from Mo'in's footnote at BQT 1643 n.1: 'کلمهٔ مزبور از مادهٔ kust ... است که در پهلوی بمعنی طرف، سوی، جانب است ... چنانکه در لاتینی costa و در انگلیسی coast و در ایتالیایی costa و در فرانسوی côte از همین ماده است'. Horn - whom Nourai cites here as AEF:261, the Persian translation of the Grundriss - says the exact opposite in the footnote to no. 854: 'Aber nicht gehört dazu lat. costa \\\"Rippe\\\"' ('but Latin costa \\\"rib\\\" does not belong here'). Modern Iranian etymology (Edelman, ESIJa IV 411-2, followed by Wiktionary) derives the family from Proto-Iranian *kušti-, a t-extension of *kuši- 'side (of the body)', from PIE *kuḱis / *kew-k-, cognate with Skt kukṣi- 'belly, womb' and Lith. kūšỹs - a different root from *kost-. Sound-wise too the equation is poor: PIE *o gives Iranian a, so *kost- would yield Ir. *kast-, not kust-.\",\n \"derivation_fa\": \"واژهٔ پهلوی درست است: مکنزی (ص ۵۱) kust [kwst'] «طرف، سوی، ناحیه» و نیبرگ (جلد ۲، ص ۱۳۸) همین را می‌آورد، با وام‌واژهٔ ارمنی kołs «پهلو». امّا صورت دوم واژهٔ پهلوی نیست؛ بازسازیِ هرن است: هرن در بند ۲۰۵ (ص ۴۸) «برگستوان» را تقریباً *uparō-kustapāna- می‌داند، یعنی upari- «بر، بالا» + kusta- «پهلو» + pāna- «نگاهداری، پاسبانی». امّا پیوند با ریشهٔ هندواروپایی *kost- پذیرفتنی نیست: این ادّعا از حاشیهٔ معین بر برهان قاطع (ص ۱۶۴۳، پاورقی ۱) گرفته شده که می‌گوید «چنانکه در لاتینی costa و در انگلیسی coast ... از همین ماده است»، در حالی که هرن — همان کتابی که نورایی در همین بند به ترجمهٔ فارسی‌اش (اسفا، ص ۲۶۱) ارجاع می‌دهد — در پاورقی بند ۸۵۴ صریحاً می‌نویسد: «ولی لاتینی costa به این خانواده تعلق ندارد». ریشه‌شناسی امروزی (ادلمان، فرهنگ ریشه‌شناختی زبان‌های ایرانی ۴: ۴۱۱–۴۱۲) این خانواده را از ایرانی آغازین *kušti- (گسترش‌یافتهٔ *kuši- «پهلوی تن») می‌گیرد، هم‌ریشه با سنسکریت kukṣi- «شکم». از نظر آوایی نیز *o هندواروپایی در ایرانی به a بدل می‌شود، پس *kost- باید *kast- می‌داد نه kust-. پژوهش امروزی ادّعای نورایی را رد می‌کند. افزون بر این، صورت چاپیِ کتاب (uparô-kušta-pâma) غلط چاپی است به جای *uparō-kusta-pāna-.\",\n \"error_in\": \"book\",\n \"book_prints\": \"uparô-kušta-pâma\",\n \"correct_form\": \"*uparō-kusta-pāna-\",\n \"sources\": [S_KOSHTI, S_COSTA],\n \"ref_check\": [\n   {\"ref\": \"BQT:1643\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' vol. 3 p. 1643 (BQT_v3_pages.txt pdf page 436), Mo'in's footnote 1 s.v. کستی: 'کستی = کشتی. از پهلوی kustīk است ... کلمهٔ مزبور از مادهٔ kust است که در پهلوی بمعنی طرف، سوی، جانب است ... چنانکه در لاتینی costa و در انگلیسی coast و در ایتالیایی costa و در فرانسوی côte از همین ماده است'. This footnote IS Nourai's chart - root, Pahlavi kust, Latin costa, English coast, Persian belt and wrestling all together.\"},\n   {\"ref\": \"AEF:261\", \"status\": \"contradicts\",\n    \"note\": \"AEF = Khaleqi-Motlaq's Persian translation of Horn's Grundriss; the corresponding place is Horn no. 854 (p. 191-192, HRN.txt L.7446): 'kust \\\"Seite, Flanke\\\", kustī \\\"Gürtel\\\", vergl. bergustvuan (No. 205); kuštīgīr \\\"Ringkämpfer\\\" ... phlv. kust, kustak \\\"Seite\\\", kustīk', with the footnote 'Aber nicht gehört dazu lat. costa \\\"Rippe\\\"' - Horn admits the Persian family but expressly excludes Latin costa from it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 51 (PHD.txt L.430)\", \"stance\": \"supports\",\n    \"note\": \"'1kust [kwstʹ] side, direction; district. ... kustag [kwstkʹ | M kwstg] = 1kust. ... kustig [kwstykʹ | N ~i] sacred girdle' - the Pahlavi word and its girdle derivative are exactly as drawn; MacKenzie gives no PIE etymology. (His 2kust [kwstʹ | Ar. qust] 'costus' is an unrelated Arabic plant name.)\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II 138 (NYB_vol2_glossary.txt L.2355-2357)\", \"stance\": \"supports\",\n    \"note\": \"'kust [kwstʹ] side, direction; region, district ... Paz. kūst, cf MPrt kws \\\"country, countryside\\\"; Arm. lw. kołs \\\"side\\\", kust \\\"the waist, the belly\\\" = NP kust'; 'kustik [kwstyk] the sacred thread worn by the Zoroastrians (tied round the waist)'. Nyberg's comparanda are Parthian and Armenian, never Latin.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 854, p. 191-192 + footnote\", \"stance\": \"contradicts\",\n    \"note\": \"see ref_check AEF:261 - 'Aber nicht gehört dazu lat. costa \\\"Rippe\\\"'.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn no. 205, p. 48\", \"stance\": \"supports\",\n    \"note\": \"'205. bergustuwān \\\"Panzer, Pferdepanzer\\\". Etwa *uparō-kustapāna-; phlv. vergl. kustak \\\"Seite\\\". Vergl. np. kust (No. 854)' - this is the source of Nourai's second entry, and shows the third element is pāna- 'protection', not '-pâma'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon\", \"stance\": \"silent\",\n    \"note\": \"grep 'kust' in KNT.txt: no hit; the word is not Old Persian.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"kostî «کستی»; košti «کشتی»; bargostovân «برگستوان»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Within Iranian the three words do belong together and do come from MP kust 'side'. (1) کستی kustī, the Zoroastrian sacred girdle, continues MP kustīg [kwstykʹ] (MacKenzie 51; Nyberg II 138 kustīk 'the sacred thread worn by the Zoroastrians, tied round the waist'), an -īg adjective/possessive of kust 'side, waist'; Arabic borrowed it as کستیج kustīj (already in BQT 1643 'و معرب آن کستیج است'), Syriac as qwsty. (2) کشتی koštī 'wrestling' is the same word: Mo'in, BQT 1643 n.1, 'لغت کشتی (مصارعه) نیز از همین ریشه است. بنابرین کشتی گرفتن عبارتست از مصارعهٔ دو تن با گرفتن کستی ... برای غلبه بر طرف' ('to take koštī is for two men to grapple by seizing the belt'), and Horn 854 already quotes kuštīgīr 'Ringkämpfer'. Wiktionary, after Edelman ESIJa IV 411-2 and Chehabi 2018, refines this: کشتی is a borrowing of Parthian *kuštīg (hence the š for s), a doublet of the inherited کستی - so within Persian the two are cognates rather than one from the other, which the chart's single box blurs. (3) برگستوان bargostovān 'armour, horse-armour' = Horn's *uparō-kusta-pāna- 'protection over the sides', with OIr. upari- > MP abar > NP bar- and pāna- 'protection'; Horn notes that the Garshāspnāma has the shorter kustuwān (printed gustuwān). BQT 261 has the entry with just the sense - 'پوششی است که در روز جنگ پوشند و بر اسب هم پوشانند' - and no etymology. Only the ultimate PIE parentage inherited from node 1 is wrong.\",\n \"derivation_fa\": \"هر سه واژه در درونِ ایرانی به یکدیگر مربوط‌اند و همه از فارسی میانهٔ kust «پهلو، سو» می‌آیند. «کستی» از پهلوی kustīg (مکنزی ۵۱؛ نیبرگ ۲: ۱۳۸) است، با پسوند -īg؛ معرّب آن «کستیج» است که خودِ برهان قاطع (ص ۱۶۴۳) می‌آورد. «کشتی» (مصارعه) هم همین واژه است؛ معین می‌نویسد «کشتی گرفتن عبارتست از مصارعهٔ دوتن با گرفتنِ کستی»، و هرن (بند ۸۵۴) نیز kuštīgīr «کشتی‌گیر» را می‌آورد. امّا پژوهش تازه (ادلمان، ویکی‌واژه) «کشتی» را وام‌واژهٔ پارتی *kuštīg و دوگانهٔ (doublet) «کستی» می‌داند — همین توجیه‌کنندهٔ شینِ آن است. «برگستوان» هم بنا بر هرن (بند ۲۰۵) *uparō-kusta-pāna- «نگاهدارِ پهلوها» است، با upari- > بر، و در گرشاسپ‌نامه صورت کوتاهِ «کستوان/گستوان» آمده است. خلاصه اینکه زنجیرهٔ ایرانی درست است و تنها پیوند آن با ریشهٔ هندواروپایی *kost- نادرست است.\",\n \"sources\": [S_KOSHTI],\n \"ref_check\": [\n   {\"ref\": \"BQT:261\", \"status\": \"partial\",\n    \"note\": \"BQT vol. 1 p. 261 (BQT_v1_pages.txt leaf 481) s.v. برگستوان: 'بمنم کاف فارسی و تای فوقانی، پوششی باشد که در روز جنگ پوشند و اسب را نیز پوشانند'; the neighbouring برگستان is glossed 'مخفف برگستوان'. The entry confirms word and meaning but offers no etymology.\"},\n   {\"ref\": \"BQT:1643\", \"status\": \"supports\",\n    \"note\": \"same footnote as node 1: 'لغت کشتی (مصارعه) ... از همین ریشه است. بنابرین کشتی گرفتن عبارتست از مصارعهٔ دوتن با گرفتن کستی ... برای غلبه بر طرف' - exactly the chart's gloss 'wrestling (by grabbing the opponent's belt)'.\"},\n   {\"ref\": \"BQT:1649\", \"status\": \"supports\",\n    \"note\": \"BQT vol. 3 p. 1649 (pdf page 442) s.v. کشتی, sense 5 'زنار', and it prints the very verse Nourai quotes: 'در خرابات نبینی که ز مستی همه سال - راهب دیر ترا کشتی و زنار دهد' (attributed there to سنایی غزنوی), matching the chart's 'Sanâî'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. کستی and کشتی (MON_part2.txt L.22987, 23339)\", \"stance\": \"supports\",\n    \"note\": \"'کستی: [= کشتی - معر. کستیج ...] کمربندی است زردشتیان را ...' and 'کشتی: (اِ.) کستی. گلاویز شدن دو تن با یکدیگر برای زورآزمایی و زمین زدن' - Mo'in equates the girdle and the wrestling word.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 51 s.v. kustig\", \"stance\": \"supports\",\n    \"note\": \"'kustig [kwstykʹ | N ~i] sacred girdle' - the direct Pahlavi ancestor of کستی.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn nos. 205 and 854\", \"stance\": \"supports\",\n    \"note\": \"no. 854 'kust \\\"Seite, Flanke\\\", kustī \\\"Gürtel\\\", vergl. bergustvuan (No. 205); kuštīgīr \\\"Ringkämpfer\\\"'; no. 205 'bergustuwān ... Etwa *uparō-kustapāna-' - all three of Nourai's Persian words, under one Iranian head, exactly as drawn.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II 138 s.v. kustik\", \"stance\": \"supports\",\n    \"note\": \"'kustik [kwstyk] the sacred thread worn by the Zoroastrians (tied round the waist) ... Paz. NP kusti'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary کشتی, Etymology 2\", \"stance\": \"partial\",\n    \"note\": \"'Borrowed from Parthian *kuštīg, from Proto-Iranian *kušti- ... Doublet of کستی (kosti, \\\"sacred Zoroastrian waist-girdle\\\"), which was inherited' (refs Edelman ESIJa IV 411-2; Chehabi 2018) - same family, but کشتی is a Parthian loan, not a straight descendant, and the PIE root is *kew-k-, not *kost-.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"costa\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin costa, -ae f. 'rib', attested since Plautus, with a secondary 'side, flank' (Ernout-Meillet 225); it is the sole Italic witness of Pokorny's *kost- and the form on which the root name is built, so root > Latin is here definitional rather than a derivation. In Medieval Latin costa acquired the sense 'shore' via 'side of the land', which is what carries the branch into Romance (It. costa, Sp. cuesta/costa, Fr. côte, Rum. coastă) and thence into English. Caveat: de Vaan (2008) severs costa from OCS kostь and calls it isolated, so the arrow's ultimate anchor is weaker than the chart implies.\",\n \"derivation_fa\": \"لاتینی costa «دنده»، گواهدار از پلاوتوس به بعد، و در معنای ثانوی «پهلو، کنار» (ارنو-مییه ص ۲۲۵). این تنها شاهدِ ایتالیایی ریشهٔ *kost- پوکورنی است، پس پیکانِ «ریشه و لاتینی» در اینجا بیشتر تعریفی است تا اشتقاقی. در لاتینی قرون وسطایی costa از راهِ «پهلوی خشکی» معنیِ «ساحل» گرفت و همین معنا به زبان‌های رومانی و از آنجا به انگلیسی رفت. یادآوری: دِ‌فان پیوند آن را با اسلاوی kostь می‌گسلد، پس پایهٔ نهایی این پیکان سست‌تر از آن است که نمودار می‌نمایاند.\",\n \"sources\": [S_COSTA, S_COAST],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. kost-: 'Latin costa, rib, side: COAST, COSTA, ... CUTLET' - Nourai cites AHD without a page here and the root list does carry the Latin form.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny 616\", \"stance\": \"supports\", \"note\": \"'Material: Latin costa \\\"rib\\\"; Old Bulgarian kostь \\\"bone\\\"'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. costa\", \"stance\": \"supports\",\n    \"note\": \"'costa, -ae f.: 1° côte ...; 3° côté, flanc. Attesté depuis Plaute' - and the Romance descendants via M.L. 3379.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.162 RIB s2\", \"stance\": \"supports\",\n    \"note\": \"'Lat. costa (> It. costa, Fr. côte, Rum. coastă; Sp. cuesta ...) : ChSl. kostĭ \\\"bone\\\"'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary 'costa' (Latin)\", \"stance\": \"partial\",\n    \"note\": \"'Of uncertain origin ... De Vaan rejects the connection between the Slavic and Latin terms.'\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"cotelette\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French côtelette (the book drops the circumflex, as it does throughout) 'cutlet', literally 'little rib': Middle French costelette, a double diminutive (-el- + -ette) of Old French coste 'rib, side' < Latin costa; OF coste > MF coste > côte with loss of preconsonantal -s- marked by the circumflex (13th-16th c.). The gloss 'originally from rib meat' is right - a côtelette is a cut from the ribs.\",\n \"derivation_fa\": \"فرانسوی côtelette «کتلت» تحت‌اللفظ «دندهٔ کوچک» است: از فرانسوی میانه costelette، مصغّرِ دوتایی (-el- و -ette) از فرانسوی کهن coste «دنده، پهلو» از لاتینی costa. s پیش از همخوان در فرانسوی افتاد و جای آن را نشانهٔ «^» گرفت (côte). معنیِ یادداشتِ نمودار — «در اصل گوشتِ دنده» — درست است. ادّعای نورایی درست است.\",\n \"sources\": [S_COTEL, S_CUTLET],\n \"ref_check\": [\n   {\"ref\": \"AHD:327\", \"status\": \"not_checked\",\n    \"note\": \"Nourai's page is in the body of the 1976 American Heritage Dictionary (the 'cutlet' page), which is not open online; the Watkins root list, which is open, gives CUTLET under kost- (AHD_watkins1985.txt L.644), so the substance is supported.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cutlet (KLN_1966.txt L.10034, p. ~700)\", \"stance\": \"supports\",\n    \"note\": \"'cutlet, n. - F. cotelette, lit. \\\"a little rib\\\", a double dimin. of cote, \\\"rib\\\", fr. OF. coste, fr. L. costa, \\\"rib, side\\\"'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary 'côtelette' (French)\", \"stance\": \"supports\",\n    \"note\": \"'From Middle French costelette (\\\"little rib\\\"), a diminutive of Old French coste (\\\"rib, side\\\"), from Latin costa.'\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"kotlet «کتلت»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian کتلت kotlet is a modern loan straight from French côtelette, taken over with the rest of the Franco-Iranian culinary vocabulary in the late Qajar/Pahlavi period (like ژله, دسر, سس); French -ette is rendered -et and the unstressed first -e- is lost, giving kotlet. In Iranian usage the sense has drifted from 'rib chop' to a fried patty of minced meat and potato, but the word is the same. Wiktionary: 'From French côtelette (\\\"cutlet\\\")'.\",\n \"derivation_fa\": \"«کتلت» وام‌واژه‌ای است نو و مستقیم از فرانسوی côtelette، از همان موجِ وام‌گیریِ اصطلاحات خوراکی فرانسه در اواخر قاجار و دورهٔ پهلوی. پسوندِ فرانسوی -ette در فارسی -et شده و واکهٔ بی‌تأکیدِ میانی افتاده است. در کاربرد ایرانی تحول معنایی رخ داده و از «تکه گوشتِ دنده» به «کوکوی گوشت و سیب‌زمینی» رسیده است. ادّعای نورایی درست است.\",\n \"sources\": [S_KATLET],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary 'کتلت' (Persian)\", \"stance\": \"supports\", \"note\": \"'From French côtelette (\\\"cutlet\\\").'\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi\", \"stance\": \"silent\",\n    \"note\": \"grep 'کتلت' in MON_part1/part2 OCR returns no headword; the word is a 20th-century borrowing and Mo'in files such items in vol. 4 (foreign compounds), not in the OCR at hand.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"cutlet\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English cutlet (1706) is French côtelette anglicised; the form was reshaped by folk etymology after the native verb cut, which is why it is cut- and not cot-. Klein: 'cutlet, n. - F. cotelette ... Cutlet was prob. influenced in form by cut'; Watkins lists CUTLET under kost-. So the chart's French > English arrow is right, with the folk-etymological remodelling worth naming.\",\n \"derivation_fa\": \"انگلیسی cutlet (۱۷۰۶م) همان côtelette فرانسوی است که در انگلیسی بومی شده؛ صورتِ آن به ریشه‌شناسی عامیانه زیرِ تأثیر فعلِ cut «بریدن» دگرگون شده و به جای cot- به صورت cut- درآمده است (کلاین: «Cutlet was prob. influenced in form by cut»). پس پیکانِ فرانسه به انگلیسی درست است.\",\n \"sources\": [S_CUTLET],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cutlet (KLN_1966.txt L.10034)\", \"stance\": \"supports\",\n    \"note\": \"'cutlet, n. - F. cotelette, lit. \\\"a little rib\\\", a double dimin. of cote, \\\"rib\\\", fr. OF. coste, fr. L. costa ... Cutlet was prob. influenced in form by cut.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kost- and index 'CUTLET kost-'\", \"stance\": \"supports\",\n    \"note\": \"CUTLET is listed among the English reflexes of kost- (AHD_watkins1985.txt L.644, L.1406).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"coast\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English coast: ME cost (early 12c. 'rib as a part of the body', early 14c. 'margin of the land') < Old French coste 'rib, side, flank; slope' (Mod.Fr. côte) < Latin costa. The chart draws the arrow straight from Latin and omits the Old French/Middle English stage, which is where the sense 'shore' actually arose: Medieval Latin/OF developed 'side of the land' > 'shore', and only the Germanic borrowings (Du. kust, Ger. Küste, Sw. kust) specialised fully in that sense. Klein: 'coast, n. - ME. cost, fr. OE. coste (F. cote), \\\"rib, coast\\\", fr. L. costa, \\\"rib, side\\\", which is cogn. with OSlav. kostĭ \\\"bone\\\"' (Klein's 'OE.' is a misprint for OF.).\",\n \"derivation_fa\": \"انگلیسی coast از انگلیسی میانه cost است که خود از فرانسوی کهن coste «دنده، پهلو، سرازیری» (فرانسوی امروز côte) و آن از لاتینی costa گرفته شده است. نمودار پیکان را یکسره از لاتینی به انگلیسی می‌کشد و مرحلهٔ فرانسوی کهن را حذف می‌کند، در حالی که تحول معنایی «پهلوی خشکی ← ساحل» دقیقاً در همان مرحله رخ داده است. جز این کاستی، ادّعای نورایی درست است.\",\n \"sources\": [S_COAST, S_COSTA],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. coast (KLN_1966.txt L.8031)\", \"stance\": \"supports\",\n    \"note\": \"'coast, n. - ME. cost, fr. OE. [sic, = OF.] coste (F. cote), \\\"rib, coast\\\", fr. L. costa, \\\"rib, side\\\", which is cogn. with OSlav. kosti, \\\"bone\\\". Cp. Rum. coasta, It., OProveng. costa ... Cp. accost, costal, ... cutlet, intercostal.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kost-\", \"stance\": \"supports\", \"note\": \"'Latin costa, rib, side: COAST, ...'\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/coast\", \"stance\": \"partial\",\n    \"note\": \"gives the Old French stage the chart omits - 'from Old French coste \\\"rib, side, flank; slope, incline;\\\" later \\\"coast, shore\\\"' - and adds de Vaan's rejection of the PIE etymology.\"}\n ]\n})\n\ndata[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 3 Kram\ne3 = {\n \"entry\": 3,\n \"root\": \"Kram, Krâmati\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Sanskrit क्रामति/क्रमति krā́mati/krámati 'strides, steps' (RV), from Indo-Iranian *kramH-; the Iranian branch is *xramH- (Cheung 2007: 449 f.)\",\n \"note\": \"The root box is right as stated: Skt kram- 'to stride, go' is Vedic and means exactly 'to walk, to step'. One correction of perspective: the Iranian forms in the chart are NOT descended from Sanskrit but are its sisters - Indo-Iranian *kramH- gives Skt kram- and Iranian *xram-, the initial x- being the regular Iranian outcome of *k before r (cf. Skt krátu- : Av. xratu-, Skt krūrá- : Av. xrūra-). Cheung, Etym. Dict. of the Iranian Verb 449 f., sets up *xramH 'to tread, stride, go' and adds: 'The IE origin of the common IIr. root *kramH- cannot be ascertained, lacking convincing IE cognate forms' - so the family is Indo-Iranian only, with no wider IE comparanda, and Nourai is right to head it with the Sanskrit verb rather than a PIE root. Wiktionary reconstructs Proto-Indo-Iranian *krā́mHti for خرامیدن.\",\n \"note_fa\": \"ریشهٔ سنسکریت kram- / krámati «گام برداشتن، راه رفتن» ویدایی و اصیل است. تنها نکته اینکه صورت‌های ایرانی از سنسکریت گرفته نشده‌اند بلکه هم‌ریشهٔ آنند: هندوایرانیِ *kramH- در سنسکریت kram- و در ایرانی *xram- شده است؛ تبدیلِ k به x پیش از r در ایرانی قاعده‌مند است (سنسکریت krátu- برابر اوستایی xratu-). چونگ (فرهنگ ریشه‌شناختی فعل ایرانی، ص ۴۴۹) ریشهٔ *xramH «گام برداشتن» را می‌نهد و می‌افزاید که برای این ریشهٔ مشترک هندوایرانی خاستگاهِ هندواروپایی مطمئنی نمی‌توان یافت. پس ادّعای نورایی درست است.\",\n \"sources\": [S_XARAM],\n \"ref_check\": [\n   {\"ref\": \"BQT:724\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' vol. 2 p. 724 (BQT_v2_pages.txt leaf 182), Mo'in's footnote 7 s.v. خرامیدن: 'از: خرام + یدن (پیوند مصدری)؛ جزو اول هندی باستان *kram- ... اسفا ۱:۲ ص ۹۳ و ۹۹' - the first element is referred to Old Indic kram-, exactly Nourai's root.\"},\n   {\"ref\": \"MON:1406\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi s.v. خرامیدن (MON_part1.txt L.55802): 'خرامیدن: xarāmīdan [هند.] (مص‌ل.) ... راه رفتن از روی ناز، تکبر، زیبایی و وقار' - the origin tag [هند.] = Indic. The page number itself cannot be checked (the OCR of Mo'in carries no page markers).\"},\n   {\"ref\": \"HRN:104\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p. 104 no. 474 (HRN.txt leaf 125): 'χirāmīden \\\"schreiten, gehen\\\". ai. krāmati, krāmyati, krāmitum \\\"gehen, schreiten\\\"' - Horn derives the Persian verb from the same Sanskrit root, and adds (after Vullers and Nöldeke) that خرام in the sense 'pleasant, delightful' is really xurram, a different word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007: 449 f. s.v. *xramH\", \"stance\": \"partial\",\n    \"note\": \"'*xramH \\\"to tread, stride, go\\\" ... *SANSKRIT: kram \\\"to stride, go\\\" (RV) ... The IE origin of the common IIr. root *kramH- cannot be ascertained' - same root, but as an Indo-Iranian sister set, not a Sanskrit-to-Iranian descent. References Horn 1893: 104, i.e. Nourai's HRN:104.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary 'خرامیدن'\", \"stance\": \"supports\",\n    \"note\": \"etymology tree 'Proto-Indo-European *k⁽ʷ⁾rḗmH-ti ~ *k⁽ʷ⁾rémH-n̥ti ? > Proto-Indo-Iranian *krā́mHti > Persian خرامیدن'; 'Inherited from Proto-Indo-Iranian *krā́mHti'.\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny\", \"stance\": \"silent\",\n    \"note\": \"no lemma kram-/xram- in POK_full.txt; Pokorny has no IE root for this family, matching Cheung's statement.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"xram\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Old Iranian root is real but the language label is not: *xram- is a reconstruction, not an attested Avestan or Old Persian word. Bartholomae's Altiranisches Wörterbuch has no verb xram- (the only apparent hit in the OCR, 'Zum V. xram-', is a misreading of 'Zum V. xraos-' in the entry xraosya-); Kent's Old Persian lexicon has nothing either; Cheung's *xramH is built on Middle Persian, Sogdian, Wakhi and New Persian alone. Nourai's own source says the same thing more carefully: Abolghasemi, Fe'l-ha-ye Farsi-ye Dari p. 50, writes 'خرام < فارسی میانه āxrām < ایرانی باستان *ā-xrām-' - 'Old Iranian', i.e. reconstructed Proto-Iranian, not Avestan/Old Persian. Phonologically the form is impeccable: Indo-Iranian *kramH- > Iranian *xram- by the regular change of *k to x before r (Skt krátu- : Av. xratu-, Skt krūrá- : Av. xrūra-).\",\n \"derivation_fa\": \"ریشه درست است ولی برچسبِ زبان نادرست: *xram- صورتی بازساخته (ایرانی باستان) است، نه واژه‌ای گواهدار در اوستا یا پارسی باستان. در فرهنگ ایرانی باستانِ بارتولومه فعلی به نام xram- نیست (تنها موردِ ظاهری در متن اسکن‌شده، بدخوانیِ xraos- است) و در فرهنگِ پارسی باستانِ کنت هم نیامده است؛ چونگ نیز ریشهٔ *xramH را تنها بر پایهٔ فارسی میانه، سغدی، وخی و فارسی نو می‌سازد. خودِ مأخذِ نورایی (ابوالقاسمی، ماده‌های فعل‌های فارسی دری، ص ۵۰) می‌نویسد «خرام < فارسی میانه āxrām < ایرانی باستان *ā-xrām-»، یعنی ایرانی باستان، نه اوستایی/پارسی باستان. از نظر آوایی بی‌عیب است: k پیش از r در ایرانی به x بدل می‌شود. پس ادّعا با احتیاط پذیرفتنی است، به شرط آنکه برچسب «اوستایی/پارسی باستان» به «ایرانی باستان (بازساخته)» تغییر کند.\",\n \"sources\": [S_XARAM],\n \"ref_check\": [\n   {\"ref\": \"FFD:50\", \"status\": \"partial\",\n    \"note\": \"Abolghasemi p. 50 (FFD_pages.txt pdf page 55) s.v. خرامیدن: '«خرام» < فارسی میانه āxrām < ایرانی باستان *ā-xrām-. ā پیشوند فعلی است. xrām صورت بالندهٔ ریشهٔ xram است و xram «گام برداشتن» معنی می‌دهد.' The root xram and its meaning are Abolghasemi's, but he calls it Old Iranian (reconstructed), never Avestan or Old Persian.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch\", \"stance\": \"silent\",\n    \"note\": \"no headword xram- anywhere in BRT.txt; the sequence 'Zum V. xram-' at L.10588 sits inside the entry xraosya- and is an OCR misreading of 'Zum V. xraos-'. Between xraod- and xraos- the dictionary jumps straight past any *xram-.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian: Grammar, Texts, Lexicon\", \"stance\": \"silent\",\n    \"note\": \"grep 'xram' in KNT.txt: no hit - the verb is not attested in the Achaemenid inscriptions.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007: 449 s.v. *xramH\", \"stance\": \"partial\",\n    \"note\": \"the entry lists Middle Persian, Sogdian, New Persian, Wakhi and Sanskrit - and conspicuously no Avestan or Old Persian section, i.e. the root is reconstructed for Iranian, not attested in the old languages.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 4174\", \"stance\": \"supports\",\n    \"note\": \"'xrʾam- (B, S) xram <Skt. kram - (to) move, (to) go' - the Sogdian cognate, which is what makes the Iranian root recoverable.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"a-xrâm\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian āxrāmīdan / āxrām- is well attested: MacKenzie 14 'Axrāmīdan, āxrām- [ʾhlʾm-ytnʹ | M ʾxrʾm-, N xirām-īdan] stride, strut' (and abar āxrāmīdan 'step up'); Cheung cites Book Pahlavi ʾhlʾmydyt /axrāmēd/ 'he strides' from Mēnōg ī Xrad ii.145, and Nyberg II 39b the Manichaean present stem ʾxrʾm-. The a- of Nourai's 'a-xrâm' is not a privative but the preverb ā-, as Abolghasemi says explicitly (FFD 50: 'ā پیشوند فعلی است' - 'ā is a verbal prefix'), attached to the full grade xrām- of the root xram-. The gloss 'to walk flauntily' matches MacKenzie's 'stride, strut'.\",\n \"derivation_fa\": \"فارسی میانه āxrāmīdan / āxrām- به خوبی گواهدار است: مکنزی (ص ۱۴) «āxrāmīdan، āxrām- [ʾhʾlʾam-ytn'] «خرامیدن، با ناز راه رفتن»، برابر فارسی نو xirāmīdan»؛ چونگ صورت فعلی /axrāmēd/ را از مینوی خرد (۲:۱۴۵) می‌آورد و نیبرگ ستاک مانوی ʾxrʾam- را. «a-» در a-xrâm پیشوندِ نفی نیست بلکه پیشوند فعلی ā- است؛ ابوالقاسمی هم می‌نویسد «ā پیشوند فعلی است» و xrām را صورتِ بالندهٔ (گران‌مایهٔ) ریشهٔ xram می‌داند. ادّعای نورایی درست است.\",\n \"sources\": [S_XARAM],\n \"ref_check\": [\n   {\"ref\": \"FFD:50\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi p. 50: '«خرام» < فارسی میانه āxrām ... ā پیشوند فعلی است. xrām صورت بالندهٔ ریشهٔ xram است' - the Pahlavi stem, its prefix and its relation to the root are exactly as the chart has them.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 14 (PHD.txt L.223)\", \"stance\": \"supports\",\n    \"note\": \"'Axrāmīdan, āxrām- [ʾhlʾm-ytnʹ | M ʾxrʾm-, N xiram-idan] stride, strut'; also 'abar āxrāmīdan: step up' (PHD.txt L.161, 3813).\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007: 449 s.v. *xramH\", \"stance\": \"supports\",\n    \"note\": \"'*MIDDLE PERSIAN: (+ *ā-) BMP ʾhlʾm- /axrām-/ \\\"to stride to\\\" ... Pres.: IND. 3sg. BMP ʾhlʾmydyt /axrāmēd/ (MX ii,145)'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II 39b (cited by Cheung)\", \"stance\": \"supports\",\n    \"note\": \"Nyberg lists the Manichaean MP present stem xrʾm-/āxrām-; Cheung notes that this MMP form 'is not mentioned in DMMPP', a small caveat about the Manichaean attestation only.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"xarâmîdan «خرامیدن»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian خرامیدن xarāmīdan 'to walk gracefully, strut' continues MP āxrām- with loss of the initial ā- (as in ābādān > NP بادان-type reductions, and cf. MP āxēzīdan > NP خیزیدن), plus the productive New Persian denominative/secondary infinitive suffix -īdan built on the present stem خرام: BQT 724 n.7 'از: خرام + یدن (پیوند مصدری)'; Abolghasemi p. 50 says the past stem خرامید is a secondary (جعلی) formation made from the present stem. The extra forms in the box, خرام and خرامان, are the bare present stem and its participle in -ān. Horn no. 474 and Mo'in ([هند.]) both refer the word to Skt krām-; the Sa'di verse Nourai quotes ('چند خرامی و تکبّر کنی - دولت پارینه تصوّر کنی') is the same verse Mo'in prints as note 8 on BQT 724.\",\n \"derivation_fa\": \"«خرامیدن» فارسی نو دنبالهٔ فارسی میانهٔ āxrām- است با افتادنِ ā- آغازین (همان‌گونه که āxēzīdan به «خیزیدن» رسید)؛ مادهٔ ماضیِ «خرامید» جعلی است و از مادهٔ مضارع «خرام» با پیوندِ مصدری «-یدن» ساخته شده (معین در حاشیهٔ برهان قاطع ص ۷۲۴: «از: خرام + یدن (پیوند مصدری)»؛ ابوالقاسمی ص ۵۰). دو صورت دیگرِ جعبه، «خرام» و «خرامان»، همان مادهٔ مضارع و صفت فاعلیِ -ان است. هرن (بند ۴۷۴) و معین (با نشانهٔ [هند.]) هر دو آن را به ریشهٔ سنسکریت krām- بازمی‌گردانند. ادّعای نورایی درست است.\",\n \"sources\": [S_XARAM],\n \"ref_check\": [\n   {\"ref\": \"MON:1406\", \"status\": \"supports\",\n    \"note\": \"Mo'in s.v. خرامیدن: 'xarāmīdan [هند.] (مص‌ل.) (خرامید، خرامد، خواهد خرامید، بخرام، خرامنده، خرامان، خرامیده) راه رفتن از روی ناز، تکبر، زیبایی و وقار' - meaning and the extra forms خرام/خرامان match; page not verifiable in the OCR.\"},\n   {\"ref\": \"FFD:50\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi p. 50: '«خرامید» مادهٔ ماضی جعلی است. از مادهٔ مضارع ساخته شده است. «خرام» < فارسی میانه āxrām < ایرانی باستان *ā-xrām-'.\"},\n   {\"ref\": \"BQT:724\", \"status\": \"supports\",\n    \"note\": \"BQT vol. 2 p. 724 s.v. خرام 'رفتاری را گویند که از روی ناز و سرکشی و زیبایی باشد' and خرامیدن 'راه رفتن به ناز و تکبر و زیبایی باشد', with footnote 7 'از: خرام + یدن (پیوند مصدری)؛ جزو اول هندی باستان *kram-' and footnote 8 quoting the Sa'di verse Nourai reproduces.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn no. 474, p. 104\", \"stance\": \"supports\",\n    \"note\": \"'474. χirāmīden \\\"schreiten, gehen\\\". ai. krāmati, krāmyati, krāmitum \\\"gehen, schreiten\\\"'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 14\", \"stance\": \"supports\",\n    \"note\": \"MacKenzie himself equates the Pahlavi verb with 'N xiram-idan'.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in s.v. خرام, خرامان, خرامیدن\", \"stance\": \"supports\",\n    \"note\": \"'خرام: xarām (اِ.) رفتار آهسته از روی ناز، سرکشی، زیبایی و وقار'; 'خرامان: xarāmān (ص‌فا.) رونده با ناز و تکبر و تبختر'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary 'خرامیدن'\", \"stance\": \"supports\",\n    \"note\": \"'Inherited from Proto-Indo-Iranian *krā́mHti'.\"}\n ]\n})\n\ndata[\"entries\"].append(e3)\n\n# ---------------------------------------------------------------- entry 6 Krei\ne6 = {\n \"entry\": 6,\n \"root\": \"Krei\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱrei- / *ḱreyH- 'to shine forth, appear, stand out' (Pokorny 618 k̑rei-; Walde-Pokorny I 478)\",\n \"note\": \"Correct in every part, but the page hides a trap: Pokorny p. 618 carries TWO roots spelled krei-. The velar krei-1 means 'to touch, brush' (Old Icelandic hrína, Lith. krienas) and has nothing to do with beauty; the one Nourai means is the palatal k̑rei-, on the same page 618, 'to appear, show oneself', whose whole material is the Indo-Iranian beauty family plus Homeric κρείων 'lord'. Walde-Pokorny I 478, Pokorny's own source, glosses it 'etwa \\\"hervorleuchten, sich hervortun\\\"' ('roughly, to shine forth, to distinguish oneself') - which is exactly Nourai's 'shine, glow, beauty'. Modern Wiktionary writes the root *ḱreyH-. Note that Watkins/AHD has no such root (his krei- is 'to sieve, discriminate', Pokorny's 4. sker- p. 945), so this is one of the roots for which Pokorny is the only列 authority Nourai could cite - and he cites it correctly. The printed page also shows an EMPTY node box drawn to the right of the Avestan box; it carries no text in the book, and the extraction rightly has no node for it.\",\n \"note_fa\": \"این ریشه درست است. تنها نکته آنکه در صفحهٔ ۶۱۸ پوکورنی دو ریشهٔ هم‌نویسه به صورت krei- آمده است: یکی krei-1 با کافِ پسین به معنی «لمس کردن، ساییدن» که به زیبایی ربطی ندارد، و دیگری که مقصودِ نورایی است ḱrei- با کافِ کامی، در همان صفحه، به معنی «پدیدار شدن، خود را نمودن» که همهٔ شواهدِ آن همین خانوادهٔ «زیبایی» در سنسکریت و اوستاست به افزودنِ یونانی هومری kreíon «سرور». والده-پوکورنی (۱: ۴۷۸) معنای آن را «چیزی مانندِ درخشیدن، سربرآوردن» می‌دهد که دقیقاً همان «shine, glow, beauty» نورایی است. ویکی‌واژه امروز آن را *ḱreyH- می‌نویسد. ادّعای نورایی درست است. در صفحهٔ چاپی، کنارِ جعبهٔ اوستایی یک جعبهٔ خالی نیز کشیده شده که در کتاب هیچ متنی ندارد.\",\n \"sources\": [S_SRI],\n \"ref_check\": [\n   {\"ref\": \"POK:618\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt L.51888: 'Root / lemma: k̑rei- | Meaning: to appear, show oneself | Material: Old Indic śrī- \\\"beauty, splendor ...\\\", Avestan srī- \\\"beauty\\\", Old Indic śrīla- \\\"beautiful\\\", a-śrīra- \\\"ugly\\\", Avestan srīra- \\\"beautiful\\\", Kompar. Old Indic śreyas-, Avestan srayah-, Superl. Old Indic śreṣṭha-, Avestan sraēšta-, ... Avestan srayan- n. \\\"beauty\\\" ... hom. poet. κρείων \\\"noble, princely, ruler\\\". References: WP. I 478. Page(s):618.' Every one of Nourai's four Avestan forms is in this entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 478 (WLD_Bd1_pages.txt leaf 487)\", \"stance\": \"supports\",\n    \"note\": \"'k̑rei- etwa \\\"hervorleuchten, sich hervortun\\\": Ai. śrī- f. \\\"Schönheit, Pracht, Zierde ... Majestät\\\", av. srī- \\\"Schönheit\\\", ai. śrīlá- \\\"schön\\\", a-śrīra- \\\"unschön\\\", av. srīra- \\\"schön\\\", Komp. ai. śreyas-, av. srayah-, Sup. ..., av. srayan- n. \\\"Schönheit\\\"' - the gloss here is closer to Nourai's 'shine, glow' than Pokorny 1959's.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\",\n    \"note\": \"Watkins has no root for this family; his 'krei-. To sieve, discriminate, distinguish' [Pok. 4. sker- 945] is a different root (CRIME, CERTAIN, CRISIS).\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. Creon and s.v. sri\", \"stance\": \"supports\",\n    \"note\": \"s.v. Creon (KLN_1966.txt L.9640): 'Gk. Κρέων, fr. κρείων ... \\\"ruler, lord, master\\\", which is cogn. with OI. śriyas-, Avestic srayah-, \\\"better\\\"'; s.v. sri (L.36511): 'OI. śrīḥ \\\"beauty, splendor, well-being ...\\\", rel. to Avestic srī \\\"beauty\\\", OI. śrīráh, Avestic srīra-, \\\"beautiful\\\", and cogn. with Gk. κρείων'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary Sanskrit श्री\", \"stance\": \"supports\",\n    \"note\": \"etymology tree 'Proto-Indo-European *ḱreyH- > Proto-Indo-Iranian *ćriHrás'; 'Compare Avestan 𐬯𐬭𐬍𐬭𐬀 (srīra)'.\"}\n ],\n \"nodes\": []\n}\n\ne6[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"srî, srayan; srîra; sra-yah; sra-ěšta\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four entries are genuine Avestan and all four stand in Pokorny's k̑rei- article. Bartholomae's Altiranisches Wörterbuch has srayan- n. 'Schönheit' (col. ~1640), srayah- Adj. 'der schönere' (col. ~1640), sraēšta- Adj. 'der schönste' (col. ~1607; e.g. yim aṣ̌ǝm vīspāi ... sraēštǝm 'the fairest', Y. 9.1), and srīra- 'schön' passim (yima srīra 'fair Yima', V. 2.22; kainīnō kǝhrpa srīrayā 'in the body of a beautiful maiden'). Morphologically Nourai's hyphens are right: sra-yah- is the comparative in *-yos- and sra-ēšta- the superlative in *-isto- built to the same stem (hence his cross-references to 'Yah 5' and 'Ištâ'), the zero-grade sra- alternating with the full grade srī- < *ḱri-H-. The Sanskrit counterparts śrī-, śrīlá-, śreyas-, śreṣṭha- match form for form, and Greek κρείων 'lord' is the western witness. The chart's 'srî ... beauty' is Bartholomae's srī- and 'srayan' his srayan- n., so listing them as one item slightly conflates two stems.\",\n \"derivation_fa\": \"هر چهار صورت اوستایی اصیل‌اند و همه در مادّهٔ ḱrei- پوکورنی (ص ۶۱۸) آمده‌اند. بارتولومه در فرهنگ ایرانی باستان می‌آورد: srayan- «زیبایی»، srayah- «زیباتر»، sraēšta- «زیباترین» و srīra- «زیبا» (مانندِ yima srīra «جمِ زیبا» در وندیداد ۲:۲۲). از نظر ساختواژه، خط‌فاصلهٔ نورایی درست است: sra-yah- صفت تفضیلی با پسوند *-yos- و sra-ēšta- صفت عالی با پسوند *-isto- است، بر همان ستاک sra- (درجهٔ صفر) در برابر srī- (درجهٔ کامل). برابرهای سنسکریتِ آن‌ها — śrī-، śrīlá-، śréyas-، śréṣṭha- — دقیقاً منطبق‌اند و یونانی kreíon «سرور» شاهدِ غربی آن است. ادّعای نورایی درست است؛ تنها «srî» و «srayan» دو ستاکِ جدایند که در یک سطر یکجا آمده‌اند.\",\n \"sources\": [S_SRI],\n \"ref_check\": [\n   {\"ref\": \"POK:618\", \"status\": \"supports\",\n    \"note\": \"Pokorny p. 618 s.v. k̑rei- lists 'Avestan srī- \\\"beauty\\\" ... Avestan srīra- \\\"beautiful\\\" ... Avestan srayah- [comparative] ... Avestan sraēšta- [superlative] ... Avestan srayan- n. \\\"beauty\\\"' - all four of the node's items, with the same glosses the chart gives.\"},\n   {\"ref\": \"KLN:371\", \"status\": \"not_found\",\n    \"note\": \"Klein 1966 p. 371 (leaf 197 of the archive scan) is the range core- ... Cornus and has nothing to do with this family. Klein does say what Nourai wants, but elsewhere: s.v. Creon, p. ~388 ('Gk. Κρέων, fr. κρείων ... cogn. with OI. śriyas-, Avestic srayah-, \\\"better\\\"') and s.v. sri, p. ~1570 ('OI. śrīḥ ... rel. to Avestic srī \\\"beauty\\\", ... Avestic srīra-, \\\"beautiful\\\", and cogn. with Gk. κρείων'). The page number looks like a slip; the substance is supported.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.vv. sraēšta- (col. ~1607), srayan-, srayah- (col. ~1640), srīra- (passim)\", \"stance\": \"supports\",\n    \"note\": \"'j., g. sraēšta- Adj. (fem. °tā-) \\\"der schönste\\\"'; 'j. srayan- n. \\\"Schönheit\\\"'; 'j. srayah- Adj. \\\"der schönere\\\"' (BRT.txt leaves 890, 894); srīra- 'schön' quoted throughout, e.g. 'āat aoxta ahurō .. yimāi: yima srīra' (V. 2.22) and 'kainīnō kǝhrpa srīrayā'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 478\", \"stance\": \"supports\",\n    \"note\": \"'av. srī- \\\"Schonheit\\\" ... av. srīra- \\\"schön\\\", Komp. ai. śreyas-, av. srayah- ... av. srayan- n. \\\"Schonheit\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. Creon, s.v. sri\", \"stance\": \"supports\",\n    \"note\": \"see ref_check KLN:371 - the same Avestan comparative srayah- and adjective srīra- are cited, with Greek κρείων.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\",\n    \"note\": \"no entry for this root; the Indo-Iranian 'beauty' family has no English reflex, so Watkins's English-oriented list omits it.\"}\n ]\n})\n\ndata[\"entries\"].append(e6)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-275.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build275.py && python3 -m json.tool data/verification/page-275.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 275"
}
```


### [2026-09-06T21:36:03.172Z] TOOL RESULT

```
written
JSON OK
nodes verified: 11/11
node verdicts: {'disputed': 1, 'plausible': 2, 'confirmed': 8}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'supports': 9, 'contradicts': 1, 'partial': 2, 'not_checked': 4, 'not_found': 1}
books consulted: {'supports': 28, 'contradicts': 1, 'silent': 5, 'partial': 4} | by book: {'Wiktionary': 5, 'PHD': 4, 'HRN': 4, 'KLN': 4, 'NYB': 3, 'MON': 3, 'AHD': 3, 'KNT': 2, 'BRT': 2, 'CHEUNG': 2, 'POK': 1, 'LAT': 1, 'SYN': 1, 'Etymonline': 1, 'SOD': 1, 'WLD': 1}
```


## [2026-09-06T21:36:11.898Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,io,re\np=\"data/verification/page-275.json\"\ns=io.open(p,encoding=\"utf-8\").read()\ns=s.replace(\"the only列 authority\",\"the only authority\")\nio.open(p,\"w\",encoding=\"utf-8\").write(s)\nd=json.load(open(p))\n# scan for CJK\nbad=set(re.findall(r'[　-鿿가-힯]', s))\nprint(\"stray CJK:\", bad)\nEOF\npython3 tools/verify_check.py 275 | tail -3\ngrep -c \"列\" data/verification/page-275.json || true"
}
```


### [2026-09-06T21:36:13.703Z] TOOL RESULT

```
stray CJK: set()
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'supports': 9, 'contradicts': 1, 'partial': 2, 'not_checked': 4, 'not_found': 1}
books consulted: {'supports': 28, 'contradicts': 1, 'silent': 5, 'partial': 4} | by book: {'Wiktionary': 5, 'PHD': 4, 'HRN': 4, 'KLN': 4, 'NYB': 3, 'MON': 3, 'AHD': 3, 'KNT': 2, 'BRT': 2, 'CHEUNG': 2, 'POK': 1, 'LAT': 1, 'SYN': 1, 'Etymonline': 1, 'SOD': 1, 'WLD': 1}
0
```


## [2026-09-06T21:36:33.096Z] AGENT

Done. `data/verification/page-275.json` written; `verify_check.py 275` reports **0 PROBLEM lines** (11/11 nodes).

**Page 275 (book p. 245) — 3 non-redirect entries, 11 nodes**
- Node verdicts: confirmed 8, plausible 2, disputed 1. Root verdicts: confirmed 2 (Kram, Krei), plausible 1 (Kost).
- Ref checks: 9 supports, 2 partial, 1 contradicts, 1 not_found, 4 not_checked. 38 `consulted` entries across POK, WLD, AHD, SYN, LAT, IEC, ARY, BRT, KNT, PHD, NYB, HRN, CHEUNG, SOD, KLN, MON, BQT, Wiktionary/Etymonline.

**disputed**
- Kost #1 (Pahlavi `kost`): the PIE *kost- parentage is Mo'in's alone (BQT 1643 n.1: "لاتینی costa و انگلیسی coast ... از همین ماده است"). Horn — whom Nourai cites here in Persian translation as AEF:261 — says the opposite at no. 854: "Aber nicht gehört dazu lat. costa 'Rippe'". Modern view (Edelman ESIJa IV 411-2 / Wiktionary): Proto-Iranian *kušti- < *kuši- "side of the body" < PIE *kew-k-, not *kost-; and PIE *o would give Ir. a, not u.

**transcription (book, not extraction)**
- Kost #1 second word: the book itself prints `uparô-kušta-pâma`; it is Nourai's misprint of Horn's reconstruction *uparō-kusta-**pāna**- (Horn no. 205, p. 48) — "-pāna- protection", which his own ☞Pa cross-reference confirms. Recorded with `error_in: "book"`; page PNG saved to `data/verification/sources/refs/ocr/BOOK/275.png`.

**plausible, worth the owner's eye**
- Kram #1 is labelled "Avestan / Old Persian" but *xram- is attested in neither: Bartholomae has no such verb (the one OCR "hit" is a misread of xraos-), Kent has none, Cheung builds *xramH on MP/Sogdian/NP/Wakhi only, and Nourai's own source Abolghasemi (FFD:50) says "ایرانی باستان" (reconstructed Old Iranian).
- Kost #2: the Iranian chain kust > kustīg > کستی/کشتی/برگستوان is solidly supported (Horn 854+205, MacKenzie, Nyberg, Mo'in), but کشتی is a Parthian-mediated doublet of کستی, not its descendant.
- KLN:371 (Krei node) is not_found: Klein p. 371 is the "core-…Cornus" range; the supporting text is at Creon (p. ~388) and sri (p. ~1570).

**Extraction errors for the owner:** none. (Informational: the printed Krei entry has a blank node box drawn to the right of the Avestan box; it is empty in the book, so the extraction is right to omit it.)
