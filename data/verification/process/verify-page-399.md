# Verification process log — verify-page-399


## [2026-09-14T00:52:50.203Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 399 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-399.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-399.json. Write /home/sfmqrb/git/rishe/data/verification/page-399.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 399` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:52:51.296Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:52:52.124Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:52:52.140Z] TOOL RESULT

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


## [2026-09-14T00:52:52.630Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-399.txt"
}
```


### [2026-09-14T00:52:52.650Z] TOOL RESULT

```
1	=== PDF page 399 (book page 369) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Perk 2 : rib, chest  (refs POK:820)
4	#1 (parent #0) [Avestan] refs=POK:820 | paresu, peresu : rib, side
5	  #2 (parent #1) [Pahlavi] refs=SNS:114 | pahlŭg : side
6	    #3 (parent #2) [Persian] refs=AEF:415 | pahlŭ «پهلو ٢» : side
7	  #4 (parent #1) [Sogdian] refs=SOD:289 | prs` : side, hour, time
8	#5 (parent #0) [Sanskrit] refs=POK:820 | paršu, pâršu, pâršva : rib, side
9	--- entry 1 ---
10	ROOT Per-per-os -> redirect to Per 1
11	--- entry 2 ---
12	ROOT [Indo-European] Persna : heel  (refs POK:823)
13	#1 (parent #0) [Avestan] refs=POK:823 | pâšna : heel
14	  #2 (parent #1) [Pahlavi] refs=BQT:355 | pâšnak : heel
15	    #3 (parent #2) [Persian] refs=None | pâšneh «پاشنه» : heel
16	  #4 (parent #1) [Sogdian] refs=SOD:301 | pšn` : heel
17	#5 (parent #0) [Latin] refs=AHD | perna : ham, a sea mussel ; pernula : pearl
18	  #6 (parent #5) [English] refs=None | pearl
19	--- entry 3 ---
20	ROOT [Indo-European] Pestěno : breast  (refs POK:990)
21	#1 (parent #0) [Avestan] refs=KLN:1513; POK:990 | fštâna : breast
22	  #2 (parent #1) [Persian] refs=POK:990; BQT:405 | pestân «پستان» : breast
23	#3 (parent #0) [Sogdian] refs=SOD:70 | `štnh : breast
24	#4 (parent #0) [Greek] refs=POK:990 | sthĕthos : breast
25	  #5 (parent #4) [English] refs=KLN:1513 | stethoscope
26	
```


## [2026-09-14T00:52:55.690Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-399.json",
 "description": "Read source JSON for page 399"
}
```


### [2026-09-14T00:52:55.739Z] TOOL RESULT

