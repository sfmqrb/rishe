# Verification process log — verify-page-363


## [2026-09-07T19:29:09.627Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 363 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-363.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-363.json. Write /home/sfmqrb/git/rishe/data/verification/page-363.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 363` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:11.652Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T19:29:12.413Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:12.429Z] TOOL RESULT

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


## [2026-09-07T19:29:12.936Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-363.txt"
}
```


### [2026-09-07T19:29:12.968Z] TOOL RESULT

```
1	=== PDF page 363 (book page 333) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Neu : to cry  (refs POK:767)
4	#1 (parent #0) [Avestan / Old Persian] refs=FFD:77 | nard : to cry
5	  #2 (parent #1) [Persian] refs=FFD:77 | nâlîdan «نالیدن» : to moan | extra: ناله ، نال | NOTE: HUB:103 derives "nâlîdan" from Sanskrit "nard: to cry".
6	#3 (parent #0) [Sanskrit] refs=POK:767 | nav, navatě, nâuti : to cry
7	  #4 (parent #3) [Persian] refs=HRN:149,236; BQT:2209; MON:4859 | novîdan «نُویدن» : to cry ; zenŭdan «زنودن» : to cry, moan | extra: زنوییدن ، زنویه
8	#5 (parent #0) [Latin] refs=POK; AHD | nŭntium : message
9	  #6 (parent #5) [English] refs=None | announce, pronounce
10	--- entry 1 ---
11	ROOT Neudh -> redirect to Sneudh
12	--- entry 2 ---
13	ROOT [Indo-European] Newn : nine  (refs POK:318)
14	#1 (parent #0) [Avestan] refs=POK:318 | nava 1, nauma : nine ; navaiti : ninety ; nava-dasa : nineteen ☞Dekm
15	  #2 (parent #1) [Pahlavi] refs=BQT:2210 | naum
16	    #3 (parent #2) [Persian] refs=BQT:2195 | noh «نُه» : nine | extra: نود ، نوزده
17	#4 (parent #0) [Old Persian] refs=BQT:2210 | navama : ninth
18	#5 (parent #0) [Germanic] refs=AHD | niwum : nine
19	  #6 (parent #5) [English] refs=None | nine, ninety, nineteen
20	#7 (parent #0) [Latin] refs=AHD | novem : nine, ninth month ; nôna : ninth hour after sunrise (noon)
21	  #8 (parent #7) [English] refs=None | November, noon
22	
```


## [2026-09-07T19:29:16.606Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-363.json",
 "description": "Read source JSON for page 363"
}
```


### [2026-09-07T19:29:16.651Z] TOOL RESULT

```
{
  "pdf_page": 363,
  "book_page": 333,
  "entries": [
    {
      "root": {
        "name": "Neu",
        "lang": "Indo-European",
        "refs": "POK:767",
        "gloss": "to cry"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "FFD:77",
          "words": [
            {"translit": "nard", "gloss": "to cry", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FFD:77",
          "words": [
            {"translit": "nâlîdan", "gloss": "to moan", "script": "نالیدن"}
          ],
          "script_extra": "ناله ، نال",
          "note": "HUB:103 derives \"nâlîdan\" from Sanskrit \"nard: to cry\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:767",
          "words": [
            {"translit": "nav, navatě, nâuti", "gloss": "to cry", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "HRN:149,236; BQT:2209; MON:4859",
          "words": [
            {"translit": "novîdan", "gloss": "to cry", "script": "نُویدن"},
            {"translit": "zenŭdan", "gloss": "to cry, moan", "script": "زنودن"}
          ],
          "script_extra": "زنوییدن ، زنویه",
          "note": null,
          "quote": {"text": "زدرد دل آن شب بدان سان نُوید - که از ناله اش ، هیچکس نغنوید", "poet": "Labîbî"}
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK; AHD",
          "words": [
            {"translit": "nŭntium", "gloss": "message", "script": null}
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
            {"translit": "announce, pronounce", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Neudh", "redirect": "Sneudh"},
      "nodes": []
    },
    {
      "root": {
        "name": "Newn",
        "lang": "Indo-European",
        "refs": "POK:318",
        "gloss": "nine"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:318",
          "words": [
            {"translit": "nava 1, nauma", "gloss": "nine", "script": null},
            {"translit": "navaiti", "gloss": "ninety", "script": null},
            {"translit": "nava-dasa", "gloss": "nineteen", "script": null, "see": ["Dekm"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:2210",
          "words": [
            {"translit": "naum", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:2195",
          "words": [
            {"translit": "noh", "gloss": "nine", "script": "نُه"}
          ],
          "script_extra": "نود ، نوزده",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "BQT:2210",
          "words": [
            {"translit": "navama", "gloss": "ninth", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "niwum", "gloss": "nine", "script": null}
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
            {"translit": "nine, ninety, nineteen", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "novem", "gloss": "nine, ninth month", "script": null},
            {"translit": "nôna", "gloss": "ninth hour after sunrise (noon)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "November, noon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T19:29:17.918Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','FFD','HUB','HRN','BQT','MON','AHD','WLD','IEC','SYN','BRT','KNT','PHD','NYB','KLN','ARY','SKT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:500])\n\""
}
```


### [2026-09-07T19:29:19.174Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verific
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf onli
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); op
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qat
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 6
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/S
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan m
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = pri
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.t
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qa
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/S
```


## [2026-09-07T19:29:25.445Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,200p' SOURCE_MATRIX.md; ls refs/ | head -80"
}
```


### [2026-09-07T19:29:25.505Z] TOOL RESULT

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
```


## [2026-09-07T19:29:25.915Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py; echo ---; sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-07T19:29:25.969Z] TOOL RESULT

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
---
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


## [2026-09-07T19:29:54.073Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-317.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:4000])\n\""
}
```


### [2026-09-07T19:29:55.328Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Mad",
 "verdict": "confirmed",
 "modern_form": "PIE *mad- (laryngealist *meh₂d-) 'wet, dripping; fat, well-fed', with the derived sense 'food, fattening' — Pokorny 694-695",
 "note": "The root is genuine and standard. Pokorny 694-695 has 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating', and Watkins/AHD (1985 ed., p. 38) has 'mad-. Moist, wet; also refers to various qualities of food' — Nourai's gloss 'wet, also food' is essentially Watkins' wording, and the language label 'Indo-European' is right. Walde-Pokorny II 230-232 is the same article. What is remarkable is that Pokorny's article contains almost the whole of Nourai's chart in the same order: 'ai. madati, madate … mada- m. Rauschtrank = av. maδa-; ai. madgu- ein bestimmter Wasservogel, ein Fisch = np. māγ ein Wasservogel; ai. matsya- m., av. masya Fisch (der nasse; Ableitung von einem -es-St. *mades-); mastu- n. saurer Rahm (*mad-stu-) … arm. macun sauer, geronnene Milch … iran. Worte für Dickmilch, so npers. mast, masīdan … lat. madeō, mattus trunken (*madi-to-s) … ahd. mast Futter, got. mats Speise, ags. mete, mnd. mat(e) Kamerad'. Two modern caveats: (a) Cheung (2007) and LIV split the family into *mad¹ 'to become intoxicated' (PIE *med-) and a separate Indo-Iranian *mad 'to curdle', for which no PIE root is set up; (b) the 'fish' member is no longer taken as certain (see node #1).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *mad- (در نگارش امروزی *meh₂d-) به معنی «خیس، تر، چکه‌کننده؛ فربه و پرورده» و از همین‌جا «خوراک»، ریشه‌ای شناخته و پذیرفته است: پوکورنی (ص ۶۹۴–۶۹۵) آن را با معنی «تر؛ چرب، فربه، مست‌کننده» می‌آورد و واتکینز در پیوست فرهنگ American Heritage نیز «mad-. نمناک، تر؛ همچنین دربارهٔ کیفیت‌های خوراک» دارد؛ پس برچسب زبانی و معنای «wet, also food» در نمودار نورایی درست است. نکتهٔ چشمگیر آنکه تقریباً همهٔ شاخه‌های نمودار — سنسکریت madati و mada-، اوستایی maδa-، سنسکریت madgu- برابر «ماغ» فارسی، سنسکریت mastu- و ارمنی macun برابر «ماست» و «ماسیدن»، لاتینی mattus و واژه‌های ژرمنی mast/mats/mete/mate — همه در همان مقالهٔ پوکورنی و به همان ترتیب آمده‌اند، یعنی نورایی مستقیماً از پوکورنی و واتکینز برداشته است. دو نکتهٔ احتیاطی: نخست آنکه چونگ (۲۰۰۷) و فرهنگ LIV دو ریشهٔ *mad «مست شدن» و *mad «بستن، دلمه شدن» را از هم جدا می‌کنند و برای دومی ریشهٔ هندواروپایی نمی‌سازند؛ دوم آنکه پیوند واژهٔ «ماهی» با این ریشه امروز قطعی دانسته نمی‌شود (بنگرید به گرهٔ ۱).",
 "sources": [
  "https://en.wiktionary.org/wiki/mattus",
  "https://en.wiktionary.org/wiki/meat"
 ],
 "ref_check": [
  {
   "ref": "POK:694",
   "status": "supports",
   "note": "POK_full.txt line 57036 ff. (= POK_02.txt line 5645 ff., German original): 'Root/lemma: mad-  Meaning: wet; glossy, fat, well-fed, intoxicating … References: WP. II 231 f., WH. II 6 f.  Page(s): 694-695'. The page number Nourai cites is exactly right, and the article's material list is the source of his whole chart."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. II 230-232 s.v. 'mad-'",
   "stance": "supports",
   "note": "incoming/WLD/WLD_Bd2_pages.txt line 15104: 'weitere iran. Worte für Dickmilch u. dgl., so np. mast \"saure Milch\", masī[dan]' — the article Pokorny cites as WP. II 231 f., same members."
  },
  {
   "src": "AHD",
   "where": "Watkins 1985 p. 38 (AHD_watkins1985.txt line 708) s.v. mad-",
   "stance": "supports",
   "note": "'mad-. Moist, wet; also refers to various qualities of food. 1. Sanskrit madati, \"it gladdens, it bubbles,\" hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA. 2. Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate … MATE. 3. Suffixed form *mad-sto- … Old English mest, fodder: MAST. [Pok. mad- 694.]'"
  },
  {
   "src": "IEC",
   "where": "Mann, leaves 553-556: 'mad- (1) feed; food', 'mad- (3) get wet; be wet', 'madtós (maditós, mastos)'",
   "stance": "partial",
   "note": "IEC.txt lines 10227, 10237, 10239: Mann splits the family into three lemmas — 'mad- (1) \"feed
```


## [2026-09-07T19:29:55.446Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['POK_full.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print(f, len(t))\nEOF\ngrep -n \"neu-\" /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt | head -40"
}
```


### [2026-09-07T19:29:56.701Z] TOOL RESULT

```
POK_full.txt 3967710
2852:Material: present *{a)i-neu-mr. Old Indie inoti, fnvati, Imper. inuhf, participle -inita- 
5717:m-) is an old present the neu-, nu- class, wherefore the new Sg. ann. (under the influence 
26415:l\1aterial: Old Indie asnoti, Avestan asnaoiti{ *nR-neu-) " if something is obtained, achieved 
28197:This root form *re-n- (maybe grown from a present *re-neu-mi, *re-nu-d) one also seeks 
29306:from * eneu-, Gothic />7^ 'without'; 
32930:Material: Only in den extensions ghnegh- : ghnegh-, ghnac^h)-, ghne'h, ghneu-. 
32986:^/-extensions ghneu-, ghneud!^-, ghneus-: 
35407:Root / lemma: genu-1, gneu- {*ghenu-) 
35417:Root / lemma: genu-1, gneu- : "knee, joint' > Root / lemma: gen-1, gene-, gne-, gno- : "to 
35476:gneu-{*ghenu-) : knee, joint'. 
35521:1, gneu-{*ghenu-) : knee, joint'. 
45359:^/■basis kneu-3iX\6 extensions: 
45379:kneu-g-, -k-: 
45408:kneu-p-: Latvian khupV zusammengekrijmmt liegen ', Lithuanian kniupoti 6s.; 
45412:kneu-f-:0\d Icelandic hnodan. " ball, tangle, knot '. 
45622:IV. :/-basis kenu-, kneu-\ 
51427:Material: 1. Old Indie srnSti {*RJ-neu-) ' hears ', srudh/" hear' (= *kAu9i), participle sruta-{= 
58394:Root / lemma: meih-5 mi-neu- 
61815:Root / lemma: /7a5- nasalized {*neu-s) 
61825:Root/ lemma: nas-: nose' derived from Root/ lemma: neu-ks-, neu-s-\ "to sniff, smell' 
62820:Root / lemma: neu-6^- {*he- neu-dy-) 
62835:Root / lemma: neu-d- {*he- neu-d-) 
62860:See also: to consecutive {neu-6'^-) 
62863:Root / lemma: neu-ks-, neu-s- {*he- neu-ks-) 
62869:Root/ lemma: nas-: nose' : Root/ lemma: neu-ks- neu-s-: "to sniff, smell' derived from 
62889:References: WP. II 325, Holthausen KZ. 69, 166 f.; probably to 2. sneu-, see there. 
62910:Root / lemma: neu-1{*he- neu-f) 
62914:Material: Old Indie navate, nauti^ sounds, rejoices, praises ', Old Irish nuall{*neu-slo-) n. 
62924:Root / lemma: neu-2{*he- neu-2) 
62933:order', numen " beckoning gesture, volition, divine will| divinity; god ' ( *neu-men, or as *neu-smen 
62938:with formant. -r(o)-'cuss. (etc.) ponuryj {*neu-ro-) " lowered (of the head), low-spirited (of 
63020:together, to web, spin I formants: -p-\ snep-, -u- : sneu-, sneu-, -r- (s)ner-, also -tr-\ netr- 
68564:Root / lemma: pneu- 
72320:Material: Old Indie a-si-n-va-, asinvan^ insatiable ' (places ein Praes. *s9-neu-mi, *s9-nu-6 
72546:had-'s\c\\ wegsetzen, dodge ', asnaoiti{ *d-zd-neu-tl) "geht heran' (see 886 asna-); gr. 
77391:through hybridization with pneu- (above S. 838 f.): *ksneu-s- ( *kneus-, *sneus-) in npers. 
78850:4. Beside sna-\\es snau- audi sneu-\ 
78854:entlassen' (present Indo Germanic *snau-tiox lengthened gradees *sneu-ti)\ gr. vaw, 
78867:5. from *sneu-i'co'(r\: v£U) (Fut. vsuaopai) "schwimme', lak. voa nnvn. s-vvuGsv ekexuvto 
78868:Hes. Latin nutrio, -Tre 'suckle, nourish ', derivative from a *sneu-trTierc\. 'milk flow lassend';
```


## [2026-09-07T19:30:01.306Z] TOOL CALL #9: Bash

```json
{
 "command": "sed -n '62900,62950p' /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
}
```


### [2026-09-07T19:30:01.369Z] TOOL RESULT

```
amazed, impressed ', luscidsus, luscTtiosus^ purblind! dim-sighted '; Lithuanian n/uksot/^ grow 

dark', niukiu, niukti^ roar, sound vaguely ', apsi-niaukti' get cloudy ', Latvian apijaukties 

ds. 

References: WP. II 324 f., WH. I 838 f. 

Page(s): 768 

Root / lemma: neu-1{*he- neu-f) 

Meaning: to call, to praise 

Material: Old Indie navate, nauti^ sounds, rejoices, praises ', Old Irish nuall{*neu-slo-) n. 

"scream, din, fuss, noise, proclamation '; perhaps Latin nuntium^ message! announcement; 

news; notice of divorce/annulment of betrothal ' ( *nouention). 

References: WP. II 323, WH. II 188 f. 

Page(s): 767 

Root / lemma: neu-2{*he- neu-2) 
Meaning: to make a push; to nod 



Material: Old Indie navate, nauti' turns, moves ', navayatT turns, sweeps ', as o^present 
probably nudati^ shoves, pushes '; gr. vsuu) " nod, beckon ' (*v£uau)), vsupa " beckoning 
gesture ', vEuara^u) " nod '; Latin nud, -ere' nod, wave, beckon, bow, lean ', nuto, -are' sich 
hin und her neigen, waver, wobble, give way', nutus, -us' nod; commandl will, beckoning gesture, 
order', numen " beckoning gesture, volition, divine will| divinity; god ' ( *neu-men, or as *neu-smen 
= gr. VEuija from *v£ua-Ma with here certainly root-like a); Old Irish noi'd ' makes known', 
*ate-no- "entrust', verbal noun aithne " deposit! trust; money placed on deposit/safe keeping; 
contract on trust money ' = cymr. adnau6s.; 

with formant. -r(o)-'cuss. (etc.) ponuryj {*neu-ro-) " lowered (of the head), low-spirited (of 
the eyes) '; with the meaning ' stupfen ' presumably gr. vupsT vuoasi, vupajv vuoaojv, ^uwv 
Hes., and (?) Lithuanian n/urkyt/" press, squeeze'; 

with 5^ further formations: gr. vuoau), Attic vuttoj " prick, prickle ', vuyu) Hes., Pass. Perf. 
VEvuyijai, participle present vuyzlq; with intensive strengthening vuKxa^u) vuaau) Hes., 
Middle Low German nuck{e) "sudden push, malice, spite; danger, peril, perniciousness; vagary, odd 
or unexpected action or idea, fickleness ', md. nucken " fall asleep, doze off, nod off ', Middle High 
German ent-nucken6s., perhaps also Old Church Slavic n(j)ukatr encourage, stimulate'. 

Maybe alb nduk' pull, pinch ' 

References: WP. II 323 f., WH. 186, 189 f., Schwyzer Gr. Gr. 1, 7174.
```


## [2026-09-07T19:30:02.102Z] TOOL CALL #10: Bash

```json
{
 "command": "grep -n \"e-neuen\\|neuen\\|Root / lemma: e-\" /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt | head -20"
}
```


### [2026-09-07T19:30:02.149Z] TOOL RESULT

```
25715:Root / lemma: e-3, ei-, /-, fem. T-{*he-3) 
26053:This is all wrong etymology. Root / lemma: e-3, ei-, /-, fem. T-\ "this, etc. (demonstrative 
26516:Root / lemma: e-neuen, neuQ, enuQ 
26523:Root / lemma: e-neuen, neup, enup {* henek'i-)'. nine' was created as a compound of Root 
26598:ordinals: *neueno- in Latin nanus, introduced after the 7 and 10 m instead of n Umbrian 
45361:Middle Irish cnu. Gen. cnd{*knus, *knuuos), cymr. cneuen, PI. cnau, mcorn. knyfan. 
62984:See also: Changing through ablaut nu' now' see there; s. also *e-neuen^ nine '. 
81685:stechenio a neuen Einheit zusammenschloft; so based on formal auf *stig-, but with the
```


## [2026-09-07T19:30:06.512Z] TOOL CALL #11: Bash

```json
{
 "command": "sed -n '26516,26620p' /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
}
```


### [2026-09-07T19:30:06.557Z] TOOL RESULT

```
Root / lemma: e-neuen, neuQ, enuQ 
Meaning: nine 



Note: 

Root / lemma: e-neuen, neup, enup {* henek'i-)'. nine' was created as a compound of Root 

/ lemma: neuos, -ios: new' + Root/ lemma: oRtd(u)\ eight'. 

Material: Old Indie nava, Avestan nava{neun) '9'; 

Armenian //7/7(sprich inan) '9' {*enun), PI. in(n)unk\ (under the influence of common 
Celtic -ns-, -nt- > -nn-). 

(*gr. *£Fva- through metathesis to gr. *£vFa-) gr. *£vFa- in hom. £iva-£T£(;, -vux£<;, 
Boeotian £va-Kr|-5£KaTr|, Ionian £iva-K6aioi, Attic £va-K6oioi; Ord. eivotoc;, Attic Aeolic 
bjaioq;, *£vFa also in hom. £vvr|pap (*£vF npap) "9 days'; besides *v£Fa ( *neun) in £vv£[F]a 
(prefixed with £v, Schwyzer Gr. Gr. 1 591); thereafter became £vriKOVTa "90' to Ionian Attic 
£V£vriKovTa; 

thrak. £V£a (v. Blumenthal IF. 51, 115); 

Note: 

This is wrong etymology. Greek order was reversed Root/ lemma: oRtd(u)\ 'eight' + Root/ 
lemma: neuos, -ios: 'new' > gr. *£Fva-: zwd-zizc,. The shift k'^> p, g"'> b'\s a common gr.. 
Greek also reflects an lllyrian-alb. trend as it puts the ordinals and adjectives after the 
noun while in IE languages the adjective and ordinal precedes the noun. 

[Phonetically attribute] alb. nende'9' {*neunti- 'number of nine', as Slavic dev^tb '9', Old 
Norse /7/^/7c/' number 9' and Old Indie navatf-, Avestan navaiti-i. '90', actually nine of 
tens); 

Note: 

Anatolian languages show a pattern similar to alb. So Lycian aitata {* oRtd(u)ta) 'eight' : alb. 

/e/a 'eight'; Lycian nuntata ^n\ne' : alb. nanda'n\ne'. Therefore alb. shtata 'seven' derived 

from a truncated *sa{pjtata ' seven' later Old Indie saptathah, Avestan hapta&a-. Old 

Saxon sivotho. Old English seofoda, Lithuanian septintas, also Old Indie saptatf-, Avestan 

haptaiti-lQ\ in alb. -ta, -teare attribute endings that were solidified in Anatolian and Indie 

cognates. The attribute /a (used in the genitive and adjectives) is unique to alb. language 

alone. 

Therefore alb. teta "eight' is a zero grade of Lycian a/tata {*oRtd(u)ta) 'eight'. It was initially 

an ordinal number used as an attribute [compare Latin octuag/nta' 80']. 

Alb. Tosc nanta, Geg nanda' nine ' derived from Lycian nuntata 'n\ne'. 



Slavic follows alb. attribute -/e [nasalized -nte; -nc/e en6'\ng] 

Latin novem' nine ' {-mior -/?? after septem, decern); 

Old Irish noi n-, cymr. corn, naw, bret. nao {to as. Pokorny IF. 38, 190 f.); 

Gothic Old High German n/un, Proto Norse n/u, Old Norse n/io'Q', Old Saxon n/gun, Old 
Frisian ni(u)gun. Old English /7/jc/7 (from *niuuun); 

Note: This is wrong etymology. Germanic family reflects the compound {*niuktuun) from 
Root / lemma: neuos, -ios: new' + Root/ lemma: oRtd(u)\ eight'. 

Lithuanian devyni, Latvian devini{n- still in ordinals Old Prussian newTnts), Old Church 
Slavic dev^tb " nine ' {d- becomes steady probably through dissimilation against auslaut n 
and through influence of the 10; Berneker 189); 

Note: 

Old Church Slavic devgtb " nine ' derived from Lycian nuntata 'n'\ne' the same as alb. Tosc 
nanta, Geg nanda^ nine ' [common alb.-lllyrian n > nd > d\. 

Tocharian AB nu^ nine '. 

ordinals: *neueno- in Latin nanus, introduced after the 7 and 10 m instead of n Umbrian 
nuvime' the ninth ', Old Indie navama-, Avestan naoma-. Old pers. navama-. Old Irish 
nomad, cymr. nawfed {*neum-eto-); -/oformation also gr. ziva^oc,, evaroq {* enun-to); 
Gothic niunda. Old High German niunto. Old Norse nionde. Old Saxon nigundo, nigudo. 
Old Frisian niugunda. Old English ni^oda, Lithuanian devintas. Old Prussian newTnts, Old 
Church Slavic dev^tb; Tocharian B nunte, oblique of nunce. 

Note: 

Ordinals in IE are built according to lllyrian pattern; alb. -/a adjective formant: alb. Tosc 
nanta, Geg nanda^ nine ' : Lycian nuntata 'n\ne' 

One assumes connection with *neuo-'ne\N', because a new countable segment has 
begun with 9, while the binary form from *o/(tou'8' points to a 4-calculation system. 

References: WP. I 128, Feist 378 f., Schwyzer Gr. Gr. I 590 f. 
Page(s): 318-319 



Root / lemma: eng"-, gg^en {eng^h^ 

Meaning: swelling
```


## [2026-09-07T19:30:14.623Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^newn\\|newn\\.\\|nuntius\\|nuncio\\|announce\" AHD_watkins1985.txt | head -20; echo ===; grep -n -i \"neu-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T19:30:14.676Z] TOOL RESULT

```
Exit code 1
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.] bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan (*for, before; see per') in: a. Old English béodan, to proclaim: BID; b. Old English forbéodan, to forbid: FORBID; ¢. Old High German farbiotan, to forbid: VERBOTEN, @: Germanic *tudén- in Old English boda, messenger, hence bodian, to announce: BODE!. 3. Ger- manic *budilaz, herald, in Old English bydel, herald, messenger: BEADLE. 4, Germanic *budam in Old Norse bodh, command: OMBUDSMAN. 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE. [Pok. bheudh- 150.]
608:Germanic *hal6n, to call, in: a. Dutch halen, to haul, pull (2? < “to call together, summon”): KEELHAUL; b. Old French haler, to haul: HALE?, HAUL. ITI. Zero-grade form *klo- (> *kal-). 1. Suffixed form *kal-yo- in Latin conct- lium, a meeting, gathering (< “a calling together”; con-, together; see kom): CONCILIATE, COUNCIL. 2. Suffixed form *kal-énd- in Latin kalendae, the calends, the first day of the month, when it was publicly announced on which days the nones and ides of that month would fall: CALENDAR, CALENDS. 3. Suffixed form *kal-e- in Greek kalein (variant klé-), to call: ECcLESIA, PARACLETE. 4. Suffixed form *kal-d- in Latin caldre, to call, call out: INTERCALATE, NOMENCLATOR. 5. Suffixed form *klp-ro- or suffixed variant form *klaa-ro- contracted to *kld-ro- in Latin clarus, bright, clear: CLEAR, GLAIR; CHIARO- SCURO, CLAIRVOYANCE, DECLARE, ECLAIR, ECLAIRISSE- MENT. IV. Possibly extended zero-grade form *kid-, becoming *klad- in suffixed form *klad-ti- in Latin classis, summons, division of citizens for military draft, hence army, fleet, also class in general: cLAss. [Pok. 6. kel- 548.] kelp-. To hold, grasp

... [3073 characters truncated] ...

d: NUTATION; INNUENDO. 2. Suffixed form *neu-men- in Latin niimen, “a nod,” hence “command,” divine power, deity: NUMEN. [Pok. 2. neu- 767.] neud-. To make use of, enjoy. Germanic *nautam, “thing of value, possession,” in: a. Old English néat, bovine
786:newn
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
1946:NUNCIO neu-1 NUNCUPATIVE kap-, nd-men- NUPTIAL sneubh- NURSE (s)nau- NURTURE (S)nau- NnuT ken-5 NUTATION neu-2 NUTHATCH skep- NUTRIA wed-1 NUTRIENT (s)nau- NUTRIMENT (s)nau- NUTRITION (s)nau- NUTRITIOUS (s)nau- NUTRITIVE (s)nau- NUX VOMICA weme- NUZZLE nas- NYCTALOPIA nekw-t-, okw- NYCTITROPISM nekw-t- NYMPH sneubh- NYMPHOLEPT (s)lag¥- NYSTAGMOUS sneud(h)-
(eval):1: == not found
```


## [2026-09-07T19:30:15.747Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"nalidan\\|nālīdan\\|nal-\\|nard\" CHEUNG.txt | head -40"
}
```


### [2026-09-07T19:30:15.800Z] TOOL RESULT

```
255:made to come up with a comprehensive work. For example, Leonard Hertzenberg 
558:(Skt. bharv), *gaus ‘to hear’ (Skt. ghos) and *nard ‘to lament, moan’ (Skt. nard), 
4848:(ha)nardin/ner- ‘to send’ (connected to *Hnar ?), Gur. (Kand.) nimdir-/-ámdür- “о 
11357:hinér-, (Central) (ha)nardin/nér- ‘to send’ (with sec. hin-, han- ?) 
11369:stretch out, extend; to pour, flow out’ || (+ *ni-) ? Wa. nards (in nards di-, roč- ‘to run 
12511:Oss. nard, narst ‘fat, well-fed’ || (+ *abi-) ? Oss. I. evnalyn/evneld, D. evnalun/ 
18585:*PARTHIAN: ? n’r- ‘moan, groan’ (rather *nard ?) = Ghilain: - | DMMPP: 238a 
18605:282 *nard 
18608:*nard ‘to lament, moan’ 
18627:nalin/nal-, Zaz. nalayis/nalen- ‘to moan’, Anar. nolo/enol- ‘to groan’, Gz. nal-/nala, 
18628:Khuns. nal-/nala ‘to lament’ 
18632:*SANSKRIT: nard ‘to hum (while singing samans), to roar, to bellow (of animal, 
42294:nalin/nal-, 282 
42631:(ha)nardin/nér- 
43809:nal-/nala, 282 
44271:nal-/nala, 282 
46802:nard, narst, 183 
51716:nard, 282 
55793:*nard (s.v.), *raH (s.v.) 
57039:*nard, *xsai, *zarH (s.v.) 
57214:*nard
```


## [2026-09-07T19:30:26.096Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('neu-!')\nfor m in re.finditer(r'neu-[!1¹]\\.', t):\n    print(m.start(), t[m.start()-200:m.start()+900].replace('\\n',' '))\n    print('-----')\nEOF"
}
```


## [2026-09-07T19:30:26.114Z] TOOL CALL #15: Bash

```json
{
 "command": "sed -n '18580,18660p' /home/sfmqrb/git/rishe/data/verification/sources/refs/CHEUNG.txt"
}
```


### [2026-09-07T19:30:27.299Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-07T19:30:27.355Z] TOOL RESULT

```
*nar ‘to roar, bray, thunder ?’ 


*PARTHIAN: ? n’r- ‘moan, groan’ (rather *nard ?) = Ghilain: - | DMMPP: 238a 

Pres.: IND. 3р1]. *n’rynd 

*KHOTANESE: ? nar- ‘to roar’. 0 The existence of this root, postulated in DKS: 174b 
is doubted by Skjarve, SVK П: 64 f., 73 f., especially since one of the two forms in 
support of its existence, пага, must be read as tfärä. 

*CHORESMIAN: mjnr- ‘to roar, moan, bray’ (or mjnr- ?, cf. MacKenzie I: 544) 
= Samadi: 132 

*NEIR: Oss. I. пагуп/пазгѕі, D. naerun/nzrst ‘to thunder’ 

% An IE provenance for *nar cannot be established. This Ir. root is perhaps 


expressive, similar to Du. sneren, Engl. to sneer. 
«REFERENCES: Abaev, Slovar’ II: 171 f.; DKS: 174b 


282 *nard 


*nard ‘to lament, moan’ 
*MIDDLE PERSIAN: ВМР nt /näl-/ ‘to lament, moan’, MMP n’rysn ‘moaning’ 


{unpublished} = DMMPP: 238b 
Partic.: pres. BMP n'I'n /nalan/ 


*PARTHIAN: ? n’r- ‘moan, groan’ (rather *nar ?) > DMMPP: 238a 
Pres.: IND. 3р1]. “n’rynd 


*SOGDIAN: BSogd. nrö- ‘to lament’ (Benveniste, TSP: 25 f., 175 ad 507) 
Pres.: IND. 3sg. BSogd. nrött {hapax} 


*CHORESMIAN: nrö- ‘to lament’? — Samadi: 132 

*NWIR: NP nälidan/näl- ‘to lament’, Bal. narit/nar- ‘to groan’, Kurd. (Kurm.) 
nalin/nal-, Zaz. nalayis/nalen- ‘to moan’, Anar. nolo/enol- ‘to groan’, Gz. nal-/nala, 
Khuns. nal-/nala ‘to lament’ 

*NEIR: Pash. naral/nar- ‘to screech (of birds, etc.); to bray, bellow, low’ 

*SANSKRIT: nard ‘to hum (while singing samans), to roar, to bellow (of animal, 
human, cloud)’ (Br.+) = EWAia II: 22 

9 This apparently Ilr. root is probably expressive in nature, similar to ME snurtin ‘to 


snore’, MHG snarz ‘rattle; landrail’. 
*REFERENCES: Ivanow 1926: 421; EVP: 53; WIM I: 71; WIM II/1: 80; Omar 1992: 423a; Gharib: 242, 
no. 6054; Werba 1997: 464; Paul 1998: 306b; NEVP: 58; Korn 2005: 220, 319, 408 


*narp ? ‘to decrease, wane (of moon)’ 

*AVESTAN: norof- “о decrease, wane (of moon)’, OAv. narapis- (n.) ‘decrease, 
waning’ = Liste: 40 

Pres. inch.: IND. 35р. OAv. nerofsaiti (Y 44.3), YAv. norofsaiti (Yt 7.2, Ny 3.4); Partic.: pres. YAv. 
norofsas ° (Yt 7.2, Ny 3.4) 


9 With no further correspondences, the Av. forms are hardly of Ir./IE origin. 
*REFERENCES: Kellens 1984: 157 ad 15. 


*nas ‘to disappear; to perish’ 

*AVESTAN: näs- ‘to disappear’ || (+ *apa-) ‘to vanish’ || (+ *ui-) ‘to vanish’. 0 YAv. 
na@ation (V 3.20) cannot belong to this root at all (pace Kellens 1984: 297). 
= Liste: 41
```


## [2026-09-07T19:30:38.777Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"neu-.\\{0,20\\}To shout.\\{0,600\\}\" AHD_watkins1985.txt | head; echo ===; grep -n -o \".\\{200\\}nuntius.\\{0,400\\}\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T19:30:40.117Z] TOOL RESULT

```
Exit code 1
785:neu-'. To shout. Suffixed (participial) o-grade form *now-ent-(yo-), “shouting,” in Latin niintius, “announc- ing,” hence a messenger, also a message, and ndéntium, message: NUNCIO; ANNOUNCE, DENOUNCE, ENUNCIATE, PRONOUNCE, RENOUNCE. [Pok. 1. neu: 767.] neu-2, To nod. 1. Latin *nuere, to nod (attested only in compounds), frequentative nutdre, to nod: NUTATION; INNUENDO. 2. Suffixed form *neu-men- in Latin niimen, “a nod,” hence “command,” divine power, deity: NUMEN. [Pok. 2. neu- 767.] neud-. To make use of, enjoy. Germanic *nautam, “thing of value, possession,” in: a. Old English néat, bovine
(eval):1: == not found
```


## [2026-09-07T19:30:48.976Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"nuvid\\|novid\\|nûvîd\\|navîd\\|zanûd\\|zanud\\|zenud\\|nālīd\\|nalid\\|nâlîd\" HRN.txt | head -30; echo \"=== leaf149+21=170\"; awk 'BEGIN{RS=\"\\f\"} NR==170' HRN.txt | head -50"
}
```


### [2026-09-07T19:30:50.277Z] TOOL RESULT

```
=== leaf149+21=170
— 148 —
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
g. Jen (Vullers sen, Asteräbäd); Käs. K. zen, Jen,
Jin, Z. mn,
aw. Jeni- (y. 53, 6), Jaini- (y. 10, 17) *Weib'; phlv.
zan; ai. Jäni-, Jäm- 'Weib, Gattin'; arm. kiu 'Frau'
(H. No. 144).
kurd. 2in 'Weib' (zaza Jev); af/. Jinat, JünaJ; bei.
Jan (174) ; si;'n. yin, sar. yJw, ;^m, niinj. zinga.
669. jSJ^^icx 'Kinn', zene/dän,
ai. Äaww- 'Kinn'; aw. zanva- (Geldnor, KZ. 30,
514); arm. cnaut Kinnbacke, Wange (H. No. 137).
af}'. LW. zana, zana/; bei. zanük, zanlk, n. zatm/
'Kinn' (LW.) (416); wa;<. zanax (i^W.) , si^'n. zingü,
sar. zangän,
670. ^eii<J gross, stark', vergl. zende plV),
aw. vergl. /ra]^«^^«-; phlv. zand[])tl (PPGL); ai.
vergl. Jantü- 'Geschöpf, Wesen, Mensch'; lat. gern, (?)
V
*3 Vergl. np. äsfl neben äsitn (Sahn. I, 177 Vers 874), ähenl (häre)
Sahn. I, 187 Vers 1054 neben ahemn (bare), Hahn. I, 39 Vers 96.
*) C'^'utjv (Glossator zu Mich. Psellus, de Lagarde Ges. Abh. 222)
ist direct das moderne np. zennn.
3) Arm. LW. zafwar (Hubs eh mann, ZDMG. 35, 134, No. 40).
*) Sputer mit Angleichiing an zhnle Mebondig* zhifle pil go-
sp rochen.
```


## [2026-09-07T19:30:54.314Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### leaf171\"; awk 'BEGIN{RS=\"\\f\"} NR==171' HRN.txt; echo \"### leaf258\"; awk 'BEGIN{RS=\"\\f\"} NR==258' HRN.txt"
}
```


