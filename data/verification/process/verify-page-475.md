# Verification process log — verify-page-475


## [2026-09-14T02:28:12.641Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 475 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-475.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-475.json. Write /home/sfmqrb/git/rishe/data/verification/page-475.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 475` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:28:13.646Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:28:14.483Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:28:14.499Z] TOOL RESULT

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


## [2026-09-14T02:28:14.978Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-475.txt"
}
```


### [2026-09-14T02:28:14.999Z] TOOL RESULT

```
1	=== PDF page 475 (book page 445) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Stâ, Stha, Stâk : to stand  (refs POK:1008,1009)  PART 2
4	#1 (parent #0) [Latin] refs=AHD | stabulum : standing place
5	  #2 (parent #1) [Arabic] refs=MON | 
6	    #3 (parent #2) [Persian] refs=MON:266 | establ «اسطبل» : stable
7	  #4 (parent #1) [English] refs=AHD | stable 1 : horse shelter
8	#5 (parent #0) [Germanic] refs=None | standan : to stand
9	  #6 (parent #5) [French] refs=AHD:1257 | estandard : (a flag), standing firmly ☞Kar 1
10	    #7 (parent #6) [Persian] refs=MON:239 | estândârd «استاندارد» : standard, a hard standing rule"
11	    #8 (parent #6) [English] refs=AHD | standard
12	  #9 (parent #5) [English] refs=AHD | stand, station, steel
13	#10 (parent #0) [Latin] refs=AHD | 
14	  #11 (parent #10) [English] refs=AHD | constant, cost, distance, exit, instant, substance, store, resist, statistics, system ; stable 2 : steady
15	--- entry 1 ---
16	ROOT [Indo-European] Stâi 1, Tâi : to steal  (refs POK:1010)
17	#1 (parent #0) [Old Persian] refs=FFD:59 | stan, sta 3 : to steal
18	  #2 (parent #1) [Persian] refs=HRN:157; BQT; FFD:59 | setâdan «ستادن ( استدن ، ستدن )» : to grab, steal
19	#3 (parent #0) [Avestan] refs=POK:1010 | tâyu : thief
20	  #4 (parent #3) [Sogdian] refs=SOD:384 | t`y : thief
21	#5 (parent #0) [Sanskrit] refs=POK:1010; SYN:790 | stena, sta : to steal, grab ; stâyu, tâyu : thief
22	--- entry 2 ---
23	ROOT Stâi 2 -> redirect to Stei
24	--- entry 3 ---
25	ROOT Stâk -> redirect to Stâ
26	
```


## [2026-09-14T02:28:16.403Z] AGENT

I'll read the source JSON and the reference index.


## [2026-09-14T02:28:17.797Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-475.json",
 "description": "Read source JSON page 475"
}
```


### [2026-09-14T02:28:17.842Z] TOOL RESULT

```
{
  "pdf_page": 475,
  "book_page": 445,
  "entries": [
    {
      "root": {
        "name": "Stâ, Stha, Stâk",
        "lang": "Indo-European",
        "refs": "POK:1008,1009",
        "gloss": "to stand"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "stabulum", "gloss": "standing place", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "MON",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:266",
          "words": [
            {"translit": "establ", "gloss": "stable", "script": "اسطبل"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "stable 1", "gloss": "horse shelter", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": null,
          "words": [
            {"translit": "standan", "gloss": "to stand", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": "AHD:1257",
          "words": [
            {"translit": "estandard", "gloss": "(a flag), standing firmly", "script": null, "see": ["Kar 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:239",
          "words": [
            {"translit": "estândârd", "gloss": "standard, a hard standing rule\"", "script": "استاندارد"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "standard", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "stand, station, steel", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "constant, cost, distance, exit, instant, substance, store, resist, statistics, system", "gloss": null, "script": null},
            {"translit": "stable 2", "gloss": "steady", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Stâi 1, Tâi",
        "lang": "Indo-European",
        "refs": "POK:1010",
        "gloss": "to steal"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "FFD:59",
          "words": [
            {"translit": "stan, sta 3", "gloss": "to steal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:157; BQT; FFD:59",
          "words": [
            {"translit": "setâdan", "gloss": "to grab, steal", "script": "ستادن ( استدن ، ستدن )"}
          ],
          "note": null,
          "quote": {
            "text": "چنین گفت کاین را نشاید سِتَد - بد آمد به روی من از راه بـد",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1010",
          "words": [
            {"translit": "tâyu", "gloss": "thief", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Sogdian",
          "refs": "SOD:384",
          "words": [
            {"translit": "t`y", "gloss": "thief", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:1010; SYN:790",
          "words": [
            {"translit": "stena, sta", "gloss": "to steal, grab", "script": null},
            {"translit": "stâyu, tâyu", "gloss": "thief", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Stâi 2", "redirect": "Stei"},
      "nodes": []
    },
    {
      "root": {"name": "Stâk", "redirect": "Stâ"},
      "nodes": []
    }
  ]
}
```


## [2026-09-14T02:28:20.307Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','MON','HRN','BQT','FFD','SOD','SYN','WLD','IEC','KLN','PHD','NYB','BRT','KNT','HUB','CHEUNG','ARY','SKT','PLA','AFM','FVQ','LKT','WEB','FSD']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:400])\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-14T02:28:21.689Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-09-14T02:28:24.968Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -60 data/verification/page-385.json && echo --- && sed -n '1,80p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T02:28:25.039Z] TOOL RESULT

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
{
  "pdf_page": 385,
  "book_page": 355,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-07",
  "entries": [
    {
      "entry": 0,
      "root": "Peg",
      "verdict": "plausible",
      "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
      "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
      "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
      "sources": [
        "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
        "https://en.wiktionary.org/wiki/pectus"
      ],
      "ref_check": [
        {
          "ref": "POK:792",
          "status": "partial",
          "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. peg-",
          "stance": "supports",
          "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
          "stance": "partial",
          "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
        },
        {
          "src": "IEC",
          "where": "Mann, alphabetical",
          "stance": "silent",
          "note": "grep of IEC.txt for 'peg-', 'pokso-', 'pektos' returns no headword for this root."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Sanskrit",
          "words": "pakša",
          "verdict": "plausible",
          "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
          "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
          "sources": [
            "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
          ],
          "ref_check": [
            {
              "ref": "AHD",
              "status": "partial",
              "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
---
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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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
```


## [2026-09-14T02:28:29.134Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK offsets ===\"\npython3 - <<'EOF'\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['POK'],ensure_ascii=False,indent=1))\nEOF"
}
```


### [2026-09-14T02:28:30.191Z] TOOL RESULT

```
=== POK offsets ===
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
```


## [2026-09-14T02:28:30.202Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"stā-\" POK_full.txt | head -40; echo \"=== stai ===\"; grep -n \"stāi-\\|stāy\\|tāyú\\|tāyu\" POK_full.txt | head -40"
}
```


### [2026-09-14T02:28:30.274Z] TOOL RESULT

```
=== stai ===
```


## [2026-09-14T02:28:32.506Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la POK_*; echo ===; head -30 POK_full.txt"
}
```


### [2026-09-14T02:28:32.554Z] TOOL RESULT

```
Exit code 1
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
(eval):1: == not found
```


## [2026-09-14T02:28:34.652Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -40 POK_full.txt; echo \"-----\"; grep -n \"Page(s): 1008\\|Page(s): 1009\\|Page(s): 1010\" POK_full.txt | head"
}
```


### [2026-09-14T02:28:34.722Z] TOOL RESULT

```
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 
-----
80984:Page(s): 1010 
80996:Page(s): 1010 
81042:Page(s): 1010-1011
```


## [2026-09-14T02:28:36.529Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '80930,81060p' POK_full.txt"
}
```


### [2026-09-14T02:28:36.591Z] TOOL RESULT

```
Lithuanian strenos^6\e loins, the cross'. 

References: WP. II 705. 

Page(s): 1 002 

Root / lemma: sng-, sngos- 

Meaning: cold, frost 

Material: Gr. pTyoc; n. "frost', pTvEU), Perf. m. present-meaning sppTva " freeze, shudder, 

erschauern'; plYcbcjo "friere'; 

Latin fngus, -or/'sn. (= gr. pTyoc;) "coldness, frost', fnged, -ere'co\d sein, freeze, gefroren 
sein', fng/dus ^co\d'. 

References: WP. II 705 f.; after WH. I 547, II 434, zero grade from *{s)re/g-, to Latin riged' 
rigid', r/gor^ solidification (vor coldness)', Lithuanian re/zt/s ' s\c\r\ strecken' (different above 
S. 855, 862.) 
Page(s): 1 004 

Root / lemma: sromo- 

Meaning: lame 

Note: only altindisch and slavisch 

Material: Old Indie 5/'a/77a-"lame', srama-m. "Lahmheif; Old Church Slavic (etc.) chromb 

"lame'. 

References: WP. II 706; Machek Slavia 16, 191, IF. 53, 94; Vasmer3, 272 f. 

Page(s): 1 004 

Root / lemma: stag- 
Meaning: to drop, drizzle 

Material: Gr. ara^u), aTa^w GTaynvai "drip, trickle, eintraufein tr., drip, trickle let; drip, trickle 
intr., rinnen', araKToq "tropfeind, tropfend', araycbv, -6vo(;f. "drip', omyzq PI. ds.; 

Latin stagnum^]e6es ausgetretene Gewasser, sea, pond, pool, pond, pool or langsam 
running Gewasser'; 



Latin (Celtic loanword?) stagnum'Z\nn' ("das Getropfte, light Schmelzbare'), Old Irish 
Stan 'Z\nn'; cymr. ystaen, ncorn. stean, bret. stean {irovc\ Latin?); 

abret. staer, nbret. s/e^'river, stream, brook' {*stagra), cymr. /ae/7"conspersio, 
adspersio' {*stagna). 

References: WP. II 612, WH. II 585, Flasdieck Zinn under Zink 14 ff. 
Page(s): 1010 

Root / lemma: (s)tai- 
Meaning: to conceal; to steal 

Material: Old Indie stayat^ clanoestine, hide, conceal', stay'u-, tay'u- "thief (= Old Church 
Slavic /ay Adv. 'secret ', if from *tajLr, gr. Tr|u-aiO(;); steya-m^ theft ', stena- 'thief; Avestan 
tayu- 'thief, taya- ' theft '; gr. rriuairi 656c; 'ein way, the einen um die MiJhe the intention 
betrugt' (*tc(u-tio(;, from *tc(ju-tc(), Tniri arropia, £v5£ia, GTspnaK; Hes., rriTau) 'bringe um 
etwas, rob', Med. 'darbe'; Old Irish /a/io''thief (= Old Bulgarian tatb, das -o'analogical); Old 
Church Slavic /ay" secret ', tajQ, tajiti^ hide ', tatb 'thief; Hittite tajezzi, /ayazz/'stiehit'. 
References: WP. II 610, Trautmann 313, Vasmer 3, 69. 
Page(s): 1010 

Root / lemma: stai-, sff- sti-a- 

Meaning: to condense, press together 

Note: in addition steib(h)-, steip-^ shaft, pole etc' 

Material: Old Indie s/yaya/e'gerinnt, wird hart', participle styana-; (Gramm.) prastJma- 

'gedrangt, gehauft', s//777a-'idle' (actually ' jammed, packed, stuck '), vistTmfn- Bez. of 

pudenda, stfyai. 'trages, stehendes water', stimita- ' clumsy, idle, unbeweglich, damp'; 

Avestan sta{}/)- 'heap, mass'; 

gr. GTsap, oitaioQ, 'stehendes fat, tallow, suet' {*stajj)\ hom. ayxi-aiTvoq ' near 
aneinandergedrangt' (compare Old Indie stya-na-); afia f., gtTov n. ' small stone '; oY\kr\ 
'drip' (compare Latin stfr/'a, stTlla); 

Latin s//?/a 'frozen drip, icicle', Demin. s//7/a'drip' {*stTr[e]la); 

nisi. 5//?^/" 'stiffness in the eyes', Norwegian stTra, Old Icelandic stira, Danish Swedish 
stirra^Qaze, stare'. East Frisian s//?' stiff, rigid'. Modern High German stier, stieren, 
Lithuanian styrstu, styrti' solidify, congeal ', styrau, -oti^ stiff and lijmmelhaft dastehen'; 



Old Icelandic stfmn. " restlessness, din, fuss, noise', Norwegian 5//777Tischschwarnn', 
Middle High German st/m, ste/m ^bunte bulk, mass, Getummel'; 

Gothic stains. Old Icelandic steinn. Old English stan. Old High German stein ' stone '; 

Old Church Slavic stena'\Na\\', stentnh " stony '; 

perhaps also Old Icelandic s//"n. "stall', stTa' make a hedge, fence ', Old English stig, stT 
" pigpen; hall'. Middle Low German s/ege "corral, pen, fold'. Old High German stTga, Middle 
High German stTge, 5/ye "stall or Lattenverschlag for small cattle'; 

Lithuanian stlngtr curdle, coagulate, harden ', Latvian stingt^ compact become', stingrs 
"stramm, rigid, zusammenhaltend, gespannt, stiff; 

about Latin ///77ed "dread myself, etc. s. WH. II 682. 

References: WP. II 610 f., WH. II 595; 
See also: s. also steya-S. 1035. 
Page(s): 1010-1011 

Root / lemma: stak-, stek- 

Meaning: to stand; to put 

Note: extension from 5/5- "stand' 

Material: Old Indie s/5/ra// "widerstehf, Avestan staxta- "tight, firm, strong', staxra- "strong, 

tight, firm; esp. of Winterfrost: stern'; Umbrian s/a/raz "statutus'; 

Old High German stafialu. m. Old Icelandic stalu. (derived Old High German stefili. Old 
English stieien.) "Stahl' (from dem Germanic derives Old Prussian stac/an 'StahV), 
Germanic *5/a/7/a- probably = Avestan staxra-, Indo Germanic *stdicio-. Old Icelandic stagi 
n. "wheel, das zur Hinrichtung dient', Norwegian s/a^/e "picket, pole', staga' stiff go'. Old 
Icelandic stagn.. Old English staegu. "rope, hawser' ('*das steif gespannte'); 

with other meaning change ("stehenbleiben = stocken, to short become') Old Icelandic
```


## [2026-09-14T02:28:42.821Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Root / lemma: st\" POK_full.txt | sed -n '1,80p'"
}
```


### [2026-09-14T02:28:42.881Z] TOOL RESULT

```
80966:Root / lemma: stag- 
80998:Root / lemma: stai-, sff- sti-a- 
81044:Root / lemma: stak-, stek- 
81069:Root / lemma: sta- : sta- 
81277:animal)', s^/ze 'kill (an animal)'. Alb. suggests that Root / lemma: sta-. sta-\ (to stand) 
81374:Root / lemma: steb(hj- and steb(h)-. stdo"^-, nasalized stemb(h)-, step- {a\so step-?), 
81479:Root / lemma: stegh-, nasal, stengh- 
81594:Root / lemma: steigh- 
81779:Root / lemma: stel-2, stela- 
81800:Root / lemma: stel-3 
81919:Root / lemma: stem- 
81980:Root / lemma: sten-2 
81998:Root / lemma: sterg-, sterk- 
82496:Root / lemma: ster-3 
82508:Root / lemma: ster-4 
82599:Root / lemma: ster-5, stera- : stre-, steru- : streu- 
82687:Root / lemma: ster-6 
82919:Root / lemma: steu-2 
82936:Root / lemma: steue- 
82959:Root / lemma: steib(h)-, sffb(h)-, steip- sffp- 
83007:Root / lemma: ster-2 
83063:Root / lemma: stilp-, stilb- ? 
83077:Root / lemma: stomen- 
83094:Root / lemma: stores, stornos {stfno^) 
83110:Root / lemma: streig-1 
83132:Root / lemma: streig-2 
83167:Root / lemma: strenk-, streng- 
83232:Root / lemma: stru-
```


## [2026-09-14T02:28:44.767Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '81044,81120p' POK_full.txt; echo \".....\"; sed -n '81240,81290p' POK_full.txt"
}
```


### [2026-09-14T02:28:44.849Z] TOOL RESULT

```
Root / lemma: stak-, stek- 

Meaning: to stand; to put 

Note: extension from 5/5- "stand' 

Material: Old Indie s/5/ra// "widerstehf, Avestan staxta- "tight, firm, strong', staxra- "strong, 

tight, firm; esp. of Winterfrost: stern'; Umbrian s/a/raz "statutus'; 

Old High German stafialu. m. Old Icelandic stalu. (derived Old High German stefili. Old 
English stieien.) "Stahl' (from dem Germanic derives Old Prussian stac/an 'StahV), 
Germanic *5/a/7/a- probably = Avestan staxra-, Indo Germanic *stdicio-. Old Icelandic stagi 
n. "wheel, das zur Hinrichtung dient', Norwegian s/a^/e "picket, pole', staga' stiff go'. Old 
Icelandic stagn.. Old English staegu. "rope, hawser' ('*das steif gespannte'); 

with other meaning change ("stehenbleiben = stocken, to short become') Old Icelandic 
stakicai. " stub', stal<kadr, stgkuttr^ short', Danish stak-aandet^kurzatmg'; Lithuanian stoka 
"lack', stokstu, stokti^ to lack begin'. 

References: WP. II 611, WH. II 585. 
Page(s):1011 



Root / lemma: sta- : sta- 

Meaning: to stand 

Note: reduplicated s/'-sta- extended stai-. sff-, stau-. s/itz-and st-eu- 

Material: A. Old Indie tisthati, Avestan histaiti, ap. 3. Sg. Impf. a-/5/a/a"stehn' (: Latin sisto, 

Irish -sissiur, athematic still gr. TaTr||Ji, during late Old High German ses/d/7'disponere' 

from dem roman. Italian assestare^ bring in order' borrowed is), Aor. Old Indie a-stha-m 

(= gr. EGTriv), Perf. tasthau, tasthima, tasthivas-, gr. TaTr||Ji (Doric ToTapi) "stelle', Aor. eotpiv, 

Perf. EorriKa, 'iaia\xzy, saraux; (sni-OTapai ' understand ' probably neologism after Aor. 

eTTi-aTai|jr|v, £ni-aTap£vo(;); iaroq " mast, the senkrechte Weberbaum, texture '; 

Avestan ap. staya-' place; Med. sich stellen'; 

Latin 5/5/0 "stelle', Umbrian sestu ' s'\st6' , Volscan 5/5//^//e/75"statuerunt'; 

Old Irish ta/r-{s)/ss/ur' stay, stand', 5/'-5/55eo'a/''insistitur, innititur', /b-5/55eo'5/' " tritt ein 
for' (5e'55a/77'das Stehen', sessedds. etc.); 

Latin sto {stare, stetl) = Umbrian sfahu' stand ', *sfa-/d; Old Latin probably also trans. ' 
place '; Oscan staft{*stajeieti) 'stat' PI. stahfnt, eestfnt {*estajejent} 'extant'; Old Irish ad- 
tau, -/o'l befinde myself, bin' {*sta-jd), 3. Sg. (ad)-ta= cymr. /an/'daft es is' from *sta-t, 
unpersonl. Passiv tathar'man is (mad, wicked, evil)'from *sta-fo-ro{7), mcymr. 
Impersonale ny-m-dawr'es kijmmert myself nicht', corn, ny-m-deur {*ta-ro-) "I will not'; Old 
Irish ness- {*ni-sta-) 'niedertreten' in com-ness-6s., 'verurteilen', dhness^ despise ', to- 
ness- "betreten', ar-ossa " expect t' {*are-uks-sta-)\ assae "light to tun' from *ad-sta-io- 
"adponendus'; 

Note: 

Maybe alb. 5/a/7 'winter station for animals' from med.L stantiat L stant-pres. ppl stem of 
stare to stand. 

Old Saxon Old High German 5/5/7, 5/e/7 "stand'; Reimwortbildungen to gen, ^5/7 "go' 
(see 419); with /-extension: preterit Gothic sfof^. Old Icelandic stod. Old Saxon sfod. Old 
High German 5/^c»/(mostly 5/^0/7/ after dem present) "I stand', wherefore with present 
nasalization Gothic Old Saxon standan. Old Icelandic standa. Old English stondan. Old 
High German 5/5/7/3/7 "stand'; in addition Old High German stanta^ bowl, basin, Kufe' and 
with neuem ablaut Old Icelandic 5/^/70' "time(punkt), while, hour, length'. Old English stund 
f. " certain time, hour, Mai', Old Saxon 5/^/70^5 "time(punkt)'. Old High German sfunfads.. 
Late Middle High German also "hour'; 



Lithuanian st6Ju{* staid), stot/' tread', Old Cliurcli Slavic *stajg, stat/"s\ch stellen', stq/'g 
stojati {* stajeti) 'stand'; Tocharian B 5/e"is', 3. PI. stare. 
.....
unbeweglich, stiff, zugewogen', araSriv 'stehend', ano-araSov 'fern abstehend'. 



9. with /-formant: 

cymr. cystar just as well ' ( *kom-sta-lo-)\ Gothic stols "throne', Old High German stuol. 
Old English stol. Old Norse s/o/Z'stool', Lithuanian pastolai^ rack for Bienenkorbe', zero 
grade Old Church Slavic s/o/b 'throne, seat', in den neuern Slavic Spr. "stool' or 'table, 
desk'. 

Alb. stor stool' a Slavic loanword. 

10. with /7^fornnant: 

Old Indie sthaman-v\. "Standort, power'; gr. aTri|ju)v m., arripsvai "stand', Latin stamen 
n. "Aufzug am aufrecht stehenden loom, etc.', Umbrian Dat. 5/a/7/77e/"stationi'; stahmito 
"statutum'; Old Irish sessam'das Stehen' {*si-sta-mu-), foessam^ protection' {*upo-si-sta- 
mu-) = mcymr. ^M/5ess5M/"Garantie'; Gothic stoma ^UTTdoiao\q, foundation, Stoff'; 
Lithuanian stomud, -ens^ stature '; russ. s/a/77//^"Stutzbalken'; 

gr. GTapvoc; "crock, pitcher', arapTv-sq PI. "Stander, Seitenbalken'; cymr. cyse/^/7 "first' 
{*kentu-stamTno-)\ Middle Irish s5/775/^//77"stelle', cymr. sefyll, corn, sei/e// "stand', bret. 
sevell{ *stamilio-) "erect, to build' (besides with Celtic /Old Irish tamun^tree truck'; Old 
High German stam, stammes 'stem'etc. seems Verquikkung eines related *stamna- \N\t\r\ a 
stabna-, s. *steb- " jamb '); Tocharian A stam, B stam "tree'; but Old High German 
ungistuomi' boisterous ' to stem- "hamper', see there. 

1 1 . with /^formant (compare die Prasensbildungen with n): 

Old Indie sthana-v\., Avestan ap. stana-n. "Standort, place', npers. s/tan, gr. 5ua- 
[a]Tr|vo(;, Doric buomvoq "(in schlechtem Zustande) unlucky ', aaTr|vo(; ds., Lithuanian 
s/d/7as "Stand', Old Church Slavic 5/5/7b "Stand, lair', alb. sMuare ' ste\r\en6' , shtoraze 
"erect' ( *sta-no-dio-, compare to o'-suffix gr. anoaraSov etc.), shtaze, shteze ' catt\e' ( *stan- 
ze). 

Maybe alb. s/a/7 'animal stall', {* status), s/7/5/ 'standing body', s/7/j7''push (pushing 
animal)', s^/ze 'kill (an animal)'. Alb. suggests that Root / lemma: sta-. sta-\ (to stand) 
derived from Root / lemma: sed- : (to sit). 

12. with /•-formants: Old Indie sth/ra-'t\g\r\t, firm, unbeweglich'; Lithuanian s/d^as "thick, 
umfangreich' (actually "stammig'). Old Church Slavic starh "old' ("*stammig' in contrast zur 
zarteren youth). Old Norse stdrr'b'\g, large'. Old Saxon 5/d/7"big, large, illustrious'. Old 
English stor's/ast, grand'; 



13. with demy'from *s/a;/o other formations: Old \v\6\c Jala-sthaya-xw. " water container, 
water carrier ', s//7a>7/7-'stille stehend, verweilend, stetig' , sfheman-m. Testigkeit, 
tranquility, duration' {*sf hay/man-).
```


## [2026-09-14T02:28:49.656Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=81069 && NR<=81380 && (/Page\\(s\\)/ || /stabulum/ || /standard/ || /References:/)' POK_full.txt"
}
```


### [2026-09-14T02:28:51.026Z] TOOL RESULT

```
References: WP. II 603 ff., WH. I 343 f., 705 f., Trautmann 280 ff., Vasmer 3, 2 ff. 
Page(s): 1004-1010
```


## [2026-09-14T02:28:55.233Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"stabulum\\|stabul\" POK_03.txt | head -20; echo \"=== which leaf ===\"; python3 - <<'EOF'\ndata=open('POK_03.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(data):\n    if 'stabul' in p:\n        print('leaf',i)\nEOF"
}
```


### [2026-09-14T02:28:56.320Z] TOOL RESULT

```
3376:8.  mit  Formans  -dblo-:  lat.  stahulum  ,Standort,  Aufenthalt;  Lager  wilder Tiere,  Stall'  (pröstihulum  ,Ding  zum  öffentlich  Ausstehen,  Dirne',  nausti- bulum  , Schiffstandort,  Gefäß  in  Schiffsform'),  stahilis  ,f eststehend,  stand- haft', umbr.  staßarem  ,stabulärem',  osk.  staflatas-set  ,statutae  sunt*,  pälign. pri-stafalacirix  ,*praestibulätrix,  antistita* ;
=== which leaf ===
leaf 248
```


## [2026-09-14T02:28:59.231Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ndata=open('POK_03.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=data[248]\nprint(p[:300])\nprint('...TAIL...')\nprint(p[-300:])\nEOF"
}
```


### [2026-09-14T02:29:00.428Z] TOOL RESULT

```
tandort,  Herde  von  Stuten  mit  einem  oder  mehreren ^engsten',  ags.  stöd  n.  ,Pferdeherde',  mnd.  stöt  (-d-)  f.  , Einzäunung  für Pferde,  Herde  von  Zuchtpferden',  ahd.  stuot  f.  , Herde  von  Zuchtpferden', auch  , Stute',  nhd.  Stute-,  aisl.  (z.  B.  hug-)  stMr  ,feststehend, 
...TAIL...
ls  ,Thron',  ahd.  stuoly ags.  stöl,  anord.  stöll  ,Stuhl*,  lit.  pastölai  , Gestell  für  Bienenkörbe',  tief- stufig aksl.  stoh  , Thron,  Sitz',  in  den  neuern  slav.  Spr.  ,Stuhl'  oder  ,Tisch'.
10.  mit  122-Formantien : ai.  sthäman-  n.  , Standort,  Kraft*;  gr.  ari^fiwv  m.,  aT
```


## [2026-09-14T02:29:08.388Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndata=open('POK_03.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(238,256):\n    t=data[i]\n    # find standalone 4-digit numbers 1000-1020\n    nums=re.findall(r'\\b10[0-2]\\d\\b',t)\n    print(i, nums[:6], repr(t[:70]))\nEOF"
}
```


### [2026-09-14T02:29:09.522Z] TOOL RESULT

```
238 [] "�,  -ere  ,streuen,  hinstreuen,  sprengen,  spritzen' ;\nmnd.  sparJce"
239 [] '  ,Regenwolke  (spritzend, sprengend);  der  Regen-  und  Gewittergott'
240 [] "Geschäft'  {*pudnä)'j  ^\nfalls  ^-Erweiterung  einer  Wurzel  speu- : "
241 ['1000'] 'spyja^  ags.  as.    ahd.   splwan  , speien*,    aisl.    spyta   , s'
242 ['1001'] 'da.\nWP.  II  684.\n(s)pleigh-  ,die  Beine  spreizen*.\nAi.  *pUhate  ,g'
243 ['1002', '1003'] " iniQQO&og  (und  iniTdgQo&og)\n1002  '\n, herbeisausend;  auch  von   G"
244 ['1004'] "  Flüsse',  urvant-{sru-vant-)  ^fließend' ; von  einem  (^(Ä)-Präs.  "
245 ['1005'] "tgeö,  -ere  ,kaltlieii^ frieren,  gefroren  sein',  frlgidus  ,kalt'."
246 ['1006'] "  Ablaut  aisl.  stund  ,Zeit(punkt), Weile,  Stunde,  Länge',  ags.  "
247 ['1007'] '.  *sf[9]^i-s  mit  in  der  Komposition  geschwundenem  a  sind  hin*'
248 [] "tandort,  Herde  von  Stuten  mit  einem  oder  mehreren ^engsten',  a"
249 ['1008'] "rjiLsvai  ,stehen',  lat.\nstämen   n.    , Aufzug   am  aufrecht   ste"
250 ['1009'] "Med.  ,bin  steil  aufgerichtet',  atvi^a  n. ^erectio  penis',  orv^i"
251 ['1010'] "tützen,  steuern,  lenken';  wohl  ursprüngl.  , Pfahl, Steuerruder  ("
252 [] "es  Fett,  Talg'  (^stäif)]  hom.  dyxi-azlvog  DaJ># aneinandergedrän"
253 ['1012'] "l'  (=  lit.  stdmbas I   .Kohlstrunk');     .\ngr.  ar£i.ißü)  ,stampf"
254 ['1013'] '.    *stafs   (Nom.    PL    stabeis)    atoixsXa    ,Buchstaben*    ('
255 ['1014'] ".  am-do  ,amiculum, ^    involucrum',  air.  etach  , Kleid*,  cymr. "
```


## [2026-09-14T02:30:06.959Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD stā- ===\"; grep -n -A30 \"^stā-\\|^sta-\\. To stand\\|^stā-\\.\" AHD_watkins1985.txt | head -80"
}
```


### [2026-09-14T02:30:07.207Z] TOOL RESULT

