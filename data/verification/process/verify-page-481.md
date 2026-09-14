# Verification process log — verify-page-481


## [2026-09-14T03:08:12.985Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 481 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-481.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-481.json. Write /home/sfmqrb/git/rishe/data/verification/page-481.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 481` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:14.035Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:14.959Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:14.976Z] TOOL RESULT

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


## [2026-09-14T03:08:15.399Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-481.txt"
}
```


### [2026-09-14T03:08:15.429Z] TOOL RESULT

```
1	=== PDF page 481 (book page 451) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ster 4 : barren  (refs POK:1031)
4	#1 (parent #0) [Sanskrit] refs=POK:1031 | stari : infertile, barren
5	  #2 (parent #1) [Persian] refs=BQT:1100; MON:1833 | satarvan «سَتَروَن ( استَروَن )» : sterile
6	#3 (parent #0) [Latin] refs=AHD | sterilis : unfruitful
7	  #4 (parent #3) [French] refs=None | 
8	    #5 (parent #4) [Persian] refs=MON:249 | esterîlîzeh «استریلیزه» : sterilized
9	    #6 (parent #4) [English] refs=AHD | sterile, sterilize
10	--- entry 1 ---
11	ROOT Sterp -> redirect to Ster 3
12	--- entry 2 ---
13	ROOT [Indo-European] Steu 1 : to praise  (refs POK:1035)
14	#1 (parent #0) [Avestan] refs=POK:1035 | stav : to praise ; staoiti : praised
15	  #2 (parent #1) [Pahlavi] refs=BQT:747,1098; SNS:31 | stâyîtan : to praise ; âstvân : believer, trusted ; âstôbân : confessor
16	    #3 (parent #2) [Persian] refs=BQT:1101; HRN:159; NYB:180; SNS:31; MON:261 | setâyîdan «سِتایِدَن (ستایش، ستودن)» : to praise ; ostovân «اُستوان ۱ (ستوان ۱)» : believer, confessor ; xastŭ «خَستو۲ (خستوان)» : believer, confessor
17	
```


## [2026-09-14T03:08:18.101Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-481.json",
 "description": "Read source JSON for page 481"
}
```


### [2026-09-14T03:08:18.142Z] TOOL RESULT

```
{
  "pdf_page": 481,
  "book_page": 451,
  "entries": [
    {
      "root": {
        "name": "Ster 4",
        "lang": "Indo-European",
        "refs": "POK:1031",
        "gloss": "barren"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:1031",
          "words": [
            {"translit": "stari", "gloss": "infertile, barren", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1100; MON:1833",
          "words": [
            {"translit": "satarvan", "gloss": "sterile", "script": "سَتَروَن ( استَروَن )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "sterilis", "gloss": "unfruitful", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:249",
          "words": [
            {"translit": "esterîlîzeh", "gloss": "sterilized", "script": "استریلیزه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "sterile, sterilize", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sterp",
        "redirect": "Ster 3"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Steu 1",
        "lang": "Indo-European",
        "refs": "POK:1035",
        "gloss": "to praise"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1035",
          "words": [
            {"translit": "stav", "gloss": "to praise", "script": null},
            {"translit": "staoiti", "gloss": "praised", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:747,1098; SNS:31",
          "words": [
            {"translit": "stâyîtan", "gloss": "to praise", "script": null},
            {"translit": "âstvân", "gloss": "believer, trusted", "script": null},
            {"translit": "âstôbân", "gloss": "confessor", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1101; HRN:159; NYB:180; SNS:31; MON:261",
          "words": [
            {"translit": "setâyîdan", "gloss": "to praise", "script": "سِتایِدَن (ستایش، ستودن)"},
            {"translit": "ostovân", "gloss": "believer, confessor", "script": "اُستوان ۱ (ستوان ۱)"},
            {"translit": "xastŭ", "gloss": "believer, confessor", "script": "خَستو۲ (خستوان)"}
          ],
          "note": null,
          "quote": {
            "text": "تو خَستو شو آنرا كه هست و یكیست - روان و خرد را جز این راه نیست",
            "poet": "Ferdowsî"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-14T03:08:20.452Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','BQT','MON','HRN','NYB','SNS','WLD','PHD','HUB','KLN','IEC','SYN','BRT','ARY','CHEUNG','SKT','WEB','FSD']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T03:08:21.540Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG MISSING
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-09-14T03:08:26.091Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80; echo ---; sed -n '1,80p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T03:08:26.152Z] TOOL RESULT

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
KNT_full.txt
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


## [2026-09-14T03:08:28.095Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','NYB','SNS','BRT','PHD','MON','BQT','AHD','IEC','SYN','WLD','ARY','HUB']:\n    v=d[k]; print('==',k, v.get('local_file'), '|offset:', v.get('page_offset'), '|hint:', str(v.get('lookup_hint'))[:300])\n\""
}
```


### [2026-09-14T03:08:29.195Z] TOOL RESULT

```
== POK /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt |offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== HRN /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== NYB /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt |offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== SNS ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] |offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image |hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== BRT /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt |offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt |offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== MON ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== BQT ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== AHD /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== IEC /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt |offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt |offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== WLD ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] |offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). |hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== ARY ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] |offset: printed page = pdf page + 1 |hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== HUB /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt |offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
```


## [2026-09-14T03:08:31.586Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T03:08:31.645Z] TOOL RESULT

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


## [2026-09-14T03:08:32.341Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==1039' POK_02.txt | head -60"
}
```


### [2026-09-14T03:08:33.410Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:08:38.206Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 103[0-9]\" POK_full.txt | head -30"
}
```


### [2026-09-14T03:08:38.273Z] TOOL RESULT

```
82764:Page(s): 1031-1032 
82917:Page(s): 1032-1034 
83215:Page(s): 1036-1037 
83273:Page(s): 1037-1038 
83365:Page(s): 1039-1040 
84594:Page(s): 1038-1039
```


## [2026-09-14T03:08:39.313Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 265 266 267 268 269 270 271 272 273; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_03.txt | head -12; done"
}
```


### [2026-09-14T03:08:40.248Z] TOOL RESULT

```
=== leaf 265 ===
m,  wacker' ;  alb.  shterr  {*ster-n-)  ,lege  trocken,  mache  TerfH über  strenä  , gutes  Vorzeichen'   s.  WH.  II  601 ;   lat.   consternöy exsternö  ,bestürzen,  aus  der  Fassung  bringen',  sternäx  , scheu,
cymr.  trin  ,Mühe,  Kampf  {*strenä?)]
germ.  *stara-  ,starr,  bes.  vom  Auge'  in  mnl.  star  m.  , Starrheit  des' ahd.  stara-hlint,  ags.  stcßr[e)hlind  , star  blind',  aisl.  stara,  ags.  starU Staren  ,starren,  stieren';  mit  -rr-  (aus  -rn-)  aisl.  st^rr  f.  ,Carex*  (« Steife'),   starr  (Akk.   starran)  ,steif,   starr,  hart',   nhd.   starr,  inhc nhd.  bair.  sterr  ,starr,  steif,  wovon  mhd.  starren,  sterren  , starr  seil werden',  nhd.  erstarren^  starren,  norw.   stara   und   sterra  {*starriam sträuben,  sich  anstrengen';  *sturra-  (*sturna-)  ,sich  steif  aufricbtenc mend'  in  got.  and-staürran  ,unmutig  sein',  ahd.  storren  , steif  herai hervorragen',  ahd.  storro  , Baumstumpf,  Klotz',  nhd.  st'örrig,  störrui stieme   ,ernst,    hart,   streng',    ahd.    stornen   , stutzen,   ersclirecken*  •  i starr  vor  Schrecken'),  sturni  ,stupor',  schwed.  sturna  , stutzen';
aisl.  stirdr  , steif,  unbeugsam,  hart,  unfreundlich';
apr.    stüriiawlskan   Instr.    Sg.    , Ernst',   stürnawingisku   Adv.    ,ei stürm- tickröms  , eifrig';  lit.  starinü,  -inti  , steif  machen';
russ.  stardthsja  ,sich  abmühen' ;  mit  Ablaut  *strö-  (zu  (jTgr]-vrjgj  si und  DentaUormans :    aksl.   strada  , harte   Arbeit,   Mühe',   stradati dazu  aksl.  strasth  ,Leid'  {*strad-t'b),  lett.  struostet  ,bedrohen';  mit  Ffl -mo-  vermutlich  aksl.   strhmo  ,steil,   abschüssig',   ablaut.    poln.   sti (Trautmann  290,  Vasmer  3,  25).
1023
4   Qutturalerweiterungen:
(s)ter'g-  und  {s)tre-g-:
\isl.  V^vii'z.  storhinn  ,geroniieii;  erstarrt^;  got.  ga-staürknan  ^erstarren',
-.1  storkna  .gerinnen^  ahd.  Jci-,  er-storchanen   ,erstarren,   erkalten';   nhd.
^«irol-  ^^^^^  , Knorren,   Stumpf  eines   Baumes*,   bair.   stork  , Fischerstange*,
=== leaf 266 ===
gs.  strec-
I  ^in , ausstrecken';  vgl.  noch  ^re^-  ,die  Kräfte  anstrengen';
lett.  terglis  , eigensinniger,  störrischer  Mensch^,  tergläties  ,sich  auf  etwas Versteifen';
lit.  strSgti  ,erstarren,  zu  Eis  werden';  unsicher,  ob  dazu  abg.  strachz. Schrecken'  als  *strögso-j  vgl.  Vasmer  3,  23;
vielleicht  beruht  auf  (s)terg-:  lat.  tergus,  -oris  ,harte  Rückenhaut  der Piere,  Fell,  Rücken'  (wohl  von  dem  am  Rücken  am  stärksten  gesträubten [aare),  tergum  ,ds.,  bes.  Rücken*,  terglnum  ,Peitsche  aus  Leder*;
hierher  vielleicht  als  nasalierte  Form  strenk-,  streng-^  s.   dort.
{s)ter-k-:
klr.   storcdtyj  storcity  ,ragen,  starren',   torSdtij   torHty  ds.,   öech.   strceti^ \ttieti  ds.
2,  Dentalerweiterungen:
(s)ferf-,  richtiger  *ster-to-  in  cymr.  serth  ,steil,  obszön*,  aisl.  stirdr  , steif [(«.  oben)  und  storcC  ,Gras,  grüner  Stengel';
(s)terd-:
aisl.  stertr  , Schwanz',  ags.  steort,  ahd.  sterz  ds.,  mhd.  auch  , Stengel, [Stiel'  (wie  engl,  start),  nhd.  Sterz  ]  ablaut.  norw.  dial.  start  , steifer  Zweig, [itumpf*,  mhd.  stürzel  ,Stengel*;  aisl.  wp'p-stertr  , hochmütig',  aisl.  sterta [i>pannen',  mhd.  sterzen  (auch  st.  Verb.)  ,steif  emporragen,  sich  rasch  be- ^e^en',  trans.  (auch  starzen)  ,starr  aufwärtsrichten',  mengl.  sterten  ,auf- 'fc^hren,  erschrecken',  engl,  start;  aisl.  stirtla  , aufrichten*,  ags.  steartlian »«tolperu',  engl,  startle  ,vor  Schreck  auffahren';  westgerm.  *sturtjan,  ahd.
=== leaf 267 ===
 Stamm  eines  Baumes  (übertr.  Nachkommenschaft,  ÜrfOftä«
lit.  stirpti  , etwas  emporkommen,  heranwachsen'  (eig.  ,*sich^  ttnül< sterptis  ,auf  seinem  Rechte  bestehen'  (,sich  versteifen'),  stürplis^*^^^, des  Pferdes*;  1^*
alb.  shterpe  ,unfruchtbar*  (vgl.  auch  6.  ster-  ,unfruchtbar') ;  ir.  $tt^ »Füllen^  (von  den  langen  Beinen);  *^^
ohne  S-:   torpeö,  -ere  , starr,   gefühllos,   betäubt  sein*  (=  abg.'H-fFiip oder  =  russ.  toropeth)]  lit.  tirpti  , erstarren,  gefühllos  werden',  lett  ftf|>iiilf
serb.-ksl.  utrbpäti  ,erstarren*,  russ.  terpnuth  ,ds.,  auch  vor  Furcht*,  f/ terpkij  „aiiarrjQÖg^ ,  r.  terpkij  ,herb,  sauer^ ;  russ.  toropeth,  otoropith  fh^lSM werden*  (Trautmann  Bsl.  Wb.  325),  klr.   toröpa  , unbeweglicher slov.  träp  ,Dummkopf*;  auf  der  Bedeut.  ,starr,  steif  =  ausdauei beruht  wohl  aksl.  trhpHi  ,leiden',  russ.  terpeth  ds. ;  urslav.  *torpitx in  cech.  trdpiti,  apoln.  tropic  ,quälen*,  russ.  toropith  ,antreiben*; stumpf,  vom  Standpunkte  des  Geschmacks' :  aksl.  *trbp^k^  ,acerbi russ.   terpkij  ,herb,   sauer*,   wie  np.   turus  , sauer'  (wenn  aus  *^j nhd.  derb  (s.  unten).
Teils  auf  {s)terp-,  teils  auf  {s)terbb-  können  zurückgehen; aisl.  piarfr,   ags.    deorf,    as.    thervi,   ahd.   derhi  ,ungesäuert',  Ä derb  ,dürr,  trocken,  mager*:
mit  anlaut.  s-:  aisl.  stjarfi  m.  , Arbeit,  Mühe',  stjarfr  ,hartmäi
1025
Pferden)*;  stirfinn  ,halsstarrig^,  starf  n.  , Arbeit,  Streben,  Amt*,  starfa  ,sich .bmüben';
•bd.  sterban  ,sterben'  (,*erstarren' ;  s.  unten  mir.  ussarh)',  as.  sterban, jfies.  sterva,  ags.  steorfan  ds.  (engl,  starve  ,umkommen,  bes.  vor  Hunger'); Aj.  sterboy  ags.  steorfa  ,Pest';
obd.-tirol.  storfii  ,Strunk,  Baumstumpf,  westfäl.  storpeln  , straucheln' vxnneü  ^^^  einer  Wurzelform  auf  b  beruhen.
strep'-' :  Ijit.  par-strajpmti  ,heimtorkeln',  strypti  , trampeln',  stripinys,  sträipis j^tersprosse' ;  spätmhd.  straf  {-ff-)  , straff,  strenge',  wfläm.  straf  {*strepo-) fjl^k,  kräftig,  streng',  ostfries.  strabben  ,sich  widerspenstig  gebärden*, j.  strabbeln  , zappeln';  Schweiz,  strapfen  ,straff  ziehen*  {*strappön)'^ ibl  als  jStreng  behandeln'  hierher:  afries.  straffia  ,bestreiten,  schelten*, b  mnd.  straffen,  woraus  entlehnt  mhd.  strafen,  ds.  jStrafen^y  strafe ^belte,  Tadel,  Strafe',
=== leaf 268 ===
ss.   u-strebe  Aor.   ,wurde  reif,  ksl.   strbbh  ,gesund,  fest',  russ.
hnuth  , erstarren,  absterben',  usw.  (Trautmann  284 f.,  Vasmer  3,  11  f.);
ob  die  gr.  Gruppen  von  argsßXög  ,gedrehf,  GTgeq)siv  ,drehen*,  ablaut. ßög  ,verdreht*,   OTgaßcov   , schielend',    axQoßiw   , drehe  herum',  axqocprj
endung'  usw.   aus   einer   Bed.    , straff  zusammenziehen'  (s.  unten  nhd.
iremmen   dieser   Bed.)   erklärt   werden   dürfen,    ist  höchst  fragwürdig;
ir  zu  einer  besonderen  Wurzel  streb-,  strebh-  , drehen,  winden*.
htremb-,  stremp-i
iniid.  strampe(le)n  ,mit  den  Füßen  heftig  auftreten',  nhd.  (eigent.  nd.) Mrampeln,  mnd.  strumpe(le)n  ,straucheln,  anstoßen'  u.  dgl. ;  mhd.  strumpf
Ind.  strump  ,Strumpf,  Stummel'  (nhd.  , gestutzte  Hosen,  Strumpf),  norw.
l.  strump   ,kleine    Holzschüssel   u.    dgl.'   (,*ausgehöhlter    Baumstamm',
ISO  stropp  ,ein  Maß') ;  norw.  dial.  stremba  , anspannen ;  Brust  oder  Magen
)lähen',  isl.  strembinn  , straff,  hart,  stolz',  norw.   dial.  stramb  , scharfer
=== leaf 269 ===
ndl.  struikj  mnd.  strük,  mhd.  strYich,  nhd.  Strauch ;  mhd.  strüch  ^
nisl.  striügr  , Gericht  aus  geronnener  Milch',  strüga  .rauh,  struppig aisl.  strügr  ,Widerwille,  Hochmut',  mengl.  nengl.  to  stimggle  .sich kämpfen' ;  I
lett.  strükuls  , Eiszapfen',  auch  alit.  strungas,  lit.  strügas  8triü> .kurz,  gestutzt'.
2.  Mit  Dentalerweiterungen: lit.  strustts  f.   jBaststreifen  im  Siebe';   ohne  anlaut.  s-:  nrt;
in  aksl.  trbsth  ,Rohr';   gr.   S'qvöv  n.   ,Binse'   {*truso7n)]  lit.  irü ,Rohr*,  trusts,  triusts  f.  ,Rohr,  Schilfrohr*,  lett.  trusis  .Binse, trbsuj  trzsina  ,steifes  Haar.  Borste*;  lett.  trums  ,Beule,  Geschwttr*| für  *trud-mo-,  vgl. :)  lat.  strüma  f.  .geschwollene  Drüsen,  Kropt*  V'^^ stroud-,  strüd-ma)-  nach  Vasmer  3,  145  dazu  lit.  trauHi  ,zerbrÖck^'' trausls  ,zerbrechlich',  trust  , faulen,  modern';  *^-
aisl.  strütr  ,Spitze',  dän.  strude,  strutte  ,steif  stehen,  widerstrebenfj  i^'
1027
tta  »stolpernd  geben',  ags.  strütian  , steif  stehen',  nd.  strutt  ,steif',  nhd. ^  ds.;  mhd.  nhd.  strotzen,  mhd.  striuzen  ,sträuben,  spreizen',  strüz  ,Wider- .  ^'^  Streit^  nhd.  Strauß  ds.  =  mengl.  strüt  ,das  Schwellen,  Streit'; i  hd-  strn^ach  ^Gehüsch^,  gestriuze  , Buschwerk^,  nhd.  (Blumen-) Strauß ; .j^j.jier  auch  as.  strota  ,tuba,  guttur',  mnd.  strote^  strotte  f.,  mhd.  strozze reblö;  Luftröhre',  afries.  strot-bolla  ds.;  ohne  anl.  s- :  ags.  (?ro<w,  ^ro<6;, ^jrl.  throat,  throttle  ,Kehle,  Luftröhre^,  ags.  drot-hoUa  ^Luftröhre',  (engl. Ar^üple)^  ahd.  drozza  , Kehle,  Luftröhre',  nhd.  Drossel  mit  der  Ableitung drosseln,  mhd.  drüzzel  ,Kehle'  und  , Schnauze',  aisl.  prütr  , Schnauze'; aisl.  prütinn  ,geschwollen',  prütna  ,schwellen,  auch  vor  Hochmut',  proti Anschwellung^,  ags.  drütian  ,vor  Hochmut  oder  Zorn  schwellen^; dieselben  Bedeutungen  ^schwellen,  Streit^  auch  in  mir.  trot,  nir.  troid Jgtreit^  (*truzdä7),  cymr.  trythu  , schwellen^,  trythyll  ,wollüstig^;
3.  Mit  Labialerweiterungen:
^r.  arqvcpvoQ  ,herb  (von  Geschmack);  mürrisch;  fest,  steift;
as.  strüf  , struppig,  rauh'^  strüvian  , sträuben',  mhd.  strup  {-h-),  strübe jtruppig^   ahd.   strühen,  mhd.   strühen,   *striuben   , starren',   nhd.   sträuben,
d.  strobel , struppig^,  agerm.  Strubüoscalleo  ^Strubbelkopf ;  mhd.  Strujppe
=== leaf 270 ===
e  , Stumpf^  Strauch',  strobbelen  ,strau-
In';  schwed.  strubbla  ds.;  mit  germ.  -p-  (idg.  -6-):  norw,  stroypa  ,klemmen^,
,d.  Schweiz.  stru(rn)pfen,  mnd.  strumpen  ,zusammenziehen',  struppe, JStumpf ;
aisl.  str(j)üpi  ,Kehle,  Gurgel',  norw.  strop  ,enge  Öffnung';
lit.  strübas,   lett.   stru(rn)ps   ,kurz   abgestutzt',   strubikis,  strnpikis,  stru-
tis  ,Stumpfschwanz',  lett.  strupulis  ,kurzer  dicker  Mensch ;  Stück  Holz,
otz',  alit.  strupas  , abgelebter  Mann'.
WP.  II  627  ff.,  WH.  II  595,  601  f.,  606  f.,   692,  Trautmann  284f.,  325,
Mmer  3,  98  f.,  126.
idr-  /Stern',  Kollektiv  ster-ä,  Gen.  str-äs,  dehnstufig  ster-ä  ^Gestirn,
Stern',  ster-nä  ds.;  daneben  terä,  teros-,  terQs  ds. Ai.  Instr.  PI.  stfbhih,  Nom.  PL  tärah  m.  , Sterne',  tarä  f.  , Stern',  av. tk.  Sg.  stärdm.  Gen.  stärö,  PI.  Nom.  staras-ca,  stärö,  Akk.  strdus.  Gen. i,  Dat.  stdrdbyö  , Stern';  arm.  asti,  Gen.  astei  , Stern,  Gestirn';  gr. rfe  -eqog  , Stern',  kollekt.  ^atqa  ,jünger'  ^argov  , Stern,  Gestirn'  (daraus astrum),  wozu  wohl  mit  (w7r-)(37r-:  (ä)aTeQ07r7j,  dargafti^  , Blitz,  Wetter- ichten', axegoip  ,fiimmernd',  {d)a'CQa'rti:oj  ,blitzen,  funkeln',  daTSQOTtrjzrjg, ^^qoTcaXog  ,Blitzeschleuderer  (Zeus)' ;  ohne  anl.  s-  (wie  ai.  tärah,  tara) ^(jdv  Gen.  PL,  mit  metr.  Dehnung  rslgsa,  tbiqsglv  , Gestirne';  lat.  Stella Jrn'  {^ster-[o]lä,  Deminutiv);  bret.  sterenn,  corn.  sterenn  (PL  steyr),  cymr.
65*
=== leaf 271 ===
leiner  Fischschwarm',  ostfries.  sträl  , Streifen',  as.  sträl  m.,  mM^fe (*strelia-)  ,Kamm^  (von  den  Zähnen  =  Strahlen),  wovon  ahd.  sirälm^  Kk-'^ strählen  ,kämmen';  norw.  sti-ll^  strlla  , Streifen,  Ader,  Strahl',  schwer? ,kleiner  Wasserstrahl',  strila  , rieseln',  aksl.  strSla  ,Pfeil*;  '<^    ^'
mhd.   sträm  , Lichtstreifen,    Strahl,   Strom',  nhd.   dial.  sträm' zu  strei-:  ahd.  strlmo,  nhd.  dial.  streimen,  mnd.   strime  ,StreifeDj" Strahl';   zu   *streu-    vielleicht:    mhd.    mnl.  strieme,   mnd.  strlvM  ,8^» Strahl'  (wenn  aus  ahd.  *striomo),  nhd.  Striemen-^
ahd.  streno,  mhd.  stren{e)  ßträhne,  Haarflechte';  zu  *streU'i  lit.  HfiOMA ,bauen',  aksl.  struna  , Strang,  Saite';  von  der  Basis  *5^er-:  klr.  j>oi<«>f****^^ poln.  postronek,  cech.  postranek  ,Strang,  Strick,  Saite'.
lett.   (saules)   stars   ,Sonnenstrahl',   stars   ,Ast',   stara  , Strick,  St
streig-:  gr.  ^iarqi^  (knid.)  ,sechsseitig',  falls  aus  ^ea-atqi^]  ^*^.*fj!l ,Strich,  Schwade;  Zeltreihe;  Längsfurche',  strigösus  ,schmächlif, Stria  (wohl  *strigia)  , Furche,  Falte';  stringö,  -ere  in  der  Bed.  ,J streichen,    berühren,   das   Schwert    ziehen',    strigilis    ,Schabeisen*  {ti^^ nhd.  Striegel)]
ahd.  strlhhan  ,streichen%  ags.  strlcan  ,streichen,   reiben,  sich  b«i gehen';   got.  striks   »Strich',   ahd.   strik  ,Strich,   Streifen,   Streckt  *Wi Strich  Landes',  ags.  strica  ,Streifen';  aisl.  strik  ,gestreiftes  Ze«|| strik  ,Strich,  Windstrich,  Streich';  mnd.  strek  ,Streich,  PossenS
1029
-[teich,  Schlag*  (*straika-),  ags.  sträcian  ^streichen*,  engl,  stroke  , Schlag';
\ür.  strigli  jDisteV -,  9iks\.  strigg^  striHi  ,scheren';  russ.-ksl.  sträg^  „-Aovgd'' ^itroigO'  =  mhd.  Streich);  mit  schwed.  streke  (*strikan-)  ,Stromstrich'  vgl.
rsW-  •^^^^^■*  russ.  strezenb,  streit,  stre^d  ,Stromstrich^; pach  Trautmann  290,  Vasmer  3,  12  f.  hierher  als  ,Mitte,  Herz',  apr.  stri- -     Q  ^Gehirn',   urslav.    *strhi^i,m,   hzw.    *str'b^en'b   ,Mitte,    Mark*,    russ.-ksl. i^enh  ,Mark'  usw.
f  streik-'  air.  srlab  , Streifen*  (*streiba)]  mnd.  stripe  , Streifen*,  mhd. I^fe,  nhd.  Streifen,  norw.  strljpa  ds.,  schwed.  stripa  ,herahhängender  Haar- 'Wscher;  mnd.  mnl.  strlpen  ,(ab) streifen*,  mhd.  streifen  (*straipjan)  ,strei- Ugn,  gleiten,  umherstreifen,  (ab)ziehen,  schinden',  nd.  strepen  ,abstreifen^
I  siTGUg-'.  gr.  arQBvyofxai  , werde  entkräftet,  schmachte  hin*  (air.  trog Rilend*?  s.  u.  ter-,  treugh-  ,reiben');  aisl.  strjüka  ,streichen,  wischen,  glätten; [geh  rasch  bewegen',  strykja,  strykva  ds.,  stryk  ,Strich',  strykr  ,starker f^ind*,  ahd.  struchon  ,ruere,  impingere*,  mhd.  strüchen  ,straucheln',  nl. rooken  , streicheln,  übereinstimmen  mit',  ostfries.  strök  , Streif,  Streifen', id.  straken  ,streifen,  streicheln*  (a  aus  o),  ags.  strocc
=== leaf 272 ===
ian  , streichen*, 'W.  strokk  ,Hobel^;  lett.  strügains  ,gestreift*,  lit.  striTigas  ,Messer'  (poln. Ijtr.);  aksl.  strultq,  str^gati  ,schaben,  scheren',  strug^  , Werkzeug  zum jhaben^,  russ.  strug  ,Hobel'  usw.
streuh-:  ahd.  stroufen,  mhd.  ströufen  (*straupjan)  , abstreifen,  berauben, lündern,  umherstreifen'  =  mnd.   ströpen  ds.,  ags.   be-strlepan  ds.,  mhd. iefen  (*streupan)  ,streifen*;  mhd.  strupfen  , streifen,  abrupfen*.
streudb-  oder  streut- ;  ags.   strüdian  und  strüdan  ,plündern',  strydan
jrauben*,  mnd.  stroden,  ahd.  strutten  ds.
cWP.  II  636 ff.,  WH.  II  603,  604 f.,  Trautmann  288 f.;  Vasmer  3,  27,  30 ff.
l/ttr-,  stero-  :  stre-,  steru-  :  streu-  ,aus breiten,  ausstreuen'  (vgl.  ster- ,starren,  steif  sein*);  storo-  ,Schicht',  str-to-  , Ausgebreitetes',  stero- men-  :  str-men-  , Ausbreitung'. A.  ai.  stj-näti,  stpiöti  (eig.  zur  Basis  streu-),  später  auch  starati  ,streut Ün),  bestreut;  wirft  hin,  wirft  nieder*,  Partiz.  strtd-,  stlrnd-,  Inf.  stdrtave id  staritaväi,  starltave;  sva-stara-  m.  , eigene  Streu',  pra-stard-  m.  , Streu, Mster;  Fläche,  Ebene*  (=  russ.  prostör  ,Raum,  Geräumigkeit*);  stdri- »n-  n.  , Ausbreitung,  Ausstreuung'  (ablaut.  mit  gr.  afgcüixa,  lat.  strämen)-, Vr.  Star-  (Präs.  starati,  stdrdnaoti,  stdrdnäti)  ,sternere*,  Partiz.  stdr^ta- »d  stardta- ;  stairiä-  n.  , Streu,  Lager,  Bett* ;  urvarö-straya-  ,Niederhauen Pflanzungen* ;
1030
gr.  aroQvvfXi  (nur  Präs.  und  Impf. ;  zum  Vokalismus  vgl.  d^6QYwu\\ gevvV'fXL    (Neubildung),    orQOJvvviii    (nach   argwaat)   ^bestreue,   strecke  k^
breite  aus;  ebne',  äol.  Perf.  iarögozai;  Partiz.  argcoTÖg;  argu)^  j^^
•^
Lager,  Teppich,  Decke',  aTgcofxvrj  ds. ;  orgarög  (=  ai.  strtd-)  ^Schar^^^^T    ' menge'  (kret.   azagrög  mit  Umstellung  ,eine  Unterabteilung  der  PL?a    ^ dann  ,Heer'  (dazu  aTgavLd,   oxgaxsia^   otgarriyög),  äol.   GzgoTÖg'^  hot^tJ^ orsgvov  ,Brust'  (^ausgebreitete  Fläche';  vgl.  ahd.  stirna  , Stirn',  reüt^ stlrna-,  cymr.  sarn,  und  o-stufig  aksl.  strana)]
alb.  shtrinj  ,  breite  aus^  (strniö)]  shtie  ,lege  hin,  werfe,  mache  eine  F^ geburt'  {*sterö);  shtrofke  , Decke,  Höhle,  Nest';
=== leaf 273 ===
,Strohdecke'  i^upo-stori-),  sreth  ,strues'  (^stftä),  sreAth  ,prj[^j^  ^ von  der  schweren  Basis  mir.  srath  (iw-St.)  , Strand,  Ufer,  Talgrund**^" Lw. ;  lat.  Lw.  sind  aber  cymr.  ystrad  ,Tal',  bret.  strad  ,le  fond,  TeS le  plus  bas');  cymr.  sarn  ,stratum,  pavimentum'  (*sterdno-j  urkelt.  *8iamim] ai.  stümd-'j
ahd.  stirna  ßtirne^  (*sternia)^  ags.  steornede  , dreist';
lit.  sträja  ,mit  Stroh  ausgelegter  Stall' ;
aksl.  pro-sthrg  -strUi  (russ.  stereth)  ,ausbreiten',  prostram  (*storno-)  ^bltifi strana  , Seite,  Gegend',  russ.  storond  ds.;  aksl.  aruss.  usw.  s^ro^t)  ,Ordllttft|*, strojiti  ,paräre';  ^'  "
vielleicht  hierher  die  z.  T.  s-losen,  auf  einem  St.  *{s)tr-enO',  *{s)ttnl^ (s)tron-t-  beruhenden  Formen:
preuß.-lit.  trenis  , Gegend,  Stelle,  Ort'  (vgl.  aksl.  strana,  ursl.  *iiOT'f^\ alit.  trenta  ,0v\,  Gegend,  Strich';  air.  tret  (Gen.  treoit)  ,Herde'  {*tr€i^)\ aisl.  strlnd  f.  ,Seite,  Kante;  Land';  strgnd  ,Rand,  Strand',  ags.  kfouli spätmhd.  strant  {-d-),  nhd.  Strand,  aisl.  fer-strendr  ,viereckig'.
B.  Erweiterungen:  £
stre-k-:    ags.    stregdan    st.  V.    ,streuen,    spritzen,   verteilen'   (Prllil#'  [ bildung  wie   bregdan)]    dehnstufig   aksl.   strekati   ,stechen',   ablaut  ttnkl j^yiivzgov,   ariyna^,    slav.   *stn>kati   in   cech.   strkati   ,stoßen',    serb.  $^Ct^ »spritzen'.  ,^^,
streu-:  lat.  struö,  -ere  {struxi,  structum  mit  analog.  Gutt.  nach  Vfrti»- mit  V  aus  g^)  »übereinander  breiten,  schichten,  aufbauen',  strues, , Haufe,  Menge',  umbr.  strugla  ,*struiculam' ;
1031
-bret.  strouis  ,stravi'^^  nbret.  streuein  , streuen*;
trot.  straujan  .streuen',  norw.  streya,  aisl.  strä  ,streuen,  ausbreiten',  ags.
```


## [2026-09-14T03:08:45.549Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '82740,82790p' POK_full.txt; echo \"=====2\"; sed -n '82900,82930p' POK_full.txt; echo \"=====3\"; grep -n \"lemma: steu\" POK_full.txt | head; echo ====4; grep -n \"lemma: (s)ter\" POK_full.txt | head -20"
}
```


