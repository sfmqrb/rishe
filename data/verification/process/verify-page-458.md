# Verification process log — verify-page-458


## [2026-09-14T01:57:19.236Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 458 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-458.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-458.json. Write /home/sfmqrb/git/rishe/data/verification/page-458.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 458` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:57:20.264Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:57:21.172Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:57:21.192Z] TOOL RESULT

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


## [2026-09-14T01:57:21.670Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-458.txt"
}
```


### [2026-09-14T01:57:21.695Z] TOOL RESULT

```
1	=== PDF page 458 (book page 428) ===
2	--- entry 0 ---
3	ROOT Skhed -> redirect to Sek
4	--- entry 1 ---
5	ROOT Skou -> redirect to Keu 3
6	--- entry 2 ---
7	ROOT Sku -> redirect to Skeu 2
8	--- entry 3 ---
9	ROOT Skŭr -> redirect to Skeu 2
10	--- entry 4 ---
11	ROOT [Indo-European] Skwalo, Skwalos, Kwalo, Kwalos, Kwal : a big fish, whale  (refs POK:958)
12	#1 (parent #0) [Avestan] refs=POK:958; SOD:194 | kara 2 : whale
13	  #2 (parent #1) [Sogdian] refs=SOD:194 | krw : big fish, whale
14	  #3 (parent #1) [Persian] refs=SOD:194 | karv «کرو» : a kind of fish
15	#4 (parent #0) [Germanic] refs=AHD | hwaliz : whale
16	  #5 (parent #4) [English] refs=AHD | whale, walrus
17	#6 (parent #0) [Latin] refs=AHD | squalus : a kind of fish
18	  #7 (parent #6) [English] refs=AHD | squalene
19	--- entry 5 ---
20	ROOT Skwalos -> redirect to Skwalo
21	
```


## [2026-09-14T01:57:24.832Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-458.json",
 "description": "Read source JSON page 458"
}
```


### [2026-09-14T01:57:24.880Z] TOOL RESULT

```
{
  "pdf_page": 458,
  "book_page": 428,
  "entries": [
    {
      "root": {
        "name": "Skhed",
        "redirect": "Sek"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Skou",
        "redirect": "Keu 3"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sku",
        "redirect": "Skeu 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Skŭr",
        "redirect": "Skeu 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Skwalo, Skwalos, Kwalo, Kwalos, Kwal",
        "lang": "Indo-European",
        "refs": "POK:958",
        "gloss": "a big fish, whale"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:958; SOD:194",
          "words": [
            {"translit": "kara 2", "gloss": "whale", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:194",
          "words": [
            {"translit": "krw", "gloss": "big fish, whale", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Persian",
          "refs": "SOD:194",
          "words": [
            {"translit": "karv", "gloss": "a kind of fish", "script": "کرو"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hwaliz", "gloss": "whale", "script": null}
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
            {"translit": "whale, walrus", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "squalus", "gloss": "a kind of fish", "script": null}
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
            {"translit": "squalene", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Skwalos",
        "redirect": "Skwalo"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:57:26.677Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','AHD','WLD','IEC','SYN','BRT','KLN','SKT','HRN','HUB','MON','BQT','PHD','NYB','WEB','FSD','ARY','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-14T01:57:27.790Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
```


## [2026-09-14T01:57:30.568Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80"
}
```


### [2026-09-14T01:57:30.625Z] TOOL RESULT

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
```


## [2026-09-14T01:57:31.893Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n -i \"squalus\\|skʷalo\\|sq[uv]alus\" POK*.txt | head -40"
}
```


### [2026-09-14T01:57:31.950Z] TOOL RESULT

```
POK_03.txt:2633:Lat.  squalus  ,ein  größerer  Meerfisch^;  das  5-  könnte  aber  erst  sekundif von  squatus  ds.^,  squäma  ,Schuppe^  bezogen  sein;
POK_full.txt:77855:Material: Latin squalus^e'xu grofterer Meerfisch'; das 5- could but previously secondary
```


## [2026-09-14T01:57:33.738Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '2600,2680p' POK_03.txt"
}
```


### [2026-09-14T01:57:33.786Z] TOOL RESULT

```
lit.  shudriXs,  skaudrüs  ,flink';  lett.  skaudrs  ds.,  skudra  , Ameise';  aksl. is-kydati  , herauswerfen',  russ.  kiddth  , werfen*,  kidkij  , rasch,  bereit,  gieri»"*^
WP.  II  554 f.;  s.  auch  unter  5.  skeu-  und  skeub-,
(s)keup-,  skeub(h)-  , Büschel,  Schopf,  Quaste';  nur  gerin.  und  slav.
Aisl.  skauf  ,Büschel,  Quaste',  ags.  sceaf,  ahd.  scoub  ,Bündel,  Strohbund Garbe',    nhd.    dial.    Schaub    , Bündel,    Strohbund,    Strohwisch*,   aisl.   sküjr ,Troddel,  Quaste,  Büschel';   ahd.   scubil  ,Büschel  von   Haaren   oder  Stroh oder  dgl.,  Haufen,  Menge' ;
ags.  scyfelie)  f.  ,Frauenhaube'  (mit  jp:  aisl.  skypill,  skujpla  ds.);
ahd.  scobar  ßchober^  Haufe,  bes.  von  Getreide  oder  Heu',  mhd.  schöbet här  , Büschel,  Haare';
got.    skufta   (Dat.    Sg.)    , Haupthaar',    aisl.    sko'pt    ds. ;    mhd.   schöpf  m, ' ßchopf,   schöpfen   und    (nd.)   schoppen  , stopfen   (ursprüngl.   mit   Büschela  f^-^- von    Heu,    Haar   usw.),    geschwollen    sein';    mit    ebensolchem    germ.    pp: norw.  hupp  ,Quaste',  ahd.  hopfo  ,Hopfen^ ;
vielleicht  als  ,mit  Strohbündeln  gedecktes  Dach'  hierher  nd.  schupp ,Wetterdach'  (nhd.  Schuppen),  ahd.  scopf  m.  , Gebäude  ohne  Vorderwand, Scheune',  nhd.  bair.  Schweiz,  schöpf  m.  ds.,  ags.  scypen  f.  , Stall',  engl. shippen,  ags.  sc.oppa  m.  , Schuppen,  Bude'  (engl,  shop  ,Kramladen');
serb.  cüpa  ,Büschel   Haare',   russ.   cup^,   cub^,   cech.   cup,   cub   , Schopf;
vielleicht  slav.  *kyta  i^küp-tä)  in  russ.  küa  ,  Stengel  und  Blätter  lang- stieliger Pflanzen',  kitka  , Kätzchen  an  Bäumen'  usw.,  und  russ.  kisth i^^-küp-sti-)  , Quaste,  Pinsel,  Traube,  Hand',  bulg.  kiska  (aus  kyst^ka)  , Strauß*, skr.  koscica  ,Art  Pinsel',  alt  auch  kist,  poln.  kisc  ,Quaste,  Besen,  Busch, Büschel'.
WP.  II  555  f.
{s)keut',  (s)keudh-  ,einschrumpfen';  nur  germ.  und  baltisch.
Germ,   teils  -tt-,  teils  -dd-:   schwed.    dial.    hott,    hodd   m.   ,kleiner,   ein-
957
o-eschrumpfter  Mensch',,  ndl.  hotten  ^g-erinnen'^  ndd.  hotten  , einschrumpfen', yjl.  hot,  mnd.  hotte  , geronnene  Milch*^,  nhd.  dial.  hutzeln,  verhutzeln  ,ein- gchrumpfen^,  verhutzelt  ,verschrumpft,  vertrocknet' ;
lit.   ajp-kiausti   ^verkümmernd ;    hüstu,   Jcüdaü,    Jcüsti   , abmagern',    sujcüdes 2usam  mengeschrumpft'. '   WP.  II  553.
silek-,  sklQk-  ,naß,  spritzen,  sprengen'?
Aisl.  slag  n.  , Nässe  (von  Regen)',  sleginn  ,benetzt',  norw.  slagen  , feucht', -schwed.  slaga  , Sumpf;  mnd.  slagge  ^schlackiges,  regnerisches  Wetter^, schwed.  slagga-väder  ds. ;  nhd.  dial.  slaclc  ,Schneequatsch';  nd.  slack  ,große und  schwere  Tropfen',  slackern  ,verschütten,  sudeln',  besleckern  ,beklecken'; ablaut.  ags.  sloh  , Morast^,  mnd.  slöch  ds. ;
lit.  släkas  , Tropfen,  Fleck,  Kleck'  (in  der  Bed.  , Schlacke'  dt.  Lw.), slakstau,  -yti  ,mehrfach  spritzen,  sprengen',  slakü,  -eti  ,tröpfeln^  slekiuj sltJcti  ^spritzen',  lett.  slaka  , Anfeuchtung',  slacit  ,naßmachen,  besprengen, fein  regnen'.
WP.  II  602  f.,  705;  vgl.  auch  sresk-  ,tropfen'?
skordho-,     ä-  , Pfanne,  Scherbe'?
Ahd.  scart-lsarn,  mlid.  schart  m.  n.,  scharte  f.  , eiserne  Pfanne';  aksl. skrada  ,Tiegel,  Pfanne,  Herd'  (auch  skvrada,  skovrada,  poln.  skowroda, russ.  skovorodd]  v  kann  von  slav.  skver-  ,schmelzen',  aksl.  raskvhrg  usw., übernommen  sein);  lett.  skärds,  skärde  , Blech,  Weißblech'  hat,  wenn  zu- gehörig, seine  Bed.  vielleicht  aus  , Scherbe  (scharf  und  dünn)'  entwickelt.
WP.  II  601.
skot-  ,Schatten,  Dunkel'.
Gr.  OY.OTog  , Dunkelheit'  (m.,  später  n.);  air.  (dehnstufig)  scäth  n.  , Schatten, Schutz,    Spiegel';    mcymr.    isgaudj    cy-sgawd,    cymr.    cy-sgod,    acorn.    scod, neucorn.  skez,  bret.  skeud  , Schatten';  got.  skadus  m.,  ags.  sceadu  f.,  scead  n., ahd.  scatOj  -awes  , Schatten',  norw.  skodda,  skadda  ,Nebel'. WP.  II  600.
{s)kut-  ,rütteln'.
Lit.  kutü,  kuteti  , auf  rütteln',  kustü  und  kuntü,  kutan,  kusti  ,sich  auf- rütteln, sich  erholen',  kutrüs  , hurtig',  kutä  , Quaste,  Franse';
daneben  mit  anlaut.  s-:
as.  scuddian  ,mit  einem  Schwünge  ausgießen',  ahd.  scutten,  afries.  skedda , schütteln,  erschüttern',  nhd.  schütten^  mndl.  mengl.  schuderen,  engl,  shudder , schaudern,   zittern'   (*,sich  schütteln'),   nhd.   schaudern  (rheinfränk.  Wort
958  ,
'i mit  nd.  d\  ahd.  scutilön,  nhd.  schütteln:  ags.  scüdan,  scyndan,  aisl.  sKni« , treiben^  und  skunda  , beschleunigen ;  eilen^,  as.  farskundian  »anreizen,  anL     ^ hetzenS  alid.  scunten  ^antreiben,  reizen';  aksl.  skytati  se  ;Vagari^  -^^   '
WP.  II  601  f. ;  s.  auch  oben  S.  632  unter  kuet-.  "^^^
(s)k^alo-s  oder  vielmehr  k}ialo-s  ,eme  größere  Fischart^?
Lat.  squalus  ,ein  größerer  Meerfisch^;  das  5-  könnte  aber  erst  sekundif von  squatus  ds.^,  squäma  ,Schuppe^  bezogen  sein;
aisl.  hvalr  m.  (neben  -hveli  n.)  ^Walfisch^  C^'-St.),  ags.  hwal,  engl.  tohaiT as.  ahd.  hwal  ds.,  neben  ahd.  hwelira  (germ.  *hvali-s-ön-),  nhd.  WalUr Weller  und  mhd.  ,Wels'-  (germ.  *hvali-s),  wozu  auch  apr.  kalis  »Welt«, der  mythische  Fisch  av.  kora-  ist  die  iran.  Wiedergabe  eines  urmordwin *kola  ,Fisch^^  später  kal^  zu  tscherem.  kol,  läpp,  guole,  finn.  Ä:aZa  usw.  •  die ganze  Sippe  also  wohl  finno-ugr.  Herkunft.
WP.  II  541,  WH.  II  581  f.,  Hoops,  Engl.  Stud.  28,  Iff.,  Jacobsohn,  Arier und  Ugrofinnen  241  f.
skuerh{h)-  , stechen,  etwa  wie  Dornen'?  Nur  keltisch  und  baltisch. Com.  bret.  syern  ,spinae*  {-rn-  aus  -rhn-) ;
lit.   skverbiü,   skverbti   ,m\i   einem   spitzen  Werkzeug   bohrend   stechen', Iter.    skvarhaüj   skvarbyti  ds.,   skvirhinu,   -inti  , stechen,   bohren,  prickeln', WP.  II  602.
sk{h)uoi-,  sk{h)ui{i)-  ,Nadel  oder  Dorn  von  Pflanzen'.
Air.  sce,  Gen.  PL  sciad  ,Hagedorn'  [* skuii-at-s) ;  cymr.  ysbyddad  ds.,  —^ com.  spethes  ,Brombeerstrauch,  Dorngestrüpp',  bret.  spezad  ,StachelbeereD**  ^J lit.  skujä  , Tannennadel  und  -zapfen',  lett.  skiijas  , Tannenreisig';  russ.  chvojd^^ f.,  chvoj  m.  ,Nadeln  und  Zweige  der  Nadelhölzer'  (usw.;  Berneker  408^ erwägt  Zugehörigkeit  auch  von  russ.  chuj  ,penis'  als  ^{s)khouios). WP.  II  602,  Trautmann  268.
(s)läg^-  ,fassen,  ergreifen'.
Gr.  (ep.  ion.)  XdZo^ai  (Präs.  und  Impf.)  ,nehme,  fasse,  ergreife  (*Aay(")iö>);  ^^'. nach  aivv(.iaL  ist  ion.  att.  Adjvftat,  böot.  Xaddovad-rj  umgebildet;  Aor.  sXlaßs (hom.),  elaßov,  aegin.  Ihaßcbv,  att.  inschr.  Ahaßsxog  oder  -rjTog,  Perf.  att. sXlrjCpa  {*aaaläq)a)j  Fut.  Irjipo^ai,  ion.  IdipoiLai,  Präs.  ion.  att.  lay.ßav(ü  (zu XaßeZv  neugebildet) ;  Xäßqoq  ,heftig,  ungestüm ;  gefräßig,  gierig',  IdßgG^  m. ,Meerwolf'  (Fisch),  hom.  laßgevoj-iai  ,schwatze  frech,  vorlaut',  laßQ-ayÖQrjg jfrech  redend',  laßgovad^ai  ,sich  worauf  stürzen';
ags.  IcBccan  ,fassen,  ergreifen'  (==  Xal^Ofiai  aus  *slagYiiö),  engl,  latch,
WP.  II  707,  Schwyzer  Gr.  Gr.  1,  649,  698,  699.
959
Igen,  hämmern'';  nur  irisch  und  orermanisch.
,  ..V..  ..    ^..^  j^.
cc  ^Schwerf^^  nir.  slacaire  , Schläger^  (mit  expressivem  -/^A:-);  mir. eschlagen''^  nir.  slaclit  m.  ;gute  Erscheinung,  von  gutem  Schlagt, daim  , schlage  mit  dem  Hammer^^  slachdan  ^Keule^ ; 'lAan,  aisl.  slä,  ags.  sleaii^  as.  ahd.  slahan  (sluoc,  sluogen,  geslagen) ahd.  slagon,  afries.  slagia  ds. ;  aisl.  slä  f.  , Stange,  Riegel'^  ags. a  jWeberkamm',  mhd.  sla^  dage  ,Schlagwerkzeug^,  mnd.  slawe lag'',  mhd.  slouice  ,Spur,  Fährte'  (^slagtcö);  dehnstufig  aisl.  slegr
g'  (*^ verschlagen^);  got.  slauhts  f.  , Schlachtung^  (*slk-ti-)]  aisl. lahd^,  slätr  L  ^Schlachtfleisch',  ahd.  slahta  ^Tötung,  Schlachtung';
Bedeutung  wie  nhd.  jemandem  nachschlagen,  Schlag  ,Art^:  ahd. del  geartet^,   gislahti  n.    , Stamm,    Eigenschaft'^    nhd.    Geschlecht.
706  f.,  Wissmann  Nomina  postverb.  74.
7o5-,  (s)lep-,  (s)lop-,  s.  oben  S.  655  ff.^  wozu  vielleicht  mir. xp  [p  =  b)y  lenah  {h  =  w)  , kleines  Kind''.
iQg-  und  {s)leg-  , schlaff,  matt  sein'  (aus  Joslassen'),  nas.  (s) leng- eng- , schaukeln,  schwanken^?);  sl9g-on-  , Herabhängendes' ;   aus
ff^  über  , weichlich'  auch  , wollüstig'.
xja-  ,lahm' ;  gr.  XjJ^'w  ,lasse  ab,  höre  auf  (*ermatte);  trans.  , mache
[*slegö),  aXXrjy,Tog  (*gX-)  , unaufhörlich',  Xay&ooai'  dcpsTvat  Hes., 'chlaff,  schmächtig,  dünn^,  hom.  laycoög,  ion.  Xayög,  att.  Xaycog,  -d) 's)ldg-öusos  ,mit  schlaffen  Ohren*),  Xaywv,  -ovog  gewöhnlich  PI. Jien,  Dünnen'  (formell  =  aisl.  Uiki  , Faltmagen'),  Xdyavov  , dünner ichen*  (formell  =  as.  laJcan  usw.  ,Tuch'),  XfxjydvLOv  , Wamme'  (vgl. iöJca  , schlaff  herabhängen'),  nasaliert  vermutlich  hierher  Xayycc^co Xayychv  , Zaudern',  Xayysvai '  cpevyat  Hes.  (*,matt  sein,  schlaff  und ^  sein') ;   mit   der   Bedeutung  ,Tvollüstig' :  Xdyvog  ,geil',  Xayvsveiv
sein',   Xayveia  , Geilheit,  Wollust',   Xujydg-    noQrrj    Hes.   (daneben
.  Xeyai  de  yvvatyisg  =  dy.öXaOTOi  ArchiL,  eXsyalvaiv  „daeXyalvsiv'^
'IS  , schlaff,  weit,  geräumig',  nas.  langueö,  -ere,  ,matt,  schlaff,  ab- sein';
(mit  expressivem  gg) , schlaff,  schwach';  mcymr.  llacc,  ncjmr.  Uac ammt  wegen  seines  cc  statt  ch  aus  engl,  slack; ik  , schlaff,  lose',  ndl.  lak,  nhd.  mdartl.  lack  ds.,  mndl.  lak  auch :,  aisl.  lakr  und  (vollstufig)  Wer  ^schlecht,  gering' ;  mit  Abtönung dial.  löka  , schlaff  herabhängen',  aisl.  lökr  , Dummkopf,  Faulpelz' ; ana- , baumelnder  Lappen.  Zipfel'  in  as.  lakan  ,Tuch',  ahd.  lahhan
960
#
ds.  (nhd.  Laken  aus  dem  Nd.,  formell  vgl.  gr.  Xayavov),  aisl.  lalcim.  ,Quan der  dritte  Magen  der  Wiederkäuer,  Faltmagen^  (=  Xaywv),  Mangel,  Fehl!.
mit  S-:   aisl.   5ZaÄ:r  ^schlaff"    (poet.),   slakna   ^erschlaffen',    as.    mn^,   ./^ ,schlaff,    schwach',    Fartiz.    as.    gislekit   , stumpf    gemacht',    mnd.    «Zaifc-uJ , Bauchseite'  (wie  laycbv  und  nhd.  Weichen),  ags.  sJ(SC  ^schlaff,  träge,  lan^^s^^t ahd.  slah-  ^schlaff,  träge',  ags.  sleccan  (*slekjan)  , schwächen';  *
mit  Abtönung  ö:  aisl.  slökr  ,ein  schlaffer  Bursche^norw.  slöken  ,schUff* schwed.  slöka  , schlaff  herabhängen  lassen',  dial.  ,träge  sein',  slök  und  (m^  jj släk  ^leichtsinniges  Weib',  aschwed.  slökifrip,  -frilla  ,Kebsweib';
nasaliert  wohl  schwed.  slinka  , nicht  fest  ansitzen,  schlottern,  hinken* ahd.  sUnc,  ndl.  slink  ,link',  mhd.  link,  nhd.  link]  ahd.  lenka  ,die  Linkft** schwed.  linka  und  lanka  ,etwas  hinken',  lunka  , langsam  gehen',  dän.  sZi^nii^ , schlaff,  schlotterig'  (*  schlaff  dahergehen');  vielleicht  schwed.  dial.  ilatik süddt.  schlank  ,Fetzen';
lett.  legens  , schlaff,  weich';  ,.
unsicher  russ.  pere-slega  , Fehler  im  Gewebe'  (*, Auslassen  des  Fadens'? ?1 sloven.  preslegast  , fadenscheinig,  kahl';
ob  auch  toch.  A  släkkär  , traurig'?
WP.  II  712  ff.,  WH.  I  7ö8f.
sleg^-  , drücken,  bedrücken,  mißhandeln' ;  slög^ä  , Plage'.
Gr.  X(bßrj  f.  , schimpfliche  Behandlung,  Schmach,  Mißhandlung,  Schaden^ Verderben',  Xcüßdojxai  , behandle  schimpflich,  mißhandle,  verstümmle,  frevle, schädige';
lit.  slogä  , Plage,  Landplage',  mit  sekundärem  Ablaut.:  lett.  sZä^a , Schaden, Beschwerde';  lit.  slogiis  , beschwerlich',  sloginti  ,plagen',  sluogal  , Hölzer zum  Beschweren  eingeweichten  Flachses';  mit  uo:  lit.  slüogas,  lett.  sluog$ jKlotz,  Stein,  Last',  sluodzit  ,beschweren,  niederpressen,  prügeln',  sluogdt^ sluoguot  ds. ;  mit  e:  lit.  sleg-iu,  -ti  , bedrücken,  pressen',  lett.  siegt  , schließen' (*,zudrücken'),  lit.  sUgtis,  siegte  , Presse,  Kelter',  lett.  at-slega  ,Schloß', slegs  , Bürde'.
WP.  II  714.
{s)leih-  , schlüpfrig,   gleiten'  s.  oben   S.   663;   dazu  vielleicht  (nach  Morris- Jones  WGr.  125)  cymr.  llithr  m.  ,das  Gleiten'  (*slib-tro-).
(s)leidh-  ^schlüpfrig,   gleiten';   Erweiterung  von   3.  lei-,  slei-  ohen  S.  662 f,
Ai.   sredhati  , gleitet   ab,    geht    fehl,    irrt';    gr.    öhaMvco,    Aor.    Öjlta^Of
,gleite',  dXta^TjQÖg  ,schlüpfrig',  HXio&og  m.  ,Glätte,  Schlüpfrigkeit'  (Hidh-to-t)
beruhen  auf  einem  -dhö-  oder  -tö-  Präsens ;  Anlaut  wie  in  dXißQÖg  von  der
verwandten  Wurzel  {s)leih-,  oben  S.  663;
961
```


## [2026-09-14T01:57:34.415Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '77830,77890p' POK_full.txt"
}
```


### [2026-09-14T01:57:34.477Z] TOOL RESULT

```
rainy weather ', Swedish slagga-vader6s.\ Modern High German 6\a\. slack 

"Schneequatsch'; Low German s/5c/r"big, giant and heavy drip', s/ac/re/r? "verschijtten, 

pollute ', i6'es/ec/re/r7"beklecken'; ablaut. Old English 5/0/7 "morass'. Middle Low German 

sldch6s.\ 

Lithuanian 5/aAas "drip, stain, Kleck' (in the meaning "Schlacke' German loanword), 
slakstau, -y//"mehrfach spritzen, sprinkle ', slaku, -e//"drip, trickle', slekili, s/ekt/" spray' , 
Latvian 5/a/ra "Anfeuchtung', 5/ac/7"naftmachen, sprinkle, fine rain'. 

References: WP. II 602 f., 705; 

See also: compare also sresk- "drip'? 

Page(s): 957 

Root / lemma: (sj/ca/o-s 

Meaning: a large fish 

Note: or rather /cra/o-s? 

Material: Latin squalus^e'xu grofterer Meerfisch'; das 5- could but previously secondary 

from squatus ds., squama^ scale, husk ' attributed sein; 

Old Icelandic hvalrm. (besides -hveliu.) "whale' (/-stem). Old English hwael, engl. 
whale. Old Saxon Old High German hwalds., besides Old High German hwelira 
(Germanic *hvali-s-dn-). Modern High German Waller, i/Velleran6 Middle High German 
'H/e/s'(Germanic *hvali-s), wherefore also Old Prussian /ra/zis "Wels'; the mythische fish 
Avestan kora- is die Iran. Wiedergabe eines urmordwin. */ro/5 "fish', later kal, to tscherem. 
kol, lapp. guole, Finnish kalaetc; die ganze family also probably finno-ugr. origin. 

References: WP. II 541, WH. II 581 f.. Hoops, Engl. Stud. 28, 1 ff., Jacobsohn, Arierand 
Ugrofinnen 241 f. 
Page(s): 958 

Root / lemma: (s)k''el-5, (s)kel- 
Meaning: " sound, shout ' 
See also: see above S. 550 {kel-). 
Page(s): 928 



Root / lemma: (s)k''er- 

Meaning: ' make ' 

See also: see above S. 641 f. {k^er-). 

Page(s): 947 



Root / lemma: slak- 

Meaning: to hit, hammer
```


## [2026-09-14T01:57:51.756Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && ls | tail -30; echo ---; grep -n -i \"squal\\|whale\\|walrus\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-14T01:57:51.822Z] TOOL RESULT

```
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
SKT_dli_revised.txt
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
---
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
949:(s)kwal-o-. Big fish. 1. Suffixed form *kval-o- in Ger- manic *hwalaz, whale, in: a. Old English hwel, whale: WHALE); b. Old Norse Avalr, whale: NARWAL, RORQUAL. 2. Latin squalus, a sea fish: SQUALENE. [Pok. (s)k¥alo- 958.]
2281:SPRINGE spergh- SPRINKLE (8)preg- SPRIT sper-4 SPROUT sper-4 SPRY (s)preg- SPUME (S)poi-mo- SPUR spere- SPURGE peue- SPURN spere- SPURRY (s)preg- SPURT sper-4 SPUTNIK ksun, pent- SPUTTER spyeu- SPUTUM spyeu- SPY spek- SQUAD kWetwer- SQUALENE (8)kWal-o- SQUARE kWetwer- SQUASH2 kwét- SQUAT ag- SQUIRE skei- SQUIRREL ors-, skeoi- STABLE! sta- STABLE? sta- STACK steg- STACTE stag- STADDLE sta- STADHOLDER sta- STAFF! stebh- STAG stegh- STAGE sta- STAGGER steg- STAGNANT stag- STAIN teng-
```


## [2026-09-14T01:57:52.500Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n -i \"kara\" BRT.txt | sed -n '1,60p'"
}
```


