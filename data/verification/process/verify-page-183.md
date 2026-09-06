# Verification process log — verify-page-183


## [2026-09-05T20:54:16.324Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 183 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-183.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-183.json. Write /home/sfmqrb/git/rishe/data/verification/page-183.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 183` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:54:18.066Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:54:18.774Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:54:18.785Z] TOOL RESULT

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


## [2026-09-05T20:54:18.971Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-183.txt"
}
```


### [2026-09-05T20:54:18.983Z] TOOL RESULT

```
1	=== PDF page 183 (book page 153) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghei 1, Ghiem, Ghi, Khai, Khei : winter  (refs POK:425)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:425 | zem : cold ; zyâ 1, zyâo, zimô : winter
5	  #2 (parent #1) [Persian] refs=BQT:1028,1032; FVF:320 | zam «زم» : cold ; zemestan «زمستان» : winter ☞Stâ ; zamharîr «زمهریر» : a very cold place | extra: سمیرم ، سمیران ، شمیران | NOTE: areas with cold winters
6	#3 (parent #0) [Avestan] refs=POK:425; KLN:728; SYN:1014 | zaem, zyam : winter
7	  #4 (parent #3) [Persian] refs=POK:425; SYN:1014 | day «دی ۱» : (first month of) winter | NOTE: BQT:907 derives this word from the Avestan root "datuš:creator". See root "Dô 2".
8	#5 (parent #0) [Sanskrit] refs=POK:425 | hima : snow ; hima-alaya : home of snow
9	  #6 (parent #5) [Persian] refs=MON6:2320 | hîmâlâyâ «هیمالیا» : Himalayan mountains
10	  #7 (parent #5) [English] refs=None | Himalayan
11	#8 (parent #0) [Latin] refs=AHD | hibernus : pertaining to winter
12	  #9 (parent #8) [English] refs=None | hibernate
13	
```


## [2026-09-05T20:54:22.086Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-183.json",
 "description": "Read source JSON page 183"
}
```


### [2026-09-05T20:54:22.122Z] TOOL RESULT

```
{
  "pdf_page": 183,
  "book_page": 153,
  "entries": [
    {
      "root": {
        "name": "Ghei 1, Ghiem, Ghi, Khai, Khei",
        "lang": "Indo-European",
        "refs": "POK:425",
        "gloss": "winter"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:425",
          "words": [
            {"translit": "zem", "gloss": "cold", "script": null},
            {"translit": "zyâ 1, zyâo, zimô", "gloss": "winter", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1028,1032; FVF:320",
          "words": [
            {"translit": "zam", "gloss": "cold", "script": "زم"},
            {"translit": "zemestan", "gloss": "winter", "script": "زمستان", "see": ["Stâ"]},
            {"translit": "zamharîr", "gloss": "a very cold place", "script": "زمهریر"}
          ],
          "script_extra": "سمیرم ، سمیران ، شمیران",
          "note": "areas with cold winters",
          "quote": {
            "text": "برگ بنفشه چون بُن ناخن شده کبود - در دست شیرخواره بسرمای زمهریر",
            "poet": "Manŭchehrî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:425; KLN:728; SYN:1014",
          "words": [
            {"translit": "zaem, zyam", "gloss": "winter", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "POK:425; SYN:1014",
          "words": [
            {"translit": "day", "gloss": "(first month of) winter", "script": "دی ۱"}
          ],
          "note": "BQT:907 derives this word from the Avestan root \"datuš:creator\". See root \"Dô 2\".",
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:425",
          "words": [
            {"translit": "hima", "gloss": "snow", "script": null},
            {"translit": "hima-alaya", "gloss": "home of snow", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON6:2320",
          "words": [
            {"translit": "hîmâlâyâ", "gloss": "Himalayan mountains", "script": "هیمالیا"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Himalayan", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "hibernus", "gloss": "pertaining to winter", "script": null}
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
            {"translit": "hibernate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:54:24.553Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','BQT','MON','FVF','AHD','WLD','IEC','BRT','HRN','HUB','PHD','NYB','ARY','SKT','WEB','FSD','CHEUNG','KNT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online.json keys"
}
```


### [2026-09-05T20:54:26.239Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
CHEUNG MISSING
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-05T20:54:54.010Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:54:54.046Z] TOOL RESULT

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


## [2026-09-05T20:54:54.860Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo ---- && ls data/verification/ | head -50",
 "description": "List refs dir"
}
```


### [2026-09-05T20:54:54.904Z] TOOL RESULT

```
AFA.txt
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
AHD_watkins1985.txt
AHM.txt
AID.txt
AIN.txt
AKD.txt
ARB_abdulraheem.txt
ARB_mo3rb.txt
ARP.txt
AVG.txt
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
BRT.txt
BST.txt
CHEUNG.txt
DEV.txt
DOZ.txt
DRM.txt
EAV_studies.txt
FRS_pages.txt
FRS.txt
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
FSF_pages.txt
FSF.txt
FVQ_pages.txt
FVQ.txt
GPL.txt
HENNING_selected_papers.txt
HID.txt
HJB.txt
HRN.txt
HUB.txt
IEC.txt
incoming
ISS_alt_DKS.txt
KFL.txt
KLN_1966.txt
KLN_1971.txt
KNT.txt
LAM.txt
LAT.txt
LEW_1910.txt
LKT.txt
LST.txt
MON_part1.txt
MON_part2.txt
MPP.txt
NAT_2005.txt
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
SIN.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
----
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
```


## [2026-09-05T20:54:58.887Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T20:54:58.922Z] TOOL RESULT

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


## [2026-09-05T20:55:00.371Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','KLN','BQT','MON','FVF','AHD']:\n    print('=====',k)\n    print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\"",
 "description": "Full ref metadata"
}
```


### [2026-09-05T20:55:02.287Z] TOOL RESULT

```
===== POK
{
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
===== SYN
{
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
===== KLN
{
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
===== BQT
{
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
===== MON
{
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
===== FVF
{
 "title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968",
 "kind": "website",
 "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)",
 "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."
}
===== AHD
{
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
```


