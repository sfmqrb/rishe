# Verification process log — verify-page-282


## [2026-09-06T21:33:32.950Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 282 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-282.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-282.json. Write /home/sfmqrb/git/rishe/data/verification/page-282.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 282` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:33:34.623Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:33:35.257Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:33:35.273Z] TOOL RESULT

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


## [2026-09-06T21:33:35.580Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-282.txt"
}
```


### [2026-09-06T21:33:35.604Z] TOOL RESULT

```
1	=== PDF page 282 (book page 252) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ksîro : milk  (refs WLD1:503)
4	#1 (parent #0) [Avestan] refs=AHD:1175; HRN:178; SOD:29 | xšîra, xšvipata : milk ; apa-xšîra : milk
5	  #2 (parent #1) [Persian] refs=SYN:385; BQT:1322; HRN:178; MON:2108,5187; ETM:69 | šîr 1 «شیر ۱ ( شیرین ، شیرینی )» : milk ; šîr-o-šekar «شیروشکر» : milk and sugar, a kind of silk fabric ; ham-šîreh «همشیره» : sister
6	    #3 (parent #2) [Hindustani] refs=None | 
7	      #4 (parent #3) [English] refs=AHD:1175; KLN:1411 | seersucker : a cotton fabric with a striped pattern
8	#5 (parent #0) [Sogdian] refs=SOD:29,82 | `xšy`bt : milk
9	#6 (parent #0) [Sanskrit] refs=WLD1:503; SYN:385 | kšîra : milk
10	--- entry 1 ---
11	ROOT [Indo-European] Ksudros, Qusudros : coarse, granular, crushed in small pieces  (refs IEC:576,1060)
12	#1 (parent #0) [Avestan] refs=BQT:729; IEC:576,1060 | xšudram : seed ; xvareta : small
13	  #2 (parent #1) [Pahlavi] refs=BQT | kvart : small
14	    #3 (parent #2) [Persian] refs=BQT:729; IEC:576,1060 | xord «خُرد ( خرده ، خردسال )» : small
15	#4 (parent #0) [Sanskrit] refs=IEC:576 | ksudrah : small
16	#5 (parent #0) [Armenian] refs=IEC:576 | xord : small
17	
```


## [2026-09-06T21:33:39.615Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-282.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-06T21:33:39.658Z] TOOL RESULT

```
{
  "pdf_page": 282,
  "book_page": 252,
  "entries": [
    {
      "root": {
        "name": "Ksîro",
        "lang": "Indo-European",
        "refs": "WLD1:503",
        "gloss": "milk"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "AHD:1175; HRN:178; SOD:29",
          "words": [
            {"translit": "xšîra, xšvipata", "gloss": "milk", "script": null},
            {"translit": "apa-xšîra", "gloss": "milk", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "SYN:385; BQT:1322; HRN:178; MON:2108,5187; ETM:69",
          "words": [
            {"translit": "šîr 1", "gloss": "milk", "script": "شیر ۱ ( شیرین ، شیرینی )"},
            {"translit": "šîr-o-šekar", "gloss": "milk and sugar, a kind of silk fabric", "script": "شیروشکر"},
            {"translit": "ham-šîreh", "gloss": "sister", "script": "همشیره"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "تا تو تاریک و ملول و تیره ای - دان که با دیو لعین همشیره ای", "poet": "Molavî"}
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Hindustani",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:1175; KLN:1411",
          "words": [
            {"translit": "seersucker", "gloss": "a cotton fabric with a striped pattern", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:29,82",
          "words": [
            {"translit": "`xšy`bt", "gloss": "milk", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "WLD1:503; SYN:385",
          "words": [
            {"translit": "kšîra", "gloss": "milk", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ksudros, Qusudros",
        "lang": "Indo-European",
        "refs": "IEC:576,1060",
        "gloss": "coarse, granular, crushed in small pieces"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:729; IEC:576,1060",
          "words": [
            {"translit": "xšudram", "gloss": "seed", "script": null},
            {"translit": "xvareta", "gloss": "small", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT",
          "words": [
            {"translit": "kvart", "gloss": "small", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:729; IEC:576,1060",
          "words": [
            {"translit": "xord", "gloss": "small", "script": "خُرد ( خرده ، خردسال )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "چند استخوان که هاون دوران روزگار - خُردش چنان بکوفت که خاکش غبار کرد", "poet": "Sa`dî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:576",
          "words": [
            {"translit": "ksudrah", "gloss": "small", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Armenian",
          "refs": "IEC:576",
          "words": [
            {"translit": "xord", "gloss": "small", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== MATRIX ===
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


## [2026-09-06T21:33:41.723Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['WLD','AHD','HRN','SOD','SYN','BQT','MON','ETM','KLN','IEC','POK','PHD','NYB','BRT','CHEUNG','ARY','HUB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-06T21:33:43.472Z] TOOL RESULT

```
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_ety
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
```


## [2026-09-06T21:34:09.678Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/ | head -30; echo ---; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-259.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False)[:3000])\n\"",
 "description": "Look at a prior verification file for format"
}
```


### [2026-09-06T21:34:11.524Z] TOOL RESULT

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
---
{"entry": 0, "root": "Kerd 1, Kred", "verdict": "confirmed", "modern_form": "PIE *ḱḗr, oblique stem *ḱr̥d- (root *ḱerd-) 'heart'; with the compound *ḱred-dʰeh₁- 'to place one's heart, trust'", "note": "Pokorny p.579 bottom–580 heads the entry exactly '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’', so Nourai's headword 'Kerd 1, Kred', the language label 'Indo-European' and the gloss 'heart' all reproduce his source correctly; AHD (Watkins) has 'kerd-1. Heart. [Pok. kered- 579.]'. The one substantive caveat concerns the 'kred-' half: Pokorny himself (p.580) says the kred-dhē- 'believe' group is 'nicht hierher' (not to be connected with 'heart'), and Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree; modern standard works (Watkins/AHD, de Vaan 2008 s.v. crēdō, Wiktionary) do connect it, analysing *ḱred-dʰeh₁- as 'to place one's heart'. Nourai therefore follows the newer, now dominant, view — but not the page of Pokorny he cites. The Iranian branch has a further complication that the chart passes over: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, Av. zərəd-, PII *ȷ́ʰā́rd) where *ḱ- is expected, 'unexplained voiced aspiration' (Wiktionary), 'mit init. as if fr. IE gh, due to a blend with some other word' (Buck 251).", "note_fa": "ریشهٔ هندواروپایی آغازین *ḱḗr (ستاک غیرفاعلی *ḱr̥d-، ریشهٔ *ḱerd-) به معنی «دل، قلب» است و پوکورنی در ص ۵۷۹–۵۸۰ سرواژه را دقیقاً «kerd-, kērd-, kr̥d-, kred-: Herz» آورده؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ محل بحث بخش kred- است: خودِ پوکورنی در ص ۵۸۰ پیوند kred-dhē- «باور داشتن» را با «دل» رد می‌کند و باک و کلاین و ارنو–مه‌یه نیز همین نظر را دارند، اما واتکینز (AHD)، دِ وان و ویکی‌واژه آن را می‌پذیرند و *ḱred-dʰeh₁- را «دل نهادن» می‌دانند؛ یعنی نورایی از دیدگاه نو پیروی کرده است نه از صفحه‌ای که به آن ارجاع داده. نکتهٔ دیگر آنکه در هندوایرانی به جای *ḱ- انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-، اوستایی zərəd-) که هنوز توضیح قطعی ندارد.", "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r", "https://en.wiktionary.org/wiki/credo%23Latin", "https://www.etymonline.com/word/heart"], "ref_check": [{"ref": "POK:579", "status": "supports", "note": "Pokorny IEW p.579 (bottom) – 580, read in POK_02.txt leaf 239–240 (awk 'BEGIN{RS=\"\\f\"} NR==239'): '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’. Arm. sirt … gr. καρδία (att.), κραδίη (hom.) … lat. cor (aus *cord) … got. hairto, ahd. herza, ags. heorte, anord. hjarta n. ‘Herz’ (*ḱērd-on-)'. Exactly Nourai's root name and gloss."}, {"ref": "SYN:251", "status": "supports", "note": "Buck, Selected Synonyms p.251 = §4.44 HEART (SYN.txt leaf 289, page number '251' printed in the running head above '4.44 HEART'): 'Most of the words for ‘heart’ belong to an inherited group … 1. IE *ḱerd-, etc., with gradation. Walde-P. 1.423 ff. Ernout-M. 219 f.'"}], "consulted": [{"src": "AHD", "where": "Watkins 1985, s.v. kerd-1 (AHD_watkins1985.txt line 621)", "stance": "supports", "note": "'kerd-
```


## [2026-09-06T21:34:11.985Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['WLD','AHD','HRN','SOD','SYN','BQT','IEC','KLN','BRT','PHD','MON']:\n    v=d.get(k) or {}\n    print('==',k, '| offset:', v.get('page_offset'), '| local:', v.get('local_file'), '| hint:', (v.get('lookup_hint') or '')[:300])\n\"",
 "description": "Page offsets for needed refs"
}
```


### [2026-09-06T21:34:13.669Z] TOOL RESULT

```
== WLD | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== AHD | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== HRN | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== SOD | offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== SYN | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== IEC | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== BRT | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== MON | offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
```


## [2026-09-06T21:34:19.099Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 282 -l 282 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg282 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 282"
}
```


### [2026-09-06T21:34:21.513Z] TOOL RESULT

```
total 23588
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:34 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     484 Sep  6 17:33 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   76489 Sep  6 17:24 bqt1237_foot.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51778 Sep  6 17:32 mk276.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70575 Sep  6 17:34 pg282.png
```


## [2026-09-06T21:34:22.641Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC ksudr ===\"; grep -n -i 'ksudr\\|kseudr\\|qsudr\\|qusudr' IEC.txt | head -20; echo \"=== IEC ksir ===\"; grep -n -i '^ksir\\|^ksīr\\|ksiro' IEC.txt | head -20; echo \"=== AHD kseiro ===\"; grep -n -i 'kseiro\\|ksiro\\|seersucker' AHD_watkins1985.txt | head; echo \"=== SYN milk 385 ===\"; grep -n 'kṣīra\\|ksira\\|xšīra\\|xsira' SYN.txt | head -20",
 "description": "Grep IEC, AHD, SYN"
}
```


### [2026-09-06T21:34:22.724Z] TOOL RESULT

```
=== IEC ksudr ===
8230:ksudros (skudhros) ‘coarse, granular; coarse- ness, granules, grit’. Cf. also qusudros, skudh- ros Skt. ksudráh ‘small, fine’; Prakritic ksulla-, id. cf. Romani čulo, adv. ‘little’; (e-gde in) Skt. ksódàmi ‘pulverize’; Av. xsudrom “seed”; Per. xurd ‘small’; Arm. xord ‘sackcloth’; G cf. (with *-dh-) Schotter “clinkers, road-metal, shingle'
14335:do, Siditi, v. ‘scorn, if fr. *qusiüd-, but *ksiüd- is possible; and ON skjóttr *piebald' ofa horse) quseudros (qusudros) ‘bent, awry, wrong, false? ; Arm. (zero-gde) xotor ‘awry’; Gk. psudrós ‘false’; Moravian šídrý, adj. 'awry. (Iso- phonic: Blg. šùdrav (1) ‘dirty’) quseuið (quseuð, qusëuãið) "come, become, happen’. Phonol. ambig. (ks-?) Per. šavam, inf; šūdan, v. ‘become, happen’; Blg. (long-gde) šàvam, tr. and intr. ‘sway; move; go; depart’; cf. also šàvra, tr. intr. ‘move’; R cf. ševeliť, inf. tr. ‘stir, move’ qusibà, ið “sway, swish; whip, lash’; qusibos, à, S. id. Skt. ksibami, v. "be drunk’; kgibah, adj. ‘tipsy’: Ir. cf. síobaim, v. “blow, gust? beside sfobhas, m. (Frage, fr. *qusibost-, if here); Welsh chwi- fio, inf. (fly round, wander round beside (short vowel) chwyfio, v. ‘move’; OCS cf. ši- bajo, ati, v. ‘flog’ beside R o-Sibit'sa, inf. ‘err’; za-Sibit, inf. “hurt, bruise’; cf. also R &ibkij ‘swift; ó-Sib, m. ‘tail, brush’; po-Sib, m. “style, manner’; OCS šiba, f. ‘lash’; Srb. šib *brush- wood. Variant of type squib- in OE swipian, ON svipa, v. “flog? beside (long-vowel) EME to swipe, v. id.; swipe, s. ^well-beam', cf. MHG swifen, sv. L “move, go' and (*-i- in) Du. zwiepen, v. ‘lash, flog; totter, sway’. The Gmc. forms display all the variants of sense seen in the Slavonic forms. Cf. also (short vowel in) LG swipp, adj. ‘dashing; shrill’. (The phonology of Lat. vibrāre is uncertain) qusidh- ‘whizz, whistle, blow, whisper. Onomat. Gk. cf. psithurós, On. mn. ‘whisper’; Lat. si- bilus, um, mn. “hiss? beside the Umbrianism implied in OLat. sifilare, Fr. siffler, but Sp. silbar, inf. ‘whisper’; cf. Rumansch sivel, m. ‘blast’; MIr. & Ir. sidhe, m. id.; Br. chwéza, inf. ‘blow, inflate’; chwéz, m. ‘blast’; W chwyddo, inf. ‘swell’; chwydd, m. ‘swelling’. Variants implied in Skt. ksvid-, vb. root “hiss, whizz’ and in Ukr. švydkyj, adj. “swift? qusiið (qusinið) “crush, destroy” Skt. ksinómi, ksinami, v. “destroy” beside ksih, f. ‘destruction’; Av. xSi-, id.; Gk. psío, v. ‘crush’. Extns. of this root are seen in Gk.
14336:quseudros (qusudros) — quso£os, à, us
14376:qusoudhos ‘puny’. Cf. qusudros & ksud-. (Phonology indeterminate in some instances) Skt. cf. ksódhukah, adj. dim. type “hungry”; Av. šud-, v. ‘hunger’ beside Suðo, m. id. (both z-gde); cf. Gk. (?) psüthos, n. (ffalsehood". Infl. of type quseud-, q. v.); ON sauór, pl. sau- ðir, s. sheep’, lit. small animal"); OCS xudŭ, adj. ‘little’; Blg. xud, Srb. hud, adj. ‘bad’; OCz. & Cz. chudý, adj. ‘poor’; Moravian ‘slim, thin’; Ukr. cf. xudoba “cattle?
14377:qusudros ‘worn, granular’. Cf. ksudh- (sic) and qusoudhos. (Phonol. ambig. in some in- stances). WP I, 502 (Various reflexes in Iran.) Skt. ksudráh, adj. ‘crushed; small; humble; mean’; Av. xšudrəm, n. geed Per. cf. (from various dialects) xurd ‘minute, tiny’; sūdan, pp: süde, v. (rub, wear down’, fr. *Ksud- ?); sul ‘feeble, weak-willed'; Romani: cf. culo, adv. "little; Gk. cf. psüdrakes, fpl., & psudrá- kia, npl. ‘pimples, rash’. Radical in Av. x3ud-, v. “pound, crush?
=== IEC ksir ===
8190:ksirom “milk, derivative of milk’. Cf. skir-.
8201:ksirp- ‘sword, reed, iris’. Cf. WP II, 501 Oss. áxsirf, àxsirf ‘sickle’; Lat. sirpus, scirpus, m. ‘rush, reed’. (Olr serr, Ir. searr ‘scythe, sickle, sword” seems to represent a type *serp-, see sIp-). Cf. Oss. àxsirf ámbal "lamb's entrails roasted on a spit
15535:skeir- (skheir-, skhir-) ‘product of soured milk’. Cf. skir-, ksirom Oss. Ciri, Digor. Kere, s. fcheese-cake'; Arm. xer, O-st. (‘dish of beestings'. Cf. for phonol. lezu ‘tongue’: Li. liežuvis), Alb. hirrë, f. Cwhey', perh. fr. *skirs-, but vocalism may be *-ei- cf. dimén: Gk. kheima)
=== AHD kseiro ===
=== SYN milk 385 ===
9677:; cre. hese ofr. $4 ic, NE sugar), Fr. su- | s.v. sugar. snr, sures 5.86 MILK (sb.) Goth. miluks Lith. pienas yada ON mjolk Lett. piens edo Dan. melk ChSl. mléko lac Sw.  mjolk SCr.  mlijeko latte OE meole, mile Boh. mléko lait ME  melk Pol. —-mleko ee NE milk Russ. moloko aple Du. melk Skt.  payas-, ksira- milicht, 288, Bx OHG miluh Ay. payah-, xbvid- Drath, Buth MHG milich, milch : NHG_ milch
9706:Goth. .--- u Lett. szers ostr % a Den. a ae caseus . Sw. ost z B ‘i td. , 1 maggias caer? OE _ ciese, cése oh.  syr (tvaroh) henge ME chese Pol. ser (twarég) ie NE cheese Russ. syr (trorog) FG  brinzd Du. ‘aas Skt.  (dadhi-ja-, ksira-ja-) * aise OHG chast Av. fsula- (tiiri-) It ogise MHG kese alos NHG kaise
```


## [2026-09-06T21:34:37.535Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndef leafof(path, linenos):\n    txt=open(path,encoding='utf-8',errors='replace').read()\n    # map line -> leaf\n    lines=txt.split('\\n')\n    leaf=0; res={}\n    want=set(linenos)\n    for i,l in enumerate(lines,1):\n        if i in want: res[i]=leaf\n        leaf+=l.count('\\f')\n    return res\nprint('IEC', leafof('IEC.txt',[8190,8201,8230,14335,14336,14376,14377]))\nprint('SYN', leafof('SYN.txt',[9677,9706]))\nEOF",
 "description": "Compute leaf numbers for IEC/SYN hits"
}
```


## [2026-09-06T21:34:39.089Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT xsvipta / xsira ===\"; grep -n \"xšvip\\|x&vip\\|xsvip\\|xšīra\\|xšira\\|Milch'\" BRT.txt | head -30",
 "description": "Grep Bartholomae for milk words"
}
```


### [2026-09-06T21:34:39.857Z] TOOL RESULT

```
IEC {8190: 326, 8201: 326, 8230: 327, 14335: 585, 14336: 586, 14376: 587, 14377: 587}
SYN {9677: 431, 9706: 433}
```


### [2026-09-06T21:34:39.896Z] TOOL RESULT

```
=== BRT xsvipta / xsira ===
7542:•  j.,  g.  ä-zutay-  f.''  'Fett,  Schmalz':  raoy- nyqtn  i'aranhim  "suitlmca  urvaranqm  Yt. /2.3.  a)  überhaupt  sva.  'feste  Ndirung' gegenüber  der  flüssigen,  im  Gegensatz  zu ' xsi'td-  'Milch' :  pars  xsvisät  (sd.)  -zaitUca  "  1 girii mal  V.  13. z8;  — xhioaica  'sBlayaEca  ■> ^.68.2;  —  t!m  'iSdiis'''  ahurB  mq%r)m tasal  .  .  mazdä  gavei  xhildimcil  *ki'B.- umiaHbys  spmt3  säsnayä  "das  Wort  vom Fett  hat  AhM. ..  für  das  Rind  geschaffen und  die  Milch  für  die  Nahrung  begehren- den durch  sein  Gebot,  der  heilige"  Y. 29.71'.  a)  Du.  in  Verbindung  mit  xhild- Du.:  xsviöa  'zütH  yazamaide  .  .  ilzSis  .  . hamsistri  \.i6.8.  2)  'Üppigkeit,  strotzende Kraft  und  Fülle':  vaKuAlm  'zBülm*^  . . frasasttm  .  .   *p3r»ndlm  yazamaidl  Y.jS.
10138:—  tistryS ..vaz»mnö  -Jus  k)hrpa  zaranyS.-  bagä  x^ar^mnif  (sd.)  Y. 32. 8;  —  "Su/x'ar»- srvahe  YLÄ16;  i4-l,  Y.ig.yi.  A)  Das  \%ahe  nr^yJ  V.7.  43; — 'Sul  vä  s^var3%ahe Rind  gilt  als  Repräsentant  aller  nützlichen  j  (sd.)  vä  W.14.1T,  —  '!us  i^ar/itinqm {ahumohtn)  Tiere,  daher  ^gav-  auch  inJH, /.  5;  —  yasca  ..  lanumazs {^A.)  'Jui weiterem  Sinn  gebraucht  wird*"':  para\da%at  "W-iS.!!);  —  °amla  ifsst)m  anäp»m •Su^  ca^war).paitistanaya  dänheit  para\{%d.)  V.5,  52;  S3f.',  7.55;  —  buiri 'aas  ,  . nars  asaotiB  bipaittstänahe  zq%st  Y.  /p.  8 ;  j  3far>^a  . .  VyL  4:5.  3)  'Milch',  bes.  zur
10985:•  j.,  g.  xSvid-  m.  'Milch';  im  Gegensatz zu  axBtay-  (sd.)  überhaupt  'flüssige  Nah- rung' im  Gegensatz  zu  fester:  pars  °isca (NS.)  äsaitisca'^  gsui  mal  "hervor  (geholt werde)  Milch  und  Fett  samrat  Fleisch" V.13.2%;  —  ■ilaica  (DS.)  azStayalFa''> Y.ßS.ii  —  am  äiStBis(sd.)  aAurB mohnm tasat  .  .  gavSi  'lihmlä'''  * AvS urusalibyS V.  25,  7;  —  *mmdäidyäi  (sd.)  «ftfem^)  Y. 1/.9.  a)  Du.  in  Verbindung  mit  äsütay- Du.:  "röa  (AD.)  äzuiti  yazamaiäeY.iG.Z; zit.  *F,5.  a)  pasca  xsavaidlm  ayara- namca  (soll  heissen)  "nach  sechs*'  Tagen" Vd.5.
10988:PDa.  xewd,  PDS.  jvicrf'Milch'').  —  Pü.:  iirö- mand.  —  ')  Im  Gegensatz  zu  patmavant:  — ■)  VII.  ist  "ilvifla-  eig.  das  'herausge  sehn  eilte', d.i.  'gemolkene',  PPfP.[  vgl.  xivofpä-  und  ai.
11659:KompE.—  Zum  V.  '^gay-.  —  Pü.  (lu  Y.  62): tfitwii*!),  (inY-^iJ):  transskr.,  loitderErL; ffi-  CMilch')').  —  ')  So  ist  statt  säyiinlh  m lesen,  vgL  Gab.  6.  3  und  Npü.;  ändagl.  Da- mit stimmt  auch  die  PüErl. :  läk  man  afaga- yeht^sA.)  mä  iavät  ...  S.  auch  Pü.  zu  iuji- tajr-,  dar3TS.Jitay:  —  ')  Vgl.  zu  BicüianI-.
14792:Ableit.  aus  *paena-  m.  'Honig'');  mp.  attgu- fin,  np.  angHÜn  'Bienenhonig'.  —  Ob  zu  lit. /Ami  'Milch'?  {s.  daiu  JSchmidt  Krit.  :<h)'). —  Pü.:  fehlt. —  ")  So  der  Ausgang  in  T.  — >)  Die  Bedeutung  'Milch'  ist  für  *ptüna-  nicht wahrscheinlich,  obwohl  sich  ja  np.  anpibln allenralls  als  'Bienen milch' fassen  Hesse;  vgl. Hb«.  PSL  19,  AGr.  /.  124.
14800:•  '].  paema'vant-  Adj.,  nur  fem.  'vaili- 'die  mit  Muttermilch  versehen  ist"h  °vaHi xsviptavaiH  (VSf.)  V.  21.  7.
15285:•  j.  'payah-  n.  'Milch',  auch  Plur.:  *'yB F.  10  i  —  nsit  *yB  fsuta  (sd.) , .  toit  gstd . . ^■7-  77;  —  aipi.yiaurvatqm  aspayanqm^a °yar3hqm  gävayanamcä  malsinatiqmca  buz- yanqmla  hqm.vaoirinqm  la.vaoirinqm  V. 5.  5a;  —  rafu/ris  *°ySbls'^^  sfastiisca a:^ästäisca  N.57.  a)  mit  'tütrya-  Adj. 'Molke':  taitya  (sd.)  paya  bavat  aspa- yüaiea  *'xaraySaJ/a  "die  Molke  kann  von
```


## [2026-09-06T21:34:51.837Z] TOOL CALL #11: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg282.png"
}
```


### [2026-09-06T21:34:52.295Z] TOOL RESULT

```

```


## [2026-09-06T21:34:52.293Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T21:35:05.682Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD xwurd/xward ===\"; grep -n \"^xward\\|^xwurd\\|^xwar\\b\\|^xwurdag\" PHD.txt | head -20; echo \"--- PHD sir ---\"; grep -n \"^šīr\\|^šir\\|milk\" PHD.txt | head -20; echo \"=== NYB ===\"; grep -n \"xvart\\|xvurt\\|xward\\|'milk'\\|šīr\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-06T21:35:05.748Z] TOOL RESULT

```
=== PHD xwurd/xward ===
664:xwarüfrün 96 yal
665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
--- PHD sir ---
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
414:jawédan [LOLMN < А l-Imn; ywyt?n' | (P y'wyd?n, M Pyn), N ~] eternally, always. ~ag [-k! | (P -g), N ~a] eternal, perpetual. jawén [S£yn! | № jawin] made of barley. jeh [yh, yyh = Av. jahi-] the Whore, female arch-demon. fiw [суш!, yyw! = Av. fiwya-] (consecrated) milk. *jomā [ywm’y] together with; both. jorda [ywilt’y, 2k | (P yw?rd?w), J *jwrd?r] corn, grain. jo(y) [ywd, ywb! | N ~] stream, channel. Jóy-, -išn, v. Jadan. jud [ywdt' | M jwd] separate, different; anti-. ~ az [N juz] except, apart from. judàg [ywd? h! | N juda] separate, different. ~ih: separation, difference. Jūdan, jóy- [ywtn!, ywd- | M jwwdn, (jw-), (N jawruan)] chew; devour (daevic). „išn: eating (daevic). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk!] schismatic, heretic. ~th: heresy. Juy [усе | N ~] yoke. Jumbāģīh [ywmb’kyh] motion. jumbénidan, jumbén- [ywmbyn-yin'] (cause to) move. jumbidan, jumb- [ywmb-yin' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- [ywmbyh-stn'] be moved. juttar [ywdtl | M jwtr] different, otherwise. --īh: opposite, reverse. Juwān [ywb?n! | (P ywn), N jawàn] young; a youth. ~th: youth. juxt [ywht! | (P ywxt), N juft!] pair, couple.
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
457:mäst [m'st! | N <] curds, sour milk.
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
585:šimšār Lë"! | N ~] box tree. Sir [HLBA < A hlb’; $1 | M šyyr, N ~] milk. šīrēn [5/yn! | M syryn, N ~in] sweet. ~ih: sweetness. SiSag [$y$k! | N fifa) bottle, flask. škaft [Ар] = Skeft. škāftan, škāf- [sk’p-tn' | M ‘kk’ pt, N fikáftan] split, burst. Skarag [skik! | P *škr-] (bird) of prey. škarwīdan, škarw- [fklw-ytn' | M ‘fkrw-st, N fikarfidan] stumble, stagger. škastan, Sken(n)- [TBLWN-tn' < A N tbr; škstn!, škyn- | M ‘tkn-, N stkastan, fikan-] break. ^ i$n: breaking. škēbāģ [fkyp?k! | P kyb-, N #hëba] patient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] be broken. Skóf-, у. Skuftan. Skdfag [fRwpk! | N šukēfa] flower, blossom. Skoft [škwpt'] = škeft. 1$kóh [ол | M Ай] poor. --īh: poverty. *§k6h [kwh | N sukdh] dignity, majesty; fear. škuftan, &ЕбЇ- [škwp-tn! | N fukuftan] flower, blossom. Énàs-, v. Snaxtan. šnàsag [fn'sk! | P *$n*sg] knowing, knower; sense. ~ih: knowledge. šnāxtan, $nàs- [fm htn!, fie | M хіп, Чи s-, N fin-] know, recog- nize. šnāyēnīdan, šnāyēn- [sz dyn-ytn'] please, propitiate. ~išn: happiness. šnāyīdan, šnāy- [fr'd-ytn!] praise, propitiate. --i$n : praise, gratitude. šnāz [frc | (N šinā(w))] swimming. šnāzīdan, šnāz- [fr'c-ytn! | M $2? 2-, (IN šināw-)] swim. $nóhr [snwhl | М *fnwhr] gratitude, contentment. šnūmaģ [fnwmk! | M *fnwm-] satisfaction, contentment. &nó&ag [šnwšk! | N šunoša] sneeze. $nüg [šnwk' | M *fnwg] knee. šnūman [fnwmn! = Av. xsniimaine] propitiation. 86n [swn'] kind, manner. ~ig [-yk!] customary, ordinary. šūy-, v. Sustan. Sdy [std | N ~] husband.
1127:buttermilk, dried ~ kašk.
2806:milk (n.) jiw, pém, Sir; sour ~ mast.
2807:milk (v.) dóxtan, (dēšīdan).
=== NYB ===
649:ArtaxSér ['Ithšdl] = Artaxsahr, 1-17, passim. 117°. 1201-2 (v. also nev-— and Véh-—), Artašēr [ltšdl] 11571. 116? sq. — Olr Arta-xsadra-, cf s. v. Art-vahist and šahr; OP Arta-xšaca-; KZŠ, Gr. v. Apta- Eeto, -Eep, -Ero (the common Gr. ’Apra- Eep&ng is influenced by HépEns); NP Ar- dašīr. Ci Bailey, BSOAS XIII, 1949, 123. Hence
2347:kurušk [kwlwšk'] ewe, of a big species of sheep 509-11, — Zsprm X, 20 in telling this story: meš kurušk i šīr-pistān "with milk in her udder’. Also kwryšk' = Paz. kurišk, koriák, BdA, p. 959-1? = BdJ2918— 303: meš 5 sratak: han i pat-dumb, han 4 a-dumb, u sak meš, u meš *takilé [tkly ; Paz. tagr, tgar] <u> kurišk tmeš, ke srub vazurg, asp homänäk, 3 köf [BdA corrected from tan, BdJ Paz. koh] dārēt api-š 6 bārak girénd, cigēn gobet ku Mānušcihr + amāh niyak kurišk-ē pat bārak dāšt [sak
```


## [2026-09-06T21:35:07.130Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN seersucker ===\"; grep -n \"seersucker\\|Seersucker\" KLN_1966.txt KLN_1971.txt SKT.txt | head; echo \"=== HRN 178 area ===\"; grep -n \"šīr\\|sir 'Milch'\\|Milch\" HRN.txt | head -30",
 "description": "Grep Klein for seersucker and Horn for milk"
}
```


### [2026-09-06T21:35:07.206Z] TOOL RESULT

```
=== KLN seersucker ===
KLN_1971.txt:216939:seersucker, n., a kind of cotton fabric. — Hind. 
KLN_1971.txt:236338:second element in seersucker. 
KLN_1966.txt:34437:seerpaw,  n.,  a  complete  suit  presented  by  the sovereign  ( Anglo-Indian ).  • —  Hind,  sar-d-pa,  fr. Pers.  sar-a-pa,  lit.  ‘from  head  to  foot’.  Pers.  sar, ‘head’,  is  rel.  to  OI.  siras-,  ‘head,  summit’;  see cerebrum  and  cp.  the  first  element  in  seerband. Pers.  pa,  ‘foot’,  is  rel.  to  OI.  pat,  acc.  padam, ‘foot’ ;  see  foot  and  cp.  the  first  element  in  pajama, seersucker,  n.,  a  kind  of  cotton  fabric.  —  Hind. sirsakar,  fr.  Pers.  shir-o-shakar,  lit.  ‘milk  and sugar’.  Pers.  shir  is  rel.  to  OI.  ksirdm,  Ossetic dhshir,  ‘milk’.  Pers.  shakar  is  rel.  to  Pali  sak- khara,  OI.  sarkard,  ‘gravel,  grit,  sugar’.  See  sugar, seesaw,  n.,  antiphonic  reduplication  of  saw,  ‘cut¬ ting  tool’.
KLN_1966.txt:37391:Sufism,  n.,  mystical  doctrines  of  the  Sufis.  — Formed  fr.  Sufi  with  suff.  -ism. sug-,  assimilated  form  of  sub-  before  g. sugar,  n.  —  ME.  suger,  sugre,  fr.  OF.  (=  F.) sucre,  fr.  ML.  succarum,  fr.  Arab,  sukkar,  fr. Pers.  shakar,  fr.  Pali  sakkard,  fr.  OI.  sarkara, sarkarah,  ‘gravel,  grit,  sugar’,  which  is  cogn. with  Gk.  xp 6>o],  xpoxiXv),  ‘pebble’,  and  with the  first  element  in  xpoxo-Slkog,  ‘crocodile’. Cp.  It.  zucchero,  Sp.  aziicar,  Port,  afucar,  Rum. zdhar,  OHG.  zucura  (whence  MHG.  zuker,  G. Zucker),  ‘sugar’,  which  all  are  borrowed  fr. Arab,  sukkar.  (The  inital  a  in  Sp.  aziicar.  Port. acucar  represents  the  Arab,  article  al).  Cp.  sac- char-,  saccharin,  sucrate,  sucrose.  Cp.  also  jag¬ gery,  the  first  element  in  crocodile,  and  the second  element  in  seersucker.
=== HRN 178 area ===
5001:*ein Tropfen Milch* (Metrik, S. 153) ist schwerlich richtig (s. Ausgabe).
5203:Milch' (AM. 216 Zeile 5) ').
7000:802. Str 'Milch', stre^ sinn (Käs. 7j,sTrem); vergl. hern]sTre.
7001:aw. apaY/slra- (?); ai. ksvrd- 'Milch'; phlv. sJr-),
7003:kurd. bei. (368) LW. (?) sTr 'Milch'; oss. d. a/ßir,
8298:959. mäst saure Milch*, mäsiden gerinnen*.
8300:arm. macum saure Milch', macanhn 'ankleben (intr.),
9419:«) Reimt auf sir 'Milch* (Öflhn. I, 240 Vers 1982).
10904:aw. pa^man^ *Milch', paemaim- 'säugend*, paf^mavaüt-,
10905:aw. payah' *Milch* (ai. päyas-; af;'. pai; wa;^^. pdi,
10906:si>'n. päi, sar. pöi geronnene Milch, Lab, Quark') ist
10909:minö, *menö haben ^), also *pP.nö) *saure Milch, frischer
```


## [2026-09-06T21:35:32.592Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd1 leaf 512 (p.503) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==512' incoming/WLD/WLD_Bd1_pages.txt | head -60",
 "description": "Print Walde-Pokorny Bd1 p.503"
}
```


### [2026-09-06T21:35:34.270Z] TOOL RESULT

```
=== WLD Bd1 leaf 512 (p.503) ===
               -




                                                             kser-       — ksuelp-                                                 503

von wilden Kindern; Possen reiBen, Zoten angeben" (vgl. dt. Schwank zu
sueng- „biegen, schwingen"), preuB.-lit. suboti , lit. siubiioti ..schaukeln, sich
mit dem Oberkorper wiegen" ( subinS ,,AfterofFnung"?? Leskien Abl. 310),
siubuokle „Schaukel". Lett, schaublt ,,wackeln machen" (setzt ein *siub- vor-
aus,Leskien aaO.), doch konnen die bait. Formen auch idg. seu-bQi)- sein,
s.  sen
     u.    biegen", wo auch iiber lit. siipti.
                    ,,


  Mit aksl. zybati „schaukeln“ ist preuB.-lit. suboti trotz Bruckner KZ. 46,
234 nicbt zusammenzubringen.

kser- „trocken“;                               vom Himmel und Wetter auch                    „trocken = hell. klar\
     Gr. gegov (*nur Akk.) ,,festes, trockenes Land', dehnstufig gijoog ,,trocken,
diirr     ’   (zur       wohl triigerischen Gleiehsetzung mit ai. ksard- ,,brennend“ siehe
u. *kse-   ,,brennen“); lat. serescunt (Lucil. I 306) „(die Kleider) trocknen
                                1
(in  der Sonne)     (verschieden von lac frigore seresrit „wird molkig", das
                                    '



von serum „Molken" abstamint). serenus ,.heiter, hell, klar, trocken (vom                                                11



Himmel und Wetter; gegen die Deutung „*hell wie Molkenwasser spraclie                                            1
                                                                                                                     '




das obige serescunt, da dessen Bed. kaum erst nach serenus umgewandelt
sein kann, selbst wenn dies von einer solchen Gdbed. aus zur Anwendung
auf lichten Himmel gelangt ware) Prellwitz BB. 21, 02 (s anch Vf. I^EWb. 2
s. v. gegen    die Yerbindung mit ai. ksarati „zerflieBt. HieBt", gr. cf Helgco
durch Brugmann BSGW. 1897. 20, Grdr. I'2 428); sehr unsicher mir. surd
„glanzend, hell(?/‘ Fick II 4 306); walirscheinlich ahd. serawen ..trocken
werden, tabescere, languere, marcere ', mhd. nhd. serial .,verdorren. welk  1




               11
werden (Pedersen KZ. 36, 329, KG. I 78, Persson Beitr. 577; nicht nach
Schroeder IF. 17, 465 zu einem idg. *ser- ,.einschrumpt'en = biegen, sich
biegen", s. u. *ser- „Sichel“).
   Ir. serb, cymr. chweric, corn, wherow, bret. chouero „bitter“ (von Pedersen

aaO. initunserer Sippe und gleichzeitig mitai. ksard- „brennend. atzend“ usw.
— s kse- ,.brennen“ — verbunden bleibt fern (Anlaut muB wohl sn sein, siehe
auch          u. suros                  ,,   sauer").    Desgleichen arm. cor „trocken“                   (s   Hiibschmann
```


## [2026-09-06T21:35:35.421Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT apa-xsira ===\"; grep -n \"apa\\.x\\|apaxš\\|apa-xš\\|ap5.x\\|apa\\.xś\" BRT.txt | head -20; echo \"=== BRT xsvipta headword ===\"; grep -n \"xšvipta\\|xhipta\\|x3vipta\\|xsvipta\\|ilvifla\\|xšvip\" BRT.txt | head -20; echo \"=== POK ksiro ===\"; grep -n \"ksīro\\|ksiro\\|kṣīra\\|ksirom\" POK_full.txt | head -10",
 "description": "Grep Bartholomae and Pokorny"
}
```


### [2026-09-06T21:35:35.499Z] TOOL RESULT

```
=== BRT apa-xsira ===
9559:-~    n    Nur  in  dieser  Form;    sie  ist  auch  im  'säfrim  apa.xsai:rfmi%A.)nisähayat^'g.^^.
=== BRT xsvipta headword ===
10988:PDa.  xewd,  PDS.  jvicrf'Milch'').  —  Pü.:  iirö- mand.  —  ')  Im  Gegensatz  zu  patmavant:  — ■)  VII.  ist  "ilvifla-  eig.  das  'herausge  sehn  eilte', d.i.  'gemolkene',  PPfP.[  vgl.  xivofpä-  und  ai.
14800:•  '].  paema'vant-  Adj.,  nur  fem.  'vaili- 'die  mit  Muttermilch  versehen  ist"h  °vaHi xsviptavaiH  (VSf.)  V.  21.  7.
=== POK ksiro ===
```


## [2026-09-06T21:35:45.117Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD p503 grep Milch ===\"; awk 'BEGIN{RS=\"\\f\"} NR==512' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i \"milch\\|ksir\\|ksuiro\\|ksei\" ; echo \"=== WLD Bd1 502-504 heads ===\"; for n in 510 511 512 513 514; do echo \"--leaf $n--\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' incoming/WLD/WLD_Bd1_pages.txt | head -8 | tr -s ' '; done",
 "description": "Check WLD Bd1 around p.503"
}
```


### [2026-09-06T21:35:46.969Z] TOOL RESULT

```
=== WLD p503 grep Milch ===
77:  Ai. ksJra- n. „ Milch"; alb. hire .,Molken‘‘. Pedersen IF. 5. 45, KZ. 36, 277.
=== WLD Bd1 502-504 heads ===
--leaf 510--
 qsei- — qseu-, qsneu-, qneu-, sneu- 501


qsei- „licht“.
 Av. xsae-ta-, f. xsov&ni- „licht, strahlend, herrlich", a-xsae-na- „dunkel-
farbig" (eig. „nicht licht“, Bartholomae IP. 5, 360 Anm. 1 ); xsaeta- aisl. =
seidr „merlangus carbonarius, Kohlfisch"? Fick III 4 422, Falk-Torp unter
sei zw.
--leaf 511--
 , ;




502 qseu-, qsneu-, qneu-, sneu- — qseubh-

Lautnachalimung verhaltenem Niesen gehort; man erinnert andrer-
--leaf 512--
 -




 kser- — ksuelp- 503

von wilden Kindern; Possen reiBen, Zoten angeben" (vgl. dt. Schwank zu
--leaf 513--
504 kpei qpep)-, qpe i)-


 DaB mit Anlaut k[s]u- auch ags. hwilpe „ein schreiender Meervogel",
ndl. wulp ,.Regenpfeifer“, nd. {reycn- wilp, ivalp, wolp ds verwandt seien )



--leaf 514--
 i : ;




 qpen- — q”hpei- 505

Kretschmer aaO.; Yermittlung mit der Sippe von na/ia, gxdoaodai siehe
```


## [2026-09-06T21:35:47.211Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT xsira variants ===\"; grep -n \"x[sš]ira\\|xSira\\|xsīra\\|xšlra\\|kšīra\\|ksird\\|xsi'td\" BRT.txt | head -20; echo \"=== SOD milk ===\"; grep -n \"milk\" SOD_pages.txt | head -30",
 "description": "Grep BRT and Gharib Sogdian"
}
```


### [2026-09-06T21:35:47.272Z] TOOL RESULT

```
=== BRT xsira variants ===
7542:•  j.,  g.  ä-zutay-  f.''  'Fett,  Schmalz':  raoy- nyqtn  i'aranhim  "suitlmca  urvaranqm  Yt. /2.3.  a)  überhaupt  sva.  'feste  Ndirung' gegenüber  der  flüssigen,  im  Gegensatz  zu ' xsi'td-  'Milch' :  pars  xsvisät  (sd.)  -zaitUca  "  1 girii mal  V.  13. z8;  — xhioaica  'sBlayaEca  ■> ^.68.2;  —  t!m  'iSdiis'''  ahurB  mq%r)m tasal  .  .  mazdä  gavei  xhildimcil  *ki'B.- umiaHbys  spmt3  säsnayä  "das  Wort  vom Fett  hat  AhM. ..  für  das  Rind  geschaffen und  die  Milch  für  die  Nahrung  begehren- den durch  sein  Gebot,  der  heilige"  Y. 29.71'.  a)  Du.  in  Verbindung  mit  xhild- Du.:  xsviöa  'zütH  yazamaide  .  .  ilzSis  .  . hamsistri  \.i6.8.  2)  'Üppigkeit,  strotzende Kraft  und  Fülle':  vaKuAlm  'zBülm*^  . . frasasttm  .  .   *p3r»ndlm  yazamaidl  Y.jS.
=== SOD milk ===
5850:                                                                   milk
5856:         371; -w, Karab. Insc. 19.7; -h, VV-Li 71                  milky, milk
9805:                                                                          milk      OxsyPt-) ©Av. xsvipta ^ysyPt, xsypt
15318:                   cow's milk                                                     Tales. 486.3
15717:       yYsyfitk, "mud-milky" Vim. 25                      4206 yrb-    C => yrp-
34585:                                                                      milk
37943:conflagration       1826                     (to)convert 7286                       cow's milk       4074
38841:  6450, 7120, 7671                        meaning    6080, 6082, 8066             milk    746, 747, 2084, 10668
38843:                                                                                  milky     747
```


## [2026-09-06T21:35:55.487Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD 503 ctx ===\"; awk 'BEGIN{RS=\"\\f\"} NR==512' incoming/WLD/WLD_Bd1_pages.txt | sed -n '60,95p'",
 "description": "Context around WP I 503 kṣīra"
}
```


## [2026-09-06T21:35:56.347Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SOD line 9805 ctx ===\"; sed -n '9795,9815p' SOD_pages.txt; echo \"=== SOD 5845-5860 ===\"; sed -n '5845,5860p' SOD_pages.txt",
 "description": "Context in Gharib Sogdian dictionary"
}
```


### [2026-09-06T21:35:57.348Z] TOOL RESULT

```
=== WLD 503 ctx ===
auch          u. suros                  ,,   sauer").    Desgleichen arm. cor „trocken“                   (s   Hiibschmann
Arm. Gr. 1 485; arm.                                r-   nicht     aus ks-).      Formed und         z.    T. in der Bed.
unwahrscheinlich ist Petersson’s Stud, zu Fortunatovs Regel 58 Zuriick-
fiihrung von cech. chfada , chfadu, alt. chrieda oder chi' e da ,,Abzehrung,
Schwund", vhfadnouti „welken, dahinwelken darben; einschrumpfen“, skr.-              ;

                                                                                                                              11
ksl. chreds chrudi „crispus“ (Gdbed. wohl „verhutzelt. verkrunkelt ) auf
                         ,


ein *ksr-endo -, -ondo-.
  DaB kser- eine Erw. von kse- oder eher ksd- „brennen, versengen" sei
(Fick 1 4 31, Prellwitz, Persson aaO.), ist denkbar, vgl. zur Bed. aT&u) „brenne“
:    aidgiog,            ai.    idhriya-            ,,zur   Himmelshelle gehorig" und                 lat.     areo      :    ardco.

kslro- „Hilch, Molken”.
  Ai. ksJra- n. „ Milch"; alb. hire .,Molken‘‘. Pedersen IF. 5. 45, KZ. 36, 277.
Nicht zu rechtfertigen ist Charpentier’s, IF. 28, 17Sff., weitere Ankniipfung
an ai. ksveda- ..Gift" usw. unter einer Wz. *kseu-, *ksu-ei- „FeuchtIgkeit".

ksuelp- „pfeifen“?
      Gr. oakjir/g „Trompete“ zu                                 lit.   svil/uu, svdjiti .,mit    den Lippen pfeifen",
lett. svilpju,                 svilpt, svilpuot ds., svilpis ..Dompfaflf" ?                      Curtius 287: unsicher
weil die bait. Worte vielleicht jiingere Schallworte.
```


### [2026-09-06T21:35:57.397Z] TOOL RESULT

```
=== SOD line 9805 ctx ===
                                                                         royal
     C2, 48V27                                                           GMS 1103
2072 >xh S                                                 <jT<jl
                                                                    2083 'xs'y-     M                    Q^J'^bJ^J <o^oJa.U
     xa ©pron. art. f. sg. & m. f. pi. =»ZKh, x\ yh, YJ
     that, the, she                                                       (o)xsay    (xs*y-) ^'ys'y-
     Anc. Lett. 2.13; KG 604; MSP bll3, 120, pi. bl02                     Go)rule
                                                                          GMS 1086; C2 n p51; Sund. Man. Lett. 310.16
2073 >XRny -> >XRZY(n)                                              2084 'xs'ypt-, S                                  ^
2074 'xrwzn M                                      ^j^JCul^               oxsipd
                                                                          milk      OxsyPt-) ©Av. xsvipta ^ysyPt, xsypt
     a(n)xar-wazan =»Jnyrwzn
     zodiacal circle
                                                                          KG 504, -y, 505; MSP a5
     GMS      341; BBB f37; Hen. JRAS 1942, 236 n 1;
                                                                    2085 'xs'ywn     S                                        \^ Loy^
          Gersh. Sogd. Cpds. 1945, 146.7, a(n)xar "star"                  axsewan ^ysy'wn
          +wazan, "movement*                                              lament
2075 *xrysq C                                     •jl^<8jujj              MSP bl69
     axarisk ? ©pres. pt. =>xr-\ }xyrsq
                                                                    2086 'xsn'qc => 'fsn'qc
=== SOD 5845-5860 ===

                                                                  Frag. Len. 27.6
    MDii 128n9, B-16, 9
                                                                                                                      'Yt'w
 29
                                                                   milk
 735 >Ysnyrkc,) B                                       uUj
       (o)xsnirk ? Oysnyrkh) =^xsnyrk(>1                           VJ 6a, 1029; BBB plOl; Tales. 486.22; GMS 243
       mark, target                                            747 >ysyptk B, S                               ^
       GMS 976 nl; TSP 7.198, 22.7; BSTBL, Dhy.                    (o)xsi(3de OysyPty) ©Yaghn. xsift-, Khwar.
         85(N), 154, 224, 333; -\ Dhy. 226; pi. -tt Dhy.             xwflcy =>xsyPt
         371; -w, Karab. Insc. 19.7; -h, VV-Li 71                  milky, milk
 736 'ysnyrkh S => >Ysnyrk(,)                                     BSTBL, Vim. 25; VJ 6", 1029; BBB plOl cl8
 737 >Ysp- B,S                                    ^           748 >ysypty =» 'ysyptk
                                                              749 »Ysy8 S
     (o)xsap <§)<*xsapa ©f.n. -h, ob. -yh ^'xsp-,                                                            -I ioJjU^S iali-
```


## [2026-09-06T21:36:18.716Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i in (5845,9805): print('line',i,'leaf',leaf)\n    leaf+=l.count('\\f')\ntxt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n'); leaf=0\nfor i,l in enumerate(lines,1):\n    if i in (7000,7001,7003): print('HRN line',i,'leaf',leaf,'printed',leaf-21)\n    leaf+=l.count('\\f')\nEOF\necho \"=== SYN leaf 431 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==431' SYN.txt | head -5\necho \"=== SOD leaf check page 82 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==148' SOD_pages.txt | head -3",
 "description": "Compute leaves/pages for SOD, HRN, SYN"
}
```


## [2026-09-06T21:36:20.558Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB ===\"; grep -n \"kṣīra\\|ksira\\|šīr\\|sir 'Milch'\\|axsir\" HUB.txt | head -20; echo \"=== HJB seersucker ===\"; grep -n -i \"seersucker\\|sirsakar\" HJB.txt AID.txt LKT.txt | head",
 "description": "Grep Hübschmann and Hobson-Jobson"
}
```


### [2026-09-06T21:36:20.752Z] TOOL RESULT

```
line 5845 leaf 93
line 9805 leaf 147
HRN line 7000 leaf 199 printed 178
HRN line 7001 leaf 199 printed 178
HRN line 7003 leaf 199 printed 178
=== SYN leaf 431 head ===
ocat, Boh., Pol. ocet (> Lith. actas). REW 98. Falk-Torp 180. Feist 32. Briickner 373.
3. Fr. vinaigre (> Br. gwinegr, with influence of gwin ‘wine’; ME vinaigre, NE vinegar > NIr. finéagra, W. finegr, also W. gwinegr with influence of gwin ‘wine’), Sp. vinagre, cpd. of Lat. vinum ‘wine’ and dcer ‘sharp’. REW 9356.
4, Lith. rigpyvé (Kurschat’s word for ‘vinegar’, as in Pruss. Lith.), cpd. of rug- (as in riégti ‘sour, ferment’) and pyvas ‘beer’.
SCr. sirée fr. Turk. sirke ‘vinegar’.
5. Skt. gukta- (not strictly ‘vinegar’, but used of any sour, acid liquid), fr. ¢uc- ‘gleam, burn’ and ‘burn with pain’. Uhlenbeck 313.
=== SOD leaf check page 82 ===
 'wztlc
```


### [2026-09-06T21:36:20.809Z] TOOL RESULT

```
=== HUB ===
7323:taxsir BB. 4, 35, alter Artaxsatr (historische Schreibung')
8364:Fiir phi. Artasir , alter Artaxsir BB. 4, 35 u. s. w.
=== HJB seersucker ===
```


## [2026-09-06T21:36:35.133Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 429 430 431 432; do echo \"--- SYN leaf $n first/last ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | grep -oE '\\b(3[0-9][0-9]|4[0-2][0-9])\\b' | head -5; done; echo \"=== find 5.86 MILK line ===\"; grep -n \"5\\.86\" SYN.txt | head; echo \"=== SOD leaves 145-149 page markers ===\"; for n in 145 146 147 148; do echo \"--leaf $n--\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SOD_pages.txt | grep -oE '^\\s*[0-9]{2,3}\\s*$' | head -3; done",
 "description": "Find printed page numbers in SYN and SOD"
}
```


### [2026-09-06T21:36:37.097Z] TOOL RESULT

```
--- SYN leaf 429 first/last ---
328
382
--- SYN leaf 430 first/last ---
383
--- SYN leaf 431 first/last ---
373
313
384
400
417
--- SYN leaf 432 first/last ---
385
=== find 5.86 MILK line ===
1470:ChSl. studenict ‘well’, so SCr. stu- denac, Boh. studné, Pol. studnia : ChSl. student ‘cold’ (15.86). Miklosich 327. Briickner 523. ;
1886:SCr. hladovina ‘coolness’ (fr. hladan ‘cool’, 15.86), also ‘shade’.
2035:2. Lat. glaciés (VLat. glacia > It. ghi- accia, now ghiaccio, Fr. glace, Rum. ghiatd) : gelu ‘icy cold’ (> Sp. hielo ‘ice’), adj. gelidus, Goth. kalds ‘cold’, ete. (15.86). Walde-P. 1.622, 612. Er- nout-M. 412, 423. REW 3718, 3771.
4998:Ir. sed, seg, W. hydd : Ir. segas ‘forest’? Loth, RC 35.86 f.
8314:CHAPTER 5 FOOD AND DRINK; COOKING AND UTENSILS 5.11 Eat 5.57 Minn 5.12 Foop 5.61 Mezar 5.13 Drink (vb.) 5.612 Burcurr 5.14 Hunexr (sb.) 5.62 Brrr 5.15 Turrsrt (sb.) 5.63 Sausace 5.16 Suck (vb.) 5.64 Sour, Brots 5.17 Mrx 5.65 VEGETABLES ' 5.21 Cook (vb.) 5.66 Bran ? 5.22 Bor 5.67 Pra 5.23 Roast, Fry 5.68 Onion 5.24 Baxe 5.69 CaBBAGE 5.25 Oven 5.70 Porato 5.26 Por 5.71 Fruir 5.27 Kerrin 5.72 APPLE 5.28 Pan 5.73 PEAR 5.31 Disx 5.74 Pracu 5.32 Prats 5.75 Wie : 5.33 Bown 5.76 Grape 5.34 Pircuer, Jue 5.77 Nur 5.35 Cup 5.78 OLIvE 5.36 Saucer 5.79 Om 5.37 Spoon 5.80 Berry 5.38 Kyire 5.81 Saur 5.39 Fork 5.82 Prpprr 5.41 A Mua, 5.83 VINEGAR 5.42 BReakFast Bi Rdeer ona 5.43 Luncx 585 § 544 Dinner een Base Sucnbn. 5.86 Mixx (sb.) 5.51 Breap 5.87 Minx (vb.) 5.52 Caxn 5.88 CHEESE 5.58 Dover 5.89 Burrer 5.54 Kwrap 5.91 Merap 5.55 Mzau, Frour 5.92 Wine 5.56 Grinp 5.93 Brrr
9677:; cre. hese ofr. $4 ic, NE sugar), Fr. su- | s.v. sugar. snr, sures 5.86 MILK (sb.) Goth. miluks Lith. pienas yada ON mjolk Lett. piens edo Dan. melk ChSl. mléko lac Sw.  mjolk SCr.  mlijeko latte OE meole, mile Boh. mléko lait ME  melk Pol. —-mleko ee NE milk Russ. moloko aple Du. melk Skt.  payas-, ksira- milicht, 288, Bx OHG miluh Ay. payah-, xbvid- Drath, Buth MHG milich, milch : NHG_ milch
9713:5. Skt. dadhi-ja-, kstra-ja-, lit. ‘milk- born’, cpds. of dadhi- or kstra- ‘milk’ (5.86) are used for ‘curds’, whether formed ‘cheese’ is not clear.
25879:15.85 Hot, WARM 15.86 Cop
27280:15.86 Grk. oxpds Goth. kalds NG Kptos ON kaldr Lat.  frigidus, gelidus Dan. _ kold It. freddo Sw. kall Fr. froid OE ceald Sp. Jrio ME cold Rum. rece, friguros NE cold Ir. tar Du. koud Nir. = fuar OHG alt W. oer MHG kalt Br. yen NHG kalt
=== SOD leaves 145-149 page markers ===
--leaf 145--
 79
--leaf 146--
                                                                                                                                    80
--leaf 147--
--leaf 148--
```


## [2026-09-06T21:36:49.781Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v2 leaf 186 (p.729?) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==186' BQT_v2_pages.txt | head -50",
 "description": "Print Borhan vol2 leaf 186"
}
```


## [2026-09-06T21:36:50.511Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v3 around pdf 113 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==113' incoming/BQT/BQT_v3_pages.txt | head -40",
 "description": "Print Borhan vol3 pdf page 113"
}
```


### [2026-09-06T21:36:51.405Z] TOOL RESULT

```
=== BQT v2 leaf 186 (p.729?) ===
  ‫خر حه‬                                                                                              ‫‪۳-۷ ۲۷‬‬



  ‫باعد و آرن بکیزی‬        ‫ان‬
                           ‫لشیر‬
                              ‫کز»‬
                                ‫معنی سا‬               ‫باشد وانکررایکوبند وبر گوشت‌پاشند وبگرك‬
‫غلیواج میشود و پیوسته خود را سرنکون از‬                    ‫دهند تا بخورد بعد از ساعتی بمیرد وبدان سبب‬
 ‫درخت آویزد (‪ )4‬؛ و با بای فارسی هم‬                                      ‫خانق الذئب وقاتل‌الذئب خوانندش ‪.‬‬
                                   ‫کفته اند ‪٩‬‏‬
                                                      ‫خر بله = بفتح‌اول وبئاركوثزن‌سر کله‪,‬‬
 ‫خر تك س بانای‌قرشت بروزن مردك‬
                                                           ‫‪۰‬‬
                                                          ‫‪۱‬‬              ‫دولاب وچرخاب راگوبند ‪.‬‬
‫‪.‬مهرد الوانی را گوبند که بجهت دفع چشم زخم‬             ‫ارزنده ‪ .‬کی را‬            ‫حر بنده ‪ .‬س وزن‬
‫بر بازو کوردن اطفال بندند وآویزند ؛ و یامن‬            ‫‪۱‬ن‪-‬وعی از‬
                                                              ‫کویند که خرالاغ بکرابه دهد و‬
     ‫معنی بجای تای قرشت میم هم‌آهده‪ .‬است ‪-‬‬
                                                      ‫صنیل در لفت خربازان‬
                                                                        ‫تآ‬‫و‬                  ‫بازی ههمست‬
‫خر تنگ = بورزن خرچنگه ‪ ۰‬فام‬                                                                     ‫‪۰.‬‬   ‫مذ کور شل‬

              ‫قربه‌است در دوفرسخی صمر قنف ‪۰‬‬
                                                       ‫حر پور = بفتح اول(‪ )۱‬بروزن‌شبکور‬
‫رزتنوت » توت‬
           ‫ختروت * ‪ ۰‬بفر و‬                            ‫شب‌بره را(‪ )۲‬گویند؟ ؛وبضم‌اول‌هم‌آمده است ؛‬
               ‫برزکه زبون بی‌مزه کروابند ‪.‬‬             ‫وبابای فارسی نیز گفته‌اند ؛ ودرجای‌دیگرخوبوز‬
‫چرال * ‪ ۰‬باجیم فارسی بروزن ابدال ‪.‬‬
                                 ‫خ‬                    ‫آورده که بجای حرف ثانی واو وبجای بای ابجد‬
                                                      ‫بای حطی و بجای رای قرشت زای هوز باشد‬
‫مرغی‌است بزر که ازجنس‌هوبرموآ دراباشاهی‌وبلز‬                   ‫و گفته )‪ ۳‬هرمرغی که درشب برواز کند ‪:‬‬
‫شکار کنند وترکان توقدری گویند » وحضی کویتد‬
                                                          ‫حر بواز ‪ = ۳‬بکرثالث بروزن سروناز‪,‬‬
 ‫وقداق (ه) خوانند بوعضی آنرا سرخاب وعیش‬                   ‫شپرة بزر کے راکوبند » آن ببزر کی غلیواج‬
              ‫درخ گهفمته‌الد و"اه اعلم ‪١٠.‬‏‬                                  ‫میشود وبرسردوش ناخنها دارد‪.‬‬
‫ور وزن درجسته » یمعئی‬     ‫خر جسته =‬

 ‫وشلتاقآ وردماد ‪۹۷‬‬   ‫جنگ وخصومت وخرخشه(‪)+‬‬


‫ربحکضیودیبگند جماعتی باشندمتسید یعنی‬
                                   ‫و‬                      ‫خر بیوار“ ‪-‬با تحتانی مجہول بروزن‬
               ‫(‪ )۲‬چك » چش ‪ :‬شپر؛ برزکه را‪.‬‬                        ‫‪ - :‬بفتح اول‪.‬‬   ‫چش‬    ‫(‪ )۱‬چك‬

                              ‫یزد‪.‬‬ ‫‏(‪)٤‬یاچشو‪:‬‬
                                          ‫ب‬                                ‫(‪ )۳‬چش ‪ :‬کفته‌اند ‪.‬‬
                          ‫(‪ )3‬چش ‪:‬خرخشته ‪.‬‬                                   ‫‏)‪ (e‬خم‪ : ۱‬دقداق ‪.‬‬

   ‫‪ - ۱‬معرب آن‌خربندج (مکاری) «دزیح اص‪ »۷۵۳‬وخربندبه‌وخرمندیه (مکاربان)«وزی‌جاص‬
```


### [2026-09-06T21:36:53.213Z] TOOL RESULT

```
=== BQT v3 around pdf 113 ===
[pdf page 113]
als
‏لیزمعروفت» وآن چیزی باشد سفید ور.ا ن که‎
‏و از آن پنیر‎ aT ‏از یتان ماده حبوانات بر‎
. ٩ ‏و ماست بندلد‎

شیر اه - با اول ‎yi‏ رسیده و ‎SME‏
‏بالف کشیده وفتح بای ایجد , خشخش را کوبند؛
و یی شيره خشخاش را کفته‌اند.

شیراز دو ‎gine‏ دارد : اول‌تام شهری
‎col‏ مشهور و مروف درفاری . گوبندعمرولیث
آفرا سم رکرد ۴ - و دویم ‎wT‏ شبت راریزه
کنند و با ماست بيامیزند و قدری شیر بر آن
ریزند و درمشکی با ظرقی کنند و چند روزی

bh Soh 0 Seed

بگذارد تا ترش گردد ‎sary‏ ازآن با نان‌بخورند؛
و بعضی گویند معنی‌دوم عربی است ۴ ؛ وبه‌عنی
ریچال هم ‎kd‏ آمده است که مربای دوشایی
‎ath‏ .

شیر الیشر ۴ - کنابه ازحترت رسالت
صلوات اند ‎ade‏ و آله است.

‎ot =‏ پولاد ‎Ko GE‏ رن .
‎al‏ از مردمان دلیر و شجاع وبوادر باشد -
وکنایه از اسب پرزور هم است .

‏شیر ا نداز ‎ow‏ با ثانی همروف بر وزن
زیرانداز , پستانیرا کوبند که پر از شیر باشد

‏۱ - اوستا )7( - 25۳1۳2 ‎wae. apa]‏ باستان ‎kshira_‏ ( شیر ) « ‎Shitse‏
‏قی : ارمتی ع ‎hamshirak‏ .کردی و بلوچی ‎shir (se‏ )+( » استی ‎vaxsir axshir‏
مثجی ‎cacy gels xshir‏ ( ورك : دب که ۲۱۵ : شیرین ) » دزفولی۲ 501 «امام». گیلکی
قربزندی . برلی ولظازی 501۲ « ۵ . اص ‎apt , ٩۲۹۶‏ ادی ‎SHIT‏ « ۵. ۲ ص۱8۰
۴ - ام « شیراز » ‎(pik)‏ در الواح عیلامی مکشوف در تخت جمشید بصورتهای
‎Ti-ra_is_si-ish, Shir_si _is, 11 ۲2 5 ish, Shi_ra_is _ si_ish‏
آمده . رك: ‎G. G. Cameron , Persepolis Treasury Tablets (vocabulary)‏
```


## [2026-09-06T21:37:06.699Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"khurt\\|khvart\\|xvart\\|kvart\\|khurd\\|xshudra\\|kshudra\" BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt BQT_v1_pages.txt 2>/dev/null | head -20; echo \"=== search خرد leaf ===\"; python3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if 'خرد' in p and ('اوستا' in p or 'باستان' in p):\n        print('leaf',i, 'printed~', i+543)\nEOF",
 "description": "Find خرد entry with etymology footnote in Borhan"
}
```


### [2026-09-06T21:37:08.368Z] TOOL RESULT

```
=== search خرد leaf ===
leaf 20 printed~ 563
leaf 30 printed~ 573
leaf 33 printed~ 576
leaf 37 printed~ 580
leaf 70 printed~ 613
leaf 122 printed~ 665
leaf 176 printed~ 719
leaf 187 printed~ 730
leaf 188 printed~ 731
leaf 189 printed~ 732
leaf 190 printed~ 733
leaf 196 printed~ 739
leaf 199 printed~ 742
leaf 208 printed~ 751
leaf 214 printed~ 757
leaf 238 printed~ 781
leaf 246 printed~ 789
leaf 247 printed~ 790
leaf 296 printed~ 839
leaf 301 printed~ 844
leaf 316 printed~ 859
leaf 368 printed~ 911
leaf 389 printed~ 932
leaf 417 printed~ 960
leaf 433 printed~ 976
leaf 449 printed~ 992
leaf 458 printed~ 1001
leaf 469 printed~ 1012
leaf 474 printed~ 1017
leaf 479 printed~ 1022
leaf 480 printed~ 1023
leaf 493 printed~ 1036
leaf 531 printed~ 1074
leaf 535 printed~ 1078
leaf 554 printed~ 1097
leaf 561 printed~ 1104
leaf 584 printed~ 1127
leaf 586 printed~ 1129
leaf 595 printed~ 1138
leaf 596 printed~ 1139
leaf 648 printed~ 1191
leaf 654 printed~ 1197
leaf 658 printed~ 1201
leaf 675 printed~ 1218
```


## [2026-09-06T21:37:13.640Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 186 187; do echo \"===== leaf $n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tail -25; done",
 "description": "Print footnotes of Borhan v2 leaves 186-187"
}
```


### [2026-09-06T21:37:15.889Z] TOOL RESULT

```
===== leaf 186 =====
‫ربحکضیودیبگند جماعتی باشندمتسید یعنی‬
                                   ‫و‬                      ‫خر بیوار“ ‪-‬با تحتانی مجہول بروزن‬
               ‫(‪ )۲‬چك » چش ‪ :‬شپر؛ برزکه را‪.‬‬                        ‫‪ - :‬بفتح اول‪.‬‬   ‫چش‬    ‫(‪ )۱‬چك‬

                              ‫یزد‪.‬‬ ‫‏(‪)٤‬یاچشو‪:‬‬
                                          ‫ب‬                                ‫(‪ )۳‬چش ‪ :‬کفته‌اند ‪.‬‬
                          ‫(‪ )3‬چش ‪:‬خرخشته ‪.‬‬                                   ‫‏)‪ (e‬خم‪ : ۱‬دقداق ‪.‬‬

   ‫‪ - ۱‬معرب آن‌خربندج (مکاری) «دزیح اص‪ »۷۵۳‬وخربندبه‌وخرمندیه (مکاربان)«وزی‌جاص‬
   ‫‪ ۴‬مت مخفف ”خر بيواز“(هم‪).‬‬           ‫ورك‪ :‬خربواز‪۲ ‎‬‬          ‫«خربواز»(«‪.‬م‪).‬‬      ‫‪ _ ۳‬ضوف‬                ‫‪Y1‬‬

         ‫خر(بز رگه) ‪ ۳‬بیواز(ه‪.‬م‪ .).‬رکه‪ :‬خربواز‪‎‬‬       ‫>‬        ‫©‬           ‫‪- ۴‬مخفف‌خرابه(ه‪.‬م‪.).‬‬
                                         ‫‪:‬‬   ‫خریواز‬   ‫‪:‬‬    ‫شب بازه ‪:‬ورك‬      ‫شب پره»‬    ‫‪-‬رکه‪:‬‬        ‫‪1‬‬


   ‫«خت فرس ‪.*۳۷۱‬‬
               ‫خدازقاینی‪ .‬ل‬            ‫کار توشب‌بود چو بخیرواز‪.‬‬                    ‫نکنی هیج کار روز دراز‬
   ‫خر(بز رکن) ‪+‬‬      ‫‪=۹‬‬        ‫‪ _ ۸‬از‪ :‬خر(بز رگه) ‪٣+‬‏توت ‪3‬‬               ‫‪_ ۲‬مصحف«خرمكث»(«‪.‬م‪).‬‬

                     ‫*‪« -۶‬خرچال» مرغیاست برشکل بطبزرکه‪ .‬زینبی کوبد ‪:‬‬                                 ‫چال («‪.‬م‪).‬‬
        ‫چنان کجا بنواحی عقاب بر»خرچال‪.‬‬                              ‫همیشه درفز ع آزوی سیاه‌های ملوك‬
        ‫رش‪:‬ته ‪.‬‬
              ‫وخرکه‬         ‫شحتفه‪(:‬ه‪.‬م‪).‬‬
                                       ‫‪- ۱‬خظر‪,‬خمم‬                                   ‫‪۳‬‬    ‫«لفت فری‬

===== leaf 187 =====
‫است و آن جانوری باشد که صیادان بر کار دام‬                                                         ‫از بروج دوازده‬
               ‫ْف تف تا حانوران دیگردردام افتند‪. ۱۱‬‬
                                                                                                 ‫ظك حم‬      ‫کانة‬
‫=روزن شبدین نام شهر ست‬
                     ‫خر خیز م‬

     ‫‪ ۳‬خر(بز رکه) ‪ +‬جل («‪.‬م ‪ - ۴ .‬ركخرچکوکك‪ ۵ .‬یپلوی‬                                       ‫‪.‬‬   ‫رك‪ :‬خرجلوك‬   ‫‪- ۷‬‬

     ‫» طبق‌وجه اشتقاق عامیانه از ‪ :‬خر (الاغ) ‪ +‬چنك (فولری‪ :‬خر؟) «حوبتمان ‪۰۷4۰‬‬                            ‫‪8‬‬
     ‫‪ .‬دزفولی‬      ‫‪۳۲‬‬
                    ‫‪۰‬ص‬‫«اسقا!‪ :‬ص ‪۸٩‬‏ ‪ ۰۷۲ ۰‬در لهج که ‪« 8021618‬مجلةٌ بشوتن ‪٩‬‏ ‪٩ :‬‬
    ‫‏‪ -1 .qerezleng‬بككبرخ‌تومامو آن‌د کررخ زهره ` زهرهءبعقرب نشته(نهفته‪ .‬دهضدا) ماهبخرچنك‪.‬‬
     ‫»‪.‬‬        ‫فری‬    ‫ابوطلهر‪« .‬لفت‬


    ‫(‪۰‬م‪. ).‬‬      ‫«چرخشت»‬          ‫^ _ مسحضف‬      ‫رك ‪ :‬خرخشه‪.‬‬         ‫‪۵‬‬     ‫‪ - ۷‬باین معنی اسم صوت ‪.‬‬

     ‫‪ -6‬در نرکی خرخشه بفتح دو خاء = قرغاش بمعتی تراع » مجادله واشوب«جضتایی‬
                                            ‫ه‪.‬‬ ‫خ‪:‬‬‫رکه‬
                                                   ‫خ ر‬ ‫‏‪٩‬‬        ‫و ‪ . ۰۰۸۰‬رك ‪ :‬خرشه ‪.‬‬                       ‫‪۲‬‬
                        ‫خ٭رجیدی ‪ -‬بم اول وقح پنجم کرستن «فهرست شاحنامةً ولف» ‪:‬‬
     ‫‪۹۲۷‬‬       ‫حرةٌ‬
                  ‫صهف د‬
                      ‫ی‬
```


## [2026-09-06T21:37:24.995Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in range(185,196):\n    p=pages[i]\n    lat=re.findall(r'[A-Za-z][A-Za-z_\\-\\.]{2,}',p)\n    print('--- leaf',i,'printed~',i+543,'---')\n    print(' latin:', lat[:40])\nEOF",
 "description": "Scan Borhan v2 leaves for Latin-script etymology footnotes"
}
```


### [2026-09-06T21:37:26.769Z] TOOL RESULT

```
--- leaf 185 printed~ 728 ---
 latin: []
--- leaf 186 printed~ 729 ---
 latin: ['qerezleng']
--- leaf 187 printed~ 730 ---
 latin: []
--- leaf 188 printed~ 731 ---
 latin: ['edratuoM', 'edratuoM', 'Thlaspi', 'Hara']
--- leaf 189 printed~ 732 ---
 latin: []
--- leaf 190 printed~ 733 ---
 latin: []
--- leaf 191 printed~ 734 ---
 latin: ['dnas', 'adnaS', 'dnas']
--- leaf 192 printed~ 735 ---
 latin: []
--- leaf 193 printed~ 736 ---
 latin: ['psa', 'Loraanthus']
--- leaf 194 printed~ 737 ---
 latin: []
--- leaf 195 printed~ 738 ---
 latin: []
```


## [2026-09-06T21:37:40.949Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in range(186,193):\n    p=pages[i]\n    print('=== leaf',i,'printed~',i+543,'===')\n    for ln in p.split('\\n'):\n        s=ln.strip()\n        if 'خرد' in s or 'خُرد' in s:\n            print('   ',s[:160])\nEOF",
 "description": "Find خرد lines in Borhan v2"
}
```


### [2026-09-06T21:37:42.852Z] TOOL RESULT

```
=== leaf 186 printed~ 729 ===
=== leaf 187 printed~ 730 ===
    ‫خرداد‬                                                                                        ‫‪-‬‬
    ‫خرداد ‪ °‬د م اول بروزن مرداد ؛‬                        ‫ثانی وسکون‬   ‫شتح اول و" شف ف‬   ‫=‬       ‫حرد‬
    ‫‪ «۴‬خرد » گل بود ‪ ۰‬خسروانی گفت ‪:‬‬                       ‫ببعد * ‪.‬‬
    ‫بخرد ‪.‬‬   ‫بردت‬    ‫باز ناکه فرو‬                    ‫آن کجا سرت بر کشید بچرخ‬
    ‫‪ - ۴‬پپلوی ‪« 4۲۵۷5‬ناوادیا ‪[ ۷۹۱‬رك ‪. :‬خرده] اورامانی ‪. 4 < 4۲۷7۷‬‬        ‫« مینا‪.»4۳۱‬‬
    ‫هم ‪ ۰ 0711‬معرب آن خردة «نفس» هرن خرد فارسی را از اوستایی ‪) 2/۵72۷‬ندانته«اسفا‪۲: ۱‬‬
    ‫خردش چنان بکوفت که خاکش‌غبار کرد‪.‬‬            ‫چند استخوان که هاون دوران روز کار‬
    ‫‏‪ («٥‬گو بد ‪« :‬معنى هذا الاسم (خرداد) ثدات الخلق» وی نام ابزدی از ایزدان دین‌زرشتی‌است‪.‬‬
    ‫نگهبانی سومین ماه سال وششمین روز ماه (شمسی) با اوست ‪ .‬در اوستاو کتب دینی پهلوی خرداد‬
    ‫وامرداد غالبا باهمباد شده‌اند ‪.‬خرداد مظهر کمال اهورمزدا درین جهان و درجهان مینوی‌بخشایش‬
    ‫ابزدی جزای اعمال لیکوکاران است ‪ .‬در عالم مادی‌نگهبانی آب با خردادست‪ .‬بیرونی(آ ارالباقه‬
    ‫كويد ‪« :‬هروذا (خرداد) هوالملك المو کل بتربية الخلق والاشجاروالنبات و ازالقالتجانات‬               ‫‪۰‬‬
=== leaf 188 printed~ 731 ===
    ‫یر ار —‬                                                                                                     ‫خردر‬
    ‫جشن وعید نمایند واين جشن راجثن خرداد کان‬
    ‫درختان ‪ .‬و امور و مصالحی که در ماه خرداد‬
    ‫تره تیزلك باشد ‪ .‬و خردل‌سفید‬
    ‫خردل‬                                        ‫خوانند ‪.‬‬                                             ‫که زغن است ‪.‬‬
    ‫خردما = بضم اول وسکودنانی وفتح‬                                    ‫خر در گله صجماعتی باشندازمتید(ه)‬
    ‫وخوش ر‬          ‫با سین بی‌نقطه بر وزن‬      ‫خرد سود‬
    ‫راجت‬     ‫نمی‬   ‫وهند‬       ‫بمعنی عقل‬    ‫خرد‬   ‫باشد ‪٩‬‏ چه‬
    ‫بر وزن منزل ‪.‬‬       ‫كارلث‬   ‫خردل ‪> -‬‬
    ‫‪ = ۴‬خردل بری = ‪edratuoM 6823۷125‬‏ (فر)«لك؟ص ‪. ۰ ۹۱‬‬                                                 ‫ص‪.* ۷۱‬‬
    ‫رک‪ :‬خرده گاه ‪.‬‬       ‫‪ #‬خر د "اه‬
    ‫‪ .‬دز روز خرداد ازماه خردادجشن‌خر داد گان‬                    ‫عی‌المیاه *‪ .‬متشت چپارم در اوستا بخرداد تعلق دارد‬
    ‫برها متفه ‪ .‬بیرونی در فهرست روزهای ابرانی (در آثارالبافه) روز ششم را «خرداد؟ و در سفدی‬
    ‫‪ ۰‬فخرده آوستا ‪ « ۵۸۲‬فهرس تت هزدسنا » در طبری ماه خرداد را هرماه ‪Hara mãh‬‬         ‫‪۹‬‬
    ‫‪.*۱‬‬    ‫«وس‌ورامن ص‪۲۹۲‬؛‪,‬‬             ‫جهان ازخرمی چون کرم بغداد‪.‬‬                      ‫مه آردیبپشت و روز خرداد‬
=== leaf 189 printed~ 732 ===
    ‫خرده مرده‬                                                                                    ‫‪۷۳۱‬‬
    ‫ج‬                   ‫سهل وریزورباشد ودرموبدالقضلا خرد(‪ )۱‬ومورد‬
    ‫خردهگاه" « با کاف فارسی بالف‬                           ‫ممعذی خردمند است که زبرك و عاقل و صاحب‬
    ‫بحذف های اول هکفمته‌اندکه خردگاه باشد ‪-‬‬
    ‫خرد‬                  ‫ازدقیق وباريك هم هست چه‬              ‫وه‬
    ‫خیم بزر که برپای کنند ‪.‬‬           ‫خرده بین باربك بین را گونند ‪ -‬و بمعنی دندان‬
    ‫خردة کندد = بمربى دقابق الکندر‬                          ‫همآ مده است_ونام نسکی‌است ازجملة بیست‌ويك‬
    ‫ون‬ ‫[اف‬         ‫‪ - ۱‬پپلوی ‪ 0020700211‬از ‪ :‬خرت (خرد ) ‪ +‬او‬
    ‫( خردشدن ‪ ۰‬شکتن ) لیب کت ‪4۳۱٩‬‏ رك ‪:‬خرد ‪.‬‬                            ‫نیء‬
    ‫‪.‬‬    ‫با ند است‬   ‫‪« - ۳‬اخرده» تفیراجزای‬
    ‫کی ابارده خوالم شها کهی خرده»‪.‬‬                         ‫ببیتم آخر روزی بکام دل خود را‬
    ‫‪ = ۴‬رك‪ :‬خرده گاه‪.‬‬               ‫خرده اوستا ‪۱‬‬    ‫رك ‪:‬‬   ‫‪.‬‬   ‫اوستا » است‬   ‫اخرده‬   ‫ازخرده‬   ‫مراد‬
    ‫خر‪-‬ده درمیان نهادن» دفایق گفتن ‪ « :‬پس (عاشق)خردة عشق را در میان نهاد و از‬
    ‫بقمه درصضحة ‪۷۳۳۱‬‬   ‫‪.‬‬   ‫رکك‪ :‬خردومرد‬    ‫‪۷‬‬              ‫‪ - ۱‬رك ‪ :‬خرده ‪.‬‬              ‫‪.‬‬      ‫‪۸‬ش‪۵‬‬
=== leaf 190 printed~ 733 ===
    ‫‪A‬‬                                                                                  ‫خرد* مینا‬
    ‫تقطه دار ‪ ,‬اسباب خرده فر‬
    ‫آونرا بعریی سم الحمار خوانند » و معرب آن‬          ‫خرده فروش‌باشد ‪ -‬ونام شهری و مدینه‌ای هم‬
    ‫‪« ۱‬موضمی خدوشرخخرمتوان درهم» تگفوتی خرد؛ همینا برخاکش ربخته امت‬
    ‫خرازی بخرده فروشی اطلاق شود) ‪:‬‬
    ‫‪ #‬خرده‌اوستا ‪ -‬بضم‌اول وفتح سوم‌وینجمو کسرشتم ‪ ۰‬دریهلوی ‪۷۵/۲۵ 6۵/5۵۳۸‬‬
    ‫ات خرده اوستا ‪ ,‬بزباناوستايی يحت بلکه پخش بز ر گی از‪Ty‬‏‬                ‫ممةٌ‬
    ‫‪:‬جمةٌ خرده اوستا بقام پور داود ‪ .‬اانزتشارات انجمن زرتشتیان ابرانی‬
    ‫‪ .‬در شعر دقیقی نام «خرده؟ بادشده‬       ‫وافسن امران لگ مزودسنا هم تکارنده ص ‪۲‬‬               ‫ی‬
=== leaf 191 printed~ 734 ===
=== leaf 192 printed~ 735 ===
```


## [2026-09-06T21:38:07.173Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN xurd ===\"; grep -n \"xurd\\|hurd 'klein'\\|klein'\" HRN.txt | head -20; echo \"=== BRT xvarəta ===\"; grep -n \"x\\\"ar9ta\\|x\\\"arata\\|xvareta\\|x\\\"ar»ta\\|x'ar»ta\" BRT.txt | head -10",
 "description": "Grep Horn for xurd, Bartholomae for xvarəta"
}
```


### [2026-09-06T21:38:07.233Z] TOOL RESULT

```
=== HRN xurd ===
490:6. abiSy^ur, abisxurdy äb/ifr (geschrieben und früher ge-
4584:np. yurde, ynrd 'klein', phlv. yiirtak^ arm. LW. yortak
7528:865. kern 'wenig, gering, klein', kemJn,
7580:aw. kutaka- 'klein'; phlv. kütak bezw. kötak,
=== BRT xvarəta ===
```


## [2026-09-06T21:38:10.350Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D8%B1' --note 'page 282, root Ksiro, Persian šir milk etymology' 2>&1 | tail -5; python3 tools/fetch_source.py 'https://www.etymonline.com/word/seersucker' --note 'page 282, root Ksiro, English seersucker' 2>&1 | tail -5; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%AF' --note 'page 282, root Ksudros, Persian xord small' 2>&1 | tail -5",
 "description": "Archive web sources"
}
```


### [2026-09-06T21:38:12.431Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ff12e8ca683ab8a4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ba1304f311dda486.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7bfbbf0ba43ddbd.txt
```


## [2026-09-06T21:38:16.774Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4578,4592p' HRN.txt; python3 - <<'EOF'\ntxt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(txt,1):\n    if i==4584: print('HRN line 4584 leaf',leaf,'printed',leaf-21)\n    leaf+=l.count('\\f')\nEOF",
 "description": "Horn xurd entry context"
}
```


## [2026-09-06T21:38:18.180Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== seersucker etymonline ===\"; sed -n '1,60p' c7bfbbf0ba43ddbd.txt 2>/dev/null || head -60 ba1304f311dda486.txt",
 "description": "Read fetched pages"
}
```


### [2026-09-06T21:38:18.961Z] TOOL RESULT

```
ydr-am, sar. yör-am, sangl. y^är-afn.
Die l^y^m*' bedeutet sowohl essen' als auch 'trinken',
vergl. aw. äfs anaiui^.y^ared^a' (vd. 6, 31); ai. sürä-,
aw. hurä'^), lit. .wla (*Birkensaft') werden aber besser
zu i/^sav' 'auspressen' gestellt, woran Fick, Wörter-
buch^ noch zweifelt.
np. yurde, ynrd 'klein', phlv. yiirtak^ arm. LW. yortak
'zerbrochen, zerschlagen* kann nicht hierher gehören,
da es auf u reimt (Vis und RämTn S. 51, Vers 12,
V
Sahn. I, 179 Vers 905) und auch AM. u spricht; auch
mit aw. y^ara- 'W^unde* (de Lagarde) wird es schwer-
lich zusammengestellt werden können. Nöldeke
(mündliche Mitteilung), vergleicht lat. curttts 'kurz',
das zur [/^qert- 'schneiden' gehört. Die Aspiration im
HRN line 4584 leaf 133 printed 112
```


### [2026-09-06T21:38:19.001Z] TOOL RESULT

```
=== seersucker etymonline ===
URL: https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%AF
FETCHED: 2026-09-06T15:58:09Z
STATUS: 200
TITLE: خرد - Wiktionary, the free dictionary

خرد - Wiktionary, the free dictionary 

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

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Ottoman Turkish 

 Toggle Ottoman Turkish subsection
```


## [2026-09-06T21:38:32.671Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== خرد wikt Persian etym ===\"; grep -n -A12 -i \"Persian\" c7bfbbf0ba43ddbd.txt | grep -n -i -B2 -A10 \"etymology\" | head -80",
 "description": "Extract Persian etymology from خرد page"
}
```


### [2026-09-06T21:38:32.723Z] TOOL RESULT

```
=== خرد wikt Persian etym ===
4-80-
5-81- 2.1 
6:82- Etymology 1 
7-83-
8-84- 2.1.1 
9-85- Pronunciation 
10-86-
11-87- 2.1.2 
12-88- Adjective 
13-89-
14-90- 2.1.2.1 
15-91- Usage notes 
16---
--
26-243- petty , insignificant 
27-244-
28:245- Etymology 2
29-246- [ edit ] 
30---
31-248: Borrowed from Classical Persian خِرَد ( xirad , “ wisdom, intellect ” ) , from Middle Persian [script needed] ( hlt /⁠xrat, xrad⁠/ , “ wisdom, understanding, intelligence ” ) , from Proto-Indo-Iranian *krátuš ( “ intelligence, mental power ” ) , from Proto-Indo-European *krét-us .
32-249-
33-250- Noun
34-251- [ edit ] 
35-252-
36-253- خرد • ( hıred ) 
37-254-
38-255- wisdom , intellect , sense , judgment , understanding 
--
46-263- [ edit ] 
47-264-
48:265- Etymology 1
49-266- [ edit ] 
50-267-
51-268: Inherited from Middle Persian [script needed] ( hwlt' /⁠xwurd⁠/ , “ little ” ) , perhaps originally the past participle of [script needed] ( hwltn' /⁠xwardan⁠/ , “ to eat ” ) ; for the semantic development, compare the derivation of Proto-West Germanic *biti ( “ bit ” ) from *bītan ( “ to bite ” ) . [ 1 ] Compare Talysh هرد ( hərd ) , Northern Luri هیرد ( hird ) , Baluchi ہورت ( hurt , “ little, tiny; lamb herd ” ) ; see خوردن ( xwardan  / xordan ) for more on the root.
52-269-
53-270- Pronunciation
54-271- [ edit ] 
55-272-
56-273: ( Classical Persian ) IPA ( key ) : /ˈxurd/ 
57-274-
58-275- ( Dari, formal ) IPA ( key ) : [xʊɹd̪] 
--
159-534- Pages with etymon 
160-535: Persian entries with etymon 
161:536- Pages with etymology trees 
162:537: Persian entries with etymology trees 
163-538-
164-539- This page was last edited on 24 August 2026, at 05:20.
165-540-
166-541- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
167-542-
168-543- Privacy policy 
169-544-
170-545- About Wiktionary 
171-546-
172-547- Disclaimers
```


## [2026-09-06T21:38:35.351Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== شیر ===\"; grep -n -i \"Proto-Iranian\\|Proto-Indo-Iranian\\|kṣīrá\\|substrate\\|Middle Persian\" ff12e8ca683ab8a4.txt | head -30; echo; echo \"=== etymonline seersucker ===\"; grep -n -i -A6 \"seersucker\" ba1304f311dda486.txt | head -40",
 "description": "Extract from شیر and seersucker pages"
}
```


### [2026-09-06T21:38:35.418Z] TOOL RESULT

```
=== شیر ===
369: From Proto-Iranian *xšiHrám , from Proto-Indo-Iranian *kšiHrám . Cognate with Persian شیر ( šir ) .
502: From From Classical Persian شیر ( šīr ) , from Middle Persian [Book Pahlavi needed] ( HLḆA ) .
515: From Classical Persian شیر ( šēr ) , from Middle Persian 𐫢𐫃𐫡 ( šgr /⁠šagr, šēr⁠/ , “ lion; (astronomy) Leo ” ) .
549: From Middle Persian 𐫢𐫃𐫡 ( šgr /⁠šagr, šēr⁠/ , “ lion; (astronomy) Leo ” ) .
664: From Middle Persian [Book Pahlavi needed] ( HLḆA ) , [Book Pahlavi needed] ( šyl ) , 𐫢𐫏𐫏𐫡 ( šyyr /⁠šīr⁠/ , “ milk ” ) , from Proto-Iranian *xšiHrám , from Proto-Indo-Iranian *kšiHrám .
777: Proto-Indo-Iranian *ćŕ̥Has 
781: Inherited from Sanskrit शिर॑स् ( śíras ) , from Proto-Indo-Iranian *ćŕ̥Has , from Proto-Indo-European *ḱŕ̥h₂-os ~ ḱŕ̥h₂-es- , from *ḱerh₂- , possibly from *ḱer- + *-h₂ .
876: Central Kurdish terms inherited from Proto-Iranian 
877: Central Kurdish terms derived from Proto-Iranian 
878: Central Kurdish terms inherited from Proto-Indo-Iranian 
879: Central Kurdish terms derived from Proto-Indo-Iranian 
900: Ottoman Turkish terms derived from Middle Persian 
904: Persian terms inherited from Middle Persian 
905: Persian terms derived from Middle Persian 
916: Persian terms inherited from Proto-Iranian 
917: Persian terms derived from Proto-Iranian 
918: Persian terms inherited from Proto-Indo-Iranian 
919: Persian terms derived from Proto-Indo-Iranian 
925: Southeast Pashayi terms inherited from Proto-Indo-Iranian 
930: Southeast Pashayi terms derived from Proto-Indo-Iranian 
951: Requests for Book Pahlavi script for Middle Persian terms 
960: Middle Persian terms with redundant script codes 

=== etymonline seersucker ===
1:URL: https://www.etymonline.com/word/seersucker
2-FETCHED: 2026-09-06T21:38:12Z
3-STATUS: 200
4:TITLE: Seersucker - Etymology, Origin & Meaning
5-
6:Seersucker - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
--
21: Origin and history of seersucker 
22-
23: seersucker (n.) 
24-
25- thin linen fabric, originally imported from the East, 1722, from Hindi sirsakar , said to be an East Indian corruption of Persian shir o shakkar "striped cloth," literally "milk and sugar," a reference to the alternately smooth and puckered surfaces of the stripes. This would be from Persian shir (cognate with Sanskrit ksiram "milk") + shakar (cognate with Pali sakkhara , Sanskrit sarkara "gravel, grit, sugar;" see sugar (n.)).
26- also from 1722 
27-
28: Entries linking to seersucker 
29-
30- sugar (n.) 
31-
32- late 13c., sugre , "sweet crystalline substance from plant juices," from Old French sucre "sugar" (12c.), from Medieval Latin succarum , from Arabic sukkar , from Persian shakar , from Sanskrit sharkara "ground or candied sugar," originally "grit, gravel" (cognate with Greek kroke "pebble").
33-
34- The Arabic word also was borrowed in Italian ( zucchero ), Spanish ( azucar , with the Arabic article), and German (Old High German zucura , German Zucker ), and its forms are represented in most European languages (such as Serbian cukar , Polish cukier , Russian sakhar ).
--
46: Share seersucker 
47-
48- ‘ cite ’ 
49- Page URL :
50: https://www.etymonline.com/word/seersucker Copy 
51-
52- HTML Link :
53: <a href="https://www.etymonline.com/word/seersucker">Etymology of seersucker by etymonline</a> Copy 
54-
55- APA Style :
56: Harper, D. (n.d.). Etymology of seersucker. Online Etymology Dictionary. Retrieved September 6, 2026, from https://www.etymonline.com/word/seersucker Copy 
57-
```


## [2026-09-06T21:38:52.348Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb; python3 git/rishe/tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/k%C5%A1iHr%C3%A1m' --note 'page 282, root Ksiro, PII *kšiHrám milk' 2>&1|tail -2; python3 git/rishe/tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%87%D9%85%D8%B4%DB%8C%D8%B1%D9%87' --note 'page 282, Persian hamšireh sister' 2>&1|tail -2; python3 git/rishe/tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%80%E0%A4%B0' --note 'page 282, Sanskrit kṣīra milk' 2>&1|tail -2; python3 git/rishe/tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%AF%D9%86' --note 'page 282, Persian xordan eat, root of xord' 2>&1|tail -2",
 "description": "Archive more web sources"
}
```


## [2026-09-06T21:38:53.921Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd1 p.502 (leaf 511) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==511' incoming/WLD/WLD_Bd1_pages.txt | sed -n '1,80p'",
 "description": "Read Walde-Pokorny I 502"
}
```


### [2026-09-06T21:38:58.441Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b587a72d8f378885.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/81d200500f5081fe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e019b6ec2053877.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f2a175c6a18dacab.txt
```


### [2026-09-06T21:39:00.188Z] TOOL RESULT

```
=== WLD Bd1 p.502 (leaf 511) ===
                                                                                           ,                                     ;




502                                      qseu-, qsneu-, qneu-, sneu-                   — qseubh-

Lautnachalimung       verhaltenem Niesen gehort; man erinnert andrer-
                                   bei
seits     an qs-n-m       „kratzen“ zu qes- ds.) **qsneu und
                               :    qs-eu-                        vielleicht                                      —
daraus vereinfachtes                     —
                         *sneu und *qneu- in mengl. snesen, engl. sneeze
..niesen" (ahnlich nd. sniisen, dan. snnse ,,schnobern, -wittern"), npers.
isnosa, asnbsa „niesen“ (ahnlich lit. sniaukti ..schnupfen")                       ahd. niosan mnd.     ;                            ,


mengl. ncsen, aisl. hnjosa                    ,,   niesen" (wieder verschieden, aus *pneus, ags .fnco-
snn , hoW.fniesen „ niesen", vgl. aueh mhd. phmtsen niesen, schnauben"; esspielt
wohl die Wz. von gr. nveco zivevya herein). Ygl. Trautmann Bsl. Wb. 266.
                                                       ,



   Im Slav, ein kwh-, kyeh- aus Ms- (z. B. skr.-ksl. kshnovenije Niesen'',                                              ,,


klr. kychaty) und rsch- cich- (*kts - z. B. russ. c'echs Niesen", achats cAchcUs
                                                                     ;                             ,,
                                                                                                                             ,


,,
     niesen").
  Ygl. Zupitza Gutt. 9, BB. 25, 95, Uhlenbeck Ai. Wb. 72, Fick III 4 100f.,
Falk-Torp u. fnyse, nyse snuse, Berneker 165, 658.-
                                              ,




kseud-        ,,klein     stampfen".
                      zermalmt", ksoda- m. „StoB, Stampfen, Zermalmen;
      Ai. kioduti „stampft,
Mehl. Pulver. Puder", kinulrd- ..klein. gering; niedrig, gemein", Komp.
ksoihyas -, kmdra- n. ..Staubchen"; abg. clinch ,, klein; diirftig, gering.
schlecht;         Komp. chnzds/s i: ai. k^ldiyas-).
   Pedersen IF. 5, 60 f. mit fernzuhaltendem, so der u. *qseud- „Fliissig-
 keit" behandelten Sippe von ai. k-6das „Flut". ferner       wie auch KZ. 39.                           —
 428     —
        von gr. ipvdgos ..liignerisch", endlich von lit. siaudjs „Strohhalm".
 simulaT ..Stroh", deren Bed. mit der von ai. ksocla- nur kiinstlicli zu ver-
 einigen ware und die ini Gutt. von chads abweichen wiirden).


 qseud-       ..Fliissigkeit"              (nur arisch).
       Ai.   k sodas-     n.        ..bewegtes Wasser, Flut, Wassermasse, Strom" = av.
 xsaodah-         n.   „FIuB,         Strdmung, Wasserschwall", xsudra -, xsudra- ..fliissig;
 n.     Fliissigkeit",             xsitsta-            (   *ksud-ta -)       ..fliissig,   breiig,      geschmolzen‘‘,                   fsra-
 xiuostra-        n.   ..YorwartsflieBen".   Cbarpentier IF. 28, 178ff., der eine
                                                                    Lit. bei
 Wzvariante ksn-i-(d-) in folgenden, schon wegen der verschiedenen Be-
 deutungswendung auf schleimiges Bedenken weckenden Worten sucht                                                                             ;



 ai. kivrda-, ksvcta- m. ,,Gift“, (mi.) kheta- „Schleim, Rotz", khed aya- „Gift“

 (aber k'slra- ,, Milch" nicht mit ks- aus ksu- in denselben Kreis, s. *ksTro-;
 und av. xivld- „Milcb" zu lit. svestas „Butter", dessen Anlaut trotz Ch. nicht
 wohl aus ksv- herleitbar ist).
    Lit .kudus ..ScheiB" (Pedersen IF. 5, 60 f.) ist im Gutt. unvereinbar.


     qseubh- ..schwanken, in schwingender Bewegung sein".
       Ar. ksiihhyati, ksobhate                            (   ksubhnoti ,   -ndti)    „schwankt,           zittert",   ksobhayati
 ,,setzt     Bewegung", ksobha-h „Schw anken, Erschiitterung"; av. xsaob-
             in                                                                r
```


## [2026-09-06T21:39:17.912Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\ntargets={10985,10988,7542,14800}\nfor i,l in enumerate(txt,1):\n    if i in targets: print('BRT line',i,'leaf',leaf)\n    leaf+=l.count('\\f')\nEOF\necho \"=== BRT leaf 546-548 col numbers ===\"; for n in 546 547 548 549; do echo \"--awk NR=$n--\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BRT.txt | grep -oE '\\b1[0-9]{3}\\b' | head -4; done\necho \"=== BRT xšudra seed ===\"; grep -n \"x3udra\\|xsudra\\|xšudra\\|Samen'\" BRT.txt | head -10",
 "description": "Locate Bartholomae columns"
}
```


## [2026-09-06T21:39:19.510Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY شیر / خرد ===\"; grep -n \"شیر\\b\" incoming/ARY/ARY_pages.txt | head -10; echo \"---\"; grep -n \"خرد\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY latin index ===\"; grep -n -i \"KSEIRO\\|KSIRO\\|KSEUD\\|KSUD\" incoming/ARY/ARY_latin_index_pages.txt | head",
 "description": "Grep Aryanpur"
}
```


### [2026-09-06T21:39:19.595Z] TOOL RESULT

```
BRT line 7542 leaf 218
BRT line 10985 leaf 332
BRT line 10988 leaf 332
BRT line 14800 leaf 465
=== BRT leaf 546-548 col numbers ===
--awk NR=546--
--awk NR=547--
--awk NR=548--
--awk NR=549--
=== BRT xšudra seed ===
8240:•  j.  ui9^e.tät-  f.-  ?  -:  yü  *xsudra  (sd.) *ya£   v3  yasanti  yat  vä  * Aqm.raS^vi}nti
10772:•  j.  xSaOri-  £  TVeib,  Weibchen'  (geschlecht- lich); a)  von  Menschen:  ar»dvT  .  .  hä yaozdahaili  . .  arsnqm  xsudrh  hä  -'^rinatn *garxi>qn  hä  ''hrinqm  paima  Y.  65.  5;  — yd^a  anyasHi  arsänff  avi  xsudra  °%nsiia hqm.v»rmavairtii  V.  iS.^z.  b)  von  Tieren (K.3mtl):yff  (nämhusirS)  ar/nq»t..tnasishm aojS  äbaraiti  . .  yS  '^rtsiia  aväiti  Yt  14. 1 2 ;  ^  avä  zJ  *'in'iu  hupatSJ?ma  ya  ui'trS
10869:KompE.,  A.(?)9.  —  PPfP.  einer  Basis  (ar.) *ksaud-,  woiu  noch  xsaoiah-,  xsudra-,  pm- xia0itra-%  s.  Hdm.  ZDMG.  38.  43i-  —  !'"■ (lu  F.,  Y.):  ^imxt,  (iu  V.);  /,«r.  -  ')  Unthom.; zSchr.  s.  IF.  //.  137.  NA.  xiivisli.  —  ")  S. noch  '^hilasmc.  —  3)  VgL  intay').  —  4)  Hds. hisf.  —  SS.  No.  2.
20920:asavJ  eara'iuslrOY.i2.6;\t-4.T,  —  zatö  be'.mraomi  (sd.)  ..yam  dahmqm  ..  S/rTlTm yS  a/ava  saraiiuärB  y.ip.  46;  Vr. //.  19, '  P.j;^.  c)  IPm.,  n.:  pairi  yäi/  hapta Yt5.io4,  14.2S,  IJ.47;  —  nazdyB  tqm^  karsvqrt  mairyB  apatat /ratgrase  "Vt.  ig.%3; upahi^tat  y  B  spitilfnB  zara^us'tr jYt.  ij.  21;  —  humäyQ.tarala  .  .  inhäma  yäü  ipm- 1 8, 10,  V.  JJ.  1 7 ;  —  uHa  nd  siitB  lihrava  yB  tahe  mainySul  dlmqn  Vr.  12.  4. spittimB  sara^ui/rB  Yt  13. 94  fodcr  zu  A); —  [  Von  undeutlichen  oder  verderbten  Stelleo jasani  il  ava»ha?ca  rafttai>ha!'a  (iwffi_j'5|  erwähne  ich:  hamSm  tatvahUtähtySusu- (zu  A)  ahurS  mazda  fasäiti  .  .yB  varthui  ruy!  syascU  dahmahya  Y.J2. 16;  —  tiBit sraosS  .  .  jasaiiti  .  .  yä  (s.  d)  äpB  Yt  /.  9;  i  ftä  xsnäul yä  v»r>ZSnä  hScä  Y.  4^- 1 ;  — 10. 100;  — yaiä  aha  vairyB  zaotä  frä  tnl  yä  (NDra.)  nara  gatum  baraite  F.^d;  — mrütg ya'iia  aha  vairyB  yä  zaota  frä  mZjaht  ..yB  xsudra  ham.raS%wayäH  V.lS. m^fi/f  Y.J.  25;  N._y7*,  Vr._j,  7; — paoinm  6a '^^i — yS  hapta  hmdu  V./,i8;  —  upa gtima  frabarat  yö  narif  asaonS  urva  H.  2.  |  a^a^u  (sd.)  rauhaya  yB  asärO  aiwyiixia- 15;  7i  8,  15;  —  bavat  aiwl.vanyh  yasi  yanti  V.l.  19;  —  psityh  ähitya  yä  anrö taxmS  kava  vlsiäspö  \X.iy.%i;    —   yim  mainyui  fraksrtniat  V.  20.  3;  —  aridvim
21228:jAw.:  i)  mit  Ind.:  ^°  aiAlA  amS  mkanie spanasia  irista  . .  ka  hl  asti  aha  V.3.  36; iX  36,  37,  12.  i;  —  y  .  .  caratd  dva  mS apajw>tayaaa  V.y.49;  —  hs para  mintS daSvS  .  ■  y  maiys  maitm  xhtdra  avi franhirftaiti  y  vä  mafys  .  .  xsudranqm *pairi,gmrvayäti  V.  Ä32;  —  hs  ba  .  . arhtqm  MtyS  y  na  paurva  frabda  (Sp. 984  o) /rabdsJrajB  framalxaiti  V.  j8.  40; 34,  46,  54;  —  y  aoxte  aiia  . .  a%a  *ha *x/ayete..  haxäsit (sd.)  ü.g;  7;  — y  hakat *amrute  . .  aliü  *ratu/rii y5 . .  N.24;  — ta^a  y  paiti.barvnti  yä  .  .  äjayaurra N,54;  —  yl>  sSne  piÜr^m  jainti  . . yas»*'^ tat . .  täyus  . .  para.baraiti  dasa  (sd.)  oSj/ päili  afsl  aiayai(sd.)  Y.  13. 10;  —  aät y  bavaiti  avijpastS  sasta  .  .  ta  hascit upajbayäte  Yl  13.  69;  46;  —  yO  nars snaHmt  usihiltaiti  a^at  hl  ag^r^ptam  (sd.) y  frasusaiti  altai  hl  avaoirist»m  {sd.)  y . . Y.4.1T,  —  al^  zr  narS  paityeinti  (sd.) *aslS.vitotus  pgsanaiti  yasla'>''  isui..p»ia- naiti yasca^..Y .4.^^^^; — h^m  ita  (s.Ntr.) tltao^ra  bavairiti  (Sp.  939  O.)  yasj*^  tava frabannte  drvantö  . .  ".  .  dann  .  .  wenn (sie)  dir  darbringen  . ."  Yt.5. 94,  2)  mit Konj.  (oder  Inj.);  y  .  .  masdayasna  .  . nassum  frajasqn  ku%a  . .  v^myqn  "ange- nommen den  Fall:  die  M.  stossen  aul einen  Leichnam  .  .,  wie  .  .?"  V.  6. 36: 5.45,  Äi,  4,  J&i;  —  y  •■  spä  avaca va  bavat , ,  kuha  . .  vjrxyqn  . .  masdqyasna V.  13.  39;  35;  — y  . .  masdayasna  bal^atai (sd.)  fravasänte  katärö  paurvB  ämayänie (sd.)  V.  7. 36;  —  y  iavani  (sd.)  aiwi.- sasls  . .  eis  aiAhe  asti  balfazd  Yt  J4.34; —  y  afvS  zaata  (sd.)  frayatäiti .,  zaoiars gatava  N,  tf/;  70;  —  y  ahmt  nmlne  . . nairika  daxstavaiti  arthal  y  vä  ..  *aipi.- irytS.gatus  isd.)  altala  .  .  V.5.  59;  — y pouruiaist^a  hanjasänte . .  t^m  i^ra  ha*- Jasante  V,  7,44;  YL//.6;  —  yas/a^>  .  . väcim  paiti  taBtii' {sd.)  ar?hat  nsil.. täyus .  .  para.baraiti  Y.J3.40;  —  y  ma^äia frayazantt  .  .  rüsit  t^ra  airyä  daiähävS /ras  hyätYt.i4.^&;  — y paoirim . . itryntäl .  .y ' . ,  ktrmtät'  ava  hö  miryaite  anämStS ZT  ais6  Y.y.^T,  —  nthenyesi:  yeti/a  alte asti  . .  gar>mBkva  (sd.)  vjiänte  y  vä  aiU gar^ma  (sd.)  i^ars^a  stamaruM  .  .  apa.- daiai  .  .  aiühai   haca  .  .  bavainti  p»sB.-
21263:. ,  aparaöhayäe  y  v  naimsm  y  v  ä«'- /um  y  V  cahru/um  y  V  paatartkum '^■ig.y,  Y.6.32*,  l6.2*; — yä  *xsudra(ßd.) *y'il  y  yazmti  y  v°  *hqm.ralhwpnii y'v' ..  N.  61.  n)  in  aülimiliger  Ver- wendung; xrafstrMn  ava.janaita  maotrim dänSjiaritm  y"  v'  hama  duyt  laile  kahyä- cit  .  .  xrafstranqm  ava.janyät  y  v  .  . zaOta  "das  Xr.-Geschmeiss,  die  kömer- schleppende  Ameise  soll  er  im  Sommer töten,  zweihundert  Stück,  dagegen  (zwei- hundert Stück)  beliebiger  Xr.s  soll  er  im Winter  töten"  V.  16. 12  {?).
28597:Beziehung  ist  ungenau:  hS para  mtntä . . kS pasca  mirsts  mainyava  datva  frabavainti yat  masyö  masim  xsudra  avi  franhirssaiti V.  i^.  32;  —  hs  bä  trn  altaihm  arlnqm paoiryS  yat  na  . .  naire . .  tWil  daoäiti  V.  iS. 34.  b)  adjektivisch,  nur  mit  nar-  (Sp. 1051  ra.):  ^vai  hö^  nä'  asayeiti  .  .  ä/ai ahmäi  naire  miidtin  a»kal  yS  .  .  ra/i- "kv/irum  .  .  framaräite  A.  4-4f.;  ßf-'i  V. 15.47.  2  a)   auf  eine  erläuternde  oder
29673:enüassen':  "anya.tkaliais^)  näirika pairi      "='"'  Etymologie  bringt  Dst.  ZA.  /.  «3- xsudra  fraipharTsaiW^  Nik.  7.  •  j.hastra- n. 'Versammlung' uzw.  solcher,
```


### [2026-09-06T21:39:19.664Z] TOOL RESULT

```
=== ARY شیر / خرد ===
1363:۴-گفته شده است که واژه‌ی فارسی «شیرین» از واژه‌ی فارسی «شیر» درست شده است (همانگونه
3641:۱ واژه‌ی آانگیین" فارسی از آانگه" به چم "شیر ۰ و عسل" است(برهان قاطع :: ۱۷۴). واجریشه‌ی ۰81881 از هند و
4931:معنی واژه‌ی .5۳۸۸-۳3681 در زبان آلمانی: خوکك شیرخوار,
4979:معنی اين واژه در زبان‌های ژرمنی: تبر زیر شیروانی؛ دیرکك.
5436:چم این واژه در زبان‌های ژرمنی: خامه» سرشیر,
5437:چم این واژه در زبان لیتوانی؛ شیر,
6840:بلوچی (1للعلاءلم8): اند انا آلبانی (4(مشتم: شاهاة شیر
7083:۱ یکی از چم‌های این واژه در زبان‌های ژرمنی: شمشیر؛ درد.
7285:۱ بازگشت به: شیرین.
7837:چم واجریشه‌ی هند و اروپایی این واژه: مکیدن» شیردادن,
---
963:(۸7۳8۸) الهه‌ی خرد ودانش و فنوری بود. در هند نیز سه «کست» (۸8772) به نام‌های «برهمان ۱
11304:چم اصلی این واژه: شکافتن» جداکردن» خردکردن» قطع کردن.
11856:۲- چم این واژه در زبان لاتین: خرد کردن؛ کوفتن.
14019:۱- چم این واژه در سانسکریت و پلفاری: خرد» غاقل,
14024:۲- در اوستایی 11۸210 به چم خردمند" و "عافل " هم بوده است.
=== ARY latin index ===
```


## [2026-09-06T21:39:29.174Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- BRT leaf idx 332 (awk NR=333) top ---\"; awk 'BEGIN{RS=\"\\f\"} NR==333' BRT.txt | head -6; echo \"...\"; awk 'BEGIN{RS=\"\\f\"} NR==333' BRT.txt | grep -oE '\\b[0-9]{3,4}\\b' | head -8; echo \"--- xšudra headword search ---\"; grep -n \"'Same\\|Samen\" BRT.txt | head -10",
 "description": "Bartholomae column numbers and xšudra headword"
}
```


### [2026-09-06T21:39:30.802Z] TOOL RESULT

```
--- BRT leaf idx 332 (awk NR=333) top ---
vä  V.5.45. Pü.:  sai  mähak.
•  j.  x5va§.satö.-zyain-"  m.,  Pltir.  'sechs- hundert Winter':  aa$yimäi  xsakrai  *°zima (NP.)  *kmjas>nta  V.2.12.
Pii. :  an  i  iahim  lai  i  tam.  —  VgL  ai.  iaiä- kima-  Adj.
•  j.  x^vazaya  Adv.  'sechsmal':  spumm  . . iayaüil  tata    aai  pa%ä    vJväoayantu    V.
'.17.    '
uänft'af
...
564
846
140
113
274
103
567
567
--- xšudra headword search ---
4043:•  j.  a-fra'nharsza-  Adj.  'sich  nicht  er- giessend';  °sat  J>airi  xsudrät  "ohne  dass Samenerguss  erfolgt''  W.iG.id.
4094:•  j.  aß-äSra-'*  Adj.  'den  Samen  des Wassers  enthaltend',  von  Sternen*':  Hstrim staivm  °r»n  Yt<?.4;  —  vlspe  starB  'ra S.IM3;  Yt/i'.z9;—  U.ira  gufra  'raukö
4738:"er  lässt  seinen  Samen  in  eine  Frau,  die  'M, .  .rm>rä,Yt.,o.26;  A.i.i.'F.y«;
5828:•  j,  astvat^rsta-  m.  EN.  des  dritten  der drei  Söhne  Zara^ustras,  die  aus  dessen; im  See  Kasaoya  aufbewahrten  Samen hervorgehen  sollen '' " :  uxsyatjtylahe  .  . uxsyai.mmanhs . .  'Iahe  aiaota  Yt  13. 1 28; HO,  117;  —  yttt  'lö /raxstäile  haca  apat kasaoyät  asts  mazdä  ahurahe  vjspa.taur- v'ayä  (sd.)  pu^rif  Yt.i5.92;  —  Aaxayif.. Hahe  vjrihrayne  Ytig.^s;  —  {'laAe)  ys atiAai  sao^as  (sd.)  vtrüraja  nama  'fasca iiqma  . .  ava'ha  'tS  ya%a  astva  kam  usfa- nava  (sd.)  astval  *aihyejahim  paitisät  Yt. JJ.129.
6505:•  j.  as.dSnav-  Adj.  'mit  starken,  grossen  •  P-  aSna-  m.  'Marschiren',  mit  astty  'er (Samen-)Körnem':  us  apam  aoavS  .  .  befindet  sich  auf  dem  Marsch  nach  — ' jasänti  -nunqmca  yavanq'm  kasuJätm-  («^V  »"'*  Akk.):  *adaiiy  adam  ^naiy^^ natnca  västra'nam  "die  wässerbäche  wer-  •'^'"»  "^'y  ''uv'^jam  pasäv<^  kacämi/' den.,  hervorbrechen  hin  zum  Getreide  atars<^^y^  uz-aßyä  "damals  war  ich mit  den  grossen  und  zum  Gras  mit  den  ^  d^™  Marsch  nach  Susa;  drauf  bc- kleinen  Körnern"  YtÄig".  kamen  die  Suser  Furcht  vor  mir"  Bh.2.4.
7166:%raodet  *^/ara%ra  (s  294.  3)  verlangte.  imSchlaf  ergossenenSamen  vorgeschrieben
7177:T  rausgese    .  ,.,     .  ,         |  den  im  Schlaf  ergossenen  Samen  vorge-
7188:•  j.  ätrv.karst-  Adj.  'der  sich  mit  dem  j  ')  Nämt.  dem  Mann,  der  seinerieit  {»/•"  süram Feuer  zu  tun  macht,  dabei  tätig  ist':  'tä,  /raB.i-^y^nm)  aus  dem  im  Schlaf  ergossenen p  _                                                                             !  Samen  erstehen  soll;  rgl.  v.  iS.  40,  51.
7191:•  ].  atM.Öarana-  n.  'Feuergerat,  zur  In-  '  ^'  ^  ,  ,  ^  ,  ,.  ,.  „,  ,-' standhaltung  des  Feuers  dienendes  Gerät':  .^°|- „  ^)  ^nter  den  Namen,  d,e  fiir  den '«  (AP.)  pairisMnäna  V.  14. 7-                   ""^^'"^^  ergossenen  Samen  vorgeschrieben
7649:*)  Indem  sie,  im  See  Kqs/Kiya  badend,  von dem  daselbst  verwahrten  Samen  Zara%ui/ras befruchtet  wird;  s.  unter  xhiJra-,  wo  litt.*) Eig.  'die  dem  Vater  Gedeihen  schafft',  fem. vP'iridal.fUar- k.fi\.;  *>r3daul- kAy,  PPA.  lum V.  arfd-.  —  ■)  Die  mp.  Namensform  wäre nach  West  SBE.  4/.  115  gSviJk  pil  'having  a tcätifying  fathet'  zu  lesen.     Sehr  zweifelhaft.
```


## [2026-09-06T21:39:31.690Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6835,6850p' incoming/ARY/ARY_pages.txt; echo \"=== which pdf page ===\"; python3 - <<'EOF'\ntxt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ncur=None\nimport re\nfor i,l in enumerate(txt,1):\n    m=re.match(r'\\[pdf page (\\d+)\\]',l.strip())\n    if m: cur=m.group(1)\n    if i in (6840,7285,14019): print('line',i,'pdf page',cur)\nEOF",
 "description": "Read Aryanpur context"
}
```


### [2026-09-06T21:39:34.794Z] TOOL RESULT

```
[pdf page 232]
خله ۱۳۳۱
پارسی باستان (0۷ای۶87 صا0): هقایة2» پرتغالی (۳077001882): ۸0
پهلری (۷1مانمه): 21 ایرلندی کهن (57ل1 صان): 0
کردی (080/370): لش ,اباشاز ,22۷ گالی (للقلانامه): 07
بلوچی (1للعلاءلم8): اند انا آلبانی (4(مشتم: شاهاة شیر
افغانی (پشتو) (۸۲077۸(17م: 4 ,086
ختنی (6707۸(۳37). 1۸ پسگشت‌ها شید
سانسکریت (۸(587: 2014301۸8 7 و
ارمنی (7ل۸/82۵): اد 0 ,163 :ما0
یونانی (0850): 5 مه
لاتین (110): ۸5 9 (6۸) ,109 (۸1-058))
فرانسه (/#52): ۸ 1008 :05 هلتهاد
اسپانیایی (8۳۸(/154): ان ۹۲ :یم
ایتالیایی (7مله1): ۸0 5 (0۱8[۶۳) ,275 هه
رومانی (۸2۸7(ج): ۸۸ برهان قاطع : ۷۰۴
=== which pdf page ===
line 6840 pdf page 232
line 7285 pdf page 247
line 14019 pdf page 471
```


## [2026-09-06T21:39:47.496Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== PII ksiHram ===\"; grep -n -i \"substrat\\|Lubotsky\\|Descendants\\|kṣīrá\\|xšīra\\|Proto-Iranian\" b587a72d8f378885.txt | head -25; echo; echo \"=== hamshireh ===\"; grep -n -i -B2 -A6 \"Etymology\" 81d200500f5081fe.txt | head -40",
 "description": "Read PII and hamshireh pages"
}
```


### [2026-09-06T21:39:47.552Z] TOOL RESULT

```
=== PII ksiHram ===
71: Descendants 
140: Unknown; possibly cognate with Albanian hirrë ( “ whey ” ) , [ 1 ] perhaps both borrowed from an Asiatic substrate language, [ 2 ] [ 3 ] or possibly further connected to Proto-West Germanic *hwaij ( “ whey ” ) , from Proto-Indo-European *tkʷeyH- , *tkʷeHy- . [ 4 ] [ 5 ] 
225: Descendants
229: Sanskrit: क्षीर ( kṣīrá ) ( see there for further descendants )
231: Proto-Iranian: *xšiHrám ( see there for further descendants )
238: ^ Lubotsky, Alexander ( 1999 ), “The Indo-Iranian substratum”, in Early Contacts between Uralic and Indo-European: Linguistic and Archaeological Considerations ‎ [1] , Helsinki 
253: Proto-Indo-Iranian terms borrowed from substrate languages 
254: Proto-Indo-Iranian terms derived from substrate languages 

=== hamshireh ===
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Synonyms 
--
77-
78- 2.1 
79: Etymology 
80-
81- 2.2 
82- Pronunciation 
83-
84- 2.3 
85- Noun 
--
155- [ edit ] 
156-
157: Etymology
158- [ edit ] 
159-
160- From Persian همشیره ( hamšire ) .
161-
162- Noun
163- [ edit ] 
--
180- [ edit ] 
181-
182: Etymology
183- [ edit ] 
184-
185- From هم ( ham , “ also, too, same ” ) +‎ شیر ( šīr  / šir , “ milk ” ) +‎ ـه ( -a  / -e , noun forming suffix ) .
186-
187- Pronunciation
188- [ edit ]
```


## [2026-09-06T21:39:50.241Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FSD/WEB seersucker ===\"; grep -n -i \"seersucker\" FSD_vol4.txt FSD_vol3.txt WEB_vol1.txt 2>/dev/null | head -5; echo \"=== MON shir ===\"; grep -n \"شیرو شکر\\|شیروشکر\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -5",
 "description": "Grep Funk&Wagnalls, Webster, Moin"
}
```


### [2026-09-06T21:39:50.322Z] TOOL RESULT

```
=== FSD/WEB seersucker ===
=== MON shir ===
```


## [2026-09-06T21:40:04.145Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HJB variants ===\"; grep -n -i \"sirsakar\\|seersuck\\|shir-o-shakar\\|shir o shakar\" HJB.txt AID.txt RCH.txt SKT.txt FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head; echo \"=== MON files list ===\"; ls -la incoming/MON/ 2>/dev/null | head; echo \"=== grep MON for شیر headword ===\"; grep -c \"شیر\" incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null",
 "description": "Search Anglo-Indian and Moin sources"
}
```


### [2026-09-06T21:40:04.243Z] TOOL RESULT

```
=== HJB variants ===
=== MON files list ===
total 48692
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4331421 Sep  4 14:06 MON_2vol_Adena_v2_djvu.txt
=== grep MON for شیر headword ===
429
```


## [2026-09-06T21:40:07.991Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb; python3 git/rishe/tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%B4%DB%8C%D8%B1%D9%88%D8%B4%DA%A9%D8%B1/' --note 'page 282, Persian sir-o-sekar, Moin/Dehkhoda entry' 2>&1|tail -2; python3 git/rishe/tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/x%C5%A1iHr%C3%A1m' --note 'page 282, Proto-Iranian *xsiHram milk, descendants incl Sogdian Ossetic' 2>&1|tail -2",
 "description": "Fetch abadis and Proto-Iranian page"
}
```


### [2026-09-06T21:40:12.709Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/813f46778c919041.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/26911bfdb33a3f53.txt
```


## [2026-09-06T21:40:17.561Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== abadis shirosekar ===\"; grep -n \"شیر و شکر\\|شیروشکر\\|معین\\|دهخدا\" 813f46778c919041.txt | head -20; echo; echo \"=== Proto-Iranian xsiHram descendants ===\"; sed -n '1,40p' 26911bfdb33a3f53.txt | head -5; grep -n -i \"Sogdian\\|Ossetian\\|Middle Persian\\|Khotanese\\|Descendants\\|Bactrian\\|Yaghnobi\" 26911bfdb33a3f53.txt | head -25",
 "description": "Read abadis and Proto-Iranian pages"
}
```


### [2026-09-06T21:40:17.627Z] TOOL RESULT

```
=== abadis shirosekar ===
4:TITLE: شیر و شکر - معنی در دیکشنری آبادیس
6:شیر و شکر - معنی در دیکشنری آبادیس 
10: شیر و شکر
14: لغت نامه دهخدا
16: شیر و شکر. [ رُ ش ِ ک َ ] ( ترکیب عطفی ، اِ مرکب ) شیر مخلوط با شکر. ( فرهنگ فارسی معین ). || سخت آمیخته و اختلاطیافته. ( یادداشت مؤلف ).
17:- شیر و شکر برآمدن ؛ شیر و شکر بودن. کنایه از غایت اختلاط است. ( از آنندراج ) : 
19:شکرلبی که به شیر و شکر برآمده است. ملا شانی تکلو ( از آنندراج ).
20:رجوع به ترکیب شیر و شکر بودن شود.
21:- شیر و شکربودن ؛ شیر و شکر برآمدن. کنایه از غایت اختلاط است. ( از آنندراج ) : 
26:رجوع به ترکیب شیر و شکر برآمدن شود.
27: || قسمی بستنی از شیر و شکر. ( یادداشت مؤلف ). || شیر و شکری. سپید با گلهای زرد: عمامه شیروشکری ؛ سپید و زرد. ( یادداشت مؤلف ) : 
33:شکم اندوده ای به شیر و شکر. نظامی.
34:گفتند اینها دلفریب چون میان بند شیر و شکر است. ( نظام قاری ).
36:کند شیر و شکر دستار خوان را. سلیم ( از آنندراج ).
38:- قصب شیر و شکر؛ نوعی پارچه : 
57: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 

=== Proto-Iranian xsiHram descendants ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/x%C5%A1iHr%C3%A1m
FETCHED: 2026-09-06T21:40:12Z
STATUS: 200
TITLE: Reconstruction:Proto-Iranian/xšiHrám - Wiktionary, the free dictionary

71: Descendants 
225: Descendants
229: > ? Khotanese: [script needed] ( tcīratsa , “ sweet juice ” ) ( + *cyah ? [ 5 ] ) 
231: Ossetian: 
232: Digor Ossetian: ӕхсир ( æxsir ) , хсир ( xsir ) 
233: Iron Ossetian: ӕхсыр ( æxsyr ) , хсыр ( xsyr ) 
252: Middle Persian: ( /⁠šīr⁠/ ) 
299: Requests for native script for Khotanese terms 
300: Middle Persian term requests 
301: Requests for Book Pahlavi script for Middle Persian terms
```


## [2026-09-06T21:40:19.959Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nfor f in ['incoming/MON/MON_2vol_Adena_v1_djvu.txt','incoming/MON/MON_2vol_Adena_v2_djvu.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for m in re.finditer(r'شیر\\s*و\\s*شکر|شیروشکر|همشیره', t):\n        s=max(0,m.start()-200); print(f, '...', t[s:m.end()+250].replace('\\n',' ')[:450]); print('---')\n        break\nEOF",
 "description": "Search Moin text for compounds"
}
```


### [2026-09-06T21:40:21.697Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v1_djvu.txt ... 2۷2)0(۲۳12-.2 (ام_ف.) آن  جبزی که آب آن را بباورد. آب آورد.  خاشاک و جزه آن که دریا با رود با سیل با  خود آورد. چشم آب آورده: چشمی که به  بیماری اب مبتلا باشد.   آباجی: 2.0211 [تر. - آغایاجی] (امر.)  همشیره» خواهر» ابجی باچی.   اباد: 5024 (ص.) معمورء دایر» بریا؛ مق  ویران» خراب. مزروع» کاشته. بر» مشحون»  ممتلی. سالم» تن‌درست. بسامان؛ منظم.  مرفه» در رفاه. (ا.) آبادی؛ معموره؛ مق  ویرانه» خرابه. (صت. ادات تحسین و دعا)»  آفرین! احسنت! مرحبا! زه! بصو
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt ... با هم سبفر کنند  (نسبت به یکدیگر)  سنگ؛ هممسنگ: ۱۰-8۵ (ص.)   هم‌وزن. (مج.) همشأن» هم مر تبه.  هم‌شیر» همشیر: :۰-۵3 (ص.) دو يا چند  کودک که از بک بستان شبر خورده‌انده  برادر با خواهر رضاعی.  هم شیر ه» همشیره: (3]۳)6-. (ص. !.)  خواهر (خواه با شخص از یک مادر باشد و  خواه رضاعی)» اخت. برادر رضاعی (عسم.)  ضح.-های آخر این ترکیب های نسبت است  و اين کلمه به معنی همشیر (اعم از پرادر یا  خواهر) و به معنی همشیر (اعم از برادر با  خواهر) و به معنی دو تن است ک
---
```