### [2026-09-14T01:57:52.571Z] TOOL RESULT

```
<persisted-output>
Output too large (29.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bfq5dowxb.txt

Preview (first 2KB):
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  
...
</persisted-output>
```


## [2026-09-14T01:58:02.994Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n -io \"WALRUS [a-z-]*\" AHD_watkins1985.txt | head; echo ---NARWHAL---; grep -n -io \"NARWHAL[ A-Za-z-]\\{0,20\\}\" AHD_watkins1985.txt|head"
}
```


### [2026-09-14T01:58:04.060Z] TOOL RESULT

```
---NARWHAL---
771:NARWHAL
1900:NARWHAL nau-
```


## [2026-09-14T01:58:04.082Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n \"Fisch\" BRT.txt | grep -n -i \"kara\\|kar3\\|kar»\" | head -20"
}
```


### [2026-09-14T01:58:04.143Z] TOOL RESULT

```
3:9227:•  j.  'kara-  n.  Name  eines  Fisches";  'r5'     Karchedonier  (KarthagerV
```


## [2026-09-14T01:58:08.011Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '9220,9235p' BRT.txt"
}
```


### [2026-09-14T01:58:08.085Z] TOOL RESULT

```
ob,Google
45'  kara?  —  karat-  3  45z
aihiiara-.    S.  oben  bei /flr/j'.  —  ')  Hds.  j^aj-',  ■      n.,   lam  V.  'i-ar-,    ^   ai.    iäraim-    n,    anin- aber  Pü.:  rauimd;  vgl.  /anlä-  No.  l.  —  3)  Un- '      setien.
sichereKorr.  d«  N  A     Grammatisch  verwahr-    ,         ^arka-   Adj.,  bezeichnet  ein  Volk'»: loste  Stelle.  —  4)  Vel.  lu  'vah-,  ■  j   i  k    \.  j  7
„ .  ,,  .  im3    dahyävar    tyn    adam    asarbäyam  ,  .
'  ^"''Vi!  ^''  "  "'«'^>^  "■*^  (NPm.)  D.tf.3.
'""  """■  ')    Nach    JtJSTI  GlrPh.  2.  455    das  Volk  der
•  j.  'kara-  n.  Name  eines  Fisches";  'r5'     Karchedonier  (KarthagerV
masys  upäps  yd  ranhaya  .  .  var?ss.stava-  ,  j.  kahrka  indekl.,  den  Ruf  des  Hahns
nhsm  äpS  urvaliim   marayeite  Yt  14.  29;  nachahmendes  Wort  'Kikeriki'.       a)  auch
V.  sg.  4a.  als  Bezeichnung  des  Hahns,
•)  Im  Mp.  iar  m<>hU,    ein  mythischer  Fisch,  KompA. ;  Abicit.  —  np.  tart  'Huhn';  ai.  vgl.
der  grösste  und  Akt  Ralav  der  Fische;  vgl.  Bd.  krka'vAkav'  m.  'Hahn',
14.  II,  34.  13;  tS-  3.  zs.  M.  4-  ,  .   kahrka'tit-  f.  (gemeiner  oder  Spott-)
.]  'kara-m.EN.emesTuramers:.^.j^e^^  ^'^^^   ^^^  ^^^^^._  \           y^  j^/,jJl
alavazdä..yatbavämaa,tut.vanyädänavs  ^^^^  ^^^^      -^  „^^^^_^^  ^...  ^„.,,„,^„^^
```


## [2026-09-14T01:58:09.137Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n \"krw\\|kr'w\" SOD.txt | head -20; echo \"=== pages file ===\"; grep -n \"big fish\\|whale\" SOD.txt | head -20"
}
```


### [2026-09-14T01:58:09.224Z] TOOL RESULT

```
11660:646  >5krw   S 
17211:1454  Vkrwn'y    B  >'<J><J^^X 
17212:ark(k)arune   Orkrwny) 
17217:1455  'rkrwny  =>  >rkrwn}y 
19159:1751  >skrwp   B  (J>jJlt.)j^\^iKjF^ 
31053:6andak   (6n5yt)  ©f.n.;  pi.  dnfyt   =»krw 
39598:4821  kr'wny  B  fl=*»<J-* 
39599:karunc  =>krwn 
39931:4875  krw*   B  <hJ*  vS  tJ^^t^'J^W^ 
39939:4876  krwpr'n   M  jlijA* 
39946:4877  krw  8nt>k(h)   B  ^jj^tJ*  u'^  ^"OW4  0'^ 
39954:4878  krw  kpy   M        ?  JL+  <?  ^U  ^J  .(^U  ^y)  )/ 
39971:4879  krwn    M  fb*l  <fU3l  <J\ « J^p 
39978:269,  347;  >rkrwriy:  >rk-krwriy,  STii;  Gersh. 
39982:4880  qrwn    M,  C  =*  krwn 
59921:KG  475,  583;  ptkr'w,  SCE  87;  Dhy.  120; 
75968:10,  27;  W-Lii  572n3;  wkrw,  BBB  533;  KG 
82076:10915  y>tk  kr'wny   B 
83415:11109  yxwnk  kr'wny   S  S^t^aJ^: 
86038:11483  zwkrwfi'k   B  ^.^  c[f  l0 p  ^u 
=== pages file ===
39955:kar(w)-kapi   ©<Av.  kara;  <IE  *skvalos,  whale-, 
39958:Kar  f ish(a  kind  of  fish),  cat-fish  ?,  whale  ? 
95262:whale    4878
```


## [2026-09-14T01:58:16.009Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '39925,39995p' SOD.txt"
}
```


### [2026-09-14T01:58:16.087Z] TOOL RESULT

```
incorruptible 

Sund.  Man.  Lett.  305.5,  301  n  14,  312.5 

4874  krts'r   S  =*  kwrts'r 

4875  krw*   B  <hJ*  vS  tJ^^t^'J^W^ 

karwa 

gap 

BSTBL,  Dhy.  66;  Hen.  L  W  96 

4876  krwpr'n   M  jlijA* 
karu  Paran 

heavy-loaded 

Sund.  MSP  bl37,  139n  p46 

4877  krw  8nt>k(h)   B  ^jj^tJ*  u'^  ^"OW4  0'^ 
karw-5ande,  Sandak 

gap-toothed 

SCE  83;  Sogdica.  23.19;  Gersh.  Sogd.  Cpds.  144.1; 
Hen.  L  W  96 

4878  krw  kpy   M        ?  JL+  <?  ^U  ^J  .(^U  ^y)  )/ 
kar(w)-kapi   ©<Av.  kara;  <IE  *skvalos,  whale-, 

Finish.  kala;  Hung,  kat 
Kar  f ish(a  kind  of  fish),  cat-fish  ?,  whale  ? 
Bailey.  AM  1965,  113;  Hen.  Tales.  483.3 


i 


195 


qs- 


4879  krwn    M  fb*l  <fU3l  <J\ « J^p 
karGn,  karwan  ?  (qrwn)  =>kr}wny 

making,  effect,  executing 

GMS  1101  n  1,  1123  n  1;  STi  63.14,  68.22;  TSP  2, 

269,  347;  >rkrwriy:  >rk-krwriy,  STii;  Gersh. 

Sogd.  Cpds.  137 

4880  qrwn    M,  C  =*  krwn 

4881  qrwn'mndyh   M  jJkijftJ** 
karunamande   (qrwn'mnty) 

action,  effecting 

Sogdica.  36.16;  GMS  1101;  C2,  nom.  94R28,  ace. 

-fw,  51V  23,  61R27,  abl.  -/>,  31R18:  BSTii 

826.28,  829.18,  909.27       \ 

4882  qrwn'mnty    C  =4  qrwn}mndyh
```


## [2026-09-14T01:58:32.137Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && ls | grep -i \"BQT\\|MON\\|ARY\\|SOD\\|FRS\\|TAD\"; echo \"=== grep کرو ===\"; grep -l \"کرو\" *.txt 2>/dev/null"
}
```


### [2026-09-14T01:58:32.224Z] TOOL RESULT

```
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
FRS_pages.txt
FRS.txt
MON_part1.txt
MON_part2.txt
NYB_vol2_glossary.txt
SOD_pages.txt
SOD.txt
TAD_pages.txt
TAD.txt
=== grep کرو ===
AFM_alt.txt
BQT_v2.txt
BQT_v2_pages.txt
BQT_alt_v1.txt
FRS_pages.txt
BQT_v1_pages.txt
BQT_v1.txt
FSF.txt
FRS.txt
NYB_vol1.txt
MON_part2.txt
FSF_pages.txt
GPL.txt
MON_part1.txt
SBK.txt
```


## [2026-09-14T01:58:32.956Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n \"\\[pdf page\" SOD_pages.txt | sed -n '190,205p'"
}
```


### [2026-09-14T01:58:33.017Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:58:36.274Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n \"کرو\" MON_part1.txt MON_part2.txt | grep \"ماهی\" | head -20; echo \"=== kar mahi ===\"; grep -n \"کر ماهی\\|کرماهی\" *.txt | head -20"
}
```


### [2026-09-14T01:58:36.367Z] TOOL RESULT

```
=== kar mahi ===
MON_part2.txt:50020:که در دعاوی عادی کر ماهیتی
```


## [2026-09-14T01:58:47.022Z] TOOL CALL #19: Bash

```json
{
 "command": "pdftoppm -f 458 -l 458 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg458 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg458.png"
}
```


## [2026-09-14T01:58:48.035Z] TOOL CALL #20: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-14T01:58:48.736Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 43086 Sep 13 21:58 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg458.png
```


### [2026-09-14T01:58:48.782Z] TOOL RESULT

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


## [2026-09-14T01:58:50.774Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg458.png"
}
```


### [2026-09-14T01:58:51.325Z] TOOL RESULT

```

```


## [2026-09-14T01:58:51.315Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:59:01.773Z] TOOL CALL #22: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sk%CA%B7alos\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hwalaz\" \\\n \"https://www.etymonline.com/word/walrus\" \\\n \"https://www.etymonline.com/word/whale\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 458, root Skwalo, whale/walrus/Germanic hwalaz chain\" ; done"
}
```


## [2026-09-14T01:59:03.438Z] TOOL CALL #23: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/squalene\" \\\n \"https://en.wiktionary.org/wiki/squalus\" \\\n \"https://en.wiktionary.org/wiki/walrus\" \\\n \"https://www.iranicaonline.org/articles/kara-fish\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 458, root Skwalo: Latin squalus/squalene; Avestan kara fish\" ; done"
}
```


### [2026-09-14T01:59:04.819Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/11eedba020b64501.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/91fd887dfbbde243.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ca6f20558d98ab5e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/49307c9a0d029ad9.txt
```


### [2026-09-14T01:59:11.168Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/8f0b4d1f3e4b2567.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9834815a11839908.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/49ac1e4287fac18f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aa12859c0186d55a.txt
```


## [2026-09-14T01:59:13.619Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -c 600 11eedba020b64501.txt; echo; echo \"=====hwalaz\"; grep -n -i -A5 \"Etymology\" 91fd887dfbbde243.txt | head -60"
}
```


### [2026-09-14T01:59:13.685Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sk%CA%B7alos
FETCHED: 2026-09-14T01:59:03Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
=====hwalaz
65: Etymology 1 
66-
67- 1.2.1 
68- Noun 
69-
70- 1.2.1.1 
--
77: Etymology 2 
78-
79- 1.3.1 
80- Noun 
81-
82- 1.3.1.1 
--
159: Etymology 1
160- [ edit ] 
161-
162- From Proto-Indo-European *(s)kʷálos ( “ large fish, sheatfish ” ) . Compare Latin squalus , Old Prussian kalis , Ancient Greek ἀσπαλιεύς ( aspalieús , “ fisherman ” ) , Avestan 𐬐𐬀𐬭𐬀 ( kara , “ kind of fish ” ) . [ 1 ] 
163-
164- Noun
--
257: Etymology 2
258- [ edit ] 
259-
260: From Proto-Indo-European *(s)kʷálos ( “ large fish, sheatfish ” ) , from the same source as Etymology 1.
261-
262- Noun
263- [ edit ] 
264-
265- *hwalaz   n 
--
343: ^ Vladimir Orel ( 2003 ), “*xwalaz”, in A Handbook of Germanic Etymology ‎ [2] , Leiden, Boston: Brill , →ISBN , page 197 
344-
345- Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Germanic/hwalaz&oldid=92427338 "
346-
347- Categories : Proto-Germanic terms with IPA pronunciation 
348- Rhymes:Proto-Germanic/ɑ.lɑz
```


## [2026-09-14T01:59:15.003Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== walrus etymonline ===\"; grep -n -i -B2 -A12 \"walrus\" ca6f20558d98ab5e.txt | head -60; echo \"=== iranica ===\"; head -c 400 aa12859c0186d55a.txt"
}
```


### [2026-09-14T01:59:15.085Z] TOOL RESULT

```
=== walrus etymonline ===
1:URL: https://www.etymonline.com/word/walrus
2-FETCHED: 2026-09-14T01:59:04Z
3-STATUS: 200
4:TITLE: Walrus - Etymology, Origin & Meaning
5-
6:Walrus - Etymology, Origin & Meaning 
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
17-
18- Advertisement Remove Ads 
19- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
20-
21: Origin and history of walrus 
22-
23: walrus (n.) 
24-
25: "very large pinniped carnivorous mammal" (the males are noted for their enormous tusk-like canine teeth), 1650s, from Dutch walrus , which was probably a folk-etymology alteration (by influence of Dutch walvis "whale" and ros "horse") of a Scandinavian word, such as Old Norse rosmhvalr "walrus," hrosshvalr "a kind of whale," or rostungr "walrus."
26-
27- Old English had horschwæl , and later morse , from Lapp morsa or Finnish mursu , which ultimately might be the source, much garbled, of the first element in Old Norse rosmhvalr .
28-
29- In reference to a type of large, overgrown mustache, by 1888.
30- also from 1650s 
31-
32: Entries linking to walrus 
33-
34- sea-horse (n.) 
35-
36: late 15c., "walrus" (apparently), from sea + horse (n.); compare walrus . Also in heraldry as a fabulous animal with the foreparts of a horse and the tail of a fish. Main modern sense in zoology is attested from 1580s.
37-
38- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
39-
40- More to explore
41-
42- sward 
43-
44: Dutch swarde "rind of bacon," Dutch zwoord "rind of bacon," German Schwarte "thick, hard skin, rind," Old Norse svörðr "walrus...
45-
46- whale 
47-
48: "animals of the mammalian order Cetacea," Old English hwæl "whale," also "walrus," from Proto-Germanic *hwalaz (source also...
49-
50- seal 
51-
52: "fish-eating marine mammal with flippers; any pinniped not a walrus," Middle English sele, from Old English seolh "seal,"...
53-
54- pinniped 
55-
56: "a fin-footed mammal," one having feet like fins or flippers, especially of the group of fin-footed aquatic carnivorous quadruped mammals that includes seals, sea-lions, and walruses, 1842, from Modern Latin Pinnipedia, suborder of aquatic carnivorous mammals (seals and walruses)
57-
58- sea 
59-
60- Middle English se, seo, from Old English sæ, "sheet of water, sea, lake, pool," from Proto-Germanic *saiwa- (source also of Old Saxon seo, Old Frisian se, Middle Dutch see, Dutch zee, German See, Swedish sjö), of unknown origin, outside connections "wholly doubtful" [Buck], and a
=== iranica ===
URL: https://www.iranicaonline.org/articles/kara-fish
FETCHED: 2026-09-14T01:59:11Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T01:59:30.608Z] TOOL CALL #26: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)k%CA%B7%C3%A1los\" \\\n \"https://en.wiktionary.org/wiki/%F0%90%AC%90%F0%90%AC%80%F0%90%AC%AD%F0%90%AC%80\" \\\n \"https://en.wiktionary.org/wiki/whale\" \\\n \"https://www.ahdictionary.com/word/indoeurop.html\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 458, root Skwalo: PIE (s)kʷálos, Avestan kara, English whale, AHD appendix\" ; done"
}
```


## [2026-09-14T01:59:32.559Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== squalene wikt ===\"; grep -n -i -A8 \"Etymology\" 8f0b4d1f3e4b2567.txt | head -30; echo \"=== squalus wikt ===\"; grep -n -i -A10 \"Latin\" 9834815a11839908.txt | head -40"
}
```


### [2026-09-14T01:59:34.517Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9f9c11a79838ed77.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/757ce544eda74572.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/435dcb9842952f5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3735d75498a331a4.txt
```


### [2026-09-14T01:59:34.611Z] TOOL RESULT

```
=== squalene wikt ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
--
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Noun 
92-
93- 2.3.1 
--
170: Etymology
171- [ edit ] 
172-
173- From Latin squālus ( “ shark ” ) +‎ -ene , because it is found in shark liver.
174-
175- Pronunciation
176- [ edit ] 
177-
178- IPA ( key ) : /ˈskweɪliːn/ , /ˈskwɑːliːn/ 
--
=== squalus wikt ===
57: Latin 
58-
59: Toggle Latin subsection 
60-
61- 1.1 
62- Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
69-
--
169: Latin
170- [ edit ] 
171-
172- Etymology 1
173- [ edit ] 
174-
175- Uncertain. 
176-
177- Perhaps from Proto-Indo-European *(s)kʷálos ( “ sheatfish ” ) , cognate with Ancient Greek ἄσπαλος ( áspalos ) , Avestan 𐬐𐬀𐬭𐬀 ( kara , “ kind of fish ” ) , Old Prussian kalis , and Old English hwæl ( “ whale ” ) ; more information at whale .
178-
179: De Vaan suggests that it might be related to Latin squāma ( “ scale ” ) . De Vaan proposes that the term came to refer to a species of fish based on its scales. If this theory is accepted, the term must be pronounced as squālus .
180-
181- Pronunciation
182- [ edit ] 
183-
184- If pronounced as squalus 
185-
186: ( Classical Latin ) IPA ( key ) : [ˈskʷa.ɫʊs] 
187-
188- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈskʷaː.lus] 
189-
190- If pronounced as squālus 
191-
192: ( Classical Latin ) IPA ( key ) : [ˈskʷaː.ɫʊs] 
193-
194- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈskʷaː.lus]
```


## [2026-09-14T01:59:37.845Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== PIE root ===\"; sed -n '1,6p' 9f9c11a79838ed77.txt; grep -n -A30 \"^ *Noun$\" 9f9c11a79838ed77.txt | head -60"
}
```


### [2026-09-14T01:59:38.784Z] TOOL RESULT

```
=== PIE root ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)k%CA%B7%C3%A1los
FETCHED: 2026-09-14T01:59:32Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/(s)kʷálos - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/(s)kʷálos - Wiktionary, the free dictionary 
142: Noun
143- [ edit ] 
144-
145- *(s)kʷálos   m [ 2 ] 
146-
147- large fish 
148-
149- sheatfish 
150-
151- Inflection
152- [ edit ] 
153-
154- Thematic
155-
156- singular
157-
158- nominative
159-
160- *(s)kʷálos 
161-
162- genitive
163-
164- *(s)kʷálosyo 
165-
166- singular
167-
168- dual
169-
170- plural
171-
172- nominative
```


## [2026-09-14T01:59:39.264Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== Avestan kara ===\"; sed -n '1,6p' 757ce544eda74572.txt; grep -n -i -A6 \"Etymology\\b\" 757ce544eda74572.txt | sed -n '1,60p'"
}
```


### [2026-09-14T01:59:39.331Z] TOOL RESULT

```
=== Avestan kara ===
URL: https://en.wiktionary.org/wiki/%F0%90%AC%90%F0%90%AC%80%F0%90%AC%AD%F0%90%AC%80
FETCHED: 2026-09-14T01:59:32Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T01:59:44.127Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '100,142p;175,280p' 9f9c11a79838ed77.txt"
}
```


### [2026-09-14T01:59:44.180Z] TOOL RESULT

```
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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Sometimes compared with Proto-Uralic *kala , as well as to Proto-Indo-European *kʷel- ( “ to turn ” ) . [ 1 ] 

 Noun

 *(s)kʷáloh₁ 

 *(s)kʷáloes 

 vocative

 *(s)kʷále 

 *(s)kʷáloh₁ 

 *(s)kʷáloes 

 accusative

 *(s)kʷálom 

 *(s)kʷáloh₁ 

 *(s)kʷáloms 

 genitive

 *(s)kʷálosyo 

 *? 

 *(s)kʷáloHom 

 ablative

 *(s)kʷálead 

 *? 

 *(s)kʷálomos , *(s)kʷálobʰos 

 dative

 *(s)kʷáloey 

 *? 

 *(s)kʷálomos , *(s)kʷálobʰos 

 locative

 *(s)kʷáley , *(s)kʷáloy 

 *? 

 *(s)kʷáloysu 

 instrumental

 *(s)kʷáloh₁ 

 *? 

 *(s)kʷálōys 

 Descendants
 [ edit ] 

 Proto-Balto-Slavic: 
 Old Prussian: kalis ( “ sheatfish ” ) 

 Proto-Germanic: *hwalaz ( “ whale ” ) ( see there for further descendants )

 Proto-Hellenic: 
 Ancient Greek: ἄσπαλος ( áspalos , “ fish ” ) 

 Proto-Indo-Iranian: *(s)káras 
 Proto-Iranian: *(s)kárah 
 Avestan: 𐬐𐬀𐬭𐬀 ( kara , “ kind of fish ” ) 

 Proto-Italic: 
 Latin: squalus ( “ shark ” ) ( see there for further descendants )

 References
 [ edit ] 

 ^ Kroonen, Guus ( 2013 ), “*hwali-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 262 

 ^ Mallory, J. P. with Adams, D. Q. ( 2006 ), The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World (Oxford Linguistics), New York: Oxford University Press, →ISBN , page 147 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/(s)kʷálos&oldid=92151138 "

 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European nouns 
 Proto-Indo-European masculine nouns 
 ine-pro:Catfish 
 Proto-Indo-European thematic o-stem nouns 

 Hidden categories: Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages with entries 
 Pages with 1 entry 

 This page was last edited on 23 August 2026, at 21:53.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary
```


## [2026-09-14T01:59:54.001Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== KLN whale ===\"; grep -n \"whale, n\\.\\|whale,  n\\|hwæl\\|hwæl\" KLN_1966.txt | head -10; echo \"=== KLN walrus ===\"; grep -n -i \"walrus\" KLN_1966.txt | head -10; echo \"=== KLN squalene/squalus ===\"; grep -n -i \"squalene\\|squalus\" KLN_1966.txt | head -10"
}
```


### [2026-09-14T01:59:54.116Z] TOOL RESULT

```
=== KLN whale ===
=== KLN walrus ===
18101:ors.  MDu.  ors ,  Du.  ros,  OHG.  hros,  ros,  MHG. ros,  ors,  G.  RoJS,  wich  possibly  meant  orig.  ‘the jumping  animal’,  fr.  Teut.  *hrossa-,  corre¬ sponding  to  pre-Teut.  *qru-ta-s,  participle  of  a lost  verb  meaning  ‘to  jump’,  from  a  dental  en¬ largement  of  I.-E.  base  *(s)qer-,  ‘to  leap,  jump, bound’,  whence  also  OI.  kdrdati,  ‘leaps,  hops’. See  Scarus  and  cp.  cardinal,  adj.,  and  words there  referred  to.  Cp.  also  the  second  element in  walrus.  F.  rosse,  OProven?.  rosa.  It.  rozza, ‘mare’,  are  Teut.  loan  words.  Derivatives: horse,  v.  (q.v.),  horse,  adj.,  horsy  (q.v.) horse,  tr.  and  intr.  v.  —  ME.  horsen,  ‘to  provide with  a  horse  or  with  horses’,  fr.  OE.  horsian, fr.  hors.  See  horse,  n.
24443:morrow,  n.  —  ME.  morwe,  a  collateral  form  of morwen,  ‘morning’.  See  morn.  Cp.  tomorrow, morse,  n.,  a  large  round  brooch.  —  ME.  mors,  fr. OF.  mors,  fr.  L.  morsus,  ‘a  biting,  a  catching hold,  that  which  catches  hold’,  fr.  morsus,  pp. of  mordere,  ‘to  bite’.  See  mordant morse,  n.,  walrus  —  Lapp,  morsha,  ‘walrus’.
26073:Odobenus,  n.,  the  genus  consisting  of  the  walrus¬ es  ( zool .)  —  ModL.,  compounded  of  Gk.  68cov, ‘tooth’,  and  fiouveiv,  ‘to  walk’  (see  odonto-  and base,  n.);  so  called  in  allusion  to  the  use  of  the tusks  in  walking.
28878:pinnigrade,  adj.  and  n.  —  See  prec.  word, pinniped,  adj.  and  n.  —  See  next  word. Pinnipedia,  n.  pi.,  a  suborder  of  aquatic  carniv¬ orous  mammals,  the  seals  and  walruses  (zool.) —  ModL.,  lit.  ‘having  feet  serving  as  fins’,  fr.  L. pinna,  ‘fin',  and  pes,  gen.  pedis,  ‘foot’.  See  pinni- and  pedal.
37674:Derivatives:  swapp-er,  n.,  swapp-ing,  adj.  and  n. swaraj.  n.,  self-government.  —  OI.  sva-raj,  ‘self- ruling’,  fr.  sva-,  ‘one’s  own’,  and  raj,  ‘rule’.  The first  element  is  cogn.  with  L.  suus,  ‘one’s  own’; see  sui  and  cp.  the  second  element  in  swadeshi, swami.  For  the  second  element  in  swaraj  see  raj. sward,  n.,  grass-covered  ground,  turf.  —  ME.,  fr. OE.  sweard,  swearO,  ‘skin,  rind,  rind  of  bacon', rel.  to  OFris.  swarde,  ‘skin  of  the  head'.  MDu. swarde,  swarde ,  Du.  zwoord,  ‘rind  of  bacon  , MHG.  swarte,  ‘hairy  scalp’,  G.  Schwarte,  ‘thick, hard  skin,  rind’,  ON.  svordr,  gen.  svardar, ‘skin,  esp.  of  the  head;  walrus  hide',  grassvdrdr, ‘greensward’,  Dan.  svier,  Norw.  svor,  Swed. srcl,  ‘rind  of  bacon’,  and  prob.  cogn.  with  Lett. scherwe  (fr.  *scherdwe,  fr.  Old  Baltic  *sverdve), ‘thick  skin’.  The  sense  development  of  E.  sward is  Scand.  Cp.  Dan.  grensvter,  ‘greensward  (see
=== KLN squalene/squalus ===
36468:squalid,  adj.,  foul,  filthy;  sordid.  —  L.  squalidus, ‘rough,  filthy’,  fr.  squalere,  ‘to  be  filthy’,  fr. squalus,  ‘foul,  filthy’,  which  stands  for  *sqwa- los  and  is  rel.  to  squa-ma,  ‘scale’;  not  cogn.  with Gk.  mqkig,  ‘clay’,  and  nor  with  OSlav.  kalu, ‘dirt’.  Cp.  squama.
36472:Squalodon,  n.,  a  genus  of  fossil  toothed  whales (paleontol.)  —  ModL.,  a  hybrid  coined  fr.  L. squalus,  ‘a  large  fish’,  and  Gk.  oStov,  gen. oSovtoc,  ‘tooth’.  See  Squalus  and  odonto-. squaloid,  adj.,  resembling  a  shark.  —  A  hybrid coined  fr.  L.  squalus,  ‘a  large  fish’,  and  Gk. -oel8y)c,  ‘like’,  fr.  eISoi;,  ‘form,  shape*.  See Squalus  and  -oid.
36474:Squalus,  n.,  a  genus  of  fishes  of  the  family  of sharks  ( ichthyol .)  —  L.,  ‘a  large  kind  of  sea fish’,  cogn.  with  ON.  hualr,  OE.  hwatl,  ‘whale’. See  whale.
36475:squam-,  form  of  squamo-  before  a  vowel, squama,  n.,  scale.  —  L.  squama,  rel.  to  squalus, ‘foul,  filthy’.  See  squalid  and  cp.  desquamate,  es- quamate.
```