## [2026-09-05T20:55:06.247Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: ĝhei\\|lemma: ghei\\|lemma: ĝhi\\|Page(s): 425\" POK_full.txt | head -30",
 "description": "Find Pokorny root ghei"
}
```


### [2026-09-05T20:55:06.301Z] TOOL RESULT

```
7063:[see Root/ lemma: ghei-2. ghi-\ "winter; snow' 
7245:lemma: ghei-2, ghi-, ghei-men-, *gheimn- : 'winter; snow'. 
17987:Root / lemma: dem-, derna-: "to build; house' derived from Root/ lemma: ghei-2. ghi-: 
26888:lemma: ghei-2, ghi-, ghei-men-, *gheimn- : "winter; snow' 
32563:Root / lemma: gheid!^- 
32588:Root / lemma: gheigh- 
32613:Root / lemma: gheis- and gheiz-d- 
32698:Root/ lemma: gheigh-: "gland' derived from an extended Root/ lemma: gel-1\ "to curl; 
32806:the winter' [see Root/ lemma: ghei-2 . ghi-\ 'winter; snow' 
36116:Root / lemma: ghei-1, ghei- 
36164:Root / lemma: ghei-2. ghi- 
36221:lemma: ghei-2, ghi-, ghei-men-, *gheimn- : "winter; snow' 
36272:Page(s): 425-426 
73509:Root/ lemma: sem-3: "summer' has certainly derived from Root/ lemma: ghei-2. ghi-,
```


## [2026-09-05T20:55:07.330Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==81||NR==82' POK_02.txt | head -120",
 "description": "Print Pokorny leaf 81-82"
}
```


### [2026-09-05T20:55:08.951Z] TOOL RESULT

```
s.  geador,  tö  gcedere  (engl,  together)  ,zusammen'^  afries. gadur,  mnd.  gader,  mhd.  gater  ds.,  ags.  gadrian^  gced(e)rian  (engl,  gather) ,sammeln',  afries.  gaderia^  mnd.  gad(d)eren  ds.,  mhd.  vergatern  ,sich  vereini- gen', nhd.  vergattern  ds.;  dazu  vermutlich  auch  ahd.  gataro,  nhd.  Gatter (umgelautet  mhd.  geter,  nhd.  Gitter),  aschwed.  gadder,  mnd.  gaddere  , Gitter';
mit  Dehnstufe:  got.  göps,  aisl.  gödr,  ags.  göd,  ahd.  guot,  nhd.  gut  (germ. *göda-  ,passend');  aisl.  göda  ,gut  machen'  usw.
aksl.  god^  ,Zeit^  rechte  Zeit',  godina  ,äQa%  godhm  ,gefällig'_,  russ.  godnyj ,tauglich',  aksl.  u-goditi  ,gefallen',  russ.-ksl.  goditi  ds.,  ksl.  ugoda  ^Wohl- gefallen', russ.  vygoda  ,Vorteil',  aksl.  negodovati  ,unwillig  sein',  iter.  aksl.
424  •
ugozdo,  ugoHiti  ,es  einem  recht  machen,  gefallen'   (usw.,  Berneker  317^ wo  auch   über  die  poln.  Lehnworte  lit.  gädas  ^Vereinig-ung-'^  gädijtis  ^ ereignen,  treffen'  u.  a.).  ?^'
Dazu  vielleicht  lit.  dial.  guddas,  lett.  güods  ,Ehre,  Ruhm;  Anstand,  Hö^ lichkeit;  Festlichkeit,  Schmaus';
hingegen  sind  lett.  gäds,  sagäds  ,Vorrat,  erworbene  Habe',  gädät  ,sorgeQi wohl  aus  dem  Russ.  entlehnt;
hierher  (vgl.  Van  Windekens  Lexique  32)  toch.  AB  kätk-,  erweictj[ A  käck-^  B  käcc-  ,sich  erfreuen'  (vgl.  oben  mnd.  gaden  ,gefallen');  ändert Pedersen  Toch.  172.
WP.  I  531  ff.,   Trautmann  74,   Feist  218.    S.  auch  unter  ghend-,
ghegh-  jkrümmen,  biegen'.
Arm.  gog  ,Höhlung,  Schoß,  Busen,  Bauch'  usw.,  als  Adjektiv  ,hülil. konkav',  gogem  ,aushöhlen';  gugem  (*ghögh-)  ,umarmen,  pflegen';
norw.  gagr  ,zurückgebogen',  aisl.  gag-hals  ,mit  zurückgebogenem  Hals' ablaut.  gcegiask  ,sich  strecken',  usw.;  ^*«
lit.  gogas  m.  ,Widerrist  des  Pferdes'.
WP.  I  570,  Liden  Armen.  Stud.  93  f.
i{h)egh'  ,Iltis'?
Ai.  jdhakä  ,Iltis'  (oder  ,Igel'?),  lit.  seskas  ,Iltis'  (durch  zweifache  Assi- milation aus  *zezkas  entstanden);  vgl.  lit.  oskä  ,Ziege'  gegenüber  ai.  ajikä  ds.
WP.  I  570,  W.  Schulze  Kl.  Sehr.  630;  anders  Mühlenbach-Eudzelia III  820.
I.  ghei-,  ghei-  , antreiben,  lebhaft  bewegen  (schleudern)  oder  bewegt  seia^; ,(geschleudertes)  Geschoß';  von  der  Bed.  , Geschoß'  oder  allenfalls verbal  , wonach  schleudern,  treffen'  kann  , verwunden'  (Gruppe  B) ausgegangen  sein  (Wurzelf.  ghei-s-).  Vgl.  noch  gheis-,  gheizd-  , aufge- bracht sein',  sowie  ghaiso-, A.  ghei-  , antreiben' :
Ai.  hinöti,  hinvati  (Partiz,  hdgant-)  , treibt  an,  schleudert',  
Partiz. hitd-h]  hemdn-  n.  , Eifer';  heti-h  m.  ,Geschoß'  (vgl.  germ.  *gaida)]
av.  zaeni-  ,rege,  eifrig',  zaeman-  , regsam,  wach',  n.  ,Regsamkeit,  Munter- sein, Wachsein',  zaenahvant-  (von  einem  *zaenah-  n.)  ,wachend,  wachsam'; zaena-  m.  ,Waffe',  zaya-  m.  ,(*Waffe),  Gerät,  Ausrüstungsgegenstand', zayan-  ,bewaffnet'.
Auch  ai.  hdya-h  ,Roß'  =  arm.  ji,  Gen.  jioy  ds.  hierher  als  ,das  Leb- hafte'?;
langob.  gaida  f.  ,Speer',  ags.  gäd  f.  ,Stachel,  Spitze,  Stecken',  PN  ahd. Guido ;  dazu  aisl.  gedda  f.  ,Hecht'  <  geidida,  vgl.  läpp,  kaito  ds.
425
got.  lang'ob.  gain-  ,Waffe^  in  PN  {Gainhard,  Gainwald),  ags.  gaen-  in  PN ;
got.  *gails  m.   ,Speer^  in  PN  Gel-mlrus,   ag's.  Gäl-frid,    ahd.   Geil-imiot.
B.   fjheis-  , verwunden^ :
Ai.  hesas-  n.  , Geschoß^  (kann  aber  auch  idg.  *ghaisos  sein,  s.  dort);  dazu wahrscheinlich  h'(,sati  (erst  nachved.  hindsti)  , schädigt^  verletzt^;
air.  (70/^e  ^vulueratus^,  mir.  gäetas  ,qui  occidit^  (*ghoizd-)]
lit.  ^eidziü,  zeidziaü,  £eisti  ^verwunden',  Itaizdä  ,Wunde^  Dieselbe  c?-Er- weiterung  bei  gkeis  :  gheizd-  _,aufgebracht^
WP.  I  546,    Pokorny  Urillyrier  64,  Holthausen  Got.  etym.  Wb.  34.
j.  ghei'  :  gbi-  ,Winter,  Schnee^;  nach  Specht  Dekl.  14,  330 f.  alter  -men- Stamm,  mit  schon  idg.  Wandel  von  mn  zu  m.
A.  ghei-men-,  *gheimn-:
Die  r-Er Weiterung  ist  analogisch  nach  ^s^mero-  ,sommerlich^
Ai.  himaji  (Lok.)  ,im  Winter^,  hemantd-h  m.  ,Winter^  (:  hitt.  gimmanza  ds.) ;
gr.  xeiy,a  n.  ,Winter,  Wintersturm,  Kälte^,  xel^ojv  m.  ,Wintersturm, Winterwetter,  Winter^  (dazu  auch  x^i^f^Qog  , Zapfen^,  der  herausgezogen wurde^  wenn  das  Schiff  aus  Land  gebracht  wurde) ;
alb.  geg.  dlmeii  m.,  tosk.  dimer{e)   , Winter^    (alter  Akk.  *ghei-me7i-om) ;
bsl.  *zeimä  (aus  "^zelmna)  in  lit.  ziemäj  lett.  zzwa,  apr.  semo  ,Winter^  und
aksl.  zima,  Gen.  zmy,  russ.  zimd^  bulg.  ziniaj  skr.  zimaj  sloven.  zima, cech.  zima,  poln.  zima  ,Winter^
hitt.  gi-im-ma-an-za  , Winter^  s.  oben.
Dazu  gheiin{e)rinos  und  glieiminos  ,winterlich^
In  gr.  x^^y-^Q^'^^'sy  ^^^'  hibernus  (<^  *gheimrinos),  Vit.  iiemmis,  aksl.  ziimm, russ.  zimnijj  skr.  zimni,  cech.  zimni  (dech.  zimny  ,kalt^),  poln.  zlmny  ,kalt, winterlich'  (vgl.  mit  ablaut.  i  in  der  Wurzelsilbe  arm.  jmern  , Winter').
Zu  *ghei-  allein:  av.  zayan-,  zaen-  m.  , Winter^,  npers.  dai]  av.  zayana- , winterlich^  und  mit  Vrddhierung  ai.  häyana-  ,jährlich^,  häyand-  m.  n. ,Jahr^  (Reimbildung  zu  av.  hamana  , sommerlich^).
B.  ghiöm,  ghiidm,   Gen.  ghiemös,   ghimös,  auch  ghiomös  (m  aus *mn  ?).
Av.  zyä  f.  , Winter'  (Akk.  zyqm^  Gen.  zlmö) ;
arm.;m7i,Schnee''(<  *ghiiöm)j  Gen.jean  (<i  ghijPn-,  s.  MeilletEsquisse45);
gr.  XLdtv  (*xta;^0;  X'-^'^^'s  , Schnee^;
ligur.  möns  Berlgierna  (,schneetragend'),  mit  umgestalteter  Endung;
lat.  hiems,  -is  , Winter^ ;
mir.  gem-adaig  ,Winternacht'  {gam  , Winter^  ist  nach  sam  , Sommer*  um- geformt, vgl.
```


## [2026-09-05T20:55:37.370Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN dai ===\" && grep -n \"dai\\b\" HRN.txt | head -40 && echo \"=== HRN Winter ===\" && grep -n \"Winter\" HRN.txt | head -40",
 "description": "Grep Horn for dai/Winter"
}
```


### [2026-09-05T20:55:37.434Z] TOOL RESULT

```
=== HRN dai ===
985:Wohl zu ö + i^dai- (ai. {^dhai-) wie die folgende
1001:a+ i^dai' (ai. dhai-),
1482:ol (Vf nvToi xai aaiaV^Ti« (lies aaydvdai); vergl. auch Herod. VIII, 98
4827:'saugen (103); bei. LW. dai (53).
5306:ap. i^dai-, didiy sehen'; aw. l/'rföi-, a]di^aifi:
6023:Sein , zvandai 'lebendig'.
6890:aw. \^8caüd'^), scindai/^Urzerhrechen ; phlv. skastan
9600:Citat, dai>- Vullers übrigens gewiss nicht mala fide unterlassen hat,
15888:dai&r 619.
=== HRN Winter ===
3542:375. tejer 'Winterhaus mit Heizvorrichtung; Magazin*,
5877:666. xeni 'Kälte', zemistan 'Winter.
5878:aw. zyao- 'Winter', Gen. ziniö; phlv. zam 'Winter'
5879:(vd. 2 (20)), zam(i)stan; ai. himä- 'Winter ; arm. vergl.
5880:jiun 'Schnee', jmern 'Winter', jmerem 'überwintern
5882:oss. d. zumägy t. zimag 'Winter' (135); af/. zimai;
9573:ap. *han(/ama' *Zeit*, vergl. aw. aiwLgäma^ 'Winter ;
```


## [2026-09-05T20:55:38.132Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT zya ===\" && grep -n \"zyå\\|zyā\\|zyam\\|zimö\\|zim<\\|zaēn\\|zayan\" BRT.txt | head -40",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T20:55:38.189Z] TOOL RESULT

```
=== BRT zya ===
2660:•  p.  aiva-,  j.,  g.  aeva-,  j.  oiva-'*  Zw. (fem,  'vn-)  'ein*  i)  als  eig.  Zw.,  im  Gegens. zu  anderen  Zw.  oder  einer  beliebigen Mehrheit  'ein;  einzig,  allein' :  tilm  '*  . .  di'a . .  tisrö  F.  /;  —  nöit  . .  °vo  nvit  dva  mit '^räyS  nöit  fräyankö  Y.44\  —  'vake  .  . *al>ntaoyaAe  .  .  dvaya  .  .  'irayqm  V.  iS. 11;  ^.0^,108;  —  ^riS"  may^m  (sd.)  .. dva  ..  *öiin'^ '^  \. 16.12;  • —  zayante  .  . dasa  puira  >rayä  . .  ^rHyÖ  .  ,  ^rJyS  .  . »ra  (statt  NSm.)  Az.5;  Vyt^i  —  'vqmvä avi  xsapan>in  äuyS  vä  pancäsahm  va  Yt Ali;  —  'va  (IS.)  'iritva  akmiil  masye- Aim  .  .  dva  iriA-a  .  .  ^ribyö  ^rih'aiifyö V,  2. 1 1  f.;  —  cvaf  .  .  yaam  (sd.)  frabaräti
2776:afiar;  damit  wird  aber  auch /^W  übersetit.  |,  j_  ,g^^^^,  ^  .pg^g..  _j,^^/„„  zayan^m •  j.,  g.  =ae5-,  p.  ais-  V.  '(sich)  in  eilige  Be-  ysstryehe  fhiyantö  'la  CND.)  >'»yA«»»(sd.) weguQg  setzen'.  Praes.  3  iSa-,  27  isya-,  30  ■  v_  j^^  ^^
3453:•  j.,  g.  aj-cit  ParL,  an  der  Spitze  des  Satzes und  Versglieds;  1)  im  Nachsatz  hinter ^fl/- ät:  a)  yatcil  tnqm  Iura  pazäayatita  ..  at- cit asim  tanöm  aguse  .  .  ajat  mqm  fra- guzayanta  "als  .  .,  da  .  .  da  . ."  Yt.  f^. 56.        h)  yatcit  Ävasf;fm {sd.)  *aaAyeiti..
4679:tsin  aiare^  utä  'niyä  bagäA^  lyaty  At^tiy Bh.  4-  ■  2  >  13;  —  "^'"i  vahistsm . .  'iiya^qm yat  anifsanqm  spmtanqtn  YL_j,3;  —  yetii zT  MS  maiysia  .  .  yazayanta  yak:a  'nye yazaiinhe  . .  yazinti  ". .  wie  dae  andern y.  verehrt  werden"  YtÄii;  —  ahe  nars asaofiB  ..  äai  'nyazsqm  asaonqm  Yti.30; i3-  ^Ti  —  airime  gstüm  kl  nUhka^a  .. *par^itar?m  kala  'uyalibyd  mazdayas- f>aiibysY.(}.^y, —  'nye  aaksus /rals.iar^ %ra  Aog.65(?)'';  —  \'.ulä  pärsJ' uls  msdt^ utä  "niyS  dahySve^  Bh. /.  13,  14;  11;  — psrsaiy . .  msdaiy  utä  'niy^uvä  dakyusuvä Bh.  J.  10;  —  ahmäi  nmsnäi  daaäiti  gBu^ca vq^iwa  . .  upa  'nya  (APn.)  sHndayäti  Yt /o,  2  8 ;  —  vätB  , ,  AubaoioitarS  . .  'nyalifyö vstaeihyö  H.2.7;  25,  V.j.ss,  ^,29,  Vyt. 45i  —  ""^  a%ra  frakavB  mä  apakavB  . . maia.cim  'nyqm  (GPn.)  daxstanqm  V,  2. 29;  —  ahtnavaila  (sd.)  gäkanqm  .  . uilavaitTm  hsitlmca  , .  av5  yS  °nya  (näml. gä'^h)  srSvaydii  N.  46.  a)  Plur.  mit folg.  äi  'auch  die  andern' :   tl  mqm  ava%a
4907:•  j.  aya^äna-  n.  Name  eines  landwirt- schaftlichen, anscheinend  beim  Pflügen notwendigen  Geräts:  yaiSatn  zayanqm vastryehe  ßiiyantS  .  .  'iJna  (NP.)  paiti.- dar>zäna  (sd.)  V.  i4- 10.
5072:•  j.  ava'Sra  Adv.  'illic,  dort':    airyamm vaijS  . , .    dasa    ''^ra    manttö   zayana  V.
5655:•  i-,  p,   'arätay-  f;  m."  'Speer,  Lanze': yaäam  zayanqm   raitöiiti  paoiryS  °iis  V. 14.^;    —    'tayasiä    karitayasca    '^.fj —  •//'/  ki-aiwyästa  Yt  13.  7 ; •tSis  huxsnutaya  Yt  10.  24;  —  'tayasat
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
7038:satz'so,  dann;  da.' -.yezi ('wenn') aAipaurva.- naem3l  3'  mqm  avi.rimilnaya  (sd.)  Yt.16. 2;  a.  3-3,  Y.2.43,  ^'.36,  103,  /ö'.ii,Nik. 3,  Vd.  13';  —  yat  ('wenn')  yave  dayat ä'  datva  y^ism  (sd.)  V.J. 32;  321,  H.  2". 13,  N.  IJ2;  —  3at  (s.  8)  yat  apö  uzbargnte .  .  a°  fraiasinti  . .  fravasayö  Yt.  13.65; V.  Ä40,  i7.4;  —  yat  ("als')  mqm  tura pazdayatita  .  .  3'  az3m  tanüm  aguze  .  . \3at  (s.  3)  mqm  fraguzayanta  ..Yt  i7.  55^'; — yas}  tat  nmäfum  äk^rstmn  .  .  «7°  mqm tnairyö  akasat  dai  (s.  2)  .  .  fräksrmaot V.  22.  i£;  —  3at  (s.  8)  yat  miirtm  .  . /radaöqm   .  .   a°  dim  danqm  ,  .  Yt.  10.  i ;
7053:•  j.  f,  g.)  äitay-  f.  'Herzu-,  Hinzugehen', nur  IS.  °/f"  im  Sinn  eines  Absolutivs  bei Verben  der  Bewegung  zur  Verstärkung des  Verbalbegrifis;  a)  bei  gam-:  ava  tä anya  maya  'ti  jassit  "zu  den  andern Löchern  soll  er  hinzutreten"  V,i7.3i;  — verdoppelt:  pasca^a  ava  ta  °ti  maya  'ti jaiSitV.g.iz;  32.  b)  bei  'sta-  mit  a/iu und  i'i:  yavat  anu  aipi  (sd.)  *°ti''>  garayj visastars  Yt.  ig.  8.  c)  bei  'bar-,  ver- doppelt: asänS  °ti  maya  "ti  bardil  safom (sd.)  fä  ". .  sollst  du  Steine  zu  den  Löchern hinzubringen  oder  . ."  Y.g.ii.  saota- yanta    'ti  niräzayantl  Vytj6"(?).  aite
7265:13,  N.  Ö2;  —  äat  (s.  8)  yat  äpd  udiannte .  .  ä'  fralasinH  .  .  fravalayS  Yt  JJ.  65; V,  ^,40,  ^7.4;  —  yat  ('als')  mqm  Iura pazdayaiita  . .  ä°  azsm  tanüm  aguze  . . äat  (s.  3)  mamfraguzayanta  ..  Yt  i;.  553'; — yas)  Uli  mnärom  äktrirum  .  .  ü°  mam mairyd  äkasat  äat  (s.  2)  .  .  fräkirmaot V.  22.  if;    —    äat  (s.  8)  yat  mi>r)m   .  .
8584:•  j.  *uzayant-  Adj.,  PPA,:  s.  sä-.
9546:yaihe  vanuM  °fs  Yt/0, 60;  —  "pfm  srao- Iahe .  .yasamaide  'pftn  rasnaes . .  'p^m^*  . , Yt.  //,  21  f.;  —  paoiryä  dasa  xiapanJ  .  . listryB  .  .  'pf/n  rai'^wayeiti  .  .  nars  'pa (IS.)  panco-dasanhS  ".  .  formam  induit ,  , viri  forma  .  ."  Yt  Ä  13;  16,  iS;  — mae^imca  värimta  yä  ts  (näml.  Haomakt) 'piin  vaxlayats  V. /O-3;  —  vupimca  'ß (als  AS.)^'  ahurahe  mazdä  yazamaide  Y. 77.4;  — yat  dim  mazaos  (sd.)  °/J  türahe V.  13.  39;  —  pueril  zayante  tanuAshrpa 'pa  Yyt.i;  —  biDX'jqm  tnöi  firasaostrd ..dalddiit  "pJm  (AS.)'y.5/.  17;  —  upa.- iaht  ar?dvi .  .  kainlnB  'pa  srtraya  Yt 5.  64;  H.  2.  9;  —  yq/"  ■  ■  car.liii/iqm  'pa sralstqm  dildansa  H.  2.  10;  9,  YL5.  34, j/'.  11;  —  yeAAä  'pS  hurae'-aya  Yt  y. i9o(?);  —   'fimca   F.^jht?)^'.  a)    sva.
9673:•  j.  kuirit-"  m. 'Halsbinde, -berge': ^«Sä« zayanqm  rd^öisti..aU3mS  *°rit  (NS.)'*  V. i4-9i  —  °risciAe^>  Vd.J2.
9875:mit^a  'aus  dem  Versteck  hervorholen': äai  mam  fraguzayanta  . .  "da  holten  mich aus  dem  Versteck  . ."  Yt. /".  55.
10543:•  j.  puirS  zayante  tanu-kihrpa  kikrpa "xay^us'*  Vyt,  /,
11044:—  Ki'aUm  vlspa  tarsu'a  xsutraca  Yt.  IQ. 58;  — ye^hs.  .ynnhqmlä  (Sp,  565  m.)  tnscä tascä..  Y. 27. 15;  —  vTspaU  ayqnca  xsaf- nas^aY.SJ.iT,  —  Aamaka  .,  hqmimmca zayan^mca  Y.6'1.5;  —  zqm..yqm  masJmca pahanqmcaYt.13.  q;  —  syao^anäcä  sing-
11964:•  j.  tanu.kahrp-  Adj.  'die  Gestalt  der eigenen  Person  habend' (?) '*,  von  Söhnen: puHrS  zayanle  °pa  kiArpa  Vyt  V;  3.
12155:•  j.  Haäta-  n.  'Tasse,  Schale' :  3r)zataina hala  "ta  (IS.)  zarattaemm  aoi  taxSe  Y.  lO. 17;  —  °täi  *tao%rS.bai'anai  {s,A.)  Yt.  10. i;  —  °ta  (NP.)  änuhanna  V.  7.  73;  N. 66;  —  'taca  haomaca  hävana^a  V.5. 39; '5-  9i  —  yaglqm  zayanqm  d^aurune  . . 'la  Aaomya  V.  14.  8.
12544:mit  pairi  'rings-,  rundum  aufdämmen, mauern':  altera  he  alte  masdayasna  ai^ha e^rnH  pairi.dalxan  (sd)  pairi.datzayan  V. 3.  18.
12725:Landes,  Landesherr*;  vanmm  yim  ca%ru.'\ gaosfm  . .  ake  paityänat  fräk»r>ntat  avrS ! mainyu!  araiiwyUca  daxsta  (sd.)  anair- yala  'Iura  (als  AP.)  ". .  und  nichtarische Herren  des  Landes"  V.  /.  17;  —  vpa aoia?su  ranhaya  .  .  ake  paityärim  frä- ifryrUat  anrS  mainyui  zyam'a  . .  taoiyäca (sd.)  'iura  V.l.  19. Komp.  mit  NS.  im  1.  Glied.  —  Pü.:  aitfr diAän  apar  mäminth,  (za  V.  r.  19)1  fehlt.
13365:-blähend',  von  Fröschen":  batvar»  vasaya- nam    'nyanatn   .  .   vazayanam    upapanam
14321:—  yd^ä  ^wä  zTvTiHfK  uzimökz  (sd.)  Y. 46.');  —  *yavatai'>  ^wä  masds  *staomI ufya(s±)cä  Y.43.S;  —  maibyB  %wä sqsträi  (sd.)  v»r?nl  akurä  Y.4^-Z'>  — vakistim  %wa  .  .  akur»m  yäsa  (sd.)  Y. 2Ä8.  zu  I  a):  atzt'h-wäfsuyantailä.. "hwsnlta  (sd.)  latasä  Y.  2p.  6;  —  dazu wohl  auch*':  azSm  tai!  ^wä  /raxsnlisd.) aväml  magdä  Y.  44-  7 1  —  sp^nttm  at %wä  mazda  mingkx  (zA^  V.4J.  5,  7,  9, 11,  13,  ij.  zu  3):  firalaostrai  .. alakyä  da  I  sarSm  ta}  %wä''^  mazdä yäsai^d.)  Y.4p.8;  —  s.  noch  Y.2Ä  5  im Anhang.  Anhang.  Der  Akk.,  dem ein  Vok,  vorhergeht,  ist  dem  Akk.  eines (mit  CS  angeschlossenen)  Subst  koordinirt (Sp.  565  u.);  vgl.  2,  9  (Sp.79ou.):  asä  kaf %wa^''  darisani  (sd.)  manascä  vokü  Y. 28.  s;  s.  zu  2.  B  I  ß)  im  YHapt.;  zu  1): a%a  %iiia  ail  yazamaidiY-sg.i,;  36.\ i.St,  3;  —  kumälm  %wa  .  .  yazat^m  .  . dadsmaidi  Y,  47. 3 ;  —  äzoö  (zu  'hwa-)  ^wä mainya  spStiistä  (näml.  pairT.jasämaidt) Y.36.1;  5;  —  vokB  %tvä  manar^ks  voka %7iia  asa  ..  Y.36.4;  4.  zu  z):  a^ä isBidyämakx  %wä  mazdä  akurä  Y.^^,4;
14953:•  j,  paiti.däna-  m.  'Vortuch,  Schutztuch'; a)  auf  der  Brust  (unter  demPanzer)  getragen, 'Brusttuch':  yalsqm  zayanqm  ra^BtlH  . . naumö  'nS'V.j4.g;  —  taranafrum  °ram  .  . histaile  draiimns  (statt  fem,)  artdvX  Yt 5.133.  b)  insbes.  Name  des  von  den Priestern  über  Nase  und  Mund  getragenen Tuchs  *^  das  bestimmt  war,  das  Feuer  vor der  Berührung  durch  den  Atem  zu  be- wahren**': yagsqm  zayanqm  a%aurune astra  gaoihi  'nD  V.14.8;  —  'rum  *ainm iarai/i  anaiwyäs/ff  dalnqm  V.  lÜ.  i;  — wird  dem  Toten  mitgegeben  (s.  *'):  avi h?  iristanqm  tanüm  .  ./rada%eiiti  , ,  xa/fvl 'nahe  Vd.  12.
17449:yal  tarn . .  vansasia  (sd.)  * hqmj-äzayanka varjsäs^a  *pairi.brlnaf3ha  '1  V.  77.  4;  — ^yö  .  .  varpsäsca  *hqm.razayeiti  ,  .  pairi.- I  "brTn^nti'^  y.iy.3.
17603:•  j.  fradaxSaiü-  f.  'Schleuder'  als  Waffe: yagsam  zayanqm  rdhsisli . .  x//vf  "na  snä- var».iämra  (si)  maj  'krisqs  /radaxianyäis "..  Schleuder  mit  dreissig Schleudersteinen'
18656:•  j.  nava.satö.-zyam-  m.  Flur,  'neun- hundert Winter' :  äat yimili  xsa%r3i  *'!Pma (NP.)  ''hnjassttta  V.2. 16.
19401:—  nsit  mqm  vlspe ..fraonHntaYK.i'^.i^; 8.  a3;  —  a  mam  yasamiha  .  .frä  mqm hunvamtha  . .  aoi  mam  staomaine  stüm Y.g.a;Y.iS.i9',  Yt  &  24.  /?•  15';  — nasdyB  mqm  upaM^ta  Yt.ij.ai;  — vTvashä  mqm  paoiryS  .  .  hunota  Y.5. 4; — Jainti  mqm  ahuna  vairya  . .  \lapaydti mqm  a!a  vaAista..YLiy.io; — usihista tu  \vyaraynle  mqm  Y. 18.26.  zu  t  a): y^i  gj  ma  mafyaka  . . yazayantaYtS.ii;
19402:—  y^tlH  vtqm  iura  pazäayatita  .  .  atai mqm  fi-aguzayanta  ..  YLJ7.56;  56;  — *daSaJ  zTmqm  avavata  daxsa (%^)yd^a  . . P.  22.  2)  Abi.;  a)  im  Ap.;  zu  a  a): tyJ'lam  hahma''  d^aAya"  .  .  ave^  .  .  Eh. /.  7;  8,0.6.3; — pasäv<r  kacama^  atars<i' Bh.2.4;  D.j.a;  —  imä  dahyäv^  tyä Aacäma"  Aami%''iy3  abava'  Eh.  2.  2;  5, ,?■  S.  13'  zti  33):  vahyatdat^ ..hauv *duvitty(^{sA.)ma^  udapatata  Eh.  5.5;  — mana  als  Abi.:  hauv  ''uvajam  hami^^iyam akunauS mana  Bh.4>3.  bi)  im  gAw.; zu  a  3):  yezT  ahya  \asa  psi  mai  xsayeht Y.44.1^,  n)  im  jAw.;  mäveya  als AbL;  zu  a  i);  ima  .  .  ya  mavSya  pasia vazstiti  Yt^.  95.  3)  Dat;  b)  nurn)  im jAw.;  zu  a  i):  uzvar^zai  (sd.)  mavöya mihB.matanqm^a  . .  Vr.  20.  2.         4)  Gen.;
20338:•  j.,  g.,  p.  mah'  m.  i)  'Mond',  auch  als Gottheit*':  avat  hvan  .  .  käu  ma  .  .  ave stärS  V.p.  41 ;  —  yat  ml  starS  .  .  kacilnie (sd.) paraca  mä  ..YtS.i;  —  stärS  mSahS (NS.?)''  *ki>an  anayra  *rao^ä  FrBy.;  — i.7»hqm  (yä.m\.  fravaHnqm)  raya . .  hvars . . mä  ava  pa%a  aiiti  . .  stärS  Yt.  13.  r  6 ;  — upa  tairam  AaraihyA  .  .  yat  tnl  aiwits urvispnli  staras^a  mis^a  hvanla  Yt./2,as; V.  2. 40;  —  strSuÜca  mäahsmca  hvar?ca Y.  2.  II,  7/.  9,  G.^.6,  Yt/O.  I4s;  V.  ir.  i, 2  (statt  NS.),  7.  52  (statt  NS.),  VyL  43;  — haca  manhsm  (statt  AbL)  V.//.10;  — fravalayö  .  .  yä  strqtn  mäahS  (GS.)  hürB .  .  pa%S  dalsaym  Yt /J.  57;  Y./.  16;  — yazai  hax^r)mca  yat  asti  . .  antan  maf?- h)mca  hvanca  Yt  6.<,\8.\;  —  kj  yä  mil ux^äti  tunfsaitx  Szcß/(sd,)  Y.  .^3;  — pancaJasa  (sd.)  mä  ux^eiti  panla.dasa mh  mnßatti  Yt?.  3;  z',  F.  (?;  —  yai mätshtm  (statt  NS.)  raoxlne  täpayeiti  Yt. 7. 4;  —  raoxsrum  mafihtm  aiwi.vainsm Yt7. 3;  3^;  —  tanüm  .  .  yaha  maaAs hväraexmS  {sA.)  Yt. /0,14a;  —  ragnna- vatitwt  bavähi  yä^a  mävh^m  (statt  NS.) Az.  6;  Vyt  4;  — yatai  mäahgm  ffoaa^r^m bay»m  raSvanttm  i^annaauAantpm  YL7. 5, S.2.  12;  Yt7.3,  6,  -TZ- 33,  Y./6.4;  — mäahahe'^  gaoc^rahe  Vt?,  o;  Y.  j.  11, N.  47;  —  mmS  mänhai^^  gaocÜiräi  Yt. 7. 1 ;  —  uzayara  usTra  mnnha  (VS.) '' gaoHhra  V.  21. 9.  a)  mäahahe''^  (näml. ayari)  heisst  der  12,  Monatstag:  mäis- hahe^^  gaoevirake  S.  j.  12;  vgl.  2.1a,  Y. 16.  i,,  2)  'Monat':  dasa  ava%ra  tnäKhö (NP.)  zayana  dva  hqtiüna  V.  /.  3 ;  —  hapta
20844:g.  8;  —  ävSya  *dä^r^m  ddhaiie  yeüke dä%rahe  däiti  *nait  Aava  urva  *väurltza (sd.)  N.  84;  —  ma/ianahe  .  .  yahmi  il käai  ianunqm  dmjistim  (sd.)  käme  mai- %ame  mi'^näi  Y.16.  10;  —  vispe  taya yag/qm  zayanqm  V,/4.8ff;  —  NSm,  mit nä:  zarahuitnm .  .ys  nä  tstasca  yesnyasca . vaoce  Yt  7^.  1 5  2 ;  —  das  adjektivische  Re- lativ vertritt  lat  cuius  (s.  Sp.  4  m.,  7  o.) ; vprihra-fiamla.. yahmi  ssire  mi'kriS.drujS aipi  (sd.)  vJ^is'i  jata  paurva  (Sp.  855  m.) maiyakutths  "(. .  in  quo  judicio  . .  sva.) in  cuius  judicio  .,"  Yt.JO.  80;  —  mii-rsm ...  b>r?jayat  {sA.)  akurö  ..  \ytAhi  kthrps Auraolayä\t.lo.^o.  2)  folgt; nur a)  im gAw.;  das  Relativ  ist  substantivisch; Ayat  nä  fryäi  ..  isvä  (sd.)  daidll  maibyö .  .  iava  rafmg  JrOxitDTum  (sd.)  hyat  .  . /rqita  Y.45.  14;  —  para  iyat  mä  ya (APn.)  min^  piriha  (sd.)  ßmaitt  ^.48.2;
20912:Nominativ  oder  dem  ihm  gleichen  Akku-' 12; —  Hat  mqm  fraguzayanta  ysi  i
21103:ai-^uV;;  S2J2.Ä  —  Vgl-  '>^:i'-  —  Pö.  (furj'-  a): cc  haiar»),  Npü.;  eirä  a,i;ar.  Sä,:  ya/B  yai/i. — O  Siels  mit  folgendem  n".  —  ')  So  auch  -  at statt  «m  t  -  Yt.  6. 3  lU  lesen?  —  3)  Unsicher; s.  aber  j'fl^J,  Sp.  1245  o. •  j.  ya'S'a,  j.,  g.,  p.  ya&ä  Adv.  imd  Konjn. Die  korrelativen  Demonstrativa  (Stverz.), die  im  Übergeordneten  Satz  erscheinen, ferner  °cit,  "fVj' (Stverz.  Sp.  590),  das  hinter y,  und  miinay)n  {ahe  oder  bä;  Stven. Sp.  1123  m.),  das  in  Verbindung  damit ■  id  durch  Sperrdruck  hervorge- hoben. I)  vergleichend;  I)  die  Aus- sage des  ^y'-Satzes  gilt  als  wirklich:  'wie, so  wie,  gerade  wie,  entsprechend  dem wie,  in  dem  Masse  wie;  als';  dabei  kann die  Aussage  im  y-  und  im  übergeordneten Satz  i)  verschieden,  2)  gleich  sein,  in welchem  Fall  das  Praedikat  meist  nur einmal  gesetzt  ist  a)  im  Ap.;  zu  i)  tyJ'säm adam  a'haham  ava''  *akunavayc^tä  y mäm  kSmJ'  skJ*  "was  .  .,  das  taten  sie, so  wie  es  mein  Wille  war"  D.  ff.4;  /?.  3; —  '^SsiJm  kacSm^  a'^oAyc^  ava'hä ^aiunavaya'tä  Bh.  7.  8;  —  y  mClm  kämi^ ava^a  dis  akunavam  Bh.  4. 4;  —  iyam yux'iya  (sd.)  akäniy  *ava%a  *y  adam niyastäyam  D.  //.  3;  —  adam  käram *gaiava  avastäyam  y'  paruvamciy  (nämt. ähefi)  ava%a  Bh,  i.  14;  l4^  zu  2): availäm  tiaiy  astiy  kariam  y  manä  (i^mL (tstiy  kartam)  Bh.<^.9.  b)  im  gAw.;  zu i):  kä  tsth'(sd.)  fyao'hanäi..y  *7'a  *haxmT \y :  dakyJusmaiy  duruvS  ahatty  Bh.  4-  \  (sd.)  Y. 34.  5 ;  —  a%S  nS  at?kat  y  hvö S-  a)  mit  OpL;  a)  die  Annahme  wird  wuja/  (sd.)  Y.2(j,4;  —  ydi  Jm  v!  nsit ab  künftig  möglich  hingestellt;  im  Nach-  i%3  mq'irfm  vartSintt  (sd.)  y  Tm  mSitiii^ä salz  steht  der  Opt.:  'oi  zT  ma  masyäka..  vaocacä  Y.i^5.3;  — yBt  it  a%ä  vtriwyqn yazayanta  .  .  fiä  s'usuyam  Yt  S,  1 1,  10.  y  Tl  (Sp,  367  0.)  aitl  Y.^ß.  6;  —  y  /a 55  (*'^0.  74i  —  •'^'  «f  >"S  ma^.lka  .  .  f  .  ,  mSngftScä  vaocascä  .  .  yä  vsha  ahs yazayanta  ..  api  niqm  ari.bint'ryqm  ..  tni  dadiWiahT '^.^g.^;  35.6;  —  *y  *aii aop  \t.8.2^.        b)  die  Aussage  geht  auf  I  (Sp.  9  u.)  i'kä  vansaia  yi  data  ofahsus
21384:bindung mit  dem  V,  yaz-  (auch  mit  frä); a.)  mit  lD3tr.  'Jemanden  (Akk.)  mit  Gebet, Opfer  usw.  verehren,  feiern':  tarn  yasüi surunvata  °na  tarn  yazäi  huyalta  'na arxivTm  Yt  5. 9 ;  j.  1 8,  Y.  57. 3 ;  —  y^i  zJ mä  ma^äia  aoxtö.nümana  'na  yazayanta yäka..  YLÄ  11;  II,  23',  24',  10.  30,  31, 54'.  56;  —  sraofpm  . .  yazamaide  paoiryaca 'na  upamaca  Yt, /j.  18;  —  kana  %wqtn *na  yazäne  kana  'na  fräyazäne  Yt,  5.  90, ^5'54i  J7-6i'.  V. /().  i7'*>,  Vyt  20',  21; —  wertlos:  'na  miira  .  ,  /rayazänti Vd.5.  ß)  mit  Akk.  'Verehrung,  Opfer darbringen;  Gottesdienst  verrichten':  yi? nä  mazistfm  'mm  yazaite  Yt  j.  24  (s.  Sp. 1237  u.);  —  zaota  . .  pmnimca  bar?sma (sd.)  staränS  darr^imca  'nsm  yazSnS  Yt. IQ.  138.  A)  mit  kaptankätay-  Adj.  'der siebenteiügc  K',  d.i.  Y._J5.3— 4^.6:  sraoitm .  .  yaike  akunö  vairyS  snaihi/  vTsa/a  .  . 'nasca  Aapta/fkäitts  fsB^asca  mq'^rS  .  . vUpäsla  yasnd.k9r>tayS  Y.  57.  22;  —  yezi .  .  akunavajca  *ga%anqm  srävaytiti  'mmca
21440:yas3  ('wie  sva.  womit')  hwä  yazata vTstäsps  Yt77.  61;  61,  5.90,  91,  /5- 54, V.  75.  17,  Vyt.20,  3/;  — ka%a  zaota  xsäta apB ..yazäile  Y.ö^.g;  —  tim  yazät surunvata  yasna  sraol»m  . .  zaokrabyB  (DP. statt  IP.)  Y.57.  3;  Yt.>  18,  70.  31 ;  —  yö aHm  yjzäite  zaohräbyB  Yt/7.  2;  2,  8.\, 10.6,  Y.68.10;  —  yatal^a  mqm  zara- ^uära  ..  zaokrräbyS  Yt  /.  9 ;  mangelhaft  zitirt F.4g; — hvanx^aitim ..yazamaide  haomays gava  barismana  .  ,  zaohrabyasca  arsux- öaäbyasca  vayzibyS  (DP.  statt  IP.)  Ny.  7. 1 6 ; —  yazayania  %wqm  mazdayasna  pasubya staoraHbya  vayalibya  pataraialibya  (sd.)  Yt 10. 1  \(j;—ultaiaiiya  (LS.  statt \%.)ca  vTspnn asavamm  .  .yazamaide  Vr.  18, 2.  b)  Akk.; tarn  yazata  kaolyaahü . .  sat)m  aspanqm  . . hazaisr)m  gavqm  "ihr  opferte  ff. . .  hundert Rosse, .."  Yt. 5.  21;  p.  ag;  —  tarn  yaztnta .  .  hunavB  .  .  sat>m  aspanqm  Yt  5.  57; 72.  c)  paiti  mit  Gen.(?);  yqm  yazata zara'huitrS  humatahe  paiti  mananhS  Yt 16.  6.  2)  mit  Angabe  des  wozu?  durch
21630:•  j.  y^varvna-  n.  'Stössel'  (des  Mörsers): yai^qm  zayanqm  vastrytke  fsityantU  . .  °mm zgfTfsnö.va-fiarum  ". .  ein  StÖssel  mit  rund- lichem Kop&tUck"  V. /4. 10.
21965:ximaibyä  (Sp.  1303  m.)r  at  vS  xsmaibya asBna  vaOia  ..  Y.28.  10.  zu  2);  vgl. fl/  No.  2 :  maHs  at  vi  drtgoatS  mdkrqsla güsta  sasnät(sd.)cä  Y.31.18; — aAuroAyä ai  v!  mazdä  yasmmca  . .  Y.^5.  7 ;  —  tat at  v!  vfnzyamahJ. .  Y._J5.7.  ni  a)  j.  vS Akk.-Gen.-DaL;  zu  i):  vjse  vS  atmsa sffnia  stoüta  Vr.5.  i ;  —  JamySi  vS  vara- kaot  var»hB  Y. 55,31;  F. 2  d,8;  — mS  vS jamyat  akät  aio  Y.  35. 31;  —  aat  vS kasHt  masyanqm  :^armB  isaita  Yt.jp.S3; Vr.  j.  S ;  —  a  vS  aiiihe  fi-iüa  stuye  nT  vB vaMayani  Y.  7.  aa;  —  usta  ä.baväi  dai^ havB  US  vS  apqm  alavB  . .  jasänti  Yt  <K 2  9 ;  V,  JÄ 1 6 ;  —  imat  v  B  aps  Ja&yemi  Y. 65-12; — yl>  vB 3pB ..yazaite Y. 68. 10;  — yBi  vB  vatfUÄit  . .  «Bit  ätSrayeräe  Yt  13. 30;  —  yeAhä  v5  ai^B  usirBJtanis  (sd.) aahat  V.  15.  25  (?);  —  ioAe  vd  urva  fra- yayai  Yt  13.  $0;  —  ya'^ra  vB  ahurB  .  . frada'him  6axsatF.4b; — yai  vB didvaisa Y.I.32;  aa;  —  ähra  vB  buyans  masäna Ny._?.  11;  11;  —  apd/  Istlm  vB /aiiyami Y.  65. 11;  11;  —  wertlose  Stellen:  Vyt <?,  Az.5.  niB)  j.  p?  Gen.-Dat";  zu i):  ramB  vS  ga^ä  asaonis  Y.28.0;  — firä  vJ  rähl  am)sa  spmta  yastvmia.. Y.Ji.  18;  —  sonst  unmittelbar  vor  am^Jä spintä:  pairX  vi  am'  sp'  .  .  da%qmi  . . ultatum  Y.  7j.  4;  —  vuai  vf  am'  sp* slaota  Y.i4.i;42.i;  —  mms  vJ  am' sp'  tiy.i.r.
22359:Diktum'  (sva.  'vak-  a);  a)  im  gAw.:  °(5 srüidyäi  (sd.)  Ayat  mar>talibyS  vahisUm Y.*(5-5;  —  agusts{%A.')  'ch  sPnghämaht aHbys  ysi  . .  at'it  aHbys  vahüta  yöi  .  . Y.31.1;  —  yastum  mazdn  xsmävats  at vä  ala  staomyä  (sd.)  'ca.  Y._jy.  8;  — »niuxhäi  'catshqm  xsayamnd  (sd.)  hiwS vasS  Y.ji.  19;  —  imH  at  uc^ä  °M  .. fravaocämä  Y,_J5.  9;  —  at  vJ  vayci  (sd.) aKkaitt  apSmtm  'csX.^.l.  B)imjAw.'. ahe  'cB paityesti ..upa.vazata  *nairy3.sat»Ad \ V.  22. 13;  —  bfnzyaogit  'cö  räzayan  (sd.) V,  8.  100;  —  äaX  . .  kqm.räzayata  äiars.A ttiti  °cSbll aojaiUS:  tinja ..  Yt  1^,49 f.;  5-76,1
23016:hatqm  syaohananqm  vahiHa  ^.3^.3;  — avat  "voAvar/te  nqma  yat  vohä  virtiyami Yt  75. 44;  —  humataii  mainimna  hüxtail mrvats  hvarsiais  vinzyantB  (NP.)  Y, 70.  4;  Yt  70. 106';  —  humatanqm  hüxta- nam  hvanstanqm  ..  vpr^zyamnanafn^ä vavfnzananqmca  Y.J5.  a;  —  vJspaca hvarsla  ,  .  iyadhna  .  .  •uaritaca  vans- yamnaia  Y.  57.  4;  —  manya  manavAs humat>m  .  .  Aisva  mrBili  Aäxtsm  .  . zastalibyB  varx!a(_aS.y^  Avarltim  *Syadhrum Aog.  27;  Gs.  ;5j;  —  voAu  .  .  hvarit>m fyaohmm  vtrizimnim  V.J.  41;  —  sps- nistä  (APn.)  armatsil  Audänvansvä  3'  Y. 53- V>  — "  y^*  '"'  *'  "^'^  '^^  mq%nm Tiaryffntl(Kon).)  ya'äa  Im  mSnaica  vaocaca "die  von  euch  das  Wort  nicht  so  be- tätigen, wie  ich  es  denke  und  sage"  Y. 45-  3 ;  —  staota  yesnya  yazamaide  .  . manmna  vpr^zimna  (APn.)  *sixhmna sacayamna  Y.  55. 6;  —  kimcit  .  .  aoi marfntim  *v3r?zyant»m'''^  sixlmttm  saca-
23038:"  ■*■].,  g.  varazayant-  Adj.  'wirkend,  werk- tätig': a(  Jraziax/yä  ,  .  palarSm  vaishSu/ 'yantB  manatths  "ich  will  reden  , ,  von dem  Vater  des  werktätigen  VM"  Y. 45.4.  Unklar:    kqstrtm  paiHlAimim
```


## [2026-09-05T20:55:48.017Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 5865,5900p HRN.txt && echo \"=== dai/dei month ===\" && grep -n \"Monat\\|dai 'W\\|dai =\" HRN.txt | head -30",
 "description": "Horn 666 zemistan"
}
```


### [2026-09-05T20:55:48.074Z] TOOL RESULT

```
Muss dialektisch sein, da die reguläre Form np.
dehan (No. 589) ist.
664. i^elTi, zalü 'Blutegel', zerü (AM. 180 Zeile 2 v. u.).
skr. LW. (?) Jalüka-, jaluka-, Jalikä- 'Blutegel*
(Bütticher, Arica 67).
kurd. zdü, zuliil, zalüg, zürT; af/. LW. zallü 'Blut-
egel', echt zavara\ bei. zaray (417).
Gegen Curtius' Zusammenstellung mit lat. hirüdö,
air. gil vergl. Hübsch mann, ZDMG. 38, 424.
665. zelle^ ziUe 'Grille, Heimchen'.
skr. jhillikCL', jhillU Grille, Heimchen' (Hübsch-
mann, ZDMG. 38, 424).
666. xeni 'Kälte', zemistan 'Winter.
aw. zyao- 'Winter', Gen. ziniö; phlv. zam 'Winter'
(vd. 2 (20)), zam(i)stan; ai. himä- 'Winter ; arm. vergl.
jiun 'Schnee', jmern 'Winter', jmerem 'überwintern
(H. No. 178).
oss. d. zumägy t. zimag 'Winter' (135); af/. zimai;
wa;^. zam, zamin (Adj.), sar. zainän, zamämn (Adj.),
si/n. zimjy zinj 'Schnee'.
) vt. 19, 42 ]int die neuo AuRfj^abe harözuiiem.
10*— 148 —
Daneben auch allgemein entlehnt, kurd. afy. zamistän,
bei. zamisiän, :^imisfän, zavistän (414), sar. zümistän,
yidg. zemistän.
Die Pazendlesung damistan ist belanglos und falsch
wie päz. damik statt zamtk (np. zemin).
667. ;s;emi: (Öähn. I, 134 Anm. 4, 178 Vers 877)'), zemm
*Erde.
ap. uzmaya[patiy ; aw. ^^äo 'Erde', Gen. zemö; phlv.
zamlk; ai. //wtt- auf der Erde'.
af/. zmaka 'Erde*; oss. d. zän/ä, t. zä/ (127); sar.
zems, siyn. zemc,
LW. bei. zamtk 'Felder, Saaten' (415); ausserdem
ist np. zemm^) allgemein entlehnt (vergl. bei. No. 298).
668. ^en *Weib'; zenber 'Sänfte''-).
=== dai/dei month ===
255:(Monatsber. BAW. 1879, 463), paikka- Tussoldat' zu np.
5958:Stack elberg, Baltische Monatsschrift, XXKVIII, lieft 8, 674).
6147:(Nöldeke, Monatsber. BAW. 1883, 1100).
6718:Weber, Monatsber. BAW. 1879, 812).
8390:968. '»nah, meh *Mond, Monat' ^).
8391:ap. müh' 'Monat'; aw. mäh- 'Mond, Monat*; phlv.
8392:mäh; ai. mds- 'Mond, Monat'; arm. amis- 'Monat' (H.
8394:kurd. LW. meh 'Mond, Monat'; afy. tarög[mair
8396:mm 'helle Nacht', miyOst 'Monat' (aus *mai]astj Darme-
8397:steter, CXXIII); oss. d. mäyä, t. mäi 'Mond, Monat'5
8407:vier Bedeutungen : 'Mond, Monat, Mondgesicht, Medien' lesen.
8410:Nöldeke bei Weber, Monatsber. BAW. 1879 S. 812 als 'raedisch*;
10004:ap. a- in Anämaka' Monatsname (?) ; aw. a-, an- ;
```


## [2026-09-05T20:55:49.074Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB zam/zim ===\" && grep -n \"zamistan\\|zemistan\\|zimistan\\|zyao\\|zim<\\|zima\" HUB.txt | head -30 && echo \"=== HUB dai ===\" && grep -n \" dai\\b\\|dai '\" HUB.txt | head -20",
 "description": "Grep Hübschmann"
}
```


### [2026-09-05T20:55:49.141Z] TOOL RESULT

```
=== HUB zam/zim ===
=== HUB dai ===
4846:*) Wrzl. arisch rfai, dai (ana (foij, di, s. mein Vokalsystem p. 27
```


## [2026-09-05T20:56:05.707Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'Winter'\\|,Winter'\\|Winter’\" BRT.txt | head -40",
 "description": "Grep BRT Winter"
}
```


### [2026-09-05T20:56:05.756Z] TOOL RESULT

```
3797:•  j.  aiwLgäma-  m.  r)  'Winter';  fra  hama (stL)  iocinte  aHa  'me  V.j.io;  —  hama.. °me  "während  des  Sommers  . .  im  Winter" F.  2jb;  V.5.4a,  75.45,  "-^.46,  47,  4^'\ $0,  j/,  103'.  3)  sva,  'Jahr':  hasannm •manqm  Yt().  lo;  ig.2^,  V.  2.41.
27723:•  j.  'zayan-  :  zaitt'  m.  'Winter':  ■_ytf(NS.) ava%a  s/axrff  {sd.)  yat  ..  FrW.<y.  2;  — yal  vä  hama  . .  yat  vä  aete  (näml.  masda- yasna)  zaOta  (IS.)  V.i6'.  12.
28266:•  j-.  g-  zyana-  dl  'Winter':  staxtü  mrSrS jya  (5lS.)  V.a.a»;  —  aoa  tyasatQiS.) pairi-paiaüi  aoa  fral^m  vsifnanqtn  (sd.) V.J. 3;  —  «yamÄ  (AS.)  dalvdJÜbm  V.
```


## [2026-09-05T20:56:06.922Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT zam ===\" && grep -n \"zam-\\|zām\\|'earth'\" KNT.txt | head -20 && echo \"=== PHD zam ===\" && grep -n \"^zam\\|zamistān\\|zamestān\\|^dai\\|^day\" PHD.txt PHD_mackenzie.txt | head -30",
 "description": "Kent and MacKenzie"
}
```


### [2026-09-05T20:56:06.983Z] TOOL RESULT

```
=== KNT zam ===
408:$11. Diaugcr MIXTURE IN THE OP VocaBU- LARY: it is difficult at times to decide what is genuinely OP and what is borrowed. Of the two words for ‘good’, nazba- is a religious term, and vatu- is found only in proper names. Of the two for ‘earth’, zam- (which would have Med. 2) appears only in the form zm-, which is phoneti- cally OP as well as Median, and occurs m one proper name and in an official term for execution with torture; būmi- occurs chiefly in phrases of official character, but is used also in DSf to de- note the earth which was excavated for the palace of Darius. On some other points, the usages of Pahlavi seem to inform us: nom. hau» ‘he’, «yam ‘this’, prep. hadd ‘with’ belong to Pahlavi of the Northwest and not to that of the Southwest, and thus are shown to be borrowings from Median.!
1774:йр- ‘water’, zíap- ‘night’, xfnau- in u-zfnau- ‘well satisfied’, gau- ‘cow’ in compounds, bard- ‘year’, dwar- ‘door’ in duvara-, nar- ‘man’ in üv-nara-, nàv- ‘ship’, паћ- ‘nose’, pad- ‘foot’ in nipadiy etc., vas- ‘wish’ in adv. vasiy, vib- ‘house’, séd- in upa-stá- ‘aid’, zam- ‘earth’ in u- zma- etc.; perhaps napdl- ‘grandson’, an old pIE word, probably a compound; possibly dà- in ‘wada- as element of Paisiyà-uvüdà-, and vaj- in gen. daha-vaja. $143. Noun AND ApjectivE STEMS WITH THE-
5212:Uvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-18, Akk. þu- ma-ri-iz-ma-’, Gk. Xwpaspin, Av. asf. z'airizom. From u- ‘good’ + vāra- ‘0° (8126, 5148.111), + ami- (§95, $120, 5152.) to zam- ‘land’. See also Uvürazmiya-. Uvirazmiy nsf. (SI79.1; Lg. 19.223) DB 1.16, DPe 16f; Uvārazmiš DNa 231, DSe 22°, DSm 9°, XPh 21f. Uvārazmiyā арзї. DSf 39f.
5226:uzma- adj. as sb. ‘that which is up from the earth, stake’: from ud- ‘up’ + zma- to zam- ‘earth’ ($84, $95, $120, $130, §142, 5148.11, VI): other- wise Wackernagel, KZ 61.208; Lommel, OLZ 37.180.n2; König, RuID 72. uzmayā-patiy lsn. DB 2.76, 91; 3.52, 92.
=== PHD zam ===
PHD.txt:676:zamān 98 zāyistan
PHD.txt:677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
PHD.txt:1479:daily rozwārag.
PHD.txt:1480:dais šādurwān.
PHD.txt:1497:day rēz; — and night r6z-šaban.
PHD.txt:1498:daytime tēzgār.
PHD.txt:4320:winter zam, zamestān.
PHD.txt:5338:zamig
PHD.txt:5341:zamigpaymünih AU росу gn?
PHD.txt:5342:damidan mir-! murdant uštar! gow-t guftan™ gow-! guftant zamestān damišn. yask dastyār dastyārīh
PHD.txt:5349:zamanag
PHD_mackenzie.txt:1953:daya~ [d'yk l I M d'yg-, N --a] (wet-)nurse.
PHD_mackenzie.txt:5743:zam [zm I P zmg] winter.
PHD_mackenzie.txt:5746:zaman [ODNA < A (dn); ;m)ll l , Z11l1l 1 1M zm)1I, N -] time, hour.
PHD_mackenzie.txt:5749:zamenidan, zamen- [z)myn-.:vtn' 1M z)myn-] lead, send.
PHD_mackenzie.txt:5750:zamestan [?1nst)n l I (M dmyst)n), N ......] winter.
PHD_mackenzie.txt:5751:zamig [z-, ?myk I M zmyg, N zami] earth.
PHD_mackenzie.txt:5756:zamyad ["'z)md)t l (misreading of z'my?dt l = zam-J'azd?) I M z'my'd,
PHD_mackenzie.txt:9720:zam
PHD_mackenzie.txt:9722:zamig
PHD_mackenzie.txt:9725:zaman                                   ,~       zadanI                    \\¥'\~
PHD_mackenzie.txt:9809:zamyad                     ,~
PHD_mackenzie.txt:10511:zamanig                    \\.)~      drafs
PHD_mackenzie.txt:10513:zaman                       ,~        drafs-                    - "'Ucz.}..
PHD_mackenzie.txt:10514:zamanag                    \~~        draf?iiuan          \\~~
```


## [2026-09-05T20:56:19.765Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 28255,28285p BRT.txt && echo \"===27715===\" && sed -n 27715,27735p BRT.txt",
 "description": "Bartholomae zyā- and zayan- context"
}
```


### [2026-09-05T20:56:19.850Z] TOOL RESULT

```
•  ).  zbanntam  Absol.'*  'beim  Laufen'  (in lAiAdscher  An):  jJ^/a  dai^hSui .  ,pat?nt3m (sd.)  i/J  »*•  wJ  Yt  75.50.
Zorn  V.  'liar-.  —  ■)  VgL  Bthl.  IF.  u.  348.
•  j.    zbarannA-  Adj.,  PPM.:   s.  '«Aar-.
•  j.  '''zbaiirvataDa-''  patr.  Adj.  'von Ziaurvant-  abstammend,  dessen  Nach- komme': karsnahe  •tanake  Yt  13. 106.
AbleiL  am  tiaimiant-.  —  1)  So  nach  F I,  wo •■vaitan* ;  NA.  mit  Mr3  tiaurviu%in- ,  ai  ist allerdingi  uifTäUig.
•  j.  zbaurvant-  m.  EN.  eines  Gläubigen: •pais  osaBTtB  Yt/J.  106.
AbleiL  —  Eig.  Bed.  7  Anscheinend  PFzoA. Ob  in  u.  jvalitäl    Kaom  id  *tiar-.
•  j.  zbätar-  m.  'Rufer,  Anrufer  (der  Gott- heit)': vise  vs  anusa  tptnta  staeta  taota  °ta yaiia  Vr.5.  i,  Y./4. 1  (wo  *'3);  —  ■»'«"- tar?ca    iaotanla    'tanca    makranaca    Yt
Ji-
;  kvitar-  m.  —   Pü.:  j'a-
j,  imanayA  N,  Zy:  lie»  itnan'.
•  j-.  g-  zyana-  dl  'Winter':  staxtü  mrSrS jya  (5lS.)  V.a.a»;  —  aoa  tyasatQiS.) pairi-paiaüi  aoa  fral^m  vsifnanqtn  (sd.) V.J. 3;  —  «yamÄ  (AS.)  dalvdJÜbm  V.
|j.a,   19;  ig.AZ,  F.20;    —    «wJ  (GS.)'J
\daaödälahe  V.  7.  »7;  —  /lucii  ttmB^'* ifAr/(sd.)  atwigaitlvt  V.p.  6;  —  ^r9 **3mg^^    V.2.a4;   —   «ob    *s^««itif')  «>
iffldt'äfffi  a}>a  *z^maAe'>  ^t^r^talmW.t.^;
I  —  avi  oAttm  . .  ayjm  (sd.)  *3^me'*  (NP.)
■.jat?h>ntu  V.  3. 2  a  *.      a)  GS.  mit  ptnUtv-  m,
I 'Pforte  des  Winters',  Name  einer  Öitlich- keit:   nHi  tä   im  xshäus  vaipys  (sd.)  . .
\ptntS  stmB  Y.5/.  II.
'      KompE.;  Ableiu  —  Vgl.  auch  tayaii-.  —  ai.
1      Um- ;    np.  tan ;    arm.  tiuH  (woid  Hbm.  AGr.
'  T.  471).  —  Pfl.!  aim,  tamailän.  —  ')  W^en *""'  veI-  S  90.  3-  NA.  hat  mehrmals  in*, aber   7   ist    überall  besser  bezeugt;   s.  auch
.      omaia-.  —  ■)  Them.
•  j.  zyä.;  p.diyä- V.  'schädigen'.  Praes.  1 1 \sina-,älf^ä•■.äln''^,3^  (Pass.) ya-";  Perti \*üy.  —  PPfP.  äOa-'^i  Int  syänai.         S.
noch  "syat.
i)  'Jemanden  (Akk.)  um  etwas  (Akk.)
schädigen,  benachteiligen,  bringen':  /J  mam
tat  draond  einä/  vä  tnjyat  vä  apa  vä yäsäüi  "wer  mich  um  diesen  Anteil  bringt,
ihn  mir  stiehlt  oder  wegnimmt"  Y.  ;r.  5;
—  I  xsah'^am  ty<^  gaumätt^  .  .  adinl^  •> (^SPrA)  ki^büjiyam  "die  Herrschaft,  um die  C.denX  brachte"  Bh.i.  11;  12, 14;
—  xlai^amsim  adam  adlnam^'  Bh-J.  13;
===27715===
•^■«1- Adj,,  lamV-gaoi-;  ai.  vgl-.fvia  Adv.'im Versteck'.  —  Pü,:  andar  tamik  nikän.  — ')  So  Yt  75.  81.  NA.  um',  aber  gegen  alle guten  Hda.  —  ')  Hier  sam',  s.  No.  I.  — 3)  Tbem.
•  j.  zamb-  V.,  nur  mit  harn  'zermal- men'.    Piaes.  30  (Iter.)  zimbaya-.
'zermalmen,  zertrümmern';  harn  *zagna (sd.)  sf/nbayahtiim'^  "zertrümmert  ihre Waffen"  Yt  /.  27.
ai.jaiiiAiij'.i/i,  l'Ds.  vkamham  'ich  zerquetsche'.
—  Vgl,  vha/iiia-.  —  Pü.;  hamäk  hac  aivz'\r i  tö  valdenän  rSi  iiaslak  afe  kunc.  —  ')  Vgl. die  Var.,  bes.  E  I.  NA.  hat  kqm  ;^nva  tim- bay-  mit  Mf3;  s,  aber  Pu.
•  j.  zaya-  m.  'Gerät,  Ausrüstungsgegen- stand': vlspe  •>«(AP.)  dhaurune ..yat^am •yanam..  V./4.8;  9,  10;  —  äat  kl  zaya (AD.)  frabanm  .  .  suwrqm  .  .  a^trqmca V.  2.  6.  a)  insbesondere  des  Kriegers 'Waffe'  (zum  Angriff):  va^nm  .  .  a»ia- vastitmin  'yanqm  ■v>rihravast»ni?>n  *yanqm Yt/0. 133*';  —  kana  »lya  (IS.)  hukirs- iäfjie  (sd.)..  V,;p.8;9;  —  mana 'ya  asii vahistiitt  (Sp.  1402  u.)  V.;p.  9.
KompE.;  Abieil.  —  Vgl.  :a7na-.  —  Pii.:  lac.
—  ')  Vgl.  Yt.  10.  96  und  V.  ig.  15.
•  j.  'zayan-  :  zaitt'  m.  'Winter':  ■_ytf(NS.) ava%a  s/axrff  {sd.)  yat  ..  FrW.<y.  2;  — yal  vä  hama  . .  yat  vä  aete  (näml.  masda- yasna)  zaOta  (IS.)  V.i6'.  12.
Ableit.  {zayaiia-\  —   np.  dai.  —  Vgl.  cyani-.
—  ztün-a  '.  ai.  Aiman ,  gr.  x"/^^'  =*^  j-  aln-e  \ ai.  aJttiaa,  gr.  äx/iüit ;  s.  noch  irayan-,  masan-. Dazu  JScHUiDT  Kritik  87.
•  j. 'zayan-  Adj.  'bewaffnet':  mtkrjm..hu- zamtm  a^armatsukasUmim  'yanqm  v?r»- '^ravashmim  °yanam  V.  ig.  1 5  '*.
Abteil.  (^ayS.l^^ta■^y  ~  Ableit.  au»  saya-.  — Pa.:  zay  (wie  für  saya-).  —  ')  Vll.  sind  die Worte  x'ann'  nur  ungeschickte  Verpflanzung aus  Yt.  10.  132;  s.  aber  nayö-luna-.
•  j.  zayana-  Adj.  i)  'winterlich':  dasa  ava- ^ra  maahs  °na  (NP.)  äva  hqtiiina;  hapla h>nti  hqmittB  mär^ha  patüa  'na  a^kar? (Sp.  ISS3  u.)  V.i.3  und  3PuZ.  a)  n. 'winterliche  Zeil':  Aama%a  (sd.)  . .  Aqmi- mmca  'mmfa  Y.S^.^;  —  at  Aama  at °yme  Y.16. 10.
Ableit  aus  'layaii;  —  ai.  vgl.  häyanä-  (mit Vrddhih)  1)  Adj.  'jährlich',  2)  n.  'Jahr'.  — Fü. :  (/d)  sammtäH,
ob,Google
i667
zayö.t9ina-
•  j.  zayö.t»ina-  Adj.  'der  bestbewafibete' : ks  asti  . .  yatatanam  'mö  Yt  14.  i.
Superl.  am  *zayan-i  y^  gamäJima-.  —  KpQ. : Hlib  ba  yäri  rasandalar.
•  j-,  g.  zav-,  zbä-'*  V.  'rufen'.  Praes. 2  sava-,  5  sBm>;  ^  zaosav,  5  +  7  zao- tftv-'>,  24  tiaya';S' AOT.  x  zävii'-.  —  PPfP. 'tbata-;  PFP.  'saoya-.
```


## [2026-09-05T20:56:20.564Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN 1014 winter ===\" && grep -n \"WINTER\" SYN.txt | head && grep -n \"14.7\" SYN.txt | head -20",
 "description": "Buck winter section"
}
```


### [2026-09-05T20:56:20.621Z] TOOL RESULT

```
=== SYN 1014 winter ===
24329:WINTER
25744:WINTER SPRING , éap a XELPOV é Cr eves ee i pa led rimavera Late jnverno lad It. hiver printemps Ir. invierno primavera Sp. jarnd primdvard Rum. gam gemred errach ar qeim hreadh earrach Nir. gacaf gwanwyn y * gor nevez-amzer T. "
1969:1457. Puscariu 359.
5869:shining ball’. 1, IE *ok- in various formations. There are also verbal forms for ‘see’, as Skt, desid. ks-, Grk. fut. dpoua, perf. szwra, etc., but these are much less wide- spread than the nouns for ‘eye’. Walde- P. 1.169 ff. Ernout-M. 697f. Falk- Torp 1417f. Feist 64 f. Grk. doce (dual, poet.); duua mostly poet., but also sometimes in NT and pap., whence through dim. éupartov the NG part; 6¢9adpds, the usual prose form, prob. a cpd. with second part related to $aXauos ‘inner room’ and orig. used for the socket of the eye; dial. dxradnos, érritos, formation unexplained; Lat. oculus, whence the Romance words (also the Tare Ir. ugazl ‘eyes’); Goth. augo, OE éage, etc., all the Gmc. words (diph- se erolained in part by influence of tities a ; Goth. ausod, etc.? but con- Lith os this group denied by some); ti Bae Co Reng acs, ChSl. ete. oko (obs. 8.); Skt. aksi, gen. sg. aksnas; Av.
6720:‘blow’ (10.38) ; Sp. resollar, Rum. rdsufla (whence sb. rdsuflare), fr. new cpd. parallel to Lat. resptrare. REW 8430. Puscariu 1447.
10403:ON feldr : Lat. pellis, OE fell, etc. ‘hide’ (4.12). Walde-P. 2.58f. Falk- Torp 1457 f.
11354:Fr. brosse (OFr. > ME brusshe, NE brush > NIr. bruis, W. brws), Sp. bruza, same word as OF’. brosse, broce, MLat. bruscia, brossa, ete. (cf. Du Cange) ‘brush’ = ‘brushwood’, with sec- ondary application to the utensil made therefrom—orig. dub.; borrowing fr. a word of the Gme. group (ON bursti, ete., below, 4) now generally rejected. REW 1340a (but Sp. bruza fr. Goth., 1417), Wartburg 1.572 ff.
16367:ON prefix aud-, as in aud-ser ‘easy to see’, aud-sdlir ‘easy to get’, etc., OE éape, éapelic, ME ethe, OHG odi, MHG ade, prob. same word as Goth. aus (or aupeis), ON audr, OHG ddi ‘uninhabit- ed, empty’ (NHG éde), with develop- ment through ‘free from difficulties’. NED s.v. eath. Weigand-H. 2.380. Otherwise (as orig. ‘willing’ : Skt. av- ‘favor, help’, Lat. avére ‘desire eagerly’, etc.) Falk-Torp 1407 (Walde-P. 1.19 with doubt).
17684:Lith. vyti, Lett. vajat, Av. 3sg. vayertt, 3pl. vyeinti, etc. (Barth. 1407) : Skt. 3sg. veti, 8pl. vyanti ‘seek, approach eagerly’, Grk. teuar ‘hasten, be eager’, etc., IE *wei-. Walde-P. 1.228 ff.
18276:\" gs HG reita ‘carriage’, Ir. ria- Walde-p, Pa ete, ‘ride’ (10.66). i ; aoa us, Gallic word = Ir, MW Currere oon ‘Lat. currus ‘chariot’, 14o7 ir ete. (10.46), Walde-P. ieee eM. 157, Walder Hence | f, (Mostly «a? SP+ carro ‘cant? Th. iz _ chariot’, ete. cart’, Fr. char
24172:NHG dreifach (late MHG zwivach, eto.), cpd. of fach ‘compartment, part’, ete, (MHG vach also ‘fold’ of a garment, hence use in place of -valt), OHG fah ‘yall’ = OF fec ‘interval of space or time’: Grk. amfyvipe ‘fix’ (cf. ad—rat ‘once’), etc. Walde-P. 2.3. Weigand-H. 1487. Paul, Deutsches Wtb. 152. Kluge-G. 142.
24305:14.53 14.61 14.62 14.63 14.64 14.65 14.66 14.67 14.68 14.71 14.72 14.78 14.74 14.75 14.76 14.77 14.78
24349:Grk. &pa ‘period of time’, in Hom. esp. ‘time of year, season’ or ‘fitting time’, later esp. ‘time of day, hour’, but wider use continued in part (so even NG kap- moon pa ‘considerable time, quite a while’) : Av. yara, Goth. jer, ete. ‘year’ (14.73), Slavie jaro ‘spring’ (14.75), all prob. fr. *yé-, yd- beside *yd- (cf. Skt. ya- ‘go’, Lith. joti ‘ride’, etc.), extensions of ei-, i- ‘go’. Walde-P. 1.105. Boi- sacq 1083.
24366:melai ‘year’, see 14.73.
24443:réros ‘year’, etc. (14.73), as orig. ‘full —
25292:tainly those of the large inherited | léto ‘year, summer’ (14.73). Walde-P. ze denoted the -bright ‘day’ vs. | 2.427. Pedersen 1.133. Thurneysen, ie Kit and only secondarily (like ‘sum- | Gram..35, 180. Pokorny KZ 50.43 if ne ss ‘winters’ for ‘years’) the com- (taking lae as of different orig., but cf. wehensive 94-hour ‘day’ (for which | Vendryes, RC 42.234 f.). Dan., Sw. have distinctive forms). 4. Goth. dags, ON dagr, OE deg, 1. Derivs. of IE *dei- ‘shine’, rare in | OHG fag, etc. general Gmc. (also derivs. verbal forms (Skt. 3sg. imperf. adzdet, Goth. fidur-dogs ‘of four days’, OE dégor etc.), but widespread in words for ‘sky, | ‘day’, ON degr ‘12-hour period, day or heaven’ as Skt. nom. sg. dydus and the | night’, Dan. dégn, Sw. dygn (the last two personified Grk. Zebs, Lat. Iupiter, Iovis; denoting the 24-hour day), etym. dub., ‘god’ as Skt. deva-, Lat. deus, etc.; and | but perh. (despite phonetic difficulties ‘ay’. Walde-P. 1.772 ff. Ernout-M. | with the gutturals) : Lith. dagas ‘(sum- 268 ff. Walde-H. 1.350. Here as ‘day’. | mer-) heat’, OPruss. dagis ‘summer’, Skt. a) IE *dyeu-, *diw-, etc. nidagha- ‘heat, summer’, fr. the root Lat, digs (> It. di, OF r. di, Sp. dia, | *dheg*h- in Skt. dah-, Lith. degti, etc., Rum. zi); Ir, dia, die, W. dydd, Br. | ‘burn’, and also (with init. doublets, as deiz; Skt, diva- (in dive dive ‘day by day’, | Skt. agru-, Lith. asara : Grk. daxpu otherwise divasa-); Arm. tiw. Lat. deriv. | Goth. tagr ‘tear’, etc.), Skt. ahan-, Ay. adj. diurnus ‘of the day’, late sb. diur- | azan ‘day’. Walde-P. 1.849 f. Walde- mm > Fr. jour, Prov., Cat. jorn; It. | H. 1.467. Falk-Torp 183, 176. Feist ee vs. di perh. due to lit. influence | 113. ea or Fr. REW 2632, 2700.| 5- Skt. gat Caisse ae il ae 3.71f., 105f. Bonfante, | instr. sg. ahna, etc.), Av. se . Sg. “74 59.877 ff. (with refs.). asni, etc.), see above, 4, with reis. b) With nasal suffix. Av. ayan- (nom. sg. ayara, gen. 8g. aes Lett. diena; ChSl. dint, ete., | war ete., neut r/n stem. like Skt eral Slavies Skt. di in epds.): | 2a" above), prob. : Grk. fier ‘in the Me ed (eap. in epds.); ning’, Goth. air, ON ar, etc., ‘early’, » tre-denus ‘triduum’, Goth. sin- he eee z
25680:14.71 MONTH
25690:14.72. Names of the months. Pre- vious to the widespread, though still in- complete, Eur. adoption of the Lat. names, there was the utmost diversity. In ancient Greece alone there were doz- ens of different local calendars (cf. Pauly- Wissowa 10.1575 ff.). There was no agreement between the old Gmc. names (even the OHG lists vary somewhat), nor between Indic and Iranian, not even be- tween the Ay. and OPers. names. Nei- ther the modern Lith. literary names, a
25709:14.73 YEAR Grk, gros, buavrds Goth. jér, abn, alapbni Lith. metaz NG 0500s, ros ON @ Lett. gads lat. annus Dan. ar ChSl.  léto : pO Sw. dr SCr. godina coal OE géar Boh. rok Ru eg ME ~ yeer Pol. rok ie Pe NE year Russ. god Nir Dliadain Du. jaar Skt. vatsara-, varsa-, ha- V . bliadhain OHG jar yana- Br, lwyddyn MHG jar Ay. yar-, sarad-, aeons NHG jahr OPers. @ard-
25724:Goth. jér, ON ar, OE géar, etc., gen- eral Gmce.; Av. yar- (nom. sg. yara); Grk. wpa ‘period of time’ (14.11), ‘hour’; Boh. jaro, etc. ‘spring’ (14.75).
25741:Skt. hdyana-: Av. zaén- ‘winter’, zayana- ‘wintry’, (14.74).
25748:14.74-14.77, Of the now recognized four seasons of the year, the ‘winter’ is the one for which there is the most im- Préssive agreement in the words denot- a ee in all the main branches of ther family except Gmc. belong to an to re group, pointing unmistakably an word for ‘winter’. For ‘spring’ ea there are less widespread which groups pointing to IE words tise ge ‘te probably used without pre- : i ean of the two. The earliest nee Was Presumably one of two sea- ‘ae - es and ‘non-winter’ (or in 5 oe dry’ and ‘wet’; but this chra der, eon, on IK relations). Cf. Seasons Hex. 1.529 f., and, for the n India (3 in the Vedic period,
```


## [2026-09-05T20:56:28.086Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 25748,25800p SYN.txt",
 "description": "Buck 14.74 winter discussion"
}
```


### [2026-09-05T20:56:28.131Z] TOOL RESULT

```
14.74-14.77, Of the now recognized four seasons of the year, the ‘winter’ is the one for which there is the most im- Préssive agreement in the words denot- a ee in all the main branches of ther family except Gmc. belong to an to re group, pointing unmistakably an word for ‘winter’. For ‘spring’ ea there are less widespread which groups pointing to IE words tise ge ‘te probably used without pre- : i ean of the two. The earliest nee Was Presumably one of two sea- ‘ae - es and ‘non-winter’ (or in 5 oe dry’ and ‘wet’; but this chra der, eon, on IK relations). Cf. Seasons Hex. 1.529 f., and, for the n India (3 in the Vedic period,
Digitized by Arya Samaj Foundation Chennai and eGangotri
1013 14.76 14.77 SUMMER AUTUMN Oépos POtvérwpov xadoxalpt P0tvorwpo aestas aulumnus estate aulunno été automne verano, estio otono vara toamnd sam, samrad fog(a)mar samhradh foghmhar haf hydref (cynhaeaf) haziv diskar-amzer, dilost-hanv asans Re sumar haust sommer efteraar (h¢st) sommar hést sumor herfest sumer hervest, autum(p)ne summer autumn, fall zomer herfst sumar herbist sumer herb(e)st sommer herbst vasara ruduo vasara rudens Zetva, léto jesent ljeto jesen. leto podzim, jesen lato jester leto osen’ grisma-, nidagha- ¢arad- ham-
later 5, 6, or even 7), BR s.v. rtu-, Zim- mer, Altind. Leben 371f., Macdonell- Keith 1.110 f.
14.74. ‘Winter’.
1. IE *gheim-, *§hyem-, etc., prob. with m-suffixes fr. *ghei-. Walde-P. 1.546 ff. Ernout-M. 451f. Walde-H. 1.645 f. Pedersen 1.66.
Grk. xedv, NG xeudvas; Lat. hiems (adj. hibernus, whence hibernum (tempus) > Romance words. REW 4126); Ir. gem-red (red: raithe ‘season’; Loth, RC 43.143 f.), NIr. geimhreadh, Ir. gam (for *gem, after sam ‘summer’), W. gaeaf, Br. goaitv; Lith. ziema, Lett. ziema; ChSl. zima, etc., general Slavic; Ved. hima-, class, Skt. usually hemanta- (also
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
zayana- ‘wintry’, Skt. hayana- ‘year’.
2. Goth. wintrus, etce., general Gmce., etym. dub., but perh. as ‘wet season’ : Goth. watd, ON vain, OE water, Grk. dwp, etc. ‘water’ (r/n-stem; for nasaliza- tion ef. Lith. vanduo). Walde-P. 1.253.
‘il Falk-Torp 1885. Feist 566.
3. Av. aiwigama- (mostly ‘winter’, also ‘year’), NPers. hangam ‘time’,
etym.? Barth. 89. Horn 248,
14.75. ‘Spring’. Apart from certain inherited groups, words for ‘spring’ are based on ‘early, fore-, first’ (time, year,
Summer), or ‘opening, beginning’. d ]
1. IE *wesr-, *wesn- (r/n-stem neut.), whence perh. in part also IE *wer-, Walde-P. 1.310f. Ernout-M. 1087.
Falk-Torp 1340.
Grk. éap, Lat. vér (cpds. > It., Sp. primavera, Rum. primdvard, OFr. pri-
mevoire; REW 6754); Ir. errach, NIr.
earrach (*wesr-ak-, with loss of w- by
Sentence phonetics? Pedersen 1.82, 435), W. gwanwyn (Pedersen 1.74); ON var, Sw. vdr (Dan. vaar, poet.); Lith., Lett. vasara ‘summer’, hence pa-vasaris ‘spring’, lit. ‘a kind of summer, quasi- summer’ (cf. Lith. pa-moté, Lett. pa- mate ‘stepmother’, etc.; Miihl.~Endz. 3.3); ChSI., Boh., Russ. vesna, Pol. wiosna; Skt. vasanta-, Ay. vanhar-; Arm. garun.
2. Grk.  avoukis ‘opening’, hence (opening of the flowers, ete.), NG ‘spring’, pop. a&vottn.
3. OFr. tamps prim (= Lat. tempus primum ‘first season’), Fr, Printemps (replaces Fr. primevére as ‘spring’ in 16th cent.), lit. ‘first season’. REW 6754. Gamillscheg 719. Bloch 2.318,
4. Br. nevez-amzer, lit. ‘new-time’ (cf. 14.11, 14.13).
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
——
mi ‘ Digitized by Arya Samaj Foundation Chennai and eGangotri :
; i]
i
1014 SELECTED INDO-EUROPEAN SYNONY MS
once RV; Macdonell-Keith, 1.110, 2.504, 507), Av. zyam-. Here also (fr. *Ghei-) Av. zaén- (NPers. daz) ‘winter’ and
5. Dan. voraar, ‘fore-year’.
OE lencten, ME lenten, lente (NE lent), Du. lente. OHG lenzo, MHG lenze, NHG lenz (poet.), also OHG len. zin, langiz (cf. lentzinmansth ‘March’) perh. orig. ‘having long days’ fr, Gro, langa- ‘long’ and -tin- : Goth. sin-leing ‘daily’, Lith. diena, ChSI. dins ‘day’, ete (14.41). Walde-P. 1.774. Klugeq 355. NED s.vy. lenten, lent, sb. 1.
NE spring, earlier in spring of the yere = ‘beginning, rising of the year’ (cf. day-spring ‘dawn’). NED sy.
NHG friihling, late MHG vriieline, fr. frith, MHG vrieje ‘early’ (cf. NHG dial. spdtling ‘autumn’). Paul, Deutsch- es Wtb.s.v. Kluge-G. 177.
6. SCr. proljeée, also Boh. podlett ‘early summer, spring’, lit. ‘pre-summer’ (SCr. Ljeto, Boh. leto ‘summer’),
Boh. jaro, Pol. obs. jar, jarz, old jaro, Russ.-ChSl. jara : Goth. jer ‘year’, etc. (14.73). Berneker 446 f. Brickner 199.
7. Av. zaramaya-, etym.? Barth. 1683.
14.76. ‘Summer’. Apart from the inherited group, several of the words are cognate with those for ‘hot’ or ‘burn’; some were orig. ‘spring’; one is ‘good season, fine weather’.
1, IE *sem-. Walde-P. 2.492 f. Falk- Torp 1107.
Ir. sam, W. haf, Br. ham, Ir. samrad, NIr. samhradh (sam-r-ad Pedersen 2.53, but -rad :rdithe ‘season’, Loth, RC 43, 143 f.); ON sumar, OE sumor, etc., general Gmc., except Goth.; Av. ham- (Skt. samda- ‘season, year’ rarely also ‘summer’, cf. Macdonell-Keith 2.429 f.);
Arm. am ‘year’. MA
J 2. Grk. Gépos, orig. ‘summer heat,
whence ‘summer’ and also ‘crop, hat- vest’ : Pépouar ‘become hot’, Skt. haras
Du. orjaar,
fre’, Tk. Gepuos ‘warm’, Skt. rene BY? oath etc. Walde-P. 1.687.
ghar roxalptor NG xadokaipu, lit. De eon! (xadds ‘good’ and xarpés ion season, weather’).
Ve 1a aestas (> It. estate, Fr. été; ; a Lat. aeslivus > Sp., Port. estfo) :
Fab in Grk. aifw ‘kindle, burn’, etc.
HL 1.20. REW 245, 248.
Rum. vard, fr. Lat. ver ‘spring’ (14.75); and Sp. verano, fr. deriv. VLat. (gloss) veranum (tempus). REW 9213, 9216. 4. Goth. asans (renders @épos ‘sum- mer’ once Mk. 13.28, otherwise Oepiopds harvest?) : OHG aran, etc. ‘harvest’, SCr. jesen, etc., ‘autumn’ (14.77). Walde-P. 1.161. ‘Summer’ prob. se- mantic borrowing fr. Grk.
5, Lith., Lett. vasara : Grk. éap, Lat. vér, ete., ‘spring’ (14.75).
6, ChSl. zetvua (renders both Gépos as ‘summer’ and Gepicuds ‘harvest’) : Zeti teap, harvest’, etc. (8.32). ‘Summer’ prob. semantic borrowing fr. Grk.
```


## [2026-09-05T20:56:41.347Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN hibernate/hiemal ===\" && grep -n \"^hibernate\\|^hibernal\\|^hiemal\\|^chimera\\|^hiems\" KLN_1966.txt KLN_1971.txt | head -20",
 "description": "Klein hibernate"
}
```


