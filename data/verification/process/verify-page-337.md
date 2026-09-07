# Verification process log — verify-page-337


## [2026-09-07T16:18:19.263Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 337 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-337.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-337.json. Write /home/sfmqrb/git/rishe/data/verification/page-337.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 337` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T16:18:21.460Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T16:18:22.171Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T16:18:22.185Z] TOOL RESULT

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


## [2026-09-07T16:18:22.695Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-337.txt"
}
```


### [2026-09-07T16:18:22.719Z] TOOL RESULT

```
1	=== PDF page 337 (book page 307) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Merg, Mereg : mark, border  (refs POK:738)
4	#1 (parent #0) [Avestan] refs=POK:738; KLN:940 | mereza : boundary
5	  #2 (parent #1) [Persian] refs=BQT:1986 | marz «مرز ۱» : border
6	#3 (parent #0) [Germanic] refs=None | mark : to mark
7	  #4 (parent #3) [English] refs=None | mark, remark, march
8	#5 (parent #0) [Latin] refs=AHD | margo : border, edge
9	  #6 (parent #5) [English] refs=None | margin
10	--- entry 1 ---
11	ROOT Mer-k -> redirect to Mer 2
12	--- entry 2 ---
13	ROOT [Indo-European] Merk : to take, grasp  (refs POK:739)
14	#1 (parent #0) [Latin] refs=POK:739 | merx, comerx : merchandise
15	  #2 (parent #1) [Italian] refs=MON:3392 | commerci : commerce
16	    #3 (parent #2) [Portuguese] refs=None | cumerx : trade
17	      #4 (parent #3) [Persian] refs=MON:3392; HJB:384 | gomrok «گمرک» : customs duties ; gambroon «گمبرون» : former name of port "Bandar Abbâs".
18	  #5 (parent #1) [English] refs=AHD | commerce, merchant, market
19	#6 (parent #0) [Latin] refs=AHD | merces : pay, reward, kindness ; Mercurius : god of commerce
20	  #7 (parent #6) [French] refs=None | 
21	    #8 (parent #7) [Persian] refs=MON:4015 | mercî «مرسی» : thanks
22	    #9 (parent #7) [English] refs=AHD:821 | mercy : kindness
23	  #10 (parent #6) [French] refs=None | 
24	    #11 (parent #10) [Persian] refs=MON |  | extra: مرکور ، مرکورکرم
25	  #12 (parent #6) [English] refs=None | mercury
26	--- entry 3 ---
27	ROOT Meth -> redirect to Menth
28	
```


## [2026-09-07T16:18:26.965Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-337.json",
 "description": "Read source JSON page 337"
}
```


### [2026-09-07T16:18:26.999Z] TOOL RESULT

```
{
  "pdf_page": 337,
  "book_page": 307,
  "entries": [
    {
      "root": {
        "name": "Merg, Mereg",
        "lang": "Indo-European",
        "refs": "POK:738",
        "gloss": "mark, border"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:738; KLN:940",
          "words": [
            {"translit": "mereza", "gloss": "boundary", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1986",
          "words": [
            {"translit": "marz", "gloss": "border", "script": "مرز ۱"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": null,
          "words": [
            {"translit": "mark", "gloss": "to mark", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "mark, remark, march", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "margo", "gloss": "border, edge", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "margin", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mer-k",
        "redirect": "Mer 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Merk",
        "lang": "Indo-European",
        "refs": "POK:739",
        "gloss": "to take, grasp"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:739",
          "words": [
            {"translit": "merx, comerx", "gloss": "merchandise", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Italian",
          "refs": "MON:3392",
          "words": [
            {"translit": "commerci", "gloss": "commerce", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Portuguese",
          "refs": null,
          "words": [
            {"translit": "cumerx", "gloss": "trade", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:3392; HJB:384",
          "words": [
            {"translit": "gomrok", "gloss": "customs duties", "script": "گمرک"},
            {"translit": "gambroon", "gloss": "former name of port \"Bandar Abbâs\".", "script": "گمبرون"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "commerce, merchant, market", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "merces", "gloss": "pay, reward, kindness", "script": null},
            {"translit": "Mercurius", "gloss": "god of commerce", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:4015",
          "words": [
            {"translit": "mercî", "gloss": "thanks", "script": "مرسی"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:821",
          "words": [
            {"translit": "mercy", "gloss": "kindness", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "مرکور ، مرکورکرم",
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "mercury", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Meth",
        "redirect": "Menth"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-07T16:18:27.150Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T16:18:27.187Z] TOOL RESULT

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


## [2026-09-07T16:18:35.549Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','MON','HJB','AHD','KLN','BRT','PHD','LEW','LAT','WLD','IEC','SYN','SKT','HRN','HUB','NYB','ARY','LKT','FSD','WEB','PHN','DEV','SIN']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


## [2026-09-07T16:18:36.706Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && ls site/pages/337.jpg 2>/dev/null; ls data/verification/sources/refs/ocr/ 2>/dev/null"
}
```


### [2026-09-07T16:18:36.933Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed pag
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
== SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sectio
```


### [2026-09-07T16:18:36.977Z] TOOL RESULT

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
site/pages/337.jpg
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
TAD
```


## [2026-09-07T16:18:44.241Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"=== $f\"; grep -n \"merǝg\\|mere.g-\\|merg-\" $f | head -20; done"
}
```


## [2026-09-07T16:18:45.055Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *merk-\\|merk-\\b\" POK_02.txt | head -30; echo \"---full\"; grep -c \"\" POK_full.txt"
}
```


### [2026-09-07T16:18:45.991Z] TOOL RESULT

```
=== POK_01.txt
=== POK_02.txt
6108:Ai.  märäti,  märjati,  rnfjäti  , wischt,  reibt  ab,  reinigt',  Partiz.  Perf.  mrstd-, s-Präs.  mxksdti  , streicht,  reibt,  striegelt',  mrksdyati,  mraksdyati  , bestreicht*; av.  mardzaiti,  mdrdzaiti  , berührt  streifend',  zastä-marsta-  , durch  Hand- schlag (d.  i.  Berührung  der  Hände)  geschlossen  (Vertrag)';  d-Präsens  ai. mrddti,  mrddyati  ,ist  gnädig,  verzeiht,  verschont',  av.  mdrdzdä-  ,verzeihen' {mdrdzdika-,  marzdika-  ,sich  erbarmend',  n.  , Barmherzigkeit');  diese  ar. Worte  können  auch  *merg-  enthalten ;  nichtpalatalen  Guttural  zeigt  ai. nir-märgd-h  »Verwischung;  Abgestreiftes,  Abfall',  ni-mxgra-  , sich  anschmie- gend', vi-mjrgvari  f.  , reinlich',  apämargdh-  ,Achyranthes  aspera'  (J.  Schmidt KZ.  25,  114);
6119:WP.  II  298  f.,  WH.  I  741  f.,  II  62  f.,  121  f.,  Trautmann  178,  Specht Idg.  Dekl.  147  f.;  vgl.  auch  melk-  und  merg-.
6314:mnd.  morken  ,zerdrücken',  ags.  murc(n)ian  ,sich  grämen',  murc  , drückend, nagend  (vom  Hunger)' ;  s.  weiteres  unter  (merk-),  merg-  ,morschen,  faulen' usw.
6348:1.  znerg-  (z.  T.  auch  ostidg.  merg-)  ,abstreifen,  abwischen'.
6351:2.  merg-  s.  unter  1.  merk-.
6366:I.  merk-,  merg-,  mergk-,  merog-  ,morschen,  faulen,  einweichen',  ursprüng- lich =  (mer-)^  merk-  ,auf reiben'  (S.  737).  jedoch  schon  grundsprachlich durch   die  Beziehung  auf  die  Feuchtigkeit  verselbständigt;   mroku- , Sumpf. Lat.   marceöj    -ere  ,welk,   schlaff  sein',  marcidus  ,welk,   schlaff',   marcor ,Welkheit,  Morschheit,  Schlaffheit';  gall.  hracis  , Getreideart  zur  Malzberei- tung'; mir.  mraich,  hraichj  cymr.  corn.  brag  ,Malz',  d.  i.  ,eingeweichtes,  ge- quollenes Getreide';  gallorom.  Hracu-  (*'mraku-) , Morast'  (:  slav.  *morky  ds.), cymr.  hrag-wellt  , Sumpfgras';  gall.  mercasius  ,Sumpf',  afrz.  marchais]  gall. emhrektoii  ,eingetunkter  Bissen'  (daraus   lat.  imhractum)-  mir.  bren,  cymr. braen  (*mrakno-)  ,morsch,  faul';  mhd.  mer(e)n,  mnd.  meren  ,Brot  in  Wein oder  Wasser  eintunken'  {*merhen),  lit.  merkiüj  merkti  ,(Flachs)  einweichen',
6370:znerg-  in  gleicher  Bed.  (vgl.  S.  736  wer-,  merg-  , aufreiben*) : Alb.  mardhem  , fröstle,  schauere',  marth  m. , starker  Frost*  (=  slav.  *morzx\, air.  meirc  (nir.  meirg)  ,Rost*,  mergach  , runzlig*  (*mergi-) ;  nir.  meirqeall ,Rauhheit*,  cymr.  merydd  , feucht,  träge*;  merddwfr  , Brakwasser',  abret mergidhaam  ,hebesco*  (bret.  mergl  ,Rost*  ist  ir.  Lw.) ;  mhd.  murc  ,morsch welk*,  nisl.  morkinn  , morsch,  mürbe  von  Fäulnis*,  aisl.  morkna  , morsch werden* ;  bulg.  'mr^zel  , Faulheit*,  aksl.  mr^z^h  (*'mirHti)  j^ßöeXvTTsad'at,^^ slov.  mrziti  ,ekeln*  (Basis  *merdg-)j  vgl.  ahd.  bruoh  »Moorboden,  Sumpf* mnd.  brök^  ndl.  broek ;  damit  ist  als  , Kälte  infolge  Nässe*  oder  als  , Gänse- haut* (vgl.  air.  meirc  ,Runzel*)  identisch  aksl.  po-m'nzngti  , frieren*,  mrazi russ.  moröz  (ebenfalls  Intonation  der  schweren  Basis)  ,Frost*. WP.  II  281  f.,  WH.  II  36  f.,  129,  Trautmann  182,  187.
=== POK_03.txt
```


### [2026-09-07T16:18:46.048Z] TOOL RESULT

```
6280:lit.  merk-iu,  -ti  ,die  Augen  schließen,  blinzeln',  m\rks-iu,  -"kti  , fort  während blinzeln',  ablaut.  üz-marka  , einer,  der  etwas  anblinzelt',  markstaü,  -^^' , blinzeln' ;
---full
93771
```


## [2026-09-07T16:18:55.789Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"merx\" POK_02.txt POK_01.txt POK_03.txt | head -20; echo \"=== mereg\"; grep -n \"mereg\\|merè\\|Grenze,  Rand\\|,Rand,  Grenze\" POK_02.txt | head -20"
}
```


### [2026-09-07T16:18:55.849Z] TOOL RESULT

```
POK_02.txt:6364:fraglich  ist  Zugehörigkeit  von  lat.  merx  ,Ware',  merces,  -edis  , Preis, Lohn.  Sold',  mercärl  .handeln',  osk.  amiricadut  .handelsmäßig',  amirikum .commercium'.
=== mereg
6263:X.  jner-,  erweitert  meregh-,  merdgh-,   ,flecliten,   binden;    Schnur,  Masche, Schlinge'. Gr.  fieq^lg,   -l^oq  f.    , Faden*;    dehnstufig   (irjQvofxai   ,wickle    zusammen, wickle  auf,  ^TjQiv^og  ,Faden,  Schnur'  (o^rjQLv^og  Plato  mit  sekundärem  er-), vorausgesetzt,  daß  j^ßQvsTai  Theokrit  1,  29  Hjperdorismus  ist;    aschwed. merpi,  aisl.  mei^d  .Fisch-Reuse'.
6264:meregh-,  merogh- :  gr.  ßgöxog  (*fAQ6xog)  m.  , Strick,  Schlinge,  Masche', ,Demin.'  ßqoxig  f.,  ^öoottov  ,Korb  aus  Rinde'  (aus  *^o^arToy ?) ;  mir.  braige, hraga  , Gefangener' ;  lett.  merga,  ablaut.  marga  , Geländer',  vielleicht  lit. 7ndr§ka  , Laken,  Fischernetz',  falls  aus  *mordgh-ska]  aksl.  mrä^a  .Netz, Schlinge',  russ.  mereza  , Netzsack,  Beutelnetz',  Demin.  mere^ka  , Masche im  Netz,  feines  Muster'  (daraus  zurückgebildet  merega  , Gewebe,  Geflecht, Stickerei'),  serb.  mreza  ,Netz'.
6342:mereg-  ,Rand,  Grenze'.
6343:Npers.  marz  ,Landstrich,  Mark';  lat.  margö,  -inis  ,Rand,  Grenze'  (^rn^TQ'^m^ -en-) ;  air.  mruig,  mir.  hruig  (*mrogi-)  ,Mark;  Landstrich',  cymr.  coriL bret.  bro  ,Bezirk',  hrogae  Galli  agrum  dicunt  (Schol.  zu  Juvenal  VIII  234^ gall.  PN  Brogi-märoSj  VN  AUohroges  (=  urnord.  alja-markiR  ,Ausländei^ u.  dgl. ;  got.  marka  f.  , Grenze',  ahd.  marc{h)a  , Grenze,  Grenzland',  aW mearc  ds.,  aisl.  mqrk  f.  , Grenzland,  Wald'  (*morgaj,  aisl.  landa-mark  n. ags.  gemearc  n.  , Grenze,  Grenzstrich,  Abgrenzung,  Definitio'  {*morgom) wahrscheinlich  auch  anord.  mark  n.  ,Zeichen,  Kennzeichen',  mhd.  marc(h) n.  ,Marke,  Kennzeichen',  nhd.  merken  (auch  Mark  als  Geld,  eigentlich .  wohl  ,Merkstrich  am  Gewicht').
6345:meregh-  ,benetzen,  rieseln'.
```


## [2026-09-07T16:18:56.765Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=393 && NR<=397 {print \"----LEAF \" NR; print}' POK_02.txt | head -120"
}
```


### [2026-09-07T16:18:58.048Z] TOOL RESULT

```
----LEAF 393
ern,  bereitwillig' ;
air.  menicc  , häufig,  reichlich,  oft',  cymr.  mynych  .frequenter',  corn. menough  ds.  (*meneggi-,  expressiv) ;  got.  manags,  ahd.  as.  manag,  ags.  manig, menig  ,viel,  manch\  aisl.  mengi  n.  , Menge' ;  mangr,  margr  , manch,  viel, freundschaftlich' ;  aksl.  m^nog^  ,viel'  {*monogo-)y  vgl.  auch  lit.  miniä  ,Menge' {*mfnia).
WP.  II  268  f.,  Trautmann  189.
nien{p)k-  ,kneten  (quetschen,  zermalmen)';  menku-  , weich'.
x4i.  mdcate,  mancate  , zermalmt,  betrügt,  ist  übermütig(?)'  (Dhätup. ;  mit wahrscheinlicher  Anreihung  auch  von:)  ai.  maiikü-  , schwach,  schwankend';
731
g,lb.  mekem  , mache  feucht,  werde  ohnmächtig,  erstarre',  i  mekan  ,matt, schwach',  meke  »Dummkopf  (*mnk-)-.
gr.  ion.  fidaaw  (*mnk-io),  att.  juättw  , drücke,  knete,  streiche,  wische' (paradigmatisch  vereinigt  mit  Aor.  Pass.  (xayfjvai,  zu  (xaysvg  usw.,  Wz. mag-^  ^'  ^^^^5  ^^  Glitt  zweideutig  (j^axTga  , Backtrog'),  ^ayiagia'  ßg&fia  ix Uo^ov  %olI  dXcpLTcjv  Hes. ;
ags.  mengan,  as.  mengian,  mhd.  mengen,  nhd.  mengen  (eigentlich  ,durchein- auderkneten'),  as.  gi-mang,  ags.  {ge)-mang  n.,  mhd.  ge-manc,-ges  m. , Mischung, Gemenge'  ;
lit.  minkau,  -yti  ,(Teig)  kneten',  minkstas  , weich',  ablaut.  mdnkau,  -yti (==  germ.  *mangjan),  lett.  micU  , treten',  miksts  , weich' ;
aksl.  mek^-k^  , weich',  *mekngti  ,weich  werden',  o-me-citi  , erweichen', russ.  mjäkis  ,das  Weiche  vom  Brot',  ablaut.  aksl.  m^ka  ,Mehl'  (skr.  müka, russ.  mukd  ds.),  mpka  ,Qual'  (skr.  müka  ds.)  usw. ;
vgl.  die  ähnlichen  Wurzeln  mak-  und  mag-.
WP.  II  368,   WH.  I  508,  II  3,  23  f.,  Trautmann  184  f.
meng'  , schöner  machen,  schwindelhaft  verschönern' :  nur  nominal.
kl.  manjü-,  manjuld-  , schön,  lieblich',  mangald-  n.  .gutes  Omen,  Glück'; osset.  mäng  , Betrug';  gr.  i.tdyyavov  n.  , Zaubermittel,  Kriegsmaschine', usw.  (daraus  entlehnt  lat.  manganum  ,Maschine',  alb.  mange  , Hanfbreche' usw.,  mhd.  mange  , Wurfmaschine',  nhd.  Mange{l)  ,Wäscherolle'),  gr. *[.iayyo)v  (daraus  lat.  mangö  , betrügerischer  Händler'),  (.layyavsvw  , betrüge', usw. ;  mir.  meng  ,Trug,  List',  mengach  , verräterisch' ;  aus  nhd.  mange stammt  ^.^v.  manga  ,Hure',  Vit.  mang a  , ungezogene  Person';  toch.  A  mank , Schuld,  Fehler'.
WP.  II  233,  WH.  II  28  f.
Wem-  , Fischname'?
Gr.  ^aivrj  (daraus  lat.  maena),  fxaLvlg  ,ein  kleiner  Seefisch',  slav.  *mhnb, russ.
----LEAF 394
  menh  usw.  .Aalraupe' ;  aber  ai.  mlnd-  m.  , Fisch*  (wovon  mäinikd-, mainald-  , Fischer')  ist  dravid.  Herkunft;  vielleicht  hierher  ahd.  muniwa, ags.  myne,  engl,  minnow  ,Elritze,  ein  Fisch'.
WP.  II  267  f.;  gehört  wohl  zu  4.  men-.
menöt,  Gen.  meneses,  woraus  menes-,  mens-,  mes-,  men-^m,  , Monat' und  ,Mond^^  wohl  als  personifizierte  »Zeitmessung'  zu  me-  , messen'. Ai.  mäs,  mäsa-  m.,  av.  mä,  Gen.  mär)hö,  npers.  mäh  ,Mond,  Monat'; arm.  amis,  Gen.  amsoy  , Monat'  {*mensos)]  gr.  att.  Neubildung  ff^Jy,  zum Gen.  inivog  (lesb.  f^i^vvog),  Nom.  ion.  (.isig,  dor.  ^ir^g  m.  ,Monat'  (*mens), lirjVTi  {^i.LTivGa)  ,Mond';  alb.  muai  , Monat'  {*mön-  aus  idg.  *77igw-);  lat. mensis    m.    , Monat'    (kons.    Gen.  PL  mens-um),  menstruus  ,monatlich'   (GN
732
Mena  ist  gr.  Lw.),  seme(n)stris  , sechsmonatig,  halbjährig',  umbr.  memn^' ,mense';  air.  ml  (*mens),  Gen.  mls  (*7nmsos),  cymr.  acorn.  mis,  bret.  7^12 , Monat';  got.  mena,  aisl.  mäni,  ags.  möna,  as.  ahd.  mäno  ,Mond'  (-en-St.)- got.  menöps,  aisl.  mänadr,  ags.  mönad,  as.  mänuth,  ahd.  mänöt,  nhd.  Monat (*me7iöt-),  lit.  miinuo  (*menöt),  m^nesis  m.  ,Mond,  Monat',  lett.  menes(i)g ,Mond,  Monat'  (dial.  lit.  minas  aus  einem  neutr.  *menos),  apr.  menins ,Mond';  abg.  m§s§ch  m.  ,Mond,  Monat'  (*mes-n-ko-) ;
toch.  A  man  , Monat',  man  nkät  ,Mond'  (=  ,Gott  Monat'),  B  meüe  ,Monat', mem  ,Mond'.
WP.  II  271  f.,  WH.  II  71  f.,  Trautmann  179  f..  Brandenstein  Studien  11  f.
1.  menth-f  meth-  , quirlen,   drehend  bewegen';   menthu-   , Rührlöffel' beim
Opfern'.
Ai.  mdnthati,  mathnäti  , quirlt,  rührt,  schüttelt',  mdntha-  m.  , Drehung, Rührlöffel',  av.  mant-  , rühren' ;
gr.  fj.öd'og  m. , Schlachtgetümmel',  uöd-ovQa  (*(j,od-oofa)  L  ,Heft  des  Ruders', dor.  iiod-wv  m.  ,Metökenkind' ;  att.  , Frechling',  lak.  f.iöd'a^  ds. ;
lat.  (osk.)  mamphur,  besser  manfur  ,ein  Stück  der  Drehbank' ;
aisl.  mgndull  m.  , Drehholz  an  der  Handmühle*,  nhd.  Mandel,  Mandel- holz  , Rollholz,   walzenförmiges  Holz' ;
lit.  mentüris,  -üre  (lett.  mieturis)  , Quirl,  Rührstock',  menöiü,  mgstl  , um- rühren (Mehl)',  lit.  mentZ  , Spatel',  mente  f.  , Schulterblatt' ;  abg.  m^tp,  mesti ^TaQ&xrsiv,  turbare',  Iter.  mgtiti,  *sz-metana  (russ.  smetdna  usw.)  , Sahne, Milchrahm',  dissimil.  aus  *s^-m§tana ;
abg.  motati  s§  ,agitari',  russ.  motäh  , auf 
----LEAF 395
 wickeln,  schütteln;  verschwen- den', usw.
WP.  II  269,  WH.  II  22  f.,  Specht  KZ  64,  13;  6Q,  49,  Trautmann  181  f.
2,  inenth-  ,kauen;  Gebiß,  Mund'.
Ai.  math-  , fressen' :
gr.  (.idd-vtaL'  yvctd-oi  Hes.  (vgl,  uatvvyrj  ,maked.  Fleischgericht'),  f.iaadoixaL ,kaue,  beiße'  (von  *^ad^Lcc-,  idg.  *mnth-{a),  ^adTdCco  ,kaue',  {.idaTa^  f. ,Mund'  und  , Mundvoll',  fj.aafixdw  , knirsche  mit  den  Zähnen',  ^oGavveiv' fiaffäffd-at '  ßgccdscog  Hes.  (wohl  mit  0  aus  a  vor  v,  aus  *iiao(o)vveiv,  vor- ausgesetzt von  att.  Maavvrlag,  TtaQaixaavvtrjq  m.  ^pai-asita') ;  e-stufig  iiea- Ta%a '  rijv  ^s^aar](j,iv7]v  Tqocprjv  Hes.  {^menth-to-) ;
lat.  mandö,  -ere-,  -i,  mansum  ,kauen'   {*m^nthö) ;
nir.  meadal  , Bauch,  Gedärme'  (*menth-lä  oder  *mnth-la)',
ahd.  mindil,  gamindel  n.  , Gebiß  am  Zaum',  ags.  midi  ds.,  aisl.  m^l {^minpl),    aschwed.    mll    ds. ;    aisl.   minna-sk    , küssen' :   schwundstufig  got.
\
733
jnunps,   aisl.   mudr,  munne,    ags.  müd,  ahd.  mund  ,Mund' ]    oder   zu  cymr. ^an^,  s.  oben  1.  men-.
WP.  11  270,  WH.  II  24;  Specht  Ug.  Dekl.  253  f.
X.  jner-,  erweitert  meregh-,  merdgh-,   ,flecliten,   binden;    Schnur,  Masche, Schlinge'. Gr.  fieq^lg,   -l^oq  f.    , Faden*;    dehnstufig   (irjQvofxai   ,wickle    zusammen, wickle  auf,  ^TjQiv^og  ,Faden,  Schnur'  (o^rjQLv^og  Plato  mit  sekundärem  er-), vorausgesetzt,  daß  j^ßQvsTai  Theokrit  1,  29  Hjperdorismus  ist;    aschwed. merpi,  aisl.  mei^d  .Fisch-Reuse'.
meregh-,  merogh- :  gr.  ßgöxog  (*fAQ6xog)  m.  , Strick,  Schlinge,  Masche', ,Demin.'  ßqoxig  f.,  ^öoottov  ,Korb  aus  Rinde'  (aus  *^o^arToy ?) ;  mir.  braige, hraga  , Gefangener' ;  lett.  merga,  ablaut.  marga  , Geländer',  vielleicht  lit. 7ndr§ka  , Laken,  Fischernetz',  falls  aus  *mordgh-ska]  aksl.  mrä^a  .Netz, Schlinge',  russ.  mereza  , Netzsack,  Beutelnetz',  Demin.  mere^ka  , Masche im  Netz,  feines  Muster'  (daraus  zurückgebildet  merega  , Gewebe,  Geflecht, Stickerei'),  serb.  mreza  ,Netz'.
WP.  U  272  f.,  Trautmann  182.
2.  mer-  , flimmern,  funkelnd
Ai.  mdrlci-,  marlcl  , Lichtstrahl,  Luftspiegelung^  (mari- :  gr.  [.laiga,  ^agtXr]) ;
gr.  f^aQf^aiQw,  {.lagiiagi^o)  , schimmere',  fxagt-Xr]  , Glutkohle',  Maiga  ,der '  funkelnde  Hundsstern';  dfAagvoooj  , funkle',  diiagvyr]  , Glanz,  Funkeln' (-tj-  durch  metrische  Dehnung,  vgl.  :)  i.iagf.iagvyrj  , Glanz,  schnelle  Bewe- gung', uagixagvüou)  {*-kiö)  , funkle',  wohl  von  einer  Basis  meru-]  vielleicht ^ogq)rj  f.  , Gestalt,  (*schimmerndes)  Äußeres
----LEAF 396
'  (*mor-bhä),  d-^sgcpeg'  alayjgov Hes.,  (.logcfvög  , dunkelfarbig'  (Reimwort  zu  dgcpvog  ds.);
lat.  merus  ,bloß,  rein,  uuvermischt',  wohl  ursprüngl.  ,klar,  hell';
ags.  ä-merian  , läutern;  prüfen,  auf  die  Probe  stellen',  ags.  mare  f.,  ablaut. aisl.  mura  f.  ,Silberkraut^;
russ.  dial.  mar^  , Sonnenglut ;  Schlaff  mdrevo  , Hitze,  bei  der  die  Luft  trüb weiß  ist;  Höhenrauch,  Luftspiegelung'  (*möreuom)  u.  dgl. ;  mit  '^m'br-  klr. 'rrtryj  ,neblig,  düster,  dumpfig',  mriju,  mrity  , schimmern,  dämmern,  neblig werden';
unsicher  mir.  hrl  , Forelle'  als  altes  Fem.  '^mrl  zu  lat.  merus,  sowie  gr. {a)(A,agig  ,ein  gewisser  kleiner  Fisch'.
Guttural  erweiterungen:
mer(9)k-  ,flimmern,  vor  den  Augen  flimmern:  sich  verdunkeln',  auch vom  Zwielicht.
Air.  mrecht-  »buntscheckig'  (*mrkto-  ,bunt'),  nir.  hreocktach  ds.,  ncymr. brith,  f.  braith  ds.,  corn.  bruit  ,varius',  bret.  briz  .fleckig',  cymr.  brithyll
734
f
, Forelle',  com.  hreithil  ,mugil',  bret.  Sreze^, Makrele'  (Marstrander  Zceltpk 7,  373  f.  unter  Anreihung  von:)  isl.  murta  , kleine  Forelle*,  norw.  tti^J jRotauge' ;
got.  maürgins  , Morgen',  aisl.  myrginn,  morg-inn,  -unn,  ags.  mergen,  mornon. as.  ahd.  morgan  , Morgen*.
lit.  merk-iu,  -ti  ,die  Augen  schließen,  blinzeln',  m\rks-iu,  -"kti  , fort  während blinzeln',  ablaut.  üz-marka  , einer,  der  etwas  anblinzelt',  markstaü,  -^^' , blinzeln' ;
slav.  *m'brknoti  in  aksl.  mirbknoti  ,sich  verdunkeln',  Aor.  po-mrbce,  serb mrknuti  , dunkel  werden*,  aksl.  nemrh^emyjh  , unzugänglich',  aöech.  mrkati , dämmern',  6ech.  , blinzeln,  schlummern,  finster  werden' ;  dazu  slav.  *mhrh\ in  serb.  wr/c  , schwarz',  slovak.  mrk  , Wolke',  klr.  swer/c , Abenddämmerung' ablaut.  slav.  *morkz  in  aksl.  mrak^  , Dunkel',  russ.  mörok  »Finsternis,  Nebel Gewölk':  russ.  merek  , Phantasieren,  Erscheinung;  böser  Geist',  bul» mräzgav  ,trüb,  unfreundlich  (vom  Wetter)',  mr^zd^,  mrish  , werde  trüb finster',  mTbzdoUjz  ,flimmere*  (stimmhafter  Wurzelausl.  durch  Fernassimi- lation), öech.  dial.  mfizdeti  se  , dämmern' ;
Gr.  dfxoQßög  , dunkel'  (äol.  oq  für  ao);  alb.  mje(r)gule  , Nebel,  Finsternis**
aisl.  myrkr  (*m{rkwa-),  acc.  myrkvan  , dunkel',  mjgrkvi,  myrkvi  m.  ,Finster-    f^ nis',  as.  mirki,  ags.  mierce  , dunkel;
lit.  mirgu,  -Ui  , flimmern',  lett.  mirdzet  , flimmern,  blinken',  mirgas  ,plötz- liches  iiervorblinken',  lit.  mdrgas  ,bunt',  marguoti  ,bunt  schimmern',  lett, marga  , Schimmer',  mürgi  ,Fhantasiebilder,  Nordlicht' ;  russ.  morgaU  ,blin- zeln,  winken*  ;
vielleicht  hierher
----LEAF 397
  die  Sippe  von  ai.  mrgd-  , Gazelle'  usw.  als  , scheckiges  -^^ Tier'  (wovon  rnfgayati  ,jagt')?
WP.  II  273  ff.,  WH.  II  78,  Trautmann  182  f.
5.  (iner-),  mor-(u-)  , schwärzen,  dunkle  Farbe,  Schmutzfleck'.
Gr.  (.lÖQVxog  ,,ö'xo2r£tv<5g",  f.is(.iOQvxi.isyog  ,(rauch) geschwärzt' ;  lit.  morai  PL , Schimmel' ;  russ.  mardju,  -tb  , schmieren,  verleumden',  maruSka  , Fleck, Mal',  öech.  morous  , aschfarbig  gestreiftes  Rind',  moraty  , schwarz  gestreift*, poln.  morus  , Schmutzfink' ;  n-Stamm  in  poln.  morqg  ,bunt  gestreift*  u.  dgl. ; hierher  auch  gr.  y.ÖQvov'  eidog  dexov  %al  ^avd-ög  Hes.  (, schmutziggelb'),  fiogrög' lieXag  cpaiog  Hes.,  vielleicht  auch  mit  s-Erw.  arm.  mrayl  , Dunkel,  Nebel, Wolke;  finster,  dunkel'  {*murayl  auf  Grund  von  *mor-so-),  mafaxul  , dicker Dampf,  DunkeP  {mfso-)  und  lit.  mürsinu  , besudle',  7nür(k)§linu  ,wasche, sudle'.
WP.  II  279 f.,  Trautmann  169,  Specht  Idg.  Dekl.  119.
735
f    ,,  xcer-,  mero-  ,sterben'  (==  5.  me7'-  , aufgerieben  werden').
l  2Vi.  marati,    mdrate    , stirbt',    arm.  meranim   , sterbe',    gr.   Ef.iOQTsv   ,starb
Hes.  (vgl-  lit.  meris  m.,  mire  f.  ,Tod^  merdeti  ,im  Sterben  liegen');  Kausat ^l  märdyati  , tötet',  osset.  märyn  ,töten',  lit.  marmti,  serb.  mbriti  ds., yswr.;  schwundstuf.  ai.  mriydte  , stirbt',  av.  miryeite  (=  md'ryeHe)  ds.,  apers (t-mariyatä  ,er  starb',  lat.  morior  (*mr-iör)  ,ich  sterbe';  baltoslav.  ^mire in  lit.  mirstu,  mifti  , sterben',  lett.  mirstu,  mirt  ds.  (dazu  lit.  mire  ,der Tote',  lett.  mirejs  m.  , Sterbender') ;  aksl.  wbrp,  mre7i  und  -m-ör^jJt  ds.,  hitt Ttie-ir-ta  (mert)  , starbt
Partiz.  mr-tö-  ,tot'  in  ai.  rnftd-  =  av.  mdrdta-  , gestorben',  arm.  mard ,Mensch'  (,Sterblicher'),  lat.  Moria,  Todesgöttin,  baltoslav.  *mirta-  ,tot' in  lit.  mirtöji  dienä  , Todestag',  aksl.  u-mr^t^je  n.  ,Tod',  usw. ;  n-mr-to- ,unsterblich,  lebendig'  in  ai.  amfta-,  av.  amdsa-,  gr.  ^/.ißgozog  (äol.  qo  für ga),  davon  ScfÄßgöoiog  ,zu  den  Unsterblichen  gehörig';  aus  äf.ißgoTog  ab- strahiert ßgoTÖg  , sterblich'  und  ßgövog  ,Blut'  (M.  Leumann,  Homer.  Wörter 126  ff.).
mr-tö-za  ,Tod'  in  ai.  mrtd-  n.  ,Tod',  ahd.  mord,  ags.  aisl.  mord  n. jMord'  (daneben  ^mf-tro-m
```


## [2026-09-07T16:19:05.697Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index for a given line number\nimport bisect\n# build cumulative: leaf boundaries at form feeds\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i in (6342,6364):\n        print('line',i,'leaf',leaf)\n    leaf += l.count('\\f')\nEOF"
}
```


### [2026-09-07T16:19:07.092Z] TOOL RESULT

```
line 6342 leaf 399
line 6364 leaf 401
```


## [2026-09-07T16:19:10.163Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==400 || NR==402 {print \"----LEAF(1based) \" NR; print}' POK_02.txt"
}
```