## [2026-09-06T21:40:38.038Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD watkins roots ksei/kseud ===\"; grep -n -i \"^kseu\\|^ksei\\|^ksero\\|milk\\b\" AHD_watkins1985.txt | head -15; echo \"=== IEC leaf for 576/1060 check ===\"; python3 - <<'EOF'\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(txt,1):\n    if i in (8190,8230,14377): print('line',i,'leaf',leaf,'printed~',(leaf-15)*2,'or',(leaf-15)*2+1)\n    leaf+=l.count('\\f')\nEOF",
 "description": "Check AHD roots and IEC page mapping"
}
```


### [2026-09-06T21:40:39.631Z] TOOL RESULT

```
=== AHD watkins roots ksei/kseud ===
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
739:melg-. To rub off; also to milk. I. 1. Zero-grade form *mig- in Latin mulgére, to milk: EMULSION. 2. Full-grade form *melg- in Germanic *melkan, to milk, was contami- nated with an unrelated noun for milk, cognate with the Greek and Latin forms given in II. below, to form the blend *meluk- in: a. Old English meolc, milc, milk: MILK; b. suffixed form *meluk-ja-, giving milk, in Old English -milce, milch: MILCH Cc. Old High German miluh, milk: MILCHIG. II. Included here to mark the unexplained fact that no common Indo-European noun for milk can be reconstructed is another root *g(ajlag-, *g(a)lakt-, milk, found only in: a. Greek gala (stem galakt-), milk: (GA- LACTIC), GALACTO-, GALAXY; AGALACTIA, POLYGALA; b. Latin lac (stem lact-), milk: (LACTATE), LACTEAL, LACTESCENT, LACTO-, LETTUCE; C. the blended Germanic form cited in I. 2. above. [Pok. melg- 722, glag- 400.]
1870:MIL? gheslo- MILCH melg- MILCHIG melg- MILD mel-? MILDEW melit- MILE gheslo- MILFOIL bhel-3, gheslo- MILIEU medhyo- MILIUM mele- MILK melg-
=== IEC leaf for 576/1060 check ===
line 8190 leaf 326 printed~ 622 or 623
line 8230 leaf 327 printed~ 624 or 625
line 14377 leaf 587 printed~ 1144 or 1145
```


## [2026-09-06T21:40:39.883Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb; python3 git/rishe/tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D5%AD%D5%B8%D6%80%D5%A4' --note 'page 282, Armenian xord (Mann IEC 576)' 2>&1|tail -2",
 "description": "Fetch Armenian խորդ"
}
```


### [2026-09-06T21:40:42.763Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/890be83c4fa08cb4.txt
```


## [2026-09-06T21:40:50.212Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 326 327 328 587 588; do echo \"--- IEC awk NR=$n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | grep -oE '\\b(5[0-9][0-9]|6[0-9][0-9]|10[0-9][0-9]|11[0-9][0-9])\\b' | head -6; done",
 "description": "Find printed page numbers in Mann"
}
```


### [2026-09-06T21:40:52.317Z] TOOL RESULT

```
--- IEC awk NR=326 ---
503
503
572
523
504
502
--- IEC awk NR=327 ---
537
574
503
501
--- IEC awk NR=328 ---
575
504
576
504
502
--- IEC awk NR=587 ---
1058
1059
--- IEC awk NR=588 ---
1060
502
1061
```


## [2026-09-06T21:40:58.349Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i -A4 \"Etymology\\|խորդ\" 890be83c4fa08cb4.txt | sed -n '1,60p'",
 "description": "Read Armenian xord page"
}
```


### [2026-09-06T21:40:58.397Z] TOOL RESULT

```
4:TITLE: խորդ - Wiktionary, the free dictionary
5-
6:խորդ - Wiktionary, the free dictionary 
7-
8- Jump to content 
9-
10- Main menu 
--
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
85: Etymology 
86-
87- 2.2 
88- Noun 
89-
--
107: խորդ 
108-
109- 2 languages 
110-
111- Հայերեն 
--
169: Etymology
170- [ edit ] 
171-
172: Learned borrowing from Old Armenian խորդ ( xord ) .
173-
174- Pronunciation
175- [ edit ] 
176-
--
184: խորդ • ( xord ) 
185-
186- ( archaic ) synonym of կռունկ ( kṙunk ) 
187-
188- Declension
--
199: խորդ ( xord ) 
200-
201: խորդեր ( xorder ) 
202-
203- dative 
204-
205: խորդի ( xordi ) 
206-
207: խորդերի ( xorderi ) 
208-
209- ablative
210-
211: խորդից ( xordicʻ ) 
212-
213: խորդերից ( xordericʻ ) 
214-
215- instrumental
216-
217: խորդով ( xordov )
```


## [2026-09-06T21:41:03.529Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '220,330p' 890be83c4fa08cb4.txt",
 "description": "Read rest of Armenian page"
}
```