### [2026-09-05T20:56:41.404Z] TOOL RESULT

```
=== KLN hibernate/hiemal ===
KLN_1971.txt:45300:chimera, chimaera, n., a monster with lion’s head, 
KLN_1971.txt:113469:hibernate, intr, v., to pass the winter. — L. hiber- 
KLN_1971.txt:113610:hiemal, adj., pertaining to winter; wintry. — L. 
KLN_1971.txt:127269:chimera and cp. words there referred to. 
KLN_1966.txt:17764:hiemal,  adj.,  pertaining  to  winter;  wintry.  —  L. hiemalis,  ‘of  winter’,  fr.  hiems,  gen.  hiemis, ‘winter’.  See  hibernate  and  adj.  suff.  -al. hier-,  form  of  hiero-  before  a  vowel.
```


## [2026-09-05T20:56:42.307Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD gheiem ===\" && grep -n -i \"^ghei\\|^gheim\\|gheimn\\|hibernus\" AHD_watkins1985.txt | head -20",
 "description": "AHD Watkins ghei"
}
```


### [2026-09-05T20:56:42.362Z] TOOL RESULT

```
=== AHD gheiem ===
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
```


## [2026-09-05T20:56:49.904Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 113469,113490p KLN_1971.txt && echo \"--- 1966 leaf of hiemal ---\" && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('hiemal,  adj.,  pertaining')\nprint('leaf',t[:i].count(chr(12)))\n\"",
 "description": "Klein hibernate entry"
}
```


### [2026-09-05T20:56:51.715Z] TOOL RESULT

```
hibernate, intr, v., to pass the winter. — L. hiber- 
nat'(um), pp. stem of hibernare , ‘to pass the 
winter, to winter’, fr. hibernus , ‘pertaining to 
winter, wintry’, which is rel. to hiems (gen. hie- 
mis ), ‘winter’, fr. I.-E. base *ghei-, *ghi-, 
‘winter; snow’, whence also OI. himan , ‘in 
winter’, hemantah, ‘winter,’ himdh, ‘winter’, 
Hitt, gimmanza , ‘winter’, Avestic zaya(n)-, zy& 
(gen. zimo), ‘winter’, Arm. jiun, ‘snow*, jmern , 
‘winter’, Gk. x e ^ a > ‘winter, winter weather, 
storm’, x et ^ v » season of winter’, 
piv6? ‘wintry’, yicov (for ‘snow’. Alb. 

Gheg dimen, Tosk dimers, ‘winter’, OSlav. zima , 
Lith. ziemd, Lett, ziema, OPruss. semo, ‘winter’, 
OIr. gaim (for Celtic *giamo~), Mir. gem-red, 
‘winter’, Gk. x^M-^P 0 ^ ‘he-goat’, x'-P'-apa, x^~ 
{zaipa, ‘goat’ (lit. ‘a goat one winter old*), Toch. 
A cemdl, ‘goat’ Git. ‘a goat one winter old’), L. 
bimus (contraction of *bi-himos ), ‘two years 
old* Qit. ‘two winters old’), trimus (contraction 
of *tri-himos), ‘three years old’ Git. ‘three win- 
--- 1966 leaf of hiemal ---
leaf 392
```


