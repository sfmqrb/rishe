# Verification process log — verify-page-427


## [2026-09-14T01:21:46.754Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 427 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-427.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-427.json. Write /home/sfmqrb/git/rishe/data/verification/page-427.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 427` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:47.849Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:48.742Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:48.767Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T01:21:49.248Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-427.txt"
}
```


### [2026-09-14T01:21:49.267Z] TOOL RESULT

```
1	=== PDF page 427 (book page 397) ===
2	--- entry 0 ---
3	ROOT [Arabic] R.z.m : to bundle up, collect  (refs FVA:161)
4	#1 (parent #0) [Arabic] refs=FVA:161 | rezmeh : bundle
5	  #2 (parent #1) [Persian] refs=FVA:161; MON:1649 | rezmeh «رزمه» : bundle
6	  #3 (parent #1) [Spanish] refs=KLN:1307; FSD:2060 | resma : bundle
7	    #4 (parent #3) [French] refs=LAM:199 | rame, rayme : bundle
8	      #5 (parent #4) [English] refs=AHD:1086; KLN:1307 | ream 3 : bundle of paper (500 sheets)
9	
```


## [2026-09-14T01:21:51.926Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-427.json",
 "description": "Read source JSON for page 427"
}
```


### [2026-09-14T01:21:51.966Z] TOOL RESULT

```
{
  "pdf_page": 427,
  "book_page": 397,
  "entries": [
    {
      "root": {
        "name": "R.z.m",
        "lang": "Arabic",
        "refs": "FVA:161",
        "gloss": "to bundle up, collect"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVA:161",
          "words": [
            {
              "translit": "rezmeh",
              "gloss": "bundle",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:161; MON:1649",
          "words": [
            {
              "translit": "rezmeh",
              "gloss": "bundle",
              "script": "رزمه"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Spanish",
          "refs": "KLN:1307; FSD:2060",
          "words": [
            {
              "translit": "resma",
              "gloss": "bundle",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "LAM:199",
          "words": [
            {
              "translit": "rame, rayme",
              "gloss": "bundle",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:1086; KLN:1307",
          "words": [
            {
              "translit": "ream 3",
              "gloss": "bundle of paper (500 sheets)",
              "script": null
            }
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


## [2026-09-14T01:21:53.758Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVA','MON','KLN','FSD','LAM','AHD','PLA','AFM','LKT','DOZ','DEV','PHN','ARY','BQT','SKT','WEB','HJB']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-14T01:21:54.867Z] TOOL RESULT

```
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start wit
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
```


## [2026-09-14T01:22:02.958Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80; echo ---; ls ocr 2>/dev/null | head -40"
}
```


### [2026-09-14T01:22:03.027Z] TOOL RESULT

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
---
AFM
ARY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
TAD
```


## [2026-09-14T01:22:03.581Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T01:22:03.643Z] TOOL RESULT

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


## [2026-09-14T01:22:09.232Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN_1966 ream ===\"; grep -n -i \"resma\" KLN_1966.txt | head -20\necho \"=== KLN_1966 rizmah ===\"; grep -n -i \"rizm\" KLN_1966.txt | head -20\necho \"=== KLN_1971 ===\"; grep -n -i \"resma\\|rizm\" KLN_1971.txt | head -20\necho \"=== SKT ===\"; grep -n -i \"resma\\|rizm\" SKT.txt | head -20\necho \"=== LKT ===\"; grep -n -i \"rizma\\|resma\" LKT.txt | head -20\necho \"=== LAM ===\"; grep -n -i \"rame\\b\\|rayme\\|rizma\\|resma\" LAM.txt | head -30"
}
```


### [2026-09-14T01:22:09.385Z] TOOL RESULT

```
=== KLN_1966 ream ===
22917:It.,  fr.  L.  maritima,  neut.  pi.  of  maritimus,  ‘per¬ taining  to  the  sea,  near  the  sea’,  fr.  mare,  ‘sea’. Cp.  OF.  maresme,  Catal.  maresma,  ‘marsh’, which  are  of  the  same  origin,  and  see  maritime. Margaret,  fem.  PN.  —  OF.  Margaret  (F.  Mar¬ guerite),  fr.  L.  margarita,  pearl  .  See  margarite and  cp.  Margery.
31826:ream,  n.,  20  quires  of  paper.  —  ME.  reme,  fr.  OF. ray  me  (F.  rame),  fr.  Sp.  resma,  fr.  Arab.  rizmah, ‘bundle,  bundle  of  paper’.
=== KLN_1966 rizmah ===
2189:algology,  n.,  the  study  of  algae.  —  A  hybrid  coin¬ ed  fr.  L.  alga  and  Gk.  -Xoyla,  fr.  -Xoyo;,  ‘one who  speaks  (in  a  certain  manner) ;  one  who  deals (with  a  certain  topic)’.  See  alga  and  -logy. Derivatives:  algolog-ical,  adj.,  algolog-ist,  n. algor,  n.,  cold;  chill.  —  L.,  fr.  algere,  ‘to  be  cold’. See  algid  and  -or.  For  the  mode  of  formation cp.  terror,  ‘fright’,  fr.  terrere,  ‘to  frighten’,  albor, ‘white  color’,  fr.  albere,  ‘to  be  white’, algorism,  n.,  the  Arabic  system  of  numerals.  — ME.  algorisme,  fr.  OF.  algorisme  (F.  algorith- me),  fr.  ML.  algorismus ,  from  the  inexact  trans¬ literation  of  Arab.  al-Khowarizmi,  ‘the  man  of Khowarizm  (the  modern  Khiva),  surname  of Abu  Jafar  Mohammed  ibn  Musa,  great  mathe¬ matician  of  the  9th  cent.  His  famous  work  Al- jabr  w’al  muqdbalab  (‘Reunion  and  compar¬ ison’),  introduced  the  use  of  Arabic  numerals  in Europe,  which  denoted  a  turning  point  in  the history  of  mathematics.  Cp.  algebra, algous,  adj.,  pertaining  to  algae.  —  L.  algosus, fr.  alga,  ‘seaweed’.  See  Alga  and  -ous. alguazil,  n.,  peace  officer  in  Spain.  —  Sp.  alguacil, fr.  earlier  alguazil,  fr.  Arab,  al-wazfr,  fr.  al-, ‘the’,  and  waztr,  ‘vizier’.  See  vizier, algum,  n.  —  See  almug.
31826:ream,  n.,  20  quires  of  paper.  —  ME.  reme,  fr.  OF. ray  me  (F.  rame),  fr.  Sp.  resma,  fr.  Arab.  rizmah, ‘bundle,  bundle  of  paper’.
=== KLN_1971 ===
11007:by Mohammed ibn Musa al-Khowarizmi, 
11106:literation of Arab. al-Khowarizmi, ‘the man of 
11107:Khowarizm (the modem Khiva), surname of 
145160:Cp. OF. maresme , Catal. maresma , ‘marsh’, 
201037:ray me (F. rame), fr. Sp. resma, fr. Arab. rlzma h , 
=== SKT ===
17847:Soul.  (E.)     A.S.  rizM>/,j<fo'/.4r>« Icel.   s4la,  sdl.  L>an.  rur/,  Swed  t/ii, seeU^  Goth,  saswafa.
=== LKT ===
3891:1705.  Pers.  räsinä: 'Pferdegeschirr,  -sattel',  ebenso  tk.  res- me  'Zügel  und  Kette' ;  hieraus  serb.  re^- ma  'Zügel',  russ.  resma  'Teil  des  Zau- mes'.
3926:1723.  Ar.  rizma:
3927:'Bündel  oder  Pack  Kleider,  Papierstoß' ; hieraus  it.  risma  'ein  Ries  Papier',  sp. \>e,.  resma,raztyia,  VBi.raima,  frz.  rame; engl,  ream,  ndl.  7'iem,  dtsch.  Eies  [mit Abfall  der  letzten  Silbe  des  it.  Grund- worts], dän.  riis,  schwed.  ris.  Dazu sp.  pg.  rima  'ein  Haufen'  (z.  B.  Kleider, Lumpen),  rimero  'Stoß,  Schicht'.  —  Man denke  daran,  daß  das  Baumwollpapier bereits  früh  von  den  Arabern  hergestellt
8353:resma  1723
=== LAM ===
2568:rameurs de rompre sa rame, le Grand Seigneur lui fait
6115:mot serait composé de rame et de berge. Berge et Barge
6129:Rame. Esp : resma. Cat : raima. It : risma, Vieux fr. :
6130:rayme; de m3j ri^ma^ paquet de hardes (2); et vulgaire-
6132:wali, rame de papier. (Bocthor et Dozy. Supp.) On trouve
6136:trame des voiles de navire. (V. Trévoux et Bouill.) Car
9634:Rame
```


