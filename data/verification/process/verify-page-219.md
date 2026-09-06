# Verification process log — verify-page-219


## [2026-09-06T15:11:29.230Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 219 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-219.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-219.json. Write /home/sfmqrb/git/rishe/data/verification/page-219.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 219` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:11:30.826Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:11:31.535Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:11:31.551Z] TOOL RESULT

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


## [2026-09-06T15:11:31.617Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-219.txt"
}
```


### [2026-09-06T15:11:31.640Z] TOOL RESULT

```
1	=== PDF page 219 (book page 189) ===
2	--- entry 0 ---
3	ROOT [Aramaic] Habl : rope  (refs VDQ:176)
4	#1 (parent #0) [Arabic] refs=KLN:216 | habl : rope, cable
5	  #2 (parent #1) [Persian] refs=FVA:89 | habl «حَبل» : rope
6	  #3 (parent #1) [Portuguese] refs=KLN:216 | cable | NOTE: KLN:216 claims this is a blend of Arabic "habl: rope" and Latin "caplum: a halter for cattle". AHD and FSD drive it from Latin (See "Kap").
7	    #4 (parent #3) [French] refs=KLN:216 | kâbl
8	      #5 (parent #4) [Persian] refs=MON:2777 | kâbl «کابل» : cable
9	      #6 (parent #4) [English] refs=KLN:216 | cable | NOTE: See root "Kap" for another possible root.
10	--- entry 1 ---
11	ROOT [Avestan] Haem, Haya : character, nature  (refs HRN:114; FVS:168,179)
12	#1 (parent #0) [Pahlavi] refs=PHD:94; HRN:114 | xîm : temper, nature
13	  #2 (parent #1) [Persian] refs=BQT:804; HRN:114; FSF:168,179 | xîm «خیم» : temper, nature ; dožxîm «دژخیم» : bad tempered ☞Dus | extra: بدخیم ، خوش خیم
14	--- entry 2 ---
15	ROOT [Avestan] Hâvana : mortar  (refs MON:5095)
16	#1 (parent #0) [Pahlavi] refs=MON:5095 | hâvan : mortar
17	  #2 (parent #1) [Persian] refs=BQT:2312; HRN:244 | hâvan «هاون» : mortar
18	--- entry 3 ---
19	ROOT Haya -> redirect to Haem
20	
```


## [2026-09-06T15:11:34.599Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-219.json",
 "description": "Read page 219 source JSON"
}
```


### [2026-09-06T15:11:34.639Z] TOOL RESULT

```
{
  "pdf_page": 219,
  "book_page": 189,
  "entries": [
    {
      "root": {
        "name": "Habl",
        "lang": "Aramaic",
        "refs": "VDQ:176",
        "gloss": "rope"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:216",
          "words": [
            {"translit": "habl", "gloss": "rope, cable", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:89",
          "words": [
            {"translit": "habl", "gloss": "rope", "script": "حَبل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "کله دلو کرد آن پسندیده کیش - چو حبل اندرآن بست دستار خویش", "poet": "Sa`dî"}
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Portuguese",
          "refs": "KLN:216",
          "words": [
            {"translit": "cable", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "KLN:216 claims this is a blend of Arabic \"habl: rope\" and Latin \"caplum: a halter for cattle\". AHD and FSD drive it from Latin (See \"Kap\").",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "KLN:216",
          "words": [
            {"translit": "kâbl", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:2777",
          "words": [
            {"translit": "kâbl", "gloss": "cable", "script": "کابل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:216",
          "words": [
            {"translit": "cable", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "See root \"Kap\" for another possible root.",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Haem, Haya",
        "lang": "Avestan",
        "refs": "HRN:114; FVS:168,179",
        "gloss": "character, nature"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "PHD:94; HRN:114",
          "words": [
            {"translit": "xîm", "gloss": "temper, nature", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:804; HRN:114; FSF:168,179",
          "words": [
            {"translit": "xîm", "gloss": "temper, nature", "script": "خیم"},
            {"translit": "dožxîm", "gloss": "bad tempered", "script": "دژخیم", "see": ["Dus"]}
          ],
          "script_extra": "بدخیم ، خوش خیم",
          "note": null,
          "quote": {"text": "دگر خوی را آنک خوانیم خیم - که با او ندارد دل از دیو بیم", "poet": "Ferdowsî"}
        }
      ]
    },
    {
      "root": {
        "name": "Hâvana",
        "lang": "Avestan",
        "refs": "MON:5095",
        "gloss": "mortar"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:5095",
          "words": [
            {"translit": "hâvan", "gloss": "mortar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2312; HRN:244",
          "words": [
            {"translit": "hâvan", "gloss": "mortar", "script": "هاون"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "نه پیش من دواوین بود و دفتر - نه عیسی را عقاقیر است و هاون", "poet": "Marzbân Nâmeh"}
        }
      ]
    },
    {
      "root": {"name": "Haya", "redirect": "Haem"},
      "nodes": []
    }
  ]
}
```


## [2026-09-06T15:11:35.122Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:11:35.162Z] TOOL RESULT

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


## [2026-09-06T15:11:38.797Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['VDQ','FVA','FVS','FSF','KLN','MON','BQT','PHD','HRN']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900])\n    print()\n\""
}
```


## [2026-09-06T15:11:39.622Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"caplum\" KLN_1966.txt KLN_1971.txt | head -30"
}
```


### [2026-09-06T15:11:40.609Z] TOOL RESULT

```
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghbook.ir) as an app/EPUB per news reports.", "cites": "page number of the Persian translation of Jeffery's Foreign Vocabulary of the Qurʾān"}

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

FVS {"title": "(not in Table IV — probably a typo for FVF or FSF)", "kind": "none", "url": null, "lookup_hint": "Check the two citations against FVF (Emam Shushtari) and FSF (Noushin).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "abbreviation not defined in Nourai's Table IV."}

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Dony

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
```


### [2026-09-06T15:11:40.657Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:11:43.589Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"capulum\\|cable\" KLN_1966.txt | head -40"
}
```


### [2026-09-06T15:11:43.639Z] TOOL RESULT

```
2406:Amati,  n.,  a  violin  made  by  a  member  of  the Amati  family  at  Cremona  (16th  and  17th  cent.) amative,  adj.,  pertaining  to  love,  amatory.  — Formed  with  suff.  -ive  fr.  L.  amatus,  pp.  of  amd- re,  ‘to  love’,  from  the  I.-E.  infantile  imitative base  *ama-,  whence  also  amita,  ‘father’s  sister’, amicus,  ‘friend’.  Cp.  Gk.  ASxpivEiv,  ‘to  love’ (Hesychius),  which  is  formed  fr.  Phrygian  in¬ tensive  pref.  AS-  and  *ap.veiv,  ‘to  love’.  See aunt  and  cp.  Amabel,  amadou,  Amanda,  Aman¬ dus,  amateur,  amenity,  amiable,  amicable,  amity, amorous,  amour,  enamor,  enemy,  enmity,  ina¬ morato,  inimical.
2474:Amhaarez,  n.,  an  ignoramus.  —  Heb.  ‘am  had- retz,  ‘the  people  of  the  land’.  Heb.  'am,  ‘people’, derives  fr.  base  ‘- m-m ,  ‘to  join,  be  united’, whence  also  ‘am,  ‘kinsman’,  'im,  ‘with’.  Cp.  the rel.  Aram.-Syr.  ‘ammd,  ‘people’,  Ugar. ‘/n, ‘clan’, Arab,  ‘amm,  ‘a  great  crowd’,  ammah,  ‘rabble’, ‘dmma,  ‘it  comprised,  included’,  ‘amm,  ‘father’s brother’,  ‘ dmma *,  ‘father’s  sister’,  Aram,  'im, Syr.  ‘am,  Ugar.  'm,  Arab.  ma‘a,  dial,  ‘am, ‘with’.  Cp.  the  first  element  in  Emmanuel  and the  second  element  in  Jeroboam.  Heb.  eretz, ‘earth’,  is  rel.  to  Aram.  dra‘,ar‘d,  Ugar.  Vy,  Arab. ard,  Akkad,  irfitu,  ‘earth’.  Cp.  Eretz  Yisrael. amiable,  adj.  — OF.  (=  F.),  fr.  Late  L.  amicabilis, ‘friendly’,  fr.  L.  amicus,  ‘friend’.  F.  amiable  was influenced  in  form  by  aimable,  ‘lovely’,  fr.  L. amdbilis,  fr.  amare,  ‘to  love’.  See  amicable. Derivatives:  amiabil-ity,  n.,  amiable-ness,  n., amiabl-y,  adv.
2478:amicable,  adj.,  friendly.  —  L.  amicabilis,  friend¬ ly’,  fr.  amicus,  ‘friend’,  fr.  amare,  ‘to  love’.  See amative  and  cp.  amiable,  which  is  a  doublet  of amicable.  Cp.  also  enemy,  inimical.  For  sense development  cp.  Gk.  <plXo c„  ‘friend’,  from  the base  of  cptXeiv,  ‘to  love’,  and  Heb.  ohfbh, ‘friend’,  which  is  prop.  part,  of  ahdbh,  ‘he loved’.
2479:Derivatives:  amicabil-ity,  n.,  amicable-ness,  n., amicabl-y,  adv.
3189:‘folded  sheet’,  pronounced  nap-pe  pliee.  See napery  and  ply,  ‘to  bend’, appliance,  n,  —  Formed  fr.  apply  with  suff.  -ance. applicable,  adj.  —  Formed  with  suff.  -able  fr.  L. applicare.  See  apply.
3190:Derivatives:  applicabil-ity,  n.,  applicable-ness, n.,  applicabl-y,  adv.
3191:applicancy,  n.,  quality  of  being  applicable.  — Formed  fr.  next  word  with  suff.  -cy. applicant,  n.,  one  who  applies  for  something.  —
5024:bind,  tr.  and  intr.  v.  —  ME.  binden,  fr.  OE. bindan,  rel.  to  OS.,  Goth,  bindan,  ON.,  OFris. binda,  OHG.  bintan,  MHG.,  G.  binden,  fr.  I.-E. base  *bhendh-,  ‘to  bind’,  whence  also  OI.  badh- ndti,  later  form  bandhati,  ‘binds’,  bandhuh , ‘kinsman’,  Gk.  7revbep6<;,  ‘father-in-law’,  prop, ‘bound  (through  marriage)’,  ireiopa  (for  *7rev0- tjpa),  ‘cable’,  7taSvT],  Att.  cpixvr,  (for  * bhqdh-na).
5083:Derivatives:  bitter-ly,  adv.,  bitter-ness,  n. bitter,  n.,  turn  of  the  cable  about  the  bitts  (naut.)
6015:cable,  n.  —  ME.  cable,  cabel,  kable,  fr.  F.  cable, fr.  Port,  cable,  which  is  a  blend  of  Arab,  habl, ‘rope,  cable’,  and  VL.  cap(u)lum,  ‘a  halter  for cattle’,  fr.  capid,  capere,  ‘to  catch,  seize,  take, hold’.  Arab,  habl  is  rel.  to  habala,  ‘he  bound’, Heb.  hebhel,  ‘rope,  cord’,  Ethiop.  habal,  ‘rope’, habala,  ‘he  bound’,  Akkad,  nahbalu,  ‘rope, snare’,  Aram,  habhld,  ‘cord,  rope’.  For  the  ety¬ mology  of  L.  capere  see  captive.
6016:Derivatives:  cable,  v.,  cabl-ed,  adj.,  cabl-er,  n., cabl-ing,  n.,  cabl-et,  n.
6017:cablegram,  n.  —  A  blend  of  cable  and  telegram.
6035:cachalot,  n.,  the  sperm  whale.  —  F.,  fr.  Sp.  ca¬ chalot?,  fr.  Port,  cacholotte,  lit.  ‘thick-headed’, fr.  cachola,  ‘head,  pate’,  which  is  perh.  a  dimin. of  cacha,  ‘handle  of  a  razor’,  fr.  VL.  capula, pi.  of  capulum,  corresponding  to  L.  capulus, ‘handle,  hilt  of  a  sword’,  fr.  capere,  ‘to  catch, seize’.  See  captive.
6478:fr.  L.  captivus,  ‘caught,  taken  prisoner’,  fr.  cap¬ tus,  pp.  of  capere,  ‘to  catch,  seize,  take  hold  of, take,  receive,  hold,  contain’,  whence  L.  capsa, ‘repository,  box,  chest,  case’,  capulus,  ‘sarco¬ phagus,  bier’ ;  fr.  I.-E.  base  *qap-,  ‘to  seize,  hold, contain’,  whence  also  Gk.  yAnzeiv,  ‘to  swallow greedily,  gulp  down’,  xam;,  ‘manger’,  xcotty), ‘handle,  handle  of  an  oar,  haft’.  Alb.  kap,  ‘I take,  seize’,  kam,  ‘I  have’,  Lett.  kamp(j)u,  kdmpt, ‘to  seize*,  Goth,  hafjan,  OE.  hebban,  ‘to  raise, lift’,  Goth,  haban,  OE.  habhan,  ‘to  have’, and  prob.  also  OI.  kapati,  ‘two  handfuls’. See  heave  and  have  and  cp.  words  there  referred to.  Cp.  also  accept,  anticipate,  apperccive,  apper¬ ception,  aucupate,  cabas,  cabbage,  ‘to  pilfer’, cable,  cachalot,  caisson,  caitiff  (which  is  a  dou¬ blet  of  captive),  caja,  cajeta,  cajole,  capable,  ca¬ pacious,  capacity,  capias,  capistrate,  capsa,  Cap¬ sella,  Capsicum,  capstan,  capsule,  captation, caption,  captious,  captor,  capture,  Carpocapsa, case,  ‘box,  chest’,  casement,  cash,  catch,  chara¬ banc,  chase,  conceive,  concept,  conception,  cop, ‘to  catch',  Copepoda,  deceipt,  deceive,  deception, disciple,  discipline,  emancipate,  except,  excipient, forceps,  imperceptible,  incept,  inception,  inter¬ cept,  intussusception,  mancipate,  mercaptant, municipal,  nuncupative,  occupy,  participate,  per¬ ceive,  percept,  perception,  precept,  preceptor, prince,  principal,  principle,  purchase,  recado,  re¬ ceipt,  receive,  recept,  receptacle,  reception,  re¬ ceptive,  recet,  recipe,  recover,  recuperate,  sus¬ ceptible,  usucapion.
8399:commune,  n.,  a  small  political  district.  —  F.,  fr. L.  commiinia,  neut.  pi.  of  communis,  ‘common’, which  was  mistaken  for  fern.  sing.  See  common, commune,  intr.  v.  —  OF.  comuner,  fr.  comun, ‘common’.  See  common,  adj. communicable,  adj.  —  F.,  fr.  Late  L.  communi- cdbilis,  fr.  L.  commitnicare.  See  communicate and  -able.
8400:Derivatives:  communicabil-ity,  n„  communi- cable-ness,  n.,  communicabl-y,  adv. communicant,  adj.  and  n.  —  L.  commdnicdns, gen.  -antis,  pres.  part,  of  communicdre.  See  next word  and  -ant.
8674:confiscable,  adj.  —  See  next  word  and  -able, confiscate,  tr.  v.,  to  seize  by  authority.  —  L.  con¬ fiscates,  pp.  of  confiscdre,  'to  lay  up  in  a  chest; to  seize  on  for  the  public  treasury’,  fr.  con-  and fiscus,  ‘basket,  public  chest,  treasury’.  See  fisc and  verbal  suff.  -ate.
11058:Derivatives :  desperate-ly,  adv.,  desperate-ness ,  n . desperation,  n  —  ME.  desperacioun,  fr.  MF.  despe¬ ration,  fr.  L.  desperationem,  acc.  of  desperdtio, ‘despair,  hopelessness’,  fr.  desperatus,  pp.  of desperare.  See  despair,  v.,  and  -ation. despicable,  adj.  —  Late  L.  despiedbilis,  ‘contempt¬ ible,  despicable’,  fr.  L.  despiedri,  ‘to  despise, disdain’,  rel.  to  despicere,  ‘to  look  down  upon; to  despise,  disdain’,  fr.  de-  and  specere,  spicere, ‘to  look  at’.  See  species  and  -able  and  cp.  next word.
11059:Derivatives:  despicabil-ity,  n.,  despicable-ness, n.,  despicabl-y,  adv.
12038:domesticable,  adj.  —  ML.  domesticabilis,  fr. domesticdre.  See  next  word  and  -able, domesticate,  tr.  v.,  to  tame.  —  ML.  domesticatus , pp.  of  domesticdre,  ‘to  tame’,  lit.  ‘to  make  dom¬ estic’,  fr.  L.  domesticus.  See  domestic  and  verbal suff.  -ate.
12656:educable,  adj.  —  See  next  word  and  -able, educate,  tr.  v.  —  L.  educatus,  pp.  of  eduedre,  ‘to bring  up,  rear,  educate’,  rel.  to  educere,  ‘to  lead out,  bring  out;  to  bring  up,  rear,  raise’,  fr.  e- and  ducere,  ‘to  lead’.  See  duke  and  verbal  suff. -ate  and  cp.  educe.
13150:enema,  n.,  injection  of  a  fluid  into,  the  rectum (med.)  —  Late  L.,  fr.  Gk.  SvEpia,  ‘injection, clyster’,  fr.  tviiv 01,  ‘to  throw  in,  send  in’,  fr.  tv (see  2nd  en-)  and  Itvou,  ‘to  send,  throw, project’,  which  stands  for  *yi-ye-nai  and  is  cogn. with  L.  jacere,  ‘to  throw’.  See  jet,  ‘to  spirt forth’,  and  cp.  words  there  referred  to. enemy,  n.  —  OF.  enemi  (F.  ennemi),  fr.  L.  ini- mtcus,  ‘hostile,  unfriendly;  an  enemy’,  fr.  in-, ‘not’,  and  amicus,  ‘friend’.  Cp.  It.  nemico.  Prov¬ en?.  enemic,  Catal.  enamic,  Sp.  enemigo,  Port. inimigo,  which  all  derive  fr.  L.  inimicus,  and see  amicable.  Cp.  also  enmity,  inimical, energetic,  adj.  —  Gk.  4vspy9Tix6i;,  ‘able  to  act upon’,  fr.  IvEpyetv,  ‘to  work,  be  strenuous,  act upon’,  fr.  £vEpfr)?,  later  form  of  £vEpy<k,  ‘at work,  active’.  See  energy  and  -ic.
13508:eradicable,  adj.  —  See  next  word  and  -able.
13642:Derivative:  espalier,  tr.  v. esparto,  n.,  also  esparto  grass.  —  Sp.  esparto,  fr. L.  spartum,  fr.  Gk.  crmipTOv,  ‘rope,  cable; Spanish  broom:  esparto’,  which  is  rel.  to CTJrdipToq,  ‘Spanish  broom;  esparto’,  and  to csTcetpa,  ‘coil,  twist’,  and  prob.  cogn.  with  Lith. spartas,  ’band’.  See  spire,  ‘spiral’,  and  cp. Spartina,  Spartium.
14112:explicable,  adj.  —  L.  explicabilis,  ‘that  may  be explained’,  fr.  explicare.  See  next  word  and -able.
14226:extricable,  adj.  —  See  next  word  and  -able, extricate,  tr.  v.  —  L.  extricatus,  pp.  of  extricare, ‘to  disentangle,  extricate’,  formed  fr.  ist  ex-  and tricae  (pi.),  ‘trifles,  stuff;  perplexities,  wiles, tricks’,  which  is  of  uncertain  origin.  It  meant perh.  orig.  ‘twisted  ways’,  and  derives  fr.  I.-E.
18794:immedicable,  adj.,  incurable.  —  L.  immedicabilis, ‘incurable’,  fr.  in-,  ‘not’,  and  medicabilis, ‘curable’.  See  medicable.
18854:impeccable,  adj.,  1)  not  liable  to  sin;  2)  faultless.
18855:—  Late  L.  impeccabilis,  ‘impeccable’,  lit.  ‘not liable  to  sin’,  fr.  in-,  ‘not’,  and  L.  peccdre,  ‘to sin’.  See  peccant  and  -able.
18904:Derivatives:  impious-ly,  adv.,  impious-ness,  n. implacaoility,  n.  —  Late  L.  implacabilitas,  fr. L.  implacdbilis.  See  next  word  and  -ity. implacable,  adj.  —  F.,  fr.  L.  implacdbilis,  ‘un¬ appeasable’,  fr.  in-,  ‘not’,  and  pldcabilis,  ‘easily appeased’.  See  placable.
18905:Derivatives:  implacable-ness,  n.,  implacabl-y,  adv. implacental,  adj.,  having  no  placenta  (applied  to a  group  of  mammals  including  the  marsupials).
19286:Derivatives:  inexpert-ly,  adv.,  inexpert-ness,  n. inexpiable,  adj.  —  L.  inexpiabilis,  ‘that  cannot be  atoned  for,  implacable’,  fr.  in-,  ‘not’,  and expiare,  ‘to  make  amends  or  atonement  for’. See  expiable.
19287:Derivatives:  inexpiable-ness, n.,  inexpiabl-y, adv. inexplicable,  adj.  —  F.,  fr.  L.  inexplicabilis,  fr. in-,  ‘not’,  and  explicabilis.  See  explicable. Derivatives:  inexplicabil-ity,  n.,  inexplicable¬ ness,  n.,  inexplicabl-y,  adv. inexplicit,  adj.  —  L.  inexplicitus,  ‘not  to  be  un¬ folded,  unexplained’,  fr.  in-,  ‘not’,  and  explicitus. See  explicit,  adj.
19289:Derivatives:  inexpugnabil-ity,  n.,  inexpugnable¬ ness,  n.,  inexpugnabl-y,  adv. inextricable,  adj.  —  L.  inextriedbilis,  ‘that  can¬ not  be  disentangled’,  fr.  in-,  ‘not’,  and  extri- cabilis.  See  extricable.
19290:Derivatives:  inextricabil-ity,  n.,  inextricable¬ ness,  n.,  inextricabl-y,  adv.
19417:inimical,  adj.  —  Late  L.  inimicalis  ‘hostile’,  fr.  L. inimicus,  ‘enemy’,  fr.  in-  ‘not’  and  amicus,  ‘friend’. See  amicable  and  adj.  suff.  -al.  and  cp.  enemy. For  the  change  of  Latin  d  (in  dmlcus)  to  i  (in in-imicus )  see  abigeat  and  cp.  words  there referred  to.
19927:Derivative:  irreverent-ly,  adv. irreverential,  adj.  —  Formed  with  adj  suff.  -al fr.  L.  irreverentia.  See  irreverence, irrevocable,  adj.  —  L.  irrevocabilis,  ‘that  cannot be  recalled,  irrevocable’,  fr.  in-,  ‘not’,  and  re- vocabilis.  See  revocable.  Derivatives :  irrevocabil¬ ity,  n.,  irrevocable-ness,  n.,  irrevocabl-y,  adv. irrigate,  tr.  v.,  to  water.  —  L.  irrigatus,  pp.  of irrigate,  ‘to  conduct  water  to;  to  water,  irri¬ gate;  to  wet,  moisten;  to  refresh,  nourish’, fr. a-,  ‘in',  and  rigare,  ‘to  wet,  moisten’,  which  is cogn.  with  Goth,  rign,  OE.  regn,  ‘rain’.  See rain,  n.,  and  verbal  suff.  -ate.
20462:Juncus,  n.,  a  genus  of  plants,  the  rush  (bot.)  — L.  juncus,  ‘rush,  bulrush’,  which  stands  for *yoini-kos  and  is  cogn.  with  Mir.  din,  ‘reed’, and  prob.  also  with  ON.  einir,  Swed.  en,  ‘juni¬ per’;  see  Walde-Hofmann,  LEW.,  I,  727L  Cp. jonquil,  Junco,  junk,  ‘bulrush’,  junk,  ‘old  cable’, junket,  and  the  first  element  in  juniper.
20469:'  words  there  referred  to. junk,  n.,  1)  old  cable;  2)  old  cordage.  —  Port. junco,  ‘rush,  cordage’,  fr.  L.  juncus.  See  Juncus and  cp.  prec.  word.
22774:manducable,  adj.  —  Formed  with  suff.  -able  fr.
```


## [2026-09-06T15:11:44.748Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==121||NR==120||NR==122 {print \"=== leaf \" NR-1 \" ===\"; print}' KLN_1966.txt | head -120"
}
```


### [2026-09-06T15:11:47.232Z] TOOL RESULT

```
<persisted-output>
Output too large (29.7KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b3rycwtpm.txt

Preview (first 2KB):
=== leaf 119 ===
OF. bruisier,  ‘to  break’.  Both  OE.  brysan  and  OF. bruisier  derive  fr.  I.-E.  base  *bhreus-,  *bhres-, ‘to  break,  crush,  crumble’,  whence  also  OIr. bronnaim  (for  *bhrusnami),  ‘I  wrong,  hurt’,  bris- sim,  ‘I  break’,  brisc,  ‘brittle’,  Bret,  bresk,  of s.m.,  brezel,  ‘war’,  VL.  brisare,  ‘to  break’,  a word  of  Celtic  origin  (whence  F.  briser,  of  s.m.), Mir.  brtiim,  ‘I  crush’,  OE.  berstan,  OS.,  OHG. brestan,  etc.,  ‘to  burst’,  and  prob.  also  L.  frus¬ tum  (fr.  *bhrus-to-),  ‘piece’,  Alb.  bresen,  ‘hail’. Cp.  I.-E.  *bhrousmen,  whence  OS.  brosma, OHG.  brosama,  brosma,  MHG.  broseme,  bros- me,  G.  Brosam,  Brosame,  ‘crumb’.  Cp.  debris, debruise.  Cp.  also  burst.  Cp.  also  frustum. Derivatives :  bruise,  n.,  bruis-er,  n.,  bruis-ing,  n. bruit,  n.,  noise;  rumor  (archaic).  —  F.  ‘noise’, orig.  pp.  of  bruire,  ‘to  rustle,  rumble’,  used  as  a noun.  F.  bruire  derives  fr.  VL.  *brugere,  which is  a  blend  of  L.  rugire,  ‘to  roar’,  with  VL.  *bra- gere,  ‘to  whine,  cry’  (whence  F.  braire,  ‘to  bray’ (see  bray,  ‘to  cry’).  L.  rugire  (whence  VL.  *ru- gere),  ‘to  roar’,  is  cogn.  with  Gk.  Epuystv,  ‘to bellow,  roar',  opufraySog,  ‘a  loud  noise’,  pu£etv (for  *p(>Yi£iv),  ‘to  growl,  snarl’,  OSlav.  rykati, ryknQti,  ‘to  roar,  bellow’,  OE.  ryn  (for  *ruhjan), OHG.  rohon,  of  s.m.
Derivatives:  bruit,  tr.  v.,  bruit-er,  n.
Brumaire,  n.,  name  of  the  second  month  of  the French  revolutionary  calendar  (lasting  from October  23rd  to  November  21st).  —  F.,  lit.,  ‘the foggy  month’,  coined  by  Fabre  d’Fglantine  in 1793  fr.  brume,  ‘fog’,  fr.  L.  bruma.  See  brume and  -aire.
...
</persisted-output>
```


## [2026-09-06T15:12:11.813Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('cable,  n.  —  ME.')\nprint('leaf(0-based ff count):', t[:i].count('\\f'))\nEOF"
}
```


### [2026-09-06T15:12:13.815Z] TOOL RESULT

```
leaf(0-based ff count): 125
```


## [2026-09-06T15:12:13.910Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- PHD xem ---\" && grep -n \"^x[eēê]m\\|xēm\\|hym\" PHD.txt PHD_mackenzie.txt | head -20; echo \"--- HRN xim ---\" && grep -n -i \"chîm\\|ch[iî]m \\|xim\\|hîm\" HRN.txt | head -30"
}
```


### [2026-09-06T15:12:13.976Z] TOOL RESULT

```
--- PHD xem ---
PHD.txt:318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
PHD.txt:376:gabr [gpl, gwbl | M gbr, N ? gór] hollow, cavity, womb. ~ih: hollowness. баё [gc | N ~] plaster, gypsum. -ёп [-yn!] (made of) plaster. gad [gt! = Av. gada-] club, mace. gādan, gày- [SL Y TWN-tn! < А V sry ?; g'tn! | N ~] copulate with. gadar [g??]] husband. gadwar [gtwl = Av. gaóawara-] bearing a club. 1gàh [gs | M ek, N ~] place, throne, bed. ?6àh [g’s | N ~] time; a fifth division of the day; = ģāhānbār. збаһ [gs] а Gatha, hymn. gah4n [g’s’n'] the Gathas; those scriptures dealing with spiritual and theological matters. ģāhānbār [gnb] | N gáhanbár] the six divisions of the year, the five-day festivals celebrated at the ends of these. ģāhānīg [g?snyk!] relating to the Gathas; spiritual; the five epact days at the end of the year. gahbed [g’spt' | N *gahbad] treasurer, banker. ~ih: treasurership. gahl [г()А | N gal] sorghum, giant millet. gāhüg [p hwk'] bier. gāhwārag [g’swlk' | N gāhwāra] cot, cradle. ģāl [2° household, following.
PHD.txt:400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
PHD.txt:566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:657:wizürd-wars [wc'/t' wls] with parted hair. wizāstan, wizāy- [wyz'stn!, wyz'd- | M wy2’y-, N guzáy-] injure, impair, prejudice. ~išn: injury. ~išnīg: injurious. wizén [wcyn! | N guzin] choice. wizend [wz(y)nd | M wzynd, N guzand] hurt, harm, injury. wizéngar [wcynkl] chooser; selective. | wizidan, wizin- [weytn', wcyn- | M weyd, N guzīdan, guzīn-| choose, select, prefer, discriminate. wizihidan, wizīh- [w(y)cyh-ytn'] be separated. „išn(īh): separation; dawn(ing). wizin- , v. wizidan. wizir [weyl] decision, judgement. wiziristan, wizir- [wcyl-stn! | J bzyr-, N guzir-) be able to dispense with, avoid. ~iSnig : avoidable. wizistan [westn' | M weyst] teach. wizóstan, wizóh/y- [wewstn', wewd- | (J bzwb-, N pizohidan)] examine, investigate. -~i§n : investigation. wizüdan [wyzwin'] = wizastan. wizurd [wewlt'] valid, genuine, true. ~th: validity, truth. Wērūbaršt [w’wklwblst' = Av. wouru.barasti-] the north-western con- tinent of the earth. Wērūjaršt [w>wklwelft' = Av. wouru.jarasti-] the north-eastern con- tinent of the earth. wurróyistan, wurróy- [H YMNN-stn! < A hymn, У °тп | M wrwyst, (wrw-), J *brwy-, grww-, N brw-, girawidan] believe; choose. —išn [wlwdén'] belief. wuzurg [LBA < Arb’; wc(w)lg | M wzrg, N buzurg] big, great. ~ith: size, greatness. wuzurg-framadar [LBA plm't I) prime minister.
PHD.txt:1820:evil-natured dušxēm.
PHD.txt:2350:hymn gah.
PHD.txt:2369:tll-natured wad-xēm.
PHD.txt:4010:thyme, wild — sisimbar.
PHD.txt:5422:1*dēš-, duš- dušēwāzīh dušxēm dušxwār
PHD_mackenzie.txt:2157:  .......-xem [-hym] evil-natured.
PHD_mackenzie.txt:2421:agAh [g)s] a Gatha, hymn.
PHD_mackenzie.txt:2996:hu-xem [hwhym] of good character, good-natured.
PHD_mackenzie.txt:4556:sisimbar [sysymbl, -nbll N sisambar] sisymbrium, wild-thyme.
PHD_mackenzie.txt:5133: ......-xem [-hym] ill-natured.
PHD_mackenzie.txt:5514:wurroyistan, wurroy- [HYMNN-stn < A hymn, ..; 'mn I M wrw)'st,
PHD_mackenzie.txt:5554:xeIYl [hym] nature, character.
PHD_mackenzie.txt:6827:hymn gih.                                improper anabiiy.
PHD_mackenzie.txt:7784:than az, kG.                              thyme, wild", sisimbar.
--- HRN xim ---
```


## [2026-09-06T15:12:22.566Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==126' KLN_1966.txt | head -5; echo \".....\"; awk 'BEGIN{RS=\"\\f\"} NR==126' KLN_1966.txt | tail -5"
}
```


## [2026-09-06T15:12:23.269Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==136' HRN.txt | head -60"
}
```


### [2026-09-06T15:12:24.329Z] TOOL RESULT

```
cabalist,  n.,  a  student  of  cabala.  —  A  hybrid formed  fr.  cabala  with  suff.  -ist.
Derivative:  cabalist-ic,  adj. cabaret,  n.  —  F.,  a  loan  word  fr.  MDu. cabret ,  denasalized  fr.  cambret,  camret,  fr. OPicard  cambrete,  dimin.  of  cambre,  ‘chamber, room’,  which  is  rel.  to  F.  chambre,  of  s.m.  See chamber  and  -et.
cabas,  n.,  a  fiat  basket.  —  F.,  ‘frail,  basket’,  fr. OProven?.  cabas,  ‘basket  of  sedge’,  fr.  VL.  *ca- pacius ,  fr.  I.,  capdx,  gen.  capdcis,  ‘that  can  con¬ tain  much,  capacious,  spacious’,  fr.  capid,  ca- pere,  ‘to  catch,  seize,  take,  hold’.  See  captive  and cp.  cabbage,  v.
cabbage,  n.,  plant  of  the  order  Brassica.  —  ME. caboche,  fr.  ONF.  ( —  F.)  caboche,  ‘head’,  fr. OF.  caboce ,  formed  fr.  pejorative  pref.  ca-  and boce  (F.  bosse ),  ‘a  swelling'.  See  boss,  ‘a  pro¬ tuberance’,  and  cp.  Boche,  cabochon.
Derivative:  cabbage,  intr.  and  tr.  v. cabbage,  tr.  and  intr.  v.,  to  pilfer.  —  F.  cabasser, ‘to  steal',  fr.  cabas,  ‘basket’.  See  cabas, cabby,  n.,  a  cabman  (colloq.)  —  Short  for  cabman, caber,  n.,  a  beam.  —  Gael,  cabar,  ‘pole,  beam’, cabildo,  n.,  the  chapter  of  a  cathedral.  —  Sp., metathesized  fr.  L.  capitulum,  ‘head  of  a  col¬ umn’,  dimin.  of  caput,  ‘head’.  See  capital,  adj., and  cp.  chapter.
.....
caesura
eaconym,  n.,  a  bad  name.  —  Compounded  of caco-  and  Gk.  ovupa,  dialectal  form  of  ovopjx, ‘name’.  See^pame  and  cp.  onomato-.
Derivative  :  caconym-ic,  adj. cacoon,  n.,  the  tropical  bean.  —  Of  uncertain origin.
cacophonous,  adj.,  ill-sounding.  —  Gk.  xaxo- tpcovo?,  compounded  of  xaxo-  (see  caco-)  and tpouvY),  ‘sound,  voice’.  See  phone.  For  E.  -ous, as  equivalent  to  Gk.  -04,  see  suff.  -ous. cacophony,  n.,  a  harsh  or  discordant  sound.  — Gk.  v.axotpomi,  fr.  xaxocpcovos.  See  prec.  word and  -y  (representing  Gk.  -(a) .
Cactaceae,  n.  pl„  the  cactus  family  (hot.)  — ModL.,  formed  fr.  cactus  with  suff.  aceae. cactaceous,  adj.  —  See  prec.  word  and  -aceous. cactiform,  adj.,  resembling  a  cactus  in  form.  — Compounded  of  Cactus  and  -form, cactus,
```


### [2026-09-06T15:12:26.044Z] TOOL RESULT

```
- 114 -
vd. 3 (105)), /i'lstak (vd. 13 (13) GL, (22), (24) (aw.
roya-)), ynstahlh (vd. 9, (109) — der Commentar denkt
falschlich an np. y ästen, /ez-em): ai. svvda-; arm. l^irtn
(H. Xo. 291).
kurd./«, /öh, /oi 'Schweiss'; af/. yyale (f. pl.); oss.
yed (300, 2); bei. hed, n. ÄtJ (158); wa/. yß, sar. y«/().
514. /''^Ä ^verwandt, angehörig; selbst (eigen)', y^esävend^
yj^estefi, yyeskär^).
aw. vergl. y^aefU" angehörig, verwandt'; phlv. /«'es,
y^esih^ yHslmtan, y^'äskär, y^eskänh.
wa/. /is, sar. yeiy 'Verwandtschaft, Familie*.
Fr. Müller nimmt (WZKM. 5, 187) sehr unwahr-
scheinlich die Instrumentalform aw. ^/^aetusa als Grund-
form für np.y^es an. — Bartholomae (briefl. Mitteilung)
denkt dagegen an ein ap. *kwäisiija' als Grundform;
zum Suffix 'ttja- vergl. ai. -tya-, Whitney, § 1245, b.
515. -^f^en (dialektisch yec) 'Pflug'.
aw. aem- (vd. 14, 10 (43)); phlv. /es(?).
Darmesteter, Et. ir. I, 77.
51G. ^j!lm 'Naturanlage, Charakter'-), vergl. hed^hn^ dns/lm,
duzyim {Vis und Ramm S. 32 V. 5 v. u.).
aw. vergl. haya-^ haem vd. 13 (124), pancö^\hya-
(Geldner, KZ. 30, 514 Note 1); phlv. /I?« bezw. /n;j
(vd. 13 (124), 5 (117) Gl.), huyjm (Gemme, ZDMG. 44,
068 No. 105), dus/wu
Anders und falsch Fr. Müller, WZKM. 5, 187; die
Bedeutung der aw. Worte steht jedenfalls fest.
517. x^?/'^» yJ^ 'Speichel', ylin (Gazophyhicium s. v.
saliva, Vullers s. v. ylm No. 3).
aw. gereöi.']yava'^ yt. 15, 47 (?); plilv. ;^ay?7Ä; (y. 38
(13) GL), yaya (Bund.).
Justi, Bund. s. v. yayü,
AM. gebraucht die Form yeön (208 Zeile 3 v. u., 209
*J Bedeutet auch bei Firdüsi 'fleissig, rechtschaffen* wie im
Pehlevi; ein np. ^^'es *Pflug' statt j^es (No. 515) giebt es nicht.
2) Reimt auf htm (Via und Rämln S. 51 Vers 9; 166 Vers 13),
dns sohon damals nicht mc»]ir bem gesprochoii wurde.
```


## [2026-09-06T15:12:47.599Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la KLN_1971.txt && grep -c \"\" KLN_1971.txt && grep -n \"cabalist\\|cachalot\" KLN_1971.txt | head"
}
```