### [2026-09-14T03:08:45.705Z] TOOL RESULT

```
Exit code 1
(s)teii(-, nasal. (s)trenR-: 

Latin stercus, -oris " excrement, ordure, crap, muck, droppings, manure', sterculTnum, 
sterquilTnum^ dunghill '; cymr. trwnc^ urine, yeast', bret. s//ic»/7/r "human excrement'; 



cymr. troeth^\ye, urine ', /Aoe/^/'mingere', bret. troaz^ urine ' {*trokta or * tronktS); 
Lithuanian tersiu, /eA5//"smudge', S/O/eAs// "smudge', ///"sZ/'dickfiussig become'; East 
Litliuanian tr§siu, tr^stT fertilize ' (as Latin stercorare); 

Litliuanian tr^sa^ manure', tresti^ decayed, verwesen', fraskanos^pus in den Augen', 
wherefore nisi. Prarlau\, rancid ', Norwegian traads., Old English droh Rancor'. 

(s)terg-, (s)treg- 

gr. OTspyavoq Konpwv Hes.; rapyavov "Weinessig'; ablaut, rpu^, -yog "young, still trijber 
wine, Weinhefe '; expressive Old Icelandic t^rekkr. Middle High German dree, -ckes^ filth '; 
probably also Old English dreax^caues'; perhaps Latin tro/a'sow' {*troQ/a'6\e Dreckige'), 
das but also to Middle Irish //'c»^a/io'"gebiert' belong could; whether Old Irish tore, cymr. 
t\/i/rch, acorn, torch, bret. tourc'h'boar' from *trogos aiter fpjorc-' s\N\ne' reshaped sei, is 
doubtful, yet could es as *torkos zur group auf Tenuis belong. 

References: WP. II 641 f., WH. II 708, VasmerS, 12. 
Page(s): 1031-1032 

Root / lemma: (s)teu-1 

Meaning: to push, hit 

Note: with conservative extensions 

Material: A. (s)teu-k-. gr. tuko(; 'hammer, chisel; battle axe ', tukI^u) "bearbeite stone ', 

TUKOvri 'Dreschvorrichtung' (by Hes. Turavn); Old Irish /o//" hollow', /c»//'cave, hole' {*tukslo- 

), cymr. /m/// 'foramen', adj. "perforatus', bret. /c»^//'hole'; probably Old High German duken 

'press, niederdriJcken', Old English dy{a)n, deo/7 'press, constrain, oblige, prick' (see 

accurately under tuengh-' beset'), 

Latvian tukstet^ knock', taucet"\n mortar stampfen', russ. -Church Slavic /stbkngt/ 
'effodere'. Old Church Slavic thkat/^to weave, prick', etc.; 

maye alb. {*stuk) //7^/r' mortar' common alb. s- > th- 

Old Icelandic styggr^ au^vj , irate, unfriendly', nl. stug, older stugge^ stiff, unfriendly, 
abstoftend' can originally 'abstossend' and ' stiff ' sein and in letzteren case with 
Lithuanian stukt/{see below) under sfeo'p^-'steif dastehen' combined become. 

=====2
ds.. Old Icelandic stubbr, sfubb/m. "stump, trunk'. Old English stybbn. " stump '; 

with Germanic -p-: Old Icelandic stupa' tower'. Old English stupian, mnl. stupen's\c\r\ 
biJcken'; ablaut. Old English steap'\r\\g\r\, ragend' (engl. steep ^ steep'). Middle High 
German 5/0^/" hochragender rocks' {Hohestaufen), Middle High German stiefsieep"; Old 
Icelandic staupu. "hole, goblet'; Old English steap. Old High German Middle High German 
s/o^rgoblet'; Old English stoppa^ bowl, basin, bucket, pail '; from "abgestutzt = stolen; 
looted ' expounded sich Old Icelandic s^i/p- "Stief-' (s^t7p/'"Stiefsohn'), Old English steop-. 
Old High German stiof-, stiuf-. Modern High German Stief-, Old English abe-stTepan^vnuq, 
rob', a-st/eped\eoj\/a\st'. Old High German ar-, bi-stiufan^Vc\e parents or the Kinder 
berauben'; 



Latvian staupe^ Pferdefufltapfen '; stupe, stups^ Besenstumpf; (ruptured, broken) rod'. 

References: WP. ll615ff.,WH. II 608ff., Trautmann 331, Vasmer3, 109, 160. 
Page(s): 1032-1034 

Root / lemma: steu-2 

Meaning: to praise 

Note: only indo-iran. under gr. 

Material: Old Indie stauti, stavateetc. "lobt, praises ', participle stuta- "gepriesen', stutf-i. " 

laudation, praise ', stotar- "Lobsanger' etc., Avestan s/ac»///"lobt, praises, besingt; prays ', 



=====3
82919:Root / lemma: steu-2 
82936:Root / lemma: steue- 
(eval):1: ===4 not found
```


## [2026-09-14T03:08:49.933Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '82919,82940p' POK_full.txt; echo \"=== ster barren ===\"; grep -n \"lemma: ster\" POK_full.txt | head -20"
}
```


### [2026-09-14T03:08:50.020Z] TOOL RESULT

```
Root / lemma: steu-2 

Meaning: to praise 

Note: only indo-iran. under gr. 

Material: Old Indie stauti, stavateetc. "lobt, praises ', participle stuta- "gepriesen', stutf-i. " 

laudation, praise ', stotar- "Lobsanger' etc., Avestan s/ac»///"lobt, praises, besingt; prays ', 



participle stuta-, stuiti-, staotar-etc, extended Old Indie stobhatr praises, jauchzt'; gr. 
areuTai '(*ruhmt sich) verspricht boasting '. 
References: WP. II 620. 
Page(s): 1 035 

Root / lemma: steue- 
Meaning: to get dense or tight 

Note: perhaps stau-, stau-. stuW\Vc\ stai-\ sff-: s//-a-"sich verdichten, stocken' as 
extension eines *sta- auffaftbar 
=== ster barren ===
81998:Root / lemma: sterg-, sterk- 
82496:Root / lemma: ster-3 
82508:Root / lemma: ster-4 
82599:Root / lemma: ster-5, stera- : stre-, steru- : streu- 
82687:Root / lemma: ster-6 
83007:Root / lemma: ster-2
```


## [2026-09-14T03:08:52.999Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '82687,82740p' POK_full.txt"
}
```


### [2026-09-14T03:08:53.073Z] TOOL RESULT

```
Root / lemma: ster-6 

Meaning: sterile 

Note: old Sonderanwendung from ster- " stiff ' 



Material: Old Indie stan-i. " infertile e cow'; 

Armenian sterj^ infertile, from animals', also sterd {*ster-6^-o-, -Jo); 

gr. GTsTpa f. ' infertile ' (cow, wife, woman), aT£pi(po(; ' infertile ' (and " rigid'); 

alb. sMJerre young cow, lamb'; also prefixed alb. meshqere " young cow'. 

Latin sterilis " infertile '; 

Gothic stairoi. " infertile ', Old High German stero^aues, ram'; with /r- extended mndd. 
s/eA/re "young cow'. Old English stierc^caW; isl. stirtla^ infertile cow'; 

Bulgarian s/e/7ic5'Gelte'. 

References: WP. II 640 f., WH. II 589 f. 
Page(s):1031 

Root / lemma: (s)ter-7n- 

Meaning: sharp stalk or thorn 

Note: to ster- ' stare, stiff sein' 

Material: Old Indie //•/7a-/77'Grashalm, grass, herb'; gr. rspva^ 'Artischocken-, 

Kaktusstengel'; Gothic t^aurnus. Old Icelandic Old English t^orn. Old High German dorn 

"thorn'; Old Church Slavic trbni, 'thorn', strbnt ' stem '. 

References: WP. II 641, Trautmann 324, Vasmer 3, 14, 98. 

Page(s):1031 

Root / lemma: (s)ter-8 

Meaning: dirty water, mud, smear 

Material: Avestan star- "sich blemish, commit a sin'; 

Armenian f arax, -ic, -oc'pus, humeur' {%ro-, besides ograde perhaps:) Armenian for 
"that flows down, that drops'; Norwegian storn. 'Faulen, Verwesen'; russ.-Church Slavic 
stbrvb, russ. sterva^ carrion '; without aniaut. s-: Lithuanian ferment/^ smear', Bulgarian 
torb ' manure'. 

(s)teii(-, nasal. (s)trenR-:
```


## [2026-09-14T03:09:18.697Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== AHD ster\"; grep -n \"^ster\" AHD_watkins1985.txt | head -20; echo \"== AHD steu\"; grep -n \"^steu\" AHD_watkins1985.txt | head -20; echo \"== sterilis AHD\"; grep -n -i \"sterilis\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T03:09:18.842Z] TOOL RESULT

```
== AHD ster
243:ster-3, 3. Oldest root from *oster- in Greek astér...
1018:ster-2. Also stere-. To spread. I. Extended form *streu-. 1. Germanic suffixed form *streu-nam in Old English stréon, something gained, offspring: STRAIN?. 2. Latin struere, to pile up, construct: STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION. 3. Zero-grade form *stru- in Latin industria, diligence, activity (endo-, within; see en): INDUSTRY. 4. Russian struga, deep place: SASTRUGA. 5. Germanic *strél6 in Old High German sirdla, arrow, lightning bolt (> German
1020:ster-*, Star. 1. Suffixed form “ster-s- in Germanic “ster- rén- in Old English steorra, star: STAR. 2. Suffixed form *stér-ld- in Latin stélla, star: STELLAR, STELLATE; CON- STELLATION. 3. Oldest root form “aster- in Greek astér, star, with its derivative astron, star, and possible com- pound astrapé, asteropé, lightning, twinkling (< “looking like a star”; Ops, stem op-, eye, appearance; see okw-): ASTER, ASTERIATED, ASTERISK, ASTERISM, ASTRAEA, ASTRAL, ASTRO-; ASTEROID, ASTRAPHOBIA, DISASTER, Sterope. 4, Iranian stem *s¢dr- in Persian sitareh, star: ESTHER. [Pok. 2. ster- 1027.]
1021:ster-4. To rob, steal. 1. Possibly dissimilated form in Germanic *ste/an in Old English stelan, to steal: STEAL. 2. Germanic derivative noun *stél-ithé (-ithd, abstract suffix) in Middle English stelth, stealth: STEALTH. 3. Ex- tended dissimilated form in Germanic frequentative *stalkon in Old English *stealcian, to move stealthily: STALK?. [Pok. 3. ster- 1028.]
1022:ster-5. Barren. Latin sterilis, unfruitful: STERILE. [Pok. 6. ster- 1031.]
== AHD steu
1025:steu(8)-
== sterilis AHD
1022:ster-5. Barren. Latin sterilis, unfruitful: STERILE. [Pok. 6. ster- 1031.]
```


## [2026-09-14T03:09:20.490Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== IEC ster\"; grep -n \"^ster[ié]\\|^sterio\\|sterilis\" IEC.txt | head -20; echo \"== IEC stau\"; grep -n \"^stāu\\|^stau-\\|^steu\" IEC.txt | head -20"
}
```


### [2026-09-14T03:09:20.568Z] TOOL RESULT

```
== IEC ster
6245:-is, adjectival formant denoting (1) colour; (2) animate content (1) Skt. harih ‘yellow’; Av. zairis, id.; Hitt. har- kis (^white', as against Gk. argós “bright”, where i-type adjj. are rare); Lat. viridis; OHG gruoni; OE erëne ‘green’ (2) Skt. šučih ‘pure’; Hitt. mekkis ‘big’: Lat. fortis, acris, rudis, mitis, tristis, lenis, sterilis, facilis, etc.; Go. hrains, sels, süts, brüks, anda- sets “pure, kind, sweet, useful, revolting’; OCS vísi "all, Zen “female? (other forms in -ï are adverbial, cf. svobodi, is-plünf, razlict, sugubi, roct, all undeclined. Cf. OCz. je mi len, im- pers. ‘I am (too) lazy . . ^: Lat. lēnis); Li. pats ‘the same’. Sole example of i-st. in Li. Absent fr. Latv. Gk. eünis “bereft'; ídris “skilled”
17210:sterið ‘run dry, become barren’; sterios ‘run dry, sterile, barren; sterile animal. WP II, 640. (Variant: sther-, sthr-) Skt. starih, acc. sg. staryám, npl. staryás, f. ‘barren cow, heifer’; Oss. stålin, Dig. ast'ålun, inf. ‘collapse, go to ruin’; Tokh. sçire, adj. ‘rough, stiff; Arm. teri, adj. ‘defective’ beside taram, adj. (faded', fr. *sterəmos); Gk. steíro, v. ‘make sterile’; steréo, v. ‘deprive, extort’; steiros, adj. ‘barren’; Alb. shterr, v. ‘run dry, become barren’; tr. ‘make barren, sterilize’; shterrë, f. ‘heifer’; Lat. cf. sterilis, adj. "bar. ren’; sterilésco, v. “become sterile’; Go. staíro, wf. ‘barren animal; MHG stëre, stër, wm. Tan; Li. cf. sterilüs, adj. (‘sterile’: OLat. ste- rilus, id. Lucretius); cf. also Alb. shtrof, shtroh, v. (run dry”, fr. *st(e)resKo: Li. stérstu & stéru, sterti, v. ‘grow numb, turn to wood or stone’). Extns. of type *steribho-, *sterbh- in Gk. stériphos “hard, solid"; sterphos, eos, n. ‘hard skin’; OCS strüblü E streblü, adj. in Jo tělo “fit, robust. Z-gde in Skt. sthiráh “solid”, and in OCS strüví, strüvo, R steríva *car- rion, corpse'. Cf. sterp-
== IEC stau
17165:stau- (stauið) ‘howl’. Skt. staumi, v. ‘praise’; cf. (variant) stobhami, v. ‘shout; MHG stouwen, stóuwen, v. ‘shout’; Norw. cf. stöy, sm. f. ‘noise’; Li. cf. (variant) stáugiu, stáugti, v. how?
17217:steu- ‘boost, display, propagate’. Cf. stuuð Skt. cf. staumi, stáve & stavīmi, pp: stutáh, v. ‘praise’; cf. Vedic stavah, m. ‘praise, hymn’; Av. cf. staotəm, staoman, n. ‘praise’; Gk. steümai (2) “make a show of, make as if 10: 5 x
17219:steud- (stud-, sth-) “press, push’. Cf. stoud-, (sth-), stud-, sthud- & steuið. WP II, 618. (E-gde explicit: Gmc. & Slav). E-gde in MHG stiezen, sv. “push? Alb. cf. shtyej, v. (push, ambig. cf. steuio); Lat. (z-gde) studeo, Gre, v. “apply oneself, concentrate on); MHG (z-gde) stuz, gs: stutzes, sm. “jol; G cf. stutzen, v. ‘buffet’; OCS cf. Studi, f. (1) ‘gait, manner, way’; W cf. (variant) sut, m. ‘manner’; sud, m. ‘shape’ (both fr. *steut- or *stout-)
17220:steug- (stüg-) ‘bend, curve, twist MI. stuag, f., stuagh, m. (1) “arch, bow; roll; book: (*stüg- in) G verstauchen, Du. ver-stuiken, v. ‘sprain’; (for Fris. stjūch, adj. ‘surly, stubborn" see next)
17221:steu- (sth-) ‘stiff, solid, stern’. Cf. sthugeros Ir. stuagh, m. (2) 'stalwart'; Fris. stjüch, adj. ‘surly, stubborn'; Du. cf. stiekem, adv. “slily, sneaking’; (z-gde in) G stocken, v. ‘come to a
17234:steuplis, steuplo(n), cf. stüp-. Variant steupr- (stupr-). Arm. ambig. Ir. stualán, m. ‘simpleton’; OCS Stupli, adj. ‘feeble’; cf. (variant) Arm. t'iwr, o-st. ‘wrong, askew’; Lat. (z-gde) stuprum, n. ^wrong-doing'
17236:steuió (steuið, stiü-, stüu-, sth-) ‘thrust, force, take a stand'. Cf. steud- Hom. Gk. steümai, v. “take a stand; be about to .. ^; cf. pi-steuo ‘trust (Of ambig. origin, either aphetic from *epi-^, or fr. *bhidh-^, cf. bheidh-); Alb. ambig. shtyj, v. ‘push’. Cf. steud-, stud-); OCz. ščuju, inf: SCváti, v. *in- cite, bait”; Cz. inf. štvát, id.; Li. cf. nu-SCiüvu, -Sciüti, v. ‘settle down, cease; MHG stuwen, stūn, inf. ‘crop — hair’; Pol. szczuc, inf. as OCz.
```


## [2026-09-14T03:09:29.711Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN\"; grep -n -i \"satarwan\\|staruwan\\|sterwan\\|satarvan\\|unfruchtbar\" HRN.txt | head -20; echo \"== HUB\"; grep -n -i \"satarwan\\|unfruchtbar\\|sterwan\" HUB.txt | head -20; echo \"== PHD\"; grep -n -i \"^stary\\|stariy\\|barren\" PHD.txt | head -20"
}
```


### [2026-09-14T03:09:29.793Z] TOOL RESULT

```
== HRN
6271:716. setei*veH, suturven^ esterven 'unfruchtbar' (Schefer,
6273:Gehört wohl zu ai. start- 'unfruchtbar ; arm. sferj
== HUB
== PHD
570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
930:barren starwan.
```


## [2026-09-14T03:09:33.155Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BQT v1/v2 ستروَن\"; grep -n \"ستروَن\\|ستَروَن\\|ستروان\\|استروَن\" BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head -20; echo \"== plain\"; grep -n \"ستروَن\\|ستروَ\" BQT_v1.txt BQT_v2.txt 2>/dev/null|head; echo \"== MON\"; grep -n \"ستروَن\\|ستَروَن\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-14T03:09:33.299Z] TOOL RESULT

```
== BQT v1/v2 ستروَن
BQT_v1_pages.txt:5748:و دیگری بان‌همچو «باغبان» و«دربان » ؟ ودیگری وان‌همچوه استروان»
== plain
== MON
```


## [2026-09-14T03:09:44.648Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=6255 && NR<=6290' HRN.txt; echo \"=== leaf of that line ===\"; awk 'NR<=6271{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line:\",n}' HRN.txt"
}
```


## [2026-09-14T03:09:45.541Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=570{n+=gsub(/\\f/,\"\")} END{print \"PHD leaf idx:\",n}' PHD.txt"
}
```


### [2026-09-14T03:09:45.660Z] TOOL RESULT

```
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
-) Arm. LW. sioivar.
8J Syr. LAV. ^n^P.DX» <lc Lagnrdo, Oor. Abli. 13.— 159 —
717. ffitem 'unrecht, Gewalt'.
phlv. stahmak^ sfahmaklh bezw. sta/mak^ Rtaxtnakih
gewaltthätig, Gewaltthat'.
Also aus aw. '*8ta/ma-^ vergl. staxlra- (zu dem
Suffixwechsel vergl. oben unter No. 479). Vergl.
N. pr. Gustehm aus '^Vista/^na-,
718. Htetnbe') 'gewaltthätig, streitsüchtig, kampflustig
=== leaf of that line ===
formfeeds before line: 179
```


### [2026-09-14T03:09:46.822Z] TOOL RESULT

```
PHD leaf idx: 103
```


## [2026-09-14T03:09:54.747Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"sitäjiden\\|sitajiden\\|setayiden\\|sitüden\\|situden\\|stäjiden\\|loben\" HRN.txt | sed -n '1,40p'"
}
```


### [2026-09-14T03:09:55.258Z] TOOL RESULT

```
6294:719. ftitTiden, sutä(fe7i 'loben, preisen*, Praes. sitäy-ew,
6298:oss. sfatm 'loben, rühmen', d. sfitd, t. sfjd 'Lob,
10540:hyyvdio Verloben (einhändigen)' (Fick^, 407).
```


## [2026-09-14T03:09:56.222Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"ustuwan\\|ostowan\\|astawan\\|āstawān\\|astwan\\|xastu\\|khastu\\|chastu\" HRN.txt HUB.txt NYB_vol2_glossary.txt PHD.txt | head -30"
}
```


### [2026-09-14T03:09:56.283Z] TOOL RESULT

```
PHD.txt:195:~ih: destruction. ānāstag [Mrstā!] = ānāst. an-āstawān [”1-”stwb*n', -’stwp’n'] disbelieving.
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:970:belief āstawānīh, wābar, wurroyiin, xwastügih.
PHD.txt:972:believing dēn-āstawān | xwastūg.
PHD.txt:1333:confessing āstawān, xwastüg.
PHD.txt:1334:confession āstawānīh, xwastūgīh; āškārāgīh.
PHD.txt:1401:corpor(e)al astómand, astwand, kāl- bodómand, tanig, tanigard, tan- ómand.
PHD.txt:1629:disbelief anāstawānīh.
PHD.txt:1630:disbelieving anāstawān.
PHD.txt:1869:faithful dēn-āstawān | -burdār.
PHD.txt:2747:material astwand, astūmand.
PHD.txt:3234:professing astawan.
PHD.txt:5531:dēnāstawān
HUB.txt:9507:xastu *Kern* = xasta JRAS. 1894, p. 458 = asta, zd. ast-
```


## [2026-09-14T03:10:06.488Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"xwastūg\\|xwastug\\|xvastūk\\|xvastuk\\|xwastwan\\|xvastvan\" NYB_vol2_glossary.txt CHEUNG.txt HENNING_selected_papers.txt 2>/dev/null | head -20; echo \"== NYB astawan\"; grep -n \"āstawān\\|āstwān\\|astawān\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T03:10:06.575Z] TOOL RESULT

```
== NYB astawan
```


## [2026-09-14T03:10:07.556Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== CHEUNG stau\"; grep -n \"^\\*staw\\|staw-\\|\\*stau\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T03:10:07.611Z] TOOL RESULT

```
== CHEUNG stau
23536:wast-/wustoy- (orig. caus.) ‘to place, leave behind’ || (+ *a-) Pash. ästaw- ‘to send, 
23873:366 *stau 
23876:*stau ‘to praise’ 
23921:s(i)taw-d/s(i)tud (LW ?), Pash. stäyol ‘to praise’ (< NP), (?) M. staw-/stiy-, stay- ‘to 
23938:*staub/f ‘to sound, utter’ 
23945:apparently Пг. root has IE cognates: it is perhaps a blend of the ‘praise’ (*stau) and 
23953:*staup ‘to overcome, defeat’ 
47363:ästaw-, 360 
50694:staw-/stiy-, stay-, 366 
56292:*staup 
56344:*staup (s.v.), *tanč (s.v.), 
57328:*staup, *taru 
57384:*karH'! , *stau 
57682:*stau (S.V.) 
57948:*hyar’, *nad, *staub/f, *zag 
58271:*staub/f, *uab/f , *zag
```


## [2026-09-14T03:10:09.139Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '23870,23960p' CHEUNG.txt"
}
```


### [2026-09-14T03:10:09.198Z] TOOL RESULT

```
*REFERENCES: EVP: 71; Fraenkel II: 902 f.; Nyberg II: 180; DKS: 433; NEVP: 77; Kluge 2002: 876 


366 *stau 


*stau ‘to praise’ 

*AVESTAN: stau-, stù- ‘to praise’ || (+ *apa-) ‘to renounce, disparage’ || (+ *2-) ‘to 
profess/pledge oneself to’ || (+ *upa-) ‘to praise’ || (+ *us-) ‘to swear off, renounce’ || 
(+ *fra-) ‘to promise (solemnly), oblige oneself to’ = Liste: 64 