### [2026-09-06T21:41:03.576Z] TOOL RESULT

```
 locative 

 —

 —

 definite forms

 nominative 

 խորդը  / խորդն ( xordə / xordn ) 

 խորդերը / խորդերն ( xorderə / xordern ) 

 dative 

 խորդին ( xordin ) 

 խորդերին ( xorderin ) 

 1 st person possessive forms (my)

 nominative 

 խորդս ( xords ) 

 խորդերս ( xorders ) 

 dative 

 խորդիս ( xordis ) 

 խորդերիս ( xorderis ) 

 ablative

 խորդիցս ( xordicʻs ) 

 խորդերիցս ( xordericʻs ) 

 instrumental

 խորդովս ( xordovs ) 

 խորդերովս ( xorderovs ) 

 locative 

 —

 —

 2 nd person possessive forms (your)

 nominative 

 խորդդ ( xordd ) 

 խորդերդ ( xorderd ) 

 dative 

 խորդիդ ( xordid ) 

 խորդերիդ ( xorderid ) 

 ablative

 խորդիցդ ( xordicʻd ) 

 խորդերիցդ ( xordericʻd ) 

 instrumental

 խորդովդ ( xordovd ) 

 խորդերովդ ( xorderovd ) 

 locative 

 —

 —

 Derived terms
 [ edit ] 

 խորդենի ( xordeni ) 

 References
 [ edit ] 

 “ խորդ ”, in Žamanakakicʻ hayocʻ lezvi bacʻatrakan baṙaran [ Explanatory Dictionary of Contemporary Armenian ] (in Armenian), Yerevan: Academy Press, 1969–1980 

 Old Armenian
 [ edit ] 

 Etymology
 [ edit ] 

 The origin is uncertain. According to J̌ahukyan, perhaps of imitative origin, connected with the onomatopoeic verb խորդամ ( xordam , “ to snore; to snort ” ) .

 Noun
 [ edit ] 

 խորդ • ( xord ) 

 common crane ( Grus grus ) 

 flock of cranes
```