### [2026-09-07T19:30:55.534Z] TOOL RESULT

```
### leaf171
149
Der Bedüutungsunterschied macht diese Zusammen-
stellung bedenklich.
671. niindän 'Gefängniss'.
aw. *2:aewa.d(2wa- (y) ; ^\\\\, z(i)ndan (PPöl.); arm.
LW. zndan.
Etwa urspr. 'WafFenarsenar wie auch HNIliNDN (Jer.
32 (2) 8) *Ort, an dem die Scheiben aufgehoben werden*,
allgemein 'Gefängniss* heisst? Darmesteter, Et. ir.
I, 290 setzt zweifelnd auch np. zen}Tr^ zmjlr (andere
iranische Formen siehe bei Geiger bei. LW. No. 299)
hierher 0. Vergl. Hörn, KZ. 32, 583 No. 13 2).
672. xinüden, zunüden *heulen , Praes. ziuec-em, ztmöylden.
ai. [/'nav-j naiiti, ndmite *brüllen (von Tieren)', mit
accha 'zurufen' (mit ud kommt es nicht vor).
Vergl. np. nöyiden etc. (No. 1054).
673. xüd 'schnell'.
aw. \/jav- 'eilen*, Java, javarö (?, Geldner, BB.
XIV, 21, 22, aber auch KZ. 30, 533); phlv. zät (päz.
zöt); ai. i^jav-, jdvate *eilen*.
kurd. zu; bei. züt^ zU, n. zid^ (430).
674. zur 'falsch; Lüge*.
ap. zurah- {znrah-) ; aw. zurö.Jata- ; phlv. zur,
zür]zat, zür]ynhäsih, arm. LW. zur\ ai. hvaras-.
Bartholomae, zuletzt ZDM6. 46, 296, Ilübsch-
mann, gleichzeitig ib. 329.
674*»^'* {\)»ör 'Kraft, Gewalt' (reimt auf hör, Sahn. I, 202
Vers 1311).
aw. zävar- 'Macht, Kraft*; phlv. zör, zörlh, arm.
LW. zatir^ zaurcwor, zauruüun,
LW. kurd. afy. bei. (312) zör.
675. {^i)zör 'Weihwasser (pärsisch).
aw. zaotirä' 'Weihwasser*; phlv. zölir, zur, arm.
*) Im Ossctisclicn bezeichnet das L W. zjndon *Höllc* (v o n
Stack elberg, Baltische Monatsschrift, XXKVIII, lieft 8, 674).
*J Herr Prof. Nöldeke vermag zindän mit plene geschriebenem
i bezw. e im Pehlevl zu belogen, was für die Richtigkeit der obigen
Etymologie spricht.
### leaf258
- 236 —
1052. nÜH jetzt, nun', vergl. ekniln, kunün.
aw. nü, nürem jetzt', vergl. oss. d. mtr, t. njr 'nun'
(207); §iyn. nur, sar. nur *heute*; phlv. nun; ai.
nündm,
bei. nü^ nun jetzt, nun (270).
1053. uuved *frolie Botschaft.
Die übliche Erklärung aus ni -j- l^vaed-, vergl.
aw. niva^dayemij ist erstens wegen der auffälligen
Erhaltung des d bedenklich und zweitens scheint
wegen np. pizöhlden im PehlevT n(i)v(i)hmUan, nicht
n(i)vedinltan gelesen werden zu müssen (vergl. No. 314).
1054. nöylden 'klagen (Sahn. I, 183 Vers 986, Calc),
necä 'Klage', nevtden, vergl. nevaliden, nallden.
ai. i/'nav-, nünti, ndvate 'brüllen (von Tieren)'; vergl.
np. zlnüden (No. 672).
1055. ne (geschrieben neh) nicht'.
aw. na; päz. na\ ai. nd.
kurd. ne; af/. na; oss. d. ne, t. nä (201).
1056. nu (geschrieben nah) neun'.
ap. navama- 'neunter ; aw. nava, näuma-, naoina-
neunter; phlv. wawm; d^.,ndva; arm. iw« (H. No. 115).
kurd. ne(h), ne(h); aty, LW. nu{h); wa,/, siyn. ndo,
sangl. minj. nao, yayn. nau, sar. nev.
Np. nuhiim ist eine ganz junge Bildung, die man
nicht auf das PehlevT übertragen darf.
1057. nihäden ^hinlegen, hinsetzen', Praes. w/Ä-e/w, aber
neht (AM. 65 Zeile 10).
aw. ni + 1^2 da- {nidadät) 'hinsetzen'; phlv. n(i)hatan
(AV.); ai. m+ l^l dha- (nldadhäti),
1058. nihän Verborgen, heimlich*.
ap. ^nidäna- 'etwas (heimlich) hingelegtes*, vergl.
ind. ni -f- [/'dhä- 'niederlegen zur Aufbewahrung oder
um zu verbergen'; phlv. n(i)hän.
nehmär 'zahllos* siehe sumär (No. 791).
1059. nihuften , nuhuften Verbergen', Praes. nihuft-em,
niheirihiden ^), nnhumhtden ^).
') Geschrieben -wZ>-.
```


## [2026-09-07T19:31:12.990Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 112 113 114; do echo \"### leaf$L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' HUB.txt | head -60; done"
}
```


### [2026-09-07T19:31:14.123Z] TOOL RESULT

```
### leaf112
- 101 —
1023. Arm. nkan ftihrt zu phi. nikan ^) = np. *nigan, aber
nicht zu nan. Bal. nagan etc. setzt Iran, "^nagan^
voraus. Zur Noth liesse sich fUln vielleicht aus
"^nayna- erklaren.
1024. Zd. navaza- (KZ. 27, 252) = arm. LW. navaz 'Schiflfer*
= skr. navajd- = lat. *navigu8 (in navigare) ZDMG.
35, 662. — Hierher auch np. naxudd *Schiflfscapita,n*
aus ''^nav'Xuda.
1026. Dazu np. naryan 'Hengst', von gleicher Bildung wie
mOdiydn 'Stute' (aus *nartkan, '^matlkan).
1032. Die Form nisaxtan auch bei Fird. I, 246, v. 57 als
Nebenform von niSastan, vgl. Horn Nr. 1033.
1033. Praes. niStnam aus "^nisldndmiy wie sikanam aus
*8kadnamiy? Vgl. Fr. Miiller, WZKM. 6, 190. —
Dazu afgh. -nastql sich setzen', pr. 3. sg. -nF, ptc.
.'nOst (mit der Praep. k^S- zusammengesetzt).
1034. Np. niSeh ist Gegensatz von bulandl *Hdhe' Fird.
1, 107, V. 840 und oft zu firaz *hinauf . Dazu phi. nisepak
*Untergang' (von Sonne und Mond) Min. cap. 49, 27,
wo im Paz. nis^wa fQr vahSza zu lesen ist (West, les
textes du Mainyo-i-Khard p. 11, Mann, ZDMG. 47,
705). Kurd. LW. sdr neStw umgekehrt' (*Kopf unten)
Socin, kurd. Samml. II, 340.
1034»>*»- Np. ndSftn 'Nest' (mit %l) = *nisfdman'? Vgl.
Fr. Miiller, WZKM. 6, 190; Mann, ZDMG. 47, 706.
Horn stollt das Wort jetzt (KZ. 33, 435) zu skr.
ksBma- 'Aufenthalt, Rast'.
1035. Das ptc. pass, einer Wrzl. nabh wiirde im Avesta
urspr. *nabda^ lauten, kQnnte aber auch nach der
Analogic der zahlreichen Ptcp. auf -ta zu napta- um-
gestaltet werden, vgl. basta- = skr. baddha^ etc.
Also liegt kein Grund zur Annahme einer Wrzl. naph
vor. Ist das Wort iiberhaupt indogermanisch ? —
Hierzu arm. navf 'Erdharz, Erdpech, ErdSl* (5. Jhd.),
gr. vd^&a.
^) Dieses nikSn 'begraben, yersohArrt' = paz. nag^n u. s. w. siehe
bei Horn p. 286, Nr. 148.
### leaf113
-- 102 —
1038. Im Phi. steht, so viel ich sehe, immer nikfrisn, niki-
rttan etc., im Paz. nigeriSn^ nigareSn etc. Phi. niklret
= ap. *nikriyafiy? Vgl. oben Nr. 992 phi. m^nisn fiir
paz. manisn.
Hier fehlt np. nigun = phi. nikun *uingekehrt,
umgestiirzt* = arm. nkun 'niedrig'? WZKM. 7, 380.
Hierher nach Horn (KZ. 33, 434) np. nikuhtdan
'tadeln, schmahen' = skr. kutsay- schmahen, tadeln .
Schon bei Vullers, Radices, s. v.
1039. Np. nam aus *namna- ~ *nabna- wie kam aus ap.
kamna- = *kabna'. Dazu afgh. numd, nUmd u. s. w.
(Geiger).
1040. Die iranischen Dialektformen sind schwerlich ent-
lehnt, also iran. ^namad- anzusetzen.
1041. Zd. nimata- ist dunkel, vgl. Darmesteter, Zend-
Avesta n, p. 45, Anm. — Dazu osset. nimdt, nmdt
Tilz, Filzmantel', s. Verfasser, Etym. und Lautl. der
osset. Sprache, p. 129, Miller-Stackelberg, Fiinf
osset. Erzahlungen p. 62. Skr. namata- Tilz' ist LW.
1043. In phi. anaumet (sprich anomef) ist die Anlaut-
schreibung beibehalten. Np. naumed (= afgh. LW.
naurmd) ist eine neue Zusammensetzung aus na und
umU. Vgl. naumed Fird. I, 133, Z. 2.
1044. Lallwort.
1045. Wird nau (now) gesprochen, wie die Ipt. saw, rau
{soUy rou),
1046. Heisst na/vdxtan urspriinglich : streicheln, streichen,
schlagen'? Es bedeutet ein Instrument spielen (oder
schlagen), singen; schmeicheln, streicheln, liebkosen'.
Dazu auch nava 'Melodic, Gesang , arm. nuag *Melodie,
Lied*, nuagem singe, spiele ?
1047. Die Pehleviform nap (geschrieben napl Hajiab5d-In-
schrift Z. 4), zu der np. nava = jiid. tat. newe 'Enkel'
(Miller p. 74) aus phi. *napak 'gehort', geht auf den
ap. Nominativ napa zurtick; np. navada = phi.
### leaf114
— 103 —
*napat'ak auf den ap. Ace. *napatam = zd. napatem;
np. navCLs-a (unbelegt) auf einen ap. Ace. '^napdd''am
(vgl. zd. naptarem) zuriick. Daneben nahasa 'Enkel*
JRAS. 1894, 489.
1049. Sal. Shuk., pers. Gram. p. 39: nuvacL
1051. Np. mive^ nube konnen nicht hierher gehoren.
1053. Np. nuved *frohe Botschaft' stellt Fr. Miiller,
WZKM. 8, 98 zu arm. LW. nwer *Darbringung, Weih-
geschenk, Opfergabe', das ein phi. *nived voraussetzen^)
und zu zd. nivaedayemi 'ich kiindige an* gehdren konnte,
Doch soUte man dann im Neup. *nuvai erwarten.
1054. Np. naltdan 'klagen, seufzen' stellt Geiger (Etym.
und Lautl. des Afgh. Nr. 136) besser zu skr. nard
'briillen, kreisehen, afgh. nar^l *heulen, schreien'.
1055. Vgl. oben Nr. 1014.
1056. Np. null neun' hat sein hSrbares h (ZDMG. 38, 97,
vgl. paz. nuh neun , nahum *der neunte* Min. Gl. 142,
147, Shk. 260, jiid. tat. nuf aus nuh, kas. nuh-do)
offenbar von dah zehn erhalten wie hcfst *aeht' sein
anlautendes h von haft 'sieben.
1057. Pr. niham aus *nihiham, vgl. pr. diham von dddan,
Dazu np. nihdd *fundaraentum, natura, indoles', vgl.
unser *Anlage',
Hierher nach Salem ann: np. nahar = nahOr^
naxdra (afgh. LW. niharai 'breakfast*) 'Fasten, Friih-
stUek' (nach No Id eke niichtern, dann *gierig') von
na-xurdan nichtessen ? Ich finde nahdr = gierig,
durstig* bei Vis und Ramin p. 131, 6 v. u.
1059. Als iran. Wrzl. von nuhunbam : nuhuftan 'bedecken,
verbergen' wird *ni-dub, jedenfalls nicht ni-gup anzu-
setzen sein. Phi. n(i)huftan, n(i)huft Gl. and Ind. 230,
Shk. 259. Ebenso jetzt Fr. Muller, WZKM. 8, 190.
1060. Np. nal 'Rohr, Stengel, Rfihre' — afgh. nam f.
'Stengel* = skr. nadd- 'Schilf, Schilfrohr = arisch
"^narda- (Geiger, Etym. und Lautl. des Afgh. Nr. 140).
*) Vgl. arm. hrauer *Einladung* = zd. frava^Sa^ ; arm. paiu&r
*Befehl' = zd. *paitivae3a' (jpaitiva^Say^mi *ioh kUndige an*) nach
Fr. Miiller, WZKM. 7, 371.
```


## [2026-09-07T19:31:35.363Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-07T19:31:36.537Z] TOOL RESULT

```
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
```


## [2026-09-07T19:31:40.780Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for p in 278 292 293; do echo \"##### pdf page $p (printed $((p+1917)))\"; awk -v n=\"$p\" 'BEGIN{RS=\"\\f\"} /\\[pdf page '\"$p\"'\\]/{print}' BQT_v4_pages.txt | head -70; done"
}
```


### [2026-09-07T19:31:42.012Z] TOOL RESULT

```
##### pdf page 278 (printed 2195)
[pdf page 278]
-م۱۹- فوژه
نو ۱ - بنم اول وسکون تانی‌مجهول ‌ و شکوفه‌های نوشکفتهٌ چمن باشد ‏
وزای فارسی » بممنی‌دویم فوزاست که‌کاج وصئوین نوات « با زای فارسی بروزن سوزان,
باشد ۴ ؛ و بی گوبند درختی است مانندصنویر | نام رودخانهایست بانهیب- وشوریسیار وفرباد وصد!
که پیوسته سبز وخرم است .* و بانك سهمناك را نیز کوبند ۴ .3
نوزاد « با زای نقطه‌داربر وزن اوتادء نوژن * » با زای فارسی‌بروزن سوزن,
نام دهی است درخراسان از اراضی طوی ودرآن | درخت صنوبر وکاج راگوبند .
جا بزرکیآسوده است ۴ - نوژنده ‎٩‏ (۱) - بفتح اول بر وزن
نوزادگان چمن - بمسنی‌بورستگان | ارزنده » بمعنی موئر واثر کننده باشد .
و نوژه ۷ - بنم اود و فتح زای فلرسی
‎٩9[‏ خم۳ : لوزنده +

< بوز * نوج . رل : نوژن » ناژ . ورك : ثابتی ص ۲۱۷ ۰

۲ - ز زاغان بر نو ژ کوب ی که هت کلاء سیه بر سر خواهران .

2 منوچهری ص۱٩‏ > ور : [ و ۹

۴ - نوزاده دهی‌ازدهستان گلمکان بخش‌طرقبه شهرستانمشهد. دارای۱۵۸سکنه - دهی از
دهستان مرکزی بخش حومةٌ شپرستان کاشمر دارای ۳*۰ سکنه - دهی از دهستان عربغانه بخش
شوسف شهرستان بیرجند دارای ۳*۱ سکنه « فرهنگه جغرافیائی ابران ج ‎٩‏ ص 4۲۹

۴ - « نوژان . رود (یعنی رودخانه ) با باك وسهم بود . منجيك (ترمذی) گفت :

ها برفتیم و شده نوژان وکحلان () پی ها

بغبی کفتی نو کش سلب از آنقای است .»
« لفت فرس ص ۳۸۹ >
وظ . بجای ‏ کحلان » « وخأن » است که نام ناحیه و رودیست درفمت علیای درء جیحون:اقبال,
لفت فرس ایضاً 4 *. 8 < بوژ* نوز* نوج ؛ و رك : ناژ :
نوژن دب است . هردم از قامت او فر‌باد ز سرو بوستان میریزد .
شمی‌طیسی « فرهنگه نظام >.

‎٩‏ نوزنده » از دسائین « فرهنگه دساتیر ص ۲۷۱ > ۷ - دررشیدی «نوزه»

‏5 نوزده << نوازده ۶ اسشق ۱۶۶۸ « ژابا ص 42۲۵ >؛ بشم اول وفتح دال» پهلوی
‎٩ ) 882420 ( 8‏ نبیر که س ۱۵۵ ۰ اوستا 38۷841888 ( نوزدهم ) » هندی
باستان 26۷84888 ( نوزده ) » افغانی 00183 , 88888 ۰ استی 321438 » 81035 :اسشق
۸ کردی جع - ۵7 , 0۵2068 , 00202 ؛ زازا 68 - 86۷ « ژابا س ۸۲۵+
عدد نه بعلاوة ده » قدد بین هیجده و ابیست .

##### pdf page 292 (printed 2209)
[pdf page 292]
۱۹ بریدن
ومتحرك شوی هم هست ۰۱ کوید , پعنی بلرزد وبنالد ونوحه کند ۴ - وبا
وان - بروزن کوبان » پادشاهزادمرا ثالی مجهول بروزن امید » عژده و هژژدکالی و
کوبند , وترکان ملوك و سلاطین را بدین انم | خبرخوش‌وهرچیز که‌سبب‌خوشحالی‌شوده وبشارت
خوانند؟ - وسبدی با طبفی را نیز کوبند که از دادن بضیافت ومهمانی وامیدوار کردانیدن‌ووعده
چوب بیدا بافته باشند . کردن بخغدمات دیوانی وکارهای بز رکه با نقع
۱ نویچ - بفتحاول‌وثانی بتحتا بیمجهول و ۱ ۹ ی متحرك ولرزان غد ولوزید
کشیدوبجيم فارسی‌زده, کیاهیاست که بردرخت 8 نویدن - بروزن دوبدن » بممتی‌زاری
پیچد وعربان لبلاب وعشقه کویند . کردن ونالیدن باشد۹ - وبممتی حر کت کردن
وید - بنم اول وتانی مجهول بر وزن | وجنبیدن ولرزیدن هم‌آمده است۷ .
۱ - رك : نویدن. ۴ # نوبین * نوین (مغولی) «رشیدی » « شموری » «عموماً
پادشاء اما خصوصاً خطاب سلاطین ترکان است > فرهنگه اظفری بتقل « فرهنگه نظام »4«نوبین »
نوبان » فرمانده سپاه . آمیر » نجیب > * جفتایی ۰۵۱۱ ۴ - « نویج بروزن عریج ولوج
بروزن عوج » اسم لبلاب معروف به عشقه است .» « محیط اعظم > + ۴ - رك : دوبدن .
- ۸0۷60 از : ۰۷2۵4-۲۴۵ قی اوستا 81۷26052600 « اسدق 4۱*۵۳
هوبشمان گوید : 813۷8 ( خبرخوش ) را ۳۳.۷/1116۲,۷۷2:1۳۸/.8,98 همريشهٌ آرمنی ع
7 (تقدم, فدیه. قربانی). ازپهلوی 281۷80613 میداند که‌به کلمه اوستایی 81۷860486701
(من خبر میکتم).مربوط است » بنابرین می‌باست درفارسی‌جدید 2810۷81 آمده باشدهعوبشمان
۴۳ کردی 860 ( امر » سفارش ) « ژابا ص2۲۷ >. كلمةٌ نوید را مرکب از پیشودد -81
+۷264 (7 کاهانیدن » بغارت دادن ) داسته‌اند « نا ص۱۱۵ ح۱ ». سبزواری 26۷16
( مژدکای ) « فرهنکه نظام » ۶ نوید . چنان باشد که کسی‌را بامید کنند . رود,کی (سمرقندی)
کوید :
اگر امیر جهاندار داد من ندهد چهارساله نوید مراکه هست خراب (خرام.دهشدا).
« لفت فری ص ۱۱۷ ۰۴
‎٩‏ - هرن کوید : 2811068 ( شکایت کردن ) ( شاهنامه 1 ۰ ۱۸۳بیت ۹۸۹ ؛کلکته).
نوا 86۷2 ( شکایت ) ۰ 360۷1068 . هندی باستان ۳۵۷ , 2801 ۰ 24۷816 ( غریدن
[ جانوران ]) ۰ قس : فارسی : زنودن « اسشق ۱۶۵۶ .
ز درد دل آن شب بدان سان نوید کم از ناله‌اش , هیچکی فنوید .
لبیبی « رشیدی ؟ .
ً اکنون زمفلسی چه نوی چندین بر درده‌اتی و اغم مغبولی ؟
ناصر خرء بلخی ص 2۷4 *.
و رك : نوان .
۴ - تو ازم ن کنون داستانی شنو بدین داستان بیشتر زین مئو .
پوشکور (بلخی) «لفت فرس ص4۱۷
آپری کز او کوهر بود » با دست او بر خود نود
باشد خجل کزچه بود هر دو جهاش يك خطا .
جمال‌الدین آشهری . « فرهنگه نظام؟.

##### pdf page 293 (printed 2210)
[pdf page 293]
نویده ۱۰۳
نویده" بروزن‌خمیده, بمعنی‌لرزیده | کوبند که‌از درخت‌رسته باشدوعر بان(۱) سر
وجنبیده ونالیده وزاری کرده باشد - خوانند .
نویم۲ « بفتح اول بروزن قدیم. لفظی نوییی؟ « بائانی مجهول بروزن‌موبین,
است که آلرادرعربی محض میگویند همچنانکه | بمعتی اول نوبان است که‌پادشاهزاده باشدءوملو4
کوبند «بنویم دیدن شناخت» بمنی بمحض‌دیدن | وسلاطین راکه خوش‌وقوم وقرایت باشدلیزبدین
شناخت* . تام خوانند ؛ ویعضی کویند ترکان سلاطین‌خودرا
نویه « بروزن موبه » شاخ نی وتازمرا | بدین نام خوانند.
بیان لیست وسیم
در نون با ها مشتمل بر هفتاد لغت و کنایت
3 « بکراول‌وظپورتانی, بممتی‌شهراست | میگوبند ۸ - واشاره برنه فلك - و نه سوراخ
مربان مدینه وبلد خوانند همچوشابو رکه‌نه | قالب آدمی باشد که آن دوسوراخ کوش ودوچشم
5 مت شیر خاندرةه ۰
ایور است بمتی‌شپرشاپور٩‏ ولهاوند مت شهن ام بینی‌ودهان اغ مه وس است-
آوند" چه‌درآنجا ظروف‌واوانی سپارمیاختهاس |" ً رخقای 6 سرا میکند
وامربنهادن هم هت بعنی بنه ویگذار۷ سوم وبفتح اول و انی. افاده معتی لیاقت‌هب
اول وظپورها(») عددی است که آنرا بعریی‌تمه | همچو شاخانه وبزرکانه ودرویشانه ‎٩‏ - وتضین
() چش: - وعربان - (۲) خم۱ : ثانی.
۱ - انم مقعول از « نویدن» (هم.) ۴ - از دساتیر ۶ فرهنگه دساتیرص ۰۶۲۷۱
۴ -« السرع والسرعرع » آنچه ببالد ازسرشاخ رز» «مهذب‌الاسماء نخةٌ خطی کتابغان
دهخدا! > و ر4 : منتهی‌الارب . ۴ نوبان (ه.م.). رك: جفتایی ص ۵۱۱: « خافان‌منصور
قلب میمنه و میسرة سهاه اف پناه را بنور طلمت خاء زادکان آفتاپ احتشام و فر وجود نوبینان
بهرام انتقام زیت و استحکام داده بمیدان جنگه و ممرکهٌ نام و اشگه فرستاد . > « میرخواند .
حبیب‌المیر. چاپ خیام اج ‎٩‏ ص۲۰۹*. 8 - فقه‌اللفهٌ عامیانه . رك : نیشاپور +
۹ - ققه‌اللقهٌ عامیانه . رك : نهاوند . ۷ - رك : نهادن -
۸ - پارسی باستان -38۷21738 (مم) ۰ اوستا 88۷2 821۷0138-۰ ۰ (نم)
پهلوی 32113 , هندی باستان 8۷8 , ارمنی 188 ۰ افغانی ع (320)10 ۰ وخی و شفنی ۰340
سنگایجی ومنجی 320 ۰ پفنوبی 831 ۰ سربکلی36۷ « اسشق ۱۶۵۹ > ورد: هوبشمان۹۱*۵۹
کردی 8610 ۰ 2۵ . 285 ۰ 8610 ۰ زازا 2821 ۰ دوجیکی 210 «ژابا س ۶۲۸ »پهلوی880.
ایرانی‌باستان -82۷8 ۰ بقرابت « ده » 1210 ساخته شدم. فارسی‌جدید 8118 از 8۵0 از -28۷8
با 8 بقیای 48 ۸« یب رکه س۶ ۱۵ > ‎٩‏ - درین کلمات پسوند ۶ آنه» است.
‎٩‏ نوین - ر4 : نوبان .
( برهان قاطع ۳۷۹ )
```


## [2026-09-07T19:32:24.000Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt && grep -c \"\" MON_part1.txt MON_part2.txt && grep -n \"نویدن\\|زنودن\\|زنوییدن\" MON_part1.txt MON_part2.txt | head -20"
}
```


### [2026-09-07T19:32:24.076Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
MON_part2.txt:94500
MON_part1.txt:99339
MON_part2.txt:81143:نویدن: 2۷-1000 (- ناویدن] (مصل.) 
MON_part2.txt:81145:نویدن: بر حود پیچیدن.
```


