# Verification process log — verify-page-428


## [2026-09-14T01:21:49.543Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 428 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-428.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-428.json. Write /home/sfmqrb/git/rishe/data/verification/page-428.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 428` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:50.549Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:51.443Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:51.457Z] TOOL RESULT

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


## [2026-09-14T01:21:51.992Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-428.txt"
}
```


### [2026-09-14T01:21:52.011Z] TOOL RESULT

```
1	=== PDF page 428 (book page 398) ===
2	--- entry 0 ---
3	ROOT [Akkadian] Šabatu : to cut, stop working  (refs AKD:67; BQT:1300)
4	#1 (parent #0) [Hebrew] refs=BQT:1300 | šâbat : to stop work
5	  #2 (parent #1) [Persian] refs=MON:2081; BQT:1300 | šanbeh «شنبه» : Saturday, day of rest
6	  #3 (parent #1) [Greek] refs=None | 
7	    #4 (parent #3) [Latin] refs=None | 
8	      #5 (parent #4) [English] refs=KLN:1369; AHD:1139 | sabbatical ; Sabbath
9	#6 (parent #0) [Arabic] refs=BQT:1300 | s.b.t : to cut, day of stopping the work, Saturday
10	  #7 (parent #6) [Persian] refs=MON:1815 | sabt «سَبْت» : Saturday
11	--- entry 1 ---
12	ROOT Sabha -> redirect to Abâ
13	--- entry 2 ---
14	ROOT Sâen -> redirect to Sě 2
15	--- entry 3 ---
16	ROOT Saěna-mereğa -> redirect to Mereğa
17	--- entry 4 ---
18	ROOT Sâi 1 -> redirect to Sě 1
19	--- entry 5 ---
20	ROOT [Indo-European] Sâi 2, Sěi 3, Sî 3; Sneu, Sněu, Snŭ : to bind; cord, band, tendon  (refs POK:977; KLN:1448)
21	#1 (parent #0) [Avestan] refs=POK:977; KLN:1448 | snâvar : band, sinew
22	  #2 (parent #1) [Persian] refs=HRN:291 | snavar «سَنَّور» : cord, band (obsolete)
23	#3 (parent #0) [Germanic] refs=AHD | senawô : tendon
24	  #4 (parent #3) [English] refs=None | sinew
25	#5 (parent #0) [Latin] refs=POK:977 | nervus : sinew
26	  #6 (parent #5) [English] refs=AHD | nerve, nervous
27	#7 (parent #0) [Greek] refs=POK:977 | neuron : sinew
28	  #8 (parent #7) [English] refs=AHD | neuron, neurology
29	
```


## [2026-09-14T01:21:54.984Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-428.json",
 "description": "Read source JSON for page 428"
}
```


### [2026-09-14T01:21:55.027Z] TOOL RESULT

```
{
  "pdf_page": 428,
  "book_page": 398,
  "entries": [
    {
      "root": {
        "name": "Šabatu",
        "lang": "Akkadian",
        "refs": "AKD:67; BQT:1300",
        "gloss": "to cut, stop working"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "BQT:1300",
          "words": [
            {
              "translit": "šâbat",
              "gloss": "to stop work",
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
          "refs": "MON:2081; BQT:1300",
          "words": [
            {
              "translit": "šanbeh",
              "gloss": "Saturday, day of rest",
              "script": "شنبه"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Greek",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:1369; AHD:1139",
          "words": [
            {
              "translit": "sabbatical",
              "gloss": null,
              "script": null
            },
            {
              "translit": "Sabbath",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Arabic",
          "refs": "BQT:1300",
          "words": [
            {
              "translit": "s.b.t",
              "gloss": "to cut, day of stopping the work, Saturday",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:1815",
          "words": [
            {
              "translit": "sabt",
              "gloss": "Saturday",
              "script": "سَبْت"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sabha",
        "redirect": "Abâ"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sâen",
        "redirect": "Sě 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Saěna-mereğa",
        "redirect": "Mereğa"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sâi 1",
        "redirect": "Sě 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sâi 2, Sěi 3, Sî 3; Sneu, Sněu, Snŭ",
        "lang": "Indo-European",
        "refs": "POK:977; KLN:1448",
        "gloss": "to bind; cord, band, tendon"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:977; KLN:1448",
          "words": [
            {
              "translit": "snâvar",
              "gloss": "band, sinew",
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
          "refs": "HRN:291",
          "words": [
            {
              "translit": "snavar",
              "gloss": "cord, band (obsolete)",
              "script": "سَنَّور"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "senawô",
              "gloss": "tendon",
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
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "sinew",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:977",
          "words": [
            {
              "translit": "nervus",
              "gloss": "sinew",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "nerve, nervous",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:977",
          "words": [
            {
              "translit": "neuron",
              "gloss": "sinew",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "neuron, neurology",
              "gloss": null,
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


## [2026-09-14T01:21:55.675Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:21:55.734Z] TOOL RESULT

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


## [2026-09-14T01:22:15.414Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['AKD','BQT','MON','KLN','AHD','POK','HRN','HUB','BRT','WLD','IEC','SYN','SKT','LEW','LAT','FVQ','AFM','PLA','AFA','LKT','ARY','FSD','WEB','TAD','ARB']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-14T01:22:16.622Z] TOOL RESULT

```
== AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by semantic field; Akkadia
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning o
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git
```


## [2026-09-14T01:22:21.718Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"snēu\\|snāvar\\|snauuar\\|nervus\" POK_full.txt | head -40",
 "description": "Grep Pokorny for sneu root"
}
```


### [2026-09-14T01:22:21.814Z] TOOL RESULT

```
79204:gr. vsupov 'sinew', vsupa 'sinew, bowstring '; Latin nervus^s\ne\N, tendon; muscle, Nerv';
```


## [2026-09-14T01:22:22.842Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==215||NR==216' POK_03.txt | head -120",
 "description": "Print Pokorny p977 area"
}
```


### [2026-09-14T01:22:24.098Z] TOOL RESULT

```
 vfj  ,spinnt'  (*avi^isL',  evvr]  ,nebat',  ivvvriTog  ,gut  gesponnen'  erweisen Anl.  sn-),  Fut.  vrjCTio ;  vrjd^ü)  ,spinne',  vfjf,ia  , Gespinst,  Faden'  (=  lat.  nemen)^ vfjffig  ,das  Spinnen'  (:  ahd.  nät  ,Naht'),  vfiTQOv  , Rocken';  vcj^svogj  vwvra Gramm,  wohl  aus  *v7j-önevog,   ^yrjovTa',