### [2026-09-06T15:12:47.672Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 10278576 Sep  4 14:06 KLN_1971.txt
271509
36163:cabalist, n., a student of cabala. — A hybrid 
36166:Derivative: cabalist-ic , adj. 
36308:cachalot, n., the sperm whale. — F., fr. Sp. ca- 
39294:cable, cachalot, caisson, caitiff (which is a dou- 
150223:gadic and cabalistic literature (Judaism). — 
181637:Physeter, n., cachalot, sperm whale {zool.) —
```


## [2026-09-06T15:12:49.183Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 120 122 124 126 128; do echo \"=== awk leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KLN_1966.txt | grep -nE \"^[0-9]{2,4}$|^ *[0-9]{2,4} *$\" | head -4; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KLN_1966.txt | head -1; done"
}
```


### [2026-09-06T15:12:50.909Z] TOOL RESULT

```
=== awk leaf 120 ===
6:205
OF. bruisier,  ‘to  break’.  Both  OE.  brysan  and  OF. bruisier  derive  fr.  I.-E.  base  *bhreus-,  *bhres-, ‘to  break,  crush,  crumble’,  whence  also  OIr. bronnaim  (for  *bhrusnami),  ‘I  wrong,  hurt’,  bris- sim,  ‘I  break’,  brisc,  ‘brittle’,  Bret,  bresk,  of s.m.,  brezel,  ‘war’,  VL.  brisare,  ‘to  break’,  a word  of  Celtic  origin  (whence  F.  briser,  of  s.m.), Mir.  brtiim,  ‘I  crush’,  OE.  berstan,  OS.,  OHG. brestan,  etc.,  ‘to  burst’,  and  prob.  also  L.  frus¬ tum  (fr.  *bhrus-to-),  ‘piece’,  Alb.  bresen,  ‘hail’. Cp.  I.-E.  *bhrousmen,  whence  OS.  brosma, OHG.  brosama,  brosma,  MHG.  broseme,  bros- me,  G.  Brosam,  Brosame,  ‘crumb’.  Cp.  debris, debruise.  Cp.  also  burst.  Cp.  also  frustum. Derivatives :  bruise,  n.,  bruis-er,  n.,  bruis-ing,  n. bruit,  n.,  noise;  rumor  (archaic).  —  F.  ‘noise’, orig.  pp.  of  bruire,  ‘to  rustle,  rumble’,  used  as  a noun.  F.  bruire  derives  fr.  VL.  *brugere,  which is  a  blend  of  L.  rugire,  ‘to  roar’,  with  VL.  *bra- gere,  ‘to  whine,  cry’  (whence  F.  braire,  ‘to  bray’ (see  bray,  ‘to  cry’).  L.  rugire  (whence  VL.  *ru- gere),  ‘to  roar’,  is  cogn.  with  Gk.  Epuystv,  ‘to bellow,  roar',  opufraySog,  ‘a  loud  noise’,  pu£etv (for  *p(>Yi£iv),  ‘to  growl,  snarl’,  OSlav.  rykati, ryknQti,  ‘to  roar,  bellow’,  OE.  ryn  (for  *ruhjan), OHG.  rohon,  of  s.m.
=== awk leaf 122 ===
21:208
34:209
ffix and  accordingly  dropped.
=== awk leaf 124 ===
27:212
28:213
e.  —  G.  Burggraf,  lit.  ‘count  of  a  castle", fr.  Burg,  ‘castle’,  and  Graf,  ‘count’.  See  borough and  grave,  ‘count’.
=== awk leaf 126 ===
49:218
50:219
cabalist,  n.,  a  student  of  cabala.  —  A  hybrid formed  fr.  cabala  with  suff.  -ist.
=== awk leaf 128 ===
isy.  —  F.,  ‘hypocrisy’,  for¬ med  fr.  prec.  word  with  suff.  -ise. cafe,  n.,  i)  coffee;  2)  coffeehouse;  restaurant.  — F.,  fr.  It.  caffi,  fr.  Turk,  qahve ,  fr.  Arab.  qahvah, ‘wine;  coffee’.  See  coffee, cafeteria,  n.,  a  restaurant  at  which  the  patrons serve  themselves  from  the  food  displayed  at  a counter.  —  Mexican  Sp.,  meaning  ‘retail  coffee store’.  Cp.  F.  cafetidre  and  see  prec.  word, caffeine,  caffein,  n.,  an  alkaloid  obtained  from coffee  and  tea  ( chem .)  —  F.  cafeine,  fr.  cafe, ‘coffee’.  See  coffee  and  chem.  suff.  -ine,  resp.  -in. cafila,  n.,  a  convoy  of  travelers,  caravan.  —  Arab. qdfilah,  fem.  used  as  a  collective  noun  fr.  qifil, ‘one  who  returns  from  a  journey’,  part,  of  qa- fala,  ‘he  returned  from  a  journey’, cafiz,  n.,  a  measure  of  capacity.  —  Sp.,  fr.  Arab. qafiz,  a  measure  for  com. caftan,  n.,  a  long-sleeved  garment  worn  in  Tur¬ key,  Egypt,  etc. — T atV.qaftdn,  fr.  Arab,  qaftdn, fr.  Pers.  khaftan.
```


## [2026-09-06T15:13:04.654Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==266' HRN.txt | head -50"
}
```


## [2026-09-06T15:13:05.827Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hāvana\\|h[aâā]vana\\|havana\" BRT.txt | head -20; echo \"=== haya/haem ===\"; grep -n \"haéma\\|haēma\\|haya-\" BRT.txt | head -20"
}
```


### [2026-09-06T15:13:06.445Z] TOOL RESULT

```
244
H.
1088. hämün *Ebene'.
Vergl. ap. aw. hama- 'derselbe, der gleiche', ai.
samd' 'eben, planus, in gleicher Lage befindlich*.
1089. fiaven 'Mörser', (AM. 132 Zeile 6), kaukas.-bergjüd.
heveng, arab. LW. hävun,
aw. hävmia- 'Mörser ; phlv. havan^ arm. LW. havan.
^^90. her* jeder, all'.
ap. haruva- all*, fraharavam (Bartholomae, BB.
XIII, 69) 'im Ganzen'; aw. haurva-; phlv. har, har[vJsp;
ai. sdrva-.
1091. hurrä ^Geschrei' (äähn. I, 17 Vers 66).
mhd. hurra, vergl. hurr (Interjection) , engl. dän.
schwed. franz. hurrn (s. Grimm, Wörterbuch).
Sollten die germanischen Worte, etwa durch
türkische Verniittelung (wo ich ein hurrä aber nicht
nachweisen kann), aus dem Persischen entlehnt sein ?
\ }(^92. hergiz jemals, je*, mit Negation 'niemals'.
ap. Vmkaramöiy *ein Mal' (Darmesteter, Et. ir.
I, 245 ; unsicher) ; phlv. akarc bezw. hakaix, luxharj,
phlv.-päz. hargij bezw. hargiz (PPGl.), püz. hargizi.
Np. hergiz gegen phlv. hakarc ist wohl durch her
beeinflusst.
i '1093. hezär 'tausend'.
aw. hazatlra- 'tausend'; phlv. ha zur, hazärak
'Millennium' , vergl. a^apanursTg' oi staayysXsTc nngd
üspaaig Hesych, arm. LW. hazarapet {/Mag/og,
oiaovo/iiog^ enirpoTrog); ai. sahdsra-,
af/. zar 'tausend*; LW. arm. hazar^ kurd. hazdr
etc.
1093**^^ hii^tr, hujir, yujlr 'schön', auch N. pr. (Sahn. III,
1191 Vers 985; 1239 Vers 1927; 1240 Vers 1936;
1503 Vers 127 u. ö. im DaqiqTstück).
aw. huci&ra-; phlv. hucihr.
Nöldeke, ZDMG. 46, 137.
```


### [2026-09-06T15:13:06.508Z] TOOL RESULT