```
{
  "pdf_page": 399,
  "book_page": 369,
  "entries": [
    {
      "root": {
        "name": "Perk 2",
        "lang": "Indo-European",
        "refs": "POK:820",
        "gloss": "rib, chest"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:820",
          "words": [
            {"translit": "paresu, peresu", "gloss": "rib, side", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:114",
          "words": [
            {"translit": "pahlŭg", "gloss": "side", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "AEF:415",
          "words": [
            {"translit": "pahlŭ", "gloss": "side", "script": "پهلو ٢"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:289",
          "words": [
            {"translit": "prs`", "gloss": "side, hour, time", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:820",
          "words": [
            {"translit": "paršu, pâršu, pâršva", "gloss": "rib, side", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Per-per-os",
        "redirect": "Per 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Persna",
        "lang": "Indo-European",
        "refs": "POK:823",
        "gloss": "heel"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:823",
          "words": [
            {"translit": "pâšna", "gloss": "heel", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:355",
          "words": [
            {"translit": "pâšnak", "gloss": "heel", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "pâšneh", "gloss": "heel", "script": "پاشنه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:301",
          "words": [
            {"translit": "pšn`", "gloss": "heel", "script": null}
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
            {"translit": "perna", "gloss": "ham, a sea mussel", "script": null},
            {"translit": "pernula", "gloss": "pearl", "script": null}
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
            {"translit": "pearl", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Pestěno",
        "lang": "Indo-European",
        "refs": "POK:990",
        "gloss": "breast"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:1513; POK:990",
          "words": [
            {"translit": "fštâna", "gloss": "breast", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:990; BQT:405",
          "words": [
            {"translit": "pestân", "gloss": "breast", "script": "پستان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:70",
          "words": [
            {"translit": "`štnh", "gloss": "breast", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:990",
          "words": [
            {"translit": "sthĕthos", "gloss": "breast", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:1513",
          "words": [
            {"translit": "stethoscope", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T00:52:57.994Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SNS','AEF','SOD','BQT','AHD','KLN','HRN','HUB','PHD','NYB','BRT','WLD','SKT','WEB','FSD','MON','ARY','IEC','SYN','CHEUNG','ISS','DKS']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-14T00:52:59.135Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo
```


## [2026-09-14T00:53:04.306Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['POK'], ensure_ascii=False, indent=1))\nprint(json.dumps(d['SOD'], ensure_ascii=False, indent=1))\n\"; ls data/verification/sources/refs/ | head -80"
}
```


### [2026-09-14T00:53:05.823Z] TOOL RESULT

```
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
{
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


## [2026-09-14T00:53:10.453Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 82[03]\" POK_full.txt | head -20; echo ---; grep -n \"Page(s): 990\" POK_full.txt | head"
}
```


### [2026-09-14T00:53:10.522Z] TOOL RESULT

```
66369:Page(s): 820 
66392:Page(s): 820 
66416:Page(s): 820 
66434:Page(s): 820 
66466:Page(s): 820-821 
67188:Page(s): 823 
67218:Page(s): 823 
67246:Page(s): 823 
67801:Page(s): 823-824 
---
79627:Page(s): 990 
79683:Page(s): 990-991
```


## [2026-09-14T00:53:11.871Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 54 55 56 57 58 59 60; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1))'' POK_03.txt | head -20; done"
}
```


### [2026-09-14T00:53:13.140Z] TOOL RESULT

```
=== leaf 54 ===
e',  porög-b  ds.,  poln.  prög  ,Schwene,  Haus,  Wohnung', progi  PI.  , Dielen,  Bänke';
62*
820
9
vielleicht    hierher  lat.    pergula    , Vorsprung,  Vorbau    an    einem   Haus©. Vorraum,  Weinlaube'  als  Demin.  eines  ^pergä  , Gebälk'. WP.  II  48,  WH.  II  288;  vgl.  oben  S.  819  Mitte.
2.  perg-  , Furcht,  sich  fürchten'?
Got.  faurhrtei,  Sigs.  fyrhtu  f.  , Furcht*;  got.  faurhts,  ahd.  as.  for(a)hi^
ags.  forht    ,furchtsam';    ahd.    as.  forhta   ,Furcht';    got.  faurhtjan,    ahd.
furhten,  for{a)hten  ,fürchten';   vielleicht  zu  toch.   A  B  'pärsk-,  A  prask-^-
B  präsk-  , fürchten',  A  praski,  B  proskoj  proskye  ,Furcht'  {-sk-  aus  -k-sk^y
WP.  II  48,  Holthausen  Altengl.  etym.  Wb.  112.
1.  perk-,  prek-  ,füllen,  auffüllen'?   Nur  indisch  und  irisch.
Ai.  prndkti  {prücati,  piparkü)  ^füllt,  gibt  reichlich;  mengt,  mischt*/ Partiz.  prkta-  ,gemischt,  erfüllt,  voll  von',  Aor.  apräk]  upala-prak^ii^. ,die  Handmühle  drehend',  sam-pfc  ,in  Berührung  stehend';  pracura-  ,viel,' reichlich';  mir.  ercaim  ,fülle'.
WP.  II  47,  Kuiper  Nasalpräs.  81.
2.  (perk-) :  prk-  ,glühende  Asche,  Kohle'.
Lit.  pirkänys  f.  PI.  , Asche  mit  glühenden  Funken',  lett.  pirkstis,  pirkstes PI.  ds. ;  air.  riches  f.  ,glühende  Kohle',  bret.  regez  ,Kohlenglut'  {^prki-stä^ vgl.  das  lett.  Formans);  unklar  cymr.  rhys-yn,  PL  rJiys-od  ,glühende Asche',  mit  anderem  Formans  acorn.  regihterij  KoUekt.  regyth  ds. ;  ob  als jSprühend'  zu  *sp(h)er-  , streuen,  sprühen'?  vgl.  lett.  spirgsti  , glühende Kohlen  unter  der  Asche'  unter  sp{h)er{e)g-  ,zucken,  sprühen'.
WP.  II  47,  Mühlenbach-Endzelin  III  223.
1.  perk-  , Rippe;  Rippengegend,  Brust'.
Ai.  pdrsu-  f.  jRippe,  gebogenes  Messer',  pärsvd-,  -m  ,Kippengegend, Seite',  av.  par^su-  f.  ,Rippe',  pdi-Qsu-  m.  ,Rippe,  Seite',  osset.  fars  ,Seite, Strich,  Gegend';  aksl.  pr^si  ,Brüste',  f.  PI.  wohl  aus  ,Rippengegend' ;  vgl. lit.  zem.  p\r§ys  f.  PI.  ,Brust  des  Pferdes'.
WP.  II  44  f.,  Trautmann  220.
=== leaf 55 ===
 ,Forelle',  as. fiirnia,  ags.  forn(e)  ds.  (*pr]c-nä)j  ablaut.  schwed.  färna  ,Weißfisch* (^perk-nä) ;
mit  -uo:  ahd. /aro,  mhd.  vare,  flekt.  varit-er  , farbig',  substantiviert  ahd. farawa  , Farbe'  {*pork'u6-)]  lat.-germ. /arzö  ,Lachsforelle'  (germ.  *farhjön-^ älter  *farhwjön-)-
andere  Bildungen:  gr.  nsoxog  m.  , Sperber'  (Aristot.),  nsQ-KÖ-Ttrsgog  ,weiß- köpfige  Geierart',  Tteoxd^eL  ,wird  dunkel,  schwarz';  Ttgö^,  -KÖg  f.  und ^QOTidgj  -ddog  ,Hirschkalb',  TtQcb^j  -y,ög  , Tautropfen' ;  neQy.7]  (lat.  perca  Lw.) , Barsch',  lat.  porcus  ,ein  Fisch  mit  Stachelflossen',  ligur.  FIN  Porco-bera (,Forellen  führend');  mir.  orc  (und  erc,  s.  oben)  , Lachs' ;  aisl.  fjgrsimgi' ,trachinus  draco'  (*perks-nkö-)  ]  redupl.  vielleicht  Ttartga^  ein  thrak.  See- fisch GForelle?');
vielleicht  hierher  durch  Diss.  eines  *perk-ro-s  zu  *pelcro-j  *polcrO':  lat. pulc{h)ery  alat.  polcher  , schön'  (=  ,bunt').
WP.  II  45  f.,  WH.  II  384;  Erweiterung  von  1.  per-.
5.  perk-,  prk-  ,auf reißen,  aufwühlen,  aufkratzen':  , Furche,  und  die  daneben aufgewühlte  Erde';  p^kä  , Furche'.
Ai.  pdHäna-  m.  ,Kluft,  Abgrund,  Einsenkung*;
lat.  porca  , Furche  im  Acker',  , Wasserabzugsrinne  im  Acker'  (porcu- letum  , Ackerbeet'  mars.  umbr.  jporculeta^)  ]  cymr.  rhych  ,Furche'  (mit expressivem  -kk)  vielleicht  =  bret.-rec'Ä  , Kummer*,  dagegen  mit  k  abret. 7'ec,  gl.  ,sulco',  ro-ricse[n]ti  ,sulcavissent' ;  gall.  rica  ,Furche*,  frz.  raie , Streifen';  Sihd.  furuh,  sigs.  furJi  f.  ,Furche',  aisl. /or  f.  , Abzugsgraben, Kanal'  (*p2'k-)j  hochstufig  norw. /ere  m.  , Ackerbeet';  nach  F.  R.  Schröder, Festgabe  K.  Helm  25  ff.  hierher  aisl.  Fjgrgyn  f.  als  , Göttin  der  Acker- furche';
lit.  pra-persis  , Blanke  im  Eis',  pra-par§as  , Graben',  peHeti  ,brennend schmerzen'  (von  Wunden) ;
dazu  *porkös  , Schwein'  (, Wühler').
WP.  II  46,  47,  WH.  II  340  f.
4.  perk-,  prek-,  prk-  ,f ragen,  bitten';  prk-skä-  ,Frage'.
1.  s£o-Präs.  *prk-sköj  woraus  *prskö :  Sii.  prcchdti  ^ira.gt\  av.  pdresaiti , fragt,  begehrt'  (Partiz.  parHa-\  ap.  aparsam  ,ich  frug';  arm.  e-harc  ,er hat  gefragt'  (:  ai.  d-pxcchat\  davon  das  Präs.  harcanem]  lat.  poscö  , fordere, verlange,  er  bitte';  ir.  arco  ,ich  bitte',  cymr.  arcTiaf,  corn.  arghaf  ds., mbret.  archas  ,il  commanda'  (air.  imm-chom-arc  ,gegenseitiges  Fragen, Begrüßen'  usw.)  mit  ar  aus  f  vor  dem  s  der  Grundf.  *prskö  (aus  *pxk-skö)',
822  f
lit.  per^Ä,  pirUi  ,für  jemanden  freien*  {pirslys  ^Freiwerber*),  wenn  mit analogischem  Präs.-Ablaut  e  statt  i;  dazu  a.1  prcchä  »Frage,  Erkundigung* =  arm.  harc  ds. ;  ahd.forsca  »Forschung,  Frage*  ist  Postverbale  znforscön »fragen,  forschen*;  lat.  postulö  ,fordere*  (Deminutiv  vom  Fartiz.  *posctoi zu  poscö))  im  Osk.-Ümbr.  ist  *porscö  zu  *perscö  umgebildet:  umbr.  per«- nivm  Imper.  Med.  ,precätorS  dazu  mit  (Formans  -(e)Zo-)  umbr.  persklu^ pesklu  ,supplicätiöneS  ferner  mars.  pesco  ,sacrificu
=== leaf 56 ===
mS  und  vom  Partiz. *pes[c]to-  aus:  osk.  pestlürriy  peeslüm  ,templum*,  woraus  messap.  nevayX^ , Bethaus*.
2.  Ai.  präS'  , (gerichtliche)  Befragung*,  av.  frasä  f.  ,Frage*,  ai.  prstha- (=  av.  parUa-)  ,Gerichtsf rage*,  prasnä-,  av.  frasna-  m.  ,Befragung,  Frage* (=  ahd. /ra^an  , Specht^  KZ  62,  31,  2),  arm.  harsn  ,Braut,  Neuvermählte, Schwiegertochter*  (vgl.  got.  fraihnan) ;  lat.  procus  ,Freier',  prex  f.  ,Bitte', precoTy  -äri  »bitten*,  umbr.  pepurkurent  3.  PL  Fut.  ,poposcerint* ;  got. fraihnan  ,f ragen*,  aisl.  fregna,  ags.  frignan  (und  to-Präs./ricnaw)  ds.,  as. Prät.  fragn]  ags.  friccea  ,Herold*;  germ.  *frehii-  in  aisl.  frUt  f.  Frage, Erforschung*,  ags.  frtht  f.  , Wahrsagung* ;  ahd.  fräga  ,Frage*  i^fräg-on^ -en,  frohen  ,fragen*),  aisl.  frägr,  ags.  gefrcege,  as.  gifrägi  ,berühmt*; ablaut.  ahd.  fergön  ,bitten* ;  aisl.  prositi,  bitten ;  lit.  Iterat.  praSaü^  -yti »fordern,  bitten*;  toch.  A  prak-j  B  prek-  , fragen*.
WP.  II  44,  WH.  II  346  f.
perk"u-s  , Eiche*,  daraus  vielleicht  , Stärke,  Kraft,  Leben,  Weltenbaum'  und ,Baum  des  Donnergottes  Perknuno-s'. Ai.  parkatl-  ,heiliger  Feigenbaum*,  nind.  pargäi  , Steineiche* ;  ven.  VN Quarqueni  , Eichenmänner*  (lat.  Relikt?);  NympMs  Percernibus  vielleicht  "^  " ligurisch  (Yaucluse);  lat.  quercus  f.  ,Eiche';  ital.-trent.  porca  ,Föhre* (rät.  *porca)]  kelt.  Hercynia  Silva  ,das  deutsche  Mittelgebirge*  (aus  *Per- kunia,  älter  *Perk'i^unia)j  cymr.  perth  L  ,Busch,  Hecke*  (*k^erkl/^-t-  ?) ;  kelt. VN  Querquerni  (goidel.)  in  Hispania  Tarrac. ;  aus  *Perkuniä  wohl  entlehnt germ.  *ferguniö,  ahd.  Fergunna  , Erzgebirge*,  mhd.  Virgunt  f.  _, Waldgebirge westlich  Böhmens*,  got.  fairguni  n.  , Gebirge*,  Sigs.firgen  ,Waldhöhe';  ahd. fereheihj  langoh.  f er eha  ,Speiseeiche*,  aisl.  ^'prr  m.  , Baum,  Mann*;  ablaut. ahd.  forha  ,Kiefer*,  ags. /wrÄ;  aisl. /wra  f.  »Föhre*, /^ri  n.  ,Föhrenwald*; aus  ahd.  *forh-ist  »Föhrenwald*  :  nhd.  Forst;  aus  ahd.  kien-forha  (kien- zu  ags.  cen  »Kienfackel*,  ablaut.  zu  ags.  cinan,  oben  S.  355)  wird  nhd. Kiefer;  unsicher  ob  nach  Vendryes  RC  44,  313 ff.  hierher  auch  got.  fairhus ,Welt*,  ags.  feorhy  ahd.  ferah  ,Leben*,  westgerm.  Alaferhuiae  (=  *Ala- ferhwiös),  zu  aisl.  flrär  {*firhw-jöR),  ags.  firas  PI.  ,Männer*  usw. ;  alit. perkünas  Donnergott,  lit.  perkünas  , Donner*,  perkünija  f.  , Gewitter*,  lett. p^rkuons   ,Donner,    Donnergott*,    apr.    percunis    , Donner';    aruss.    Perum

=== leaf 57 ===
823
Donnergott',  russ.  perün  ,Donnerkeil,  Blitz*  sind  volksetymol.  nach  slav. *perö  , schlage'  umgestaltet;  unklar  ist  ai.  Parjdnya-  , Gewittergott'  (s.  oben unter  3.  per-,  perg-).
WP.  II  42  f.,  47  f.,  WH.  II  402  f.,  Specht  KZ.  64,  10  f.,  68,  193 ff., Thieme,  Untersuchungen  zur  Wortkunde  des  Rigveda  71.
perS'  ^sprühen,  stieben,  spritzen  (bespritzt  =  gesprenkelt),  prusten^ ;  prso-s , Staub,  Asche'.
Ai.  pfsat,  pj-satd-m  n.  ,Tropfen';  pfsant-^  L  pfsa^l , gesprenkelt,  scheckig, bunt',  prsati  , scheckige  Kuh,  gefleckte  Antilope^;  av.  parhiya-  ,vom Wasser',  n.,  vielleicht  , Schneewasser' ;  aisl.  fors^  foss  m.  ,Wasserfall' ;
lit.  purslaSj  pursla  , Schaumspeichel',  pufkUi  ,wie  eine  Katze  prusten, schnarchen';  lett.  ^örsZa  , Flocke'  (von  Schnee,  Asche,  Wolle)  ablaut.  p^rsla ds. ;  (vgl.  lett.  sjpurslät  , prusten');  slav.  *parsa-  m.  ,Staub'  >  *porcJn  in aksl.  pi-achz  ds. ;  slav.  ptrsth  in  aksl.  prbstb  „^oUg",  (*p,rs-),  neben  sloven. prh  m.  ,Staub,  Asche'  (=  aisl.  fors),  pr^hati  ,streuen,  stieben',  öech.  prseti ds.  usw.;  toch.  AB  pars-  ,besprengen' ;  Partiz.  Akt.  papärs,  hit.  papparS- ,spritzen,  sprengen'.
WP.  II  50;  Trautmann  206  f.,  Erweiterung  von  1.  per-  ,spirühen'.
■persnä,  -sni-,  -sno-  , Ferse'.
Ai.  pärsni-  t,  av.  päSna-  n.  , Ferse';  gr.  rttegvi]  f.;  lat.  perna  f.  {^persnd) ,Hinterkeule,  Schweineschinken,  Schenkel,  Bein',  pernls  , schnell'  (mit  der Ferse);  got.  fairsna,  a.s.  f er sna,  ahd.fersana  , Ferse'  {*persna)j  Sigs.fiersin f.  ds.  (*persni-)]  hitt.  parsina  (leg.  parsna)  , Oberschenkel,  Lende',  par§- (a)näi-  ,hocken'  (auf  den  Oberschenkeln).
WP.  II  50  f.,  WH.  II  289  f.,  Pedersen  Hitt.  258.
pertb-  jStange,  Schößling'?
Arm.  ort""  (o-St.)  ,Weinstock,  Rebe';  gr.  TCtood-oq  m.  ,Schößling'  (vgl. -rtTÖlsfiog  :  rtöXefxog  usw.);  vielleicht  lat.  pertica  , Stange',  falls  nicht  aus per-ti-ca  zu  osk.  jpert  ,bis  zu'  aus  *jper-tij  also  ursprüngl.  ,Querholz';  vgl. cech.  jpHska  ds.,  S.  810.
WP.  II  49,  WH.  II  292  f.
I.  pes-  ,blasen,  wehen'  (s.  auch  2.  pes-  ,Staub,  Sand').
Aisl.  fQnn  f.  ,Schneewehe,  Schneehaufe'  (*faznö),  -fenni  n.  ds. ;  als  ,im  Win- de wehender  Faden':  ah d. /aso  m.,fasa  f.  ^Faser,  Franse,  Saum',  sgs.fces(ri) n.  ,Franse',  engl,  feaze  ,Fasern';  aisl.  fqsull  m.  ,B^iid',  mnd.  vese{n),  Spreu, Faser,  Franse',  ndl.  vezel  ,Faden',  ahd.  fesa  ,Spreu,  Spelze',  nhd.  Fehse, dän.  ßcBser^  älter  f{j)es  ,Fasern',  ahd.  fasön  ^untersuchen'  (*zerfasern) ;
824
aksl.  'p^chyrh  ,bulla,  Blase',  'pachati  ,ventilare,  agitare',  russ.  pacÄnui^, 
=== leaf 58 ===
 ^' ,wehen',  pdchnuh  ,duften,  riechenS  zapacA^  , Geruch,  Duft' usw. ;  russ.  pds,no  - ,Garnsträhne',  lett.  pudsm(i)s  ,Abteilung  zwischen  zwei  Endpunkten',  .soviel'" man  mit  zwei  Fingern  aus  der  Kunkel  Flachs  zieht';  6ech.-poln.  pochvQ  , ,Schwanz'  (, wedelnd'),  aksl.  o-pash  ds. ;  nasaliert  poln.  p^chnqc  ,anblasen,  J anwehen',  pqcJi,  p^ch  ,Witterung  (des  Hundes')  usw. ;  vielleicht  bulg.  "f; pasmina  ,Rasse'  (vgl.  ai.  tdntu-  ,Faden,  Faser,  Geschlechtsfaden,  Reih, der  Nachkommen,  Nachkommenschaft').
WP.  II  67,  Trautmann  229,  Vasmer  2,  320.
2.  pes-,  nasaliert  pens-  , Staub,  Sand'.
Ai.  pämm-,  pämsukd-  , Staub,  Sand',  av.  pqsnu-s  ds.;  ksl.  peshH  ,Sand'; vermutlich  als  ,der  wehende,  gewehte'  benannt  und  zu  1.  pes-  ,blasen'. WP.  II  68,  Trautmann  216  f.
5.  pes-,  pesos  n.  ,das  männliche  Glied'.
Ai.  päsas-  n.  =  gr.  neog  n.  ,penis',  gr.  rcöa^r]  f.  ds.,  lat.  penis  {*pesm8)'^ ahd.  faselj  ags.  fcesl,  ahd.  faselt  ,penis',  mhd.   vaselrint  ,Zuchtstier',  nhd. Faselschwein.    , Zuchtschwein*,  ablaut.  mhd.  vesil  ,fruchtbar',  visel  ,penis*. WP.  II  68,  WH.  II  281.
I.  pet-,  pet-,  petQ-  ,ausbreiten',  bes.  die  Arme.
Av.  pa&ana-  ,weit,  breit'  (das  d-  nach  pdi-dd^u-  ds.);
gr.  Aor.  Ttszdaaai,  rcer&aaL,  danach  TtsrdvvvfXL  , breite  aus,  öffne',  altes Präs.  Tthvriiii,  tcltvo)  (aus  *pet-),  nhaaixa  n.  , Vorhang',  nhaaog  m.  ,breit- krempiger  Hut',  Ttiralog  ,ausgebreitet',  nsraXov  n.  ,Platte,  Blatt',  naTavt] f.  , Schüssel'  (aus  *ftsTdvä]  daraus  lat.  patina  ds.);
lat.  pateö,  -ere  ,sich  erstrecken,  offenstehen' ;  dazu  pandö,  -ere  ,öffne, breite  aus'  (der  Wechsel  t :  d  erklärt  sich,  durch  alte  athemat.  Flexion nach  Kuiper,  Nasalpräs.  163),  passus  m.  , Schritt,  Klafter';  patera  ,flache Schale'  (aus  patina  durch  Einfluß  von  cratera?)]  ob  hierher  petllus  ,dünn und  schmächtig'??;  osk.  pa^[i^?]  ,patet',  patensins  ,panderent',  volsk.  Imper. an-patitu    *adpanditö' ;
schott.-gäl.  aitheamh  (*eitheamh)  , Faden'  (als  Maß),  =  acymr.  etem, ncjmr.  edau  ds.  (*petima)]
aisl.  fadmr  ,Umarmung,  Klafter,  Faden',  FIN  Fgd,  Gen.  Fadar,  ags. fasdm  mf.  ds.  , Faden,  Klafter',  engl,  fathom,  ahd.  fadam,  fadum  , Faden'; hierher  auch  ags.  foder,  engl,  fother,  nhd.  Fuder '^  ahd.  fuodar,  as.  föther^ ags.  födor  ,Wagenlast',  nhd.  Fuder,  aus  germ.  *födra-  ,das  Umfassende'; got./ojba,  mhd.  vade  f.  ,Zaun'  (als  ,Umfassung') ;  ahd.  fedel-gold  ,Blattgold' (:gr.  nhalov),  fraglich  ags.  gold-fell , Goldplatte',  mhd.  goltvel  ,Goldblech';
^Si^s!
«^
825
lit.  'petys  jSchulter^;  apr.  'pette  f.  ds. ;  pettis  m.  ^Schaufel,  Schulterblatt^;
hitt.  pattar,  Dat.  paddani  ,Tablett(?y.
WP.  11  18,  WH.  II  244  f.,  262,  Trautmann  217.
2.  pet'f  P^t^-  '  Pt^-f  Ptö~  (griech.  ptä-)  ,auf  etwas  los-  oder  niederstürzen, fliegen,  fallen'^;  dazu  ein  r/n-St.  Nom.  pet-r-(g),  Gen.  pet-n-es jFlügel^;  pet-ero-,  pet-onti  , fliegend^,  ptö-to-  , fallen d^
Ai.  pdtati
=== leaf 59 ===
  ^fliegt,  wirft  sich,  fällt^  (=  7t€T0j.iaL,  lat.  petö^  acymr.  liedant), Aor.  apaptat'j  petd-  in  Fut.  patisyati,  Supin.  pdtitum^  Partiz.  patitd-)] patdyati  , fliegt^  (=  gr.  7tOTaoi,Lai),  pätdyati  ,läßt  fliegen,  schleudert,  läßt fallen^  (dehnstufig  wie  päta-  m.  ;Flug,  Fall,  Sturz^,  gr.  noiiaoixai  ,flattre^), pra-pat-  , hineilen,  stürzen',  pdtman-  n.  ,Flug,  Pfad,  Bahn^  (:  Tc6Tt.iog^  nora- l^ög)',  av.  pataiti  ,fliegt,  eilt^,  ap.  ud-apatatä  ,erhob  sich^,  av.  patayeiti ,fliegt^,  acapastöis  Inf.  ,hinahzufallen^,  paitipasti-  f.  ,Entgegengehen,  -treten' (vgl.  ai.  ati-patti-  , Zeitablauf'),  von  einem  u-Präs.  parapad-ivant-  ,fortflie- gend  (vom  Pfeil)';  av.  täta-  (*ptätd-),  , fallend  (vom  Regen':  gr.  nrißzog  ds.);
arm.  t'^fcim  ,ich  fliege'  (*pter-i-sko).
gr.  hom.  nstoy,ai  ,fliege'  {iftrö(.irjv) ;  sonst  auch  Trsraf-iaij  emaTO  ,entflog', fcräg,  8ftTr]v,  dor.  ercxav,  Fut.  TtrrjaofxaL]  djyiVTtsrrjg  , schnell  fliegend',  nsrsvjvög, (*7TSTsaav6g)j  TtsTStvög  {^7T.8TBav6g)  ,geflügelj;,  ^üg^Q^,  Ttoir]  ,Flug',  rtOTävög, -Tjvög  ,zum  Fliegen  befähigt,  beflügelt,  fliegend',  noTdo^aL  (und  Ttorso^ai^ s.  oben)  ,flattre',  TtcjrdofxaL  ds.,  rcTTJaig,  bei  Suidas  irvrjfxa  ,Flug',  mrivog, dor.  TitGvög  ,fliegend^;
Stamm  TtEta-,  rtrd-  ,fliegen',  aber  Tters-,  tttj;-,  jttw-  mit  der  Bed. ,fallen' :  nt-TtTo)  (für  *7it-TtTü)  nach  qtrtxü))  , falle' ;  Perf.  TTfWwxcr,  Partiz. TtsrtTTjdyg,  att.  fCBTCxwg  aus  *jte7n;'öi(bg]  äTirvog  (Pind.),  dnir^g  (dor.  inschr.) ,nicht  fallend,  nicht  dem  Falle  ausgesetzt';  TiiTvia  ,falle',  sij-fcsrrjg  ,bequem, günstig',  TtQO-fiETrjg  ,vorwärts  fallend,  geneigt'  (:  ai.  pra-pat-),  Treaog  n. (Gen.  naasog  aus  *n€Teog)  ,cadaver',  nÖTfiog  ,Los,  Schicksal,  bes.  trauriges', noraf-iög  ,Fluß',  eig.  ,Wassersturz';  Ttröiia,  TtrcoaLg  ,Fall'  (:  yrfWwxa); fcrcjüTÖg  jfallend';
mit  der  Bed.-färbung  des  lat.  petere:  gr.  rtirvXog  ,heftige  Bewegung' (:  lat.  petulans]  vgl.  auch  if^Ttsaetv  ,impetum  facere');
endlich  hat  Ttzä-  :  tvtco-  :  rtra-  auch  die  wohl  aus  ,niederstürzen'  entw. Bed.  ,sich  niederducken'  und  , verzagt,  in  Furcht  sein':  y.aTa-TCTrjxriv  ,(die Pferde)  scheuten',  TtsnTrjcog  , geduckt',  TtTola  ,Scheu,  Schrecken'  {^ntcjJ^iöt, vgl.  Arjxd)  Utcba,  *Atc61Xo)v  Rxthog),  TCXo{C)eXv  ,erschrecken,  in  Bestürzung versetzen',  Pass.  ,von  Schrecken  ergriffen  werden';  mit  gutt.  Erw.  mr^GGia (*7rräx-jia))  ,ducke  mich'  (Aor.  zitxr^^a,  dor.  znxa'Aa  auch  trans. , erschrecken'; xaTa-7tTäyid)v),  TiTcoG-Kd^ct)  , ducke  mich  furchtsam,  fliehe',  tztwgglü  (*/rTa>x-
826
(Txtcü)    ds.;    Trrwg;   -xog  ,scheu,   flüchtig^   (m.   .HaseQ,    ablaut.   nzd^   m.  j^ , Feigling';    Gen.  tttöxos;  7tvoj%6g   ^Bettler';  zu  letzteren,   wie  es   scheint "^ auch  arm.  t'aJcöim,
=== leaf 60 ===
  t'ak'eay  ^sich  verbergen';
lat.  petöj  -ere,  -ivi,  Itum  ,auf  etwas  losgehen,  zu  erlangen  suchen,  ver-' langen'    (petl-tor,   -tio,   auch    wohl    petlgo    ,Räude'  als  , Befall');    petulant ^aggressiv,  keck,  mutwillig,  ausgelassen',  petulcus  jStoßend'  (von  '^petulm  " vgl.   zum  i-Formans  gr.   nlivlog),  impetus  , Anfall,   Angriff',    praepes  ,1^  * Fluge  vorauseilend;  schnell';
acymr.  hedant  ,volant',  ncjmr.  eh-edeg  ,das  Fliegen';  eh-edydd  m.  ,Lerche';
lett.  petU  ,Verlangen  haben,  nachforschen'.
r-und  iz-Bildungen :  1.  mit  dem  g^-Formans  ai.  patamgd-  ,fliegend,  Yogel', pataga-  ,Vogel'  (*pe<^-^o-s;  von  den  Indern  als  ,im  Fluge  gehend'  umge- deutet); 2iV.  fraptdrdjät-  (-jant-)  ,Vogel';  gr.  nzegv^,  -vyog  ,Flügel'  (vgl. ai.  patdru-);  das  Denom.  TtTsgvaao^ai  ,schlage  mit  den  Flügeln'  nach aid-vaau)  ,schüttle';  ahd.  fed{e)rah  ,Flügel',  anf rk. /e^Äeracco  ,alarum'  (-a-c- durch  Einfluß  von  ahd.  fedara-,  anf rk.  fethera) ;
2.  Ai.  pdtira-,  pdta-tra-  n.  , Flügel,  Feder',  patard-,  patdru-  fliegend, av.  patardta-  ,fliegend';  arm.  t'ir  ,Flug',  t'itefn  , Schmetterling'  (redupl.), t'ert'  , Blatt,    Laub'  {*pter-)]   gr.   nxeqöv  , Feder,   Flügel';   nreqLg    ,Farn';
lat.  acci-piteTj  -pitris  ,Habicht,  Falke'  (zum  1.  Glied  s.  unter  ^öku- ,schnell');  penna  ,Feder,  Flügel'  (*pe^nä);  alat.  pesna  aus  *pets-nä;  pinna ist  wohl  dial.  Form  für  penna]  pro(p)tervus  ,ungestüm  vordringend,  frech' {*pro-pteru-o-) ;
acymr.  eterin  , Vogel',  PL  atar^  ncjmr.  aderyn^  adar  ds.  (a  sekundär aus  e);  air.  en  , Vogel'  (^petno-)^  cymr.  edn,  acorn.  hethen  ds.,  abret.  ein- coilhaam  ,halte  Vogelschau',  mbret.  ezn,  nbret.  evn,  ein  ,Vogel',  acymr.  atan (*petf.no-)f  ncymr.  adain  , Flügel,  Arm'  (*pettn-),  bret.  (h)adan  ,Nachtigall^, mit  sekundärem  a,  wie  cymr.  ac^a/ , Flügel',  Hand  (*pete'mä)]  abret.  attanoc ,volitans';  mir.  ette,  nir.  eite  ,Fittich'  (aus  *pet-entiä),  mir.  ethait  ,Vogel, =  ai.   pdtanti   fliegend'  (*pet-onti) -,    mir.   eithre   n.    , Schwanz'    (*peterio-)]
ahd.  fedara,  anfrk.  fethera,  ags.  feder,  aisl.  fjgdr  f.  ,Feder'  (*petra) ; s}id.  fettähj  mhd.  vittich,  mnd.  vit(te)]c,  nhd.  Fittich-,
hitt.  pattar  n.,  Gen.  PL  paddanas  ,Flügel'.
*pt^i-,  pti'i  gr.  fCTaiü)  ,stoße  an  etwas  (intr.),  strauchle,  irre,  habe wobei  Unglück'  (TrraiW,  e7iTaLai.iaL,  iftTaia-^rjv),  seltener  tr.  ,stoßen,  um- stürzen', Ttrata^a  ,Schaden,  Verlust,  Unglück,  Niederlage',  id^vnxtcüv  ,ge- radaus  fliegend'  (wohl  eig.  ,geradaus  treffend  =  stoßend,  aufschlagendO, tctLXov  ,Feder,  Flaumfeder'.
WP.  IT  19  ff.,  WH.  II  282  f.,  297  f.
827
peu-,  peu9-:ph-  ^reinigen^  läutern,  sieben^;  pü-ro-,  pu-to-  ,reia^
Ai.  Trans,  'punäti,  Med.  pdvate  , reinigt,  läu
```


## [2026-09-14T00:53:24.933Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 224 225 226 227; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1))'' POK_03.txt | head -40; done"
}
```


### [2026-09-14T00:53:25.939Z] TOOL RESULT

```
=== leaf 224 ===
Macht'  (wohl  auch lett.  spXte  , Trotz',  spitigs  , trotzig');
aksl.  spSjg^  speti  , Erfolg  haben';  sp^ch^  m.  , Studium',  spesiti  , eilen';
aksl.  sporz  (=  ai.  sphird-  usw.)  , reichlich',  in  neueren  slav.  Sprachen auch  (und  wohl  das  ursprünglichere)  ,lange  dauernd,  lang  ausreichend', so  Tuss.  spöryj,  serb.  spor  ,lang  dauernd',  daher  anderseits  auch  ,lange ausreichend,  sparsam',  dech.  spory  , ergiebig,  ausgiebig*  und  ,sparsam,  spär- lich', spofiti  ,sparen'  (dt.  Einfluß?),  ahd.  spar  , sparsam,  knapp',  ags.  spcer, aisl.  sparr  ,sparsam,  karg'  (:  spor^) ;
hitt.  ispäi  ,ißt  sich  satt',  3.  PL  Upiianzi.
Von  spi'  (:  spei-)  aus :
mit  der  Bedeutung  ,fett,  dick'  und  ^-Formans :  ai.  sphij-  (Nom.  Sg.  sphik, Du.  sphijäu\  sphicäu  durch  Entgleisung  nach  d.  Nom.  Sg.?),  sphigl  , Arsch- backe, Hüfte';  aisl.  spik  n.,  ags.  spie  n.,  ahd.  spec,  -ckes  ,Speck' ]
Mit  Dentalformantien:  gr.  aftldvoq  , ausgedehnt,  weit,  eben',  otzi- ^dsLg,  OTtiövög  (Hes.)  ds.,  amdöd-sv  ,von  weitem',  sXsa-la'j^Lg,  -crtidog ,Sumpffläche',  äoTtidrig  {^av-üTtiörig  mit  Präp.  äv)  , geräumig',  äoTtlg,  -Idog ,Schild',  (,*dem  Körper  entlang  gebreitete  Fläche'  ?),  otzl^o)  '  „^xTfitVw" ;
984  •
lat.  spissvs  (*spid'to-)  , dicht,  dick,  langsam,  zögernd*;
mit  dh:  artL^ci^r}  , Spanne  (der  Hand)S  omd-lai'  oaviöeg  vedyg  Hes.*^-
mit  t:  lit.  speiHü,  spetsti  ,umringen',  spiesti  ^schwärmen',  spintü^  l^L .  ,in  Schwärmen  ausbrechen,  von  Bienen*^,  lett.  sjpiets  »Bienenschwarm*  fpw^  j tiz.  lit.  sputas  ^gedrängt*,  lat.  spissus) ;  vgl.  auch  lett.  spaile,  spailis  ,Stri*L  \ Schwaden  des  Mähers^  {-l-  vielleicht  aus  -dl-),  lit.  spielöti  ,in  den  J^  ^ rahmen  einspannen^  lett.  spailes  ^gespaltener  Stecken  zum  Einklemme spihj  spUis  ,eine  Zwicke,  Zwickeisen;  Holznägel;  Not,  Verlegenheit  (n>tj* Lw.?),  spilis  auch  ,zeltartig  ausgespannte  Leinwand'^  spilet  ,klemmeiK. zwicken,  spannen*.
Mit  ^--Formantien :
gr.  acplyyiü  ^schnüre  ein,  klemme  ein^,  aq)Lyy,Ti^Q  , Schnur,  Band;  Musk^J*.
lett.  spaiglis,  spaigle  , Krebsgabel';  germ.  mit  der  Bedeutung  ,ausspannti =  spreizen* :  nhd.  dial.  spaichen  ,ausschreiten^
=== leaf 225 ===
;  ausspaichen  ,mit  Schrittii oder  ausgespannten  Fingern  ausmessen',  norw.  speika  ,mit  steifen  fe». spannten)  Beinen  gehen',  splka  , widerspenstig  sein*.
WP.  II  656  ff.,  WH.  II  568  f.,  576,  Trautmann  274  f.,  Vendrjes  RQ. 50,  92,  Vasmer  2,  707,  710;  dazu  2.  spei-  und  1.  spen-.
spek-   ,spähen,   scharf   hinsehen';   spek-s,   spek-ön-,   spek-tor-  ,Spähef^ spek-to-  ,erspäht*,  spok-o-s  , Späher'.
Ai.  spdsati  (Dhätup.),  pd^yati  , sieht',  Partiz.  spastd-  (=  av.  spaHa-^  \gi spectus)^  spat  ,Späher*  (=  av.  spas,  lat.  au-,  haru-spex)^  spdsa-  ds.  (:  p.  . aM7i6g)y  av.  spasyeiti  ,späht^  (==  lat.  speciöy  gr.  ayisnro^aL),  spas  ,Spähei^  ^ spaSiar-  ds.  (=  lat.  -spector^  umb.  spetur-e),  spasan-  ,hinspähend  auf*  (=  ahd. speho  ,Späher*);  arm.  spasem  ,ich  erwarte'  ist  iran.  Lw. ;
gr.  aneTttoiiai  ,schaue'  {av.En-  umgestellt  aus  *sjpeÄ:-);  ayi.oitog  ,Späher| Ziel*,  G-aorteTv  »beobachten,  zielen,  untersuchen',  ayconrj,  G^ionid  ,Wart«\ axhpig  ,Betrachtung* ;  alb.  pashe  ,ich  sah'  (*[s]pok-s-  ?);
lat.  speciö,  -ere,  -xi,  -dum  ,sehen*  (con-spiciö  usw.),  spectö,  -äre  ,anschauen*, species  , Anblick,  Ansehen,  Aussehen,  Erscheinung*,  au-,  haru-spex]  specu$, -WS  , Höhle*,  speculum  , Spiegel',  speculor,  -ärl  ,spähen*;  umbr.  speture  jSpec- töri*,  speturie  ,spectöriae' ;
ahd.   spehön  ,spähen',    dazu  speha  f.   , aufmerksames  Betrachten,  Unte^ suchung.  Auskundschaftung,  Aufpassen*;  aisl.  spä  ,Wahrsagung*  {*spa1ai gr.  ayiOTtrj  ?  doch  weist  spä-  auf  Wurzelbetonung  und  ist  postverbalen  Ür Sprungs  verdächtig,  s.  Wissmann  Nom.  postv.  1,  41);  spä  , wahrsagen*  (*sp^  '^ hön,  s.  Wissmann  a.  a.  0.  1, 110),  spar  ,wahrsagend,  prophetisch*  {^spaha-iYf  - as.  ahd.  spähi  ,klug,  geschickt*.
WP.  II  659 f.,  WH.  II  570 f.;  vgl.  spe^-  , hinsehen*.
985
)pel'  J3,^t>  nachdrücklich  sprechen^;  (s)pel-no-  , Erzählung'. ^      ^rm.  afa-spel  jQsige,  Sprichwort,  Rätsel^;
got.  spül  n.  .Erzählung,  Sage,  FaheP,  aisl.  spjall  n.  , Erzählung,  Rede^, ^.  spell  n.  , Erzählung,  Rede,  Predigt^  (engl,  gospel  =  ags.  göd-speU)  ,Evan- t^elium';  ahd.  spei,  -les  n.  , Erzählung,  Rede,  Märchen',  ahd.  mhd.  bl-spel belehrende  Erzählung,  Fabel,  Gleichnis*,  nhd.  Beispiel]
davon  got.  spillön  ,verkündigen,  erzählen',  aisl.  spialla  ,reden,  erwäh- nend ags.  spellian  , reden,  erzählen'  (engl,  spell),.  ahd.  got-spellön  ,evan- (relizare^  mhd.  spellen  ,erzählen,  reden,  schwatzen^-
damit  sind  als  s-lose  Formen  vereinbar  gr.  ärteilrj  , Drohung ;  prahlerische Versprechung'  ((J/rfidfcu, drohe;  gelobe,  verheiße;  rühme  mich,  prahle^), falls  aus  "^äTvelvia,  worin  ä-  am  ehesten  die  Präp.  *r
=== leaf 226 ===
i  „h"]  (auch  germ.  -II- ^ohl  aus  -In-)  lett.  pett  ,schmähen,  lästern,  verleumden^,  paVas  (Plur.)  ,Ta- del,  Schmähung',  iz-paVu6t  ,tüchtig  ausschmähen^,  sowie  toch.  päl-,  päl- ,preisen'.
WP.  II  676  f.,  WH.  I  59,  Frisk  119  f.
l.  (s)p(-&)ei-  ,spalten,  abspalten,  absplittern,  abreißen';  sp(h)el-tä  , Brett'.
Ai.  sphatati  (Dhätup.)  , reißt,  springt  auf^,  sphatita-  ,gesprungen,  zerfetzt*, sphatikä-  ,Bergkristall'  (,sich  blättrig  abspaltend*),  *sphätdyati  ,spaltet*, belegt  das  Partiz.  sphatita- ;  sphutdti  , spaltet  sich,  springt  auf,  platzt,  reißt* (sek.  sphötati) ;  neben  diesen  ^-Präsentien  (:  ahd.  spaltan)  das  ^o-Partiz. sphuta-  ,aufgeblüht,  offen*  (:  got.  spilda)]  ai.  patati  , spaltet  sich,  birst*, pätayati  , spaltet,  bricht,  zerreißt*  (:  paiü-  ,scharf*.  gr.  ftXazvg  ,salzig*?  s.  u. *pltü-s) ;
phdlati  ,birst,  springt  entzwei*,  phdlakam  ,(*gespaltenes  Holz)  Brett,  Latte, Blatt,  Schild,  Holzbank*,  phäla-  m.  , Pflugschar'  (,zugespitztes  Aststück*?); apers.  Glosse  GTvaqa-ßaQai '  oi  ysQQoq)6QOi  Hes.  , schildtragend',  npers.  ispar, sipar  , Schild*  (ai.  jpharam,  spharam  , Schild*,  unbelegt,  wohl  aus  dem  Iran, und  im  Anlaut  nach  phdlakam  gerichtet);
gr.  acpaXdaasiv  xifiveiv,  yievtetv  Hes.,  acpdXa^  , Stechdorn*,  äonaXad^og m.  ds.  (,*woran  man  sich  reißt,  ritzt*),  ocpdXa^,  dacpäla^,  anaXa^,  doTtäXa^ ,Maulwurf*  (,die  Erde  aufreißend*),  GTcaXiGGSTai'  GTragaGGezai,  ragaGGSTai Hes.,  ^GTtaXov'  GzvTog  Hes.,  GJtdXavd-QOv  ,Schüreisen*;  GnöXia'  xa  itaqa- TdXöj^eva  igidia  drcb  rCov  gy^Xcjv  xibv  TtQoßaTwv  Hes.  (:  lat.  spolium),  att. OfcoXdg  , abgezogenes  Fell*  und  ,Überwurf  von  Leder,  Brustharnisch,  Mantel*, äol.  GTcaXlg,  att.  ipaXig  ,Schere*;  zu  Gq^aX&GGsiv  auch  GcpaXög  ,Fußblock  für Gefangene;  Wurfscheibe*  und  GcpdXXw  ,werfen  (ursprüngl.  mit  ,Prügeln*), schleudern,  stoßen'  und  , (zunächst  beim  Ringen)  ein  Bein  stellen,  im  Kampf behindern*,  woraus  ,zu  Fall  bringen,  schädigen,  täuschen,  betrügen'.  Med. ,wanken,  fallen,  sich  irren*,  dGcpaXrjg  »unerschütterlich,  ohne  sich  fortstoßen
986
zu  lassen'  —  ,T\ihig,  sicherS  a(paX€gög  ^schlüpfrig,  aq)(xXfxa  »falscher  Schritt»* Gcpüag  »Holzscheit,  Knüppel;  ausgehöhlter  Block,  Bank';  J  ■
aus  dem  Alb.  vielleicht  pale  ,Seite,  Partei'  {*polnä,  vgl.  aksl.  po?^  ,Seit» Ufer,  Geschlecht,  Hälfte') ;  popele  ,Felsstück,  Scholle^  plis  (*pZi-«iV)  ^^ schölle*,  plish  ,Schilfrohr'  (*pU-s{o-):

=== leaf 227 ===
lat.  spolium  »abgezogene  oder  abgelegte  Tierhaut;  dem  Feinde  aW nommene  Rüstung,  Beute';
mit  ^Erweit. ;  ahd.  spaltan,  mnd.  spalden  ,spalten%  got.  spilda  {*8ptUi) ,Schreibtafel',  aisL  spjald  (*speltos)  ,Brett',  ags.  speld  ,Splint;  Holzsttlck* mhd.  spelte  ^abgespaltenes  Holzstück,  Handgerät  der  Weberei';  aisl.  spj^ spell  »Schaden'  {*spelpa-,  -i-),  ags.  spM,  spild  ,Vernichtung,  Ruin',  wotqö aisl.  spilla,  spella  ,verderben,  töten'  (*spelpjan^  *spelpön),  as.  spüdian,  j^ spildan  , vernichten',  ahd.  spildan,  spilden  , vergeuden,  verschwenden*,  ai^ spildi , freigebig';  germ.  t  in  mnd.  spelte  »gespaltenes  Stück*,  ostfries.  «poldr ds.,  germ.  *speltö  (daraus  lat.  spelta)  in  ahd.  spelza  vlat.  spelta  (woramt^ , Spelt';  engl,  spelter  ,Zink'  (*spaldiz-) -,  ags.  spaldur  ,Balsam'  (*spaldut^ , Ausfluß  aus  gespaltenen  Pflanzen') ;  n-Präs.  ags.  spillan  mhd.  spülen  ,spÄl. ten'  {*spelljan)j  wozu  ohne  s-  schwed,  fjäll  ,Schinnen  im  Haar'; spqlr  ,dünne  flache  Stange',  mengl.  spale  ds.,  mhd.  spale  , Leiterspros wahrscheinlich  (als  ,dünnes,  flaches  Holzstück')  ahd.  spuolo  m.,  isl. , Weberschiffchen',  norw.  spöle  , Spule'  (germ.  '^spölan-)-^  ahd.  spuola  (gen *spölön-)  ySpule^j  ,Röhre,  Federkiel';  ohne  anl.  s-i  aisl.  fjql  ,Brett'  (*|?e24)S
mit  <-Erweit.,  aber  ohne  s-  wohl  ir.  alta{i)n,  cymr.  ellyn,  acymr.  eli^ , Schermesser',  abret.  altin  gl.  ,ferula',  mbret.  autenn,  nbret.  aotenn  ,Sch( messer*  {^paltina)]  mcymr.  allaw  ,rasieren'  (^altä-mu-)]  J.  Loth  RC.  45,  171
lit.  spälisj  PI.  späliai,  lett.  spaVi  ,Flachsschäben';  lett.  spals  »Griff,  Hand- habe' ;  apr.  spelanxtis  , Splitter* ;
aksl.  ras-platiti  ,spalten'  {*poltiti,  vgl.  nhd.  spalten,  ai.  sphatafi),  plai%] „QocKog"  ,Fetzen',  poUno  ,Scheit  Holz',  polica  , Brett',  palica,  aruss.  paVAa, ,Stock',  russ.  ras-polöth  »entzweischneiden',  pöloth,  polth  »(abgeschnittene)! Speckseite',  poltina  , Hälfte',  aksl.  poh,  Gen.  -u  ,Hälfte,  Seite,  Ufer,  Q( schlecht';  abg.  plevq,  pUti  (russ.  polöt^)  ,jä.ten\  pUv eh  »Unkraut*;  *o-peli^ in  ßech.  oplen,  oplin  ,Gipf stock,  Rungenstock',  sloven.  opV^n  ,Wagengipfefr holz'  usw.;
mit  dem  v  von  pUoq  (*pelu5)  ist  zusammenzuhalten:  lett.  spalva  »Feder,'' Gefieder,    Haar',    spüva    , Hülse,    Samenwolle,   Wollgras',    spilv^ns   ,Bett- kissen'  usw. ;
toch.  A  spälik-j  B  spalk-  ,sich  anstrengen';
mit  {s)p{h)el-  ,spalten'  hängen  möglicherweise  zusammen:  pel-  ,Haut|l Fell',   spelg-  ,spalten',    splei-   ,spalten*,  pl
```


## [2026-09-14T00:53:30.952Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 229 230 231; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='$((n+1))'' POK_03.txt; done | grep -n -i -A8 -B3 \"sten\\|Brustwarze\\|fstana\\|\\bpst\" | head -80"
}
```


### [2026-09-14T00:53:31.952Z] TOOL RESULT

```
18-(*(5
19-=== leaf 230 ===
20-)pei2-),  (s)pon-,  {s)pondho-  ,Holzeimer^,  auch  gelegentlich  von  an- deren Holzgeräten;  verwandt  mit  s'phe-,  sjpJid-  ^langes,  flaches  Holz- stück' (vgl.  dessen  -no-Ableitung  nhd.  Span).
21:Arm.  pund  , Gefäß'  (*phondho-) j  lat.  sponda  ^Bettstelle*;  mir.  sonn  m. Pfosten,  Pfeiler^,  sonnaid  , stößt,  drückt',  cymr.  ffon  f.  , Stock'  (*spondha) ; aisl.  spann  n.  , Eimer'  (dän.  spand  ,Eimer'),  mnd.  span,  -nnes  ,Holzeimer', fat-sfan  ^hölzernes  Henkelgefäß*  (germ.  *8panna-,  vielleicht  o-Ableit.  eines ^-St.  *spanan-j  oder  aus  *spondh-no-  oder  ^spoTj-wo-) ;  aksl.  sp^c^T»  ,modius';
22-e-Formen  fehlen;  ndl.  spiwcZe  , Speisekammer',  nhd.  Spind  , Schrank' stammen  aus  mlat.  *(dis)penda  (Frings,  Germania  Romana  146).
23-WF.  II  662,  WH.  II  578.
24-spetid-  ,ein  Trankopfer  darbringen;  geloben'.
25-Gr.  OTtevdo)  ,verspreche  (Gortyn);  bringe  ein  Trankopfer  dar,  spende', Med.  , schließe  einen  Vertrag' ;  anovörj  , Spende,  Trankopfer;  PL  Verträge';
26-lat.  spondeöj  -ere  (Kaus.-Iter.)  , feierlich  versprechen,  sich  verbürgen'; sponsa  ,die  Verlobte';  respondere  ,eine  Gegenleistung  versprechen;  ant- worten' ;  despondere  animum  ,den  Mut  sinken  lassen' ;  hitt.  Hpand-  ,spenden, opfern'.
27-WP.  II  662,  665,  WH.  II  578  f.,  Pedersen  Hitt.  166.
28-sp{h)e{n)d'  ,zucken,  zappeln'  und  (über  ,flackern')  , glänzen'.
29-Ai.  Spandau  ,zuckt,  schlägt  aus*,  spanda-  m.  , Zucken,  Bewegung',  snäyu- spanda-  , Pulsschlag',  spandana-  m.  , zuckend';  gr.  aq)evdöv7]  , Schleuder', aq)aöd^ü)  ,zucke,  zapple,  bewege  mich  heftig'  (*Gq)nö-) ;  Gg)6vövlog,  oitov- ^vloQ,  m.  jWirbel  an  der  Spindel,  usw.';  unnasaliert  aq)edavögy  ocpodqdg jheftig,  eifrig';  älter  ndl.  spat  , Krampf,  nhd.  SpatQi),  mhd.  spat,  ostfries. spat{t),  spad{de)  , Geschwulst  am  Pferdefuß'  (germ.  d,  dd  neben  t^  tt  kann junge  Variation  sein),  nd.  ndl.  spatten  ,zucken,  zappeln*;
--
41-da  *spend-  »glänzen'  eine  Zerlegung  in  *sp(h)en-g-,  -d-  zur  Erwägt^j» stellt,  kann  speng-  nicht  zuversichtlich  als  Nasalform  eines :
42-{s)peg-  gelten,  das  erschlossen  wird  aus  nhd.  Spule  aus  mnd.  spök  ,SpuV Gespenst'  (germ.  *spö'k-)'^  ob  dazu  auch  die  Gruppe  von  mnd.  spakttt^ ,sprühen'  (usw.)?.
43-WP.  11663  f.  r
44:spenO'y  st^no-,  p{Q)st^nO'  ,Zitze,  Brustwarze,  Brust*.
45:1.  Anlaut  sp:  air.  sine  m.  , Zitze':  hö  tri-phne  =  hö  tri  sine  ,Kuh  mit drei  Zitzen',  mir.  sine  Seäin  ,uvula*;  aisl.  speni  m.  , Zitze,  Brustwarze* (aschwed.  spini  auch  , Zäpfchen  im  Halse'),  mnd.  spene  ds. ;  o-stufig  a«. Spane,  spanu  f.  ,Brustwarze*,  spanan  , entwöhnen';  mhd.  spen  f.  ,Bruat| Muttermilch*  (wohl  *spani'^  vgl.  nhd.  Span-ferJcel) ;  reduktionsstufig  mnd. spone  f.,  ahd.  spunni,  mhd.  spünne  und  spune  ,Brustwarze' ;  lit.  spen^t , Zitze,  Zäpfchen  im  Halse,  Ohrläppchen',  apr.  spenis  , Zitze*.
46:2.  mpers.  np.  pistän  ,weibliche  Brust*  (*p9stäna-),  av.  fStäna-  m.  Da. ,ds.,  Brustwarze,  Knoten'  (*pstäna),  drddvafsnyä  ,der  hochbusigen',  ai.  stäna»^ , Brust,  bes.  weibliche';  arm.  stin  »weibliche  Brust'  {*stenO']  Gen.  Sg.  stean)] gr.  avr^vlov'  arfj'^og  Hes.  (daß  avfj'd^og  verwandt  sei,  ist  schwer  glaublich; hat  neben  ^viov,  n^rjvrj  einst  ein  *d-r]-d^og,  Hrj-d-og  bestanden,  das  neben aTiqvlov  eine  Parallelbildung  az^d^og  ins  Leben  treten  ließ??).
47-Die  Vereinigung  der  Anlaute  unter  p(d)st'in-  scheint  möglich. WP.  II  663,  Trautmann  275,  Specht,  Idg.  Dekl.  86.
48-1.  (s)per'  , Sparren ;  Stange,  Speer' ;  verbal  ,mit  Sparren  verspreizen,  stützen,' stemmen,  sich  sperren*,  ursprüngl.  denominativ. Lat.  sparus,  sparum  ,kurzer  Speer  des  Landvolkes  als  Jagd-  und  dürf- tige Kriegswaffe'  (*spero-);  dazu  der  Fischname  sparus,  gr.  a^tagog;  alb» shparr,  shperdhe  ,Eiche*  (als  ,Bauholz*;  rr  aus  rn);  germ.  "^speru-  in  aisL spjgr  , Speer*,  ags.  spere  n.,  afries.  spiri,  spere,  sper,  as.   ahd.  sper,  mhd.
49-I
50-991
51-toer  ßi-  ^-j  ^^^-  ^P^^^  ^f  ahd.  spereboum  , aesculus';  aisl.  spari,  sparri  m. ;  Spei^®^^  Sparren,  Balken^,  sperra  f.  (j^sparriön)  ^Dachbalken^  ahd.  sparro kalken,  Dachbalken,  Stange',  nhd.  Sparren-^  davon  aisl.  sperra  ,mit  Sparren yersehen;  die  Beine  spreizen,  aussperren,  verhindern';  aisl.  sperra,  ags. le-  9^'  sparrian  ,ver
```


## [2026-09-14T00:53:52.996Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD pahlug ===\"; grep -n -i \"pahlūg\\|pahlug\\|phlwk\" PHD.txt PHD_pages.txt PHD_mackenzie.txt 2>/dev/null | head -20; echo \"=== PHD pasnag ===\"; grep -n -i \"pāšnag\\|pasnag\\|pāšn\\|pasn\" PHD.txt | head -20; echo \"=== PHD pestan ===\"; grep -n -i \"pestān\\|pistān\\|pystʾn\\|pestan\" PHD.txt | head -20"
}
```


### [2026-09-14T00:53:53.070Z] TOOL RESULT

```
=== PHD pahlug ===
PHD_mackenzie.txt:7444:reply paywaz-.                           rib pahlug.
PHD_mackenzie.txt:8862:puzand                        "QYCl>         pahlUg
PHD.txt:3439:rib pahlūg.
PHD_pages.txt:7444:reply paywaz-.                           rib pahlug.
PHD_pages.txt:8862:puzand                        "QYCl>         pahlUg
=== PHD pasnag ===
545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
4746:pāyag pānāgīh pānāg -bān pänagīh panag pānzdah pākīzag pāk pālāy- pālūdan pālūdag 1-2pärag pārsīg pāsox pāsbānīh pāsbān pazen pāzand pazen pāšnag pāšom
=== PHD pestan ===
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
1080:breast pestān; sēn(ag), war.
4720:pērēzgarīh pīlbān pēm, pīm pēmēn- pēmēnīdan pimgen pës- pésidan pēsišn pestan pēč- pēčīdan pēš pēšānīg pēšūbāy pēšūbāyīh
```


## [2026-09-14T00:53:55.858Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n -i \"pahlūg\\|pahlug\\|pāšnak\\|pasnak\\|pistān\\|pestān\" NYB_vol2_glossary.txt | head -20; echo \"=== BRT parasu ===\"; grep -n -i \"par\\.su\\|parəsu\\|pərəsu\\|paresu\" BRT.txt | head -10; echo \"=== BRT pasna ===\"; grep -n -i \"pāšna\\|pashna\\|päsna\" BRT.txt | head -10; echo \"=== BRT fstana ===\"; grep -n -i \"fštāna\\|fstana\\|fätäna\" BRT.txt | head -10"
}
```


### [2026-09-14T00:53:55.959Z] TOOL RESULT

```
=== NYB ===
2347:kurušk [kwlwšk'] ewe, of a big species of sheep 509-11, — Zsprm X, 20 in telling this story: meš kurušk i šīr-pistān "with milk in her udder’. Also kwryšk' = Paz. kurišk, koriák, BdA, p. 959-1? = BdJ2918— 303: meš 5 sratak: han i pat-dumb, han 4 a-dumb, u sak meš, u meš *takilé [tkly ; Paz. tagr, tgar] <u> kurišk tmeš, ke srub vazurg, asp homänäk, 3 köf [BdA corrected from tan, BdJ Paz. koh] dārēt api-š 6 bārak girénd, cigēn gobet ku Mānušcihr + amāh niyak kurišk-ē pat bārak dāšt [sak
=== BRT parasu ===
=== BRT pasna ===
10462:mit  «r'aufstemmen' :  kakat  n  ig>  r?pta  ii  - bya  päsnaiibya  urg>r3ptalibya{%^^  angus- talibya  V.S.ji;  70,
10532:airihä  zimS  (sd.)  päsnalibya  vTspara aslaäbya   vixala  (aS.)  V,  2.  31;  32    (wo
27932:•  j.  zairi-päSna-  Adj.  'mit  gelber,  gold- farbener Ferse  (?):  gattdarswan  (sd.)  yim 'n>m  YL5.  38,  75.41-
=== BRT fstana ===
```


## [2026-09-14T00:54:04.113Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT Rippe ===\"; grep -n -i \"Rippe\" BRT.txt | head -20; echo \"=== BRT Ferse ===\"; grep -n -i \"Ferse\" BRT.txt | head -20; echo \"=== BRT Brustwarze/Brust ===\"; grep -n \"fstana\\|fätäna\\|fstäna\\|f§tana\\|fitäna\" BRT.txt | head"
}
```


### [2026-09-14T00:54:04.207Z] TOOL RESULT

```
=== BRT Rippe ===
15812:•  j.  parasav-  f.  'Rippe':  *°jz'/ (ND.)"  "die beiderseitigen  Rippen"  F.^  g.
15841:Vgl.  'Par'sla:  —  ai.  ppfßy-  t,  'Rippe'?  — Pü.:  pult.  —  ')  Weil  aus  zwei  Haften  rechts und  links  des  Rückgrats  bestehend.
16145:•  3.  'pvF'asav-  m.  i)  'Rippe'  (nur Komp.).  2)  'Rippengegend,  Bnistscite': JaHitim  {/ii'yum)  hl  •säum  V.  &  54— 56', V.^.  17,  30^.
16148:■  j.  p»rasu.masab-  i)Adj. 'von  der  Grösse einer  Rippe';  oitwt . .  fnsuMavatth^m  vä vuvA»»  (ASm.  statt n.)  Z'd  V.ß.iö.  2)0. 'Rippengrösse'  (nur  Komp.).
17280:•  j.  bi-pt>rasu.masah-  Adj.  'doppelt  so gross  als  eine  Rippe':  asUm  balirizu.- stavankftn  vil  -sar»h}m  (ASm.  statt  n.)  vä V.  6. 1 8.
=== BRT Ferse ===
16060:•  j.pääna-n. 'Ferse':  u^f7n>^/(iA'4}'<i  'na^bya V.  Ä  70,  71;  —  aiiiAä  t?m5  'näöya  vUfara V.2.31.
27706:ki  avar»tam  nipsrayanta  (Sp.  851  u.)  V. ij?.  2  6 ;  —  yS  s»  m  S  tisrS  karsä  frakära- yeiti  N.  loi.  4)  'Erde'  als  Stoffj  'Lehm' ; är//  /rastt3tay?n  malsmana  glui  %ris simd  hankanaym  (sd.)  V.  7. 14:9.  30;  — hahnl  frasnälaym  malsmana  gSus  ka- k^rit  eimS  usda^ay3n  V.  7,  74;  —  aSai- satttca  a»mS  piri^u.fraväU  fraitavata  V. 5.  29;  —  Ivaniim  dräjö  zrvämm  sairi  .. sfmff(GS.  dapain/i,Sp.^39To.)  V.  7.45;  — aiä/tä  5imS  (als  Obj.)  painäbya  vTspara sastasibya  vTxaia  .  .  ya%a  na  masyäka *xij'isH  z^ml"^  vJfJrayänie  "stampf  Erde mit  den  Fersen,  quetsch  (Erde)  mit  den Händen  auseinander,  wie  heutzutag  die Leute  aufgeweichten  Lehm  auseinander- kneten" V.  2.3i5>.  A)  als  Gottheit  (>■«- zata-)**'>:  asmaniin  .  .  sqm  hmaahtm yasaiiiaiäe  Y.16.6;  S.2.28;  —  iqmcä asmammcä  yazamaidgY.42.  3; —  s.noch Y.  /.  16    und    A  a.  A  a)  ztmB  (näml.
27932:•  j.  zairi-päSna-  Adj.  'mit  gelber,  gold- farbener Ferse  (?):  gattdarswan  (sd.)  yim 'n>m  YL5.  38,  75.41-
=== BRT Brustwarze/Brust ===
11056:spmts  mainyui  yasca  a^rö  Y.  57.  17;  — dva  yaska  .  ,  yasca  suis  yasca  tarsnS  V. 7.70;  —  äva  aurvanta  .  .  yimca  bipaiti- stätum  aurvanUm  yimca  cahwarypaiiiit3- mm  Ytj.  131; — yaiaca  hukmpta  fstäna yaha'a  atalan  niväzäna  Yt  5. 1 2 7 ;  — ya'iraca  mazistA  Jrfr»tä  ya^raca  atbislö as'ava  Yt.  13.  25;  —  ähnlich,  aber  mit  ab- weichender Stellung  des  ca :  yaihä  pourüica hr^ijayqn  naiäica  aiäha  (Sp.  80.)  yasaiü «jfJnJi  (sd.)  .,  Y.  65.  II.  fi)  'ii  Ver- bindung mit  ä  (s.  Sp.  300  m.):  yaHbyascä  töi 3  ya^ä  aiibyS  ä  a»h}n  Y.3p.  i.  An- hang zu  I.  Beim  ersten  Glied  steht  ci^ statt  lä:  tJctJ  maxdä  vasimJ  anyäcil  vXäuyl Y.44.  3.  3)  die  Glieder  sind  verbal; a)  sie  folgen  sich  unmittelbar:  yavat  . . tavalü  isäiia  Y.JO.  11;  —  ySi  iahara'a hmicä  Y.  5/.  aa;  — ydä^a  Tm  mSiiäica raoca^ä  Y.  45. 3;  —  hanalmacS  zaimscn y.41.^; —  daitihul  nihatai'^a  haosätai'a Yt  13.  66 ;  — ya'isa  m . .  *bairyetica  *x'air' yetica  V.  5.  40 ;  —  asBis  .  .  yä  ns  äraicä frtnavataicä  Y.  56^.  3;  —  yat  haonumca ahunavat  aNhavatwmca  *vTma$täi  (sd.)  N, 72;  —  yat  haomimca  äsnayät  haonDmSa pairi.kamat  N.  75.  a)  mit  unregel- mässiger Stellung  des  ersten  la:  yat  hao- miMca   gava  *rag^JoayäJ  baxsayäa/äi  N.
```


## [2026-09-14T00:54:15.168Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"fstäna\\|fitäna\\|f§täna\\|fätäna\\|fstäna-\\|fstana-\" BRT.txt | head; echo \"--- search context 'Brustwarze' ---\"; grep -n \"Brustwarze\\|Busen\\|hochbusig\" BRT.txt | head"
}
```


### [2026-09-14T00:54:15.228Z] TOOL RESULT

```
11056:spmts  mainyui  yasca  a^rö  Y.  57.  17;  — dva  yaska  .  ,  yasca  suis  yasca  tarsnS  V. 7.70;  —  äva  aurvanta  .  .  yimca  bipaiti- stätum  aurvanUm  yimca  cahwarypaiiiit3- mm  Ytj.  131; — yaiaca  hukmpta  fstäna yaha'a  atalan  niväzäna  Yt  5. 1 2 7 ;  — ya'iraca  mazistA  Jrfr»tä  ya^raca  atbislö as'ava  Yt.  13.  25;  —  ähnlich,  aber  mit  ab- weichender Stellung  des  ca :  yaihä  pourüica hr^ijayqn  naiäica  aiäha  (Sp.  80.)  yasaiü «jfJnJi  (sd.)  .,  Y.  65.  II.  fi)  'ii  Ver- bindung mit  ä  (s.  Sp.  300  m.):  yaHbyascä  töi 3  ya^ä  aiibyS  ä  a»h}n  Y.3p.  i.  An- hang zu  I.  Beim  ersten  Glied  steht  ci^ statt  lä:  tJctJ  maxdä  vasimJ  anyäcil  vXäuyl Y.44.  3.  3)  die  Glieder  sind  verbal; a)  sie  folgen  sich  unmittelbar:  yavat  . . tavalü  isäiia  Y.JO.  11;  —  ySi  iahara'a hmicä  Y.  5/.  aa;  — ydä^a  Tm  mSiiäica raoca^ä  Y.  45. 3;  —  hanalmacS  zaimscn y.41.^; —  daitihul  nihatai'^a  haosätai'a Yt  13.  66 ;  — ya'isa  m . .  *bairyetica  *x'air' yetica  V.  5.  40 ;  —  asBis  .  .  yä  ns  äraicä frtnavataicä  Y.  56^.  3;  —  yat  haonumca ahunavat  aNhavatwmca  *vTma$täi  (sd.)  N, 72;  —  yat  haomimca  äsnayät  haonDmSa pairi.kamat  N.  75.  a)  mit  unregel- mässiger Stellung  des  ersten  la:  yat  hao- miMca   gava  *rag^JoayäJ  baxsayäa/äi  N.
--- search context 'Brustwarze' ---
18421:•  j.  ßt^a-  m.  i)  'weibliche  Brusf,  Du.:  Aä hl  mailim  nyazata  (sd.)  ya%aea  huk^r^ta 'naya^aca  anhin  niväzäna {sd.)Yl.S-i^7i F-JS'  2)  'Wölbung  der  Brust',  um  die Brustwarze  herum  riÄtft'wOT(bz.Äö>«OT)  'n^m V.Ä53— 54*,  p.  19*.  3)'Buckel,Knoten' (nur  Komp.).
```


## [2026-09-14T00:54:16.406Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15805,15845p' BRT.txt; echo \"=====16050,16070=====\"; sed -n '16050,16070p' BRT.txt; echo \"=====16140,16155=====\"; sed -n '16140,16155p' BRT.txt"
}
```


### [2026-09-14T00:54:16.490Z] TOOL RESULT

```
(AbL)'':  avä  dätnqn ..yä  hinti  °ta  paotryS.- fra%war^ta  a^näat^'a  apäatca  ..  Vr.  7.4.
PQ.:  fretum  dät.    —    i)  Der  Abi.  hängt  vom I.  Glied  des  Komp.  ab.
•  j.  paoiryö.t^aeSa-  m-,  Plur,  'die  ersten Lehrer  des  Glaubens'*':  asaunqm  fra- vasinqm  .  .  *fanqm  /ravaltnam  "den  Fr. der  Gläubigen  .  .,  den  Fr.  der  ersten Lehrer"  Y.r.  18.
*1  Vgl,  Y.  23.  a,  Yt  13.  17.  DsT.s  Bemer- kangen  ZA.  J.  xxix  sind  unzutrefTend,  wenn ich  schon  nicht  leugnen  will,  dass  man  später die  Stelle  so  gefasst  hat.  Der  Gegensatz  von afiara-  ist  paurva-,  nicht  paoirya-.  S-  ''tkaela- No.  2.
•  j.  paolryö.fra'd'warsta-  Adj.  i)  'als erster,  zuerst  geschaifen,  gebildet*:  asma- tt3m  .  .  paoirys.dät?m  (sd.)  't^nt  ^galt^Tm gtif^yayä  stsü  Vr.  7.  4.  z)  'vorherig gebildet,  eher  gebildet  als  — '  (Abl.)'>: ava  damqn  .  .  ya  hmti  paoiryS.d-3ta  'ia asnäatca  afüatca  ,  .  Vr.  7.  4.
Vä.i/raium  fräc  äfrlt.  —  ')  Der  Abi.  hängt vom  I.  Glied  des  Komp.  ab.
j.  paraanyeili  Yt.  *.  151  liea^Ww!*;  s./raj-.
•  j.  parasav-  f.  'Rippe':  *°jz'/ (ND.)"  "die beiderseitigen  Rippen"  F.^  g.
ai.  J>ariav-  f. »),  —  Vgl.  firisav-.  —  Pü. :  fahWi.
—  >)  Bestimmung  unsicher,  vgl.  ai.  und  ATin. S.  noch  Dbr.  VglS.  /.  143.  —  >)  Woiu  BB. 2j-  295.
•  j.  *parsa-''  m.  'Getreideähre,  Ähre': mqnay^n  ahe  yaä^a  nä  sai?mca  hazar?r»mca ,  .  'l'anqm'^  *nijat3irt  hyat  ".  .  als  ob  ein Mann  auf  hundert  und  tausend  . .  Ähren einschlüge"  Yt. /j.  71''.
ai.  par;ä-  m.  —   ')  So  F  1  i  NA.  fairislanqm.
—  >)  Das  Bild  RV.  10.  4S.  7  ist  ganz  ähnlich.
•  j.  paräatgav-'' m.  EN.  zweier  Gläubiger:
i)  'gfus  paratahe  asaottj  "des  /*.,  Sohns des  Par.  . ."  Yl  13.  96.  _  z)  -gava  (GD.) dazgrsgava  (sd.)  alaona  Yt  JJ.  127.
Eig.  'bunte,  gefleckte  ('/arsant-  Adj.,  woiu IF.  5.  261)  Rinder  habend';  ai.  pfiani-  Adj., vg\.  Pl-IOilah'a-  Adj.;  Bthl.  KZ.  29.  563.  — yg\.  parlav-.  —  ')  Zu  Yt  13.  127  hat  F  l fariaig';  S  263-  50.
•  j.  paräav-  Adj.  'ungleichfarbig,  ge- sprenkelt': 'hia  F.  5,
KompA.  —  Unsicher.  —  VgL  parlal.'  und  zu farhiatäta:  —  Pü. :  p  p  d  da  p  k.
•  j.  paräinta-  m.  EN.  eines  Gläubigen: °la?u  gandr/wahe  aiaonS  Vt  13. 1 23.
Eig.  Bed.?
•  j.  parSuya-  Adj.  (fem.  'ys-)  'nivalis, Schnee-',  Bezeichnung  bestimmter  Wasser; vispisca  aps  ya  ztmä  .  .  'ya  (NPf.)  *väir- yäsca  Y.  6S.  6.
Bed.  und  El.?»).  —  Pu.:  k  t  dd  Uj  l.  lu  nä- vaya-.  —  >)  Die  bei  Wn.  AiGr.  /.  $6  erwähnte Zusammenstellung  ist  ganz  unsicher.
•  j.  "parSta  aisnam  y.ii.iz;  iaf.'^'>.
Pii. :  falkärem,  erl. ;  putlenim.  —  *)  Gramma- tisch wertlose  späte  Stelle.  Der  Verf.  wollte  mit p°  augenscheinlich  das  selbe  sagen,  was  V. //.  9  durch  p!Tfne,  V.  to.  1  durch  pinnäta ausgedrückt  ist;  s.  par>l-  (wozu  farlla  nicht gezogen  werden  kann).
•  g.  parStä  Inf.  'Jemanden  (Akk.)  wonach (Akk.)  zu  fragen',  mit  'ah-  im  Sinn  des PFP.  (Sp.  277  m.):  pjrfsaca  nA  ya  tSi 7kmä  parstä  "et  inteiroga  nos  quae  tibi sumus  interrogandi"  Y.^^.  10.
Zum  V.froi-.  —  Vgl,  ^paritay.  —  Vi.:  pur- ilca  kac  arnSi  pa  an  puräsn  i  dfn.
•  j.,  g.  -paräU-  Adj.,  PPfP.:  s./ras-. KompA.,  E.
•  j.  'paräta-  m.  1)  'Rücken,  Rückgrat':
frä  *°t)m^'>  nämayänii  vT  maStyqmm  fsäna- yänti{sä.)  Yt.  74.56.  2) 'Rückhalt': /.r
(Tä.m\.  frava^ayö)  hl . .  °tasca  patriväras^a vismte  pairi  ..  drujat  '^t  13.  T 1 ;  /.  19.
Vgl.  'parSfay-.  —  ai.  pfsfhä-  n.,  np.  piät-, weitre  unsichere  Anknüpfungen   IF.  //.  285.
—  Pü.  (in  Yt.  /):  Hai pas  u  pii  Si  i  man  näm hac  piiit  palirai  barih,  Npü-fzuVl.  7^);  pSsux.
—  0  So  alle  guten  Hds.;  NA.  'ilm.
•  j.  "parStay-  f.  '(gegenseitige)  Befragung, Disputation':  yS  .  .  gaot)ma?ie  (sd.)  parSyä HSit  avaiti  \t13.16.  LS.  'ta  als  Int sbes.
KompE.  —  Zum  V./ras-.  —  S.  lüm.parsISii Inf,  a-nä  firailay:  —  afy.  \^.  puilrdql 'ita%fa' (wozu  IF.  9.  264>
•  j,  'parätay-  f..  Du."  'Rücken':  'ti (AD.)  he  .  .  assa  drux^  .  .  upaJvqsaiti S.S.  51;  52,  g.  18,  19.         [Yt.14.  56:  lies
Vgl.  'Par'sla:  —  ai.  ppfßy-  t,  'Rippe'?  — Pü.:  pult.  —  ')  Weil  aus  zwei  Haften  rechts und  links  des  Rückgrats  bestehend.
•  j.  parStS.va£ah-  Adj.  'der  die  (heiligen) Sprüche  erfragt,  durch  Fragen  erkundet hat':  ä^ravanö  'canhs paitiparstö.sravatfh8 Yt.5.91.
•  j.paräv-anika-  Adj.  'mit  ungleichfarbiger, gesprenkelter  Stirn-,  Vorderseite',  vom  Wild- schwein'*:  Au  kthrpa   varszahe  .  .  'iahe
IL  14- 15-
')    Vgl,    Br£HU   Tietleben:  'Am   Vorderteil
=====16050,16070=====
Unrichtige  Et,  GlrPh.  a.  409.  —  Ob  im  RV.
genannt?    Vgl,  zu  fflhiipärsavafy  RV.  7.83.1
ZiMMEK   AL,  134,   EMever  GeschdAltert.  /.
5iSi  aber  die  Farsua  s.  ebd.  413,  ZDMG.JV-
126,  KZ.  37.  535.
'].  faHiia  fär?smanäi  N.  S4:  lies  ..pintm'.
•  j.  pizah'vant-  Adj.  —  ?— :  *'sattukantan ! F.  So'.
VU.  10  ai.  päjas-  n.  —  Pii. ;  miid  ariämtiAä  ^ ■in  lobnwBrdig«r  Weise'.
•  j.  päzinah-  m.  EN.  eines  Gläubigen: 'natfhö  asaenS  Yt.  Jj.  1 1 7.
Eig.  Bed.?  Ob  pä-änah-  (lum  V.  »fä-)  eig. 'frei  Ton  Schädigung'?
•  j.pääna-n. 'Ferse':  u^f7n>^/(iA'4}'<i  'na^bya V.  Ä  70,  71;  —  aiiiAä  t?m5  'näöya  vUfara V.2.31.
KompE.  —  ai.  Tgl.  färfriay  f. ;  np.  fäina. Vgl.  Hbm.  IFAni.  ö.  35.  —  Pü. :  päi'tak,
•  g.  pih-  'sehen'.     Praes.  27  pisya-. 'sehen',  mit  Akt:  3r?z?jl}{^.)  ..fourusü
hvars  pisyasü  ". .  unter  den  vielen,  die das  Sonnenlicht  sehen"  y.50.  a.  a)  das Obj.  wird  durch  einen  Reladvsatz  gegeben: yöi  pisyeiniV'>  ,.yais  gqm  kara-ps  uslxscä (sd.)  aiiitnsi  data  "die  sehen,  wie  .  ." Y.  44.  io.
Vgl.  apiiman'  und  Gdn.  KZ.  ^  520.  —  Ich nehme  fäh-  (af.  päi-)  als  'Erweiterung'  aus f^y\\  vgl.  iBed,  nhd,  iBohrett  und  gr.  epö». Doch  kdnntc  pii-  auch  au(  idg,  'pxi-  (tu  ai. pafyali)  gehen.  —  Pii.  (dRn.):  pänakih,  päyend. —  ")  rSchr.  piji'  in  J  2  usw.  s.  S  36/i.  9. j.  pidiKÜpi:  s.  dvaipa-,
•  j.  "/W(/  sfqm  p^ragsraptayät"  Nik.j, /^w  nohl  statt  pairi.
•  j.  ■•■parat-"  f.  "Kampf,  Streit*:  OxStlm ham.vmniim  'tasüa  mrvayasca  Aamaistara Yti/,is.
Zum  V.  paTit:  —  aL  ///■  f.,  mp.  purl-inllan; np.  vgL  na-burd.  —  S.  noch  pjianä-,  —  Pu, : undeutlich,  fifä.:  jang.  —  >)  So  J  lo;  NA. fatif.     Zahlreiche  Var.
•  j.  paratamna-  Adj.,  PPM:  %.pant-. KompE.
•j.,g.p»r9tav-ra.,f.'*i) 'Durchgang,  Gang*: "tui  F.  JO;  —  frabm?m  daiähsus  nava '%ioS  (AP.)  k»r?nai'a  "in  der  grössten  Ab- teilung des  Bezirks  mach  neun  Gänge ((L  i.  Abteile)"  V.  2. 30";  —  fraUtmm °^wd  (AP,)  Aazavnm  narqm  näirinanua taoxma  upa.bara  "in  die  Gänge  der  grSssten Abteilung  bring.. "■V.2.3o'>,  2)'^gang, Pforte',  mit  z^mS  'Pforte  des  Winters',  Name einer  Örtlichkeit:  ndt^  tä  im  xsnäus  vaipyS (sd.).,V?(LS.)  t?mB\.5i.  1 2.  3)  'Durch- gang durch  — ,  Übergang  über  das  Wasser, Furt,  Brücke':  afqmca  -/«/(AP.)  Y.42.1; —  apqm  .  .  nOvayanqm  patti  °tül  Yt. II.  4.  a)    mit    GS.    Smiatö  (sd.)    'die
Brücke  des  Scheiders'  (beim  letzten  Ge- richt): Ayat  aüT^gpirun  yd^rä  ^vatJ  °tui "wenn  sie  dahin  kommen,  wo  die  Brücke des  Scheiders  ist"  Y.4Ö".  11;  —  frS  toii vispsis  cinvats  frafra  (Sp,  851  m.)  'tum \.46. 10;  —  tarS  änvats  °tSm  Y.  71. 16, V.  7p.  30;  Vr.  7.  i;  — yeiya  urvä  xraodaUl änvatJ  'tä(l£,.) aia(s��)Y.5i.i3.  a)dn. auch  ohne  cinvatB  'die  Brücke'  Kar'  i^,: hrlicit  (Sp.  591  m.)  tarS  'tümcit  la  urväram vahistfm  aÄsm  frapärayem  Y.  ig.  6.
=====16140,16155=====
g6.  784;  TgL  »LpäBÖy-  m,  'Hand',  gr.  «tXofi^.
j.  pirinäi,  ptraiäne  usw.,  Verbalf. :  s.  par>l-.
j.  p«r»näyav-  Adj.   'der  die   bürger-
VgL  parfnin:  —  AbleiL  >iu  'pirtna-, j.  pitfoiHÖi  F.  ./  c :  lies  firimmnäi. j.  ffriyeilt  N.  41:  %,  ^t-  mit  So,  I,
•  Jt  g.  parMant-  Adj,  PPA.:  s.  /ras-.
•  3.  'pvF'asav-  m.  i)  'Rippe'  (nur Komp.).  2)  'Rippengegend,  Bnistscite': JaHitim  {/ii'yum)  hl  •säum  V.  &  54— 56', V.^.  17,  30^.
KompA.  —  VgL  ptirtiau:  —  Pü. :  paAlük.
•  j,  'p>riiav-  m.  'Frage'. KompE.  —  Zum  '^.frai-.
■  j.  p»rasu.masab-  i)Adj. 'von  der  Grösse einer  Rippe';  oitwt . .  fnsuMavatth^m  vä vuvA»»  (ASm.  statt n.)  Z'd  V.ß.iö.  2)0. 'Rippengrösse'  (nur  Komp.).
liehe'*  Mündigkeit  erreicht  hat,  voll-,  gross-  ■  KompE.  —  Pü. :  fahUk  maiät. jährig':  °yus  .  .  *°yu'>  (ND,)  ,  .  *'yunam ''  j  •  j,  p^nskä-  f.  'Preis,  Werf  ":  hat yazat F.  2e;  — *°yu^'^  F.io;  —  ap^rpnJyu  ahmi  \  irfzaitmi  .  .  yaia  aspahe  arsnö  'ta  "wie «^'^  'y*  (als  NSm.)  ^*  ytzi  baväni  (sd.)  "yu  I  viel  Silber?  .  ,  Soviel  als  der  Wert  eines "minderjährig  bin   ich,   noch   nicht   voll-' Rosshengstes  (ist)"  V. i4. 11;  11.
jährig;    wenn   ich   (erst)    ,  ."   YLjp.43;    —         Aus  •//■/-j*i.;Tgl.  aLa/j-a/a,  I»t./»?Äi>»insw.i
DP.)'I  a-hqm   >W>r>sattt   V.^.43.  |      „\'„    ,.  st.=   ia^n,   ^^  t.:    v<,^ai  (L  np!
KompE.,  A-tmyKomp.).  — Komp.:  'piri»a-Y  .  i^/a).  —  ■)  JusTls  abweichende  Fassone  des ^J,.flt.6).  — ai.vgL/w-wj.ü/-m.EN.(?>  — Pü.:'      Aw.  Worts,   2DMG.  49-  684   halle  ich  nicht
/»/■«äf,    (lU   V.  3):    ä/TcnaiänÜ.     —    ■)    Im :      ft,  richtig;  t.  BthU  IFAni.  S.  16.
J)  S^y.    Unticher.    Oder  auch  MSn.,  ...a.*.   *  *J.,  g- p9r»smana- Adj.,  PPM.:  S.Jras-.
Sp.  276  n.  —  4)  VgL  zu  ^flAu  Y.  13.  4.    S.  I         j.  pisialt  P.  44  -.  lies  pn-isin/e.
```


## [2026-09-14T00:54:32.382Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD prs ===\"; grep -n \"prs'\\|prs\\`\\|prsʼ\" SOD_pages.txt | head -20; echo \"=== SOD psn ===\"; grep -n \"pšn'\\|psn'\\|pšn\\`\" SOD_pages.txt | head -20; echo \"=== SOD stnh ===\"; grep -n \"štnh\\|stnh\" SOD_pages.txt | head -20"
}
```


### [2026-09-14T00:54:33.929Z] TOOL RESULT

```
=== SOD prs ===
5137:      a[3ar =>»pr-                                              490 >prsr =* 'prs'r
7448:                                                                    aprse ? ^prs'k
24396:         farnxunde                                                      parsem ^prs'ym
24411:    7204 prs' M                      ^ <o^ <o^U <oUj                    parsanx(e) ©pi. -t
24419:    7205 prs'k B                              ^Lij^^U.
24430:    7207 prs'ym B                      J^^       <v~j>&*P*             (ro)escape
=== SOD psn ===
25300:       spilled                                                7509 psn' M, C                                         -uil
=== SOD stnh ===
7563:      sheep's shoulderblade                                        1326 >pstnh B, S                                i/^i^jJs
7718:     (o)pu (o)/apse5                                      1384 'pw pstnh        B
8909:                                                                  1785 >stnh B                                     jl^*^
25112:       pasaw ^ps^v-                                                     -h, ->; pi. -/ =^>pw pstnh, >pstnh
```


## [2026-09-14T00:54:40.162Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (24411,25300,8909,7563):\n    # count formfeeds before that line\n    pre='\\n'.join(lines[:ln])\n    print(ln, 'leaf', pre.count('\\f'), 'printed~', pre.count('\\f')-66)\nEOF"
}
```


### [2026-09-14T00:54:41.254Z] TOOL RESULT

```
24411 leaf 355 printed~ 289
25300 leaf 367 printed~ 301
8909 leaf 135 printed~ 69
7563 leaf 117 printed~ 51
```


## [2026-09-14T00:54:44.809Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24405,24435p' SOD_pages.txt; echo \"==== psn ====\"; sed -n '25290,25310p' SOD_pages.txt; echo \"==== stnh ====\"; sed -n '8895,8925p' SOD_pages.txt"
}
```


### [2026-09-14T00:54:44.888Z] TOOL RESULT

```
    7203 prs-     B                 (0>>>^^)o-^>,                       parse8 ©<*pari-sadaya =»prsy6-
                                                                        (ro)settle down, (ro)lodge
          prs, pars (pwrs-) ©<prsa- ^prs-, ps-\ 'ps-1
          0o)ask                                                        GMS 409n 1; Tales. 472.12; TSP 2.3; AVS 78
          GMS    145
                                                                  7215 prsnx(y)   M                            ^V^^^^
    7204 prs' M                      ^ <o^ <o^U <oUj                    parsanx(e) ©pi. -t