lat.  neöf  nere  {*sne-iö)   ,spinnen',   nemen  , Gespinst,   Gewebe',   netus  ds. ;
mir.  smid  , dreht;  bindet,  quält,  müht  sich  ab';  cymr.  nyddu  ,nere',  corn. nethe,  mbret.  nezaff  ds.  {*sn(i){ö);  mir.  snim  m.  ,das  Spinnen,  Drehen;  Kum- mer'; Abtönung  snö-  in  air.  snäth{e)  , Faden',  bret.  neud  ds. ;  (aber  cymr. ysnoden  ,lace,  band',  corn.  snod  ,vitta'  aus  engl,  snood  ,Haarband');  air. snäthat  ,Nadel',  cymr.  nodwydd  ,acus,  acicula',  acorn.  notuid,  mbret.  na- doez  ,Nadel*;
ahd.  näu  ,nähe*  (=  lat.  neö,  gr.  vfj,  ai.  snäyati^  doch  ohne  s-),  nät  jNahV ; got.  neplttj  aisl.  näl,  ahd.  nädala,  ags.  nädl  f.  ,Nadel'  (aisl.  snälda  , Hand- spindel', wohl  umgestellt  aus  *snäd[i]la)]  *snö'  in  agutn.  snöp,  nschwed. snod{d)  , Schnur',  ags.  snöd  f.  , Kopf  binde'  (:  air.  snäthj  lett.  snäte)-^
lett.  snäjuj  snät  ,locker  zusammendrehen,  spinnen',  snäte,  snäne,  snät{e)ne f.  ,leinene  Decke';  s-los;  ndtns  ,leinen,  zwirnen*,  nät{e)ne  =  snät{e)ne]  *m- als  Schwundstufe  zu  *7iei-  (s.  o.  ai.  nlvi-)  in  lit.  nytis  ,Hevelte  oder  Weber- kamm', lett.  nits  ,Teil  des  Webstuhls',  aksl.  "^nith  , Faden,  Strick',  russ. nith  , Faden',  skr.  niti  , Weber trumm'.
WP.  II  694f.,  WH.  II  159 f.,  Trautmann  199,  272,  Vasmer  2,  221.
(s)nehh-ri-f  (s)nöbb-ri-  ,eng,  dünn,  schmal'  (germ.  auch  ,flink*  aus  , mager'); nur  armen,  und  german. Arm.  nurb  ,eng,  schmal,  dünn  u.  dgl.'  (*snöbh-ri-,  =  aisl.  snöfr)]
974  •
aisl.  snößfr  (Gen.  -rs)  ,eng;   schnellS   aschw.   sri^ver  , schmal,   eng«^  j^j  | snöefugr  ,rasch,  flink*,  mit  Abtönung  aisl.  sriefr  , schnell,  flink',  reduktion^. stufig  sngfurligr  , rasch';  s-lose  Nebenformen  aschw.  ri^ver  und  never^  aisl nefr  (neutr.  7wfrt)  ,rasch,  flink*  (dazu  auch  mhd.,  nhd.  alem.  nuofer  ,mmiter frisch,  nüchtern*,  nhd.  bair.  nuober).
WP.  II  698.
sneig-  ,kriechen':  s.  unter  sneg-  ds.
sneig'Ah-  ,schneien,  (sich)  zusammen  ballen',  snig^h-,  snoig]iho-s  , Schnee*.
Präkrit.  sineha-  (=  ai.  sneha-)  , Schnee^;  av.  anae^a-  
, schneien*,  pamir §ugni  ^9nij  , Schnee*,  (*snaiga-)'j  gr.  yicpa  Akk.  ,Schnee*,  hom.  äydwKpo^ ,sehr  beschneit*^  vslq)eL  (ytcpsi)  ,es  schneit',  viq)dg  , Schneeflocke*  (nyertÖ , Schneegestöber*),  lat.  nix,  nivis  jSchnee*,  nivit  ,es  schneit'  (wohl  i);  Nasal- präs, ninguit  (ninxit)  ds.;
ir.  snigid  ,es  tropft,  regnet*,  snige  n.  ,Tropfen,  Fließen*,  snecht(a)e  , Schnee* (zum  ^Formans  vgl.  vicpSTÖg)]  cymr.  nyf  , Schnee',  nyfio  ,schneien';
ahd.  ags.  sniwan  , schneien*  (st.  V.,  Fartiz.  gi-snigan,  vgl.  noch  nhd.  bair, Partiz.  geschniwen ;  sonst  nhd.  schw.  V.),  aisl.  snyr  ,es  schneit'  (Partiz.  snißnn jverschneit') ;  got.  snaiws  , Schnee'  =  ags.  snäw,  ahd.   sneo  (Gen.   snewes)*
lit.  sniegas,  lett.  sniegs  (Vokal  vom  Verb  übernommen)  , Schnee*,  snaXgala ^Schneeflocke',  sniega  ,es  schneit',  Inf.  smgtij  apr.  snaygis  , Schnee',  aksl» sn4g^  , Schnee*.
V^P.  II  695,  WH.  II 169  f.,  Trautmann  272f.,  Vasmer  2,  680,  R.  L.  Turner BSOAS  18,  449 f.;  vgl.  ai.  snihyati  ,wird  feucht,  heftet  sich*,  sneha-  m.  ,Kle- brigkeit,  Öl,  Fett*.
sneit-  jSchneiden*;  snoito-  , Abgeschnittenes*.
Got.  sneipan,  aisl.  snida  , schneiden,  ernten*,  ags.  snldaTi  jSchneiden,  hauen*, as.  snithan,  ahd.  snldan  »schneiden';  aisl.  sneid  ,abgeschnittenes  Stück*, mhd.  sneite  , durch  den  Wald  gelegter  Durchhau*  u.  dgl. ;  ahd.  snit  ,der Schnitt*,  mhd.  snlde  , Schneide*,  Intensiv,  '^snittön  in  mhd.  snitzen  ,schnitzen'j aisl.  sneis  , kleiner  (abgeschnittener)  Zweig',  ags.  snWs,  snas  ,Spieß,  Speiler*, mhd.  sneise  ,Reihe,  Schnur,  worauf  etwas  gereiht  wird*  {^snoid-tä))
klr.  snit  ,Klotz*,  öech.  snU  ,Ast'  (^snoito-s)]  vgl.  vielleicht  mir.  sneid  ,klein, kurz',  falls  aus  air.  *sneith?
WP.  II  695  f.
(suep-),  snöp-,   sn9p-  ,zu   einem   Strick   zusammendrehen,  Bund,   Garbe*. Lat.  (etrusk.?)  napurae  , Strohseile* ;  ahd.  snuaba  ,vitta',  snuobili  ,kleine
975
rette*;  aksl.  snop^  .deaixrj,  fasciculus,  i7tLds(T[.Log,  ligatura^  russ.  snop^  usw.
■  ■  Garbe';
*  wahrscheinlich  Erweiterung  zu  (s)ne-  ^zusammen drehen*.
^P.  II  698,  WH.  II  142,  Trautmann  272,  Vasmer  2,  682.
(s)oe^'f  (s)rzur-  schallnachahmend  ^murren,  knurren  u.  dgl.^
Gr.  evvQsv  *  STQtasv ;  ivvQrjGeig '  d^QrjvrjasL
```


## [2026-09-14T01:22:28.486Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=216 && NR<=218' POK_03.txt | head -100",
 "description": "Print Pokorny leaves 216-218"
}
```


## [2026-09-14T01:22:29.264Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '79180,79230p' POK_full.txt",
 "description": "Print POK_full around nervus"
}
```


### [2026-09-14T01:22:29.547Z] TOOL RESULT

```
, schneien*,  pamir §ugni  ^9nij  , Schnee*,  (*snaiga-)'j  gr.  yicpa  Akk.  ,Schnee*,  hom.  äydwKpo^ ,sehr  beschneit*^  vslq)eL  (ytcpsi)  ,es  schneit',  viq)dg  , Schneeflocke*  (nyertÖ , Schneegestöber*),  lat.  nix,  nivis  jSchnee*,  nivit  ,es  schneit'  (wohl  i);  Nasal- präs, ninguit  (ninxit)  ds.;
ir.  snigid  ,es  tropft,  regnet*,  snige  n.  ,Tropfen,  Fließen*,  snecht(a)e  , Schnee* (zum  ^Formans  vgl.  vicpSTÖg)]  cymr.  nyf  , Schnee',  nyfio  ,schneien';
ahd.  ags.  sniwan  , schneien*  (st.  V.,  Fartiz.  gi-snigan,  vgl.  noch  nhd.  bair, Partiz.  geschniwen ;  sonst  nhd.  schw.  V.),  aisl.  snyr  ,es  schneit'  (Partiz.  snißnn jverschneit') ;  got.  snaiws  , Schnee'  =  ags.  snäw,  ahd.   sneo  (Gen.   snewes)*
lit.  sniegas,  lett.  sniegs  (Vokal  vom  Verb  übernommen)  , Schnee*,  snaXgala ^Schneeflocke',  sniega  ,es  schneit',  Inf.  smgtij  apr.  snaygis  , Schnee',  aksl» sn4g^  , Schnee*.
V^P.  II  695,  WH.  II 169  f.,  Trautmann  272f.,  Vasmer  2,  680,  R.  L.  Turner BSOAS  18,  449 f.;  vgl.  ai.  snihyati  ,wird  feucht,  heftet  sich*,  sneha-  m.  ,Kle- brigkeit,  Öl,  Fett*.
sneit-  jSchneiden*;  snoito-  , Abgeschnittenes*.
Got.  sneipan,  aisl.  snida  , schneiden,  ernten*,  ags.  snldaTi  jSchneiden,  hauen*, as.  snithan,  ahd.  snldan  »schneiden';  aisl.  sneid  ,abgeschnittenes  Stück*, mhd.  sneite  , durch  den  Wald  gelegter  Durchhau*  u.  dgl. ;  ahd.  snit  ,der Schnitt*,  mhd.  snlde  , Schneide*,  Intensiv,  '^snittön  in  mhd.  snitzen  ,schnitzen'j aisl.  sneis  , kleiner  (abgeschnittener)  Zweig',  ags.  snWs,  snas  ,Spieß,  Speiler*, mhd.  sneise  ,Reihe,  Schnur,  worauf  etwas  gereiht  wird*  {^snoid-tä))
klr.  snit  ,Klotz*,  öech.  snU  ,Ast'  (^snoito-s)]  vgl.  vielleicht  mir.  sneid  ,klein, kurz',  falls  aus  air.  *sneith?
WP.  II  695  f.
(suep-),  snöp-,   sn9p-  ,zu   einem   Strick   zusammendrehen,  Bund,   Garbe*. Lat.  (etrusk.?)  napurae  , Strohseile* ;  ahd.  snuaba  ,vitta',  snuobili  ,kleine
975
rette*;  aksl.  snop^  .deaixrj,  fasciculus,  i7tLds(T[.Log,  ligatura^  russ.  snop^  usw.
■  ■  Garbe';
*  wahrscheinlich  Erweiterung  zu  (s)ne-  ^zusammen drehen*.
^P.  II  698,  WH.  II  142,  Trautmann  272,  Vasmer  2,  682.
(s)oe^'f  (s)rzur-  schallnachahmend  ^murren,  knurren  u.  dgl.^
Gr.  evvQsv  *  STQtasv ;  ivvQrjGeig '  d^QrjvrjasL
g ;  övvQi^saL '  ödvqsr  au  Hes. ; Uihd.  snarren  , schnarren^  schwatzen',  snerren  ^schwatzen',  snurren  ,rauschen, sausen",  snurrcere,  srmrrinc  , Spaßmacher,  Narr',  nhd.  schnarren,  schnurren, Schnurre,  engl,  snarl  ^knurren',  mengl.  snorin,  nengl.  snore  ,schnarchen', mengl.  sneren,  nengl.  sneer  ^verächtlich  lachen';  mengl.  nurnen  /hersagen', ßchwed.  dial.  norna,  nyrna  ,zuflüstern',  aisl.  norn  , Schicksalsgöttin',  mhd. ^arreUj  nerren  ,knurren',  ahd.  narro  ,Narr*;
lit.  niürniuj  niurneti  ,brummen,  knurren';  lett.  nura  ,ein  weinerlicher Mensch',  nurdt  ,brummen,  spinnen  wie  eine  Katze^
Auf  -d\  mengl.  snurtin  ,schnarchen^  mhd.  snarz  , Schnarre,  Wachtel- könig'; lett.  nurdet  , murren,  brummen,  knurren'.
Auf  -g:  norw.  schwed.  snerka  ,prusten,  schnarchen',  schwed.  snurka ,rÖcheln',  mnd.  snorken,  snarken  , schnarchen,  schnauben',  mhd.  snarchen ds.,  nhd.  schnarchen'^  norw.  nurka  ,knarren,  knurren',  ndl.  nurken  ,brum- men,  nörgeln';  lit.  snarglys  , Nasenschleim',  lett.  snurgalas  ds.  (,*rasselnd, röchelnd');  snirguot  , schluchzen;  fauchen  wie  die  Gänse';  lett.  nir^guoties jhöhnisch  lachen',  nui^gt  ,die  Zähne  zeigen';  auch  wohl  lit.  narglyti  ,etwas langsam  tun'  (Bed.  ähnlich  wie  in  Schweiz,  norggen  ,ohne  Erfolg  arbeiten').
Auf  -k:  aisl.  sngrgla  (*snargulön)  , röcheln',  nhd.  nörgeln,  nergeln  ,un- deutlich  sprechen,  mit  verdrießlichem  näselnden  Tone  tadeln';  lit.  niurksaü, -öti  , düster  oder  brütend  dasitzen',  lett.  üurk'et,  nufkstet,  nurkset  ,brummen, murren,  knurren',  n^rka  ,ein  weinerlicher  Mensch',  nafkäet , weinerlich  sein, knarren',  nirkstet  ,knirschen,  ein  Geräusch  machen,  als  ob  etwas  bricht*, mirkt  ,knirschen'.
Auf  -p:  aisl.  snarfla  ,röcheln*,  norw.  schwed.  snarva  ,knurren,  die  Zähne fletschen'. WP.  II  698  f.
3.  {s)ner-  , drehen,  winden  (auch  von  Fäden  und  Flechtwerk),  zusammen- drehen,  zusammenschnüren;    sich   zusammenwinden,    einschrumpfen'; vielleicht  Erweiterung  zu  sne-  ds. Ai.  nytyati  ,tanzt',  nfti-  f.  ,Tanz,  Spiel',  nrtü-  , tanzend',  narma-  n.,  narmd- m. , Scherz',  naristä  f.  ds.,  usw.;  miran.  när-  ,fassen' (Persson  Beitr.  816a  1);
976
gr.  vdgva^'  xißcüTog  Hes.  (und  inschriftlich),  woraus  dissim.  Xagpa^^^ sten,  Kiste,  Gefäß';  durch  Weitergreifen  dieses  dissim.  Wandels  auchSc^^^ (von  der  ^-Erweiterung,  s.  unten),  noch   erhalten  in  vaQxiov  daxög  fl^ zu  XaQ-Kog  ,KorV;
as.  naru,  ags.  nearu,  engl,  narroio  ,eng'  (*nar-wa-  eigentlich  ,zusammi geschnürt*),  aisl.  in  Ngrva-sund  , Gibraltar*  (daneben  Niqrva-sund  uq^ Nehrung  ,schmale  Landzunge*  aus  *ner-wa-),  ahd.  narwa  f.,  narwo  m.  ,Kj (d.  i.  ,zusammengezogene  WundränderQ,  auch  ,an
sa,  fibulatura',  nhd.  2Vai^ dial.    auch   ,Klammer,   Krampen   an   Türen*    wie   norw.   norve   , Klamme' Krampe'  (und  lett.  närs,  näre  , Klammer');  *
nhd.  bair.  der-narren  , starr  werden,  besonders  vor  Frost'  (,*sich  zusammÄ»*' ziehen,  -krampfen'),  narr  , mißratene  verschrumpfte  Frucht*,  narr  (schweii^ ,krampfartige   Spannung',   narrennagel  ,unförmig  ausgewachsener  KagSj^ schwundstufig  (mit  s-)  nhd.  schnurren,  ein- schnurren,  -schnorren  »zusamiuto^v schrumpfen',  isl.  snurda , Knoten  an  einem  Faden,  bildlich  vom  Nasenrümpfea^  ^
dehnstufig  aisl.  näri , Weichen^  (,Einschnürung  des  Leibes'),  mhd.  nSrUdk , knapp,  genau,  jung*  und  mit  Abtönung  aisl.  Nöri  , Zwergname',  nör  n.  ,enrft Bucht,  Sund',  dän.  schwed.  nör  ,Knirps,  ganz  kleines  Kind' ;  '*
wahrscheinlich  ahd.  snuor  , Schnur,  Band,  Seil',  dän.-schwed.  snör^^ got.  snörjö  ,geflochtener  Korb*,  ags.  sner  (*snör{ö)  ,  Saite  einer  Harfe',  aiiL sneri  n.  , gedrehtes  Seil';
lit.  neriüj  nerti  , untertauchen,  einschlüpfen,  einfädeln',  nyrH,  Prät.  ni mrti  ,sich  schlängeln,  ranken',  ismrtij   ,sich  verrenken',   näras  ,Tauchei narys  , Schlinge;  Gelenk,  Glied';  lett.  närs,  näre  ,Klammer*;
russ.  neret,  neretö  ,Art  Fischreuse';
hierher  gehört  3.  ner-,  oben  S.  766.
Erweiterungen :
sner-b-  mit  germ.  p:  norw.   dial.   snerpa   st.  V.   ^einschrumpfen,  sie zusammenziehen',  ahd.  (hi-,  fir-)  snerfan  ,den  Mund  zusammenziehen,  dt Miene  verfinstern*,  bair.  schnurfen  ,sich   einziehen,  schrumpfen'  =  norf3 snurpa  , fälteln,  lose  zusammennähen*,  norw.   snerp  ,Haut  auf  der  Milch*
sner-g-:  ags.  sneorcan  st.  V.  ,einschrumpfen*,  norw.  snerka,  snyrJ^t^ ds.,  snerh{e)  m.  , dünne  Haut  auf  der  Milch*,  aisl.  snerkja  {*snark%aiA ,zusammenziehen,  runzeln'.
{s)ner-k-i  Arm.  nergev  ,tenuis,  gracilis'  (,*zusammengeschnürt  oder  ei geschrumpft*) ;
gr.   vdQT/ir]    ,das   Erstarren,    Krampf,    Lähmung;    Krampf  rochen',   vagtctf' ,erstarren'  (s.  auch  oben  über  vccqxlov,  laQyiog)]   ahd.   sner(a)han  (st.  V.) ,schlingen,  knüpfen,  binden*,  mhd.  snerhen  ,knüpfen,  binden,   zusammea-
1
977
-iehenS  ahd.  snar(a)ha  , Schlinge*,  aisl.  snara  (*snarhö7i)  »schlingen,  knüpfen, ^indenS  snara  f.  ,Schlinge'  (skand.  Lw.  ist  ags.  sneare  f.  , Schlinge^),  snarr rasch,  scharf^  mnd.  snarllken  Adv.  ,schnell,  bald',  ags.  snierian  ,eilen^  aus 0gjiarhian  (,schnelP  aus  ,was  sich  dreht,  schnell  wendet'). WP.  II  699  ff.,  WH.  II  165,  T
```


### [2026-09-14T01:22:29.599Z] TOOL RESULT

```
Root/ lemma: {snep-), snop- snap- 
Meaning: to gather in sheafs, sheaf, bundle 

Material: Latin (etrusk.?) napurae ^StrohseWe'; Old High German snuaba WWa' , snuobili^ 
small chain '; Old Church Slavic snopt 'Ssapn. fasciculus, £ni5£a|J0(;, ligatura', russ. 
snop-b etc. ' fascicle, sheaf '; 

References: WP. II 698, WH. II 142, Trautmann 272, Vasmer2, 682. 
See also: probably extension to (s)ne- 'zusammendrehen'. 
Page(s): 974-975 



Root / lemma: sneu-. 5/7 J- and sneu- 

Meaning: to turn, to bind, attach; band; sinew 

Material: Old Indie snavan- (n.) and snavan- 'band, strap, sinew'; reshuffling eines r/n- 

neuter: a-snavira- 'ohne Sehnen' {snuta- 'from the sinew'), Avestan snavara^s\v\e\N' 

[snauya- 'from an Tiersehne gefertigt'); Armenian nearcf's\ne\i\/, filament. Fiber' ( *sneurt); 

gr. vsupov 'sinew', vsupa 'sinew, bowstring '; Latin nervus^s\ne\N, tendon; muscle, Nerv'; 

alb. /7i/5'Bindfaden, cord' {*snu-tio-)\ 

Old Icelandic snua {snera, snuinn) ' coil, zwirnen, turn ' {*sndwan), snudr. Gen. -arm. ' 
loop, noose, snare ' and ' quickness ', Old English snudvn. 'haste, hurry'. Old Icelandic 
snud/gr^s\c\r\ herumdrehend (of millstone), quick, fast', Gothic sniwan. Old English 
s/7eoM/5/7 'hurry'. Old Icelandic sn0ggr^ o^uick, fast' {*snawwu-), Norwegian snaa 
'hurry'(*s/7ai4/e/7); *s/7e^-/77/c»- 'hurrying' in Gothic sniumjan^\\uny\ sn/umundo^ hasty', Old 
High German sniumiM]. 'rash, hasty, hasty, sly, cunning'. Old English sneome Mv . 
'rash, hasty, immediately ' (besides stands ein unerklartes Old lcelandics/7e/77/775, snimma 
' early, bald'); 

Latvian snaujis 'loop, noose, snare '; Old Church Slavic snovgar\6 snujg, snuti 
'anzettein, ordlrT, Iter, osnyvati, russ. snovatb 'anzettein' and 'quick, fast hin and her go'. 

Tocharian B snaura^Sehueu, Nerven'. 

cognitional with {s)ne- and presumably out of it um originally formant -u- extended. 

References: WP. II 696, WH. II 165, Trautmann 272, Vasmer2, 682. 
Page(s): 977 

Root /lemma: (s)ne-ax\6 (s)nei- 

Meaning: to sew together, to web, spin
```


## [2026-09-14T01:22:43.042Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Sabbath\" KLN_1966.txt | head -20; echo \"=== 1971 ===\"; grep -n \"^sabbath\\|Sabbath,\" KLN_1971.txt | head -20",
 "description": "Grep Klein for Sabbath"
}
```


### [2026-09-14T01:22:43.153Z] TOOL RESULT

```
17086:hallah,  n.,  1)  a  kind  of  cake  used  in  offerings; 2)  priest’s  share  of  the  dough;  3)  twisted  bread used  at  the  Sabbath  meals  (Jewish  religion).  — Heb.  halldh,  ‘cake’,  prob.  meaning  lit.  ‘perforated (cake)’,  fr.  hillil,  Pi‘el  of  hdlul,  ‘he  pierced,  per¬ forated’,  whence  also  halldn,  ‘window’,  haltl, ‘pipe’,  haldl,  ‘pierced;  slain’;  rel.  to  Syr.  haltl, ‘hollow’,  haloid,  ‘a  cave’,  Arab,  khalla,  ‘he  per¬ forated’,  Ethiop.  hallat,  ‘a  (hollow)  reed’, halle),  n.,  psalm  of  praise  especially  applied  1)  to the  group  of  Psalms  113-118,  called  the  Egyptian Hallel;  2)  to  Psalm  1 36,  called  the  Great  Hallel. —  Heb.  hallil,  ‘praise,  song  of  praise*,  prop.  inf. used  as  a  noun  fr.  hillil,  ‘he  praised’,  whence  the nouns  hillil,  mahaldl,  tfhilldh,  ‘praise’;  rel.  to Aram.-Syr.  hallel,  ‘he  praised’,  Arab,  hdlla,  ‘he shouted’,  hallala,  ahdlla,  ‘he  praised  (in  wor¬ ship)’,  Aram,  hilluld,  ‘marriage  song’,  Akkad. alalu,  ‘to  shout  for  joy’.  All  these  words  are  of imitative  origin,  with  the  primary  sense  ‘to  trill’. Cp.  next  word.  Cp.  also  Hillel,  Tehillim. hallelujah,  halleluia,  interj.  and  n.  —  Heb.  haldlii- ydh,  ‘praise  ye  the  Lord’,  compounded  ot hall f Id,  pi.  imper.  of  hillil,  ‘he  praised’,  and  the shortened  form  of  the  Tetragrammaton.  See prec.  word  and  Elijah  and  cp.  alleluia, halliard,  n.  —  See  halyard, hallmoot,  n.,  the  court  of  the  lord  of  a  manor (English  hist.)  —  ME.  halimot,  lit.  ‘hall  meet¬ ing’,  fr.  hal,  ‘hall’,  and  -imot,  fr.  OE.  gemot, ‘meeting’.  See  hall  and  moot,  ‘meeting’,  and  cp. gemot,  witenagemot.
17181:haphtarah,  also  spelled  haftarah,  n.,  a  portion  ot the  Prophets  read  in  the  synagogue,  immediately after  the  reading  of  the  Torah,  on  Sabbaths, feasts  and  fasts.  —  Mishnaic  Heb.  haphtardh, lit.  ‘conclusion’,  short  for  hapfhardh  WnabhV, ‘conclusion  with  a  prophetfic  portion)’,  verbal noun  of  hiphtir ,  ‘he  concluded’,  also  ‘discarded, dismissed’,  Hiph'il  of  Bibl.  Heb.  pdtar,  ‘he  broke through,  split,  separated,  removed’  (in  Mishnaic Hebrew:  ‘he  discharged,  acquitted;  he  exempt¬ ed’),  rel.  to  Arab,  fatara,  ‘he  cleft,  split;  he created’,  Ethiop.  fatara,  ‘he  created’,  Aram.- Syr.  pftar,  ‘he  departed’,  Akkad,  pataru,  ‘to break  through’,  iptiru,  ‘ransom’, hapless,  adj.  —  Formed  with  suff.  -less  fr.  hap, ‘chance’  (taken  in  the  now  obsol.  sense  ‘good luck’).
24148:Moed,  n.,  the  second  of  the  six  orders  of  the Mishnah,  dealing  with  the  Sabbath,  feasts  and fasts.  —  Heb.  md‘ed,  ‘appointed  time,  appoint¬ ed  season,  feast’,  also  ‘appointed  meeting’, from  yadd,  ‘he  appointed,  assigned,  designated’ (whence  also  ‘edah,  ‘congregation’  lit.  ‘people assembled  by  appointment’),  which  is  rel.  to Aram,  ya'ed,  ‘he  designated’,  Syr.  wa'da,  ‘ap¬ pointment,  agreement’,  wa‘ed,  ‘he  invited’, Arab.  wd‘ada,  ‘he  promised’,  wa'ada,  'he  ap¬ pointed  (a  time  or  place)’, mofette,  n.,  noxious  exhalation  from  the  earth.
24717:Musaph,  also  spelled  Musaf,  n.,  additional  prayer on  the  Sabbath  and  on  festivals,  immediately following  the  morning  prayer  ( =  Sltaharith).  — Mishnaic  Heb.  musaph,  ‘additional  offering,  ad¬ ditional  prayer’,  prop,  subst.  use  of  the  Hoph'al part,  of  yasaph,  ‘he  added,  increased’,  which  is rel.  to  Aram,  ostph,  Syr.  auseph,  ‘he  added’,  and prob.  also  to  Akkad.  u$supu,  ‘to  add’,  fiptu, ‘interest’.
27342:parasceve,  n.,  the  day  before  the  Jewish  Sabbath. —  F.  parasceve,  fr.  Late  L.  parasceve,  fr.  Gk. Ttxpxoxs’jr;,  short  for  7;|iepa  TtapacrxEur;;,  ‘day of  preparation’  (scil.  for  the  Sabbath),  fr.  -apa (see  para-,  ‘beside’)  and  crxeur),  ‘equipment’, which  is  rel.  to  oxEuop,  ‘implement,  tool,  vessel". See  diaskeuasis.
27763:paysage,  n.,  landscape.  —  F.,  fr.  pays,  ‘country’, fr.  OF.  pais,  of  s.m.,  fr.  L.  pdgus,  ‘province,  dis¬ trict’.  See  pagan  and  -age  and  cp.  peasant, payyetan,  also  spelled  payetan,  n.,  an  author  of religious  poems  forming  part  of  the  Jewish  lit¬ urgy  on  festivals  and  special  Sabbaths.  — Talm.  Heb.  payyetan,  ‘poet’,  in  MedHeb.  ‘writ¬ er  of  liturgic  poems’,  a  hybrid  coined  fr.  Gk. noirjTfjq,  ‘poet’  (see  poet),  and  the  Heb.  suff. -an.  Cp.  piyyut.
28974:pixie,  n.  —  A  var.  of  pyxie. pixy,  pixie,  n.,  fairy,  elf.  —  Fr.  earlier  pisky, which  is  rel.  to  Swed.  pysk,  ‘a  little  fairy';  of uncertain  origin, pixy,  n.  —  A  var.  of  pyxie. piyyut,also  spelled  piyut,n., a  religious  poem  added to  the  liturgy  of  the  Jewish  festivals  and  spe¬ cial  Sabbaths.  —  Talmudic  Heb.  piyyut,  ‘poem, hymn’,  in  Medieval  Heb.  Titurgic  poem,  liturgic poetry’,  verbal  noun  of piyyet,  ‘he  wrote  poetry’, in  Medieval  Heb.  ‘he  wrote  liturgic  poetry’, which  is  prob.  a  back  formation  fr.  payyetan, ‘poet’.  See  payyetan.
33416:Sabbatarian,  adj.,  1)  pertaining  to  the  Sabbath; 2)  pertaining  to  the  Sabbatarians  or  their  doc¬ trine;  n.,  one  who  keeps  the  seventh  day  of  the week  as  holy.  —  Formed  with  suff.  -an  fr.  L. sabbatarius,  fr.  sabbatum,  ‘the  seventh  day  of the  Jewish  week’.  See  next  word  and  -arian. Derivative:  Sabbatarian-ism,  n.
33417:Sabbath,  n.  —  L.  sabbatum  (partly  through  the medium  of  F.  sabbat)  (whence  also  It.  sabato, OProven?.,  Catal.  dis-sapte,  Sp.,  Port,  sdbado, Serbo-Croatian  subota,  Czech  and  Slovak  sobo- ta,  Russ,  subbota,  etc.),  fr.  Gk.  oa|3(3aTov,  fr. Heb.  shabbath,  ‘Sabbath’  (whence  also  Aram. shabb  td,  Arab,  sabt,  Ethiop.  sanbat),  prop,  ‘day of  rest’,  fr.  shabbath,  ‘he  rested’,  which  is  rel. to  Arab,  sabata,  ‘he  cut  off,  interrupted,  ceased, rested’,  and  to  Akkad,  shabdtu,  which  prob. means  ‘to  cease,  be  completed’.  Cp.  Gk.  *aap.(3a- tov,  a  vulgar  var.  of  aippaxov,  whence  VL. sambatum  (whence  Ru.  simbdtd,  OSlav.  sqbota. Hung,  szombat,  ‘Saturday,  Sabbath’)  and  sam- batl  dies,  ‘the  day  of  Sabbath’  [whence  OF.
33419:Sabbathia,  n.,  a  genus  of  plants  of  the  gentian family  ( hot .)  —  ModL.,  named  after  the  Italian botanist  L.  Sabbati.  For  the  ending  see  suff.  -ia. Sabbatic,  Sabbatical,  adj.  —  L.  sabbaticus,  fr.  Gk. aappaxixoc,  ‘pertaining  to  the  Sabbath’,  fr. oappxTov.  See  Sabbath  and  -ic,  resp.  also  -al. Derivative:  Sabbatical-ly,  adv.
33420:Sabbatize,  tr.  v.,  to  keep  as  a  Jewish  Sabbath.  — Late  L.  sabbatizare,  fr.  Gk.  aappa-ri^Etv,  fr. oappaxov.  See  Sabbath  and  -ize. saber,  sabre,  n.,  a  one-edged  sword.  —  F.  sabre, fr.  G.  Sabel,  later  Sabel,  fr.  Pol.  szabla,  ult.  fr. Hung,  szablya,  ‘saber’,  lit.  ‘a  tool  to  cut  with’, fr.  szabni,  ‘to  cut’.  Cp.  sabreur  and  the  first  ele¬ ment  in  sabretache.
=== 1971 ===
131162:sabbath or a festival, by saying the benediction 
131164:sabbath, resp. the festival (Jewish ritual). — 
153315:Mishnah, dealing with the Sabbath, feasts and 
210470:Sabbath, n. — L. sabbatum (partly through the
```


## [2026-09-14T01:22:44.137Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sinew\" KLN_1966.txt | head -20; echo \"=== 1971 ===\"; grep -n \"sinew\" KLN_1971.txt | head -20",
 "description": "Grep Klein for sinew"
}
```


### [2026-09-14T01:22:44.211Z] TOOL RESULT

```
9493:OI.  kaksah,  kaksd,  ‘armpit’,  OE.  huh,  ‘heel’,  and with  the  first  element  in  OE.  hoh-sinu,  ‘hock sinew’.  See  hock,  ‘joint  in  the  hind  leg  of  a horse’,  and  cp.  cuisse,  cushion,  Quixotic. Derivative:  cox-al,  adj.
11220:Diadelphia,  n.,  a  class  of  plants  in  the  Linnaean system  ( bot .)  —  ModL.,  prop,  ‘plants,  the stamens  of  which  are  united  into  two  bundles’, lit.  ‘like  two  brothers’,  fr.  di-,  ‘two’,  and  Gk. aSeXcpo;,  ‘brother’.  See  adelpho-  and  -ia. diadelphous,  adj.,  1)  having  filaments  united  by two  bundles;  2)  pertaining  to  the  class  Dia¬ delphia.  —  Formed  fr.  di-,  ‘two’,  Gk.  dSeXcpo;, ‘brother’,  and  suff.  -ous.  See  prec.  word, diadem,  n.,  crown;  fillet.  —  OF.  diademe  (F.  dia- deme),  fr.  L.  diadema,  fr.  Gk.  SidSrjpa,  ‘band, fillet,  royal  headband’,  fr.  SiaSciv,  ‘to  bind on  either  side’,  fr.  Sid  (see  dia-)  and  Seiv,  ‘to bind’,  fr.  I.-E.  base  *de(i)-,  *d1-,  ‘to  bind’, whence  also  OI.  dy-dti,  ‘binds’,  di-man,  'band, bond’.  Alb.  del ,  ‘sinew,  tendon’,  duai,  ‘sheaf’. See  desmo-  and  -ma  and  cp.  anadem.  Cp.  also Aditi,  Aditya.
13151:Derivatives:  energetic-s,  n.  pi.,  energetic-al-ly, adv.,  energet-ic-ist,  n.,  energet-ist-ic,  adj. energumen,  n.,  a  demoniac;  a  fanatic.  —  Late  L. energumenos,  ‘one  possessed  of  the  devil’,  fr. Gk.  IvepyoupLEvo?,  pass.  pres.  part,  of  ivepyEtv, ‘to  act  upon’.  See  energy.  For  the  suff.  see  alum¬ nus  and  cp.  words  there  referred  to. energy,  n.  —  Late  L.  energia,  fr.  Gk.  tvt pysia, ‘energy,  efficiency’,  which  was  formed  by  Aris¬ totle  fr.  ivepyf]?,  later  form  of  £vEpy6q,  ‘at work,  active’,  fr.  tv  (see  2nd  en-)  and  £pyov, ‘work’.  See  ergon  and  cp.  allergy,  anergy. Derivatives:  energ-ic,  adj.  (rare),  energ-ize,  tr. and  intr.  v.,  energ-iz-er,  n. enervate,  tr.  v.  —  L.  enervdtus,  pp.  of  enervdre, ‘to  enervate,  weaken’,  fr.  e-  and  nervus,  ‘nerve, sinew’.  See  nerve  and  verbal  suff.  -ate. enervate,  adj.  —  L.  enervdtus,  pp.  of  enervdre.  See enervate,  v.
14710:—  In  some  senses  fr.  F.  file,  ‘row’,  fr.  filer,  ‘to spin’,  fr.  Late  L.  filare,  ‘to  spin’  (whence  also It.  filare,  OProveng.  filar,  Sp.  hilar,  ‘to  spin’),  fr. L.  filum,  ‘thread’,  in  some  fr.  E.fil,  ‘thread’  (fr. L.  filum).  L.  filum  stands  for  I.-E.  base  *gwhis- lom  and  is  cogn.  with  Arm.  Jit,  ‘sinew,  string, line’,  Lith.  gysla,  ‘vein,  sinew’,  Lett,  dzisla, ‘vein’,  OPruss.  pette-gislo,  ‘vein  of  the  back’, OSIav.  zifa,  ‘vein’.  L.  funis,  ‘rope,  line,  cord’, is  not  cognate.  Cp.  Filago,  filament,  Filaria, filigree,  ficelle,  enfilade,  profile,  purfle.  Cp.  also hilum,  nihil.
17907:Hobson's  choice,  n.  —  So  called  after  Thomas Hobson  (died  in  1631),  who  had  livery  stables  at Cambridge  and  let  out  horses  to  customers  on the  condition  that  they  had  to  take  the  animal standing  in  the  stable  nearest  to  the  stable  door, hock,  n.,  the  joint  in  the  hind  leg  of  a  horse.  — ME.  hough,  hoch,  fr.  OE.  hoh,  ‘heel’,  rel.  to  the first  element  in  ON.  ha-sin,  OE.  hoh-sinu,  ‘hock sinew’,  OHG.  hahsa,  MHG.  hahse,  G.  Hachse, ‘hock’,  ON.  hzll,  OE.  hsela,  ‘heel’,  and  cogn. with  OI.  kaksah,  kakfd,  Avestic  kasha,  ‘armpit’, L.  coxa,  ‘hip’,  Lith.  k'mka,  kenkle,  ‘knee  joint’, cinksla,  ‘knee  sinew’,  OIr.  coss,  ‘foot’.  Cp.  bough. Cp.  also  heel.  Cp.  also  coxa.  For  the  second element  in  ON.  hd-sin,  OE.  hoh-sinu,  see  sinew. Derivative:  hock,  tr.  v.,  to  hamstring, hock,  n.,  white  Rhenish  wine.  —  Orig.  ‘wine  of Hochheim’,  abbreviation  of  obsol.  hockamore, ‘wine  of  Hochheim’,  fr.  G.  Hochheimer,  fr.
19421:inion,  n.,  the  nape.  —  ModL.,  fr.  Gk.  ivtov, ‘nape’,  a  derivative  of  t<;  (gen.  *tv6<;),  ‘sinew, tendon;  muscle,  fiber’,  which  prob.  stands  for *Ftc,  (gen.  *Fiv6s)  and  derives  fr.  I.-E.  base *wei-,  ‘to  bend,  twist’,  whence  also  Gk.  t-r£a, eixia  (for  *Fenr£a),  ‘willow’.  See  withy  and cp.  ino-  and  the  first  element  in  Inodes  and  in Iphigenia.
19459:ino-,  before  a  vowel  in-,  combining  form  meaning ‘fibrous’.  —  Gk.  tvo-,  tv-,  fr.  tq  (gen.  Mq), ‘sinew,  tendon;  muscle,  fiber’.  See  inion.
19874:Iphigenia,  n.,  the  daughter  of  Agamemnon  and Clytemnestra  ( Greek  mythol.)  —  L.,  fr.  Gk. iI<piy£veia,  lit.  ‘mightily  bom’  (i.e.  a  mighty princess),  compounded  of  191,  instrumental  of tj,  ‘sinew,  tendon;  muscle,  fiber’,  and  y£vo 4, ‘race,  descent’.  For  the  first  element  see  inion, for  the  second  see  genus  and  cp.  words  there referred  to.
25133:need,  tr.  v,,  to  want,  be  in  need  of;  intr.  v.,  to  be necessary.  —  ME.  neden,  needen,  fr.  OE.  neo- dian ,  ‘to  be  necessary’,  fr.  neod.  See  need,  n. needle,  n.  —  ME.  nedle ,  fr.  OE.  nSdl,  rel.  to  OS. nathla,  ON.  nal,  Swed.  nal,  Dan.  naal,  OFris. nedle,  OHG.  nadala,  nbdla,  MHG.  nadele,  na- del,  G.  Nadel ,  Goth,  nepla ,  and,  with  metathe¬ sis,  OFris.  nelde,  MLG.  nalde,  MDu.  nallde,  Du. naald,  ‘needle’  (Finn,  neula  and  nallo,  ‘needle’, are  Teut.  loan  words),  lit.  ‘a  tool  for  sewing’, formed  with  I.-E.  instrumental  suff.  *-tld  fr. l.-E.  base  *(s)ne-,  ‘to  spin,  to  sew  with  a  needle’, whence  MLG.  neien,  MDu.  naeyen,  Du.  naaien, OHG.  najan,  MHG.  mejen,  G.  nahen,  ‘to  sew’, OI.  snayati,  ‘wraps  up’,  snayuh,  ‘sinew’,  Gk. vsoj,  veiv,  ‘to  spin’,  v5jp.x,  ‘that  which  is  spun, thread’,  v7)-rpov,  ‘distaff’,  L.  ned,  nere,  ‘to  spin’, OSlav.  niti,  nista,  ‘thread’,  snujq,  snovati,  ‘to twist',  Lett,  sndte,  ‘a  linen  cover’,  OIr.  snathe , ‘thread’,  sndthat ,  ‘needle’,  W.  nyddu,  Co.  nethe, ‘to  sew",  OW.,  OBret.  notuid,  W.  nodwydd, ‘needle’.  Cp.  -nema,  nemato-,  nerve.  Cp.  also snood.
25279:nerve,  n.  —  L.  nervus ,  ‘sinew,  tendon;  cord,  bow¬ string;  nerve;  vigor,  force’,  cogn.  with  Gk.  veu- pov  (for  *sneurom)  of  s.m.,  OI.  snavan-,  ‘band, sinew’,  Avestic  sndvar e,  ‘sinew’, Toch.  B  shaura, ‘sinews,  nerves’.  Arm.  neard ,  ‘sinew’,  fr.  I.-E. base  *(s)ne-,  ‘to  spin,  sew  with  a  needle’,  whence also  Gk.  veelv,  L.  nere,  ‘to  spin’,  MDu.  naeyen, OHG.  ndjan,  ‘to  sew’.  See  needle  and  cp.  ncuro-. For  the  relationship  between  Gk.  vsupov  and L.  nervus,  cp.  Gk.  troOpoe,  ‘little,  small’,  and  L. parvus,  of  s.m.,  Gk.  auXoc,  ‘flute,  pipe,  tube’, ooiXtov,  ‘a  hollow  way,  canal,  channel’,  and  L. alvus,  ‘stomach,  womb’.
25282:nervous,  adj.,  1)  pertaining  to  the  nerves;  affect¬ ing  the  nerves;  2)  agitated,  excitable;  3)  strong, vigorous.  —  ME.  neruous,  fr.  L.  nervosus, ‘sinewy,  vigorous’,  fr.  nervus.  See  nerve  and
25321:(med.)  —  Medical  L.,  formed  with  suff.  -itis  fr. Gk.  VEupov,  ‘nerve’.  See  neuro-. neuro-,  before  a  vowel  neur-,  combining  form meaning  ‘pertaining  to  a  nerve  or  nerves’.  —  Fr. Gk.  vEupov,  ‘sinew,  tendon;  cord,  bowstring, nerve;  strength,  vigor",  which  stands  for  *sneu- rom  and  is  cogn.  with  L.  nervus,  of  s.m.  See nerve  and  cp.  words  there  referred  to.  Cp.  also perineurium.
28976:pizzle,  n.,  penis  of  an  animal,  esp.  of  a  bull.  — Cp.  Du.  pees,  ‘sinew,  string,  pizzle’.
35288:sinew
35290:‘which’  (see  quod),  and  non,  ‘not’.  See  non. sinew,  n.  —  ME.  senewe,  sinewe,  fr.  OE.  seonu, sinu,  rel.  to  OS.  sinewa,  ON.  sin,  sina,  Norw.  sin, Swed.  sena,  Dan.  sene,  OFris.  sine,  MDu.  se- nuwe,  senewe,  Du.  zenuw,  OHG.  senawa,  MHG. senewe,  serme,  G.  Sehne,  fr.  I.-E.  base  *sai-, *sei-,  *sl-,  ‘to  bind',  whence  also  OI.  sndvah, ‘sinew’,  Avestic  snavare,  of  s.m.,  Ir.  sin,  ‘chain’, Lett,  pa-sainis,  ‘cord,  string’.  Cp.  seta, sinfonia,  n.,  a  symphony.  —  It.,  fr.  L.  symphonia. See  symphony.
37039:Derivatives:  strike,  n.,  strik-er,  n.,  strik-ing,  adj. and  n.,  strik-ing-ly,  adv.,  strik-ing-ness,  n. string,  n.  —  ME.  streng,  string,  fr.  OE.  streng, ‘string  of  a  bow  or  harp,  cord,  rope,  sinew’,  rel. to  ON.  strengr,  Dan.  streng,  Swed.  Strang,  MDu. strenge,  stringe,  Du.  streng,  OHG.  Strang, MHG.  strange,  stranc,  G.  Strang,  ‘rope,  cord’, and  cogn.  with  L.  stringere,  ‘to  draw  tight’.  See stringent.
37043:can,  ‘to  rub,  move’,  Goth,  striks,  G.  Streich,  ‘a stroke’,  OSlav.  strigQ,  stristi,  ‘to  shear',  OPruss. strigli,  ‘thistle’;  see  strike  and  cp.  stria,  striga, strigil,  strike;  2)  the  other  verb  derives  fr.  earlier *strengere  and  is  cogn.  with  Gk.  axpayi;,  gen. erxpaYY^S,  'a  drop*,  lit.  ‘that  which  is  squeezed out’,  oxpaYYO^r’twisted,  crooked’ ;  flowing  drop by  drop’,  <JTpxyY®M)>  ‘halter’,  <rxpaYY*^stv, axpaYYaXouv,  ‘to  twist,  strangle*,  ctxp oyyv\o$, ‘twisted,  round’,  Mlr.srengim,  ‘I  pull,  draw,  drag’, Ir.  sreangaim,  ‘I  tear,  drag’,  sreang,  ‘string,  rope’, Lett,  string!,  ‘to  become  tight’,  OE.  streng,  ON. strengr,  ‘string  of  a  bow  or  harp,  rope,  sinew’, OE.  strong,  ON.  strangr,  ‘strong,  severe’.  Cp. astringe,  astringent,  constrain,  v.,  constrict,  dis¬ train,  distress,  district,  estrangelo,  obstriction, prestige,  restrain,  restrict,  strain,  v.,  strait, strand,  ‘fiber’,  strangle,  strangulate,  stress,  stret¬ to,  strict,  stricture,  string,  strong,  strongyie.  For the  ending  of  stringent  see  suff.  -ent. Derivatives:  stringent-ly,  adv.,  stringent-ness,  n. strip,  tr.  v.,  to  remove  the  covering  or  clothing  of ; to  tear  off;  intr.  v.,  to  take  off  all  clothing  — ME.  stripen,  strepen,  fr.  OE.  -strppan  in  bestrp-
38532:tend,  intr.  v.,  to  move  in  a  certain  direction.  — ME.  tenden,  fr.  MF.  (  =  F.)  tendre,  ‘to  stretch, hold  out’,  fr.  L.  tendere,  ‘to  stretch,  extend,  di¬ rect  one’s  course,  aim,  strive’,  fr.  I.-E.  *tend-, -//-enlargement  of  base  *ten-,  ‘to  stretch,  ex¬ tend’,  whence  01.  tanoti,  ‘stretches,  extends’, tanah,  ‘thread’,  tdntih,  ‘thread,  string,  cord’, tanuh,  fem.  tanvi,  ‘thin,  tender’,  lit.  ‘stretched out,  extended’,  tannili,  ‘thin,  tender',  tdntram, ‘thread,  loom,  warp;  the  essential;  doctrine, system’,  Gk.  teiveiv,  for  ‘tevieiv,  ‘to  stretch’, Homeric  Gk.  xava&c,  ‘stretched  out,  long’,  Gk. txv'jei v,  ‘to  stretch’,  rfvuv,  ‘sinew,  tendon’, xovo ;,  ‘rope,  cord,  brace’  (lit.  ‘that  which  can be  stretched’),  also  ‘tone,  note’,  raivia,  ‘band, ribbon’,  tx<ji?  (for  *tntis),  ‘stretching,  strain¬ ing’,  L.  tenuis,  ‘thin’,  OSlav.  teneto,  tonotu.
38540:tendinous,  adj.,  related  to,  or  resembling,  a  ten¬ don.  —  Formed  with  suff.  -ous  fr.  ML.  tendo, gen.  tendinis,  ‘sinew,  tendon’.  See  next  word, tendon,  n.,  sinew  ( anat .)  —  ML.  tendo,  gen.  ten¬ dinis,  formed  fr.  L.  tendo,  tendere,  ‘to  stretch, extend’,  on  analogy  of  Gk.  tevcov,  ‘sinew,  ten¬ don’,  which  derives  from  the  stem  of  teiveiv (for  *T£vtetv),  ‘to  stretch’.  See  tend,  ‘to  move  in a  certain  direction’.  The  anatomical  term  tendo Achillis  (‘Achilles’  tendon’)  was  first  used  by  the German  surgeon  Heister.  The  original  name was  chorda  Achillis  (‘Achilles’  sinew’)  and  was coined  by  the  Dutch  anatomist  Philip  Verheyen in  1693,  when  he  dissected  his  own  amputated leg.  He  so  called  it  with  reference  to  the  myth  of Achilles  w  hose  heel  was  the  only  vunerable  spot of  his  body.  Cp.  teno-,  tenonto-. tendril,  n.,  slender,  spirally  coiling  organ  of  climb¬ ing  plants.  —  Shortened  fr.  F.  tendrillon,  di- min.  of  tendron,  ‘a  tender  shoot’,  fr.  tendre, ‘soft,  delicate,  tender’.  See  tender,  ‘soft’. Derivative:  tendrill-ar,  adj. tenebrae,  n.  pi.,  the  matins  and  lauds  for  the  last three  days  of  the  Holy  Week  ( Roman  Catholic Religion).  —  L.,  ‘darkness’.  See  next  word, tenebrous,  adj.,  dark.  —  ME.,  fr.  OF.  tenebrus  (F. tenebreux),  fr.  L.  tenebrosus,  ‘dark’,  fr.  tenebrae, ‘darkness’,  which  stands  for  *temebrae,  fr. *temesrae,  and  is  rel.  to  L.  temere,  ‘rashly,  at random’,  prop,  ‘in  the  dark’.  See  temerity  and cp.  words  there  referred  to.
38550:teno-,  before  a  vowel  ten-,  combining  form  de¬ noting  the  tendon  (anat.)  —  Gk.  tevo-,  tsv-,  fr. t£vcov,  ‘sinew,  tendon’;  see  tendon  and  cp. tenonto-.
=== 1971 ===
58737:sinew’. See hock, ‘joint in the hind leg of a 
70146:bond’, Alb. del, ‘sinew, tendon’, dual, ‘sheaf’. 
82356:sinew’. See nerve and verbal suff. -ate. 
92798:lom and is cogn. with Arm. fil, ‘sinew, string, 
92799:line’, Lith. gysla, ‘vein, sinew’, Lett, dzisla, 
114544:sinew’, OHG. hahsa , MHG. hahse , G. Hachse, 
114548:cinksla , ‘knee sinew’, Olr. coss, ‘foot’. Cp. hough. 
114550:element in ON. ha-sin, OE. hoh-sinu, see sinew. 
123916:‘nape’, a derivative oft? (gen. ‘sinew, 
124141:‘sinew, tendon; muscle, fiber’. See inion. 
126604:tc, ‘sinew, tendon; muscle, fiber’, and y^og, 
159815:OI. snayati, ‘wraps up’, snayuh, ‘sinew’, Gk. 
160612:nerve, n. — L. nervus, ‘sinew, tendon; cord, bow- 
160615:sinew’, Avestic sndvar s , ‘sinew’, Toch. B $naura , 
160616:‘sinews, nerves’, Arm. neard, ‘sinew’, fr. I.-E. 
160638:‘sinewy, vigorous’, fr. nervus. See nerve and 
160897:Gk. veupov, ‘sinew, tendon; cord, bowstring, 
183564:Cp. Du. pees, ‘sinew, string, pizzle’. 
222484:sinew, n. — ME. senewe , sinewe, fr. OE. seonu , 
222485:sinu, rel. to OS. sinewa , ON. sin, sina , Norw. sin,
```


## [2026-09-14T01:22:57.704Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sinew\\|snēu\\|sneu-\\|nervus\\|neuron\" AHD_watkins1985.txt | head -40",
 "description": "Grep Watkins AHD for sinew/sneu"
}
```


### [2026-09-14T01:22:57.755Z] TOOL RESULT

```
968:(s)neeu-. Tendon, sinew. Extension of (s)né-. Suffixed form *(s)neow-r-, further suffixed in: a. *neu-r-o- in Greek neuron, sinew: NEURO-, NEURON; APONEUROSIS;
970:b. metathesized form *nerwo- in Latin nervus, sinew: NERVE; ENERVATE. [Pok. snéu- 977.]
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
```


## [2026-09-14T01:22:59.089Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sēi-\\|sei-.*binden\\|pa-sainis\\|Sehne\" POK_full.txt | head -30",
 "description": "Grep Pokorny for sei- bind"
}
```


### [2026-09-14T01:22:59.162Z] TOOL RESULT

```
79200:neuter: a-snavira- 'ohne Sehnen' {snuta- 'from the sinew'), Avestan snavara^s\v\e\N'
```


## [2026-09-14T01:23:05.942Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"SINEW\" AHD_watkins1985.txt | head -10; echo ---; grep -n \"^sé[i-]\\|sei-. *To bind\\|To bind\" AHD_watkins1985.txt | head -20",
 "description": "Find AHD sinew and bind roots"
}
```


