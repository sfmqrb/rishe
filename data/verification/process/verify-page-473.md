# Verification process log — verify-page-473


## [2026-09-14T02:28:07.279Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 473 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-473.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-473.json. Write /home/sfmqrb/git/rishe/data/verification/page-473.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 473` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:28:08.262Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-14T02:28:09.117Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:28:09.133Z] TOOL RESULT

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


## [2026-09-14T02:28:09.613Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-473.txt"
}
```


### [2026-09-14T02:28:09.637Z] TOOL RESULT

```
1	=== PDF page 473 (book page 443) ===
2	--- entry 0 ---
3	ROOT [Sanskrit] Srgâla, Črğâla : howler  (refs KLN:823; MON:2050)
4	#1 (parent #0) [Pahlavi] refs=MON:2050 | šağâl : coyote
5	  #2 (parent #1) [Persian] refs=KLN:823 | šağâl, šoğâl «شغال» : coyote | extra: شکال ، شگال
6	    #3 (parent #2) [Turkish] refs=None | 
7	      #4 (parent #3) [English] refs=KLN:823 | jackal
8	--- entry 1 ---
9	ROOT [Avestan] Srîra : satisfied  (refs BLY:78)
10	#1 (parent #0) [Pahlavi] refs=BLY:78 | sěr : satisfied, not hungry
11	  #2 (parent #1) [Persian] refs=BLY:78 | sîr «سیر» : not hungry, satisfied, full | extra: سیراب
12	--- entry 2 ---
13	ROOT [Indo-European] Srisâ, Srisnâ : file, saw  (refs IEC:1277)
14	#1 (parent #0) [Persian] refs=IEC:1277; MON:209 | arreh «ارّه» : saw
15	#2 (parent #0) [Latin] refs=IEC:1277 | serra : file
16	#3 (parent #0) [Greek] refs=IEC:1277 | rhině : file
17	  #4 (parent #2) [English] refs=AHD; KLN:1424 | serra : a saw-like organ ; serrate : notched ; serradela, serranoid, serriferous, serriform, serrulate
18	--- entry 3 ---
19	ROOT Srisnâ -> redirect to Srisâ
20	--- entry 4 ---
21	ROOT Sru -> redirect to Ser 1
22	--- entry 5 ---
23	ROOT [Avestan] Sru 3, Srva 2 : lead (metal)  (refs BQT:1116; SYN:617; BRT:1649; SNS:183)
24	#1 (parent #0) [Pahlavi] refs=HRN:161; BQT:1116; SNS:183 | srpîn, sruběn : lead, made of lead
25	  #2 (parent #1) [Persian] refs=MON:266,1854; BQT:1116; SNS:614 | sorb «سرب» : lead | extra: أُسرُب ، أُسرُف
26	--- entry 6 ---
27	ROOT Srva 2 -> redirect to Sru 3
28	
```


## [2026-09-14T02:28:12.163Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-473.json",
 "description": "Read source JSON for page 473"
}
```


### [2026-09-14T02:28:12.217Z] TOOL RESULT

```
{
  "pdf_page": 473,
  "book_page": 443,
  "entries": [
    {
      "root": {
        "name": "Srgâla, Črğâla",
        "lang": "Sanskrit",
        "refs": "KLN:823; MON:2050",
        "gloss": "howler",
        "note": "BQT:1270 indicates the root may be from Babylonia"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:2050",
          "words": [
            {
              "translit": "šağâl",
              "gloss": "coyote",
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
          "refs": "KLN:823",
          "words": [
            {
              "translit": "šağâl, šoğâl",
              "gloss": "coyote",
              "script": "شغال"
            }
          ],
          "script_extra": "شکال ، شگال",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Turkish",
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
          "refs": "KLN:823",
          "words": [
            {
              "translit": "jackal",
              "gloss": null,
              "script": null
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
        "name": "Srîra",
        "lang": "Avestan",
        "refs": "BLY:78",
        "gloss": "satisfied",
        "note": "Avestan \"srîra\" was found in POK:618 with the meaning of \"pretty\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BLY:78",
          "words": [
            {
              "translit": "sěr",
              "gloss": "satisfied, not hungry",
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
          "refs": "BLY:78",
          "words": [
            {
              "translit": "sîr",
              "gloss": "not hungry, satisfied, full",
              "script": "سیر"
            }
          ],
          "script_extra": "سیراب",
          "note": null,
          "quote": {
            "text": "گر سیر نشد دل ترا از ما - یک لحظه مباش غافل از ما",
            "poet": "Attâr"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Srisâ, Srisnâ",
        "lang": "Indo-European",
        "refs": "IEC:1277",
        "gloss": "file, saw"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:1277; MON:209",
          "words": [
            {
              "translit": "arreh",
              "gloss": "saw",
              "script": "ارّه"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "درخت اگر متحرک شدی زجای به جای - نه جور ارّه کشیدی و نه جفای تبر",
            "poet": "Anvarî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "IEC:1277",
          "words": [
            {
              "translit": "serra",
              "gloss": "file",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:1277",
          "words": [
            {
              "translit": "rhině",
              "gloss": "file",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "English",
          "refs": "AHD; KLN:1424",
          "words": [
            {
              "translit": "serra",
              "gloss": "a saw-like organ",
              "script": null
            },
            {
              "translit": "serrate",
              "gloss": "notched",
              "script": null
            },
            {
              "translit": "serradela, serranoid, serriferous, serriform, serrulate",
              "gloss": null,
              "script": null
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
        "name": "Srisnâ",
        "redirect": "Srisâ"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sru",
        "redirect": "Ser 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sru 3, Srva 2",
        "lang": "Avestan",
        "refs": "BQT:1116; SYN:617; BRT:1649; SNS:183",
        "gloss": "lead (metal)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "HRN:161; BQT:1116; SNS:183",
          "words": [
            {
              "translit": "srpîn, sruběn",
              "gloss": "lead, made of lead",
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
          "refs": "MON:266,1854; BQT:1116; SNS:614",
          "words": [
            {
              "translit": "sorb",
              "gloss": "lead",
              "script": "سرب"
            }
          ],
          "script_extra": "أُسرُب ، أُسرُف",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Srva 2",
        "redirect": "Sru 3"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T02:28:15.037Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','MON','BLY','IEC','AHD','BQT','SYN','BRT','SNS','HRN','PHD','NYB','HUB','WLD','POK','ARY','CHEUNG','LKT','TTS','SKT','FSD','WEB','AID','HJB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:500])\n\"",
 "description": "Check refs_online for relevant abbreviations"
}
```


### [2026-09-14T02:28:15.989Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French
BLY {"title": "H. W. Bailey, 'Hvatanica II' (glossary of Khotanese words), BSOAS 9.1 (1937) pp. 69-78", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/bailey-studies-1930-1993 (Robert Bedrosian's open compilation \"Selected Writings of H. W. Bailey\"; Hvatanica II = PDF pp. 313-322)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/BLY_Hvatanica_II_BSOS9_1937_pp69-78.pdf", "/home/sfmqrb/git/rishe/data/verifica
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 6
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qat
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/S
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan m
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/veri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); op
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.t
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf onli
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verific
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qa
CHEUNG null
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf 
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/gi
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/S
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, w
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-t
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offse
```


## [2026-09-14T02:28:20.051Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T02:28:20.098Z] TOOL RESULT

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
```


## [2026-09-14T02:28:23.366Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','IEC','BLY','SNS','SYN','BRT','HRN','BQT','MON','POK','PHD','NYB','ARY','LKT','TTS','SKT','HJB','AID','HUB']:\n    v=d.get(k)\n    if not v: continue\n    print('==',k)\n    for f in ['local_file','page_offset','lookup_hint','scans']:\n        if v.get(f): print('  ',f,':',json.dumps(v[f],ensure_ascii=False)[:800])\n\"",
 "description": "Print page offsets and hints"
}
```


### [2026-09-14T02:28:24.500Z] TOOL RESULT

```
== KLN
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt"
   page_offset : "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."
== IEC
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt"
   page_offset : "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."
== BLY
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/BLY_Hvatanica_II_BSOS9_1937_pp69-78.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/BLY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/Bailey_Studies_1930-1993_bedrosian.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/BLY_bailey_studies_pages.txt"]
   page_offset : "BLY_pages.txt: 11 leaves; printed = leaf(1-based) + 67 (leaf 2 = p.69 ... leaf 11 = p.78)."
   lookup_hint : "JSTOR only (BSOAS 9, 1937-39). Not on IA. Bailey's Dictionary of Khotan Saka (ISS_alt_DKS.txt, open) supersedes Hvatanica for the same words."
== SNS
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"]
   page_offset : "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image"
   lookup_hint : "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping."
== SYN
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt"
   page_offset : "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."
== BRT
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt"
   page_offset : "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."
== HRN
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt"
   page_offset : "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."
== BQT
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt", "/home/sfmqrb/git/rishe/data/v
   page_offset : "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm wit
   lookup_hint : "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. |
   scans : [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, chec
== MON
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"]
   lookup_hint : "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."
== POK
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt"
   page_offset : "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"
== PHD
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt"
   page_offset : "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."
== NYB
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt"
   page_offset : "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."
== ARY
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"]
   page_offset : "printed page = pdf page + 1"
   lookup_hint : "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"
   scans : [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf", "first_printed": 1, "last_printed": 546, "pdf_offset": -1, "lang": "fas+eng", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"}]
== LKT
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt"
   page_offset : "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."
== TTS
   local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"]
   page_offset : "TTS_pages.txt: 253 leaves; printed page N = leaf N+30."
   lookup_hint : "Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books."
== SKT
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt"
   page_offset : "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."
== HJB
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt"
   page_offset : "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers."
== AID
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt"
   page_offset : "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Headword in bold at line start; grep -n '^Word'."
== HUB
   local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt"
   page_offset : "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
   lookup_hint : "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."
```


## [2026-09-14T02:28:50.169Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN jackal ===\"; grep -n -i \"jackal\" KLN_1966.txt | head -20\necho \"=== KLN serrate ===\"; grep -n -i \"^serrate\\|^serra\\|^serried\\|^serrulate\" KLN_1966.txt | head -20",
 "description": "Grep Klein for jackal and serra"
}
```


### [2026-09-14T02:28:50.257Z] TOOL RESULT

```
=== KLN jackal ===
3024:Anubis,  n.,  a  jackal  god,  son  of  Osiris  (Egypt, mythol.)  —  L.  Anubis,  fr.  Gk.  ” Avouch?,  fr. Egypt.  Anepu ,  Anpu.
6349:Canidae,  n.  pi.,  the  family  of  dogs,  wolves,  foxes and  jackals  (zool.)  —  ModL.,  formed  with  suff. -idae,  fr.  L.  canis,  ‘dog'.  See  next  woid. canine,  adj.,  pertaining  to  the  dog.  -  L.  caninus, fr.  canis,  'dog',  which  is  cogn.  with  Gk.  xotov, gen.  xuvog,  Goth,  hunds,  OE.  hand,  'dog'.  Sec hound  and  cp.  words  there  referred  to.  For  the ending  see  suff.  -ine  (representing  L.  -in us). Derivative:  canine,  n.
6351:Canis,  n.,  the  genus  including  the  dog,  the  wolf, the  fox  and  the  jackal  (zool.)  —  L.  canis,  'dog  .
20110:jack,  n.,  1)  a  sleeveless  coat;  2)  a  vessel  for  liquor. —  OF.  jaque,  ‘sleeveless  coat’,  fr.  Jacques, ‘Jack’,  a  nickname  given  to  the  French  peasant in  the  14th  century,  for  this  kind  of  garment was  used  especially  by  the  peasants  of  that  era. See  Jack  and  cp.  Bloch-Wartburg,  DELF., p,  333  s.v.  jaquette.  Cp.  also  jacket.  For  sense development  cp.  jacquerie, jack,  n.,  an  East  Indian  tree  ( Artocarpus  inte- grifoiia).  —  Port,  jaca,  fr.  Malayalam  chakka, lit.  ‘something  round’,  fr.  OI.  cakrah,  ‘wheel, circle’,  which  is  cogn.  with  Gk.  y.bw'koq,  ‘ring, circle’.  See  cycle  and  words  there  referred  to and  cp.  esp.  chukker,  hackery, jackal,  n.  —  Turk,  chagal,  fr.  Pers.  shaghal,  fr.
39104:Thos,  n.,  a  genus  of  digitigrade  Carnivora,  the jackal  ( zool .)  —  L.  thos,  fr.  Gk.  fto'jc  (for *lkoF6<;),  ‘jackal',  which  is  of  uncertain  origin. It  possibly  stands  in  gradational  relationship  to Gk.  ffauvop,  ‘wild  beast’.  See  fauna.
=== KLN serrate ===
34714:serra,  n.,  a  sawlike  organ  (zool.)  —  L.,  ‘a  saw’,  of uncertain  origin.  Cp.  sierra.  Cp.  also  cero.
34715:serradella,  n.,  a  kind  of  clover.  —  Port,  serradela, a  dimin.  noun  formed  fr.  serrado,  ‘serrated’,  fr. L.  serrdtus.  See  serrate.
34716:Serranidae,  n.  pi.,  a  family  of  fishes  ( ichthyol .)  — ModL.,  fr.  Serranus,  name  of  the  type,  fr.  L. serra,  ‘saw’.  See  serra  and  -idae.
34717:serranoid,  adj.,  pertaining  to  the  Serranidae.  — A  hybrid  coined  fr.  ModL.  Serranus  and  Gk. -oeiSr;?,  ‘like’,  fr.  e18o?,  ‘form,  shape’.  See prec.  word  and  -oid.
34718:serrate,  adj.,  notched,  resembling  the  teeth  of  a saw.  —  L.  serrdtus,  ‘sawlike’,  fr.  serra,  See serra  and  adj.  suff.  -ate.
34724:serra  and  horn  and  cp.  corn,  ‘a  horny  indura¬ tion’.  For  the  ending  see  2nd  suff.  -ia. serriferous,  adj.,  having  serrated  edges  (hot.  and zool.)  —  Compounded  of  L.  serra,  ‘saw’,  and the  stem  of ferre,  ‘to  bear,  carry’.  See  serra  and -ferous.
34726:serrulate,  adj.,  finely  toothed.  —  Fr.  L.  serrula,  ‘a little  saw’,  dimin.  of  serra,  ‘saw’.  See  serra,  -ule and  adj.  suff.  -ate.
```


## [2026-09-14T02:28:51.653Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC srisa ===\"; grep -n \"sris\" IEC.txt | head -30\necho \"=== IEC leaf check ===\"; grep -n \"serra\" IEC.txt | head -20",
 "description": "Grep Mann IEC for srisa"
}
```


### [2026-09-14T02:28:51.763Z] TOOL RESULT

```
=== IEC srisa ===
11003:moguhilå ‘woman, maid”. Cf. moguhos. WP H, 228. See next Skt. mahilà “woman? beside mahela, id.; Lat. cf. muli-er, gs -eris, & adj. -ebris (fr. *-esris) ‘woman; womanly’; Go. mawilo, f. ‘gir’; OE meowle (*maiden, woman': E moll); ON (al- leged) meyla, id. (FH: WAN)
14254:qurisnos ‘kind of oak’. Cf. WP I, 524 Gk. prínos, mf. *holm-oak; scarlet oak’; Lat. cerrus, gs: -1, f. "oTurkey-oak'; W prin-wydden, f. (“scarlet oak’. For -wydden, see uidh-, be- low). (The phonology is that of Gk. hung: Lat. serra, see srisnà; Gk. tris: Lat. ter, see tris; Gk. kríno: Lat. cerno, see krin-)
17091:srin- (sris-) “nose; headland”; Cf. WP I, 140 Gk. hus gs: rhinós, f. ‘nose’; cf. rhíon, n. “headland”; Br. fri, pl. friu, m. ‘nose’; Cor. ryn, pl. -yow, and rün, pl. -yow, m. “head- land”; rynen and rünen, f. ‘hillock’
17092:srisà, srisnà “file, saw’. (onomat.) Per. arrah, id.; Oss. xirx, Dig. xirxá, s. ‘saw’; Kurd. ere, id.; Gk. hung f. ‘file’; Lat. serra, f. ‘saw’. (Phonol. of cerrus & Plautine terr ‘3 times', cf. terni, cerno, etc.)
=== IEC leaf check ===
7924:krind (1) ‘sift, separate’. Cf. kritós. WP II, 584 Gk. krínō, fut: krino “separate; decide; choose; judge’; Lat. cerno, inf. cernere (‘sift; judge’. Vocalism of terni, cerrus, serra); W cf. go-gryn, -grynu ('sift', fr. *upo-?^); Ir. cf. críonna, indecl. adj. (discerning, shrewd', fr. *krisont-); O-gde in OHG hreini ‘pure’; ONorse: hreinn, id.
7928:kriquos, à (?) ‘comb, crest, rake, serration’ OW & W crib ‘comb; crest; summit’; cf. cri- - bin ‘rake’ and cribell, f. ‘cook’s comb’; Br. krib ‘comb’; kriben, kribel ‘crest; hoopoe’ beside kriben, pl. u, iu, f. ‘curry-comb’; Cor. cryb ‘comb, crest’; cryben ‘crest’; Icel. hrífa (‘take’. Phon. of ülfr ‘wolf’);
14254:qurisnos ‘kind of oak’. Cf. WP I, 524 Gk. prínos, mf. *holm-oak; scarlet oak’; Lat. cerrus, gs: -1, f. "oTurkey-oak'; W prin-wydden, f. (“scarlet oak’. For -wydden, see uidh-, be- low). (The phonology is that of Gk. hung: Lat. serra, see srisnà; Gk. tris: Lat. ter, see tris; Gk. kríno: Lat. cerno, see krin-)
17092:srisà, srisnà “file, saw’. (onomat.) Per. arrah, id.; Oss. xirx, Dig. xirxá, s. ‘saw’; Kurd. ere, id.; Gk. hung f. ‘file’; Lat. serra, f. ‘saw’. (Phonol. of cerrus & Plautine terr ‘3 times', cf. terni, cerno, etc.)
```


## [2026-09-14T02:28:59.675Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef leafof(path, lineno):\n    txt=open(path,encoding='utf-8',errors='replace').read()\n    lines=txt.split('\\n')\n    pre='\\n'.join(lines[:lineno])\n    return pre.count('\\f')\nprint('IEC srisa leaf', leafof('IEC.txt',17092), '-> printed approx', (leafof('IEC.txt',17092)-15)*2)\nprint('KLN jackal leaf', leafof('KLN_1966.txt',20110))\nprint('KLN serra leaf', leafof('KLN_1966.txt',34714))\nEOF",
 "description": "Compute leaf numbers for IEC and KLN hits"
}
```


## [2026-09-14T02:29:01.072Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20110,20112p' KLN_1966.txt | fold -w 200 | head -20\necho \"---- serra full\"\nsed -n '34719,34727p' KLN_1966.txt | fold -w 200",
 "description": "Print Klein jackal and serra entries"
}
```


### [2026-09-14T02:29:01.197Z] TOOL RESULT

```
IEC srisa leaf 704 -> printed approx 1378
KLN jackal leaf 444
KLN serra leaf 756
```


### [2026-09-14T02:29:01.269Z] TOOL RESULT

```
jack,  n.,  1)  a  sleeveless  coat;  2)  a  vessel  for  liquor. —  OF.  jaque,  ‘sleeveless  coat’,  fr.  Jacques, ‘Jack’,  a  nickname  given  to  the  French  peasant in  the  14th  cent
ury,  for  this  kind  of  garment was  used  especially  by  the  peasants  of  that  era. See  Jack  and  cp.  Bloch-Wartburg,  DELF., p,  333  s.v.  jaquette.  Cp.  also  jacket.  For  sense develo
pment  cp.  jacquerie, jack,  n.,  an  East  Indian  tree  ( Artocarpus  inte- grifoiia).  —  Port,  jaca,  fr.  Malayalam  chakka, lit.  ‘something  round’,  fr.  OI.  cakrah,  ‘wheel, circle
’,  which  is  cogn.  with  Gk.  y.bw'koq,  ‘ring, circle’.  See  cycle  and  words  there  referred  to and  cp.  esp.  chukker,  hackery, jackal,  n.  —  Turk,  chagal,  fr.  Pers.  shaghal,
  fr.
OI.  srgaldh,  lit.  ‘the  howler’, jackanapes,  n.,  1)  a  monkey  (archaic);  2)  an  im¬ pertinent,  conceited  fellow,  a  coxcomb.  —  Fr.
Jack  a  Napes  =  Jack  o' Napes,  Jack  of  Napes,  = ‘a  monkey  from  Naples  (in  Italy)’, jackaroo,  n.,  a  new  apprentice  on  a  sheep  farm in  Australia  (slang).  —  A  blend  of  J
ack  and (kang)aroo.
---- serra full
Derivatives:  serrat-ed,  adj.,  serrat-ion,  n.
Serricornia,  n.  pi.,  a  class  of  beetles  with  serrated antennae  izoot.)  —  ModL.,  lit.  ‘having  sawlike horns’,  fr.  L.  serra,  ‘saw’,  and  cornu,  ‘horn’.  See
1424
1425
seta
serra  and  horn  and  cp.  corn,  ‘a  horny  indura¬ tion’.  For  the  ending  see  2nd  suff.  -ia. serriferous,  adj.,  having  serrated  edges  (hot.  and zool.)  —  Compounded  of  L.  ser
ra,  ‘saw’,  and the  stem  of ferre,  ‘to  bear,  carry’.  See  serra  and -ferous.
serriform,  adj.,  sawlike.  —  Compounded  of  L. serra,  ‘saw’,  and  forma,  ‘form,  shape’.  See  serra and  form,  n.
serrulate,  adj.,  finely  toothed.  —  Fr.  L.  serrula,  ‘a little  saw’,  dimin.  of  serra,  ‘saw’.  See  serra,  -ule and  adj.  suff.  -ate.
serry,  intr.  and  tr.  v.,  to  press  closely  together.  — F.  serre,  pp.  of  serrer,  ‘to  press  together’,  fr.  VL. *serrare,  ‘to  bar,  bolt’,  fr.  Late  L.  serare,  fr.  L. se
ra,  ‘a  bar  (for  fastening  a  door)’.  See  sear,  ‘the catch  in  the  lock  of  a  gun’.
```


## [2026-09-14T02:29:09.899Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==445' KLN_1966.txt | grep -n \"^[0-9]\\{3,4\\}$\\|jacka\" | head\necho \"--- printed nums on that leaf:\"\nawk 'BEGIN{RS=\"\\f\"} NR==445' KLN_1966.txt | grep -oE \"\\b8[0-9]{2}\\b\" | head",
 "description": "Find printed page number on Klein jackal leaf"
}
```


### [2026-09-14T02:29:11.062Z] TOOL RESULT

```
33:822
57:jack,  n.,  1)  a  sleeveless  coat;  2)  a  vessel  for  liquor. —  OF.  jaque,  ‘sleeveless  coat’,  fr.  Jacques, ‘Jack’,  a  nickname  given  to  the  French  peasant in  the  14th  century,  for  this  kind  of  garment was  used  especially  by  the  peasants  of  that  era. See  Jack  and  cp.  Bloch-Wartburg,  DELF., p,  333  s.v.  jaquette.  Cp.  also  jacket.  For  sense development  cp.  jacquerie, jack,  n.,  an  East  Indian  tree  ( Artocarpus  inte- grifoiia).  —  Port,  jaca,  fr.  Malayalam  chakka, lit.  ‘something  round’,  fr.  OI.  cakrah,  ‘wheel, circle’,  which  is  cogn.  with  Gk.  y.bw'koq,  ‘ring, circle’.  See  cycle  and  words  there  referred  to and  cp.  esp.  chukker,  hackery, jackal,  n.  —  Turk,  chagal,  fr.  Pers.  shaghal,  fr.
58:OI.  srgaldh,  lit.  ‘the  howler’, jackanapes,  n.,  1)  a  monkey  (archaic);  2)  an  im¬ pertinent,  conceited  fellow,  a  coxcomb.  —  Fr.
59:Jack  a  Napes  =  Jack  o' Napes,  Jack  of  Napes,  = ‘a  monkey  from  Naples  (in  Italy)’, jackaroo,  n.,  a  new  apprentice  on  a  sheep  farm in  Australia  (slang).  —  A  blend  of  Jack  and (kang)aroo.
60:jackass,  n.,  a  male  ass.  —  Compounded  of  jack, ‘male  of  animals’,  and  ass.
61:Derivative:  jackass,  intr.  v.,  to  ride  a  jackass, jackass  copal,  Zanzibar  copal.  —  Corruption  of chakazi  copal,  fr.  Zanzibar  chakazi,  chakazzi. jackdaw,  n.  —  Compounded  of  jack,  ‘male  of animals’,  and  daw.
62:jacket,  n.  —  OF.  jaquet  (F.  jaquette),  dimin.  of jaque.  See  jack,  ‘a  sleeveless  coat’,  and  -et. jack  rabbit,  a  long  eared  American  hare.  — Short  for  jackass  rabbit;  so  called  in  allusion to  its  long  ears.  Cp.  its  earlier  names  mule-eared rabbit,  mule  rabbit.
--- printed nums on that leaf:
822
```


## [2026-09-14T02:29:11.542Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==705' IEC.txt | head -5\necho \"=== page nums:\"\nawk 'BEGIN{RS=\"\\f\"} NR==705' IEC.txt | grep -oE \"\\b12[0-9]{2}\\b\" | head",
 "description": "Find printed page numbers on IEC srisa leaf"
}
```


### [2026-09-14T02:29:12.657Z] TOOL RESULT

```
cipice’; cf. stremit'sa, v. ‘rush, gush’; stremglàv ‘headfirst’
sren- ‘loin, kidney’. Cf. rénos, is Lat. rén, gs: rénis, m. ‘kidney’; Li. dial. srénos, usu. strenos, fpi. ‘loins, waist'. (NB. The initial str- is characteristic of Latv., where the wd. does not occur).
(srep-, improbable reconstruction for (1) strep-, (2) urep-, q. v.)
sret- “spread, expand, spill, flood”. (variant: stret- ? for OCor. and OHG). Ir. sreathaim, v. *spread; shed'; (OCor. stret, Cor. streth, pl. ow, f. ‘stream, flow? conflicts w. phonol., since sr- normally Cor. & W fr-, ffr-); OHG str&dan, sv. ‘well up, spurt’; (uncertainly Gk. rheità, npl. ‘streams’, preferably fr. *sreuito)
sreum- ‘flowing; flow, stream; pour’. Cf. sroum-, sru-, etc. WP II, 703 Gk. rheüima, n. ‘flood, current’; Alb. rrymë, f. ‘current’; Olr. sráaim, id. (*-eu- or *-ou-); Li. cf. (o-gde) sraumu0ó, gs: eps, m. id.; Gk. cf. rhéa, adv. ('easily', fr. *sreum). (W rhuf, m. 'gush' suggests a type *reum-, roum-)
=== page nums:
1277
```


## [2026-09-14T02:29:20.518Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BLY p.78 (leaf 11) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==11' incoming/BLY/BLY_pages.txt | head -80",
 "description": "Print Bailey Hvatanica II p.78"
}
```


### [2026-09-14T02:29:21.641Z] TOOL RESULT

```
=== BLY p.78 (leaf 11) ===
 78       HVATANICA                                  II


  sira-,                 not              to          Av.              srzra,       sin
       sayr                (ser),                 NPers.                 sTr    '   sat

  harmgrita-                                 to         hamggalj,               as   h

ha.ngris- as ham.thris-. [Iran. grab- had ptc. *grb-td-, Ba]5ai gipta,
     NPers. girift, and *gorb- before suffix in Av. garaft-.]

ha.mgrautta-
haththa-      < *ham-grabita-
         < *haoya, certainly not (?).
                                 *har(a)-sthd-, which is found as
     harstaya-.
hamthuta- to patkhuta-. Chorasmian -l'.
hana- 'blind' < OIran. *anda-: the meaning of O0ran. *hana-
     ' old' is quite different. Sogd. 'nt.
hambrausta-, not *sampravista- which cannot explain -au-, but probably
    to -rauys- in parauysard.
hamura- ' forgetting' < *framar- ' forget ', cf. NPers. fardmii/.
havia- ' one's own', OIran. *hvaipa0ya, Mid. Pers. Xvgpas, Pavta xpul,
hi-mTjnaa- ' bleeding', adj. to a secondary form with -ka [ny > iiy, n~.
     not > nj].
hota- < *frdvata , Armen. havat, with vat, Av. fra-, aipi-vat-, Skt. api-vat.
haur- < *fra-bar-, OPers. fra-.bar- ' offer, give '.

   Many other points need further elucidation. We are, however,
fortunate in having this valuable instrument for the further study
of Khotanese. It is particularly useful to have a complete Index
verborum of this text, in which the language is 'Classical' in com-
parison with the later texts.




                            This content downloaded from
          71.172.217.118 on Thu, 11 Feb 2021 00:49:26 UTC
                    All use subject to https://about.jstor.org/terms
```