Pres. {1} athem.: IND. 15р. OAv. stäumi (Y 43.8), YAv. staomi (Y 10.3 f., Y 17.18, Y 26.1, etc.), YAv. 
staomi (Y 0.6, Y 1.0, Y 11.19, Ny 1.3, etc.), YAv. upa.staomi (Y 10.17), med. YAv. astuiie (Y 12.8 Ё), 
Y Av. us ... stuiie (Y 12.2), YAv. fra? stuiie (Y 1.21 £, Y 12.2), 3sg. YAv. staoiti (H, Y 10.6), YAv. 
upa.staoiti (Y 10.7, Vyt 39), med. 35р. Y Av. astaoite (Y 10.19), med. Ipl. ҮАУ. fra staomaide (FrW 7.2), 
INJ. 3sg. Y Av. staot (Yt 13.89), med. 35р. YAv. astaota (Yt 19.84), SUBJ. med. 1sg. YAv. apa.stauuäne 
(У 19.7), 2sg. YAv. upa.stuiiä (P 29), 3sg. YAv. upa.stuiiät (V 18.43, V 18.49), IMPV. 25р. YAv. aoi 
stuiói (Y 9.2), 2pl. YAv. staota (У 18.16, V 18.24); Pres. (2) them.: SUBJ. 3sg. YAv. stauuat (Yt), 3pl. 
Y Av. stauuan (Y 9.2), OPT. 25р. Y Av. upastauuöis (V 19.22), med. Y Av. apa.stauuay‘ha (V 19.6), 35р. 
Y Av. "apastauuoit (N 41); Partic.: pres. {1} OAv. stauuat- (Y 34.6, Y 45.6, Y 50.4, Y 50.9), med. ҮАУ. 
stauuana- (Y 10.6, VdPZ 7.43), Y Av. astauuana- (V 3.41), perf. pass. Y Av. ästüta- ‘professed’ (Y 12.8, V 
3.40) 

*MIDDLE PERSIAN: MMP ‘st’y-, BMP st'd-, st’y- /stay-/ ‘to praise’ || (+ *ā-) MMP 
”stw’n, ’stw’n ‘professing? > DMMPP: 89b, 56a 

Widely attested: Pres.: IND. 1sg. MMP ‘st’ym, BMP st’dym /stayém/, 25р. BMP st’yd /staye/, 3sg. BMP 
st’yt/stayéd/, 1р1. MMP ‘st’ym, etc. 

*PARTHIAN: ‘st’w- ‘to praise’ || (+ *apa-) ’byst’w- ‘to deny, apostate’ || (+ *pati-) 
pdyst’w- ‘to promise’ = Ghilain: 77 | DMMPP: 88b f., 17a, 273a 

Pres.: IND. 15р. ‘st’w’m, 3sg. ‘st’wyd, 1р1. ‘st’w’m, ‘st’, 2р1. ‘st’wyd, 3pl. ‘st’wynd, SUBJ. Ipl. ‘st’w’m, 
IMPV. 2pl. ‘st’wyyd, ‘st’wyd; Partic.: perf. pass. ‘stwd, II ‘st’w’d; Inf.: ‘st’w’dn || (+ *apa-) Pres.: IND. 
3р1. *byst’wynd; Partic.: perf. pass. П "byst^w'd || (+ *pati-) Partic.: perf. pass. pdystwd, П pdyst’w’d 
*KHOTANESE: stav- ‘to praise’ || (+ *pati-) OKh. pastu- ‘to promise’ = SGS: 134, 78 
*SOGDIAN: (+ *apa-) MSogd. ’pstw ‘to disown, renounce’ || (+ *ui-) CSogd. wystw 
‘to promise’, BSogd. wyst’w, CSogd. wystw (m.) ‘promise, oath’ 

(+ *apa-) Pres.: OPT. 3sg. MSogd. ’pstwyy; Inf.: caus. ? MSogd. ’pst’wyy ‘to cause to defect’ (+ *ui-) 
Pret.: tr. 3pl. CSogd. w’d’d’rnt, Partic.: perf. pass. CSogd. wystw’ty 

*CHORESMIAN: m/stw- ‘to promise’ (rather with *ni- ?, cf. MacKenzie IV: 534) || (+ 
*apa-) bstw- ‘to deny, disavow’ © Samadi: 187, 27 

*BACTRIAN: (+ *apa-) oBiotaooayo ‘denunciation’ = S-W, Bact.: 175a 

*NWIR: NP sitüdan/sitäy- ‘to praise’, sitayidan/sitay- ‘to praise; call’ 

*NEIR: Oss. I. stawyn/styd, D. (&)stawun/(&)stud, Wa. stow-/stowd, Sariq. 
s(i)taw-d/s(i)tud (LW ?), Pash. stäyol ‘to praise’ (< NP), (?) M. staw-/stiy-, stay- ‘to 
scold, abuse’ 

*SANSKRIT: stav ‘to honour, praise, invoke’ (RV+) = EWAia II: 757 

«PIE *steu- ‘to praise, to announce solemnly’ = LIV: 600 f. | Pok.: 1035 

*IE COGNATES: Hitt. /istuua-/ ‘to become public’, Gr. oeren ‘announces solemnly, 
brags, boasts’ 

*REFERENCES: EVP: 71; IIFL II: 541a; EVS: 76b; Abaev, Slovar’ III: 145 f.; DKS: 431b; Werba 1997: 
259 f.; Steblin-Kamenskij 1999: 317 


*stranj ? 367 


*staub/f ‘to sound, utter’ 

*NEIR: Oss. D. æstuf ‘sound, noise’ 

*SANSKRIT: stobh ‘to cheer, exult, utter a sound ' (RV+) © EWAia II: 761 

© The Oss. form is isolated within Ir. It is very much doubtful whether this 
apparently Пг. root has IE cognates: it is perhaps a blend of the ‘praise’ (*stau) and 
‘utter’ (*yab/f') roots. 


*PIE— > LIV: — | Pok.: 
*REFERENCES: Abaev, Slovar’ III: 155; Werba 1997: 260 


*staup ‘to overcome, defeat’ 
*MIDDLE PERSIAN: MMP ‘stwy- ‘to defeat’, BMP stwbyn- /stöwen-/ (sec. caus.) ‘to 


destroy’, BMP stwb /stob/ ‘powerless’ > DMMPP: 91b 
Pres.: SUBJ. 3sg. MMP ‘stwy’d; Inf.: BMP stwbynytn /stowenidan/
```


## [2026-09-14T03:10:17.013Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"xwastūg\\|xwastug\\|xastu\\b\\|hu-stau\\|xwāstūg\" CHEUNG.txt | head; echo \"== NYB 180 area\"; awk -v n=189 'BEGIN{RS=\"\\f\"} NR==n' NYB_vol2_glossary.txt | head -40"
}
```


### [2026-09-14T03:10:18.135Z] TOOL RESULT

```
== NYB 180 area
ustan [lwstn'] röd- [lwd-] to grow 6. 4074, 4122, 9218, 9518.22, — Av. (1492 sq.) 2raod-; MPrs pt. rwst, v. n. rwyysn (A-H I), Verbum 183; Paz. rustan roded (Mx 6238), pres. pass. rövihed (Sav XVI, 35, dubious); NP rustan röy- ; cf Bailey, BSOS VII, 1933, 84.
ruvan [lwb?n'] soul, the immortal part of the human being: F:2. 9!4, 125, 1326 (v. s. v. vart). 31-34 passim. 72—76 passim, etc. passim; v. also anösak. — Av. (1537 sqq.) urvan-; KZŠPrth ^rwn; MPrth rwn, rwn (A-H. III, BBB); MPrs rwn; Ps lwb’n; Paz. rua; NP ravan.
Rvänän [lw*n'-*n', and Paz.] patron.: ‘of the Rvän clan’ 371-5, v. Frahim Rwäng Zčiš.
sacakiha [~-yh’] properly, fittingly 795. 80°.
sacäk-vär [~-w’l] seemly, becoming 220, 311, - NP sazāvār.
*Sacidarm [scyd’lm] n. pr. of an Indian sovereign 1185. 119 passim. 121°-®. — I believe -it renders a Skr. name *Satya- dharma-.
sacišnēh [scšnyh] the act of passing away,
of elapsing (of time), v. a-frde-sacišneh. — Av. (1553 sq.) ?sak-, OP Oak- in 0akatà
www .parsianjoman.org | ool wok
sacišnēh
used in indicating dates; MPrth pt. sat in the same function (A-H ITI, BBB).
sagr [sgl] (sēr) satiated, satisfied 862. — Ps. sgly; Paz. NP sér; -ayr- > -ér- ac- cording to the common SW law, cf šer.
sagreh (séréh) satiation, repletion 5012. 7218,
*sahén [*MDMHn-yn'] splendid, won- derful, comp. ~-tar 39%, — My conjecture, based on MPrs adv. shynyh’h ‘in a won- derful form’ (A-H I). Doubtful. The traditional text MDM gwntl = apar- gontar ‘of the most excellent kind (or colour)" also gives sense, but seems a little pale. From sahistan.
sahikéh [s’hykyh] resplendence, magni- ficence 1052. — Abstr. of sahik ‘resplendent magnificent’, also ‘showy’, v. PR 32%, PT 166"; NP sahi ‘fresh, young; erect (of a cypress)’, v. Kanga in a (typed) paper on the PT passage, 1953, p. 11. From sahistan.
sahist [shst'] splendid, magnificent 34. — Pt. of
sahistan [MDMHn-stn'] sah-, subj. 3d p. sg. sahät 35%, opt. sahē [MDMHn-yd] 4027, to appear, to be visible, to seem, to please: 1. with a subj.: pattāk sahist pat hamkarpeh i amahraspandān he was manifestly seen in the same shape as the Amahraspands 38?6; an õi sahist Vahuman pes-karp V. appeared to him conspicuous in shape 5697"; an man sahist Spandarmat hu-örön S. appeared to me beautiful in front 5720-21. ruvan ... hün i ke veh sahet? whose soul seems (to thee) the best? 312-3; cë ... homtar sahē? what would seem more haoma-filled ...? 40?'; ne sahét (Evil) does not occur to his mind 77?3-?4, — 2. impers. with an indir. obj.: ašān avd sahčt it wil seem marvellous to them 9724-25. v.s. v. avd; Ardavàn Skuft sahist (it seemed surprising to A. =) A. was stupefied 774; Zartuxšt garān sahist 2. was grieved 3510; -t mā garän sahät do
172 sal
not grieve! 359; hakar šmah bagän sahet if it please Your Majesty 19-27, passim; - governing a clause with ki: apt-mān eton sahist ku it seemed to us that 86-7; 3812-13, 569-9. 7834, — Av. (1559) Isand-, pres. sadaya-; OP pres. 0adaya-; MPrs pt. shyd, Verbum 171; the Pazandists (Mx, SGV) give for MDMHn- the equivalent Sthastan ših- (of obscure etymology).
sahm [shm] terror 9!. — NP sah(1m; MPrs adj. shmyn ‘terrible, dreadful’; from OP "cahma, nom. of "cahman-, SW form of *Oürah-man-, from Av. (802 sqq.) 0rah-, v. tarsitan.
sahmakan [~-kn'] awful 7212,
ilgak [KLB"] dog 10!. 727. 9421.22, — < OP *saka- < *sn-ka- < the zero degree of *san-, the SW form of Av. (1610 sqq.) span-, OInd svan-; “the Medes call the dog oraxa'' Her. I,110 (the NW form of *saka-); NP sag.
?sak [sk'] stone 10224, —
```


## [2026-09-14T03:10:25.995Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 196 197 198; do echo \"===== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' NYB_vol2_glossary.txt | grep -n \"^1[78][0-9]\\|stay\\|stāy\\|stav\\|ōstv\\|ostv\" | head -20; done"
}
```


### [2026-09-14T03:10:27.041Z] TOOL RESULT

```
===== leaf 196
23:179
===== leaf 197
15:180
23:stavr [stpl] strong, sturdy 718; comp. ~-tar 4918, — Av. (1592) stawra-; MPrth Prs 'stbr, v. Sogd 18; Paz. adv. stavarihā ‘thickly, firmly’ (Mx); NP sitabr; from the same root Ps. stpty, MPrth sstft ‘strong, firm’.
25:stayišn st’dän'] praise, worship 115, from stäyitan [st’dytn'] stay- [st*d-], imp. stäi [st’y] 59°. 99%, 100°; pres. Ist p. sg. st
===== leaf 198
1:āyēm [st’dym] 642°; 2nd p. sg. stāyē [st’yd] 59%; 3d p. sg. stäyet [st>dt'] 9927. 1007; 2nd p. pl. stāyēt [st’dyt'] 601; subj. 2nd p. sg. stāyā [st’d’] 100%; pt. = pret. pass. 3d p. sg. stäyit [st’dyt'] 61?: to praise, to profess (the religion) — Av. (1593 sqq.) stav-; MPrth ‘st’w’dn ‘stw-; MPrs ‘stwdn “sty; Paz. staidan, pres. 3d p. sg. stáed (SGV); NP sutüdan or sitayi-
3:stāyītār confessor of the true religion, be- liever, pl. cas. obl. ~-dn 10374,
5:stob [stwb'] powerless: ~ kartan to de- feat 3319. 858-12, 11574; ~ bütan to be defeated 912. — NW form: MPrth ‘stwb- ‘to enfeeble, to annihilate’ (A-H II, 302 n. 4), evidently a denom. of the adj. ‘stwb = estob (i. e., estöß), taken over by BP as stwb' (the original NW form ’stwb' is still found in FrP, Cod. P fol. 6%) and developed to *stēw > *stöi alternating as usual with stoh, which prevailed: Paz. stoh, stuh, NP sutüh. (The reading stwb' = "stav which I gave in HP was wrong, as shown by the MPrth form ; the spelling -wb- for -v- is unknown in MPrth). The authentic SW form is ‘stw = estav (also in Prth: MPrth ‘st’w- caus. ‘to annihilate’, W.-L. 112, II R 3b) attested in ‘stwy- gwn- ‘to overcome’, ‘stwy-bwdn ‘to be defeated’ (List 81, cf s. v. àkas?), also attested by FrP, Cod. P fol. 284, in the form stw' (erroneously read in Paz. stün, but glossed by sutüh, Anguetil Duperron ‘foible, pauvre’). I derive it from *us- tavah- ‘out of force, powerless’, from Av. (639) tavah-; MPrth estob may go back to *ustava(h)-bū- ‘being powerless’, cf SW ‘stwy-bwdn just mentioned.
8:181 sūtēh
```


## [2026-09-14T03:10:35.549Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 554 555 556 557 558 559; do echo \"===== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -25; done"
}
```


### [2026-09-14T03:10:36.597Z] TOOL RESULT

```
===== leaf 554
 ‫سپوز کار‬                                                                                                              ‫‪۱ ۰۹۱-‬‬
 ‫بعنف وتمدی و زور فرو بردن ‪ - ۴‬و بر آوردن‬                               ‫سیندان ‪ = ۱‬بفتح اول بروزن لوندان‪,‬‬
 ‫است ؛ و بقتح اول‬               ‫اد‬
                                 ‫داز‬
                                   ‫ضغت‬
                                     ‫ان ل‬
                                        ‫باشد ‪ ۵8‬؛ ای‬                    ‫خردل فارسی باشد ‪ .‬و آن تخمی است دوابی‬

                                                                                  ‫خوانند ؛ وبکر اول هم بنظرآمده است‪.‬‬
 ‫سيو حته ‪: = 1‬کر اول و واو مجهول‬
                                                                         ‫سیید و ر = بکر اول بروزن سپردوز‪.‬‬
 ‫بر وزن فروخته ‪ ۰‬بمعنی بزور فرو برده‌وخللانیده‬
                                                                        ‫تادرسه و کماج خر مه را گوند ‪ ۰‬و آن نخته‌ای‬
        ‫ویر آورده باشد ‪ 1‬وشتح اول همآمده اس‬
                                                                       ‫که بر سر ستون خیمه‬                           ‫راناخ‬
                                                                                                                        ‫سشدومي‬
                                                                                                                             ‫با‬
 ‫سیوز ‪ ۰ ۲‬بکر اول و واو محهول ›‬                                                                                            ‫گذراند ‪.‬‬
 ‫بمعنی ‪-‬یوخت است که از فروبردن ‪ -‬وبرآوزدن‬
                                                                        ‫سیند یں ‪ = ۴‬بر وزن درم‌چین ‪ ۰‬بمعتی‬
 ‫بعنف و زور باشد چیزی را دچریزی ‪ -‬وامی‬
 ‫و شلان‬      ‫بر‬    ‫فرو‬        ‫است می‬      ‫هم أ مده‬   ‫تاين مەی‬
                                                                        ‫مپندان است که خردل فارسی ‪ -‬و تنم تره‌تیزل‬
                                                                                                                             ‫باشد ‪۰‬‬

===== leaf 555
‫که درجنگه دوازده رخ بردست حجیری نگودرز‬             ‫سیهید ‪ = ۱‬بکر اول‌وضم بای ابجد‪.‬‬
                                    ‫شته شد‪.‬‬           ‫نادچه‬
                                                          ‫ور‬‫ککر‬
                                                              ‫سیه‌سالار و خدارند و صاحب لش‬
‫‪ = ۷‬بابای ابجد بروزن‬             ‫سیه‬
                              ‫بر ه‬
                              ‫ل‬                        ‫ود‬
                                                        ‫وبن‬
                                                          ‫دنیاصاح‬
                                                                ‫خبمع‬
                                                                   ‫سپه بمعنی لشکر و بد‬
         ‫ستیزه مند ‪ ۰‬طلسم وجادو را گویند ‪.‬‬          ‫اصفهبد خوانند ‪ -‬و بعضی‬              ‫وربی‬
                                                                                           ‫باشد ‪۰ ۴‬بع‬
                                                    ‫بادشاهان‬          ‫مخصوص‬       ‫گونند سپهید نامی است‬
  ‫میخ»فف‬
       ‫اول بروزن صف‬       ‫=ح‬
                           ‫بیفت‬
                              ‫س‬
                                                   ‫طبرستان که دارالمرز باشد ‪٩‬‏ چنان که قیسر‬
 ‫سفید باشد ‪ ۷‬و بعربی بیاض کوبند ؛ وبکر‬
                          ‫اول همآمده است‪.‬‬           ‫مخصوص بادشاحان روم وخان مخصوص بادشاحان‬
                                                                                                 ‫کان‬
                                                                                                   ‫ر‬
 ‫سیتاك ‪ = ۸‬بفتح اول ونحتالی مجهول‬
 ‫د وان ارو عروزن وهی‬            ‫وقوقانن بالف‬       ‫سپهید آن ‪ -‬بدال ابجد بر وزن نگه‬
===== leaf 556
  ‫سییفه‌داز‬                                                                                                ‫‪۱۱۳‬‬
                            ‫د‪.‬‬
                             ‫نرا‬
                               ‫یتال‬
                                  ‫وابس‬
                                     ‫گل ت‬
                                        ‫کر‪ .‬قص‬            ‫بیاش خواند ‪ - ۱‬و نام قلعه و حصاری باشد از‬

                                                          ‫توران که سهراب ين رستم گرفت ت وتامدیوی که‬
‫سپیف بر = بابای فارسی بر وزن سفید‬
                                                               ‫رستم کشت ‪ -‬ورنوادمخانه‌ای هم هت ‪. ۴‬‬
         ‫نقند‪.‬‬
             ‫ا پثشهد وبخعروبیا ب‬
                               ‫کر ؛ بمبعنی‬
                                                           ‫سبید ار ‪ = ۴‬مخقف سفدار است؛وآن‬
 ‫سفتح بای ابجد وسکون‬
                   ‫سیید بر گ ب‬
‫رای قرشت وکاف فارسی ‪ ۰‬نامگیاهی است‌وآ درا‬                                                 ‫از جملهٌ درختهای بی‬
                                ‫د‪.‬‬
                                 ‫نافیه‬
                                     ‫بة بم‬
                                         ‫وبقل‬
                                            ‫گربی‬
                                               ‫بع‬                                        ‫ثمر است ولوعی ازید‬
‫سید هنا = کنابه ازصبح دوم است که‬                                         ‫رت‬                          ‫باشد ‪.‬‬
===== leaf 557
 ‫—‬      ‫‪۰5 6‬‬



‫بهنای‬     ‫‪۰‬‬    ‫سفده‬     ‫ورن‬           ‫اش‬
                                                                                           ‫نس دست د بفتح دال ایچد وسکون‬
‫وکشها زانخیبرمضراودیقاوماالند ک وونآشنت اقاومه میباشادی‬
 ‫‪.‬‬
                                                                                           ‫سین و تای قرشت " بمعنی جوانمرد و سخی‬

              ‫بهترین آن آنت که شگاخ‬
                                                                                           ‫و کنایه‌از‬   ‫ومبارك باشد ‪5‬‬         ‫وخحصتنه‬    ‫وصاحب همت‬

 ‫وزن را سوزانند‬                                                                                                  ‫‪.‬‬       ‫موسی علیه‌اللام هم هت‬
                                       ‫ویکویند‬                 ‫شود‬    ‫یا سفمد‬
         ‫با عاست‬    ‫و‬   ‫وییزند‬
 ‫خمس‬
                                                                                           ‫سض رای‌فر شت وسکون‬            ‫و د ‪۳ ۴‬‬        ‫سییر‬
                             ‫کنند و خ‬
‫سشاكزند و بعد از آن بایشد و بر‬                                                             ‫ام رودخانه ایست ازآ ذربابجان‬               ‫واو و وال أجود‬
                                                               ‫مالند ‪.‬‬       ‫روی‬
                                                                                                               ‫که بر دیلمان وگیلان گذرد ‪.‬‬
‫بقتح دال ابجد و سکون‬                   ‫سبیكه دم »‬

‫و صلم‬    ‫باشد ‪-‬‬    ‫صادق‬           ‫صبح‬      ‫دم‬      ‫سحر گاه و‬               ‫هيم ‪۰‬‬            ‫سپیكد زوری = بروزن سفیدموی‪,‬قلمی‬
===== leaf 558
                                                   ‫يان چهارم‬
           ‫درسین بی‌نقطه بانای‌قرشت مشتمل برهفتاد وپنج لغت کونایت‬
‫امول حم‬
      ‫بص‬         ‫موعنی‬
                     ‫ن؛‬‫اتی ‪۷‬‬
                           ‫بدش‬
                             ‫تصنیفات زر‬                   ‫ستا د بکر ارل و ثانیبالف کشیده »‬
                                           ‫گفته اند ‪.‬‬      ‫بممنی ستایش وستودن است که ازدعا وثناوشکر‬
  ‫شالیفده‬
        ‫ستاخ ‪ - 4‬بکس اول وثاکلی‌ب‬                         ‫را‬    ‫ندمت باشد ‪ - ۷‬و ستاننده و ستاش کننده‬
 ‫وبضای نقطه دار زده » شاخ درخت وچ زگ‬                       ‫نبز بگاونمدنموعنی؛دون ترکیب درخ رکمات‬
‫راگویند که از شاخ دبگر سبد و ای ادسگز‬                     ‫گفته نمنگود همجو | فثاب ستا و خود ستا‪ -‬واهر‬

‫گویند شاخ درختی شت که درشاخ‌دبگریچد ‪.‬‬                      ‫باینمعنی هم هست یعنی ستایش کن و بستای ‪-‬‬
 ‫ستاك ^ د بکر اول بروزن فتاد‪.‬مشفف‬                          ‫وایبان‬
                                                                ‫ونوعی از چادر باشد که آنرا شامیانه س‬
‫استاد باشد که بر بای بودن است ‪ -‬و مخفف‬                         ‫مهیمگوبند ‪ - ۴‬و نام لاحنزیماوستسیقی‪-‬‬
                                                           ‫كه و اجه راخ ‪۴‬‬               ‫یات‬
                                                                                          ‫کز تر‬
                                                                                              ‫قنور ونا‬
‫ستاند همهت که از گرفتن باشد ؛ وباین هعنی‬
                        ‫بفتح اول هم آ مده ات‬              ‫وسه ببالهةٌ شرابی را نز گویند که بموجب قرار‬
 ‫ستاذاب د بکراول وثالی وذالمسجمه‬
                                                           ‫داه راازاخلاط‬
                                                                       ‫مردع ت‬
===== leaf 559
 ‫‪۱۰۵۹‬‬                                                                                                                     ‫ستار‬
‫تک ناف و آن چیزست راست ‪ ۳‬تنک و بهن‬
                                                                     ‫فر»‬
                                                                     ‫ف‬       ‫ستاد = بنتح اول برو‬
                                                                       ‫مزنخقطا‬
‫بمرض دوانگشت بافکموترل‪,‬اادزباجوب واستضوان‬                       ‫ستاره باشد که‌بعربی کو کب خوانندا ‪-‬وخیمه‌ای‬
‫و امثال آن سازندویعربی مسطر خوالند ؛ویمعنی‬
                                                                ‫را یزکوبند کهبجهت منم مگس وپشه زند‬
‫کوکب ومسطر بفتح اول گهفمته‌اند ‪ -‬و بازی‬
 ‫سیم فرد را یز گوبند که ستا باشد و‪۷‬ب‪-‬معنی‬
                                                                ‫وبتکار دارریلن هزمماآنمده‌دااسنت گووابینن‌داصح؛‌اوسبتس‪-‬نیو سااوزل‬
‫رات وعلم‌هم آمده است ‪ -‬وآستان درخانه راهم‬                                                      ‫طتبور را حم میگوبند ‪۴‬‬
                           ‫‪:‬‬       ‫کو‬
                                                                ‫ستاره ‪ -‬بفتح اول بروزن شرارهءنوعی‬
                                                                ‫راازچناییزربکاوشندنکده کدهر‪۲‬اازشاپمایراچنةه‌خوابنينادر ‪-‬ناوخیمه‌ای‬
‫ستارة رهیی ه‌کنانه از سنگه طلق‬
‫باشد » و آن سنگی احت مانند آیینه براق‬
                                                                ‫زك دوزند‬
  ‫از روی حم مرھىشىرد ‪.‬‬             ‫وشفاف که برده برده‬                                                     ‫بجهت منع مک‬
                                                                ‫و بشه ‪ ۳‬آ را درین زمان‬
‫ستاره شمر ‪ ۰ ۸‬بن شین نقطه‌دار »‬
                                                            ‫بشه‌دان خوانند ‪ ۴‬؛ و ؛معنی اول بکسر اول‌هم‬
                    ‫منجم وستاره شنای رگاوبند ‪.‬‬                  ‫آمده است که بروزن آشاره باشد ؛ وبکسر اول‬
‫ستاره شمردن ‪ -‬کنابه از بدا‬                                      ‫طنبوره وسازیرا گویند که ‪-‬ه‌تار داشته‌باشد وباین‬
                         ‫کردن وشب زنده‌داری باشد‪.‬‬           ‫ممتی منقصل بابد نوشت ‪ - ۴‬و کوک را یز‬
```


## [2026-09-14T03:10:51.333Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== سترون v2\"; grep -n \"سترون\\|ستروان\\|ستر ون\" BQT_v2_pages.txt | head; echo \"== خستو v2\"; grep -n \"خستو\" BQT_v2_pages.txt | head; echo \"== استوان v1\"; grep -n \"استوان\" BQT_v1_pages.txt | head"
}
```


### [2026-09-14T03:10:51.439Z] TOOL RESULT

```
== سترون v2
33423:                                                     ‫که بفارسی سترون و بعربی‬         ‫بازاینده حم هت‬
33651: ‫بيك ستون بر پباایشد ؛ و بکسر اول یز‬                    ‫سترون ‪ /‬ه بفتح اول و واو بر وزن‬
33657:                                             ‫فارمی ‪« 0011۷-۲8153‬هوبشمان ‪ .۹۱۷۲‬رك ‪ :‬استرون ‪.‬‬
== خستو v2
12038: ‫خستو نه بضم اول بر وکزلنگونه ‪.‬‬
12057: ‫که زخم را و(‪ )۲‬دست ویای شکستهرا می‌بندد‪-‬‬             ‫خستوان‪ = 1‬یبنرماووزلن‌استخوان »‬
12071:                                                            ‫‪۲ : ۱‬ص‪٩۸۱٥‬‏ رك ‪ :‬خستوان ‪:‬‬            ‫«اسفا‬
12086:    ‫‪ ۸‬ح هته(وم‪ 2152 ,158- ).‬استخوان(ه‪.‬م‪« ).‬اسفاا ‪ ۲:‬ص‪»۲4۱ ۰ ۷۱‬ورك‪:‬خستو‪.‬‬
== استوان v1
11953:استوان ۲ - بن اولو تالث بروزن
```


## [2026-09-14T03:10:54.964Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- sterun ctx\"; sed -n '33640,33665p' BQT_v2_pages.txt; echo \"--- leaf:\"; awk 'NR<=33651{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v2_pages.txt"
}
```


### [2026-09-14T03:10:55.924Z] TOOL RESULT

```
--- sterun ctx
 ‫‪۰‬نابه‬
     ‫ستم بر ور = بفتح بای فارسی ک‬
                                                       ‫نهاده اند و معرب آن شطرنج است و اکنون به‬
                                                                               ‫قعرمب اشتهار دارد ‪٩‬‏ ‪.‬‬
  ‫نده و ظلم روا دارنده باشد ‪.‬‬
                            ‫کطنلم‬
                                ‫از ظالم و‬
                                                        ‫ستر و لك= بفتح اول‌بروزن متروك‪,‬مردم‬
 ‫ستی آ و ده ‪ -‬من اول والی‌وسکون‬                         ‫می‌مایه وییکار ‪ -‬وبدخو و خشمناك ‪ -‬ودزد پیشه‬
 ‫لون وهمزه ممدوده و فتح واو و تون ودال ابجد‬                                       ‫‪ -‬وهرژه گوی رکاویند‪.‬‬
 ‫هردو حاکن » صفه و ابوان خاله را گونندکه‬
 ‫بيك ستون بر پباایشد ؛ و بکسر اول یز‬                    ‫سترون ‪ /‬ه بفتح اول و واو بر وزن‬
                                        ‫کفته اند ‪.‬‬      ‫قلمزن » زن لا زاینده وفقیمه راکونند ‪ ۴‬ومعنی‬
 ‫ستنبه ‏ = بکر اول بروزن شکنبه »‬                        ‫کتیبی ابن لفت استرمالند است چه ستربمعنی‬
  ‫‪ ۴‬هندی باستان ‪ ( 11805-‬یی حاصل ‪ ,‬ا حاصلخیز )‬          ‫‪ - ۱‬رك ‪ :‬شترنگه ‪.‬‬

   ‫ارمتی ‪۲6‬ا‪ , 8‬بوفالی ‪ , 8۳1603‬لاتینی ‪ . 5111۲605‬کتی ‪۵‬تنقاد « اسشق ‪.» ۹۱۷‬بهودی ‪-‬‬
                                             ‫فارمی ‪« 0011۷-۲8153‬هوبشمان ‪ .۹۱۷۲‬رك ‪ :‬استرون ‪.‬‬
          ‫از آن فرزند زادن شسدترون ‪.‬‬                    ‫فرئوت‬       ‫کدشوت‬
                                                                        ‫ک‪۴‬ن‪-‬ون‌شوش بمر‬
   ‫‪ ۶‬منوچهری دامغالی ‪. ۷۵‬‬
   ‫وندبشومان اآرا قابل توجه‌داند « استق‪-‬‬
                                       ‫هدا‬
                                         ‫‪-‬رن این وجه اشتغاق را عامیانه می‬
                                                                        ‫‪ ۴‬ه‬
   ‫رك‪ :‬اتم ‪ .‬بهلوی ‪mhats‬‏‬
--- leaf:
562
```


## [2026-09-14T03:11:08.779Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 561 562 563; do echo \"== leaf $n numerals:\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -o \"[۰-۹][۰-۹][۰-۹][۰-۹]\" | head -5; done; echo \"== استرون in v1\"; grep -n \"استرون\" BQT_v1_pages.txt | head"
}
```


### [2026-09-14T03:11:09.752Z] TOOL RESULT

```
== leaf 561 numerals:
۹۱۲۷
۵۲۵۳
۵۵۳۱
۳۱۷۰
== leaf 562 numerals:
== leaf 563 numerals:
۹۱۷۲
== استرون in v1
```


## [2026-09-14T03:11:28.763Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"--- xastu ctx\"; sed -n '12030,12090p' BQT_v2_pages.txt; echo \"--- leaf:\"; awk 'NR<=12038{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v2_pages.txt"
}
```


### [2026-09-14T03:11:29.814Z] TOOL RESULT

```
--- xastu ctx
                                                                                                 ‫‪۷‬‬


 ‫لباسی باشد که درویشان وفران پوشند وازآن‬              ‫جست ه بفتح اول بروزن مست» ماضی‬
 ‫یشمها وموبها اوبزان باشد‪ - ۷‬وخرقه ایرا لیز‬           ‫حستن و آزرده ساختن باشد بعنی مجروح کرد‬
 ‫کونند که از بارچپای الوان دوخته شده باشد ؛‬            ‫ویند‬ ‫وآزرده ساخت ‪ - ۱‬ورنگ ولون را نکیز‬
                       ‫وفتح اول هم آمده اس‬            ‫ویمعتی تفع وفایده هم‌هست ‪ -‬وبضم اول بمعتی‬
                                                      ‫حامه را لیز‬    ‫و آستن‬        ‫فرار و ارام باشد ‪-‬‬
 ‫خستو نه بضم اول بر وکزلنگونه ‪.‬‬
                                                                                               ‫گفتها ند‬

                                            ‫باشد‬       ‫خستر؟ ‪ -‬برورن کفتر‪,‬حثرات‌الارض‌را‬
 ‫وزن دسته ‪.‬‬   ‫اول بر‬    ‫حسته ‪ -‬بفتح‬
                                                           ‫کوند همچو مورو مار وموش وامثال آن‬
 ‫ثال آن باشدھ ‪-‬‬
              ‫ووزاردم]‬     ‫استخوان‌خرما وش‬
                     ‫لفتوالو‬                          ‫خستی ‪ = ۲‬بپروزن بستن بمعنی‌ مجر وج‬
 ‫ومجروح وزخم خورده وسماررا لیزکو ند ‪ 6‬ہے‬                              ‫کردن ‪ -‬ومجروح شدن باشد ‪.‬‬
    ‫مندخ‪-‬فوف‬
           ‫زومینی که آنرا شریکارده باش‬                ‫حستو ت بفتح اول بروزن بدخو » دانۀ‬
 ‫‪ -‬ونم اول بمعنیهی‬     ‫خاسته وبرخاسته هم هت‬
                                                      ‫میوهارا کوبند همچودانةٌ زآرلدو وشفتالو وخرما‬
                           ‫وبنورة دیوار باشد ‪.‬‬
                                                      ‫و مانند آن ‪ - ۴‬و م اول ناممکی از اکابر‬
 ‫حسته نك = بابای ابجد بروزن هرزه‬                      ‫وبزرکان چن است ‪ -‬واقرار واعتراف کننده را‬
‫لیزگفته‌اند(‪ -)۱‬وبمعنی‌جانورخز ندحهمبذظر آ مده خند ‪ .‬پارچه‌ای کروایند کهچون دستی بایایی‬
 ‫شکته باشد بدان بندند ‪ -‬و کی را تیز گوبند‬                                                      ‫است ® ‪.‬‬
 ‫که زخم را و(‪ )۲‬دست ویای شکستهرا می‌بندد‪-‬‬             ‫خستوان‪ = 1‬یبنرماووزلن‌استخوان »‬
 ‫وهرچیز که انرابرزخ‌بندند خواه پلرچه باشد‬              ‫افرار و اعتراف کنندکان و معترف شکدانرا‬
                                     ‫خواه هر هم‪.‬‬                                     ‫گویند ‪.‬‬
  ‫ان گر فتی‪ -‬بسنی‌خس‬
                   ‫خدسهدر‬                              ‫حستو انه = پم اول‌بروزن خرواله»‬

                            ‫‪ -:‬را و‬     ‫(‪)۲‬چك‪ .‬چش‬                   ‫)‪ (۱‬چك ‪,‬چش‪ :‬کونند ‪۳‬‬


                ‫«خراستر» (ه‪.‬م‪ = . ).‬خرفتر‪.‬‬            ‫مخفف‬
                                                         ‫‪۴‬‬               ‫رك ‪ :‬خستن ‪.‬‬      ‫‪۱‬‬
   ‫‪ - ۴‬هلوی ‪ 08152۷5‬ک(وفتن ‪.‬كتك زدن) «ناوادیا ‪ ۷۹۱2‬ورگ ‪ :‬اسفا! ‪:‬ص‪. ۲۸۱‬‬
    ‫هه بهلوی ‪6-4۵1‬‬               ‫‪.‬‬    ‫ورك ‪ 1‬استخوان‬    ‫هته(ه‪.‬م‪.).‬‬    ‫چ‬   ‫(ھ‪.‬م‪(.‬‬     ‫و‬     ‫‪۴‬‬

                                                            ‫‪۲ : ۱‬ص‪٩۸۱٥‬‏ رك ‪ :‬خستوان ‪:‬‬            ‫«اسفا‬

               ‫کرچه کوا تخواهندازختو‪.‬‬                      ‫بقرنل اوکوا کنراند دل‬
     ‫‪۰‬ت‪۹۰4‬‬
         ‫ر«ی ل‬
             ‫فای‬
               ‫فرخی س‬
    ‫ار«له ص ‪٩۸۱٩‬‏ ‪ ۰‬ارمنی ع ‪582701905‬‬
                                    ‫هف)‬
                                      ‫دتر‬
                                        ‫‪-‬هلوی ‪( 0200052‬مقر ‪ ,‬مع‬
                                                              ‫‪ ۱‬ب‬
                                                                          ‫‪.‬‬       ‫*اسفا! ‪ ۲ :‬ص ‪۵۸۱‬‬
           ‫زختواله جه مابه هت شوشتری؟‬                 ‫‪ - ۷‬نگر زسنك چهمابه بت کوهرسرخ‬
    ‫معروفی‌بلخی‪« .‬لت‌فری ‪۸44‬‬
    ‫‪ ۸‬ح هته(وم‪ 2152 ,158- ).‬استخوان(ه‪.‬م‪« ).‬اسفاا ‪ ۲:‬ص‪»۲4۱ ۰ ۷۱‬ورك‪:‬خستو‪.‬‬
   ‫‪« : ۲2۱‬روی زبيا مرحم دلهای‌خته‬         ‫‪ ۰‬رك ‪ :‬اسفاا ‪:‬‬
                                         ‫‪۲‬ص‬                          ‫اسم مفمول از «خ‪‎‬‬      ‫‪a‬‬
                                                        ‫و‌تسا دیلک یاهرد ‪».‬هتس ‪‎‬ناتلک« ‪.* ۱۱۸‬‬
  ‫با]س‬
--- leaf:
205
```


## [2026-09-14T03:11:49.679Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T03:11:49.690Z] TOOL RESULT

```


```


## [2026-09-14T03:11:51.682Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== ARY سترون\"; grep -n \"سترون\\|ستودن\\|ستایش\" incoming/ARY/ARY_pages.txt | head -20; echo \"== ARY latin\"; grep -n -i \"STERILE\\|STAU\\|STEU\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-14T03:11:51.771Z] TOOL RESULT

```
== ARY سترون
83:می‌بردند و وپژگی‌های بدنی و اجتماعی و فرهنگی آنان را مورد ستایش قرار می‌دادند. در دوران
10196:۱ ستایش / ۳۴۵
10218:۱ بازگشت به؛ ستودن,
10260:سترون» استرون / ۳۴۷
10292:۱ فقدان واژه‌های همریشه در زبان‌های اوستایی و پهلوی و دیگر زبان‌های ایرانی وابستگی "سترون" يا واجریشه‌ی
10294:به احتمال زباد واژه‌های "استر" (به چم "قاط" که جانوری" مقطوع اللسل است) و سترون" (به چم" پا کر د(وارييي.
10312:بازگشت به: ستایش.
== ARY latin
2409:STAUL (RUMANIAN) gle, STAN, STEL, STELN:(ARMENIAN) 54,1
2483:STEUER, STEUERN :(GERMAN) jlsT STAYOA, STUI-, — -(AVESTAN) (gl!
2490:STUUR DUTCH) .gocke STAUROS, STOA (GREEK) gli,
2491:(IN)STAUR(RARE) LATIN) 3
2496:SKEAT: (STEU., STHEU-) 759 HOLD HIGH GERMAN) pf laT
5798:TORAINN, STEU STYNJA OLD NORSE) oS 25
10003:é } tof seb olay STAU, STUTT- (SANSKRIT) Site |
10027:IR y hay sbi aby STAUKA NORWEGIAN) (5 $343
10064:STERILE (aii) ENGLISH) pulSsl sTaRis (SANSKRIT) <2 Soilee
10068:‘REFERENCES wenthay STERILE ~ (FRENCH) «15 |
10070:BARNHART: (STERILE) 1066 STERIL ITALIAN). p'No 4"
10071:DELAMARRE: (STERILE) 235 ESTERIL —-""1QlQRTUGHESE) Js
10072:ONIONS: (STERILE) 868 STAIRO ” GOTHIC) Sa
10073:SKEAT: (STERILE) 602 (OLD SCANDINAVIAN) oS gt!
10092:STEUTAL, STEUTI = (GREEK) iy HAVESTAN) gi 3)
10095:POKORNY, ——~=~S~*~S*~S*~S*S*~S«CS STUO, STID, STAUN :(OSSETIC) 2-31
10098:wel seb dey STU-, STAU., STAVATE, STAUTI
10167:‘REFERENCES cntKag STYLOS, STAUROS (GREEK) gli
10168:POKORNY. —=~=~=« 081009. -STAU,, (IN-STAU-RARE).(LATIN) 53
10174:SKEAT: (STEU) 789 STIURA
```


## [2026-09-14T03:11:58.237Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10255,10300p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T03:11:58.283Z] TOOL RESULT

```
اوستی (0858712): ررر نان لزان
کردی (078215): دادن آلمانی (/08704۸): زان
هه
[pdf page 346]
۹
سترون» استرون / ۳۴۷
ِ :
انگلیسی کهن (بلولا52(0 ۵ا0: 57۸7 پسگشت‌ها ۸/5
ٍ انگلیسی (لوآلا6۸/0): ان 2 ت۶0
د دانمارکی (0۸715/7): 7 ,57۸8 6 (87۸7۲) +8۸0/7
سوئدی (8(۷5075/1): ین :۸213
نروژی (/0۷07008014: 5۸ 4 (873036) ,104 610
هلندی ((0176): 57۸0 61 (87۸77) :0/10
روسی (894(7تا): ان دون 57
لیتوانی ((۸(/۵ت7(4/)): ,7 ,595 (87۸77)
5 ,87۸1815 9 (ت57581
لنونی (لتی) (/4774ل): نراد ادن 8 13160 تنم
| برهان قاطع + 1.۹۸
یادداشت:
ِ چم اين واژه در زبان‌های ژرمنی: چوبدستی.
پهردی - فارسی تایه ایک انگلیسی کهن (#اکناه/80 ۰:0۵ 571886
سانسکریت (5۸/5۳77): 57۸85 انگلیسی (تل5ل6۸/0)(از فرانشه) 8788312
ارمنی (4/۵45149۷): زد ان بلفاری ((متماناق): 8رد ان
بونانی (6523): 57818۸ ,57۸88717۸ آلبانی ‏ (/(۸۸۷1۸قله): درون
لاتین (710۷با): 578315
ا فرائسه (/۳88/6): - ند اد دنم پسگشت‌ها 5
ٍ اسپانیایی (5۶۸(/1524): نا 1
[ اه ایبایای (ملم: 8 ون 6 ات78 2/7
پرتغانی (۳:077618892 3818811 5 ای نامام
گرتیک (007[716): ید ان 8 (۲3ت975) :0/705
ایسلندی کهن (/0104/1۸2/(ی50 صا0): 2 (878۴-۲۵) یا
871871۸ برهان قاطع : ۰
آلمانی کهن (057214(0 0[7اتز صزه): لفت‌نامه دهخدا : ۶ رو ۲۸۴۸
زد دی فرهنگ معین + ۳۳
[pdf page 347]
۸ | ستنبه» ستمبه (به چم *مرد درشت و قوی و دلیر")
یادداشت:
۱ فقدان واژه‌های همریشه در زبان‌های اوستایی و پهلوی و دیگر زبان‌های ایرانی وابستگی "سترون" يا واجریشه‌ی
هند و اروپایی 8781۰ را نامسجّل می‌کند و بهمین دلیل در جلو واجریشه‌ی مندارلاییای (شاید) آورده‌ام.
به احتمال زباد واژه‌های "استر" (به چم "قاط" که جانوری" مقطوع اللسل است) و سترون" (به چم" پا کر د(وارييي.
تراشیدن نیز از همین واجریشه‌اند. ً
فارسی ((۳28814): استنبه, ستمبه (به چم آمرد درشت و قوی و دلیر) 5
اوستایی (/4837۸2): 338۸1۸ آرمنی (4ل842(14): 87۸/8۸
پارسی باستان (۳881۸(۷ صا0): :
87۸3/8۸3۸ پسگشت‌ها ایشا دی
سانسکریت (54(5877): سا
```


## [2026-09-14T03:11:58.861Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10190,10230p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T03:11:58.912Z] TOOL RESULT

```
ارمنی (۸۵7/8/70۷): ۸7 ساکسونی کهن (5420010 ۰:02 5718230

سس
[pdf page 344]
۹
1
۱ ستایش / ۳۴۵
۱
فریزی کهن ((9۵ل۶۳ 010): دون برتونی (876700): دنر ان
آلمانی کهن ((62724 ۲۲/۵/4 7ا0): هبت (177775): 3 ند ۱۲
0 ,53330
آلمانی ((05801۸): لک دون پسگشت‌ها 5
انگلیسی کهن (8(0/30 00): 8 2 ۸08020
. 503 0 (57۸3) +7 8۸70
انگلیسی (تل8لا6۸0): 3 ی 1 (670115) :ما05
دانمارکی (0۸/7154): ادلی ان آلان 4 (87۸3) :۸۸2215
سرئدی (877:0157): 1۱ لا 5556 ها
نروژی (0/07۳780۵2۷: لدلی اد رلای 3 (57۸3) :0105
هلندی (007021): دادن 8 (57۸3) :57
: ایرلندی کهن (7ل3ل] 0ا0): اد 39 +۸۸47
ولزی (5 )+ لاد ادن برهان قاطع : ۱۹۶
رام
اوستایی (4/597//4): 577815 ,857۸ پسگشت‌ها ات دی ۴ وی
ِ پهلری (تتمابنمم: ۰ 57۸۷18718 ,87۸ ۰ ۳۳ ۳
۱ اففانی (پشتر) 7040+ با8لا57۸ 8 (۲8۸138) :24۸0052/21 7
ْ سانسکریت (84//807): -87071 574109 برهان قاطع + ۹۸
زو
بادداشت: ۹ ۰
۱ بازگشت به؛ ستودن,
هه ۱
ا
: 3
افغانی (پشتو) (//۸۳0/۸): ۸ فرانسه کهن ([۳۲2۸0 010): دنه ۷
تخاری ۸ (۸ (۸ل70221۸): 07 ایتالیایی (۸۸لل77): دش دب
سانسکریت (8۵(9۳7): 57۸181۸8 ابسلندی کهن (/524(0/0۸7/14 0ا0):
ِ پونانی (07628): 595 ,57038 ,57۸ 87118
[pdf page 345]
۶ | ستبر» استبر
ساکسونی کهن ((54200 070): 50 ۸8 ,8717
فریزی کهن ((۲۸/54 ا0): 8706 لنرنی (لني) (7714(7): 5
آلمانی کهن (/688/4 04[ (01): ایرلندی کهن (5/7لااالما0): 8۸3
```


## [2026-09-14T03:12:10.557Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"سترون\" \"استریلیزه\" \"ستایید\" \"استوان\" \"خستو\"; do echo \"== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done; ls -la MON_part1.txt MON_part2.txt; head -c 300 MON_part1.txt"
}
```


### [2026-09-14T03:12:11.699Z] TOOL RESULT

```
== سترون
MON_part2.txt:6
MON_part1.txt:6
== استریلیزه
MON_part1.txt:1
MON_part2.txt:1
== ستایید
MON_part2.txt:0
MON_part1.txt:5
== استوان
MON_part1.txt:36
MON_part2.txt:45
== خستو
MON_part2.txt:4
MON_part1.txt:8
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نا
```


## [2026-09-14T03:12:13.941Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"سترون\" MON_part1.txt | head; echo ---; grep -n \"استریلیزه\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-14T03:12:14.025Z] TOOL RESULT

```
11855:استرول: مسماعه [- سترون] (ص.) زنی 
23540:شین کسترون: سط تنل کشتاد کین دست» 
37210:مانند اينکه آهن و سترون یا حاصل و مقبل 
41721:نازا ساختن» سترون کردن. (بز.) ضد عفونی 
97456:4 : 2 [ع.] (امص.) نازایی» سترونی. 
97593:را فرزند نشوده نازاه سترون. (مسج.) 
---
MON_part2.txt:27199:خوراکی که آن را بصورت استریلیزه در 
MON_part1.txt:11869:استریلیزه: 6 (ص.) آنجه که به
```


## [2026-09-14T03:12:16.242Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '11845,11880p' MON_part1.txt; echo \"=== 41715\"; sed -n '41712,41726p' MON_part1.txt; echo \"=== 97590\"; sed -n '97585,97600p' MON_part1.txt"
}
```