### [2026-09-14T01:23:06.019Z] TOOL RESULT

```
909:sé-4, To bind, tie. Contracted from *sea-. Variant *sesi-, zero-grade form *si-. Suffixed form *si-nw- in Germanic *sinwo- in Old English sinu, seonu, tendon: SINEW. [Pok. 3. sé(i)- 891.]
2260:SINCE s6@-2 SINCERE ker-3 SINCIPUT kaput SINECURE cura, sen-2 SINEW sé-4
---
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to ride (> ridder, rider, knight): RITTER. 2. Celtic *vo-réd- in Latin verédus, post horse (*vo-, under; see upo): PALFREY. II. O-grade form *roidh-. 1. Germanic *raid- in: a. Old English rdd, a riding, road: RAID, ROAD; b. possibly Middle High German reidel, rod between upright stakes (< “wooden horse”): RADDLE!. 2. Prob- ably Germanic *raid-ja- in Old English réde, geréde, ready (< “prepared for a journey’): READY. 3. Germanic *raidjan in Vulgar Latin *arrédare, to arrange: ARRAY. [Pok. reidh- 861.] reig-'. To bind. 1. Germanic *rigg- (the -gg- is anoma- lous) in Norwegian rigga, to bind, akin to the Scandina- vian source of Middle English riggen, to rig: RIG. 2. Zero-grade form *rig- in Latin corrigia (probably borrowed from Gaulish), thong, shoelace (cor-, from com-, together; see kom): SCOURGE. [Pok. reig- 861.] reig-2. To reach, stretch out. 1. O-grade form “roig- in Germanic *raikjan in Old English récan, to stretch out, reach: REACH. 2. Possibly suffixed (stative) zero-grade form “rig-é- in Latin rigére, to be stiff (? < “be stretched out”): RIGID, RIGOR. [Pok. (reig-) 862.] rendh-. To tear up. 1. Germanic *randjan in Old English rendan, to tear: REND. 2. Germanic *rind- in Old English rinde), rind (< “thing torn off”): RIND. [Pok. rendh- 865.] rep-. To snatch. Suffixed zero-grade form *rap-yo- in Latin rapere, to seize: RAPACIOUS, RAPE!, RAPID, RAPT, RAVEN?, RAVIN, RAVISH; EREPSIN, SURREPTITIOUS. [Pok. rep- 865.] rép-'. To creep, slink. Latin répere, to creep: REPENT?, REPTILE; SUBREPTION. [Pok. 1. rép- 865.] rép-2, Stake, beam. Suffixed variant form *rap-tro- in Germanic *raf-tra- in: a. Old English refter, rafter: RAFTER; b. Old Norse raptr, beam: RAFT!. [Pok. 2. rép- 866.] ret-. To run, roll. 1. Prefixed form *to-vo-ret-, “a running up to” (to-, to; vo, under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1. Extended form *reud- in Germanic *rauton in Old Norse rauta, to roar (akin to the Scandi- navian source of ROTE?): ROUT’. 2. Suffixed extended form *reum-os- in Latin riimor, rumor, “common talk”: RUMOR. 3. Extended form *reug- in Latin rigire, to roar: RIOT, RUT’. 4. Variant *rau-ko- in Latin raucus, hoarse: RAUCOUS. [Pok. 1. reu- 867.]
909:sé-4, To bind, tie. Contracted from *sea-. Variant *sesi-, zero-grade form *si-. Suffixed form *si-nw- in Germanic *sinwo- in Old English sinu, seonu, tendon: SINEW. [Pok. 3. sé(i)- 891.]
1059:syi-. To bind, sew. I. Basic form *syi- in Germanic
```


## [2026-09-14T01:23:07.914Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pa-sainis\\|sinu, Sehne\\|ags. seonu\\|seonu\\|sinwō\" POK_full.txt POK_0*.txt | head -20",
 "description": "Grep Pokorny for OE seonu sinew"
}
```


### [2026-09-14T01:23:08.001Z] TOOL RESULT

```
POK_03.txt:1681:Mit  n-Formantien :  av.  hinu-  m.  ,Band;  Fessel',  ags.  slnu^  ahd.  sem aisl.  sin  f.  ,Sehue'  (urgerm.  '^simvä,  Has  nach  dem  Wandel  von  nu  zu aus  sinu-  umgebildet  ist),  mir.  s^n  ,Kette,  Halsband';  lett.  pa-sainis  ,Schni aif-sainis  ,Bündel',  lit.  siena  , Grenze,  Wand',  lett.  siena  ,Wand';
```


## [2026-09-14T01:23:18.606Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=173 && NR<=175' POK_03.txt | grep -n \"sei-\\|binden\\|hinu\\|891\\|892\" | head -20",
 "description": "Find Pokorny 891 sei- root"
}
```


### [2026-09-14T01:23:19.918Z] TOOL RESULT

```
27:nasaliert  {s)krenk-:  vermutlich  russ.  krjdkath  ,eine  andere  Wendung nehmen',  krjac  , Knebelholz',  krjdcith  , festbinden';  ksl.  krucina  (*krqcina) jXoleqa,  epilepsia',   sloven.   u-kroknem,   -niti  ,sich   krümmen',   u-krociti   ds.,
31:norw.  kork  (aisL  ^-Jiqrk  f.)  ^Weidenband',  dial.  auch  »runzeliges  Weib' herkja  , zusammenbinden',  hurkl  , Unebenheit,  Knorren '_,  harkal  ^knornV. russ.  korgd  »verkrüppelter  Baum',  korzdvyj  , verschrumpft,  verkümmert! hart'  (usw.)  ;
```


## [2026-09-14T01:23:20.530Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"snavar\\|snâvar\\|snāvar\\|Sehne\" HRN.txt | head -20; echo \"=== leaf for p291 = 312 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==313' HRN.txt | head -60",
 "description": "Grep Horn for snavar"
}
```


### [2026-09-14T01:23:21.625Z] TOOL RESULT

```
5977:aw. jyd' 'Bogensehne; Sehne* (yt. 10, 70, Geldner,
10994:180. snavar 'Sehne' (nur AW.-Komm. ; auch für aw. t^an^
11002:aw. siiävar- *Seline*; ai. sndvan- 'Band, Sehne'; arm.
11003:neard *Nerv, Sehne' (Hübschmann, No. 217); oss. d.
=== leaf for p291 = 312 ===
291
174. sacltan 'vorübergehen, ablaufen', Praes.saeet '), sazad
(vd. 18 (60), 5 (84)), sac(i)sn.
ap. Sakatä'); aw. [^sac- Vorübergehen, ablaufen'.
175. sartak (d. i. sardak) *Art und Weise*.
ap. t^wrd- 'Art'; aw. sareda- *Art, Gattung; ai.
rdrdha' nur *Schaar .
np. serde {rd statt /, also nicht lautgesetzliche Form)
findet sich nur in den Riväyet's.
176. sar^mr 'Helm'.
aw. säravära- 'Helm*.
177. sästär 'Herrscher, Tyrann* (AW.-Komm., AV.).
aw. sastar-; skr. ^as^tdr- 'Gebieter, Züchtiger; arm.
vergl. säst 'Schelten, Vorwurf, Drohung, Unwille,
Strenge', sastem schelten, drohen, einschärfen', sastik
'heftig (H. No. 246).
178. sej 'Schmerz, Leid', sejömand (Bund., AV.), asefömand,
päz. seS\
aw. id-yejah'.
np. sej ist nur pärsisch. FJ und FR citiren folgenden
Vers von Behräm Zerätuät (Metrum: Hezej):
jfehän-i s^fmend-T pur ^na%
Ja öra pese hased bevefäi
179. snahs, snas 'Schläger; Schlag (AW.-Komm., Säy.-
näsäy.^).
aw. snaid^is-, sna^^a- 'Schläger (zum Schlagen);
Schlag'.
180. snavar 'Sehne' (nur AW.-Komm. ; auch für aw. t^an^
var^)j vielleicht nur Transcription.
Jj Vd. 9 (135) (139) säcät für aw. aacaorUe,
*) Dass »dkatä zur aw. l^sac- gehört, darüber herrsollt Einigkeit,
wenn auch über die grammatische Form selbst die Meinungen aus-
einandergehen (zuletzt Bartholomae, BB. XIV, 243).
^) XVI, 2, wo West snes liest.
19*
```


## [2026-09-14T01:23:33.654Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==314' HRN.txt | head -40",
 "description": "Horn p292"
}
```


### [2026-09-14T01:23:34.980Z] TOOL RESULT

```
--- 292 —
aw. siiävar- *Seline*; ai. sndvan- 'Band, Sehne'; arm.
neard *Nerv, Sehne' (Hübschmann, No. 217); oss. d.
nawr, t. nvar Ader' (No. 195).
181. sfiehr^) 'Schnee (vd. 6 (74) u. ö., Men., AV.).
aw. [/^snaej-, snaeJenti 'es schneit'; ksl. mögü; lit.
sn'egas 'Schnee', stiigti schneien'; gr. vicpei; lat. nix\
nivis ; got. snaiws, ahd. smuit es schneit', nhd. Schnee,
Vergl. Hörn, Indog. Forsch. II, Anzeiger 2.
182. spaxff *verleumderisch', spazgth 'Verleumdung' (Men.,
AV.).'
aw. spazga- (yt. 3, 8, 11, 15), Bedeutung unsicher.
V
np. dpezgi (so FJ, sonst meist sipergt) 'Leid' er-
scheint in folgendem Verse von Henzelebäd (?) 'Isä
(Metrum: A'efTf):
hei sipezgl kesiden^E zt r^tb
ger hude yär-t mihr%än bä men
Die falsche Schreibung mit r (die im FR z. B. aus-
drücklich als richtig bezeichnet wird) beweist aber die
Ungebräuchlichkeit des Wortes.
188. s^hU bezw. spek 'Schössling', nur y. 10 (12).
aw. frajspareya- 'Schössling'.
e für r- Vokal wie in np. bese (oben No. 256), -des
(oben No. 598). k kann für / stehen, wie öfter im
PehlevT.
184. srältan 'schützen', sräy(i)sn, nur im AW.-Komm.
aw. l/"tVr(?-, d-räy^inti 'schützen'; ai. {/'trä-, trdyate
'schützen, behüten'.
185. Hvav *Wort', nur im AW.-Komm.
aw. sravah' 'Wort'; ai. grävas- 'Ruhm'; ksl. sloro
'Wort'.
186. Star 'Stern', häufig (neben stürak).
aw. Star- 'Stern'; ai. stdr-.
Vergl. np. sitare (oben No. 711).
187. Start 'erschreckt'.
aw. stareta-. Von vd. 19 (6) ist das Wort in die
Literatur eingedrungen und wird hier in der gleichen
*J Odor i^nexr unter dem Einfiuss von iji'x J^is ?
```


## [2026-09-14T01:23:35.064Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sn\\(a\\|ā\\|â\\)var\\|snauuar\" BRT.txt | head -20",
 "description": "Grep Bartholomae for snavar"
}
```


### [2026-09-14T01:23:35.227Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:23:46.388Z] TOOL CALL #20: Bash

```json
{
 "command": "ls site/pages/428.jpg 2>/dev/null; pdftoppm -f 428 -l 428 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg428 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg428.png",
 "description": "Render PDF page 428"
}
```


## [2026-09-14T01:23:47.590Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==75 || NR==76' AKD.txt | head -60",
 "description": "Print AKD leaf for page 67"
}
```


### [2026-09-14T01:23:48.261Z] TOOL RESULT

```
site/pages/428.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 61436 Sep 13 21:23 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg428.png
```


### [2026-09-14T01:23:49.298Z] TOOL RESULT

```
ae  dies  usw.,  Jfowtag,  3)  fifiiga  'Aqiws,  Martis dies  usw.,  fi'anz.  marä\,  engl,  thtiesdaj,  deutsch  (dial.)  Äestag,  und  viell. doch  auch  Dienstag,  4)  ?/^/pa  'Egf/ov,  Mercurii  dies  usw.,  franz.  mercreAi, engl.  wednesAaj,  5)  nfxiqa  Ai.ög,  Jovis  dies  usw.,  engl,  thiirsdaj,  Donners- tag, 6)  ijf^^ga  'Aq)QoSlT>]g,  Veneris  dies  usw.,  i^mtag,  7)  i'jfii'^a  Kqövov, Satiirni  dies  usw.,  engl.  saturAaj,  niederdeutsch  safe>-dach,  gehen  durch mehrfache  Übersetzungen,  wenn  auch  nicht  unmittelbar,  so  doch  mittelbar insofern  auf  eine  Benennung  der  Tage  nach  den  babyl.  Göttern  1)  Samas, 2)  Sin,  3)  Nergal,  4)  Nabu,  5)  Mardtik,  6)  Btar,  1)  Kaimänu,  zurück, als  der  7tägigen,  auf  hellenistischem  Boden  entstandenen  Woche  eben  die 7  urspr.  babylonischen  Planetengötter  zugrunde  liegen.
Die  akk.  Monatsnamen  1)  Nisannu,  2)  Ajjaru,  3)  Simänu,  4)  Düzu (urspr.  Tamüzu),  5)  Abu,  6)  Ulülu,  auch  Elidu,  7)  Tasrltu,  8)  Arah-samna,
1)  Eig.;  in  ihr  (unter  dem  Horizont  gelegenes)  Haus  eintreten.
2)  Eig. :  aus  ihrem  (unter  dem  Horizont  gelegenen)  Hause  herausgehen.
      65       —
9)  Kislimu,  10)  Tebetu,  11)  Sabätu,  12)  Addaru  :  >>  späthebr.  u.  arani. 1)  Nlsän,  2)  ^Ijjär,  3)  Smän,  4)  Tammüs,  5)  Ab,  6)  'iM,  7)  mn, 8)  Marhes'Wän,  9)  /sTwZm,  10)  Teftci!,  11)  &&äf,  12)  'Ädär,  die  dann  z.T. auch  ins  Syr.-Arab.  und  neuerdings  auch  ins  Türkische  übergegangen sind.  Dazu  auch  noch  der  aram.  (syr.-arab.  und  tiirk.)  Monatsname  Kämm <C  akk.  Kinünu,  Kamlnu  (s.  schon  oben  S.  32  f.).
Zu  akk.  sabattu  und  nubattu  für  bestimmte  Monatstage  s.  unten  S.  67.
akk.  isten  eins  (wohl  <C  sum.  aS-tan)  :  >  wohl,  trotz  des  ',  spät- hebr. 'aSti  in  "asie  'ämr  elf.  akk.  sinipu,  sinipätu  zwei  Drittel  : >  altaram.  snb  u.  'snb  dass.;  auch  hebr.  pt-sdnajim  viell.  davon  beein- flußt, akk.  hism'^  sechzig  (eig.  ein  Sechstel,  nänil.  der  Vollzahl  360)  : ^  wohl  mand.  Söm  Bez.  für  den  12.  Teil  einer  Stunde.  Deutsch  Schock hat  dagegen  mit  akk.  stiSsu  keinen  etymologischen  Zusammenhang,  während sachlich  die  Kechnung  nach  Sechzigern  allerdings  im  letzten  Grunde  auf das  babylonische  Sexagesimalsysteni  zui'ückgehen  wird.
17.   Religion,  Kultus  und  Mythus.
akk.  palähu  sich  fürchten  vor,   dann  spez.   (die  Götter)   fürchten, verehren,  ihnen  dienen  :  >-  wohl  aram.  pdlah  (Gott)  verehren,  dienen, akk.  amäru  pän  ili  (wörtl.   das  Antlitz   des   Gottes  sehen)  vor  dem  Gotte ersche
inen    :    davon   vieU.   beeinflußt    hebr.    raä   panim  in    Verb,    mit Jahwe.     Vgl.  auch  oben  S.  10  zu  akk.  dagälu  pän.  Zu  pers.-arab.
den,  dm  Keligion  s.  oben  S.  24  unter  akk.  denu.
akk.  Pa.  sullü  anflehen,  (^u  den  Göttern)  beten  :  (in  dieser  Bed.) ^  aram.  Pa.  salll  beten,  sdlötä^  Gebet  O  arab.  sallä  u.  salät,  äth.  sallaja u.  salöt).  akk.  Pa.  sullü  anflehen,  beten  :  dazu  mehrfach  der  1. 1.
sälä  der  hebr.  Pss.  gestellt;  aber  sehr  zweifelhaft.
akk.  loräbu-  segnen,  beten  :  ^  viell.  doch,  ti'otz  anderer  Möglich- keiten, südarab.  krb  segnen,  shrb  weihen,  mkri  (auch  noch  heute  mikräb) Heiligtum,   Tempel  (>  wohl  äth.  mekwräb  Heiligtum).  akk.  aräru
verfluchen  :  >>  viell.  hebr.  \lrar  dass.
akk.  naqu'^  (ein  Trankopfer)  spenden,  allg.  opfern,  dann  spez.  auch
1)  Griech.  als  ahaaoq  wiedergegeben,  wie  entsprechend  die  600,  akk.  neru,  als j-^fo?,  und  die  3600,  akk.  Sar,  als  aä^oq.
2)  Urverwandt  mit  hebr.  herek,  aram.  harrek,  ai'ab.  u.  äth.  häraka.
3)  Damit  urverwandt  hebr.,  aram.,  arab.  nqj  rein  sein.
9
      66  
Schafe  opfern  :  >-  wohl  syr.  nuqqi  opfern,  S}-r.  u.  christl.-pal.  nuqqdjä Libation,  späthebr.  (wohl  <;  aram.)  manaqqit  Opferschale  O  syr.  nwneqJtri), sowie  syr.  neqja  Schaf  (s.  hierzu  bereits  oben  S.  50).  akk.  nakäsu
(den  Kopf)  abhauen,   spez.  (dem  Opfertier)  die  Kehle  durchschneiden  :  > wohl  aram.  ndk<is  schlachten,  opfern,  niJcsata  Schlachtung,  Opfer. akJc.  Pa.  qurruhu  nahebringen,  spez.  v.  Opfer  darbringen  :  davon  wohl beehiflußt  aram.  qarreh,  späthebr.  hiqrib  Opfer  darbringen,  aram.  qurhdna, späthebr.  qorhan  (NT  xogßäi',  xoQßaväi)  Opfergabe.  [akk.  zihii  Opfer,
selten  u.  als  Verbuni  niclit  gebräuchlich;  daher  vieU.  (aber  lautgesetzlich entwickelt)  <<  westsem.  (hebr.  sähnh,  aram.  (hhah ,  arab.  dahaha,  äth. zabha).]  akk.  reScti  das  Erste,  der  beste  Teil  (als  Opfergabe):  davon
viell.  beeinflußt  hebr.  reStt  in  dieser  Bed.
akk.  zaraqu  sprengen  (von  Wasser,  Öl  usw.  im  Kultus)  :  davon viell.  beeinflußt   die  gleiche  kulttechn.  Bed.  von  hebr.  saraq.  akk.
sdlälni  besprengen  (mit  Wasser  usw.)  :  ^  viell.  aram.  zalah  sprengen, und  viell.  darauf  zurückgehend  auch  hebr.  sälah  .(Sünde)  vergeben.
akk.  l:ap<rru  bestreichen  (z.  B.  mit  Erdpech,  laipru  s.  oben  S.  60), abwischen  (z.  B.  Tränen),  kulttechn.  l-uppiini  wischen,  bestreichen  (z.  B. einen  Kranken  mit  einer  Teigmasse),  dann  wohl  auch  in  allgemeinerem Sinne  reinigen  u.  ä.  :  darauf  wahrsch.  zurück
```