## [2026-09-14T02:29:23.672Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD sagr/ser ===\"; grep -n \"^ser\\b\\|^sagr\\|^syl\\|sated\\|satiat\" PHD.txt | head -20\necho \"=== NYB ===\"; grep -n -i \"sagr\\|s\\[e\\]r \\|satiat\" NYB_vol2_glossary.txt | head -20\necho \"=== HRN sir ===\"; grep -n -i \"sīr\\|sir '\\|satt\\b\\|gesättigt\" HRN.txt | head -20",
 "description": "Grep MacKenzie, Nyberg, Horn for sēr/sīr satiated"
}
```


### [2026-09-14T02:29:23.766Z] TOOL RESULT

```
=== PHD sagr/ser ===
562:sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo | M sd, N ~] hundred. Sadwés [stwys | M sdwys] a star (Fomalhaut ?). ваб [KLBA < A klb | N ~] dog. Zeag [sk!] stone. sag [PR | P g] number. sagén [skyn! | M sygyn] stony. sagr [sg] | N sēr] sated, satiate. «ЛЬ: satiety. sahig [shyk' | M shyg, N sahi] worthy. ~th : worthiness. sahistan, sah- [MDMEN-stn' = A mdmh, V dmh | (M shyd, s‘y-)] seem; seem proper. ~išn: satisfaction. sahm [skm | = M, N ~] terror. ~gin [-k(y)n! | N —gin] terrible. ~genith : terribleness. sahög [shwk'] hare. sāk [s | (N sdw)] tribute. sal [SN T < A fnt | (M sr), N <] year. -sálag [SN TA, oli | N -sala] . . . -years-old. ~ih: age (of... years). salar [srd?] | M ffr, s’r’r, N ~] leader, master. ^h : authority. salwar Leikofl perennial. sāmān [?mn! | = M, N ~] limit, boundary. —Óómand [-’wmnd | M -wmnd] bounded. samór [smzl | N ~] sable (marten). sàn [?л! | N ~] kind, manner.
3514:sated, satiate sagr.
5398:ser Nee
=== NYB ===
1754:expressed (nominal sentence as in the Semitic languages): man Sähpuhr hom 154; tē ke he? 737; to rād ke Dugdav he 4721. en rētak ke hast? who is this boy? 1617; Artaxsér ... nē pat giyāk hast 6?" sq.; kë zan-& hac õi hucihrtar nest ‘qua pulchrior non est mulier', who is the most beautiful of all women 259-19; ēzšān amüh hem ke ... we are of those who 5723-24, šmāh ke xtēn het 6111; sagr hend 86%, — 3. in the 3d p., together with a subst. virtually in dat., or with a pron. in cas. obl., it expresses ‘to possess’ xdnak i-t hast the house that belongs to thee 5325-26; fradandan i-5 hast the chil- dren he has 142; with ràd as in NP: Papak rüd pus-é hast 3?. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions, e. g. han- dešitar vicītār hom 125; frēftār hah 3419; matür hom 46’; kartar hom 101?’; brihenäk hend 7777; ke (cas. obl.) vitīrišn nest which is incorruptible 66°; tö hän-ic äkäh he this thou knowest 399; hayyär hend they help 106%; -š hayyaréh hénd they help him 1001-12; pat kamēstārēh + spihr hénd they offer resistance to the. Sphere 8721; ké (cas. obl.) Mihr u Mah pat pust hah which M. and M. protect 317-8, ete. — 5. auxiliary vb. forming compound tenses: būt hom, būt hend I was, they were, eto., v. Grammar; notice: HWH-nd, regularly hend, must stand for the subju. händ 14? (fut.). 335 (cond.). — 6. Wrong use of the ideogr. HWH-: a) HWH-wm for the encl. pron. lst p. sg., added to the pret. pass. in order to emphasize the agent-
2734:the pronunciation nikér- < *ni-karyati (of the same type as the syn. spas-: spasyeiti ‘he espies, finds out’, cf also Skr pasyati), which also accounts for Paz. NP nigar-, niger-, ci men(itan) < *manyati: Paz. manidan, minidan. Hübschmann, PSt. 102, no. 1038, nikir- < *nikriya- (better *nikrya-), accepted by Bthl; I disagree. - Arm. lw. *nkirt- (< *ni-kirt-) in nkrt-em ‘to strive for, to care for’ in the N. T., Ep. ad Philipp. 31%. — To be combined with 2kartan; cf also Skr kal- ‘to observe, to mean, to consider’.
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3007:doubt and its antonyms (gumdn, apé- gumän, apēgumānēh pat), reliance (upon); — to look on, at (nikéritan); to consider, regard as (dāštan pat); to make a p. such and such (kas kartan pat + subst., often in the cas. obl. sg. ending in -čh); to entrust (gumürtan pat kas); to get married (v. zančh) ; etc. ete., v. the individual ws. — 9. forming adverbial expressions: from adjectives, with or without the ending -éh: pat buland aloud, pat sihsčilak, pat näm- cist; pat bavandakeh, pat perözeh, pat sagréh, pat tuxsakéh; from a subst.: pat frazam, pat dēkān; pat hamäzakeh, pat sihsaleh, pat bundahisnéh, pat paitiyära- kēh; pat ax"arišneh without food; from adverbs: pat uléh, pat niküneh, pat apākēh. — 10. compound expressions: pat
3366:sagr [sgl] (sēr) satiated, satisfied 862. — Ps. sgly; Paz. NP sér; -ayr- > -ér- ac- cording to the common SW law, cf šer.
3367:sagreh (séréh) satiation, repletion 5012. 7218,
3573:Sagr
5687:sr’w-: srutan srwš*w: Sroš sxt: sacišnēh sy’w, sy wg: siya šh-: šayistan Šrg: Sagr
6131:Sb: Sap Sgr: Sagr Shr: Sahr
6802:sér: sagr
7387:sēr: sagr
7443:Sér: Sagr
=== HRN sir ===
408:Zäl), dass jener edle Löwe (d. i. Rustemj satt wurde (Mohl's Über-^— XVI —
9419:«) Reimt auf sir 'Milch* (Öflhn. I, 240 Vers 1982).
```


## [2026-09-14T02:29:43.871Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT srira ===\"; grep -n \"srīra\\|srira\\|sri ra\\|schön\" BRT.txt | grep -i \"sri\" | head -20\necho \"=== BRT srva / lead ===\"; grep -n \"srva\\|sru-\\|Blei\" BRT.txt | head -40",
 "description": "Grep Bartholomae for srira and srva/Blei"
}
```


### [2026-09-14T02:29:43.950Z] TOOL RESULT

```
=== BRT srira ===
2872:aoxta  zaraiiuitrö:  mmö  /taomifi  "drauf, sprach  Z.:  'Verehrung  dem  .ff.'"  Y.(j.i6, 3,  /£>.  17;  -1.2,  Az.  I,  Yl  /.  5,  21,  j.  2, 5.83,  91,  95,  i<.io,  77.54.  V.  2.  40,  42,' 3.  26,  Vyt  24,  54,  Vd.  12,  20;  —  ,7a/! Aim  aoxta  p»r>sö  yö  narl  asaonö  un'a:\ as.'a  ..  "und  es  sagte,  ihn  fragend  ..: 'Und  wer  ..'"  H.  2. 10;  —  äal  aoxta  akurö  \ ..  yimii:  yima  srira  "und  es  sprach  Ah.^ zu  y.:  'y.  . .'"  V.2.22; — yö  naire  aoxte (3SP0.-  M  ml  aä  (sd.)  F.^d;  N.;,^,! tft;  —  aojUa  (jSPr.)"  ../raiaoitrazibya  ..: aiayata  . .  Vyt, //;  —  at  Aöi  aoß  (iSPr.) zara'httströ  paourvTm  "Drauf  sagte  ich zu  ihm  ersthch:  ^Zar.  (bin  ich)'"  Y.  43. 8.  a  )    mit    uili  (sd.):    mi^rim  .  .  yö
5754:•  j.  asö.söidra-  n.,  Plur.  'Stätten  und Wohnplätze'(?)":  kaia  xi..  yzarqm  atwi- yzanm  srirasca  'rasca'>  gaoyaoiliS^a  ilta- cin/ls  (sd.)  YtÄ42.
5880:•  j.  asp5.stao/ah-  Adj.  (fem.  °ye/tJ-) 'starker,  umfangreicher  als  ein  Pferd, Pferdeleib"':  xä  'yehls  apam  \'t.8.$,A2; —  srira  vü  ar»)im  b.lzava  aurusa  "ythTs'^
6091:—  kadä  vatds  yezT  <ahyä  xlayaüa  (sd.) masda  °sa  (Vok.)  ".  .  o  M.  und  Asa" Y.4<?,g;  i^.  18, 50. 9;  —  atvs  staoiä  aojäi (sd.)  mazda..  'sa  Y.50,11;  2,  6,8,  2Ä  i, 34.T,  —  hvö  zi  "Sil  .  .  ahamMs  (sd.) urväkS  masds  Y.44.2;  18;  —  ara' (sd.) sf  xsmä  mazda  °s3  ahurä^^''  hyal  .  . yoorjaaäa  (sd.)  Y.  50.  5;  —  in  GHapt: masda  aAura  .  .  fava/ä  haxamS  (sd.) -sahyala  \.4a.ii.;  41.6; —  *aAura.mazda °ia  (Vok.)  srira  Y.j'5.3;  —  masdai  ahurai 'säila  vahistai  Y.  JJ.  j ;  4/.  i .  «)  in dualiscjiei  Verbindung  mit  ahura-:  yöi  vS syaoianäissärMil{%d.)aAurff*asa*Aisvä^''''> axhai/ ..  Y.51.3  (s.c).  b)  neben  VoAu- ManaA:  yäcS  vehü  uxoa  fral%  (sd.)  ma- nauAä  yOcs  °sa  (Instr.)  aahlus  Y.  44-  8; '31  —  yf  «""'^  "^  (Instr.)  tmüi  hvö *mainyJus  a  vaMstat  kaya{iA.)..  Y.S3.6; 4g,$;  —  %wavas  . ,  masda  hadtmsi  (sd.) -ia  vohulä  yyas  manavkä  Y.  44-  9 ;  2Ä  5 ;
7655:•  j,  »radva-fana-  Adj,,  nur  fem,  'ni-  'deren Brüste  in  die  Höhe  stehen,  mit  straffen Brüsten':   kainTiiö  hhrpa  sriraya  .  .  'r/yä
8705:—  'saiihqm  para  frSritSii  FrW.  /0,4i ;  — ytzi  xsapsAva  mpr^ncaiie  (sd.)  'lakva bisazyat  V.  l'7.3J  —  uü'  (LS.).  A)  als weibliche  Gottheit  gedacht:  'sqm  (AS.) sriram  yazamaide  'säuAfm  . .  xsSi'inJm ravaLaspqm  .  ,  "säPikem  .  .  nvim  ranjat.- aspqm . .  avqm  'sqm . .  G.  5. 5.  a)  Name der  fünften  und  letzten  der  (priester- lichen) Tages  abteilungen*';  vupim  paiti "sauham  ä  kB  vaxsat  "immer  in  der Morgenfrühe  bis  Sonnenaufgang"  V.  /y. I.  3)  mit  süra-  Adj.  Name  des dritten  Abschnitts  der  Nacht**':  hö tiurr/ö  (j'S  parö.dars)  väHm  baraili  upa 'iaukim  yqm  särqm  V,  iS.  15;  —  'sqm särqm  V.2j\}.
10303:—  upäai  hi  (näml.  der  Hündin)  °iBm baraym  .  .  V.  jj.43;  —  ma  °tSm  nipail- yavuka  (sd.)  Yt/7,57;  — yats  {sA.)  °lus .  .  x^ar^^a  .  .  V.5.55;  —  star»tasca  -tui anyfma  ..  avar?tä  YLJ7.  7;  —  agsqm 'tava  (NP.)  kistmte  husiania  .  .  zaran- yapaxsta.pmSnkS  'S.t.i'j.f);  —  ya'ia  nä fryS  .  .  slanta  °tul  (AP.)  sayamanS  (sd.) V.^.25;  —  'tu  (AS.)  ^x^ainUtarftu  tnai bariziia  . .  nisirinuyät  V.  /4. 1 4 ;  Yt  ?.  i  o  2 ; — aisam  vantsnks  °A(/(  AP.)  paiti  *äak»ute (sd.)  ysi  srira   banzis.havanis  Yt, /7,  10;
10762:•  j.  'xSa*r5.k8r»ta-  Adj.  'fiir  den,  die Herrscher  erbaut,  fürstlich';  *antarp.anhm nmänake  srirahe  'tahe  Yt  i-].  60.
12424:oAurischta  Religion :  kahmät  paoiryS  mal-  \ yänqm  , ,  frada^ayS  'nqm  ,  .1  . .  yimäi .  .  fradaisalm  °nqm  .  .  äai  hi  mraom  . . vUanha  ml  minlff  b^ntala  (sd)  "nayäi (als  Gen.)  äat  . .  pailyaoxta  yimS  .  .  nSit dato  ahmt  . ,  tnirstl!  b3r?tala  'nayäi  V. 2.1  ff.;  Ytn.  14;  —  vXltäspaht.  .yS  batuUa upastaca  vTsata  .  .  •nayä  Yt  13.  99;  — ya%a  axsm  Asüyene .  .  zara%uänm  anu- matSe  'nayäi  anuxtie  'nay3i  anu.värltSe •nayäi  Yt.  j,  18;  Y.t?.  7;  —  hutaosqm  .  . yä  rrn  °nam . .  zraiia  (sd.)  dät  apica  aotaf Yt  ().26;'Vyt.  Jo(?);  —  ks  .  .  'nam  .  . vJbarat  aitaisva  vanfsva  ySyimö  ktnrtaoi^ .  .  vTs  iarsipia  V.  2. 42 ;  —  satö  .  .  zara- huiirS  .  .  ita  apam  vTjasaiH  .  .  °na  .  . vlspais  avi  karsvqn  Yt  jj.  94; —  mi^nm . .  yahmi  vyane  (sd.)  °nayäi  (als  Gen.) srirayai  p}r>^u.fräkaysi  . .  Yt  10.  64;  — sraoi^m  .  .  yB  damsJisS  *°nayä  Y. 57.23;
13262:I  des  Inhalts  (?) :  srira  doonifi  dacjnäna  dü-
15059:•  j.  paiti-srira-  m.  EN.  eines  Gläubigen":  '"^J^Y-^P- 43.;^ usmänaraheca    pailataahs    'rahe    Yt.  y.       *    °"  ""  *"""
20897:srira  ustavaitica  ya  *süra  Yt. /p.  67;  — gäui ya  ca?9rat3haxl ya  .  .  frasarsta  Yt. jo.  38;  —  alis  (Stverz.)  vavuAi  yä  hr>- zaiti  Yt/7.  25  usw.;  V, //,  9';  —  hutaosa yä  pourubrä%ra  YLJ5. 35;  —  aß  ya awzdänva  nqma  Yt  rp.  6  2 .  o)  aisa  druxs yä  iMSUs  Y.j.i  usw.;  —  a^sa  ya  kaine V.  J5.9— 14*;  —  *avau  pairika  ya  dui- yäirya  Yt*.  54;  —  ha  druxf  ya  nasus V.^t.is  usw.;  5.21, /Ä  31.  c)N.-ASn.; zrayS  yat  kqsaSm  Yt. /p.  66;  —  »o»  asti .  .  ahm  yat  vahtstim  Yt.  ;.  25 ;  —  yS  .  . staoia  as»m  yat  vahisttm  YL  J7. 18;  Y.lQ. %y. 18.16;  —  'kvan  yat  amshm  Y\.  (j. 4; ig.  65;  —  haicS  ksrmaoiti yat  avästnm  V. i3.%\;  —  aoinmän3Myim  (als  APn.)  «"iM- paihitn  Yt5.63;  62;  —  äyapDm  ya^  ahu- 39*
21828:—  -malte  x/dire  .  .  nSil  saurva  änha nSii  rnfry%yu/  Y.  g.  5;  —  'mJi  srirai  .  . paoiryB  masyänqm  aptrise  aam  yS  ahurl V.  2.  2;  9,  23,  75.39;  —  äat  'ms  varsm (sd.)  kirmaot  V.  2. 33';  39;  —  aisqm atnanhqm  vlvanhusS  trOvl  'masct{  "zu diesen  Frevlem  gehört,  wie  bekannt,  auch y.,  der  Sohn  des   Vtv."  Y.32.&.
27397:srira-
27427:•  ].,  g.  srira-  Adj.  (fem.  T3-)  i)  "schön anzu  sehen,  schön' ;  a)  vom  schönen Äussern  der  Menschen  und  Götter:  virahe kihrpa  ,.  'rahe  YX.14.2T,  17;  —  kainlnö kihrpa  'rayä  Yt.  5.  64,  H.  2.  9;  —  'rB ahi  tara^uilra  huktntB  ahi  . .  kvascvB darrj^.bäiäus  Yi.i-].%z;  —  kikrpasla  ,. 'ra  amisanqm  sppntanqm  Yl  y .  8 1 ;  F.  72 ;
27437:sriraoxäan-
27442:•  y  sriraoxian-  m.  EN.  eines  Gläubigen : 'xfnS  aiaom  YL  y.  loi.
27447:kompar.  ans  srira-.  -~  Pfl.:  nniailar.
=== BRT srva / lead ===
6418:•  j.  a^ö.zuita-  m.  (theologischer)  Name der  Eule*':  /«//»  t!  tmrr/a  'ta  ima  srva raPtayein't . .  imas»  tE  srvä  m>rrfa  °ta  hyäri aritayasca . .  paiti  dagvS  mäzanyan  V.  ly.  9,
8395:•  j.  upa-srvant-  Adj.:  s.  unter  srvanl:
10138:—  tistryS ..vaz»mnö  -Jus  k)hrpa  zaranyS.-  bagä  x^ar^mnif  (sd.)  Y. 32. 8;  —  "Su/x'ar»- srvahe  YLÄ16;  i4-l,  Y.ig.yi.  A)  Das  \%ahe  nr^yJ  V.7.  43; — 'Sul  vä  s^var3%ahe Rind  gilt  als  Repräsentant  aller  nützlichen  j  (sd.)  vä  W.14.1T,  —  '!us  i^ar/itinqm {ahumohtn)  Tiere,  daher  ^gav-  auch  inJH, /.  5;  —  yasca  ..  lanumazs {^A.)  'Jui weiterem  Sinn  gebraucht  wird*"':  para\da%at  "W-iS.!!);  —  °amla  ifsst)m  anäp»m •Su^  ca^war).paitistanaya  dänheit  para\{%d.)  V.5,  52;  S3f.',  7.55;  —  buiri 'aas  ,  . nars  asaotiB  bipaittstänahe  zq%st  Y.  /p.  8 ;  j  3far>^a  . .  VyL  4:5.  3)  'Milch',  bes.  zur
10924:fl-'Eiweiterung^'t  lus  dem  V.  'zan-;  ^zS.m, S6.  —  M.  jijiiäsati,  jnälah ;  np.  Haäsad  'er erkennt''),  lat.  ^näjfo.  —  i)'Vgl.  Hirt  Abi  au  i 93.  —  ')  mp.  inätan,  np.  sunSdan  "höien' (Hbu.  FSt  8z)  scheint  auf  einer  Kontamina- tion von  air.  xsnä-  und  sru-  lu  beruhen;  vgl. auch  die  PD..werter  SWienAW.  jhS.  880, GIrPb.  /  b.  306.  Undeuüich  Ut  mir  ClrPb. I-  303.  34 1
11372:üyatis  axsaia  kauHy  .  .  mrasatiy  . .  D. 5.  3.  b)  im  Aw.:  ya  maninumlit  mya- dinqm  ..  upa.vaz^ilte  YL/_J.  64;  —  huxsa- "^röJfMäi^it  at  xsäir^m  illyät  yat  ahurai A.3,6;  —  nitjin»m(sd.)^it"^  apjrinayükim V.  j?.  38;  —  yä  umm  (sd.)  p»r?7Um  k»T3- naoiti  p?r7n^m/it  viyzärayäti  (sd.)  V.  22. I  s;  —  avatUim^il  bandayeiti  bantsmca  drütn I  ksrmaoiti  V.  22.  j ;  —  äsnqmlit"^  frasain- '  tm  Yt  10. 108,  1 10,  Y.  ö^.  1 1 ;  —  asnas- ät"^  xraitts  Yl  10. 107 ;  —  darrf^mUt"'' aipi   srvatum   Y.62.  3,  Yt/(J.  z6;  JJ.  54;
11399:Zur  Herkunft  des  'Slamms'  s.  415  ß  No,  l  ]), Bg«.  GrGr.3  321;  urir,  '/ana-,  S  2g8.  4.  — Pü.  (lu  V.)r  pa  ii,  (lu  N.):  evakH.  —  ')  So nacb  dem  Zusammenhang  und  Pü.;  s.  auch zu  srva-i  syntaktisch  anklat.  —  ')  Nach  dem ai.  na  .  .  ikai  eand  wäre  nna  (sd.)  la  er- warten; der  Flexionsausgaag  könnte  von  den umgebenden  Worten  stammen.  —  3)  Aber  das dort  angefühlte  'ciaa  ist  nicht  Instr.,  sondern PartikeL
11799:'los  machen  sva.  loslassen,  fallen  lassen in  — '  {paili  mit  Akk.):  yö  bansma  *taosa- yäti'-^  draos  (sd.)  vS  paiti  ss'inma  "wer einen  Ä-Stengel  fallen  lässt  in  .  ."  N.  loo. mit  dpa  (Kaus.)  'leer  sva.  schwach, (Ohren)  stumpf  machen':  narqm  mii:rö.- drujqm  .  .  apa  gaola  taosayeiti  Vt/0.48. mit  upa  Kaus.  dnwS.  2 :  yS  .  .  vars- sas^a  hqm.räsaydti  . .  srvaica  upa^wsr»- sinti  a'ka  d'tm  *upa.taosayäti  *utiähva  dim ralsayaca  (sd.)  V.  17.2.
12787:a)  als  Akk.  ohne  Kiicksicht  auf  Numerus  und Genus*',  zurückweisend:  y5  .  .  vamäsca hqm.räzayäti  . .  srvaiia  . .  a%a  'im  *upa.- tagsayäH  *unähva  dim  rat?aya{%A^ca  V. 17,2; — srväbya  may>m  ava-kansis  ..paiti 'im  äbarsii  ".  .  für  die  Nägel  sollst  du eine  Grube  graben  . .  du  sollst  sie  hin- bringen" y.ij.T,  5;  —  sao%rä  ..  a%a yS  'im  *frahinHn  (sd.)  N.  68-,  —  hqm.- vaniflm  .  .  framm.narqm  .  .  yä  d°  (näml. narSuil)  jasaiti  bafs'baxttmcii  (sd.)  yä narqm .  .Nt.-j  .^.  b)  alsGen.'';  a)  zurück- weisend auf  ein  Relativ:  yas^a  ..  aparao- oayete . . pairi  'im  lanava  anm..urvän3m haca  vahistat  a»haoi  ".  .  procul  eius dislinebo..animama.."Y.jp.7">.  ß)  vor- ausweisend :  ÄS  ba  aisS  äs  .  .  yS  .  .  paiti.- hincaiti  ä  'im  nBit  apivatäite  dainayh  ,  .
12924:■  j.  dar9f  ö.x^a^ta-  Adj.  'der  lange  Zeit, immer  der  eigenen  Bestimmung  untersteht sva.  cmg':  %waäm  afaZafym  .  .  irvaram akaramm  . .  trvatvm  'ttm  yazamatde  Ny. /.  8; — %wasahe  j^atataie  srvanahe  akara- nahe  srvanaAe  °take  Y.72. 10;  —  vayqm 'Um  Ny.  /.  I .
15113:•  j.  paiti.hin^  Int  'anzugiessen,  zu  be- giesseo',  bei  der  rituellen  Reinigung:  ^:i srump'  "wenn  ein  Bleigef^  zum  Begiessen (dient)"  V.g.  14'»,
15747:•  j,  paurva-naema-"  m.  'die  vordere Seite';  nur  Abi.  'mal  'von  der  Vorderseite her,  an  der  Vorderseite'  sva,  1}  'vom,  vor- aus', a)  absolut:^«!  aM  °mät..ym paskät Yt.iS.2.  h)  mitG^a.: yeAAe  °m3t  vazaiU jvnihraynS  "welchem  voraus  fährt.."  Yt. 10,  Jo; —  ms^r)m..y5  tarU harqm  asnaoiii °tiist  amisahe  hü  ".  .  voraus  vor  der  ud- sterblichen  Sonne"  Vt./o.  13;  —  auirmja- yais  aom  srum  °mäl  ahe  gr-avaAe  "üa  soVisX befestigen  das  Blei(gefäss)  vom  an  dem Stock"  V.  §.  1 4.  a)  'kopfüber'  (?) :  'mät  '> paiai  dyaos^S^.  761  u.)  ..  artrö  mainyus Yt.,?.  13-
16741:•  j-,  g.,  p.  bav-  V.  'werden'.  Fraes.  1  \hm  V.  7.  52  PiiZ.;  —  iJ»«*'  gag'^ia  ''amar- bu;  bv-'\  2  bava-,  3  bva-'\  17  (Fat.)  ] säntis  Yt  ig.  12;  —  iä  srva  ..  bun^  .. büiya-,  22  bJ-'^,  [25  'vlli/\'>,  27  buya-(^)i']  dagvattam  karstayasia  . .  "die  Nägel  wer- Perf.  I  bväv*',  2  babv'^;  J-Aor.  i  bUs-*''.  \  den  zu  Messern  der  Z>.  und  . ."  V.  ly.  10; —  PPfP.  bsta-]  Inf.  buy^,  'bata,  bOzdyäi.  —  vXsp^m  a  ahmat  yat  kan5  .  .  bavaj I)  'werden  sva,  ins  Dasein  treten,  ent- ,  "usque  eo  donec  senex  . .  fuerit"  Y.j.ig; stehen;  erfolgen,  geschehen':  vupim  a/a-'j,  32,  5.38,  5.31,  Y.  65.  9,  FrW.4.3;  — vamm  hsntiinca  bavanlimcai'^  bßsyan-'  itala  dai/iAävS  AuyäiiyS  baväitti  Yt  S.  36; titnca  ",  .  der  (jetzt)  da  ist  und  (jetzt)  FrW.^.jj — yat  baväni /rya  fri^a  paiti.- ins  Dasein  tritt  und  künftig  ins  Dasein  irdn/tf  (s.5)  Yt./J.sö;  —  siviÜS  bavski ya'ka treten  wird"  Y.2/.4,  Vr,/Ä2;  — vispam  ,mazdi  Az.2.  2-7"^  Vyt4*;  —  *ya%a*ra aSaetüS  sttm  haitimca  bavaintJmca^''  bäs-  ,buyäl  (statt  Plur.)  Aväyaonänhs  pantätüS yeintxmia  Y.  rp,  9;  —  vTspayS  afaonö  Yl/ö.  3;  —  yesnyS  ahi  .  .  yesnyö  buyi stuii Aai'ätyaica  bavqi%yäi^a^  bB^yqi%-\Y.62.i;  —  Uta  buyä  afrazaintis  Y.ii.i; yäi^a  Y,52,i;  68.22;  —  ala  Aau  apa-\  —  ta  tiS  buyqn  kumiid^Y.^^.2;  —  «ä«i ylärB  bvat'''  "da  entstand  jener  Abfluss" ,  e?  buyarps  masänä  Ny. _j-ii;  —  alsiJca Yt  ig.  56;  —  yat  kvan  uzuxsyäti  bvat'>  ■  ^wä  Smavantasca  buyamä  "wirksam  möch- zqm  , .  yacsdäi^rjm  "wenn  die  Sonne  auf-  i  ten  wir  durch  dich  werden  und  mächtig" geht,   erfolgt  eine  Purifizirung  der  Erde"  |y.  47. 4;   —   buyama  ahurahe  . .  frya  ..
19526:•  j.  'maj^-  m.,  mayä-  f.'>  'Loch  im  Erd- boden, Grube':  srvabya  (sd.)  'f»m  ava.- kanöis'V.iy.T,  5,  F.i7; —  baTvari  'yanqin (GPf)  irimaitinqm  aiühh  z?mö  aipt.kan- yät  V.  14. 6.  a)  insbes.  von  den  zu Zwecken  ritueller  Reinigung  gegrabenen Lochern":  mazdayasna  aiäAa  z?md  %rii (sd.)  'yjm  ava.kanay>n  dva  'fa  frasnä^aym malsmana  giul  *Bim  äp3  "die  Mazday. sollen  in  der  Erde  drei  Löcher  graben, zwei  Löcher  —  da  sollen  sie  mit  Rindsurin waschen  — ,  eins  —  mit  Wasser  — "  V.  76'.  1 2 ; Ä37; — paoirtm  upa  'fim  nt^w^>söis . . iitim  Ufa  . .  xltUm  upa  . .  "hrayS  anya  'ya ni^TVinssis  "ein  erstes  Loch  sollst  du  aus- stechen, ein  zweites  . .  ein  sechstes  . .  drei weitre  Löcher  sollst  du  ausstechen"  V. p.  6  ff.;  70. 18;  —  ^rJyS  yim  antari  vlta (sd.)  atitan  %räyS  {xh/as,  novo)  'ya  fra^ iärayBisY.g.  ii>;  11',  12,31; — arttanca (sd.)  .  .  'ya  (NP.)  V.p.  11;  —  karsascit frakäraySiS . .  ^ai  hala  'yaHbya  V.p.io; 29;  — paoirJfn  upa  *yim  frä.nasui  nanm (statt  NS.)  bavaiii  "am  ersten  Loch  . ." V.p.  28;  3iJ;  —  US  tansm  snayaSa  us vasirät  (statt  AP.)  gius  maSsmana  qpäca nava  (sd.)  upa  °ypm  "er  soll  seinen  Leib und  seine  Kleider  bei  den  neun  Löchern , .  waschen"  V.5.  54.
19742:1)  'bleiben',  nur  Kaus.  'zum  Bleiben zwingen,  aufhalten,  im  Wege  stehen':  at akfä  ma  bSndvak/a  (sd.)  mätiayätt  ^aZsS Y.4p.a.  a)  'warten  auf—,  erwarten': Wpatava^  vJ'itmiit^  ata  mam  amanaye^ yäta  adam  arasam  madam  Bh.2. 1 1 ;  6, 9.
20072:•  j.  mairya-  Adj.  (fem.  ya-)  'betrügerisch, tückisch,  schurkisch;  Schurke':  *ahalcti ♦»/•«'>  (NSf.)  nas'atagca  'ys  "und  es  wird  zu Grunde  gehen  die  Schurkin  und  verder- ben wird  der  Schurke"  Yt/p.ia;  4.Z; —  armatsis  deihrubya  avästryaia  (sd.) -ys  Yt/.  29;  —  tmnniaite  vJspqm  daiti- haom  'yS  mihrSjruxl  YLJ0.3;  —  °yS drvi  bizangrs  V.  5,  35;  —  sii^rqm yqm  karafnqmüa  'yanqmla  bieangn aimcur/anqmca  Y,  <>.  18;  —  *JanyS. 'yayh  Y.  JO.  15;  —  mä  hl 'y3  giurvayHt ma  /akika  Yt.<?.59;  —  nSU  *'yehe'''  ttSij jakikayä  t.io;  —  'yS  tBiryS  franrase  Yt. J.41,  J5-S6.  82;  8»,  77.5-5°;  —  'r^^ tairim/raarasyanam  YL5. 18,  zz,  ip.  77, Y. //.  7;  —  °yeke  tyaonaAe  ar»jal.aspahe Yt.  5.  30 ;  —  tafsatca  AS  °yB  (näml.  aiis srvarü)  Y.p.  11;  —  "«(NSC)  .  .  bSsyqsta FrW, /0.4a;  —  Sai  mqm  °yS  äkasat  atsrö mainyui"V.22.a;  2.  '  a)  ASn.  'rfm  ' Adv. 'trügerischer Weise.betrüglich':  a/trqm *rTm  küsayeiti  (sd.)  anaiwySstS  dalnqm "betrüglich  handhabt  die  Strafgeissel,  wer nicht  . ."  V.  18.  41'.  \az»M  maire  Yt /.  ag:  lies  zamara^
20830:—  N.-APn,:  vjspi..yä  h?nti  haptöMars- vShva  Yt.  6.  3;  —  dama  .  .  ya  k?nti  sp?n- tahe  mainySus  Yt,  6.  a ;  —  draomJbyS  .  , y  ä  aism3  . .  drävayäi  Y.  57.  a  5 ;  —  ASm, ; ../anal  azim  srvar»m yim  (s.II)  asps^anm .  .  yim  upairi  *vis  ''raooai  yim  upairi ktnsäsp»  .  .  pitam  pacata  Y,  5. 1 1 ;  Yt /4.  7,  9,  70.66;  —  va^am yim  (&,'n.)  vär?- hrayrum  yim  öarat  .  .  %raltaonl!  yim^ barat  ..  Ytig-^it;  8.6,  77.15,  '4-39*. 48,  ig.  35,  81;  —  mi'^rfm  ..yim  yazsnte daiAhupatayB  YL  /0.8;  11,47,  66,  68,83  f.^ 88,  89,  103,  109,  123,  8.  5,  36,  41,  44', 48,  7_5. 147,  Aog.  77;  —  spänam  ..yim (s.  II)  vavkäpar^m  yim  ..  duzak^m  nama aojaite  V.13.  2;  6,  18. 15;  —  ASf.:  avqm vanqm  yqm(s.11)  salnahe  yS  hiStaüe  mai- äüw  srayanhö  ..yqm  upairi  urvaranqm  .. taoxma  nt^ayal  yx.  12.  17;  —  arltis  ..yqm *ai9hyeiti  avi.mi%riS  Yt/o.  20;  21,  5.  6;
21216:vorausgehendem  farä  'antequam':  *ut- inidyäi  pars  hy"  möi  a.jimal  siraois  Y. 4_j.i2;  —  vaola  mSi  ,.parS  hy  mä yS  mSng pprfhä{%A.)jimaitlY.48.2.  4)dasVer- bum  {'ah-)  ist  weggelassen:  ya'ha  ii  anhm hmkinta  (sd.)  hy  ('wenn')  V,^7. 14.  b)  im j  Awr. ;  I )  mit  dem  Praeteritum  oder  Perfekt; /)  mit  dem  Praeteritum :  tqm  yazata  j3- mäspd  y  ('als')  spätem  pairi.avamat  Yt. 5.68;  61;  — y'  bitlm  a^artnS  apatamata . .  aom  afarfnS  hang^urvayata  . .  %raltaonl! Yt  ig.  36;  38;  —  vaäam  .  .  yim  barat  .  . %raifaonS  y  asis  dahlks  Jaiiti  Yt.  ig.  92 ; 93'.  77;  — y  titaral  anrS  mainyu?  dählm asahe  . .  antar»  pairi.avait>m  (sd.)  vohuca manS  -  .  Yt.  /^.  77;  —  frava^ayS  .  .  yä ta%a  ar^mih  kiliania  y  *mainyu  däman dai^Uem  YtJj.  76;  — y-  mqm  iura  (sd.) pazdayanta  ..aal  az3m  aguze  ..Ytiy.  $$; 10.  \;  —  y  tum  .  .  var^sSs(sd.)ia  *hqm.' rätayatiha  .  .  srvai'a  ^upa.^winsanha äat  tum  pascaUa  .  .  V,  /j.  4;  —  y  tum ainim  avafnSis  (sd.)  ..äat  tum  m/hiAöt/. . H.  2. 1 3.  a)  mit  vorhergehendem /<w«7Ä(i 'postquam':  yS  nüil  pas^agta  huix^afa  y mainya  damqn  daiZit^mY.^j.ij'K  b)mil vorhergehendem  para  ahmät  'antequam': ye^he  xlährata  nSit  aot?m  änha  .  .  para ahmät y..väam  anhai><lm  cittmäne (sd.) paiti.barata  Yt.  ig.  33.  c)  mit  vorher- gehendem vTsp»m  ä  ahmät  'donec,  bis':  ä dim  paskat  anu.marizatpm  ..vtspim  ä  ahmäi y  a^m  paiti.apayat .  .YlS-^B.  2)  mit dem  Perfekt:  taMu.mazS  (sd.)  ..  aiayqm *pa/re  *y  ^'  nöit  yava  miiiB  mamm  ,  . P.  iS.  3)  mit  dem  Praesens:  y  ('dann wenn')  asava  para.irihyeili  kva  .  .  havS urva  vaahaite  H.2,  i;  19,  V,/y.5o;  — äat  y  duidi  fradvaratti  ,  .  'hwaüm *yujyeite  väl^m  tnihrS  Yt.  70.  52;  48,  loi, (?.  9;  —  äat  y  aps  usbannte  ..  äat frahlSittti  .  .  fravaSayd  Yty.  65;  I4.(>Z',
27337:•  j-i  g-  srav-  V.  'audire'.  Praes.  1  srav-: srv,  10  surunav;  srunav- :  turunv-*'^ ,  16 (Des.)  suiruia-,  3  7  (Pass.)  sruya-,  30  (Kaus.) srävaya-,  PrP.  smvj;  Pert  i  susru-; j-Aor.  I  smi:  —  PPfP.  irSta-,  PFP. suruftvata-;  Inf.  srüidyai,  srävayeiihi,  srä- vayei'iyäi;  Absol.  -srut^m.
27372:•  j.  sravant-  Adj.:  s.  unter  srvant-,
27448:•  j.  srü-,  srvä-'>  f.  i)  'Nagel'  der  Finger und  Zehen:  paiti  te  m>rrfa  aiS^su/la  (sd.) ima  'va  (AP.)  va^ayant  V./7.9;  9;  — imsn  ts  'vh  minya  aisxt/fa  kyär»  arlta- yaslä  . .  "diese  Nägel  sollen  dir,  0 Vogel  A.,  als  Speere  dienen  . ,"  V.  17. 9; 10.  a)  Du.  '(beiderlei  Nägel  sva.)  die Nägel  der  Hände  und  FÜsse">:  yat  tarn ..varasasla  *hqm.räsayaj3ha ..  'vaf{AD.)ca *upa.%W3nsanAa  "wenn  du  dir.. und  die Nägel  zuschneidest"  V.  ij.  4;  —  ir  (Sp. 6a I  o.)  aisqm  paiti  *srvi  (AD.)'*  a^a äruxf  . .  upa.dvqtaiti  "auf  deren  Nägel kommt  ,.  herzugeflogen"  V.  7.  a4,  37,  g, 41;^.  14  (vio  sruye)**;  —  srvabya  marfim ava.kanSi/  "du  sollst  für  die  (abgeschnitte- nen) Nägel  ein  Loch  graben"  V.  ly. 7.  a)  'Hom'  der  Tiere  (und  tierähn- lichen Wesen,  s.  Komp.):  gSu/  .  .  yim upairi  sntye  (AD.)*'  sanal  (Sp.  1590  o.) amö  Yt,  14.  7.  a)  Piur.  mit  Aafia  Name eines  Sternbilds  (?) :  nitbayemi  m^ntuiSp. iiT4  0.)..nizbayemi  kapta  sraps  {AP.)i^ b.imya  V. /p.  4a,  3)  'Hom'  als  Stoff, 'Homstück'  (nur  Komp.  und  Ableit).
27481:•  j,  srva-  n.  'Blei;  Gefäss  aus  Blei'; ayanhaintm  v3  °rttm  **  va  rättma  (sd.) xsa^ra  vairya  "in'>  einem  Gefäss  aus Eisen    oder   aus  Blei  . ."  V.16.6;  5.14;
27483:Pü.  (lu  V.p.  14  3.St.):  truf,  (sonst)  snifi».  — '}  S.  Sp.  S9S  m.  mit  No.  1.  —  «)  D.  L  *sru-
27486:•  j.  srvant-,  sravant-  "  Adj.  'schleichend, anschleichend':  -afa/J  (GS.)  F. /^.
27490:•  j.  srvara-  Adj.  'gehörnt"':  asTm  'r^m .  .  yim  .  .  tairit?m  Y.g.  11.
27494:Vgl.  ReMY  JAOS.  20.  70  und  zu  srvara-  No.  I.
27850:.  .  arins  pmska  (sd.)  V.  z^,  11;  —    srvama
28593:ß-aiusaiti  .  .  upa  tarn  vanam  aiili  yam hs  min-jS ..  V.j.if.  Anhang.  'Äa- (subst.)  steht  an  Stelle  des  Pron.  rel.  in einenn  Satz,  der  einem  vorausgehenden Relativsatz  inhaltlich  koordinirt  ist*':  yat nmänö.paitim  vindätna  ..yö  nS  hub)r?tqm barat  frazaintimla  hd  v»r3zyat  YL  73.  40; — ■  aiim  srvanm  .  ,  yim  upairi  k>r»saspB ayanha  pitüm  pacata  . .  tafsaica  h  S  uiatryH afUatia    Y.p.  II.  2)    auf  ein   Relativ
29915:Et.?  —  Pü.:  matai.  —  >)  Ali  Gegenstück  lu  ^aSa  upanh'^'  ayaahattam  vä  srum  vS "-l"":-  "^hy-  "■?■/■.-  '}.  ^."'*  <!'«  f^'«?*=  "Rindsurin  sollst  du  dann  giesscn  in  ein yd  ^afcifl.  I  Geföss  aus  Eisen  oder  Blei"  V,^.  14.
```


## [2026-09-14T02:29:45.264Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN p161 (leaf 182) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==183' HRN.txt | head -60",
 "description": "Print Horn page 161"
}
```


### [2026-09-14T02:29:46.298Z] TOOL RESULT

```
=== HRN p161 (leaf 182) ===
— 161 —
kurd. afj'. bei. (884) sar; oss. sär (220) ; wa/. sangl.
minj. sar.
121. se^'üT, sera *PaIast*.
Wohl zu aw. l/^i^rcl-, ^h'äyeinfi 'schützen , ai. yträ-^
trdyate; phlv. srWitan.
Hierher gehört wohl auch jüd.-pers. HNID 'Vorhof'
(Is. 62, 9), arm. LW. sr»/*, srahak^ arab. LW. surädiq
(de Lagarde, Pers. Stud. 72), aber nicht der lydische
Stadtnanie Sardes (vergl. 6. Meyer, Indog. Forsch.
I, 827).
Allgemein entlehnt.
728. sut% usmh Blei', "P)nD (Jer. 6, 29).
g. aurob.
aw. srn' 'Blei'; phlv. srpin 'bleiern'.
kurd. sirift (H.-Sch.); bei. surup, suruf (855).
729. serhär, sertvär 'Last, die man auf dorn Kopfe trägt .
aw. ^sara.hära- *Kopflast', vergl. sarnharn 'capitum
tegmina' (Isid. t&, 23).
Vergl. No. 726.
730. stir-^ Vot', Suhr[äbj Suhr]esp; vergl. sur/tce^ sur/tze
llöteln'.
ap. Ou/ra- (N. pr.) ; aw. sii^/ra- rot ; phlv. sii/r ;
ai. gukrä' 'klar, licht, hell'.
kurd. sör ; afy. sür ; oss. d. sur/, t. sir/ rot, schön'
(286) ; bei. suhr^ sohr Vot, glühend' (350) ; wa/. sökr.
731. serd 'kalt', sermä 'Kälte'.
g. sart,
aw. sareta- 'kalt'; phlv. sarty sarmäk (Bund.); skr.
vergl. gigira- 'Kälte'; arm. sarn 'Eis*, sahium., sarcim
'gefrieren, erfrieren' (H. No. 245) ; lit. szdlfas 'kalt'.
kurd. sür; afy. sör; oss. t. sald 'Kälte' (219); bei.
.sa/d, n. särf (336) ; wa;^. sür, süri.
np. sei'ma erklärt Nöldeke (mündliche Mitteilung)
überzeugend als Analogiebildung nach germä 'Wärme' ').
*j Lit. szarmä kann ihm also nicht gleichgeaetzt werdon
(Bezzonberger, Beitr. z. Gesch. der lit. Sprache, Ol).
II r II , (jiunUriüM tl. iioup. Ktyiuologpie. 11
```


## [2026-09-14T02:29:59.312Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nfor ln in (27427,27448,27481):\n    leaf='\\n'.join(lines[:ln]).count('\\f')\n    print('line',ln,'leaf',leaf)\nEOF\necho \"=== leaf around srva- ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==862' BRT.txt | grep -oE \"^\\s*1[0-9]{3}\\s*$\" | head\nawk 'BEGIN{RS=\"\\f\"} NR==862' BRT.txt | head -4\necho \"--- leaf 861/863 headers\"\nfor n in 859 860 861 862 863 864; do echo \"leaf $n:\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | grep -oE \"\\b1[5-7][0-9]{2}\\b\" | head -4; done",
 "description": "Locate Bartholomae column numbers for srva and srira"
}
```


### [2026-09-14T02:30:00.547Z] TOOL RESULT

```
line 27427 leaf 897
line 27448 leaf 897
line 27481 leaf 898
=== leaf around srva- ===
1578

1578
*'taÄi^^  Y.jö'.i;  —  ahurai  masdäi ..°t3m (statt  DS.)  vfnkrayne  fi-üdat^a^äi  Vr. i7. 1 ;  —  ttm  (näml.  mihtvm)  amixüanhm yazat)m  sBrim  damshu  °t>m  YtJO.  6;  13; —  sara  mihra..'ta  Yt  70.  31;  F./2; — tiÜrlm  ..yakmäi  ..fradä^at..lffs'firalsva °täi  YtÄ45;  43,  47;  — fravaslS . . spinta ..  spifüsth  ..  sürä  ..  'tu  Yt7j.75;  147, 31,  34;  —  vartuhi  °U  (VSf.)  andvl  süre ans/Ute  Yl.  5.  18,  130,  Ny.  /.  19;  Yt g,  4.  b)  sonst:  frataan  äps  */i  Yt. 13.  78.
KompE.  —  Superl.  zu  isüra-;  vgl.  Yt  r.  15, ro.  6,  31,  13.  75,  147.  —  ai-  iävif/ha-  Adj.  - Vgl,  säsfi/üta:  -Fi.:  sät  j^astSr»),  tri  (lu Yt.  /.  8] ;  dSmSa  räi  süt  J'Shtm ;  (lU  V.  33) : sültnänä,  erL:  sät  kunänd.  —  ')  NA,  sivtit'; s.  Var.  —  3)  Diese  Übersetzung  -  Sü. :  lä- bhepsuh,  läbkUihilifan  -  lässt  erkennen,  dass ntln  in  üf  nicht  das  Superlativsuffix,  sondern ein  Nomen  sah.  Der  Anlass  daiu  wird  Y, 55.  l :  *irvisiahc  . .  yt  rtä  iil5  gewesen  sein  : süf  J^ätl  ir  .  ,  ke  amäi  j^ästär  i  neTiiaiiA.
--- leaf 861/863 headers
leaf 859:
leaf 860:
leaf 861:
1577
leaf 862:
1578
leaf 863:
1579
1580
leaf 864:
```


## [2026-09-14T02:30:06.291Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 897 898 899 900; do echo \"=== awk leaf $n:\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | grep -oE \"\\b1[6][0-9]{2}\\b\" | head -4; done",
 "description": "Check Bartholomae column numbers near srva"
}
```