## [2026-09-14T01:59:55.061Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== SKT ===\"; grep -n -i \"whale\\b\" SKT.txt | head -10; echo \"--- walrus\"; grep -n -i \"walrus\" SKT.txt | head -5"
}
```


### [2026-09-14T01:59:55.177Z] TOOL RESULT

```
=== SKT ===
3277:Cetaceous,  of  the  whale  kind.  (L.-* Gk.)  L,  tett,  ctfmt^^Gk.  Jrijrpr,  a  sea- monster.
10341:logger-head,  a  dunce,  a  piece  of  tira^ (in  a  whale>boac)  over  which  a  line passed  to  make  it  run  more  slowly.  (Sca^ and  E.)     A  similar  fonnation  to  bifici
12165:Narwhal.  &ea-unicorn.  (Scand.)  Dan. Swcd.  markvai;  Iccl.  nJhvair,  a  narwhal. The  lit,  sense  is  *  corpse-whale ; '  the  lish being  (often)  of  a  pallid  colour.  -•  Icel nii-r,  cor^ne  ;  Aiv/r,  whale
18064:Sperm,  spaun,  spermaceti.  (F,~L.— Gk  )  M.  E  speitnt.^V^.  spenru,  'sprim, seed;'  Cot  — L.  j/Vr»i<i.  — Gk.  tr^ipfia.^ Gk.  awtiptir,  to  sow;  orig.  to  S4.atler  with a  jerk  of  the  hand.  (y'SPAU.)  Der. sptrm-atic  (Gk.  ffwrp/ianiriii);  ipfrvioidi, L.  sp^t-ma-cetit  i.e.  spcnn  of  the  whale;  sec C«tnoeoua.
21331:WHALE.
--- walrus
21174:Walrus :  see  Wlusle.
21353:walrus,  a  large  seal    (Du-  -  Sc«AN^ Du.  iL'a/mj.~S^^.  vallrQ3s,\>axv.  KvaUos^ a  monc;  Uv  a  *  n4\vo.\«-\vo^«  \    vVt^axa*. as  A.  S,  hort-kwoX^  %  xnoi^fc,  Vomft-^i
```


## [2026-09-14T02:00:04.989Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== KLN whale entry ===\"; grep -n \"whale\" KLN_1966.txt | grep -i \"hvalr\\|hwael\\|hwæl\\|ON\\.\" | head -5; echo \"--- try 1971\"; grep -n -i \"whale, n\" KLN_1971.txt | head -5"
}
```


### [2026-09-14T02:00:05.079Z] TOOL RESULT

```
=== KLN whale entry ===
4321:base  *bhel-,  ‘to  swell’.  See  ball,  ‘a  round  body’, and  cp.  Balaena,  balinger. balefire,  n.  —  OE.  bielfyr,  ‘funeral  fire’,  com¬ pounded  of  bxl,  ‘a  blazing  fire,  a  funeral  pile’, and  fyr,  ‘fire’.  The  first  element  is  rel.  to  ON.  bdl, ‘a  great  fire’,  fr.  I.-E.  base  *bhel-,  ‘to  shine’;  see bald.  For  the  second  element  see  fire, balinger,  n.,  a  whaleship  ( obsol .)  —  OF.  balen- gier,  ‘whaleship*,  fr.  baleine,  ‘whale’.  See  baleen, balk,  also  baulk,  n.,  ridge  of  land  left  unplowed between  furrows :  a  beam.  —  ME.  balke,  ‘beam’, fr.  OE.  balca,  ‘ridge  between  furrows,  beam, rafter’,  rel.  to  OS.  balko,  ON.  bjalki,  Dan.  bjelke, Swed.  bjdlke,  OFris.  balka,  OHG.  balko,  balcho, MHG.  balke,  G.  Balken,  ‘beam,  rafter’  (cp., with  vowel  gradation,  OE.  bolca,  ‘wooden gangway  of  a  ship’),  ON.  bolr,  ‘trunk  of  a  tree’ ; fr.  I.-E.  base  *bheleg-,  ‘beam,  plank’,  whence also  Gk.  tpaXzy?,  ‘trunk,  log;  line  of  battle, battle  array’,  cpaXtoit;,  ‘beam’,  L.  fulcire,  ‘to prop’,  fulcrum,  ‘bedpost’,  Lith.  balziena,  ‘cross¬ bar’,  Lett,  bdlziens,  ‘prop,  stay’.  Cp.  balcony. Cp.  also  block,  bole,  ‘trunk’,  bulk,  ‘projection’, debauch,  ebauchoir,  fulcrum,  phalange,  phalanx, planch,  planchet,  plancier,  plank.
5831:bull,  n.,  the  male  of  a  bovine  animal.  —  ME.  bule, bole,  fr.  OE.  bula,  ‘bull’,  rel.  to  ON.  bolt,  MDu. bul(le),  Du.  bul,  G.  Bulle,  of  s.m.,  OE.  bulluc, ‘little  bull’,  bealluc,  ‘testicle’,  ON.  bollr,  ‘ball’, fr.  I.-E.  base  *bhel-,  ‘to  swell’,  whence  also  Gk. 9«XX'j?,  ‘penis’,  cpxXXaivx,  oocXXt; ,  ‘whale’,  L. follis,  ‘a  pair  of  bellows’.  Cp.  bullock.  Cp.  also baleen,  ball,  ‘a  round  body’,  bold,  bulk,  ‘size’, follicle,  phallus.  For  derivatives  of  base  *bhelgh-, an  enlargement  of  base  *bhel-,  see  belly,  bud¬ get,  bulge.
14897:flench,  flense,  flinch,  tr.  v.,  to  strip  the  blubber from  a  whale.  —  Dan.  flense,  of  s.m. flesh,  n.  —  ME.  flesch,  fr.  OE.  flsesc,  rel.  to  OS., OFris.  flesk,  MLG.  vlees,  vleis,  Du.  vlees, OHG.  fleisc,  MHG.,  G.  fleisch,  ‘flesh’,  ON., Dan.  flesk,  ‘pork,  bacon’.  The  ultimate  origin of  these  words  is  uncertain.
17253:harper,  n.  —  ME.  harpere,  fr.  OE.  hearpere,  fr. hearpe.  See  harp,  n.,  and  agential  suff.  -er. harpings,  n.  pi.,  the  stout  wales  round  the  bow of  a  vessel  ( naut .)  —  Rel.  to  harpoon, harpist,  n.,  a  harper.  —  A  hybrid  coined  fr.  harp and  -ist,  a  suff.  of  Greek  origin, harpoon,  n.,  a  barbed  spear  used  against  whales, etc.  —  Fr.  earlier  E.  harpon,  prob.  fr.  Du.  har- poen,  fr.  MDu.  harpoen  (whence  also  earlier  G. Harpon,  G.  Harpune),  fr.  OF.  harpon,  ‘clamp, grappling  iron,  harpoon’  (whence  F.  harpon, ‘harpoon’),  fr.  OF.  (=  F.)  harpe,  ‘claw’,  fr.  OF. (=  MF.)  harper,  ‘to  seize,  grapple’,  which  is prob.  of  Teut.  origin.  Cp.  ON.  herpask,  ‘to  con¬ tract  (one’s  fingers)’,  and  see  harp.  F.  harpon was  influenced  in  meaning  by  an  association with  Late  L.  harpe  (fr.  Gk.  ap-nri]),  ‘sickle’,  with which,  however,  it  is  not  connected. Derivatives:  harpoon,  tr.  v.,  harpoon-er,  n. harpsichord,  n.,  a  keyboard  stringed  instrument, forerunner  of  the  piano  (mus.)  —  Earlier  harp- sechord,  fr.  obsol.  F.  harpechorde,  fr.  It.  arpi- cordo,  which  is  compounded  of  arpa,  ‘harp’,  and corda,  ‘string,  chord’.  See  harp  and  chord, harpy,  n.,  1)  any  of  several  rapacious  monsters  in Greek  mythology;  2)  a  rapacious  person. —  F.  harpie,  fr.  L.  harpyia,  fr.  Gk.  apmjiott (pi.),  lit.  ‘snatchers’,  which  is  rel.  to  apin'], ‘sickle’,  aprox£eiv,  ‘to  snatch,  seize’,  apira-fr], ‘hook;  rake’,  ap7ra*;,  ‘rapacious’,  prob.  fr.  I.-E. base  *srep-,  *sfp-,  ‘to  seize,  rob’,  whence  also OSlav.  srupu,  ‘sickle’,  Russ,  serp',  Lith.  sirpe, of  s.m.  Base  *srep-,  *spp-  is  prob.  rel.  to  base *rep-,  whence  Gk.  £p£7rre<jffat,  ‘to  pluck  off’, L.  rapere,  ‘to  seize  and  carry  off  ’ .  See  rapid  and  cp. sarmentose.
24990:narwhal,  narwal,  n.,  an  arctic  whale  with  a  long spiral  horn.  —  Dan.,  Norw.  narhval,  or  Swed. narval,  metathesized  fr.  ON.  nahvalr,  lit.  ‘corpse- whale’,  fr.  nar,  ‘corpse’,  and  hvalr,  ‘whale’ ;  prob. so  called  in  allusion  to  the  whitish  color  of  the skin.  ON.  nar  is  rel.  to  OE.  ne,  neo,  Goth,  naus, ‘corpse’,  and  cogn.  with  OCo.  naun,  OSlav.  navi, OPruss.  nowis,  ‘corpse’,  Lett,  nawe,  ‘death’, Lith.  novyti,  ‘to  torture,  kill’.  For  the  etymology of  ON.  hvalr  see  whale.
--- try 1971
266288:whale, n. — ME. whale, whal, fr. OE. hwxl, rel.
```


## [2026-09-14T02:00:06.759Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== IEC ===\"; grep -n -i \"skʷalo\\|squalus\\|sqalos\\|qalos\" IEC.txt | head -10; echo \"=== WLD band3 ===\"; grep -n -i \"squalus\\|hvalr\\|whale\" WLD_band3.txt | head -10; echo \"=== SYN ===\"; grep -n -i \"squalus\\|hvalr\" SYN.txt | head -10"
}
```


### [2026-09-14T02:00:06.927Z] TOOL RESULT

```
=== IEC ===
=== WLD band3 ===
=== SYN ===
```


## [2026-09-14T02:00:10.269Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '266285,266300p' KLN_1971.txt; echo \"=== walrus 1971 ===\"; grep -n -i \"^walrus\" KLN_1971.txt | head -3"
}
```


### [2026-09-14T02:00:10.361Z] TOOL RESULT

```
Derivatives: whack, n., whack-er, n., whack-ing, 
n. and adj. 

whale, n. — ME. whale, whal, fr. OE. hwxl, rel. 
to OS. hwal, ON. hvalr, hvalfiskr , Swed. val, 
MDu. wal, walvisc, Du. walvis, OHG. wal , 
waif sc, MHG. wal, wal vise h, G. Wal , Walfsch, 
‘whale’, G. Weis, ‘shad’, and prob. cogn. with 
OPruss. kalis, ‘shad’, and prob. also with Finn. 
kala, ‘fish’, L. squalus, ‘a kind of sea fish’. Cp. 
walrus and narwhal. Cp. also rorqual, Squalus. 
Derivatives: whale, intr. v., whal-er, n., w hal- 
er y, n., whal-ing, n. 

whang, tr. and intr. v., to strike, blow; n., a 
strike, blow. — Of imitative origin. Cp. bang, 
=== walrus 1971 ===
264725:walrus, n. — Du., fr. Swed. vallross , fr. ON. 
266295:walrus and narwhal. Cp. also rorqual, Squalus.
```


## [2026-09-14T02:00:12.644Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== IEC qalos ===\"; grep -n \"alos ‘\\|kʷ\\|qualus\" IEC.txt | head -5; echo \"=== IEC squalus ===\"; grep -n -i \"squal\" IEC.txt | head -10; echo \"=== WLD whale ===\"; grep -n -i \"hval\\|Walfisch\" WLD_band3.txt | head -10"
}
```


### [2026-09-14T02:00:12.810Z] TOOL RESULT

```
=== IEC qalos ===
2305:diuios ‘heavenly, divine, wonderful, strange". Cf. diu-, etc. Skt. divyáh; Arm. cf. tir, tiwr “god, idol; Myc. diwijo-; Gk. díios, dios; Lat. dius, beside divus, a *god'; MIr. diadha; OW dydd, pl. diew ‘day’; W dydd; Cor. deih, dyth, jeth *dze-, d: OCS divij, adj., divija, s. ‘wild; wildness; OCz. diví ‘wonderful’; Li. cf. dývas, usu. pl. d$vai ‘monster, wonder’; Late cf. dīvains ‘strange’. Derivative forms: Hes. díalos ‘bright: Br. déol, W duwiol ‘divine’ fr. *diuiolos. Further: Lat. divinus; Cz. divný ‘strange’; Li. dývinas, id. fr. *diuinos
4574:ghalo, ið (3) ‘shout, howP Gk. cf. trá-khëlos, Dor. -khalos ‘throat; ON góla *howl; OCS cf. galinü “cockerel'; galica “jackdaw: R cf. gal-dét ‘brawl; Ukr. cf. hala-burda ‘uproar’; hal-ajko ‘brawler’
4626:OBr. gabl ‘fork’; W gafl, id.; Br. gaól, gavl “fork, spit' (Celtic LW in G Gabel, etc.); OHG gëbal, MHG gëbel ‘head, skull, gable’; Du. gevel *gable-end'; Slovene žebelj "nat" (A variant of type *ghebhor- arises in Ir. geabar *arge-headed fish’, cf. Gk. képhalos ‘mullet’, and in Latv. Zeburs ‘two-pronged fork") (ghebholos (2) *piece' in OE geofola, giefel *morsel'. See gabholos and cf. WP I, 571) ghed- “acquire; acquisition'. Cf. ghnd- and WP I, 589 Oss. zíd, zudà (‘greedy fr. *ghedu-, *gheduo); Lat. cf. -da (for *-heda in prae-da ‘booty’; hedera ‘ivy’, fr. a neut. pl. *ghedeso; and helluo (?) ‘glutton’, if for *ghed-leuon, see leu-); OE gietan ‘get; ON geta, id. beside geta, f. ‘guess’; MHG -gezs- in a-gezzel "Tor, getful'; er-gezzen ‘forget; (*-6- in) gæze, adj. ‘greedy’ and ON gæta ‘watch, heed', ON gáta ‘riddle’, Sw. gåta, id. and apparently *-0- in Cz. zá-hada, id.; OCS cf. Zadati ('desire', if distinct from ZeZdo, Zedéti, id. See ghnd- and cf. OCz. žádný *beloved") (*-e-); Li. gedáuju, -auti ‘desire’. Uncertainly Alb. gjuej, gjuaj ‘hunt beside gjojé, f. ‘hunt’, fr. *ghed- (cf. the LW rruej, rruaj ‘shave’ fr. Lat. radere). Cf. ghend-. Alb. gjej “find, guess? is ambig. A desiderative form of type *ghedsio occurs
5341:guóuolos (guəuəl-) “head of cattle; bull, ox, buffalo". WP II, 112 Skt. golah ‘bull’; Hind. gaur ‘wild bull, bison’; Oss. gal ‘ox; bull; Gk. boübalos ‘buffalo’; Lat. (LW fr. Gk) bübalus, id., beside It. (from Umbrian) bufolo, id.; MIr. büáaball, id.; W bual, id. (both fr. Lat. but cf. also Ir. bólach, bólacht, bualacht ‘livestock’, fr. *guouol-a$-
7602:kondulos, å ‘knob, lump, bump, gnurl, knot’. (Variants: kundəlos, kondol-, kondəl-). WP I, 390. Cf. kondos Skt. kandalah, à, am (“cheek, jowl’; m. ‘gold nugget’); kandalam (also ‘plantain flower’); Gk. kóndulos "kouckle bone, fist; kondúle “lump, bump’ beside kúndalos ‘peg’; OCS kọ- deli, f., Pol. kadziel ‘distaff; distaff-ful of flax’; R: kude? ‘hemp; distaff-ful’; Slovak kude? & kudla, f. ‘topknot, knot of tow, hair or fibre’; Cz. koudel, id. & kudla; Li. cf. kanduolas ‘kernel’; Latv. kodols, id. beside kodaļa ‘dis- taff-ful’. The background of G Hanteln (LG ?) ‘dumb-bells’ is obscure.
=== IEC squalus ===
1843:bhū- (2) ‘howl, gale, blast. Cf. bhübh- Arm. bu (o-st. 'owl) beside buk, pl. form “gale, storm’; Per. cf. bü timàr ‘heron’; Phryg. or Mac. büza ‘owl’; Du. bui ‘squall’; cf. Lat. butio and MIr. bufa (‘bittern’, fr. *bhuuo-). Sw. rágn-by (LW < Du.)
3869:Li. gagü, eti. Cf. *gagaio in Blg. gagam; Latv. gagaju, id. gagos (gaglis) ‘knob, lump, berry’; as adj. *lumpish, boorish’ Alb. gogël “berry, oakapple'; gogé ‘boorish’; Sw. koka (&clod'. Ambig. cf. gogos); Li. gõgas ‘Jump, hump; withers’; Icel. kaekur, m. (' vice. Mod. -æ- for ON -ce-) gāið (1) ‘croak, caw'. WP I, 526. Cf. gauið, gouo Skt. gāyāmi ‘sing’; cf. G kaien ‘prattle’; keien “blub, weep’; OCS gajọ, ati ‘croak, caw’ gāið (2), see gígāmi gàios, à (1) “raucousness, cawing; jay, mag- pie, or other raucous bird’. WP I, 526. Cf. gaio (1) Skt. gayah ‘song’; Arm. čaj, Lat (jay, with induced palatalism); Lat. gaius, gaia “jay, mag- pie; G (short vowel) Kai ‘prattle’; Norw. Sw. Scots kaja, kaie, kae ‘jackdaw’; E caw; R gaj ‘caw’. Cf. Ukr. Zaj-voronok Clark fr. *gēi-); Pol. ga-wron, Cz. ha-vran ‘raven’ gaios, om (2) ‘pace, gait'. Cf. gígàmi, ghàio. WP I, 526 & 677 Skt. gayah, adj. ‘striding’; Av. gàyom ('pace', also 'yard-measure)); (ambig.) Cz. hej-no, OCz. hajno ‘flock’; (ambig.) cf. Li. góju, son ‘amble, wade’; Latv. (ambig.) gāju Cl went, but Arm. gaci, id. is fr. ghai-, q.v.); cf. also gājums ‘gait, track’; gājējs ‘pedestrian’ galdāið, galdeio ‘bawl, exuit, howl’. Skt. gardāmi, Av. garəd- (1); Alb. (denom.) galdoj ‘exult’; Lat. gallo, are (‘rave���, but poss. denom. of gallus, cf. gagol-); MHG kalzen, kelzen *bawl'; kelz “loud talk’; OFris. kaltia “talk”; Du. kouten chat": kout, s. id.; R. cf. galdét ('brawl', but the phonol. is irregular) galið *shout'. Cf. gald-, galu- Gk. cf. a-gállo ‘glorify’; MHG kallen ‘shout, chatter, sing, croak’; Du. G kallen ‘chatter’; LG kohlen, id.; Tirol. kallen ‘bellow, rut; OE ceallian: ON kalla (“calP', etc.). Cf. also Alb. galé ‘rook’; Br. gal-dü “black sea-bird"; OE -calla *-crier'. (Ambig. or variant in Skt. járe, Av. jar- ‘creak, rustle; call’, cf. &el-) galuó ‘call’. Cf. galið, gald-; galuos, s. Skt. cf. garvah ‘pride’; Br. galv ‘appeal’; W galw ‘call, vocation’; Ir. (?) gailbh ‘squall’;
6426:ieuros (ieuruot-?) ‘filth’. Cf. ouros . Gk. cf. eurós, gs. eurótos ‘decay, squalor, mould"; Li. jáuras, -a, m. f. ‘swamp’
6904:käng, ið (kou-, kāu-, kü-) (1) “strike, hew’. WP I, 330. Gk. etc. ambig. Cf. Káu- Av. cf. fra-kava ‘fight’; apa-kavo ‘warrior’; Per. kavam, inf. kavidan and kaftan ‘dig’; Tokh. A ko-, B kau- 'strike, kil; Pelasg? cf. Ká- beiroi (/émetalworkers of Vulcan! fr. *kau-uiroi (?), see uiros); Gk. cf. kaunós “lot, fate’; Ir. cf. caibe 'spade-blade, blade of hoe’; Br. cf. kawad, f. 'surprise-attack'; W cawod ‘shower’: Cor. cowas ‘gust, squal; OHG houwan, OE
9336:Arm. šujt, gs šuti, abl. -av 'swift'; OE hwipu, f. (squall?, but, with OE hwióa, wm. ‘breeze’ possibly as here, with onomat. basis); ON hvióa, f. (gust', but see Kuit- (2)); Li. cf. švy- trüs, adj. (swift
15280:seubð, ið ‘fume, pant, gasp’. Cf. seu- (séu-) above, and WP I, 502 Arm. (ambig.) hevam, v. ‘pant’ beside hivand ‘sick’; G cf. seufzen, v. (sigh. FK:EWDS untenable); Li. siaubiü, ti, v. ‘fume, rage’; siaubas, m. ‘fury, squall’. See next
15282:seuros, à “mixture, mess, filth, urine’. Cf. leur-, iour- Gk. (ambig.) eurós, gs: eurótos, n. *mould, decay, squalor’; Per. cf. Sür, s. ‘stir, tumult’; Hitt. cf. sehur, gs: sehunas, s. ‘urine’; Alb. shurrë, f. id.; (o-gde in) ON saurr, m. ‘mud, excrement
16751:soutos, iə, us ‘surge, seethe; surging, boil- ing’. Cf. seuto, ið Skt. sótuh, m. ‘soma-pressing; soma-libation'; Go. saups, m. ‘sacrificial offering’; MHG sot; MHG sot gs: sodes, sm. & n. “boiling, brew'; OE (queried) seaóa, m. ‘heartburn’; cf. G Sod-brennen, id.; OE séap, m. ‘spring, sour- ce’; ON seyðir, m. pl. ‘cooking-fire’; Pol. suty, adj. 'abundant' ; Ukr. sutyj, id.; Latv. saute, f. 'fomentation, scalding, steeping’; Li. cf. siau- tis, gs: -Cio, m. ‘squall’ beside (z-gde) siütis, gs: -Cio, m. ‘rage’
17039:sphótåmi, id.; Romani cf. phuterav, tr. “break, burst’; Arm. prt'im, prt'anim, v. “break loose, snap off (fr. *sphurst-). In the examples that follow, initial squ- may alternate with qus- in some instances: squábh- ‘limp, soft, feeble, faulty. Cf. qusabh- EME squab, s. “young bird; sofa, soft cushion’; Sw. cf. skvablig ‘feeble, limp’; G cf. schwabbeln, v. ‘dangle’; Cz. (long-gde) chabý, adj. ‘feeble’; chabnouti, inf. ‘faint’; chabiti, inf. ‘enfeeble’; OCS xabljo, xabiti, v. ‘corrode, weaken’. Extended variant in Gk. psapharós, adj. ‘dry, brittle; squalid’; cf. the senses of Cz. chabí, chabdi, n. ‘brushwood’ and chabý, chably, adj. ‘feeble’; R po-xabnyj, adj. ‘ribald, vulgar’: Sw. skvablig, adj. (2) ‘nauseous’ squal- (1) ‘brawl, shout G Schwall, m., usu. Wort" ‘spate of words, bombast’; ON skval, n. ‘braw?!’ beside skvala, v. 'brawl; E (fr Norse) squall, id. and ‘sudden storm at sea’; Sw. skvaller, npl. ‘twaddle’; OCS (long-gde) xvala, f. ‘praise’, (& com. SL). (NB. Slav initial xv- appears to be an intensive variant of initial x-) squàál- (2) ‘dirty; dirt Lat. squàlus, adj. ‘dirty’ beside squalor, s. ‘dirt’; OCS xala, f. id.; Srb. håla, id.; Big. cf. xàla, f. ‘monster; horror’; R na-xal, m. ‘lewd one’. (Ehrlich here, despite WH 3) squăr- (qusăr-); squars- (?) Lat. squarra, f. ‘scab, roughness of skin’; cf. Gk. psarós or psārós, adj. ‘drying’; as s. ‘drying-powder’; Cz. cf. chrásta, f. (‘scab, mange’, if fr. *squarst-) squat- (?) “a fish" (qusåt- ?) Lat. cf. squatus, gs. -1, m. (mulleť or sim.); Gk. cf. psétta, f. ‘turbot
=== WLD whale ===
```


## [2026-09-14T02:00:17.783Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n -i \"hvalr\" IEC.txt | head -5; echo \"--- qualos/qalos\"; grep -n \"qualos\\|qalos\\|qualis\\|kalis\" IEC.txt | head -8"
}
```


### [2026-09-14T02:00:17.859Z] TOOL RESULT

```
9225:leuo “stir, shake’; sálos, m. ‘surge’, cf. Hes. salós, adj. ‘silly’; OE cf. hwall, adj. ‘dashing’; hwelan, sv. 4 ‘rage, roar’. (Isophonic: OHG hval, m., G Wal, OE hwal, ON hvalr, pl. -ar & -ir, m. *whale'. DW in Finn. valas)
13874:qualos, is 'sea-monster' Av. karð, m. ‘chief of the fishes’; Ir. cail, f. ‘brown trout; hag’; OHG hwal, OE hwæl, ON hvalr (pl. -ar & -ir), m. ‘whale’; OPr. kalis, id.; (LW in Finn. valas, id.)
--- qualos/qalos
5446:gurus, gurus ‘solid, heavy’. WP I, 685 Skt. gurúh ‘heavy, severe, big, venerable’; gur- vinth, adj. f. ‘pregnant’; Av. gouru-, cpds.; Arm. cf. krem ‘carry, bear, suffer’; Alb. eur ‘stone’; Gk. barüs (&heavy', etc.) beside ém- bruon ‘embryo’; Lat. cf. R-gde grăvis beside gravida, f.; MIr. brú, W bru ‘belly, womb’; Go. kaúrus ‘heavy’; Norw. kry ‘proud’; OCS gyrja, R girja ‘weight’; Li. cf. gurv-uolis ‘clod’; Latv. cf. dzir-kalis ‘stone-cutter’. An OLat. rustic type seems to be represented in barð, -Onis (*dolt. ‘Gmc. or Gallic for Ainsworth 1736) and in barrus ('elephant.. ‘Sabine’ for Ains- worth. See WH:LEW, 3, p. 97)
6213:-ilis, adj. extn. of quality Alb. cf. í vogël ((small', fr. *suagilis or *uag(h)-); Lat. cf. qualis, tālis, gracilis, habilis, etc.; OCS cf. koli, tolí “how much, so much’: Latv. cf. svilis (“red pig’, cf. Lat. suile 'sty^)
6677:kalos (2) ‘sagacious’. Variants: kalios, kalis. Cf. WP I, 356 l Skt. kalyáh “fit; clever’; Gk. cf. peu-kálimos ‘sagacious’; Lat. callidus ‘wise’ (-11- unex- plained); Umb. kalefu- ‘tame, of oxen’; W call ‘wise, sly’; Cz. cf. ne-kolný ‘stubborn’
7617:konkolos (konkól-, konkl-) ‘knob, head, tip’. Cf. kunkol-. WP I, 401, 445 Skt. kankolah (a plant); Per. (ambig.) kangar ` ‘artichoke’; kangare ‘pinnacle’; Lat. concula ‘distaff; W congl ‘corner’; cf. conglog ‘two nuts joined’; Li. kañkalas (“bell-clapper-, pl. “testes?); kankolas ‘dumpling’; Latv. kankalis ‘clod’ fr. Li.
9793:ligo (ligsKó) level, smooth, equalise'. Cf. ligos, and cf. WP II, 712 Arm. cf. hykem (smooth, level, fr. *en-lig-); Ir. líogaim “smooth, polish’; OS Itkon, denom. ‘please’; MHG lichen, wv. ‘smooth, polish’; OE hoan ‘please; suffice; liken’; ON líka ‘smooth, polish; please’; Li. lygstu, lygti come to terms”; Latv. ligstu, ligt, id.
13872:quāl- (quālis, os) “of what kind; sort, kind’. WP I, 521. Cf. quà Skt. kaláh ‘due season’; Gk. cf. pēlí-kos, adj. ‘such, of age or size; Lat. qualis "of what kind’; MIr. Ir. cáil, f. “quality, quantity”; Cz. kaly ‘good, superior, of quality? hence ne- kaly ‘sinister’; Latv. (?) kals, m. (‘bundle of 30 pieces”, lit. *quantity'?). (Isophone: Li. kol, adv. ‘as long as"). Cf. Li. kólyti, inf. “praise?
13873:quàalinos ‘clayey, muddy’. Cf. qualos Gk. pélinos, id.; OCS kalínü, id.; Cz. kalny ‘muddy, filthy’ and com. Sl.
13874:qualos, is 'sea-monster' Av. karð, m. ‘chief of the fishes’; Ir. cail, f. ‘brown trout; hag’; OHG hwal, OE hwæl, ON hvalr (pl. -ar & -ir), m. ‘whale’; OPr. kalis, id.; (LW in Finn. valas, id.)
```


## [2026-09-14T02:00:19.135Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== WLD band3 index (kalis/skualos) ===\"; grep -n \"kalis\\|skṷalo\\|squalus\\|kara\" WLD_band3.txt | head -15"
}
```


### [2026-09-14T02:00:19.188Z] TOOL RESULT

```
=== WLD band3 index (kalis/skualos) ===
42:I, Indiseh. jtindisch unbeseichnet. Buchstabenfolge; a, 4, i, f, 4, ii, i hb & af 2, ma; E, th, og gh, me Ch, Jy ah, Arh, bh, d, dA, wy t, fh, d, dh, oy; p, ph, b, BAL mw: #6 epg és k a- (Augment) 96. cayman 3, anadeah- 192, a-, an. BOO", ayra-b 1, onah ,Lastwagen* 12. ant. ajrea- 37. oniigas. 38, conga 128, avlicati 60, andgha ved. 62. amsadhrl (69). anjali-h 34. , dritrita-h 24" ccm 62. a anes ee ton 60). ‘aida 26. a i n> (bedi iP fa eal smalnyit= A | amhod abl. 2. mt hitaco pali 185. dnike- 126, 169, dkara- S68, dod-d 187, 160. amu he, ne arash 0 “ida ue 89, anurdrase BH7, @ Nacht* Sos". afati 41, anipda. di, altu- 308". diah 43, 99. persis ondpd 385", akrd- ved. 28. ati 42. | and 127. akdd-  Wirfel* 169. wikarca, -kidew 447, dnta-h 67, difa- ,Achre* 47. atiu-: (315*), antdr, antare- 196 akdate- S05. atiréis- 396". dntara- 67, eat 10, dtka- iH contertpa 46 tkdipat ved. 169. aid, ati 44, dati 65, . dibiy- 326", atha 67. anlika- 65. aga- 3, athari 45 Anm. 1. dutya- 67. ram. 5M). itharnans 43, a 45. E aly cndhd- 1#2. BS. andhati me 150), 3 ri
47:tbhitah of, alasd- 152, aefha 155. abiiddsats B14, aldtoim BA. asmitn 320°. athibhavatt (136°). alikd- (157). dam 160. cbjieditas 213, veep alpake- $12, cayutt 134. abhinlag- 272, aara~ 12 aap (11), 2b arfoun 378", acatt ,werkt ayf 17 dif veo, 115. mir ak Fait 19, (22). dha $8. ahém 115, ati 4. ifr (6), 5 ea meh ayora- SN] ane, ano 115, avir 13. ahima ved. 62. dirara ,inferior® 13, aha 52 rai" » westlich* 15. : san” 50, 95, Befriedigung* 19 a (bervorb.) 99, dou Forder +94. Baueraty 1, 16%. nai 461". aon ooo, araskara-fi hT3*. dikhu- 39D. akand-A 552", | itea- 582. avast! ,unten* 13, 604". agas- BS ardgidf ,weatlich von" 15. nite SH) ard $3, 15, fijyam 181, dvdta- (211). dja hindi, beng. 85. ari-- 167. iuthrd- (37 Anm, 1), aritcr= 1). hi - Beinteil fiber dem arare avirrjiia- IBS. Knie* 70, 167. orale dis. acy 157. at 99, ari- .aehr* 69, dtrodantes .chwankten* 273, d@idngona-m TZ.
380:JL. Armeaiachs, ere — karayi
2652:diolas oatlit. dial. 83 tinarre lit, 334* : itnakas lit. 470*. ak. wiviburyti Lit, 191° STG. acta Brsepueerty edly, wisu, vist lett. 214 vibalas lit, 255. fae erat ad védaraa lit. (111), Li), taddott wdara lett, (111), dots Lit; 216, vedena lit. 285. soda It Fr rede alt 1. ial ci aE By — - reigis ris i. 310. ag vedinfi lit. 222. ane Pie nae iu it, (17), 220. toaldét lett. 213. ere eee raijal lott. 213. wk lit 29), caine Iott. oo). = Lit. 239 eajéju, ti lit, 230 ize le val, a in # lit. 240, eesbti, werkt it, on, 235. innit, “itt lit lit. a ir i ae on veikiss lit. 235, ® ks S14. veislics, wialivs lit: 242. | va veri¢ lit. 287. wajt wit i nieehan® Snags i fit. 264. s OHA legen" lit, 290. tikarae lit, 15, S11. iy lese (311) fal Lit. 207. eerattetts om lit. 303 velde, eeldre lett. 309. valinda enidadi lit. 210 celdu, veldéti lit. 210. coldad, veald jad elled, v2 Lit. 308. walgie Tit NG wide lit. 805. ee ier de allt. 301. i 205. vale lit. 295. vedi, ein lit. 306. ‘ee Iott. 306. vel lit. 205: er payt energie tasty err a relia, «9h “4 voletiue Lit. 210. reltay lit. 208, voles lett. 210. eélfin, -wo lit, BOS. odlicg Lit. 207, TO3, veluabas alit. 305. oompli ot er hy roe volts lit. bees ” oeeN “Be it. cermin, olmfi Lit. rn ay oe 219, Hi + ‘hi fa range, tangas lett, 219, sander et hr Bis nt wa otens lit. 240 fee] it. 2 it. 240, Soa 4it hit, 217, (258).  Vapriaé lit. 121. varanda a 2ikt. repris lett. IPI. tofdas lit. 289 eerba lit. S75. vores lit. 320. verbiu, werbti lit. 276. vargice lit. cerca, weratd Ht. 275.
2827:210 KVL Slavisch,. bryjo, bryti — lopata cy kryte dia. kypre 3 russ. 477 kyadls krzealo poln. kyeati éech. 376 brida nsorb. 585* fibati ekr. 384" keiati Seoh. 470, lolvizha ross. 386". Tusa, 37 Inbid eerb. 09 kibart rasa. 375. lobdz kir. 24" buibéis rosa, 375. lack kiruss. 420°, 440°, . a kubdes russ. 375. lachéns russ. 420,* 440%. [akors russ.-kel. 903.. Libé russ. 375. jada, lado éech. 438°. [493 obg. (90 Anm. 1), 04°. kilboke rues. 376. iy dija ko fet poln. 457°. waka ruse. 275. th } Ielfo rosa, 372. inigera russ. dink, 372 idhi ruse. o72. kudd ruse, 771. kids russ. 378. hiika ross. 371. kbkara wkr. 371. bdkafs ruse. 331. kukevice hulg. 467. kukonoss rusa,-kal, $71 kukokily kir, 331 ivkiida ross. 467 neniraey bulg. 331 1. 430". Ihility kir. 371 . 420° kuly ruse, 432 tw kin serb. 468. laskaja, -i 387", likornti Lit) bund ruse. (068), 378. lasko-sérdyj Truss. 387*. ike 1. lunind ruse. 350, losordis rusa. 3877- like ruse. 306*. it] ldeq} russ. 387%. lint, Tusa. 36H". dihe rosa. 382". lipa russ. 404". latarh, fatann kel. 352°. Pasd kie. 308, Idea russ. 407. lidin 3H7*. lds «kr. (426°). Pit’ kl, 428%. lasing rues. (428)*- lifomeja ross. 164. lasnem slr. 4019. Vityty kir. 428°. loéa, i 4565". Habs, Iyubiti 410". Lidge kal. 436°. udine 416°, Lika 435* fiudaje 416". loka 435° be i russ. 376* lebedd ruae. 03. s ida rosa, 276° lebeds. 03. pute 216", fede 425°. i aie ae 405". i¢ russ. 427" tral r. 405". te nee 377", hiEa, lesati OL". lelet poln. 377%. thad wrues, 380° lalja rune.-kal. 377". lobed poln. 354 janis ari” fobs russ. 418* Fell pate, ary earh. STG*. loiazott a4" lemedy kal, 434". loéu, lokati kel. 380* mid osorb. 434%. Iéchma mas. 420", 440° lepécha ruse. 490°, ® kel, 202". lepént russ. 430°. lokoty rusk. LOT lépesta. rua, 4307. diva nboly. 380" lepetdty rosa. 420°, foky 3h0". IniziniE poln. 430°, Jorn!’ ja, lomiti 404° rt loaf Berk. #4 ruse. oni & i ganda SM. lone L5G, | letina rosa. dial. 161. landr ekr. 425°.
```


## [2026-09-14T02:00:32.997Z] TOOL CALL #39: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%DA%A9%D8%B1%D9%88/\" \"https://vajehyab.com/dehkhoda/%DA%A9%D8%B1%D9%88\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 458, Persian karv کرو 'a kind of fish' — Dehkhoda/Moin lookup\"; done"
}
```


## [2026-09-14T02:00:33.475Z] TOOL CALL #40: Bash

```json
{
 "command": "sed -n '1,50p' tools/ref_page.py"
}
```


### [2026-09-14T02:00:36.045Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/010de82e17b1073b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/38519e9e601e02cd.txt
```