%        parsa ?, parsa ©<Av. pdrdsu ©ace. f.                           branch
         hour, side                                                     GMS 1142; Gersh. Sogd. Cpds. 1945, 145.2
         GMS 138, 971; Hen. BSOAS 11312.99, 101
                                                                  7216 prsp»r     B                       «x^ , JUj& « jut,
            n p3l6
                                                                        parspar
                                                                        trampled (psp'ry) ©<*pari-spar-       -^nspr-
    7205 prs'k B                              ^Lij^^U.
         parse ?, prsak ? -^prsy                                        TSP 13.3 n p226
         gratitude ?
                                                                  7217 prsprn M                              ^j ^L^ < JJ0.>U
         BSTBL, n pl6; Vim. 53
                                                                       parspar(a)n
    7206 prs>kh B, M                                o> tj+w             pavement
         parsak, parsak ©Khot. palsa ^prs*                              GMS 1028; Hen. BSOAS 12, 307.25
         side, rib
         TSP 7.57 n p211;MSPbl47                                  7218 prst-' S                         Cx^t/^J'JJ
                                                                       parast Cprst-) ©pt. st. -^prstk, pryz-, pryst-2
    7207 prs'ym B                      J^^       <v~j>&*P*             (ro)escape
         parsem ? ©<*samya =»prsym
                                                                        MDii pl72.3f. 6; Gersh. Advice. 88; CII 1990, 84
         oppression, enquiry, punishment
         TSP 2.1149; S W, C2p56, 27                                       E9

==== psn ====

7496 psyt- M, C                               j^    <oJLil           trap ?
                                                                   gulp
                                                                   Sogdica. 21.22, 23b; GMS 81
     pasayd ©pt. St. =*psync-
     (fo)sprinkle, (rcOspill                                  7508 psn-     S, M, C                                 4: <(b
       GMS 600; perf. psYt&r-, BBB 531                             pasan    ©loc. psny\ ace. psnw   =^psyn-, }psn
7497 psrty C                                         <sj&
                                                                   S W apud. Mack. AI 25, 428 n 16; C2 p51 n 5
     pasayde ©pp.
       spilled                                                7509 psn' M, C                                         -uil
       STi 81.14; BSTi 346                                         pasna ©<Av. pasna ©f. ace.
                                                                   heel
7498 psqV C                             <*^i<>rj-
                                                                   BSTii: C2, 51V13 n p98; Bailey. Prolexis. 183;
     paskar =#pskr-
                                                                                                                       302



 psp'cyg
==== stnh ====
                                                                       astamik ^stmyq
      SCE 359; GMS      155                                       1783 >stmykC)) S

1771 >stc» SfB                       (u^>i->»)^u                       eighth
     ast(a) ('st, }sth) ®<*asta =*sV                                   TSP 3.99, 14.17, 9.18; Frag. Len. 69.27; -w, MSP
     eight                                                               b33, 108

      GMS 87, 1316.8; Frag. Len.; >Stht MDii                      1784 >stn B                              J*^jL^-I
1772 WdV-        C *± >st>y-                                           ostan ®<*hista- =^skwn                                *j>r
                                                                       durative particle
1773 >st't S                                               &±*
                                                                       Benv. AO 30, 1966, 46
      astat ©<*aJr5n" =»st>t
      eighty
                                                                  1785 >stnh B                                     jl^*^
      Frag. Len. 117 R5                                                ostana ©Av. fstana; Skt. stana

1774 »st»t- ** >st>y-                                                  breast
                                                                       VJ 6a, 1208; GMS 314 n 1
1775 St'tc S     (j(^./ .-^j^oU ^jc^-j jjj oj^Lil
     astac- ©Av. arstat                                           1786 Jstrwsk M            (.Ji^^i^j^S)^ JjL* (j/ ^5C)
     twenty-sixth day of the month                                     (a)s9rusk ?, (o)susk ? Ostrwsk)
     GMS 357; MDii 149.6; MDiii 91                                     lunar mansion
                                                                       GMS 981; Hen. JRAS 1942, 242 n 1
1776 >st»y- C                                        j,hd[^
                                                                  1787 >stwkry B
     astay, amstay Osty-, 'st*!-) ©impf. mft'y; trans.
                                                                       ast-wakre
       pret. 'fr'dV-, }st}td}r- ^'nst'y-, 'nst't-, 'st'yny,
                                                                                                                    u^   ,
                                                                                                             'tSrmnwkw'nch
```


## [2026-09-14T00:54:57.141Z] TOOL CALL #18: Bash

```json
{
 "command": "ls site/pages/399.jpg 2>/dev/null; pdftoppm -f 399 -l 399 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg399 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg399.png"
}
```


### [2026-09-14T00:54:59.137Z] TOOL RESULT

```
site/pages/399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 64776 Sep 13 20:54 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg399.png
```


## [2026-09-14T00:55:00.871Z] TOOL CALL #19: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg399.png"
}
```


### [2026-09-14T00:55:01.575Z] TOOL RESULT

```

```


## [2026-09-14T00:55:01.556Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T00:55:17.769Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD stnh variants ===\"; grep -n \"'štnh\\|\\`štnh\\|ʼštnh\\|štn\" SOD_pages.txt | head; echo \"=== AHD watkins persna ===\"; grep -n -i \"persna\\|pernula\\|perna\" AHD_watkins1985.txt | head -20; echo \"=== AHD perk ===\"; grep -n -i \"^perk\\|perk-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T00:55:18.881Z] TOOL RESULT

```
=== SOD stnh variants ===
=== AHD watkins persna ===
844:fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
1105:uper. Over. 1. Extended form *uperi in Germanic *uberi in: a. Old English ofer, over: OVER; b. Middle Dutch over, over: ORLOP. 2. Variant form *(sjuper in: a. Latin super, super-, above, over: SOUBRETTE, SOVEREIGN, SUPER-, SUPERABLE, SUPERIOR, SUPREME, (SUPREMO), SUR-; SIRLOIN; b. suffixed form *(s)uper-no- in Latin supernus, above, upper, top: SUPERNAL,; C. suffixed form *super-bhw-o-, “being above” (*bhw-o-, being; see bheue-), in Latin superbus, superior, excellent, arrogant: SUPERB; d. suffixed (superlative) reduced form *sup-mo- in Latin summus, highest, topmost: SUM, SUMMIT; @. var- iant form *(s)juprd in Latin supra, above, beyond: (so- PRANINO), SOPRANO, SUPRA-; SOMERSAULT. 3. Basic form *uper in Greek huper, over: HYPER-. [Pok. uper 1105.]
2069:PEACE pag- PEARL! persna PEASANT pag- PECCABLE ped-1 PECCADILLO ped-! PECCANT ped-1 PECTEN pek-2 PECTIN pag- PECTORAL peg- PECULATE peku- PECULIAR peku- PECUNIARY peku- -PED ped-! PEDAGOGUE ag- PEDAL ped-! PEDATE ped-! PEDESTAL sstel- PEDESTRIAN ped-! PEDI- ped-1 PEDICEL ped-1 PEDICULAR pezd- PEDICURE cura PEDIGREE gere-2 PEDO-! ped-1 PEDO-2 pau- PEDUNCLE ped-1 PEEL? pag-
2327:suP2 seue-2 SUPER- uper SUPERABLE uper SUPERANNUATED at- SUPERB uper SUPERCILIOUS kel-2 SUPERCILIUM kel-2 SUPEREROGATE reg-' SUPERFETATE dh@(i)- SUPERFLUOUS bhieu- SUPERIOR uper SUPERJACENT yé- SUPERLATIVE tele- SUPERNAL uper SUPERNATANT sna- SUPERNUMERARY _nem- SUPERSCRIBE skribh- SUPERSEDE sed-1 SUPERSTITION sta- SUPERVENE gWa- SUPERVISE weid- SUPINE! upo SUPINE? upo SUPPLANT plat- SUPPLE plek-, upo SUPPLICATE plek- SUPPLY pele-1 SUPPORT per-2 SUPPOSE apo- SUPPRESS per-5 SUPPURATE pu-2 SUPRA- uper SUPRALAPSARIAN leb-1 SUPREME uper SUPREMO uper SUR- uper SURCULOSE swer-3 SURD swer-2
=== AHD perk ===
165:Terms for the furrow are perk-? and selk-; wog”h-ni- designated the wedge-shaped plowshare. Other related roots are yeug-, “to yoke,” serp-', “sickle, hook,” and kerp-, “to gather, pluck” (HARVEST). The root g”ere-?, “heavy,” is the probable base of *g”ero-nd-, “hand mill” (QUERN). The term is found throughout the Indo-European-speaking world, including India.
844:fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
1546:FURBISH prep- FURL leig-1 FURLOUGH leubh- FURNACE gWher- FURNISH per! FURROW perk-2 FURTHER per! FURTIVE bher-1 FURUNCLE bher-1 FURUNCULOSIS_ bher-1 FURZE piiro-
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
```


## [2026-09-14T00:55:18.997Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN stethoscope ===\"; grep -n -i \"stethoscope\" KLN_1966.txt KLN_1971.txt | head; echo \"=== KLN pearl ===\"; grep -n -i \"pernula\\|perna \" KLN_1966.txt | head"
}
```


### [2026-09-14T00:55:19.080Z] TOOL RESULT

```
=== KLN stethoscope ===
KLN_1971.txt:180988:phonendoscope, n., an intensifying stethoscope. 
KLN_1971.txt:232334:as in stethoscope. — Gk. axvjffo-, fr. ax7)&o<;, 
KLN_1971.txt:232343:stethoscope, n., an instrument for examining the 
KLN_1971.txt:232344:sounds produced in the body. — F. stethoscope, 
KLN_1971.txt:232350:Derivatives: stethoscope , tr. v., stethoscop-ic , 
KLN_1966.txt:28578:phone,  n.  ( colloq .)  —  Abbreviation  of  telephone, -phone,  combining  form  meaning  ‘voice’,  as  in megaphone,  microphone,  telephone.  —  Fr.  Gk. 9« vf],  ‘sound,  voice’.  See  phone,  ‘speech  sound’, phoneme,  n.,  a  distinctive  sound  or  group  of sounds.  —  F. phoneme,  fr.  Gk.  961751//,  ‘sound, utterance’,  fr.  901V7).  See  phone,  ‘speech  sound’, and  cp.  the  second  element  in  grapheme,  hyph- eme,  semanteme,  solideme,  morpheme. Derivative:  phonem-ic,  adj. phonendoscope,  n.,  an  intensifying  stethoscope. —  Compounded  of  Gk.  9COV7),  ‘sound,  voice’, evSov,  ‘within’,  and  -oxdmov,  fr.  cxoteeiv,  ‘to look  at,  examine’.  See  phone,  ‘speech  sound’, endo-  and  -scope.
KLN_1966.txt:36771:stet,  intr.  v.,  direction  to  printer  to  disregard  cor¬ rection  made  in  the  texts,  whence  stet,  tr.  v.,  to cancel  a  correction.  —  Fr.  L.  stet,  ‘let  it  stand’, 3rd  sing.  pres.  subj.  of  stare,  ‘to  stand’.  See  state, stetho-,  combining  form  meaning  ‘breast,  chest’, as  in  stethoscope.  —  Gk.  ctxtj&o-,  fr.  axvjRo?, ‘breast’,  prob.  cogn.  with  OI.  stanah,  ‘teat,  nip¬ ple’,  Avestic  fshtana-,  Arm.  stin,  of  s.m. stethometer,  n.,  an  instrument  for  measuring  the expansion  of  the  chest  during  breathing.  — Compounded  of  stetho-  and  Gk.  pixpov,  ‘meas¬ ure’.  See  meter,  ‘poetical  rhythm’.
KLN_1966.txt:36772:Derivatives :  stethometr-ic,  adj.,  stethometr-y,  n. stethoscope,  n.,  an  instrument  for  examining  the sounds  produced  in  the  body.  —  F.  stethoscope, lit.  ‘instrument  for  examining  the  breast’,  coined by  the  French  physician  Rene-Theophile-Hya- cinthe  Laennec  (1781-1826)  in  1819  fr.  Gk. ox^-9-o?,  ‘breast’,  and  -oxdntov,  fr.  <Jxo7t£tv, ‘to  look  at,  examine’.  See  stetho-  and  -scope. Derivatives:  stethoscope,  tr.  v.,  stethoscop-ic, stethoscop-ic-al,  adjs.,  stethoscop-ic-al-ly,  adv., stelhoscop-y,  n.,  stethoscop-ist,  n. stevedore,  n.,  one  employed  at  loading  and  un¬ loading  ships.  —  Sp.  estibador,  fr.  estibar,  ‘to pack’,  fr.  L.  stipdre,  ‘to  crowd  together,  com¬ press’.  See  stipate  and  cp.  steeve,  ‘to  stow’.  Sp. suff.  -dor  represents  L.  -tor;  see  -tor.
=== KLN pearl ===
27779:pearl,  n.,  a  concretion  in  the  shell  of  various  mol- lusks,  used  as  a  gem.  —  ME.  perle,  fr.  MF. (=  F.)  perle,  prob.  borrowed  fr.  It.  perla,  fr. VL.  *perla  (whence  also  O Proven?.,  Sp.  perla. Port,  perola),  which  is  a  blend  of  L.  perna,  ‘ham, sea  mussel,  pearl’,  and  sphaerula,  ‘a  small  ball’, dimin.  of  sphaera,  ‘ball’.  L.  perna  stands  for *persna  and  is  cogn.  with  OI.  parsnih,  ‘heel’, Avestic pashna-  ‘heel’,  Gk.  7TTepv7],  Goth.  Zaire, na,  OHG.  fersana,  MHG.  versene,  verse,  G. Ferse,  Du.  verzenen  (pi.),  OS .fersna,  OE .  fiersn, of  s.m.  For  L.  sphaera  see  sphere.
```


## [2026-09-14T00:55:36.831Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=36740 && NR<=36790' KLN_1966.txt | grep -n \"^[0-9]\\{3,4\\}$\\|^\\s*1[45][0-9][0-9]\\s*$\" ; echo \"---formfeed leaf of line 36771---\"; python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\npre='\\n'.join(t[:36771]); print('leaf',pre.count('\\f'))\n\"; echo \"--- look for page numbers near ---\"; sed -n '36760,36780p' KLN_1966.txt | cut -c1-200"
}
```


### [2026-09-14T00:55:38.169Z] TOOL RESULT

```
6:1513
48:1514
49:1515
---formfeed leaf of line 36771---
leaf 803
--- look for page numbers near ---
Derivative:  stern-ed,  adj. sternal,  adj.,  pertaining  to  the  sternum.  —  Medi¬ cal  L.  sterndlis,  fr.  L.  sternum.  See  sternum  and adj.  suff.  -al.
stemo-,  combining  form  meaning  ‘sternal  and’.
See  sternum.
stemson,  n.,  sternpost  bolted  to  the  keelson.  — Coined  fr.  the  noun  stern  and  the  second  syl¬ lable  in  keelson.  Cp.  stemson. sternum,  n.,  breastbone  ( anat .)  —  ModL.,  fr
Derivatives:  sternutat-ive,  adj.,  sternutat-or,  n., sternutat-ory,  adj.
sternward,  adj.  and  adv.  —  Compounded  of stern,  n.,  and  suff.  -ward, sternwards,  adv.  —  Compounded  of  stern,  n., and  suff.  -wards.
steroid,  n.,  any  of  a  group  of  compounds  includ¬ ing  the  sterols,  bile  acids  and  sex  hormones.  — Coined  fr.  ster(ol)  and  Gk.  -oeiSt;;,  ‘like’,  fr. eTSoc,  ‘form,  shape
9\
sterol,  n.,  any  of  a  group  of  solid  alcohols  ( bio - chem.)  —  Back  formation  fr.  cholesterol, stertor,  n.,  heavy  snoring  (med.)  —  Medical  L., fr.  L.  stertere,  ‘to  snore�
stertorous,  adj.,  characterized  by  snoring.  — Formed  with  the  suffixes  -or  and  -ous  fr.  L.  ster¬ tere,  ‘to  snore',  which  is  prob.  rel.  to  L.  sternu¬ ere,  ‘to  sneeze’
Derivatives:  stertorous-ly,  adv.,  stertorous-ness, n.
stet,  intr.  v.,  direction  to  printer  to  disregard  cor¬ rection  made  in  the  texts,  whence  stet,  tr.  v.,  to cancel  a  correction.  —  Fr.  L.  stet,  ‘let  it  stand’, 3rd  sing
Derivatives :  stethometr-ic,  adj.,  stethometr-y,  n. stethoscope,  n.,  an  instrument  for  examining  the sounds  produced  in  the  body.  —  F.  stethoscope, lit.  ‘instrument  for  examini
Stevia,  n.,  a  genus  of  shrubs  (bot.)  —  ModL., named  after  the  Spanish  botanist  Pedro  Jaime Esteve  (died  in  1566).  For  the  ending  see  1st suff.  -ia.
stew,  tr.  and  intr.  v.,  to  cook  slowly.  — -  ME. stuert,  stuwen,  to  bathe’,  fr.  OF.  estucer,  ‘to bathe  in  warm  water’  (whence  F.  etuver,  ‘to heat,  stove,  stew'),  fr.
Derivatives:  stew,  n.,  dish  cooked  by  stewing, slew-able,  adj.,  stew-ed,  adj.,  stew-y,  adj. stew,  n.,  a  brothel.  —  ME.  stuwe,  stue,  fr.  OF. estuve  (F.  elute),  ‘sweating  roo
stew,  n.,  a  fishpond.  —  ME.  stewe,  fr.  OF.  estui, ‘prison;  case,  depository’  (whence  F.  etui,  ‘case, box’),  back  formation  fr.  OF.  estuier,  ‘to  shut in,  hold,  keep�
Derivatives:  steward,  tr.  and  intr.  v.,  steward¬ ess,  n.,  steward-ly,  adj.  and  adv.
Stewartia,  n.,  a  genus  of  plants  of  the  tea  family (bot.)  —  ModL.,  named  after  John  Stuart — also written  Stewart — (1713-92),  Marquis  of  Bute. For  the  ending  see  1st  suf
stibine,  stibin,  n.,  a  colorless,  poisonous  gas, SbH3  (chem.)  —  Formed  from  next  word  with chem.  suff.  -ine,  -in;  so  called  because  it  con¬ tains  antimony.
stibium,  n.,  antimony.  —  L.  stibium,  ‘powdered antimony’,  fr.  Gk.  axifit,  axippi,  ‘a  sulfuret  of antimony’,  fr.  Egypt,  stm,  Demotic  slim.  Cp. antimony.
```


## [2026-09-14T00:55:44.864Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'], ensure_ascii=False, indent=1))\n\""
}
```


### [2026-09-14T00:55:46.019Z] TOOL RESULT

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


## [2026-09-14T00:55:51.124Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor w in ['پاشنه','پستان']:\n    print('=====',w)\n    for i,p in enumerate(pages):\n        if w in p:\n            print('leaf',i,'printed~',i-222)\nEOF"
}
```


### [2026-09-14T00:55:52.056Z] TOOL RESULT

```
===== پاشنه
leaf 100 printed~ -122
===== پستان
leaf 469 printed~ 247
leaf 498 printed~ 276
leaf 529 printed~ 307
leaf 557 printed~ 335
leaf 629 printed~ 407
leaf 640 printed~ 418
leaf 757 printed~ 535
```