## [2026-09-14T01:23:54.833Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==77' AKD.txt | head -60",
 "description": "AKD page 67"
}
```


### [2026-09-14T01:23:55.859Z] TOOL RESULT

```
gehend  hebr.  Upper  als  kult- techn. Bez.  für  sühnen.
akk.  quddusii  glänzend,  rein,  spez.  kiüttech.  qudduSu  reinigen  :  > viell.,  dann  freüicli  früh,  hebr.  qiddas  heiligen,  weihen,  qados  heUig  (auch phön.),  aram.  qaddei  u.  qaddlAa  dass.  O  wohl  südarab.,  arab.,  äth.  qds  in der  loilt.  Bed.).  Vgl.  auch  noch  unten  S.  68  zu  qadiStu  Hierodule  und oben  S.  38  zu  syr.  qddns/i  Ohrring.  akk.  jnt  pi  wörtl.  Mundöffuung,
eine  babyl.  kultische  Reinigungszeremonie  :  davon  abhängig  wohl  mand. peldä  wörtl.  Öffnung,  als  Bez.  einer  lail tischen  Speisung.
Zu  akk.  himänu  eine  kultisch  verwendete  Art  Kuchen,  s.  oben S. 38.
Zu  aldv.  hafa  sündigen,  s.  bereits  oben  S.  11.
akk.  tajjäru  (eig.  zurücldcehrend ,  sich  wieder  zuwendend)  barm- herzig, gnädig  (von  der  Gottheit)  :  davon  viell.  beeinflußt  hebr.  Süh  \ll od.  h  von  Gott,  mand.  (auch  avoIiI  palm.  i)  tajjübä  barmherzig  (aus  aram. ^  arab.  tawwäb).  akk.  paSähu  sich  besänftigen  (von  der  erzürnten
1)  Falls  liier  nicht  doch  tjru,  d.  i.  das  akt.  tajjarti,  zu  lesen  ist.
      67      
Gottheit)  :  >  viell.  (doch  kommen  hier  noch  allerlei  andere  Möglichkeiten in  Betracht)  hebr.  päsah,  O  aram.  pishä  usw.,  LXX  n.  NT  näaxa.  Passah).
akk.  nnbbil.  numhfi  wehklagen  (Pa.  zu  nnhü  rufen,  St.  «&')  :  ^ maud.  numhdjil  Trauer,  namlii  trauern.  akk.  sa^Kldu  klagen,  trauern:
;>  viell.  hebr.  säpad.  jüd.-aram.,  christl.-pal.  sdpad.^
akk.  Saqqn  Sack  (für  Geti-eide,  Mehl  usw.),  und  Büßergewand  : >  wohl  hebr.  sag,  altaram.  PI.  Sqqii,  später  saqqti  O  äth.  Sag).  Aus  dem Semit.  >  giüech.  adxxog,  lat.  Saccus  usw.,  Sacl:
Zu  akk.  nigfdu,  ningfitu  Spiel,  Musik,  sowie  zu  zamftru  singen und  spielen  s.  bereits  oben  S.  29.
akk.  sahattu,  auch  (sekundär)  sapattu  (Etym.  noch  unklar),  15.  Tag  des Monats,  Tollmondstag  :  >  wohl  sicher  hebr.  sahhät  Sabbath  O  aram. iahbdtct,  ^  äth.  sanhat;  ferner  aüßßaror,  saibatitm  usw.  bis  franz.  samedi und  andererseits  Samstag,  sowie  jüd.-deutsch  Schahhes).  Dazu  viell.  auch ägypt.  snit-t^  15.  Tag  des  Monats.  akk.  nuhattti  Abend,  Yor-
abend,  Festvorfeier  :  in  Anlehnung  daran   viell.  neuhebr.  'äreb  Sabbat, jüd.-aram.  'ärribtcij.napaaxtvi'i  (XT),  Rüsttag,  Freitag.
akk.  IcoMapu,  lia-isaptu  Zauberer,  Zauberin,  l;usSupu  zaubern, Impu  Zauber  :  >  wohl  hebr.  liMep  zaubern,  lassap  Zauberer,  malcassepä Zauberin,  l^ampim  Zaubereien.  akk.  fisipu  Beschwörer  {siptti  Be-
```


## [2026-09-14T01:24:15.411Z] TOOL CALL #23: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1300 --image 2>&1 | tail -60",
 "description": "Fetch BQT page 1300"
}
```


### [2026-09-14T01:24:16.936Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1300.png
[transcription from the page image; OCR text in data/verification/sources/refs/ocr/BQT/1300.txt]
[read from the PNG by a vision model, 2026-09-05] BQT vol. 3 PDF page 91 = printed 1300 (entries
شنبد؟ ، شنت ، شنتا ، شنج ، شنجار ، شند ، شندف ، شندله). Rendered only to fix the printed-page offset.
```


## [2026-09-14T01:24:21.112Z] TOOL CALL #24: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ | head -50; echo ---; cat /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1300.vision.txt 2>/dev/null | head -40",
 "description": "Check BQT ocr cache"
}
```


### [2026-09-14T01:24:21.172Z] TOOL RESULT

```
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1074.vision.txt
1092.jpg
1092.vision.txt
1187.png
1187.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1237.png
1237.txt
1237.vision.txt
1261.png
1261.txt
1266.png
1266.txt
1266.vision.txt
1267.png
1267.txt
1267.vision.txt
1272.png
1272.txt
1275.png
1275.txt
1279.png
1279.txt
1280.png
1280.txt
1280.vision.txt
1287.png
1287.txt
1294.png
1294.txt
1294.vision.txt
1296.png
1296.txt
1296.vision.txt
1297.png
1297.txt
---
[read from the PNG by a vision model, 2026-09-05] BQT vol. 3 PDF page 91 = printed 1300 (entries
شنبد؟ ، شنت ، شنتا ، شنج ، شنجار ، شند ، شندف ، شندله). Rendered only to fix the printed-page offset.
```


## [2026-09-14T01:24:25.561Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1299 --image 2>&1 | tail -40",
 "description": "Fetch BQT page 1299"
}
```


### [2026-09-14T01:24:32.313Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1299.png
[transcription from the page image; OCR text in data/verification/sources/refs/ocr/BQT/1299.txt]
[read from the PNG by a vision model, 2026-09-05, verification of dictionary page 198]
BQT vol. 3 (BQT_v3_picofile.pdf) PDF page 90. Printed page number in the header reads "-۱۲۹۹-" (= 1299).
Running head: شنبه. Entries: (continuation of شنان) ، شناو ، شناه ، شنب ، شنبد ، شنبلیت ، شنبلید ،
شنبلیله ، شنبه. So the page immediately preceding it (printed 1298) is the one carrying شنا / شناختن /
شناس — which is the page Nourai cites as BQT:1298, and whose text is in BQT_v3_pages.txt "[pdf page 85]".
```


## [2026-09-14T01:24:35.105Z] TOOL CALL #26: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1299.png"
}
```


### [2026-09-14T01:24:35.131Z] TOOL RESULT

```

```


## [2026-09-14T01:24:46.868Z] TOOL CALL #27: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1300.png"
}
```


### [2026-09-14T01:24:47.617Z] TOOL RESULT

```

```


## [2026-09-14T01:24:47.613Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-14T01:25:16.100Z] TOOL CALL #28: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1300.vision.txt <<'EOF'\n[read from the PNG by a vision model, 2026-09-05] BQT vol. 3 PDF page 91 = printed 1300 (entries\nشنبد؟ ، شنت ، شنتا ، شنج ، شنجار ، شند ، شندف ، شندله). Rendered only to fix the printed-page offset.\n\n[re-read from the PNG by a vision model, 2026-09-13, verification of dictionary page 428 (book 398)]\nPrinted page number in header: -۱۳۰۰-  (running head شنت). Top of right column continues the entry\nشنبد from p.1299: «... که لام روز اول هفته باشد ۱ .»\nMo'in's etymological footnote no. 1 at the foot of printed p. 1300 reads, verbatim:\n\n«۱ = شنبد (ه‍.م.)، شیرازی shambed ، گیلکی shamba  لغتی است سامی . در آرامی sabbath ،\nسریانی shabtâ ، عبری shabbât ، اکدی shabattu . شبانو در نزد اکدیان بروز پانزدهم ماه ــ روزیکه\nدائرهٔ ماه پر شود ــ اطلاق میشد . این کلمه مشتق از افعال ذیل است : عبری shâbat (از کار کنار رفت،\nاستراحت کرد) ، سریانی shbat (استراحت کرد) ، اکدی shabâtu (استراحت کرد، عاطل گذاشت) ،\nعربی سبت (استراحت کرد) و سبت الشیء (قطع کرد آنرا) . و آن از «سب» است بمعنی قطع و استراحت\nمتوقف بر انقطاع از شغل مولد تعب . همین کلمه است که در عربی سبت ، «شنبه» و در فرانسوی samedi\nو در آلمانی Samstag شد .\nH. Zimmern, Akkadische Fremdwörter. Leipzig. 1917. s.67 .\nرک : «شنبه» ، پورداود ج ۲ ص ۷۹ ؛ معجمیات عربیه ــ سامیه ص ۱۷۵ .»\n\n(Footnote 2 on the same page, for شنت: «هز ، shnat ، shnit ، آرامی shanatn ، پهلوی sâl «سال» ،\nدهارله ۲۶۹ ، یونکر ۸۲ ، عربی سنة .»)\nEOF\necho saved",
 "description": "Save BQT 1300 vision transcription"
}
```


### [2026-09-14T01:25:16.211Z] TOOL RESULT

```
saved
```


## [2026-09-14T01:25:17.122Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"== $f\"; grep -n \"شنبه\" $f | head -5; done",
 "description": "Grep Mo'in for shanbeh"
}
```


### [2026-09-14T01:25:20.085Z] TOOL RESULT

```
== MON_part1.txt
8836:کیف در عربی. ادات تشنبه: (بیا.) کلمه‌ای 
10983:از شنبه شروع و به جمعه ختم کردد؛ هفته. 
37897:تشنبه: (ه)درنجده) [ع. تغنبه ] (مص ع.) دو تا 
46265:سه‌شنبه (روز)؛ ج. ثلاثاوات (غم.) 
51795:چهار شنبه س 
== MON_part2.txt
4680:شب چهارشنبه سوری برای اطلاع از آینده 
8697:شنر اغاجی» درخت فلوس» خیار شنبه؛ 
10290:عملی که زنان در شب چهارشنبه سوری 
72497:شنبه. ترکیبات فعلی: به ناف کسی بستن 
80673:چون نوروز به شنبه می‌افتاد» بادشاه می‌فرمود
```


## [2026-09-14T01:25:25.972Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^شنبه\\|شنبه:\\|شنبه (\\|shanbe\\|sanbat\" MON_part1.txt MON_part2.txt | head -20; echo \"=== sabt ===\"; grep -n \"سبت:\\|^سبت\\|سبت (\" MON_part1.txt MON_part2.txt | head -20",
 "description": "Grep Mo'in headwords"
}
```


### [2026-09-14T01:25:26.119Z] TOOL RESULT

```
MON_part2.txt:72497:شنبه. ترکیبات فعلی: به ناف کسی بستن 
MON_part1.txt:8836:کیف در عربی. ادات تشنبه: (بیا.) کلمه‌ای 
MON_part1.txt:37897:تشنبه: (ه)درنجده) [ع. تغنبه ] (مص ع.) دو تا 
MON_part1.txt:46265:سه‌شنبه (روز)؛ ج. ثلاثاوات (غم.) 
MON_part1.txt:71415:شنبه هم بر خلاف اصل استعمال شده. 
MON_part1.txt:85573:شنبه تا جمعه). 
=== sabt ===
MON_part2.txt:6678:سبتر ونلال وجود دارد. این گیاه در طب به 
MON_part2.txt:18443:سبت دادن. سر او تلافی خطای دیگران ر 
MON_part2.txt:28927:سبت هم نباشد و به عبارت دیگر کیف 
MON_part2.txt:45142:مس_سبت: ۱:۸1 [ع.] (مسصل.) شب 
MON_part2.txt:68162:سبت به پاهایش بسیار کوچک است (علت 
MON_part2.txt:71807:بیدا می‌کنند و به مناست سبت: شکا تیصو 
MON_part2.txt:75659:تفاضل مابین اوسط و اصغر باشد. به نسبت: 
MON_part1.txt:22796:سبت ۰۷ قسمت مس و ۲۳ قسمت روی) 
MON_part1.txt:23419:مسبت (متعن 6 چتتر کاراب چنیر 
MON_part1.txt:40680:تسهیم به نسبت: (رض.) تقسیم کردن مبلغ يا 
MON_part1.txt:49118:سبتریکك. اصیل» با ک نژاد. رشیدء صاحب 
MON_part1.txt:53292:حسبت: ا0۵ع۲ [ع. حسیه ] (ا.) مزد؛ اجر. 
MON_part1.txt:53783:سبت به سهمی از اب نات و غیره. 
MON_part1.txt:54917:سبت به امر دیگر محدودتر و کم وسعت‌تر 
MON_part1.txt:63261:سبته آویزان گر دد؛ دنگداله» گلفهشنگ. 
MON_part1.txt:94380:سبت. عالم ملکوت» عالم ملاکه. عالم
```


## [2026-09-14T01:25:28.984Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:25:28.995Z] TOOL RESULT

```


```


## [2026-09-14T01:25:32.466Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%86%D8%A8%D9%87",
 "prompt": "Give the full Persian etymology of شنبه (šanbe) \"Saturday\": intermediate forms (Middle Persian, Aramaic, Syriac, Hebrew, Akkadian), and any cited authorities."
}
```


## [2026-09-14T01:25:33.868Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/sinew",
 "prompt": "Full etymology of \"sinew\": Old English seonu/sinu, Proto-Germanic form, Proto-Indo-European root, and cognates (Avestan, Sanskrit). Quote the reconstruction."
}
```


### [2026-09-14T01:25:38.391Z] TOOL RESULT

```
# Persian Etymology of شنبه (šanbe)

Based on the Wiktionary article, here is the etymological path:

**Modern Persian شنبه** derives from earlier form **شنبذ** (šambiḏ), which came from late Manichaean Middle Persian **𐫢𐫖𐫁𐫅** (šmbd /šambad/), itself from early Manichaean Middle Persian **𐫢𐫖𐫁𐫎** (šmbṯ /šambat/, "Sabbath, Saturday").

The ultimate source is **Hebrew שַׁבָּת** (shabát, "Sabbath"), which may derive from **Akkadian šapattum** (described as "the middle day of the month").

**Related but distinct:** Manichaean Parthian **𐫢𐫖𐫁𐫤** (šmbt /šambat/) shows the same Middle Persian root in another Iranian language.

The article notes this word is "akin to" Aghwan forms, representing Iranian borrowings of the Hebrew term. However, the source does not cite specific Aramaic or Syriac intermediate stages in the etymology chain.
```


### [2026-09-14T01:25:38.646Z] TOOL RESULT

```
# Etymology of "Sinew"

**Old English Origin:** The term derives from Old English *sinu* ("tendon, sinew; nerve").

**Proto-Germanic Form:** It traces back to Proto-Germanic *\*sinwō*.

**Proto-Indo-European Root:** The ultimate source is Proto-Indo-European *\*snéh₁wr̥* ("sinew, tendon"), stemming from *\*(s)neh₁-* meaning "to twist (threads), spin, weave."

**Reconstruction Quote:** The Wiktionary entry states the PIE root as *\*snéh₁wr̥* ("sinew, tendon"), derived from *\*(s)neh₁-*.

**Cognates:** Related words appear across Germanic languages (Dutch *zeen*, German *Sehne*, Swedish *sena*), as well as in Classical Greek *neûron*, Latin *nervus*, and Sanskrit *snāván*.
```


## [2026-09-14T01:25:46.536Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/sinwō",
 "prompt": "Give the reconstruction, meaning, etymology (which PIE root it comes from, and any alternative derivations mentioned, e.g. from *seh₁(i)- 'to bind' vs *sneh₁u-), and descendants."
}
```


## [2026-09-14T01:25:47.632Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sabbath",
 "prompt": "Full etymology of Sabbath: Old English/Latin/Greek/Hebrew chain, the Hebrew verb shabath, Akkadian, and any note on sabbatical."
}
```


### [2026-09-14T01:25:51.480Z] TOOL RESULT

```
# Proto-Germanic *sinwō

**Reconstruction:** *sinwō (feminine ō-stem noun)

**Meaning:** Cord, tendon, sinew, or nerve

**Etymology:** The term derives from an earlier form *senwō, which traces back to Proto-Indo-European *senh₁-weh₂-. This formation relates to the more typical PIE *snḗh₁wr̥ ("sinew, tendon") attested in other Indo-European languages.

**Alternative reconstructions** include *senawō, *senuwō, and *sinawō, reflecting scholarly disagreement about the exact vowel patterns.

**Key descendants:**
- English: sinew
- German: Sehne
- Dutch: zenuw
- Swedish: sena
- Danish: sene
- Icelandic: sin
- Norwegian: sene

The term's widespread presence across Germanic branches confirms its Proto-Germanic origin, with descendant forms showing regular sound changes across West Germanic, North Germanic, and other branches.
```


### [2026-09-14T01:25:52.891Z] TOOL RESULT

```
# Etymology of Sabbath

## Language Chain

The word "Sabbath" traces back through multiple languages:

**Hebrew Origin:** The term derives from Hebrew *shabbath*, meaning "day of rest," which comes from the verb *shabath* meaning "he rested."

**Greek:** Hebrew *shabbath* was transliterated into Greek as *sabbaton*.

**Latin:** The Greek form became Latin *sabbatum*.

**Old English/Middle English:** Latin *sabbatum* entered Old English as *sabat*, then Middle English as *sabat*. The modern spelling with "-th" appeared in the late 14th century but wasn't widespread until the 16th century.

## Original Meaning and Shift

The original meaning preserved the Hebrew concept: "seventh day of the week in the Jewish calendar; Saturday" as "a day of rest from secular employment and of religious observance."

However, among European Christians, the observance shifted from Saturday to Sunday to commemorate Christ's resurrection. This change was "completed among the English people generally during the Reformation," though the etymological connection to the seventh day remains in Romance languages (Spanish *Sabado*, Italian *Sabato*, French *samedi*).
```


## [2026-09-14T01:26:02.920Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%A8%D8%AA",
 "prompt": "Give the Arabic entry سبت: the root س ب ت, the verb سَبَتَ (sabata) meaning, the noun سَبْت (sabt) 'Saturday/Sabbath' and its etymology (borrowed from Aramaic/Syriac/Hebrew?). Also give the Persian entry سبت if present."
}
```


## [2026-09-14T01:26:04.994Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sn%C3%A9h%E2%82%81wr%CC%A5",
 "prompt": "Give the reconstruction *snéh₁wr̥ 'sinew, tendon', its root, and the descendants list (Avestan, Sanskrit, Greek neuron, Latin nervus, Armenian, Tocharian)."
}
```


### [2026-09-14T01:26:08.738Z] TOOL RESULT

```
# سبت (sabt) - Arabic Entry Analysis

Based on the Wiktionary content provided, here's what's documented:

## Root
The word belongs to the Semitic root **س ب ت** (s-b-t).

## Meanings Across Languages

**Hijazi Arabic** has two distinct entries:
1. **Saturday**: "a Saturday" (pronunciation: /sabt/)
2. **Basket**: "usually an immovable plastic basket, mostly a laundry basket" (pronunciation: /sa.bat/)

**Urdu** entry shows:
- **The Sabbath** (pronunciation: /səbt̪/)
- Etymology: "Borrowed from Classical Persian سَبْت (sabt), from Arabic اَلسَّبْت (as-sabt)"

## Etymology Note
The Wiktionary article traces the religious/temporal sense through Persian borrowing from Arabic, but **does not provide information about earlier Aramaic, Syriac, or Hebrew origins** in this entry.

The second Hijazi sense (basket) derives from Ottoman Turkish سبد (sebed/sepet), which came from Persian سبد (sabad, "basket")—a completely different etymological path from the Saturday/Sabbath sense.

**Note**: The specific Persian entry for سبت is not included in the provided content.
```


### [2026-09-14T01:26:09.514Z] TOOL RESULT

```
# Proto-Indo-European *snéh₁wr̥

**Reconstruction:** *snéh₁wr̥ (neuter noun)

**Meaning:** "sinew, tendon"

**Root:** From "(s)neh₁-" meaning "to twist threads, spin, weave" plus the substantifying suffix "-wr̥"

**Key Descendants:**

- **Sanskrit:** स्नावन् (snā́van)
- **Avestan:** 𐬯𐬥𐬁𐬎𐬎𐬀𐬭𐬆 (snāuuarə)
- **Ancient Greek:** νεῦρον (neûron)
- **Latin:** nervus
- **Armenian:** նյարդ (nyard)
- **Tocharian B:** ṣñor

The term demonstrates consistent development across Indo-European language families, with the Greek and Latin forms showing characteristic phonetic shifts from the reconstructed proto-form.
```


## [2026-09-14T01:26:16.603Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ sabt ===\"; grep -n -i \"sabt\\|Sabbath\" FVQ_pages.txt | head -20",
 "description": "Grep Jeffery for sabt"
}
```


### [2026-09-14T01:26:16.669Z] TOOL RESULT

```
=== FVQ sabt ===
5953:CZ- (Sabt).
5955:Sabbath.
5959:Jewish Sabbath. The Muslim authorities treat it as genuine Arabic
```


## [2026-09-14T01:26:17.025Z] TOOL CALL #39: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/428.jpg"
}
```


### [2026-09-14T01:26:17.070Z] TOOL RESULT

```

```


## [2026-09-14T01:26:28.635Z] TOOL CALL #40: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 428 -l 428 -r 600 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg428hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg428hi.png'); print(im.size)\nw,h=im.size\n# persian node snavar approx x 0.55-0.79, y 0.575-0.62 of page\nim.crop((int(0.55*w),int(0.565*h),int(0.80*w),int(0.615*h))).resize((1400,int(1400*(0.05*h)/(0.25*w)))).save('$S/crop428a.png')\nim.crop((int(0.20*w),int(0.485*h),int(0.52*w),int(0.545*h))).save('$S/crop428b.png')\n\"; ls $S",
 "description": "Crop page 428 regions"
}
```


### [2026-09-14T01:26:33.946Z] TOOL RESULT

```
(5100, 6600)
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
404-top.png
411-top.png
412-zoom.png
414-bot.png
afm74-420.png
afm76-421.png
agents.txt
beekes410.txt
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
build-389.py
build-390.py
build-391.py
build393.py
build-394.py
build-395.py
build-396.py
build-398.py
build-400.py
build-401.py
build-405.py
build-406.py
build-407.py
build-412.py
build-414.py
build-415.py
c404-empty.png
c404-greek.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
c412_cedar.png
c412_makrome.png
c412_makrome_zoom.png
c412_meqrameh.png
c412_meq_zoom.png
c412_sedr_zoom2.png
c412_sedr_zoom.png
crop14-394.png
crop18-394.png
crop411_a.png
crop411_b.png
crop411_c.png
crop428a.png
crop428b.png
edit_about.py
edit_research.py
ffprof
pg390b.jpg
pg390b.png
pg390.png
pg391big.png
pg391crop.png
pg391.png
pg391root.png
pg391sog.png
pg392.png
pg393.png
pg394hi.png
pg394.png
pg397.png
pg398.png
pg399-crop1.png
pg399-greek.png
pg399.png
pg399-sog.png
pg400big.png
pg400_fa_heli.png
pg400_fr2.png
pg400_french.png
pg400_kasak2.png
pg400_kasak3.png
pg400_kasak.png
pg400.png
pg402.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
pg409.png
pg410hi.png
pg410-k2.png
pg410-kadm2.png
pg410-kadm.png
pg410-persian.png
pg410.png
pg410-q2.png
pg410-qedam.png
pg411_300.png
pg411.png
pg412_hi.png
pg412.png
pg412_uhi.png
pg413.png
pg414-greek.png
pg414.png
pg415-emptybox.png
pg415hi.png
pg415.png
pg416-v.png
pg417.png
pg418hi.png
pg418.png
pg418-raj2.png
pg418-raj3.png
pg418-rajidan.png
pg424.png
pg428hi.png
pg428.png
pg429-crop1.png
pg429-crop2.png
pg429-crop3.png
pg429hi.png
pg429.png
pg431.png
pg433.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
write409.py
write410.py
```


## [2026-09-14T01:26:36.840Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop428a.png"
}
```


### [2026-09-14T01:26:36.862Z] TOOL RESULT

```

```


## [2026-09-14T01:26:42.968Z] TOOL CALL #42: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg428hi.png'); w,h=im.size\nc=im.crop((int(0.735*w),int(0.568*h),int(0.785*w),int(0.590*h)))\nc=c.resize((c.width*6,c.height*6), Image.LANCZOS)\nc.save('$S/crop428c.png'); print(c.size)\n\"",
 "description": "Zoom Persian script snavar"
}
```


### [2026-09-14T01:26:45.105Z] TOOL RESULT

```
(1530, 876)
```


## [2026-09-14T01:26:47.077Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop428c.png"
}
```


### [2026-09-14T01:26:47.101Z] TOOL RESULT

```

```


## [2026-09-14T01:26:52.329Z] TOOL CALL #44: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg428hi.png'); w,h=im.size\nc=im.crop((int(0.715*w),int(0.556*h),int(0.775*w),int(0.578*h)))\nc=c.resize((c.width*5,c.height*5), Image.LANCZOS)\nc.save('$S/crop428d.png'); print(c.size)\n\"",
 "description": "Re-crop Persian script"
}
```


### [2026-09-14T01:26:54.097Z] TOOL RESULT

```
(1530, 725)
```


## [2026-09-14T01:26:55.786Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop428d.png"
}
```


### [2026-09-14T01:26:55.813Z] TOOL RESULT

```

```


## [2026-09-14T01:27:30.757Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== Horn section heading (leaves 290-300) ===\"; for n in 285 290 295 300; do echo \"--leaf $n--\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' HRN.txt | head -6; done",
 "description": "Find Horn Pahlavi section heading"
}
```


### [2026-09-14T01:27:31.830Z] TOOL RESULT

```
=== Horn section heading (leaves 290-300) ===
--leaf 285--
A, A').
1. a-, a//-, un-, nicht-' (« privativumj. Sehr häulig, z. B.
asnr endlos*, a/^ar(i)sn *das Nichtessen , aguftar 'nicht
sprechend' u. v. m.
ap. a- in Anämaka' Monatsname (?) ; aw. a-, an- ;
ai. a-, an-; arm. aw- (H. No. 20).
--leaf 290--
— 268 —
schon durch die Lesung asta- hinfällig ; aber auch die
Bedeutung ^Gesandter, Bote' kam seinem asta- nicht zu.
Bartholomae's schöne Gleichsetzung von aw. asti-
mit ai. dtithi- (BB. 15, 10) hat, beiläufig bemerkt,
Jackson, Ayesta Grammar § 794 angenommen.
--leaf 295--
— 273 —
(Ivitan bei Spiegel (Glossar) und dnyUan^ dvätan
bei West (AV.) sind auch damistan zu lesen.
67. duzltan Verbrennen, brennen*, dazad *er verbrennt*.
aw. [/^dajlz-^ dazaiti er verbrennt'; ai. [/'dah-^ ddhati;
lit. degüy def/ti ^brennen*.
--leaf 300--
- 278 —
aw. gairi- *Berg'; ai. f]firi' 'Berg': ksl. gora,
kurd. gir ^Hügel', girk; wa/. yar, ya/n. gor^ rösn.
jir, siyn, zir, sar. zer.
Wohl in dem Namen ferjistan *Bergland'.
90. ffars 'Haar (vd. 18 (4) GL, 17 (4)), daneben vars
```