### [2026-09-07T16:19:11.385Z] TOOL RESULT

```
----LEAF(1based) 400
  anl.  s-  lit.  smerkti  ,in  Not  zu  versetzen  suchen',  smarküs  ,grausam', pa-smerkti  ,verderben',  nhd.  dial.  schmorgen  , darben,  notleidend
Hierher  (als  , Häcksel')  ags.  mearg  ,Wurst'  ==  aisl.  mgrr  ,ds.,  Eingeweide- fett* (*marhu-),  redupl.  gr.  ^ilfxagyivg  ,Blutwurst^;  hitt.  mar-kdn-zi  ,zer- schneidet^
S.  auch  2.  merk-  , verdrießlich'^  und  1.  merk-  ,morschen,  faulen  usw.'.
mer-s-'.
Ai.  masam,  masTm  kar-  ,pulverisieren*^,  masi-,  masl  ,Pulver^;
ahd.  morsäri  , Mörser'  (umgebildet  aus  lat.  mortärium,  s.  S.  736),  mhd. zermürsen  ,zerdrücken,  zerquetschen',  md.  zermorschen  ds.,  Schweiz,  -morsen, milrsen  ,zermalmen,  kleinstoßen',  mhd.  nd.  mursch,  murs,  nhd.  morsch,  ndl. morzelen  ,zerreiben'^.
WP.  II  276  ff.,  WH.  42,  110  ff.;  identisch  mit  4.  mer-.
6.  mer-,  mer-s-  ,stören,  ärgern,  vernachlässigen,  vergessen^;  morso-  , Ge- duld, Vergessen'^. Ai.  mfsyate  ,vergißt,  vernachlässigt,  verzeiht',  marsa-  m.  , Geduld', mfsä  , umsonst,  irrig',  Kaus.  marsayati  ,duldet,  verzeiht';  arm.  moranam ,vergesse'  (Meillet,  Esquisse^  40);  got.  marzjan  , ärgern',  ags.  mierran,  as. merrian,  afries.  meria,  ahd.  marren,  merren  ,hindern,  stören';  ags.  ä-mierran ,verderben',  afries.  mere  ,Band,  Fessel';  lit.  marsas,  , Vergessen',  dazu marsüs  ,vergeßlich',  lett.  äiz-märsa  f.  , Vergeßlichkeit' ;   lit.  mir§tü,  miHti
47
738  •
(nur   mit   uz-^  pa-)    und    lett.    äiz-mirstu,    äiz-mirst   , vergessen',   Ht    ir marsinti  , vergessen  machend WP.  II  279,  Trautmann  187.
merodh-,  mrädh-  ^aufsprudeln,  aufschütteln'??
Gr.  ßgciaau),  att.  ßgaTTco  (*ixQG-9'-ia)),  Aor.  eßqäGa,  ion.  iyc-ßQrjoao)  si^ brause  auf,  worfle^,  ßQaajxög  ,das  Sieden';  lett.  mürdet  ^aufsprudeln',  mt»2 , Sprudel',  lit.  mürdau,  -yti  , hineinstoßend  versenken'.
WP.  II  280.
mereg-  ,Rand,  Grenze'.
Npers.  marz  ,Landstrich,  Mark';  lat.  margö,  -inis  ,Rand,  Grenze'  (^rn^TQ'^m^ -en-) ;  air.  mruig,  mir.  hruig  (*mrogi-)  ,Mark;  Landstrich',  cymr.  coriL bret.  bro  ,Bezirk',  hrogae  Galli  agrum  dicunt  (Schol.  zu  Juvenal  VIII  234^ gall.  PN  Brogi-märoSj  VN  AUohroges  (=  urnord.  alja-markiR  ,Ausländei^ u.  dgl. ;  got.  marka  f.  , Grenze',  ahd.  marc{h)a  , Grenze,  Grenzland',  aW mearc  ds.,  aisl.  mqrk  f.  , Grenzland,  Wald'  (*morgaj,  aisl.  landa-mark  n. ags.  gemearc  n.  , Grenze,  Grenzstrich,  Abgrenzung,  Definitio'  {*morgom) wahrscheinlich  auch  anord.  mark  n.  ,Zeichen,  Kennzeichen',  mhd.  marc(h) n.  ,Marke,  Kennzeichen',  nhd.  merken  (auch  Mark  als  Geld,  eigentlich .  wohl  ,Merkstrich  am  Gewicht').
WP.  II  283  f.,  WH.  II  39  f.
meregh-  ,benetzen,  rieseln'.
Gr.  ßQix(x)  ,benetze,  regne,  überströme', 
----LEAF(1based) 402
ipat  , ergreifen'. H&oTtTLg  , Räuber';  durch  Metathese:  ßgaipai  .ergreifen',  ßgartrsiv  lod-ieiv u.  dgl.,  Hes. ;
fraglich  ist  Zugehörigkeit  von  lat.  merx  ,Ware',  merces,  -edis  , Preis, Lohn.  Sold',  mercärl  .handeln',  osk.  amiricadut  .handelsmäßig',  amirikum .commercium'.
WP.  II  283,  WH.  II  78  f.
I.  merk-,  merg-,  mergk-,  merog-  ,morschen,  faulen,  einweichen',  ursprüng- lich =  (mer-)^  merk-  ,auf reiben'  (S.  737).  jedoch  schon  grundsprachlich durch   die  Beziehung  auf  die  Feuchtigkeit  verselbständigt;   mroku- , Sumpf. Lat.   marceöj    -ere  ,welk,   schlaff  sein',  marcidus  ,welk,   schlaff',   marcor ,Welkheit,  Morschheit,  Schlaffheit';  gall.  hracis  , Getreideart  zur  Malzberei- tung'; mir.  mraich,  hraichj  cymr.  corn.  brag  ,Malz',  d.  i.  ,eingeweichtes,  ge- quollenes Getreide';  gallorom.  Hracu-  (*'mraku-) , Morast'  (:  slav.  *morky  ds.), cymr.  hrag-wellt  , Sumpfgras';  gall.  mercasius  ,Sumpf',  afrz.  marchais]  gall. emhrektoii  ,eingetunkter  Bissen'  (daraus   lat.  imhractum)-  mir.  bren,  cymr. braen  (*mrakno-)  ,morsch,  faul';  mhd.  mer(e)n,  mnd.  meren  ,Brot  in  Wein oder  Wasser  eintunken'  {*merhen),  lit.  merkiüj  merkti  ,(Flachs)  einweichen',
47*
740
ablaut.   mirkstü,  mifJcti  ,iin  Wasser  liegen*,   markyti   , einweichen*,  markh , Flachsröste*,  lett.   märks  ds.,  mP^rka  , Feuchtigkeit*,  mkrcet  , tunken*-   Vi morokvd  , Mo  rast*  (Umbildung  aus  *morky)^   wruss.  mjareca   ds.  (*merk{a\
znerg-  in  gleicher  Bed.  (vgl.  S.  736  wer-,  merg-  , aufreiben*) : Alb.  mardhem  , fröstle,  schauere',  marth  m. , starker  Frost*  (=  slav.  *morzx\, air.  meirc  (nir.  meirg)  ,Rost*,  mergach  , runzlig*  (*mergi-) ;  nir.  meirqeall ,Rauhheit*,  cymr.  merydd  , feucht,  träge*;  merddwfr  , Brakwasser',  abret mergidhaam  ,hebesco*  (bret.  mergl  ,Rost*  ist  ir.  Lw.) ;  mhd.  murc  ,morsch welk*,  nisl.  morkinn  , morsch,  mürbe  von  Fäulnis*,  aisl.  morkna  , morsch werden* ;  bulg.  'mr^zel  , Faulheit*,  aksl.  mr^z^h  (*'mirHti)  j^ßöeXvTTsad'at,^^ slov.  mrziti  ,ekeln*  (Basis  *merdg-)j  vgl.  ahd.  bruoh  »Moorboden,  Sumpf* mnd.  brök^  ndl.  broek ;  damit  ist  als  , Kälte  infolge  Nässe*  oder  als  , Gänse- haut* (vgl.  air.  meirc  ,Runzel*)  identisch  aksl.  po-m'nzngti  , frieren*,  mrazi russ.  moröz  (ebenfalls  Intonation  der  schweren  Basis)  ,Frost*. WP.  II  281  f.,  WH.  II  36  f.,  129,  Trautmann  182,  187.
2.  merk-,  znork-  ,verdrießlich*.
Corn.  moreth  ,Ärger,  Kummer*,  bret.  morc'het  ,souci,  malheur* ;  poln. marhotb  ,Brumme
```


## [2026-09-07T16:19:20.358Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==401 {print}' POK_02.txt | tail -30"
}
```


### [2026-09-07T16:19:21.622Z] TOOL RESULT

```
 ßQOxrj,  ßgox^rög  ,Regeii';  letj mer^wö^ , sanft  regnen',  me^rga,  märgä  ,sanfter  Regen';  cech.  mrhoUti  ,nieseln*, mrhülka  , feiner  Regen',  russ.  morgah  , trübe  werden'  (*mzrgatb)y  morochf morozgd  , feiner  Regen'  (*morgh-s-)^  morositb  ,fein  regnen'.