## [2026-09-05T20:56:57.198Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer('hibernate',t):\n    print(m.start(), 'leaf', t[:m.start()].count(chr(12)))\n\" | head",
 "description": "Locate hibernate in KLN 1966"
}
```


### [2026-09-05T20:56:59.014Z] TOOL RESULT

```
1727879 leaf 156
4492078 leaf 392
4492102 leaf 392
4493825 leaf 392
4498462 leaf 392
4509652 leaf 393
```


## [2026-09-05T20:57:02.397Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\np=t.split(chr(12))\nimport re\ns=p[391]+p[392]\nprint(s[:600])\nprint('...PAGENUM markers:', re.findall(r'\\b7[0-9][0-9]\\b', s)[:20])\n\"",
 "description": "Check page numbers on leaf 392"
}
```


### [2026-09-05T20:57:04.131Z] TOOL RESULT

```
o  first  analyzed  it.  For  the  ending see  subst.  suff.  -ite.
hest,  n.,  bidding,  behest.  —  ME.  hest,  formed with  excrescent  t  fr.  hes,  fr.  OE.  his,  from the  stem  of  hdtan,  ‘to  bid’.  See  hight  and  cp. behest.
hestemal,  adj.,  of  yesterday.  —  Formed  with  adj. suff.  -al  fr.  L.  hesternus,  ‘of  yesterday’,  which stands  for  *hestrinos  and  is  cogn.  with  OI. hyaslanah,  Gk.  -/fttavjoq,  ‘of  yesterday’.  L. hesternus  derives  fr.  heri,  ‘yesterday’,  as  OI. hyastanah  derives  fr.  OI.  hyah,  ‘yesterday’,  Gk. X&eotvo?  fr.  of  s-m-  See  yester-.
...PAGENUM markers: ['726', '727', '728', '729']
```


## [2026-09-05T20:57:12.464Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport sys\np=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nprint('leaves',len(p))\nfor leaf in (487,488,489,491,492,493):\n    print('===== leaf',leaf,'printed ~',leaf+540)\n    print(p[leaf][:2500])\n\"",
 "description": "Borhan vol2 pages 1027-1033"
}
```


### [2026-09-05T20:57:14.192Z] TOOL RESULT

```
leaves 684
===== leaf 487 printed ~ 1027
  ‫زکاسه‬                                                                                         ‫سب ی ‪=4 ۲۰‬‬




‫باشد سیاه رنگه و آن‬             ‫‪,‬ی‬
                                 ‫نگ‬‫سیده‬
                                      ‫بتحتالی رس‬        ‫ثالی والث هم بمعنی دهان و کنج دهان است‪-‬‬
                             ‫وذام است ‪.‬‬
                                      ‫دافع قروح ج‬       ‫ودر عربی بمعنی بازداشتن وواداشتن باشد وحم‬
‫رفو ‪ « ۳‬بن اول وثانی بواو کشیده ‪.‬‬                       ‫اول وفتح ثانی هم‌درعربی بزر کث ومهتر‪ -‬وجوی‬
              ‫لان خوالند ‪.‬‬         ‫ردبی‬
                                      ‫عوین‬
                                         ‫با گ‬
                                            ‫واتر‬
                                               ‫زب‬       ‫بزرکه و رودخانة کوچك باشد ‪ -‬وبکر اول و‬
                                                        ‫سکون الی در عربی مایحتاج و مایمرف هافر‬
 ‫=روزن فلولیاء نام درختی‌است‬
                           ‫رفو نا ب‬                     ‫راگوبند همچو مشك آب ورخت خواب وبار و‬
             ‫خاردار» وآن نوعی از زقوم است ‪.‬‬                                  ‫اسداب وماند آن ‪١‬‏ ‪.‬‬
‫ر قیرف ‪ = ۴‬بنتح اول و ثانیبتحتالی‬                       ‫رفرین ‪ - ۲‬ضم اول * بروزن و معنی‬
                                                        ‫زرفن است > و آن حلفه ای باشد که برچهار‬
‫رسیده روای بی نقطةٌ مفتوح بزفاده » بزبان‬
‫ای باشد شبیه‬     ‫اندلس عنایر ا گوند و آن موه‬                                       ‫چوب در صب کنند‪.‬‬
              ‫بنجد وییشتر در دواها بکار برند ‪۰‬‬          ‫رفنی = بکر اول وسکون ثانی و نون‬



                                              ‫بیان بدازهم‬

                 ‫در زای نقطه دار باکاف تازی مشتمل بر دوازده لغت‬
‫صواب ‪۰‬‬       ‫زرکاب = بفتح اول بر وزن‬                  ‫زك ‪ -‬بنتح‪.‬اول و سکون انی» مخفف‬
‫که در دوات کنند و‬             ‫م رکب و سیاهی باشد‬        ‫زاك است ‪ ۵‬و آن جوحری باشد شبیه بنمك ‪-‬‬
                    ‫بعربی حبر ومداد کویند ‪. ۸‬‬           ‫و ضم اول خود بخود حرف زدن باشد در زر‬
‫رار ‪٩‬‏ = بفتح اول بر وزن هزاره »‬
                               ‫ک‬                     ‫‪-‬امر باین معنی هم هت کهبزکه‬
                                                                               ‫لب ‪ ۱‬و‬
      ‫مردم خیره و‪-‬تیزه‌کار ولجوح راگویند ‪۰‬‬              ‫وعوامگوبند‌بلند بضملام‪ -‬وبلفت زند وپازس(‪)۱‬‬
‫کراسه*‪ -‬نم اول وتح سینبی‌شله‬                                  ‫بمعنی آن باشدکه کلمة اشاره باشد ‪. ۷‬‬

                   
===== leaf 488 printed ~ 1028
 ‫سح‬    ‫هفش‬
                                                                                                                        ‫زکاشه‬

                 ‫تریج » اة سفالین بزرکه باشد ‪.‬‬                ‫ر وزن خلاصه ‪ ۰‬خاریشتی را گوبندکه خار های‬
                                                                                                       ‫ب‬
‫نم اول و فتح ثالی‌بر وزن‬          ‫زرگنف ‪- ۴‬‬

‫خجند ‪ .‬بمعنی ز کنج است که ‪6‬ه سفالن‬                                ‫اس باشیننقطه دار ‪ ۰‬بروزن و‬                ‫ر کاشه‬

                                                                  ‫معنی زکاسه |ست که خار بشت تیر انداز باشد »‬
‫‪ -‬بنتح اول بروزن ضبور ‪.‬‬                 ‫ز کور‬                                         ‫و با زای‌فارسی حم درست است ‪.‬‬
   ‫د‬
   ‫ددر‪-‬و‬
       ‫بمعنی سقله و بخیل و گرفته باش‬                              ‫ر کان؟ = بفتح اول بر وزن مکان »‬
             ‫و راهزن فوطاع الطریقرا لز گوبند ‪.‬‬                    ‫یاند که از خود رمیده باشد و‬   ‫رر‬‫کصی‬
                                                                                                    ‫شخ‬
 ‫زکریا ب‪۱‬نت‪-‬ح‌اول و کوسترحانتیانی‬                             ‫خود بخود سخن کوید * و طم ارول هم‬
‫(‪ )۱‬کارد را‬            ‫زندنود‬‫از‬ ‫یلغت‬
                                   ‫بالف کشیده ‪.‬ب‬                                                                     ‫کگفته‌اند ‪.‬‬

                      ‫گویند ویعربی سکین خوانند ‪.‬‬                  ‫ر کش = بنتح اول و کرکاف وسکون‬
 ‫ر کیدن ‪ ۷‬د بفتح اول‌بروزن رمیدن»‬                                 ‫شین شطه دار‪ .‬لذت و طعم زمخت را گوبند و‬

‫بعنی خودبخود از فهر وخشم سخن کردن »وضم‬
                              ‫‪۰‬‬   ‫‪.‬ات‬    ‫اول هم ورخ‬               ‫نم اول وفتح ثانیبروزن‬                ‫زرکنج ‪۶‬‬



                                                ‫بان دواردهم‬

                      ‫در زای نقطه دار باکاف فارسی مشتمل بر سه لغت‬
‫مدار‬    ‫حربی حبر و‬       ‫کنند و‬    ‫باشفد که در دوات‬               ‫رال‪ = ۸‬بروزن و معنی زغال است‬
                                            ‫خوالند ‪.‬‬              ‫معربی‬       ‫و‬    ‫کشته باشد »‬     ‫اخگر‬      ‫و‬       ‫که انگشت‬


‫کال ‪١١‬ے‏ بضم اول بروزن کلاله ‪,‬‬
                             ‫ر‬                                                                            ‫فخحومانند ‪٩‬‏ ‪.‬‬

‫بمعنی زکالاب است که سیاهی و مرکب‬                                  ‫زرگالاب لت بضْم اول و ثانی ولام هر‬
                                                ‫باشد
===== leaf 489 printed ~ 1029
                                    ‫بیان سیزدهم‬
             ‫درزای نقطه دار بالام مشتمل برباتزده لفت و کنایت‬


                    ‫تنکه و تلريك را گویند ‪.‬‬       ‫رلال ‪ -‬صم اول بروزن جوال » کرمی‬
‫رلقیی ‪ - ۱‬نم اول ‪ .‬بر وزن و معنی‬                 ‫را کوبند که درميان برف هم میرسد » و او‬
                                                  ‫پرنده‌ابت پر از آب صاف و آن آب را آب‬
              ‫نند ‪۰‬‬
                  ‫اکسب‬      ‫رخچوابنه‬
                                   ‫دار‬
                                     ‫وچ‬          ‫زلال خوانند و آن کرمرا اندك حیائی وح رکت‬
 ‫زلو ‪ - ۴‬تح اول ثوائی بکوشایوده‪.‬‬                  ‫مذیوحی‌هت ‪ -‬وزلال بمعنی صاف عربیاست ‪.‬‬
‫کرمی باشد سیاه رنگه ‪ .‬چون بر اصنای آدمی‬           ‫بلسفتی د کنابه از نمودن مطلوب‬
                                                                              ‫ز‬
               ‫مجیانند خون ازآ جا بمکد ‪.‬‬          ‫(‪ )۱‬است خودرا حاشق و دل او را بکمند خود‬
‫ز لو ك ‪ -‬تح اول و انی بو اوکشیده‬                                                        ‫آوردن ‪.‬‬

   ‫زات رھ رل باه که کے ا‬                          ‫زلف خطا ‪ -‬بک الت ‪ .‬بمعنی‌خطا‬
                              ‫معروف است ‪.‬‬                                  ‫و گناء و تتصیر باشد ‪.‬‬

‫رله ‪ = ۴‬بفتح اول‌وثانی‌مشدده جائوری‬              ‫زلف رهی = بکس ثالت ‪ ۰‬کنابه از‬
‫باشد شبیه بملخ که پیوسته در میان غله زارها‬       ‫شب است که جربی لیل خوالند ‪ -‬و کنابه از‬
                                                  ‫خاکی هم حت که جوهر آدمی از آست‪ -‬و‬
 ‫وهوای کرم فرباد طولانی کندوآنرا جزد بروزن‬
                                                                        ‫بلةٌ ارضی را نز گویند ‪.‬‬
 ‫بزد هم خوانند؛ وباین معنی بکسراول آیمزده‬
‫ست؛ وبعضی کویند جانوریست سیامرنکک وپر او‬          ‫وال‪ -‬ممروف است ‪ -‬کونابه‬
                                                                        ‫رلف خ‬
 ‫در زیرکاسة يشت او می‌باشد ‪ ,‬وآن لوعی‌ازجمل‬       ‫است اطزلا لواجورد که بر‬       ‫یشنوتی‬
                                                                                     ‫زرای‬
                                                                                        ‫از آ‬
‫باشد ؛ و بضی دبگر کوبند جالوردست پردار‬                         ‫روی عروس در شب زفاف کنند ‪.‬‬
‫که بیشتر درحمامها و جاهای لمناك بهممیرسد‬          ‫ارلفه = بنتح اول و ثانیو الث کوچ‬


  ‫‪:‬سشق و‬
       ‫‪ - ۱‬اوسا ‪( 6۷02722 . 080122‬شت ‪( )۹۲۱ ۰ ۰۱‬کباردن زرین) رك ا‬
   ‫هوشمان‪ ۸۵۱‬؛ درفارمی‪ -‬زفرین< زرفین == زورفن‪ <-‬زولفی<‪ -‬زوفرین»
===== leaf 491 printed ~ 1031
  ‫رمج‬                                                                                         ‫‪-۱۰۷4-‬‬
 ‫رمام = بکر اول بورزن لظام 'مپار‬                      ‫هم هت » وبضی چشمهٌ زمزم را کوبند ‪٩‬‏ ‪-‬‬
                 ‫شتو باشد ‪ .‬گوبند عربی است ‪٩‬‏ ‪.‬‬      ‫و بممتی آهسته هم هست و زمزم بمنی آحسته‬

 ‫رمان = بفتح اول‌بروزن رمان» بمعنی‬                    ‫آهته ‪ - ۴‬و طفلی که در هنگام حرف زدن‬
‫ورمکه باشد‪ -‬و در عربی مقدار‬             ‫متووت‬
                                            ‫فو‬       ‫آب از دهنش بیرون آید ‪ -‬و شخصی که بوقت‬
                           ‫ح ركت فلك اعظم ‪. ۷‬‬        ‫لب او‬        ‫گوشت‬      ‫زدن‬      ‫و حرف‬        ‫خندیدن‬

  ‫رمقر ] ‪ -‬با تا و رای فرشت بورزن‬                   ‫بیرون ابد و گوشت دهان او تمام یبدا و ‪.‬‬
 ‫فلکاء بلفت زند و پازند ( ‪ ) ۲‬بمعنی تمسخر‬             ‫تمابان شود‪ - ۴‬و فتیله را بیز کوبند مطلقا‬
                                ‫ویشخند باشد ‪.‬‬
                                            ‫ر‬
                                                      ‫خواه فتیلة داغ و خواءه چراغ باشد و خواه‬
‫رهج ‪ -‬بفتح اول و سکون الی و جیم‬                          ‫د‬ ‫دنی‬
                                                             ‫شاثا‬
                                                                ‫می ب‬
                                                                   ‫فتبله نفنگگ و زخم ‪ -‬و در عرب‬
‫ابجد » مطلق صمغ را کوبند خواء صمخ عربی‬                ‫بمعنی مهار کردن شتر باشد‪ -‬و بمعنی تکبر و‬
 ‫باشد و خواه غیر عربی ‪ -‬مطلق زاج را لیز‬              ‫نخوت هم هت ‪ -‬و بلند بدراشتن سر را یز‬
                                                       ‫‌ماست ‪.‬‬ ‫هه‬‫دتن‬‫وی پآیشمرف‬  ‫‪-‬ن‬ ‫مدع‬
                                                                                     ‫بین‬
                                                                                       ‫گو‬
 ‫کویند ‪ - ۷‬اعم اززاج سفید وسرخ وسیاء وزرد‬
‫و سبز؛ وبعضی کویند ابن لغتبفتح اول و ثالی‬             ‫زماروغ ‪ - ۴‬بفتح اول و انی بالف‬
 ‫است ومعرب زمه است و زمه زاج سفید باشد له‬             ‫کشیده ورای‌بی نقطه بواو رسیده و بغین شطه‌دار‬
‫مطلق زاج ‪ -‬و بضم اول وفتح الیمشدد بعربی‬               ‫زده" رستنیی باشد که اززمینهای نمناك ومتعفن‌و‬
‫مرغی اتسرتاذکوهبآرادران‌میگونند ‪ ۸‬؛وبنی‬               ‫دبوار های حمام وزبرهای خم آب (‪ )۱‬و امثال‬
‫کویند مرغی است شکاری و خوش منظر از‬                    ‫آن روبد باندام چتر و عوام آنرا کلاء قاضی‬
  ‫جنس سیاء چم یمئی از جنس چرخ‌وشاهین ‪.‬‬                      ‫و چترمار کوبند؛ وضم او
===== leaf 492 printed ~ 1032
 ‫‏—‪ opo‬اسه‬




‫طعم‬       ‫مانئد‬   ‫قطه‌دار و فوقانی » طعمی راگوشد‬
                                                     ‫هچ ‪ -‬بفتح اول و سکون ثالیو جیم‬
‫عفص خوانندب‬          ‫حنرویی‬
                          ‫حلیله و مازو و امثال آ‬
‫و بنعنی نیشکر هم آمده است ‪ -‬و گرهی رایز‬                ‫را" زمج بلور میگوبند ‪ -‬و نام موضمی هم‌هست‬
‫گفته‌اند که بغامت مخت بته باشند ‪ -‬و کنابه‬              ‫در خراسان و احمد زمچی بآن موضع موسوم‬
‫ازمردم گرفته ومقبوض ‪ -‬و بخیل ‪ -‬و درشت و‬                ‫است ‪ . ۴‬وبکسر اول مرغی باشد سرخ ردکه‬
           ‫‪ :‬ورشتح اول‌هم آمده‌است ‪۰‬‬   ‫تانق باشد‪6‬‬
                                                      ‫و بزرکه شبیه بعقاب ویسیکوبند شکره امت‬
‫‪ « ۱‬باکاف ‪ ۰‬بروزن و ععنی‬               ‫هك‬              ‫و آن پردده‌ای باشد شکاری کوچکتوازباشه ‪. ۴‬‬
‫ومرد‬       ‫ه سخت‪.‬‬      ‫زمخت است که طعم عفص‪ -‬و‬
                                                         ‫زسیا»ج‬
                                                              ‫زهج بلور ‪ -‬بکر جیم فار‬
                              ‫بخیل وناکس باشد ‪.‬‬        ‫سفید را گوبند ‪ -‬و بعریی شب بمانی خوانند‬
 ‫وای قرشت‬
        ‫زمر و نتن ‪ ۰ ۲‬بانون ت‬                                                        ‫بتشدید بای ابد ‪.‬‬
‫(‪ )۱‬بروزن پهلو شکن » بلغت زند و یلزند(»)‬               ‫زهمچاك؟ » بفتح اول و جیمفارسی و‬
 ‫بمعتی‌سراییدن وخوانند گی کردن باشد ‪,‬وزمروب‬            ‫واف ‪" ۰‬تامپرنده ایست غير‬
                                                                              ‫سکون انی ک‬
‫نمی بعنی برایم و خوانند کیکتم “ و زمرویه‬                                                        ‫فظوم‬
                    ‫یعنی برایید وخوانن دک یکنید ‪.‬‬       ‫زمچیکور۔ بفاجایرمسی کواف‪.‬این‬
 ‫آهسته‬      ‫بمعتی‬   ‫بروزن همدم ‪۰‬‬   ‫ی‬   ‫رمز م‬
                                                       ‫خود از موّید النسّلا‬   ‫لفت را سروری در فرهنك‬

‫آهته‌است چهزمآهسته را گویند ‪ ۸‬وخوالند گی‬               ‫سمعنی زمج بلور‬     ‫بروزن کردی دور آورده ات‬

 ‫ورنمی که بآهستگی کنندوزمزمه عبارت ازآن‬
                                      ‫ت‬                ‫که زاح سفید باشد ‪ .‬و چنین ظاهر میشرد که‬
 ‫نی آتش‬              ‫مشدضکاهن‬
                            ‫با‬      ‫ل‏م‪-‬اتی‬
                                          ‫ک‪٩‬‬‫اوست‬        ‫ماتصل نونته بودند و باران تصحف‬
                                                                                     ‫رمج بلور ر‬

 ‫تش آتش‬
      ‫رلیسو‬
          ‫پیتما‬
              ‫پرستان درمحل ستایش بار‬           
===== leaf 493 printed ~ 1033
                                                                                   ‫‪-۱۰۳۱-‬‬
‫پاکیره منظر از جنس چرغ و آنچه رنگش‬             ‫ر‪5‬‬     ‫‪ -‬ونام کتابی است از مصنفات زردشت‬   ‫رند‬

                                                             ‫در مکه معظمه ‪۴‬‬     ‫و نام چاهی است‬
‫بسرخی زد بهتر است وآنچه در صحر! تولك و‬
‫کرمز کرده باشد بکاری راید و آثرا بعرربی زمج‬    ‫از‬    ‫کنابه‬   ‫| نش فشان ‪-‬‬         ‫رمزم‬
‫خوانند؛و بی دیکر کننه‌اند که همای است و‬                                   ‫آ فتاب عالمتاب ات‬
                  ‫آنرا استخوان رند کو‬
                                               ‫رهز هه ‪ ۴‬بر وزن سردمه ‪ ۰‬بمعتی‬
‫زهو ‪ -‬بفتحاول و ضمالى و سکون‬                   ‫زمزماست هکسهتبگای‌چیزی‌خواندن_‪ -‬وکماتیکه‬
‫واو مجپول » ابن لدت ازاضداد است بمعنی گل‬
                                               ‫ل ستایش و مناجات بباری تعالی و‬ ‫منحدر‬
                                                                                  ‫مغا‬
‫نر وکل خدك هردو آهده است که بعربی طبن‬
                                                ‫پرستش آتش و چیزی خوردن بر زبان رند ‪-‬‬
  ‫نی‬
   ‫عهم‬   ‫کویند ؛ ویضم اول همباین هع‬
     ‫بنیمو‬                                              ‫‪ 1‬نامکتابی است از مصنفات زردشت ‪4 .‬‬
  ‫ل‬  ‫وزب وعل‬
  ‫ګف و‬          ‫سقف خاله باشد که آنر‬
             ‫چا ا‬
‫پوشیده باشند و آنرا بعربی غمی بر وزن هوا‬       ‫واف فارسی‬ ‫رمگانه = بفتح اول ک‬
                                 ‫خوانند ‪.‬‬      ‫بروزن البان » موی زهار را گویند ؛ و ضم‌اول‬
                                                                                ‫هم آ مده‌است ج‬

‫رمودن ‪ .‬بفتح اول بر وزن بودن »‬
             ‫بمعنی نقش ونگار کردن باشد ‪.‬‬        ‫رمنج! یکی اول وانی مضموم‌بنون‬
                                               ‫‪ 5‬جيم زده » مرغی باشد از جنس عقاب ورنگش‬
 ‫رموده = بفتح اولیروزن لبوده »هش‬
                                               ‫بسرخی مابل بود؛ بوعضی کوبند مرغی است‬
                      ‫ونگار کرده را کویند ‪.‬‬
                                               ‫سیاه و از غلیواج بزرکتر و آنرا دو برادران‬
                                               ‫خوانند ؛ و بعضی گویند جالوریست‪ .‬شکاری بغایت‬
  ‫‪ - ۱‬وآن مترادف «باژ» است ‪ .‬درکتاب الناج منوب بجاحظ آمده ‪« :‬پادشاهان‌ساسافی‪-‬‬
  ‫هنگامیکه طعام ابشان حاضر ميشد ‪ -‬برآن زمزمه میکردند‪ .‬وکسی بحرفیمخن‌نمیگفت تابلند‬
  ‫شود واگر بخن گفتن ناچار میشد » بجای آن‌باشاره » غرض ومتصود خودرا میفپماند ‪» .‬فردوسی‬
                                          ‫در داستان پذبرابی خرو
```


## [2026-09-05T20:57:23.080Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\np=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nimport re\nfor i,t in enumerate(p):\n    if 'زمهریر' in t or 'زمستان' in t and 400<i<520:\n        print(i, i+538, [w for w in ['زمهریر','زمستان','زمهر','شمیران','سمیران','سمیرم'] if w in t])\n\"",
 "description": "Find zamharir/zemestan leaves"
}
```


### [2026-09-05T20:57:25.639Z] TOOL RESULT

```
490 1028 ['زمستان']
493 1031 ['زمستان']
513 1051 ['زمستان']
```


## [2026-09-05T20:57:28.595Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\np=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nfor i in (490,494,495):\n    print('===== leaf',i,'printed',i+538)\n    print(p[i][:3000])\n\"",
 "description": "Print Borhan leaves 490,494,495"
}
```


### [2026-09-05T20:57:30.329Z] TOOL RESULT

```
===== leaf 490 printed 1028
 ‫‪٩‬‏ ‪۱ ۵‬سه‬   ‫سز‬                                                                               ‫زلبا‬



‫ز لیف ‪ - ۴‬بفتح اول بروزن حربف ‪۰‬‬                     ‫و شبها فرباد نند و تیز وطولالی میکند و او را‬
                   ‫بمعنی ترس وبیم باشد‪.‬‬              ‫چرخ رمه نیز میگویند ‪ -‬و در عربی طمامي‬
‫ر لیفی * = بفتح اول بروزن طبیدن »‬      ‫‪۱‬‬             ‫باشد که مردم فرومایه از جایی بردارند وبرند ‪.‬‬
 ‫بمعنی ترسیدن و بیم بردن ‪ -‬و تهدید کردن‬              ‫لیا ‪ = ۱‬بباای ابچد بروزن‌کسیاه‬
  ‫قهاوم‬
      ‫تین‬
        ‫ن ک‬
          ‫اعنی‬
             ‫تورسالیدن باشد ‪ - ۷‬و بم‬                 ‫و عربان زلابه‬         ‫نام حلوابی است مشهور‬
‫هم آمده است‪ -‬وچرخی را نیزگویند که بدان‬
                                                                                         ‫گونند ؟ ‪.‬‬
‫نه دانه را از پنبه جدا کنند ؛ و بکسر اول‬
                                     ‫همکفته‌اند ‪.‬‬   ‫وای شطه دار‬
                                                              ‫زلیخا ‪ -‬بانول خ‬
  ‫ای‬
   ‫دو‬‫صاز‬
       ‫رلیل ‪ -‬بر وزن خلیل " آو‬                      ‫بالف کذیده بروزن سویدا » نامزن عزیز مس‬
                                    ‫ند‪.‬‬
                                      ‫ویرا‬
                                         ‫ککلو‬                                     ‫باشد ‪. ۴‬‬


                                          ‫بیان جهار دهم‬

                 ‫در زای نقطه دار بامیم مشتمل بر سی و وو لقت و کنات‬

‫وکون انی " نام| موسوم است ‪ -‬و بمعنی سرما باشد که در مقابل‬      ‫تح اول س‬    ‫بمفد‬ ‫د‬
 ‫رودخانه‌ایست؛ وبعضی کویند نام شهربست که‌این | کرماست ولهذا ابام سرمارا زمستان گوهد‪:‬د ‪- 4‬‬
 ‫و ام‌چشمه‌ای‬         ‫رودخانه از بهلوی آن میگذرد ‪ ۷‬و بدان شهر | و باد سشت وتندرا یز گفته‌اد‬


  ‫‪ - ۱‬کیلکی ‪ . 270112‬نهرابی ‪ . 40102‬معرب زلاية «لك‪۲‬ص ‪ « * ۵۱۲‬محالم‬
  ‫حلوایی که با دوغن‬         ‫‪۴‬‬         ‫‪ ۰‬ترکی « زلویبه » ‪ ۰‬آرامي « زلویا» «تفس> ‪.‬‬       ‫الفربة ص‪6۰۱‬‬

                                                              ‫زتون با روغن کنجد وامتال آن یزند ‪:‬‬
                        ‫راست کویی زلیبا باشد ‪.‬‬          ‫شکن اکر بيابم هیچ‬
                                                                        ‫نکان‬
   ‫‪.‬‬    ‫«هعود سعف لاهوری ‪۸‬‬
   ‫‪ .‬رك ‪ :‬داثرةالمعارفانگلیسی ‪۰‬‬      ‫نام زنان دیگر بوده است‬    ‫ت عبر از رن عز بز هعس ‏‬   ‫‪۳‬‬

                            ‫‪:‬كر نفیلز ‪.‬‬    ‫‪۴‬‬        ‫‪. 26162 : Universal‬‬               ‫‏‪knowledge‬‬
                                                                       ‫‪.‬‬   ‫رك ‪ :‬زلف‬      ‫‪°‬‬

                       ‫زلیفن بستنش بهتر زلیفن ‪.‬‬        ‫‪ - ۱‬سیاست کردش بهتر سیاست‬
   ‫‪°‬‬   ‫‪۹°‬‬   ‫دامغالی‬    ‫(منوچهری‬



       ‫‪lî ۲‬‏ ‪maZ‬‬                     ‫در سخ چایی مزبور اثتباهاً هر دوجا « زلفین» است ‪-‬‬
  ‫‪۶۶۲٩‬‏ ؛ ‪ ۶‬رم » شهر کی‌است‬         ‫در جوا رکش و اسف (ماوراء النهر) است «مینورسکی ‪ .‬حدود ص‬
  ‫برراه جیحون از ترمذ و آمل» ‪ .‬صگروید ‪ :‬شهرست دربایی و کمان برده بین صرء و عمان‬
    ‫ت»ا‪.‬‬‫س)‬‫وما‬
     
===== leaf 494 printed 1032
‫=‪m‬‬
                                                                                                                    ‫زمهر بر‬


‫رمیدن = بروزن‌ره‌یدن ‪ ۰‬بمعنی‌خابیدن‬                                ‫کونند و معرب آن زمج است و بی گوبند‬
                              ‫و جاویدن(‪)۲‬باشد ‪# .‬‬                                            ‫مه ‏‪ E2‬است شبیه‌بز اج ‪.‬‬

‫زمین ار زیر پای کشیدن ‪-‬‬                                             ‫» معروف‬         ‫رههر بر" بر وزن ند خمیر‬
‫کنابه از آن است که دیوانگایرا ننازی بازی‬                           ‫آسنت‌وجابی(است) بسیارسردنزديك بانتهای کر‬
                                                ‫‪.‬‬    ‫اند‬
                                                       ‫مسسر‬
                                                                   ‫هوا ‪١‬‏ و ابن لفظ مر کب استت از زم و هرر‬
‫رمین‌پیمای ‪ - ۴‬ماح ر ساح‬                                            ‫بمعثی سرمای سخت کننده چه رم بمعنی سرمای‬
 ‫پیمای ومافرراگوبند ‪۰‬‬               ‫ان‬
                                     ‫و عالم کجردپ و‬                   ‫و هر مر نمعنی کندده ‪,‬اشد که فاعل‌است‬               ‫ەت‬


                                                                    ‫انی سحتانی‬            ‫= غتح اول ‪+‬‬
                                                                                                      ‫زمی ‪۲‬‬
                            ‫که اه و ساباد‬
                                                                   ‫ارض‬      ‫بعربی ‏‬   ‫که‬      ‫رهن انش‬          ‫طف‪.‬فف‬
                                                                                                                   ‫متده‬
                                                                                                                      ‫رس‬

                                                                                                                     ‫خوانند ‪.‬‬
‫‪۳۹‬‬            ‫‪E‬‬                         ‫‪e‬‬

‫ارم شده‬     ‫چاره |‬     ‫م‬    ‫بای مر دم‬
                                                                   ‫رمیاد ‪ ۴‬ه بفتح اول و کر انی و‬
                                        ‫و‬    ‫در زیر دست‬
                                                                   ‫تالف کشہده و ‪,‬دال (‪ )۱‬زده ‪ .‬لام‬              ‫نحتالی مدد‬
                                                        ‫باشد‬
                                                                   ‫وهشم استت از هرماه شمی‪ . .‬گویند‬                   ‫روز یت‬
‫زهین کوب ‪ ۰ °‬باکاف بواو رسیده‬                                       ‫شالدنوعمارت‬            ‫در اىن روزتخم افكندن ودرخت‬
‫‪.‬نابه از اسب و شتر و امثال‬
                         ‫و ببای ابجد زده ک‬
                                                                  ‫کردن بار خوب است ‪ -‬و نام فرشته‌ایست که‬
                                            ‫انها باشد ‪.‬‬
                                                                   ‫‪:‬محاقظات حوران بپدتی و ندبیر مصالح این روز‬
 ‫زهین‌هر ‪ » ۵۵‬بک نون و هض