## [2026-09-14T01:22:12.473Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DEV ===\"; grep -n -i \"rame\\|rizma\\|resma\" DEV.txt | head -20\necho \"=== PHN ===\"; grep -n -i \"rizma\\|resma\\|RAME\" PHN.txt | head -20\necho \"=== DOZ ===\"; grep -n -i \"rizma\\|resma\\|riem\" DOZ.txt | head -20\necho \"=== FSD4 resma ===\"; grep -n -i \"resma\" FSD_vol4.txt | head -20\necho \"=== AFM رزم ===\"; grep -n \"رزمة\\|الرزمة\" AFM.txt AFM_pages.txt | head -20\necho \"=== PLA ===\"; grep -n -i \"rizma\\|Rizma\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20"
}
```


### [2026-09-14T01:22:12.657Z] TOOL RESULT

```
=== DEV ===
475:L'ancienne  pharmaceutique  disait  pénide  pour  sucre tors.  C'est  le  même  mot  persan.  On  a  r np^woché  peiiidium du  grec  tsvviov,  réseau  de  fils ,  trame ,  parce  que  la cristallisation  du  sucre  candi  s'obtient  au  moyen  de  fds tendus  dans  la  dissolution  sucrée.
684:Ayer.  Arbuste  des  Moluques.  et  Lorsqu'on  fait  des  inci- sions à  ses  rameaux,  il  en  découle  un  suc  limpide  propre à  désaltérer  les  voyageurs.  5?  (^Dict.  de  Dét.  111,  122.)  C'est assurément  le  malais ^jÎ  fiyer,  eau,  bien  que  la  déno- mination *ji  ^l^  kâyou-âyer ,  arbre  d'eau,  s'applique  d'or- dinaire au  ginseng  chinois.
699:AziMECH.  Etoile  aussi  nommée  l'Epi  delaVierge;  en  arabe dUuJî  as-simâk.  Les  cosmographes  orientaux  appliquent ce  nom  à  deux  étoiles  différentes  :  Tune  appelée  dUvJi ^îJt  as-simâk  ar-nlmili,  azimech  armé  d'une  lance,  est Arcturus,  du  Bouvier,  et  la  lance  est  une  petite  étoile  voi- sine ;  l'épithète  ar-rmnih  devient  chez  nos  anciens  astro- nomes, aramech,  alramech,  noms  qu'on  donne  encore  quel- quefois à  cette  étoile.  L'autre  se  nomme  Jjs.>}]  liiUwJî, azimech  désarmé;  c'est  notre  Azimech  ou  a  de  la  Vierge, la  onzième  des  quinze  étoiles  de  première  grandeur  que compte  Alfergani^.
969:ChérameJle,  chermeUe ,  cherembellier,  chéramellier  (portug. cheramella)  sont  d'autres  formes  de  carambolier. ^  Quant  à  la  dénomination  botanique  avcrrhoa,  elle  est prise  du  nom  du  célèbre   philosophe   arabe  Averrhoès, c'est-à-dire  Js^^  ^1  Ibn-rouchd.
1146:Chott.  Vastes  dépressions  du  sol,  en  Algérie,  qu'on suppose  avoir  formé  autrefois  le  lit  d'une  mer  intérieure. Ce  mot,  employé  par  les  géographes,  a  pris  une  certaine notoriété,  depuis  qu'on  songe  à  ramener  la  mer  sur  cette
1334:Felouque.  Petit  navire  à  voiles  et  à  rames.  Esj).  faluca, falua ,  falucho  (petite  barque);  i^ovixxg.  falua ;  liû.  fiduca , fhica.filucca.  Boctbor  traduit  ce  mot  par  »S^  faloûha.  La plupart  des  ctymologistes  rattachent  tous  ces  termes  à l'ancien  arabe  A)é  foidh,  navire.  Mais  M.  Dozy  affirme  que cette  étymologie  doit  être  r^  rejetée  immédiatement  et  sans réserve,  car  dl)i  n'appartient  pas  à  la  langue  qu'on  par- lait au  moyen  âge;  c'est  un  vieux  mot  qu'on  rencontre bien  encore  quelquefois  chez  les  poètes,  parce  que  ceux- ci  recherchent  précisément  les  termes  surannés,  mais  ja- mais chez  les  prosateurs,  ni  dans  la  signification  générale de  navire,  ni  comme  le  nom  d'une  certaine  espèce  de  vais- seau. Le  peuple  et  les  marins  ne  le  connaissent  pas;  il ne  peut  donc  avoir  passé  dans  les  langues  romanes,  car il  va  sans  dire  que  tous  les  mots  arabes  qu'elles  ont  admis appartiennent  à  la  langue  telle  qu'on  la  parlait  ^  ??  Il  est permis  à  un  savant  de  la  valeur  et  de  la  vaste  érudition de  M.  Dozy  d'être  ainsi  affirmatif;  et  nous  n'avons  qu'à nous  incliner  devant  ce  jugement  sans  appel.  Je  me  con- tenterai de  faire  remarquer  que  les  traducteurs  de  la  Bible en  arabe  n'ont  pas  craint  de  choisir  ce  terme  même  di-U Joulk  ou  folk  pour  désigner  l'arche  de  Noé^,  et  le  P.  Ger- main de  Silésie  a  noté  le  mot  avec  ce  sens  dans  son  dic- tionnaire italien-arabe  (1687).
1441:GouRAME.  Nom  d'un  poisson  des  mers  de  l'Inde  et  de la  Chine,  aussi  nommé,  dans  nos  dictionnaires  d'histoire naturelle,  goiirami  ou  goramy  (osphronème)  et,  à  l'île  de
1779:son  oviducte  dans  la  terre  pour  y  pondre  ses  œufs.  «3^ razza  est  dans  Meninski  ^tforamen  ferreum  quo  pessulus excipitur  vel  sera  ??,  ce  qui  est  tout  à  fait  l'un  des  sens  par- ticuliers de  mortaise,  c^  ouverture  pratiquée  dans  une  gâche pour  recevoir  un  pêne?r,  c'est  la  gâche  elle-même  dans Bocthor  et  dans  Cherbonneau,  et  M.  Dozy  tire  de  là  l'es- pagnol alguaza  qui  est  certainement  notre  mot  gâche^.  Mor- taise serait  un  participe  de  la  huitième  forme  du  verbe.
1956:Rame.  Vieux  français  rayme,  esp.  el  [)orlug.  rezma, ital.  risma.  Do  l'arabe  iU^^  rizma,  qui  a  signidé  paquet  de havdes,  ballot^,  puis  rame  de  papier  (dans  Bocthor).
1957:Cette  étymologie,  proposée  par  Sousa,  combattue  par Diez  qui  préfère  la  dérivation  dpiOçxos,  nombre,  de  Mura- tori,  a  été  appuyée  et  mise  hors  de  doute  par  M.  Dozy. [GIoss.  p.  333  et  suiv.)  J'ajouterai  que  rame  s'est  dit, même  en  français,  dans  un  sens  qui  correspond  à  ballot. Ce  sens  n'est  pas  indiqué  dans  le  Dictionnaire  de  Littré; mais  en  voici  deux  exemples  pris  dans  Tournefort  :  ç^Le coton  en  coque,  c'est-à-dire  enveloppé  de  son  fruit, vaut  un  sequin  le  quintal,  et  jusqu'à  lo  ou  is  francs lorsqu'il  est  en  rame,  c'est-à-dire  épluché  et  sans  coque ^.  v «  Nos  marchands  tirent  de  Smyrne  le  coton  filé  ou  caragach, le  coton  en  rame,  les  laines  fines,  etc. ^.  w  Je  ne  sais  trop comment  Muratori  et  Diez  accommoderaient  leur  àpiOyLos à  ce  coton  épluché.
1958:Rizma  est  devenu  par  la  chute  du  z  (comme  dans rayme,  rame)  le  portugais  rima,  amas,  tas,  monceau;  il ne  faudrait  point  vouloir  tirer  de  là  notre  verbe  arrimer qui  a  une  tout  autre  origine.
1986:arrais.  De  l'arabe  (jmajj  raïs,  chef,  dérivé  de  ^jJ^  ras,  tête. (Mot  resté  dans  l'espagnol  res,  tête  de  bétaib)  On  écril aussi  raïs.  «Le  raïs  maure,  a  la  barre,  crie  aux  rameurs.  ^^ iyTour  du  monde,    1"  voL  p.  •)  1  5.)
2383:Àxrf,  voy.  Taraxacum. Aciche,  esp.  voy.  Alchimie,  3i. Acige,  esp.  voy.  Alchimie,  3i. Acipipe,  pg.  voy.  Jubis. Açucar,  pg.  voy.  Sucre. Adaraca ,  hisp.  voy.  Targe. Adarame,  esp.  voy.  Dirhem. Adarga,  hisp.  voy.  Targe. Adarne,  esp.xoy.  Dirhem. Adarnech,  voy.  Alcliimie,  29. Adec ,  voy.  Alchimie ,  h . Adégige,  voy.  Astronomie,  y. Adène.
2682:Alquimia,  hisp.  voy.  Alchimie. ^    Alquirivia,  pg.  voy.  Carvi. Alquitran,  esp.  voy.  Goudron. Alquitranum,  b.  lat.  voy.  Goudron. Alrachas,  voy.  Alchimie,  2 5. Alramech,  voy.  Azimech. AIramudi,  voy.  Alchimie,  2t. AIruccabah,  voy.  Astronomie,  i3. Alsech,  voy.  Alchimie,  33. Altaïr. Al  taris,  voy.  Alchimie,  23.
2753:Aramech,  voy.  Azimech.
2769:Apidfiàs,  voy.  Rame.
3226:Catrame,  ital.  voy.  Goudron.
3260:ranthe. Cheiri,  voy.  Cheiranthe. Chelub,  voy.  Algénib, Chénib,  voy,  Aigénib. Chepula,  lat.  bot.  voy.  Chébule, Cheramella ,  pg.  voy,  Carambolier, Chéramelle,  voy.  Carambolier. Chérembellier,  voy.  Carambolier. Chérif,
3595:G  ou  RAME.
4142:Rame.
=== PHN ===
90:Légende des sept Dobhants; in-8*. (Eitrait de la Rame de rOriimt, juin 1867.)
194:les formes suivantes : Abdérame, Boabdil, Noradin^ Aver-
435:Les élémeots des consonnes arabes, persanes el turques, rame-
1348:l'action de ramener les fractions à un nombre intégral. Le verbe
2506:mise par les historiens ; mais il est assez facile de le ramener
2894:nombre de paires de rames dont ils sont garnis. Il y en a qui
2895:portent depuis une paire jusqu'à cinq paires de rames, nombre
2898:ambassadeurs étrangers ont sept paires de rames. — Le ba-
2900:tinople les habitants des villages du Bosphore et à les ramener
3375:les ramener à leur source orientale. — La cave désigne un
4853:à voiles et à rames, en usage sur la Méditerranée. — Les Ita-
5368:(l'en ramener, par analogie, les autres sens à celui du radical
5380:alcatrào. Les Italiens écrivent catrame, par une m.
5527:à San-Lucar de Barameda.GUE 189
7279:l'entoure. — On peut encore ramener le mot français miche h
7397:mune en Egypte. Suivant Ebn Beîtar, les rameaux de la mélo-
8578:* RAME) (terme de papeterie), s. f. (a.)
8579:iUj^ \rizmai\ assemblage, paquet, ballot' de marchandises; dérivé de
8583:pas dans le mot français rame, on le retrouve transcrit par s
8584:dans l'espagnol et le portugais resma, ainsi que dans l'italien
=== DOZ ===
1248:roeischepen met van vier tot tien riemen, één mast en
2195:rizmay bg Freytag een bundel kleederen; het beduidt
2198:geven, benevens eene rizma Angora- wol, eene rizma
2199:satgn, eene rizma fluweel en eene rizma laken." Dit
2210:p. 97): „Sein Diener hatte ein grosses Bundel, rizma,
2213:den zin is rizma, samengetrokken rima, in het Sp.
2216:^) Zamachsjari, Jsds al-baldga (HS.): 'indaho rizmaton minat-tliij
2219:in denzelfden zin. Het Arab. rizma is bij Bocthor ook
2222:een riem; Pedro de Alcala heeft het (zooals reeds door
2227:(HS. 1376): „Van Hollandsch papier zes rizma's."
2239:men tegenwoordig minder goed schrgft, resma (zoo
2242:in een stuk van 1397. De vorm rizma is in 't Ital.
2284:het zeer natuurlgk, dat hun woord rizma te gelgk
=== FSD4 resma ===
2153:Sa-n!c'u-la,  1   sa-nik'yu-ls,  2   sa-nic'yu-la,  n   Bot  A   ge- nus of  North-Amerlcan  herbaceous  perennials  of  the  fam- ily Apfaccj?,  with  alternate,  palmate  leaves  and  Inconspicu- ous white  purple,  or  yellow  flowers  In  umbels  The  fruits aresmall  globose,  and  covered  with  recurved  bristles  [LL  , sec  3VMCLF  J
46786:magnetic  field  2.  An  Instrument  showing  changes  in  **®“*®*'f®*  1   varino-let,  2   varino-lSt,  n   A   composition  of barometric  pressure  used  to  determine  the  rate  at  which  a   resmate  of  lead,  or  resin  and  compounds  of  lead-manganesO
=== AFM رزم ===
=== PLA ===
```


## [2026-09-14T01:22:29.888Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD3 ream ===\"; grep -n -i \"resma\" FSD_vol3.txt | head; grep -n \"^Ream\\|ream, *n\\|ream,  n\" FSD_vol3.txt | head\necho \"=== WEB ===\"; grep -n -i \"resma\" WEB_vol1.txt | head\necho \"=== MON رزمه ===\"; grep -n \"رزمه\" MON_part1.txt MON_part2.txt | head -20\necho \"=== BQT رزمه ===\"; grep -n \"رزمه\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -20\necho \"=== PLA pages ===\"; grep -n -i \"rizma\\|rezme\" incoming/PLA/PLA_pages.txt | head\necho \"=== TAD ===\"; grep -n \"رزمة\" TAD.txt TAD_pages.txt 2>/dev/null | head\necho \"=== ARB ===\"; grep -n \"رزمة\" ARB_abdulraheem.txt ARB_mo3rb.txt 2>/dev/null | head"
}
```


### [2026-09-14T01:22:30.120Z] TOOL RESULT

```
=== FSD3 ream ===
14776:— Mark Mason, rresmasonrp 1. [ir. rj a Mason
68950:ticf'essary for coniinaiiil, or for a rommiiiider neresMary
123248:presMaria hera^Uma), now widely distributed, destructive to
221222:r.). I< F rame, < Rp resma. < Ar rizma. bundle at
83822:111 trance 3. In figurative use, a stream, nver, also, a
154903:outer Burfoce of au earthenware pipe — p. •dream, n
178025:II. 1 1. 'I'o flow foitli in a Hi ream, ns. wutt'r poure
=== WEB ===
=== MON رزمه ===
MON_part1.txt:31281:جامه» رزمه. پارچه‌ای که قماش را بدان 
MON_part1.txt:67171:ررمه: (ند. ۲2002-022 [ع. رزمه] (ا.) 
=== BQT رزمه ===
BQT_v1_pages.txt:19191:و سبد و بنهٌ قماش باشد و آنرا بعربی رزمه
BQT_v1_pages.txt:25228:بته قماش واسباب را گویندوبعرمی رزمه‌خوانشد.
BQT_v1_pages.txt:26303:کومند وجربی رزمه خوانند .
incoming/BQT/BQT_v3_pages.txt:28131:‎٩۵‏ - یکی دیبا فرو ریزد برزمه
BQT_v2_pages.txt:23927:   ‫است‬   ‫سته‌شده‬   ‫آجیزیتکه‬     ‫بکراول»‬        ‫) عر ( «رزمه‬    ‫‪۹‬‬          ‫‪‎‬ندیزر > ‪.‬‬
=== PLA pages ===
=== TAD ===
=== ARB ===
ARB_mo3rb.txt:1318:ا رزمة عن أفى سعيد عن أبن در يد» فالظاهى عندى أنه مع مئه كاب اجمهرة 
ARB_mo3rb.txt:1319:لان در يد 6 و« أبن رزمة » هو حمد بن عبد أأواحد بن على بن |براهم بن رزمة 6 
ARB_mo3rb.txt:5713:وقال الأعى 6 أخزناء أ أبن | 0 ن أن رزمة 32 2100-5 ع عن 
ARB_mo3rb.txt:11581:5 0 زكرت عن أبن رزمة عن ألى معد عن ابن دريد قال : 2 3 
ARB_mo3rb.txt:18240:58 أخيرنا أبن شدار عن أبن رزمة عن أبى سعيك عر. أ دريدك : أن 
ARB_mo3rb.txt:21599:1 وأخيرنا ابن ب دار عن ابن رزمة عن أبى سعد عن 
ARB_mo3rb.txt:31851:ابن رزمة 1و4 #ورتت ووو:
```


## [2026-09-14T01:22:31.616Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- KLN page locate ---\"; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('ream,  n.,  20  quires')\nprint('leaf(ff before)=', t[:i].count('\\f'))\nprint(t[i-1500:i+400])\nEOF"
}
```


### [2026-09-14T01:22:32.804Z] TOOL RESULT

```
--- KLN page locate ---
leaf(ff before)= 696
r,  n.,  realiz-ing,  adj.,  realiz-ing-ly,  adv.
realm,  n.  —  ME.  realme,  reaume,  fr.  OF.  realme, reaume  (F.  royaume),  ‘kingdom,  realm’,  which is  a  blend  of  OF.  reial  (F.  royal),  ‘regal,  royal’ (see  royal),  and  OF.  reiame,  reemme,  which  de¬ rives  fr.  L.  regimen,  ‘direction,  government’; see  regimen.  Cp.  OProven?.  reyalme,  realme, which  also  derives  fr.  L.  regimen,  and  It.  reame, OSp.  reame,  realme,  which  are  borrowed  fr. OProven?.  or  OF.
realmless,  adj.  —  Coined  by  the  English  poet John  Keats  (1795-1821)  fr.  realm  and  suff.  -less.
realpolitik,  n.,  real,  i.e.  practical,  politics.  —  G. Realpolitik.  See  real,  adj.,  and  politic.
realschule,  n.,  secondary  school  in  which  no  clas¬ sics  are  taught;  the  opposite  of  a  gymnasium.  — G.  Realschule,  lit.  ‘real  (=  practical)  school’; first  used  by  the  German  parson  Chr.  Semler  in 1706.  See  real,  adj.,  and  school,  ‘a  place  of  learn¬ ing’,  and  cp.  the  first  element  in  prec.  word.
realtor,  n.,  a  real  estate  broker.  —  Coined  by  C. Chadbournof  Minneapolis  about  1915  fr.realty, Teal  estate’,  and  agential  suff.  -or.
realty,  n.,  real  estate.  —  Formed  fr.  real,  adj., with  suff.  -ty.
realty,  n.,  royalty  ( obsol .)  —  OF.  realte  (F. royaute),  ft.  VL.  *regalitdtem,  acc.  of  *regalitds, fr.  L.  regalis,  ‘belonging  to  a  king’.  See  regal, adj.,  and  cp.  words  there  referred  to.
ream,  n.,  20  quires  of  paper.  —  ME.  reme,  fr.  OF. ray  me  (F.  rame),  fr.  Sp.  resma,  fr.  Arab.  rizmah, ‘bundle,  bundle  of  paper’.
ream,  n.,  cream;  froth.  —  ME.  rem,  fr.  OE. ream,  ‘cream’,  rel.  to  MLG.  rom,  rome,  Du. room,  MHG.  roum,  G.Rahm,  Icel.  rjomi,  ‘cream’, fr.  Teut.  base  *rauma-,  which  corresponds  peril, to  I.-E.  *raugma-,  whence  Avestic  ra
```


## [2026-09-14T01:22:41.519Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['KLN','FSD','LAM','DEV','PHN','DOZ','LKT','AHD','MON','BQT','FVA','ARB','TAD']:\n    e=d.get(k,{});print('==',k,'| offset:',e.get('page_offset'),'| hint:',str(e.get('lookup_hint'))[:300]);print('   local:',e.get('local_file'))\n\""
}
```


### [2026-09-14T01:22:42.567Z] TOOL RESULT

```
== KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
== FSD | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
== LAM | offset: leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start with running heads like '2 ABRI'.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt
== DEV | offset: leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt
== PHN | offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt
== DOZ | offset: leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Dutch headword in caps at line start.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt
== LKT | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
== AHD | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
== MON | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
== BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
== FVA | offset: None | hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
   local: None
== ARB | offset: None | hint: Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt']
== TAD | offset: 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt']
```


## [2026-09-14T01:22:57.271Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leafof(path, needle):\n    t=open(path,encoding='utf-8',errors='replace').read()\n    i=t.find(needle)\n    return i, t[:i].count('\\f'), t\ni,l,t = leafof('LAM.txt','Rame. Esp : resma')\nprint('LAM leaf',l,'=> printed', l-57)\ni,l,t = leafof('FSD_vol3.txt','< Rp resma')\nprint('FSD3 leaf',l,'=> printed', l+1466)\ni,l,t=leafof('DEV.txt','Rame.  Vieux  fran')\nprint('DEV leaf',l,'=> printed ~', l-30)\ni,l,t=leafof('PHN.txt','RAME) (terme de papeterie')\nprint('PHN leaf',l,'=> printed', l-31)\ni,l,t=leafof('LKT.txt','1723.  Ar.  rizma')\nprint('LKT leaf',l,'=> printed', l-26)\nEOF"
}
```


## [2026-09-14T01:22:58.399Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==666' KLN_1966.txt | head -8; echo \".....\"; awk 'BEGIN{RS=\"\\f\"} NR==697' KLN_1966.txt | head -6"
}
```