WP.  II  280,  Trautmann  182.
1.  znerg-  (z.  T.  auch  ostidg.  merg-)  ,abstreifen,  abwischen'.
Ai.  mr-na-j-äni  (1.  Sg.  Konj.),  mrnjata  (3.  PI.)  , wischen,  abstreifen'  (vgl. ö^ÖQywixi)  ]  s.  auch  unter  melg-]  arm.  merzem  ,scaccio,  espello';  gr.  d^egyat ,streife  ab  (Blätter,  Früchte)',  di.iogyög  ,ausdrückend',  dixögyrj  ,mulsche Masse  der  ausgepreßten  Oliven'  (daraus  lat.  amurca) ;  dfxögyvVj^iL  , wische ab;  drücke  aus'  {-og-  wohl  aus  -er-  unter  Einwirkung  des  folgenden  v); lat.  mergae,  -ärum,  ,Mähgabel',  mergeSj  -itis  f.  ,Garbe'  (,Zusammengestreiftes').
WP.  II  283,  WH.  II  76.
2.  merg-  s.  unter  1.  merk-.
merio-  ,junger  Mann'  und  zugehörige  oder  ähnliche  Femininbildungen.
1.  Ai.  mdrya-  m.  ,Mann,  junger  Mann,  Geliebter,  Freier',  maryakd-  m. ,Männchen'  (=  mpers.  merak),  gr.  fxetga^  m.  f.  ,Knabe,  Mädchen',  fj,eigdy.iov
739
^Knabe'  (der  Vokal  der  2.  Silbe  wohl  nach  nalla^)  ;  alb.  shemtre  f.  ,Neben- frau;  Rivalin'  {"sirL-meri),  vgl.  merkosh  ^Männchen,  Wöchner'  (vom  Männer- Kindbett),   vielleicht  auch   martoj  ,ich  verheirate'  {*mer-efonj)^   Jokl  L -k iJ.öff.;
ein  fem.  *m,rt  junges  Weib'  kann  vorliegen  in  lat.  marl-tus  .beweibt, verheiratet  (vom  Manne)'.
2.  Mit  ^--Formantien :  lit.  mergä,  apr.  mergo  .Mädchen,  Dienstmädchen, Magd' ;  vermutlich  auch  mit  brit.  -ch-  aus  -kk-  (Kons. -Doppelung  im  Kose- wort):  cymr.  merch,  bret.  merc'h,  corn.  myrgh  .Tochter.  Weib';  mit  -gn- hinter  formantischem  i :  kelt.  *morignä,  acorn.  moroin  .virgo.  puella,  ancilla' cymr.  mor-forwyn  .Seejungfer,  Sirene'  (aus  dem  Brit.  stammt  air.  muir- moru  ds.).
3.  Auf  -fi:  lit.  marti  .Braut.  Jungfer',  apr.  märtin  Akk.  Sg.  .Braut', lett.  märsa  .des  Bruders  Weib',  krimgot.  marzus  .nuptiae'  (d.  i.  marpus? oder  aus  *marpjös  assibiliert).  gr.  wohl  (?)  in  BqLTo^aQTig,  dem  kret.  Namen
I     der  Artemis,
WP.  II  281,  WH.  II  40  f.,  Trautmann   170.
ixneri:-  .fassen,  ergreifen'.
Ai.  mr§dti  .berührt,  faßt  an',  gr.  ßoazsTv  auvievai,  övaßQd'navog  .schwer zu  behandeln'  Hes.j  ßgayterov'  rcXfjd'og,  ßoärrsLV  jtXrj^vvsLv'  ßaqvyeiv  Hes.  ;
daneben  durch  Assimilation  aus  *marktö:  gr.  ^dguTO),  {.idg
```


## [2026-09-07T16:19:32.400Z] TOOL CALL #14: Bash

```json
{
 "command": "pdftoppm -f 337 -l 337 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg337\" 2>/dev/null || pdftoppm -f 337 -l 337 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg337; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T16:19:34.122Z] TOOL RESULT

```
total 16216
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 12:19 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb      471 Sep  7 12:18 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 12:18 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T16:19:37.415Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a862-a326-6760238436df/scratchpad/pg337.png"
}
```


### [2026-09-07T16:19:37.431Z] TOOL RESULT

```
File does not exist. Note: your current working directory is /home/sfmqrb/git/rishe.
```


## [2026-09-07T16:19:40.046Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg337.png"
}
```


### [2026-09-07T16:19:40.401Z] TOOL RESULT

```

```


## [2026-09-07T16:19:40.399Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T16:20:08.469Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT marəza\"; grep -n \"mardza\\|marəza\\|marzsa\\|marz-\\|mar.za-\" BRT.txt | head -25"
}
```


### [2026-09-07T16:20:08.523Z] TOOL RESULT

```
=== BRT marəza
18387:•  j.  *ßaoni.mar3za- '>  Adj.  (fem.  'sä-) 'Streifen   von   Fett   (habend,   d.  i.  beim
20077:•  j.  maraz-  V.  'streifend  berühren'.  Praes. 2  marsza-,  3  mfrpza-,  8  m^qz-''>.  —  Int m^rqidyäi.  [S,  noch  zu  mfr>^yumna-^
20093:•  j.  maraza-  m.  'Mark,  Grenzgebiet*: anusi^  plrftn  "z^m  avahistäl  "zwangs- weise soll  er  sich  in  das  äusserste  Grenz- gebiet" begeben"  V.  ^.  5^1.
```


## [2026-09-07T16:20:10.209Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD merg\"; grep -n -i \"^merg-\\|merg- *\\.\\|mereg\" AHD_watkins1985.txt | head -20; echo \"=== AHD merk\"; grep -n -i \"merk-\\|merx\\|mercari\\|Mercurius\\|mercari\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T16:20:10.295Z] TOOL RESULT

```
=== AHD merg
757:merg-. Boundary, border. 1. Germanic *mark-, bound- ary, border territory; also to mark out a boundary by walking around it (ceremonially “beating the bounds”); also a landmark, boundary marker, and a mark in general (and in particular a mark on a metal currency bar, hence a unit of currency); these various meanings are widely represented in Germanic descendants and in Romance borrowings: a. Old English mearc, boundary, landmark, sign, trace: MARK}; b. Middle Dutch mark, border: MAR- GRAVE; ¢. Old French marc, marche, border country: MARCH?, (MARQUEE), MARQUIS, (MARQUISE); d. Late and Medieval Latin marca, boundary, border: MARCHIONESS; e. Old Italian marcare, to mark out: DEMARCATION; f. Old English marc and Middle High German marke, a mark of weight or money: MARK?; g. Swedish mark, a mark of money: MARKKA. 2. Germanic *markja-, mark, border, in Old Norse merki, a mark, possible source of Old French marque, a mark: MARQUETRY; REMARK. 3. Germanic denominative verb *mark6dn in Frankish *markoén, to mark out (> Old French march(iJer, to trample): MARC, MARCH!, 4, Latin margo, border, edge: MARGIN. [Pok. mereg- 738.]
758:mergh-. To wet, sprinkle, rain. Variant form *mregh- in Greek brekhein, to wet: EMBROCATE. [Pok. meregh- 738.]
=== AHD merk
752:mer-'. To flicker; with derivatives referring to dim states of illumination. 1. Suffixed form *mer-o- in Latin merus, pure, unadulterated (< “unmixed wine” < “clear liq- uid”): MERE!, 2. Extended form *merk- in Germanic *murgana- in: a. Old English morgen, morning: MORN, MORNING, MORROW; b. Middle Dutch morghen, morn- ing: MORGEN; Cc. Old High German morgan, morning: MORGANATIC. 3. Possibly extended root *merg~- in Ger- manic *merkwia-, twilight, in Old English mirce, dark- ness: MURK. [Pok. 2. mer- 733.]
760:merk-'. To decay. Latin marcére, to decay, wither: MARCESCENT. [Pok. 1. merk- 739.] [merk-2. Italic root, possibly from Etruscan, referring to aspects of commerce. 1. Latin merx (stem merc-), mer- chandise (> mercdri, to trade): MARKET, (MART), MER- CER, MERCHANT; COMMERCE. 2. Latin merces, pay, reward, price: MERCENARY, MERCY. 3. Probably Latin Mercurius, the god of (inter alia) commerce: MERCURY. [In Pok. merk- 739.]] [merph-. Form. Greek root of unknown origin. 1. Suf- fixed o-grade form *morph-G- in Greek morphé, form, beauty, outward appearance: -MORPH, MORPHEME, MOR- PHO-, MORPHOSIS. 2. Possibly borrowed from Greek morphé, via Etruscan, is Latin forma, form, shape, contour, appearance, beauty: FORM, FORMAL, FORMULA; CONFORM, CORACIIFORM, DEFORM. [In Pok. 2. mer- 733.]] mers-. To trouble. Suffixed o-grade form mors-eyo- in Germanic *marzjan in Old English merran, mierran, to impede: MAR. [Pok. 6. mer- 737.] meu-. Damp; with derivatives referring to swampy ground and vegetation and to figurative qualities of wetness. 1. Extended form *meus- in Germanic *meus-, *mus- in: a. Old English mos, bog: Moss; b. Old Norse mosi, bog, moss, akin to the Scandinavian source of LITMUS. 2. Germanic suffixed form *meuz-i- in Old Norse myrr, bog: MIRE; (QUAGMIRE). 3. Suffixed zero-grade form *mus-to- in Latin mustus, new, newborn (< “wet”): MUST’, MUSTARD. 4. Possibly suffixed extended zero-grade form *mii-ro- in Greek murios, countless (< “flowing, endless”): MYRIAD. 5. Possibly suffixed ex- tended zero-grade form *mud-so- in Greek musos, un- cleanness: MYSOPHILIA, MYSOPHOBIA. [Pok. 1. meu- 741.] meue-. To push away. Latin movére, to move (> mobilis, neuter mobile, fickle, changeable): MOB, MOBILE, MO- MENT, (MOMENTOUS), MOMENTUM, MOSSO, (MOTIF), MO- TION, MOTIVE, MOTOR, MOVE, MOVEMENT; COMMOTION, EMOTION, PROMOTE, (REMOTE), (REMOVE). [Pok. 2. meu- 743.) meug-'. To act surreptitiously. Germanic *muk- or Celtic *mug- in Old French muchier, to skulk: MOOCH. [Pok. 1. meug- 743.] meug-2. Slimy, slippery; with derivatives referring to various wet or slimy substances and conditions. Enlarged form of meu-. 1. Nasalized form *mu-n-g- in Latin mungere, to blow the nose: EMUNCTORY. 2. Possibly Germanic *(s)mug-, referring to wetness and also to figurative slipperiness: a. Old English smoc, shirt: smock; b. Middle High German smuck, “clothing,” adornment, jewel: scHmMuCK; c. Old Norse mugga, driz- zle, akin to the source of Middle English muggen, to drizzle: MuGGY; d. Low German smukkelen, smuggeln, to smuggle (< “to slip contraband through”): SMUGGLE; e. Middle Low German smucken, to adorn (< “to make sleek”): SMUG; f. Old Norse mygla, mold, mildew, akin to the source of Middle English molde, mold: MOLD®. 3. Ger- manic *meuk- in Old Norse mjikr, soft: MEEK. 4. Variant form *meuk- in Latin miicus, mucus: MOIST, MUCILAGE, MUCO-, MUCUS, (MUSTY). 5. Zero-grade variant form *muk- in: a. Greek mukés, fungus, mushroom: -MYCETE, MYCO-; STREPTOMYCES, (STREPTOMYCIN); b. suffixed form *muk-so- in Greek muxa, mucus, lamp wick (< “nozzle of a lamp” < “nostril”): MATCH2, Myxo-. [Pok. 2. meug- 744.] mezg-'. To dip, plunge. 1. Latin mergere, to dip, dive: MERGE; EMERGE, IMMERSE, SUBMERGE. 2. Latin mergus, diver (water bird): MERGANSER. [Pok. 1. mezg- 745.] mezg-*. To knit. Germanic “mésk- in Middle Dutch a maesche, knitted fabric: MESH. [Pok. 2. mezg- 746. [mimos. A mime. Greek noun of unknown origin. MIME, MIMESIS, MIMIC.] [miser. Wretched, unfortunate. Latin adjective of un- known origin. MISER, MISERABLE, MISERY; COMMISER- ATE.]
1385:coMAl keme- COMB gembh- COMBAT battuere COMBINE dwo- COMBUSTION eus- COME gWa- COMEDO ed- COMEDY wed-2 COMESTIBLE ed- COMFIT dhé-1 COMFORT bhergh-2 COMITIA  ei-1 COMITY smei- COMMA skep- COMMAND man-2 COMMANDO man-2 COMMEMORATE (s)mer-1 COMMENCE ei-1 COMMEND man-? COMMENSURATE mé-2 COMMENT men-! COMMERCE merk-2 COMMINUTE mei-2 COMMISERATE miser COMMIT (s)meit(a)- COMMIX meik- COMMODE med- COMMODIOUS med-
1817:MARASCA om- MARASCHINO om- MARASMUS- mer-2 MARC merg- MARCESCENT merk-1 MARCH! merg- MARCH2 merg- Marcu Mawort- MARCHIONESS merg- MARE! marko-
1819:MARK2 merg- MARKET merk-2 MARKKA merg- MARLINE mer-3 MARMALADE melit-, mélon MARQUEE merg- MARQUETRY merg- MARQUIS merg- MARQUISE merg- MARRAM_ mori- MARROW mozgo- MARRY! = mari-
1820:Mars Mawort- MARSH mori- MARSHAL marko- MART merk-2 MARTIAL Mawort- MarTIAN Mawort- MARVEL smei- MASCULINE mas MASH meik-
1846:MELON mélion MELT mel-1 MEMBER méms- MEMBRANE méms- MEMENTO men-! MEMORABLE (S)mer-1 MEMORANDUM (s)mer-1! MEMORY (s)mer-1 MENACE men-2 MENAGE men-3 MENARCHE = arkhein, mé-2 MEND mend- MENDACIOUS mend- MENDICANT mend- MENHIR s6-2 MENINX méms- MENISCUS mé-2 MENOPAUSE mé-2 MENSCH man-! MENSES mé6-2 MENSHEVIK mei-2 MENSTRUAL mé-2 MENSTRUATE mé-2 MENSURAL mé-2 MENTAL men-1 MENTION men-1 MENTOR men-1 MENU mei-2 MERCENARY merk-2 MERCER merk-2 MERCHANT merk-2 MERCURY merk-2 MERCY merk-2 MERE! mer-1 MERE? mori-
```


## [2026-09-07T16:20:35.785Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 940 area: mark/margin/merx\"; grep -n \"^margin\\b\\|^marge\\|^mark\\b\\|Merx\\|merx\" KLN_1966.txt | head -30"
}
```


### [2026-09-07T16:20:35.836Z] TOOL RESULT

```
=== KLN 940 area: mark/margin/merx
8369:commerce,  n.  —  F.,  fr.  L.  commercium,  ‘trade, traffic,  intercourse,  commerce’,  fr.  con-  and merx,  gen.  mercis,  ‘merchandise’.  See  mercantile. Derivatives:  commerce,  intr.  v.,  to  have  inter¬ course,  commerc-iat,  adj.  and  n.,  commercial¬ ism,  n.,  commercial-ist,  n.,  cammercial-ize,  tr. v.,  commercial-ity,  n.,  commercial-ly,  adv. comminate,  tr.  and  intr.  v.,  to  threaten;  to  ana¬ thematize.  —  L.  comminatus,  pp.  of  commindri, ‘to  threaten’,  fr.  com-  and  minari,  ‘to  threaten’. See  minatory  and  cp.  menace, commination,  n.,  a  threat.  —  L.  comminatio,  gen. -onis,  fr.  comminatus,  pp.  of  commindri.  See prec.  word  and  -ion.
22921:marge,  n.,  edge,  border.  —  F„  fr.  L.  margo,  gen. marginis.  See  margin.
22922:margent,  n.,  margin.  —  An  archaic  var.  of  mar¬ gin.
22960:mark,  n.,  1)  boundary  (archaic);  2)  sign.  —  ME. merke,  marke,  fr.  OE.  mearc,  ‘boundary, bound¬ ary  sign,  sign,  mark’,  rel.  to  ON.  merki,  mark, 'boundary  sign’,  mork,  ‘forest’  (forests  often served  as  frontiers),  OFris.  merke,  OS.,  Goth. marka,  ‘boundary,  frontier’,  Du.  merk,  ‘mark, brand’,  mark,  ‘borderland;  mark,  sign’,  OHG. marcha,  MHG.  marke,  G.  Mark,  ‘boundary, boundary  land',G.  Marke,  ‘sign,  token ;  stamp  , and  cogn.  with  Avestic  marlza,  ‘border’,  L. margo,  gen.  marginis,  ‘edge,  brink,  border  ,  OIr. mruig,  h.  bruig,  ‘boundary;  district’,  W„  Co., Bret,  bro,  ‘district’.  Cp.  mark,  ‘to  put  a  mark on’,  mark,  a  weight.  Cp.  also  march,  ‘bounda¬ ry’,  Marcomauni,  margrave,  marque,  marquetry, marquis,  marquise,  countermark,  demarcation, remark.  Cp.  also  margin.  Cp.  also  Cymric, mark,  tr.  v.,  to  put  a  mark  on.  —  ME.  merken, ntnrken.  fr.  OE.  mearcian ,  ‘to  make  a  mark,  to
22962:mark’,  fr.  OE.  mearc,  ‘boundary,  sign,  mark’, rel.  to  ON.  merkja,  Dan.  merke,  Swed.  marka, OFris.  merkia,  MDu,  Du.  merken,  OHG. merken,  merchen,  MHG.,  G.  merken,  "to  mark, note’,  and  to  OS.  markon,  ON.  marka,  OHG. marchon,  markon,  of  s.m.  See  prec.  word.  OF. merchier ,  ‘to  mark,  note’,  is  a  Teut.  loan  word. Derivatives:  mark-ed,  adj.,  mark-ed-ly,  adv., mark-ed-ness,  n.,  mark-er,  n.,  mark-ing,  n. mark,  n.,  1)  a  weight;  2)  any  of  various  coins;  3) the  monetary  unit  of  Germany.  —  ME.  marke, fr.  OE.  marc,  prob.  fr.  ON.  mork,  which  is  rel. to  MHG.  mark,  marke,  G.  Mark,  ‘mark’.  These words  are  very  prob.  rel.  to  OE.  mearc,  ON.
22963:mark,  ‘boundary  sign’,  OHG.  marcha,  ‘bounda¬ ry,  boundary  land’.  See  mark,  "boundary; sign’.
22964:Mark,  masc.  PN.  —  L.  Marcus.  See  Marcus. Markab,  n.,  a  star  of  the  constellation  of  Pegasus. Arab,  markab,  ‘saddle;  ship,  vessel’,  fr.  rakiba, ‘he  mounted  a  horse,  he  rode’  (whence  also mdrkabah,  ‘vehicle,  carriage’),  which  is  rel.  to Heb.  rdkhdbh,  ‘he  mounted  a  horse,  he  rode’, rekhebh,  ‘chariot’,  merkabh,  ‘chariot,  saddle’, merkdbhdh,  ‘chariot’,  Aram.-Syr.  rlkhebK  ‘he mounted  a  horse,  he  rode’,  Syr.  mark  bha, ‘ship’,  Ugar.  rkb,  ‘to  mount  a  horse,  to  ride’, Akkad,  rakabu,  of  s.m.,  markabtu,  ‘chariot’, Ethiop.  rakaba,  ‘he  attained’, market,  n.  —  ME.,  fr.  ONF.  market,  correspond¬ ing  to  OF.  marchiet,  marc/iic  (whence  F.  marche), fr.  L.  mercatus,  ‘trade,  business,  marketplace’ [whence  also  It.  mercato,  OProveng.  and  Catal. mercat,  Sp.  and  Port,  mercado,  OS.  markat, MDu.  market  (Du.  markt,  dial.  Du.  mart), OHG.  markat  (MHG.  market,  G.  Markt)],  fr. mercatus,  pp.  of  mercari,  ‘to  trade’,  fr.  merx, gen.  mercis,  ‘ware,  merchandise’.  See  merchant and  cp.  mart,  which  is  a  doublet  of  market. Derivatives:  market,  intr.  andtr.  market-able, adj.,  market-abil-ity,  n.,  market-abl-y,  adv., market-ing,  n.
23519:Derivatives :  Mephistophele-an,  Mephistopheli- an,  Mephistophel-ic,  Mephistophel-ist-ic,  adjs. mephitic,  adj.,  exhaling  poison  from  the  earth;  of poisonous  smell.  —  Late  L.  mephiticus,  fr.  L. mephitis.  See  mephitis  and  adj.  suff.  -ic. mephitis,  n.,  poisonous  exhalation  from  the  earth ; a  poisonous  smell.  —  L.  mefitis  (less  correctly spelled  mephitis) ;  of  Oscan  origin, mercantile,  adj.,  commercial.  —  F.,  fr.  It.  mercan¬ tile,  fr.  L.  mercans,  gen.  -antis,  pres.  part,  ol mercari,  ‘to  trade,  traffic,  buy,  purchase’,  fr. merx,  gen.  mercis,  ‘merchandise,  wares’,  which is  of  uncertain  origin.  Cp.  market,  mart,  Mer¬ cedes,  mercenary,  merchandise,  merchant,  mercy, amerce,  commerce.
23525:Mercedes,  fem.  PN.  —  Sp.  (abbreviation  of  Maria de  las  Mercedes,  ‘Mary  of  mercies’),  pi.  of  mer- ced,  ‘mercy,  grace’,  fr.  L.  mercedem,  acc.  of merces,  ‘hire,  pay,  reward’.  See  next  word, mercenary,  adj.  —  ME.  mercenarie,  fr.  L.  merce- narius,  ‘hired,  paid’,  which  prob.  derives  fr. *mercennos,  for  *mercednos,  ‘of  pay,  for  hire’, fr.  merces,  gen.  -edis,  ‘hire,  pay,  reward’,  fr. merx,  gen.  mercis.  See  mercantile  and  adj.  suff. -ary  and  cp.  mercy.
23527:mercer,  n.,  a  dealer  in  textile.  —  F.  mercier, ‘trader’,  fr.  VL.  *mercidrius,  fr.  L.  merx.  gen. mercis.  See  mercenary.
23534:Mercurialis,  n.,  a  genus  of  plants,  the  mercury (bot.)  —  L.,  short  for  herba  Mercurialis,  name of  a  plant  mentioned  by  Pliny,  lit.  meaning  ‘be¬ longing  to  the  god  Mercury’.  See  Mercury. Mercury,  n.,  1)  the  god  of  traders  and  thieves  and the  messenger  of  the  gods  in  Roman  mythology; identified  later  with  the  Greek  Hermes;  2) name  of  the  smallest  planet  in  the  solar  system. —  L.  Mercurius,  fr.  Etruscan  *Mercura,  a  di¬ vinity  introduced  from  Etruria  into  Rome about  the  end  of  the  sixth  century  B.C.E.  (see Ribezzo  in  Rivista  indo-greco-italica,  15,99); prob.  not  related  to  L.  merx,  gen.  mercis,  ‘mer¬ chandise’.  Cp.  mercury,  the  element, mercury,  n.,  name  of  a  siivery-white,  fluid  me¬ tallic  element  (chem.)  —  Named  after  Mercury, the  messenger  of  the  gods  in  Greek  mythology ; prob.  so  called  because  of  the  great  mobility  of this  element.
23536:mercy,  n.  —  ME.  merci,  fr.  OF.  mercit,  merci  (F. merci),  fr.  L.  mercedem,  acc.  of  merces,  ‘hire, pay,  reward’  (in  VL.  also  ‘favor,  pity  ),  fr.  merx, gen.  mercis,  ‘merchandise,  wares’.  It.  merce,  Sp. merced,  ‘favor,  grace,  mercy’,  also  derive  fr.  L. mercedem.  See  mercantile  and  cp.  gramercy. Derivatives:  merci-ful,  adj.,  merci-ful-ly,  adv., merci-ful-ness,  n.,  merci-less,  adj.,  merci-less-ly, adv.,  merci-less-ness,  n.
```


## [2026-09-07T16:20:36.585Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB Gombroon\"; grep -n -i \"gombroon\\|gomron\\|gamron\" HJB.txt | head -20"
}
```


### [2026-09-07T16:20:36.639Z] TOOL RESULT

```
=== HJB Gombroon
2734:BANDEL, 'n.p.  The  name  of  the old  Portucuese  settlement  in  Bengal about  a  mile  above  Hoogly,  where  there still  exists  a  monastery,  said  to  be  the oldest  church  in  Bengal  (see  Imp. Gaseteer).  The  name  is  a  Port,  corrup- tion of  bandar,  *  the  wharf ' ;  and  in this  shape  the  word  was  applied  among the  Portuguese  to  a  variety  of  places. Thus  in  Correa,  under  1641-42,  we find  mention  of  a  port  in  the  Red Sea,  near  the  mouth,  called  Bandel dos  Malemos  0  of  the  Pilots ').  Chitta- gong  is  calleci  Bandel  de  Chaiigao  (e.g. m  Bocarro,  p.  444),  corresponding  to Bandar  Chdtgdm  in  the  Autobiog.  of Jahangir  {Elliot,  vi.  326).  [In  the Diarjr  of  Sir  T.  Roe  (see  below)  it  is applied  to  (Gombroon],  and  in  the following  passage  the  original  no  doubt runs  Bandar-i-Hvghll  or  Hngll-Bandar,
4243:1638.— "They  have  (at  Gombroon)  a certain  Copper  Coin  which  they  call  Beaorg, whereof  6  make  a  PeySy  and  10  Peys  make a  Chay  {ShOhA)  which  is  worth  alwut  bd. English."— F.  and  Tr.  of  J,  A,  Mandelslo into  the  E,  Indies,  E.  T.  1669,  p.  8.
7227:OONOO-BUNDEB,  CONa,  n.p. Rung  bandar  J  a  port  formerly  of  some consequence  ana  trade,  on  the  north shore  of  the  Persian  Qulf,  about  100  m. west  of  Gombroon.  The  Portuguese had  a  factory  here  for  a  good  many years  after  their  expulsion  from  Or- nius,  and  under  treaty  with  Persia, made  in  1625,  had  a  right  of  pearl- fishing  at  Bahrein  and  a  claim  to  half of  the  customs  of  CJong.  These  claims seem  to  have  been  gradually  disre- garded, and  to  have  had  no  effect after  about  1670,  though  the  Portu- guese would  appear  to  have  still  kept up  some  pretext  of  monopoly  of  rights there  in  1677  (see  Chardin,  ed.  1735, i.  348,  and  Bruc^s  Annals  of  the  E.I.C.. iii.  393).  Some  confusion  is  created by  the  circumstance  that  there  is  an- other place  on  the  same  coast,  called KongHn,  which  possessed  a  good  many vessels  up  to  1859,  when  it  was  de- stn^ed  bv  a  neighbouring  chief  (see Stiffe^B  P.  Gulf  Pilot,  128).     And  this
7231:1677.—"^  Voyage  to  CongO/or  Pearl,— Two  days  after  our  Arrival  at  Gombroon,  I
10351:GOMBROON.
10364:The  first  mention  of  Gombroon  in the  £.  I.  Papers  seems  to  be  in  161 G, when  Edmund  Connok,  the  Company's, chief  agent  in  the  Gulf,  calls  it  ^  Goin- hraun^  the  best  port  in  all  Persia,"  and "that  hopeful  and  glorious  port  of Gombroon "  {SainsfywnL  L  484-5  ; [Foster^  Letters,  iv.  264J).  There  was an  English  factory  here  soon  after the  capture  of  Hormuz,  and  it  con- tinued to  be  maintained  in  1759,  when it  was  taken  by  the  Comte  d'Estaisg. The  factory  was  re-established,  but ceased  to  exist  a  year  or  two  after.
10373:fVver  in  another  place  (marginal  rubric, p.  331)  says:  ''Gombroon  ware,  made  of Earth,  the  best  next  China."  Was  this  one of  the  sites  of  manufacture  of  the  Persian porcelain  now  so  highly  prized  ?  [*'  The  main Tarieties  of  this  Perso-Chinese  ware  are  the following: — (1)  A  sort  of  semi-porcelain, called  by  fhiglish  dealers,  quite  without reason,  ^Chnwroon  ware,'  wnich  is  pure white  and  semi-transparent,  but,  unlike Chinese  porcelain,  is  soft  and  friable  where not  protected  by  the  glaze." — Bncy,  Brit. 9th  ed.  xix.  621.]
10486:coin  spoken  of  in  Persia  (at  Gombroon and  elsewhere).  From  the  quotation from  Fryer  it  appears  that  there  was a  Go8s  and  a  Gosbegty  corresponding  to Herbert's  double  and  single  Cozbeg^ Mr.  Wollaston  in  his  English-Persian Did.  App.  p.  436,  among  "Moneys now  current  m  Persia,"  gives  "  5  dindr =  1  gh&z ;  also  a  nominal  money." The  ghdZy  then,  is  the  name  of  a  coin (though  a  coin  no  longer),  and  gh&z- beg!  was  that  worth  10  dindrs. Marsden  mentions  a  copper  coin, called  kaabegi^fiO  (nominal)  dinars^  or about  34(2.  {Numism.  Orient.,  456.)  But the  value  in  dindrs  seems  to  be  in error.  [Prof.  Browne,  who  referred the  matter  to  M.  Husayn  Kuli  Elhan, Secretary  of  the  Persian  Embassy  ia London,  writes :  "This  gentleman  states that  he  knows  no  word  ghdai-beg,  or gdzi-heg,  but  that  there  was  formerly a  coin  called  ghdz,  of  which  6  went  to the  shdhi;  but  this  is  no  longer  used or  spoken  of."  The  ghdz  was  in  use at  any  rate  as  late  as  the  time  of Hajji  Baba  ;  see  below.]
15723:1673.— "On  the  day  of  the  Vernal  Sqm-  ' nox,   we  returned  to  Gombroon,  when  the Mooret  introduced  their  New- Year  jEde  (see EED)  or  Noe  Boss,  with  Banqueting  and great  Solemnity."— /Vycr,  806.
16039:OBMUS,  OBMUZ,  n.p.  Properljr Hurmuz  or  Hurmuz^  a  famous  mari- time city  and  minor  kingdom  near  the mouth  of  the  Persian  Gulf.  The original  place  of  the  city  was  on  the northern  shore  of  the  Gulf,  some  30 miles  east  of  the  site  of  Rindar  Abbas or  Gombroon  (q.v.) ;  but  about  a.d. 1300,  apparently  to  e8caT)e  from  Tartar raids,  it  was  transferrea  to  the  small island  of  Gerun  or  Jerun,  which  may be  identified  with  the  Organa  of Nearchus,  about  12  m.  westward,  and five  miles  from  the  shore,  and  this was  the  seat  of  the  kingdom  when first  visited  and  attacked  by  the Portuguese  under  Alboquerque  in 1606.  It  was  taken  by  them  about 1B15,  and  occupied  permanently (though  the  nominal  reign  of  the native  kings  was  maintained),  until wrested  from  them  by  Shah  'Abbas, with    the    assistance    of    an    English
18134:1638.— "This  voyage  (Gombroon  to  Surat) ...  we  accomplished  in  19  days.  .  .  .  We drank  English  beer,  Spanish  sack,  French wine,  Indian  spirit,  and  good  English  water, and  made  good  Palepnnxen."— ifa}u:k/«/o, Putch  ed.  1668),  p.  24.  The  word  Pale- punsen  seems  to  have  puzzled  the  English translator  (John  Davis,  2nd  ed.  1669),  who has  •*  excellent  good  sack,  English  beer, French  wines,  Aruk.  and  otfver  re/reshynetUt." (p.  10).
20037:[1727.— "Shyraah  is  a  large  City  on  the Road,  about  550  Miles  from  Gombroon." — A.  Hamilton,  ed.  1744,  i.  99.
22247:1677.  —  ".  .  .  Receipt  of  Custom  (at Gombroon)  for  which  he  pays  the  King yearly  Twenty-two  thousand  Thomands. every  Thomand  making  Three  pound  and a  Noble  in  our  Accompt,  Half  which  we have  a  Right  to:*— Fryer,  222.
25171:Gamron,  466 ;  Gam- rou,  Gamrun,  3846,  a
```