### [2026-09-14T02:00:36.141Z] TOOL RESULT

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
```


## [2026-09-14T02:00:39.857Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== abadis کرو ===\"; grep -n -i -m40 \"کرو\" 010de82e17b1073b.txt | head -30; echo \"=== status ===\"; sed -n '1,5p' 010de82e17b1073b.txt; sed -n '1,5p' 38519e9e601e02cd.txt"
}
```


### [2026-09-14T02:00:39.947Z] TOOL RESULT

```
=== abadis کرو ===
4:TITLE: کرو - معنی در دیکشنری آبادیس
6:کرو - معنی در دیکشنری آبادیس 
10: کرو
16: کرو. [ ک َ رَ ] ( اِ ) پرده سفیدی را گویند مانند کاغذ که عنکبوت سازد و در آن تخم کند و بچه برآرد. ( برهان ) ( آنندراج ). کره. کری. ( جهانگیری ). نوعی از نسج عنکبوت. ( فهرست مخزن الادویه ).
17: کرو. [ ک ُ ] ( اِخ ) نام یکی ازخویشان افراسیاب و او در کشتن سیاوش سعی بسیار می کرد. ( برهان ) ( آنندراج ). گرو. رجوع به گروی زره شود.
18: کرو. [ ک ِ رَ / ک َرْوْ ] ( ص ) دندانی را گویند که میان آن تهی و کاواک شده باشد. ( برهان ) ( آنندراج ). دندان نیم ریخته. ( فرهنگ اسدی نخجوانی ). دندان میان تهی و کاواک شده و شکسته و ناهموار. ( ناظم الاطباء ). کروه. ( حاشیه برهان چ معین ). کاواک. تهی و فرسوده. ( صحاح الفرس ). پوک. اجوف. مجوف [ دندان ] : 
20:سزد که او نکند طمع پیر دندان کرو. کسائی.
22:کرودندان و پشت چوگان است. رودکی.
24:ای دو بادام تو چو گوز کرو
26: کرو. [ ک ِ رَ ] ( اِ ) کشتی کوچک را خوانند و آن را سنبک نیز گویند. ( جهانگیری ). کشتی و جهاز کوچک. ( برهان ). کشتی خرد که در دریا باشد. ( غیاث اللغات ). کشتی و جهاز کوچک را نیز گویند مستند بدین بیت شیخ سعدی : 
27:جوانی پاک باز و پاکرو بود
28:که با پاکیزه رویی در کرو بود. ( آنندراج ).
33: کرو. [ ک ِ رَ / ک َرْوْ ] ( اِ ) کاهوی تلخ. || کاسنی. ( ناظم الاطباء ).
34: کرو. [ ک َرْوْ ] ( ع مص ) کندن زمین را. || برآوردن چاه را به چوب و جز آن. ( آنندراج ) ( منتهی الارب ) ( از اقرب الموارد ). برزیدن چاه. ( تاج المصادر ). || بارها کردن کاری را. ( آنندراج ) ( منتهی الارب ) ( از اقرب الموارد ). || بشتافتن ستور و دست و پای ناهموار انداختن در رفتن. ( آنندراج ) ( از منتهی الارب ) ( ناظم الاطباء ). || گوی بازی کردن. ( تاج المصادر ). گوی باختن و زدن تا بالا رود. ( از اقرب الموارد ). || نوعی از خرامان رفتن زن. یقال : کرت المراءة فی مشیتها. ( از منتهی الارب ) ( ناظم الاطباء ). بطرز خوشی راه رفتن زن و خرامان رفتن او. ( از ناظم الاطباء ). بیشتر بخوانید ... 
38: ( کروی زره ) یکی از خویشان افراسیاب که در کشتن سیاوش سعی بسیار داشت ( داستان ) .
40:( اسم ) فرهنگ نویسان بمعنی کشتی و جهاز کوچک و زورق نوشته اند و این معنی را جهانگیری از شعر سعدی استنباط کرده : [ جوانی پاک بازو پاکرو بود که با پاکیزه رویی در کرو بود ] . [ شنیدستم که در دریای اعظم بگردابی در افتادند با هم ... ] . رشیدی گوید : او در این معنی متفرد است . معنی مزبور درست نیست . چه از بیت دوم تلویحا بودن آنان در کشتی استنباط میشود و صحیح [ در گرو بود ] است . یعنی عاشق او بود و مشهور هم همین است . ولی باید دانست که این کلمه بهمین معنی در سواحل خلیج فارس مستعمل است .
52:قایق: جوانی پاک بازِ پاک رو بود / که با پاکیزه رویی در کرو بود (سعدی: ۱۴۸ ). 
56: /karoo/ از مکان های واقع در منطقه ی زیارت در جنوب گرگان & جایگاه سر پوشیده ی بره - آهسته & جوانه ای که هنوز باز نشده باشد - یکی از واحدهای شمارش، مخفف کرور معادل پانصدهزار
60: ( کُرّو (کروک) ) میوه انار کوچک
66: کرو ( به آلمانی: Cro ) ( نام اصلی کارلو وایبل[ ۱] [ ۲] [ ۳] ( به آلمانی: Carlo Waibel ) ) زادهٔ ۳۱ ژانویه در آلن، خواننده، رپر و طراح آلمانی است. موسیقی او ترکیبی از رپ و پاپ است و خودش آن را با عنوان راوپ ( Raop ) توصیف می کند. [ ۴] 
67:کرو از سن ۱۳ سالگی شروع به ضبط موسیقی کرد. [ ۴] او پیانو و گیتار را نیز در خردسالی آموخت. [ ۵] 
68:در سال ۲۰۰۹، اولین رمیکس با نام Trash و در فوریه ۲۰۱۱ دومین میکس تیپ خود را با نام «ماینه موزیک» ( به آلمانی: Meine Musik ) را منتشر کرد[ ۶] که برای دانلود رایگان در دسترس بود. او تمام آن ها را به تنهایی درست کرده بود[ ۷] و در همین کارش از سوی خواننده هیپ هاپ آلمانی «کاز» شناخته شد. [ ۶] کرو علاوه بر کار موسیقی به عنوان یک طراح نیز فعال است و قبلاً به عنوان یک طراح رسانه ها و کاریکاتوریست برای روزنامه اشتوتگارتر کار می کرد. [ ۸] [ ۹] 
74: wiki: کرو 
101: کرو /غرو ( و را میتوان هر گونه خواندش هم بر سنگ سرو هم هم بر سنگ سبو ) چیز میان تهی را گویند چون نی چون دندان کرو چون کشتی و هر کشتی را می توان گ گفت از یاد نبریم که کشتی را ناو نیز می گفتند که انهم بهمین چم بود 
103:ای دو بادام تو چو گوز کرو
106:جوانی پاک باز و پاکرو بود
107:که با پاکیزه رویی در کرو بود. 
110:سزد که او نکند طمع پیر دندان کرو. 
113:کرودندان و پشت چوگان است. 
146: کرو=میلیون میلیون
=== status ===
URL: https://abadis.ir/fatofa/%DA%A9%D8%B1%D9%88/
FETCHED: 2026-09-14T02:00:35Z
STATUS: 200
TITLE: کرو - معنی در دیکشنری آبادیس

URL: https://vajehyab.com/dehkhoda/%DA%A9%D8%B1%D9%88
FETCHED: 2026-09-14T02:00:36Z
STATUS: 200
TITLE: معنی کرو | لغت‌نامه دهخدا | واژه یاب
```


## [2026-09-14T02:01:02.075Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== PHD kar ===\"; grep -n \"^kar \\|kar m\\|mahig\\|māhīg\" PHD.txt | head -20; echo \"=== PHD_mackenzie ===\"; grep -n -i \"kar māhīg\\|kar mahig\\|kar-mahig\" PHD_mackenzie.txt | head"
}
```


### [2026-09-14T02:01:02.193Z] TOOL RESULT

```
=== PHD kar ===
442:mahig [m’hyk' | M m'hyg, N mahi] fish; astr. Pisces.
443:māhīgān [BYRH-, m'hykEn! | M whyg’n, N māhiyān] month.
1957:fish mahig.
2842:month mah, māhīgān.
4896:mah māhīgān māhīg mayān mayanag mayānjīgīh mayānjīg mehmānīh mehmān māzdēsn māyišn zan-!
=== PHD_mackenzie ===
```


## [2026-09-14T02:01:04.003Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== NYB kar ===\"; grep -n \"kar māhīk\\|kar mahik\\|kar-māhīk\\|kar2\\|karmāhīk\" NYB_vol2_glossary.txt | head -10; echo \"=== grep کرماهی ===\"; grep -rn \"کرماهی\\|کر ماهی\\|ماهی کر\" *.txt | head -10"
}
```


### [2026-09-14T02:01:04.115Z] TOOL RESULT

```
=== NYB kar ===
=== grep کرماهی ===
MON_part2.txt:50020:که در دعاوی عادی کر ماهیتی
```


## [2026-09-14T02:01:11.854Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n \"^kar\" PHD.txt | head -20; echo \"=== NYB kar entries ===\"; grep -n \"^kar\\b\\|^kar \" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T02:01:11.917Z] TOOL RESULT

```
425:kardan 5o kehtar
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
750:karm,
4987:kardagān 1%kardāg kam kamāndār kamān kamāl kamālīg kamistīh ‘kamist kamzor kamzorih kamar kamarband maygt arz! kastār kastärīh kchtar kaf
4992:karbāš karbunag karg kirīh- askamb! kirrén- kirrēnīdan kilēl
4997:kardārīh
5005:kardār kardārīh kāntigr
5006:kard
5010:karr, -gat.
5011:kar-
5012:karün
5013:karxūš
=== NYB kar entries ===
2203:kar-dahak
2208:kar [k'1] work, act, deed (also evil), busi- ness, errand, matter, case, task, cas. obl. kārē [k'ly], käreh [k'lyh] (ef s. v. karp); with indef. art. kār-ē [k'14-1] anything 1122, something 104°; pat kār-ē for some business 1417; 3511-14, 5027 etc., passim; — 6 butan i ham-ic kārē frahaxtak in order that all might be instructed in this matter (viz. in the new religion) 10811; pat martom käreh through human work (= as far is humanly possible) 1172; — ~ framiitan to bring about 19%; ~-om tō framāyē do thou thy duty to me! 2722; amāh dp i tč pat ~ né apäyet we do not need thy water 1423; 375-5; andar 6 ~ kartan to begin using regularly 9614; pat én ~ ku with the commission to ask: “.. — often coordinated with another notion so as to form a hendiadys expressing that the notion is put into practice: ~ u kirpak (work and religious virtue =) meritorious religious deeds 13% and passim; ~ u dätistän, v. this w.; ~ u räyenisn prac- tical function 87? (in this construction u is very often wanting in MSS and edi- tions); — šahrē -än (pl. cas. obl.) “‘state- work" — penal servitude, forced labour 92; zanč ~-dn 834 v.s.v. zan. — = NP. Av. only in the adj. kära-vant- (465); on OP kära- v. kürécür. — V. also a-kär, dast-kārēh, "ham-kär, kām-kār, kār-dāk, kàür-nàmak. ' > god
2214:kar-dahak or kär-däk (k'ldhk' or k’ld’k], pl. cas. obl. —-k'n' trader, merchant, (perhaps) pedlar 85%. — Paz. kärdahag-, Skr. v. vāņijyakāra (Mx 4° vamikloka); MPrs k’rd’g ‘migrant, tramp’, Henning, BSOAS XIII, 1950, 643; [on xa&pdaxec,
2216:kar-dahak
4902:kar- (kunav): !kartan
5217:karš: kašitan
5218:karšvar: kišvar
```


## [2026-09-14T02:01:14.032Z] TOOL CALL #45: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%DA%A9%D8%B1%D9%85%D8%A7%D9%87%DB%8C/\" \"https://en.wikipedia.org/wiki/Kar_fish\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 458: Avestan kara fish / Persian kar-mahi\"; done"
}
```


### [2026-09-14T02:01:16.828Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/d008ead3fe9f0b2a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e559cf693667b89.txt
```


## [2026-09-14T02:01:19.825Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,5p' d008ead3fe9f0b2a.txt; grep -n \"کرماهی\\|ماهی\" d008ead3fe9f0b2a.txt | head -15; echo \"=== wikipedia kar fish ===\"; sed -n '1,8p' 1e559cf693667b89.txt"
}
```


### [2026-09-14T02:01:19.912Z] TOOL RESULT

```
URL: https://abadis.ir/fatofa/%DA%A9%D8%B1%D9%85%D8%A7%D9%87%DB%8C/
FETCHED: 2026-09-14T02:01:16Z
STATUS: -1
TITLE: 

=== wikipedia kar fish ===
URL: https://en.wikipedia.org/wiki/Kar_fish
FETCHED: 2026-09-14T02:01:16Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T02:01:22.701Z] TOOL CALL #47: ToolSearch

```json
{
 "query": "select:WebSearch,WebFetch",
 "max_results": 2
}
```


### [2026-09-14T02:01:22.711Z] TOOL RESULT

```


```


## [2026-09-14T02:01:25.238Z] TOOL CALL #48: WebSearch

```json
{
 "query": "Avestan kara fish Kara masya Bundahishn \"kar mahig\" Middle Persian mythical fish etymology"
}
```


### [2026-09-14T02:01:34.733Z] TOOL RESULT

```
Web search results for query: "Avestan kara fish Kara masya Bundahishn "kar mahig" Middle Persian mythical fish etymology"

Links: [{"title":"(PDF) Understanding the Names and Functions of Mythical Fishes in the Avesta","url":"https://www.researchgate.net/publication/342955077_Understanding_the_Names_and_Functions_of_Mythical_Fishes_in_the_Avesta"},{"title":"(PDF) A Thematic and Etymological Glossary of Aquatic and Bird Genera Names in Iranian Bundahišm","url":"https://www.researchgate.net/publication/283752293_A_Thematic_and_Etymological_Glossary_of_Aquatic_and_Bird_Genera_Names_in_Iranian_Bundahism"},{"title":"(PDF) Understanding the Names and Functions of Mythical Fishes in the Avesta / К значению имен и функций мифических рыб в \"Авесте\"","url":"https://www.academia.edu/43630166/Understanding_the_Names_and_Functions_of_Mythical_Fishes_in_the_Avesta_%D0%9A_%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8E_%D0%B8%D0%BC%D0%B5%D0%BD_%D0%B8_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9_%D0%BC%D0%B8%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%85_%D1%80%D1%8B%D0%B1_%D0%B2_%D0%90%D0%B2%D0%B5%D1%81%D1%82%D0%B5_"},{"title":"www.ssoar.info A Thematic and Etymological Glossary of Aquatic","url":"https://d-nb.info/1191596176/34"},{"title":"FISH iii. IN PRE-ISLAMIC PERSIAN LORE - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/fish-iii/"},{"title":"Bundahishn","url":"https://en.wikipedia.org/wiki/Bundahishn"},{"title":"Mashya and Mashyana","url":"https://en.wikipedia.org/wiki/Mashya_and_Mashyana"},{"title":"(PDF) A Thematic and Etymological Glossary of Carnivorous Animals Based on the Pahlavi Text of Iranian Bundahishn","url":"https://www.academia.edu/27976603/A_Thematic_and_Etymological_Glossary_of_Carnivorous_Animals_Based_on_the_Pahlavi_Text_of_Iranian_Bundahishn"},{"title":"(PDF) A Thematic and Etymological Glossary of Aquatic and Bird Genera Names in Iranian Bundahišm","url":"https://www.academia.edu/75278977/A_Thematic_and_Etymological_Glossary_of_Aquatic_and_Bird_Genera_Names_in_Iranian_Bundahis_m"}]

I found relevant search results about the Avestan kara fish, its etymology, and related Middle Persian terms. Here's what the sources reveal:

## Etymology of Kara

The name of the mythical Kara fish (*kara-) is highly probable to be a Uralic loan word from an early period of contacts between Indo-Iranian and Finno-Ugric tribes.

## Avestan and Middle Persian Forms

In Avestan, the fish is known as masya-, kara-, and vasī-, while in Manichaean Middle Persian it appears as māhīg, and in Pazand as māhig. In Bundahišn, the kar-māhīg (kar-fish) was the biggest of the aquatic creatures.

## The Name and Epithet

In Yasna 42.4, the epithet panchasadvar (Av. pancā.sadvarā-) means "that of fifty fins" or "that of fifty gates," which presumably refers to the plates on the body of this mythical fish (similar to the Acipenser species).

The epithet of Kara, upāpa- meaning 'the one near the water,' apart from its literal meaning, may also point to its habitat at the source of Ardvisur in the Sea of Frahvkard.

## Role in Bundahišn

Pahlavi sources endow the Kara fish with expressive eschatological functions (Bundahishn 18.1–6; Menog-i hrad 62.28–29).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:01:41.838Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \"https://www.iranicaonline.org/articles/fish-iii/\" \"https://d-nb.info/1191596176/34\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 458: Kara fish in pre-Islamic Persian lore; etymological glossary of aquatic names in Iranian Bundahišn (kar-māhīg < Av. kara-)\"; done"
}
```