## [2026-09-07T19:32:24.752Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"نالیدن\" MON_part1.txt MON_part2.txt | head; echo ===; grep -n \"\\[pdf page\" MON_part1.txt | head -3; echo ===; head -20 MON_part1.txt"
}
```


### [2026-09-07T19:32:24.817Z] TOOL RESULT

```
Exit code 1
MON_part1.txt:49698:جاو بده). بانگ کردن نالیدن. راز و نباز 
MON_part1.txt:75790:گفت. (مص‌ل.) بانگ کردن کبوتر. نالیدن 
MON_part1.txt:93991:نالیدن عاجزانه» زارنالی. 
MON_part2.txt:1602:نالیدن و گریستن» زاری کردن. 
MON_part2.txt:38407:لایسیدن: :۱5۷70 (مصل.) نالیدن. 
MON_part2.txt:72823:نال: 2۱« ناله. امر از نالیدن؛ بنال. (افاء) در 
MON_part2.txt:72830:مر بض» بیمار. (ق.) در حال نالیدن, ناله کنان. 
MON_part2.txt:72847:نالش: 2۱-04« (امص.) عمل نالیدن» ناله. 
MON_part2.txt:72863:نالیدن: ۱2۱-2 (مص‌ل.) (نالید» نالدء 
MON_part2.txt:72868:آواز کت خواندن. نالیدن آلات 
(eval):1: == not found
```


## [2026-09-07T19:32:27.733Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '81130,81160p' MON_part2.txt; echo \"=== nalidan\"; sed -n '72855,72880p' MON_part2.txt"
}
```


### [2026-09-07T19:32:27.801Z] TOOL RESULT

```
تعالی» قر آن. 

نویان: 550« (- مغ. تر. - نویین - نوین] 
(.) امبر. فر مانده سیاه» سردار. ضح.- در 
عنوان سرداران مغول و ترک آید. 

لو ید: (0۷[066۷20 (.) خبر خوش» مژده؛ 
شارت. وعده نیکك. شارت دادن‌ه‌ضیافت» 
دعوت‌به مهمانی) مق. خرام. 

نویدگر: ۰-2۲ (ص‌فا.) به مهمانی خواننده» 
شارت دهنده به ضیافت. 

نویدن: 2۷-1000 (- ناویدن] (مصل.) 
جنبیدن» حرکت کردن. لرزیدن. بر خود 
نویدن: بر حود پیچیدن. 

نو یده. (0-)02[-۱3۲ (امف.) جنیده» حرکت 
کر ده. لر ز بده. 

نو یده: (6-)20۷-102 (امذ.) ناله کرده» زاری 
کر ده. 

نویس: 5[ (فعد.) مفرد امر حاضر از 
نوشتن. (افا.) در ترکیب به معنی نویسنده 
آید: کتاب‌نویس. 

نسویسا: ۱۵۶-3 (ص‌فا.) نو سنده) مق. 
تانو بسا. 

نسو یسنده: (0-)5-2002 (افا.) آنکه 
=== nalidan
مراعات نکند؛ ناجوانمرد. 

ناله: (200: (امص.) آوازی بلند که از 
سوز دل, از دهان بر آورند و حاکی از درد و 
غم و فصه و شکایت باشد. آواز بلند 
(مطلقاً)؛ نعر ۵. آوازی که از آلات مو سبقی 
برخیز د» نغمه. (مس.) نوایی است از موسیقی. 
(تص.) مناجات. رود کوچکك» جوی خرد. 
نالیدن: ۱2۱-2 (مص‌ل.) (نالید» نالدء 
خواهد نالید» بنال» نالنده» نالان» نالیده» 
نالشء ناله). ناله کردن» فریاد و فغان کردن. 
شحایت کرفن کله کون دعا کردن با 
زاری» تضرع کردن. نغمه محزون سر دادن» 
آواز کت خواندن. نالیدن آلات 
مو سیقی: (مس.) به ترنم در آمدن آن» نو اخته 
شدن آن. بانگ برداشتن» خروشیدن. تظلم 
کردن؛ دادخواهی کردن. رنجیدن. مر بض 
شدن» سمار شدن. 

نام: ( (.) لفظطی که بدان چیزی با 
شخصی را بخوانند؟ اسم. لفظ» کلمه. 
شهرت؛ آوازه (خوب)) مق. ننگ. نام و 
بانگ: شهرت و آوازه. نام و ندگت: نام و 
آوازه» شهر ت. نام نیکك: شهرت خوت. با 
نام: مشهور» معروف. خطیر» مهم. به نام: 
نامی» نامدار. به افتخار؛ با سر بلندی. نام بلند:
```


## [2026-09-07T19:32:36.381Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))['MON'];print(json.dumps(d,ensure_ascii=False,indent=1))\""
}
```


### [2026-09-07T19:32:37.637Z] TOOL RESULT

```
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
```


## [2026-09-07T19:32:48.225Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD nal\"; grep -n \"nālīdan\\|nalidan\\|nāl-\\|nālēnīdan\\|n'lytn\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD no/nine\"; grep -n \"^nō \\|nine\\|nohom\\|nawom\\|nāwom\" PHD.txt | head -30"
}
```


### [2026-09-07T19:32:48.302Z] TOOL RESULT

```
=== PHD nal
PHD.txt:494:nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
PHD.txt:2159:groan nāl-.
=== PHD no/nine
501:narm [nlm | M nrm, N ~] meek, humble, soft. nasā [ns’y | M n(y)s?h, № ~] corpse, carrion. nask [nsk' | N ~] a division of the Avesta. nasrušt(īh) [xslwšt', -yh] pollution, corruption. nastaran [nstln' | N ~] dog-rose, sweet briar. nawad [90 | N —] ninety.
516:—jh: weakness. nizārīh- [nz?lyh-] become weak. nē [ТА < A t£? | М пол, N nuh] nine. nóg [nek! | М mwg, N naw] new, recent. ~erz [-hvc | N nawróz] New Year's day. ---zád(ag) [-z't(k)! | N nawzàád] new-born. nohom [nhwm | = M, N ~] ninth. nózdah [nwzdh | № ~] nineteen. nin [KON < A k‘n | M, J поп] now.
2920:nine nē.
2921:nineteen nēzdah.
2922:ninety nawad.
2923:ninth nohom.
5280:nāydāg wahīg wihīr- nārīg wihīrišn nāysrāy nayizag wan- niyox&- niyox&idan niyoxiián wing wānīdan nān Worübarst Worüjarst nohom nihumb- nihumbidan Wahman naxust nihuftan
```


## [2026-09-07T19:32:49.536Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB\"; grep -n -i \"nālītan\\|nalitan\\|nāl\\b\\|nāwom\\|nohom\\|nine\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T19:32:49.592Z] TOOL RESULT

```
=== NYB
1369:druž [dlwc'] all that is false, untrue, wrong, deceptive: 1. the world of Guile and Untruth, conceived as a personal cosmic power, 3822, 9313. — 2. individual manifestations of this power, demons, conceived as feminine supernatural be- ings: sg. 5716-25, 583. 9620-24, 9817-19, 101% (voc.). 1023-14; ~ ; anāštēh 671; ^ 4 spazgeh 6811-12; ~ 7 ahramög 10124-25; pl. cas. rect. ~ 648. 65*. 9721, 9819 (of human beings). 10224-27, 1033; pl cas. obl. —-än in the set phrase devün u ~-dn 75" ete. (voc. 9027). V. also mthr-druz, mihrčin-druž. — Av. (778 sqq.) drug-, nom. druxš, gen. drüjö; MPrs drwaš (S); Paz. drü£.
2614:nahom [nhwm], nohom [nhwwm] the ninth. — MPrth nhwm; MPrs nw(w)m; NP nuhum.
2791:nózdahom [nwzdhwm; 19-wm] the nine-
3384:of His Mazdayasnian Majesty Sh. P I: 1; apar — 68 [this seems to be the correct reading] inthe year 68 [of the reign of King Shapur II] P2:1; ~ 58, àtur* + Artaxšer ~ 40 etec., v.s. v. tur; — ~ pat ~ year by year 191; pat har 40 m every 40th year 86**; pat 3 ~, pat 6 ~, pat 9 — in three, six, nine years 9319-21; 10621-22; pat 3000 ~ 4 menos āstišnēh within the 3000 years of heavenly exis- tence 3820-21; 393; ka 30000 ~ gētē āstišnēh (but), anaibigatik 330 ~ apäc but when it was the 3000 years’ (period) of material existence, and 330 years of the unassailed period still remained 3926-27; — hac én and — apäc so many years ago 1674. — Av. (1566) sarad-, OP Gard-; MPrthPrs sr; Paz. NP sal.
```


## [2026-09-07T19:33:19.319Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT nava\"; grep -n \"nava-dasa\\|nava\\.dasa\\|navadasa\\|navaiti\\|naoma-\\|nāuma\" BRT.txt | head -20; echo \"=== BRT nard\"; grep -n \"nard\\b\\|narəd\" BRT.txt | head -10"
}
```


### [2026-09-07T19:33:19.405Z] TOOL RESULT

```
=== BRT nava
2478:Stelle  der  kongruenten  Form  steht :  a)  das  i ;  —  iE  äbyö  frSrtt^  fr}r»m-ainti  asaonqm Neutr.  Sing.:  yüzim  .  .  aogS  data  .  .  x/a-  ..frtrvaBbyoYX.13.afi;  —  zugleich  zurück- '^nmcS  .  .  azimcll  ahyä  (statt  Du.)  ..'weisend:  asti'atjntö  ..  atihe  haxayü  frä- %wqm  mPtihi  ..vaSd>m{sA.)Y.2<).ia;  —  \yente  astvatjr?lahe  Yt.i'>.95;  —  dacnnm dva/sing  ..  qstqscä  .  .  yezT  ahyä^^  (statt'.,  atiihi  ..  kavaya  ..  daenayn  V./o.ig. Plur.) /ö/  mal  xsayehTY.44.\\i.; — duye  —  a)  mit  relativischem  Anschluss;  ama- navaiti  astanqm  (sd.)  .  .  däittm  ahmäicil  !'af6yö  acibyö  yazataHbvT'  yat  am»saeibyö harf^r?m  hrmi^ät  V.  74. 17.  b)  das  sp»^aAbyöYi.fj.^;  —  mmö  äbyö  döi'iräbyü
4439:j.  anairitay-  f.  Name  eines  Insekts,  das sich  auf  Hunden  aufhält:  duye  navaiti yaoidai'iTta  stiptibyasca  (sd.)  "riti- byasca  .  .  V.  i4.\T.
9867:•  j.  gao-8urä-  f.  'Reichtum  an  Rindern' (?) : TtrthrtrjnS  avi  imal  nmänpm  •räbyBijiV. als  IP.)  :^ar»nö  pairi.vsnnavaiti  (sd.)  Yt.
9947:■  j.  gaSwa-  m.,  gaSwä-  f.  'Hund,  Hün- din''' i)xa.:di^e  navaiti 'wqm{CiY,) pairi.- yaoidaikUa  stiptibyas£a{^^..'S.i4-  I7;  — bis  hapta  puhrqm  'wqm  (AP.)  uzjämöit (sd.)  V.  r4.  i6;  17;  —'  fra  mi  'wa  (NP. als  AP.)  sasayqn  mzbjnta  (sd.)  V,  8. 37.  2)  f.:  aiia  (näml.  hätrist)  ca%wan.- failißäna ya  'Tva'W .i^.iqGl.; — yaica  aisa toa  uÜrS-itänaisva /rajasät{sA.)  V.  15.23; — yS  °wqm  yqm  apu%Tqm  {sd.) /anaiä  vs ,.pasdaya/i{sd.)  vä  yaica  alsa  "wa  magye .  .  pai'jyäite  V.  Jj.  S ;  —  °wqm  yqm  apu- irqm  "^rayqm  *baesdri  "eine  Hündin,  die kürzlich  geworfen  hat,  . ,"  V.  15.49.
10903:•  j.  xänaoma-  m.  'Zufriedenstellung, Wohltat':  ks  paoirim  itnam  sam  mazista 'ma  xsnüvayäti  V.J.12.
13300:päyulca  ahmt  'täca  ^riita^a  ahmt..  Yt. /. 3;  —  navadasa  yai  akmi  °tö  (statt NS'.)"  Yt.  /.  8;  —  •tar?:  *ivajii,ra  .  . FrW. /o.  39;  —  'ta  ahura  sppnta  mazda VA.I.
13926:7. 74  No.  i),  i,yiini  enthaltenen  Basis  idg.  V^|-.   V.  18. 73^  **,   Vd,  6;  —  duye  (Af.)^'  navaiti
15171:—  u^&m  tristem  mdansaynt  kavaMya 'ätalibya'^  V.6'.46;  5.11.  b)  von  Tieren: aal  as?m  tanBm  aguu  a^airi 'ähm^*  gjuf armaYtiy.$$.  c)  von  Dingen  (nur Komp.).  3)  'Versteil,  Vers':  ahunavaitim gahqm  .  .  mal  vayiibyaca  *'at3byasca^'* Yx.14.1.         S,  noch  zu  upasu.
18522:j.  naoma-  Adj.  (fem.  'mr-):   s.  unter aavama-.
18613:•  j.  ^nava  indekL''  Zw.  'neun':  ya^  Ai  'va (als  Nom.)  xsafna  lacantt  Y.g.  35,  ig.  23; i/i.  10,  1 1 ;  —  'va  (als  Akk.)  ptrüwS . . i^rmuFa  V.2.  ^o;  5.  $1,  ().ii,  ii.jaPüZ., 10.18,  14-14,  17-6',  /^.aiPüZ.,  22.ao', P.g,  Yt4-ö(?>,  /9.41;  —  °^'a  «/«  may^m'^ V.5,  54;  —  -zraÄ  yatkj  navaitisca  °vaca sata  'va^a  hatattra  navasSsea  (sd.)  batvqn y.22.3;  YL/j.  59;  —  'va^a  navaÜTm^a "99"  Yt5. 8a;  —  'va  sala  upäzananqm V.  ^,  15;  15;  —  'va  (als  Instr.)  satäts harta.cnanqni  V,  4.  9;  —  *°va  *sat-lts^^ hazannmla  Ytj.  120;  —  'va  (als  Dat) druJaiH  xsa^raaiyd  V.4.10  PuZ.(?);  —  1 'vaijqm  (Gen.)  aspatiqm  ar/ham  V.  22. , 30;  —  *m?nääidyäi  (sd.) . .  'va  dasmi  Y.
18628:•  j.  navaiti'vant-  Adj.  'neunzigütch':  'ni (näml.  asti  mt^fH)  antar?  inlhra  Yt  10.
18629:KompA.  (1.  aoch  *itaimaya);  Ableit  —  ai. näva  (Gen.  navänani),  PDw.  »au ;  np.  vgL ituAii).  —   Pü.;  nöhO.g.  —  i)  S,  aber  Gen.  |  •   j.  nava.dasa-   Adj.   'der  neunzehnte'
18634:Ableit.  aos  *nava.dasa  indekl.  Zw. '19'.  —  ai. navadaiä-  Adj.;  woss.  vgl.  näudäs  '19'.  — Pü,:  navazäahnm.
18645:•  p.  navama-,  j.  naoma-'',  näuma-'^ Adj.  (fem.  'ml-)  'der  neunte' ;  H  8  manä taumSyä  tyaiy  x/äya'iiyä  äAa'  adam  °me^ Bh.  i.  3;  —  ahmat  haca  garayS  fraoxsyqn .  .  -mö  matisva  Yl  ig.  2 ;  /.  7 '',  14.  2  5,  V. /4. 9'';  —  yai  *mnn  (ASm.)  frasnaoiii asUmim  paiti.ra^wayält  V.5.  28'';  38'*; —  'm^m  (ASn.)''  asatjhqmca  .,  V.l.
18690:39,  79.69;  'Yt4-t,  Vyt.  74^;  —  duye navaiti  narqm  a/aonqm  vasiryaäa g^ . . - V.  74. 1 7 ;  A.  j.  7 ;  —  aü'hwSjgabmq  .  . narqm  aIaunqmY.13.3; — Sing.inkollekt. Sinn:  %rilum  nari  asaonS  frayoAuma- take  . .  apayasaitt  V.  18. 64.  c)'**  kas- na'^^  dtrita  tqmta  . .  avapastBt/ (sd.)  ks apB  . .  ks  .  .   iasnä'^^   "(welcher   Mann
18862:•  j.  nium^tn  Adv. :  s.  naoma-.
19201:•  j.  nivavant-  Adj.  (fem.  'vaitr-)  —?  —, käu  (nämL  kaine)  .  .  spanavaiti  'vaiti pasvaili  . .  V.  iq.  30.
19389:—  yaha  at^m  laurvaymi  vupe  yätavB  ,  . yat  mqm  na^ti taurvayat\x,i.^; —  Rica %wqm  cakana  .  .  htm  mqm  "/aiaaa  H. 2.12;  —  a  mqm  ava%a  vtrytunie  yaha anyasat  arlänS  avt  xhtdrh  xla%riAa hqm.V3r3navaititi  V./Ä.32;35;  —  s.  noch bei  3.  zu  I  b):  uHa  ba ytm  halahi  ula mqm  upatihal^i  Ytl^.j;  ~  mqm  sT mainyae yasaifm  Yt  10. 108 (?).  zu  a): paiti  mqm. .pinsanuAa yim  da%väaAim . . V.  /<?.  7 ;  Yt.  12. 3;  —  zugleich  zu  1  a):  y3 af>m  staoiti  hs  mqm  staetti  yim  aAurtm mazdqm  H. /.  3;?. /jj  —  ax^m  dalqm  .. tis'tnm  . .  av3ni?m  . .  ya%a  mqmcij  yim aAunm  masdqm  Yt  8.  50.  2)  AbL; b)  nur  u)  im  j  Aw.j  mana  als  AbL;  zu  2) :  at^B mana  yat  zardhusträi  V.2.r.  3)  Dat.; Bi)  imgAw.j  ei)«a/4)'a'';zu  i  a):  ääidi .. vikaspai  is^m  maibyäcä  Y.2Ä7;  8,  4g.%;
19592:•  j.  iiiaSav  n.  '(Wein  uzw.)  Beerenwein'  '* : gqm^a  ..yaom?a  . .  ''iula  ansptm  V.5. 52; 53>  54iF.  7/;    —    duye  navaiti  narqm  .
19698:•  j.  matp^rasav-  Adj.  (fem.  'svf-)  'mit den  Fragen  *'  versehen,  sammt  den  Fragen' : yasmm  . .  haptarahaittm  . .  'sUm  Vr.  id.  o; —  gähqm  ahunavaitim  ..  'svTm  Vr.  z^.  i.
=== BRT nard
4425:•  j.  an-ä'p«rafta-  Adj.  'was  (auch  durch Leibesstrafen)  nicht  ausgeglichen,  gesühnt werden  kann':  aya  °i<i  (APd.)  syaoina nard.vaipaya  V.  /.  1 1 ;  12,  16;  —  *spayäli
6074:ys. .  mazdayasnö  aojanö  'sähe  raima  (sd.)  \  13.  42,  Y.  68.  7,  14-  48;  —  a^al  nS  vacö jlsti^amnS  "V .  8.  y, —  uxltie  (sd.)  xraiwe  .  ,  *sixsaimca  (sd.)  .  .  °jvW  haäz  yat vTdrvanahe  °sät  'V.4-AS',  — yaüra  nard  vahiHät  Y.iff.ii.  LS.  'Saya  als  Adv, asavatts  'um  h^tüi  zrazdatsma  (sd.)  YL  j  sbes.  II)  '(dem  heiligen  Recht  ent- y-  'S;  —  tha  5%ravanS  .  .  ma/iyetiU  sprechtnics,  ^/«mässigesj  rechtes,  recht- vanh^s  'sähe  Yt7j.  147;  —  vahistmi  schafTenes  Tun,  Gerechtigkeit,  Recht- °i3m  yatamaide  Vr.  2g.  i ;  —  ySi  'iäi  schaffenhcit';  auch  in  kollekt  Sinn  'alles vaonarp  (sd.)  Y.  26.  4,  S;**  —  yö  yaomwas  einer  recht  tut,  bona  opera'.  i)  im iärayeiti  hs  'hm  iarayeiti  [sA.)  V._J,  31;  ■  gAw.:     huää    (sd.)    'Sim    vohucä    manä
7899:yeie  dus:^arm3:  nSit  imat  .  .  mihr/f  vat- naili  Ytio.105;  —  aeü/a  (sd.)  ti  sävan .  .  framrava  .  .  °5«  tl  zävan  .  .  fra- ifiraomi {sd.)  YLJj.r-ig;  —  "äil  mainya matnanäitl  Y.  j_y.  4;  4';  —  °äa  ät  yaza- maide  ahurtm  Y.jj.i;  39-1;  —  ät  '%ä yazamaidi  .  .  Y.  jtj?.3;  —  °äa  f  hai^ya (sd.)  nard  d^ä  jjnayö  Y.5^.6;  ■ —  Aaca ..pairi.sa^äiti  °äa  *aiwi.game  Hat  hama.. "sie  dauert  von  . .  bis  ,  .;  so  im  Winter; aber   im   Sommer  .  ."   N. 4Ö;  47,  ^SO^"^;
12401:Pron.  I.  Pers.  'du'.  Es  tritt  auf  i)  wenn auf  dem  Subjekt  ein  besonderer  Nach- druck liegtj  a)  bei  Gegenüberstellung:  Of alsqm  asH  anhuca  ratuscal  .  .  urvatat- nard  sara%mtra  tuntca  yS  larakustrS^. 2.43^*;  —  yt  '*"»  {'^u  4  b  ß)  ainim avasnsis  .  .  3at  tum  nisAttsis  .  .  H.  2,
18675:elliptisch  sva,  'ein  Mann  und  ein  Weib,  ein Menschenpaar"**:  dvaübya  haca  n)r>bya dva  nara  us^ayein/e (sd.)  t//i^wa/ia  s/ri^a nairyas^a  V.2.41.  2) '•  praegn. 'wehr- hafter Mann,  Kriegsmann;  kriegerischer Held':  narSi  ßrasaoifträi  Y.  28.  8;  — katna  (sd.)  syävarsänai  zurSjatahe  na- rahe''*  Yt*j.  18;  — pqsnus  narJ  (NS.)'^ HryS  taxmS  Aog.  84;  — y^i  narS  taxma ptntmU  Yt./J  27;  —  t! nard paiti.sanmti ySkva  v3r3%ra.l'aohl!  {sd.)  YtJ_j.  46;  — yat  mS  slärS  .  .  AacÜnte  (sd.)  n?r>byS ä^annff  *bax/3nia  Yt- 8.  1 ;  5.11,  77.6,7; das/a  narqm  *pouru.tät?m  stäkyanqm.. vanatqm  avammnanqm  Ny. J.  10;  —  hva- iai  naire  barumnäi  Y.  65.  4;  — yä  na- qm  vjg3r>pla{sd.yit . .  baoxtär^m  dahäi/i Vr.7,3;  Yt  10.12;  —  ya^a  hazannm Oim  narftn  adar.taySi^  Yt.  8.  $$; I.  19*;  —  a%ra  narqtn  mihrS.drujqtn apq/{sd.)  gavB  dar>tayeiti  Yt70. 48;  — narqm  asätanqm  frasS.car^'hrqm  saosyan- tqm  Y.  24.  5,  Yt.  13. 17.  a)  als  Bezeich- nung für  den  zweiten  Stand  (s.  'piflra-) 'Krieger,  Ritter***:  kada  .  .  mquarfi/ (sd.) rS  vis3nliY.48.  10;  — daidx atturai (AP.)  ,  .  asaunS  .  .  aidyüi  väsliyJng  ,  . ahmaibyä  ahma.rafonarahs  {^d^  Y.40.3; %wqm  ttarakl  ysi  taxma  Jathyintt äsu.aspim  .  .  %wqm  a^ravanS  .  .  mastim Yt5.  86.  3)''  ohne  Betonung  des  Ge- schlechts sva.  Mensch;  Person';  1)  im Gegensatz  zum  Tier;  uzw.  zu  a)  pasav-: ahe  nmanaßie pasvqmca  narqntla  Y.^-S; pasBm  .  .  nanm  ra?syät  V,  13.  32 b)  'span-.  . .  ahe  nmanake  spä  vä na  va  irihyat  V.5, 39;  8. 1,  4;  —  yat ahmi  spänasca  narasca  para.irüinti  V. 6.1; — y!i  pa^a  uebarmte  (^)  spänasca irista  iiarawca  (NF.)"  irisia  V.  Ä  14; 3.  32;  —  yat  ,  .  sairi  riiianie  spänasca irista  naraila  (AP.)'*  irista  V.  3.  8; 36.  c)   ^av-:  janyäi  *n>rSuI^'*  para
```


## [2026-09-07T19:33:20.451Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT\"; grep -n \"navama\" KNT.txt | head -10; echo \"=== SYN nine\"; grep -n -o \".\\{80\\}13\\.15.\\{0,300\\}\" SYN.txt | head -5; echo \"=== IEC newn\"; grep -n \"neun\\b\\|néwn\\|neuen\" IEC.txt | head -10"
}
```


### [2026-09-07T19:33:21.883Z] TOOL RESULT

```
=== KNT
2364:IV. Nine: nsm. navama ‘ninth’ is identical with Skt. navamá-s, and is formed from the ordinal pIE *neyn, Skt. ndva, in imitation of "debemos to *dekm, cf. Skt. daSamd-s to dasa, Lt. decimus to decem. The - in ‘nine’ is seen in the Lt. ordinal nonus, from *nouenos.
2955:With an adverbial expression the present may, as in other languages, indicate time begun in the past and extending into the present, and the im- perfect stmilarly may express time begun їп a re- moter past and extending into a nearer past; the best examples are in DB 1.7 hacd paruviyata ётйй amahy һас paruniyata hya améxam taumā a Sdyahiyd cha ‘from long ago we are (= have been) noble, from long ago our family was (= had been) royal (or kings)’, and 9-11 VIII manā tawmaya tyaiy paruvam xsdyahiyd cha adam navama IX duviláparanam xsdyahiya amahy ‘8 of my family (there were) who were (= had been) kings; I (am) the ninth; 9 in succession we are (= have been) kings’.
3149:0816. Sryzistic Omissions occur in OP, es- pecially of the copula when there is a predicate adjective or phrase; cf. §275, §276. Examples: DB Lf Cišpäãiš pita (sc. cha) Hazàmanis; 1.9 VIII mand іаитӣуӣ (ве. dha") tyaty . . .; 1.10 adam (sc. amiy) navama; 1.13 ima (se. ha*tiy) dahydva tyaty ‚..} 1.15 tyaty drayahyá (ве. ha*tiy; or possibly daraya"tiy, сї. XPh 23f); 1.27 ima (sc. astiy) tya mand kartam (se. astty).
3469:10 : xSayafiyaé : dha : adam : navama : IX : duvitiparanam : vayam : хёйуай
5603:navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
=== SYN nine
22441:er, which are partly expressed by the same terms but partly differentiated, see 13.15, 13.17.
23395:from jut ‘op, since they are obvious {he discus ’ nonates of the words for gar (13.15) or ‘great, large iguchy i060). ar equivalents to ( 0 ne Am ia are NE amount, fr. vb. oe ie _ ‘mount’ (fr. OFr. amonter, u! vane i nd monte), hence ‘rise 1n quantity * aber’ (similarly Fr. montant, etc.) ; Lp amount’? (> Fr. at. st mme, N ; ie of summus ���highest’. 1, Grk. xoodrns (Aristot.), fr.
23565:us but plis). Most of these have been included in the discussion of the latter (13.15), leaving only the following for notice here.
23616:hSl. malo, etc. (advs. with gen.; Boh. mdlo indecl. but used like mnoho ‘much’, 13.15) : ChSl. mali, etc. ‘small’ (12.56).
23671:e words for ‘multi- jude! are derivs. of, or cognate with, tho for ‘much, many (13.15). Some of these are formally of learned origin and not frequent in common speech, e.g. Sp. mullitud vs. muchedumbre, or Fr., NE multitude vs. foule, crowd.
=== IEC newn
3611:enneun (enneunti) ‘nine’. WP I, 128. Cf. neun Skt. náva, návan; Av. nava; Per. nuh; Kurd. n0; Oss. cf. náw- (cpds.); Tokh. AB fiu; Arm. inn, gs onni; ino; Myc. enewo; Cypr. enna; Gk. ennéa beside einás /ninesome'; Alb. nánd$é, ndåndë, T nëntë, nëndë; OLat. neuen, beside neuna ‘nonae’; Lat. novem; Umb. cf. nuvis ‘novies’; MIr. nói; Ir. naoi, beside naomhoadh ‘ninth’; Br. nað, nav; W. Cor. naw; Go. OHG niun; OS nigun; OE nigon; ON niu, beside níund *ninesome'; OPr. new- ints (nine? or (ninth). Cf. OCS deveti (and com. Sl.); Li. devyni; Latv. devini (influence of dem, q.v. The Slav forms derive from noun-type in *-tis)
11716:(neuomos ‘ninth’. Cf. neun Skt. navamab; Ober, navama-; elsewhere inhi- bited by homonymic clash with the superla- tive of type *neuos. Cf. Ir. naomhadh *ninth")
11727:neun (en-neun, -neum) ‘nine’ Skt. nava; Av. nava, id. beside naums (ninth: Ir. naomhadh, id.); Per. nuh; Gk. cf. ennéa, Myc. enewo, id.; Lat. novem (infl. of decem for final cons.); Olr. nó, Ir. naoi; W naw, Br. nað, nàv; Go. MHG niun; OE nigon; Du. negen; Fris. njuggen, njoggen, id.
11732:neun (en-neun, -neum) — nik-
```


## [2026-09-07T19:33:52.335Z] TOOL CALL #30: Bash

```json
{
 "command": "pdftoppm -f 363 -l 363 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg363 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


## [2026-09-07T19:33:52.699Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && ls; grep -n \"نالیدن\" FFD_pages.txt | head -20"
}
```


### [2026-09-07T19:33:54.422Z] TOOL RESULT

```
total 30712
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 15:33 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1297 Sep  7 15:29 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


### [2026-09-07T19:33:54.466Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
2095:ریش 13200 به معنی «نالیدن» است.
2101:نالیدن
2429:8 (ريشة بالانده -ء 5ق) ۳ ۶۸ 0 (ريشه < نالیدن) ۰۱/۷
```


## [2026-09-07T19:34:01.153Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && sed -n '2080,2110p' FFD_pages.txt; echo ===; awk 'NR>=2060 && NR<=2105 && /pdf page/' FFD_pages.txt; echo === ; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['FFD'];print(d.get('page_offset'),'|',d.get('lookup_hint','')[:300],'|',d.get('notes','')[:400])\""
}
```


### [2026-09-07T19:34:02.373Z] TOOL RESULT

```
Exit code 1
مُرد < فارسی میانه ۵۶۵ < ایرانی باستان 13-1۵" برای 12 > آراست. 17
صورت ضعیف ريشةٌ 1387 به معنی «مردن» است.
میر < فارسی میانه 3۲۲ < ایرانی باستان 2دیط*. برای ساختن مادهٌ مضارع از
ریشه به کار می‌رفته است.
[pdf page 82]
ماده‌های ماضی و مضارع قارسی دزی شش ۷۷
مشت.
مُشت + فارسی میانه 151 + ایرانی باستان 1۹-1۵*. برای ۵ > آراست. 177
صورت.اصلی ۲5 است» 2 پیش از ۲ به 5 بدل شده است. 172 صورت ضعیف ريشهةٌ
2 به معنی «مالیدن» است.
مال + فارسی میانه 721 + فارسی باستان 1۵۳4-8* < ایرانی باستان 1۵72-۵*. برای
3 > آرای.
موییدن
«مویید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
موی < فارسی میانه 136 < ایرانی باستان 1۳۵-2*. برای 2 آرای.
ریش 13200 به معنی «نالیدن» است.
نازیدن
«تازید» مادهٌ ماضی جعلی است. از مادةٌ مضارع ساخته شده است.
ناز ج فارسی میانه 232 + ایرانی باستان ۸32*. 232 در ایرانی باستان اسم است به
معنی «شادی»» «افتخار». 132 در فارسی میانه «شاد بودن» «مفتخر بودن» معنی
می‌دهد.
نالیدن
«نالید» ماده ماضی جعلی است. از ماده مضارع ساخته شده است.
نال ج فارسی میانه 281 < ایرانی باستان 8۵۲۵-۵*. برای 2 آرای. ريشةٌ 1874 به ۱
معنی «بانگ کردن» است.
نشاست < فارسی میانه 213391 < ایرانی باستان 339-۵-زم"
[pdf page 83]
۸ فعلهای فارسی دری
برای 1۵ -> آراست. 11 پیشوند فعلی است. ۸34 که صورت بالاندةٌ ريش 144 است.
صورت اصلی 538 است. 1 پس از آبه 5 بدل و 4 پیش از 1 به 8 بدل شده است.
تشان <ج فارسی میانه 81530. 8827 که در فارسی میانهٌ ترفانی مادةٌ مضارع 215291
(eval):1: == not found
```


## [2026-09-07T19:34:18.474Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 82 -l 82 -r 200 -png -singlefile /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf ffd77 && python3 -c \"\nfrom PIL import Image\nim=Image.open('ffd77.png'); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.55),w,int(h*0.95))).save('ffd77_bot.png')\n\""
}
```