## [2026-09-07T16:20:44.497Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10345,10375p' HJB.txt"
}
```


### [2026-09-07T16:20:44.548Z] TOOL RESULT

```
OOLD    MOHUB    FLOWER,    s.
Ca^emlfinia  pulcherrima,  Sw.  The name  is  a  corruption  of  the  H.  gtUmoTy which  is  not  in  the  dictionaries,  but  is said  to  mean  *  peacock-flower.'
[1877.— "The  crowd  began  to  press  to  the great  Gool-mohur  tree"— Allardyce,  City  of iSun^n^,  iii.  207.]
GOLE,  s.  The  main  body  of  an army  in  array ;  a  clustered  body  of troops  ;  an  irregular  squadron  of  horse- men. P. — H.  ghol;  perhaps  a  con- fusion with  the  Arab,  jam  (gavJ),  *a troop ' :  [but  Platts  connects  it  with Skt.  hula,  *  an  assemblage '].
1507.— "As  the  right  and  left  are  called Berftngh&r  and  Sewftnghftr  .  .  .  and  are  not included  in  the  centre  which  they  call  ghftl, the  right  and  left  do  not  belong  to  the ghUL'^BaAr,  227.
G0MA8TA,  OOMASHTAH,       384
GOMBROON.
180a— "When  within  reach,  he  fired  a few  rounds,  on  which  I  formed  my  men into  two  gholes.  .  »  .  Both  gholM  at- tempted to  turn  his  flanks,  but  the  men behaved  ill,  and  we  were  repulsed." — Skinner,  Mil,  Mem,  I  298.
1849.—"  About  this  time  a  large  gole  of horsemen  came  on  towards  me,  and  I  pro- posed to  charge  ;  but  as  they  turned  at  once from  the  fire  of  the  g^uns,  and  as  there  was  a nullah  in  front,  I  refrained  from  advancing after  them." — Brigadier  LoeJhwood,  Report  qf 2nd  Cavalry  Division  at  Battle  of  OoojaiU,
aOMASTA,  OOMASHTAH,  s. Hind,  from  Pers.  aumdshtahy  part. *  appointed,  delated.'  A  native  agent or  factor.  In  Madras  the  modem  ap- plication is  to  a  clerk  for  vernacular correspondence.
1747.—"  As  for  the  Salem  Cloth  they  beg leave  to  defer  settling  any  Price  for  that sort  till  they  can  bei^vised  from  the  Goa MastolB  (1)  in  that  Province."— ^.  St,  David Consn,,  May  11.  MS.  Records  in  India Office.
1762.— "You  will  direct  the  gentleman, Qomastahs,  Muttatvddies  (see  MOOT- BUDDY),  and  Moonthiei,  and  other  officers of  the  English  Company  to  relinquish  their farms,  taalues  (see  TALOOE),  gonges,  and golaluk"- 7A«  Nabob  to  the  Gofvemor,  in  Vaai Sittarty  i.  229.
1776. —  "The  Magistrate  shall  appoint some  one  person  his  gomastah  or  Agent  in each  Town."— JSToMof  5  Code,  56.
1778. —  "The  Company  determining  if possible  to  restore  their  investment  to  the former  condition  .  .  .  sent  gomastaliB,  or Gentoo  factors  in  their  own  pay." — OtTne, ed.  1803,  ii.  57.
c.  1785, — "I  wrote  an  order  to  my gomastah  in  the  factory  of  Hughly."— Zkuraccioli^s  L\fe  of  Clive,  lii,  448.
1817. — "The  banyan  hires  a  species  of broker,  called  a  Oomastah,  at  so  much  a month."— Jfi/r»  Higt,  iii.  13.
1837.—" .  .  .  (The  Bajah)  sent  us  a  vei^ good  breakfast ;  when  we  had  eaten  it,  his gomashta  (a  sort  of  secretary,  at  least  more like  that  than  anything  else)  came  to say  .  .  ." — Lettertfrom  Madras,  128.
OOMBBOON,  n.p.  The  old  name in  European  documents  of  the  place on  the  Persian  Gulf  now  known  as Bandar  'Ahbds,  or  'Aliba9l,  The  latter name  was  given  to  it  when  Shah 'Abbas,  after  the  capture  and  destruc- tion of  the  island  city  of  Hormuz, established  a  port  there.  The  site which  he  selected  was  the  little  town of  Gkunrnn.  This  had  been  occupied by  the  Portuguese,  who  took  it  from the  *King  of  Lar'  in  1612,  but  two years  later  it  was  tal^en  by  the  Shah.
The  name  is  said  (in  the  Geog,  Moffcmne^ i,  17)  to  be  Turkish,  meaning  *a Custom  House.'  The  word  aUud^  to is  probably  gumruk,  which  has  that meaning,  and  whici  is  again,  through Low  Greek,  from  the  Latin  cammarcmm* But  this  etymology  of  the  name  aeems hardly  probable.  That  indicated  in the  extract  from  A.  EUunilton  below  is from  Pers.  JbamrUn^  *a  shrimp,'  or Port.  camaraOj  meaning  the  same.
The  first  mention  of  Gombroon  in the  £.  I.  Papers  seems  to  be  in  161 G, when  Edmund  Connok,  the  Company's, chief  agent  in  the  Gulf,  calls  it  ^  Goin- hraun^  the  best  port  in  all  Persia,"  and "that  hopeful  and  glorious  port  of Gombroon "  {SainsfywnL  L  484-5  ; [Foster^  Letters,  iv.  264J).  There  was an  English  factory  here  soon  after the  capture  of  Hormuz,  and  it  con- tinued to  be  maintained  in  1759,  when it  was  taken  by  the  Comte  d'Estaisg. The  factory  was  re-established,  but ceased  to  exist  a  year  or  two  after.
[1565.— "Bam(M  Gombmo,  so-called  in Persian  and  Turkish,  which  means  Custom- house."— Mestre  Afonso's  Overland  Journey^ Ann,  Maritim.  e  Colon,  ser.  4.  p.  217.]
1614.— (The Captain-major)  ''under orders of  Dom  Luis  da  Gama  returned  to  succour Comor&o,  but  found  the  enemy's  fleet already  there  and  the  fort  surrendered.  .  .  . News  which  was  heard  by  Dom  Luis  da Oama  and  most  of  the  people  of  Ormuz  in such  way  as  might  be  expected,  some  of the  old  folks  of  Ormuz  prognosticating  at once  that  in  losing  C<miorlU>  Ormuz  itself would  be  lost  before  long,  seeing  that  the former  was  like  a  barbican  or  outwork  on which  the  rage  of  the  Persian  enemy  spent itself,  giving  time  to  Ormuz  to  prepare against  their  coming  thither."  —  iooarro. Decada,  349.
1622.—"  That  evening,  at  two  hours  of  the night,  we  started  from  below  that  fine  tree, and  after  travelling  about  a  league  and  a half  ...  we  arrived  here  in  SimbrJL,  a place  of  decent  size  and  population  on  the sea-shore,  which  the  Persians  now-a-days, laying  aside  as  it  were  the  old  name,  call the  'Port  of  Abbas,'  because  it  was  wrested from  the  Portuguese,  who  formerly  poaaesBed it,  in  the  time  of  the  present  King  Abbas/' —P.  delta  Valle,  ii.  418  j  [in  HakTSoc.  i.  8. he  calls  it  Combn].
c.  1680.— "  GKimbrown  (or  Gomroon,  as some  pronounce  it)  is  bv  most  Persians Kar'  i^ox^p  cald  Bander  or  the  Port Towne  .  .  .  some  (but  I  commend  them not)  write  it  Oamrou,  others  Gomrovf,  and other-some  Cummeroon,  ...  A  Tbwne  it  is of  no  Antiquity,  rising  daily  out  of  the mines  of  late  glorious  (now  most  wretched) Ormra,"'-Sir  T,  Herbert,  m.
GOMUTL
385
GONQ.
1673.— **  The  Sailors  had  stigmatized  this place  of  its  Excessire  Heat,  with  this  sarcasti- cal  Saying,  l%at  there  was  but  an  Inch-Deal between  Oomberoon  and  Hdl,**— Fryer ,  224.
fVver  in  another  place  (marginal  rubric, p.  331)  says:  ''Gombroon  ware,  made  of Earth,  the  best  next  China."  Was  this  one of  the  sites  of  manufacture  of  the  Persian porcelain  now  so  highly  prized  ?  [*'  The  main Tarieties  of  this  Perso-Chinese  ware  are  the following: — (1)  A  sort  of  semi-porcelain, called  by  fhiglish  dealers,  quite  without reason,  ^Chnwroon  ware,'  wnich  is  pure white  and  semi-transparent,  but,  unlike Chinese  porcelain,  is  soft  and  friable  where not  protected  by  the  glaze." — Bncy,  Brit. 9th  ed.  xix.  621.]
1727.— ''This  Ctombroon  was  formerly  a Fishing  Town,  and  when  Shaw  Abate  began to  buud  it,  had  its  Appellation  from  the Portugueze,  in  Derision,  because  it  was  a good  place  for  catching  Prawns  and Shrimps,  which  they  call  Camerong." — A. Hamitum,  i.  92 ;  [ed.  1744,  i.  93].
1762.— "As  this  officer  (Comte  d'Estaing) .  .  .  broke  his  parole  by  taking  and  de- stroying our  settlements  at  Oombroon,  and upon  the  west  Coast  of  Sumatra,  at  a  time when  he  was  still  a  prisoner  of  war,  we  have laid  before  his  M^esty  a  true  state  of  the case." — In  Long^  ^.
```


## [2026-09-07T16:20:55.025Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"=== $f\"; grep -n \"گمرک\" \"$f\" | head -5; done"
}
```


### [2026-09-07T16:20:56.309Z] TOOL RESULT

```
=== MON_part1.txt
39631:بدون تأدبهٌ حق گمرک و مالبات (فقط 
39855:(متاع): اجازة خروج دادن از گمرکث و 
91177:زمین و مانند آن. گمرک. تیزی شمشیر. 
98901:گمرکی: وجوهی که بابت گمرک از 
=== MON_part2.txt
11469:و پرداخت گمرک وارد کند» کسی که با 
32137:گمرکی و عوارض را ندهند. 
85932:و اکنون اداره گمرکث همان وظایف را 
86196:( گم رکخانه‌ها؛ گمرکات): وزسری که 
=== incoming/MON/MON_2vol_Adena_v1_djvu.txt
39631:بدون تأدبهٌ حق گمرک و مالبات (فقط 
39855:(متاع): اجازة خروج دادن از گمرکث و 
91177:زمین و مانند آن. گمرک. تیزی شمشیر. 
98901:گمرکی: وجوهی که بابت گمرک از 
=== incoming/MON/MON_2vol_Adena_v2_djvu.txt
11469:و پرداخت گمرک وارد کند» کسی که با 
32137:گمرکی و عوارض را ندهند. 
85932:و اکنون اداره گمرکث همان وظایف را 
86196:( گم رکخانه‌ها؛ گمرکات): وزسری که
```


## [2026-09-07T16:20:56.423Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW merx\"; grep -n \"^merx\\|merx,\" LEW_1910.txt | head -10; echo \"=== LEW margo\"; grep -n \"^margo\\|margo,\" LEW_1910.txt | head -10; echo \"=== LAT merx\"; grep -n \"merx\\|margo\" LAT.txt | head -10"
}
```


### [2026-09-07T16:20:56.491Z] TOOL RESULT

```
=== LEW merx
=== LEW margo
=== LAT merx
8918:merx, autres types rares, sans (Rymologie i.-e. sure.
13291:commercium: v.merx.
37619:merces; v.merx.
37742:lumiere". Pour le sens, ce qui serait le plus pres, ce serait v. angi.merx
37746:merx (mers; non. merces dans Sali. ap. Char. GLK I 37,aa), mercis
37780:a Mirqurios ( Mircurius Varr.). Pas d'itymologie sire, bien que merx
```


## [2026-09-07T16:21:00.508Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37740,37800p' LAT.txt"
}
```


### [2026-09-07T16:21:00.556Z] TOOL RESULT

```
mesure le rapprochement avec gr. oqj,apUCT< 7 io "j '^tincelle, je brille",
ixap^uxupw "j e brille", p,app.apa* Xap.7tpa Hes. et skr. mdrlcih "rayon de
lumiere". Pour le sens, ce qui serait le plus pres, ce serait v. angi.merx
7ia -
i-merian "purifier".
*
merx (mers; non. merces dans Sali. ap. Char. GLK I 37,aa), mercis
f.: marchandise. Dans la 1 . familiare s'emploie, comme negStiun, merci¬
monium, au sens de "affaire, chose", meme en pariant de personnes,
cf.Pl.Ci.7a7, «oZo mers, era, haec et callida est . - Anci en, usuel.
M.1.5536.
Dirivis et composis: mercor,-Oris (et mercO, M.L.5515): faire commerce
de; d'ou mercator , M.L.ssisb; -tiO; -tus,-Os, M.1.5516; iri. marcat,
etc., gem.: ali. Markt; -tOrius; -tara, etc.; mercimonium,-l n. (arch.);
commercor, -aris; commercium: - est emendi u endendique inuicem ius
Dlp. reg. 19,5; i* sens concret: "co'mptoir", et meme "marchandise";
3 ° relations (d'abord commerciales), ichanges, cf. Cic. Verr.5,31; Sali.
Iu.18,fi, mare magnum et ignara lingua commercia prohibebant . Enfin
quelquefois A 1 ’ipoque impiriale "pouvoir riciproque", on synonyme
de negotium; Omercor (Tac. Amm.), praemercor.
Mercurius,-l m. (Mirqurios dial.): 1* Mercure, di eu du commerce;
a* Mercure, planete; 3 0 garrot (dans la 1 . des vitirinaires)j influence
du gr. epuot? Mercuri (l) dies "jour de Mercure", M.1.5515»; britt. Mercher.
Le suffixe de Mercurius est le meme que celui de Titurius, Mamurius,
Veturius (itrusque?). Dirivi: mercuridlis,-e: de mercure; substantivi
mercuriSlis f.: mercuriale, piante, M.X.5518; mercuridles m.pl.: mem-
bres du colloge des marchands.
mercSs, - 5 dis (acc. mercem A basse ipoque, cf. heres) f. : 1° prix
payi pour une marchandise, cf. Cic., R.Am.as»,80 uno mercede duas res
assequi, et specialement pour un travail, "salaire, gage" et au figuri
"ricompense, punition"; a* loyer, fermage; par suite "revenu, rentes".
- Ancien, M.L.5517. Iri. meircit. »
Dirivis: mercSdula; mercennarius ( mercenarius), adj. et subst. (opposi
A gratuitus); nercgdSrius (ipoq.imp.); mercedonius adj. et subst.:
relatif A la paye, au salaire; payeur; *. mSnsis "mois intercalaire"
(proprement "qui solde le du"); mercedituum : mercennarium, quod
mercede se tueatur ? P.F.111,18; mercenndlis; mercedimerus (Lucii.
d'aprbs pAoOapvoc).
1 'osque a amiricatud "sana rimuniration", avec t qui, se retrouve
dans comnircium que cite Varron, fr.70 Goetz-Schoell, et le prinestin
a Mirqurios ( Mircurius Varr.). Pas d'itymologie sire, bien que merx
ait une forme archaique.
mespilum, -i n.: nefle. Emprunt au gr. |Aecr7uXov (—\t|), latinise;
d'ou des formes phonitiques mespulus et dissimilees *nespilus, nespila,
etc. (cf. nibulus). V. Graur, Mil.ling., p.15. M.L.5540; v.h. a. mespi la;
bret., arm. mesper.
messis: -y.meto.
-met: particule qui s'ajoute aux pronoms personnels (comme - pte,
-te), pour mettre la personne en relief ou 1 'opposer A d'autres; souvent
accompagni de ipse: egomet ipse, sSmet ipsum. Quelquefois anssi jointe
aux adjectifs possessifs. A survicu dans les langues romanes, unie
A ipse, cf. M.L. 5551 metipse, met ipsimus, et aussi 5547 -net.
Le -t suppose q^une voyelle finale s’est amuie. Ce -met ne se
retrouve nulle part ailleurs. On ne peut 1 'expliquer que par la juxta-
position de deux anciennes particules; pour cf.osq. tll-um, ombr.
ti-om en face de v.lat. tff-d (cette particule itait surement indo-
europienne), cf. '*eti (v. et). Mais les combinaisons que l'on peut faire713
m Stior
ainsi sont arbitraires.
meta, -ae £,: tout objet de forme conique, i* borne du cirque (com¬
poste de trois colonnes coniques); a° meule inftrieure d*un moulin
```


## [2026-09-07T16:21:01.291Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '85920,85945p' MON_part2.txt; echo \"=== v2 86190\"; sed -n '86190,86205p' MON_part2.txt"
}
```


### [2026-09-07T16:21:01.354Z] TOOL RESULT

```
عهده دارد. وزارت کشاورزی: (فره.) 
وزارتسخانه‌ای که ادارة امور مربوط به 
فلاحت و زراعت را به عهده دارد؛ وزارت 
زراعت» زراعت و فلاحت. وزارت کشور: 
(فر ه.) وزار تخانه‌ای که ادارة امور داخله 
کشور رابه عهده دارد؛ وزارت داخله. 
وزارت کمک ( گم رکخانه‌ها, گم رکات): 


وزارتخانه‌ای که در عهد قاجاریه (پیش از 
مشروطیت) ادارةٌ امور گم رک را به عهده 
داشت (مرآت البلدان ج ۱ضممهً ص ۲۹) 
و اکنون اداره گمرکث همان وظایف را 
متعهد است. وزارت مالیه: وزارت دارایی. 
ضح. در عهد قاجاریه (پیش از مشروطیت) 
این وزارتخانه دایر بود. (مرآت البلدان ج ۱ 
ضمیمهً ص ۲۵) وزارت مختار: (سیا.) شغل 
و مقام وزیر مسختار. (در عهد ناصرالدین 
شاه): رابجاد وزارت مختار که عبارت بود از 
یک قدرت افذه و سلطهٌ قویه قایم به وجود 
شش کس از اعضاء دولت و کبراء مملکت 
که در سال بسیست و هشتم جلوس 
(ناصرالدین شاه) بعد از مراجعت از سفر 
فرنگ برقرار گردید» (الماثر و الاثار. 
۵ وزارت مشاغل: (قاجاریان) وزارت 
کار. وزارت معادن: وزار تخانه‌ای که در عهد 
=== v2 86190
وزارت کار را اداره کند (پهلویان). وزیر 
کشاورزی: (فره.) وزیری که وزارت 
کشاورزی را اداره کند (پهلویان)؛ وزیر 
زراعت» وزیر فلاحت. وزیر کشور: (فره.) 
وزسری که وزارت کشور را اداره کند 
(یسهلویان)؛ وزیر داخله. وزیر گم رک 
( گم رکخانه‌ها؛ گمرکات): وزسری که 
وزارت گم رک را اداره کند (قاجاریان» 
بسهلویان). وزیر لشکر: وزیسر جنگ 
(قاجاریان). وزیر مالیه: وزیری که وزارت 
سالیه را اداره می‌کرد (قاجاریان؛ پهلوی 
اول)) وزیر دارایی. وزیر مختار: (سیا.) 
مأمور وزارت خارجه در سفارتخانةٌ کشور 
خود که در کشور دیگر به کار می بردازد؛ 
مقام وی پس از سفیر (کبیر) است. وزیر 
مشاغل: وزیری که وزارت مشاغل را اداره
```


## [2026-09-07T16:21:11.427Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T16:21:11.434Z] TOOL RESULT

```


```


## [2026-09-07T16:21:15.445Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%B2",
 "prompt": "Give the Persian entry مرز (marz) 'border': its etymology in full — Middle Persian form, Old/Proto-Iranian, Avestan cognate, PIE root, and any cited sources."
}
```


## [2026-09-07T16:21:16.848Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/merx",
 "prompt": "Give the Latin entry merx: etymology in full (including any statement about unknown/Etruscan origin, de Vaan), and derived terms (mercor, merces, mercatus, commercium)."
}
```


### [2026-09-07T16:21:22.888Z] TOOL RESULT

```
# Etymology of Persian مرز (marz) "border"

**Middle Persian Form:**
From Middle Persian (mlc /⁠marz⁠/, meaning "boundary, march; (astronomy) term")

**Proto-Iranian/Old Iranian:**
The word descends from Proto-Indo-European *mórǵs, meaning "edge, boundary, border"

**Avestan Cognate:**
𐬨𐬀𐬭𐬆𐬰𐬀 (marəza), meaning "frontier"

**PIE Root:**
*mórǵs ("edge, boundary, border")

**Related Cognates Across Languages:**
The entry documents cognates in Proto-Germanic *markō (yielding English "march" and "mark"), Latin margo, Old Armenian մարզ (marz), Georgian მაზრა (mazra), and Classical Syriac ܡܪܙܐ (marzā).

**Cited Sources:**
The etymological information derives from three references: Ačaṙean's Armenian Etymological Dictionary (1977), MacKenzie's Concise Pahlavi Dictionary (1971), and Steingass's Comprehensive Persian–English Dictionary (1892).
```


### [2026-09-07T16:21:23.048Z] TOOL RESULT

```
# Latin Entry: merx

## Etymology

The word **merx** derives from Proto-Italic *merks. De Vaan proposes connections to Mercurius, "deriving them both from a root referring to various aspects of economics, which he presumes to have an Etruscan origin."

However, two competing Indo-European etymologies emerged in the 2020s:

- **Nikolaev's reconstruction**: Proto-Indo-European *merkʷ-, relating to Ancient Greek márptō ("to take hold") and Tocharian A märk- ("to take away").

- **Matasović's derivation**: A root *merǵ- meaning "to divide," also appearing in Latin margō ("border") and connected to Persian marz, Hittite mar-ak-zi ("to cut up, separate, divide, distribute"), and potentially extending from *mer- ("to divide, apportion, allot").

## Derived Terms

The entry lists these related words:
- commercium
- mercēs
- mercimōnium
- mercor

**Note**: The source document does not include "mercatus" among the listed derived terms.
```


## [2026-09-07T16:21:29.989Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%85%D8%B1%DA%A9",
 "prompt": "Persian گمرک (gomrok) — full etymology: what language is it borrowed from (Turkish? Greek? Italian?), the intermediate forms, and any cited sources."
}
```


## [2026-09-07T16:21:30.549Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Mercurius",
 "prompt": "Latin Mercurius: full etymology — is it derived from merx, or Etruscan? What does the entry say and which scholars are cited?"
}
```


### [2026-09-07T16:21:34.988Z] TOOL RESULT

```
# Etymology of Latin *Mercurius*

According to the Wiktionary entry, the origin is uncertain. The etymology section states:

"Possibly from *merx* ("merchandise"), or perhaps from Etruscan and influenced by *merx*."

The entry cites only one source: Douglas Harper's *Online Etymology Dictionary* (2001–2026), which discusses the term "Mercury." No additional scholars are referenced to support either the Latin derivation theory or the Etruscan influence hypothesis. The entry presents both possibilities without definitively resolving which origin is correct.
```


### [2026-09-07T16:21:35.085Z] TOOL RESULT

```
# Etymology of Persian گمرک (gomrok)

The word **گمرک** is ultimately borrowed from Latin, but passed through several intermediate languages before arriving in Persian.

## Borrowing Path

"Borrowed from Ottoman Turkish كمرك (gümrük), borrowed from Byzantine Greek κομμέρκιον (kommérkion), borrowed from Latin commercium"

The Latin root **commercium** combines "con-" (together, with) and "merx" (merchandise), plus the suffix "-ium."

## Language Chain

1. **Latin** → *commercium*
2. **Byzantine Greek** → *κομμέρκιον* (kommérkion)
3. **Ottoman Turkish** → *كمرك* (gümrük)
4. **Persian** → *گمرک* (gumrok/gomrok)

The word means **"customs"** in Persian and belongs to the semantic field of taxation and trade regulation. This borrowing pattern reflects historical trade and administrative contact between Persian-speaking regions and Ottoman Turkish influence.
```


## [2026-09-07T16:21:40.999Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%B3r%C7%B5s",
 "prompt": "Reconstruction Proto-Indo-European *mórǵs: gloss, root, and list of descendants (Proto-Iranian, Proto-Germanic, Latin, Celtic). Quote the gloss exactly."
}
```


## [2026-09-07T16:21:42.305Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mercy",
 "prompt": "Etymology of \"mercy\": Old French merci, Latin mercedem/merces, the semantic shift to 'pity/thanks', and the ecclesiastical Latin use. Quote key phrases."
}
```


### [2026-09-07T16:21:44.886Z] TOOL RESULT

```
# Proto-Indo-European *mórǵs

**Gloss:** The root means "boundary" or "border."

**Root:** *mórǵs (oblique stem *mr̥ǵ-)

**Major Descendants:**
- Proto-Iranian: *marjah → Avestan marəza, Persian marz
- Proto-Germanic: *markō
- Latin: margō
- Proto-Celtic: *mrogis

The entry states: "Possibly derived from the verb underlying Hittite (mārki, 'to divide, separate')."
```


### [2026-09-07T16:21:49.428Z] TOOL RESULT

```
# Etymology of "Mercy"

The word "mercy" has undergone a fascinating semantic transformation across languages and centuries.

## Origin and Evolution

The term entered English in the late 12th century from Old French *mercit/merci*, which originally meant "reward, gift; kindness, grace, pity." This traces back to Latin *mercedem* (nominative *merces*), initially denoting "reward, wages, pay, hire." The root connection runs through *merx*, meaning "wares, merchandise"—the same source as the modern word "market."

## Semantic Shift

A crucial shift occurred in Vulgar and Medieval Latin. As noted in the source, the term evolved to mean "favor, pity" and later "thanks; grace." The meaning "disposition to forgive or show compassion" emerged by the early 13th century, followed by "an act or exercise of forbearance or good will" around 1300.

## Religious Application

Church Latin gave the word specific theological importance. Starting in the 6th century, "mercy" came to describe "the heavenly reward earned by those who show kindness to the helpless and those from whom no requital can be expected."

The phrase "at (one's) mercy" (meaning discretionary power) appeared by the mid-14th century, while the "Seat of mercy" referenced the Ark of the Covenant's golden covering, representing God's throne.
```


## [2026-09-07T16:21:55.503Z] TOOL CALL #33: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1986 2>&1 | head -60"
}
```


## [2026-09-07T16:21:56.172Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/margin",
 "prompt": "Etymology of \"margin\" and of \"march\" (border/frontier) and \"mark\" (sign) — quote the Latin margo / PIE root given."
}
```


### [2026-09-07T16:22:01.639Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 69; check the printed number and re-run with --pdf-page if off)
REF: BQT:1986  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 69  OCR-lang: fas

مردوی -۱۹۸۹-
عربان انان المین خواند .** بماند - و شخصیر| نیز کویند که سست وفرومایه
مردوس < بروزن افوس » کندنای کار و بیکار و «یچ کار اش وازوکاری برنیاید.
غامی راگویند - مرده سنگت * - بنم اول و فتح سین
مرده‌ری! - با رای بی‌نقطه(۱)پروزن ۱ بی نقطه » بمعنی مرداسنگه (۲) است و آن
-فره‌چی » مال و اسپابیرا گویند که از کی بسن | جوهری باشد که ازحرب سازند . زخمها راعلاج
از مردن مانده باشد وبعربی میرات خوانند. کند .
مرده دیگب ؟ - بازیادتی کاف.یمعنی هر ؟ - بفتح اول وسکون ثانی وزای
مرده ری باش د که مال ومیرائی امت که از کی | نقطه دار » زمین را کویند * - و زمینی را نیز
(۱) چل : بلرا . (7) چك : مرده سنگه (۷) . ۱
۹ - مخفف « مرده زیگه >:
بمرد وجهان مرده ری ماند از او شد آن کنج با شاهی و رنگه و بو.
۰ فردوسی طوسی « رشیدی > و رك : فهرست ولف.
۴ همرده‌ری (هم.) :
از خراج ارجمم آری رَر چو ریگ آخر آن از تو بماند مرده ریگ .
مولوی . « مثنوی چاپ علاء‌الدوله صس ۳4۱ >
۴ <مرداسنگه(۸.م.) ۳ مردارسنگه < مرتك(۸.م.) ۰ ۴ مرج اوستا -1267621
(سرحديك کشور) [اين‌کلمة اوستابی دریهلوی به 52821 (خانه »؛ مسکن) ترجمه شده «هوبشمان
4 پهلوی 028-[1327 . 338۳7-028 (کارنامه ۳۹ ) » ارمنی ع ۱۳38۲2 138۳28088.
کتی 122762 ( علامت سرحدی ) » ابرلندی قدرم ۳۵8 ۰ ۳۳۵۵۵ ۰ لاتینی 1332780
(حاشیه ,کنار) ۶ اسشق ۹۷۶ ۰ » ارمنی 31272 13 براهامیان > .
8 - همه سنگه خاراست آن کوه ومرز تهی بکسر از میوه وکشت ورز .
اسدی طوسی « رشیدی > .
هردن - بم اول وفتح سوم , از: مر دن ( پسوند مصدری ) . پپلوی 1217128.
«تاوادیا ۱۹۳ » ابرانی باستان -77187 (مردن) «بارتولمه۲ ۱۱۶ « نیب رکه ص۱۵۳ ۰ پارسی
باستان واوستا - 1327 (مردن) » هندی باستان - 77387 (مردن) » آرمنی 7116788170 (مردن)»
افغانی 12۴2 ۰ بلوچی 21۳88 ۰ 2217883 ۰ وخی 13271-270 ۰ 721711 » شغنی و سریکلی
0 اسشق ۹۷۳ . جزء اول‌کلمه دراوراق مانوی (پارتی) 339۷5۳ ( مر که )ءقس: اوستا
0 (85. 0 را و 1۸و 505 ...۳679180 1110016 ‎٩۶‏ اقن1 ۸ موعند11).
استی 2270 ( مرده ) ؛ 78۴18 ( کعتن ) . 1386118 ( مردن ) ۶ 4 . است ص ۰۲۱۲۹
کردی 239۳ (م رکه ) «زابا ص۳۹۲ . 729۳1 ( مرکه ) « ایشا ۰۳۹۹ 1370 (م رکه .
مرده ) « ایا ۰۳۹۳ ۹۶ 8 (مردن ) « انا ۰۳۹۹ ؛ فوت کردن ؛ وفات کردن .
درگذختن , جدا شدن روان از کالی کی .
(برهان قاطع ۳۲۵۱)
```