## [2026-09-14T01:27:32.395Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sinwar\\|sanwar\\|snawar\\|snavar\" RCH.txt HJB.txt HUB.txt 2>/dev/null | head -20",
 "description": "Grep Richardson/Hubschmann for snavar"
}
```


### [2026-09-14T01:27:32.457Z] TOOL RESULT

```
HUB.txt:9069:snavare *Sehne' (phi. snavar ist nur Umschreibung des Zend-
```


## [2026-09-14T01:27:39.796Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 282 283 284; do echo \"--leaf $n--\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' HRN.txt | head -20; done",
 "description": "Horn appendix heading"
}
```


### [2026-09-14T01:27:40.940Z] TOOL RESULT

```
--leaf 282--

--leaf 283--
VERLORENES SPRACHGÜT.
--leaf 284--
```


## [2026-09-14T01:27:41.156Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9055,9080p' HUB.txt; echo \"=== which leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /snavare/{print NR}' HUB.txt",
 "description": "Hubschmann context for snavare"
}
```


### [2026-09-14T01:27:42.311Z] TOOL RESULT

```
kambistem; nam *feucht' = ap. *namna' = idg. *nabhna-y
vgl. zd. napta- 'feucht*. Siehe w6 = m § 153.
e) Idg. pn = iran. fn = np. / oder m oder 6 ? im
Auslaut: ^a/ *Hitze' = zd. tafnu-, tafnah-; sdm^) *Nacht-
essen', phi. iflw, zd. xsdfnlm (ace, ys. 62, 7 der Neuaus-
gabe), vgl. zd. xsafni; x^ab^) *Schlaf' = zd. x^afna- (oder
= skr. svapa- *Schlaf *) ? ; tab 'Fieber = zd. tafnu- (oder :f=
skr. tapas *Hitze, Gluth*)? Das Verhaltniss dieser Formen
zu einander ist mir nicht klar. Inl. fn in tafna 'Spinne-
webe' H. 372.
«
f) Idg. sn bleibt anl. im Zd. als sn (vgl. sniz 'schneien
= idg. snig^h), wird aber zu n im Ossetischen, Afghani-
schen und Balu5i, vgl. osset. nawr, nvar *Ader = zd.
snavare *Sehne' (phi. snavar ist nur Umschreibung des Zend-
wortes); nain 'baden*, zd. skr. sna; afgh. n^Or 'Schwieger-
tochter = bal. nasCir = skr. snusd-. So ist vielleicht
anl. sn auch im Persischen zu n geworden. Ueber sinCL,
Osna *Schwimmen* siehe oben p. 81. Inl. sn bleibt im Zend,
vgl. sasna-, im Persischen fehlen sichere Beispiele. Viel-
leicht ist es hier zu sn geworden, vgl. u§nan *Seifenkraut'
== zd. *usnana' aus us + snana- (oben p. 15).
Ueber ns = np. ng siehe § 109, c; iiber gn siehe
§ 143, b.
*) Naoh Bartholomae, Stud. II, 94 = arisoh *bhundhna-,
•j Vgl. § 9, b.— 254 -
=== which leaf ===
264
```


## [2026-09-14T01:28:06.758Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5940,5990p' FVQ_pages.txt; echo \"=== leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /\\(Sabt\\)/{print NR}' FVQ_pages.txt",
 "description": "Read Jeffery on al-Sabt"
}
```


### [2026-09-14T01:28:07.909Z] TOOL RESULT

```
Saba'.
The name of a city in Yemen destroyed by a great inundation.
We have fairly extensive evidence for the name of the city from non-
Arabic sources. It is the hFIA of the S. Arabian inscriptions (CIS, ii,
375; Mordtmann, Sab. Denkm, 18; Glaser, Zwei Inschriften, 68;
.Rossini, (llossarium, 192 ; Ryckmans, Noms propres, i, 353), which
occurs in the Cuneiform inscriptions as Sub* a and Saba\ 2 in Greek us
2a/3ct, 3 in Heb. 3$, from which are Syr. )m, Kth. frflfc.
As the Qur'anic statements about Saba' are connected with the
Solomon legend, it is possible that like, the name Suleiman, it came
to him from Christian sources, though we cannot, absolutely deny its
derivation from Rabbinic material (Horovitz, KU, 115; JPN, 157),
and indeed the name may have come directly from S. Arabia.
CZ- (Sabt).
ii, 61 ; iv, 50, 153 ; vii, 163 ; xvi, 125.
Sabbath.
(Sprcnger and others would add to this OLl.*-, rest in xxv, 49 ;
Ixxviii, 9.) 4
We find ol^ only in relatively late passages and always of the
Jewish Sabbath. The Muslim authorities treat it as genuine Arabic
from CHI* to cut, and explain it as so called because God cut off
1 Hifl examples arc JAJ
2 Delitzsch, Parwlie.% 303.
3 27a/Ja in LXX, but Zd^arav in Strabo.
4 Leben, ii, 430 ; Gninbaum, ZDMG, xxxix, 584, but see Horovitz, K[J, 96.FOREIGN VOCABULARY OF THE QUR'AN 161
His work on the seventh day 1 (cf. Bai(J. on ii, 61 ; and Mas'udi,
Muruj, iii, 423).
There can be no doubt that the word came into Arabic from Aram. 2
and probably from the Jewish NFISt? rather than from the Syr.
)Ao. The verb cH**^" f vu \ 163, is then denominative, as Fraenkel,

Vocab, 21, has noted. It is doubtful if the word occurs in this meaning
earlier than the Qur'an.
(Sabbaha).
Of very frequent occurrence, cf. ii, 28, etc.
To praise.
Besides the verb we have jUtX,*- p raise 3 ;
*c,1H~,4 one who celebrates praise, all obviously later formations from
x- tf>
cr-
The primitive sense of the root is to glide, and in this sense we find
in the Qur'an, so that some of the philologers
- ^
endeavoured to derive *c-l-M from this (cf. Baid. on ii, 28). It has been
C'
pointed out frequently, however, that the sense of praise is an Aram.
development of the root. It occurs in Hebrew in this sense only
as a late Aramaism (BDB, 986), and in S. Semitic only after contact
with Aramaic speaking peoples.
HUB? is found even in O.Aram., 4 meaning to laid, praise, and has
a wide use in Syriac. Fraenkel, Vocab, 20, and Hirschfeld, Beitrdge, 45,
=== leaf ===
178
```


## [2026-09-14T01:28:09.802Z] TOOL CALL #51: Bash

```json
{
 "command": "cp /home/sfmqrb/git/rishe/site/pages/428.jpg /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/428.jpg 2>/dev/null || (mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg428.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/428.png); ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page image for audit"
}
```


### [2026-09-14T01:28:10.799Z] TOOL RESULT

```
92.png
94.png
95.png
96.png
99.png
```


## [2026-09-14T01:28:23.635Z] TOOL CALL #52: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/428.* 2>&1; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA sabbat ===\"; grep -n -i \"Sabbat\\|sabt\" AFA.txt | head -20",
 "description": "Check page copy and grep Fraenkel"
}
```


### [2026-09-14T01:28:23.695Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 57689 Sep 13 21:28 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/428.jpg
=== AFA sabbat ===
3316:denken. Im Talmud Sabbat SGa wird (gewim nieht ohne Grunde angegeben,
```


## [2026-09-14T01:28:25.760Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%D9%86%D8%A8%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for شنبه, including any origin tag in brackets, and the Dehkhoda entry's etymology if present."
}
```


### [2026-09-14T01:28:32.361Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for شنبه

**Quote from Farhang-e Mo'in:**
"(شَ بَ یا بِ ) (اِ. ) روز اول هفته مسلمانان و یهودیان"

This entry identifies شنبه as the first day of the week for Muslims and Jews, with no etymology tag provided in the Mo'in dictionary.

## Dehkhoda Entry Etymology

The Dehkhoda dictionary provides etymological information, tracing شنبه back to Hebrew origin: "از کلمه عبری شَبَّت. سَبْت" (from the Hebrew word Shabbat/Sabt). The entry notes this represents the first day of the weekly cycle, originally derived from Hebrew linguistic roots.
```


## [2026-09-14T01:28:36.854Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%A8%D8%AA/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for سبت — the bracketed origin tag (e.g. [ع.]) and the definition — and the Dehkhoda entry for سبت (Saturday) with its etymology."
}
```


## [2026-09-14T01:28:39.225Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%A9%D7%91%D7%AA",
 "prompt": "Give the Hebrew entry שבת: the verb שָׁבַת (shavat) 'to cease, rest' and the noun שַׁבָּת (shabbat) 'Sabbath', with their etymologies and any mention of Akkadian šapattu."
}
```


### [2026-09-14T01:28:43.182Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for سبت

**Farhang-e Mo'in (Mo'in Dictionary):**

The entry presents two distinct definitions:

1. **(سَ) [ع.] (اِ.)** — "شنبه، نخستین روز هفته" translating to Saturday, the first day of the week.

2. **(سُ بَّ) [ع. سبة]** — "ننگ و عار" meaning disgrace or shame.

---

# Dehkhoda Lughratnama Entry

**Etymology and Historical Context:**

The Dehkhoda dictionary provides extensive etymological information, noting that سبت carries multiple meanings including "استراحت" (rest), "آسایش" (comfort), and "بریدن" (cutting). The entry emphasizes that the term derives from Hebrew usage among Jewish communities.

The entry specifically references Saturday observance: "سبت و سبوت جمع آن است، اسم. آن روزی است که اصحاب یهود از تمامی اعمال خود دست کشیده استراحت میکردند" — indicating it refers to the day when Jewish people ceased work and rested.
```


### [2026-09-14T01:28:43.321Z] TOOL RESULT

```
# Hebrew Entry: שבת (Shabbat)

## Verb: שָׁבַת (shavat)

**Meaning:** "to stop working, to rest"

The verb appears in biblical context: "And on the seventh day God finished His work...and He rested on the seventh day from all His work."

## Noun: שַׁבָּת (shabbat)

**Meanings:**
1. Shabbat/Sabbath—the weekly day of rest
2. Saturday
3. (archaic) week in Mishnaic Hebrew

## Etymology

**Akkadian Connection:** The Hebrew term may derive from Akkadian *šapattum*, described as "the middle day of the lunar month." This represents a possible borrowing from Akkadian into Hebrew, linking the Sabbath concept to lunar calendar terminology in ancient Mesopotamian culture.
```


## [2026-09-14T01:28:49.874Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Sabbath,  n.  —  L.  sabbatum' in p: print('Sabbath leaf',i)\n    if 'sinew,  n.  —  ME.  senewe' in p: print('sinew leaf',i)\nprint('total leaves',len(pages))\n\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['KLN']['page_offset'])\"",
 "description": "Find KLN leaf numbers"
}
```


### [2026-09-14T01:28:51.126Z] TOOL RESULT

```
Sabbath leaf 727
sinew leaf 768
total leaves 903
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-14T01:29:00.399Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (726,727,728,767,768,769):\n    p=pages[i]\n    nums=re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$', p)\n    nums2=re.findall(r'\\b1[34][0-9]{2}\\b', p[:400]+p[-400:])\n    print(i, nums, nums2, repr(p[:80]))\n\"",
 "description": "Find printed page numbers in KLN leaves"
}
```


### [2026-09-14T01:29:01.559Z] TOOL RESULT

```
726 ['1365'] [] 'he cud’,  fr.  ruminatus,  pp.  of  ruminari.  See  prec. word  and  -ion.\nrumin'
727 [] [] ' suff.  -ine. Cp.  rucervine.\nrusk,  n.,  light,  soft  bread  or  biscuit.  —  '
728 [] [] 'i,  F.  samedi,  ‘Saturday’  and — prob. through  the  medium  of  the  Gothic— '
767 ['1444', '1446'] [] 'g  to,  or  con¬ taining,  silica.  —  See  silica  and  -ous. silicic,  adj.,  '
768 ['1448'] [] ' Pure  is  dealt  with  as  an  impostor  and  is  believed only  after  he  has'
769 ['1449', '1450', '1451'] [] ',  pertaining  to Ceylon;  n.,  a  native  of  Ceylon.  —  Formed  with suff.  -'
```


## [2026-09-14T01:29:15.815Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 sneu ===\"; grep -n \"sneu\\|snāuar\\|snävar\\|nervus\" incoming/WLD/WLD_Bd2_pages.txt | head -15",
 "description": "Grep Walde-Pokorny Bd2 for sneu"
}
```


### [2026-09-14T01:29:15.870Z] TOOL RESULT

```
=== WLD Bd2 sneu ===
5032:M^enn in nervus          gegeniiber vbvqov die L'mstellung in einer dreisilb. Gdf.
5033:*sneuero- begrundet ist,         kann auch parvus ein *pau^ro zugrunde liegen,
12313:IP. 3, 59 f. auf Ablautsneubildung zu beruhn, da auch brit. bed e zeigt,
21367:,,nicken (aber nicht ruardfco ,.schlafen, s. sneudQi)- „schlafrign) ; lat. ntio, ^ere,
32155:se{i)d-^ wozu sed- Ablautsneuhildung sein miiBte. Ygl. Osthoff Pf. 414f.,
46020:  Neben snd- liegt snau- \mdsneu-                       (ygl.   das Nebeneinander ^sp€L-p-\
46024:Muttermilch, entlassen“ (Praes. idg, ^snau-ti oder dehnstufiges *sneu-ti); gr,
46048:Ableitung von einem snu-trl (oder *sneu-trt) fem. „Milcli flieBen lassend"
46051:   Als Erweiterung von sneu- faBt man (z. B. Curtius 319, Froehde BB. 21,
46074:                                               s. sneudh- „sclilafrig^‘   nichts       —
46077:*sneudh~ „Neber‘ als „Feuchtigkeit'‘ (s. d.); ob hierher nach Froehde BB. 21,
46108:       „drehen“, vgl. die verwandten Wzln. sneu-^                      meu-^ sner-^ auch neir-
46115:vgl. uber dt. SeTine, arm. anur, air. sanh das unter sneu- bemerkte.
46205:696                                      sneu-, sneu-
46221:sneu- und sneu- etwa „drehen'‘, bes. „Faden zusammendrehen, kniipfen'^;
```


## [2026-09-14T01:29:17.743Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ===\"; grep -n \"snavar\\|snāvar\\|snãvar\\|snavara\\|snävar\" BRT.txt | head -10; echo \"=== BRT col 1631 area? grep Sehne ===\"; grep -n \"Sehne\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-14T01:29:17.821Z] TOOL RESULT

```
=== BRT ===
27146:•  j.  snävar-  'Sehne,  Schnur':  'van F.  12.
27147:KompA.  —  Vgl.  ai.  sn&vaii'  n.  'Sehne,  Schnur', OOS5.  m>ar{%ds.2)  'Ader';  weiteres  bei  Hbm. AGr.  /,  478,  Bgm.  GrCr.3  54.  —  S.  auch siiäiiya;  —  Pü. :  dan  ddr');  vgl.  snävarj.- bäsHta:   —    '>  Mit  den  np.  Glossen  mai  und
27148:•  j.  snävara.bäzu'ra-  Adj.  (fem.  °rä-) 'Schnüre,  Sehnen  als  Arme  habend,  des Arme  von  Schnüren,  Sehnen  gebildet  wer- den', von  der  Schleuder;  fradaxlana  °ra mal  %risqs  fradaxlanyais  V.  14-  9-
=== BRT col 1631 area? grep Sehne ===
4855:.  j.  a-yaozdä-  f.  'Verunreinigung  Ver- . .  -  ayaBhö.Jyä-  Adj.  (mask.  -ya-)  'mit seuchung':  vT^pm  a  ahmat  'i^"  f 'dya\  ^^^^^^  (eisernen)  Sehnen':  vLlzah...
9044:»II.  *ki/'bü'-^''jiyä-  'mit  Sehnen  aus  -?  -';  s.  ■
10632:'Jemandem  (Abi.)  angelegen  sein,  sein Anliegen  (Sehnen,  Hoffen)  bilden':  ahü (sd.,  Sp.  3  o.)  at  paiti  adähü  tnazää  akurä masdqmtä  bSiricä  kar^svä  räitl  tot  xra- paiti  ahmat  hyat  aib[  hyat  mliditn  *mavai- iim  (sd.)  . .  "bei  diesen  Heimzahlungen jetzt,  o  MAh.,  gedenk  dessen  und  erfülle es,  was  unser  Anliegen  bildet,  durch  deine Gewährung  des  Lohns,  den.."  Y.  40.1".
11687:•  j.  Jya-Jata-  Adj,  Von  der  (Bogen)sehoe getroffen,  geschnellt:  isavasal  . .  'tanhi vaamna  "die  Pfeile,  die  von  der  Sehne geschnellt  dahinfliegen"  Yt.  10. 39.
11693:•  j.  ^yä-'>,  p.  _;t)'J-»>  £  'Sehne';  a)  im Fleisch  (nur  Komp.).  b)  des  Bogens: yat..'yä{^.)  navi^yan  (sd.)  Yt/0.ii3i —  as(i  yS  gavasnahe  (sd.)  snäuya  -ya (NS.)  Yt70.  laS.
15394:folgt  Praet :  /=  a'  yai . .  vääm  aKihai>,m  ^ ,  j.  para.pa*want-  Adj.  '(von  der  Sehne,
18520:yat,.aftra  kaAvart (sd.)  Jyä  navi^yan'> tifranhs  aüays  "wenn  .  .  die  Sehnen schwirren,  die  spitzen  Pfeile . ,"  Yt.  10. 1 1 3. Ganz  unsicher;  nur  die  Form  3FKA.  steht fest  —  ')  Oder  mit  (ausl.)  I.  —  >>  Ich  nehme nin/Ay'  {üx  mii^y'  und  verweise  auf  xlaviili
27146:•  j.  snävar-  'Sehne,  Schnur':  'van F.  12.
27147:KompA.  —  Vgl.  ai.  sn&vaii'  n.  'Sehne,  Schnur', OOS5.  m>ar{%ds.2)  'Ader';  weiteres  bei  Hbm. AGr.  /,  478,  Bgm.  GrCr.3  54.  —  S.  auch siiäiiya;  —  Pü. :  dan  ddr');  vgl.  snävarj.- bäsHta:   —    '>  Mit  den  np.  Glossen  mai  und
27148:•  j.  snävara.bäzu'ra-  Adj.  (fem.  °rä-) 'Schnüre,  Sehnen  als  Arme  habend,  des Arme  von  Schnüren,  Sehnen  gebildet  wer- den', von  der  Schleuder;  fradaxlana  °ra mal  %risqs  fradaxlanyais  V.  14-  9-
```


## [2026-09-14T01:29:25.745Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '46205,46245p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Read WLD II 696 sneu- entry"
}
```


### [2026-09-14T01:29:25.796Z] TOOL RESULT

```
696                                      sneu-, sneu-



suit „der Schnitt^",       mhd, mtde „Schneide“, mhd. mitzen         5
                                                                         ,schaitzen“;   aisl.

sneis „klemer   (abgeschnittener) Zweig'‘, ags. sn^s, snas „SpieB,               Speiler*',
mhd. sneise „Reihe, Schnur, worauf etwas gereiht wird“ (*snoid-ta)^ z. B.
Fick III"^ 522f., klr. snU „Klotz^‘, cech. snU          {^snoito-s] Lewy KZ.
40,561); ir.5wezV?„klein, kurz“(*5ne«(ii-5?; Stokes KZ. 38, 471). Dafi "^^sneit-
als .s-praefigierte Form sqneit-
                              zu qen-^ qenei-d-, -t- „kratzeii“ gehore (Jo-
hansson PBrB. 14, 354 f., Falk-Torp u. snitte) ist ganz unerweislich.


sneu- und sneu- etwa „drehen'‘, bes. „Faden zusammendrehen, kniipfen'^;
    andrerseits „sich drehen, schnelle Bewegung"' (diese nur im Germ, und
    Slay, begegnende Bedeutungswendung erst yom Bilde der sich drehen-
    den Spindel? Wenigstens begegnen Formen der leichten und der
    schweren Wzf, im Germ, in beiden Bedeutungen, und weisen die auf
    sneu- beruhenden si. Formen beide Bed. auf, so da6 eine Scheidung
    beider Wzformen nach der Bed. nicht durchfuhrbarist). Dazu swe«-(f)r-,
     -en- (heteroklitisches n., Lit. u. sner) „Sehne, Band“.
   Ai snavan- (n., nom. snava)          Sehne“, a-sncivira- ^.ohne Sehnen‘‘
{snutdh „yon der Sehne“), av. snavars „Sehne'^ (snauya- „aus einer Tier-
sehne gefertigt^‘) gr. vsvqov „Sehne“, vavga „Sehne, Bogensehne"; lat.
                   ;


sehr wahrscheinlich nervus „Sehne, Flechse; Muskel, Nerv“ (s. u. *sner-
„Drehen“, wo Lit. ahd. snuor „Schnur“ usw. wahrscheinlicher zu *sner-j als
                       ;


mit einer bei *sneuer- sonst unbelegten Abtonung sno[u]-ro- hierher) arm.           ;


neard „Sehne, Faser, Fiber“ (Hiibschmann Arm. Gr. 1 478; Gdf. *snmrt;
nicht nach Bartholomae Stud. II 26 f. Anm. 1 aus *sneirt zu sne-, snei-),
   Dagegen ahd. senawa^ ags, sinu^ aisl. sin „Sehne“ zu set- „binden‘‘; sie
```


## [2026-09-14T01:29:27.556Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if \\\"snävar-  'Sehne\\\" in l:\n        print('leaf',i)\n        import re\n        print(re.findall(r'\\b1[0-9]{3}\\b', l)[:20])\n        break\n\"",
 "description": "Find Bartholomae column for snavar"
}
```


### [2026-09-14T01:29:28.888Z] TOOL RESULT

```
leaf 888
['1631']
```


## [2026-09-14T01:29:40.253Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC ==\"; grep -n \"sneu\\|neuron\\|nervus\" IEC.txt | head -8; echo \"== SYN ==\"; grep -n -i \"sinew\\|nervus\\|neuron\" SYN.txt | head -8; echo \"== LAT nervus ==\"; grep -n \"nervus\" LAT.txt | head -5; echo \"== LEW nervus ==\"; grep -n \"nervus\" LEW_1910.txt | head -5",
 "description": "Grep Mann/Buck/Ernout/Walde for nervus"
}
```


### [2026-09-14T01:29:40.357Z] TOOL RESULT

```
== IEC ==
403:aKulos, ios, à ‘barb, awl’. WP I, 29. Cf. aKi- los, aKus Skt. a$ula 'vitex alata; Gk. ákulos “holm acorn'; Alb. éhull, éfull ‘icicle’; Lat. aculeus; cf. nov-acula (see ksneu-); W ebill *gimlet'; OBr. epill; Br. ebil ‘peg, pin’; OE awel, awel, awol; cf. ON -áll (in sóó-áll "book: (Icel. alur ‘awl is ambiguous, see gl) For OCS osla, see akilos
744:aruos (2) ‘quick, ready’. WP I, 141. Cf. oruos Skt. cf. árvan, árvat (act. pt. type 'quick)); Av. aurvO beside aurvafit, wd: OPer. aruva; Tokh. AB arwar B arwer; Gk. cf. aüri, auri- (for phonol. cf. neüron, paüros: Lat. nervus, parvus (7); ON or, acc. grvan; OE earu (beside ge-aru, gs ge-arwes); OS aru (west. ‘ready’)
759:asnu-mi (asneu-) ‘do, work, achieve” Hitt. asnumi “prepare, supply, serve’; Gk. á- nümi beside ánuo, ånd; but cf. sanu-mi; Lat. cf. (?) in-anis (Cineffectual', etc.); Go. cf. asneis ‘labourer’; OHG asni; OE esne; OSax. asna ‘pay’; OFris. esna “to pay
818:aulos, ios ‘hollow, channel Cf. aluos. WP I, 20 & 24-6, also I, 92 Tokh. B (loanword fr. A?) olyi ‘boat; Arm. uy, o, ov and uyi, vo, vov "road, cf. uyuk (dim. “palm of the hand?) (vocalism obscure); Gk. aulós beside aülax, aülion; Lat. alvus, i f. beside alveus (w. possible metathesis as in parvus, nervus); OCS ulij, Cz. úl *hive', cf. priulükü (dim. Jane"); R pere-ulok, id.; Blg. ulej ‘hollow trunk, hive, trough’; Srb. cf. kos-ulja (2) ‘plough’; Li. auls ‘hive’ beside aülas ‘hopper
8205:ksneuo (ksneumi) ‘pierce, stab, be sharp, be keen'. Cf. sneu- Skt. kspaumi ‘sharpen’; Gk. cf. ikshneümon (?) (Cichneumondly,, if for ix, gs ikós ‘grub’ + *ksneu- ‘pierce’); Lat. cf. nov-acula ‘razor’; OE sneowan ‘hasten’; cf. sneome: OS sniumo “quickly”; pp. in Skt. ksnutáh, Av. hu-xinuta-; o-gde in MHG snoede ‘contemptuous’; ON snauór ‘bare; impoverished’
11728:neuó (1) (neu-mi, neuuo) ‘turn, move’. WP II, 323. See sneu- Skt. náve, mp., apa-naumi, v. ‘remove, set aside’; vi-nave, intr. mp. ‘turn, twist, wind’; Gk. neuo (2) ‘bend forward’; do-neüo ‘bend, swing’; W cf. de-nu, inf. ‘lure’; OE cf. neow- ol ‘headlong’; OCS cf. novici, mpl. (money, lit. change")
15199:senouos, à (senouuo-) “twist, gut, sinew'. Cf. sneuàa, sneuor-, sinuos, ambig. Hitt. senahhas, sinahhas ‘snare, ambush’; Lat. sinus, gs: -üs, m. (2) ‘ringlet; bow of net'; cf. sinuosus, adj. ‘winding’; (in)sinuo, are, v. ‘wind’; OHG sénawa, senwa, f. ‘sinew’; MHG sénewe, s & wf. ‘sinew, nerve’; OE. seono, f. ‘sinew’; Sw. sena, f. id. (and nerve")
15218:senuå, see senouá, and cf. sneuá OHG sénwa ‘sinew’: Lat. sinus, üs (bay, lit. *bend"); sinuus ‘winding’ (formally also Hitt. senahhas, sinahhas *ambush")
== SYN ==
3551:snavan- ‘sinew’, etc.’ Walde-P. 2.701. Ernout-M. 689.
10172:1. IE *(s)né-, *(s)néi- in words for ‘spin’, ‘sew’ (Gmc.), ‘thread’, ‘needle’ be- side *sneu- in words for ‘sinew’, primary sense ‘turn, wind’ or ‘stretch’(?). Walde-P. 9.694. Ernout-M. 665 f. Pedersen 1.68, 2.633.
10173:Grk. véw (*ovqw, cf. 3 sg. pres. vp, 3 sg. imperf. én, etc.), v70w, NG pop. yw; Lat. nére; Ir. sni-, NIr. snio- mhaim, W. nyddu, Br. neza : OHG najan ‘sew’; Lett. snat ‘twist lightly’ (as in spinning or esp. plaiting, cf. Miihl.- Endz. 3.974), Skt. sn@yu- and snavan-, Grk. veipov ‘sinew’.
13887:ON snerd ‘twisted rope’, Dan. sn¢re, Sw. sndre, Dan. snor, Du. snoer, OHG, MHG snuor, NHG schnur : Goth. snorjo ‘plaited basket’, OE snér ‘harp-string’, all either : Lith. nertz ‘to noose, thread’, narys ‘knot, loop, link, joint’, etc.; or : Skt. sndvan- ‘band, sinew’, Grk. vedpov ‘sinew’, etc. Walde-P. 2.699. Falk- Torp 1098. Feist 441.
13914:some by-form of *sné(z)- in Skt. sndyu- ‘bond, sinew’, Lat. nére ‘spin’, Ir. snathe ‘thread’, etc. Walde-P. 2.329, 694 f.
13915:W. clwm, cwlwm, Corn. colmen, Br. koulm, skoulm, prob. : Ir. colum ‘skin’ and ‘sinew’ (cf. columne gl. nervus), re- flecting the old use of sinews for binding. Loth, RC 41.375 ff.
22618:OE nearu, ME narowe, NE narrow, OS naru : ON Norva-sund ‘Straits of Gi- braltar’, OHG narwa ‘scar’ (i.e. ‘closed wound’), prob. fr. a root meaning ‘draw together, tie’(?) in OHG snuor ‘band, string’, Lat. nervus ‘tendon’, ‘nerve’, etc. Walde-P. 2.699 f. (with 2.696), Falk- Torp 755.
23082:aes kringlottr, fr. kringla ‘circle’. ON stvalr (also simple valr), OE sin(o)wealt (seonwwalt, etc.); OHG sin(a)- rd, MAG sinwel, OS sinuwel, MLG sinewolt, epds. of ON sz-, OE, OHG sin- ilnays' (= ‘entirely’), and last member ‘ON velia, OE wealtan, OHG walzen toll, turn’, ChS1. valite ‘roll’, Lith. ap- ralus ‘round’ (below, 5), etc. Walde-P. 1302, Falk-Torp 789. Franck-v. W. 07.
== LAT nervus ==
== LEW nervus ==
```