```
=== AHD stā- ===
997:sta-. To stand; with derivatives meaning “place or thing that is standing.” Contracted from *stag-. I. Basic form *std-. 1. Extended form *stddh- in: a. Germanic *stéd- J6n- in Old English stéda, stallion, studhorse ( < “place for breeding horses”): STEED; b. Germanic *st6d6 in Old English stéd, establishment for breeding horses: sTuD2. 2. Suffixed form *std-lo- in Germanic *stdlaz in: a. Old English st6/, stool: sTooL; b. compound *faldistélaz (see pel-3). 3. Latin stdre (third person singular present subjunctive séet), to stand, with its past participle status (< “sta-to-) and derivatives statira, height, stature, and statuere, to set up, erect, cause to stand: STAGE, STANCE, STANCH, (STANCHION), (STANZA), STATOR, (STATUE), STATURE, STATUTE, STAY!, STET; ARREST, CIRCUM- STANCE, CONSTANT, CONSTITUTE, CONTRAST, (COST), DESTITUTE, DISTANT, ESTANCIA, EXTANT, INSTANT, IN- STITUTE, OBSTACLE, OBSTETRIC, (OUST), PROSTITUTE, REST?, RESTITUTE, RESTIVE, SUBSTANCE, SUBSTITUTE, SUPERSTITION. 4. Suffixed form *std-men- in Latin std- men, thread of the warp (a technical term): STAMEN, STAMMEL. 5. Suffixed form *std-mon- in Greek stémén, thread: PENSTEMON. 6. Suffixed form “s¢d-ro- in Russian staryi, old (“long-standing”): STARETS. II. Zero-grade form *st- (before consonants). 1. Nasalized extended form *sfa-n-t- in Germanic *standan in: a. Old English standan, to stand: STAND; b. Old English understandan, to know, stand under (under-, under; see ndher): UN- DERSTAND; Cc. Old French estandard, rallying place: STANDARD; d. secondary zero-grade form in Germanic *stund-6 in Old English stund, a fixed time, while: STOUND. 2. Suffixed form *sé-tyo- in Germanic *stath- Jon- in Old Norse stedhi, anvil: strTHY. 3. Suffixed form *sta-tlo- in Germanic *stathlaz in Old English stathol, foundation: STADDLE, STARLING?. 4, Suffixed form *sta-mno- in Germanic *stamniz in Old English stefn, stem, tree trunk: sTeM!. 5. Suffixed form *sta-ti- in: a. Germanic *stadiz in (i) Old English stede, place: STEAD (ii) Dutch stad, place: STADHOLDER (iii) Old High Ger- man stat, place: SHTETL; b. Latin stati6, a standing still: STATION; C. Latin -stitium, a stoppage (in solstitium, solstice; see sawel-): ARMISTICE; d. Greek stasis, a standing, a standstill: sTAsIs; HYPOSTASIS, ICONOSTASIS, IsOSTASY. 6. Suffixed form *sfo-to- in Greek statos, placed, standing: STATIC, STATICE, STATO-; ASTASIA, ASTATINE. 7. Suffixed form “sta-no- in: a. Latin désti-
998-stag-
999-nare, to make firm, establish (dé-, thoroughly; see de-): DESTINE; b. Latin obstindre, to set one’s mind on, persist (ob-, on; see epi): OBSTINATE. 8. Suffixed form *séa-tu- in Latin status, manner, position, condition, attitude: STATE, STATISTICS, STATUS. 9. Suffixed form *sto-dhlo- in Latin stabulum, standing place: STABLE. 10. Suffixed form *si-dhli- in Latin stabilis, standing firm: ESTAB- LISH, STABLE!. 11. Suffixed form *sf-td- in Greek -statés, one that causes to stand, a standing: -sTAT; ENSTATITE. III. Zero-grade form *st-, *st()- (before vowels). 1. Reduplicated form *si-sio)- in: a. Latin sis- tere, to set, place, stop, stand: ASSIST, CONSIST, DESIST, EXIST, INSIST, INTERSTICE, PERSIST, RESIST, SUBSIST; b. Greek histanai (aorist stanai), to set, place: APOSTASY, CATASTASIS, DIASTASIS, ECSTASY, EPISTASIS, EPISTEMOL- OGY, METASTASIS, PROSTATE, SYSTEM; Cc. Greek histos, web, tissue ( < “that which is set up”): HISTO-; HISTIO- cyTE. 2. Compound form *iri-st-i-, “third person stand- ing by” (see trei-). 3. Compound form *por-st-i-, “that which stands before” (*por-, before, forth; see per’), in Latin postis, post: PosT!. 4. Suffixed form *st-o- in compound *upo-st-o-, “one who stands under” (see upo). IV. Extended root *std@u- (< *staau-), becoming *stau- before consonants, *stdw- before vowels; basic meaning “stout-standing, strong.”’ 1. Suffixed extended form *staw-d in Germanic *st6w6 in Old English stéw, place: stow. 2. Probable o-grade suffixed extended form *stow-yad in Greek stoa, porch: STOA, STOIC. 3. Suffixed extended form *stau-ro- in: a. (i) Latin instaurdre, to restore, set upright again (in-, on; see en): STORE; INSTAURATION (ii) Latin restaurdre, to restore, rebuild (re-, anew, again; see re-): RESTORE; b. Greek stauros, cross, post, stake: STAUROLITE. 4. Variant *tau-ro-, bull (see tauro-). V. Zero-grade extended root stii- (< *stua-). Suffixed form “*sti-lo- in Greek stulos, pillar: STYLITE; AMPHISTYLAR, ASTYLAR, EPISTYLE, HYPOSTYLE, PERI- STYLE, PROSTYLE, STYLOBATE. VI. Secondary full-grade form *steua-. Suffixed form *steua-ro- in Sanskrit stha- vira-, thick, stout, old: THERAVADA. VII. Variant zero-grade extended root *stu-. Suffixed form *stu-t- in Old English stuthu, studu, post, prop: STUD'. VIII. Sec- ondary full-grade form *steu-. 1. Suffixed form *steu-raé in Germanic *steur6, “a steering,” in Old English stéor, a steering: STARBOARD. 2. Germanic denominative *steur- Jan in: a. Old English stieran, to steer: STEER}; b. Old Norse styra, to steer, with its derivative stjérn, a rudder, a steering, akin to the possible source of Middle English sterne, stern of a boat: STERN?. 3. Suffixed form *steu-ro-, a larger domestic animal, in Germanic *steu- raz, ox, in Old English stéor, steer: STEER?. 4. Probably Germanic diminutive *steur-ika- in Old English stirc, stierc, calf: sTIRK. See stak-. [Pok. std- 1004.]
1000-stag-. To seep, drip. Possible root. 1. Latin stagnum, pond, swamp: STAGNANT. 2. Suffixed form *stag-yo- in Greek stazein, to ooze, drip: STACTE; EPIsTaxis. [Pok. stag- 1010.]
1001-stak-. To stand, place. Zero-grade form *stak-; extension of sta-. 1. Suffixed form *stok-o- in Germanic *staga- in: a. Old English stzg, rope used to support a mast: sTAY3; b. Old French estaie, a support: STAY?. 2. Suffixed form *stak-lo- in Germanic *stahla- in Old English stéli, style, steel (< “that which stands firm”): STEEL. [Pok. stak- 1011.]
1002-[stam-. To push, stutter, stammer. Germanic root. 1. Old English stamerian, to stammer:. STAMMER. 2. Middle Dutch stom, mute: stum. 3. Old Norse stemma, to stop: STEM?, 4, Old Norse *stumla, stumra, to stumble, akin to the probable Scandinavian source of Middle English stumblen, to stumble: sTUMBLE. [In Pok. stem- 1021.]] [staup-. (Cooking) vessel. Germanic root. 1. Old Norse staup, vessel: stouP. 2. Middle Low German stove, heated chamber: sTOVE!. [In Pok. 1. stew- 1032.]] stebh-. Post, stem; to support, place firmly on, fasten. I. Basic form *stebh-. 1. Germanic *stab- in Old English
1003-65
1004-steigh-
1005-stef, stick, rod: STAFF!. 2. Greek stephein, to tie around, encircle, crown, wreathe: STEMMA, STEPHANOTIS. II. Un- aspirated form *steb-. 1. Germanic *stap- in: a. Old English stapol, post, pillar: sSTAPLE?; b. Old English stzpe, step (< “a treading firmly on, foothold”): sTEP; c. Middle Dutch stapel, pillar, foundation: STAPLE}; d. Middle Dutch stoep, stoop: stoor?; e. Low German stope, a step: STOPE. 2. Germanic nasalized form *stamp- in: a. Middle English stampen, to pound, stamp: STAMP; b. Middle Low German stump, stump: sTuMP; c. Old High German stam, base, stem, in German Stammlager, base camp: STALAG; d. Provencal estampier, to stamp: STAMPEDE. III. Variant *stabh- in Greek staphulé, grape- vine, bunch of grapes: STAPHYLO-. [Pok. steb(h) 1011.]
1006-steg-. Pole, stick. O-grade form *stog- in Germanic *stak- in: a. Old English staca, stake: sTAKE!; b. Old Norse stakkr, haystack: stack; c. Old Norse staka, to push, cause to stumble (as with a stick): STAGGER; d. Old Italian attacare, to attack: ATTACK; e. Old French atta- chier, to attack: ATTACH; f. Spanish estaca, stake: STOCKADE. [Pok. 2. (s)teg- 1014.]
1007-(s)teg-. To cover. I. O-grade form *tog-. 1. Germanic *thakjan in: a. Old English theccan, to cover: THATCH; b. Middle Dutch dekken, to cover: DECK?; c. Old High German decchen, to cover: DECKLE. 2. Germanic *tha- kam in Middle Dutch dec, decke, roof, covering: DECK}. 3. Suffixed form *tog-d-, covering, in Latin toga, toga: TOGA. 4. Possibly Sanskrit sthagayati, he covers: THUG. II. Basic form *steg- in Greek stegein, to cover: STEGODON. III. Basic form *teg-. 1. Latin tegere, to cover, and tegula, tile: TECTRIX, TECTUM, TEGMEN, TEG- MENTUM, TEGULAR, TEGUMENT, TILE, TUILLE; DETECT, INTEGUMENT, OBTECT, PROTECT. 2. Persian fdj, crown: Tad. [Pok. 1. (s)teg- 1013.]
1008-stegh-. To stick, prick; pointed. 1. Nasalized form *stengh- perhaps in Germanic *stingan in Old English stingan, to sting: STING. 2. O-grade form *stogh- in: a. Germanic *stag- in Old English stagga, stag: STAG; b. Greek stokhos, pointed stake or pillar (used as a target for archers), goal: STOCHASTIC. [Pok. stegh- 1014.]
1009-stei-. Stone. Suffixed o-grade form *stoi-no- in Germanic *stainaz in: a. Old English stan, stone: STONE; b. Middle Dutch steen, stone: STEENBOK; C. Old Norse steinn, stone: TUNGSTEN; d. Old High German stein, stone, in German Steingut, stoneware: STEIN. [Pok. stdi- 1010.]
1010-steig-. To stick; pointed. Partly blended with stegh-. I. Zero-grade form *stig-. 1. Germanic suffixed form *stik-ilaz in Old English sticel, a prick, sting: STICKLE- BACK. 2. Suffixed form *stig-i- in Germanic *stikiz in Old English stice, a sting, prick: STITCH. 3. Germanic expres- sive form *stikk6n- in Old English sticca, stick: sTICK. 4. Germanic blended variant *stekan in Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET; SNICKERSNEE. 5. Nasalized form “sti-n-g- in Latin stinguere, to quench, perhaps originally to prick, and its apparent derivative distinguere, to separate (semantic transitions obscure): DISTINGUISH, EXTIN- GUISH, INSTINCT. 6. Suffixed form *stig-yo- in Greek stizein, to prick, tattoo: STIGMA; ASTIGMATISM. 7. Suf- fixed reduced form “*tig-ro- in Old Persian tigra-, sharp, pointed, and Avestan fighri-, arrow, in Greek tigris, tiger (from its stripes): TIGER. II. Basic form *séeig- in Latin -stigdre, to spur on, prod, in instigdre, to urge: INSTI- GATE. III. Suffixed o-grade form *stoig-d- in Germanic *staikd in Old Norse steik, roast, steak, and steikja, to roast (on a spit): STEAK. [Pok. steig- 1016.]
1011-steigh-. To stride, step, rise. I. Basic form *steigh-. 1. Germanic *stigan in Old English stigan, to go up, rise: sty. 2. Germanic compound *stig-raipaz, “mount-rope” (*raipaz, rope; see rei-1), in Old English stigrdp, stirrup: STIRRUP. II. Zero-grade form *stigh-. 1. Germanic *sti- gila- in Old English stigel, series of steps: STILE!. 2. Suf- fixed form *stigh-to- in Germanic *stihtan, “to place on a step or base,” in Old English stiht/i)an, to settle, arrange:
1012-steip-
1013-STICKLE. 3. Suffixed form *stigh-o- in Greek stikhos, row, line, line of verse: STICH; ACROSTIC, CADASTER, DISTICH, HEMISTICH, ORTHOSTICHOUS, STICHOMETRY, STICHO- MYTHIA. III. O-grade form *stoigh-. 1. Suffixed form *stoigh-ri- in Germanic *staigri in Old English stéger, stair, step: STAIR. 2. Greek stoikheion, shadow line, element: STOICHIOMETRY. [Pok. steigh- 1017.] steip-. To stick, compress. 1. Germanic *séifaz in: a. Old English séff, rigid, stiff: stirF; b. Dutch stip, tip, point: STIPPLE. 2. Latin stipes, post, tree trunk: STIPE, STIPES. 3. Suffixed form *steip-d- in Latin stipdre, to compress, stuff, pack: STEEVE!, STEVEDORE; CONSTIPATE. [Pok. stéib(h)- 1015.] stel-. To put, stand; with derivatives referring to a standing object or place. I. Basic form *stel-. 1. Suffixed form *stel-ni- in Germanic “*stilli- in Old English stile, quiet, fixed: sTILL’. 2. Suffixed form “stel-yo- in Greek stellein, to put in order, prepare, send, make compact (with o-grade and zero-grade forms sfol- and stal-): APOSTLE, DIASTOLE, EPISTLE, PERISTALSIS, SYSTALTIC. II. O-grade form *stol-. 1. Suffixed form *sfol-no- in Germanic *stalla- in: a. Old English steall, standing place, stable: STALL; FORESTALL; b. Old French estal, place: INSTALLMENT!; Cc. Old French estalon, stallion: STALLION; d. Old Italian stallo, stall: PEDESTAL; e. Me- dieval Latin stallum, stall: INSTALL; f. Germanic denomi- native *stalljan in Old High German stellen, to set, place: GESTALT. 2. Suffixed form stol-6n- in Latin stolé, branch, shoot: STOLON. 3. Suffixed form *stol-ido- in Latin stoli- dus, “firm-standing,” stupid: sTOLID. 4. Suffixed form *stol-d- in Greek stolé, garment, array, equipment: STOLE}, III. Zero-grade form “*stj-. 1. Suffixed form *stl-to- in Latin stultus, foolish (< “unmovable, unedu- cated”): STULTIFY. 2. Suffixed zero-grade form “st/-no- in Germanic *stullén- in Old High German stollo, post, support (> German Stolle, Stollen, stollen): sTOLLEN. 3. Suffixed zero-grade form *stal-nd- in Greek stélé, pillar: STELE. IV. Extended form “stelg- in Germanic *stalk- in Norwegian dialectal stalk, stalk, akin to the source of Middle English stalk(e), stalk: sTALK’. V. Ex- tended form *steld- in: a. Germanic *stiltjon- in Low German and Flemish sfilte, stick, akin to the source of Middle English stilte, crutch, stilt: sTILT; b. zero-grade form “*stld- in Germanic *stult-, “walking on stilts,” strutting, in Old French estout, stout: stout. [Pok. 3. stel- 1019.] stele-. To extend. Zero-grade form “*sélo-. 1. Suffixed form *stlo-to- in Latin /atus, broad, wide: LATITUDE; DILATE. 2. Attributed by some to this root (but more likely of obscure origin) is Latin /aémina, place, layer: LAMELLA, OMELET. [Pok. 2. stel- 1018.] sten-. Narrow. Suffixed form *sten-wo- in Greek stenos, narrow: STENO-, STENOSIS. [Pok. 2. sten- 1021.] (s)tene-. To thunder. 1. Zero-grade form *stno- in Ger- manic *thunaraz in: a. Old English thunor (genitive thunres), thunder, Thor: THUNDER; THURSDAY; b. Middle Dutch doner, donder (> Dutch donder), thun- der: BLUNDERBUSS, DUNDERHEAD; C. Old Norse Thorr (older form Thunarr), “thunder,” thunder god: THOR. 2. O-grade form *tona- in Latin tondre, to thunder: TORNADO; ASTONISH, DETONATE, STUN. [Pok. 1. (s)ten- 1021.] ster-'. Stiff. I. O-grade form *stor-. 1. Suffixed form *stor-é- in Germanic *staren in Old English sfarian, to stare: STARE. 2. Suffixed form *stor-g- in: a. Germanic *starkaz in Old English stearc, hard, severe: STARK; b. Germanic denominative *starkjan in Old English *stercan (> Middle English starchen), to stiffen: STARCH. II. Full-grade form *ster-. 1. Germanic *sternjaz in Old English stierne, styrne, firm: STERN}. 2. Suffixed form *ster-ewo- in Greek stereos, solid: STERE, STEREO-; CHOLESTEROL. 3. Lengthened-grade form *s¢ér- in Greek stérizein, to support: STERIGMA. III. Zero-grade form *str-. 1. Extended form *strg- in Germanic *sturkaz in
1014-66
1015-(s)teu-
1016-Old English storc, stork (probably from the stiff move- ments of the bird): STORK. 2. Germanic *striit- in Old English striitian, to stand out stiffly: struT. IV. Extend- ed form *sterd-. 1.Germanic *stertaz in Old English steort, tail: REDSTART. 2. Germanic “*stert- in: a. Old English *styrtan, to leap up (< “move briskly, move stiffly”): start; b. Old English steartlian, to kick, strug- gle: STARTLE. V. Extended form *sterbh- in Germanic *sterban in Old English steorfan, to die (< “become rigid”): STARVE. VI. Extended form *(s)ierp- in suffixed (stative) zero-grade form *trp-é- in Latin torpére, to be
1017-stiff: TORPEDO, TORPID, TORPOR. [Pok. 1. (s)ter- 1022.]
1018-ster-2. Also stere-. To spread. I. Extended form *streu-. 1. Germanic suffixed form *streu-nam in Old English stréon, something gained, offspring: STRAIN?. 2. Latin struere, to pile up, construct: STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION. 3. Zero-grade form *stru- in Latin industria, diligence, activity (endo-, within; see en): INDUSTRY. 4. Russian struga, deep place: SASTRUGA. 5. Germanic *strél6 in Old High German sirdla, arrow, lightning bolt (> German
1019-Strahl, ray): BREMSSTRAHLUNG. II. O-grade extended form *strou-. 1. Suffixed form *strou-eyo- in Germanic *strawjan in: a. Old English stré(o)wian, to strew: STREW; b. Old High German strouwen, strowwen, to sprinkle, strew: STREUSEL. 2. Suffixed form *strow-o in Germanic *strawam, “that which is scattered,” in Old English stréaw, straw: sTRAW. III. Basic forms *ster-, *stero-. 1. Nasalized form *ster-n-a in Latin sternere (past participle strdtus from zero-grade *stro-to-), to stretch, extend: STRATUS, STREET; CONSTERNATE, SUB- STRATUM. 2. Suffixed form *ster-no- in Greek sternon, breast, breastbone: STERNUM. IV. Zero-grade form *str-, stra-. 1. Suffixed form “str-to- in Greek stratos, multi- tude, army, expedition: STRATAGEM; STRATOCRACY. 2. Suffixed form *stro-to- becoming Celtic s(t/rato- in Scottish Gaelic srath, a wide river valley: STRATH. 3. Suf- fixed extended form *stro-mn in Greek stréma, mattress, bed: STROMA; STROMATOLITE. [Pok. 5. ster- 1029.]
1020-ster-*, Star. 1. Suffixed form “ster-s- in Germanic “ster- rén- in Old English steorra, star: STAR. 2. Suffixed form *stér-ld- in Latin stélla, star: STELLAR, STELLATE; CON- STELLATION. 3. Oldest root form “aster- in Greek astér, star, with its derivative astron, star, and possible com- pound astrapé, asteropé, lightning, twinkling (< “looking like a star”; Ops, stem op-, eye, appearance; see okw-): ASTER, ASTERIATED, ASTERISK, ASTERISM, ASTRAEA, ASTRAL, ASTRO-; ASTEROID, ASTRAPHOBIA, DISASTER, Sterope. 4, Iranian stem *s¢dr- in Persian sitareh, star: ESTHER. [Pok. 2. ster- 1027.]
1021-ster-4. To rob, steal. 1. Possibly dissimilated form in Germanic *ste/an in Old English stelan, to steal: STEAL. 2. Germanic derivative noun *stél-ithé (-ithd, abstract suffix) in Middle English stelth, stealth: STEALTH. 3. Ex- tended dissimilated form in Germanic frequentative *stalkon in Old English *stealcian, to move stealthily: STALK?. [Pok. 3. ster- 1028.]
1022-ster-5. Barren. Latin sterilis, unfruitful: STERILE. [Pok. 6. ster- 1031.]
1023-(s)ter-n-. Name of thorny plants. Extension of ster-1. Suffixed zero-grade form *tr-n-u- in Germanic *thurnu-, thorn, in Old English thorn, thorn: THORN. [Pok. 7. (s)ter-n- 1031.]
1024-(s)teu-. To push, stick, knock, beat; with derivatives referring to projecting objects, fragments, and certain related expressive notions and qualities. I. Extended forms *steup-, steub-. 1. Germanic *staup- in Old English stéap, lofty, deep, projecting: STEEP!. 2. Germanic *staupilaz in Old English stypel, st@pel, steeple: STEEPLE. 3. Germanic *steup-, “bereft” (< “pushed out”), in Old English stéop-, step-: STEP-. 4. Germanic *stip- in Old English stipian, to stoop: stoop}. 5. Germanic expres- sive form *stubb- in Old English stubb, stybb, stump: STUB. 6. Germanic *stuf-, “fragment,” small coin, in
1025-steu(8)-
1026-Middle Dutch stuyver, stiver: STIVER. II. Extended form *steud-. 1. Nasalized form *stu-n-t- in Germanic *stunt- jan in Old English styntan, to dull: stinT!. 2. Germanic *staut- in: a. Old High German stézan, to push: sTOss; b. Middle Low German and Middle Dutch stéten, to force, akin to the source of Middle English stutten, to stutter: sTUTTER. III. Extended form *steug-. 1. Ger- manic *stukkaz in: a. Old English stocc, tree trunk: stock; b. Old High German stoc (> German Stock), staff: ALPENSTOCK; Cc. Old French estoc, rapier, sword point: TUCK’, 2. Germanic *stukkjam in: a. Old High German stukki, crust, fragment, covering: SHTICK; b. Italian stucco, stucco: stucco. 3. Germanic *stok- in Dutch stoken, to poke, thrust: sTOKER. IV. Suffixed (stative) zero-grade extended form *stup-é- in Latin stupére, to be stunned: STUPENDOUS, STUPID; STUPEFY. V. Suffixed (stative) extended zero-grade form *stud-é- in Latin *studére, to be diligent (< “to be pressing for- ward”): STUDENT, STUDY. VI. Extended zero-grade form *stug- in Greek Stux, the river Styx (< “hatred”): Styx. VII. Variant zero-grade form *tud-. 1. Latin tudes, ham- mer: TOIL!. 2. Suffixed form *tud-ti- in Latin tussis, cough: TussIs. 3. Nasalized form *tu-n-d- in Latin tun- dere, to beat: CONTUSE, OBTUND, PIERCE, RETUSE. VIII. Variant zero-grade form *tup-. 1. Suffixed form *tup-o- in Greek tupos, a blow, mold, die: TYPE; ANTI- TYPE, ARCHETYPE. 2. Nasalized form *tu-m-p- in Greek tumpanon, drum: TYMPANUM. [Pok. 1. (s)teu- 1032.] steu(e)-. To condense, cluster. Possible root. 1. Extended form *stip- in: a. Greek stuppé, tuft, tow: STOP, STUPE; b. Sanskrit stipah, tuft of hair, crown of the head: STUPA. 2. Extended form *stibh- in Greek stuphein, to contract: sTYPTIC. [Pok. steua- 1035.]
1027-ste-men-. Denoting various body parts and orifices. Greek stoma, mouth: STOMA, STOMACH, STOMATO-, (STO- MATOUS), -STOMY; ANASTOMOSIS, ANCYLOSTOMIASIS, PROSTOMIUM, SCYPHISTOMA. [Pok. stomen- 1035.] storo-. Starling. Germanic *staraz in Old English ster, starling: STARLING}. [Pok. storos 1036.]
```