```
4164:•  j.  a-»havana-m. 'Stösscl,  Mörserkeule': hävananO  yat  . .  'tumia  ^vlmanUt  (sd.) N.72.
13335:•  j.  däityo.kerata-  Adj.  'den  Vorschriften entsprechend,  nach  Vorschrift,  rite  ge- fertigt': havana  'ta  (NDm.)  V. /J.  8;  — bixfhr>m  °t»m  V.ig.ai.
16992:ahmya  saokre  'manas^a  (LS.  als  IS.)^* ahur?m  .  .  äyese  yesti  Y.  2.  2;  3ff.,  Vr.  2. iff.;  —  anahitai  pars  'mm  anahitayai pars  sao%rayäi  Ytio.  88;  —  yS  anyeke . .  'ma  */rastyrmti  (sd.)  frajasaiti  N. 104\  —  'mana  paiH.bfr>ta  .  .  hai/anSi/ .  .  :far»%»m  myasdim  ayese  yesti  Y.j,  i; 22. 1 ;  —  yB  paiti  ape  baraiti  nsit  'maine (DS.)  N.  6g;  6g,  V.  7.  77;  —  yeti  'ma antarat  naimai  .  .  (näml.  asti)  paiti *'manalHt<''>  [/a/ft']  barSit  N.6p;  — yS dim  */ra hinan  *antan  ätarpmla  'maca N.  68;  Yt  J2. 3  {'maia) ;  —  atrtmca  'mala taäaca  kaomala  havanaca  V,  5.  39;  14.8; —  hävanaHbya . .  taÜai . .  varpsäi . .  tavaca 'manS  Vr.  70,  2;  —  haomqsca  myaadqsia zao%rhca  'maca  . ,  gqmü  Y.4.1;  —  *Äava assma  hava  'mana  N.  108;  —  ha' ml  iara aSsmaca  'maca  N.  lo^;  lOj,  71T,  Y. 62, 9; — aat frabmtars  (näml.  lia/n'M  atahai) yai.. 'mqnca  fraksm  (sd.)  a%raeca  paiti.Öaräi N,  74;  —  yat  saota  ahurtm  mazdam  ya- zaiti  *mahmai  'man  (GS.)  paiH.bärHi  N. 70;  jo*^;  —  havanatm{^^)  daityS  gatui .  .  fratarqn  'mqn  (GS.)  aparqm  akrS  N. 79f  79t  —  y^  *""'  *taa/ayeiti  (sd.)  draitf wJ  . .  N.  100.
19128:•  j.  ni'tama-  Adj.  (fem.  'ms-)  'der  unterste, am  tiefsten  befiadliche'  (nach  Lage,  Grösse, Zahl,  Dauer  usw.):  °ma?hia  gätuha  hasa- t9rS.Umahvaca  "an  den  tiefstgelegenen  und ganz  finsteren  Orten"  Yt  15. 53  {?);  —  'macit avatlqm  stsrqm  (sd.)  ya'ha  .  .  "die  klein- sten .  ."  F.  4  a;  —  cvatbya  nä  'maübya havana^bya  (sd.)  ratufri^  "wie  gross mindestens  . ."  N.  108;  —  fratamim  dat'ä- hSus  nava  Pfriems  (sd.)  .  .  m^»nts . .  'ntü ft'jrJ  V.2.  30;  30'';  —  *äjata  nU  *''ma'^ bansmana  ratu/ris  'Ü.QO;  —  *cvaia  (sd.) nä  *'ma'^  vaca  gahä  srävayS  ratufril "quanta  minima  voce , ."  N.  27;  —  dvadasa Vitara  (sd.)  upima  nava  . .  mäb>ma  xi^a/. . 'ttia  (NPm.)  V.  14.  14;  —  cvat  'mum haslnm  (sd.)  anhat  .  .  N.  J/;  —  'macit *haoma.küiiil  hazatgraynyai  astt  dalvanqm "auch  die  geringfügigste  //! -Kelterung  dient dazu  tausend  D.   zu   töten"    V,  70.  6;  6*;
19855:hin    und    her   bewegen':    sa/   havananö
24761:Knochen  und  Haare  und  . .  auf  der  Erde  |  •  j.  raeÖTwiä.bajina-  n.  'Mischgefäss,  -krag, durcheinandermengtf'  Yt.  JO.  72;  —  _)'J  -becher':  yaslqm  eayanqm  a^aurune  .  . *'xhtdra  (sd.)  *yat  vä  yazanti  yat  vä  urunya  'jina  (NP.)  havana  Y.I4-&;  — *hqm.rathwmii  N.6/";  62  (wo  rae%wa- ,  xSüudrinqm  payatfhqm  paifi-barat  yi^a yanti).  z)  'unmittelbar,  direkt  in  'Rs-\^ri^  3^ar»ma  *'6aßnS'^  (GS.)-**  ",  .  drei riihrung  treten  mit—,  Einfluss  üben  auf— '"' Schluck  aus  dem  Mischgefäss"  N.67;  — {ft}i^.y.CDa{  asie  spa..Äqm.rai%wayeiH  fziai  äal  tütrinqm  yaha  'äris  i^anma  'finS faiH.ral^wayeiti(%A.)^.$.ZZ.  a)insbes.  (G"s.)3>  H.'66. von    ansteckender,    verseuchender  Beruh- 1     ^e'-  ■ '
27770:ai.  havanairüt-  Adj.  —  ')  F  l  hat  zweimal  11.  —
29549:havana-
29564:•  j.  havana-  m.  ('Auspresser,  Kelterer') Name  für  die  beiden  Teile  des  loi  Haoma- bereitung  verwendeten  Geräts,  spez.  beim ffaemamÖTsti  des  Trogs  und  Stössels*': fraiarfm{&A.)(it  tl  °»?m  . .  upa.staotni  . .  yö qsui * hanglurvayete  upanmat''  U  °n»m.. yahmi  niyne  nars  aojanha  "das  erstere (untere)  Stuck  deines  (des  Haoma-)bAÖt- sers  . .,  das  die  (.ff<zii/nii-)Zweige  aufnimmt, und  das  obere  , .,  womit  ich  hineinstampfe mit  Manneskraft"  Y.  lo.a; — ^d3ityö*ainyS havanS  *däityS  *ainyS  ya%a  *va  *däifys hita  "der  Vorschrift  entsprechend  sei  das eine  Stück  des  (Äiiowa-) Mörsers  und  der Vorschrifl  entsprechend  das  andre,  auf dass  beide  der  Vorschrift  entsprechen,  wenn sie  verbunden  sind"    N.  J07,  a)    Du,
29878:•  1.  havanan-  m.  Name  des  ersten  und    .      n     ji  i\     ■       ^,      --^        ....
=== haya/haem ===
10644:•  j.  xrlohaya-  den.  Praes.  31,  nur  mit \fra  'erschüttern'.
19578:•  j.  'mad-  V.  'sich  berauschen'.  Fraes.  2 ma^a-,  24  mahaya-.  —  PPfP.  °masta-'^.
25282:•  g.,  j.  rah-  V.  'abtrünnig  sein;  —  machen'. Praes.  29  ransya-'^,  30  (Kaus.)  rJw- haya-.        Vgl.  ränla-.
25986:•  j.  'sand-,  p.  ^a''d-  V,  'videri'.  Praes. 13  b  lan-'^,  34  sahaya-,  sadaya-,  %adaya-f 36  sa^ya-,  30  (Kaus.)  smdaya-.
29497:haya-
29499:•  j.  haya-,  hya-^''  n.  'Eigentümlichkeit, eigen lütnlicti es  Gebahren':  asti  ii  (näml. sünahe)  Aaim  ya^a  .  .  "er  (der  Hund) zeigt  ein  Gebahren  wie  . ,"  V.  ij.  44*;  — ai/i  sl  (näml.  sBiiahe)  '"hatiH'^  yd^a  .  . "soviel  Gcbahningen  zeigt  er  (der  Hund) wie  .  ."  V.jy.  45-48*.
```


## [2026-09-06T15:13:25.149Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD leaf 115/116 (printed 94/95) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==116' PHD.txt | head -20 | cut -c1-1500"
}
```


## [2026-09-06T15:13:26.195Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hāwan\\|h.wan \\[\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB ===\"; grep -n \"xēm\\|xem\\|hāwan\\|hawan\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T15:13:26.660Z] TOOL RESULT

```
=== PHD leaf 115/116 (printed 94/95) ===
ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
wénig go wihéz(ag)
wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guà
```


### [2026-09-06T15:13:26.734Z] TOOL RESULT

```
PHD.txt:396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
PHD.txt:3659:similarity hāwandīh; v. likeness.
PHD_mackenzie.txt:2873:Ihawan [h'wn' I N -] a mortar.
PHD_mackenzie.txt:2874:2hawan [h)wn' = Av. hawani-] the morning giih.
=== NYB ===
736:ašgihānēh [’Sgyh’nyh] laziness, indolence 8416, — Thus spelt, with a marked g, Mx Cod. K here and ch. 515; in the same ch. also 'šygy'n (possibly only a slip of pen for 'šgyd'n) and *šgd*nyh (no mark over g). These spellings represent respec- tively: ’Sgyh’n a form ašgihčin, ’Sgyd’n, ’sgd’n a form ašgtyān, exemplifying the common alternation of intervocalic -y- : -h-, cf s. v. apasthistan and doublets such as drāyītan: drāhītan, x¥ahét: x“dyisn, ete. The common BP spelling is ’Sgh’n, passim. However, the Paz. forms are aš(a)gāhan, as(a)Jgahän; MPrs "jg?" P?nyy (Henning, GGA 1935, 14); NP ažgahān, ažgān, ažhān (BQ) + ažgin (Steingass). The forms with -gà- seem difficult to reconcile with aš- gihän, asgiyän. — I do not insist on the etymology in HP II, 24.
2987:passand [psnd] lenity, in a juridical sense: reduction of what the law formally pre- scribes in any special case, as opposed to dätistän (g. v.), 701. — passand and dätistän are symmetrically opposed juridical terms, defined and exemplified in the Syriac Corpus iuris of I$6*boxt (Syrische Rechtsbūcher, ed. by Sachau, III, 1914, 12-14): — Suppose a man owes a sum and equally as much in interest fallen due, but cannot pay the sum total be- cause of poverty, illness, or the like; if then, at his request, the creditor remits the interest and rests content with the capital, this is passand. On the other
4285:xem [hym] nature, disposition, temper 9018.19.23. v. also vat-xēm. — Cf Av. (1781) haya-, hya- ‘peculiarity’; hence Olr *haiman- or the like. Paz. NP xim.
```


## [2026-09-06T15:13:39.708Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['xém [hym]','xēm [hym]','xem [hym]','1hàwan','hàwan [h?wn','hāwan']:\n    i=t.find(pat)\n    print(repr(pat), i, 'leaf(0b)=', t[:i].count('\\f') if i>0 else None)\n# find x section\nimport re\nfor m in re.finditer(r'x[eēéè]m\\s*\\[hym\\]', t):\n    print(m.group(0), m.start(), 'leaf0b=', t[:m.start()].count('\\f'))\nEOF"
}
```


## [2026-09-06T15:13:40.529Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v2_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt incoming/BQT/BQT_v3_pages.txt; do echo \"=== $f ===\"; ls -la $f 2>/dev/null; done"
}
```


### [2026-09-06T15:13:41.516Z] TOOL RESULT

```
'xém [hym]' -1 leaf(0b)= None
'xēm [hym]' -1 leaf(0b)= None
'xem [hym]' -1 leaf(0b)= None
'1hàwan' -1 leaf(0b)= None
'hàwan [h?wn' 96658 leaf(0b)= 66
'hāwan' 96735 leaf(0b)= 67
```


### [2026-09-06T15:13:42.975Z] TOOL RESULT

```
=== BQT_v2_pages.txt ===
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
=== incoming/BQT/BQT_v4_pages.txt ===
-rw-rw-r-- 1 sfmqrb sfmqrb 2055176 Sep  4 14:06 incoming/BQT/BQT_v4_pages.txt
=== incoming/BQT/BQT_v5_pages.txt ===
-rw-rw-r-- 1 sfmqrb sfmqrb 723928 Sep  4 14:06 incoming/BQT/BQT_v5_pages.txt
=== incoming/BQT/BQT_v3_pages.txt ===
-rw-rw-r-- 1 sfmqrb sfmqrb 2499427 Sep  4 14:06 incoming/BQT/BQT_v3_pages.txt
```


## [2026-09-06T15:13:50.766Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'\\[hym\\]', t):\n    s=max(0,m.start()-120)\n    print('leaf0b=',t[:m.start()].count('\\f'), '|', t[s:m.start()+120].replace('\\n',' '))\n    print('---')\nEOF"
}
```


## [2026-09-06T15:13:50.807Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"هاون\" incoming/BQT/BQT_v4_pages.txt | head -20"
}
```


### [2026-09-06T15:13:52.741Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T15:13:52.789Z] TOOL RESULT

```
562:زمین جبل » و۸ ماهین ‏ عبارتند از ماه سره که دینور باشد و ماه کوفه که نهاوند باشد » واغلب
563:بآن دو ۶« ماه سیذان > را افزابند و جمله را ۶ ماهات > نامند » و با نهاوند را به « ماه دیتار >
1497:خوانند . کوبند حذیقه بمد ازفتح‌همدان بنهاوند | بمد ازآن دختری‌آورد تور لام کردند و منوچهر
1498:آمد و چون نهاوند كوچك بود وکنجایش سپاه | ازآن دختر بهم رسید 9 .
1500:وهرچه‌سپاه صره بود بنهاوند فرودآمدند وجون کشیده » مادرشا کمونی است وشاکمونی باءتقاد
1501:ماه بزبان پهلوی شهرومملکت راکوبند نهاوند کفرة هند پیغمبر صاحب کتاب است .
4088:هاونط۲ 33080۷ در با ۹۵ :۷ ) ذکر شده است ( رك : اسشق ۹۸۶ ؛ پور داود . سنا اص
4921:دوفراری از نهاوند بغور آمدند و درین ناحیه مقام کردند و گفتند : « زومندیش » آن موضع را
5784:هم والی کابل ات که رستم از دختر او تولد | بمعنی هاون باشد مطفاً خواء هاون سنگی باشد
5817:8 - ( مر ) « مهرای » بروزن مفتاح بانه و هاونی است که کوییده میشود پاوکندم -
11751:ایور است بمتی‌شپرشاپور٩‏ ولهاوند مت شهن ام بینی‌ودهان اغ مه وس است-
11762:۹ - ققه‌اللقهٌ عامیانه . رك : نهاوند . ۷ - رك : نهادن -
11895:نهان پیگران - بنتم بای فرسی . نهاوند * - بکراولوتحواووسکون
11948:هم‌آمده است و یکثرت استممال نهاوند شد.۴ - صلوات ال علیه وآله می‌بودند +
11951:نهاوندی ۴ - بکر اول بروزن | که نه‌آسمان باشد .
11953:کرامندی , منسوب بنهاوند راگویند - و نام نه‌خر اس ‎٩‏ - با غای قله‌دار» بممنی .
11955:پرده‌ای هم هست ازموسیقی * واین غیرازنهاوند | به حصاراست که کنایه ازنه‌آسمان باشد ‎ .‏
11982:۹ - نام ناحیتی است در جنوب غربی ملاین . مر‌کز آن شهر آنهاوند دارای ۱۰/۰۰۰
11988:۴ - چنان‌کز سینه غم را بیخ برکند فروگفت این غزل را در نهاوند .
11992:۴ - از : نهاوند+ی (دبت).
```


## [2026-09-06T15:14:01.749Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4075,4100p' incoming/BQT/BQT_v4_pages.txt; echo \"=== page tags near ===\"; awk 'NR>=3950 && NR<=4100 && /pdf page/' incoming/BQT/BQT_v4_pages.txt | tail -8"
}
```


## [2026-09-06T15:14:02.912Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5540,5560p' PHD_mackenzie.txt; echo \"--- ff count ---\"; python3 -c \"\nt=open('PHD_mackenzie.txt',encoding='utf-8',errors='replace').read()\nprint('ff total',t.count('\\f'))\ni=t.find('xeIYl [hym]')\nprint('leaf0b',t[:i].count('\\f'))\n\""
}
```


### [2026-09-06T15:14:03.634Z] TOOL RESULT

```
مغ - بفتح اول و سکون ثانی ۰ بممتی مغاث ۱ » با ای مثلئه بروزن پلای ؛
ژرف است که بعربی عمق خوانند ۴ - و بمعنی بیخ درخت انارصحرائی‌است که بعرپی رمان‌البری
رودخانه هم‌آمده است - ویضم اول » آتش‌پرست | خوانند » ونوعی‌ازآن بغدادی و لوعی‌هندی است
راگویند ۴ - و بکسر اول مخفف میغ است * | و آن سفید بزردی مابل میباشد . کوفتکی
وآن بخاری باشد تیره وملاسق زمین . وشکتکی اعنا را فافع است. ۱

‎٩‏ - براساسی تیست ( رك : شیراز ) اما عمروین‌لیت بارس را تخیر کرد . راك : تاریخ
سیستان س ۲۹۷-۲۸4 وراه : فهرست کتاب هزبور : شیراز. ۲ - ابوالولید من ین زائدة
ابن‌عبداله شیبانی یکی ازمشهورترین بخشند کان ودلیران وفصیحان عرب ۰ وی عهد اموی وعبامی
را درك کرد ودر ۱۵۹ ۸ . در گذشت « اعلام زرکلی ج۳ ص ۱۰۵۹

‏۴ - اوستا - 1333802 ( سوراخ ) » پهلوی 133813 . از همین ریشه است « مفاکه >
(هم.) « اسشق ۹۸۵ > ۴ - در اوستا یکبار كلمة 7308130 ( در ضم ن كلمة م رکب
هاونط۲ 33080۷ در با ۹۵ :۷ ) ذکر شده است ( رك : اسشق ۹۸۶ ؛ پور داود . سنا اص
۹) . ۸1655102 بیز برهمین عقده‌است » اما استاد بئونیت ارتباط اين‌کلمةٌ هر کب‌را با «مغ»
رد کرده ريشةٌ مغ را 13388 میداند که با 12282 همربشه است «مفان در ابران باستان س۱۲-
۴۳ اما کلمات دیکری که از ريشة همین کلمه است مکرر در خودگانها آمده است » از آن
جمله امت 33888 (یسا ۲۹ :۱۱ ؛ سنا ‎24٩‏ : ۹۶ ! سنا ۵۱ :۱۱) . عفران اروپایی اوستا
این‌کلمه را بمعانی مختلف گرفته‌اند . گر این کلمه را با لفت سانسکریت 1732802 که بمعنی
ثروت و پاداش و دهش است مربوط داسته » بمعنی دهش و بختش بگیریم مقرون تر صوابست
« پورداود. ایضاً > , درکتیبهٌ داربوش‌بز رکه در بهستان (بیستون) مکرر11308 (مغ) آمده‌است -
کمانا که باسم بردیا برادر کبوجیه و پسکوروش سلطنت هغامنشیان را سب کرده خود را پادشاه
خواند , يك مغ بوده است . درتورات و انجیل نیز چندین بار باین اسم برميخوريم : در کناب
آرمیا باب۳۹ بند ۳ راجع بلشکر کشی بخت اضر ( نب وکدتزر ۹*۵ - ۹۲ ق.م.) باورشلیم در
جزو سران وخواجه‌سرایان و سرداران ؛ بز رکه مفان ( 1332 ۳30 ) نیزهمراء پادشاءبابل بود.
در مآخذ چبنی این کلمه بسورت ۸10-121 آمده . نوسند گان بونان آنرا صورت ۸4801 ۰
=== page tags near ===
[pdf page 100]
[pdf page 101]
[pdf page 102]
[pdf page 103]
```


### [2026-09-06T15:14:05.248Z] TOOL RESULT

```
xar [HMRA < A lJ,mr); hll N.......,] donkey, ass.
xar [h)ll M x)r, N .......,] thorn.
xar- buz [hlbwc I M xrbwz] oryx.
xar.g6A [hlgws IN.......,] rabbit, hare.
xaroIYland [h)[>wm1zd] thorny.
xar-puAt [h)lpwst IN.......,] porcupine, hedgehog.
                        '
xastan [hstn' I M xst, N .......,] wound, injure.
xa§en [hsyn' I N xaJ'in] (dark) blue.
xayag [h)d(y)k I N xaya] egg.
                     '
 . . . . -des [-dys] oval, egg-shaped.
xayiig [he)dwk ' I N xayii] saliva, spittle.
xaz [hz IN.......,] marten.
xeIYl [hym] nature, character.
x~AIYl eysm, hfm I M xysm, N xism] anger; the demon Wrath.
 . . . . en [-yn l I M -yn] angry.
xindag [hyndk I M xyndg] ill, sick.
                           '
 . . . . ih: illness, sickness.
xir [CBW' < A ~bw; hyll M xyr] thing, matter.
--- ff count ---
ff total 259
leaf0b 115
```


## [2026-09-06T15:14:15.780Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== خیم in v2 ===\"; grep -n \"خیم\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-06T15:14:15.837Z] TOOL RESULT

```
=== خیم in v2 ===
363:‫جاجم = بر وزن خادم » پلای را‬                               ‫تخته‌ای باشد‬   ‫آن‬   ‫خیمه را گوبند ‪ ,‬و‬            ‫کلِجة‬
365:                                                               ‫سوراخ دار که برسر نون خیمه گذارید‪۰ ۳‬‬
3836:         ‫‪۱‬‬                 ‫معرب آن‌شوذر (بفتح‌ارلوسوم) «نفی»؛ خیمه ‪ ۰‬سایان » بالاپوش زنان» ردا‪.‬‬
3851:‫وبقاف زده » معروف است ‪ - ۷‬ولوعی از خیمةٌ‬                     ‫نصب لمایند وزنجیری با چند حلقه وچهار تمه‬
3895:                                           ‫است ‪. 4‬‬          ‫دورهند‪ .‬راوتی گوبند ‪ - ۷‬و خیمة مطبخ رالیز‬
6057:    ‫‪:‬‬     ‫رک‬   ‫رشه های ضخیم آن مواد غذابی بسیار مخصوصاً قند اندوخته میشود ‪.‬‬                             ‫در‬   ‫و‬   ‫است‬   ‫متعدد‬
6960:  ‫ویای احزنا‬    ‫است ‪ -‬و آنجه زان بر دست‬                ‫چتاب = بروزن‌طتاب ‪,‬کلیچخیمه(‪)۱‬‬
6977:                                  ‫‪ :‬بدان‪.‬‬     ‫)‪ (۱‬چش‬                ‫(‪ )۱‬خم ‪ : ۳‬کلیم خیمه ‪.‬‬
7104:                ‫سپه خیمه زد در شیب و فراز ‪.‬‬             ‫* ‪ -‬رسیدند زی‌شهر چندان فراز‬
7621:‫نوعی ازخیمه باشد‬        ‫چهار اکارن ‏‬               ‫چه = بنتح اول و ظهور انی » مخفف‬
7629:‫است که خیمة شروانی ¬ وچپارحد جهان باشد‬             ‫مقام استفار استعمال کنند‪ - ۴‬وصقت کثرت حم‬
7634:    ‫چهار آ لین‪ -‬بمعنی‌خیمة چگها‬                      ‫نم«تواند‬
7673:‫چهار طرف عالم ‪ -‬و کنابه اعنزاصر ارعه‬                               ‫خلفای اربعه ‪ -‬وخیمة چهار گوشه باشد ‪.‬‬
7683:‫چهار طاق ‪ -‬نوی از خیمه است که‬                          ‫چهار بسیطت کناب از عناص اریمه | _‬
7933:  ‫‪ - ۴‬ازترکی «چیغ» نوعی حصیز که‌ازلی‌بافته ودرجدارهای خیمه‌اصب‬           ‫(ه‪.‬م‪ ).‬است ‪۰‬‬
7935:                                ‫کننده توعی برده حصری که در مدخل خیمه آویزند‪« .‬جفتای ‪۹۳‬‬
10720:                                                        ‫نشیب‌باشد‪ -‬وخیمه؟ ‪ -‬وطاق وابوان » وهرچیز‬
11042:                     ‫خیم بزر که برپای کنند ‪.‬‬           ‫خرده بین باربك بین را گونند ‪ -‬و بمعنی دندان‬
13380:                                                                         ‫خیم ‪۰‬‬    ‫رك‪:‬‬         ‫‪۹‬‬
15530: ‫جهانگیری‌بمعنی اولکه خیمهٌ کتان باشد باسین‬                           ‫= بروزن‌بیجیدن ؛ بم‌عنی‬         ‫خیز بدن ‪°‬‬
```


## [2026-09-06T15:14:18.024Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; do echo \"=== $f ===\"; grep -c \"هاون\\|هاؤن\\|ه‌اون\" $f; done; echo \"--- last printed page tags v4 ---\"; grep -o \"\\[pdf page [0-9]*\\]\" incoming/BQT/BQT_v4_pages.txt | tail -3; grep -o \"\\[pdf page [0-9]*\\]\" incoming/BQT/BQT_v5_pages.txt | tail -3"
}
```


### [2026-09-06T15:14:20.169Z] TOOL RESULT

```
=== BQT_v1_pages.txt ===
11
=== BQT_v2_pages.txt ===
10
=== incoming/BQT/BQT_v3_pages.txt ===
5
=== incoming/BQT/BQT_v4_pages.txt ===
39
=== incoming/BQT/BQT_v5_pages.txt ===
1
--- last printed page tags v4 ---
[pdf page 551]
[pdf page 552]
[pdf page 553]
[pdf page 291]
[pdf page 292]
[pdf page 293]
```


## [2026-09-06T15:14:27.205Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=13300 && NR<=13400' BQT_v2_pages.txt | grep -n \"pdf page\"; echo \"---\"; sed -n '13370,13395p' BQT_v2_pages.txt"
}
```


## [2026-09-06T15:14:27.619Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"هاون\" incoming/BQT/BQT_v4_pages.txt | grep -v \"نهاوند\" | head -20"
}
```


### [2026-09-06T15:14:29.158Z] TOOL RESULT

```
---
   ‫از‪:‬‬       ‫راظ‬     ‫‪۴‬‬     ‫‪« _ ۴‬خلش‪ .‬گگنلدیده» «لفت فرس ‪۰ ۹۲۷۰‬‬                ‫‪:‬خلاش‪.‬‬   ‫رك‬     ‫‪۱‬‬


  ‫‪.‬‬       ‫‪.‬یارسی بامتان ‪_ap)n(ak‬‏ ‪« #‬اسقا‪۲ :۱‬م‪۰٦۰‬‏ وخمیدن ازهمن کمه‌ساخته شده‬                 ‫خنب ‪00181‬‬
          ‫‪x‬‏‪nux)kabnu‬‬
                    ‫‪:‬نب « خەب یپلوی ‪ka(b‬‬
                                       ‫‪ ۵9‬از خ‬                         ‫‪ 2 ۴‬خن («م)‪.‬‬
             ‫«اسفا‪۱:۲‬ص ‪۹۵‬و‪ ۷۰‬در اوراق مانوی (پارتی) ‪( ۵/۸0۳5‬کوزه» سبو)‪. ‎‬‬                   ‫‪mu‬‬
                                                                                             ‫اومتا‪abX ‎‬‬
  ‫‪(Henning,‬‬              ‫‪A list of Middle Persian..., BSOS,‬‬            ‫)‪1,۱,۵. 89.‬‬
                                                                         ‫خیم ‪۰‬‬    ‫رك‪:‬‬         ‫‪۹‬‬

            ‫ببانگ شیشم‪ .‬بابانگك افسرسگزی‬                  ‫‪ - ۷‬بگیربادة نوشن ونوش کن بصواب‬
             ‫بلحن مويهة زال و قصيدة لعبزی‪.‬‬
                                                           ‫بلفط پارسی و چینی و خماخسرو‬
      ‫‪.‬‬    ‫دامغانی ‪۲۱۱‬‬    ‫د منوچپری‬

         ‫ور کوه را ز عثبر درسرخمار باشد‪.‬‬                ‫‪- ۸‬کرسرو را ز کوهر برسرشمار باشد‬
      ‫د منوچهری دامفالی ‪.» ۱۲‬‬
  ‫خماهن‬                                                                                ‫مه‬

‫خمافیدن؟ = بروزن رسایدن‪ ,‬تقلید‬                   ‫خماشه » بر وزن ومعنی خلاشه است‪.‬‬
 ‫کردن گفتگو وحرکات وسکنات عردم راکوشد‬             ‫وهر چیز افکندنی وبکار نیامدنی را نگیوزند‪.‬‬
‫که بطریق تمسخر باشد و آنرا شیرازبان والو‬         ‫خمالیون ‪ - ۱‬بکرلا وتحتانی بواو‬
 ‫چانیدن خوانند» وآیورردن همگویند ‪ -‬وبمعنی‬        ‫کشیده و نون زده » بیونانی نوعی از مازریون‬
              ‫کجردن وخم نمودن هم هست ‪.‬‬          ‫سیاء است» وبعضی گویند خربق‌سیاء است کهآنرا‬
```