### [2026-09-07T19:34:20.303Z] TOOL RESULT

```
(1136, 1705)
```


## [2026-09-07T19:34:22.953Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd77_bot.png"
}
```


### [2026-09-07T19:34:22.968Z] TOOL RESULT

```

```


## [2026-09-07T19:34:32.257Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg363.png'); print(im.size)\nw,h=im.size\nim.crop((0,0,w,int(h*0.42))).resize((int(w*1.2),int(h*0.42*1.2))).save('p363_top.png')\nim.crop((0,int(h*0.38),w,int(h*0.80))).resize((int(w*1.2),int(h*0.42*1.2))).save('p363_mid.png')\n\""
}
```


### [2026-09-07T19:34:34.430Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-07T19:34:37.246Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p363_top.png"
}
```


### [2026-09-07T19:34:37.702Z] TOOL RESULT

```

```


## [2026-09-07T19:34:37.699Z] INPUT

[Image: original 3060x1663, displayed at 2000x1087. Multiply coordinates by 1.53 to map to original image.]


## [2026-09-07T19:34:42.382Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p363_mid.png"
}
```


### [2026-09-07T19:34:42.736Z] TOOL RESULT

```

```


## [2026-09-07T19:34:42.723Z] INPUT

[Image: original 3060x1663, displayed at 2000x1087. Multiply coordinates by 1.53 to map to original image.]


## [2026-09-07T19:35:09.455Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 neu (navate nauti)\"; grep -n \"nūntium\\|nuntium\\|navate, nauti\\|nauti \" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== WLD Bd1 neun\"; grep -n \"e-neuen\\|neuen, neun\\|neun'\\|newn\" incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-07T19:35:09.522Z] TOOL RESULT

```
=== WLD Bd2 neu (navate nauti)
=== WLD Bd1 neun
11548:128                                eneuen, neun, enug            — enek-, nek-, enk-, nk-
11556:eneuen, neun, ennn „neun“.
```


## [2026-09-07T19:35:11.123Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW nuntius\"; grep -n \"nuntius\\|nūntius\" LEW_1910.txt | head -8; echo \"=== LAT nuntius\"; grep -n \"nuntius\\|nūntius\" LAT.txt | head -8; echo \"=== LAT novem\"; grep -n -o \".\\{0,80\\}novem.\\{0,300\\}\" LAT.txt | head -6"
}
```


### [2026-09-07T19:35:14.593Z] TOOL RESULT

```
=== LEW nuntius
=== LAT nuntius
42451:nuntius
42469:nuntius (forme ancienne nountios d'aprbs Mar. Victor. GLK VI 13,
42474:sert a la fois d'adjectif, nuntius,-a,-um " annonciateur", et de sub-
42475:stantif: nUntius,-i m. "messager" et "message", nuntius et res ipsa
42477:sage", d'aprbs Servius, Ae. n,8y6, nuntius est qui nuntiat, nuntium
42485:spectionem et Fest.444,16. Cf. encore Mercurius, nuntius Iouis. Dans
42486:la langue du droit public, le nuntius est celui qui est charge de
42489:miserat, nisi legatorum nuntio paruisset ; dans le droit civil, nuntius
=== LAT novem
ugrep: error: error at position 82
f][\x80-\xbf]*){0,300}
                      \___exceeds complexity limits
```


## [2026-09-07T19:35:17.848Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11548,11600p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-07T19:35:17.899Z] TOOL RESULT

```
128                                eneuen, neun, enug            — enek-, nek-, enk-, nk-

mit       lat.    sine usw. (vgl. Yf. LEWb. s. v.)                          mag bestehen, docb keineswegs
sicber (Prellwitz 40).
        Ygl. Boisacq      6 f., Prellwitz 40, Horton Smith BB. 22,
                                   1                                                                  189ff.            Auch
Prellwitz           BB. 22, 78, Vf. LEWb. 2 715, Fick III * 25.

eneuen, neun, ennn „neun“.
  Ai. nova, av. nara „9“: arm. inn „9“               pi. in(n)unH (Hiibsch-

mann Arm. St. I 31, Arm. Gr. I 450f.), gr. *evj:a- in hom. elva-exeg -vv%eg.                                      ,


boot. sva-yg-dey.dxg,                        jon. slva-y.oaioi ,     att.   iva-y.ooioi,       ord. eivaxog   ,
                                                                                                                      att. aol.

e'vaxog, woneben noch nicht geklartes errefpja, und wohl h’fsv- in evev-
•gy.ovxa (Lit. zu don gr. Formen bei Boisacq 252, 254 f., 1109); alb. nsnde
„9“ (* neunti „Anzahl von neun“, wie si. dcvqtb „9“, anord. niund „Yeun-
zahl“ und ai. navatl-, av. navaiti- f. „90“, eigentbch Neunzahl von Zehnern;
G. Meyer Alb. St. II 66f., Alb. Wb. 304); lat. novem „9“ (-m lautgesetzlich
aus -n ? sonst nach septem, decern)-, air. noi n-, cymr. corn, naw, bret. nao
(zum a s. Pokorny IF. 38, 190f ); got. ahd. niun, anord. nio „9“, as. nigun,
                             (zum g dieser und der Ordinalia s. die Lit. bei
afries. ni(ti)gtm. ags. nit,on
Brugmann II 2 2, 20);                lett. devini («- noch im Ordinale apr.
                                               lit.   devyn\,
ilewTnts), aksl. dev eh „9“ (d- wohl durch Diss. gegen das ausl. n und durch
EinfluB der 10 festgeworden. Lit. bei Berneker 189).
    Ordinale; *noueno- in lat. nontts mit nach der 7 und 10 eingefiihrtem
                                                                 ,


in statt n umbr. niivime „nonum“, ai. navamd -, av. naoinci-; ap. navama -,

air. nomad cymr. nawfed (um -to- erweitert); -A)-Bildung gr. el'varog, evaxog
                     ,


               got. niunda, ahd. niunlo, anord. nionde     as. nigundo nigudo,
    :




( *enim-to -),                                                                             ,                      ,

afries. niugunda, ags. niyjda (s. o.), lit. devintas, apr. neivlnts, aksl. devqfo.
    Man vermutet Zusammenliang mit *neuo- „neu“, weil mit 9 ein neuer
 Ziihlabschnitt              begonnen habe, indem                      die    Dualform von *oktou „S“ auf
    eine Yiererreclinung                      weise.    — Ygl. Curtius          5
                                                                                    310,       Brugmann       II 2       2,   20
```


## [2026-09-07T19:35:18.216Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '42469,42520p' LAT.txt"
}
```


### [2026-09-07T19:35:18.280Z] TOOL RESULT

```
nuntius (forme ancienne nountios d'aprbs Mar. Victor. GLK VI 13,
18; on trouve aussi nontiata CIL 1 9 586, cf .noundinun et nondinun’,
quant au nouentium que Suecheler substitue au mouentium du manuscrit
dans le Carmen Cn. Marci uatis cit^ par Festus 163,6: quamuis mouentium
duonum negumate, il n'a que la valeur d'une conjecture): mot qui
sert a la fois d'adjectif, nuntius,-a,-um " annonciateur", et de sub-
stantif: nUntius,-i m. "messager" et "message", nuntius et res ipsa
et persona dicitur , P.F.179,1; nuntia f. "messagbre"; nUntium n. "mes¬
sage", d'aprbs Servius, Ae. n,8y6, nuntius est qui nuntiat, nuntium
quod nuntiatur ; toutefois nuntium dans ce sens n'est que l'adj. accom-
pagnant un nom neutre. L'emploi comme adjectif est le plus rare;
du reste dans les cas ou le mot est en apposition, la valeur precise
en est souvent indiscernable.
Terme de la 1 . religieuse et officielle, et specialement de la 1 .
augurale: nuntia auis, nuntia fibra ; nuntiatio est oppose a spectio ,
Cic., Phil.3,33,81, non nuntiationem solum habemus, consules etiam
spectionem et Fest.444,16. Cf. encore Mercurius, nuntius Iouis. Dans
la langue du droit public, le nuntius est celui qui est charge de
faire connaitre une d 4 cision de caractere public, ou la proclamation
elle-meme, cf. Cic., Fam.13,34,3, quos senatus ad denuntiandum betlum
miserat, nisi legatorum nuntio paruisset ; dans le droit civil, nuntius
designe specialement la "lettre de divorce": nuntium uxori (re)mittere.
Ce sens technique se retrouve dans les composes denuntio, obnuntio,
renuntio. - Ancien (Naev.), usuel et classique. Formes romanes en
partie de caractere savant, M.L.5997.
Derivas et composes: nuntio, -as (et nontio, cf. nontiata CIL I 3 5^6);
nuntiatio (t. relig. et jurid.): annonce des auspices; declaration
au fise; nuntiator,-trix (l. eccles. et Dig.); adnuntio (epoq.imp.):
annoncer. Tros frequent dans la 1 . eccl£s. pour praenuntio) de la
adnuntiator, -tid, traduisant ay^eXXoo et ses composes; denuntio (l.
du droit et du rituel): declarer solennellement, faire connaitre
par message (d. bellum ); presager; citer en temoignage. Dans la 1 .
commune: annoncer, declarer (d 1 apros declamo, declaro), denuntiatio
- delStio, Suet.Aug.66; denuntiator "policier" (epoq.imp.); enuntio:
faire connaitre au dehors, denoncer. Dans la 1 . de la gramm. et de
la rhetor, ^exprimer, enoncer"; enuntiatluus = oatocfavTixoc, anuyyeX-
Tixoc; inenuntiabilis (Cens.); internuntio (T.L.); internUntius :interprete, interm<?diaire; obnuntid: -are proprie dicuntur augures
qui aliquid mali ominis saeuumque uiderint, Pon.Ter. Ad.547; "apporter
une mauvaise nouvelle" et "a'oppoaer i"; praenuntia prodire; prae¬
nuntius ; prdnUntid: annoncer publiquement) d'ou a haute voix, rendre
une sentence, se prononcer; declarer; prononcer (t. de logique);
renUntid (= aTtayyeXXw) : i° annoncer en rdponse; proclamer le resultat
d'une dlection, et renuntius, -tidtor, -tio} a° (avec re- dans le sens
de "rejeter, refuser"): annoncer le retrait de, r^voquer, reprendre,
et "renoncer a", d'ou dans la 1. de l'Egl. abrenUntid,-tidtiS (cf*
abrelictus Tert.).
On ne peut preciser le rapport avec nouus autrement que par des
hypotheses incertaines.
. nu 5 , -ls, -ere: faire un signe de fete. Le verbe simple ne semble
pas atteste en dehors des gloses nuo , veuu) CGL II 375 ,G5, nuit, pro¬
misit, nutum dedit IV 369,30. II a peut-etre disparu par suite de
son liomonymie avec un verbe *nuere (<?galement disparu) suppos^ par
```


## [2026-09-07T19:35:34.601Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^323 \\|^ *323  *neu\" incoming/WLD/WLD_Bd2_pages.txt | head; grep -n \"nauti\\|navate\" incoming/WLD/WLD_Bd2_pages.txt | head"
}
```


### [2026-09-07T19:35:34.697Z] TOOL RESULT

```
21350:      navate, nanti „tont, jubelt, preist"', ah. nuaU n. „Schrei, Larm“,
46022:  ai. snauti^ Ptc. snutd- „triefen, eine Flussigkeit des Korpers, besonders
46049:(s. Yf. LEWb,^ 8. V. und zur Bed. oben ai. snauti).
```


## [2026-09-07T19:35:37.622Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21340,21365p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-07T19:35:37.667Z] TOOL RESULT

```
av. naddnto            an. Xey.                (s. Bartholomae Airan. Wb.
                                   j^schmahende, lasternde^^
1038,        und      *0720-   „6Vo/2ar‘)   und
                                        sekundar mit nid- usw. zsgeflossen
                                                  erst
(Giintert IF. 30, 86f.) (Boisaeq 705 Anm. 1 erwagt mit Unrecht auch fiir
av. naddnto eine Lesung nindonto oder nkhnto).


1.    neu- „rufen, preisen“.
      navate, nanti „tont, jubelt, preist"', ah. nuaU n. „Schrei, Larm“,
      Ai.
nuahha „clamosas“. Pick II ^ 195.
  Aber lett. 7'ianju, naid „miauen^‘ (Pick I^ 98, 503) ist eine Schallnach-
ahmung ohne Geschichte; ahd. (^fotker) niumo „sonor, modulation (ibd.)
ist    ds,   aus kirchenlat. neuma.


2. neu- „einen kurzen Buck machen oder StoB gebenn, bes. (europ.) ,,nicken,
        winken^.
              7iaiiti „wendet sich, kehrt sich^j 7idvayati „wendet, kehrtn,
     Ai. ndvaio,
als (f-Praes.wohl nuddti „stoBt fort, riickt^ (andere Deutungen s. u. nan-
,,Todn; liber lit. pa^iustu „gelu8ten s. u. netidJi- „begehren“, von dem es
ganz fraglich ist, ob es als „woraufzu einen Ruck machen^ Erw, unsere
Wz. ist);
```


## [2026-09-07T19:35:43.012Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T19:35:43.020Z] TOOL RESULT

```


```


## [2026-09-07T19:35:47.864Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%84%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology section for نالیدن verbatim (Middle Persian form, Proto-Iranian root, cognates, references cited)."
}
```


## [2026-09-07T19:35:49.039Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/nuntius",
 "prompt": "Give the Latin etymology of nuntius verbatim, including any reconstruction (*noventios / *nowe-ntios), whether it is derived from novus or from a root *neu- 'to shout', and which authorities (de Vaan, Pokorny) are cited. Also note nuntium."
}
```


### [2026-09-07T19:35:49.290Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T19:35:55.056Z] TOOL RESULT

```
# Latin Etymology of *nuntius*

The etymology remains uncertain with competing hypotheses:

**Proto-Indo-European origin (*newH-):**
"From Proto-Indo-European *newH- ('to cry'), whence Sanskrit nu ('to sound out, praise'), Old Irish núall ('a loud noise')" — tentatively favored by De Vaan.

**Contraction theory (*noventius):**
"Contracted from *noventius, from an obsolete *noveō, from *novus, though this is rejected by De Vaan due to the hypothetical proto-form *no(wo)wentio- not making sense morphologically."

**Alternative PIE root (*new-):**
"From Proto-Indo-European *new- ('to nod'), same source as Latin *nuō, Ancient Greek neúō ('to beckon, nod')" and Old Irish *noid* ('make known').

**Etruscan possibility:**
Possibly "from Etruscan nunth ('to bring')."

The document also references *nuntium* as a related term without elaboration. De Vaan is cited as the primary etymological authority consulted here.
```


## [2026-09-07T19:36:00.974Z] TOOL CALL #47: WebSearch

```json
{
 "query": "wiktionary نالیدن Persian etymology Middle Persian nālīdan Proto-Iranian *nard"
}
```


## [2026-09-07T19:36:02.527Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%87#Persian",
 "prompt": "Give the Persian etymology of نه (noh) 'nine' verbatim: Middle Persian form, Proto-Iranian, Proto-Indo-European, and any note about the final -h."
}
```


### [2026-09-07T19:36:07.189Z] TOOL RESULT

```
# Persian Etymology of نه (noh) 'Nine'

Based on the Wiktionary entry, here is the etymological chain:

**Middle Persian:** "nwk' /⁠nōg⁠/" (native script not provided in the source)

**Proto-Iranian:** "*Hnáwa"

**Proto-Indo-European:** "*h₁néwn̥"

**Note on the final -h:** The entry does not explicitly explain the etymology or function of the final -h in the modern Persian form. The source simply presents "نه (nuh / noh)" as the contemporary numeral without commentary distinguishing how the Middle Persian form evolved into the current spelling with the -h diacritic.

The cognate relationship to English "nine" is noted, suggesting a shared Indo-European origin.
```


### [2026-09-07T19:36:07.517Z] TOOL RESULT

```
Web search results for query: "wiktionary نالیدن Persian etymology Middle Persian nālīdan Proto-Iranian *nard"

Links: [{"title":"نرد - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%86%D8%B1%D8%AF"},{"title":"پریدن - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C%D8%AF%D9%86"},{"title":"ناهید - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%87%DB%8C%D8%AF"},{"title":"ناله - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%84%D9%87"},{"title":"Iran - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Iran"},{"title":"نالان - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%84%D8%A7%D9%86"},{"title":"ـه - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%80%D9%87"},{"title":"Nazanin","url":"https://en.wikipedia.org/wiki/Nazanin"},{"title":"Etymological Dictionary of the Iranian Verb","url":"https://www.parsianjoman.org/wp-content/uploads/2016/04/Etymological-Dictionary-of-the-Iranian-Verb.pdf"},{"title":"A concise review of the Iranian calendar","url":"https://arxiv.org/pdf/astro-ph/0409620"}]

Based on the search results, I found relevant information about the Persian verb نالیدن (nâlidan):

The verb نالیدن (nâlidan) means "to groan, to moan", and it appears in related forms like نالان (nâlân, "groaning, moaning") and نالش (nâleš, "groaning, lamentation").

Regarding the etymology you mentioned, the search results reference Proto-Iranian *nard meaning "to lament, moan", which aligns with the semantic field of the Persian نالیدن. This suggests a connection between the modern Persian verb and the Proto-Iranian root you referenced.

However, the search results don't provide the complete etymological chain from Middle Persian nālīdan through Proto-Iranian *nard that you're looking for. The results do confirm the existence of this Proto-Iranian root and its meaning, but a more detailed Wiktionary entry on نالیدن itself would be needed for the full etymology you're searching for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T19:36:14.314Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%84%D9%87",
 "prompt": "Give the Persian etymology of ناله (nāle) verbatim — the verb نالیدن, Middle Persian form, Proto-Iranian root, cognates and any references cited."
}
```


## [2026-09-07T19:36:17.082Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81n%C3%A9wn%CC%A5",
 "prompt": "Give the PIE reconstruction *h₁néwn̥ 'nine' verbatim: meaning, descendants in Proto-Indo-Iranian/Proto-Iranian (Avestan nauua, Old Persian), Latin novem, Proto-Germanic *newun, and any note connecting it to *néwos 'new'."
}
```


### [2026-09-07T19:36:18.821Z] TOOL RESULT

```
# Persian Etymology of ناله (nāle)

Based on the Wiktionary content provided, I cannot give you the information you've requested. The page explicitly states:

"(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

The document does not contain:
- The Middle Persian form
- Proto-Iranian root information
- Cognates from other languages
- Academic references for etymological claims

The page only lists related terms like نالیدن (nālidan, "to groan, to moan") and descendants in Azerbaijani and Turkish, but offers no etymological analysis or historical linguistic documentation.
```


### [2026-09-07T19:36:22.333Z] TOOL RESULT

```
# PIE *h₁néwn̥ 'Nine'

**Meaning:** The numeral nine in Proto-Indo-European.

**Key Descendants:**
- Proto-Indo-Iranian: *Hnáwa (leading to Avestan and Old Persian forms)
- Latin: novem
- Proto-Germanic: *newun

**Connection to *néwos 'new':**

According to one theory presented, "related to the PIE adjective *néwos ('new'), allegedly an endingless locative meaning 'in the new'" with potential reinforcement from the preposition *en ('in'). However, the page notes this etymology faces challenges, as "prothetic vowels in Greek and Armenian are today usually explained as reflexes of word-initial laryngeal #h₁-."

An alternative proposal suggests *h₁néwn̥ represents the accusative of an older noun *h₁enu- ('lack'), connecting instead to *h₁new ('without'), which appears in forms like Ancient Greek áneu and German ohne.
```


## [2026-09-07T19:36:31.461Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN announce\"; grep -n -o \"announce, tr\\..\\{0,400\\}\" KLN_1966.txt | head -3; echo \"=== KLN nine\"; grep -n -o \"nine, adj\\..\\{0,400\\}\" KLN_1966.txt | head -3; echo \"=== KLN noon\"; grep -n -o \"noon, n\\..\\{0,400\\}\" KLN_1966.txt | head -3; echo \"=== KLN November\"; grep -n -o \"November, n\\..\\{0,400\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-07T19:36:32.841Z] TOOL RESULT

```
=== KLN announce
=== KLN nine
=== KLN noon
=== KLN November
```


## [2026-09-07T19:36:36.727Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"announce\" \"nona hora\" \"novem\" \"nigon\"; do echo \"===== $w\"; grep -n -m3 -o \".\\{0,120\\}$w.\\{0,300\\}\" KLN_1966.txt | head -3; done"
}
```


### [2026-09-07T19:36:47.962Z] TOOL RESULT

```
===== announce
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,300}
                          \___exceeds complexity limits


===== nona hora
ugrep: error: error at position 87
0-\xbf][\x80-\xbf]*){0,300}
                           \___exceeds complexity limits


===== novem
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,300}
                       \___exceeds complexity limits


===== nigon
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,300}
                       \___exceeds complexity limits
```


## [2026-09-07T19:36:52.179Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'announce', r'nona hora', r'\\bnigon\\b', r'November']:\n    ms=list(re.finditer(pat,t))\n    print('=====',pat,len(ms))\n    for m in ms[:3]:\n        print(repr(t[max(0,m.start()-250):m.start()+350].replace('\\n',' ')))\n        print('---')\nEOF"
}
```


### [2026-09-07T19:36:53.877Z] TOOL RESULT

```
===== announce 43
'adj. annotation,  n.  —  L.  annotdtio,  gen.  -dnis,  fr.  an- notatus,  pp.  of  annotare.  See  prec.  word  and -ion  and  cp.  connotation, annotator,  n.  —  L.,  fr.  annotatus,  pp.  of  anno- tare.  See  annotate  and  agential  suff.  -or. announce,  tr.  v.  —  ME.  anounce,  fr.  OF.  anoncer (F.  annoncer),  fr.  L.  annuntiare,  ‘to  announce, relate’,  fr.  ad-  and  nuntiare,  ‘to  relate,  report’, fr.  nuntius,  ‘messenger’.  See  nuncio  and  cp. annunciate. Derivatives:  announce-ment,  n.,  announc-er,  n. annoy,  n.  —  ME.  anoi,  anui,  fr.  OF.  enui  (F.  en¬ nui),  ‘'
---
'rec.  word  and -ion  and  cp.  connotation, annotator,  n.  —  L.,  fr.  annotatus,  pp.  of  anno- tare.  See  annotate  and  agential  suff.  -or. announce,  tr.  v.  —  ME.  anounce,  fr.  OF.  anoncer (F.  annoncer),  fr.  L.  annuntiare,  ‘to  announce, relate’,  fr.  ad-  and  nuntiare,  ‘to  relate,  report’, fr.  nuntius,  ‘messenger’.  See  nuncio  and  cp. annunciate. Derivatives:  announce-ment,  n.,  announc-er,  n. annoy,  n.  —  ME.  anoi,  anui,  fr.  OF.  enui  (F.  en¬ nui),  ‘worry’,  back  formation  fr.  enuier,  ‘to worry,  vex,  annoy’.  See  annoy,  v. annoy,  tr.  v.  '
---
'or. announce,  tr.  v.  —  ME.  anounce,  fr.  OF.  anoncer (F.  annoncer),  fr.  L.  annuntiare,  ‘to  announce, relate’,  fr.  ad-  and  nuntiare,  ‘to  relate,  report’, fr.  nuntius,  ‘messenger’.  See  nuncio  and  cp. annunciate. Derivatives:  announce-ment,  n.,  announc-er,  n. annoy,  n.  —  ME.  anoi,  anui,  fr.  OF.  enui  (F.  en¬ nui),  ‘worry’,  back  formation  fr.  enuier,  ‘to worry,  vex,  annoy’.  See  annoy,  v. annoy,  tr.  v.  —  ME.  anuien,  fr.  OF.  anoier,  en- noier  (F.  ennuyer),  fr.  VL.  inodiare,  ‘to  hate’, fr.  L.  in  odio,  ‘in  hate,  in  aversion’.  Se'
---
===== nona hora 0
===== \bnigon\b 4
"stility', fr.  inimicus,  ‘enemy’.  See  enemy  and  -ity  and cp.  amity. ennea-,  combining  form  meaning  ‘nine'.  —  Fr. Gk.  ivvea,  ‘nine’,  which  stands  for  *b\\>irx, *4vfx-,  and  is  cogn.  with  OI.  ndva,  L.  novem. Goth,  niun,  OE.  nigon ,  ‘nine’.  See  nine  and  cp. words  there  referred  to.  Cp.  also  ennead. enneacontahedron,  n.,  a  polyhedron  with  ninety faces.  —  Compounded  of  Gk.  *evveoczovtx. ‘ninety’,  and  eSpa,  ‘side,  face’.  *’ Ewedbcovxa  is erroneously  formed  fr.  evvex,  ‘nine’;  the  correct form  is  evevr)>covxa.  See  ennea-  and  -hcdron. F"
---
'and  cp.  F.  Ninon,  Ni¬ nette,  which  are  diminutives  of  Anne,  ‘Ann’, nincompoop,  n.,  a  fool,  simpleton.  Prob.  an invented  word. Derivatives:  nincompoop-ery ,  n.,  nincompoop - istj  adj. nine,  adj.  —  ME.  nigen,  nine,  fr.  OE.  nigon,  nigan, rel.  to  OS.  nigun,  OFris.  niugun,  nigun,  ON .  niu, Dan.  ni,  Swed.  nio,  dial.  Norw.  nio,  nie,  MLG., Du.  negen,  OHG.,  MHG.  niun,  G.  neun,  Goth. niun,  ‘nine’,  and  cogn.  with  OI.  nava,  Avestic nava,  Toch.  hu,  Arm.  inn  (for  *envan),  Gk.  i\'J\'du. (for  *evve"x),  Alb.  mnde,  L.  novem  (for  *  no¬ yen'
---
'een,  adj.  —  ME.  nigentene,  nynetene,  fr.  OE. nigontiene,  nigontyne.  See  nine  and  -teen. Derivative:  nineteen,  n. nineteenth,  adj.  —  ME.  nyntenthe ,  formed  on analogy  of  fourth  by  adding  -th  to  nineteen.  The OE.  form  is  nigon-teoda. Derivative:  nineteenth,  n. ninetieth,  adj.  —  ME.  nyntithe,  formed  fr.  ninety with  numeral  suff.  -th. ninety,  adj.  —  ME.  nigenty,  nyneti,  fr.  OE.  nigon- tig.  See  nine  and  the  numeral  suff.  -ty. Derivative:  ninety,  n. ninny,  n.,  a  fool,  a  simpleton.  —  Fr.  a  ninny, corrupted  fr.  an  innocent  and  i'
---
===== November 12
', ryknQti,  ‘to  roar,  bellow’,  OE.  ryn  (for  *ruhjan), OHG.  rohon,  of  s.m. Derivatives:  bruit,  tr.  v.,  bruit-er,  n. Brumaire,  n.,  name  of  the  second  month  of  the French  revolutionary  calendar  (lasting  from October  23rd  to  November  21st).  —  F.,  lit.,  ‘the foggy  month’,  coined  by  Fabre  d’Fglantine  in 1793  fr.  brume,  ‘fog’,  fr.  L.  bruma.  See  brume and  -aire. brumal,  adj.,  pertaining  to  winter.  —  L.  brumalis, fr.  bruma,  ‘winter’.  See  brume  and  adj.  suff.  -al. brume,  n.,  mist,  fog.  —  F.,  ‘mist,  fog’,  fr.  L. bruma,  ‘winter’,  l'
---
',  a  ruffle.  —  Of  uncertain  origin. Derivatives:  frill,  tr.  and  intr.  v.,  frill-ed,  adj., frill-ery,  n.,  frill-ing,  n.,  frill-y,  adj. Frimaire,  n.,  name  of  the  3rd  month  of  the French  revolutionary  calendar  (lasting  from November  21st  to  December  20th).  —  F.,  lit. ‘the  month  of  frost’;  a  hybrid  coined  by  Fabre d’Eglantine  in  1793  from  F.frimas,  ‘frost,  hoar¬ frost’,  a  word  of  Teut.  origin,  and  F.  suff.  -aire (fr.  L.  -arius).  See  rime,  ‘hoarfrost’,  and  adj. suff.  -ary. fringe,  n.,  a  border  of  loose  threads.  —  ME. frenge,'
---
'godspellere,  ‘evang¬ elist’,  fr.  godspel.  See  gospel  and  agential  suff.  -er. gospodar,  n.  - —  See  hospodar. gossamer,  n.,  a  filmy  cobweb.  - —  ME.  gossomer, gosesomer,  lit.  goose  summer;  so  called  because it  appears  early  November,  at  the  time  when geese  are  in  season.  See  goose  and  summer. Derivatives :  gossamer-ed,  gossamer-y,  adjs. gossip,  n.,  1)  godparent  (obsol.  or  dial.)-,  2)  one given  to  idle  talk;  3)  idle  talk.  —  ME.  godsib, gossib,  fr.  OE.  godsibb,  ‘sponsor’,  fr.  god,  ‘God’, and  sibb,  ‘relationship’.  See  god  and  s'
---
```


## [2026-09-07T19:37:02.623Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'noon,\\s+n\\.', r'November,\\s+n\\.', r'pronounce,\\s', r'nones,\\s+n\\.']:\n    ms=list(re.finditer(pat,t))\n    print('=====',pat,len(ms))\n    for m in ms[:2]:\n        print(repr(t[m.start():m.start()+500].replace('\\n',' ')))\n        print('---')\nEOF"
}
```


### [2026-09-07T19:37:04.163Z] TOOL RESULT