## [2026-09-06T21:42:23.597Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(t,1):\n    if i==34437: print('KLN line 34437 leaf',leaf,'printed~',(leaf-12)*2,(leaf-12)*2+1)\n    leaf+=l.count('\\f')\nEOF\nfor n in 730 731; do echo \"--- KLN awk NR=$n page nums ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -oE '\\b1[34][0-9][0-9]\\b' | head -4; done\necho \"=== POK kseud ===\"; grep -n \"kseu-d\\|kseud-\\|k^seud\\|kseu- d\" POK_full.txt POK_02.txt 2>/dev/null | head -6",
 "description": "Klein page for seersucker; Pokorny kseud"
}
```


## [2026-09-06T21:42:25.135Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT xvar- eaten PPP ===\"; grep -n \"x\\\"ar»ta\\|xVar»ta\\|ar»ta-  Adj\\|'gegessen'\\|gegessen\" BRT.txt | head -10; echo \"=== CHEUNG hwar ===\"; grep -n -i \"hwar\\|xwar\" CHEUNG.txt | head -8",
 "description": "Bartholomae xvarəta and Cheung"
}
```


### [2026-09-06T21:42:25.205Z] TOOL RESULT

```
KLN line 34437 leaf 749 printed~ 1474 1475
--- KLN awk NR=730 page nums ---
1373
--- KLN awk NR=731 page nums ---
=== POK kseud ===
POK_02.txt:4503:kseud-  jklein  stampfen'.
POK_02.txt:4507:Verbindung  von  ai.  ksudrd-  mit  av.  x§udra-  ,flüssig*  (s.  2.  kseud-)  versucht Batakrishna  Ghosh  (Les  formations  nominales  en  p^  S,  21)  zu  begründen.
POK_full.txt:48878:Root / lemma: kseud- {*gheud-) 
POK_full.txt:48901:connection from Old Indie ksudra-W\\h Avestan xsudra-^i\u\(y (see kseud-2} attempts
```