### [2026-09-14T02:30:07.369Z] TOOL RESULT

```
=== awk leaf 897:
1646
1616
1641
=== awk leaf 898:
1647
=== awk leaf 899:
1641
1650
=== awk leaf 900:
1651
1653
1652
```


## [2026-09-14T02:30:07.465Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 617 lead ===\"; awk 'BEGIN{RS=\"\\f\"} NR==641' SYN.txt | head -60",
 "description": "Print Buck SYN page 617"
}
```


### [2026-09-14T02:30:08.525Z] TOOL RESULT

```
=== SYN 617 lead ===
root connection? Pedersen 1.168.
2. Du., NHG kunst (> Dan. kunst, Sw. konst), orig. ‘knowledge, skill’, fr.
the root of NHG kennen ‘know’, kénn ‘know how, be able’. Kluge-G. 336, it
3. Lith. menas (cf. NSB S.V.), ori ‘understanding’ : minti, menu tt ; : remember’. Leskien, Ablaut 336, Neo. log. in this sense, influenced by NHG kunst, etc.
Lith. dailé, with dailininkas « dailus ‘beautiful’ (16.81).
Lett. maksla : mdcét ‘be able’ = Lith mokéti ‘be able’, beside Lith. mokyti, Lett. mécit ‘teach (17.25). MiihlRndy’ 2.579,
4, SCr. umjetnost, Boh. umént, orig. ‘understanding’, fr. umjeti, uméti ‘know how, be able’. Cf. ChSI. um, raz-umit ‘intelligence’ (17.12), razuméti ‘under- stand’ (17.16), etc.
Pol. sztuka ‘piece’ (fr. NHG stuck), also ‘work of art’ and ‘art? (sztuka malar- ska ‘art of painting’), for which also kunszt, directly fr. NHG kunst. Briick- ner 555 f.
Russ. iskussivo = late ChSI. iskust- stvo ‘trial’, fr. iskusiti ‘try’ (9.98). Berne- ker 653.
Russ. chudozestvo = late ChSI. chado- zistvo ‘art, science’, fr. *chqdogit, chudogit ‘wise’, loanword fr. a Gme. form *han- dags beside Goth. handugs ‘wise’ (17.21). Berneker 400. Stender-Petersen 334.
artist? :
9.42 ARTISAN, CRAFTSMAN
Grk. — rexvirys Goth. (-smipa) Lith. amatininkas
NG retry, éaropas ON — smidr, iénarmadr Lett. amatnieks
Lat.  faber, artifex Dan. haandvarker ChSl. chytrtct, ktznYnikit It. artigiano Sw. handlverkare SCr. zanatlija, obrinik a artisan OE wyrhla, creftiga Boh. emeslntk
ip. artesano , ME wright, craftiman Pol. —_rzemieslnik Rum. meslesugar, meseriag NE artisan, craftsman Russ. remeslennik, masler- Ir. sder, cerd Du. —handwerker, am- ovaj NIr. aor, ceard bachtsman Skt. gilpin-, karu- W. _saer, crefftwr OHG = wurhto, wercmeistar ’.\ oe Br. micherour MHG wercmerster, hant-
werker
NHG _handwerker
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
. tty of words for ‘artisan, he aioe serivs cpds., oF aes eaftso of those for ‘craft’, discusse a iets are mostly of similar se- ip Be rees, notions like ‘work, fit, past? E eaveril there is an early tend- kno - d specialization, chiefly to ep ‘metalworker’ (9.48, 9.60).
s. of words for
u ‘ a - Grk. rexvirns (cf. also réxrwv fearpenter” with wider sense 1n Hom. Ci
‘iano (> Fr. artisan in 1 ee Tormey ‘rataman’ A Sp. artesano, NE artisan; REW 619. Gamillscheg 52), Rum. mestegugar, meseriag; W. crefftwr, Br. micherour; OK creftiga, Dan. haandverker, Sw. handt- verkare, Du. handwerker, MHG hant- werker, NHG handwerker; Lith. amati- ninkas, Lett. amatnieks; ChSl. ktzninzki, SCr. zanatlija, obrinik, Boh. remesintk, Pol, rzemteslnik, Russ. remeslennik; Skt. gilpin-.
Cpds., the second part meaning ‘doer, maker’, ‘man’ or ‘master’ : Lat. artifex (cf. facere ‘do, make’); ON tonarmaor, ME craftiman, NE craftsman (earlier craftes man), Du. amb
```


## [2026-09-14T02:30:15.114Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"9\\.6[0-9] *LEAD\\|LEAD$\\|^9\\.6\" SYN.txt | head -20\necho \"=== search 'lead' metal section ===\"\ngrep -n \"plumbum\" SYN.txt | head -10",
 "description": "Find Buck LEAD section"
}
```


### [2026-09-14T02:30:16.166Z] TOOL RESULT

```
15289:9.61 FORGE (vb.)
15331:9.62 ANVIL
15352:9.63 CAST (Metals)
15373:9.64-9.69. Schrader, Sprachverglei- chung und Urgeschichte 2.10 ff., Real- lex. s.v. Metalle, Erz, Gold, etc. V. Bradke, Methode und Ergebnisse der arischen Altertumswissenschaft 28 ff. Hirt, Indogermanen 684 ff. Feist, Kul- tur, Ausbreitung und Herkunft der Indo- germanen 196 ff.
15402:9.65 SILVER Grk. — &pyupos Goth.  silubr Lith. sidabras NG done ON silfr Lett. sidrabs Lat. argentum Dan. sfif ChSl.  s(it)rebro It. argento Sw. silver SCr.  srebro Fr. argent OE siolfor, seolfor Boh. _ sifebro Sp. plata ME - sylver Pol. __srebro Rum. argint NE silver Russ. serebro Tr. argat, airged Du. —_zilver Skt. —_ rajata- Nir. airgead OHG - sil(a)bar Av. grazata-, OPers. W. arian MHG ssilber ardata- Br. arc’hant NHG silber
15426:9.66 COPPER, BRONZE
15466:r 9.68 LEAD an Goths isis Lith.  Svinas plumbum ON bly Lett. _svins Piombo Dan. bly ChSl. olovo plomb Sw. bly SCr. _olovo Plomo OE léad Boh. _olovo plumb ME ede Pol. oléw luaide NE lead Russ. svinec luaidhe Du. —_lood Skt. sisa- Plum OHG blio Av. srva- Ploum MHG bli NHG ble:
15481:9.69 TIN; TIN-PLATE
=== search 'lead' metal section ===
15466:r 9.68 LEAD an Goths isis Lith.  Svinas plumbum ON bly Lett. _svins Piombo Dan. bly ChSl. olovo plomb Sw. bly SCr. _olovo Plomo OE léad Boh. _olovo plumb ME ede Pol. oléw luaide NE lead Russ. svinec luaidhe Du. —_lood Skt. sisa- Plum OHG blio Av. srva- Ploum MHG bli NHG ble:
15472:2. Lat. plumbum (> Romance words, also W. plwm, Br. ploum), prob. a loan- word fr. the same source as the Grk. word. Ernout-M. 781.
15482:Grk. — xacalrepos Goth . Lith. cinas, alvas; skardis NG Kaddt; revexés ON lin Lett. alvs, alva; skards Lat. plumbum album Dan. tin; blik ChSl.  kostterit
17125:plumbum ‘lead’ through its nautical sense.
```


## [2026-09-14T02:30:21.499Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\ntxt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('leaf0', '\\n'.join(txt[:15466]).count('\\f'))\n\"\nfor n in 640 641 642 643; do echo \"leaf $n:\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' SYN.txt | grep -oE \"\\b6[0-9]{2}\\b\" | head -3; done\necho \"=== print leaf with 9.68 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==642' SYN.txt | sed -n '1,40p'",
 "description": "Find printed page for Buck 9.68 LEAD"
}
```


### [2026-09-14T02:30:22.900Z] TOOL RESULT

```
leaf0 669
leaf 640:
675
leaf 641:
653
619
leaf 642:
leaf 643:
=== print leaf with 9.68 ===
achtsman; OHG weremeistar, MHG wercmeister (lit. Work-master’); also NHG handwerks- man, Dan. haandverksman, Du. hand- werksman, and NHG handarbeiter.
2. eat Hacropas, Lacropns, used for -workman’ and one who is master
ag Ree it, Lat. magister » M. Meyer, N Cf. OHG meista » Neuer. Stud. 3.43.
ili 7 (in weremeistar, above 1 Luss, masterovoj, fr. the same source,
wISCELLANEOUS PHYSICAL ACTS, ETC.
Digitized by Arya Samaj Foundation Chennai and eGangotri
585
3. Lat. faber, general term for worker in hard materials, including metals, also used with descriptive adjectives to apply to particular crafts (cf. 9.48, 9.60), but in the majority of cases when standing alone ‘carpenter’, prob. fr. an orig. idea of ‘one who fits, makes fitting’ : Goth. gadaban ‘be fitting, happen’, OE gedéfe ‘fitting, proper’, gedafnian ‘be fitting’, ChSl. po-doba jest ‘is fitting’, dobrit ‘good’, etc., (here perh. also Arm. darbin ‘smith’, fr. *dhabhro-), IE *dhabh-. Walde-P. 1.824. Ernout-M. 319. Walde-H. 1.4386 f.
4. Ir. sder, NIr. saor, W. saer ‘crafts- man’ and esp. ‘carpenter’, fr. *sapero- : Lat. sapere ‘taste, perceive, know’, OHG intseffen ‘perceive’. Walde-P. 2.450. Pedersen 1.92.
Ir. cerd ‘craftsman’, also ‘smith, artist, poet’, NIr. ceard : Ir. cerd ‘craft? (9.41).
5. Goth. -smipa only in aiza-smipa ‘coppersmith’ and so uncertain whether still generic ‘craftsman’ or ‘smith’, ON smior ‘craftsman, woodworker or metal- worker’ (cf. gull-, jarn-, tré-smidr) : OE smih, OHG smid ‘smith’, etc. (9.60), fr. the root in Goth. gasmipon ‘effect’, ON smida ‘make, forge’, etc. (9.61).
OE wyrhia (cf. isern-, stan-, tréow- wyrhta), ME (with metathesis) wright, OHG wurhto, MHG (only in cpds.) -wiirhte, -worhte : OE weorc, OHG were, etc. ‘work’ (9.12).
6. ChSI. chytrici, deriv. of chytrt ‘skilled, crafty’ (cf. 9.41).
Russ. masterovoj, deriv. of ‘master, maker’ (9.41).
7. Skt. k@ru- ‘doer, maker’, but esp. craftsman’ : kr- ‘do, make’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
9.422 TOOL ‘ a adelov, Spyavor Gophie ys $i ani Lith.  inagis, irankis Tiegh ah lea ON | {al (pl.) Lott. ike Lat. instriimentum Dan. verkidj, redskab ChSI. (orqdtje) It. ordigno, utensili (pl.) Sw. verktyg, redskap SCr. orude, alat Fr. outil, instrument OE t6l Boh. ndiin, néslroj Sp. herramienta ME tole Pol. narzedzie Rum. unealtd NE tool Russ. orudie Ir. airnisi (pl.) Du. werktuig. Skt... karana- NIr. — wirlis, oirnéis, acra OHG  giztuc ‘ Av. WwW. arf MHG ztuc, wercziuc Br. benveg NHG_~ werkzeug
Many of the words listed have a wider range than NE Zool in its usual applica- ‘tion and may cover any ‘instrument, im- plement’.
1. Grk. épyadefov, deriv. (perh. through *épya-dov, cf. épya-rns, Epya-v7) of épyor ‘work’ (9.12).
Grk. dpyavov : épyov ‘work’.
2. Lat. instriimentum (> It.. stru- mento, F'r., NE, NHG, Pol. Russ. instru- ment), deriv. of instruere ‘provide, equip’, orig. ‘set in order’, cpd. of struere, ‘arrange, prepare’, fr. the same root as Lat. sternere ‘spread out’, etc. (9.34). Ernout-M. 989 f.
It. ordigno, fr. VLat. *ordinium, deriv. of Lat. or
```


## [2026-09-14T02:30:28.663Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15455,15480p' SYN.txt | cut -c1-400",
 "description": "Print Buck lines around 9.68 LEAD"
}
```


### [2026-09-14T02:30:28.854Z] TOOL RESULT

```
Ir. iarn, NIr. tarann, W. haearn, Br. houarn, fr. a Celt. *tsarnon (cf. Gall. Isarnus, etc.), whence the Gmc. group, Goth. eisarn, ON zsarn (the more com- mon ON jarn by later borrowing fr. Ir. iarn), OB isern, tsen, OF, ME iren, NE iron, OHG isarn, isan, NHG eisen, etc. The Celt. *tsarnon perh. itself of Illyrian origin (there is a similar Illyr. river hame, and the Hallstatt iron finds are
earlier than the Celtic) and : Skt. isira- strong’,
origin
Digitized by Arya Samaj Foundation Chennai and eGangotri
MISCELLANEOUS PHYSICAL ACTS, ETC. 613 . 9.67 IRON Goth. eisarn Lith. gelezis gldnpos ON isarn, jarn Lett. dzelzs [€p0 Dan. jarn Chl. Zeléso F ferrum Dan. jam SCr. Zeljezo, guozde ferro OE isern, isen, tren Boh.  Zelezo fer ME iren Pol. zalazo hierro NE tron Russ. Zelezo | fer Du. zzer Skt. ayas- jarn OHG  isarn, isan Av. ayah- garann MHG_ isern, isen ‘aan NHG eisen ou n is comparatively late 
neut., prob. a loanword, but source un- known. Schrader, Reallex. 1.239.
3. Lat. ferrum (> Romance words), orig. dub., loanword fr. Semitic (?). Schrader, Reallex. 1.240. Ernout-M. 352. Walde-H. 1.486.
4, Lith. gelezis, Lett. dzelzs, OPruss. gelso, ChSl. Zeléso, general Balto-Slavic word, perh. with Grk. xadxés ‘copper, bronze’ as loanwords fr. some common source. Walde-P. 1.629. Schrader, Reallex. 1.236.
SCr. also guozde, deriv. of old gvozd ‘nail’ (9.51), hence orig. ‘nail material’. Berneker 366.
5. Skt. ayas-, Av. ayah-: Lat. aes, etc. See 9.66.
Skt. ¢ydma- ‘black’ is used with ayas- or alone for ‘iron’. Macdonell-Keith 1.31 f.
r 9.68 LEAD an Goths isis Lith.  Svinas plumbum ON bly Lett. _svins Piombo Dan. bly ChSl. olovo plomb Sw. bly SCr. _olovo Plomo OE léad Boh. _olovo plumb ME ede Pol. oléw luaide NE lead Russ. svinec luaidhe Du. —_lood Skt. sisa- Plum OHG blio Av. srva- Ploum MHG bli NHG ble:
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
614
Lead dates from the bronze age in the eastern Mediterranean region and pos- sibly in Britain, but in most of Europe it is contemporaneous with iron. Among the words for ‘lead’ there is a group com- mon to Celtic and Gmc., resting on bor- rowing, and probably the Greek and Latin words are from a common, un- known source. There is some confusion between ‘lead’ and ‘tin’. Schrader, Real- 
1. Grk. pédvBd0s (with variants pd6d.- Bos, Bddtpos, BodBos), NG pordbBr (also BoXtur), doubtless a loanword, but source unknown. Boisacq 644.
2. Lat. plumbum (> Romance words, also W. plwm, Br. ploum), prob. a loan- word fr. the same source as the Grk. word. Ernout-M. 781.
3. Ir. luaide, NIr. luaidhe; OE léad, ME lede, NE lead, Du. lood (MHG lat, NHG lot ‘lead’ as ‘solder’ or ‘plummet’; so also Dan., Sw. lod, fr. MLG). The Gme. words are prob. borrowed from Celtic, and the latter perh. deriv. of IE
SELECTED INDO-EUROPEAN SYNONYMS
*pleu- in words for ‘flow, float’, ete applied to the quickly melting lead, Walde-P. 2.442. Franck-y. W. 3961, 4. ON bly, Dan., Sw. bh OHG 5) bi (gen. bliwes), MHG bi, NHG yi pointing to a Gmc. *bliwa-, perh. : Lith,
blyvas ‘violet colored’, etc. Walde-p 2.210. Falk-Torp 86. 5. Lith. Svinas, Lett. svins, Russ
svinec, etym. dub. Persson, Beitriige 745 Buga, Kalba ir Senové 262,
OPruss. alwis ‘lead’, Lith. alvas ‘tin’ Lett. alvs, alva ‘tin’, ChSl., SCr., Boh; olovo, Pol. oféw all ‘lead’, but Russ. olovo ‘tin’, orig. a color word (with charac- teristic -wo-suffix) with application to either ‘lead’ or ‘tin’ and subsequent varying distribution in this respect, But root connection dub. (OHG elo ‘yellow’, etc.?). Walde-P. 1.159, 2,449,
6. Skt. stsa- neut. (AV-+, cf. Mac- donell-Keith 2.452), etym.?
Av. srva- neut. (Barth. 1649), NPers, surb, etym.?
```


## [2026-09-14T02:30:37.057Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"MISCELLANEOUS PHYSICAL ACTS, ETC. 617\\|^617$\\| 617 \\|617 9\\.\" SYN.txt | head -10",
 "description": "Locate Buck printed page 617"
}
```


### [2026-09-14T02:30:38.095Z] TOOL RESULT

```
15568:617
33464:Lat. minister, deriv. of minor, minus ‘less, smaller’ (on the model of magister : magis). Ernout-M. 617 f.
```


## [2026-09-14T02:30:38.885Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS srub / lead ===\"; grep -n -i \"srub\\|srwb\\|sruw\\|lead\" SNS.txt | head -20\necho \"=== PHD srub ===\"; grep -n -i \"srub\\|lead\\b\" PHD.txt | head -20",
 "description": "Grep SNS and PHD for srub/lead"
}
```


### [2026-09-14T02:30:38.954Z] TOOL RESULT

```
=== SNS srub / lead ===
11169:^oi*» •*£» ( srub + en: 
31447:srubSn 183/7-184/6 
=== PHD srub ===
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
188:~ih : immortality. ahr Phl] dread, fury. ahrüftan, ahram- P4Pftn', *hm- | M hr’ рїп, ? hr? m-] raise, lead up. Ahreman ['Al(y)mn! | М ?hrmyn, N ~] the Evil Spirit. >
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
876:astray wiyābān; lead ~ wiyābānēn- īdan.
2577:lead (n.) arziz, srub.
2578:lead (v.) anidan, franāftan, haxtan, nidan, rāyēnīdan, zaménidan, adēn-; ~ up ahrāftan.
2579:leaden arzīzēn, srubēn.
4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
```


## [2026-09-14T02:30:50.747Z] TOOL CALL #25: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T02:30:50.753Z] TOOL RESULT

```


```


## [2026-09-14T02:30:52.689Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 570-576 search سرب ===\"\ngrep -n \"سرب\" BQT_v2_pages.txt | head -20",
 "description": "Grep Borhan vol2 for سرب"
}
```


### [2026-09-14T02:30:52.757Z] TOOL RESULT

```
=== BQT v2 leaf 570-576 search سرب ===
1708:                           ‫نكند‬    ‫خسرب‬
1794:  ‫سربا‪ .‬وهزی اليك بجذم النخلة تساقط عليكرطبا جنیا‪ .‬فکلی‌واشربی وقریعیناً «سورة ‪(۱٩‬مریم)‏‬
1949:       ‫وزن سربسته » ربسمان خامی باشد که در وقت‬                          ‫و کج باشد ‪ -‬و چوب‌بندی‌تا انگور ‪ ۴‬وسقف‬
2277: ‫و گیاهی‌بود سربپن که احزاه ی‌نمباك ودءوارهای‬               ‫‪۳‬اول و ضم اور مم‬                         ‫چوبن باشد؛‬
2674:‫تلمشهرست ‪ ۴‬که مردم آنجا اکثر خوش طبع و سربالی نام دوایی است که آنرا بفارسی اوشه‬
2683:                                                     ‫کنجد » بسربانی کل را کویند که بعربی ورد‬
2912: ‫‪ ۷81.‬شننی ز‪ ۰ 2۷4‬سربکلی [‪ ( 8۵۷[ ۰ 8۷2۷‬آرد )‬
3323: ‫وبهندی *‪٩‬علتی‏ است کهآ نراسربی‌فالخوانند‬       ‫مر‪-‬وف است که بافند‪.‬‬
3917:                        ‫چار چ‬                                   ‫بعربی سربرخوانند ‪ -‬کونایه از تابوت همهت‬
4124:‫ازروی ناز و قکبر وءجب کنند ‪ -‬وبمعنی‌جنگه‬                   ‫است از ولابت قزوین کهسربلوك رامند است ‪-‬‬
4832:   ‫‏‪ - ٩‬کلم فارسی‌است که در آرامی و سربانی ویزعربی (سراح) وارد شده ( قرآن»سورءة‬
5532:      ‫سرب‬                                                                                       ‫‪۳۳‬‬
6367:                                ‫وآهنگران راء وسربی‬        ‫که او راکاروانك نیز کوبند» وبمربی‌مة کر او را‬
7058: ‫که نجاستها و پلیدیپا را پاك کند واو را سربی‬
7392: ‫زوبین؛ روپاکی باشد سرخ ردکه که برسربندندد‬                                             ‫جداکتند ‪. ۴‬‬
8087:‫خی‌اسالی‬   ‫تر‬     ‫حبق خراسانی ‪-‬‬                        ‫سربانی داروبی است کهآ نرا حندقرقی کوندا »‬
9036:        ‫که اقلم کلتان را بات خار کن دارد‪.‬‬           ‫‪ - ۸‬برون کن ازبخور هی زمغزسربخار وی‬
9397: ‫خالوما = بامیم بالف کشیده ؛سربالی‬                          ‫وعلم را گدوزبند بفتح هین ‪ -‬و بمعنی ابرام‬
9476:                                                                     ‫نبز گوید که سربراه نشده باشد ‪.‬‬
9777:  ‫بنام « چندراسرا ب»اد شده بمعنی (چشمه ماه)‪ .‬درنخهة سربانی کلله که از بهاوی ترجمه شده‬
```


## [2026-09-14T02:30:58.974Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%BA%D8%A7%D9%84",
 "prompt": "Give the full etymology section for the Persian word شغال (šoğâl) 'jackal': what it derives from (Sanskrit śṛgāla, Middle Persian form?), and any borrowings into Turkish/English."
}
```


## [2026-09-14T02:30:59.898Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/jackal",
 "prompt": "Give the full etymology of 'jackal' — the route through Turkish, Persian, Sanskrit, and dates."
}
```


### [2026-09-14T02:31:05.118Z] TOOL RESULT

```
# Etymology of Jackal

The word "jackal" entered English around 1600 and traveled through multiple languages before reaching its current form.

**Language Journey:**
The English term derives from French *chacal* (earlier *jackal*), which came from Turkish *çakal*. The Turkish word originated from Persian *shaghal*, which connects to Sanskrit *srgala-s*, meaning "the howler."

**Original Meaning:**
The Sanskrit root literally translates to "the howler," reflecting the animal's distinctive vocalizations. Over time, the word acquired a figurative sense: "skulking henchman," based on the historical belief that jackals would "stir up game for lions."

**Timeline:**
- **c. 1600**: Word appears in English from French sources
- Earlier stages: Turkish → Persian → Sanskrit origins

This etymological path illustrates how the word traveled westward from South Asia through the Middle East and into European languages during the early modern period.
```


### [2026-09-14T02:31:07.286Z] TOOL RESULT

```
# Persian Etymology of شغال (šoġâl) - Jackal

## Direct Lineage

The Persian word derives from **Middle Persian šγal (/šaγāl/)**, which was borrowed from **Sanskrit sṛgālá** (meaning "jackal"). The Sanskrit term traces back to **Proto-Indo-Aryan *śr̥gālás**, ultimately originating from **Proto-Indo-Iranian *ćárguš**.

## Source Documentation

According to the entry: "from [Middle Persian] (šγal /šaγāl/), borrowed from [Sanskrit] (sṛgālá), from [Proto-Indo-Aryan] (*śr̥gālás), from [Proto-Indo-Iranian] (*ćárguš)."

The word may derive from Proto-Indo-European roots or possibly the BMAC substrate.

## Transmission to European Languages

The Persian form subsequently spread through **Ottoman Turkish as چقال (çakal)**, which then dispersed to multiple languages:

- **Turkish**: çakal
- **English**: jackal (via French chacal)
- **Greek**: τσακάλι (tsakáli)
- **French**: chacal
- **Bulgarian**, **Romanian**, **Serbo-Croatian**, and numerous other European languages

This represents a comprehensive linguistic journey from South Asian Sanskrit through Persian and Ottoman intermediaries into modern European vocabulary.
```


## [2026-09-14T02:31:13.248Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%B1",
 "prompt": "For the Persian entry سیر: give the etymologies of all the homonyms, especially سیر (sir) meaning 'satiated, full' — what Middle Persian / Proto-Iranian / PIE forms are given? Also سیر 'garlic' and 'travel'."
}
```


## [2026-09-14T02:31:14.188Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D9%87",
 "prompt": "For the Persian entry اره (arre) 'saw': give the full etymology — Middle Persian form, Proto-Iranian, PIE root, and any cognates listed."
}
```


### [2026-09-14T02:31:20.064Z] TOOL RESULT

```
# Etymology of Persian اره (arre) 'saw'

Based on the Wiktionary entry, here's the etymological chain:

**Proto-Indo-European origin:** The word derives from PIE *\*sers-* meaning "to cut off."

**Cognates listed:**
- Latin *serra* ("saw"), which entered English as "serra"
- Mazanderani *هره* (hare, "saw")
- Baluchi *ہرگ* (harrag, "saw")
- Northern Luri *ݖڔںە* (əǝṛə)

The entry does not provide an explicit Middle Persian or Proto-Iranian intermediate form, jumping directly from the PIE root to the Persian term. However, the shared cognates across Iranian and non-Iranian languages suggest the word was inherited through Proto-Iranian from the ancient Indo-European root meaning "to cut."
```


### [2026-09-14T02:31:20.993Z] TOOL RESULT

```
# Persian سیر Etymologies

## سیر (sēr/sir) - "Full, Satiated"

**Etymology 1** traces this adjective to cognates with Northern Kurdish _têr_. The entry notes it's related to earlier language forms but provides limited reconstruction details beyond indicating Proto-Indo-European origins.

## سیر (sīr/sir) - "Garlic"

**Etymology 2** states the word is "Inherited from Proto-Indo-European" and possibly reflects Middle Persian or an Aramaic heterogram. The text suggests a connection to an Old Persian form *θigraʰ, potentially reflected in the month name Θāigraciš, meaning "the month of garlic-collecting." An alternative theory links it to Proto-Turkic _*sarmïsak_ borrowed from Iranian languages.

## سیر (sayr/seyr) - "Travel, Movement"

**Etymology 3** indicates this noun was "Borrowed from Arabic _سَيْر_ (sayr)." This represents a direct loanword from Arabic rather than inherited forms.

The entry notably lacks detailed Proto-Iranian reconstructions for the first two senses, offering mainly comparative language evidence rather than comprehensive etymological chains.
```


## [2026-09-14T02:31:26.493Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb && curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B3%DB%8C%D8%B1&action=raw\" | sed -n '1,120p'",
 "description": "Fetch raw wikitext for Persian سیر"
}
```


### [2026-09-14T02:31:27.964Z] TOOL RESULT

```
{{also|شیر|سير|ـسز}}

==Central Kurdish==

===Noun===
{{ckb-noun|tr=sîr}}

# [[garlic]]

==Khowar==

===Etymology===
From {{inh|khw|sa|सेतु|tr=sétu|t=bridge}}, from {{inh|khw|iir-pro|*sHáytuš}}.

===Noun===
{{head|khw|noun|tr=ser}}

# [[bridge]]

===References===
* {{R:khw:Bashir}}

==Ottoman Turkish==

===Etymology 1===
{{root|ota|ar|س ي ر}}
{{bor+|ota|ar|سَيْر}}.

====Noun====
{{head|ota|noun|tr=seyr}}

# [[motion]]
# [[show]], [[spectacle]]

=====Derived terms=====
{{col|ota|سیر یری<tr:seyr yeri>|سیرجی<tr:seyrci>}}

=====Descendants=====
* {{desc|tr|seyir}}

===Etymology 2===
{{ety|ota|id=garlic}}
{{bor+|ota|fa|سیر|tr=sir|t=garlic}}.

====Noun====
{{head|ota|noun|tr=sir}}

# [[garlic]]

=====Descendants=====
* {{desc|tr|sir|sirmo}} {{q|dialectal}}

===Etymology 3===
{{bor+|ota|fa|سیر|tr=sir|t=satiated}}.

====Adjective====
{{head|ota|adjective|tr=sir}}

# [[full]], [[satiated]]

===References===
* {{R:ota:RedhouseWells1880|سیر|page=607b}}

==Persian==

===Etymology 1===
Cognate with {{cog|kmr|têr}}.

====Pronunciation====
{{fa-IPA|sēr}}

====Adjective====
{{fa-regional|سیر|سیر|сер}}
{{fa-adj|cls=سیر}}

# {{senseid|fa|satiated}} [[full]], [[satiated]]
#: {{ant|fa|گرسنه<tr:gorosne>}}
# [[sated]], [[fed up]]
# {{lb|fa|of colors}} [[dark]]
#: {{syn|fa|تیره<tr:tire>}}
#: {{ant|fa|روشن<tr:rowšan>}}
#: {{uxa|fa|قرمز '''سیر'''|tr=qermez-e '''sir'''|t='''dark''' red}}

===Etymology 2===
Inherited from {{inh|fa|ine-pro|-}}; in {{inh|fa|pal|tr=syl|sc=Phlv}} or [[Aramaic]] [[heterogram]] {{l|pal|tr=TWMʾ}}; often claimed to come from an {{inh|fa|peo||*θigraʰ}}, only imagined to be reflected in the {{w|Iranian calendar|month name}} {{inh|fa|peo|𐎰𐎠𐎡𐎥𐎼𐎨𐎡𐏁|tr=Θāigraciš|lit=*the month of garlic-collecting}}, while another suggestion sees the full term rather reflected by {{cog|trk-pro|*sarïmsak|*sarmïsak|t=garlic}} borrowed from {{cog|ira|-}}.

====Pronunciation====
{{fa-IPA|sīr}}

====Noun====
{{fa-regional|سیر|سیر|сир}}
{{fa-noun|cls=سِیر}}

# {{senseid|fa|garlic}} [[garlic]]

=====Descendants=====
* {{desctree|ota|سیر|tr=sir|bor=1|id=garlic}}
* {{desctree|rom|sir|bor=1}}

====See also====
{{list:Haft Sin/fa}}

===Etymology 3===
{{ety|fa|:bor|ar:سَيْر|text=+|tree=1}}

====Pronunciation====
{{fa-IPA|sayr}}

====Noun====
{{fa-noun|cls=سَیر}}

# act of [[go]]ing; [[movement]]
# [[excursion]], [[trip]]
#* {{RQ:fa:Selim Divan|83
|داشتیم وقت سحر در '''سیر''' گلشن گریه‌ای<br>کز غمم خواند این غزل مرغی بدرد افغان کنان
|دَاشْتیم وَقْتِ سَحَر دَر '''سَیرِ''' گُلْشَن گِرْیَئی<br>ک-اَز غَمَم خْوَانْد اِین غَزَل مُرْغی بَ-دَرْدِ اَفْغَان کُنَان
|I wept a little at the time of dawn during my '''outing''' to the rose garden,<br>For out of my grief, a bird sang this love poem with a pain that makes one cry out.
}}

===Further reading===
```


## [2026-09-14T02:31:28.439Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb && curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%A7%D8%B1%D9%87&action=raw\" | sed -n '1,80p'; echo \"=== srva\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B3%D8%B1%D8%A8&action=raw\" | sed -n '1,120p'",
 "description": "Fetch raw wikitext for اره and سرب"
}
```


### [2026-09-14T02:31:30.470Z] TOOL RESULT

```
{{also|آره}}
==Mazanderani==

===Pronunciation===
* {{IPA|mzn|[ˈæːɾɛ]}}

===Particle===
{{head|mzn|particle|tr=are}}

# [[yes]]

==Ottoman Turkish==

===Etymology===
{{bor+|ota|fa|اره|tr=arre|t=saw}}.

===Noun===
{{ota-noun|tr=erre}}

# [[saw]], a [[tool]] with a toothed [[blade]] used for cutting [[hard]] [[substance]]s
#: {{syn|ota|بچقی|tr1=bıçkı|منشار|tr2=minşar}}

====Descendants====
* {{desc|tr|erre}}

===Further reading===
* {{R:tr:OTK|erre2|vol=1|page=1474}}
* {{R:ota:Kelekian|page=70}}
* {{R:ota:Meninski|C|column=1547|Serra}}
* {{R:ota:Meninski|T|column=152}}
* {{R:ota:Redhouse|page=75}}

{{C|ota|Tools}}

==Persian==

===Etymology===
From {{der|fa|ine-pro|*sers-||to cut off}}. Compare {{cog|la|serra|t=saw}} (whence {{cog|en|serra}}), {{cog|mzn|هره|tr=hare|t=saw}}, and {{cog|bal|ہرگ|tr=harrag|t=saw}}, {{cog|lrc|ݖڔںە|tr=əǝṛə}}.

===Pronunciation===
{{fa-IPA|ar`ra}}

===Noun===
{{fa-regional|اره|اره|арра}}
{{fa-noun|tr=arre}}

# [[saw]]
#: {{syn|fa|منشار<tr:menšâr>|یوسه<tr:yuse>}}
#* {{quote-book|fa|title=fa:دیوان انوری|trans-title=Dīvān of Anvarī|year=c. 1180|chapter=Qaṣīda 72|author={{w|Anvari|Anwarī}}|url=https://ganjoor.net/anvari/divan-anvari/ghaside-anvari/sh72
|text=درخت اگر متحرک شدی ز جای به جای<br>نه جور '''اره''' کشیدی و نه جفای تبر
|tr=diraxt agar mutaharrik šudē zi jāy ba jāy<br>na jawr-i '''arra''' kašīdē u na jafā-yi tabar
|t=If trees could move about from place to place,<br>They would suffer neither the oppression of the '''saw''' nor the torment of the axe.
|footer=(Classical Persian transliteration)}}

====Descendants====
* {{desc|chg|اره|bor=1|ts=ärrä}}
** {{desc|ug|ھەرە}}
** {{desc|uz|arra}}
* {{desc|kk|ара|bor=1}}
* {{desc|klj|harra|bor=1}}

===References===
* {{R:fa:Steingass}}
* {{R:fa:Nourai|page=443}}

{{C|fa|Tools}}=== srva
{{also|شرب|سرت|سرپ|شرت}}
==Arabic==
{{ar-rootbox|س ر ب}}

===Verb===
{{ar-verb|I/i~a.ipass.vn:سَرَب.ap:+++}}

# {{lb|ar|intransitive}} to [[leak]], to [[seep]], to [[ooze]] {{+obj|ar|:مِن<from something>}}

====Conjugation====
{{ar-conj|I/i~a.ipass.vn:سَرَب.ap:+++}}

===Verb===
{{ar-verb|II}}

# {{lb|ar|transitive}} to [[leak]], to [[let]] through

====Conjugation====
{{ar-conj|II}}

===Noun===
{{ar-noun|سَرَب|m|pl=أَسْرَاب}}

# {{ar-verbal noun of|سَرِبَ|form=I}}
# [[burrow]], [[den]], [[lair]]
# [[offlet]], [[offtake]], air [[return]], [[flue]]

====Declension====
{{ar-decl-noun|سَرَب|m|pl=أَسْرَاب}}

===Noun===
{{ar-noun|سِرْب|m|pl=أَسْرَاب}}

# [[flock]] (of birds etc.)

====Declension====
{{ar-decl-noun|سِرْب|pl=أَسْرَاب}}

==Persian==
{{chemical element box|fa}}
{{wp|fa:}}

===Alternative forms===
* {{alt|fa|اسرب|tr=osrob|اسرف|tr2=osrof||archaic}}

===Etymology===
From {{inh|fa|pal|sc=Phlv|tr=slwp|ts=srub|t=lead}}. Cognate with {{cog|sla-pro|*sьrebro}}.

===Pronunciation===
{{fa-IPA|surb}}

===Noun===
{{fa-noun|tr=sorb}}

# [[lead]] (chemical element)

{{C|fa|Chemical elements|Metals}}
```


## [2026-09-14T02:31:44.969Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK full: srira ===\"; grep -n -i \"srīra\\|srira\" POK_full.txt | head -20\necho \"=== POK full page 618 ===\"; grep -n \"Page(s): 618\\|Page(s): 617-618\\|Page(s): 618-619\" POK_full.txt | head",
 "description": "Grep Pokorny for srira and page 618"
}
```


### [2026-09-14T02:31:45.042Z] TOOL RESULT

```
=== POK full: srira ===
=== POK full page 618 ===
48258:Page(s): 617-618 
48339:Page(s): 618-619
```


## [2026-09-14T02:31:47.341Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK full: serra ===\"; grep -n -i \"serra\" POK_full.txt | head -20\necho \"=== POK full: srva / Blei ===\"; grep -n -i \"'Blei'\\|srva-\" POK_full.txt | head -10\necho \"=== AHD watkins: serra / ser- ===\"; grep -n -i \"serra\\|serrate\" AHD_watkins1985.txt | head -20",
 "description": "Grep Pokorny and Watkins for serra"
}
```


### [2026-09-14T02:31:47.431Z] TOOL RESULT

```
=== POK full: serra ===
50548:Material: For palatales /^speaks aapaai apa^ai Hes., as Latin sarracum, serracum{\\.a\\aw 
74047:with -p- Lithuanian serpes PI. 'ein gelbes Farberkraut, Serratula tinctoria', sirpstu, 
82225:alb. shterpe' infertile ' (compare also 6. ster-' infertile '); Irish serrach' plenitude' (from 
=== POK full: srva / Blei ===
50604:from the ^-basis Avestan sru-, srva-' horn; nail in fingers and toes ', srvara ^horned ' 
=== AHD watkins: serra / ser- ===
```


## [2026-09-14T02:31:54.388Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '48230,48270p' POK_full.txt | cut -c1-300\necho \"=== 618-619 ===\"\nsed -n '48320,48345p' POK_full.txt | cut -c1-300",
 "description": "Print Pokorny roots at page 617-619"
}
```


### [2026-09-14T02:31:54.502Z] TOOL RESULT

```
kru- 

Meaning: to heap up, put together; heap; roof, cottage, shed. 

Material: Gothic hrotu. 'roof. Old Norse hrot'rooi, attic ', Old Saxon Old English hrost' 

Sparrenwerk des Daches ' {*krdd-s-to-) = Dutch roest^ perch, chicken roost, chicken 

ladder'. Middle High German raz, raze^pyre, stake' {*kreda; fem. collective as Old Church 

Slavic krada); with Middle High German raz(e)^pyre, stake' corresponds to Middle High 

German raz, raze 'honeycomb', afr. rata, mnl. /"a/e 'honeycomb', next to which with ablaut 

mnl. rete {*hretdn-) and rote. Dialectal still rote {* hruti-) 'honeycomb'; 

Old Bulgarian krada^pyre, stake, woodpile ' {*krdda). 

/n^^paTOnwen<^u^rateruJS\A^Gezi^^ Lithuanian 

Ares/as 'stately stool', Latvian kr^sls. Old Prussian CAes/a/? 'armchair', Lithuanian krase 
'stool', russ. kreslo, Czech /r/fes/o 'armchair', as well as Lithuanian krosnis, Latvian krasns 
"oven'. Church Slavic krosno^ a weaver's beam ', russ. krosno ^\oorw, piece of canvas, 
fabric', Bulgarian krosno^ Aufzug beim Webstuhl; Torriegel ', krosnai. ' cradle ', Serbo- 
Croatian krosna ^\oorw\ Czech krosna, krusna{o\6 krosna) 'pannier, basket for carrying 
food or supplies'. 

References: WP. I 485 f., Trautmann 141. 
Page(s): 617-618 

Root / lemma: kreg-1 (and kerg-1) 



Meaning: to suffer 

Material: Old Indie karjat/" affWcts, torments' (Dhatup.); 

Old Icelandic ^AeA/a "torment, smite, bother, annoy, pursue ', Old Frisian hreka' rend '. 

References: WP. I 484. 
=== 618-619 ===

KpoKP) " EinscmagTaaen^eweDe ', Kpo^ ds., KpoKouv "to weave', KpoKU(;, -u5o(; f. "flock, 
tuft of wool'; 