===== leaf 495 printed 1033
                                        ‫بیان بدانهزم‬

               ‫در زای نقطه دار بانون مشتمل بر هشتاد لفغت و کنابت‬
‫کنابه از موج پیالةً شراب است ‪ -‬و خطی را‬           ‫ثالی ‪.‬ممروف‬    ‫وون‬‫کول‬
                                                                      ‫سح ا‬
                                                                         ‫رن = بفت‬
‫یگزومند منحن یکه از شراب در بیاله معلوم‬              ‫ااوهلی‬
                                                          ‫یضم‬
                                                            ‫کوب‬
                                                              ‫است کهنقیض مرد باشد ‪٩‬‏ ‪-‬‬
                        ‫مشود تپارشدن بیاله ‪.‬‬     ‫است که آلرا دو سگروند و در میان زراعت‬
‫ر نباره » بنتح اول و بای اسجد (‪» )۲‬‬                                         ‫کندم و جو روید ‪.‬‬
‫را گومند چنانکه‬    ‫بر وزن انگاره » زن دوست‬       ‫زفراج‪ -‬بض اول و تالی مشدد بالف‬
‫را ‪ ۴‬چه باره بمعتی دوست‬      ‫ست‬
                              ‫دهوپر‬
                                  ‫غلام بار‬       ‫کشیده و بجیم زده ‪ ,‬چرب رود گوسفند را‬
                              ‫هم آمده است ‪.‬‬       ‫گوبند که دبه و برج را باهمکوفته درمیان‬
‫ز بر ‪ -‬بفتح اول بروزن چتبر ‪ ۰‬چهار‬                   ‫بشنعدروبی‬
                                                            ‫آن پر کرده براوغن بربان کرده با‬
‫چوب باشد مالند نردیان دو یایهکه ميان آبرا‬        ‫میب خوانند ‪ ۴‬؛ وباجیم فارسی‌هم آمدهات ‪.‬‬

 ‫ببافند و از خاك وخشت‬     ‫م‬   ‫برسمان بالوا‬
                          ‫چرربا‬                      ‫ن‬
                                                     ‫وددزبر‬
                                                          ‫ونی حش‬
                                                               ‫رنار ‪ ۴‬سس اول ا‬
 ‫و امثال آن پرکنند و د وکس برداشته اجزایی‬        ‫شته را گومفند عموماً و رشته ای‬
                                                                              ‫هر‬‫کفار » ر‬
‫یجابی برند و بعربی مثقل خوانند ® ‪ -‬ومشکی‬         ‫هرستان باخود دارید‬    ‫اش‬    ‫کهبت برستان و‬

‫را نیز کفته‌اند کهبردو سرآن دو چوب تعببه‬                                                ‫خصوصا‬
‫ر‪-‬شوك رانیز‬
          ‫زند‬
            ‫داون آب کش‬
                     ‫کرده بابشند‬                 ‫رنارساغر = بکسر رای قرشت( ‪)۱‬؛‬

                                     ‫ایجد ‪۰‬‬    ‫چك‪:‬‬   ‫(‪)۲‬‬        ‫(‪ )۱‬چك‪ - :‬قرشت ‪.‬‬

 ‫‪ ۱‬بهلوی ‪( 8202‬زن ‪ .‬زوجد) »اوستا_‪ [103 - , 102‬د بارتولمه ‪ .»+۳۰‬رك‪:‬یب رکه‬
  ‫‪înaJ‬‏ ) زن ‪ ۰‬زوجه)» ارمنی ‪nik‬‏ (زن ‪ ۰‬بانو) > کردی‬        ‫‪ ١ ۸۵ -‬هندی باستان ‪-1 -‬‬       ‫‪۷‬‏‬
  ‫(ازا ‪ , ) [06‬اففانی ‪ ° 12001 . [1281‬بلوچی ‪ [02‬شەنى ‪ , 01018‬سریکلی‬
                                                                  ‫‪ (۵‬زن ) ز‬
          ‫‪ . 01112,‬منجی ‪« 2801112‬اسذق‪»»۸۹1‬اورامانی ‪ 0802‬د‪ . 4‬اورامان ‪- ۸۲۱‬‬                ‫‪0‬‬
      ‫در عمرخوش آوبز له در عمر دراژ ‪.‬‬                ‫لنیه برنج هست زناج بهل‬
```


## [2026-09-05T20:57:47.299Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\np=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nfor i in (367,368,369,370):\n    print('===== leaf',i,'printed',i+538)\n    print(p[i][:2600])\n\"",
 "description": "Borhan around printed 905-908 (day)"
}
```


### [2026-09-05T20:57:48.992Z] TOOL RESULT

```
===== leaf 367 printed 905
‫دي‬                                                                                     ‫=‬

‫‪ » ۱‬بروزن افزوده » بمعنی‬      ‫دوه‬
                                ‫ده ب‬             ‫و تحتانی بواو مجپول رسیده و بای فارسی‬
                   ‫عشر باشد که ده بك است ‪.‬‬                          ‫مفتوح مدال ابجد زده ا‬
                                                ‫»مر‌معروف واهی‌منکررا‬




                                     ‫بیان بیست ویکم‬


‫ماه دهم باشد از سال شمسی ‪ ,‬وآن مدت بودن‬
                                                 ‫دی = بقتح اول وسکون انی‪ .‬نام‌ملکی‬
                                                 ‫است که تقددس امور و مصالح دیماه و روز دی‬
‫وتام روزنهم ‪ ۴‬ازهرماه فارسی » ودرین روز ازماه‬
‫بمهر ودیبادین و دیباتر بدوتلق است ‪ -‬د ‏ | وی فارسیان جشن ‪-‬ازند ومد کنند؟ ‪ -‬وبکس‬
  ‫ظ‪ ,‬ممحف « دهوبه »‪ .‬این‌کله درعصر ساسانبان ویز در قرنهای اول اسلام معمول‬         ‫‪۱‬‬
 ‫بود ‪ .‬درالفهرست ابن‌الندیم(چاپ مصري ‪ )۸۳۳‬در موضوع اقل‌دبوان عرب ازفارسی بعربیآمدد‪:‬‬
  ‫صالح‌بن عبدالرحمن مولی‌بنی تمیم که" زیر دست مردایشام بر للفيخ صاحب دیوان حجاج بود‬
  ‫‪ :‬کیفتصنع بدهویه وششوبه؟‬           ‫قیول کرد که آنرا از فارسی بعربی بگرداند ‪ .‬رونام‬
     ‫قال ‪ :‬اکتب عثراً و نصف عشراً » در اینجا ظاهراً ششوبه مصحف « پنجوبه » است »ببااازب‬
  ‫مضیقه در اصطلاح عربی » تاگزیر شده صف عثر را بجای « شثوبه » بشنهاد کند ‪ .‬مب لمات ‪.‬‬
  ‫‪ - ۴‬دراوستا _تاکناا‪ 21‬با ‪ 2۷01021-‬بمعنیآ فربنندہ‪.‬‬    ‫‪ ۴‬هشتم صحیح‌است‪.‬‬
  ‫دادار و آفریدکار است و غالبا صفت اهورمزداست و آن ازمصدر ‪ 21‬بمعنی‌دادن وآفربدن است‪.‬‬
  ‫دی) برای تعین دهه‌ین ماه استممال شده ‪ .‬درمیان سی روز مامه‬      ‫در خود اوستا صفت دئوش [‪-‬‬

  ‫روزهای هشتم و پاتزدهم وبیست وسوم به دی( د=ئوش) موسوم است بنا بر تسمیه بنام ختا‪ .‬برای‬
  ‫بقیه درصفحةٌ ‪۸۰٩‬‏‬
                                                                          ‫‪4۰٩‬‏‬    ‫حة‬
                                                                                   ‫صبهفاز‬
                                                                                        ‫بق‬
       ‫رك ‪ :‬خاله گیر ء ده هزاران ‪.‬‬     ‫‪۸‬‬         ‫‪۲٩‬‏ ‪.‬‬   ‫‪:۸۹‬‬   ‫معرب آن دهنج‪ « .‬دزی ح ‪ ۱‬ص‬
        ‫عبارآن‌هفت دهم (طلامانقره) بوده‪.‬‬   ‫نی‬            ‫‏‪ ٩‬رك‪ :‬ده هزار خانه گیر‪.‬‬
  ‫‪ 0‬و بکشید ‪ « :‬و حن ( سلیمان ) گفت ‪ :‬دهید و حشمتی بزرکه افکتید بکشتن‬
      ‫بیار که کنید ‪ .‬تا یس از این دتدانها کند شود از ری» «تاریخ بیهقی ص‪ ۳4‬متن وحاشیه» ‪.‬‬
     ‫=ه بسعنی ناحیه وکشور ) [ رك ‪:‬ده ]‪= +‬‬
                                        ‫(ي‬
                                         ‫از ‪ :‬دهیو د‬             ‫=یت‬
                  
===== leaf 368 printed 906
   ‫سره‬                                                                                                         ‫دبافودا‬

‫دابا * = بروزن زببا ‪,‬قماشی باشد از‬                                               ‫اول رو ز گذشته را گوند ‪. ۱‬‬

‫ونابه از دیدارخوبان همهت ‪.‬‬
                         ‫حربرالوان ‪ -‬ک‬                      ‫دیاقود‪ - ۴ )۵‬بنتح اول و انیبالف‬
‫دییاجی ‪ = ۱‬بروزن تیماجی» دیبایاف‬                            ‫اقطه بالف‬    ‫دال ‪۳‬‬    ‫و‬       ‫کشیده و قاف بواو زسده‬

‫راگوند بعتی هرچه آزدیبا بافته شده باشد ‪#.‬‬                   ‫را گونند‬    ‫خشخاش‬     ‫‪ ۰‬بلغت عودانی شرت‬             ‫کشده‬

                                                             ‫که ازیوست خشخاش بخته باشند نهازشم آن‪:‬‬
‫دیبادین ‪ = ۳‬بفتح اول ودال دیگر بر‬
‫وزن شرم کین » نام فرشته است ‪ -‬و مکی از‬                      ‫دیا وش س با نون بر وزن قبایوش »‬
‫نامهای‌الهی هم هت ‪ -‬ونام روز بیست وسیم(‪)۱‬‬
‫از دیماه مغان‬    ‫روز‬       ‫در ین‬   ‫‪۰‬‬   ‫باشد ازهر ماه شمسی‬    ‫خشکی ودربا دزدی وراهزنی میکردند ‪ ۰‬وبصنی‬
‫روز‬     ‫بتن‬
          ‫دكراس‬
              ‫جشن سازند و عید کنند و لي‬                         ‫کگوبند دام شخصی است که عذرا را بفروخت ‪.‬‬
‫دعا کردن بجهت دفم شر شیاطین واز حق تمالی‬                     ‫دیب = پکسراول بروزن‪ :‬سیب » بندری‬
                                       ‫فرزند درخواستن ‪.‬‬
                       ‫‪۱‬‬                    ‫‪۰‬‬                      ‫باشد ازبنادر هند ‪ -‬ودر ترکی‌بیخ وین ه‬
                                                                ‫چریز‬
‫دیباذر ‪ = ۲‬بفتح اول دوال قطه دار‬                                                                     ‫رگاونند ‪. ۴‬‬

                                                                          ‫(‪ )۱‬چك‪ :‬ببست وسوم ‪.‬‬
  ‫]‪id‬‏ ‪evécs‬‬      ‫ع‬         ‫‪ ,‬کردی‬       ‫‪kîd‬‏‬   ‫یهلوی‬   ‫( دیروز ‪۹5‬‬     ‫هندی ‏ باستان ‪séyh‬‏‬             ‫‪۱‬‬
  ‫د(یروز عصر ) ‪ ۰‬استی ‪ 2002 , 8012 , 6022‬و ‪ ( 00012‬دیروز ) " بلوچی ‪۵2 , 612‬‬
       ‫‪4:۲۰ ۶۸‬‬   ‫‪ .‬ورك‪ :‬دزی حاص‬             ‫‪۱۸۱‬‬    ‫(فر) «لك‪۲‬ص‬    ‫‪60062‬‬       ‫‪Ff‬‏ —‬              ‫‪.‬‬    ‫داسشق ‪۰۹۵۰‬‬
   ‫‪ - ۴‬سانسکریت ‪« 301۷‬فهرست ماللهند بیرونی ص ‪« :»۲4۳‬الدیبات » وحی‌الجزاثره‬
  ‫‪ - ۴‬درترکی ‪ :‬شایستگی‪ ,‬خوشبختی؛ ته " پ »ا پابه «جفتابی‬                               ‫م«اللهند ص ‪ ۰۸‬ی ‪٩‬‏ > ‪.‬‬
      ‫* ‪ -‬بهلوی ‪ « 081‬تاوادیا ‪ ۰ ۰۹۱‬از هندی باستان ‪802۷010 . 01 -‬‬                                          ‫‪.‬‬         ‫‪۳‬‬
   ‫‪ .‬رجه اشتقاق آن قطعی ليست‬                        ‫( زبانه کشیدن » پرتو افکندن » درخشیدن) ‪٠‬‏ ارمنی ع‬
   ‫د اسشق ‪۱٩٥۰‬‏ در فارسی
===== leaf 369 printed 907
   ‫دور‬                                                                                                     ‫سس‬
 ‫اس * ‪ -‬برای بیقطه وجیم‬
                      ‫جیبر‬
                         ‫د‬                              ‫بروزن سودا کر ‪ ۰‬تلم روز هشم است ازهر ماه ‪.‬‬

 ‫بالف کشیده و سین مپمله و حرکت مجهول ‪.‬‬                   ‫شمسی و دربن روز ‪.‬از ماه دی که دیماه ماشد‬
           ‫بلغت ہوتانی نوعی از مرقشیشا باشد ‪.‬‬            ‫فارسیان عکیندند وجشن سازند بنا برقاعده‌کلیه‬
                                                        ‫که مبان ابشان معمول‌است‪.‬ونام ملکی است که‬
‫وسر میم‬
      ‫دی بمهر ‪ - ۱‬بفتح اول ک‬
                                                             ‫امور ومصالح اين روز بدوتعلق دارد‪ .‬ونيك است‬
 ‫وسکون ها ورای قرشت » نامی است از امهای‬
                                                         ‫درین‌روزصدقهدادن ابزهرتندرستی خود وفرزسدان‬
 ‫الهی ‪ -‬ونام فرشته‌ابست‪ -‬ونام روز پاتزدهم جود‬                                                          ‫ودعا کردن ‪.‬‬
‫هزاه دی‬
      ‫از هرماه شمسی » ومغان این روز را ا‬
 ‫مبارك دانند وجشن کنند وعیدسازند وصورتي از‬                   ‫دبال = بروزن تیتال‪ ,‬نام شخصی است‬
   ‫ننرد‬
      ‫هه گ‬
         ‫ارا‬
           ‫گل با از خمیر نان بازند و در‬                  ‫ودیبال پور که قصبه ابت در ملك‌پنجاب‪ .‬اوبتا‬
                                                                                                           ‫کرد ‪.‬‬
 ‫وتعظیم کنند چنانکه ملوك وسلاطین را میکنند‬
  ‫ومد ازآن بوزانند ‪ ,‬وفطام فرسون درین روز‬                ‫دیباو ند ‪ - ۱‬بروزن خویشاوند‪ .‬لقب‬
 ‫بوده بعنی درین روز از شیر بازشده و درین روز‬             ‫طهمورت دیوبند است » و مفنی آن تمام سلاح‬
 ‫ب رگاو نشسته وزردشت درین روز از ابران ببرون‬                                                                ‫باشفد ‪.‬‬

 ‫هکه سوسن‌دود‬
            ‫‪.‬وبند در شب ابن روز ر‬
                                ‫رفت ک‬                    ‫دییاه ‪ ۴‬د بروزن بیراه" نوعی آزقماش‬
 ‫کند تمام سال بفراغت کذراند و از قحطی‬                                                         ‫کران مابه است ‪.‬‬
 ‫و دروشی ایمن باشد وهر که بامداداین روزسیب‬
‫بخورد و ر گس ببوید تمام سال بی آزار باشد‬
                                                         ‫رته ‪ -‬دببابرا‬
                                                                     ‫دیبای پخته پدخ‬
 ‫وبراحت بگنراند » ودرین روز نك است صدقه‬
                                                                  ‫گوبند کهتاروپودش هيچيك خام نباشد ‪.‬‬
                ‫دادن وتزد ملوك و بز رکان رفتن ‪.‬‬          ‫دییدار ‪ ۴‬س بکر اول و دال ابجد‬
                                             
===== leaf 370 printed 908
 ‫=‬                                                                                                    ‫دیع‬

‫دیده بان ‪ ۲‬س بروزنبی‌زبان» همان‬                           ‫یدبدا س بفتح اول بروزن شیدا » بمعنی‬
            ‫دیدیان است که بعربی ربیثه خوائند ‪.‬‬                                      ‫وم شده باشد ‪.‬‬
                                                                                                ‫تاپیدا ک‬
‫دید بانان عالم ت کنابه از هفت‬
                                                          ‫د دار ‪ ۱‬عم بر وزن دیوار » ترجمهةٌ‬
‫ک وکباست کهزحل‌ومشتری‌ومرشو فتاب‌وزهره‬                     ‫روت است ‪ -‬وبمعنی رخ وروی وچهره باشد ‪-‬‬
                             ‫وعطارد وماه باشد ‪.‬‬           ‫ویمعتی رخ لمودن ردیدن هم هست ‪ - ۴‬وچشم‬
‫دید م بان فلك ‪ -‬کنابهاز کوکبزحل‬                           ‫ویاعيننند ‪ -‬و ببنابی‬  ‫خرب‬
                                                                                  ‫کاویبزندکه یم‬‫ر‬
                    ‫است که درفلك هفتم میباشد ‪.‬‬             ‫وقوت باسرء رایز کفته‌اسوبمعنی پیدا ویدیدار‬
 ‫دیده بان کبود حصار ک‪-‬نابه‬                                                                          ‫همهت ‪.‬‬
‫از زحل است ‪ -‬وهربك اکزواکب سبع سیاره‬                       ‫بابای‌ابجدبروزن رسمان‪,‬‬        ‫دید بان ‪۴‬‬
                          ‫را بگیوزبند ‪.‬‬                  ‫شخصی را کویند که برجای بلند مانند سرکوه‬
‫‪ ۵‬بك ه بر داشتی د کنابه از منتظر‬                           ‫و بالای کشتی شیند وهرچه ازدوربیند خبردهد‬
                      ‫بودن وانتظار کشیدن باشد ‪.‬‬                          ‫نند ‪#.‬‬   ‫ایه‬‫ور‬
                                                                                      ‫خریی‬
                                                                                         ‫و او را خ‬
‫دة لشت = منم بای فارسی ‪ .‬اشاره‬
                             ‫د‬                             ‫‪ ۵‬بد ه = بااول بثالی رسیده وفتح‌ثالك‬
        ‫بمنفذ سفلی است که صوراخ مقعد باشد ‪.‬‬
                                                          ‫چشم را کوبند (‪ -)۱‬و بعضی مردمك چشم را‬
‫ذبده دار د بروزن کیسه دار» بمعنی‬                           ‫گفتماند؟ ‪ -‬وبمعنی‌مرگی ومشاهده شده‌باشد ‪۵‬‬
‫دیده بان است» و اوشخصی‌باشد که برجای بلندی‬                 ‫ودرخت‌بلند و کوه بلند رایز گوبند که‌دیده‌بانان‬
            ‫شیند وآنجه از دور بیند خبردهد ‪.‬‬                ‫نگاء کنند ‏ ‪ -‬وماضی‌دیدن‬       ‫مربالای آن سته‬
‫دیدة کافوری ‪ -‬کنابه از ایا‬                                 ‫هم هت یعتی پیش ازن دیده بود ‪ -‬و بمعئی‬
                                             ‫باشد ‪۰‬‬
```


## [2026-09-05T20:58:14.731Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\np=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nimport re\nfor i in range(360,380):\n    t=p[i]\n    m=[x for x in re.findall(r'بقی[هة][^\\n]{0,40}', t)]\n    if m: print(i, m)\n\"",
 "description": "Find footnote continuations near day"
}
```


### [2026-09-05T20:58:16.775Z] TOOL RESULT

```
367 ['بقیه درصفحةٌ \u202a۸۰٩\u202c\u200f\u202c']
```


## [2026-09-05T20:58:27.573Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\np=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef num(s):\n    return int(''.join(str(fa.index(c)) for c in s))\nfor i in list(range(360,375))+list(range(485,500)):\n    t=p[i]\n    cands=set()\n    for m in re.finditer('[%s]{3,4}'%fa, t):\n        try:\n            v=num(m.group())\n        except: continue\n        if 850<v<1100: cands.add(v)\n    print(i, 'l+538=',i+538,'l+540=',i+540, sorted(cands))\n\"",
 "description": "Extract candidate page numerals"
}
```


### [2026-09-05T20:58:29.405Z] TOOL RESULT

```
360 l+538= 898 l+540= 900 [893]
361 l+538= 899 l+540= 901 []
362 l+538= 900 l+540= 902 [851]
363 l+538= 901 l+540= 903 [985]
364 l+538= 902 l+540= 904 []
365 l+538= 903 l+540= 905 []
366 l+538= 904 l+540= 906 []
367 l+538= 905 l+540= 907 []
368 l+538= 906 l+540= 908 [950]
369 l+538= 907 l+540= 909 []
370 l+538= 908 l+540= 910 []
371 l+538= 909 l+540= 911 []
372 l+538= 910 l+540= 912 []
373 l+538= 911 l+540= 913 []
374 l+538= 912 l+540= 914 [900]
485 l+538= 1023 l+540= 1025 []
486 l+538= 1024 l+540= 1026 []
487 l+538= 1025 l+540= 1027 [901]
488 l+538= 1026 l+540= 1028 [883]
489 l+538= 1027 l+540= 1029 [851, 921]
490 l+538= 1028 l+540= 1030 [991]
491 l+538= 1029 l+540= 1031 []
492 l+538= 1030 l+540= 1032 [857, 933]
493 l+538= 1031 l+540= 1033 [1031]
494 l+538= 1032 l+540= 1034 [991]
495 l+538= 1033 l+540= 1035 []
496 l+538= 1034 l+540= 1036 []
497 l+538= 1035 l+540= 1037 []
498 l+538= 1036 l+540= 1038 [991]
499 l+538= 1037 l+540= 1039 [982]
```


## [2026-09-05T20:59:21.522Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK leaf 82 (p426) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==83' POK_02.txt | head -40",
 "description": "Pokorny p.426"
}
```


### [2026-09-05T20:59:23.203Z] TOOL RESULT

```
=== POK leaf 82 (p426) ===
Thurneysen  KZ.  59,  2,  8;  61,  253);  acymr.  gaem.^  ncymr. gauaf)  acorn.  goyf,  bret.  goaJW,  gall.  Wintermonat  Giamon\ios\,  Eigenname
426  ,
Giamülus,    weitergebildet   mir.   gem-rad   n.,   mcymr.   gaeaf-raicd   ,Wintei (*ghii,mo-röto-,  zu  ret-  ^laufen') ;  auch  ir.  gamuin  ^jähriges  Kalb';
aisl.  göi  f.  und  gx  t,  göi-mänadr  ,der  Monat  von  Mitte  Februar  bis Mitte  März^  isl.  göa,  u.  f.,  norw.  gje  L,  schwed.  göjemänad  (gö-  <  giö-  nach Bugge  Ark.  f.  nord.  Fil.  4,  123  ff.).
Fraglich  die  Anreihung  von  an.  gcmall  ,^\l',  gemlingr  .jähriges  Schaf« ags.  gamol  ,alt',  gamellan  ^altern',  as.  gigamalod  ,bejahrt'_,  ahd.  nur  in Ei<''ennamen  wie  Gamalholdy  Gamalherht,  Gamalbevga  usw.  als  , bejahrt* vffl.  lat.  annösiis.
C.  ghimo-  (aus  ghi-mn-o-?):
Ai.  himd-h  m.  J\älte,  Frost,  Schnee',  Mmä  f.  ,Winter',  av.  zdmaka-  m, ,Wintersturm'  (vgl.  den  Gen.  von  zyäizimö  unter  B.);
^v.  Svaxi^tog  ^winterlich,  stürmisch',  6  yjfxagog  , Ziegenbock',  gj  X^hCiQog ,die  einjährige  (Ziege)',  %ii.iaiQa  ;Ziege',  lat.  hlmus  (<  HiUmos),  trimui^ quadrimus  ,zwei-  usf.  jährig'  (vgl.  ved.  satd-hima-  ,hundertjährig'),  norw. dial.  gimber,  schwed.  dial.  gimber^  dän.  gimmerlam  , weibliches  Lamm', dial.  aber  ^einjähriges  Lamm'  (Pedersen  KZ.  32,  248),  andfrk.  (Lex  Salica) ingimus?  ,porcus  anniculus'.  Die  Formen  mit  y:  aisl.  gymbr  , ein  jährige Sau',  norw.  gymber,  schwed.  gymmer  ,Lamm'  beruhen  wahrscheinlich  au£ Einfluß  des  nicht  verwandten  —  übrigens  ungedeuteten  —  aisl.  gymhill^ PN  GumbuU,  aschwed.  guwmerlamb  ,Widder',  isl.  gummarr,  norw.  gumse, schwed.  gumse  ,Widder',  siehe  Hellquist  SvEO.  210.
WP.  I  546  ff.,  WH.  I  106,  645  f.,  Trautmann  367,  Specht  KZ.  53,  307  f.
gheidh-  , begehren,  gierig  sein';  gheidh-tlo-  , Bürgschaft,  Pfand';  vgl.  gheigh-,
Air.  glall  =  cymr.  givystl,  acorn.  guisfel  , Geisel',  bret.  goestl  ,gage, caution',  gall.  in  Congeistlus  MN.  (cymr.  cyngwystl  , Verpflichtung')  =  ahd. gisal,  nhd.  Geisel,  ags.  gisel,  aisl.  gisl  ds. ;  die  genaue  Übereinstimmung zw.  Germ,  und  Kelt.  spricht  vielleicht  für  Entlehnung  seitens  des  Germ.; got.  PN  Glsla-mun-dus  \  daneben  ohne  l:  got.  PN  Ända-gls,  ags.  Gls-ioulf, ahd.  Glsi-ulf,  vgl.  mnd.  glse  , Geisel'.
Mit  Ablaut  hierher  ir.  gell  , Einsatz,  Pfand'  {^ghistlo-),  wovon  das  Verbum air.  gell-,  gill-  ,to  pledge,  promi
```


## [2026-09-05T20:59:23.961Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ zamharir ===\" && grep -n -i \"zamharir\\|zamharīr\\|زمهرير\\|زمهریر\" FVQ.txt FVQ_pages.txt | head -20 && echo \"=== AFM ===\" && grep -n \"زمهرير\\|زمهریر\" AFM.txt AFM_pages.txt TAD.txt ARB_mo3rb.txt 2>/dev/null | head -20",
 "description": "Jeffery / Addi Shir zamharir"
}
```


### [2026-09-05T20:59:24.033Z] TOOL RESULT

```
=== FVQ zamharir ===
=== AFM ===
```


## [2026-09-05T20:59:34.466Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FVQ.txt AFM.txt AFM_alt.txt TAD.txt ARB_mo3rb.txt ARB_abdulraheem.txt LKT.txt; do echo \"--- $f\"; grep -n \"مهرير\\|مهریر\\|amharir\\|amharīr\" $f 2>/dev/null | head -5; done",
 "description": "Search Arabic loan books for zamharir"
}
```


## [2026-09-05T20:59:36.129Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ghiem ===\" && grep -n \"ghiem\\|gheim\\|ĝhiem\\|hiems\\|hibernus\" IEC.txt | head -15 && echo \"=== LEW hiems ===\" && grep -n \"^hiems\\|hiems,\" LEW_1910.txt LAT.txt | head -10",
 "description": "Mann and Latin dictionaries"
}
```


### [2026-09-05T20:59:36.291Z] TOOL RESULT

```
--- FVQ.txt
--- AFM.txt
--- AFM_alt.txt
3109:3 ( از مهریر) ا ارد عر دة من دم ا ومن هر پر اې م وج وقالوا 
--- TAD.txt
--- ARB_mo3rb.txt
--- ARB_abdulraheem.txt
--- LKT.txt
```


### [2026-09-05T20:59:36.354Z] TOOL RESULT

```
=== IEC ghiem ===
5963:Sheim-, gheimn- (ghim-) (resolutions of a prototype *ghiiom-, see £hiia- & extns.) WP I, 546 Skt. cf. himáh, himàá, hemantáh; himám
5965:‘snow, ice’; Av. Zima, gs zimahe, id. (and *year?); zim, m. id.; Per. cf. zim-istan, id.; Oss. zímág, zumág, dim. type, id.; Gk. kheima; Alb. dimén, T dimér; Lat. hiems, cf. bimus (for *dui-himos ‘two winters old); MIr. gaim, gemred; Gaul. giam-; Sequanian giamon ‘snow’; W gauaf, pl. -oedd; Br. goanv, goan, Vannes: guian; OCS zima (and com. Sl.); Li. žiemà; Latv ziema, id. Variant in Gk. khei- món, id.
6058:£hiiün- “winter; snow”. (lit. the empty per- iod"? Cf. &hiia & derivs.) Av. zyaO, acc. zyàm “winter frost; zayano ‘wintry’; Arm. dziwn, gs dzean ‘snow’; Gk. khión, gs -onos, id. Cf. perhaps Lat. hiems, if for *&hi-ambhs, cf. ambhmn-. WP I, 547
=== LEW hiems ===
LAT.txt:27927:hiems dans toutes les langues romanes, M.L.4136; et le denominatif
LAT.txt:27949:Les formes de hiems,-himus et hibernus sont tontes anciennes.
```


## [2026-09-05T20:59:41.795Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T20:59:41.801Z] TOOL RESULT

```


```