### [2026-09-07T16:22:05.585Z] TOOL RESULT

```
# Etymology of Margin, March, and Mark

Based on the Online Etymology Dictionary content provided, I can address the etymology of "margin":

**Margin** derives from "Latin _marginem_ (nominative _margo_) 'edge, brink, border, margin,' from PIE root *merg- 'boundary, border.'"

However, the source document does not contain etymological information for "march" or "mark." To provide accurate etymologies for those terms, I would need access to their respective dictionary entries, which are not included in the material above.

The Latin root *margo* clearly establishes the semantic connection to boundaries and edges that underlies the word "margin," but comparative analysis with "march" and "mark" cannot be completed using only this source.
```


## [2026-09-07T16:22:20.103Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mark",
 "prompt": "Etymology of \"mark\" (n. sign/boundary): Old English mearc, Proto-Germanic *marko, PIE root. Quote key phrases. Also any mention of \"remark\"."
}
```


## [2026-09-07T16:22:20.898Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mercury",
 "prompt": "Etymology of \"mercury\" and the god Mercury: is it from merx 'merchandise' or Etruscan? Quote key phrases."
}
```


### [2026-09-07T16:22:25.821Z] TOOL RESULT

```
# Etymology of "Mark"

## Primary Origin
The noun "mark" (meaning sign or boundary) descends from Old English *mearc*, deriving from Proto-Germanic *markō*, ultimately tracing to the PIE root *merg- meaning "boundary, border."

## Semantic Evolution
The word's meaning evolved progressively: "boundary" → "pillar or post marking a boundary" → "sign in general" → "impression or trace forming a sign." By around 1200, it referred to "any visible trace or impression."

## Key Historical Meanings
- **Late Old English**: A cross or character made by illiterate persons as a signature
- **Medieval period**: A tract of land held communally in England and Germany
- **1887**: The starting line in racing contexts (as in "on your marks")
- **1520s**: A characteristic or distinctive feature
- **1829**: A numerical grade given by teachers

## Notable Connection: "Remark"
While not explicitly detailed in this source, "remark" shares etymological roots with "mark," both involving the concept of "noting" or "observing"—the prefix "re-" intensifying the act of marking or noticing something.
```


### [2026-09-07T16:22:26.835Z] TOOL RESULT

```
# Etymology of Mercury: Origin Debate

The etymology of Mercury involves competing theories about its origin.

**The Latin/Commerce Theory:**
The name likely derives from Latin *merx* meaning "merchandise." According to the source, Mercury was "originally a god of tradesmen and thieves, from *merx* 'merchandise.'"

**The Etruscan Theory:**
However, scholars propose an alternative. The text notes that the god's name was "perhaps from Etruscan and influenced by *merx*." Additionally, de Vaan suggests "it possible the whole stem *merk-* was borrowed and the god-name with it."

**The Scholarly Consensus:**
Rather than a definitive answer, the evidence suggests both theories may have merit. One scholar observes that "the god's name was borrowed from Etruscan; in principle, the same is possible for the stem *merk-* altogether," indicating Etruscan borrowing with Latin semantic influence.

The uncertainty reflects genuine scholarly debate rather than a settled conclusion about whether Mercury's name originated from the Latin word for goods or from Etruscan sources—or potentially from both.
```


## [2026-09-07T16:22:35.439Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD marz\"; grep -n \"^marz\\|marz \\|marzbān\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB marz\"; grep -n \"marz\" NYB_vol2_glossary.txt | head -10; echo \"=== HRN marz\"; grep -n -i \"marz\" HRN.txt | head -10; echo \"=== HUB marz\"; grep -n -i \"marz\" HUB.txt | head -10"
}
```


### [2026-09-07T16:22:35.519Z] TOOL RESULT

```
=== PHD marz
PHD.txt:430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
PHD.txt:455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] abode, dwelling. ~ag [-k'] sedentary, settled. mānsār [mnsl = Av. ma0ra-] (holy) word, spell. -~-bar [-b/] priest. ~spand [-spnd = Av. spanta-] holy word; v. máraspand. imar [ml | M mr, N ~] number, reckoning, account; class. *mar [m/] scoundrel, felon. таг [ml | N ~] snake. mār-, —išn, v. mārdan., тагар [mik!] number. тпагар [mPk!] perceptive, sensitive. Māraspand [mrspnd | N ~] (= máns?rspand), cal. 29th day. *martabuk [mic”5wk'] brave, valiant. ~ith: bravery, valour. mard [GBRA < A gbr; mlt' | M m(y)rd, N ~) man. mārdan, màr- [ml-tn'] perceive, notice, feel. ~i$n: perception. „išnūmaud [-£rwmnd] perceptive. mardanag [mit?nk! | N ~a] manly, brave. ~ih: manliness, bravery. mardóm [ANŠWTA < A?niwt?; mltwm | M mrdwhm, N mardum] man, mankind, people. ~th: humanity, humanness. mardóm-zàádag [mltwm 2tk' | N mardum-zād] human being. ~ih: humanity. marģ [mlg | M mrg, N ~] death. ~-arzan [-lc’n'] deserving death. ~ih: = marg. --0mand [-”wmnd] mortal. mārīģ [m'Lyk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M mrz, N ~] boundary, march; astr. term. marzanģēūš [mlengws | N ~] marjoram. marzidan, marz- [mlc-ytn! | М mrzyst, mrz-] copulate. išn(īh): copulation, fornication. marz(o)bàn [mlcp’n' | № ~] margrave, warden of the marches. -masāy [-ms'd] suffix, -sized. mast [mst! | = M, N ~] bemused, intoxicated.
PHD.txt:1084:marz, sāmān,
PHD.txt:2742:marzipan lawzēnag.
PHD.txt:4830:marzobān marzišnīh marzišn mardānagīh mardānag marčābukīh marčābuk mard mardēm
PHD.txt:4850:marz- marcabukih marčābuk marzīdan
PHD.txt:4851:marzangūš
PHD.txt:5022:kundur kün künmarz kunjid kunjid kunišngar kunišn karak, kūk kūr
PHD_mackenzie.txt:3360:kiin-marz [kwnmle] sodomite; sodomy.
PHD_mackenzie.txt:3483:marz [mlc I M m"z, N~] boundary, march; astr. term.
=== NYB marz
1819:Paz., Skr. v. prativädin. < ham + *emäl < *abi-marda- (as to abi- > ē- cf éraxtan, éstatan), *marda- being the SW form of *_marza-, v. málitan and marzihistan.
2342:kün-marz [kwnmle'] sodomy, pederasty 777, 824. — NP kin ‘backside’ + marz, v. marzihistan.
2398:malitan [m'lytn'] to stroke 2119. — < *mard-. SW form of marz-, v. marzthistan ; NP mälidan. Inf. also muštan, pt. must < *mrsta-, e.g. Zsprm II, 9. III, 12, ef hištan: hil-.
2476:marzihistan [mlcyhstn'] pres. 3d p. pl. marzihénd [mleyhynd] they are in con- tact (astronomically : in conjunction) 511. — Pass. of marz-. Av. (1152 sq.) maraz- ‘to touch’; MPrs' mrz- ‘to copulate’, mrzyšn ‘eoition’, borrowed from NW, v. Verbum 170 (cf also kün-marz); the genuine SW form is *mard- > mäl-, v. mdlitan.
2477:marz-pän [mlep’n'] governor of a border district, margrave 1*. 115°. 117’. — Av. (1153) maraza- ‘border district’, MPrth mrz (A-H III, BBB) + pin ‘protector’, v. pünak; borrowed in Arm: marzapan, in Aram: Syr marzbänä = Talm, and in Arab: marzubün; NP marzbün.
2930:pänak [p'nk'] protector 521%, 66%, — M PrthPrs p’ng (cf BBB, Gl s.v.); NP panah (v. Steingass). Av. (888) pūna-; cf marz-pän, stör-pän.
5227:maé0ana-: mahmančh mahrka-: marg Mahrküsa: Markus maičyšna-: miyan maidy6.zaromaya-: maióyozarm mainyaoya-: mönöi mairya-: ?mar, mérak maxši-: *macäh Iman-: mčnitan, 6mét 2man-: mandan manah-: hešm-manihš Manuš-ciEra-: Manucihr maodanö.kara-: mustā- pät Imar- (mirya- morota-): murtan ?mar-: amar ?mar- + avis: ošmurtan maroz-: marzihistan maroza- -- pana-: marz- pan Maryu (Mouru-): Marv maršo.kara: "maškar mas-, Masan-: mas masya-: mahik mašya-: mart mafra-: mānsr mafra-sponta: mahras- pand (fra-)may-: framātan (ni-ymāy-: ni-mütan (pati-ymāy: patmān mazdayasna-: mazdēsn mazga-: mazg meroždā-, meroždika-: āmuržītan midaoxta- (mi€oxta): mitöxt miOra-: mihr
6045:mrw: ?murv mrz-: marzihistan mwrdy?ng: Mahlah mwrw: lmurv mwrw?: murvāk mwy'g: mödak my?n: miyàn myrd: mart mysg: hamésak mzd: mizd
7256:malax: Sak malidan: malitan mana: mānākēh mānistan: mānākēh māndagī: māndakēh mary: *murv marzbàn: marz-pàn mäyah: mātakēh mazah: micak
=== HRN marz
848:49. äniurzlden Verzeihen', ämarzis^ amurzlst (Qiss. Dan.).
849:aw. ä+i/'marz', ämarezen; iphlw, ümurzUan, ämurz(i)sn,
7601:phlv. kün, kün\marz.
8314:aw. [/^marz-, marezaiti 'fegt*; phlv. ktin\marz,
8315:dastän[marz, dösak[marz vd. 1 (18), marz(i)sn, 'Coitus*
8316:(Bund.) 2), marzUan 'coitiren*, mälUan, mCU(i)8n; ai.
8320:Vergl. Hübschmann, ZDMG. 44, 558; phlv. -marz
8466:phlv. marjpün bezw. marzpcin (Kärn. 36), arm. LW.
8467:marz^ marzpan.
8547:aw. [/^marz-j marezaiti *fegen'; phlv. mmt^ mmt
=== HUB marz
2173:marz) neben mitstan (von mrz) u. s. w. Oder sind auch
4287:= arm. dehpet (EliSe) = zd. danhupaiti- ; marzban *Mark-
4288:graf, phi. marzpdn, arm. marzpan; mobad == syr. NtCSIQ
5265:mard *Mann', marz 'Mark, Landstrich', mary *Gras, marg
7901:skr. war/ abwischen', osset. mdrzjn 'fegen', pers. marz
7902:reiberi' in phi. kun-marz u. s. w. H. 962, 7nustan reiben',
7961:np. amurzidan. phi. -marz,
8680:pers. General bei Fa list us, persischer Marzban von Ar-
9315:phi. -marz, zd. marez; iola 'Hagel, Reif* aus *kirdak H. 684;
9570:Vogel' = zd. mereya-] warz 'Mark*, vgl. arm. marzpan
```


## [2026-09-07T16:22:37.614Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT gümrük\"; grep -n -i \"gümrük\\|gumruk\\|kommerkion\\|commercium\" LKT.txt | head -10; echo \"=== SKT margin/mark\"; grep -n \"^margin\\|^mark\\|^merchant\\|^market\\|^mercy\" SKT.txt | head -10; echo \"=== SYN border\"; grep -n -i \"marz\\|mar.za\" SYN.txt IEC.txt | head -10"
}
```


### [2026-09-07T16:22:37.706Z] TOOL RESULT

```
=== LKT gümrük
1828:751.  Tk.  gümrük:
1829:'Zoll'  [aus  gr.  KO|U|u^pKiov,  lat.  commer- cium] ;  hieraus  bulg.  gumruk  'dass.,  Zoll- haus', serb.  dzumruk  'Zoll'.
5640:740 i^M/fe  730 gumruk  751
7427:earuba  832 carumba  832 Castrum  1117 cavilla  980 census  1050 centenarius  1178 cephalica  (vena)  1172 cer  Villa  1095 ciccum  434 cimiabaris  1827 cintra  1057 commercium  751 cophinus  1225 cribellum  673 cromm  1247 cummum  1046 cuppa  1225 cnpresstis  727 ci/c^as  1794.  1905 cywa  445 t«/^oZa  442
=== SKT margin/mark
8607:mark   (")   of  separation.
11128:mark  (i),  a  coin.  (E.)  M.  £,  mart, A.  S.  marc,  a  mark,  coin  ;  a  particular  use of  A.  S.  meartt  a  mark,  stomp,  &C'4-G. mark,  a  weight  of  silver,  a  coin :  Icel.  m&rk. marquo,  letters  of.  (F.*G.)  A Utter  of  marque  was  a  v<Tm\&^Qtv  \r)  % ntlcr  to  ooake  tvpiisaU  4iu  v\ui  gouBXri  ^
11443:merchant.  (F.— L.)    ME.  warcAiiw/.
23166:margin— raarpcot.  marge.
=== SYN border
IEC.txt:10337:mar$os, us, ó(n) “borderland, strip, baulk'. WP II, 283 Av. morozu 'borderland'; Per. marz ‘region’; Lat. margo, gs -inis, m. & f. ‘edge, bank’; Go. marka, f. ‘boundary; OHG marca "border. land, boundary’; MHG march, marke, f. id.; OE mearc, f., mierce, n. ‘boundary’; ON mork, gs markar, merkir, pl. markir, merkr, f. “for- est; Sw. mark, m. “earth, field, lang’. (Iso- phonic: Gk. márgos “wild”. Li. margas ‘acre’: R morg, id. are from Gmc. cf. G Morgen (Land))
IEC.txt:10346:mars- (marsó, io; marsos) ‘bad; be bad, err; wickedness, error'. Cf. mors- Hitt. mars- ‘be bad’; marsas ‘bad, corrupt’; Alb. í marrë ‘mad’; Arm. (?) cf. maš “outworn, old’; mašem ‘wear out, corrode’; Go. marzjan, v. “scandalize'; OE mearr “evil, deceptive’;
IEC.txt:10547:melĝð ‘caress, titillate, massage, milk’. Cf. ml£o and next. WP II, 298 Skt. cf. (z-gde) mrjámi ‘wipe; Av. marozai- (mi), id.; Tokh. AB malk-, v. ‘milk’; Gk. mélgo “massage, handle’; a-mélgo (*milk', fr. em": Thr. melg-, Illyr. mei. id.; Alb. mjel, aor: mola, id.; Lat. cf. (z-gde) mulgeo, id.; Olr. mligim, MIr. bligim, mod. bleaghaim, v. id. (z-gde as Lat.); W cf. ar-mael, m. ‘second milk; MHG mélken, mélchen, sv. 3 “milk; be in milk’; OE melcan, sv. 3. ‘milk’ beside (o-gde) melcian ‘milk; suckle’; ON mjólka, v. “milk; be in milk’; Du. melken, id.; OCS (z- gde) mlüzo, mlésti, id.; Li. mélZiu, -ti and (z- gde) inf. milZti, id. (The semantic association of ‘wipe’ and “milk? is apparent in Latvian Slauku, slaucit, v. ‘wipe’; slaucu, slaukt, v. “milk?). Cf. melgos, molg- and mlé-.
IEC.txt:11257:mré- (3) ‘harden, solidify, freeze’ Skt. cf. (ambig.) mūrčhāmi ('solidify', if fr. *mr&sko); Gk. margóno, v. “feel numb’; Alb. mardha, aor. ‘froze, felt cold’; cf. mërdhif, mérdhih, v. (*freeze, feel cold’, fr. *mrgisKo); OCS mrüZzo, mrüzati, & mrüzng, -noti, intr. ‘freeze’ beside mrüZza, f. ice; R mérznut, inf. as OCS; Pol. marznac, as OCS. (Variant in Arm. mardzem ‘coagulate’, fr. *mrgh-)
SYN.txt:12204:CHAPTER 8 th AGRICULTURE, VEGETATION! : . A 8.11 FARMER 8.44 Bariey ac : 8.12 Frexp (for Cultivation) 845 Rys dl ¢ 8.13 GarRDEN 8.46 Oats i ‘a 8.14 Barn 8.47 Marzz, (U.S.) Corn q 8.15 Cuurivats, TLL 8.48 Rice Me ; 8.21 Pxow (vb.; sb.) 8.51 Grass ht : 8.212 Furrow 8.52 Hay a i 8.22 Dic 8.53 PLant al 8.23 SpavE 8.54 Roor ( 8.24 SHovEL 8.55 Brancu ba 8.25 Hor 8.56 Lear ere 8.26 Tork 8.57 FLowER me 8.27 Raks 8.58 Rosz M 8.28° Harrow 8.60 Tree = 1.42 * 8.31 Sow; Srep 8.61 Oak 8.32 Mow, Reap a oe Bo 8.33 Sickie; ScyrHE 8, 64 ei i 8.34 THREsH 8.65 = t in ? 8.35 TsresHinc-Foor 8.66 hee 8.41 Crop, Harvest 8.67 VINE mS 8.42 Grarn (Generic = British Corn) 8.68 Tosacco ‘co 843 Wxeat 8.69 SmoxE (Tobacco) (6. ink 8.11 FARMER - Grk. — -yewpyés Goth. (airpds) waurstwja i ikini ini : . Lith kininkas, laukinin- NG —-yewpyds, xwpixds, ON bondi, akrmasr, to, ieee a i fal Ra Lat. aa Dan. — dyrker, landmand, Lett. laucinieks, zemnieks Ia Hiesehee “aactnctiorglontts bonde ChSI. délatelt, tezatelt the : as ae iiva- Sw. dkerman, jordbru-  SCr. __ratar, teak, seljak 1 Tr ant re fee kare, bonde Boh. __rolnik, sedldk i ; 4 ee pied tiva- OE = (eord)tilia, wcerman, Pol. _rolnik, chlop It Sp Waban RUE gebir, etc. Russ. zemledelec, krest'ja- thi pes f r “i agricultor ME husbond(man), acre- nin, muzik DD Ir, : eke He abe man Skt. ksetrakarsaka-, P Nir. paecmba ugar Ne eld (husbandman) kselrapati- W. amaethwr, ffermur OHG ee ae Av. vdstrya-
SYN.txt:29495:afmarzeins, liutet, Lith. apgaulé, apgavas lists Lett. krapSana, viliana
SYN.txt:29522:4. Goth. afmarzeins (&rérn), fr. af- marzjan, marzjan ‘cxavdaditw, offend’ : OE mierran ‘hinder’, OHG merren ‘hin- der, vex’, MHG marren ‘delay’, outside connections dub. Feist 347. Walde-P. 2.279.
SYN.txt:30981:1. IE *mers-, perh. the same as in Goth. marzajan ‘vex’, OE mierran, OHG merren ‘vex, bother, hinder’, etc., and fr. an extension of *mer- ‘rub’ (Skt. mr- ‘crush’, etc.). Walde-P. 2.279.
SYN.txt:32947:OHG marcha, MHG marke : Lat. margo ‘edge’, Ir. mruig, bruig ‘cultivated land, district’, Av. maraza- ‘borderland’ (Barth. 1153; NPers. marz ‘borderland, district’).
```


## [2026-09-07T16:22:52.748Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 8455-8475\"; sed -n '8455,8475p' HRN.txt; echo; echo \"=== BRT context 20085-20100\"; sed -n '20085,20100p' BRT.txt"
}
```


### [2026-09-07T16:22:52.811Z] TOOL RESULT

```
=== HRN 8455-8475
gel. wardmy mäz. bamardeni.
ap. l^mar-y amariyata 'sterben ; aw. 1/^mar-, fra-
mairy^it^; phlv. murtan^ nilret (vd. 5 (134) Gl.); ai.
[/^mar-^ mriydte 'sterben ; arm. meranim 'sterben' (H.
No. 195).
kurd. wmn 'sterben ; aiy.mral; oss. mälin 'sterben'
(178b), d. märiin, t. marin 'morden, tödten* (178c);
bei. mirag, n. miray (237); wa/. mari-am, mlrlt^ §iyn.
sar. mTram.
974. merz 'Landstrich*, Mark*, merj, merzban.
(aw.) merezu' *boundary of a country' (ZPGl.)^);
phlv. marjpün bezw. marzpcin (Kärn. 36), arm. LW.
marz^ marzpan.
got. marka 'Mark'; air. mruig, bruig; lat. margo
Rand' (weiteres bei Froehde, BB. VII, 327).
975. mury 'Vogel; Huhn, mury[abi 'Ente ^).
mäz. wary.
aw. mereya- 'Vogel'; phlv. mury, murv (auch Papyrus,
Hörn, ZDMG. 43, 51)^); ai. mrgd- 'Waldtiej-; Vogel*.
kurd. vergl. miräwi 'Ente* (H.-Sch.); afy. marya;
oss. d. t. mary 'Vogel* (179); bei. (LW.?) murg, n.

=== BRT context 20085-20100
dby  Google
"53
:i54
. .  frampr^öii  V.$.  4a.  3)  '(einen  Ver- trj^  aufheben':  vaii.,mi^r3m  kirmaoiti *zastS.mat5 .  .framinzaUi . .  antar^  urvaitya (sA.)  frada^aifi  V.4.3;  sf.*.  4)  'fgrt-
fliegen':  dz'a  ämarvtsn  dva  vJmamin  äva framanssn  (statt  Du.)  "die  zwei  (Federn) sollen  auf,  , .  hin  und  her, . .  fortfliegen" Yt.  14.  4S-
mit  nj\  s.  Inf.
mit  vi  hin  und  herfliegen':  dva  ämars- zm  .  .  vlinartan  . ,  framanzin  (sd.)  Yt, '4- 45-,
a\.  marfli,  m^Jinü,  ni-mfTijyät\  Cip.  mälidan 'reiben',  woss.  märsin  '(egen'.  —  Vgl.  miriiää-. —  Pü.  (mit/z-a): /™/  mätUan,  (mit  alfä):  afar ..  däi  d^är  ('Mauer');  Npü.  {lu  Yt.  14.  45): mälii  äiäa»,  [in  YL  14.  21):  dar  man.  — ')  Nur  im  Inf.
•  j.  maraza-  m.  'Mark,  Grenzgebiet*: anusi^  plrftn  "z^m  avahistäl  "zwangs- weise soll  er  sich  in  das  äusserste  Grenz- gebiet" begeben"  V.  ^.  5^1.
mp.,  np.  man.  —  Pu. :  a^arsandihä  fa  an /röltiim  mars  äff  tslind;  Erl.  undeutlich.  — ■)  Wo  ei  wegen  der  anruhigen  Nachbuschaft Km  gefährlichsten  isl.
j.  marixämyeke  Yt.  /j.    126  !ie»  mim'.
■  j.  maräaona-  Adj.  'mit  (dem  Dana) Mariavan  in  Verbindung  stehend,  von ihm  henlihrend':  ihye/O  'tarn  V.i^.i,  i, 43;  —  ihyejaKkS  'nahe  yt6.4;  13.  130.
Ableit.  aus  martavan-.  —  PO. :  sei  i  iiikäi,  ratvan, Npü.:  marg i »Ulan  äyanda.  So.:  mftyiir gvfla-
•  j.  maräavan-  m.  Name  eines  Dafva*^: k:j  atti  i^yejä  'saonS  "welches  sind  die Gefahren  (von  Seiten)  des  M.V  V.  iS.  8  '>.
»)  Der  den  Abfall  vom  rechten  Glauben  be- wirkt; vgl.  V.  iS.  9  und  und  unten  iEL
Abieil.  —  marsa<van-  eig,  'das  Vergessen  be- wirkend';    %.     GDN.     KZ.     2$.     405;     »gl-     "■     •^'"^^
```


## [2026-09-07T16:23:07.557Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=22940 && NR<=22975' KLN_1966.txt | grep -n \"^[0-9]\\{3\\}\\|9[34][0-9]\" | head; echo \"---- page markers near\"; sed -n '22930,22965p' KLN_1966.txt | grep -o \"\\b9[0-9][0-9]\\b\" | head"
}
```


## [2026-09-07T16:23:08.839Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/merchant",
 "prompt": "Etymology of \"merchant\", \"market\" and \"commerce\" — quote the Latin chain (mercari, mercatus, merx, commercium) and the routes through Vulgar Latin / Old French / Old North French."
}
```


### [2026-09-07T16:23:08.980Z] TOOL RESULT

```
22:940
29:941
---- page markers near
940
```


### [2026-09-07T16:23:14.489Z] TOOL RESULT

```
# Etymology: Merchant, Market, and Commerce

## The Latin Chain

The words "merchant," "market," and "commerce" share a common Latin root system:

**Core Latin terms:**
- *mercari* — "to trade, deal in, buy"
- *mercatus* — "trading, buying and selling; trade; market"
- *merx* (genitive *mercis*) — "wares, merchandise"

## Word Evolution

**Merchant** derives from Anglo-French *marchaunt*, which came from Vulgar Latin *mercatantem*, a present participle form of *mercatare* (a frequentative of *mercari*). The noun emerged in early 13c. as "one engaged in the business of buying commercial commodities and selling them again for profit."

**Market** developed from Old North French *market*, itself derived from Latin *mercatus*. First documented in early 12c., it originally meant "a meeting at a fixed time for buying and selling livestock and provisions."

## Possible Etruscan Origin

Scholars suggest the Italic root *merk-* underlying these terms "possibly from Etruscan," indicating the ultimate source may predate Latin itself.
```


## [2026-09-07T16:23:22.201Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%AF%D9%85%D8%B1%DA%A9/",
 "prompt": "Show the \"فرهنگ معین\" (Mo'in) entry for گمرک, including any bracketed origin tag such as [ایتالیایی], [تر.], [فر.], and the Dehkhoda etymology if present. Quote the Persian text."
}
```


## [2026-09-07T16:23:23.516Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B1%D8%B3%DB%8C/",
 "prompt": "Show the \"فرهنگ معین\" (Mo'in) entry for مرسی, including any bracketed origin tag such as [فر.] (French). Quote the Persian text."
}
```


### [2026-09-07T16:23:28.062Z] TOOL RESULT

```
# "فرهنگ معین" Entry for مرسی

According to the Farhang-e Mo'in dictionary section on this page, the entry is:

**(مِ ) [فر.] (فعل . ) متشکرم ، ممنونم**

The bracketed tag [فر.] indicates French origin. The definition translates to "thank you" or "I am grateful," presented as a verb form with synonyms meaning "I thank you" and "I am obliged."
```


### [2026-09-07T16:23:30.555Z] TOOL RESULT

```
# فرهنگ معین Entry for گمرک