```
===== noon,\s+n\. 1
'noon,  n.  —  ME.,  ‘the  ninth  hour  of  the  day  reck¬ oned  from  sunrise,  noon’,  fr.  OE.  non,  "the ninth  hour  of  the  day  reckoned  from  sunrise’,  fr. L.  nona  (hora),  ‘the  ninth  (hour)’,  fem.  of  nonus, contraction  of  *noven-os,  ‘ninth’,  fr.  novem, ‘nine’  (see  nine),  orig.  used  in  the  sense  of  nones, ‘church  office  said  daily  at  the  ninth  hop-’  (q.v.) The  prayers  referred  to  were  originally  said  at the  ninth  hour  from  sunrise,  i.e.  at  3'
---
===== November,\s+n\. 1
'November,  n.  —  L.  November  {mentis),  ‘the  ninth month’  (of  the  Roman  year),  fr.  novem,  ‘nine’; see  nine.  (The  Roman  year  began  with  March; cp.  September,  October,  December .) novennial,  adj.,  recurring  every  nine  years.  — Formed  with  adj.  suff.  -al  fr.  Late  L.  novennis, ‘of  nine  years’,  which  is  compounded  of  novem, ‘nine’,  and  annus,  ‘year’.  For  the  first  element see  nine,  for  the  second  see  annual.  For  the change  of  Latin  a  (in  a'
---
===== pronounce,\s 3
'pronounce,  pronunciamento,  pronunciation,  re¬ nounce,  renunciation. nuncle,  n.,  uncle  (obsol.)  —  From  misdivision  of an  uncle  (or  mine  uncle)  into  a  nuncle  (resp.  my nuncle). nuncupative,  adj.,  declared  orally,  oral  ( said  of wills)  —  Late  L.  nuncupative,  ‘so-called,  nom¬ inal’,  fr.  L.  nuncupate,  pp.  of  mmcupare,  ‘to call  by  name,  to  call,  name’,  fr.  *ndmo-capos, ‘taken  by  name’,  which  is  compounded  of  no- men,  ‘name’,  and  capere,  ‘to  cat'
---
'pronounce, pronoun,  n.  —  MF.  (=  F.)  pronom,  fr.  L.  prono- men,  from  the  phrase  pro  nomine,  ‘instead  of  a noun’,  fr.  pro,  ‘for’  (see  1st  pro-),  and  abl.  of nomen,  ‘name’ ;  see  noun.  L.  prondmen  is  a  loan translation  of  Gk.  avrcovupda. pronounce,  tr.  and  intr.  v.  —  ME.  pronouncen ,  fr. OF.  pronuncier,  prononcier  (F.  prononcer),  fr.  L. prdnuntiare,  ‘to  make  publicly  known,  tell,  an¬ nounce,  pronounce’,  fr.  1st  pro-  and  niintidre,  ‘to a'
---
===== nones,\s+n\. 2
'nones,  n.  pi.,  the  ninth  day  before  the  ides  ( Ro¬ man  Calendar).  —  L.  nonae  (dies),  ‘ninth  (days)’, fern.  pi.  of  nonus,  ‘ninth’,  contraction  of  •noven- os,  fr.  novem,  ‘nine’.  See  nine  and  cp.  nonagon, nonagenarian,  nonary,  nonuple.  Cp.  also  next word. nones,  n.  pi.,  church  office  orig.  said  daily  at  the ninth  hour  reckoned  from  sunrise,  i.e.  about  3 o’clock  P.M.;  now  usually  said  somewhat  ear¬ lier.  —  PI.  of  none,  ‘ninth  hour’,  fr'
---
'nones,  n.  pi.,  church  office  orig.  said  daily  at  the ninth  hour  reckoned  from  sunrise,  i.e.  about  3 o’clock  P.M.;  now  usually  said  somewhat  ear¬ lier.  —  PI.  of  none,  ‘ninth  hour’,  fr.  L.  nona ( hora ),  ‘ninth  (hour)’.  See  prec.  word  and  cp. noon. nonesuch, nonsuch, adj.,  unequalled;  n.,  a  person or  thing  unequalled.  —  Compounded  of  none and  such. nonfeasance,  n.,  failure  to  do  something  that should  be  done  (law).  —  Formed  fr.  non-  an'
---
```


## [2026-09-07T19:37:14.774Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY noh\"; grep -n \"نُه\\|^نه\\b\\|نه (\\|نهم\" incoming/ARY/ARY_pages.txt | head -15; echo \"=== ARY nalidan\"; grep -n \"نالیدن\\|ناله\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-07T19:37:14.857Z] TOOL RESULT

```
=== ARY noh
168:طی این کوچ‌های مرکز گریزانه (107۸710075/ ب273877817170۸3) هندوار وپایی‌ها.
407:مثلاً انگلیسی برمی‌گردد به انگلیسی میانه (از ۱۱۰۰ تا ۱۵۰۰ میلادی) و انگلیسی میانه منشعب است
408:از انگلیسی کهن (از ۵۰۰ تا ۰ میلادی). همین طور فرانسه پرمی گردد به فرانسه‌ی میانه (از ۱۴۰۰
595:هفتم تانهم میلادی و هتیت مربوط به ۲۰۰۰ تا ۱۲۰۰ سال پیش از میلاد) بیش ما در باره‌ی زبانهای ۱
613:میانه (حدود ۱۵۰۰ تا ۱۳۵۰ پیش از میلاد) وهتیت نو (حدود ۱۳۵۰ تا ۱۲۰۰ پیش از میلاد) نوشته ..
691:نخستین اشاره به اقوام ایرانی (مادها و پارس‌ها) در متون آسودی وابسته به قرن نهم پیش از
694:این متون چنین برداشت می‌شود که مادها و پارس‌ها تازه‌واردانی بودند که قبل از حدود قرن نهم پیش
727:از گذشت زمان» پارسی کهن تبدیل به پارسی میانه (پهلوی) شد. پهلوی زبان ایرانیان در دوران .. ؛
779:۰ میلادی). بعدها این زبان به ایرلندی میانه (۰ ۹۰۰-۰ میلادی) و سپس به ایرلندی و
800:کهن(۴۵۰تا ۰ میلادی) تبدیل شد به انگلیسی میانه (۱۱۰۰ تا ۱۵۰۰) و سپس به انگلیسی نوین,
801:(۱۵۰۰ به بعد). مشابهاً آلمانی کهن (۹۰۰ تا ۱۱۰۰) تبدیل شد به آلمانی میانه (۱۱۰۰ تا 2۱3۰۰ 2
836:پیشین‌ترین متن به زبان‌های اسلاوی عبارتست از ترجمه انجیل در سده‌ی نهم میلادی. این
843:آمدند. ولی رشد آنها آنقدر سریع بود که از قرن چهارم تا قرن نهم میلادی از خاور تاکوه‌های اورال
968:نهادهای بنیادین هند و اروپائیان نخستین
1870:ایردی میانه (۸/31ا ظاط0ا/0: ۰ 0585 38 لاه
=== ARY nalidan
9793:اسلاوی کهن (6املد تلعقناله ا0). -1(187) 6۷۷ :5( 2 027 ملد
14269:بلوچی (الق‌تاملشفها: 110 اسلاوی کهن (ع477ها5 #ل#6ناله 00):
14923:۴ / نواء نوانیدن, نویدن (به چم "نغمه* *خواندن" *نالیدن*)
14931:فارسی (/(۳8۶14): نواء نوانیدن, نویدن (به چم"نغمه آخواندن "نالیدن)
```


## [2026-09-07T19:37:15.719Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FRS novidan\"; grep -n \"نویدن\\|زنودن\\|نوید\" FRS_pages.txt | head -15"
}
```


### [2026-09-07T19:37:15.771Z] TOOL RESULT

```
=== FRS novidan
5534:    ‫که از ناله اش هیچکس تفتوید ‪.‬‬       ‫ز درد دل‌آن شب بدان سان نوید‬
14404: ‫کفرادن نوید باشد »چ ‪ :‬خرام نوید دادن‬
16134:‫‪ - 4‬چ ‪:‬نو آبین نویدید آمده‬         ‫طبقی » س این لفت را ندارد‪-:۳ .‬هچه‬
```


## [2026-09-07T19:37:23.237Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY ctx\"; sed -n '14900,14945p' incoming/ARY/ARY_pages.txt; echo \"=== pdf tag\"; awk 'NR<=14931 && /\\[pdf page/{p=$0} END{}' incoming/ARY/ARY_pages.txt; grep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F: '$1<14931' | tail -2"
}
```


### [2026-09-07T19:37:24.496Z] TOOL RESULT

```
=== ARY ctx
اوستی (05987/0: ۱۷20 ,۲۷۵۵ انگلیسی (#لدلاه/(ق): ازندن
کردی (11801574): 0 ,۸۲ دانمارکی (0۸//8[4): 4
بلوچی (/7عتاله8): ,306 سوندی (89(۳80/877): ود
افغانی (پشتو) (/4۳0/۸/۷: ,۲۲۸۷۸ ,لا۸۸ نروژی (07701۸2/): ی
رازن هلندی ([0176): دا انا
تخاری ۸ (۸ ۸(۷ل702071۸۶): زا اسلاوی کهن (۲10ما5 7ل#6نابل )+
تخاری 8 (8 4۸ل1038:)7017۸7 ,8175 0
سانسکریت (540/5077): ۸۲۸۷۷۸۹ ,۷۸8 لهستانی (/۳0./3): #یزان
ارمنی (45۸17۸24): 0 روسی (/۷5540: ۰ ۳۲0۷1۲ ,۲0۵۷۷3
یونانی (07554): 8 ,۸805 چک (2501)): 0
لاتین (471): ۰ ۲۵۲۲۷286 ,210۷15 صربی (5858814/۷): انداند
فراسه (//۳۵2/6): ۰ ۷8177 ,۲۵۲2۷۸ برهمی (801721/1/2): 0
چي ,اسپانبایی (9ال ۰:62 ۷۷8۸ ,2۷0570 اسلواکی (51.014): 0
۹ #ایتالیایی (( له )): ۹ ۱۲0۷۵ یتوانی (۸/1/۷نا7/): 3۸۷۸۹ ,2۸7۸5
رومانی (/۷02/4۸4, ۹۱۳۹+ 0 ایرلدی کهن (اقنها صا0): 05(
پرتغالی (007000588: ۰ 0۷۸ ,310۷0 گالی (84لله۸): 0
گرنبک (00777/6): ۸۱لا ولزی (874ا#5): زا زا ورد ند
ایسلندی‌گهن (/5(/0/01۸740 صاه): برتونی (/87870۸): این برد لد
۵3 گالبک (0۸51/0): ۸7
ساکسونی کهن (540۸ ۰:0۵ ۴1۷۲۱ هیت (111۳7118): 1۸5
فریزی گهن (۲۸/3۱۵ ۰:۱۵ ۸1۵۱۲
سس
[pdf page 503]
۴ / نواء نوانیدن, نویدن (به چم "نغمه* *خواندن" *نالیدن*)
پسگشت‌ها اه ادن دناد 937 ۰ ناه
رر ۳ 8 (۸8۷) :00/5
2 (۱85) تین 9 (018) 1 ظ» ۱ +537
9 (نا۸0۵۲۷۴۸) :۸5( ما08 برهان قاطع + ۱ 1۱۷۳ 3
5 (015_ :5 ۳205(12 ۸/۸
بادداشت: َ
این واجربشه هند و اروپایی با واجریشه‌ی هند و اروپایی ۸۷811۰ با ۴۸/۰ (به چم "اکنون") خویشی دارد.
فارسی (/(۳8۶14): نواء نوانیدن, نویدن (به چم"نغمه آخواندن "نالیدن)
اوستایی ([۸۷8870): ۸ ایرلندی کهن (317لغ] صا0): 7۸5 ٍ
پهلری (1هالاه۳): زا نالا
01 ,۸ 2۲7۷/8/51:10 پسگشت‌ها شید ۲ ْ
کردی (07([8[7)): 1۸ 9 ۸00/0
تخاری 8 (8 ۸(۷ل70(7): زا 1 (۲388) هام02
سانسکریت (84(/5877): 1 ۸۸۵۷۸55 ,3 (12102190) ۸025
ارمنی (/(۵78(/4): ۰ ۲۷۸0586 ,۲۲۸6 :للم ۸ 0 مها ۱
یونانی 0280): 0 ۸50۸ 2 (۸۳۹۲۲۲۵)
لاتین (471): 710 ,۳۷۸7108 | 253 0۸181۵00۷ ۸40
لتونی (لتی) (714/۷ل): تا[نا7۸ برهان قاطع + ۹ ۲۱۷۴و ۲۱۸۰ ۱
بادداشت: ۱
چم اپن واژه در زبان لاتین: پیام رسان» فرستاده, ا
۱
| م‌انگلیس سروازی رن 0
=== pdf tag
14888:[pdf page 502]
14922:[pdf page 503]
```


## [2026-09-07T19:37:37.329Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14888,14902p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-07T19:37:37.365Z] TOOL RESULT

```
[pdf page 502]
کب یی .
نوء نوین / ۵۱۳
یادداشت,
چم این واژه در زبان آلمانی: (زبان کردگان) شیر,
چم این واژه در زیان پلغاری؛ ارشد» بزرگتر.
| مانگلیسی سروازهی ان 88۷
اوستایی (488744): ۸ ,2۸۷0 آلمانی کهن (/08701۸ 104 0ا0):
پارسی باستان (۳87817 صا0): آرررا ان
8 ۸۲817801 آلمانی (0280/2(4): دی
پهلوی (۲1بمابته۳): ,۸06 ,۸۷۸۷۸۵۹ ,۲۲06 انگلیسی کهن (باقلا8/0 صام): ‏ ,۸۷۲5
0 5 ,۸30۲/5
اوستی (05987/0: ۱۷20 ,۲۷۵۵ انگلیسی (#لدلاه/(ق): ازندن
کردی (11801574): 0 ,۸۲ دانمارکی (0۸//8[4): 4
بلوچی (/7عتاله8): ,306 سوندی (89(۳80/877): ود
```


## [2026-09-07T19:37:45.706Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"نه» «نهم\\|نه, نهم\\|نه (به چم\\|«نه»\" incoming/ARY/ARY_pages.txt | head; echo ===; grep -n \"نه / ۵\\|نه/ ۵\\|نهم /\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-09-07T19:37:45.758Z] TOOL RESULT

```
Exit code 1
5657:فارسی (۳8۶/4۷). ۰ ترخینه, تلخینه, ترخنه (به چم "آب کشک)
11015:شانه (به چم "استخوان کلف" و "کثیف) / ۳۷۳
12022:فارسی (۳88514(0): کش, کشال, کشانه (به چم "بغل, آغوش, آسینه آزیربغل", اکشاله:
13284:۸ / گون گونه (به چم *رنگ» "رخسار")
15241:والانه ولانه (به چم *زخم", *جراحت") / ۵۱۵ ٍ
(eval):1: == not found
```


## [2026-09-07T19:37:50.130Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"novem\\|21ا0۷\\|ننه\\|نُهم\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo === ; grep -n -i \"NEWN\\|NEUN\\|NINE\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-07T19:37:50.182Z] TOOL RESULT

```
Exit code 1
463:4 naoi | naw ennea novem nove; a
(eval):1: == not found
```


## [2026-09-07T19:37:53.170Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '440,480p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-07T19:37:53.220Z] TOOL RESULT

```
V4 | aelus

[esis Fe | Geman | Dah ——_—| St
\ yak | un einz cen en
Y do | deux we} tween WA
Y se | trois drei drie tre
¥ chahar | quatre vier vier fyt
O— panj | cing funf vif fem
%  shesh | six sechs zs Sex.
Vv haft | sept sieben zeven su
A hasht | huit acht acht atta
4 noh | neuf neun negen nio
y+ dah | dix zebn tien tio
Yee sad cent hundert honderd hundra
Trish ‘Weish Greek Latin Italian
\ aon | .un hen unus uno
v do | dau duo duo due
y tri tri treis tres tre
¥ ceathair | pedwar tettares quattuor quattro:
O — cuig | pump pente quinque cingue
ta se | chwech hex Sex sei
Yseacht | saith hepta septem sette
A ocht | wyth okto octo otto -
4 naoi | naw ennea novem nove; a
\+ Deich | deg deka decem +] leet
Yes coad cant ‘hekaton centum cento
[pdf page 19]
805 ly} sata cla, | Te
\ en | one jeden odin ek
Y to | two dwie dva dvi
Y tre | three try tri tri
* fire | four | extery chetyre car
age elm me me
Tg seks | six szese shesht chay
Vv sw | seven . | siedem sem sat
A Otte | eight osiem vosem at
4 ni nine dziewiec devyat nay
Ye | ten dziesiee desyat das
hundrede | hundred sto sto sa
ee .
Spanish | Lithuanian | albanian Armenian Tocharian A
```


## [2026-09-07T19:38:01.792Z] TOOL CALL #62: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2210 --image 2>&1 | tail -20"
}
```


### [2026-09-07T19:38:08.886Z] TOOL RESULT

```
1 ص با وبفتخ اول وخفای ثانی» افاده معنی لیاقت‌میکند
وامرپنهادن هم هست بمنی بنه ویگذار۷ سوم
اول وظپورها(؟) عددی است که آرا بعر بی تسعه همجو شاهانه وبز رگانه ودرو بشانه ۹ اس وتقسیسر
(۱) چش: - وعربان - (۲) خم۱ : ثانی.
۱ - اسم مقعول از « نویدن» (ه.م.) ۴ - از دساتیر ۸ فرهنگه دساتیرصض ۰۴۲۷۱
۴ -« السرع والسرعرع » آاچه ببالد ازسرشاخ رز» «مهذب‌الاسماء نسخهٌ خطی کتابغانه
دهغدا » و رك4 : منتهی‌الارب . ۴ - نوبان (ه.م.). ر4: جفتایی ص ۵۱۱: « خاقان‌منصور
قلب میمنه و مسرهة سپاه ظفر یناه را بنور طلمت شاه زادگان آفتاب احتشام و فر وجود نوبینان
بهرام التقام زیت و استخکام داده بمیدان جنگه و هم رکه نام و شگه فرستاد . د میرخواند ۰
حبیب‌المیر. چاپ خام جح 4 ص۹٩۹‏ 6۲۰. فقه‌اللنه عامیانه ۰ ر4 : نیشابور ۰
‎٩‏ - فقه‌اللفهٌ عامیانه . رك : نهاوند . ۷ - رك : نهادن .
۸ - پارسی باستان -88۷2778 (نهم) » اوستا 82038-۰88۷2 820708۰ (هم)»
بهلوی 321 , هندی باستان 34۸۷8 , ارمنی 188 ۰ افغانی ع (21)12 » وخی و شغفنی ۰340
سنگلیجی وهنجی 120 ۰ پغنوبی 8314 » سربکلی36۷ ۶۸ اسشق ۱*۵۹ > ورك: هوبشمان۱*۵۹؛
کردی 8610 , 2۵ . 285 . 36۵ ۰ زازا 88۷ ۰ دوجیکی 210 «ژابا س ۶۲۸ »پهلوی ۰38
ابرانی‌باستان -32۷8 ۰ بقرابت « ده » 121 ساخته شده. فارسی‌جدید 810 از 3۵ از 28۷8
با ظ بقیای 188 « یب رکه ص۱۵4 >. ‎٩‏ - درین کلمات پسوند ۸ آنه» است.
‌ وین - رد : نوبان ۰
( برهان قاطع ۳۷۹ )
```


## [2026-09-07T19:38:14.848Z] TOOL CALL #63: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ | tail -5; python3 -c \"\nfrom PIL import Image\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2210.png'\nim=Image.open(p); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.62),w,int(h*0.90))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2210_foot.png')\n\""
}
```


### [2026-09-07T19:38:16.376Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb    1152 Sep  5 01:39 733.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  726576 Sep  6 18:36 829.png
-rw-rw-r--  1 sfmqrb sfmqrb     981 Sep  6 18:36 829.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  624515 Sep  5 16:20 902.png
-rw-rw-r--  1 sfmqrb sfmqrb    1658 Sep  5 16:20 902.vision.txt
(1650, 2546)
```


## [2026-09-07T19:38:20.230Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2210_foot.png"
}
```


### [2026-09-07T19:38:20.252Z] TOOL RESULT

```

```


## [2026-09-07T19:38:44.217Z] TOOL CALL #65: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2195 --image >/dev/null 2>&1; python3 -c \"\nfrom PIL import Image\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2195.png'\nim=Image.open(p); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.72),w,int(h*0.95))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2195_foot.png')\n\""
}
```


### [2026-09-07T19:38:50.537Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-07T19:38:53.731Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2195_foot.png"
}
```


### [2026-09-07T19:38:53.748Z] TOOL RESULT

```

```


## [2026-09-07T19:39:24.191Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr && cat > BQT/2210.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 2210 (vol 4 scan, pdf p. 293) — headword نه and Mo'in's footnote 8, read from the page image]\n\nنه ... اول و ظهور ها(؟) عددی است که آنرا بعربی تسعه میگویند - و اشاره بر نه فلک - و نه سوراخ\nقالب آدمی باشد که آن دو سوراخ گوش و دو چشم و دو سوراخ بینی و دهان و مقعد و مبال است ...\n\n۸ - پارسی باستان navama- (نهم) ، اوستا nava ، nâuma- ، naoma- (نهم)،\nپهلوی naum ، هندی باستان náva ، ارمنی inn ، افغانی ع nu(h) ، وخی و شغنی náo ،\nسنگلیجی و منجی nao ، یغنوبی nau ، سریکلی nev « اسشق ۱۰۵۶ » ؛ و رک: هوبشمان ۱۰۵۶؛\nکردی neh ، nû ، nah ، nêh ، زازا niu ، دوجیکی nau « ژابا ص ۴۲۴ » ، پهلوی nah ،\nایرانی باستان nava- ، بقرابت « ده » dah ساخته شده. فارسی جدید nuh از nôh از nava-\nبا h بقیای dah « نیبرکه ص ۱۵۴ ».\nEOF\ncat > BQT/2195.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 2195 (vol 4 scan, pdf p. 278) — headword نوزده and Mo'in's footnote 8, read from the page image]\n\n۸ نوزده = نوازده « اسشق ۱۰۴۸ » ، « ژابا ص ۴۲۵ » ؛ بضم اول و فتح دال، پهلوی\nnavazdah (nôzdah) « نیبرکه ص ۱۵۵ » ، اوستا navadasa- ( نوزدهم ) ، هندی\nباستان návadasa ( نوزده ) ، افغانی nûlas ، nûnas ، آستی näudās ، nudās « اسشق\n۱۰۴۸ » ، کردی deh - nûz ، nôzdeh ، nuzdak ؛ زازا yés - neu « ژابا ص ۴۲۵ » ؛\nعدد نه بعلاوهٔ ده ، عدد بین هیجده و بیست .\n\n[NB: the etymological footnote for the headword نه 'nine' itself is on p. 2210, not here.]\nEOF\nmkdir -p FFD BOOK && cat > FFD/77.vision.txt <<'EOF'\n[M. Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, printed p. 77 (= pdf page 82 of FFD_asmaneketab.pdf), read from the page image]\n\nنالیدن\n«نالید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است.\nنال ← فارسی میانه nāl ← ایرانی باستان *nard-a. برای a ← آرای. ریشهٔ nard به\nمعنی «بانگ کردن» است.\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg363.png BOOK/363.png\nls -la BQT/2210.vision.txt BQT/2195.vision.txt FFD/77.vision.txt BOOK/363.png"
}
```


### [2026-09-07T19:39:25.363Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66511 Sep  7 15:39 BOOK/363.png
-rw-rw-r-- 1 sfmqrb sfmqrb   762 Sep  7 15:39 BQT/2195.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1091 Sep  7 15:39 BQT/2210.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   405 Sep  7 15:39 FFD/77.vision.txt
```


## [2026-09-07T19:39:29.181Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/noon",
 "prompt": "Give the etymology of \"noon\" verbatim: Old English non, Latin nona hora, and the date/reason the sense shifted from 3 p.m. to midday."
}
```


### [2026-09-07T19:39:33.528Z] TOOL RESULT

```
# Etymology of "Noon"

**Old English Origin:**
"Old English _non_ '3 o'clock p.m., the ninth hour from sunrise,' also 'the canonical hour of nones,'"

**Latin Source:**
"from Latin _nona hora_ 'ninth hour' of daylight, by Roman and ecclesiastical reckoning about 3 p.m."

**Sense Shift Timeline and Reasons:**
The transition from 3 p.m. to 12 p.m. began during the 12th century and was complete by the 14th century. The document attributes this shift to several possible causes: unreliable medieval timekeeping devices, seasonal variations in daylight hours in northern regions, the practice of ending monastic fasts at nones (which may have incentivized moving the time earlier), or changes in customary mealtimes for the midday meal.
```


## [2026-09-07T19:39:39.657Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/nuntius' --note 'page 363, root Neu, node #5 Latin nuntium: de Vaan tentatively favours PIE *newH- \"to cry\"' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁néwn̥' --note 'page 363, root Newn: PIE *h₁néwn̥ \"nine\", PII *Hnáwa, PGmc *newun, Lat novem' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/noon' --note 'page 363, root Newn, node #8: OE non < L nona hora, sense shift 3pm > midday 12th-14th c.' 2>&1 | tail -3"
}
```


### [2026-09-07T19:39:41.886Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5c038e36894fbdc6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7d04dc4781350e06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0bed3615bc25cee.txt
```


## [2026-09-07T19:40:02.358Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -ln \"زنودن\" *.txt incoming/*/*.txt 2>/dev/null; echo ===; grep -n \"زنودن\\|زنوییدن\" BQT_v2_pages.txt FRS_pages.txt MON_part2.txt 2>/dev/null | head"
}
```


### [2026-09-07T19:40:02.441Z] TOOL RESULT

```
Exit code 1
incoming/BQT/BQT_v4_pages.txt
GPL.txt
(eval):1: == not found
```