## [2026-09-05T20:59:42.571Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 27915,27960p LAT.txt",
 "description": "Ernout-Meillet hiems"
}
```


### [2026-09-05T20:59:42.619Z] TOOL RESULT

```
et Lucrbce, Cdsar, Varron, et le plus souvent Cic 4 ron emploient Aiens
au sens de "hiver", cf. Enn., A.434, aestatem autumnus sequitur, post
acer hiemps it. Ancien, usuel. Non roman (cf. plus bas).
D 4 riv 4 s et compos 4 s: 1° hiemSlis: d'hiver; tempetueui; nauigatio
longa et hiemalis, Cic.Fam.6,30,1; hiemo,-as: 1° passer 1 'hiver (dans
ce sens tend k etre remplacd par hiberns) ; 3 0 etre en- tempete, hiemat
mare Hor., Sat .3,3,17 (cf. x®Mx^l- 1 ® 1,vw ) > 3° impersonnel, hiemat
"c^st 1 'hiver, il fait- froid"; 4 0 faire refroidir, congeler (Pline);
hiematio; exhiemS (ital.); perhiemo (d'aprbs pernoctd , Colum.).
3° hibernus: d'hiver; de IA hiberna n.pl.: quartiers d'hiver, et
a basse 4 poque hibernum (sc .tempus) (a partir de Minue. Fel., cf.
aussi Vg. En.i,aCC) "hiver" ( hibernus , Mul.Chir.) qui a remplac 4
hiems dans toutes les langues romanes, M.L.4136; et le denominatif
hiberno,-ds: hiverner. Panroman. M.L.4134, et exhibernare , 30iab;
hiberndlis (cf. autumnalis), hiberndculum (epoq. imper. ), hibernatio
(Gl,).
Une forne k degre zero *him- figure dans des adjectifs composes
bimus (de dwi-him-os), trimus, quadrimus "de deux, trois, quatre
ans", mots de la langue rurale, s*appliquant aux animaux qui, nes
au printemps, en 4 t 4 ou en fin d'annee, ont passe deux, trois» quatre
hivers, par opposition a hornus, anniculus et annotinus. L'origine
de ces adjectifs n'avait pas 4 chapp 4 aux anciens, cf. Cassiod.(ex
Eutyche), GLK VII 300,5, bimus, trinus, quadrimus quasi a bis, ter,
quater, hieme dicta. Ces adjectifs, en passant dans la langue commune,
se sont ensuite appliques aux enfants; mais dans les 1. romanes iis
n'ont surv 4 cu qu'avec leur valeur ancienne, cf.M.L.1107 bimus , 8907
trimus, 6q 19 quadrimus. De bimus, trimus, quadrimus existent aussi
les d 4 riv 4 s bimulus, bimatus, et bimatus,-us m."age de deux ans", etc.
Il n'y a pas d'adjectif pour dire "d'un hiver" (tandis que le gree a
Xi>|iapoC, le latin recourt k des d 4 rives (r 4 cents) de annus; anniculus.hietO
5»4
annStinusi v. Meillet, MSL «3,146. Aprfcs quadrimus on a des compos£s
de annus: quinquennis, sexennis, etc. M.W.Schulze a note que Horaee
oppose bimum, quadrimum merum k ulnum quinquenne.
Les formes de hiems,-himus et hibernus sont tontes anciennes.
Elies appartiennent k nne racine indo-europeenne designant les frimas,
1'hiver, la neige.
Le mot hiems est d'un type archalque; il repo se snr nn theme indo-
enropeen a vocalisme radical z 4 ro g'hi — snivi d'un 41 ement -em-
qui ne se retrouve guere a l^tat de suffixe. Le «eme mot existe en
iranien, oh 1 1 on a av. zya, g£n .zim 5 , au sens de "hiver". - Le meme
vocalisme que dans hiems apparait dans un nom de la "neige 11 : gr. )(l,a)V
(gen. yiovoc), arm. j ivm (gen. jeon); le latin a un autre nom de la "neige"
aussi indo-europ^en, nix. - Pour la racine,.cf. av. zayana- "d'hiver".
En face de cette forme, il y a des derives i vocalisme radical
e-. En -a-: v.sl. zima, lit. Memh. Souvent un mot en -n-/-r-, notamment
```


## [2026-09-05T20:59:49.855Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0e%C9%AAm-",
 "prompt": "Give the reconstructed PIE root form, its meaning, and the list of descendants (especially Indo-Iranian, Latin, Greek). Quote the etymology/derived-terms section."
}
```


### [2026-09-05T20:59:52.055Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T20:59:52.066Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%85%D8%B3%D8%AA%D8%A7%D9%86",
 "prompt": "Give the full Persian etymology of زمستان (zemestân): Middle Persian form, Old Iranian/Avestan antecedents, Proto-Iranian reconstruction, and any cited references (Hasandust, MacKenzie, Cheung)."
}
```


### [2026-09-05T20:59:58.279Z] TOOL RESULT

```
# Persian Etymology of زمستان (zemestân)

## Middle Persian
The word is "inherited from Middle Persian \[script needed\] (ẕmstʾn' /⁠zamestān⁠/), borrowed from a Northwestern Iranian language."

## Proto-Iranian Components
The term combines two Proto-Iranian elements:
- **\*jimáh** (the "winter" root)
- **\*stā́nam** (a locative/place suffix)

## Indo-European Ancestry
The etymology traces back through Proto-Indo-Iranian *ȷ́ʰimás to Proto-Indo-European *ǵʰimós, which itself derives from the root *ǵʰey- meaning "winter."

## Cognates
Related forms appear across Iranian languages (Northern Kurdish *zivistan*, Ossetian *зымӕг*) and extend to other Indo-European branches, including Latin *hiems* and Sanskrit *himá*.

**Note:** The page does not cite specific scholarly references (Hasandust, MacKenzie, or Cheung) for its etymological reconstruction.
```


## [2026-09-05T21:00:05.745Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C",
 "prompt": "List all Persian etymologies given for دی: the month name, the word meaning \"winter/frost\", and \"yesterday\". For each give the Middle Persian, Old Persian/Avestan and Proto-Iranian antecedents and any cited references."
}
```


## [2026-09-05T21:00:06.751Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ey-",
 "prompt": "Give the PIE root form, meaning, and descendants/derived terms listed."
}
```


### [2026-09-05T21:00:13.456Z] TOOL RESULT

```
# Persian Etymologies for دی

Based on the Wiktionary entry, here are the Persian etymologies:

## Etymology 1: "Yester" (Archaic Adverb)
- **Middle Persian**: /⁠dīk⁠/ [term marked as request]
- **Proto-Indo-Iranian**: *ȷ́ʰyás
- **Proto-Indo-European**: *dʰǵʰyés
- **References**: None cited

## Etymology 2: Month Name & "Mother" (Noun/Proper Noun)
- **Middle Persian**: ddw' (Day, "Creator")
- **Old Persian/Avestan**: Not provided
- **Proto-Iranian**: Not provided
- **References**: None cited

## Etymology 3: Letter "D" (Noun)
- **Source**: "Borrowed from English dee"
- **Middle Persian/Proto-Iranian**: Not applicable (modern borrowing)
- **References**: None cited

**Note**: The entry contains incomplete etymological information. Most pathways lack Proto-Iranian or Old Persian/Avestan intermediates, and no scholarly references support these etymologies beyond the single Pashto citation referencing Kreidl (2021).
```


### [2026-09-05T21:00:14.974Z] TOOL RESULT

```
# Proto-Indo-European Root *ǵʰey-

## Root Form
**\*ǵʰey-**

## Meanings
The root has two distinct etymologies:

1. **Winter** (Etymology 1) - though "the existence of this root is uncertain"
2. **To drive, propel** (Etymology 2)

## Key Derived Terms and Descendants

**From Etymology 1 (winter):**
- \*ǵʰéy-mn̥ ~ \*ǵʰi-mén-s
- \*ǵʰéy-ōm ~ \*ǵʰi-m-és

**From Etymology 2 (drive):**
- Sanskrit: हि (hi), हिनोति (hinóti "drives"), हेमन् (hemán "impulse, zeal, driving")
- Avestan forms showing causative derivations
- Proto-Balto-Slavic: \*źṓjinkas

The root demonstrates various verbal formations including athematic aorists, new-presents, and eye-causatives across Indo-Iranian and other language families.
```


## [2026-09-05T21:00:35.486Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/calendars",
 "prompt": "What is said about the origin of the month name Day (Dai/Dey), the tenth month? Does it derive from Avestan daθuš- \"creator\" (epithet of Ahura Mazda)? Quote the relevant passage. Also list the Zoroastrian month names and their meanings."
}
```


## [2026-09-05T21:00:36.294Z] TOOL CALL #42: WebSearch

```json
{
 "query": "شمیران وجه تسمیه سمیران زم سرد ریشه‌شناسی"
}
```


### [2026-09-05T21:00:37.209Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T21:00:48.595Z] TOOL RESULT

```
Web search results for query: "شمیران وجه تسمیه سمیران زم سرد ریشه‌شناسی"

Links: [{"title":"شمیران - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%B4%D9%85%DB%8C%D8%B1%D8%A7%D9%86"},{"title":"سمیرم - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.m.wikipedia.org/wiki/%D8%B3%D9%85%DB%8C%D8%B1%D9%85"},{"title":"شمیران - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%B4%D9%85%DB%8C%D8%B1%D8%A7%D9%86/"},{"title":"وجه تسمیه نام تهران و محلات آن؛ از طهران تا تهران - کجارو","url":"https://kojaro.com/2021/9/22/192393/tehran-neighborhoods-name-meaning"},{"title":"شهربَراز: نام تهران","url":"http://shahrbaraz.blogspot.com/2008/02/blog-post_20.html"},{"title":"وجه تسمیه نام بسیاری از محلات پایتخت + تصویر كمیاب از تهران قدیم","url":"https://www.shafaf.ir/fa/news/36981/%D9%88%D8%AC%D9%87-%D8%AA%D8%B3%D9%85%DB%8C%D9%87-%D9%86%D8%A7%D9%85-%D8%A8%D8%B3%DB%8C%D8%A7%D8%B1%DB%8C-%D8%A7%D8%B2-%D9%85%D8%AD%D9%84%D8%A7%D8%AA-%D9%BE%D8%A7%DB%8C%D8%AA%D8%AE%D8%AA-%D8%AA%D8%B5%D9%88%DB%8C%D8%B1-%D9%83%D9%85%DB%8C%D8%A7%D8%A8-%D8%A7%D8%B2-%D8%AA%D9%87%D8%B1%D8%A7%D9%86-%D9%82%D8%AF%DB%8C%D9%85"},{"title":"سوماموس یا سماموث ؟! - پایگاه خبری تحلیلی رانکوه نیوز","url":"https://rankoohnews.ir/%D8%B3%D9%88%D9%85%D8%A7%D9%85%D9%88%D8%B3-%DB%8C%D8%A7-%D8%B3%D9%85%D8%A7%D9%85%D9%88%D8%AB-%D8%9F/"},{"title":"معرفی شهرستان سمیرم – سمیرم سفر","url":"https://semiromsafar.com/moarefi-semirom/"},{"title":"شمیران , شمال تهران و منطقه شمیرانات ( شمیران , شمرون , شمیرانات ) - فن و هنر","url":"https://ashwood.ir/%D8%B4%D9%85%DB%8C%D8%B1%D8%A7%D9%86-%D8%B4%D9%85%D8%A7%D9%84-%D8%AA%D9%87%D8%B1%D8%A7%D9%86-%D9%88-%D9%85%D9%86%D8%B7%D9%82%D9%87-%D8%B4%D9%85%DB%8C%D8%B1%D8%A7%D9%86%D8%A7%D8%AA-%D8%B4%D9%85/"}]

بر اساس نتایج جستجو، اطلاعات مفصلی درباره وجه تسمیه و ریشه‌شناسی نام‌های شمیران، سمیران و سمیرم یافت شد:

## وجه تسمیه و ریشه‌شناسی

شمی، سمی و زمی در زبان‌های کهن به‌معنای سرد است و جاهایی که در نامشان بخش شمی یا سمی پدید آمده‌، جاهای سردسیر است مانند شمیرم و سمیرم و سمیران و شمیران.

احمد کسروی ریشه لغوی نام این منطقه را چنین دانسته‌است: «ران» به معنی جایگاه و سرزمین است، و «سمی» یا «شمی» به معنای سرد است و لذا شمیران به معنای جای سرد یا سردسیر است.

زم همان است که در زمستان به معنای زمان سرما می‌بینیم.

## ارتباط بین نام‌ها

منطقی‌ترین رویکرد این است که نام سمیرم را به زمیران، سمیران یا شمیران نسبت دهیم، که در آن شم یا سم به معنای سرد و ران یا رام به معنای مکان است.

به‌طور خلاصه، تمام این نام‌ها (شمیران، سمیران، سمیرم، و تغییرات دیگری مانند شمیرم) ریشه مشترکی دارند که به معنای "جای سرد" یا "منطقه سردسیر" است.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T21:00:54.169Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hibernate",
 "prompt": "Give the full etymology of hibernate and hibernal/hibernus, including the PIE root and cognates cited."
}
```


## [2026-09-05T21:00:55.190Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Himalaya",
 "prompt": "Give the etymology of Himalaya: the Sanskrit source, its components (hima + ālaya), meaning, and how it entered English."
}
```


### [2026-09-05T21:01:00.048Z] TOOL RESULT

```
I cannot provide the etymology you've requested based on the content supplied. The Wiktionary page for "Himalaya" does not include etymological information about the Sanskrit origin, component breakdown (hima + ālaya), or how the term entered English.

The page offers definitions across multiple languages and pronunciation guides, but lacks the historical linguistic details necessary to explain the word's Sanskrit roots or semantic composition.
```


### [2026-09-05T21:01:01.065Z] TOOL RESULT

```
# Etymology of Hibernate and Hibernal

## Hibernate (verb)
The term emerged in 1802, likely as a "back-formation from hibernation." It means to "pass the winter in torpidity and seclusion."

## Hibernation (noun)
Dating to the 1660s, this referred to "action of passing the winter" of plants and insects, deriving from Latin *hibernationem*, which comes from *hibernare* "to winter, pass the winter, occupy winter quarters."

## PIE Root: *gheim-
The ultimate source is the Proto-Indo-European root "*gheim-" meaning "winter." This root connects to the Latin *hiems* "winter."

## Cognates
The root appears across multiple language families:
- Sanskrit: *heman* "in winter"
- Hittite: *gimmant-*
- Armenian: *jmern*
- Greek: *kheima* and *khion* "snow"
- Old Church Slavonic: *zima*
- Lithuanian: *žiema* "winter"

## Hibernal
While not explicitly detailed separately in the source, *hibernal* is listed among words formed from or containing the *gheim-* root, indicating it shares the same Latin-derived "winter" etymology as related terms like hibernacle.
```


## [2026-09-05T21:01:04.494Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B9%E0%A4%BF%E0%A4%AE%E0%A4%BE%E0%A4%B2%E0%A4%AF",
 "prompt": "Give the Sanskrit etymology of हिमालय (himālaya): its components, meaning, and the etymology of हिम (hima)."
}
```


## [2026-09-05T21:01:05.326Z] TOOL CALL #46: WebSearch

```json
{
 "query": "Encyclopaedia Iranica month name \"Day\" Avestan \"daθuš\" creator tenth month Zoroastrian calendar"
}
```


### [2026-09-05T21:01:10.065Z] TOOL RESULT

```
# Sanskrit Etymology of हिमालय (himālaya)

**Components:**
The word is a compound of two Sanskrit elements: हिम (hima, "snow, frost") + आलय (ālaya, "house, dwelling").

**Meaning:**
The compound literally translates to "abode of snow" or "dwelling of frost," which refers to the Himalayan mountain range.

**Etymology of हिम (hima):**
According to the Wiktionary entry, हिम derives from "the Proto-Indo-European root *ǵʰey- (winter)," establishing its ancient linguistic ancestry in the Indo-European language family.

**Mythological Significance:**
In Hindu tradition, हिमालय also personifies the mountain range as a deity—specifically, the husband of Menaka and father of both Parvati (consort of Shiva) and Ganga (the personified Ganges river).
```


### [2026-09-05T21:01:15.267Z] TOOL RESULT

```
Web search results for query: "Encyclopaedia Iranica month name "Day" Avestan "daθuš" creator tenth month Zoroastrian calendar"

Links: [{"title":"DAY - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/day/"},{"title":"Vol. VII, Fasc. 2, pp. 163-164 1 DAY","url":"https://www.iranicaonline.org/articles/day/?generate_pdf=1"},{"title":"CALENDARS - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/calendars/"},{"title":"Iranian calendar | Familypedia | Fandom","url":"https://familypedia.fandom.com/wiki/Iranian_calendar"},{"title":"The happiest month, the month of the Creator | Authentic Gatha Zoroastrianism","url":"https://authenticgathazoroastrianism.org/2015/01/05/the-happiest-month-the-month-of-the-creator/"},{"title":"Zoroastrian Religious Calendar Month Names","url":"https://www.avesta.org/zcal_months.htm"},{"title":"Zoroastrian calendar - Wikipedia","url":"https://en.wikipedia.org/wiki/Zoroastrian_calendar"},{"title":"Ameretat","url":"https://en.wikipedia.org/wiki/Ameretat"},{"title":"Daena","url":"https://en.wikipedia.org/wiki/Daena"}]

Based on the search results from Encyclopaedia Iranica, here is the information you requested:

DAY is an epithet of Ahura Mazdā (meaning "creator") that became the name of the tenth month, as well as of the eighth, fifteenth, and twenty-third days in each month of the Zoroastrian calendar.

The Younger Avestan form daδuuah-/daθuš– is a perfect active participle of the verb dā-, meaning "to place, put, create." In the calendar reform in the 5th century B.C.E., the tenth month was named daθušō (māh-) "(month) of the creator."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T21:01:21.305Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/day/",
 "prompt": "Quote the full article DAY: the Avestan form, its meaning, the calendar reform, and any mention of a rival derivation from Avestan zyā-/zaēn- \"winter\"."
}
```


### [2026-09-05T21:01:23.120Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T21:01:23.941Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON himalaya ===\" && grep -n \"هیمالیا\\|هیمالا\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10 && echo \"=== ARY ===\" && grep -n \"زمستان\\|هیمالیا\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Mo'in and Aryanpur lookups"
}
```


### [2026-09-05T21:01:24.018Z] TOOL RESULT

```
=== MON himalaya ===
MON_part1.txt:2367:قلل هیمالیا زندگی می‌کند. 
MON_part1.txt:23013:کوه‌های هیمالیا و هندوکش فراوان است و 
MON_part1.txt:81271:هیمالیا می‌باشد؛ سوسن ختایی» سوسن 
=== ARY ===
```


## [2026-09-05T21:01:31.797Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"زمس\\|زمستا\" ARY_pages.txt | head -10; echo \"--- latin index ---\"; grep -n -i \"ghei\\|gheim\\|ZEMEST\\|ZAMEST\\|HIMA\" ARY_latin_index_pages.txt | head -20",
 "description": "Aryanpur lookups"
}
```


### [2026-09-05T21:01:31.858Z] TOOL RESULT

```
300:گزمسیری می‌بود در حالیکه تفریباً همه‌ی واژه‌های گرمسیری و استوایی از ریشه‌ی هند و اروپایی
--- latin index ---
4088:BAILES, LATVIAN) (33) gig BHAYA, BHIMA, BIBHETI, BHAYATE
9383:ZIMA A(CZECH) “So ZAM., ZAMESTAN (PAHLAVI) 5 shy
11127:SHIMARTIN, ASHMARDIN,
11128:‘REFERENCES both, ISHMAR, ZHIMARTIN
```


## [2026-09-05T21:01:32.426Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.avesta.org/zcal_months.htm",
 "prompt": "List the Zoroastrian month names with their Avestan forms and meanings, especially the tenth month Day/Dae."
}
```


### [2026-09-05T21:01:57.836Z] TOOL RESULT

```
# Zoroastrian Calendar Month Names

Here are the twelve religious calendar months with their Avestan forms and meanings:

1. **Frawardin** - The Guardian Spirits or Angels
2. **Ardwahisht** - "Highest Asha," one of the Amesha Spentas
3. **Hordad** - "Wholeness (Perfection or Health)," presides over waters
4. **Tir** - Tishtrya, the Star Sirius
5. **Amurdad** - "Immortality or Life," presides over plants
6. **Shahrewar** - "Desirable Dominion," presides over metals
7. **Mihr** - Mithra, Yazad of the Contract
8. **Aban** - Waters
9. **Adar** - Fire
10. **Day** - "The Creator"
11. **Vohuman** - "Good Mind or Purpose," presides over animals
12. **Spandarmad** - "Holy (or Beneficent) Devotion," presides over the Earth

The tenth month, Day, represents the divine creator principle. Most months are associated with the Amesha Spentas (divine entities in Zoroastrianism) and govern natural elements like water, fire, metals, plants, and animals.
```


## [2026-09-05T21:02:02.139Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n 9370,9395p ARY_latin_index_pages.txt && echo \"---- page tag ----\" && awk 'NR>=9300 && NR<=9390 && /pdf page/' ARY_latin_index_pages.txt | tail -3",
 "description": "Aryanpur index context"
}
```


### [2026-09-05T21:02:04.082Z] TOOL RESULT

```
SKEAT: (GHOST) 238 JEST, GAST (OLD FRISIAN) Ss p35
ent ‘bi oby HOLD HIGH GERMAN) pS gS
HED, HEDAH, GEIST
. seat look
seth Cotas Gy sT etd (Bile toy “abla cal eT 6
” CCI Sil sy BUNT J2 5s eal eg
[pdf page 324]
(
yrO | ok
|

ZIMA RUSSIAN) .ya3 ZA, ZYAM, ZAEM :(AVESTAN) pls)

ZIMA A(CZECH) “So ZAM., ZAMESTAN (PAHLAVI) 5 shy

ZIMA (SERBIAN) g po ZIMAG, ZUMAG —(OSSETIC) 51

ZIMA BOHEMIAN) gad y ZIVISTAN ARURDISH) 635

ZIMA x(SLOVAK) S'\ Lal ZHEMAY HAFGHAND (32%), gi)
ZHIEMA :(LITHUANIAN) |i HEMAN, SSANSKRIT) cy Sait |
ZIEMA LATVIAN) (3) 6) HEMANTAS, HEMA-

GIAMONIOS HGAULISH) JS JIUN, ZMERN- (ARMENIAN) |

DIMEN ALBANIAN) UT KHEIMON GREER) gli
---- page tag ----
[pdf page 322]
[pdf page 323]
[pdf page 324]
```


## [2026-09-05T21:02:11.138Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"ZAEM\\|ZYAM\\|GHEI\\|HIMA-ALAYA\\|HIMALAYA\" ARY_pages.txt | head -20",
 "description": "Find ARY main entry"
}
```


### [2026-09-05T21:02:11.180Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:02:19.149Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && awk '/\\[pdf page 324\\]/,/\\[pdf page 325\\]/' ARY_latin_index_pages.txt | head -60",
 "description": "ARY pdf page 324 full"
}
```


### [2026-09-05T21:02:56.893Z] TOOL RESULT

```
[pdf page 324]
(
yrO | ok
|

ZIMA RUSSIAN) .ya3 ZA, ZYAM, ZAEM :(AVESTAN) pls)

ZIMA A(CZECH) “So ZAM., ZAMESTAN (PAHLAVI) 5 shy

ZIMA (SERBIAN) g po ZIMAG, ZUMAG —(OSSETIC) 51

ZIMA BOHEMIAN) gad y ZIVISTAN ARURDISH) 635

ZIMA x(SLOVAK) S'\ Lal ZHEMAY HAFGHAND (32%), gi)
ZHIEMA :(LITHUANIAN) |i HEMAN, SSANSKRIT) cy Sait |
ZIEMA LATVIAN) (3) 6) HEMANTAS, HEMA-

GIAMONIOS HGAULISH) JS JIUN, ZMERN- (ARMENIAN) |

DIMEN ALBANIAN) UT KHEIMON GREER) gli
KIMANZA HITTITE) esa HIEMS ALATIN) 3

HIVER HPRENCH) Wil

‘REFERENCES both, INVERNO SPANISH) glilyel
POKORNY: ——=ss«~«~C*« DG INVERNO AUTALIAN) gilts!
DELAMARRE: (HIVER) 194 JARNA ARUMANIAN) gles
MACKENZIE: * (WINTER) 140 INVERNO (PORTUGUESE) (Jit 4

BUCK: 1013-1016 OLD CHURCH SLAVIC) 45 53%!
AMINDAROV: (WINTER) 310 ZIMA

FOP g SOTA eG oby ZIMA (POLISH) lng)

: sestloal
1p 5g) 45 92 STUN Go5ls 6 ae
ahn5 lanl Se (gab vadls ale 7 |
few

ZAMIK, ZAMIG HBALUCHI) gr ge ZAM- HMAVESTAN) glu 31

JMAKA AFGHAN] (2%), sual ‘ZAMIK (PAHLAVI) «5 shy

TKAM. :(TOKHARIAN A) A 5) ZAX, ZANXA HOSSETIC) «nl
[pdf page 325]
```


## [2026-09-05T21:03:06.756Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%87%DB%8C%D9%85%D8%A7%D9%84%DB%8C%D8%A7/",
 "prompt": "Quote what Dehkhoda and Mo'in say about هیمالیا: its meaning, Sanskrit origin (hima + alaya), and any note on how the name reached Persian."
}
```


## [2026-09-05T21:03:09.614Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://fa.wikipedia.org/wiki/%D8%B4%D9%85%DB%8C%D8%B1%D8%A7%D9%86",
 "prompt": "Quote the وجه تسمیه / etymology section on the name شمیران: what does شمی/سمی/زم mean, what does -ران mean, and who proposed it (Kasravi?). Also any mention of سمیران، سمیرم."
}
```


### [2026-09-05T21:03:12.786Z] TOOL RESULT

```
# Dehkhoda and Mo'in on هیمالیا

The provided content does not include specific entries or quotes from Dehkhoda's dictionary (لغتنامه دهخدا) or Mo'in's dictionary (فرهنگ معین). While the page mentions these as resources available in the Abadis dictionary system, their actual definitions for هیمالیا are not reproduced here.

However, the page does provide information about the Sanskrit etymology: The name derives from Sanskrit, meaning "place of snow" or "snowland" (برفستان). It combines *hima* (snow/cold) and *alaya* (place/abode).

For the exact Dehkhoda and Mo'in entries on this term, you would need to consult those dictionaries directly.
```


### [2026-09-05T21:03:16.075Z] TOOL RESULT

```
# Etymology of شمیران (Shemiran)

According to the article's etymology section, the name comprises two parts:

**Word components:**
- "شمی" or "سمی" or "شم" means "high/elevated"
- "ران" means "place/location"
- Combined: "بلندجای" (high place)

**Alternative etymology by Ahmad Kasravi:**
Kasravi proposed that "سمی" or "شمی" means "cold," making شمیران signify "cold place" or "cold region."

**Related forms mentioned:**
The article notes variant spellings including شمیرام، شمیرم، شمیلان، سمیران, and references سمیرم as a separate location.

**Note on plural form:**
The article criticizes using "شمیرانات" as a plural, arguing شمیران is already a collective name for the region encompassing multiple towns and villages.
```


## [2026-09-05T21:03:23.429Z] TOOL CALL #56: Bash

```json
{
 "command": "pdftoppm -f 183 -l 183 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg183 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 183"
}
```


### [2026-09-05T21:03:25.333Z] TOOL RESULT

```
total 24876
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:03 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    2762 Sep  5 17:02 p189_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24596 Sep  5 17:02 p189_greek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20222 Sep  5 17:02 p189_khoris.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33994 Sep  5 17:02 p189_n12.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   88207 Sep  5 17:02 pg177.png
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53414 Sep  5 17:03 pg183.png
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


## [2026-09-05T21:03:28.116Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg183.png"
}
```


### [2026-09-05T21:03:28.469Z] TOOL RESULT

```

```


## [2026-09-05T21:03:28.466Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T21:03:54.866Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Zoroastrian_calendar",
 "prompt": "What does the month name Day (Dae, tenth month) mean and what Avestan word is it from? Quote the table row and any note on daθuš / Dadv \"creator\"."
}
```


## [2026-09-05T21:03:57.265Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg183.png data/verification/sources/refs/ocr/BOOK/183.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T21:04:00.589Z] TOOL RESULT

```
# Zoroastrian Month Name: Dae

Based on the article's month names table, the tenth month entry states:

> "10. Dae (_Daθušō \[Ahurahe Mazdå\]_)"

The month dedicated to Ahura Mazda uses a special naming convention. According to the text:

> "The month dedicated to Ahura Mazda is a special case – that month is named after Mazda's stock epithet, "Creator" (Avestan _Dadvah_, whence Zoroastrian Middle Persian _Dae_)"

So "Dae" derives from the Avestan word *Dadvah*, meaning "Creator." Rather than using Mazda's proper name, this month employs His characteristic epithet emphasizing His role as creator.
```


### [2026-09-05T21:04:00.643Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T21:04:08.960Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%85%D8%B3%D8%AA%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ey-\" \\\n \"https://www.etymonline.com/word/hibernate\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%B9%E0%A4%BF%E0%A4%AE%E0%A4%BE%E0%A4%B2%E0%A4%AF\" \\\n \"https://www.avesta.org/zcal_months.htm\" \\\n \"https://en.wikipedia.org/wiki/Zoroastrian_calendar\" \\\n \"https://fa.wikipedia.org/wiki/%D8%B4%D9%85%DB%8C%D8%B1%D8%A7%D9%86\" ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 183, root Ghei 1 (winter): zam/zemestan/zamharir, day, himalaya, hibernate' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T21:04:13.729Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/490ee2a1a2175442.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/828f0d6ec27b0a28.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/255659eeb6ddd5c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7cbc305bc4e50ba4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a64016f6d55ceaac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5d7e0a4720be75dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f677b84b75764446.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/099c37afda3bf55a.txt
```