### [2026-09-14T03:12:16.346Z] TOOL RESULT

```
واحد پول رسمی انگلستان. نشانهُ اختصاری 
آن 4 است. (بانک.) کشورهایی که معاملات 
خارجی آنهاتوسط لیر استلنگگ صورت 
می‌گیرد) مق .گروه دلار. 

استرواح: اروت نت ( وت ) آسایش 
جستن. . آسایش کین ارام ٍ بافتن» 
برآسودن. بوی برداشتن» بو گرفتن» 
گندبدن. 

استرول: مسماعه [- سترون] (ص.) زنی 
که بچه نیاورد» نازاه عقه 

استر ۵ (6-)0500۲-2 01 ۳ که بدان موی 
سر و صورت ترآشند» تیغ 

استرهلیسیدن: م02[ف1.ه (مص م.) ( کد.) 
دلیری کردن» جانبازی کردن. 


استری: -25121 (حامص.) مانند استر رفتار 


کردن» چموشی. 
استریلیزه: 6 (ص.) آنجه که به 
وسایل علمی میکرب‌های وی کشته شده 
باشد» ضد عفونی شده. 
اسستزاده: (6-)2202عاعت (ع. استزادة] 
(مصم.) بیش خواستن» فزونی طلبیدن» 
افزون» خواستن» طلب افزونی کردن. مقصر 
شسمردن» (سصم.) کله کردن؛ دلشنگی 
نمودن؛ ج. استزادات. 
استزاره: (625۲2۵)6)وم [ع. استر ار ة ] (مص عم.) 
دیدار خواستن» طلب زیارت کسی کردن. 
استسعاد: 0 مه (غ.) (مص‌م.) نیکبختی 
حواستن» سعادت جستن. مسعود دانستن» 
=== 41715
(اسص.) پیچیدگی؛ ج. تعقیدات. تعقید 
لفظی: (اد.) آن است که به سبب تیجید کی 
الفاظ خو اننده و شنونده معنی کلام را به 
آسانی در نبابد. تعقید معنوی: (اد.) ان است 
که شاعر یا نویسنده کلماتی آورد که مرادش 
معنی حقیقی آنها نباشد. بلکه منظور معانی و 
مفاهیم دور از ذهنی باشد که شنونده و 
خو اننده به اسانی انها را در نباید. 
تعقیم: 270 [ع.] (مص ع.) عقیم کردن» 
نازا ساختن» سترون کردن. (بز.) ضد عفونی 
کردن میکرب‌ها به وسیلةٌ ضد عفونی ساختن 
شیق؛ ج. تعقیمات. 
تعلق: 2110 [ع.] (مص‌ل.) آو بخته شدن. 
درآویسختن» واحت کر داشتن. (امص.) 
دلبستگی؛ ج . تعلقات. 
=== 97590
(عقایل). 
عقبله: (6-)2-]آره [ع. عقبله ] (.) رسمانی 
که بدان ساق و وظیف شتر را بندند؛ پای‌بند. 


مایٌ گرفتاری. تعهد پیمان. 

عفیم: 20 [غ.] (ص.) مرد یا زنی که وی 
را فرزند نشوده نازاه سترون. (مسج.) 
بیحاصل؛ بی ثمر. 

ر: 2 (ع.] (.) عصای چوبان؛ 
عصای اسقف» عصایی که در تفرج بدست 
گیرند. 
عکاس: ۵ [ع.] (ص. .) آنکه شغلش
```


## [2026-09-14T03:12:29.900Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D8%B1%D9%88%D9%86",
 "prompt": "Give the full Persian entry: etymology of سترون (sotorvan/satarvan) 'barren, sterile' — Middle Persian form, Proto-Iranian/PIE root, cognates, and any cited sources (Hasandust, MacKenzie, Horn)."
}
```


## [2026-09-14T03:12:31.911Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D9%88%D8%AF%D9%86",
 "prompt": "Give the full Persian entry for ستودن: etymology, Middle Persian form, Avestan/Proto-Iranian root, related forms like ستایش/ستاییدن, and cited sources."
}
```


## [2026-09-14T03:12:32.937Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sterile",
 "prompt": "Full etymology of 'sterile' and 'sterilize': Latin sterilis, PIE root, French intermediary, dates."
}
```


### [2026-09-14T03:12:35.212Z] TOOL RESULT

```
# Persian Entry: سترون (satarwan/satarvan)

## Etymology