### [2026-09-06T15:14:29.210Z] TOOL RESULT

```
4088:هاونط۲ 33080۷ در با ۹۵ :۷ ) ذکر شده است ( رك : اسشق ۹۸۶ ؛ پور داود . سنا اص
5784:هم والی کابل ات که رستم از دختر او تولد | بمعنی هاون باشد مطفاً خواء هاون سنگی باشد
5817:8 - ( مر ) « مهرای » بروزن مفتاح بانه و هاونی است که کوییده میشود پاوکندم -
11751:ایور است بمتی‌شپرشاپور٩‏ ولهاوند مت شهن ام بینی‌ودهان اغ مه وس است-
16012:‎٩‏ اوستا 84۷۵02 (هاون) . پهلوی 88۰88 ۰ ارمنی ع » لهجدٌیپودبان
16013:جبال قنتازع 36۷۵۵ . معرب هاون 8۷28 « اسشق ۹*۸۹ درتعریب هاون (بفتح واو)وهاوون
16015:(هاون ) « ژابا س 4۵4 ۰ 38۷68 , 8۷60 ۶ ژابا س 4۳۹ ۲ ۵6۷6۴ « ژابا
16016:س 40۹ کبلکی 88۷888 (هاون ) » در اراك (سلطانآباد) ۵8۷308 (هاون) «مکی‌نزاد».
16017:اساسا هاون ( هاونه اوستایی) ظرفی‌است که زرتشتیان درآن «هوم» (ه.م.) را با دسته می کوین
16018:ولیز اهاون در دین زرتعتی بمنوان زنگه (ناقوی) بکار میرفت - عموماً هاون و دستةٌ آنرا از هس
16030:میکردند ۳ هاون
16032:هاون کوب ۴ - عسی را گوبند هاینه* سوها پینه بروزنآبنهوآبینه,
16049:۲ - مجاز ازمعثی اول. ۴ - در اوستا 128۷881 که اکنون « هاونگاء > کوبند .
16052:۴ - از: هاون (ه.م.) ۲- کوب (کوبنده)؛ لغة بمعنی کوبنده در هاون +
19655:آب زور وشاخه کوچکی ازاورهُرام 13۳۷87812 (شاخهٌ انار) درهاون با ترتیب ممین فشرده میشوده
20244:تحقه فرستند . آعنا هم کنته‌اند ‎٩‏ - و دستهٌ هاون را نیز
20284:ز برق لیخ روشن شد شب تار سردشمن چوهاون , گرز چون بار.
20626:یاه بنتح نون, بممنی هاون‌باشدمطلقً یاو « بروزن‌ساغش, بممنی باری‌دهنده
20627:و آن ظرفی است که چیزها در آن کوبند ۲ - | ومددکار باشده - و دستهٌ هاونرا نی زکویند۹" -
20640:- اوستا - 74۷87682 ( دستة هاون) ( 50 ,1 50001160 ,0610065) ‎٩‏ اسشق
```


## [2026-09-06T15:14:39.563Z] TOOL CALL #29: Bash

```json
{
 "command": "ls tools/ | head -30; echo ---; sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T15:14:39.619Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
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


## [2026-09-06T15:14:40.831Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=15900 && NR<=16060 && /pdf page/' incoming/BQT/BQT_v4_pages.txt; echo \"--- text ---\"; sed -n '16005,16055p' incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-06T15:14:42.708Z] TOOL RESULT

```
[pdf page 394]
[pdf page 395]
[pdf page 396]
--- text ---
1 «خأقانی غشروانی . دبوان صس۳۹۲*.

۴ - رك : هامرز . ۴ -ر4 : هاوشت . * - پهلوی 8۸۷1681 مغ
(ررخانی‌زرتشتی) » موبد «یولکرص۹4 ؛ شاکرد . روحالی جوان ( زرتشتی ) که در مراسم دینی
بقربانی کننده » پاری کند «دهارله ص۷۵>. دراوستا 8۵۷18۷068 آمده که درفرهنگهای فارسی
خزولغات زند وپازند ضبط شده وبمعنی امت گرفته‌اند «پورداود . خرده اوستا سح

‎٩‏ اوستا 84۷۵02 (هاون) . پهلوی 88۰88 ۰ ارمنی ع » لهجدٌیپودبان
جبال قنتازع 36۷۵۵ . معرب هاون 8۷28 « اسشق ۹*۸۹ درتعریب هاون (بفتح واو)وهاوون
ی واو اول )آمده « اين‌دزید > ۸« تفس» ۰ جمع‌آن « اهوان »> است « دزی جص44 ۷ کردی
(هاون ) « ژابا س 4۵4 ۰ 38۷68 , 8۷60 ۶ ژابا س 4۳۹ ۲ ۵6۷6۴ « ژابا
س 40۹ کبلکی 88۷888 (هاون ) » در اراك (سلطانآباد) ۵8۷308 (هاون) «مکی‌نزاد».
اساسا هاون ( هاونه اوستایی) ظرفی‌است که زرتشتیان درآن «هوم» (ه.م.) را با دسته می کوین
ولیز اهاون در دین زرتعتی بمنوان زنگه (ناقوی) بکار میرفت - عموماً هاون و دستةٌ آنرا از هس
آمباخته‌اند « دارمستتر . زید اوستا جاص آ]] 1-227 > ؛ ورك : پوردآود . بشتها اس 2۹۹ 4 م +
همین . مزدیستا . ص ۲۳۳ .
[pdf page 396]
۲۳۱۳۳ های های
معروف است ۱ - و کنایه از فرج زدان یمنی هایاهای ۱ - با ستای ر های بالف
موضع جماع ابغان هم هست ۴ - و بکس واو | کشیده و بیای‌حطی‌زده » شور وغوغای‌مانم‌زدکان
بلفت زند و پازند (۱) اراد : و واقعه دیدگان باشد ۷ .
پیاد اولاست ازجم ای و هایاهوی ۸ « با های بواو کشیده
ی وت 72 | وبیای حطی زده » شور و اغوغای ارپاب طرب
عبادتی که زردشت قرار ۳ تس : ومیزبانی وعروسی باشد برخلاف هایاهای که‌شور
داده بوده و تابمان او وغوغای هام زدگان است . َ
میکردند ۳ هاون

هاون کوب ۴ - عسی را گوبند هاینه* سوها پینه بروزنآبنهوآبینه,
که بجهت عطاران وطبیبان دارو واجزای معاجین مغفف هر آینه است که یممتی ناچار و لاعلاج
بیکوید - وم کب و سیاهی ساز را نیز کویند | ولابدا و بی‌شاك و بی‌دغدشه باشد ۴۰
وکنابه ازجماع کننده هم هست. های های ۰۱۶ پنکرار های , بیمنی

های * - بروزن و معنی وای‌است‌وآن | زود زود و جلد جلد و شتاب و تعجیل باشد -
لفظی باشد ‎)٩(‏ که دروقت دردی والمی وآزاری | و بمعنی هایاهای هم‌هست که شور وکریهٌ مسیبت
ومصیبتی پرزبان رانند . زدگان است .

() چك : ژند و پاژد . () چش : لفظی است .
- ظرفی فلزی ( غالیاً مسی ) با سنکی که درآن ادوبه و تخمپای گیاهان وغیره را با

دسته‌ای کوبند :

چند استخوا ن که «اون دوران روز کار خردش چنان بکوفت کم خاکش غبا رکرد.

سمدی شیرازی .
۲ - مجاز ازمعثی اول. ۴ - در اوستا 128۷881 که اکنون « هاونگاء > کوبند .
یکی ازاوقات پنجگانهٌ روز است » وآن وقتی است که در آن هوم تهیه میشود » و مدت آلرا از
برآمدن خورشید تا لیمروز قرار داده‌اند. ۶ پورداود . بفتها ای 2۹۹ ح» +
۴ - از: هاون (ه.م.) ۲- کوب (کوبنده)؛ لغة بمعنی کوبنده در هاون +
8 اسم صوت. قی :کردی های ۵ ( فرباد » احنار ) , 861 , 2 » ترکی های
«زاباه 2۶4 در خطاب بجای «آی». «ای» :
گفت موسی های خیره سر شدی خود مسلمان نا شده‌کافن شدی .
```


## [2026-09-06T15:14:59.051Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nt2=re.sub(r'[‎‏‪-‮⁦-⁩­]','',t)\nlines=t2.split('\\n')\npage=None\nfor i,l in enumerate(lines):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: page=m.group(1)\n    if 'خیم' in l and ('طبیعت' in l or 'خوی' in l or 'سرشت' in l or 'خُلق' in l or 'خلق' in l):\n        print(page,i,l.strip()[:300])\nEOF"
}
```


### [2026-09-06T15:15:00.988Z] TOOL RESULT

```
None 15594 خیمه ردن = کنابه از عجب و نکبر                                خوی وطبیعت باشد ١ ؛ وبعضی خوی بد راخیم
```


## [2026-09-06T15:15:05.691Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v2_pages.txt | head -3; echo \"---\"; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nt2=re.sub(r'[‎‏‪-‮⁦-⁩­]','',t)\nlines=t2.split('\\n')\nfor i in range(15560,15640):\n    print(i, lines[i].strip()[:250])\nEOF"
}
```


### [2026-09-06T15:15:07.401Z] TOOL RESULT

```
---
15560 ۔
15561 سشمدبهم
15562 ری‌چ
15563 بتراشند -وفی وچر کیکه‌در گوشها                                                                    را ناف ات 8.
15564 ولعابی که آزدهان وبینی مردم براید  -و بمعنی
15565 بر وزن فیل ۰             (ل)۲
15566 حیل  -بکر او
15567 اماب علدظی را بند که ازبینی‌مردم‌برمیآید ۴۔
15568 را    دبوانه ومحنون        هم آمده است ك           جراحت
15569 
15570 
15571 و بفتح اول درعربی بمعنی خیمه                نیز گوبند -        و بفتح اول در عربی بمعتی جماعت و طایفه
15572 باشد . ¥                                                                           ماش .
15573 خیمه از دق کنابه اآزسان است .
15574 خیل تاش  ۴ح بفوافانی بالفکشیدہ
15575 حیمه بصحر ا رذن = کنابه از                                   وك‌کریرا گوبند که                    ۰سیاهی    شین نقطه‌دار زده
15576 
15577 
15578 عایب شدن باشد  -ویمعتی آ شکارا وبی‌پرده بودن                    همه ازيك خیل وبك طایفه باشند .وصاح خیل
15579 .     هم ھت
15580 وسیاه را نز گفته‌اند ۳
15581 
15582 
15583 کنابه از               ندبی
15584 رخر ا
15585 خیمه در
15586 سقرارشدن وبیقراری کردن باشد-ءبی‌باك وبی‌شرم
15587 بودنرا نیز گوبند .             خیلو *  -با اول بنانی رسیده و الك
15588 خیمه د هر  -کنابه ازآسمان است .                             بکوشاویده *بمعنی خیروست * وان کلی باشد
15589 خیمه حراونیان = بمعنی‌خیمةدهر                                                                  کهآ برا خبازی نز گوند ِ
15590 
15591 است که آسمان باشد . ۸                  عیمن»ی
15592 ممبوزن
15593 حیم = بکر اول بر
15594 خیمه ردن = کنابه از عجب و نکبر                                خوی وطبیعت باشد ١ ؛ وبعضی خوی بد راخیم
15595 .   اول   بکر     - :    .چش    چك     ()۷                     -و.     ) (۱چش:
15596 
15597 ۰   خله   خل؛   :                    = ) grain de 0008رف( كل« ص. ٩۱۸ ۲                                          ۱
15598 تاش (بوند) (ه۰ )..           از :خىل (عر) (ھ.م+ ).                  ‌-
15599 در زد آنشس بخیل خان کرد .                     - ۴چون -خن گوسخن بآخر برد
15600 نظامی کنجوی« .گذچینه.۷۵
15601 
15602 - ۱بپلوی ( 00۵5طمیمت جنلی»جبه)  ,از اوستا_ 8۷25                                       .    رك< خىرو       _   ®
15603 
15604 هوشمان            ۱اسشق ۹              زیر گك ۳۱           ارتو لمه \\AY
15605 
15606 ( - ۷عر)«هرخانة گرداست ازخانهای‌اعراب»                                        .       ۹
15607 
15608 « شرح فاه‌وی
15609 - ۵زد نف ربهر سیح‌ملمم نقاب .
15610 خیمهٌ روخافان گشت معثبر طناب .
15611 “i      «خاقانی‌شروانی
15612 
15613 
15614 -بر اول  .مخفف آن خی                                بكگوه
15615 خخي
15616 *
15617 9۳
15618 
15619 ا
15620 
15621 
15622 
15623 ۹6:؛ آوند چره‌ین که در آن                    ۳۱
15624 ۰ص۲ :           ?غاا            (ھ .م) .
15625 مغات.   ,   کنند        جزآن     و   شره   ۰   روغن            ۰   آن
15626 =Aو
15627 
15628 
15629 
15630 
15631 خیناگر = باکاف فارسی‌بروزن تیرآور.                کردن وباد دربوق انداختن باشد .که آنهم کنابه
15632 و    ساز نده ومغنی را گومند ۳
15633 از برخاستن و برپایشدن آلت تناسل است -
15634 = بفتح واو بروزن بی‌خبر »        حینو ر            کونابه از فرودآمدن ومقیم شدن ولزول کردن.
15635 پل صراط رگاویند .                           ولشکر کشیدن و نوت نا
15636 حو  = ۴بسراول وسکون‌ثانی وواو,                      خیم نزگادی  -کنابه از آسمان
15637 آب‌دهن راگوبند؛ وبفتح اول وضم ثانی‌هم‌درست
15638 است .
15639 اكت ::      خیمه کبوه = بعنی خيمة زنکاری
```


## [2026-09-06T15:15:21.577Z] TOOL CALL #33: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:804 2>&1 | head -40"
}
```


### [2026-09-06T15:15:23.217Z] TOOL RESULT

```
no scan of BQT covers printed page 804 (see 'scans' in refs_online.json)
```


## [2026-09-06T15:15:28.022Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nraw=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds:', raw.count('\\f'))\nprint('first 300:', repr(raw[:300]))\n# look for page markers\nfor m in list(re.finditer(r'\\[[^\\]\\n]{0,40}\\]', raw))[:10]:\n    print(repr(m.group(0)))\nEOF"
}
```


### [2026-09-06T15:15:29.743Z] TOOL RESULT

```
formfeeds: 683
first 300: '\x0c                                         \u202b\u202a7\u202c\u202c\n\n                          \u202bرن\u202a۳\u202c\u202c\n    \u202bنات\u202c\n      \u202bا م\u202c\n              \u202bلض\u200cبال \u202a ۰ ۲۶\u202cرک\u202c\n\u202b\u202a۱\u202c\u202c       \u202bاسا تعدولیدیارتم و\u202c\n                                     \u202b\u202a7\u202c\u202c\n\u202b\u202a ۰\u202cو زل رسوا »وا روون لات سا روصا مواقم\u202c      \u202bوتان\u202c\n\n                      \u202b\u202a۴2 ۱\u202c\u202c'
'[ برای پرندکانماهی و غیرہ ]'
'[از\u202a:\u202cجنب اش (پوند اسم\u200cمصدر) ]'
'[ از » جنب \u202a +\u202cبدن (پوند مصاری )پ]'
'[ر \u202a :\u202cح\u202a.]'
'[یکرکاف ]'
'[ك \u202a:\u202cگاه ]'
'[رك \u202a :\u202cخامالا و خامالیون ]'
'[ رجوع به وال شود ]'
'[ک]'
'[که ابن\u200cدوم را آذرخراد کفته\u200cاند]'
```


## [2026-09-06T15:15:37.700Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nraw=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nclean=re.sub(r'[‌‎‏‪-‮⁦-⁩­]','',raw)\ni=clean.find('خوی وطبیعت باشد')\nprint('leaf(0b)=',clean[:i].count('\\f'),'of',clean.count('\\f'))\npages=clean.split('\\f')\n# print head of a few pages to spot printed numbers\nfor n in (1,2,3):\n    print('--- page idx',n,'---')\n    print(pages[n][:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T15:15:39.418Z] TOOL RESULT

```
leaf(0b)= 264 of 683
--- page idx 1 ---
                                         7 |  |                           رن۳ |     نات |       ا م |               لضبال  ۰ ۲۶رک | ۱       اسا تعدولیدیارتم و |                                      7 |  ۰و زل رسوا »و