### [2026-09-14T02:01:54.449Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/0be5b8f653dcc665.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0d73b8858ef69ab.txt
```


## [2026-09-14T02:01:57.524Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,5p' 0be5b8f653dcc665.txt; grep -n -i \"kar\\b\\|Kara\\|kar-māhīg\\|karmāhīg\" 0be5b8f653dcc665.txt | head -20; echo \"=== dnb ===\"; sed -n '1,5p' c0d73b8858ef69ab.txt"
}
```


### [2026-09-14T02:01:57.600Z] TOOL RESULT

```
URL: https://www.iranicaonline.org/articles/fish-iii/
FETCHED: 2026-09-14T02:01:46Z
STATUS: 200
TITLE: FISH iii. IN PRE-ISLAMIC PERSIAN LORE - Encyclopaedia Iranica

57: The Bundahišn (q.v.) contains interesting pseudo-scientific, mythical, and sometimes inconsistent information about fishes. The fifth (and last) ēwēnag (class?) of animals created by Ahura Mazdā (q.v.) was that of aquatic ( ābīg ) creatures, of which the kar-māhīg ( kar -fish; cf. the kar shark below) was the biggest, and namatū (?; probably “shrimp” according to Bahār, p. 79) the smallest (tr. Anklesaria, 13.10, pp. 120-21). These aquatic creatures included ten sardag s (genera?) of fishes, all unidentifiable: araz, arzūkā, marzūkā, warzūkā, takāweryo (?), pašmāzak (?), s ūmakčīt (?), wāsī pančā sadwarām (?), and kar (13.26-27, pp. 122-23, 15A.1-8, 10, pp. 142-45; tr. Bahār, pp. 79, 85-86). Then, within each sardag , there developed other sardag s (species and subspecies?) so that the total number of fishes (species?) reached two-hundred and eighty-two (13.27, pp. 122-23; in Bahār’s tr., p. 79, two-hundred and sixty-two). All fishes (just like water, earth, and plants) are said to be female ( mādag ) “and are never otherwise” (15A.1, pp. 142-43; tr. Bahār, p. 85). Although all female, fishes mate like heterosexual creatures: At the time of pus-xwāhišnīh (lit., “son-desiring”; estrus), the fish pair up, go down in deep water as much as one hāsar (about 1 mile), and then come back to the surface; during that coming and going, they rub each other, thus secreting a xwēy (lit., sweat) by which they both become pregnant. In seas such as Frāxkard (q.v.) and Kamrōd, which are unaffected by tides (sic), “fish mate in shallow water but lay eggs in deep water” (15A.2-4, pp. 142-43; tr. Bahār, pp. 85-86). These ten (species of) fish yearly beget “children” as many as follows: kar , 200,000 young; arzūkā , 9,000; marzūkā , 8,000; warzūkā , 7,000; takāweryo , 6,000; sūmakčīt , 5,000; pašmāzag , 4,000, but wāsī pančā-sadwarām only 500 (15A.5, pp. 144-45; tr. Bahār, p. 86). The propagation of fishes is parthenogenetic (because, like all plants, “they have no male”). However, the fertilization and conception are internal: “The eggs develop like [the fetuses of] cattle ( gōspandān ) in the womb, and when mature enough, they are ejected. The eggs continue their maturation in water; then they hatch, giving birth to small fry.” Fishes “become pregnant in the month of Šahrīvar, and give birth in Farvardīn” (15A.7, 10, pp. 144-45; tr. Bahār, p. 86).
58: Most remarkable among fishes are the wāsī pančā sadwarām and the kar -fish, both living in the Frāxkard Sea. The former is so long that, “if it moves fast from morning till sunset, it cannot cover a distance as long as its length….Most aquatic creatures live under its sālārīh ” (chieftainship, authority; 24.6-7, pp. 192-93; tr. Bahār, p. 101). The kar -fish, elsewhere equated with araz (see above), is also said to be “the rad (chief) of water creatures” (17.14, pp. 154-55; tr. Bahār, p. 89). It is “the biggest animal created by Ahura Mazdā.” Two [specimens of] kar -fish are charged with continually watching over the miraculous white hōm (see HAOMA) in that sea, because the latter is threatened by a gigantic wazaγ (frog; “lizard” [sic] in Anklesaria) created by Ahriman (q.v.) against fishes, to counter the two kar -fishes, and to destroy the white hōm (5.3, pp. 56-57; tr. Bahār, p. 56). To restrain that wazaγ , which is Ahriman’s largest living creature, the kar -fishes keep on circling the white hōm , and in order to be always on guard, they “do not need anything to eat,” because “they are provided with mēnōg xwarišn (spiritual food). Further, “they are so perceptive that they sense any increase or decrease in sea water as much as the volume of a sharp needle” (24.1-5, pp. 192-93; tr. Bahār, pp. 100-101).
=== dnb ===
URL: https://d-nb.info/1191596176/34
FETCHED: 2026-09-14T02:01:54Z
STATUS: -1
TITLE:
```


## [2026-09-14T02:02:02.734Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -o -i \".\\{200\\}kar shark.\\{400\\}\" 0be5b8f653dcc665.txt | head -3; echo \"=== 'kar ' mentions ===\"; grep -n -o -i \".\\{100\\}\\bkar\\b[^-].\\{200\\}\" 0be5b8f653dcc665.txt | sed -n '1,6p'"
}
```


### [2026-09-14T02:02:02.876Z] TOOL RESULT

```
57:nconsistent information about fishes. The fifth (and last) ēwēnag (class?) of animals created by Ahura Mazdā (q.v.) was that of aquatic ( ābīg ) creatures, of which the kar-māhīg ( kar -fish; cf. the kar shark below) was the biggest, and namatū (?; probably “shrimp” according to Bahār, p. 79) the smallest (tr. Anklesaria, 13.10, pp. 120-21). These aquatic creatures included ten sardag s (genera?) of fishes, all unidentifiable: araz, arzūkā, marzūkā, warzūkā, takāweryo (?), pašmāzak (?), s ūmakčīt (?), wāsī pančā sadwarām (?), and kar (13.26-27, pp. 122-23, 15A.1-8, 10, pp. 142-45; tr. Bahār, pp. 79, 85
=== 'kar ' mentions ===
57:mals created by Ahura Mazdā (q.v.) was that of aquatic ( ābīg ) creatures, of which the kar-māhīg ( kar -fish; cf. the kar shark below) was the biggest, and namatū (?; probably “shrimp” according to Bahār, p. 79) the smallest (tr. Anklesaria, 13.10, pp. 120-21). These aquatic creatures included ten sard
57: arzūkā, marzūkā, warzūkā, takāweryo (?), pašmāzak (?), s ūmakčīt (?), wāsī pančā sadwarām (?), and kar (13.26-27, pp. 122-23, 15A.1-8, 10, pp. 142-45; tr. Bahār, pp. 79, 85-86). Then, within each sardag , there developed other sardag s (species and subspecies?) so that the total number of fishes (speci
57:-43; tr. Bahār, pp. 85-86). These ten (species of) fish yearly beget “children” as many as follows: kar , 200,000 young; arzūkā , 9,000; marzūkā , 8,000; warzūkā , 7,000; takāweryo , 6,000; sūmakčīt , 5,000; pašmāzag , 4,000, but wāsī pančā-sadwarām only 500 (15A.5, pp. 144-45; tr. Bahār, p. 86). The pr
58:res live under its sālārīh ” (chieftainship, authority; 24.6-7, pp. 192-93; tr. Bahār, p. 101). The kar -fish, elsewhere equated with araz (see above), is also said to be “the rad (chief) of water creatures” (17.14, pp. 154-55; tr. Bahār, p. 89). It is “the biggest animal created by Ahura Mazdā.” Two [s
58:γ (frog; “lizard” [sic] in Anklesaria) created by Ahriman (q.v.) against fishes, to counter the two kar -fishes, and to destroy the white hōm (5.3, pp. 56-57; tr. Bahār, p. 56). To restrain that wazaγ , which is Ahriman’s largest living creature, the kar -fishes keep on circling the white hōm , and in o
```


## [2026-09-14T02:02:07.485Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -o -i \".\\{150\\}shark.\\{250\\}\" 0be5b8f653dcc665.txt | head -6"
}
```


### [2026-09-14T02:02:07.544Z] TOOL RESULT

```
57:ast) ēwēnag (class?) of animals created by Ahura Mazdā (q.v.) was that of aquatic ( ābīg ) creatures, of which the kar-māhīg ( kar -fish; cf. the kar shark below) was the biggest, and namatū (?; probably “shrimp” according to Bahār, p. 79) the smallest (tr. Anklesaria, 13.10, pp. 120-21). These aquatic creatures included ten sardag s (genera?) of fishes, all unidentifiable: araz, arzūkā, marzūkā, warzū
```


## [2026-09-14T02:02:13.803Z] TOOL CALL #53: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T02:02:13.887Z] TOOL RESULT

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


## [2026-09-14T02:02:19.296Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | sed -n '1,3p'; echo \"---\"; grep -n -i \"hvalr\\|Walfisch\\|squalus\\|kalis\" WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T02:02:19.391Z] TOOL RESULT

```
---
208:vokalisch ai. pajasyd- n. Bauchgegend. Weichen^^, russ.    pachz „Leisten-
305:    Vgl. die ahnliche, aber anders vokalisierte                     Wz. {s)pen- „spinnen“.
341:darf  (: ags. /yne), kann der Wzvokalismus auch "^[pen- '^pon- sein.         Ob
877:    und des Yokalismus. Ygl. Noreen Urg. Ltl. 195, 223, Schmidt KZ. 26,
1037:Gutt. l88f. m. Lit.) ist im Yokalismus wie in der Bed. zu beanstanden.
1952:Yokalismus befrie digender ware eine Zs. mitfra-, s. Brugmannl^ 925, zw.
2205:   Alb. pa j,bevor‘‘               wenn aus ^pari^ das im Yokalismus nacb pare j,erster^^
2613:Dutch ihren o-Vokalismus auffallige Biidung.
3136:276 f., Verb. m. placet als „gefMig“ weiB ich mit dem Yokalismus von
3490:                                        Mit anderem Yokalismus ahd. feili^ mnd.
```


## [2026-09-14T02:02:20.743Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"کرو\\|نهنگ\\|وال\" ARY_pages.txt | head -10; echo \"=== latin index ===\"; grep -n -i \"SQUAL\\|WHALE\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T02:02:20.815Z] TOOL RESULT

```
88:کوج کردهاند. طی این کوج‌های متوالی؛ آریایی‌ه با بومیان هر محل درآمیختند و در نتیجه پاک و
166:رزم آوری) آنها را قادر کرد که طی موج‌های متوالی در ظرف حدود دو هزار سال اروپا و آسیای
181:یک سلسله تهاجم‌ها وکوچ‌های متوالی در پخش عظيمي از آسپای مرکزی و آسپای صفیر ساکن
209:پذیریم که کوج هند و اروپائیان به صورت موج‌های متوالی مرکز گریز انجام شده» به این نتیجه
259:والامیزان همسانی زبانهای مجاور به گونه‌ای دیگر مي‌بود.
393:کند. برعکس» عبری زبانی والا و اصبل است که طی قرون تغییر نکرده است و هر کسی که غبری
628:کیفیت والای این اثر در سطحی است که امروزه هم برای شناخت زبان سانسکریت از آن استفاده
840:صربی» کرواتی» مقدونی). جمع سخنگویان به این زبان‌ها حدود ۴۵۰ میلیون نفر است.
981:مورد به قربانی کردن انسان اشاره شده است. ظاهراً در نظر هندیان پاستان» انسان والاترین جانداری
1054:هسرش) پیامد دیگری نیز داشت: مقام او والاتر از مقام پدر و رئیس ابل بود ولی آنها راکاملاً
=== latin index ===
922:aE Fraly tips gills dhl whales Jeske ko ge
15001:WHALE ENGLISH) Si SQUALUS (LATIN) 3
15013:BARNHART: (WHALE) 1229
```


## [2026-09-14T02:02:25.296Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '14985,15025p' ARY_latin_index_pages.txt; echo \"=== page tag ===\"; awk 'NR<=15001 && /\\[pdf page/ {p=$0} END{}' ARY_latin_index_pages.txt; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<15001' | tail -2"
}
```


### [2026-09-14T02:02:26.460Z] TOOL RESULT

```
-VES (BANVES) XBRETON) gigi YVASTOH, VAS- (SANSKRIT) cy Suite
WESHI _ AHITTITE) <0 VESCOR (GREER) gin
GOTHIC) SF
‘REFERENCES beth WISAN (WAILA WISAN)
POKORNY SCOTS VIST (OLD SCANDINAVIAN) pS she!
Theva STOVE Hasias wail WIST :(OLD HIGH GERMAN) x48 galt
FAFA Loge Kad WIST (OLD ENGLISH) oS JS
TFA sgbGoly | :(QMIDDLE IRISH) sls 6-32!
FESS, FEISS
femtlool
obaggh hin Obj 22 13a ctl pe oV
ge 0S Lge Saga) CHIL) 22 19 atl OF
sche gues hers eat os sanity So Cel" "ps cecal gedls cde OV
tsa LED aT asl te seals Be 8 3 oe net?
cael ots ogLth Sly gal gael clastas eal y> y nt shtalé "SF Sy ot ee So oot
Wel (OLD ENGLISH) 9S 5S! PHALAINA (44) (GREER) 2b y
WHALE ENGLISH) Si SQUALUS (LATIN) 3
HVAL DANISH) ila BALEINE (alt) (FRENCH) il
VAL s(SWEDISH) $8 yo (OLD SCANDINAVIAN) 5 Soe!
KVAL, HVAL (NORWEGIAN) 539 HVALR
WALVIS DUTCH) ache HWAL —(OLD SAXON) wf gS
KALIS —-(OLD PRUSSIAN) eS +3.4 (OLD HIGH GERMAN) gf gat
WAL , WALFISC
WAL, WALFISCH — (GERMAN) glT
[pdf page 514]
i
| OND I Coole" gsi" 4) cy aly
read Mans aaticadl REFERENCES oc tKy
BARNHART: (WHALE) 1229
leatlooy
EM aay contd cal clan dly Spo b co gh ool ela y clip lanjly Seal sw SKEAT~}
wa gt) ohaal a te Ge aly dary |) oad eel uy} lanly ai) ONIONS -1
haa SL OT aliaal ya sete aely yvab GUL, Cong gy! oy} lanjly gedul BARNHART -¥
wage aly onl Sa Cal” (74) KAL KOLA, KORA- ply! slaejly POKORNY -7
BD) gm FAAS 22 059 cal Sa oS ates! 9 ally lAdLj 32 “Ub 9 “Uly" ly ant -0
BI PCa C813 9 IE N33 (Gob 5a He OF AUN) gesh Gel g (pad ga PY
JBALAENA cet sLaejly L "Ub" su5ls (PF Genie) 42 1355 ayy yalls cpaw Kind 5 aly
tot Aeglis PHALAINA gt 505}p b"Jty" ashy Se So jl gg Corb ot Als BALEINE aii 5
tha soT CLE) oh aal ya eh sly gle aybagey St a5ly ol beds oar APA gerbe) col
Fra mane $e aa eS
WAL HOLD ENGLISH) 5 nds! VRAVA, VRANA- :(SANSKRIT) cy Sle
=== page tag ===
14953:[pdf page 512]
14982:[pdf page 513]
```


## [2026-09-14T02:02:35.232Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && head -3 WLD_Bd2_pages.txt; grep -c \"pdf page\" WLD_Bd2_pages.txt; grep -n \"541\" WLD_Bd2_pages.txt | head -5"
}
```


### [2026-09-14T02:02:35.302Z] TOOL RESULT

```
                ALOIS WALDE


0
9041:mannll- 1,541, Solmsen Beitr. 239), Tiiorog ,,zuverlassig, treu: vertrauend,
10130:   bir „Sohn'' (W?e^-             vgl. got. baur „Sobn‘’, Pedersen KZ. 33, 541, Jokl lA.
11337:Zimmer KZ. 24, 541, Thurneysen KR. 44, 49, KZ. 28, 146, Pick II ^ 171 f.,
18117:541; mit idg. Anlautwechsel                         b:p zn gv. Tioanvog,        TisQy.vog         usw.? oder zu
19192:Fehler“ (^meUs-os, vom 6s-St       Brugmann 11^1,541), mellaim „betruge‘‘
```


## [2026-09-14T02:02:38.920Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"hvalr\\|hval\\b\\|hvali\\|Walfisch\\|hwal\" WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T02:02:38.984Z] TOOL RESULT

```
1823:ziindliche Geschwalst**^, jiQrjpalvco „blase heftig‘‘, JCQrjpovdoy „tobe"‘, 7tQif]oxif]Q
3080:Hes .; jigexvov' noixiXoxQovv I'/a^rov Hes.: Ilooxvrj ,,die Schwalbe": ahd./’or/^n-
3238:   Unter einer Bed.*Entw. ,,Eiche, Eichwald, Wald iiberhaupt, Waldge-
4993:Bed. vielleichfe mnd. v%          vihe, vie n. „Sumpf, Bruch, Sferauchwald, Teich“
6380:nach Pick III^ 255) „losgerissenes Stiick Walfischspeck", Iiual-flustri ds.,
11655:udgl.), bei Lycophr. cpdXXr] „Walfisch“ (nicht zu "^sq^alo-s^ s. d. m. Lit.; vgl.
13798:schwalles“    noXv cpXo to p og d^dXao a a {^(pXoido-pog^ Formans nach Schall-
17144:(Loc. sg.) ds.hieher auch (Lit. bei Berneker aaO.) als "^jjBuschwald auf dem
30140:form m. anl, su- noch die Sippe von nhd. sc hwalien, Wasserschwall usw.
35272:swale „Schlund, Wirbel“, nhd. Schwalch jjOflFnung des Schmelzofens“, nd.
```


## [2026-09-14T02:02:42.850Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"sq\\^alo\\|squalus\\|q\\^alo\" WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T02:02:42.909Z] TOOL RESULT

```
11655:udgl.), bei Lycophr. cpdXXr] „Walfisch“ (nicht zu "^sq^alo-s^ s. d. m. Lit.; vgl.
35940:  Lat. squalus „ein groBerer Meerfisch (Meersaufisch?)^'; anord. livalr^ pi.
35956:   Osthoff aaO., beziiglich Form und Bed. des lat. squalus zweifelnd wie
35957:Schrader, zioht (Bersiis Gutt. 144, 161) Yerbindung von squalus mit gi\
35961:stufe zu ^sq^alos^ namlich als *sqV:liom mit ^-farbigem                    Z,   richtigen   J ver-
44991:Block, Bank, Schemel, Buderbank“. S. noch u. ^sq^alos iiber doTtaXog
```


## [2026-09-14T02:02:44.811Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '35930,35975p' WLD_Bd2_pages.txt"
}
```


### [2026-09-14T02:02:44.871Z] TOOL RESULT

```
farbigen sqond-^ zuruckgefiihrt werden diirften (freilich warum gerade o-
                                     (s)q«alo-s   —   sqei-                                   54


Stufe?) ware die Kormalstufe als idg. sqend- ansetzbar. Norw.        shvetta^
skvait .jSpritzen, schneilen, auffahren^^ hat fernzubleiben (s. Falk-Torp u.
shvette).


(s)qSalo-S     „fiir   groBe Fischarten'".
  Lat. squalus „ein groBerer Meerfisch (Meersaufisch?)^'; anord. livalr^ pi.
      m. „Walfisch“ (/-St.), ags. hiccel^ ahd. (li)tvaJ^ {]i)weUra „Walfisch‘‘
Jivalir
(Liden Uppsalastudier 91), mhd. nhd.              ivels (nhd.      auch Waller^ Weller mit
r aus z 8. Solmsen KZ. 34, 541); apr. kalis „Wels“ (Schrader Phil. Studien,
Festg. f. Sievers Iff., Reallex. 951; -weitere Lit. bei Osthoff Par. I 324;
Solmsen KZ. 37, 587 gegen 34, 541; friihe Entlehnung aus dem Germ, ver-
muten irrig Mikkola Balt, und Slav. 10, Solmsen Beitr. I 122 Anm.); avest.
kara- „ein mythischer Fisch*’ (Vasmer Festschr. Baudouin de Courtenay 83).
   Sehr zweifelhaft ist Zugehorigkeit von gr. dojialog „Fisch‘^ (mit d-Vor-
schlag; Solmsen Beitr. I 21 Anm.; ’wenn ein zu oTiakdaoeiv zejuveiv                  '         —
s. ^sjphel „spalten“      —
                      gehoriges ^ondXog oder ^ondka in der Bed. „Schuppe“
vorausgesetzt werden durfte, so eher psilotisch fur "^d-onaXog „schuppiges
Tier''; ahnlich Fick BB. 18, 141; anders Hellquist, s. Falk-Torp 1433 unter
asp^ Fischname).
   Osthoff aaO., beziiglich Form und Bed. des lat. squalus zweifelnd wie
Schrader, zioht (Bersiis Gutt. 144, 161) Yerbindung von squalus mit gi\
oxvXiov „Haifischart“ vor, das aber eher eine Seitenform von oxvka^ „Hund-
chen'^ ist, mit einer der haufigen tTbertragungen von Namen von Land-
tieren auf Wassertiere (Solmsen aaO.; theoretisch ware es auch als Tief-
stufe zu ^sq^alos^ namlich als *sqV:liom mit ^-farbigem                    Z,   richtigen   J ver-
standlich).
  Gegen Zuziehung von gr. q)dkkaiva^ cpdkkiq „Wallfisch“ (Kluge KZ. 26,
89, Hoops Engl. Stud. 28, 92 ff., Osthoff aaO.) unter Ansatz sq^h- spricht
bes. das lat. hallaena (s. Yf. LEWb.^ 734, Persson Beitr. 797f. a 5).Unver-
wandt ist auch gr. nekcDo „Ungeheuer“ (friiher Solmsen KZ. 34, 540 f. nach
Benfey und Froehde, neuerdings Bechtel Lexil. 275 f.).
  Benennung des Tieres nach der Farbe (Uhlenbeck Ark. f. nord. fil. 15,
154 vergleicht av. kala- „8chwarz, schwarzblau‘‘) ist nicht gestiitzt. Be-
achtenswert sind finn. Anklange, s. Hoops aaO.

sqei- .jschneiden, trennen, scheiden“, Erw, von seq- (vgl. lat. secivum^ abg.
      Sccivo), Anlaut z. T. auch sk- und aspiriert sqh-.                    sJch-^   wie auch in
      den Weiterbildungen.
   Ai. chydti „schneidet ab“,          Ptc. chafa-h^          chitd-h   ,,abgeschnitteii“,   kaus.
```


## [2026-09-14T02:02:59.963Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,5p' 3735d75498a331a4.txt; wc -l 3735d75498a331a4.txt; grep -n -i \"kwal\\|whale\" 3735d75498a331a4.txt | head"
}
```


### [2026-09-14T02:03:00.043Z] TOOL RESULT

```
URL: https://www.ahdictionary.com/word/indoeurop.html
FETCHED: 2026-09-14T01:59:34Z
STATUS: 200
TITLE: Appendix I - Indo-European Roots

8290 3735d75498a331a4.txt
760: Possibly Greek phal(l)aina , whale baleen .
2562: quail 2 , from Middle Dutch quelen , to be ill, suffer. Both a and b from Germanic *kwaljan .
```


## [2026-09-14T02:03:03.712Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"squalene\\|squalus\\|rorqual\\|narwhal\" 3735d75498a331a4.txt | head; echo \"=== last lines ===\"; tail -5 3735d75498a331a4.txt"
}
```


### [2026-09-14T02:03:03.771Z] TOOL RESULT

```
5775: rorqual , from Old Norse raudhr , red;
=== last lines ===

 California Privacy Policy 
 Do Not Sell My Personal Information 
 Copyright 2022 HarperCollins Publishers All rights reserved.
 *This website is best viewed in Chrome, Firefox, Microsoft Edge, or Safari. Some characters in pronunciations and etymologies cannot be displayed properly in Internet Explorer.
```


## [2026-09-14T02:03:07.656Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"big fish\\|sheatfish\\|kwal\" 3735d75498a331a4.txt | head; echo \"---context 5770\"; sed -n '5765,5780p' 3735d75498a331a4.txt"
}
```


### [2026-09-14T02:03:07.736Z] TOOL RESULT

```
2562: quail 2 , from Middle Dutch quelen , to be ill, suffer. Both a and b from Germanic *kwaljan .
4782: silurid , from Greek silouros , sheatfish, probably from ourā , tail (with an obscure first element).
---context 5770
 Suffixed o-grade form *rot-ā‑ . rodeo , roll , rota , rotary , rotate , rotund , rotunda , roulette , round 1 , rowel ; barouche , control , prune 2 , rocambole , rotavirus , rotaxane , rotiform , rotogravure , from Latin rota , wheel.
 Suffixed (participial) form *ret-ondo‑ . rotund , rotunda , round 1 , from Latin rotundus , round, probably from *retundus , "rolling.".

[Pokorny ret(h)‑ 866.]

 ‌ ‌ reudh- 

Red, ruddy. Oldest form *h 1 reudh‑ .

Derivatives include red , robust , corroborate , ruby , and rubric. O-grade form *roudh‑ . red , from Old English rēad , red;
 rorqual , from Old Norse raudhr , red;
 rooibos , from Middle Dutch root , red. a-c all from Germanic *raudaz .

 Perhaps ultimately also from Germanic raudaz is Old Spanish roán , roan, if from Gothic *rauths , red, or a kindred Germanic source. roan .
 rowan , from a source akin to Old Norse reynir , mountain ash, rowan (from its red berries), from Germanic *raudnia‑ .
 rufescent , rufous , from Latin rūfus (of dialectal Italic origin), reddish.
```