## [2026-09-14T02:30:07.606Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG stan ===\"; grep -n \"staH\\|\\*stan\\b\\|STAN\\|stān\" CHEUNG.txt | head -40"
}
```


### [2026-09-14T02:30:07.693Z] TOOL RESULT

```
=== CHEUNG stan ===
1364:*AVESTAN: (+ *ä-) ? YAv. auuä- ‘to have the appearance of, be like’ || (+ *fra-) 
1416:*AVESTAN: baZ- (baxs-) ‘to bestow, divide, give a share’ (cf. Martinez 1999: 128 ff.) 
1470:*AVESTAN: Y Ау. astö.biö- ‘who breaks a bone’ (V 4.37, V 4.39) = Liste: 38 
1499:*AVESTAN: b(a)il- ‘to fear [intr.]; to be scary, scare’ || (+ *ni-) ‘to be afraid of’, also 
1565:*AVESTAN: ban- (caus.) ‘to make ill, afflict’. © КеПепѕ 1984: 143 emends ҮАУ. 
1595:*AVESTAN: YAv. band- ‘to bind’ = Liste: 37 
1702:*AVESTAN: bar- ‘to bring, carry’ || (+ *ati-) ‘to carry over, to’ || (+ *apa-) ‘to take, 
1896:*AVESTAN: YAv. baranti (Lsg.) ‘when it storms’ (V 8.4) 
1926:*AVESTAN: Y Av. baraj- ‘to honour, welcome’. Ф A noun, probably instr. sg, baraja, 
2016:*AVESTAN: YAv. as.baouruua- '(place) where there is a lot to chew he to eat]’ (Yt 
2046:*AVESTAN: YAv. baraz- ‘to enlarge’, (Gpl.) barazimanam ‘heights’, YAv. barazant- 
2146:*AVESTAN: baod-, Y Av. baoö- ‘to feel, sense’ || (+ *pati-) ‘to concentrate on, heed’ || 
2215:*AVESTAN: YAv. *baoö- (bus-) ‘to smell’ || (+ *upa-) ‘to smell, have a smell’ || (+ 
2273:*AVESTAN: bauu- (bü-) ‘to be, become’ || (+ *pari-) ‘sich machen über; to get hold 
2369:*AVESTAN: (+ *api-) ? YAv. aipi-óDaoya- ‘bending from behind (?)’ (-d- < ?, Yt 
2393:*AVESTAN: YAv. büj- (bunj-) ‘to save, redeem’ = Liste: 39 
2472:*AVESTAN: baxs- ‘to divide, have a share’ = Liste: 36f. 
2533:*AVESTAN: Y Av. аиш. Баба ‘due to pressure’ (Yt 10.134) 
2566:*AVESTAN: YAv. bisaz- ‘to cure, heal’, also YAv. baesaza- ‘healing, curative’ 
2606:*AVESTAN: YAv. braz- ‘to shine’ — Liste: 40 
2655:*AVESTAN: (+ *pari-) Y Av. pairi.bri- ‘to shave, shear’ = Liste: 40 
2825:*AVESTAN: YAv. bräs- ‘to wander, roam ?’ © The interpretation of hapax ҮАУ. 
2869:*AVESTAN: OAv. bus- ‘to endeavour, strive for’, OAv. bustis (pl.) ‘endeavours’ (Y 
2898:*AVESTAN: Av. caii- ‘to heap up, gather’ || (+ *ui-) ‘to select, choose’ || (+ *ham-) ‘to 
2984:*AVESTAN: Y Av. ci- (caii-, kaii-, kae-) ‘to atone’ = Liste: 22 
3025:*AVESTAN: OAv. cailas-ca (n.) ‘attention, respect’ (Y 45.5) || (+ *ш-) ҮАУ. (Gsg.m.) 
3152:*AVESTAN: ciS- ‘to assign’, tkaesa- ‘teaching’ || (+ *para-) ‘to make it understood’ || 
3187:*AVESTAN: c(ö)it- ‘to remark, observe’ || (+ *fra-) ‘to recognise [Humbach II: 80; 
3348:*AVESTAN: car- ‘to come and go’ || (+ *para-) ‘to pass over’ || (+ *ui-) ‘to go to and 
3434:*AVESTAN: Ү Ау. са$- ‘to teach, show’ = Liste: 22 
3595:*AVESTAN: 3(ii)à- ‘to be calm, glad, rest" > Liste: 70 
3653:*AVESTAN: Y Av. Sama ‘defecation, excrement’ (F 201, Klingenschmitt 1968: 73 f.) || 
3712:*AVESTAN: YAv. (“)Sam- ‘to swallow’ = Liste: 69 
3762:*AVESTAN: S(ii)auu- (Sauu-, $0-) ‘to move, go’ || (+ *abi-) ‘to come to’ || (+ *fra-) ‘to 
3875:*AVESTAN: dab- ‘to deceive’ — Liste: 27 
3923:*AVESTAN: dă- (6a-) ‘to bestow, place upon’ || (+ *abi-) *beigeben, beilegen’ || (+ 
4051:*AVESTAN: see *daH! || (+ *à-) ‘to put, place in, on’ || (+ *uz-) ‘to erect’ || (+ *ni-) ‘to 
4129:*AVESTAN: OAv. d(a)ii- ‘to divide, distribute’ = Liste: 30 
4149:*AVESTAN: OAv. da- ‘to bind’ © Liste: 30 
4251:*AVESTAN: d(a)i- (ба1-) ‘to look, see’ || (+ *aua-) ‘to see off || (+ *a-) ‘to look, see
```


## [2026-09-14T02:30:25.603Z] TOOL CALL #19: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:30:25.612Z] TOOL RESULT

```


```


## [2026-09-14T02:30:28.682Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D8%B3%D8%B7%D8%A8%D9%84",
 "prompt": "Arabic إسطبل: etymology, meaning, borrowing route from Latin stabulum / Greek. Quote the etymology section verbatim."
}
```


## [2026-09-14T02:30:29.673Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/standard",
 "prompt": "Quote the full etymology of 'standard' (noun) — Old French estandart, Frankish *standhard, alternative proposals."
}
```


### [2026-09-14T02:30:32.627Z] TOOL RESULT

```
Based on the Wiktionary content provided, I cannot fulfill your request. The page does not include an etymology section for إسطبل (isṭabl). 

The entry only contains:
- Pronunciation: /ʔis.tˤabl/
- A noun definition stating it is "alternative form of إِصْطَبْل (ʔiṣṭabl)"
- Declension tables

There is no etymological information explaining the word's origin from Latin *stabulum* or Greek, nor any borrowing route details. To access the etymology you're seeking, you would need to consult the entry for إصطبل (the primary form), which is referenced but not included in this excerpt.
```


### [2026-09-14T02:30:35.002Z] TOOL RESULT

```
# Etymology of "Standard" (Noun)

**Primary Origin:**
The word comes from "shortened form of Old French _estandart_ 'military standard, banner'" and Medieval Latin _standardum_.

**Proposed Etymology (Primary Theory):**
According to Barnhart and Watkins, these likely derive from Frankish _*standhard_, described as "literally 'stand fast or firm,'" combining elements cognate with the verbs "stand" and "hard."

**Alternative Theory:**
The OED and others dismiss the above as folk-etymology, instead connecting the Old French term to _estendre_ ("to stretch out"), which traces back to Latin _extendere_.

**Historical Context:**
The flag sense made sense because "the flag was fixed to a pole or spear and stuck in the ground to stand upright." Some extended senses (upright pole, mid-15c.) appear influenced by the verb "stand," and Middle English used the word for various standing objects—poles, stumps, candlesticks, and towers.
```


## [2026-09-14T02:30:37.991Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D8%B5%D8%B7%D8%A8%D9%84",
 "prompt": "Arabic إصطبل / اصطبل: etymology section verbatim — borrowing from Greek στάβλον / Latin stabulum, Aramaic mediation, meaning 'stable'."
}
```


## [2026-09-14T02:30:40.458Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%A7%D9%86%D8%AF%D9%86",
 "prompt": "Persian ستاندن (setândan) / ستدن: full etymology section verbatim — Middle Persian form, Proto-Iranian root, cognates, whether related to *stā- 'stand' or to 'steal/take'."
}
```


### [2026-09-14T02:30:43.877Z] TOOL RESULT

```
# Summary of إصطبل (Stable/Stall)

This Wiktionary entry documents an Arabic noun meaning "stable" or "stall"—a building for housing horses.

**Etymology**: The word traces back through Byzantine Greek στάβλος (stáblos) to Latin "stabulum," reflecting ancient trade and cultural contact across Mediterranean regions.

**Key Details**:
- **Pronunciation**: /ʔisˤ.tˤabl/
- **Plural**: إصطبلات (ʔiṣṭablāt)
- **Gender**: Masculine

**Historical Usage**: The entry includes citations from an 873 CE geographic text by al-Ya'qubi, demonstrating the word's established presence in classical Arabic literature.

**Linguistic Descendants**: The term spread across languages through Persian (اصطبل) into South Asian languages including Hindi (अस्तबल) and Urdu (اصطبل), showing the word's journey along historical trade routes.

The detailed declension table shows how the word inflects across singular, dual, and plural forms in classical Arabic grammar patterns.
```


### [2026-09-14T02:30:45.282Z] TOOL RESULT

```
# ستاندن (Standin) - Wiktionary Entry

This entry documents a verb appearing in **Central Kurdish** and **Persian**.

## Central Kurdish

The word **ستاندن** (standin) derives from Proto-Iranian *staHn-, meaning "to take." It functions as a transitive verb with two primary meanings:

1. "to take, obtain" (synonym: وەرگرتن)
2. "to buy" (synonym: کڕین)

The entry includes comprehensive conjugation tables covering simple past, present, imperfect, progressive, perfect, subjunctive, and imperative forms across all persons and numbers.

## Persian

In Persian, **ستاندن** (setândan) is listed as "alternative form of ستدن (setadan)," indicating it represents a variant spelling of the same verb.

## Etymology

The Central Kurdish term traces back through Proto-Iranian linguistic ancestry, positioning it within a larger family of Iranian language development.
```


## [2026-09-14T02:30:48.685Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%AF%D9%86",
 "prompt": "Persian ستدن (setadan): quote the etymology verbatim — Middle Persian, Proto-Iranian root, Old Persian forms, cognates, meaning."
}
```


## [2026-09-14T02:30:49.998Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/staHn-",
 "prompt": "Proto-Iranian *staHn-: quote the reconstruction page verbatim — meaning, PIE source root, Old Persian / Avestan attestations, descendants."
}
```


### [2026-09-14T02:30:51.048Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:30:53.962Z] TOOL RESULT

```
# Etymology of ستدن (setadan)

The verb ستدن originates from **Middle Persian** (YNSḆWN-tn' /stadan/), which derives from **Proto-Iranian** *staHn- meaning "to take."

This Proto-Iranian root may represent "a suffixed form of Proto-Indo-European *stnéh₂ti ('to stand'): 'to cause to stand' > 'to fix [a price, one's mind on something]' > 'to take'?"

The semantic evolution shows a progression from the concept of standing to fixing or establishing something, ultimately developing into the meaning of taking or obtaining.
```


## [2026-09-14T02:31:00.217Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"staH\\|stān\\|stan-\\|\\bstad\\b\\|sitadan\\|sitānīdan\\|stānīdan\" CHEUNG.txt | head -40"
}
```


### [2026-09-14T02:31:00.272Z] TOOL RESULT

```
11017:sim., go back to *fra- + *staH. 
23400:358 *staH 
23411:*staH ‘to place, set; [intr.] stand’ 
23455:*staH 359 
23506:360 *staH 
23540:Oss. I. styn/stad ‘to stand up’, I. stajyn/stad, D. (#)stajun/(a)stad ‘to become tired, 
23573:*staHn ? ‘to take’ 
23574:*AVESTAN: (+ *fra-) ? Y Av. frastan- ‘to take, convey forward’ (Gershevitch, Mithra: 
23598:© This root is perhaps originally a pres. n-stem of *staH (?). 
23995:instance, *staH ‘to place, set, stand’ and *@ra(n)é ‘to (op)press'. 
33401:frastan-, 361 
41492:sitadan/sitan-, 361 
46323:(«)stajun/(&)stad (D), 
47059:stajyn/stad (I), 360 
47066:styn/stad (T), 360 
55885:*parH?. (s.v.), *staHn (s.v.), 
57368:*daH’, *kan', *staH 
57789:*staH 
57980:*pad, *staH, *uindar 
58114:*staHn
```


## [2026-09-14T02:31:01.850Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^\\*ST\\|^\\*staH\\|^\\*stan\\|^\\*sta\" CHEUNG.txt | head -40; echo \"=== TAY ===\"; grep -n \"tāyu\\|tāiiu\\|'thief'\\|thief\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T02:31:01.919Z] TOOL RESULT

```
22399:*stand (*skand) ‘to break, cleave’ 
23411:*staH ‘to place, set; [intr.] stand’ 
23455:*staH 359 
23557:*staij ? 361 
23573:*staHn ? ‘to take’ 
23612:*staij ? ‘to stab; to be contentious ?' 
23650:*stamb(H) ‘to withstand, be stiff, stern, unmoving’ 
23684:*star 363 
23707:*stap ‘to hasten, (op)press’ 
23735:*star ‘to sweep, throw down; to sin” 
23776:*starH. See also Narten 1964: 278. 
23790:*starH! ‘to spread’ 
23810:*starH2 365 
23844:*starH ‘to make/become stiff, rigid’ 
23876:*stau ‘to praise’ 
23938:*staub/f ‘to sound, utter’ 
23953:*staup ‘to overcome, defeat’ 
55357:*staij 
55515:*stamb(H) 
55602:*stamb(H) 
56292:*staup 
56344:*staup (s.v.), *tanč (s.v.), 
56788:*stap, *tauj !, *Syar/tur 
57328:*staup, *taru 
57395:*stap 
57682:*stau (S.V.) 
57789:*staH 
57827:*star 
57974:*staij 
58114:*staHn 
58220:*star 
58271:*staub/f, *uab/f , *zag 
58409:*stamb(H) 
=== TAY ===
3316:stick, adhere’, ? Anar. Capowger ‘robber, thief?
```


## [2026-09-14T02:31:04.779Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '23570,23615p' CHEUNG.txt"
}
```


### [2026-09-14T02:31:04.836Z] TOOL RESULT

```
gwas-; NEVP: 11; Korn 2005: 117, 351, 386 


*staHn ? ‘to take’ 
*AVESTAN: (+ *fra-) ? Y Av. frastan- ‘to take, convey forward’ (Gershevitch, Mithra: 


177 ad 20) > Liste: — 
Pres. ua-: IND. 3pl. ? YAv. frastanuuanti (Yt 10.20) 


*MIDDLE PERSIAN: MMP ‘st’n- (ВМР YNSBWN-) ‘to take (away) = DMMPP: 
88b 

Pres.: IND. 35р. MMP “‘st’nyd, 3р1. MMP ‘st’nynd, ‘st’nynd, SUBJ. 3sg. MMP ‘st’n’d, ‘st’n’d, Ipl. 
MMP *‘st’n’m, 3р1. MMP ‘st’n’nd, ‘st’n’nd, IMPV. 2р1. MMP ‘st’nyd; Partic.: perf. pass. MMP * ‘std, 
‘std; Pass.: pres. IND. 3sg. MMP ‘st’nyhyd, SUBJ. 3sg. MMP ‘st’nyh’d 

*PARTHIAN: ‘st’n- ‘to take (away)’ = Ghilain: 71 | DMMPP: 88b 

Pres.: IND. 3sg. ‘st’nyd, ‘st’nyd, 3pl. ‘st’nynd, ‘st’nynd, SUBJ. 1sg. ‘st’n’n, 2sg. ‘st’n’h, 3sg. *‘st’n’h, 
3р1. *‘st’n’nd, IMPV. 2р1. “пуа, OPT. ‘st’nndy, ‘st’nyndyh; Partic.: perf. pass. ‘std; Inf.: *‘stdn 

*NWIR: NP sitädan/sitän- ‘to take, carry away; stand, stay’, Awrom. asay/-san-, Gur. 
(Kand.) -sän- ‘to take, buy’, Kurd. (Kurm.) standin/stén-, stin-, (Sor.) s(t)andin/ 
s(t)en-, Gil. (Rsht.) usadoen/usan- ‘to take (up), gather’, Siv. san-, sen- (supplet. 
es(s)ä, es(s)é, isd < ?) ‘to take (away)’ 

© This root is perhaps originally a pres. n-stem of *staH (?). 

«PIE pres. n-stem *st(e)H>n- ‘to (want to) buy; fix (a price, one's mind on 
something)’ ? = LIV: 590 f. | Pok.: 1004 ff. 

*IE COGNATES: Lat. prae-stinare ‘to buy, fix (a price)’, de-stinäre ‘to fix (in position, 
one’s mind on something); to destine for one’s own by settling terms, arrange the 
purchase of’, ob-stinare ‘to set one's mind on’, ? Arm. stanam ‘I receive, acquire’ (< 
Ir. ?) 

*REFERENCES: KPF II: 203; Christensen, Contributions: I: 60; MacKenzie 1966: 89; WIM III:116; 
Cabolov 1997: 73 


*staij ? ‘to stab; to be contentious ?' 
*AVESTAN: YAv. stij- (f.) ‘fight, struggle’ (Yt 10.71) 
*MIDDLE PERSIAN: MMP ‘styz- ‘to quarrel’, ВМР styck /stézag/ ‘quarrel, strife’
```


## [2026-09-14T02:31:14.886Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['FFD','SOD','MON','ARY','BQT']: print(k, json.dumps(d[k],ensure_ascii=False,indent=1)[:1500]); print('---')\n\""
}
```


### [2026-09-14T02:31:15.998Z] TOOL RESULT

```
FFD {
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).",
 "covers_etymology": true,
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Se
---
SOD {
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
---
MON {
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
  "/home/sfmqrb/git/rishe/data/ver
---
ARY {
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ],
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin 
---
BQT {
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={
---
```


## [2026-09-14T02:31:19.778Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; python3 - <<'EOF'\nfor f in ['FFD_pages.txt','FFD_pages_faseng.txt']:\n    d=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    print('=====',f,'blocks',len(d))\n    for i in (62,63,64):\n        print('--- leaf',i,'(pdf page',i+1,'printed',i+1-5,')')\n        print(d[i][:1800])\nEOF"
}
```


### [2026-09-14T02:31:20.877Z] TOOL RESULT

```
Exit code 1
===== FFD_pages.txt blocks 115
--- leaf 62 (pdf page 63 printed 58 )
[pdf page 63]
ها فعلهای فارسی دری
زدن
زد < فارسی میانه 240 + ایرانی باستان ۵-12[*. برای ۵ > آراست. 3[صورت
: ضعیف 20[ است» به معنی «زدل).
زن < فارسی میانه 227 < ایرانی باستان «۵[*. به 48[ چیزی برای ساختن مادهٌ
مضارع افزوده نشده است > اوژدن.
زدودن
زدود < ایرانی باستان ۶2-43-12 برای 1۵ -> آراست. ۳۶ پیشوند فعلی است. ريشهٌ
تا به معنی «پاک کردن» است.
زدای + ایرانی باستان 8ر12-437-2* 22 برای ساختن مادهٌ مضارع از ريشه به کار
می‌رفته است. 413۷ صورت بالانده و ۵5 صورت ضعیف ريشةٌ 4۵۷ هستند > اندودن.
زیستن
زیست < فارسی میانه 2731» صورت کهنتر ۰.2۷181 27181 مادةٌ ماضی جعلی است.»
از 27۷ مادةٌ مضارع.
زی + فارسی میانه ۰27 صورت کهنتر 27۷« ایرانی باستان ۷۵[*. 7۷2[ صفت است
که مادةٌ مضارع گرفته شده و از ریشهٌ ۲[: زیستن» و پسوند 2 ساخته شده است.
ساختن
ساخت < فارسی میانه ۶371 + ایرانی باستان ۹21۵". برای 1۵ -> آراست. ‎٩3‏
‏صورت اصلی 835 است» ۴ پیش از ۲ به #بدل شده است. 83 صورت بالاندةٌ 82۴ است و
ريشهٌ 8۵ به معنی «توانابودن» است.
ساز < فارسی میانه 932 < ایرانی باستان ۹30-۵". برای 2 > آرای. ۴ به 6 بدل شده

--- leaf 63 (pdf page 64 printed 59 )
[pdf page 64]
ماده‌های ماضی و مضارع فارسی دری سا ۵۹
بنن .
سپردن (طی کردن)

سپرد < فارسی میانه 5070 < ایرانی باستان 5۶07-1. برای ۵ > آراست. 50
صورت ضعیف 5047 است. ريشهٌ 5047 به معنی «گام‌نهادن» است.

سپر < فارسی میانه 8027 < ایرانی باستان -۶02۳*. برای 2 > آرای.

۱ ۰
سپردن (تسلیم کردن)

سپرد < فارسی میانه 20190070 < ایرانی باستان ۵01-807-12*. برای ق1 > آراست.
01 پیشوند فعلی است. ۶07 صورت. ضعیف ريشةٌ 8047 است. ۶07 «رها کردن» معنی
می‌دهد و با 5027 به معنی گام‌نهادن فرق دارد -> سپردن (طی کردن).

سپار < فارسی میانه ۵018037 < ایرانی باستان ۵1-8037-4*. برای 2 > آرای. ‎٩037‏
‏صورت بالاندة ريشهٌ 8027 است.

سپوخت < فارسی میانه 5057 < ایرانی باستان ۶۵2۳۳۵*. برای 18 > آراست.
8 صورت اصلی ۶047 است» ۲ پیش از 1 به #بدل شده است.

سپوز < فارسی میانه 5052 < ایرانی باستان ۶0۵0-2*. برای 2 > آرای. به 6 بدل
شده است.

ریشهٌ 80201 به معنی «فشاردن» است. ۶0531278 به معنی «فشاردن» و «نافرمانی‌کردن»
است. «سپوختن» از اضداد است؛ به معنی «فرو کردن» و «بیرون کشیدن».

ستدن

سند < فارسی میانه 5120 < ایرانی باستان 812-1۵*. برای 12 -> آراست. 512 صورت
ضعیف ريشةٌ 8187 است به معنی «گرفتن»» برای ضعیف کردن ريشه 7 حذف شده است.

ستان < فارسی میانه 5137 ج ایرانی باستان ۶138-۵*. برای 2 -> آرای. ‎٩137‏ صورت
بالاندهٌ ۶120 است.

--- leaf 64 (pdf page 65 printed 60 )
[pdf page 65]
انا انا فعلهای فارسی دری
«ستاند» ج «ستانید» مادهٌ ماضی جعلی از «ستان» است.
۱ ستودن
ستود + فارسی میانه 5100 < ایرانی باستان ۹18-12*. برای 2 آراست. صورت
ضعیف 514۷ است و ريشهٌ 912۷ به معنی «ستودن» است.
ستای < فارسی میانه 513 < ایرانی باستان 8ر813۷-۵*. 278 نشانه‌ای بوده که
برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است. ‎٩13‏ صورت بالاندةٌ ریشهٌ 312۷
است.
دا
سخت + فارسی میانه 3231 < ایرانی باستان ۶۵-1*. برای ۵ > آراست. 8 صورت
اصلی است و آن صورت ضعیف ريشهٌ 8 به معنی «کشیدن» است. برای
ضعیف‌کردن ريشه 8 حذف شده است.
سنج + فارسی میانه [828 < پهلوی اشکانی [8۵2 < ایرانی باستان ۵-[۶28*. برای 8 ->
آرای. [به جای ج آمده است.
سرشتن
سرشت < فارسی میانه 85151 + ایرانی باستان ۶713-1۵*. برای ۵ > آراست. کزرّه
صورت ضعیف ريشةٌ 8788 است و آن به معنی «چسباندن» است.
سریش < فارسی میانه 8783 < ایرانی باستان ۶۲۵15-2*. برای 2 > آرای.
«(سریش)» به معنی «رستنی‌ای که ... بعد از رسیدگی خشک کنند و آرد سازند و
کفشگران و صحافان چیزها بدان چسبانند.» (برهان قاطع)» از ریشهٌ 788 است.
سرودن
سرود + فارسی میانه ۶734 < ایرانی باستان ۹۳8-1۵" برای 1۵ > آراست. ‎٩۳3‏
‏صورت ضعیف ريشةٌ 818۷ است. به معنی «خواندن».

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'FFD_pages_faseng.txt'
```


## [2026-09-14T02:31:33.929Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor i in (177,178,179):\n    print('=== leaf',i,'printed ~',i-21)\n    print(d[i][:1600])\nEOF"
}
```


### [2026-09-14T02:31:35.009Z] TOOL RESULT

```
leaves 412
=== leaf 177 printed ~ 156
— 156 —
aw. spereza- 'Milz' (ZPGl.) ; pblv. spärz; ai. pWidn-
*Milz\
703. siperl Vollendet', isperl .(Sahn. II, 820 Vers 866).
aw. "^usjjerena-, tis- 4- {/'par- ; LW. chald. N^löDN,
arm. spar.
de Lagarde, Semitica 45. Unsicher, vergl. np.
supürden (No. 697).
704. 8ipe7iJ 'RuhepVdtz, Gasthaus' (8ähn. I, 229 Vers 1791).
plilv. «5paw/ 'Ruheplatz, Asyl' (Men. ; AV.), spun-
jänaklh, arm. LW. aspnjakan Gast', cliald. syr. LW.
rr^'N, prSK^N 'Gasthof, Gasthofbesitzer (de Lagarde,
Semitica 51).
Dazu gehören auch die Lehnworte türk. ispenje
'Steuern von Kriegsgefangenen , Sklavengeld', serb.
spendza *Aufwand', rumaen. spendze 'Steuer, bulg.
ispenö 'Sklaventaxe' bei Miklosich, Denkschr.
WAW. Band 37, 48 und 38, 130 (dort falsch erklärt).
de Lagarde, Armen. Stud. No. 207 sieht in dem
Worte eine Zusammensetzung mit np. esp *Pferd'.
705. siijJuS, uspus 'Laus', siqms (etc.).
miiz. isftj (H.-Sch.).
aw. spis 'Laus'; phlv. spis (vd. 17 (8)), sjjus (AV.).
kurd. sipi^ aspe 'Laus' ; afy. spa$a ; oss. sis^ (239) ;
wa/. sisy sar. spal.
706. sipöyten^ supö/ten 'einheften {der- Sa'di, Bostän
S. 261 Vers 304); heraustreiben (Sahn. III, 1797
Vers 231; Is. 16, 3, 4)' 0.
phlv. spöj (päz. spöz) 'Aufschub' (Salemann, Mel.
asiat. IX, 247, 248 Note 85), spö/tan^ spöjet 'ent-
fernen, heraustreiben (Men., AV.), spö/tUan; arm. LW.
spidem Verschieben'.
Wenn 'einheften' die Grundbedeutung ist, so Hesse
sich lat. pungö (V^ptig-) vergleichen; doch ist dies
durchaus unsicher.
707. sipiJir 'Himmel'.
ap. JSnid^ofMrag^ 2l!7itd()tddT?jg; phlv. Huspitr (Gemme,
*) Die Belegstellen stammen von Herrn Prof. Nöldeke.
=== leaf 178 printed ~ 157
- 157 -
Hörn, Mitth. Heft IV, 40 No. 47), zweifelhaft'), spihr
(Men.).
Vergl. Nöldeke, Pers. Stud. 36 ffolg.
708. siped, sefedj isped Veiss'; sipede fEiweiss AM. 31
Zeile 6, 'Leukom des Auges' AM. 31 Zeile 14, 18,
*Morgenlielle' Öahn. I, 88 Vers 496 u. ö.) ; jüd.-pers.
TB1D (Is. 1, 18).
Käs. Q. esbed, K. esbe, Z. söbö.
aw. Sparta- Veiss*; phlv. spSt, arm. LW. spitak; ai.
cvSt'- 'lieht, weiss'.
kurd. LW. sipT; B.{y. spTn; bei. (LW.? ispet, n. safe^-
(166); LW. sar. spSid, sangl. ispSd, sijn. sufed, rtiinj.
supl,
Phlv. spenak (Men. H, 113, Fr. Müller, SWAW.,
Band CXXV Seite 10) ist unsicher. •
709. sitäden 'wegnehmen', Praes. sitän-em, siteden^ isteden,
sitänden,
phlv. päz. statan (PPGl.).
ai. skr. l/^sta-^) 'stehlen* in stäi/dt 'verstohlen', stäi/u-
(neben tayd-) *Dieb', stmä- 'Dieb*, ^^feija- 'Diebstahr,-
aw. tayu- *Dieb', taya- 'Diebstahl*; vergl. ksl. fai/q,
taiti Verbergen', air. tdid 'Dieb*.
710. 'ffitän, 'istän *-Stand, -Ort* (nur in Conipositen) ).
ap. aw. stäna- 'Stand*, aw. -stana-; phlv. -stän, arm.
LW. -stan ; ai. afhd)ia- 'Stand', sthäwf-,
711. {\)sitäre 'Stern.
aw;. Star- 'Stern*; phlv. stärak; ai. stdr-; arm. astk
(H. No. 32).
>) Justi (ZDMO. 46, 289) wiU x"äpafzä lesen; jedenfalls scheint
mir meine Lesung des Steins ZDMG. 18 No. 127 (II) Farraxü(%) m
Heft IV der Mitteilungen, 8. 39 vor Spirh desselben Gelehrten (ZDMG.
46, 285) den Vorzug zu behalten.
*) Hübschmann, Indog. Vocalsystem, S. 31.
') Im Hähname sehr häufig -sitän, z. B. guhitän (I, 161 Vers 594),
KäbuUitän (z. B. I, 157 Vers 506), Zabulsitän (I, 146 Vers 821). Die
Wörterbücher führen längst nicht al
=== leaf 179 printed ~ 158
— 158 —
kuid. istirk; af/. sförai, 8tar[ya fAuge'); oss. stali
(229) ; wa/. stär, si/n. starf^ stirj ^), sar. /turj^ minj.
asiäri, sangl. ustürak.
712. {2)sitäre Tliegennetz, Schirm' (Öähn. I, 102 Vers 746).
Zu [/^star- ausbreiten' (Rückert, ZDMG. 8, 314).
713. sitebr, setehr (AM. 112 Zeile 4), istebr *stark, gewaltig',
vergl. usttiwär^); arab. LW. istabraq'^^) grober Atlas-
stoff'.
aw. stawra- i^stahlira-, "^str^bhra-) *fest*; phlv. stapr
(vd. 18 (65) GL), d. i. stawr; ai. [^stabh- 'feststellen,
stützen etc., stambha- 'Pfosten, Säule (Hübsch-
niann, ZDMG. 39, 93 Note 1).
oss. vergl. sfawd stark*.
714. sifff/r, ista/r 'Wasserbassin* (eigentlich etwas 'fest
sc. Ummauertes*).
Kh«. esseil j ostor ^ üsor^ sa/r (vergl. isfel etc. bei
Vullers).
aw. sta/ra- 'stark, fest'; vergl. den Stadtnamen
Sfa/r^ Ista/r,
715. sntuvff, sittirg 'stark, gross*.
ai. sthürd- 'dick, breit\ sthülä- 'grob, dick, gross,
feist'; phlv. sturg (ZPGl.).
kurd. nstär; oss. d, sfiir^ t. sfir gross, stark' (232);
bei. istür (167); yidg. üstür.
716. setei*veH, suturven^ esterven 'unfruchtbar' (Schefer,
ehrest, persane II, 188 Zeile 2).
Gehört wohl zu ai. start- 'unfruchtbar ; arm. sferj
(II. No. 258); gr. otttga; lat. sterilis; got. sfairö
(Hörn, KZ. 32, 583 No. 12).
Die neuper?ische Volksetymologie 'Maulesel ähnlich*
ist unwahrscheinlich, zumal es ein Suffix -ve72 'ähnlich*
sonst gar nicht giebt. Oder ist jüd.-pers. H^mriDN
(Is. 54, I) die ursprüngliche Form?
'J Im Satzsandlii entstanden nach Bartholomae, Studien II, 42;
aber verf^l. nhd. stern,. sterben u. v. a. ni. (Hörn, KZ. 32, 588 No. 24).
-) Arm. LW. sioi
```


## [2026-09-14T02:31:53.150Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD stad/stan ===\"; grep -n \"stad\\b\\|st'n\\|YNSBWN\\|stānīdan\\|stān-\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"YNSBWN\\|stadan\\|st'n-\" NYB_vol2_glossary.txt | head -20; echo \"=== HUB sitadan ===\"; grep -n \"sitad\\|städen\\|sitāden\" HUB.txt | head"
}
```


### [2026-09-14T02:31:53.235Z] TOOL RESULT

```
=== PHD stad/stan ===
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
PHD.txt:570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
PHD_mackenzie.txt:785:abcstan ['pst'n l ] refuge, support, trust.
PHD_mackenzie.txt:850:   a-dad ['d't'], a-dadestan ['-DYNA, -d'tst'n ] illegal. unjust.
PHD_mackenzie.txt:1313:awestad [)wst)t' I M )'wyst)d, N ostad] master (craftsman).
PHD_mackenzie.txt:1513:biistan [b)st)n I M b'yst'n, N ,,-,] always, often.
PHD_mackenzie.txt:1604:boyestiin [bwdst'n l I M bwyst)n, N bostan] (flower) garden .
PHD_mackenzie.txt:1824:dAdestiin [DYNA < A dyn'; d)tst'n l I M d'(d)yst'n, N da(de)stdn]
PHD_mackenzie.txt:1925:  --estan [-st'n l ] secluded place for menstruous women.
PHD_mackenzie.txt:1946: -estan [-st'n l ] cemetery.
PHD_mackenzie.txt:1991: -estan [-st'n' I. N --] school.
PHD_mackenzie.txt:4659:stadan, stAn- [YNSBWN-tn < A ynsbwn, ..; nsb , M <std, <st'n-, N
PHD_mackenzie.txt:6489:eighty hastad.                               equal (n.) hamahl, hamal, hamtag.
PHD_mackenzie.txt:7062:master awestad, rad, salar; ,.,., of the   merry wiyufsisnig; V. happy; make--
PHD_mackenzie.txt:9053:hastad"                      ~          sak
PHD_mackenzie.txt:11900:awestad                  ,K)'MtV~          humurwag                   \~~~t-'
=== NYB ===
242:YNSBWN-: YINS' BÜN impt. 3d p. pl. of NSB to take
3537:statan [YNSBWN-tn'] stān-, to take, in all senses; imp. YNSBWN = stan 28?’. 70%; —-i (ending written in Paz.!) = stam 60%; the forms with the endings -X, and -x, function a) as imp. sg. = stané 911 (-x,). 44? (-x2); b) as pres. 3d p. sg. 2515. 2815, 29? (-x,); c) as pret. pass. 3d p. sg. 2813, 121? (-x,). 42°. 4821, 498.22, 5015, 6019 (.x,); inf. YNSBWN-tn' 77°. 7917, 8919, — FrP 21 both YNSBWN- and YNSBWN., Ir. equivalents ysttn' - yst*nyt' — yst'nym = istatan — istānēt — istaném, some MSS *sttn' — ’st’n- ete. = astatan — astän-; Paz. stadan stan- (Mx), stän- (Aog.); MPrthPrs pt. ‘std, pres. *s?n-, v. Verbum 189, Ghilain 71; NP sitadan sitdn-.
6809:stadan, stán-: statan stah(a)m: stahm stāīdan, stāed: stayitan star: stur
=== HUB sitadan ===
383:= np. istadan, sitadan, das Praesens lautete in der
2583:709. Die urspriingliche Infinitivform scheint sitadan ge-
2584:wesen zu sein, vgl. np. sitadan (neben sitadan) = paz.
10711:sitadan 74.287 —
```


## [2026-09-14T02:31:54.860Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT tāyu ===\"; grep -n \"tāyu\\|tāyav\\|tayu-\" BRT.txt | head -20; echo \"=== SYN 790 steal ===\"; python3 - <<'EOF'\nd=open('SYN.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=d.find('STEAL')\nprint(d[i-200:i+2500] if i>0 else 'not found')\nEOF"
}
```


### [2026-09-14T02:31:55.989Z] TOOL RESULT

```
=== BRT tāyu ===
=== SYN 790 steal ===
x
11.33 Lose
11.34 RELEASE
11.41 Property
1142 Weaura, RicHes
1143 Money
M44 Com
1145 Purse
1146 Treasure
1147 Bank
1148 Herr
WL8L Rice
1152 Poor
11.53 Beccar
Wot Avartctous, Stiney
11.55 Miser
11.56 STEAL
11.57 THIEF
11.58 Ros, RoBBER
11.61 Lenp
11.62 Borrow
11.63 OwE
11.64 Drst
11.65 Pay (vb.)
11.66 AccouNnT, RECKONING 11.67 Security, SURETY 11.68 INTEREST
11.69 Tax (sb.)
11.71 IncoME
11.72 EXPENSE, Cost
11.73 Prorit
11.74 Loss
11.75 Lease, Rent (to Another) 11.76 Rent, Lease (from Another) 11.77 Hire (vb., a Person) 11.78 Wacss, Pay
11.79 Earn
11.81 Buy
11.82 SELL
11.83 Trav (vb.)
11.84 Mercuant, TRADESMAN 11.85 Market (Place)
11.86 Srorz, SHOP
11.87 Pricr
11.88 Dear (=Costly, Expensive) 11.89 CHmap
739
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and e
{ ? | |
740 SELECTED INDO-EUROPEAN SYNONYMS
11.11 HAVE Grk.  &w Goth. haban (aigan) Lith.  turéty NG &w ON hafa Lett, but with dat.; turgy Lat. habére Dan. have ChSl.  tmetz , It. avere Sw. hava SCr.  imati Fr. avoir OE habban Boh. mitti Sp. tener ME shave Pol. miéé Rum. avea NE have Russ. prep. u with een Ir. phrase with ‘be’ Du. hebben imel! ” NIr. phrase with ‘be’ OHG habén Skt. as- or bhi- with gen W. phrase with ‘be’ MHG haben Av. —_ah- with gen, ; Br. phrase with ‘be’; NHG haben
kaout
There is considerable overlapping of sense among the verbs listed in 11.11- 11.17. There is no sharp line between the colorless ‘have’ and the stronger ‘own, possess’. ‘Have’ is mostly from earlier ‘seize, take hold of’, ‘hold’, or ‘take’, which are again closely allied with each other and in part with ‘get, ob- tain’ and ‘keep, retain’.
The oldest method of indicating sim- ple possession, and doubtless that of the TE period, was by means of a phrase containing the verb ‘be’, expressed or implied, with an oblique case for the person. This is common enough even in languages which also have verbs for ‘have’ (Grk. pot gor, Lat. mihi est, etc.), and is the normal type in Indo- Iranian, and in the Celtic languages down to the present day.
The secondary use of verbs for ‘have’ as auxiliaries, esp. for past tenses, but also for future and ‘must (9.94), is not considered here.
Cf. Meillet, Le développement du verbe “avoir”, Festschrift Wackernagel, 9 ff.
1. ‘Have’ regularly expressed by phrases. Ir. rotbia less log dodaggnima lit. ‘reward shall be to thee with him of thy well-doing’ (Wb. 6a11), or using a prepositional phrase, is ed inso fil lasuide lit. ‘it is this that is with him’ (MI. 63d4), or, taking NT, Jn. 4.17, otk exw
avépa is rendered by NIr ni Shuil fear agam, W. nid oes gennyf wr, and Br. nem eus pried ebet ‘there is not a hus- band to me’; so also Le
```


## [2026-09-14T02:32:04.177Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('SYN.txt',encoding='utf-8',errors='replace').read()\ni=d.find('11.56 STEAL')\nwhile i>0 and 'Skt' not in d[i:i+3000]:\n    i=d.find('11.56 STEAL', i+1)\nprint(d[i:i+4200] if i>0 else 'nf')\nEOF"
}
```


### [2026-09-14T02:32:05.179Z] TOOL RESULT

```
11.56 STEAL
11.57 THIEF
11.58 Ros, RoBBER
11.61 Lenp
11.62 Borrow
11.63 OwE
11.64 Drst
11.65 Pay (vb.)
11.66 AccouNnT, RECKONING 11.67 Security, SURETY 11.68 INTEREST
11.69 Tax (sb.)
11.71 IncoME
11.72 EXPENSE, Cost
11.73 Prorit
11.74 Loss
11.75 Lease, Rent (to Another) 11.76 Rent, Lease (from Another) 11.77 Hire (vb., a Person) 11.78 Wacss, Pay
11.79 Earn
11.81 Buy
11.82 SELL
11.83 Trav (vb.)
11.84 Mercuant, TRADESMAN 11.85 Market (Place)
11.86 Srorz, SHOP
11.87 Pricr
11.88 Dear (=Costly, Expensive) 11.89 CHmap
739
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and e
{ ? | |
740 SELECTED INDO-EUROPEAN SYNONYMS
11.11 HAVE Grk.  &w Goth. haban (aigan) Lith.  turéty NG &w ON hafa Lett, but with dat.; turgy Lat. habére Dan. have ChSl.  tmetz , It. avere Sw. hava SCr.  imati Fr. avoir OE habban Boh. mitti Sp. tener ME shave Pol. miéé Rum. avea NE have Russ. prep. u with een Ir. phrase with ‘be’ Du. hebben imel! ” NIr. phrase with ‘be’ OHG habén Skt. as- or bhi- with gen W. phrase with ‘be’ MHG haben Av. —_ah- with gen, ; Br. phrase with ‘be’; NHG haben
kaout
There is considerable overlapping of sense among the verbs listed in 11.11- 11.17. There is no sharp line between the colorless ‘have’ and the stronger ‘own, possess’. ‘Have’ is mostly from earlier ‘seize, take hold of’, ‘hold’, or ‘take’, which are again closely allied with each other and in part with ‘get, ob- tain’ and ‘keep, retain’.
The oldest method of indicating sim- ple possession, and doubtless that of the TE period, was by means of a phrase containing the verb ‘be’, expressed or implied, with an oblique case for the person. This is common enough even in languages which also have verbs for ‘have’ (Grk. pot gor, Lat. mihi est, etc.), and is the normal type in Indo- Iranian, and in the Celtic languages down to the present day.
The secondary use of verbs for ‘have’ as auxiliaries, esp. for past tenses, but also for future and ‘must (9.94), is not considered here.
Cf. Meillet, Le développement du verbe “avoir”, Festschrift Wackernagel, 9 ff.
1. ‘Have’ regularly expressed by phrases. Ir. rotbia less log dodaggnima lit. ‘reward shall be to thee with him of thy well-doing’ (Wb. 6a11), or using a prepositional phrase, is ed inso fil lasuide lit. ‘it is this that is with him’ (MI. 63d4), or, taking NT, Jn. 4.17, otk exw
avépa is rendered by NIr ni Shuil fear agam, W. nid oes gennyf wr, and Br. nem eus pried ebet ‘there is not a hus- band to me’; so also Lett. man vira nav, Russ. u menja net muza ‘there-is-not a husband to me’. Skt. as- or bha- with the gen. may be ‘have’ or ‘own’, cf. tasya gatam jaya babhuvur ‘he had a hundred Wives’, or manor ha vd rsabha asa ‘Manu had a bull’ (cf. Delbriick, Altind, Syn- tax 162), and similarly, Av. agava dana .... yd hanti spantahe mainysué ‘those creatures....which the holy spirit possesses’ (Yt. 6.2), also with omission of ah-: vahista i84& sradvi zarabustrahé ‘Zarathustra has the best good known���, lit. ‘optimum bonum auditum (est) Zarathustri’ (cf. Reichelt, Aw. Gramm. 253; Barth. 269).
2. Grk. éw ‘hold, possess, have’ : Skt. sah- ‘be able, be powerful, overcome, be victorious’, Av. haz- ‘take possession of, gain’, Goth. sigis, etc. ‘victory’. Walde- P, 2.481 f.
3. Lat. habére (> It. avere, Fr. avoir, Rum. avea) earlier ‘hold’, whence ‘oc- cupy, possess’ and finally ‘have’ : Umbr. habitu, habetu ‘habeto’, but the older sense in haburent ‘ceperint’, etc., Ir. gaibim ‘take, seize’, W. gafaelu ‘hold, grasp’ (10.14), perh. Lith. gabenti ‘carry off, transport’, IE *ghab(h)-. Walde-P. 1.344f. Ernout-M. 442. WaldeH. 1.630 f.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Gangotri 4
{ }
tized by Arya Samaj
Lat tenere hold’ (11.15). | ‘get, find’, etc.
te., general Gme. ; ae) Goth. hafjan, Lett. kampt ‘seize, 342 ff. _ Walde-P. 1,342: Falk-Torp 386. Feist
.
n renders Grk. éxw In ex- as father’
Lk. 20.33,
p ‘ to wie 38, nave the general
Me. 19,93), but represents
In most cases any expression for ‘have’ may be used also for ‘own, possess’ if the context shows that the re- lations ip is one of enduring (or legal, ete.) nature, as opposed to the tempo- Fy alire notion of ‘h
```


## [2026-09-14T02:32:05.671Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"t[aā]iiu\\|tāyu\\|taiiu\\|'Dieb'\" BRT.txt | head -20; echo \"=== grep Dieb ===\"; grep -n \"Dieb\" BRT.txt | head -20"
}
```


### [2026-09-14T02:32:05.787Z] TOOL RESULT

```
12012:•  j.,  g.  taya-  i)  Adj.  '(diebisch  sva.)  ver- stohlen, heimlich':  yS  frasäi^A.)  ävllyä  yä va..*p3r?saaiya(^Va.)\.3i.i^.  2)  m. a)  'Dieb':  'yaY.18.  b)  'Diebstahl'!?): °yS^'>  F.  25  b,
12182:•  j.  täyav-  m.  'Dieb':  aü  haeai»uha *anak3sf{sA.)°yuS"üSea&.ci\:  ein  Räuber, beimlidii  ein  Dieb"''  N.6;  63';  —  '^u/ .  .  hazattha  .  .  ga%0  Y.  65.8;  —  'yus mmanhs  (sd.)  .  .  hatattha  tamS.barahe V.  4. 1 ;  —  'yunamca  hatasnamca  Y.  61. 3 ; yt.6^,4,  /2.8; —  'yßm  ptSjär»n  Y.1/.3; —  raimiS  ari^amal  bairista  .  .  '^iß»! ni/aynisia  ¥1/2.7;  —  *'''  -i^CnäinLjfiÄflÄ^) ^nAn  ^a^fl  'yae/  V.ij.^n;  47S;  — _>'<Mii Ai/  . .  °yu/  vä  vthrkö  vä  apaiti.busH  para.- baraiti  dasa  (sd.)  \. 13.1a;  40; — paurva 'yüm  .  ,  gaojm  .  .  vihrkfm  bnhydimatoe Y.p.ai.
13076:fi^n/^a-  (sd.):  'mff  zaota  taiiu.p>r3ia  upa.- jrao/ärii  {sd.)  N.j#;  jf)i;  —  y^  hmcU 'maiiqm  \_apjrynäyunqm]i>  aibm  (sd.)  dasli . .  nairiiqm  vä  * aptnnaysk^m  va  astsm dasti  .  .  daivayasnnn  vä  tanu.pirütgm  vä asbtrt  dasti  N. /05;  —  cvai  aisqm  upa.- manaym  (sd.)  . .  cval  "manqm  cvat  tanu.- p^nhanqm  V.  12.  i .
13313:•  j.  *däitim''  Inf.  'zu  geben,  zu  verleihen': vasa%a  aht  xiayamna  taiiuye  x''an»at»Ae''> d'  "nach  Gefallen  vermagst  du  deinem Leibe  Herrlichkeit  zu  verleihen"  Yt  ly.  1 5  3>.
13850:ai,  vg\.di^ii;  dutJii- Ad}.;  np.diarf'Dieb'l?), —  Pü. !  duidätiät.  Sä.:  dustajääm;  (zu  V,  /); duSdSyäi(f),  erl,;  /a  afarStäh  dät  iitet.  — ')  S  3^3,  410,  414.  —  ')  Hds.  duidqfjirö;  i. aber  Bd.  38.  23.  —  3)  Eine  merkwürdige Sentenz.  Bd.  28.  23  Hesse  einen  etwas  andern Text  erwarten.  Pü.:  fehlt,  —  «)  PQ.  erl.:  fa anäklh  pa  dämän  i  SMrmaad  iartan  hävand hunuSak  u  zurät  menäk  hind.  Vgl.  dl^eg«n Y.  4$.  6:  hudi  ySi  kinlS.  —  9  Them.
25636:gAw.:  aya  *arSi  käkur^iam  (sd.)  yayi haantt  'vqnö  y.3S-9'  —  mainyB  ..yaya sf>anya  (sd.)  Hilf  mravat  ySm  angnm: rtsit  fta  manä  .  .  sSngka  ,  .  xratavS  .  . varanä  (sd.)  . .  vxha  . .  syaehanä  . .  daini . .  'vqnS  Aacainti'S..4S- '.  b)  im  jAw.: ahurake  masdä  . .  yaiAe  'va  ma^rd  spmts Yt/J.  81,  V. /p.  14;  —  amisanqm  spmla- »am  ..yalsqm  ainyS  ainyeAe  'varam  aiwi.- vainaiti  m^ri^iomt^m  Aumataiiu  .  .  Yl j^.  83f.  3)  bei  Tieren;  a)  im  gAw.: aAmakSng  (s.  I)  äat  'unS  pasukanqm(sA)^ ysi  na  Jißänti  Y.jg.  t;  —  daüiAanqmca aidyünqm  Ayat  'unS  yasamaidi  Y.  519,  2 ;
29780:daroä  . ,  alä  'zs  smavai  "schenk  . .  durch  ! As'a  starke  Gewalt"  Y.33. 1 3 ;  — gartma  (sd.) , ^rS  hyat  .,  vartAsui  'tS  jtmal  matiat»As\ ". .  die  Macht  des  guten  Sinns  '>  . ."  Y.  .  j.  hahya-  Adj.  'der  es  mit  dem  Getreide, 4-3- ^-  3)  'Gewalt,  Gewalttat':  5a/ /i   der  Getreideerate  zu  tun  hat,  fnimentaiius',
=== grep Dieb ===
4400:•  j.  an-äkih-  Adj.  'unsichtbar'  sva.  'der sich  (dabei)  nicht  sehen  lässt,  es  heimlich tut':_j'ajrä  altaliqm. .  anahaxta {%A.)  para- baraiti  nöit  täyus  nSit  hasanha  bavat .  . ainy5  kasHl . .  para.baraiti  aka  *haza»ha '"^iw"  (NS.)  täytis  "-  .  nimmt  irgend  ein andrer  (davon)  weg,  (so  ist  er)  ein  Räuber, wenn  er  es  offenkundig,  ein  Dieb,  wenn er  es  heimlich  tut"  N.6j'>;  — '"frsit.varS paratihacäiti  äka  hazauuha  **käs.)^^  täyus
12012:•  j.,  g.  taya-  i)  Adj.  '(diebisch  sva.)  ver- stohlen, heimlich':  yS  frasäi^A.)  ävllyä  yä va..*p3r?saaiya(^Va.)\.3i.i^.  2)  m. a)  'Dieb':  'yaY.18.  b)  'Diebstahl'!?): °yS^'>  F.  25  b,
12013:Ableil.  (s.  'liiya-).  —  lEt.  s.  */äyii.'a-.  —  taya- *diebisch;  Dieb' (mit  Schwaslufeji  'tJya-  'Dieb- stahl' =•  ai.  vf-dkä-  :  vardha-  (usw.,  B.  JScHUinT riur.  391).  —  Pü.  (zu  1):  tiihäaik,  (zu  3  a): duzd,  (lU  2  b)i  tir/l  »>,  erl  1  duäilAä  dr/l.  — ')  Lies  läyö  (lu  ^/äya-)}  S.  No.  Z.  —  »  D.  i. 'Diebstahl',    s.   die  vAbleit   tirßenllan   unter
12106:Vgl.  ai-  'Irt-  Adj.  'stehlend'  (KZ.  35.  311). mp.  lirß*)  'DiebsUhl';  alles  übrige  (Horn NpEt.  86,  Hbm.  PSt  185)  ist  unsicher.  — Pü.:  HrflFnUan').  —  ')  Statt  bn/y',  %  368. 39.  —  ")  Vgl.  zu  taya-  und  l^vis:  Wie  zu lesen?  Wl.  Iri/t°,  Analogiebildung  nach^r^* (IF.  II.  ia6),  wenn  man  annehmeD  darf,  dass air.  *lffjati  zu  mp.  'Grcl  führte,  wie  "g^iiaii zu  gira  (IF.  12.  107).
12177:•  j.  'täjra-  m.  Diebstahl':  ui  gSus  stuyi 'jSaica  h^aatihalcS  Y.  12. 2.  [S.  noch /ay^  F.  25  b.  '>j
12180:•  j,  "tiya-  Adj.  (fem.  yä-}  Vod  einem  1 Dieb  herrührend' :  yiu(a  tni  'y&sca  ..  tac- 1 Jz-i  frabaräl  P.  22.  |
12182:•  j.  täyav-  m.  'Dieb':  aü  haeai»uha *anak3sf{sA.)°yuS"üSea&.ci\:  ein  Räuber, beimlidii  ein  Dieb"''  N.6;  63';  —  '^u/ .  .  hazattha  .  .  ga%0  Y.  65.8;  —  'yus mmanhs  (sd.)  .  .  hatattha  tamS.barahe V.  4. 1 ;  —  'yunamca  hatasnamca  Y.  61. 3 ; yt.6^,4,  /2.8; —  'yßm  ptSjär»n  Y.1/.3; —  raimiS  ari^amal  bairista  .  .  '^iß»! ni/aynisia  ¥1/2.7;  —  *'''  -i^CnäinLjfiÄflÄ^) ^nAn  ^a^fl  'yae/  V.ij.^n;  47S;  — _>'<Mii Ai/  . .  °yu/  vä  vthrkö  vä  apaiti.busH  para.- baraiti  dasa  (sd.)  \. 13.1a;  40; — paurva 'yüm  .  ,  gaojm  .  .  vihrkfm  bnhydimatoe Y.p.ai.
12186:•  j.  *üiyuäa-''  m.  strafrechtlicher  Terra, techn.,  wahrscheinlich  für  den,  der  bei einem  Diebstahl  als  Anstifter,  Gehilfe  oder Begünstiger  (Hehler)  beteiligt  ist;  'sasla (NP.)  F.  25  b.
12219:VgL  IrvSi-.  —  Pü. !  är/lär  -  Sü. :  slenai^  -,  eri. : tum  afi  duidel;  s.  dazu  Bthl.  IF.  g.  370, Meillzt  Jouto.  des  Sar.  igoa.  38S  {,  der  in Irviilä  eine  graphische  VeratüniQelitng  von *laydM  -  lu  läyair-  -Dieb'!  S  394-  3  -  findet. Aber  I.  ut  mir  ein  zweiter  Fall  solcher  Schrei- bang  nicht  bekannt,  s.  dagegen  %  368.  14, wozu  noch  afiii;  3,  verlangte  ich  dos  Ab- straktam.  Gegen  den  Ansati  eines  'lävi!-  n. IHebitahr  sprechen  die  verwandten  Worte, die  auf  *iäi-  -  s.  in  *läyula-  -  weiten).
13021:•  j.  dasa-  n.  'Gegenstand  der  fahrenden Habe,  Vennögensstlick'"*:  yaa  .  .  layul vS  Vfhrkö  vä  haca  gai%abyS  paraMaraiti •sa  (AP.)  "wenn  ,  .  ein  Dieb  oder  Wolf aus  dem  Anwesen  fahrendes  Gut  fort- schleppt" V.  13.10.
13850:ai,  vg\.di^ii;  dutJii- Ad}.;  np.diarf'Dieb'l?), —  Pü. !  duidätiät.  Sä.:  dustajääm;  (zu  V,  /); duSdSyäi(f),  erl,;  /a  afarStäh  dät  iitet.  — ')  S  3^3,  410,  414.  —  ')  Hds.  duidqfjirö;  i. aber  Bd.  38.  23.  —  3)  Eine  merkwürdige Sentenz.  Bd.  28.  23  Hesse  einen  etwas  andern Text  erwarten.  Pü.:  fehlt,  —  «)  PQ.  erl.:  fa anäklh  pa  dämän  i  SMrmaad  iartan  hävand hunuSak  u  zurät  menäk  hind.  Vgl.  dl^eg«n Y.  4$.  6:  hudi  ySi  kinlS.  —  9  Them.
14050:Et  und  eig.  Bed.?  —  Pü.:  dräi  (transskr.), erl. ;  /  dänil  ku  :  *duidii  ne  apäyit  katlan,  api pa  e  dSrft  iu :  ka  hat  luväniiän  duidrm  u  ö drijöiäa  dahim,  am  karpai.  —  ')  Nach  PüErl. Diebstahl  bei  Reichen  zum  Zweck  derllnter- siaizang  Armer.
16556:i)  'sentire,  wahrnehmen,  gewahr,  inne werden':  paurva  täyüm  .  .  bBtiySimatiie mä  äs  paurvö  baioyaita  nS  vlspe  paurva büi'tySimaihe  "zuerst  möchten  wir  des  Diebs gewahr  werden  ,  ."  Y.  ^.  21;  —  a'ira pas^aSa  vaosirim  (sd.)  baoi>ntS  lufDirt tarmmSa  "..  sentientes  famem  sitimque" Yt.  if).  69;  69;  ~  baelff  (NS.)  vlöwS aiihtiiä  (sd.)  V.76'67.  a)  Kaus.  'zu  er- kennen geben':  haemö..yakmäi  kvar>  därät tamö  baoöayeiti  Yt  10.  90.  2)  'riechen
16954:•  j.  {,  g.)  bairiäta-  Adj.  'der  am  besten pflegt,  hegt  (usw.)',  mit  Akk.:  rainvS arvhamat  (sd.)  'ta  .  .  täyüm  nijaynisla "o  Ji.,  der  du  dem  Beklagten  am  besten betstehst,  . ,  den  Dieb  . ."  Yt.  12. 7.
17832:—  41  Im  Mp.  heisst  das  Fat  yravar/iiän,  TOn Menander  als  HKUm  'Totenfest*  beieicbnet ^eLacardr  GesAbh.  161).  —  il  DiebeiDsT. ZA.  2.  501  vorgeschlagene  Deutung  halle  ich für  durchaus  verfehlt;  lEt.  des  np.farvnräan s.  GIrPh.  /.  359,   7  b.  49.  —   *)  Woraus  np.
18609:•  j.  'nava  Psut  'durchaus  nicht,  überhaupt nicht,  sicher  nicht,  keineswegs':  kä  filasti Li>af  ..tf  he  asii  ä^a  tf  ke  asti  äp^ntii iiC-it  kl  asti  yaotdairym  "Vas  ist  die  Sühne dafür?  .  .  Es  gibt  dafür  überhaupt  keine Sühne  .  ."  V.  j,  39;  —  yS  mqm  . .  dära- yeiä  yaia  täybm  pfssaärtm  n'  ahmt p>sS.- sUrö  ".  .  wie  einen  todsündigen  Dieb;  und ich  bin  doch  sicher  kein  Todsünder"  Y. //.  3;  —  tum  afi-a  ..  anaiivySstis  kunahi .  .  «•  as3m  .  .  anaiwyäsfil  kunämi  "ge- bierst du  denn  . .  ohne  Begattung?  . . Ich  getäie  keineswegs  ohne  Begattung" V.  /<V.  31;  —  yaf  . .  yu:rtanqm  . .  /ratjm?m '^anjayeni  (sd.)  .  .  *«'  */rä~i:w>nsäma  ** razunm  (sd.)  Yt.  5.  50;  l^.  ti  "'.  nava.- ci!  sbes.
18975:•  j,  'n«inah-  n.  'Darlehen':  yS  natre  n»- mataAgnte  nBit  'mS  paitiiaraiti  täyus 'mariAs  bavaiti  AazaaAa  ivms.baraA£  "wer einem  Darleiher  das  Darlehen  nicht  wieder- gibt, wird  zu  einem  Dieb  des  Darlehens, zu  einem  Räuber  am  Darlehnsgeber"  V, 4.1.
27197:1)  'haftenaß-' (Dat):  nSi^ *Ai/iu (sd.) iiiivsi  sraiiyäti  "Trocknes  wird  nicht  an Trocknern  haften"  V.  8. 34.  2)  'sich heften  an  -  (Akk.)  sva.  nachgehen,  ver- folgen'; yö , .  hala  gaiisabyS  paraiti  srai- hmns^^  tayol  v)hrk)mca  "wer ..  weggeht in  der  Absicht  die  Diebe  oder  den  Wolf zu  verfolgen"  V.  13. 1 7.
```


## [2026-09-14T02:32:13.872Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"stena\\|tāyú\\|tayu\\|11.57 THIEF\" SYN.txt | head -20"
}
```


### [2026-09-14T02:32:13.944Z] TOOL RESULT

```
1755:OE stenan (cf. NHG stéhnen), Lith. stenétz, ChSl. stenatz, all meaning ‘groan’, Skt. stan- ‘roar, thunder’, Lat. tonare ‘roar, thunder’. Walde-P. 2.626 ff. Er- nout-M. 1045f. REW 8778, 8780. Falk-Torp 1273.
9235:Fr. viande, ‘meat’ (chair ‘flesh’), orig. ‘food’ (cf. NE viands) fr. Lat. vivenda ‘means of life, sustenance’. REW 9410.
11882:Grk. _—_retxos} rotxos, retxlov Goth. -waddjus Lith. miras; stena NG TotxXos ON mirr; veggr Lett. miiris; siena Lat. mitrus, moenia (pl.); Dan. mur; vag Chl. zidit, sléna paries Sw. mur; vdgg SCr. id, stijena It. muro; parele OE weall; wag Boh. zed’; sténa Fr. mur, muraille ME wall (waw) Pol. mur; Sciana Sp. muro; pared NE wall Russ. stena Rum. id; pdrete Du. muur; wand Skt. dehi-, prakdara-; ky- Ir. mur; fraig OHG mira; want dya~ NIr. muir; falla (fraigh) MHG mir(e); want Av. uzdaézi- W. mur, gwal, magwyr; NHG mauer; wand pared Br. moger
11909:5. Lith., Lett. stena : Lith. sieti, Lett. siet ‘bind’, Skt. sd-, si- ‘bind’, etc. Walde-P. 2.463 ff.
18721:11.57 THIEF
20069:11.57 THIEF
20080:Ir. tadid; ChSl. tatt, ete.; Skt. tayu- (RY), also stayu-, Av. ta@yu-, Skt. stena-; ef. ChSl. taj ‘secretly’, tajiti ‘hide’, Grk. tnrdopar “be in want, bereft of’, Hitt. tdyézzi ‘steals’ (Sturtevant, Hitt. Gloss. 157).
20101:8. Skt. stena-, tayu-, slayw, Ay. tdyu-, see above, 1.
28546:; Goth. swégatjan Lith. stenetz gre, OT evdto ON slynja Lett.  stené orev bfo Dan.  stgnne ChSl.  stenati gemere Sw. _—sténa SCr. _ stenjati gemeré OE granian, stenan Boh. _ stenati gémir ME grone Pol. jeczec, stekaé
28556:Grk. crew, orevatw; ON stynja, Dan. stgnne, Sw. sténa, OE stenan, MLG stenen, Du. stenen, MLG stonen, Du. steunen, NHG (fr. LG) stéhnen; Lith. stenéti, Lett. stenét; ChSl. stenati, etc., general Slavic; cf. Skt. stan- ‘roar, thun- der’, and without s- Lat. tondre ‘thun- der’, OF punor, etc. ‘thunder’.
28567:ON stynja, OE stenan, etc., above, 1.
28574:5. Lith. stenéti, ChSl. stenat; (Supr,; in the Gospels crevatw is rendered hs vydychati ‘sigh’), etc., general Balto- Slavic, above, 1.
31163:6. ChSI. tajinii, etc., general Slavic, beside taj adv. : tatt ‘thief’, Skt. (s)tayu-, Av. tayu- ‘thief’, Av. taya- ‘secret, fur- tive’, sb. ‘thief’, etc. Walde-P. 2.610.
32918:Grk. — 8pos, Sptov Goth. marka Lith. stena (rubezius, riba)
32953:5. Lith. stena ‘wall’ (7.27) and ‘boundary’ (now the preferred- word, Senn).
```


## [2026-09-14T02:32:19.269Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '20060,20105p' SYN.txt; echo \"=== page markers ===\"; awk 'NR>19950 && NR<20120 && /^[0-9]{3}$|SELECTED INDO-EUROPEAN/' SYN.txt | head"
}
```


### [2026-09-14T02:32:20.385Z] TOOL RESULT

```
6. ChSl. krasti, etc. general Slavic, prob. : Lett. krdé ‘collect, heap up’, with labial extension Lett. krapt, Lith. kropti ‘deceive’, root *krd(u)- in Lith. krauti ‘heap up, load’, etc. Walde-P. 1.477. Berneker 605. Briickner 264 f.
Russ. vorovat’, fr. vor ‘thief’ (11.57).
7. Skt. mus-, prob. : Frank. (Lex Sal.) chreo-mdsido ‘corpse-robbery’, and fr. an extension of IE *meu- in Lat. movere ‘set in motion, move’, Skt. miv- ‘shove, press’, etc. Walde-P. 2.253.
Skt. cur-, etym.?
Av. tarap- (trafya-) : Skt. irp- in pacu-trp- ‘cattle-stealing’, root connec- tion? Walde-P. 1.737. Barth. 648.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
¢ :
Digitized by Arya Samaj Foundation Chennai and eGangotri
790 SELECTED INDO-EUROPEAN SYNONYMS
11.57 THIEF
Grk. —_xAéxrns, dcop Goth. piufs, hliftus Lith. vagis
NG Kerns ON Ajofr Lett. zaglis
Lat. fiir Dan. tyv ChSl.  tatt
It. ladro Sw. uf SCr. tat, kradljivac
Ir. voleur (larron) OE péof Boh. —zlodéj, kradce
Sp. ladr6n, hurtador ME _eitheef Pol. 2lodziej
Rum. ho{ NE thief Russ. vor (tat’)
Ir. taid, merlech Du. dief Skt. slena-, céura-, mosq NIr. gadaidhe OHG  diob eae, Udita ok eas W. — leidr MHG diep Av. layu- de Br. laer NHG dieb
Several of the words for ‘thief’ are derived from those for ‘steal’, as in part conversely. But more often there is no connection, as in the Gme. group (NE steal, but thief). Several of the words for ‘thief? were originally more general terms for ‘evildoer, rascal, bandit, rob- ber’, etc.
1. TE group based on “*(s)lai-. Walde-P. 2.610.
Ir. tadid; ChSl. tatt, ete.; Skt. tayu- (RY), also stayu-, Av. ta@yu-, Skt. stena-; ef. ChSl. taj ‘secretly’, tajiti ‘hide’, Grk. tnrdopar “be in want, bereft of’, Hitt. tdyézzi ‘steals’ (Sturtevant, Hitt. Gloss. 157).
2. Grk. xdérrns, NG xdédbrns : KAérrw ‘steal’ (11.56).
Grk. ¢ap (Hdt.+-), as ‘one who car- ries off? : Grk. gépw, Lat. ferre ‘carry’. Walde-P. 2.154 ff.
3. Lat. far, either cognate with or loanword fr. Grk. ¢&p. Ernout-M. 403. Walde-H. 1.569.
It. ladro, Fr. larron, Sp. ladrén, fr. Lat. latr6 ‘mercenary soldier’ (so in Plaut., class. also), ‘bandit, highway- man’, loanword fr. Grk. N&rpov ‘pay, wage’, Aazpets ‘hired servant’, etc. Er- nout-M. 527. Walde-H. 1.771. REW 4931.
Fr. voleur, fr. voler ‘steal’ (11.56).
Sp. hurtador, fr. hurtar ‘steal’ (11.56).
Rum. hot, also ‘robber, rascal’ and
prob. orig. a general abusive term, but source unknown. Tiktin 739.
4. Ir. laid, see above, 1.
Ir. merlech, fr. merl ‘theft’, etym. dub. (: mairnim ‘betray’?). Pedersen 2.55.
Nir. gadaidhe, fr. gadaim. ‘steal’ (11.56).
W. lleidr, Br. laer, fr. Lat. latrd. Loth, Mots lat. 181.
5. Goth. piufs, OE péof, OHG diob, etc., general Gme. : Goth. Aiubjé ‘se- cretly’, and so perh. as ‘cowering, crouching’ : Lith. twpéli ‘cower, squat’, Lett. tupt ‘squat’. Walde-P. 1.714. Falk-Torp 1310 f. Feist 497.
Gorh. hliftus : hlifan ‘steal’ (11.56).
6. Lith. vagis: vagiu, vogli ‘steal’ (11.56).
Lett. zaglis : zagt ‘steal’ (11.56).
7. ChSl. tatt, SCr. tat, Russ. tat’ (obs.), see above, 1.
SCr. kradljivac, Boh. kradce, fr. Slavic krasti ‘steal’ (11.56).
Boh. zlodé, Pol. ztodziej = Russ. zlodej ‘villain, rascal, wretch’, ChSI. ztilo- déji ‘evildoer’ (zitlit ‘evil’ and déti ‘put, place’). Berneker 193. Briickner 654.
Russ. vor : Pol. wér, Boh. vor a kind of ‘sack’, SCr. verati ‘stick away, hide’ Lith. verti ‘open or shut’ (Trautmann 351f., without Russ. vor), ete. Miklo- sich 382. Brickner 631.
8. Skt. stena-, tayu-, slayw, Ay. tdyu-, see above, 1.
Skt. caura-, fr. cur- ‘steal’ (11.56).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
pOsSESSIO
» ‘hese differ
=== page markers ===
786 SELECTED INDO-EUROPEAN SYNONYMS
787
788 SELECTED INDO-EUROPEAN SYNONYMS
790 SELECTED INDO-EUROPEAN SYNONYMS
```


## [2026-09-14T02:32:26.431Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"thief\" SOD_pages.txt | head -20"
}
```


### [2026-09-14T02:32:26.489Z] TOOL RESULT

```
13598:     thief
15266:       thief,
15357:                                                                               thief
31199:     (ro)cut, 0o)dig                                              thief ©<Av. tayu ©pi. -f; ob. pi. -ty =»t>yh, ty3
31226:     thief
31860:     thief
39668:thief 3441, 4052, 4091, 9514, 9518,       9265, 9268, 9279                         10701, 10705
```


## [2026-09-14T02:32:29.389Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '31180,31240p' SOD_pages.txt; echo \"=== leaf ===\"; python3 - <<'EOF'\nd=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if '<Av. tayu' in p:\n        print('leaf',i,'printed ~',i-66)\n        print(p[:200])\nEOF"
}
```


### [2026-09-14T02:32:30.545Z] TOOL RESULT

```
                                                                  SCE 10; Hen. Tales. 472.30; BSOAS 12, 307.58;
9499 t's M                                            *>.y
     tas ©Av. taszm-daru                                            GMS 1068, 1641; STii 5.13, 6.16; BSTi 170;
     tablet                                                         Hen. BSOAS 11.702; STSC 133.24; Frag. Len.
     BBB 527                                                        98a 1; MSP b30; BSTii 858.13, 882.5, 827.45: C2

9500 t>s- B, M                                                      gloss. p227; ace. t>wntw, C2, 69 R22
                                           0*~*Ji&u>.
     tas=*ts
           ©<Av. tas; Pahl. tasidam% Khot. ttds              9512 tNvnt C =» t>w>nt(t)
             ycq
                                                             9513 tVnty* C                                  j^^y
      (to)cut                                                     tawandy* (t'w'nty) ^tVndyfy), t}wnc, t}wndqy}
      TSP 2.116, 514, 537, 538; GMS 637; Frag. Len.
        37.7                                                      STii 4.10
                                                                  power
                                                             9514 tV B, M                                     jju. oj>
9501 t*s- M                        ojS i&J'klj loXji
     tas,tes ? =»t}s-, ts-                                        tay
     (ro)cut, 0o)dig                                              thief ©<Av. tayu ©pi. -f; ob. pi. -ty =»t>yh, ty3
     Sund. Man. Lett. 305.19; GMS 637                             TSP 2.1113, 7.138, 24.2; Hen. Tales. 478.2.30,
385

        478.6; Mack. BSOAS 1984, 534                           9528 8b>r C                                            -uja
                                                                                                                   8brt-
9515 ty B, S      • JL*. j& ttsJj*- ^>*jjj -'j <>■**                 OPar ©ob. -y ^Ob^qy*, 8p>r
     tay ©Skt. ayatana ©pi. -t                                       gift, giving
     entrance(/c»r sense organs)                                     C2, 51V28
     TSP 2.1043 etc.; Frag. Len. 103R2; Mack. BSTBL,           9529 8b»r ywz C                           \jf «£ju> jl=J ^
       Notes pl5.15                                                  G^r-xoz
                                                                     asking for alms, beggar
9516 tywny      B, S                           cJ^<^>
                                                                     STi 42.4; GMS 57 n 1, 921; Gersh. Sogd. Cpds.
      tayune, tayoni (t}ywnyy, t}ywny)                                 1945, 144.5
      theft
      TSP 9.15; BBB plOO e 6, GMS 1087; Frag. Len.             9530 BbVqy* C                      ^Sia^ijjl**
        98a-l5Sund. AI28, 1988, 185                                 eparakya (Gbr^y*) -»brqy\ y^-Gbr^y'
9517 t>y>yck> B                               J*i<J>»                STii 3.39; BSTii 895.52, 893.3; C2, 31V25, 54V22,
     tay-ick
     stealthily                                                        57V9; pi. -yu C2, 31V3; C2 p77.25
      VJ 339; GMS 1013; Benv. JA 1955, 330                     9531 Bb'rxwzqy' C                                    ^Jjf
                                                                    8par-xozakya
                                                                       gift
                                                                    beggary
9518 t»yh#B                                      ^
     tay ©Av. tayw, Khwar. tah% MP tay -»ty3, ty                     BSTii 886.9: C2, 51V9
     thief
                                                               9532 tbr- C                                      b>J^>
      VJ 239; Benv. HitUE. 115
                                                                     tipar ©Yaghn. divan Av. aiti-bara% Khwar.
9519 t}yw»k B                             -*V«»s
                                                                      cfir- ©impf. tybr «»tybr-
     taywak, tewak (^yw'kCk)) ©pi. -f; ob. pi. -ty                  (fo)insert
       «*tyw}k(k)                                                   S W, C2 pl32, 60V6
     child
                                                               9533 Bbr- C                                              ^b
      GMS 991; t}ywl})kt, VJ pl20; used always with                  9par   (tbr-) ©<*fra-bara-     ©impf. 0}br, t}br
        pi. -t(h), -ty, t>ywk, Anc. Lett. 2.50
                                                                      =»9brt-, 6>br-, 6p>r-, Spr-1
9520 t}yw>qcyk M                                       «&*,         (ro)give
     taywak-cik =»tyw}qmync                                         GMS 492, 592; C2 gloss. p228; STii p597; trans.
=== leaf ===
leaf 451 printed ~ 385
 t'r'kp'zn                                                                                                          384


9489 tVkp'zn B                             J*Xjt tj^         9502 t'w B, M, C
```


## [2026-09-14T02:32:42.372Z] TOOL CALL #40: Bash

```json
{
 "command": "pdftoppm -f 475 -l 475 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg475 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg475.png"
}
```


### [2026-09-14T02:32:44.232Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 67658 Sep 13 22:32 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg475.png
```


## [2026-09-14T02:32:45.072Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D8%A7%D9%86%D8%AF%D8%A7%D8%B1%D8%AF/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for استاندارد verbatim, including the bracketed origin tag (e.g. [فر.] or [انگ.]), and any other dictionary's etymology note."
}
```


### [2026-09-14T02:32:48.497Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for استاندارد

According to the Farhang-e Mo'in dictionary included on this page:

"( اِ ) [ فر. ] (اِ. ) نمونه تصویب شده ، قاعده ."

This entry indicates the word is borrowed from French (marked with [فر.]), and defines it as an "approved model" or "rule."
```


## [2026-09-14T02:32:52.763Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%B7%D8%A8%D9%84/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for اسطبل verbatim including the bracketed origin tag (e.g. [یو.] Greek, [ع.] Arabic, [لا.] Latin), and any other etymology notes (دهخدا, عمید)."
}
```


## [2026-09-14T02:32:53.412Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg475.png"
}
```


### [2026-09-14T02:32:53.957Z] TOOL RESULT

```

```


## [2026-09-14T02:32:53.932Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


### [2026-09-14T02:32:57.334Z] TOOL RESULT

```
# فرهنگ معین Entry for اسطبل

The webpage does not include a specific entry labeled "فرهنگ معین" (Mo'in Dictionary) for اسطبل. 

The available dictionary entries shown are:
- **لغت نامه دهخدا** (Dehkhoda)
- **فرهنگ فارسی** (Persian Encyclopedia) - which notes the word comes from Greek *طویله* and means a stable or resting place for quadrupeds
- **فرهنگ عمید** (Amid Encyclopedia) - defining it as "جای سرپوشیده برای نگه داری چهارپایان، به ویژه اسب، طویله" (a covered place for keeping quadrupeds, especially horses)

Unfortunately, the Mo'in Dictionary entry you're requesting is not displayed in this particular web page content.
```


## [2026-09-14T02:33:22.566Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN stable ===\"; grep -n \"stabulum\" KLN_1966.txt | head -10; echo \"=== KLN standard ===\"; grep -n \"^standard\\|standard,\\ n\\.\" KLN_1966.txt | head -5; echo \"=== SKT ===\"; grep -n \"stabulum\\|estandart\\|estandard\" SKT.txt | head -10; echo \"=== LKT ===\"; grep -n -i \"istabl\\|stabulum\\|Stall\" LKT.txt | head -10"
}
```


### [2026-09-14T02:33:23.530Z] TOOL RESULT

```
=== KLN stable ===
8865:conspuc,  tr.  v.,  to  spit  upon  in  contempt,  assail. —  F.  conspuer,  ‘to  spit  upon,  despise,  to  decry’, fr.  L.  conspuere,  ‘to  spit  upon  in  contempt’,  fr. con-  and  spuere,  ‘to  spit’.  See  spew  and  cp. sputum.  Cp.  also  cuspidor, constable,  n.,  peace  officer.  —  ME.,  fr.  OF.  cone- stable  (F.  connetable),  fr.  Late  L.  comes  stabuli, lit.  ‘count  of  the  stable’,  fr.  L.  comes,  ‘com¬ panion’,  and  genitive  of  L.  stabulum,  ‘stable’. See  count,  ‘title  of  nobility’,  and  stable, ‘stall’.
36519:Derivatives:  stable-ness,  n.,  stabl-y,  adj. stable,  n.,  a  building  for  horses  or  cattle.  —  ME., fr.  OF.  estable  (F.  Stable),  fr.  L.  stabulum,  ‘stable, stall,  lair,  hut’,  which  stands  for  *sti-dhlo-m  and lit.  means  ‘a  place  for  standing’,  from  the  stem of  stare,  ‘to  stand’.  See  state  and  cp.  the  second element  in  constable.
36526:sense  development  cp.  the  cognate  L.  stabulum, ‘stable,  stall’,  from  the  stem  of  stare,  ‘to  stand’ (see  stable,  n.)
=== KLN standard ===
11301:standard  major  or  minor  scale,  without  chrom¬ atic  variations  (music).  — -  F.  diatonique,  fr.  L. diatonicus ,  fr.  Gk.  Skxtovixo^,  fr.  Siazovoq,  ‘ex¬ tending;  pertaining  to  the  diatonic  scale’,  fr. SiaxEiveiv,  ‘to  stretch  out’,  which  is  formed fr.  8ta  (see  dia-)  and  teiveiv,  ‘to  stretch’.  See tonic.
36582:standard,  n.  —  ME.,  fr.  OF.  estendard,  estandard (F.  etendard),  a  hybrid  formed  with  the  Teut. suff.  -ard  fr.  OF.  estendre  (F.  etendre),  ‘to  stretch out’,  fr.  L.  extendere',  see  extend.  Some  senses of  the  noun  standard  are  due  to  the  erroneous association  of  this  word  with  the  verb  stand. Derivatives :  standard,  adj.,  standardize  (q.v.) standardize,  tr.  v.  —  A  double  hybrid  formed  fr. standard  with  -ize,  a  suff.  of  Greek  origin. Derivatives:  standardiz-ation,  n.,  standardiz-er, n.
=== SKT ===
=== LKT ===
300:[Horn  NpEt  S.' 4,  Nr.  8]  'Stall',  ebenso tk.  o/t//r  'Stall,  Hürde'.  Hieraus  bulg. ah^r  'Stall,  Pferdestall',  serb.  ahar,  har, aar  'dass.'.    [Bern  SlEtWb  25.
379:c)  Mit  ähur  [s.  hier  Nr.  36]  ergibt  sich pars,  mlr  ähur  'Stallmeister,  Vorsteher eines  Marstalles',  ebenso  Ik.,  vulgär ausgesprochen  imrahor  [A.  Hindoglu, Dictionnaire  Franqais-Turc.  Vienne  1831. S.  201  a],  hieraus  rum.  imhrohor  'Stall- knecht'.
684:'Kristall';  hieraus  sp.  abalorio  'kleine Glasperle',  pg.  avelorios,  avellorios  'Glas- perlen, wertlose  Kleinigkeiten'.  [DE  31.
883:308!  Tk.  bin-: Binmek  'reiten'  [Stamm  men  'oben,  zu- erst, vorwärtskommen'  Vämbery  Tkt- ETWb  S.  214,  Nr.  233;  zu  dem  Wechsel zwischen  den  Labialen  m  und  b  vgl. z.  B.  hier  Nr.  305:  kirg.  -bez  =  osm. -mez];  dazu  btnigi  'Reiter';  hieraus  rum. binigiü  'Stallknecht'.  —  Aus  tk.  binis 'Art  zu  reiten',  dann  in  früheren  Zeiten das  'Gewand,  das  bei  feierlichen  Ge- legenheiten getragen  wurde',  wurde  rum. bini^  'ein  Kleidungsstück'.
1239:jeanne  [mit  volkrielyinologischer  Umge- stalluug],  sp.  dainajuana,  kat.  damajana; engl,  demi-john  'Korbflasche'.  Der  ge- naue Gang  der  gegenseitigen  Entleh- nungen ist  noch  nicht  klargestellt,  da- her sind  zahlreiche  andere  Etymologien aufgestellt  worden,  die  aber  weit  weniger befriedigen  [aus  lat.  dimidiana,  aus lat.  domina  und  galbma  >  frz.  dame und  jaune  u.  a.  m.].  [Devic  DEt  101/102. Lammens  Rem  94/95.  RomForsch  III, 497.    ZfromPh  II,  35i2.
1658:'Streif-  und  Raubzug  auf  feindliches Gebiet';  hieraus  mit  ar.  Art.  sp.algara 'Streifzug,  Haufe  berittener  Parteigänger', Vb.  algarear  'Kriegsgeschrei  erheben' [man  denke  an  den  Brauch  der  Araber, wie  die  homerischen  Helden  den  Angriff mit  lautem  Geschrei  zu  beginnen  und zu  begleiten],  algarada  'Kriegsgeschrei'; pg.  algara  'Gefecht,  Kampf,  Slreifzug' (Constancio  Dicc  50b];  frz.  algarade 'Kriegsgeschrei'.  [V.  HAMMER-PURG- STALL  in  ZDMG  V,  192  Anm.  DE  119. Eguilaz  176.  Devic  DEt  17.  Lammens Rem  12.    ML  3679.
1752:'Gips'  [aus  gr.  yü^oq,  lat.  gypsum]; hieraus  it.  gesso,  pg.  gesso,  sp.  yeso,  algez [woraus  dann  wieder  ar.  gass,  vulg.  gess nach  dem  Orient  zurückgewandert  ist]. Die  übrigen  europäischen  Formen  des Wortes  sind  unmittelbar  aus  dem  Lat., z.  B.  frz.  gypse  [gewöhnlich  pMtre], dtsch.  Gyps,  Gips.  [Doch  i.st  es  nicht unwahrscheinhch,  daß  das  gr.-lat.  Grund- wort selbst  wieder  aus  dem  Orient stammt,  vgl.  hebr.  gä^ls  'Kristall'  Hiob 28,  18;  ZDMG  XXV,  542  f.  In  der  Tat deuten  der  alte  Gebrauch  des  Gipses  bei den  Ägyptern  und  in  Äthiopien  (vgl. Herodot  3,  24  u.  7,  69)  sowie  die  Her- kunft der  besten  Sorten  aus  Syrien (vgl.  Plinius  36,  59)  auf  orientalischen Ursprung  auch  des  Namens.]  Übrigens ist  auch  tk.  alcy  'Gips'  eine  verderbte Form  für  ar.  al-gibs.
3688:'Stall'  [eigentlich  'schützend'  Horn  NpEt S.  63,  Nr.  2S2J,  tk.  ebenso  pajanda 'fest,  Balken'  [Kelekian  Kamüs  316  b]; hieraus  vnm.paianta  'Bund,  Strebeholz'.
3786:hronzo,  frz.  sp.  hronce,  frz.  bronze;  ndl. brons,  engl,  bronze,  dtsch.  Bronze, Prinzmetall  [mit  vcjlksetymologischer Umgestallung,  POTT  in  ZKM  IV,  264]; russ.  hronza,  klruss.  bronza,  öecli.  poln. bronz,  serb.  bronac;  bulg.  pernio,  serb. pirinac  'Messing'.  —  [Die  anderen  Ab- leitungen sind  weniger  wahrscheinlich:
4041:'Schatten,  Schutz'  [Horn  NpEt  S.  154, Nr.  695],  ebenso  tk.  saje  [aus  'schattiger Ort'  wird  'Hof,  Stall'];  hieraus  rum.  saia 'Stall',  saigiü  'Stall-,  Pferdeknecht'.  Aus pers.  säjäbän  'Schattenwächter  >  Bal- dachin, Schutzdach',  tk.  sajwan  wurde poln.  sejwan  'eine  Art  Zelt'.
```


## [2026-09-14T02:33:24.044Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AFM istabl ===\"; ls | grep -i afm; grep -n \"اصطبل\\|إصطبل\\|اسطبل\" AFM_pages.txt 2>/dev/null | head; echo \"=== AFA ===\"; ls | grep -i \"AFA\\|FVQ\\|PLA\""
}
```


### [2026-09-14T02:33:24.134Z] TOOL RESULT

```
=== AFM istabl ===
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
192:والكردنة ٠‏ وام الاصطبل فهو تعريب الرومى 562111111153
3449:3 ܐܕܝܨ حض ومعناه الاصطبل ‏ ܒܝܬܦܣܣܬ/ ܟ
=== AFA ===
AFA.txt
FVQ_pages.txt
FVQ.txt
```


## [2026-09-14T02:33:34.656Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '185,200p' AFM_pages.txt; echo \"=== leaf ===\"; python3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if 'الاصطبل' in p:\n        print('leaf',i, p[:80].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-14T02:33:36.217Z] TOOL RESULT

```
ܐܝܟ المعاول والظاهر ان الفاسي ماخوذ من اليونالي :ܘܡܐ
( إلا جور اليا عور والا جور والا جر 0 وال جرون) قري ١‏ "لوز دعو
تراب يحكم عجلة وتقريصة 2 2 5 'وقالوا فيه أ جر الطين ٠‏ وييرادفة بالارمشة
سدمارس وقال )ܡܢܐ (ص 09110 اصل اللفظة ارا ى ܐܓܪܐ وهو موحود :
اللغة 32 القدعة ٠واما‏ العُرميد فهو @ 7لكر له
| 0 13110 و 0 2 000 نالع ٠‏ ومئنهة الفرني ¢¢
والايطا ليائي - 0 3430 بالسر ± الدارجة 36
والكردنة ٠‏ وام الاصطبل فهو تعريب الرومى 562111111153
( إلا درون ) المثلفٍ والارى والوطن وهر إما معرب 50 80350 ,<
ماخوذ عن اليونائي ا ثاريه وهر القسم من ܝܗ الختص باارجال ܢ܆ܐ ܐܢܝܕܪܘܢܐ
11:20 ® ܕ[ 0 والقليد فاخوذان عن بسجده»: وعن 0 اي المخدع
وسبه مخدع
( الاذرريون ). زهر اضفر في 71005 5957 الذذ كو راصل 11 ]ا
شمه الثار. وآذر يون اغة فيه ± ` 096( حيجكى ( زهر القمر )
وقره كز ( العين السوداء )
3( الأرجان ) ,شر 4033( :3( 600390550901017 ا
=== leaf ===
leaf 9 لكر له | | 0 13110 و 0 2 000 نالع ٠‏ ومئنهة الفرني ¢¢ | والايطا ليائي - 0 3430 بالسر
leaf 136 2-0 | ( الك ركاه ) آلة للحائك وهي فارسيّة | ( الكرويا) بزر ننات شه اغصانة وورقه بالر
```


## [2026-09-14T02:33:45.735Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['AFM'].get('page_offset'), d['AFM'].get('local_file'))\n\"; echo \"=== ARY ===\"; grep -n \"استاندارد\\|اسطبل\\|اصطبل\\|ستدن\\|ستاندن\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-14T02:33:46.728Z] TOOL RESULT

```
198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
=== ARY ===
2477:۲- معطی این واژه در برخی زبان‌های هند و اروپایی: اسطبل» محل نگهداری دام. :
2478:۳- واژه‌ی فارسی "اسطبل" از واژه‌ی لاتین 57۸811181 آمده د این واژه‌ی لانین خود یا واژه‌های اوستایی
2481:و فرار گرفتن" و دبگری 818۳ (۱۰۱۹) به معنی "ایستاندن" و ار دادن", 8
```


## [2026-09-14T02:33:48.568Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd2 stabulum ===\"; grep -n \"stabulum\" incoming/WLD/WLD_Bd2_pages.txt | head -5; echo \"=== WLD stāi thief ===\"; grep -n \"stāyú\\|stayu\\|tāyú-\\|steya\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== IEC ===\"; grep -n \"^stābulom\\|^stā-\\|^stāiō\\|^tāius\\|stāius\" IEC.txt | head -20"
}
```


### [2026-09-14T02:33:48.668Z] TOOL RESULT

```
=== WLD Bd2 stabulum ===
42639:Anlehnung an Stall „stabulum“), schweiz. auch von Menschen (Senn brief-
=== WLD stāi thief ===
40501:Adv. „geheiin‘‘, wenn aus       gr. rrjv-oiog) steya-m „Diebstahr‘, stend-h
=== IEC ===
```


## [2026-09-14T02:33:51.859Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY context ===\"; sed -n '2465,2495p' incoming/ARY/ARY_pages.txt; echo \"=== which leaf ===\"; python3 - <<'EOF'\nd=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if 'اسطبل' in p:\n        print('leaf',i,'printed',i+1)\nEOF"
}
```