### [2026-09-06T21:42:25.272Z] TOOL RESULT

```
=== BRT xvar- eaten PPP ===
3186:Pii. :  anapasmiin'\  [itx  Y.  g):  ana/VKäyistii); erl,;  ka  »."att  mal  "wenn  gegessen,  ials  wieder da";  Sü.:  atiavasääah.  —  ')  NA.  'jay'  mit rt4!  s.  aber  K  s  und  Yt.  75.  16.  —  >)  Vgl. lu  satil-.  —  Sl  Vgl.  ai.  apahänay-  f.
17801:•  j.  fra-var»ta-  Adj.,  PPfP.:  s.  'var-.
=== CHEUNG hwar ===
278:of M. Samadi, “Das chwaresmische Verbum”, has been used. For Middle Western 
746:Choresmian = Khwarezmian 
4693:CSogd. füm'ty ‘insufflated’ (cf. Schwartz 1967: 57) 
5142:wrap’ || (+ *aua-) BSogd. ’wö’yz, CSogd. ’wdyZ ‘to strangle’ (Schwartz 1971: 412b) 
5740:*REFERENCES: IIFL II: 225a, 205a, 258a; GMS: §972; Abaev, Slovar’ I: 181 f.; Schwartz 1967: 56 f.; 
5950:(+ *pati-) CSogd. ptZnq ‘pledge’ (*pati-dranga-, Schwartz 1967: 112) || (+ *ш-) 
5964:*SANSKRIT: (+ *aua) ? BSkt. avadranga- ‘earnest money’ (cited by Schwartz 1967: 
6013:howl, talk (daevic)’ (Schwartz, l.c.). 0 The Persian forms can also derive from *zrad
```


## [2026-09-06T21:42:35.327Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- KLN leaf 749 (awk 750) page nums ---\"; awk 'BEGIN{RS=\"\\f\"} NR==750' KLN_1966.txt | grep -oE '\\b1[34][0-9][0-9]\\b' | head -6; echo \"--- POK page for kseud ---\"; python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(t,1):\n    if i in (4503,4507): print('line',i,'leaf',leaf)\n    leaf+=l.count('\\f')\nEOF\nsed -n '4498,4512p' POK_02.txt",
 "description": "Klein page and Pokorny kseud context"
}
```


## [2026-09-06T21:42:36.266Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"\\*Hu̯ar\\|HUAR\\|‘to eat’\\|to eat, consume\" CHEUNG.txt | head -10",
 "description": "Cheung root for eat"
}
```


### [2026-09-06T21:42:36.948Z] TOOL RESULT