The word سترون derives from **Middle Persian** (stlwn' /starwan/), meaning "barren, childless."

The ultimate origin traces to **Proto-Indo-European** *\*str̥-wénts*, with the sense "barren, sterile."

A folk etymology attributes the term to ستر/استر (satar/astar, "mule"), since mules cannot reproduce.

## Source

The entry cites the **Dehkhoda Dictionary** (1931–), compiled by Ali-Akbar Dehkhoda at Tehran University, as the primary reference for these etymological details.

---

*Note: The provided content does not include citations from Hasandust, MacKenzie, or Horn.*
```


### [2026-09-14T03:12:37.350Z] TOOL RESULT

```
# Etymology of Sterile

**Origin:** The word "sterile" entered English in the mid-15c., derived from Old French *stérile* and Latin *sterilis*, meaning "barren, unproductive."

**Root:** The term traces to the Proto-Indo-European root *\*ster-*, which means "stiff" and also connects to Sanskrit *starih* ("barren cow") and Greek *steira* ("sterile").

**Semantic Evolution:**
- **1530s:** Applied to persons, chiefly women
- **1570s:** Referenced unproductive soil
- **1640s:** Used figuratively for writing lacking richness
- **1877:** Acquired the bacteriological sense of "free from living germs"

**Related Terms:** The etymology page also documents *sterility* (early 15c.) and *sterilize* (1690s), with the latter's medical meaning—rendering things free of micro-organisms—documented by 1878.

The word's journey reflects how classical language adapted to describe biological and medical concepts across centuries.
```


### [2026-09-14T03:12:38.772Z] TOOL RESULT

```
# Persian Entry for ستودن

## Part of Speech
Verb

## Meanings
The verb conveys the sense of praising or commending. It encompasses meanings such as "to praise, to commend, to extol, to eulogize, to glorify, to adore, to worship."

## Etymology
The word descends from Middle Persian forms including _stwtn'_ and _stʾdytn'_, which trace back to Proto-Iranian _*stā́wti_ and ultimately Proto-Indo-Iranian _*stā́wti_, all meaning "to praise" or "to laud."

## Cognates
Related words appear across Indo-European languages: Sanskrit _स्तौति_ (stauti), Old Punjabi _ਉਸਤਤਿ_ (usatati), Ancient Greek _στεῦται_ (steûtai), and Hittite _istuwa-_.

## Transliteration and Pronunciation
Classical Persian: _sitūdan_ (/si.tuː.ˈdan/)
Iranian reading: _sotudan, setudan_

## Present Stem
**ستای** (setây)

## Sources
References include Johnny Cheung's *Etymological Dictionary of the Iranian Verb* (2007) and D. N. MacKenzie's *A Concise Pahlavi Dictionary* (1971).
```


## [2026-09-14T03:12:47.759Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/سترون' --note 'page 481, root Ster 4, node #2: Persian سترون satarvan < MP starwan, PIE *str̥-wénts \"barren\"' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/ستودن' --note 'page 481, root Steu 1, node #3: NP sotudan < MP stwtn/staydytn, Proto-Iranian *stāwti \"to praise\"'; python3 tools/fetch_source.py 'https://www.etymonline.com/word/sterile' --note 'page 481, root Ster 4, nodes #3-#6: Latin sterilis > OFr sterile > English sterile/sterilize'"
}
```


## [2026-09-14T03:12:48.528Z] TOOL CALL #43: WebSearch

```json
{
 "query": "Middle Persian xwastūg \"confessing\" etymology āstawān xwāstwānīft Manichaean confession"
}
```


### [2026-09-14T03:12:49.558Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/57ba81786d047c15.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1c4fbf4d1b14a2df.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1d1c24874c118994.txt
```


### [2026-09-14T03:12:55.968Z] TOOL RESULT

```
Web search results for query: "Middle Persian xwastūg "confessing" etymology āstawān xwāstwānīft Manichaean confession"

Links: [{"title":"FESTIVALS ii. MANICHEAN - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/festivals-ii/"},{"title":"MANICHEAN SCRIPT - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/manichean-script/"},{"title":"DATABASE OF MANICHAEAN TEXTS I ¥]-^µ A Selection of Manichaean Texts in the","url":"https://www.manichaeism.de/wp-content/uploads/2019/11/edbmt-12-bbb-1102019pdf.pdf"},{"title":"THE MANICHAEAN MIDDLE PERSIAN WRITINGS ((b)) - The Cambridge History of Iran","url":"https://www.cambridge.org/core/books/abs/cambridge-history-of-iran/manichaean-middle-persian-writings/27BEDEC8D4E0A2F70CCAD59E1799C3E9"},{"title":"Varieties of Middle Persian I: The Manichaean, Book Pahlavi and Inscriptional Scripts | Invisible East","url":"https://invisibleeast.site.ox.ac.uk/article/middle-persian"},{"title":"Dictionary of Manichaean Middle Persian Durkin-Meisterernst","url":"https://www.scribd.com/doc/212104683/Dictionary-of-Manichaean-Middle-Persian-Durkin-Meisterernst"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"},{"title":"Persian Online – Grammar & Resources » Middle Persian","url":"https://sites.la.utexas.edu/persian_online_resources/history-of-the-language/middle-persian/"}]

Based on the search results, I found relevant information about Manichaean confession terminology. In Sogdian Manichaean texts, the term xwʾstwʾnyfṯ (xwāstwānīft) is used for "confession" in the context of the elect's prayer and confession book. The elect confessed their sins at the beginning of the rite to the levitated Mani and the gods, and toward the rite's end mutually forgave each other.

The search results also indicate that there is a Manichaean Prayer and Confessional Book in Middle Persian, Parthian and Sogdian, which provides context for the use of these confession-related terms in Manichaean religious practices.

However, the search results do not contain detailed etymological information specifically about the Middle Persian word "xwastūg" or its relationship to the Sogdian "xwāstwānīft" form. To find more specific etymological analysis, you may want to consult specialized Manichaean texts and Iranian linguistics resources directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:13:00.619Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%AD%D5%B8%D5%BD%D5%BF%D5%B8%D5%BE%D5%A1%D5%B6",
 "prompt": "Armenian խոստովան: give the etymology in full — which Iranian form it is borrowed from, and what that form is analysed as (prefix + root)."
}
```


### [2026-09-14T03:13:01.752Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T03:13:01.851Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B3%D8%AA%D9%88",
 "prompt": "Persian خستو: does an entry exist? Give meaning and etymology if present."
}
```


### [2026-09-14T03:13:03.100Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T03:13:06.371Z] TOOL CALL #46: WebSearch

```json
{
 "query": "Armenian խոստովանիմ xostovanim etymology Iranian *hu-stawan Parthian borrowing confess"
}
```


## [2026-09-14T03:13:08.164Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"xostovan\\|χοστοβ\\|hu-stavan\\|hustavan\" *.txt incoming/*/*.txt 2>/dev/null | head -10"
}
```


### [2026-09-14T03:13:08.272Z] TOOL RESULT

```
ISS_alt_DKS.txt:3695:scripts of the Saddharrna-Pundarika, 1949, Куб) lera- nihelamati ' maintaining humble thought’, where Zera- is from dàürava- (Khotan Saka der-, Parāči- dër-) with mati- = māna- 'thinking'. The word náhala-, nihela- ‘humble, reverent’ is then from ni- ' down, low’, adjective niha- Чом" with secondary suffix -/a-, comparable with naha- in Manj. 192 mahasía 'nadir' = nasta, older natülto; for the -la-, note also órauka-la- 'brow', bakalaka- ‘small’, The adjective niha- < *niĝa- is then to be set with Suyni *nz8 'low' (queried in IIFL 2:35* and absent from Et. Voc. Shughni group), but -/i- is very ambiguous in Khotan Saka; the Gilgit Iranian dialect is too little known. КТ 6'139 offered a Prakrit to BS nikhila- 'full', but it was unsuitable for the meaning. See also jsondta- омей, humble, reverent’, and Armen. lw xonarh Чох, humble, respectful! < *hu-ānaĝra- (xo- as in xostovan ‘confessing’ < *Au-à-stavüna-).
```


### [2026-09-14T03:13:13.026Z] TOOL RESULT

```
Web search results for query: "Armenian խոստովանիմ xostovanim etymology Iranian *hu-stawan Parthian borrowing confess"

Links: [{"title":"Armenian etymology Research Papers - Academia.edu","url":"https://www.academia.edu/Documents/in/Armenian_etymology"},{"title":"Anushawan","url":"https://en.wikipedia.org/wiki/Anushawan"},{"title":"ARMENIA AND IRAN iv. Iranian influences in Armenian Language - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/armenia-iv/"},{"title":"Parthian language","url":"https://en.wikipedia.org/wiki/Parthian_language"},{"title":"խոստանամ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D5%AD%D5%B8%D5%BD%D5%BF%D5%A1%D5%B6%D5%A1%D5%B4"},{"title":"Armenian Etymology With English Cognates and PIE Roots","url":"https://www.arak29.org/wp-content/uploads/2019/04/Armenian-Etymology-1.pdf"},{"title":"-shat","url":"https://en.wikipedia.org/wiki/-shat"},{"title":"On \"Parskahayeren\", or the Language of Iranian Armenians - borderlessblogger","url":"https://borderlessblogger.com/2015/08/25/on-parskahayeren-or-the-language-of-iranian-armenians/"},{"title":"Parthian–Armenian language contact and its historical context | Iranian Syntax in Classical Armenian: The Armenian Perfect and Other Cases of Pattern Replication | Oxford Academic","url":"https://academic.oup.com/book/55800/chapter/434346720"}]

Based on the web search results, I found relevant information about Armenian borrowings from Iranian languages, particularly Parthian. While the search results contain references to Armenian etymological works and general information about Iranian influences on Armenian, they don't provide specific details about the etymology of խոստովանիմ (xostovanim) related to *hu-stawan.

However, the results confirm the broader context: Most of the linguistic borrowings came into Armenian from the Northwest Iranian language of the Parthians, and several hundred loanwords were borrowed from Middle Iranian (Parthian, Middle Persian) into Classical Armenian.

The Wiktionary result (item 5) does reference խոստովանիմ (xostovanim) and cites classical etymological sources like Hübschmann (1897) and Ačaṙean's Armenian Etymological Dictionary, but the search results don't contain the specific etymological explanation connecting it to *hu-stawan or the Iranian roots you're asking about.

To find the detailed etymology you're looking for, you would likely need to consult the primary sources cited in Wiktionary directly, particularly Hübschmann's "Armenische Etymologie" or Ačaṙean's etymological dictionary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:13:20.666Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=3695{n+=gsub(/\\f/,\"\")} END{print \"leaf idx:\",n}' ISS_alt_DKS.txt; sed -n '3690,3700p' ISS_alt_DKS.txt | cut -c1-200; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d.get('ISS'),ensure_ascii=False)[:800])\""
}
```


### [2026-09-14T03:13:21.739Z] TOOL RESULT

```
leaf idx: 222
nista- ' paid back' from ‘adjusted, put in its proper place', у 339, 77Y4 ka (muhu da)samyai hadai nistu yanümane thui nāsu u ne tä nistu yana(may)ne ' if we can repay it on the tenth day you ar
niha 'of the navel’, see zaha-.
niharkáü ‘repression’, V 115, 64у5; 6 BS migraha-, later K rss:58 ñaharka. See nihalj-.
nühalamána- ‘reverent’, Z 278:92 Adde náhalamana hämäre ‘they become humble-minded, reverent’; v 113, 35v2 и abátandá u sa-gauravád u nihalamanána hoüstoñdna reverently and with hu
188 nihalj- — nuva
scripts of the Saddharrna-Pundarika, 1949, Куб) lera- nihelamati ' maintaining humble thought’, where Zera- is from dàürava- (Khotan Saka der-, Parāči- dër-) with mati- = māna- 'thinking'. 
nihalj. ‘suppress’, v 148, 131, rbz parstore uihaljindi (dyadic) 'they. stop’, Z 22:142 Aie nihaljāka plur. ‘checking the army'; Z 2:178 date trāmu nihaljd ‘he would so subdue wild beasts�
nihujs- 'sink', participle nihuta-, 3 sing., Z 5'54 nihusdá, Z 5'79 hamtsa klaisyau jsa nisemáiid ku ttädātä náhusdd 'together with the A/efa-afflictions it must be made to cease when the darkne
nühvarr- ‘desire, grasp at’, participle nähvarrda-, present stem, Manj. 147 nūhvarāre dharma vira 'they grasp at
the dharma-doctrine'; v 124, 4v4 pajsamd anähvarremate
jsa "without desire of worship’, Manj. 170 se jsa nühua- rama dharma vira; 3 sing., Z 12793 hà ndhvarrde, ВЗ na virodhayati 'does not oppose' = 'greatly desires'; v 10274 nähvarrde, Tib. lhag-p
{"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "local_file": null, "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
```


## [2026-09-14T03:13:29.607Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '11945,11975p' BQT_v1_pages.txt; echo \"--- leaf:\"; awk 'NR<=11953{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v1_pages.txt"
}
```


## [2026-09-14T03:13:30.204Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ستوان\" BQT_v2_pages.txt | head -10"
}
```


### [2026-09-14T03:13:30.751Z] TOOL RESULT

```
ک رکه (۱ ) شده باشد بعنی سرما خورده باشد
ویع‌بی کابوی‌خوانند - ویسمتی دیوهمآمدماست
که درمقابل برست: - ومودم دلیر وصاحب قوت
وقوی‌بازو را نیز کفتهانم.:
استو ار ۱ بم اول بروزن خشکوار
بمعنی محکم و عضبوط باشد - و آمین و متمد
وامادی‌را نیز کوبند - وبمعنی باورهم حست‌چه
استوار داشتن بمعنی باورداشتن است .
استوان ۲ - بن اولو تالث بروزن
پلبلان » بسعنی استوار است که محکم و مضبوط
واهمین ومعتمد باشد.
استو‌ذان؟ - بن اول و ثاك و دا
بالف کشیده و بتون زده » دخمه ومقبرة کبران‌ر!
گوند .
استود ذ بنم اول واكث و سکون‌تالی
و رایع و رای قرشت شت ۰ هر چهار یاه را گوینه
عموماً و اسپ واستر را خصوصاً .
استون - بر وزج کلکون . بسنی
ستون باشد؟
استوه - بکرلول ونم ثالث وسکون
نانی و راب و ها » بمنی مانده شده و افرده,
ویتنگه آمد - وماند گی وبتنگهآوردن- وملول
بلشد ؛ وجضم اول هم درست است.
۹ پهاری 105111025 معتفد وثابت‌فدم «بونکر*4», 8504087 «بوستی. بندهش۹4*.
ی ون . ۴ - بهلوی 2540080 ,
حرزه اول آن نمعتی استخوان است و دان دسو ند مکان است . چون زرششان استخوان مرده را
پی‌از 1: ن.که ک رکس‌ها ولاشه خوران گوشت جد وی را خوردند - او را ح رکودالی می‌اندازند ,
آن کودال را اسنودان کویند و مجاراً یگورستان اطلاق میشود . در تهران رسم مذ کور در میان
زرشتیان منسوخ شده است
۴ - بپلوی50002, اوستا 50002 بارتولمه ۱5۰۸* فارسی‌نيزستون «یبر که 0۹۰۵.
۵ _ رک : هه واستخوان . وکا فنلسته::
--- leaf:
341
```


### [2026-09-14T03:13:30.803Z] TOOL RESULT

```
4393:     ‫سرون آوردن آب وحر آن کنند‪-‬‬                            ‫کودی استوانه شکل عم‌قی که در زمن جهت‬                    ‫‪۱‬‬
12057: ‫که زخم را و(‪ )۲‬دست ویای شکستهرا می‌بندد‪-‬‬             ‫خستوان‪ = 1‬یبنرماووزلن‌استخوان »‬
12071:                                                            ‫‪۲ : ۱‬ص‪٩۸۱٥‬‏ رك ‪ :‬خستوان ‪:‬‬            ‫«اسفا‬
33707:               ‫ستوان ‪ - ۲‬ببصمراو‬                     ‫سوامان را بیزکفته اند؛ وبفتح اول و ثالی هم‬
33742:  ‫‪ - 4‬امروز بدرجه ای بظامی اطلاق شود که شامل سفرنبه‬                    ‫رکه ‪ :‬استوان ‪.‬‬                 ‫‪۷‬‬
33744:  ‫است ‪ :‬ستوان کم (فایب‌اول)‪ .‬ستوان دوم (دایب دوم) » ستوان سوم (دایب سوم) ‪.‬پابین ترازستوان‪.‬‬
33745:        ‫رکه ‪ 7‬اسنودان ‪۰‬‬    ‫‪- 4‬‬        ‫سوم «استواریکم» است و بالاتر از ستوان یکم «سروان» ‪.‬‬
```


## [2026-09-14T03:13:42.368Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=33707{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n}' BQT_v2_pages.txt; sed -n '33700,33750p' BQT_v2_pages.txt"
}
```


### [2026-09-14T03:13:43.436Z] TOOL RESULT

```
leaf: 563
‫محف استواز استکه بمعنی مضبوط و محکم‬                  ‫چوییرا کوبند که در زیر آن غلطکها سب کنند‬
‫باشد ‪ -‬و بمعتی امین و ممتمد هم هت ‪-‬وباور‬             ‫آونرا برکردن کاوبندند و بربالای غلهایکه‬
                                                      ‫ازکاه جبدااششددبهگردانند تاغله از کام‌جدا‬
‫د جم‬     ‫یت‬        ‫مد‬           ‫کردن و صدیق‬
                     ‫اول وثالی هم آمده ات‬            ‫کردد ‪ - ۴‬وبمعنی ذخیره و پس‌انداز همآمده‬
                                                     ‫است ‪ -‬وجمم کردن مال و برهسمانیدن اسباب‬
‫ولزن بپتان»بممنی‬
               ‫ستوان ‪ - ۲‬ببصمراو‬                     ‫سوامان را بیزکفته اند؛ وبفتح اول و ثالی هم‬
‫‪ -‬ومد رامین‬        ‫ستوار است که ‪ 9‬ر‬                                                               ‫‪۳‬‬            ‫درست‬

                    ‫داشتن باشد ‪. ۵‬‬    ‫باوور‬
                                          ‫‪-‬‬
                                                      ‫شطه‬    ‫خای‬   ‫و‬   ‫پنتم اول‬      ‫=‬     ‫ستش‌شیز‬


 ‫ستودان ‏‪ = ٩‬بضم‌اول بروزن‌جپودان»‬                   ‫سجر‬            ‫دار (‪ )۱‬بتحتالی مجهول ‪7‬‬
‫برر آتش پرستان‬
             ‫عمارتی را کوبند کهبقرس‬                                           ‫است‬   ‫رستاخیز‬       ‫بمعنی‬    ‫‪۰‬‬    ‫خىز‬

‫سازند ‪ -‬و بمعنی کورستان هم مدهاست‌ودخمه‬
                                                                                                      ‫وشر باشد ‪.‬‬
‫را یز گونند ‪,‬بعنی جایی که مرده را در آتجا‬
                                                      ‫ستو د یکر اول و ثانی بواو مجهول‬
         ‫گذار ند ‪ ۹‬؛ ویفتح اول ہما مده اس‪۳‬ت‬
                                                      ‫رسمده» طنموره را گونند که سه ار داشته باشد ‪۴‬‬

‫ستودن ‪ » ۱۲‬بکر ارلبروزن فزودن»‬                       ‫‪ -‬و زر قلب روکش را نیز کفته‌اند بعنی درون‬

                                                                          ‫‪۰‬‬    ‫ه وخا‬     ‫)‪ (۰‬چك‬



          ‫دلیر و ستنبه هو کینه کاه‪.‬‬                         ‫‪ -‬ازابرانیان بد تهم کینه‌خواه‬
  ‫فری ‪. 6° 14‬‬     ‫لفت‬
                    ‫فردوسی طوسی ‪.‬‬

  ‫ومخفف «رستخضیزز» = رستاخیز (هدم‪).‬‬   ‫مصحف‬       ‫‪۳‬‬            ‫!سبنج» (ه‪.‬م‪. ).‬‬        ‫سحف‬
                                                                                       ‫م¬‬‫‪۳‬‬

  ‫سومین از ثلیث‬    ‫‪ .‬مصحف سوا ‪4۷1‬‬      ‫ظ‬     ‫‪-‬‬   ‫©‬           ‫ستار ' ستاره ‪.‬‬     ‫ر‪ :4‬ستا‬       ‫‪-‬‬       ‫‪۴‬‬

               ‫رکه ‪ :‬استوار ‪.‬‬   ‫‪-‬‬            ‫(خدابان) هند » پرورد کار مخرب و فراوالی همت ‪.‬‬
  ‫‪ - 4‬امروز بدرجه ای بظامی اطلاق شود که شامل سفرنبه‬                    ‫رکه ‪ :‬استوان ‪.‬‬                 ‫‪۷‬‬

  ‫است ‪ :‬ستوان کم (فایب‌اول)‪ .‬ستوان دوم (دایب دوم) » ستوان سوم (دایب سوم) ‪.‬پابین ترازستوان‪.‬‬
        ‫رکه ‪ 7‬اسنودان ‪۰‬‬    ‫‪- 4‬‬        ‫سوم «استواریکم» است و بالاتر از ستوان یکم «سروان» ‪.‬‬
        ‫آین جهان چون تاکردون گردان‌شد‪.‬‬                 ‫‪ - ۰۷‬هرده لشود زاشه‪.‬زلده بتودان شد‬

  ‫رود کی سمرفندی‪« .‬لفت فری‪. > ۹۵۳‬‬
       ‫‪imoats ۰‬‏ (مدح کردن ‪e‬‏ تمجید کردن)؛بهلوی ‪22‬‬                 ‫"‪ ۳‬اوستا رشة = ‪۲211‬‬
```


## [2026-09-14T03:13:53.879Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ntxt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in range(545,575):\n    nums=re.findall(r'[۰-۹]{4}', txt[i])\n    print(i, nums[:4])\nEOF"
}
```


### [2026-09-14T03:13:55.216Z] TOOL RESULT

```
545 ['۰۲۰۱', '۰۲۹۲']
546 []
547 []
548 []
549 ['۷۱۹۱']
550 []
551 ['۳۰۲۷']
552 []
553 []
554 []
555 ['۹۰۹۱', '۲۷۲۰']
556 []
557 ['۳۰۳۱']
558 ['۱۰۵۹', '۱۱۷۲']
559 []
560 ['۹۱۲۷', '۵۲۵۳', '۵۵۳۱', '۳۱۷۰']
561 []
562 ['۹۱۷۲']
563 ['۹۱۲۷']
564 ['۲۵۷۵']
565 ['۱۰۱۲']
566 []
567 ['۷۱۳۸']
568 []
569 []
570 ['۷۶۱۱']
571 ['۲۱۳۱', '۰۲۱۸', '۰۱۱۱']
572 ['۹۰۱۱']
573 ['۵۹۵۱']
574 ['۳۱۳۱']
```


## [2026-09-14T03:14:14.123Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== LEW sterilis\"; grep -n \"sterilis\" LEW_1910.txt | head -5; echo \"== LAT sterilis\"; grep -n \"sterilis\" LAT.txt | head -5; echo \"== KLN sterile\"; grep -n -i \"^sterile\\|sterile, adj\\|sterilize\" KLN_1966.txt | head -8; echo \"== SKT\"; grep -n -i \"sterile\" SKT.txt | head -5"
}
```


### [2026-09-14T03:14:14.226Z] TOOL RESULT

```
== LEW sterilis
== LAT sterilis
1481:CGL II 564,18, a das a: pro senectute sterilis. Non expliqn.6; sans antre
60321:ferent d'une langue a 1'autre. II en est quelques-uns qui, malgr^sterilis
60325:sterilis, -e (et arch. sterilus , cf.P. F.419,4; et v. Lucrece,
60338:sterilis intro ad nos, \ grauidas foras exportet. - Usit<? de tout
60341:(= uulua sterilis), Petr.35,3.
== KLN sterile
6509:carbolic,  adj.,  pertaining  to  carbon  and  oil.  — Compounded  of  L.  carbo,  ’coal’,  and  oleum , ‘oil’.  See  carbon,  oil  and  -ic. carbolize,  tr.  v.,  to  sterilize  with  carbolic  acid (chem.)  —  Formed  fr.  carbol-  and  -ize. carbon,  n.,  a  nonmetallic  clement  (chem.)  —  L. carbo,  gen.  -onis,  ‘coal,  charcoal’,  prob.  standing for  *car-dho  and  derived  fr.  E-E.  base  *ker-, ‘to  singe,  burn,  glow’.  See  hearth  and  cp.  cre¬ mate.  Cp.  also  carbonado,  Carbonari,  carbuncle. Derivatives:  carbon-ic,  adj.,  carbon-ize,  tr.  v. carbonaceous,  adj.,  1)  coaly;  2)  pertaining  to,  or containing,  carbon.  —  Formed  with  suff.  -ace- ous  fr.  L.  carbo,  gen.  -bnis,  ‘coal’.  See  prec.  word, carbonado,  n.,  a  broiled  piece  of  meat.  —  Sp.  car¬ bonado,  prop,  subst.  use  of  the  fern.  pp.  of  car- bonar.  See  next  word.
27626:pasteurize,  tr.  v.,  to  sterilize  (milk,  beer,  etc.)  by Pasteur’s  methods  —  See  PasteureUa  and  -ize. Derivative:  pasteuriz-ation,  n.
36755:sterility,  n.  —  ME.  sterylite,  fr.  MF.  (=  F.)  steri- lite,  fr.  L.  sterilitdtem,  acc.  of  sterilitds ,  fr.  steri¬ lis.  See  prec.  word  and  -ity. sterilize,  tr.  v.  —  Formed  with  suff.  -ize  fr.  L. sterilis.  See  sterile.
== SKT
18488:Sterile.  (K.  -  L.)  O.  K.  turi'u.  -  L. tttfUtm^  ace.  of  sUriUs,  barren.
```