Old Icelandic hrgell{ *hrarjhila2) "a weaver's reed ', Old English hreol{ *hrehula^ " 
windlass, reel '; Old English hraeglu. "dress, garment ', engl. rail. Old Frisian hreil. Old 
High German hregilu. " a garment, the skin, hide, fell '; 

Latvian kr^kls " shirt '; 

if the Latvian word has received a second Arthrough West Indo Germanic influence, it 
can also be followed by the Slavic family: russ. kresu, kresatb b " mit dem Feuerstahl 
Feuer schlagen ', kir. kresaty, kresnufyl\re hit', dial, "hew, hit, strike ', Serbo-Croatian 
kresem, kresat/l'\re hit; scabble, cut or chisel stone roughly; branch cut off the branch ' 
(etc., s. Berneker611). 

Maybe alb. kr/smen. "strike, shot ' a Slavic loanword. 

References: WP. I 483 f. 
Page(s): 618-619 

Root / lemma: krek-2, kfk- 

Meaning: roe; slimy stuff in water 

Material: Old Icelandic hrognu.. Old High German (h)rogan, rogen^ spawn, fish eggs,
```


## [2026-09-14T02:32:07.674Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"sraesta\\|sraeta\\|srayah\\|sri-ra\\|s'ri\" POK_full.txt | head -10\necho \"=== POK01/02 search ===\"\ngrep -n \"srīra\\|srira\" POK_0*.txt | head -10\necho \"=== what is on POK printed 618 (POK_02 leaf 618-344=274) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==275' POK_02.txt | head -20",
 "description": "Search Pokorny for Avestan srira"
}
```


### [2026-09-14T02:32:08.884Z] TOOL RESULT

```
51898:srayah-, Superl. Old Indie srestha- {srai'stha-), Avestan sraesta-. Old Indie sreman-m. " 
=== POK01/02 search ===
=== what is on POK printed 618 (POK_02 leaf 618-344=274) ===
inschiene*;
air.  cnäim  ,Bein,  Knochen*  (ob  gr.  kelt.  -nä-  =  idg.  n,  d.  i.  -eW9-,  oder =  idg.  -wä-,  d.  i.  Vollstufe  der  2.  Silbe  sei,  ist  unentschieden) ;
614  f
mit  Vollstufe    der    1.  Silbe   (kon[d]mä)   und   Assim.   von    -nm-  zu   -mm.**' (daraus  z.  T.  -m-) :  .L.
ahd.   hamma  , Hinterschenkel,  Kniekehle^  ags.  hamm  ,Kniekehle',  aisl hgm  f.  , Schenkel  (an  Tieren)'.
Unsicher  ist,  ob  die  Bed.  von  hom.  yf,v7]ixög  , Bergwald,  bewachsener Berghang*  (,*Wade  des  Berges'?)  durch  ndd.  hamm  ,Bergwald'  als  alt erwiesen  wird,  da  letzteres  vielleicht  als  umzäuntes  Waldstück  mit  mnd harn  ,eingefriedetes  Stück  Land',  ndd.  hamme  ,umzäuntes  Feld'  (s.  Äem- ,zusammendrücken')  zu  verbinden  ist.
WP.  I460f.
konk-  ,in  Zweifel  sein,  schwanken,  in  Sorge,  Angst  sein^
Ai.  sdjdkate  ,schwankt,  zweifelt,  ist  besorgt,  fürchtet',  sardkita-  ,besorgt ängstlich  vor',  §a7dkä  »Besorgnis,  Furcht,  Verdacht,  Zweifel' ;
lat.  cünctovy  -an  ,zaudernd,  zögern'  (*concitor  Frequentativ,  vgl.  ai. saTdkita-) ;
anord.  hcetta  ,riskieren'  (*hanhatjan),  hcetta  , Gefahr',  Jiäski  ds.  (*Aan- h{a)skan-).
Über  ahd.  hähan  , hängen'  usw.  s.  S.  566  unter  kenk-  ,schwanken'.
WP.  I  461.
konkbo-  ,Muschel'?
Ai.  SaTdkhd-  m.  ,Muschel,  Schläfe';
gr.  y.6yxog,  xd/x^  ,Muschel,  Hohlmaß';  v,öx^og,  Y,o%Viag  ,Muschel,  Schnecken- haus, Schnecke',  vielleicht  aus  *xo/xA-;
lat.  congius  ,Hohlmaß  für  Flüssigkeiten'  ist  höchstwahrscheinlich  gr.  Lw. ; unsicher  lett.  sence  ,Muschel',  da  zence  die  richtigere  Form  scheint. WP.  I  461  f.,  WH.  I  260,  J.  B.  Hofmann  Gr.  etym.  Wb.  151.
kop{h)elo-s  oder  kap(h)elo-s  ,Karpfenart'.
Ai.  saphara-  m.  ,Cyprinus    sophore'  =  lit.  säpalas   ,C7prinus    dobula'. gr.  TiVftQLvog   , Karpfen',   vielleicht    nach    xsarQivog,    Kogayuvcg,    igv-d^Qivog usw.  umgebildet;  v-  eventuell  volksetymologisch  nach  KvTTQog,  da  *y.07tQlvog an  ytÖTtQog  denken  ließe.
WP.  I  457,  WH.  I  171,  Trautmann  299.
```


## [2026-09-14T02:32:10.183Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY: اره ===\"; grep -n \"اره\\b\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== ARY latin index serra/saw ===\"; grep -n -i \"SERRA\\|SAW\\b\\|JACKAL\\|LEAD\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur for arre, serra, jackal, lead"
}
```


### [2026-09-14T02:32:10.259Z] TOOL RESULT

```
=== ARY: اره ===
78:می‌شد ولی امروزه این نام بشتر برای اشاره به زبانهای بخش شمالی شبه قاره‌ی هند و به صورتث
82:تنها در اشاره به یک خانواده‌ی بزرگك زبانها بلکه در اشاره به تیره‌ی بخصوص از نژاد سفید بکار
87:معتقد بودند که گهواره‌ی آریایی‌های ابرنژاد شمال باختری اروپا بوده و از آنجا به سرزمین‌های دیگر
98:کاربرد قرار گرفت و همانطور که در پالاگفته شد امروزه فقط برای اشاره به زبانهای ناشی از
102:ساسکریت در هندوستان و (بسه طور نادرتر) برای اشاره به زبانهای اییرانی و هندی
=== ARY latin index serra/saw ===
229:SMaedly cal eaten gl BHU oles fl y0 qetlen gdb Sash cpl crglis gph cle cal Saw
555:cpl S sidinn jy pl) scul 00 y “AGRAS" Sacre silead get OT jl Leeds ool Gear :
571:Sy Sacsan glygsl 9 a cuales glandly dod Ha y lead glitih 1 6 ch yry
598:Sle bond HES IVG 9 gk yy jlo yb ala! jpn bets yey lodil plead
1001:JET She) plead Glebe caiman y gS sled ply bad Som oy bas
1167:6S HN oP Cops Ad le ale oy yo WTR dle ys cae pr plead a Sb
4418:wlead oh F
5570:SERRACH :(IRISH) 43 p\ STERBAN (OLD SAXON) oS py-St
7366:sdilead vaho com gh
10867:DELAMARRE: 195 ‘AxsAW AOSSETIC) gay)
12430:hts Lead Uy i pST Sly gel el tiie Lalita, ly et ly LA eel A rly coe
14060:‘REFERENCES bewhay MUGIR SPANISH) olilead
```


## [2026-09-14T02:32:17.171Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '51880,51905p' POK_full.txt | cut -c1-260\necho \"--- page line after\"\nawk 'NR>51898 && NR<51930 && /Page\\(s\\)/' POK_full.txt | head -3\nawk 'NR<51898 && /Root \\/ lemma/' POK_full.txt | tail -2",
 "description": "Find Pokorny root containing Avestan sraesta"
}
```


### [2026-09-14T02:32:18.310Z] TOOL RESULT