--- page idx 2 ---
                   م و | نآکو سخنیم بیاموزد مرا |                        د د ل ج م ة چ ا ی د | على ۰             بند گر دا ند ۰                       ۳      ۳7 |  | داربان مقدمهٌ مجلد اول برحان قاطع ( صفحدٌ صد 
--- page idx 3 ---
                                                     ar |                                      مااضحاذفی |  است    و رسالههابی استفاده شده   نیز ( از 5    در محلد دوم (وطماً مجلد سوم |  |  | اسم    اسك        ا
```


## [2026-09-06T15:15:58.097Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt; echo \"=== hawan in MON ===\"; grep -n \"هاون\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10; echo \"=== kabl ===\"; grep -n \"کابل\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T15:15:58.181Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 incoming/MON/MON_2vol_Adena_v1_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 incoming/MON/MON_2vol_Adena_v2_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
=== hawan in MON ===
MON_part1.txt:882:پیمودن: آب به هاون کوبیدن. آب به کس 
MON_part1.txt:884:هاون کوییدن (کوفتن): عمل لغو و بیهوده 
MON_part1.txt:912:وی). آب در هاون سودن ( کوبیدن» کوفتن): 
MON_part1.txt:10316:گوشه که آلت‌های مخصوص از قیل هاون 
MON_part1.txt:10317:و دستهٌ هاون و برسمدان و طشت و ورس را 
MON_part1.txt:33632:ماه‌نهاوند» ماه‌یصر ه ما کو فه ماهی‌دشت و 
MON_part1.txt:45273:تهاون: 203۷0۵ [ع.] (مسص‌ل.) کوتاهی 
MON_part1.txt:45276:سهل‌انگاری؛ ج. تهاونات. 
MON_part1.txt:48799:جواز. 1۱32 کهازه - جوازه] (.) هاون 
MON_part1.txt:54312:واجب بوده تهاون نمایند. نخوت اباء. 
=== kabl ===
MON_part2.txt:16805:کابل: ا (.) مفتول فلزی لفاف‌دار و سیم 
MON_part2.txt:16809:کابل‌کشی: ۲:01 (فر. ف.] 
MON_part2.txt:16812:کابل. 
MON_part2.txt:28274:کولی: 0۳ ,-۸۷۱ [- کاولی - کابلی؟] 
MON_part2.txt:35103:آ تاکن بیر کابلی: ( کد.) دنیاه جهان. 
MON_part2.txt:90895:می‌روید؛ هلیلهةٌ کابلی» اهلیلح کابلی؛ اهلیلج؛ 
MON_part2.txt:90897:یکی از گونه‌های هلیله. هلیلهٌ کابلی: (گیا.) 
MON_part1.txt:350:(لندن)؛ اشتار (پاریس)» آهنگ (دهلی)۰ آریانا (کابل) و نیز در سالنامه‌های 
MON_part1.txt:57600:کلیک, کالوج؛ کابلیج.
```


## [2026-09-06T15:16:02.298Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16800,16815p' MON_part2.txt; echo \"=== havan headword ===\"; grep -n \"^هاون\\|هاون:\" MON_part2.txt | head; echo \"=== search hawan section ===\"; grep -n \"هاون\" MON_part2.txt | head -20"
}
```


### [2026-09-06T15:16:02.395Z] TOOL RESULT

```
خاک چینی جهت ساختن ظروف در 
مملکت چین انجام شده است؛ خاک چینی» 
کاباره: 02:0 (.) میکده. میخانه؛ 
مشروب‌فروشی. 

کابل: ا (.) مفتول فلزی لفاف‌دار و سیم 
زیرزمینی یا زیردریایی که جهت برق و تلفن 
وتلگراف‌بکا رآید. 

کابل‌کشی: ۲:01 (فر. ف.] 
(حامص.) کشیدن سیم‌های زیرزمینی یا زیر 
دریایی برای برق و تلفن و تلگراف؛ کشیدن 
کابل. 

کاینه: «معظ۲ [منظر ه] (1.) چشم. 
و ۵ (.) حالتی که به شخص 
=== havan headword ===
47354:متهاون: ۱۱۱۵۵۵۷۵۸ [ع.] (افا.) سستی کننده 
88804:هاون: ۵۷ (.) طرفی که در آن ادو به 
88811:هاونان: ممه۰2 ).٩(‏ یکی از هشت متام 
88813:هاونن» اتروخش» فربر تره آبرت؛ آسناتر 
88817:هاون‌دسته: (6-)۸5۱۸-.۱ (امر.) اسزاری 
88821:هاون‌کوب: ۰-0 [- همساون کونده] 
88827:هاونگاه: «تی.« (.) (زردشتی) یکی از 
=== search hawan section ===
2877:سروده نغمه. غناء نهاوندی: (مس.) نوایی 
3003:روغن از کوبین بیرون آید. هاون چوبین با 
16856:کابیله: (م)ه1آ2 [- کابیله] (ا.) هاون. هر 
16857:چیز که در آن غله کونند (عموما). هاون 
27711:عصا. دسته هاون. چوب گازران. ضصرب 
31347:ضرب کار حریف را تمام کند. دسته هاون. 
32346:می‌گفتند و آن کز کامل بود؛ مق. گز نهاوند 
32357:الخلقه؛ گز ملک .گر نهاوند: واحد طول در 
35761:طول شا ذراع. هاون و 1 
47354:متهاون: ۱۱۱۵۵۵۷۵۸ [ع.] (افا.) سستی کننده 
69269:مهراس: ۱۱ [ع. .]۳ ۱ هاونی است که با 
81684:ممی: فد نیشکر. نی نهاوندی: (گیا.) 
88804:هاون: ۵۷ (.) طرفی که در آن ادو به 
88806:جوغن» جواز» چپسین» مهراس. ضح. هاون 
88811:هاونان: ممه۰2 ).٩(‏ یکی از هشت متام 
88813:هاونن» اتروخش» فربر تره آبرت؛ آسناتر 
88817:هاون‌دسته: (6-)۸5۱۸-.۱ (امر.) اسزاری 
88819:چیزی را در هاون کوند. 
88821:هاون‌کوب: ۰-0 [- همساون کونده] 
88824:(ص‌فا.) آنکه در هاون چیزی را کوید. کسی
```


## [2026-09-06T15:16:18.246Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '88800,88812p' MON_part2.txt; echo \"=== FVQ habl ===\"; grep -n -i \"habl\\|ḥabl\" FVQ.txt | head -20; echo \"=== AFA habl ===\"; grep -n -i \"habl\" AFA.txt | head -10"
}
```


### [2026-09-06T15:16:18.341Z] TOOL RESULT

```
هاو: 5۷ (صت.) کلمه‌ای است که در هنگام 
حمله بر دشمن بر زبان رانند. 

هاون: ۵۷ (.) طرفی که در آن ادو به 
تخم‌های گیاهان و غیره را با دسته‌ای کوبند» 
جوغن» جواز» چپسین» مهراس. ضح. هاون 
یکی از آلات مقدس پرستشگاه زردشتیان 
نوده و در آن یاه هوم را سی‌کوییده‌اند. 
(کذ.) فرج زن. 

هاونان: ممه۰2 ).٩(‏ یکی از هشت متام 
روحانی دین زردشتی از این قرار: زئوتر» 
=== FVQ habl ===
928:4 'Ata' b. Yasar died in A.D. 712. Sco an-Nawawi, 424 ; adh-l)hahabl, i, 13. 
930:5 'Ata' b. Abi Rabah died in A.U. 733. See an-Nawawi, 422 adh-Dhahabl, i, 16. 
=== AFA habl ===
```


## [2026-09-06T15:16:20.410Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD cable ===\"; grep -n \"^cable\\|cable, n\" FSD_vol1.txt | head -10; echo \"=== AHD watkins kap ===\"; grep -n \"cable\" AHD_watkins1985.txt | head -10; echo \"=== SKT cable ===\"; grep -n -i \"cable\" SKT.txt | head -10; echo \"=== LKT ===\"; grep -n -i \"habl\\|kabel\\|câble\" LKT.txt | head -10"
}
```


### [2026-09-06T15:16:20.518Z] TOOL RESULT

```
=== FSD cable ===
23756:cable  molding  flamboyant
54024:cable
54229:cables. —   c.»tlre,  n.  A   large           
=== AHD watkins kap ===
173:It was probably not long before the disper- sal of the Proto-Indo-European community that the use of the wheel and wheeled trans- port was adopted. Despite the existence of widespread word families, most terms relat- ing to wheeled vehicles seem to be metaphors formed from already existing words; they are not primitives or primary vocables. So the word for AXLE (aks-) may mean simply “a pivotlike juncture”; the NAVE or hub of the wheel (nobh-) is the same word as NAVEL. This is clearly the case with WHEEL itself, where the widespread *k(e)-k“l-o- is an ex- pressive derivative of a verb (k"el-') meaning “to revolve or go around.” Other words for “wheel” are dialectal and again derivative, like Latin rota from a verbal root ret-, “to run.” A root wegh-, “to go, transport in a vehicle” (WAGON), is attested quite early, though not in Hittite. This evidence for the late appearance of the wheel agrees with archaeological findings that date the distri- bution of the wheel in Europe to the latter
981:ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
=== SKT cable ===
105:5  5.  Symbols  of  Languages.    The  symbols,  such  as  F.  =  f  ren* are  not  used  in  their  usual  vague  sense,  so  as  to  baffle  the  enquirer who  wishes  10  find  the  words  referred  to.     Every  symbol  has  a unse^  and  has  reference  to  certain  books,  in  one  at  least  of  which word  cited  may  be  found,  as  I  have  ascertained  for  myself  by  lool ibein  all  out.     I  have  purposely  used,  as  far  as  was  practicable,  cl and  easily  accessible  authorities.     The  exact  sense  of  each  symbol  j given  in  ihc  list  btlow.
602:amicable.  (L.)  L.  amUabilis,  friendly ; as  alwve.  j-
1847:bifct8«  oaval  term.  (Scand.)  The  bi/O arc  two  strong  posts  on  deck  to  which cables  me  fastened.  — Swed.  beiin^,  a  bi!t, whence   btttti^iittg   a  bitt  bolt,    bitt-pin ;
2557:Cable,  a  rope ;  see  Oapaotons.
2910:CAbbAge  (i\  a  TCseCable.  (T.«teL' U)  O.  F,  fiMJT  ai^w»  *a  cabbide^'  O (lit.  *  RMiad-headcd  cat-lvi^e  : '  wc  ti dropped  ckgmxY  The  >.  /-aAau,  n beaded,  is  from  llal.  eapmecis,  a  lutte  1 dimiiL  of  nor/v.  head.  *  JL  or/w/,  head
10115:coll  (i\  to   gather  together.   (F.-L.) *  C&iUd  op   in    a    cable  ;*    Rcanmont    and Fletcher.  -  O.  F.  fw7/i>.  to  collect.  -  L.       fl tolHgtrt ;  tee  ooUeot  below.  f
13583:Peccable,  Peooadillo ;  see  Poooant.
13585:peccable,  liable  to  sin.  (L.)  Coined as  if  from  L.  peccahUu*,  fiom  ptccart,
19022:air.  {F.  -  Gk.)  F.  s^ifiA^.  -  Gk.  oIk^tj,  a kind  of  wonn  or  grub  (Aristotle).  On this  word  it  would  seem  that  Paracelsus lonncd  the  name  sylpkt ;  he  also  used  the names  ffnome,  salamandtr^  and  nymph  (all of  Gruk  origin'),  to  si^ify,  respectively,  a genius  of  earth,  fire,  and  water.  Hence the  form  sytphid,  a  false  form,  bat  only explicable  on  the  hypothesis  of  a  Greek ongin;  as  if  from  a  nom.  irtA^ir*  (base iriAt^iS-).  ^  Liltrc's  explanation,  that sylph  is  of  Gaul  ish  origin,  seems  to  me  futile ; FaiacelsQS  could  hardly  know  Gaulish.
19455:Tetchy,  Techy,  touchy :  see  Tack.   I Tether,  a  rope   for  taitteitifif;   up.    (Q Formerly  written  teJder.     M.  E_  teAr  i Gael,  teadhair,  a  tclhcr;   ta^J,  «  hslri hair  rope,  chain,  cable ;  taodam,  liltle  con Irish  tead,  tend,  cord,  rope,  teiJim.  ad rope,  cord  ;   W.  tid,  a  chain ;  Manx  A* teU,  a  rope.     C£  W.  feJm^  to  stretfih:  S tttntu,    a    thread,    from    tarn,    to    stieu (VTA?)     p.  We  find  also  IcrL  t^» tether,  Low  G.  tider^  Swed.  tjmdtTt  tk toir,  prob.  all  of  Celtic  origin. Tetragon,    a  figure  with  four  ml^ (F.  -  L.  -  Gk.)     F.  tttragme,  adj..  to cornered.  — L.  tetmgonus^  adj.«*Gk.  fffl 7an'o»,    four-coraerrd.  —  Gk.    rirp^   (I T«Tapa),  prefix  allied   to   rimpa.  All form  of  rlaaapft,  four,   cognate  witfa Four;  and  ya/via,  an  angle,  from  1^1% knee,  coenate  with  E^  IC&ee.
=== LKT ===
1864:766.  Ar.  habl:
1865:'Stil' ;  hieraus  mlat.  capulum  'Fangseil', frz.  cäble,  sp.  cablo  'Ankertau',  engl. cable,  ndl.  kabel,  dtsch.  Kabel  [schon  im Gudrunliede  heißt  es :  ankersail  von Arabe,  wozu  Flachs  kaitän  benutzt Avurde.]
4231:'Gute  Frau,  treues  Weib'.  Dieses  Wort wird  in  den  ind.  Dialekten  heutzutage zur  Bezeichnung  der  Frau  benutzt,  die sich  in  höchster  Erfüllung  ihrer  Treue selbst  auf  dem  Scheiterhaufen  ihres verstorbenen  Gemahls  dem  Tode  weiht. Die  Anwendung  des  Wortes  auf  den selbstmörderischen  Akt  statt  auf  die Person  ist  erst  europäisch:  engl,  suttee, dtsch.  Satti  'freiwillige  Witwenverbren- nung'. Die  Unsitte  wurde  im  Jahre  1829 durch  eine  strenge  Regulation  for  declar- ing  the  practice  of  suttee  or  of  burning or  burying  alive  the  widows  of  Hindoos illegal  and  punishable  by  the  criminal courts  verboten,  aber  es  dauerte  sehr lange,  bis  sie  restlos  verschwand,  ja  in abgelegenen  Teilen  Indiens,  wie  Nepal, soll  sie  noch  jetzt  vorkommen;  so  soll sich  um  1890  die  Witwe  von  SIR  JANG BEHADUR,  des  Premierministers  von Nepal,  mit  der  Leiche  ihres  Gemahls auf  dem  Scheiterhaufen  verbrannt  haben [Globus  LXIX,  337].  Eine  gute  Schilde- rung des  Vorganges  gibt  ein  Augen- zeuge in  Philipp  van  Mökern,  Ostindien. Seine  Geschichte,  CuHur  und  Bewohner. Leipzig  1857.  I,  326/332.  Ausführlich handelt  über  Suttee  F.  Max  Müller, Alte  Zeiten  —  alte  Freunde.  Lebenser- innerungen. Übersetzt  von  H.  Groschke.
```


## [2026-09-06T15:16:30.035Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '54020,54035p' FSD_vol1.txt"
}
```


### [2026-09-06T15:16:30.105Z] TOOL RESULT

```
by5,  n.,  a   settlement  (<  frfin,  dwell).  4-  log,  pi.  log,  woo!.—  bys'sal,  c.  Of  or  pertaining  to  tneoyasus  of  a   mol-  river  in  Poland,  where  Russians  defeated  the  Germans
law1.]  Milage;;  blrTawt;  burtcy;;  byMaw;.—  byr'-  lusk.—  bys-sITer-ous,  a.  Bearing  or  having  a   byssus.—  Feb.  4-0,  1915.
For  words  not  given  abovB  see  by.  adc.,  page  304.
c
cable
Key  1:  artistic,  firt;  fat,  fare;  fast;  get,  prev;  ldt,  police;  obey,  gO;  net,  Sr;  full,  rQIe;  bnt,  bOrn;  a   =   final;  1   =   habit,  renew; Key  2:  art,  ape,  fat,  fare,  fast,  what,  all;  me,  get,  prey,  fern;  hit.  Ice;  1   =   5;  I   =   e;  go,  not,  or,  won,  wolf,  do.
366
C
C   c
Roman.
©c
ca5.
Script.
,Icai
Black  Letter.
C,  C,  1   si;  2   ge.  n.  [cees,  C’s,  or  Cs,  1   sis;  2   ges,  p7.]  1. A   letter;  the  third  in  the  English,  Latin,  and  Romanic alphabets;  in  Latin  and  Anglo-Saxon  called  cc  =   k£.
```


## [2026-09-06T15:16:31.623Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WEB cable ===\"; grep -n \"cable, n\" WEB_vol1.txt | head -5; echo \"=== RCH habl/havan ===\"; grep -n -i \"habl\\b\" RCH.txt | head -5; echo \"=== HUB xim ===\"; grep -n \"xim\\|χim\\|χīm\" HUB.txt | head -10"
}
```


### [2026-09-06T15:16:31.728Z] TOOL RESULT

```
=== WEB cable ===
=== RCH habl/havan ===
32843:,   A   JL>.  habl  (from  Making  a   treaty.  Finding  aecurity.
35467:A   khubul,  The  palsy.  Amputation  of  the  hands  and  feet, (pi.  of  khabl),  Corruptions.
51444:A   (JA  shabl  (from  (JA),  Growing.  Being  delicately  or  well brought  up.  Shibly  The  whelp  of  a   lion  or  other  beast  of  prey, p   shabldnulany  To  cause  to  adhere,  to  unite.
=== HUB xim ===
4945:afgh. iBmq^ arm. dSm-k^; xim *Charakter, duzxlm^ diixTm von
```


## [2026-09-06T15:16:38.991Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4935,4960p' HUB.txt; echo \"=== leaf ===\"; python3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\\\"xim *Charakter\\\")\nprint('leaf0b',t[:i].count('\\f'))\n\""
}
```


### [2026-09-06T15:16:40.671Z] TOOL RESULT

```
arm. few, zd. ka^na-; xasln *blau8chwarz' = zd. axsa^na-;
ctn, dfnistan 'China* = arm. rfer/-^ (pi.), denastan; idhin^Falke
= arm. sahen (vgl. das N. pr. Sahln Tab. 291 ~ arm. SahSn);
paz. ein *Waflfe* Min. kap. 43, 7, arm. zSn, zd. za^na- ; np.
kahln *Mitgift* = arm. kapSnl?; parvln 'Plejaden' s. oben
p. 40; np. pdrgln 'Wallgraben' = arm. parkBn; np. kaiktn
'Gerstenbrot' = arm. Raskin; GurgTn N. pr. = arm. GurgSn^)
(Joh. Kathol., Thom. Artsr. u. s. w.), alter Vrk^n (FH.
104); aimury 'Greif = zd. 8a^nd-\' mereyd; paz. plm 'Milch*
Min. Gl. 163 = zd. pa^ma; np. dim 'Geaicht' :^ bal. dew,
afgh. iBmq^ arm. dSm-k^; xim *Charakter, duzxlm^ diixTm von
schlechtem Charakter , paz. du§xtm Min. Gl. 68, arm. dixem
schlecht*; ntm *Halfte, halb' == zd. na^ma-; dann mmrOz —
paz. mmroz Min. Gl. 146, bal. nBmr66 'Mittag*; rim 'pu8,
sanies viilneris = bal. r^m 'Eiter.
Im Inlaut blieb e vor m linger als im Auslaut, vgl.
paz. passman Veuig' (oben p. 40).
§ 30. Ap. ai = np. e kann (vor h, vor Doppelkon-
sonanten etc.) zu i verkiirzt werden: mihman 'Gast* aua
mehman, afgh. mSlmq *Gast', zd. *ma^i^man'; firiita 'Bote'
>) Aber Sirln Frao Choaru's II (Tab. 283) - arm. Sirin
(Sebeos p. 45), np. Sirln 'siiiis' (auB *Sfrin)? Suffix -fi/ = zd. a^na-
(np. zarrtn *golden', zd. zaranafna-) b. bei Yullers, Gram. p. 255,
Der Name wird erst im 7. Jhd. den Armeniern bekannt geworden sein.— 142 -
= firSsta, arm. hrestaJc; xism (xasm^) Zorn' = zd. aesma-;
zinhdr *Schutz, Sicherheit, gieb Acht! hiite dichf = zinhar
=== leaf ===
leaf0b 151
```


## [2026-09-06T15:16:50.189Z] TOOL CALL #43: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-06T15:16:50.256Z] TOOL RESULT

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


## [2026-09-06T15:16:55.148Z] TOOL CALL #44: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/cable\" \\\n \"https://www.etymonline.com/word/cable\" \\\n \"https://en.wiktionary.org/wiki/%D8%AD%D8%A8%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D9%88%D9%86\" ; do\n echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 219 verification: Habl/cable chain, xim, havan\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T15:17:02.388Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/cable
/home/sfmqrb/git/rishe/data/verification/sources/web/1d881a30b9707b12.txt
### https://www.etymonline.com/word/cable
/home/sfmqrb/git/rishe/data/verification/sources/web/4890a9a2415c12af.txt
### https://en.wiktionary.org/wiki/%D8%AD%D8%A8%D9%84
/home/sfmqrb/git/rishe/data/verification/sources/web/147900dc6c2cfb42.txt
### https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/130ef368746a10b0.txt
### https://en.wiktionary.org/wiki/%D9%87%D8%A7%D9%88%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/19023599236cc2ae.txt
```


## [2026-09-06T15:17:04.201Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"######## cable wikt\"; grep -n -A14 -i \"Etymology\" 1d881a30b9707b12.txt | head -50"
}
```


### [2026-09-06T15:17:04.248Z] TOOL RESULT

```
######## cable wikt
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.3.2 
74- Related terms 
75-
76- 1.3.3 
--
94: Etymology 
95-
96- 2.2 
97- Pronunciation 
98-
99- 2.3 
100- Noun 
101-
102- 2.3.1 
103- Derived terms 
104-
105- 2.4 
106- Further reading 
107-
108- 3 
--
117: Etymology 
118-
119- 3.3 
120- Pronunciation 
121-
122- 3.4 
123- Noun 
124-
125- 3.5 
126- References 
127-
128- 4 
129- Middle English 
130-
131- Toggle Middle English subsection 
--
137: Etymology 
138-
```


## [2026-09-06T15:17:05.086Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"######## etymonline cable\"; sed -n '1,80p' 4890a9a2415c12af.txt | grep -v \"^$\" | head -40"
}
```


### [2026-09-06T15:17:07.267Z] TOOL RESULT

```
######## etymonline cable
URL: https://www.etymonline.com/word/cable
FETCHED: 2026-09-06T15:16:58Z
STATUS: 200
TITLE: Cable - Etymology, Origin & Meaning
Cable - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of cable 
 cable (n.) 
 c. 1200, "large, strong rope or chain used on a ship," from Old North French cable , from Medieval Latin capulum "lasso, rope, halter for cattle," from Latin capere "to take, seize," from PIE root *kap- "to grasp."
 Technically, in nautical use, a rope 10 or more inches around, to hold the ship when at anchor; in non-nautical use, a rope of wire (not hemp or fiber). It was given a new range of senses in 19c. in telegraphy (1850s), traction-railroads (1880s), etc. The meaning "message received by telegraphic cable" is from 1883, short for cable message (1870), cablegram (1868), cable dispatch (1864). Cable television is attested by 1963; shortened form cable in this sense is from 1970.
 Speed, speed the Cable; let it run,
   A loving girdle round the earth,
 Till all the nations 'neath the sun
   Shall be as brothers at one hearth;
 [T. Buchanan Read, "The Cable," 1858]
 also from c. 1200 
 cable (v.) 
 c. 1500, "to tie up with cables," from cable (n.). As "to transmit by telegraph cable," 1868. Related: Cabled ; cabling .
 We have done our part lately to bring into use the verb cabled, as applied to a message over the Atlantic cable. It is proper to say "it has been cabled," instead of "it has been telegraphed over the Atlantic cable." [The Mechanics Magazine, London, Sept. 11, 1868]
 But other British sources list it as an Americanism.
 also from c. 1500 
 Entries linking to cable 
 cable-car (n.) 
 "car on a cable railroad," 1879, from cable (n.) + car . A streetcar moved by an endless cable which is cased in a small tunnel under the railway and kept in motion by a remote stationary engine.
 cablese (n.) 
 "shorthand used by journalists in cablegrams," 1916, from cable in the telegraphic sense + -ese as a language-name suffix. "Since cablegrams had to be paid for by the word and even press rates were expensive the practice was to affix Latin prefixes and suffixes to make one word do the work of several" [Daniel Schorr], such as exLondon and Londonward to mean "from London," "to London" (non-Latin affixes also were used). Hence the tale, famous in the lore of the United Press International, of the distinguished but harried foreign correspondent who reached his breaking point and wired headquarters UPSTICK JOB ASSWARD. Its economy and expressive power fascinated Hemingway in his newspapering days.
 *kap- 
 Proto-Indo-European root meaning "to grasp."
 It might form all or part of: accept ; anticipate ; anticipation ; behave ; behoof ; behoove ; cable ; cacciatore ; caitiff ; capable ; capacious ; capacity ; capias ; capiche ; capstan ; caption ; captious ; captivate ; captive ; captor ; capture ; case (n.2) "receptacle;" catch ; catchpoll ; cater ; chase (n.1) "a hunt;" chase (v.) "to run after, hunt;" chasse ; chasseur ; conceive ; cop (v.) "to seize, catch;" copper (n.2) "policeman;" deceive ; emancipate ; except ; forceps ; gaffe ; haft ; have ; hawk (n.); heave ; heavy ; heft ; incapacity ; inception ; incipient ; intercept ; intussusception ; manciple ; municipal ; occupy ; participation ; perceive ; precept ; prince ; purchase ; receive ; recipe ; recover ; recuperate ; sashay ; susceptible .
 It might also be the source of: Sanskrit kapati "two handfuls;" Greek kaptein "to swallow, gulp down," kope "oar, handle;" Latin capax "able to hold much, broad," capistrum "halter," capere "to grasp, lay hold; be large enough for; comprehend;" Lettish kampiu "seize;" Old Irish cacht "servant-girl," literally "captive;" Welsh caeth "captive, slave;" Gothic haban "have, hold;" Old English hæft "handle," habban "to have, hold."
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
```


## [2026-09-06T15:17:12.940Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"capulum\\|Old North French\\|Portuguese\\|Arabic\\|Middle English cable\" 1d881a30b9707b12.txt | head -20"
}
```


### [2026-09-06T15:17:13.041Z] TOOL RESULT

```
314: Recorded since c.1205 as Middle English cable , from Old Northern French cable , from Late Latin capulum ( “ lasso, rope, halter ” ) , from Latin capiō ( “ to take, seize ” ) . Use of the term "cable" to refer to the USD/GBP exchange rate originated in the mid-19th century, when the exchange rate began to be transmitted across the Atlantic by a submarine communications cable.
540: Portuguese: cabo   (pt)   m 
574: Arabic: كَابْل   m ( kābl ) 
652: Portuguese: cabo   (pt)   m , fio   (pt)   m 
722: Portuguese: boça   (pt)   f 
759: Portuguese: cabo   (pt)   m , linha   (pt)   f 
813: Portuguese: telegrama   (pt)   m 
1042: Borrowed from Old Northern French cable , from Late Latin capulum .
1083: From Late Latin capulum .
1263: Terms with Portuguese translations 
1279: Terms with Arabic translations
```


## [2026-09-06T15:17:13.739Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### habl arabic\"; grep -n -i \"Proto-Semitic\\|ḥabl\\|Etymology\\|rope\" 147900dc6c2cfb42.txt | head -30"
}
```


### [2026-09-06T15:17:13.792Z] TOOL RESULT

```
#### habl arabic
62: Etymology 1 
80: Etymology 2.1 
92: Etymology 2.2 
104: Etymology 2.3 
121: Etymology 
135: Etymology 
223: Etymology 1
232: From Proto-Semitic *ḥabl- .
242: حَبْل • ( ḥabl )  m ( plural حِبَال ( ḥibāl ) or أَحْبُل ( ʔaḥbul ) or حُبُول ( ḥubūl ) or أَحْبَال ( ʔaḥbāl ) ) 
244: ( countable ) a rope , a cable ; a hawser ; a cord ; a string ; a thread 
245: Synonyms: سَبَب ( sabab , “ a rope ” ) , وَتَر ( watar , “ a cord; a string; a band ” ) , خَيْط ( ḵayṭ , “ a thread ” ) , عَصَب ( ʕaṣab , “ a band; a sinew ” ) , رِبَاط ( ribāṭ , “ tie, bond ” ) , مَرَسَة ( marasa ) , قَلْس ( qals ) , أَشْل ( ʔašl ) , طُنُب ( ṭunub ) , مَرَار ( marār ) , إِصَار ( ʔiṣār ) , مَأْصِر ( maʔṣir ) , سِلْسِلَة ( silsila ) , مِقَاط ( miqāṭ ) 
246: ( countable ) something resembling , likened to, or related to a rope (such as a ray , a beam , a jet , a vein , and so on)
247: 609–632 CE , Qur'an , 50:16 : وَلَقَدْ خَلَقْنَا ٱلْإِنسَنَ وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ wa-laqad xalaqnā l-ʾinsana wa-naʿlamu mā tuwaswisu bihī nafsuhū wa-naḥnu ʾaqrabu ʾilayhi min ḥabli l-warīdi We have created man and know what his spirit suggests to him, and We are closer to him than the rope of his [jugular] vein. 
252: Declension of noun حَبْل ( ḥabl )
267: ḥabl 
270: al-ḥabl 
273: ḥabl 
278: ḥablun 
281: al-ḥablu 
284: ḥablu 
289: ḥablan 
292: al-ḥabla 
295: ḥabla 
300: ḥablin 
303: al-ḥabli 
306: ḥabli 
319: ḥablayn 
322: al-ḥablayn 
325: ḥablay 
330: ḥablāni
```


## [2026-09-06T15:17:37.660Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ arabic script habl ===\"; grep -c \"حبل\" FVQ.txt; echo \"=== AFA Seil/Strick ===\"; grep -n -i \"Strick\\|Seil\" AFA.txt | head -10; echo \"=== MON habl ===\"; grep -n \"حبل:\" MON_part1.txt | head -5"
}
```


### [2026-09-06T15:17:37.737Z] TOOL RESULT

```
=== FVQ arabic script habl ===
0
=== AFA Seil/Strick ===
889:verschiebung geschützt scheint, mit Guidi Dellu seile p. 16.
2402:Wurzel jJU »drehen*' (vom Seile) zu gehören, daher dann
3626:Wir kommen nun zu den Stricken, Seilen und Riemen.
3638:Dass Jjj »Strick** aus IL^] entlehnt ist, haben schon
5844:Honig und PfefiFer") ; conditum (seil, vinuni) ; auch syrisch
5862:34), rosatum seil, vinum, das in griechischer Form also
6740:sondern wie die Analogie von /ZH »Strick" und »Pfand"
6994:aus constans (seil, libra) vorgeschlagen. Der Lautwandel
7360:geschweige denn zur See , fAttri ye , xotrx bikctrrxv (seil to-
7831:Seil an Stelle eines Segels ist mir unverständlich. Auch
=== MON habl ===
52392:حبل: 0۱ [ع.] ((.) ریسمان» رشته» بند؛ ج. 
52396:حبل: ۵0۱" [ع.] (اتضی) استتی:,(۱) 
52400:حبل: اع [ع.] (ص. .) دانشمند. زی رکك»
```


## [2026-09-06T15:17:37.952Z] TOOL CALL #50: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/site/pages/219.jpg 2>/dev/null; ls /home/sfmqrb/git/rishe/*.pdf"
}
```


### [2026-09-06T15:17:37.990Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/site/pages/219.jpg
/home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf
```


## [2026-09-06T15:17:42.485Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3620,3665p' AFA.txt"
}
```


### [2026-09-06T15:17:42.532Z] TOOL RESULT

```
Ob «LS »Sitzle<ler' zu j^l2i »ausspannen** gehört, ist
noch nicht ganz klar.
Hierher gehört noch J,^ xIa»^ aus U.^i.lä^; schon Hoff-
mann Martyreracten. Note 206. Vgl. Gauh. s. ▼. J|V;
Div. Hmj. 66, 13; ^Arüch s.v. ^SPi; Tosepht ed. Zuc-
kerm. 595, 26.
Wir kommen nun zu den Stricken, Seilen und Riemen.
Da erscheint mir zunächst fremd das alte i^Jo plur. ii»!^!
(schon bei Amrulk. Mu^ll. 46). Die Wurzel ^j»^ zer-
fallt in zwei Theile. Der verbale J^Zi = ^.▲ylo (erweichen)
»pressen*' Lst echt arabisch; der nomin. aLlLo aber scheint
erst aus l^i^o übernommen; er fehlt im Hebräischen und
Äthiopischen. Die Verba ^Jo, (j^I^I zeigen sich deut-
lich als Denominativa. Dass später auch eine Form J^Lt
sich in's Arabische einschlich, (Gawali]p MorgenL Forsch.
154) ist allerdings wohl nur so zu verstehen, dass das
classische Arabisch in diesem Worte durch eine aramäische
Bildung im Irak und Syrien verdrängt wurde.
Dass Jjj »Strick** aus IL^] entlehnt ist, haben schon
die Araber erkannt. (Eamüs ilk^).
Nach Noldeke (brieflich) ist auch das alte und verbreitete
Wort für )» Giemen*' im Arabischen SStt ^Antara 15,8; Agani
XI. 37. 10 a.f.;Qam. 351 nichts weiter als entlehntes ^itpi.
Vermittelt ist es durch das Aramäische, in welchem es in
mancherlei Formen, theilweise noch unerkannt, auftritt.•'1. . ■ • ■•,..' .
94
[li^ Barh. gr. L 233, 11 = 9tipi (Assem. m. 466);
plar. ja^'^>äZO (oi = « =s «/) ^npaT^ Athaoas. Festbriefe pag.
y; ferner ^iJ^i-j^ tr;/;«^ lud. 16,13. Hesapl.; ProY. 5,22.
Hex. Dazu Opuac. Nestor (HoflFm.) 147, 18 ^i.-J^ = nX.
Dayon ist dasselbe Wort ^j-i^ >c:l9 ^] Exod. 28 , 32 ; 39,
23 nicht zu trennen. Dazu Gast, fälsch punctirtes li^^^
Th. Nüld.].
Einige Spinn- und Webegemthe tragen auch aramäische
Namen. Si^ ]> Weberbaum" scheint im Arabischen ohne
Ableitung zu sein; daneben wird auch noch ^^^ . ^ (aller-
dings nach Asma^i bei Gauh. s. y. *_««^ in yerschiedener
Bedeutung) gebraucht. Ich bin nicht sicher, ob ich ri£)Ti
Sabb. 96^, 18 a. f. (es soll nach der Glosse »Rand" wie
Jöma 77^, 16 a. f., nach ^Arüch aber den Kamm, mit dem
man auf das Gewebe schlagt, bedeuten) damit zusammen-
stellen darf.
Mit einiger Sicherheit aber kann ich JI3 9 (leider habe
ich keinen alten Beleg dafiir) woneben sich wohl später erst
JtaJU (Amrk. 52, 49) entwickelt hat, fQr eine aramäische Ent-
lehnung erklären. Es hat im Arabischen keine Ableitung,
```


## [2026-09-06T15:17:42.761Z] TOOL CALL #52: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/219.jpg"
}
```


### [2026-09-06T15:17:42.790Z] TOOL RESULT

```

```


## [2026-09-06T15:18:33.347Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF xim ===\"; python3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nt=re.sub(r'[‌‎‏‪-‮⁦-⁩­]','',t)\nlines=t.split('\\n')\npage=None\nfor i,l in enumerate(lines):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: page=m.group(1)\n    if 'خیم' in l:\n        print(page,i,l.strip()[:200])\nEOF"
}
```


## [2026-09-06T15:18:34.942Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK hu/haoma press ===\"; grep -n \"hunāmi\\|hunami\\|haoma\" POK_full.txt | head -10; echo \"=== BRT hav press ===\"; grep -n \"'auspressen'\\|auspressen\" BRT.txt | head -8"
}
```