## [2026-09-14T02:03:12.021Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"Pokorny\" 3735d75498a331a4.txt | tail -5; echo \"---\"; grep -c \"Pokorny\" 3735d75498a331a4.txt"
}
```


### [2026-09-14T02:03:12.092Z] TOOL RESULT

```
8177:[Pokorny 3. i̯eu‑ 510.]
8194:[Pokorny 2. i̯eu‑ 508.]
8202:[Pokorny i̯eu̯os‑ 512.]
8206:A grain, probably barley. Suffixed form *yew-ya . zein ; zeaxanthin , from Greek zeia , one-seeded wheat. [Pokorny i̯eu̯o‑ 512.]
8210:You. Second person (plural) pronoun. ye 2 , you , from Old English gē and ēow , you, from Germanic *jūz (nominative) and *iwwiz (oblique). [Pokorny 1. i̯u‑ 513.]
---
604
```


## [2026-09-14T02:03:16.323Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"al‑o\\|alo‑ 958\\|958\" 3735d75498a331a4.txt | head; echo \"---s roots\"; grep -n \"^ ‌ ‌ s\" 3735d75498a331a4.txt | head -40"
}
```


### [2026-09-14T02:03:16.394Z] TOOL RESULT

```
---s roots
5851: ‌ ‌ sā- 
5862: ‌ ‌ sāg- 
5878: ‌ ‌ sak- 
5887: ‌ ‌ sal- 
5901: ‌ ‌ sāwel- 
5916: ‌ ‌ sē- 
5927: ‌ ‌ sed- 
5969: ‌ ‌ segh- 
5986: ‌ ‌ sek- 
6006: ‌ ‌ sek w - 1 
6019: ‌ ‌ sek w - 2 
6026: ‌ ‌ sek w - 3 
6037: ‌ ‌ sel- 
6046: ‌ ‌ sem- 1 
6082: ‌ ‌ sem- 2 
6091: ‌ ‌ sēmi- 
6100: ‌ ‌ sen- 
6107: ‌ ‌ seng w h- 
6116: ‌ ‌ sent- 
6125: ‌ ‌ sep- 
6129: ‌ ‌ septm̥ 
6137: ‌ ‌ ser- 1 
6144: ‌ ‌ ser- 2 
6153: ‌ ‌ seuə- 1 
6158: ‌ ‌ seuə- 2 
6177: ‌ ‌ skand- 
6187: ‌ ‌ skei- 
6215: ‌ ‌ skel- 1 
6244: ‌ ‌ skel- 2 
6248: ‌ ‌ sker- 1 
6302: ‌ ‌ sker- 2 
6330: ‌ ‌ sker- 3 
6375: ‌ ‌ skeud- 
6395: ‌ ‌ skrībh- 
6402: ‌ ‌ slēb- 
6406: ‌ ‌ slēg- 
6419: ‌ ‌ sleiə- 
6427: ‌ ‌ sleubh- 
6443: ‌ ‌ smei- 
6466: ‌ ‌ snā-
```


## [2026-09-14T02:03:20.965Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"^ ‌ ‌ k w\\|^ ‌ ‌ (s)\" 3735d75498a331a4.txt | head -20; echo \"--- whale word\"; grep -n -i \"whale\" 3735d75498a331a4.txt | head"
}
```


### [2026-09-14T02:03:21.032Z] TOOL RESULT

```
3329: ‌ ‌ k w e 
3333: ‌ ‌ k w ei- 1 
3337: ‌ ‌ k w ei- 2 
3344: ‌ ‌ k w eiə- 
3374: ‌ ‌ k w el- 1 
3405: ‌ ‌ k w el- 2 
3416: ‌ ‌ k w ent(h)- 
3423: ‌ ‌ k w er- 
3449: ‌ ‌ k w etwer- 
3479: ‌ ‌ k w o- 
3529: ‌ ‌ k w rep- 
3536: ‌ ‌ k w r̥mi- 
6340: ‌ ‌ (s)keu- 
6452: ‌ ‌ (s)mer- 1 
6459: ‌ ‌ (s)mer- 2 
6475: ‌ ‌ (s)nāu- 
6483: ‌ ‌ (s)nē- 
6500: ‌ ‌ (s)neəu- 
6560: ‌ ‌ (s)pen- 
6722: ‌ ‌ (s)teg- 
--- whale word
760: Possibly Greek phal(l)aina , whale baleen .
```


## [2026-09-14T02:03:27.530Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '264723,264735p' KLN_1971.txt; echo \"=== KLN squalene ===\"; grep -n -i \"squalene\" KLN_1971.txt | head -3"
}
```


### [2026-09-14T02:03:27.660Z] TOOL RESULT

```
suff. -ite. 

walrus, n. — Du., fr. Swed. vallross , fr. ON. 
hrossvalr (cp. OE. horshwxl), lit. ‘horse whale’, 
fr. hross, ‘horse’, and hvalr, ‘whale’. Cp. Dan., 
Norw. hvalr os and see whale and horse. 

Walter, masc. PN. — ONF. Waltier, correspond- 
ing to OF. Gualtier , Gautier (F. Gautier), of G. 
origin. Cp. OHG. Walthari, Walthere , lit. ‘ruler 
of the army’, which is compounded of OHG. 
waltan (whence MHG., G. waken), ‘to rule’, and 
OHG. hari, heri (whence MHG. her, G. Heer ), 
=== KLN squalene ===
```


## [2026-09-14T02:03:35.243Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== SYN whale ===\"; grep -n -i \"whale\" SYN.txt | head -5; echo \"=== LEW squalus ===\"; grep -n -i \"squalus\" LEW_1910.txt | head -5; echo \"=== LAT squalus ===\"; grep -n -i \"squalus\" LAT.txt | head -5"
}
```


### [2026-09-14T02:03:35.328Z] TOOL RESULT

```
=== SYN whale ===
3844:5. Words denoting the male or female of a particular animal may be prefixed to names of other animals, as NE buill- elephant, bull-whale, cow-elephant, and hen applied to the female of birds in gen- eral and sometimes even to the female fish (NED s.v.), Br. taro- ‘bull-’ in maout-taro ‘ram’, targaz (fr. taro-kaz) ‘tomeat’, ete.
4868:| etc.), but also to that of various large animals, as the moose, elephant, whale. Du. jonge hond, NHG junger hund, now the usual term for ‘puppy’ (in place of the old welp, welf), and so in general
4952:W. blaidd, Br. bleiz = Ir. bled ‘sea monster, whale’, but etym.? Stokes 188. Henry 37. Against connection with Lat. bellua, cf. Walde-H. 1.100.
6510:Words for ‘belly’ were used alike for the external ‘belly’ and the internal ‘bel- ly, stomach’, and most of them are still familiar in the latter sense, in biblical language (“the whale’s belly”) and in common, partly vulgar, speech. Either the external or internal application may be the more original etymologically. Many of the same or related words were also used for ‘womb’ (4.47).
6522:Grk. crézaxos, deriv. of c7dza ‘mouth’ (4.24), hence, as orig. the passage from the mouth, ‘throat, gullet’ (see 4.29), later ‘orifice of the stomach’ and finally ‘stomach’ (c7éuaxos occurs only once in NT, namely 1 Tim. 5.23, likewise the only occurrence of stomach in the English Bible; elsewhere, as Mt. 12.40 ‘whale’s belly’, ko:Na, likewise in the translations NE belly, NHG bauch, Lith, pilvas, etc.). Hence Lat. stomachus > It. stomaco, Sp. ee Rum. stomac, Fr. estomac >
=== LEW squalus ===
=== LAT squalus ===
60165:squalus, -a, -um: couvert de croutes, ou de plaques de boue for¬
60182:squalus, -Ia.: squale, chien de aer. Quantitd de l'a inconnue;
60183:la forae squalus que certains lisent dans Ov., Hal.133, est en r 4 alit 4
```


## [2026-09-14T02:03:36.194Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.merriam-webster.com/dictionary/squalene\" --note \"page 458: English squalene < NL Squalus, shark\""
}
```


### [2026-09-14T02:03:37.420Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/32924127a4118ee5.txt
```


## [2026-09-14T02:03:39.495Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '60178,60200p' LAT.txt"
}
```


### [2026-09-14T02:03:39.554Z] TOOL RESULT

```
On pense a dor. 7 iaXos, ion.-att.TCqXoS («ais le n- initial peut
aussi reprdsenter p-) et k r. sl.kalu "boue" (aais on propose aussi
d'autres rapprocheaents: v. Trautaann, Balt. -sl. ifort., p.113 et suiv.) .
On sfe^a- initial n'§st pas atteatd, pour ce groupe, hors du latin.
squalus, -Ia.: squale, chien de aer. Quantitd de l'a inconnue;
la forae squalus que certains lisent dans Ov., Hal.133, est en r 4 alit 4
squatus. Si 1*5 4 tait long, squSlus pourrait au point de vue latip
fctre "1 * 4 cailleux, le rugueux", cf.squS.ma, ce qui convient A. la
peau du chien de aer; cf. en gr. o Xe7UBarroc.
Mais, pour designer un "gros poisson", le vieux prussien a kalis
"wels (silure)" et le vieil islandais hualr} avec a%— pr 4 c 4 d 4 de
prothese, le grec a aoroxXoc pour ddsigner un poisson. M.'Jules Bloch
signale le noa d'un poisson rouge d'eau douce, skr .chdla-.
squama, -ae f. : dcaille (sehs propre et figur 4 ). Ancien, tech-
nique, usuel. M.L.&xyg.
D 4 riv 4 s et coapos£s: squdmStus (Tert., Vulg.), cf. Xe 7 n 5 arr 6 c, squd-
mdtim (Plin.); sqjudmeus, squamosus, M.L.8303; squamula (Ceis.),
M.L.8301; desquSmS, ~Ss: 4 cailler, M.1.3603, d'ou *squSmdre, M.L.
8300 avec le aeae sens; squdmi-fer, -ger,-cutis (po 4 t.).
V, squSlus.
squarrosus, -a, -un: -i ab eadem squamarum similitudine dicti,
quorum cautis surgit ob assiduam inluuiem. Lucilius (1131): " uaronun
ac rupicum squarrosa incondita rostra "; P.F.443,x. Sans doute cor-
```


## [2026-09-14T02:03:40.635Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,5p' 32924127a4118ee5.txt; grep -n -i -A4 \"squalene\" 32924127a4118ee5.txt | grep -i \"latin\\|shark\\|origin\" | head -5"
}
```


### [2026-09-14T02:03:40.707Z] TOOL RESULT

```
URL: https://www.merriam-webster.com/dictionary/squalene
FETCHED: 2026-09-14T02:03:37Z
STATUS: -1
TITLE:
```


## [2026-09-14T02:04:07.693Z] TOOL CALL #72: WebSearch

```json
{
 "query": "Persian \"کرو\" ماهی نوعی ماهی سغدی krw کر ماهی ریشه اوستایی kara"
}
```


### [2026-09-14T02:04:14.379Z] TOOL RESULT

```
Web search results for query: "Persian "کرو" ماهی نوعی ماهی سغدی krw کر ماهی ریشه اوستایی kara"

Links: [{"title":"Persian Word of the Day - fish (noun) - PersianPod101.com Blog","url":"https://www.persianpod101.com/blog/2013/11/26/persian-word-of-the-day-fish-noun/"},{"title":"Essential Persian Vocabulary for Talking about Marine Animals & Fish","url":"https://www.persianpod101.com/persian-vocabulary-lists/marine-animals-fish"},{"title":"MasalBench: A Benchmark for Contextual and Cross-Cultural Understanding of Persian Proverbs in LLMs","url":"https://arxiv.org/pdf/2601.22050"},{"title":"ماهی - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%87%DB%8C"},{"title":"PEYMA: A Tagged Corpus for Persian Named Entities","url":"https://arxiv.org/pdf/1801.09936"},{"title":"The meaning of Fish in Persian or Farsi ماهی mahi - YouTube","url":"https://www.youtube.com/watch?v=W_3DWlgtnnc"},{"title":"Learn Persian Vocabulary: Seafood غذای دریایی","url":"https://www.learnpersianonline.com/beginners/persian-vocabulary/seafood/"},{"title":"Extending LLMs to New Languages: A Case Study of Llama and Persian Adaptation","url":"https://arxiv.org/pdf/2412.13375"},{"title":"How to say fish in Farsi","url":"https://www.wordhippo.com/what-is/the/farsi-word-for-64875fcccaac069fcb3e0e201e7d5b9166641608.html"},{"title":"What is \"Fish\" in Persian and how to say it?","url":"https://languagedrops.com/word/en/english/persian/translate/fish/"}]

Based on the search results, I found relevant information about Persian fish terminology and etymology:

The Persian word ماهی (māhī) is inherited from Middle Persian, from Proto-Iranian *mácyah, from Proto-Indo-Iranian *mátsyas, possibly borrowed from the BMAC substrate. It is cognate with Younger Avestan masiia and Sanskrit मत्स्य (mátsya).

However, the search results do not contain specific information about the term "کرو" (krw/karu) that you mentioned, or details about Sogdian fish terminology, the abbreviation "krw," or the Avestan root "kara" that you referenced in your query. The search results primarily focused on the general Persian word for fish (ماهی) and its Indo-European etymological origins rather than the specific term and etymological connections you were asking about.

To get more detailed information about that particular term and its linguistic connections, you might need to consult specialized Persian or historical linguistics resources that focus on Sogdian and Avestan languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:04:23.562Z] TOOL CALL #73: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:04:23.617Z] TOOL RESULT

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


## [2026-09-14T02:05:38.244Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== HRN kar fish ===\"; grep -n -i \"kar māhī\\|karmahi\\|Fisch\" HRN.txt | head -8; echo \"=== HUB ===\"; grep -n -i \"kara.*Fisch\\|Fisch\" HUB.txt | head -8"
}
```


### [2026-09-14T02:05:38.320Z] TOOL RESULT

```
=== HRN kar fish ===
7519:Das Suffix ist spezifisch iranisch (vergl. kurd. ktdäw,
8402:969. mahl 'Fisch'.
8405:aw. masya- 'Fisch'; phlv. mählk; ai. mätsya- 'Fisch*.
11124:aw. wdra- 'Otter'; ai. udrä- 'Krabbe, Fischotter (un-
11126:ahd. ottar, an. otr 'Fischotter' 3).
=== HUB ===
1264:und machte apuxt, ihn fiir einen Fisch haltend.
4035:spezifische Kennzeichen des Persischen ^), welches urspriing-
4067:mah; musu *Fisch* (Jezd, ZDMG. 35, 379) gegen np. maht; Wrzl. vac
4643:skr. madgti-; mdhi 'Fisch* = phi. mOhik : zd. masya-, skr.
6870:*Fisch\ phi. mOhik = zd. masya-, skr. matsya-.
6899:van-, ap. *artavan'\ aber phi. ahlav ist specifisch parsisch
6904:specifisch parsisch und wiirde echt mittelpersisch *amurt' oder
6909:aber das Wort ist specifisch parsisch und wiirde echt per-
```


## [2026-09-14T02:05:39.998Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && echo \"=== HENNING krw kpy ===\"; grep -n \"krw kpy\\|kar-kapi\\|karkapi\\|kpy\" HENNING_selected_papers.txt | head -8; echo \"=== ISS/DKS ===\"; grep -n \"kara- \\|kar fish\\|karkapi\" ISS_alt_DKS.txt | head -8"
}
```


### [2026-09-14T02:05:40.072Z] TOOL RESULT

```
=== HENNING krw kpy ===
5787:ky ‘ty zwstm[byyt) (9) Cty Ckpynd wm't’nd oo jyw [BrBnd) (10) [
7414:(8) 00 i mayx ‘Chwa(yly wt (9) (yy wayy cfylodr iit kpfyi: wo't(nd) i py “yw (10) deny eo 8Btyk kipyy) C dey b ey sty (11) kpyy ar im'rynyy"© wm't w'yw(k) [i "H(y)t "ty &'r pe Bt dh 'tyy swuyy Bw (13) yafAm'eynyt kpyityy "WB p ‘ty xwnyy ‘yw (14) kneyyée kpyy ayy nyt Bt 00
8032:(1) Jwys L! . [ (2) [0's CWRH sn’y'y yet em 2'kt ple'yw + about eight letters} (8) ZY kew kpy ® ywetS'rt mn’ ew yw'n’sty rty (4) c'n’kw ywBw MN 3f'mpnwh
8055:kw ! "py ‘pat ZY (20) [Ay krw kpy ywrt] 3'rt [
15107:(1) ays xxx werd sew fin every theeshold] are thirty (2) wyspw wefe)falyy xii xii ‘yal bazaars each, in each bazaar 12 8) ‘styy 00 wyfspy’] ‘yadtyy oyndrt ws, in each row [3}60 stalls. (4) (xxxx}xx kpy8 'styy 0 'rty my Those bazaars, stalls, rows
15108:(8) «oD kpy8t ‘yadt "ty w'erf (therein) are [fettered)
=== ISS/DKS ===
1191:usphis- 'rise up (water), be exalted, proud (mind), flash (rays), п 104/80 satsürüi mühsamüdrrd myäña üspiisadai ttyai vi au naravaundüü üspara vira pariphida ‘they establish (this world) upon the road to Nirvana, being exalted in the midst of the great ocean of migration” (see translation AM, n.s, 11, 1965, 104); compound with -kara- ‘making’, V 123, 19V4 (d) usphīsaroñä kará айй ‘there is no pride at all’, BS (Sukhavati-vyüha 7, verse 3) lenonnamanü na cüsti, wich BS unnamana 'pride'; и 104'6g-70 üsphisaryam bvaiyau jsa pyasti vajrráysa ‘the diamond-seat (BS vajrüsama-) decorated with up-rising rays'; H 104777-80 üsphisaradq-ütcyai drraisfiytnyam daga-raksaysyüm jsa panadai...mühasamüdrrà туййа 'in the midst of the great ocean with splashing waters noisy with the water-demons (BS udaka-rükgasa-) of heresies (BS drsfi-)'. From us with phis- to base bag- ' go fast’, hence from *bliag-sk-. *phays-, phis-. IE Pok. 116 bheg*- ' move fast, гип’, Greek фоно, póßos 'fear', Lit. bígu, bügti ' run', Slav. Russ. bégú, bésdti. See also below pahaj- ‘to flee’,
1340:kar- ‘о sow, plant', pres. Aer-, participle &álsta-, v 333, 2713 bissu vätä kumjsatu kerä ' he should sow everywhere sesame seed’, BS G 37, 2423-4 sa catursu dvipa-Rsetregu Шат vàápayet; v 334, 32v6-33r1 tcürimu vdtd kwnjsatà kerä, BS С 37, 29b6 loka-dhatau tilam vapayet; Z 4:35 ne ye nandanu kálste ‘опе has not planted the Nandana- grove’; I gr117 Аа? yudamdd; тїї $o'rg kaista jsará 'planted corn’; У 342, 84r1 bamhyu Rálste ‘Һе planted a tree’, BS G 37, 7837 vapito drumah; v 108, зоуб uru yädāndä sta kälstāndä sta uhu sddye Баро ' vou have done good, you have planted the root of goodness’, BS Arta- dhikarü avarapita-kusala-müla. With ni-, v здо, Sors nydsta- (as ed. Konow, not Rálsta-) Noun käljsa- ‘garden’, see below. Compounds, 11 28, 37b2 ganama- kerai ' wheat-sower', и 35, 8а8 Aamjsata-herü u ganama- Rerà 'sowers of sesame and wheat’; HI 14721 barija-kerai *sawer of crops', See also kara- ' field(?)'. From kar- ‘to scatter, Av. Айгауа-, beside karš-, karíta-, Zor.P. kistan, N.Pers. Айгай, kiftan, WI. Pers. T. Куй! ‘зом’, M.Parth.T. Ryit; Sogd. kyr-:kyštk; АИЛ 'seed'; Àfi'yc-kr'k, Sogd. Chr. gst'rt, qsd'rm; Balāčī Айар, ista ‘to sow, plough’; Oss, D. kalun, I. kalyn, kald ‘pour, scatter’, intransitive D. kälun, I. kälyn, kald; Pašto karal, Orm. kar- ‘to sow, till’, Suyni ¿zr- ‘to cultivate’, pret. črt, infinitive dërtõw, Sarikoli čār-, čārd-,Waxī küram, köštam ‘cultivatre,plough', Айт ' cultivation', Yazg. k'ar-:k'ard ' plant, cultivate’, IE Pok. 933-4 (s)Rer-, O.Ind. Аі, kīrud- ‘strew’,
1343:kara- ' monster fish', t1 10.4779 аглу karyau bhargyam ttamattamagalà prrünà jsa | ajaraista, . ,imühasamüdrrá myaña ' in the midst of the great sea haunted by the kara- beasts, the bAarga-beasts and the timitimingila-beasts'. From kara-, Ау. kara- ' monster fish’, Zor.P. kar māhīk, called the ratu- 'chief' of the fish, Sogd. krw kpy ‘the Rara-ish'. IE Pok. 958 (s)k*alos 'whale'. Note also Finnish kala ‘fish’, Hungarian Aal. See AM, n.s, rr, 1965, 113.
1344:kara- ‘surrounding’, partitive adjective, Sid. r42r2 karä kammä hainai hame, и ysida u üsem ‘the part around the woünd becomes red, and yellow, and blue’, BS pita-nila-, "Tib. тта dan, fien-skor-gyi mdog ser-5iy dmar-zin suo-ba dan; Sid. 14473 kard kammá и kamaña pisalyaiiá ‘around the wound and at its head it must be besmeared'; Sid. 147V4 hard tcimanüm ‘around the eyes', Tib. mig-gi phyi- rol; K 18:217 drrai tcira kara kathe parajüistauda ‘they three times wound it round the city’, BS Divyávadàna 448-1 sarvam tam nagaram antrair vegtitam; її 126:20-1 kara Ки hina büste u vari sti karā kamthe ‘he led the troop to the vicinity of the city and there it is around the city'; noun v 343, 87v2 bodhisatva kard váld àre 'the bodhisattvas sit around’, BS G 37, 5246 bodhi(satoa mahásatvà-saha)sra-parivrtah ‘surrounded by a thou- sand bodhisattvas, great beings’; Z 533 hard váti, Z 2-79 &ará vird; Z 3:115 karvira; N 176-1 karu ve. Adjective п
1347:kara- ‘enclosure, fort, town', it 1251 АЛуегой kara hina райатай базе ' we deigned to lead a troop to the Khyesa- Town (= Ka&yar)'. See АМ, n.s., 11, 1964, зо. Possibly to #аг- ' draw lines, enclose with lines’.
1353:karā va hambüm harastadá ' they presented the share for the kará-official', and гу 55a2 aharastá ' not given’. With this context can be compared the loan-word prahänaja- 'gift', BS prahenaka-, Pali pahenaka- 'gift', W 14, 2b2 uspurrá prahünaji hodi 'gave the full gift'; H 14, 2b7 prahánaji їй müra 5 hedä “ће gift one müra-coin, he gives 5'. See SD'TV 4. The two earlier attempts to inter- prer these phrases in 1v 146, and SD'TV 4 are here super- seded. The title kard is from older *kása-&ara- ‘watcher, protector, keeper', to the base Ads-:Ragfa-, with kara- ' maker ', beside kaka- ' protector from *kdsüka-' ; note the bases kät- and k- in kätāña-, kāña- 'to be cared for'. For the absence of -G-, see batai ‘opened’, Zor.P. vitataka-. The word ráysai ' gift' is from raz-, as Greek óp£yo ‘to stretch out, give'. The earlier rendering of kara by 'region' AM, n.s. 2, 1951, 9 is unsatisfactory.
1355:karavātä ‘іп the morning, betimes', Z 22:121 pand ssive ttändiku Бей karavātä vàátco vasusti ' every night it rains only so much, in the morning then it is clear'; Z 24:508 karavütd naltsute іп the morning he went out’; I1 115728 iva ата karavü “аі midnight, in the morning’; 1 181, 9974-5 karavà hhasaña 'it is to be drunk in the morning’. From kara- 'point of time' Sogd. kry' 'succession in time’, Мап. gry’; n'kry'£yg ‘untimely’ ; Oss. D. kara, І. kar tage of a person’, D. kargun, kardzud, kargin 'aged', DL ämgar ‘companion’, For ‘time’ for ‘early time’, note also N.Pers. pa-gāh ' early. The second component is rather -düta- as in Zor.P. bam-dat ‘dawn’, than *báta- ‘shining’, see s.v. baimya, Outside Iranian, note also O.Ind. kard-, ' point of time’, later &2/4- 'time', BS vikāla- ‘evening’, kālyam ‘early’, halyam eva ‘in the morning’.
1358:karünam '60,000 (villages), the one village 3oo[ooo] wards’; II 56:23 тагата karana drai-sse 'there 300 wards’; v 628 jau-karünüm jsa hvamdä drünü himüre 'men of the whole ward thereby become healthy’; H 104:90-1 visna-vakrrürma-sakhüra kitha káranü vara mäñadi pastai üirivye ће deigned to erect in che city the Visnu-vikrama- ürüma sanghárüma (monastery) like a court (vara) with enclosures’. See SDTV 70-72. From karana- to kara- ‘bounded space, enclosure, surroundings’, and ‘limit’, Av. karana- 'limit, end', akarana- 'unlimited', in the phrase Ya&t ro:9gg dasimam ира Бағапэт аїйһй zamó ‘at the right end of this earth'; Oss. D. Айғопӣ, I. kdron tend, side, fence’, hara käronmä ' from end to end’, dgár 'exceedingly'; Sogd. A&yr'n 'side, direction'; Zor.P. kanürak, N.Pers. karan, kanür ‘side’. See also tcalca-.
```


## [2026-09-14T02:05:52.075Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt; do echo \"== $f\"; grep -c -i \"walrus\" $f; done; echo \"=== FSD vol4 whale ===\"; grep -n -i \"walrus, *n\\|hwæl\\|hval\" FSD_vol4.txt | head -5"
}
```


### [2026-09-14T02:05:53.222Z] TOOL RESULT

```
== FSD_vol1.txt
2
== FSD_vol2.txt
2
== FSD_vol3.txt
9
== FSD_vol4.txt
13
=== FSD vol4 whale ===
79527:2,538  Khllchipur 7   Khiva 45  Khol 10  Khojent 13  Khokand 4   Khonsar 24  Khotan 41  Kbotin 3   Khulm 6   Khurja 23  Khvalynsk 10  Kiangsi 15  KInngsu 62  Klaochow 35  Kidder
```


## [2026-09-14T02:05:55.542Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n -i -o \".\\{80\\}walrus.\\{200\\}\" FSD_vol4.txt | head -4; echo \"=== squalene FSD ===\"; grep -n -i \"squalene\\|squalus\" FSD_vol4.txt | head -4"
}
```


### [2026-09-14T02:05:55.628Z] TOOL RESULT