## [2026-09-14T03:14:16.183Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BRT staoiti\"; grep -n \"staoiti\\|stao-iti\\|1593\\|1594\" BRT.txt | head -10; echo \"== SNS\"; grep -n -i \"stay\\|stāy\\|xvastuk\\|xvastvan\\|astvan\" SNS.txt | head -20"
}
```


### [2026-09-14T03:14:16.254Z] TOOL RESULT

```
== BRT staoiti
2492:aohqm  saoi:ranqm  vinditayä  mävöya  nipä- rayeinti  .  .  Yt  77.54;  —  vTspanqm/a  att-  • kam   aiaonqm  alaoninqm^a  .  .  ya^qn zaoyasca  fravasayö  Yt./J.i48;    148; .  .  aAmat  haca  nmänilt  .  .  ya^ra  .  .  1 staoiti  Y.io.-j;  —  nbyö  daiiiAubyö  . . ya^-a  ( l'wo')    aim    bavaiti  yaslö    YtÄ47;    /j. 34,  P. /7*;   —    ..  ahmi   nmäne  ..  yaia aAmya  (sv^.  yaAmya)  amtsä  sp^nta  . .  pai-
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  —  sardiiustrahe  .  .  yd  paoiryö  .  . Staat  'Lm  naist  daivS  Yt.  13. 89;  —  yal  nä . .  %ris  "s^n  ufajtuyät  V.  18. 43 ;  —  "hmca *!0  pasca  hü  fräsmSJaitim  (näml  stuyät od.dgl.)  N.  6"^;  imd  so  Öfters.  a)  auch  mit a)  vanhav-'h  aiwi^r^lmahi  's>m  voAa  Vr. J7. 1.  ß)  vaAista-'^:  ahun^mca  vairitn  .  . °s?m(a  vahUtim . .yeAhl.tiätqmca\.6i.\\i3. 8,'Hyuf.S;—jainii  mqm  ahuna  vairya  ..lapa- yäti  mqm  'la  vakUta  Yt/7. 20;  —  6ayqm 'iahe  vahistake  yazatnatde  'sähe  vahÜtahe yasamaide  frasraeimmca  .  .  Y.  20.  5;  — zara^uitrS  ys  paoiryö  .  .  staota  °sfm  ya^
6869:Ikät^  'rynt    masdqm..aat  mr€oH^Xvtxz.,\ jnier  I  1)    "rö  mazda  V.  2.  if.;  usw.;    — j  dim  p9r^sat  sarai^uslrS  -rahe  (statt  Akk.) ' masdi    Nile  i ;    —    wii    mraot  (Stverz-,  [ nnter  1  3)      °rJ    masdä    V.iS.i;  usw.;  — miinm    .  .  y5   gimatte    'rät    mazdai  Yt. ' '''■53;    8.  to',   — frSmraot  °rS  mazda  Y. M.  1; — jiimäi ..paoiryS  maiyänqm  apsnse^ oum    y3     "rö    mazdä    V.  2.  2;  1 ;    —    äat ioxta   *rj  masds  V.  2.  21,  40,  42;  31,  Vr. 3.  3,  Y,  10.  9;  — paiti  sS  aoxta  'rS  mazds A.4.6,  H./.  2,  7,  P.27,  FrW./o.40,  Nik. 2;  —   aite  sl  vä^ . .  "rS  mazdn  främraot zara^ultrai  Y.  7/,  14;  ig.  i,  15;  —  rätayS ..*yqm    °rv  mazdil  xaraisuiträi /ravavaca frä    tara^uitrS  gaiHäiyö  ..  Y,6§.g;  — ja'ia    dim    isat    °rS    mazdh    V.2.32;  — jaia  . .  zaois  mana  yat  °rahe  masdä  Yt. ir).%z;    &35;    —    xmaoi:ra    (sd,    auch fdSt.)   'rahe  masdä  Yt.  7.0,  usw.;  — j;As- maitie  'rahe  mazda  Y._^.  i,  22.4,  23;  — frasasti  °rah*  mazdil  Y.  S.  i;  —  staotala .  .  yat  a^a  'rahe  mazda  Vt.i}.  6;  —  /ava 'ra  mazda  yasrum  . .  vahm>mca  Vr.  21.  a; P._3P;    —    ramasf    ti  'ra    mazda    "hrlsHt pars  anyäis  ääman  Ny,  /.  i ;  Y.6S.X2,  Yt. 7.1,  V.ig.25;    —  fumahl  iyiJmS    *'ra.- wiazdä'"'*    Y.  5>y.  3;    —   yat   zaota    'rsm ma-uiam  yazäiti  N.  70;  Y,  25. 4,  57.  a,  V. 7q.  19,  Vt  6.  4,  77. 18,  Vr.  jj.  I,  i8. 1,  23. 1, G.5.S;usw,;  —  kö  mqm  staoiti  yim  'r^m mazdqm  H.7. 3;    —    'rai  mazdäi  haomq äJoAayamahi  Y.  24- 1 ;  Vr.  //.  16,12.1;  — zbayamahi    JrJnämahi     mqm    ytm     °r>m mazdqm     Yt/2.3(?);    Vyt2.^(;    —    'nm mazdqm    danyo.yas/fmca  (si)    hqm.parl- timca  H-2, 14;    —    ks  itvqm  yim  °rgm mazdqm  . .  mazista  ibaisatiha  tbaisayeiti  V. /iS'.6i*;zitY.(?.8PiiZ.; — mä  zl  ahmt  nmane . .  fnm  i-aocata   mqm  yim  'nm  mazdqm yaia  ..  P.  17;    —    i^a    dim  ^ara-cinasti yim    'nm    mazdqm     .  .    damabyS    Y.  ig. la.        a)  in  Verbindung  mit  andern  Gott- heiten: 'rahe  mazda  . .  varahSus  mananks ..asahe  vahisiahe  .  ,  xia^rahe  vairyehe.. tpmtayB    ärmatöil .  .  haurvatä  amir^täta  , . .  ^ui  urune  gSUs    lalne  .  .  ä^re  °rahe  1 mazda  Y.  70.  z;  /.  if,,  57.24,  Vr.  i/.  16,  j ^-  5-  5«  V.  7p,  1 1 ;  —  -räica  mazdäi  srao- , s.Wa    a^.li    rasnvalta    razilläi   mt^räica Vr.  //.  6;  Y.  4. 2,  Vyt  i4;  —  «Äu  me  'ra , mazda   uäa    üpS  urvar&sca  usia  daine  .  . , VlÄ  29;  23.  a.)  bes.  häufig  mit  den
7269:Schritt  entfernt  ist,  auch  dem  Wasser opfern"  N.  6g.  A)  oft  neben  Feuer, Himmel,  Erde,  Rind,  FQanzen  (usw.):  ma x^ayamna  jasStt  ätnm  . .  äp>m  . .  tarn  . . gqm  ,  .  urvarqmY.g.^y,  42,  11. 1,  2,  5, 9,  10;  —  jia}  . .  vi'iürayat  asmamm  . . np)m  .  .  zqm  .  .  gqm  .  .  urvarqm  Yt  13. aS;  86,  Y.  ig.  8;  —  ahtaatca  apäalca^'> zimaatca  urvarayaatca  gaotca  Vr.  7. 4;- — para  asrntm  .  .  äp^m  ,  .  zqm  .  .  gqJt  ,  . urvarqm  .  .  atr?m  Y.  SQ.2;  —  fravaiayö ya  asmtm^m  viöäray^n  . .  lip»m  . .  zqm  . . gqm  Y.  2^.  1 ;  —  hs  ßptm  staoiti  .  .  zqm . .  gqm  . .  urvarä  . .  vtspa  vohü  H.  /.  3 ;
8472:brauchten Pflanze :  *h<ata  nS  rnhma  bans- mana  ratu/risi  ^ris.uri'ara  (sd.)  cyävaitis aäaya  'rayti  (NP.)  anhsnl  ".  .  wie  gross sollen  die  Pflanzenstengel  sein?"  N.i^o;  — yezi  *paitila  (sd.)  °varh  upa-doo^litt  ratu- /ri/H.ioi.  S.  auch  3.  a)  oft  neben Feuer,  Wasser,  Rind,  Himmel,  Erde  usw. : xshiivayeiti  ätrmt  .  .  ap^m  .  .  gqm  .  .  °rqin V.f).4Z;  33,  i/.  I,  2,  6,  9;  —  haca  a^rat .  .  Opal  .  .  z^mat  .  .  gaot  .  .  "rayiJf  V. ;/. 10;  —  aHiS  .  ,  apas^a  ttmasca  'rayhsca Ytij.jS;  aS.  86,  Y.ytj.a,  8;  —  asnäalca apäatca  z»mäatca  'rayüatca  Vr.  7. 4;  — hs  äp?m  staoiti  .  ,  zqm  .  .  gqm  .  .  'rqm H.  7.3;  —  ys  gqmcä  ahmcä  dät  apascä 'räsctl  vat^kli  y.  3-^.1 ;  —  yS  gqm  tasö (sd.)  apaslS  °rasca  Y.si-T,  —  vlspä  bal- iazä  apqmca  gavqmea  'ranqmca  Y,52.  a; J2. 7 ;  —  nasuspaim  .  .  äsirysnie  .  ,  apasca Zimasca  'rayäsca  V.  6.y,  /.j,  2/.3,  Y.  j.  16, 2.16,  Vr./Ö.3,  G.2.6;  —  ntzbayemi  zqm .  .  äppm  .  .  'rqm  asaonim  V,  ;p.35;-  — imat  vö  sps  jaiüyemi  . .  tfmO  . .  'rä  Y.
10142:—  yS  astm  sfaeili  hö  apsm  staoiti  ..zqm  urva  dämi.dälJYt.i4.^^; — '/«/ äköSw,4j" °am  .  .  urvarä  .  .  vispa  vo^B  H./.3;  Y.  urvämm  yazamaide  Y.16.4,  26.^,  8.2.14^ 7/.  9;  —  diiidi  msi  yt  "qm  iasj(ßd.)  Q.  4-6; — yä  x/n?vi/ä  (_sd.)  '7uscä  *urTq- apaicä    urvarasla    Y.  5/.  7 ;    —    ahurfm   mm  Y.  28.  i  '*';  —  i'iil  Ht  yazamaidi  "Sus
12778:*frä  *vta  *nar?  *gSrt^Sil , ,  vTsaiii  'im frarfrsrayn  . .  N. /i);  —  tä  hasHi  upa.- sbayäte  .  .  tä  Al  Jasanti  yezi  sl  bavainti anäair?t3  .  .  tÜ  'im  ava  ni/ravayeinte  Yt Jj.  ögf.;  V.  5.  34;  —  haomS  uxsyeiti  sta- vanS  aäo  nä  yS  'im  staoiti  Y. /0.6;  Yt 10. 16  (VfOT)'';  —  oParata  narö . .  myazä»m ^yBi.dim  harfkäna  (sd.)  Y.  Ä  2 ;  —  tni\nm . .  yatära  vä  'im  paurva  fräyazäiti  Yt  lo. 9;  18;  — yirnl!  kur^naol yaia  -im  *jiasat< (sd.)  ahurB  ,  .  V.  2. 3a;  —  psurvS  .  ,  yat< 'im  usla  uzävqnayat  (sd.)  .  .  ^ra^aonff Yt5.6i;  J0.68,';p.39.  77,V.4.i7,  i^-'oo, 103,  Y./^.ia,  14,  N.i^;  —  *tanu.pn%B . zaota  dakma  u^.sraetarö  yezi  -im  tatm.- fmh»m  *v^an .  .yezi  äat  'im  tiBii  ianu.- p»r3k»m  *v^ar3  N._yß;  vgL  jdi';  —  miinm ,.yai  Vä  'im  aiwi.druzaiti ..  nmünB.paitis YLJ0.i7f.;  V.Äioo;  —  hö  imqm  tarn aiwifvai  .  .  avi  -im  (ASf.)  sifat  V.  2. 10; 5.  if.';  —  y^t^i  tanüm  afiayeiti  (näml, aräif)  a0i  °im  nSii  räsayente  Yt io.%\\
18699:Y.5/.8; — ka^usiit  na  a/avm  ia:^g(sd.} aahat  Y.  47.  4;  —  s^ä'irByj  (sd)  nä  3?ä- irpm  daidttä  Y-4S-  'i  —  puxi^mät  na arxüisam  tanäm  piryäte  V,  4.  1 7 ;  — dansa  nä  .  .  tiyete  .  .  /rasi/maüls  (sd.) j  P.5Ä;  N.  JOÄ;  —  *srao>ra  *na '*> gäianqm '  ratu/ris  paitxMsti{iA.ya  ..  N.  22; —  nöit na  pourüS  (sd.)  dngvatB  tyät  axhtusB  Y. 43-  15;  —  ai:a  nä  yj  dim  staoiti  . .  Y. ;o.6; — akt  tl  nä  * sravaahB aframar»nii (sd.)  . .  N.  22.  a)  besonders  nach  dem Fron,  a)  inlerrog.  und  ß)  reL;  a)  lOm nä'"'  .  .  mavaitl  (sd.)  payUm  dadai  Y. 46.  7  'ä;  —  iavham  nä  gä^anam  . .  ara- tu/ris^.3T,  Y.p.'asPüZ.;  — ^ä/(Sp.436) nä  *daBvayasnäi  . ,  gSu?  a-iäitya  (sd.) ästryäü  ti.lS;  *i6"\  i-j,  Sl.Ä2a(?);  — cvat  nä  * ai'^rapaitim  (sd.)  upsisaf  Vi.  11; —  *cvata  (sd.)  nä  *mt^ma  vaca  .  .  ratu- frii  N.  27;  66,  6y,  106,  *io8"^;  —  caili nä  aiDohe  pasvB  (sd.)  *zao%rä  barät  N. 65;  —  *kahyäcfl  nä  dakmanqm  xaekräöa (sd.)  ..  Vi.  4a.  ß)  yqm  b'a  nä  fraaur
18700:hanfa  .  .  afym  staoiti  "wenn  man  , ,"  H, J.  7 ;  —  hyat  n  a  /ryli  vasiamnö  isvä  (sd.) daidlt  Y.  43.  14;  — yat  nä  paurva  frahda (sd)  .  .  fi-amaaaiti  V.  18.  40J  34,  37,  46, 49i  54  (Sp-  Sao  u.);  —  ya%a  na  snaüi/ . .  nifmatfm  (Sp.  500  m.)  paiH.valnoit  P. 21;  YL13.JO,  71,  aa)  In  gleichem  Sinn erscheint  auch  NP.:  äai  mqm  narB  . . yazmte..  darrfB.yast»m(sd.)/a  .  .  H.2.  14; Vd.iS;  —  ^aj  ta  (Sp.  6ia)  nara  yaos- dayqn  aahm  .  .  ya  nasaum  avahistät "können  die  Männer  (sva.  kaim  man)  puxi- fizirt  werden  .  .,  wenn  man  . ."  V.  5*.  33; 35.  97.  7-"3.  "5-
19389:—  yaha  at^m  laurvaymi  vupe  yätavB  ,  . yat  mqm  na^ti taurvayat\x,i.^; —  Rica %wqm  cakana  .  .  htm  mqm  "/aiaaa  H. 2.12;  —  a  mqm  ava%a  vtrytunie  yaha anyasat  arlänS  avt  xhtdrh  xla%riAa hqm.V3r3navaititi  V./Ä.32;35;  —  s.  noch bei  3.  zu  I  b):  uHa  ba ytm  halahi  ula mqm  upatihal^i  Ytl^.j;  ~  mqm  sT mainyae yasaifm  Yt  10. 108 (?).  zu  a): paiti  mqm. .pinsanuAa yim  da%väaAim . . V.  /<?.  7 ;  Yt.  12. 3;  —  zugleich  zu  1  a):  y3 af>m  staoiti  hs  mqm  staetti  yim  aAurtm mazdqm  H. /.  3;?. /jj  —  ax^m  dalqm  .. tis'tnm  . .  av3ni?m  . .  ya%a  mqmcij  yim aAunm  masdqm  Yt  8.  50.  2)  AbL; b)  nur  u)  im  j  Aw.j  mana  als  AbL;  zu  2) :  at^B mana  yat  zardhusträi  V.2.r.  3)  Dat.; Bi)  imgAw.j  ei)«a/4)'a'';zu  i  a):  ääidi .. vikaspai  is^m  maibyäcä  Y.2Ä7;  8,  4g.%;
== SNS
3325:.fr/^t^ UiW>. 215) astvant 
3337:xustuwan : ^j/ .(j^^*) astvan:^ II, 43) 
3339:,0*1*^** , j^ l i i-l:astvan bQdan: wwnO t^Jtf ** 
8425:\6/U>S (GNPE. 49) /bhray- ^^ ./Stay-: t- 
9051:-pwst : jsk (AiWb. 878)? prstayt.L-pasti- :fc- 
10773:.j UtI .4 ..**W^b-:stayidar: *— 
12787:•VH^.Ui^.458)krstay: .^^ Karita _ , fc 
14981:;#»*U*' MiW». 1440)vitastay- -.L v £. tastay-:^ 
17077:■f/lf^ (AiWb. 748)distay-: i ^t5-* iB disti- ttm 
28341:rathestha- 41/16 vitastay- 268/5 
28452:distay- 313/13 
28504:prstay 139/7 
28674:krstay 220/7 
29014:vt.tastay- 268/5 
29861:astvat-/astvant 31/1 
31456:stayad 178/6 
31457:stayldar 177/17 
31458:stayisn 178/12 
34031:astvan 31/10 
34033:astvan bQdan 31/14
```


## [2026-09-14T03:14:21.968Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3320,3350p' SNS.txt"
}
```


### [2026-09-14T03:14:22.056Z] TOOL RESULT

```
,astvat-£« (>** -^) J^j^ -^j-*:omand + (xj'j 1 * : ^) 

.fr/^t^ UiW>. 215) astvant 



o'>^- ! : ast jlo-if-i . j iji^- 1 . 4^« I . *i-A :astag: li« M 

(CiVPF. 20)stag: J -7asthi,asthan s j|Sj^ast-i <fl 
ast : V CJVir. Man. II, 47X *st: >;<* {AiVb. 211) , 



{.Mir. Man. ^stw'n-.^ii . (66 ofc*£*j* < &ff) »/stav+a:L- 
xustuwan : ^j/ .(j^^*) astvan:^ II, 43) 

,0*1*^** , j^ l i i-l:astvan bQdan: wwnO t^Jtf ** 

, a .6-f /Yo^ -r/\<S .o^O-V'O^^J* 

•Y/Y^ f/6 J 

{Mir. Man. II, 50)dydn :>;fc dtd:^ IJZyTWN,t: fii) 
.fjj»>*»Jdit :^ (Wtr.Jtan. Ill, 54)dydri«^ 

vo .rr/io-^ w/a^ ■ M-fA-f6-*r-i/^ 

.fA-ffi-f'T/T ^ .•^.Ju<^ai :n§ did: V"Y**»* ^
```


## [2026-09-14T03:14:32.282Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,p in enumerate(t):\n    if re.search(r'\\b159[0-6]\\b', p[:4000]) and ('stav' in p or 'staot' in p):\n        print('leaf',i, p[:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T03:14:33.451Z] TOOL RESULT

```
1041
leaf 867 tarÖjSra-  No.  I.  —  VIL lu  got.  s/ahu;  s.  FlcK  VglWb
leaf 869   den  Wunsch  nach  der  langen  Dauer des  köstlichen  Das
leaf 870 t  stuyi{\%.y^  tüSil  ahmät *ä  *syänlm(sd.)..x/tä  "..gelo
leaf 1017  havaiahäica .  .'nyäica yat  saolyantqm  Vr.5.  i. Ableit.
```


## [2026-09-14T03:14:35.608Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[869]\nimport re\nprint(p[:2500])\nEOF"
}
```


### [2026-09-14T03:14:36.704Z] TOOL RESULT

```
  den  Wunsch  nach  der  langen  Dauer des  köstlichen  Daseins,  von  dem  gesagt ist,  dass  es  in  deinem  Reiche  sei"  Y. 4?-  13''-  a)  von  einem  einzelnen Seienden  'Geschöpf:  ^/vzos  .  .  pdhs  . . /laihymg  (sd.)  *ä  *stisi>  yfng  *a.saän ahurs  Y.  43-3;  —  Aspla  gSuscä  *asaiiAäcä asaonasca  asävairyisiä  stsis  "er  ist  der Vater  des  Rinds  und  des  A!a  und  jedes zum  Asa  gehörigen  männlichen  und  weib- lichen Geschöpfes"  Y.  5Ä  4.  a)  mit  GS. asaonö  (Sp,  251  u.):  u^la  paoiryam  asaonS stXm  yasamaide  ".  .  das  erste  Geschöpf des  Heiligen*'  . ."  '^1.18.1;  —  kai^yä- var?S3m  (ASm.!)'J  .  .  aiäonS  stim  G. ?.  7-  3)  von  der  Gesammtbeit  der Seienden  'Schöpfung,  Welt":  zara%ustr-7m .  .  gal%yayä  stsis  ahUmca  ratumca  "den Z.  .  .,  den  A.  und  R.  der  materiellen Schöpfung"  Vr.  2.  4;  4;  —  zara%ustraAe . . ys  paoirys  stöii'  astvai^yä ..  Yt.  13.  Bg  ii ;
—  asmamm  ..  *gaä^Im  *gaH&yayä  stSis Vr.  7. 4.  a)  mit  GS.  aiaone{^^.  251  u.): yaca  upairi  (sd.)  iS  akarana  anayra  a^acnS Sil/  aSi  Yt.  Ä",  48;  —  ^antim  trvamm mainyava  stx/*asaonS data  .w(Sp.a76ni.) V.  2.  igPüZ.  et)  mit  vlspa--.  vTspqm asaenS  stim  .  .  mainynfm/ä  gaihyqmcä Y.  3S.i;Vt.  16. 1 ;-- vlspqm  asaons'stXm haitlmca  bavairUlmca  büsydntlmca  Y.  ip.g;
—  vJspayä  asaonS  stöis  haihysüa  bavqi- %yaica  büiyqikylUca   Y. 52.1,  68.22;  —
dby  Google
^^593
*siay-
stav-  mit  US
1594
frad^si  vUpayh  aiaonS  stöi!  hamisße vispayä  drvats  siBii  Y.52. 4;  4.2,  ÄS, 55.3,  70.6,  Vr.n.  I,  Yt./.2i,5.89,  //.17, V.  jo.  5,  F.  26,  b)    mit    GS.    drvati^
(Sp.  777  o.)  und  vls^a-.  ravasca  .  .  äfrX- nämi  -vlspayh  aiaenS  stSis  qsasca . .  vlsfaya drvaW  siDis'Y.  8.  8;  52.  4,  61.  5.  4)  sva. 'Besitz,  Hab  und  Gut'(?):  asavatam  mahr- ka^äi  aom  Hhr>mca  *stimca  "um  den Gläubigen  zu  verderben,  ihn  und  sein Geschlecht  und  sein  Hab  und  Gut"  Yt. ig.  la.  LS.  stsi,  Sil  als  Inf,  sbes,
KompA.,  E. ;  AbleiL  —  ai.  stäy-  m.  (?,  LUDWIG Rigvcdi  5.  220);  lat.  caele-slisli  'qui  est  ir caelo'.  —  Pü. :  gc/ai  (?,  geschr.  ddt  d),  Sü, : paiiküh,  sj-i/ih;  E.  noch  No.  2,  4  und  Komp., Ableit.  —  i)  Nur  Y.  43-  3,  G.  3-  7  und  Y, Jif.  4;  sn  der  letzten  Stelle  handelt  ce  Eicb um  den  Gegensatz  von  männlich  und  weib- lich; vgl.  ^ääman-  No.  2.  —  •)  Pü. : /3  kämak isläl,  Sfi. :  sveechayästu.  —  Sl  NA.  äsßl;  %.
```


## [2026-09-14T03:14:42.744Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (869,870):\n    p=t[i]\n    for m in ['loben','preisen','staoiti','stav-','staomi']:\n        idx=0\n        while True:\n            j=p.find(m,idx)\n            if j<0: break\n            print(i,m,'|',p[max(0,j-200):j+200].replace('\\n',' '))\n            idx=j+1\n            break\nEOF"
}
```


### [2026-09-14T03:14:43.791Z] TOOL RESULT

```
869 loben | mpForm  zu  'slhilal- (ai.  slhilay-);  IF.  ;-.  70.  —  Vgl.  'j/o-, •  j-,  g,  Stav-  V.  'preisen'.  Praes.  i  slav-i stv-'K  —  PPfP.  'siSfa-;  PFP.  'staota-,  Inf. staomaine. 1)  'preisen,  loben,  besingen':  staomi maly^mca  värinüa  .  .  slaemi  garayS  .  . staomi  zqm  .  .  slaomi  z)mS  .  .  laramm Y.  10. 3  £  a)  bes.  Gottheiten:   haoms uxsyeiti  stavanS'^  a%a  (sd.)'  nS 
869 preisen |  'Stehen,  Treten  (usw.)'. KompE.  —  Zum  V.  sli:  —  ai.  'slhay-  f.  — Aus  «r.  *'slAai-,  der  KompForm  zu  'slhilal- (ai.  slhilay-);  IF.  ;-.  70.  —  Vgl.  'j/o-, •  j-,  g,  Stav-  V.  'preisen'.  Praes.  i  slav-i stv-'K  —  PPfP.  'siSfa-;  PFP.  'staota-,  Inf. staomaine. 1)  'preisen,  loben,  besingen':  staomi maly^mca  värinüa  .  .  slaemi  garayS  .  . staomi  zqm  .  .  sla
869 staoiti | esingen':  staomi maly^mca  värinüa  .  .  slaemi  garayS  .  . staomi  zqm  .  .  slaomi  z)mS  .  .  laramm Y.  10. 3  £  a)  bes.  Gottheiten:   haoms uxsyeiti  stavanS'^  a%a  (sd.)'  nS  yS  dim staoiti  .  .  Y.  /o.  6 ;  —  yäha  mä  (näml. haotmni)  aparaät  saofyantB  slavqn^'*  Y, g.2;  —  fravasayö  ..  avat  avS  zixSnS- nhimna  (sd.)  ks  «J  stavSp''  kü  yasäite  ks ufyät  Yt. /j.4
869 stav- |   3S.i;Vt.  16. 1 ;-- vlspqm  asaons'stXm haitlmca  bavairUlmca  büsydntlmca  Y.  ip.g; —  vJspayä  asaonS  stöis  haihysüa  bavqi- %yaica  büiyqikylUca   Y. 52.1,  68.22;  — dby  Google ^^593 *siay- stav-  mit  US 1594 frad^si  vUpayh  aiaonS  stöi!  hamisße vispayä  drvats  siBii  Y.52. 4;  4.2,  ÄS, 55.3,  70.6,  Vr.n.  I,  Yt./.2i,5.89,  //.17, V.  jo.  5,  F.  26,  b)    mit    GS.    drvati^
869 staomi | - (ai.  slhilay-);  IF.  ;-.  70.  —  Vgl.  'j/o-, •  j-,  g,  Stav-  V.  'preisen'.  Praes.  i  slav-i stv-'K  —  PPfP.  'siSfa-;  PFP.  'staota-,  Inf. staomaine. 1)  'preisen,  loben,  besingen':  staomi maly^mca  värinüa  .  .  slaemi  garayS  .  . staomi  zqm  .  .  slaomi  z)mS  .  .  laramm Y.  10. 3  £  a)  bes.  Gottheiten:   haoms uxsyeiti  stavanS'^  a%a  (sd.)'  nS  yS  dim staoiti  . 
870 loben | yänlm(sd.)..x/tä  "..gelobe  ich  das: .." Y./2.3, mit  aoi  dnwS.,  mit  Inf.  staomaine:  aoi mqm  staomaine  stäibi  ya%a  mä  aparaai saoiyanis  stavqn  (s.  SimpL)  Y.p,  2, mit  apa  'sich  abgeloben,  etwas  ab- schwören'; a)  mit  Akk.:  apa.stavanuka^ .  .  dainqm  mätdayasnim  Y.ig.6;  —  nsi^ ki  {als  Akk.)  apastavUne  .  .  damqm  . . V.  ig.l-  b)    mit    haca  und   AbL:  yS hala
870 staoiti | Y.ig.6;  —  nsi^ ki  {als  Akk.)  apastavUne  .  .  damqm  . . V.  ig.l-  b)    mit    haca  und   AbL:  yS hala  dainaySt  mäzdayasnsit  *apastv3ii^ N.4I- mit  3  i)  dnwS.  i:  vankraynis  kinttm *ästaoiti*'>  Adhra  ana  gäiwya  vaca  Y. if».  igj  —  S  tl  (statt  Akk.)  aitihe  Jraca stuyi^''  Y.1.21.  2)  Med.  'sich  ange- loben an  — ,  sich  einschwören  auf—'  (Akk.): yat  tipar»hacat  
870 stav- | .  Sri/  ahm upa.stuyüt  V,  iH.  43;  —  satgm  asö.stüitinqm upastvBis^  Y.  ig.  32. mit  US  'sich  feierlich  lossagen  von  -, abschwören',    mit   Abi.:    us  güi/  stuyi''> dby  Google '595 stav-  Schluss 'Star-  Noten 1596 tayaaüä   hazafihaüa  us   mazäayasnanqm  \ vTsqm  tyanayal{%Ä.)cä  vivapaila  Y.  12.  i.     ' xaitfrä  1)  dowS.i ;  a  ff  (statt  Akk.)  atriAe , /ra^a  stuyl'1 
870 staomi | ol.:  masda- yasnS  .  .  fravaräng  (sd.)  ästatas^S  fra- varstascä  Y.  12.  8;  —  *spayeiti  .  .  dama matdayasnis  nars  ästavanahe  bandim V.J.  41. mit  upa  1)  dnwS.  i:  vXspe  haoma tipa.staomi  Y.  JO.  17;  2';  —  ydhra  bäha upa.staoiti  haomake  .  .  ü^nm  dasvan baisas»m  Y, /o.  7;  VytJ9;  —  s.  noch PFP.  2)  dnwS.  2:  yai  nä  ..  Sri/  ahm upa.stuyüt  V,  iH.  43;  —  sa
```


## [2026-09-14T03:14:53.943Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D8%B1%DB%8C%D9%84%DB%8C%D8%B2%D9%87/",
 "prompt": "What do the Persian dictionaries (فرهنگ معین، لغت‌نامه دهخدا) say for استریلیزه — the definition and the origin tag (e.g. [فر.] French)?"
}
```


## [2026-09-14T03:14:55.245Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AE%D8%B3%D8%AA%D9%88/",
 "prompt": "What do Persian dictionaries (دهخدا، معین) say for خستو — definition and any etymology/origin note (Pahlavi form)?"
}
```


### [2026-09-14T03:14:58.020Z] TOOL RESULT

```
# Dictionary Definitions for استریلیزه

Based on the content provided:

**فرهنگ معین** defines it as:
> "(اِ تِ زِ ) [ فر. ] (ص . ) ضدعفونی شده ، سترون ساز"

This indicates the term originates from French [فر.] and means "disinfected" or "sterilized."

**لغت‌نامه دهخدا** is mentioned as part of Abadis Dictionary's resources, but no specific definition from this source is provided in the page content shown.

The فرهنگ معین entry clearly marks the origin as French and provides the Persian equivalent meaning sterilization or disinfection.
```


### [2026-09-14T03:15:00.804Z] TOOL RESULT

```
# Persian Dictionary Definitions of خستو

## Primary Meanings

According to the Dehkhoda and Moein dictionaries presented:

**Dehkhoda** defines خستو with two main senses:
1. "دانه میوه ها را گویند" (the pit/kernel of fruits like apricots, peaches, dates)
2. "مقر. معترف" (one who confesses or admits; an acknowledger)

**Moein** provides: "مقر، معترف" (confessor, one who admits/acknowledges)

## Etymology

The page notes a Pahlavi origin: "خوستوگ xwastūg" where the ū represents a "پساوند بازخوانی" (reconstruction suffix). The Pahlavi suffix was "اوک ūg."

The word appears to derive from the root خسته (to weaken/exhaust), with users noting connections to Indo-European etymologies related to bone/kernel meanings through older language stages (Avestan and Middle Persian).
```


## [2026-09-14T03:15:50.988Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN 719\"; sed -n '6294,6310p' HRN.txt; echo \"== MON استوان\"; grep -n \"استوان:\" MON_part1.txt | head -5"
}
```


### [2026-09-14T03:15:51.134Z] TOOL RESULT

```
== HRN 719
719. ftitTiden, sutä(fe7i 'loben, preisen*, Praes. sitäy-ew,
sifäyis,
aw. i/^stav-y staomi preisen ; phlv. stätaUj stät/ttan,
stai/(i)sn ; ai. \/'stav-^ xtätiti,
oss. sfatm 'loben, rühmen', d. sfitd, t. sfjd 'Lob,
Ruhm' (230); af/. L\V. stayal; wa/. sto-amy siyn. sar.
stdu-am.
720. sutöVy ustör 'Ross' (Srihn. Calc. 1373 Vors 10; Vts
und Ramm, S. 52, V. 4 v. u.).
aw.staora- 'Zugtier; phlv. s^ör 'Zugtier, aber auch
lioss' (Nöldeke, Kärn. 40, Note 5, vergl. störpcVf^
störgäSj ebendas. S. 43 bezw. 41)-); skr. sthätirin^
'Lastpferd, Lastochs (spät); got. st'mr \Stier'.
oss. t. sturtä 'Vieh' (233); kurd. zaza L\V. estör,
dujik. ästori 'Pferd'; Titr. LW. istorr^ astor 'Pferd',
si;'n. stör, sar. stdur^ stdor 'Zugtier, ausgowachscMio.s
Rind', ya/n. «li^wr 'Schaf, Vieh überhaupt' (Tomaschok,
== MON استوان
12586:استوان: 05-0-50 [- ستوان] (ص‌مر.)
```


## [2026-09-14T03:15:52.990Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (644,645,646):\n    p=t[i]\n    print('--- leaf',i, p[:200].replace('\\n',' '))\n    if 'sterilis' in p:\n        j=p.find('sterilis'); print('HIT:',p[max(0,j-700):j+500].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T03:15:54.064Z] TOOL RESULT

```
725
--- leaf 644 640                                                    ster-    Seite,      Reihe      u.    dgl/^   aisl.    sirqnd              Strand^,   ags, strand, spatmhd. strant      {-d-),    nhd. Strand,   
--- leaf 645                                                             ;                                                                 ster-                                            641        got. stairo   
--- leaf 646 642                                     sterg-, sterk   (8)tel-         lit.   irasai   „allerlei     Moderndes, Verdorbenes^S trasza ^Moder^^, trqsa j^Diinger^^, tr^tu, tresau, tresti „trockeii faule
```


## [2026-09-14T03:16:03.713Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[644]\nj=p.find('unfruchtbar')\nprint(p[-1800:].replace('\\n',' '))\nprint('=== leaf645 head')\nprint(t[645][:900].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T03:16:04.789Z] TOOL RESULT

```
      aus feind- lichen WafiPenriistungen errichteter Siegeshiigel" leitet auch iiber zur Bed. der germ. Gruppe    (s. J. Schmidt Yoc. II 286, Pick III^ 502, Persson Beitr.  788) von ags, streon n. „Schatz, Reichtum, Gewinn, Wucher", as. gistrkmi n. „kostbarer Erwerb oder Besitz*', ahd. gistrkmi n. „Gewinn“, wozu De-  nominativ as. gistrinnit „ausgeschrauckt“, ags. strJenan, streonan „erwerben, erzeugen“; ahd. gistriunan „lucravi", mhd, strhinen „schnopperad umher- streifen",nhd. bair. streunen „nach guten Bissen, kleinen Yorteilen umher- suchen'^     strune „Gassendirne“ eig. „die umherstreifende" (wohl auch                iid.  letztere Worte durchaus auf der Bed. „lucrari" beruhend, und nicht auf „sich       ausbreiten,       sich   zerstreuen,       palari,   vagari";    nicht    nach Palk-Torp u.    str^m zu '^sreu- „flie6en");      ob hierher skr. strovo „Haufe                vom Sturme herabgeschiittelter Friichte", kroat. strovasiti ,,streuen“              als   Erbwort gehore, ist wegen der geogr. Be- schrankung sehr fraglich.    Wahrscheinlich aksl. ostridti^ ostnijati „zerst6ren“ (*„auseinander streuen''; J. Schmidt Yoc. II 286).    6. ster- „unfruchtbar“, alte                  Sonderan wen dung von ster-            ,,steif“.       Ai. start-h       f.    „unfruchtbare Kuh, Starke";      arm.    sterj ,,unfruchtbar,            von Tieren", auch sterd (Gdf. *sie)'-dh-o-,         -io-; Hubschmann Arm. Gr. I 492 f., Pedersen KZ. 38, 224, Scheftelowitz BB. 29, 31 f., Persson Beitr. 435 mit Anm. 1);      gr. orsiQa      „unfruchtbare", oregapog „unfruchtbar" (und „starr");                       f.       alb. stjere   ,junge Kuh, Lamm" (G. Meyer Alb. Wb. 41 6f. mit Zubehor);      lat.   sterihs „unfnichtbar" (Spuren einer Bed. .,starr" bei Persson Beitr. 428 a 2); 
=== leaf645 head
                                                            ;                                                                 ster-                                            641        got. stairo       f.       ,,iinfruchtbar‘^         ahd.     stero    „Widder‘';    mhd.   sterlce,   stirlie  ,,junge       Kuh, die noch nicht geworfen hat‘';      nhd. Stdrhe^ ags.             stirc,      styrc „Kalb“;        isl.   stirtla „unfruclitbare   Kuh“;      bulg. sterica „Gelte“.      Curtius 213, Pick                      146, 570,     III^ 4S5f., Persson Wzerw. 57, 63, Beitr. 428ff.   7.    (s)ter-     in ^Yorten           fiir    steife    stechende Pflanzenschafte, wohl zu ster-            „starren,   steif      sein“        (kaum „durchboliread“, zu     ter- „durchdringen“).       Abg. str^nh „stipula‘';      ai.    tna-m „Grashalm,                  Strob,     Gras, Kraut'^;        gr.
```


## [2026-09-14T03:16:11.153Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (623,624,625):\n    p=t[i]\n    if 'loben' in p or 'steu' in p[:300]:\n        j=p.find('loben')\n        print('--- leaf',i,p[:120].replace('\\n',' '))\n        print(p[max(0,j-900):j+700].replace('\\n',' '))\n        break\nEOF"
}
```


### [2026-09-14T03:16:12.077Z] TOOL RESULT

```
--- leaf 623                                                  steu-                                                619  Stengel"; mit
                                                 steu-                                                619  Stengel"; mit der Bed.-Farbung von                     lat.   stupere,   ahd. stoharon, auch          dt. „betroffen sein", aber mit ausL Media hinter                     dem Nasal Tzagarerviufiei na-    *   QacpQOveT, fipdQrrjxsv Hes., rvu^oyegeov' io^aroysQcog xal jzagrjXXayjuivog                            Tfj diavoia Hes.,       ysgovra rvp^ov  Pedersen KZ. 39, 363; daS nach Meillet                                          (s,  Msl. 9, 154, Pedersen aaO., zw. Persson IP. 35, 209 arm. fmbir „BetaU“ bung, betaubender Trank", fmbrel „obstupefieri“ aus nachststehendem ^hiynp- erwachsen
```


## [2026-09-14T03:16:14.621Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/استریلیزه/' --note 'page 481, root Ster 4, node #5: Mo'\"'\"'in marks استریلیزه as [فر.] French, \"ضدعفونی شده، سترون\"'; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/خستو/' --note 'page 481, root Steu 1, node #3: Dehkhoda/Mo'\"'\"'in خستو = مقر، معترف; Pahlavi xwastūg'"
}
```


### [2026-09-14T03:16:17.849Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e27bd4fadba33d02.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bff803c5abf161c8.txt
```


## [2026-09-14T03:16:21.069Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (623,624,625,626):\n    p=t[i]\n    j=p.find('preisen')\n    if j>=0:\n        print('--- leaf',i,p[:100].replace('\\n',' '))\n        print(p[max(0,j-800):j+800].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T03:16:22.931Z] TOOL RESULT

```
--- leaf 624 620                                               steu      (s)teg-    u. stif, stuh, stupe, st0p,  
620                                               steu      (s)teg-    u. stif, stuh, stupe, st0p,               Vf. LEWb,^ u. stupa, stupeo, stuprum^ tituho, Boi- sacq    u.    rvmco,  2.   steu- jjlaut preisen^.      Ai, stauti, stavate usw.               „lobt,     preist*^,   Ptc.    stutd-h ,jgepriesen% stuti-h „Lob,     Preis‘^,         stdfdr-    „Lobsanger“ usw.,            av. staolti „lobt,              preist,    besingt; betet",      Ptc,      stiita-^      stuiti-^   staotar-    usw.,     erweitert         ai.        stobhati    j,preist,          dazu wahrscheinlich gr. orevzai „(^ruhmt sich) verspricht p^ahlend^^ jauchzt"^; Pick   145, 334, L, Meyer Hdb. IV 177 f., Prellwitz^ s. v., Giintert Reimw. 36a 1; das gr. Wort nicht wahrscheinlicher als „stellt sich zu etwas an“ zu einem "^steu- ==^ sta- „stehn“.  steu(a^)- „sich verdichten, sich ballen“.                          Oder staii, stdti      stu-1
```


## [2026-09-14T03:16:28.428Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '36750,36756p' KLN_1966.txt | cut -c1-1200"
}
```


### [2026-09-14T03:16:28.492Z] TOOL RESULT

```
stereopticon,  n.,  a  double  magic  lantern  pro¬ ducing  dissolving  views.  —  Compounded  of stere-  and  Gk.  otttixov,  neut.  of  oixxixds,  ‘per¬ taining  to  sight’.  See  optic, stereoscope,  n.,  an  instrument  blending  into  one image  two  pictures  of  an  object,  so  as  to  give  the impression  of  solidity.  —  Coined  by  the  English physicist  Sir  Charles  Whetstone  (1802-75)  fr. stereo-  and  Gk.  -axomov,  fr.  axo7TEiv,  ‘to  look at,  examine’.  See  -scope.
Derivatives :  stereoscop-ic,  stereoscop-ic-al,  adjs., stereoscop-ic-ally,  adv.,  stereoscop-y,  n. stereotype,  n.  (print.)  —  Compounded  of  stereo- and  -type.
Derivatives:  stereotype,  tr.  v.,  stereotyp-er,  n., stereotyp-ist,  n.,  stereotyp-y,  n. stereotypography,  n.,  the  art  of  printing  from stereotypes.  —  Compounded  of  stereotype  and -graphy.
steric,  adj.,  spatial.  —  Formed  with  adj.  suff.  -ic fr.  Gk.  oTEpeop,  ‘solid’.  See  stereo-, sterigma,  n.,  stalk,  filament  (bot.)  —  ModL. sterigma,  fr.  Gk.  axr, ptypa,  ‘a  support',  from the  stem  of  axyjpi^av,  ‘to  prop,  support’,  prop, ‘to  make  firm’,  which  is  rel.  to  oxspeo?,  ‘firm, solid;  stiff;  hard’.  See  stereo-  and  -ma. sterile,  adj.,  1)  barren;  2)  free  from  living  germs.
—  L.  sterilis,  ‘barren,  unfruitful’,  cogn.  with  OI. start  ft,  ‘a  barren  cow’,  Gk.  axepEo?,  ‘firm,  solid; stiff;  hard’,  axetpa,  ‘a  barren  woman,  a  barren cow’,  axeptipoi;,  ‘firm,  hard,  sterile'.  Arm.  sterj, ‘unfruitful,  sterile’.  Alb.  stjen,  ‘lamb,  young cow’,  OSlav.  sterica,  ‘a  barren  cow’,  Goth. stairo  (fem.),  ‘barren’,  MLG.  sterke  (whence  G. Sterke ),  ‘heifer’,  ON.  stirtla,  ‘a  barren  cow' ;  fr. I.-E.  base  *ster-,  ‘barren,  sterile’,  orig.  identical with  base  *ster-,  ‘stiff,  rigid’.  See  stare  and  cp. words  there  referred  to.  For  the  ending  see  suff. -ile.
sterility,  n.  —  ME.  sterylite,  fr.  MF.  (=  F.)  steri- lite,  fr.  L.  sterilitdtem,  acc.  of  sterilitds ,  fr.  steri¬ lis.  See  prec.  word  and  -ity. sterilize,  tr.  v.  —  Formed  with  suff.  -ize  fr.  L. sterilis.  See  sterile.
Derivatives:  steriliz-ation,  n.,  steriliz-er,  n. sterlet,  n.,  a  kind  of  small  sturgeon.  — •  F.,  fr. Russ,  sterlyad',  which  is  of  Teut.  origin.  Cp. Russ,  osetr,  ‘sturgeon’,  and  see  sturgeon, sterling,  n.  —  ME.,  ‘a  silver  penny’,  prob.  fr.  OF. esterlin,  estrelin,  fr.  WFrankish  *ester(e)ling,  a hybrid  coined  fr.  OF.  estedre,  ester ,  ‘stater’,  and the  Teut.  suff.  -ling.  OF.  estedre  derives  fr.  VL. istater,  fr.  L.  stater ,  fr.  Gk.  axxxrjp;  see  stater. See  Kluge-Mitzka,  EWDS.,  p.  747  s.v.  Sterling. Sterling  is  not  related  to  ME.  sterre,  ‘star’  (as suggested  by  most  lexicographers).
```


## [2026-09-14T03:16:46.423Z] AGENT

Now I'll write the verification file.


## [2026-09-14T03:22:30.179Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_STR = \"https://en.wiktionary.org/wiki/سترون\"\nW_STU = \"https://en.wiktionary.org/wiki/ستودن\"\nETY   = \"https://www.etymonline.com/word/sterile\"\nAB_EST= \"https://abadis.ir/fatofa/استریلیزه/\"\nAB_XAS= \"https://abadis.ir/fatofa/خستو/\"\n\ndata = {\n \"pdf_page\": 481,\n \"book_page\": 451,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Ster 4\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ster- 'barren, sterile' (Pokorny 6. ster-, p. 1031; an old specialisation of *ster- 'stiff, rigid')\",\n   \"note\": \"Root, language label and gloss are all correct. Pokorny's entry '6. ster-' is glossed 'sterile/unfruchtbar' and sits exactly on p. 1031, the page Nourai cites; Walde-Pokorny II 640 f. has the same entry ('6. ster- „unfruchtbar“, alte Sonderanwendung von ster- „steif“'), and Watkins/AHD numbers it ster-5 'Barren'. Nourai's '4' is his own serial number for the homonymous roots, not Pokorny's. Klein (s.v. sterile) states the same: 'fr. I.-E. base *ster-, ‘barren, sterile’, orig. identical with base *ster-, ‘stiff, rigid’'. The one caveat worth recording is that the Greek and Indo-Aryan derivatives (Gk. steîra < *ster-ih₂-, Skt. starī-) make a laryngeal-final shape *sterh₁- likely in current reconstructions; this does not affect any arrow on the chart.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ster- «نازا، سترون» که پوکورنی آن را زیر «۶. ster-» در صفحهٔ ۱۰۳۱ آورده و همان‌جا آن را کاربرد ویژه‌ای از ریشهٔ *ster- «سخت، خشک» دانسته است؛ والده–پوکورنی (جلد دوم، ص ۶۴۰–۶۴۱) و واتکینز (AHD) نیز همین را می‌گویند. بنابراین نام ریشه، برچسب زبانی (هندواروپایی) و معنای «نازا» در نمودار نورایی درست است و شمارهٔ «۴» شمارهٔ خودِ نورایی است نه پوکورنی. تنها نکتهٔ تکمیلی آن است که بر پایهٔ یونانی steîra و سنسکریت starī- امروزه صورت *sterh₁- (با حنجری پایانی) را محتمل‌تر می‌دانند که در هیچ‌یک از پیکان‌های این نمودار اثری ندارد.\",\n   \"sources\": [ETY],\n   \"ref_check\": [\n    {\"ref\": \"POK:1031\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt: 'Root / lemma: ster-6 / Meaning: sterile / Note: old Sonderanwendung from ster- ‘stiff’ / Material: Old Indic starī- ‘infertile cow’ ... Latin sterilis ‘infertile’ ... References: WP. II 640 f., WH. II 589 f. / Page(s):1031' (grep -n 'lemma: ster' POK_full.txt, line 82687). The printed text is on POK_03.txt leaf ~273 f.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 640 f. (incoming/WLD/WLD_Bd2_pages.txt leaf 644-645)\", \"stance\": \"supports\",\n     \"note\": \"'6. ster- „unfruchtbar“, alte Sonderanwendung von ster- „steif“. Ai. starī-ḥ f. „unfruchtbare Kuh, Starke“; arm. sterj ...; gr. στεῖρα ...; lat. sterilis „unfruchtbar“ ... got. stairo ... isl. stirtla „unfruchtbare Kuh“'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ster-5 (AHD_watkins1985.txt line 1022)\", \"stance\": \"supports\",\n     \"note\": \"'ster-5. Barren. Latin sterilis, unfruitful: STERILE. [Pok. 6. ster- 1031.]' — same root, same gloss, same Pokorny page.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. sterið / sterios (IEC.txt line 17210)\", \"stance\": \"supports\",\n     \"note\": \"'sterið ‘run dry, become barren’; sterios ‘run dry, sterile, barren’. WP II, 640. Skt. starih ... f. ‘barren cow, heifer’; ... Gk. steiros, adj. ‘barren’; ... Lat. cf. sterilis, adj. ‘barren’; Go. staíro ...'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. sterile (KLN_1966.txt line 36755)\", \"stance\": \"supports\",\n     \"note\": \"'sterile, adj. ... L. sterilis, ‘barren, unfruitful’, cogn. with OI. starīḥ, ‘a barren cow’ ... fr. I.-E. base *ster-, ‘barren, sterile’, orig. identical with base *ster-, ‘stiff, rigid’.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"stari\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Vedic starī́- (nom. starī́ḥ), f., 'a cow that does not calve, barren cow, heifer' (RV+), i.e. the e-grade/zero-grade *str̥-ih₂- formation of PIE *ster- 'barren'. Pokorny p. 1031 opens the entry with exactly this word ('Old Indic starī- ‘infertile cow’'), as do Walde-Pokorny II 640, Mann and Klein; it is the cognate of Gk. steîra, Lat. sterilis, Goth. stairo. Nourai's spelling 'stari' is the usual simplified transliteration of starī́-; gloss 'infertile, barren' is right, though in the Veda the word is specifically used of a barren cow.\",\n     \"derivation_fa\": \"سنسکریت (ودایی) starī́- «ماده‌گاوِ نازا»، صورت مؤنث *str̥-ih₂- از ریشهٔ هندواروپایی *ster- «نازا». پوکورنی در همان صفحهٔ ۱۰۳۱ نخستین شاهد ریشه را همین واژه آورده و آن را هم‌ریشهٔ یونانی steîra، لاتینی sterilis و گوتی stairō دانسته است. آوانگاشتِ «stari» در کتاب همان starī́- است و معنای «نازا» درست است؛ تنها باید افزود که در ودا این واژه بیشتر دربارهٔ گاو به کار می‌رود. ادعای نورایی در این گره درست است.\",\n     \"sources\": [ETY],\n     \"ref_check\": [\n      {\"ref\": \"POK:1031\", \"status\": \"supports\",\n       \"note\": \"Pokorny ster-6, p. 1031: 'Material: Old Indic starī- ‘infertile cow’' — the first form listed under the root, exactly as drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II 640 (WLD_Bd2_pages.txt leaf 644)\", \"stance\": \"supports\",\n       \"note\": \"'Ai. starī-ḥ f. „unfruchtbare Kuh, Starke“' heads the material of WP's 6. ster-.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, s.v. sterið (IEC.txt line 17210)\", \"stance\": \"supports\",\n       \"note\": \"'Skt. starih, acc. sg. staryám, npl. staryás, f. ‘barren cow, heifer’' — with the full paradigm, confirming the stem starī-.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. sterile\", \"stance\": \"supports\",\n       \"note\": \"'cogn. with OI. starīḥ, ‘a barren cow’'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"satarvan\", \"verdict\": \"plausible\",\n     \"derivation\": \"NP سَتَروَن satarvan / setarvan (also استَروَن astarvan, and Horn's variants setervan, suturven, esterven) 'barren, sterile (of a woman)' is a genuine Persian word of exactly this root — but it does NOT come from Sanskrit. It continues Middle Persian starwan [stlwn'] 'barren, childless' (MacKenzie, CPD 82), i.e. Old Iranian *str̥-wan-/*str̥-want- ('possessing barrenness'), the Iranian sister-formation of Skt. starī-, with the regular NP prothetic/anaptyctic vowel breaking the initial st- cluster (st- > sit-/sat-, and with prothesis ist-/ast-, whence the doublet استرون). Wiktionary reconstructs *str̥-wénts and derives NP سترون from MP starwan; Mo'in's own footnote in Borhan-e Qate' lines the word up with Skt. starī-, Arm. sterj, Gk. steîra, Lat. sterilis, Goth. stairo and Judaeo-Persian 'strwn (after Hübschmann). So the root box is right and the word is right; only the drawn parent (Sanskrit) is wrong — Persian and Sanskrit are cognates here, not ancestor and descendant, and the Iranian intermediate MP starwan is missing from the chart. The old native folk etymology 'like a mule' (ستر/استر astar 'mule' + -van) is rejected by Horn ('unwahrscheinlich, zumal es ein Suffix -ven ‘ähnlich’ sonst gar nicht giebt') and by Mo'in, who calls it عامیانه.\",\n     \"derivation_fa\": \"«سَتَروَن / اِستَروَن» به معنی «نازا، عقیم» واژه‌ای اصیل فارسی است و از فارسی میانهٔ starwan (نوشتهٔ پهلوی stlwn')، از ایرانی باستان *str̥-wan- می‌آید؛ همان ساختی که سنسکریت starī- نیز از آن است. خوشهٔ آغازین st- در فارسی نو با واکهٔ میانجی شکسته شده (st- > سَتـ/سِتـ) و گونهٔ دارای الفِ آغازین «استرون» از همان قاعدهٔ واکهٔ پیشین (پروتز) پدید آمده است. معین در حاشیهٔ برهان قاطع همین واژه را کنار «هندی باستان starī-، ارمنی sterj، یونانی steîra، لاتینی sterilis، گوتی stairō و یهودی–فارسی ʾSTRWN (هوبشمان)» نشانده و ریشه‌شناسی عامیانهٔ «شبیه استر (قاطر)» را رد کرده است؛ هرن نیز همین نظر را دارد. پس ریشهٔ هندواروپایی درست است، اما پیکان نمودار نادرست رسم شده: فارسی از سنسکریت نیامده بلکه هم‌ریشهٔ آن است و حلقهٔ میانی، یعنی فارسی میانهٔ starwan، در نمودار افتاده است. ادعای نورایی با این اصلاح پذیرفتنی است.\",\n     \"sources\": [W_STR],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1100\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate', vol. 2, entry سترون (BQT_v2_pages.txt leaf 562; printed page in the 1100s — the running-head numerals are unreadable in the OCR, so the exact figure could not be confirmed): 'سترون ... زن لازاینده و عقیمه را گویند و معنی ترکیبی این لغت استرمانند است', with Mo'in's footnote 'هندی باستان starī- (بی‌حاصل)، ارمنی sterj، یونانی steira، لاتینی sterilis، گوتی stairo ... یهودی–فارسی ʾSTRWN «هوبشمان»، رک: استرون' and the remark that the 'mule' etymology is عامیانه — i.e. exactly Nourai's set of cognates.\"},\n      {\"ref\": \"MON:1833\", \"status\": \"partial\",\n       \"note\": \"Mo'in, Farhang-e Farsi: the entry exists ('استرون: [= سترون] (ص.) زنی که بچه نیاورد، نازا، عقیم', MON_part1.txt line 11855) and gives the meaning Nourai gives, but Mo'in's lexicon entry carries no etymology, so it supports the word and gloss only, not the derivation; the OCR of the volumes carries no page numbers, so p. 1833 itself could not be confirmed.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 82 (PHD.txt leaf 103)\", \"stance\": \"supports\",\n       \"note\": \"'starwan [stlwn' | N sit~] barren, childless' — and in the English index (PHD.txt line 930) 'barren starwan'. This is the Middle Persian link the chart omits, and it disproves the claim that Iranian has no cognate.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 716, p. 158/159 (HRN.txt leaf 179)\", \"stance\": \"partial\",\n       \"note\": \"'716. seterven, suturven, esterven ‘unfruchtbar’ ... Gehört wohl zu ai. starī- ‘unfruchtbar’; arm. sterj; gr. στεῖρα; lat. sterilis; got. stairō ... Die neupersische Volksetymologie ‘Maulesel ähnlich’ ist unwahrscheinlich'. Horn gives the same cognate set but as a comparison ('gehört wohl zu'), not as descent from Sanskrit.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, s.v. سترون، استرون, printed p. 347-348 (incoming/ARY/ARY_pages.txt, pdf page 346-347)\", \"stance\": \"partial\",\n       \"note\": \"Lists Skt. STARIS, Arm., Gk. STEIRA/STERIPHOS, Lat. STERILIS, Fr. STÉRILE, Goth. STAIRO, citing Borhan-e Qate', Dehkhoda and Mo'in; but his note says 'فقدان واژه‌های هم‌ریشه در زبان‌های اوستایی و پهلوی ... وابستگی سترون را ... نامسجّل می‌کند' and he even entertains a link to استر 'mule'. MacKenzie's MP starwan shows this reservation to be unfounded.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt, grep 'sterwan/unfruchtbar')\", \"stance\": \"silent\",\n       \"note\": \"No entry for the word in Persische Studien; Hübschmann's relevant note (Judaeo-Persian ʾSTRWN) is the one Mo'in quotes from his Armenische Grammatik, which is not in the local library.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Latin\", \"words\": \"sterilis\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Lat. sterilis, -e 'barren, unfruitful' (Plautus onward, used of women, animals and of soil) < PIE *ster- 'barren' with the adjectival suffix -ilis (cf. OLat. sterilus, Lucretius). It is the exact Italic counterpart of Skt. starī-, Gk. steîra, Goth. stairo. Ernout-Meillet (s.v. sterilis, -e, with the archaic sterilus) and Walde-Hofmann II 589 f. carry it; Klein derives it straight from the I.-E. base *ster-.\",\n     \"derivation_fa\": \"لاتینی sterilis «نازا، بی‌بار» (از پلاوتوس به بعد، هم دربارهٔ زن و جانور و هم دربارهٔ زمین) از ریشهٔ *ster- با پسوند صفت‌ساز -ilis ساخته شده (گونهٔ کهن sterilus در لوکرتیوس). این واژه برابرِ ایتالیکِ سنسکریت starī-، یونانی steîra و گوتی stairō است. ارنو–مه‌یه و والده–هوفمان (جلد دوم، ص ۵۸۹) و کلاین همگی همین را می‌گویند؛ پس این گره نمودار درست است.\",\n     \"sources\": [ETY],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 1022): 'ster-5. Barren. Latin sterilis, unfruitful: STERILE. [Pok. 6. ster- 1031.]' — the reference Nourai cites says precisely this.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. sterilis (LAT.txt line 60325)\", \"stance\": \"supports\",\n       \"note\": \"'sterilis, -e (et arch. sterilus, cf. P. F. 419,4; et v. Lucrece...)' with classical uses ('uulua sterilis', Petron. 35,3) — the word, form and meaning as drawn.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. sterile\", \"stance\": \"supports\",\n       \"note\": \"'L. sterilis, ‘barren, unfruitful’ ... fr. I.-E. base *ster-, ‘barren, sterile’.'\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny p. 1031, ster-6\", \"stance\": \"supports\",\n       \"note\": \"'Latin sterilis “infertile”' listed among the root's continuants.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Pass-through box with no word printed: it stands for French stérile 'barren' (Old/Middle French sterile, 14th-15th c., a learned borrowing of Lat. sterilis, not a popular inheritance — hence the intact -il-) and its derived verb stériliser / stérilisation. French is the correct hinge for the two children drawn from it: Persian استریلیزه is unquestionably from French stérilisé, and English sterile is standardly traced through Old French (Etymonline: 'mid-15c., from Old French sterile ... and directly from Latin sterilis'), although Klein prefers a direct Latin source for the English adjective.\",\n     \"derivation_fa\": \"این جعبهٔ خالی در کتاب نمایندهٔ فرانسهٔ stérile «نازا» است؛ واژه‌ای عالمانه که در سدهٔ چهاردهم–پانزدهم میلادی مستقیم از لاتینی sterilis وام گرفته شده (نه میراثِ گفتاری، و به همین سبب -il- دست‌نخورده مانده است) و فعلِ برساختهٔ stériliser از آن آمده. همین حلقهٔ فرانسوی درست است، زیرا «استریلیزه»ی فارسی بی‌گمان از stériliséی فرانسوی است و انگلیسی sterile نیز بنا بر اتیمونلاین از راه فرانسهٔ کهن به انگلیسی رسیده است (هرچند کلاین آن را یکسره از لاتینی می‌گیرد).\",\n     \"sources\": [ETY],\n     \"ref_check\": [\n      {\"ref\": \"(none)\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference in the book (refs=None); nothing to verify. The claim itself is covered by Etymonline and by Mo'in's [فر.] tag on استریلیزه.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. sterility / sterilize\", \"stance\": \"partial\",\n       \"note\": \"'sterility, n. — ME. sterylite, fr. MF. (= F.) sterilite, fr. L. sterilitatem' — Klein routes the noun through French but derives the adjective sterile and the verb sterilize straight from Latin.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Sterile (SKT.txt line 18488)\", \"stance\": \"supports\",\n       \"note\": \"'Sterile. (F. – L.) O.F. sterile. – L. sterilem, acc. of sterilis, barren.' — Skeat has exactly the Latin > French > English route the chart draws.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\", \"words\": \"esterîlîzeh\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP استریلیزه esterilīze 'sterilized, disinfected' is a 20th-century loan of French stérilisé (past participle of stériliser), taken in with the rest of the French medical vocabulary that entered Persian through the Dar al-Fonun and the medical schools; the initial cluster st- again receives a prothetic e- (استریلیزه, exactly as استکان، استادیوم), and the French final -é is rendered -ه /-e/. Mo'in tags the entry '[فر.]' (French) and glosses it 'ضدعفونی شده، سترون', so the chart's French > Persian arrow is exactly right — and note that this word and node #2 سترون are doublets, the one inherited through Iranian, the other borrowed back through Latin and French.\",\n     \"derivation_fa\": \"«استریلیزه» وام‌واژه‌ای است از فرانسهٔ stérilisé (اسم مفعولِ stériliser) که در سدهٔ چهاردهم خورشیدی همراه با دیگر اصطلاحات پزشکی فرانسوی وارد فارسی شد. خوشهٔ آغازین st- مانند «استکان» و «استادیوم» با الف (واکهٔ پیشین) شکسته شده و -éی پایانی فرانسوی به «ـه» بدل گشته است. معین این مدخل را با نشانهٔ «[فر.]» یعنی فرانسوی آورده و «ضدعفونی شده، سترون» معنی کرده است؛ پس پیکان فرانسه ← فارسی در نمودار درست است. جالب آنکه این واژه با «سترون» (گرهٔ ۲) دوگانه (doublet) است: یکی از راه ایرانی به ارث رسیده و دیگری از راه لاتینی–فرانسوی وام گرفته شده است.\",\n     \"sources\": [AB_EST],\n     \"ref_check\": [\n      {\"ref\": \"MON:249\", \"status\": \"supports\",\n       \"note\": \"Mo'in, Farhang-e Farsi s.v. استریلیزه: '(اِ تِ زِ) [فر.] (ص.) ضدعفونی شده، سترون ساز' (abadis.ir, فرهنگ معین section); the local OCR has the same entry ('استریلیزه: (ص.) آنچه که به وسایل علمی میکرب‌های وی کشته شده باشد، ضد عفونی شده', MON_part1.txt line 11869), immediately after استری, which fits p. 249 of the continuous pagination. The [فر.] tag is Mo'in's own statement that it is French.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vajehyab/abadis, فرهنگ معین s.v. استریلیزه\", \"stance\": \"supports\",\n       \"note\": \"'[فر.] (ص.) ضدعفونی شده، سترون ساز' — explicit French origin tag.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, s.v. سترون، استرون (printed p. 347)\", \"stance\": \"partial\",\n       \"note\": \"Lists 'انگلیسی (از فرانسه) STERILIZE' and French STÉRILE among the reflexes of the root, i.e. the same Latin>French modern chain, though he does not treat استریلیزه itself.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"sterile, sterilize\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Eng. sterile is first attested mid-15c. 'barren', from Old French sterile and/or directly from Lat. sterilis; applied to persons from the 1530s, to soil from the 1570s, figuratively of writing from the 1640s, and in the bacteriological sense 'free from living germs' from 1877. sterilize is a 17th-century formation (1690s 'to make barren'), Lat. sterilis + -ize (Klein: 'Formed with suff. -ize fr. L. sterilis'), whose medical sense 'to free from micro-organisms' is documented from 1878, i.e. it followed the same Pasteur-era shift as French stériliser and is the immediate model of Persian استریلیزه's French source.\",\n     \"derivation_fa\": \"انگلیسی sterile نخستین بار در میانهٔ سدهٔ پانزدهم میلادی به معنی «نازا» دیده می‌شود، از فرانسهٔ کهن sterile و/یا یکسره از لاتینی sterilis؛ از ۱۵۳۰ دربارهٔ آدمیان، از ۱۵۷۰ دربارهٔ خاک، و از ۱۸۷۷ در معنای زیست‌شناختیِ «عاری از میکروب» به کار رفته است. sterilize ساختی است از لاتینی sterilis با پسوند -ize (کلاین) که از دههٔ ۱۶۹۰ به معنی «نازا کردن» و از ۱۸۷۸ به معنی «ضدعفونی کردن» آمده است. بنابراین این گره نمودار درست است؛ تنها اختلاف جزئی میان منابع آن است که کلاین صفتِ sterile را مستقیم از لاتینی می‌گیرد و اتیمونلاین و اسکیت آن را از راه فرانسه.\",\n     \"sources\": [ETY],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. ster-5: 'Barren. Latin sterilis, unfruitful: STERILE.' — the English word is derived from Lat. sterilis under this root, as drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966, s.v. sterile, sterilize (KLN_1966.txt line 36755)\", \"stance\": \"partial\",\n       \"note\": \"'sterile, adj., 1) barren; 2) free from living germs. — L. sterilis' and 'sterilize, tr. v. — Formed with suff. -ize fr. L. sterilis' — Klein has no French step for these two, only for sterility.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, s.v. Sterile\", \"stance\": \"supports\",\n       \"note\": \"'Sterile. (F. – L.) O.F. sterile. – L. sterilem ... barren' — French mediation, as in the chart.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Steu 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *stew- 'to praise, proclaim solemnly' (Pokorny 'steu-2', p. 1035; LIV 600 f.)\",\n   \"note\": \"Exactly right, down to the page. Pokorny's 'steu-2, Meaning: to praise' occupies p. 1035 — the page Nourai cites — with the note 'only indo-iran. and gr.' and the material 'Old Indic stauti, stavate ‘lobt, preist’ ... Avestan staoiti ... gr. στεῦται'; Walde-Pokorny II 620 is the same entry. Modern work (LIV *stew-, Cheung EDIV 366 *stau, with Hittite istuwa- 'to become public' added) keeps the root and the gloss unchanged. Nourai's serial '1' is again his own numbering.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *stew- «ستودن، آشکارا اعلام کردن»؛ پوکورنی آن را زیر «steu-2 ‘to praise’» درست در همان صفحهٔ ۱۰۳۵ که نورایی یاد کرده آورده و گفته است شواهدش تنها هندوایرانی و یونانی است: سنسکریت stauti/stavate، اوستایی staoiti، یونانی steûtai. والده–پوکورنی (جلد دوم، ص ۶۲۰) همین را دارد و پژوهش امروزی (LIV و فرهنگ فعل ایرانیِ چونگ، ص ۳۶۶، با افزودن هیتیِ istuwa-) نیز ریشه و معنا را دست‌نخورده نگه داشته است. پس ادعای نورایی در جعبهٔ ریشه درست است.\",\n   \"sources\": [W_STU],\n   \"ref_check\": [\n    {\"ref\": \"POK:1035\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt line 82919: 'Root / lemma: steu-2 / Meaning: to praise / Note: only indo-iran. [and] gr. / Material: Old Indic stauti, stavate ... Avestan staoiti ‘lobt, praises, besingt; prays’ ... gr. στεῦται / References: WP. II 620. / Page(s): 1035'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 620 (incoming/WLD/WLD_Bd2_pages.txt leaf 624)\", \"stance\": \"supports\",\n     \"note\": \"'2. steu- „laut preisen“. Ai. stauti, stavate usw. „lobt, preist“, Ptc. stutá-ḥ ... av. staoiti „lobt, preist, besingt; betet“, Ptc. stūta-, stuiti-, staotar-'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 366, *stau\", \"stance\": \"supports\",\n     \"note\": \"'*stau ‘to praise’ ... «PIE *steu- ‘to praise, to announce solemnly’ = LIV: 600 f. | Pok.: 1035' — same root and same Pokorny page.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt, grep '^steu')\", \"stance\": \"silent\",\n     \"note\": \"The 1985 appendix has 'steu(ə)-' ‘to push, stick, knock, beat’ but no separate 'praise' root — Watkins omits it because it has no English reflex; that is an absence of coverage, not a contradiction.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"stav; staoiti\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Av. stav- / stū- 'to praise, laud, celebrate in song; pray' is the Iranian continuant of PIE *stew-; staoiti is the athematic 3sg. present (Hom Yt, Y 10.6 'yō dim staoiti'), 1sg. staomi (Y 10.3 'staomi maiiʔə́mca vāiriʔāca ... staomi zām'), ppp. stūta-, agent noun staotar- 'praiser'. Bartholomae sets it out at col. 1593-1596: 'stav- V. ‘preisen’. Praes. 1 stav-/stv-. PPfP. *stūta-; PFP. *staota-, Inf. staomaine. 1) ‘preisen, loben, besingen’'. Both forms Nourai prints are thus correct, and his gloss 'to praise / praised' matches (staoiti is strictly 'he praises', not 'praised'; the ppp. is stūta-). Crucially for the next node, Bartholomae's same entry lists the prefixed ā-stav- 'sich angeloben an, sich einschwören auf' with the participle ā-stavana- (V 3.41 narəš āstavanahe) — the direct ancestor of Pahlavi āstawan.\",\n     \"derivation_fa\": \"اوستایی stav-/stū- «ستودن، ستایش کردن، سرود خواندن، نیایش کردن» دنبالهٔ ایرانیِ ریشهٔ *stew- است: staoiti سوم‌شخص مفرد حال بی‌میانوند (یسنا ۱۰٬۶)، staomi اول‌شخص (یسنا ۱۰٬۳)، اسم مفعول stūta- و فاعلی staotar- «ستاینده». بارتولومه در ستون‌های ۱۵۹۳–۱۵۹۶ فرهنگ ایرانی باستان همین را آورده است. هر دو صورتی که نورایی نوشته درست‌اند؛ تنها باید توجه داشت staoiti «می‌ستاید» است نه «ستوده‌شده» (که stūta- است). نکتهٔ مهم آنکه در همان مدخل، صورت پیشوندیِ ā-stav- «خود را به چیزی متعهد و معترف کردن» با اسم فاعل ā-stavana- آمده که نیای مستقیمِ «آستوان» پهلوی است.\",\n     \"sources\": [W_STU],\n     \"ref_check\": [\n      {\"ref\": \"POK:1035\", \"status\": \"supports\",\n       \"note\": \"Pokorny steu-2, p. 1035: 'Avestan staoiti “lobt, praises, besingt; prays”, participle stūta-, stuiti-, staotar-' — the very form Nourai prints.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiWb. col. 1593-1596 s.v. stav- (BRT.txt leaf 869-870)\", \"stance\": \"supports\",\n       \"note\": \"'stav- V. ‘preisen’ ... 1) ‘preisen, loben, besingen’: staomi maiθímca ... haōmō uxsyeiti stavanō ... yō dim staoiti Y. 10.6'; further down 'mit ā ... āstaoiti', 'narəš āstavanahe V. 3.41'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 366, *stau\", \"stance\": \"supports\",\n       \"note\": \"'*AVESTAN: stau-, stū- ‘to praise’ || (+ *ā-) ‘to profess/pledge oneself to’ ... 3sg. YAv. staoiti (H, Y 10.6)'.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, s.v. ستایش (printed p. 345)\", \"stance\": \"supports\",\n       \"note\": \"Lists 'اوستایی: STAV, STAOITI' and 'پهلوی: STĀV, STĀYĪTAN' and 'سانسکریت: STAUTI/STAV-' under the same headword — the same chain as the chart.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"stâyîtan; âstvân; âstôbân\", \"verdict\": \"confirmed\",\n     \"derivation\": \"MP stāyīdan/stūdan, pres. stāy- [stʾytn', stwtn'] 'to praise' continues Av. stav-/stū- directly: the Avestan present stem stav- gives MP stāy- (with the regular Middle Iranian outcome of *-āw- before a vowel), the old ppp. *stūta- gives the past stem stūd, whence the two competing infinitives stūdan and the analogical stāyīdan; MacKenzie, CPD 82: 'stāyīdan [stʾydytn' | M ʾytʾy, N sit~] = stūdan', 'stūdan, stāy- [stwtn', stʾyd- | M ʾystwd, ʾystʾy-, N sit—] praise'. Āstawan [ʾystwbʾyn', ʾystwpʾyn'] 'confessing, professing; believing' (abstract āstawanīh 'confession, belief', negative an-āstawan 'disbelieving') is the same root with the preverb ā-, i.e. Av. ā-stavana- 'professing oneself to'. Nourai's third form 'āstōbān' is not a separate word: Book Pahlavi <p> and <b> are the same letter, so ʾystwpʾyn'/ʾystwbʾyn' can be read āstobān or āstawan — MacKenzie and the Manichaean spelling ʾystwʾyn settle it as āstawan. The Shayast ne Shayast glossary analyses it exactly as the chart does: 'āstvān ← ā + stav-'.\",\n     \"derivation_fa\": \"فارسی میانه (پهلوی) stāyīdan/stūdan با ستاکِ حالِ stāy- دنبالهٔ مستقیم اوستایی stav-/stū- است: ستاک حالِ اوستایی stav- در ایرانی میانه به stāy- بدل شده و اسم مفعول کهن *stūta- ستاک گذشتهٔ stūd را داده است؛ از این‌رو دو مصدر stūdan و stāyīdan (قیاسی) در کنار هم به کار رفته‌اند (مکنزی، فرهنگ کوچک پهلوی، ص ۸۲). «آستوان» āstawan «معترف، مؤمن» (و مصدرِ اسمیِ āstawanīh «اعتراف، ایمان» و منفیِ an-āstawan) همان ریشه با پیشوند ā- است، یعنی اوستایی ā-stavana-. صورت سومِ نورایی «آستوبان» واژه‌ای جداگانه نیست: در خط پهلوی کتابی حرف <p> و <b> یکی است و از این‌رو ʾystwpʾyn' را می‌توان āstobān یا āstawan خواند؛ املای مانوی ʾystwʾyn نشان می‌دهد خوانش درست āstawan است. واژه‌نامهٔ شایست ناشایست نیز آن را درست همان‌گونه که نمودار می‌گوید تجزیه کرده است: «āstvān از ā + stav-».\",\n     \"sources\": [W_STU],\n     \"ref_check\": [\n      {\"ref\": \"SNS:31\", \"status\": \"supports\",\n       \"note\": \"Tavoosi, Vazhe-name-ye Shayast ne Shayast: the index gives 'astvan 31/10', 'astvan bUdan 31/14', 'astvat-/astvant 31/1' (SNS.txt lines 29861, 34031, 34033), and the entry itself (SNS.txt line 3337) reads 'āstvān ... ← *stav + ā- ... (Mir. Man. ʾystwʾyn) ... xustuwan' — i.e. page 31 carries āstvān, derived from the root stav- with ā-, and even cross-refers to xustuwan (the ancestor of خستو in node #3). Exactly Nourai's claim.\"},\n      {\"ref\": \"BQT:747\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' vol. 2 leaf 205 (= printed p. 747-748) is the خستو/خستوان page: 'خستو ... اقرار و اعتراف کننده را گویند'; 'خستوان ... اقرار و اعتراف کنندگان و معترف شدگان را گویند', with Mo'in's etymological footnote giving the Pahlavi form '(مقر، معترف)' and an Armenian comparison. It supports the 'confessor' member of this Pahlavi node.\"},\n      {\"ref\": \"BQT:1098\", \"status\": \"supports\",\n       \"note\": \"The ستـ stretch of vol. 2 (BQT_v2_pages.txt leaves 558-563, printed pages in the 1100s; the OCR running heads are unreadable, so the exact numeral could not be confirmed) carries ستا 'بمعنی ستایش و ستودن', ستوان ('مخفف استوان ... رک: استوان') and ستودن with Mo'in's footnote 'اوستا ریشه ... (مدح کردن، تمجید کردن)؛ پهلوی ...' — the Avestan root plus the Pahlavi form, as the arrow requires.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 82 and p. 13 (PHD.txt leaves 103, 219; English index lines 1333-1334, 3234)\", \"stance\": \"supports\",\n       \"note\": \"'stāyīdan [stʾydytn' | M ʾytʾy, N sit~] = stūdan'; 'stūdan, stāy- ... praise'; 'āstawan [ʾystwbʾyn', ʾystwpʾyn' | M ʾystwʾyn] confessing, professing. ~ih: confession, belief'; index: 'confessing āstawan, xwastūg', 'professing astawan'. This both confirms the node and shows that āstōbān is only the alternative reading of the same spelling.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, p. 180 (NYB_vol2_glossary.txt leaves 197-198)\", \"stance\": \"supports\",\n       \"note\": \"'stāyišn [stʾydān'] praise, worship, from stāyītan [stʾydytn'] stāy- ... to praise, to profess (the religion) — Av. (1593 sqq.) stav-; MPrth ʾystʾwʾydn; MPrs ʾystwdn; NP sutūdan or sitāyī-' and 'stāyītār confessor of the true religion, believer'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 366, *stau\", \"stance\": \"supports\",\n       \"note\": \"'*MIDDLE PERSIAN: MMP ʾystʾy-, BMP stʾyd-, stʾy- /stay-/ ‘to praise’ || (+ *ā-) MMP ʾystwʾyn, ʾystwʾyn ‘professing’' — the two Pahlavi items of the node, and the ā- prefix explicitly.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"setâyîdan; ostovân; xastŭ\", \"verdict\": \"plausible\",\n     \"derivation\": \"Two of the three words are straightforward; the third needs a correction. (1) ستاییدن/ستودن setāyīdan/sotūdan 'to praise', with ستایش setāyeš and pres. stem ستای- setāy-, is MP stāyīdan/stūdan with the usual New Persian prothetic vowel breaking st- (st- > sit-/set-); Horn no. 719 gives 'sitūden, sutūden ‘loben, preisen’, Praes. sitāy-ed ... aw. √stav-, staomi; phlv. stātan, stāyītan, stāy(i)šn; ai. √stav-, stautī'. Confirmed. (2) استوان/ستوان ostovān 'believing, professing, trustworthy' is MP āstawan (ā- + stav-), with the same prothesis; Borhan glosses it 'استوار ... امین و معتمد ... باور داشتن' and Mo'in's footnote there gives the Pahlavi form glossed 'معتقد و ثابت‌قدم'. Confirmed (the modern military rank ستوان 'lieutenant' is a 20th-c. revival of this same word). (3) خَستو xastū 'confessing, one who avows' belongs to the root too, but not to the parent drawn: it is MP xwastūg [xwstʾwk] 'confessing, professing' (MacKenzie, CPD index 'confessing āstawan, xwastūg'), i.e. Old Iranian *hu-ā-stū-ka- — the preverb string xw-/hu- + ā- prefixed to the SAME root stav-/stū-, with MP -ūg > NP -ū. Bailey (Dictionary of Khotan Saka 188) states the analysis for its Armenian loan: 'xo- as in xostovan ‘confessing’ < *hu-ā-stavāna-'. So the node's three words are all *stew- words, but xastū's immediate parent is xwastūg, not āstavān — hence 'plausible' rather than 'confirmed'. The Ferdowsi line quoted on the page ('تو خَستو شو آنرا که هست و یکیست') uses it correctly in the sense 'avow, confess'.\",\n     \"derivation_fa\": \"از سه واژهٔ این گره دو تا بی‌چون‌وچرا درست‌اند و سومی نیازمند اصلاح است. ۱) «ستاییدن/ستودن» با اسم مصدر «ستایش» و ستاک حال «ستای-» همان stāyīdan/stūdan فارسی میانه است که خوشهٔ آغازین st- آن در فارسی نو با واکهٔ میانجی شکسته شده (st- > سِتـ)؛ هرن در بند ۷۱۹ (ص ۱۵۹) همین را با صورت‌های اوستایی و پهلوی آورده است. ۲) «اُستوان/ستوان» به معنی «معتقد، معترف، امین» از پهلوی āstawan (ā- + stav-) است؛ برهان قاطع آن را «استوار، امین و معتمد، باور داشتن» معنی کرده و حاشیهٔ معین صورت پهلوی را «معتقد و ثابت‌قدم» آورده است (درجهٔ نظامی «ستوان» احیای همین واژه در سدهٔ چهاردهم خورشیدی است). ۳) «خَستو» به معنی «مقر، معترف» نیز به همین ریشه بازمی‌گردد، اما نه از راهی که نمودار نشان می‌دهد: این واژه از پهلوی xwastūg است، یعنی ایرانی باستان *hu-ā-stū-ka- با پیشوندهای xw-/hu- و ā- بر همان ریشهٔ stav-/stū-، و پسوند پهلوی -ūg در فارسی نو به -ū بدل شده است؛ بیلی در فرهنگ ختنی (ص ۱۸۸) دربارهٔ وام‌واژهٔ ارمنیِ آن می‌نویسد: «xostovan ‘معترف’ < *hu-ā-stavāna-». پس ریشه درست است ولی پدرِ بی‌واسطهٔ «خستو» صورت xwastūg است نه āstavān؛ به همین سبب داوری این گره «با احتیاط پذیرفتنی» است. بیت فردوسی که در همین صفحه نقل شده، واژه را درست در معنای «اقرار کردن» به کار برده است.\",\n     \"sources\": [W_STU, AB_XAS],\n     \"ref_check\": [\n      {\"ref\": \"HRN:159\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss no. 719 (HRN.txt leaf 179, the printed marker '— 159 —' stands immediately before nos. 717-720): 'sitūden, sutūden ‘loben, preisen’, Praes. sitāy-ed, sitāyiš. aw. √stav-, staomi ‘preisen’; phlv. stātan, stāyītan, stāy(i)šn; ai. √stav-, stautī' — the whole Avestan > Pahlavi > New Persian chain of the chart, on the cited page.\"},\n      {\"ref\": \"NYB:180\", \"status\": \"supports\",\n       \"note\": \"Nyberg II p. 180 (NYB_vol2_glossary.txt leaf 197-198, the page numerals 180 and 181 are visible on the leaves): 'stāyišn ... from stāyītan ... to praise, to profess (the religion) — Av. (1593 sqq.) stav- ... NP sutūdan or sitāyī-' and 'stāyītār confessor of the true religion, believer'. Precisely Nourai's page and precisely his claim, including the 'confessor' sense.\"},\n      {\"ref\": \"SNS:31\", \"status\": \"supports\",\n       \"note\": \"Same page 31 of the Shayast ne Shayast glossary as for node #2: 'āstvān ... ← *stav + ā-', 'astvan bUdan 31/14', with the cross-reference 'xustuwan' — which is the direct source of NP خستو.\"},\n      {\"ref\": \"BQT:1101\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' vol. 2: the ستـ chapter opens with 'ستا ... بمعنی ستایش و ستودن است که از دعا و ثنا و شکر ... باشد' (leaf 558) and two leaves later has ستوان ('مخفف استوار ... امین و معتمد ... باور داشتن', with 'رک: استوان') and ستودن with Mo'in's Avestan/Pahlavi footnote — the words and senses of this node.\"},\n      {\"ref\": \"MON:261\", \"status\": \"partial\",\n       \"note\": \"Mo'in, Farhang-e Farsi s.v. استوان: 'استوان: [= ستوان] (ص مر.)' (MON_part1.txt line 12586) — the entry exists with the equation استوان = ستوان that Nourai's 'اُستوان ۱ (ستوان ۱)' reproduces, and p. 261 fits the استـ stretch of the continuous pagination (استریلیزه = p. 249); but Mo'in's lexicon gives no etymology, so it supports the form and gloss only.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD, English index p. 233 f. (PHD.txt lines 970, 972, 1333-1334)\", \"stance\": \"partial\",\n       \"note\": \"'belief āstawanīh, wābar, wurroyīšn, xwastūgih'; 'believing dēn-āstawan | xwastūg'; 'confessing āstawan, xwastūg' — confirms both Pahlavi words but shows that خستو continues xwastūg, a sister formation, not āstawan itself.\"},\n      {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka p. 188 s.v. nīhalamāna- (ISS_alt_DKS.txt leaf 222)\", \"stance\": \"supports\",\n       \"note\": \"'Armen. lw xonarh ‘low, humble’ < *hu-ānaĝra- (xo- as in xostovan ‘confessing’ < *hu-ā-stavāna-)' — the explicit analysis of the xw-/hu- + ā- + stav- compound behind MP xwastūg / NP خستو and its Armenian loan, i.e. independent confirmation that خستو does belong to this root.\"},\n      {\"src\": \"MON\", \"where\": \"abadis.ir, دهخدا and فرهنگ معین s.v. خستو\", \"stance\": \"supports\",\n       \"note\": \"Dehkhoda: 'مقر، معترف' (beside the homonym 'دانهٔ میوه‌ها'), with the note that the Pahlavi form is خوستوگ xwastūg (MP suffix -ūg) — the gloss Nourai gives and the Middle Persian antecedent.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 366, *stau\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: NP sitūdan/sitāy- ‘to praise’, sitāyīdan/sitāy- ‘to praise; call’' — both New Persian infinitives of the node under the root.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, s.v. ستایش (printed p. 345, 'بازگشت به: ستودن')\", \"stance\": \"supports\",\n       \"note\": \"Gives Avestan STAV/STAOITI, Pahlavi STĀV/STĀYĪTAN, Sanskrit STAUTI and Pashto STĀYAL for ستایش/ستودن, citing Borhan-e Qate' — an independent modern Persian source for the same chain.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open(\"data/verification/page-481.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 -m json.tool data/verification/page-481.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 481"
}
```


### [2026-09-14T03:22:31.737Z] TOOL RESULT

```
written
JSON OK
nodes verified: 9/9
node verdicts: {'confirmed': 7, 'plausible': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 13, 'partial': 2, 'not_checked': 1}
books consulted: {'supports': 20, 'partial': 6, 'silent': 1} | by book: {'KLN': 4, 'ARY': 4, 'PHD': 3, 'CHEUNG': 3, 'SKT': 2, 'MON': 2, 'WLD': 1, 'IEC': 1, 'HRN': 1, 'HUB': 1, 'LAT': 1, 'POK': 1, 'BRT': 1, 'NYB': 1, 'ISS_alt_DKS': 1}
```


## [2026-09-14T03:22:36.473Z] TOOL CALL #69: Bash

```json
{
 "command": "ls -l /home/sfmqrb/git/rishe/data/verification/page-481.json && head -c 200 /home/sfmqrb/git/rishe/data/verification/page-481.json"
}
```


### [2026-09-14T03:22:36.532Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 43248 Sep 13 23:22 /home/sfmqrb/git/rishe/data/verification/page-481.json
{
 "pdf_page": 481,
 "book_page": 451,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-13",
 "entries": [
  {
   "entry": 0,
   "root": "Ster 4",
   "verdict": "confirmed",
   "modern_form":
```


## [2026-09-14T03:22:52.074Z] AGENT

Page 481 (book p. 451) verified — `/home/sfmqrb/git/rishe/data/verification/page-481.json`; `verify_check.py 481` reports 9/9 nodes, 0 PROBLEM lines.

Counts: roots 2 confirmed; nodes 7 confirmed, 2 plausible. Ref checks: 13 supports, 2 partial, 1 not_checked (the empty French box has no refs). Entry 1 (Sterp) is a redirect, skipped.

No `disputed` or `transcription_suspect` items, and no extraction errors: the JSON matches the chart text throughout.

The two `plausible` nodes:
- **Ster 4 #2, Persian سَتَروَن satarvan** — word and root are right, but the arrow Sanskrit→Persian is a cognate relation, not descent. It continues MP `starwan` [stlwn'] 'barren, childless' (MacKenzie CPD 82), which the chart omits; Wiktionary reconstructs *str̥-wénts. Mo'in's own Borhan footnote lines it up with Skt starī-, Arm. sterj, Gk steîra, Lat. sterilis, Goth. stairō — i.e. as cognates. (Aryanpur's claim that no Avestan/Pahlavi cognate exists is refuted by MacKenzie.)
- **Steu 1 #3, Persian setāyīdan / ostovān / xastū** — the first two confirmed (Horn no. 719 p. 159; MP stāyīdan, āstawan). خستو goes back to MP `xwastūg` = *hu-ā-stū-ka-, i.e. xw-/hu- + ā- on the same root, not to āstavān as drawn; Bailey (DKS 188) gives the analysis via Armenian xostovan < *hu-ā-stavāna-. Same root, different immediate parent.

Worth noting for the owner: Nourai's third Pahlavi form "âstôbân" is not a separate word — Book Pahlavi ⟨p⟩/⟨b⟩ are one letter, so ʾstwpʾn'/ʾstwbʾn' is just another reading of āstawan (Manichaean ʾstwʾn settles it). His POK page numbers are exact (ster-6 = p. 1031, steu-2 = p. 1035), and SNS:31, NYB:180, HRN:159, BQT:747 all land on the right pages; only BQT:1100/1101 sit a few pages off the سترون/ستودن entries (vol. 2 leaves 558–563), though the OCR running heads are too poor to fix the numeral exactly.