## [2026-09-05T21:04:17.636Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-127.json'))\nprint({k:v for k,v in d.items() if k!='entries'})\ne=d['entries'][0]\nprint(json.dumps({k:(v if k!='nodes' else v[0]) for k,v in e.items()},ensure_ascii=False,indent=1)[:2500])\n\"",
 "description": "Inspect previous verification file"
}
```


### [2026-09-05T21:04:19.523Z] TOOL RESULT

```
{'pdf_page': 127, 'book_page': 97, 'verified_by': 'claude-opus-5', 'verified_on': '2026-09-05'}
{
 "entry": 0,
 "root": "Dhem",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
 "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
 "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
   "stance": "supports",
   "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
  },
  {
   "src": "CHEUNG",
   "where": "
```


## [2026-09-05T21:04:29.798Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT ===\" && grep -n -i \"hibernate\\|Himalaya\" SKT.txt | head -5 && echo \"=== FSD vol2/3 ===\" && grep -n -i \"Himalayan\\|hibernate\" FSD_vol2.txt FSD_vol3.txt WEB_vol1.txt HJB.txt 2>/dev/null | head -10",
 "description": "Skeat/FSD/Webster/Hobson-Jobson"
}
```


### [2026-09-05T21:04:29.871Z] TOOL RESULT

```
=== SKT ===
8656:—  L,    hibtmalts,    wintry.  —  1*   kiktri wintry;  allied  to  kums,  winter.    At Gk.  x*-<^»'.  snow.  SkL  ki-maJxCAl.  ( VGI Der.  hibernate.
=== FSD vol2/3 ===
HJB.txt:825:Hooker  (Sir)  Jos.  Dalton.  Himalayan Journals.  Notes  of  a  Naturalist,  ke. 2  vols.    Ed.  1855.
HJB.txt:5665:1848. — "Kajees,  Counsellors,  and  mitred Lamas  were  there,  to  the  number  of  twentv, all  planted  with  their  backs  to  the  wall, mute  and  motionless  as  statues." — Hooker' $ Himalayan  JoumaUf  ed.  1855,  L  286.
HJB.txt:6211:unu&ETTA,  s.  H.  chirdUa,  Mahr. hirditd,  A  Himalayan  herbaceous ^nt  of  the  order  Gmticmaceae  {Swertia UhiratOy  Ham.  ;  (Mulia  ChiratOy Griesbaich  ;  Getitiana  Chirayita,  Roxb. ; Agathetes  chiraytc^  Don.),  the  dried twigs  of  which,  infused,  aJTord  a  pure bitter  tonic  and  febrifuge.  Its  Skt. name  kirdtct-tdOo^  Hhe  bitter  plant  of the  Kirdtasy'  refers  its  discovery  to  that people,  an  extensively-diffused  forest tribe,  east  and  north-east  of  Bengal, the  KifipddoL  of  the  Periplus,  and  the people  of  the  Ki^Sia  of  Ptolemy. There  is  no  indication  of  its  having been  known  to  G.  de  Orta.
HJB.txt:8751:1879.— "The  Sub-Himalayan  Hills  .  .  . as  a  genera]  rule  .  .  .  consist  of  two  ranges, separated  by  a  broad  flat  valley,  for  which the  name  'ditn*  (Doon)  has  been  adopted. .  .  .  When  the  outer  of  these  ranges  is wanting,  as  is  the  case  below  Naini  Tal  and Dariiling,  the  whole  geopaphical  feature might  escape  notice,  the  inner  range  being confounded  with  the  spurs  of  the  moun- tains."—i/a»«aZ  of  the  Oeology  qf  IwHa^
HJB.txt:9239:1854.— (In  Cachar)  ''the  eagle-wood,  a tree  yielding  iiggiir  oil,  is  also  muoh  sought for  its  fragrant  wood,  which  is  carried  to Silhet,  where  it  is  broken  up  and  distilled." — HookeTf  Himalayan  JowndU,  ed.  1855, ii.  318.
HJB.txt:10440:^^  GOOBIJL.  s.  H.  gUraly  goral;  the Himalayan  chamois;  NemorhoedusGoral of  Jerdon.  [Cemas  Goral  of  Blanford (MamMncLlioy  516).]
HJB.txt:11979:1850.— "To  the  geologist  the  Jheelsand Sunderbunds  are  a  most  instructive  region, as  whatever  may  be  the  mean  elevation  of their  waters,  a  permanent  depression  of 10  to  15  feet  would  submerge  an  immense tntct." — Booker's  Himalayan  JonnuUs,  ed. 1865,11/265.
HJB.txt:12507:KHUDD,  KUDD,  s.  This  is  a term  chiefly  employed  in  the  Hima- laya, khadd,  meaning  a  precipitous hill-side,  also  a  deep  valley.  It  is  not in  the  dictionaries,  but  is  probably allied  to  the  Hind,  khdt,  'a  pit,'  Dakh. — Hind,  khaddd.  [Platts  gives  Hind. khad.  This  is  f  rom  Skt.  khanda,  *  a  gap, a  chasm,'  while  khdt  comes'  from  Skt. khdta,  *  an  excavation.']  The  word  is  in constant  Anglo-Indian  colloquial  use  at Simla  and  other  Himalayan  stations.
HJB.txt:13669:&c.  Hind,  mdkddr,  mafidsefy  mdhda- auldy  s.  The  name  is  applied  to  per- haps more  than  one  of  the  larger species  of  Ba/rbus  (N.O.  Oypnmdae), but  especially  to  B.  mostU  of  Buchanan, B.  Tor,  Day,  B.  megalepis,  McLelland, found  in  the  larger  Himalayan  rivers, and  also  in  the  greater  perennial  rivers of  Madras  and  Bombay.  It  grows  at its  largest,  to  about  the  size  of  the biggest  salmon,  and  more.  It  affords also  the  highest  sport  to  Indian anglers  ;  and  from  these  circumstances has  sometimes  been  called,  mislead- in^ly^,  the  'Indian  salmon.'  The origin  of  the  name  Mahseer^  and  its proper  roelling,  are  very  doubtful  It may  be  Skt.  mahd-Hras^  *  big-head,'  or maM-ialkay  4arge-scaled.'  The  latter is  most  probable,  for  the  scales  are  so large  that  Buchanan  mentions  that playing  cards  were  made  from  them at  Dacca.  Mr.  H.  S.  Thomas  suggests mahd-dsyoy  *  great  mouth.'  [The  word does  not  appear  in  the  ordinary  diets. ; on  the  whole,  perhaps  the  derivation from  mahd-Hrcu  is  most  probable.]
HJB.txt:13869:medicine  from  old  times  of  much repute  in  the  East,  especially  for  eye- diseases,  and  imported  from  Himalayan and  Trans- Himalayan  regions.  It  ia^ a  popular  native  drug  in  the  Punjab- bazars,  where  it  is  still  knowa  as mamira^  also  as  pUidrl,  It  seems probable  that  the  name  is  applied  ta bitter  roots  of  kindred  properties  but of  more  than  one  specific  origin. Hanbury  and  Fliicki^r  describe  it  as> the  rhizome  of  Coptis  Teeta^  Wallich^ tUa  being  the  name  of  the  dru^  in the  Mishmi  country  at  the  heaa  of the  Assam  Valley,  from  which  it  i»  * imported  into  Bengal.  But  Stewart states  explicitly  that  the  mumira  of the  Punjab  Ijazars  is  now  "known  to be"  mostly,  if  not  entirely,  derived from  Thalidr^im  foltosum  D.C.,  a  tall plant  which  is  conunon  throughout  the temperate  Himalaya  (50(X)  to  8(XK)  feet) and  on  the  Kasia  Hills,  and  is  ex- ported from  Kunlaun  unaer  the  name of  Momiri.  [See  J^ott,  Econ,  Diet.  vi. pt.  iv.  42  tteq.J  "The  Mamira  of  the old  Arab  writers  was  identified  with XcXid^nov  fiiya,  by  which,  however. Low  {Aram,  PJlanzennamen^  p.  220) says  they  understood  curcuma  lon^/^ W.R.S.
```


## [2026-09-05T21:04:43.319Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghei-\\|ĝhei\\|Winter, Schnee\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Walde-Pokorny Bd1 ghei"
}
```


### [2026-09-05T21:04:43.369Z] TOOL RESULT

```
33239:Schwierigkeit der Yermittlung mit ghei- „antreiben“ s. d.). 
33241:Ai. hesah n. „GeschoB“ (doch s. u. ghei- „antreiben“); 
33551:und dgl. (s. unter ghei- ^Winter"). S. unten S. 547! 
34218:ags. gasne „entbehrend“ (Zup. aaO.; s. auch u. ghei- „gahnen“). 
34225:(ware glmo-s ), arm. j> „RoG“ (doch s. ghei- „antreiben“) und aksl. mjccb 
34328:gkei- — ghei- : ghi- 
34348:ist es, aucb *ghaiso-s „Ger“ (s. d.) mit unserem ghei- zu vereinen, da 
34378:2. ghei- : ghi- „Winter, Schnee". (Uber den Wurzelansatz s. Specbt KZ. 53, 
34394:ghei- : ghi- 
34402:yagog aus | ghei- „antreiben“ -f- mar ,Wasser, Meer"); alb. dimen m.
```


## [2026-09-05T21:04:45.908Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 34378,34440p incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "WLD Bd1 ghei-2 entry"
}
```


### [2026-09-05T21:04:45.949Z] TOOL RESULT

```
2. ghei- : ghi- „Winter, Schnee". (Uber den Wurzelansatz s. Specbt KZ. 53, 
307 f. Bei dem friihoren *gliciem-, yhim -, Hirt Abl. 559, Yf. 

LEWb. 2 365, Wackernagel Ai. Gr. I 100, Brugmann KYG. 148, bleibt 
ai. huyana ,.Jahr‘, av. zayan a ,.winterlich“ unerklart: anders Brugmann 2 
II 1 , 1 35 . 

A. *yhe. i- men . hrtmn- (alter /•in-Stamm nach Pedersen KZ. 32. 
248, Sommer Festschr. f. Windisch 125?, Specht aaO. halt die r-Erweite- 
rung fur analogiscb nach *s a mero- ..sommerlich", vgl. unten II 492 f.). 

Ai. heman (locj „im Winter', himantd m. ,, Winter'; gr. yeiya „schlechte 
Jahreszeit, Winter. Wintersturm. Klilte", yetinov „Wintersturm, Winter- 



ghei- : ghi- 


547 


wetter, \Yinter“ (dazu stellt Sommer aaO. auch ydgagog .Zapfen" ala 
„Schlechtwetterspund". ?? Nicht wahrscheinlich deutet Prellwitz 2 504 yd- 
yagog aus | ghei- „antreiben“ -f- mar ,Wasser, Meer"); alb. dimen m. 
„Winter“ (G. Meyer BB. 8, 187, Alb. Wb. 67, Pedersen KZ. 36, 333). 

Lit. ziema, lett. z'lema, pr. sumo „Winter“, aksl. zima, russ. zimd, bulg. zima, 
skr. zima, slov. zima, cech. zima, poln. zima ds. (m < mn : Job. Schmidt 
KdS. 100, 119). 

Dazu *yheim(e)rinos und '*yheiminos „winterlich“. 

In gr. ysifisgivog, lat. hibernus (< % gheimrinos s. Solmsen KZ. 34, 18 mit 
Lit.), lit. ziemmis , aksl. zimvnz, russ. zimnij. skr. zhmu, cech . zimni (cech. 
zimnij „kalt“), poln. zimny „kalt, winterlich" (vgl. mit i in der Wurzelsilbe 
arm. jmern „Winter“ Hiibschmann Arm. Gr. I 471). 

Zu *gheimen auch av. zaen- m. „Winter“, np. tlai. 

(Nach Bartholomae Ir. Wb. 1666 zacna < *ghehnno), av. zayana „winter- 
lich“ und mit Vrddhierung ai. lidyanct ,.jahrlich", liCiyana m. n. „Jahr“. 
(Nach Specht aaO. Reimbildung zu av. hdmana „sommerlich a , eine Les- 
art, fur die sich Job. Schmidt Pluralbildung 211 Af. ausgesprochen hatte; 
Bartholomae Ir. Wb. 1809 bietet hq»iina.) 

B. t/hiom, ( jhiijrm , Gen. ghiemos , gliimos , auch ghiomos. 

Av. zyd „Winter“ (acc. zyqm, gen. sdmo), arm. jinn „Schnee“ (< *ghigon), 
gen. jean (< ghii°n s. Meillet Esquisse 24), gr. ytcbv, yiovog „Schnee“, lat. 
hiems ., Winter" (s. Specht aaO.); mir. gemred „Winter“ (s. Pedersen K. Gr. 
I 66 ; yam „Winter‘ ist nach sain „Sommer“ umgeformt, vgl. Thurneysen 
b. Fick II 4 104, Brugmann 2 II 1, 135), acymr. gaem, ncymr. gauaf, acorn. 
goyf bret. goahv , gall. Eigenname Giamillus , auch ir. gamttin „jahriges 
Kalb" (Pedersen KGr. II 56); aisl. goi f., goimanadr „der Monat von Mitte 
Februar bis Mitte Marz", isl. goa, u. f., norw. gjo f„ schw. gojemcinad (go- < 
gib- nach Bugge Ark. f. nord. Fil. 4, 123 ff.). 

Fraglich die Anreihung von an. gam all „alt“, gemlingr ,,jahriges Scliaf". 
ags. gamol „alt“, gamelian „altern“, as. gigamulod „bejahrt‘ , ahd. nur in 
Eigennamen wie Gamalbold, Gamaiberht, Gamalberga usw. bei Forstemann 
I 2 592 als „bejahrt" vgl. lat. annosns (Fick III 4 126, Falk-Torp 298, Hell- 
quist SvEO. 179).
```


## [2026-09-05T21:11:26.109Z] TOOL CALL #65: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build183.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n  \"entry\": 0,\n  \"root\": \"Ghei 1, Ghiem, Ghi, Khai, Khei\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ǵʰey- : *ǵʰi- 'winter, snow', with the stems *ǵʰey-men- / *ǵʰeim-, *ǵʰyṓm ~ gen. *ǵʰim-és and *ǵʰi-mo-\",\n  \"note\": \"Pokorny IEW 425 heads the entry '2. ghei- : ghi- \\\"Winter, Schnee\\\"' and divides it exactly as Nourai's root-name string does: A. ghei-men-, *gheimn- (whence Nourai's 'Ghiem'), B. ghiōm, ghii̯ōm, C. ghimo- (Nourai's 'Ghi'). Walde-Pokorny I 546 f. and Watkins/AHD ('ghei-2. Theoretical base of *ghyem-, *ghiem-, winter') give the same root with the same gloss, so language label ('Indo-European') and gloss ('winter') are correct. The two extra shapes 'Khai, Khei' are not separate roots: they are Nourai's transliteration of the Greek reflexes kheimōn / khiōn (Gk. kh- is the regular outcome of PIE *ǵʰ), so they belong inside this same root box and are not an error, only a redundancy. Wiktionary flags the bare root *ǵʰey- 'winter' as uncertain and prefers to start from the derived stems *ǵʰéy-mn̥ / *ǵʰéy-ōm, which is a presentational, not a substantive, difference.\",\n  \"note_fa\": \"ریشهٔ این نمودار همان ریشهٔ هندواروپاییِ آغازینِ *ǵʰey- / *ǵʰi- «زمستان، برف» است. پوکورنی در صفحهٔ ۴۲۵ فرهنگ خود سرواژهٔ «۲. ghei- : ghi- ‹Winter, Schnee›» را آورده و آن را به سه شاخه بخش کرده است: ghei-men- (همان «Ghiem» نورایی)، ghiōm/ghii̯ōm و ghimo- (همان «Ghi»)؛ والده-پوکورنی (جلد یکم، ص ۵۴۶ به بعد) و واتکینز/AHD نیز همین ریشه و همین معنا را می‌آورند. پس برچسب زبان و معنای جعبهٔ ریشه درست است. دو صورت «Khai, Khei» ریشه‌های جداگانه نیستند، بلکه صورت‌های یونانیِ همین ریشه‌اند (kheimōn، khiōn)، چون ǵʰ هندواروپایی در یونانی به kh بدل می‌شود؛ آوردنشان زائد است ولی نادرست نیست. ویکی‌واژه وجود ریشهٔ برهنهٔ *ǵʰey- را نامطمئن می‌داند و ترجیح می‌دهد از ستاک‌های *ǵʰéy-mn̥ و *ǵʰéy-ōm آغاز کند که تفاوتی صوری است نه ماهوی. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n  \"sources\": [\n    W + \"Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ey-\",\n    W + \"%E0%A4%B9%E0%A4%BF%E0%A4%AE%E0%A4%BE%E0%A4%B2%E0%A4%AF\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:425\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt, form-feed leaf 82 (= IEW p.425; POK_02 leaf = p-344, printed '425' visible in the leaf): '2. ghei- : ghi- ,Winter, Schnee'; nach Specht Dekl. 14, 330 f. alter -men-Stamm, mit schon idg. Wandel von mn zu m. A. ghei-men-, *gheimn- ... B. ghiōm, ghii̯ōm, Gen. ghiemos, ghimos ... C. ghimo- (aus ghi-mn-o-?)' (the C section runs onto p.426). Exactly the root box as drawn, including Nourai's three sub-shapes.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 546-547 (WLD_Bd1_1930_dli_70244_djvu.txt line 34378)\", \"stance\": \"supports\",\n     \"note\": \"'2. ghei- : ghi- „Winter, Schnee\\\". ... A. *ǵhei-men-, ǵheimn- ... Dazu *ǵheim(e)rinos und *ǵheiminos „winterlich\\\". In gr. χειμερινός, lat. hibernus (< *gheimrinos) ... B. ǵhiōm, ǵhii̯ōm, Gen. ǵhiemos, ǵhimos' — the source Pokorny 425 abridges.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ghei-2 (AHD_watkins1985.txt line 510)\", \"stance\": \"supports\",\n     \"note\": \"'ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suffixed variant form *gheim-ri-no- in Latin hibernus ... 3. Suffixed zero-grade form *ghim-ar-ya ... Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, cols. under *ǵheim-, ǵheimn- and *ǵhii̯ōm (IEC.txt lines 5963, 6058)\", \"stance\": \"supports\",\n     \"note\": \"'ǵheim-, ǵheimn- (ghim-) (resolutions of a prototype *ǵhii̯om-) WP I, 546 Skt. cf. himáh ... Gk. kheima ... Lat. hiems' and '*ǵhii̯ōm- \\\"winter; snow\\\" ... Av. zyā̊, acc. zyām \\\"winter\\\"; zayano \\\"wintry\\\"'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 14.74 'Winter', pp. 1013-1014\", \"stance\": \"supports\",\n     \"note\": \"'1. IE *gheim-, *ǵhyem-, etc., prob. with m-suffixes fr. *ghei-. Walde-P. 1.546 ff. ... in all the main branches of the family except Gmc. belong to an obvious group, pointing unmistakably to an IE word for \\\"winter\\\".'\"}\n  ],\n  \"nodes\": []\n}\n\nN = root[\"nodes\"]\n\nN.append({\n  \"id\": 1,\n  \"lang\": \"Avestan / Old Persian\",\n  \"words\": \"zem : cold; zyâ 1, zyâo, zimô : winter\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The 'winter' forms are genuine Avestan and are quoted straight from Nourai's own reference: Pokorny 425 section B gives 'Av. zyā f. \\\"Winter\\\" (Akk. zyąm, Gen. zimō)', i.e. Bartholomae AiW s.v. zyā- f. 'Winter', nom. sg. zyā̊ — which is exactly Nourai's 'zyâo' — acc. zyąm, gen. zimō, continuing PIE *ǵʰyṓm ~ gen. *ǵʰim-és; the '1' after zyâ is Nourai's homonym number, distinguishing it from Av. zyā- 'to harm' (AiW s.v. zyā-, OP diyā-). Two things are wrong with the box. (a) 'zem : cold' is not an Avestan word: Avestan zam-/zǝm- means 'earth' (Kent, Old Persian §143: 'zam- \\\"earth\\\" in u-zma-'), the cold-stem showing up only in the gen. zim-ō and in zǝmaka- m. 'winter storm' (Pok. 426). Nourai's 'zem \\\"cold\\\"' is in fact the New Persian headword of Horn, Grundriss no. 666 (p.147), 'zem \\\"Kälte\\\", zemistan \\\"Winter\\\"', lifted up into the Avestan box. (b) No Old Persian word for winter is attested, and it could not have looked like this: in Old Persian PIE *ǵʰ regularly yields d-, not z- (Av. zasta- : OP dasta- 'hand'; Av. zan- : OP dan-), so z-forms of this root are Avestan/Median, not Old Persian — which is precisely why Persian has both zamestān (with NW z-) and day (with SW d-, node 4). Hence the node is accepted as Avestan but its language label and its first gloss are loose.\",\n  \"derivation_fa\": \"صورت‌های «زمستانی» این جعبه اوستایی راستین‌اند و درست از همان مأخذی گرفته شده‌اند که نورایی یاد کرده است: پوکورنی در ص ۴۲۵، بخش ب، می‌آورد «اوستایی zyā مؤنث ‹زمستان› (رایی zyąm، اضافی zimō)»؛ در فرهنگ بارتولومه نیز سرواژهٔ zyā- با صورت فاعلیِ zyā̊ آمده که همان «zyâo»ی نورایی است. اینها دنبالهٔ *ǵʰyṓm هندواروپایی‌اند و شمارهٔ ۱ کنار zyâ برای جدا کردن آن از zyā- «آسیب رساندن» است. اما دو نکته نادرست است: نخست آنکه «zem» به معنی «سرد» واژه‌ای اوستایی نیست؛ در اوستا zam-/zǝm- «زمین» است (کنت، پارسی باستان) و ستاک سرما تنها در zimō و zǝmaka- «توفان زمستانی» دیده می‌شود. «zem: سرما» در حقیقت سرواژهٔ فارسیِ هرن (Grundriss، شمارهٔ ۶۶۶، ص ۱۴۷) است که نورایی آن را به جعبهٔ اوستایی برده است. دوم آنکه هیچ واژهٔ پارسی باستانی برای زمستان بر جای نمانده و چنین صورتی هم ممکن نبود، زیرا ǵʰ هندواروپایی در پارسی باستان به d بدل می‌شود نه z (اوستایی zasta- در برابر پارسی باستان dasta- «دست»)؛ پس صورت‌های z-دار شمال‌غربی/اوستایی‌اند. به همین سبب فارسی هم «زمستان» (با ز) دارد و هم «دی» (با د). ادعای نورایی با احتیاط پذیرفتنی است ولی برچسب زبان و معنای نخست دقیق نیست.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ey-\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:425\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 82 (IEW p.425), section B: 'Av. zyā f. ,Winter' (Akk. zyąm, Gen. zimō)'. The 'zem : cold' half of the node is not on that page; p.426 has only 'av. zǝmaka- m. ,Wintersturm' (vgl. den Gen. von zyā: zimō unter B.)'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. zyā- (BRT.txt line 28266) and s.v. zayan- : zaēn- (line 27723, col. 1666)\", \"stance\": \"supports\",\n     \"note\": \"The zyā- entry cites the paradigm forms 'zyą̇ (NS.) ... zyąm (AS.) ... zimō (GS.)' and closes 'ai. himá-; np. zam; arm. jiun ... Pū.: zam, zamastān' — i.e. Bartholomae himself carries the chain Av. zyā-/zim- → Pahlavi zam, zamastān.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss no. 666, p. 147\", \"stance\": \"partial\",\n     \"note\": \"'zem \\\"Kälte\\\", zemistan \\\"Winter\\\". aw. zyā̊ \\\"Winter\\\", Gen. zimō; phlv. zam \\\"Winter\\\" (vd. 2 (20)), zam(i)stan; ai. himá- \\\"Winter\\\"' — Horn's 'zem \\\"Kälte\\\"' is a NEW PERSIAN headword, which is where Nourai's Avestan 'zem : cold' comes from.\"},\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §143 and s.v. uzma- (KNT.txt lines 1774, 5226)\", \"stance\": \"contradicts\",\n     \"note\": \"'zam- \\\"earth\\\" in u-zma- etc.'; 'uzma- ... from ud- \\\"up\\\" + zma- to zam- \\\"earth\\\"'. Old Persian zam- means EARTH, and Kent §11 notes that even this z- is a Median trait ('zam- (which would have Med. z) appears only in the form zm-'). No OP winter word exists.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. *ǵhii̯ōn- (IEC.txt line 6058)\", \"stance\": \"supports\",\n     \"note\": \"'ǵhii̯ōn- \\\"winter; snow\\\" ... Av. zyā̊, acc. zyąm \\\"winter, frost\\\"; zayano \\\"wintry\\\"'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2,\n  \"lang\": \"Persian\",\n  \"words\": \"zam «زم» : cold; zemestan «زمستان» : winter; zamharîr «زمهریر» : a very cold place (extra: سمیرم ، سمیران ، شمیران)\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"زم zam 'cold' and زمستان zamestān 'winter' are the regular Iranian continuants of this root: Middle Persian zam 'winter' and zamestān 'winter' (MacKenzie, CPD 97-98: 'zam [zm | P zmg] winter', 'zamestān [zmstʾn | (M dmystʾn), N ~] winter'), from Old Iranian *zima- < PIE *ǵʰi-mo-, with the place/time suffix -stān (< *stāna-) as in tābestān, bahārestān. One qualification: the z- shows that these are not the inherited Southwest-Persian forms — in Persian's own ancestor PIE *ǵʰ gives d- (see node 4) — so Middle/New Persian zamestān was taken over from a Northwestern (Median/Parthian) dialect, as Wiktionary states explicitly ('inherited from Middle Persian zamestān, borrowed from a Northwestern Iranian language'), and the Manichaean MP spelling dmystʾn recorded by MacKenzie preserves a trace of the native d-form. زمهریر zamharīr is a different case: Borhan-e Qāṭeʿ p.1032 gives it as Nourai does ('معروف است و جایی است بسیار سرد نزدیک به انتهای کرهٔ هوا؛ و این لفظ مرکب است از زم و هریر') and analyses it as zam 'cold' + harīr; but the word is a Qurʾānic Arabic word (Q 76:13 'lā yarawna fīhā šamsan wa-lā zamharīrā', 'neither sun nor bitter cold'), quadriliteral z-m-h-r, so Persian زمهریر is at best a Persian compound arabicized and re-borrowed (the round trip Nourai's FVF reference asserts) — the direct arrow Persian < Persian zam is only half the story. The place-names سمیرم / سمیران / شمیران belong to the same family under the 'cold place' etymology (šam-/sam- = zam 'cold' + -rān/-ram 'place'), which is Kasravi's and is the one Persian encyclopaedias repeat; but fa.wikipedia records a rival reading šam 'high' → 'high place', so the toponym arrow is not settled.\",\n  \"derivation_fa\": \"«زم» و «زمستان» دنبالهٔ منظم همین ریشه در ایرانی‌اند: فارسی میانه zam «زمستان» و zamestān (مکنزی، فرهنگ کوچک پهلوی، ص ۹۷–۹۸)، از ایرانی باستان *zima- و آن از *ǵʰi-mo- هندواروپایی، با پسوند جای/زمان ‑ستان (از *stāna-) مانند تابستان و بهارستان. یک نکتهٔ مهم: «ز» آغازین نشان می‌دهد که این صورت‌ها میراث خودِ فارسی (جنوب‌غربی) نیستند، زیرا ǵʰ هندواروپایی در نیای فارسی به «د» بدل می‌شود (بنگرید به گرهٔ ۴)؛ پس zamestān وام‌واژه‌ای از گویشی شمال‌غربی (مادی/پارتی) است، چنانکه ویکی‌واژه صریحاً می‌گوید، و املای مانوی dmystʾn که مکنزی ثبت کرده یادگار صورت بومیِ د-دار است. «زمهریر» داستان دیگری دارد: برهان قاطع (ص ۱۰۳۲) همان‌گونه که نورایی می‌گوید آن را «مرکب از زم و هریر» می‌داند، اما این واژه در عربی قرآنی آمده است (انسان ۱۳: «لا یرون فیها شمساً و لا زمهریراً») و ساختِ چهارحرفی z-m-h-r دارد؛ بنابراین «زمهریر» فارسیِ امروز دست‌کم معرّبی است که دوباره به فارسی بازگشته، نه واژه‌ای که یکسره از «زم» فارسی ساخته شده باشد. نام‌های سمیرم و سمیران و شمیران بنا بر ریشه‌شناسی کسروی («شمی/سمی» = سرد + «ران» = جای) به همین خانواده می‌پیوندند و همین توضیح در دانشنامه‌های فارسی تکرار شده است، اما ویکی‌پدیای فارسی خوانش رقیبِ «شم = بلند، بلندجای» را نیز می‌آورد؛ پس این پیوند قطعی نیست. در مجموع: با احتیاط پذیرفتنی است.\",\n  \"sources\": [\n    W + \"%D8%B2%D9%85%D8%B3%D8%AA%D8%A7%D9%86\",\n    \"https://fa.wikipedia.org/wiki/%D8%B4%D9%85%DB%8C%D8%B1%D8%A7%D9%86\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1028\", \"status\": \"supports\",\n     \"note\": \"BQT_v2_pages.txt form-feed leaf 490 (printed page fixed by the running head '-۱۰۳۱-' on leaf 493, so printed = leaf + 538): 'بیان چهاردهم — در زای نقطه‌دار با میم ... زم: به فتح اول و سکون ثانی ... و به معنی سرما باشد که در مقابل گرماست و لهذا ایام سرما را زمستان گویند؛ و باد سخت و تند را نیز گفته‌اند؛ و نام رودخانه‌ای است ...'. Exactly Nourai's 'zam : cold' and the link to zemestān.\"},\n    {\"ref\": \"BQT:1032\", \"status\": \"supports\",\n     \"note\": \"BQT_v2_pages.txt leaf 494: 'زمهریر — ... معروف است و جایی است بسیار سرد نزدیک به انتهای کرهٔ هوا، و این لفظ مرکب است از زم و هریر به معنی سرمای سخت کننده، چه زم به معنی سرما و هریر به معنی کننده باشد'. Supports both the gloss ('a very cold place') and the zam-compound analysis.\"},\n    {\"ref\": \"FVF:320\", \"status\": \"not_checked\",\n     \"note\": \"Emam Shushtari, Farhang-e vāžehā-ye fārsi dar zabān-e ʿarabi: no accessible copy (noorlib page-viewer needs a browser session; the ketabnak/parsianjoman PDFs are behind a login). refs_online.json records local_file: null for FVF.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp. 97-98 (PHD.txt line 677; PHD_mackenzie.txt lines 5743, 5750; English index 'winter zam, zamestān')\", \"stance\": \"supports\",\n     \"note\": \"'zam [zm | P zmg] winter.'  'zamestān [zmstʾn | (M dmystʾn), N ~] winter.' — Middle Persian antecedents of both Persian words, and the Manichaean spelling dmystʾn.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss no. 666, p. 147\", \"stance\": \"supports\",\n     \"note\": \"'zem \\\"Kälte\\\", zemistan \\\"Winter\\\". aw. zyā̊ \\\"Winter\\\", Gen. zimō; phlv. zam \\\"Winter\\\", zam(i)stan ... oss. d. zumäg, i. zimäg \\\"Winter\\\"; afγ. zimai' — Horn draws the same Avestan → Pahlavi → Persian chain, and adds that kurd./afγ./bel. zamistān are themselves loans from Persian.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā-ye hend-o-orupāyi, printed p. 325 (ARY_latin_index_pages.txt, [pdf page 324]) s.v. زمستان\", \"stance\": \"supports\",\n     \"note\": \"The cognate box of the entry زمستان reads '(AVESTAN) ZYA, ZYAM, ZAEM | (PAHLAVI) ZAM, ZAMESTAN | (OSSETIC) ZIMAG, ZUMAG | (KURDISH) ZIVISTAN | (SANSKRIT) HEMAN, HEMANTAS | (LATIN) HIEMS ...', with REFERENCES 'POKORNY 425 / MACKENZIE (WINTER) 140 / BUCK 1013-1016'. An independent modern Persian source with the same chart — and, notably, with the same 'ZAEM' misreading discussed at node 3.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qāṭeʿ p.1028 and p.1032 (leaves 490, 494)\", \"stance\": \"supports\", \"note\": \"See ref_check above; Mo'in's edition carries no Latin-script etymological footnote at either place, only the Persian definitions.\"},\n    {\"src\": \"MON\", \"where\": \"vajehyab/abadis Moʿin (not reachable in this session) — used fa.wikipedia شمیران instead\", \"stance\": \"partial\",\n     \"note\": \"fa.wikipedia 'شمیران', وجه تسمیه: two competing readings, «شمی/سمی به معنای سرد» (Kasravi: شمیران = جای سرد) versus «شم = بلند» (بلندجای); variants شمیرام، شمیرم، شمیلان، سمیران and the separate town سمیرم are listed. Nourai's 'areas with cold winters' is one of the two current explanations, not the only one.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3,\n  \"lang\": \"Avestan\",\n  \"words\": \"zaem, zyam : winter\",\n  \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"The second form is right: zyąm is the accusative singular of Av. zyā- 'winter' (Bartholomae AiW s.v. zyā-; Pokorny 425 'Akk. zyąm'). The first form is not an Avestan word. What all three of Nourai's own references print is zaēn-, with n: Pokorny 425 'Zu *ghei- allein: av. zayan-, zaēn- m. \\\"Winter\\\", npers. dai'; Buck, Selected Synonyms 1014 'Here also (fr. *ghei-) Av. zaēn- (NPers. dai) \\\"winter\\\" and zayana- \\\"wintry\\\"'; Klein s.v. hibernate (1966 ed. p.727-728, leaf 392 of KLN_1966.txt) 'Avestic zaya(n)-, zyā (gen. zimō), \\\"winter\\\"'; Walde-Pokorny I 547 'Zu *ǵheimen auch av. zaēn- m. \\\"Winter\\\", np. dai (Nach Bartholomae Ir. Wb. 1666 zaēna < *ǵheimno)'; and Bartholomae himself, AiW col. 1666, heads the entry 'j. zayan- : zaēn- m. \\\"Winter\\\"' and closes it 'Ableit. (zayana-). — np. dai.' So the correct headword is zaēn- (stem zayan-), from *ǵʰey-mn-, and 'zaem' is a mis-set/mis-read final n. The printed page 183 of the dictionary itself reads 'zaem, zyam : winter', so the JSON extraction is faithful and the error is the book's; the same 'ZAEM' recurs in Aryanpur's Persian IE-roots dictionary (p.325), which suggests a shared secondary source rather than a one-off slip. The derivation drawn (root → Avestan winter-word) is otherwise correct.\",\n  \"derivation_fa\": \"صورت دوم درست است: zyąm همان رایی مفردِ zyā- «زمستان» در اوستاست (بارتولومه، ذیل zyā-؛ پوکورنی ص ۴۲۵: «رایی zyąm»). اما صورت نخست واژه‌ای اوستایی نیست. هر سه مأخذی که خود نورایی نام برده «zaēn-» با «ن» چاپ کرده‌اند: پوکورنی ص ۴۲۵ «اوستایی zayan-، zaēn- مذکر ‹زمستان›، فارسی نو dai»؛ باک ص ۱۰۱۴ «Av. zaēn- (NPers. dai)»؛ کلاین ذیل hibernate (چاپ ۱۹۶۶، ص ۷۲۷–۷۲۸) «Avestic zaya(n)-, zyā (gen. zimō)»؛ والده-پوکورنی جلد یکم ص ۵۴۷ «av. zaēn- m. ‹Winter›, np. dai»؛ و خودِ بارتولومه در ستون ۱۶۶۶ سرواژهٔ «zayan- : zaēn- مذکر ‹زمستان›» را آورده و در پایان می‌نویسد «np. dai». پس صورت درست zaēn- (ستاک zayan-) از *ǵʰey-mn- است و «zaem» خطای خواندن «ن» به «م» است. تصویر صفحهٔ ۱۸۳ چاپی نشان می‌دهد که خودِ کتاب «zaem, zyam» چاپ کرده؛ پس خطای خوانشِ اسکن نیست، خطای چاپیِ کتاب است — و جالب آنکه همین «ZAEM» در فرهنگ ریشه‌های هندواروپایی آریان‌پور (ص ۳۲۵) هم تکرار شده، که نشان می‌دهد هر دو از یک مأخذ دستِ‌دوم گرفته‌اند. جز این، خودِ پیوند (ریشه ← واژهٔ اوستاییِ زمستان) درست است.\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"zaem, zyam : winter\",\n  \"correct_form\": \"zaēn- (stem zayan-) 'winter'; acc. zyąm (of zyā-)\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ey-\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:425\", \"status\": \"partial\",\n     \"note\": \"POK_02.txt leaf 82: 'Zu *ghei- allein: av. zayan-, zaēn- m. ,Winter', npers. dai; av. zayana- ,winterlich''. Pokorny has the node and the arrow but spells the word zaēn-, not zaem.\"},\n    {\"ref\": \"KLN:728\", \"status\": \"partial\",\n     \"note\": \"KLN_1966.txt leaf 392 = printed pp. 726-729 (page numerals 726, 727, 728, 729 occur on that leaf), s.v. hibernate; the fuller 1971 text (KLN_1971.txt line 113469) reads: 'fr. I.-E. base *ghei-, *ghi-, \\\"winter; snow\\\", whence also OI. himan ... Hitt. gimmanza ... Avestic zaya(n)-, zyā (gen. zimō), \\\"winter\\\" ...'. Klein has zaya(n)-/zyā, again no zaem.\"},\n    {\"ref\": \"SYN:1014\", \"status\": \"partial\",\n     \"note\": \"Buck p.1014: 'Av. zyam-. Here also (fr. *ghei-) Av. zaēn- (NPers. dai) \\\"winter\\\" and zayana- \\\"wintry\\\", Skt. hayana- \\\"year\\\".' Supports zyam and the winter sense, but spells the other form zaēn-.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1666 (BRT.txt line 27723)\", \"stance\": \"partial\",\n     \"note\": \"'j. zayan- : zaēn- m. \\\"Winter\\\": ... FrW.9.2; ... V.16.12. Ableit. (zayana-). — np. dai. — Vgl. zyani-.' The headword is zaēn-, the derivation to np. dai is Bartholomae's own; the form 'zaem' is nowhere in AiW.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 547 (WLD_Bd1 djvu line ~34400)\", \"stance\": \"partial\",\n     \"note\": \"'Zu *ǵheimen auch av. zaēn- m. „Winter\\\", np. dai. (Nach Bartholomae Ir. Wb. 1666 zaēna < *ǵheimno), av. zayana „winterlich\\\"' — same form, same n.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur p. 325 s.v. زمستان (ARY_latin_index_pages.txt, [pdf page 324])\", \"stance\": \"partial\",\n     \"note\": \"'ZYA, ZYAM, ZAEM :(AVESTAN)' — Aryanpur prints the identical erroneous ZAEM beside the correct ZYA/ZYAM, so Nourai is not alone in it.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4,\n  \"lang\": \"Persian\",\n  \"words\": \"day «دی ۱» : (first month of) winter\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Two different words are being conflated. (i) For a Persian word day 'winter' the derivation Nourai draws is the classical Indo-Europeanist one and his references really do say it: Bartholomae AiW 1666 ends the entry zayan- : zaēn- 'Winter' with 'np. dai'; Walde-Pokorny I 547 'av. zaēn- m. \\\"Winter\\\", np. dai'; Pokorny 425 'av. zayan-, zaēn- m. \\\"Winter\\\", npers. dai'; Buck 1014 'Av. zaēn- (NPers. dai) \\\"winter\\\"'. Phonetically it works only through Southwest Iranian, where PIE palatal *ǵʰ > d- (Av. zasta- : OP dasta- 'hand', Av. zan- : OP dan- 'know'), making day the inherited Persian doublet of the Northwestern loan zamestān (node 2). (ii) But what Nourai actually glosses is the MONTH — 'دی ۱ : (first month of) winter' — and for the month name Iranian scholarship is unanimous the other way: the tenth month is Young Avestan daθušō (māh-) '(month) of the Creator', from daδuuah-/daθuš-, the perfect active participle of dā- 'to place, create' and a stock epithet of Ahura Mazdā, whence Middle Persian Day; the same name marks days 8, 15 and 23 of every month (Day-pad-Ādur, Day-pad-Mihr, Day-pad-Dēn), which only makes sense for a divine name, not for 'winter'. Encyclopaedia Iranica s.v. DAY, avesta.org's calendar table ('10. Day — \\\"The Creator\\\"') and Wikipedia's Zoroastrian calendar ('named after Mazda's stock epithet, \\\"Creator\\\" (Avestan Dadvah, whence Zoroastrian Middle Persian Dae)') all state this, and so does the very footnote of Moʿin that Nourai's NOTE cites. English Wiktionary likewise gives the month دی only from Middle Persian ddwʾ (Day 'Creator'), and reserves a third homonym دی 'yesterday' for PIE *dʰǵʰyés (Skt. hyás) via MP dēg. So the arrow as drawn — Avestan winter-word → the month دی — is rejected by modern scholarship; Nourai's own NOTE flags the alternative, and the alternative is the accepted one.\",\n  \"derivation_fa\": \"در اینجا دو واژه با هم آمیخته شده‌اند. نخست، اگر مقصود «دی» به معنی «زمستان/سرما» باشد، همان است که هندواروپایی‌شناسان کلاسیک گفته‌اند و مآخذ خودِ نورایی هم آن را می‌آورند: بارتولومه (ستون ۱۶۶۶) پس از سرواژهٔ zayan- : zaēn- «زمستان» می‌نویسد «np. dai»؛ والده-پوکورنی (ج ۱ ص ۵۴۷)، پوکورنی (ص ۴۲۵) و باک (ص ۱۰۱۴) نیز همین را تکرار می‌کنند. از نظر آوایی تنها از راه ایرانی جنوب‌غربی درست درمی‌آید، چون ǵʰ کامی هندواروپایی در آن شاخه به «د» بدل می‌شود (اوستایی zasta- در برابر پارسی باستان dasta- «دست»)؛ پس «دی» دوگانهٔ بومیِ «زمستان»ِ وام‌گرفته از شمال غرب است. اما دوم، آنچه نورایی در عمل معنا کرده «ماهِ دی» است، و دربارهٔ نامِ ماه، ایران‌شناسی امروز یکدل نظر دیگری دارد: ماه دهم در اوستای متأخر daθušō (māh-) «ماهِ آفریدگار» است، از daδuuah-/daθuš-، صفت فاعلی کاملِ ریشهٔ dā- «آفریدن» و لقب همیشگی اهورامزدا، که در فارسی میانه Day شده؛ همین نام بر روزهای هشتم و پانزدهم و بیست‌وسوم هر ماه هم نهاده شده (دی‌به‌آذر، دی‌به‌مهر، دی‌به‌دین) و این تنها برای نام خداوند معنا دارد نه برای «زمستان». دانشنامهٔ ایرانیکا (مدخل DAY)، جدول گاه‌شمار زردشتی در avesta.org و ویکی‌پدیا همین را می‌گویند و — مهم‌تر — حاشیهٔ خودِ معین بر برهان قاطع که نورایی در یادداشتش به آن ارجاع داده نیز همین را می‌گوید. پس پژوهش امروزی این پیوند را رد می‌کند و «دی» را از daθuš «آفریدگار» می‌گیرد. (واژهٔ سومِ «دی» به معنی «دیروز» نیز جداست و از *dʰǵʰyés هندواروپایی، سنسکریت hyás، فارسی میانه dēg می‌آید.)\",\n  \"sources\": [\n    W + \"%D8%AF%DB%8C\",\n    \"https://www.avesta.org/zcal_months.htm\",\n    \"https://en.wikipedia.org/wiki/Zoroastrian_calendar\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:425\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 82: 'Zu *ghei- allein: av. zayan-, zaēn- m. ,Winter', npers. dai'. Pokorny does assert the arrow — for a Persian word dai 'winter', without saying it is the month name.\"},\n    {\"ref\": \"SYN:1014\", \"status\": \"supports\",\n     \"note\": \"Buck p.1014: 'Here also (fr. *ghei-) Av. zaēn- (NPers. dai) \\\"winter\\\" and zayana- \\\"wintry\\\", Skt. hayana- \\\"year\\\".' Same claim, same silence about the calendar.\"},\n    {\"ref\": \"BQT:907\", \"status\": \"partial\",\n     \"note\": \"Cited inside Nourai's own NOTE. The footnote is in BQT_v2_pages.txt leaf 367, i.e. printed p.905 rather than 907 (printed = leaf + 538, fixed by the running head '-۱۰۳۱-' on leaf 493), and it continues on p.909 ('بقیه در صفحهٔ ۹۰۹'); its content is exactly what Nourai reports: 'در اوستا daθuš با ... به معنی آفریننده، دادار و آفریدگار است و غالباً صفت اهورمزداست و آن از مصدر dā به معنی دادن و آفریدن است. در خود اوستا صفت دئوش (= دی) برای تعیین دهمین ماه استعمال شده. در میان سی روز ماه روزهای هشتم و پانزدهم و بیست‌وسوم به دی (= دئوش) موسوم است بنا بر تسمیه به نام خدا.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. 1666 s.v. zayan- : zaēn- (BRT.txt line 27723)\", \"stance\": \"supports\",\n     \"note\": \"'Ableit. (zayana-). — np. dai.' Bartholomae is the origin of the Pokorny/Buck/Walde-Pokorny statement.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 547\", \"stance\": \"supports\",\n     \"note\": \"'Zu *ǵheimen auch av. zaēn- m. „Winter\\\", np. dai.' — the same nineteenth-century equation, repeated in 1930.\"},\n    {\"src\": \"BQT\", \"where\": \"Moʿin's footnote to Borhan-e Qāṭeʿ, printed p.905 (leaf 367)\", \"stance\": \"contradicts\",\n     \"note\": \"See ref_check BQT:907: Moʿin derives the month and day name دی from Av. daθuš 'creator', epithet of Ohrmazd, not from the winter root.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. dēg / day (PHD_mackenzie.txt) and the calendar entries\", \"stance\": \"partial\",\n     \"note\": \"CPD has no Middle Persian *day 'winter' — its winter words are zam and zamestān (English index: 'winter zam, zamestān'), which is a silence against the winter reading of the month name.\"},\n    {\"src\": \"Wikipedia/avesta.org\", \"where\": \"Zoroastrian calendar month table; avesta.org zcal_months\", \"stance\": \"contradicts\",\n     \"note\": \"'10. Dae (Daθušō [Ahurahe Mazdå])' ... 'that month is named after Mazda's stock epithet, \\\"Creator\\\" (Avestan Dadvah, whence Zoroastrian Middle Persian Dae)'; avesta.org lists '10. Day — \\\"The Creator\\\"'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5,\n  \"lang\": \"Sanskrit\",\n  \"words\": \"hima : snow; hima-alaya : home of snow\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Sanskrit himá- m. 'cold, frost, snow', himā́ f. 'winter' continues PIE *ǵʰi-mo-, the C-section of the very Pokorny entry Nourai cites: IEW 426 'C. ghimo- (aus ghi-mn-o-?): Ai. himá-ḥ m. \\\"Kälte, Frost, Schnee\\\", himā f. \\\"Winter\\\", av. zǝmaka- m. \\\"Wintersturm\\\"', beside the -ant- derivative hemantá- 'winter' and the locative héman 'in winter'. Himālaya is the regular tatpuruṣa hima- + ālaya- 'abode, dwelling' (from ā-lī- 'to settle on'), with the -a + ā- > -ā- sandhi that Nourai's hyphenated spelling 'hima-alaya' spells out; the compound is post-Vedic, current in the epics and the Purāṇas as both the mountain range and its personification (father of Pārvatī and Gaṅgā). Nourai's rendering 'home of snow' is the standard gloss ('abode of snow').\",\n  \"derivation_fa\": \"سنسکریت himá- «سرما، یخبندان، برف» و himā́ «زمستان» دنبالهٔ *ǵʰi-mo- هندواروپایی‌اند و دقیقاً در همان مدخلی که نورایی ارجاع داده آمده‌اند: پوکورنی ص ۴۲۶، بخش ج: «ghimo- (از ghi-mn-o-؟): سنسکریت himá-ḥ مذکر ‹سرما، یخبندان، برف›، himā مؤنث ‹زمستان›، اوستایی zǝmaka- ‹توفان زمستانی›»؛ در کنار آن hemantá- «زمستان» و héman «در زمستان». «هیمالیا» ترکیب تتپوروشهٔ منظمِ hima- + ālaya- «جایگاه، خانه» (از ā-lī- «نشستن، آرام گرفتن») است و همان ادغام a + ā > ā در کار است که املای خط‌فاصله‌دار نورایی («hima-alaya») آن را باز می‌نماید. این ترکیب پس از دورهٔ ودایی رواج یافته و در حماسه‌ها و پورانه‌ها هم نام رشته‌کوه است و هم نامِ ایزدینهٔ آن (پدر پارواتی و گنگا). برگردان نورایی («خانهٔ برف») همان معنای پذیرفتهٔ «جایگاه برف» است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"%E0%A4%B9%E0%A4%BF%E0%A4%AE%E0%A4%BE%E0%A4%B2%E0%A4%AF\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:425\", \"status\": \"supports\",\n     \"note\": \"The Sanskrit material sits at the end of the entry that begins on p.425: POK_02.txt leaf 83 (= IEW p.426) 'C. ghimo- (aus ghi-mn-o-?): Ai. himá-ḥ m. ,Kälte, Frost, Schnee', himā f. ,Winter''; p.425 itself already has 'Ai. himan (Lok.) ,im Winter', hemantá-ḥ m. ,Winter''.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. ǵheim-, ǵheimn- (IEC.txt line 5963)\", \"stance\": \"supports\",\n     \"note\": \"'Skt. cf. himáh, himā́, hemantáh; himám \\\"snow, ice\\\"' listed under the same prototype as Gk. kheima and Lat. hiems.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 14.74, p.1013\", \"stance\": \"supports\",\n     \"note\": \"'Ved. hima-, class. Skt. usually hemanta- (also once RV; Macdonell-Keith 1.110, 2.504, 507)' under IE *gheim-, *ǵhyem-.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ghei-2\", \"stance\": \"silent\",\n     \"note\": \"Watkins lists only the Latin and Greek derivatives (HIEMAL, HIBERNATE, CHIMERA) because no English word reaches the root through Sanskrit; the silence is not a disagreement.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6,\n  \"lang\": \"Persian\",\n  \"words\": \"hîmâlâyâ «هیمالیا» : Himalayan mountains\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The ultimate source is right — Persian هیمالیا is Sanskrit himālaya 'abode of snow' — but the arrow Sanskrit → Persian is not a line of descent or an old Indo-Iranian borrowing. Persian has no medieval attestation of the name (classical Persian geographers of India use جبال / کوه‌های هند, and Bīrūnī writes the range's local names); هیمالیا enters Persian only in the modern period, in the nineteenth-twentieth centuries, from the European geographic name Himalaya (English/French), which itself was taken from Sanskrit through Anglo-Indian usage. The Persian spelling with final ا (rather than an expected هیمالیه) reproduces the Latin-letter European form, which is the diagnostic of a modern, book-learned borrowing. So: correct etymon, but the route is Sanskrit → English/French → Persian, not Sanskrit → Persian.\",\n  \"derivation_fa\": \"خاستگاه نهایی درست است — «هیمالیا» همان himālaya سنسکریت «جایگاه برف» است — اما پیکانِ «سنسکریت ← فارسی» نه تداومِ زبانی است و نه وام‌گیریِ کهنِ هندوایرانی. در فارسی کهن و میانه هیچ گواهی از این نام نداریم؛ جغرافی‌نویسان فارسیِ سده‌های میانه کوه‌های شمال هند را با نام‌های دیگر می‌آورند. «هیمالیا» تنها در دورهٔ نو (سدهٔ سیزدهم–چهاردهم هجری) از راه نام جغرافیاییِ اروپاییِ Himalaya (انگلیسی/فرانسه) به فارسی رسیده، و آن نام خود از سنسکریت و از راه کاربردِ انگلیسیِ هند گرفته شده است. املای فارسی با الف پایانی (نه «هیمالیه») درست همان صورت لاتین‌نویسِ اروپایی را بازمی‌تاباند و نشانهٔ آشکارِ وام‌واژه‌ای کتابی و نو است. پس ریشه درست است ولی مسیر «سنسکریت ← انگلیسی/فرانسه ← فارسی» است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [W + \"%E0%A4%B9%E0%A4%BF%E0%A4%AE%E0%A4%BE%E0%A4%B2%E0%A4%AF\"],\n  \"ref_check\": [\n    {\"ref\": \"MON6:2320\", \"status\": \"not_checked\",\n     \"note\": \"Moʿin, Farhang-e fārsi vol. 6 (اعلام) p.2320. Volumes 5-6 of the six-volume edition are not online: vajehyab's Moʿin has no proper-name entries, abadis returns Dehkhoda and فرهنگ اسم‌ها instead, and no scan of the six-volume Amir Kabir edition exists on archive.org / Google Books / HathiTrust / noorlib (refs_online.json records this explicitly). Only the two-volume Adena condensation is on disk, and it has no هیمالیا headword.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt (2-vol. Adena condensation) lines 2367, 23013, 81271\", \"stance\": \"silent\",\n     \"note\": \"هیمالیا occurs only inside other entries ('قلل هیمالیا زندگی می‌کند', 'کوه‌های هیمالیا و هندوکش') and has no headword of its own in the abridgement, so no etymology can be read from it.\"},\n    {\"src\": \"Abadis (Dehkhoda/Moʿin portal)\", \"where\": \"abadis.ir/fatofa/هیمالیا\", \"stance\": \"supports\",\n     \"note\": \"Gives the Sanskrit etymology 'برفستان' = hima 'snow, cold' + alaya 'place, abode', but reproduces no Dehkhoda/Moʿin entry text, so it confirms the etymon and not the route.\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson (HJB.txt): no headword 'Himalaya'\", \"stance\": \"silent\",\n     \"note\": \"The Anglo-Indian glossary has no entry for the range; it only quotes Hooker's Himalayan Journals (1855) in other articles — i.e. the name was a plain geographic term in nineteenth-century English, the stage from which Persian took it.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7,\n  \"lang\": \"English\",\n  \"words\": \"Himalayan\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English Himalayan is simply the adjective in -an to Himalaya, taken into English from Sanskrit himālaya through Anglo-Indian usage in the early nineteenth century (earlier English spellings Himmaleh, Himmalayan reflect the Hindi/Urdu pronunciation of the Sanskrit name). By the mid-century it is fully naturalized — Sir Joseph Dalton Hooker's Himalayan Journals (1854, cited throughout Hobson-Jobson) is the standard early example. The arrow Sanskrit → English is therefore right; the only unstated link is the Anglo-Indian intermediary.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی Himalayan صرفاً صفتِ ‑an ساخته‌شده از Himalaya است، و Himalaya خود در آغاز سدهٔ نوزدهم از راه کاربردِ انگلیسیِ هند از himālaya سنسکریت به انگلیسی رفته است (املاهای کهن‌ترِ Himmaleh و Himmalayan تلفظ هندی/اردوی این نام را بازمی‌تابانند). تا میانهٔ همان سده کاملاً جا افتاده بود؛ نمونهٔ کلاسیکش سفرنامهٔ Himalayan Journals نوشتهٔ جوزف دالتون هوکر (۱۸۵۴) است که در هابسن-جابسن بارها نقل شده. پس پیکانِ «سنسکریت ← انگلیسی» درست است و تنها حلقهٔ ناگفته، میانجیِ انگلیسیِ هند است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"%E0%A4%B9%E0%A4%BF%E0%A4%AE%E0%A4%BE%E0%A4%B2%E0%A4%AF\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node (refs=None in the source JSON); nothing to check.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson (HJB.txt lines 825, 5665, 8751, 9239, 11979, 12507)\", \"stance\": \"partial\",\n     \"note\": \"No headword, but the glossary's bibliography lists 'Hooker (Sir) Jos. Dalton. Himalayan Journals ... Ed. 1855' and quotes it repeatedly, and s.v. KHUDD notes 'a term chiefly employed in the Himalaya ... in constant Anglo-Indian colloquial use at Simla and other Himalayan stations' — the Anglo-Indian channel by which the name and its adjective entered English.\"},\n    {\"src\": \"FSD / WEB\", \"where\": \"FSD_vol1-4.txt, WEB_vol1.txt\", \"stance\": \"silent\",\n     \"note\": \"grep -i 'Himalayan' returns nothing in the Funk & Wagnalls volumes or in Webster vol. 1 (A-?) held here, as expected for a proper-name derivative.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8,\n  \"lang\": \"Latin\",\n  \"words\": \"hibernus : pertaining to winter\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Latin hībernus 'of winter, wintry' goes back to *ǵʰeim-ri-no-, the -rino- adjective of the *ǵʰey-men-/*ǵʰeim- stem, exactly the formation Nourai's AHD reference gives: Watkins, 'ghei-2 ... 2. Suffixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE'. Pokorny 425 has the same: 'Dazu *gheim(e)rinos und *gheiminos \\\"winterlich\\\". In gr. kheimerinós, lat. hibernus (< *gheimrinos)', with Greek kheimerinós as the exact match; the -mr- cluster gives Latin -br- (as in membrum : *mems-ro-). Beside it stands the noun hiems, -is 'winter' < *ǵʰyems (Pokorny 425 section B), and Ernout-Meillet s.v. hiems note that hibernus 'a remplacé hiems dans toutes les langues romanes'. So the root → Latin arrow is correct as drawn.\",\n  \"derivation_fa\": \"لاتین hībernus «زمستانی» از *ǵʰeim-ri-no- می‌آید، یعنی صفتِ ‑rino- ساخته‌شده بر ستاک *ǵʰey-men-/*ǵʰeim-؛ همان ساختی که مأخذ خودِ نورایی (AHD/واتکینز) می‌دهد: «ghei-2 ... صورت پسوندیِ *gheim-ri-no- در لاتین hibernus». پوکورنی (ص ۴۲۵) نیز همین را دارد: «*gheim(e)rinos و *gheiminos ‹زمستانی›؛ در یونانی kheimerinós، لاتین hibernus (< *gheimrinos)»، و یونانی kheimerinós برابرِ دقیقِ آن است. خوشهٔ ‑mr- در لاتین به ‑br- بدل می‌شود (مانند membrum از *mems-ro-). در کنار آن اسمِ hiems «زمستان» از *ǵʰyems ایستاده است، و ارنو-مه‌یه ذیل hiems یادآور می‌شوند که hibernus در همهٔ زبان‌های رومی جای hiems را گرفت. پس این پیکان درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/hibernate\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt line 510: 'ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suffixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. ... [Pok. 2. ghei- 425.]' — Nourai's bare 'AHD' citation is the modern standard for this claim.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 425 (POK_02.txt leaf 82)\", \"stance\": \"supports\",\n     \"note\": \"'Dazu *gheim(e)rinos und *gheiminos ,winterlich'. In gr. χειμερινός, lat. hibernus (< *gheimrinos), lit. žiemìnis, aksl. zimьnъ ...' and, under B, 'lat. hiems, -is ,Winter'.'\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. hiems (LAT.txt lines 27927-27950)\", \"stance\": \"supports\",\n     \"note\": \"'hibernus: d'hiver ... qui a remplacé hiems dans toutes les langues romanes, M.L.4136 ... Les formes de hiems, -himus et hibernus sont toutes anciennes. Elles appartiennent à une racine indo-européenne désignant les frimas, l'hiver, la neige ... Le même mot existe en iranien, où l'on a av. zyā̊, gén. zimō, au sens de \\\"hiver\\\". - Pour la racine, cf. av. zayana- \\\"d'hiver\\\".'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 547\", \"stance\": \"supports\",\n     \"note\": \"'In gr. χειμερινός, lat. hibernus (< *gheimrinos s. Solmsen KZ. 34, 18 mit Lit.)'.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. hibernal (SKT.txt line 8656)\", \"stance\": \"supports\",\n     \"note\": \"'L. hibernalis, wintry. — L. hibernus, wintry; allied to hiems, winter. Cf. Gk. χιών, snow, Skt. hima-. Der. hibernate.'\"}\n  ]\n})\n\nN.append({\n  \"id\": 9,\n  \"lang\": \"English\",\n  \"words\": \"hibernate\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English hibernate is a learned Latinism of the first years of the nineteenth century (1802), formed as a back-formation from hibernation, which is itself the older borrowing: hibernation is attested from the 1660s of plants and insects, from Latin hibernātiōnem (nom. hibernātiō), noun of action to hibernāre 'to pass the winter, occupy winter quarters', a denominative of hibernus (node 8). Klein s.v. hibernate gives the same chain — 'L. hibernat(um), pp. stem of hibernare \\\"to pass the winter, to winter\\\", fr. hibernus \\\"pertaining to winter, wintry\\\", which is rel. to hiems ... fr. I.-E. base *ghei-, *ghi-, \\\"winter; snow\\\"' — and Skeat closes his hibernal entry with 'Der. hibernate'. The arrow Latin hibernus → English hibernate is therefore right, with hibernāre/hibernātiō as the unnamed intermediate step.\",\n  \"derivation_fa\": \"فعل انگلیسی hibernate وام‌واژه‌ای عالمانه از لاتین و از نخستین سال‌های سدهٔ نوزدهم است (۱۸۰۲) که با اشتقاق معکوس از hibernation ساخته شده؛ و hibernation خود کهن‌تر است و از دههٔ ۱۶۶۰ دربارهٔ گیاهان و حشرات به کار می‌رفته، از لاتین hibernātiōnem، اسمِ مصدرِ hibernāre «زمستان را گذراندن، در قرارگاه زمستانی ماندن» که خود از صفتِ hibernus (گرهٔ ۸) ساخته شده است. کلاین ذیل hibernate همین زنجیره را می‌دهد: «از hibernat(um)، ستاک اسم مفعولِ hibernare، از hibernus، هم‌ریشه با hiems، از ریشهٔ هندواروپاییِ *ghei-, *ghi- ‹زمستان؛ برف›»؛ اسکیت نیز مدخل hibernal را با «مشتق: hibernate» می‌بندد. پس پیکانِ «لاتین hibernus ← انگلیسی hibernate» درست است و تنها حلقهٔ ناگفته‌اش hibernāre/hibernātiō است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/hibernate\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node (refs=None in the source JSON); the parent node's AHD citation covers the Latin step and is checked there.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. hibernate (1966 ed. p.727-728 = KLN_1966.txt leaf 392; text quoted from KLN_1971.txt line 113469)\", \"stance\": \"supports\",\n     \"note\": \"'hibernate, intr. v., to pass the winter. — L. hibernat(um), pp. stem of hibernare, \\\"to pass the winter, to winter\\\", fr. hibernus, \\\"pertaining to winter, wintry\\\", which is rel. to hiems (gen. hiemis), \\\"winter\\\", fr. I.-E. base *ghei-, *ghi-, \\\"winter; snow\\\" ... Avestic zaya(n)-, zyā (gen. zimō), \\\"winter\\\" ...'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. hibernal (SKT.txt line 8656)\", \"stance\": \"supports\",\n     \"note\": \"'L. hibernus, wintry; allied to hiems, winter. ... Der. hibernate.'\"},\n    {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/hibernate\", \"stance\": \"supports\",\n     \"note\": \"'hibernate (1802), \\\"pass the winter in torpidity and seclusion\\\", probably a back-formation from hibernation (1660s), \\\"action of passing the winter\\\", from Latin hibernationem, from hibernare \\\"to winter, pass the winter, occupy winter quarters\\\"; PIE root *gheim- \\\"winter\\\".'\"}\n  ]\n})\n\nout = {\n  \"pdf_page\": 183,\n  \"book_page\": 153,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [root]\n}\np = \"/home/sfmqrb/git/rishe/data/verification/page-183.json\"\nwith open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", p)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build183.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-183.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 183",
 "description": "Write and validate page-183.json"
}
```


### [2026-09-05T21:11:29.897Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-183.json
JSON OK
nodes verified: 9/9
node verdicts: {'plausible': 3, 'transcription_suspect': 1, 'disputed': 1, 'confirmed': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 7, 'not_checked': 4, 'partial': 4}
books consulted: {'supports': 18, 'partial': 7, 'contradicts': 3, 'silent': 4} | by book: {'BRT': 3, 'WLD': 3, 'HRN': 2, 'IEC': 2, 'PHD': 2, 'ARY': 2, 'BQT': 2, 'MON': 2, 'HJB': 2, 'SKT': 2, 'KNT': 1, 'Wikipedia/avesta.org': 1, 'SYN': 1, 'AHD': 1, 'Abadis (Dehkhoda/Moʿin portal)': 1, 'FSD / WEB': 1, 'POK': 1, 'LAT': 1, 'KLN': 1, 'Etymonline': 1}
```