## [2026-09-14T00:55:55.609Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[629][:3000])\nEOF"
}
```


### [2026-09-14T00:55:56.903Z] TOOL RESULT

```
حمشوق است.
بی جانشین ۳ ۳
شخصی ات که چون صاحب دکان برخیزد او
یجای صاحب د کان بنشیند وکالا بقروشد
ی خم زدن - کنابه از کریختن
باشث .
ی دست گردن ۰ کنابه از پنبان
کردن وذخیره‌نهادن باشد .#8
پستادست - با دال ابجد بروزن
هرجا هست + بمعنی نسیه پاشد و آن خربدن
اسباب واچناسی است که بعد از چند روز قیمت
مدهند ۱ # .
پستان مادد بر بدن « کنابه از
حرعی رشره وبی‌همنی- وحق‌ناشناسی وبی‌حشفتی
ویی هقی سنارتن بنشد. 9
سته‌شکر فشان- کنایه‌از لب ودهان
9 رد : مساوست .
پستای - بکس اول , اوستا 15100202 (یستان) .
پهلوی ۳)(5020 و ۳15428 , حتدی‌باستان - 81888, ارمنی
هناد .انبانی 5)20ا0 < اسعق ۰۰۳۱۷ کیلکی ۳540 ؛
غده‌های بزر که برسينةٌ جانوران که از آنها شیری فراود . دوغده
بزر که برسيتة آدمی که فزه وتا در کتر است و از آنها شیز
مقطح مت
یرون میا بد:
تهی‌دید پستان کاوش زشیر دل میزبان جوان کشت پیر .
فردوسی طوسی. «لفت نامه».
۵ پستاقك - بکسر اول وفتح پنجم ( از: منان ۵ پوند شباحت) »
ظرفی ازبلور با غیر آن شبیه بستان که مادران بی‌شیر» شیرحیوان با زنی دیگر
پتانك در آن‌کنند وبدهان طفل هند . * لفت نامه *.
۵ پسه ‏ بکر اول وشتح سوم» درتازی فستق ازآرامی فتفا (بکسراول), چه معا آن
شام ( سوربه ) است و بونانی نقل شد ۳۱50۵108 و از آن
بدیگر زبانهای ارویابی داخن شد . در ابتالیابی نمی 5)2ز۳ هه
«لفس» ؛ درختی است میوه دار که درآب و هوای معتدل واراضی --
سيك خوب میروید . مهمترین نوع آن همان یسته معمولی تک
( ۷۵۲2 ۱582012 ) است . مراکز مهم یس ابران کرمان,
آذرباجان» داعفان وفزوناست.رگ: فرهنگه روستابی۲۷۵ بعد بسله
وثابتی ۱۷۰ و کل کلاب ۰۲۱۷ ۱
۵ پسر - بکس اول وفتح دوم (درلهجةٌ مر کری) » در پارسی باستان واوستا ۳09072 ؛
پهلوی ۳فکنا۳ و کنام [ رك و ره سیون , کردی 15 . استی +5
واع1] , بلوچی 0۱1528 , وخی 0۵4۲ : شغنی 0۷6 . سربکلی ۳4: عنجی ۳۲ » ممرب
آن قور در قنفور؛ امه ها ور مه راک ممصص :ریات
#9" , نطنزی ۳0۲ <2 . ۱ص ۸۵ ۰ ۰ سمثانی ۳1۳ ۶ مشگکری و نرخةٌ
ولاسگردی0ا۳» شهمیرزاوی ۳6526۲ 4 ,۲ صس ۱۸۷ در فارسی نیز پس ویور؛ فرژند فرینه
این . ولد .
```


## [2026-09-14T00:56:09.014Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(560,600):\n    p=pages[i]\n    if 'اشن' in p or 'پاش' in p:\n        print('leaf',i,'printed~',i-222, [l for l in p.split('\\n') if 'اشن' in l or 'پاش' in l][:6])\nEOF"
}
```


### [2026-09-14T00:56:10.095Z] TOOL RESULT

```
leaf 566 printed~ 344 ['پاشان باشد - و بمعنی پاشیدن هم هست6']
leaf 567 printed~ 345 ['حزار فابده با صد هزار پاداشن ۷ .', 'رد پاداشن ۳']
leaf 574 printed~ 352 ['«اسشق ۰۲۷۲ . ٩\u200f - ره : پاچ نامه و پاش نامه.']
leaf 576 printed~ 354 ['پاش بر وزن ماش » بمعشی پربشان', 'باشنا با فون بروژن آشناء یاشنة بارا', '0 رله : باسكث . ۴ رل : باشنه.', '۴ ره : پاششگه ویاشنگه.']
leaf 577 printed~ 355 ['و همال پاش ۷ - . .', 'باشنك - بروزنآونگ , خوشه کوچكث', 'پاشیب « بر وزنآسیب, نردبان وزیته']
leaf 582 printed~ 360 ['وخشك کرده باشنف ۰']
leaf 583 printed~ 361 ['باشند تا مردم با دانی آب از آن بردارند - و ته']
leaf 585 printed~ 363 ['(۱) خم۳ : بتراشند .']
leaf 590 printed~ 368 ['نظر داشتن و چشم برنداشنن باشد - و بمنی | وبندکی و خدمتکاری باشد .']
leaf 594 printed~ 372 ['۵ پاشن ی اول » پهلوی ۳۱06120 » اوستا و سانسکریت 26 (طبخ). کردی']
leaf 596 printed~ 374 ['پدر پاشد؟ - و ختح اول درختی را گوبند که']
leaf 597 printed~ 375 ['کرده باشند و']
leaf 599 printed~ 377 ['و کلوله کرده باشند , و بکر اول هم آهده', 'براش بفتح اول\u200cبروزن\u200cلواش» پاشیدن', 'و پاشانیدن - و فرو شاندن\u200cباشد۷ .']
```


## [2026-09-14T00:56:15.253Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (576,577):\n    print('======== leaf',i,'printed~',i-222)\n    print(pages[i][:2600])\nEOF"
}
```


### [2026-09-14T00:56:16.202Z] TOOL RESULT

```
======== leaf 576 printed~ 354
بر ون دلدگار » بیعتی سار است که فگد
باشد؟ _ ولگد کوب راه مگفتماند - و بضم ثالت
درآب و درخشکی میکنند .
پاسبان ۴ - با بای ابجدبروزنآسمان,
شب زنده دار و محافظت کنندء ۴ باشد؟ .
پاسبان طار م نهم- کابه‌از کر کب
زحل باشد .
پاسبان قلاث - بنمنی پامبان طارم
نهم ات که کوک رحل باشد .
پاسخ؟ -
دار ؛ ۳ در مقابل سوال است .9
پاسره - بنتح ثاك بر وزن تاسره »
زه‌عنی راکه ء بند که‌صاحب زراعت دروجه‌اخراجات
صرف اخراجات دبواای و غيره کنئد .
پاساث - منم ثاكت بروزن نازك. خمیازه
و دهان دره باشد . و بفتح الث یز آمده
ات ۷۸ .
: پاستگه - بر وزن آهنگه, آنچه ند
۱ - رك . یاسار.
بان ( پوند اصاف ) «اسشق ۲۷4».
زر ۱
دیگ ۷
پاسواد -_بممنی سوار پاست که پبادة
و چايك باشد .
پاسه - بی وزن 8 بمعشی تاسه
و تلواسه است که عیل کردن هر چیز -. و غم
واندوه ‏ و فشردن کلو باشد » دباین حعنی بجای
#9 9
پاش بر وزن ماش » بمعشی پربشان
است منی پربشان کن و از هم جدا ساز و بر
افعان .
با شات ۷" فتح الث‌بروزن ناولگ. نمعئی
خمازه باشد۷۷.
باشنا با فون بروژن آشناء یاشنة بارا
کوبند ۷۴- وخیار ثر خربزه و هندوانه و کدو
وامثال آ نرائیز کفته‌اند که‌بجهت نخم نگاهدار بر۴٩۰‏
+ کلتان ۵۱ *.
بارستگه .
ارمنی ۳80285201 < اسخق ۷۵ > جمماً
* را : باشك ۸ ی
. لت نامه». ٩‏ مرک از
نتارکان » « الفهيم بنقل لفت نامه» .
6۰ خاکرا نذمکی ده ی که باش
0 رله : باسكث . ۴ رل : باشنه.
۵ پاسدار - نگاهبان, مراقب :
بزد تیغ بر کردن پاسدار
۴ ره : پاششگه ویاشنگه.
======== leaf 577 printed~ 355
۳66 77
و همال پاش ۷ - . .
باشنك - بروزنآونگ , خوشه کوچكث
انگور را کویند - و خیار و خریزه و هندوانه
کدو و امثاآنر" نیز کفته اندکه بجهت نخم
نگاهدارند , و با باهنگك و یاچ جنگ مترادف
لت ۲ :
اس بان فرچندوا
و
انگوریرا نیز کفته اند که برتال خشك شده
باشد ۴ . «د
پاشیب « بر وزنآسیب, نردبان وزیته
یابه را گویند #
هاغر - بر وزن لاغر, ستوئی راکویند
که مقف خانه بدان. قرارگیرد .
پاغره - منم غبن له دار و فتح رای
بی نقطه ؛ مرضی است که پای آ دمی‌مقابل بخیکی
یود وآنرا عربی داء الفیل ۴ خوانند ؛ وبعضی
گویند زحمتی و آزاری است
دیگر بهم زسیده باشد حانند غلولهُ " که تا زحمت
اول برطرف شودا هم برطرف نگردد .
۱ - رك:پاچ‌نامه و پاژنامه .
۱ - بود زوداکه آیی نبك خاموی
۲ - را : باافزار .
۰ باغند - نم ثالث و سکون نون ودال
ابجد . کلولهٌ نب حلاجی کرده را گویند
پاغنده - بنم تالت و فتح دال ابجد .
بمعنی باغند است که كلولة پثبةٌ حلاجی کردم :
رید ثالك هم کفته‌اد که بر وزن
پاغوش - باواو مجهوذبر وزن آغوشی,
ب‌منی غوطه باشد بعنی سرباآب فرو بردن ۷.
بافز اد - مخنف با افزار است که
کنش باشد ۷.
پالك ۵« بر وزن خاك . بدشی صاف
ویی‌غش و پاکیزه باشد - و بمعنی همه وتمام
و باقی هم آمده است ت چنانکه کوبند «حساب‌ا
با شد * ممنی‌تمام‌شدو چیزی نماندو *پابردند»
عنی همه با بردند و چیزینگذاشتند 2
پا کار باکاف بروزن‌نلچار ؛ کسی‌را
گونن دکه چون تحصیل داری بجابی یابد او زد
آزمردم تحصیل کند وبتحصل‌داردهدوشضصی‌رالیز
کویند که‌ستراح‌و ادبخانعراجاروب کند وپا کیزه
اوه وا دای کتای عو اننعت ومنللن خدستر)
لز کفته‌اند ۳
پاکان خط اول کید زاب
و کروبیان و حاملان عرش مملی باشد .
. «لخت نامه >.
« . ۱ ص ۲۹۲
6 وخ 51202 ۳8. سر یکلی 0۷6112 «اره
ی
```


## [2026-09-14T00:56:30.358Z] TOOL CALL #28: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:355 --image 2>&1 | head -40"
}
```


### [2026-09-14T00:56:31.526Z] TOOL RESULT

```
no scan of BQT covers printed page 355 (see 'scans' in refs_online.json)
```


## [2026-09-14T00:56:40.410Z] TOOL CALL #29: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-14T00:56:40.454Z] TOOL RESULT

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


## [2026-09-14T00:56:46.516Z] TOOL CALL #30: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B4%D9%86%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/p%C4%81r%C5%A1nas\" \\\n \"https://en.wiktionary.org/wiki/%CF%83%CF%84%E1%BF%86%CE%B8%CE%BF%CF%82\" \\\n \"https://www.etymonline.com/word/pearl\" \\\n \"https://www.etymonline.com/word/stethoscope\" ; do\n echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 399 verification (Perk 2 / Persna / Pesteno)\"; done"
}
```


### [2026-09-14T00:56:50.666Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88
/home/sfmqrb/git/rishe/data/verification/sources/web/93eaf6e5d0758898.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B4%D9%86%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/0ada1111cb15d4aa.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D8%A7%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/e7d58c15d60b531e.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/p%C4%81r%C5%A1nas
/home/sfmqrb/git/rishe/data/verification/sources/web/61b30301d4bf6a4c.txt
### https://en.wiktionary.org/wiki/%CF%83%CF%84%E1%BF%86%CE%B8%CE%BF%CF%82
/home/sfmqrb/git/rishe/data/verification/sources/web/489badc3b09ed868.txt
### https://www.etymonline.com/word/pearl
/home/sfmqrb/git/rishe/data/verification/sources/web/74ad65fd17d69e92.txt
### https://www.etymonline.com/word/stethoscope
/home/sfmqrb/git/rishe/data/verification/sources/web/a4226b25e3f8845b.txt
```


## [2026-09-14T00:56:53.088Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 93eaf6e5d0758898 0ada1111cb15d4aa e7d58c15d60b531e; do echo \"######## $f\"; grep -n -i -A12 \"Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-14T00:56:54.099Z] TOOL RESULT

```
######## 93eaf6e5d0758898
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
--
82: Etymology 1 
83-
84- 2.1.1 
85- Pronunciation 
86-
87- 2.1.2 
88- Noun 
89-
90- 2.1.2.1 
91- Derived terms 
92-
93- 2.1.2.2 
94- Descendants 
--
97: Etymology 2 
98-
99- 2.2.1 
100- Pronunciation 
101-
102- 2.2.2 
103- Noun 
104-
105- 2.3 
106- References 
107-
108- Toggle the table of contents 
109-
--
176: Etymology
177- [ edit ] 
178-
179- Borrowed from Persian پهلو ( pahlû , “ side, flank ” ) .
180-
181- Noun
182- [ edit ] 
183-
184- پهلو • ( pehlu ) 
185-
186- side , flank , the flesh between the last rib and the hip 
187- Synonym: بوگور ( böğür ) 
188-
--
219: Etymology 1
220- [ edit ] 
221-
222- Inherited from Middle Persian [script needed] ( pʾhlwk' /⁠pahlūg⁠/ ) , from Old Persian *parθukah , suffixed from Proto-Iranian *párcuš ( “ rib ” ) . [ 1 ] Compare Northern Kurdish parsû ( “ rib ” ) , Sanskrit पर्शु ( parśu , “ rib ” ) , Russian пе́рси ( pérsi , “ bosom ” ) .
######## 0ada1111cb15d4aa
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Derived terms 
75-
76- 1.4.2 
77- Descendants 
--
152: Etymology
153- [ edit ] 
154-
155- From Proto-Indo-Iranian *pā́ršniš , from Proto-Indo-European *tpḗrsneh₂ .
156-
157- Pronunciation
158- [ edit ] 
159-
160- ( Classical Persian ) IPA ( key ) : /paːʃ.ˈna/ 
161-
162- ( Dari, formal ) IPA ( key ) : [pʰɑːʃ.ná] 
163-
164- ( Dari, formal ) IPA ( key ) : [pʰɑːʃ.ná] 
######## e7d58c15d60b531e
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Derived terms 
75-
76- 1.4.2 
77- Descendants 
--
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Noun 
95-
96- 2.3.1 
97- Derived terms 
98-
99- 2.4 
100- References 
--
190: Etymology
191- [ edit ] 
192-
193: Etymology tree
194-
195- Proto-Indo-European *pstḗn 
196- Proto-Indo-European *pstén-o-s 
197- Proto-Indo-Iranian *pstānás 
198- Proto-Iranian *pstānáh 
199- Middle Persian 𐫛𐫏𐫘𐫤𐫀𐫗 ( pystʾn' /⁠pestān⁠/ ) 
200- Persian پستان 
201-
202- Inherited from Middle Persian 𐫛𐫏𐫘𐫤𐫀𐫗 ( pystʾn' /⁠pestān⁠/ ) , from Proto-Iranian *pstānáh , from Proto-Indo-Iranian *pstānás . Cognate with Sanskrit स्तन॑ ( stána ) , Old Norse speni , Ancient Greek στήνιον ( stḗnion ) , Old Armenian ստին ( stin ) .
203-
204- Pronunciation
205- [ edit ] 
--
305: Etymology
306- [ edit ] 
307-
308- PIE word 
309- *pstḗn 
310-
311- Borrowed from Classical Persian پستان ( pistān , “ breast; udder ” ) .
312-
313- Pronunciation
314- [ edit ] 
315-
316- ( Standard Urdu ) IPA ( key ) : /pɪs.t̪ɑːn/ 
317-
--
386: Pages with etymology trees
```


## [2026-09-14T00:57:12.229Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### stethos\"; grep -n -i -A10 \"^ Etymology$\" 489badc3b09ed868.txt | head -40; echo \"##### etymonline pearl\"; sed -n '1,80p' 74ad65fd17d69e92.txt | grep -n -i -A6 \"pearl\" | head -40; echo \"##### etymonline stethoscope\"; grep -n -i -B2 -A8 \"stethoscope (n\" a4226b25e3f8845b.txt | head -40"
}
```


### [2026-09-14T00:57:13.395Z] TOOL RESULT

```
##### stethos
156: Etymology
157- [ edit ] 
158-
159- As this word is also Doric and Aeolic , the connection with ῐ̔́στημῐ ( hĭ́stēmĭ , “ to stand ” ) must be given up. The similarity to στήνιον ( stḗnion ) , Old Armenian ստին ( stin , “ breast ” ) and Sanskrit स्तन॑ ( stána , “ female breast ” ) is hardly coincidental. If cognate, the relation between this word and στήνιον ( stḗnion ) would be like that of Latin plēnus ( “ full ” ) to πλῆθος ( plêthos , “ multitude ” ) .
160-
161- Pronunciation
162- [ edit ] 
163-
164- IPA ( key ) : /stɛ̂ː.tʰos/ → /ˈsti.θos/ → /ˈsti.θos/ 
165-
166- ( 5 th BCE Attic ) IPA ( key ) : /stɛ̂ː.tʰos/ 
##### etymonline pearl
1:URL: https://www.etymonline.com/word/pearl
2-FETCHED: 2026-09-14T00:56:50Z
3-STATUS: 200
4:TITLE: Pearl - Etymology, Origin & Meaning
5-
6:Pearl - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
--
21: Origin and history of pearl 
22-
23: pearl (n.) 
24-
25: "nacreous mass formed in the shell of a bivalve mollusk as a result of irritation caused by some foreign body," early 14c., perle (mid-13c. as a surname), from Old French perle (13c.) and directly from Medieval Latin perla (mid-13c.), which is of unknown origin. Perhaps from Vulgar Latin *pernula , diminutive of Latin perna , which in Sicily meant "pearl," earlier "sea-mussel," literally "ham, haunch, gammon," so called for the shape of the mollusk shells.
26-
27: Other theories connect it with the root of pear , also somehow based on shape, or Latin pilula "globule," with dissimilation. The usual Latin word for "pearl" was margarita (see margarite ).
28-
29: Used from 14c. of anything valuable or of the finest kind; from mid-15c. of something small, round, and glistening white. For pearls before swine , see swine . Pearl Harbor translates Hawaiian Wai Momi , literally "pearl waters," so named for the pearl oysters found there; transferred sense of "effective sudden attack" is attested from 1942 (in reference to Dec. 7, 1941).
30- also from early 14c. 
31-
32: pearl (v.) 
33-
34: late 14c., "to adorn with pearls," from pearl (n.). From 1590s as "to take a rounded form" (intrans.); from c. 1600 as "to make into a form, or cause to assume the form and appearance, of a pearl" (trans.). Related: Pearled; pearling .
35- also from late 14c. 
36-
37: Entries linking to pearl 
38-
39- margarite (n.) 
40-
41: "a pearl," late Old English, from Late Latin margarita (see Margaret ). Figuratively, "that which is precious or excellent, a priceless quality or attribute;" also used as an epithet for Christ, Mary, etc., late 13c. Also margerie (mid-14c.). Related: Margaritic .
42-
43- pear (n.) 
44-
45- Middle English pere , from Old English pere , peru "fruit of the pear tree," common West Germanic (Middle Dutch, Middle Low German pere , Old High German pira , bira , Dutch peer ), from Vulgar Latin *pera , variant of Latin pira , plural (taken for fem. singular) of pirum "pear," a loan word from an unknown source, perhaps Semitic or a lost Mediterranean language. It likely shares an origin with Greek apion "pear," apios "pear tree." Their cultivation began as much as 3,000 years ago.
46-
47- swine 
##### etymonline stethoscope
21- Origin and history of stethoscope 
22-
23: stethoscope (n.) 
24-
25- instrument for examining the chest, 1820, from French stéthoscope , coined 1819 by its inventor, French physician René-Théophile-Hyacinthe Laënnec (1781-1826), from Greek stēthos "chest, breast" + -scope . Greek stēthos is perhaps related to sternon (see sternum ); it meant "front of the chest," and was only rarely used of a woman's breasts, but in Modern Greek it became the preferred polite term. Related: Stethoscopic; stethoscopically ; stethoscopy .
26- also from 1820 
27-
28- Entries linking to stethoscope 
29-
30- sternum (n.) 
31-
```


## [2026-09-14T00:57:37.294Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS pahlug ===\"; grep -n -i \"pahlūg\\|pahlug\\|pahlūk\" SNS_pages.txt SNS.txt 2>/dev/null | head -10; echo \"=== HRN ===\"; grep -n -i \"pahlū\\|pahlu\\b\\|pāšna\\|pasna\\|pistān\\|pistan\" HRN.txt | head -20"
}
```


### [2026-09-14T00:57:37.355Z] TOOL RESULT

```
=== SNS pahlug ===
=== HRN ===
9102:ap. ni + [/^pais-, nipistanaiy 'schreiben* 2) — ai.
```


## [2026-09-14T00:57:39.142Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n -i \"pahlu\\|päsna\\|pasna\\|pistan\" HUB.txt | head -20; echo \"=== SYN Buck breast/heel/rib ===\"; grep -n -i \"pistan\\|pahlu\\|pasna\" SYN.txt | head -10; echo \"=== IEC Mann ===\"; grep -n -i \"persna\\|pstēn\\|psteno\" IEC.txt | head -10"
}
```


### [2026-09-14T00:57:39.233Z] TOOL RESULT

```
=== HUB ===
406:*) Vgl. auoh phi. stik ip sftk-pistan *with prominent breasts'
1484:342. Np. pahlu 'Seite' hat mit zd. pere&U" *breit*, skr.
1487:ZPGl. 10: paresU' -= phi. pahluk Rippe etc.) zuriick.
4817:von zd. ap. ni-, vgl. ap. nipistam geschrieben', nipiStanaiy- 138 -
6212:*schreiben', ap. nipistanaii/; kdbln *Mitgift* = kdvm JRAS.
6597:2) Wie aber verhalt sich np pistan 'Brust' zu zd. fstana-? Vgl.
6598:oben p. 41. Etwa pistan (aus ^pdatdna-?) zu. fstana' (aus *pstana-)
7386:pahaliim (= pahlim, pahlum) = phi. pahlum Vortrefflich'
7390:kann freilich pahlum nach § 89 auch auf ein zd. ^partemar-
7588:pahlu *Seite' = zd. peresu-^ paresu-^ skr. pargu-j ap. *pard^U',
8296:aviskcira-; pasna Terse' = zd. pasna-, skr. parSni- u. s. w.
8410:das Verhaltniss von zd. fstdna- zu np. pistan 'Brust', siehe
8440:= ap. nipistanaiy, pr. nuvesam, Wrzl. pdk^ ; histan 'lassen*,
8611:altererbtem Suffix ak = ap. a-ka) ; pasna *Ferse' = phi.
8612:pasnak, zd. pasna-; dana 'Korn' = phi. danak (arab. danaj
8633:pahlu 'Seite* (reimt auf buzu Fird. I, 454, 352) = phl. j^aA/wi
9035:b) Ap. sn = np. sw und s: pasna 'Ferse = phi. pas-
9036:nakj zd. pasna-, skr. parsnu; tisna 'durstig = phi. iisnalc,
=== SYN Buck breast/heel/rib ===
6248:Sp. pierna, fr. Lat. perna ‘ham, haunch’ (esp. of pork) : Grk. mrépva ‘heel, ham’, Skt. parsni-, Av. pasna-, Goth. fairzna ‘heel’, ete. Walde-P. 2.50f. Ernout-M. 757. REW 6418.
6433:7. Skt. stana-, Av. fstdna- (NPers. pistan) : Arm. stin ‘woman’s breast’, Grk. orfvov orf80s (4.40), perh. also OE spane, OPruss. spenis ‘teat’, etc., with orig. init. pst-. Walde-P. 2.663. Here also (or: Lat. pectus?) Toch. A passdém, B pdscane (dual)? Pedersen, Tocharisch 74, 75.
=== IEC Mann ===
13712:ptersna (persna) "bock heel, ham, ankle, leg-joint, lower leg'. WP II, 50
```


## [2026-09-14T00:57:56.438Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- HUB 1480-1495\"; sed -n '1480,1495p' HUB.txt; echo \"--- HUB 6590,6605\"; sed -n '6590,6605p' HUB.txt; echo \"--- HUB 7580,7595\"; sed -n '7580,7595p' HUB.txt; echo \"--- HUB 8605,8615\"; sed -n '8605,8615p' HUB.txt"
}
```


### [2026-09-14T00:57:56.547Z] TOOL RESULT

```
--- HUB 1480-1495
Neup. nur ^pana werden.— 44 —
341. Np. pahra = pas Nr. 274. Bal. pahar =^ afgh.
pahar, pahar 'Abschnitt von drei Stunden' aus dem
Sindhi.
342. Np. pahlu 'Seite' hat mit zd. pere&U" *breit*, skr.
prthivi nichts zu thun, sondern geht auf ein ap. *par&U'
aus iran. ^parsu- (skr. pargu- 'Rippe', zd. peresu-,
ZPGl. 10: paresU' -= phi. pahluk Rippe etc.) zuriick.
Die Dialektformen mit hi, I fiir rs (wie g. pahli 'Rippen'
ZDM6. 36, 37 etc.) sind aus dem Persischen ent-
lehnt.
343. Hier fehlen die n5tigsten Eriauterungen zu pahlav
(urspr. = Tarthien') und die Litteraturangaben. Ich
komme anderswo darauf zuriick.
345. Ap. patiy als 1. Glied von Comp. ist neup. zu paS
(vor Vocalen), pa (vor c, s, 5), pai (vor den ubrigen
--- HUB 6590,6605
2. fiir pers. h aus / in kohak *Woge, Berg' = phi. ko-
fak, np. koha (siehe § 80, a) ; kapkoh 'Kaukasus' (E 1 i s e)
d. i. kap'herg = mp. *kap'kdh fiir phi. kofikaf Bdh. 21, 2
V. u., np. koh i qaf?
Hier wurde h fiir / im Persischen schon gesprochen,
als die Armenier die Worter entlehnten.
') Vgl. zd. fsebls *mit Fesseln' zu skr. pag,
2) Wie aber verhalt sich np pistan 'Brust' zu zd. fstana-? Vgl.
oben p. 41. Etwa pistan (aus ^pdatdna-?) zu. fstana' (aus *pstana-)
wie zd. pitar- zu zd. ptar- ?— 187 -
b) durch v = u in den Verbindungen pers. aft^ ifU
afs, afs: tauf Ritze\ np. taft; »at?f *Erdharz\ np. naft; Khav-
far ein Orbelier (bei Vardan), np. kaftar *Hyane'; ^iwf 'Pech',
arab. pers. zift; drauS Tahne, Banner = np. dirafs, zd.
drafsa-) karatis, karos *Eppich', np. karafs; kausik, kdsik
'Schuh', np. kafsy bal. LW. kaus *Schuh'; ausarak (osarak)
--- HUB 7580,7595
a) gars *Haar (siehe oben p. 92 und 109) = phi. vars,
zd. varesa-; Pctrs =^ ap. Pdrsa-; gurs ^Hunger, gursina
hungrig* = ap. *vrsa', *vrsna' (neben gusna *hungrig*, von
tisna 'durstig beeinflusst, oben p. 92), dessen s freilich nicht
aus idg. k^ entstanden zu sein braucht. Np. Oarsdsp bei
Fird. ist aus ^Kirsasp = zd. keresaspa- entstellt.
b) iil = cihil Vierzig aus *^ihihl = "^cahihl = *cadf&
= ap. *da&vf&at' = zd. dadwar(e)sat'em, skr. datvarjgaU;
pahlu *Seite' = zd. peresu-^ paresu-^ skr. pargu-j ap. *pard^U',
Vgl. § 97: ap. rd- = np. hi
§ 104. Ap. 8 =^ iran. s, idg. sVh bleibt s im Np. :
sindsam 'kenne', pursam *frage*, tarsam *fiirchte mich*, rasam
'komme an', siehe oben § 98, d; pus^dan 'faulen von pU
(vgl. puda 'fauF); xusptdan *schlafen* (aus *xufsTdan); cas-
ptdan *kleben' = cafsidan; tafsldan u. s. w. (alles Inchoativ-
bildungen); gusistan 'zerbrechen =^ ap. *vi'si8tanaiy von
--- HUB 8605,8615
zd. xsmakem, Ueber pak^ bak u. s. w. siehe unten § 137, c.
2. Abweichend.
Die im Phi. in der Kegel neu entstandenen, leben-
digen Suffixe -afc, -ak, -ik, -uk, -ok sind (iiber ag, ag u. s. w.)
im Np. zu a, a, f, e*, 6 geworden :
a) handa *Sklave' = phi. bandak^ ap. bandaka- (mit
altererbtem Suffix ak = ap. a-ka) ; pasna *Ferse' = phi.
pasnak, zd. pasna-; dana 'Korn' = phi. danak (arab. danaj
und danaq H. 535, mand. ^CpJX'^ *obolus ) = zd. dana- *Korn ;
casma 'Quelle' von cas7n *Auge\; dasta *6riff* = phi. dastak
von dast *Hand' = ap. dasta- ^ u. s. w. (Vullers, Gram,
```


## [2026-09-14T00:57:59.384Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN Seite/Ferse/Brust ===\"; grep -n -i \"pahlū\\|pahluv\\|pahlü\\|Rippe\" HRN.txt | head -20; echo \"=== HRN pistan ===\"; grep -n \"pistän\\|pistän\\|pistān\\|pistan \" HRN.txt | head -10; echo \"=== IEC perk rib / psten ===\"; grep -n -i \"\\bpersu\\|parsu\\|pstēn\\|psten\\|stēnos\" IEC.txt | head -15"
}
```


### [2026-09-14T00:57:59.460Z] TOOL RESULT

```
=== HRN Seite/Ferse/Brust ===
3066:kurd. pist, zaza past; af/. pw5^ bezw. pt^j^^ 'Rippe';
3241:aw. pere&ii' 'breit'; phlv. pahlük hezw, pffhrük 'Seite';
3243:LW. bei. pahll 'Rippe (279); kurd. pal (H.-Sch.).
6581:Inf. Hüten, hafilznv (Oftusat.), g. lie.^(Ji(J (3. Sg.), sejeuph 'Tripper*.— 167 —
7475:dazu lat. c^ista *Rippe*, das Meringer, Sitzb. WAW. CXXV, *Beitr. z.
=== HRN pistan ===
3032:317. pistän 'Brust (der Frau)'.
3033:a.w./stana' *Brust'; phlv. p(i)stan (vd. 9 (71)), pistän
3035:LW. af/. pistän.
6472:743. seg *Hund'; vergl. arab. sij[ihistan d. i. np. seglpistän
13385:pistän 317.
19965:pistän 317.
=== IEC perk rib / psten ===
1204:bheidho (1) (bhindh-, bhidh-) ‘urge, per- suade, offer, promise'. WP II, 139. Cf. bheidh- above Gk. peítho, adj. pithanós; Lat. fido, Gre: Alb. cf. bind ‘persuade’; Ir. cf. béin (tcompulsion', fr. *bheidhnis)
1312:bhidh- “mind, purpose, intention, belief”. WP II, 139. Cf. bhoidh- Oss. bedun, pp. bidt “be evident, happen’; Gk. pithéo, pithanós; Alb. cf. bind ‘persuade’; Lat. fides, s., fidus, adj.; ON bió, n.pl. *wait- ing’; OFris. cf. bidia, OE -bidian, cpds. ‘wait’; MHG bit; bite ‘wait’. A form *bheidh- is im- plied in MHG biten *bide'. Go. bida “prayer”, though isophonic with the above, is ‘un- certain” for SE
7859:krentos ‘turned, bent; turn, bend’. Cf. kron- tos. WP I, 422 Ir. cf. creann-acht (‘skill ’, cf. G Gewandt-heit); Br. krenn ‘round, dumpy’; Cor. cren ‘round’; OCS cf. kretajo, -ati beside kreno, -noti ‘turn, deflect’; Pol. krety (o-gde ‘twisted, turned") beside (e-gde) krzątać się ‘be busy’; s-krzętny ‘busy’; Slovak na-kriatnuť ((tame; persuade’, lit. ‘turn’)
12743:perksKo, see prÉs-, preK-, prok- Umb. cf. persklum, n. ‘prayer’; Li. persu, piřšti, v. (“mediate between a prospective bride and groom’; refl. ‘woo, pester’)
15287:seu- (1) ‘start, move’. (Variants: sou-, su-). Cf. seuos (2) Skt. saumi, sávami, pp: sutáb, v. “drive, impel, move’; saváh, m. ‘starter, impulse’; variant: suvámi, v. “create, start"; Av. hunàmi, v. “bear — a child; prepare’; havohom, n. ‘preparation’; Arm. hav, u-st. 'beginning, origin'; Ukr. (ambig.) sovaty, inf. (thrust. Cz. souvat, id.). (Uncertain cognates are W hu, adj. “persua- sive; penetrative; bold? and huan, f. ‘sun’, cf. Skt. saváh, m. ‘sun’).
16799:spenis, ios ‘nipple, breast’. Cf. psten-, spen- do. WP II, 663 Olr. sine, cpds: -phne, id.; MIr. sin, sine; Ir. sine, pl. sinidhe, id.; MHG spen, sf. *breast; mother's milk'; Fris. spien, n. “nipple'; Du. speen, f. id.; ON speni, m. id.; Sw. spene, m. "breast, udder’; Li. spenys, io, m. ‘nipple’; OPr. spenis, id. O-gde in OE span, spane, f. id. and z-gde in OHG spunne, i-st. mpl. ‘breasts’; MHG spünne, id. and spune, spüne, sf. n. id.
17196:(stenos, à, Skt. variant of type psten-, q. v. in Skt. stánab, à, 1h, mf. *breast; (LW in) Arm. stin, id.)
17526:sthàn- (stháno; sthànos) ‘stand, set, set up, fix; standing, station, place. Cf. WP II, 606 and sthā- with extns. Verbal types: Gk. cf. histáno, v. get beside mod. sténo, v. ‘set up”; cf. -staino in kru-staíno, v. ‘turn to ice’; Lat. cf. de-stino, are ‘fix’; ob-stino, are ‘persist’; prae-stino, are ‘buy up’ (but for festino, festinus see below tuerst-); Ir. stă- naim, stán-, v. ‘stare’; W sanu, inf. ‘gaze; amaze’; cf. san, adj. ‘wide-eyed; amazed’; OCS stanọ, inf; stati & stanọti, v. stand’ and com. S1.). Nominal types: Skt. sthānam, n. “stand, station’; Av. stānō, m. ‘place, stable’; OPer. stānam, n. id.; Per. -stān, cpds. id.; Gk. cf. dústēnos, Doric: -stānos, adj. “in a bad state’; Hes. cf. bou-stáne, f. ‘cowstalľ; Oss. äston, ston, s. ‘stall, cowshed’; Tokh. A cf. stank, B: stank, s. ‘palace’; Alb. shtonë, f. “water- hole, catchment’; Ir. stán, m. “vat, barrel’; Du. steun, m. (umlaut) ‘support’; OCS stanü, m. ‘stand, camp’; Ukr. ‘state, condition’; Li. stónas, m. ‘rank, status’; stóne, f. ‘stable, stall’
17880:suádó, eio “make sweet; be sweet’. See next Skt. svade, mp. ‘taste well: svattáh, adj. ‘spiced’; Gk. hédó, v. ‘sweeten, delight’; hédo- mai, mp. (/rejoice. Boeotian: wà-); Lat. suadeo, ere, v. *persuade, advise'; OE swetan, v. ‘sweeter’ beside swetian ‘be sweet
```


## [2026-09-14T00:58:09.065Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- HRN 3230-3250\"; sed -n '3228,3250p' HRN.txt; echo \"--- HRN pasna\"; grep -n \"päsna\\|pasna\\|päsne\\|Ferse\" HRN.txt | head -10"
}
```


### [2026-09-14T00:58:09.123Z] TOOL RESULT

```
--- HRN 3230-3250
Vergl. Seil rader, Sprachvergl. und Urgesch.^ 287,
Miklosich, Fremdwort. 8, Hübschmann, Etymol.
u. Lautl. d. osset. Spr. 121. Fr. Müller hält (WZKM.
5, 186) np. püläd für ein griechisches Lehnwort (etwa
no'Kvnava^) ; ganz unsicher.
341. pehre *Wache\
aw. i)ädra' 'Schutz'; ai. pätra- (unsicher; ein Mal),
arm. LW. paliak (cpQovgu)^ vergl. paA, pahapan etc.,
fara\parhaJc (de Lagarde, No. 2203).
LW. af/. pahra, pahar; bei. pahar, pahrä (193).
342. 2>ehlü 'Seite'; Stadt' (Sahn. 1, 104 Vers 793, 105
Vers 804), arab. LW. fahla 'Stadt*.
mäz. päll; gel. pälü.
aw. pere&ii' 'breit'; phlv. pahlük hezw, pffhrük 'Seite';
ai. vergl. pfthm- 'Erde'.
LW. bei. pahll 'Rippe (279); kurd. pal (H.-Sch.).
Mit aw. peresH' 'Kippe, Seite\ ai. pärgcd-, kurd.
pärsü, wa/. pürs, kurm. parsü, oss. fars 'Seite, Strich,
Gegend' (278) lässt sich np. pehlü lautlich nicht direkt
zusammenstellen.
343. peJilev, pehletan 'Held'^).
ap. Parfhava-; phlv. pahlav (gehört etwa auch
pahlum hierher?).
--- HRN pasna
2728:276. päSne 'Ferse'.
2729:aw. päsna- 'Ferse'; phlv. päsnak*^ ai. pdrsni-,
2732:päsna, sar. pu/nä 'Ferse'.
2734:sich im Bade die Fersen reibt', de Lagarde, Ges.
11370:Ein np. serjeng 'Ferse*, das de Lagarde auch
```


## [2026-09-14T00:58:10.480Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC psten ===\"; grep -n \"psten\" IEC.txt | head -10; echo \"=== IEC perk rib ===\"; grep -n -i \"perKus\\|perKu\\|'rib'\" IEC.txt | head -15"
}
```


### [2026-09-14T00:58:10.550Z] TOOL RESULT

```
=== IEC psten ===
16799:spenis, ios ‘nipple, breast’. Cf. psten-, spen- do. WP II, 663 Olr. sine, cpds: -phne, id.; MIr. sin, sine; Ir. sine, pl. sinidhe, id.; MHG spen, sf. *breast; mother's milk'; Fris. spien, n. “nipple'; Du. speen, f. id.; ON speni, m. id.; Sw. spene, m. "breast, udder’; Li. spenys, io, m. ‘nipple’; OPr. spenis, id. O-gde in OE span, spane, f. id. and z-gde in OHG spunne, i-st. mpl. ‘breasts’; MHG spünne, id. and spune, spüne, sf. n. id.
17196:(stenos, à, Skt. variant of type psten-, q. v. in Skt. stánab, à, 1h, mf. *breast; (LW in) Arm. stin, id.)
=== IEC perk rib ===
12747:perKus, uos (prku-) ‘side, bosom, soul, heart, life’. (Semantics obscure). WP II, 44. Skt. cf. par$vya, dual n. “heaven & earth’; pārśvam, n. “side? and pársuh, f. ‘rib’; Av. (z- gde) porosus, m. ‘rib, side’; Oss. fars, s. ‘side, rib, wall: cf. also fársmá' ‘sideways’; färsäi “on one side”, färsón, s. ‘side, flank, bosom’; Go. fairhwus, m. ‘world’; Crim. Gothic fers, m. (mar, lit. sou); OS firihos, mpl. ‘men’; OHG firah-, id.; OE feorh, m. “life, soul; MHG vërch, gs: vérhes, sn. id.; adj. ‘vital; cf. also OE feorm, f. (“food', if for *perKm-). Z-gde in Alb. preh, usu. prehén, T prehër, m. (bosom, fr. *prKu-); OCS prüsi, fpl. ‘breasts’; Cz. prsa, n. dual ‘chest, breast’; Li. pirSys, gpl: -iu, f. “breast of horse’. Cf. ON fjor, ds: fjorvi ‘life’ beside firar, pl. “people?
12751:perkus, uos (prKu-) — péros, à, om (peior-?)
13380:pork- (porKs-) (?) ‘surrounding, edge, rim’. Cf. perkus & WP II, 45 Ober. parsa- ‘court’; Gk. pórkes, m. “loop, ring, snath’; Lat. porca, f. (fridge, baulk’, but cf. porKos ‘pig’ and semantic note); W cf. variant: orch, pl. -au, f. ‘border, limit’
13661:prK- (proK-) (4) ‘breast, front". Cf. perKus OBr. cf. rac, prp. ‘before’; W rhag, id. (fr. *proK-); Cz. prsa, pl. “breast, bosom’; R pérsi, fpl. id.; Li. pir$ys, fpl. “breast of horse
13680:prquð (1) “touch, hit, meet, join’. Cf. perquo & prequo Skt. cf. pricami, pi-prCami E prnákmi, pp: prktáb “make touch; join, mix’ cf. also prktih, f. ‘contact’; Alb. cf. prek, v. id. (fr. *prequo or *prqu-. See Mann: Alb. Hist. Gr. pp. 159 & 167) beside pérkás, id. (Mann: p. 181); Gk. cf. (e-gde) prépo, v. ‘resemble; beseem, suit, fit; Cor. cf. ryp, prep. «touching, alongside’; Srb. cf. prk, m. ‘obstinacy’; u-prk, prp. 'de- spite’; Li. perku, inf. pifkti, v. ‘buy’; pilkis, gs. io, m. “purchase; Latv. pérku, pirkt, v. as Li.
```


## [2026-09-14T00:58:30.084Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13705,13720p' IEC.txt; echo \"--- around 17190-17200\"; sed -n '17190,17200p' IEC.txt; echo \"=== ARY files ===\"; ls incoming/ARY 2>/dev/null | head; ls | grep -i ary"
}
```