According to the Mo'in Dictionary section on this page, the entry reads:

"(گُ رُ ) (اِ. ) [ مأخوذ از ترکی ] ۱ - اداره ای که مأمور مراقبت از ورود و خروج کالاها (بر اساس قانون واردات و صادرات ) و دریافت حقوق گمرکی از دارندگان آن هاست . ۲ - هزینه ها و حقوق گمرکی ."

**Key details:**
- The bracketed origin tag indicates the word is derived from Turkish: **[مأخوذ از ترکی]** (borrowed from Turkish)
- The entry provides two primary definitions: (1) an administrative agency overseeing imports/exports and collecting customs duties, and (2) customs fees and duties themselves
- The Dehkhoda etymology traces the Greek root "kommerks" or "kommerkī," noting its adoption into Turkish after Constantinople's conquest, and subsequently into Persian
```


## [2026-09-07T16:23:49.765Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/g%C3%BCmr%C3%BCk",
 "prompt": "Turkish gümrük: give the etymology as Nişanyan states it (Greek kommerkion, Latin commercium), with dates of first attestation."
}
```


## [2026-09-07T16:23:51.389Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B1%DA%A9%D9%88%D8%B1%DA%A9%D8%B1%D9%85/",
 "prompt": "Show any dictionary entry for مرکورکرم and مرکور — origin tag (French?), meaning. Quote the Persian text."
}
```


### [2026-09-07T16:23:53.827Z] TOOL RESULT

```
I appreciate your question, but I must be honest: the web page content provided doesn't actually contain the etymological information you're requesting. 

The page shows only the header and footer of Nişanyan Sözlük (Nişanyan Dictionary), including navigation elements and copyright information. It doesn't include the dictionary entry for "gümrük" itself, which would contain the etymology, Greek/Latin origins, and attestation dates you're asking about.

To provide the etymology as Nişanyan states it, I would need the actual dictionary entry content, which isn't present in the material supplied.
```


### [2026-09-07T16:23:56.840Z] TOOL RESULT

```
# Dictionary Entry: مرکورکرم (Mercurochrome)

## Origin
The term comes from English "Mercurochrome," a trade name for the chemical compound merbromin (مربرومین).

## Meaning
According to the Dehkhoda Dictionary:

> "محلولی است که تقریباً دارای 26 درصد مرکور (جیوه) است"

(A solution containing approximately 26% mercury)

It's an antiseptic medication prepared in 1919 by Hugh H. Young and White. The dark red solution is used for disinfection through injection and topical application on wounds.

## Related Term: مرکور
The entry doesn't provide a separate definition, but "مرکور" refers to mercury (جیوه in Persian), the heavy metallic element that comprises about 26% of the mercurochrome compound.

**Note:** The U.S. FDA removed mercurochrome from the safe drug list in 1998 due to mercury toxicity concerns.
```


## [2026-09-07T16:24:08.615Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 mereg\"; grep -n \"mereg\\|mar.zu.*Grenz\\|margo\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-07T16:24:08.665Z] TOOL RESULT

```
=== WLD Bd2 mereg
13353:Zup. G. 198 zu ir. "^mruig^ lat. margo als ^mreng-),
17974:stehende leichte Wzform *meregh^ *m(o)rogh-j sondern ist gleichartig mit
18435:8udle“ (dies kaum zu meregh- „benetzen‘^).
18459:meregh- „benetzen, rieseln“.
38735:   ksl. pohromh ,,margo panni"', russ. kromd „Bi’otschnitt Ende des Brotes,
```


## [2026-09-07T16:24:10.075Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 alt\"; grep -n \"merek\\|mereĝ\\|Grenzgebiet\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20"
}
```


### [2026-09-07T16:24:10.122Z] TOOL RESULT

```
=== WLD Bd2 alt
17832:mcrcdih „dammern^; wohl auch (s, Berneker II 38) merekT* „Phanta- 
18455:av. maroza- m. „Grenzgebiet": lat. maygo, -hiis „Rand''; air. my'uig,
```


## [2026-09-07T16:24:15.056Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18450,18462p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \"=== page tag\"; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd2_pages.txt | awk -F'[][]' 'NR>0' | head -0; grep -n \"av.  maroza\\|maroza- m\" incoming/WLD/WLD_Bd2_pages.txt | head -3"
}
```


### [2026-09-07T16:24:16.365Z] TOOL RESULT

```
Wegen des Yokalverhaltnisses zweifelhaft ist die Zugehorigkeit folgender 
W^orte, die unter idg. ^yyiareg- oder "^yyiarog- (Hirt Abl. 127) vereinbar 
waren und Bedeutungsentwicklung von „8treichen, streifen" zu „Rand 
(woran man streift), Streifen, Landstrich, Grenzstreifen'' voraussetzen wiirden; 

av. maroza- m. „Grenzgebiet": lat. maygo, -hiis „Rand''; air. my'uig, 
Irukj {^ynrogk) „Mark, Landstrich", cymr. corn. bret. Iro „Bezirk", hy'ogae 
Galli agrum dicunt (Schol. zu Juvenao YIIT 231), gall. Brogi-ryiaros, Alio- 

Walde, Etymologisches Worterbuch. IF. 19 



=== page tag
18708:   av. maroza- m. „Grenzgebiet": lat. maygo, -hiis „Rand''; air. my'uig,
```


## [2026-09-07T16:24:25.011Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=18708 && /\\[pdf page/ {p=$0} END{}' incoming/WLD/WLD_Bd2_pages.txt; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1<18708' | tail -2; sed -n '18690,18712p' incoming/WLD/WLD_Bd2_pages.txt | grep -n \"28[0-9]\""
}
```


### [2026-09-07T16:24:26.329Z] TOOL RESULT

```
23:284                                                           mei-
```


## [2026-09-07T16:24:30.447Z] TOOL CALL #50: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T16:24:30.485Z] TOOL RESULT

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


## [2026-09-07T16:24:39.651Z] TOOL CALL #51: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%B2' \\\n 'https://en.wiktionary.org/wiki/merx' \\\n 'https://en.wiktionary.org/wiki/%DA%AF%D9%85%D8%B1%DA%A9' \\\n 'https://en.wiktionary.org/wiki/Mercurius' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%B3r%C7%B5s' \\\n 'https://www.etymonline.com/word/mercy' \\\n 'https://www.etymonline.com/word/margin' \\\n 'https://www.etymonline.com/word/mark' \\\n 'https://www.etymonline.com/word/mercury' \\\n 'https://www.etymonline.com/word/merchant' \\\n 'https://abadis.ir/fatofa/%DA%AF%D9%85%D8%B1%DA%A9/' \\\n 'https://abadis.ir/fatofa/%D9%85%D8%B1%D8%B3%DB%8C/' \\\n 'https://abadis.ir/fatofa/%D9%85%D8%B1%DA%A9%D9%88%D8%B1%DA%A9%D8%B1%D9%85/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 337, roots Merg/Merk: marz, margo, mark, merx, gomrok, merci, mercury' 2>&1 | tail -2\ndone"
}
```


### [2026-09-07T16:24:50.403Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4b6e8ff2480facba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/db61a16d57e3e704.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7bddd1a7a2c43a69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5ed859b2ea93ee87.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9185ee66980ec65.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c96c7b36f259b5cc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d96d2fd4521ce524.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1d9663988012e950.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/484a5b8c338410a6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fca901f2f05b012a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c968f9aba11f0d2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d478872a2615da54.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6f68c6324fec6dd8.txt
```