## [2026-09-14T01:29:42.951Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT ==\"; grep -n \"^sinew\\|sinew (\\|nerve,\" SKT.txt | head -8; echo \"== LKT sabbat ==\"; grep -n -i \"sabbat\\|samstag\" LKT.txt | head -8; echo \"== AFM sabt ==\"; grep -n \"السبت\\|سبت\" AFM_pages.txt | head -8; echo \"== TAD ==\"; grep -n \"السبت\" TAD_pages.txt | head -5",
 "description": "Grep Skeat/Lokotsch/AddiShir/Unaysi"
}
```


### [2026-09-14T01:29:43.046Z] TOOL RESULT

```
== SKT ==
== LKT sabbat ==
1200:[Vom  Vb.  dafana  'vergraben,  begraben'] 'zurückgezogene  Frau' ;  hieraus  mit  leicht verständlichem  BedeuLungswandel  sp. adefina,  adafina,  dafina  'ein  bei  den Juden  Spaniens  früher  gebräuchlicher Ragout,  der  Freitags  auf  ein  Kohlen- becken gestellt  und  verdeckt  wurde,  um Samstags  gegessen  zu  werden',  in  er- weiterter Bedeutung  [oder  Rückkehr zur  ursprünglichen]  'verborgene,  geheime Sache'.    [DE  43/44.
1778:'Volk,  heidnisches  Volk',  vulg.  goje 'christliche  Dienerin';  hieraus  prov. gougeo  'Magd',  frz.  «/ow^'t; 'Dirne',  goujat 'Troßbube,  Trainsoldat'.  Jidd.  sabbesgoj ist  derjenige  Nichtjude,  der  dem  Juden das  am  Sabbat  verbotene  Feuer-  und Lichtmaclien  besorgt  [Birnbaum  Hebr El  5ü].
3376:1461a.  Ar.  mimbar: Aussprache  für  ursprüngliches  minbar [von  ar.  nabara  'erheben';  minbar  aXso ursprünglich  die  Erhebung,  auf  die  man sieh  setzt  oder  stellt,  Untergestell,  s. BECKER  in  Orient.  Studien  (Festschrift für  Nöldeke)  I,  S.  338;  letzten  Endes aus  dem  Äthiop.,  s.  Nöldeke,  Neue  Bei- träge, S.  49]  'Kanzel',  und  zwar  im Gegensatz  zur  Predigtkanzel  kurst  die- jenige Kanzel  in  der  Moschee,  auf  der an  jedem  Freitag  die  Jiutba,  d.  h.  das Gebet  für  den  obersten  Herrscher  der Gläubigen,  gehalten  wird.  Hieraus  jüd.- dtsch.  Almemor,  die  inmitten  der  Syna- goge betindliche,  zum  Verlesen  der Tliora  bestimmte  Erhöhung  [die  in  jüd. Schriften  als  bema  oder  mifdal  bezeich- net wird],  vgl.  z.  B.  in  Heinrich  Heines , Prinzessin  Sabbath":  'Stolz  aufflackern auch  die  Kerzen  /  Auf  der  Brüstung des  Almemors'.
3966:Der  Ruhetag  nach  den  sechs  Wochen- tagen; hieraus  gr.  ödßßaxov,  lat.  sab- batum  und  it.  sabbato,  prov.  sabda,  sp. pg.  sdbado,  [mit  Einschiebung  eines  m angeblich  unter  Einfluß  von  lat.  septi- mus]  frz.  samedi,  rum.  sämhätä;  ähnlich in  den  slav.  Sprachen:  VMSs.subota,  serb, subota,  öech.  poln.  sobota,  und  in  den germ.  Sprachen:  dtsch.  Samstag [<^  Sampztag  <^  Sambtac  <^  Sambez- <^  ahd.  Sambaztac],  mhd.  sameztag.  — Die  neuhebr.  Aussprache  sabbes  ergab jüd.-dtsch.  Schabbes  und  russ.  sabas 'Feierabend'  >  'gut,  fertig,  genug!'. Engl,  sabbdth  wird  in  England  und
3969:Amerika,  bes.  in  New-England,  im höheren  Stile  ähnlich  für  'Sonntag'  ge- sagt, wie  etwa  im  Dtsch.  von  'ernster Sabbathstille'  gesprochen  wird.  —  Aus poln.  sobota  wird  sobotka,  plr.  sobötki 'Feier  am  Tage  vor  St.  Johannes',  dazu das  Vb.  sohotowac  'ausruhen,  feiern'. Aus  szabas  'jüdischer Sabbath'  wird  poln. szabasnik  'Art  Ofen',  szabasöwka  'kleiner Leuchter',  szabasowac  'feiern,  d.h.  nicht arbeiten'.  [KLUGE  in  Zeitschrift  des allgemeinen  dtsch.  Sprachvereins.  Wis- sensch. Beiheft  Vin,  98.  Karlowicz416 u.  417.
4364:'Schlaf,  Ruhe,  Lethargie'  [vom  Vb.  sa- bata  'ruhen',  gleicher  Wurzel  wie  Sabbat, s,  hier  Nr.  1742],  ebenso  tk  ;  hieraus poln.  (alt)  subet  'Zuflucht;  Lethargie'. [JVIikl  SlEtWb  328  b.    Karlowicz  422.
7167:sabbato  1742 suboga  sard.  1746 saccheggiare  1781 söcco  1781 .«rtccu  sard.  1781 sacomanno  1781 sacro  1799 saffata  sard.  1753 sagrin  dial.  1760 sata  1778 aaio  1778
7445:sabacus  1744 sabbatum  1742 saccharuDi  1855 Saccus  1781
== AFM sabt ==
697:( )ܐܗ نمت مسبت رضت ]لسن ص يه 3 )ܕ :
== TAD ==
```


## [2026-09-14T01:29:54.151Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3960,3968p' LKT.txt; echo \"== LEW/LAT alt ==\"; grep -n \"neruus\\|nervös\\|nervŏ\\|neruos\" LEW_1910.txt LAT.txt | head -8; echo \"== LAT 'nerv' ==\"; grep -n \"nerv\" LAT.txt | head -8",
 "description": "Lokotsch 1742 and Latin dicts"
}
```


### [2026-09-14T01:29:54.249Z] TOOL RESULT

```
'Pflug'  [vom  Stamme  saj)  'hauen, schlagen'  Vämbery  TktEtWb  S.  142, Nr.  1531;  also  saban  'der  untere  feste Teil  eines  Körpers,  der  in  der  Hand  fest- gehalten oder  in  die  Erde  eingeschlagen wird'],  dazu  kumük.  sabanci  'Ackers- mann, Pflüger';  hieraus  russ.  saban 'zweiräderiger  Pflug',  sabanscik  'Pflüger'. [Gorjajew  309.
1740.  Ar.  sabbäk:
'Kleines  Schiff  mit  drei  Masten  und  la- teinischen Segeln',  im  Mittelmeere  ge- bräuchlich gewesen  [vielleicht  mit  ar. sabaka  'Netz',  s.  hier  Nr.  1737,  irgend- wie verwandt];  hieraus  mit  Imäla [ä  <C  e]  sp.  jabeque,  pg.  chaveco,  (alt) enxabeque  'maurisches  Fischerfahrzeug', it.  sciabecco,  frz.  chebec  'kleines  drei- mastiges  Kriegsschiff'',  it.  stambecco, zambecco,  frz.  zambuche;  dlr^ch.  Schebecke 'schmales  Kriegsschiff'.  IDozy  Oosl  28. DE  352.  Eguilaz  426.  ZfromPh  XXX, 318;  XXXH,  44.    ML  7668.
1741.  Ar.  sabbära:
'Aloe  Aloe  variegata';  hieraus  aiz.gam- mara,  sard.  sevada,  und  mit  Beein- flussung der  Vokale  durch  das  gleich- bedeutende ar.  sabira  sp.  zabila,  zdbila, zdbida,  kat.  cever  'Aloe'.  —  [Ableitung von  saepes  ML  7496  ist  also  irrig]. [DE  35.  WAGNER  in  Herrigs  Archiv CXXXV,  116.
1742.  Hebr.  sabbaö:
Der  Ruhetag  nach  den  sechs  Wochen- tagen; hieraus  gr.  ödßßaxov,  lat.  sab- batum  und  it.  sabbato,  prov.  sabda,  sp. pg.  sdbado,  [mit  Einschiebung  eines  m angeblich  unter  Einfluß  von  lat.  septi- mus]  frz.  samedi,  rum.  sämhätä;  ähnlich in  den  slav.  Sprachen:  VMSs.subota,  serb, subota,  öech.  poln.  sobota,  und  in  den germ.  Sprachen:  dtsch.  Samstag [<^  Sampztag  <^  Sambtac  <^  Sambez- <^  ahd.  Sambaztac],  mhd.  sameztag.  — Die  neuhebr.  Aussprache  sabbes  ergab jüd.-dtsch.  Schabbes  und  russ.  sabas 'Feierabend'  >  'gut,  fertig,  genug!'. Engl,  sabbdth  wird  in  England  und
139
[Pers.  säbbaü
== LEW/LAT alt ==
LAT.txt:3117:laire, cf. neruus et veupov, et les articles paruus, taurus.
LAT.txt:41127:snovati "ourdir", lette snaujis "lacet, lacs". - V.neruus.
LAT.txt:41243:neruus, I m.: 1 tendon, ligament, nerf; au pl.nerwt "muscles,
LAT.txt:41255:Les formes romanes se partagent entre neruus et neruius ; neruulus,-i
LAT.txt:41260:vigoureux, muscle; d*ou neruQsS, neruositas} neruicosus (Gloss.)
LAT.txt:45875:e neruus avec gr. veupov et de aluus avec gr. auXo£; mais, meme si
LAT.txt:68918:forme sur umosus , ayec lequel il allitere. Glose aussi neruosus,
== LAT 'nerv' ==
35498:par suite "amolli,r, dnerver, affaiblir, dpuiser", e.g. Pl., Cap.ysO,
44815:anci en terme du rituel deriv 4 sans doute de Paluda 4 pithete de Minerve,
52118:1 'honneur de Minerve; les maiores se c 414 braient du 19 au 33 mars,
52178:quinquenervi , M.L.6y6sa,b; quinquennis; qulnquert ium,-t io , mots
```


## [2026-09-14T01:29:59.729Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '41243,41275p' LAT.txt",
 "description": "Ernout-Meillet nervus"
}
```


### [2026-09-14T01:29:59.801Z] TOOL RESULT

```
neruus, I m.: 1 tendon, ligament, nerf; au pl.nerwt "muscles,
nerfs : nerui quos xevovTccc Graeci appellant, Ceis.8,1; et aussi
membrum uirile", d'oi "force, virilit^"; 3 0 tout objet fait de ten-
dons: corde d'arc, d'instrument de musique; instrument de supplice
servant a entraver les criminels (d'abord fait de cordes, puis de
cbaines de fer): neruum appellamus etiam ferreum uinculum quo pedes
uel etiam cjruices inpediuntur, P.F. 161,13. Tous ces sens se retrouvent
dans gr.veupov, et ont pu lui etre empruntes, au moins partiellement.
- Ancien (Loi des XII Tab.), usuel. M.L.5898.
Derives et compos^s: neruia,-orum n. (sur l'origine, v.Niedermann,
N. Jahrbo f. kl. Alto ,2535 et neruiae f.: cordes d f un instrument de
musique; nerfs = gr. veupiov et veupiot (Sept.); cf.M.L.5897 neruium.
Les formes romanes se partagent entre neruus et neruius ; neruulus,-i
n.; nerualis (n. herba Scrib. Larg., "plantain", cf. xo veupoeu6eC77 9
nex
Diosc.4,16); neruicus (Vitr.), neruicsus (Vulg.), neruinus (Vdg.);'
nerudsus (seni classique et usitd): tendineux, plein de nerfs; et
vigoureux, muscle; d*ou neruQsS, neruositas} neruicosus (Gloss.)
contaminationde neruicus et neruSsus', eneruis (-uus), et SneruS,-Ss
avec aes dAriv4s; inneruis ( = oivsupos); subneruo (tardif): couper
lea .jarrets, trad. de veupOKOrcetv. Cf. aussi sans doute Kerua, pre-
nom de type populaire ( B gr. veupot); Neruo.laria (fibula^ titre d f une
comddie perdue de Piante.
Le sens et 1'aspect g4neral dn mot indiquent nn rapprochenent avec
gr. veupov, veupot et avec av. snavora (v. sons neo); le sena explique
que le genre 11 anin^ H ait 4to admis. Ia forme gr.veupo— est ce que
l»on attend; mais, ai nn w consonne a etd r4tabli par quelque analogie,
en partie parce qne le radical est *snS, avec e, il a pn y avoir nn
*snStqro- qui, dans la langue populaire, anra 4t4 inverad en neruo -;
cf. aluus, paruus en face de paucus et celt. tarwo- en face de lat.
taurus . Cea inversions semblent etre le fait dn vocabulaire "popn¬
laire
nespula: v, mespilum.
```


## [2026-09-14T01:30:07.704Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"NERVE\\|SINEW\\|SABBATH\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"== ARY fa ==\"; grep -n \"شنبه\\|سنور\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Aryanpur"
}
```


### [2026-09-14T01:30:07.824Z] TOOL RESULT

```
== ARY fa ==
```


## [2026-09-14T01:30:13.510Z] TOOL CALL #67: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%B4%D9%86%D8%A8%D9%87\" \"https://en.wiktionary.org/wiki/sinew\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/sinw%C5%8D\" \"https://www.etymonline.com/word/sabbath\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sn%C3%A9h%E2%82%81wr%CC%A5\" \"https://abadis.ir/fatofa/%D8%B4%D9%86%D8%A8%D9%87/\" \"https://abadis.ir/fatofa/%D8%B3%D8%A8%D8%AA/\" \"https://en.wiktionary.org/wiki/%D7%A9%D7%91%D7%AA\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 428 (book 398): roots Šabatu and Sâi 2/Sneu — šanbeh, sabt, Sabbath, sinew, nervus, neuron\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:30:20.141Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/518d2a36b31bd0db.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5abb9ed455331470.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/21e03998f415f807.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/248d27bb030bc794.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc74294af02db239.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c1be1efb08efc139.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/313cd168f33671c6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8bbe058c60ab10d5.txt
```


## [2026-09-14T01:30:31.570Z] TOOL CALL #68: WebSearch

```json
{
 "query": "Akkadian šapattu šabattu full moon day fifteenth Sabbath etymology disputed CAD šabātu \"to beat\""
}
```


### [2026-09-14T01:30:39.141Z] TOOL RESULT

```
Web search results for query: "Akkadian šapattu šabattu full moon day fifteenth Sabbath etymology disputed CAD šabātu "to beat""

Links: [{"title":"(PDF) The etymology of \"Sabbath\"","url":"https://www.academia.edu/121188250/The_etymology_of_Sabbath_"},{"title":"Biblical Sabbath - Wikipedia","url":"https://en.wikipedia.org/wiki/Sabbath_etymology"},{"title":"1 THE ETYMOLOGY OF “SABBATH” François de Blois, June 2015 [Handout] HEBREW","url":"https://bpb-eu-w2.wpmucdn.com/blogs.ucl.ac.uk/dist/5/322/files/2015/07/SABBATH-paper.pdf"},{"title":"How and When the Seventh Day Became Shabbat - TheTorah.com","url":"https://www.thetorah.com/article/how-and-when-the-seventh-day-became-shabbat"},{"title":"Shabbat, Mid-Fifth Century B.C.E. - TheTorah.com","url":"https://www.thetorah.com/article/shabbat-mid-fifth-century-bce"},{"title":"What Millenia did the Sabbath Begin? | Sefaria","url":"https://www.sefaria.org/sheets/613729"},{"title":"Sabbath Transcript - The Endless Knot","url":"http://www.alliterative.net/sabbath-transcript"},{"title":"Biblical Sabbath","url":"https://en.wikipedia.org/wiki/Biblical_Sabbath"}]

Based on the search results, here's what scholars have found regarding the Akkadian šapattu/šabattu and its connection to Sabbath:

## The Akkadian Terms

A number of scholars propose a cognate Akkadian word šapattu or šabattu, which refers to the day of the full moon. The fifteenth day is called šapattu or šabattu, which is also used for 'full moon' and 'period of fifteen days'.

## Etymology Disputed

The etymology is indeed contested. As yet there is no satisfactory etymology for this. However, it might be connected with the Akkadian word šaptu 'lip', cognate with Hebrew śòp̅ ò, Arabic šafatun, Syriac seftā, etc., from Semitic *s2ap-(a)t-.

## Connection to Sabbath Questioned

Other scholars doubt that the Akkadian and Hebrew terms share a common etymology. Some scholars note that šapattu refers almost exclusively to the fifteenth day of the month or the phenomenon of lunar alignment, not to the seventh day of a week.

Regarding the CAD (Chicago Assyrian Dictionary) entry for šabātu meaning "to beat," this specific reference did not appear in the search results, so I cannot confirm that particular etymological connection from these sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:30:43.915Z] TOOL CALL #69: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Sabbath_etymology\" --note \"page 428 (book 398), root Šabatu: modern view on Akkadian šapattu/šabattu and Hebrew šabbāt\" 2>&1 | tail -2; sed -n '1,80p' tools/verify_check.py",
 "description": "Archive Wikipedia and inspect verify_check"
}
```


### [2026-09-14T01:30:45.632Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4fed7ba9f1861a2c.txt
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


## [2026-09-14T01:30:47.799Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-14T01:30:47.849Z] TOOL RESULT

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


## [2026-09-14T01:37:21.133Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-428.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 428,\n \"book_page\": 398,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Šabatu\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Akkadian šabattu / šapattu 'the 15th day of the month, full-moon day' (noun); the verbal sense 'to cease, stop work' belongs securely to West Semitic *šbt (Hebrew šābat)\",\n   \"note\": \"Nourai's root box is Mo'in's footnote in Borhan-e Qate' p.1300 almost word for word (Mo'in even prints the same source line, 'H. Zimmern, Akkadische Fremdwoerter. Leipzig 1917, s.67'), and Mo'in does gloss Akkadian shabatu as 'استراحت کرد، عاطل گذاشت'. Zimmern himself, however, on exactly that page writes 'akk. šabattu, auch (sekundär) šapattu (Etym. noch unklar), 15. Tag des Monats, Vollmondstag', i.e. a NOUN for the full-moon day whose etymology he calls unclear, and he says only that Hebrew šabbāt is 'wohl sicher' derived from it. Klein (s.v. Sabbath) is more guarded still: 'Akkad. shabatu, which prob. means to cease, be completed'. Modern Assyriology and Semitics (de Blois 2015; the survey in Wikipedia 'Sabbath etymology') note that šapattu denotes the fifteenth day / full moon and NOT a seventh-day rest, that Akkadian šabātu A means 'to beat, strike (of wind)', and that several scholars doubt the Akkadian–Hebrew equation altogether. So the root box is defensible as a report of Zimmern via Mo'in, but the gloss 'to cut, stop working' is a West Semitic meaning retro-fitted onto the Akkadian word. Language label 'Akkadian' is right.\",\n   \"note_fa\": \"ریشهٔ مورد ادعای نورایی، اکدی šabattu / šapattu است. زیمرن در همان صفحه‌ای که نورایی (به واسطهٔ حاشیهٔ معین در برهان قاطع، ص ۱۳۰۰) بدان ارجاع می‌دهد، این واژه را «روز پانزدهم ماه، روز بدر» معنی می‌کند و ریشه‌شناسی آن را «هنوز ناروشن» می‌خواند؛ معنای «بریدن، دست از کار کشیدن» در اصل از ستاک سامی غربی šbt (عبری šābat) است نه از اکدی. آشورشناسی امروزی نیز šabātu اکدی را «زدن، وزیدن (باد)» می‌داند و پیوند اکدی با عبری را قطعی نمی‌شمارد. بنابراین برچسب زبانی درست است ولی معنای ریشه با احتیاط پذیرفتنی است.\",\n   \"sources\": [\n    \"https://en.wikipedia.org/wiki/Sabbath_etymology\",\n    W+\"%D7%A9%D7%91%D7%AA\",\n    \"https://www.etymonline.com/word/sabbath\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"AKD:67\", \"status\": \"partial\", \"note\": \"Zimmern, Akkadische Fremdwörter, p.67 (local AKD.txt, form-feed block 77): 'akk. šabattu, auch (sekundär) šapattu (Etym. noch unklar), 15. Tag des Monats, Vollmondstag : > wohl sicher hebr. šabbāt Sabbath (> aram. šabbtā, > äth. sanbat; ferner σάββατον, sabbatum usw. bis franz. samedi und andererseits Samstag ...)'. The page supports Akkadian > Hebrew > Greek > Latin, but gives the Akkadian word as a noun 'full-moon day' with UNCLEAR etymology, not a verb 'to cut, stop working'.\"},\n    {\"ref\": \"BQT:1300\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, printed p.1300, footnote 1 (read from the page image, saved at data/verification/sources/refs/ocr/BQT/1300.vision.txt): «... لغتی است سامی. در آرامی sabbath، سریانی shabtâ، عبری shabbât، اکدی shabattu ... این کلمه مشتق از افعال ذیل است: عبری shâbat (از کار کنار رفت، استراحت کرد)، سریانی shbat (استراحت کرد)، اکدی shabâtu (استراحت کرد، عاطل گذاشت)، عربی سبت (استراحت کرد) و سبت الشیء (قطع کرد آنرا) ... همین کلمه است که در عربی سبت، «شنبه» و در فرانسوی samedi و در آلمانی Samstag شد. H. Zimmern, Akkadische Fremdwörter. Leipzig. 1917. s.67». This is Nourai's whole chart in one footnote.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p.1368-1369 s.v. Sabbath (KLN_1966.txt leaf 727-728)\", \"stance\": \"partial\", \"note\": \"'fr. Heb. shabbath, Sabbath ..., prop. day of rest, fr. shabbath, he rested, which is rel. to Arab. sabata, he cut off, interrupted, ceased, rested, and to Akkad. shabatu, which PROB. means to cease, be completed' — Klein hedges on the Akkadian meaning that Nourai states flatly.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1742 (LKT.txt line 3966)\", \"stance\": \"partial\", \"note\": \"Lokotsch heads the entry 'Hebr. šabbaṯ: Der Ruhetag nach den sechs Wochentagen; hieraus gr. σάββατον, lat. sabbatum ... frz. samedi ... dtsch. Samstag' — he starts the chain at Hebrew and mentions no Akkadian ancestor at all.\"},\n    {\"src\": \"FVQ\", \"where\": \"p.160-161 s.v. al-Sabt (FVQ_pages.txt block 178)\", \"stance\": \"partial\", \"note\": \"'There can be no doubt that the word came into Arabic from Aram. and probably from the Jewish שבתא rather than from the Syr.' — Jeffery too routes everything through Aramaic, never directly from Akkadian.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Hebrew\", \"words\": \"šâbat\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Biblical Hebrew שָׁבַת šābat (qal perf. 3 m.sg.) 'he ceased, desisted, rested (from work)', root š-b-t, whence the noun שַׁבָּת šabbāt (< *šabbat-, with the geminate/qattal pattern) 'day of ceasing, Sabbath' — the derivation the chart draws inside Hebrew, and the one Genesis 2:2-3 puns on. The relation of this Hebrew verb to Akkadian is the doubtful link (see the root note): Zimmern derives Hebrew šabbāt from Akkadian šabattu 'full-moon day' as a loan, which makes the Hebrew VERB denominative from the borrowed noun rather than its source. Nourai's arrow Akkadian 'to cut, stop working' > Hebrew 'to stop work' therefore smuggles the Hebrew meaning back into Akkadian.\",\n     \"derivation_fa\": \"عبری شَبَت (שָׁבַת) «دست از کار کشید، آرام گرفت» از ستاک سامی š-b-t است و اسم شَبّات (שַׁבָּת) «روز آسایش» از همان ستاک با ساخت qattal ساخته شده. پیوند این فعل عبری با اکدی همان حلقهٔ مورد تردید است: زیمرن šabbāt عبری را وام‌واژه‌ای از šabattu اکدی («روز بدر») می‌داند، و در این صورت فعل عبری خود از آن اسمِ وام‌گرفته مشتق شده است نه برعکس. پس واژه و معنای عبری درست است، ولی جهت پیکان از اکدی به عبری با همان معنای «بریدن/دست کشیدن» ادعایی افزون بر منابع است.\",\n     \"sources\": [W+\"%D7%A9%D7%91%D7%AA\", \"https://www.etymonline.com/word/sabbath\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1300\", \"status\": \"supports\", \"note\": \"Mo'in's footnote 1 on p.1300: «عبری shâbat (از کار کنار رفت، استراحت کرد)» — exactly the node's word and gloss.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1368 s.v. Sabbath\", \"stance\": \"supports\", \"note\": \"'fr. Heb. shabbath, Sabbath ..., prop. day of rest, fr. shabbath, he rested'.\"},\n      {\"src\": \"AKD\", \"where\": \"p.67\", \"stance\": \"partial\", \"note\": \"Zimmern: akk. šabattu ' > wohl sicher hebr. šabbāt Sabbath' — the Hebrew NOUN is the borrowed item; Zimmern says nothing about a Hebrew verb 'to stop work' descending from Akkadian.\"},\n      {\"src\": \"FVQ\", \"where\": \"p.161\", \"stance\": \"supports\", \"note\": \"Jeffery treats Hebrew שבת / Jewish Aramaic שבתא as the source of the Arabic word, presupposing the Hebrew verb-noun pair.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"šanbeh «شنبه»\", \"verdict\": \"plausible\",\n     \"derivation\": \"NP شنبه šanbe 'Saturday' does go back to the Semitic Sabbath word, but not straight from Hebrew as the arrow shows. The attested chain is early Manichaean Middle Persian šmbt /šambat/ 'Sabbath, Saturday' (also Manichaean Parthian šmbt), then late Man. MP šmbd /šambad/, NP شنبذ šambiḏ, and finally شنبه šanbe with the regular MP -ad > NP -a(h) weakening; Shirazi shambed and Gilaki shamba preserve the older shapes (Mo'in). The intrusive -n- shows that Iranian took the word from an Aramaic form of the type šabbtā / šabbaṯā (compare Ethiopic sanbat, Vulgar Greek *sambaton > Romanian sâmbătă, French samedi, German Samstag), not from Hebrew šabbāt directly; Mo'in's own footnote lists «آرامی sabbath، سریانی shabtâ» before the Hebrew form. Semantically the word kept 'Saturday' and, as the pivot of the Persian week, generated دوشنبه, سه‌شنبه etc.\",\n     \"derivation_fa\": \"«شنبه» در فارسی نو از فارسی میانهٔ مانوی šambat (و پارتی مانوی šambat) «شنبه، سبت» است که در متون متأخرتر مانوی به šambad و سپس «شنبذ» و «شنبه» بدل شده؛ صورت‌های گویشی شیرازی shambed و گیلکی shamba (به گفتهٔ معین) همان شکل کهن‌ترند. وجود «ن» میانجی نشان می‌دهد وام‌گیری از صورت آرامی/سریانی šabbṯā ـ نه مستقیماً از عبری šabbāt ـ صورت گرفته است؛ همین «ن» در حبشی sanbat و در samedi فرانسوی و Samstag آلمانی نیز دیده می‌شود. بنابراین ادعای نورایی در اصلِ سامی‌بودنِ واژه درست است، اما پیکانِ «عبری ← فارسی» راهِ واقعی (آرامی و سپس فارسی میانه) را نادیده می‌گیرد؛ حاشیهٔ خود معین هم آرامی و سریانی را پیش از عبری می‌آورد.\",\n     \"sources\": [W+\"%D8%B4%D9%86%D8%A8%D9%87\", \"https://abadis.ir/fatofa/%D8%B4%D9%86%D8%A8%D9%87/\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:2081\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Farsi print pagination cannot be mapped online and the local OCR (MON_part1/2.txt) is too corrupt to locate the headword شنبه (greps for '^شنبه', 'شنبه:' return only running text). The online Mo'in text at abadis.ir/fatofa/شنبه gives only «(شَ بَ یا بِ) (اِ.) روز اول هفتهٔ مسلمانان و یهودیان» with no origin tag, the gloss Nourai reports.\"},\n      {\"ref\": \"BQT:1300\", \"status\": \"supports\", \"note\": \"Mo'in's footnote 1 to Borhan p.1300 (image read, saved to refs/ocr/BQT/1300.vision.txt): «= شنبد (ه‍.م.)، شیرازی shambed، گیلکی shamba  لغتی است سامی. در آرامی sabbath، سریانی shabtâ، عبری shabbât، اکدی shabattu ... همین کلمه است که در عربی سبت، «شنبه» ... شد.» Supports the Semitic origin; note that Mo'in puts Aramaic and Syriac BEFORE Hebrew.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"printed pp.1299-1300, entry شنبد + footnote 1\", \"stance\": \"partial\", \"note\": \"The Saturday word is entered in Borhan as «شنبد ـ بکسر بای ابجد بروزن مـجد، شنبه را گویند که روز اول هفته باشد»; the separate headword «شنبه» on p.1299 is a different word ('the neighing of a horse', «شیههٔ اسب را گویند و بعربی صهیل خوانند»). Mo'in's etymological footnote hangs on شنبد.\"},\n      {\"src\": \"MON\", \"where\": \"vajehyab/abadis online text s.v. شنبه\", \"stance\": \"partial\", \"note\": \"«(شَ بَ یا بِ) (اِ.) روز اول هفتهٔ مسلمانان و یهودیان» — gloss only, no etymology online; Dehkhoda on the same page: «از کلمهٔ عبری شَبَّت. سَبْت».\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'شنبه' and 'SABBATH' in Aryanpur returns nothing — it is a dictionary of Indo-European roots and does not treat Semitic loans.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Greek\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The empty pass-through box is Greek σάββατον sábbaton, the Septuagint's transcription (3rd-2nd c. BCE, Alexandria) of Hebrew šabbāt / Aramaic šabbṯā; the Greek neuter -on ending and the doubled -ββ- render the Hebrew geminate, and the plural τὰ σάββατα was used for the single day, which is why Latin and the Romance forms sometimes look plural. A vulgar variant *σάμβατον with intrusive nasal (Klein) is the ancestor of Vulgar Latin sambatum, French samedi and German Samstag — the same nasal that Persian شنبه shows.\",\n     \"derivation_fa\": \"این جعبهٔ خالی همان σάββατον یونانی است، آوانگاری ترجمهٔ سبعینیه (سدهٔ سوم–دوم پیش از میلاد، اسکندریه) از عبری šabbāt / آرامی šabbṯā؛ دوگانگی ββ برابر مشدّدِ سامی و پایانهٔ خنثای -on یونانی است. صورت عامیانهٔ *σάμβατον با «م» میانجی (به گفتهٔ کلاین) سرچشمهٔ sambatum لاتینی عامیانه، samedi فرانسوی و Samstag آلمانی است ـ همان «ن/م» میانجی که در «شنبه» فارسی هم دیده می‌شود. ادعای نورایی در این حلقه درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/sabbath\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this pass-through box; the link is covered by his KLN:1369 citation on the English node.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1368-1369 s.v. Sabbath\", \"stance\": \"supports\", \"note\": \"'L. sabbatum ... fr. Gk. σάββατον, fr. Heb. shabbath ... Cp. Gk. *σάμβατον, a vulgar var. of σάββατον, whence VL. sambatum'.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 1742\", \"stance\": \"supports\", \"note\": \"'hieraus gr. σάββατον, lat. sabbatum'.\"},\n      {\"src\": \"AKD\", \"where\": \"p.67\", \"stance\": \"supports\", \"note\": \"'ferner σάββατον, sabbatum usw. bis franz. samedi'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The empty box is Latin sabbatum (also pl. sabbata), taken from Greek σάββατον in the Christian Latin of the 2nd-4th c. (Tertullian, the Vetus Latina, the Vulgate) with the usual Greek-neuter > Latin-neuter substitution. It is the source of Italian sabato, Spanish/Portuguese sábado, Catalan dissabte, and of Old French sabat, from which and from Latin directly English took its word; the parallel vulgar sambatum gives French samedi.\",\n     \"derivation_fa\": \"این جعبهٔ خالی همان sabbatum لاتینی (و جمع sabbata) است که در لاتینِ مسیحی سده‌های دوم تا چهارم میلادی (ترتولیان، وتوس لاتینا، ولگات) از σάββατον یونانی گرفته شد، با تبدیل معمول خنثای یونانی به خنثای لاتینی. بازماندگان آن sabato ایتالیایی، sábado اسپانیایی و پرتغالی و dissabte کاتالانی‌اند و صورت عامیانهٔ sambatum به samedi فرانسوی رسیده است. این حلقه بی‌مناقشه و مورد تأیید کلاین و لوکوچ است.\",\n     \"sources\": [\"https://www.etymonline.com/word/sabbath\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given in the book for this pass-through box.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1368-1369 s.v. Sabbath\", \"stance\": \"supports\", \"note\": \"'L. sabbatum (partly through the medium of F. sabbat) (whence also It. sabato, OProvenç., Catal. dis-sapte, Sp., Port. sábado ...)'.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 1742\", \"stance\": \"supports\", \"note\": \"'lat. sabbatum und it. sabbato, prov. sabda, sp. pg. sábado'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"sabbatical; Sabbath\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Sabbath: Old English sabat / sæterndæg glossing, then ME sabat (from Latin sabbatum, partly through Old French sabat); the learned spelling with -th, restoring the Hebrew tāw, appears in the late 14th c. and prevails from the 16th (Etymonline). Sabbatical: from Latin sabbaticus < Greek σαββατικός 'of the Sabbath' + -al; in English first 'of the Sabbath' (1640s), then via the Levitical sabbatical year (every seventh year, Lev. 25) the modern academic sense 'leave every seventh year' (US universities, 1880s). Both words are straight descendants of the Latin box above, so the arrow is right.\",\n     \"derivation_fa\": \"واژهٔ Sabbath انگلیسی از sabbatum لاتینی (تا اندازه‌ای از راه sabat فرانسهٔ کهن) به انگلیسی میانه sabat رسید و املای عالمانهٔ -th ـ که «ت» پایانی عبری را بازمی‌نمایاند ـ از اواخر سدهٔ چهاردهم پیدا شد و از سدهٔ شانزدهم چیره گشت. sabbatical از sabbaticus لاتینی، از σαββατικός یونانی، است و معنای امروزی «مرخصی پژوهشی هر هفت سال» از «سالِ سبت» تورات (لاویان ۲۵) و کاربرد دانشگاه‌های آمریکا در دههٔ ۱۸۸۰ برآمده است. این حلقه بی‌اشکال و مورد تأیید کلاین است.\",\n     \"sources\": [\"https://www.etymonline.com/word/sabbath\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1369\", \"status\": \"supports\", \"note\": \"Klein's 'Sabbath' entry begins on printed p.1368 (KLN_1966.txt leaf 727) and runs over onto p.1369 (leaf 728 opens 'i, F. samedi, Saturday and — prob. through the medium of the Gothic—'); 'Sabbatic, Sabbatical, adj. — L. sabbaticus, fr. Gk. σαββατικός, pertaining to the Sabbath' stands on the same page. Exactly Nourai's claim.\"},\n      {\"ref\": \"AHD:1139\", \"status\": \"not_checked\", \"note\": \"AHD:1139 is a page of the main word list of the American Heritage Dictionary, New College Edition (1975/76); only the Watkins Indo-European appendix is on disk (AHD_watkins1985.txt) and the New College scans on archive.org are lending-only.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1368-1369 s.vv. Sabbath, Sabbatarian, Sabbatic/Sabbatical, Sabbatize\", \"stance\": \"supports\", \"note\": \"the whole sub-family is derived from L. sabbatum < Gk. σάββατον < Heb. shabbath.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 1742\", \"stance\": \"supports\", \"note\": \"'Engl. sabbath wird in England und Amerika, bes. in New-England, im höheren Stile ähnlich für Sonntag gesagt'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Arabic\", \"words\": \"s.b.t\", \"verdict\": \"disputed\",\n     \"derivation\": \"Arabic has both سَبَتَ sabata 'he cut off, ceased, rested' and السَّبْت al-sabt 'Saturday, the Jewish Sabbath', and Nourai draws the whole root down from Akkadian as a second branch parallel to Hebrew. Modern Semitic scholarship reverses part of this. Jeffery (FVQ 160-161) on Qur'anic al-sabt: 'The Muslim authorities treat it as genuine Arabic from سبت to cut ... There can be no doubt that the word came into Arabic from Aram., and probably from the Jewish שבתא rather than from the Syr. ܫܒܬܐ. The verb sabata (vii,163) is then DENOMINATIVE, as Fraenkel, Vocab. 21, has noted' — i.e. the day-name is an Aramaic loanword of the Qur'anic period and the Arabic verb in this sense is built back from it, not inherited from an Akkadian ancestor. Klein keeps only a cognate (not descent) relation: Hebrew šābat 'is rel. to Arab. sabata'. So the node's words and glosses are real, but the arrow Akkadian > Arabic is not the route modern sources give.\",\n     \"derivation_fa\": \"در عربی هم فعل «سَبَتَ» (برید، دست کشید، آرام گرفت) هست و هم «السَّبْت» (روز شنبه، سبتِ یهود)، و نورایی همهٔ ستاک را شاخه‌ای مستقل از اکدی می‌گیرد. جفری در «واژگان دخیل در قرآن» (ص ۱۶۰–۱۶۱) این را وارونه می‌داند: «السبت» وام‌واژه‌ای است از آرامیِ یهودی šabbattā و فعلِ «سَبَتَ» در این معنا ـ به گفتهٔ فرنکل ـ فعلِ اشتقاقی (denominative) از همان اسمِ وام‌گرفته است. کلاین نیز تنها نسبتِ هم‌ریشگی میان šābat عبری و sabata عربی قائل است، نه فرودآمدنِ مستقیم از اکدی. پس واژه‌ها و معناها درست‌اند ولی پژوهش امروزی راهِ «اکدی ← عربی» را نمی‌پذیرد و «آرامی ← عربی» می‌گوید.\",\n     \"sources\": [W+\"%D8%B3%D8%A8%D8%AA\", \"https://en.wikipedia.org/wiki/Sabbath_etymology\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1300\", \"status\": \"supports\", \"note\": \"Mo'in's footnote 1: «عربی سبت (استراحت کرد) و سبت الشیء (قطع کرد آنرا). و آن از «سب» است بمعنی قطع ... همین کلمه است که در عربی سبت ... شد» — Mo'in does present the Arabic root as one of the cognate Semitic verbs alongside Akkadian and Hebrew, as Nourai draws it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"pp.160-161 s.v. السبت (FVQ_pages.txt block 178)\", \"stance\": \"contradicts\", \"note\": \"'There can be no doubt that the word came into Arabic from Aram., and probably from the Jewish שבתא ... The verb سبت, vii,163, is then denominative, as Fraenkel, Vocab, 21, has noted. It is doubtful if the word occurs in this meaning earlier than the Qur'an.'\"},\n      {\"src\": \"KLN\", \"where\": \"p.1368 s.v. Sabbath\", \"stance\": \"partial\", \"note\": \"'Heb. shabbath ... whence also Aram. shabbtā, Arab. sabt, Ethiop. sanbat' and 'rel. to Arab. sabata, he cut off, interrupted, ceased, rested' — Klein makes Arabic sabt a descendant of the HEBREW word, and the verb only a cognate.\"},\n      {\"src\": \"AFM\", \"where\": \"AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"Addi Shir's dictionary of Persian loans in Arabic has no entry for سبت (grep 'سبت' returns only an OCR-garbled unrelated line) — expected, since سبت is not a Persian loan.\"},\n      {\"src\": \"AKD\", \"where\": \"p.67\", \"stance\": \"silent\", \"note\": \"Zimmern routes Akkadian šabattu to Hebrew, then Aramaic and Ethiopic, and never mentions Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Persian\", \"words\": \"sabt «سَبْت»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP سَبْت sabt 'Saturday, the Jewish Sabbath' is a plain literary Arabism, taken from Arabic السَّبْت al-sabt with the Arabic consonant cluster -bt preserved; it belongs to the Qur'anic/religious register (أصحاب السبت 'the people of the Sabbath') and never displaced the inherited شنبه in everyday Persian, which is why the two Persian boxes of this chart sit on different branches. Mo'in marks it [ع.] (Arabic) and glosses it «شنبه، نخستین روز هفته». The same word passed on from Persian into Urdu (Wiktionary: 'Borrowed from Classical Persian سَبْت (sabt), from Arabic السَّبْت').\",\n     \"derivation_fa\": \"«سَبْت» در فارسی وام‌واژه‌ای ادبی و دینی از عربی «السَّبْت» است، با حفظ خوشهٔ همخوانی -بْت؛ کاربرد آن بیشتر در بافت قرآنی و دینی است («اصحاب السبت») و هرگز جای «شنبهٔ» موروثی را در زبان روزمره نگرفته است ـ و به همین سبب دو جعبهٔ فارسیِ این نمودار روی دو شاخهٔ جداگانه‌اند. معین آن را با نشانهٔ [ع.] می‌آورد و «شنبه، نخستین روز هفته» معنی می‌کند. همین واژه از فارسی به اردو نیز رفته است. ادعای نورایی در این حلقه درست است.\",\n     \"sources\": [W+\"%D8%B3%D8%A8%D8%AA\", \"https://abadis.ir/fatofa/%D8%B3%D8%A8%D8%AA/\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:1815\", \"status\": \"partial\", \"note\": \"The print page cannot be reached (Mo'in's pagination is not mapped online and MON_part1/2.txt OCR is unusable for this headword), but the Mo'in text itself, served at abadis.ir/fatofa/سبت, reads «(سَ) [ع.] (اِ.) شنبه، نخستین روز هفته» — the Arabic origin tag and the gloss 'Saturday' that Nourai reports.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"abadis.ir online Mo'in text s.v. سبت\", \"stance\": \"supports\", \"note\": \"«(سَ) [ع.] (اِ.) شنبه، نخستین روز هفته» — tagged [ع.] = Arabic.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', footnote to p.1300\", \"stance\": \"supports\", \"note\": \"Mo'in there equates «عربی سبت» with the Semitic Sabbath word and says «همین کلمه است که در عربی سبت ... شد».\"},\n      {\"src\": \"FVQ\", \"where\": \"pp.160-161\", \"stance\": \"supports\", \"note\": \"Jeffery establishes Arabic al-sabt as the Qur'anic word for the Jewish Sabbath, which is the form Persian borrowed.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 5,\n   \"root\": \"Sâi 2, Sěi 3, Sî 3; Sneu, Sněu, Snŭ\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *sneh₁u- / *snéh₁wr̥ 'sinew, tendon' (Pokorny sneu-, snēu- p.977), an extension of *(s)neh₁- 'to spin, twist threads'; the first half of the heading is the separate root *seh₁(i)- / *sh₁i- 'to bind' (Pokorny 3. sē(i)- p.891)\",\n   \"note\": \"The box is right about the material but merges two roots that the handbooks keep apart. POK:977 is 'sneu-, snēu- und snū-, Meaning: to turn, to bind, attach; band; sinew', with exactly Nourai's Avestan snāvarə, Greek neuron and Latin nervus; KLN:1448 is Klein's 'sinew' entry, which derives the Germanic word 'fr. I.-E. base *sai-, *sei-, *sī-, to bind' — that is where Nourai's 'Sâi 2, Sěi 3, Sî 3' comes from, and it is Pokorny p.891 (AHD sē-4 'to bind, tie ... Suffixed form *si-nw- in Germanic *sinwo- in Old English sinu, seonu, tendon: SINEW [Pok. 3. sē(i)- 891]'). Walde-Pokorny II 696 states the split in one line: after listing Skt snāvan-, Av. snavarə, Gk. neuron, Lat. nervus under sneu-, it adds 'Dagegen ahd. senawa, ags. sinu, aisl. sin Sehne zu sē(i)- binden'. So Nourai has silently glued POK 891 + POK 977 into one root box. Both glosses ('to bind' / 'cord, band, tendon') are correct for their halves and the root is real; the merge is the reason for 'plausible' rather than 'confirmed'. Note that current Wiktionary/LIV practice has moved the other way and puts Proto-Germanic *sinwō under *senh₁-weh₂ beside *snéh₁wr̥, i.e. back with the sinew root.\",\n   \"note_fa\": \"جعبهٔ ریشه از نظر مواد درست است اما دو ریشهٔ جداگانه را در هم آمیخته. «Sneu, Sněu, Snŭ» همان *sneu-/snēu- پوکورنی (ص ۹۷۷) «تابیدن، بستن؛ بند، زه» است با همان نمونه‌های اوستایی snāvar-، یونانی neuron و لاتینی nervus؛ ولی «Sâi ۲، Sěi ۳، Sî ۳» ریشهٔ دیگری است: *sē(i)- «بستن» (پوکورنی ص ۸۹۱) که کلاین در مدخل sinew (ص ۱۴۴۸) و واتکینز در پیوست AHD بدان ارجاع می‌دهند. والده-پوکورنی (ج ۲ ص ۶۹۶) صریحاً می‌نویسد: «در برابر، senawa آلمانی علیای کهن و sinu انگلیسی کهن و sin ایسلندی کهن به sē(i)- «بستن» تعلق دارند». پس ریشه‌شناسیِ نورایی پذیرفتنی است ولی ادغام دو ریشه در یک جعبه از خود اوست؛ گفتنی است که ویکی‌واژه امروز *sinwō ژرمنی را دوباره در خانوادهٔ *snéh₁wr̥ می‌نشاند.\",\n   \"sources\": [\n    W+\"Reconstruction:Proto-Indo-European/sn%C3%A9h%E2%82%81wr%CC%A5\",\n    W+\"Reconstruction:Proto-Germanic/sinw%C5%8D\",\n    W+\"sinew\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:977\", \"status\": \"supports\", \"note\": \"Pokorny p.977 (POK_full.txt, 'Page(s): 977'): 'Root/lemma: sneu-, snū- and snēu-. Meaning: to turn, to bind, attach; band; sinew. Material: Old Indic snāvan- ... Avestan snavarə sinew ... gr. νεῦρον sinew, νευρά sinew, bowstring; Latin nervus sinew, tendon; muscle, Nerv ... References: WP. II 696.' Every branch of Nourai's chart except the Germanic one stands on this page.\"},\n    {\"ref\": \"KLN:1448\", \"status\": \"supports\", \"note\": \"Klein printed p.1448 (KLN_1966.txt leaf 768, which carries the printed number 1448) s.v. sinew: 'ME. senewe, sinewe, fr. OE. seonu, sinu ... fr. I.-E. base *sai-, *sei-, *sī-, to bind, whence also OI. snāvah sinew, Avestic snavare, of s.m., Ir. sīn chain, Lett. pa-sainis cord, string.' This is verbatim the first half of Nourai's root heading.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.696 (WLD_Bd2_pages.txt line 46205 ff.)\", \"stance\": \"partial\", \"note\": \"'sneu- und snēu- etwa drehen, bes. Faden zusammendrehen, knüpfen ... Dazu sneu(e)r-, -en- (heteroklitisches n.) Sehne, Band. Ai. snāvan- ... av. snavarə Sehne ... gr. νεῦρον ... lat. sehr wahrscheinlich nervus ... Dagegen ahd. senawa, ags. sinu, aisl. sin Sehne zu sē(i)- binden.' Supports the root but explicitly splits off the Germanic word.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. (s)neu- and sē-4 (AHD_watkins1985.txt lines 968-970, 909)\", \"stance\": \"partial\", \"note\": \"'(s)neu-. Tendon, sinew. Extension of (s)nē-. Suffixed form *(s)neu-r-, ... a. *neu-r-o- in Greek neuron ... b. metathesized form *nerwo- in Latin nervus [Pok. snēu- 977]' AND separately 'sē-4. To bind, tie. ... Suffixed form *si-nw- in Germanic *sinwo- in Old English sinu, seonu, tendon: SINEW [Pok. 3. sē(i)- 891]'. Two roots, as in Nourai's heading, but kept apart.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.16/6.33 (SYN.txt lines 10172-10173)\", \"stance\": \"supports\", \"note\": \"'IE *(s)nē-, *(s)nēi- in words for spin, sew ... beside *sneu- in words for sinew, primary sense turn, wind or stretch. Walde-P. 2.694 ... Skt. snāyu- and snāvan-, Grk. νεῦρον sinew.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.vv. senouos and sneuā (IEC.txt lines 15199, 15218)\", \"stance\": \"partial\", \"note\": \"'senouos, ā (senouuo-) twist, gut, sinew. Cf. sneuā, sneuor-, sinuos ... OHG sénawa, senwa f. sinew; MHG sénewe; OE seono f. sinew; Sw. sena' — Mann sets up a separate stem senou- for the Germanic word beside sneuor-.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"snâvar\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Younger Avestan snāuuarə / snāvar- (neuter r/n-heteroclite, gen. *snāuuan-) 'sinew, cord', continuing PIE *snéh₁wr̥ with regular Iranian *sn- kept word-initially (contrast Ossetic nawr, Pashto/Balochi n-, where sn- > n-). It is directly cognate with Vedic snā́van- n. 'band, sinew', Armenian neard, Greek neuron and Latin nervus, and it yields the Avestan adjective snāuuiia- 'made of animal sinew' and the compound snāuuarə.bāzura- 'having sinews for arms' (of a sling, Vd. 14.9). So the root > Avestan arrow is exactly right; the only quibble is the gloss order — Bartholomae's 'Sehne, Schnur' is 'sinew, cord', i.e. the physical tendon first.\",\n     \"derivation_fa\": \"اوستایی جوان snāuuarə / snāvar- اسمی خنثی از گونهٔ r/n (قلب‌شونده) به معنی «زه، رَگ، ریسمان» است و دنبالهٔ هندواروپایی آغازین *snéh₁wr̥ به شمار می‌رود؛ خوشهٔ آغازین sn- در اوستایی نگاه داشته شده، حال آنکه در آسی (nawr) و پشتو و بلوچی به n- ساده شده است. هم‌ریشه‌های آن سنسکریت snā́van- «بند، زه»، ارمنی neard، یونانی neuron و لاتینی nervus‌اند، و در خود اوستا صفت snāuuiia- «ساخته‌شده از زهِ جانور» و ترکیب snāuuarə.bāzura- «زه‌بازو» (وندیداد ۱۴٫۹) از آن ساخته شده است. پس پیکانِ ریشه ← اوستایی درست است و بارتولومه و پوکورنی هر دو آن را تأیید می‌کنند.\",\n     \"sources\": [W+\"Reconstruction:Proto-Indo-European/sn%C3%A9h%E2%82%81wr%CC%A5\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:977\", \"status\": \"supports\", \"note\": \"'Avestan snavarə sinew (snauya- from an Tiersehne gefertigt)' stands in the Material section of Pokorny p.977 — the node's word, language and gloss.\"},\n      {\"ref\": \"KLN:1448\", \"status\": \"supports\", \"note\": \"Klein p.1448 s.v. sinew cites 'Avestic snavare' among the cognates of the base *sai-/*sei-/*sī-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 1631 (BRT.txt form-feed block 888, which carries the column number 1631)\", \"stance\": \"supports\", \"note\": \"'j. snāvar- Sehne, Schnur: ... Vgl. ai. snāvan- n. Sehne, Schnur, oss. nwar (id.) Ader; weiteres bei Hübschmann AGr. I, 478 ... S. auch snāuuya-' and the following entry 'j. snāvara.bāzura- Adj. Schnüre, Sehnen als Arme habend ... V. 14.9'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p.253-254 §f (HUB.txt block 264)\", \"stance\": \"supports\", \"note\": \"'Idg. sn bleibt anl. im Zd. als sn ... vgl. osset. nawr, nvar Ader = zd. snavare Sehne'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.696\", \"stance\": \"supports\", \"note\": \"'av. snavarə Sehne (snauya- aus einer Tiersehne gefertigt)'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"snavar «سَنَّور»\", \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"extraction\",\n     \"book_prints\": \"سنَوَر\",\n     \"correct_form\": \"snavar — a Book-Pahlavi (Zand) form; it has no established New Persian spelling, and «سَنَّور» (sannawr) is not it\",\n     \"derivation\": \"Two problems, one of transcription and one of substance. (1) Transcription: the printed page 398 shows the letters س ن و ر with a fatḥa over ن and a fatḥa over و and NO šadda — «سنَوَر», matching the transliteration 'snavar'; the JSON prints «سَنَّور», with the fatḥa moved onto س and a šadda added to ن, which spells sannawr/sinnawr, the Arabic word for 'cat'. That is an extraction error in the diacritics (the consonant skeleton سنور is right). (2) Substance: the source Nourai cites, Horn no. 180 on p.291, is in Horn's appendix 'Verlorenes Sprachgut' (Grundriss p.262 ff.), a list of MIDDLE Persian/Pahlavi words that did not survive; the entry reads 'snavar Sehne (nur AW.-Komm.; auch für aw. ϑanvar), vielleicht nur Transcription', i.e. 'sinew', attested only in the Pahlavi Avesta commentary, and Horn already suspects it is nothing but a transcription of the Avestan word. Hübschmann (Pers. Stud. 253-254) says so flatly: 'phl. snavar ist nur Umschreibung des Zendwortes'. So the node is not a New Persian word at all, and the gloss 'cord, band' should be 'sinew'. The genuine Iranian continuations of Av. snāuuarə are Ossetic nwar/nawr 'vein, sinew' (Horn p.292), not any Persian form.\",\n     \"derivation_fa\": \"این گره دو اشکال دارد: یکی خطای خوانش اسکن و دیگری خطای ماهوی. نخست، در صفحهٔ چاپی ۳۹۸ خودِ کتاب «سنَوَر» چاپ شده است (س ن و ر با فتحه روی ن و و، بی تشدید) که با آوانگاری snavar می‌خواند؛ اما در داده‌های استخراجی «سَنَّور» آمده که با تشدیدِ ن همان «سِنَّور» عربی به معنی «گربه» است ـ پس خطا در خوانشِ حرکت‌هاست نه در کتاب. دوم، مأخذی که نورایی می‌دهد (هرن، شمارهٔ ۱۸۰، ص ۲۹۱) در بخش «واژگان ازدست‌رفته» (Verlorenes Sprachgut) است و دربارهٔ واژه‌ای پهلوی است نه فارسی نو: «snavar «زه» (تنها در تفسیر پهلویِ اوستا)، شاید صرفاً آوانگاری باشد». هوبشمان (پژوهش‌های فارسی، ص ۲۵۳–۲۵۴) نیز می‌نویسد «snavar پهلوی تنها رونویسیِ واژهٔ زند است». بنابراین چنین واژه‌ای در فارسی نو وجود ندارد و معنای آن هم «زه/رگ» است نه «بند و ریسمان»؛ بازماندهٔ راستین snāuuarə اوستایی در ایرانی، nwar/nawr آسی است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"HRN:291\", \"status\": \"partial\", \"note\": \"Horn, Grundriss der neupersischen Etymologie, printed p.291 (HRN.txt block 313, header '291'), entry '180. snavar Sehne (nur AW.-Komm.; auch für aw. ϑanvar), vielleicht nur Transcription.', continuing on p.292 'aw. snāvar- Sehne; ai. snāvan- Band, Sehne; arm. neard Nerv, Sehne (Hübschmann, No. 217); oss. d. nawr, i. nvar Ader (No. 195).' The page has the word and the Avestan etymology Nourai draws, but labels it Pahlavi, glosses it 'Sehne' (not 'cord, band'), and doubts it is a real word — none of which the chart conveys.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien pp.253-254 (HUB.txt block 264)\", \"stance\": \"contradicts\", \"note\": \"'osset. nawr, nvar Ader = zd. snavare Sehne (phl. snavar ist nur Umschreibung des Zendwortes)' — Hübschmann denies that phl. snavar is a real Middle Persian word.\"},\n      {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary has no headword snavar (grep 'snavar', 'snʾwl' finds nothing), consistent with Horn's and Hübschmann's verdict that it is a Zand transcription rather than a Pahlavi lexeme.\"},\n      {\"src\": \"BRT\", \"where\": \"col. 1631\", \"stance\": \"partial\", \"note\": \"Bartholomae records under Av. snāvar- a Pahlavi gloss ('Pü.: ...') and the note 'Mit den np. Glossen ...', i.e. the word is known only as an Avesta-commentary gloss, not as a living Persian word.\"},\n      {\"src\": \"MON\", \"where\": \"abadis/vajehyab Mo'in and Dehkhoda\", \"stance\": \"silent\", \"note\": \"no Persian dictionary consulted has a headword سنور meaning 'cord, band'; Persian سنور/سنّور is the Arabism 'cat'.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Germanic\", \"words\": \"senawô\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *senawō / *sinwō f. 'sinew, tendon' (also reconstructed *senuwō, *sinawō), whence OHG senawa (> MHG senewe > German Sehne), OS sinewa, OE seonu/sinu, ON sin, Dutch zenuw, Swedish sena. Nourai's spelling senawô is the OHG-based reconstruction used in the AHD appendix, and the reference 'AHD' is exact: Watkins s.v. sē-4 'To bind, tie ... Suffixed form *si-nw- in Germanic *sinwo- in Old English sinu, seonu, tendon: SINEW [Pok. 3. sē(i)- 891]'. Which PIE root feeds it is the open question (see the entry note): Walde-Pokorny, Klein and Watkins attach it to *sē(i)- 'to bind' with an -nu- suffix, while current Wiktionary derives *sinwō from *senh₁-weh₂ beside the more usual *snéh₁wr̥, i.e. from the sinew root itself. Either way the word is real and belongs under Nourai's double heading.\",\n     \"derivation_fa\": \"ژرمنی آغازین *senawō / *sinwō (مؤنث) «زه، وتر» است که OHG senawa (> Sehne آلمانی)، انگلیسی کهن seonu/sinu، نورس کهن sin، هلندی zenuw و سوئدی sena از آن‌اند. املای senawô در نمودار، صورت بازسازی‌شده‌ای است که پیوست AHD به کار می‌برد و ارجاع «AHD» دقیق است: واتکینز ذیل ریشهٔ sē-4 «بستن» می‌نویسد «صورت پسوندیِ *si-nw- در ژرمنی *sinwo-، در انگلیسی کهن sinu, seonu «وتر»». اینکه این واژه به کدام ریشهٔ هندواروپایی بازمی‌گردد هنوز محل بحث است: والده-پوکورنی و کلاین و واتکینز آن را به *sē(i)- «بستن» می‌بندند و ویکی‌واژهٔ امروزی به *senh₁-weh₂ در کنار *snéh₁wr̥. در هر دو حالت واژه راست است و زیر عنوانِ دوگانهٔ نورایی جای می‌گیرد.\",\n     \"sources\": [W+\"Reconstruction:Proto-Germanic/sinw%C5%8D\", W+\"sinew\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 909): 'sē-4. To bind, tie. Contracted from *seə-. Variant *seəi-, zero-grade form *si-. Suffixed form *si-nw- in Germanic *sinwo- in Old English sinu, seonu, tendon: SINEW. [Pok. 3. sē(i)- 891.]' — Nourai's unpaged 'AHD' reference is this appendix entry.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1448 s.v. sinew\", \"stance\": \"supports\", \"note\": \"'OE. seonu, sinu, rel. to OS. sinewa, ON. sin, sina, ... OHG. senawa, MHG. senewe, senwe, G. Sehne, fr. I.-E. base *sai-, *sei-, *sī-, to bind'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.696\", \"stance\": \"partial\", \"note\": \"'Dagegen ahd. senawa, ags. sinu, aisl. sin Sehne zu sē(i)- binden' — the Germanic word is assigned to the OTHER of Nourai's two root halves.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. senouos (IEC.txt line 15199)\", \"stance\": \"supports\", \"note\": \"'senouos, ā (senouuo-) twist, gut, sinew ... OHG sénawa, senwa, f. sinew; MHG sénewe ... OE seono, f. sinew; Sw. sena, f. id. (and nerve)'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"sinew\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE seonu / sinu (fem. wō-stem, gen. sinwe) > ME senewe, sinewe > NE sinew; the modern spelling keeps the inflectional -w- of the oblique stem, and the vowel of the nominative gives the -i-. Sense 'tendon' throughout, with the figurative 'source of strength' ('the sinews of war') from the 16th c. Old English also had the compound hōh-sinu 'hock sinew' (Klein s.v. hock), which shows the word in its literal anatomical use. The arrow Germanic > English is uncontroversial.\",\n     \"derivation_fa\": \"انگلیسی کهن seonu/sinu (مؤنث، حالت غیرفاعلی sinwe) به انگلیسی میانه senewe/sinewe و سپس sinew امروزی رسیده است؛ «w» املای امروزی از ستاکِ غیرفاعلی و واکهٔ «i» از صورت فاعلی مانده است. معنای آن همواره «وتر، زه» بوده و کاربرد مجازی «مایهٔ نیرو» (the sinews of war) از سدهٔ شانزدهم پیدا شده است. ترکیب انگلیسی کهنِ hōh-sinu «وتر پاشنه» نیز کاربرد تشریحی آن را نشان می‌دهد. این حلقه بی‌مناقشه است و کلاین و ویکی‌واژه آن را تأیید می‌کنند.\",\n     \"sources\": [W+\"sinew\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the book gives no reference on this box; the parent box's 'AHD' and the root's KLN:1448 cover it.\"}],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1448 s.v. sinew\", \"stance\": \"supports\", \"note\": \"'sinew, n. — ME. senewe, sinewe, fr. OE. seonu, sinu'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sē-4 and index (lines 909, 2260)\", \"stance\": \"supports\", \"note\": \"'SINEW sē-4' in the English index; the root entry ends '... in Old English sinu, seonu, tendon: SINEW'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Latin\", \"words\": \"nervus\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin nervus, -ī m. 'tendon, ligament, sinew; bowstring, string of an instrument; fetter; (pl.) strength', already in the Twelve Tables. It continues *(s)neuro- with loss of initial s- and metathesis of the -eur- sequence to -erw-: Ernout-Meillet, s.v., 'le sens et l'aspect général du mot indiquent un rapprochement avec gr. νεῦρον, νευρά et avec av. snāvarə ... il a pu y avoir un *snēuero- qui, dans la langue populaire, aura été inversé en nervo-; cf. alvus, parvus en face de paucus et celt. tarwo- en face de lat. taurus'. Pokorny and Watkins say the same ('metathesized form *nerwo-'). The physical senses of nervus were partly calqued on Greek neuron, and the anatomical 'nerve' sense is a Hellenistic medical transfer.\",\n     \"derivation_fa\": \"لاتینی nervus «وتر، زه، رباط؛ زهِ کمان و ساز؛ بند و زنجیر؛ (جمع) نیرو» است و از دوازده‌لوح به بعد گواهی دارد. این واژه دنبالهٔ *(s)neuro- است با افتادن s- آغازین و قلبِ (metathesis) خوشهٔ -eur- به -erw-؛ ارنو و مِیه می‌نویسند که صورتی چون *snēuero- در زبان عامیانه وارونه شده و nervo- داده است، همان‌گونه که alvus در برابر یونانی aulos و parvus در برابر paucus و tarwo- کلتی در برابر taurus لاتینی. پوکورنی و واتکینز نیز همین «صورت قلب‌شده *nerwo-» را می‌آورند. معنای پزشکیِ «عصب» ترجمهٔ قرضیِ neuron یونانی در دورهٔ هلنیستی است. ادعای نورایی درست است.\",\n     \"sources\": [W+\"Reconstruction:Proto-Indo-European/sn%C3%A9h%E2%82%81wr%CC%A5\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:977\", \"status\": \"supports\", \"note\": \"Pokorny p.977, Material: 'Latin nervus sinew, tendon; muscle, Nerv' listed immediately after Greek neuron under sneu-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. neruus (LAT.txt lines 41243-41272)\", \"stance\": \"supports\", \"note\": \"'neruus, ī m.: tendon, ligament, nerf ... rapprochement avec gr. νεῦρον, νευρά et avec av. snavarə ... le radical est *snē- ... il a pu y avoir un *snēuero- qui ... aura été inversé en neruo-; cf. aluus, paruus ... celt. tarwo- en face de lat. taurus.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)neu- (line 970)\", \"stance\": \"supports\", \"note\": \"'b. metathesized form *nerwo- in Latin nervus, sinew: NERVE; ENERVATE. [Pok. snēu- 977.]'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.696\", \"stance\": \"supports\", \"note\": \"'lat. sehr wahrscheinlich nervus Sehne, Flechse; Muskel, Nerv'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"nerve, nervous\", \"verdict\": \"confirmed\",\n     \"derivation\": \"nerve: ME nerve, from Latin nervus (partly through Old French nerf), first in the classical senses 'sinew, tendon' and 'bowstring', the anatomical 'nerve fibre' sense following the Galenic tradition from the 16th c., and 'courage, coolness' from the 19th. nervous: ME nervous from Latin nervōsus 'sinewy, vigorous'; the modern sense 'easily agitated' develops in the 18th c. out of the medical 'suffering from disordered nerves'. Straight Latin > English descent, exactly as drawn.\",\n     \"derivation_fa\": \"واژهٔ nerve از انگلیسی میانه و آن از nervus لاتینی (تا اندازه‌ای از راه nerf فرانسهٔ کهن) است؛ نخست به همان معناهای کلاسیک «وتر، زه کمان» و از سدهٔ شانزدهم ـ در پی سنت جالینوسی ـ به معنای «عصب»، و از سدهٔ نوزدهم به معنای «خونسردی و جرئت». صفت nervous از nervōsus لاتینی «پُروتر، نیرومند» است و معنای امروزیِ «عصبی، مضطرب» در سدهٔ هجدهم از کاربرد پزشکیِ «مبتلا به اختلال اعصاب» برآمده است. زنجیرهٔ لاتینی ← انگلیسی دقیقاً همان است که نمودار نشان می‌دهد.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. (s)neu- (AHD_watkins1985.txt line 970) ends the Latin branch with the English derivatives in small caps: 'NERVE; ENERVATE'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1030 s.vv. nerve, nervous (KLN_1966.txt lines 25279, 25282)\", \"stance\": \"supports\", \"note\": \"'nerve, n. — L. nervus, sinew, tendon; cord, bowstring; nerve; vigor, force, cogn. with Gk. νεῦρον (for *sneurom) of s.m., OI. snāvan-, band, sinew, Avestic snāvarə, sinew, Toch. B ṣñaura ...' and 'nervous, adj. ... fr. L. nervosus, sinewy, vigorous, fr. nervus'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. neruus\", \"stance\": \"supports\", \"note\": \"lists neruōsus among the derivatives: 'neruōsus (sens classique et usité): tendineux, plein de nerfs; et vigoureux, musclé'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Greek\", \"words\": \"neuron\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Ancient Greek νεῦρον neûron 'sinew, tendon; cord, bowstring; (pl.) strength', beside νευρά neurá 'bowstring'. It is the most transparent reflex of the root: *sneh₁-ur-o- with the regular Greek loss of initial s- before a nasal (compare νέω 'spin' < *sneh₁-) and -eu- from the *-eh₁u- sequence; Klein spells it out, 'Gk. νεῦρον (for *sneurom)'. From Hippocrates and Aristotle onward it is also the anatomical term, and in Galen it takes on the modern sense 'nerve'. The gloss 'sinew' on the chart is the primary meaning, correctly given.\",\n     \"derivation_fa\": \"یونانی باستان νεῦρον «زه، وتر، ریسمان، زهِ کمان» (و νευρά «زه کمان») روشن‌ترین بازماندهٔ این ریشه است: از *sneh₁-ur-o- با افتادن قاعده‌مندِ s- آغازین پیش از خیشومی در یونانی (بسنجید با νέω «رشتن» از *sneh₁-). کلاین صریحاً می‌نویسد «νεῦρον (به جای *sneurom)». این واژه از بقراط و ارسطو به بعد اصطلاح تشریحی است و در جالینوس معنای امروزیِ «عصب» می‌یابد. معنای «زه/وتر» که نمودار می‌دهد معنای نخستین و درست آن است.\",\n     \"sources\": [W+\"Reconstruction:Proto-Indo-European/sn%C3%A9h%E2%82%81wr%CC%A5\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:977\", \"status\": \"supports\", \"note\": \"Pokorny p.977, Material: 'gr. νεῦρον sinew, νευρά sinew, bowstring' directly under sneu-, snū- and snēu-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1030 s.vv. nerve, neuro- (KLN_1966.txt lines 25279, 25321)\", \"stance\": \"supports\", \"note\": \"'Gk. νεῦρον, sinew, tendon; cord, bowstring, nerve; strength, vigor, which stands for *sneurom and is cogn. with L. nervus'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II p.696\", \"stance\": \"supports\", \"note\": \"'gr. νεῦρον Sehne, νευρά Sehne, Bogensehne'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)neu- (line 968)\", \"stance\": \"supports\", \"note\": \"'a. *neu-r-o- in Greek neuron, sinew: NEURO-, NEURON; APONEUROSIS'.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"neuron, neurology\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Both are learned modern coinages on Greek νεῦρον, not inherited words: neuron is Greek neuron taken over as a technical term, used for the nerve cell by Waldeyer in 1891 (German Neuron) and in English from the 1890s; neurology is Modern Latin neurologia (Willis, Cerebri anatome, 1664) from neuro- + -logia. The combining form neuro- (before a vowel neur-) is Klein's 'Gk. νευρο-, νευρ-, fr. νεῦρον'. So the Greek > English arrow is a borrowing of a scientific vocabulary, not a phonetic descent — worth saying, but exactly what the chart means.\",\n     \"derivation_fa\": \"هر دو واژه ساخته‌های نوِ علمی بر پایهٔ νεῦρον یونانی‌اند نه واژه‌های موروثی: neuron همان نورونِ یونانی است که والدایر در ۱۸۹۱ برای «یاختهٔ عصبی» به کار برد و از دههٔ ۱۸۹۰ در انگلیسی رایج شد، و neurology از لاتینِ نو neurologia (توماس ویلیس، Cerebri anatome، ۱۶۶۴) از neuro- و -logia ساخته شده است. پیشوندِ ترکیبی -neuro (پیش از واکه neur-) به گفتهٔ کلاین همان «νευρο-، νευρ- از νεῦρον» است. پس پیکانِ «یونانی ← انگلیسی» در اینجا وام‌گیریِ واژگانِ علمی است نه تحول آوایی موروثی؛ ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. (s)neu- (AHD_watkins1985.txt line 968) lists the English derivatives of Greek neuron as 'NEURO-, NEURON; APONEUROSIS'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p.1032 s.v. neuro- (KLN_1966.txt line 25321)\", \"stance\": \"supports\", \"note\": \"'neuro-, before a vowel neur-, combining form meaning pertaining to a nerve or nerves. — Fr. Gk. νευρον, sinew, tendon; cord, bowstring, nerve; strength, vigor, which stands for *sneurom and is cogn. with L. nervus'; the neighbouring entry derives 'neuritis' as 'Medical L., formed with suff. -itis fr. Gk. νεῦρον'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and root entry\", \"stance\": \"supports\", \"note\": \"NEURON and NEURO- are listed as English reflexes of the Greek branch of (s)neu-.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-428.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-428.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-428.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 428",
 "description": "Write and validate page-428.json"
}
```