```
--- KLN leaf 749 (awk 750) page nums ---
1410
--- POK page for kseud ---
line 4503 leaf 285
line 4507 leaf 285
Daß  ks^-ro-  eine  Erweiterung  von  ksä-  ,brennen,  versengen'  sei,  ist  wahr- L     scheinlich. i       WP.  I  503,  Schwyzer  Gr.  Gr.  I  329.
kseuhh-  ,schwanken,  in  schwingender  Bewegung  sein'.
Ai.  ksübhyatij  ksöbhate  (ksubhnöti,  -näti)  ,schwankt,  zittert',  ksöbJiayati ,setzt  in  Bewegung',  ksöbha-  m.  , Schwanken,  Erschütterung';  av.  x§aob- ,in  Aufregung  geraten'  (xsufsqn),  npers.  ä-mftan^  ä-§öftan  ,in  Bewegung versetzen',  ä-söb  , Verwirrung,  Tumult';
poln.  chybac  ,schaukeln,  hin  und  her  bewegen' ;  cJiybki  ,behend,  rasch' ;  klr. chybdty  ,zweifeln,  unschlüssig  sein',  chyba  (*ksüba)  , Mangel,  Fehler'  usw.
WP.  I  502  f.,  Trautmann  144.
kseud-  jklein  stampfen'.
Ai.  ksödati  ,stampft,  zermalmt',  ksöda-  m.  ,Stoß,  Stampfen,  Zermalmen; Mehl,  Pulver,  Puder',  ksudrd-  ,klein;  niedrig,  gemein',  Komp.  ksödlyas-] ksudrd-  n.  ,Stäubchen';
abg.  chud^ ', klein-,    gering,   schlecht',    Komp.  chuzdhjh   (:  ai.  ksödiyas-).
Machek  (Slavia  16,  174)  nimmt  als  ursprüngl.  Bedeutung  ,mager'  an (cech.  chudy  ,mager'),  das  er  somit  zu  ai.  ksudhyati  ,hungert',  ksödh-uka- ,hungrig'  stellen  möchte.
Verbindung  von  ai.  ksudrd-  mit  av.  x§udra-  ,flüssig*  (s.  2.  kseud-)  versucht Batakrishna  Ghosh  (Les  formations  nominales  en  p^  S,  21)  zu  begründen.
WP.  I  502.
40
626  •
kpei'  ,siedeln,  sich  ansiedeln,  eine  Niederlassung  gründen*.
Ai.  ksiti,  hsiydti  ,weilt,  wohnt',  av.  saeiti  ds.,  ai.  ksiti',  av.  Hti-  ,Wohn.' platz,  SiedelungS   ai.  kskra-,   av.  söid-ra-  n.  ,Gnindbesitz,  Wohnplatz',  ^j^ Jcsema-  m.  ,ruhiges  Verweilen';
```


### [2026-09-06T21:42:36.991Z] TOOL RESULT

```
521:Éópevou, Lat. edere, Goth. itan, etc.) has been supplanted by *huar, which 
2103:*Huar ‘to cover’, which is not mentioned in DKS: l.c. 
3513:*SANSKRIT: cas ‘to eat’ (Dha.), casaka- ‘drinking vessel’ (class.) > EWAia III: 183f. 
6502:*NWIR: Siv. far-, Khr. for- ‘to eat’, NP (Tadj.) furt, for ‘gulp’, Gz. fart ‘sip, gulp [of 
6503:drinking]’. © These forms may not necessarily derive from *huar- (with "Median" 
10284:*huar 1 147 
10309:*huar' ‘to consume, eat’ 
10326:*PARTHIAN: wxr- ‘to eat’ || (+ *4-) "xwr- ‘to eat, consume, devour (of fire)’ 
10334:*SOGDIAN: SSogd. xwr-, BSogd. xwr-, CSogd. xwr-, MSogd. xwr- ‘to eat, consume’, 
10349:148 *huar |
```


## [2026-09-06T21:42:49.564Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Molken\\|ksiro\\|kslro\\|ksīro\" POK_01.txt POK_02.txt POK_03.txt 2>/dev/null | head -10; echo \"--- CHEUNG huar page ---\"; sed -n '10309,10330p' CHEUNG.txt",
 "description": "Check Pokorny for milk root and Cheung huar"
}
```


### [2026-09-06T21:42:49.633Z] TOOL RESULT

```
POK_03.txt:1984:seu-k-:  osset.  xurx  ,Molken,  Käsewasser^  (ar.  *sukra-:  lit.  suJcrüs  ,*was  /.. sich  leicht  dreht') ;  lit.  sunkalai  PI.  , Molken',  pä-sukos  ds. ;  lit.  sukü,  sühti  77 , drehen,  wenden^,  sukrüs  , beweglich,  flink',  apsitkalas  , Türangel*,  lett.  sukt  ^f^ ,entwischen*,  sukata  ,Drehkrankheit',  slav.  *s^kQ,  *s^kati  (Prät.-St.  *sukä-)  '^ in  russ.  sku^  skaH  ,zwirnen,  zusammendrehen,  aufwickeln*,  ablaut.  ksl. '^* sukati  , drehen'  (umgebildet  aus  *soukeie-j  vgl.  russ.  suHH  ,zwirnen*);
POK_03.txt:3342:Gr.  (ßVTtog  m.  ^Schmutz,  UnreinlichkeitS  Qvrröayj  Qv^raivo)  ,befl^y ^vnaQÖg  ^schmutzig',  Qvrtdcj  ,bin  schmutzig',  ^vn;og  n.  ,Molken»,  f^^ ,reinigeS  Med.  ^wasche  mich,  schneuze  mich*;  urslav.  ''strup^  {&\xB*srtup^ oder  *sroupos)  ,Wunde^  (aksl.;  eig.  ,*Schorf  auf  der  Wunde^,  ,Gift,  fi^^ (slov.),  ,SchorP  (nbulg.  russ.),  ^Ausschlag  bei  Kindern^  (skr.),  ,Q^^ Kruste'  (pohi.  dech.);  ablaut.  ksl.  str^'p^t^  ,Rauheit,  Härte'. WP.  II  703,  Vasmer  3,  32.
POK_01.txt:1873:Neben  der  sehr  fruchtbaren  Wzf.  bbereu-  (s.  dort)  ist  wohl  auch bh{e)rei-,  bh(e)ri-  anzuerkennen.  Auf  diese  kann  bezogen  werden  ai. jar-bhurl-ti,  gr.  *q)VQi-(x),  *7tOQ(pvQi-(o  (s.  oben);  mit  xn -Formantien  vermut- lich gr.  (pQL^dcj,  q)Qi^daao(xat  , bewege  mich  unruhig,  springe,  schnaube*; aisl.  brimi  ,Feuer';  mengl.  brlm  ,Glut*,  wahrscheinlich  auch  aisl.  biim  n. , Brandung',  ags.  hnm  n.  ,Meer,  See*;  die  in  brühen,  Brodem,  braten  yot- liegende  Bedeutungsfärbung  kehrt  wieder  in  norw.  prim  ,eine  Art  aus saurem  Molken  unter  starkem  Kochen  bereiteter  Käse*  (auch  nhd.  Brimsen- käse), mdartl.  auch  bi'lm  ,ds.;  auch  Kruste,  Bodensatz  einer  eingekochten Flüssigkeit*  (nbd.  bair.  Brimsen,  Brinzen  ,was  sich  beim  Mus  angebräunt an  der  Pfanne  festsetzt');  daneben  mit  formantischem  -uo-  sehr  wahr- scheinlich abd.  brio,  mbd.  brl(e),  ags.  briw  ,Brei'  (als  ,*Sud,  Gekochtes'), briwan  , kochen*;  hierzu  auch  mir.  breo  ,Flamme*  (*bhri-uo-).
POK_02.txt:750:iiorw.  haure  ,krause  Locke  (bes.  von  Wolle)',  kaur  ,gekräuselte  "Welle^ (idg.  "^gou-ro-;  daneben  germ.  '^kait-ara-  in:)  anord.  karr  m.  ,krause  Locke' käri  ,das  Wasser  kräuselnder  Windstoß',  norw.  käre  ,Hobelspan' ;  mit  -^u, das  germ.  Lehnwort  finn.  keuru  ,curvus';  mit  iZ  (vgl.  yvqoq  und  die  ^  ent. haltenden  arm.  Worte)  norw.  küra  ,sich  zusammenkauern;  ruhen',  mn^ küren  ,(dem  Wild)  auflauern',  nhd.  kauern]  mit  Anwendung  von  Gerinnen der  Milch  norw.  kjere  i^keuran-)  ,Käse  im  ersten  Zustand',  kür  (^kuraÄ ,ds.,  geronnene  Milch',  keyr  {^^kauri-)  ,Käsemasse  von  säuerlicher  Milch* kaara  (^kauarön)  ,gerinnen,  käsig  werden'  (fraglich  hingegen  sloven usw.  zur  , Molken'  wegen  der  auf  g  weisenden  Nebenform  sloven.  züra zgra  ,Molken');
POK_02.txt:4554:mit  andern  Formantien  vermutlich  arm.  siv  ,Bodensatz  gepreßter  Trauben, (kift-uo-)]  viel  unsicherer  ags.  hwceg^  mndl.  ivey  ,Molken'  (*kuoio-?).
POK_02.txt:5977:Hierher  wohl  ai.  ä-miksä  ,Quark  von  Milch^,  osset.  misin  , Buttermilch', mir.  medg,  cymr.  maidd,  ncorn.  meith,  abret.  meid,  gall.-lat.  *mesga  (frz. megue)  , Molken'  (*misga),  aisl.  mysa  ,Molken'  (*mihswön').
POK_02.txt:6115:ahd.  milchu,  melchan,  ags.  melcan  ^melken'  (st.  V. ;  dagegen  ags.  meolcian^ aisl.  mjolka  Denominative  von  *mp.lick-  , Milch'  s.  unten),  ahd.  chumelktra jMelkkübel'  (vielleicht  dem  lat.  mulctra  nachgebildet),  anord.  mjaltr  , milch- gebend' (*melJcta-)]  mit  Tiefstufe  ags.  molcen,  mhd.  molchen,  molken  , dicke Milch',  nhd.  Molken,  und  aisl.  schw.  V.  molka  , melken',  mylkja  , säugen' ;
--- CHEUNG huar page ---
*huar' ‘to consume, eat’ 

*AVESTAN: ҮАУ. x’ar- ‘to consume, eat’ || (+ *fra-) ‘to consume, eat’ = Liste: 18 
Pres. them.: IND. 3sg. YAv. x'araiti, 3р1. YAv. x'aronti, med. 3р1. YAv. x'aronte (Y 9.16), SUBJ. 3sg. 
Y Av. x‘arat, OPT. YAv. ? x'arois (P 28), 3sg. YAv. x‘ardit (N 45), YAv. fra.gharöit (N 71), IMPV. 3sg. 
Y Av. x'aratu (У 3.19), 2pl. YAv. x‘arata, 3pl. Y Av. frax'arontu (Yt 5.92, Yt 5.93); Partic.: pres. x'arant-; 
Pass.: pres. IND. 35р. YAv. x'airiieite (V 2.26, V 2.34); Caus.: pres. INJ. 3sg. YAv. fran‘haraiiat (A 3.4) 


*MIDDLE PERSIAN: MMP xwr-, BMP hwl- /xwar-/ (‘STHN-) ‘to drink, eat, enjoy 


(food), consume’ = DMMPP: 368b f. 
Widely attested: Pres.: IND. 35р. MMP xwryd, MMP xwryyd, 1р1. MMP xwr'm, BMP hwlym /xwarém/, 
etc. 


*PARTHIAN: wxr- ‘to eat’ || (+ *4-) "xwr- ‘to eat, consume, devour (of fire)’ 
= Ghilain: 57 | DMMPP: 349a, 79b 

Pres.: SUBJ. 15р. wxr’n, 3sg. wxr’h; Partic.: perf. pass. wxrd; Inf.: wxrd, wxrdn || (+ *a-) Pres.: IND. 35р. 
"xwryd, ’xwrynd
```


## [2026-09-06T21:42:57.675Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"'Speise\" BRT.txt | head -6",
 "description": "Bartholomae xvarəθa Speise"
}
```


### [2026-09-06T21:42:57.734Z] TOOL RESULT

```
16360:•  j.  pitav-  m.  'Speise',  insbes.  feste,  'Fleisch- speise': yim  (näml.  azim)  upairi  kirssaspB .  .  °täm  pacata  ".  .  sich  (Reise h) speise kochte"  Y.().  11;  —  'tum  F.  jo,  *N.ö'7'J;
```


## [2026-09-06T21:43:06.903Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c \"klein'\" BRT.txt; grep -n \"kasu\\|'klein'\" BRT.txt | head -5; echo \"=== BRT leaf w/ xsudra headword ===\"; grep -n \"j\\.  xsudra\\|xsudra-  n\\.\" BRT.txt | head -5",
 "description": "Check BRT for klein and xsudra headword"
}
```


### [2026-09-06T21:43:06.987Z] TOOL RESULT

```
2
2768:mit  paiti  i)  'streben  nach  — ,  begeh- ren': a)  mit  Akk,:  tafca  yä  kasu.xratul ,  masyöjcrdkwqm  (sd.)  nöit  paitiSaiti  V.  7, I  59.  b)  mit  Gen.:  s.  AbsoL  a)  'sich befleissigen,  betätigen',  mit  Akk.'>:  paiti- sata  (2P.)  mazdayasna  sraoiahe  a/yeke '  yasmm  Y.  37. 13;  —  staota  yesnya  yaza- maide  .  .  dadräna  paitHäna  paitiima- .  r^mna  Y.  55. 6 ;  —  six/anlfm  sa/ayaitt^m paitisant^m  Vyt52,  *P- /?  (wo  °Ä«- ,ljm)'i^.  3)  'erfahren,  erleben':  iaia lUli  (sd.)  *paitUäma  '*>  frya  paiti  tanvi ,  Yt.  i7, 10.  a)  bes. 'zur  Vergeltung,  zum Dank  erfahren,  empfangen':  kä>:ä..kä%3 .  (sd.)  saidyäi  yS  I  paitisift  Y.44.2 ; — ya^a ahmya  amtsa  spmta  sraoläoa  aiyäoa paitisqn  . .  yasnqsca  vahmqsca  Y.  öb.6.
2783:xaA/rä  (frö)  i) 'forteilen,  entweichen': ,  Y.  43. 7;  —  kyat  '^wH  xsayqs  {^A^  °hm s.  Ini./rasstö.  2)  'zum  Forteilen,  Weichen  \dy,il  imavanitm  "weil,  wer  es  vermag, bringen":  tia^a  eil  raSva  masya  /«/«/'  deinen  des  mächtigen  Wunsch  erfüllen nasoa  fraeiyeiti  "kein  .  .  vermag  (ihn)  zu  möchte"  Y.4j.  ro";  ■ —  "Ü!  *kasu.draonö töten  noch  zum  Weichen  zu  bringen"  Vt.  (sd.)  jn^a  a^rava  V.J.  45. t4Z^-       3) 'impellere,  anspornen,  dringen      KompE.  —  Zum  V.  a-j-;  aus  ar.  »iwi/a- ;  vgl.
5283:•  j.  'ara-  m.  EN.  eines  Gläubigen:  hr^- ziihao^  "rahe .  .  kasupitJus  "rake  "des  B. (AT.),  Sohns  des  A"  Yt.  13.110.
6505:•  j.  as.dSnav-  Adj.  'mit  starken,  grossen  •  P-  aSna-  m.  'Marschiren',  mit  astty  'er (Samen-)Körnem':  us  apam  aoavS  .  .  befindet  sich  auf  dem  Marsch  nach  — ' jasänti  -nunqmca  yavanq'm  kasuJätm-  («^V  »"'*  Akk.):  *adaiiy  adam  ^naiy^^ natnca  västra'nam  "die  wässerbäche  wer-  •'^'"»  "^'y  ''uv'^jam  pasäv<^  kacämi/' den.,  hervorbrechen  hin  zum  Getreide  atars<^^y^  uz-aßyä  "damals  war  ich mit  den  grossen  und  zum  Gras  mit  den  ^  d^™  Marsch  nach  Susa;  drauf  bc- kleinen  Körnern"  YtÄig".  kamen  die  Suser  Furcht  vor  mir"  Bh.2.4.
9393:V..?.24;  —  zqm  'yqm  "^radyam  V. 14.13.  ,  j.  kasu.xratav-  Adj.  'der  geringe  Ein- PFP.  iura  V.  ik<ir!.  —  Pü.  (lu  V.  j):  kilürr,  sjcht besitzt' :  /<^^^a  vJ  'tus  masyöj(rtt'i>wam (zu  V.  I4\:  undeutlich.  ,    ,  ,  ....  .,-.  ,-  ■'  •
=== BRT leaf w/ xsudra headword ===
```


## [2026-09-06T21:43:13.297Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg282.png data/verification/sources/refs/ocr/BOOK/282.png && ls -la data/verification/sources/refs/ocr/BOOK/282.png",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-06T21:43:13.359Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 70575 Sep  6 17:43 data/verification/sources/refs/ocr/BOOK/282.png
```


## [2026-09-06T21:43:15.753Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,80p' tools/verify_check.py",
 "description": "Read verify_check requirements"
}
```


### [2026-09-06T21:43:15.791Z] TOOL RESULT

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
```


## [2026-09-06T21:43:18.671Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '80,140p' tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-06T21:43:18.712Z] TOOL RESULT

```
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


## [2026-09-06T21:43:31.415Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== Sanskrit ksira ===\"; grep -n -i \"Proto-Indo-Iranian\\|milk\\|kṣīrá\\|Etymology\" 5e019b6ec2053877.txt | head -12; echo \"=== xordan ===\"; grep -n -i \"Proto-Iranian\\|xwardan\\|to eat\" f2a175c6a18dacab.txt | head -8",
 "description": "Verify Sanskrit and xordan pages"
}
```


### [2026-09-06T21:43:31.485Z] TOOL RESULT

```
=== Sanskrit ksira ===
62: Etymology 
85: Etymology 
179: Etymology
194: milk 
283: Etymology
286: Etymology tree
288: Proto-Indo-Iranian *kšiHrám 
292: Inherited from Proto-Indo-Aryan *kṣiHrám , from Proto-Indo-Iranian *kšiHrám ( “ milk ” ) . Cognate with Avestan 𐬑𐬱𐬎𐬎𐬌𐬛- ( xšuuid- ) , Northern Kurdish şîr , Persian شیر ( šir ) , Zazaki şıd , şıt . Originally thought to be from Proto-Indo-European *swēyd- ( “ milk ” ) , but Lubotsky claims a borrowing from the BMAC substrate .
304: क्षी॒र • ( kṣīrá ) stem ,  n 
306: milk , thickened milk
311:Sarasvatī draws forth for him water and butter, milk and meath. 
315: the milky juice or sap of plants 
=== xordan ===
169: Inherited from Middle Persian [Book Pahlavi needed] ( OŠTEN-tn' /⁠xwardan⁠/ ) , 𐫑𐫇𐫡𐫅𐫗 ( k̇wrdn /⁠xwardan⁠/ ) , from Proto-Iranian *hwar- ( “ to eat, consume ” ) , from Proto-Indo-Iranian *suar- , [ 1 ] further origin unknown, with no obvious Indo-European cognates outside of Iranian. 
171: Cognates include Northern Kurdish xwarin ( “ to eat ” ) , Northern Luri هںرده ( hərde , “ to eat ” ) , Pashto خوړل ( xwaṛə́l , “ to eat ” ) , Avestan 𐬓𐬀𐬭𐬀𐬌𐬙𐬌 ( xᵛara i ti , “ to consume, eat ” ) .
173: Original meaning of the root was "to take". During the Proto-Iranian period it replaced the native Indo-European root for "to eat" *h₁ed- , perhaps originally being used in a more informal way. The other root has been preserved in several nominal formations, such as Proto-Iranian *HacwaHastiš ( “ alfalfa ” ) and Ossetian ад ( ad , “ taste ” ) ^ citation needed .
197: xwardan
216: خوردن • ( xwardan  / xordan ) ( present stem خور ( xwar  / xor ) , Tajik spelling хӯрдан ) 
218: ( transitive ) to eat 
673: Persian terms inherited from Proto-Iranian 
674: Persian terms derived from Proto-Iranian
```