## [2026-09-07T16:26:10.467Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT margin/march/mark2\"; grep -n \"margin\\. \\|march  (\\|march (\\|mark  (2)\\|mark (2)\\|remark\\. \\|mercy\\. \\|market\\. \\|commerce\\. \\|mercury\" SKT.txt | head -15"
}
```


### [2026-09-07T16:26:10.512Z] TOOL RESULT

```
=== SKT margin/march/mark2
11125:march  (1).  a  border,  frontier.  (E ) M.  E.  marcke.  —  A.  S.  mcarc,  a  mark, boundary.
11433:form  of  market. lamlec  t.  1.  74*  Prob.  in X.  mmrk/t  market  (of  Luiin mve.
11445:mercury.  q»ick«ilver.  (F.  — O  ME. mtrcurie,  quicksilver, narard  after  the  planet Mercury.  —  O.  F.  Me*xurit  U  Norman foim^;  F.  mtrcure.  —  L.  Mtrcunnm,  ace, of  Mircurius,  Mercnr)*,  god  of  tiaftic.  •■  L. mer<;  item  of  merx,  merchandise.
23160:march  (i> — ^mark  (x),  mar-
```


## [2026-09-07T16:26:11.881Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD mercury/margin\"; grep -n \"Mercurius\" FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head -6; echo \"=== ARY marz\"; grep -n \"مرز\" incoming/ARY/ARY_pages.txt | head -8"
}
```


### [2026-09-07T16:26:11.950Z] TOOL RESULT

```
=== FSD mercury/margin
=== ARY marz
208:مرز میان اين دو دسته زبان هند و اروپایی خطی است که حدوداً در مرکز اروپا قرار دارد. حال اگر
210:خواهیم رسید که مرکز تغل باگرانیگاه (67۸۷17۷ 05 032۲788) این موج‌ها در حدود مرز... |
231:این دوگروه حا کی از وجود خاستگاه هند و اروپائیان در حدود مرز میان این دو گروه است.
659:پاسداری مرزهای امپراتوری روم در شمال انگلستان؛ به استخدام رومیان درآمدند
844:و از باختر تا مرز باختری لهستان و از جنوب تا بلفارستان و مقدونیه را تصرف کردند. تاریخ احتمالی
1191:اخص توسط دانشمندان برونمرزی (بارتولومه» یونگر» هنینگه» نیبرگ) در چند دهه قبل آغاز شد.
1192:استادان ایرانی نیز (به ویژه معین و خانلری و پورداود) با بهره گیری از پژوهشهای برونمرزیان امن ۱
4031:روسی ((7551۸:): رل اد ند برش 191 مرزی 8۱/۸۱
```


## [2026-09-07T16:26:19.145Z] TOOL CALL #54: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg337.png data/verification/sources/refs/ocr/BOOK/337.png && ls -la data/verification/sources/refs/ocr/BOOK/337.png"
}
```


### [2026-09-07T16:26:19.204Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60414 Sep  7 12:26 data/verification/sources/refs/ocr/BOOK/337.png
```


## [2026-09-07T16:28:06.116Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:38:34.418Z] TOOL CALL #55: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk337.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_MORGS = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%B3r%C7%B5s\"\nW_MARZ  = \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%B2\"\nW_MERX  = \"https://en.wiktionary.org/wiki/merx\"\nW_GOM   = \"https://en.wiktionary.org/wiki/%DA%AF%D9%85%D8%B1%DA%A9\"\nW_MERC  = \"https://en.wiktionary.org/wiki/Mercurius\"\nE_MERCY = \"https://www.etymonline.com/word/mercy\"\nE_MARGIN= \"https://www.etymonline.com/word/margin\"\nE_MARK  = \"https://www.etymonline.com/word/mark\"\nE_MERCUR= \"https://www.etymonline.com/word/mercury\"\nE_MERCH = \"https://www.etymonline.com/word/merchant\"\nA_GOM   = \"https://abadis.ir/fatofa/%DA%AF%D9%85%D8%B1%DA%A9/\"\nA_MERSI = \"https://abadis.ir/fatofa/%D9%85%D8%B1%D8%B3%DB%8C/\"\nA_MKRM  = \"https://abadis.ir/fatofa/%D9%85%D8%B1%DA%A9%D9%88%D8%B1%DA%A9%D8%B1%D9%85/\"\n\nPOK738 = (\"Pokorny IEW p. 738 (POK_02.txt leaf 400, printed no. 738 on the leaf): \"\n          \"„mereg- ,Rand, Grenze‘. Npers. marz ,Landstrich, Mark‘; lat. margö, -inis ,Rand, Grenze‘ \"\n          \"… got. marka f. ,Grenze‘, ahd. marc(h)a ,Grenze, Grenzland‘, ags. mearc ds. … \"\n          \"WP. II 283 f., WH. II 39 f.“\")\nPOK739 = (\"Pokorny IEW p. 739 (POK_02.txt leaves 401–402): the root is printed „merḵ- ,fassen, ergreifen‘“ \"\n          \"with Ai. mṛśáti ,berührt, faßt an‘, gr. μάρπτω; then „fraglich ist Zugehörigkeit von \"\n          \"lat. merx ,Ware‘, merces, -edis ,Preis, Lohn, Sold‘, mercārī ,handeln‘“ — i.e. Pokorny lists \"\n          \"Nourai's whole Latin family here but calls the connection doubtful.\")\nAHD_MERG = (\"AHD_watkins1985.txt l.757: “merg-. Boundary, border. 1. Germanic *mark-, boundary, border \"\n            \"territory; also to mark out a boundary by walking around it … a. Old English mearc … MARK; \"\n            \"c. Old French marc, marche, border country: MARCH2, MARQUEE, MARQUIS … 2. Germanic *markja- … \"\n            \"MARQUETRY; REMARK … 4. Latin margo, border, edge: MARGIN. [Pok. mereg- 738.]”\")\nAHD_MERK = (\"AHD_watkins1985.txt l.760: “[merk-2. Italic root, possibly from Etruscan, referring to aspects \"\n            \"of commerce. 1. Latin merx (stem merc-), merchandise (> mercāri, to trade): MARKET, (MART), \"\n            \"MERCER, MERCHANT; COMMERCE. 2. Latin merces, pay, reward, price: MERCENARY, MERCY. 3. Probably \"\n            \"Latin Mercurius, the god of (inter alia) commerce: MERCURY. [In Pok. merk- 739.]]” — the square \"\n            \"brackets are Watkins's mark for a NON-Indo-European root.\")\nWLD283 = (\"Walde-Pokorny II 283 (WLD_Bd2_1927_dli_106624_djvu.txt l.18450-18455, printed 283/284): \"\n          \"„Wegen des Vokalverhältnisses zweifelhaft ist die Zugehörigkeit folgender Worte, die unter \"\n          \"idg. *mareg- oder *marog- … vereinbar wären … av. marəza- m. ,Grenzgebiet‘: lat. margo, -inis \"\n          \",Rand‘; air. mruig, bruig (*mrogi-) ,Mark, Landstrich‘, cymr. corn. bret. bro ,Bezirk‘“\")\nIEC_MARG = (\"Mann IEC.txt l.10337: “marǵos, us, ó(n) ‘borderland, strip, baulk’. WP II, 283 Av. mərəzu \"\n            \"‘borderland’; Per. marz ‘region’; Lat. margo, gs -inis ‘edge, bank’; Go. marka, f. ‘boundary’; \"\n            \"OHG marca ‘border, land, boundary’; OE mearc ‘boundary’”\")\nSYN_MARG = (\"Buck SYN.txt l.32947 (ch. 19 ‘boundary’): “OHG marcha, MHG marke : Lat. margo ‘edge’, \"\n            \"Ir. mruig, bruig ‘cultivated land, district’, Av. marəza- ‘borderland’ (Barth. 1153; \"\n            \"NPers. marz ‘borderland, district’)”\")\nBRT1153 = (\"Bartholomae AiW col. 1153/54 (BRT.txt l.20093): „j. marəza- m. ,Mark, Grenzgebiet‘: \"\n           \"anušiḵ … „zwangsweise soll er sich in das äußerste Grenzgebiet begeben“ V. 3.5‘; \"\n           \"mp., np. marz“ — Young Avestan, Vendidad 3.5.\")\nNYB_MARZ = (\"Nyberg, Manual of Pahlavi II, s.v. marz-pān (NYB_vol2_glossary.txt l.2477): “marz-pān \"\n            \"[mlcp’n’] governor of a border district, margrave … Av. (1153) marəza- ‘border district’, \"\n            \"MPrth mrz … + pān ‘protector’ … borrowed in Arm: marzapan, in Aram: Syr marzbānā … \"\n            \"and in Arab: marzubān; NP marzbān”; s.v. marzihistan (l.2476) he keeps the homonymous \"\n            \"Av. marəz- ‘to touch’ (AiW 1152) apart from it.\")\nPHD_MARZ = (\"MacKenzie CPD s.v. marz (PHD.txt l.455 / PHD_mackenzie.txt l.3483): “marz [mlc | M mrz, N ~] \"\n            \"boundary, march; astr. term”; and “marz(o)bān [mlcp’n’ | N ~] margrave, warden of the marches”.\")\nHRN974 = (\"Horn, Grundriss no. 974 (HRN.txt l.8465-8469): “974. merz ,Landstrich‘, ,Mark‘, merj, merzban. \"\n          \"(aw.) merezu ,boundary of a country‘ (ZPGl.); phlv. marjpān bezw. marzpān (Kärn. 36), arm. LW. \"\n          \"marz, marzpan. got. marka ,Mark‘; air. mruig, bruig; lat. margo ,Rand‘” — note Horn too writes the \"\n          \"Avestan word with e (merezu), as Nourai does.\")\nHUB_MARZ = (\"Hübschmann, Persische Studien (HUB.txt l.5265) lists “mard ,Mann‘, marz ,Mark, Landstrich‘, \"\n            \"mary ,Gras‘“ among the inherited Persian words, and (l.4287-88) “marzban ,Markgraf‘, phl. marzpān, \"\n            \"arm. marzpan”.\")\nBQT1986 = (\"Borhan-e Qāte‘ ed. Mo‘in p. 1986, s.v. مرز, footnote 4 (fetched with tools/ref_page.py BQT:1986 = \"\n           \"BQT_v4_picofile.pdf p. 69): «مرز اوستا marəza- (سرحدِ کشور) [این کلمة اوستایی در پهلوی \"\n           \"به … (خانه، مسکن) ترجمه شده «هوبشمان»] پهلوی marz، marz-bān (کارنامه ۳۹)، ارمنی marz، marzpan، \"\n           \"گوتی marka (علامت سرحدی)، ایرلندی قدیم mruig، لاتینی margo (حاشیه، کنار)» — exactly Nourai's arrow \"\n           \"Avestan → Persian.\")\nKLN940 = (\"Klein, Comprehensive Etym. Dict. p. 940 s.v. mark (KLN_1966.txt l.22960; the page marker ‘940’ stands \"\n          \"on that leaf): “ME. merke, marke, fr. OE. mearc, ‘boundary, boundary sign, sign, mark’, rel. to \"\n          \"ON. merki … OFris. merke, OS., Goth. marka, ‘boundary, frontier’ … OHG. marcha, MHG. marke, \"\n          \"G. Mark … and cogn. with Avestic marǟza, ‘border’, L. margo, gen. marginis, ‘edge, brink, border’, \"\n          \"OIr. mruig, … ‘boundary; district’ … Cp. also march, ‘boundary’ … remark. Cp. also margin.”\")\nKLN_MERC = (\"Klein s.v. mercantile (KLN_1966.txt l.23519): “L. mercans … pres. part. of mercari, ‘to trade, \"\n            \"traffic, buy, purchase’, fr. merx, gen. mercis, ‘merchandise, wares’, which is of uncertain origin.”\")\nKLN_MERCUR = (\"Klein s.v. Mercury (KLN_1966.txt l.23534): “L. Mercurius, fr. Etruscan *Mercura, a divinity \"\n              \"introduced from Etruria into Rome about the end of the sixth century B.C.E. (see Ribezzo …); \"\n              \"prob. not related to L. merx, gen. mercis, ‘merchandise’.”\")\nKLN_MERCY = (\"Klein s.v. mercy (KLN_1966.txt l.23536): “ME. merci, fr. OF. mercit, merci (F. merci), fr. \"\n             \"L. mercedem, acc. of merces, ‘hire, pay, reward’ (in VL. also ‘favor, pity’), fr. merx, gen. mercis, \"\n             \"‘merchandise, wares’. It. merce, Sp. merced, ‘favor, grace, mercy’, also derive fr. L. mercedem.”\")\nKLN_MKT = (\"Klein s.v. market (KLN_1966.txt l.22964): “ME., fr. ONF. market, corresponding to OF. marchiet, \"\n           \"marché … fr. L. mercatus, ‘trade, business, marketplace’ [whence also It. mercato … Sp. and Port. \"\n           \"mercado … OHG. markat] … fr. mercatus, pp. of mercari, ‘to trade’, fr. merx, gen. mercis”; and \"\n           \"s.v. commerce (l.8369): “F., fr. L. commercium … fr. con- and merx, gen. mercis, ‘merchandise’.”\")\nLAT_MERX = (\"Ernout-Meillet, Dict. étym. lat. pp. 712–713 (LAT.txt l.37746, l.37780; index l.8918): \"\n            \"“merx (mers …), mercis f.: marchandise … Ancien, usuel”; under Mercurius: “Le suffixe de \"\n            \"Mercurius est le même que celui de Titurius, Mamurius, Veturius (étrusque?) … Pas d’étymologie \"\n            \"sûre, bien que merx ait une forme archaïque”; the index line reads “merx, autres types rares, \"\n            \"sans étymologie i.-e. sûre”.\")\nLKT751 = (\"Lokotsch no. 751 (LKT.txt l.1828-29): “751. Tk. gümrük: ‘Zoll’ [aus gr. κομμέρκιον, lat. \"\n          \"commercium]; hieraus bulg. gumruk ‘dass., Zollhaus’, serb. džumruk ‘Zoll’.”\")\nHJB384 = (\"Hobson-Jobson p. 384 s.v. GOMBROON (HJB.txt l.10351 ff.): “The name is said (in the Geog. \"\n          \"Moẓhanne, i. 17) to be Turkish, meaning ‘a Custom House.’ The word alluded to is probably gumruk, \"\n          \"which has that meaning, and which is again, through Low Greek, from the Latin commercium. But this \"\n          \"etymology of the name seems hardly probable. That indicated in the extract from A. Hamilton below is \"\n          \"from Pers. kamrūn, ‘a shrimp,’ or Port. camarão, meaning the same.” Hamilton 1727 (quoted there): \"\n          \"the Portuguese named it “in Derision, because it was a good place for catching Prawns and Shrimps, \"\n          \"which they call Camerong”.\")\nSKT_MARCH = (\"Skeat SKT.txt l.11125: “march (1). a border, frontier. (E.) M.E. marcke. — A.S. mearc, a mark, \"\n             \"boundary.”\")\nSKT_MERCUR = (\"Skeat SKT.txt l.11445: “mercury. quicksilver. (F.—L.) ME. mercurie, quicksilver, named after \"\n              \"the planet Mercury. — O.F. Mercurie … F. mercure. — L. Mercurium, acc. of Mercurius, Mercury, god \"\n              \"of traffic. — L. merc-, stem of merx, merchandise.”\")\nMON_GOM = (\"Mo‘in, Farhang-e Fārsi s.v. گمرک (p. 3392 of the 6-vol. print; text read on abadis.ir): \"\n           \"«(گُ رُ) (اِ.) [مأخوذ از ترکی] ۱- اداره‌ای که مأمور مراقبت از ورود و خروج کالاها … و دریافت حقوق \"\n           \"گمرکی از دارندگان آن‌هاست. ۲- هزینه‌ها و حقوق گمرکی.» — the origin tag is ‘from Turkish’, and the \"\n           \"Dehkhoda entry on the same page traces it to Greek kommerki(on), adopted by Turkish after the \"\n           \"conquest of Constantinople and thence into Persian. No Italian or Portuguese step.\")\nMON_MERSI = (\"Mo‘in s.v. مرسی (p. 4015 of the print; text read on abadis.ir): «(مِ) [فر.] (فعل.) \"\n             \"متشکرم، ممنونم» — tagged [فر.] = French, exactly Nourai's arrow.\")\nDEH_MKRM = (\"Dehkhoda s.v. مرکورکرم (read on abadis.ir): the word renders the trade name \"\n            \"‘Mercurochrome’ (merbromin, مربرومین), «محلولی است که تقریباً دارای ۲۶ درصد مرکور (جیوه) است», \"\n            \"an antiseptic prepared in 1919 by Hugh H. Young — i.e. an American trade name, not a French word.\")\n\ndef rc(ref, status, note): return {\"ref\": ref, \"status\": status, \"note\": note}\ndef cs(src, where, stance, note): return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": note}\n\ne0_nodes = [\n {\"id\":1,\"lang\":\"Avestan\",\"words\":\"mereza\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Young Avestan marəza- m. 'march, border district', attested at Vendīdād 3.5 (Bartholomae, AiW col. 1153: 'Mark, Grenzgebiet'). Nourai's spelling 'mereza' is simply the older Western transliteration of marəza-, with schwa written e — Horn 1893 (no. 974) prints 'merezu' and Klein 'marǟza', so the form is not corrupt. It goes back to Proto-Iranian *marȜa(h)- from PIE *mórǵ-s 'edge, boundary': PIE palatal *ǵ gives Avestan z by the satem shift, against the plain g of Latin margō and Germanic *markō. One caution the chart does not make: this marəza- 'border' (AiW 1153) is a different word from the homonymous Avestan verb marəz- 'to graze, touch' (AiW 1152), the source of MP marz- 'copulate' (Nyberg s.v. marzihistan) — the two are constantly confused.\",\n  \"derivation_fa\":\"اوستایی marəza- «مرز، ناحیة سرحدی» در وندیداد ۳؛۵ آمده است (بارتولومه، ستون ۱۱۵۳). نگارش «mereza» در کتاب خطا نیست؛ شیوة کهنِ اروپایی است که شوای میانگی (ə) را e می‌نوشته‌اند — هرن هم «merezu» می‌نویسد. این واژه از ایرانی باستان *marȜa- و آن از هندواروپایی آغازین *mórǵ-s است؛ *ǵ کامی در زبان‌های ستم (اوستایی) به z بدل شده، در برابر g در لاتینی margō. هشدار: این marəza- را باید از همآوایِ آن، ستاک marəz- «ساییدن، لمس کردن» (ستون ۱۱۵۲، منشأ marz- پهلوی)، جدا دانست. ادعای نورایی درست است.\",\n  \"sources\":[W_MARZ,W_MORGS],\n  \"ref_check\":[rc(\"POK:738\",\"partial\",\"Pokorny's mereg- entry (p. 738) has the root and 'Npers. marz', but does NOT cite the Avestan word; for marəza- one must go to Bartholomae 1153 (or WP II 283, which Pokorny cross-refers). \"+POK738),\n               rc(\"KLN:940\",\"supports\",\"Klein p. 940 s.v. mark: '… and cogn. with Avestic marǟza, ‘border’, L. margo …' — precisely the Avestan form and gloss Nourai draws. \"+KLN940)],\n  \"consulted\":[cs(\"BRT\",\"col. 1153/54 s.v. marəza-\",\"supports\",BRT1153),\n               cs(\"NYB\",\"Part II Glossary s.v. marz-pān / marzihistan\",\"supports\",NYB_MARZ),\n               cs(\"WLD\",\"Bd. II p. 283\",\"partial\",WLD283),\n               cs(\"SYN\",\"ch. 19 (boundary), p. as l.32947\",\"supports\",SYN_MARG)]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"marz\",\"verdict\":\"confirmed\",\n  \"derivation\":\"NP مرز marz 'border, boundary; strip of land between fields' continues Middle Persian marz [mlc] 'boundary, march; (astronomical) term' (MacKenzie, CPD s.v.) < Old Iranian *marza- = Av. marəza-. The development is trivially regular: the cluster -rz is stable from Old Iranian through Middle to New Persian, so marza- > marz > marz with only loss of the thematic vowel. The derivative marzbān 'margrave, warden of the marches' (MP marz-pān, Kārnāmag 39) proves the word's currency in Sasanian administration and was itself lent onward to Armenian marzpan, Syriac marzbānā and Arabic marzubān. Mo'in's own etymological footnote at Borhan-e Qāte' p. 1986 — Nourai's cited page — gives exactly this chain (Av. marəza- 'frontier of a country' > Pahl. marz, marz-bān > NP marz), with Gothic marka and Latin margo as cognates.\",\n  \"derivation_fa\":\"«مرز» فارسی نو بازماندة فارسی میانة marz «مرز، سرحد، اصطلاح نجومی» (مکنزی) و آن از ایرانی باستان *marza- همانندِ اوستایی marəza- است. دگرگونی آوایی ناچیز است: خوشة پایانی -rz در همة دوره‌ها پایدار مانده و فقط واکة ستاکی افتاده است. مشتقِ «مرزبان» (پهلوی marz-pān، کارنامه ۳۹) به ارمنی marzpan، سریانی و عربی «مرزبان» وام داده شده است. معین در حاشیة برهان قاطع (ص ۱۹۸۶) دقیقاً همین زنجیره را می‌آورد؛ ادعای نورایی درست است.\",\n  \"sources\":[W_MARZ],\n  \"ref_check\":[rc(\"BQT:1986\",\"supports\",BQT1986)],\n  \"consulted\":[cs(\"PHD\",\"s.v. marz, marz(o)bān\",\"supports\",PHD_MARZ),\n               cs(\"NYB\",\"s.v. marz-pān\",\"supports\",NYB_MARZ),\n               cs(\"HRN\",\"no. 974\",\"supports\",HRN974),\n               cs(\"HUB\",\"Pers. Studien, marz / marzban\",\"supports\",HUB_MARZ),\n               cs(\"BQT\",\"p. 1986 s.v. مرز fn. 4\",\"supports\",BQT1986)]},\n {\"id\":3,\"lang\":\"Germanic\",\"words\":\"mark\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Proto-Germanic *markō f. 'boundary, border territory' < PIE *mórǵ-s: Gothic marka 'Grenze', OHG marc(h)a 'Grenze, Grenzland', OE mearc, ON mǫrk 'borderland, forest' (forests served as frontiers) — all listed at Pokorny 738. Nourai's gloss 'to mark' belongs strictly to the denominative verbs built on that noun, PGmc *markōn / *markjan (OE mearcian 'to make a mark', OHG merken 'to note'): a boundary was established by walking it and setting boundary-posts, so 'boundary' > 'boundary-post, landmark' > 'sign' > 'to make a sign'. Watkins states the double value in one breath: 'Germanic *mark-, boundary, border territory; also to mark out a boundary by walking around it (ceremonially “beating the bounds”); also a landmark, boundary marker, and a mark in general'. So the node is right, with the noun logically prior to the verb.\",\n  \"derivation_fa\":\"ژرمنی آغازین *markō «مرز، سرزمین سرحدی» از همان ریشة هندواروپایی است: گوتی marka، آلمانی باستان marc(h)a، انگلیسی باستان mearc (پوکورنی ۷۳۸). معنای «نشان کردن» که نورایی می‌دهد از فعل‌های اسمی *markōn/*markjan می‌آید؛ تحول معنایی این گونه بوده است: «مرز» > «ستونِ مرزی، نشانة مرز» > «نشان» > «نشان نهادن». واتکینز (AHD) هر دو معنا را یکجا می‌آورد؛ پس ادعای کتاب پذیرفتنی است.\",\n  \"sources\":[E_MARK,W_MORGS],\n  \"ref_check\":[rc(\"(none on this node)\",\"not_checked\",\"Nourai gives no reference for the Germanic box; POK:738 (cited on the root) and AHD merg- both cover it and were checked instead — see consulted.\")],\n  \"consulted\":[cs(\"AHD\",\"Watkins s.v. merg-\",\"supports\",AHD_MERG),\n               cs(\"KLN\",\"p. 940 s.v. mark\",\"supports\",KLN940),\n               cs(\"POK\",\"p. 738 s.v. mereg-\",\"supports\",POK738),\n               cs(\"IEC\",\"Mann s.v. marǵos\",\"supports\",IEC_MARG)]},\n {\"id\":4,\"lang\":\"English\",\"words\":\"mark, remark, march\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Three reflexes of the same Germanic noun, but by two different routes. mark n. is direct inheritance: ME merke, marke < OE mearc 'boundary, sign, mark', whose sense-history runs 'boundary' > 'boundary post' > 'sign in general' > 'visible trace' (Etymonline; 'any visible trace or impression' by c. 1200). march 'border, frontier' (13th c., whence the Welsh Marches) is a re-import: Frankish *marka gave Old French marche 'border country', borrowed into ME as marche — Skeat: 'march (1). a border, frontier … A.S. mearc, a mark, boundary'; Watkins files MARCH¹ and MARCH² under merg- via 'Old French marc, marche' and Frankish *markōn. remark (17th c.) is F. remarquer = re- + marquer, and OF marquer/merchier is itself a Germanic loan (Klein: 'OF. merchier, ‘to mark, note’, is a Teut. loan word'), from PGmc *markja- (ON merki). So the arrow Germanic > English is right in substance for all three; two of them travelled through French, which the chart does not show.\",\n  \"derivation_fa\":\"هر سه واژه بازماندة همان اسمِ ژرمنی‌اند، اما از دو راه: mark میراس مستقیم است (انگلیسی باستان mearc)؛ ولی march «مرز، ناحیة سرحدی» و remark وام‌واژه‌اند از فرانسوی کهن (marche، remarquer) و آن فرانسوی خود وام‌گیری از فرانکی *marka/*markōn است (کلاین: «merchier در فرانسوی کهن وام‌واژه‌ای ژرمنی است»). پس پیکان کتاب درست است، اما میانجیِ فرانسوی در نمودار افتاده است.\",\n  \"sources\":[E_MARK],\n  \"ref_check\":[rc(\"(none on this node)\",\"not_checked\",\"No reference printed in the box; AHD merg- and Klein p. 940 (both cited elsewhere on the chart) cover MARK, MARCH and REMARK and were checked — see consulted.\")],\n  \"consulted\":[cs(\"AHD\",\"Watkins s.v. merg- 1a, 1c, 2, 3\",\"supports\",AHD_MERG),\n               cs(\"KLN\",\"p. 940 s.v. mark ('Cp. also march … remark')\",\"supports\",KLN940),\n               cs(\"SKT\",\"s.v. march (1)\",\"supports\",SKT_MARCH)]},\n {\"id\":5,\"lang\":\"Latin\",\"words\":\"margo\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Latin margō, gen. marginis 'edge, brink, border, margin' is the Italic member of the family, formed with an -n- stem extension on PIE *mórǵ- (Pokorny writes '*m̥ rǵ-en-'). Its plain velar g — against Avestan marəza-, Persian marz with z — is exactly the centum treatment of PIE palatal *ǵ, which is what makes this cognate set a standard textbook example. Pokorny 738 puts 'lat. margö, -inis „Rand, Grenze“' immediately after Npers. marz; Watkins gives 'Latin margo, border, edge: MARGIN' as branch 4 of merg-. Latin has no verb from the base, which has led some (de Vaan) to suspect a Celtic or Germanic loan into Latin, but nobody disputes the etymological connection itself.\",\n  \"derivation_fa\":\"لاتینی margō (مفعولی marginem) «کناره، حاشیه، مرز» عضو ایتالیکی این خانواده است و با پسوندِ ستاکی -n- از *mórǵ- ساخته شده است. وجود g در لاتینی در برابر z در اوستایی و فارسی همان تقابل دو گروهِ کنتوم و ستم است و این مجموعه را به نمونة درسی بدل کرده است. پوکورنی (۷۳۸) و واتکینز هر دو همین را می‌گویند؛ ادعای نورایی درست است.\",\n  \"sources\":[E_MARGIN,W_MORGS],\n  \"ref_check\":[rc(\"AHD\",\"supports\",\"Watkins, merg- branch 4: 'Latin margo, border, edge: MARGIN. [Pok. mereg- 738.]' \"+AHD_MERG)],\n  \"consulted\":[cs(\"POK\",\"p. 738\",\"supports\",POK738),\n               cs(\"WLD\",\"Bd. II p. 283\",\"partial\",WLD283),\n               cs(\"IEC\",\"Mann s.v. marǵos\",\"supports\",IEC_MARG),\n               cs(\"LAT\",\"Ernout-Meillet\",\"silent\",\"grep of LAT.txt for 'margo' returns only the cross-reference lines (l.13291 'commercium: v.merx' etc.); the margo article itself is not in the OCR range searched, so Ernout-Meillet is silent here.\")]},\n {\"id\":6,\"lang\":\"English\",\"words\":\"margin\",\"verdict\":\"confirmed\",\n  \"derivation\":\"ME margine (late 14th c., Chaucer's era, first of the blank edge of a page) < Latin marginem, the accusative of margō; as usual for Latin -o/-inis nouns the English form is built on the oblique stem (cf. virgin < virginem, origin < originem). Etymonline: 'from Latin marginem (nominative margo) “edge, brink, border, margin,” from PIE root *merg- “boundary, border”'. Klein s.v. marge/margin agrees ('F., fr. L. margo, gen. marginis'), and Watkins ends the merg- article with 'Latin margo …: MARGIN'. The financial and figurative senses ('margin of profit', 'marginal') are 19th-c. metaphors on the page-edge sense.\",\n  \"derivation_fa\":\"انگلیسی margin از لاتینی marginem (حالت مفعولی margō) گرفته شده است؛ از سدة چهاردهم میلادی به معنای «حاشیة سفید صفحه». مانند دیگر وام‌واژه‌های لاتینیِ ستاکِ -in- (مانند virgin و origin) از ستاک مورب ساخته شده است. اتیمونلاین، کلاین و واتکینز همه همین را می‌گویند؛ ادعای نورایی درست است.\",\n  \"sources\":[E_MARGIN],\n  \"ref_check\":[rc(\"(none on this node)\",\"not_checked\",\"No reference in the box; the parent's AHD citation covers MARGIN and was checked — see consulted.\")],\n  \"consulted\":[cs(\"AHD\",\"Watkins s.v. merg- 4\",\"supports\",AHD_MERG),\n               cs(\"KLN\",\"s.v. marge, margin (KLN_1966.txt l.22921)\",\"supports\",\"Klein: 'marge, n., edge, border. — F., fr. L. margo, gen. marginis. See margin.'\"),\n               cs(\"SKT\",\"index l.23166 'margin—margo, marge'\",\"supports\",\"Skeat's index refers margin to Lat. margo, via F. marge — same chain.\")]},\n]\n\ne2_nodes = [\n {\"id\":1,\"lang\":\"Latin\",\"words\":\"merx, comerx\",\"verdict\":\"transcription_suspect\",\n  \"derivation\":\"Latin merx, gen. mercis f. 'wares, merchandise' is genuine and old (Plautus, Cistellaria 727 'bona mers, era, haec et callida est'; Ernout-Meillet 'Ancien, usuel'). 'comerx' however is not a Latin word at all: Nourai has compressed con- + merx, i.e. commercium 'trade' (Klein s.v. commerce: 'L. commercium … fr. con- and merx, gen. mercis'), into a pseudo-nominative. The printed page (pdf 337) really does show 'merx, comerx : merchandise', so this is the book's own shorthand/misprint and the extraction is faithful. On the derivation itself: Pokorny does file the family here — p. 739 under merk͝- 'fassen, ergreifen' — but explicitly with 'fraglich ist Zugehörigkeit von lat. merx'. Watkins brackets merk-² as an 'Italic root, possibly from Etruscan'; Ernout-Meillet: 'merx … sans étymologie i.-e. sûre'; Klein: 'merx … which is of uncertain origin'. In the 2020s Nikolaev has argued for a real PIE *merkʷ- linking merx to Gk. márptō 'take hold' and Toch. A märk- 'take away', which would vindicate Nourai's arrow — so the derivation is plausible, only the second form is spurious.\",\n  \"derivation_fa\":\"لاتینی merx (مضاف‌الیه mercis) «کالا، متاع» واژه‌ای کهن و اصیل است؛ اما «comerx» در لاتینی وجود ندارد و فشرده‌سازی نورایی از con-+merx یعنی commercium است؛ تصویر صفحة ۳۳۷ نشان می‌دهد که همین صورت در کتاب چاپ شده — پس خطای خوانشِ اسکن نیست، خطای خود کتاب است. اما دربارة ریشه: پوکورنی خود در ص ۷۳۹ پیوستگی merx را به این ریشه «fraglich» (مشکوک) می‌خواند، واتکینز آن را ریشة ایتالیکیِ احتمالاً اتروسکی می‌داند و ارنو-میه و کلاین «ریشة نامعلوم» می‌نویسند؛ در مقابل، نیکولایف (دهة ۲۰۲۰) ریشة *merkʷ- را با یونانی márptō «گرفتن» بازسازی کرده که در این صورت ادعای نورایی پذیرفتنی است.\",\n  \"error_in\":\"book\",\"book_prints\":\"merx, comerx : merchandise\",\"correct_form\":\"merx (gen. mercis) 'merchandise'; commercium 'trade'\",\n  \"sources\":[W_MERX],\n  \"ref_check\":[rc(\"POK:739\",\"partial\",\"Pokorny p. 739 s.v. merk͝- does list merx here, but as doubtful: 'fraglich ist Zugehörigkeit von lat. merx ‚Ware‘ …'. \"+POK739)],\n  \"consulted\":[cs(\"LAT\",\"pp. 712-713 s.v. merx; index\",\"partial\",LAT_MERX),\n               cs(\"KLN\",\"s.v. mercantile\",\"partial\",KLN_MERC),\n               cs(\"AHD\",\"Watkins s.v. merk-²\",\"contradicts\",AHD_MERK),\n               cs(\"POK\",\"p. 739\",\"partial\",POK739)]},\n {\"id\":2,\"lang\":\"Italian\",\"words\":\"commerci\",\"verdict\":\"transcription_suspect\",\n  \"derivation\":\"The Italian word for 'commerce' is commercio (plural commerci); the box prints the plural as if it were the headword, and the page image confirms 'commerci : commerce' is what the book set, so the extraction is faithful. Italian commercio is a learned (dotta) borrowing straight from Latin commercium (con- + merx), not a popular development — the inherited Italian member of the family is mercato < Lat. mercātus (Klein s.v. market: 'whence also It. mercato …'). The arrow Latin merx > Italian is therefore unobjectionable in itself. What the node cannot bear is the weight the chart puts on it: its reference MON:3392 is Mo'in's گمرک article, which tags the Persian word simply '[مأخوذ از ترکی]' (from Turkish) and knows nothing of an Italian step.\",\n  \"derivation_fa\":\"در ایتالیایی واژه commercio است و commerci صورت جمع آن؛ کتاب همین صورت جمع را سرمدخل گرفته است (تصویر صفحه تأیید می‌کند؛ خطای کتاب است، نه خطای استخراج). خودِ commercio وام‌واژه‌ای عالمانه از لاتینی commercium است، و واژة موروثی این خانواده در ایتالیایی mercato است. پیکان merx > ایتالیایی ایرادی ندارد، ولی مأخذِ خودِ نورایی (معین ۳۳۹۲) «گمرک» را مأخوذ از ترکی می‌داند و از میانجیِ ایتالیایی سخنی نمی‌گوید.\",\n  \"error_in\":\"book\",\"book_prints\":\"commerci : commerce\",\"correct_form\":\"commercio\",\n  \"sources\":[A_GOM,E_MERCH],\n  \"ref_check\":[rc(\"MON:3392\",\"partial\",MON_GOM)],\n  \"consulted\":[cs(\"KLN\",\"s.v. market, commerce\",\"supports\",KLN_MKT),\n               cs(\"LKT\",\"no. 751\",\"contradicts\",LKT751),\n               cs(\"LAT\",\"s.v. merx (commercium listed among the derivatives)\",\"supports\",\"Ernout-Meillet list 'commercor, -aris; commercium' among the dérivés of merx (LAT.txt l.37752 ff.), confirming commercium < con- + merx, the base of It. commercio.\")]},\n {\"id\":3,\"lang\":\"Portuguese\",\"words\":\"cumerx\",\"verdict\":\"disputed\",\n  \"derivation\":\"There is no Portuguese *cumerx. Portuguese for 'trade' is comércio, a learned loan from Lat. commercium (the inherited member being mercado < mercātus, cf. Klein s.v. market 'Sp. and Port. mercado'). Nor is Portuguese the channel by which the word reached Persian: Lokotsch no. 751 gives the real route — 'Tk. gümrük: ‚Zoll‘ [aus gr. κομμέρκιον, lat. commercium]' — and Hobson-Jobson p. 384, which Nourai himself cites on the child node, says the same: gumruk 'is again, through Low Greek, from the Latin commercium'. κομμέρκιον was the Byzantine customs levy (a Latin administrative term taken into Greek in late antiquity), and it passed from Byzantine Greek into Ottoman Turkish, not through the Iberian trading languages. The printed page shows 'cumerx : trade', so the odd form is the book's, but the node itself has no place in the tree.\",\n  \"derivation_fa\":\"در پرتغالی واژه‌ای به صورت *cumerx وجود ندارد؛ «تجارت» در پرتغالی comércio است، وام‌واژه‌ای عالمانه از commercium. مهم‌تر آنکه راهِ رسیدن این واژه به فارسی پرتغالی نبوده است: لوکوتش (شمارة ۷۵۱) و خودِ مأخذِ نورایی (هابسن-جابسن ص ۳۸۴) می‌گویند که ترکی gümrük از یونانی بیزانطینی κομμέρκιον گرفته شده و آن خود از لاتینی commercium است. پژوهش امروزی این گره را رد می‌کند؛ صورتِ چاپی نیز خطای خود کتاب است.\",\n  \"error_in\":\"book\",\"book_prints\":\"cumerx : trade\",\"correct_form\":\"comércio (and the node should be Byzantine Greek κομμέρκιον → Ottoman Turkish gümrük)\",\n  \"sources\":[W_GOM,A_GOM],\n  \"ref_check\":[rc(\"(none on this node)\",\"not_checked\",\"No reference printed in the Portuguese box. The two references that do bear on the claim — HJB:384 on the child node and Lokotsch 751 — were checked and both give the Greek–Turkish route instead; see consulted.\")],\n  \"consulted\":[cs(\"LKT\",\"no. 751 (p. ~ leaf 1828)\",\"contradicts\",LKT751),\n               cs(\"HJB\",\"p. 384 s.v. GOMBROON\",\"contradicts\",HJB384),\n               cs(\"KLN\",\"s.v. market\",\"partial\",KLN_MKT)]},\n {\"id\":4,\"lang\":\"Persian\",\"words\":\"gomrok; gambroon\",\"verdict\":\"disputed\",\n  \"derivation\":\"Two unrelated words are put in one box. (a) گمرک gomrok 'customs, customs duty/house' is a Turkish loan: Ottoman Turkish گمرك gümrük < Byzantine Greek κομμέρκιον kommérkion (the Byzantine customs levy) < Latin commercium; Mo'in tags the Persian word '[مأخوذ از ترکی]' and Dehkhoda dates the Turkish adoption to after the conquest of Constantinople (1453), whence Persian; Lokotsch 751 gives the identical chain with Bulg. gumruk, Serb. džumruk as parallel borrowings. Nourai's ultimate Latin source is right, his Italian→Portuguese relay is not, and the phonetics confirm it: Greek/Turkish gü- for Latin co(m)- and the -ük ending are Turkish, whereas an Italian or Portuguese loan would have kept -io/-cio. (b) گمبرون Gambroon/Gombroon, the European name of the port Shah ʿAbbās renamed Bandar ʿAbbās in 1622, is a place-name, and Nourai's own cited page rejects the customs etymology for it: Hobson-Jobson p. 384 reports the 'Turkish for custom-house' story and answers 'But this etymology of the name seems hardly probable', preferring Pers. kamrūn / Port. camarão 'shrimp' after A. Hamilton (1727), who says the Portuguese named the fishing village so 'in Derision, because it was a good place for catching Prawns and Shrimps, which they call Camerong'. Early European spellings — Gamrun, Comorão (1614), Cummeroon, Gamron — point the same way. So the node is disputed on both halves.\",\n  \"derivation_fa\":\"در یک جعبه دو واژة بی‌ربط نشانده شده است. ۱) «گمرک» وام‌واژه‌ای ترکی است: ترکی عمانی gümrük از یونانی بیزانطینی κομμέρκιον (حقّ گمرکی دولت بیزانطین) و آن از لاتینی commercium؛ معین آن را «مأخوذ از ترکی» و دهخدا ورودِ آن را به ترکی پس از فتح قسطنطنیه می‌داند؛ لوکوتش (۷۵۱) نیز همین را می‌گوید. پس منشأ لاتینی درست است ولی میانجیِ ایتالیایی–پرتغالی نادرست است؛ شکل آوایی (gü- و پایانة -ük) ترکی است. ۲) «گمبرون» نام جای است (بندرِ پیشازِ بندرعباس) و خودِ مأخذِ نورایی (هابسن-جابسن ص ۳۸۴) ریشه‌گرفتنِ آن را از gümrük «بسیار نامحتمل» می‌خواند و فارسی «کمرون/کمبرون» یا پرتغالی camarão «میگو» را ترجیح می‌دهد. پس این گره از دو سو محلّ اختلاف است.\",\n  \"sources\":[W_GOM,A_GOM],\n  \"ref_check\":[rc(\"MON:3392\",\"partial\",MON_GOM),\n               rc(\"HJB:384\",\"contradicts\",HJB384)],\n  \"consulted\":[cs(\"HJB\",\"p. 384 s.v. GOMBROON\",\"contradicts\",HJB384),\n               cs(\"LKT\",\"no. 751\",\"partial\",LKT751),\n               cs(\"MON\",\"s.v. گمرک (p. 3392; read via abadis.ir)\",\"contradicts\",MON_GOM),\n               cs(\"KLN\",\"s.v. commerce\",\"partial\",KLN_MKT)]},\n {\"id\":5,\"lang\":\"English\",\"words\":\"commerce, merchant, market\",\"verdict\":\"confirmed\",\n  \"derivation\":\"All three are the Latin merx family, entering English by different Romance routes. commerce (16th c.) is F. commerce < Lat. commercium 'trade, traffic' = con- + merx (Klein s.v. commerce). merchant (early 13th c.) is Anglo-French marchaunt < Vulgar Latin *mercātantem, pres. part. of *mercātāre, a frequentative of mercārī 'to trade' < merx (Etymonline). market (early 12th c., one of the earliest French-Latin loans in English) is Old North French market, answering to central OF marché, < Lat. mercātus 'trading, marketplace', pp. of mercārī < merx — mart is its Middle Dutch doublet. Watkins lists precisely 'MARKET, (MART), MERCER, MERCHANT; COMMERCE' under merk-², i.e. Nourai's own AHD reference supports the node; the only difference is that AHD treats the Latin base as Italic/possibly Etruscan rather than PIE.\",\n  \"derivation_fa\":\"هر سه واژه از خانوادة merx لاتینی‌اند ولی از مسیرهای گوناگون به انگلیسی راه یافته‌اند: commerce از فرانسوی و لاتینی commercium (con- + merx)؛ merchant از فرانسوی آنگلو-نورمن marchaunt از لاتینی عامیانه *mercātantem؛ market از فرانسوی شمالی market از لاتینی mercātus. واتکینز (همان AHD که نورایی ارجاع می‌دهد) همین سه واژه را زیر merk-² می‌آورد؛ ادعای کتاب درست است.\",\n  \"sources\":[E_MERCH],\n  \"ref_check\":[rc(\"AHD\",\"supports\",\"Watkins, merk-² branch 1: 'Latin merx (stem merc-), merchandise (> mercāri, to trade): MARKET, (MART), MERCER, MERCHANT; COMMERCE.' \"+AHD_MERK)],\n  \"consulted\":[cs(\"KLN\",\"s.v. market, commerce, mercantile\",\"supports\",KLN_MKT),\n               cs(\"SKT\",\"s.v. merchant (l.11443), market (l.11433)\",\"supports\",\"Skeat: 'merchant. (F.—L.) M.E. marchant' and 'market … prob. … of Latin merc-'; same Latin base.\"),\n               cs(\"AHD\",\"Watkins s.v. merk-²\",\"supports\",AHD_MERK)]},\n {\"id\":6,\"lang\":\"Latin\",\"words\":\"merces; Mercurius\",\"verdict\":\"plausible\",\n  \"derivation\":\"mercēs, gen. mercēdis f. 'hire, pay, reward, price' is a straightforward -ēd- derivative of merx and Pokorny 739 prints it in the same breath ('merces, -edis ‚Preis, Lohn, Sold‘'); in Vulgar and Church Latin it drifted 'wages' > 'favour, pity, grace', which is where Nourai's added gloss 'kindness' comes from — Klein s.v. mercy: 'L. merces, ‚hire, pay, reward‘ (in VL. also ‚favor, pity‘)'. Mercurius is the doubtful half of the box. Skeat derives it outright from 'L. merc-, stem of merx, merchandise', and Watkins keeps it under merk-² ('Probably Latin Mercurius, the god of (inter alia) commerce'), but Klein says flatly 'L. Mercurius, fr. Etruscan *Mercura, a divinity introduced from Etruria into Rome about the end of the sixth century B.C.E. … prob. not related to L. merx'; Ernout-Meillet note that its suffix is that of Titurius, Mamurius, Veturius ('étrusque?') and that there is 'pas d'étymologie sûre'; de Vaan allows that the whole stem merk- may be an Etruscan borrowing along with the god's name. Hence plausible: mercēs certainly, Mercurius only probably.\",\n  \"derivation_fa\":\"mercēs (مضاف‌الیه mercēdis) «مزد، پاداش، بها» مشتقی روشن از merx است و پوکورنی (۷۳۹) همانجا می‌آوردد؛ در لاتینی عامیانه و کلیسایی معنای آن از «مزد» به «لطف، رحمت» دگرگون شد — منشأ معنای «kindness» در کتاب همین است. اما دربارة Mercurius اختلاف هست: اسکیت و واتکینز آن را از merx می‌دانند، ولی کلاین صریحاً می‌گوید از اتروسکی *Mercura است و احتمالاً با merx پیوندی ندارد، و ارنو-میه پسوند آن را اتروسکی می‌شمارند. پس نیمة نخست قطعی و نیمة دوم فقط با احتیاط پذیرفتنی است.\",\n  \"sources\":[W_MERC,E_MERCUR],\n  \"ref_check\":[rc(\"AHD\",\"supports\",\"Watkins merk-² branches 2-3: 'Latin merces, pay, reward, price: MERCENARY, MERCY. 3. Probably Latin Mercurius, the god of (inter alia) commerce: MERCURY.' \"+AHD_MERK)],\n  \"consulted\":[cs(\"KLN\",\"s.v. Mercury; s.v. mercy\",\"contradicts\",KLN_MERCUR+\" (Klein does, however, derive merces from merx: \"+KLN_MERCY+\")\"),\n               cs(\"LAT\",\"pp. 712-713 s.v. merx, Mercurius, mercēs\",\"partial\",LAT_MERX),\n               cs(\"SKT\",\"s.v. mercury\",\"supports\",SKT_MERCUR),\n               cs(\"POK\",\"p. 739\",\"partial\",POK739)]},\n {\"id\":7,\"lang\":\"French\",\"words\":\"\",\"verdict\":\"confirmed\",\n  \"derivation\":\"An unlabelled pass-through box standing for French merci. Latin mercēdem (acc. of mercēs) > Old French mercit, then merci f. 'reward, gift; kindness, grace, pity' (11th–12th c.), by the regular loss of the Latin post-tonic syllable and palatalisation of -c- before the front vowel. The semantic groundwork was already Latin: in Vulgar Latin mercēs meant 'favour, pity', and from the 6th c. Church Latin used it of 'the heavenly reward earned by those who show kindness to the helpless and those from whom no requital can be expected' (Etymonline s.v. mercy). Out of that 'favour owed' sense French merci became the formula of thanks. Klein s.v. mercy documents the same step: 'fr. OF. mercit, merci (F. merci), fr. L. mercedem'.\",\n  \"derivation_fa\":\"این جعبة تهی در واقع جایگاهِ فرانسوی merci است: لاتینی mercēdem > فرانسوی کهن mercit > merci، با افتادنِ قاعده‌مندِ هجای پس‌از‌تکیه و نرم‌شدنِ c پیش از واکة پیشین. تحول معنایی از پیش در لاتینی رخ داده بود: mercēs در لاتینی عامیانه «لطف، ترحم» و در لاتینی کلیسایی (از سدة ششم) «پاداش الهی» معنا می‌داد؛ از همین «لطفِ وامدار‌شدن» کاربردِ سپاسگویی پدید آمد. ادعای کتاب درست است.\",\n  \"sources\":[E_MERCY],\n  \"ref_check\":[rc(\"(none on this node)\",\"not_checked\",\"Empty pass-through box with no reference; Klein s.v. mercy and Etymonline cover the Latin > Old French step and were checked — see consulted.\")],\n  \"consulted\":[cs(\"KLN\",\"s.v. mercy\",\"supports\",KLN_MERCY),\n               cs(\"AHD\",\"Watkins merk-² branch 2 (MERCY)\",\"supports\",AHD_MERK)]},\n {\"id\":8,\"lang\":\"Persian\",\"words\":\"mercî\",\"verdict\":\"confirmed\",\n  \"derivation\":\"مرسی mersi 'thank you' is a direct modern loan from French merci, one of the large Francophone layer that entered Persian from the Qājār period on — the Dār al-Fonūn, French-educated officials and students, and (for polite formulas) salon usage; it is now fully colloquial beside ممنونم and متشکرم. Mo'in's entry, Nourai's cited page, tags it exactly so: «(مِ) [فر.] (فعل.) متشکرم، ممنونم», '[فر.]' being Mo'in's tag for French. Phonetically French [mɛʁsi] is taken over as mersi, the French uvular r rendered by Persian ر and the final -i as ی; Nourai's spelling 'mercî' is his own transcription habit (c for [s], î for final ī), not a Persian form. The node therefore closes a chain Latin mercēdem > OF merci > NP مرسی — a European loan, with no Arabic mediation.\",\n  \"derivation_fa\":\"«مرسی» وام‌واژه‌ای مستقیم از فرانسوی merci است و از لایة بزرگِ وام‌واژه‌های فرانسوی است که از دورة قاجار (دارالفنون و تحصیل‌کردگان فرنگ) به فارسی راه یافت. معین در همان صفحه‌ای که نورایی ارجاع می‌دهد آن را با نشانة [فر.] می‌آورد. در وام‌گیری، r ملازیِ فرانسوی به «ر» و واکة پایانی به «ی» بدل شده است؛ نگارش «mercî» در کتاب فقط شیوة آوانگاری خود نورایی است. ادعای نورایی درست است.\",\n  \"sources\":[A_MERSI,E_MERCY],\n  \"ref_check\":[rc(\"MON:4015\",\"supports\",MON_MERSI)],\n  \"consulted\":[cs(\"MON\",\"s.v. مرسی (p. 4015; read via abadis.ir)\",\"supports\",MON_MERSI),\n               cs(\"KLN\",\"s.v. mercy (for the Latin > French step)\",\"supports\",KLN_MERCY)]},\n {\"id\":9,\"lang\":\"English\",\"words\":\"mercy\",\"verdict\":\"confirmed\",\n  \"derivation\":\"ME merci (late 12th c.) < Old French mercit, merci 'reward, gift; kindness, grace, pity' < Lat. mercēdem, acc. of mercēs 'reward, wages, pay, hire' — Klein s.v. mercy gives exactly this, adding that It. mercé and Sp. merced 'favor, grace, mercy' come from the same accusative. The semantic path is the Church-Latin one: 'pay' > 'favour, pity' (Vulgar Latin) > 'heavenly reward for kindness to the helpless' (Church Latin from the 6th c.) > 'disposition to forgive' (English by the early 13th c.) and 'an act of forbearance' (c. 1300); the phrase 'at (one's) mercy' is mid-14th c. Watkins lists MERCY under merk-² branch 2 with mercēs. So the node is right; only the ultimate PIE status of the root is at issue (see the root entry).\",\n  \"derivation_fa\":\"انگلیسی mercy از فرانسوی کهن merci و آن از لاتینی mercēdem (مفعولی mercēs «مزد، پاداش») است. تحول معنایی کلیسایی است: «مزد» > «لطف، ترحم» (لاتینی عامیانه) > «پاداش الهی در برابر مهرورزی به ناتوانان» (از سدة ششم) > «گرایش به بخشودن» (انگلیسی میانه). کلاین و واتکینز هر دو همین زنجیره را می‌دهند؛ ادعای کتاب درست است.\",\n  \"sources\":[E_MERCY],\n  \"ref_check\":[rc(\"AHD:821\",\"partial\",\"Nourai's AHD:821 is a page of the New College Edition body (the ‘mercy’ headword page), which is not available open online (the lending scans of americanheritag00morr etc. cannot be paged from here). The Watkins appendix, which is the same work's IE material and the modern standard, does support the claim: \"+AHD_MERK)],\n  \"consulted\":[cs(\"KLN\",\"s.v. mercy\",\"supports\",KLN_MERCY),\n               cs(\"AHD\",\"Watkins s.v. merk-² branch 2\",\"supports\",AHD_MERK)]},\n {\"id\":10,\"lang\":\"French\",\"words\":\"\",\"verdict\":\"confirmed\",\n  \"derivation\":\"The second unlabelled French pass-through, standing for French mercure — both the god/planet Mercure and the metal mercure 'quicksilver'. Latin Mercurius gave Old French Mercurie (Skeat: 'O.F. Mercurie'), refashioned in modern French as mercure on the Latin stem; the metal took the god's name in medieval alchemy, where the seven metals were paired with the seven planets and quicksilver's mobility suited the swift messenger god. From this French box come the Persian chemical and pharmaceutical terms of the next node.\",\n  \"derivation_fa\":\"این جعبة تهی دوم جایگاهِ فرانسوی mercure است؛ هم نام خدا/سیاره و هم نام فلزِ جیوه. لاتینی Mercurius در فرانسوی کهن Mercurie شد و سپس بر پایة ستاک لاتینی به mercure دوباره‌سازی شد. نامگذاری فلز به نامِ این خدا در کیمیاگری قرون وسطا رخ داده، زیرا هفت فلز را با هفت اختر متنازر می‌گرفتند و تحرکِ جیوه با پیکِ تیزپای خدایان متناسب بود.\",\n  \"sources\":[E_MERCUR],\n  \"ref_check\":[rc(\"(none on this node)\",\"not_checked\",\"Empty pass-through box with no reference; Skeat s.v. mercury and Klein s.v. Mercury/mercury cover the Latin > French step and were checked — see consulted.\")],\n  \"consulted\":[cs(\"SKT\",\"s.v. mercury\",\"supports\",SKT_MERCUR),\n               cs(\"KLN\",\"s.v. Mercury, mercury\",\"partial\",\"Klein derives the metal-name from the god ('Named after Mercury … prob. so called because of the great mobility of this element') but the god-name itself from Etruscan: \"+KLN_MERCUR)]},\n {\"id\":11,\"lang\":\"Persian\",\"words\":\"(no transliteration in the book) مرکور ، مرکورکرم\",\"verdict\":\"plausible\",\n  \"derivation\":\"The box gives only Persian script, no transliteration or gloss: مرکور merkur and مرکورکرم merkurokrom. مرکور is the learned name of mercury/Mercury, taken over with the French scientific nomenclature that shaped Persian chemistry and astronomy vocabulary from the Dār al-Fonūn onward (F. mercure) — for that word the French node is right. مرکورکرم is not French, however: Dehkhoda's entry says it renders the proprietary name Mercurochrome (the antiseptic merbromin, «محلولی است که تقریباً دارای ۲۶ درصد مرکور (جیوه) است»), coined in the United States in 1919 by Hugh H. Young at Johns Hopkins — mercuro- + -chrome, an English/American trade name, even if it reached Iranian pharmacies through French-style usage. Both words do descend ultimately from Lat. Mercurius, so the arrow is right at the top and only the immediate donor of the second word is wrong. Note also that Nourai's reference here is bare 'MON' with no page, so the citation cannot be pinned down.\",\n  \"derivation_fa\":\"در این جعبه فقط دو واژة فارسی به خط فارسی آمده است. «مرکور» نام علمی جیوه و سیارة عطارد است و با واژه‌نامه‌های علمی فرانسوی (mercure) از دورة دارالفنون وارد فارسی شده — در این مورد پیکانِ کتاب درست است. اما «مرکورکرم» فرانسوی نیست: دهخدا آن را برگردانِ نام تجاری Mercurochrome (مربرومین) می‌داند که در ۱۹۱۹ در امریکا ساخته شد؛ پس داده‌وامِ مستقیم انگلیسی است. هر دو در نهایت به Mercurius لاتینی می‌رسند، پس ادعای کتاب با احتیاط پذیرفتنی است.\",\n  \"sources\":[A_MKRM,E_MERCUR],\n  \"ref_check\":[rc(\"MON\",\"not_checked\",\"The box cites 'MON' with no volume/page, so there is nothing to look up; the print edition of Mo'in is not online (only an abridged 2-vol. archive.org scan, which has no مرکورکرم entry — grep of MON_2vol_Adena_v1/v2_djvu.txt finds nothing). Dehkhoda's entry was used instead: \"+DEH_MKRM)],\n  \"consulted\":[cs(\"MON\",\"مرکورکرم / مرکور (abadis.ir, Dehkhoda section)\",\"partial\",DEH_MKRM),\n               cs(\"SKT\",\"s.v. mercury\",\"partial\",SKT_MERCUR)]},\n {\"id\":12,\"lang\":\"English\",\"words\":\"mercury\",\"verdict\":\"confirmed\",\n  \"derivation\":\"ME mercurie 'quicksilver', named after the planet and god Mercury — Skeat s.v. mercury: 'ME. mercurie, quicksilver, named after the planet Mercury. — O.F. Mercurie … F. mercure. — L. Mercurium, acc. of Mercurius, Mercury, god of traffic. — L. merc-, stem of merx, merchandise'. Klein agrees on the naming ('Named after Mercury … prob. so called because of the great mobility of this element') while dissenting on the god's own origin. Watkins puts MERCURY under merk-² branch 3. So the arrow Latin Mercurius > English mercury is uncontroversial; what is uncertain is only the step above it (Mercurius ← merx), for which see node #6.\",\n  \"derivation_fa\":\"انگلیسی mercury در انگلیسی میانه mercurie «جیوه» بوده و به نام سیاره/خدای مرکور نامیده شده است؛ از فرانسوی کهن Mercurie و لاتینی Mercurium (اسکیت). واتکینز نیز MERCURY را زیر merk-² می‌آورد. پس این پیکان محلّ اختلاف نیست؛ تنها پیوندِ بالاتر (Mercurius ← merx) تردیدآمیز است (نگاه کنید به گره ۶).\",\n  \"sources\":[E_MERCUR,W_MERC],\n  \"ref_check\":[rc(\"(none on this node)\",\"not_checked\",\"No reference printed in the box; the parent's AHD citation covers MERCURY and was checked — see consulted.\")],\n  \"consulted\":[cs(\"SKT\",\"s.v. mercury\",\"supports\",SKT_MERCUR),\n               cs(\"AHD\",\"Watkins merk-² branch 3\",\"supports\",AHD_MERK),\n               cs(\"KLN\",\"s.v. mercury (the element)\",\"supports\",\"Klein: 'mercury, n., name of a silvery-white, fluid metallic element — Named after Mercury, the messenger of the gods … prob. so called because of the great mobility of this element.'\")]},\n]\n\ndata = {\n \"pdf_page\":337,\n \"book_page\":307,\n \"verified_by\":\"claude-opus-5\",\n \"verified_on\":\"2026-09-07\",\n \"entries\":[\n  {\"entry\":0,\n   \"root\":\"Merg, Mereg\",\n   \"verdict\":\"confirmed\",\n   \"modern_form\":\"PIE *mórǵ-s / *mereǵ- 'edge, boundary, border' (Pokorny 738 mereg-; AHD merg-)\",\n   \"note\":\"Pokorny p. 738 has the root in exactly these words — 'mereg- ‚Rand, Grenze‘' — with Npers. marz, Lat. margō, Goth. marka, OIr. mruig as its members; Watkins/AHD gives 'merg-. Boundary, border' with the cross-reference '[Pok. mereg- 738.]'. Nourai's two shapes 'Merg / Mereg' answer to Pokorny's *merg-/*mereg- notation, and Wiktionary reconstructs the underlying noun as *mórǵ-s (obl. *m̥ rǵ-) 'edge, boundary, border'. Language label ('Indo-European') and gloss ('mark, border') are both right, and all six nodes on the chart are members of the standard cognate set, so the whole entry stands. Two refinements a modern reader should add: (i) Walde-Pokorny II 283 (1927) had not yet made this a root of its own — it filed the border-words under the 'streichen, streifen' root and called their membership 'zweifelhaft' on vowel grounds; Pokorny 1959 separated them, which is the view followed today (Wiktionary's *mórǵ-s cautiously adds 'possibly derived from the verb underlying Hittite mārki “to divide, separate”'). (ii) The 'mark = sign' sense of the Germanic branch is secondary to 'boundary'; see node #3. The extraction is faithful to the printed page (pdf 337, copied to data/verification/sources/refs/ocr/BOOK/337.png).\",\n   \"note_fa\":\"ریشة هندواروپایی آغازین *mórǵ-s / *mereǵ- «کناره، مرز» درست و پذیرفته است؛ پوکورنی در ص ۷۳۸ دقیقاً همین را «mereg- ‚Rand, Grenze‘» می‌آورد و فارسی «مرز»، لاتینی margō و گوتی marka را زیر آن می‌نشاند؛ واتکینز (AHD) نیز همین را «merg-. Boundary, border» ثبت کرده است. نامِ زبان (هندواروپایی) و معنا («نشان، مرز») هر دو صحیح است و هر شش گرهِ نمودار از اعضای شناختة این خانواده‌اند. دو نکتة تکمیلی: والده-پوکورنی (ج ۲ ص ۲۸۳) در ۱۹۲۷ این واژه‌ها را زیر ریشة «ساییدن» می‌آورد و پیوستگی آنها را «مشکوک» می‌خواند، و جداکردنِ آن از پوکورنی ۱۹۵۹ است؛ دیگر آنکه معنای «نشان» در شاخة ژرمنی ثانوی است و از «مرز» پدید آمده است.\",\n   \"sources\":[W_MORGS,W_MARZ,E_MARGIN,E_MARK],\n   \"ref_check\":[rc(\"POK:738\",\"supports\",POK738)],\n   \"consulted\":[cs(\"POK\",\"p. 738 s.v. mereg-\",\"supports\",POK738),\n                cs(\"WLD\",\"Bd. II p. 283\",\"partial\",WLD283),\n                cs(\"AHD\",\"Watkins 1985 s.v. merg-\",\"supports\",AHD_MERG),\n                cs(\"IEC\",\"Mann s.v. marǵos\",\"supports\",IEC_MARG),\n                cs(\"SYN\",\"Buck, ch. on 'boundary'\",\"supports\",SYN_MARG)],\n   \"nodes\":e0_nodes},\n  {\"entry\":2,\n   \"root\":\"Merk\",\n   \"verdict\":\"plausible\",\n   \"modern_form\":\"PIE *merk͝- 'to grasp, seize' (Pokorny 739); but the Latin merx-family is usually assigned to a separate Italic root merk- 'commerce', possibly Etruscan (Watkins merk-²)\",\n   \"note\":\"The root box itself is accurate as far as it goes: Pokorny p. 739 does have 'merk͝- ‚fassen, ergreifen‘' (Skt. mṛśáti 'touches, takes hold', Gk. márptō, Gk. hárptis 'robber'), so the language label and the gloss 'to take, grasp' are right. What is doubtful is the whole tree Nourai hangs from it. Pokorny himself attaches the Latin family only with a caveat — 'fraglich ist Zugehörigkeit von lat. merx ‚Ware‘, merces, -edis … mercārī ‚handeln‘'. Watkins goes further and lists the commerce words as a separate BRACKETED root, his notation for a non-Indo-European item: '[merk-2. Italic root, possibly from Etruscan, referring to aspects of commerce … [In Pok. merk- 739.]]'. Ernout-Meillet: 'merx … sans étymologie i.-e. sûre'; Klein: 'merx … which is of uncertain origin'; de Vaan reconstructs only Proto-Italic *merks and suspects an Etruscan source for the whole economic stem (Mercurius included). Against that, recent work has tried to make merx Indo-European again after all: Nikolaev derives it from *merkʷ- with Gk. márptō and Tocharian A märk- 'take away' — essentially Nourai's arrow — while Matasović would instead attach it to *merǵ- 'to divide', i.e. to the root of the preceding entry on this very page. So 'plausible': a defensible minority position, not the consensus. Verdicts below are given per node accordingly.\",\n   \"note_fa\":\"خودِ ریشه درست است: پوکورنی در ص ۷۳۹ ریشة *merk͝- «گرفتن، چنگ زدن» را با سنسکریت mṛśáti و یونانی márptō می‌آورد؛ پس برچسب و معنا صحیح است. اما پیوستنِ خانوادة لاتینی merx به این ریشه محلّ تردید است: خودِ پوکورنی آن را «fraglich» می‌خواند، واتکینز آن را ریشة جداگانة ایتالیکی و احتمالاً اتروسکی می‌شمارد (در کروشه، که نشانة غیرهندواروپایی بودن است)، و ارنو-میه و کلاین و دووان آن را «بی‌ریشة مطمئن» می‌دانند. در مقابل، پژوهش‌های تازه (نیکولایف) باز ریشة *merkʷ- را با همان معنای «گرفتن» بازسازی کرده‌اند. پس ادعای نورایی با احتیاط پذیرفتنی است، نه رای غالب.\",\n   \"sources\":[W_MERX,W_MERC],\n   \"ref_check\":[rc(\"POK:739\",\"partial\",POK739)],\n   \"consulted\":[cs(\"POK\",\"p. 739 s.v. merk͝-\",\"partial\",POK739),\n                cs(\"AHD\",\"Watkins 1985 s.v. merk-² (bracketed)\",\"contradicts\",AHD_MERK),\n                cs(\"LAT\",\"Ernout-Meillet pp. 712-713 + index\",\"contradicts\",LAT_MERX),\n                cs(\"KLN\",\"s.v. mercantile, Mercury\",\"contradicts\",KLN_MERC+\" \"+KLN_MERCUR),\n                cs(\"WLD\",\"WP II 283 (cited by Pokorny for merk͝-)\",\"partial\",\"Pokorny's bibliography line for merk͝- is 'WP. II 283, WH. II 78 f.'; the same Walde-Pokorny page carries the border-words discussed in entry 0, and WP likewise offers no confident IE etymology for merx.\")],\n   \"nodes\":e2_nodes},\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-337.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk337.py && python3 -m json.tool data/verification/page-337.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 337"
}
```


### [2026-09-07T16:38:36.294Z] TOOL RESULT

```
written
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 12, 'transcription_suspect': 2, 'disputed': 2, 'plausible': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'partial': 5, 'supports': 6, 'not_checked': 8, 'contradicts': 1}
books consulted: {'supports': 36, 'partial': 13, 'silent': 1, 'contradicts': 7} | by book: {'KLN': 14, 'AHD': 8, 'SKT': 7, 'POK': 4, 'LAT': 4, 'LKT': 3, 'MON': 3, 'NYB': 2, 'WLD': 2, 'IEC': 2, 'HJB': 2, 'BRT': 1, 'SYN': 1, 'PHD': 1, 'HRN': 1, 'HUB': 1, 'BQT': 1}
```


## [2026-09-07T16:38:43.049Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport io\np='data/verification/page-337.json'\ns=io.open(p,encoding='utf-8').read()\nfor a,b in [(\"همانجا می‌آوردد\",\"همان‌جا می‌آورد\"),(\"متنازر\",\"متناظر\"),(\"ترکی عمانی\",\"ترکی عثمانی\")]:\n    print(a, s.count(a)); s=s.replace(a,b)\nio.open(p,'w',encoding='utf-8').write(s)\nEOF\npython3 -m json.tool data/verification/page-337.json > /dev/null && echo OK && python3 tools/verify_check.py 337 | tail -8"
}
```