### [2026-09-14T00:58:30.185Z] TOOL RESULT

```
1005
Li. spenys, see spen-. (Alb. ftujak, m. ‘kid’, if for *ftuejak may represent a type *psténjak-. The initial may be represented also in the synth. Gk. cpds. stéthos, stérnon & Dor. stét&)
pstreuó (pstruió) ‘sneeze’. Onomat. Cf. WP II, 101 Gk. cf. ptaíro beside ptárnumai, id.; W ystre- wu, Cor. strewy, Br. stréfia & strévia, striuein, inf. id.; MIr. cf. sren, s. ‘wheeze, snore’. The vocalism of Lat. sternuo, ére, id. is obscure
pstuio (pstiuio, psth-) ‘spit’. Cf. spuuo, ið. Onomat. WP II, 683 Skt. sthivami, pp: sthyütah, id.; Hind. cf. thuk, s. id.; Per. tuff, s. id.; Oss. tü, s. id.; Arm. t'uK, gs: tko, o-st. id.; t'Knem, v. id.; Gk. ptáo, v. id.; Alb. pshtyj, v. id.; Br. cf. tufa, v. id.
ptā-, extended z-gde of type pet- (2), peto, q. v. Cf. WP II, 19 Per. cf. futadan, inf. ‘fal’; Gk. cf. ptémai, v. ‘flake down, fall”; cf. ptenós, (Doric: -à-), adj. ‘winged’; ptená, npl. ‘birdlife’
pteleuå (peleua) "a tree’. Phonol. and back- ground uncertain. Cf. WP II, 84 (Oss. färwe ‘alder’; OHG felawa, felwa, f. “wil- low; G cf. Felber, f. and Felbinger, m. id. for the form *peleua, and cf. peluà above); Myc. ptereu- for pteleu-: Gk. pteléa, f. ‘elm’; LW in Arm. t'eyi, id.
pterom, is (variant of type petor-, petno-, q. v.) ‘wing, flap, side, blade, leaf. WP II 21 & 39 Skt. cf. pataráh, adj. ‘flying’; pát(a)tram, n. ‘wing, feather, leaf; Av. cf. patarom, n. ‘wing’ beside fra-ptoro-jat, pp. ‘winged’; Per. par, s. “feather”; parra, s. ‘side’; Arm. Ver, gs: -i, i- st. ‘side’; 'era-, cpd. forms ‘half-’; cf. also t'ert', i-st. (-leaf, petal, scale, sheet, fr. a type *ptetri- with assimilation of *-t-); (long-gde in) tif, gs: tri, ab. s. triv, s. (flight, wings’, fr. *ptetri-); Gk. pterón, n. “wing, oar, side wall, partition’; ptéris, f. ‘fern’; Alb. fier, m. ‘fern’; W cf. adar, s. coll. (birds', fr. *petro, w. assimilated vo- wels). (Of uncertain composition are Arm. t'i- t'ern, gs: t'itran ‘butterfly’, fr. (?) *pte-ptér-; & Hitt. partawar, gs: partaunas, s. *wing")
ptersna (persna) "bock heel, ham, ankle, leg-joint, lower leg'. WP II, 50
pstreuó (pstruio) — pü£os, à, io
20
25
30
35
40
45
1006
--- around 17190-17200
stenguo (sth-) ‘thrust, push, press, jostle’. Cf. stembo. (Gk. ambig.). WP II, 613 Gk. (ambig.) stémbo, v. ((trample; buffet, browbeat’, but cf. stemb-); Lat. cf. ex-stinguo, ére, v. beside OLat. stingo & stinguo 'extin- guish"; Go. stigqan, sv. 3. “butt, press, push’; ON stókkva, sv. 4, 3s: stekk, v. “jump; bounce; flee’; mod. ‘dispatch; sprinkle’; Li. (ambig.) sténgiu, ti, v., refl: sténgtis 'strive; resist; avail
stend, ið (ston-) ‘groan, moan’. WP II, 626 Skt. stánami, v. ‘roar, bellow’; Arm. cf. Vind arnum, v. ‘resound’; t'ndam, v. denom. (vari- ant: t'ntam), id.; Ck. sténo, v. ‘groan’; (o-gde in) MHG stenen, OE stenan, Du. stenen, v. ‘moan, lament; OCS stenjo, stenati (and com. SLL id.; Li. stenü, čti, v. ‘roar, groan’; Latv. stenu, t, id. Cf. Fris. stinne, v. (1), as Du. (: Arm. t'ndam ?)
stenos (stenios, stentós) (1) “narrow, close” Gk. stenós, steinós, id.; steinos, n. ‘strait’; Fris. cf. stinne, v. (3) ‘squeeze, press’ beside stith, adj. “harsh”; OE stió, adj. “hard, harsh’;
1285
ON stinnr, adj. ‘stiff, strong’; Sw. stind, adj. ‘stiff, crammed, bursting’
stenos (2) ‘groan, moan’. Cf. stend, stonos. WP II, 626 Gk. sténos, gs. -eos, n. id.; OE sten, n. id.; (o-gde in) OCS *stonü, m. id. and Gk. stónos, m. id.; Cz. ston, m. id. (OCS cf. stonava, id. stonati, v. id.); Sw. cf. stánka, v. “moan, pant’: OE stencan (2), id., fr. *ston-ago via *stong-)
(stenos, à, Skt. variant of type psten-, q. v. in Skt. stánab, à, 1h, mf. *breast; (LW in) Arm. stin, id.)
stepti-, variant of type septm (and *se- qudm-?) in W saith ‘seven’; Br. seiz, d: Alb. shtatë, id.; Olr. cf. secht, id. (fr. *sequt- ?)
ster-, e-gde of radical str-, q. v. Cf. also stor- *strew, spread”, etc. WP II, 640 Skt. stare, mp. ‘strew’; pp: strtáb; Av. star-, id.; Per. cf. gu-stardan, inf. id.; gu-star, s. ‘spreader (fr. *aue-^); Lat. cf. sterno, Ere, v. id.; cf. ster-cus & -cor, -quilinium, n. ‘dung’; Srb. stérem, stérati, v. ‘stretch’; cf. OIr. sernaim, v. 'strew'. (In the sense of “side”, a possible formant in Gk. ari-sterós, Lat. sini-ster, OHG, OE winister, win-ster, etc.)
stergsos, à “shelter, protection'; *stergo, ra- dical e-gde type present only in Slavonic. (O-gde variant: *storgs-) Oir. serc, f., Ir. searc, mf. ‘love’, W serch, m. id.; serchu, inf. id.: Cor. sergh, m. ‘fond- ness’; Br. serch, mf. ‘concubine’; OCS strěxa, f. "roof besides (o-gde, and com. Sl.) straža, f. ‘guard’; Srb. stráZa, id.; R stràža, f. (OCS style) beside o-storðZnyj, adj. “careful'; cf. straxovát, v. ‘insure’ (fr. *storgs-)
sterá- (storg-, střĝ-) “lack, fail, collapse; failure, ruin". Cf. WP II, 642 Gk. stérgo, v. ‘want, lack, accede to’; Ir. (ambig.) (?) searg, adj. (decayed, shrivelled', but see serguh-); seirg, adj. ‘parched’; sear- gaim, v. ‘shrivel, decay’; MLG stérke, stirke, wf. ‘heifer’; OE stirc, Scots stirk, id.; Cz. cf. střízlý, adj. ‘stunted, puny’; (o-gde in) Hitt. stark-, v. “be ill; Gk. storgé, f. ‘love’; Cz. strázeň, f. ‘pathos’; (z-gde in) Lat. strages, f. ‘overthrow’, fr. *str&-; Go. ga-staürknan, v.
=== ARY files ===
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
NYB_vol2_glossary.txt
```