```
Page(s):617 

Root / lemma: Rred- 

See also: see above S. 579 f. under Rered-. 

Page(s):618 

Root / lemma: Rrei- 

Meaning: to appear, show oneself 

Material: Old Indie sn-i. "beauty, splendor, satisfaction, richness, glory, magnificence', 

Avestan s/7"-' beauty'. Old Indie 5/7-/a- 'beautiful, lovely, superb, pretty, splendid', a-snra-^ 

ugly, not good looking ', Avestan 5/7?5- "beautiful', Kompar. Old Indie sreyas-, Avestan 

srayah-, Superl. Old Indie srestha- {srai'stha-), Avestan sraesta-. Old Indie sreman-m. " 

decoration, preference ', Avestan srayan-n. "beauty'. Adj. "beautiful'. Old Indie sr/yase Dat 

n. "beautiful'; 

horn. poet. Kpsiwv "noble, princely, ruler' (supu Kpsiojv, Kpsiouaa) Kpsojv Pind. Aiseh., 
nachhom. EN Kpsouaa (*Kp£[i]-ovT- participle " shining out ' (?), stands perhaps as 
--- page line after
Page(s):618 
Page(s):617 
Page(s):617 
Root / lemma: Rred- 
Root / lemma: Rrei-
```


## [2026-09-14T02:32:19.466Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY شغال سرب سیر ===\"\ngrep -n \"شغال\\|سرب\\|شگال\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== HUB sir/surb ===\"; grep -n -i \"surb\\|728\\.\" HUB.txt | head -10",
 "description": "Grep Aryanpur and Hübschmann"
}
```


### [2026-09-14T02:32:19.554Z] TOOL RESULT

```
=== ARY شغال سرب سیر ===
1079:را اشغال کردند نه تنها از پرتری فنی (اسب و ارابه) برخوردار بودند بلکه از نظر جنگجویی و
1083:می‌شد. در روم باستان» هنگام جنگ کشاورزان عادی تبدیل به سربازان ماهر می‌شدند. در اسپارت
1084:(5۳۸77۸) اکثر مردان سرباز بودند و بردگان و زنان کشاورزی و دامداری می‌کردند. ْ
6109:۲- چم این واژه در زبان پهلوی و زبان بلوچی؛ شغال.
10531:چم اين واژه ذر زبان ابرلندی کهن و ولزی: گروه» گروه سربازان.
=== HUB sir/surb ===
313:liche Name fiir *Blei' ist surb, Urspriinglich gilt arzzz
2614:728. Dazu auch afgh. surup *Blei' mit auffalligem p wie in
2617:Ebenso fiihrt Vullers neben usruh = surb die Formen
6258:Kerb'; surb (fiir ^surub) ^= usrub *Blei', afgh. bal. surup,
7571:zd. sraoni'^ surbj usrub *Blei* H. 728, oben p. 74; siristan
```


## [2026-09-14T02:32:29.793Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (313,2614,6258,7571):\n    print(ln,'leaf0',\"\\n\".join(txt[:ln]).count('\\f'), '-> printed', \"\\n\".join(txt[:ln]).count('\\f')-10)\nEOF\necho \"--- HUB 2610-2625\"; sed -n '2608,2625p' HUB.txt | cut -c1-200\necho \"--- HUB 6252-6262\"; sed -n '6252,6262p' HUB.txt | cut -c1-200\necho \"--- HUB 308-318\"; sed -n '308,318p' HUB.txt | cut -c1-200",
 "description": "Read Hübschmann passages on surb"
}
```


### [2026-09-14T02:32:30.943Z] TOOL RESULT

```
313 leaf0 22 -> printed 12
2614 leaf0 84 -> printed 74
6258 leaf0 187 -> printed 177
7571 leaf0 223 -> printed 213
--- HUB 2610-2625
723. Zur Bedeutung vgl. gr. yigarvg^ v^Qarsgog 'stark' = got.
hardus *hart*.
726. Np. sardpd *Ehrengewand' heisst eigentlich: Von Kopf
zu Fuss. Vgl. np. sarvapCi von gleicher Bedeutung.
727. Die verschiedenen Formen gehen auf ein ap. ^sroda-
== zd. ^srada^ zuriick.
728. Dazu auch afgh. surup *Blei' mit auffalligem p wie in
bal. surup. Auch im Phi. erscheint p : srp {= srup)
und srpen (= srupen) Phi. Vd. p. 131, Z. 15 und 13.
Ebenso fiihrt Vullers neben usruh = surb die Formen
*) Die Lesung *stowar* ist falsch.— 75 -
usrup und usruf an. Alle stimmen nicht zu zd. sruva-
'Blei' (nur als accus. 'srutn belegt).
731. Np. sarma ^est forme par analogie siir garma'* Dar-
mesteter, Etud. iran. I, p. 267 Anm. Die Analogie-
bildung fand schon im Phi. statt [sarmok nach gar-
mak).
732. Vgl. afgh. LW. sariSi, siriSt 'nature, temperament',
--- HUB 6252-6262
'dunkelblau ; lab Xippe (oben p. 96) ; 7iab rein, ungemischt*,
zd. andpem (ace); wat^ *Fruchtsaft, Wein H. 1025****; nisBb
'Unteres, unten H. 1034; vireb *curvus', arm. vr^ 'torto,
perverse*; kobm *Mitgift', arm. kapenR; kabl *ASe = phi.
kaplk, arm. kapik ; kabar 'Kapernstrauch', armen. kapar, gr.
xdnnaptg ; sabad, arab. sabada = arm. sapat, sapatak 'Kasten,
Kerb'; surb (fiir ^surub) ^= usrub *Blei', afgh. bal. surup,
phi. sr(u)p; sabuk 'leicht' = paz. sabuk Min. 61. 180 — 181,
phi. sapiik (oder spuk?) Phi. Min. p. 63, Z. 15, Yatk. i.
Zar. 65 (afgh. spuk light*).
§ 69. In einigen Fallen ist p nach Vokalen geblieben.
--- HUB 308-318
flir *Seide' sind wohl sammtlich aus dem Neupersischen
entlehnt, ebenso das syr. Wort, vgl. de Lagarde, G. A.
p. 7.
68. Np. a/i^Tz heisst auch 'Zinn\ vgl. Gazophyl. s. v. stagno,
Rosen, Neup. Sprachfuhrer p. 35 u. s. w., der eigent-
liche Name fiir *Blei' ist surb, Urspriinglich gilt arzzz
fiir beide Metalle, indem man zwischen weissem arztz
= 'Zinn' und schwarzem arziz — 'Blei' unterschied.^)
Auch die Armenier nennen Blei schwarzes ardic, Im
Pehlevi musste das Wort *arctc lauten. Geldner's
arezazi' (nach Darmesteter = *bataille*) habe ich
```


## [2026-09-14T02:32:31.665Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6100,6118p' incoming/ARY/ARY_pages.txt | cut -c1-300\necho \"=== which pdf page ===\"\nawk 'NR<=6109 && /\\[pdf page/' incoming/ARY/ARY_pages.txt | tail -2",
 "description": "Read Aryanpur context for shaghal"
}
```


### [2026-09-14T02:32:32.780Z] TOOL RESULT

```
گوتیکه (007710): 75 پسگشت‌ها 5
ابسلندی کهن (504(0701۵2۷ صا0): 271070 9 . ۹ 80070
71/۸ 11124 : مد ها
انگلیسی (6۸01/34)(از فرانسه‌ی کهن) 40 جتما‌دن 1
7 ومو 1 :0/105
لینرانی (/777۸/4لر): 7۸۸8 635 درا
آلبانی (0ا#لمقلم: 721 برهان قاطع + ۲ و ۵۳۵
یادداشت:
۱- چم این واژه در زبان اوستایی: بچه,
۲- چم این واژه در زبان پهلوی و زبان بلوچی؛ شغال.
۳ این واژه در زبان‌های رومانس و انگلیسی به چم اتازه" و "لطیف" و "تورسیده" هم بکار می‌رود.
اوستایی (472874/۷): دانمارکی (0۸(153): 70
71 بل1۸08 سوئدی (81782(57): 70
پارسی باستان (/(۲8۸۶ صا0): نروژی (49ا0/0750: 70
: 758۸ ,70773۸ اسلاوی کهن (16شا5 7767 صاه):
پهلری (1اتلمه): ان
6 مبم 713 ,73 روسی (/لم891لا): 71
افغانی (پشتو) (/4۳۵۸): ان لیتوانی (هفتاهفتانتتلم: 7083651۸8
سانکریت (54/577): 1 دنا ۷ با
=== which pdf page ===
[pdf page 206]
[pdf page 207]
```


## [2026-09-14T02:32:48.629Z] TOOL CALL #42: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1116 --image 2>&1 | tail -40",
 "description": "Fetch Borhan-e Qate page 1116"
}
```


### [2026-09-14T02:32:49.780Z] TOOL RESULT

```
no scan of BQT covers printed page 1116 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:32:54.837Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 573 574 575; do echo \"=== awk leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -25; done",
 "description": "Print Borhan vol2 leaves near p.1116"
}
```


### [2026-09-14T02:32:55.877Z] TOOL RESULT

```
=== awk leaf 573 ===
  ‫تس رز —‬

‫برامن آن است کهیومرث را صد فرزدد از‬                 ‫قاضی شهر لوط است و او فتوی بلواط (‪ )۱‬داده‬
 ‫نور بود‪.‬ءچون بحد رشد و تمیزرسيدد‬
                                ‫اناث و ک‬            ‫از فرای لوط »ودر آن‬        ‫بود ‪ -‬ونام قرده‌ایست‬
  ‫خادا‬  ‫ده ر‬
           ‫در شب این روز جشن ساخت وکهم‬               ‫میاه و اشجار بسیار بوده و در این زمان مقلوب‬

 ‫کرد و فرمودکه آنش بسیار ابفرروختند‪.‬بدان‬             ‫است و در زمین آن زرع وگیاه نووید وزمینش‬
‫سیب آن را سده میگویند > وبسنی مخترع این‬               ‫سیاه باشد و مفروش بسنگهای سیگاءوی‪.‬ند‬
 ‫جشن هوشنگه بسنيامك را میدانند و سبب‌آن‬              ‫آن سنگهایی است که برقوم لوط باریده بوده‬
‫در *چشن سده » مذ کور است ؛ وجمعی برآ نند‬            ‫است ‪ -‬و حاکم شالم را یز گفته‌آند ‪ -‬و نم‬
‫که چون درین روز عدد فرزندان آدم ودر سیف‬            ‫اول نام دارالسياسةٌ بهرام کور بود و چوندرآ لجا‬
 ‫جشن عظیمی کرد بدین نام موسوم شد؛ وبعضی‬             ‫می نشت بار اول نظرش بهر که می‌افتاد او را‬
 ‫دیگر کوبند چون از ابن روز تا وروز پنجاء‬             ‫میکشت تناکآه‌روزی اعراسبی‌رادید وحکم کشتن‬
 ‫روز وینجاه شب است که مجموع آن صد باشد‬               ‫اکورد ‪ .‬اعرابی پرسید‪ :‬سبب کشتن من چیست؟‬
 ‫می‌گویند» وصد هاد معرب سد‬        ‫متام ان سده‬        ‫گفت ‪ :‬دیدن تو مرا نامبارك است ‪ .‬اعرابی در‬
 ‫بین است چه دکلرام فری‌قديم صاد نیامده‌است‬          ‫خنده شد و گفت‪:‬الحال دیدن تومرا شوم و نا‬
 ‫‪ -‬وئام درختی هم هت که در دارالمرز و ماوراء‬          ‫مبارك باشد ‪ .‬بهرام ازین کفتگو متأتر شد و بر‬
     ‫انبم‬                        ‫اا دک‬                                                    ‫طرف کرد ‪۰‬‬
 ‫وبمثابه‌ای بزر که که تنه آن بدشواری در بغل‬         ‫سكه = بفتح اول و انی ‪ ۰‬بمعنی آتش‬
‫و بگرهایش بمرتبه ای‬        ‫چهپارکس دآرید‬
                                       ‫س‬            ‫شعلة کشنده و آتش مله بلند باشد ‪٩‬‏ ‪ -‬و نام‬
 ‫انبوه که باران ازآن نگذرد و" تا دوصد سوار در‬        ‫قربه ایست از قرای صفاهان ‪ - ۴‬و نام روز دهم‬
 ‫سابة آنآ رام توانند گرفت و مهدی مدور که‬            ‫بهمن ماه است ‪ ۷‬و در این روز فارسیان‌عید کنند‬
=== awk leaf 574 ===
                                                                                                  ‫=‬            ‫‪-‬‬

‫وا خلال‬
      ‫آشدنر‬
          ‫بلفت اهل مدینه غور خرما با‬                        ‫کنند سیاهی را بیار شفاف ورنگین سازدوآن‬
                                    ‫گیوزبند ‪.‬‬            ‫درخت را آغال مشه ویشه غال ویشه دار ودر دار‬

‫سك یر ‪ = ۲‬بروزن سربر » مخقف سه‬                           ‫و سارخکدار (‪ )۱‬و سارشکدار و لامشگر وکڑم‬
‫مود که نعمان‌ین منذر‬     ‫دیر است و آن عمارتی‬             ‫ونجك وناژین نیز خوانند و بعربی شجرةالبق‬
                                                                                               ‫گ‬
  ‫ممرب‬
     ‫دسضی‬
        ‫بودنوب‬
             ‫وه ب‬
                ‫گخت‬
                  ‫بجهت بهرام کور سا‬                                    ‫کوبند ‪ ,‬وممرب آن صدق است‪.‬‬
                                   ‫صەدىر است ‪.‬‬              ‫سكی = بفتح اول والی بتحتالی رسیده‪,‬‬


                                                ‫بیان نهم‬
  ‫و کنات‬        ‫ودولغت‬     ‫وشصت‬         ‫بی‌نقطه بارای بی نقطه مشتمل بر دوست‬                            ‫درسین‬


‫خوانند چنان که کوبند «برسردیوار؟ یمنی بالای‬               ‫سر = بفتح اول و سکون الی‪ ,‬ممروف‬
 ‫دبوار بور«سر کوه»بمنی‌بالای کومو«برسرراه»یمنی‬
=== awk leaf 575 ===
  ‫‪“NNN‬‬                                                                                                 ‫سراب‬


   ‫نی‬
    ‫‪-‬و‬‫مع‬
       ‫بآید‬
          ‫که آب از رود ځاله بجوی می‬                          ‫خراسان روی آثرا از رمان سیاه سازند ‪٩‬‏ ‪-‬‬
 ‫و کنابه از معدوم‌ولابود‬      ‫زیده و خلاصه همست‬             ‫جلوامششی است کهبر اعضا پهن شود و بشره‬
                                                                                                ‫و‬
                            ‫باشف ‪۰‬‬      ‫غرور وک‬      ‫و‬       ‫را کسرخداند و آنرا بعربی شری خوانند ‪-‬‬
                                                              ‫ونام نوعی است ازماهی که طولآن ببكاکشزد‬
                                           ‫و تمام باشد‪.‬‬      ‫دراکرهد مانند پیکان تیرو اکثر‬
                                                                                         ‫و خرطومي بز‬
‫سر ابردی ‪ = °‬بارگاه بادشاهان را‬                              ‫حیوانات را بدان گزلد رسالد وبمعنی‌رنگهسرخ‬
                                                             ‫بلشد ‪ - ۳‬ویمعنی باودان حم هت که در نامهای‬
 ‫کوبند ‪ -‬وپرد بلندی‌را نیز میگوبند کهبمنزله‬
         ‫کشند‬    ‫خیمه گاه‬    ‫دور‬   ‫باشد که در‬   ‫دبواری‬
                                                            ‫خانه بجهت آب باران صب کنند ‪ -‬ونوعی از‬
                                                                                 ‫رقص باشد شبیه بارغعنك ‪۰#‬‬
 ‫‪-‬نابه ازآسمان‬
             ‫سرا برد کحلی ک‬
                                   ‫‪ -‬و ابرسیاه باشد ‪.‬‬        ‫سراب د بر وزن خراب ‪ .‬زمین شوره‬
                                                             ‫راکوبند که در آفتاب می‌درخشد و از دور باب‬
 ‫سآرلیلی ‪ -‬با بای ابجدبروزن قبانیلی‪,‬‬
              ‫تشک و رسای راکو‬                                                                        ‫میماند و‬
```


## [2026-09-14T02:33:05.089Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (5532,):\n    print(ln, '\\n'.join(t[:ln]).count('\\f'))\n\"\necho \"=== leaf around ===\"\nfor n in 577 578 579 580; do echo \"### $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | grep -n \"سرب\\|اسرب\\|رصاص\" | head -6; done",
 "description": "Locate سرب headword leaf in Borhan vol2"
}
```


### [2026-09-14T02:33:06.209Z] TOOL RESULT

```
5532 96
=== leaf around ===
### 577
### 578
### 579
3:‫کوبند و‪-‬هرچیز لرمی را نیز گفته‌اند که‌درزیر‬               ‫سرب = بفتح اول و کر ثالی بروزن‬
7:                                                          ‫که‬   ‫اسرب است‬              ‫رضم اولوسکون ثانی؛ مخقف‬
52:   ‫‪ ۱‬اوستا ‏ لا‪٩۲‬‏ ( سرب ) ‪ ۰‬بپلوی ‪ ( ۳1۳۲9‬سربی ) ‪ .‬کردی ]‪ » 3۳15‬بلوچی‬
54:       ‫‪ - ۴‬رك سربار (ح) ‪.‬‬     ‫رك ‪ :‬اسرب » معرب آن یز «اسرب» «لخب ‪« ۲۲۲‬تفس؟ ‪.‬‬
59:  ‫در برهان فاطم مرفوم که حصه ونصیب وقسمت است امااز‬                    ‫‪« - ۴‬سربخش‬                        ‫گفته مشود ‪.‬‬
62:   ‫که تو سربخش مردمالی معلوم میشود که تو آغاز وابتدای نوع اسانی یا زبده وخلاصة مردمانی‬
### 580
16:                                                                            ‫باشد ‪ -‬و سربالا کردن را نیز گوبند‪.‬‬
```


## [2026-09-14T02:33:13.262Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==579' BQT_v2_pages.txt | sed -n '1,10p;48,60p'\necho \"=== page-number-ish tokens ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==579' BQT_v2_pages.txt | grep -oE \"[0-9]{4}\" | head",
 "description": "Print Borhan leaf 579 sarb entry and footnote"
}
```


### [2026-09-14T02:33:14.651Z] TOOL RESULT

```
 ‫‪Ahhh‬‬

‫کوبند و‪-‬هرچیز لرمی را نیز گفته‌اند که‌درزیر‬               ‫سرب = بفتح اول و کر ثالی بروزن‬
‫ولاه زره دوزند تا سررا آزار نکند‬
                               ‫کلاه خود ک‬                 ‫عقب ‪ ۰‬بمع؛ی بوده وافشرده و آزهم رفته باشد ‪4‬‬
‫هم بنظر آمده است که‌فوته‬     ‫ازار )‪۱‬‬   ‫و نمی‬      ‫‪-‬‬
                                                          ‫که‬   ‫اسرب است‬              ‫رضم اولوسکون ثانی؛ مخقف‬
                            ‫وشلوار باشد‬   ‫ولنکوته‬
                                                                     ‫عریی آنك وبهندی سا خوانند‪۶ .‬‬
‫برتیغ خاریدن «کنابه از کنتن‬

                                                                   ‫آزار ‪.‬‬   ‫‪:‬‬        ‫چب ‪ , ۱‬چش‬          ‫(‪)۱‬‬


   ‫‪ ۱‬اوستا ‏ لا‪٩۲‬‏ ( سرب ) ‪ ۰‬بپلوی ‪ ( ۳1۳۲9‬سربی ) ‪ .‬کردی ]‪ » 3۳15‬بلوچی‬
   ‫‏‪< suru. surup‬استق ‪ ۱۲ ۸۲۷‬افتانی ‪0۵‬ا‪۲‬نا‪ . 5‬رك ‪ :‬هویشمان ‪ ۰ ۸۲۷‬کیلکی ‪0۲‬نا‪.5‬‬
       ‫‪ - ۴‬رك سربار (ح) ‪.‬‬     ‫رك ‪ :‬اسرب » معرب آن یز «اسرب» «لخب ‪« ۲۲۲‬تفس؟ ‪.‬‬
   ‫شاه بپلوی‬   ‫رضا‬   ‫محمد‬    ‫سلطنت‬   ‫اوائل‬   ‫و‬   ‫بهلوی‬   ‫رضا شاه‬     ‫أطت‬            ‫دورة‬   ‫اواخر‬   ‫در‬     ‫‪۴‬‬


   ‫‪ ۵‬سرپاس ؟ بہمردیف سرتیپ در تشکیلات شهربالی (نظمیه ) اطلاق میشده وابنك مجدداً سرتیپ‬
  ‫در برهان فاطم مرفوم که حصه ونصیب وقسمت است امااز‬                    ‫‪« - ۴‬سربخش‬                        ‫گفته مشود ‪.‬‬

=== page-number-ish tokens ===
2720
```


## [2026-09-14T02:33:25.547Z] TOOL CALL #46: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:1270 --image 2>&1 | tail -50",
 "description": "Fetch Borhan page 1270"
}
```


### [2026-09-14T02:33:33.889Z] TOOL RESULT

```
بر 1
ی 6 عامیدن 8 .
وزن کمال . جالوری فغ بو ‎٩‏ ار :
است معروف ؟ «واو شفغال تعر 72 ه بفتح اول وین دوم
ی ۰ خ ا؟ توایم نموه
برزخ‌است میان گر که و روباه. کویند در زمان بر وزن شکر بکن *کلمه‌ایست از توابع بمعنی
ابوشیر وا پراکنده و پریشان .
شیروان بهم رسید . ۰
دی شغْت -« بر وزن كجك . مردم جلف
ی دزن کدالی . نوعی از ۶ | وایله و نادان را گوبند.
باشد و بعربی عنب کوبند. *
شغه ۷ ه بفتم اون و بان » معت |
شفا ۳ درد یش ۹ ترکش بسح ول و نی بمعمی ول
۵ - بروزن تباه کیش و اتر ۱ ای
۱ 5 ۱ شغ است که خاخ درخت و غاخ کوسقند وکاو

تبرداثر گوید خوانند. ۰

وتیردالرا وید و بمربی ی 2۳ باشد - وپینةٌ دست وپا و اعضای اسان وحیوانرا

شغر - بح اولءئانی‌وسکون رای‌فرشت. کویند که بسیب‌کار کردن بسیار بهم رسیده‌وبسیار
پوست دست و اندام باشد که بسبب‌کار کردن وکار سخت و سطبر و کنده شده باشد ۸ - و آبله
فرمودن‌بسیار سخت وسطبر شده باشد ۴ ؛ وبفتح | دست ویا را نیز کویند که بسبب کار کردن وراه
اول و ثانی هم باین معتی وهم بمعنیآبله باشد | رفتن بهم رسیده باشد ۸ ۰

۹ کال (م.) ازسماسکریت 6۳8214 (شغال).یپلوی 51328101 #ترکیع 22981
«اسدق ۰۹۷۸۵ افنانی 22832 (رك : هوبشدان ۷۸۵ معرب آن جقل (,فتح اول ودوم)«نفی»
این‌5 مه ازتر کی وارد زبانهای آروپایی شده : آلمانی 51221 » فرانسوی 6۶0۵ ۰ انگایی
1 آقای پورداودکلمهٌ «شفغال» رالفت سرزمین بابل داسته‌اند ۸« فاب ص۲۱۸ ۰

۲ چهارپایی کوشتخوار راز نوع سک که بیشّر در مناطق حاره رز پست آکنده

صیاد نه هر بار شغالی ببرد افتد که بکی روز پلنگش‌بدرد.

« کلتان ۰.۰۱۹۲

۴ اشفا (ه.م.). ۴ مصدف *شفه؟» («.م.) 5 8 - ر4: هنتهی آلارب
وشرح فاموی . ‎٩‏ - در فرهنگه نظام « شغز بفر * ۰ امااين ثر کیب عربی است وهردو
براه است : «تفرقوا شغربفر» ویکراولهما پراکندیدند بهر روی و هما اسمان جعملا و اخداً وبنیا
عای الفّح». «منتهی‌الارب؟؛. ابو شخ (و.م.) تس شوغ (و.م.) < شوغه (.م.) ۰

۸ -. «شوغ وشفه »سنگین شدن‌دست وپای بود وآ نرا بتر کی ایشتی() کوبند» (واسخةٌ
دیگر) « آن کوشت باشد که در دست‌وپای سخت شده باشد چون چرم» (دردخهٌ دیگر) «ستبری
باشد دریوست. عجدی(ءروزی) گوند :

«می دوم بجهان اندر از بی روزی دوبای پرشفه ومانده با دلی بریان».

«لفت فری ۲۳۳-۲۳۲ ور4ك: ۸4۹۷ -
( برهای‌قاطع ۱۹۴)
```


## [2026-09-14T02:33:45.680Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%D8%BA%D8%A7%D9%84/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for شغال, including any bracketed origin tag such as [سنس.] or [په.], and also the Dehkhoda entry's etymology if present."
}
```


## [2026-09-14T02:33:47.108Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%A8/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for سرب, including any bracketed origin tag (e.g. [په.], [ع.]), and the Dehkhoda entry etymology if present."
}
```


### [2026-09-14T02:33:51.026Z] TOOL RESULT

```
# Mo'in Dictionary Entry for شغال

**فرهنگ معین:**

"(شَ) [په.] (اِ.) جانوری است پستاندار از راستة گوشت خواران شبیه به سگ، که دارای دُمی پُر مو می باشد."

The bracketed tag [په.] indicates the origin marker used in Mo'in's dictionary.

---

## Dehkhoda Etymology

The Dehkhoda entry provides etymological context, noting that the word likely derives from Hebrew "shoual" (meaning fox). The entry also references that Turks borrowed this Persian word and called it "choghal," though Larousse mistakenly attributed it as originally Turkish. The word appears in various forms across Persian texts: شکال، شگال، شال، and others.
```


### [2026-09-14T02:33:53.212Z] TOOL RESULT

```
# سرب (Sorb/Lead)

## Farhang-e Mo'in Entry

**سرب** (sُ) [اِ.] — "A soft, malleable metal with a grayish color that exists in nature not in a free state."

## Dehkhoda Etymology

The Dehkhoda dictionary traces سرب back through multiple language layers:

- Avestan: "سرو" (saro)
- Pahlavi: "سرپین" (sorbin)
- Kurdish: "سیریفت"
- Balochi: "سوروپ"، "سوروف"
- Afghan: "سوروپ"
- Gilaki: "سورب"

The entry notes it's an abbreviation of اسرب (arsab), which is the Arabized form. In Arabic it's called "آنک" and in Hindi "سیسا."

**Additional context:** The metal possesses physiological and health properties with both acute and chronic toxicity effects. Historically known since ancient times, lead is a soft, heavy, grayish-white substance with specific gravity of 11.33, typically found as sulfur ore and often containing significant toxic compounds.
```


## [2026-09-14T02:33:59.176Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B1%D9%87/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for اره (arre, saw), including any bracketed origin tag, and the Dehkhoda entry's etymology if present."
}
```


## [2026-09-14T02:34:02.551Z] TOOL CALL #50: Bash

```json
{
 "command": "pdftoppm -f 473 -l 473 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg473 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg473.png",
 "description": "Render PDF page 473 to PNG"
}
```


### [2026-09-14T02:34:05.259Z] TOOL RESULT

```
# اره (Saw) - Dictionary Entries

## Farhang-e Mo'in (معین Dictionary)

The Mo'in entry presents two distinct meanings:

1. **Anatomical**: "(رِ) (اِ.) آرواره" - referring to the jawbone or alveolar ridge where teeth are situated.

2. **Tool**: "(اَ رُِ.) (اِ.) ابزاری است برای بریدن چوب یا فلز..." - a cutting instrument made from iron with a thin, serrated blade and wooden or metal handle, used for severing wood and metals.

## Dehkhoda Dictionary Etymology

The Dehkhoda entry provides linguistic background: اره originates as a noun referring to a speech impediment involving the letter "ر" (r-sound). The dictionary also traces geographical and anatomical uses, including references to dental alveoli (tooth sockets).

The tool definition in Dehkhoda cites classical Persian poetry from Ferdowsi to illustrate historical usage, particularly in the context of cutting objects in half—a practice documented in ancient narratives.
```


### [2026-09-14T02:34:07.109Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 72343 Sep 13 22:34 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg473.png
```


## [2026-09-14T02:34:08.626Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg473.png"
}
```


### [2026-09-14T02:34:09.200Z] TOOL RESULT

```

```


## [2026-09-14T02:34:09.193Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:34:20.859Z] TOOL CALL #52: Bash

```json
{
 "command": "SP=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npdftoppm -f 11 -l 11 -r 220 -png -singlefile \"/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BLY/BLY_Hvatanica_II_BSOS9_1937_pp69-78.pdf\" $SP/bly78-473 && ls -la $SP/bly78-473.png",
 "description": "Render Bailey Hvatanica II p.78"
}
```


### [2026-09-14T02:34:22.865Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 207924 Sep 13 22:34 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bly78-473.png
```


## [2026-09-14T02:34:24.501Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bly78-473.png"
}
```


### [2026-09-14T02:34:25.066Z] TOOL RESULT

```

```


## [2026-09-14T02:34:25.050Z] INPUT

[Image: original 1247x2103, displayed at 1186x2000. Multiply coordinates by 1.05 to map to original image.]


## [2026-09-14T02:34:40.819Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW serra ===\"; grep -n \"^serra\\|serra,\" LEW_1910.txt | head -10\necho \"=== LAT serra ===\"; grep -n \"^serra\\|serra \" LAT.txt | head -10\necho \"=== SKT serrate ===\"; grep -n \"^SERRATED\\|^SERRY\\|^SIERRA\" SKT.txt | head",
 "description": "Grep Walde, Ernout-Meillet, Skeat for serra"
}
```


### [2026-09-14T02:34:41.037Z] TOOL RESULT

```
=== LEW serra ===
=== LAT serra ===
1156:serra, globus; sur ces termes v.Kretschmer, Glotta 6,30), et par exten-
12317:serrare primitive se composait d'un clou ou d'une cheville passae dans
57766:serra, -ae f;: i° scie (outil), et scie (poisson); 2° ordre de ba~
57779:serracum : sarracum.
=== SKT serrate ===
```


## [2026-09-14T02:34:43.507Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57766,57782p' LAT.txt\necho \"=== LEW grep serr ===\"; grep -n \"serr\" LEW_1910.txt | head -10",
 "description": "Read Ernout-Meillet serra entry"
}
```


### [2026-09-14T02:34:43.644Z] TOOL RESULT

```
serra, -ae f;: i° scie (outil), et scie (poisson); 2° ordre de ba~
taille en dents de scie.(cf. acies, globus, cuneus, etc.); 3 0 montagne
(b.latin; v.Eoogter, D in du Cange, 9, p.10). - Ancien, technique.
M.L.7861. Celt.: iri., britt. serr.
D 4 rir^s: serrula f.; serrSrius m.: scieur (de pierres); serratus :
en dents de scie (^pithbte de la germandr^e); serrat in', serro, -as:
scier (b.lat.); serrdgS : sciure (Cael. Aurei.), M.L.7863; serrSbilis
(Plin.), etc., tous tardifs; serrdtula, nom it ali que de la "b 4 toine"
(Plin.); serrdlia (valr. sarralia Isid., Or.17,10, 11) • salade fris^e,
cf.M.L.7865 et sarracla CGL III 540,36. (sarracia)', 7866 *serrdnus
"poisson-scie"; 7868 serrdtai 7869 serricula: petite faucille.
Terme technique sans dtymologie claire. V.sarpG, et sera.
serrSculum: v. sera.
serracum : sarracum.
serula (serola) : fisalidus (-dis) = cpuooAtSoC Gloss. Sans doute
de serum, designant-une ampoule; cf.scara: scabies super uulnera,
et scaria : fisalida (Gloss.).-
=== LEW grep serr ===
7570:seemin (air.) IT 559 seinm (nir.) II 559 seir (mir.) IT 572 sewrig (mir.) IT 376 seisg (nir.) II 505 seisreach (nir.) IT 529 selb (air.) I 264, IT 745 selg (air.) [799 selige (air.) IT 470 semar (nir.) IT 808 sén (mir.) ,,Netz‘ IT 575 sen (air.) ,,alt‘ IT 514 sén ,,Zeichen‘‘ IT 535 senvm (air.) IT 559 senmathir (air.) II 514 senn- (air.) IT 559 serb (air.) IT 450 serbh (mir., nir.) IT 526, 588 sercom (air.) IT 526 serg (mir.) Il 526 sernaid (air.) IT 523 sernim (air.) IT 591 serr (mir.) II 480, 524 serrfiach (mir.) IT 257 serriach (mir.) IT 257 sesc (air., mir.) IT 5338, 675 sescaind (mir.) IT 488 sessam (air.) IT 597 sessed (air.) IT 529, 597 sessrach, sessrech (mir.) IJ 524 sét (air.) ,,Weg* IT 516 sét (mir.) ,,Wert- einheit’ JZ 516 sét- (air.) ,,blasen‘‘ IT 532 sétaim (mair.) IT 476
12201:preicalis I 226 pro IT 364 quar IT 405 quatts I 714 quer, quendan IT 405 queke I 262 quote I 714 ragis II 435 rakis I 151 rawys IT 453 redo If 440 reiks II 432 rikant- IT 432 riclis I 38 ryparts IT 430 sackis IT 623 salme I 303 salmis £196 salus IT 538 same I 665 san- I 252 sansy I 52 sardis I 243 sarke I 275 sarwis If 523 sarates I 166 sasins, sasintinklo TI 156 saxtis Ii 464 saxsto IT 484 schis I 193 schuwikis, schume- no Il 6381 sebbet IT 626 seydis I 502 seeming If 224 seyr I 271 semen II 512 semmar, senme T6665 semo I 645 sen I 252, IT 539 sen- (kur.) I 252 sengijdi IIT 359 senrists IT 433 septmas IT 518 sermen I 204 serripimar II 430 sidons IT 508 sien IT 626
```


## [2026-09-14T02:34:52.004Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb && curl -s \"https://en.wiktionary.org/w/index.php?title=serra&action=raw\" | sed -n '/==Latin==/,/==Portuguese==/p' | head -40\necho \"=========== rhine\"\ncurl -s \"https://en.wiktionary.org/w/index.php?title=%CE%A1%CE%AF%CE%BD%CE%B7&action=raw\" | head -30\necho \"=========== rhine lower\"\ncurl -s \"https://en.wiktionary.org/w/index.php?title=%E1%BF%A5%CE%AF%CE%BD%CE%B7&action=raw\" | head -40",
 "description": "Fetch Wiktionary Latin serra and Greek rhine"
}
```


### [2026-09-14T02:34:54.052Z] TOOL RESULT

```
==Latin==
[[Image:Pily rozplatnice.jpg|thumb|trēs serrae (three saws)]]

===Etymology===
According to De Vaan, from {{inh|la|itc-pro|*serzā}}, from {{inh|la|ine-pro||*sers-eh₂}}, from {{m|ine-pro|*sers-||to cut off}}, from which he also notes Schrijver's derivation of {{m|la|sarrio}} from a zero-grade of such a root.<ref>{{R:itc:EDL|head=serra|page=558}}</ref>

Compare, however, {{noncog|cel-pro|*serrā|t=sickle, scythe; billhook}}, with a different etymology.

===Pronunciation===
* {{la-IPA}}

===Noun===
{{la-noun|serra<1>}}

# a [[saw]] (tool)
# a kind of [[sawfish]]
# {{lb|la|military}} a [[serrated]] battle order

====Declension====
{{la-ndecl|serra<1>}}

====Related terms====
{{col4|la
|serrābilis
|serrāgo
|serrātim
|serrātōrius
|serrātūra
|serrātus
|serrō
|serrula
}}

====Descendants====
{{top4}}
* {{desc|sq|sharrë}} {{q|disputed}}
* {{desc|rup|sharã}}
* {{desc|ast|serra}}
* {{desc|eu|zerra}}
* {{desc|ca|serra}}
=========== rhine
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
=========== rhine lower
==Ancient Greek==

===Alternative forms===
* {{alter|grc|ῥίν|g=f||Koine}}

===Etymology===
{{rfe|grc}} <!-- Is there relation to {{m|grc|ῥῑ́ς|g=f|t=nose}} or  {{m|grc|ῥῑνός|g=f|t=skin of a man; hide of a beast}}  ἡ ῥῑνός, τῆς ῥῑνοῦ -->

===Pronunciation===
{{grc-IPA|ῥί¯νη}}

===Noun===
{{grc-noun|ῥῑ́νη|ῥῑ́νης|f|first}}

# [[file]], [[rasp]]
# [[angel shark]] ({{taxlink|Squatina squatina|species}}), whose [[skin]] was used for [[polish]]ing [[wood]] and [[marble]]

====Inflection====
{{grc-decl|ῥί̄νη|ης|form=F}}

====Derived terms====
{{col4|grc
|ῥῑνάριον<!--small file-->
|ῥινάω<!--lead by the nose; file-->
|ῥῑνέω<!--file-->
|ῥῑ́νημα<!--which is filed off, filings-->
|ῥίνησις<!--filing-->
|ῥινητήριον
|ῥινητής<!--one who files-->
|ῥινίζω<!--file-->
|ῥινίον<!--diminutive of file (ῥίνη), or nose (ῥίς)-->
|ῥίνισμα<!--which is filed off, filings-->
}}

====Descendants====
* {{desc|mul|{{taxfmt|Rhina|genus}}|bor1=1|{{taxfmt|Batrachorhina|genus}}|der2=1}}

====See also====
Not to be confused with:
* {{m|grc|ῥῑ́ς|t=nose}} and its [[ῥίς#Related terms|related terms]]
```


## [2026-09-14T02:35:13.170Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN arre ===\"; grep -n \"arra\\|arre\\|'Säge'\\|Säge\" HRN.txt | head -10\necho \"=== HUB arre ===\"; grep -n \"Säge\" HUB.txt | head -10\necho \"=== PHD saw ===\"; grep -n \"^saw \\|saw (n\" PHD.txt | head -5; grep -n \"arrag\\|arra \" PHD.txt | head -5\necho \"=== NYB arrag ===\"; grep -n \"arrak\\|arrag\" NYB_vol2_glossary.txt | head -5",
 "description": "Grep Horn, Hübschmann, MacKenzie, Nyberg for arre/saw"
}
```


### [2026-09-14T02:35:13.272Z] TOOL RESULT

```
=== HRN arre ===
1591:i/^sthä' 'bleiben, verharren*, avasthita- (von Personen)
3676:nApers. takaharä = elamit. takaharrahe = assyr. sa magidüta ina
6238:mir meine Lesung des Steins ZDMG. 18 No. 127 (II) Farraxü(%) m
6620:OeraT, miuj. sardi, sar haröi, si/n. arrai,
6758:5) IV^u/^ijufQoy, H. 8. Jarret, Aln-i Akbari-Transl. Vol. II, 13
7061:np. ferrux 'glücklieh', phlv. farraxü, farraxülh
7068:den Beinamen farra/ß (Hörn, a. a. O., 39).
8039:arm. arab. LW. vard, (sogar ar. muvarrad rosenfarbig',
=== HUB arre ===
=== PHD saw ===
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
832:Aries Warrag.
2550:lamb warrag.
=== NYB arrag ===
1202:darrak [drky] ravine, or rock HajB: 7. 13, Prth. equivalent vēm (q. v.). - NP darrah ‘a valley between hills. V. Nyberg, Christensen Vol., p. 69.
1434:én [inser., Ps. ZNH, but already in the inser. the z is often stunted; BP ZNH] dem. pron. this here, always referring to the present situation, that of the speaker, or to what is to follow; no pl.: api-n pad pat én darrak% nihat api-n tigr tar han citak be apakand we set our foot on this rock here and shot the arrow beyond that cairn yonder HajB:6-8; én damik this earth, our earth; én dam, én dam u dahisn, en getäh this world; én apécak vēh-dēn íi mäzdesnän this pure good religion of the Mazdayasnians 84? eto.; always én dén this (our) religion, of the Mazdaism; pat én apēgumān būtan ku to entertain no doubt about the fact that 634 etc.; vicčirišn ... en kū the explan- ation is this that 121"; — én i forms an elliptic gen.: frdc én % man yaz perform what here is mine (my duty, the rite incumbent on me on this occasion) 535; én būt i 6 peš gobam this happened which I am now going to tell 54!?; — én and, v. and. — Skr ena-; not in Av. and OP; SW w.: MPrs. ‘yn (no pl, instead im&sän, imin are used); Paz. NP in. Tedesco, Dial. 216.
2710:darraky — to put one’s feet on the rock HajB:6-7.12-13; tigr andar kamān ~ to put the arrow to the bow (-string) 100%; catrang ~ to arrange a game of chess 11914.20.21. gartänäk be ~ to cast the dice 1202122; pat ... ~ to deposit in... 10719, 11312; apar ~ to put (wood) on (the fire) 95°; dast apar ~ to put one's hand (to work) 6215; bé ~ to deposit 4216, to take off (a garment) 5717; — nam m to give a name, to name 1025-36, 11421, 11623; pat nām i ... ~ to name after 1201-2; mēnišn ~ 6 to ponder on 5?2-?3, — Av. (721 sq.) ni-dä-; MPrs nh’dn, nyh?dg, Verbum 194; Ps. nyd?t; Paz. nahādan; NP nihādan; only SW.
3001:2pat[PWN; Prth. inser. pty] A. prep.; not governing encl. pronouns (in pat-šān dra- sanéh 10974 the enel. belongs to the follow- ing subst.). I. in a concrete sense: 1. local: in, on, upon, at; (to pass) over (a bridge), through (a passage); (to remain, dwell) with a p.; passim; 'pn LGLH PWN ZNH drky HNHTWN = api-n päd pat én darraky nihāt HajB: 6-7. (12-13), Prth NGRYN pty ZK wym HQ’YMW-t HajA: 6—7. (11-12); PWN ZK Psy ZY ... = pat hàn rah" 1... on the road to... P1:4. — 2. time: pat ham Sap 16°; pat- vastak hamë pat sap ka 5!; sap 1 sitikar pat usbam 1012-8 ; pat ul vaxšišneh inazdeh
3428:*2gīh: restore in 717-24, 8? the reading lk 4-7 of the MSS instead of conjectured wlk-- 1 (= varrak-ē) and 7?9. 8° Ik of the MSS instead of conjectured wlk' (= varrak), and read lk as the figure 30 = sih, lk--1 as 80+1 = sih-é. It is not advisable to emend a reading so persistently repeated and so unyieldingly maintained by all MSS, in spite of its enigmatic character. Of course, it cannot be the numeral thirty; the context requires a w. signifying a supernatural being which is finally un- veiled as the Glory (x%arrah, x"aranah) of the Kayanian kings. I venture the
```


## [2026-09-14T02:35:15.349Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT jackal ===\"; grep -n -i \"schakal\\|çakal\\|tschakal\" LKT.txt | head -10\necho \"=== TTS jackal ===\"; grep -n -i \"schakal\\|tschakal\\|čakal\" incoming/TTS/TTS_pages.txt | head -10\necho \"=== HJB jackal ===\"; grep -n \"^JACKAL\" HJB.txt | head -3",
 "description": "Grep Lokotsch, Vambery, Hobson-Jobson for jackal"
}
```


### [2026-09-14T02:35:15.433Z] TOOL RESULT

```
=== LKT jackal ===
1329:'Schakal';  hieraus  mit  ar.  Art.  sp.  adice, adiva  'dass.',  pg.  adibe,  adiba  'Schakal, Gold  wolf,  figürlich  auch 'Zwischenträger, Ohrenbläser'  [Constancio  Dicc  23  a],  frz. adive  'Zwergwolf'.  [DE  45/46.  Eguilaz 56.    ML  2626.
4358:T.anis  aureus,  Schakal',  ebenso  pers. säyäl,  tk.  sakal,  cakal;  hieraus  rum. ceacal,  it.  sciacallo,  afrz.  jachal,  frz. chacal;  engl,  jackal,  ndl.  jakhals [mit  volkselyinologischer  Umgestaltung], dtsch.  Schakal;  russ.  sakal,  cakal,  bulg. serb.  sakal,  cech.  sakal,  poln.  szakal 'Goldvvolt'.
5874:Saccharin  1855 ÄicÄ;  1781 SäcAreZ  1781 Sacker  falk  1799 Sackmann  1781 &'a/^«n  1752 Äa/"«/-«  1879 Ärt/'/jaw  1769 SaA/-«w  2178 Sa^o  1761 Sahara  1766 Sniga(antilope)  1774 Salangan  1844 Äa^pft  2001 Sa/t;p  2001 Äa/i««-  1567 Salniter  1567 salomonisch  1881 Sambuk  1824 sambaztac  ahd.  1742 sameztag  nihd.  1742 Samatag  1742 Samum  1819 Sandel(holz)  1825 Sapeke  1835 Sarafan  1845 Sarazene  1856  c Sarsche  1878 Sarong  1862 Safa«'  1867 Äa<m  2188 S(,/rt  1869 Schabbes  j.  1742 Schabbesgoj  j.  728 Schabracke  395 Schach  1762 Schacherjude  1763 schachern  j.  1763 schachtnott  1443 schachzabel  mhd.  1762 Schachzngel  1762 Schäfzngel  1762 si-haqgün  mhd.  434 Sc-Äa/i  1762 Schakal  1929
=== TTS jackal ===
=== HJB jackal ===
11674:JACKAL.
```


## [2026-09-14T02:35:23.179Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 1929 ===\"; sed -n '4354,4360p' LKT.txt | cut -c1-600\npython3 -c \"\nt=open('LKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('leaf0',' ','\\n'.join(t[:4358]).count('\\f'), 'printed', '\\n'.join(t[:4358]).count('\\f')-26)\"\necho \"=== HJB JACKAL ===\"; sed -n '11674,11686p' HJB.txt | cut -c1-700",
 "description": "Read Lokotsch 1929 and Hobson-Jobson JACKAL"
}
```


### [2026-09-14T02:35:24.416Z] TOOL RESULT

```
=== LKT 1929 ===
153
[Sskr.  srgäla.
XIV,  240/249;  mit  lautgeschichtlichen und  kulturhistorischen  Gründen  zurück- gewiesen von  Joseph  Schmidt,  A  persza saman  etymonja  in  Nyelvtudomänyi Közlemenyek  XLLV,  470/474.
1929.  Sskr.  srgäla:
T.anis  aureus,  Schakal',  ebenso  pers. säyäl,  tk.  sakal,  cakal;  hieraus  rum. ceacal,  it.  sciacallo,  afrz.  jachal,  frz. chacal;  engl,  jackal,  ndl.  jakhals [mit  volkselyinologischer  Umgestaltung], dtsch.  Schakal;  russ.  sakal,  cakal,  bulg. serb.  sakal,  cech.  sakal,  poln.  szakal 'Goldvvolt'.
1930.  Sskr.  sriig-avera;
'Ingwer,  Zingiber  olficinarum  Roscoe' [eigentlich  'horiiarlig' ;  so  sind  die  Wur- zeln des  braunen  oder  gemeinen  Ing- wers tatsächlich  beschaffen];  mit  Schwin- den des  vokalischen  r  wurde  ar.  zen- §ehll,  tk.  zingifre  sowie  gr.  Zi-fYißepn;, lat.  zingiber  und  hieraus:  iL  zenzovcro, zenzero,  gengioi-o,  aprov.  gingebre,  frz. gingembre,  kat.  gingebre,  sp.  gengibre, agengibre,  pg.  gengibre,  gengivre,  rum. ghimber,  zingifil,  zinzifil ;  ndl.  gemher, engl,  ginger,  dtsch.  Ingtver  [mit  Abwurf des  Anlautes  wie  bei  den  folgenden Formen];  russ.  im
leaf0   181 printed 155
=== HJB JACKAL ===
JACKAL.
Bvdkul;  some  of  the  first  are  so  Urge  as to  be  too  heavy  for  one  man  to  oarrv." — Oladto%n*t  Ayeet^  ii.  25.  In  Blochmann  s  ed. of  the  Persian  text  he  reads  larhalf  [and  so in  Jarrett's  trans,  (ii.  152).]  which  is  a  Hind, name  for  the  Ar(oearpu$  Lakoocha  of  Roxb.
1563.  —  "ii.  What  fruit  is  that  which  is as  big  as  the  largest  (coco)  nuts  ?
"  O.  You  just  now  ate  the  ekestuMU  from inside  of  it,  and  you  said  that  roasted  they were  like  real  chestnuts.  Now  you  shall  eat the  envelopes  of  these  .  .  .
"i2.  They  taste  like  a  melon;  but  not so  good  as  the  better  melons.
"0.  True.  And  owing  to  their  viscous nature  they  are  ill  to  digest ;  or  say  rather they  are  not  digested  at  all,  and  often  issue from  the  body  Q]iute  unchanged.  I  don't much  use  them.  They  are  calkd  in  Malavar jaoM  ;  in  CSanarin  and  Guzerati  pandt.  .  .  . The  tree  is  a  great  and  tall  one;  and  the fruits  ^row  from  the  wood  of  the  stem,  right up  to  it,  and  not  on  the  branches  like  other fruits." — Garei4ij  f.  111.
[1698.— "  A  certain  fruit  that  in  Malabar is  called  iaca,  in  Canara  and  Ousurate Panar  and  PamzM,  by  the  Arabians  Panax, by  the  Persians  Fanax," — Lintehoten,  Hak. Soc.  ii.  20.
[c.  1610.— "The  JaaaM  is  a  tree  of  the height  of  a  chestnut.  —Pymrrf  de  LavaX, Hak.  Soc.  ii.  366.
[1623.— "We  had  Zlaoche,  a  fruit  very rare  at  this  time."— P.  della  VcUU,  Hak. Soc.  ii.  264.]
1673.—"  Without  the  town  (Madras)  grows their  Rice  .  .  .  Jawks,  a  Coat  of  Armour over  it,  like  an  Hedg-hog's,  guards  its weighty  Fruit."— /Vy^r,  40.
1810.  —  "The  Jack-wood  ...  at  first yellow,  becomes  on  exposuro  to  the  air  of the  colour  of  mahogany,  and  is  of  as  fine a  grain." — Maria  Oraham,  101.
1878.— "The  monstrous  lack  that  in  its eccentric  bulk  contains  a  whole  magazine  of tastes  and  smells." — Ph.  Robinton,  In  My Indian  Garden,  49-50.
It  will  be  observed  that  the  older authorities  mention  two  varieties  of the  fruit  bv  the  names  of  shaki  and barkij  or  modifications  of  these,  different kinds  according  to  Jordanus,  only  from different  parts  of  the  tree  according  to Ibn  Batuta.  P.  Vincenzo  Maria  (1672) also  distinguishes  two  kinds,  one  of which  he  calls  G-iacha  Barca,  the  other Giacha  papa  or  girasole.  And  Rheede, the  great  authority  on  Malabar  plants, says  (iii.  19) :
```


## [2026-09-14T02:35:32.587Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"shagal\\|shaghal\\|shagāl\\|Canis aureus\\|chakal\" HJB.txt | head -10\necho \"=== AID ===\"; grep -n -i \"jackal\" AID.txt | head -5",
 "description": "Grep Hobson-Jobson and Whitworth for jackal"
}
```


### [2026-09-14T02:35:32.661Z] TOOL RESULT

```
=== AID ===
```


## [2026-09-14T02:35:40.394Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '31440,31455p' SNS.txt | cut -c1-200\necho \"--- 11160-11175\"; sed -n '11160,11178p' SNS.txt | cut -c1-200\necho \"--- total leaves:\"; grep -c $'\\f' SNS_pages.txt",
 "description": "Read SNS entries for srubēn"
}
```


### [2026-09-14T02:35:41.390Z] TOOL RESULT

```
srasg 183/19 
srSyiin 183/2 
srlt 186/20 
srOs 184/8 
srOl ahrav 184/15 
srOscarnam 184/21 
srCsOcarnaio 185/4 
srubSn 183/7-184/6 
srtld 134/17 



srfldan 184/19 
srflv 185/12 
-Stan 178/4 
stanSnd 332/2 
--- 11160-11175



^-ag^^^lyll^^'^'oW Uj- rsarmag: A~4>" 
L/ ^—(./^cjiUUo^^^^r-- 1 - 1 *" 15 -" 15 ^*-^*^ 1 - sard 

• n/T^-UiVt. 1566)sarata z fe» 
.ywt«^ . c^-tfLj- :sarmag I saxt: yooJ » v*-6^*» 

^oi*» •*£» ( srub + en: 



MY/T ^ 



,\ 

--- total leaves:
242
```


## [2026-09-14T02:35:57.142Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD sers ===\"; grep -n \"sers-\\|ser-2\\|^sers\" AHD_watkins1985.txt | head -5\necho \"=== AHD saw ===\"; grep -n -i \"\\bsaw\\b\" AHD_watkins1985.txt | head -5",
 "description": "Grep Watkins for sers root"
}
```


### [2026-09-14T02:35:57.298Z] TOOL RESULT

```
=== AHD sers ===
2211:SAMOVAR sem-1, wer-7 SAMPLE em- SAMSARA sem-1, ser-2 SANCTIFY sak- SANCTUM sak- SAND bhes-1 SAND-BLIND sémi- SANDHI dhé-1, sem-1 SANE sano- SANHEDRIN  sed-1 SANITARY sano- SANS sen-2 SANSKRIT k¥er-1, sem-1 SAP! sab-
2249:SEQUESTRUM sekw-1 SERAC ser-2 SERE! saus- SERENE ksero- SERF servus SERGEANT servus SERIES ser-3 SERIF skribh- SERIOUS swer-5 SERMON ser-3 SEROTINOUS sé@-2 SERPENT serp-2 SERPIGO serp-2 SERRIED ser-3 SERTULARIAN ser-3 SERUM ser-2 SERVAL_ ker-! SERVE servus SERVICE servus SERVILE servus SERVITUDE servus SESQUI- kwe, sémi- SESQUIPEDALIAN ped-! SESSILE sed-1 SESSION sed-1 SESTERCE sémi-, trei- SESTET s(w)eks SESTINA s(w)eks SET! sed-1 SETTLE sed-1 SEVEN septm SEVER pere-! SEVERAL pere-1 SEVERE WEér0- SEW syu-
2322:STRUDEL ser-2 STRUT  ster-1 STRUTHIOUS trozdo- STUB (s)teu- sTucco (s)teu- sTuD! sta-
=== AHD saw ===
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
914:sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
2219:SAW! sek-
```


## [2026-09-14T02:35:58.444Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/%C3%A7akal",
 "prompt": "Give the etymology of Turkish çakal: source language, Persian form, Sanskrit form, and first attestation date in Turkish."
}
```