## [2026-09-05T21:11:48.690Z] AGENT

Page 183 (book p. 153) verified — one entry, root "Ghei 1, Ghiem, Ghi, Khai, Khei" (PIE *ǵʰey- "winter"), 9 nodes. `verify_check.py 183`: 9/9 nodes, 0 PROBLEM lines.

Verdicts: root confirmed; nodes confirmed 4, plausible 3, disputed 1, transcription_suspect 1.
Ref checks: supports 7, partial 4, not_checked 4 (FVF:320 and MON6:2320 have no accessible copy; two nodes carry refs=None).

Flagged items:
- **disputed — #4 Persian دی "day"**: Pokorny 425, Buck 1014, Bartholomae AiW 1666 and Walde-Pokorny I 547 do all print "np. dai" from Av. zaēn- "winter", so Nourai's refs back him. But he glosses the *month*, and Iranian scholarship (Iranica s.v. DAY, avesta.org/Wikipedia calendar tables, and Moʿin's own Borhan footnote that Nourai's NOTE cites) derives the tenth month from YAv. daθuš-/daδuuah- "Creator" (epithet of Ahura Mazdā, also days 8/15/23). Modern view goes against the arrow as drawn.
- **transcription_suspect — #3 Avestan "zaem"**: the real form is zaēn- (stem zayan-); "zyam" is fine (acc. of zyā-). All four reference works print zaēn-. `error_in: "book"` — the printed page 183 really reads "zaem, zyam", and Aryanpur p. 325 repeats the same "ZAEM", so it is Nourai's (inherited) misreading, not an extraction slip. Page image copied to `data/verification/sources/refs/ocr/BOOK/183.png`.

Notable "plausible" caveats: #1 "zem : cold" is not Avestan (Av. zam- = "earth"; the form is Horn's *New Persian* headword no. 666 moved into the Avestan box) and no Old Persian winter word exists (OP would give d-, not z-); #2 زمستان is a Northwestern-Iranian loan into Persian (Wiktionary; cf. Manichaean MP dmystʾn) and زمهریر is a Qurʾānic Arabic word (Q 76:13) at best re-borrowed; #6 هیمالیا is a modern loan via European Himalaya, not Sanskrit → Persian directly.

**No extraction errors found** — the JSON matches the printed page throughout.

Files: `/home/sfmqrb/git/rishe/data/verification/page-183.json` (new); 8 web sources archived via `tools/fetch_source.py` into `data/verification/sources/web/`.