## [2026-09-14T02:33:52.617Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '40490,40520p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-14T02:33:52.962Z] TOOL RESULT

```
=== ARY context ===
آلمانی کهن (/027۵4۸ بزهابز صا0): صربی (۷ل5581۸4): 357۸۸
87۸3 برهمی (8048211۸01): ماد
آلمانی (058//۸00): 578780 مال87۸ لنونی (لنی) (771۸۸7)ما): ات87۸
انگلیسی کهن (لل5لاه8۸ ط0): «بلف578 برتونی (878670/۷): 87۸01
ال اند آلبانی (7لهالمقلم: 51۸
انگلیسی (لل5اا6۸0): 87۸
دانمارکی (0۸(7824): 0 ,57۸7.0 پسگشت‌ها 05
سوئدی (8218(0((): 575۸ نان رس ۱
نروژی (۸/0719509). 87۸ 10-151 ماه
هلدی (00703): 857۸ برهان قاطم + ۱۰۹۷-7۴
۱ بادداشت:
۱-اين واژه یا واژه‌های "استاک" و "ایستادن" همریشه است. ار
۲- معطی این واژه در برخی زبان‌های هند و اروپایی: اسطبل» محل نگهداری دام. :
۳- واژه‌ی فارسی "اسطبل" از واژه‌ی لاتین 57۸811181 آمده د این واژه‌ی لانین خود یا واژه‌های اوستایی
۸ (حل نگهدار ی اسب‌ها) و 06۸۷0-57۸۷۸ (محل نگهداری گاوها) از یک ريشه است.
۴ ۳016013۷ برای واژه‌های این فهرست دو واجریشه را می‌دهد یکی 978* , ۱۰۱۹(978) به معنی "ایستادن"
و فرار گرفتن" و دبگری 818۳ (۱۰۱۹) به معنی "ایستاندن" و ار دادن", 8
ه-واژه‌ی انگلیسی 0 عم از همین ریشه‌ی -871* یا 87۸۰* آمده است.
4+ چم انگلیسی سرواژه‌ی فارسی:,577۸08013010 ,(3۸5 18 ۲07۷ ۸ 08 01۸168) 357۸6118
2 9 دا
اوستایی (لل۸725374): 51۸38۸۰ ,87۸3۳1۸۰ آلمانی کهن (058/۸2 ۲/0 صا0):
سانسکریت (54۸/88/7): 57۸7 ,7 )57۸ تفتت۸ 57
ایسلندی‌کهن (7 هش صضا0). ۰ آلمانی (085/۸). 857۸7۲
572 انگلیسی کهن 20/05 00 بکل75د
ساکسونی کهن (/5420 صا0): 575813 8 ان
سس
[pdf page 87]
۸ / استخوا ان آست
انگلیسی (1ل5/ا6(0): ادن
دانمارکی (0۸(//5): ,87۸۵ پسگشت‌ها کت
سوئدی (820134): 5738 3
=== which leaf ===
leaf 85 printed 86
```