### [2026-09-14T01:37:22.551Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 15/15
node verdicts: {'confirmed': 12, 'plausible': 1, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'plausible': 2}
ref checks: {'supports': 11, 'not_checked': 5, 'partial': 2}
books consulted: {'supports': 29, 'partial': 6, 'silent': 5, 'contradicts': 2} | by book: {'KLN': 10, 'WLD': 4, 'AHD': 4, 'AKD': 3, 'FVQ': 3, 'MON': 3, 'LKT': 3, 'BQT': 2, 'BRT': 2, 'HUB': 2, 'LAT': 2, 'ARY': 1, 'AFM': 1, 'PHD': 1, 'IEC': 1}
```


## [2026-09-14T01:37:28.204Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"snavar\" PHD.txt PHD_mackenzie.txt; grep -n \"sn'wl\\|snʾwl\\|snwl\" PHD.txt PHD_mackenzie.txt | head -5; echo \"(exit $?)\"",
 "description": "Verify MacKenzie has no snavar"
}
```


### [2026-09-14T01:37:29.374Z] TOOL RESULT

```
PHD_mackenzie.txt:0
PHD.txt:0
PHD_mackenzie.txt:4492:sanwar [snwl = Av. 8anwar-] bow.
PHD.txt:564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
(exit 0)
```