### [2026-09-14T02:36:01.491Z] TOOL RESULT

```
I cannot provide the etymology information you requested based on the webpage content supplied. The page excerpt shown only displays the header and footer of the Nişanyan Sözlük (Nişanyan Dictionary) website, without any actual dictionary entry or etymological data for the word "çakal."

To obtain the etymology details you're seeking—including the source language, Persian form, Sanskrit form, and first attestation date—you would need to access the full dictionary entry for "çakal" on the Nişanyan Sözlük website directly.
```


## [2026-09-14T02:36:14.314Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D8%BA%D8%A7%D9%84' \\\n 'https://www.etymonline.com/word/jackal' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%A8' \\\n 'https://en.wiktionary.org/wiki/serra' \\\n 'https://en.wiktionary.org/wiki/%E1%BF%A5%CE%AF%CE%BD%CE%B7' \\\n 'https://abadis.ir/fatofa/%D8%B4%D8%BA%D8%A7%D9%84/' \\\n 'https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%A8/' \\\n 'https://abadis.ir/fatofa/%D8%A7%D8%B1%D9%87/' ; do\n timeout 180 python3 tools/fetch_source.py \"$u\" --note \"pdf page 473 (book 443) verification: Srgala/jackal, Srira/sir, Srisa/arreh-serra-rhine, Sru3-Srva2/sorb\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources used"
}
```


### [2026-09-14T02:36:27.723Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/87cca5a480ae63d7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7e576a061878b792.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f093cb94ee871d43.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30ee0f214830bf26.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2a6b8ba408b42d89.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e2d801b6cb3c515a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fda31486d257022a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/11de2a1c0eab099f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8cc02784a31bf5a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/98e95bd1d6ff0a10.txt
```


## [2026-09-14T02:36:30.430Z] TOOL CALL #65: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py",
 "description": "Read verify_check.py requirements"
}
```


### [2026-09-14T02:36:30.470Z] TOOL RESULT

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


## [2026-09-14T02:36:32.713Z] TOOL CALL #66: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py",
 "description": "Read rest of verify_check.py"
}
```


### [2026-09-14T02:36:32.787Z] TOOL RESULT

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