### [2026-09-06T15:18:35.581Z] TOOL RESULT

```
=== FSF xim ===
None 781 نگون گشت وزهم             بخفتند در خیمه بکاام خویش
None 5464 قارن از این پیشامد آگاه میشود و بهنوذر         بهخیمهشد این»آن بهخرگاه خویش
None 6675 بگویش کهبرخیز و نزد من آی                        سراپرده و خیمهها گشته تر
None 7008 بفرمای کایند باتو به راه                                  سراپرده؛ دپهرسراء خیمه ,خرگاه:
None 9266 خیم
None 10291 رنگ رنگ   ز خرگاه و ازخیمۀ        نه بر آرزو کینهخواه آمدیم
None 10983 بدنهاد.    جزء دوم واه مرکب دژخیم                زبان خیره پرتاب و دل پردروغ
None 10986 خود در بیت زیر «خیم» را معنی میکند:                                               خی 4ش
None 10989 دگر خوی را انک خوانیم خیم                        به شخی ککهرگس برو نگذرد
None 10995 اخیم»
None 11008 خیم (بروزن بیم)
None 11749 به دژخیم فرمود شاه اردشیر
None 11759 دژخیم                                   پشیمانی آنگه نداردت سود
None 11772 (ناصر :)۲۶۲-۰۲        طبع (صحاح      دوم خیم به معنی خو       جزء
None 11780 د             واژ؛ خیم   در داستان نوشیروان        فردوسی
None 11785 (حافظ :)۶۰۱        آنک خوانیم خیم »کهبااو ندارددل از دیو
None 11798 دگزمشت سالار بسیار هوش            مرا بیوفایی و دزخیم نشت
None 11803 (۲-۶۱-4۵                                                    چنان مهربان بود دژخیم شد
None 11812 ()۱-۵۶۱-۲۴۴                                                    4دزخیم فرمود تا تيغ تيز
None 11849 خود اندر میان رفت بایک پسر                        مرکب از دژ (بهواژة دژخیم نگاه کنید) +
None 12100 ترکیب یافته است :یکی من از مصدر ۸۵۳         مرکب از دش [به وارهُ دژخیم نگاه کنید] +
None 12892 ز بیگانه خیمه بپرداختند                         ()۱-۵۰۲-۵۵۰۱
None 13426 - ۱دژخیم:
None 14946 همه دشت پر خرگه و خیمه کشت
None 16506 غنودن                     برون آمد از خیمه ارژنگ دیو
None 21032 در شاهنامة چاپ تهران [برو خیم ] نیزکه
None 21068 بریدند ازو تختههای گران                           شمارة این بیت در شاهنامةٌ چاپ بروخیم
None 22034 -۳و دبرا                   چسند گردی گردمای خیمة انبد
None 22179 سوی خیم خویش رفتند باز                              من امروز براختر کرم سیب
```


### [2026-09-06T15:18:35.661Z] TOOL RESULT

```
=== POK hu/haoma press ===
74278:', susutl-i. "leichtes parturition'; Avestan hav- {hunami) " to give birth to children. Kinder zur 
74281:present *sunami {zoxxv^axe Avestan hunami) and *5^/i7(compare Old Indie suyate): Indo 
=== BRT hav press ===
29501:•  j,  'hav-  V.  'auspressen',  den  Haoma. Praes.  10  Aunav- :  ium>-'\  11  Aun-'\ ij  (Fut)  iaorya-'K  —  PPfP.  Au/a-,  PFP. Aao/yanta-;  Inf.  °hutayae-ca.        [Vgl.  noch
29502:'auspressen,  ausstampfen,  keltern',  den Haoma:  aia  hävana  haomqn  kunyät  "so soll  der  Havanan  die  Haemazvi\%t  aus- pressen" N.Öl?;  —  kaa  %wqm  paoiryS haoma  ..  kunäta  Y.fj.  3;  4;  —  hävana- yas{sA.)ca  Aaoma  Aunvatntya  (GDf.)  Vr. 12.3;  —  yäi  h)nH  haoma  .  .  asaya  hun- vana  asaya  Aaosyatiia  "die  Zfacwazweige, die  . .  jetzt  ausgepresst  werden  und  künftig ausgepresst  werden  sollen"  Vr.p.j;  — nSit  haomS  hutö  axii/  nSit  tnahrks  .  . ava  alle  ahuta  V.  6.  43;  —  pasca  fra- riuAaniti  haemahe  Autahe  H.  1.  9;  V. 18.  13;  —  haomanqmca  asaya  Autanqm Vr.  12. 3.
```


## [2026-09-06T15:18:50.416Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"pdf page\" FSF_pages.txt; grep -n \"pdf page\" FSF_pages.txt | head -3; echo \"---\"; python3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('total lines',len(lines))\npat=re.compile(r'pdf page (\\d+)')\nlast=None\nfor i,l in enumerate(lines):\n    m=pat.search(l)\n    if m: last=(i,m.group(1))\n    if i in (10983,11008,11749,11812):\n        print(i,'last page tag',last)\nEOF"
}
```


### [2026-09-06T15:18:52.500Z] TOOL RESULT

```
0
---
total lines 23569
10983 last page tag None
11008 last page tag None
11749 last page tag None
11812 last page tag None
```


## [2026-09-06T15:18:57.903Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nprint('ff',t.count('\\f'))\nlines=t.split('\\n')\ndef leaf_of(lineno):\n    off=sum(len(l)+1 for l in lines[:lineno])\n    return t[:off].count('\\f')\nfor ln in (10983,11008,11749,11812,9266):\n    print(ln, 'leaf0b', leaf_of(ln))\n# print pages around to find printed numbers\npages=t.split('\\f')\nfor idx in (leaf_of(11008), leaf_of(11780)):\n    p=pages[idx]\n    print('=== leaf',idx,'===')\n    print(p[:300])\nEOF"
}
```


### [2026-09-06T15:18:59.960Z] TOOL RESULT

```
ff 484
10983 leaf0b 223
11008 leaf0b 223
11749 leaf0b 237
11812 leaf0b 238
9266 leaf0b 189
=== leaf 223 ===
                                           ‫‪۳۳۰‬‬


‫دلاقشت‌های گات‌ها ‪:)۹۷‬‬
                     ‫ا»د خ‬
                         ‫س(ریشت‬                            ‫سپهبد بکهژی نگیرد فروغ‬
‫بدنهاد‪.‬‬    ‫جزء دوم واه مرکب دژخیم‬                ‫زبان خیره پرتاب و دل پردروغ‬
‫از همین ریشه است‪ .
=== leaf 238 ===
                           ‫دژم (با پیش اول)‬   ‫فارسی هنوز بر سر چند واژه‪ :‬دشمن [‪:‬‬
                   ‫‪-۱‬افسرده اندوهناک‪:‬‬          ‫بداندیش ] دشنام [‪ :‬بدنام اکزسی به بدی‬
         ‫شما دل مدارید چندین به غم‬             ‫نام بردن] دشخوار [‪ :‬دشوار <بداسان نه‬
‫که از غم شود جان حرم درم‬
```


## [2026-09-06T15:19:13.563Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor idx in (61,72,190,223,224,237,238):\n    p=re.sub(r'[‌‎‏‪-‮⁦-⁩­]','',pages[idx])\n    head=[l.strip() for l in p.split('\\n') if l.strip()][:2]\n    print(idx, head)\nEOF"
}
```


### [2026-09-06T15:19:15.254Z] TOOL RESULT

```
61 ['۵۸                                    اندر آمدن', 'ازواندرآمدهمی پرورش                                               از منوچهری (دیوان )۰۳۱']
72 ['به بالای تو بر چمن سرو نیست', 'چو رخسار تو تابش پرو نیست                    -۱به معنی «با» کهافادة معنی استعانت و']
190 ['جواز', 'یکی از بر خنگ زرین جناغ                            حلب = جلب (بازبراول و دوم)']
223 ['۳۳۰', 'دلاقشتهای گاتها :)۹۷']
224 ['و', 'رد']
237 ['۴۳۳                                           درود', '(حافظ ۰۸                     گی بدند   نرک']
238 ['دژم (با پیش اول)   فارسی هنوز بر سر چند واژه :دشمن [:', '-۱افسرده اندوهناک:          بداندیش ] دشنام [ :بدنام اکزسی به بدی']
```


## [2026-09-06T15:19:36.304Z] TOOL CALL #58: Bash

```json
{
 "command": "timeout 180 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%A8%D9%84/\" --note \"page 219: Mo'in entry for کابل (MON:2777), French origin tag\" 2>&1 | tail -2; timeout 180 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%87%D8%A7%D9%88%D9%86/\" --note \"page 219: Mo'in entry for هاون (MON:5095)\" 2>&1 | tail -2"
}
```


## [2026-09-06T15:19:39.977Z] TOOL CALL #59: Bash

```json
{
 "command": "pdftoppm -f 219 -l 219 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg219 && python3 -c \"\nfrom PIL import Image\np='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg219.png'\nim=Image.open(p); print(im.size)\nw,h=im.size\nim.crop((int(w*0.35),int(h*0.24),int(w*0.80),int(h*0.32))).resize((int(w*0.45*2),int(h*0.08*2))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_habl.png')\n\""
}
```


### [2026-09-06T15:19:41.221Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/16941f648af3c212.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/351733ea1d1f426b.txt
```


### [2026-09-06T15:19:44.159Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-06T15:19:45.937Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_habl.png"
}
```


### [2026-09-06T15:19:46.084Z] TOOL RESULT

```

```


## [2026-09-06T15:19:46.081Z] INPUT

[Image: original 2295x528, displayed at 2000x460. Multiply coordinates by 1.15 to map to original image.]


## [2026-09-06T15:19:47.380Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### kabl abadis\"; grep -n -i \"معین\" -A6 16941f648af3c212.txt | head -30; echo \"### havan abadis\"; grep -n -i \"معین\" -A6 351733ea1d1f426b.txt | head -30"
}
```


### [2026-09-06T15:19:47.475Z] TOOL RESULT

```
### kabl abadis
22: کابل. [ ب ُ ] ( اِخ ) شهر مهم و پایتخت افغانستان در 43درجه و 30 دقیقه عرض شمالی و 69 درجه و 13 دقیقه طول شرقی ، در 1762 گزی فوق سطح دریا واقع در نجدی حاصلخیز و پر آب و جمعیت آن در حدود 150000 تن است. ( برهان قاطع چ معین حاشیه لغت کابل بنقل از دائرة المعارف اسلام ). مؤلف حدودالعالم زیر عنوان «سخن اندر ناحیت حدود خراسان و شهرهای وی » آرد: شهرکی است و او را حصاری است محکم و معروف به استواری و اندر وی مسلمانانند و هندوانند و اندر وی بتخانه هاست و رای قنوج را ملک تمام نگردد تا زیارت این بتخانه نکند و لوای ملکش اینجا بندند. ( حدود العالم چ سید جلال الدین طهرانی ص 64 ). یاقوت در معجم البلدان آرد: کابل در اقلیم سوم است. طول آن از جانب مغرب صد درجه و عرض آن از جانب جنوب 28 درجه باشد. و اصطخری آرد: خلج صنفی از ترکانند که از دیرباز در سرزمین کابل که بین هند و نواحی سجستان در ظهر غوز است افتاده اند و آنان خداوندان نعمت اند و در لباس و زبان همانند ترکانند، و کابل ناحیه ای است و شهر بزرگ آن اوهند. و من با مردی از عقلای سیستان که شهرها و راه های آن ناحیت را گردش کرده بود ملاقات کردم و او از دیده های خود گفت کابل ولایتی است بزرگ میان هند و غزنه با مرغزارهای وسیع و نسبت آن به هند بیشتر است و این سخن نزد من درست آمد.
23-و اما گفته ابن فقیه که کابل از ثغور طخارستان است از صواب دور نباشد و شاید طخارستان در مثلث شرقی آن ناحیت است.
24-ابن فقیه آرد: کابل از ثغور طخارستان و از شهرهای آن : واذان وخواش و خشک وجزه است و گوید: به کابل عود و نارگیل و زعفران و اهلیلج بود. چه آن سرزمین [ در آب و هوا ] با هند برابر است و خراج آن دو هزار هزار و پانصد هزار درهم بود و از کنیزکان دو هزار سر که بهای آنان ششصدهزار درهم بود. مسلمانان بروزگار بنی مروان بدآنجا غزو کردند و آن ناحیت بگشودند و مردم آن سرزمین مسلمانند. یاقوت گوید: اگر غیر ساحلی بود رواست.و عبیداﷲبن قیس الرقیات گفت :
25-و لقد غالنی شیب و کانت 
26-فی شبیب مغیلة و مغاله 
27-غلبت امه علیه اباه 
28-فهو کالکابلی اشبه خاله.
--
39: فرهنگ معین
40-
41- (بْ لْ ) [ فر. ] (اِ. ) ۱ - رشته های ضخیمی از سیم های تابیده شده با روکش عایق دار برای انتقال جریان برق ، تلفن و... . ۲ - رشته سیم فولادی ضخیم برای بستن و بلند کردن قطعاتِ سنگین ، بافه (فره ). 
42-
43- فرهنگ عمید
44-
45- ۱. (برق ) مجموعۀ چند سیم هادی روکش دار که جریان برق را انتقال می دهند.
--
127:استانداردی که در درون آن غالب و چهارچوب معین، یک مُلک و مِلاکِ مولکولاریزه شده و سیال و لطیف و دارای انرژی و نیرو نهفته شده باشد. 
128-و فراوان از این دست کلمات مثل؛ 
129- ( گرانول گلایکول مولکول آمپول و. . . ) 
130-هرچند حرف ( ل ) در قانون و قواعد ایجاد کلمات در قانون قلب ها متناسب با کاربری کلمات و عینیت آن با عالم واقع قابل تبدیل به حرف ( ر ) می باشد. 
131-در مجموع در بسیاری از موارد، دو حرف ( ل ر ) در ترکیب ساختمان کلمات، نماد وجود و هستی و وجود نیرو و انرژی و توانمندی و حرکت در مفهوم کلمات در ابعاد مختلف می باشد. که حرف ( ل ) تداعی کننده ی یک حرکت سیال گونه و لطیف و مستمر و حرف ( ر ) تداعی کننده ی یک حرکت خرامان گونه و خراط وار و خروشان و خراش انداز مستمر مادی و فیزیکی منطبق با عالم واقع برای صحنه سازی در ذهن می باشد. 
132-کلمه ی ساق در کلمه ی ساقل به لحاظ نزدیک ترین کلمات مشابه در اطراف این کلمه مرتبط با کلمات هم خانواده خودش مثل ( ساقه ساقی سقایت ساغر ) می باشد. 
133-کلمه ی ساقه که در مورد گیاهان و درختان به عنوان یک ستون مستحکم و استوار برای شاخه ها و برگ و بار آن کاربرد دارد، زیاد از این کلمه استفاده می شود در واقع به صورت تعریف انطباقی با ریشه ی این کلمه اشاره به زمختی و شَقُّ و رَق بودن و به صورت تعریف موازی و غیرانطباقی اشاره به استوار بودن و پابرجا بودن و پایداری آن را دارد. 
--
218: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
219-
220- لینک ها 
221-
222- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
223-
### havan abadis
33: فرهنگ معین
34-
35- (وَ ) [ په . ] (اِ. ) ظرفی آهنی یا سنگی که در آن چیزی را می کوبند یا می سایند. 
36-
37- فرهنگ عمید
38-
39- ظرف فلزی استوانه ای از جنس چوب، سنگ که در آن چیزی می کوبند یا می سایند، کابیله. 
--
88:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
89-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
90-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
91-
92- مهراس 
93-حمید رضا مشایخی - اصفهان
94-
--
133: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
134-
135- لینک ها 
136-
137- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
138-
139- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-06T15:19:55.616Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### خیم\"; grep -n -B2 -A6 \"Persian\" 130ef368746a10b0.txt | sed -n '1,60p'"
}
```


### [2026-09-06T15:19:55.681Z] TOOL RESULT

```
### خیم
55-
56- 1 
57: Persian 
58-
59: Toggle Persian subsection 
60-
61- 1.1 
62- Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
--
147- From Wiktionary, the free dictionary
148-
149: Persian
150- [ edit ] 
151-
152- Etymology 1
153- [ edit ] 
154-
155- From Avestan [Term?] .
--
158- [ edit ] 
159-
160: ( Classical Persian ) IPA ( key ) : /ˈxiːm/ 
161-
162- ( Dari, formal ) IPA ( key ) : [xiːm] 
163-
164- ( Dari, formal ) IPA ( key ) : [xiːm] 
165- ( Kabuli ) IPA ( key ) : [xiːm] 
166-
--
223- [ edit ] 
224-
225: From Middle Persian [Term?] . Cognate with Parthian xdm ( xaδm , “ wound ” ) ; Persian خلم ( xelm , “ mucus ” ) .
226-
227- Pronunciation
228- [ edit ] 
229-
230- IPA ( key ) : /xiːm/ 
231-
--
244- Retrieved from " https://en.wiktionary.org/w/index.php?title=خیم&oldid=91573348 "
245-
246: Categories : Persian terms derived from Avestan 
247: Persian terms with IPA pronunciation 
248: Rhymes:Persian/iːm 
249: Rhymes:Persian/iːm/1 syllable 
250: Persian lemmas 
251: Persian nouns 
252: Persian terms with archaic senses 
253: Persian terms inherited from Middle Persian 
254: Persian terms derived from Middle Persian 
255-
256- Hidden categories: Avestan term requests 
257- Pages with entries 
258- Pages with 1 entry 
259: Middle Persian term requests 
260- Parthian terms in nonstandard scripts 
261-
```


## [2026-09-06T15:19:56.900Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### هاون\"; grep -n -i \"Middle Persian\\|Avestan\\|Etymology\\|hāwan\\|mortar\" 19023599236cc2ae.txt | head -25"
}
```


### [2026-09-06T15:19:56.953Z] TOOL RESULT

```
### هاون
62: Etymology 1 
74: Etymology 2 
97: Etymology 1 
115: Etymology 2 
190: Etymology 1
207: هَاوَنَ • ( hāwana ) III ( non-past يُهَاوِنُ ( yuhāwinu ) , verbal noun مُهَاوَنَة ( muhāwana ) ) 
224: muhāwana 
236: muhāwan 
280: hāwantu 
283: hāwanta 
286: hāwana 
289: hāwantumā 
292: hāwanā 
295: hāwannā 
298: hāwantum 
301: hāwanū 
306: hāwanti 
309: hāwanat 
312: hāwanatā 
315: hāwantunna 
318: hāwanna 
568: ʔuhāwanu 
571: tuhāwanu 
574: yuhāwanu 
577: tuhāwanāni
```


## [2026-09-06T15:20:02.292Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '140,200p' 19023599236cc2ae.txt"
}
```


### [2026-09-06T15:20:02.336Z] TOOL RESULT

```
 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Arabic
 [ edit ] 

 Etymology 1
 [ edit ] 

 Root 

 ه و ن ( h w n ) 

 18 terms 

 Pronunciation
 [ edit ]
```


## [2026-09-06T15:20:50.326Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T15:20:50.369Z] TOOL RESULT

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