## [2026-09-14T01:37:39.135Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\np=\"data/verification/page-428.json\"\nd=json.load(open(p,encoding=\"utf-8\"))\ne=[x for x in d[\"entries\"] if x[\"entry\"]==5][0]\nn=[x for x in e[\"nodes\"] if x[\"id\"]==2][0]\nfor c in n[\"consulted\"]:\n    if c[\"src\"]==\"PHD\":\n        c[\"note\"]=(\"MacKenzie's Concise Pahlavi Dictionary has no headword snavar (grep 'snavar' in PHD.txt and \"\n                   \"PHD_mackenzie.txt: 0 hits). What it does have, p.74, is 'sanwar [snwl = Av. ϑanwar-] bow' — \"\n                   \"the very homograph Horn warns about ('auch für aw. ϑanvar'), since Book-Pahlavi <snwl> can be \"\n                   \"read both ways. So the only Pahlavi word actually spelt this way means 'bow', not 'sinew/cord'.\")\njson.dump(d, open(p,\"w\",encoding=\"utf-8\"), ensure_ascii=False, indent=2)\nopen(p,\"a\",encoding=\"utf-8\").write(\"\\n\")\nprint(\"patched\")\nPYEOF\npython3 -m json.tool data/verification/page-428.json > /dev/null && python3 tools/verify_check.py 428",
 "description": "Patch PHD note and re-validate"
}
```


### [2026-09-14T01:37:40.394Z] TOOL RESULT

```
patched
nodes verified: 15/15
node verdicts: {'confirmed': 12, 'plausible': 1, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'plausible': 2}
ref checks: {'supports': 11, 'not_checked': 5, 'partial': 2}
books consulted: {'supports': 29, 'partial': 6, 'silent': 5, 'contradicts': 2} | by book: {'KLN': 10, 'WLD': 4, 'AHD': 4, 'AKD': 3, 'FVQ': 3, 'MON': 3, 'LKT': 3, 'BQT': 2, 'BRT': 2, 'HUB': 2, 'LAT': 2, 'ARY': 1, 'AFM': 1, 'PHD': 1, 'IEC': 1}
```


## [2026-09-14T01:37:59.711Z] AGENT

Page 428 (book 398) verified — `data/verification/page-428.json`, `verify_check.py 428` shows 0 PROBLEM lines.

**Counts:** 2 non-redirect entries (4 redirects skipped), 15 nodes — confirmed 12, plausible 1, disputed 1, transcription_suspect 1; both roots `plausible`. Ref checks: 11 supports / 2 partial / 5 not_checked. 15 books consulted.

**Flagged items**
- ROOT *Šabatu* (plausible): Nourai's box is Mo'in's BQT p.1300 footnote verbatim (which itself cites Zimmern AKD p.67). But Zimmern on that page says `akk. šabattu, auch (sekundär) šapattu (Etym. noch unklar), 15. Tag des Monats, Vollmondstag` — a noun for the full-moon day with *unclear* etymology, not a verb "to cut, stop working"; modern Assyriology separates šabātu "to beat, blow" and doubts the Akkadian–Hebrew equation.
- #6 Arabic `s.b.t` (**disputed**): Jeffery FVQ 160–161 — "the word came into Arabic from Aram., and probably from the Jewish שבתא … The verb sabata is then denominative (Fraenkel)". So Arabic *al-sabt* is an Aramaic loan, not a second branch descending from Akkadian.
- #2 Persian `snavar` (**transcription_suspect**, error_in = **extraction**): the printed page shows **«سنَوَر»** (fatḥa on ن and و, no šadda); the JSON has **«سَنَّور»**, which spells *sannawr* = Arabic "cat". Owner fix needed. Substantively the node is also wrong-headed: Horn no. 180, p. 291 is in his appendix *Verlorenes Sprachgut*, glosses it 'Sehne' (not "cord, band"), calls it Pahlavi attested only in the Avesta commentary and "vielleicht nur Transcription"; Hübschmann p. 253–4: "phl. snavar ist nur Umschreibung des Zendwortes". MacKenzie has no such word (only `sanwar [snwl = Av. ϑanwar-] bow`).
- #2 Persian شنبه (plausible): real chain is Man. MP *šambat* → *šambad* → شنبذ → شنبه, borrowed from an **Aramaic** form (the intrusive -n-, cf. Eth. *sanbat*, Fr. *samedi*), not straight from Hebrew as drawn.
- ROOT *Sâi 2 … Sneu* (plausible): the box silently merges two Pokorny roots — *sneu-* p. 977 (Av./Gk./Lat. branches) and *sē(i)-* p. 891 (the Germanic *sinew* branch). WLD II 696 says it outright: "Dagegen ahd. senawa, ags. sinu, aisl. sin 'Sehne' zu sē(i)- 'binden'". Both of Nourai's refs check out for their respective halves (KLN:1448 is exactly the *sinew* entry; POK:977 exactly the *sneu-* lemma).

**Extraction errors for the owner:** one — entry 5 node #2 Persian script «سَنَّور» should be «سنَوَر» per the print.

Notes: saved Mo'in's full BQT p. 1300 footnote to `…/refs/ocr/BQT/1300.vision.txt`; page image copied to `…/refs/ocr/BOOK/428.jpg`; 9 web pages archived via `fetch_source.py`.