### [2026-09-14T02:33:53.014Z] TOOL RESULT

```
      Erweiterte Wzformen                   oder als solche in Rechnung gezogene                              s.   unter:
stale-,



(sjtai- „heiinlich    um etwas bringen,                                      hehlen,    stehlen^^;     Wzansatz     nach
         Schulze KZ. 27, 426,
  Ai. staydt „heimlich, verborgen“, stayii-h,^ tayu-li ^Dieb^^ (= aksL taj
Adv. „geheiin‘‘, wenn aus       gr. rrjv-oiog) steya-m „Diebstahr‘, stend-h
                                                      ;                             ;


„Dieb“; av. tayu- „Dieb“, taya- „DiebstahV'; gr. Trjvoirj ddd^ „ein Weg,
der einen um die Mtihe der Absicht betrugt“ C^rdu-Tiog, von jw/o-xd ; Lud-
wig KZ. 10, 449, Bgm. IF. 11, 106 Bechtel, Lexil. 316), xiqxri dnoQia^ Evdsia^                          •



oreQf]otg Hes., rrjxday             „bringe         um etwas, beraube^^, med. „darbe‘^; air. tdid
„DieV‘ (= abg.             tath,  Pedersen KG. 133); abg. taj „heim-
                                    iiber das -d                  s.

lich“      (s.   o.),   tajq^      tah „Dieb“. Ygl. Windisch KZ. 21,
                                tajiti    „verhehlen‘‘,
432, Pick KZ. 22, 374, Wb. 1^56, 144, 226, 332 f., 439, IIM22, und
gegen die schon durch den Yokalismus verwehrte Anreihung von lat.
mustela „Wieser' Yf. LEWb.^ s. v.
```


## [2026-09-14T02:34:02.768Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC head ===\"; head -5 IEC.txt; echo \"=== IEC stab ===\"; grep -n \"stābulom\\|stāb-\\|stāiō\\|tāius\\|stāiu\" IEC.txt | head -20"
}
```


### [2026-09-14T02:34:02.865Z] TOOL RESULT

```
=== IEC head ===
 