## [2026-09-14T02:36:43.686Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nSP=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nmkdir -p data/verification/sources/refs/ocr/BLY\ncp $SP/bly78-473.png data/verification/sources/refs/ocr/BLY/78.png\ncat > data/verification/sources/refs/ocr/BLY/78.vision.txt <<'EOF'\n[read from the page image by an Opus verification agent, 2026-09-13; BLY = H. W. Bailey,\n\"Hvatanica II\", BSOS 9 (1937) pp. 69-78 — p. 78, first entry of the page]\n\n78                          HVATANICA  II\n\nsira-, not to Av. srira, since sr > Khotan ss.  Cf. rather Mid. Pers.\n    sayr (ser), NPers. sir 'satiated'.\nhamgrita- to hamggalj, as haspalj-, haspriya-, and hamdriya-, darjs-.\nhamgris- as hamthris-.  [Iran. grab- had ptc. *grb-ta-, Baloci gipta,\n    NPers. girift, and *grb- before suffix in Av. garafs-.]\nhamgrautta- < *ham-grabita- (?).\nhaththa- < *hathya, certainly not *har(a)-stha-, which is found as\n    harstaya-.\n...\nEOF\nls -la data/verification/sources/refs/ocr/BLY/",
 "description": "Save Bailey p.78 vision text and page image"
}
```


### [2026-09-14T02:36:44.655Z] TOOL RESULT

```
total 216
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep 13 22:36 .
drwxrwxr-x 14 sfmqrb sfmqrb   4096 Sep 13 22:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb 207924 Sep 13 22:36 78.png
-rw-rw-r--  1 sfmqrb sfmqrb    637 Sep 13 22:36 78.vision.txt
```


## [2026-09-14T02:37:32.887Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:44:07.911Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-473.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 473,\n \"book_page\": 443,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Srgâla, Črğâla\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Sanskrit शृगाल (śṛgāla-) m. 'jackal, Canis aureus'\",\n \"note\": (\"The Sanskrit word is real and is the universally accepted ultimate source of the \"\n   \"Persian/Turkish/European jackal-words. Nourai's two headforms are one word: 'Srgâla' is the \"\n   \"s-transliteration and 'Črğâla' the palatal-ś transliteration of शृगाल. The gloss 'howler' is \"\n   \"Klein's (KLN:823 'lit. the howler'), an old connection with a root for 'cry out'; modern \"\n   \"Indo-Aryan scholarship treats śṛgāla- as of unclear, possibly non-IE (BMAC substrate) origin \"\n   \"and does not endorse 'howler' as an etymology, so the GLOSS is folk-etymological even though \"\n   \"the word and the descent chain are right. Nourai's own chart-note ('BQT:1270 indicates the \"\n   \"root may be from Babylonia') reproduces Mo'in's footnote reporting Purdavud's opinion that \"\n   \"šaġāl is a word of the land of Babylon; that is a minority view nobody follows today — the \"\n   \"Indo-Aryan origin is standard.\"),\n \"note_fa\": (\"ریشه در واقع واژهٔ سنسکریت शृगाल (śṛgāla-) «شغال» است؛ هر دو صورتی که نورایی آورده \"\n   \"(Srgâla / Črğâla) یک واژه‌اند و تنها در آوانگاری سایشی س و ش‌گونهٔ سنسکریت تفاوت دارند. معنای \"\n   \"«زوزه‌کش» که کلاین (KLN:823) داده ریشه‌شناسی عامیانه است؛ زبان‌شناسان امروز خاستگاه این واژهٔ \"\n   \"هندوآریایی را ناروشن و شاید برگرفته از زیرلایهٔ پیشاهندواروپایی (BMAC) می‌دانند. یادداشت خود \"\n   \"کتاب دربارهٔ «بابلی بودن» واژه، بازگفتِ حاشیهٔ معین در برهان قاطع (ص ۱۲۷۰) از نظر پورداود است \"\n   \"که امروز پذیرفته نیست. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.\"),\n \"sources\": [W+\"%D8%B4%D8%BA%D8%A7%D9%84\", \"https://www.etymonline.com/word/jackal\",\n             \"https://abadis.ir/fatofa/%D8%B4%D8%BA%D8%A7%D9%84/\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:823\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 vol. I p. 822/823 (KLN_1966.txt leaf 444, printed number 822 on the leaf), s.v. jackal: 'jackal, n. — Turk. chagal, fr. Pers. shaghal, fr. OI. srgalah, lit. ‘the howler’.' Exactly Nourai's root, its gloss and its chain.\"},\n   {\"ref\": \"MON:2050\", \"status\": \"partial\",\n    \"note\": \"Mo'in's entry for شغال (read at abadis.ir/fatofa/شغال) tags it '(شَ) [په.] (اِ.)' i.e. Pahlavi, and describes the animal; Mo'in gives the Pahlavi tag but not the Sanskrit etymon, and the 6-vol page numbering cannot be checked online.\"},\n   {\"ref\": \"BQT:1270\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' p. 1270 (fetched with tools/ref_page.py BQT:1270 --image), Mo'in's footnote 1 under شغال: 'از سانسکریت śṛgāla (شغال)، پهلوی šagāl … ترکی چاقال … این کلمه از ترکی وارد زبانهای اروپایی شده: آلمانی Schakal، فرانسوی chacal، انگلیسی jackal. آقای پورداود کلمهٔ «شغال» را لغت سرزمین بابل دانسته‌اند، «هاب» ص ۲۱۸.' — both the chain and the Babylonia remark that Nourai's chart-note reports.\"}],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1929, p. ~155 (LKT.txt leaf 181)\", \"stance\": \"supports\",\n    \"note\": \"'1929. Sskr. srgäla: Canis aureus, Schakal', ebenso pers. šaγāl, tk. sakal, çakal; hieraus rum. ceacal, it. sciacallo, afrz. jachal, frz. chacal; engl. jackal, ndl. jakhals …, dtsch. Schakal'\"},\n   {\"src\": \"KLN\", \"where\": \"vol. I p. 823 s.v. jackal\", \"stance\": \"supports\",\n    \"note\": \"'Turk. chagal, fr. Pers. shaghal, fr. OI. srgalah, lit. ‘the howler’'\"},\n   {\"src\": \"BQT\", \"where\": \"p. 1270, Mo'in's footnote 1 s.v. شغال\", \"stance\": \"supports\",\n    \"note\": \"'از سانسکریت śṛgāla (شغال)، پهلوی šagāl' — same etymon, same route\"},\n   {\"src\": \"AID\", \"where\": \"AID.txt, grep -i jackal\", \"stance\": \"silent\",\n    \"note\": \"Whitworth's Anglo-Indian Dictionary has no jackal entry in the OCR\"}],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"šağâl\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Middle Persian šgʾl / šγʾl, read šaγāl 'jackal', is a Middle Iranian loan from \"\n   \"Old Indo-Aryan śṛgāla- taken over in the Sasanian period through the Indo-Iranian frontier \"\n   \"contact that also gave MP šatrang 'chess' and many animal names. Indic ś- is rendered by MP \"\n   \"š-, and the Indic vocalic ṛ is resolved as a (śṛ- > ša-), exactly as in other Indic loans; \"\n   \"the ending -āla is kept unchanged. Mo'in's footnote in Borhan p. 1270 states the Pahlavi form \"\n   \"explicitly ('پهلوی šagāl'), and Wiktionary's Persian entry likewise derives the modern word \"\n   \"'from Middle Persian (šγal /šaγāl/), borrowed from Sanskrit (sṛgālá)'. The gloss 'coyote' is \"\n   \"Nourai's Americanism for the jackal Canis aureus; no coyote exists in Iran.\"),\n \"derivation_fa\": (\"فارسی میانه šaγāl (نوشتهٔ šgʾl) «شغال» وام‌واژه‌ای است از هندی باستان śṛgāla- \"\n   \"که در دورهٔ ساسانی از راه داد و ستد با هند به ایران رسیده است؛ ش هندی به ش فارسی میانه بدل شده \"\n   \"و ــرِ واکه‌ای سنسکریت (ṛ) به «شَـ» گشوده شده است. حاشیهٔ معین در برهان قاطع (ص ۱۲۷۰) همین \"\n   \"صورت پهلوی را می‌آورد و ویکی‌واژه نیز آن را تأیید می‌کند. گزارش نورایی درست است؛ تنها «coyote» \"\n   \"در ترجمهٔ او آمریکایی‌مآبانه است و منظور همان Canis aureus است.\"),\n \"sources\": [W+\"%D8%B4%D8%BA%D8%A7%D9%84\", \"https://abadis.ir/fatofa/%D8%B4%D8%BA%D8%A7%D9%84/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2050\", \"status\": \"supports\",\n    \"note\": \"Mo'in marks شغال '[په.]' = Pahlavi (abadis.ir/fatofa/شغال, فرهنگ معین section); that is precisely the Sanskrit→Pahlavi step Nourai draws, though Mo'in's own page number is unverifiable online.\"}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"p. 1270 fn. 1 (ref_page.py BQT:1270)\", \"stance\": \"supports\",\n    \"note\": \"'از سانسکریت śṛgāla (شغال)، پهلوی šagāl'\"},\n   {\"src\": \"PHD\", \"where\": \"PHD.txt, grep 'šagāl'/'sgl'\", \"stance\": \"silent\",\n    \"note\": \"MacKenzie's Concise Pahlavi Dictionary has no entry for the jackal word (not attested in the Book Pahlavi corpus he excerpts)\"},\n   {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt\", \"stance\": \"silent\",\n    \"note\": \"Nyberg's glossary (Škand/KārNāmag texts) has no šagāl\"}]})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"šağâl, šoğâl «شغال»\", \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian شغال šaġāl/šoġāl continues MP šaγāl unchanged apart from the ordinary \"\n   \"NP raising of unstressed a to o in the first syllable (šaġāl > šoġāl, as in ثواب/خُدا-type \"\n   \"variation); the by-forms Nourai prints, شکال šakāl and شگال šagāl, are the older spellings with \"\n   \"unspirantized k/g and are attested in classical Persian (Dehkhoda lists شکال، شگال، شال). The \"\n   \"form with غ is the one that spread. Persian is the immediate donor to Ottoman Turkish.\"),\n \"derivation_fa\": (\"«شغال» در فارسی نو دنبالهٔ مستقیم فارسی میانهٔ šaγāl است؛ دگرگونی تنها در \"\n   \"واکهٔ نخست است (šaγāl > šoγāl). صورت‌های کهن‌ترِ «شکال» و «شگال» که نورایی هم آورده در متون \"\n   \"کلاسیک آمده‌اند و دهخدا آن‌ها را همراه «شال» ثبت کرده است؛ اینها همان واژه با کاف/گافِ \"\n   \"سایشی‌نشده‌اند. فارسی خود وام‌دهندهٔ ترکی عثمانی است. ادعای نورایی درست است.\"),\n \"sources\": [W+\"%D8%B4%D8%BA%D8%A7%D9%84\", \"https://abadis.ir/fatofa/%D8%B4%D8%BA%D8%A7%D9%84/\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:823\", \"status\": \"supports\",\n    \"note\": \"Klein p. 823 s.v. jackal: 'Turk. chagal, fr. Pers. shaghal' — Persian is the source of the Turkish word, as drawn.\"}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"p. 1270 headword شغال + fn. 1\", \"stance\": \"supports\",\n    \"note\": \"the Borhan entry 'شغال … جانوری است معروف' with Mo'in's note deriving it from Sanskrit via Pahlavi and passing it on to Turkish\"},\n   {\"src\": \"MON\", \"where\": \"فرهنگ معین s.v. شغال (via abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"'(شَ) [په.] (اِ.) جانوری است پستاندار از راستهٔ گوشت‌خواران شبیه به سگ' — Pahlavi origin tag\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1929\", \"stance\": \"supports\",\n    \"note\": \"'ebenso pers. šaγāl, tk. sakal, çakal'\"}]})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Turkish\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": (\"The empty pass-through box stands for Ottoman Turkish چقال çakal (modern Turkish \"\n   \"çakal) 'jackal', borrowed from Persian شغال. Turkish has no /ʃ/ ~ /tʃ/ constraint here, but the \"\n   \"loan was re-shaped with initial č- and the Persian غ /ɣ/ was dropped between vowels (šaġāl > \"\n   \"čaqal > çakal); Lokotsch no. 1929 lists the two Turkish variants 'tk. sakal, çakal' side by \"\n   \"side, which shows the substitution in progress. Turkish, as the language of the Ottoman \"\n   \"Mediterranean, is the donor to all the European forms.\"),\n \"derivation_fa\": (\"این خانهٔ خالی نمایندهٔ ترکی عثمانی «چقال» (ترکی امروز çakal) است که از فارسی \"\n   \"«شغال» وام گرفته شده. در گذر به ترکی، «ش» آغازین به «چ» بدل شده و «غ» میان‌واکه‌ای افتاده است \"\n   \"(šaγāl > čaqal). لوکوچ (شمارهٔ ۱۹۲۹) هر دو صورت ترکی sakal و çakal را کنار هم آورده که همین \"\n   \"جانشینی را نشان می‌دهد. ترکی عثمانی همان زبانی است که واژه را به اروپا رسانده. درست است.\"),\n \"sources\": [W+\"%D8%B4%D8%BA%D8%A7%D9%84\", \"https://www.etymonline.com/word/jackal\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives no reference on this pass-through node; the claim is covered by KLN:823 on the neighbouring boxes.\"}],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1929, p. ~155\", \"stance\": \"supports\",\n    \"note\": \"'pers. šaγāl, tk. sakal, çakal; hieraus rum. ceacal, it. sciacallo … frz. chacal; engl. jackal'\"},\n   {\"src\": \"TTS\", \"where\": \"TTS_pages.txt, grep 'schakal/čakal'\", \"stance\": \"silent\",\n    \"note\": \"Vámbéry's Turko-Tatar etymological dictionary has no jackal entry in the OCR (he excludes obvious Persian loans)\"},\n   {\"src\": \"KLN\", \"where\": \"vol. I p. 823\", \"stance\": \"supports\",\n    \"note\": \"'Turk. chagal, fr. Pers. shaghal'\"}]})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"jackal\", \"verdict\": \"confirmed\",\n \"derivation\": (\"English jackal is first recorded c. 1600 and comes, as Etymonline sets out, from \"\n   \"French chacal (16th-17th c., earlier jackal) < Turkish çakal; the English initial j- reflects \"\n   \"the older French/travellers' spelling jackal rather than modern chacal, and the -al was later \"\n   \"assimilated to the English name Jack (whence the Dutch folk-etymological jakhals 'jack-neck'). \"\n   \"Klein telescopes the chain to 'Turk. chagal' without the French stage, which is what Nourai's \"\n   \"Turkish → English arrow reproduces; the French intermediary is the only refinement modern \"\n   \"sources add. The figurative 'skulking henchman' sense rests on the old belief that the jackal \"\n   \"roused game for the lion.\"),\n \"derivation_fa\": (\"انگلیسی jackal نخستین بار حدود سال ۱۶۰۰ میلادی ثبت شده و از فرانسوی chacal \"\n   \"(صورت کهن‌تر jackal) گرفته شده که خود از ترکی çakal است؛ «ج» آغازینِ انگلیسی بازتاب املای \"\n   \"کهن فرانسوی است. کلاین (ص ۸۲۳) میانجی فرانسوی را حذف کرده و یکراست از ترکی می‌آورد و نمودار \"\n   \"نورایی هم همین را بازتاب می‌دهد؛ تنها افزودهٔ پژوهش امروزی همان مرحلهٔ فرانسوی است. پس ادعای \"\n   \"نورایی درست، اما اندکی خلاصه‌شده است.\"),\n \"sources\": [\"https://www.etymonline.com/word/jackal\", W+\"%D8%B4%D8%BA%D8%A7%D9%84\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:823\", \"status\": \"supports\",\n    \"note\": \"Klein vol. I p. 823: 'jackal, n. — Turk. chagal, fr. Pers. shaghal, fr. OI. srgalah' — Turkish → English exactly as the arrow is drawn.\"}],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1929\", \"stance\": \"partial\",\n    \"note\": \"'afrz. jachal, frz. chacal; engl. jackal' — Lokotsch inserts (Old) French between Turkish and English\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt, grep '^JACKAL'\", \"stance\": \"silent\",\n    \"note\": \"Skeat's Concise has no jackal headword in the OCR\"},\n   {\"src\": \"HJB\", \"where\": \"HJB.txt\", \"stance\": \"silent\",\n    \"note\": \"the OCR of Hobson-Jobson yields only a running-head 'JACKAL.' with jack-fruit text; no usable entry\"}]})\n\ndata[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Srîra\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"Avestan srīra- adj. 'beautiful, fair to look on' (PIE *ḱrey- 'to appear, shine'); NOT 'satisfied'\",\n \"note\": (\"Two things are wrong here, and Nourai's own source says so. (1) The gloss: Avestan \"\n   \"srīra- means 'beautiful', not 'satisfied'. Bartholomae, AiW (BRT.txt s.v. srira-) defines it \"\n   \"'Adj. (fem. -iiā-) 1) schön anzusehen, schön', with comparative sraiiah- and superlative \"\n   \"sraēšta-; Pokorny puts it under Root/lemma *ḱrei- 'to appear, show oneself', Page(s): 618, with \"\n   \"'Avestan srira- ‘beautiful’, Kompar. … Avestan srayah-, Superl. … Avestan sraesta-' — \"\n   \"which is exactly what Nourai's own chart-note records ('Avestan srîra was found in POK:618 with \"\n   \"the meaning of pretty'), yet he kept 'satisfied' in the root box anyway. (2) The derivation: the \"\n   \"single reference he cites, Bailey BLY:78, says the OPPOSITE of his arrow. Its first line reads \"\n   \"'sīra-, not to Av. srīra, since śr > Khotan ṣṣ. Cf. rather Mid. Pers. saγr (sēr), NPers. sīr \"\n   \"‘satiated’.' Bailey is refusing to connect the 'satiated' word with Av. srīra- on a \"\n   \"sound-law argument, and Nourai has read the sentence backwards. The real history of Persian سیر \"\n   \"is MP sagr (Pāzand/NP sēr) < *sagra-, with the regular south-western change -agr- > -ēr- that \"\n   \"Nyberg states in so many words; Av. srīra- is out of the picture.\"),\n \"note_fa\": (\"این ریشه دو خطا دارد و منبعِ خود نورایی هر دو را آشکار می‌کند. نخست معنا: اوستایی \"\n   \"srīra- به معنی «زیبا، خوش‌منظر» است نه «سیر»؛ بارتولومه در «فرهنگ ایرانی باستان» آن را \"\n   \"'schön anzusehen, schön' معنی کرده و پوکورنی (ص ۶۱۸) آن را زیر ریشهٔ *ḱrei- «نمایان شدن، \"\n   \"درخشیدن» آورده است — همان که خودِ یادداشت نورایی در نمودار به آن اشاره می‌کند ولی در خانهٔ \"\n   \"ریشه اصلاحش نکرده است. دوم خودِ اشتقاق: بیلی در «هواتانیکا ۲» ص ۷۸ سطر نخست می‌نویسد \"\n   \"«sīra-, not to Av. srīra … Cf. rather Mid. Pers. saγr (sēr), NPers. sīr ‘satiated’»، یعنی \"\n   \"به صراحت پیوند این واژه را با srīra- اوستایی رد می‌کند. تاریخ درست «سیر» این است: فارسی \"\n   \"میانه sagr (پازند/فارسی نو sēr) از ایرانی *sagra-، با دگرگونی آواییِ قاعده‌مندِ جنوب‌غربی \"\n   \"-agr- > -ēr- که نیبرگ آن را «قانون عمومی جنوب‌غربی» می‌نامد. بنابراین پژوهش امروزی ادعای \"\n   \"نورایی را رد می‌کند.\"),\n \"sources\": [W+\"%D8%B3%DB%8C%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BLY:78\", \"status\": \"contradicts\",\n    \"note\": \"Bailey, 'Hvatanica II', BSOS 9 (1937) p. 78, first line, read from the page image (saved as data/verification/sources/refs/ocr/BLY/78.png and 78.vision.txt): 'sīra-, not to Av. srīra, since śr > Khotan ṣṣ. Cf. rather Mid. Pers. saγr (sēr), NPers. sīr ‘satiated’.' The page denies the very link the root box asserts.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW s.v. srira- (BRT.txt line 27427, col. ~1647)\", \"stance\": \"contradicts\",\n    \"note\": \"'j., g. srira- Adj. (fem. -iā-) 1) ‘schön anzusehen, schön’; a) vom schönen Äussern der Menschen und Götter …' — 'beautiful', never 'satisfied'\"},\n   {\"src\": \"POK\", \"where\": \"IEW p. 618, Root/lemma *ḱrei- 'to appear, show oneself'\", \"stance\": \"contradicts\",\n    \"note\": \"'Old Indie srī- ‘beauty, splendor’, Avestan srī- ‘beauty’, Old Indie srīla- ‘beautiful’ …, Avestan srīra- ‘beautiful’, Kompar. … Avestan srayah-, Superl. … Avestan sraesta-' (POK_full.txt, block ending 'Page(s):618')\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. sagr\", \"stance\": \"contradicts\",\n    \"note\": \"'sagr [sgl] (sēr) satiated, satisfied 86². — Ps. sgly; Paz. NP sēr; -ayr- > -ēr- according to the common SW law, cf. šēr.' The Persian word goes back to sagr, not to Av. srīra-\"}],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"sěr\", \"verdict\": \"disputed\",\n \"derivation\": (\"The Middle Persian word is real but its citation form and its ancestry are both \"\n   \"misstated. MacKenzie gives 'sagr [sgl | N sēr] sated, satiate'; Nyberg gives 'sagr [sgl] (sēr) \"\n   \"satiated, satisfied (Škand 86²) — Ps. sgly; Paz. NP sēr; -aγr- > -ēr- according to the common \"\n   \"SW law, cf. šēr [‘lion’ < *šagr]'. So the Book-Pahlavi spelling is sgl, transcribed \"\n   \"sagr, and sēr is the later (Pāzand/New Persian) pronunciation reached by the south-western \"\n   \"development -agr- > -ēr-, the same change that turns *šagr into šēr 'lion'. Nourai's 'sěr' is \"\n   \"therefore the Pāzand reading offered as the Pahlavi form. More seriously, the arrow from \"\n   \"Avestan srīra- cannot stand: Bailey (the very page cited) rejects it because Indo-Iranian śr- \"\n   \"would have to give Khotanese ṣṣ-, and Av. srīra- in any case means 'beautiful'. MP sagr goes \"\n   \"back to an Iranian *sagra-, unconnected with srīra-.\"),\n \"derivation_fa\": (\"واژهٔ فارسی میانه هست، اما هم صورتِ آن و هم نیای آن نادرست گزارش شده است. \"\n   \"مکنزی می‌نویسد «sagr [sgl | فارسی نو sēr] سیر، سیراب» و نیبرگ نیز «sagr [sgl] (sēr)» را ثبت \"\n   \"کرده و می‌افزاید که ــagrــ در فارسی میانهٔ جنوب‌غربی به ــērــ بدل می‌شود، همان‌گونه که \"\n   \"*šagr به šēr «شیر» بدل شده است. پس نوشتار پهلوی sgl = sagr است و «سِر/sēr» تلفظ پازند و \"\n   \"فارسی نو است، نه صورت اصلی پهلوی. مهم‌تر آنکه پیکانِ «از اوستایی srīra-» پذیرفتنی نیست: \"\n   \"بیلی در همان صفحه‌ای که نورایی به آن ارجاع داده این پیوند را با استدلال آوایی رد کرده است. \"\n   \"بنابراین: پژوهش امروزی این حلقه را رد می‌کند و sagr را از ایرانی *sagra- می‌داند.\"),\n \"sources\": [W+\"%D8%B3%DB%8C%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BLY:78\", \"status\": \"contradicts\",\n    \"note\": \"p. 78 line 1: 'sīra-, not to Av. srīra, since śr > Khotan ṣṣ. Cf. rather Mid. Pers. saγr (sēr), NPers. sīr ‘satiated’.' Bailey supports MP saγr/sēr ~ NPers. sīr but explicitly denies the Avestan srīra- parentage drawn here.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"A Concise Pahlavi Dictionary p. 74 s.v. sagr (PHD.txt leaf 562 block)\", \"stance\": \"partial\",\n    \"note\": \"'sagr [sgl | N sēr] sated, satiate. ~ih: satiety.' — the word exists, but the head form is sagr and MacKenzie gives no Avestan antecedent\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. sagr / sagrēh\", \"stance\": \"contradicts\",\n    \"note\": \"'sagr [sgl] (sēr) satiated, satisfied 86². — Ps. sgly; Paz. NP sēr; -ayr- > -ēr- according to the common SW law, cf. šēr.' No srīra-\"},\n   {\"src\": \"BRT\", \"where\": \"AiW s.v. srira-\", \"stance\": \"contradicts\",\n    \"note\": \"Av. srira- is 'schön anzusehen, schön', with no 'sated' sense anywhere in the entry\"}]})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"sîr «سیر»\", \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian سیر sēr/sir 'sated, no longer hungry, full' is the regular continuation \"\n   \"of MP sagr: the SW Iranian development -aγr-/-agr- > -ēr- (Nyberg's 'common SW law') gives \"\n   \"Pāzand sēr, and classical NP ē merges with ī in the modern standard, whence today's sir. Bailey \"\n   \"himself pairs 'Mid. Pers. saγr (sēr), NPers. sīr ‘satiated’' in the line Nourai cites, so \"\n   \"the Pahlavi → Persian arrow (unlike the one above it) is right. The extra form Nourai prints, \"\n   \"سیراب sīr-āb, is the transparent compound sīr + āb 'sated with water, watered', and the \"\n   \"'dark (of colours)' sense of سیر is a later metaphorical extension ('saturated'). This سیر is \"\n   \"homonymous with, but unrelated to, سیر 'garlic' and the Arabic loan سیر sayr 'journey'.\"),\n \"derivation_fa\": (\"«سیر» فارسی نو دنبالهٔ قاعده‌مند sagr فارسی میانه است: ــagrــ در فارسی میانهٔ \"\n   \"جنوب‌غربی به ــērــ بدل می‌شود (قانونی که نیبرگ آن را «قانون عمومی جنوب‌غربی» می‌خواند) و \"\n   \"«ای کشیدهٔ» فارسی میانه در فارسی امروز به «ای» تبدیل شده است. بیلی در همان سطر، «فارسی میانه \"\n   \"saγr (sēr)» و «فارسی نو sīr» را کنار هم آورده؛ پس این حلقه — برخلاف حلقهٔ بالای آن — درست \"\n   \"است. «سیراب» که نورایی افزوده ترکیب روشنِ سیر + آب است، و معنی «تیره» برای رنگ‌ها گسترش \"\n   \"استعاری همین «اشباع» است. این «سیر» با «سیرِ» خوراکی و «سَیرِ» عربی هم‌آواست ولی هم‌ریشه نیست.\"),\n \"sources\": [W+\"%D8%B3%DB%8C%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BLY:78\", \"status\": \"supports\",\n    \"note\": \"p. 78 line 1: '… Cf. rather Mid. Pers. saγr (sēr), NPers. sīr ‘satiated’' — Bailey's own pairing of the Middle and New Persian forms, i.e. exactly this arrow.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 74 s.v. sagr\", \"stance\": \"supports\",\n    \"note\": \"'sagr [sgl | N sēr] sated, satiate' — MacKenzie himself equates the MP word with NP sēr\"},\n   {\"src\": \"NYB\", \"where\": \"glossary s.v. sagr\", \"stance\": \"supports\",\n    \"note\": \"'Paz. NP sēr; -ayr- > -ēr- according to the common SW law' — the sound law that produces the New Persian form\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss, grep 'sīr/satt'\", \"stance\": \"silent\",\n    \"note\": \"Horn has no numbered entry for سیر 'sated' in the OCR (only an incidental 'satt wurde' in a Shahnama translation, p. XVI)\"},\n   {\"src\": \"MON\", \"where\": \"Wiktionary's Persian entry (Etymology 1)\", \"stance\": \"partial\",\n    \"note\": \"Wiktionary gives only 'Cognate with Northern Kurdish têr' and no Avestan antecedent — the Kurdish t- / Persian s- pair again points to *sagra-, not to srīra-\"}]})\n\ndata[\"entries\"].append(e1)\n\n# ---------------------------------------------------------------- entry 2\ne2 = {\n \"entry\": 2,\n \"root\": \"Srisâ, Srisnâ\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *sers- 'to cut off' (de Vaan, EDL p. 558); Mann's *srisā-, *srisnā- 'file, saw' is his own reconstruction\",\n \"note\": (\"The root box is a faithful copy of Mann, IEC p. 1277 (verified: IEC.txt leaf 705 carries \"\n   \"the printed page number 1277 and reads 'srisà, srisnà ‘file, saw’. (onomat.) Per. arrah, \"\n   \"id.; Oss. xirx, Dig. xirxá, s. ‘saw’; Kurd. ere, id.; Gk. [rhinē] f. ‘file’; Lat. \"\n   \"serra, f. ‘saw’'). The family is therefore Mann's, and Mann himself marks it \"\n   \"'(onomat.)', i.e. he is not claiming a well-founded inherited root. Pokorny has no such root and \"\n   \"Watkins/AHD has no such entry (grep of AHD_watkins1985.txt finds no *sers-; SAW is under *sek-, \"\n   \"SERRIED under *ser-3, an unrelated word). Ernout-Meillet s.v. serra call it 'terme technique \"\n   \"sans étymologie claire'. The one modern authority that does reconstruct a root is de Vaan, \"\n   \"EDL p. 558: Latin serra < Proto-Italic *serzā < PIE *sers-eh₂, to a root *sers- 'to cut off' — \"\n   \"which is compatible in substance with Nourai/Mann but differently shaped (*sers-, not *srisā-). \"\n   \"Hence 'plausible': the word-family is genuine, the reconstructed root-form is not the standard \"\n   \"one. NB a gloss slip that is the book's own, not the extraction's: the printed page (checked \"\n   \"against the page image) glosses Latin serra as 'file' and Greek rhinē as 'file', but serra is \"\n   \"'saw' and only rhinē is 'file' — Mann's own line has 'Lat. serra, f. ‘saw’'.\"),\n \"note_fa\": (\"خانهٔ ریشه رونوشت وفادارِ مان (IEC ص ۱۲۷۷) است؛ در همان صفحه آمده: «srisà, srisnà \"\n   \"‘file, saw’. (onomat.) Per. arrah … Oss. xirx … Kurd. ere … Gk. rhinē … Lat. serra». خودِ مان \"\n   \"آن را «(onomat.)» یعنی آوایی/نام‌آوا نشان کرده و مدعی ریشه‌ای استوار نیست. پوکورنی چنین ریشه‌ای \"\n   \"ندارد، واتکینز (AHD) نیز؛ و ارنو-مییه دربارهٔ serra می‌نویسد «اصطلاحی فنی بدون ریشه‌شناسی \"\n   \"روشن». تنها منبع امروزی که ریشه‌ای بازسازی می‌کند دُ وان است (EDL ص ۵۵۸): لاتینی serra از \"\n   \"ایتالیایی آغازین *serzā و آن از هندواروپایی *sers-eh₂ از ریشهٔ *sers- «بریدن». پس خانوادهٔ \"\n   \"واژگانی راست است ولی صورتِ بازسازی‌شدهٔ نورایی/مان صورت پذیرفتهٔ امروزی نیست: «با احتیاط \"\n   \"پذیرفتنی است». نکتهٔ دیگر، خطای معنایی در خودِ کتاب (نه در خوانش اسکن) است: serra لاتین «ارّه» \"\n   \"است نه «سوهان»؛ تنها rhinē یونانی «سوهان» است.\"),\n \"sources\": [W+\"serra\", W+\"%D8%A7%D8%B1%D9%87\", W+\"%E1%BF%A5%CE%AF%CE%BD%CE%B7\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:1277\", \"status\": \"supports\",\n    \"note\": \"Mann, IEC p. 1277 (IEC.txt line 17092; the \\\\f-block containing it prints '1277'): 'srisà, srisnà ‘file, saw’. (onomat.) Per. arrah, id.; Oss. xirx, Dig. xirxá, s. ‘saw’; Kurd. ere, id.; Gk. [rhinē] f. ‘file’; Lat. serra, f. ‘saw’. (Phonol. of cerrus & Plautine terr ‘3 times’, cf. terni, cerno, etc.)' — the root, its gloss and all three daughter boxes come from this one line.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'serra'\", \"stance\": \"silent\",\n    \"note\": \"Pokorny has no root for Latin serra; the only hit is 'Latin sarracum, serracum' (a wagon) under an unrelated lemma\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and body\", \"stance\": \"silent\",\n    \"note\": \"no *sers- root; 'SAW! sek-', 'SERRIED ser-3' (= Lat. sera 'bar') — Watkins gives serra no Indo-European root at all\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. serra (LAT.txt line 57766 ff.)\", \"stance\": \"partial\",\n    \"note\": \"'serra, -ae f.: 1° scie (outil) … Ancien, technique. … Terme technique sans étymologie claire. V. sarpō, et sera.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 9.68 LEAD / 9.6x tools\", \"stance\": \"silent\",\n    \"note\": \"Buck's synonym list has no 'saw' concept section, so nothing to compare\"}],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"arreh «ارّه»\", \"verdict\": \"plausible\",\n \"derivation\": (\"Persian ارّه arre 'saw' is genuinely the Iranian member of this family. The \"\n   \"derivation runs PIE *sers- (de Vaan) > Proto-Iranian *harsa-/*harra- — PIE initial *s- \"\n   \"regularly becomes Iranian h- — > *harra- > Middle Persian *arrag with the ordinary New \"\n   \"Persian/late MP loss of initial h-, whence NP arre with its geminate -rr- (which is why the \"\n   \"word is written with tašdīd, ارّه). The h- is still there in the neighbouring languages: \"\n   \"Mazanderani هره hare, Baluchi ہرگ harrag (with the -ag suffix that MP *arrag also had), beside \"\n   \"Kurdish ere and Ossetic xyrx / Digor xirxá cited by Mann. Two cautions keep this at 'plausible' \"\n   \"rather than 'confirmed': Wiktionary's Persian entry, which gives this PIE derivation, cites \"\n   \"Nourai p. 443 — this very chart — as its reference, so it is not an independent witness; and \"\n   \"neither Horn nor Hübschmann nor MacKenzie has the word, so there is no Old/Middle Iranian \"\n   \"attestation to anchor it. Mo'in and Dehkhoda record the word from Ferdowsi onward but give no \"\n   \"etymology.\"),\n \"derivation_fa\": (\"«ارّه» به‌راستی عضو ایرانیِ این خانواده است. مسیر چنین است: هندواروپایی *sers- \"\n   \"«بریدن» > ایرانی باستان *harsa-/*harra- (زیرا «س» آغازینِ هندواروپایی در ایرانی به «ه» بدل \"\n   \"می‌شود) > فارسی میانه *arrag با افتادن «ه» آغازین > فارسی نو «ارّه» با رای مشدد. «ه» آغازین \"\n   \"هنوز در گویش‌های همسایه مانده است: مازندرانی «هره» hare و بلوچی harrag؛ کردی ere و آسی xyrx \"\n   \"نیز که مان آورده هم‌ریشه‌اند. دو نکته سبب می‌شود حکم را «با احتیاط پذیرفتنی» بدانیم: نخست \"\n   \"آنکه ویکی‌واژه که همین اشتقاق را می‌دهد، منبعش خودِ همین صفحهٔ نورایی (ص ۴۴۳) است و شاهد \"\n   \"مستقلی نیست؛ دوم آنکه نه هرن، نه هوبشمان و نه مکنزی این واژه را ندارند و صورت ایرانی کهنی \"\n   \"برای آن گواهی نشده است. معین و دهخدا واژه را از فردوسی به بعد ثبت کرده‌اند ولی ریشه‌ای \"\n   \"نداده‌اند.\"),\n \"sources\": [W+\"%D8%A7%D8%B1%D9%87\", W+\"serra\", \"https://abadis.ir/fatofa/%D8%A7%D8%B1%D9%87/\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:1277\", \"status\": \"supports\",\n    \"note\": \"Mann p. 1277 lists 'Per. arrah, id.' as the first witness of *srisā, *srisnā 'file, saw' — exactly the arrow drawn.\"},\n   {\"ref\": \"MON:209\", \"status\": \"partial\",\n    \"note\": \"Mo'in's اره entry (read at abadis.ir/fatofa/اره, فرهنگ معین section) gives '(اَ رِ) (اِ.) ابزاری است برای بریدن چوب یا فلز …' — the word and gloss, but no etymological tag and no Indo-European root; the 6-vol page number cannot be checked online.\"}],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie, grep 'arra/Säge'\", \"stance\": \"silent\",\n    \"note\": \"Horn has no entry for arre 'saw'\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien, grep 'Säge'\", \"stance\": \"silent\",\n    \"note\": \"Hübschmann has no entry for the word either\"},\n   {\"src\": \"PHD\", \"where\": \"PHD.txt, grep 'arrag' and English index 'saw'\", \"stance\": \"silent\",\n    \"note\": \"MacKenzie has no Middle Persian *arrag; the word is unattested in Book Pahlavi\"},\n   {\"src\": \"MON\", \"where\": \"فرهنگ معین / لغت‌نامهٔ دهخدا s.v. اره (abadis.ir)\", \"stance\": \"partial\",\n    \"note\": \"both record اره 'saw' with classical citations from Ferdowsi, neither gives an etymology\"}]})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Latin\", \"words\": \"serra\", \"verdict\": \"plausible\",\n \"derivation\": (\"Latin serra is 'a saw' (and by extension the sawfish, and a saw-toothed battle \"\n   \"line) — Nourai's gloss 'file' is a slip of the book, since Mann's own line, from which the box \"\n   \"is copied, reads 'Lat. serra, f. ‘saw’'. On the derivation, opinions split. Klein \"\n   \"(p. 1424) says flatly 'L., ‘a saw’, of uncertain origin'; Ernout-Meillet call it a \"\n   \"'terme technique sans étymologie claire'; de Vaan (EDL p. 558) does give it a pedigree, \"\n   \"Proto-Italic *serzā < PIE *sers-eh₂ to *sers- 'to cut off', with Schrijver's sarriō 'to hoe' as \"\n   \"a zero-grade of the same root — the *-rs- > -rr- assimilation being the regular Latin outcome, \"\n   \"which is what makes the geminate of serra and of Persian arre match. Nourai's root-shape \"\n   \"*srisā-/*srisnā- is Mann's, not de Vaan's, so the Latin word belongs to the family but not \"\n   \"quite by the route the chart draws. Celtic *serrā 'sickle' is kept separate by Wiktionary.\"),\n \"derivation_fa\": (\"لاتینی serra «ارّه» است (و به گسترش، ماهی اره و آرایش دندانه‌دار جنگی)؛ معنیِ \"\n   \"«سوهان» که نورایی نوشته لغزش خودِ کتاب است، زیرا سطر مان که خانه از آن رونویسی شده «Lat. serra, \"\n   \"f. ‘saw’» دارد. دربارهٔ ریشه، دیدگاه‌ها یکسان نیست: کلاین (ص ۱۴۲۴) می‌نویسد «از لاتینی serra \"\n   \"«ارّه»، با خاستگاه نامعلوم» و ارنو-مییه نیز آن را بی‌ریشه‌شناسی روشن می‌دانند؛ اما دُ وان \"\n   \"(EDL ص ۵۵۸) آن را از ایتالیایی آغازین *serzā و هندواروپایی *sers-eh₂ از ریشهٔ *sers- «بریدن» \"\n   \"می‌آورد؛ همگونیِ ــrsــ به ــrrــ در لاتین قاعده‌مند است و همین «رای مشدد» را در «ارّهٔ» فارسی \"\n   \"نیز توضیح می‌دهد. پس این واژه به همین خانواده تعلق دارد ولی نه دقیقاً با صورتِ ریشه‌ای که \"\n   \"نورایی (به پیروی مان) رسم کرده است.\"),\n \"sources\": [W+\"serra\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:1277\", \"status\": \"partial\",\n    \"note\": \"Mann p. 1277 does list 'Lat. serra, f. ‘saw’' under srisà/srisnà — the arrow is Mann's — but Mann glosses it 'saw', not 'file' as the chart box does.\"}],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. serra\", \"stance\": \"contradicts\",\n    \"note\": \"'serra, -ae f.: 1° scie (outil) … Terme technique sans étymologie claire.' — no IE root admitted\"},\n   {\"src\": \"KLN\", \"where\": \"vol. II p. 1424 s.v. serra\", \"stance\": \"partial\",\n    \"note\": \"'serra, n., a sawlike organ (zool.) — L., ‘a saw’, of uncertain origin. Cp. sierra. Cp. also cero.' — gives the Latin gloss 'a saw', refuses an etymology\"},\n   {\"src\": \"POK\", \"where\": \"IEW, grep 'serra'\", \"stance\": \"silent\",\n    \"note\": \"no root; the only occurrence of the string is Latin sarracum/serracum 'wagon' under a different lemma\"}]})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Greek\", \"words\": \"rhině\", \"verdict\": \"plausible\",\n \"derivation\": (\"Greek ῥῑ́νη rhī́nē is 'a file, rasp' (and, by the same metaphor as Latin serra, the \"\n   \"angel-shark whose skin was used to polish wood and marble); Nourai's 'rhině' renders the eta. \"\n   \"Mann's derivation from *srisnā- is internally coherent: PIE *sr- gives Greek initial ῥ- with \"\n   \"rough breathing (as in ῥέω < *sreu-), and the cluster *-sn- is simplified with compensatory \"\n   \"lengthening of the preceding vowel, which is exactly what the long ῑ of ῥῑ́νη requires. No \"\n   \"standard Greek etymological dictionary accepts it, however: Wiktionary's entry carries an \"\n   \"explicit 'etymology needed' tag and only asks whether it might belong with ῥῑ́ς 'nose' / ῥῑνός \"\n   \"'hide' (which is where Mann puts ῥῑνός, under a separate root srin- (sris-) 'nose; headland'). \"\n   \"So the phonology works but the connection is unattested elsewhere — plausible, not confirmed.\"),\n \"derivation_fa\": (\"یونانی ῥῑ́νη (rhī́nē) «سوهان، سوهانِ زبر» است — و به همان استعارهٔ serra، نام \"\n   \"کوسه‌ای که پوستش را برای صیقل چوب و سنگ به کار می‌بردند؛ «rhině» نورایی همان آوانگاریِ اتای \"\n   \"پایانی است. اشتقاقِ مان از *srisnā- از نظر آوایی سازگار است: *sr- هندواروپایی در یونانی به \"\n   \"ῥ- با دم‌آواز درشت بدل می‌شود (مانند ῥέω از *sreu-)، و خوشهٔ *-sn- ساده می‌شود و واکهٔ پیشین \"\n   \"را می‌کشد — که همان «ای» کشیدهٔ ῥῑ́νη را توضیح می‌دهد. با این همه هیچ فرهنگ ریشه‌شناسی معتبر \"\n   \"یونانی این پیوند را نپذیرفته است؛ ویکی‌واژه آشکارا «ریشه‌شناسی لازم است» زده و تنها می‌پرسد \"\n   \"آیا با ῥῑ́ς «بینی» پیوندی دارد یا نه. پس: با احتیاط پذیرفتنی، نه تأییدشده.\"),\n \"sources\": [W+\"%E1%BF%A5%CE%AF%CE%BD%CE%B7\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:1277\", \"status\": \"supports\",\n    \"note\": \"Mann p. 1277 lists the Greek word (OCR mangles ῥίνη to 'hung') as 'Gk. [rhinē] f. ‘file’' under srisà, srisnà — the arrow from the root is Mann's own.\"}],\n \"consulted\": [\n   {\"src\": \"IEC\", \"where\": \"Mann p. 1277 (srin- (sris-) 'nose; headland', same page)\", \"stance\": \"partial\",\n    \"note\": \"Mann keeps ῥίς/ῥινός 'nose' in a separate lemma 'srin- (sris-) ‘nose; headland’ … Gk. hus gs: rhinós, f. ‘nose’', i.e. he deliberately separates ῥίνη 'file' from ῥίς 'nose'\"},\n   {\"src\": \"POK\", \"where\": \"IEW, grep 'rhine/serra'\", \"stance\": \"silent\",\n    \"note\": \"Pokorny has no lemma covering ῥίνη 'file'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. serra\", \"stance\": \"silent\",\n    \"note\": \"the Latin dictionary cites no Greek cognate for serra, consistent with there being no accepted equation\"}]})\n\ne2[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"serra; serrate; serradela, serranoid, serriferous, serriform, serrulate\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All of these are learned formations on Latin serra 'saw' and are found together on \"\n   \"Klein's pp. 1424-1425, the page Nourai cites. serra 'a saw-like organ (zool.)' is the Latin word \"\n   \"taken over unchanged; serrate 'notched' is L. serrātus 'sawlike' with the adjective suffix -ate; \"\n   \"serradella (Nourai prints 'serradela') is Portuguese serradela, a diminutive of serrado \"\n   \"'serrated' < L. serrātus, the name of a fodder clover with toothed leaflets; serranoid is a \"\n   \"hybrid of Modern Latin Serrānus (the fish genus named from serra) with Greek -oeidēs 'like'; \"\n   \"serriferous is serra + the stem of ferre 'to bear'; serriform is serra + forma; serrulate is \"\n   \"from L. serrula, the diminutive 'a little saw', + -ate. The one caveat is the AHD citation: \"\n   \"Watkins's Indo-European Roots appendix — the list Nourai's bare 'AHD' normally points to — has \"\n   \"no root for serra at all, so that reference can only be to AHD's ordinary dictionary entries.\"),\n \"derivation_fa\": (\"همهٔ این واژه‌ها ساخته‌های دانشورانه بر پایهٔ لاتینی serra «ارّه»اند و در همان \"\n   \"دو صفحهٔ کلاین (۱۴۲۴–۱۴۲۵) که نورایی به آن ارجاع داده کنار هم آمده‌اند: serra خودِ واژهٔ \"\n   \"لاتین است؛ serrate از serrātus «ارّه‌مانند» با پسوند صفت‌ساز -ate؛ serradella از پرتغالی \"\n   \"serradela، مصغّر serrado «دندانه‌دار»؛ serranoid آمیزه‌ای دورگه از لاتینِ نو Serrānus (نام \"\n   \"جنس ماهی، از serra) و یونانی -oeidēs «مانند»؛ serriferous از serra + ستاک ferre «بردن»؛ \"\n   \"serriform از serra + forma؛ و serrulate از serrula «ارّهٔ کوچک». تنها نکته این است که \"\n   \"پیوستِ ریشه‌های هندواروپاییِ واتکینز (AHD) اصلاً ریشه‌ای برای serra ندارد، پس ارجاع «AHD» \"\n   \"در اینجا تنها می‌تواند به مدخل‌های عادی فرهنگ باشد. ادعای نورایی درست است.\"),\n \"sources\": [W+\"serra\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1424\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 vol. II pp. 1424-1425 (KLN_1966.txt leaf 756, the leaf itself prints '1424 1425'): 'serra, n., a sawlike organ (zool.) — L., ‘a saw’ …'; 'serradella, n., a kind of clover. — Port. serradela, a dimin. noun formed fr. serrado, ‘serrated’, fr. L. serrātus'; 'serranoid, adj., … A hybrid coined fr. ModL. Serranus and Gk. -oeidēs'; 'serrate, adj., notched … L. serrātus, ‘sawlike’, fr. serra'; 'serriferous … Compounded of L. serra, ‘saw’, and the stem of ferre'; 'serriform, adj., sawlike. — Compounded of L. serra … and forma'; 'serrulate, adj., finely toothed. — Fr. L. serrula, ‘a little saw’, dimin. of serra'. Every word in the box is on the cited page.\"},\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins 1985 (AHD_watkins1985.txt) has no root for serra: the index gives 'SAW! sek-' and 'SERRIED ser-3' (Lat. sera 'bar', an unrelated word), and there is no *sers-/*srisā- entry. The AHD reference can therefore only be to the main dictionary entries, not to the Indo-European appendix Nourai usually means.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"vol. II pp. 1424-25\", \"stance\": \"supports\",\n    \"note\": \"the whole serra- family with the Latin base, as quoted above\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt, grep '^SERRATED/^SIERRA'\", \"stance\": \"silent\",\n    \"note\": \"Skeat's Concise does not carry these technical words\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. serra\", \"stance\": \"supports\",\n    \"note\": \"lists the Latin derivatives the English words are built on: 'serrula f.; serrārius m.; serrātus: en dents de scie; … serrātula, nom italique de la ‘bétoine’; … *serrānus ‘poisson-scie’'\"}]})\n\ndata[\"entries\"].append(e2)\n\n# ---------------------------------------------------------------- entry 5\ne5 = {\n \"entry\": 5,\n \"root\": \"Sru 3, Srva 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Avestan srva- n. 'lead; a vessel of lead' (Bartholomae, AiW col. 1649)\",\n \"note\": (\"The root box is right and Nourai's homonym numbering is right too. Bartholomae has two \"\n   \"separate entries: 'j. srū-, srvā- f. 1) ‘Nagel’ der Finger und Zehen … 2) ‘Horn’ \"\n   \"der Tiere' (the 'nail/horn' word, PIE *ḱer-, which Pokorny cites as 'Avestan sru-, srva- \"\n   \"‘horn; nail in fingers and toes’'), and immediately after it 'j. srva- n. ‘Blei; \"\n   \"Gefäss aus Blei’: ayaŋhaēnīm vā srvaēnīm vā rāδəm ‘in a vessel of iron or of lead’ \"\n   \"V.16.6; 8.14' — the lead word, which is the one numbered here. Buck, in the very passage \"\n   \"Nourai means, writes 'Av. srva- neut. (Barth. 1649), NPers. surb, etym.?' — confirming both the \"\n   \"Avestan word and Bartholomae's column number, but flagging that the family has no further \"\n   \"Indo-European pedigree. One citation is off by a few pages: the lead section of Buck is 9.68, \"\n   \"printed pp. 613-614, not p. 617.\"),\n \"note_fa\": (\"خانهٔ ریشه درست است و شماره‌گذاری هم‌آواها نیز درست. بارتولومه دو مدخل جدا دارد: \"\n   \"«srū-, srvā- مؤنث: ۱) ناخنِ دست و پا ۲) شاخِ جانوران» (که از ریشهٔ هندواروپایی *ḱer- است و \"\n   \"پوکورنی هم آن را زیر همان ریشه آورده) و بی‌درنگ پس از آن «srva- خنثی: سُرب؛ ظرفِ سربی»، با \"\n   \"شاهدِ وندیداد ۱۶٫۶ و ۸٫۱۴ «در ظرفی از آهن یا از سرب». همین دومی است که نورایی شماره‌گذاری \"\n   \"کرده. باک نیز در بخش ۹٫۶۸ می‌نویسد «Av. srva- neut. (Barth. 1649), NPers. surb, etym.?» که هم \"\n   \"واژهٔ اوستایی و هم شمارهٔ ستون بارتولومه را تأیید می‌کند، اما یادآور می‌شود که این خانواده \"\n   \"ریشهٔ هندواروپاییِ شناخته‌ای ندارد. تنها لغزش، شمارهٔ صفحهٔ باک است: بخش «سرب» در صفحات \"\n   \"۶۱۳–۶۱۴ است نه ۶۱۷. در مجموع ادعای نورایی دربارهٔ ریشه درست است.\"),\n \"sources\": [W+\"%D8%B3%D8%B1%D8%A8\", \"https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%A8/\"],\n \"ref_check\": [\n   {\"ref\": \"BRT:1649\", \"status\": \"supports\",\n    \"note\": \"Bartholomae, AiW (BRT.txt line 27481, on the leaf that carries columns 1647-1650): 'j. srva- n. ‘Blei; Gefäss aus Blei’; ayaŋhaēnīm vā srvaēnīm vā rāδəm ‘in einem Gefäss aus Eisen oder aus Blei’ V.16.6; 8.14'. Column 1649 is exactly where the entry stands.\"},\n   {\"ref\": \"SYN:617\", \"status\": \"partial\",\n    \"note\": \"Buck's 'lead' entry is 9.68 on printed pp. 613-614 (SYN.txt: '9.68 LEAD … Av. srva-' with the running head '613' immediately before and '614' after), not on p. 617; content-wise it supports: 'Av. srva- neut. (Barth. 1649), NPers. surb, etym.?'. The page number in Nourai is wrong by three.\"},\n   {\"ref\": \"BQT:1116\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' s.v. سرب (BQT_v2_pages.txt \\\\f-block 579, i.e. printed p. ~1116-1121 by the vol. 2 offset), Mo'in's footnote 1: 'اوستا srva (سرب)، پهلوی srupēn (سربی)، کردی sirib، بلوچی surub/surup، افغانی surup. رك: هوبشمان …' plus 'رك: اسرب، معرب آن نیز «اسرب»'. The Avestan → Pahlavi → Persian chain is verbatim Nourai's.\"},\n   {\"ref\": \"SNS:183\", \"status\": \"supports\",\n    \"note\": \"Tavoosi's Šāyast nē Šāyast glossary: the index line 'srubēn 183/7-184/6' and the glossary entry 'srub + ēn:' — the Pahlavi adjective occurs at 183/7, i.e. on the cited page.\"}],\n \"consulted\": [\n   {\"src\": \"SYN\", \"where\": \"Buck 9.68 LEAD, pp. 613-614\", \"stance\": \"partial\",\n    \"note\": \"'Av. srva- neut. (Barth. 1649), NPers. surb, etym.?' — the Avestan word is accepted, but Buck marks the family as etymologically opaque\"},\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1649 s.v. srva- n.\", \"stance\": \"supports\",\n    \"note\": \"'srva- n. ‘Blei; Gefäss aus Blei’', with V.16.6 and V.8.14; distinct from srū-/srvā- f. 'Nagel, Horn' in the preceding column\"},\n   {\"src\": \"POK\", \"where\": \"IEW, s.v. *ḱer- 'horn'\", \"stance\": \"partial\",\n    \"note\": \"'from the ǝ-basis Avestan sru-, srva- ‘horn; nail in fingers and toes’, srvara ‘horned’' — Pokorny knows only the HOMONYM (nail/horn); he has no entry for the lead word, which confirms that Nourai was right to number them apart\"}],\n \"nodes\": []\n}\n\ne5[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"srpîn, sruběn\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Both forms are genuine and are two spellings of one Middle Persian word. MacKenzie \"\n   \"has 'srub [sl(w)p | N usrub] lead' with the derived adjective '~ēn [-yn'] leaden', i.e. srubēn \"\n   \"'made of lead' — the -ēn suffix is the ordinary MP material adjective (cf. zarrēn 'golden', \"\n   \"arzīzēn 'of tin'). The spelling srpīn that Nourai prints first is Horn's transcription of the \"\n   \"same Pahlavi word: Horn, Grundriss p. 161 no. 728 gives 'aw. srva ‘Blei’; phlv. srpīn \"\n   \"‘bleiern’', the p standing for the /b/ of Book-Pahlavi sl(w)p. Phonetically Av. srva- \"\n   \"(an u̯-stem) yields MP srub by the resolution of the -rv- cluster into -rub-, and the Šāyast nē \"\n   \"Šāyast glossary records srubēn at 183/7 and 184/6. So the Avestan → Pahlavi arrow is sound.\"),\n \"derivation_fa\": (\"هر دو صورت راست‌اند و در واقع دو املای یک واژهٔ فارسی میانه‌اند. مکنزی \"\n   \"«srub [sl(w)p] سرب» و صفت آن «srubēn سربی» را ثبت کرده است؛ پسوند ــēn همان پسوند جنس‌سازِ \"\n   \"معمول فارسی میانه است (مانند zarrēn «زرین» و arzīzēn «ارزیزی»). صورت srpīn که نورایی نخست \"\n   \"آورده آوانگاری هرن از همین واژه است: هرن در «مبانی ریشه‌شناسی فارسی نو» ص ۱۶۱ شمارهٔ ۷۲۸ \"\n   \"می‌نویسد «aw. srva ‘Blei’; phlv. srpīn ‘bleiern’»، که در آن p همان ب است. از نظر آوایی، \"\n   \"خوشهٔ ــrvــ اوستایی در فارسی میانه به ــrubــ گشوده شده است. واژه‌نامهٔ شایست نه شایست نیز \"\n   \"srubēn را در ۱۸۳/۷ و ۱۸۴/۶ ثبت کرده است. پس این حلقه درست است.\"),\n \"sources\": [W+\"%D8%B3%D8%B1%D8%A8\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:161\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss der neupersischen Etymologie p. 161 (HRN.txt \\\\f-block 183, which opens '— 161 —'), no. 728: 'surb, usrub ‘Blei’ … aw. srva ‘Blei’; phlv. srpīn ‘bleiern’. kurd. sirib; bel. surup, suruf.' Nourai's Pahlavi form and its gloss come straight from here.\"},\n   {\"ref\": \"BQT:1116\", \"status\": \"supports\",\n    \"note\": \"Mo'in's footnote to سرب in Borhan: 'اوستا srva (سرب)، پهلوی srupēn (سربی)' — same Pahlavi adjective, same Avestan source.\"},\n   {\"ref\": \"SNS:183\", \"status\": \"supports\",\n    \"note\": \"Šāyast nē Šāyast glossary index: 'srubēn 183/7-184/6'; the glossary body has 'srub + ēn:'\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"A Concise Pahlavi Dictionary p. 77 s.v. srub\", \"stance\": \"supports\",\n    \"note\": \"'srub [sl(w)p | N usrub] lead. ~ēn [-yn'] leaden.' — note that MacKenzie's New Persian equivalent is usrub, the prothetic form\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II glossary\", \"stance\": \"silent\",\n    \"note\": \"Nyberg's glossary (grep 'srub') has no lead word; his texts do not use it\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien § 69, p. 177\", \"stance\": \"supports\",\n    \"note\": \"'surb (für *surub) = usrub ‘Blei’, afgh. bal. surup, phl. sr(u)p' — Hübschmann confirms the Pahlavi form sr(u)p\"}]})\n\ne5[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"sorb «سرب»\", \"verdict\": \"plausible\",\n \"derivation\": (\"New Persian سرب sorb/surb 'lead' continues MP srub directly, with the initial \"\n   \"cluster sr- resolved by an anaptyctic vowel (srub > surb/sorb); the by-forms Nourai prints, \"\n   \"أُسرُب usrub and أُسرُف usruf, are the same word with a prothetic u- before the cluster, and are \"\n   \"the forms MacKenzie actually gives as the New Persian equivalent ('N usrub'). Mo'in's footnote in \"\n   \"Borhan adds the cognates (Kurdish sirib, Baluchi surub/surup, Afghan surup, Gilaki surb) and notes \"\n   \"that the Arabicised form is likewise أسرب. The reason this is 'plausible' rather than 'confirmed' \"\n   \"is Hübschmann's objection at exactly this point. In Persische Studien p. 75, annotating Horn's \"\n   \"no. 728, he writes: 'Ebenso führt Vullers neben usrub = surb die Formen usrup und usruf an. Alle \"\n   \"stimmen nicht zu zd. sruva- ‘Blei’ (nur als accus. srum belegt)' — the -b/-p/-f variation \"\n   \"and the u-vocalism do not fit Avestan srva-, which is attested only in the accusative srum. Buck \"\n   \"records the same doubt with his bare 'etym.?'. So the Iranian word for lead is certainly one word \"\n   \"from Avestan to New Persian, but the precise Avestan-to-Persian phonetic route the chart draws is \"\n   \"not fully accounted for, and a Wanderwort/substrate source (as for Greek mólybdos and Latin \"\n   \"plumbum, both loans from an unknown source) remains possible.\"),\n \"derivation_fa\": (\"«سرب» فارسی نو دنبالهٔ مستقیم srub فارسی میانه است؛ خوشهٔ آغازینِ sr- با واکهٔ \"\n   \"میانجی گشوده شده (srub > سُرب). صورت‌های «أُسرُب» و «أُسرُف» که نورایی افزوده همان واژه با واکهٔ \"\n   \"پیشافزوده‌اند و مکنزی هم برابر فارسی نوِ srub را همین usrub می‌داند. حاشیهٔ معین در برهان قاطع \"\n   \"هم‌ریشه‌ها را می‌افزاید: کردی sirib، بلوچی surub/surup، افغانی surup، گیلکی surb، و یادآور \"\n   \"می‌شود که معرّب آن نیز «اسرب» است. اما حکم را «با احتیاط پذیرفتنی» گذاشته‌ایم، زیرا هوبشمان \"\n   \"در «پژوهش‌های فارسی» ص ۷۵، در حاشیهٔ شمارهٔ ۷۲۸ هرن، صریحاً می‌نویسد که صورت‌های usrub/usrup/\"\n   \"usruf «هیچ‌کدام با اوستایی sruva- ‘سرب’ سازگار نیستند» (که تنها در حالت مفعولی srum گواهی \"\n   \"شده است)؛ باک نیز با نوشتن «etym.?» همین تردید را نشان می‌دهد. پس واژه از اوستایی تا فارسی نو \"\n   \"یک واژه است، ولی مسیر آواییِ دقیقی که نمودار می‌کشد هنوز توضیح داده نشده و وام‌واژه بودنِ آن \"\n   \"(مانند mólybdos یونانی و plumbum لاتینی که هر دو وام‌اند) رد نشده است.\"),\n \"sources\": [W+\"%D8%B3%D8%B1%D8%A8\", \"https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%A8/\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1116\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' s.v. سرب with Mo'in's footnote 1: 'اوستا srva (سرب)، پهلوی srupēn (سربی)، کردی sirib، بلوچی surub/surup، افغانی surup. رك: هوبشمان' and 'رك: اسرب، معرب آن نیز «اسرب»' — the Persian word, its Pahlavi and Avestan antecedents and the أسرب by-form all as drawn (BQT_v2_pages.txt \\\\f-block 579).\"},\n   {\"ref\": \"MON:266,1854\", \"status\": \"partial\",\n    \"note\": \"Mo'in's سرب entry (abadis.ir/fatofa/سرب): '(سُ) [اِ.] فلزی نرم و چکش‌خوار به رنگ خاکستری…' — the definition but no etymology on the online text; Dehkhoda on the same page carries the full chain 'اوستا سرو / پهلوی سرپین / کردی / بلوچی / افغانی / گیلکی', matching Nourai. The two Mo'in page numbers (presumably اسرب at 266 and سرب at 1854) cannot be checked, as the 6-vol pagination is not online.\"},\n   {\"ref\": \"SNS:614\", \"status\": \"not_found\",\n    \"note\": \"The Šāyast nē Šāyast glossary scan runs to 242 leaves and its word index cites text lines only up to the 330s; there is no p. 614. The lead word is at SNS:183 (index: 'srubēn 183/7-184/6'), which Nourai cites correctly on the root and Pahlavi boxes. '614' looks like a misprint.\"}],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss p. 161 no. 728\", \"stance\": \"supports\",\n    \"note\": \"'surb, usrub ‘Blei’ … aw. srva ‘Blei’; phlv. srpīn ‘bleiern’. kurd. sirib; bel. surup, suruf.'\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 75, note on Horn 728 (and § 69, p. 177)\", \"stance\": \"contradicts\",\n    \"note\": \"'Ebenso führt Vullers neben usrub = surb die Formen usrup und usruf an. Alle stimmen nicht zu zd. sruva- ‘Blei’ (nur als accus. srum belegt).' — Hübschmann rejects the straight Avestan derivation of the New Persian forms\"},\n   {\"src\": \"PHD\", \"where\": \"p. 77 s.v. srub\", \"stance\": \"supports\",\n    \"note\": \"'srub [sl(w)p | N usrub] lead' — MacKenzie equates the MP word with NP usrub\"},\n   {\"src\": \"MON\", \"where\": \"فرهنگ معین / لغت‌نامهٔ دهخدا s.v. سرب (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"Dehkhoda: 'اوستا «سرو»، پهلوی «سرپین»، کردی، بلوچی «سوروپ، سوروف»، افغانی «سوروپ»، گیلکی «سورب»؛ مخفف اسرب که معرب آن است'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 9.68 LEAD, p. 614\", \"stance\": \"partial\",\n    \"note\": \"'Av. srva- neut. (Barth. 1649), NPers. surb, etym.?' — accepts the equation, leaves the etymology open, and notes that Greek mólybdos and Latin plumbum are themselves loans from an unknown source\"}]})\n\ndata[\"entries\"].append(e5)\n\nwith io.open(\"data/verification/page-473.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-473.py",
 "description": "Write page-473 verification JSON"
}
```