```
5155:flsh  —   5ca*Irory,  n   Ivory obtained  from  marine  mammals  such  as  the  walrus-tusk  — sca-jclly,  R   A   Jellyfish  — sea*Kaic,  n   A   hardy  per- ennial herb  <Crambc  maritima)  of  the  musta’'d  family,  natlv  0 of  European  «cacoasts,  and  cultivated  for  Its  edib
19580:  2   The  blowhole  or  spiracle  of  a cetacean  also,  the  nostril  of  a   walrus  —   s   *sbell,  n   A   ma- rine aporrhaold  gastropod  hav- ing  Iho  outer  Up  of  the  shell expanded  and  spout-like  at  the ends  — up  the  s   [Slang], pau  n   See  spout,  n   ,   4   H
39130: bencalction Trlch'-c-chus,  n   (t  g )   — Trlch'^-e-cbrna,  n   pi  Mam The  walruses  as  a   subfamily  — trich'e-chlnfc^,  a   &   n   — trlch-cch'o-dont,  a   Having  teeth  with  cross-rldgcs,  as  In the  rricAfchifia?  or  manatees— trlch'e-chold  In  Of  or pertaining  to  t
50508:  hind  limbs  flexible forward  and  tusk-like  ca- nines in  the  upper  jaw "Walruses  fe^  mostlv  on blv  alve  moUusks,  which  the> obtain  by  digging  with  their tusks  They  are  usually found  near  the  coast  or  on floating  Ice  Rosmarus  ros- tnarus  Is  the  common*  
=== squalene FSD ===
19974:Squa'll,  1   skwe'li,  2   skwa'h,  n   pi  Ich  A   division  of selachians,  sharks  [   <   L   squalus,  shark  1   Squa'll-dat* SquaPid,  1   akwel'id,  2   skwal'id,  a   Having  a   dirty, mean,  poverty-stricken  appearance,  as,  a   squalid  cabin or  people  [<  L   squalidus,  <   Sffuaieo,  be  foul  ]   — squaP- Id-ly,  adv  —   squaPid-ness,  n   The  state  of  being  squalid squa-Hd'I-tyt*
19976:Squa'll-form,  1   skwe'Ii-ferm,  2   skwaMi-fdrra,  n   Having the  form  of  a   squalid  [   <   L   squalus,  shark,  +   -form  J squallb  Iskwel,  26kwal,tii  Toblov.  a   squall,  besquaU> used  impersonally,  as,  it  sguqffs  on  the  bay squalid  vt  &   ti  To  cry  loudly,  as  an  angry  child, scream  harshl>  usually  derogatory  ( <   Ice  skvala, scream  squalPer.  n   One  who  utters  a   squall Squalls  n   A   sudden  burst  of  wind,  as  in  a   thunder- storm. a   violent  wind  of  brief  duration,  often  accom- panied by  ram  or  snow,  as,  a   wind-squafi,  asnotv-aguaW, Si  dry  squall  Abbreviated  to  g   for  the  log-book  [< Sw  sqval,  rush  of  water,  <   sqvala,  gush  ]
19979:8qua'lo-don,  1   skwS'lo-den,  2   skwH'lo-dfin,  n   Jlfam  1* A   genus  typical  of  SqualodonUdx  2   [s-1  A   fossil  cetacean of  this  genus  [   <   Squalus  +   Gr  odous  {pdoni-) ,   tooth  ]   — Squa'qo-don'tl-dse,  n   pi  Mam  An  evtinct  family  of toothed  cetaceans  with  double-rooted  hind  molars  —   squa'- lo-dont,  a   &   n   —   squa"lo-don'tId,  n   —   squa'lo-don'- totd,  a   A   n
19980:squa'lold,  I   skwg'leld,  2   skwfi'lOld  I   a   Of  or  pertaining to  the  Squaltda:,  resembling  a   shark  II.  n   One  of  the Squalidx  [<  Squalus  + -oip  1 squal'or,  1   skwePer  or  akwC'ler,  2   skw^iPor  or  skwSMor Km),  n   The  state  or  condition  of  being  squalid,  or  the filth  of  thriftless  pov’ertj  ,   as,  the  squalor  of  the  slums [L  ,   <   squaleo,  be  foul  1
```


## [2026-09-14T02:06:01.648Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n -i -o \"Wal'rus.\\{0,350\\}\\|Whale, *1 .\\{0,300\\}\" FSD_vol4.txt | head -5; echo \"---\"; grep -n -o -i \"walrus,\\? *1 *.\\{0,300\\}\" FSD_vol4.txt | head -3"
}
```


### [2026-09-14T02:06:05.058Z] TOOL RESULT

```
---
ugrep: error: error at position 55
:[^\n\x80-\xbf][\x80-\xbf]*){0,300}
      exceeds complexity limits___/
```


## [2026-09-14T02:06:08.114Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && grep -n -i \"AS  hwael\\|AS hwæl\\|hwsel\\|hw.el,\" FSD_vol4.txt | head -5; echo \"--- walrus entry\"; awk '/Wal.rus/{print NR\": \"substr($0,1,400)}' FSD_vol4.txt | head -5"
}
```


### [2026-09-14T02:06:09.345Z] TOOL RESULT

```
--- walrus entry
```