Stuart E. Mann AN INDO-EUROPEAN COMPARATIVE DICTIONARY
AN INDO-EUROPEAN COMPARATIVE
DICTIONARY
BY STUART E. MANN
=== IEC stab ===
```


## [2026-09-14T02:34:04.009Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sta- : sta-\\|stā- : stə-\\|„stehen\\|stehen, stellen\" incoming/WLD/WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-14T02:34:04.068Z] TOOL RESULT

```
5173:lich“, ibd. und Stokes KZ. 38, 459 f., auf ad-staio- zuriick, s. sta~ „stehen‘‘).
25075:   lat.   lacus,   „stehendes Gewasser, See; Brunnentrog; Grube“, lacuna
30994:Rinne“, norw. stka ,, seihen^', anord. slk n. „stehendes oder langsam rinnen-
40189:    Ptc. ai. sthiid- „stehend^‘ (av. stata- mit geneuerter Hochstufe), gr, orarog
40245:Steha bringen^; mit germ.                lautet ab lit. sidcias „stehend‘^; lit.
40275:Standort, Gewicht**, ora'dagog „stehend, tmbeweglich, fesf ordSiog „stehend,     *
40279:unbeweglich, steif, zugewogen**, orddr]v „stehend**, djiooradov „fern ab-
40285:shtare „stehend**, sforaze „aufrecht** (^sta-no-dio-,^ vgl. zum ^?-Suffix gr. dno-
40360:stoviis   „stehend (vom Wasser)“, lett.             stavti, stdvet   „stehn“, stcivus „stehend,
40632:[Studier II 26ff., Zitat nach:] Bgm. II^ 1,262; wohl nicht als „stehendes
40661:stoig- „stehen; spitz^, wohl Erw. von                   stei- ds.
40839:                              stct- „stehen, steif sein, steif emporstehn“ zu be-
41174:                             oder „stehen“                     =    „steif sein“ die.Bedeutungsver-
41483:  ir. timpdn   (angeblich „stehender Stein, kleiner abgebrochener Hiigel^
```


## [2026-09-14T02:34:09.129Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>40150 && NR<40400 && (/stabul/ || /dhlo/ || /Standort/)' incoming/WLD/WLD_Bd2_pages.txt | head -20; echo \"=== page tags near 40200 ===\"; awk 'NR>40150 && NR<40320 && /pdf page/' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-14T02:34:10.255Z] TOOL RESULT

```
— osk. statif „Standort“, got. slaps m.                            ;
   anord. stod n. „Standort, Herde von Stuten mit einem oder mehreren
steallnach Sievers IP. 4, 337 f. aus idg. *std4l6- oder als ^'std-dhlo-                               =
  Mit Pormans -dhlo-: lat. stahulum „Standort, Aufenthalt; Lager wilder
standhaft**,    umhr. staflarem „stabularem**, osk. staflatas-set „statutae sunt**,
Standort, Gewicht**, ora'dagog „stehend, tmbeweglich, fesf ordSiog „stehend,     *
  ai.     sthdna- n., av. ap. sterna- n. „Standort,                 Aufenthaltsort,           Ort, Platz**,
„Weber**, das aber unbelegt); si, sthdman- n. „Standort, Kraft**; got. stoma
=== page tags near 40200 ===
```


## [2026-09-14T02:34:16.163Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nlines=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ndef tag(n):\n    for i in range(n,0,-1):\n        m=re.search(r'\\[pdf page (\\d+)\\]',lines[i])\n        if m: return m.group(1)\nfor n in (40200, 40501):\n    print(n, 'pdf page', tag(n))\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['WLD'].get('page_offset'),d['WLD'].get('notes','')[:400])\""
}
```


### [2026-09-14T02:34:17.382Z] TOOL RESULT

```
40200 pdf page None
40501 pdf page None
Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). Tried IA (several queries), Google Books API (quota exceeded / not full view), HathiTrust (blocks automated access, 403). Band 2 (1927) is US public domain; Band 1 (1930) became US PD in 2026, so HathiTrust full view may exist - check manually at https://catalog.hathitrust.org/Search/Home?lookfor=walde+pokorny+vergleichendes. || UPDATE 2026-09: Bände I and II obtained in full from the Digital Libr
```


## [2026-09-14T02:34:21.616Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ntxt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\n# map line numbers to leaf\ncum=0\nbounds=[]\nfor i,l in enumerate(leaves):\n    n=l.count('\\n')+1\n    bounds.append((cum,cum+n,i))\n    cum+=n\ndef leafof(ln):\n    for a,b,i in bounds:\n        if a<=ln<b: return i\nfor ln in (40200,40501,42639):\n    i=leafof(ln)\n    print('line',ln,'leaf(0-based)',i,'printed',i+1-5)\nEOF"
}
```


### [2026-09-14T02:34:22.717Z] TOOL RESULT

```
line 40200 leaf(0-based) 600 printed 596
line 40501 leaf(0-based) 604 printed 600
line 42639 leaf(0-based) 637 printed 633
```


## [2026-09-14T02:34:27.749Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nleaves=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (600,604):\n    t=leaves[i]\n    print('=== leaf0',i)\n    print(repr(t[:150]))\n    print(repr(t[-150:]))\nEOF"
}
```


### [2026-09-14T02:34:28.871Z] TOOL RESULT

```
=== leaf0 600
'                                                                                                                    ;\n\n\n\n\n596                         '
'des (Uhlenbeck Tijdschr. v. Jfed. Taal- en Letterk,\n                                                        25, 294 f.) dieselbe\nBed.-Entw. erfahren.\n'
=== leaf0 604
'600                                         (8)kel   skot-\n\n\n\n    Lit. slcalbiu, sTcalbti             dem Waschholz schlagend waschen“.\n    ^-Erw. nM.'
'                               idg. e\n202).       Ebenso ai. cafati „ver8teckt u. dgl.” (Schulze KZ. 27, 426 beruft sich\nauf oxoTo/utjviog    :   ai.\n'
```


## [2026-09-14T02:34:38.215Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ntxt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\ni=txt.find('heiinlich    um etwas bringen')\n# find previous formfeed\na=txt.rfind('\\f',0,i); b=txt.find('\\f',i)\npage=txt[a+1:b]\nprint(repr(page[:200]))\nprint('...')\nj=txt.find('Mit  Pormans  -dhlo-') \nj=txt.find('Mit Pormans -dhlo-')\na2=txt.rfind('\\f',0,j); b2=txt.find('\\f',j)\nprint(repr(txt[a2+1:a2+200]))\nEOF"
}
```


### [2026-09-14T02:34:39.302Z] TOOL RESULT

```
'           ;\n\n\n\n\n 610                                            (s)tai-   —       stai-, sti-, sti-a-\n\n\n\n      Erweiterte Wzformen                   oder als solche in Rechnung gezogene              '
...
'                             :\n\n\n\n\n606                                                   sta-\n\n\n\nSteha bringen^; mit germ.                lautet ab lit. sidcias „stehend‘^; lit.\nstatine  „gro6e Holzw'
```


## [2026-09-14T02:34:50.551Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"stabulum\" IEC.txt | head -5; echo \"--- stāiō/tāius ---\"; grep -n \"tāyu\\|tāiu\\|stāiu\\|stenos\\|steuā\" IEC.txt | head -10; echo \"--- stā- headword ---\"; grep -n \"stā-, stə-\\|stāiō\\|stātis\\|stā- 'stand'\" IEC.txt | head -10"
}
```


### [2026-09-14T02:34:50.643Z] TOOL RESULT

```
17481:sthadhəlos (sthadhul-), à ‘stop, stand, stall’. WP II, 606 Latin stabulum, n. *living-quarters, stall’ beside stallus, um, id.; W sail, pl. seiliau, f. (‘base’, fr. *sthadhlis, ie); Br. staol, pl. iu, m. ‘stable’; EME staddle, s. ‘standing tree’; E staddle ‘foundation post in a barn; stone sup- port for haystack beside OE steall, E stall; MHG stal, gs: stalles, sm. ‘stable’; ON stallr, m. id.; OCS stodolü, m., stodolja, f. id. and com. Sl. Li. stadala, f. “stable, inn’; Latv. stadals, staduls, stadala, mf. id. (perh. Slav LWs). See next
--- stāiō/tāius ---
17177:Steigu, stigu- — stenos (stenios, stentós)
17188:sten-agio ‘groan’. Cf. stend E stenos (2), ston- Gk. stenágo, id.; OE stenecian, id.
17192:stenos (stenios, stentós) (1) “narrow, close” Gk. stenós, steinós, id.; steinos, n. ‘strait’; Fris. cf. stinne, v. (3) ‘squeeze, press’ beside stith, adj. “harsh”; OE stió, adj. “hard, harsh’;
17195:stenos (2) ‘groan, moan’. Cf. stend, stonos. WP II, 626 Gk. sténos, gs. -eos, n. id.; OE sten, n. id.; (o-gde in) OCS *stonü, m. id. and Gk. stónos, m. id.; Cz. ston, m. id. (OCS cf. stonava, id. stonati, v. id.); Sw. cf. stánka, v. “moan, pant’: OE stencan (2), id., fr. *ston-ago via *stong-)
17196:(stenos, à, Skt. variant of type psten-, q. v. in Skt. stánab, à, 1h, mf. *breast; (LW in) Arm. stin, id.)
17201:stenos — stero (sterno)
17295:stonos ‘groan, moan, roar’. Cf. steno, stenos. WP H, 626 Gk. stónos, m. id.; Cz. ston, m. id.; OCS cf. stonava, f. id.; stonati, inf. id.; Sw. cf. stánka, v. ‘groan, moar’, fr. *ston-ag0)
--- stā- headword ---
```


## [2026-09-14T02:34:54.783Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"WP II, 610\\|‘thief’\\|'thief'\" IEC.txt | head -20"
}
```


### [2026-09-14T02:34:54.838Z] TOOL RESULT

```
9476:lap- (?) ‘snatch’. Cf. lapos Gk. cf. lapázo ‘plunder, carry off’; Srb. cf. lopov ‘thief’; Li. lapë ‘fox’
18197:tāios, us ‘secretive; secretiveness; secret; silence; theft; thief". Cf. táið (2), above. WP II, 610 Skt. tayüh, m. ‘thief’; Av. tayus, m. id., tayo, m. ‘theft’; Hitt. cf. tayi-, v. ‘steal’; Gk. cf. téusios, adj. ‘misleading, misguiding"; Olr. tái, taí & tó, adj. “silent'; W taw, adj. ‘silent’; m. “silence”; Br. tað, tav, m. “silence; toez, pl. -iu, m. ‘ghost, will-o-the-wisp'; OBr. cf. taguel, adj. ‘silent’; W tawel, adj. id.; OCS taj, adv.
18228:tat- (1) (tatis) ‘secrecy, theft; thief". Cf. Gig (2) and tàios. WP IL, 610 Olr. táid, m. ‘thief; táide, f. ‘secrecy; theft’; táidim, v. ‘steal’; OCS tati, m., Slovene tat, m. ‘thief’. (NB. For Gk. tétē, tetáo, see quāt-)
```


## [2026-09-14T02:35:01.772Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/stable",
 "prompt": "Quote the etymology of stable (n.) 'building for horses' and stable (adj.) 'steady' — Old French estable, Latin stabulum, Latin stabilis."
}
```


## [2026-09-14T02:35:02.783Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/exit",
 "prompt": "Quote the etymology of 'exit' — Latin exitus, exire, from ex + ire. Which PIE root is it from?"
}
```


### [2026-09-14T02:35:06.011Z] TOOL RESULT

```
# Etymology of "Stable"

**Noun (building for horses):**
"building or enclosure with stalls where horses or cows are kept" originated in the early 13th century from Old French *estable* and Latin *stabulum*, meaning "a standing place."

**Adjective (steady/firm):**
Dating to the mid-12th century, this sense derives from Old French *estable* and Latin *stabilis*, meaning "firm, steadfast, stable, fixed." Both ultimately trace to the Proto-Indo-European root *\*sta-*, signifying "to stand, make or be firm."

The shared etymological foundation connects the physical structure (where animals stand) to the abstract quality of stability and dependability through the central concept of standing or firmness.
```


### [2026-09-14T02:35:06.574Z] TOOL RESULT

```
# Etymology of "Exit"

Based on the Online Etymology Dictionary, the word "exit" traces back through Latin to an ancient Indo-European root.

**Etymology chain:**
The noun "exit" (1530s) comes from Latin *exit* ("he or she goes out"), derived from *exire* ("go out, go forth, depart"). This breaks down into *ex-* ("out") plus *ire* ("to go").

**PIE root:**
The root *ire* ("to go") descends from the Proto-Indo-European root **\*ei-**, meaning "to go."

As the source states: "from *ex-* 'out' (see ex-) + *ire* 'to go' (from PIE root \*ei- 'to go')."
```


## [2026-09-14T02:35:15.515Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%A5%D8%B5%D8%B7%D8%A8%D9%84' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%AF%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%A7%D9%86%D8%AF%D9%86' \\\n 'https://www.etymonline.com/word/standard' \\\n 'https://www.etymonline.com/word/stable' \\\n 'https://www.etymonline.com/word/exit' \\\n 'https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D8%A7%D9%86%D8%AF%D8%A7%D8%B1%D8%AF/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 475, roots Sta/Stai 1 (stabulum-establ, standard, setadan, exit)' 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T02:35:22.061Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e57799501a5ca79f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa122a3c412183f6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/af2fc83105178875.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c7450309af77f4c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/298d40f16025a4dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/719b2c85719f3ba4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f0c61dbd0575f9c1.txt
```


## [2026-09-14T02:35:25.499Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '1,60p' e57799501a5ca79f.txt | head -60"
}
```


### [2026-09-14T02:35:25.549Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D8%A5%D8%B5%D8%B7%D8%A8%D9%84
FETCHED: 2026-09-14T02:35:17Z
STATUS: 200
TITLE: إصطبل - Wiktionary, the free dictionary

إصطبل - Wiktionary, the free dictionary 

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
 Arabic 

 Toggle Arabic subsection
```


## [2026-09-14T02:35:27.989Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -n -A8 -i \"Etymology\" e57799501a5ca79f.txt | sed -n '1,60p'"
}
```


### [2026-09-14T02:35:28.047Z] TOOL RESULT

```
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
--
154: Etymology
155- [ edit ] 
156-
157- From Byzantine Greek στάβλος ( stáblos ) , στάβλον ( stáblon ) , from Latin stabulum .
158-
159- Pronunciation
160- [ edit ] 
161-
162- IPA ( key ) : /ʔisˤ.tˤabl/
```


## [2026-09-14T02:35:33.376Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '163,230p' e57799501a5ca79f.txt"
}
```


### [2026-09-14T02:35:33.428Z] TOOL RESULT

```
 Noun
 [ edit ] 

 إِصْطَبْل • ( ʔiṣṭabl )  m ( plural إِصْطَبْلَات ( ʔiṣṭablāt ) ) 

 stable , stall (building where horses or the like are kept)
 873 , ابو العباس اليعقوبي , edited by Michael Jan de Goeje , كتاب البلدان [ kitāb al-buldān ] ( Bibliotheca Geographorum Arabicorum ; 7)‎ [1] , Leiden: E. J. Brill, published 1850, 1892 , page 243 , line 12 : 

 873 , ابو العباس اليعقوبي , edited by Michael Jan de Goeje , كتاب البلدان [ kitāb al-buldān ] ( Bibliotheca Geographorum Arabicorum ; 7)‎ [2] , Leiden: E. J. Brill, published 1850, 1892 , page 249 , line 7: 

 873 , ابو العباس اليعقوبي , edited by Michael Jan de Goeje , كتاب البلدان [ kitāb al-buldān ] ( Bibliotheca Geographorum Arabicorum ; 7)‎ [3] , Leiden: E. J. Brill, published 1850, 1892 , page 253 , line 10 : 

 Declension
 [ edit ] 

 Declension of noun إِصْطَبْل ( ʔiṣṭabl )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 إِصْطَبْل 
 ʔiṣṭabl 

 الْإِصْطَبْل 
 al-ʔiṣṭabl 

 إِصْطَبْل 
 ʔiṣṭabl 

 nominative

 إِصْطَبْلٌ 
 ʔiṣṭablun 

 الْإِصْطَبْلُ 
 al-ʔiṣṭablu 

 إِصْطَبْلُ 
 ʔiṣṭablu 

 accusative

 إِصْطَبْلًا 
 ʔiṣṭablan 

 الْإِصْطَبْلَ 
 al-ʔiṣṭabla 

 إِصْطَبْلَ 
 ʔiṣṭabla 

 genitive

 إِصْطَبْلٍ 
 ʔiṣṭablin 

 الْإِصْطَبْلِ 
 al-ʔiṣṭabli
```


## [2026-09-14T02:35:35.735Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg475.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/475.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/475.png"
}
```


### [2026-09-14T02:35:35.814Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 67658 Sep 13 22:35 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/475.png
```


## [2026-09-14T02:35:42.438Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v1 اسطبل ===\"; grep -n \"اسطبل\\|اصطبل\" BQT_v1_pages.txt | head -5; echo \"=== BQT v2 ستدن ===\"; grep -n \"ستدن\\|ستادن\" BQT_v2_pages.txt | head -10"
}
```


### [2026-09-14T02:35:42.520Z] TOOL RESULT

```
=== BQT v1 اسطبل ===
12823:گلاب ۷۵-۲۷4 ۰ . ‌ اصطیل و اسطبل - تکسراول و فتح سوم . از
25103:۴ - هرن *بروار» فارسی رابمعنی اصطبل آورده و گوید: دراوستا 02171۷2۲202 ۵ قی :
25105:بممنی اصطبل آورده » بادکند :
=== BQT v2 ستدن ===
1021:                                     ‫وم‬                         ‫استادن باشد ‪ - ۴‬و بقصر الف خاك گردا گرد‬
1095:‫استادن‌است " وجتبولمن‌بعنی می‌شینم وجتبولید‬               ‫چت؟ د ختح اول و سکون الی ‪.‬‬
1477:    ‫غین نقطه‌دار » بمعنی جزدر استدنکبهٌبرشته‬           ‫جانوری باشد سب رتککشبیه‌بملخ و بیسنگوند‬
3205:‫که از جوشیدن ‪ ۸‬و ازشورش وبهم برآمدن‬                  ‫من" بلغت زند وپازند (‪ )۱‬بمعتی‌استدن‪.‬و کرفتن‬
3219:                           ‫قرائتی ازکلمهٌ ‪ , 0818006501۷‬پهلوی ‪ » 021215‬ستدن گ‬
5979: ‫بادکه تعربی قام‬      ‫بممتی استادن‬     ‫و بازند ‪۳‬‬        ‫جغز یدن؟ ‪ -‬بر وزن‌لغزیدن ‪ ۰‬بمعنی‬
11847:                ‫(میخرم) «واژه نامه ‪۸۱۳٩+‬‏ ستدن چیزیبا برداختن‌بهای آن» مقابل‪:‬فروختن ‪.‬‬
17916:   ‫بند بروی فگرذواشتند و آن چهل هزارمرد بر مزشن کردن استادند و درولی ندشتند وقدری په‬
19161:            ‫رك‪ :‬دزی ج‪۱‬ص‪۲6‬؛ «دستور» (بسم‌اول) ‪.‬‬              ‫‪۴‬‬             ‫‪.‬‬     ‫کرستدن ‪ .‬سامان ‪2۷0524] .:‬‬
19782:‫دل دادن ‪ -‬بروزن استادن ک‪.‬نابه از‬                                        ‫خوانند‪٩‬‏ ‪ .‬خشك شد آنرا بکوبند وبرریشهای‬
```


## [2026-09-14T02:35:48.069Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== v1 12823 ===\"; sed -n '12815,12835p' BQT_v1_pages.txt; echo; echo \"=== leaf ===\"; python3 - <<'EOF'\nimport re\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\ni=txt.find('اصطیل و اسطبل')\na=txt.rfind('\\f',0,i)\nprint(repr(txt[a+1:a+120]))\nEOF"
}
```


### [2026-09-14T02:35:49.185Z] TOOL RESULT

```
=== v1 12823 ===
۵ اشنودن - دریهلوی 25100020« اونوالا ۲۲ » « بونکر ۰۷۵
مر کپ ازیشوند 2 + 5110 مبدل 5۳۷ و 5۲1۷ (شنیدن) « دعارله ۱۸۹ *۰
طبری ۵65110005040 ۰ ماژندرانیکنونی ۵۵0005560 و 05627تاعه
« وازء نامه ۱۲۰ » ,گیلکی ۵1511۳734۷250817,در فارسی نز شنودن» شنبدن ؛
شنفش . اشنیان - 5002 9215012 از ثر؛ اسفناجیان » درصحاری 1
مر کزی ابران بسبار میروند و بر_گهای ریز و بهم فشرده دارد و در آن مقداری
نمکپای فلیابی ذخیره مبشود ؛ و چون سافه های آنرا بوزانند خاکستری بنام
شخار بدست میا ید که مواد فلیابی زیاد دارد و در حابونازی بکار میرود « کل
گلاب ۷۵-۲۷4 ۰ . ‌ اصطیل و اسطبل - تکسراول و فتح سوم . از
نازی از لانینی 502101011170 بمعنی جایگاه چاپاربان ۶ تفی *. * اخنیان۳و
معتی امتضر است که قلمةٌ فاری باشد و آن
که داراین داراب‌استت هاگن وتالابرا لس
گویند .
اصطر خ" س بروزن ومعنی استخراست
که فلمة فارس ناشدب وتالابو آبگررا نز گووند.
سمفی است سرخ بسیاهی حابل و بسنی گویند
صمغ درخت زیتون است . نزله را نافم است .
اصطر لاب - ممروف است و آن
آلتی باشد ازیرنج وتال ساخته که منجمان‌بدان
ارتفاع آفتاب و کواکب معلوم کنند و این لفت
بونالی است بمعنی نرازوی آفتاب چه اصطرترازو

=== leaf ===
'اشو ی\nکه کمانگران بر باژوی از جابدر رفته \u200f بندند\nواشق معربآشت .\nاشتاف مامثا بنتح اول و کسرفاه\nیعنی عصاره مامثا ومامیئا '
```


## [2026-09-14T02:35:56.078Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3200,3228p' BQT_v2_pages.txt"
}
```


### [2026-09-14T02:35:56.135Z] TOOL RESULT

```
      ‫‪0‬‬          ‫‪۰‬‬    ‫‪0‬‬            ‫اس‬




‫که از جوشیدن ‪ ۸‬و ازشورش وبهم برآمدن‬                  ‫من" بلغت زند وپازند (‪ )۱‬بمعتی‌استدن‪.‬و کرفتن‬

                                                                   ‫)‪ ۱‬چك ‪ :‬ژلد ویاژند ‪.‬‬

 ‫انارکیل که‌باشکر‬    ‫آمده ول‬     ‫‪( €‬ند*ه)‬   ‫در رسالة بپلوی «خسرو کواتان ورتك وی‬           ‫‪۱‬‬


  ‫خورند بهندوی اثارکیل خواننه و بپارسيك کوچ ی هیندوك ( کوزهندی ) خواند ‪« ».‬اوبوالا‬
                                                                                         ‫‪۵‬؟ ‪°٩‬‏ ‪:‬‬   ‫ص‬

          ‫چو حنظل هریکی زهری بشیشه‪.‬‬                       ‫دو رخ چون جوز هندی رشه رشه‬
          ‫نظامی کنجوی «کنجینه ‪.۳4‬‬
  ‫‪ ۴‬هز ‪natnubesoj .‬‏‬         ‫‪ ۴‬رك ‪ :‬گوزشه ‪.‬‬          ‫اك ‪.‬‬ ‫ز‪:‬‬‫جورك‬  ‫‪۴‬‬
  ‫»رفتن « لریبکه ج ‪ ۷‬ص ‪» ۷۸۷‬‬
                           ‫قرائتی ازکلمهٌ ‪ , 0818006501۷‬پهلوی ‪ » 021215‬ستدن گ‬
  ‫«راحذمای زبان‌پهلوی ‪ .‬آبراهامان ص ‪٩4‬‏ بوستی درفرهنك بندهش (س‪ )۷۱۱‬آرد ‪ :‬جوسبوتن»‬
  ‫قرائت پارسبان بجای « دسیون ؛ ودرشرح « دسیوتن * گوبد (ص ‪ : ) ۵۵۱‬بمعنی آوردن *‬
                                                     ‫رك ‪ :‬جوسه ‪.‬‬       ‫‪۵‬‬            ‫ها‬        ‫بردڻ »‬
            ‫کەجوسنکش بود فطای لوقا‪.‬‬                       ‫‏‪ ٩‬ب‪-‬قطاسی بنجم راز موبد‬
              ‫خ«اقانی شروآنی‪›»٤‬‏‬
                          ‫‪ ۸‬رك ‪ :‬جوشیدن ‪.‬‬               ‫‪ « :‬نشی» و رل ‪ :‬جوصق‬      ‫ره‬      ‫‪۲‬‬

                             ‫‪۱‬‬                                        ‫بقه ازصفحه ‪۸۹٥‬‏‬
          ‫‪ - °‬ونيز رك‪ :‬جوجن ‪.‬‬                ‫راجا»‬    ‫ک)ت«ر‬
```


## [2026-09-14T02:36:08.788Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B5%D8%B7%D8%A8%D9%84/",
 "prompt": "Quote the فرهنگ معین entry for اصطبل verbatim including any bracketed origin tag, and the دهخدا entry's etymological remark."
}
```


### [2026-09-14T02:36:13.669Z] TOOL RESULT

```
# Requested Dictionary Entries

**Farhang-e Moein entry:**
"(اِ طَ ) [ معر - لا. ] (اِ. )=اسطبل : ۱ - طویله . ۲ - آخور."

**Dehkhoda entry's etymological remark:**
"با اتابل فرانسه از یک اصل است و لاتینی استابولوم است"

(The word shares a common origin with French "étable" and derives from Latin "stabulum.")
```


## [2026-09-14T02:36:33.288Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T02:36:33.334Z] TOOL RESULT

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


## [2026-09-14T02:36:37.501Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A7%D8%B5%D8%B7%D8%A8%D9%84/' --note 'page 475, root Sta: Mo'\"'\"'in entry for اصطبل = معرب لاتین' 2>&1 | tail -1"
}
```


### [2026-09-14T02:36:40.039Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/57c3ad7c202cd408.txt
```


## [2026-09-14T02:38:47.209Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT stā ===\"; grep -n \"^stā\\|stā-\\|'stand'\\|a-stāya\" KNT_full.txt | head -15; echo \"=== KNT steal/thief ===\"; grep -n -i \"steal\\|thief\" KNT_full.txt | head -10"
}
```


### [2026-09-14T02:38:47.285Z] TOOL RESULT

```
=== KNT stā ===
23892:stāna- ‘place’ (831, §160.Ib; Foy, KZ 35.48; hardly 
24113:augmented imf. of ava- + stā-. Probably not а 
=== KNT steal/thief ===
```


## [2026-09-14T02:38:48.493Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB 383 ===\"; sed -n '378,390p' HUB.txt; echo \"=== HUB 2580 ===\"; sed -n '2578,2592p' HUB.txt; echo \"=== HUB 10711 ===\"; sed -n '10705,10715p' HUB.txt"
}
```


### [2026-09-14T02:38:48.564Z] TOOL RESULT

```
=== HUB 383 ===
= zd. *aiwistditi-, aber ustad existirt nicht und *aiwi'
stditi^ ware = np. *afstad.
84. Np. estddan geht jedenfalls nicht auf ap. *adi-8ta
zuriick, das doch zu np. *aiSt(ldan oder *aistCLda7i ge-
fiihrt hatte.2) Der Infinitiv von sta war ap. *8tatanaiy
= np. istadan, sitadan, das Praesens lautete in der
3. p. sg. *histataiy (vgl. zd. histaiti^ skr. tisthati) oder
*istataiy (belegt ist 3. p. sg. imperf. med. aistata),
woraus im Neup. (mit Anlehnung an den Infinitiv ista-
dan) istad wurde. Die Form estad lasst sich vielleicht auf
ein ap. 3. p. pr. *aistataiy (von a + sta) zuriickfuhren,
das im Phi. *estat ergab und sein anlautendes e auf den
Infinitiv (ap. *astatanaiy == phi. ^astatan) ubertrug, der
=== HUB 2580 ===
schieben', spuiumn 'Aufschub' (aus spoii- =■ ipsLZ.spdz-),
Phi. y^spoxtxtan'^ ist eine XJnform.
707. Np. sipihr 'Himmel' ist nach NSldeke direkt =
skr. gvitrd" Veisslich, wei3s', dazu nach Geiger afgh.
sper^ grau*.— 74 —
709. Die urspriingliche Infinitivform scheint sitadan ge-
wesen zu sein, vgl. np. sitadan (neben sitadan) = paz.
stadan, ptc. stad Min. 61. 192. Hier kommt auch der
Praesensst. stan- haufiger vor als stan-. Wrzl. ston?
712. Das Wort sitdra ist arabisch, von satara 'texit*
(N5ldeke).
713. Das in der Note angefuhrte stuar'^) *dick' stelle ich
zu zd. stavah- *Dicke*, stui-^ stvi- als 1. Glied von
Comp. (fur *5^wra-. stehend, vgl. C aland, KZ.31,267)
= *dick', skr. sthAvira- 'breit, dick, massig , sthura-
=== HUB 10711 ===
siA;ar 76.
siwt 79.
siparl 73.
si>i/ir 73.
siristan 75.
iSiS^a/i 128, 239-240.
sitadan 74.287 —
sitdra 74.
situdan 136.
siyah 78.
5«i/«rws78, 234,261,273.
```


## [2026-09-14T02:38:57.438Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"stan?\" HUB.txt | head; echo \"=== p287 area ===\"; python3 - <<'EOF'\nd=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d))\nfor i,p in enumerate(d):\n    if 'sitadan' in p or 'sitādan' in p:\n        print('leaf',i,'printed~',i-10)\nEOF"
}
```


### [2026-09-14T02:38:58.553Z] TOOL RESULT

```
=== p287 area ===
300
leaf 24 printed~ 14
leaf 84 printed~ 74
leaf 296 printed~ 286
```


## [2026-09-14T02:39:01.008Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nt=d[296]\ni=t.find('sitadan')\nprint(t[max(0,i-900):i+400])\nEOF"
}
```


### [2026-09-14T02:39:01.909Z] TOOL RESULT

```
 36, 204.
pa sand 41, 191.
pasoa;^ 36, 133, 191.
/?rts^ 41.
|)asMa7 36, 133, 191, 193,
218.
pasanjldan 42, 191.
paslntdn 40.
paskam 41, 191.
2>as/M 42.
patydra 37, 188.
pdytstan 37.
2?%%^ 37, 194.
pdzahr 36, 133, 193.
p^rdz 45.
pes 45.
pidrdm 38.
pi/i 46.
pir 38, 131, 146.
jofrar 45.
pis^ 42.
pistdn 41, 186.
pizinurdan 41.
pizdhidan 41.
p5/ad 43.
po5^ 43.
po^a 43.
pwfc 43.
pw/ = pwW 195, 207.
ptiia 43.
r«d 66, 270.
rflda 66.
raftan 67.
raA 66.
ra/?i 68.
raja 66.
ram 67.
randldan 67.
radlrfaw 67.
ras 12, 269.
rasfc 13.
raarm 66.
reg 68.
rgy 6, 135, 240.
rim 68.
riS 68.
risk 67.
ristan 67.
rot 68.
r52i 67.
rttbudan 66.
rudan 67.
ritw 68.
Rust am 251.
sa 73.
sa(/ 76, 116, 178.
sai^a 72.
5a/ar 72.
sdmdn 72.
sdn 72.
sang 76.
sanjidan 77.
sarat 14, 199.
satarvan 74.
saugand 77.
5gr 78.
sezdah 78.
5/ 78, 271.
Si 78.
siA;ar 76.
siwt 79.
siparl 73.
si>i/ir 73.
siristan 75.
iSiS^a/i 128, 239-240.
sitadan 74.
```