## [2026-09-07T19:40:07.538Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -B3 -A3 \"زنودن\" GPL.txt | head -30; echo \"=== what is GPL\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d.get('GPL',{}).get('title'), '|', d.get('GPL',{}).get('page_offset'))\""
}
```


### [2026-09-07T19:40:08.825Z] TOOL RESULT

```
1042-(i) Drop this termination and replace it by ای‎ (see II. A); eg.
1043-Bg) to test’ زدودن آزمای‎ ‘to polish’ زدای‎ آسودن‎ ‘to rest’ ستودن آسای‎ ‘to praise’ سناعا‎ افزودن‎ ‘to increase’ سرودن افزای‎ ‘to sing’ سرای‎ آلودن‎ ‘to soil’ فرمودن آلای‎ ‘to speak, command’ فرمای‎ آندودن‎ ‘to smear’ نمودن اندای‎ ‘to show’ نمای‎ پالودن‎ ‘to filter’ «خشودن بالای‎ ‘to give’ «خشای‎ پیمودن‎ ‘to measure’ بالودن پیمای‎ ‘to grow tall’ بالای‎ خشودن‎ ‘to prune’ حخشای‎ ws, ‘to carry off’ sh,
1044-a کشودن‎ ‘to open’ کشای‎ [ see pus] (ii) By dropping the infinitive termination and pointing the vav with fatha; e.g. شنودن‎ ‘tohear’? 424 [see [شنیدن‎
1045:غنو ‘to nod’‏ غنودن 32 reap’‏ درودن تنو stretch’‏ 0 تنودن زنو neigh’‏ 0 زنودن
1046-not used ] [شودن‎ ‘to become’ 52 [see oe | Trregular : بودن‎ ‘tobe’ ��اش‎ or 53 ۵
1047-D. Infinitives in کین‎ with a preceding consonant. (a) Preceded by ن‎ ۰ The Present Stem is (i) Formed by dropping کن‎ dan; e.g.
1048-مان ‘toremain’‏ ماندن ‘to throw’ owl‏ انگندن
--
2818-Note. رآندن‎ ‘to drive’. The verb راندن‎ ‘to drive’ (aor. stem ran-) is a contraction of the causal رواندن‎ rav-an-dan, of theverb رفتن‎ ‘to go’; aor. stem رو‎ ۰
2819-B. VERBS WITH A CHARACTERISTIC 1) Verbs with the Characteristic a
2820-§ 76. The primitive roots of the class end in وه‎ which is strengthened before the characteristic (i. e. w becomes aw) to form the stem or base of the O.P. pres. indicative (e.g. rt. bu: pres. indic. stem bav-a). Persian generally lengthens the root-vowel in the infinitive; and for the aorist stem (which corresponds to the O.P. pres. indic. stem), usually employs ba- instead of baw- in the verb bu-dan; e.g.
2821:Root INFINITIVE Aorist Stem bu: (cf.8. bhai) | yoy ba-dan (poetical also oa.) 3 bau-; bu-(ac- ‘to be’ cording to usage) shiyu شدن‎ shu-dan (old (شودن‎ ‘to go, | شو‎ shau- become” وه‎ Fi درو 4 اس‎ dirau-, or ; et J dru درودن‎ 2 0 reap ee (conjunct dr dissolved in Persian) zi-nu-dan ees بل‎ efix UZ | زنودن‎ } ‘to neigh رز‎ 20nau- Noe oe wy zu-nu-dan رد‎
2822- 
2823- 
2824- 
=== what is GPL
J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911 | leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-07T19:40:16.771Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('GPL.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find char offset of line 2821 (1-based)\noff=sum(len(l)+1 for l in lines[:2820])\nleaf=t[:off].count('\\f')\nprint('leaf(0-based ff count)=',leaf,'printed approx=',leaf-12)\noff2=sum(len(l)+1 for l in lines[:1044])\nprint('line1045 leaf=',t[:off2].count('\\f'),'printed approx=',t[:off2].count('\\f')-12)\ni=t.find('zi-nu-dan')\nprint(repr(t[i-700:i+300]))\nEOF"
}
```


### [2026-09-07T19:40:18.053Z] TOOL RESULT

```
leaf(0-based ff count)= 252 printed approx= 240
line1045 leaf= 110 printed approx= 98
'Characteristic a\n§ 76. The primitive roots of the class end in وه\u200e which is strengthened before the characteristic (i. e. w becomes aw) to form the stem or base of the O.P. pres. indicative (e.g. rt. bu: pres. indic. stem bav-a). Persian generally lengthens the root-vowel in the infinitive; and for the aorist stem (which corresponds to the O.P. pres. indic. stem), usually employs ba- instead of baw- in the verb bu-dan; e.g.\nRoot INFINITIVE Aorist Stem bu: (cf.8. bhai) | yoy ba-dan (poetical also oa.) 3 bau-; bu-(ac- ‘to be’ cording to usage) shiyu شدن\u200e shu-dan (old (شودن\u200e ‘to go, | شو\u200e shau- become” وه\u200e Fi درو 4 اس\u200e dirau-, or ; et J dru درودن\u200e 2 0 reap ee (conjunct dr dissolved in Persian) zi-nu-dan ees بل\u200e efix UZ | زنودن\u200e } ‘to neigh رز\u200e 20nau- Noe oe wy zu-nu-dan رد\u200e\n \n \n \n \n200 Accidence\nghuniidan ‘to nod,\u200f غنودن ‘to nod’; (2945 “to draw’. Rem.\u200f غنودن ghunau-.\u200f غنو doze’ (a verb of doubtful origin), has for its aor. stem\u200f ۰ تنو ‘to draw’, &c., also has for its aor. s\x0ctem\u200f م2000 تن'
```


## [2026-09-07T19:40:27.319Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer(r'NINE', t))[:6]:\n    print(repr(t[max(0,m.start()-200):m.start()+700].replace('\\n',' ')))\n    print('-----')\nEOF"
}
```


### [2026-09-07T19:40:29.051Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:40:33.329Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'13\\.1[0-9]', r'Nine\\b']:\n    ms=list(re.finditer(pat,t))\n    print('==',pat,len(ms))\nfor m in list(re.finditer(r'Nine\\b', t))[:8]:\n    print(repr(t[max(0,m.start()-150):m.start()+400].replace('\\n',' ')))\n    print('---')\nEOF"
}
```


### [2026-09-07T19:40:34.808Z] TOOL RESULT

```
== 13\.1[0-9] 52
== Nine\b 0
```


## [2026-09-07T19:40:40.194Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer(r'novem', t))[:6]:\n    print(repr(t[max(0,m.start()-500):m.start()+500].replace('\\n',' ')))\n    print('-----')\nEOF"
}
```


### [2026-09-07T19:40:41.471Z] TOOL RESULT

```
', Grd. d. indo-ar. Phil. 3.9.12. For the Celts the Calen- dar of Coligny attests an old division of the month into halves (Thurneysen, Z. deutsch. Wortf. 1.191). The times CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar of new moon and full moon were the oc- casion of folk-assemblies among the Germans (Tacitus, Germ. ch. 1) and of religious festivals among the Greeks. The regular Greek division of the month was into three decades. The Ro- mans had their market-day, nindinae (cpd. of novem ‘nine’ and old word for ‘day’), held every ninth day, the inter- vening period (really eight days if reck- oned from a given point of the first to the ninth) being niindinum. . The seven-day week was unknown 1n Europe until its importation from the East. Whatever its ultimate source and explanation, the seven-day week is defi- nitely known as an ancient Jewish insti- tution. Hence first the Jewish week and, somewhat later, with an adn of orienta] astrology, the planetary weé became known t'
-----
'y those prescribed by Charlemagne) would require so much space that it seems best here to consider only the Lat. names and their spread. The Lat. names were adj. forms with ménsis ‘month’ understood. Since the Roman year orig. began with March, the numeral derivs. which served is July-December, were Quinctilis ‘fifth for July, Sextilis ‘sixth’ for August (these later replaced by Idlius and Augustus 0 honor of Julius Caesar and Augustus), aay oR eS Ae et ee ae i a hen October, November, December novem-ri-s, *decem-ri-s, f medial mr to mbr, order beginning with Janu- Fe er eidesoon naisly the names of gods or g dTa RABE. Janus, Mars, Mava, an nel neces arius, the last month of the o ca en ar, yas the ‘month of PUAN NOH, fr. februdre ‘cleanse, purify (Ernout-M. 34], Walde-H. 1.472). Aprilis, prob. f, an Btruscan name based on a short form of Grk. Adpodirn. Benveniste BSL 32.70 ff. Cortsen, Glotia 27.270 ff. The Roman names have persisted in all the Romance languages. But most of the Rum. '
-----
```


## [2026-09-07T19:40:55.601Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\*nau\\|^\\*nu \\|\\*nauH\\|nawidan\\|noyidan\\|nōyīdan\" CHEUNG.txt | head -15; echo ===; grep -n \"zenūdan\\|zinūdan\\|zunūdan\" CHEUNG.txt HRN.txt HUB.txt | head"
}
```


### [2026-09-07T19:40:55.658Z] TOOL RESULT

```
Exit code 1
17915:rejoice’ at a certain stage. Cf. NP noyidan ‘to cry aloud, lament’, navistan ‘to groan’, 
18742:*nau ‘to move’ 
18777:*nau(H) ‘to cry, wail’ 
18784:*NWIR: NP noyidan ‘to cry aloud, lament’, navidan ‘to complain, lament’, navidan 
18787:new ‘mew’ || (+ *uz-) NP zinudan/zinav-, zunudan/zunav-, zunoyidan ‘to wail’ 
41223:noyidan, 271, 284 
(eval):1: == not found
```


## [2026-09-07T19:40:58.989Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18775,18800p' CHEUNG.txt; echo \"==== ctx 17905\"; sed -n '17900,17925p' CHEUNG.txt"
}
```


### [2026-09-07T19:40:59.070Z] TOOL RESULT

```
*nau(H) ‘to cry, wail’ 

*KHOTANESE: ? OKh. nuva- ‘to make a noise (i.e. howl ?)’ > SGS: 58 

*SOGDIAN: 9 Sogd. nwß ‘noise’, cited in DKS: 190a, does not exist, Sims-Williams 
1983: 43. 

*NWIR: NP noyidan ‘to cry aloud, lament’, navidan ‘to complain, lament’, navidan 
‘to complain’, navistan ‘to groan’, NP nöyah ‘plaint, moan’, NP navä ‘sound, song; 
grief, pain (etc.)’, nöstah, navastah ‘noise in the throat by one’s crying’, Kurd. new- 
new ‘mew’ || (+ *uz-) NP zinudan/zinav-, zunudan/zunav-, zunoyidan ‘to wail’ 
(LW) 

*NEIR: Oss. I. niwyn/niwd, D. newun/niwd ‘to cry’, (with long *-a-) Sariq. niuw, 
new-/niwd ‘to weep’, Wa. nbrw-/nowd ‘to weep, wail’, Sh. naw-/ntid, Rosh. naw-/ 


*naz 285 


nawd ‘to weep’, Yghn. nuyok ‘crying, howling’, novva ‘sound’ || (+ *а-) Yi. anuv- 
‘to bellow’ || (+ *fra-) Sh. (Baj.) rinäw-/rinewd (orig. caus.) ‘to tease, mock, make 
weep’ 

==== ctx 17905

*NWIR: NP möyidan ‘to mourn; weep and cry aloud’, NP must ‘trouble, distress of 
mind, complaint, lamentation’ 

*MISC: ? Arm. (LW) moyr ‘begging’ (semantically not evident, Benveniste 1964: 5) 
© The Persian forms are isolated within Ilr.: they might be connected to the IE 
correspondences cited by Pokorny: 743: Lith. maudziu (maüsti) ‘I long for’, Gr. 
u$00c (m.) ‘word; tale’, OCS mysle ‘thought’, etc. However, if the Persian forms 
were from older *maud as assumed generally, they would be identical with the 
semantically antonymous root *maud ‘to rejoice’ (Skt. mod), which is attested in 
Iranian: not only in Avestan (maoóano.kara- “providing joy’), but apparently also in 
OP (*maudabaga- ‘who pleases God’, Mayrhofer 1973: 208, ad 8.1185). The co- 
existence of two formally identical roots with opposite meanings within one 
language is inconceivable. More likely, we are dealing with the root *nau(H) ‘to 
mourn’ (q.v.), which became contaminated with the antonymous root *maud ‘to 
rejoice’ at a certain stage. Cf. NP noyidan ‘to cry aloud, lament’, navistan ‘to groan’, 
NP nöyah ‘plaint, moan’, nöstah, navastah ‘noise in the throat by one’s crying’. 

*PIE — = LIV: — | Pok.: 743 


*REFERENCES: Horn 1893: 223 f. 


*maug (*mauz) ? ‘to err, be foolish’
```


## [2026-09-07T19:41:05.743Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18800,18820p' CHEUNG.txt"
}
```


### [2026-09-07T19:41:05.789Z] TOOL RESULT

```
*SANSKRIT: nav” ‘to roar, cry’ (RV+) > EWAia II: 23 

«PIE *neu(H)- ‘to cry out, shout’ — LIV: 456 f. | Pok.: 767 

*IE COGNATES: Toch. nu- ‘to cry out; threaten’, Lat. nuntius ‘(official) message’, 


Olrish nuall ‘cry, alarm, proclamation’ 
*REFERENCES: IIFL II: 191a; Abaev, Slovar’ II: 184 f.; EVS: 50b, 68a; DKS: 190b; Gharib: 245a; Werba 
1997: 355; Adams 1999: 339 f.; Steblin-Kamenskij 1999: 253; Cheung 2002: 102, 208 


*naj ? ‘to turn, roll’ 

*MIDDLE PERSIAN: 9 Bailey, DKS: 180a, s.v. пауѕ- ‘be proud, delicate’ cites BMP 
nazénd ut garténd (Dd 36.22), the first verb would contain the base näz-, naZ- ‘to 
roll, turn’. In fact it should rather be read as the very common verbal form /wazend/ 
‘they fly, move’ (cf. Jaafari-Dehaghi: 118 ad 36.22). 

*SOGDIAN: BSogd. n'z, MSogd. n? ‘to roll, twist, turn around’ || (+ *pari-) BSogd.
```


## [2026-09-07T19:41:35.889Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/w/index.php?title=%D9%86%D9%87&action=raw",
 "prompt": "Quote verbatim the Persian numeral section for نه 'nine': its etymology template chain (Middle Persian form, Proto-Iranian, Proto-Indo-European) exactly as written in the wikitext."
}
```


### [2026-09-07T19:41:39.542Z] TOOL RESULT