## [2026-09-14T00:58:36.761Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13690,13707p' IEC.txt | cut -c1-1500"
}
```


### [2026-09-14T00:58:36.808Z] TOOL RESULT

```
prt- (prtos, à, is, us) (1) “passage, crossing, way, ford, shallow’. Cf. port- (1). WP II, 40 Av. porotus, f. ‘bridge’; Per. pul, id.; Lat. por- tus, gs: -üs, m. ‘port? beside porta, f. ‘gate, entrance'; Gaul. -ritum, -ritu-, in cpds.; OW and OCor. rid, W rhyd, pl. au, -iau, f. ‘ford’; Cor. res, pl. rezyow, id. OBr. rit, id.; OHG (and com. Gmc.) furt, m. ‘ford’; OE ford, m. id. beside M. Eng. forth, s. (course; ford’. Langland); Slovak prt, f. ‘woodland track’;
prs- — psténos, ios, iom
20
25
30
35
40
45
1004
Cz. ^sheep-track'; Srb. prt, m. ‘track through snow’; OCS pa-prütí and pri-prütü, m. vest, bule? (final vowel uncertain); cf. Blg. prátja, Srb. prtiti, v. ‘blaze a trail’. Long-gde variant prob. in W rhawd, pl. au, f. ‘course, route’; rhawden, pl. au. f. ‘footstep, path” (if fr. *prt-)
prt- (2) ‘beating, battle, shattering, ruin’. Cf. perið (2), (poros) Skt. prt, f. id.; Av. porot-, v. ‘fight’; Ober cf. (e- or o-gde) partara- ‘battle’; OCz. cf. za-prtiti, inf. 'spoiP: R port, inf. id.; Blg. prátja, v. id..; Ukr. cf. partac, m. (Cbungler', fr. Pol.?); Big. cf. prátina, f. ‘spoil of war’; Li. pirtis, gs: -iés, f. (3) 'beating-floor for flax’
prt- (3) (prtos, om, io) “piece, patch" Per. pül, s. ‘money’; Gk. prasía, f. 'garden- plot; Lat. pratum, n. ‘meadow’; OCS prütü, m. ‘rag’; OR port, m. ‘garment’; Slovene prt, m. ‘sheet’; Lusat. cf. porémo, n. ‘lap of coat’; R cf. portnój ‘tailor’; Cz. cf. prták, m. ‘cobbler’; prtati, inf. ‘mend — shoes’. (Skt. patih, f. “strip of cloth’, hence E ‘puttee’, is ambig. cf. pelt-)
prthus ‘broad’ (?) Cf. plithus. (The Indo- Iranian forms are ambig.). WP II, 99 Skt. (ambig.) prthuh, adj. (broad, big; abun- dant, smart; fr. *plth-?); Av. poro0us, adj. (broad', ambig. as Skt.); Per. cf. pahlü, s. ‘side’; Arm. bart, adj. (flat, level. Ambig. cf. prosthos above); Icel. cf. furóu-, px. (/very-^; but furða, f. = *wonder); R cf. portki, pl. (*knickers', but cf. prt- (3) above)
pruos “first, foremost’. WP II, 38 Skt. pürvah, adj. “front; eastern; former, prior’; Av. paurvó, paourvo & paourvyo, adj. “former, earlier; first; Ober, parüva- ‘earlier’; Tokh. A cf. párwat, B párwe, adj. ‘first’; cf. B y-parwe “at first’; Alb. i parë, adi (first; ar from loss of final cons. as valë *wave"); Sequanian priou- in priou-dixivos (if = Skt. pürva-daksinah *south-eastern?); OCS prüvü (and com. SL), adj. “first”; R pérvyj, id.; cf. also OCS priprüvü, adj. “ready, to hand"
psténos, ios, iom *nipple, breast'. Cf. spén-. Onomat. Skt. cf. stánab, m., stana, stanib, f. id.; Av. fstana, dual. id.; Per. pistan, id.; Oss. fázdon ‘udder’; Arm. stin, gs: stean ‘breast’; Tokh. A påssån, B päşcane, id.; Hes. stënion, id. For
1005
Li. spenys, see spen-. (Alb. ftujak, m. ‘kid’, if for *ftuejak may represent a type *psténjak-. The initial may be represented also in the synth. Gk. cpds. stéthos, stérnon & Dor. stét&)
pstreuó (pstruió) ‘sneeze’. Onomat. Cf. WP II, 101 Gk. cf. ptaíro beside ptárnumai, id.; W ystre- wu, Cor. strewy, Br. stréfia & strévia, striuein, inf. id.; MIr. cf. sren, s. ‘wheeze, snore’. The vocalism of Lat. sternuo, ére, id. is obscure
```


## [2026-09-14T00:58:38.439Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor w in ['پهلو','پاشنه','پستان']:\n    print('=====',w)\n    for i,p in enumerate(pages):\n        if w in p: print(' leaf',i, p.strip().replace('\\n',' | ')[:300])\nEOF"
}
```


### [2026-09-14T00:58:39.614Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'ARY_pages.txt'
```


## [2026-09-14T00:58:48.392Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('pages',len(pages))\nfor w in ['پهلو','پاشنه','پستان']:\n    print('=====',w)\n    for i,p in enumerate(pages):\n        if w in p: print(' leaf',i,'|', ' '.join(p.split())[:400])\nEOF"
}
```


### [2026-09-14T00:58:49.476Z] TOOL RESULT

```
<persisted-output>
Output too large (139.7KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bqsb19nci.txt

Preview (first 2KB):
pages 545
===== پهلو
 leaf 1 | [pdf page 2] نج ۰ ۰ پیشگفتار ۳ پیش گفتار هدف این کتاب نشان دادن ریشه‌ی هند و اروپایی واژه‌های فارسی ناب است. این هدف موجب ۳۳۱ سس ویژگی‌های زیر شده است: ۱- هیچ واژه‌ی فارسی که ریشه‌ی هند و اروپایی آن ناشناخته است آورده نشده است. صدها واژه‌ی فارسی وجود دارد که ریشه‌پابی آنها تا حد پهلوی و اوستایی و حتی پارسی‌باستان پیگیری شده است ولی ریشه‌ی هند و اروپایی آنها شناخته نیست. ممکن است برخی از آنها هند و
 leaf 9 | [pdf page 10] دیباچه / ۱۱ تردید قرار می‌دهد این است: زبان هند و اروپایی تخاری (10077۸131۸31) که در ترکستان چین " یعنی در خاوری‌ترین سرحد زبانهای هند و اروپایی قرار داشت. یک زبان ستتم پود! آپا آنها از اروپا به‌جلگه‌ی تارم (باختر چین) کوج کردند و علت شباهت زبان آنها با یونانی و سلتی همین است؛ آیا به همین علت است که نقش‌های دیواری یافت شده در تورفان و تارم آنها را با موی سرخ و چشمان آبی و پوست سفید ت
 leaf 21 | [pdf page 22] ۰ ۱ ا :ْ دیباچه / ۲۳ اروپایی نشان می‌دهد که در سانسکریت 0" تبدیل به **شده است. لذا واژه‌ی پنیادین هند و اروپایی که همه‌ی این واژه‌ها از آن مشق شده‌اند محتمالً *4 بوده است. (امروز معتقدند که اين واژه‌های بنیادین *۸0۸05" بوده است). طی صد سال گذشته بازسازی واژه‌های بنیادین هند و" اروپایی پیشرفت بسیاری کرده است و دانشمندان ریشه مشترکك اکثر واژه‌های هند و آروپایی را (از ۱ طریق پیگیری پسگر
 leaf 26 | [pdf page 27] ۸ / ریشه‌های هندو اروپایی زبان فارسی نزدبکك واژگان گانها با واژگان کناب هندوان (ودا ۷80۸5) نیز می‌تواند حا کی از این باشد که اقوام هندی و ایرانی در فاصله زمانی کمی از یکدیگر از خاستگاه هند و اروپائیان به سوی جنوب کوج کردند. (192:4 ,883۳80) بخش‌های دیگر اوستا در سده‌های بعدی نگاشته شده‌اند. رویهم رفته اوستای اپرانیان و ودای ِ هندیان؛ باستانی ترین نوشتارهای هند و اروپایی بوده و پل مهمی
...
</persisted-output>
```


## [2026-09-14T00:58:55.053Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor w in ['پهلو','پاشنه','پستان']:\n    print('=====',w)\n    for i,p in enumerate(pages):\n        for line in p.split('\\n'):\n            s=line.strip()\n            if s.startswith(w) or re.match(r'^[٠-٩۰-۹\\s\\-–]*'+w+r'\\s*[:،.]', s):\n                print(' leaf',i,'|',' '.join(line.split())[:350])\nEOF"
}
```


### [2026-09-14T00:58:56.267Z] TOOL RESULT

```
===== پهلو
 leaf 49 | پهلوی (۲هاتلهه): 17 باانتا۸7 پسگشت‌ها دای اد ادن ای
 leaf 50 | پهلوی (۷هاتل۸ط): ۸1 پسگشت‌ها لامش اد ادن
 leaf 50 | پهلوی (۷7هالل۲۸): ۸ آلمانی (057/۸0): نراد با
 leaf 52 | پهلوی (1الل۳۸): ۸۳۸ روسی (/75514): 1.007
 leaf 61 | پهلو ی (۵7آل(۸ط). ۸۹۸۵۲ لهستانی (۳۵/3[4). ۱:۱
 leaf 65 | پهلوی (2:]4۲ :۸0۸30۸7216۸10۸7۷ ,7 مفان6۸ 00۳57578
 leaf 65 | پهلوی (4۲اتل۳۸): آل262 بققلة
 leaf 66 | پهلوی (۲ماتقهه): 3 ار قته9
 leaf 72 | پهلوی (1اتز۸): : پسگشت‌ها 5
 leaf 72 | پهلوی ‏ (/مالطهه): ,۸138 7 ار و ی (02501: 17
 leaf 73 | پهلوی: (۳۸(74): , ۸ 1 ,8102۲
 leaf 75 | پهلوی (۷1ماتزم۳). ,86 سرئدی (8775213/7): ندید نالدرا
 leaf 77 | پهلوی (۲1مالزهه): ۸7۸ نروژی (07۷201۸/: 102
 leaf 77 | پهلوی (4/1ال۸): زی ان سانسکریت (6۸۸/367/7: بقکلهه مق
 leaf 80 | پهلوی ۸۲۷1 ۸): ۸۸ ۸
 leaf 86 | پهلوی (۲1مالظه‌ه): :6 ,آک۸8 اسلراکی 5101۸0): ان
 leaf 87 | پهلوی (1اتلهه): 3 دا ان
 leaf 89 | پهلوی (۸(71471): با نان روسی (/785142): 1
 leaf 93 | پهلوی (۸۷/1ائلهغ): لانراننا دانمارکی (18[4(م0): ۸
 leaf 94 | پهلوی (2۸(1۲1): 09,30 08 ب۸۷۳ لهستانی (۳0.187): 0۸ ,0
 leaf 97 | پهلوی (1اتلمم): 0۸0 پسگشت‌ها شرت دی
 leaf 104 | پهلوی (1اللهه): ه3 ,81706
 leaf 104 | پهلوی (۲1اتلم۳). 1 ,۷۸7 فریزی کهن (للفاکلا۲ ۰:02 ۰ ۷۲8۷۸
 leaf 105 | پهلوی (۷1هاتزهه): 8112۸6۸ 1 11 0001 ۳ ۳
 leaf 106 | پهلوی (1الله۳): هلم8 بقلة8 ۰ نروژی (۷اها۵ ۸07۳+ 6
 leaf 107 | پهلوی (41اتل۸): 20 ‎ -‏ نورس کهن (۱۷0788 010):
 leaf 110 | پهلوی (۲7مالز۸): ,3۸8۸6 ,8۸78۸ ( ز لن ۱
 leaf 112 | پهلوی (۷1هابل#ه): .3 پسگشت‌ها ۱۱5
 leaf 113 | پهلوی (۳۸14۲7): ۷۸۳7۸۹ ,۷۸ ,۷۷۸ پسگشت‌ها 5
 leaf 114 | پهلوی (۲1الل۸ط): 8۸ روسی ((994لا): زی اه اه ۱
 leaf 115 | پهلوی (1هالله۳۸): با8۸ انگلیسی کهن (0ا5لا5۸0 2: ,8187135
 leaf 120 | پهلوی (7شات۳۸): 202 انگلیسی (57با8/0): 16
 leaf 121 | پهلو ی*(1ماَمع): ظ ۰ ۷۹
 leaf 122 | پهلوی (17الل۳۸): ۸6 ,۷/۸۸6 دآنمارکی (0۸۷1574): 0اآ8
 leaf 124 | پهلوی (۸۲۷1ال۳۸): امانلی ۱1۱ لیتوانی (0۸(/4/۷ 0/777 ,کشم8530۷1
 leaf 130 | پهلوی (4۷7آلل2۸): زر ۱۱1۱8
 leaf 132 | پهلوی (1ماللم): 7 ,817۳۸۵ انگلیسی کین (لاخلاه2 هزم ,850
 leaf 135 | پهلوی (۸]۸۲7): 21 1 (310شآ),20 راد ها
 leaf 135 | پهلوی (۲1اتل۸ه): ,9 ,)30910۸ آترنی (لنی) (47740۷ا): 3۸1818 بشلاتا8۸
 leaf 138 | پهلوی (1/اتقهه): کفتا8 اق۸ ,25
 leaf 141 | پهلوی (/ا3ل۸): 7 ,۷۷181 انگلیسی کهن (8:0/37 ۵۵): 1۷78۸۲۲16 :
 leaf 148 | پهلوی (1/ماتله۳): 6 ۴28۸6 ایتالبایی (۷لمللم7): ۳۸371886 ,8۸37
 leaf 151 | پهلوی (۳۸414۲7): 7۸171۸۸ ,8.11۸34 انگلیسی (8/0/58)(از فرانسه): ۴25
 leaf 154 | پهلوی (۲1ماتام۳۸): + ,820۸ اسلاوی کهن (0//ابماک ۲71086 010)(شاید)
 leaf 156 | پهلوی (1ا7ل۳۸): نورس کهن (۸0785 0): را ابا
 leaf 160 | پهلوی (17ل(۸): نروژی (۸/07/801): ند
 leaf 165 | پهلوی (1ماتلهه): ,8۸8 آلبانی (0هفانمقتم: 2۸8
 leaf 166 | پهلوی (امریزهم: ۳۳۵720 ,۲/8720 دوم "۱"
 leaf 169 | پهلوی (4ات۳۸): 1 هلندی (ع076ه): ۷7
 leaf 169 | پهلوی (1شایل۸): ۰" یا :۱:۱۹ گوتیکه (0077710): 710
 leaf 171 | پهلوی (1/ماتلهه): 8 ,ال81 پرتغالی (۳017001832): ۰ 207
 leaf 172 | پهلوی (//۳۸]۸): 2۸7 ایلندی کهن (۷(م 2۸ید صام):
 leaf 175 | پهلوی (1/ ۸1 ): رل ۱۱ لاتین (710ا): ۳05 205
 leaf 178 | پهلوی (/ا/ل۳۸): ,۶11817۸۷ ,۶107۸86 آلمانی (0880/4۷): ت7۸
 leaf 181 | پهلوی (47/7ال۸): اد هیت (07777172: 2۸
 leaf 184 | پهلوی (ماقلهه): 1 سرئدی (5۲780/37): لاین ۱
 leaf 185 | پهلو: ی (ماتلوه: ۰ اسلاوی کهن (۲/2شا5 207 صت0):
 leaf 189 | پهلوی (۲1اللمه): پسگشت‌ها رد رد۳۹۱
 leaf 189 | پهلوی (7ماتقهه): ب۸3 م777۸ سانسکریت (8۸4۸/87077):
 leaf 191 | پهلوی (۷1ال2۸): 7 بال7۸ ایرلندی کهن (لکل#ا صا0):
 leaf 194 | پهلوی (۲اماللمم): 6ها7۸23 بش7۸ دانمارکی (0۸(/784): ۹ 07
 leaf 195 | پهلوی (11ماتتم۳): لاد وا و ای (۸) ۷۰
 leaf 196 | پهلوی (۷1اتلم۸): 86 ,718 ۷ ,85۳1۷۷۸
 leaf 197 | پهلوی (47الل۳۸): انگلیسی (4لولا8۸/0): 710
 leaf 199 | پهلوی (۲ماتنمه): 71۸ پسگشت‌ها آشت رد دا
 leaf 201 | پهلوی (4۷7]لل2۸): زان سانسکریت (54۸/58/7): 3۸37۳ ,۳۸۲۸7
 leaf 202 | پهلوی (۲1هاتلمم): 7۸ لیترانی (الفاللهلاتز تم 1۸0۸8 ,۳۳۲۶
 leaf 203 | پهلوی (۳۸(1]4/1): 70 دانمارکی (0۸15/7): 0
 leaf 204 | پهلوی (1/ه1ل۸2م): اسلراکی (5-0744/0): 100306 ,1829
 leaf 205 | پهلوی (4۲1اللهه): 7100 یونانی (07882): ۰ 78833085 ,7۸2301
 leaf 209 | پهلوی (1ها3ل۳۸): 788۸ لهستانی (۳0/57)(شاید) مدا ادا ۱
 leaf 209 | پهلوی (1مابلمه): 0۸ ,6۸0
 leaf 211 | پهلوی راام‌برمم: تْ. فلال ,۸0۸8 لانین (0امم: 75860878 ,1800
 leaf 217 | پهلوی (امنتنمم: #هاتفتل تفای 1 1
 leaf 219 | پهلوی (1اماتله): ی ۹ اسلاوی کهن (16/ما5 بل#ناتل) صا0):
 leaf 224 | پهلوی (۸7]41): ناه اه
 leaf 225 | پهلوی (1/(ملتل۸): 6 نروژی (۷لفا۵/0850: ۰ 115۸
 leaf 230 | پهلوی (امابلهط): 3۸81987 ب7۵8 ابرلندی کهن (54ل12 0ا0): ققدع
 leaf 235 | پهلوی (/ا(۸): 3 نا ۱۹ اپرلندی میانه (3/#ا 041026 تیه
 leaf 236 | پهلوی (41اتل۸ه): 205 لیتوانی (14(۷/لهلا27 7 85قاتاتاه۶ ۴
 leaf 237 | پهلوی (۲7اللهه): 207۸0 روسی (551۸24(ا#): ۸7
 leaf 242 | پهلوی (1شالق۸ه). ولزی (لاکا75(): لری ۱1۹۳۹
 leaf 243 | پهلوی (۷7الل۸): برتونی (/8870): نا
 leaf 247 | پهلوی (۳۸/]۸4/1): اوستی (08587/6): ,20072
 leaf 252 | پهلوی (1ماتلمط): آلمانی کهن (057/۸0 01ابز صزه):
 leaf 255 | پهلوی (47اتل2۸): آلمانی کهن ((8721۸ ۷0۵۶7 صا0):
 leaf 257 | پهلوی (اللمالله): ۱ برهمی (80[78(41۸7): 271
 leaf 259 | پهلوی (41اتقهه): کة0
 leaf 261 | پهلوی (7/1الل۳۸): 3 دانمارکی (0۸/784): 1۸۵
 leaf 269 | پهلوی (7اتلهه): 2 سانسکریت (84(78۹7077): 12۸77
 leaf 276 | پهلوی (1/الاوه): 217 سوئدی (5175015). 26
 leaf 277 | پهلوی (۳۸7]۷1): لهستانی (ل57/ا۳0): ی
 leaf 280 | پهلوی (1ماظ۳۸): 2۸/7870 ,0۸3 آلمانی کهن (/۸/ل087 ۲/04 صا0):
 leaf 281 | پهلوی (477تینم2۸): 2۸77۸۲ ,2۸3110۸۲ دانمارکی (0۸/877): 016
 leaf 282 | پهلوی (۲1شاللهه): ۸۷ ,02 انگلیسی (50لا6(/0): ۳1007
 leaf 285 | پهلوی (1 ۸314 ): 3 رومانی (4۸(/۸انا): 118۸
 leaf 286 | پهلوی (۷/1اللمه): انگلیسی کهن (ل8/ا8۸6 ط1). ۸0و50
 leaf 287 | پهلوی (1/اماللم۳): کردی (801377():
 leaf 292 | پهلوی (1الل۸): 0/1 بلوچی (للللاءله8): 4 با
 leaf 294 | پهلوی (۲1ماتلهمم: (6۸8) ۸۸۷05/201 پسگشت‌ها 5
 leaf 295 | پهلوی (۲7ماللهه): 3 در بوهمی (80/78141421): 20
 leaf 297 | پهلوی (۲7مائغم۳): لا انگلیسی (6۸01/54)(شاید) دا
 leaf 298 | پهلوی (۸47ا(۳۸): م7 8۸0
 leaf 299 | پهلوی (477آل۸7): (82۷)03۸۷0 0 (81) :۸402/2/5
 leaf 302 | پهلوی (41آ۳۸7): 2ض/
 leaf 304 | پهلوی (1/ انم ۴۸۹۲1 ,۸۸۳5136 انگلیسی کهن (لفلا200 صزم. ‏ هر
 leaf 306 | پهلوی (۷1الل۳۸): ۸7 ,8۸ ایرلندی میانه (52ل1# 041002: دی
 leaf 308 | پهلوی (۸47ا۳۸): 0 ,207 لهستانی (۳0(/53): ندداا با ان
 leaf 309 | پهلوی (۲7الل۸): 306 پسگشت‌ها : هار درد
 leaf 310 | پهلوی (/۸(14۲): ۸081181۲1 ,۸08130 نروژی (۸/0/1750141): 1385
 leaf 316 | پهلوی (1اللمه): 06ات2۸ اپر لندی کهن (317ل8] ا0): 61
 leaf 318 | پهلو ی (ماتلمم: ,210۷۷8۸0 ,112/2 آلمانی (/0578//۸): دننز 2
 leaf 321 | پهلوی (1ا۳۸/7): 2 ,7۸7 لهستانی (۳0157): 721101171
 leaf 326 | پهلوی (1/هاتلهط). ,710۸4 آلمانی کهن (087/4(7 نز 2ا۵): 0186
 leaf 329 | پهلوی (۸1اب۸): 3 سرئدی (57750150): ۸
 leaf 330 | پهلوی (۵/7ا۳۸(7). 7۸ 193 207070
 leaf 333 | پهلوی (7ل۳۸): 77۸۸ افغانی (پشتو) (/۸۳0[7۸): هلق7
 leaf 334 | پهلوی (۲1بماتله): سرئدی (9520/517): 2207
 leaf 336 | پهلوی (1/ا۳۸3): 525 انگلیسی کهن رباکلاه80 صا۵):
 leaf 337 | پهلوی (بابلهه): 5۸ ساکونی کهن 54000۷0 ۰:00 5831۸8۷
 leaf 338 | پهلوی (1/مائلهه): ایسلندی کهن (۷210۸4۸بی8 صا0):
 leaf 339 | پهلوی (۲7ماتقهط): 3 رن آلمانی کهن (/027۵/۸0 بلاط صا0):
 leaf 340 | پهلوی (1/اتلهه): ,857282 گالیک (لاقهه): ۳
 leaf 341 | پهلوی (۳۸]47): 0 ,8۳۳ بلرچی (اتلنال۸): 7 ,187۳
 leaf 342 | پهلوی (741ل۳۸): فرانسه (ل7(ق۳۸): ۸7۵1
 leaf 344 | پهلوی (تشاتل۸): ۸ 87۸78
 leaf 347 | پهلوی (4۷1آ۸(7): 3 (نون هلندی (017627): ان
 leaf 350 | پهلوی (1/اتلمط): ۰ 5.7 دانمارکی (0۸7/8[7): ۱۱4
 leaf 352 | پهلوی (477ا7ت۲۸): 4 هلندی (7لع007). بت۸ا
 leaf 353 | پهلوی (1ام 41( ۳۸): 0 ,5۸3 لینوانی (4۸/1۸۸ن7): تآنتهقا5 ,ک۸آنل52
 leaf 355 | پهلوی (/۷ماللمه): آلمانی کهن (022(/۸7 ۱۵۷( 2ا۵):
 leaf 364 | پهلوی (۲ماتنههم: 5 رت 0 رسک ندید
 leaf 365 | پهلوی (۲1النه5۳:)۳ بگا5 سانسکریت (54۸/8877):
 leaf 368 | پهلوی (1/اتلمه): اناد 8 ادن نروژی (۷ل0۵ ۸70 (محلی) 11811
 leaf 368 | پهلوی (۲1شاتلهمم: 5۸ آلمانی کهن (ل05۶/۸ نانز صامم:
 leaf 369 | پهلوی (۲7هاتلهه): ۸ ,0ق5 ساکسونی کهن (542:0۸ 012): رید
 leaf 377 | پهلوی (۷ملتلهه): 2 گرنیکه (00777/0): اب :0۹۱
 leaf 388 | پهلوی (۷1هاتله): 7 ,لا 57 لینوانی (/(4الههتا7#لرم. ۳05
 leaf 389 | پهلوی (الاماللهه): ایا دا زر 1 ۳
 leaf 402 | پهلوی (۸2۲۸۲1ه): کف 10522/250
 leaf 406 | پهلوی (۲1مالقه): ۸ 3
 leaf 408 | پهلوی (1ماتله): ۷۸۵6 ,۷۸3۵63 اسپانیایی (52۸2/1877): امد دراه
 leaf 410 | پهلوی (۲1شاننمه): ۹1 سانسکریت (6۸(97077).
 leaf 416 | پهلوی (1اللهه): «زته انگلیسی (8(/0115): ۰ 101
 leaf 424 | پهلوی, (1/ها#لهج).. ‏ 2۸ لیترانی (04/۷4/۷ 607۳31:78 ,008871
 leaf 426 | پهلوی (۲مانهم): 6۸3۸۲ ,058025 اسلاوی کهن (10/شا5 ناب صا۵):
 leaf 428 | پهلوی (۱/مااقمه): هلندی (بلع07): " دی
 leaf 432 | پهلوی (1بماللهه): اند نی پروسی کهن (/(۶5ن۶۸ ۵0): هلاه
 leaf 434 | پهلوی (1ماتقهط). سوئدی (852[5[7). زد ان
 leaf 435 | پهلوی (۸۶۲7 ۰:۳ ۷۷181۴ ,۷۷18157۸۷ ,۸۸۲73870
 leaf 437 | پهلوی (7/مائله۳): اسلاوی کهن (51416 670863 00): ا
 leaf 440 | پهلوی (۲7مائلهه). بش61 ,شاه دانمارکی (0۸(75): 0۸
 leaf 441 | پهلو ی (1ا7ل[۳۸):
 leaf 443 | پهلوی (/۸۷ا۳۸): ,۸ انا چکه (28077)): زد ۷۸:۱
 leaf 445 | پهلوی رن ۰ ممتعته هلندی (/0076): 1
 leaf 457 | پهلوی (/ا2۸۶):(پازند) 3 ایسلندی کهن (9420/0۸ 0):
 leaf 462 | پهلوی (1الل۸): لهستانی (۳0/152): ند ۱۱۱
 leaf 464 | پهلوی (4ال2۸): 81۸7۸۲ ,۸127015717 8ب ۱۱۳۹
 leaf 466 | پهلوی (۲1اتزمم): ۸2 سوئدی (550157): 1۸ ‌
 leaf 468 | پهلوی (7/لتله): 0 ,11170 سانسکریت (5(757877):
 leaf 469 | پهلوی (۸7/4): ۰ ۷1220858 م۸۸2۵ ,5ف۸1۸3707
 leaf 470 | پهلوی (4۲1اللهه): ان لیترانی (/(۸ا۸07ا2777):
 leaf 471 | پهلوی (41ا۳۸3): بلغاری (۸لم.انا): 1
 leaf 474 | پهلوی (1ما۸): انگلیسی کهن (لداماه 8۸ 0/0):
 leaf 480 | پهلوی (۳۸/4]4۲7): 310011۸36 ,110۸6 ارمنی (۸84871۸01): 101
 leaf 482 | پهلوی (1/اتله): 5 ۸/801 روسی (۷ا55/): 7 ,ش3106
 leaf 487 | پهلوی (۲7هالله۳): ردان روسی (81835314/7): دا
 leaf 488 | پهلوی (۲مابزه: ۰ ,۸18306 ,۸4506 1 ,۸11۷70
 leaf 496 | پهلوی (47ا۳۸/7): رال۸]۹1۸57۸ ایسلندی‌کهن (270۸۲7۵اییو صاه).
 leaf 501 | پهلوی (۲1بمابته۳): ,۸06 ,۸۷۸۷۸۵۹ ,۲۲06 انگلیسی کهن (باقلا8/0 صام): ‏ ,۸۷۲5
 leaf 504 | پهلوی (۷7الله۸): ۸ انگلیسی کهن (81/ا8۸0 صل0): 3۷8۸
 leaf 506 | پهلوی (1/ابله۳۸): ۸۸ آلمانی کهن (0لهال052 بزتاط صام.
 leaf 510 | پهلوی (1مات(۸ط). رل ولزی (7اک 21 ): 0 ,2۷
 leaf 511 | پهلوی (/۷ل۳۸): آلمانی (/0870):
 leaf 516 | پهلوی (/4ا۸(7): ۷7 لهستانی (۳07./524): 03۸
 leaf 518 | پهلوی (۷1اللم۲۸): ۰ دانمارکی (0۸۷]514): ۷۸
 leaf 519 | پهلو ی (ماتطمم: ۰ ۷۷۸82۵0 ,۷۸۸2۵ صربی (558814(۷):(شاید) ۷۵
 leaf 520 | پهلوی (1ماتلم۳): ۷۷۸310۸ ,۷۸277۸۷ هلندی (7لع07ا0): ۰ را یدنا(
 leaf 521 | پهلوی (4۲اتت۸ :۰ ۷۷۵۸/1۵۸۲ ۷۸۵6۰ ۰ ۷84۸
 leaf 521 | پهلوی (4۲7ا۳۸(7): ۷۴ ایتالیایی (/۶۵ :۰ ۷۲97۵ ,۷۸۲۵
 leaf 522 | پهلوی (۲1مابلمه): ۰ ۷۷۳۳۲۸۸۲ ,۷12۸۷ لتونی (لتی) (/47۲1۸۸): ۷1863۷8 ,۷138717 ۱
 leaf 527 | پهلوی (4۲7ا۳۸7): ایا ۱۲ نروژی (/(۸707(۲201۸): از ی ۳۷
 leaf 530 | پهلوی (۲7ها۳۸/7): اد دانمارکی (0/157): رون
 leaf 533 | پهلوی (1اماتلهه): ,۸ ,11۸341 لیترانی (2/140۷ن7ل7/): -8۸
 leaf 538 | پهلوی (۸(71۸7): 1 2080520
===== پاشنه
===== پستان
```


## [2026-09-14T00:59:05.400Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS pahl ===\"; grep -n -i \"pahl\" SNS_pages.txt | head -20; echo \"=== SNS files ===\"; ls SNS* 2>/dev/null; wc -l SNS_pages.txt 2>/dev/null"
}
```


### [2026-09-14T00:59:05.449Z] TOOL RESULT

```
=== SNS pahl ===
18: A pahlavi persian Glossary
123:         rivSyat dar pahlavl az avistS ud zand.
234:                           An OZd Pahlavi Rivayat                                                                                        ?                     I
293:                                                                                                                          J.C. TAVADIA: $ayaet-n3 "Sayaet. A Pahlavi Text on
537:Nyb.           (Nyberg)   H.S. Nyberg, A Manual of Pahlavi
546:Pahl. V.-Glos.: D.D. Kapadia, Glossary of Paht-i
547:                                                                              FrP.:     H.F.J. Junker, The Farhang i Pahlavik,
550:Pahl. V.:  Dastoor Hoshang Jaraasp, Pahlavi Vendi-
555:Pahl. y. Vr.:              B.N. Dhabhar,' Pahlavi Yasna and
565:Paris 1960                                     Pahl. y                Vr. Glos.:     ibid.   (vol.   2)
567:Zeitschrift der Veutschen morgenl&ndU          PRivDd                  B.N. Dhabhar, The Pahlavi Rivayat accom-
572:C. Bartholomae, Zum Sasanidischen U»oht\       P.V         Gl ,:          CSee: Pahl. y. Vr. Glos.)
629:      (Pahl. Y     Vr.
630:                                                                                                          Pahl. V.                   Anklesaria     ^^^     •   *i j   1
727:        Pahlavi Fragments with text, trannlti
734:                      :   Pahlavi Vendidad, Bombay                                      i
750:                 :    The Pahlavi texts, vols 1,                                    M 1
831:                                                                                                                          :       The Pahlavi RivSyat accompanying
835:                                                                                                                          :       Pahlavi Yasna and Visperad, Bom-
862:          of the Persees, 2nd. ed., Bombay                             Hoshang, D.J.J : Pahlavi Vendidad with Glossarial
=== SNS files ===
SNS_pages.txt
SNS.txt
16583 SNS_pages.txt
```


## [2026-09-14T00:59:06.838Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n -i \"pahlūk\\|pahluk\\|phlwk\\|pāšnak\\|pasnak\\|pāšn\" NYB_vol2_glossary.txt NYB.txt 2>/dev/null | head -20"
}
```


### [2026-09-14T00:59:06.893Z] TOOL RESULT

```
=== NYB ===
NYB_vol2_glossary.txt:5274:pāra-: pārak Para-data-: Pēš-dāt parena-, perona-: parr paresu- (peresu-): pahlūk paršta-, paršti-: pušt pasca: pas
```


## [2026-09-14T00:59:14.265Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c $'\\f' SNS_pages.txt; grep -n \"\\[pdf page\" SNS_pages.txt | head -5; python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('leaves',len(p))\nfor i in range(130,150):\n    print('---leaf',i,'---')\n    print(' '.join(p[i].split())[:400])\nEOF"
}
```


### [2026-09-14T00:59:15.407Z] TOOL RESULT

```
242
leaves 243
---leaf 130 ---
V Ujc^Utab^'* ; l^ c^,b a.b fljl ? m p- 168. •rT/ia«5 ai^ :abar ravsnd: 3<t>i ^ .tA/Vt^ (Xofcual 5n5. * IH 137) ra ff ax*- : *•*** -oWo^rasan: VP& .T»-u-, r^/A^-u^i. Umvt&v-tafa*. ra tu-.fa. V .rr-.rr-.n-u/ir* •,***««• .**'tr«diiii ^ CAiW».15l6) J^rasnu- : fa. . T/Tr ^ IA/TT* u/u^ iji^loAi-^ofijsraSn, it: f*o3 •T1/U* (roMc^GoU.,.-^^!^ ^^l^^^^^ :rasn-a§tad: ^Y^-w^ A1/M ( ^-6-^) U j i, oMl)tar: L?T 
---leaf 131 ---
^ Ujc^Ua-U*^ m iU-; *=-yU 4.U«;I 5 TTA .^ . Ijj:ravan: X*J* •T/TV«$ -Tr:33: _>-3> H*. Man. It, 67)rwW» 0W».1M1 -van- :*» (Mir. Man. 111,61) rw n : >>V tpdM/A* lt/t* IT/IT* \ mj* ( P ^) f r . :30-um: Jjufe l .*Jff«4*j:ramag: SL£J 1 *-l /A^ olu^W ^'jj:ravanlg: -^^ .Y/YT^S -yr/T^ .{Kotwal. I66)rm : >^/j3A o-^l rabgandan/afgandan: LMYTWN, tn: j. «l>«£ft^ {Kotwal. -bgn- i^*.(n». 24)ai wi+ /Wi *. 16/W^ 
---leaf 132 ---
Lti o—*li *.L«;lj ltoc^U«,L«il, rr If -1,1 :abag: LWTH :>»: y$^> (Mir. Man. 11, 34) *b*g ^.>Tb J,ljl«j-l^- :sar a sar: ^->^ -* *^ :>;£ H (GNPE. 160) firas- ^j^" sarah- : :t- (Afir.Jftzn.11,62) sr «^ 1;1 x-j- r N Ui(/fc.440) CkaD-maratfa- : o'j u^;*' ,4*^ff>>^W6*iJ {^ U):R6san/R5ln: WU> r "JlJ :rOz: «-P . ,. Kent. Uapadifl. P- 329 :ii > - "/*** / 1 1 ***» r5cas- : U raucah-: ^ raocah-: b. .y-a^-TV^
---leaf 133 ---
rv li; .-.-jl-t fc.U «3'> lAi c^b «.b«jl, rrr .jaio :rextan: Vflft« * ^tf-^ ra?cayat- j /raSc j< : fc- nakti /r§c : •T/T»5 (p.31 n6. M/Y^ (fiffPE. 141) • aMtaam-:^ (i^ww^^ WtoJto*. ii, 4fi)VMj|fc &»«. U :amag/araah: 167 (^UcJU, LNH : ahni3ka _ >»: ^ ^\ •f/1A^ .V/JHS ^X «-U > i>'» *** <^ T> " Wj-«it- fc **? >' ** iwVi- 1 »' U ^ I .Y/W* -JUA^^g^ :abaxtar rOn: nVS**, if .Y/1Y** ITf/T* \ rwy : ^um.149
---leaf 134 ---
.Ujii-^U^t^l, ^^o-,b*. b *ys , rrr «7ffP£. 63) P Sda- :*#**-* PS^- : t- T/ir^ v/.v^.M/»rJ ( ^m,'.^^,, ^toob^o^M^ P a y raezisnlh: .ovu^^ : _oO i*&) ^:sab: LyLY* >»: *0>*> • 1/** ••»->: ng rased : ^^ ^ ( : •VM«S •»-* :be rased: ^.ii-u rm»»«ooTuSi,^»j£1 WWi 137) (/_ as _ > » _ ( te\r«*>* »£>) .cu.1 :rasldan .- -'£\^-'°^^^'^-asis„I -W^ *» CGffPE. 142) /rB- '.urtS*-** /***-' j' &- rn M. _^^ ^ ^ ra si5
---leaf 135 ---
U-i^-,Li*-U*;l, £1 dthus- L o*X oSt- tr" ** /ma6t . : ;l madman- : fa. .ffyYT* .fl-TV-Y-P/lT^ UotuaJ. 156.) .y^W-yo^-^ahmantar: ^i**-*^ miyaru. t^-6 U/YY^ .YA/\T^ !?/>•** -oW'OW'^ (0 Id/I-** .*K^'^ (?) *- Ur.Man. my J n:^ Wifto. 1116-17) mai<fyana-: (Wtr. Man. Ill, 58) rady^n: ^ II* 60.) .6/1*5 .i-j.owfcw^miyanag: 3W^ t jSli.(GNPE. 216-171matsya- : otfiS** masya-:^- J .Y/Tl^-n^sy'g :^«V {Mir. Man.
---leaf 136 ---
.^^l^o^U^U^'? c^U; u^b^L^I, TfA -^i-«jU_^ :abar mfidag sudan: W»h£i *--£- -9tf-K£ 1488)rao*na- :fc- U«*. .,TT-rT/f5 t> :mar: ^ • 6Y-TVTA/T^ (ilttfU^I, *..*;) ( \*>4? :^) joU.-madar: \t»4 lt/tY£ -oljjU :m5dar3n: &W-6 -i^t* ^U>,j , vH*"rfl*i*«» rraazanSn dSvfln: \juou *?£-*>.£ yt 01y (JU . ^ v /-«« u:raau5n! ,_ r l)^JU:raali5n: "»al<*• * : £. (Henning, BSOAS XI, 1943. p. 54 ;ju) .^Ji Wr. Wan. 1,491 
---leaf 137 ---
lii ,i_,U «.U»jlj JA3 c^^b^t *j1j YT - >^=n.axnyus . L. ..5i0ra-+(4iW.. 11") : : Jrt pT*i U.* Jii3 T,*Ki5 T: m3n j stasan: *uu-*¥>* - icf WiWb. 387) , l .TA/l->* \/X**S MUX'S -&/\iS ..bJ^Ul^l SBflndag garzidan: W^*'-*^ .*iU. u^iJ .*jl>iU-^ i ^,^U:mSnbad-/bi<3: fo^ {.Mir. la'nbyd: j-fc Uif/fc. 1093)nman5.paiti :t- •&/\^ -ff-\\/\r>S -Man.1, 42) l*™*^ 1fl/ir«^ .jIa,uU: ti*«)^ ,*.4W ^.^: Z anad:MHYWN,
---leaf 138 ---
Lft-U n .Ui^^lt*.L i. TTT \P/TT^ lj-j*.o>|l*»i»jH (V) . a.T : madan: ln*fi iraat a +,/gam-:La Jamiya, a +/gara : &$ rfW Ian s.^ (W£r.M<zrt.II,59)rodn, md : jili IGNPE. 11) • t/lV* . **W:be madan: t"^ "^ nj^l^O**1 ^ **!* :rast be madan: \V*4 ^j <&»->*> 1 ^^>-W*«-Mnc abar raad: ^^ U JhfljUU »A *!«" >>* o^O*** mihrandroz < :. ^H* *ttv*£ •***'**•« :deh/dxh= -^o^M^^'tf^^ : roihrandrozlh: Ih: L— „, -o-j
---leaf 139 ---
n : bj ia««UmIj >jlj fa _^_^-vUft-b*jlJ rrr (**##} m3h :^ (Worsens* *!^* »/TT* ^U ^^ *'W ^f *A '^ u L f u J* *>-Mard-bM: - •A?/T^ JT/HiS -AY/T^ f*j* :mard5m: ^ 11°^ J J ^' v '^*«tfU:ma S ag/masay: -0»-6 -rA-v/T^ iw/iy-5 .t/1** -f/1* 5 n/w<s it/*s \Y-A/to^ o Ujj* ( eH mardoman ***-£ ^-£ IT-V/V6** IT/v* ( ^*u't-*o*• •*) : l/TT^ «jar^ (ji4- imihtar: * ^ SJ -l,*patiy + /-grab lt4>iji-^A j*tf« Jj^. mar
---leaf 140 ---
,Uj --w fc U*^0^ Us is-«U *»|j •£!• W .*;*£•& Jj» • > . i tj"ii.ii ' o'jj *^j* :margarzan: 1 WtViobf jjlj ^ *ljl«- T oJ U r Uol ^^U^.US . j« j l5t ^^ c ^k.l jj ( <iw :«&) •-^/.j.o'jj ^ '^- r 1 1 l -^* l o1>^o T . TT-T l-IA-ir-W-A-T/A^ . a : - » Jj.jiji^. aS^LS ^bljjUT^ :margarzanan: , tri-O-o^-tf •^WoVi'^^'tfA^jM^'ob 1 ^ :margarzan: W^»^ /V««5.T-T/A^ WA-UY-Ufr-ni-A6-AT^Al-Yf-ff-?T-fo-n/T^ oT .Uil4
---leaf 141 ---
, U; c-^^ "^ *jV .—_,, L~ C^U **L Ojl) m ETV • *J*^ • W « ***• >.i fyj --» « o 'jj *Sj> I •• margar zan : WV*o$£ . Tr-T 1-1 A-l T-1-Y-6-T /A ^ . v - . . . a t5j*J9 iym tS^LS ^bljjUjt :margarzanan: ttvu-o^ ^U^'jj'o-i^j^j jLiy 'o'jj*^ :margarzan: W^«^" /I oiS . f-T/A^ l »A-l oY-1 <»6-1 1-A£i-AT-A t-Yf-*f-f r-f <»-1/V^ • 1/1Y^ -Tr-YY/16^ H aTpUila^ltf 4>HJ 4 Lr :raargarzan vinah: <>Ml ?e^-£ , ** *-T 
---leaf 142 ---
L_ V—-I- **L o;lj TTA j>j,i i^^c^j^JA^" tea** tta'A^wflffi *>£ «jrfU*M«trt*i»A*W»T*ftta*te* C^/PE.222)maoiri-±- u o K W >>;-> **** tfW^** J ol»-W v>— *W ^^ - crA?j»**«• J; lj {Bailey, BSOAS, XXIV, 1961, *.-4») - .«jj« imurdag: 3*a>»£ /Inar : L- araariyatS /mar : j'^*5 ^^' rariyatS, /mar : ji^*^.*. jfra-mairyeite WH»F. 218) .TT/i** {Mir. Man. II, 59) mwrdg: jtfi U*aj.i ^> rraurdagan: «f,5r r£ t&/t»
---leaf 143 ---
l_ __,!_ 4»L *;l_j Yfi tx; c— ^ *»^ *3'j * . JijUi, . jjjUs : usmurend : MNYTWN , nd :>* : »«***'£ • f/ir^ {Mir. Man. 1,44-53) >sm'r- c smyr :,-/• MDMHN , yh . -o !*&$* ^AW ^-'oV-^ "»>** ? -<tntf *tf jp jyo- ^Tjki ^ ; saheh: , 6 •)r/A^^J>tf>i-*;slh- : L (verbum, 171, 8)sh-:>;k >» :tis/cis: MND M : >» : -^yr^ {Mir. Man. tys :jsli{Kent, 184)cis-ciy :**i 0is: ^ {Mir. Man. Ill, 53) cys:>;^ 11,69) •Y/Y
---leaf 144 ---
bjc-,U«.U«i1j TOT b 4.U »v|j 11/ IT** (^jt^JiSjlirt^jij* *fyfr\ ?>j ^Ul . *£»*« rraexag? • 3-*<_,-6 eoo£ 5^maezant- /mafiz :*.*• VP£. m&hati:^ 226 m l ^-^M-ttJfriStejOfr* mask? r^j^bV 5*5. p. 74) 1108) . ft/w .S -Ai«». 3fc>-6 U>ai>ar 5n5.p.23) t *^U ^ >&K j| l^T^A. £0B. V) - t/ftl5 1( wt<*> :mizag: . :«*) tub tagak? a^*- : jl ^fc^ l^T tffcafefcar , o^r-iJ* *« *+fil< <S .{Dhabhavi-Per'eian Rivayate
---leaf 145 ---
* Lj c^-rfU **ii «;'j Ujcu^U^L^I, TAT 3>fc£ >i*-:mSnOg: r j>>^;awar :^ (Mir. Man. II, 44) >br- 6" .Man. mynwgt^t Wi^.1140) mainyav- : .(ij&.y**) raainyS :<fll* 61) ^^^.-T^zmSnOg I ab: -V* - *«* • Y-r/To^ w *..„.»L-*Jfc ******•(**) smSnoglha: >>— <£.&. Vh**jiRan* s Jackson Mem.p.S7 :*, n- s ^ A/W<5 .«>». :m§vag: 5l$£ mlwa ^ mygdg : :^ (Mir. Man. r,42)myw:^ tA 'T/ IV* .**/** itr/T*5 .(ijs-^j .j£b «A
---leaf 146 ---
I*. c^U *.L*)»J pU (AiWb. 632) T a*ji» jl** 'O^iaZjni-yaz: t» 1V/^ {Mir. Man. I, 43.1 •tfjlr^'rJ^ :niyabag: 5€xn Uotwai. 160) ny'bg : J** .a/iT^ .^^lfj^:niyabag ku. : £2 OW* (A*<MA< rvahar: **^> /,. vasar"-: l^J^ va ri- ;' vaijhar-::*" — '••uT^bS^i* iM.jU./vlil^ (uU^ .r/H^-OVir-tfatt. I,38)wh*r :>* 1348). )jud:w |Jfc| t ' fAt^-b^Oi^ 384) uta: L uta:L-_.^ r.Woyt , (AiWb. 1422) v»ra0ra#na- : t- |AUS
---leaf 147 ---
M Lj c—^L: ft-U illj U; ^—,b*.Ltjlj ran TO^ Cupa + a) upa-^Uc^^ ^var ***•>•«* 1" CMir .Man. II, ^^ w'wrydn ifi*lOM*S. 41.) u/w ^ 51.) • Y*-Tft/lV«f -TT/W -{Mir. Man. II,52)wha ng : ^fc wt^' •O*^ :naxun: \*o- ^• tfotw<2Z,158)n'xwn:^ i i i l\ a^». -,SLi^U:vavarigan: GffP*. 228) nakha-:^*^ ^ U/1^ *«*:>* •y/it*5 .6r-T-r/v^ (Mir. Han. n'zwg :> .**!>. ^b :nazuklh: ^1W • ojU.Uj,^^ miyayisn: «*->*-«o* .*#
---leaf 148 ---
) li; ^^U 4.1*3!} (Ujo-^U^L*^ T*' b. 1399-I402)vahistha- r^ii-1-** vahista-: sp»nja*ra-: J^U^l^T.^I^T.c^ :vazist:*u£«l why5t:>;L {Mir. Man. II, 52) whyit s jjA .Ma«. <*•£«>. 1417- vahistha-:^*-^ vaziSta- : U •T*/ir^ is.) vahist-it: -.pad V*>u-» uu .oo&IO* :vahist I bamlg: *£j »**>-"' . f rf (,c*M .«>U , ^ «*lfflj>:vastr: \«***»l ( V^*****-'-" T1/1T^ .(4tf/b. 1385) 2 vastra- : km • Si* r U [4 *i «*
---leaf 149 ---
o^U;c-,l:».t»;lj Lu c—»Lr a*b ail* Tf 9-X .v.^Uy-o^V'^ vuhuman: >6*M •d/n^f -A/A^ m/T<^ lotwal 5n5. 181) .^ W*i ^W :vohu. mana-:t- •T/yX'S .c-llafj^ « j^oL ltfi K,ii : namgenih: -*0* 3.$ \f\x3 'T/YT^ -?-A-T/16^ • t/TT^ l^c^-" vuhuraan-it: V>*V r-A* 1 **^ UiJ/fc. 1062-63)? nama. a^airyat 5 h. i bhabhar. Eeeaye. vol. I. p. 118 \£* murva^ : *«**' +W<J*»*> 'fi*t+*to'**tl vuhuman x jili.^3 rvuhuxsatr:
```


## [2026-09-14T00:59:25.678Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پهلو\" SNS_pages.txt | head -5; echo \"--- alt translit ---\"; grep -n -i \"pahluk\\|pahlUg\\|pahl.g\" SNS.txt | head -5"
}
```


### [2026-09-14T00:59:25.731Z] TOOL RESULT

```
--- alt translit ---
7944:•>*♦*: pahlQg: liVc^w 
31683:pahlQg 114/3
```


## [2026-09-14T00:59:29.923Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \\\n \"https://abadis.ir/fatofa/%D9%BE%D9%87%D9%84%D9%88/\" \\\n \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B4%D9%86%D9%87/\" \\\n \"https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%AA%D8%A7%D9%86/\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pst%E1%B8%97n\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/p%C3%A1r%C4%8Du%C5%A1\" ; do\n echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 399 verification (pahlu, pashne, pestan)\"; done"
}
```


### [2026-09-14T00:59:36.371Z] TOOL RESULT

```
Exit code 1
### https://abadis.ir/fatofa/%D9%BE%D9%87%D9%84%D9%88/
/home/sfmqrb/git/rishe/data/verification/sources/web/454583eccf7d94de.txt
### https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B4%D9%86%D9%87/
/home/sfmqrb/git/rishe/data/verification/sources/web/088d8a0db5ef98db.txt
### https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%AA%D8%A7%D9%86/
/home/sfmqrb/git/rishe/data/verification/sources/web/2576a75fe20938ee.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pst%E1%B8%97n
/home/sfmqrb/git/rishe/data/verification/sources/web/9cf778692d083772.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/p%C3%A1r%C4%8Du%C5%A1
/home/sfmqrb/git/rishe/data/verification/sources/web/51316aade70a1b1a.txt
```


## [2026-09-14T00:59:40.517Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7938,7950p' SNS.txt; echo \"---index---\"; sed -n '31680,31686p' SNS.txt"
}
```


### [2026-09-14T00:59:40.567Z] TOOL RESULT

```
no lt&) .^ :p ad: nojlpy :pa . _„& 

I .i/^r^ 

•>*♦*: pahlQg: liVc^w 
Uttffc. 896)parasu- : 6* 

•Oijjt'O*?** :pahlum: -6r*wo 
XKapadiya. Phi. V Gl. p.474 :^o'jo* 1 *jU jj) 
I Y J >>W pahalura:^ (Wan. Stud. lll)phlwm;/3ii 
I \^_>f/To^ M/16^ .t/1T'*S -T*/N** -t-r/f"S 
---index---

pahikarfid 120/9 
pahikarisn 120/6 
pahlQg 114/3 
pahlum axV 114/11 
pahlura ciS 114/14 
pahnay 115/14-117/19
```


## [2026-09-14T00:59:41.993Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### PIE psten\"; grep -n -A20 \"Proto-Indo-European$\" 9cf778692d083772.txt | sed -n '1,60p'; echo \"#### PIr parcus\"; head -60 51316aade70a1b1a.txt"
}
```


### [2026-09-14T00:59:43.314Z] TOOL RESULT

```
#### PIE psten
137: Proto-Indo-European
138- [ edit ] 
139-
140- Etymology
141- [ edit ] 
142-
143- Unknown; possibly related with Ancient Greek στῆθος ( stêthos , “ breast ” ) .
144-
145- Noun
146- [ edit ] 
147-
148- *pstḗn   m [ 1 ] 
149-
150- breast , teat 
151-
152- Inflection
153- [ edit ] 
154-
155- Athematic, hysterokinetic
156-
157- singular
#### PIr parcus
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/p%C3%A1r%C4%8Du%C5%A1
FETCHED: 2026-09-14T00:59:36Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T01:00:03.968Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg399.png')\nprint(im.size)\n# Greek box approx y 2050-2170, x 580-920 in 2550x3300\nim.crop((560,1930,1000,2180)).resize((1320,750)).save('pg399-greek.png')\nim.crop((560,1930,1000,2060)).resize((1760,520)).save('pg399-sog.png')\n\"; ls"
}
```


### [2026-09-14T01:00:05.421Z] TOOL RESULT

```
(2550, 3300)
agents.txt
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
c404-empty.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
crop14-394.png
crop18-394.png
edit_about.py
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
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
queue.txt
```


## [2026-09-14T01:00:10.637Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg399.png')\nim.crop((580,1930,1000,2200)).resize((1680,1080)).save('pg399-crop1.png')\n\""
}
```


### [2026-09-14T01:00:12.024Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:00:14.102Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg399-crop1.png"
}
```


### [2026-09-14T01:00:14.131Z] TOOL RESULT

```

```


## [2026-09-14T01:00:21.371Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:00:21.412Z] TOOL RESULT

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


## [2026-09-14T01:00:23.661Z] TOOL CALL #55: Bash

```json
{
 "command": "sed -n '80,160p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:00:23.703Z] TOOL RESULT

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


## [2026-09-14T01:00:29.355Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT pearl ===\"; grep -n -i \"PEARL,\" SKT.txt | head -3; echo \"=== FSD pearl (vol3) ===\"; grep -n -i \"perna\" FSD_vol3.txt | head -5; echo \"=== WLD band3 register persna ===\"; ls | grep -i wld"
}
```


### [2026-09-14T01:00:29.466Z] TOOL RESULT

```
=== SKT pearl ===
15201:Purl  {7),  spiced  beer.  (F.  -  L.)  lo Fhillips,  ed.  1 70^1.  But  it  should  be  pearl. It  was  a  term  in  cookery;  thus  sue  re  per U is  sugar  boiled  twice,  bcuillen  perU^  jelly- broth.  Cf.  Q.  perleUy  to  pearl,  rise  in  small bubbles  like  pearls.     See  Pearl.
=== FSD pearl (vol3) ===
920:soene was indicatecf or a supernatural being or action
999:government 3. (Archaic ] 'I'hc supernatural or other
2833:presenting supernatural or superhuman powers; acting
2838:2, Effected by magic, produced by occult supernatural
2935:supernatural or spiritual beings, of departed spirits, or of
=== WLD band3 register persna ===
WLD_band3.txt
```


## [2026-09-14T01:00:33.060Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT pearl entry ===\"; grep -n -i \"^Pearl\\|Pearl\\.\" SKT.txt | head -5; grep -n \"perla\" SKT.txt | head -5; echo \"=== WLD band3 ===\"; grep -n -i \"persnā\\|persna\\|pstēno\\|psteno\\|perku\" WLD_band3.txt | head -10"
}
```


### [2026-09-14T01:00:33.153Z] TOOL RESULT

```
=== SKT pearl entry ===
10884:name,  due  to  the  existence  of  such  terms madtx-jc/va,  honeysuckle  (lit.  moth wood),  madrrdHitiv,  worxibine  (lit  molV bush),  madrt-pcrla,  mother  of  pearl.  Hcri ma*frt  is  from  L.  mafrtm,  ace  <4  maftf mother;  see  Mother.  Pora  U  from  Gl wSipoz,  a.  light  friable  stone,*  also  a  stalid tile.  ^  Itut  the  word  has  certainly  bed mtdefstaiHi  (prob.  misundtrttocd)  as  coa nccted  witn  pert,  whence  na  merool scientific  terms  such  as  taitm-pora.  tnbi pora^  dfnti-fora. gtmmUporn,  'Scientific' etymology  is  usually  clumsy,  and  frC quently  wrong.  We  may  conclude  t E.  fere  has  been  substituted  for  Gk. by  conftision.
13564:PEARL.
13576:PearL  ^K.-L)     U.'E. perU.-^V. perU. 'a   i>carl,   a  berrie;'    Cot.      Of  disputea' origin;    we   find   also    Ital..   Span.    ProV. ptrta.  Port,  pereta^  peria ;  Low  L.  pernio (7lh  cent),     Prob.  put  for  L.  fiiruia  •,  i.  e. a  little  pear,  from  h.  finem,  a  pear ;  ef. Span.^r»7/a,  (1)  a  little  pear,  [2)  a  pear- shaped  ornament,   O.  Ital.  peroU,  a   little button   00   a  cap.     I'cihaps  suygested the  various  senses  of  L.  Isxica,  (1)  a \i)  olive-berry,  ^3)  round  fruit,  U)  a ^  Horace).     Set  P>ttl  \^lY
13578:PEARL-BARLEY.
13579:Pearl-barley.   (F.  -  L,:  and  E.)    F. ■*^  per!^,  pearl  barley   (Hamilton) ;    but jthis  seems  to  be  a  comiption  of  orge p<li, •billed  barley/  Cot.     See  Peel  (i).
201:superl. — SQperlatire.
942:Aristocracy.  (Gk.)  Modified  from  Gk. upicTiwparta,  govenunent  by  the  nobles  or •  bt-sl'  men.  — Gk.dpiiJTo-,  for  d/«ffTot,  best; and  Hparuv,  to  be  strong,  govern,  from mftiTin,  strong.  The  form  op-taroi  is  a  su- perlative from  the  base  d/i-  seen  in  np-rtof, hi.  (ip-iT^.  excellence.  (V  AK.  to  fit.) Per.  aristacmiic ;  whence  aristocrait  pot for  '  aiistocratic  perMjn.'
9535:Jotiflt,  Juat.  to  till.  (F.  — L.^  O.  F. fcujter.  to  UlL  —  Low  L.  iuxfane,  to approach  (hence  to  approach  with  hostile intent,  as  in  tilling). » I..  jMjr/a,  close  to, hard  by  (whence  O.  F.  jomjU,  dose  to). p.  The  form  iuxta  is  short  for  iug-ii'td,  fem. abl.  of  the  superlative  form  of  L.  iu^Ut continual.  From  the  base  tug'  of  iun^ert, toioin.    (VYUG.)
9798:Iiab«l :  see  I<ap  (i). I«abial.  (L.)     l^tt  L.  laHatu,  perlaio- ing  (o  the  lips.  *  L.  /ahum,  the  lip.     See Z#ap  it).  Lip.
10917:'  superlative  oTmapf$us,  great
=== WLD band3 ===
```


## [2026-09-14T01:00:51.132Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 454583eccf7d94de 088d8a0db5ef98db 2576a75fe20938ee; do echo \"######## $f\"; grep -n -A6 \"فرهنگ معین\\|معین\" $f.txt | head -30; done"
}
```


### [2026-09-14T01:00:52.245Z] TOOL RESULT

```
######## 454583eccf7d94de
70: فرهنگ معین
71-
72- (پَ ) ۱ - دو طرف سینه و شکم . ۲ - کنار، نزدیک . ۳ - ضلع .
73- (پَ لَ ) (ص . اِ. ) ۱ - قومِ پارت . ۲ - دلیر، شجاع . ۳ - شهر. 
74-
75- فرهنگ عمید
76-
--
174:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
175-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
176-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
177-
178- رَخ، ور، روی، کران، سویه، راستا، رهسو، پهلو، کنار، بازو
179-
180- جنب، جانب، کنار، 
--
199:فرهنگ لغت معین
200-
201- ازحد سند تا آب فرات بلاد فرس خواندندی یعنی شهرهای پارسی ، فرس جمع فارس و معنی فرس پارسایانست و بتازی چنین نویسند و پارسی را فارسی نویسند - فارسنامه ابن بلخی
202-
203- در لری بختیاری
204-پهلو ( بدن ) : پَلْ، پَهلی
205-پهلو / کنار: کِلْ، پَهلی، جُفت
--
241: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
242-
243- لینک ها 
244-
245- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
246-
######## 088d8a0db5ef98db
43: فرهنگ معین
44-
45- (نِ ) [ په . ] ( اِ. ) ۱ - بخش عقب پای آدمی ، پاشنا، عقب . ۲ - قسمتی از کفش که پاشنه روی آن قرار می گیرد. ۳ - قسمتی از در که در روی آن می چرخد. ۴ - استخوانی درشت و کوتاه که تکیة آدمی و دیگر حیوان هنگام ایستادن بر آن باشد. ، ~ در خانة کسی را درآوردن کنا 
46-
47- فرهنگ عمید
48-
49- ۱. (زیست شناسی ) قسمت عقب کف پا: پاشنهٴ پا.
--
105:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
106-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
107-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
108-
109- منبع. عکس فرهنگ فارسی یافرهنگ عمید
110-
111- پاشنه/[ نَ / نِ ] ( ا ) جز موخر پای آدمی، پَل، بَل، عقب، پاشنا، بَسل
--
120:زیر نظر دکتر محمد معین و دکتر سید جعفر شهیدی 
121-انتشارات دانشگاه تهران 
122-پاشنه سر: عقب سر. 
123-مانند: خاموش و درون آشفته، نادعلی زیر شب سیاه، پشت به ستون کهنه ی گچی داده و پاشنه ی سر بر خشتی خوابانده بود. 
124-کلیدر 
125-محمود دولت آبادی
126-
--
136: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
137-
138- لینک ها 
139-
140- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
141-
######## 2576a75fe20938ee
48: فرهنگ معین
49-
50- (پِ ) (اِ. ) اندامی در پستانداران که در جنس ماده دارای غده های تراوش شیر است و معمولاً رشد بیشتری دارد. ، ~ مادر را گاز گرفتن کنایه از ناسپاسی و حق نشناسی کردن . 
51-
52- فرهنگ عمید
53-
54- عضوی از بدن جانوران ماده که روی سینه رشد می کند و غدد شیری در آن قرار دارد. 
--
131:همان چشمه شیر و ماء معین. 
132-فردوسی. 
133-|| کنایه است از برجی از بروج دوازده گانه. کنایه از برج اسد است : 
134- ... [مشاهده متن کامل] 
135-چو برزد سر از چشمه شیر شید
136-جهان گشت چون روی رومی سپید. 
137-فردوسی. 
--
155:فرهنگ فارسی معین
156-
157- شیرجامه. [ م َ / م ِ ] ( اِ مرکب ) پستان زن و دیگر حیوانات. ( ناظم الاطباء ) ( از آنندراج ) ( برهان ) . پستان. ( فرهنگ جهانگیری ) . || آوندی که شیر در آن کنند. ( ناظم الاطباء ) ( آنندراج ) ( برهان ) ( از فرهنگ جهانگیری ) .
158-
159- پستان
160-ریشه هندواروپائی پستان، پستانوس pestānos ودر ایران باستان پستاناه pstanah و ریشه هند و ایرانی ان پستاناس pstānas ودر اوستا فشتان feštāna ودر سانسکریت استانا stana در بونان باستان استنیون stenion و در زبان توخاری پاسام pāssām و در زبان سغدی اشتن štenh. 
161- ... [مشاهده متن کامل] 
--
189: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
190-
191- لینک ها 
192-
193- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
194-
```


## [2026-09-14T01:00:52.697Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"4\\.44 RIB\\|‘RIB’\\|4\\.40 BREAST\" SYN.txt | head -10; grep -n -i \"Skt. parsu\\|parsu-, \" SYN.txt | head -5"
}
```


### [2026-09-14T01:00:52.766Z] TOOL RESULT

```
1169:Lat. costa ‘rib’ and ‘side’ (12.36) > It. costa, Fr. céte (OFr. coste) ‘side’ and ‘coast’, Sp. cuesta ‘slope’ but costa ‘coast’, Rum. coastd ‘rib, side, coast’. OFr. coste > ME coste ‘side’ and ‘coast’, NE coast; > Du. kust, MLG kost > Sw. kust; > NHG kiiste > Dan. kyst. The Gme. loanwords, in contrast to the Ro- mance words, are fully specialized to ‘coast’. REW 2279. Falk-Torp 612.
5460:6. ChSl. kostt, etc., general Slavie : Lat. costa ‘rib’. Further analysis of both as k-ost-, with relation to IE *ost- (above, 1) is attractive but dub. Walde-P. 1.186. Ernout-M. 225, 716. Berneker 582 f.
5464:The largest group of words for ‘rib’ is connected with words for ‘cover with a roof’, ‘a roof’ and were evidently applied to the plural ‘ribs’ as forming a sort of roof over the interior of the thorax. Some are connected with words for ‘bone’. The secondary use as ‘side’, etc. is widespread.
5466:2. Lat. costa (> It. costa, Fr. céte, Rum. coastd; Sp. cueste as ‘rib’ replaced by deriv. costilla) : ChSl. kostt ‘bone’ (4.16). Walde-P. 1.464. Ernout-M. 225. Walde-H. 1.281.
5469:4. ON rif, OE rib, OHG rippa, ete. general Gmc. (but Dan., Sw., rev ag ‘rib’ replaced by Dan. ribben, Sw. revben, epds. with ben ‘bone’) : ChSl. rebro ‘rib’, etc. general Slavic, fr. the root seen in Grk. épé¢w ‘roof over’, dpodos ‘roof’, ete. Walde-P. 2.371. Falk-Torp 896.
6377:4.40 BREAST" (Front of Chest)
6400:ChSl. priisi (pl.), SCr., Boh. prsa (pl.) or prsi, prsy (pl.), Boh. SE. prs ‘woman’s breast’, Pol. piers : Skt, Pargu., prsti-. Av. parasu- ‘rib’. Slavic shift from ‘ribs’ through ‘chest’ to ‘breast’, or ‘ribs’ and ‘chest’ fr. a common notion of ‘inclosing’; uncertain which, since root connection doubtful. Walde-P. 2.444
11924:roof’, OHG hirni-reba ‘skull’, OHG rip- pa, OF ribb ‘rib’, etc. Walde-P. 2.371.
13433:OHG reba, MHG, NHG rebe (also OHG winreba, etc.), prob. : Lat. répere ‘creep’, etc. (10.41). Falk-Torp 894. Walde-P. 1.277. Kluge-G. 473. Other- wise (: OHG ribba ‘rib’, etc.) Weigand- H. 2.544.
22037:Several of the words for ‘side’ were first used only for the ‘side’ of the body and are connected with words for ‘rib’.
```


## [2026-09-14T01:01:09.946Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"sogdian\\|ʾstn\\|Khotanese\" 9cf778692d083772.txt | head -20; echo \"---- pstanah page?\"; grep -n -i -A25 \"Descendants\" 9cf778692d083772.txt | head -50"
}
```


### [2026-09-14T01:01:10.025Z] TOOL RESULT

```
255: Sogdian: 𐼰𐽁𐽂𐼻𐼳 ( ʾštnh /⁠əštana⁠/ , “ breast ” ) 
---- pstanah page?
74: Descendants 
75-
76- 1.3 
77- References 
78-
79- Toggle the table of contents 
80-
81- Reconstruction:Proto-Indo-European/ pstḗn 
82-
83- Add languages 
84-
85- Reconstruction 
86-
87- Discussion 
88-
89- English 
90-
91- Read 
92-
93- Edit 
94-
95- View history 
96-
97- Tools 
98-
99- Tools
--
241: Proto-Germanic: *spenô ( “ nipple ” ) [ 4 ] ( see there for further descendants )
242-
243: Proto-Indo-Iranian: *pstánas ( see there for further descendants )
244-
245- *pston-ó-s [ 5 ] 
246- Proto-Indo-Iranian: *pstānás 
247- Proto-Iranian: *pstānáh 
248- Avestan: 𐬟𐬱𐬙𐬁𐬥𐬀 ( fštāna , “ woman's breast ” ) 
249-
250- Middle Persian: pystʾn' ( pestān , “ breast ” ) 
251- Persian: پستان ( pestân , “ breast ” ) 
252-
253- Northern Luri: پسۆ ( pesø ) 
254-
255- Sogdian: 𐼰𐽁𐽂𐼻𐼳 ( ʾštnh /⁠əštana⁠/ , “ breast ” ) 
256-
257- *sptén-yo-s [ 4 ] ( < metathesis *pstén-yo-s ) 
258- Proto-Balto-Slavic: *spenis 
259- Latvian: spenis ( “ nipple, teat, uvula ” ) 
260-
261- Lithuanian: spenỹs ( “ uvula ” ) 
262-
263- Old Prussian: spenis ( “ nipple, teat ” )
```


## [2026-09-14T01:01:50.899Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -8 61b30301d4bf6a4c.txt; echo \"...\"; grep -n -i -A12 \"Etymology\" 61b30301d4bf6a4c.txt | head -25"
}
```


### [2026-09-14T01:01:51.009Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/p%C4%81r%C5%A1nas
FETCHED: 2026-09-14T00:56:49Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found...
```


## [2026-09-14T01:01:57.705Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb && for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tp%E1%B8%97rsneh%E2%82%82\" \\\n \"https://en.wiktionary.org/wiki/perna%23Latin\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/p%C3%A1r%C4%87u%C5%A1\" ; do\n echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 399 verification (Persna, Perk 2)\"; done"
}
```


### [2026-09-14T01:01:58.740Z] TOOL RESULT

```
Exit code 2
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tp%E1%B8%97rsneh%E2%82%82
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
### https://en.wiktionary.org/wiki/perna%23Latin
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/p%C3%A1r%C4%87u%C5%A1
python3: can't open file '/home/sfmqrb/tools/fetch_source.py': [Errno 2] No such file or directory
```


## [2026-09-14T01:02:02.290Z] TOOL CALL #63: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tp%E1%B8%97rsneh%E2%82%82\" \\\n \"https://en.wiktionary.org/wiki/perna\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/p%C3%A1r%C4%87u%C5%A1\" ; do\n echo \"### $u\"; python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"$u\" --note \"page 399 verification (Persna, Perk 2)\"; done"
}
```


### [2026-09-14T01:02:07.299Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tp%E1%B8%97rsneh%E2%82%82
/home/sfmqrb/git/rishe/data/verification/sources/web/0c064032014d6c2d.txt
### https://en.wiktionary.org/wiki/perna
/home/sfmqrb/git/rishe/data/verification/sources/web/740700a48bfeb76f.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/p%C3%A1r%C4%87u%C5%A1
/home/sfmqrb/git/rishe/data/verification/sources/web/9ff956c3732e5c03.txt
```


## [2026-09-14T01:02:10.110Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 0c064032014d6c2d 740700a48bfeb76f 9ff956c3732e5c03; do echo \"######## $f\"; head -5 $f.txt; grep -n -i -A14 \"^ Etymology$\\|^ Descendants$\" $f.txt | head -45; done"
}
```


### [2026-09-14T01:02:11.180Z] TOOL RESULT

```
######## 0c064032014d6c2d
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tp%E1%B8%97rsneh%E2%82%82
FETCHED: 2026-09-14T01:02:03Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/tpḗrsneh₂ - Wiktionary, the free dictionary

137: Etymology
138- [ edit ] 
139-
140- Perhaps from *t(s)pērH- ( “ to kick with the heel ” ) +‎ *-sneh₂ , possible compound of *pd- ( “ foot ” ) +‎ *sperH- ( “ to beat, kick ” ) . [ 1 ] 
141-
142- Noun
143- [ edit ] 
144-
145- *tpḗrsneh₂   f [ 2 ] [ 3 ] [ 1 ] [ 4 ] 
146-
147- heel , upper thigh 
148-
149- Inflection
150- [ edit ] 
151-
--
234: Descendants
235- [ edit ] 
236-
237- Proto-Anatolian: 
238- Hittite: [script needed] ( paršna- ) 
239-
240- Proto-Germanic: *fersnō [ 3 ] ( see there for further descendants )
241-
242- Proto-Hellenic: 
243- Ancient Greek: πτέρνη ( ptérnē ) 
244-
245- Proto-Indo-Iranian: *pā́ršniš ( < *tpērsneh₂-i-s ) 
246- Proto-Indo-Aryan: *pā́rṣniṣ 
247- Sanskrit: पार्ष्णि ( pā́rṣṇi ) 
248-
######## 740700a48bfeb76f
URL: https://en.wiktionary.org/wiki/perna
FETCHED: 2026-09-14T01:02:06Z
STATUS: 200
TITLE: perna - Wiktionary, the free dictionary

394: Etymology
395- [ edit ] 
396-
397- Inherited from Latin perna . Compare Spanish pierna and Portuguese perna .
398-
399- Pronunciation
400- [ edit ] 
401-
402- IPA ( key ) : ( Northern ) [ˈpe̞r.nə] 
403-
404- IPA ( key ) : ( Balearic , Central ) [ˈpɛr.nə] 
405-
406- IPA ( key ) : ( Valencia ) [ˈpɛɾ.na] 
407-
408- IPA ( key ) : ( Northwestern ) [ˈpɛr.na] 
--
451: Etymology
452- [ edit ] 
453-
454- From Middle Cornish prena , from Proto-Brythonic *prɨnad , from Proto-Celtic *kʷrinati , from Proto-Indo-European *kʷrinéh₂ti ~ *kʷrinh₂énti .
455-
456- Pronunciation
457- [ edit ] 
458-
459- IPA ( key ) : /pernə/ 
460-
461- Verb
462- [ edit ] 
463-
464- perna 
465-
--
476: Etymology
477- [ edit ] 
478-
479- Inherited from Old Galician-Portuguese perna .
480-
481- Pronunciation
482- [ edit ] 
483-
484- IPA ( key ) : /ˈpeɾna/ 
485-
486- Rhymes: -eɾna 
487-
488- Syllabification: per‧na 
######## 9ff956c3732e5c03
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/p%C3%A1r%C4%87u%C5%A1
FETCHED: 2026-09-14T01:02:07Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-Iranian/párćuš - Wiktionary, the free dictionary

134: Etymology
135- [ edit ] 
136-
137- From Proto-Indo-European *pérḱus .
138-
139- Noun
140- [ edit ] 
141-
142- *párćuš   f 
143-
144- rib 
145-
146- Declension
147- [ edit ] 
148-
--
221: Descendants
222- [ edit ] 
223-
224- Proto-Indo-Aryan: *párśuṣ 
225- Sanskrit: पर्शु ( párśu ) ( see there for further descendants )
226-
227- Proto-Iranian: *párcuš ( see there for further descendants )
228-
229- Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-Iranian/párćuš&oldid=87171008 "
230-
231- Categories : Proto-Indo-Iranian terms inherited from Proto-Indo-European 
232- Proto-Indo-Iranian terms derived from Proto-Indo-European 
233- Proto-Indo-Iranian lemmas 
234- Proto-Indo-Iranian nouns 
235- Proto-Indo-Iranian feminine nouns
```


## [2026-09-14T01:02:19.048Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '245,275p' 0c064032014d6c2d.txt; echo \"=== latin perna ===\"; grep -n -B3 -A12 \"Proto-Italic \\*persnā\\|persnā\\|ham, gammon\\|sea mussel\" 740700a48bfeb76f.txt | head -40"
}
```


### [2026-09-14T01:02:19.130Z] TOOL RESULT

```
 Proto-Indo-Iranian: *pā́ršniš ( < *tpērsneh₂-i-s ) 
 Proto-Indo-Aryan: *pā́rṣniṣ 
 Sanskrit: पार्ष्णि ( pā́rṣṇi ) 

 Proto-Iranian: *pā́ršniš 
 Avestan: 𐬞𐬁𐬱𐬥𐬀 ( pāšna ) 

 Gurani: پاژنە ( pāžna ) 

 Kurdish:
 Northern Kurdish: pehnî , panî 
 Central Kurdish: پانێ ( panê ) , پانیە ( panye ) , پاژنە ( pajne ) 
 Southern Kurdish: پاژنە ( pajne ) 

 Old Persian: 
 Middle Persian: [script needed] ( pʾšnk' /⁠pāšnag⁠/ ) 
 Persian: پاشنه ( pâšne ) 

 Zazaki: paşne 

 Proto-Italic: *persnā [ 1 ] 
 Latin: perna ( see there for further descendants )

 Proto-Tocharian: *porsno ( “ ankle ” ) ( < *tpērsneh₂-h₁en- ) [ 4 ] 
 Tocharian B: porsnai- 

 References
 [ edit ] 

 ↑ 1.0 1.1 1.2 De Vaan, Michiel ( 2008 ), “ perna ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , pages 460-461 : “ *persnā- ” 

=== latin perna ===
1425- Etymology 1
1426- [ edit ] 
1427-
1428: From Proto-Italic *persnā , from Proto-Indo-European *tpḗrsneh₂ ( “ heel ” ) . Cognate with Ancient Greek πτέρνη ( ptérnē ) , Sanskrit पार्ष्णि ( pā́rṣṇi ) , Gothic 𐍆𐌰𐌹𐍂𐌶𐌽𐌰 ( fairzna , “ heel ” ) , Persian پاشنه ( pâšne , “ heel ” ) . [ 1 ] 
1429-
1430- Noun
1431- [ edit ] 
1432-
1433- perna   f ( genitive pernae ) ; first declension 
1434-
1435- A haunch or ham together with the leg, gammon .
1436-
1437- ( of animals ) A thigh - bone , with the meat upon it to the knee-joint, a leg of pork, a ham or gammon of bacon.
1438-
1439- a kind of mussel 
1440-
```


## [2026-09-14T01:02:25.489Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg399.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/399.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/399.png"
}
```


### [2026-09-14T01:02:25.607Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 64776 Sep 13 21:02 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/399.png
```


## [2026-09-14T01:09:19.561Z] TOOL CALL #67: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-399.json",
 "content": "{\n  \"pdf_page\": 399,\n  \"book_page\": 369,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Perk 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *perḱ-/*pérḱus 'rib; rib-cage, chest' (Pokorny 'perk-1' p. 820)\",\n      \"note\": \"Pokorny I 820 has exactly this root as '1. perk- ,Rippe; Rippengegend, Brust'' with Ai. párśu- / pārśvá-, av. parəsu- / pərəsu-, osset. fars, aksl. prьsi. Nourai's '2' is his own numbering (he separates the homophonous perk- roots differently from Pokorny, whose perk-1 'rib' sits between perk- 'fill' and perk- 'speckled'); the language label (Indo-European) and gloss ('rib, chest') are Pokorny's own wording. Wiktionary/Mann cite the u-stem shape *pérḱus > PII *párćuš. Watkins/AHD has no entry for this root (his perk-1 is Pokorny's 'speckled' root at the same page), so AHD is silent, not contradicting. Note the whole entry sits inside a well-known problem: Horn (1893) refused to derive NP pahlū from this root; Hübschmann (1895) corrected him and modern scholarship follows Hübschmann — see node #3.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *perḱ-/*pérḱus «دنده؛ ناحیهٔ دنده‌ها، سینه». پوکورنی (جلد ۱، ص ۸۲۰) همین ریشه را با همین معنا آورده و سنسکریت párśu-/pārśvá-، اوستایی parəsu-/pərəsu-، آسی fars و اسلاوی کهن prьsi را ذیل آن نهاده است. شمارهٔ «۲» از آنِ نورایی است نه پوکورنی. برچسب زبانی و معنای ریشه در نمودار درست است و ادعای نورایی در سطح ریشه پذیرفتنی است؛ اختلاف اصلی در حلقهٔ فارسی «پهلو» است که هرن آن را رد کرده و هوبشمان تصحیح کرده است (بنگرید به گرهٔ ۳).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/p%C3%A1r%C4%87u%C5%A1\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:820\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 54 (printed p. 820): '1. perk- ,Rippe; Rippengegend, Brust'. Ai. párśu- f. ,Rippe, gebogenes Messer', pārśvá-, -m ,Rippengegend, Seite', av. parəsu- f. ,Rippe', pərəsu- m. ,Rippe, Seite', osset. fars ,Seite, Strich, Gegend'; aksl. prьsi ,Brüste' ... WP. II 44 f.' — root, label and gloss are Nourai's source verbatim.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Bd. I p. 820 (POK_03.txt leaf 54)\", \"stance\": \"supports\", \"note\": \"'1. perk- ,Rippe; Rippengegend, Brust''.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann col./p. ~988 (IEC.txt l.12747)\", \"stance\": \"supports\", \"note\": \"'perKus, uos (prku-) \\\"side, bosom, soul, heart, life\\\". (Semantics obscure). WP II, 44. Skt. ... pársuh, f. \\\"rib\\\"; Av. (z-gde) pərəsus, m. \\\"rib, side\\\"; Oss. fars ...' — same root, u-stem shape.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 4.40 'breast' (SYN.txt l.6400)\", \"stance\": \"supports\", \"note\": \"'ChSl. prьsi (pl.) ... : Skt. parśu-, pṛṣṭi-, Av. parəsu- \\\"rib\\\". Slavic shift from \\\"ribs\\\" through \\\"chest\\\" to \\\"breast\\\"' — supports the 'rib → chest' semantics Nourai puts in the root box.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. perk-1, perk-2, perkwu- (AHD_watkins1985.txt l.844)\", \"stance\": \"silent\", \"note\": \"Watkins has no 'rib' root; his 'perk-1. Speckled ... [Pok. 2. perk- 820]' is a different root printed on the same Pokorny page. No contradiction, simply absent.\"},\n        {\"src\": \"WLD\", \"where\": \"WP II 44 f. (cited by Pokorny); only Band 3 (Register) is on disk as WLD_band3.txt\", \"stance\": \"silent\", \"note\": \"Bände I–II are not in the local library, so the WP page Pokorny points to could not be read; the Register volume has no usable entry.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"paresu, peresu\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan has two ablaut variants of the same u-stem: parəsu- f. 'rib' and pərəsu- m. 'rib; rib-region, side of the chest' (the second attested only in compounds, e.g. parəsu.masah- 'of the size of a rib', Vd. 5.54–56, 8.16). Both continue Proto-Iranian *parću- < PII *párćuš < PIE *pérḱus, with the regular Iranian outcome of PIE palatal *ḱ as s (against Old Persian θ, Sanskrit ś). Nourai's 'paresu, peresu' is simply the schwa-less typing of parəsu-/pərəsu-.\",\n          \"derivation_fa\": \"در اوستای نو دو گونهٔ آوایی از یک ستاک u-دار به کار رفته است: parəsu- (مؤنث) «دنده» و pərəsu- (مذکر) «دنده، ناحیهٔ دنده‌ها، پهلوی سینه» که تنها در ترکیب دیده می‌شود (مثلاً parəsu.masah- «به اندازهٔ یک دنده»، وندیداد ۵٫۵۴–۵۶). هر دو از ایرانی باستان *parću-، از هندوایرانی *párćuš و در نهایت از هندواروپایی *pérḱus می‌آیند؛ کامی‌شدهٔ هندواروپایی *ḱ در ایرانی به s و در پارسی باستان به θ بدل شده است. نگارش نورایی («paresu, peresu») تنها صورتِ بی‌شوایِ همان دو واژه است و ادعای او درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/p%C3%A1r%C4%87u%C5%A1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:820\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 54: 'av. parəsu- f. ,Rippe', pərəsu- m. ,Rippe, Seite'' — both of Nourai's forms, both glossed 'rib, side'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. s.v. parəsav- and pərəsav- (BRT.txt ll.15812, 16145)\", \"stance\": \"supports\", \"note\": \"'j. parəsav- f. \\\"Rippe\\\" ... ai. párśav- f. ... Pü.: pahlūk' and 'j. pərəsav- m. 1) \\\"Rippe\\\" (nur Komp.) 2) \\\"Rippengegend, Brustseite\\\" ... Vgl. parəsav-. Pü.: pahlūk' — Bartholomae not only has both stems but glosses them with the Pahlavi rendering pahlūk, i.e. node #2.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 820\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. perKus (IEC.txt l.12747)\", \"stance\": \"supports\", \"note\": \"'Av. (z-gde) pərəsus, m. \\\"rib, side\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"pahlŭg\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian pahlūg [phlwk'] 'side, rib' does not descend from the Avestan (North-West-ish, s-) form but from the South-West Old Persian cognate *parθu-ka- (PIE *ḱ > OP θ). The cluster -rθ- then underwent the characteristic SW Iranian change -rθ- > -hl-, exactly as Old Persian Parθava- 'Parthia' > MP Pahlav 'Parthian', which is why pahlūg 'rib/side' and Pahlav 'Parthian' look alike without being the same word. The suffix -ka- > -g is the ordinary MP diminutive/adjectival -ag/-ug. Nourai's arrow Avestan → Pahlavi is a shortcut: Avestan parəsu- is the sister, not the mother, of the form pahlūg continues — but the Pahlavi word itself and its membership in this root are not in doubt, and both Bartholomae and Nyberg gloss Av. parəsu- with 'Pü. pahlūk'.\",\n          \"derivation_fa\": \"فارسی میانهٔ pahlūg (نوشتار phlwk') «پهلو، دنده» مستقیماً از صورت اوستایی نمی‌آید، بلکه دنبالهٔ همتای پارسی باستانِ آن یعنی *parθu-ka- است؛ زیرا کامیِ هندواروپایی *ḱ در ایرانی جنوب‌غربی (پارسی باستان) به θ بدل شده و سپس خوشهٔ -rθ- در همان شاخه به -hl- تبدیل شده است — همان دگرگونی که Parθava- را به «پهلو/پهلَو» (پارتی) رساند. پسوند -ka- نیز به -g فارسی میانه بدل شده است. پس پیکانِ «اوستایی ← پهلوی» در نمودار میان‌بُر است و اوستایی parəsu- خواهرِ این واژه است نه مادرِ آن؛ با این همه، بارتولومه و نیبرگ هر دو برابرِ پهلویِ parəsu- را همان pahlūk نوشته‌اند و اصل ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SNS:114\", \"status\": \"supports\", \"note\": \"Tavoosi, Vāže-nāme-ye Šāyast nē Šāyast: the index (SNS.txt l.31683) reads 'pahlūg 114/3', i.e. p. 114 line 3; the glossary entry on that page (SNS.txt l.7944) prints 'pahlūg' with the comparison '(AiWb. 896) parəsu-', exactly the arrow Nourai draws (Av. parəsu- → Phl. pahlūg). The page number Nourai cites is correct.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict., English index 'rib pahlug' (PHD.txt l.3439)\", \"stance\": \"supports\", \"note\": \"'rib pahlug.' — the word and meaning are standard MP.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Avestan–Pahlavi index (NYB_vol2_glossary.txt l.5274)\", \"stance\": \"supports\", \"note\": \"'parəsu- (pərəsu-): pahlūk' — Nyberg equates precisely Nourai's two Avestan forms with Pahlavi pahlūk.\"},\n            {\"src\": \"BRT\", \"where\": \"s.v. parəsav-/pərəsav- (BRT.txt ll.15841, 16147)\", \"stance\": \"supports\", \"note\": \"'Pü.: pahlūk' under both stems.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §342 (HUB.txt ll.1484-1487)\", \"stance\": \"supports\", \"note\": \"'geht auf ein ap. *parθu- aus iran. *parśu- (skr. parśu- \\\"Rippe\\\", zd. pərəsu-, ZPGl. 10: parəsu- = phl. pahlūk \\\"Rippe\\\" etc.) zurück' — gives the Old Persian *parθu- intermediate that Nourai's chart skips.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"pahlŭ «پهلو ٢»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian پهلو pahlū 'side, flank; the flesh between the last rib and the hip' continues MP pahlūg regularly: final MP -g after a long vowel is lost in NP (cf. MP bandag > NP banda, MP dānag > NP dāna), giving pahlū(v). The word was borrowed onward into Ottoman/Turkish pehlu 'side, flank' and back into Kurdish pal, Baluchi pahlī 'rib'. The one real dispute: Horn (Grundriss no. 342 = the entry translated at AEF:415) refused this derivation, writing 'Mit aw. pərəsu- \\\"Rippe, Seite\\\" ... lässt sich np. pehlū lautlich nicht direkt zusammenstellen' and connecting it instead with Av. pərəθu- 'broad' (Skt. pṛthu-); Mann (IEC s.v. prthus) still follows Horn. Hübschmann §342 answered this two years later — 'Np. pahlū \\\"Seite\\\" hat mit zd. pərəθu- \\\"breit\\\", skr. pṛthivī nichts zu thun' — and his route through OP *parθu-ka- is what Wiktionary and current handbooks give. Nourai is on the winning side; Nourai's «پهلو ٢» simply distinguishes this word from پهلو 'Parthian, hero' (his Per-per-os / Pahlav entry).\",\n          \"derivation_fa\": \"«پهلو» در فارسی نو از فارسی میانهٔ pahlūg است؛ ‑g پایانیِ پس از واکهٔ بلند در گذر به فارسی نو می‌افتد (مانند bandag > بنده و dānag > دانه) و pahlū به دست می‌آید. این واژه سپس به ترکی عثمانی (pehlu «پهلو، کنار») وام داده شده و صورت‌های کردی pal و بلوچی pahlī «دنده» نیز وام از فارسی‌اند. نکتهٔ مورد اختلاف این است: هرن در Grundriss (شمارهٔ ۳۴۲، همان مدخلی که ترجمهٔ فارسی‌اش AEF:415 است) این ریشه‌شناسی را رد کرده و «پهلو» را به اوستایی pərəθu- «پهن» بسته است، و مان نیز همان را تکرار کرده است؛ ولی هوبشمان در بند ۳۴۲ «مطالعات فارسی» صریحاً نوشته که «پهلوِ فارسی نو با pərəθu- و pṛthivī هیچ ارتباطی ندارد» و آن را از پارسی باستانِ *parθu-ka- گرفته است. پژوهش امروزی (ویکی‌واژه و کتاب‌های مرجع) جانب هوبشمان را می‌گیرد، پس ادعای نورایی درست است. شمارهٔ «۲» در نمودار تنها برای جدا کردن این «پهلو» از «پهلو/پهلَو» به معنی پارتی و پهلوان است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88\",\n            \"https://abadis.ir/fatofa/%D9%BE%D9%87%D9%84%D9%88/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AEF:415\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asās-e Ešteqāq-e Fārsi (the Persian version of Horn + Hübschmann) is not online and not on disk (refs_online.json marks it 'catalog', 'Not online'). The German original of the corresponding entry — Horn, Grundriss no. 342 'pehlū \\\"Seite\\\"' (HRN.txt ll.3239-3247) — actually CONTRADICTS the chart ('lässt sich np. pehlū lautlich nicht direkt zusammenstellen'), while the Hübschmann notes that AEF incorporates (Pers. Stud. §342) support it; Nourai evidently cites the volume for the Hübschmann correction.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 342 (HRN.txt ll.3239-3247)\", \"stance\": \"contradicts\", \"note\": \"'aw. pərəθu- \\\"breit\\\"; phlv. pahlūk bezw. pahrūk \\\"Seite\\\"; ai. vergl. pṛthivī \\\"Erde\\\" ... Mit aw. pərəsu- \\\"Rippe, Seite\\\", ai. pārśva-, ... oss. fars \\\"Seite\\\" lässt sich np. pehlū lautlich nicht direkt zusammenstellen.'\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §342 and §103b (HUB.txt ll.1484-1487, 7588)\", \"stance\": \"supports\", \"note\": \"'pahlū \\\"Seite\\\" = zd. pərəsu-, parəsu-, skr. parśu-, ap. *parθu-. Vgl. §97: ap. rθ = np. hl' — explicit correction of Horn, with the sound law rθ > hl.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. prthus 'broad' (IEC.txt l.13695)\", \"stance\": \"contradicts\", \"note\": \"'prthus \\\"broad\\\" (?) ... Per. cf. pahlü, s. \\\"side\\\"' — Mann keeps Horn's rejected connection.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi s.v. پهلو (via abadis)\", \"stance\": \"silent\", \"note\": \"'(پَ) ۱ - دو طرف سینه و شکم. ۲ - کنار، نزدیک. ۳ - ضلع.' — meaning matches the chart, but the online text carries no origin tag for this entry.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rišehā-ye Hend-o-Orupāyi (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"no headword پهلو; every hit for the string is the language label 'پهلوی' in other entries.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"prs`\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Manichaean Sogdian prsʾ (pársā) continues the same Proto-Iranian *parću- as Av. parəsu-, in the accusative-feminine shape; Gharib registers it with the explicit note '<Av. pərəsu, acc. f.' The double gloss is real: alongside 'side' the word is used for 'hour / division of time' (Henning, BSOAS 11, 312.99–101 — a 'side/part' of the day, the same metonymy as Arabic-Persian پاس 'watch of the night'), which is where Nourai's 'hour, time' comes from. Buddhist Sogdian has the parallel prsʾkh 'side, rib' (Gharib 7206), matched to Khotanese pālsa-.\",\n          \"derivation_fa\": \"سغدیِ مانوی prsʾ (pársā) دنبالهٔ همان ایرانی باستان *parću- است که اوستایی parəsu- نیز از آن است؛ غریب در فرهنگ سغدی (شمارهٔ ۷۲۰۴) صریحاً می‌نویسد «<Av. pərəsu، حالت رایی مؤنث». دو معنایی که نورایی آورده هر دو در منبع هست: «پهلو/سو» و «ساعت»، و معنای دوم از همان مجازِ «بخش/پارهٔ روز» می‌آید (هنینگ، BSOAS ۱۱). در سغدی بودایی صورت موازی prsʾkh «پهلو، دنده» (شمارهٔ ۷۲۰۶) هم ثبت شده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:289\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 7204 on the leaf whose printed page computes to 289 (SOD_pages.txt leaf 355, printed = leaf − 66): '7204 prsʾ M | parsa ?, pārsā ©<Av. pərəsu ©acc. f. | hour, side | GMS 138, 971; Hen. BSOAS 11, 312.99, 101'. Nourai's page number is exact and the gloss 'side, hour' is verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib nos. 7204, 7206 (p. 289)\", \"stance\": \"supports\", \"note\": \"see ref_check; 7206 prsʾkh 'side, rib', Khot. pālsa-.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 820\", \"stance\": \"silent\", \"note\": \"Pokorny lists Avestan, Sanskrit, Ossetic and Slavic under 1. perk- but no Sogdian.\"},\n            {\"src\": \"BRT\", \"where\": \"s.v. parəsav- (BRT.txt l.15812)\", \"stance\": \"supports\", \"note\": \"gives the Avestan etymon Gharib points to.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"paršu, pâršu, pâršva\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit पर्शु párśu- f. 'rib (also: curved knife)' and पार्श्व pārśvá- n./m. 'rib-region, side, flank' are the Indo-Aryan reflexes of PII *párćuš < PIE *pérḱus, with PII *ć > Skt. ś. pārśvá- is the vṛddhi-derivative in *-u̯o- built on párśu-, hence the long ā. Nourai's middle form 'pâršu' is not a separate Vedic lemma; it is either the vṛddhi stem pārśu- (attested as the first member of compounds and as an adjective 'belonging to the ribs') or simply a doublet spelling of pārśvá-. The pair párśu-/pārśvá- is exactly what Pokorny prints on the cited page.\",\n          \"derivation_fa\": \"سنسکریت párśu- (مؤنث) «دنده» و pārśvá- «ناحیهٔ دنده‌ها، پهلو» بازتاب هندوآریاییِ همان *párćuš هندوایرانی‌اند؛ ć هندوایرانی در سنسکریت به ś بدل می‌شود و pārśvá- ساختِ وریدی‌شدهٔ (vṛddhi) párśu- با پسوند *-u̯o- است، از این رو ā کشیده دارد. صورت میانیِ نمودار (pâršu) واژهٔ مستقلی در ودا نیست و یا همان ستاک وریدیِ pārśu- در ترکیب‌هاست یا نگارش دوگانهٔ pārśvá-. جفت párśu-/pārśvá- دقیقاً همان است که پوکورنی در صفحهٔ ۸۲۰ آورده است؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/p%C3%A1r%C4%87u%C5%A1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:820\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 54: 'Ai. párśu- f. ,Rippe, gebogenes Messer', pārśvá-, -m ,Rippengegend, Seite''. Two of Nourai's three forms are verbatim; 'pâršu' is not separately listed.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 820\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. perKus (IEC.txt l.12747)\", \"stance\": \"supports\", \"note\": \"'Skt. cf. parśvya, dual n. \\\"heaven & earth\\\"; pārśvam, n. \\\"side\\\" and pársuh, f. \\\"rib\\\"'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.40 (SYN.txt l.6400)\", \"stance\": \"supports\", \"note\": \"'Skt. parśu-, pṛṣṭi-, Av. parəsu- \\\"rib\\\"'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Persna\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *tpḗrsneh₂ 'heel' (Pokorny's persnā, -sni-, -sno-, p. 823)\",\n      \"note\": \"Pokorny I 823 prints 'persnā, -sni-, -sno- ,Ferse'' with Ai. pā́rṣṇi-, av. pāšna-, gr. πτέρνη, lat. perna (*persnā), got. fairzna, hitt. paršina — page, label and gloss all as Nourai gives them. Modern reconstruction adds an initial stop to explain the Greek πτ- and Hittite paršna-: Mann already wrote 'ptersna (persna)', and Wiktionary/de Vaan (2008) give *tpḗrsneh₂; this is a refinement of Nourai's form, not a refutation. Note the root itself is unrelated to the Perk 2 root above despite the similar look.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *tpḗrsneh₂ «پاشنه». پوکورنی (جلد ۱، ص ۸۲۳) آن را به صورت persnā, -sni-, -sno- «پاشنه» آورده و سنسکریت pā́rṣṇi-، اوستایی pāšna-، یونانی πτέρνη، لاتین perna (< *persnā)، گوتی fairzna و هیتی paršina را ذیل آن نهاده است؛ یعنی صفحه، برچسب زبانی و معنای نمودار درست است. بازسازی امروزی برای توضیح πτ- یونانی و paršna- هیتی همخوان آغازینِ *t- را نیز می‌افزاید (مان: ptersna؛ دِ ڤان ۲۰۰۸ و ویکی‌واژه: *tpḗrsneh₂)؛ این تکمیل صورت نورایی است نه ردّ آن.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tp%E1%B8%97rsneh%E2%82%82\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:823\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 57 (printed p. 823): 'persnā, -sni-, -sno- ,Ferse'. Ai. pā́rṣṇi- f., av. pāšna- n. ,Ferse'; gr. πτέρνη f.; lat. perna f. (*persnā) ,Hinterkeule, Schweineschinken ...'; got. fairsna ... hitt. paršina ... WP. II 50 f.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Bd. I p. 823\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann s.v. ptersna (IEC.txt l.13712)\", \"stance\": \"partial\", \"note\": \"'ptersna (persna) \\\"hock heel, ham, ankle, leg-joint, lower leg\\\". WP II, 50' — same root, but Mann's headword already carries the initial pt-.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 4.37 (SYN.txt l.6248)\", \"stance\": \"supports\", \"note\": \"'Lat. perna \\\"ham, haunch\\\" (esp. of pork) : Grk. πτέρνα \\\"heel, ham\\\", Skt. pārṣṇi-, Av. pāšna-, Goth. fairzna \\\"heel\\\", etc. Walde-P. 2.50f.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. persna (AHD_watkins1985.txt l.844)\", \"stance\": \"supports\", \"note\": \"'persna. Heel. Latin perna, ham, leg, sea mussel: PEARL. [Pok. persna 823.]' — Watkins keeps Pokorny's headword shape and page.\"},\n        {\"src\": \"WLD\", \"where\": \"WP II 50 f. (cited by Pokorny)\", \"stance\": \"silent\", \"note\": \"Bände I–II of Walde-Pokorny are not in the local library; only the Register (WLD_band3.txt), which yields nothing for this root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"pâšna\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan pāšna- n. 'heel', attested in the instrumental dual pāšnaēibya (Vd. 8.70–71) and pāšnāibya (Vd. 2.31), and in the compound zairi-pāšna- 'with golden heel' (Yt. 5.38). It continues Proto-Iranian *pā́ršniš with the regular Iranian loss of r before the cluster and *ršn > šn; Sanskrit keeps the r in pā́rṣṇi-. Nourai's 'pâšna' is the standard transliteration with â for ā.\",\n          \"derivation_fa\": \"اوستایی نو pāšna- (خنثی) «پاشنه»، برجای‌مانده در صورت دوگانهٔ ابزاری pāšnaēibya (وندیداد ۸٫۷۰–۷۱) و pāšnāibya (وندیداد ۲٫۳۱) و در ترکیب zairi-pāšna- «زرین‌پاشنه» (یشت ۵٫۳۸). این واژه از ایرانی باستان *pā́ršniš است؛ در ایرانی r پیش از خوشهٔ šn افتاده (*ršn > šn) حال آنکه سنسکریت آن را در pā́rṣṇi- نگاه داشته است. نگارش نورایی تنها â را به جای ā به کار برده و ادعای او درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tp%E1%B8%97rsneh%E2%82%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:823\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 57: 'av. pāšna- n. ,Ferse''.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. s.v. pāšna- (BRT.txt l.16060)\", \"stance\": \"supports\", \"note\": \"'j. pāšna- n. \\\"Ferse\\\": ... pāšnaēibya V. 8.70, 71; — aiwiδā zəmō pāšnāibya vīžara V. 2.31. KompE. — ai. vgl. pā́rṣṇi- f.; np. pāšna. ... Pü.: pāšnak' — Bartholomae gives the Pahlavi and New Persian continuations in the same entry.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 823\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.37 (SYN.txt l.6248)\", \"stance\": \"supports\", \"note\": \"'Av. pāšna-' listed with Skt. pārṣṇi- and Goth. fairzna.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"pâšnak\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian pāšnag [p'šnk'] 'heel' = the Iranian *pāšna- of the Avestan node plus the productive MP suffix -ak/-ag (the same -ak that gives bandag, dānag, dastag). MacKenzie normalises it pāšnag, older transcriptions (Bartholomae's 'Pü.', Horn, Hübschmann) write pāšnak; Nourai's -k form is the older convention, not an error.\",\n          \"derivation_fa\": \"فارسی میانهٔ pāšnag (نوشتار p'šnk') «پاشنه» از همان *pāšna- ایرانی به‌علاوهٔ پسوند زایای -ak/-ag فارسی میانه ساخته شده است (همان پسوندی که در bandag، dānag و dastag دیده می‌شود). مکنزی آن را pāšnag می‌خواند و نگارش‌های کهن‌تر (ترجمهٔ پهلویِ بارتولومه، هرن، هوبشمان) pāšnak؛ پس -k در نمودار نورایی خطا نیست بلکه سنت نگارشی کهن‌تر است و ادعای او درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tp%E1%B8%97rsneh%E2%82%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:355\", \"status\": \"partial\", \"note\": \"Borhan-e Qāte' (Mo'in's ed.) vol. 1: the پاشنه entry with Mo'in's footnote falls on leaves 576–577 of BQT_v1_pages.txt, i.e. printed pp. ~354–355 by the volume's offset — so Nourai's page is right — but the Persian OCR of Mo'in's Latin-script footnote on that leaf is unreadable ('ارمنی ۳80285201', 'وخ 51202 ۳8. سریکلی 0۷6112' = Wakhi and Sarikoli cognates), so the Pahlavi form Mo'in prints could not be read out of the scan. Vols 1–2 are not covered by tools/ref_page.py ('no scan of BQT covers printed page 355').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict. s.v. pāšnag (PHD.txt l.545)\", \"stance\": \"supports\", \"note\": \"'pāšnag [p'šnk' | N ~a] heel.' — with the New Persian continuation marked.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 276 (HRN.txt ll.2728-2729)\", \"stance\": \"supports\", \"note\": \"'276. pāšne \\\"Ferse\\\". aw. pāšna- \\\"Ferse\\\"; phlv. pāšnak; ai. pā́rṣṇi-' — the whole Av. → Phlv. → NP chain of the chart in one entry.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §§124a, 129b (HUB.txt ll.8611, 9035)\", \"stance\": \"supports\", \"note\": \"'pāšna \\\"Ferse\\\" = phl. pāšnak, zd. pāšna-' and 'Ap. sn = np. šn und s: pāšna \\\"Ferse\\\" = phl. pāšnak, zd. pāšna-, skr. pārṣṇi-'.\"},\n            {\"src\": \"BRT\", \"where\": \"s.v. pāšna- (BRT.txt l.16060)\", \"stance\": \"supports\", \"note\": \"'Pü.: pāšnak'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II glossary\", \"stance\": \"silent\", \"note\": \"grep for 'pāšnak/pasnak' in NYB_vol2_glossary.txt returns nothing; the word does not occur in Nyberg's text selection.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"pâšneh «پاشنه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian پاشنه pāšna/pāšne 'heel (of the foot; of a shoe; the pivot a door turns on)' from MP pāšnag by the regular loss of the final -g and its replacement by -a/-e (MP -ag > NP -a, as bandag > banda, dānag > dāna). Hübschmann files it under exactly this rule ('Die im Phl. ... Suffixe -ak ... sind im Np. zu a ... geworden: ... pāšna \\\"Ferse\\\" = phl. pāšnak'). Dialect forms pāžna (Gurani), pajne/pehnî (Kurdish), paşne (Zazaki) show the same inheritance rather than borrowing. Mo'in tags the word [په.] 'Pahlavi'. The chart gives no reference for this node; none is needed.\",\n          \"derivation_fa\": \"«پاشنه» در فارسی نو از فارسی میانهٔ pāšnag است: پسوند -ag فارسی میانه در فارسی نو به -ه/-a بدل می‌شود (bandag > بنده، dānag > دانه). هوبشمان همین واژه را نمونهٔ همان قاعده آورده است. صورت‌های گویشی مانند pāžna (گورانی)، پاژنه/pehnî (کردی) و paşne (زازاکی) نیز میراثی‌اند نه وام‌واژه. معین در فرهنگ فارسی برابر این مدخل نشانهٔ [په.] (پهلوی) گذاشته است. نمودار برای این گره ارجاعی نداده و نیازی هم نیست؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B4%D9%86%D9%87\",\n            \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B4%D9%86%D9%87/\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tp%E1%B8%97rsneh%E2%82%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi s.v. پاشنه (via abadis)\", \"stance\": \"supports\", \"note\": \"'(نِ) [ په. ] (اِ.) ۱ - بخش عقب پای آدمی، پاشنا، عقب ...' — the bracketed [په.] marks the word as inherited from Pahlavi.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 276 (HRN.txt l.2728)\", \"stance\": \"supports\", \"note\": \"'276. pāšne \\\"Ferse\\\". aw. pāšna-; phlv. pāšnak'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §124a (HUB.txt l.8611)\", \"stance\": \"supports\", \"note\": \"'pāšna \\\"Ferse\\\" = phl. pāšnak, zd. pāšna-'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. pāšnag (PHD.txt l.545)\", \"stance\": \"supports\", \"note\": \"'pāšnag [p'šnk' | N ~a] heel' — the '| N ~a' is MacKenzie's note of the New Persian form پاشنه.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no headword پاشنه in Aryanpur's IE-root dictionary.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"pšn`\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Manichaean and Christian Sogdian pšnʾ (pašnā) 'heel' is the Sogdian reflex of the same Proto-Iranian *pāršni-/*pāšna-; Gharib registers it with the explicit note '<Av. pāšna, f. acc.' and cites the Christian Sogdian text C2 51v13 and Bailey's Prolexis 183. The Sogdian short a for Avestan ā is the ordinary result of the Sogdian rhythmic-law shortening in a heavy-stem noun.\",\n          \"derivation_fa\": \"سغدیِ مانوی و مسیحیِ pšnʾ (pašnā) «پاشنه» بازتاب سغدیِ همان *pāršni-/*pāšna- ایرانی باستان است؛ غریب (شمارهٔ ۷۵۰۹) صریحاً می‌نویسد «<Av. pāšna، حالت رایی مؤنث» و به متن سغدی مسیحی C2 ۵۱v۱۳ و «پرولکسیس» بیلی ص ۱۸۳ ارجاع می‌دهد. کوتاه‌شدن ā اوستایی به a در سغدی نتیجهٔ قانون آهنگین (rhythmic law) سغدی است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:301\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary entry 7509, on the leaf whose printed page computes to 301 (SOD_pages.txt leaf 367, printed = leaf − 66; the page numeral printed at the foot of that block reads 302, so Nourai is within one page): '7509 psnʾ M, C | pašna ©<Av. pāšna ©f. acc. | heel | BSTii: C2, 51v13 n p98; Bailey, Prolexis, 183'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib no. 7509 (p. 301/302)\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"BRT\", \"where\": \"s.v. pāšna- (BRT.txt l.16060)\", \"stance\": \"supports\", \"note\": \"gives the Avestan etymon Gharib refers to.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 823\", \"stance\": \"silent\", \"note\": \"Pokorny lists no Sogdian under persnā.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"perna; pernula\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin perna f. 'a haunch or ham with the leg, gammon' and, by shape-metaphor, 'a kind of sea mussel' is the regular Italic reflex: PIE *tpḗrsneh₂ > Proto-Italic *persnā > perna, with -rsn- > -rn- and compensatory lengthening (de Vaan 2008, 460-461). Nourai's two glosses are both classical. The second word is weaker: pernula 'pearl' is not classical Latin but a Low-Latin diminutive first attested in the 7th century (Skeat), and modern dictionaries treat Vulgar Latin *pernula as a reconstruction — Etymonline: Medieval Latin perla is 'of unknown origin. Perhaps from Vulgar Latin *pernula, diminutive of Latin perna, which in Sicily meant \\\"pearl\\\", earlier \\\"sea-mussel\\\"'. So 'perna' is confirmed, 'pernula: pearl' is only the most popular of several theories; hence the node as a whole is plausible rather than confirmed.\",\n          \"derivation_fa\": \"لاتین perna (مؤنث) «ران و کپل خوک، ژامبون» و به قیاس شکل «نوعی صدف دریایی» بازتاب منظم ایتالیایی آغازین *persnā < هندواروپایی *tpḗrsneh₂ است؛ خوشهٔ -rsn- به -rn- بدل شده و واکه کشیده شده است (دِ ڤان ۲۰۰۸، ص ۴۶۰–۴۶۱). هر دو معنایی که نورایی آورده در لاتین کلاسیک هست. اما واژهٔ دوم سست‌تر است: pernula «مروارید» لاتین کلاسیک نیست، بلکه مصغّری در لاتین متأخر است که نخستین بار در سدهٔ هفتم میلادی دیده می‌شود (اسکیت) و فرهنگ‌های امروزی *pernula را صورتی بازسازی‌شده در لاتین عامیانه می‌دانند. پس «perna» قطعی و «pernula: مروارید» تنها محتمل‌ترین فرضیه است و این گره «با احتیاط پذیرفتنی» ارزیابی می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/perna\",\n            \"https://www.etymonline.com/word/pearl\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985, IE roots appendix s.v. persna (AHD_watkins1985.txt l.844): 'persna. Heel. Latin perna, ham, leg, sea mussel: PEARL. [Pok. persna 823.]', and the word-index line 'PEARL! persna' (l.2069). Nourai's bare 'AHD' citation is exactly this entry — AHD is itself the modern standard here. Watkins does not spell out the intermediate pernula.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. pearl (KLN_1966.txt l.27779)\", \"stance\": \"partial\", \"note\": \"'L. perna stands for *persna and is cogn. with OI. pārṣṇiḥ \\\"heel\\\", Avestic pāšna-, Gk. πτέρνη, Goth. fairzna ...' — the root connection agreed; but Klein derives perla from a blend of perna with sphaerula, not from pernula.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Pearl (SKT.txt l.13576)\", \"stance\": \"partial\", \"note\": \"'Of disputed origin; ... Low L. pernula (7th cent.). Prob. put for L. pirula, i.e. a little pear, from L. pirum, a pear' — Skeat confirms that pernula exists (7th c.) but prefers pirula.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 823\", \"stance\": \"partial\", \"note\": \"'lat. perna f. (*persnā) ,Hinterkeule, Schweineschinken, Schenkel, Bein', pernīs ,schnell'' — has perna from the root but gives no 'sea mussel' or 'pearl' sense.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.37 (SYN.txt l.6248)\", \"stance\": \"supports\", \"note\": \"'Sp. pierna, fr. Lat. perna \\\"ham, haunch\\\" (esp. of pork) : Grk. πτέρνα \\\"heel, ham\\\" ...'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"pearl\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English pearl is Middle English perle (early 14c., as a surname mid-13c.) from Old French perle (13c.) and directly from Medieval Latin perla (mid-13c., alongside Italian/Spanish/Provençal perla, Portuguese pérola). The step that makes Nourai's arrow work is perla < Vulgar Latin *pernula, diminutive of perna 'sea mussel' — named from the ham-shaped shell of the Pinna mussel, and Latin perna did mean 'pearl' in Sicily. Watkins/AHD prints this chain without hedging ('Latin perna ... : PEARL'), but Etymonline calls Medieval Latin perla 'of unknown origin' and lists rival derivations from pirula 'little pear' (so Skeat) and pilula 'globule'; Klein makes perla a blend of perna and sphaerula. The Romance chain itself is uncontroversial; the Latin etymon is not, hence 'plausible'.\",\n          \"derivation_fa\": \"انگلیسی pearl از انگلیسی میانهٔ perle (آغاز سدهٔ چهاردهم میلادی) است، از فرانسهٔ کهن perle و مستقیماً از لاتین قرون وسطایی perla (میانهٔ سدهٔ سیزدهم)، همراه با ایتالیایی/اسپانیایی perla و پرتغالی pérola. حلقه‌ای که پیکان نورایی به آن وابسته است اینکه perla از لاتین عامیانهٔ *pernula، مصغّر perna «صدف دریایی»، آمده باشد — نام‌گذاری از روی شکلِ ژامبون‌مانندِ صدف Pinna، و در سیسیل خودِ perna معنی «مروارید» داشته است. واتکینز (AHD) این زنجیره را بی‌تردید می‌آورد، اما Etymonline اصلِ perla را «ناشناخته» می‌داند و از گزینه‌های رقیب pirula «گلابیِ کوچک» (نظر اسکیت) و pilula «گویچه» یاد می‌کند و کلاین آن را آمیزهٔ perna و sphaerula می‌شمارد. زنجیرهٔ رومیایی (لاتین ← فرانسهٔ کهن ← انگلیسی) مسلّم است و تنها ریشهٔ لاتینی مورد اختلاف است؛ از این رو «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/pearl\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the parent Latin node carries his 'AHD' citation, which does name PEARL as the English descendant.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. pearl (KLN_1966.txt l.27779)\", \"stance\": \"partial\", \"note\": \"'ME. perle, fr. MF. (= F.) perle, prob. borrowed fr. It. perla, fr. VL. *perla, ... which is a blend of L. perna, \\\"ham, sea mussel, pearl\\\", and sphaerula, \\\"a small ball\\\"' — same Latin base, different mechanism.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Pearl (SKT.txt l.13576)\", \"stance\": \"contradicts\", \"note\": \"'Of disputed origin ... Low L. pernula (7th cent.). Prob. put for L. pirula, i.e. a little pear.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. persna and index 'PEARL! persna'\", \"stance\": \"supports\", \"note\": \"'Latin perna, ham, leg, sea mussel: PEARL.'\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict., vol. 1 (A–?) only on disk\", \"stance\": \"silent\", \"note\": \"'pearl' falls in the missing volume 2; could not be consulted.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Pestěno\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *pstḗn / *pstén-o-s 'breast, teat' (Pokorny 'p(ə)stə̄no-', p. 990)\",\n      \"note\": \"Pokorny I 990 heads the entry 'spenə-, st(h)ə̄no-, p(ə)stə̄no- ,Zitze, Brustwarze, Brust'' and its section 2 gives 'mpers. np. pistān \\\"weibliche Brust\\\" (*pəstāna-), av. fštāna- m. Du. \\\"ds., Brustwarze, Knoten\\\" (*pstāna), ... ai. stána- ..., arm. stin', ending 'Die Vereinigung der Anlaute unter p(ə)st-in- scheint möglich.' So Nourai's root name, language label, gloss and page are all right; the modern shape is Wiktionary's *pstḗn / *pstén-o-s > PII *pstānás > PIr *pstānáh. The one problem inside the entry is the Greek node: Pokorny, on the very page Nourai cites, calls the connection of στῆθος with this root 'schwer glaublich' (see node #4).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *pstḗn / *pstén-o-s «پستان، سینه». پوکورنی (جلد ۱، ص ۹۹۰) مدخل را چنین آورده است: spenə-, st(h)ə̄no-, p(ə)stə̄no- «نوکِ پستان، پستان، سینه»، و در بند دوم می‌نویسد «فارسی میانه و فارسی نو pistān «پستان زن» (< *pəstāna-)، اوستایی fštāna- (< *pstāna)، سنسکریت stána-، ارمنی stin». پس نام ریشه، برچسب زبانی، معنا و شمارهٔ صفحه در نمودار درست است؛ صورت امروزی آن در ویکی‌واژه *pstḗn > هندوایرانی *pstānás > ایرانی باستان *pstānáh است. تنها مشکل این مدخل گرهٔ یونانی است که خودِ پوکورنی در همان صفحه پیوند آن را «به‌سختی باورکردنی» خوانده است (بنگرید به گرهٔ ۴).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pst%E1%B8%97n\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:990\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 230 (printed p. 990): 'spenə-, st(h)ə̄no-, p(ə)stə̄no- ,Zitze, Brustwarze, Brust'. ... 2. mpers. np. pistān ,weibliche Brust' (*pəstāna-), av. fštāna- m. Du. ,ds., Brustwarze, Knoten' (*pstāna) ... WP. II 663.' Root name and gloss are Nourai's source verbatim.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"Bd. I p. 990\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann s.v. psténos (IEC.txt, p. 1004-1005 block)\", \"stance\": \"supports\", \"note\": \"'psténos, ios, iom \\\"nipple, breast\\\". Cf. spén-. Skt. cf. stánaḥ ...; Av. fstana, dual. id.; Per. pistan, id.; Oss. fəzdon \\\"udder\\\"; Arm. stin ...; Tokh. A pāssāṃ, B päścane; Hes. stēnion' — the same root with the same Iranian members.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.41 (SYN.txt l.6433)\", \"stance\": \"supports\", \"note\": \"'Skt. stana-, Av. fštāna- (NPers. pistān) : Arm. stin \\\"woman's breast\\\", Grk. στήνιον στῆθος (4.40), perh. also OE spane, OPruss. spenis \\\"teat\\\", etc., with orig. init. pst-. Walde-P. 2.663.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"Watkins has no root for 'breast/teat' of this shape (no *psten-/*spen- entry); absent, not contradicting.\"},\n        {\"src\": \"WLD\", \"where\": \"WP II 663 (cited by Pokorny)\", \"stance\": \"silent\", \"note\": \"Bände I–II of Walde-Pokorny are not in the local library.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"fštâna\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan fštāna- m. 'woman's breast' (dual), also 'the swelling of the breast round the nipple' and, in compounds, 'boss, knot'; attested e.g. Yt. 5.127 yaθaca hukərəpta fštāna 'and as (she had) well-shaped breasts'. It goes back to PIr *pstāna- < PII *pstānás < PIE *pstén-o-s; Avestan regularly turns the initial *p before a voiceless stop/sibilant cluster into the fricative f (pst- > fšt-), and *st > št after the labial. Nourai's 'fštâna' is the standard form with â for ā.\",\n          \"derivation_fa\": \"اوستایی نو fštāna- (مذکر، غالباً دوگانه) «پستانِ زن»، و نیز «برآمدگی سینه پیرامون نوک پستان» و در ترکیب «گره، برجستگی»؛ نمونه: یشت ۵٫۱۲۷ «yaθaca hukərəpta fštāna» یعنی «و پستان‌های خوش‌ریخت». این واژه از ایرانی باستان *pstāna-، از هندوایرانی *pstānás و هندواروپایی *pstén-o-s است؛ در اوستایی p آغازی پیش از خوشهٔ ناهمخوان به سایشیِ f بدل می‌شود (pst- > fšt-) و s نیز به š. نگارش نورایی درست و ادعای او پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pst%E1%B8%97n\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:990\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 230: 'av. fštāna- m. Du. ,ds., Brustwarze, Knoten' (*pstāna), drəδwafsnyā ,der hochbusigen''.\"},\n            {\"ref\": \"KLN:1513\", \"status\": \"supports\", \"note\": \"Klein 1966, p. 1513 s.v. stetho- (KLN_1966.txt l.36771, between the page numerals 1513 at l.36745 and 1514 at l.36787): 'Gk. στῆθος, \\\"breast\\\", prob. cogn. with OI. stanaḥ, \\\"teat, nipple\\\", Avestic fshtāna-, Arm. stin, of s.m.' — Klein lists exactly Nourai's Avestan form under this root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. s.v. fštāna- (BRT.txt l.18421)\", \"stance\": \"supports\", \"note\": \"'j. fštāna- m. 1) \\\"weibliche Brust\\\", Du.: ... yaθaca hukərəpta fštānaya-ca aŋhən nivāzāna Yt.5.127; 2) \\\"Wölbung der Brust\\\", um die Brustwarze herum ...; 3) \\\"Buckel, Knoten\\\" (nur Komp.).'\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 990\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.41 (SYN.txt l.6433)\", \"stance\": \"supports\", \"note\": \"'Skt. stana-, Av. fštāna- (NPers. pistān)'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"pestân «پستان»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian پستان pestān/pistān 'breast' comes from Middle Persian pestān [pystʾn'], which MacKenzie lists with the New Persian continuation marked. The Persian form is not a descendant of the Avestan word but its South-West sister: Proto-Iranian *pstānáh gave Avestan fštāna- with f-, but in the Persian branch the initial cluster was broken by an anaptyctic vowel instead, *pəstāna- > MP pestān > NP pestān, which is exactly Pokorny's note '(*pəstāna-)' and Hübschmann's suggestion that 'pistān (aus *pəstāna-?) zu fštāna- (aus *pstāna-) wie zd. pitar- zu zd. ptar-'. So the arrow Avestan → Persian is a shortcut (sister, not mother) and the Middle Persian stage is missing from the chart, but the root membership and the word itself are beyond doubt; Mo'in's own footnote in Borhan-e Qāte' gives the same chain including the Pahlavi step.\",\n          \"derivation_fa\": \"«پستان» در فارسی نو از فارسی میانهٔ pestān (نوشتار pystʾn') است که مکنزی با اشارهٔ «| N ~» به دنبالهٔ فارسی نو ثبت کرده است. اما این واژه فرزندِ صورت اوستایی نیست، بلکه خواهرِ جنوب‌غربیِ آن است: ایرانی باستانِ *pstānáh در اوستایی با سایشی‌شدن p به fštāna- بدل شد و در شاخهٔ پارسی خوشهٔ آغازین با واکهٔ میانجی شکسته شد: *pəstāna- > pestān فارسی میانه > «پستان». همین را پوکورنی با نشانهٔ «(*pəstāna-)» و هوبشمان با قیاس «pitar- در برابر ptar- اوستایی» گفته‌اند. پس پیکان «اوستایی ← فارسی» میان‌بُر است و حلقهٔ فارسی میانه در نمودار افتاده است، ولی اصل ریشه‌شناسی درست است و حاشیهٔ معین بر برهان قاطع نیز همین زنجیره را با حلقهٔ پهلوی می‌آورد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D8%A7%D9%86\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pst%E1%B8%97n\",\n            \"https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%AA%D8%A7%D9%86/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:990\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 230: 'mpers. np. pistān ,weibliche Brust' (*pəstāna-)' — Pokorny puts the Persian word under the root and notes the anaptyctic reconstruction, but he does NOT derive it from the Avestan form.\"},\n            {\"ref\": \"BQT:405\", \"status\": \"supports\", \"note\": \"Borhan-e Qāte' (Mo'in's ed.) vol. 1, leaf 629 of BQT_v1_pages.txt = printed p. ~405-407: the entry 'پستان - بکسر اول' carries Mo'in's footnote listing (OCR partly garbled but the sequence is legible) 'اوستا fštāna (پستان). پهلوی pstʾn / pestān، هندی باستان stana، ارمنی stin ...' — i.e. exactly Nourai's chain, with a Pahlavi link the chart omits.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. pestān (PHD.txt l.549)\", \"stance\": \"supports\", \"note\": \"'pestān [pystʾn' | N ~] breast.'\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 317 (HRN.txt ll.3032-3035)\", \"stance\": \"supports\", \"note\": \"'317. pistān \\\"Brust (der Frau)\\\". aw. fštāna- \\\"Brust\\\"; phlv. p(i)stān (Vd. 9 (71)), pistān ... LW. afγ. pistān.'\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p. 186 n. 2 (HUB.txt ll.6597-6598)\", \"stance\": \"partial\", \"note\": \"'Wie aber verhält sich np. pistān \\\"Brust\\\" zu zd. fštāna-? ... Etwa pistān (aus *pəstāna-?) zu fštāna- (aus *pstāna-) wie zd. pitar- zu zd. ptar-?' — same root, but Hübschmann explicitly makes the two parallel developments, not one from the other.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi s.v. پستان (via abadis)\", \"stance\": \"silent\", \"note\": \"'(پِ) (اِ.) اندامی در پستانداران که در جنس ماده دارای غده های تراوش شیر است' — meaning only, no origin tag in the online text.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no headword پستان in Aryanpur.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`štnh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Buddhist Sogdian ʾštnh (ōstānē/əštāna) 'breast' continues Proto-Iranian *pstānáh as a sister of Avestan fštāna- and Persian pestān — the chart is right to hang it directly from the root rather than from the Avestan node. The Sogdian form shows the usual prothetic ʾ- before the old initial cluster and loss of the labial (*pst- > ʾst-/ʾšt-). Gharib's dictionary prints the transliteration ʾstnh with s, Wiktionary ʾštnh with š (the Sogdian script letters differ); Nourai's spelling agrees with Wiktionary, so it is a transliteration convention, not a misreading. Gharib's own note is 'Av. fštana; Skt. stana', i.e. exactly this root.\",\n          \"derivation_fa\": \"سغدیِ بودایی ʾštnh «پستان» دنبالهٔ همان ایرانی باستانِ *pstānáh است و خواهرِ fštāna- اوستایی و «پستان» فارسی به شمار می‌رود؛ بنابراین درست است که نمودار آن را مستقیماً از ریشه گرفته و نه از گرهٔ اوستایی. در سغدی پیش از خوشهٔ آغازین الفِ پیشین (prothetic) افزوده شده و همخوان لبی افتاده است (*pst- > ʾst-/ʾšt-). غریب در فرهنگ سغدی آوانگاشت را با s می‌نویسد (ʾstnh) و ویکی‌واژه با š (ʾštnh)؛ نگارش نورایی با ویکی‌واژه می‌خواند، پس اختلاف در سنت آوانگاری است نه خطای خوانش. یادداشت خودِ غریب «Av. fštana؛ Skt. stana» است، یعنی همین ریشه.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pst%E1%B8%97n\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:70\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary entry 1785, on the leaf whose printed page computes to 69-70 (SOD_pages.txt leaf 135, printed = leaf − 66): '1785 ʾstnh B | ōstānē ©Av. fštana; Skt. stana | breast | VJ 6a, 1208; GMS 314 n 1'. Page and meaning match Nourai; his š for Gharib's s is a transliteration variant (Wiktionary writes ʾštnh).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib no. 1785 (p. 69/70)\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"BRT\", \"where\": \"s.v. fštāna- (BRT.txt l.18421)\", \"stance\": \"supports\", \"note\": \"supplies the Avestan comparandum Gharib cites.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 990\", \"stance\": \"silent\", \"note\": \"Pokorny lists no Sogdian under p(ə)stə̄no-.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"sthĕthos\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"Two things are wrong here, one certainly and one arguably. (a) The form: the Greek word is στῆθος stēthos 'chest, front of the chest', with st- and a long ē; 'sthĕthos' (σθηθος, with an aspirate in the first syllable and a short e) is not a possible Greek word. I rendered pdf page 399 at 300 dpi and read the box: the printed page itself has 'sthěthos', so the extraction is faithful and the misprint is Nourai's. (b) The derivation: Nourai hangs stēthos on this root citing POK:990, but on that very page Pokorny writes 'gr. στήνιον· στῆθος Hes. (daß στῆθος verwandt sei, ist schwer glaublich...)' — i.e. the Greek member of the root is the Hesychian gloss στήνιον, and Pokorny explicitly doubts στῆθος. The cited reference therefore contradicts the arrow. The connection is not dead, though: Klein (the other reference Nourai gives here, KLN:1513) states it as probable, Buck 4.41 lists 'Grk. στήνιον στῆθος' together, Mann says 'the initial may be represented also in the synth. Gk. cpds. stéthos, stérnon', and Wiktionary's *pstḗn page says 'possibly related with Ancient Greek στῆθος'. Etymonline instead links stēthos to sternon, and Beekes leaves it without etymology. So the substance is 'accepted by some, doubted by others'; the flag on this node is the printed form.\",\n          \"derivation_fa\": \"در این گره دو اشکال هست. نخست صورت واژه: واژهٔ یونانی στῆθος (stēthos) «سینه، جلوِ سینه» است با st- و ē کشیده؛ «sthěthos» (یعنی σθηθος با دمیدگی در هجای نخست و e کوتاه) واژه‌ای ناممکن در یونانی است. صفحهٔ ۳۹۹ نسخهٔ پی‌دی‌اف را با تفکیک ۳۰۰ نقطه بازنمایی کردم و در جعبهٔ «Greek» همان «sthěthos» چاپ شده است؛ پس خطای خوانشِ اسکن نیست، خطای چاپی خودِ کتاب است. دوم ریشه‌شناسی: نورایی این واژه را با ارجاع به POK:990 به این ریشه بسته، حال آنکه پوکورنی در همان صفحه می‌نویسد «στήνιον· στῆθος (هزیخیوس) — اینکه στῆθος هم‌ریشه باشد به‌سختی باورکردنی است»؛ یعنی عضو یونانیِ این ریشه στήνιον است نه στῆθος و منبعِ مورد استنادِ خودِ نویسنده این پیکان را رد می‌کند. با این حال پیوند یکسره مردود نیست: کلاین (همان KLN:1513 که نورایی آورده) آن را «محتمل» می‌داند، باک در بند ۴٫۴۱ «στήνιον στῆθος» را کنار هم می‌آورد، مان می‌گوید همخوان آغازین شاید در ترکیب‌های یونانی stéthos و stérnon نیز بازتاب یافته باشد، و ویکی‌واژه نیز آن را «احتمالاً مرتبط» می‌خواند؛ در مقابل Etymonline آن را به sternon می‌بندد و بیکس آن را بی‌ریشه‌شناسی رها می‌کند. پس در محتوا «با احتیاط پذیرفتنی» است و آنچه در اینجا نشانه‌گذاری می‌شود خطای چاپی کتاب است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"sthěthos\",\n          \"correct_form\": \"stēthos (στῆθος)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CF%83%CF%84%E1%BF%86%CE%B8%CE%BF%CF%82\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pst%E1%B8%97n\",\n            \"https://www.etymonline.com/word/stethoscope\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:990\", \"status\": \"contradicts\", \"note\": \"POK_03.txt leaf 230 (printed p. 990), section 2 of the root: 'gr. στήνιον· στῆθος Hes. (daß στῆθος verwandt sei, ist schwer glaublich; hat neben στήνιον, στήνη einst ein *θη-θος, στη-θος bestanden ...??)'. The Greek member Pokorny admits is στήνιον; he calls the στῆθος connection hard to believe.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 1513 s.v. stetho- (KLN_1966.txt l.36771)\", \"stance\": \"supports\", \"note\": \"'stetho-, combining form meaning \\\"breast, chest\\\", as in stethoscope. — Gk. στηθο-, fr. στῆθος, \\\"breast\\\", prob. cogn. with OI. stanaḥ, \\\"teat, nipple\\\", Avestic fshtāna-, Arm. stin, of s.m.'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. psténos (IEC.txt p.1004-1005 block)\", \"stance\": \"partial\", \"note\": \"'The initial may be represented also in the synth. Gk. cpds. stéthos, stérnon & Dor. stētha' — admitted only as a possibility.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.41 (SYN.txt l.6433)\", \"stance\": \"supports\", \"note\": \"'Grk. στήνιον στῆθος (4.40) ... with orig. init. pst-'.\"},\n            {\"src\": \"POK\", \"where\": \"Bd. I p. 990\", \"stance\": \"contradicts\", \"note\": \"see ref_check.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"stethoscope\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A 19th-century learned coinage, not an inherited word: French stéthoscope, coined in 1819 by its inventor, the physician René-Théophile-Hyacinthe Laënnec (1781–1826), from Greek στῆθος 'chest' + -σκόπιον (σκοπεῖν 'to look at, examine'); English stethoscope from 1820. The Greek → English arrow is therefore correct as a route of learned borrowing via French. (Whether the Greek word in turn belongs to this Indo-European root is the open question of node #4.)\",\n          \"derivation_fa\": \"«stethoscope» واژه‌ای ساختگی و دانشگاهی از سدهٔ نوزدهم است، نه واژه‌ای میراثی: فرانسه stéthoscope را در ۱۸۱۹ سازندهٔ این ابزار، پزشک فرانسوی رنه لَئِنِک (۱۷۸۱–۱۸۲۶)، از στῆθος یونانی «سینه» و -σκόπιον (از σκοπεῖν «نگریستن، معاینه کردن») ساخت و انگلیسی آن را در ۱۸۲۰ وام گرفت. پس پیکان «یونانی ← انگلیسی» در نمودار درست است و راهِ آن وام‌گیریِ دانشورانه از راه فرانسه است. (اینکه خودِ واژهٔ یونانی به این ریشهٔ هندواروپایی بازمی‌گردد یا نه، مسئلهٔ گرهٔ ۴ است.)\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/stethoscope\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1513\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 1513 (KLN_1966.txt l.36772): 'stethoscope, n., an instrument for examining the sounds produced in the body. — F. stéthoscope, lit. \\\"instrument for examining the breast\\\", coined by the French physician René-Théophile-Hyacinthe Laennec (1781-1826) in 1819 fr. Gk. στῆθος, \\\"breast\\\", and -σκόπιον, fr. σκοπεῖν, \\\"to look at, examine\\\".' Nourai's page is exactly right (the numerals 1513 and 1514 bracket this line in the scan).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. stethoscope, stetho-, stethometer (KLN_1966.txt ll.36771-36772)\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt finds no entry 'stethoscope' — Skeat's concise dictionary omits modern scientific coinages.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict. vol. 1 only on disk\", \"stance\": \"silent\", \"note\": \"'stethoscope' falls in the missing volume 2.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:09:19.594Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-399.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:09:22.370Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-399.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 399"
}
```


### [2026-09-14T01:09:23.784Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 13, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 13, 'not_checked': 3, 'partial': 1, 'contradicts': 1}
books consulted: {'supports': 38, 'contradicts': 4, 'silent': 12, 'partial': 6} | by book: {'POK': 9, 'BRT': 8, 'HUB': 5, 'SYN': 5, 'IEC': 4, 'PHD': 4, 'HRN': 4, 'KLN': 4, 'MON': 3, 'ARY': 3, 'SOD': 3, 'SKT': 3, 'NYB': 2, 'WEB': 2, 'AHD': 1}
```


## [2026-09-14T01:09:46.544Z] AGENT

Done. `verify_check.py 399` reports 0 PROBLEM lines.

**Page 399 (book p. 369) — 3 entries (1 redirect skipped), 16 nodes**

- Root verdicts: 3 confirmed (Perk 2, Persna, Pestěno — all match Pokorny 820 / 823 / 990 verbatim in name, label and gloss).
- Node verdicts: **13 confirmed, 2 plausible, 1 transcription_suspect**.
- Ref checks: 13 supports, 1 partial, 1 contradicts, 3 not_checked. Books consulted: POK, BRT, HUB, HRN, PHD, NYB, SOD, IEC, SYN, KLN, SKT, AHD, MON, ARY, WEB.

Flagged items:

- **transcription_suspect — Pestěno #4 Greek "sthĕthos"**: the Greek word is στῆθος *stēthos*; "sthěthos" is impossible Greek. I rendered pdf p. 399 at 300 dpi — the printed page itself reads `sthěthos`, so `error_in: "book"` (Nourai's misprint); the extraction is faithful. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/399.png`.
- **Same node, substantive dispute**: Nourai cites POK:990 for Greek `stēthos ← *pstēno-`, but Pokorny on that page says the opposite — "daß στῆθος verwandt sei, ist schwer glaublich"; his Greek member is στήνιον. Klein (KLN:1513), Buck 4.41, Mann and Wiktionary allow the connection; Etymonline prefers στέρνον. Recorded as `contradicts` for POK:990.
- **plausible — Persna #5 Latin "pernula: pearl"** and **#6 English "pearl"**: Latin *perna* 'ham, sea mussel' is solid (AHD/Watkins s.v. persna names PEARL), but *pernula* is Low Latin (7th c., Skeat) / reconstructed VL; Etymonline calls Med.Lat. *perla* "of unknown origin", Skeat prefers *pirula*, Klein a *perna* × *sphaerula* blend.

No extraction errors found — the JSON matches the printed page everywhere I checked (including Sogdian `štnh`, which agrees with Wiktionary's ʾštnh even though Gharib prints ʾstnh).

Notable findings worth the owner's attention:

- **Perk 2 #3 Persian pahlū**: Horn's *Grundriss* no. 342 (= the entry translated at Nourai's own AEF:415) explicitly **rejects** this derivation ("lässt sich np. pehlū lautlich nicht direkt zusammenstellen") and Mann still follows Horn; Hübschmann §342 corrected him (OP \*parθu-ka-, rθ > hl as in Parθava > Pahlav) and modern scholarship follows Hübschmann. Nourai is right, but his cited volume contains both views.
- Two chart shortcuts noted in the derivations: MP *pahlūg* and NP *pestān* descend from South-West (OP-type) forms, not from the Avestan nodes drawn as their parents; and the MP link `pestān` is missing between Avestan and Persian (Mo'in's own Borhan footnote at BQT:405 has it).
- `AEF:415` not checkable (not online, not on disk); `BQT:355` page located (vol. 1 leaves 576–577) but Mo'in's Latin-script footnote is unreadable in the OCR and vols 1–2 aren't covered by `ref_page.py`.
- `SNS:114` verified exactly: Tavoosi's index reads "pahlūg 114/3" and p. 114 prints pahlūg ← Av. parəsu- (AiWb 896).