## [2026-09-06T21:50:59.150Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk282.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 282,\n \"book_page\": 252,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ksîro\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Proto-Indo-Iranian *kšiHrám 'milk' (Walde-Pokorny I 503 *ksīro- 'Milch, Molken'); Proto-Iranian *xšiHrám\",\n   \"note\": \"The headword is copied verbatim from the reference Nourai cites: Walde-Pokorny I 503 has an entry 'ksīro- „Milch, Molken“' whose whole evidence is 'Ai. kṣīra- n. „Milch“; alb. hirë „Molken“'. So the root name and the gloss 'milk' are correct as a citation. What is overstated is the language label 'Indo-European': the etymon has no witness outside Indo-Iranian except the doubtful Albanian word, Pokorny 1959 dropped the entry altogether (no *ksīro- in IEW), and Watkins/AHD s.v. melg- states flatly that 'no common Indo-European noun for milk can be reconstructed'. Wiktionary's Proto-Indo-Iranian *kšiHrám says 'Unknown; possibly cognate with Albanian hirrë „whey“, perhaps both borrowed from an Asiatic substrate language' (Lubotsky 1999, 'The Indo-Iranian substratum' — the BMAC hypothesis). The correct label is therefore Proto-Indo-Iranian (probably a substrate loan), not Indo-European. Nothing in the chart's tree is affected below the Indo-Iranian level.\",\n   \"note_fa\": \"سرواژهٔ «Ksîro» دقیقاً از همان مأخذی گرفته شده که نورایی به آن ارجاع می‌دهد: والده–پوکورنی جلد ۱ ص ۵۰۳ مدخلی دارد با عنوان ksīro- «شیر، آبِ پنیر» که تمام گواه آن سنسکریت kṣīrá- و آلبانیایی hirrë است. پس نام ریشه و معنای «شیر» درست نقل شده، اما برچسب «هندواروپایی» بیش از اندازه است: این واژه بیرون از شاخهٔ هندوایرانی هیچ گواه مطمئنی ندارد، پوکورنی در ویراست ۱۹۵۹ این مدخل را یکسره حذف کرده، و واتکینز (AHD) صریح می‌گوید هیچ نام مشترک هندواروپایی برای «شیر» بازسازی‌شدنی نیست. لوبوتسکی (۱۹۹۹) و ویکی‌واژه آن را هندوایرانی آغازین *kšiHrám و به احتمال زیاد وام‌واژه‌ای از زیرلایهٔ آسیای میانه (BMAC) می‌دانند. بنابراین ادعای نورایی با احتیاط پذیرفتنی است، به شرط آنکه «هندواروپایی» را به «هندوایرانی آغازین» تصحیح کنیم.\",\n   \"sources\": [W+\"Reconstruction:Proto-Indo-Iranian/k%C5%A1iHr%C3%A1m\", W+\"%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%80%E0%A4%B0\"],\n   \"ref_check\": [\n    {\"ref\": \"WLD1:503\", \"status\": \"supports\", \"note\": \"Walde-Pokorny Bd. I p. 503 (WLD_Bd1_pages.txt leaf 512, running head 'kser- — ksuelp- 503'): headword 'kslro- „Hilch, Molken“' (OCR for 'ksīro- „Milch, Molken“'), body: 'Ai. ksJra- n. „Milch“; alb. hire „Molken“. Pedersen IF. 5, 45, KZ. 36, 277.' Exactly Nourai's root name and gloss.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 1959, whole text (grep 'ksiro|ksīro|Molken' in POK_01/02/03)\", \"stance\": \"silent\", \"note\": \"Pokorny 1959 has no *ksīro- entry at all; the only kser-/ksei- material near it is 'kseiro- ... eine Erweiterung von ksā- „brennen, versengen“ ... WP. I 503' (POK_02.txt leaf 285), i.e. the DRY root, not the milk word. Pokorny thus silently dropped WP's *ksīro-.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. melg- (AHD_watkins1985.txt line 739)\", \"stance\": \"partial\", \"note\": \"'Included here to mark the unexplained fact that no common Indo-European noun for milk can be reconstructed'. Watkins has no *ksīro- root; supports the word's existence in Indo-Iranian but denies it PIE status.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann p. 573/574 (IEC.txt leaf 326, line 8190)\", \"stance\": \"supports\", \"note\": \"'ksirom „milk, derivative of milk”. Cf. skir-.' Mann keeps WP's reconstruction, and at leaf 15535 adds 'skeir- (skheir-, skhir-) „product of soured milk“. Cf. skir-, ksirom' with Oss. ciri, Arm. xer, Alb. hirrë.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 5.86 MILK, p. 384/385 (SYN.txt leaf 431)\", \"stance\": \"partial\", \"note\": \"Buck's MILK table gives 'Skt. payas-, ksira- / Av. payah-, xšvid-' — he records the Indo-Iranian words but sets up no common IE etymon for 'milk'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"xšîra, xšvipata; apa-xšîra\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Three things are packed into one box. (a) A bare Avestan xšīra- 'milk' is NOT attested; Bartholomae's Altiranisches Wörterbuch has no such headword. (b) apa-xšīra- is real but comes with a query mark: it is Horn's entry no. 802 (Grundriss p. 178) 'šīr „Milch“ ... aw. apa-xšīra- (?); ai. kṣīrá- „Milch“; phlv. šīr', a hapax that Horn himself flags, and Mo'in repeats it with the same query in his Borhan footnote ('اوستا (؟) apa-xshira'). Nourai simply copies Horn/Mo'in, so the citation is faithful even though the Avestan form is insecure. (c) 'xšvipata' is Nourai's spelling of Av. xšvipta- 'milk', which IS attested (adj. xšviptavaitī- 'having milk', V. 21.7), beside the primary noun xšvīd- m. 'Milch' (AiW, BRT.txt leaf 333, cols. c.561–567: 'xšvid- m. „Milch“; im Gegensatz zu āzūtay- ... „flüssige Nahrung“'). Bartholomae analyses xšvipta- as the past participle of xšvip- 'to shoot/squirt out', i.e. 'that which has been squirted out = milked'. Whether that word belongs with kṣīra- is disputed: Walde-Pokorny I 502 says expressly that 'av. xšvīd- „Milch“ zu lit. sviestas „Butter“' and does NOT belong with *ksīro-, whereas Wiktionary s.v. Sanskrit क्षीर lists 'Avestan 𐬑𐬱𐬎𐬎𐬌𐬛- (xšuuid-)' as a cognate of kṣīrá-. Nourai therefore follows the connecting view; the two Avestan words are not a single lemma, and 'xšīra' alone should be deleted.\",\n     \"derivation_fa\": \"در این جعبه سه چیز با هم آمده است. نخست: در اوستایی صورت مستقل xšīra- «شیر» گواه ندارد و بارتولومه چنین سرواژه‌ای ندارد. دوم: apa-xšīra- واقعی است اما با علامت پرسش؛ این همان مدخل شمارهٔ ۸۰۲ هرن (ص ۱۷۸) است: «šīr، اوستایی apa-xšīra- (؟)، سنسکریت kṣīrá-، پهلوی šīr»، و معین نیز در حاشیهٔ برهان قاطع همان را با همان علامت پرسش آورده («اوستا (؟) apa-xshira»). پس نقل نورایی امانت‌دارانه است هرچند خودِ صورت اوستایی مطمئن نیست. سوم: «xšvipata» همان xšvipta- اوستایی است که واقعاً به معنی «شیر» گواهی شده (صفت xšviptavaitī- در وندیداد ۲۱٫۷) در کنار نام اصلی xšvīd- «شیر». بارتولومه xšvipta- را اسم مفعول ستاک xšvip- «بیرون جهیدن، فوران کردن» می‌داند، یعنی «دوشیده‌شده». پیوند این واژه با kṣīra- محل اختلاف است: والده–پوکورنی (۱: ۵۰۲) صریحاً آن را با لیتوانیایی sviestas «کره» می‌سنجد و از *ksīro- جدا می‌کند، اما ویکی‌واژه آن را هم‌ریشهٔ kṣīrá- می‌شمارد. نورایی از دیدگاه دوم پیروی کرده است؛ با این حال دو واژهٔ اوستایی یک سرواژه نیستند و «xšīra» تنها باید حذف شود.\",\n     \"sources\": [W+\"%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%80%E0%A4%B0\", W+\"Reconstruction:Proto-Iranian/x%C5%A1iHr%C3%A1m\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1175\", \"status\": \"partial\", \"note\": \"Nourai's AHD page numbers 1505-1550 are the IE appendix; 1175 is an ordinary dictionary page of the 1976 New College edition (not open online), evidently the page carrying 'seersucker'. The local Watkins 1985 IE-roots text has no root of this shape and states s.v. melg- that no common IE noun for milk can be reconstructed — so AHD cannot be supporting an Avestan-to-PIE link here.\"},\n      {\"ref\": \"HRN:178\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p. 178 (HRN.txt line 7000-7003, leaf 199 = printed 178), entry '802. šīr „Milch“ ... vergl. ham-šīre. aw. apa-xšīra- (?); ai. kṣīrá- „Milch“; phlv. šīr; kurd. ... oss. d. äxšir'. This is the exact source of Nourai's 'apa-xšîra'.\"},\n      {\"ref\": \"SOD:29\", \"status\": \"supports\", \"note\": \"Gharib p. 29 (SOD_pages.txt leaf 93, page numeral '29' printed in the block): entries '746 ... milk' and '747 ʾγsyptk B, S (o)xsiβde (ʾγsyβty) © Yaghn. xsift-, Khwar. xwβcy ⇒ xsyβt | milky, milk'. Confirms a Sogdian/East-Iranian xšīβt-, not an Avestan xšīra-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae AiW cols. c.561-567 (BRT.txt leaf 333, line 10985); also leaf 465 line 14800\", \"stance\": \"partial\", \"note\": \"'j., g. xšvid- m. „Milch“; im Gegensatz zu āzūtay- (sd.) überhaupt „flüssige Nahrung“ im Gegensatz zu fester' (V.13.28, Y.29.7); footnote: 'xšvipta- eig. das „herausgeschnellte“, d.i. „gemolkene“, PPfP.'; and 'paēma.vant- ... °vaitī xšviptavaitī (VSf.) V. 21.7'. So xšvipta- exists and means 'milk', but as a participle of xšvip-; there is no headword xšīra- anywhere in AiW.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 502 (WLD_Bd1_pages.txt leaf 511)\", \"stance\": \"contradicts\", \"note\": \"'(aber kṣīra- „Milch“ nicht mit ks- aus ksu- in denselben Kreis, s. *ksīro-; und av. xšvīd- „Milch“ zu lit. sviestas „Butter“, dessen Anlaut trotz Ch. nicht wohl aus ksv- herleitbar ist)'. Nourai's own root reference explicitly separates the Avestan word from *ksīro-.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 5.86 MILK, p. 384/385 (SYN.txt leaf 431)\", \"stance\": \"partial\", \"note\": \"Buck's Avestan entry for 'milk' is 'xšvid-', never xšīra-.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"šîr 1 «شیر ۱ ( شیرین ، شیرینی )»; šîr-o-šekar «شیروشکر»; ham-šîreh «همشیره»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP شیر šīr 'milk' continues Middle Persian šīr, written with the Aramaic heterogram HLBA (from Aram. ḥlb 'milk') and phonetically šyl / Manichaean šyyr (MacKenzie, Concise Pahlavi Dictionary p. 78 and 585: 'šīr [HLBA < A hlbʾ; šl | M šyyr, N ~] milk'), from Proto-Iranian *xšiHrám; the Old Iranian cluster xš- was simplified to š- in Middle Persian (cf. Oss. æxsyr, which keeps it), and the Middle Persian long ī was preserved, giving Classical NP šīr, modern Tehrani šir. It is homophonous with, but etymologically distinct from, شیر šēr 'lion' (MP šagr) — hence Nourai's 'šîr 1'. The chart's parenthesis (شیرین، شیرینی) is right: شیرین 'sweet' is MP šīrēn, a -ēn derivative of the same šīr (PHD p. 585 'šīrēn [šlynʾ | M syryn, N ~in] sweet'). شیروشکر šīr-o-šekar 'milk and sugar' is a compound with Arabic-mediated šakar (< MP šakar < Skt. śarkarā); Dehkhoda/Mo'in gloss it 'شیر مخلوط با شکر (فرهنگ فارسی معین)' and record the technical textile sense 'قصب شیر و شکر؛ نوعی پارچه' — a two-tone (white/yellow) striped cloth, precisely Nourai's 'a kind of silk fabric'. همشیره ham-šīreh 'sister' is ham- 'same, co-' + šīr 'milk' + -a, i.e. 'sharing one milk, foster-sibling'; Mo'in's dictionary has 'هم‌شیر: دو یا چند کودک که از یک پستان شیر خورده‌اند، برادر یا خواهر رضاعی' and 'همشیره: خواهر (خواه با شخص از یک مادر باشد و خواه رضاعی)', which is the semantic path 'milk-sibling' > 'sister'. Strictly the Persian word descends from Proto-Iranian *xšiHrám via Middle Persian, not from the Avestan word drawn as its parent — the usual convention of this book.\",\n     \"derivation_fa\": \"«شیر» فارسی نو دنبالهٔ فارسی میانهٔ šīr است که در پهلوی کتابی با هزوارش آرامی HLBA و آوانگاری šyl و در مانوی šyyr نوشته می‌شود (مکنزی، فرهنگ کوچک پهلوی، ص ۵۸۵)، و آن از ایرانی باستان *xšiHrám است؛ خوشهٔ آغازین xš- ایرانی باستان در فارسی میانه ساده و به š- بدل شده (در آسی هنوز به‌صورت æxsyr مانده است) و ای کشیده محفوظ مانده. این واژه با «شیر» به معنی «اسد» (فارسی میانه šagr) هم‌آواست ولی هم‌ریشه نیست؛ ازین‌رو نورایی «šîr ۱» نوشته است. پرانتز چارت هم درست است: «شیرین» همان šīrēn پهلوی، مشتق پسوندی از همین šīr است. «شیروشکر» ترکیب عطفی «شیر + شکر» است و دهخدا به نقل از فرهنگ معین آن را «شیر مخلوط با شکر» و نیز «قصب شیر و شکر: نوعی پارچه» ثبت کرده، که همان معنای پارچهٔ راه‌راه دورنگ در چارت است. «همشیره» از هم + شیر + ـه ساخته شده، یعنی «کسی که با دیگری از یک شیر خورده، خواهر رضاعی»، و معین می‌نویسد: «هم‌شیر: دو یا چند کودک که از یک پستان شیر خورده‌اند» و «همشیره: خواهر (خواه از یک مادر و خواه رضاعی)». تحول معنایی «هم‌شیر» ← «خواهر» روشن است. ادعای نورایی درست است؛ تنها نکتهٔ فنی آنکه شیر فارسی مستقیماً از اوستایی نیامده بلکه از ایرانی باستان از راه فارسی میانه رسیده است.\",\n     \"sources\": [W+\"%D8%B4%DB%8C%D8%B1\", W+\"%D9%87%D9%85%D8%B4%DB%8C%D8%B1%D9%87\", W+\"Reconstruction:Proto-Iranian/x%C5%A1iHr%C3%A1m\", \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D8%B1%D9%88%D8%B4%DA%A9%D8%B1/\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1322\", \"status\": \"supports\", \"note\": \"Borhan-e Qateʽ vol. 3, pdf page 113 (= printed c.1322; BQT_v3_pages.txt block '[pdf page 113]'), the شیر page. Mo'in's footnote 1 reads: '۱ - اوستا (؟) apa-xshira ، باستان kshira ( شیر ) ... ارمنی hamshirak ، کردی و بلوچی shir ، اسِتی axshir ... منجی xshir' — the same chain Nourai draws, including the Armenian loan hamshirak matching همشیره.\"},\n      {\"ref\": \"HRN:178\", \"status\": \"supports\", \"note\": \"Horn no. 802, p. 178: 'šīr „Milch“, šīre ... vergl. ham-šīre. aw. apa-xšīra- (?); ai. kṣīrá-; phlv. šīr; ... oss. d. äxšir' — Horn himself derives ham-šīre from šīr.\"},\n      {\"ref\": \"SYN:385\", \"status\": \"supports\", \"note\": \"Buck 5.86 MILK (SYN.txt leaf 431/432, printed 384-385) lists the Indo-Iranian words 'Skt. payas-, ksira-' / 'Av. payah-, xšvid-' as the 'milk' etyma of the family.\"},\n      {\"ref\": \"MON:2108,5187\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Farsi is online only without page numbers (vajehyab/abadis), so pp. 2108 and 5187 cannot be verified as pages; the CONTENT is confirmed from the 2-vol Adena reprint (see consulted, MON).\"},\n      {\"ref\": \"ETM:69\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374 — no copy online or on disk (refs_online.json: kind 'catalog', local_file null).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 78 and p. 585 (PHD.txt lines 583-585)\", \"stance\": \"supports\", \"note\": \"'šīr [HLBA < A hlbʾ; šl | M šyyr, N ~] milk. šīrēn [šlynʾ | M syryn, N ~in] sweet. ~ih: sweetness.' Also 'māst [mʾastʾ | N ~] curds, sour milk' and the index 'milk (n.) jiw, pēm, šīr'. The MP link NP šīr < MP šīr is direct.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi, 2-vol Adena reprint vol. 2 s.v. هم‌شیر / همشیره (MON_2vol_Adena_v2_djvu.txt)\", \"stance\": \"supports\", \"note\": \"'هم‌شیر، همشیر (ص.) دو یا چند کودک که از یک پستان شیر خورده‌اند، برادر یا خواهر رضاعی. هم‌شیره، همشیره (ص.ا.) خواهر (خواه با شخص از یک مادر باشد و خواه رضاعی)، اخت.'\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan vol. 3 pdf p.113, footnote 1\", \"stance\": \"supports\", \"note\": \"see ref_check BQT:1322 — quoted there.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss p. 178 no. 802\", \"stance\": \"supports\", \"note\": \"quoted above; Horn explicitly cross-references ham-šīre under šīr.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, searched for شیر / شیرین headwords\", \"stance\": \"silent\", \"note\": \"Aryanpur's Persian OCR on these leaves is too corrupt to isolate a شیر headword (hits at lines 1363, 7285 are cross-references only: '۴-گفته شده است که واژه‌ی فارسی «شیرین» از واژه‌ی فارسی «شیر» درست شده است'); no usable etymological statement recovered.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Hindustani\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box: the Persian compound šīr-o-šakar was carried into Hindustani (Hindi-Urdu) as sīrsakar / śīrśakar, the name of the puckered striped cloth, during the Mughal period, and it is from that Hindustani form, not directly from Persian, that the English word was taken by the East India trade. Klein (p. 1410-1411, s.v.) writes 'seersucker, n., a kind of cotton fabric. — Hind. sirsakar, fr. Pers. shir-o-shakar, lit. „milk and sugar“'; Etymonline dates the English borrowing to 1722 'from Hindi sirsakar, said to be an East Indian corruption of Persian shir o shakkar'. The Persian → Hindustani → English route drawn here is therefore exactly the standard one.\",\n     \"derivation_fa\": \"این جعبه خالی است و تنها حلقهٔ واسط را نشان می‌دهد: ترکیب فارسی «شیروشکر» در دورهٔ گورکانیان به هندی–اردو راه یافت و آنجا sīrsakar / śīrśakar تلفظ شد و نام همان پارچهٔ راه‌راهِ چین‌دار گردید؛ انگلیسی این واژه را نه مستقیم از فارسی بلکه از همین صورت هندوستانی و از راه بازرگانی کمپانی هند شرقی گرفت. کلاین (ص ۱۴۱۰–۱۴۱۱) می‌نویسد: «seersucker از هندی sirsakar، از فارسی shir-o-shakar، تحت‌اللفظ „شیر و شکر“»، و اتیمانلاین ورود آن به انگلیسی را سال ۱۷۲۲ می‌داند. پس مسیر فارسی ← هندوستانی ← انگلیسی که نورایی کشیده، همان مسیر پذیرفتهٔ همگانی است.\",\n     \"sources\": [\"https://www.etymonline.com/word/seersucker\"],\n     \"ref_check\": [\n      {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The node carries no refs= in the book (empty Hindustani pass-through box, confirmed on the printed page, pdf 282). Checked instead the references of the child English node, which name the Hindustani form.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 pp. 1410-1411 s.v. seersucker (KLN_1966.txt leaf 749, line 34437)\", \"stance\": \"supports\", \"note\": \"'seersucker, n., a kind of cotton fabric. — Hind. sirsakar, fr. Pers. shir-o-shakar, lit. „milk and sugar“. Pers. shir is rel. to OI. ksirdm, Ossetic dhshir, „milk“. Pers. shakar is rel. to Pali sakkhara, OI. sarkard ...'\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson and Whitworth, Anglo-Indian Dictionary (grep 'seersuck|sirsakar')\", \"stance\": \"silent\", \"note\": \"Neither HJB.txt nor AID.txt has an entry for the word (they do have seerband, seerpaw); so no Anglo-Indian corroboration of the Hindustani form from those two.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"seersucker\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English seersucker, first recorded 1722, is a straightforward East-India-trade borrowing of Hindustani sirsakar, itself Persian šīr-o-šakar 'milk and sugar'. The name is a metaphor for the fabric's alternating bands: the smooth (glossy) stripe is the 'milk', the crinkled/puckered stripe the 'sugar' — Etymonline: 'a reference to the alternately smooth and puckered surfaces of the stripes'. The English spelling shows the usual 18th-c. Anglo-Indian rendering of Indic ī by <ee> (cf. seerband, seerpaw) and a folk-etymological reshaping of -sakar to -sucker. Nourai's gloss 'a cotton fabric with a striped pattern' is exactly right for the English word (the Persian source term, by contrast, denotes a silk/qasab cloth).\",\n     \"derivation_fa\": \"واژهٔ انگلیسی seersucker که نخستین‌بار در ۱۷۲۲ ثبت شده، وام‌واژه‌ای از هندوستانی sirsakar و در نهایت از فارسی «شیروشکر» است. این نام استعاره‌ای است از نوارهای متناوب پارچه: نوار صاف و براق «شیر» و نوار چین‌خورده و زبر «شکر». املای انگلیسی نمایانگر شیوهٔ رایج آنگلو–هندی برای نشان‌دادن ای کشیدهٔ هندی با ee است (مانند seerband و seerpaw) و بخش دوم به‌سبب ریشه‌شناسی عامیانه به sucker بدل شده است. معنایی که نورایی داده («پارچهٔ نخیِ راه‌راه») برای واژهٔ انگلیسی کاملاً درست است، هرچند اصل فارسی آن پارچه‌ای ابریشمی/قصب بوده. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/seersucker\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1411\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 1410-1411 (KLN_1966.txt leaf 749, page numeral 1410 visible on the leaf): 'seersucker, n., a kind of cotton fabric. — Hind. sirsakar, fr. Pers. shir-o-shakar, lit. „milk and sugar“.' Nourai's page number is exact.\"},\n      {\"ref\": \"AHD:1175\", \"status\": \"not_checked\", \"note\": \"The 1976 AHD New College edition is not open online; p. 1175 falls in the 'se-' range of the main dictionary, so it is plausibly the 'seersucker' page, but it could not be inspected. The online AHD/Watkins IE-roots appendix (the local 1985 text) contains no root for this word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 pp. 1410-1411\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (grep 'seersucker')\", \"stance\": \"silent\", \"note\": \"no entry.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, vols 1-4 (grep 'seersucker')\", \"stance\": \"silent\", \"note\": \"no hit in the OCR of FSD_vol1-4.txt; likewise none in WEB_vol1.txt.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Sogdian\",\n     \"words\": \"`xšy`bt\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Sogdian word is real and Nourai's transliteration reproduces Gharib's headword: SOD entry 2084 'ʾxšʾypt-, S | (o)xšipδ | milk | (ʾxšyβt-) © Av. xšvipta | γšyβt, xšypt' (p. 81/82), with the Buddhist/Christian by-forms at entries 746-747 on p. 29, 'ʾγšyβtk ... (o)xšiβde © Yaghn. xšift-, Khwar. xwβcy | milky, milk'. Phonetically Sogd. ʾxšyβt / xšypδ continues Old Iranian *xšwipta- with the regular Sogdian spirantisation of intervocalic -p- to -β- and the prothetic ʾ- before the initial cluster; Yaghnobi xšift and Khwarezmian xwβcy continue the same word. The caveat is that this is the xšvipta- family, NOT *xšiHra-: Gharib herself equates it with Avestan xšvipta-, and Wiktionary's Reconstruction:Proto-Iranian/xšiHrám lists as descendants only Middle Persian šīr, Ossetian æxsir/æxsyr and (with a query) Khotanese tcīratsa — no Sogdian form. Whether the box belongs under this root therefore depends on the same disputed equation kṣīra- ~ xšvīd-/xšvipta- discussed at node 1; on WP I 502's view it does not, on Wiktionary's it does.\",\n     \"derivation_fa\": \"این واژهٔ سغدی واقعی است و آوانگاری نورایی همان سرواژهٔ قریب است: مدخل ۲۰۸۴ فرهنگ سغدی «ʾxšʾypt- / xšipδ «شیر»، مقایسه شود با اوستایی xšvipta» (ص ۸۱–۸۲) و صورت‌های دیگر در مدخل‌های ۷۴۶–۷۴۷ در ص ۲۹ («ʾγšyβtk، یغنابی xšift، خوارزمی xwβcy»). از نظر آوایی سغدی ʾxšyβt دنبالهٔ ایرانی باستان *xšwipta- است: پ میان‌واکه‌ای به β سایشی بدل شده و پیش از خوشهٔ آغازین همزهٔ افزوده (پروتز) آمده است. اما نکتهٔ مهم آن است که این واژه به خانوادهٔ xšvipta- تعلق دارد نه به *xšiHra-؛ خودِ قریب آن را با اوستایی xšvipta می‌سنجد و ویکی‌واژه در مدخل ایرانی آغازین *xšiHrám هیچ بازماندهٔ سغدی نیاورده و تنها فارسی میانهٔ šīr، آسی æxsyr و (با تردید) ختنی tcīratsa را برشمرده است. پس جای این جعبه زیر این ریشه به همان اختلاف نظر بند ۱ بازمی‌گردد: به رأی والده–پوکورنی نه، به رأی ویکی‌واژه آری. با احتیاط پذیرفتنی است.\",\n     \"sources\": [W+\"Reconstruction:Proto-Iranian/x%C5%A1iHr%C3%A1m\", W+\"%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%80%E0%A4%B0\"],\n     \"ref_check\": [\n      {\"ref\": \"SOD:29\", \"status\": \"supports\", \"note\": \"Gharib p. 29 (SOD_pages.txt leaf 93, the numeral '29' printed in the block): '746 ... milk' and '747 ʾγsyptk B, S | (o)xsiβde (ʾγsyβty) © Yaghn. xsift-, Khwar. xwβcy ⇒ xsyβt | milky, milk | BSTBL, Vim. 25; VJ 6ᵃ, 1029; BBB p101 c18'.\"},\n      {\"ref\": \"SOD:82\", \"status\": \"supports\", \"note\": \"Gharib entry 2084 (SOD_pages.txt leaf 147; leaf 145 = printed 79, leaf 146 = 80, so this is printed 81/82 — Nourai's 82 is right to within the leaf): '2084 ʾxsʾypt-, S | oxsipd | milk (ʾxsyβt-) © Av. xsvipta | γsyβt, xsypt | KG 504, -y, 505; MSP a5'. This is Nourai's `xšy`bt.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib pp. 29 and 81/82, entries 746-747 and 2084\", \"stance\": \"partial\", \"note\": \"supports the Sogdian form and its meaning, but ties it to Av. xšvipta rather than to *ksīro-.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 502 (leaf 511)\", \"stance\": \"contradicts\", \"note\": \"'av. xšvīd- „Milch“ zu lit. sviestas „Butter“' — the xšvipta-/xšvīd- family is put outside *ksīro-.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p. 573/574 s.v. ksirom (IEC.txt leaf 326)\", \"stance\": \"silent\", \"note\": \"'ksirom „milk, derivative of milk“. Cf. skir-.' — Mann cites no Sogdian reflex.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"kšîra\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sanskrit क्षीर kṣīrá- n. 'milk, thickened milk; the milky juice or sap of plants' is attested from the Rigveda on and is the single strongest witness of the etymon: it is the very word on which Walde-Pokorny's *ksīro- is built ('Ai. kṣīra- n. „Milch“', WP I 503) and the source of the Indo-Iranian reconstruction *kšiHrám. Nourai's transliteration 'kšîra' with š for the retroflex ṣ of kṣ- is his usual convention and is not an error. Wiktionary derives it 'from Proto-Indo-Aryan *kṣiHrám, from Proto-Indo-Iranian *kšiHrám „milk“', naming Avestan xšuuid-, Persian شیر and Kurdish şîr as cognates, and adds that it was 'originally thought to be from Proto-Indo-European *swēyd- „milk“, but Lubotsky claims a borrowing from the BMAC substrate' — which is the only qualification on the arrow: the parent is Indo-Iranian, and probably itself a loan, rather than an inherited Indo-European noun.\",\n     \"derivation_fa\": \"سنسکریت क्षीर (kṣīrá-) خنثی به معنی «شیر، شیر بسته؛ شیرابهٔ گیاهان» از ریگ‌ودا به بعد گواهی شده و مهم‌ترین گواه این ریشه است: همین واژه است که والده–پوکورنی *ksīro- را بر پایهٔ آن ساخته («Ai. kṣīra- n. Milch»، جلد ۱ ص ۵۰۳) و بازسازی هندوایرانی *kšiHrám نیز از آن برمی‌آید. آوانگاری نورایی (kšîra با š به‌جای ṣ در خوشهٔ kṣ) شیوهٔ همیشگی اوست و خطا نیست. ویکی‌واژه آن را از هندوآریایی آغازین *kṣiHrám و هندوایرانی آغازین *kšiHrám می‌داند و اوستایی xšuuid-، فارسی «شیر» و کردی şîr را هم‌ریشهٔ آن می‌شمارد، و می‌افزاید که پیش‌تر آن را از هندواروپایی *swēyd- «شیر» می‌گرفتند اما لوبوتسکی آن را وام‌واژه‌ای از زیرلایهٔ BMAC می‌داند. پس ادعای نورایی درست است، تنها با این قید که «پدرِ» این واژه هندوایرانی است نه هندواروپایی.\",\n     \"sources\": [W+\"%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%80%E0%A4%B0\", W+\"Reconstruction:Proto-Indo-Iranian/k%C5%A1iHr%C3%A1m\"],\n     \"ref_check\": [\n      {\"ref\": \"WLD1:503\", \"status\": \"supports\", \"note\": \"WP I 503 (WLD_Bd1_pages.txt leaf 512): 'kslro- „Hilch, Molken“. Ai. ksJra- n. „Milch“; alb. hire „Molken“' — the Sanskrit word is the headword's chief witness.\"},\n      {\"ref\": \"SYN:385\", \"status\": \"supports\", \"note\": \"Buck 5.86 MILK (SYN.txt leaf 431/432, printed 384-385): 'Skt. payas-, ksira-'; and at 5.88 CHEESE 'Skt. (dadhi-ja-, ksira-ja-)', with the discussion 'Skt. dadhi-ja-, ksira-ja-, lit. „milk-born“, cpds. of dadhi- or ksira- „milk“ (5.86)'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I p. 503\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p. 573/574 (IEC.txt leaf 326)\", \"stance\": \"supports\", \"note\": \"'ksirom „milk, derivative of milk“'; and at leaf 15535 'skeir- ... „product of soured milk“. Cf. skir-, ksirom | Arm. xer ... Alb. hirrë, f. „whey“'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 1959 (grep)\", \"stance\": \"silent\", \"note\": \"no *ksīro- entry; Pokorny dropped WP's lemma.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 5.86, p. 385\", \"stance\": \"supports\", \"note\": \"quoted above.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Ksudros, Qusudros\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *kseud- 'to pound/crush small' (Pokorny 625; Walde-Pokorny I 502), with the o-grade noun *kseud-ro- → Skt. kṣudrá- 'small'\",\n   \"note\": \"Both headwords and the gloss are copied verbatim from Mann, whom Nourai cites: IEC p. 575-576 'ksudros (skudhros) „coarse, granular; coarseness, granules, grit“. Cf. also qusudros, skudhros | Skt. ksudráh „small, fine“ ... Av. xsudrom “seed”; Per. xurd „small“; Arm. xord „sackcloth“', and IEC p. 1060 'qusudros „worn, granular“. Cf. ksudh- ... WP I, 502'. So the root box faithfully reports its source and both variants really are Mann's. The reconstruction itself is sound but the doubled headword is Mann's idiosyncrasy: the standard form of this root is Pokorny p. 625 'kseud- „klein stampfen“. Ai. ksódati „stampft, zermalmt“, ksóda- m. „Stoß, Stampfen, Zermalmen; Mehl, Pulver“, ksudrá- „klein; niedrig, gemein“ ... abg. chudŭ „klein, gering, schlecht“. WP. I 502', with no Iranian member at all. Nourai's gloss 'coarse, granular, crushed in small pieces' is Mann's wording; Pokorny's 'to pound small' is the verbal sense behind it. The real problems are all downstream (nodes 1, 2, 3, 5).\",\n   \"note_fa\": \"هر دو سرواژه و معنایی که نورایی برای ریشه آورده، عیناً از مان (IEC) گرفته شده که خودش به آن ارجاع می‌دهد: ص ۵۷۵–۵۷۶ «ksudros (skudhros) „درشت، دانه‌دانه؛ زبری، خرده، شن“ ... سنسکریت ksudráh „خرد“، اوستایی xsudrom „تخم“، فارسی xurd „خرد“، ارمنی xord „پلاس“» و ص ۱۰۶۰ «qusudros „ساییده، دانه‌دانه“ ... WP I 502». پس جعبهٔ ریشه امانت‌دارانه از مأخذ نقل شده است. خودِ بازسازی درست است اما دوگانه‌بودن سرواژه از ویژگی‌های مان است؛ صورت متعارف این ریشه در پوکورنی ص ۶۲۵ چنین است: «kseud- „خرد کوبیدن“؛ سنسکریت kṣódati „می‌کوبد، خرد می‌کند“، kṣudrá- „خرد، پست“؛ اسلاوی کهن chudŭ „خرد، ناچیز“» — و در آن هیچ عضو ایرانی نیامده است. بنابراین ریشه با احتیاط پذیرفتنی است و اشکال‌های اصلی در گره‌های زیرین (۱، ۲، ۳ و ۵) است.\",\n   \"sources\": [W+\"%D8%AE%D8%B1%D8%AF\"],\n   \"ref_check\": [\n    {\"ref\": \"IEC:576\", \"status\": \"supports\", \"note\": \"Mann, IEC.txt leaf 327 (awk NR=328; the leaf carries the printed numerals 575 and 576), line 8230: 'ksudros (skudhros) „coarse, granular; coarse-ness, granules, grit”. Cf. also qusudros, skudhros | Skt. ksudráh „small, fine“; Prakritic ksulla-, id. cf. Romani čulo, adv. „little“; ... Skt. ksódàmi „pulverize“; Av. xsudrom “seed”; Per. xurd „small“; Arm. xord „sackcloth“'. Nourai's root name and gloss come straight from here.\"},\n    {\"ref\": \"IEC:1060\", \"status\": \"supports\", \"note\": \"Mann, IEC.txt leaf 587 (awk NR=588 carries the printed numeral 1060), line 14377: 'qusudros „worn, granular“. Cf. ksudh- (sic) and qusoudhos. (Phonol. ambig. in some instances). WP I, 502 (Various reflexes in Iran.) Skt. ksudráh, adj. „crushed; small; humble; mean“; Av. xšudrəm, n. “seed”; Per. cf. (from various dialects) xurd „minute, tiny“; sūdan, pp. sūde, v. „rub, wear down“, fr. *ksud- ?; ... Radical in Av. xšud-, v. „pound, crush“'. The second headword of Nourai's root box.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny IEW p. 625 (POK_02.txt leaf 285, lines 4503-4507)\", \"stance\": \"supports\", \"note\": \"'kseud- „klein stampfen“. Ai. ksödati „stampft, zermalmt“, ksöda- m. „Stoß, Stampfen, Zermalmen; Mehl, Pulver, Puder“, ksudrá- „klein; niedrig, gemein“, Komp. ksödiyas-; ... abg. chudŭ „klein, gering, schlecht“ ... WP. I 502.' Supports the root but with an Indic+Slavic distribution only.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 502 (WLD_Bd1_pages.txt leaf 511)\", \"stance\": \"supports\", \"note\": \"'kseud- „klein zermalmt“, ksoda- m. „Stoß, Stampfen, Zermalmen; Mehl, Pulver, Puder“, ... ksudra- „klein, gering; niedrig, gemein“ ... abg. chudŭ „klein; dürftig, gering, schlecht“'. Same lemma, same members.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 IE roots (grep '^kseu')\", \"stance\": \"silent\", \"note\": \"Watkins does not include this root; there is no English reflex to hang it on.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann pp. 575-576 and 1060\", \"stance\": \"supports\", \"note\": \"quoted in ref_check.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"xšudram; xvareta\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Both Avestan words in the box are problematic. (a) Av. xšudra- n. is real and does mean 'seed, semen' in the Vidēvdād (V. 16.11, V. 18.32 'yat mašyō mašīm xšudra aiwi fraŋharəzaiti'; a-fraŋharəza- 'ohne dass Samenerguß erfolgt', AiW), but its basic sense is 'liquid, fluid' and Walde-Pokorny put it under a DIFFERENT root: WP I 502 'qseud- „Flüssigkeit“ (nur arisch). Ai. ksodas- n. „bewegtes Wasser, Flut“ = av. xšaodah- n. „Fluß, Strömung“, xšudra-, xšuδra- „flüssig; n. Flüssigkeit“'. Pokorny p. 625 makes the same split and adds that the identification of Skt. kṣudrá- with Av. xšudra- 'flüssig' is only an attempt: 'Verbindung von ai. ksudrá- mit av. xšudra- „flüssig“ (s. 2. kseud-) versucht Batakrishna Ghosh ... zu begründen'. Mann himself flags the same doubt at IEC 1060 ('Phonol. ambig.'). So Av. xšudra- 'seed' is at best a homonym of the 'crushed/small' word. (b) 'xvareta' (i.e. xᵛarəta-) is not an Avestan word for 'small' at all. Bartholomae's AiW has no adjective xᵛarəta- 'klein'; the Avestan word for 'small' is kasu- (kasu.xřatav-, kasu.draonō-, AiW). xᵛarəta- belongs with xᵛar- 'to consume, eat' (Cheung, EDIV *huar¹ pp. 147-148, YAv. xᵛaraiti) and its nominal xᵛarəθa- 'Speise, Nahrung'; the gloss 'small' is back-projected from New Persian xurd. Mo'in's own footnote in the Borhan (the BQT page Nourai cites) says as much: 'هرن خرد فارسی را از اوستایی xᵛarəta ندانسته' — Horn did NOT derive Persian xurd from Avestan xᵛarəta-.\",\n     \"derivation_fa\": \"هر دو واژهٔ اوستایی این جعبه اشکال دارد. نخست: xšudra- اوستایی واقعی است و در وندیداد (۱۶٫۱۱ و ۱۸٫۳۲) به معنی «نطفه، تخم» به کار رفته، اما معنای پایهٔ آن «مایع، روان» است و والده–پوکورنی آن را زیر ریشهٔ دیگری آورده‌اند: «qseud- „مایع“ (تنها آریایی): سنسکریت kṣodas- „آب روان، سیل“ = اوستایی xšaodah- „رود، جریان“، xšudra- „روان؛ مایع“» (جلد ۱ ص ۵۰۲). پوکورنی (ص ۶۲۵) نیز همین جدایی را می‌پذیرد و می‌افزاید که یکی‌دانستن kṣudrá- سنسکریت با xšudra- اوستایی تنها «کوششی» از سوی باتاکریشنا گوش بوده است. خودِ مان هم در ص ۱۰۶۰ به ابهام آوایی آن اعتراف می‌کند. پس xšudra- «تخم» در بهترین حالت هم‌آواییِ اتفاقی با واژهٔ «خردشده» است. دوم: «xvareta» (یعنی xᵛarəta-) اصلاً در اوستایی به معنی «خرد/کوچک» نیست؛ بارتولومه چنین صفتی ندارد و واژهٔ اوستایی «کوچک» kasu- است. xᵛarəta- به ریشهٔ xᵛar- «خوردن» تعلق دارد (چونگ، *huar¹، ص ۱۴۷–۱۴۸) و اسم آن xᵛarəθa- «خوراک» است؛ معنای «کوچک» از فارسی نو «خرد» به عقب فرافکنده شده است. حاشیهٔ خودِ معین در برهان قاطع (همان صفحه‌ای که نورایی به آن ارجاع داده) می‌گوید: «هرن خرد فارسی را از اوستایی xᵛarəta ندانسته». بنابراین این گره را پژوهش امروزی رد می‌کند.\",\n     \"sources\": [W+\"%D8%AE%D8%B1%D8%AF\", W+\"%D8%AE%D9%88%D8%B1%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:729\", \"status\": \"partial\", \"note\": \"The Borhan page Nourai means is the خُرد entry, BQT_v2_pages.txt leaf 187 (printed c.730, i.e. one page off), which carries the Sa'di verse Nourai quotes ('چند استخوان که هاون دوران روزگار / خردش چنان بکوفت که خاکش غبار کرد') and Mo'in's footnote 4: 'پهلوی xvart ... [رك: خرده] اورامانی xvart ... معرب آن خردة ... هرن خرد فارسی را از اوستایی xᵛarəta ندانسته «اسفا ۱:۲»'. So Borhan is the source of the two forms in the chart, but it reports Horn as REJECTING the Avestan derivation Nourai draws.\"},\n      {\"ref\": \"IEC:576\", \"status\": \"partial\", \"note\": \"Mann p. 576 does write 'Av. xsudrom “seed”' inside the ksudros entry, which is exactly Nourai's word and gloss; but Mann lists no xᵛarəta- at all, and at p. 1060 he concedes the phonology is 'ambig.'\"},\n      {\"ref\": \"IEC:1060\", \"status\": \"partial\", \"note\": \"'qusudros „worn, granular“ ... Av. xšudrəm, n. “seed”; ... Radical in Av. xšud-, v. „pound, crush“.' Again xšudra- yes, xᵛarəta- no.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae AiW, entries a-fraŋharəza-, xšaθri-, hastra- (BRT.txt lines 4043, 10772, 29673); kasu- compounds at lines 2783, 9393\", \"stance\": \"partial\", \"note\": \"'a-fraŋharəza- Adj. „sich nicht ergiessend“; °sat pairi xšudrāt „ohne dass Samenerguss erfolgt“ V.16.11' and 'yat mašyō mašīm xšudra aiwi fraŋharəzaiti V.18.32' — xšudra- 'semen' is confirmed. But AiW has no headword xᵛarəta- 'small'; Avestan 'small/scanty' is kasu- ('kasu.xřatav- Adj. „der geringe Einsicht besitzt“', 'kasu.draonō-').\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 502 (leaf 511)\", \"stance\": \"contradicts\", \"note\": \"'qseud- „Flüssigkeit“ (nur arisch). Ai. ksodas- n. ... = av. xšaodah- n. „Fluß, Strömung, Wasserschwall“, xšudra-, xšuδra- „flüssig; n. Flüssigkeit“, xšusta- (*ksud-ta-) „flüssig, breiig, geschmolzen“' — a separate lemma from kseud- 'klein zermalmt' on the same page.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny p. 625 (POK_02.txt leaf 285 line 4507)\", \"stance\": \"contradicts\", \"note\": \"'Verbindung von ai. ksudrá- mit av. xšudra- „flüssig“ (s. 2. kseud-) versucht Batakrishna Ghosh (Les formations nominales en -ra, S. 21) zu begründen' — i.e. the identification is an unproven proposal, not Pokorny's own analysis.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *huar¹ 'to consume, eat', pp. 147-148 (CHEUNG.txt lines 10284-10334)\", \"stance\": \"partial\", \"note\": \"'*huar¹ „to consume, eat“ | AVESTAN: YAv. xᵛar- „to consume, eat“ ... MIDDLE PERSIAN: MMP xwr-, BMP hwl- /xwar-/' — this, not a word for 'small', is where an Avestan xᵛarəta- would belong.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"kvart\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"There is no Pahlavi word 'kvart'. The Middle Persian adjective is xwurd 'small, little', written ⟨hwltʾ⟩ — MacKenzie, A Concise Pahlavi Dictionary p. 96: 'xwurd [hwltʾ | N ~] small, little. xwurdag [hwltkʾ | N ~a] something small, particle ... ~ih: smallness.' The source Nourai used, Mo'in's footnote to خُرد in the Borhan-e Qateʽ, prints the Latin transliteration 'xvart' (with x for خ); Nourai's 'k' is a misreading of that x. The printed page (pdf 282, book 252) does read 'kvart', so the extraction is faithful and the error is the book's. Substantively the Pahlavi → New Persian step is right: MP xwurd ⟨hwltʾ⟩ > NP خُرد xurd, with the regular loss of the labial glide after x- in the Persian orthography and retention of the short u.\",\n     \"derivation_fa\": \"واژه‌ای به‌صورت «kvart» در پهلوی وجود ندارد. صفت فارسی میانه xwurd «خرد، کوچک» است که به خط پهلوی ⟨hwltʾ⟩ نوشته می‌شود؛ مکنزی در فرهنگ کوچک پهلوی (ص ۹۶) می‌آورد: «xwurd [hwltʾ | فارسی نو همان] small, little» و «xwurdag [hwltkʾ] چیز خرد، ذره». مأخذ نورایی، یعنی حاشیهٔ معین بر مدخل «خُرد» در برهان قاطع، آوانگاری «xvart» را چاپ کرده است و «k» در کتاب نورایی خوانشِ نادرست همان «x» است. تصویر صفحهٔ چاپی (صفحهٔ ۲۸۲ پی‌دی‌اف = ۲۵۲ کتاب) نشان می‌دهد که خودِ کتاب «kvart» چاپ کرده، پس استخراج داده امانت‌دارانه است و خطا از آنِ کتاب است (خطای چاپی کتاب). از نظر محتوایی حلقهٔ پهلوی ← فارسی نو درست است: xwurd ⟨hwltʾ⟩ فارسی میانه به «خُرد» فارسی نو رسیده است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"kvart\",\n     \"correct_form\": \"xvart (MP xwurd, Book Pahlavi ⟨hwltʾ⟩)\",\n     \"sources\": [W+\"%D8%AE%D8%B1%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"Nourai gives no page here, only 'BQT'. The relevant footnote is on the خُرد page of Borhan vol. 2, BQT_v2_pages.txt leaf 187 (printed c.730): 'پهلوی xvart ... اورامانی xvart ... معرب آن خردة' — i.e. Mo'in prints xvart, which is what the chart garbles to 'kvart'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 96 (PHD.txt lines 664-665)\", \"stance\": \"partial\", \"note\": \"'xwurd [hwltʾ | N ~] small, little. xwurdag [hwltkʾ | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.' Supports the Pahlavi → NP step and the form, contradicts the spelling 'kvart'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary (grep 'xvart|xvurt|xward')\", \"stance\": \"silent\", \"note\": \"no entry for the adjective recovered from NYB_vol2_glossary.txt (the only hits are unrelated, e.g. 'kurušk ... šīr-pistān').\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan vol. 2 leaf 187 footnote 4\", \"stance\": \"supports\", \"note\": \"quoted in ref_check.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"xord «خُرد ( خرده ، خردسال )»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Persian word and its family are exactly as drawn — خُرد xurd 'small', خرده xurda 'fragment, particle', خردسال xurdsāl 'of tender age' — and the Pahlavi ancestor MP xwurd ⟨hwltʾ⟩ is right (PHD 96). What modern scholarship rejects is the ultimate source. Wiktionary s.v. خرد: 'Inherited from Middle Persian ⟨hwltʾ⟩ /xwurd/ „little“, perhaps originally the past participle of ⟨hwltnʾ⟩ /xwardan/ „to eat“; for the semantic development, compare the derivation of Proto-West Germanic *biti „bit“ from *bītan „to bite“. Compare Talysh هرد (hərd), Northern Luri هیرد (hird), Baluchi ہورت (hurt, „little, tiny“)' — i.e. Proto-Iranian *hwr̥ta- from *hwar- 'to consume', the root of خوردن. Horn (p. 112, under xᵛar-) had already rejected BOTH the connection to 'eat' and the connection to Av. xᵛara- 'Wunde': 'np. xurde, xurd „klein“, phlv. xurtak, arm. LW. xortak „zerbrochen, zerschlagen“ kann nicht hierher gehören, da es auf u reimt ... Nöldeke (mündliche Mitteilung) vergleicht lat. curtus „kurz“, das zur √qert- „schneiden“ gehört.' The route via Avestan xšudra-/xᵛarəta- that Nourai draws is Mann's minority proposal ('Per. cf. (from various dialects) xurd „minute, tiny“', IEC 1060), and it fails phonetically: Old Iranian *xšud- would give Persian šud-/šuδ- (cf. سودن sūdan, which Mann himself derives from *ksud-), never xurd-. So the Persian word cannot descend from an Avestan xšudra-.\",\n     \"derivation_fa\": \"خودِ واژه و خانواده‌اش دقیقاً همان است که در چارت آمده — «خُرد»، «خرده»، «خردسال» — و نیای فارسی میانه‌اش نیز درست است: xwurd ⟨hwltʾ⟩ (مکنزی ص ۹۶). آنچه پژوهش امروزی رد می‌کند خاستگاه نهایی است. ویکی‌واژه می‌نویسد: «از فارسی میانهٔ xwurd „خرد“، احتمالاً در اصل اسم مفعول xwardan „خوردن“؛ برای این تحول معنایی، مقایسه کنید ژرمنی غربی *biti „لقمه“ از *bītan „گاز گرفتن“»، و صورت‌های تالشی hərd، لری شمالی hird و بلوچی hurt را هم‌ریشهٔ آن می‌شمارد؛ یعنی از ایرانی باستان *hwr̥ta- از ریشهٔ *hwar- «خوردن». هرن نیز پیش‌تر (ص ۱۱۲) هم پیوند با «خوردن» و هم پیوند با اوستایی xᵛara- «زخم» را رد کرده بود و به نقل از نولدکه آن را با لاتین curtus «کوتاه» (از ریشهٔ *(s)ker- «بریدن») سنجیده است. مسیری که نورایی از xšudra-/xᵛarəta- اوستایی می‌کشد، پیشنهاد اقلیتیِ مان است و از نظر آوایی نمی‌ایستد: *xšud- ایرانی باستان در فارسی به šud-/sūd- می‌رسد (چنان‌که خودِ مان «سودن» را از *ksud- می‌گیرد) نه به xurd-. پس ادعای نورایی در این حلقه پذیرفتنی نیست.\",\n     \"sources\": [W+\"%D8%AE%D8%B1%D8%AF\", W+\"%D8%AE%D9%88%D8%B1%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:729\", \"status\": \"partial\", \"note\": \"The خُرد entry with the Sa'di verse Nourai prints is at BQT_v2_pages.txt leaf 187 (printed c.730, one page off Nourai's 729). Mo'in's footnote gives 'پهلوی xvart' and adds 'هرن خرد فارسی را از اوستایی xᵛarəta ندانسته' — the Pahlavi form supports the chart, the Avestan derivation is explicitly attributed to Horn as REJECTED.\"},\n      {\"ref\": \"IEC:576\", \"status\": \"supports\", \"note\": \"Mann p. 576: 'Per. xurd „small“' is listed among the reflexes of ksudros — Nourai's arrow is Mann's.\"},\n      {\"ref\": \"IEC:1060\", \"status\": \"partial\", \"note\": \"Mann p. 1060 s.v. qusudros: 'Per. cf. (from various dialects) xurd „minute, tiny“; sūdan, pp. sūde, v. „rub, wear down“, fr. *ksud- ?' — note that Mann's own Persian reflex of *ksud- is sūdan, which is the phonetically regular one; xurd is only 'cf.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss p. 112 (HRN.txt line 4584, leaf 133)\", \"stance\": \"contradicts\", \"note\": \"'np. xurde, xurd „klein“, phlv. xurtak, arm. LW. xortak „zerbrochen, zerschlagen“ kann nicht hierher gehören, da es auf u reimt (Vis und Rāmīn S. 51 Vers 12, Šāhn. I 179 Vers 905) ... auch mit aw. xᵛara- „Wunde“ (de Lagarde) wird es schwerlich zusammengestellt werden können. Nöldeke ... vergleicht lat. curtus „kurz“, das zur √qert- „schneiden“ gehört.'\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 96\", \"stance\": \"supports\", \"note\": \"'xwurd [hwltʾ | N ~] small, little. xwurdag [hwltkʾ | N ~a] something small, particle' — confirms the MP → NP link and the derivative خرده.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV *huar¹ 'to consume, eat' pp. 147-148\", \"stance\": \"partial\", \"note\": \"Cheung reconstructs the verbal root (YAv. xᵛar-, MMP xwr-, BMP hwl- /xwar-/, Parth. wxr-, Sogd. xwr-) from which Wiktionary derives xwurd as a participle; Cheung himself does not list the adjective.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan vol. 2 leaf 187 footnote 4\", \"stance\": \"partial\", \"note\": \"quoted in ref_check; supports the Pahlavi form, records the Avestan derivation only as one Horn rejected.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in, 2-vol Adena reprint (grep خرد)\", \"stance\": \"silent\", \"note\": \"the abridged 2-vol reprint carries no etymological tag for خُرد beyond the sense 'کوچک'.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"ksudrah\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sanskrit kṣudrá- 'minute, small, fine; low, mean' is the pivot of the whole root and is correctly given. It is the -ra- adjective of the verb kṣud- 'to pound, crush' (pres. kṣódati 'stampft, zermalmt'), with the o-grade noun kṣóda- m. 'a pounding; flour, powder, dust' beside it and the neuter kṣudrá- 'a mote, particle'; Pokorny p. 625 lists exactly this set under 'kseud- „klein stampfen“', with Old Church Slavonic chudŭ 'small, poor, bad' (comparative chuždьjь : Skt. kṣódīyas-) as the only other member. Semantically 'crushed small' → 'small' → 'mean, base' is the ordinary path (compare Slavic chudŭ, already 'schlecht'). Nourai's transliteration 'ksudrah' reproduces the nominative singular masculine kṣudráḥ.\",\n     \"derivation_fa\": \"سنسکریت kṣudrá- «ریز، خرد، نازک؛ پست، فرومایه» محور همهٔ این ریشه است و درست ثبت شده. این صفت با پسوند -ra- از فعل kṣud- «کوبیدن، خرد کردن» (زمان حال kṣódati «می‌کوبد، خرد می‌کند») ساخته شده و در کنار آن اسم kṣóda- «کوبش؛ آرد، پودر، گَرد» و صورت خنثای kṣudrá- «ذره» می‌آید. پوکورنی در ص ۶۲۵ زیر «kseud- „خرد کوبیدن“» دقیقاً همین مجموعه را می‌آورد و تنها عضو غیرهندی آن را اسلاوی کهن chudŭ «خرد، ناچیز، بد» می‌داند. تحول معنایی «خردشده ← خرد ← پست» عادی است. آوانگاری نورایی (ksudrah) همان صورت فاعلی مفرد مذکر kṣudráḥ است. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"IEC:576\", \"status\": \"supports\", \"note\": \"Mann p. 576: 'Skt. ksudráh „small, fine“; Prakritic ksulla-, id. cf. Romani čulo, adv. „little“; ... Skt. ksódàmi „pulverize“' — verbatim Nourai's word and gloss.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"Pokorny p. 625 (POK_02.txt leaf 285 line 4503)\", \"stance\": \"supports\", \"note\": \"'kseud- „klein stampfen“. Ai. ksödati „stampft, zermalmt“, ksöda- m. „Stoß, Stampfen, Zermalmen; Mehl, Pulver, Puder“, ksudrá- „klein; niedrig, gemein“, Komp. ksödiyas-; ksudrá- n. „Stäubchen“.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 502 (leaf 511)\", \"stance\": \"supports\", \"note\": \"'kseud- „klein zermalmt, stampfen“. Ai. ksoduti „stampft“, ksoda- m. ..., ksudra- „klein, gering; niedrig, gemein“, Komp. ksodiyas-, ksudra- n. „Stäubchen“; abg. chudŭ „klein; dürftig, gering, schlecht“.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann pp. 576 and 1060\", \"stance\": \"supports\", \"note\": \"at 1060 'Skt. ksudráh, adj. „crushed; small; humble; mean“'.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Armenian\",\n     \"words\": \"xord\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Armenian form is taken from Mann, but the gloss is not. IEC p. 576 reads 'Arm. xord „sackcloth“' — 'sackcloth', i.e. coarse haircloth, which is how Mann links it to a root meaning 'coarse, granular'. Nourai has silently replaced that with 'small', which no source gives. Independently, the only Old Armenian խորդ (xord) that Wiktionary records is a bird name, 'common crane (Grus grus); flock of cranes', with the note 'The origin is uncertain. According to J̣ahukyan, perhaps of imitative origin, connected with the onomatopoeic verb խորդամ (xordam, „to snore; to snort“)'. The Armenian word that really does belong to this family is not xord but xortak 'broken, smashed', and it is a loan, not a cognate: Horn p. 112 lists 'arm. LW. xortak „zerbrochen, zerschlagen“' beside phlv. xurtak, i.e. a borrowing of Middle Persian xwurdag. So the node as drawn (an inherited Armenian 'small' from the IE root) is not supportable.\",\n     \"derivation_fa\": \"صورت ارمنی از مان گرفته شده اما معنایش نه. مان در ص ۵۷۶ می‌نویسد: «ارمنی xord „پلاس، جامهٔ زبرِ مویین“» و از همین راه آن را به ریشه‌ای با معنای «درشت، دانه‌دانه» پیوند می‌دهد؛ نورایی این معنا را بی‌اشاره به «small» بدل کرده که هیچ مأخذی آن را نمی‌دهد. از سوی دیگر، تنها խորդ ارمنی کهن که ویکی‌واژه ثبت کرده نام پرنده است: «درنا (Grus grus)؛ دستهٔ درناها»، با این یادداشت که «خاستگاه آن نامعلوم است؛ به گفتهٔ جاهوکیان شاید صوتی باشد و با فعل نام‌آوای خորդամ „خرخر کردن“ پیوند داشته باشد». واژهٔ ارمنی‌ای که به‌راستی به این خانواده تعلق دارد xortak «شکسته، خردشده» است و آن هم وام‌واژه است نه هم‌ریشه: هرن در ص ۱۱۲ آن را «وام‌واژهٔ ارمنی xortak» در کنار پهلوی xurtak می‌آورد، یعنی وام‌گیری از xwurdag فارسی میانه. پس این گره به آن صورت که کشیده شده پذیرفتنی نیست.\",\n     \"sources\": [W+\"%D5%AD%D5%B8%D6%80%D5%A4\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:576\", \"status\": \"partial\", \"note\": \"Mann p. 576 (IEC.txt leaf 327, line 8230) has the form but a different gloss: '... Per. xurd „small“; Arm. xord „sackcloth“'. Nourai's 'small' for the Armenian is not in his cited source.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"IEC\", \"where\": \"Mann p. 576\", \"stance\": \"partial\", \"note\": \"quoted above; the form is Mann's, the meaning is not.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss p. 112 (HRN.txt line 4584)\", \"stance\": \"contradicts\", \"note\": \"'np. xurde, xurd „klein“, phlv. xurtak, arm. LW. xortak „zerbrochen, zerschlagen“' — 'LW.' = Lehnwort: the Armenian member of this family is a Persian loan xortak, not an inherited xord 'small'.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny p. 625, WP I 502\", \"stance\": \"silent\", \"note\": \"neither Pokorny nor Walde-Pokorny lists any Armenian reflex of kseud-.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nimport io, os\np = \"/home/sfmqrb/git/rishe/data/verification/page-282.json\"\nwith io.open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"wrote\", p, os.path.getsize(p))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk282.py && python3 -m json.tool data/verification/page-282.json > /dev/null && echo JSON_OK && python3 tools/verify_check.py 282",
 "description": "Write and validate page-282.json"
}
```


### [2026-09-06T21:51:02.244Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-282.json 61068
JSON_OK
nodes verified: 11/11
node verdicts: {'plausible': 2, 'confirmed': 5, 'disputed': 3, 'transcription_suspect': 1}
root verdicts: {'plausible': 2}
ref checks: {'partial': 7, 'supports': 13, 'not_checked': 4}
books consulted: {'partial': 9, 'contradicts': 6, 'supports': 14, 'silent': 9} | by book: {'WLD': 5, 'IEC': 4, 'POK': 4, 'PHD': 3, 'BQT': 3, 'HRN': 3, 'BRT': 2, 'SYN': 2, 'MON': 2, 'KLN': 2, 'CHEUNG': 2, 'ARY': 1, 'HJB': 1, 'SKT': 1, 'FSD': 1, 'SOD': 1, 'NYB': 1}
```