```
# Persian Numeral Etymology for نه (nine)

The etymology template chain for the Persian numeral section is:

```
From {{inh|fa|pal||tr=nwk'|ts=nōg}}, from {{inh|fa|peo|𐎴𐎺|tr=n-v|ts=nava}}, from {{inh|fa|ira-pro|*Hnáwa}}, from {{inh|fa|iir-pro|*Hnáwa}}, from {{inh|fa|ine-pro|*h₁néwn̥}}.
```

This shows the inheritance pathway: Middle Persian (nwk') → Old Persian (nava) → Proto-Iranian (*Hnáwa) → Proto-Indo-Iranian (*Hnáwa) → Proto-Indo-European (*h₁néwn̥).
```


## [2026-09-07T19:43:11.159Z] AGENT

Now I'll write the verification file.


## [2026-09-07T19:43:12.855Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%86%D9%87' --note 'page 363, root Newn, node #3: Wiktionary derives Persian نه noh from Middle Persian, Old Persian nava, PIr *Hnawa, PIE *h1newn' 2>&1 | tail -2"
}
```


### [2026-09-07T19:43:14.600Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/388e37fa0e8f68b2.txt
```


## [2026-09-07T19:47:53.095Z] TOOL CALL #81: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk363a.py <<'PY'\n# -*- coding: utf-8 -*-\nimport json\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Neu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *neu(H)- 'to shout, call out, praise' (Pokorny 767 neu-1; LIV² 456f.; Watkins/AHD neu-1 'to shout')\",\n \"note\": \"The root is genuine and the language label is right. Pokorny p. 767 has 'Root/lemma: neu-1  Meaning: to call, to praise  Material: Old Indic navate, nauti „sounds, rejoices, praises’, Old Irish nuall (*neu-slo-) „scream, din, proclamation’; perhaps Latin nuntium „message’ (*nouention)', i.e. exactly the three branches Nourai draws (Sanskrit, Latin, English via Latin). Cheung (2007) 284 sets up the Iranian root *nau(H) 'to cry, wail' and equates it with 'PIE *neu(H)- „to cry out, shout” — LIV: 456 f. | Pok.: 767', listing NP nōyīdan and the *uz- compound zinūdan among its descendants — so the whole Sanskrit–Persian–Latin part of the chart is modern doctrine. Two caveats: (a) the gloss should be 'shout, call, praise' rather than 'cry' in the sense 'weep'; the 'lament' meaning is the Iranian specialisation; (b) the FIRST branch of the chart (Avestan/OP 'nard' → nâlîdan) does NOT belong to this root: Cheung keeps *nard 'to lament, moan' (p. 282) and *nau(H) (p. 284) apart, and only the latter has an IE pedigree. See nodes #1 and #2.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *neu(H)- به معنی «بانگ زدن، فراخواندن، ستودن» ریشه‌ای شناخته و پذیرفته است: پوکورنی در ص ۷۶۷ آن را با معنی «to call, to praise» می‌آورد و همان سه شاخه‌ای را که نورایی رسم کرده است — سنسکریت navate/nauti، ایرلندی کهن nuall و «شاید» لاتینی nuntium از *nouention — گواه می‌گیرد؛ واتکینز نیز neu-1 «to shout» دارد. چونگ (۲۰۰۷، ص ۲۸۴) ریشهٔ ایرانی *nau(H) «گریستن، شیون کردن» را می‌سازد و آشکارا آن را با «هندواروپایی *neu(H)- ... پوکورنی ۷۶۷» یکی می‌داند و «نویدن» و «زنودن» فارسی را از آن می‌شمارد؛ پس تنه و شاخه‌های سنسکریتی، فارسی و لاتینی نمودار درست است. دو نکتهٔ احتیاطی: نخست آنکه معنی ریشه «بانگ زدن و ستودن» است و مفهوم «نالیدن» تخصیص ایرانی آن است؛ دوم آنکه شاخهٔ نخست نمودار (nard ← نالیدن) به این ریشه تعلق ندارد و چونگ آن را ریشهٔ جداگانهٔ *nard (ص ۲۸۲) می‌داند (بنگرید به گره‌های ۱ و ۲).\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:767\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt (English rendering of IEW) lines 62910-62918: 'Root / lemma: neu-1 (*he-neu-)  Meaning: to call, to praise  Material: Old Indic navate, nauti \\\"sounds, rejoices, praises\\\", Old Irish nuall (*neu-slo-) n. \\\"scream, din, fuss, noise, proclamation\\\"; perhaps Latin nuntium \\\"message! announcement; news\\\" (*nouention).  References: WP. II 323, WH. II 188 f.  Page(s): 767'. The cited page number is exactly right.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 323 s.v. '1. neu- „rufen, preisen“'\", \"stance\": \"partial\",\n    \"note\": \"incoming/WLD/WLD_Bd2_pages.txt line 21347-21352: '1. neu- „rufen, preisen“. Ai. navate, nauti „tönt, jubelt, preist“; a[i]r. nuall n. „Schrei, Lärm“, nuallna „clamosus“'. Walde-Pokorny does NOT yet list Latin nuntium here (Pokorny added it in 1959 with 'perhaps'); it also warns that Latvian naujūt 'miauen' is mere onomatopoeia.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. neu-1 (AHD_watkins1985.txt line 785)\", \"stance\": \"supports\",\n    \"note\": \"'neu-1. To shout. Suffixed (participial) o-grade form *now-ent-(yo-), “shouting,” in Latin nūntius, “announcing,” hence a messenger, also a message, and nūntium, message: NUNCIO; ANNOUNCE, DENOUNCE, ENUNCIATE, PRONOUNCE, RENOUNCE. [Pok. 1. neu- 767.]' — Nourai's Latin and English boxes are copied from this article.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 284 s.v. *nau(H)\", \"stance\": \"supports\",\n    \"note\": \"CHEUNG.txt lines 18777-18803: '*nau(H) “to cry, wail” ... *NWIR: NP noyidan “to cry aloud, lament”, navidan “to complain, lament” ... || (+ *uz-) NP zinudan/zinav-, zunudan/zunav-, zunoyidan “to wail” ... *SANSKRIT: nav “to roar, cry” (RV+) ... PIE *neu(H)- “to cry out, shout” — LIV: 456 f. | Pok.: 767. *IE COGNATES: Toch. nu- “to cry out; threaten”, Lat. nuntius “(official) message”, OIrish nuall'.\"},\n   {\"src\": \"ARY\", \"where\": \"printed p. 514 (ARY_pages.txt, [pdf page 503])\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur's independent Persian dictionary of IE roots has the same root box: 'نوا، نوانیدن، نویدن (به چم «نغمه»، «خواندن»، «نالیدن»)' with Avestan, Pahlavi, Sanskrit (navate/nauti), Latin ('چم این وازه در زبان لاتین: پیام رسان، فرستاده') and English columns, and a note that the root is akin to IE *nu 'now'.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Avestan / Old Persian\",\n \"words\": \"nard\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The form itself is a real Indo-Iranian verbal root, but it is neither Avestan nor Old Persian, and it does not belong to the root box above. 'nard' is attested in Sanskrit (nard- 'to hum while singing sāmans, to roar, to bellow (of animal, human, cloud)', Brāhmaṇas onwards, EWAia II 22); in Iranian it appears only as a reconstruction *nard 'to lament, moan' (Cheung 282), whose attested reflexes are Middle Persian nāl- (BMP n'l-, MMP n'rysn 'moaning'), Parthian n'r-, Buddhist Sogdian nrδ- 'to lament', Chorasmian nrδ-, NP nālīdan, Baluchi nar-, Kurdish nalīn, Pashto naral. Bartholomae's Altiranisches Wörterbuch has no root nard- at all (the only 'nard' strings in the text are the compound nard.vaipaya- and unrelated sequences), and Kent's Old Persian lexicon has nothing of the kind, so the label 'Avestan / Old Persian' is wrong — Nourai's own source, Abolghasemi (FFD 77), writes 'ایرانی باستان *nard-a', i.e. a reconstructed Old/Proto-Iranian root, not an attested word. Furthermore Cheung treats *nard (p. 282) and *nau(H) (p. 284, = Pokorny's neu- 767) as two different roots and calls *nard 'probably expressive in nature, similar to ME snurtin „to snore“, MHG snarz', giving it no PIE ancestry; so hanging 'nard' under the root box 'Neu' is not supported by modern scholarship.\",\n \"derivation_fa\": \"این صورت ریشه‌ای هندوایرانی و واقعی است، اما نه اوستایی است و نه پارسی باستان، و به ریشهٔ بالا هم تعلق ندارد. nard در سنسکریت گواه دارد (nard- «غریدن، بانگ کردن»، از دورهٔ براهمنه‌ها به بعد) و در ایرانی تنها به صورت بازساخته *nard «نالیدن، مویه کردن» شناخته می‌شود که بازمانده‌های آن فارسی میانهٔ nāl-، پارتی n'r-، سغدی nrδ-، فارسی نو «نالیدن»، بلوچی nar- و پشتوی naral است (چونگ ۲۰۰۷، ص ۲۸۲). در فرهنگ ایرانی باستان بارتولومه هیچ ریشهٔ nard- نیست و در واژه‌نامهٔ پارسی باستان کنت نیز چنین واژه‌ای نیامده؛ خود مرجعی که نورایی می‌آورد (ابوالقاسمی، فعل‌های فارسی دری، ص ۷۷) آن را «ایرانی باستان *nard-a» می‌نامد، یعنی ریشهٔ بازسازی‌شده و نه واژهٔ گواه‌دار. افزون بر این، چونگ *nard (ص ۲۸۲) و *nau(H) (ص ۲۸۴، همان پوکورنی ۷۶۷) را دو ریشهٔ جدا می‌داند و *nard را «آوایی/تقلیدی» می‌شمارد و برای آن نیای هندواروپایی نمی‌سازد؛ پس آویختن nard به ریشهٔ Neu از دید پژوهش امروزی پذیرفتنی نیست: برچسب زبانی نادرست و پیوند با ریشه رد شده است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"FFD:77\", \"status\": \"partial\",\n    \"note\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p. 77 (= pdf p. 82; page image read and transcribed to data/verification/sources/refs/ocr/FFD/77.vision.txt): 'نالیدن — «نالید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است. نال ← فارسی میانه nāl ← ایرانی باستان *nard-a. ... ریشهٔ nard به معنی «بانگ کردن» است.' The page does support a root nard 'to cry out' as the ancestor of nāl-, but it labels it Old/Proto-Iranian (reconstructed), not Avestan or Old Persian, and says nothing about PIE *neu-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, searched for nard-/narəd-\", \"stance\": \"silent\",\n    \"note\": \"grep -n 'nard\\\\b\\\\|narəd' BRT.txt returns only unrelated hits (col. 4425 'an-āpərəšta- ... nard.vaipaya-', and text sequences in Y.34, V.2 etc.); there is no Avestan verbal root nard- in Bartholomae, i.e. the language label of this box has no attestation behind it.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 282 s.v. *nard\", \"stance\": \"partial\",\n    \"note\": \"CHEUNG.txt lines 18605-18640: '*nard “to lament, moan”  *MIDDLE PERSIAN: BMP n'l- /nāl-/ “to lament, moan”, MMP n'rysn “moaning” ... *SOGDIAN: BSogd. nrδ- “to lament” ... *NWIR: NP nālidan/nāl- “to lament” ... *SANSKRIT: nard ... ¶ This apparently Ilr. root is probably expressive in nature'. No Avestan or Old Persian entry, and no PIE line — the root is kept separate from *nau(H) (p. 284).\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 57 s.v. nāl-\", \"stance\": \"partial\",\n    \"note\": \"PHD.txt line 494: 'nāl- [n'l- | P (n'r-), N ~] groan, complain' — the Middle Persian and Parthian stems exist, which is what the reconstructed *nard rests on; MacKenzie of course gives no Avestan form.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon\", \"stance\": \"silent\",\n    \"note\": \"no nard-/nad- root in Kent's lexicon (grep of KNT.txt); the Old Persian half of the label is unattested.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"nâlîdan «نالیدن»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Persian word and its immediate ancestry are right; only the parent box's label and its attachment to *neu- are wrong. NP نالیدن nālīdan, present stem nāl-, continues Middle Persian nāl- 'to groan, complain' (MacKenzie: 'nāl- [n'l- | P (n'r-), N ~] groan, complain'; MMP n'rysn 'moaning'), from Old/Proto-Iranian *nard-a- (Abolghasemi FFD 77; Cheung 282), with the regular Iranian development *-rd- > -l- and compensatory lengthening of the vowel — the same change as Av. sarəδa- 'year' > MP/NP sāl — while Parthian keeps the r (n'r-) and Sanskrit shows the unchanged cluster in nard-. The infinitive in -īdan is a New Persian secondary formation on the present stem ('مادهٔ ماضی جعلی' in Abolghasemi's words). Of the chart's two extras, ناله nāle is the deverbal noun of the same stem, and نال is the present stem nāl- (the homonymous noun نال 'reed, stalk' = Skt naḍa- is a different word: Hübschmann no. 1060). The chart's own NOTE is decisive and modern scholarship is on its side: Hübschmann p. 103 no. 1054, following Geiger, refers nālīdan to Skt nard, and Cheung's *nard does the same — whereas Horn's older grouping of nālīdan with nōyīdan under Skt nav- (no. 1054) is superseded. Hence nālīdan is NOT a descendant of PIE *neu-, and this whole branch is misplaced in the 'Neu' chart.\",\n \"derivation_fa\": \"واژهٔ فارسی و نیای نزدیک آن درست است و تنها برچسب گرهٔ پدر و آویختن آن به ریشهٔ *neu- نادرست است. «نالیدن» با ستاک حال «نال-» از فارسی میانهٔ nāl- «نالیدن، شکایت کردن» می‌آید (مکنزی: «nāl- [n'l- | پارتی n'r-] groan, complain») و آن از ایرانی باستان *nard-a- است؛ در این راه خوشهٔ *-rd- ایرانی در فارسی میانه به «ل» بدل شده و واکه کشیده شده است — همان دگرگونی که اوستایی sarəδa- «سال» را به sāl فارسی رسانده — در حالی که پارتی «ر» را نگه داشته (n'r-) و سنسکریت صورت دست‌نخوردهٔ nard- را دارد. مصدر «نالیدن» ساخت متأخر فارسی نو بر پایهٔ ستاک حال است («مادهٔ ماضی جعلی» به تعبیر ابوالقاسمی). از دو واژهٔ افزودهٔ نمودار، «ناله» اسم‌مصدر همان ستاک است و «نال» خودِ ستاک حال؛ «نالِ» به معنی نی و ساقه واژهٔ دیگری است (هوبشمان، شمارهٔ ۱۰۶۰). یادداشت خود نمودار درست است و پژوهش امروزی آن را تأیید می‌کند: هوبشمان (ص ۱۰۳، شمارهٔ ۱۰۵۴) به پیروی گایگر «نالیدن» را به nard سنسکریت می‌بندد و چونگ نیز همین را می‌گوید؛ پس این شاخه از ریشهٔ *neu- نیست و جای آن در نمودار «Neu» نادرست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"FFD:77\", \"status\": \"supports\",\n    \"note\": \"FFD p. 77 (image transcribed to refs/ocr/FFD/77.vision.txt): 'نال ← فارسی میانه nāl ← ایرانی باستان *nard-a ... ریشهٔ nard به معنی «بانگ کردن» است' — the arrow nālīdan ← nard is exactly what Nourai's reference says.\"},\n   {\"ref\": \"HUB:103\", \"status\": \"supports\",\n    \"note\": \"The chart's NOTE cites HUB:103 and it is verbatim there. HUB.txt leaf 114 (= printed p. 103), no. 1054: 'Np. nalīdan „klagen, seufzen“ stellt Geiger (Etym. und Lautl. des Afgh. Nr. 136) besser zu skr. nard „brüllen, kreischen“, afgh. narəl „heulen, schreien“.' Hübschmann is correcting Horn, and this is the view modern scholarship follows.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. nāl- (PHD.txt line 494; index line 2159 'groan nāl-')\", \"stance\": \"supports\",\n    \"note\": \"'nāl- [n'l- | P (n'r-), N ~] groan, complain' — the Middle Persian stem that NP nālīdan is built on, with the Parthian r-form beside it.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 282 s.v. *nard\", \"stance\": \"supports\",\n    \"note\": \"'*nard “to lament, moan” ... *NWIR: NP nālidan/nāl- “to lament”, Bal. narit/nar-, Kurd. (Kurm.) nalin/nal-, Zaz. nalayis/nalen- ... *SANSKRIT: nard'. Cheung derives nālīdan from *nard, and (p. 284) keeps *nau(H) = Pok. 767 separate.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1054, printed p. 236 (HRN.txt leaf 258)\", \"stance\": \"partial\",\n    \"note\": \"'1054. nöyiden „klagen“ ... nevīden, vergl. nevahiden, nallīden. ai. √nav-, nauti, navate „brüllen (von Tieren)“; vergl. np. zīnüden (No. 672).' Horn lumps nālīdan in with the nav- group; Hübschmann p. 103 explicitly rejects this in favour of nard, and Cheung follows Hübschmann.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi s.v. نالیدن (MON_part2.txt line 72863)\", \"stance\": \"supports\",\n    \"note\": \"'نالیدن: nālīdan (مصل.) (نالید، نالد، ... نالنده، نالان، نالیده، نالش، ناله). ناله کردن، فریاد و فغان کردن ...' — confirms the word and the gloss 'to moan' and lists ناله/نالان as the same family (no etymology in the 2-vol condensation available locally).\"},\n   {\"src\": \"HUB\", \"where\": \"no. 1060, printed p. 103\", \"stance\": \"partial\",\n    \"note\": \"'1060. Np. nal „Rohr, Stengel, Röhre“ — afgh. naṛə f. „Stengel“ = skr. naḍa- „Schilf, Schilfrohr“ = arisch *narda-' — i.e. the noun نال 'reed' is a separate word (Skt naḍa-), so the chart's extra نال must be read as the present stem of nālīdan, not as that noun.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Sanskrit\",\n \"words\": \"nav, navatě, nâuti\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit root nu-/nav- 'to sound, shout, roar, praise' (Ṛgveda onwards): active 3sg nauti (full grade *neu-ti), middle 3sg navate (thematic *new-e-tai), the root cited by Indologists as nav/nu. Pokorny 767 quotes precisely 'Old Indic navate, nauti “sounds, rejoices, praises”' as the first witness of neu-1, Walde-Pokorny II 323 has the same, and Cheung 284 has '*SANSKRIT: nav “to roar, cry” (RV+) = EWAia II: 23'. So the words, the language and the meaning are right, and the descent from PIE *neu(H)- is uncontroversial; only Nourai's spelling 'nâuti' is loose (the vowel is short a + u diphthong: nauti, not nāuti).\",\n \"derivation_fa\": \"ریشهٔ سنسکریت nu-/nav- «بانگ کردن، غریدن، ستودن» از ریگ‌ودا به بعد گواه دارد: صورت گذرای معلوم nauti (درجهٔ کامل *neu-ti) و میانهٔ navate (*new-e-tai). پوکورنی در ص ۷۶۷ همین «navate، nauti: می‌طنَد، شادی می‌کند، می‌ستاید» را نخستین گواه ریشهٔ neu-1 می‌آورد، والده-پوکورنی (جلد ۲، ص ۳۲۳) همان را دارد و چونگ (ص ۲۸۴) نیز «سنسکریت nav «غریدن، گریستن» (از ریگ‌ودا به بعد)» را زیر *nau(H) می‌گذارد. پس واژه‌ها، زبان و معنی درست است و پیوند آن با ریشهٔ هندواروپایی بی‌چون‌وچرا؛ تنها نگارش «nâuti» در کتاب دقیق نیست، زیرا واکهٔ آن a کوتاه به همراه u است (nauti).\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:767\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 62914 (neu-1, Page(s): 767): 'Material: Old Indic navate, nauti “sounds, rejoices, praises”' — the very forms of this node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 323\", \"stance\": \"supports\",\n    \"note\": \"'1. neu- „rufen, preisen“. Ai. navate, nauti „tönt, jubelt, preist“' (WLD_Bd2_pages.txt line 21350).\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 284 s.v. *nau(H)\", \"stance\": \"supports\",\n    \"note\": \"'*SANSKRIT: nav “to roar, cry” (RV+) = EWAia II: 23' and the PIE line '*neu(H)- “to cry out, shout” — LIV: 456 f. | Pok.: 767'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. neu-1\", \"stance\": \"silent\",\n    \"note\": \"Watkins' article lists only the Latin branch ('Suffixed (participial) o-grade form *now-ent-(yo-) ... Latin nūntius'), no Sanskrit, so AHD neither confirms nor denies the Indic forms.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"Persian\",\n \"words\": \"novîdan «نُویدن»; zenūdan «زنودن»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both verbs are genuine New Persian reflexes of the same root, and Cheung's article on *nau(H) lists them together exactly as Nourai draws them. (a) نویدن nōyīdan/navīdan 'to cry aloud, lament' (Shahnameh I 183 v. 986 of the Calcutta ed., cited by Horn no. 1054), beside نوا navā 'plaint, sound, song', continues the Iranian present stem *nau- of *nau(H) 'to cry, wail' with the New Persian -īdan infinitive; the -y-/-v- alternation (nōyīdan ~ navīdan) is the usual glide before the vowel of the suffix. (b) زنودن zinūdan/zunūdan (present zinav-/zunav-, extended zunōyīdan = the chart's زنوییدن, verbal noun زنویه) 'to wail, howl' is the same root with the Old Iranian preverb *uz- 'up, out': *uz-nau- > MP/NP zi-nūd-, i.e. 'to cry out'; Platts & Ranking's Persian grammar analyses the verb the same way ('prefix uz ... zonau-'), and Cheung writes '|| (+ *uz-) NP zinudan/zinav-, zunudan/zunav-, zunoyidan “to wail”'. Horn (no. 672) had already put zīnūden/zunūden 'heulen' with Skt nauti/navate and cross-referred to nōyīden (no. 1054), adding the caveat that Sanskrit nav- is not attested with the preverb ud-. The Labībī verse quoted in the box ('ز درد دل آن شب بدان سان نُوید — که از ناله‌اش ، هیچکس نغنوید') is genuine and comes from Asadi's Loghat-e Fors (it is in FRS and in Mo'in's footnote at Borhan 2209).\",\n \"derivation_fa\": \"هر دو فعل بازماندهٔ راستین همین ریشه در فارسی نو هستند و چونگ در مقالهٔ *nau(H) دقیقاً همان‌ها را در کنار هم آورده است. الف) «نویدن» (nōyīdan/navīdan) «زاری کردن، نالیدن» — گواه آن بیت شاهنامه است (هرن، شمارهٔ ۱۰۵۴، شاهنامهٔ کلکته ۱/۱۸۳ بیت ۹۸۶) — در کنار «نوا» «ناله، آوا»، ادامهٔ ستاک حال ایرانی *nau- است با مصدرساز «-یدن» فارسی نو؛ جابه‌جایی y/v (نویدن ~ نویدن) همان میانجی معمول پیش از واکهٔ پسوند است. ب) «زنودن» (zinūdan/zunūdan، ستاک حال zinav-/zunav-، صورت گستردهٔ zunōyīdan = «زنوییدن» نمودار و اسم «زنویه») همان ریشه است با پیشوند ایرانی باستان *uz- «بر، بیرون»: *uz-nau- > زنود-، یعنی «بانگ برآوردن»؛ پلاتس و رنکینگ در دستور زبان فارسی (ص ۱۹۹) همین تجزیه را دارند («prefix uz ... zonau-») و چونگ می‌نویسد «(+ *uz-) NP zinudan/zinav-, zunudan/zunav-, zunoyidan». هرن (شمارهٔ ۶۷۲) نیز zinūden/zunūden «heulen» را با nauti/navate سنسکریت پیوند داده و به نویدن (۱۰۵۴) ارجاع می‌دهد، با این احتیاط که ریشهٔ nav- سنسکریت با پیشوند ud- گواه ندارد. بیت لبیبی نیز اصیل است و از لغت فرس اسدی می‌آید (در حاشیهٔ برهان قاطع ص ۲۲۰۹ هم نقل شده). ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"HRN:149,236\", \"status\": \"supports\",\n    \"note\": \"Both pages are exactly right. HRN.txt leaf 171 (= printed p. 149) no. 672: 'zīnüden, zunüden „heulen“, Praes. zīnuv-em, zīnöyiden. ai. [√nav-] nauti, návate „brüllen (von Tieren)“, mit accha „zurufen“ (mit ud kommt es nicht vor). Vergl. np. nöyiden etc. (No. 1054).' HRN.txt leaf 258 (= printed p. 236) no. 1054: 'nöyiden „klagen“ (Šahn. I, 183 Vers 986, Calc.), necā „Klage“, nevīden ... ai. √nav-, nauti, návate „brüllen (von Tieren)“; vergl. np. zīnüden (No. 672).'\"},\n   {\"ref\": \"BQT:2209\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in printed p. 2209 (vol 4 scan, pdf p. 292) s.v. نویدن: 'نویدن - بروزن دویدن، بمعنی زاری کردن و نالیدن باشد — و بمعنی حرکت کردن و جنبیدن و لرزیدن هم آمده است', with Mo'in's footnote 9 reproducing Horn: 'هرن گوید: nālīdan (شکایت کردن) (شاهنامه ... ۱۸۳ بیت ۹۸۶؛ کلکته). نوا nawā (شکایت)، nawīdan. هندی باستان nav, nauti, navate (غریدن [جانوران]). قس: فارسی: زنودن «اسشق ۱۰۵۴»', followed by the Labībī verse 'ز درد دل آن شب بدان سان نوید / که از ناله‌اش، هیچکس نغنوید  لبیبی «رشیدی»'. This single page carries both words, both glosses, the Sanskrit comparison and the quoted verse.\"},\n   {\"ref\": \"MON:4859\", \"status\": \"partial\",\n    \"note\": \"Only the 2-volume Adena condensation of Mo'in is available locally and its pages cannot be mapped to the 6-vol pagination, so p. 4859 as such could not be checked. The entry itself is there (MON_part2.txt lines 81143-81150): 'نویدن: navīdan [- ناویدن] (مصل.) جنبیدن، حرکت کردن، لرزیدن' — Mo'in gives نویدن only the 'move, tremble' sense and puts the 'lament' sense under the participle 'نویده: (امذ.) ناله کرده، زاری کرده'; so Mo'in supports the word but distributes the two senses (which Borhan p. 2209 gives to one headword) differently.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"p. 284 s.v. *nau(H)\", \"stance\": \"supports\",\n    \"note\": \"'*NWIR: NP noyidan “to cry aloud, lament”, navidan “to complain, lament” ... NP nōyah “plaint, moan”, NP navā “sound, song; grief, pain” ... || (+ *uz-) NP zinudan/zinav-, zunudan/zunav-, zunoyidan “to wail”' — the modern standard treatment, with Ossetic niwyn, Wakhi nəw-, Shughni naw- 'to weep' as further Iranian cognates.\"},\n   {\"src\": \"GPL\", \"where\": \"Platts & Ranking, Grammar of the Persian Language, printed p. 199 §76\", \"stance\": \"supports\",\n    \"note\": \"GPL.txt (leaf 252) table: 'zi-nu-dan / zu-nu-dan زنودن “to neigh” ... [pr]efix uz ... zonau-' — an explicit analysis of زنودن as *uz- + the root nau-, matching Cheung; p. 98 lists زنودن with present stem زنو.\"},\n   {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors (FRS_pages.txt line 5534)\", \"stance\": \"supports\",\n    \"note\": \"The Labībī verse of the chart stands in Loghat-e Fors: 'ز درد دل آن شب بدان سان نوید / که از ناله اش هیچکس نغنوید' — the source Mo'in's footnote also names (لغت فرس).\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p. 514 ([pdf page 503])\", \"stance\": \"supports\",\n    \"note\": \"The root entry 'نوا، نوانیدن، نویدن (به چم «نغمه»، «خواندن»، «نالیدن»)' lists Persian نویدن with Avestan, Pahlavi, Sanskrit and Latin (nuntius) cognates and cites Borhan-e Qate' — an independent modern Persian source for this very node.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5,\n \"lang\": \"Latin\",\n \"words\": \"nūntium\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin nūntius 'messenger' (n. nūntium 'message') is the standard Italic witness of this root: Watkins reconstructs 'suffixed (participial) o-grade form *now-ent-(yo-), “shouting”' (whence 'announcing' > 'messenger, message'), and the old spelling nountios recorded by Marius Victorinus (GLK VI 13,18) plus the conjectured nouentium in the Carmen Marcianum point to *nowentios. Pokorny 767 admits it with 'perhaps' ('perhaps Latin nuntium “message” (*nouention)'), Cheung 284 lists 'Lat. nuntius “(official) message”' among the IE cognates of *neu(H)-, and de Vaan tentatively favours exactly this derivation from PIE *newH- 'to cry', rejecting the rival contraction from *noventius ‹ novus because '*no(wo)wentio-' makes no morphological sense; Ernout-Meillet, more cautiously, say only 'On ne peut préciser le rapport avec nouus autrement que par des hypothèses incertaines'. The gloss 'message' is right for the neuter nūntium (Servius: 'nuntius est qui nuntiat, nuntium quod nuntiatur'). One inaccuracy: the vowel is long, nūntium, where the book prints a breve (nŭntium).\",\n \"derivation_fa\": \"لاتینی nūntius «پیام‌آور» (و صورت خنثای nūntium «پیام») گواه ایتالیکی این ریشه است: واتکینز آن را از «صورت وصفی درجهٔ o با پسوند، *now-ent-(yo-) به معنی «بانگ‌زننده»» می‌سازد که از آن «آگاهی‌دهنده» و سپس «پیام‌آور، پیام» برآمده است؛ نگارش کهن nountios (به گواهی ماریوس ویکتورینوس) و صورت حدسی nouentium در سرودهٔ مارکیوس نیز به *nowentios راه می‌برد. پوکورنی (ص ۷۶۷) آن را با قید «شاید» می‌پذیرد، چونگ (ص ۲۸۴) nuntius را در شمار هم‌ریشه‌های هندواروپایی *neu(H)- می‌آورد و دُ وان نیز همین بازسازی از *newH- «بانگ زدن» را با احتیاط ترجیح می‌دهد و ریشه‌شناسی رقیب (از novus، *noventius) را به دلیل ناهمسازی ساختواژی رد می‌کند؛ ارنو-مِیه محتاط‌تر می‌گویند که «پیوند آن با nouus را جز با فرض‌های نامطمئن نمی‌توان روشن کرد». معنی «پیام» برای صورت خنثای nūntium درست است (سرویوس: nuntius کسی است که خبر می‌دهد و nuntium آن چیزی که خبر داده می‌شود). تنها خطای کوچک، کوتاه نشان دادن واکهٔ نخست است: nūntium با «او»ی کشیده.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/nuntius\"],\n \"ref_check\": [\n   {\"ref\": \"POK\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 62916 (neu-1, p. 767): 'perhaps Latin nuntium “message! announcement; news; notice of divorce” (*nouention)'. Pokorny's 'perhaps' is worth keeping: the Latin link is the least secure member of the article.\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. neu-1 (AHD_watkins1985.txt line 785): 'Suffixed (participial) o-grade form *now-ent-(yo-), “shouting,” in Latin nūntius, “announcing,” hence a messenger, also a message, and nūntium, message'. Nourai's box (form, gloss 'message') is taken straight from here.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. nuntius (LAT.txt line 42469 ff.)\", \"stance\": \"partial\",\n    \"note\": \"'nuntius (forme ancienne nountios d'après Mar. Victor. GLK VI 13,18 ...): mot qui sert à la fois d'adjectif ... et de substantif: nūntius,-i m. “messager” et “message” ... nūntium n. “message”, d'après Servius ... On ne peut préciser le rapport avec nouus autrement que par des hypothèses incertaines.' Supports form and meaning; leaves the etymology open (and thinks first of nouus, not of *neu-).\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 323 s.v. 1. neu-\", \"stance\": \"silent\",\n    \"note\": \"Walde-Pokorny's article on neu- 'rufen, preisen' lists only Ai. navate/nauti and OIr. nuall — the Latin word is not yet part of the root in 1927.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p. 284 s.v. *nau(H), *IE COGNATES\", \"stance\": \"supports\",\n    \"note\": \"'*IE COGNATES: Toch. nu- “to cry out; threaten”, Lat. nuntius “(official) message”, OIrish nuall “cry, alarm, proclamation”'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. nuncio / announce\", \"stance\": \"supports\",\n    \"note\": \"Klein derives the English family 'fr. L. annuntiare ... fr. ad- and nuntiare, “to relate, report”, fr. nuntius, “messenger”' (KLN_1966.txt s.v. announce), i.e. the same Latin base word.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6,\n \"lang\": \"English\",\n \"words\": \"announce, pronounce\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both are Latin verbs in nūntiare 'to report', taken into English through French. announce: ME anounce, from Old French anoncer (mod. annoncer), from Latin annūntiare (ad- + nūntiare) 'to announce, relate'; pronounce: ME pronouncen, from OF pronuncier/prononcier (mod. prononcer), from Latin prōnūntiare 'to make publicly known, tell, announce'. Watkins lists exactly this English set under neu-1 ('NUNCIO; ANNOUNCE, DENOUNCE, ENUNCIATE, PRONOUNCE, RENOUNCE'), and Klein gives the chain word by word; the borrowings entered Middle English in the 14th-15th c. through Anglo-French legal and ecclesiastical usage.\",\n \"derivation_fa\": \"هر دو واژه از فعل لاتینی nūntiare «خبر دادن» می‌آیند و از راه فرانسه به انگلیسی رسیده‌اند: announce از انگلیسی میانهٔ anounce، از فرانسهٔ کهن anoncer، از لاتینی annūntiare (ad- + nūntiare)؛ و pronounce از انگلیسی میانهٔ pronouncen، از فرانسهٔ کهن pronuncier، از لاتینی prōnūntiare «آشکارا اعلام کردن». واتکینز همین مجموعهٔ انگلیسی را زیر ریشهٔ neu-1 می‌آورد (NUNCIO; ANNOUNCE, DENOUNCE, ENUNCIATE, PRONOUNCE, RENOUNCE) و کلاین زنجیرهٔ واژه‌به‌واژه را می‌دهد؛ وام‌گیری در سدهٔ چهاردهم و پانزدهم از راه کاربرد حقوقی و کلیسایی انگلیسی-فرانسوی رخ داده است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n    \"note\": \"The English box carries no reference in the book; Klein and Watkins were consulted instead (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. announce, pronounce\", \"stance\": \"supports\",\n    \"note\": \"'announce, tr. v. — ME. anounce, fr. OF. anoncer (F. annoncer), fr. L. annuntiare, “to announce, relate”, fr. ad- and nuntiare, “to relate, report”, fr. nuntius, “messenger”.' — 'pronounce, tr. and intr. v. — ME. pronouncen, fr. OF. pronuncier, prononcier (F. prononcer), fr. L. prōnuntiare, “to make publicly known, tell, announce, pronounce”, fr. 1st pro- and nūntid[re]'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. neu-1 and index (AHD_watkins1985.txt lines 785, 1246, 1946)\", \"stance\": \"supports\",\n    \"note\": \"The article's word list ends 'NUNCIO; ANNOUNCE, DENOUNCE, ENUNCIATE, PRONOUNCE, RENOUNCE', and the reverse index has 'ANNOUNCE neu-1', 'NUNCIO neu-1'.\"}\n ]\n})\n\njson.dump(e0, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/e0.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(e0[\"nodes\"]))\nPY\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk363a.py"
}
```


### [2026-09-07T19:47:54.508Z] TOOL RESULT

```
ok 6
```


## [2026-09-07T19:51:54.562Z] TOOL CALL #82: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk363b.py <<'PY'\n# -*- coding: utf-8 -*-\nimport json\n\ne2 = {\n \"entry\": 2,\n \"root\": \"Newn\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₁néwn̥ 'nine' (Pokorny 318-319 'e-neuen, neun, enun'; Watkins/AHD 'newn'; Walde-Pokorny I 128)\",\n \"note\": \"Root, language label and gloss are all correct, and Nourai's root name 'Newn' is Watkins' spelling of the lemma. Pokorny pp. 318-319 'Root/lemma: e-neuen, neun, enun  Meaning: nine' has the whole chart in one article: 'Old Indic nava, Avestan nava (neun) “9”; ... Latin novem “nine” (-m for -n after septem, decem); Gothic Old High German niun ... Old English nigon (from *niuwun); ordinals: *neueno- in Latin nonus ... Old Indic navama-, Avestan naoma-, Old pers. navama-'. (Caution: the local POK_full.txt is the annotated 'dnghu' English rendering, whose interpolated 'Note:' paragraphs about Albanian/Lycian are the editor's, not Pokorny's; the Material and Page(s) lines are Pokorny's.) Wiktionary's reconstruction page gives PIE *h₁néwn̥ > PII *Hnáwa > Avestan/Old Persian, Latin novem, Proto-Germanic *newun, and notes that the old idea of a link with *néwos 'new' (Pokorny: 'One assumes connection with *neuo- “new”, because a new countable segment has begun with 9') is now doubted, since the prothetic vowels of Greek ennéa and Armenian inn are explained as reflexes of initial *h₁-.\",\n \"note_fa\": \"ریشه، برچسب زبانی و معنی هر سه درست است و نام «Newn» همان صورتی است که واتکینز برای این ریشه به کار می‌برد. پوکورنی در ص ۳۱۸–۳۱۹ زیر «e-neuen, neun, enun» با معنی «نه» همهٔ شاخه‌های نمودار را در یک مقاله آورده است: «سنسکریت nava، اوستایی nava «۹»؛ ... لاتینی novem (که -m آن به قیاس septem و decem است)؛ گوتی و آلمانی علیای کهن niun، انگلیسی کهن nigon؛ و ترتیبی‌ها: *neueno- در لاتینی nonus، سنسکریت navama-، اوستایی naoma-، پارسی باستان navama-». (یادآوری: نسخهٔ محلی POK_full ترجمهٔ انگلیسی حاشیه‌دار است و بندهای «Note» دربارهٔ آلبانی و لوکیایی از ویراستار است، نه از پوکورنی.) در بازسازی امروزی این ریشه *h₁néwn̥ است و از آن هندوایرانی *Hnáwa و سپس صورت‌های اوستایی و پارسی باستان، لاتینی novem و ژرمنی آغازین *newun برآمده‌اند؛ پیوند دیرین آن با *néwos «نو» امروز مشکوک است، زیرا واکهٔ آغازی یونانی ennéa و ارمنی inn را بازماندهٔ *h₁- می‌دانند. تنها ایرادهای نمودار در گره‌های ۱ تا ۳ و ۵ است (بنگرید به آنجا).\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁néwn̥\"],\n \"ref_check\": [\n   {\"ref\": \"POK:318\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt lines 26516-26600: 'Root / lemma: e-neuen, neuo, enuo  Meaning: nine ... Material: Old Indic nava, Avestan nava (neun) “9” ... References: WP. I 128, Feist 378 f., Schwyzer Gr. Gr. I 590 f.  Page(s): 318-319'. The cited page is right.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 128 s.v. 'eneuen, neun, enun „neun“'\", \"stance\": \"supports\",\n    \"note\": \"incoming/WLD/WLD_Bd1_pages.txt line 11556 ff.: 'Ai. náva, av. nava „9“: arm. inn „9“ ... ai. navatí-, av. navaiti- f. „90“, eigentlich Neunzahl von Zehnern; lat. novem „9“ (-m lautgesetzlich aus -n? sonst nach septem, decem); got. ahd. niun, anord. nio „9“, as. nigun, afries. ni(u)gun, ags. nigon ... Ordinale: *noueno- in lat. nonus ... ai. navamá-, av. naoma-; ap. navama-'. One article covering the root and nodes #1, #4, #5, #7.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. newn (AHD_watkins1985.txt lines 786-787)\", \"stance\": \"supports\",\n    \"note\": \"'newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nōnus, ninth: NONA-, NONES, NOON ... [Pok. e-neuen 318.]' — this is the source of Nourai's root name and of his Germanic and Latin boxes.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, An Indo-European Comparative Dictionary, s.vv. 'enneun' and 'neun'\", \"stance\": \"supports\",\n    \"note\": \"IEC.txt line 3611: 'enneun (enneunti) “nine”. WP I, 128. Cf. neun  Skt. náva, návan; Av. nava; Per. nuh; Kurd. nō ... Lat. novem ...'; line 11727: 'neun (en-neun, -neum) “nine”  Skt. nava; Av. nava, id. beside naumə “ninth” ...; Per. nuh; Lat. novem (infl. of decem for final cons.)'. Mann too puts Persian nuh directly beside Avestan nava.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, numeral table in the front matter ([pdf page 18-19])\", \"stance\": \"supports\",\n    \"note\": \"The comparative numeral table has Persian '۹ noh' in one row with neuf / neun / negen / nio, and Irish naoi, Welsh naw, Greek ennea, Latin novem, Italian nove — the same cognate set.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"nava 1, nauma; navaiti; nava-dasa\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The forms are all genuine Avestan, but two of the three glosses are off. (a) nava (indeclinable) '9' is right — Bartholomae: 'j. nava indekl. Zw. „neun“ ... Ableit. — ai. náva ...  Pü.: nōh', with Y 9.35, Yt 10.11, V 2.30 etc.; it continues PIE *h₁néwn̥ via PII *Hnáwa (final *-n̥ lost/vocalised in Indo-Iranian). (b) nauma-/naoma- is NOT 'nine' but the ORDINAL 'ninth': Bartholomae has 'p. navama-, j. naoma-, nāuma- Adj. (fem. -mī-) „der neunte“' (Yt 19.2, Y 1.7, V 5.28), i.e. it belongs with the Old Persian box #4, not with the cardinal. (c) nava-dasa: the attested Young Avestan word is navadasa- adj. 'the nineteenth', formed from an indeclinable *nava.dasa '19' (Bartholomae: 'j. nava.dasa- Adj. „der neunzehnte“ ... Ableit. aus *nava.dasa indekl. Zw. „19“ ... Pü.: navazdahom'); so glossing it 'nineteen' describes the underlying numeral rather than the attested adjective. (d) navaiti- f. '90' is right and is literally 'a nineness (of tens)' (Walde-Pokorny I 128: 'ai. navatí-, av. navaiti- f. „90“, eigentlich Neunzahl von Zehnern'), cf. the derived adjective navaiti-vant- 'ninetyfold' (Yt 10).\",\n \"derivation_fa\": \"همهٔ صورت‌ها اوستایی راستین‌اند، اما دو معنی از سه معنی دقیق نیست. الف) nava (بی‌صرف) «۹» درست است؛ بارتولومه می‌آورد: «j. nava indekl. Zw. „neun“ ... سنسکریت náva ... پهلوی nōh» با شواهد یسنا ۹/۳۵ و یشت ۱۰/۱۱ و وندیداد ۲/۳۰؛ و آن بازماندهٔ *h₁néwn̥ هندواروپایی از راه هندوایرانی *Hnáwa است. ب) nauma-/naoma- معنی «نه» ندارد، بلکه عدد ترتیبی «نهم» است: بارتولومه «پارسی باستان navama-، اوستایی naoma-، nāuma- صفت «نهم»» دارد؛ پس جای آن در کنار گرهٔ پارسی باستان (شمارهٔ ۴) است، نه در کنار عدد اصلی. ج) nava-dasa: صورت گواه‌دار اوستایی نو navadasa- به معنی «نوزدهم» است که از عدد بی‌صرف *nava.dasa «۱۹» ساخته شده (بارتولومه: «... Pü.: navazdahom»)؛ پس معنی «نوزده» به عدد پایه بازمی‌گردد نه به صفت گواه‌دار. د) navaiti- «۹۰» درست است و تحت‌اللفظ «نُه‌گانِ دهگان» است (والده-پوکورنی، جلد ۱، ص ۱۲۸)، چنان‌که صفت navaiti-vant- «نودگانه» نیز گواه دارد. در مجموع ادعای نورایی با اصلاح این دو معنی پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:318\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt lines 26527, 26548, 26598 (pp. 318-319): 'Old Indic nava, Avestan nava (neun) “9”'; '... and Old Indic navatí-, Avestan navaiti- f. “90”, actually nine of tens'; 'ordinals: *neueno- ... Old Indic navama-, Avestan naoma-, Old pers. navama-' — Pokorny's article has nava, navaiti- and naoma- exactly, but naoma- as an ORDINAL.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW cols. ~1055-1057 (BRT.txt lines 18613, 18628-18634, 18645, 18522)\", \"stance\": \"partial\",\n    \"note\": \"'j. nava indekl. Zw. „neun“ ... Pü.: nōh'; 'j. navaiti-vant- Adj. „neunzigfältig“'; 'j. nava.dasa- Adj. „der neunzehnte“ ... Ableit. aus *nava.dasa indekl. Zw. „19“ ... Pü.: navazdahom'; 'p. navama-, j. naoma-, nāuma- Adj. (fem. -mī-) „der neunte“'; 'j. naoma- Adj. (fem. -mī-): s. unter navama-'. Supports the forms, contradicts the glosses 'nauma = nine' and (strictly) 'nava-dasa = nineteen'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 128\", \"stance\": \"supports\",\n    \"note\": \"'ai. náva, av. nava „9“ ... ai. navatí-, av. navaiti- f. „90“, eigentlich Neunzahl von Zehnern ... Ordinale: ... av. naoma-'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon s.v. navama-\", \"stance\": \"supports\",\n    \"note\": \"'navama- adj. “ninth”: Av. naoma-, Skt. navamá-, pAr. navama- remade from pIE neweno- after pAr. dasama- “tenth”' — independent confirmation that Avestan naoma-/nāuma- is the ordinal 'ninth'.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"naum\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The form is real but it is the ORDINAL, and it has no gloss in the chart. Nourai took it from the page he cites: Mo'in's footnote 8 to برهان قاطع p. 2210 lists 'پهلوی naum' among the cognates of نه. That transliteration is Horn's reading (Grundriss no. 1056: 'phlv. nawm'); the Book-Pahlavi spelling is ⟨nhwm⟩, which MacKenzie reads nohom 'ninth' ('nohom [nhwm | = M, N ~] ninth') and Nyberg nahom/nohom ('nahom [nhwm], nohom [nhwwm] the ninth. — MPrth nhwm; MPrs nw(w)m; NP nuhum'), from Avestan naoma-/OIr. *navama-. The Middle Persian CARDINAL 'nine' is a different word: MacKenzie 'nē [TA < A tšʿ | M nwh, N nuh] nine' (i.e. Book Pahlavi writes it with the Aramaic ideogram, Manichaean MP has nwh = nō/nuh), and Bartholomae's Pahlavi equivalent of Av. nava is likewise 'Pü.: nōh'. So 'naum' is a genuine Pahlavi word ('ninth', older reading naum/nāwom of nohom), but as drawn — the link between Avestan nava and Persian noh — it is the wrong word; see node #3.\",\n \"derivation_fa\": \"این صورت واقعی است، اما عدد ترتیبی است و در نمودار هیچ معنایی برایش نیامده. نورایی آن را از همان صفحه‌ای که ارجاع می‌دهد گرفته است: حاشیهٔ ۸ معین بر برهان قاطع ص ۲۲۱۰ در شمار هم‌ریشه‌های «نه» «پهلوی naum» را می‌آورد؛ و این آوانگاری از خوانش هرن است (Grundriss، شمارهٔ ۱۰۵۶: «phlv. nawm»). نگارش پهلوی کتابی ⟨nhwm⟩ است که مکنزی آن را nohom «نهم» می‌خواند و نیبرگ nahom/nohom («پارتی nhwm؛ فارسی میانه nw(w)m؛ فارسی نو نهم»)، و ریشهٔ آن اوستایی naoma- است. اما عدد اصلی «نه» در فارسی میانه واژهٔ دیگری است: مکنزی «nē [با هزوارش آرامی | مانوی nwh، فارسی نو nuh] nine» و بارتولومه نیز برابر پهلوی nava اوستایی را «Pü.: nōh» می‌دهد. پس naum واژه‌ای راستین پهلوی («نهم»، خوانش کهن‌تر nohom) است، ولی در جایی که نمودار گذاشته — حلقهٔ میان nava اوستایی و «نه» فارسی — واژهٔ نادرستی است (بنگرید به گرهٔ ۳).\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:2210\", \"status\": \"supports\",\n    \"note\": \"Printed p. 2210 of Borhan-e Qate' ed. Mo'in (vol 4 scan, pdf p. 293; page image read and transcribed to data/verification/sources/refs/ocr/BQT/2210.vision.txt), footnote 8 to نه: 'پارسی باستان navama- (نهم)، اوستا nava، nâuma-، naoma- (نهم)، پهلوی naum، هندی باستان náva، ارمنی inn ... «اسشق ۱۰۵۶»؛ و رک: هوبشمان ۱۰۵۶ ... پهلوی nah، ایرانی باستان nava-، بقرابت «ده» dah ساخته شده. فارسی جدید nuh از nôh از nava- با h بقیای dah «نیبرکه ص ۱۵۴»'. The page does contain 'پهلوی naum', so the citation is accurate; note however that the same footnote derives NP nuh from nôh < *nava-, not from naum.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.vv. nē, nohom, nawad, nōzdah (PHD.txt lines 501, 516)\", \"stance\": \"partial\",\n    \"note\": \"'nē [TA < A tšʿ | M nwh, N nuh] nine'; 'nohom [nhwm | = M, N ~] ninth'; 'nawad [90 | N ~] ninety'; 'nōzdah [nwzdh | N ~] nineteen'. MacKenzie's Pahlavi cardinal is nō/nē, and ⟨nhwm⟩ is read nohom 'ninth' — so 'naum' belongs to the ordinal series.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. nahom/nohom (NYB_vol2_glossary.txt line 2614)\", \"stance\": \"partial\",\n    \"note\": \"'nahom [nhwm], nohom [nhwwm] the ninth. — MPrth nhwm; MPrs nw(w)m; NP nuhum.' Same conclusion: the word is the ordinal, and its New Persian outcome is نهم, not نه.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1056, printed p. 236\", \"stance\": \"partial\",\n    \"note\": \"'1056. nuh (geschrieben nah) „neun“. ap. navama- „neunter“; aw. nava, nāuma-, naoma- „neunter“; phlv. nawm; ai. náva; arm. inn ... Np. nuhum ist eine ganz junge Bildung, die man nicht auf das Pehlevī übertragen darf.' Horn is the ultimate source of the 'nawm/naum' form that Mo'in and then Nourai print, and he too keeps it apart from the cardinal.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae s.v. nava (BRT.txt line 18629)\", \"stance\": \"contradicts\",\n    \"note\": \"Under Av. nava '9' Bartholomae gives the Pahlavi equivalent as 'Pü.: nōh', not naum — i.e. the Pahlavi link between Av. nava and NP noh is nōh.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"noh «نُه»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The word and its ultimate origin are right, but the route drawn through the ordinal is not what the sources — including Nourai's own — say. NP نه noh 'nine' continues the Middle Persian CARDINAL nō/nuh (Book Pahlavi writes it with the Aramaic ideogram ⟨TA⟩, Manichaean MP nwh; MacKenzie 'nē ... | M nwh, N nuh] nine'; Bartholomae 'Pü.: nōh'), from Old Iranian *nava (Av. nava, OP nava), from PIE *h₁néwn̥. The audible final -h is not the -m of the ordinal naum/nohom: Hübschmann (Persische Studien no. 1056, p. 103) states 'Np. nuh „neun“ hat sein hörbares h ... offenbar von dah „zehn“ erhalten wie hašt „acht“ sein anlautendes h von haft „sieben“', and Mo'in's footnote on the very page Nourai cites for the Pahlavi box (BQT 2210) says the same: 'فارسی جدید nuh از nôh از nava- با h بقیای dah'. Horn adds that 'Np. nuhum ist eine ganz junge Bildung, die man nicht auf das Pehlevī übertragen darf' — the modern ordinal نهم is the late continuation of nohom, while نه descends from the cardinal. Wiktionary likewise takes Persian نه straight from Middle Persian/Old Persian nava. The chart's extras are correct: نود navad '90' < MP nawad < Av. navaiti-, and نوزده nūzdah '19' < MP nōzdah/navazdah < Av. *nava.dasa (BQT 2195: 'پهلوی navazdah (nôzdah) ... اوستا navadasa- (نوزدهم)').\",\n \"derivation_fa\": \"واژه و خاستگاه نهایی آن درست است، اما راهی که نمودار از عدد ترتیبی می‌کشد با منابع — از جمله منبع خودِ نورایی — سازگار نیست. «نُه» فارسی ادامهٔ عدد اصلی فارسی میانه nō/nuh است (در پهلوی کتابی با هزوارش آرامی نوشته می‌شد و در فارسی میانهٔ مانوی nwh؛ مکنزی: «nē ... | مانوی nwh، فارسی نو nuh] nine»؛ بارتولومه: «Pü.: nōh»)، و آن از ایرانی باستان *nava (اوستایی nava، پارسی باستان nava) و سرانجام از *h₁néwn̥ هندواروپایی. «ه»ی پایانی نیز بازماندهٔ «م»ی عدد ترتیبی نیست: هوبشمان (پژوهش‌های فارسی، شمارهٔ ۱۰۵۶، ص ۱۰۳) می‌گوید «نُه» این «ه»ی شنیدنی را به قیاس «دَه» گرفته است، همچنان که «هشت» «ه»ی آغازینش را از «هفت»؛ و حاشیهٔ معین در همان صفحه‌ای که نورایی برای گرهٔ پهلوی ارجاع می‌دهد (برهان ۲۲۱۰) همین را می‌گوید: «فارسی جدید nuh از nôh از nava- با h بقیای dah». هرن نیز می‌افزاید که «نهم» ساختی بسیار متأخر است و نباید آن را به پهلوی برگرداند. پس پژوهش امروزی حلقهٔ «نُه ← naum» را رد می‌کند و به جای آن nō/nuh فارسی میانه را می‌گذارد، هرچند سرچشمهٔ نهایی همان است. واژه‌های افزودهٔ نمودار درست‌اند: «نود» از nawad پهلوی و اوستایی navaiti-، و «نوزده» از nōzdah/navazdah پهلوی و اوستایی *nava.dasa.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%86%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:2195\", \"status\": \"partial\",\n    \"note\": \"Printed p. 2195 (vol 4 scan, pdf p. 278; image read, transcribed to refs/ocr/BQT/2195.vision.txt) is the page of نوزده, not of نه: its footnote 8 reads 'نوزده = نوازده «اسشق ۱۰۴۸» ... بضم اول و فتح دال، پهلوی navazdah (nôzdah) «نیبرکه ص ۱۵۵»، اوستا navadasa- (نوزدهم)، هندی باستان návadasa (نوزده) ... عدد نه بعلاوهٔ ده، عدد بین هیجده و بیست'. It therefore supports the chart's extra نوزده but not the headword نه, whose etymological footnote stands on p. 2210 — and that footnote derives nuh from nôh < *nava-, i.e. contradicts the arrow noh ← naum.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 1056, printed p. 103 (HUB.txt leaf 114)\", \"stance\": \"supports\",\n    \"note\": \"'1056. Np. nuh „neun“ hat sein hörbares h (ZDMG. 38, 97, vgl. paz. nuh „neun“, nahum „der neunte“ Min. Gl. 142, 147, Shk. 260, jüd. tat. nuf aus nuh, kas. nuh-do) offenbar von dah „zehn“ erhalten wie hašt „acht“ sein anlautendes h von haft „sieben“.' — the -h is analogical from dah, and Pazand keeps nuh (cardinal) and nahum (ordinal) apart.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. nē (PHD.txt line 516)\", \"stance\": \"supports\",\n    \"note\": \"'nē [TA < A tšʿ | M nwh, N nuh] nine' — the Middle Persian cardinal, with Manichaean nwh and New Persian nuh as its continuation.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1056, printed p. 236\", \"stance\": \"supports\",\n    \"note\": \"'1056. nuh (geschrieben nah) „neun“. ap. navama- „neunter“; aw. nava, nāuma-, naoma- „neunter“; phlv. nawm; ai. náva ... Np. nuhum ist eine ganz junge Bildung, die man nicht auf das Pehlevī übertragen darf.' Horn's headword is the cardinal nuh derived from Av. nava; the -m form is listed as the ordinal.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.vv. enneun / neun\", \"stance\": \"supports\",\n    \"note\": \"'enneun ... Av. nava; Per. nuh' and 'neun ... Av. nava, id. beside naumə (ninth ...); Per. nuh' — Mann too places Persian nuh under the cardinal and naumə under the ordinal.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, numeral table ([pdf page 18])\", \"stance\": \"supports\",\n    \"note\": \"Persian '۹ noh' stands in the cognate row with neuf, neun, negen, nio, novem, ennea — no ordinal intermediary.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"Old Persian\",\n \"words\": \"navama\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian navama- 'ninth' is well attested: nom. sg. m. navama in Darius' Bisitun inscription DB 1.10 (and DBa 10f.), 'VIII manā taumāyā tyaiy paruvam xšāyaθiyā āha; adam navama' = 'eight of my family were formerly kings; I (am) the ninth'. Kent's lexicon: 'navama- adj. “ninth”: Av. naoma-, Skt. navamá-, pAr. navama- remade from pIE neweno- after pAr. dasama- “tenth” ... cf. Lt. nōnus'; Bartholomae files it together with Av. naoma-/nāuma- 'der neunte'. The gloss 'ninth' in the chart is right, and the ordinal is a regular derivative of the numeral in the root box (PIE ordinal *newn-o-/*neweno-, remodelled in Indo-Iranian after *dasama- 'tenth'). Nourai's page reference is also accurate: Mo'in's footnote at Borhan 2210 opens 'پارسی باستان navama- (نهم)'.\",\n \"derivation_fa\": \"«navama-» پارسی باستان به معنی «نهم» گواه استوار دارد: صورت نهادی مفرد نرینهٔ navama در سنگ‌نوشتهٔ بیستون داریوش (DB ۱/۱۰) آمده است: «هشت کس از تبار من پیش‌تر شاه بودند؛ من نهمین‌ام». کنت در واژه‌نامهٔ خود می‌نویسد: «navama- صفت «نهم»: اوستایی naoma-، سنسکریت navamá-، هندوایرانی آغازین navama- که از *neweno- هندواروپایی به قیاس dasama- «دهم» بازساخته شده است؛ قس لاتینی nōnus»؛ بارتولومه نیز آن را با naoma-/nāuma- اوستایی در یک مدخل می‌آورد. پس معنی «نهم» در نمودار درست است و این عدد ترتیبی برساختهٔ قاعده‌مند همان عدد اصلیِ خانهٔ ریشه است. ارجاع نورایی هم دقیق است: حاشیهٔ معین در برهان ۲۲۱۰ با «پارسی باستان navama- (نهم)» آغاز می‌شود.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:2210\", \"status\": \"supports\",\n    \"note\": \"Footnote 8 to نه, printed p. 2210 (transcribed in refs/ocr/BQT/2210.vision.txt): 'پارسی باستان navama- (نهم)، اوستا nava، nâuma-، naoma- (نهم)، پهلوی naum ...' — the Old Persian form and its gloss are on the cited page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon s.v. navama- (KNT.txt line 5603) and §§ on numerals (line 2364)\", \"stance\": \"supports\",\n    \"note\": \"'navama- adj. “ninth”: Av. naoma-, Skt. navamá-, pAr. navama- remade from pIE neweno- after pAr. dasama- “tenth” (§149II, §204IV), cf. Lt. nōnus.  navama nsm. DB 1.10; DBa 10f.'; and 'IV. Nine: nsm. navama “ninth” is identical with Skt. navamá-s ... The -n- in “nine” is seen in the Lt. ordinal nōnus, from *nouenos.'\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. navama- (BRT.txt line 18645)\", \"stance\": \"supports\",\n    \"note\": \"'p. navama-, j. naoma-, nāuma- Adj. (fem. -mī-) „der neunte“; H 8 manā taumāyā tyaiy xšāyaθiyā āha adam °maiy Bh. i. 3 ...' — the Old Persian ordinal with the Bisitun passage.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 128 (ordinals)\", \"stance\": \"supports\",\n    \"note\": \"'Ordinale: *noueno- in lat. nonus ... ai. navamá-, av. naoma-; ap. navama-, air. nomad, cymr. nawfed'.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 5,\n \"lang\": \"Germanic\",\n \"words\": \"niwum\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"niwum\",\n \"correct_form\": \"niwun (Watkins) / Proto-Germanic *newun\",\n \"derivation\": \"The derivation is right but the form has a misprinted final letter. The node's only reference, Watkins/AHD, prints 'newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH' — with -n, not -m; the standard reconstruction today is Proto-Germanic *newun (Wiktionary s.v. *h₁néwn̥; Kroonen), and no Germanic form in -m exists (Gothic niun, OHG niun, ON níu, OS nigun, OFris. ni(u)gun, OE nigon 'from *niuwun' per Pokorny). The 300-dpi image of the printed page (copied to data/verification/sources/refs/ocr/BOOK/363.png) clearly shows 'niwum : nine', so the JSON extraction is faithful and the error is Nourai's own misprint (an -m for -n, perhaps by contamination from the Latin novem in the box below). Phonologically: PIE *h₁néwn̥ > PGmc *newun/*niwun (loss of the initial laryngeal, syllabic *n̥ > un) > OE nigon with an inserted glide g (as in OS nigun, OFris. niugun), Goth./OHG niun.\",\n \"derivation_fa\": \"خودِ اشتقاق درست است، اما واپسین حرفِ صورت غلط چاپ شده است. تنها مرجع این گره، یعنی واتکینز (پیوست AHD)، می‌نویسد: «newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon» — با «ن» و نه «م»؛ بازسازی امروزی ژرمنی آغازین *newun است و هیچ صورت ژرمنی با «م» وجود ندارد (گوتی niun، آلمانی علیای کهن niun، نورس کهن níu، ساکسون کهن nigun، انگلیسی کهن nigon از *niuwun). تصویر ۳۰۰ نقطه‌ای صفحهٔ چاپی (نگاه کنید به BOOK/363.png) به‌روشنی «niwum : nine» را نشان می‌دهد؛ پس خوانش داده‌ها درست است و خطا از خودِ کتاب است (احتمالاً به تأثیر novem لاتینی در خانهٔ زیر). از نظر آوایی: *h₁néwn̥ > ژرمنی *newun (با از میان رفتن حنجره‌ای آغازی و شدن *n̥ هجایی به un) > انگلیسی کهن nigon با میانجی g، و گوتی/آلمانی کهن niun. خطای چاپی کتاب.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁néwn̥\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins 1985 s.v. newn (AHD_watkins1985.txt line 787): 'newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH.' The reference supports the node's content but prints *niwun; the book's 'niwum' does not correspond to anything in AHD.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. nine\", \"stance\": \"supports\",\n    \"note\": \"'nine, adj. — ME. nigen, nine, fr. OE. nigon, nigan, rel. to OS. nigun, OFris. niugun, nigun, ON. níu, Dan. ni, Swed. nio ... OHG., MHG. niun, G. neun, Goth. niun, “nine”, and cogn. with OI. nava, Avestic nava, Toch. ñu, Arm. inn ... L. novem (for *noven)' — no Germanic form in -m.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 128\", \"stance\": \"supports\",\n    \"note\": \"'got. ahd. niun, anord. nio „9“, as. nigun, afries. ni(u)gun, ags. nigon' — the Germanic series, all in -n.\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny p. 318\", \"stance\": \"supports\",\n    \"note\": \"'Gothic Old High German niun, Proto Norse niu, Old Norse nio “9”, Old Saxon nigun, Old Frisian ni(u)gun, Old English nigon (from *niuuun)' — again *niwun with -n.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 6,\n \"lang\": \"English\",\n \"words\": \"nine, ninety, nineteen\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three are inherited (not borrowed) Germanic numerals: OE nigon > ME nigen/nine > nine; OE nigontig ('nine tens', with the -tig suffix) > ME nigenty/nyneti > ninety; OE nigontīene/nigontȳne > ME nigentene/nynetene > nineteen. Klein gives exactly these chains ('ninety, adj. — ME. nigenty, nyneti, fr. OE. nigontig. See nine and the numeral suff. -ty'; 'nineteen, adj. — ME. nigentene, nynetene, fr. OE. nigontiene, nigontyne'), and Watkins puts NINE, NINETEEN, NINETY, NINTH under Germanic *niwun. The intervocalic g of OE nigon was lost in Middle English, giving the long ī of modern nine.\",\n \"derivation_fa\": \"هر سه واژه میراثی ژرمنی‌اند و وام‌واژه نیستند: انگلیسی کهن nigon > انگلیسی میانهٔ nigen/nine > nine؛ انگلیسی کهن nigontig («نُه دهگان»، با پسوند -tig) > nigenty/nyneti > ninety؛ و انگلیسی کهن nigontīene > nigentene/nynetene > nineteen. کلاین همین زنجیره‌ها را واژه‌به‌واژه می‌دهد و واتکینز نیز NINE, NINETEEN, NINETY, NINTH را زیر ژرمنی *niwun می‌آورد. «گ»ی میان‌واکه‌ای انگلیسی کهن در انگلیسی میانه افتاده و واکهٔ کشیدهٔ nine امروزی از همین‌جاست. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n    \"note\": \"No reference is printed in this box; Klein and Watkins were used instead (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. nine, ninety, nineteen\", \"stance\": \"supports\",\n    \"note\": \"'nine, adj. — ME. nigen, nine, fr. OE. nigon, nigan ...'; 'ninety, adj. — ME. nigenty, nyneti, fr. OE. nigontig. See nine and the numeral suff. -ty'; 'nineteen, adj. — ME. nigentene, nynetene, fr. OE. nigontiene, nigontyne. See nine and -teen.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. newn\", \"stance\": \"supports\",\n    \"note\": \"'Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH.'\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 7,\n \"lang\": \"Latin\",\n \"words\": \"novem; nôna\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin novem 'nine' is the regular reflex of *h₁néwn̥, its final -m taken over from septem 'seven' and decem 'ten' (Watkins: '< *noven, with m for n by analogy'; WP I 128: '-m lautgesetzlich aus -n? sonst nach septem, decem'). The ordinal is nōnus < *noven-os (Klein), whose feminine nōna in the phrase nōna hora means 'the ninth hour (of daylight)', i.e. about 3 p.m. by Roman reckoning — the chart's gloss 'ninth hour after sunrise (noon)' is exactly right, the parenthesis anticipating the English outcome. One correction: 'ninth month' is not a sense of novem but of its derivative November (mēnsis), 'the ninth month' of the old Roman year that began with March (Klein; Buck 14.44: 'October, November, December ... *novem-ri-s, *decem-ri-s, [with change of] medial mr to mbr'); novem itself only means 'nine'.\",\n \"derivation_fa\": \"لاتینی novem «نه» بازماندهٔ قاعده‌مند *h₁néwn̥ است و «م»ی پایانی آن به قیاس septem «هفت» و decem «ده» آمده است (واتکینز: «از *noven با m به قیاس»؛ والده-پوکورنی، جلد ۱، ص ۱۲۸). عدد ترتیبی آن nōnus از *noven-os است (کلاین) و صورت مادینهٔ nōna در ترکیب nōna hora «ساعت نهم روز» یعنی نزدیک ساعت سه پس از نیم‌روز به شمار رومیان؛ پس معنایی که نمودار می‌دهد («ساعت نهم پس از برآمدن آفتاب») درست است و پرانتز «noon» پیش‌درآمد شاخهٔ انگلیسی است. یک اصلاح: «ماه نهم» معنای novem نیست، بلکه معنای مشتق آن November (mēnsis) است، ماه نهم سال کهن رومی که از مارس آغاز می‌شد (کلاین؛ باک ۱۴٫۴۴)؛ خودِ novem تنها «نه» است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. newn: '2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nōnus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID).' Both of Nourai's Latin words and both English outcomes are in this one article.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. noon, nones, November\", \"stance\": \"supports\",\n    \"note\": \"'noon, n. — ME., “the ninth hour of the day reckoned from sunrise, noon”, fr. OE. nōn ... fr. L. nōna (hora), “the ninth (hour)”, fem. of nōnus, contraction of *noven-os, “ninth”, fr. novem, “nine”'; 'November, n. — L. November (mensis), “the ninth month” (of the Roman year), fr. novem, “nine”; see nine. (The Roman year began with March ...)'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 128\", \"stance\": \"supports\",\n    \"note\": \"'lat. novem „9“ (-m lautgesetzlich aus -n? sonst nach septem, decem)'; 'Ordinale: *noueno- in lat. nonus mit nach der 7 und 10 eingeführtem n statt m'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Dict. of Selected Synonyms §14.44 (months)\", \"stance\": \"partial\",\n    \"note\": \"'Since the Roman year orig. began with March, the numeral derivs. ... September, October, November, December [<] *novem-ri-s, *decem-ri-s, [with] medial mr to mbr' — confirms that 'ninth month' is November's sense, derived from novem.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 8,\n \"lang\": \"English\",\n \"words\": \"November, noon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"November was taken over from Latin November (mēnsis) 'the ninth month' (of the pre-Julian Roman year beginning in March), reaching English in the 12th-13th c. through Anglo-French novembre. noon is an early Old English borrowing: OE nōn '3 o'clock p.m., the ninth hour from sunrise; the canonical hour of nones' < Latin nōna (hora); it means midday today because the office of nones (and the meal that ended the fast) drifted earlier — Etymonline dates the shift from the 12th c., complete by the 14th, and Klein explains the same ('the prayers referred to were originally said at the ninth hour from sunrise, i.e. at 3 [p.m.]'). So both English words trace back to Latin novem via nōnus/nōna, exactly as drawn.\",\n \"derivation_fa\": \"«November» را انگلیسی از لاتینی November (mēnsis) «ماه نهم» (در گاه‌شمار کهن رومی که سال از مارس آغاز می‌شد) گرفته و در سدهٔ دوازدهم و سیزدهم از راه فرانسهٔ انگلیسی-نورمن (novembre) به کار آمده است. «noon» وام‌واژه‌ای کهن‌تر است: انگلیسی کهن nōn «ساعت سه پس از نیم‌روز، ساعت نهم از برآمدن آفتاب و نیز ساعت نماز نُهم کلیسا» از لاتینی nōna (hora)؛ اینکه امروز معنای «نیم‌روز» دارد از آن است که هنگام آن نماز و خوردنِ پس از روزه رفته‌رفته جلوتر آمد — به گفتهٔ Etymonline این جابه‌جایی از سدهٔ دوازدهم آغاز شد و تا سدهٔ چهاردهم کامل گشت، و کلاین همین توضیح را دارد. پس هر دو واژه از novem لاتینی از راه nōnus/nōna می‌آیند، درست همان‌گونه که نمودار رسم کرده است.\",\n \"sources\": [\"https://www.etymonline.com/word/noon\"],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n    \"note\": \"No reference in this box; Klein, Watkins and Etymonline were used instead (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. noon, nones, November\", \"stance\": \"supports\",\n    \"note\": \"'noon ... fr. OE. nōn, “the ninth hour of the day reckoned from sunrise”, fr. L. nōna (hora) ... orig. used in the sense of nones, “church office said daily at the ninth hour” ... The prayers referred to were originally said at the ninth hour from sunrise, i.e. at 3 [p.m.]'; 'November, n. — L. November (mensis), “the ninth month” ... fr. novem, “nine”'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. newn\", \"stance\": \"supports\",\n    \"note\": \"'2. Latin novem ...: NOVEMBER, NOVENA ... 3. Ordinal form *neweno- in Latin nōnus, ninth: NONA-, NONES, NOON' — both English words are listed as outcomes of this root.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline (archived via fetch_source.py)\", \"stance\": \"supports\",\n    \"note\": \"etymonline s.v. noon: 'Old English non “3 o'clock p.m., the ninth hour from sunrise,” also “the canonical hour of nones,” from Latin nona hora “ninth hour” of daylight, by Roman and ecclesiastical reckoning about 3 p.m.'; the shift to 12 p.m. 'began during the 12th century and was complete by the 14th'.\"}\n ]\n})\n\njson.dump(e2, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/e2.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(e2[\"nodes\"]))\nPY\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk363b.py"
}
```