## [2026-09-14T02:39:09.601Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD conceal/steal roots ===\"; grep -n \"To conceal\\|To rob, steal\\|^tai\\b\" AHD_watkins1985.txt | head; echo \"=== KLN stand ===\"; grep -n \"^stand,  intr\\|stand,  intr\\. v\\.\" KLN_1966.txt | head -3; echo \"=== ARY standard ===\"; grep -n \"استاندارد\" incoming/ARY/ARY_pages.txt | head -3; echo \"=== BQT v1 استاندارد ===\"; grep -n \"استاندارد\" BQT_v1_pages.txt | head -3; echo \"=== HRN standard ===\"; grep -n -i \"estandard\\|standard\" HRN.txt | head -3"
}
```


### [2026-09-14T02:39:09.734Z] TOOL RESULT

```
=== AHD conceal/steal roots ===
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
1021:ster-4. To rob, steal. 1. Possibly dissimilated form in Germanic *ste/an in Old English stelan, to steal: STEAL. 2. Germanic derivative noun *stél-ithé (-ithd, abstract suffix) in Middle English stelth, stealth: STEALTH. 3. Ex- tended dissimilated form in Germanic frequentative *stalkon in Old English *stealcian, to move stealthily: STALK?. [Pok. 3. ster- 1028.]
=== KLN stand ===
=== ARY standard ===
=== BQT v1 استاندارد ===
=== HRN standard ===
```


## [2026-09-14T02:39:13.469Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:46:36.158Z] AGENT

I'll write the verification JSON file now, using a Python heredoc so the Persian text stays intact.


## [2026-09-14T02:57:34.300Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\n\ndata = {\n \"pdf_page\": 475,\n \"book_page\": 445,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Stâ, Stha, Stâk\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *steh₂- (traditional *stā- : *stə-) 'to stand, to place', with the extension *stāk-/*stek- 'to stand, put' (Pokorny 1004–1010 and 1011)\",\n   \"note\": \"Pokorny's headword is 'stā- : stə- ‚stehen, stellen’', Page(s) 1004-1010 (POK_full.txt line 81069 ff.; POK_03.txt leaves 244-251 = printed pp. 1004-1011). Nourai's POK:1008,1009 are pages inside that entry — p.1008 (POK_03 leaf 248) is precisely where sections 8-9 stand, i.e. 'mit Formans -dhlo-: lat. stabulum' and the Germanic *standan material, so the citation is well chosen even though the entry's head is at 1004. 'Stha' is Nourai's notation for the Indo-Iranian aspirated shape (Skt. tiṣṭhati, sthā-, sthāna-), 'Stâk' is Pokorny's separate headword 'stāk-, stek- ‚stehen; stellen’' at p.1011, printed there with the explicit note 'Erweiterung von stā- ‚stehen’' — which is why Nourai can redirect ROOT Stâk → Stâ at the bottom of this same page. Root, language label and gloss are all correct.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *steh₂- (در سنت قدیم‌تر *stā-) به معنی «ایستادن، نهادن» در فرهنگ پوکورنی در صفحات ۱۰۰۴ تا ۱۰۱۰ آمده است؛ صفحهٔ ۱۰۰۸ که نورایی به آن ارجاع داده، همان صفحه‌ای است که stabulum لاتین و *standan ژرمنی در آن بررسی شده‌اند. «Stha» صورت دمیدهٔ هندوایرانی (سنسکریت sthā-، tiṣṭhati) و «Stâk» سرواژهٔ جداگانهٔ پوکورنی در صفحهٔ ۱۰۱۱ است که خود پوکورنی آن را «گسترش ریشهٔ stā-» خوانده است؛ به همین سبب نورایی در پایین همین صفحه Stâk را به Stâ ارجاع داده است. ادعای نورایی دربارهٔ ریشه، برچسب زبانی و معنا درست است.\",\n   \"sources\": [\n    \"https://www.etymonline.com/word/stable\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:1008,1009\", \"status\": \"supports\", \"note\": \"Pokorny IEW s.v. 'stā- : stə- ‚stehen, stellen’', Page(s): 1004-1010 (POK_full.txt l.81069; References: 'WP. II 603 ff., WH. I 343 f., 705 f.'). Printed p.1008 = POK_03.txt leaf 248, which carries '8. mit Formans -dblo-: lat. stahulum ‚Standort, Aufenthalt; Lager wilder Tiere, Stall’ ... stahilis ‚feststehend, standhaft’' — the exact material of nodes #1 and #11. Leaf 249 carries the printed numeral 1008 as its footer, leaf 250 = 1009.\"},\n    {\"ref\": \"POK:1011 (for 'Stâk', not cited by Nourai)\", \"status\": \"supports\", \"note\": \"POK_full.txt l.81044: 'Root / lemma: stak-, stek- / Meaning: to stand; to put / Note: extension from stā- ‚stand’ ... Page(s): 1011' — confirms that Nourai's third headword Stâk is a real Pokorny lemma and an extension of Stâ.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. sta- (AHD_watkins1985.txt line 997)\", \"stance\": \"supports\", \"note\": \"'sta-. To stand; with derivatives meaning “place or thing that is standing.” ... 9. Suffixed form *stə-dhlo- in Latin stabulum, standing place: STABLE. ... II.1. Nasalized extended form *sta-n-t- in Germanic *standan ... See stak-. [Pok. stā- 1004.]' — Nourai's whole entry 0 is a condensation of this article.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II, running head 'stā-' p.606 (WLD_Bd2_pages.txt)\", \"stance\": \"supports\", \"note\": \"'Mit Formans -dhlo-: lat. stabulum ‚Standort, Aufenthalt; Lager wilder Tiere, Stall’ ... umbr. staflarem ‚stabularem’, osk. staflatas-set ‚statutae sunt’' — the source Pokorny himself abbreviates (WP. II 603 ff.).\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. sthadhəlos (IEC.txt line 17481)\", \"stance\": \"supports\", \"note\": \"'sthadhəlos (sthadhul-) … ‚stop, stand, stall’. WP II, 606 Latin stabulum, n. “living-quarters, stall” … OE steall, E stall; MHG stal … OCS stodolŭ' — Mann reconstructs the same *stə-dhlo- noun.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur p.86, s.v. ایستادن (incoming/ARY/ARY_pages.txt leaf 85)\", \"stance\": \"supports\", \"note\": \"«پوکورنی برای واژه‌های این فهرست دو واج‌ریشه را می‌دهد، یکی *STĀ به معنی ”ایستادن“ و دیگری *STĀK (۱۰۱۱) …» — an independent modern Persian handbook giving exactly Nourai's pair of headwords with the Pokorny pages.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Latin\",\n     \"words\": \"stabulum\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin stabulum n. 'standing place, stall, lair, inn' is a nomen instrumenti/loci built on the root *steh₂- with the suffix *-dhlom: PIE *stə-dhlo-m > Italic *stafl- > Latin -bulum, by the regular Italic change of intervocalic *-ðl- to -bl- (compare fābula : fārī, pābulum : pāscō, and the Umbrian/Oscan cognates staflarem, staflatas-set which preserve the -fl-). Attested from Plautus onward of cattle-stalls, then of inns and brothels (prōstibulum). Beside it Latin has stabilis 'firm-standing' < *stə-dhli-, the source of Nourai's 'stable 2' in node #11, so the two English 'stable' words in this chart are genuine doublets of a kind.\",\n     \"derivation_fa\": \"واژهٔ لاتین stabulum «جایگاه ایستادن، طویله» از ریشهٔ *steh₂- و پسوند ابزارساز *-dhlom ساخته شده است: *stə-dhlo-m > ایتالیایی آغازین *stafl- > لاتین stabulum؛ خوشهٔ *-ðl- در لاتین به -bl- بدل می‌شود (مانند fābula از fārī) در حالی که امبریایی و اسکی همان -fl- را نگاه داشته‌اند (staflarem). پوکورنی (ص ۱۰۰۸)، والده–پوکورنی (ج ۲ ص ۶۰۶) و کلاین هر سه همین ساخت را می‌دهند؛ ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/stable\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. sta-, item 9: '9. Suffixed form *stə-dhlo- in Latin stabulum, standing place: STABLE.' (AHD_watkins1985.txt line 997).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.1008 §8 (POK_03.txt leaf 248)\", \"stance\": \"supports\", \"note\": \"'8. mit Formans -dblo-: lat. stahulum ‚Standort, Aufenthalt; Lager wilder Tiere, Stall’ (prōstihulum ... nausti-bulum), stahilis ‚feststehend, standhaft’, umbr. staßarem ‚stabulārem’, osk. staflatas-set ‚statutae sunt’.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.606\", \"stance\": \"supports\", \"note\": \"'Mit Formans -dhlo-: lat. stabulum ‚Standort, Aufenthalt; Lager wilder Tiere, Stall’ ...' — identical wording, the source of Pokorny's paragraph.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. sthadhəlos (IEC.txt l.17481)\", \"stance\": \"supports\", \"note\": \"'WP II, 606 Latin stabulum, n. “living-quarters, stall” beside stallus, um, id.'\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. stable, n. (KLN_1966.txt l.36519)\", \"stance\": \"supports\", \"note\": \"'fr. L. stabulum, “stable, stall, lair, hut”, which stands for *stə-dhlo-m and lit. means “a place for standing”, from the stem of stāre, “to stand”.'\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Arabic\",\n     \"words\": \"\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The box is empty on the printed page; it stands for Arabic إِصْطَبْل / إِسْطَبْل (ʾIṣṭabl / ʾIsṭabl) 'stable, stall', already in al-Yaʿqūbī's Kitāb al-buldān (873 CE, ed. de Goeje pp. 243, 249, 253). Arabic did not take the word straight from Latin: the intermediary is Byzantine Greek στάβλος / στάβλον, itself a Latin loan of the imperial period and the ordinary word for the army/hippodrome stables the Arabs met in Syria and Egypt. In Arabization the initial st- cluster, impossible in Arabic, is broken by a prothetic hamza ʾi-, and the t of stablon is rendered by the emphatic ṭ (ط), with the first sibilant written either ص (assimilated to the emphatic) or س. Addi Shir states the borrowing plainly. Nourai's Latin → Arabic arrow is right in substance; the Greek way-station is omitted and the node prints no word at all, which is why this is 'plausible' rather than 'confirmed'.\",\n     \"derivation_fa\": \"جعبهٔ عربی در چاپ کتاب تهی است و منظور واژهٔ «إِصْطَبْل/إِسْطَبْل» است که در کتاب البلدان یعقوبی (۸۷۳ م.) گواهی شده است. راه وام‌گیری از لاتین به عربی بی‌میانجی نبوده؛ میانجی یونانی بیزانسی stáblos/stáblon است. در معرّب‌سازی، خوشهٔ آغازین st- با همزهٔ پیشافزوده شکسته شده و t به طای مطبق بدل گشته است (همگونی). ادعای نورایی در اصل درست است، امّا حلقهٔ یونانی را انداخته و واژه را ننوشته است؛ پس «با احتیاط پذیرفتنی» است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A5%D8%B5%D8%B7%D8%A8%D9%84\"],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in s.v. اصطبل (read at abadis.ir/fatofa/اصطبل): '( ا攎 طَ ) [ معر - لا. ] (ا攎. ) = اسطبل : ۱ - طویله . ۲ - آخور .' — the tag [معر – لا.] means 'Arabicized, from Latin', i.e. exactly Nourai's Latin → Arabic → Persian chain.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM_pages.txt leaf 9 (letter alif)\", \"stance\": \"supports\", \"note\": \"'وأما الاصطبل فهو تعريب الرومي stabulum' — 'as for al-iṣṭabl, it is the Arabicization of Latin/Rumi stabulum'.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' with Mo'in's footnote, s.v. اصطبل/اسطبل (BQT_v1_pages.txt line 12823)\", \"stance\": \"supports\", \"note\": \"OCR: 'اصطبل و اسطبل - بکسر اول و فتح سوم . از [یو]نانی از لاتینی STABULUM بمعنی جایگاه چارپایان' (Persian OCR noisy but legible) — Mo'in names the Greek step that Nourai omits.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch 1927 (LKT.txt, searched 'istabl', 'stabulum', 'Stall')\", \"stance\": \"silent\", \"note\": \"Lokotsch has Persian آخور ɡ اآخور/اهور (no.36, 'Stall') and pers. mīr-āḵur, but no entry for iṣṭabl — he only covers oriental words that entered European languages, and this one travelled the other way.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. stable, n. / constable (KLN_1966.txt)\", \"stance\": \"silent\", \"note\": \"Klein traces the European side only (OF estable < L. stabulum; Late L. comes stabuli → constable) and has no Arabic entry.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"establ «اسطبل»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian اسطبل / اصطبل (esṭabl, osṭobl) 'stable' is a straight loan from Arabic ʾiṣṭabl, i.e. the last link of Latin stabulum → Byzantine Greek stáblos → Arabic ʾIṣṭabl → Persian. Mo'in tags the word '[معر – لا.]' = muʿarrab, from Latin; Dehkhoda writes 'با اتابل [étable] فرانسه از یک اصل است و لاتینی استابولوم است'. The س/ص doublet is the normal Persian treatment of an Arabic emphatic in a word of non-Arabic origin (the printed page has اسطبل, a well-attested variant); the Persian word competes with native آخور and with طویله. Because the word reached Persian through Arabic, Nourai's three-step arrow is right; only the unnamed Greek stage is missing (see node #2).\",\n     \"derivation_fa\": \"«اسطبل/اصطبل» در فارسی نو وام‌واژه‌ای عربی است؛ یعنی زنجیرهٔ stabulum لاتین > stáblos یونانی بیزانسی > إصطبل عربی > فارسی. معین آن را «[معر – لا.]» (معرّب، از لاتین) می‌داند و دهخدا می‌نویسد «با اتابل فرانسه از یک اصل است و لاتینی استابولوم است». نوشتن آن گاه با سین و گاه با صاد روش معمول فارسی در برخورد با حروف مطبق عربی است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://abadis.ir/fatofa/%D8%A7%D8%B5%D8%B7%D8%A8%D9%84/\",\n      \"https://en.wiktionary.org/wiki/%D8%A5%D8%B5%D8%B7%D8%A8%D9%84\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:266\", \"status\": \"supports\", \"note\": \"The 6-volume Farhang-e Farsi is not paginated online, so p.266 itself could not be opened; the entry text was read at abadis.ir: 'اصطبل ( ا攎 طَ ) [ معر - لا. ] (ا攎. ) = اسطبل : ۱ - طویله . ۲ - آخور .' The page number is at least consistent with the volume's alphabet (استاندارد at 239 < اسطبل at 266).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt line 12823, Mo'in's note s.v. اصطبل و اسطبل\", \"stance\": \"supports\", \"note\": \"'از [یو]نانی از لاتینی STABULUM بمعنی جایگاه چارپایان' — Greek from Latin stabulum 'place of quadrupeds'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur p.86 s.v. ایستادن, note 3 (ARY_pages.txt leaf 85)\", \"stance\": \"supports\", \"note\": \"'واژهٔ فارسی ”اسطبل“ از واژهٔ لاتین STABULUM آمده … این واژهٔ لاتین خود با واژه‌های اوستایی … از یک ریشه است' — an independent modern Persian source giving the same derivation.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt, searched 'istabl', 'stabul')\", \"stance\": \"silent\", \"note\": \"Horn excludes Arabic loanwords from the Grundriss; no entry.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"stable 1\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English stable 'building for horses' is Middle English stable, from Old French estable (Modern French étable) < Latin stabulum; first recorded in English in the early 13th century. Old French had prefixed the prothetic e- that Gallo-Romance puts before s + consonant (schwa-prothesis, as in escole, estat); English dropped it again in the 13th-14th century, whence stable beside surviving doublets such as constable < Late Latin comes stabulī 'count of the stable'. The sense never left 'standing place for animals'.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی stable «طویله» از انگلیسی میانه stable، از فرانسهٔ کهن estable (فرانسهٔ امروز étable)، از لاتین stabulum آمده و از سدهٔ سیزدهم میلادی در انگلیسی گواهی شده است. الف پیشافزودهٔ فرانسهٔ کهن (مانند همان e- در escole) در انگلیسی افتاده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/stable\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. sta- item 9: '*stə-dhlo- in Latin stabulum, standing place: STABLE.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. stable, n. (KLN_1966.txt l.36519)\", \"stance\": \"supports\", \"note\": \"'stable, n., a building for horses or cattle. — ME., fr. OF. estable (F. étable), fr. L. stabulum … See state and cp. the second element in constable.'\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century (vol. 1 only, A-?; 'stable' not in the available volume)\", \"stance\": \"silent\", \"note\": \"Only vol. 1 of the 2nd ed. is on disk, so the S entries could not be consulted.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Germanic\",\n     \"words\": \"standan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *standaną 'to stand' (Gothic and Old Saxon standan, Old Norse standa, Old English stondan/standan, Old High German stantan) is a nasal-infixed present built on the zero grade of *steh₂-: *stə-n-t- with the -t- enlargement, beside the preterite stem without the nasal (Goth. stōp, ON stóð, OE stōd, OHG stuot) which continues *stō-d-. The pair present-with-n / preterite-without-n is the classic Germanic evidence for the infix. Nourai's spelling 'standan' is the Gothic/Old Saxon form; the box carries no reference, but the form is the standard one in Pokorny and Watkins.\",\n     \"derivation_fa\": \"ژرمنی آغازین *standaną «ایستادن» (گوتی و ساکسون کهن standan، نورسی کهن standa، انگلیسی کهن standan) زمان حالی است با میانوند دماغی که بر پایهٔ درجهٔ صفر ریشهٔ *steh₂- ساخته شده است (*stə-n-t-)؛ ستاک گذشته (گوتی stōp، انگلیسی کهن stōd) بدون آن میانوند است و همین دوگانگی گواه وجود میانوند است. گرچه نورایی برای این جعبه ماخذی نیاورده، صورت معیار همین است؛ ادعای او درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/standard\"],\n     \"ref_check\": [\n      {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"The node carries refs=None in the book; nothing to check. The form was verified against Pokorny and Watkins instead (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW p.1007-1008 (POK_full.txt l.81069 ff.)\", \"stance\": \"supports\", \"note\": \"'mit d-Erweiterung: Praeteritum got. stōp, aisl. stóð, as. stōd, ahd. stuot … wozu mit praesentischer Nasalierung got. as. standan, aisl. standa, ags. stondan, ahd. stantan ‚stehen’.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sta-, II.1\", \"stance\": \"supports\", \"note\": \"'1. Nasalized extended form *stə-n-t- in Germanic *standan in: a. Old English standan, to stand: STAND … c. Old French estandard, rallying place: STANDARD.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.604-606\", \"stance\": \"supports\", \"note\": \"The stā- article lists the Germanic present with nasal beside the d-preterite, the material Pokorny reprints.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"French\",\n     \"words\": \"estandard\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Old French estandart / estendart 'rallying point, banner fixed to a pole' is first met in 12th-century Anglo-Norman and Old French texts. Its origin is genuinely contested. (a) Watkins/AHD and Barnhart derive it from Frankish *standhard, literally 'stand firm/hard' — a compound of the Germanic verb *standan (Nourai's node #5) and the adjective *hardu- 'hard', which is why the chart adds the cross-reference '☞ Kar 1' to Nourai's root for 'hard'; Watkins prints 'Old French estandard, rallying place: STANDARD' under *stə-n-t-. (b) Klein and the OED reject that as folk etymology and make estendard a hybrid of Old French estendre 'to stretch out' (< Latin extendere) with the Germanic suffix -ard, the banner being the thing 'stretched out'; on that view the later 'upright pole / fixed measure' senses were secondarily attracted to the verb stand. Etymonline reports both. Nourai follows (a) without signalling that (b) exists, so the arrow Germanic → French is accepted by part of modern scholarship only.\",\n     \"derivation_fa\": \"واژهٔ فرانسهٔ کهن estandart/estendart «درفش، نقطهٔ تجمّع» از سدهٔ دوازدهم میلادی گواهی شده و ریشهٔ آن مورد اختلاف است. واتکینز (AHD) و بارنهارت آن را از فرانکی *standhard «سخت ایستاده» (از stand + hard) می‌دانند — همان که نورایی با ارجاع به ریشهٔ Kar ۱ پذیرفته است — ولی کلاین و فرهنگ آکسفورد این را ریشه‌شناسی عامیانه می‌خوانند و واژه را از estendre «گستردن» (از لاتین extendere) با پسوند ژرمنی -ard می‌گیرند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://www.etymonline.com/word/standard\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1257\", \"status\": \"partial\", \"note\": \"Page 1257 of the 1975 New College main dictionary is not among the copies on disk (only Watkins's root appendix is), so the exact page could not be opened; but the appendix does carry the claim — Watkins 1985 s.v. sta- II.1.c: 'Old French estandard, rallying place: STANDARD' — so Nourai's source says what his arrow says.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. standard, n. (KLN_1966.txt l.36582)\", \"stance\": \"contradicts\", \"note\": \"'standard, n. — ME., fr. OF. estendard, estandard (F. étendard), a hybrid formed with the Teut. suff. -ard fr. OF. estendre (F. étendre), “to stretch out”, fr. L. extendere; see extend. Some senses of the noun standard are due to the erroneous association of this word with the verb stand.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sta- II.1.c\", \"stance\": \"supports\", \"note\": \"Places Old French estandard directly under Germanic *standan.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt, searched 'estandard', 'stabulum')\", \"stance\": \"silent\", \"note\": \"No hit in the OCR for either string.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Persian\",\n     \"words\": \"estândârd «استاندارد»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian استاندارد is a 20th-century Europeanism, not an inherited word: Mo'in tags it '[فر.]', i.e. from French standard, and glosses it 'نمونه تصویب شده، قاعده' ('approved model, rule'). The Persian shape shows the regular prothetic e- that Persian inserts before an initial s + consonant cluster (as in استکان, اسپانیا, استخر), giving es-tāndārd, and the written final -د follows the French/English spelling rather than French pronunciation. Strictly the French word standard is itself a re-borrowing from English standard, which continues Old French estandart, so the Persian word is a great-grandchild rather than a direct continuation of Nourai's French box; the arrow French → Persian is nevertheless exactly what Mo'in says. The gloss 'a hard standing rule' is Nourai's etymologizing paraphrase, not a Persian sense.\",\n     \"derivation_fa\": \"«استاندارد» وام‌واژه‌ای اروپایی از سدهٔ چهاردهم هجری است و معین آن را با نشانهٔ «[فر.]» (فرانسه) می‌آورد: «نمونه تصویب شده، قاعده». الف آغازین همان «الف پیشافزوده» فارسی است که پیش از خوشهٔ س + همخوان می‌آید (مانند استکان، اسپانیا). نکتهٔ باریک این است که واژهٔ فرانسهٔ standard خود از انگلیسی بازوام گرفته شده، پس فارسی نوادهٔ غیرمستقیم estandart فرانسهٔ کهن است؛ با این حال پیکان فرانسه ← فارسی درست است. معنای «قاعدهٔ سخت‌ایستاده» تفسیر ریشه‌شناختی نورایی است، نه معنای فارسی آن.\",\n     \"sources\": [\n      \"https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D8%A7%D9%86%D8%AF%D8%A7%D8%B1%D8%AF/\",\n      \"https://www.etymonline.com/word/standard\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:239\", \"status\": \"supports\", \"note\": \"Mo'in s.v. استاندارد, read at abadis.ir/fatofa/استاندارد: '( ا攎 ) [ فر. ] (ا攎. ) نمونه تصویب شده ، قاعده .' — the tag [فر.] = French is precisely Nourai's arrow. Print pagination not verifiable online, but 239 is consistent with اسطبل at 266.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt (searched استاندارد)\", \"stance\": \"silent\", \"note\": \"No hit — expected, since Borhan-e Qate' is a 17th-century dictionary and the word is a modern loan; Mo'in added no such headword to his edition.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, incoming/ARY/ARY_pages.txt (searched استاندارد)\", \"stance\": \"silent\", \"note\": \"No hit; Aryanpur's book covers inherited Indo-European vocabulary, not modern European loans.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt, searched 'standard')\", \"stance\": \"silent\", \"note\": \"No hit (1893, and loanwords of this kind are outside its scope).\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"English\",\n     \"words\": \"standard\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"English standard is Middle English, a shortening of Old French estandart, with Medieval Latin standardum beside it; the earliest English use is the military one ('flag borne on a pole as a rallying point', 12th century, famously the Battle of the Standard, 1138). From the royal standard as a fixed point come the senses 'authorized exemplar of a weight or measure' (14th c.) and hence 'norm, criterion'; Middle English also used the word of various upright things (posts, candlesticks), a usage Etymonline attributes to association with the verb stand. The Old French → English step is beyond dispute; the node inherits the uncertainty of node #6 about where Old French got the word, which is why this is 'plausible' rather than 'confirmed'.\",\n     \"derivation_fa\": \"انگلیسی standard کوتاه‌شدهٔ estandart فرانسهٔ کهن است که نخست در معنای نظامی «درفش» به کار رفته (نبرد معروف the Standard در ۱۱۳۸ م.) و سپس از «درفش شاهی به‌مثابهٔ نقطهٔ ثابت» به معنای «معیار رسمی وزن و پیمانه» (سدهٔ ۱۴ م.) و سپس «هنجار» تحوّل یافته است. این پیکان (فرانسه ← انگلیسی) قطعی است؛ تنها ابهام همان است که در گره شمارهٔ ۶ گفته شد.\",\n     \"sources\": [\"https://www.etymonline.com/word/standard\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. sta- II.1.c: 'Old French estandard, rallying place: STANDARD.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. standard, n. (KLN_1966.txt l.36582)\", \"stance\": \"partial\", \"note\": \"Klein agrees that English standard comes from OF estendard/estandard but derives the French word from estendre < L. extendere, not from Germanic *standan.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sta-\", \"stance\": \"supports\", \"note\": \"Same chain as the chart.\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"English\",\n     \"words\": \"stand, station, steel\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The three words all belong to the root box, but only one of them really hangs from the Germanic verb. (i) stand: Old English standan directly continues Proto-Germanic *standaną — correct. (ii) station: NOT Germanic. Middle English/Old French station < Latin statiō, statiōnem 'a standing still, post, guard-post', a *stə-ti- formation; Watkins lists it under II.5.b 'Latin statiō, a standing still: STATION', i.e. it belongs in Nourai's own Latin box #10/#11, not under standan. (iii) steel: Old English stīle/stēli < Proto-Germanic *stahlija-/*stahla- 'that which stands firm', which Pokorny (p.1011) and Watkins assign to the extension *stāk-/*stak- — Pokorny equates Germanic *stahla- with Avestan staχra- 'strong, firm', IE *stāk-lo- — so it descends from Nourai's third headword Stâk, not from *standan. The node is therefore right about the root and wrong about the branch for two of its three words.\",\n     \"derivation_fa\": \"هر سه واژه به همین ریشه بازمی‌گردند، امّا تنها یکی از آن‌ها واقعاً از فعل ژرمنی می‌آید. stand از انگلیسی کهن standan و ادامهٔ مستقیم *standaną است. امّا station از لاتین statiō «ایستگاه، پاسگاه» (ساخت *stə-ti-) و از راه فرانسه وارد انگلیسی شده و جای آن در جعبهٔ لاتین (گره ۱۰/۱۱) همین نمودار بود، نه زیر standan. steel نیز از ژرمنی آغازین *stahla- است که پوکورنی (ص ۱۰۱۱) آن را با staχra- اوستایی «سخت، استوار» برابر می‌نهد و به گسترش *stāk- می‌بندد، نه به *standan. پس ادعای نورایی دربارهٔ ریشه درست است امّا شاخهٔ دو واژه را نادرست کشیده است.\",\n     \"sources\": [\"https://www.etymonline.com/word/standard\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. sta- puts STAND under Germanic *standan (II.1.a) but STATION under 'b. Latin statiō, a standing still: STATION' (II.5.b), and STEEL under the separate root entry 'stak-. To stand, place … 2. Suffixed form *stāk-lo- in Germanic *stahla- in Old English stēli, style, steel (< “that which stands firm”): STEEL. [Pok. stak- 1011.]' (AHD_watkins1985.txt line 1001). So Nourai's own reference assigns two of the three words to other branches.\"},\n      {\"ref\": \"POK\", \"status\": \"partial\", \"note\": \"IEW p.1011 s.v. stak-, stek-: 'ahd. stahal u. m., aisl. stal u. … ‚Stahl’ … germ. *stahla- wohl = avestan staχra-, idg. *stāklo-' — steel belongs to the Stâk extension.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.vv. stand / station / steel\", \"stance\": \"partial\", \"note\": \"Klein s.v. station: 'fr. L. statiō, gen. -ōnis, “a standing, standing still, post, station”, fr. stat-, pp. stem of stāre' — the Latin, not the Germanic, line.\"},\n      {\"src\": \"POK\", \"where\": \"IEW pp.1007-1008 and 1011\", \"stance\": \"partial\", \"note\": \"Germanic standan at 1007-8 (for stand) but Germanic *stahla- at 1011 under stak-.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat (SKT.txt, searched 'stabulum', 'estandard')\", \"stance\": \"silent\", \"note\": \"No usable hit in the OCR.\"}\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"Latin\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The empty Latin box stands for the whole stāre / status / sistere family that feeds node #11: Latin stō, stāre 'to stand' (*stə-yō, beside Umbrian stahu), its participle status (< *stə-to-), the u-stem noun status, -ūs 'position, condition', the causative statuere 'to set up', the reduplicated present sistō, sistere 'to set, place, stop' (< *si-st(e)h₂-), and the adjective stabilis. Watkins's item I.3 lists exactly this set and hangs Nourai's English words off it; Pokorny p.1004-1005 has 'lat. sisto ‚stelle’ … lat. stō (stāre, stetī) = umbr. stahu ‚stehe’'. The unlabelled box is faithful to the tree, it simply names no form.\",\n     \"derivation_fa\": \"جعبهٔ لاتینی بدون واژه، نمایندهٔ خانوادهٔ stō/stāre «ایستادن»، اسم مفعول status، اسم status, -ūs «حالت، مقام»، فعل سببی statuere و فعل دوگان‌سازی‌شدهٔ sistō (از *si-st(e)h₂-) است که همهٔ واژه‌های گره ۱۱ از آن‌ها می‌آیند. پوکورنی (ص ۱۰۰۴–۱۰۰۵) و واتکینز همین مجموعه را می‌دهند؛ پس جعبه درست است و تنها صورتی را ننوشته است.\",\n     \"sources\": [\"https://www.etymonline.com/word/stable\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. sta- I.3: 'Latin stāre … to stand, with its past participle status … and derivatives statūra … and statuere, to set up, erect, cause to stand: … CONSTANT, CONSTITUTE, … (COST), … DISTANT, … EXTANT, INSTANT, … SUBSTANCE …'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW pp.1004-1005\", \"stance\": \"supports\", \"note\": \"'lat. sisto ‚stelle’, umbr. sestu ‚siste’ … lat. stō (stāre, stetī) = umbr. stahu ‚stehe’, *stā-iō; altlat. wohl auch trans. ‚stellen’.'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.604-606 s.v. stā-\", \"stance\": \"supports\", \"note\": \"Same Latin material (stāre, status, sistō) in the article Pokorny abridges.\"}\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"English\",\n     \"words\": \"constant, cost, distance, exit, instant, substance, store, resist, statistics, system; stable 2\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The list is copied from Watkins's AHD appendix, and most of it is right: CONSTANT (constāre), COST (OF couster < Vulgar Latin *costare < constāre), DISTANT (distāre), INSTANT (instāre), SUBSTANCE (substantia), RESIST (resistere, from the reduplicated sistere), STATISTICS (Latin status, -ūs, via German Statistik, 18th c.), STORE (Old French estorer < Latin instaurāre, Watkins IV.3.a), and stable 2 'steady' (ME/OF estable < Latin stabilis 'firm-standing', the -bilis of which is the same *-dhli- suffix as in stabulum) — so the two 'stable' words of this page are genuine doublets. Two items do not belong where they stand. (a) exit: Latin exitus / exīre is ex- 'out' + īre 'to go', PIE *h₁ey- 'to go', with no connection to *steh₂-; the printed page (pdf 475, image saved at data/verification/sources/refs/ocr/BOOK/475.png) really reads 'exit', so the extraction is faithful and the slip is Nourai's own — almost certainly for AHD's EXTANT (Latin exstāre) or EXIST (Latin exsistere), both of which Watkins does list under this root. (b) system: Greek sýstēma from syn-histánai, taken into Late Latin systēma and thence into French/English; Watkins puts it under III.1.b, the Greek branch (histánai), so drawing it from a Latin box is inexact though the root is the same.\",\n     \"derivation_fa\": \"فهرست این جعبه رونوشتی از پیوست ریشه‌های AHD است و بیشتر آن درست است: constant، cost، distance، instant، substance، resist، statistics، store و stable ۲ «پایدار» (از stabilis لاتین که پسوند -bilis آن همان *-dhli- است و بنابراین دو واژهٔ stable این صفحه دوگانهٔ ریشه‌ای‌اند). امّا دو مورد جای درستی ندارند: یکی exit که از لاتین exīre = ex- + īre «رفتن» و از ریشهٔ *h₁ey- است و هیچ پیوندی با این ریشه ندارد؛ بررسی تصویر صفحهٔ چاپی نشان می‌دهد که خود کتاب «exit» نوشته، پس خطای چاپی کتاب است و نه خطای خوانش اسکن؛ بسیار محتمل صورت درست extant (یا exist) بوده که هر دو در AHD ذیل همین ریشه آمده‌اند. دیگری system است که از یونانی sýstēma می‌آید، نه از لاتین؛ یعنی شاخهٔ یونانی همین ریشه.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"constant, cost, distance, exit, instant, substance store, resist, statistics, system, stable 2 : steady\",\n     \"correct_form\": \"extant (AHD's word; or exist) in place of 'exit'\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/exit\",\n      \"https://www.etymonline.com/word/stable\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. sta- (line 997) lists under the Latin branch 'CONSTANT, … (COST), … DISTANT, … EXTANT, INSTANT, … SUBSTANCE', under sistere 'ASSIST, CONSIST, DESIST, EXIST, INSIST, … RESIST', under status, -ūs 'STATE, STATISTICS, STATUS', under instaurāre 'STORE', under stabilis 'ESTABLISH, STABLE¹' and under Greek histánai '… PROSTATE, SYSTEM'. There is no EXIT anywhere in the article; and SYSTEM stands in the Greek, not the Latin, section.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.vv. stable (adj.), store, system\", \"stance\": \"partial\", \"note\": \"Klein s.v. stable, adj.: '… fr. L. stabilis, “firm, steadfast, stable”, fr. stāre …' — supports stable 2; but his 'exit' entry is 'fr. L. exitus, fr. exire, fr. ex- and īre, “to go”', i.e. a different root.\"},\n      {\"src\": \"POK\", \"where\": \"IEW p.1004-1010 (stā-)\", \"stance\": \"partial\", \"note\": \"Pokorny's stā- article contains stāre, status, sistō, stabilis, instaurāre and Greek hístēmi — but nothing of exīre, which stands at IEW 293 ff. under 1. ei- ‚gehen’.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.604-606\", \"stance\": \"partial\", \"note\": \"Same: the Latin stā- family, no exīre.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Stâi 1, Tâi\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *(s)teh₂y- (traditional *(s)tāi-) 'to conceal, to steal' (Pokorny 1010; Walde-Pokorny II 610)\",\n   \"note\": \"Pokorny's lemma is exactly '(s)tai- / Meaning: to conceal; to steal … Page(s): 1010' (POK_full.txt l.80996 ff.), with the material 'Old Indic stāyát ‚clandestine’, stāyú-, tāyú- ‚thief’ … steya-m ‚theft’, stena- ‚thief’; Avestan tāyu- ‚thief’, taya- ‚theft’ … Hittite tāyezzi ‚stiehlt’'. Nourai's double headword 'Stâi 1, Tâi' correctly renders the s-mobile: the root appears both with and without initial s- (Skt. stāyú- beside tāyú-, Av. tāyu-), which is why Pokorny writes the parenthesized (s)-. The page number, the language label and the gloss are all exact. Watkins/AHD has no entry for this root (no English word continues it; English steal belongs to Watkins's ster-⁴ 'to rob, steal', Pok. 1028), so AHD is silent rather than contradictory.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *(s)teh₂y- «پنهان کردن؛ دزدیدن» در پوکورنی صفحهٔ ۱۰۱۰ ثبت شده و همان جا سنسکریت stāyú-/tāyú- «دزد»، stena- «دزد»، steya- «دزدی» و اوستایی tāyu- آمده است. دوگانگی سرواژهٔ نورایی («Stâi ۱، Tâi») بازتاب همان پدیدهٔ معروف s متحرک (s-mobile) است که ریشه را گاه با s آغازین و گاه بدون آن می‌آورد. ادعای نورایی دربارهٔ خود ریشه کاملاً درست است؛ اختلاف تنها در شاخهٔ ایرانی غربی («ستدن») است که در گره‌های ۱ و ۲ می‌آید.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%AF%D9%86\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:1010\", \"status\": \"supports\", \"note\": \"POK_full.txt l.80996: 'Root / lemma: (s)tai- / Meaning: to conceal; to steal / Material: Old Indic stāyat ‚clandestine, hide, conceal’, stāyú-, tāyú- ‚thief’ (= Old Church Slavic taj Adv. ‚secret’ …); steya-m ‚theft’, stena- ‚thief’; Avestan tāyu- ‚thief’, taya- ‚theft’ … Hittite tajezzi, tayazzi ‚stiehlt’. References: WP. II 610 … Page(s): 1010.' Exact match to Nourai's root box.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.610 (running head '(s)tai- — stai-, sti-, sti-a-')\", \"stance\": \"supports\", \"note\": \"'(s)tāi- ‚heimlich um etwas bringen, hehlen, stehlen’; Wzansatz nach Schulze KZ. 27, 426. Ai. stāyát ‚heimlich, verborgen’, stāyú-ḥ, tāyú-ḥ ‚Dieb’ … steya-m ‚Diebstahl’, stená-ḥ ‚Dieb’; av. tāyu- ‚Dieb’, taya- ‚Diebstahl’ … air. táid ‚Dieb’ … abg. taj ‚heimlich’.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. tāios (IEC.txt line 18197)\", \"stance\": \"supports\", \"note\": \"'tāios, us ‚secretive; secretiveness; secret; silence; theft; thief’. WP II, 610 Skt. tāyūh, m. “thief”; Av. tāyus, m. id., tāyō, m. “theft”; Hitt. cf. tāyi-, v. “steal” …'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 11.57 THIEF, p.790 (SYN.txt lines 20069-20080)\", \"stance\": \"supports\", \"note\": \"'1. IE group based on *(s)tāi-. Walde-P. 2.610. Ir. táid; ChSl. tatĭ, etc.; Skt. tāyu- (RV), also stāyu-, Av. tāyu-, Skt. stena-; cf. ChSl. taj “secretly”, tajiti “hide” … Hitt. tāyézzi “steals”.' — Nourai's SYN:790 is the same page.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 (searched for a (s)tāi- / 'conceal, steal' root)\", \"stance\": \"silent\", \"note\": \"No such root in the appendix; the nearest is 'ster-⁴. To rob, steal … Germanic *stelan in Old English stelan, to steal: STEAL. [Pok. 3. ster- 1028.]' (line 1021), which is a different root — so the appendix simply has no English reflex of *(s)tāi-.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Old Persian\",\n     \"words\": \"stan, sta 3\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"There is no attested Old Persian verb 'to steal' of this shape: Kent's lexicon has only stāna- 'place' and the compound ava-stā- (imperfect avastāya), i.e. the root stā- 'stand', and nothing glossed 'steal' or 'thief' at all. What Nourai is transcribing is Abolghasemi's entry for ستدن (FFD p.59), which sets up an Old Iranian — «ایرانی باستان», a reconstruction, not attested Old Persian — root STAN glossed «گرفتن» ('to take'), with a past stem *stə-ta- (weak grade, the -n- dropped in the weakening) and a present stem *stāna-. Modern Iranian etymology puts that root elsewhere entirely: Cheung (Etymological Dictionary of the Iranian Verb, 2007: 361) sets up '*staHn ? “to take” … perhaps originally a pres. n-stem of *staH', from PIE *st(e)H₂n- 'to (want to) buy; fix (a price, one's mind on something)' (LIV 590 f.; Pok. 1004 ff.), with Latin praestināre, dēstināre, obstināre as the cognates. On that account the node belongs under entry 0's root 'to stand', not under 'to steal'. So: the language label is wrong (Old Iranian reconstruction, not Old Persian), the gloss 'to steal' is Nourai's own, and the root attachment is the 19th-century view.\",\n     \"derivation_fa\": \"در پارسی باستان فعلی به معنی «دزدیدن» از این خانواده گواهی نشده است؛ در واژه‌نامهٔ کنت تنها stāna- «جای» و ریشهٔ stā- «ایستادن» آمده است. آنچه نورایی آورده برگرفته از مدخل «ستدن» در کتاب ابوالقاسمی (ص ۵۹) است که «ایرانی باستان» (و نه پارسی باستان) می‌گوید و ریشه را STAN به معنی «گرفتن» می‌داند، نه «دزدیدن». چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (۲۰۰۷، ص ۳۶۱) این ریشه را *staHn «گرفتن» و احتمالاً ستاک حال نون‌دار از *staH «ایستادن» می‌داند. پس پژوهش امروزی این گره را از ریشهٔ «دزدیدن» جدا می‌کند و به ریشهٔ «ایستادن» می‌بندد.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"FFD:59\", \"status\": \"partial\", \"note\": \"Abolghasemi, ماده‌های فعل‌های فارسی دری p.59 (FFD_pages.txt leaf 63, pdf page 64), s.v. ستدن: 'ستد < فارسی میانه stad < ایرانی باستان *stə-ta- … stə صورت ضعیف ریشهٔ STAN است به معنی «گرفتن»، برای ضعیف کردن ریشه n حذف شده است. ستان < فارسی میانه stān < ایرانی باستان *stāna-' — the page is right and the forms are right, but the source says 'Old Iranian' not 'Old Persian' and glosses the root 'to take', not 'to steal'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon (KNT_full.txt; searched 'steal', 'thief', 'stan')\", \"stance\": \"contradicts\", \"note\": \"The only entries of this shape are 'stāna- “place” (§160.Ib)' (line 23892) and an ava- + stā- imperfect (line 24113); there is no Old Persian verb 'to steal' at all, so the language label of the node is unsupported.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p.361 s.v. *staHn (CHEUNG.txt l.23573 ff.)\", \"stance\": \"contradicts\", \"note\": \"'*staHn ? “to take” … © This root is perhaps originally a pres. n-stem of *staH (?). «PIE pres. n-stem *st(e)H₂n- “to (want to) buy; fix (a price, one's mind on something)” ? = LIV: 590 f. | Pok.: 1004 ff. •IE COGNATES: Lat. prae-stinare “to buy, fix (a price)”, de-stināre …, ob-stinare …' — root 1004 (stand), not 1010 (steal).\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. stadan (PHD.txt line 570)\", \"stance\": \"partial\", \"note\": \"'stadan, stān- [YNSBWN-tnʹ < A ynsbwn, √ nsb | M ʾstd, ʾstn-, N sit~] take.' — the Middle Persian continuant means 'take', not 'steal'.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no.709 p.157\", \"stance\": \"supports\", \"note\": \"Horn is the one source that does attach the verb to this root (quoted in full on node #2) — the view Nourai follows.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"setâdan «ستادن ( استدن ، ستدن )»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Persian word is genuine and old: New Persian ستدن / ستادن / ستاندن (sitadan, sitādan, sitāndan) 'to take, take away, seize', present stem ستان sitān-, continuing Middle Persian stadan / stān- (written with the Aramaic ideogram YNSBWN-tnʹ, MacKenzie 'take'; Nyberg 'to take, in all senses') and Parthian ʾistān-; the Ferdowsi line quoted in the box, چنین گفت کاین را نشاید سِتَد, means 'he said this must not be taken', not 'stolen'. The disagreement is over the root. Horn no. 709 (p.157 — exactly Nourai's citation) derives sitāden 'wegnehmen' from 'ai. skr. √stā- ‚stehlen’ in stāyát, stāyú- (neben tāyú-) ‚Dieb’, stená- ‚Dieb’ … aw. tāyu- ‚Dieb’', i.e. precisely this chart. Hübschmann (Persische Studien p.74, revising Horn's very number) already balked: 'Hier kommt auch der Präsensst. stān- häufiger vor als stan-. Wrzl. stan?' — he proposes a root stan-. Modern work follows Hübschmann, not Horn: Cheung 2007: 361 sets up Proto-Iranian *staHn 'to take' (n-stem present to *staH 'stand'), PIE *st(e)H₂n- 'to fix a price, to buy', with Latin dēstināre / praestināre / obstināre and Armenian stanam 'I receive, acquire'; Wiktionary follows the same line ('Proto-Iranian *staHn- “to take” … a suffixed form of *stnéh₂ti “to stand”: “to cause to stand” > “to fix (a price)” > “to take”'). On the modern view the word belongs to entry 0 (Stâ), and the sense 'steal' in the gloss is a contextual extension of 'take away'.\",\n     \"derivation_fa\": \"واژه درست است: فارسی نو «ستدن/ستادن/ستاندن» «گرفتن، بازستاندن» با ستاک حال «ستان»، از فارسی میانه stadan/stān- (به هزوارش YNSBWN-tnʹ) و پارتی ʾistān-. اختلاف بر سر ریشه است: هرن (شمارهٔ ۷۰۹، ص ۱۵۷ — همان ماخذ نورایی) آن را به ریشهٔ سنسکریت √stā- «دزدیدن» می‌بندد؛ ولی هوبشمان (مطالعات فارسی، ص ۷۴) همان‌جا در نقد هرن پیشنهاد می‌کند که ریشه stan باشد، و چونگ (۲۰۰۷) ایرانی آغازین *staHn «گرفتن» را بازمی‌سازد که ستاک حال نون‌دار ریشهٔ *staH «ایستادن» است و هم‌ریشهٔ لاتین dēstināre و ارمنی stanam می‌باشد. بیت فردوسی هم «ستدن» را به معنی «گرفتن» به کار برده است، نه «دزدیدن». نتیجه: پژوهش امروزی این پیکان را رد می‌کند و این واژه را به ریشهٔ «ایستادن» (همان مدخل نخست همین صفحه) می‌بندد، هرچند ماخذ خود نورایی (هرن) سخن او را تأیید می‌کند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%AF%D9%86\",\n      \"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%A7%D9%86%D8%AF%D9%86\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"HRN:157\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie no.709, p.157 (HRN.txt leaf 178): '709. sitāden ‚wegnehmen’, Praes. sitān-em, siteden, isteden, sitānden. phlv. pāz. statan (PPGl.). ai. skr. √stā- ‚stehlen’ in stāyát ‚verstohlen’, stāyu- (neben tāyá-) ‚Dieb’, stená- ‚Dieb’, steya- ‚Diebstahl’; aw. tāyu- ‚Dieb’, taya- ‚Diebstahl’; vergl. ksl. tajǫ, taiti ‚verbergen’, air. táid ‚Dieb’.' The page number is exact and the content is exactly Nourai's arrow.\"},\n      {\"ref\": \"BQT\", \"status\": \"not_found\", \"note\": \"Searched BQT_v1_pages.txt and BQT_v2_pages.txt for ستدن / ستادن / استدن: Borhan has no headword ستدن with an etymological footnote; the hits are incidental glosses ('بمعنی استدن و گرفتن' at line 3205, 'ستدن چیزی با پرداختن بهای آن' = 'to buy', line 11847) and a Mo'in footnote reading a Pahlavi word as ستدن (line 3219). Nourai cites BQT with no page, so nothing more precise can be checked. Note that the incidental glosses give 'take/buy', not 'steal'.\"},\n      {\"ref\": \"FFD:59\", \"status\": \"partial\", \"note\": \"Same entry as node #1: FFD p.59 derives ستد from MP stad < Old Iranian *stə-ta-, root STAN 'گرفتن' (to take); it says nothing about stealing and nothing about PIE *(s)tāi-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p.361 s.v. *staHn (CHEUNG.txt l.23573 ff.)\", \"stance\": \"contradicts\", \"note\": \"'*NWIR: NP sitādan/sitān- “to take, carry away; stand, stay”, … Kurd. (Kurm.) standin/stēn- … «PIE pres. n-stem *st(e)H₂n- “to (want to) buy; fix (a price …)” ? = LIV: 590 f. | Pok.: 1004 ff.' — the verb is referred to Pokorny 1004 (stand), not 1010 (steal).\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.74, note to Horn no.709 (HUB.txt leaf 84)\", \"stance\": \"contradicts\", \"note\": \"'709. Die ursprüngliche Infinitivform scheint sitādan gewesen zu sein, vgl. np. sitādan (neben sitadan) = pāz. stadan, ptc. stad Mīn. 61. 192. Hier kommt auch der Praesensst. stān- häufiger vor als stan-. Wrzl. stan?' — Hübschmann, correcting the very Horn number Nourai cites, already posits a root stan-, i.e. the modern analysis.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. stadan (PHD.txt line 570)\", \"stance\": \"supports\", \"note\": \"'stadan, stān- [YNSBWN-tnʹ < A ynsbwn, √ nsb | M ʾistd, ʾistān-, N sit~] take.' — confirms the Middle Persian ancestor and the New Persian continuant; the gloss is 'take'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. statan (NYB_vol2_glossary.txt line 3537)\", \"stance\": \"supports\", \"note\": \"'statan [YNSBWN-tnʹ] stān-, to take, in all senses … Paz. stadan stān- (Mx), stān- (Aog.); MPrthPrs pt. ʾstd, pres. ʾstn-, v. Verbum 189, Ghilain 71; NP sitadan sitān-.'\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Avestan\",\n     \"words\": \"tâyu\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Young Avestan tāyu- m. 'thief' is well attested (Vd. 4.1, 13.10, 18.15; Y. 11.3, 65.8; Yt. 10.20, 12.7; N. 63), beside taya- 'furtive, secret; theft' and tāiia- n. 'theft'. It continues PIE *teh₂y-u- 'thief', the s-less variant of the root, and is the exact equation of Sanskrit tāyú- (RV); the doublet with s- survives in Skt. stāyú-. Nourai's arrow root → Avestan and his page reference POK:1010 reproduce Pokorny's article verbatim.\",\n     \"derivation_fa\": \"واژهٔ اوستایی متأخر tāyu- «دزد» در وندیداد، یسنا و یشت‌ها بارها آمده است و در کنار آن taya- «نهانی؛ دزدی» ثبت شده است. بارتولومه در فرهنگ ایرانی باستان آن را «j. tāyav- m. ‚Dieb’» می‌آورد. این صورت ادامهٔ *teh₂y-u- هندواروپایی (گونهٔ بدون s) و هم‌ریشهٔ دقیق tāyú- سنسکریت است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:1010\", \"status\": \"supports\", \"note\": \"POK_full.txt l.80996 s.v. (s)tai-: 'Avestan tāyu- ‚thief’, taya- ‚theft’ … Page(s): 1010.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch s.v. tāyav- (BRT.txt line 12182)\", \"stance\": \"supports\", \"note\": \"'j. tāyav- m. ‚Dieb’: aḵa hazaŋhā … “ein Räuber, heimlich … ein Dieb” N.63 … V.4.1 … Y.65.8 … Yt.10.20'; and line 12012 'j., g. taya- 1) Adj. ‚verstohlen, heimlich’ 2) m. a) ‚Dieb’ b) ‚Diebstahl’', with the etymological note at 12013 'taya- ‚diebisch; Dieb’ (mit Schwachstufe *tūya- ‚Diebstahl’)'.\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.610\", \"stance\": \"supports\", \"note\": \"'av. tāyu- ‚Dieb’, taya- ‚Diebstahl’' in the (s)tāi- article.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. tāios (IEC.txt l.18197)\", \"stance\": \"supports\", \"note\": \"'Av. tāyus, m. ‚thief’, tāyō, m. ‚theft’.'\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Sogdian\",\n     \"words\": \"t`y\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Gharib's Sogdian dictionary has the word twice on the page Nourai cites: no. 9514 'tʿy' (Buddhist and Manichaean Sogdian) 'thief', with the explicit note '©<Av. tāyu' and the plural -t, oblique plural -ty; and no. 9518 'tʿyh' (Buddhist) 'thief', '©Av. tayw, Khwar. tah, MP tay'. Alongside stand no. 9516 tʿywny 'theft' and no. 9517 tʿyʿyckʿ 'stealthily'. Sogdian tāy /tāy/ continues Old Iranian *tāyu-, the u-stem having lost its final vowel in the Middle Iranian reduction of final syllables; the spellings tʿy / tʿyh are the ordinary Sogdian rendering of ā by aleph. Strictly, Sogdian continues the common Iranian etymon rather than descending from Avestan, but that is how Gharib herself phrases it, so the chart reproduces its source.\",\n     \"derivation_fa\": \"در فرهنگ سغدی بدرالزمان قریب، مدخل ۹۵۱۴ «tʿy» (سغدی بودایی و مانوی) «دزد» با یادداشت «< اوستایی tāyu» و مدخل ۹۵۱۸ «tʿyh» با یادداشت «اوستایی tāyu، خوارزمی tah، فارسی میانه tay» در همین صفحه آمده است؛ همچنین ۹۵۱۶ tʿywny «دزدی». صورت سغدی tāy ادامهٔ *tāyu- ایرانی باستان است که واکهٔ پایانی آن مانند دیگر واژه‌های ایرانی میانه افتاده است. دقیق‌تر آن است که سغدی نه از اوستایی بلکه از همان اصل مشترک ایرانی می‌آید، امّا عبارت نورایی عیناً برگرفته از ماخذ اوست؛ ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"SOD:384\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 9514 on the leaf whose running head is 384 and whose second column is numbered 385 (SOD_pages.txt leaf 451): '9514 tʿy B, M / tay / thief ©<Av. tayu ©pl. -t; ob. pl. -ty ⇒tʿyh, tyẓ / TSP 2.1113, 7.138, 24.2; Hen. Tales. 478.2.30 …'; and '9518 tʿyh B / tay ©Av. tayw, Khwar. tah, MP tay ⇒tyẓ, ty / thief / VJ 239; Benv. HitUE. 115'. The page number is exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae s.v. tāyav- (BRT.txt l.12182)\", \"stance\": \"supports\", \"note\": \"Gives the Avestan etymon tāyav- 'Dieb' from which Gharib derives the Sogdian word.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. tāios (IEC.txt l.18197)\", \"stance\": \"supports\", \"note\": \"Sets up IE *tāios/-us 'thief' with the Indo-Iranian forms, the family the Sogdian word belongs to.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 (searched 'tāyu', 'thief')\", \"stance\": \"silent\", \"note\": \"Cheung's dictionary covers verbal roots only; there is no entry for the noun.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"stena, sta ; stâyu, tâyu\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The nouns are all real and all in Pokorny's article: Sanskrit stená- m. 'thief' (RV), steya- n. 'theft', stāyú- and tāyú- m. 'thief' (both RV), with the adverb stāyát 'secretly, stealthily'; Buck (11.57, p.790) lists 'Skt. stena-, tāyu-, stāyu-, Av. tāyu-' under the same IE group '*(s)tāi-'. The one soft spot is the 'verb' printed in the box: there is no Sanskrit root √stā 'to steal' in Whitney or Monier-Williams — the attested verb is the denominative stenayati 'steals' (from stena-), and the old grammarians' stāy- rests on the adverb stāyát. Nourai is however following his own sources: Horn writes 'ai. skr. √stā- ‚stehlen’' and Pokorny's material begins with 'Old Indic stāyat', so the abstraction of a verb 'sta' is inherited rather than invented. The words and the root attachment are right; only the verbal citation form is an artefact.\",\n     \"derivation_fa\": \"همهٔ نام‌های این گره درست است: سنسکریت stená- «دزد»، steya- «دزدی»، stāyú- و tāyú- «دزد» (هر دو در ریگ‌ودا) و قید stāyát «نهانی»؛ باک (ص ۷۹۰) نیز همین مجموعه را ذیل ریشهٔ *(s)tāi- می‌آورد. تنها نکتهٔ قابل تأمل، فعل «sta» است: در فرهنگ‌های سنسکریت ریشهٔ √stā به معنی «دزدیدن» ثبت نشده و آنچه هست فعل اسم‌ساختهٔ stenayati است؛ امّا این انتزاع از خود ماخذ نورایی (هرن ص ۱۵۷: «ai. skr. √stā- ‚stehlen’») آمده است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:1010\", \"status\": \"supports\", \"note\": \"'Old Indic stāyat ‚clandestine, hide, conceal’, stāyú-, tāyú- ‚thief’ … steya-m ‚theft’, stena- ‚thief’' (POK_full.txt l.80996 ff.).\"},\n      {\"ref\": \"SYN:790\", \"status\": \"supports\", \"note\": \"Buck, Selected Synonyms 11.57 THIEF, p.790: 'Skt. stena-, caura-, moṣa- … Av. tāyu- … 1. IE group based on *(s)tāi- … Skt. tāyu- (RV), also stāyu-, Av. tāyu-, Skt. stena- … 8. Skt. stena-, tāyu-, stāyu-, Av. tāyu-, see above, 1.' The page is exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.610\", \"stance\": \"supports\", \"note\": \"'Ai. stāyát ‚heimlich, verborgen’, stāyú-ḥ, tāyú-ḥ ‚Dieb’ … steya-m ‚Diebstahl’, stená-ḥ ‚Dieb’.'\"},\n      {\"src\": \"IEC\", \"where\": \"Mann s.v. tāios (IEC.txt l.18197) and tat- (l.18228)\", \"stance\": \"supports\", \"note\": \"'WP II, 610 Skt. tāyūh, m. ‚thief’ …' — Mann sets up the noun, not a verbal root, which is the point of the 'plausible' verdict.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no.709, p.157\", \"stance\": \"partial\", \"note\": \"Horn does print 'ai. skr. √stā- ‚stehlen’', i.e. the verbal citation form Nourai copies — evidence that the 'sta' of the box comes from the 19th-century literature rather than from a Sanskrit dictionary.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-475.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF"
}
```


### [2026-09-14T02:57:35.704Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-475.json
```