### [2026-09-14T01:22:59.533Z] TOOL RESULT

```
LAM leaf 256 => printed 199
FSD3 leaf 602 => printed 2068
DEV leaf 223 => printed ~ 193
PHN leaf 342 => printed 311
LKT leaf 165 => printed 139
```


### [2026-09-14T01:23:00.579Z] TOOL RESULT

```
ns,  gen.  -entis,  pres.  part,  of  procidere, ‘to  fall  forward,  fall  down’,  fr.  1st  pro-  and cadere,  ‘to  fall’.  See  cadence.  For  the  change  of Latin  a  (in  cadere)  to  i  (in  prd-cidere)  see  abigeat and  cp.  words  there  referred  to. proclaim,  tr.  v.  —  ME.  proclamen,  fr.  L.  prdcld- mare,  ‘to  call  out,  cry  out’,  fr.  1st  pro-  and  cld- mare,  ‘to  call,  cry’.  See  claim,  v.
Derivative:  proclaim-er ,  n. proclamation,  n.  —  ME.  proclamacioun,  fr.  MF. (=  F.)  proclamation,  fr.  L .  proclamationem,  acc. of  proclamatio,  ‘a  calling  out,  outcry’,  fr.  pro- clamatus,  pp.  of  proclamare.  See  prec.  word  and -ation.
proclitic,  adj.  —  ModL.  procliticus,  formed  on analogy  of  encliticus  fr,  Gk.  TrpoxXIvsiv,  ‘to lean  forward’,  fr.  itpo  (see  2nd  pro-)  and  xXTveiv, ‘to  lean’.  See  enclitic.
proclivity,  n.,  tendency,  inclination.  —  F.  procli¬ vity,  fr.  L.  proclivitatem,  acc.  of  prdclivitas,  ‘des¬ cent  ;  tendency,  inclination’,  fr.  proclivis,  ‘slop¬ ing  downward;  inclined’,  fr.  1st  pro-  and  cli¬ vus,  ‘slope,  hill’.  See  clivus  and  -ity. proconsul,  n.  —  ME.,  fr.  L.  proconsul,  from  the phrase  pro  consule,  ‘for,  instead  of,  the  consul’, fr.  pro,  ‘for’  (see  1st  pro-),  and  abl.  of  consul. See  consul  and  cp.  propraetor.
Derivative:  proconsul-ship,  n. proconsular,  adj.  — L .proconsularis,  fr.  proconsul.
See  prec.  word  and  adj.  suff.  -ar. proconsulate,  n.,  office  of  a  proconsul.  —  L. proconsulatus,  fr.  proconsul.  See  proconsul  and subst.  suff.  -ate.
procrastinate,  intr.  v.,  to  postpone.  —  L.  procras¬ tinate,  pp.  of  procrastinare,  ‘to  put  off  till  the morrow’,  fr.  1st  pro-  and  crdstinus,  ‘of  to¬ morrow’,  fr.  eras,  ‘tomorrow’,  which  is  of  un¬ certain  origin.
Derivatives:  procrastinat-ing,  adj.,  procrastinat- ing-ly,  adv.,  procrastinat-ory,  adj. procrastinator,  n.  —  L.  procrastinator,  fr.  pro- crastinatus,  pp.  of  procrastinare.  See  prec.  word and  agential  suff.  -or.
.....
nd  cp.  words  there  referred  to.
ream,  n.,  20  quires  of  paper.  —  ME.  reme,  fr.  OF. ray  me  (F.  rame),  fr.  Sp.  resma,  fr.  Arab.  rizmah, ‘bundle,  bundle  of  paper’.
ream,  n.,  cream;  froth.  —  ME.  rem,  fr.  OE. ream,  ‘cream’,  rel.  to  MLG.  rom,  rome,  Du. room,  MHG.  roum,  G.Rahm,  Icel.  rjomi,  ‘cream’, fr.  Teut.  base  *rauma-,  which  corresponds  peril, to  I.-E.  *raugma-,  whence  Avestic  raoyna-,  ‘but¬ ter’.  Cp.  ramekin.
Derivatives:  ream,  intr.  and  tr.  v.,  ream-y,  adj.
ream,  tr.  v.,  to  enlarge  a  hole.  —  Lit.  ‘to  make room’,  fr.  ME.  remen,  rumen,  fr.  OE.  ryman,  ‘to make  room,  widen’,  fr.  rum,  ‘spacious,  wide’. Cp.  OS.  riimian,  ON.  ryma ,  OFris.  rema,  OHG. rumen,  ‘to  make  room,  widen’.  Cp.  also  E.  dial. rime,  ‘to  enlarge  a  hole’,  and  see  room, reamer,  n.,  a  tool  for  enlarging  a  hole.  —  Formed fr.  prec.  word  with  agential  suff.  -er. Derivatives:  reamer,  tr.  v.,  reamer-er,  n. reanimate,  tr.  v.,  to  bring  back  to  life.  —  Formed fr.  re-  and  animate,  v.
Derivative:  reanimat-ion,  n. reap,  tr.  and  intr.  v.  —  ME.  repen,  ripen,  fr.  OE. repan,  reopan,  ripan,  ‘to  reap’,  rel.  to  MLG. repen,  ‘to  ripple  (flax)’,  Flem.  repen,  ‘to  tear, hackle’,  and  to  ripe  (q.v.)  Cp.  ripple,  ‘to  clean (flax)’.
```


## [2026-09-14T01:23:18.293Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -ho '\"ref\": \"KLN:[0-9]*\"' page-*.json | sort -u | head -40"
}
```


### [2026-09-14T01:23:18.356Z] TOOL RESULT

```
"ref": "KLN:100"
"ref": "KLN:1005"
"ref": "KLN:1007"
"ref": "KLN:1008"
"ref": "KLN:1009"
"ref": "KLN:1014"
"ref": "KLN:1018"
"ref": "KLN:102"
"ref": "KLN:1026"
"ref": "KLN:1027"
"ref": "KLN:1028"
"ref": "KLN:1031"
"ref": "KLN:1032"
"ref": "KLN:1033"
"ref": "KLN:1039"
"ref": "KLN:1042"
"ref": "KLN:1047"
"ref": "KLN:1048"
"ref": "KLN:1049"
"ref": "KLN:1059"
"ref": "KLN:1062"
"ref": "KLN:1065"
"ref": "KLN:1068"
"ref": "KLN:108"
"ref": "KLN:1091"
"ref": "KLN:1092"
"ref": "KLN:1093"
"ref": "KLN:1095"
"ref": "KLN:1097"
"ref": "KLN:1099"
"ref": "KLN:110"
"ref": "KLN:1102"
"ref": "KLN:1106"
"ref": "KLN:1108"
"ref": "KLN:1109"
"ref": "KLN:111"
"ref": "KLN:1110"
"ref": "KLN:1112"
"ref": "KLN:1115"
"ref": "KLN:1127"
```


## [2026-09-14T01:23:19.944Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 - <<'EOF'\nimport json,glob,re\nfor f in sorted(glob.glob('page-*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        for n in [e]+e.get('nodes',[]):\n            for rc in n.get('ref_check',[]) or []:\n                if rc.get('ref','').startswith('KLN:'):\n                    print(f, rc['ref'], rc['status'], rc['note'][:180])\nEOF"
}
```


### [2026-09-14T01:23:21.425Z] TOOL RESULT

```
<persisted-output>
Output too large (168.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bzfkmy6qk.txt

Preview (first 2KB):
page-100.json KLN:163 supports KLN_1966.txt form-feed leaf 97 (printed pp. 163-164, running numerals '170 171' appear at leaf 101): "ben, n., son. — Heb. ben, 'son', rel. to Arab. ibn, Aram.-Syr. bar, 'son', Akk
page-100.json KLN:163 supports KLN_1966.txt form-feed leaf 97 (printed pp. 163-164, running numerals '170 171' appear at leaf 101): "ben, n., son. — Heb. ben, 'son', rel. to Arab. ibn, Aram.-Syr. bar, 'son', Akk
page-100.json KLN:163, 164 supports KLN_1966.txt leaf 97 covers both printed pages: p. 163 'ben, n., son. — Heb. ben, "son" …' and p. 164 'Benjamin, masc. PN.; in the Bible, Jacob's youngest son. — Heb. Binyamin, lit
page-100.json KLN:163 supports KLN_1966.txt leaf 97 (p. 163-164): 'ben, n., son. — Heb. ben … Cp. Benjamin, B'nai B'rith, boanerges' and 'Ben, masc. PN. — Dimin. of Benjamin (q.v.)'; Big Ben is treated a few pag
page-101.json KLN:164 supports KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bār
page-101.json KLN:164 supports KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bār
page-101.json KLN:274 supports KLN_1966.txt leaf 155 (printed pp. 274-275), s.v. 'cherub': 'Heb. kerūbh, winged angel, prob. rel. to Akkad. karābu, to bless, karibu, one who blesses, epithet of the bull-colossus
page-101.json KLN:164 supports KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bār
page-101.json KLN:680 supports KLN_1966.txt leaf 367 (printed p. 681), s.v. 'griffin, griffon, gryphon': 'ME. griffon, fr. OF. grifoun (F. griffon), fr. Late L. gryphus ..., fr. Gk. grūps, gen. grūpos, which was
...
</persisted-output>
```


## [2026-09-14T01:23:25.747Z] TOOL CALL #16: Bash

```json
{
 "command": "grep -o 'KLN:13[0-9][0-9][^|]\\{0,200\\}' /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bzfkmy6qk.txt | sort -u | head -30"
}
```


### [2026-09-14T01:23:26.816Z] TOOL RESULT

```
KLN:1305 supports Klein 1966 leaf 694 (= pp. 1304-1305), s.v. 'raven, n., a large bird of the crow family': '... labial enlargements of I.-E. base *qer-, *qor-, *qr-, imitative of harsh sounds. From
KLN:1370 and KLN:1539 to within two pages): 'sugar, n. 
KLN:1370 supports Klein 1966 p.1370 s.v. 'sacchar-, sacchari-, saccharo-, combining forms meaning "sugar". — Fr. L. saccharon, fr. Gk. σάκχαρον, "sugar", fr. Pali sakkharā, fr. OI. śarkarā, "gravel,
KLN:1380 contradicts KLN_1966.txt line 33668, page marker '1380' on the next line: 'sandal, n. — L. sandalium, fr. Gk. sandalion, dimin. of sandalon, a word from Asia Minor (whence also Pers. sandal), 
KLN:1382 supports Klein s.v. santir (KLN_1966.txt line 33703, scan leaf 734; the leaf-to-page ratio fixed by the three Klein citations on this page — 138, 1382, 1573 — is a consistent 1.915 printed 
KLN:1383 supports KLN_1966.txt line 33732 (page marker '1382' at line 33701, so the entry stands on p.1383): "Saracen, n., 1) an Arab; 2) a Moslem. — ML. Saraceni (pl.), fr. Late Gk. Σαρακηνοί (pl.)
KLN:1386 supports Klein s.v. satrap: 'fr. Gk. σατράπης, ἐξατράπης, fr. OPers. xshathrapavan-, ‘ruler of the province’, compounded of xshathra-, ‘province’, and a derivative of pā(y)-, ‘to guard, pro
```


## [2026-09-14T01:23:34.931Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('raven,  n.,  a  large  bird')\nprint('raven leaf0=',t[:i].count('\\f'))\nj=t.find('ream,  n.,  20  quires')\nprint('ream leaf0=',t[:j].count('\\f'))\n# look for numeric page markers between\nseg=t[i-3000:j+3000]\nfor m in re.finditer(r'^\\s*1[23]\\d\\d\\s*$', seg, re.M):\n    print('marker:',m.group().strip())\n# print lines that are mostly digits\nfor line in seg.split('\\n'):\n    s=line.strip()\n    if re.fullmatch(r'[\\d\\s]{3,12}', s): print('numline:',repr(s))\nEOF"
}
```


### [2026-09-14T01:23:36.122Z] TOOL RESULT

```
raven leaf0= 694
ream leaf0= 696
marker: 1307
numline: '1307'
```


## [2026-09-14T01:23:39.688Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nj=t.find('ream,  n.,  20  quires')\nk=t.rfind('\\n1307\\n',0,j)\nprint('marker at',k,'ream at',j,'gap',j-k)\nprint(repr(t[k-600:k+200]))\nEOF"
}
```