## [2026-09-14T02:06:12.947Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ && sed -n '50505,50512p' FSD_vol4.txt | cut -c1-1200"
}
```


### [2026-09-14T02:06:13.022Z] TOOL RESULT

```
[<  AS  treoJicfan.  wallow  1   wal'owt.— waPIow-er, n   1. One  who  or  that  which  wallows  2   Macb  A   lantern-wheel TvaPlow*,  rf  [Prov  Brit]  To  fade  away TvaPloTV,a  [Prov  Png]  Having  no  flav  or  Insipid  flat wanoTV,  n   1.  The  act  of  wallowing,  a   rolling  about, as  in  mud  or  the  like  2.  That  in  which  animals  wal- low, a   pool,  mud-hole,  or  slough  frequented  bj  the  wa- ler-bufialo,  hippopotamus,  hog,  or  other  wallowing  ani- mal, also,  the  nouow  left  in  the  ground  showing  where an  ammal,  as  a   bison,  has  walloned But  idaat  by  the  time  all  three  [saddle-blanketfl]  were  well Bo&kcd  lo  the  copper-coloured  traJJoic  water  there  waa  not  a   drop left.  BAiLLir-GBOmtAN  Camps  in  the  Roefnea  p   37  [s  18S2  J
3.  A   rolling,  tumbbng  mov  ement,  as  of  billows  4t-  A rolling  walk  or  awkward  gait.  TValTlow-Iiigi.
85*
havung  hind  limbs  flexible forward  and  tusk-like  ca- nines in  the  upper  jaw "Walruses  fe^  mostlv  on blv  alve  moUusks,  which  the> obtain  by  digging  with  their tusks  They  are  usually found  near  the  coast  or  on floating  Ice  Rosmarus  ros- tnarus  Is  the  common*  arctic walrus  R   obesus  that  of  the  ,   , ,
North  Pacific  The  bulls  4Valrus  */-*
reach  12  feet  In  length  and  weigh  l*/j  tons  Both  are  killed for  their  hide  their  blubber  (which  yields  a   valuable  oil), their  lvor>,  and  their  flesh  [<  Sw  Tttalross  <   hzal  whale, -f
O   Sw  ross,  horse)  — Tval'ras»blrd",n  The  pectoral  sand- piper—TV.dron,  n   The  toggle-iron,  as  used  In  wakus- hunllng  Itown  in  Staffordshire,  England
Wal'sall,  1   wersel  2   wal'sal,  n   An  Iron-manufacturing Wal 'sen-burg,  1   wersen-burg,  2   warsSn-burg,  n   A   town, count  J   -seat  of  Huerfano  county,  Colo.
```


## [2026-09-14T02:07:30.845Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -c \"کرو\" BQT_v3_pages.txt BQT_v4_pages.txt 2>/dev/null; grep -n -o \".\\{0,60\\}کرو.\\{0,80\\}\" BQT_v4_pages.txt 2>/dev/null | head -8"
}
```


### [2026-09-14T02:07:34.783Z] TOOL RESULT

```
BQT_v4_pages.txt:44
BQT_v3_pages.txt:117
```


## [2026-09-14T02:07:36.905Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"کرو\" BQT_v4_pages.txt | head -12 | cut -c1-220"
}
```


### [2026-09-14T02:07:36.970Z] TOOL RESULT

```
1869:۴ - بدان حصار کروهی پناهکرده ( برده ) همی
2656:۴ - مردم اسم جمع است » و به ۶ مردمان > نیز جمع بسته میشود » قس : کروهان ۰
2701:مرده ) « ایض ۰۳۹۳ ۹4 ۰ ۳18 ( مردن ) « ایض ۳۹۹ > ؛ فوت کردن » وفات کرون +
3771:و کنایه از معدودی چند و کروهی الدك هم مشخنه ۷ « جم اولوفتح ثالی‌وسکون
3777:و کنایه ا ز کروهی اند4 از مردمان و آدمیان هم صبح دمیده وآفتاب برآهده » و بجای زال زر »
4899:خوانان باشد - وبکرالت . وعی ازقانی بای | ومتاع باشد ‎٩‏ - وکوزه وسبوی بی‌دسته وکرون
5450:کروه سواره . رك : شرح قاموی . ۹ - جمع جوکبی » منسوب به « موکب » (هم.)
7258:بی‌قکرواندیشه و بی‌نامل باشد چه سگالش بممنی قرشت و تحتانی ,کشت بان راگوبند که زراعت
7554:و مرد دانا ماهر‌درکار - ولظرف‌المدخل - و کازء صیاد ودامآن - ومرد سخن چین - ومکرو حيلهٌ
8347:وامق خوانند۱ » و چون برهفده رسد‌آترا دست | عربی سه معنی دارد : اول شرط و کرو قمارک »
8798:و کروهی استری نکویند . رودکی (سمرقندی) کوید :
8810:و ستیزنده و جنگه آور و ستیهنده - و ابید قعل شود در یکروزیمغرب رود و باز از مغرب پرواز
```


## [2026-09-14T02:11:48.647Z] TOOL CALL #83: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-458.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)k%CA%B7%C3%A1los\"\nW_GMC = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hwalaz\"\nW_SQUALENE = \"https://en.wiktionary.org/wiki/squalene\"\nW_SQUALUS = \"https://en.wiktionary.org/wiki/squalus\"\nW_WALRUS = \"https://en.wiktionary.org/wiki/walrus\"\nE_WALRUS = \"https://www.etymonline.com/word/walrus\"\nE_WHALE = \"https://www.etymonline.com/word/whale\"\nAHD = \"https://www.ahdictionary.com/word/indoeurop.html\"\nIRANICA = \"https://www.iranicaonline.org/articles/fish-iii/\"\nABADIS = \"https://abadis.ir/fatofa/%DA%A9%D8%B1%D9%88/\"\nVAJEH = \"https://vajehyab.com/dehkhoda/%DA%A9%D8%B1%D9%88\"\n\nentry = {\n  \"entry\": 4,\n  \"root\": \"Skwalo, Skwalos, Kwalo, Kwalos, Kwal\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *(s)kʷálos m. 'large fish (sheatfish; Gmc. whale)' — Pokorny 958 '(s)kʷalo-s oder vielmehr kʷalo-s'\",\n  \"note\": (\"Pokorny p. 958 heads the article '(s)kʷalo-s oder vielmehr kʷalo-s \\\"eine größere Fischart\\\"?' — i.e. both the \"\n           \"s-mobile form and the plain kʷalo- form, which is exactly what Nourai's five variant spellings \"\n           \"(Skwalo/Skwalos/Kwalo/Kwalos/Kwal) render; the language label 'Indo-European' and the gloss 'a big fish' are \"\n           \"right, 'whale' being the Germanic narrowing of the sense. Modern handbooks keep the root: Wiktionary \"\n           \"*(s)kʷálos 'large fish, sheatfish' (Mallory–Adams 2006:147, Kroonen 2013:262), Mann IEC 'qualos, is \"\n           \"\\\"sea-monster\\\"'. Two things a reader should know. (1) Pokorny's own article ends by pulling the Iranian member \"\n           \"out of Indo-European: 'der mythische Fisch av. kara- ist die iran. Wiedergabe eines urmordwin. *kola \\\"Fisch\\\", \"\n           \"später kal, zu tscherem. kol, lapp. guole, finn. kala usw.; die ganze Sippe also wohl finno-ugr. Herkunft' — \"\n           \"whereas Walde–Pokorny II 541 (1927) had still listed 'avest. kara- \\\"ein mythischer Fisch\\\"' as a normal IE \"\n           \"cognate (after Vasmer). Nourai's chart follows the older, IE-internal picture. (2) The root has since been \"\n           \"dropped from the AHD appendix: Watkins 1985 still has '(s)kwal-o-. Big fish' with WHALE, NARWHAL, RORQUAL, \"\n           \"SQUALENE, but the current online AHD appendix (5th ed.) has no entry between skrībh- and slēb-, and whale is \"\n           \"no longer traced to an IE root there.\"),\n  \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *(s)kʷálos «ماهی بزرگ» است. پوکورنی در صفحهٔ ۹۵۸ سرواژه را به‌صورت «(s)kʷalo-s یا بهتر \"\n              \"بگوییم kʷalo-s» آورده و همین دوگانگیِ با س‌آغازین و بی‌س‌آغازین، همان پنج صورتی است که نورایی نوشته است؛ پس نام \"\n              \"ریشه، برچسب زبانی و معنای «ماهی بزرگ» درست است و معنای «نهنگ» تنها تخصیصِ معناییِ شاخهٔ ژرمنی است. دو نکته: \"\n              \"نخست آنکه خودِ پوکورنی در پایانِ همان مقاله «karaـ»ی اوستایی را وام‌واژه‌ای از اورالی (مردویی آغازین *kola «ماهی») \"\n              \"می‌داند و کل خانواده را «احتمالاً فینو-اوگری» می‌شمارد، حال آنکه والده-پوکورنی (جلد دوم، ص ۵۴۱) آن را هم‌ریشهٔ \"\n              \"هندواروپایی دانسته بود؛ نورایی از تصویر کهن‌ترِ والده-پوکورنی پیروی کرده است. دوم آنکه پیوستِ ریشه‌های هندواروپاییِ \"\n              \"فرهنگ American Heritage در ویرایش تازه این ریشه را یکسره حذف کرده است، هرچند در ویرایش واتکینز ۱۹۸۵ هنوز هست.\"),\n  \"sources\": [W_PIE, AHD],\n  \"ref_check\": [\n    {\"ref\": \"POK:958\", \"status\": \"supports\",\n     \"note\": (\"POK_03.txt l. 2632 / POK_full.txt l. 77848 (printed p. 958): '(s)kʷalo-s oder vielmehr kʷalo-s \\\"eine größere \"\n              \"Fischart\\\"? Lat. squalus \\\"ein größerer Meerfisch\\\" … aisl. hvalr m. (neben -hveli n.) \\\"Walfisch\\\" (i-St.), ags. \"\n              \"hwæl, engl. whale, as. ahd. hwal … apr. kalis \\\"Wels\\\" … der mythische Fisch av. kara- …'. The root name, the \"\n              \"language label and the gloss are Pokorny's; the page is exactly where Nourai says it is.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 541 (incoming/WLD/WLD_Bd2_pages.txt l. 35937-35948)\", \"stance\": \"supports\",\n     \"note\": (\"'(s)qʷalo-s \\\"für große Fischarten\\\". Lat. squalus \\\"ein größerer Meerfisch (Meersaufisch?)\\\"; anord. hvalr … ags. \"\n              \"hwæl, ahd. (h)wal … apr. kalis \\\"Wels\\\" …; avest. kara- \\\"ein mythischer Fisch\\\" (Vasmer …)'. In 1927 the Avestan \"\n              \"word is still an IE cognate; only the closing remark 'Beachtenswert sind finn. Anklänge' foreshadows the later \"\n              \"Uralic explanation.\")},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)kwal-o- (AHD_watkins1985.txt l. 949)\", \"stance\": \"supports\",\n     \"note\": (\"'(s)kwal-o-. Big fish. 1. Suffixed form *kwal-o- in Germanic *hwalaz, whale, in: a. Old English hwæl, whale: \"\n              \"WHALE; b. Old Norse hvalr, whale: NARWAL, RORQUAL. 2. Latin squalus, a sea fish: SQUALENE. [Pok. (s)kʷalo- 958.]'\")},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. qualos (IEC.txt l. 13874)\", \"stance\": \"supports\",\n     \"note\": (\"'qualos, is \\\"sea-monster\\\": Av. karə, m. \\\"chief of the fishes\\\"; Ir. cail, f. \\\"brown trout; hag\\\"; OHG hwal, OE \"\n              \"hwæl, ON hvalr, m. \\\"whale\\\"; OPr. kalis, id.; (LW in Finn. valas, id.)' — Mann keeps the Iranian word inside \"\n              \"Indo-European and, like Nourai, sets up the root without s-.\")},\n    {\"src\": \"ISS\", \"where\": \"Bailey, DKS s.v. kara- 'monster fish' (ISS_alt_DKS.txt l. 1343)\", \"stance\": \"supports\",\n     \"note\": (\"'From kara-, Av. kara- \\\"monster fish\\\", Zor.P. kar māhīk, called the ratu- \\\"chief\\\" of the fish, Sogd. krw kpy \"\n              \"\\\"the kara-fish\\\". IE Pok. 958 (s)kʷalos \\\"whale\\\". Note also Finnish kala \\\"fish\\\", Hungarian kal.' Bailey holds the \"\n              \"IE comparison and the Uralic look-alikes side by side, which is the state of the question.\")},\n    {\"src\": \"SYN\", \"where\": \"Buck, grep 'squalus', 'hvalr'\", \"stance\": \"silent\",\n     \"note\": \"Buck has no 'whale/fish' synonym article touching this root; grep for squalus and hvalr in SYN.txt returns nothing.\"}\n  ],\n  \"nodes\": []\n}\n\nnodes = []\n\nnodes.append({\n  \"id\": 1,\n  \"lang\": \"Avestan\",\n  \"words\": \"kara 2\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Av. kara- is the giant mythical fish of the Yašts and (as kar-māhīg) of the Bundahišn: Bartholomae AiW col. 451 \"\n    \"'1. kara- n. Name eines Fisches' with Yt. 14.29 'masiiō upāpō yō raŋhaiia …' and the footnote 'Im Mp. kar māhīk, ein \"\n    \"mythischer Fisch, der grösste und Ratu der Fische; vgl. Bd. 14.11, 34.13'. Formally the arrow root→Avestan is regular: \"\n    \"PIE *(s)kʷálos > Proto-Indo-Iranian *(s)káras (IE labiovelar *kʷ loses its labial element before *a in Indo-Iranian, \"\n    \"giving k) > Proto-Iranian *(s)kárah > Av. kara- (thematic stem, nom. sg. karō); this is the chain Wiktionary draws and \"\n    \"the one Mann assumes ('Av. karə m. chief of the fishes'). Nourai's gloss 'whale' is a modernisation: the Avestan animal \"\n    \"is a monstrous fish, 'the rad (chief) of water creatures', never a cetacean (Iranica, FISH iii; Bundahišn 13.10, 17.14, \"\n    \"24.1-5). The reason for 'plausible' rather than 'confirmed' is the page Nourai cites: Pokorny 958 explicitly takes the \"\n    \"Avestan word OUT of the inherited family — 'der mythische Fisch av. kara- ist die iran. Wiedergabe eines urmordwin. *kola \"\n    \"\\\"Fisch\\\" … die ganze Sippe also wohl finno-ugr. Herkunft' (after Jacobsohn, Arier und Ugrofinnen 241 f.) — whereas \"\n    \"Walde-Pokorny II 541, Mann and Wiktionary keep it inside Indo-European. The '2' in 'kara 2' is Nourai's own homonym \"\n    \"number (Bartholomae numbers this one 1. kara-, his 2. kara- being the Turanian proper name).\"),\n  \"derivation_fa\": (\n    \"«کَرَ» (kara-) در اوستا نام ماهی بزرگ و اسطوره‌ای است؛ بارتولومه در ستون ۴۵۱ فرهنگ ایرانی باستان آن را «نام یک ماهی» \"\n    \"می‌خوانَد و در پانوشت می‌افزاید که در فارسی میانه kar māhīk است، «بزرگ‌ترین و رَدِ ماهیان» (بندهش ۱۴٫۱۱). از نظر آوایی زنجیره \"\n    \"منظم است: هندواروپایی *(s)kʷálos ← هندوایرانی آغازین *(s)káras (واکهٔ لبی‌کامیِ *kʷ در هندوایرانی پیش از a به k بدل می‌شود) \"\n    \"← ایرانی آغازین *(s)kárah ← اوستایی kara-. معنای «نهنگ» که نورایی آورده امروزی‌سازی است؛ کَر در متون زردشتی ماهیِ سترگ و \"\n    \"«رَدِ آبزیان» است نه پستاندار دریایی. علت آنکه حکم را «با احتیاط پذیرفتنی» گذاشته‌ایم این است که خودِ صفحهٔ استنادیِ نورایی \"\n    \"(پوکورنی ۹۵۸) این واژه را وام‌واژه‌ای از اورالی (مردویی آغازین *kola) می‌داند، حال آنکه والده-پوکورنی، مان و ویکی‌واژه آن را \"\n    \"هم‌ریشهٔ هندواروپایی می‌شمارند. شمارهٔ «۲» در «kara 2» شمارشِ هم‌نام‌های خودِ نورایی است.\"),\n  \"sources\": [W_PIE, IRANICA],\n  \"ref_check\": [\n    {\"ref\": \"POK:958\", \"status\": \"partial\",\n     \"note\": (\"POK_03.txt l. 2637: the Avestan word IS on the cited page, but as a loan, not a descendant — 'der mythische \"\n              \"Fisch av. kara- ist die iran. Wiedergabe eines urmordwin. *kola \\\"Fisch\\\", später kal, zu tscherem. kol, lapp. \"\n              \"guole, finn. kala usw.; die ganze Sippe also wohl finno-ugr. Herkunft'. Nourai's arrow root→kara is therefore \"\n              \"not what POK:958 says; it is what WP II 541 (cited by Pokorny himself) says.\")},\n    {\"ref\": \"SOD:194\", \"status\": \"supports\",\n     \"note\": (\"Gharib no. 4878 (printed p. 194, SOD.txt l. 39954-39960): 'krw kpy M … kar(w)-kapi ©<Av. kara; <IE *skvalos, \"\n              \"whale-, Finnish kala; Hung. kal | Kar fish (a kind of fish), cat-fish?, whale?' — Gharib states the Avestan \"\n              \"etymon and the IE root exactly as Nourai's chart draws them.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW col. 451-452 s.v. 1. kara- (BRT.txt l. 9227-9231)\", \"stance\": \"supports\",\n     \"note\": (\"'1. kara- n. Name eines Fisches' with the Yt. 14.29 passage 'masiiō upāpō yō raŋhaiia … V. sg. 4a', and the \"\n              \"footnote 'Im Mp. kar māhīk, ein mythischer Fisch, der grösste und Ratu der Fische'. The Avestan word and its \"\n              \"sense are secure; Bartholomae gives no IE etymology here.\")},\n    {\"src\": \"ISS\", \"where\": \"Bailey, DKS s.v. kara- 'monster fish' (ISS_alt_DKS.txt l. 1343)\", \"stance\": \"supports\",\n     \"note\": (\"'From kara-, Av. kara- \\\"monster fish\\\", Zor.P. kar māhīk … Sogd. krw kpy \\\"the kara-fish\\\". IE Pok. 958 (s)kʷalos \"\n              \"\\\"whale\\\". Note also Finnish kala \\\"fish\\\", Hungarian kal. See AM, n.s. 11, 1965, 113.' — Khotanese kara- is a \"\n              \"further Iranian witness Nourai does not use.\")},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. qualos (IEC.txt l. 13874)\", \"stance\": \"supports\",\n     \"note\": \"'qualos, is \\\"sea-monster\\\": Av. karə, m. \\\"chief of the fishes\\\"; … OE hwæl, ON hvalr … OPr. kalis' — the Avestan word listed as an inherited cognate.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 541 (incoming/WLD/WLD_Bd2_pages.txt l. 35945)\", \"stance\": \"supports\",\n     \"note\": \"'avest. kara- \\\"ein mythischer Fisch\\\" (Vasmer Festschr. Baudouin de Courtenay 83)' listed among the IE forms, with no loan caveat.\"},\n    {\"src\": \"HUB\", \"where\": \"grep 'Fisch', 'kara' in HUB.txt\", \"stance\": \"silent\",\n     \"note\": \"Hübschmann's Persische Studien discusses only māhī 'fish' (= phl. māhīk, zd. masya-); no kara-/kar entry.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 2,\n  \"lang\": \"Sogdian\",\n  \"words\": \"krw\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"The Sogdian word is real but is attested as a compound: Gharib no. 4878 (p. 194) 'krw kpy' (Manichaean script), \"\n    \"kar(w)-kapi, glossed 'Kar fish (a kind of fish), cat-fish?, whale?', with the references Bailey, Asia Major n.s. 11 \"\n    \"(1965) 113 and Henning, Sogdian Tales 483 — and the text itself has it: Henning's transcription of the Sogdian tale \"\n    \"reads '… ZY krw kpy …' (HENNING_selected_papers.txt l. 8032, 8055). Bailey translates it 'the kara-fish' (DKS s.v. \"\n    \"kara-). Two qualifications to the node as drawn. (a) The headword 'krw' on its own in Gharib's list is a different word \"\n    \"(no. 4875 krw* karwa 'gap'; cf. no. 4877 krw δnt'k 'gap-toothed'); Nourai has isolated the first member of krw kpy and \"\n    \"given it the compound's gloss. (b) The arrow Avestan→Sogdian is genealogically loose: Sogdian krw and Avestan kara- are \"\n    \"sister continuations of the same Old Iranian *kara- 'monster fish' (Gharib's '<Av. kara' is a statement of etymon, not \"\n    \"of borrowing), though the mythological subject-matter means a Zoroastrian literary transmission cannot be excluded.\"),\n  \"derivation_fa\": (\n    \"صورت سغدیِ این واژه در فرهنگ قریب (شمارهٔ ۴۸۷۸، ص ۱۹۴) به‌شکل ترکیبی «krw kpy» (کَر-کَپی) آمده است با معنای «ماهی کَر، نوعی \"\n    \"ماهی، گربه‌ماهی؟، نهنگ؟» و ارجاع به بیلی (۱۹۶۵) و هنینگ؛ در متن سغدیِ «داستان‌های سغدی» نیز همین ترکیب دیده می‌شود. دو نکته: \"\n    \"یکم، «krw» به‌تنهایی در همان فرهنگ (شمارهٔ ۴۸۷۵) واژهٔ دیگری است به معنای «شکاف»، و نورایی جزء نخستِ ترکیب را جدا کرده و \"\n    \"معنای کلِ ترکیب را به آن داده است. دوم، پیکانِ اوستایی ← سغدی دقیق نیست: کَرِ اوستایی و krwِ سغدی هر دو دنبالهٔ مستقلِ \"\n    \"ایرانی باستان *kara- اند، یعنی هم‌ریشه‌اند نه وام‌گرفته؛ البته چون موضوع اسطوره‌ایِ زردشتی است، انتقال ادبی را هم نمی‌توان یکسره رد کرد.\"),\n  \"sources\": [W_PIE],\n  \"ref_check\": [\n    {\"ref\": \"SOD:194\", \"status\": \"supports\",\n     \"note\": (\"Gharib no. 4878 is printed on p. 194 (the page number '195' follows it in SOD.txt l. 39964), so Nourai's page \"\n              \"reference is right: 'krw kpy M … kar(w)-kapi ©<Av. kara; <IE *skvalos, whale-, Finnish kala; Hung. kal | Kar \"\n              \"fish(a kind of fish), cat-fish ?, whale ? | Bailey. AM 1965, 113; Hen. Tales. 483.3'. Support with the caveat \"\n              \"that the lemma is the compound, not bare krw.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"ISS\", \"where\": \"Bailey, DKS s.v. kara- (ISS_alt_DKS.txt l. 1343)\", \"stance\": \"supports\",\n     \"note\": \"'… Zor.P. kar māhīk … Sogd. krw kpy \\\"the kara-fish\\\". IE Pok. 958 (s)kʷalos \\\"whale\\\".' — independent confirmation of the Sogdian form, its meaning and its Avestan/IE connection.\"},\n    {\"src\": \"HENNING\", \"where\": \"Selected Papers, Sogdian text transcription (HENNING_selected_papers.txt l. 8032, 8055)\", \"stance\": \"supports\",\n     \"note\": \"'(3) ZY krw kpy …' and '… [ZY] krw kpy ywrt …' — the compound in a running Sogdian text (Henning's 'Sogdian Tales'), which is Gharib's source.\"},\n    {\"src\": \"POK\", \"where\": \"p. 958 (POK_03.txt l. 2632-2640)\", \"stance\": \"silent\",\n     \"note\": \"Pokorny's article lists Latin, Germanic, Old Prussian and Avestan, but no Sogdian form.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 3,\n  \"lang\": \"Persian\",\n  \"words\": \"karv «کرو»\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"The printed page (pdf 458) does show 'karv : a kind of fish' with the script «کَرو», so the extraction is faithful and \"\n    \"the problem is the claim itself. No Persian dictionary knows a word کرو 'fish'. Dehkhoda s.v. کرو gives: (i) کَرَو, the \"\n    \"white web a spider spins for its eggs (from Borhān, Ānandrāj); (ii) کِرَو / کَرْو 'hollow, decayed (of a tooth)' with \"\n    \"Kasāʾi's and Rudaki's verses; (iii) کِرَو 'a small boat, sonbuk' (Jahāngiri, Borhān); (iv) 'bitter lettuce, chicory' \"\n    \"(Nāẓim al-Aṭibbāʾ); (v) the Arabic infinitive کَرْو; plus the proper name کُرو (Garōy). Moʿin's entry repeats only the \"\n    \"'small boat' sense. The genuine Persian reflex of Av. kara- is کَر / کَرماهی: MP kar-māhīg, 'the biggest of the aquatic \"\n    \"creatures' and 'the rad (chief) of water creatures' (Bundahišn 13.10, 17.14, 24.1-5; Iranica, FISH iii), Bailey's \"\n    \"'Zor.P. kar māhīk'. Nourai's node looks like Gharib's Sogdian krw (his own reference SOD:194) re-labelled as New \"\n    \"Persian: the page he cites is a Sogdian–Persian dictionary whose Persian column merely glosses the Sogdian entry, and \"\n    \"it records no New Persian headword کرو. The node should read کر / کرماهی, or be deleted.\"),\n  \"derivation_fa\": (\n    \"در چاپِ کتاب به‌روشنی «کَرو : نوعی ماهی» آمده است، پس خطای خوانشِ اسکن در کار نیست و اشکال در خودِ ادعاست. هیچ فرهنگ فارسی \"\n    \"«کرو» را به معنای ماهی ثبت نکرده است: دهخدا زیر «کرو» این معناها را می‌آورد: پردهٔ سفیدِ عنکبوت (به نقل از برهان و آنندراج)، \"\n    \"دندانِ میان‌تهی و کاواک (با شاهد از کسائی و رودکی)، کشتی و جهازِ کوچک (سنبک)، کاهوی تلخ/کاسنی، و مصدر عربیِ کَرْو؛ معین نیز \"\n    \"تنها معنای «زورق» را دارد. بازماندهٔ راستینِ «کَرَ»ی اوستایی در فارسی «کَر/کَرماهی» است: فارسی میانه kar-māhīg، بزرگ‌ترین \"\n    \"آبزی و «رَدِ ماهیان» در بندهش، که بیلی هم آن را «Zor.P. kar māhīk» می‌نویسد. چنین می‌نماید که نورایی همان krwِ سغدیِ فرهنگِ \"\n    \"قریب را با برچسبِ «فارسی» آورده باشد؛ فرهنگِ قریب سغدی-فارسی است و ستونِ فارسیِ آن تنها معنای واژهٔ سغدی را می‌دهد، نه سرواژه‌ای \"\n    \"فارسی به‌نام «کرو». پژوهش امروزی این گره را نمی‌پذیرد و به‌جای آن «کر/کرماهی» می‌گذارد.\"),\n  \"sources\": [ABADIS, VAJEH, IRANICA],\n  \"ref_check\": [\n    {\"ref\": \"SOD:194\", \"status\": \"partial\",\n     \"note\": (\"Gharib p. 194 no. 4878 has the Sogdian compound krw kpy with its Persian/English glosses and the note '<Av. \"\n              \"kara; <IE *skvalos'; it is a Sogdian lemma. Nothing on that page establishes a New Persian word karv «کرو» \"\n              \"'a kind of fish'.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep 'کرو' + 'ماهی'\", \"stance\": \"silent\",\n     \"note\": \"No Moʿin entry pairs کرو with ماهی; via vajehyab/abadis Moʿin s.v. کرو gives only 'قایق' (small boat), with Saʿdi's line, and adds that even that sense is doubted (Rašidi).\"},\n    {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ s.v. کرو, as quoted by Dehkhoda\", \"stance\": \"contradicts\",\n     \"note\": \"Dehkhoda cites Borhān three times under کرو — 'پردهٔ سفیدی … که عنکبوت سازد', 'دندانی … که میان آن تهی و کاواک شده باشد', 'کشتی و جهاز کوچک' — no fish. (The BQT vol. 3-4 page OCR is too noisy to grep directly: hits for کرو there are all OCR of گروه.)\"},\n    {\"src\": \"ISS\", \"where\": \"Bailey, DKS s.v. kara- (ISS_alt_DKS.txt l. 1343)\", \"stance\": \"partial\",\n     \"note\": \"Gives the Iranian series as 'Av. kara-, Zor.P. kar māhīk, Sogd. krw kpy' — i.e. the Persian continuation is kar (māhīg), not karv.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss, grep 'kar', 'Fisch' (HRN.txt no. 969 māhī)\", \"stance\": \"silent\",\n     \"note\": \"Horn has no کرو and no کر 'fish'; his only fish word is no. 969 'māhī \\\"Fisch\\\"' (aw. masya-, phlv. māhīk).\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 4,\n  \"lang\": \"Germanic\",\n  \"words\": \"hwaliz\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Proto-Germanic *hwal-i-z / *hwal-a-z 'whale' < PIE *(s)kʷálos by Grimm's law: the IE labiovelar *kʷ becomes PGmc *hʷ \"\n    \"(spelt hw-) and the thematic ending *-os becomes *-az. Nourai's i-stem 'hwaliz' is not a slip: Old Norse hvalr is an \"\n    \"i-stem (Pokorny 958 notes '(i-St.)', pl. hvalir; Walde-Pokorny II 541 'anord. hvalr, pl. hvalir'), and Kroonen (EDPG \"\n    \"2013: 262) lemmatises the word as *hwali-, though Watkins and Wiktionary print the a-stem *hwalaz. The attested \"\n    \"daughters are OE hwæl, OS/OHG hwal, ON hvalr, with the compound type MDu. walvisc, OHG walfisc, G. Walfisch; alongside \"\n    \"them OHG hwelira, G. Waller/Weller and MHG wels 'sheatfish' (*hwali-s-), which shows that the Germanic branch had \"\n    \"narrowed an inherited 'big fish' to 'whale' while keeping the freshwater sense in the s-stem.\"),\n  \"derivation_fa\": (\n    \"ژرمنی آغازین *hwaliz/*hwalaz «نهنگ» بازماندهٔ مستقیم *(s)kʷálos است: بنا بر قانون گریم، *kʷ هندواروپایی در ژرمنی به *hʷ \"\n    \"(نوشتهٔ hw-) بدل می‌شود و پایانهٔ *-os به *-az. صورتِ «hwaliz» که نورایی آورده خطا نیست؛ hvalrِ نورس باستان ستاکِ i است \"\n    \"(پوکورنی خود می‌نویسد «i-St.»، جمع hvalir) و کرونن در فرهنگ ریشه‌شناختی ژرمنی آغازین (۲۰۱۳، ص ۲۶۲) همان *hwali- را \"\n    \"سرواژه کرده است، هرچند واتکینز و ویکی‌واژه *hwalaz می‌نویسند. بازماندگان: hwælِ انگلیسی کهن، hwalِ ساکسونی و آلمانی علیای \"\n    \"کهن، hvalrِ نورس، و ترکیب‌های walvisc/walfisch. ادعای نورایی درست است.\"),\n  \"sources\": [W_GMC, E_WHALE],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": (\"Watkins 1985 s.v. (s)kwal-o- (AHD_watkins1985.txt l. 949): '1. Suffixed form *kwal-o- in Germanic *hwalaz, \"\n              \"whale, in: a. Old English hwæl, whale: WHALE; b. Old Norse hvalr, whale: NARWAL, RORQUAL.' Same node, same \"\n              \"root; AHD prints the a-stem *hwalaz where Nourai has the i-stem hwaliz.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1971 s.v. whale (KLN_1971.txt l. 266288)\", \"stance\": \"supports\",\n     \"note\": \"'whale, n. — ME. whale, whal, fr. OE. hwæl, rel. to OS. hwal, ON. hvalr, hvalfiskr, Swed. val, MDu. wal, walvisc, Du. walvis, OHG. wal, walfsc … and prob. cogn. with OPruss. kalis, \\\"shad\\\", … L. squalus, \\\"a kind of sea fish\\\".'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 541 (WLD_Bd2_pages.txt l. 35940-35944)\", \"stance\": \"supports\",\n     \"note\": \"'anord. hvalr, pl. hvalir m. \\\"Walfisch\\\" (i-St.), ags. hwæl, ahd. (h)wal, (h)welira \\\"Walfisch\\\" … mhd. nhd. wels' — the i-stem inflection Nourai's *hwaliz presupposes.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Persian entry «وال» (incoming/ARY/ARY_latin_index_pages.txt l. 15001-15007, pdf page 513 = printed 512)\", \"stance\": \"supports\",\n     \"note\": \"The Persian entry aligns HWÆL (OLD ENGLISH), WHALE (ENGLISH), HVALR (OLD SCANDINAVIAN), HWAL (OLD SAXON), WAL/WALFISC (OLD HIGH GERMAN), KALIS (OLD PRUSSIAN) and SQUALUS (LATIN), citing Pokorny — the same family, independently of Nourai.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 5,\n  \"lang\": \"English\",\n  \"words\": \"whale, walrus\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"whale is a straight inheritance: PGmc *hwalaz/*hwaliz > OE hwæl 'whale, also walrus' > ME whal, whale > NE whale \"\n    \"(Watkins: 'Old English hwæl, whale: WHALE'; Klein s.v. whale; Etymonline s.v. whale). walrus is a different story and \"\n    \"is why the node is only 'plausible': it enters English in the 1650s from Dutch walrus, which is itself a \"\n    \"folk-etymological reshaping — after Du. walvis 'whale' and ros 'horse' — of a Scandinavian 'horse-whale' compound with \"\n    \"the two members in the other order: ON hrossvalr / rosmhvalr, Sw. vallross, Da. hvalros, matching OE horschwæl \"\n    \"(Klein 1971 s.v. walrus: 'Du., fr. Swed. vallross, fr. ON. hrossvalr (cp. OE. horshwæl), lit. \\\"horse whale\\\"'; Skeat \"\n    \"s.v. walrus; Funk & Wagnalls: '[< Sw. hvalross < hval whale, + O Sw ross, horse]'). So walrus does contain the whale \"\n    \"word, but by way of 17th-c. Dutch and with metathesis of the compound, not by descent from Germanic *hwaliz; Etymonline \"\n    \"adds that the first element may ultimately be a garbled Lapp morsa / Finnish mursu. Watkins 1985 does not list WALRUS \"\n    \"under (s)kwal-o- at all (only WHALE, NARWAL, RORQUAL), so the AHD reference on this node covers whale only.\"),\n  \"derivation_fa\": (\n    \"«whale» بازماندهٔ مستقیم است: ژرمنی *hwalaz ← انگلیسی کهن hwæl ← انگلیسی میانه whal(e) ← انگلیسی نو whale. اما «walrus» \"\n    \"(گراز دریایی) چنین نیست و حکمِ این گره را به «با احتیاط پذیرفتنی» فرو می‌کاهد: این واژه در دههٔ ۱۶۵۰ از هلندی walrus به \"\n    \"انگلیسی رسیده و خودِ صورتِ هلندی دگرگون‌شدهٔ ترکیبی اسکاندیناویایی است به معنای «نهنگ-اسب» با جابه‌جاییِ دو جزء (قلب): \"\n    \"hrossvalr / rosmhvalrِ نورس باستان، vallrossِ سوئدی، hvalrosِ دانمارکی، برابرِ horschwælِ انگلیسی کهن؛ ریشه‌شناسی عامیانه \"\n    \"زیر تأثیر walvis «نهنگ» و ros «اسب» آن را به شکل کنونی درآورده است. پس جزءِ «نهنگ» در آن هست، ولی واژه وام‌واژه‌ای هلندی \"\n    \"است نه بازماندهٔ مستقیمِ *hwaliz؛ واتکینز نیز walrus را ذیل این ریشه نیاورده است.\"),\n  \"sources\": [E_WALRUS, E_WHALE, W_WALRUS],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\",\n     \"note\": (\"Watkins 1985 s.v. (s)kwal-o- (l. 949) yields WHALE (from OE hwæl) and, from ON hvalr, NARWAL and RORQUAL; the \"\n              \"index (l. 2281) lists SQUALENE under (s)kwal-o- but has no WALRUS entry at all. The AHD citation therefore \"\n              \"supports 'whale' and does not support 'walrus'.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1971 s.vv. walrus (l. 264725) and whale (l. 266288)\", \"stance\": \"partial\",\n     \"note\": \"'walrus, n. — Du., fr. Swed. vallross, fr. ON. hrossvalr (cp. OE. horshwæl), lit. \\\"horse whale\\\", fr. hross, \\\"horse\\\", and hvalr, \\\"whale\\\".' — the whale element yes, the direct descent no.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. walrus (SKT.txt l. 21353)\", \"stance\": \"partial\",\n     \"note\": \"'walrus, a large seal (Du. - Scand.) Du. walrus — Swed. vallross, Dan. hvalros, … cf. A.S. hors-hwæl, a morse, horse-whale' — same analysis.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. walrus (FSD_vol4.txt l. 50508-50509)\", \"stance\": \"partial\",\n     \"note\": \"'[< Sw hvalross < hval whale, + O Sw ross, horse]' — confirms the compound and the Scandinavian route.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 6,\n  \"lang\": \"Latin\",\n  \"words\": \"squalus\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Latin squalus 'a large sea fish, dogfish/shark' (Pliny; Linnaeus later took it for the shark genus Squalus) is the \"\n    \"Italic member of the family as drawn: Pokorny 958 opens the material with 'Lat. squalus \\\"ein größerer Meerfisch\\\"', \"\n    \"Watkins '2. Latin squalus, a sea fish: SQUALENE', Klein s.v. Squalus 'L., \\\"a large kind of sea fish\\\", cogn. with ON. \"\n    \"hvalr, OE. hwæl, \\\"whale\\\"'. The verdict is 'plausible' rather than 'confirmed' because the reservations are old and \"\n    \"still current: Pokorny in the same sentence warns 'das s- könnte aber erst sekundär von squatus \\\"ds.\\\", squāma \"\n    \"\\\"Schuppe\\\" bezogen sein'; Ernout–Meillet observe that the squalus some editors read at Ovid, Hal. 133 is really \"\n    \"squatus, and that with a long ā the word could simply mean 'the scaly one' beside squāma, which suits a dogfish's skin; \"\n    \"de Vaan (reported at Wiktionary) takes that line, and Wiktionary heads the Latin etymology 'Uncertain. Perhaps from \"\n    \"Proto-Indo-European *(s)kʷálos'. The homonym squalus 'foul, filthy' (Klein s.v. squalid, to squāma) is what keeps the \"\n    \"doubt alive.\"),\n  \"derivation_fa\": (\n    \"لاتینی squalus «ماهی بزرگ دریایی، کوسهٔ سگ‌ماهی» عضوِ ایتالیکِ این خانواده است: پوکورنی مادهٔ مقاله را با همین واژه آغاز \"\n    \"می‌کند، واتکینز آن را «Latin squalus, a sea fish» می‌آورد و کلاین می‌نویسد هم‌ریشه با hvalrِ نورس و hwælِ انگلیسی کهن است. \"\n    \"با این همه حکم را «با احتیاط پذیرفتنی» گذاشته‌ایم، زیرا تردیدها پابرجاست: خودِ پوکورنی می‌افزاید که «s-» ممکن است ثانوی و \"\n    \"برگرفته از squatus و squāma «فَلس» باشد؛ ارنو و مِیه یادآور می‌شوند که صورتِ squalus در بیتِ اوید در حقیقت squatus است و \"\n    \"اگر آ کشیده باشد واژه می‌تواند تنها به معنای «فَلس‌دار» و هم‌ریشهٔ squāma باشد؛ دو-وان نیز همین را می‌پسندد و ویکی‌واژه \"\n    \"ریشه را «نامطمئن» می‌خوانَد.\"),\n  \"sources\": [W_SQUALUS],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. (s)kwal-o- (l. 949): '2. Latin squalus, a sea fish: SQUALENE. [Pok. (s)kʷalo- 958.]' — exactly Nourai's root→Latin arrow and the Latin→English arrow of node #7.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. squalus (LAT.txt l. 60182-60191)\", \"stance\": \"partial\",\n     \"note\": \"'squalus, -i m.: squale, chien de mer. Quantité de l'a inconnue; la forme squalus que certains lisent dans Ov., Hal. 133 est en réalité squatus. Si l'ā était long, squālus pourrait … être \\\"l'écailleux, le rugueux\\\", cf. squāma … Mais, pour désigner un \\\"gros poisson\\\", le vieux prussien a kalis \\\"wels\\\", et le vieil islandais hvalr …'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Squalus (KLN_1966.txt l. 36474)\", \"stance\": \"supports\",\n     \"note\": \"'Squalus, n., a genus of fishes of the family of sharks (ichthyol.) — L., \\\"a large kind of sea fish\\\", cogn. with ON. hualr, OE. hwæl, \\\"whale\\\". See whale.'\"},\n    {\"src\": \"POK\", \"where\": \"p. 958 (POK_03.txt l. 2633)\", \"stance\": \"partial\",\n     \"note\": \"'Lat. squalus \\\"ein größerer Meerfisch\\\"; das s- könnte aber erst sekundär von squatus \\\"ds.\\\", squāma \\\"Schuppe\\\" bezogen sein' — supports the equation but flags the s-.\"},\n    {\"src\": \"LEW\", \"where\": \"Walde 1910, grep 'squalus' in LEW_1910.txt\", \"stance\": \"silent\",\n     \"note\": \"No hit in the OCR of the local copy (the s- fascicle is not searchable in this scan), so the Lateinisches etymologisches Wörterbuch could not be used here.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 7,\n  \"lang\": \"English\",\n  \"words\": \"squalene\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"squalene (C30H50), the triterpene hydrocarbon of shark-liver oil, is a modern scientific coinage, not an inherited \"\n    \"word: New Latin Squalus, Linnaeus's genus of dogfish sharks (from Latin squalus 'sea fish'), plus the hydrocarbon \"\n    \"suffix -ene, because the substance was isolated from shark liver (Tsujimoto's work on shark-liver oil, from 1906 on). \"\n    \"Wiktionary s.v. squalene: 'From Latin squālus (\\\"shark\\\") + -ene, because it is found in shark liver.' Watkins 1985 \"\n    \"lists SQUALENE as the sole English derivative of the Latin word under (s)kwal-o- (index l. 2281 'SQUALENE (s)kWal-o-'), \"\n    \"which is precisely Nourai's Latin→English arrow. The naming type is the same as Klein's Squalodon 'fossil toothed \"\n    \"whale' and Squalidae; Funk & Wagnalls (1913) already has 'Squali … [< L squalus, shark]' but not squalene, which \"\n    \"post-dates that dictionary.\"),\n  \"derivation_fa\": (\n    \"«squalene» (اسکوالن) هیدروکربنی است که نخست از روغنِ جگرِ کوسه جدا شد و نامش ساختهٔ دانشمندان است نه واژه‌ای موروثی: از \"\n    \"لاتینِ نو Squalus، نامِ سرده‌ای از کوسه‌ها که لینه از لاتینی squalus گرفت، به‌علاوهٔ پسوندِ شیمیاییِ ‎-ene‎. ویکی‌واژه \"\n    \"می‌نویسد: «از لاتینی squālus \\\"کوسه\\\" + ‎-ene‎، زیرا در جگرِ کوسه یافت می‌شود». واتکینز نیز در پیوستِ ریشه‌های هندواروپایی \"\n    \"تنها بازماندهٔ انگلیسیِ واژهٔ لاتینی را همین SQUALENE می‌داند. پس پیکانِ لاتین ← انگلیسیِ نورایی درست است، به‌شرط آنکه \"\n    \"بدانیم واژه‌سازیِ علمیِ سدهٔ بیستم است.\"),\n  \"sources\": [W_SQUALENE],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985: root entry '2. Latin squalus, a sea fish: SQUALENE' (l. 949) and index 'SQUALENE (s)kWal-o-' (l. 2281).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. Squalus, Squalodon, squaloid (KLN_1966.txt l. 36472-36474)\", \"stance\": \"partial\",\n     \"note\": \"Klein has no squalene entry, but documents the Neo-Latin word-family it belongs to: 'Squalodon … a hybrid coined fr. L. squalus, \\\"a large fish\\\", and Gk. odōn'; 'squaloid … resembling a shark'.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.vv. Squali, Squalodon (FSD_vol4.txt l. 19974, 19979)\", \"stance\": \"partial\",\n     \"note\": \"'Squa'li … Ich. A division of selachians, sharks [< L squalus, shark]'; 'Squa'lo-don … [< Squalus + Gr odous, tooth]'. The 1913 dictionary confirms the Neo-Latin base but predates squalene itself.\"},\n    {\"src\": \"AHD\", \"where\": \"current online appendix (ahdictionary.com/word/indoeurop.html)\", \"stance\": \"silent\",\n     \"note\": \"The 5th-edition appendix no longer contains the root: between skrībh- and slēb- there is no (s)kwal-o- entry, and squalene is not derived from an IE root there any more.\"}\n  ]\n})\n\nentry[\"nodes\"] = nodes\n\ndoc = {\n  \"pdf_page\": 458,\n  \"book_page\": 428,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [entry]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-458.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-458.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-458.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 458"
}
```


### [2026-09-14T02:11:49.926Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 7/7
node verdicts: {'plausible': 4, 'disputed': 1, 'confirmed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 3, 'supports': 5}
books consulted: {'supports': 10, 'silent': 6, 'contradicts': 1, 'partial': 8} | by book: {'KLN': 4, 'ISS': 3, 'WLD': 2, 'POK': 2, 'FSD': 2, 'BRT': 1, 'IEC': 1, 'HUB': 1, 'HENNING': 1, 'MON': 1, 'BQT': 1, 'HRN': 1, 'ARY': 1, 'SKT': 1, 'LAT': 1, 'LEW': 1, 'AHD': 1}
```


## [2026-09-14T02:11:56.509Z] TOOL CALL #84: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg458.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/458.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/458.png"
}
```


### [2026-09-14T02:11:56.588Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 43086 Sep 13 22:11 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/458.png
```


## [2026-09-14T02:12:15.056Z] AGENT

Page 458 done. `verify_check.py 458`: **7/7 nodes, 0 PROBLEM lines.**

**Verdicts** — root: 1 confirmed. Nodes: 2 confirmed, 4 plausible, 1 disputed.
(4 redirect entries on the page — Skhed, Skou, Sku, Skŭr, Skwalos — skipped as instructed.)

**Root Skwalo/Kwalo (PIE \*(s)kʷálos "big fish")** — confirmed; Pokorny 958 literally heads it "(s)kʷalo-s oder vielmehr kʷalo-s", which is why Nourai lists five variants. Cross-checked in WP II 541, Watkins 1985, Mann (IEC "qualos 'sea-monster'"), Bailey DKS.

**Flagged items**
- `disputed` — **#3 Persian karv «کرو» "a kind of fish"**: no Persian dictionary records such a word. Dehkhoda s.v. کرو has only 'spider web', 'hollow/decayed tooth', 'small boat', 'bitter lettuce', and the Arabic verb; Moʿin only 'قایق'. The real Persian reflex of Av. kara- is کر/کرماهی (MP kar-māhīg, Bundahišn; Bailey "Zor.P. kar māhīk"). Nourai's form looks like Gharib's Sogdian krw relabelled as New Persian — his own reference (SOD:194) is a Sogdian lemma.
- `plausible` — **#1 Avestan kara-**: the page Nourai cites, POK:958, actually takes the word *out* of IE ("die iran. Wiedergabe eines urmordwin. *kola 'Fisch' … die ganze Sippe also wohl finno-ugr. Herkunft"); WP II 541, Mann and Wiktionary keep it inherited. ref_check POK:958 = partial.
- `plausible` — **#2 Sogdian krw**: attested only as the compound krw kpy (Gharib 4878, p. 194 — page reference correct); bare krw in Gharib is a homonym 'gap' (4875). Also Sogd. krw is a sister of Av. kara-, not a descendant.
- `plausible` — **#5 English whale, walrus**: whale fine; walrus is a 1650s Dutch loan, a folk-etymological metathesis of ON hrossvalr/rosmhvalr 'horse-whale'. Watkins 1985 lists no WALRUS under the root.
- `plausible` — **#6 Latin squalus**: Pokorny's own "das s- könnte … sekundär" caveat, Ernout–Meillet (Ovid's reading is squatus; possible link to squāma), de Vaan/Wiktionary "Uncertain".

**No extraction errors.** The printed page (checked at 200 dpi) matches the JSON exactly, including "hwaliz" (an i-stem, defensible — Kroonen lemmatises \*hwali-) and the Persian script «کَرو». Page image archived at `data/verification/sources/refs/ocr/BOOK/458.png`; 12 web sources fetched via `fetch_source.py` (4 returned 404 and are not cited).