### [2026-09-07T16:38:44.454Z] TOOL RESULT

```
همانجا می‌آوردد 1
متنازر 1
ترکی عمانی 1
OK
nodes verified: 18/18
node verdicts: {'confirmed': 12, 'transcription_suspect': 2, 'disputed': 2, 'plausible': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'partial': 5, 'supports': 6, 'not_checked': 8, 'contradicts': 1}
books consulted: {'supports': 36, 'partial': 13, 'silent': 1, 'contradicts': 7} | by book: {'KLN': 14, 'AHD': 8, 'SKT': 7, 'POK': 4, 'LAT': 4, 'LKT': 3, 'MON': 3, 'NYB': 2, 'WLD': 2, 'IEC': 2, 'HJB': 2, 'BRT': 1, 'SYN': 1, 'PHD': 1, 'HRN': 1, 'HUB': 1, 'BQT': 1}
```


## [2026-09-07T16:39:01.478Z] AGENT

Page 337 (book p. 307) verified — `data/verification/page-337.json` written, `verify_check.py 337` shows 18/18 nodes and 0 PROBLEM lines.

**Verdicts:** roots 1 confirmed (Merg/Mereg), 1 plausible (Merk). Nodes: 12 confirmed, 2 plausible, 2 disputed, 2 transcription_suspect. Ref checks: 6 supports, 5 partial, 1 contradicts, 8 not_checked (mostly boxes with no printed citation).

**Disputed / transcription_suspect**
- **Merk #3 Portuguese "cumerx : trade"** — disputed. No such Portuguese word (comércio), and Portuguese is not the channel: Lokotsch 751 and Hobson-Jobson 384 both give Latin *commercium* → Byz. Greek κομμέρκιον → Ottoman Turkish *gümrük*.
- **Merk #4 Persian gomrok / gambroon** — disputed on both halves. گمرک is a Turkish loan (Mo'in tags it «مأخوذ از ترکی»; Dehkhoda: Greek → Turkish after 1453), not via Italian/Portuguese; and گمبرون (Gombroon = Bandar Abbas) is a place name that Nourai's own cited HJB:384 explicitly rejects deriving from *gümrük* ("seems hardly probable"), preferring Pers. *kamrūn* / Port. *camarão* 'shrimp'.
- **Merk #1 Latin "merx, comerx"** — transcription_suspect, `error_in: book`. *comerx* is not Latin; Nourai has compressed con- + merx (= commercium). Derivation itself rated plausible (Pokorny 739 lists merx but calls it "fraglich"; Watkins brackets merk-² as Italic/possibly Etruscan; Nikolaev's *merkʷ- revives Nourai's link).
- **Merk #2 Italian "commerci"** — transcription_suspect, `error_in: book`. Italian is *commercio*; "commerci" is the plural.
- **Merk #6 Latin merces / Mercurius** and **#11 Persian مرکور، مرکورکرم** — plausible: Klein says Mercurius is Etruscan *Mercura, "prob. not related to L. merx"; and مرکورکرم renders the American trade name Mercurochrome (Dehkhoda), not a French word.

**No extraction errors.** The JSON matches the printed page exactly in every box (page image saved to `data/verification/sources/refs/ocr/BOOK/337.png`); all odd forms are the book's own.

Notable positive finds: POK:738, KLN:940 ("cogn. with Avestic marǝza, 'border'" — page marker 940 confirmed), and BQT:1986 (Mo'in's footnote 4 s.v. مرز, giving Av. marəza- → Pahl. marz/marzbān → NP marz) all check out verbatim; BRT col. 1153, NYB, PHD, HRN 974, HUB, IEC and Buck all corroborate the Avestan→Persian link. 13 web pages archived via `fetch_source.py`.