### [2026-09-14T01:23:40.650Z] TOOL RESULT

```
marker at 7982220 ream at 7988071 gap 5851
',  react-ive, adj.,  react-ive-ly,  adv.,  react-ive-ness,  n.,  react¬ ivity,  n.,  react-or,  n.\nre-act,  tr.  v.,  to  act  again.  —  Formed  fr.  re-  and act.\nreaction,  n.  —  Formed  fr.  re-  and  action. Derivatives:  reaction-ary,  adj.  and  n.,  reaction- ari-ness,  n.,  reaction-ar-ism,  n.,  reaction-ar-ist, n.,  reaction-ism,  n.,  reaction-ist,  n. read,  tr.  and  intr.  v.  —  ME.  reden,  fr.  OE.  rsedan, ‘to  advise,  counsel,  discuss,  deliberate,  rule, guess,  interpret,  read’  (whence  OE.  rS-d,  ‘advise, counsel’),  rel.  to  OS.  rddan,  ON.  rada,  Swed.\niouo  -\n1307\nrdda,  OFris.  reda,  Du.  raden,  OHG.  ratan, MHG.  raten,  ‘to  advise,  counsel’,  G.  raten,  ‘to advise,  counsel,  guess’,  erraten,  ‘to  guess’, Goth,  -redan  (e.g.  in  ga-redan,  ‘to'
```


## [2026-09-14T01:23:52.705Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol3.txt',encoding='utf-8',errors='replace').read()\nj=t.find('< Rp resma')\nprint(repr(t[j-700:j+400]))\nprint('---markers---')\nseg=t[j-40000:j+10000]\nprint([m.group().strip() for m in re.finditer(r'^\\s*20[5-7]\\d\\s*$',seg,re.M)])\nEOF"
}
```


### [2026-09-14T01:23:53.816Z] TOOL RESULT

```
'am a eiirtndge*\nshell 4. [Scot] To skim, us cream 3i. To streteh\nout (- \\H ryman, raw, roorrivl ream\'inK*bee\'\'tl«, n\nVan/ The largest mullcl used in culkltig rcaiiilng^lron,\nn \\aul All Iron iimi*i| b> eulkers to open scums before\ndriving In the imkiini - r«‘ain«Nl, pa sury Iiured ur liev-\nileil out hv H spec till Insirument enlarged said of nasal\npassages after tin removal of a portion of the nasal cartilage,\nreaiiu, vi 1. isioi j \'locrf*uni, foam, have u foamy appeor-\nuiiie 2. I Archaic I ’I\'n streteh oneself on getting up or\nawakening - ream\'ln, a lirimfiil, frothing\nream\', « Twenty quires of paper, propi*rly, 4H0 sheets\n(a short ream), but often 500 shectH ur more (a long\nr.). I< F rame, < Rp resma. < Ar rizma. bundle at\npaimrl - printers* ream, 2li/s quires (516 sheets), the\nsurplus to nuike up for waste perfect r.;.\nream*, n lITov Lug A Beut ] Cream, froth, foam —\nream \'(kit", n A ereurn*pot\nream \'age, l rim\'ij, 2 rem\'og, n The number of reams con-\ntained In 11 pai kuge of paiNir\nreamtl, pp Reamed B 8.\nreani\'er, 1 ilm\'.ir, 2 rem\'er, n. 1. One who or that\nwhich reams.\nSpecif ( 1 '
---markers---
[]
```


## [2026-09-14T01:23:53.846Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '67160,67185p' MON_part1.txt; echo \"=== part1 31275 ===\"; sed -n '31275,31290p' MON_part1.txt"
}
```


### [2026-09-14T01:23:53.929Z] TOOL RESULT

```
رزمگاه 


رزمگاه: «تو- (- رزمگه| (اسر.) محل 
جنگ میدان جنگ. 

رزمناو: ۲-۷ (امر.) کشتی تندرو که 
مواظب کشتی‌های دشمن است و برای حمله 
بر کشتی‌های جنگی یا بازرگانی از کناره 
سیار دور می‌شود. (فره.) 

ررمه: (ند. ۲2002-022 [ع. رزمه] (ا.) 
بوقچة رخت؛ بستهةٌ لباس. لنگٌ بار قماش و 
ائائه» بشتواره. 

رزسی: : -۲3201 (ص‌نس..) جنگجوی» 
جنگاور» حربی. 

رزن‌انس: 5 (.) طنین‌اندازی» 
انعکاس صوت و تموج آن. 

رره: (0-)۲:22 (.) حلقه مانندی است که 
مادگی چفت بر آن افتد و قفل رااز آن حلقه 
پا رژه رد کنند. 

رزیثه: ()ه۰7 [ع. رزيتة - رزیه] (.) 
=== part1 31275 ===
پرولتاریا: 2اه اه:مم (.) طبقهٌ کارگر که 
حبات تولیدی سر مابه‌داران نداست آنان 
است» طقه زحمتکش. 

پرونده. (6-)۳2۲۷۵۱02 [- بر ونده < بلو نده ] 
0( سته قماش و اسنابت» ستهٌ جامه» بشتوارة 
جامه» رزمه. پارچه‌ای که قماش را بدان 
ببچند» شلهٌ قماش» برونده. جوال مانندی که 
دهن آن از پهلوی آن باشد و استادان بزاز 
اساب دکان خود را در آن نهند و با 
رسمان‌ها نندند» بلونده. امروز پرونده را به 
مجموعةٌ سندها و نوشته‌های راجع به یکك 
تن یا یک موضوع يا یک کار که در یکث جا 
جمع آوری شده اطلاق کند (فره.) 
پرونده‌اش یش من است: از سوابق او کاملاً 
مطلع هستم. پرونده کردن جامه‌ها: بشتواره
```


## [2026-09-14T01:24:24.241Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2190,2250p' DOZ.txt; echo \"=== leaf ===\"; python3 -c \"\nt=open('DOZ.txt',encoding='utf-8',errors='replace').read()\ni=t.find('rizmay bg Freytag')\nprint('leaf0',t[:i].count('\\f'))\""
}
```


## [2026-09-14T01:24:25.249Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 19185 25222 26297; do echo \"--- $L ---\"; sed -n \"${L},$((L+12))p\" BQT_v1_pages.txt; done"
}
```


### [2026-09-14T01:24:25.377Z] TOOL RESULT

```
worden, dan tot nu toe geschied is.
Het Arab. wortelwerkwoord razama (in den eersten
en in den tweeden vorm) wordt van kleederen of stoffen
gebruikt, die te samen in één kleed of in één stuk
stof worden gebonden ^). Hiervan komt het substantief
rizmay bg Freytag een bundel kleederen; het beduidt
ook baal; zoo 1001 Nacht ^ II, p. 116ed. Macnaghten:
„Kom met mij naar mijn schip, dan zal ik u den prijs
geven, benevens eene rizma Angora- wol, eene rizma
satgn, eene rizma fluweel en eene rizma laken." Dit
is de oorspronkelgke beteekenis van 't woord, dieeven-
wel uitgebreid is, zoodat het in 't algemeen j^aA, bundel
beduidt. Zoo wordt het gebruikt van een bundel zwee-
pen of karwatsen (Zamachsjari), van een pak borst-
hamassen (oud vers bg denzelfden). Bg Marcel, bij
Roland de Bussy {Uidióme d'Alger, p. 433) en in den
Dictionnaire berbère is het paquet (in den laatsten
met de uitspraak rezma). In de levensbeschrgving van
Hasan Gabartl, den vader, leest men, volgens de ver-
taling van Dorn (Drei arab. astronom. Instrumente,
p. 97): „Sein Diener hatte ein grosses Bundel, rizma,
aus welchem er das erwahnte Exemplar der astronomi-
schen Tafeln herausnahm." In een eenigszins gewgzig-
den zin is rizma, samengetrokken rima, in het Sp.
en Port. overgegaan; rima wordt door Victor aldus
verklaard: un tas, amas, monceau, comme de hardes.
^) Zamachsjari, Jsds al-baldga (HS.): 'indaho rizmaton minat-tliij
wahija ma sjodda minhd, fi thaubiu w4hidin.74
d'habits et de matelats Tun sur Tautre; van dBaxrimero
in denzelfden zin. Het Arab. rizma is bij Bocthor ook
paquet enveloppé dans du papier; — paquet, lettres
sous enveloppe. In het bgzonder is het een baal papier^
een riem; Pedro de Alcala heeft het (zooals reeds door
Engelmann is opgemerkt) onder rezma de papel; het
staat ook onder rame (de papier) bij Bocthor en bg
Berggren. In de Arabische boedellijst van een Marok-
kaanschen Jood; die in 1751 overleden is, lees ik
(HS. 1376): „Van Hollandsch papier zes rizma's."
Men ziet dus, dat de beteekenis van 't Arab. woord
vaststaat; Diez kende ze niet, doordien zgne kennis
van 't Arab. zich bepaalt tot datgene, wat hg in Freytag
vinden kan, en deze de bedoelde beteekenis niet heeft.
Het is in 't algemeen hoogst gevaarlgk, alleen op zulk
een onvolledig Lexicon, als dat van Freytag is, af te
gaan; daardoor is Diez meestal ongelukkig geweest,
als hg met het Arab. in aanraking kwam.
Den vorm rezma (zooals de Dict. berb. heeft) vindt
men in 't Sp., rezma (Alcala, Victor, Cobarruvias, die
ook reeds wist, dat het woord Arab. is), of, zooals
men tegenwoordig minder goed schrgft, resma (zoo
ook Port.); den vorm reismo vind ik bg Yanguas,
Dicc. de antig. del Reyno de Navarra, III, p. 13,
in een stuk van 1397. De vorm rizma is in 't Ital.
risma, en dit is in de Noordsche talen overgegaan, óf
met wegwerping der laatste syllabe, Duitsch RiesSj
Deensch Riisy Zweedsch m, óf samengetrokken rism^
rim (Kiliaan geeft als Latgn rismusy rimus\ ons nem,
Eng. ream. Het Fr. rame is ontstaan vXirasme, razme^75
razma; razma wordt in 't Arab. met dezelfde vokaal
(de fatha) geschreven als rezma^ en de uitspraak hangt
van willekeur of van het dialect af.
=== leaf ===
leaf0 84
```


### [2026-09-14T01:24:26.469Z] TOOL RESULT

```
--- 19185 ---
بلغت زند و پازند (۱) کوسفندی و بزیساگوند
که پیشاپیش کله راه رود - و بز کوهی را نیز
گفته‌اند ۴
بر ون آ مدن - کنابه از ترك اطاعت
و ایاد باشد .
رو فده <- بروزن شرمنده ۰ بمعنی‌سله
و سبد و بنهٌ قماش باشد و آنرا بعربی رزمه
خوانند .
برون‌سر اه زربرا کویند که در خیر
دارالضرب و ضرامخانه سکه کرده باشند .
برو وس با سین بی نقطه ونتطه‌دار
پروزن کلوسوز » لشکر و لشکربرا کویند - ونام
سرلشکری و سپهبدی حم بوده است ‏ .
--- 25222 ---
پر و ند ۲ بروزن فرزند ؛ نام مزرعه
ایست‌از مضافات قزوین؟ -و بمنی امر دهم آمده
ان که پسر مساده باشد . و ی یممنی امرود
نوشته اند که آن میوه ابست مشهور و هیچ بك
خاهدندار ند افه اعل؟ ۱
فر و ۵ ه بسکون تانی بر وزن‌ارژنده,
بته قماش واسباب را گویندوبعرمی رزمه‌خوانشد.
وبسنی لْفافةٌ ماش و اسباب را کفته الد نی
۱ ره : پروان .
۳
پارچه‌ای که قمای را بدان پیچند - وبسنی‌جوان
مانندی‌را کون دکه «هن آن از بهلوی آن باشد-
واستادان بزاز اسباب د کان خود را در آن هند
--- 26297 ---
است که فر دادن سمرب زبائی باشد .
پلو لك - بنتم اول و تانی بواو عجهول
رسیده و بکاف زده, غرفه و مخارجه و تالاری که
۳2 ی
ام راف زمن 2 1
پلو نده هبروزن شرمنده» بته قماش‌را
کومند وجربی رزمه خوانند .
یله بنتح اول و انی مخفف » بر وزن
ومعنی فله است که شیر حبوان نوزاییده باشد -
و نام درختی است خودرو که بر کش
آدمی و کلش بناخن شیر میماند » و بیخ آن
۹ سیاه و ب رکه آن تارنجی میشود ؛ و در
جنگلهای هندوستان بیار است- وبیعنی بناعت
```


## [2026-09-14T01:24:41.441Z] TOOL CALL #23: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-14T01:24:41.647Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-14T01:24:43.566Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['و آنرا بعربی رزمه','واسباب را گویندوبعرمی رزمه','کومند وجربی رزمه']:\n    i=t.find(pat)\n    print(pat[:20], 'leaf0=', t[:i].count('\\f') if i>0 else None)\nEOF"
}
```


### [2026-09-14T01:24:44.713Z] TOOL RESULT

```
و آنرا بعربی رزمه leaf0= 488
واسباب را گویندوبعرم leaf0= 618
کومند وجربی رزمه leaf0= 643
```


## [2026-09-14T01:24:51.287Z] TOOL CALL #25: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/ream\" \"https://www.etymonline.com/word/ream\" \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85%D8%A9\" \"https://en.wiktionary.org/wiki/resma\" \"https://en.wiktionary.org/wiki/rame\" \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85%D9%87\" \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85\" ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 427, root Arabic R.z.m -> rizma/resma/rame/ream: checking the chain\" ; done"
}
```


### [2026-09-14T01:24:58.120Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/ream
/home/sfmqrb/git/rishe/data/verification/sources/web/a76d157980732e33.txt
### https://www.etymonline.com/word/ream
/home/sfmqrb/git/rishe/data/verification/sources/web/3a4e19820a7d8032.txt
### https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85%D8%A9
/home/sfmqrb/git/rishe/data/verification/sources/web/b0b1f5ade6d1eb31.txt
### https://en.wiktionary.org/wiki/resma
/home/sfmqrb/git/rishe/data/verification/sources/web/1cfaa800fb202edc.txt
### https://en.wiktionary.org/wiki/rame
/home/sfmqrb/git/rishe/data/verification/sources/web/446ccf9736fe0a23.txt
### https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/e24984eaea931828.txt
### https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/72ca9f4c36216d04.txt
```


## [2026-09-14T01:25:00.657Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== WIKT ream ===\"; grep -n -i -A6 \"Etymology 1\\|Etymology 3\\|rizma\" a76d157980732e33.txt | head -60\necho; echo \"=== ETYMONLINE ream ===\"; grep -n -i -B2 -A8 \"rizma\\|resma\" 3a4e19820a7d8032.txt | head -40"
}
```