## [2026-09-06T21:51:30.924Z] AGENT

Done. `python3 tools/verify_check.py 282` → 11/11 nodes, **0 PROBLEM lines**.

**Page 282 (book p. 252) — verdicts**
- Roots: 2 plausible
- Nodes: 5 confirmed, 2 plausible, 3 disputed, 1 transcription_suspect
- Ref checks: 13 supports, 7 partial, 4 not_checked (AHD:1175 1976 ed. not online; ETM:69 no copy; MON page numbers unverifiable)
- 10 web pages archived via `fetch_source.py`; page PNG copied to `data/verification/sources/refs/ocr/BOOK/282.png`

**Flagged items**
- `Ksudros` #1 Avestan `xšudram; xvareta` — **disputed**: WP I 502 / Pokorny 625 put Av. *xšudra-* under a *separate* root *qseud-* "Flüssigkeit" (Skt. kṣodas-, Av. xšaodah-), and Pokorny calls the identification with Skt. kṣudrá- only Ghosh's *attempt*; Av. *xᵛarəta-* is not a word for "small" at all (AiW: 'small' = *kasu-*; xᵛarəta- belongs to xᵛar- "eat").
- `Ksudros` #3 Persian `xord` — **disputed**: modern account is MP *xwurd* ⟨hwltʾ⟩, probably ppp of *xwardan* "to eat" (Wiktionary; cf. Talysh hərd, Baluchi hurt). Horn p. 112 explicitly rejects the Avestan route ("kann nicht hierher gehören"); Mo'in's own Borhan footnote says Horn did *not* derive it from xᵛarəta-. Phonetically *xšud- → Pers. sūd-, never xurd-.
- `Ksudros` #5 Armenian `xord` — **disputed**: Nourai's cited source (Mann IEC 576) glosses it "sackcloth", not "small"; the only Old Armenian խորդ Wiktionary knows is "common crane" (origin uncertain, Jahukyan). The genuine Armenian relative is *xortak*, a loan from MP xwurdag (Horn 112).
- `Ksudros` #2 Pahlavi `kvart` — **transcription_suspect**, `error_in: "book"`. Printed page really reads "kvart"; correct is *xvart* (MP xwurd ⟨hwltʾ⟩, MacKenzie 96). Nourai misread the x of Mo'in's "xvart".
- `Ksîro` root and #1/#5 marked **plausible**: WP I 503 does have "ksīro- Milch, Molken", but on Skt. kṣīra- + Alb. hirrë alone; Pokorny 1959 dropped it, Watkins says no PIE noun for milk is reconstructable, Lubotsky/Wiktionary make it PII *kšiHrám, a BMAC substrate loan. Bare Av. *xšīra-* is unattested (only Horn's queried *apa-xšīra-*); *xšvipata* = Av. xšvipta- (ppp of xšvip-), which WP I 502 expressly separates from *ksīro* though Wiktionary treats it as cognate — same caveat carries to the Sogdian node (Gharib equates ʾxšʾypt- with Av. xšvipta, and the Proto-Iranian *xšiHrám page lists no Sogdian reflex).

**Extraction errors for the owner: none.** The JSON matches the printed page exactly, including the empty Hindustani box, "xšvipata", "apa-xšîra" and "kvart".

Incidental page-number notes: BQT:729 is really p. ~730 (the خُرد entry with the Saʿdi verse); KLN:1411, HRN:178, SYN:385, WLD1:503, IEC:576 and IEC:1060 all check out exactly.