## [2026-09-06T15:25:57.413Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 219,\n \"book_page\": 189,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Habl\",\n   \"verdict\": \"disputed\",\n   \"modern_form\": \"Proto-Semitic *ḥabl- 'rope, cord' (> Arabic ḥabl, Hebrew ḥeḇel, Aramaic ḥablā, Ethiopic ḥabl)\",\n   \"note\": \"The word is real and the gloss 'rope' is right, but the LANGUAGE LABEL is wrong as drawn: Aramaic ḥablā is a sister form, not the source. Arabic ḥabl is inherited from Proto-Semitic *ḥabl- and has a full native verbal root ḥ-b-l 'to bind' (ḥabala 'he bound'), so it cannot be an Aramaism. Klein — the source Nourai leans on for the rest of this chart — is explicit that Arab. habl is only 'rel. to' Heb. hebhel, Ethiop. habal, Akkad. nahbalu and Aram. habhla. The whole downstream branch (Portuguese > French > English 'cable') is Klein's minority reconstruction; AHD, Etymonline and Wiktionary derive 'cable' from Late/Medieval Latin capulum < capere, with no Semitic element (Nourai's own note on the Portuguese box says as much).\",\n   \"note_fa\": \"ریشهٔ ادعایی «آرامی ḥabl» درست‌نما نیست. واژهٔ عربی «حَبل» میراثی از سامی آغازین *ḥabl- است و ریشهٔ فعلی زندهٔ «ح‌ب‌ل» (حَبَلَ «بست») در خود عربی دارد؛ صورت آرامی ḥablā و عبری ḥeḇel هم‌ریشه (cognate) اند نه خاستگاه. کلاین نیز تنها می‌گوید عربی ḥabl «مرتبط است با» آرامی ḥablā. بنابراین برچسب زبانیِ جعبهٔ ریشه باید «سامی آغازین» باشد، نه «آرامی»؛ ادعای نورایی در این بخش پذیرفتنی نیست. شاخهٔ پرتغالی←فرانسه←انگلیسیِ cable نیز دیدگاه اقلیِ کلاین است و فرهنگ‌های امروزی (AHD، اتیمانلاین، ویکی‌واژه) آن را از لاتینی capulum «کمند، افسار» مشتق می‌دانند.\",\n   \"sources\": [W+\"%D8%AD%D8%A8%D9%84\", W+\"cable\", \"https://www.etymonline.com/word/cable\"],\n   \"ref_check\": [\n    {\"ref\": \"VDQ:176\", \"status\": \"not_checked\", \"note\": \"VDQ = Badre'i's Persian translation of Jeffery's Foreign Vocabulary of the Qur'an; the only copy (noorlib.ir/book/view/12868) is a JavaScript viewer that WebFetch/curl cannot read. Checked the ORIGINAL instead: grep -n -i 'habl' data/verification/sources/refs/FVQ.txt and grep -c 'حبل' FVQ.txt return no ḥabl entry at all (only the name 'adh-Dhahabi'), i.e. Jeffery does not list ḥabl among the Qur'anic foreign words — which makes an 'Aramaic origin' claim on his authority hard to sustain.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed., scan leaf 126 = printed pp. 218-219, s.v. 'cable'\", \"stance\": \"partial\", \"note\": \"'Arab. habl is rel. to habala, \\\"he bound\\\", Heb. hebhel, \\\"rope, cord\\\", Ethiop. habal, \\\"rope\\\", habala, \\\"he bound\\\", Akkad. nahbalu, \\\"rope, snare\\\", Aram. habhla, \\\"cord, rope\\\"' — cognates, NOT a derivation from Aramaic.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel pp. 93-94, the chapter 'Wir kommen nun zu den Stricken, Seilen und Riemen'\", \"stance\": \"silent\", \"note\": \"Fraenkel's rope chapter does declare several Arabic rope-words Aramaic loans ('Dass ... \\\"Strick\\\" aus ... entlehnt ist, haben schon die Araber erkannt (Ḳāmūs)'), but the OCR renders every Arabic word as garbage glyphs, so ḥabl could not be located there in transliteration; ḥabl is in any case not one of the standard Aramaisms, having a native verbal root.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 766\", \"stance\": \"partial\", \"note\": \"'Ar. habl: \\\"Seil\\\"; hieraus mlat. capulum \\\"Fangseil\\\", frz. câble, sp. cablo \\\"Ankertau\\\", engl. cable, ndl. kabel, dtsch. Kabel' — Lokotsch treats habl as ARABIC (not Aramaic) and as the source of the European words.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Arabic\",\n     \"words\": \"habl\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Arabic حَبْل ḥabl 'rope, cable' (pl. ḥibāl, ʔaḥbul, ḥubūl) is genuine and Qur'anic (Q 50:16 min ḥabli l-warīd 'nearer than the rope of his jugular vein'; Q 3:103 ḥabl Allāh), but the arrow drawn here — Aramaic > Arabic — is not what the sources say. Wiktionary derives it from Proto-Semitic *ḥabl-, i.e. inherited; the Arabic root ḥ-b-l is fully productive in Arabic itself (ḥabala 'he bound', ḥabbāl 'rope-maker'), which is the standard test against a loan. Klein, whom Nourai cites, lists Aram. ḥablā, Heb. ḥeḇel, Ethiopic ḥabl and Akkadian naḫbalu as RELATED forms of the same Semitic base, not as ancestors. The correct picture: Proto-Semitic *ḥabl- > Arabic ḥabl, and independently > Aramaic ḥablā, Hebrew ḥeḇel.\",\n     \"derivation_fa\": \"«حَبْل» عربی به معنی «ریسمان، طناب» واژه‌ای اصیل و قرآنی است (سورهٔ ق، آیهٔ ۱۶: «مِن حَبلِ الوَرید»؛ آل‌عمران ۱۰۳: «حَبلُ الله»)، و جمع‌های حِبال و أَحبُل و حُبول دارد. اما پیکانِ «آرامی ← عربی» با پژوهش امروزی نمی‌خواند: ویکی‌واژه آن را میراثی از سامی آغازین *ḥabl- می‌داند، و ریشهٔ ح‌ب‌ل در خود عربی زایاست (حَبَلَ «بست»، حَبّال «ریسمان‌باف») که نشانهٔ وام‌واژه‌نبودن است. کلاین هم آرامی ḥablā و عبری ḥeḇel و اکدی naḫbalu را «هم‌ریشه» می‌شمارد نه نیا. پس درست آن است که سامی آغازین *ḥabl- هم به عربی حَبل و هم جداگانه به آرامی ḥablā رسیده باشد.\",\n     \"sources\": [W+\"%D8%AD%D8%A8%D9%84\", W+\"cable\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:216\", \"status\": \"partial\", \"note\": \"The entry is on scan leaf 126 of KLN_1966 = printed pp. 218-219 (Nourai's '216' is 2-3 pages off). It reads: 'Arab. habl is rel. to habala, \\\"he bound\\\", ... Aram. habhla, \\\"cord, rope\\\"'. Klein gives Arabic ḥabl 'rope, cable' exactly as glossed here, but he makes Aramaic a cognate, not the parent — so the page supports the word and its gloss, not the Aramaic arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 ed. pp. 218-219 s.v. cable\", \"stance\": \"partial\", \"note\": \"gives 'Arab. habl, \\\"rope, cable\\\"' verbatim (Nourai's gloss is copied from here) but only 'rel. to' the Aramaic.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 766\", \"stance\": \"supports\", \"note\": \"'Ar. habl: \\\"Seil\\\"' — Lokotsch's headword is Arabic, confirming the word and meaning.\"},\n      {\"src\": \"RCH\", \"where\": \"Richardson-Johnson col. (grep 'habl')\", \"stance\": \"partial\", \"note\": \"grep of RCH.txt finds only 'habl (from ...) Making a treaty. Finding security.' i.e. a different ḥ-b-l derivative; the plain noun is not separately etymologised there.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"habl «حَبل»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian حَبل ḥabl 'rope' is a straightforward literary Arabic loan, taken over after the Islamic conquest with no change of form or meaning; it stays a bookish word beside native رسن rasan and ریسمان rismān. Mo'in's Farhang tags it '[ع.]' (= Arabic): 'حبل [ع.] (اِ.) ریسمان، رشته، بند؛ ج. ...'. Nourai's Saʿdi couplet (کله دلو کرد آن پسندیده کیش / چو حبل اندر آن بست دستار خویش, Būstān) is a genuine 7th/13th-c. attestation of the loan. The printed page (pdf p. 219) shows «حَبل» with plain ḥāʾ, matching the JSON.\",\n     \"derivation_fa\": \"«حَبل» در فارسی وام‌واژه‌ای عربی است که پس از اسلام و بی‌هیچ دگرگونی آوایی یا معنایی به کار رفته و همواره واژه‌ای ادبی و کتابی در کنار «رسن» و «ریسمان» فارسی مانده است. معین در فرهنگ فارسی آن را با نشانِ «[ع.]» می‌آورد: «حبل [ع.] (اِ.) ریسمان، رشته، بند». بیت سعدی که نورایی گواه آورده («کله دلو کرد آن پسندیدهکیش / چو حبل اندر آن بست دستار خویش») شاهدی درست از سدهٔ هفتم هجری است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [W+\"%D8%AD%D8%A8%D9%84\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:89\", \"status\": \"not_checked\", \"note\": \"FVA = S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989); refs_online.json records that no digital copy exists on archive.org, ketabnak or noorlib (re-searched 2026-09) — catalogue record only.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part2/part1 line 52392 (2-vol Adena abridgement)\", \"stance\": \"supports\", \"note\": \"'حبل: [ع.] (اِ.) ریسمان، رشته، بند؛ ج. ...' — Mo'in marks the Persian word explicitly as an Arabic loan meaning 'rope'.\"},\n      {\"src\": \"RCH\", \"where\": \"Richardson-Johnson, Persian-Arabic-English (grep 'habl')\", \"stance\": \"partial\", \"note\": \"the dictionary carries ḥabl among its Arabic-in-Persian entries; OCR gives only the derivative sense line, but the headword's presence confirms the loan's currency in Persian lexicography.\"},\n      {\"src\": \"KLN\", \"where\": \"1966 pp. 218-219\", \"stance\": \"silent\", \"note\": \"Klein has nothing on the Persian side of the word.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Portuguese\",\n     \"words\": \"cable\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"This node reproduces Klein 1966 (pp. 218-219) exactly: 'cable, n. — ME. cable, cabel, kable, fr. F. cable, fr. Port. cable, which is a blend of Arab. habl, \\\"rope, cable\\\", and VL. cap(u)lum, \\\"a halter for cattle\\\", fr. capio, capere'. Modern scholarship rejects both halves of that. (a) There is no Portuguese *cable: Portuguese 'cable' is cabo (Wiktionary's translation table), and Portuguese is in any case an implausible transmitter for a word first recorded in English c. 1200/13th c. and in Old NORTHERN French (the Norman dialect that fed English maritime vocabulary). (b) Etymonline and Wiktionary both give the chain Late/Medieval Latin capulum 'lasso, rope, halter for cattle' (< Latin capere 'to seize', PIE *kap-) > Old Northern French cable > Middle English cable, with no Semitic ingredient. Lokotsch no. 766 does derive Medieval Latin capulum itself from Arabic habl, so Nourai's Arabic element is not an invention — but that is a 1927 minority view, and even Lokotsch has no Portuguese stage. Nourai's own NOTE (AHD and FSD derive it from Latin, see root 'Kap') records the mainstream position correctly.\",\n     \"derivation_fa\": \"این گره واژه‌به‌واژه از کلاین (چاپ ۱۹۶۶، صص ۲۱۸–۲۱۹) گرفته شده است: «cable از فرانسه، از پرتغالی cable که آمیزه‌ای است از عربی habl و لاتینی عامیانه cap(u)lum «افسار چارپا»». پژوهش امروزی هر دو بخش را رد می‌کند: نخست آنکه در پرتغالی اصلاً واژهٔ cable نیست و برابرِ آن cabo است؛ دوم آنکه اتیمانلاین و ویکی‌واژه زنجیرهٔ لاتینی capulum «کمند، افسار» (از capere «گرفتن»، هندواروپایی *kap-) ← فرانسهٔ شمالی کهن cable ← انگلیسی میانه cable را می‌دهند، بی‌هیچ عنصر سامی. لوکوچ (شمارهٔ ۷۶۶) خودِ capulum لاتینی را از «حبل» عربی می‌داند، اما آن هم دیدگاهی اقلی از ۱۹۲۷ است و در آن نیز مرحلهٔ پرتغالی وجود ندارد. یادداشت خود نورایی («AHD و FSD آن را از لاتین می‌گیرند») دیدگاه رایج را درست بازگو کرده است.\",\n     \"sources\": [W+\"cable\", \"https://www.etymonline.com/word/cable\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:216\", \"status\": \"supports\", \"note\": \"Found on scan leaf 126 of KLN_1966 = printed pp. 218-219 (Nourai's page number is 2-3 low): 'fr. F. cable, fr. Port. cable, which is a blend of Arab. habl, \\\"rope, cable\\\", and VL. cap(u)lum, \\\"a halter for cattle\\\"'. The reference says exactly what the arrow says; it is the reference that is out of step with current scholarship.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 766\", \"stance\": \"partial\", \"note\": \"'Ar. habl: \\\"Seil\\\"; hieraus mlat. capulum \\\"Fangseil\\\", frz. câble, sp. cablo, engl. cable, ndl. kabel, dtsch. Kabel' — supports an Arabic source for the Latin word but has NO Portuguese link.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, 'Cable, a rope; see Capacious'\", \"stance\": \"contradicts\", \"note\": \"Skeat sends 'cable' to the Latin capere family (capacious) and gives no Semitic or Portuguese source.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins appendix, root *kap-\", \"stance\": \"contradicts\", \"note\": \"cable is listed under PIE *kap- 'to grasp' via Latin capere — the derivation Nourai's own note ascribes to AHD/FSD.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"French\",\n     \"words\": \"kâbl\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The word itself is French câble 'cable, hawser' — Nourai prints it in his own Persian-style transliteration as 'kâbl' (verified on the printed page, pdf p. 219; the extraction is faithful, this is his transliteration convention, not a misprint). The FORM is real, the PARENT is not: French câble comes straight from Late Latin capulum (Wiktionary, s.v. cable / câble), and it is the Old NORTHERN French (Norman) variant cable, not central Old French chable, that reached English c. 1200 — a Portuguese intermediary is unattested. Klein's route (Port. > F.) is what Nourai is copying; it is not the modern account.\",\n     \"derivation_fa\": \"واژهٔ مورد نظر همان câble فرانسوی است؛ نورایی آن را به شیوهٔ آوانگاری فارسیِ خود «kâbl» نوشته است (صفحهٔ چاپی، پی‌دی‌اف ۲۱۹، بررسی شد؛ خطای خوانش اسکن نیست، همان شیوهٔ نگارش کتاب است). خودِ واژه درست است، اما نیای آن نه: câble فرانسوی یکراست از لاتینی متأخر capulum آمده، و همان گونهٔ نورمانی (فرانسهٔ شمالی کهن) cable بود که در حدود ۱۲۰۰ میلادی به انگلیسی رسید. میانجی‌گری پرتغالی هیچ گواهی ندارد و تنها برساختهٔ کلاین است.\",\n     \"sources\": [W+\"cable\", \"https://www.etymonline.com/word/cable\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:216\", \"status\": \"supports\", \"note\": \"KLN_1966 leaf 126 (printed pp. 218-219) s.v. cable: 'fr. F. cable, fr. Port. cable' — the Portuguese > French arrow is verbatim Klein.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 pp. 218-219\", \"stance\": \"supports\", \"note\": \"as quoted; Klein is the only source that inserts Portuguese between Arabic and French.\"},\n      {\"src\": \"PHN\", \"where\": \"Pihan, Dictionnaire des mots français dérivés de l'arabe/persan/turc\", \"stance\": \"silent\", \"note\": \"grep of PHN.txt finds no câble entry — Pihan, whose whole subject is French Arabisms, does not count câble as one.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"no câble entry either; the standard French-orientalism dictionaries decline the Arabic etymology that Klein and Lokotsch propose.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"kâbl «کابل»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian کابل kābl 'cable' is a 20th-century technical borrowing from French câble, brought in with electricity, telephone and telegraph — exactly as drawn. Mo'in's Farhang tags it '[فر.]' (= French): 'کابل (بْ لْ) [فر.] (اِ.) ۱- رشته‌های ضخیمی از سیم‌های تابیده شده با روکش عایق‌دار برای انتقال جریان برق، تلفن و... ۲- رشتهٔ سیم فولادی ضخیم برای بستن و بلند کردن قطعات سنگین'; the derivative کابل‌کشی is tagged '[فر. + ف.]' in the same dictionary. French -â- is rendered by Persian alef, and the final consonant cluster -bl is kept as بل. The homograph کابل Kābol (the Afghan capital) is a wholly unrelated place-name.\",\n     \"derivation_fa\": \"«کابل» در فارسی وام‌واژه‌ای فنی از سدهٔ چهاردهم هجری است که همراه برق و تلفن و تلگراف از فرانسوی câble گرفته شده — دقیقاً همان‌که نورایی کشیده است. معین آن را با نشانِ «[فر.]» می‌آورد: «کابل (بْ لْ) [فر.] (اِ.) رشته‌های ضخیمی از سیم‌های تابیده‌شده با روکش عایق‌دار…»، و مشتق «کابل‌کشی» را «[فر. + ف.]» می‌نویسد. آوای â فرانسوی با الف و خوشهٔ پایانی -bl با «بل» نمایانده شده است. «کابل» به‌عنوان نام پایتخت افغانستان واژه‌ای یکسره جداست و ربطی به این وام‌واژه ندارد.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%A8%D9%84/\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:2777\", \"status\": \"supports\", \"note\": \"Mo'in's entry says what the arrow says — 'کابل ... [فر.] (اِ.)' = French loan, 'cable' (read via abadis.ir's فرهنگ معین section, archived). The printed page number could not be verified: the only local Mo'in text is the 2-vol Adena abridgement (MON_part2.txt line 16805), which has its own pagination; its entry کابل‌کشی preserves the tag '[فر. ف.]'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vajehyab/abadis فرهنگ معین s.v. کابل; MON_part2.txt line 16805-16812\", \"stance\": \"supports\", \"note\": \"'[فر.]' origin tag; 'کابل‌کشی: [فر. ف.] (حامص.) کشیدن سیم‌های زیرزمینی یا زیر دریایی برای برق و تلفن و تلگراف'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi\", \"stance\": \"silent\", \"note\": \"a modern European technical loan is outside the scope of Aryanpur's Indo-European root dictionary; no entry.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"cable\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"English cable is first recorded c. 1200/c. 1205 as Middle English cable, cabel, kable 'large, strong rope or chain used on a ship', borrowed from Old NORTHERN French (Norman) cable — so the immediate French > English arrow as drawn is right, and the nautical sense fits the Anglo-Norman maritime channel. What is not right is the chain behind it: Etymonline and Wiktionary take Old Northern French cable from Late/Medieval Latin capulum 'lasso, rope, halter for cattle', from Latin capere 'to take, seize', PIE *kap- 'to grasp' — no Portuguese and no Arabic. The 19th-c. telegraphic senses (cable 'submarine telegraph line' 1850s, 'cabled message' 1883) are later developments of the same word. Nourai's own note ('See root Kap for another possible root') already points at the accepted etymology, which is why this node is plausible rather than disputed: the word and the proximate borrowing are correct, only the deep ancestry is Klein's minority view.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی cable نخستین بار در حدود ۱۲۰۰ میلادی در انگلیسی میانه به صورت‌های cable/cabel/kable به معنی «طناب یا زنجیر ستبر کشتی» ثبت شده و از فرانسهٔ شمالی کهن (نورمانی) cable وام گرفته شده است؛ پس پیکانِ «فرانسه ← انگلیسی» درست است و معنای دریایی آن نیز با مسیر انگلونورمان می‌خواند. آنچه درست نیست، زنجیرهٔ پشت آن است: اتیمانلاین و ویکی‌واژه cable نورمانی را از لاتینی متأخر capulum «کمند، افسار» (از capere، هندواروپایی *kap-) می‌گیرند، بی‌هیچ حلقهٔ پرتغالی یا عربی. معناهای تلگرافی سدهٔ نوزدهم تحول بعدی همین واژه‌اند. چون خود نورایی در یادداشت به ریشهٔ «Kap» ارجاع داده، این گره «با احتیاط پذیرفتنی» است نه ردشده: واژه و وام‌گیری بی‌واسطه درست‌اند و تنها نیای دور جای چون‌وچرا دارد.\",\n     \"sources\": [W+\"cable\", \"https://www.etymonline.com/word/cable\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:216\", \"status\": \"supports\", \"note\": \"KLN_1966 leaf 126 = printed pp. 218-219: 'cable, n. — ME. cable, cabel, kable, fr. F. cable, ...' — Klein's English > French link is exactly Nourai's arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat, 'Cable, a rope; see Capacious'\", \"stance\": \"contradicts\", \"note\": \"Skeat routes cable to Latin capere, i.e. the *kap- family, not to Arabic.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins appendix s.v. *kap- 'to grasp'\", \"stance\": \"contradicts\", \"note\": \"cable listed among the Latin capere derivatives — Nourai's own note concedes this ('AHD and FSD drive it from Latin').\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. 1, s.v. cable (p. 366 region)\", \"stance\": \"partial\", \"note\": \"the entry is present but the column OCR is broken; per Nourai's own note FSD derives it from Latin.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Haem, Haya\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Avestan haya-, hya- n. 'peculiarity, characteristic behaviour' (acc. haēm), Bartholomae AiW col. 1781\",\n   \"note\": \"Both the language label and the gloss are right, and the two shapes in the root box are the same word: haya-/hya- is the stem, haēm the accusative singular that Horn quotes from Vd. 13.44 (= Westergaard 13.124), which is why Nourai heads the box 'Haem, Haya'. Bartholomae AiW s.v. haya-: 'j. haya-, hya- n. \\\"Eigentümlichkeit, eigentümliches Gebahren\\\": asti hē (sc. sūnahe) haēm yaθa ... \\\"er (der Hund) zeigt ein Gebahren wie ...\\\" V. 13.44; 45-48'. Nyberg reconstructs an Old Iranian *haiman- behind Middle Persian xēm, which accounts for the ē/ī. The root's second citation is printed 'FVS:168,179', an abbreviation that does not exist in Nourai's Table IV; the identical numbers reappear on the Persian node as 'FSF:168,179' (Noushin, Vazhe-namak), so FVS is the book's own typo for FSF — a book slip, faithfully extracted.\",\n   \"note_fa\": \"برچسب زبانی و معنای جعبهٔ ریشه هر دو درست است و دو صورتِ آن یک واژه‌اند: haya-/hya- ستاک است و haēm صورت راییِ مفرد که هرن از وندیداد ۱۳٫۴۴ (وسترگارد ۱۳٫۱۲۴) نقل کرده، و از همین رو نورایی سرِ جعبه را «Haem, Haya» نوشته است. بارتولومه در فرهنگ ایرانی باستان (ستون ۱۷۸۱) می‌آورد: «haya-, hya- (خنثی) «ویژگی، رفتار ویژه»». نیبرگ برای فارسی میانهٔ xēm صورت ایرانی باستان *haiman- را بازسازی می‌کند که کشیدگی ē/ī را توضیح می‌دهد. ارجاع دوم جعبهٔ ریشه «FVS:168,179» چاپ شده که چنین اختصاری در فهرست منابع نورایی نیست؛ همان شماره‌ها در گرهٔ فارسی «FSF:168,179» (واژه‌نامک نوشین) آمده، پس FVS خطای چاپی خود کتاب است، نه خطای خوانش اسکن. ادعای نورایی درست است.\",\n   \"sources\": [W+\"%D8%AE%DB%8C%D9%85\"],\n   \"ref_check\": [\n    {\"ref\": \"HRN:114\", \"status\": \"supports\", \"note\": \"HRN.txt scan leaf 136 = printed p. 114, entry 516: 'χīm \\\"Naturanlage, Charakter\\\", vergl. bedχīm, dušχīm, duzχīm ... aw. vergl. haya-, haēm vd. 13 (124), pancō.hya- (Geldner, KZ. 30, 514 Note 1); phlv. χēm bezw. χīm ..., huχīm ..., dušχēm'. This is precisely the root box: Avestan haya-/haēm.\"},\n    {\"ref\": \"FVS:168,179\", \"status\": \"not_found\", \"note\": \"'FVS' is not defined in Nourai's Table IV (refs_online.json flags it as 'probably a typo'). The same page numbers appear on the Persian node as FSF:168,179 = Noushin's Vazhe-namak, where خیم and دژخیم do occur — so FVS is a misprint for FSF in the book itself.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. 1781, s.v. haya-\", \"stance\": \"supports\", \"note\": \"'j. haya-, hya- n. \\\"Eigentümlichkeit, eigentümliches Gebahren\\\": asti hē haēm yaθa .. V. 13. 44; -- aiti sē hayaiti yaθa .. V. 13. 45-48' — both shapes of Nourai's root box, with the right gloss.\"},\n    {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. xēm\", \"stance\": \"supports\", \"note\": \"'xēm [hym] nature, disposition, temper 90.18,19,23 ... Cf Av. (1781) haya-, hya- \\\"peculiarity\\\"; hence OIr *haiman- or the like. Paz. NP xīm.'\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p. 141 (§29, the ap. ai = np. ē list)\", \"stance\": \"supports\", \"note\": \"'xīm \\\"Charakter\\\", duzxīm, dušxīm \\\"von schlechtem Charakter\\\", paz. dušxīm Mīn. Gl. 68, arm. dixem \\\"schlecht\\\"' — Hübschmann files xīm among the words whose ī goes back to an old diphthong ai, exactly what Av. haēm requires.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"xîm\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian xēm (Book Pahlavi <hym>) 'nature, character, disposition' continues an Old Iranian *haiman-/*haima- built on the Avestan stem haya-/hya-; the Avestan accusative haēm shows the diphthong that regularly yields Middle Persian ē (and New Persian ī), and the initial h- appears in Book Pahlavi's <h> grapheme, which MacKenzie and Nyberg both transcribe x- in this word (compare Pāzand dušxīm, Armenian loan dixem). MacKenzie p. 94: 'xēm [hym] nature, character'; the compounds hu-xēm 'of good character' (PHD p. 45) and duš-xēm / wad-xēm 'evil-natured, ill-natured' show the word was fully productive in Pahlavi. Nyberg cites it from the Mēnōg ī Xrad (90.18,19,23) and derives it 'from OIr *haiman- or the like' — Nourai's arrow exactly.\",\n     \"derivation_fa\": \"فارسی میانهٔ xēm (در پهلوی کتابی <hym>) به معنی «خوی، سرشت، منش» دنبالهٔ صورتی ایرانی باستان *haiman-/*haima- است که بر ستاک اوستایی haya-/hya- ساخته شده؛ دوواکهٔ ai در صورت راییِ اوستایی haēm همان است که در فارسی میانه به ē و در فارسی نو به ī بدل می‌شود. مکنزی در فرهنگ کوچک پهلوی (ص ۹۴) می‌آورد: «xēm [hym] خوی، منش»، و ترکیب‌های hu-xēm «نیک‌خوی» (ص ۴۵) و duš-xēm / wad-xēm «بدخوی» نشان می‌دهد واژه در پهلوی زایا بوده است. نیبرگ آن را از مینوی خرد (۹۰:۱۸،۱۹،۲۳) گواه می‌آورد و از «*haiman- ایرانی باستان» می‌گیرد — همان چیزی که نورایی کشیده است. ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%AE%DB%8C%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"PHD:94\", \"status\": \"supports\", \"note\": \"Exact hit. PHD_mackenzie.txt line 5554, form-feed leaf 115 = printed page 94 (MacKenzie's offset: leaf = printed + 21): 'xēm [hym] nature, character.' The gloss 'temper, nature' in the chart is MacKenzie's.\"},\n      {\"ref\": \"HRN:114\", \"status\": \"supports\", \"note\": \"HRN leaf 136 = printed p. 114, no. 516: 'phlv. χēm bezw. χīm (vd. 13 (124), 5 (117) Gl.), huχīm ..., dušχēm' — Horn gives the Pahlavi stage with both vowel spellings.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 94 (xēm); p. 45 (hu-xēm); s.v. duš-, wad-\", \"stance\": \"supports\", \"note\": \"'xēm [hym] nature, character'; 'hu-xēm [hwhym] of good character, good-natured'; 'duš-xēm [-hym] evil-natured'; 'wad-xēm [-hym] ill-natured'.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p. (glossary) s.v. xēm\", \"stance\": \"supports\", \"note\": \"'xēm [hym] nature, disposition, temper 90.18,19,23 ... Cf Av. (1781) haya-, hya- \\\"peculiarity\\\"; hence OIr *haiman- or the like.'\"},\n      {\"src\": \"BRT\", \"where\": \"AiW col. 1781\", \"stance\": \"supports\", \"note\": \"provides the Avestan etymon haya-/haēm that both PHD and NYB point back to.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"xîm «خیم»; dožxîm «دژخیم»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian خیم xīm 'temper, nature, disposition' continues Middle Persian xēm with the regular NP raising of MP ē to ī (as in šēr > šīr, bēm > bīm — Hübschmann files xīm precisely in that class). It is an archaic, mainly Ferdowsian word: Nourai's line دگر خوی را آنک خوانیم خیم / که با او ندارد دل از دیو بیم is genuine Šāh-nāma (Noushin's Vazhe-namak quotes the same verse under خیم, adding that Ferdowsi there defines the word himself). دژخیم dož-xīm = MP duš-xēm 'of evil nature', with the productive prefix duš-/duž- 'ill, bad' (Av. duš-, PIE *dus-); Borhān-e Qāṭeʿ still glosses خیم as 'خوی و طبیعت' and adds 'و بعضی خوی بد را خیم [گویند]'. In modern Persian دژخیم has drifted from 'ill-natured' to 'executioner, torturer', but that is a later specialisation, not the classical sense Nourai gives. The chart's extra forms بدخیم / خوش‌خیم (now chiefly medical, 'malignant / benign') are the same compound type, matching Horn's bedχīm and Pahlavi hu-xēm.\",\n     \"derivation_fa\": \"«خیم» در فارسی نو دنبالهٔ xēm فارسی میانه است؛ ē کشیدهٔ فارسی میانه در فارسی نو به ī بدل شده (مانند شیر < šēr و بیم < bēm)، و هوبشمان همین واژه را در همان دستهٔ آوایی جای داده است. واژه‌ای کهن و بیشتر فردوسی‌وار است: بیتِ «دگر خوی را آنک خوانیم خیم / که با او ندارد دل از دیو بیم» در شاهنامه آمده و نوشین در واژه‌نامک ذیل «خیم» همان بیت را گواه می‌آورد و می‌گوید فردوسی خودْ واژه را در آن معنی کرده است. «دژخیم» همان duš-xēm پهلوی است با پیشوند زایای duš-/duž- «بد» (اوستایی duš-، هندواروپایی *dus-)؛ برهان قاطع نیز «خیم» را «خوی و طبیعت» و «بعضی خوی بد» معنی کرده است. در فارسی امروز «دژخیم» به «جلاد، شکنجه‌گر» تخصیص یافته که تحول معنایی متأخر است، نه معنای کلاسیکی که نورایی آورده. «بدخیم» و «خوش‌خیم» نیز از همین گونهٔ ترکیب‌اند (نزد هرن bedχīm، در پهلوی hu-xēm). ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%AE%DB%8C%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:804\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 2, form-feed page 264 of BQT_v2_pages.txt (≈ printed p. 801-804, the خی section): headword 'خیم = بکسر اول بر وزن ... خوی و طبیعت باشد؛ و بعضی خوی بد را خیم [گویند]' with Mo'in's footnote 1 giving the Pahlavi and Avestan forms and citing Hübschmann and Bartholomae (col. 1781/1782).\"},\n      {\"ref\": \"HRN:114\", \"status\": \"supports\", \"note\": \"Horn no. 516, printed p. 114: 'χīm \\\"Naturanlage, Charakter\\\", vergl. bedχīm, dušχīm, duzχīm (Vis und Rāmīn S. 32 V. 5)' — both of Nourai's Persian words, plus the بدخیم of the chart's extra line.\"},\n      {\"ref\": \"FSF:168,179\", \"status\": \"partial\", \"note\": \"Noushin's Vazhe-namak does carry both entries with exactly Nourai's verse — FSF_pages.txt leaf 223 ('خیم (بروزن بیم)'; 'خود در بیت زیر «خیم» را معنی می‌کند: دگر خوی را آنک خوانیم خیم') and leaves 237-238 ('دژخیم'; 'جزء دوم واژهٔ مرکب دژخیم') — but in the scan available here those fall on printed pp. ~220 and ~234-235 (printed ≈ leaf − 3), not 168/179; the scanned printing differs from Nourai's Donyā 1363 edition.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 2, خی section (BQT_v2_pages.txt leaf 264), with Mo'in's footnote\", \"stance\": \"supports\", \"note\": \"'خیم ... خوی و طبیعت باشد' + footnote 'پهلوی xēm ... از اوستا haēm ... هوبشمان ...؛ بارتولمه ۱۷۸۱/۱۷۸۲'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 516, p. 114\", \"stance\": \"supports\", \"note\": \"'χīm \\\"Naturanlage, Charakter\\\" ... aw. vergl. haya-, haēm ...; phlv. χēm bezw. χīm'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 141\", \"stance\": \"supports\", \"note\": \"'xīm \\\"Charakter\\\", duzxīm, dušxīm \\\"von schlechtem Charakter\\\", paz. dušxīm Mīn. Gl. 68' — confirms دژخیم back to Pāzand/Pahlavi.\"},\n      {\"src\": \"FSF\", \"where\": \"Vazhe-namak, leaves 223 and 237-238\", \"stance\": \"supports\", \"note\": \"quotes the identical Ferdowsi verse under خیم and treats دژخیم as دژ/دش + خیم.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Hâvana\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Avestan hāvana- m. 'the haoma-pressing implement (mortar and pestle)', an instrument noun of Av. hav- 'to press (the haoma)'\",\n   \"note\": \"Root, language label and gloss are all right, with one refinement worth recording: hāvana- is not an unanalysable root but a derivative of the Avestan verb hav- 'auspressen, keltern' (Bartholomae AiW: 'j. 1hav- V. \\\"auspressen\\\", den Haoma'), the same base as haoma- itself and as Vedic sav-/soma-; ultimately PIE *sew-/*sū- 'to press out juice' (Av. hunāmi = Skt. sunómi). So the box is better read as 'Av. hāvana- \\\"presser, mortar\\\" < hav- \\\"to press\\\"'. Bartholomae glosses hāvana- as the name of BOTH parts of the haoma apparatus, trough and pestle, so 'mortar' is a fair, if narrowed, rendering. Nourai's ref for both the root and the Pahlavi node is MON:5095, but the substantive support is Mo'in's own footnote in Borhan-e Qate' (BQT 2312-13) which spells the chain out.\",\n   \"note_fa\": \"برچسب زبانی، صورت و معنای جعبهٔ ریشه هر سه درست است، با یک نکتهٔ تکمیلی: hāvana- اوستایی ریشه نیست بلکه اسم ابزار از فعل اوستایی hav- «فشردن، افشردن (هوم)» است (بارتولومه: «hav- «auspressen»، den Haoma»)، از همان بنیادی که «هَوم/هوم» و در سنسکریت sav-/soma از آن آمده‌اند؛ در نهایت از هندواروپایی آغازین *sew-/*sū- «افشردن، آب گرفتن» (اوستایی hunāmi برابر سنسکریت sunómi). بارتولومه hāvana- را نام هر دو پارهٔ ابزار هومکوبی (هاون و دسته) می‌داند، پس معنی «هاون» تنگ‌شده اما درست است. ارجاع نورایی برای ریشه و گرهٔ پهلوی «MON:5095» است، ولی گواه اصلی حاشیهٔ خود معین بر برهان قاطع (صص ۲۳۱۲–۲۳۱۳) است که همین زنجیره را می‌آورد.\",\n   \"sources\": [],\n   \"ref_check\": [\n    {\"ref\": \"MON:5095\", \"status\": \"partial\", \"note\": \"Mo'in's dictionary does tag هاون as Pahlavi — 'هاون (وَ) [ په . ] (اِ.) ظرفی آهنی یا سنگی که در آن چیزی را می‌کوبند یا می‌سایند' (فرهنگ معین, read via abadis.ir and archived) — but Mo'in's printed entry gives no Avestan form, and the page number could not be checked (the only local copy is the 2-vol Adena abridgement, MON_part2.txt line 88804, with its own pagination). The Avestan hāvana- of the root box comes from Mo'in's Borhan footnote (BQT 2312-13), not from the Farhang entry.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. 1784 s.v. hāvana-; col. 1783 s.v. 1hav-\", \"stance\": \"supports\", \"note\": \"'j. hāvana- m. (\\\"Auspresser, Kelterer\\\") Name für die beiden Teile des bei der Haomabereitung verwendeten Geräts, spez. ... des Trogs und Stössels'; and 'j. 1hav- V. \\\"auspressen\\\", den Haoma ... aθa hāvana haomąn hunyāt'.\"},\n    {\"src\": \"POK\", \"where\": \"IEW s.v. *seu-/*sū- (Av. hunāmi ~ Skt. sunómi)\", \"stance\": \"supports\", \"note\": \"POK_full.txt: 'present *sunami (Avestan hunami) and *suHti (compare Old Indic suyate)' — the IE base of the verb from which hāvana- is formed.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', Mo'in's footnote to هاون, printed pp. 2312-13 (BQT_v4_pages.txt pdf page 396)\", \"stance\": \"supports\", \"note\": \"'اوستا hāvana (هاون). پهلوی hāvan ... اساساً هاون (هاونهٔ اوستایی) ظرفی است که زرتشتیان در آن «هوم» را با دسته می‌کوبند'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"hâvan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian hāwan <h'wn'> 'a mortar' is the direct continuation of Avestan hāvana-: intervocalic -v- stays as -w-, the Avestan thematic ending -a is lost as everywhere in Middle Persian, giving hāvana- > hāwan. MacKenzie's Concise Pahlavi Dictionary (p. 45) lists it twice over, distinguishing the object from the liturgical hour: '1hāwan [h'wn' | N ~] a mortar' and '2hāwan [h'wn' = Av. hāwani-] the morning gāh' — the second entry showing that MacKenzie himself equates the Pahlavi form directly with the Avestan stem. The word kept its Zoroastrian ritual anchoring: the hāwan is the vessel in which the haoma is pounded, and hāwan-gāh is the sunrise watch during which the pressing is done.\",\n     \"derivation_fa\": \"فارسی میانهٔ hāwan (پهلوی کتابی <h'wn'>) «هاون» دنبالهٔ مستقیم hāvana- اوستایی است: v میان دو واکه به w می‌ماند و پایانهٔ ستاکی -a اوستایی، چنان‌که در فارسی میانه قاعده است، می‌افتد؛ پس hāvana- ← hāwan. مکنزی در فرهنگ کوچک پهلوی (ص ۴۵) آن را دو بار می‌آورد: «hāwan [h'wn'] هاون» و «hāwan [h'wn' = اوستایی hāwani-] گاهِ بامدادی»، و در دومی خود صورت پهلوی را با ستاک اوستایی برابر می‌نهد. پیوند آیینی واژه پابرجا مانده: هاون ظرفی است که زرتشتیان هوم را در آن می‌کوبند و «هاون‌گاه» بخش نخست روز است که هوم‌کوبی در آن انجام می‌گیرد. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"MON:5095\", \"status\": \"partial\", \"note\": \"Mo'in tags the Persian outcome '[ په . ]' = from Pahlavi, which is the arrow drawn here, but he supplies no Pahlavi transliteration in the entry and the printed page could not be located in the abridged local copy. The Pahlavi form itself is confirmed from MacKenzie (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 45 (PHD.txt form-feed leaf 66-67; leaf = printed + 21)\", \"stance\": \"supports\", \"note\": \"'1hāwan [h'wn' | N ~] a mortar. 2hāwan [h'wn' = Av. hāwani-] the morning gāh.' — the Pahlavi word, the gloss 'mortar', and the New Persian continuation, all as drawn.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 1089, printed p. 244\", \"stance\": \"supports\", \"note\": \"'aw. hāvana- \\\"Mörser\\\"; phlv. hāvan, arm. LW. havan' — Horn gives exactly the Avestan > Pahlavi step.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW col. 1784\", \"stance\": \"supports\", \"note\": \"the Avestan parent hāvana- 'the haoma-pressing implement'.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for 'hawan/hāwan' returns nothing — Nyberg's glossary is limited to the texts he edits and does not include the word.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"hâvan «هاون»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian هاون hāvan (also hāven, hāvon) 'mortar' continues Middle Persian hāwan unchanged apart from the ordinary NP treatment of -w- as -v-. Horn no. 1089 (p. 244) sets out the whole line: 'hāven \\\"Mörser\\\" ..., kaukas.-bergjüd. heveng, arab. LW. hāvun; aw. hāvana- \\\"Mörser\\\"; phlv. hāvan, arm. LW. havan'. Mo'in's footnote in Borhan-e Qateʿ (pp. 2312-13) adds the dialect and loan evidence — Kurdish hāvan, Arāk (Solṭānābād) hāvon, Armenian havan — and the Arabic borrowing: 'معرب هاون hāwan ... در تعریب هاون (بفتح واو) و هاوون ... جمع آن أهوان است' (citing Addi Shir p. 989 and Dozy), i.e. a Persian > Arabic loan, the reverse direction from the حبل of the first chart on this page. Mo'in's Farhang tags the word '[ په . ]' (from Pahlavi). Nourai's Marzbān-nāma couplet (نه پیش من دواوین بود و دفتر / نه عیسی را عقاقیر است و هاون) is a genuine Persian attestation. The ritual sense survives in هاون‌گاه hāvan-gāh, the morning watch, and in هاون‌دسته 'pestle'.\",\n     \"derivation_fa\": \"«هاون» فارسی نو دنبالهٔ بی‌واسطهٔ hāwan فارسی میانه است و جز تبدیل عادی w به v دگرگونی دیگری ندارد؛ گونه‌های «هاوَن/هاوُن» نیز ثبت شده است. هرن (شمارهٔ ۱۰۸۹، ص ۲۴۴) همهٔ زنجیره را می‌آورد: «hāven «هاون»؛ اوستایی hāvana-؛ پهلوی hāvan؛ وام‌واژهٔ ارمنی havan؛ وام‌واژهٔ عربی hāwun». معین در حاشیهٔ برهان قاطع (صص ۲۳۱۲–۲۳۱۳) گواه‌های گویشی و وام‌گیری‌ها را می‌افزاید: کردی hāvan، اراکی hāvon، ارمنی havan، و «معرّب هاون … جمع آن «أهوان» است» به نقل از ادّی‌شیر (ص ۹۸۹) و دُزی — یعنی وام‌گیری از فارسی به عربی، وارونهٔ مسیر «حبل» در جدول نخست همین صفحه. معین در فرهنگ فارسی نیز آن را «[په.]» می‌داند. بیت مرزبان‌نامه که نورایی آورده گواهی درست است. معنای آیینی واژه در «هاون‌گاه» و «هاون‌دسته» بازمانده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%D9%87%D8%A7%D9%88%D9%86/\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2312\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 4, BQT_v4_pages.txt pdf page 396 (printed 2312-13): headword 'هاون — ظرفی فلزی (غالباً مسی) با سنگی که در آن ادویه و تخم‌های گیاهان و غیره را با دسته‌ای کوبند' with Mo'in's footnote 'اوستا hāvana (هاون). پهلوی hāvan. ارمنی havan ... معرب هاون hāwan «اسشق ۹۸۹» ... اساساً هاون (هاونهٔ اوستایی) ظرفی است که زرتشتیان در آن «هوم» را با دسته می‌کوبند' — the whole Avestan > Pahlavi > Persian arrow, verbatim.\"},\n      {\"ref\": \"HRN:244\", \"status\": \"supports\", \"note\": \"HRN.txt form-feed leaf 266 = printed p. 244, no. 1089: 'hāven \\\"Mörser\\\", (AM. 132 Zeile 6), kaukas.-bergjüd. heveng, arab. LW. hāvun. aw. hāvana- \\\"Mörser\\\"; phlv. hāvan, arm. LW. havan.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"vol. 4, printed pp. 2312-13, Mo'in's footnote\", \"stance\": \"supports\", \"note\": \"as quoted; also 'در اوستا hāvani- که اکنون «هاون‌گاه» گویند ... وقتی است که در آن هوم تهیه می‌شود'.\"},\n      {\"src\": \"MON\", \"where\": \"فرهنگ معین s.v. هاون (via abadis, archived); MON_part2.txt line 88804\", \"stance\": \"supports\", \"note\": \"'هاون (وَ) [ په . ] (اِ.) ظرفی آهنی یا سنگی که در آن چیزی را می‌کوبند یا می‌سایند' — Pahlavi origin tag; the abridgement adds 'یکی از آلات مقدس پرستشگاه زردشتیان بوده و در آن گیاه هوم را می‌کوبیده‌اند'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 1089, p. 244\", \"stance\": \"supports\", \"note\": \"Avestan > Pahlavi > New Persian, plus the Armenian and Arabic loans.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir p. 989, as cited by Mo'in\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote credits «اسشق ۹۸۹» (= Addi Shir, Kitab al-alfaz al-farisiyya al-muʿarraba) for Arabic hāwan/hāwūn being an Arabicised Persian word — i.e. the loan runs Persian > Arabic.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('data/verification/page-219.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=1)\nprint('written')\nPYEOF\npython3 -m json.tool data/verification/page-219.json > /dev/null && echo \"valid json\"\npython3 tools/verify_check.py 219"
}
```


### [2026-09-06T15:25:59.839Z] TOOL RESULT

```
written
valid json
nodes verified: 10/10
node verdicts: {'disputed': 3, 'confirmed': 6, 'plausible': 1}
root verdicts: {'disputed': 1, 'confirmed': 2}
ref checks: {'partial': 3, 'not_checked': 1, 'supports': 10}
books consulted: {'partial': 5, 'supports': 18, 'silent': 5, 'contradicts': 4} | by book: {'KLN': 3, 'MON': 3, 'HRN': 3, 'LKT': 2, 'RCH': 2, 'SKT': 2, 'AHD': 2, 'PHD': 2, 'NYB': 2, 'BRT': 2, 'BQT': 2, 'PHN': 1, 'DEV': 1, 'ARY': 1, 'FSD': 1, 'HUB': 1, 'FSF': 1, 'AFM': 1}
```


## [2026-09-06T15:26:07.832Z] TOOL CALL #67: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null | head; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg219.png data/verification/sources/refs/ocr/BOOK/219.png && ls -la data/verification/sources/refs/ocr/BOOK/219.png"
}
```