### [2026-09-14T01:25:00.734Z] TOOL RESULT

```
=== WIKT ream ===
65: Etymology 1 
66-
67- 1.2.1 
68- Alternative forms 
69-
70- 1.2.2 
71- Noun 
--
98: Etymology 3 
99-
100- 1.4.1 
101- Alternative forms 
102-
103- 1.4.2 
104- Noun 
--
305: Etymology 1
306- [ edit ] 
307-
308- From Middle English rem , reme , from Old English rēam ( “ cream ” ) , from Proto-West Germanic *raum , from Proto-Germanic *raumaz ( “ cream ” ) , from Proto-Indo-European *réwgʰmn̥ ( “ to sour [milk] ” ) .
309-
310- Cognate with Saterland Frisian Room ( “ cream ” ) , West Frisian rjemme ( “ cream ” ) , Dutch room ( “ cream ” ) , German Low German Rahm , Rohm ( “ cream ” ) , German Rahm ( “ cream ” ) , Swedish römme ( “ cream ” ) , Norwegian rømme ( “ sour cream ” ) , Faroese rómi ( “ cream ” ) , Icelandic rjómi ( “ cream ” ) . See also ramekin .
311-
--
446: Etymology 3
447- [ edit ] 
448-
449: From Middle English reme , from Old French raime , rayme ( “ ream ” ) (French rame ), from Catalan raima ( “ ream ” ) , from Arabic رِزْمَة ( rizma , “ bundle ” ) . 
450-
451- Alternative forms
452- [ edit ] 
453-
454- reme ( obsolete ) 
455-

=== ETYMONLINE ream ===
23- ream (n.1) 
24-
25: standard commercial measure of paper, rem , mid-14c., from Old French reyme , from Spanish resma , from Arabic rizmah "bundle" (of paper), from rasama "collect into a bundle." The Moors brought manufacture of cotton paper to Spain.
26-
27- The exact path of transmission of the word to English is unclear, and it might have entered from more than one language. An early variant rym (late 15c.) suggests a Dutch influence: compare Middle Dutch rieme , Dutch riem , which probably were borrowed from Spanish during the Hapsburg control of Holland. For ordinary writing paper, 20 quires of 24 sheets each, or 480 sheets; often 500 or more to allow for waste; the count varies slightly for drawing or printing paper.
28- also from mid-14c. 
29-
30- ream (v.) 
31-
32- "to enlarge a hole," especially "to widen or enlarge by the use of a rotary cutter," 1815, a word of "somewhat doubtful origin" [OED], but it is probably a southwest England dialectal survival from obsolete Middle English reme "to make room, open up, extend by stretching."
33-
```


## [2026-09-14T01:25:07.548Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== AR رزمة ===\"; sed -n '250,400p' b0b1f5ade6d1eb31.txt | grep -n -i -v '^\\s*$' | head -60\necho; echo \"=== resma ===\"; grep -n -i -B3 -A6 \"rizma\\|Arabic\" 1cfaa800fb202edc.txt | head -50"
}
```


### [2026-09-14T01:25:08.638Z] TOOL RESULT

```
=== AR رزمة ===
1: definite
3: construct
5: informal
7: رِزْمَتَيْن 
8: rizmatayn 
10: الرِّزْمَتَيْن 
11: ar-rizmatayn 
13: رِزْمَتَيْ 
14: rizmatay 
16: nominative
18: رِزْمَتَانِ 
19: rizmatāni 
21: الرِّزْمَتَانِ 
22: ar-rizmatāni 
24: رِزْمَتَا 
25: rizmatā 
27: accusative
29: رِزْمَتَيْنِ 
30: rizmatayni 
32: الرِّزْمَتَيْنِ 
33: ar-rizmatayni 
35: رِزْمَتَيْ 
36: rizmatay 
38: genitive
40: رِزْمَتَيْنِ 
41: rizmatayni 
43: الرِّزْمَتَيْنِ 
44: ar-rizmatayni 
46: رِزْمَتَيْ 
47: rizmatay 
49: plural
51: basic broken plural triptote ‎; 
52: sound feminine plural
54: indefinite
56: definite
58: construct
60: informal
62: رِزَم ‎; رِزْمَات 
63: rizam ‎; rizmāt 
65: الرِّزَم ‎; الرِّزْمَات 
66: ar-rizam ‎; ar-rizmāt 
68: رِزَم ‎; رِزْمَات 
69: rizam ‎; rizmāt 
71: nominative
73: رِزَمٌ ‎; رِزْمَاتٌ 
74: rizamun ‎; rizmātun 
76: الرِّزَمُ ‎; الرِّزْمَاتُ 
77: ar-rizamu ‎; ar-rizmātu 
79: رِزَمُ ‎; رِزْمَاتُ 
80: rizamu ‎; rizmātu 
82: accusative
84: رِزَمًا ‎; رِزْمَاتٍ 
85: rizaman ‎; rizmātin 
87: الرِّزَمَ ‎; الرِّزْمَاتِ 
88: ar-rizama ‎; ar-rizmāti 
90: رِزَمَ ‎; رِزْمَاتِ 
91: rizama ‎; rizmāti 
93: genitive
95: رِزَمٍ ‎; رِزْمَاتٍ 
96: rizamin ‎; rizmātin 

=== resma ===
175- Etymology
176- [ edit ] 
177-
178: Borrowed from Arabic رِزْمَة ( rizma ) . [ 1 ] [ 2 ] Compare Catalan raima and Spanish resma .
179-
180- Pronunciation
181- [ edit ] 
182-
183- ( Brazil ) IPA ( key ) : /ˈʁez.mɐ/ [ˈhez.mɐ] 
184-
--
223- Etymology
224- [ edit ] 
225-
226: Borrowed from Arabic رِزْمَة ( rizma ) .
227-
228- Pronunciation
229- [ edit ] 
230-
231- IPA ( key ) : /ˈresma/ [ˈrez.ma] 
232-
--
254-
255- Retrieved from " https://en.wiktionary.org/w/index.php?title=resma&oldid=92284978 "
256-
257: Categories : Portuguese terms derived from Arabic 
258: Portuguese terms borrowed from Arabic 
259- Portuguese 2-syllable words 
260- Portuguese terms with IPA pronunciation 
261- Rhymes:Portuguese/ezmɐ 
262- Rhymes:Portuguese/ezmɐ/2 syllables 
263- Rhymes:Portuguese/eʒmɐ 
264- Rhymes:Portuguese/eʒmɐ/2 syllables 
--
266- Portuguese nouns 
267- Portuguese countable nouns 
268- Portuguese feminine nouns 
269: Spanish terms borrowed from Arabic 
270: Spanish terms derived from Arabic 
271- Spanish 2-syllable words 
272- Spanish terms with IPA pronunciation 
273- Rhymes:Spanish/esma 
274- Rhymes:Spanish/esma/2 syllables 
275- Spanish lemmas 
276- Spanish nouns
```


## [2026-09-14T01:25:14.075Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== AR رزمة etymology/noun ===\"; grep -n -i -B2 -A8 \"Etymology\" b0b1f5ade6d1eb31.txt | head -40\necho \"--- descendants/root ---\"; grep -n -i -B2 -A10 \"Descendants\\|ر ز م\\|Root\" b0b1f5ade6d1eb31.txt | head -60\necho; echo \"=== PERSIAN رزمه ===\"; grep -n -i -B2 -A8 \"Persian\\|Etymology\" e24984eaea931828.txt | head -50"
}
```


### [2026-09-14T01:25:14.187Z] TOOL RESULT

```
=== AR رزمة etymology/noun ===
60-
61- 1.1 
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
69-
70- 1.1.2.1 
--
75-
76- 1.2 
77: Etymology 2 
78-
79- 1.2.1 
80- Pronunciation 
81-
82- 1.2.2 
83- Noun 
84-
85- 1.2.2.1 
--
154- [ edit ] 
155-
156: Etymology 1
157- [ edit ] 
158-
159- Root 
160-
161- ر ز م ( r z m ) 
162-
163- 1 term 
164-
--
371- → Italian: risma 
372-
373: Etymology 2
374- [ edit ] 
--- descendants/root ---
72-
73- 1.1.2.2 
74: Descendants 
75-
76- 1.2 
77- Etymology 2 
78-
79- 1.2.1 
80- Pronunciation 
81-
82- 1.2.2 
83- Noun 
84-
--
157- [ edit ] 
158-
159: Root 
160-
161: ر ز م ( r z m ) 
162-
163- 1 term 
164-
165- Pronunciation
166- [ edit ] 
167-
168- IPA ( key ) : /riz.ma/ 
169-
170- Noun
171- [ edit ] 
--
351- rizami ‎; rizmāti 
352-
353: Descendants
354- [ edit ] 
355-
356- Andalusian Arabic: رَزْمَة ( rázma ) 
357- → Catalan: raima 
358- → Old French: raime 
359- → French: rame 
360-
361- → Middle English: reme 
362- → English: ream 
363-
--
456- Retrieved from " https://en.wiktionary.org/w/index.php?title=رزمة&oldid=92479155 "
457-
458: Categories : Arabic terms belonging to the root ر ز م 
459- Arabic 2-syllable words 
460- Arabic terms with IPA pronunciation 
461- Arabic lemmas 
462- Arabic nouns 
463- Arabic feminine nouns 
464- ar:Networking 
465- ar:Software 
466- Arabic terms with collocations 
467- Arabic terms with quotations 
468- Arabic nouns with triptote singular in -a 

=== PERSIAN رزمه ===
```


## [2026-09-14T01:25:20.159Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '353,380p' b0b1f5ade6d1eb31.txt; echo \"=== رزمه page head ===\"; head -30 e24984eaea931828.txt; echo \"=== رزم verb ===\"; grep -n -i -B2 -A6 \"razama\\|to bundle\\|bundle\" 72ca9f4c36216d04.txt | head -40"
}
```


### [2026-09-14T01:25:20.271Z] TOOL RESULT

```
 Descendants
 [ edit ] 

 Andalusian Arabic: رَزْمَة ( rázma ) 
 → Catalan: raima 
 → Old French: raime 
 → French: rame 

 → Middle English: reme 
 → English: ream 

 → Portuguese: resma 

 → Spanish: resma 

 → Medieval Latin: rīsma 
 → German: Ries 

 → Italian: risma 

 Etymology 2
 [ edit ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ra.za.ma/ 

=== رزمه page head ===
URL: https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85%D9%87
FETCHED: 2026-09-14T01:24:57Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found=== رزم verb ===
```


## [2026-09-14T01:25:27.755Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -i -A4 \"Etymology\\|Verb\\|Root\" 72ca9f4c36216d04.txt | sed -n '1,60p'"
}
```


### [2026-09-14T01:25:27.818Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
144: Etymology
145- [ edit ] 
146-
147- From Middle Persian lcm ( razm ) . Akin to Old Armenian ռազմ ( ṙazm ) , an Iranian borrowing.
148-
```


## [2026-09-14T01:25:29.558Z] TOOL CALL #31: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=ream\" --note \"page 427: AHD:1086 s.v. ream (Arabic rizmah)\"; python3 tools/fetch_source.py \"https://dle.rae.es/resma\" --note \"page 427: DRAE resma < Ar. rizmah\""
}
```


### [2026-09-14T01:25:31.431Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f3f41d552be3e74d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f82e6a52fa2ca67.txt
```


## [2026-09-14T01:25:35.818Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== AHD ===\"; grep -n -i -B3 -A6 \"rizm\\|resma\\|ream\" f3f41d552be3e74d.txt | head -50; echo \"=== DRAE ===\"; grep -n -i -B3 -A6 \"rizma\\|Del ár\" 4f82e6a52fa2ca67.txt | head -30"
}
```


### [2026-09-14T01:25:35.940Z] TOOL RESULT

```
=== AHD ===
1:URL: https://www.ahdictionary.com/word/search.html?q=ream
2-FETCHED: 2026-09-14T01:25:30Z
3-STATUS: 200
4:TITLE: American Heritage Dictionary Entry: ream
5-
6:American Heritage Dictionary Entry: ream 
7-
8- HOW TO USE THE DICTIONARY
9- To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
10- Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
11- guide to the dictionary 
12-
--
38- INTERESTED IN DICTIONARIES?
39- Check out the Dictionary Society of North America at http://www.dictionarysociety.com 
40-
41: ream  1 (r ē m) 
42- Share: 
43-
44- Tweet 
45-
46: n. 1. A quantity of paper, formerly 480 sheets, now 500 sheets or, in a printer's ream, 516 sheets.
47: 2. often reams A very large amount: reams of work to do. 
48-
49: [Middle English rem , from Old French rayme, reme , ultimately (perhaps via Old Catalan raima , from Andalusian colloquial Arabic *razma ) from Arabic rizma , bundle, from razama , to bundle; see rzm in Semitic roots.]
50-
51- The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.
52-
53: ream  2 (r ē m) 
54- Share: 
55-
56- Tweet 
57-
58: tr.v. reamed , ream·ing , reams 1. To form, shape, taper, or enlarge (a hole or bore, for example) with a reamer or similar implement.
59- 2. To remove (material) by this process.
60: 3. To squeeze the juice out of (fruit) with a reamer.
61- 4. Vulgar Slang To penetrate sexually.
62-
63: Phrasal Verb: ream out To criticize or reprimand severely: reamed me out for being late. 
64-
65- [Possibly from Middle English remen , to make room, variant of rimen , from Old English r ȳ man ; see reu ə - in the Appendix of Indo-European roots .]
66-
67- The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.
68-
69- Indo-European & Semitic Roots Appendices
=== DRAE ===
60-
61- Definición
62-
63: Del ár. hisp. rízma, y este del ár. clás. rizmah 'paquete 1 '.
64- 1. f. Conjunto de 20 manos de papel .
65-
66- resma sucia
67- 1. f. resma de papel de hilo , que tiene sus dos costeras correspondientes .
68-
69- Palabra del día
```


## [2026-09-14T01:25:51.066Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT ream ===\"; grep -n -i \"^Ream\\|Ream\\b.*quires\\|rizma\" SKT.txt | head\necho \"=== AFA ===\"; grep -n -i \"rizma\\|razama\" AFA.txt | head\necho \"=== FVQ ===\"; grep -n -i \"rizma\\|razama\" FVQ.txt | head\necho \"=== AFM rizma ===\"; grep -n -i \"rizma\" AFM.txt AFM_alt.txt | head\necho \"=== HJB ===\"; grep -n -i \"rizma\\|resma\" HJB.txt | head\necho \"=== ARY رزمه ===\"; grep -n \"رزمه\" incoming/ARY/ARY_pages.txt 2>/dev/null | head"
}
```


### [2026-09-14T01:25:51.199Z] TOOL RESULT

```
=== SKT ream ===
=== AFA ===
=== FVQ ===
=== AFM rizma ===
=== HJB ===
=== ARY رزمه ===
```


## [2026-09-14T01:25:53.596Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"quires\" SKT.txt | head; echo ---; grep -n -i \"Ream\\.\" SKT.txt | head"
}
```