### [2026-09-14T02:44:09.178Z] TOOL RESULT

```
ok
```


## [2026-09-14T02:44:11.988Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-473.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 473",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-14T02:44:13.236Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'confirmed': 7, 'disputed': 1, 'plausible': 4}
root verdicts: {'confirmed': 2, 'disputed': 1, 'plausible': 1}
ref checks: {'supports': 11, 'not_checked': 1, 'contradicts': 1, 'partial': 4, 'not_found': 1}
books consulted: {'supports': 15, 'silent': 14, 'partial': 7, 'contradicts': 4} | by book: {'PHD': 6, 'NYB': 4, 'MON': 4, 'LKT': 3, 'KLN': 3, 'HRN': 3, 'HUB': 3, 'LAT': 3, 'BQT': 2, 'SKT': 2, 'POK': 2, 'TTS': 1, 'HJB': 1, 'BRT': 1, 'IEC': 1, 'SYN': 1}
```


## [2026-09-14T02:44:32.248Z] AGENT

Done — 0 PROBLEM lines.

**Page 473 (book p. 443) — 4 non-redirect entries, 12 nodes**
- Node verdicts: confirmed 7, plausible 4, disputed 1. Root verdicts: confirmed 2, plausible 1, disputed 1.
- Ref checks: 11 supports, 4 partial, 1 contradicts, 1 not_found, 1 not_checked.

**Disputed**
- **Srîra (root + node #1 Pahlavi sěr)** — Nourai read his own source backwards. Bailey, *Hvatanica II* p. 78 line 1 (read from the page image): "sīra-, **not** to Av. srīra, since śr > Khotan ṣṣ. Cf. rather Mid. Pers. saγr (sēr), NPers. sīr 'satiated'." Also the root gloss is wrong: Av. *srīra-* = "beautiful" (Bartholomae; Pokorny p. 618 under *ḱrei-), which Nourai's own chart-note admits but did not act on. The real chain is MP **sagr** [sgl] → Pāzand/NP sēr (Nyberg: "-aγr- > -ēr- by the common SW law"). Node #2 (sēr → sīr) is confirmed — Bailey's own pairing.

**Other findings worth the owner's eye (not flagged codes)**
- **Srisâ/Srisnâ**: root and Latin/Greek nodes = plausible. Mann IEC p. 1277 verified verbatim (and he marks it "onomat."), but Pokorny and Watkins have no such root, Ernout-Meillet call *serra* "sans étymologie claire"; only de Vaan (EDL 558) gives PIE ***sers-** "to cut off" — compatible in substance, different in shape. Wiktionary's اره entry cites Nourai p. 443 itself, so it is circular.
- **Book's own gloss slip** (extraction is faithful, verified against the page image): Latin *serra* is glossed "file"; it means "saw" — Mann's own line reads "Lat. serra, f. 'saw'". Only Greek ῥίνη is "file".
- **Sru 3/Srva 2 → sorb**: root confirmed (BRT col. 1649 exact; BQT p.1116 Mo'in footnote verbatim; HRN 161 no. 728), but the Persian node is plausible because Hübschmann, *Persische Studien* p. 75, rejects it: "usrub/usrup/usruf … stimmen **nicht** zu zd. sruva- 'Blei'". Buck writes "etym.?".
- **Citation slips in the book**: SYN:617 → Buck's LEAD section is 9.68 on pp. 613–614; SNS:614 → out of range (the word is at SNS:183, which he cites correctly elsewhere); "AHD" on the English serra node cannot be the IE-roots appendix (Watkins has no root for *serra*).
- **No extraction errors found** — the JSON matches the printed page, including the Persian by-forms شکال/شگال and أُسرُب/أُسرُف.
- Archived 10 web sources via `fetch_source.py`; saved `data/verification/sources/refs/ocr/BLY/78.png` + `78.vision.txt`.