### [2026-09-06T15:26:07.910Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
-rw-rw-r-- 1 sfmqrb sfmqrb 71937 Sep  6 11:26 data/verification/sources/refs/ocr/BOOK/219.png
```


## [2026-09-06T15:26:29.481Z] AGENT

Page 219 (book p. 189) verified. `verify_check.py 219`: 10/10 nodes, **0 PROBLEM lines**.

**Verdicts** — roots: 2 confirmed, 1 disputed. Nodes: 6 confirmed, 1 plausible, 3 disputed. Ref checks: 10 supports, 3 partial, 1 not_checked.

**Disputed items**
- ROOT `Habl` "[Aramaic] rope" — Arabic حَبْل is inherited from Proto-Semitic *ḥabl- (native root ḥ-b-l, *ḥabala* "he bound"); Aramaic ḥablā is a cognate, not the source. Klein himself (whom Nourai follows) only says "rel. to … Aram. habhla".
- #1 Arabic `habl` — same reason: the Aramaic→Arabic arrow is not what any source draws.
- #3 Portuguese `cable` — verbatim Klein 1966, but there is no Portuguese *cable* (Pg. is *cabo*); Etymonline/Wiktionary/Skeat/AHD: Late Latin *capulum* < *capere* < PIE \*kap-. Lokotsch 766 does derive ML *capulum* from Arabic *habl*, so the Arabic element is a real (1927, minority) view — but with no Portuguese stage.
- #4 French `kâbl` — word real (Fr. *câble*), parent wrong: it comes straight from Late Latin *capulum*; Old **Northern** French *cable* is what reached English. Pihan and Devic, the two French-Arabism dictionaries, are silent on *câble*.
- #6 English `cable` marked **plausible**: proximate French→English step is right, only the deep ancestry is Klein's.

**Confirmed with exact reference hits**
- HRN:114 no. 516 = "χīm … aw. vergl. haya-, haēm vd. 13 (124); phlv. χēm bezw. χīm" — the root box "Haem, Haya" is straight from Horn; Bartholomae AiW 1781 and Nyberg (OIr *haiman-) agree.
- PHD:94 exact: "xēm [hym] nature, character" (MacKenzie leaf 115 = printed 94).
- HRN:244 no. 1089 and BQT 2312-13 (Mo'in's footnote: "اوستا hāvana… پهلوی hāvan… معرب هاون") confirm Av. hāvana- > MP hāwan > NP هاون; MacKenzie p. 45 "hāwan … a mortar".

**No extraction errors.** I checked the printed page (pdf p. 219, copied to `data/verification/sources/refs/ocr/BOOK/219.png`): «حَبل» with plain ḥāʾ, "kâbl" for French, and the root/node ref split `FVS:168,179` vs `FSF:168,179` are all as printed. Two book-side notes for the owner, not data fixes:
- `FVS` is undefined in Nourai's Table IV; the same page numbers recur as `FSF` on the child node, so FVS is the **book's** typo for FSF (Noushin).
- `KLN:216` is 2–3 pages low — the *cable* entry sits on printed pp. 218–219 of the 1966 edition.

Unverifiable: `VDQ:176` (noorlib is JS-only; the original Jeffery FVQ has no *ḥabl* entry at all) and `FVA:89` (no digital copy exists). `FSF:168,179` is partial — both entries with Nourai's exact Ferdowsi verse are in Vazhe-namak, but at pp. ~220/~235 in the available printing.