### [2026-09-14T01:25:53.693Z] TOOL RESULT

```
22214:the  lower  line  a  blank  will  be  observed  below  E. /.     It  is  usually  said  that  E.^ .')  SIct.  b,  but   there  is  no   proof  of  this;    and  my  own   impression  is  that  it (abnormally)  to  SkL/,  which  io  some  cases  did  aot  turn  into  £./   as  the law  requires.
---
1119:Auction-  (L.)  L.  auciifffifm,  ace.  of auctio,  a  sale  by  auction,  lit.  •  an  increase/ because  the  sale  is  to  the  highest  bidder.— L.  au£tus,  pp.  of  augert,  to  IncreaM.  See Ske.
2155:Bourn  (2),  Bum,  a  stream.  (E.)  M.  E. bounte.  A.  S.  buma,  a  fountain,  stream, well.  (VUHUR?)  +  Icel.  brunnr-.  Swed. brunrt',  Don.  brand;  G.  brunnen;  Goth. ^rw«wfl,a^iinp,  well;  cf.  Gk.f/)<op.  b  well.
2346:Stream.  (R.)    M.  £. <4-  Do.  jrvtfi.  G.  bru€M»  a flRAG)
5365:DREAM.
5400:und.  harmony;  al&o iciicc  'a  (ircain  of b^-,.  .  .  .,  |oy,  dicam  ;  Du. irttumr,  n.in.  ywcd.  <//v«,  G. led  to  Droio,  Drone. [>,  to  dream.  iE.>  A.  S.  rfr^- Ij  lormed  from  d*v4m.  sb.,  by lo/(u  qsoaIj.  +  G.  trdumeH.
7812:gurglo.  to  purl.  (ItaK  -L.)  In  Spenser. Theat^-lis,  3.     Imitated   from   Ital.  gor^o-^mm j^liari,   to   pari,    bubble,    boil ;    gor^mi^^^^^ gureUng  of  a  stream.  — Ital.  ^/y»,  a  whirl-^^^ pool.—X,  gurgtj,  whirlpool;  cT.  ^rgulit gullet
8564:hemorrhoido.  emerods.  fmii.ful bleeding  tubercles  on  the  ajius.  (F.— L,— Ck.)  F.  hetHorrhoiJi,  sing.,  a  flowing  of blood.  -•  L.  hamorrhouUs,  pi.  of  hamor- rkois.  «  Gk.  tu>opy)o^d«f,  pi.  of  ai/ui/woir. adj.,  liable  to  a  fluw  of  blood. —Gk.  oI>»o-, put  for  a/^a,  blood  ;  ^<tf ,  to  flow,  cognate with  Skt.  srm,  to  flow  ;  see  Stream.
15703:Beam  ^F.  -  Span.  -  Arab.)  M.  E. reeme.  —  O,  F.  raime  ( F.  rame)^  a  ream  01 hundte  of  pajwr.  —  .Span,  rejma,  a  ream.» Arab,  rismat  (pi.  riiam),  a  bundle.
16100:Bill,  a  streamlet  (O.  Low  G.)  Prob. from  O.  Low  <;.  rilUt  E.  Friesic  ri/le,  a Btreamlet.  Apparcully  for  ^ridtU,  ^rithtlc ; cfl  A.S.  rite^  a  stream;  Low  G.  rri/r,  a stream.
16154:derive.  (F.  -  L.)  O.  F.  Antvr,  to derive,  also  to  drain.  ••  L.  dtriuare,  to drain  off  water.  ••  L.  dk,  from ;  Hum,  a stream.
```


## [2026-09-14T01:26:02.528Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('M.  E. reeme')\nprint('SKT leaf0',t[:i].count('\\f'),'=> printed ~', t[:i].count('\\f')-20)\n\" ; echo \"--- MON markers? ---\"; grep -c $'\\f' MON_part1.txt; grep -n -m3 \"^[۰-۹0-9]\\{3,4\\}$\" MON_part1.txt | head"
}
```


### [2026-09-14T01:26:03.647Z] TOOL RESULT

```
SKT leaf0 419 => printed ~ 399
--- MON markers? ---
0
```


## [2026-09-14T01:26:05.381Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B1%D8%B2%D9%85%D9%87/\" --note \"page 427: Mo'in/Dehkhoda entry for Persian رزمه (MON:1649)\" && grep -n -i -B2 -A6 \"رزمه\" data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://abadis.ir/fatofa/%D8%B1%D8%B2%D9%85%D9%87/'.encode()).hexdigest()[:16])\").txt | head -40"
}
```


### [2026-09-14T01:26:07.873Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/058cb6a3351c3db1.txt
2-FETCHED: 2026-09-14T01:26:07Z
3-STATUS: 200
4:TITLE: رزمه - معنی در دیکشنری آبادیس
5-
6:رزمه - معنی در دیکشنری آبادیس 
7-
8- دیکشنری مترجم بپرس 
9-
10: رزمه
11-
12- معنی انگلیسی : parcel , duffel bag , duffle bag 
13-
14- دنبال کنید 
15-
16- لغت نامه دهخدا
--
19- رزمة. [ رَ م َ ] ( ع مص ) سرد گردیدن زمستان : رزم الشتاء رزمة. ( ناظم الاطباء ) ( منتهی الارب ) ( از آنندراج ) ( از اقرب الموارد ). || بر جای ماندن مرداز بیماری : رُزِم َ الرجل ( مجهولاً ). ( منتهی الارب ).
20- رزمة. [ رَ زَ م َ ] ( ع اِ ) آواز شتر ماده. ( دهار ). آوازه ماده شتر از حلق در پیش بچه خود مانند ناله بدون آنکه دهان را گشاید و آن از حنین آهسته تر است. و در مثل : لا خیر فی رزمة لا درة فیها؛ در حق کسی گویند که وعده کند و بجای نیاورد. ( ناظم الاطباء ) ( منتهی الارب ) ( آنندراج ) ( از اقرب الموارد ). || رزمةالسباع ؛ آواز ددان. ( ناظم الاطباء ) ( منتهی الارب ). || آواز رعد. ( دهار ). || آواز کودک. ( از اقرب الموارد ).
21: رزمة. [ رِ م َ ] ( ع اِ ) رَزْمة. پشتواره جامه. ( ناظم الاطباء ) ( منتهی الارب ) ( آنندراج ). آنچه در یک جامه استوار و فراهم کرده شود. ( از اقرب الموارد ). || ضرب شدید. ج ، رَزَم ،رَزِم. ( آنندراج ) ( از منتهی الارب ) ( ناظم الاطباء ). رزمه. [ رَ م َ / م ِ ] ( از ع ، اِ ) رزمة. بقچه بزرگ. ( فرهنگ خطی ). بوقچه ٔرخت. ( ناظم الاطباء ) ( لغت محلی شوشتر نسخه خطی کتابخانه مؤلف ) ( غیاث اللغات ) ( از برهان ). بسته قماش.( آنندراج ) ( از شعوری ج 2 ص 15 ). بقچه. ( یادداشت مؤلف ). بَلْغُنْده. ( دهار ) ( یادداشت مؤلف ) : 
22-زایر کز آنجا بازگردد برد
23:دیبا به تخت و رزمه و زر به من. فرخی.
24-با جامه زری زرد چون شنبلید بیشتر بخوانید ... 
25-
26- فرهنگ فارسی
27-
28- بقچه لباس، بسته رخت، پشتواره جامه، لنگه بارقماش
29:( اسم ) ۱ - بوقچه رخت بسته لباس . ۲ - لنگه بار قماش و اثاثه پشتواره . یا روی رزمه اصطلاحی است که در مورد تفوق و رجحان کسی بر دیگری استعمال شود ( نسائم الاسحار ۱۸۳ ببعد ) .
30-پشتواره جامه آنچه در یک جامه استوار و فراهم کرده شود یا ضرب شدید. 
31-
32- فرهنگ معین
33-
34- (رَ مِ ) [ ع . رزمة ] (اِ. ) بقچة لباس . 
35-
--
44-پیراهن
45-رومی و زنگیش چو صبح دو رنگ
46:رزمه روم داد و بزمه زنگ
47-✏ �نظامی�
48-
49- + عکس و لینک
```


## [2026-09-14T01:26:15.326Z] TOOL CALL #37: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-14T01:26:15.374Z] TOOL RESULT

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


## [2026-09-14T01:26:16.853Z] TOOL CALL #38: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-14T01:26:16.903Z] TOOL RESULT

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


## [2026-09-14T01:26:44.899Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN ===\"; grep -n -i \"rizma\\|rezma\\|razme\" HRN.txt | head\necho \"=== HUB ===\"; grep -n -i \"rizma\\|rezma\" HUB.txt | head\necho \"=== FSD3 markers near ===\"; python3 - <<'EOF'\nimport re\nt=open('FSD_vol3.txt',encoding='utf-8',errors='replace').read()\nj=t.find('< Rp resma')\nseg=t[max(0,j-60000):j+20000]\nprint(sorted(set(m.group().strip() for m in re.finditer(r'^\\s*2[01]\\d\\d\\s*$',seg,re.M))))\nEOF"
}
```


### [2026-09-14T01:26:46.134Z] TOOL RESULT

```
=== HRN ===
7869:arm. LW. gerezman 'Grab' Gruft, Friedhof dazu stellt).
22229:I gerezman 906l>'«'.
=== HUB ===
3258:gerezman 'Grab* nichts zu thun. Vgl. Fr. Muller,
=== FSD3 markers near ===
[]
```