## [2026-09-14T02:57:41.648Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -c \"攎\" data/verification/page-475.json; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/page-475.json'\ns=open(p,encoding='utf-8').read()\ns=s.replace('ا攎','اِ')\nopen(p,'w',encoding='utf-8').write(s)\nprint('fixed; remaining:', s.count('攎'))\nEOF\npython3 -m json.tool data/verification/page-475.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 475"
}
```


### [2026-09-14T02:57:42.880Z] TOOL RESULT

```
3
fixed; remaining: 0
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 8, 'plausible': 5, 'transcription_suspect': 1, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 12, 'not_checked': 1, 'partial': 6, 'not_found': 1}
books consulted: {'supports': 26, 'silent': 10, 'contradicts': 5, 'partial': 8} | by book: {'KLN': 7, 'WLD': 6, 'POK': 5, 'IEC': 4, 'HRN': 4, 'BQT': 3, 'AHD': 3, 'CHEUNG': 3, 'ARY': 2, 'SKT': 2, 'PHD': 2, 'BRT': 2, 'AFM': 1, 'LKT': 1, 'WEB': 1, 'KNT': 1, 'HUB': 1, 'NYB': 1}
```


## [2026-09-14T02:58:02.292Z] AGENT

Page 475 verified — `data/verification/page-475.json` written, `verify_check.py 475` shows **0 PROBLEM lines** (16/16 nodes).

**Verdicts:** roots 2 confirmed · nodes 8 confirmed, 5 plausible, 2 disputed, 1 transcription_suspect
Ref checks: 12 supports, 6 partial, 1 not_found, 1 not_checked · 18 books consulted (26 supports, 8 partial, 5 contradicts, 10 silent)

**Disputed**
- *Stâi 1, Tâi* #1 [Old Persian] `stan, sta 3` "to steal" — no such Old Persian verb exists (Kent has only `stāna-` 'place', root `stā-`); Nourai's source FFD:59 actually says «ایرانی باستان» root STAN «گرفتن» = *to take*, not steal.
- *Stâi 1, Tâi* #2 [Persian] `setâdan` — Horn 157 (Nourai's own ref) does derive it from Skt. √stā 'steal', but Hübschmann p.74 already corrected Horn ("Wrzl. stan?") and Cheung 2007:361 sets up PIr. `*staHn` 'to take' < PIE `*st(e)H₂n-` 'fix a price, buy' (Pok. 1004, the *stand* root), cognate with Lat. dēstināre; Wiktionary follows Cheung. The word belongs under entry 0, not here.

**transcription_suspect (book's own error, extraction is faithful)**
- *Stâ* #11 [English] list prints **"exit"** — Lat. exīre = ex- + īre, PIE *h₁ey-, unrelated to this root; the printed page (pdf 475) really reads "exit", so it is Nourai's slip for AHD's **EXTANT** (or EXIST). Same node: "system" is Greek-branch (σύστημα/histánai), not Latin. Page image archived at `data/verification/sources/refs/ocr/BOOK/475.png`.

**No extraction errors** — the JSON matches the printed page everywhere, including node #9's placement under Germanic.

Other notes worth the owner's eye: #6/#8 (French *estandard* → standard) marked plausible — AHD/Watkins back Frankish *standhard, but Klein and the OED call that folk etymology and derive it from estendre < extendere. #9 marked plausible: *station* is Latin-route (Watkins II.5.b) and *steel* comes from the *stāk-* extension (Pok. 1011), so only *stand* really hangs off Germanic *standan*. Node #2 (Arabic, empty box) plausible — the real route is Latin → Byzantine Greek στάβλος → Arabic إصطبل (attested 873 CE); Mo'in ([معر ـ لا.]) and Addi Shir confirm the rest. MON:266/239 page numbers couldn't be verified (Mo'in's 6-vol pagination isn't online) but the entry texts check out at abadis.ir.