### [2026-09-07T19:51:56.593Z] TOOL RESULT

```
ok 8
```


## [2026-09-07T19:52:02.104Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 - <<'PY'\nimport json\ne0=json.load(open('e0.json')); e2=json.load(open('e2.json'))\nout={\"pdf_page\":363,\"book_page\":333,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-07\",\"entries\":[e0,e2]}\njson.dump(out, open('/home/sfmqrb/git/rishe/data/verification/page-363.json','w'), ensure_ascii=False, indent=1)\nprint('written')\nPY\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-363.json > /dev/null && echo \"valid JSON\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 363"
}
```


### [2026-09-07T19:52:03.502Z] TOOL RESULT

```
Exit code 1
written
valid JSON
nodes verified: 8/14
node verdicts: {'plausible': 2, 'disputed': 1, 'confirmed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 4, 'partial': 2, 'not_checked': 2}
books consulted: {'partial': 5, 'supports': 20, 'contradicts': 1} | by book: {'WLD': 4, 'KLN': 4, 'BRT': 3, 'KNT': 2, 'PHD': 2, 'HRN': 2, 'AHD': 2, 'NYB': 1, 'HUB': 1, 'IEC': 1, 'ARY': 1, 'POK': 1, 'SYN': 1, 'WEB': 1}
PROBLEM: page 363: entry 0 (Neu) missing
```


## [2026-09-07T19:52:10.636Z] TOOL CALL #84: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-363.json'))\nfor e in d['entries']:\n    print(repr(e.get('entry')), e.get('root'), len(e.get('nodes',[])), [n['id'] for n in e['nodes']])\n\""
}
```


### [2026-09-07T19:52:13.057Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 5, in <module>
KeyError: 'nodes'
```


## [2026-09-07T19:52:16.391Z] TOOL CALL #85: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-363.json'))\nfor e in d['entries']:\n    print(repr(e.get('entry')), e.get('root'), list(e.keys()))\n\""
}
```


### [2026-09-07T19:52:17.705Z] TOOL RESULT

```
None None ['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']
2 Newn ['entry', 'root', 'verdict', 'modern_form', 'note', 'note_fa', 'sources', 'ref_check', 'consulted', 'nodes']
```


## [2026-09-07T19:52:24.318Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && ls -la e0.json e2.json && head -c 300 e0.json; echo; echo ---; python3 -c \"\nimport json;d=json.load(open('e0.json'));print(list(d.keys()))\""
}
```


### [2026-09-07T19:52:25.646Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 70860 Sep  7 15:48 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb 37506 Sep  7 15:51 e2.json
{
 "pdf_page": 359,
 "book_page": 329,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-07",
 "entries": [
  {
   "entry": 0,
   "root": "Nem 1",
   "verdict": "confirmed",
   "modern_form": "PIE *nem- 'to assign, allot; to take' (Pokorny 763-764 'nem-1'; Watkins/AHD 'nem-')",
   "note": "T
---
['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']
```


## [2026-09-07T19:52:35.820Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && sed -i \"s#scratchpad/e0.json#scratchpad/e0_p363.json#\" mk363a.py && sed -i \"s#scratchpad/e2.json#scratchpad/e2_p363.json#\" mk363b.py && python3 mk363a.py && python3 mk363b.py && python3 - <<'PY'\nimport json\ne0=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/e0_p363.json'))\ne2=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/e2_p363.json'))\nassert e0['entry']==0 and e0['root']=='Neu' and len(e0['nodes'])==6, (e0.get('entry'), e0.get('root'))\nassert e2['entry']==2 and e2['root']=='Newn' and len(e2['nodes'])==8\nout={\"pdf_page\":363,\"book_page\":333,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-07\",\"entries\":[e0,e2]}\njson.dump(out, open('/home/sfmqrb/git/rishe/data/verification/page-363.json','w'), ensure_ascii=False, indent=1)\nprint('written ok')\nPY\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-363.json > /dev/null && echo \"valid JSON\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 363"
}
```


### [2026-09-07T19:52:37.317Z] TOOL RESULT

```
ok 6
ok 8
written ok
valid JSON
nodes verified: 14/14
node verdicts: {'disputed': 2, 'plausible': 3, 'confirmed': 8, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 4, 'supports': 11, 'not_checked': 3}
books consulted: {'silent': 4, 'partial': 10, 'supports': 33, 'contradicts': 1} | by book: {'WLD': 6, 'KLN': 6, 'CHEUNG': 5, 'BRT': 4, 'PHD': 4, 'AHD': 4, 'KNT': 3, 'HRN': 3, 'HUB': 2, 'ARY': 2, 'MON': 1, 'GPL': 1, 'FRS': 1, 'LAT': 1, 'NYB': 1, 'IEC': 1, 'POK': 1, 'SYN': 1, 'WEB': 1}
```


## [2026-09-07T19:52:47.707Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 - <<'PY'\nimport json\np='data/verification/page-363.json'\nd=json.load(open(p))\nn=0\nfor e in d['entries']:\n    for nd in e['nodes']:\n        for c in nd.get('consulted',[]):\n            if c['src']=='WEB' and 'etymonline' in c.get('where','').lower():\n                c['src']='etymonline'; n+=1\njson.dump(d, open(p,'w'), ensure_ascii=False, indent=1)\nprint('fixed',n)\nPY\npython3 tools/verify_check.py 363 | tail -3; git status --short"
}
```


### [2026-09-07T19:52:49.070Z] TOOL RESULT

```
fixed 1
root verdicts: {'confirmed': 2}
ref checks: {'partial': 4, 'supports': 11, 'not_checked': 3}
books consulted: {'silent': 4, 'partial': 10, 'supports': 33, 'contradicts': 1} | by book: {'WLD': 6, 'KLN': 6, 'CHEUNG': 5, 'BRT': 4, 'PHD': 4, 'AHD': 4, 'KNT': 3, 'HRN': 3, 'HUB': 2, 'ARY': 2, 'MON': 1, 'GPL': 1, 'FRS': 1, 'LAT': 1, 'NYB': 1, 'IEC': 1, 'POK': 1, 'SYN': 1, 'etymonline': 1}
 M data/verification/page-363.json
```


## [2026-09-07T19:52:56.654Z] TOOL CALL #89: Bash

```json
{
 "command": "git log --oneline -2 -- data/verification/page-363.json; git diff --stat -- data/verification/page-363.json; git status --short --untracked-files=all data/verification/sources/refs/ocr/BQT/2210.vision.txt data/verification/sources/refs/ocr/BOOK/363.png data/verification/sources/web | head -5; cat .gitignore 2>/dev/null | head -20"
}
```


### [2026-09-07T19:52:56.779Z] TOOL RESULT

```
9b9638b Verify page 362 (Ner 2/narges, narcissus, snare, narrow; Nes 1/nâvus, nostalgia, harness)
 data/verification/page-363.json | 884 +++++++++++++---------------------------
 1 file changed, 277 insertions(+), 607 deletions(-)
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
```


## [2026-09-07T19:53:04.333Z] TOOL CALL #90: Bash

```json
{
 "command": "git show HEAD:data/verification/page-363.json | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('pdf_page'), d.get('book_page'), d.get('verified_by'), d.get('verified_on'))\nfor e in d['entries']:\n    print(' entry',e.get('entry'),e.get('root'),e.get('verdict'),[ (n['id'],n.get('verdict')) for n in e.get('nodes',[])])\n\"; git log --oneline -1 --format='%H %ad %s' -- data/verification/page-363.json"
}
```


### [2026-09-07T19:53:05.826Z] TOOL RESULT

```
363 333 claude-opus-5 2026-09-07
 entry None None None []
 entry 2 Newn confirmed [(1, 'plausible'), (2, 'plausible'), (3, 'disputed'), (4, 'confirmed'), (5, 'transcription_suspect'), (6, 'confirmed'), (7, 'confirmed'), (8, 'confirmed')]
9b9638b49e4cf629c0e75bcc57d16decef201d04 Mon Sep 7 15:52:36 2026 -0400 Verify page 362 (Ner 2/narges, narcissus, snare, narrow; Nes 1/nâvus, nostalgia, harness)
```


## [2026-09-07T19:53:21.592Z] TOOL CALL #91: Bash

```json
{
 "command": "python3 - <<'PY'\nimport json\nd=json.load(open('data/verification/page-363.json'))\nprint(d['pdf_page'], d['book_page'], d['verified_by'], d['verified_on'])\nfor e in d['entries']:\n    print('entry',e['entry'],e['root'],e['verdict'],'| note_fa?',bool(e.get('note_fa')),'| refchk',len(e['ref_check']),'| consulted',len(e['consulted']))\n    for n in e['nodes']:\n        print('   #%s %-22s %-22s fa=%s ref=%d con=%d' % (n['id'],n['lang'],n['verdict'],bool(n.get('derivation_fa')),len(n['ref_check']),len(n['consulted'])))\nPY\npython3 tools/verify_check.py 363 | head -6"
}
```


### [2026-09-07T19:53:23.061Z] TOOL RESULT

```
363 333 claude-opus-5 2026-09-07
entry 0 Neu confirmed | note_fa? True | refchk 1 | consulted 4
   #1 Avestan / Old Persian  disputed               fa=True ref=1 con=4
   #2 Persian                plausible              fa=True ref=2 con=5
   #3 Sanskrit               confirmed              fa=True ref=1 con=3
   #4 Persian                confirmed              fa=True ref=3 con=4
   #5 Latin                  confirmed              fa=True ref=2 con=4
   #6 English                confirmed              fa=True ref=1 con=2
entry 2 Newn confirmed | note_fa? True | refchk 1 | consulted 4
   #1 Avestan                plausible              fa=True ref=1 con=3
   #2 Pahlavi                plausible              fa=True ref=1 con=4
   #3 Persian                disputed               fa=True ref=1 con=5
   #4 Old Persian            confirmed              fa=True ref=1 con=3
   #5 Germanic               transcription_suspect  fa=True ref=1 con=3
   #6 English                confirmed              fa=True ref=1 con=2
   #7 Latin                  confirmed              fa=True ref=1 con=3
   #8 English                confirmed              fa=True ref=1 con=3
nodes verified: 14/14
node verdicts: {'disputed': 2, 'plausible': 3, 'confirmed': 8, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 4, 'supports': 11, 'not_checked': 3}
books consulted: {'silent': 4, 'partial': 10, 'supports': 33, 'contradicts': 1} | by book: {'WLD': 6, 'KLN': 6, 'CHEUNG': 5, 'BRT': 4, 'PHD': 4, 'AHD': 4, 'KNT': 3, 'HRN': 3, 'HUB': 2, 'ARY': 2, 'MON': 1, 'GPL': 1, 'FRS': 1, 'LAT': 1, 'NYB': 1, 'IEC': 1, 'POK': 1, 'SYN': 1, 'etymonline': 1}
```


## [2026-09-07T19:53:44.020Z] AGENT

Page 363 (book p. 333) done — `data/verification/page-363.json`, `verify_check.py 363` shows **0 PROBLEM** lines, 14/14 nodes.

Verdicts: roots 2 confirmed; nodes 8 confirmed, 3 plausible, 2 disputed, 1 transcription_suspect. Ref checks: 11 supports, 4 partial, 3 not_checked (uncited English boxes). 19 books consulted (POK, WLD, AHD, IEC, SYN, BRT, KNT, PHD, NYB, HRN, HUB, CHEUNG, BQT, MON, FRS, ARY, GPL/Platts, KLN, LAT, etymonline).

Flagged items:
- **disputed** — Neu #1 `nard` [Avestan / Old Persian]: no such root in Bartholomae or Kent; Cheung 282 has Ir. *nard only via MP nāl-, Parth. n'r-, Sogd. nrδ-, Skt nard, calls it "probably expressive" with no PIE ancestry, and keeps it separate from *nau(H) = Pok. 767. Nourai's own source (FFD 77) writes "ایرانی باستان *nard-a", i.e. reconstructed Proto-Iranian, not attested Avestan/OP. So the whole nālīdan branch is hung on the wrong root (node #2 downgraded to plausible for the same reason; the word and its MP nāl- ancestry are fine).
- **disputed** — Newn #3 `noh «نُه»`: NP noh continues the MP **cardinal** nō/nuh (MacKenzie "nē … | M nwh, N nuh] nine"; Bartholomae "Pü.: nōh"), not the ordinal naum. Hübschmann 1056 and Mo'in's footnote on the very page Nourai cites (BQT 2210: "فارسی جدید nuh از nôh از nava- با h بقیای dah") both say the -h is analogical from dah; naum/nohom yields نهم. Node #2 (Pahlavi naum) kept as plausible: the form is real but is the ordinal 'ninth' (⟨nhwm⟩ = MacKenzie nohom, Nyberg nahom), taken by Nourai from Mo'in's footnote via Horn's reading "phlv. nawm".
- **transcription_suspect** — Newn #5 Germanic `niwum`: AHD/Watkins prints Germanic *niwun (PGmc *newun); no Germanic form in -m exists. Page image confirms the book prints "niwum" → `error_in: "book"` (Nourai's misprint), extraction faithful.

Minor gloss errors noted in `derivation` (not flagged): Av. nauma = 'ninth' not 'nine'; Av. navadasa- attested as 'nineteenth'; 'ninth month' belongs to November, not novem; Latin vowel is nūntium.

No extraction errors — the JSON matches the printed page throughout.

Two housekeeping notes for you:
1. **HEAD currently holds a corrupted page-363.json.** The shared scratchpad is not agent-isolated: the page-359 agent overwrote my temp `e0.json`, my first assembly picked up its "Nem 1" entry, and that intermediate got committed in 9b9638b ("Verify page 362"). The working tree now has the correct file (entry 0 = Neu, 6 nodes) — it needs committing before any deploy. Consider having agents use page-suffixed temp filenames.
2. Audit artifacts written: `refs/ocr/BQT/2210.vision.txt`, `refs/ocr/BQT/2195.vision.txt`, `refs/ocr/FFD/77.vision.txt`, `refs/ocr/BOOK/363.png`; 4 web pages archived via fetch_source.py (Wiktionary nuntius, PIE *h₁néwn̥, Persian نه, etymonline noon).