## [2026-09-14T01:29:58.892Z] TOOL CALL #40: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-427.json",
 "content": "{\n  \"pdf_page\": 427,\n  \"book_page\": 397,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"R.z.m\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic triliteral root ر-ز-م (r-z-m), verb رَزَمَ razama 'to tie up in a bundle, wrap (clothes) together in one cloth'\",\n      \"note\": \"The root box is right: this is a genuine Semitic/Arabic triliteral root, not a Persian or Indo-European one. Note that it is NOT the same word as Persian رزم razm 'battle' (< Middle Persian razm, whence Old Armenian ṙazm), which is an Iranian homonym; Nourai correctly keeps them apart. AHD5 s.v. ream: 'from Arabic rizma, bundle, from razama, to bundle; see rzm in Semitic roots'; Etymonline s.v. ream (n.1): 'from Arabic rizmah \\\"bundle\\\" (of paper), from rasama [sic, read razama] \\\"collect into a bundle\\\"'. Dozy, Oosterlingen (leaf 84 ≈ pp. 73–75), devotes two pages to the root: 'Het Arab. wortelwerkwoord razama (in den eersten en in den tweeden vorm) wordt van kleederen of stoffen gebruikt, die te samen in één kleed of in één stuk stof worden gebonden'. Wiktionary files رِزْمَة under 'Arabic terms belonging to the root ر ز م'. The whole chart (Arabic rizma → Persian رزمه; Arabic rizma → Sp. resma → OFr. rayme → Eng. ream) is the standard textbook etymology of 'ream'; the only point on which modern scholarship differs from Nourai is whether the Romance intermediary that gave French rame was Castilian resma or Old Catalan raima.\",\n      \"note_fa\": \"ریشهٔ سه‌واکی عربی «ر-ز-م» (فعل رَزَمَ «بستن و در یک جامه پیچیدن») ریشه‌ای سامی و اصیل است و ادعای نورایی دربارهٔ آن درست است. باید توجه داشت که این واژه هیچ پیوندی با «رزم» فارسی به معنی «جنگ» ندارد؛ آن یکی از فارسی میانهٔ razm می‌آید و هم‌ریشه با رازم ارمنی است، و نورایی نیز آن دو را درست از هم جدا کرده است. فرهنگ AHD و اتیمانلاین و دوزی (در Oosterlingen) همگی رِزمهٔ عربی را برساختهٔ همین ریشه می‌دانند. کل زنجیرهٔ نمودار — عربی rizma ← فارسی «رزمه»، و عربی rizma ← اسپانیایی resma ← فرانسهٔ کهن rayme ← انگلیسی ream — ریشه‌شناسی پذیرفته‌شدهٔ امروزی است؛ تنها اختلاف بر سر آن است که واسطهٔ رومیاییِ واژهٔ فرانسوی، اسپانیاییِ قشتالی بوده است یا کاتالانیِ کهن.\",\n      \"sources\": [\n        \"https://www.ahdictionary.com/word/search.html?q=ream\",\n        \"https://www.etymonline.com/word/ream\",\n        \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85%D8%A9\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"FVA:161\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989) — refs_online.json records that no digital copy exists on any permitted platform (re-searched 2026-09); only the OpenLibrary catalogue record (OL2012991M) is available, so p. 161 cannot be read.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"online 5th ed., s.v. ream¹ (= the main-body entry Nourai cites as AHD:1086)\", \"stance\": \"supports\", \"note\": \"'[Middle English rem, from Old French rayme, reme, ultimately (perhaps via Old Catalan raima, from Andalusian colloquial Arabic *razma) from Arabic rizma, bundle, from razama, to bundle; see rzm in Semitic roots.]' — the root, its gloss and the Arabic derivative are exactly Nourai's.\"},\n        {\"src\": \"DOZ\", \"where\": \"Oosterlingen, form-feed leaf 84 (printed ≈ pp. 73–75), s.v. Riem\", \"stance\": \"supports\", \"note\": \"'Het Arab. wortelwerkwoord razama (in den eersten en in den tweeden vorm) wordt van kleederen of stoffen gebruikt, die te samen in één kleed of in één stuk stof worden gebonden. Hiervan komt het substantief rizma, bij Freytag een bundel kleederen' (grep -n 'rizmay bg Freytag' DOZ.txt).\"},\n        {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1723 (form-feed leaf 165 ≈ printed p. 139)\", \"stance\": \"supports\", \"note\": \"'1723. Ar. rizma: \\\"Bündel oder Pack Kleider, Papierstoß\\\"' — Lokotsch treats rizma as Arabic, with no foreign source.\"},\n        {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (PLA_asbaghi_1988_ia_djvu.txt, PLA_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'rizma' finds nothing: Asbaghi does not list rizma among the Persian loans in Arabic, i.e. no support for a reverse (Persian → Arabic) origin of the root.\"},\n        {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'rizma|razama' finds nothing — Fraenkel does not claim an Aramaic source for the root either.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"rezmeh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic رِزْمَة rizma(h) is the regular fiʿla-type nomen vicis/nomen rei built on the root r-z-m: from the verb رَزَمَ razama 'to tie (clothes, cloth) up together in one wrapper' comes the noun 'that which is bound up in one cloth' = 'bundle, bale, packet', pl. رِزَم rizam. Lane's and Freytag's sources, quoted by Dozy, show it used of a bundle of clothes (Zamakhsharī, Asās al-balāgha: 'ʿindahu rizmatun min al-thiyāb, wa-hiya mā shudda minhā fī thawbin wāḥidin'), of bales of Angora wool, satin, velvet and cloth in the 1001 Nights (ed. Macnaghten II 116), and from the paper trade of the ʿAbbāsid and Andalusi periods onwards specifically of a bale/ream of paper (Bocthor: 'paquet enveloppé dans du papier'). Nourai's transliteration 'rezmeh' is the Persian-style reading of the Arabic word (Classical rizma, Maghribi/dialectal rezma — Dozy notes the Dictionnaire berbère spelling 'rezma'), not a separate form. The node is exactly right.\",\n          \"derivation_fa\": \"«رِزمة» عربی (rizma) اسمی است بر وزن فِعْلَة از ریشهٔ ر-ز-م و از فعل رَزَمَ «بستن و در یک جامه پیچیدن» ساخته شده است؛ معنای آن «آنچه در یک جامه بسته و فراهم شود» یعنی «بقچه، بسته، لنگهٔ بار» است و جمع آن رِزَم می‌آید. زمخشری در اساس البلاغة می‌نویسد «عنده رزمةٌ من الثیاب، و هی ما شُدَّ منها فی ثوبٍ واحدٍ»، و از دورهٔ رونق کاغذسازی در بغداد و اندلس به بعد این واژه به معنی «بستهٔ کاغذ» نیز به کار رفته است. آوانگاشت نورایی «rezmeh» تلفظ فارسی‌شدهٔ همان واژه است، نه صورتی جداگانه (دوزی صورت گویشی rezma را از فرهنگ بربری نقل می‌کند). ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85%D8%A9\",\n            \"https://www.ahdictionary.com/word/search.html?q=ream\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:161\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vazheha-ye Arabi dar Farsi has no digital copy (refs_online.json: 'Searched archive.org, ketabnak, noorlib, web: no digital copy found'), so p. 161 could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. ream (KLN_1966.txt leaf 696; the printed running numeral '1307' stands a few lines above the entry)\", \"stance\": \"supports\", \"note\": \"'ream, n., 20 quires of paper. — ME. reme, fr. OF. rayme (F. rame), fr. Sp. resma, fr. Arab. rizmah, \\\"bundle, bundle of paper\\\".'\"},\n            {\"src\": \"DOZ\", \"where\": \"Oosterlingen leaf 84 (≈ pp. 73–75)\", \"stance\": \"supports\", \"note\": \"'Het Arab. rizma is bij Bocthor ook paquet enveloppé dans du papier … In het bijzonder is het een baal papier, een riem'; and the semantic history 'Dit is de oorspronkelijke beteekenis van 't woord, die evenwel uitgebreid is, zoodat het in 't algemeen bundel beduidt.'\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1723 (leaf 165 ≈ p. 139)\", \"stance\": \"supports\", \"note\": \"'Ar. rizma: \\\"Bündel oder Pack Kleider, Papierstoß\\\"; hieraus it. risma \\\"ein Ries Papier\\\", sp. pg. resma, razma, kat. raima, frz. rame; engl. ream, ndl. riem, dtsch. Ries … dän. riis, schwed. ris.'\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-Farisiyya al-Muʿarraba (AFM.txt, AFM_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'رزمة' and 'rizma' return nothing — Addi Shir does not list rizma among the Persian words arabicised, confirming it is treated as native Arabic.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an (FVQ.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'rizma|razama' finds nothing; the word is not Qurʾānic and Jeffery has no foreign-origin claim for it.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"rezmeh «رزمه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian رزمه razme/rezme 'bundle of clothes, bale of cloth' is a straightforward Arabic loan of رِزْمَة rizma, taken over with the usual Persian treatment of the Arabic tāʾ marbūṭa as -a/-e (ه). Mo'in tags the entry '[ع. رزمة]' (i.e. 'Arabic رزمة') and glosses it 'بقچهٔ لباس' ('bundle of clothes'); Dehkhoda gives 'رزمه [رَ مَ / مِ] (از ع، اِ) رزمة. بقچه بزرگ … بقچهٔ رخت … بستهٔ قماش'. It is old in New Persian: Dehkhoda cites Farrokhi Sistani (d. c. 1037) 'زایر کز آنجا بازگردد برد / دیبا به تخت و رزمه و زر به من', and Nizami 'رزمه روم داد و بزمه زنگ'. Borhan-e Qateʿ confirms Persian speakers' own sense of the word's foreignness: s.v. پرونده/پلونده it defines the native word as 'بستهٔ قماش و اسباب' and adds 'و آن را به عربی رزمه خوانند' ('and in Arabic it is called rezma'). Nourai's script, gloss and direction of borrowing are all correct; this is not a Persian→Arabic round-trip.\",\n          \"derivation_fa\": \"«رزمه» در فارسی وام‌واژه‌ای است از «رِزمة» عربی، با تبدیل معمول تاء مربوطهٔ عربی به «ـه» فارسی. معین در فرهنگ خود آن را با نشان «[ع. رزمة]» آورده و «بقچهٔ لباس» معنی کرده است، و دهخدا می‌نویسد «رزمه [رَ مَ / مِ] (از ع، اِ) رزمة. بقچهٔ بزرگ … بقچهٔ رخت … بستهٔ قماش». این واژه در فارسی دری کهن است؛ دهخدا بیت فرخی سیستانی «زایر کز آنجا بازگردد برد / دیبا به تخت و رزمه و زر به من» و بیت نظامی «رزمه روم داد و بزمه زنگ» را شاهد آورده است. برهان قاطع نیز ذیل «پرونده/پلونده» می‌نویسد «بستهٔ قماش و اسباب را گویند و آن را به عربی رزمه خوانند»، که نشان می‌دهد خودِ فارسی‌زبانان آن را واژه‌ای عربی می‌دانسته‌اند. پس جهت وام‌گیری در نمودار نورایی درست است و این واژه وام‌گیری دوسویه (فارسی ← عربی ← فارسی) نیست.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D8%B1%D8%B2%D9%85%D9%87/\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85%D8%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:161\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi 1368/1989 exists (refs_online.json).\"},\n            {\"ref\": \"MON:1649\", \"status\": \"supports\", \"note\": \"Mo'in's entry located in MON_part1.txt line 67171 (OCR 'ررمه' for رزمه): 'رزمه: [ع. رزمه] (ا.) بقچهٔ رخت؛ بستهٔ لباس. لنگِ بار قماش و اثاثه، پشتواره' — Mo'in marks it Arabic, exactly the arrow Nourai draws. The same text is reproduced under 'فرهنگ معین' at abadis.ir: '(رَ مِ) [ع. رزمة] (اِ.) بقچة لباس'. The printed page number 1649 could not be confirmed: the local MON OCR has no page markers (grep -c '\\\\f' MON_part1.txt = 0) and vajehyab/abadis do not print pagination; but ر falls in Mo'in vol. 2, where p. 1649 is the right region.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. رزمه (MON_part1.txt line 67171)\", \"stance\": \"supports\", \"note\": \"'[ع. رزمه] (ا.) بقچة رخت؛ بستة لباس. لنگ بار قماش و اثاثه، پشتواره.'\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ, BQT_v1_pages.txt leaves 488, 618 and 643 (s.v. پرونده and پلونده, printed pp. ≈ 270, 395, 418)\", \"stance\": \"supports\", \"note\": \"'پرونده … بمعنی سله و سبد و بنهٔ قماش باشد و آن را بعربی رزمه خوانند' (leaf 488); 'پرونده … بستهٔ قماش و اسباب را گویند و بعربی رزمه خوانند' (leaf 618); 'پلونده … بستهٔ قماش را گویند و بعربی رزمه خوانند' (leaf 643). Borhan has no independent Persian etymology for رزمه and explicitly calls it the Arabic equivalent.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie (HRN.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'rizma|rezma|razme' returns only 'gerezman' (Armenian, no. 906) — Horn does not treat رزمه, as expected for a book that excludes Arabic loans.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'rizma|rezma' returns only the unrelated Armenian 'gerezman'; Hübschmann has no entry, again consistent with an Arabic loan rather than an inherited Iranian word.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi (ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'رزمه' finds nothing — Aryanpur lists only inherited Indo-European vocabulary, so the absence of رزمه is a (weak) confirmation that it is not Iranian.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Spanish\",\n          \"words\": \"resma\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Spanish resma 'ream (of paper)' is a direct Andalusi-Arabic loan: Andalusi rízma/rázma (< Classical rizma) gave Old Spanish rezma, later spelled resma with the ordinary Castilian devoicing/graphic shift of intervocalic -z- before a consonant. The Real Academia's DLE states it plainly: 'Del ár. hisp. rízma, y este del ár. clás. rizmah \\\"paquete\\\"'; Wiktionary likewise: 'Borrowed from Arabic رِزْمَة (rizma)'. The route is a concrete historical one — as Etymonline notes, 'The Moors brought manufacture of cotton paper to Spain' (Játiva/Xàtiva was the great Islamic paper mill of al-Andalus from the 11th c.), so the trade term travelled with the commodity. Dozy documents the earliest Iberian attestations: 'rezma (Alcalá, Victor, Cobarruvias, die ook reeds wist, dat het woord Arab. is)', with the variant reismo in a Navarrese document of 1397. Nourai's arrow (Arabic → Spanish) is exactly right; only its continuation to French is debated (see node #4).\",\n          \"derivation_fa\": \"resma اسپانیایی «رِیم کاغذ» وام‌واژه‌ای مستقیم از عربیِ اندلسی rízma/rázma (از رِزمهٔ فصیح) است؛ صورت کهن‌تر اسپانیایی rezma بوده که بعدها به resma نوشته شده است. فرهنگستان زبان اسپانیا (DLE) می‌نویسد «Del ár. hisp. rízma, y este del ár. clás. rizmah» و ویکی‌واژه نیز آن را وام از «رِزمة» می‌داند. مسیر وام‌گیری مسیری تاریخی و ملموس است: مسلمانان صنعت کاغذسازی را به اندلس بردند (کارگاه‌های شاطبه از سدهٔ پنجم هجری) و اصطلاح بازرگانی «رزمه» همراه خود کالا به اسپانیایی رفت. دوزی کهن‌ترین شواهد را نقل می‌کند و صورت reismo را در سندی از سال ۱۳۹۷ میلادی در ناوار یافته است. پس این گره از نمودار نورایی تأیید می‌شود.\",\n          \"sources\": [\n            \"https://dle.rae.es/resma\",\n            \"https://en.wiktionary.org/wiki/resma\",\n            \"https://www.etymonline.com/word/ream\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1307\", \"status\": \"supports\", \"note\": \"Klein 1966 (KLN_1966.txt form-feed leaf 696; the printed running numeral '1307' occurs 5,851 characters before the entry, i.e. on the same/opposite page of the same leaf): 'ream, n., 20 quires of paper. — ME. reme, fr. OF. rayme (F. rame), fr. Sp. resma, fr. Arab. rizmah, \\\"bundle, bundle of paper\\\".' The page number checks out.\"},\n            {\"ref\": \"FSD:2060\", \"status\": \"supports\", \"note\": \"Funk & Wagnalls New Standard, vol. 3 (FSD_vol3.txt, form-feed leaf 602), s.v. ream⁴: 'Twenty quires of paper, properly, 480 sheets (a short ream), but often 500 sheets or more (a long r.). [< F rame, < Sp resma, < Ar rizma, bundle of paper]'. The recorded vol.-3 offset (printed = leaf + 1466) puts it at p. ≈ 2068 rather than 2060; no printed numeral survives in the OCR near the entry, so the 8-page difference is most likely scan-offset drift, and the content is exactly what Nourai cites it for.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, leaf 696 (p. 1307/1308), s.v. ream\", \"stance\": \"supports\", \"note\": \"'fr. Sp. resma, fr. Arab. rizmah'.\"},\n            {\"src\": \"DOZ\", \"where\": \"Oosterlingen, leaf 84 (≈ p. 74)\", \"stance\": \"supports\", \"note\": \"'Den vorm rezma (zooals de Dict. berb. heeft) vindt men in 't Sp., rezma (Alcala, Victor, Cobarruvias, die ook reeds wist, dat het woord Arab. is), of, zooals men tegenwoordig minder goed schrijft, resma (zoo ook Port.); den vorm reismo vind ik bij Yanguas … in een stuk van 1397.'\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1723 (leaf 165 ≈ p. 139)\", \"stance\": \"supports\", \"note\": \"'hieraus … sp. pg. resma, razma, kat. raima' — Lokotsch derives Spanish resma straight from Arabic rizma, as Nourai does.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., form-feed leaf 419 (≈ printed p. 399), s.v. Ream (OCR reads 'Beam')\", \"stance\": \"supports\", \"note\": \"'Ream (F. – Span. – Arab.) M.E. reeme. – O.F. raime (F. rame), a ream or bundle of paper. – Span. resma, a ream. – Arab. rizmat (pl. rizam), a bundle.'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"rame, rayme\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Old French rayme/raime (modern French rame 'ream of paper', a paper-trade term distinct from the homonyms rame 'oar' < Lat. remus and rame 'branch' < ramus) certainly goes back to Arabic rizma; what is debated is the Romance intermediary. Nourai follows the older school — Klein ('OF. rayme (F. rame), fr. Sp. resma'), Skeat, Lammens, Devic and Dozy — for whom the French word comes from Ibero-Romance resma/rezma with loss of the sibilant: Dozy, 'Het Fr. rame is ontstaan uit rasme, razme, razma', and Devic, 'Rizma est devenu par la chute du z (comme dans rayme, rame) …'. Modern lexicography prefers a Catalan link: AHD5 has 'from Old French rayme, reme, ultimately (perhaps via Old Catalan raima, from Andalusian colloquial Arabic *razma) from Arabic rizma', and Wiktionary routes Andalusi rázma → Catalan raima → Old French raime → French rame, since Catalan raima explains the diphthong -ai-/-ay- of the oldest French spellings better than Castilian resma does. Both routes start from the same Arabic word and run through Iberia in the same period (the paper trade, 13th–14th c.), so the node is substantially right but the specific Spanish→French arrow is one of two competing reconstructions.\",\n          \"derivation_fa\": \"rayme/raime در فرانسهٔ کهن (rame در فرانسهٔ امروز، به معنی «رزمهٔ کاغذ» و جدا از هم‌آواهای rame «پارو» و rame «شاخه») بی‌گمان به «رِزمة» عربی بازمی‌گردد، ولی بر سر واسطهٔ رومیایی آن اختلاف هست. نورایی از مکتب کهن‌تر پیروی می‌کند — کلاین، اسکیت، لامنس، دویک و دوزی — که واژهٔ فرانسوی را از resma/rezma اسپانیایی با افتادن «ز» می‌دانند؛ دوزی می‌نویسد «Het Fr. rame is ontstaan uit rasme, razme, razma» و دویک «Rizma est devenu par la chute du z (comme dans rayme, rame)». اما فرهنگ‌های امروزی واسطهٔ کاتالانی را ترجیح می‌دهند: AHD می‌نویسد «شاید از راه کاتالانیِ کهن raima، از عربیِ عامیانهٔ اندلسی razma*»، و ویکی‌واژه نیز همین مسیر را می‌آورد، زیرا raima کاتالانی دوواکهٔ ـai/ـay در کهن‌ترین املاهای فرانسوی را بهتر توضیح می‌دهد. هر دو مسیر از یک واژهٔ عربی و از راه شبه‌جزیرهٔ ایبری و تجارت کاغذ (سده‌های ۷–۸ هجری) می‌گذرد؛ پس گره در کل درست است، ولی پیکان «اسپانیایی ← فرانسوی» با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/search.html?q=ream\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2%D9%85%D8%A9\",\n            \"https://en.wiktionary.org/wiki/ream\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"LAM:199\", \"status\": \"supports\", \"note\": \"Lammens, Remarques sur les mots français dérivés de l'arabe (LAM.txt form-feed leaf 256 = printed p. 199, offset leaf = printed + 57), s.v. Rame: 'Rame. Esp : resma. Cat : raima. It : risma, Vieux fr. : rayme; de رزمة riẓma, paquet de hardes … et vulgairement … rame de papier. (Bocthor et Dozy, Supp.)'. The page is exactly right and it gives both the Spanish and the Catalan forms.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAM\", \"where\": \"Lammens p. 199 (leaf 256), s.v. Rame\", \"stance\": \"supports\", \"note\": \"'Esp : resma. Cat : raima. It : risma, Vieux fr. : rayme; de riẓma, paquet de hardes.'\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale, leaf 223 (printed ≈ p. 193), s.v. Rame\", \"stance\": \"partial\", \"note\": \"'Rame. Vieux français rayme, esp. et portug. rezma, ital. risma. De l'arabe رزمة rizma, qui a signifié paquet de hardes, ballot, puis rame de papier (dans Bocthor). Cette étymologie, proposée par Sousa, combattue par Diez qui préfère la dérivation ἀριθμός … a été appuyée et mise hors de doute par M. Dozy.' Devic derives the French word from Arabic directly (noting 'Rizma est devenu par la chute du z (comme dans rayme, rame) le portugais rima'), without insisting on a Spanish intermediary.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan, Dict. étym. … dérivés de l'arabe, du persan ou du turc, leaf 342 (printed p. 311), s.v. RAME (terme de papeterie)\", \"stance\": \"partial\", \"note\": \"'RAME (terme de papeterie), s.f. (a.) رزمة [rizma], assemblage, paquet, ballot de marchandises; dérivé de … [le z] ne se retrouve pas dans le mot français rame, on le retrouve transcrit par s dans l'espagnol et le portugais resma, ainsi que dans l'italien [risma]' — Pihan too takes French straight from Arabic and treats Spanish resma as a parallel, not an ancestor.\"},\n            {\"src\": \"DOZ\", \"where\": \"Oosterlingen leaf 84 (≈ p. 75)\", \"stance\": \"partial\", \"note\": \"'Het Fr. rame is ontstaan uit rasme, razme, razma; razma wordt in 't Arab. met dezelfde vokaal (de fatha) geschreven als rezma, en de uitspraak hangt van willekeur of van het dialect af' — Dozy derives French from an Arabic razma variant rather than from Castilian resma.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1723 (leaf 165 ≈ p. 139)\", \"stance\": \"partial\", \"note\": \"'hieraus it. risma, sp. pg. resma, razma, kat. raima, frz. rame' — Lokotsch lists French rame as a sister of Spanish resma under Arabic rizma, not as its descendant.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"ream 3\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English ream 'a quantity of paper' (Nourai's 'ream 3' is a homonym index: this is the paper word, as against ream 'cream' < OE rēam and ream 'to enlarge a hole' < OE rȳman) is Middle English rem/reme, first recorded mid-14th c., borrowed from Old French rayme/reme (mod. rame), ultimately Arabic rizma. The Arabic 'bundle' narrowed in the Iberian and French paper trade to the standard commercial unit, and English inherited that trade sense: 20 quires of 24 sheets = 480 sheets (a 'short ream'), later 500, and 516 in a printer's ream — so Nourai's gloss '500 sheets' is the modern count, while the historical one was 480 (Funk & Wagnalls: 'properly, 480 sheets … but often 500 sheets or more'). Klein, Skeat, Funk & Wagnalls, Etymonline and AHD all give the same chain; the only footnote is Etymonline's observation that an early variant rym (late 15th c.) and Middle Dutch rieme/Du. riem suggest the word may have entered English from more than one direction.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی ream «رزمهٔ کاغذ» (شمارهٔ ۳ نزد نورایی برای جدا کردن آن از دو هم‌آوای دیگر: ream «سرشیر» از انگلیسی کهن rēam و ream «گشاد کردن سوراخ» از rȳman) در انگلیسی میانه به صورت reme/rem از میانهٔ سدهٔ چهاردهم میلادی گواهی شده و وام‌واژه‌ای است از rayme فرانسهٔ کهن، و در نهایت از «رِزمة» عربی. معنی عمومی «بسته» در تجارت کاغذِ ایبری و فرانسوی به واحد شمارش کاغذ تخصیص یافت و انگلیسی همین معنی بازرگانی را گرفت: ۲۰ دسته × ۲۴ برگ = ۴۸۰ برگ (رزمهٔ کوتاه) و سپس ۵۰۰ برگ و در چاپخانه ۵۱۶ برگ؛ بنابراین معنی «۵۰۰ برگ» که نورایی آورده شمارِ امروزی است و شمار تاریخی ۴۸۰ بوده است. کلاین، اسکیت، فانک‌واگنالز، اتیمانلاین و AHD همگی همین زنجیره را می‌آورند و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/ream\",\n            \"https://en.wiktionary.org/wiki/ream\",\n            \"https://www.ahdictionary.com/word/search.html?q=ream\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1086\", \"status\": \"supports\", \"note\": \"Nourai cites the main body of the AHD New College ed. (1975/76), which is not openly available, so the page number itself could not be verified (the local AHD file is only Watkins's Indo-European appendix, which has no 'ream' because the word is Semitic). The AHD entry text, unchanged in substance across editions, is on ahdictionary.com s.v. ream¹: '[Middle English rem, from Old French rayme, reme, ultimately (perhaps via Old Catalan raima, from Andalusian colloquial Arabic *razma) from Arabic rizma, bundle, from razama, to bundle; see rzm in Semitic roots.]' — it supports the arrow, with the Catalan qualification discussed at node #4.\"},\n            {\"ref\": \"KLN:1307\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 696 (running numeral '1307' printed just above): 'ream, n., 20 quires of paper. — ME. reme, fr. OF. rayme (F. rame), fr. Sp. resma, fr. Arab. rizmah, \\\"bundle, bundle of paper\\\".'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 1307/1308 (leaf 696), s.v. ream 'n., 20 quires of paper'\", \"stance\": \"supports\", \"note\": \"'ME. reme, fr. OF. rayme (F. rame), fr. Sp. resma, fr. Arab. rizmah'; the same leaf shows Klein's two other 'ream' entries (OE rēam 'cream'; OE rȳman 'to make room'), which is why Nourai numbers his 'ream 3'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., leaf 419 (≈ printed p. 399), s.v. Ream\", \"stance\": \"supports\", \"note\": \"'Ream (F. – Span. – Arab.) M.E. reeme. – O.F. raime (F. rame), a ream or bundle of paper. – Span. resma, a ream. – Arab. rizmat (pl. rizam), a bundle.' — Skeat's language chain is letter-for-letter Nourai's.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, vol. 3 leaf 602 (printed ≈ 2068; Nourai cites 2060), s.v. ream⁴\", \"stance\": \"supports\", \"note\": \"'Twenty quires of paper, properly, 480 sheets (a short ream), but often 500 sheets or more (a long r.). [< F rame, < Sp resma, < Ar rizma, bundle of paper] … printers' ream, 20½ quires (516 sheets), the surplus to make up for waste.'\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1723 (leaf 165 ≈ p. 139)\", \"stance\": \"supports\", \"note\": \"'engl. ream, ndl. riem, dtsch. Ries [mit Abfall der letzten Silbe des it. Grundworts], dän. riis, schwed. ris' — the whole European family under Ar. rizma.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, 2nd ed. (WEB_vol1.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'resma' finds nothing: only volume 1 (A–…) is available locally, so the R section could not be consulted.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:29:58.941Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-427.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:30:00.679Z] TOOL CALL #41: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-427.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 427"
}
```


### [2026-09-14T01:30:01.892Z] TOOL RESULT

```
JSON OK
nodes verified: 5/5
node verdicts: {'confirmed': 4, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'not_checked': 2, 'supports': 6}
books consulted: {'supports': 14, 'silent': 6, 'partial': 4} | by book: {'LKT': 4, 'KLN': 3, 'DOZ': 3, 'SKT': 2, 'AFM': 1, 'FVQ': 1, 'MON': 1, 'BQT': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1, 'LAM': 1, 'DEV': 1, 'PHN': 1, 'FSD': 1, 'WEB': 1}
```


## [2026-09-14T01:30:19.221Z] AGENT

Page 427 (book p. 397) verified — one entry, 5 nodes, 0 PROBLEM lines.

**Verdicts:** root confirmed; nodes: 4 confirmed, 1 plausible. Ref checks: 6 supports, 2 not_checked. Books consulted: 14 supports / 4 partial / 6 silent across KLN, SKT, FSD, WEB, LKT, DOZ, DEV, PHN, LAM, MON, BQT, HRN, HUB, ARY, AFM, FVQ, plus AHD/DRAE/Wiktionary/Etymonline online (all archived via `fetch_source.py`).

**Content:** Arabic root ر-ز-م (رَزَمَ "to bundle") → rizma → Persian رزمه, and rizma → Sp. resma → OFr. rayme → Eng. ream. This is the standard textbook etymology; Nourai's chain is essentially right throughout.

- No `disputed` items.
- No `transcription_suspect` items; no extraction errors — the JSON matches the chart and the book's own conventions ("rezmeh" is Nourai's habitual Persian-style reading of Arabic *rizma*; "ream 3" is just his homonym index).
- One `plausible`: **#4 French rame/rayme.** The word is certainly from Arabic *rizma*, but the specific Spanish→French arrow is only one of two live reconstructions. Klein, Skeat, Lammens, Dozy, Devic, Pihan support it (Dozy: "Het Fr. rame is ontstaan uit rasme, razme, razma"); AHD5 and Wiktionary instead route it through Old Catalan *raima* (< Andalusi Arabic \*razma), which explains the -ai-/-ay- of the oldest French spellings better.

**Reference notes for the owner (no data fix needed):**
- KLN:1307 checks out exactly (running numeral "1307" sits a few lines above Klein's "ream" entry, leaf 696) — the recorded leaf≈floor(p/2)+12 offset is off by ~30 leaves in vol. II; the printed numerals are the reliable guide there.
- LAM:199 checks out exactly (leaf 256).
- FSD:2060 — the entry is real and says exactly what Nourai cites it for, but the recorded vol.-3 offset places it at p. ≈2068; no printed numeral survives in the OCR, so most likely scan drift rather than a bad citation.
- MON:1649 — entry text confirmed (Mo'in tags رزمه "[ع. رزمة]"), but the page number is unverifiable: the local MON OCR has no page markers and vajehyab/abadis print no pagination.
- FVA:161 (cited on the root and on nodes #1–#2) remains `not_checked`: Nahvi's *Farhang-e Vazheha-ye Arabi dar Farsi* still has no digital copy anywhere.
- AHD:1086 — content confirmed from the current AHD online entry; the 1975 New College main body is not openly available, so the page itself could not be checked (the local AHD file is Watkins's IE appendix only, which naturally lacks this Semitic word).
