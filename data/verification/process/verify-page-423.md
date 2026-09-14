# Verification process log — verify-page-423


## [2026-09-14T01:21:35.739Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 423 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-423.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-423.json. Write /home/sfmqrb/git/rishe/data/verification/page-423.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 423` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:37.262Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:37.767Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:37.813Z] TOOL RESULT

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


## [2026-09-14T01:21:38.272Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-423.txt"
}
```


### [2026-09-14T01:21:38.290Z] TOOL RESULT

```
1	=== PDF page 423 (book page 393) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Reu 1, Rěu 3, Rů 1, Reud 1 : to cry, roar  (refs POK:867)
4	#1 (parent #0) [Avestan] refs=POK:867 | raod 2 : to weep
5	#2 (parent #0) [Sogdian] refs=SOD:346 | rwš : to roar
6	#3 (parent #0) [Latin] refs=AHD | rŭgîre : to roar ; rŭ-mor : common talk
7	  #4 (parent #3) [English] refs=None | riot ; rumor
8	#5 (parent #0) [Germanic] refs=KLN:1352,1364 | 
9	  #6 (parent #5) [English] refs=None | roar ; rumble
10	--- entry 1 ---
11	ROOT Rěu 3 -> redirect to Reu 1
12	--- entry 2 ---
13	ROOT [Indo-European] Reu 2, Reua, Rů 2, Reup / Reudh 2 / Reud 2 : to dig up, tear out, snatch / to clear land / rough  (refs POK:869)
14	#1 (parent #0) [Avestan] refs=KLN:1347; POK:869 | raoidya : to cultivate land, to be fit for cultivation
15	#2 (parent #0) [Latin] refs=POK:870; AHD:1537 | rumpere : to break ; rudis : rough
16	  #3 (parent #2) [English] refs=AHD:1133,1537 | rupture, abrupt, bankrupt, corrupt, disrupt, interrupt ; rough
17	#4 (parent #0) [Germanic] refs=KLN:1347; POK:869; AHD:1537 | rutjan : to clear land, get rid of ; rupja : to rip up ; raubôn : to rob ; raubô : clothes taken as booty
18	  #5 (parent #4) [English] refs=AHD; POK:870; KLN | rid ; rip ; rob, robber, rover, rubbish, rubble ; robe
19	#6 (parent #0) [Old Norse] refs=POK:868 | ryja : to pluck wool from sheep ; rogg : wool, hair
20	  #7 (parent #6) [English] refs=AHD:1077,1134; KLN:1363; POK:868 | rug, rugged, rag, ragged
21	--- entry 3 ---
22	ROOT Reua -> redirect to Reu 2
23	--- entry 4 ---
24	ROOT Reud 1 -> redirect to Reu 1
25	--- entry 5 ---
26	ROOT Reud 2 -> redirect to Reu 2
27	
```


## [2026-09-14T01:21:41.402Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-423.json",
 "description": "Read source JSON for page 423"
}
```


### [2026-09-14T01:21:41.438Z] TOOL RESULT

```
{
  "pdf_page": 423,
  "book_page": 393,
  "entries": [
    {
      "root": {
        "name": "Reu 1, Rěu 3, Rů 1, Reud 1",
        "lang": "Indo-European",
        "refs": "POK:867",
        "gloss": "to cry, roar"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:867",
          "words": [
            {"translit": "raod 2", "gloss": "to weep", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:346",
          "words": [
            {"translit": "rwš", "gloss": "to roar", "script": null}
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
            {"translit": "rŭgîre", "gloss": "to roar", "script": null},
            {"translit": "rŭ-mor", "gloss": "common talk", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "riot", "gloss": null, "script": null},
            {"translit": "rumor", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:1352,1364",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "roar", "gloss": null, "script": null},
            {"translit": "rumble", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Rěu 3", "redirect": "Reu 1"},
      "nodes": []
    },
    {
      "root": {
        "name": "Reu 2, Reua, Rů 2, Reup / Reudh 2 / Reud 2",
        "lang": "Indo-European",
        "refs": "POK:869",
        "gloss": "to dig up, tear out, snatch / to clear land / rough"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:1347; POK:869",
          "words": [
            {"translit": "raoidya", "gloss": "to cultivate land, to be fit for cultivation", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:870; AHD:1537",
          "words": [
            {"translit": "rumpere", "gloss": "to break", "script": null},
            {"translit": "rudis", "gloss": "rough", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD:1133,1537",
          "words": [
            {"translit": "rupture, abrupt, bankrupt, corrupt, disrupt, interrupt", "gloss": null, "script": null},
            {"translit": "rough", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:1347; POK:869; AHD:1537",
          "words": [
            {"translit": "rutjan", "gloss": "to clear land, get rid of", "script": null},
            {"translit": "rupja", "gloss": "to rip up", "script": null},
            {"translit": "raubôn", "gloss": "to rob", "script": null},
            {"translit": "raubô", "gloss": "clothes taken as booty", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD; POK:870; KLN",
          "words": [
            {"translit": "rid", "gloss": null, "script": null},
            {"translit": "rip", "gloss": null, "script": null},
            {"translit": "rob, robber, rover, rubbish, rubble", "gloss": null, "script": null},
            {"translit": "robe", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Norse",
          "refs": "POK:868",
          "words": [
            {"translit": "ryja", "gloss": "to pluck wool from sheep", "script": null},
            {"translit": "rogg", "gloss": "wool, hair", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD:1077,1134; KLN:1363; POK:868",
          "words": [
            {"translit": "rug, rugged, rag, ragged", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Reua", "redirect": "Reu 2"},
      "nodes": []
    },
    {
      "root": {"name": "Reud 1", "redirect": "Reu 1"},
      "nodes": []
    },
    {
      "root": {"name": "Reud 2", "redirect": "Reu 2"},
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:21:42.371Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo ---- && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-14T01:21:42.427Z] TOOL RESULT

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
----
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


## [2026-09-14T01:21:47.601Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','KLN','AHD','BRT','SKT','LEW','LAT','IEC','SYN','WLD']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-14T01:21:48.134Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-385.json"
}
```


### [2026-09-14T01:21:48.732Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
```


### [2026-09-14T01:21:48.785Z] TOOL RESULT

```
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
      "consul
```


## [2026-09-14T01:21:52.330Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['POK'].get('page_offset'))\nprint(d['POK'].get('lookup_hint'))\nprint(d['AHD'].get('page_offset'))\nprint(d['AHD'].get('lookup_hint'))\nprint(d['KLN'].get('page_offset'))\nprint(d['KLN'].get('lookup_hint'))\nprint(d['SOD'].get('page_offset'))\n\""
}
```


### [2026-09-14T01:21:53.451Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
```


## [2026-09-14T01:21:56.009Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 86[5-9]\\|Page(s): 87[0-2]\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:21:56.060Z] TOOL RESULT

```
70322:Page(s): 865 
70336:Page(s): 865 
70377:Page(s): 865 
70432:Page(s): 866 
70477:Page(s): 871-872 
70574:Page(s): 872-873 
70662:Page(s): 867-868 
70854:Page(s): 868-871 
70864:Page(s): 871 
70869:Page(s): 871 
71108:Page(s): 865 
71118:Page(s): 866 
71126:Page(s): 866 
71138:Page(s): 866
```


## [2026-09-14T01:21:57.182Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: 1\\. reu\\|lemma: 2\\. reu\\|lemma: 3\\. reu\\|lemma: reu\\|lemma: reud\\|lemma: reup\\|lemma: reudh\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:21:57.239Z] TOOL RESULT

```
70434:Root / lemma: reu-b-ax\6 reu-g- 
70479:Root / lemma: reuA^-{*uereuA'^^ (zero grade of *hieleuRh-) 
70485:Root/ lemma: reu6!^-\ "red' derived from a zero grade of Root/ lemma: el-1, ol-, J-\ "red, 
70576:Root / lemma: reugh-m(e)n- 
70592:Root/ lemma: reu-1, reu- ru- 
70664:Root / lemma: reu-2, reus- : ru- 
70856:Root / lemma: reu-3, reu-s- 
70866:Root / lemma: reu-4 
70871:Root / lemma: reu-smen- 
70888:Root / lemma: reus- 
70898:Root / lemma: reuto-, routo- rut- 
70914:Root / lemma: reua- : ru-
```


## [2026-09-14T01:22:03.686Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '70590,70700p' POK_full.txt"
}
```


### [2026-09-14T01:22:03.745Z] TOOL RESULT

```
Page(s): 873 

Root/ lemma: reu-1, reu- ru- 

Meaning: to roar, murmur, etc.. (expr.), onomatopoeic words 

Material: Old Indie rau-ti, ruvati, /'51/5// "bellow, roar, larmt, drohnt', rava-, ravatha- rr\. " 

bellowing, braying, roar '; gr. u)puo|jai "heule, bellow, stofte einen scream from', cbpuSov 

Adv. "with bellowing, braying, roar' (prefix Indo Germanic o); Latin /x7/77c»/'"noise, shout, 

call, rumor'; ravus 'hoarse', rav/st " hoarseness ', raucus 'hoarse', ravid-Tre 's\c\\ hoarse 

talk, speak'; 

Old English /'ec»/7"Wehklagen', Middle High German rienen {*reundn) " wail, lament'; Old 
Icelandic rymja'roar, bellow, drone, grumble', rymrm. "grobe voice'; 

Church Slavic revg, rjut/ and Old Church Slavic rovg, rut/'roar, bellow', Czech ruje{o\6), 
rfjei. "clamor of Hirsches, rutting ', poln. rujai. "rutting, heat(zeit)' (out of it Lithuanian ruja, 
Latvian ruojai.); Slavic Voi/p besides *rjutiirorr\ *reud, *reuti, thereafter *rjovg> *rjevg; 

with the meaning of dumpfen, but heimlichen Murmelns: Old Irish run' mystery ', cymr. 
rh/n6s.; Gothic runai. " mystery ', Old Saxon runa. Middle Low German rune' furtive 
whispering, h. Beratschlagen, Runenzeichen', Old English run 6s., Middle High German 
rune' whispering, furtive Beratschlagen', Old Icelandic /y/7a"vertraulich together talk. 



speak', Old English runian^ whisper, sich verschworen'. Old High German runen^ 
whisper, raunen', changing through ablaut Old English reonian^ whisper' (as above reon. 
Middle High German rienen), Norwegian dial. /7C»/75 'babble'. 

extensions: 

a. reud- Old Indie rudati, roditi^heuW., weint, jammert', Avestan raod-'\Neep, cry'. Old 
Indie roda-m. 'Klageton, Winsein, Weinen' (= Old High German rozm., compare 
Lithuanian rauda); gr. pu^w? (see above); Latin rudo, -ere, -/V/'cry; roar, bellow'; Old High 
German r/ozan^\Neep, cry', /"dz'das Weinen, Winsein', Old English reotan^ wail, weep, 
cry', ablaut. Old Icelandic raufa^roar, bellow'; Bavarian rofzen^weep, cry'; Lithuanian 
raudm/1 lament', raudoju, raud6ti6s., Latvian raudaf'\Neep, cry, lament', Lithuanian aps/- 
rustu, preterit su-rudau^ma6, wicked, evil, sad become', rustas^ grumpy, surly, sullen, 
fierce, grim'; slov. rydat/^\Neep, cry'. Old Czech rud/t/ ^affWct, sadden'. 

b. reug- gr. spuyovra ' the bellowing ', spuypn^oc; ' bellowing (of bull)', opuyjjaSsc; 
Gopupoi Hes. (also 6puijaY56(; 'great din, fuss, noise' is from *6puYpa5oc; reconverted with 
metathesis), cbpuyn, wpuyfja, cbpuyfjoc; ' bellowing, braying, roar, Geheul' (to cJb- see 
above); pu^siv ' growl, bark, bay' Hes.; Latin rug/'o, -Fre^roar, bellow (of Lowen)' (after 
mugicR); Middle Irish ruchV bellowing, braying, roar, Geheul' {*rug-tu-)\ Old English reoc 
'wild', wherefore probably Gothic /n-rauMJan ^ ergnmmen'; (but Old Icelandic rauknn. ' 
draft animal ' for rgkn = vrgkn); Slavic *ruzietr neighs ' in Old Church Slavic rbzet-b, rbzati, 
Serb, rze, fzatieic. (Lithuanian rugoti^eyW nehmen' is loanword from russ. rugatb 'vilify, 
scold' = Old Church Slavic rggati sg^ mock '). 

c. reuk- Old English ryn^roar, bellow' {*ruhjan). Middle Low German rujan6s.. Old High 
German ruhin^ bellowing, braying, roar', besides ruhen {ixom *ruhjan). Old High German 
/'c»/7d/7'rugTre' (Wissmann Nom. postv. 87 f.); Latvian rucu, m/r/'roar, roar, bellow', 
Lithuanian rukf/^roar, bellow'; Old Church Slavic rykajg, /y/ra//' rug ire', russ. rykafb'roar, 
bellow'; besides Old Church Slavic r/kajg^ bellow' (from *rjukajg), ablaut, slov. rukm. 
'rutting, heat the Hirsche', rukaf/^roar, bellow' etc. 

d. ein cognate reus-seeks man in: 

Modern High German rosten (after dem knisternden Ton?), Old High German rest 
'Rostpfanne, pyre, stake'. Old High German rose. Middle High German rosch, rosch 
'knisternd, brittle, resch'. Old English ge-rosc/an^bem fire dry'?; in addition probably 
Lithuanian ruzg/u^roar, foam, schnurre, grumble'. 



References: WP. II 349 ff., WH. II 421, 447, 449, 450 f., Trautmann 241, 247, 248. 
Page(s): 867-868 

Root / lemma: reu-2, reus- : ru- 

Meaning: to tear out, dig out, open, acquire, etc.. 

Grammatical information: participle Perf. Pass, ru-to- 

Note: to part, as it seems, still volleres ereu-{see below) 

Material: Old Indie rav-, ru-' shatter, shatter' {ravat, rudhf, ravisam, roruvat, meaning 

probably from "her and in StiJcke reiften'), participle ruta-^ shatter, zerschmettert' (= Latin 

dh, e-, ob-rutus)\ roman-, /oman'\r\a\r' (compare under n. Irish rua/mneach an6 Old 

Icelandic rggg long hair'); gr. spuai-xSojv "die Erde aufwijhlend'; 

Latin mo in the meaning "tear open, dig, scratch', e-, dh, ob-ruo, -rutus{see above), ruta 
caesa "all, was auf a small area of land ausgegraben and gefallt is', rutrum "spade, hack, 
mattock, hoe, Kelle', rute//um 'smaW shovel', rutabu/um^s\r\ove\, Scharre'; 

Middle Irish ruam'spade, Grabscheit', ruamar^ eiioss\o'; nir. rua/mneach long hair'; 

Old Icelandic ryja^6en Schafen die Wolle ausreiften' (Norwegian rui. "Winterwolle'), Old 
Saxon ruw/t "rauhesfell, fur'; 

Old Icelandic rgggi., rgggrm. "long hair, long wool' {*rawwa-), Swedish m^^ "zottiges 
hair' ( *ruwwa-)\ out of it engl. rug, 

Gothic /7i//'5 "verganglich' {r/urjan 'spoW'), Old Icelandic /y/r"small, arm'; 

presumably Old Saxon Old High German /7C»/77C» "strap, leathery band, strap, belt, girdle' 
(*"abgerissener Hautstreifen'), Old English reoma, reama6s., also "thin Haut' (compare S. 
873 *reugh-m(e)n-^ skimmings'); Middle Low German Middle Dutch run, rune, schwab. 
raun^\Na\\ac\\, Gaul', because of East Frisian /7a/7-m/7e"Hahnrei' (actually " castrated 
rooster, cock') originally "equus castratus', mnl. runen, ruynen'cut, clip, castrate '; (Modern 
High German runken); borrowed Latvian rumt^ castrate ', also Finnish /■i/^/7a "Wallach', 
ruunata " castrate ';
```


## [2026-09-14T01:22:16.884Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '70700,70870p' POK_full.txt"
}
```


### [2026-09-14T01:22:16.975Z] TOOL RESULT

```
ruunata " castrate '; 

Lithuanian rauju, rauti^ ausrei^en, ausjaten', ravetT weed ' (/'ai/a5"Straftengraben', Old 
Prussian rawys^^\\.o\\, trench, channel' loanword from poln. /'dM/"ditch, trench, channel'); 
Latvian Aa^/r/zs "Raufeisen'; Old Church Slavic ryjg, /y//"dig', /7>i/(?"reiR>e from, jate from', 
/y/b, /y/o "Grabscheit, spade, hack, mattock, hoe', AOKb "ditch, trench, channel, pit, 
pothole', runo^ fleece '; 



s. also above S. 338 about ereu-2, wherefore perhaps also Lithuanian urvasxw., also 
urvai. "cave'. 

extensions: 

a. reub-. "reissen' in Latin /z/i6>^s"Brombeerstaude, blackberry ' C*shrub, bush, whereof 
man sich reiftt'), rub/cfus {par\'\s i. e. "parum coctus') 'raw, rauhrissig'; perhaps also rubeta' 
toad '; Middle Irish /'Oit'it' "animal'?; Germanic *raup-, *rupp- {\N\t\r\ intensification) in Gothic 
raupjan ^ p\uck' , Old English /yeyoa/? 'auspliJndern', Old High German roufen. Middle High 
German roufen, reufen, raufen ^p\uck'; Middle English ryppen, engl. rip^ rend ', Middle 
High German rupfen, ropfen ^ p\uck' , Old Icelandic ruppa, A^p/a"losreiften', ruplu. 'booty, 
robbery '. 

b. ref/f/- 'zerreissen'; rud-16-m^, wild'. 

Latin rudus, -er/sn. "zerbrockeltes rock, detritus, rubble '; also rud/'s' uncultivated, raw', 
Ai/Z/i/s 'coarse, baurisch' {*rud-lo-)\ Middle Irish ruad^R\}\v\e\ cymr. PI. rhudd/on 'offa\, bran 
' {*roud)\ Old Norse reyta ( *rautjan) 'abreiften, tear, to pick to pieces, pluck', also Middle 
Dutch ruten, holl. ruiten^ rend, pliJndern, rob'. Middle Low German ruter, holl. ruiter 
(Modern High German Reutei) 'Plunderer, robber' (influence of Middle Latin ru(p)tarius)\ a 
related word for 'junk' places Middle High German riuze, alt-riuze^\Ner mitGeriimpel 
handelt or es ausbessert' ahead; auf das through Wassern and Faulenlassen of Flachses 
vorbereitete Ausziehen the Flachsfaserweisen Old Icelandic rot/nnlau\, decayed ' (but u- 
rot/nn st\\\ 'wer die hair nicht lost '), rotn. ' decay; Ohnmacht', Old Saxon rotonlrom Rost 
verzehrt become'. Old English rot/an^ decayed, wither, wilt'; Middle Low German rofen 
"flax rosten'. Old High German rozzen^ decayed ', Middle High German rdzzenav\6 rsezen 
' decayed let'. Modern High German Bavarian rossen ^V\acY\s faulen let' (reshaped to 
rostenuach rdsten^a\A6erc\ Rost braten'). Middle High German /loz' friable '; 

here Old Indie Rudra-QH {*rud-lo-), pali /udda-^crue\, savage' after W. WiJst Rudra-. 

c. re^d^-'reuten, roden'. 

Avestan raoidya-^ arab\e to make'; 

Old Icelandic /yioda'reuten, raumen'. Middle High German rietensiem V. 'ausrotten, 
destroy'; Old Icelandic rjddrv\. 'offene place in Walde', Old High German /'ec»o''gerodetes 
land ', Modern High German dial. Ried^ reed ' ds.. Old High German riut/ds., riuten 
{*riutjan) 'reuten', ablaut. Old Icelandic rudu. 'gerodete place in wood, forest'. Middle Low 
German /lo/'das Roden', Old Icelandic rydja ^ro6ev\\ aufraumen, ausrotten'. Old English a- 



ryddan {ev\Q\. rid) "mug, rob, plundern'; Middle High German roten. Modern Higli German 
rotten. Middle Low German roden, out of it Modern High German roden. Old Frisian to- 
/"o/^a'ausrotten'. 

d. /(e^/Ar- (partly probably also reug-, reugh-T) 'pluck'. 

Old Indie /uncat/'rauh, rupft, enthijlst', /uncana-n. "das Ausrupfen, Ausraufen', ruksa- 
see below; 

gr. opuoaoj, Attic -ttoj "ditch, grub, scharre', opuxn, opuyn "das ditch, trench, channel', 
opuypa n. "ditch, trench, channel', KaTU)puxn<; "in the Erde vergraben'; common Old Indie - 
gh- > ks- : Gr. -gh- > -ss-, -tt- 

Latin runco, -are^ weed, ausjaten', runco, -d/7/s"Reuthacke, Jathacke'; gr. puKovn " plane ' 
(the vowel suggestion getilgt perhaps after puaia^u) "reifte weg' to *uer-s-, -u-77), from 
which Latin runc/nads. (-/?- through distant assimilation, unterstijtzt through runcare); Irish 
rucM's\N\ne' ("WiJhler' *ruktu-)\ mcymr. rhwgn ^Reibeu, Kerben' {*runk-no-l s. Loth RC. 
42, 138 f.); 

with dem concept the (ausgerauften) Wollzotten and the with it verbundenen roughness 
(as S. 868 Old Icelandic rqg^: Old Indie ruksa- "rough', common Old Indie -gh- > ks- : Gr. - 
gh- > -SS-, -tt- 

Old High German ruh. Old English /x?/? "rough, behaart; ungebildet'; Old Saxon rugi, ruwii. 
"rauhes fell, fur, grobe cover'. Middle High German riuhe, ruhe 'Pe\zwerk', Modern High 
German Rauchwerk, Old English ryhe, ruwa, /'eon^e "grobe Wolldeeke', Old Icelandic ry\. 
ds.; 

as "crack, furrow' perhaps here Lithuanian raukai., raukasm. "wrinkle', raukiu, raukti^\v\ 
Falten pull, furrow ', runku, m/r// "wrinkly become' and with ff. Latin m^a "wrinkle, crease '. 

Maybe alb. {*ruga) rrudha'\Nr'\nk\e' common alb. -g- > -dh- {not a Latin loanword. 

e. reup- ^ausre'\Q>en, tear, break, rupture'; roupa-^ho\e, aperture ', rupeis-xocV! . 

Old Indie ropayati^ causes rupture, shatters, cracks ', rupyati^has Reiften in Leibe', 
*rdpa-y\. "hole, cave' (= Lithuanian raupaT, compare Old Icelandic raufi., serb. rupa); 

Latin rumpo, -ere, rupT, ruptum'breaW, rupture', rupes' steep Felswand, cliff, cliff gap, 
abrupt abyss' (compare under Lithuanian rup/s^rock', wherefore lllyrian PN DPunsq, 
Achaia, and in similar meaning Modern High German /?/e/Oe "Schuttreuse' and die Tirol 



place names roups, roufa, inscribed Roppen, Rofen), rupex, -/ic/5"ruppiger uncoutin, 
clumsy person, Rupel' (compare Lithuanian rupus^rouqh, coarse'); 

Maybe from [thracian-illyrian word.] gr. popcpaia , n, A. large, broad sword, used by the 
Thracians, opQac, p. papuai5npouc; ano twv Ss^icjov wpoov siriasiovTEi; Plu.Aem.18 , cf. 
Phylarch. Fr.57 J., Arr.Fr.103J.: generally, sword, LXX Ge.3.24, al., Ev.Luc.2.35, Apoc.6.8, 
Jul.Ep.89b; of the sword of Goliath, LXX 1 Ki. 17.51, J.AJ6.12.4. derived Latin rhomphaia 
'a spear', later 'a sword' (Plut. Aem. Paul. 18; Eust. ad II. VI 166; Hesych.). Other forms of 
the word are rump/a {L\\/., Gell., Ascon. ad Mil.), romphea {\s\6. Etym.), romphaea vel 
romfea {CGL 7, 212). later Bulgarian rofeja, rufja^ a thunderbolt ' and the Alb. rrufeja^ a 
thunderbolt ', reja "cloud ' as derivatives of that word. 

Old Icelandic riOfa, Old English reo/^/? 'break, rupture, tear' (Old High German a-riub 
"atrox, dirus', actually "ungebrochen'); Old Icelandic rauft "col, gap, hole'. Old English reaf 
n. ' robbery, booty, dress, armament, armor' {*roupa= Slavic *rupa^\\o\e'). Old High 
German roubm. ds., to Gothic bi-raubon. Old High German roubon. Old Saxon robon 
"rob'. Old Icelandic /'5i//^"durchbrechen, rob' and /'©^/^"durchbohren, tear'. Old English 
be-nefan^ rwuQ, rob'; Old Icelandic /"©//^'"gerupfte wool, rauhesfell, fur'. Middle Dutch roof 
"abgezogenes fell, fur'; geminated East Frisian m/?/?e/7 "scratch, scrape, rub, pluck'. Low 
German rubbelig, rubberig' uneven, rough'. Modern High German At/pyO/ig "unkempt, 
shaggy', engl. rubble, rubbish^ rubble, offal'; Old Icelandic /7y/^/7/7 "bristly, unkempt, shaggy, 
rauhhaarig'; Modern High German ruffe/n^ scour, rub, clean, hart zusetzen'; 

Lithuanian rupet/'s\c\r\ kijmmern', mp^s "worries' (to russ. rupa^ care, ruefulness'), 
raupyt/ and (Indo Germanic ablaut ou\ ou) rudpt/"d'\g, hollow out', myoas "rough, bumpy ', 
A^y0^5 "rough, coarse', rup/s'rocW, East Lithuanian raupaTP\. " measles, pox' ('Rauhigkeit 
in the Haut'), raupsaf leprosy '; also Lithuanian rupuze, raupeze^ toad ' (from the 
roughness the Haut), compare also Latvian raupa^ goose bumps ' ("shudder, shiver '); 
Serb. /x/pa"hole, pit, pothole' {*roupa), poln. rupic si§^s\c\\ kiJmmern', ablaut, rypac 
"scindere, friare'. 

f. reus- Old Icelandic reyrrxu. " cairn, pile of stones set up as a memorial or mark of 
some kind ', rustt "Trummer, decomposed wall' (see above S. 686 about Old Indie losta- 
m. n.); Old High German riostar' plough handle, plough stilt ', Old English reosVoxn Teil of 
Pfluges', Modern High German dial, riester^ raig zum Schuhflicken'; Danish /"os" schnitzel, 
offal', Norwegian dial, ros, rys^ fish scale ', /i/5"thin bowl', /'c»5a"ritzen, die Haut 
aufscheuern, sich losen', isl. rosmn. "offal', rus/n. "offal'. Old Saxon rus/osm. PI. 
"Speckseite', Old English ryse/m. "bacon, fat, ; Dutch ru/' lax and dry, e.g. of sand, rough' 



{*ruzla-)\ Old Icelandic ryskj'a' rend, pluck', Norwegian /i/s/r" offal, dust, powder' (also 
Middle Low German rusch^ intestines, entrails ', Bavarian gerausch? sKxW insecure Middle 
High German roesche. Modern High German dial. /r>sc/7'hard and light frail, breakable '); 
with Germanic root variation Old Icelandic raska^\v\ Unordnung bringen'; with -/?- probably 
Old High German gi-ruspit <^\. to inhorruit{aper), and (as 'in neck scratch, scrape') Modern 
High German rauspern. Middle High German riuspern, riuspein, rOspern, compare Latin 
ruspor, -ari^ seek ', actually "aufreiftend, durchwijhlend, whereupon forschend', as Italian 
/Y/Syoare' "scratch (from the hen)', mspo "rough, neugemijnzt', rospo^ toad ' show; 

Lithuanian rausiu, /"s^s//" scratch, dig', rusys, /z/sas "pit, pothole for die Winterkartoffein', 
pelen-rusis, -AJsa "Aschenbrodel', rusinti^ poke, stoke, stir coals ', Latvian rausf stoke, 
stir coals, dig', /'ai/s//?"pull, rend ', rusa^ stacked rubble '; about Old Church Slavic rusiti^ 
overturn, knock over ', *mc/7b "movement', see above S. 332. 

References: WP. II 351 ff., WH. II 445 f., 447 f., 451 ff., Trautmann 240, 241, 247, 
Wissmann Nom. Postverb. 10, 130, 176f. 
Page(s): 868-871 

Root / lemma: reu-3, reu-s- 

Meaning: " hurry, rush ' 

See also: see above S. 331 f. {er-3), wherefore still Middle Irish /'Ja//77/77 "onrush', bret. 

rumm^ crowd, throng, mass, horde, swarm ' {reu-smen). 

Page(s): 871 

Root / lemma: reu-4 
Meaning: " explore, inquire ' 
See also: see above S. 337 {ereu-). 
Page(s): 871
```


## [2026-09-14T01:23:06.417Z] AGENT

Now let me check Pokorny's printed pages and the other references.


## [2026-09-14T01:23:08.474Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 867 868 869 870; do echo \"=== POK_02 leaf $((p-344)) (should be p.$p) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((p-344))\"' {print substr($0,1,700)}' POK_02.txt; done"
}
```


### [2026-09-14T01:23:09.542Z] TOOL RESULT

```
=== POK_02 leaf 523 (should be p.867) ===
=== POK_02 leaf 524 (should be p.868) ===
=== POK_02 leaf 525 (should be p.869) ===
=== POK_02 leaf 526 (should be p.870) ===
```


## [2026-09-14T01:23:09.807Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD reu ===\"; grep -n \"^reu-\\|^reud-\\|^reudh-\\|^reup-\\|^reuk-\\|^reug-\\|^reu\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T01:23:09.871Z] TOOL RESULT

```
=== AHD reu ===
894:reu-'
896:reu-?
897:reu-2, Also reue-. To smash, knock down, tear out, dig up, uproot. 1. Suffixed o-grade form *rous-o- in Ger- manic *rawwa- in: a. Old Norse régg, réggr, woven tuft of wool: RAG}; b. Norwegian rugga, rogga, coarse cover- let, akin to the Scandinavian source of RUG. 2. Basic form *reu- in Latin ruere, to collapse, cause to collapse: RABBLE, RUIN. [Pok. 2. reu- 868.] reudh-', Red, ruddy. I. O-grade form *roudh-. 1. Ger- manic “raudaz in: a. Old English réad, red: RED; b. Old Norse rauthr, red (> reythr, rorqual): RORQUAL. 2. Ger- manic *raudnia- in Old Norse reynir, mountain ash, rowan (from its red berries), akin to the source of ROWAN. 3. Latin rijfus (of dialectal Italic origin), reddish: RUFES- CENT, RUFOUS. 4. Latin rdbus, red, in robigd, ribigo, rust: RUBIGINOUS. 5. Latin rdbur, rdbus, red oak, hard- ness, and rdbustus, strong: ROBLE, ROBORANT, ROBUST; CORROBORATE, RAMBUNCTIOUS. II. Zero-grade form *rudh-. 1. Form *rudh-d- in Germanic *rud6 in: a. Old English rudu, red color: RUDDLE, RUDDY; b. Old English rudduc, robin: RUDDOCK. 2. Suffixed form *rudh-sto- in Germanic *riist- in Old English rdst, rust: RusT. 3. Latin rubeus, red: ROUGE, RUBEOLA, RUBY; RUBEFACIENT 4. Latin rubicundus, red, ruddy: RUBICUND. 5. Latin rubidus, red: RUBIDIUM. 6. Suffixed (stative) form *rudh-é- in Latin rubére, to be red: RUBESCENT; ERUBES- CENCE. 7. Suffixed form *rudh-ro- in: a. Latin ruber, red: RUBELLA, RUBRIC; BILIRUBIN; b. Latin rutilus, reddish: RUTILANT; Cc. Greek eruthros, red (with pro- thetic vowel, from oldest root form *sreudh-): ERY- THEMA, ERYTHRO-; d. possibly remade Greek erusi-, red, reddening: ERYSIPELAS. 8. Suffixed form *rudh-to- in Latin russus, red: RISSOLE, ROUX, RUSSET. [Pok. reudh- 872.] reudh-2, To clear land. 1. Suffixed zero-grade form *rudh-yo- in Germanic *rudjan in Old Norse rydhja, to clear land: RID. 2. Possibly Germanic expressive variant *rudd- stick, club, in Old English rodd, stick: Rop. [In Pok. 2. reu- 868.] reue-. To open; space. 1. Suffixed variant form *ri-mo- (< *rua-mo-) in Germanic *riimaz in: a. Old English rim, space: ROOM; b. Old French run, ship’s hold, space: RUMMAGE. 2. Suffixed form *reu(g)-es- in Latin ris, “open land,” the country: RURAL, RUSTIC. [Pok. reuo-, ri- 874.] reug-. To vomit, belch, smoke, cloud. 1. Germanic *reu- kan in Old English réocan, to smoke, reek: REEK. 2. Suf- fixed zero-grade form *rug-to- in Latin ructdre, to belch: ERUCT. [Pok. 4. reu- 871.] reugh-men-. Cream. O-grade form *roughmen- in Ger- manic *rau(g)ma- in Middle Low German rém(e), cream: RAMEKIN. [Pok. reugh-m(e)n- 873.] reup-. Also reub-. To snatch. I. Basic form *reub- in Germanic *rupja in Flemish rippen, to rip: RIP!. II. O-grade form *roup-. 1. Germanic *raufjan in: a. Old English réafian, to plunder: REAVE!; b. Old English beréafian, to take away (be-, bi-, intensive prefix; see ambhi): BEREAVE. 2. Germanic *raubén, to rob, in: a. Middle Dutch and Middle Low German réven, to rob: ROVER; b. Old French rober, to rob: ROB; c. Italian rubare, to rob: RUBATO. 3. Germanic *raubd, booty, in Old French robe, robe (> “clothes taken as booty”): ROBE. 4. Suffixed form *roup-tro- in Sanskrit loptram, booty, from lumpati, he breaks, removes: LOOT. III. Zero-grade form *rup-. 1. Latin dsirpdre (< *isu- rup-; isus, use, usage, from iti, to use), originally “to interrupt the orderly aquisition of something by the act of using,” whence to take into use, usurp: USURP. 2. Na- salized form *ru-m-p- in Latin rumpere, to break (> riipés, rock): ROUT!, RUPTURE; ABRUPT, BANKRUPT, CORRUPT, DISRUPT, ERUPT, INTERRUPT, IRRUPT, RUPICO- Lous. [Pok. 2. reu- 868.] rezg-. To plait, weave, wind. Germanic *ruski- in Old English risc, rysc, rush: RUSH?. [Pok. rezg- 874.] [risan. To rise. Germanic word. 1. Germanic *risan in:
```


## [2026-09-14T01:23:17.657Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '890,897p' AHD_watkins1985.txt | cut -c1-2500; echo \"=== ROUGH ===\"; grep -n \"ROUGH\" AHD_watkins1985.txt | head; echo \"=== RUBBLE/RUBBISH ===\"; grep -n \"RUBBLE\\|RUBBISH\\|RIOT\\|RUMOR\\|ROAR\\b\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T01:23:17.741Z] TOOL RESULT

```
<persisted-output>
Output too large (40.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/b8t421iea.txt

Preview (first 2KB):
rebh-2. To roof over. Germanic *rebja-, *rebj6, “covering of the chest cavity,” in: a. Old English ribb, rib: RIB; b. Old Norse rif, rib, ridge: REEF!, REEF?; c. Middle Low German ribbe, rib: SPARERIBS. [Pok. 2. rebh- 853.]
réd-. To scrape, scratch, gnaw. 1. O-grade form *réd- in: a. Latin rédere, to gnaw: RODENT; CORRODE, ERODE; b. suffixed (instrumental) form *réd-iro- in Latin rés- trum, beak, ship’s bow: ROSTRUM. 2. Possibly variant form *rdd- in: a. Latin radere, to scrape: RADULA, RASH?, RASORIAL; ABRADE, CORRADE, ERASE; b. suffixed (in- strumental) form *rdd-tro- in Latin rdéstrum, a rake, with diminutive *rdsculum, whence denominative verb *ras-
reg-'
culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grad
...
</persisted-output>
```


## [2026-09-14T01:23:19.717Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01 POK_02 POK_03; do echo \"== $f total leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f.txt)\"; done; grep -n \"reu-\\b\" POK_02.txt | head -5; echo ---; grep -n \"raoi.ya\\|raoidya\\|raoiδya\" POK_02.txt POK_03.txt BRT.txt | head -20"
}
```


### [2026-09-14T01:23:21.120Z] TOOL RESULT

```
== POK_01 total leaves: 363
== POK_02 total leaves: 433
== POK_03 total leaves: 429
581:anord.  kraki ,Sta.nge  mit  Haken;  magere  Person';  ahd.  kräclio  (*krekan-)j kracco  (als  *kraggan-^  Geminationsform  zu  germ.  *krag-  s.  unten)  ,haken- förmiges  Gerät',  anord.  kräkr  und  ablautend  krökr  , Biegung,  Bucht, Haken'  (daraus  mengl.  crök,  nengl.  crook  ,Krümmung  usw.'),  krekja ,krümmen,  greifen',  schwed.  kräka,  norw.  dial.  kreka  krak  ,kriechen', kreken  ,schwach,  hinfällig'.  Daneben  auf  germ.  -g  (wohl  =  idg.  -k)  ahd. krago  , Haken';  vielleicht  auch  ags.  crög,  ahd.  kruog  ,Krug',  wenn  nicht in  irgendwelcher  Lehnbeziehung  zu  gr.  xgcoGOÖg  (siehe  unten  u.  greu-g-).  Vgl. von  der  Wurzelf.  gr-ei-  die  gleiche  Erweiterung  in  anord.  krikr  ,Biegung, Bucht',  -/cn/ci  (woraus  mengl.  crike,  creke,  nengl.  creek)  ,Krümmung,  Bucht';
631:1.  Gutturalerweiterung-  greu-g-  in:  air.  grucj  nir.  grug  ,Runzel* (*gruggu-),  mir.  grucänach  ^runzlig^ ;
634:greu-p-:  gr.  ygvTtög  ,gekrümmt,  mit  einer  Adlernase',  ygVTtöa)  ,krümme', ygvyjj  ygVjtög  m.  , Greif  (nach  dem  krummen  Schnabel  und  den  krummen Fängen'),  nasaliert  ygvfxrtdvsLv'  ygvTtova&aL,  0vyy.d^7tT6Lv  Hes.,  wozu  wohl zunächst  ags.  usw.  krumh  , krumm'  (s.  oben  S.  387).
635:greu-b-:  hierher  vielleicht  schott.-gäl.  groban  ,top  or  point  of  a  hill' (*grubb-) ;
640:3.  s-Er Weiterung  greu-s-:  mlid.  mnd.  krüs  ,kraus,  lockig';  q^^^^ krüse  ,Gekröse,  Bauchfett^  (,*das  Krause');  mit  germ.  -au-  ndd.  krös  ;^ geweide  von  GänsenS  mhd.  (ge)krcese,  nhd.  Gekröse,  ndd.  kriise  (""krUsä ,Runzel,  Falte,  Furche,  Locke',  hoU.  kreus  ,Falz  in  Faßdauben* ;  ags.  cr^^ 'zierlich',  wfries.  kreas  .aufgeputzt';  ahd.  mhd.  krol  (-11-)  ,kraus'  (*krudd:)^ mhd.  krol(le),  krillle  ,LockeS  norw.  krull  ds.;  norw.  mdartl.  kruskn] krusken  ,hinfällig',  ndd.  krusch  ,crispus',  mhd.  h-üsp  ,kraus',  nhd.  obd. kraust  , kraus'.  ^
---
POK_03.txt:1358:Av.  raoidya-  , urbar  zu  machen';
BRT.txt:10671:'üzd  (Transskr.)  ffdtvihiihä.   —   D  Hds. 'd.V'.  —  '1  Vgl.  lu  xraoidyah:
BRT.txt:24956:•  j,  *rao^a-,  *raoi8ya-"  Adj.  (fem.  'yj-) 'urbar  zu  machtn':  yesi  vnsm  mazdayasna zqm  'thyam  htxiayalca  karstayai.'a  para- kanlaya?'a  "wenn  die  M.  ein  urbar  zu machendes  Grundstück  bewässern,  pflügen und  umgraben  wollen"  V.  6'.  6;  zit.  5.  7 PüZ.,  wo  rao'taym;  —  sam  (sd,)  karsyqm 'lyqm  V. /4-13-
```


## [2026-09-14T01:23:26.989Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\"); for(i=1;i<=n;i++){} } {print NR\": \"substr($0,1,60)}' POK_03.txt | sed -n '95,115p'"
}
```


### [2026-09-14T01:23:27.995Z] TOOL RESULT

```
70:   -ere,  -xi,  -xum  ,flechteD, ineinanderflechten'  =  ahd.
71: eßen ;  fliegen, flattern',  wohl  Erw.  von  pel-  ,fließ
72: h-  und  Nierenfett*,  nhd.  Flom,  Flaum  m.  ds.,  aisl.^e
73:  floccho  ,lanugo',  nhd.  Flocke,  mnd.  vlocke  ,Woll-,  S
74: bach-Endzelin  III  325).  •
WP.  II  100,  WH.  II  319, 
75:   vöder  ds.;  ahd.  {fedar)fötar  ,canna', spätahd.  fü
76: .  pojq,  pojiti  ,tränke';  baltoslav.  *pöta-  und *plta
77: sk.  pustma[s\  ,postremae';  umbr.  postne,  lat.  pöne  a
78: fad  , stark,  tapfer,  groß';
lit.  päts  , Ehemann'  und
79: ';  nur  kelt.  und  slav.
Air.  ög  ,jungfräulicb',  öge
80: riund  , Freund,  Geliebter,  Ver- wandter', ahd.  friunt  ,
81:  sich  auszeichnend';  d^eo-ngÖTtog  , Seher'  (,der  sich 
82: ren  ,ge- frieren  machen',  ahd.  as.  frost  (*frus-taz)] 
83: e,  lett.  paüna  ,Ränzel,  Bündel'.
pU'g- :  gr.  Ttvyri
84:  reflex.  ,schwellen', puntü,  püsti  ,schwellen,  sich  a
85: ett.  pünis  ,faulendes,  eiterndes',  punes  PI.  ,Moderer
```


## [2026-09-14T01:23:33.131Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=1358{n+=gsub(/\\f/,\"\")} END{print \"leaf index (0-based):\",n}' POK_03.txt; echo ---; awk 'BEGIN{RS=\"\\f\"} NR==105 || NR==106 || NR==107 {print \"----LEAF \"NR\"----\"; print substr($0,1,300)}' POK_03.txt"
}
```


### [2026-09-14T01:23:34.237Z] TOOL RESULT

```
leaf index (0-based): 104
---
----LEAF 105----
n  und  Faulenlassen  des  Flachses vorbereitete  Ausziehen  der  Flachsfaser  weisen  aisl.  rotinn  ,faul,  verfault' (aber  ü-rotinn  noch  ,wer  die  Haare  nicht  verloren'),  rot  n.  ,Fäulnis; Ohnmacht^,  as.  rotön  ,von  Rost  verzehrt  werden',  ags.  rotian  ,faulen, welken';  mnd.  r�
----LEAF 106----
  rüpes  ,steile  Felswand,  Klippe, Felskluft,   jäher  Abgrund'   (vgl.    unten   lit.    rupis  ,Fels',   wozu   illyr.  ON ^PvTtsg,  Achaia,  und  in  ähnlicher   Bed.   nhd.   Riepe  ,Schuttreuse'  und  die tirol.    Ortsnamen   roupd,   rouf?,   geschrieben   Roppen,   Rofen),  rüpex,  -i
----LEAF 107----
 lett.  raust , schüren,  wühlen',  rausfU  ,zerreD,  reißen',  rwsa  , aufgehäufter  Schutt' ;  über aksl.  ruHti  ,umstürzen*,  "^i'uchh  , Bewegung*,  s.  oben  S.  332.
WP.  II  351  ff.,  WH.  II  445  f.,  447  f.,  451  ff.,  Trautraann  240,  241,  247, Wissmann  Nom.  Postverb.  10,
```


## [2026-09-14T01:23:42.383Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=102 && NR<=105 {print \"\\n----LEAF(1based) \"NR\" = p.\"(NR+764)\"----\"; print $0}' POK_03.txt | cut -c1-100000 | head -200"
}
```


### [2026-09-14T01:23:43.700Z] TOOL RESULT

```
----LEAF(1based) 102 = p.866----
 Schaar',  gaeaf-rawd  .Winterszeit'  =  mir.  gem-rad  ds.,  mcymr.  bed- rawd,  cymr.  bedd-rod,  bret.  bez-ret  , Gräber'  (cymr.  bedd  .Grab'),  dazu  miri rä(i)the  .Jahreszeit.  Vierteljahr'  {^rötio-)]
air.  rethim  .laufe'  mit  Kompositis.   Kaus.  roithim  .treibe  an';  Verbaln. riutli  m.  .Lauf  (*/-<«-);  zu  air.  do-riuth  ,accurrö'  gehört  cymr.  tyred  (*to-rete)     . ,komm!';  air.  fo-riutkj  cymr.  ^2to-r6(ia/ ,succurrö',   acymr.  Perf.  gua-raut =  ir.  fo-rdith  (*upo-röt-e);
aisl.  rqdull  m.  ,Strahlenkranz,  Sonne'  und  as.  radur,  ags.  rador,  rodor  "" m.  ,Himmel';  got.  *raps  ,leicht',  (Kompar.  n.  rapizo)  ags.  rced  .schnell,  ^ behend',  ahd.  rado,  rato  adv.  ,schnell';  and.  rath,  afr.  reth,  ahd.  rad ,Rad',  radelöt  ,mit  Räderchen  versehen';  lit.  rätas  m.  ,Rad,  Kreis'  (Plur. rätai  ,Karren,  Wagen'),  lett.  rats  ,Rad'  (Plur.  rati  , Wagen'),  lit.  ratelis m.  ,Rädchen'  (vgl.  ahd.  radelöt  und  lat.  rotula  f.  ,Rädcheii'),  dvirätis (meist  PL  dviräöiai)  .zweirädriger  Wagen';
lit.  ritü,  risti  .rollen'  (*r^) ;  aber  gall.  petor-ritum  .vierrädriger  Wagen' kann  lat.  Entwicklung  von  *petor-roto-  sein;
WP.  II  368.  WH.  II  443  f..  Trautmann  238.
ret-,  rot-,  rgt-  .Stange.  Stamm,  Balken  gefüge'.
Ahd.  ruota,  aisl.  röda  ,Rute,  Stange',  as.   röda  .(Pfahl)  kreuz',   ags.  röd ds.    und   ksl.   rati§te,   ratoviste   , Lanzenschaft' ;   vielleicht   dazu   lat.   retae ,aus  dem  Ufer  des  Flusses  hervorragende  Bäume',  retäre  .den   Fluß  von  — solchen  reinigen'  und  o^ätis  .Floß'.  :
WP.  II  368.  WH.  II  420,  431.  ^
867
reti',  ^^""»  ^""  Schall  Wurzel  ^brüllen,  heisere  Laute  ausstoßen^;  , brummen,
murren';  roudo-  , Klage'.
\\,  räu-ti,  ruvdt'i,  ravati  ^brüllt,  lärmt,  dröhnt',  rdva-,  ravdtha-  m.  _,Ge-
briill*';   gl'-  (hotoLiat   ,heule,   brülle,   stoße   einen   Schrei  aus^,   (hq-Ddöv  Adv.
mit  GebrülP  (Präfix  idg.  ö);  lat.  rümor  ,Geräusch,  Ruf,   Gerücht^;   rävus
heiser^,  ravis  f.  , Heiserkeit',  raucus  ,heiser',  raviö  -ire',sich  heiser  reden';
ao-s.  reon  , Wehklagen',    mhd.  rienen  (*reunön)   ,klagen,  jammern';    aisl.
rymja  ,brüllen,  brummen',  ryjiir  m.  ,grobe  Stimme';
ksl.  revg,  rjuti  und  aksl.  rovo,  ruti  ,brüllen',  6ech.  f-üjö  (alt),  Hje  f. Geschrei  des  Hirsches,  Brunstzeit',  poln.  rnja  f.  ,Brunst(zeit)'  (daraus lit.  rujä,  lett.  ruoja  f.) ;  slar.  ^rovq  neben  *7'juti  aus  *reuö,  *reuti,  danach *rjoüg  >  "^rjevo]
mit  der  Bed.  des  dumpfen,  aber  heimlichen  Murmeins:  air.  rün  ,Ge- heimuis',  cymr.  rliln  ds. ;  got.  rüna  f,  ,Geheimnis',  as.  rüna,  mnd.  rüne ^heimliches  Flüstern,  h.  Beratschlagen,  Runenzei

----LEAF(1based) 103 = p.867----
chen',  ags.  rün  ds.,  mhd. rüne  , Flüstern,  heimliches  Beratschlagen',  aisl.  ryna  ,vertraulich  zusammen reden',  ags.  rünian  ,flüstern,  sich  verschwören',  ahd.  ränen  ,flüstern, raunen',  ablautend  ags.  reonian  ,flüstern'  (wie  oben  reoiiy  mhd.  rienen), norw.  dial.  rjona  , schwätzen'.
Erweiterungen :
a.  reud-  :  ai.  ruddti,  röditi  ,heult,  weint,  jammert',  av.  raod-  /weinen',  ai. röda-  ra.  , Klageton,  Winseln,  Weinen'  (=  ahd.  röz  m.,  vgl.  lit.  rauda)\ gr.  ^i;^a>?  (s.  oben);  lat.  rudö^  -ere,  -Ivi  ,schreien;  brüllen';  ahd.  riozan , weinen',  röz  ,das  Weinen,  Winseln',  ags.  reotan  , klagen,  weinen',  ablaut. aisl.  rauta  ,brüllen';  bair.  rotzen  ,weinen';  lit.  rdudmi  ,ich  wehklage', raudöju,  raudoti  ds.,  lett.  raüddt  , weinen,  beweinen',  lit.  apsi-rüstUj  Prät. su-rüdau  ,böse,  traurig  werden',  rüstas  ,mürrisch,  grimmig';  slov.  rydati , weinen',  aöech.  ruditi  ,betrüben'.
b.  reug-  :  gr.  igv/öyta  ,den  brüllenden',  iovyurjXog  , brüllend  (vom  Stier)', dQvyf.iaösg'  d-dqvßoi  Hes.  (auch  dQVj.Laydög  ,großer  Lärm'  ist  aus  ^dqvy^iadog umgestellt),  ü}QVyr},  djQvy[.ia,  d)Qvyfj.ög  , Gebrüll,  Geheul'  (zum  a>-  s.  oben); QvCsiv  ,knurren,  bellen'  Hes. ;  lat.  rügiö,  -Ire  ,brüllen  (vom  Löwen)'  (nach mügiö?)]  mir.  rucht  ,Gebrüll,  Geheul'  {*7mg-tu-)]  ags.  reoc  ,wild',  wozu wohl  got.  in-rauhtjan  ,ergrimmen';  (aber  aisl.  raukn  n.  , Zugtier'  für  7'gJcn =  vrgkny,  slav.  *ruzieti  ,wiehert'  in  aksl.  f^iet^J  r^zati,  serb.  rze,  rzati usw.  (lit.  rügöti  ,übel  nehmen'  ist  Lw.  aus  russ.  rugdh  ,schmähen'  =  aksl. rqgati  s^  ,spotten').
C.  reuk-:  ags.  ryn  ,brüllen'  i^rülijan)^  mnd.  rujan  ds.,  ahd.  rühin  , Gebrüll', neben  ruhen  (aus  *ruhjan),  ahd.  fohon  ,rügire'  (Wissmann  Nom.  postv. 87  f.);  lett.  rücu,  rükt  ,brauseu,  brüllen',  lit.  rükti  , brüllen';  aksl.  rykajq,
55*
868  •
rykati  ,rugire',   russ.   rykäth,   , brüllen*;   daneben  aksl.  rikajq  ^brülle'  (auj, *rjükaJQ),  ablaut.  slov.  rük  m.  ,Brunst  der  Hirsche',  rükati  ^brüllen'  ustt.
d.  ein  verwandtes  reus-  sucht  man  in: nhd.  rösten  (aach  dem  knisternden  Ton?),  ahd.  rös^  ,Röstpfanne,  Scheiter- häufen',  ahd.  rose,  mhd.  rosch,  rösch  ,knisternd,  spröde,  re^-cA',  ag-s.  ge-roscian ,beim  Feuer  trocknen'?;  dazu  wohl   lit.  rüzgiu  , brause,  schnurre,  murre*.
WP.  II  349  ff.,  WH.  II  421,  447,  449,  450  f.,  Trautmann  241,  247,  248^
2,  reu-,  reuo-:  ru-  ,auf reißen,  graben,  aufwühlen;  ausreißen;  raffen';  zu^ Teil,  wie  es  scheint,  noch  volleres  ereu-  (s.  unten);  Partiz.  Perf.  Pasg. ru-to-.  ^
Ai.  rav-,  ru-  ,zerschlagen,  zerschmettern^  (rdvat,  riidhi,  rävlsam,  röruvat*' Bed.  wohl   aus   ,her   und   in  Sücke   

----LEAF(1based) 104 = p.868----
reißen'),   Partiz.   rutd-   ,zerschlagen, zerschmettert'  (=  lat.  di-,  e-,  ob-rütus);  röman-,  löman  ,Haar'  (vgl.  unten   , n.  ir.  rüaimneach  und  aisl.  rggg  ,langes  Haar');  gr.  egvoi-x^wv  ,die  Erde  V aufwühlend';  -"*^
lat.  ruö  in  der  Bed.  ,aufreißen,  wühlen,  scharren',  e-,  dl-^  ob-ruö,  -rütui (s.  oben),  rüta   caesa  ,alles,  was   auf  einem  Grundstück  ausgegraben  und gefällt   ist',    rätrum    , Spaten,    Hacke,    Kelle',    rutellum    ,kleine    Schaufel',  ';  • rutäbulum  , Schaufel,  Scharre';  '^1
mir.  rüam  , Spaten,  Grabscheit',  räamar  ,effossio' ;  nir.  rüaimneach  ,langes Haar' ;
aisl.  ryja  ,den  Schafen  die  Wolle  ausreißen'  (norw.  rü  f.  ,Winterwolle'), as.  rüwi  f.  ,rauhes  Fell';  ^
aisl.  rggg  f.,  rgggr   m.   ,langes   Haar,   lange  Wolle'  {*rawica-)j  schwed.  H rugg  ,zottiges  Haar'  {^*ruwwa-) ;  daraus  engl.  r\ig ;
got.  rlurs  ,vergänglich'  [riurjan  ,verderben'),  aisl.  rjjrr  ,gering,  arm';
vermutlich  as.  ahd.  riomo  ,Riemen,  ledernes  Band,  Gürtel'  (*,abge- rissener  Hautstreifen'),  ags.  reoma,  reama  ds.,  auch  ,dünne  Haut'  (vgl. S.  873  *reugh-m(e)n-  ,Rahm');  mnd.  mndl.  rOw,  rüne,  schwäb.  raun  ,Wallach, Gaul',  wegen  ofries.  han-räne  , Hahnrei'  (eigentlich  »verschnittener  Hahn') ursprüngl.  ,equus  castratus',  mnl.  runen,  ruynen  'schneiden,  kastrieren*; (nhd.  runken);  entlehnt  lett.  rünlt  ,kastrieren',  ebenso  finn.  ruuna  , Wallach*, ruunata  , kastrieren*;
lit.  rdujuj  rduti  ,ausreißen,  ausjäten',  raveti , jäten'  (rävas  ,Straßengraben', apr.  rawys  ,Graben'  Lw.  aus  poln.  röw  , Graben');  lett.  raüklis  ,Rauf eisen'; aksl.  ryjg,  ryti  , graben',  r^vg  ,reiße  aus,  jäte  aus',  ryh,  rylo  ,Grabscheit, Spaten,  Hacke',  rov^  ,Graben,  Grube',  runo  ,Fließ' ;
s.  auch  oben  S.  338  über  2.  ereu-,  wozu  vielleicht  auch  lit.  ürvas  m., auch  iirva  f.  ,Höhle'.
r
869
;Brweiteruiigen :
ji.  reuh-:  ^reissen^  in  lat.  mhus  ,Brombeerstaude,  Brombeere*  (,*Straucb, ^voraa  man  sieb  reißt*),  rühidus  (panis  i.  e.  ,parum  coctus*)  ,rob,  raub- rissig*';  vielleicht  auch  rubeta  , Kröte' ;  mir.  robb  ,Tier'?;  germ.  ^raup-, *ru])p-  (mit  Verschärfung)  in  got.  raupjan  , rupfen',  ags.  rlepan  , ausplün- dern', ahd.  roufen,  mhd.  roufen,  reufen^  raufen  rupfen';  mengl.  ryppen^ en^l-  ^'i^  , reißen',  mhd.  rupfen^  ro'pfen  , rupfen',  aisl.  ruppa,  rupla  , los- reißen', rupl  n.  , Beute,  Raub'.
b.  reud-  ,zereissen^;  rud-16-  ,roh,  wild'.
lat.  rüdus,  -eris  n.  ^zerbröckeltes  Gestein,  Geröll,  Schutt^;  auch  rudis ^unbearbeitet,  roh^,  rullus  ;grob,  bäurisch^  {*rud-lo-)\  mir.  rüad  ,Ruine^, cymr.  PL  rhuddion  , Abfall,  Kleie^  (*roii(i-);  anord.  reyta  (*rantjan)  ,ab- reißen,  zerreißen,  zerpflücken,  rupfen^,  auch  mndl.  rüten,  holl.  ruiten , reißen,  plündern,  rauben^,  mnd.  rüter,  holl.  ridter  (nhd.  Reuter)  ,riün- derer,  Räuber'  (Einfluß  von  mlat.  ru(p)tarius)]  ein  zugehöriges  Wort  für , Gerumpel'  setzt  mhd.  riuze,  alt-riuze  ,wer  mit  Gerumpel  handelt  oder  es ausbessert'  voraus;  auf  das  durch  Wässer

----LEAF(1based) 105 = p.869----
n  und  Faulenlassen  des  Flachses vorbereitete  Ausziehen  der  Flachsfaser  weisen  aisl.  rotinn  ,faul,  verfault' (aber  ü-rotinn  noch  ,wer  die  Haare  nicht  verloren'),  rot  n.  ,Fäulnis; Ohnmacht^,  as.  rotön  ,von  Rost  verzehrt  werden',  ags.  rotian  ,faulen, welken';  mnd.  röten  ,Flachs  rösten',  ahd.  rözzen  , faulen',  mhd.  rözzen  und rcezen  , faulen  lassen',  nhd.  bair.  rossen  ,Flachs  faulen  lassen'  (umgebildet zu  rösten  nach  rösten  ,auf  dem  Rost  braten'),  mhd.  röz  ,müibe';
hierher  ai.  Rudrd-  GN  (*}'ud-lo-),  päli  ludda-  ,grausam'  nach  W.  Wüst Rudrd-.
c.  reudh-  ,reuten,  roden'.
Av.  raoidya-  , urbar  zu  machen';
aisl.  rjöda  ,reuten,  räumen*,  mhd.  rieten  st.  V.  ,ausrotten,  vernichten^; aisl.  rjödr  n.  , offene  Stelle  im  Walde',  ahd.  reod  ,gerodetes  Land',  nhd. dial.  Ried  ds.,  ahd.  riuti  ds.,  riuten  (*riutjan)  ,reuten',  ablaut.  aisl.  rud n.  ,gerodete  Stelle  im  Wald',  mnd.  rot  ,das  Roden',  aisl.  rydja  ,roden ; aufräumen,  ausrotten',  ags.  äryddan  (engl,  rid)  ,berauben,  plündern'; mhd.  roteri,  nhd.  rotten;  mnd.  roden,  daraus  nhd.  roden,  afries.  tö-rotha ,ausrotten'.
(1.  reuk-  (z.  T.  wohl  auch  reug-,  reugh-?)  , rupfen'.
ai.  luncati  ,rauft,  rupft,  enthülst',  luncana-  n.  ,das  Ausrupfen,  Aus- raufen', rüksd-  s.  unten;  gr.  dovaaio,  att.  -ttco  ,grabe,  scharre',  dgvxT^, ÖQvyrj  ,das  Graben',  l)Qvyi.icc  n.  , Graben',  xarw^vx'Jg  ,in  der  Erde  vergraben'; lat.  runcöj  -äre  ,jäten,  ausjäten',  runcö,  -önis  ,Reuthacke,  Jäthacke' ;  gr. ^vndvrj  ,Hobel'  (der  Vokalvorschlag  getilgt  etwa  nach  Qvaidlto  ,reiße  weg'
870
zu  *uer-s-,  -w-??),  woraus  llt.  runcina  ds.  (-n-  durch  FernassimilatioQ' unterstützt  durch  riincäre);  ir.  rucht  .Schwein^  (,Wühler'  "^ruktu-)-^  »icym/ r/iiü^n  ,Reiben,  Kerben'  (*runk-no-?  s.  Loth  RC.  42,   138  f.) ;
mit  dem  Begriff  der  (ausg-erauften)  Wollzotten  uud  der  damit  verbünd^ neu  Rauheit  (wie  S.  868  aisl.  rggg)'.  ai.  rüksd-  ,rauh',  ahd.  ruh,  ags.  ^^ ,rauh,  behaart;  ungebildet';  as.  rügi,  rüwi  f.  ,rauhes  Fell,  grobe   Decke' '^1^ mhd.  riuhe,  ruhe  ^Pelzwerk',  nhd.  Eaxichicerk,  ags.  ryhe,  rmoa,  reoice  ^grobe'^^ Wolldecke',  aisl.  ry  f.  ds. ;  _
als  ,Riß,   Furche'  vielleicht  hierher  lit.  raüka   L,  raükas   m.  ,Runzel* raukiüj  raükti  ,in  Falten  ziehen,  runzeln',  runkü,  rükti  ,runzelig  werden«  ;2i und  mit  g*:lat.  rüga  ,Runzel,  Falte'.
e.  reup-    ,ausreißen,    zerreißen,    brechen' ;    roupä-    ,Loch,    Öffnung*  "^^.' rüpeis-  ,FeIs*.
ai.  röpayail  ,verursacht  Reißen,  bricht  ab',  rnpyati  ,hat  Reißen  iia Leibe',  '^röjpa-  n.  ,Loch,  Höhle'  (=  lit.  raiipal,  vgl.  aisl.  rauf  t.,  serb.  rüpa)'^
lat.  rnmpö,  -ere,  rüpJ,  rxiptum  ,brechen',
```


## [2026-09-14T01:24:12.907Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==106' POK_03.txt | head -60"
}
```


### [2026-09-14T01:24:14.200Z] TOOL RESULT

```
  rüpes  ,steile  Felswand,  Klippe, Felskluft,   jäher  Abgrund'   (vgl.    unten   lit.    rupis  ,Fels',   wozu   illyr.  ON ^PvTtsg,  Achaia,  und  in  ähnlicher   Bed.   nhd.   Riepe  ,Schuttreuse'  und  die tirol.    Ortsnamen   roupd,   rouf?,   geschrieben   Roppen,   Rofen),  rüpex,  -icia  ■;Tr;. , ruppiger  klotziger  Mensch,  Rüpel'  (vgl.  lit.  rvpüs  ,rauh,  grob');
aisl.  riüfaj  ags.  reofan  ,brechen,  zerreißen'  (ahd.  ä-riuh  ,atrox,  dirus', eigentlich  ,ungebrochen') ;  aisl.  ravf  f.  ,Spalte,  Loch',  ags.  reaf  n.  ,Raub, Beute,  Kleid,  Rüstung'  (*roupa  =  slav.  *rupa  ,Loch'),  ahd.  roub  m.  ds.,  zu  ,; got.  hi-rauböiij  ahd.  rouhön,  as.  röbön  , rauben',  aisl.  raufet  ,durchbrechen,  ^ rauben'  und  reyfa  ,durchbohren,  zerreißen',  ags.  he-rlefan  ,berauben';  aisl. reyfi  ,gerupfte  Wolle,  rauhes  Fell',  mndl.  roof  , abgezogenes  Fell';  geminiert ostfries.  rubben  , kratzen,  reiben,  rupfen',  nd.  rubbelig,  rubberig  , uneben, rauh',  nhd.  ruppig  ,struppig',  engl,  rubble,  rubbish  ,Schutt,  Abfall';  aisl. rüfiim  ,borstig,  struppig,  rauhhaarig';  nhd.  rüffeln  , scheuern,  hart  zusetzen*;
lit.  rüpki  ,sich  kümmern',  rüpüs  ,besorgt'  (zu  russ.  rupd  ,Sorge_,  Gram'), raupyti  und  (idg.  Ablaut  ou :  öu)  ruopti  ,graben,  höhlen',  riipas  ,rauh, holperig',  rupüs  ,rauh,  grob',  rupis  ,Fels',  ostlit.  raupat  PI.  ,Masern, Pocken'  ('Rauhigkeit  in  der  Haut'),  raupsai  , Aussatz';  auch  lit.  rvpuil, raupeltl  , Kröte'  (von  der  Rauheit  der  Haut),  vgl.  auch  lett.  raupa  , Gänse- haut' (,Schauder');  serb.  rüpa  ,Loch,  Grube'  {*roupa),  poln.  rupic  sie  ,sich kümmern',  ablaut.  rypac  ,scindere,  friare'.
f.  reus-:  aisl.  reyrr  m.  , Steinhaufen',  rast  f.  ,Trümmer,  zerfallene  Mauer' (s.  oben  S.  686  über  ai.  lostd-  m.  n.);  ahd.  riostar  ,Pflugsterz',  ags.  reost ,ein  Teil  des  Pfluges',  nhd.  dial.  riester  ,Lappen  zum  Schuhflicken';  dän. ros   »Schnitzel,    Abfall*,    norw.    dial.   ros,    rys   ,Fischschuppe',    rus   , dünne
r
871
Schale*,  '>^osa  ,Titzen,  die  Haut  aufscheuern,  sich  lösen*,  isl.  rosm  n.  , Abfall', j.iisl  n.  , Abfall',  as.  ruslos  m,  PL  , Speckseite',  ags.  rysel  m.  Speck,  Fett, y^  Jo-l. ;  ndl.  rul  ,locker  und  trocken,  z.  B.  vom  Sand,  rauh'  (*ruzld-)'j  aisl. fijskja  , reißen,  rupfen',  norw.  rush  , Abfall,  Staub'  (auch  mnd.  rüsch  ,Ein- o-evveide',  bair.  geräusch?  noch  unsicherer  mhd.  roesche,  nhd.  dial.  rösch hart  und  leicht  zerbrechlich  u.  dgl.');  mit  germ.  Wurzelvariation  aisl.  raska in  Unordnung-  bringen';  mit  -p-  wohl  ahd.  gi-rüsjpit  gl.  zu  inhorruit (aper),  und  (als  ,im  Halse  kratzen')  nhd.  räuspern^  mhd.  viuspern,  riiisjpeln^ räspern,  vgl.  lat.  rüspoTj  -äri  ,suchen',  eigentlich  , auf  reißend,  durchwühlend, wonach  forschend',  wie  ital.  ruspare  ^scharren  (von  der  Henne)',  ruspo ,rauh,  neugemünzt',  rospo  ,Kröte'  zeigen;
lit.  rausiüy  rausti  , scharren,  wühlen',  rüsySj  rüsas  , Grube  für  die  Winter- kartoffeln', pelen-rüsis^  -rüsä  , Aschenbrödel*,  rüsinti  , schüren',
```


## [2026-09-14T01:24:14.785Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"roar\" \"rumble\" \"riot\" \"rumour\" \"rumor\" \"rid\" \"rip\" \"rob\" \"robe\" \"rover\" \"rubbish\" \"rubble\" \"rough\" \"rug\" \"rugged\" \"rag\" \"ragged\" \"rupture\"; do echo \"=== $w ===\"; grep -n \"^$w,\" KLN_1966.txt | head -3; done"
}
```


### [2026-09-14T01:24:16.201Z] TOOL RESULT

```
=== roar ===
33001:roar,  intr.  and  tr.  v.  —  ME.  roren,  raren,  fr.  OE. rarian,  rel.  to  MDu.  reeren,  ‘to  roar’,  OHG. reren,  MHG.  reren,  ‘to  bleat’,  G.  rohren,  ‘to troal’,  from  the  I.-E.  imitative  base  *re-,  *ra-, ‘to  cry,  roar’,  whence  also  OI.  rayati,  ‘barks’, Lith.  reju,  reti,  ‘to  scold,  chide’,  Lett,  reju,  riet, ‘to  bark’,  OSlav.  revq,  rjevq,  ‘I  roar’,  L.  raucus (for  *ravicos),  ‘hoarse’.  See  raucous  and  cp. words  there  referred  to.
=== rumble ===
33328:rumble,  intr.  v.,  to  make  a  low,  heavy  noise ;  tr.  v., to  cause  to  make  such  a  noise.  —  ME.  romblen, rumblen,  of  imitative  origin.  Cp.  Du.  rommelen, G.  rummeln,  ‘to  rumble’,  ON.  rymja,  ‘to  roar, grumble’,  rytnr,  ‘a  roaring,  grumbling’,  and  see rumor.
=== riot ===
32952:riot,  n.  —  ME.  riote,  riot,  fr.  OF.  riote  (F.  riotte), fr.  rioter,  rihoter,  ‘to  make  a  disturbance’,  which is  of  uncertain  origin.
32954:riot,  intr.  v.  —  ME.  rioten,  fr.  riote,  riot.  See  riot,  n. Derivatives:  riot-er,  n.,  riot-ing,  adj.,  riot-ing-Iy, adv.
=== rumour ===
=== rumor ===
=== rid ===
32875:rid,  tr.  v.  —  ME.  ruden,  ryden,  fr.  ON.  rydja,  ‘to clear,  empty,  rid’,  which  is  rel.  to  OHG.,  MHG. riuten,  G.  reuten,  ‘to  clear  land’,  OHG.  riuti, ‘cleared  land’,  and  to  OFris.  rothia,  MLG.  ro- den,  MHG.  roten,  G.  roden,  ‘to  clear’,  and  prob. cogn.  with  Avestic  rao(i)bya,  ‘to  cultivate’; prob.  fr.  I.-E.  *reudh-,  ‘to  clear  land’,  enlarge¬ ment  of  base  *reu-,  ‘to  dig  up’,  whence  also  L. ruere,  ‘to  dig  up’.  (L  ruere  in  this  sense  is  not rel.  to  ruere,  ‘to  fall  down’  (see  ruin). Derivative:  ridd-ance,  n. ridable,  adj.  —  Formed  fr.  ride  with  suff.  -able.
=== rip ===
32957:rip,  tr.  and  intr.  v.,  to  tear  off,  divide.  —  Of Scand.  or  LG.  origin.  Cp.  Fris.  rippe,  ‘to  tear off',  MLG.  reppen,  Flemish  rippen,  Swed.  reppa, Dan.  rippe,  ‘to  tear,  rip’;  possibly  of  imitative origin.
32959:rip,  n.,  a  worthless  person.  —  Prob.  a  var.  of rep,  abbreviation  of  reprobate, riparian,  adj.,  pertaining  to  the  bank  of  a  river.  — Formed  with  suff.  -an  fr.  L.  riparius,  ‘that  which frequents  riverbanks’,  fr.  ripa,  ‘riverbank,  sea¬ shore’,  which  is  prob.  cogn.  with  Gk.  ipelneiv, ‘to  tear  down’,  epiTrvr,,  ‘a  broken  cliff  or  crag’, ON.  rifa,  ‘to  tear,  break',  MHG.  rif,  ‘river- bank’.  See  rive,  river,  and  cp.  Ripuarian.  For  the ending  see  suff.  -ian.
=== rob ===
33005:rob,  tr.  and  intr.  v.  —  ME.  robbett,  fr.  OF.  rober (whence  F.  derober,  to  steal'),  fr.  OF.  robe, ‘booty;  booty  of  garments;  gown,  dress,  robe', fr.  WTeut.  *rauba,  ‘booty’.  Cp.  OHG.  roub, 'spoil,  plunder’,  roubon,  ‘to  rob',  and  see  reave. Cp.  also  robe.
=== robe ===
=== rover ===
=== rubbish ===
33247:rubbish,  n.,  waste,  refuse.  —  ME.  robeux,  robous, robys\  perh.  orig.  meaning  ‘that  which  is  rubbed ofi”  and  rel.  to  rub.
=== rubble ===
33249:rubble,  n.,  broken  pieces  of  stone.  —  ME.  robyl, robel,  rubel,  prob.  rel.  to  prec.  word.
=== rough ===
33191:rough,  adj.  —  ME.  rouh,  rough,  ruw,  rugh,  fr.  OE. ruh,  Tough,  untrimmed,  uncultivated’,  rel.  to MDu.  rii,  ruuch,  ru,  Du.  ruig,  OHG.  ruh,  ruher, MHG.  ruch,  ruher,  G.  rauh,  rauch,  fr.  I.-E.  base *ruq-,  *rug-,  whence  also  Lith.  raitkas,  ‘wrinkle’, runkit,  ritkti,  ‘to  shrink’,  raukiit,  raukti,  ‘to wrinkle’,  OI.  rukfdh,  ‘rough’,  L.  ruga,  ‘wrinkle’. Cp.  ruga.  Cp.  also  ruff,  the  fish,  ruffian,  rug. Derivatives:  rough,  n.,  tr.  v.,  and  adv.,  rough- age,  n.,  rough  material,  rough-en,  tr.  and  intr.  v., rough-en-er,  n.,  rough-er,  n.,  rough-ish,  adj., rough-ish-ly,  adv.,  rough-ish-ness,  n.,  rough-ly, adv.,  rough-ness,  n.
=== rug ===
33310:rug,  n.  —  Of  Scand.  origin.  Cp.  Swed.  rugg, ‘rough  hair’,  ON.  rogg,  ‘tuft,  shagginess';  rel.  to E.  rag  and  rough  and  to  the  next  word. Derivative:  rugg-ing,  n.
=== rugged ===
=== rag ===
31567:rag,  tr.  v.,  to  tease.  —  Of  uncertain  origin.  Cp. bullyrag.
=== ragged ===
=== rupture ===
```


## [2026-09-14T01:24:29.019Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leaf_of(lineno):\n    return t.count('\\f','',0) # placeholder\n# compute cumulative\nimport bisect\nff=[i for i,l in enumerate(lines) if '\\f' in l]\ndef leaf(ln):\n    return bisect.bisect_left(ff,ln-1)\nfor ln,w in [(33001,'roar'),(33328,'rumble'),(32952,'riot'),(32875,'rid'),(32957,'rip'),(33005,'rob'),(33247,'rubbish'),(33249,'rubble'),(33191,'rough'),(33310,'rug'),(31567,'rag v')]:\n    print(w, 'line',ln,'leaf',leaf(ln), '-> approx printed p.', (leaf(ln)-12)*2, 'or', (leaf(ln)-12)*2+1)\nEOF"
}
```


### [2026-09-14T01:24:30.202Z] TOOL RESULT

```
roar line 33001 leaf 719 -> approx printed p. 1414 or 1415
rumble line 33328 leaf 725 -> approx printed p. 1426 or 1427
riot line 32952 leaf 718 -> approx printed p. 1412 or 1413
rid line 32875 leaf 716 -> approx printed p. 1408 or 1409
rip line 32957 leaf 718 -> approx printed p. 1412 or 1413
rob line 33005 leaf 719 -> approx printed p. 1414 or 1415
rubbish line 33247 leaf 724 -> approx printed p. 1424 or 1425
rubble line 33249 leaf 724 -> approx printed p. 1424 or 1425
rough line 33191 leaf 723 -> approx printed p. 1422 or 1423
rug line 33310 leaf 725 -> approx printed p. 1426 or 1427
rag v line 31567 leaf 690 -> approx printed p. 1356 or 1357
```


## [2026-09-14T01:24:31.062Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^rag,  n\\|^rag, n\\|^rumor\\|^rumour\\|^robe,\\|^rover\\|^rugged\\|^ragged\\|^rupture\" KLN_1966.txt | head -20; echo \"=== search loose ===\"; grep -n \"rumor,  n\\|robe,  n\\|rover,  n\\|rugged,  adj\\|ragged,  adj\\|rupture,  n\" KLN_1966.txt | head -20"
}
```


### [2026-09-14T01:24:31.162Z] TOOL RESULT

```
1233:rupture.
=== search loose ===
23818:microbe,  n.,  a  minute  organism;  popular  name for  a  bacterium.  —  Coined  by  the  French  sur¬ geon  Sddillot  in  1878  fr.  Gk.  pixpd?,  ‘small’, and  plo?,  ‘life’.  See  micro-  and  bio-.
30326:probe,  n.  — -  Late  L.  proba,  ‘proof’,  back  forma¬ tion  fr.  L.  probare.  See  probate,  adj.
30327:probe,  tr.  and  intr.  v.  —  Partly  fr.  probe,  n., partly  directly  fr.  L.  probare.
33007:a  ‘wolflike  fish’),  fr.L./«pu.?,‘wolf '.  See  lupine,  adj . roband,  also  raband,  robbin,  n.  (naut.)  —  Du. raband,  compounded  of  ra,  ‘sailyard’,  and  band, ‘band’.  The  first  element  is  rel.  to  ON.  ra,  Dan. raa,  Swed.  ra,  Du.  ra,  MHG.,  G.  rahe,  ‘sail- yard’,  and  possibly  also  to  MHG.,  G.  ragen, etc.,  ‘to  jut  out’;  see  rake,  ‘to  project’.  For  the second  element  see  band,  ‘tie’, robber,  n.  —  ME.  robbere,  fr.  OF.  robere,  fr. rober ,  ‘to  rob’.  See  rob  and  agential  suff.  -er. robbery,  n.  —  ME.  robberie,  fr.  OF.  roberie,  fr. rober.  See  prec.  word  and  -ery. robe,  n.  —  ME.,  fr.  OF.  robe,  ‘booty;  booty  of garments;  gown,  dress,  robe’  (whence  F.,  ‘gown, dress,  robe’);  see  rob.  Cp.  OProveng.  rauba, ‘booty;  gown,  robe’.  It.  roba,  ‘things,  goods; stuff ;  cloth’,  Sp.  ropa,  ‘clothes,  clothing,  dress, garments,  robe,  gown’,  which  are  also  borrow¬ ed  fr.  WTeut.  *rauba.
33230:Derivative:  rove,  tr.  v.,  to  twist  rolls  of  wool, rover,  n.,  sea  robber,  pirate.  —  ME.,  fr.  MDu. rover,  fr.  MDu.  (=  Du.)  rover,  fr.  MDu.  (= Du.)  raven,  ‘to  rob,  plunder’,  fr.  MDu.  (=  Du.) roof,  ‘spoil,  plunder’,  which  is  rel.  to  OE.  reaf, of  s.m  .,  reafian,  ‘to  reave’.  See  reave  and  agential suff.  -er  and  cp.  rove,  ‘to  wander’, rover,  n.,  1)  a  mark  selected  at  random  (a  term  of archery);  2)  one  who  wanders.  —  ME.,  fr.  ro-
33313:Rugby,  n.,  also  Rugby  football.  —  So  called  from the  system  of  football  first  played  at  Rugby School  in  Warwickshire, rugged,  adj.  —  Formed  fr.  rug  with  1st  suff.  -ed. Derivatives:  rugged-ly,  adv.,  rugged-ness,  n.
33357:Ruppia,  n.,  a  genus  of  plants,  the  ditch  grass (hot.)  —  ModL.,  named  after  the  German  bot¬ anist  Heinrich  Bernhard  Ruppius  (1689-1719). rupture,  n.  —  ME.  ruptur,  fr.  MF.  (=  F.)  rupture, fr.  L.  ruptiira,  ‘a  fracture,  breach’,  fr.  ruptus,  pp. of  rumpere,  ‘to  break,  burst,  tear,  rend’,  which is  cogn.  with  OE.  reafian,  ‘to  seize,  rob,  plun¬ der',  reofan ,  'to  tear,  break ,  ON.  rjufa ,  to break’.  See  reave  and  -ure  and  cp.  abrupt,  bank¬ rupt,  corrupt,  corruption,  disrupt,  disruption, erupt,  eruption,  interrupt,  interruption,  irrupt, irruption,  rote,  ‘routine’,  roture,  rout,  rabble  , rout,  ‘to  put  to  flight’,  route,  routier,  routine, rupestrian,  rutter.
34248:scrobe,  n.,  a  groove  ( zool .)  —  L.  scrobis ,  ditch, trench’,  which  is  cogn.  with  Lett,  skrabt,  to hollow  out,  scrape’,  skrabinat,  ‘to  gnaw  at’,  ON. skarpr,  OE.  scearp,  ‘sharp’.  See  sharp  and  cp. next  word.
40324:trove,  adj.,  found.  —  See  treasure-trove, trover,  n.,  acquisition  of  property  (law).  —  Lit.  ‘a finding’,  fr.  OF.  trover  (F.  trouver),  ‘to  find’, orig.  ‘to  compose  poetry;  to  invent’,  fr.  VL. *tropare,  ‘to  make  tropes,  sing’,  fr.  L.  tropus, ‘trope,  song’.  Cp.  O Proven?,  trobar,  Sp.  and Port,  trovar.  It.  trovare,  ‘to  find’,  which  also  de¬ rive  fr.  VL.  *tropare,  and  see  trope.  Cp.  also troubadour  and  words  there  referred  to. trow,  intr.  v.,  to  believe,  suppose.  —  ME.  trewen, trowen,  fr.  OE.  treowian,  truwian,  ‘to  believe, trust’,  rel.  toOS.  triuwian,  ON.  trua,  Dan.,  Swed. tro,  MLG.,  MDu.  trouwen,  Du.  (ver)trouwen, OHG.  tru(w)en,  MHG.  truwen,  trouwen,  G. trauen,  Goth,  trauan,  ‘to  believe,  trust’,  and  to OE.  treow,  ‘belief,  trust,  faith,  engagement, truth'.  See  true  and  cp.  words  there  referred  to. trowel,  n.,  a  tool  used  for  spreading  mortar, plaster,  etc.  —  ME.  true!,  fr.  F.  truelle,  fr.  Late L.  truella,  fr.  L.  trulla,  ‘a  small  ladle,  dipper, scoop’  (whence  Sp.  trulla),  dimin.  of  trua,  a ladle',  fr.  I.-E.  base  *twer-,  *tur-,  ‘to  turn,  twist, twirl’,  whence  also  Gk.  TopOvi],  ‘implement  for stirring,  ladle’,  xopuveiv,  ‘to  stir  up’,  OE. Pwxre,  pwere,  OE.  pwiril,  OHG.  dwirii,  MHG. twirel,  G.  quirl,  Icel.  pyrill,  ‘twirling  stick’,  ON.
```


## [2026-09-14T01:24:41.562Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 685 690 693 694 716 719; do echo \"=== leaf $L ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$L\"' {print substr($0,1,220)}' KLN_1966.txt; done"
}
```


### [2026-09-14T01:24:42.521Z] TOOL RESULT

```
=== leaf 685 ===
rsh.  —  Fr.  earlier  quakemire, which  is  compounded  of  quake  and  mire.  Cp. quag,  ‘bog,  marsh’.
Derivative:  quagmir-y,  adj. quahog,  also  quahaug,  n.,  the  N.  American  clam.
—  Of  Algonquian  or
=== leaf 690 ===
upbearer',  fr.  rab,  ‘chief’,  and  shaqu,  pi. shaqe,  ‘cupbearer’  (see  ZDMG.,  53,  pp.  1 16  If.) For  Akkad,  rab  see  rabbi  and  cp.  the  first  ele¬ ment  in  prec.  word.  Akkad,  shaqu,  ‘high�
=== leaf 693 ===
anunculus  and  -arium. ranee,  n.,  a  variety  of  Belgian  marble.  —  F.,  of unknown  origin.
ranch,  n.,  a  large  farm  with  its  buildings  and  em¬ ployees.  —  Mexican  Sp.  rancho,  ‘a  small  farm’
=== leaf 694 ===
h  is  cogn.  with  Gk.  ep^itTEoftat,  ‘to pluck  off,  feed  on’,  Alb.  rjep,  ‘I  strip,  rob’, Lith.  raples,  ‘tongs’,  ap-repiu,  ‘I  take,  seize’,  fr. I.-E.  base  *rep-,  ‘to  snatch,  seize�
=== leaf 716 ===
��word’,  lit.  ‘that which  is  spoken’,  p?jm.;,  ‘speech’,  and  to  Eipm (for  *flpi6>),  ‘1  say,  speak’,  sfpwv  (for  *ft- ptcov),  ‘dissembler’,  lit.  ‘sayer’  (i.e.  one  who speaks  
=== leaf 719 ===
an. rille,  ‘furrow’,  derive  fr.  LG.  rille.
Derivatives:  rill,  intr.  v.,  to  flow  as  a  rill,  rill-et, n.,  a  small  rill.
rillettes,  rilletts,  n.  pi.,  potted  meat.  —  F.  rillettes, rel.  to  ril
```


## [2026-09-14T01:24:53.286Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\n# map char offset of each headword occurrence to leaf\nimport re\ndef leaf_at(idx):\n    return t.count('\\f',0,idx)\nfor pat in ['\\nroar,  intr','\\nrumble,  intr','\\nriot,  n','\\nrid,  tr','\\nrip,  tr','\\nrob,  tr','robe,  n.  —  ME.','rover,  n.,  sea','rugged,  adj','\\nrug,  n','rupture,  n.  —  ME','\\nrough,  adj','rubbish,  n.,  waste','rubble,  n.,  broken']:\n    i=t.find(pat)\n    print(repr(pat), 'leaf', leaf_at(i) if i>=0 else None)\nEOF\necho \"=== anchors ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==749 {print substr($0,1,150)}' KLN_1966.txt"
}
```


### [2026-09-14T01:24:54.563Z] TOOL RESULT

```
'\nroar,  intr' leaf 719
'\nrumble,  intr' leaf 725
'\nriot,  n' leaf 718
'\nrid,  tr' leaf 716
'\nrip,  tr' leaf 718
'\nrob,  tr' leaf 719
'robe,  n.  —  ME.' leaf 719
'rover,  n.,  sea' leaf 724
'rugged,  adj' leaf 725
'\nrug,  n' leaf 725
'rupture,  n.  —  ME' leaf 726
'\nrough,  adj' leaf 723
'rubbish,  n.,  waste' leaf 724
'rubble,  n.,  broken' leaf 724
=== anchors ===
ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze,  MDu.
seaward
secure
gesaete,  ‘seat’,  OHG.  gisdyi,  MHG.  gesiige, ‘seat;  siege;
```


## [2026-09-14T01:25:08.680Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ndef leaf_at(i): return t.count('\\f',0,i)\nfor pat in ['\\ncherub','\\nrigid','\\nrite,','\\nrise,','\\nrival','\\nriver,','\\nroad,','\\nrock,','\\nrogue','\\nrole','\\nroll,','\\nroom,','\\nroot,','\\nrope,','\\nrose,','\\nrot,','\\nround,','\\nroyal','\\nrubber','\\nruby','\\nrude,','\\nrule,','\\nrun,','\\nrust,']:\n    i=t.find(pat)\n    print(pat.strip(), '-> leaf', leaf_at(i) if i>=0 else None, '≈p.', (leaf_at(i)*2-24) if i>=0 else '')\nEOF"
}
```


### [2026-09-14T01:25:10.434Z] TOOL RESULT

```
cherub -> leaf 155 ≈p. 286
rigid -> leaf 717 ≈p. 1410
rite, -> leaf None ≈p. 
rise, -> leaf None ≈p. 
rival -> leaf None ≈p. 
river, -> leaf None ≈p. 
road, -> leaf None ≈p. 
rock, -> leaf 720 ≈p. 1416
rogue -> leaf 720 ≈p. 1416
role -> leaf None ≈p. 
roll, -> leaf 720 ≈p. 1416
room, -> leaf 721 ≈p. 1418
root, -> leaf 721 ≈p. 1418
rope, -> leaf 721 ≈p. 1418
rose, -> leaf 722 ≈p. 1420
rot, -> leaf 722 ≈p. 1420
round, -> leaf 723 ≈p. 1422
royal -> leaf 676 ≈p. 1328
rubber -> leaf 724 ≈p. 1424
ruby -> leaf 724 ≈p. 1424
rude, -> leaf 725 ≈p. 1426
rule, -> leaf None ≈p. 
run, -> leaf 715 ≈p. 1406
rust, -> leaf None ≈p.
```


## [2026-09-14T01:25:19.514Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=715 && NR<=727 {printf \"--- leaf %d ---\\n\",NR; print}' KLN_1966.txt | grep -nE \"^[[:space:]]*1[0-9]{3}[[:space:]]*$|--- leaf\" | head -40"
}
```


### [2026-09-14T01:25:20.550Z] TOOL RESULT

```
1:--- leaf 715 ---
15:1342
65:--- leaf 716 ---
78:1044
107:1345
117:--- leaf 717 ---
132:1346
133:1347
171:--- leaf 718 ---
221:--- leaf 719 ---
272:--- leaf 720 ---
291:1353
315:--- leaf 721 ---
339:1354
340:1355
364:--- leaf 722 ---
387:1356
411:--- leaf 723 ---
460:1359
473:--- leaf 724 ---
506:1360
534:--- leaf 725 ---
583:--- leaf 726 ---
645:--- leaf 727 ---
651:1365
```


## [2026-09-14T01:25:28.149Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==716 || NR==717 {printf \"\\n=== leaf %d ===\\n\",NR; print}' KLN_1966.txt | grep -nE \"^[[:space:]]*1[0-9]{3}[[:space:]]*$|^ri|=== leaf\" | head -60"
}
```


### [2026-09-14T01:25:29.255Z] TOOL RESULT

```
2:=== leaf 716 ===
15:1044
44:1345
45:rial
55:=== leaf 717 ===
67:ria,  n.,  creek;  inlet.  —  Sp.  rla,  ‘mouth  of  a  river’, rel.  to  rio,  ‘river’.  See  rio. rial,  n.  —  A  var.  of  riyal. rial,  n.,  the  monetary  unit  of  Iran.  —  Pers.,  fr. Arab,  riyal.  See  riyal.
68:rialto
69:ritacimento
70:1346
71:1347
72:rialto,  n.,  exchange,  market.  —  It.  Rialto,  name of  a  quarter  of  Venice  where  the  exchange  was situated.  The  name  is  a  contraction  of  Rivoalto , former  name  of  the  island  on  which  Venice  was built,  fr.  L.  rivus  altus,  ‘deep  river'.  For  the  first word  see  rio,  for  the  second  see  alt. riant,  adj.,  smiling.  —  MF.  (=  F.),  pres.  part,  of rire,  ‘to  laugh’,  fr.  L.  ridere.  See  risible  and  -ant. Derivative:  riant-ly,  adv. riata,  n.  —  See  reata.
73:rib,  n.  —  ME.  ribbe,  fr.  OE.  ribb,  rel.  to  OS.  ribb, ribbi,  ON.  rif,  Dan.  ribbe,  Swed.  rev ,  OFris.  ribb, rebb,  MDu.  ribbe,  Du.  ribbe,  rib,  OHG.  ribba, rippi,  MHG.  ribbe,  riebe,  rippe,  G.  Rippe,  and to  the  second  element  in  OHG.  hirni-reba,  ‘skull’, lit.  ‘brain  cover’,  fr.  I.-E.  base  *rebh-,  ‘to  root, cover’.  The  ribs  are  so  called  because  they  “roof  ” the  cavity  of  the  chest.  From  the  same  base  de¬ rive  OSlav.  rebro  (for  *rebhro),  ‘rib’,  Gk. Ipstpciv,  spsrtTeiv,  ‘to  roof’,  Spocpo?,  ‘reeds  used for  thatching  houses,  roof’,  L.  orbis,  ‘round  sur¬ face,  orbit,  orb’.  Cp.  orb,  reef,  ‘ridge  of  sand’, rep,  ‘thick  fabric  of  silk’.
76:riband,  n.,  a  ribbon  (archaic).  —  Older  spelling of  ribbon,  with  excrescent  -d.
83:rice,  n.  —  ME.  rys,  ris,  fr.  OF.  ris  (F.  riz),  fr.  It. riso,  fr.  VL.  *oryzum,  fr.  L.  oryza,  fr.  Gk. oputa,  fr.  OPers.  brizi,  fr.  Afghan  vrize,  ult.  fr.
86:rich,  adj.  —  ME.  riche,  a  blend  of  OE.  rice, ‘powerful,  strong,  noble,  rich’,  and  OF.  ( —  F.) riche,  riche,  ‘rich’;  this  latter  is  borrowed  fr. Frankish  *riki,  ‘powerful’.  OE.  rice  and  Frankish *riki  are  rel.  to  OS.  riki,  ON.  rikr,  OHG.  rihhi, ‘ruler;  powerful, rich’,  Swed.  rik,  Dan.  rig,  ‘rich’, OFris.  rike,  Du.  rijk,  MHG.  rich,  riche,  ‘pow¬ erful,  rich’,  G.  reich,  ‘rich’,  Goth,  reiks,  ‘ruler; powerful,  rich’.  These  words  derive  fr.  Teut. *rik-,  ‘ruler’,  which  is  borrowed  fr.  Celtic  *rig- (cp.  OIr.  ri,  gen.  rig),  ‘king’,  a  cognate  of  OI. raj-,  rajan-,  L.  rex,  gen.  regis,  ‘king’.  According¬ ly  OE.  rice,  etc.,  orig.  meant  ‘kingly,  royal’  [cp.
93:rick,  n.,  pile,  stack.  —  ME.  reke,  fr.  OE.  hreac, rel.  to  ON.  hraukr,  Du.  rook,  ‘heap’,  and  pos¬ sibly  to  ON.  hryggr,  OE.  hrycg,  ‘back,  ridge’. See  ridge  and  cp.  ruck,  ‘crowd,  herd’. Derivatives:  rick,  tr.  v.,  to  heap  up  in  ricks, rick-er,  n.
94:rick,  tr.  v.,  to  sprain;  n.,  a  sprain.  —  A  var.  spell¬ ing  of  wrick.
95:rickardite,  n.,  a  copper  telluride  (mineral.)  — Named  after  the  American  mining  engineer Thomas  Arthur  Rickard  (1864-1953).  For  the ending  see  subst.  suff.  -ite.
96:rickets,  n.  —  Fr.  rachitis;  influenced  in  form  by rick  or  wrick,  ‘to  twist,  sprain’, rickety,  adj.  —  Prob.  fr.  prec.  word  with  adj.  suff. -y-
99:rickle,  n.,  a  small  heap  or  pile.  —  Formed  fr. rick,  ‘pile’,  with  dimin.  suff.  -le.
101:rickrack,  n.,  serpentine  braid  of  silk,  cotton  or wool.  —  Antiphonic  reduplication  of  rack,  ‘to stretch’.
102:ricksha(w),  n.  —  Abbreviation  of  jinricksha  (q.v.) ricochet,  n.,  the  rebounding  of  an  object.  —  F., of  uncertain  origin.
104:rictus,  n.,  opening  of  the  mouth,  gape.  —  L.  ric¬ tus,  pp.  of  ringi,  ‘to  open  wide  the  mouth’.  See ringent.
105:rid,  tr.  v.  —  ME.  ruden,  ryden,  fr.  ON.  rydja,  ‘to clear,  empty,  rid’,  which  is  rel.  to  OHG.,  MHG. riuten,  G.  reuten,  ‘to  clear  land’,  OHG.  riuti, ‘cleared  land’,  and  to  OFris.  rothia,  MLG.  ro- den,  MHG.  roten,  G.  roden,  ‘to  clear’,  and  prob. cogn.  with  Avestic  rao(i)bya,  ‘to  cultivate’; prob.  fr.  I.-E.  *reudh-,  ‘to  clear  land’,  enlarge¬ ment  of  base  *reu-,  ‘to  dig  up’,  whence  also  L. ruere,  ‘to  dig  up’.  (L  ruere  in  this  sense  is  not rel.  to  ruere,  ‘to  fall  down’  (see  ruin). Derivative:  ridd-ance,  n. ridable,  adj.  —  Formed  fr.  ride  with  suff.  -able.
107:ridden,  pp.  of  ride.  —  ME.  riden,  fr.  OE.  (ge)riden, pp.  of  ridan.  See  ride.
108:riddle,  n.,  enigma,  puzzle.  —  ME.  redels,  rideles, fr.  OE.  rsedels,  rSedelse,  formed  with  the  subst. suff.  -els  fr.  OE.  riidan,  ‘to  advise,  counsel,  de¬ liberate,  guess,  interpret,  read’.  The  s  in  ME. redels  w
```


## [2026-09-14T01:25:42.260Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\n# find all page-number markers (a line that is only a 4-digit number 1000-1800)\nmarks=[(m.start(), int(m.group(1))) for m in re.finditer(r'\\n[ \\t]*(1[0-7][0-9]{2})[ \\t]*\\n', t)]\ndef page_of(idx):\n    best=None\n    for pos,p in marks:\n        if pos<idx: best=(pos,p)\n        else: break\n    return best\nfor pat in ['\\nroar,  intr','\\nrumble,  intr','\\nriot,  n','\\nrid,  tr','\\nrip,  tr','\\nrob,  tr','robe,  n.  —  ME.','rover,  n.,  sea','rugged,  adj','\\nrug,  n','rupture,  n.  —  ME','\\nrough,  adj','rubbish,  n.,  waste','rubble,  n.,  broken','\\nrumor','\\nrag,']:\n    i=t.find(pat)\n    print(pat.strip().ljust(22), page_of(i) if i>=0 else 'NOT FOUND')\nEOF"
}
```


### [2026-09-14T01:25:43.702Z] TOOL RESULT

```
roar,  intr            (8260467, 1353)
rumble,  intr          (8309307, 1360)
riot,  n               (8223013, 1346)
rid,  tr               (8223013, 1346)
rip,  tr               (8223013, 1346)
rob,  tr               (8260467, 1353)
robe,  n.  —  ME.      (8260467, 1353)
rover,  n.,  sea       (8309307, 1360)
rugged,  adj           (8309307, 1360)
rug,  n                (8309307, 1360)
rupture,  n.  —  ME    (8339701, 1365)
rough,  adj            (8300207, 1359)
rubbish,  n.,  waste   (8309307, 1360)
rubble,  n.,  broken   (8309307, 1360)
rumor                  NOT FOUND
rag,                   (7917605, 1297)
```


## [2026-09-14T01:25:58.742Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD rwš ===\"; grep -n \"rw[sš]\" SOD_pages.txt | head -20; echo \"=== SOD leaf for p346 = leaf 412 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==412 {print substr($0,1,800)}' SOD_pages.txt"
}
```


### [2026-09-14T01:25:59.817Z] TOOL RESULT

```
=== SOD rwš ===
4158:     Hen. AION 1965, 32.6; BSTBL, Dhy. 397; >rwst,
7982:                                                                    arpaste Orpst'k) =»*rpsty, 'rwstk
8077:1494 Yt'w zrwsc      B                                          1507 Vty1 M, C          -VrrO" j->)(uy >^    jJ)u~r,*ij-i<j
8540:                                                                  1653 'sptsrwsyy         M                       jb^jUySuT
8689:     aste ©3sg. irr. ^'sty1                                              1705 'strwsk => swsk
8690:     AVS 225; GMS 782; TSP 2, 164, 997                                   1706 'strwsk     M =* 'strwsk
8727:           MDii piOll 3, >strwsnk                                                (o)saycne =»zJry sy'n'k
8915:     astac- ©Av. arstat                                           1786 Jstrwsk M            (.Ji^^i^j^S)^ JjL* (j/ ^5C)
8916:     twenty-sixth day of the month                                     (a)s9rusk ?, (o)susk ? Ostrwsk)
10514:     (o)zna ^jn*                                                        (o)zrusc ©Parth. zrhwst =*zrwsc
14066: 3613 Srwst't   S                                  j~.jx; *^yu.
14917:      STii 1.87; BSTii 843.38; C2, 68 V7 n pl49                  3948 frxrws M                                 v>«*"Jj(^
17333:      GMS 34; STi 8.7; Sund. AoFi 252.7                    4788 qnygrwsn M          (cT>^ ukfj^- jO^J^jj <s°.
17531:             kars     ©<Av. karsa     =*qrws-                              kart (krth) ©<Av. kardta\ Khwar. krc% Yaghn.
17622:4883 qrws- M, C                      &£jJuto*~£
17627:4884 qrwsny C                               juI^jlulT                STi 68.22; Gersh. Sogd. Cpds. 1945, 148; GMS
19410:5478 mrws- C                              o^^r-J <0-> jo~o
20050:            BSTii: C2, pi. mzyxh GMS 1249; MSP b30,                   5710 nMsptsrwsy M                 (^J*, >UTW<-o-)jUyU
22818:                                                                   fearful                                    pcmrws-
22879:                                                             6679 pcmrws-
=== SOD leaf for p346 = leaf 412 ===
                                                                                                                               344
 rtyh


           him"; rtywr "and up", rtypr "and in"; STii                   8554 rwpcyk1 B                                    J?1 J**
           p595; SCE p69; BSTBL, pl29; KG pl89; C2                                day
                                                                              rupcik
           p224; MSP p52; rtty% TSP 5.61
8542 rtyh B                                        ^                         TSP  5.124
                                                                             (o/)mouth
     ratya                                                              8555 rwc M, S         (*^ <jl*jjj fit L ^S J j->>^)jjj
        generousi
```


## [2026-09-14T01:26:00.040Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT raod ===\"; grep -n \"raod-\\|raodaiti\\|raod\\b\" BRT.txt | head -20; echo \"=== CHEUNG raud ===\"; grep -n \"raud\\|RAUD\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T01:26:00.124Z] TOOL RESULT

```
=== BRT raod ===
3587:•  y  apa.rao9^nina-Adj.,FFM.:  s.  ^raod-.
4643:*)  Vgl.  noch  iraod-  mit  ;■(.  Die  Lehrteit  des Awesisschiiiers  ist  drei  Jahre,  je  eins  bei  drei Lehrern.  Bei  jedem  soll  er  nach  einem  halben Jahre  das  Gelernte  bereits  sicher  im  Gedächlnij haben,  so  dass  er  beim  Vortrag  keine  Verstösse macht.   Andernfalls  ist  der  Lehrer  zu  wechseln;
4835:lesen?  Oder  Iiraes.  3?  —  ")  D.i.  ä-iydi;  ai. iyi.  —  'J>  Pü. ;  ähekinilan.  —  '4)  D.  i.  ä-lyäi.  — 'S>  Pü.  i  apar  raiitan.  —  »*)  Lesung  unsicheri FoYZDMG.^i^  363:  apariy  bäbirum  naiy  aiiyä- yam. —  '?>  Pü.;  Sitdk  tu  an  ^ariel  buland*') uzet.  Vgl.  lu  (KU-  No.  2,  'ar-  No.  8  f.,  usinidyäi, gam-  Ho.  16,  'Vax!-  No.  7  und  ^raod-  No.  5. Ganz  merkwürdige  Lesungen  bei  Gdn.  KZ. ja 332  und  Mills  lausit^idyäi;  s.  auch  WEST SBE.  J7. 387.  —  »*J  Nach  dem  Metrum  blos ytinti  IM  lesen.  —  =91  H.l.  faiti\iytU;  ai. iyaie.  Hds.  pailiiU.  Pü.:  pt,  verstümmelt. — 30)  D.  i.  faiH\iy&nle,  Neubildung  zu  lySili, N0.I3.  Pu.:  tmdeutlich.  —  3>)  Pü. : /alQEtd ;  s. dazu  SWienAW.ä/.84i.  7 :  paül  bavhn  fiailman s/tpam.  —  3')  PQ.s  api  raßan.  Die  Formen mit  ä  zeigen  alle  den  Anfang  pSray'  (pärayäl —  S  268.  3  b—,  aber  paräiii;  V.  g.  39  f., 'S-  9f-);  ich  schliesse  daraus,  dass  das  ä  durch den  Einfluss  der  Praes.-Klasse  30  hervorge- rufen ist.  —  3J)  Hds,  •äi%i,  wie  V.  22.  7.  — 34)  Them.  Hds.  say';  der  l.  Buchstabe  ist nicht  recht  deutlich.  —  35)  Text  unsicher,  — 3«)  \ai. /vrayä/;  s.  No.  32.  —  37)Pu.!/fa- tiaßan,  ßanämltan.  Meist  them.,  mit  ß^y (nach  S  26S.  3  b?).  —  »)  %  304  H-  30.  — 3»  Vgl.  S  2^.  2,  iSPrA.  Oder  vU.  Absol, ai.  (nir)äyaml—  40)  S.  noch  No.  9,  I7ff.,22, 29  und  Bthu  AF.  2.  72.  —  4')  Dass  das  np. äyad  das  Praev.  ä  enthalt  (GIrPh.  I  b.  132), scheint  mir  keineswegs  sicher.  Vgl.  mp.  ii:äy/i {s.  No.  27)  und  jAw.  iKäili.  —  W  So  (für  la la}i  E.  unter  ui.
7290:■)  Die  beiden  Warter  haben  zusammen  eine 3.  Flur,  verdrängt;  etwa  *uparaßi3nit ,  lu '■raod:  I
8333:SoperL  zum  V.  iraod- 1).  —  ai.  vgl.  uparodAa- m.,  ufaeoäAin-  Adj,  —  D  Nach  Sp.  'der  auf- gewachsenste',  Dst.  'tshi  baut  de  taille'  viel- mehr mm  V.  'raad:
10572:•  g.  (,  j.)  xraod-  V,  '(sich)  ängstigen', Praes.   i  xraed-,
12441:asahya  axäyai  (sd.)  ggnedim  Y.  37, 17;  — aiäunqm  . .  uruns  .  .  kudüJiatanqmAt  .  . yailqm  vahehl^  'na  vanainti  va  vSnghm va  vaonarS  va  H.  3g.  z;  —  karapanS kavayasca  .  .  ySng  ^S  urva  ::^a!^a  xrao- dat  (sd.)  'na  Y.46.11;  —  Ö  dngvats *tnandaHg  *9r?tael  (sd.)  haihim  yehya urvü  xraodaiti , .  Y.  ji,  13;  —  tsm  *vä ahsm  dtTgvantS  .  .  'na  nailal  (sd.)  Y.^y/. so;  zT.  verwendet  V.f.  fia;  s.  a;  —  ySi .  .  aiäm>m  vandtn  (sd.)  . .  töi  daoiStig dqn  yS  drsgvats  °na  ",.  die  —  in  AnDaiva Haus  fUr  das  Ich  des  ^rv^enossen!"  Y. 4^.  4*>.  a)  im  jAiv.:  alaonqm ..  ahümla 'nam/ai*  iaooasäi  urvänsmca  fravaiSmia yagamaide  Y.  a6.  4;  —  asni  iyazamaide\ manä  . .  °nä  [yazamaidi]  saoryantqm  yaaa- vtaide  Yt  13.  7^;  —  aisS  zT  växs . .  a  va^S ahunB  vaityS . .  uruna^a  'tiaca  (IS.)  span- vanti  (sd.)  H.  J.  4;  —  'nqm  .  .  yaoldai- är/a  dha  zl  aifihä  asH  yaosdaitis  kahmai- Ht  ..  havaya  tnsvS  'naya  yl  hvqm  'nqm yaozdaite  humataisla  ..  V.  10.  19*';  —  um vä  ahOm  drvaniö  *^a  *'na  msirtnttyJJ [a/isiäi  a/fuhe]  V.  5. 6a;  —  aiiihä  dim vütaya  fr-Jmita  (sd.)  salayeiti  ya  hava 'naT>  kaininS  k>hrpa  srlrayh  .  .  aat  Alm aoxta  ..yS  nars  asaonü  urva  alca  Karditis ahi  ..?  äat  hl paiH.aoxta  ya  hava  'na  .. az?m  ba  U  ahmt  .  .  yä  hava  'na  *:^ai- paihejanvö  {sd.Y'  H.2.9— 11; — arahvam 'nqm  V.^.ai  PüZ.s),  io.  19  PüZ.
15166:ai.  pädyati ;  s.  lu  ^raod-  No.  I.  —  VgL  paüiya- mit  No.  I.  —  Pü. :  verschieden  ;  s.  No,  1  ff.  — ')  Pü.:  öpoilan.  —  »)  Pü.:  afii  (noganel;  vgl. No.  3  und  Hoan  NpEt.  24.  —  ))  Pfi. ;  . .  lu^in Aaniircl  (np.  antlrad)  .  .,  et].:  kuS  haniär  e an  yät  iarl  bavct.  —  «  Jp  I,  Mf  a.  —  S)  Hds. (auch  ZU  P.  //)  dt^aänS;  \  statt  %y,  s.  paiay- No.  I.   Pü.:  siyän;  vgl.  No.  6  und  säy-  No.  7.
15213:—  I)  In  Nachahmung  des  Wechsels  zwischen d  und  %  im  Wnrzelauslaut,  s.  ^raod-  No.  I, Doch  ist  zu  beachten,  dass  sich  ar.  ^fa/jutai and  *padia/iü  in  der  Bedeutung  berührten.  — »  Nach  der  üblichen  Erklärung,  die  jedoch nicht  einwandsfrei  ist.  —  3)  Hds.  J^&ayeili; s.  aber  Pu.
24897:•  g.  'raod-,  j.  'rao^-"  V.  'jammem'. Praes.  3  uru^a-,  30  (Kaus.)  uraddya-'^; s-AoT.   I  raos-.
24900:auch  ZDMG.  44-  553  lu  sbal.  rdtag.  — ')  S  3^.  —  ^*  Eine  höchst  auflallige  Diver- genz. —  4)  Ich  sehe  in  der  Sielt«  eine  .An- spielung auf  Y.  2p.  9.  —  i)  Vgl.  Pü.  lU  Iraaä-, itoöd:  —  6)  Erl.:  tuland  mai  älil.  Wie  ffit 'raod-;  s.  aber  V.ig.^^,  wo  die  gleiche  Ver- bindung. —  7>  Angebl.  drax/  'Baum'I
24901:•  j.  'raod-  V.  'wachsen'.  Praes.  2  rao^a-i 27  urulya-;  PerC  i  urürud-,  —  PPfp. urusda-,  urusta-^^;  In£  raose^^.
24905:'raod-  Scbluss
24906:3raod-  Noten
24921:•  j-,  g.  ^raod-,  j.  'rao9^''  V.  'abhalten'. Praes,  2  raoia-,  rao^a-,  30  (Iter.)  «70- 6aya-;  Perf.  i  ursraod: — PP(P.  "urusäa", 'urusta-  'K
24936:*raod-
24938:•  j.  ^raod-  V.  'fliessen',  Praes.  2  raooa-, 30  (Kaus.)  raoaaya-.
24947:KompE.  —  Vgl.  roöOiia-  No.  4.  —  Zum  V. *raod:  —  ai,  riha-  m.  'Erhebuuf;',  np,  rdi 'Gesicht'.  —  Pü.:  {75  sälai)  äriiiia.
24958:•  j,  'raoft-  V.  'jammern':  s,  unter  'raod-,
24959:•  j.  'raoS--  V.  'abhalten';  s.  unter  ^raod .
=== CHEUNG raud ===
6098:*IE COGNATES: Lat. fraus ‘deception’, Umb. frosetum ' fraudatum’ 
6687:unconnected (cf. NEVP: 91), rather from *Hraud (Cheung 2004: 129). 
6899:IE provenance for this II. root cannot be ascertained. The comparison to ON fraud 
13107:*(H)raud ‘to tear, break’ 
13120:*Hraud 193 
13123:© The evidence for an Ir. root *(H)raud, which would derive from IE *(H)reud-, is 
13138:*Hraud ‘to grow (bigger)’ 
13182:194 *(H)raudH 
13195:*(H)raudH ‘to moan, (be)wail’ 
13216:*IE COGNATES: Lat. rudö ‘to cry, roar’, OCz. ruditi ‘to sadden’, Lith. rauda, Latv. 
14084:*H,l(e)ud'- (> Ir. *Hraud) that has given rise to a new ablaut series: > Ш. *Hurd’/ 
20820:*raud ‘to hinder, block, ward off” 
20885:if there is a possible Ir. cognate, on which see *raud. On the etymology see also 
24938:*NWIR: NP tarfand(ah), tarvand(ah) ‘lie, falsehood, deceit, fraud’, Zaz. tiritis/tiren- 
28255:’rws- does not derive from *raud. = Ghilain: 49, 81 | DMMPP: 53 
28626:contamin. with *xraud) 
28917:448 *xraud 
28942:*xraud ‘to become/make angry ?, afraid ?, confused ?' 
28955:confuse, distract’. © Dissimilated from *pari/a-xrauda- < *раг/а-хгаиба- < 
28956:*pari/a-xrauda(ia)-. © Samadi: 158 f.
```


## [2026-09-14T01:26:05.789Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== Cheung *(H)raudH ===\"; sed -n '13182,13240p' CHEUNG.txt; echo; echo \"=== Cheung 28230-28270 ===\"; sed -n '28225,28275p' CHEUNG.txt"
}
```


### [2026-09-14T01:26:05.869Z] TOOL RESULT

```
=== Cheung *(H)raudH ===
194 *(H)raudH 


*SANSKRIT: rodh ‘to grow’ (RV+) = EWAia П: 467 
*PIE *H,leud'- ‘to grow, rise’ = LIV: 248 f. | Pok.: 306 f., 684 f. 
*IE COGNATES: Gr. £Ae0£pog (m.) ‘free man, non-slave’, Olrish Juss ‘plant’, Goth. 


liudan, OE leodan ‘to grow’ 
*REFERENCES: TFL I: 285a; Andreev — PeSéereva: 316b; DKS: 367a; WIM II/1: 82; Werba 1997: 229 f; 
Paul 1998: 312a; Shahbakhsh: s.v. rud-, amrud-; Korn 2005: 313, 377 


*(H)raudH ‘to moan, (be)wail’ 

*AVESTAN: гаоб- ‘to moan, (be)wail’ = Liste: 59 

Pres. athem.: INJ. 3sg. them. YAv. urudat (F 9), med. 3sg. ? raosta (Y 29.9, Y 9.24), 3pl. YAv. uru0ən (V 
3.32), med. 3pl. YAv. urudonta (V 19.45); Aor. athem.: med. INJ. 3sg. ? raosta (see above); Partic.: pres. 
caus. YAv. urüóaiiant- (Yt 13.151); Caus.: INJ. med. 3sg. ? OAv. urüdoiiata (Y 44.20). © On the 
interpretation of Av. raosta see Kellens 1984: 88, fn. 6. 


*NWIR: ? NP Jundidan/lund-, Gz. lund-/lunda ‘to snarl, snort’, Awrom. lawna ‘to 
bewail’, Gz. Juve ‘howling, wailing’, rud ‘cry of mourning (from women)’. 9 The 
frequent appearance of l- in these forms needs to be explained. 

*MISC: Par. ruh-/rhint ‘to weep’, (partic. pres.) rhintó ‘weeping’ || (+ *fra-) Orm. &ü-, 
S'aw-/sustuk, Sustak ‘to weep’ = Saw-/So stók, Sóstok 

*SANSKRIT: rod’ ‘to weep, bewail’ (RV+) > EWAia II: 465 

«PIE *(H)reudH- ‘to weep, cry’. OG The reconstruction of an initial laryngeal is based 
on the premise that IE roots cannot begin with an initial *r-. > LIV: 508 | Pok.: 867 
*IE COGNATES: Lat. rudö ‘to cry, roar’, OCz. ruditi ‘to sadden’, Lith. rauda, Latv. 


raüda ‘lament’, ON rauta ‘to roar’, OE réotan ‘to complain, weep’ 
*REFERENCES: IIFL I: 284a f., 409a; IIFL II: 409a; Fraenkel II: 704; WIM II/1: 79; WIM II/2: 702, 729; 
Werba 1997: 314 f.; Kiefer 2003: 207 


*HrauH (*HrabH ?) ‘to crackle; growl’ 
*AVESTAN: Y Av. uru- ‘to crackle’ = Liste: 59 
Partic.: pres. (Gsg.) Y Av. uruuatö (Yt 14.11, Yt 14.19, V 22.3) 


*SOGDIAN: SSogd. rBZ-, BSogd. rBz- (inch. ?) ‘to bark’ 

Pres.: SUBJ. 3р1. BSogd. rBz'nt; Inf.: SSogd. rBZ't 

*CHORESMIAN: rw- ‘to growl’ => Samadi: 173 

*NEIR: ? M. rev-, rav-/rivd, Yi. rov-/rivd- (why -v- ?), Yghn. rauZ-/ráuZta (inch. ?) 
‘to bark’ (-u- < *B 1) || (+ *abi-) ? Sariq. v(i)rew-/v(i)rewd ‘to howl, bay’, ? Wa. 
variy-/varoyd ‘to howl, bay’ (Lorimer) || (+ *4-) Oss. I. arawyn/aryd, D. arawun/arud 
‘to echo enormously’ 

*SANSKRIT: rav ‘to roar’ (RV+) > EWAia II: 439 

=== Cheung 28230-28270 ===


© The evidence for an Ir. root *uraiH is limited to Av. An IE provenance cannot be 
ascertained. 
*PIE — => LIV: 699 | Pok.: — 


*IE COGNATES: — 
*REFERENCES: Hoffmann 1968: 39 ff.; Werba 1997: 319 


*urais ‘to turn, spin’ 

*AVESTAN: YAv. uruuaés- ‘to twist, turn’ || (+ *abi-) ‘to turn to’ || (+ *aua-) ‘to turn 
down’ || (+ *fra-) ‘to turn to’ || (+ *ni-) ‘to turn to’ || (+ *ui-) ‘to separate’ = Liste: 
60f. 

Pres. ja-: IND. 3sg. Y Av. fraorisiieiti (Yt 10.9), ? Y Av. fraorisaiti (H 1.17), Y Av. fraoirisaite (V 9.40), 
3pl. uruuisanti (Yt 12.25), Y Av. fraoirisinti (Yt 13.46), INJ. 3du. Y Av. uruuisiiatom (Yt 19.82), SUBJ. 
lsg. YAv. ni.uruuisiiäni (Yt 17.57 Ё), 3sg. YAv. avoirisiiat (Yt 5.62), OPT. 35р. ҮАУ. fraoirisiiöit (V 
14.16), IMPV. 2sg. Y Av. ni.uruuise (Yt 17.60); Partic.: pres. med. Y Av. fraoirsimna- (Vr 12.5); Caus.: 
pres. IND. 3sg. YAv. auuaouruuaesaite (V 4.22, V 4.25), 3pl. YAv. pairi.uruuaesaiieinti (Yt 14.56), INJ. 
med. 3sg. YAv. uruuaesaiiata (Yt 13.89), SUBJ. 1sg. YAv. fraouruuaesaiieni (Yt 9.31), 35р. ҮАУ. 
auuaouruuaésaite (У 4.22, V 425) YAv. vi uruuaesaiiat (P 20) IMPV. med. 2sg. ҮАУ. 
aipi.uruuaesaiiag'ha (Yt 17.15) 

*MIDDLE PERSIAN: BMP I(y)stk /ristag/ ‘rope, string, thread’, ? MMP *rwys, BMP 
"Iwys /arwös/ ‘rope’ || (+ *abi-) MMP ’bryswm ‘silk? = DMMPP: 53b, 14b 
*PARTHIAN: (+ *4-) ’rws-, ’’rws- ‘to turn to, towards [intr.], face’. © "Despite Ghilain 
1939: 49 and 81, ’rws- and ’’rws- belong together", DMMPP: l.c. This implies that 
’rws- does not derive from *raud. = Ghilain: 49, 81 | DMMPP: 53 

Pres.: IND. 35р. "rwsyd, 3pl. ’rwsynd, SUBJ. 1р1]. ’rws’m, IMPV. 25р. ’rws; Partic.: perf. pass. "rwst, П 
"rws'd, ’rws’d; Inf.: II ’rws’d 

*SOGDIAN: ? CSogd. гуу ‘spun’ || (+ *a- ?) ? BSogd. ’rw’stk, ’rw’stkw, ’rw’st’k 
‘bound, fixed’, CSogd. ‘гух ‘bandage’ (GMS: $116, 157) 

*CHORESMIAN: rYsY- ‘to spin’, гуз ‘thread’ © Samadi: 176 

*NWIR: NP réstan, ristan/ris-, résidan/rés-, risidan/ris-, Kurd. res-/restin, Abz. 
résta/rés-, Abyan. resta/res-, Awrom. restáy/res-, (LW ?) Gz. rés-/résa, Gur. (Kand) 
-ris-, -räs-, Khuns. ris-/rist, risa, Meim. bem-reft/a-ri:s-, Nn. ressaye/ress-, Qohr. 
ris(t)a/ris-, Siv. res-/res, ris, rese, Varz. resse/res- ‘to spin’, Bal. rist, rést/rés- ‘to 
twist (threads)’, (EHB) rést’, rés6/rés- ‘to spin’, NP ristah ‘fiber, filament, etc., Yzd. 
(Zor.) résta ‘handmade noodles, macaroni; dough rolled thin then rolled up and cut 
thin into strings’, NP arvis, arvis ‘a hair rope’ (LW) || (+ *abi-) Bal. (b)resag ‘to 
spin’, NP abrésum ‘silk’ || (+ *ui-) Kurd. (Sor.) guris ‘rope, string’ 

*NEIR: Pash. réSal ‘to spin’, Yghn. riwes-/riwesta ‘to twine, spin’ || (+ *abi-) Oss. I. 
elvisyn/elvest, D. elvesun/elvist ‘to spin’, Pash. wresol ‘to spin’, (LW) Pash.
```


## [2026-09-14T01:26:21.165Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== grep roar/bark ===\"; grep -n \"roar\\|bark\\b\\|to  bark\" SOD_pages.txt | head -20; echo \"=== leaves 413-415 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=413 && NR<=415 {printf \"\\n--- leaf %d ---\\n\",NR; print substr($0,1,1500)}' SOD_pages.txt"
}
```


### [2026-09-14T01:26:23.063Z] TOOL RESULT

```
=== grep roar/bark ===
15733:     roar ing ^yryn-1
15877:                                                                    (ftf)roar
23380:6839 p5y p5y B                             .          ^jA,           roaring
28130:      (to)bark                                                       raxn   ©Yaghn. raxn      =»rxn-
28494:     OcOroar
28503:     roaring
28508:        roaring ? ©prcs. part. =»rws-2
30617:     noise, roaring
30625:     roaring
37672:as   878, 884, 2165, 2170, 2185,            OcOattempt    6849                      (to)bark 8465
39301: (to)roar       4275, 8593                                                      Saragh   8956, 8958
39302: roaring       4199, 6853, 8595, 8596,                                          Sassanid province   488
=== leaves 413-415 ===

--- leaf 413 ---
                                                                                                                     rwstm(y)

 345


      (/<9)make grow                                                       TSP 2.1193, 7.26, 8.39, 29; BSTBL, Padm. 52, 61
      Sogdica. 47.4; GMS 547
 8567 rw8ny(y) M                          ^ij^j^Jm                    8577 rwke'tCh) =» rwk
      ro8ne (rwdny) ©ace. -nw-, nom. -ny; pi. -/iyf
                                                                      8578 rwkSyspr* =* rwk
      (a/Obrass, (o/)copper, brazen                                            pl30
      GMS 1058, 1246; BBB pl34; Hen. BSOAS 8,                         8579 rwkp'r =* rwk
        1936, 584; C2 gloss. 23R4, rwdny, 91R8,                       8580 rwp— B, C                   o^,jj <c*3j i o^>- <o-^^
        rwdnw; pi. rwdnyt, Hen. Tales. 473, 51                             rop ©fraup\ Pahl. rob
                                                                           0<?)pick up
8568 rw8yn>k B                                    ijj <J=iJJ
                                                                           VJ 695; STi 47.17, 48.21
     roSene =*rw8ynch
                                                                      8581 rwps(h)   B, M                                   a\>3j
       (<?/)brass
       TSP 2.527                                                           rup(a)s ©Parth. robas\ Khot. ruvasa-, Khwar.
                                    

--- leaf 414 ---
 rwsty(h)                                                                                                                     346

         TSP 13.2, 5, 24, 25, 26, 28 ii 4, 1 1, 12                             ob. -y, STi 60.1; BSTii 857.15: C2, 22V15
 8590 rwsty(h) M, C                                   oju^j^c^j        8601 rwtc^ =» rwcyk
      ruste ©pp.
                                                                       8602 rwtcyk     MD =* rwcyk
         grownBSOAS 12, 307, 29; BSTi 112, 120                         8603 rwwt     M =» rwt
         Hen.
                                                                       8604 rwxsn-     M, C                         j^3J i^3J
 8591 rwstyk(h)       S                         c~*3J Jp\ <j^3J
      rtistik                                                                roxsn   ©nom. gen. -y(yk ace. -w; abl. voc. -\ pi.
                                                                               -t\ -d\ nom. f. -*; ob. pi. -ty\ -tyh =*rwysn,
         (from)Rust
         MDii B-9R2.15; -h B17R7                                               rywsn-, light
                                                                             luminous, rxwsn-
8592 rws-1 B, C                               0-^ ^bo^                       GMS 40, 127, 520, 1191-9; BBB b56, 58 b5, 80,
     ros ©Skt. sravati ©pt. nv?/-                                              97 f 80, 46, 566; W-Lii 569; KG 2338; MSP c20
     Onflow, (/cOdrop, (^)st

--- leaf 415 ---
347

8612 rwz- C                   j^^Je* <o\ZjjjT <jsJ>-             8626 ryj M                                     rync'q
                                                                                                     (iij'J^^J^^^jjJ
                                                                      rez =»ryz, ryz
     roz
     (/o)desire, (/cOwish                                             desire, wish
     GMS 379; STii 1.78; C2, 94V12, 51V24; AVS 138                    GMS 66; BBB 538, 567, 585, 679 bH Sund. 1994,
                                                                        45.18
8613 rwzywn'y B                          alyj-x^^b.
     rozyone =*rwsywny                                           8627 ryj-    M                         J^l^y-i^bjjjl
     desirable, suitable                                              rez =*ryz-, ryz-
     BSTBL, Dhy. 215; GMS 1114; Lentz. STii p604                      (to)desire, (/o)be desirable
                                                                      BBB 605, 3sg. subj. rypt
8614 rwzny C                                          j^-'_^
     rozne ©pres. part.
     desiring                                                    8628 ryk B                   (& J <&j:J^->)<*ik <•*><* jj>
                                                                      rik ©<OP arika
      C2, 48V 18                                                      wicked

8615 rwzty> C                                       jjjT<J~-
```


## [2026-09-14T01:26:28.366Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==414' SOD_pages.txt; echo \"#### context lines 28480-28520\"; sed -n '28480,28520p' SOD_pages.txt"
}
```


### [2026-09-14T01:26:29.836Z] TOOL RESULT

```
 rwsty(h)                                                                                                                     346

         TSP 13.2, 5, 24, 25, 26, 28 ii 4, 1 1, 12                             ob. -y, STi 60.1; BSTii 857.15: C2, 22V15
 8590 rwsty(h) M, C                                   oju^j^c^j        8601 rwtc^ =» rwcyk
      ruste ©pp.
                                                                       8602 rwtcyk     MD =* rwcyk
         grownBSOAS 12, 307, 29; BSTi 112, 120                         8603 rwwt     M =» rwt
         Hen.
                                                                       8604 rwxsn-     M, C                         j^3J i^3J
 8591 rwstyk(h)       S                         c~*3J Jp\ <j^3J
      rtistik                                                                roxsn   ©nom. gen. -y(yk ace. -w; abl. voc. -\ pi.
                                                                               -t\ -d\ nom. f. -*; ob. pi. -ty\ -tyh =*rwysn,
         (from)Rust
         MDii B-9R2.15; -h B17R7                                               rywsn-, light
                                                                             luminous, rxwsn-
8592 rws-1 B, C                               0-^ ^bo^                       GMS 40, 127, 520, 1191-9; BBB b56, 58 b5, 80,
     ros ©Skt. sravati ©pt. nv?/-                                              97 f 80, 46, 566; W-Lii 569; KG 2338; MSP c20
     Onflow, (/cOdrop, (^)stream                                               b98 bl21; C2, 91R 11; Hen. BSOAS 12.307.11,
        TSP 2.139, 3sg. pres. nv&A, n pl70; VJ 7a, 1029;                       19; STii 2.11; BSTi 165; Sund. AoFiii 1975,
   —"     C2 gloss. 14V21, 22                                                  18V17
8593 rws-2 B, S                                                        8605 rwxsn)yr8mn M                                   ,-.*g,
     ros ©IE *reu(s)                            o*lS-                       roxsna-yar8(a)man ©<Av.
     OcOroar
                                                                              raoxsna-garoSdmana ©ob. -}y, -y}A
     TSP 13.21 apud. S W, IIJ 1976, 60; MSP b38                               ^rwysn^rSmnCh)
       n p52
8594 rws*     S(M) => rws>k(h)                                              GMS,  1218; BBB f85; BSOAS 12, 307.11; 21, 1221
                                                                            paradise
8595 rws>k(h) B                                                 oJJ^   8606 rwxsnVSmncyk        M                           j^>
                                                            J-S
     rosak, rosa (rws*)                                                     roxsna-yar5mancik      ©pl^     -^rywsn'yrSmncyk
     roaring
                                                                            paradisian
        VJ 61e apud. S W, IIJ 1976, 60; MSP b40                             GMS 1014; BBB f48
8596 rws'ny      S(M)                                                  8607 rwxsndr M                                      y^jj
        rosanc                                                              roxsndar, rxusndar (rxwsntr) ©nom. -y
        roaring ? ©prcs. part. =»rws-2
                                                                            brighter
        MSP bl24, pi. -/                                                    GMS 1284; KG 366
8597 rwsywny C                          ^\y^l^\>c~>3.                  8608 rwxsny>())q =» rwxsny'k
     rozyonc ©ace. -nw          ^rwzywn'y                              8609 rwxsny'k M, C                                  ^3J
     desirable
                                                                            roxsnyak (rwxsny>())q) ©ob. -y; pi. -f
        -*h>, BSTii 842.7; Benv. Eti 328; C2 p50 n4, 184,                     ^rywsny'kCh), rwysnyMcCh)
          68R7
                                                                            brightness \
8598 rwsn S(M)                                                              GMS 1110, 1221; BBB 485 pl34; BSOAS 12,
     rosn ©<Parth. rosn                                                       307.41; STi 31.12, 65.8, 43.16; Sund. AoFviii
        light                                               dT3J              1981 p217; STii 3.64, 1.27; C2 gloss. p224,
        KG 607-98                                                             W-Lii 546, 547.25, 548.19, 564, -A, MSP b28
8599 rwsnyr'yw S(M)                       <S~*3J u~*> iCT'3J j*41
                                                                              b97; CII 1990 p67 G4-5
     rosn-yriw                                                         8610 rwxsny^y* C                           jll^jh^3j
                                                                            roxsnyakya
     light souliviva anima)
        Sund. KG 607-8 pl89; AoF, 1979, 120 n49                             brightness
8600 rwt M, C                                        <;U-^j i*3J            STi 3.72; GMS 1111; STii 3.72
     rot (rwwt) ©<OP rautah-            ©ob. -y                        8611 rwxst- C                            j* j^y iqx*z±~^
     river                                                                  ruxst ? ^ryw^nt
        GMS 39, 530; STii 1.20; BSTii 860.35, 879.11: C2
                                                                            (/a)shine
          gloss. 22V7, 12, 23R11, 12, 23V5, 53R6, 87V11;                    BSTi 31; Benv. JA 1943-5; S W, IIJ 1976, 57n 60

#### context lines 28480-28520
                                                                       8604 rwxsn-     M, C                         j^3J i^3J
 8591 rwstyk(h)       S                         c~*3J Jp\ <j^3J
      rtistik                                                                roxsn   ©nom. gen. -y(yk ace. -w; abl. voc. -\ pi.
                                                                               -t\ -d\ nom. f. -*; ob. pi. -ty\ -tyh =*rwysn,
         (from)Rust
         MDii B-9R2.15; -h B17R7                                               rywsn-, light
                                                                             luminous, rxwsn-
8592 rws-1 B, C                               0-^ ^bo^                       GMS 40, 127, 520, 1191-9; BBB b56, 58 b5, 80,
     ros ©Skt. sravati ©pt. nv?/-                                              97 f 80, 46, 566; W-Lii 569; KG 2338; MSP c20
     Onflow, (/cOdrop, (^)stream                                               b98 bl21; C2, 91R 11; Hen. BSOAS 12.307.11,
        TSP 2.139, 3sg. pres. nv&A, n pl70; VJ 7a, 1029;                       19; STii 2.11; BSTi 165; Sund. AoFiii 1975,
   —"     C2 gloss. 14V21, 22                                                  18V17
8593 rws-2 B, S                                                        8605 rwxsn)yr8mn M                                   ,-.*g,
     ros ©IE *reu(s)                            o*lS-                       roxsna-yar8(a)man ©<Av.
     OcOroar
                                                                              raoxsna-garoSdmana ©ob. -}y, -y}A
     TSP 13.21 apud. S W, IIJ 1976, 60; MSP b38                               ^rwysn^rSmnCh)
       n p52
8594 rws*     S(M) => rws>k(h)                                              GMS,  1218; BBB f85; BSOAS 12, 307.11; 21, 1221
                                                                            paradise
8595 rws>k(h) B                                                 oJJ^   8606 rwxsnVSmncyk        M                           j^>
                                                            J-S
     rosak, rosa (rws*)                                                     roxsna-yar5mancik      ©pl^     -^rywsn'yrSmncyk
     roaring
                                                                            paradisian
        VJ 61e apud. S W, IIJ 1976, 60; MSP b40                             GMS 1014; BBB f48
8596 rws'ny      S(M)                                                  8607 rwxsndr M                                      y^jj
        rosanc                                                              roxsndar, rxusndar (rxwsntr) ©nom. -y
        roaring ? ©prcs. part. =»rws-2
                                                                            brighter
        MSP bl24, pi. -/                                                    GMS 1284; KG 366
8597 rwsywny C                          ^\y^l^\>c~>3.                  8608 rwxsny>())q =» rwxsny'k
     rozyonc ©ace. -nw          ^rwzywn'y                              8609 rwxsny'k M, C                                  ^3J
     desirable
                                                                            roxsnyak (rwxsny>())q) ©ob. -y; pi. -f
        -*h>, BSTii 842.7; Benv. Eti 328; C2 p50 n4, 184,                     ^rywsny'kCh), rwysnyMcCh)
          68R7
                                                                            brightness \
8598 rwsn S(M)                                                              GMS 1110, 1221; BBB 485 pl34; BSOAS 12,
     rosn ©<Parth. rosn                                                       307.41; STi 31.12, 65.8, 43.16; Sund. AoFviii
        light                                               dT3J              1981 p217; STii 3.64, 1.27; C2 gloss. p224,
```


## [2026-09-14T01:26:53.988Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24890,24905p' BRT.txt"
}
```


### [2026-09-14T01:26:54.037Z] TOOL RESULT

```
durch  das  Licht  sva.)  Belichtung':  :^aslairis (sd.)  .  .  °na  hvarp.dar>sya  hl  zfme  paiti nidaihlta  (näml.  atdibXs)  ". .  sollen  (die  Ge- beine) zu  ihrer  Belichtung  und  Besonnung auf  dem  Boden  niedergesetzt  werden"  V. tf.  51;  —  yär}.dräj5  .  .  sairi  (sd.)  . .  wwf nibäite  *na  hvar3.dar>sya  ztmd  bavainti "in  Jahresfrist  werden  Leichname,  dadurch dass  sie  auf  der  Erde  niedergelegt  dem Licht  und  der  Sonne  ausgesetzt  sind,  zu Erde"  V.  7. 46'';  45'*.
Komp.  mit  NP.  im  1.  Glied.  —  Pü.:  röhüh apar   mhumhih.    —   ')   In  NA.  fälschlich   ge-
■  j.  raoätna'vant-  Adj.  'lichtvoll,  leuch- tend';   °vant?m  yaba  manhfm  Az.  6;  —
barisma    .  .    'vantint     (ASm.     statt    n.) bämlM  YtJj.  55. 5.  unter  taoiaHOr.
•  p.  rautah-n,  'Fluss,  Strom':  adam  niy-
astsyam  imäm  yuviyäm  (sd.)  kt^lanaiy kacä  pirävJ'  nUma"  'Ic^  (NS.)  .  .  abiy *draya'  lyt^  hacä  pSrsH^  aitiy  ". .  vom Fluss  Nil  mit  Namen"  zum  Meer  . ."  D.
Zum  m.W.sravali  'er  fliesst';  vgl. 'urvan/:  — ai.  srölas-  n.,  np.  Töd.  —  Vgl.  %raBtah:  — ')  zKonslr.  i.  Bthl.  BB.  i4-  249.  Grav  1F. //.  311-
•  g.  'raod-,  j.  'rao^-"  V.  'jammem'. Praes.  3  uru^a-,  30  (Kaus.)  uraddya-'^; s-AoT.   I  raos-.
'jammern,  heulen',  im  gAw.  nur  vom  Rind gebraucht,  dagegen  imjAw,  nur  von  dafvi- schen  Wesen^';  a)  im  gAw.:  aica  gSus urv3  raostä  "und  ein  Jammern  erhob  da die  Seele  des  Stiers"  Y.  2g.  9.  a)  Kaus. 'jammern  machen':  yälä  kavä  *qnmSnT urüdsyatä  "und  wie  der  K.  es  (das Rind)  unaufhörlich  jammern  macht"  Y. 44.  »o^>.  b)  im  jAw.:  yai  pi/irif(sd.) dayäj  aal  daeva  uru^sn  y.J.^i;  —  uru- %?ftta  adäunta  dalua  drvarüB  V.  79. 45; —  k^nsänXm  .  .  yS  raosta  xsdkrS.kämya yS  davata  "den  K. . .,  der  jammerte  in  der Sorge  um  seine  Herrschaft,  der  sagte . ."  Y. g.24;  —  uruhajF.g.  S.  noch  "aparB.
ai.  irudat,  rodayaü.  —  Pü.  (lU  Y.  2pl ;  garül, (lu  Y.  44s.  "•«^'h  ditirti,  (lu  V.  j):  giRlül (Pa«s.l,  erl.:  kuiän  ihntn  u  mgtak  karl,  (lu  V. /p):  fehlt,(iuY.9):««/flj/6),  {va^l.g): gUitti. —  >)  Der  idg.  Verbalauslaut  Ut  d\  %.  auch ahd.  rioma  'beweinen',  ä  neben  d  |1)  hat sieb  nach  dem  Vorbild  solcher  Verba  ein- gestellt, da  in  alter  Zeit  dh  und  th  wech- selten; S  2j,  Bgm.  Grdr.s  /.  632.  Der  Aus- tausch von  -d-  mit  -%-  muss  später  in  grösse- rem Umfang  staltgefunden  haben,  daher  es kommt,  dass  ar.  -</■,  -dh-  ^  air.  -d-  im  Np. durch   y   (i)   und    i  vertreten   ist;   leliteres
auch  ZDMG.  44-  553  lu  sbal.  rdtag.  — ')  S  3^.  —  ^*  Eine  höchst  auflallige  Diver- genz. —  4)  Ich  sehe  in  der  Sielt«  eine  .An- spielung auf  Y.  2p.  9.  —  i)  Vgl.  Pü.  lU  Iraaä-, itoöd:  —  6)  Erl.:  tuland  mai  älil.  Wie  ffit 'raod-;  s.  aber  V.ig.^^,  wo  die  gleiche  Ver- bindung. —  7>  Angebl.  drax/  'Baum'I
•  j.  'raod-  V.  'wachsen'.  Praes.  2  rao^a-i 27  urulya-;  PerC  i  urürud-,  —  PPfp. urusda-,  urusta-^^;  In£  raose^^.
i)  'wachsen';  a%ra  ml  urvarä  raoifft/i
dby  Google
M93
'raod-  Scbluss
```


## [2026-09-14T01:26:55.756Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 reu ===\"; grep -n \"reu-, reu\\|reud-\\|reudh-\\|reup-\\|reuk-\" incoming/WLD/WLD_Bd2_pages.txt | head -30"
}
```


### [2026-09-14T01:26:55.856Z] TOOL RESULT

```
=== WLD Bd2 reu ===
23075:                                 reibh-    — reu-, reu-, ru-                     349
23125:1. reu-, reu-, ru- Schallwurzel „brullen, heisere Laute ausstoBen** (auch        vom
23131:350                                          reu-, reu-, ru-
23218:  reud-\         ai.    ruddti^      roditi „heult,     weint, jammert*^.         av. raod-    „weinen%
23424:von Johansson IF. 8, 162 f. 19, 124f. auf "^reud-s-to- zuriickgefiihrt, stellt
23426:   reudh- bes. „reuten, roden“.
23518:  reus- (kann nicht uberall auf "^reud-s- zuriickgehn, vgl. Persson Beitr.
23524:(s. o.   "^reudh-), nhd. mdartl. riester     „Lappen von Leder zum Schuhflicken“;
23657:358                                        reudh-
23674:reudh- „rot“.
23681:IP. 19, 124f., wo Gdf. ^reudh-s-to-‘, diese bestritten vonPersson Beitr. 325
23690:wie unten die auf ^reudh-s^ *rotidh-s, "^rudh-s- beruhenden Bildungen, iiber
23714:                                           reudh-                                       359
23744:    Aksl. rudz    „rot'^,   ruda „Erz, Metall“, rusz {^reudh-s-o- oder '^rondh-s-o-')
23801:*reudh- „rot'‘), lat. raudus, rodus, nidus und rudis mit abweichendem d
27353:     neben leug ein reug (s. reu-, reuk-^ vereinzelt reug- „aufrei6en“) zu
37573:das Yon letzterem schwer zu trennende qreup- „Schorf‘‘ (s. d.) im Balt,
38995:(s. u.qreup- „SchorP‘, wo auch fiber abg. Tcrupa „Krumchen“ usw.).
42082:struma „skrofulose Anschwellung der Driisen, dicker Hals“ {^streud-,
42107:spenstigkeit^^  zu got. uspriutan „beschwerlich fallen^ s. ^treud-),
42113:trudo      ^treud-) gehoren (Pedersen KG. I 160) oder wenigstena mit An-
42141:wohl vielmehr zu "^sreup-^ s. d.    eher hieher vielleicht lit. sirubas, lett.
42340:*     streudh- oder strent-: ags. strudan „raubeTi, pliindern^, strydan ,,be-
46697:sreup- „schorfiger Schmutz am Korper".
46712: aon Beitr. 445 zu ster-^ streup- „starren"). Beziehung zu sreu- „flieBen"
```


## [2026-09-14T01:27:05.475Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- WLD 23120-23135\"; sed -n '23120,23135p' incoming/WLD/WLD_Bd2_pages.txt; echo \"--- WLD 23215-23222\"; sed -n '23213,23222p' incoming/WLD/WLD_Bd2_pages.txt; echo \"--- WLD 23424-23450\"; sed -n '23424,23450p' incoming/WLD/WLD_Bd2_pages.txt; echo \"--- WLD 23795-23810\"; sed -n '23795,23810p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-14T01:27:05.591Z] TOOL RESULT

```
--- WLD 23120-23135
egseivo) von *£0£j^7]v nach Solmsen Beitr. z. griech. Wortf. 50). Davon ab-
zuleiten idg, ^risennl-s oder ^risniu-s „wer Keigung hat, wiederholt zu
strafen** = Eqlvvg,   Ygl. ai. risanyd- u. Prellwitz aaO.
   Altere Deutungen beiBoisacq280, FroehdeBB. 20, 188, KuhnKZ. l,439ff.

1. reu-, reu-, ru- Schallwurzel „brullen, heisere Laute ausstoBen** (auch        vom
       Laute beim Erbrechen, s. reug „sich erbrechen**; reii-7n&n\ ,,brummen,
       dumpf murmeln, murren** (daraus auch „zornig, wild** u. dgl.).
  Ai. rau-ti^ nivdti, ravati „heult, briillt, larmt, drohnt**, rdva-, ravdtha- m.
„Gebrull; gr. coovoyai „heule, briille, stoBe einen Schrei aus**, djqvdov „unter
Gebriiir*   (co-,   auch mchovyiq   s.   u.,   kann nach Kretschmer KZ. 38, 135 die
350                                          reu-, reu-, ru-



Interjektion w sein, oder nach Brugmann, z. B. 11^ 2, 817, wie in ai. am-
--- WLD 23215-23222
Bland, sprakhist. bidrag 33 f.; Zweifel z. B. auch bei dt. rdcheln^ Palk-Torp
u. rcBhe)  lett.
            ;
                      fuht^ aksL [rylcati^ ryknqii „brullen“, russ. rykaihsja
„m der Brunst sem“.
  reud-\         ai.    ruddti^      roditi „heult,     weint, jammert*^.         av. raod-    „weinen%
ai. roda-       m. „Klageton, Winseln, Weinen“                    (= ahd. rd^ m., vgl. lit. rmidd);
gr. qvCco2       (s.   0 .);   lat. rfido^   -ere,    -Ivi ,.schreien     (bes.   vom Esel),    briillen^

(die Quantitatsdoppelheit  kann alt sein, vgl. das Ai.; Zweifel bei Sommer
--- WLD 23424-23450
von Johansson IF. 8, 162 f. 19, 124f. auf "^reud-s-to- zuriickgefiihrt, stellt
Persson Beitr. 20 If., 298 Anm. 1 besser zu "^leitg- „brechen“).
   reudh- bes. „reuten, roden“.
  Av. raoidya- „urbar zu machen^" (nach BartholomaeAiran.Wb. 1496, Zfdt-
Wtf. 6, 231 zu:)
  anord. rjbda „reuten, raumen“, mhd. rieten st. v. „ausrotten, vernichten";
anord, rjbdrn, „offene gerodete Stelle imWald“, ahd.         „durch Keuten
urbar gemachtes Land“, riuten (^riutjan) „reuteu“, anord. rud n. ^gerodete
Stelle im Wald“, mnd. rot „das Eoden“, anord. rydja „roden; aufraumen,
ausrotten“, ags. a-ryddan „berauben, pliindern^; mhd. roten mnd. roden^
nhd. (aus dem Nd., gegen Kluge Gl. 3, 281, obwohl auch ahd.             nhd.
Hied „durch Roden urbar gemachtes Land*' heute nur mehr bairisch ist)
roden^ afries. ibrothia             (fiir   -rodid) „exstirpare**.
  Ahd. riostar ^Pflugsterz und Pflughaupt“ (Meringer IF. 18, 242) vielleicht
mit Suffix germ. -stra’~ hieher, eher aber zur Wzf. reiis-^ wie ags. reost
„ein Teil des Pfluges**.
   re tip- „ausreiBen, zerreifien, brechen";
   ai.   ro2)a^a^?^,verursachtRei6en, bricht ab", ntpyati „hat ReiSen im Leibe“,
ropa- n. „Loch, Hohle"* (=lit. raupal^ vgl. anord. rauf f. serb. rupa)\ him-
pdti jjZerbricht", luptd- jjZerbrochen, beschadigt" wohl mit idg. V)
  lat.   rumpo,^ -ere,        riipl,^    riiptiim „brechen**, riipes „steile Felswand, Klippe,
Felskluft,       jaher Abgrund*"
                            (in ahnlicher Bed, nhd. Hiepe „Schuttreuse‘*
und die tirol. Ortsnamen roupo, rotifo, geschrieben Happen, Hofen, Schatz
Mdart.      v.   Imst   62,       77),   rtipex,   -ids „ruppiger klotziger Mensch,                Riipel"
(vgl. lit. rupiis „rauh,            grob" und von      "^retih   dt.   roh)   ;
                                                                                  nicht hierher    ir.   ropp
--- WLD 23795-23810
   Ahd. aruszi, erxzzi, aruz, as. arut „Erz, Erzstiick^ an. ^rtog (^arufia-
iaugd) „Drittel eines jere‘‘ steht schon wegen des anl. a- abseits (ob wie
alb. arents „Stahr' vom Namen der durch ihre Waffenfabriken berxihmten
Stadt Arretium^, s. Schrader RL. 203; Weigand-Hirt 472 laSt Yerbindung
mit den obigen Erznamen offen).
  Fach Ipsen IP. 39, 235 sind lohd-, abg, ruda, aisl. raudi (scheinbar zu
*reudh- „rot'‘), lat. raudus, rodus, nidus und rudis mit abweichendem d
fremdartiger Yokalisation, ahd, aruzzi aus ^orud- wieder mit d und uner-
klarlichem Yokal undYorschlag des o, der germ, unerhort ist, wegen des
Schwankens der Formen als entlehnt zu betrachten. Daher besteht Hommels
Herleitung aus sum. urud letztlich gerechtfertigt.
  ^reu-i ist bloB wegen lat. rutilus „r6tlich“ angesetzt, wozu wohl die
Muiuli; wie bei gr. Xtiga ans ital.        kann t Substitution fiir ein ital.
d (/?) im Munde von Etruskern (Bartholomae BB. 12, 84) oder eines andem
nichtitalischen Yolkes der italischen Halbinsel sein, die zugleich das ital.
"^rudro- oder *rudero (: ai. rudhird-) zu "^rudjo- dissimilierten (Diss. aus
```


## [2026-09-14T01:27:16.203Z] TOOL CALL #37: Bash

```json
{
 "command": "pdftoppm -f 423 -l 423 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg423 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg423.png"
}
```


### [2026-09-14T01:27:17.964Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66328 Sep 13 21:27 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg423.png
```


## [2026-09-14T01:27:18.611Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT (Ernout-Meillet) ===\"; grep -n \"^rumor\\|^rumpo\\|^rudis\\|^rugio\\|rumor,\\|rudis,\\|rugio,\" LAT.txt | head -20; echo \"=== LEW_1910 ===\"; grep -n \"^rumor\\|^rumpo\\|^rudis\\|^rugio\" LEW_1910.txt | head -20; echo \"=== SYN ===\"; grep -n \"rumpere\\|rumor\\|rugire\" SYN.txt | head -10"
}
```


### [2026-09-14T01:27:18.723Z] TOOL RESULT

```
=== LAT (Ernout-Meillet) ===
28481:rumpotinus. Hornus et son ddrivd ne semblent plus usites aprbs Colu-
35511:ut in agro Gallico, quod e lateribus crudis, ut in agro Sabino, quod
46344:rumpo avec le sens de "troubler dans l'exercice de"; i. aliquem in
52779:Mot rare. Rattache par les an ciens a rudis, cf., outre la glose
54061:rudis, -e: grossier, brut. Au sens moral "non degrossi (oppose
54074:rudis, —is f.: baguette; particulibrement "fleuret du gladia-
54098:rudis qui s 1 en laisse bien rapprocher par le sens; noter aes rude.
54132:rugio, -is, -Ire: rugir. DErivE: rugitus, -us m.: rugissement.
54140:Cf. rumor, runco (et rugdt).
54256:rumor, -oris m.: bruit, rumeur publique. S'emploie au singulier
54262:simple * rumo (fait sur rumor, d'apres clamo, clamor) dont le fre¬
54279:rumpo, -ls, rupi (sur un futur archafque rupsit, v.Fest. cite
54350:rumpos^appellant. Conserve dans quelques dialectes italiens, M.L.
65717:Formes nominales, derives et composes: trudis,-is f.: pique; trudes
=== LEW_1910 ===
=== SYN ===
1430:Pol. ruczaj, Russ. rucéej, ‘brook’ (Boh. rucej ‘torrent’) : SCr. ruknuti, ChSl. rykati ‘roar’, etc., (fr. *reuk-, beside *reug- in Lat. rugire ‘roar’, both exten- sions of *reu- in Skt. ru- ‘roar’, etc. (Walde-P. 2.349 ff.). Briickner 467.
1596:Lat. saxum ‘large stone, rock’ (> It. sasso ‘stone, rock’) : secadre ‘cut’, and prob. used first of a sharp cliff. Cf. rupes ‘cliff’ : rumpere ‘break’. Walde-P. 2.474. Ernout-M. 899.
3815:Ir. rop, rob, perh. as orig. ‘fierce beast’ (but for actual comprehensive use see Laws, Gloss. 618) fr. *rup-no-s : Lat. rumpere ‘break’, OE réofan ‘break’, réafian ‘plunder’, or fr. *rub-no-s : Goth. raupjan, OHG roufen ‘pluck’, etc. Walde-P. 2.354, 355.
14206:Lat. frangere, rumpere Sw. bryta, briicka SCr. —_ lomiti
14227:Feist 105. Lat. rumpere (>It. rompere, Fr.
14247:ON rjifa, OE réofan : Lat. rumpere, above, 2.
14307:Rum. rupe (also ‘break’), fr. Lat. rumpere ‘break’ (9.26).
19340:Grk. dragdelpw Goth. frawardjan Lith. gadinti NG xara ON _ spilla Lett. maitat Lat.  corrumpere Dan. fordarve ChSl.  atleti
19348:2. Lat. corrumpere (also ‘destroy’; in fig. sense ‘corrupt’, as mod. derivs. most- ly; but ME corrupt also ‘spoil’, as NE in Bible, etc., NED s.v. corrupt vb.1.), epd. of rumpere ‘break’ (9.26), hence orig. ‘break to pieces’. Ernout-M. 876.
23216:SCr. rupa (also Slov., Ukr. for ‘hole in the ground, ditch’), fr. an extension of the root in ChSl. riivati ��tear’, rytt ‘dig’, like that in Lat. rumpere, OE réofan ‘break’, etc. (9.26). Cf. ON rauf ‘hole’ (above, 4). Walde-P. 2.355.
```


## [2026-09-14T01:27:21.957Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg423.png"
}
```


### [2026-09-14T01:27:22.526Z] TOOL RESULT

```

```


## [2026-09-14T01:27:22.521Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:27:50.000Z] TOOL CALL #40: Bash

```json
{
 "command": "sed -n '1,140p' tools/verify_check.py"
}
```


### [2026-09-14T01:27:50.050Z] TOOL RESULT

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


## [2026-09-14T01:27:54.550Z] TOOL CALL #41: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:27:54.560Z] TOOL RESULT

```


```


## [2026-09-14T01:27:56.918Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/riot",
 "prompt": "Full etymology of riot, including any mention of Latin rugire or Vulgar Latin *rugitare."
}
```


## [2026-09-14T01:27:58.041Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rubbish",
 "prompt": "Full etymology of rubbish, and of rubble if mentioned; any connection to Old French robe / rob."
}
```


### [2026-09-14T01:28:02.430Z] TOOL RESULT

```
# Etymology of "Riot"

The word "riot" has an uncertain origin, though etymologists propose a connection to Latin. According to the Online Etymology Dictionary, the noun emerged around 1200, initially describing "the following of a wrong scent by hounds." The term evolved through Old French *riot* and Anglo-French *rioute*, which meant "dispute, quarrel" and various forms of disorderly conduct.

## Possible Latin Connection

The dictionary notes a potential link to Latin *rugire*, meaning "to roar." This is presented as a speculative etymology rather than a confirmed one, as the entry states the origin is "of uncertain origin."

## Semantic Evolution

The meaning shifted significantly over centuries:
- **Early 14c**: "debauchery, extravagance, wanton living"
- **Late 14c**: "civil disorder, violent disturbance of the peace"
- **1909**: "something spectacularly successful" (theater slang)
- **1891**: "vivid display of colors"

The phrase "run riot" dates to the 1520s, drawing from the original hunting-related sense, while the Riot Act was formally established in 1714.
```


### [2026-09-14T01:28:03.563Z] TOOL RESULT

```
# Etymology of Rubbish

**Origin of Rubbish:**
The word "rubbish" emerged around 1400 from Anglo-French *rubouses*, meaning "waste, broken, or worn-out material." The term's ultimate origin remains unclear, as "there are said to be no apparent cognates in Old French." The spelling with -ish appeared in the late 15th century. By 1600, it had broadened to mean "any useless or worthless stuff."

**Connection to Rubble:**
Both words derive from similar Anglo-French roots and relate to demolished building fragments. The OED notes that *rubbish* appears "related in some way to rubble," though the exact connection remains obscure.

**Old French "Robe" Connection:**
Interestingly, "rubble" possibly connects to Old French *robe* (meaning garment/clothing, as in the verb "rob"), though this association is uncertain. The Middle English Compendium suggests possible Anglo-Latin forms (*rubisum*, *robusium*) as related sources.

In summary, while "rubbish" and "rubble" clearly share etymological roots pointing to demolished building debris, scholars acknowledge significant gaps in tracing the words to their earliest origins.
```


## [2026-09-14T01:28:06.108Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rag",
 "prompt": "Full etymology of rag (n., piece of cloth) and ragged; any Old Norse rögg connection."
}
```


## [2026-09-14T01:28:06.978Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rough",
 "prompt": "Full etymology of rough: Old English ruh, PIE root, and whether any Latin source (rudis) is mentioned."
}
```


### [2026-09-14T01:28:11.666Z] TOOL RESULT

```
# Etymology of "Rag" and Old Norse Connection

## Primary Etymology

The noun "rag" (meaning a torn cloth scrap) originated in the early 14th century, likely from Scandinavian sources. The etymological dictionary notes: "probably from a Scandinavian source (compare Old Norse _rögg_ 'shaggy tuft, rough hair')"

## Old Norse Connection

Yes, there is a documented Old Norse link. The entry traces the word through:

- **Old Norse _rögg_**: "shaggy tuft, rough hair"
- **Old Danish _rag_**: directly comparable form
- **Proto-Germanic _*rawwa-_**: the reconstructed ancestor
- **PIE root _*reue-_ (2)**: "to smash, knock down, tear up, uproot"

## Related to "Ragged"

The term may also derive from a back-formation of "ragged," though the Norse connection appears more likely. The word "ragged" itself developed as an adjective meaning rough or shaggy from the noun "rag."

The etymology emphasizes some uncertainty—the sources indicate "probably" rather than definitive proof, acknowledging that an unrecorded Old English cognate of the Norse form could also explain the English word's origins.
```


### [2026-09-14T01:28:12.349Z] TOOL RESULT

```
# Etymology of "Rough"

## Old English Origins

The word "rough" traces back to Old English *ruh, rug-*, meaning "not smooth to the touch, coarse (of cloth); hairy, shaggy." It derives from West Germanic *\*rukhwaz* and ultimately Proto-Germanic *\*rukhaz*.

## Potential Indo-European Connections

The etymology document suggests the Proto-Germanic root "is perhaps related to the source of Sanskrit *ruksah* 'rough'" and mentions connections to Latin *ruere* ("to rush, fall violently, collapse") and *ruina* ("a collapse"). However, **Latin *rudis* is not mentioned** in this etymology entry.

The documented related roots include Lithuanian *raukas* (wrinkle) and *rukti* (to shrink), suggesting broader Indo-European connections to concepts of roughness and shrinking.

## Sound Evolution

Notably, "the original *-gh-* sound was guttural, as in Scottish *loch*," showing how pronunciation shifted over time in English.
```


## [2026-09-14T01:28:18.865Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '893,897p' AHD_watkins1985.txt | cut -c1-1200"
}
```


### [2026-09-14T01:28:18.926Z] TOOL RESULT

```
culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king
reu-'
ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to r
reu-?
reu-2, Also reue-. To smash, knock down, tear out, dig up, uproot. 1. Suffixed o-grade form *rous-o- in Ger- manic *rawwa- in: a. Old Norse régg, réggr, woven tuft of wool: RAG}; b. Norwegian rugga, rogga, coarse cover- let, akin to the Scandinavian source of RUG. 2. Basic form *reu- in Latin ruere, to collapse, cause to collapse: RABBLE, RUIN. [Pok. 2. reu- 868.] reudh-', Red, ruddy. I. O-grade form *roudh-. 1. Ger- manic “raudaz in: a. Old English réad, red: RED; b. Old Norse rauthr, red (> reythr, rorqual): RORQUAL. 2. Ger- manic *raudnia- in Old Norse reynir, mountain ash, rowan (from its red berries), akin to the source of ROWAN. 3. Latin rijfus (of dialectal Italic origin), reddish: RUFES- CENT, RUFOUS. 4. Latin rdbus, red, in robigd, ribigo, rust: RUBIGINOUS. 5. Latin rdbur, rdbus, red oak, hard- ness, and rdbustus, strong: ROBLE, ROBORANT, ROBUST; CORROBORATE, RAMBUNCTIOUS. II. Zero-grade form *rudh-. 1. Form *rudh-d- in Germanic *rud6 in: a. Old English rudu, red color: RUDDLE, RUDDY; b. Old English rudduc, robin: RUDDOCK. 2. Suffixed form *rudh-sto- in Germanic *riist- in Old English rdst, rust: RusT. 3. Latin rubeus, red: ROUGE, RUBEOLA, RUBY; RUBEFACIENT 4. Latin r
```


## [2026-09-14T01:28:19.985Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rover",
 "prompt": "Full etymology of rover (pirate/wanderer): Middle Dutch rover, roven, connection to Germanic *raubon 'to rob'."
}
```


### [2026-09-14T01:28:24.823Z] TOOL RESULT

```
# Etymology of "Rover"

The word "rover" has two distinct etymological paths:

**Rover (n.1) - "Sea-robber, pirate"**
Dating to the late 14th century, this sense derives from Middle Dutch *rover* meaning "robber, predator, plunderer." The term particularly appears in the compound *zeerovere* ("sea-robber"), tracing back to the Dutch *roven* ("to rob") and ultimately to Proto-Germanic roots connected to plundering and seizing goods.

**Rover (n.2) - "One who wanders"**
Emerging in the 1610s, this meaning developed as an agent noun from the verb "rove," which itself originated around the 1530s from dialectal English and Old Norse sources. The modern sense referring to "remote-controlled surface vehicle for extraterrestrial exploration" entered the language in 1970.

Both definitions share a common thread of movement—whether marauding across seas or wandering across terrain—though their etymological roots and timeframes differ considerably.
```


## [2026-09-14T01:28:32.762Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"RUMOR\\|RIOT\\|ROAR\\|RUMBLE\\|RUG\\b\\|RAG[,;]\\|ROB[,;]\\|ROBE\\|ROVER\\|RUBBLE\\|RUBBISH\\|ROUGH\" AHD_watkins1985.txt | sed 's/\\(.\\{300\\}\\).*/\\1.../' | head -20; echo \"=== To bellow ===\"; grep -n \"To bellow\\|to bellow\" AHD_watkins1985.txt | sed 's/\\(.\\{600\\}\\).*/\\1.../' | head"
}
```


### [2026-09-14T01:28:33.969Z] TOOL RESULT

```
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (re...
369:*dru-ko- in Germanic *trugaz in Old English trog, wooden vessel, tray: TROUGH. 5. Suffixed zero-grade form *dru-mo- in Germanic *trum- in Old English trum, firm, strong (> trymman, to strengthen, arrange): TRIM. 6. Variant form *derw- in Germanic *terw- in Old Eng- lish fe(o)ru, resin, pitch (ob...
386:dhragh-. To draw, drag on the ground. Rhyming variant tragh-. 1. Germanic *dragan in: a. Old English dragan, to draw, pull: pRaw; b. Old Norse draga, to draw, pull (or Old English dragan): DRAG; c. Old English drexge, dragnet: DRAY; d. Old Norse *drahtr, drdttr, act of drawing, akin to the sourc...
406:[dreug-. Dry. Germanic root. 1. Old English driigoth, drigath, dryness, drought: DROUGHT. 2. Suffixed form *drig-iz in Old English dryge, dry: DRY. 3. Suffixed variant form *draug-n- in Old English dréahnian, to strain, drain: DRAIN.]
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE...
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base,...
621:hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click...
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583...
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. ...
837:“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound...
849:patér, father: PATRIOT; ALLOPATRIC, EUPATRID, PATRI- ARCH, SYMPATRIC. [Pok. paté(r) 829.]
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan...
897:reu-2, Also reue-. To smash, knock down, tear out, dig up, uproot. 1. Suffixed o-grade form *rous-o- in Ger- manic *rawwa- in: a. Old Norse régg, réggr, woven tuft of wool: RAG}; b. Norwegian rugga, rogga, coarse cover- let, akin to the Scandinavian source of RUG. 2. Basic form *reu- in Latin ru...
900:a. Old English risan, to rise: RISE; b. Old English drisan, to arise (G-, up, out): ARISE. 2. Germanic causative *raizjan in: a. Old English réran, to rear, raise, lift up: REAR?; b. Old Norse reisa, to raise: RAISE.] rtko-. Bear. 1. Latin ursus, bear (< *orcsos): URSINE. 2. Greek arkios, bear: ...
992:(s)preg-. To jerk, scatter. 1. Germanic *sprek-, *frek- in: a. Middle Dutch sprenkelen, to sprinkle, akin to the possible source of Middle English sprenklen, to sprinkle: SPRINKLE; b. Old Norse freknur, freckles (< “that which is scattered on the skin”): FRECKLE; C. Swedish dialectal spragg, twi...
1071:[taw-. To make, manufacture. Germanic root. 1. Ger- manic *taw- in Old English tow-, spinning (only in compounds such as tow-hiis, spinning house or room): Tow. 2. Germanic *tawjan, *taw6dn, to fashion, in Old English tawian, to prepare: TAW!. 3. Germanic *gatawja- (*ga-, collective prefix; see...
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old ...
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “three...
1106:upo. Under, up from under, over. 1. Germanic *upp-, up, in: a. Old English up, uppe, up: uP; b. Old English up-, upp-, up=: UP-; C. Middle Dutch op, up: UPROAR. 2. Ger- manic *upanaz, “put or set up,” open, in Old English open, open: OPEN. 3. Germanic *ufana, “on, above,” in Old English bifan, ...
1144:*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: W...
=== To bellow ===
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inf...
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- ...
```


## [2026-09-14T01:28:44.478Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rumor",
 "prompt": "Full etymology of rumor: Old French, Latin rumor, PIE root, and any cognates given."
}
```


## [2026-09-14T01:28:45.484Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/roar",
 "prompt": "Full etymology of roar: Old English rarian, Proto-Germanic, imitative/PIE base; also mention rumble if present."
}
```


### [2026-09-14T01:28:49.417Z] TOOL RESULT

```
# Etymology of Rumor

**Noun Origin (late 14c.):**
The word derives from Old French *rumor* meaning "commotion, widespread noise or report," which comes from Latin *rumorem* ("noise, clamor; common talk, hearsay"). The Latin term connects to *ravus* (hoarse), tracing back to the Proto-Indo-European root *\*reu-* meaning "to bellow."

**Primary Definition:**
"Unsubstantiated report, gossip, hearsay" or alternatively "tidings, news, a current report with or without foundation."

**Verb Form (1590s):**
The verb emerged in the 1590s with the transitive sense of "spread a rumor; tell by way of report," derived from the noun.

**Related Terms:**
- *Rumorous* (1540s): making a loud, confused sound
- *Rumor-monger* (1884): one who spreads rumors
- *Rumor mill* (1887): figurative expression for rumor production

**Cognates:**
Dutch *rumoer* and German *Rumor* both derive from the French version.
```


### [2026-09-14T01:28:51.640Z] TOOL RESULT

```
# Etymology of "Roar"

The word "roar" traces back through multiple linguistic layers. The verb originates from Middle English *roren*, derived from Old English *rarian*, meaning "to roar, wail, lament, bellow, cry."

## Origins and Linguistic Connections

The term is "probably of imitative origin," with cognates appearing across Indo-European languages:
- Middle Dutch *reeren* and German *röhren* ("to roar")
- Sanskrit *ragati* ("barks")
- Lithuanian *rieju, rieti* ("to scold")
- Old Church Slavonic *revo* ("I roar")
- Latin *raucus* ("hoarse")

These parallels suggest a Proto-Germanic root that developed from an imitative base—essentially, the word itself mimics the sound it describes.

## Semantic Evolution

The noun form emerged in the late 14c., initially referring to "the loud, continued cry of a large beast." By around 1400, the meaning expanded to encompass "other full, loud, continued, confused sounds," including thunder and cannon fire by the 1540s. Modern uses emerged later: laughing loudly (1815) and operating noisy motor vehicles (1923).

The word's journey from onomatopoeia to multipurpose descriptor reflects how imitative language often becomes more abstract and generalized over centuries.
```


## [2026-09-14T01:29:03.144Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"raoi\" CHEUNG.txt | head; echo \"=== *(H)raud tear ===\"; sed -n '13107,13140p' CHEUNG.txt"
}
```


### [2026-09-14T01:29:03.214Z] TOOL RESULT

```
18126:Pass.: aor. INJ. 3sg. OAv. mraoi(Y 32.14) 
28242:Pres. ja-: IND. 3sg. Y Av. fraorisiieiti (Yt 10.9), ? Y Av. fraorisaiti (H 1.17), Y Av. fraoirisaite (V 9.40), 
28243:3pl. uruuisanti (Yt 12.25), Y Av. fraoirisinti (Yt 13.46), INJ. 3du. Y Av. uruuisiiatom (Yt 19.82), SUBJ. 
28244:lsg. YAv. ni.uruuisiiäni (Yt 17.57 Ё), 3sg. YAv. avoirisiiat (Yt 5.62), OPT. 35р. ҮАУ. fraoirisiiöit (V 
28245:14.16), IMPV. 2sg. Y Av. ni.uruuise (Yt 17.60); Partic.: pres. med. Y Av. fraoirsimna- (Vr 12.5); Caus.: 
=== *(H)raud tear ===
*(H)raud ‘to tear, break’ 

*NEIR: (+ *us-) Yzgh. sori0-/sorust ‘to break, tear [intr.]’, sarand- (caus.) ‘to break, 
tear [tr.]’ || (+ *pati- ?) Yzgh. pərci0-/pərcust ‘to be torn’, porcand-/porcust (caus.) 
‘to tear [tr.]’ (with meatathesis: -cr- > -rc- ?) || (+ *para-, *pari-) Sh. (Baj.) piri0-/ 
pirüst, Rosh. рагё0-, pared-/paröst, Bart. paré0-/partist, Orosh. pira0-/pirist, Sariq. 
pirad-/pirüst ‘to burst, tear [intr.]’, Sh. pirénd-/pirént, Rosh. parend-/parent, Bart. 
parend-/parend, parent, Sariq. parin-/parind (caus.) ‘to tear, burst [tr.]'. O Not from 
*rad- (i.e. *(H)ra(n)d), pace Morgenstierne, EVS\: l.c. Most, if not all, intransitive 
Pamir forms, especially with a front vowel, may derive from the pres. (or pass. ?) 
formation *(H)r(a)ud-ia- (^ *(H)r(a)u0-1á- ?). 


*Hraud 193 


© The evidence for an Ir. root *(H)raud, which would derive from IE *(H)reud-, is 
limited to modern Pamir forms. 

«PIE *(H)reud- ‘to tear, break up’. 9 The reconstruction of an initial laryngeal is 
based on the premise that IE roots cannot begin with an initial *r-. = LIV: — | Pok.: 
869 

*IE COGNATES: Lat. rudus ‘(broken) rocks, gravel’, Olrish road ‘ruins’, Welsh (pl.) 
rhuddion ‘rubbish’, ON reyta ‘to tear, pluck off’ (Germanic *rautjan), MHG rüten 


‘to rob’ 
*REFERENCES: Edel’man 1971: 240; EVS: 75b, 57a, 59a f. 


*Hraud ‘to grow (bigger)’ 

*AVESTAN: YAv. raoö- (ruö-) ‘to grow’ || (+ *fra-) ‘to grow to(wards)’ || (+ *ni-) ‘to
```


## [2026-09-14T01:29:05.525Z] TOOL CALL #52: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/riot\" \"https://www.etymonline.com/word/rubbish\" \"https://www.etymonline.com/word/rag\" \"https://www.etymonline.com/word/rough\" \"https://www.etymonline.com/word/rover\" \"https://www.etymonline.com/word/rumor\" \"https://www.etymonline.com/word/roar\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 423, roots Reu 1 / Reu 2, checking English descendants (riot, rumor, roar, rough, rag, rover, rubbish)\"; done 2>&1 | tail -20"
}
```


### [2026-09-14T01:29:08.503Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8943c6c271c2d839.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5554347cbfa0d903.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/296a6006ccf84e6c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/187eea63288f0cb4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/124f8da0f79e7f00.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/91930d88eac5b0c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b0d925d7e8eb8f4b.txt
```


## [2026-09-14T01:29:18.811Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"RIOT\" \"RUMOUR\" \"ROAR\" \"RUMBLE\" \"RID\" \"RIP\" \"ROB\" \"ROBE\" \"ROVER\" \"RUBBISH\" \"RUBBLE\" \"ROUGH\" \"RUG\" \"RAG\" \"RUPTURE\"; do echo \"=== $w ===\"; grep -n \"^$w\\b\\|^$w,\" SKT.txt | head -2; done"
}
```


## [2026-09-14T01:29:19.991Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^reu-\\|^reudh\\|^reup\\|^reud\\|^rumpo\\|^rudis\\|^rumor\\|^rugio\" IEC.txt | head -20"
}
```


### [2026-09-14T01:29:20.005Z] TOOL RESULT

```
=== RIOT ===
=== RUMOUR ===
=== ROAR ===
=== RUMBLE ===
=== RID ===
=== RIP ===
=== ROB ===
=== ROBE ===
=== ROVER ===
=== RUBBISH ===
=== RUBBLE ===
=== ROUGH ===
=== RUG ===
=== RAG ===
=== RUPTURE ===
16295:RUPTURE.
```


### [2026-09-14T01:29:20.061Z] TOOL RESULT

```
14549:reudó (roud-, rud-), ið “bellow, bawl, belch, wail'. Cf. roud-. WP II, 351 Skt. rodami, rode, rodimi, 3 pl: rudanti, v. *weep'; cf. rudàmi, rude and rudye, mp. id.; Arm. orotam, v. ‘thunder’ beside orocam, v. ‘chew the cud" cf. also orot, Let, ‘thunder’; oroč, i-st. ‘rumination��; Lat. (z-gde) rudo, ére, v. ‘roar, bray’; Ir. cf. ruadh, adj. ‘violent’; OHG riozzan, sv. 2. ‘wail’; MHG riezen (2), id.; OE reotan, sv. 2. id.; (o-gde in) ON rauta, v. ‘roar’; OCz. ruzu, ruditi, v. ‘enrage’; OLi. ráudmi, Li. raudóju, ott, v. *wail; Latv. rau- daju, id.
14550:reudos (roud-, rud-) (rough, raw, violent. WP II, 351 Skt. cf. raudrah, adj. ‘violent’; Ir. ruadh, adj. (2) “violent, strong, valiant; MHG riez, sm. ‘brawl, bawling, attack’; ge-riuze, s. n. ‘bluster, brawPľ; (o-gde in) Li. raudùs, adj. "olangent: (z-gde in Lat. rudis, adj. ‘rough, wild? which is ambiguous, cf. ghrudos, is (1). (Isophonic: MHG alt-riuze, -riuze, wm. ‘cobbler’). Cf. also Av. raoióito ‘big’
14551:reudhó ‘make red; redden’. Cf. roudhos, rudh- Gk. ereütho, v. tr. id.; OE reodan, sv. 2. tr. id.; ON rjóða, sv. tr. id.
14553:reudhos “red; redness'. Form of roudhos,
14574:reupó (rup-) 'téar, break, burst, plunder. Cf. rüp-, leup-. (Skt. ambig.) WP II, 354 Skt. (ambig.) rupyàmi, v. (“ violate; be racked'. Cf. leup-, lup-); Av. rup- v. “attack, rob” (am- big. as Skt.); Lat. cf. (rumpo, ére), pf: rupi, sup: ruptum, v. ‘burst, têar, violate, beat, tire’; MHG riefen, wv. ‘quarrel; OE reofan, sv. 2. 'téar, break’; ON rjúfa, v. “break in’;
```


## [2026-09-14T01:29:30.832Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC reu bellow ===\"; grep -n \"reuō\\|reuo \\|^reu\\|rāuos\\|raudos\\|roud\" IEC.txt | head -20; echo \"=== IEC rumos/rumor ===\"; grep -n \"rumor\" IEC.txt | head -5"
}
```


### [2026-09-14T01:29:30.901Z] TOOL RESULT

```
=== IEC reu bellow ===
19:7. 1986. 933-1092 (potrajo-roudhros)
240:agros “front, forepart; front, forward, early, primary'. WP I, 38 Skt. ágram; Av. ayro; Gk. cf. agér-ókhos *proud, arrogant" (?)
352:aksulos, aksəlos (oks-?) ‘bold, proud’. Cf. aksios (2). Arm. ağoy ‘able’; MIr. ocol, occol (for *acol, *accol? ‘bold, vehement": OCS oxolü, Srb. ohol ‘prouď’; cf. OCz. ochle ‘honour, worship’ or sim.)
1445:bhngh- ‘big; mass, lump’. Cf. bhaĝhus, panguos Hitt. (?) (ambig.) pankus ‘al’; MHG bunge *jJump'; Icel. bunga, id. and ‘bulge’; Li. bin- gùs ‘bold, proud”; bingstu ‘take root
1611:bhrat- ‘rag, tatter, rug” Lat. cf. fratilli ‘fringe, shag, nap’; Olr. brat ‘rug, cloak’, Ir. ‘cloak, shroud’, dim. bratóg ‘stag’; W brat, id. (LW in OE bratt)
1641:bhreud-, bhroud-, bhrüd- ‘crumble, break? (Gk. cpd. of hodós? phroüdos ‘decrepit, de- cayed'); OE breotan; ON brjóta; SW bryta ‘break’, beside (*-u-) OE ge-brot, Sw. brott, s.; Ir. brüádaim ‘crumple’ (*-ü-)
1683:bhroud- (?) (Gk. phroüdos ‘transient, vain” is usu. refd. to pro  hodós); ON braut, f. i-st. road: adv. "away beside breyta "change: NNorw. braute ‘boast; rampage’; RNorw. brøyte “break; turn; dear": Cor. brows 'crumbs', cf. Br. brüzün ‘crumb’; Pol. Ukr. Slovak. Cz. brud “dirt?
1701:bhrud- 'excrescent, bulging; excrescence, bulge’. WP II, 195. Cf. bhrdh- MHG bros “bud, sprout’; G (fr. LG) brutt ‘rugged; haughty’; LW in It. brutto, Fr. brut; cf. also G brütsch ‘proud’; OCS brüdo, Cz. brdo, and Srb. brdo ‘hillock’ are ambig. cf. bhrdh- (2) and bhrusdh-
1785:bhr$6, io ‘crumble’. Variant of brgh-, q.v. Alb. brydh ‘crumble; loosen (soil); OW breu, W brau ‘brittle, fragile’; breuo (‘grow brittle’, fr. *bhrghài-, denom.); OHG brocchon, MHG brocken, brücken ‘crumble’; Du. cf. brok “fragment”; Latv. birstu, birzti ‘crumble’
1904:bhukulos (-ilos, -əlos, à) ‘swollen; swell, bulge’ l Gael. bochail ‘proud’; OHG buhil Ch: G -bühl); Blg. bükül & bükla “wooden water- bottle’; Li. (?) buklüs “clever”
1980:bhürn- (3) “wild, dashing; dash, passion. Cf. bhüro, ið Skt. bhürnih, adj. id.; Arm. burn “violent, violence’; MIr. cf. búr ‘angry’ beside (*-u-) borr “proud; pride’; borrán ‘anger: Alb. cf. mburrem ‘swagger, boast
2276:diKnos ‘proud, noble, noted’. Cf. deiK-, diK- Oss. cf. äv-dīsän ‘witness’; Lat. dignus; ON tign ‘honour’; tiginn *well-born'
2476:droudhos, ā ‘forced, constrained; straint’. Cf. drudh- & WP I, 800 ON trauór ‘reluctant’; trauð ‘difficulty’; cf. trauóa (v. "Tat Latv. draudi, pl. ‘threats’; draudēt ‘to threaten’; Li. cf. draudimas "ban: warning; insurance’; draudZiü, draüsti “ban; warn; insure'
2478:droustos “held, tight, firm, constrained’. Cf. droudh-, drudh- ON traustr ‘trusty’; traust “help, protection’; Li. uZ-draustas, adj. “forbidden?”
2487:drudhó, ið “crush, squeeze’. Cf. droudh- and WP I, 800. Cf. dhrgh-, drut- Alb. (ambig.) drudh ‘crush’; drudhe, drudhé ‘crumb’; drudhem, mp. “hurtle? (see dhrgh-); (MIr. druidim 'shut, push, drive, force'; druit *compression' suggest a variant: *drut-, q. v.); Go. trudan ‘tread’; SWGer. trotten “press grapes; ON troða ‘tread, press, stuff; Cz. cf. drdy “fits, fears?
2505:drus-, drusos (2) “firm, solid”. Cf. dru-, drsus, druos, drutos, etc. Gaul. drusus “firm, boid’; LW in Fr. dru; (LG tros ‘proud, defiant reflects, like Du. trots, an obscure G Trotz, MHG trutz, trotz, s. but the radical *dru- is common to all forms); Li. cf. sü-drus 'solid'
3085:“twist, turn, spin (tr.); Ir. cf. (?) dreas (“bout, turn”, if for *dhre&hso-) (dhrën-, see dhrān-. Vocalism ambiguous in Gk. & Gmc.) Gk. cf. ten-thréne (‘bee or *wasp"); an-thrén& ‘wild bee’; thrénos ‘dirge; OS dràn, Let ‘drone’; OE dræn beside dran, id. (*-oi-?) dhreng- (dhrong-) "wer Go. drigkan, OHG trinkan, etc. («drink', and com. Gmc.); Li. drengiü, ti ‘sleet, pour w. rain’; o-gde in Sw. drank ‘mash; barm’ as well as in G Ge-trank, E to drench, etc: R (Ð cf. driàzgi ‘dirt; twaddle’ (but Pol. drzazga “chip, splinter, log? may be of Wh. R. origin) dhrengh- “slow, sullen, sad, limp, hanging”. Cf. WP I, 813 Per. dirang ‘slow’; Tokh. A trànk-, B treñk- ‘hang’; W dreng, adj. ‘surly’; R cf. drjàgat, drjagnüt ‘dangle’; Li. drengiü, ti (1) “wear out dhrésó, ið (?) “shout, rave’ Gk. thréo ‘shriek’; ON dræsa, f. ‘twaddle’; Latv. cf. (o-gde) draséju ‘yodel, jubilate? dhreudo, io, dhroud-, dhrud- “bully, illtreat, threaten’. Cf. WP I, 870 NG triezen ‘twist, tug, bully); MHG (z-gde) trutzen ‘defy’; Li. (o-gde) draudžiù, draüsti ‘warn, ban’; Latv. draudu, ét ‘threaten’ dhreugh- (1), dhrugh- ‘harm, deceive’. Cf. WP I, 860 & 874 Skt. drohah ‘harm, wrong’; drühyami ‘hurt, offend’; Av. druž- ‘deceive’ beside druxš-, o-gde in draoxš-, id.; LW in Arm. držem, id.; MHG (regen, id. beside (z-gde) troc, gs troges ‘deceit; OS driogan; Du. be-driegen *cheat'; Av. cf. draoyo; Per. durüy ‘falsehood’ dhreugh- (2), dhrough- “good, fit, sprightly, pleasant'. See dhrough- Lat. cf. ? fruor (ambig. ‘enjoy’, if distinct from früx, -gis, frügalis, etc. See bhrüg-); Br. dréó ‘gay, tipsy’; OE dreog ‘fit, sober, serious, gentle beside dréogan ‘behave, experience’; ON drjúgr ‘substantial, lasting’; Li. (o-gde) draugùs ‘sociable’ dhreus- ‘crumble, fall; crumb, fragment(sy Arm. cf. eyğiwr (2) ‘husks’; OE drēosan, v. ‘fall, perish’; drēor, m. ‘blood’; Ukr. cf. dru-
3116:dhroud- “bully, threaten'. See dhreud- Li. draudZiü, “sti “warn, ban’; Latv. draudu, et ‘threaten’; draudi, pl. ‘threats’; (e-gde in) Ger triezen ‘bully; tug, twist’; z-gde in G Trotz *defiance'. Cf. WP I, 870
3133:dhrud-, see dhreud-, dhroud-
3731:esulos (1) ‘noble’. Cf. esros, esus, etc. Skt. ásurab; Av. ahuro; Hitt. assul, assulas “favour, greeting’; Dor. cf. eslós ‘noble, kind” beside Gk. esthlós, id. (cons. obscure); Lat. erulus “lord; Olr. éola “expert, wise’; Br. héal, hael ‘noble, generous’; OHG, OS er ‘man’; OE eorl “chief, noble, earl; ON jarl, id. jarl- (cpds. *noble-"). Cf. Srb. ohol ‘proud’?
=== IEC rumos/rumor ===
```


## [2026-09-14T01:29:32.434Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in roar rumble riot rumour rid rip rob robe rubbish rubble rough rug rag rupture; do echo \"=== $w ===\"; grep -n -i \"^$w, \" SKT.txt | head -2; done"
}
```


### [2026-09-14T01:29:33.578Z] TOOL RESULT

```
=== roar ===
=== rumble ===
=== riot ===
=== rumour ===
=== rid ===
=== rip ===
=== rob ===
16167:Rob,  Robe  ;  see  Beavo.
=== robe ===
=== rubbish ===
15720:rubbish,  broken  stones,  waste  matter, refuse.  (!■'.  —  O.  H.  G.)  M.  E.  robcws, roivux,  rrompl.  Parv. ;  pi.  of  an  old  form roini*,  clearly  itpresenicd  by  mod.  E. niU'U ;  s<'e  below.  ^  Kubdiih  is,  in  fact, a  corrupt  form  of  the  old  plural  of  ru&bk,
16257:Rubbish,  Rubble ;  sec  Reave.
=== rubble ===
15721:rubble,  broken  stones,  rubbish.  (F.** O.  II.  G.)  •  KnhlU,  or  ntbhuk  of  old houses;'  Barel  (1580).  This  answers exactly  to  an  old  form  robel*,  O.  F.  robil*^ only  found  in  the  pi.  rodntx.  'A  grcte !o<Kie  of  rohcux ; '  cited  by  Way  in  Prompt. Pnrv.  Obviously  the  dimin.  of  F.  n>6i  m saa€  of  '  tnuh/  so  well  preferred  in
=== rough ===
=== rug ===
16283:Rug,  Rugged :  see
=== rag ===
=== rupture ===
```


## [2026-09-14T01:29:44.093Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in roar rumble riot rumour rid rip rob robe rough rug rag; do echo \"=== $w ===\"; grep -n \"^[[:space:]]*$w,\\|^$w,\" SKT.txt | head -2 | cut -c1-600; done; echo \"=== 16280-16290 ===\"; sed -n '16280,16290p' SKT.txt"
}
```


### [2026-09-14T01:29:45.246Z] TOOL RESULT

```
=== roar ===
=== rumble ===
=== riot ===
=== rumour ===
=== rid ===
=== rip ===
=== rob ===
=== robe ===
=== rough ===
=== rug ===
=== rag ===
=== 16280-16290 ===
RufSo;  see  Baff(iV
Ruffle    (iK    to    blaster,   be (O.  Du.)     Obsolete.     MugUry ing  bullies,  highwaymen.  U«rle» men  (Narcs).  -  O.  Do.  njgtUn, pandftT :  Low  G.  rttffeiH,  to ft  pimp,  intriguant :  t>an   ru^tr^  % A  rat^Z^and  ft  ruffian  arc  much  the
ruffian,  a  bully.  (F.  -  T« rufitn,  ru^n,  '  ft  bawd, O.  Dd  raff  en.  to  panilar  (1
Rug,  Rugged :  see
Rugose.  tuU  of  wrinkles.    fL)    L goms^  «/ij,,  from   rmsjot,  ft  wriaUe. cormgat4,    L.    pp.    mt-rH^tim
Rliln.  (F.  -  L.>    F.  mrne,  - overthrow.  —  L.  merg.  lo  nuh^ Rule ;  sec  Regent.
Rum  ( I ),  ft  splrituoos  liquor. Called  mm^o  m  Smollet.  Per.  I'n and  c  ix ;    this  is  short  for  tl word    ntttthcfwiin^,    fi^og*       Or f^umhuUUn    in    Bftrha<  Iocs,    A.  D. from  DevoQsh.    rumhunfcn.  uproar, pnf.       Founded     OQ     V.    rmm^tr. Ramp.
Rum  (3).  strange,  queer.  (Hindi.)  \ gallant,  ft  canl  wo^ ; '  Hftiley  (17,^5). really  means  '  Gypsy : '  bcnoe ft  Gypsy  pcMnt  of  view,   but from  an  outsider's  point  of  vi       _ rome  houu,  rum  btme,  good  wise, means  'a  hosband,  a  Gypsy:*    ri» adj.,  Gypsy.    ThisGypsy  word  f»iii to  Hindi  dopt  (with  initial  cerebral  4^4 fiised  with  r),  ft  man  of  low  Cftste, domba,  *  a  man  of  low  caste,  who his  livelihood  by  singing Bcnfcy.  j
Rumb.  Rhumb,  a  line  for  diiaed a  ship's  course  on  a  chftrt ;  a  petal  of  J compass.  (F.  —  Span.  -•  L.  *  Ck.1  J Jiumb  in  Phillips,  —  F.  mtni,  <  ft  rombil point  of  the  compossc.  a  line  drawn  Aittt^ from  wind  to  wind  in  ft  compafise,  trai boord,  or  sea-cftrd ; '  Cot.  «>  Spaa.  (^ Port.)  rumho,  a  ship's  course  (1 by  spiral  lines  00  a  globe).  ~  L. ace.  of  rAombus^  a  magicton't rhombus.  —  Gk.  /<{/43of.  a  top. wheel,  whirling  motion;  also  a See  Rhomb.  HAomh  mcuit  revi the  sphere,  Milton,  P.  L.  viiL  lu whiiling  or  spiral  lines,  Ac.  <f  No  fl oeclion  with  Uu.  ruim^  which  CDOily  a<
RtJMBLE.
Loc,  or  sometimei  the  hotd  of .   ie.    iU    room    or    capacity    for
```


## [2026-09-14T01:30:49.777Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '54061,54066p;54132,54142p;54256,54262p;54279,54285p' LAT.txt | cut -c1-400"
}
```


### [2026-09-14T01:30:49.850Z] TOOL RESULT

```
rudis, -e: grossier, brut. Au sens moral "non degrossi (oppose
a politus , cf. Pl. Foe. 189), inexperimente, inculte, ignorant, novice".
Souvent joint a un genitif: rudis rei militaris (cf. peritus). Anci en,
usuel et classique. M.L.74SO et aussi *rudius, id.7431.
Derivas: ruditas (a peine attest^j un ex. dans Apul.); rudimentum
(non atteste avant 1'^poque imperiale; a appartenu d'abord A la
rugio, -is, -Ire: rugir. DErivE: rugitus, -us m.: rugissement.
AttestE surtout a basse Epoque. La quantitE de 1 'u est mal attestEe
en latin; 1 'auteur du Carmen Philomelae le fait bref, mais Quicherat
dans son Thesaurus note: de quantitate primae syllabae nihil affirmare
au sim', cf. Niedermann, MEl. de Saussure, p.46, et les formes romanes
supposent rugire, rugitus, M.L. 7438,74:39. L’hypothese d’une influence
analogique de mugire (Kunst, Glotta 1935, ioy-113) est inutile.
Panrom an.
Cf. rumor, runco (et rugdt).
Mots semblables - mais non pas nEcessairement apparentEs - dans
m. iri. rucht "cri, hurlement", gr. epuyovt 01 "mugissant" (et copuyTIj
rumor, -oris m.: bruit, rumeur publique. S'emploie au singulier
comme an pluriel. Ancien (Pl.), class., usuel. Panroman, sauf roumain.
M.L.7441. - Mot isole; les rares derives ou composes sont archaiques
et de creation artificielle et n'ont pas survecu. L’abrege de Festus,
P.F.9,7 a conserve adrumauit, rumorem fecit... quod uerbum quidam
a rumine, i.e. parte gutturis putant deduci. Le compose suppose un
simple * rumo (fait sur rumor, d'apres clamo, clamor) dont le fre¬
rumpo, -ls, rupi (sur un futur archafque rupsit, v.Fest. cite
s.u. talio, et derumpo), ruptum, rumpere: briser avec force, rompre
(souvent avec une idee accessoire d'arrachement, d'^clatement: r.
inflatas uesiculas , Cic.Diu.3,14»33J r. pectora fremitu Lucr.3,397,
d'ou se rumpere ou rumpi). Vaite de tout temps. Le simple n*est at¬
teste qu 1 au sens transitif; mais il a du s ( employer au sens absolu,
comme les composes erumpS "3'elancer hors (en brisant les obstacles),
```


## [2026-09-14T01:30:50.746Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"reave,\" SKT.txt | head -3; echo ---; grep -n \"rarian\\|rärian\" POK_full.txt POK_03.txt | head"
}
```


### [2026-09-14T01:30:50.845Z] TOOL RESULT

```
15714:rereward;  see  rearward  (above). Bear    (3),    insuRicicntly    cooked.    (E.) M.  K  rtre.     A.  S.  hrfr,  half-cooVcd. BearmouBe ;  see  Beremouso. Bearword ;  see  Bear  (2). Boaaon ;  see  Bate  ( t ). Beave.    to    rob.    (E.)      M.   E.    rmtn \  ••  revtft) ;  pt.  t.  raftt,  rtfie,  pp.  raft,  rt/t. A.  S.  re4/tan^  to  despoil,  lit.  to  strip.— A.  S.  re,}/,  clothing,  a  robe,  spoil,  plunder. —  A.  S.  red/,  pi.  t.  of  strong  verb  nd/an,  to deprive. +  feel,  ran/a,   to    reave,    from   sb. mu/  spoil,  wbich  from  rau/  pt.  t.  of  rjii/a, to   brtak  up,  violate;   G.  rautrcn^  to  rob, from  mu6.  plunder.     (^RUP.)
---
POK_full.txt:70076:rdmr\o\ce, sound, pronunciation'; compare further Old English rarian'b\oken, roar,
```


## [2026-09-14T01:30:57.970Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '70060,70085p' POK_full.txt"
}
```


### [2026-09-14T01:30:58.047Z] TOOL RESULT

```
Root / lemma: rei-3, re(i)- 

Meaning: to cry, bellow, etc.. onomatopoeic words 

Note: s. also reu-, reu-, ru- 

Material: Old Indie rayati^ barks '; Lithuanian /■/ey^/7e//"losschreien, scold, chide', refl. 

"sich quarrel, squabble'; Latvian reju, reju, /7e/"bark, bay'; ablaut raju, /"a/ "scold, chide', 

Lithuanian rojdju, /ryo//"unordentlich crow, cackle' (of rooster, cock)?. Church Slavic rarb " 

clangor' (Czech rarohm. "WiJrgfalke'), russ. rajatb' clink, sound'; Old Icelandic ramr 

"hoarse' {*rema-)\ derived from a noun *rama\s remja^roar, bellow'; possible here also 

rdmr\o\ce, sound, pronunciation'; compare further Old English rarian'b\oken, roar, 

bellow'. Old High German reren ds. etc.; 

Old Icelandic ya/777a "bleat', wherefore Armenian orna/'\r\eu\e' belongs, weis perhaps auf 
eine full root era-, re- there. 

extensions: 

/•eZ7-"rulpsen':
```


## [2026-09-14T01:31:08.890Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s)\" POK_full.txt | awk -F: '$1>70060' | head -3; echo \"--- rugire in AHD ---\"; grep -n \"rugire\\|riigire\\|rümor\\|rumor\" AHD_watkins1985.txt | sed 's/\\(.\\{400\\}\\).*/\\1.../' | head -5"
}
```


### [2026-09-14T01:31:09.839Z] TOOL RESULT

```
70109:Page(s): 859-860 
70136:Page(s): 860 
70144:Page(s): 860 
--- rugire in AHD ---
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English...
```


## [2026-09-14T01:31:14.114Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=rumor",
 "prompt": "What Indo-European root does the AHD give for 'rumor'? Quote the etymology line and the root name."
}
```


### [2026-09-14T01:31:16.996Z] TOOL RESULT

```
Based on the content provided, the etymology line for "rumor" states:

"\[Middle English _rumour_, from Old French, from Latin _rūmor_.\]"

However, the page does not specify a reconstructed Indo-European root name for "rumor." While the site mentions that thousands of dictionary entries include etymologies tracing back to proto-languages with appendices on Indo-European roots available, the specific entry shown for "rumor" only traces it back to Latin, not to a named Indo-European root.
```


## [2026-09-14T01:33:41.263Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://ahdictionary.com/word/search.html?q=rumor\" --note \"pdf page 423, root Reu 1, AHD entry for rumor (etymology stops at Latin rumor, no IE root named)\" 2>&1 | tail -3; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg423.png data/verification/sources/refs/ocr/BOOK/423.png && echo copied"
}
```


### [2026-09-14T01:33:42.731Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1f70f461655f7bda.txt
copied
```


## [2026-09-14T01:41:37.215Z] TOOL CALL #64: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-423.json",
 "content": "{\n  \"pdf_page\": 423,\n  \"book_page\": 393,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Reu 1, Rěu 3, Rů 1, Reud 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *reu- / *rēu- / *rū- 'to bellow, roar, utter hoarse cries; to murmur, growl' (Pokorny 867–868, '1. reu-'), with the extensions *reud- 'to weep, wail', *reug-, *reuk-, *reus-\",\n      \"note\": \"Pokorny IEW prints the headword '1. reu-, rēu-, rū- Schallwurzel \\\"brüllen, heisere Laute ausstoßen\\\"; \\\"brummen, murren\\\"; roudo- \\\"Klage\\\"' at the top of p.867, the extensions a. reud- / b. reug- / c. reuk- / d. reus- following on pp.867–868 (References: WP. II 349 ff.). Nourai's four headwords map onto Pokorny one-for-one: Reu 1 = 1. reu-, Rěu 3 = the long-vowel variant rēu-, Rů 1 = the zero/lengthened grade rū-, Reud 1 = extension a. reud-. Language label (Indo-European) and gloss ('to cry, roar') are both right. The one caveat is inherent in the material and Pokorny states it himself: this is a Schallwurzel, an onomatopoeic base, so its 'reflexes' in the daughter languages are often re-created imitations rather than strict phonological descendants — which is why Pokorny keeps the neighbouring imitative base rei-3, rē(i)- 'schreien, brüllen' (pp.859–860, where OE rārian > roar in fact stands) separate, with only a cross-reference 's. auch reu-, rēu-, rū-'.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *reu- / *rēu- / *rū- «غریدن، بانگ برآوردن، نالیدن» که پوکورنی در صفحهٔ ۸۶۷ فرهنگ خود با سرواژهٔ «1. reu-, rēu-, rū-» و توضیح «ریشهٔ آوایی (Schallwurzel): غریدن، آوازِ خشن برآوردن» ثبت کرده و گسترش‌های آن (reud- «گریستن»، reug-، reuk-، reus-) را در همان دو صفحه آورده است. هر چهار سرواژهٔ نورایی با پوکورنی می‌خواند: Reu 1 همان ریشهٔ اصلی، Rěu 3 گونهٔ مصوت‌بلند، Rů 1 پایهٔ صفر، و Reud 1 همان گسترشِ reud-. برچسب زبانی و معنا هر دو درست است. تنها نکتهٔ احتیاطی این است که چون ریشه‌ای آواگون (نام‌آوا) است، بازتاب‌های آن در زبان‌های دختر بارها از نو ساخته شده‌اند؛ از همین رو پوکورنی ریشهٔ آواگونِ همسایه rei-3, rē(i)- (ص ۸۵۹–۸۶۰) را — که rārian انگلیسی باستان و در نتیجهٔ roar زیر آن جای دارد — جدا نگاه داشته است. ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/rumor\",\n        \"https://www.etymonline.com/word/roar\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:867\",\n          \"status\": \"supports\",\n          \"note\": \"Exact. POK_03.txt, form-feed leaf 102/103 (printed page number '867' is set inline in the scan just before the entry): '1. reu-, rēu-, rū- Schallwurzel „brüllen, heisere Laute ausstoßen“ (auch vom Laute beim Erbrechen …); reu-men: „brummen, dumpf murmeln, murren“ … Ai. rau-ti, ruváti, rávati „heult, brüllt, lärmt, dröhnt“ … lat. rūmor „Geräusch, Ruf, Gerücht“; rāvus „heiser“ … WP. II 349 ff. … Page(s): 867-868'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"IEW p.867–868, '1. reu-, rēu-, rū-' (POK_03.txt leaf 102–104; POK_full.txt line 70592, 'Page(s): 867-868')\",\n          \"stance\": \"supports\",\n          \"note\": \"'Schallwurzel „brüllen, heisere Laute ausstoßen“'; extensions a. reud-, b. reug-, c. reuk-, d. reus-.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny Bd. II p.349 ff. (WLD_Bd2_pages.txt line 23125)\",\n          \"stance\": \"supports\",\n          \"note\": \"'1. reu-, rēu-, ru- Schallwurzel „brullen, heisere Laute ausstoBen“ (auch vom Laute beim Erbrechen, s. reug „sich erbrechen“); reu-men: „brummen, dumpf murmeln, murren“ (daraus auch „zornig, wild“ u. dgl.).' — Pokorny's p.867 entry is a reprint of this.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck, Dict. of Selected Synonyms, §1.36 (SYN.txt line 1430)\",\n          \"stance\": \"supports\",\n          \"note\": \"'… (fr. *reuk-, beside *reug- in Lat. rugire \\\"roar\\\", both extensions of *reu- in Skt. ru- \\\"roar\\\", etc. (Walde-P. 2.349 ff.)' — Buck uses the same root with the same gloss.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, IE Comparative Dictionary, s.v. reudō (IEC.txt line 14549)\",\n          \"stance\": \"supports\",\n          \"note\": \"'reudō (roud-, rud-), iō \\\"bellow, bawl, belch, wail\\\". … WP II, 351. Skt. rodami … Lat. (z-gde) rudo, ēre, v. \\\"roar, bray\\\"; OHG riozzan … OE reotan … ON rauta, v. \\\"roar\\\"; OLi. ráudmi, Li. raudóju' — Mann's headword covers Nourai's 'Reud 1'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, between 'rei-1' and 'reu-2' (AHD_watkins1985.txt lines 894–896)\",\n          \"stance\": \"silent\",\n          \"note\": \"The local OCR of Watkins 1985 has lost the body of the 'reu-1' entry — only the running heads \\\"reu-'\\\" and \\\"reu-?\\\" survive between the rei-1 and reu-2 entries — so the AHD wording for this root could not be quoted from the copy on disk.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"raod 2\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan raoδ-/raod- 'to wail, lament, weep' is the standard reflex of Pokorny's extension a. reud- of *reu-. Bartholomae (AiWb col. 1489 f.) lists it as 'g. ¹raod-, j. ¹raoδ- V. „jammern“', present stem uruδa- (zero grade *rud- with the regular Avestan anaptyctic u- before the cluster), causative urūδaya-, s-aorist raos-; in the Gāthās it is used only of cattle (Y 29.9 aēca gə̄uš urvā raostā 'and the soul of the ox raised a lament'), in the Younger Avesta only of daēvic beings (V 19.45 uruδənta daēva). The exact cognates are Skt. rudáti/róditi 'weeps, wails', Lat. rudō, -ere 'to bray, roar', OHG riozan, OE rēotan 'to weep', ON rauta 'to roar', Lith. raudà 'lament', OCS rydati — i.e. PIE *(H)reud-, which Cheung reconstructs as *(H)raudH with a laryngeal simply because IE roots do not begin in *r-. The -d-/-θ- alternation inside the Avestan paradigm is a later Iranian development, not part of the PIE shape. Nourai's index '2' is his own homonym number; Bartholomae counts this one as ¹raod- (against ²raod- 'to grow', ³raod- 'to hold off', ⁴raod- 'to flow').\",\n          \"derivation_fa\": \"فعل اوستایی raoδ-/raod- «نالیدن، مویه کردن، گریستن» بازتاب مستقیم گسترشِ reud- از ریشهٔ هندواروپایی *reu- است. بارتولومه (فرهنگ ایرانی باستان، ستون ۱۴۸۹ به بعد) آن را «¹raod- در گاهانی و ¹raoδ- در اوستایی متأخر، فعل: مویه کردن» آورده، با ستاک حالِ uruδa- (پایهٔ صفرِ *rud- با «او»ی میانجی که در اوستایی پیش از خوشهٔ همخوانی می‌آید)، سببیِ urūδaya- و ماضی سادهٔ s-دار raos-؛ در گاهان تنها دربارهٔ گاو به کار رفته است (یسنا ۲۹٫۹: «روانِ گاو مویه سر داد») و در اوستای متأخر تنها دربارهٔ دیوان. هم‌ریشه‌های آن سنسکریت rudáti «می‌گرید»، لاتین rudō، آلمانی علیای باستان riozan، انگلیسی باستان rēotan و لیتوانیایی raudà «شیون» است. چونگ همین ریشه را *(H)raudH بازسازی می‌کند و صریحاً به پوکورنی ص ۸۶۷ ارجاع می‌دهد. شمارهٔ «۲» از آنِ خودِ نورایی است؛ بارتولومه این را ¹raod- می‌شمارد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:867\",\n              \"status\": \"supports\",\n              \"note\": \"POK_03.txt leaf 103 (printed p.867), extension a of 1. reu-: 'a. reud-: ai. rudáti, róditi „heult, weint, jammert“, av. raod- „weinen“, ai. róda- m. „Klageton, Winseln, Weinen“ … lat. rudō, -ere, -īvi „schreien; brüllen“ …' — precisely Nourai's arrow root → Avestan raod- 'to weep'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiWb col. ~1489 f. (BRT.txt line 24897)\",\n              \"stance\": \"supports\",\n              \"note\": \"'• g. ¹raod-, j. ¹raoδ- V. „jammern“. Praes. 3 uruδa-, 30 (Kaus.) urūδaya-; s-Aor. 1 raos-. … „jammern, heulen“, im gAw. nur vom Rind gebraucht, dagegen im jAw. nur von daēvischen Wesen … aēca gə̄uš urvā raostā „und ein Jammern erhob da die Seele des Stiers“ Y. 29.9 … ai. rudat, rodayati.'\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etym. Dict. of the Iranian Verb, pp.193–194, s.v. *(H)raudH (CHEUNG.txt lines 13195–13216)\",\n              \"stance\": \"supports\",\n              \"note\": \"'*(H)raudH \\\"to moan, (be)wail\\\". *AVESTAN: raoδ- \\\"to moan, (be)wail\\\" … *PIE *(H)reudH- \\\"to weep, cry\\\" … LIV: 508 | Pok.: 867. *IE COGNATES: Lat. rudō \\\"to cry, roar\\\", OCz. ruditi \\\"to sadden\\\", Lith. rauda, Latv. raūda \\\"lament\\\", ON rauta \\\"to roar\\\", OE rēotan \\\"to complain, weep\\\".'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II p.351 f. (WLD_Bd2_pages.txt line 23218)\",\n              \"stance\": \"supports\",\n              \"note\": \"'reud-: ai. rudáti, roditi „heult, weint, jammert“, av. raod- „weinen“, ai. roda- m. „Klageton, Winseln, Weinen“ (= ahd. rōz m., vgl. lit. raudà); gr. ῥυζω; lat. rudō, -ere, -īvi „schreien (bes. vom Esel), brüllen“.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"rwš\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gharib's Sogdian Dictionary, entry no. 8593 on p.346 — the very page Nourai cites — reads 'rws-2 (B, S) rōs ©IE *reu(s) — (to) roar', attested in TSP 13.21 and MSP b38, with the derivatives no. 8595 rws'k(h) rōsāk 'roaring' and no. 8596 rws'ny rōsāne 'roaring (present participle)'. The word is thus not only real but is itself referred to *reu- by the Sogdian lexicographer, i.e. Nourai's own source states his arrow. Formally it continues the s-extension of the root (Pokorny's 'd. ein verwandtes reus-', p.868); Sogdian ō from Old Iranian *au is written <w>, hence the graphic shape rws-. One transcription detail: Gharib prints the headword rws- and reads it rōs with plain s; the book's rwš (with háček) is Nourai's own rendering of that s, not Gharib's. It does not affect the derivation. Cheung's verb dictionary, which covers only verbs with an established Iranian etymology, has no *raus 'to roar' — his nearest root, *HrauH (*HrabH?) 'to crackle; growl', lists a different Sogdian verb, rβž-/rβz- 'to bark'.\",\n          \"derivation_fa\": \"فرهنگ سغدی بدرالزمان قریب، مدخل شمارهٔ ۸۵۹۳ در صفحهٔ ۳۴۶ — همان صفحه‌ای که نورایی ارجاع داده — چنین آورده است: «rws-2 (بودایی، سکولار) rōs ©هندواروپایی *reu(s) — غریدن»، با شواهد TSP 13.21 و MSP b38 و مشتق‌های rws'k(h) «غرّنده» (۸۵۹۵) و rws'ny «غرّنده (اسم فاعل)» (۸۵۹۶). پس واژه هم واقعی است و هم خودِ مرجعِ نورایی آن را به *reu- بازمی‌گرداند. از نظر ساخت، این ستاک دنبالهٔ گسترشِ s-دارِ ریشه است (پوکورنی ص ۸۶۸: «reus- خویشاوند»)؛ در سغدی ō برآمده از *au ایرانی باستان با حرف «و» نوشته می‌شود و از این‌رو املای rws-. یک نکتهٔ نگارشی: قریب سرواژه را rws- می‌نویسد و rōs می‌خواند؛ «ش» در rwšِ کتاب خوانشِ خودِ نورایی است و در استدلال اثری ندارد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:346\",\n              \"status\": \"supports\",\n              \"note\": \"Exact page. SOD_pages.txt form-feed leaf 414 carries the printed page number '346' in its header; entry '8593 rws-2 B, S / rōs ©IE *reu(s) / (to)roar / TSP 13.21 apud. S W, IIJ 1976, 60; MSP b38' stands on it, as do 8595 rws'k(h) 'roaring' and 8596 rws'ny 'roaring ? ©pres. part. ⇒rws-2'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"Gharib, Sogdian Dictionary, p.346 nos. 8593, 8595, 8596 (SOD_pages.txt leaf 414)\",\n              \"stance\": \"supports\",\n              \"note\": \"'8593 rws-2 B, S — rōs ©IE *reu(s) — (to)roar'. Gharib herself derives the Sogdian verb from IE *reu(s).\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etym. Dict. of the Iranian Verb, s.v. *HrauH (*HrabH ?) 'to crackle; growl' (CHEUNG.txt line ~13220 ff.)\",\n              \"stance\": \"silent\",\n              \"note\": \"Cheung has no Iranian verbal root *raus 'to roar'; under *HrauH he lists 'SSogd. rβž-, BSogd. rβz- (inch. ?) \\\"to bark\\\"' — a different stem — and YAv. uru- 'to crackle'. So he neither confirms nor contradicts rws-; grep of CHEUNG.txt for 'rws' returns only the Parthian ʾrws- of *urais 'to turn'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p.868, '1. reu-' extension d (POK_03.txt leaf 104)\",\n              \"stance\": \"supports\",\n              \"note\": \"'d. ein verwandtes reus- sucht man in: nhd. rösten … dazu wohl lit. rūzgiu „brause, schnurre, murre“' — the s-extension of the roaring root that Gharib's '*reu(s)' points to.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"rŭgîre; rŭ-mor\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Latin words are in Pokorny's material for 1. reu- on p.867. rugīre 'to roar (of lions)' belongs to extension b. reug-: Pokorny 'lat. rugiō, -īre „brüllen (vom Löwen)“ (nach mūgiō?)', beside Gk. ἐρυγεῖν/ὠρυγή 'bellowing' and MIr. rucht 'roaring' (*rug-tu-). rūmor 'noise, shout, common talk, hearsay' stands in the unextended root's material immediately after Skt. rávati and Gk. ὠρύομαι, in the company of rāvus 'hoarse', ravis 'hoarseness', raucus 'hoarse' and ravīre 'to talk oneself hoarse'; formally it is an -ōs-/-os- abstract *rū-mōs, whence rūmōr- by the Latin rhotacism of intervocalic -s- (completed in the 4th c. BCE), which is exactly what Nourai's hyphen in 'rŭ-mor' marks. Ernout-Meillet keep rūmor lexically isolated within Latin ('Mot isolé') but cross-refer it under rugiō ('Cf. rumor, runco'). The only quibble is the quantity mark: the u of rūmor is long, that of rŭgiō short, whereas the book prints a breve on both.\",\n          \"derivation_fa\": \"هر دو واژهٔ لاتینی در همان مدخلِ پوکورنی (ص ۸۶۷) آمده‌اند. rugīre «غریدن (ویژهٔ شیر)» زیر گسترشِ reug- جای دارد: «lat. rugiō, -īre „brüllen (vom Löwen)“»، در کنار ἐρυγεῖν یونانی و rucht ایرلندی میانه «غرّش». rūmor «هیاهو، آوازه، گفت‌وگوی همگانی» در بخش اصلی ریشه و بی‌درنگ پس از rávati سنسکریت و ὠρύομαι یونانی آمده، همراه با rāvus «گرفته‌صدا»، ravis «گرفتگی صدا» و raucus. از نظر ساخت، rūmor اسم معنایِ *rū-mōs است که با ابدالِ s میان‌واکه‌ای به r (قانون rhotacism لاتینی، سدهٔ چهارم پ.م.) به rūmōr- بدل شده — و خطِ تیره در «rŭ-mor»ِ نورایی دقیقاً همین تجزیه را نشان می‌دهد. ارنو و مِیه rūmor را در درونِ لاتین «واژه‌ای تنها» می‌دانند ولی زیر rugiō به آن ارجاع می‌دهند. تنها خردهٔ کار نشانهٔ کمیت است: «او»ی rūmor بلند و «او»ی rŭgiō کوتاه است، حال آنکه کتاب بر هر دو نشانهٔ کوتاهی گذاشته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/rumor\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai cites AHD without a page. The local OCR of Watkins 1985 has lost the body of the 'reu-1' entry (only the running heads survive, AHD_watkins1985.txt lines 894–896), and the online AHD entry for 'rumor' gives only '[Middle English rumour, from Old French, from Latin rūmor.]' with no root named (fetched 2026-09-13, archived). The 1976 New College appendix Nourai used is not available online.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p.867 (POK_03.txt leaves 102–103)\",\n              \"stance\": \"supports\",\n              \"note\": \"'… lat. rūmor „Geräusch, Ruf, Gerücht“; rāvus „heiser“, ravis f. „Heiserkeit“, raucus „heiser“, raviō -īre „sich heiser reden“' and, under b. reug-, 'lat. rugiō, -īre „brüllen (vom Löwen)“ (nach mūgiō?)'.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet, s.vv. rugio and rumor (LAT.txt lines 54132, 54256)\",\n              \"stance\": \"partial\",\n              \"note\": \"'rugio, -is, -īre: rugir. Dérivé: rugitus … Cf. rumor, runco (et rugīt). Mots semblables — mais non pas nécessairement apparentés — dans m. irl. rucht \\\"cri, hurlement\\\", gr. ἐρυγόντι \\\"mugissant\\\"'; and 'rumor, -oris m.: bruit, rumeur publique … Mot isolé'. Both words and the link between them are there; Ernout-Meillet are more cautious than Pokorny about the outside cognates.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck §1.36 (SYN.txt line 1430)\",\n              \"stance\": \"supports\",\n              \"note\": \"'… *reug- in Lat. rugire \\\"roar\\\" … extensions of *reu- in Skt. ru- \\\"roar\\\", etc. (Walde-P. 2.349 ff.)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"riot; rumor\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"rumor is straightforward and certain: ME rumour (late 14c.) ← Old French rumor/rumour 'commotion, widespread noise or report' ← Latin rūmōrem (acc. of rūmor); the modern -or spelling is a 16th–17th c. latinisation. riot is the weak half. It enters English c.1200 as riote, first in the hunting sense 'the following of a wrong scent by hounds', then early 14c. 'debauchery, wanton living', late 14c. 'civil disorder', from Old French riote 'dispute, quarrel' / rioter 'to make a disturbance'. Klein (p.1346) says flatly 'which is of uncertain origin'; the OED and Etymonline mention Latin rugīre 'to roar' — presumably through an unattested Vulgar Latin *rugitāre — only as a possibility. So the arrow Latin rugīre → English riot is one plausible conjecture, not the received etymology, and the node as a whole cannot rate better than plausible.\",\n          \"derivation_fa\": \"«rumor» روشن و قطعی است: انگلیسی میانه rumour (اواخر سدهٔ چهاردهم) از فرانسوی باستان rumor «هیاهو، آوازهٔ فراگیر» و آن از rūmōrem لاتین (حالت مفعولیِ rūmor)؛ املای امروزی با -or لاتینی‌سازیِ سده‌های شانزدهم و هفدهم است. اما «riot» حلقهٔ سست این گره است: حدود ۱۲۰۰ میلادی به‌صورت riote وارد انگلیسی شد، نخست در معنای شکاریِ «پی گرفتنِ بویِ نادرست از سوی سگان»، سپس «عیاشی» و در اواخر سدهٔ چهاردهم «آشوب همگانی»، از فرانسوی باستان riote «ستیزه، مشاجره». کلاین (ص ۱۳۴۶) صریح می‌نویسد «خاستگاهش نامعلوم است»، و فرهنگ آکسفورد و اتیمانلاین تنها به‌عنوان احتمال به rugīre لاتین (از راهِ *rugitāre در لاتین عامیانه) اشاره می‌کنند. بنابراین پیکانِ «rugīre ← riot» یک حدسِ پذیرفتنی است نه ریشه‌شناسیِ پذیرفته‌شده، و این گره در مجموع «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/riot\",\n            \"https://www.etymonline.com/word/rumor\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no references of its own (refs=None in the chart); it inherits the parent Latin box's bare 'AHD', which could not be checked — see node #3.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 p.1346 s.v. riot (KLN_1966.txt leaf 717, just after the inline page marker '1347' — the entry stands on the p.1346/1347 opening)\",\n              \"stance\": \"partial\",\n              \"note\": \"'riot, n. — ME. riote, riot, fr. OF. riote (F. riotte), fr. rioter, rihoter, \\\"to make a disturbance\\\", which is of uncertain origin.' Klein does NOT connect riot to Latin rugire.\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"etymonline.com/word/riot and /word/rumor (fetched and archived 2026-09-13)\",\n              \"stance\": \"partial\",\n              \"note\": \"riot: 'of uncertain origin', with a possible link to Latin rugire 'to roar' presented as speculative. rumor: 'from Latin rumorem … related to ravus \\\"hoarse\\\", from PIE root *reu- \\\"to bellow\\\"' — this half fully supports the chart.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A pass-through box with no forms of its own: the Germanic material Nourai has in mind is whatever underlies English roar and rumble (his two Klein pages, 1352 f. and 1364, are the pages for those two words). Both Klein entries are on the cited pages, but neither derives the word from *reu-: for roar Klein posits 'the I.-E. imitative base *rē-, *rā-, \\\"to cry, roar\\\"', for rumble simply 'of imitative origin'. Pokorny agrees: OE rārian and OHG rēren are filed not under 1. reu- but under the neighbouring imitative lemma rei-3, rē(i)- 'to cry, bellow' (IEW pp.859–860), with only the note 's. auch reu-, rēu-, rū-'. The one Germanic form that is securely under *reu- is ON rymja 'to roar, grumble', rymr 'rough voice' (IEW p.867), and that is exactly the word Klein compares under rumble. So a blank Germanic node hanging straight off *reu- is defensible for rumble but overstates the case for roar.\",\n          \"derivation_fa\": \"این جعبه گذرگاهی است و خود واژه‌ای ندارد: مادهٔ ژرمنیِ موردنظرِ نورایی همان است که پشتِ roar و rumble انگلیسی ایستاده (دو صفحهٔ ارجاعیِ او، ۱۳۵۲ و ۱۳۶۴ کلاین، دقیقاً صفحهٔ همین دو واژه است). هر دو مدخل در همان صفحه‌ها هست، اما کلاین هیچ‌یک را به *reu- بازنمی‌گرداند: roar را از «پایهٔ آواگونِ هندواروپایی *rē-, *rā-» می‌گیرد و rumble را تنها «آواگون» می‌خواند. پوکورنی نیز همین‌گونه: rārian انگلیسی باستان و rēren آلمانی علیای باستان را نه زیر 1. reu- بلکه زیر سرواژهٔ آواگونِ همسایه rei-3, rē(i)- «بانگ زدن، غریدن» (ص ۸۵۹–۸۶۰) آورده و تنها یادداشت کرده «نک. همچنین reu-». تنها صورتِ ژرمنیِ مطمئن زیر *reu-، فعل rymja نورس باستان «غریدن، غرولند کردن» است (پوکورنی ص ۸۶۷) که کلاین نیز زیر rumble به آن ارجاع می‌دهد. پس این گره برای rumble پذیرفتنی و برای roar اندکی فراتر از گواهی منابع است — «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/roar\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1352,1364\",\n              \"status\": \"partial\",\n              \"note\": \"Both pages are right within the resolution of the scan's inline page markers: Klein's 'roar' stands just after the marker '1353' (KLN_1966.txt leaf 719) and 'rumble' between the markers '1360' (leaf 725) and '1365' (leaf 727). But the entries do not say what the arrow says: 'roar … fr. OE. rarian … from the I.-E. imitative base *rē-, *rā-, \\\"to cry, roar\\\"'; 'rumble … ME. romblen, rumblen, of imitative origin. Cp. Du. rommelen, G. rummeln … ON. rymja, \\\"to roar, grumble\\\" … and see rumor.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 pp.1352 f. (roar) and 1364 (rumble)\",\n              \"stance\": \"partial\",\n              \"note\": \"See ref_check: Klein has both words on the cited pages but calls them imitative, not reflexes of *reu-.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp.859–860, lemma 'rei-3, rē(i)-' (POK_full.txt lines 70060–70109)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Root / lemma: rei-3, rē(i)-. Meaning: to cry, bellow, etc., onomatopoeic words. Note: s. also reu-, rēu-, ru- … compare further Old English rārian \\\"blöken, roar, bellow\\\", Old High German rēren ds. … Page(s): 859-860.' Pokorny puts the ancestor of English roar under a different (though adjacent and cross-referenced) root.\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"etymonline.com/word/roar (fetched and archived 2026-09-13)\",\n              \"stance\": \"partial\",\n              \"note\": \"'from Old English rarian … probably of imitative origin', cognates MDu. reeren, G röhren, Skt. rayati, Lith. rieju, OCS revo, Lat. raucus — the last two do belong to *reu-, so the families touch without being identical.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"roar; rumble\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"roar ← ME roren ← OE rārian 'to roar, wail, lament, bellow' (Proto-Germanic *rairōn-), with MDu. rēren, OHG rēren, MHG rēren 'to bleat', G röhren; the noun is late 14c., first of the cry of a large beast, extended to thunder and cannon by the 1540s. The base is imitative and Pokorny/Klein place it under rei-3 / *rē-, *rā- rather than under *reu-, though the two bases are explicitly cross-referenced and the wider family (OCS revǫ 'I roar', Lat. raucus 'hoarse') is *reu-. rumble ← ME romblen/rumblen (c.1384), from or reinforced by MDu. rommelen, MLG rummeln 'to rumble', likewise imitative, with the -b- an English excrescent stop inserted between m and l (as in thimble, humble); Klein compares ON rymja 'to roar, grumble', rymr 'a rough voice', which Pokorny does list under 1. reu- on p.867, and sends the reader on to rumor. Both words therefore sit in the orbit of *reu- as onomatopoeic Germanic formations rather than as regular sound-law descendants.\",\n          \"derivation_fa\": \"«roar» از انگلیسی میانه roren و آن از rārian انگلیسی باستان «غریدن، نالیدن، بانگ زدن» (ژرمنی آغازین *rairōn-) است، با هم‌ریشه‌های rēren هلندی میانه و آلمانی علیای باستان و röhren آلمانی امروز؛ صورت اسمی از اواخر سدهٔ چهاردهم، نخست دربارهٔ بانگِ جانورِ بزرگ و از دههٔ ۱۵۴۰ دربارهٔ رعد و توپ. پایهٔ آن آواگون است و پوکورنی و کلاین آن را زیر rei-3 / *rē-, *rā- می‌آورند نه زیر *reu-، هرچند این دو پایه به یکدیگر ارجاع داده شده‌اند و بخشی از خانواده (revǫ اسلاوی کلیسایی، raucus لاتین) بی‌گمان از *reu- است. «rumble» از انگلیسی میانه romblen (حدود ۱۳۸۴) است، برگرفته یا تقویت‌شده از rommelen هلندی میانه، باز هم آواگون، با «ب»ی میانجی که در انگلیسی میان m و l می‌روید (مانند thimble و humble)؛ کلاین آن را با rymja نورس باستان «غریدن، غرّیدن» می‌سنجد که پوکورنی در ص ۸۶۷ زیر 1. reu- آورده است. پس هر دو واژه در مدارِ *reu- قرار دارند اما نه به‌عنوان بازماندهٔ قاعده‌مندِ آوایی، بلکه به‌عنوان ساخت‌های آواگونِ ژرمنی — «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/roar\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no references of its own; it inherits the parent Germanic box's KLN:1352,1364, checked at node #5 (status partial).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 p.1352 f. s.v. roar; p.1364 s.v. rumble (KLN_1966.txt leaves 719, 725)\",\n              \"stance\": \"partial\",\n              \"note\": \"'roar … ME. roren, raren, fr. OE. rarian, rel. to MDu. reeren … from the I.-E. imitative base *rē-, *rā-, \\\"to cry, roar\\\", whence also OI. rayati \\\"barks\\\" … L. raucus (for *ravicos) \\\"hoarse\\\".' / 'rumble … of imitative origin … ON. rymja \\\"to roar, grumble\\\", rymr \\\"a roaring, grumbling\\\", and see rumor.'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p.867 (ON rymja under 1. reu-) and pp.859–860 (OE rārian under rei-3)\",\n              \"stance\": \"partial\",\n              \"note\": \"'aisl. rymja „brüllen, brummen“, rymr m. „grobe Stimme“' is on p.867 under 1. reu-; but 'ags. rārian' is on pp.859 f. under rei-3.\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"etymonline.com/word/roar (archived 2026-09-13)\",\n              \"stance\": \"partial\",\n              \"note\": \"'probably of imitative origin', with cognates Skt. rayati, Lith. rieju/rieti, OCS revo, Lat. raucus.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Reu 2, Reua, Rů 2, Reup / Reudh 2 / Reud 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *reu- / *reuə- : *rū- 'to tear open, dig, root up; tear out; snatch' (Pokorny 868–871, '2. reu-'), with the extensions *reub-, *reud- 'to tear apart' (→ 'raw, rough'), *reudh- 'to clear land', *reuk- 'to pluck', *reup- 'to tear out, break', *reus-\",\n      \"note\": \"Pokorny prints '2. reu-, reuə-: ru- „aufreißen, graben, aufwühlen; ausreißen; raffen“; zum Teil, wie es scheint, noch volleres ereu- (s. unten); Partiz. Perf. Pass. ru-to-' at the foot of p.868, with the six extensions on pp.869–871 (References: WP. II 351 ff.). Nourai's three glossed sub-headwords map onto Pokorny exactly: 'Reu 2, Reua, Rů 2, Reup : to dig up, tear out, snatch' = the root itself (reu-, reuə-, ru-) plus extension e. reup- 'ausreißen, zerreißen, brechen' (p.870); 'Reudh 2 : to clear land' = extension c. reudh- 'reuten, roden' (p.869); 'Reud 2 : rough' = extension b. reud- 'zerreissen', whose adjective *rud-lo- 'roh, wild' yields Lat. rudis 'unwrought, rough'. Watkins/AHD splits the same material three ways — reu-2 'to smash, knock down, tear out, dig up, uproot', reup- 'to snatch', reudh-2 'to clear land' — each tagged '[Pok. 2. reu- 868]'. Root, language label and all three glosses are correct; the numbering 'Reudh 2' is Nourai's way of keeping this root apart from reudh-1 'red' (IEW 872), a distinction Pokorny and Watkins also make.\",\n      \"note_fa\": \"پوکورنی سرواژهٔ «2. reu-, reuə-: ru- „شکافتن، کندن، زیرورو کردن؛ برکندن؛ ربودن“» را در پایان صفحهٔ ۸۶۸ آورده و شش گسترشِ آن را در صفحه‌های ۸۶۹ تا ۸۷۱ (ارجاع: والده-پوکورنی جلد دوم ص ۳۵۱ به بعد). سه سرواژهٔ معنادارِ نورایی دقیقاً با پوکورنی می‌خواند: «Reu 2, Reua, Rů 2, Reup: کندن، برکندن، ربودن» همان ریشه به‌اضافهٔ گسترشِ reup- «برکندن، دریدن، شکستن» (ص ۸۷۰)؛ «Reudh 2: پاک کردنِ زمین» همان گسترشِ reudh- «بیشه‌زدایی، آماده‌سازیِ زمین» (ص ۸۶۹)؛ و «Reud 2: زبر» همان گسترشِ reud- «دریدن» که صفتِ *rud-lo- «خام، وحشی» و از آن rudis لاتین «ناتراشیده، زبر» را می‌دهد. واتکینز در پیوستِ AHD همین ماده را سه‌پاره می‌کند (reu-2، reup-، reudh-2) و هر سه را به «پوکورنی 2. reu- ص ۸۶۸» بازمی‌گرداند. ریشه، برچسب زبانی و هر سه معنا درست است؛ شمارهٔ «۲» در Reudh 2 برای جدا کردنِ این ریشه از reudh- «سرخ» (ص ۸۷۲) است که پوکورنی و واتکینز نیز همین تفکیک را دارند. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/rag\",\n        \"https://www.etymonline.com/word/rough\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:869\",\n          \"status\": \"supports\",\n          \"note\": \"Exact. The headword stands at the foot of the printed p.868 and the extensions on p.869 (POK_03.txt leaf 104 carries the inline page number '869' followed by 'Erweiterungen: a. reub- … b. reud- „zerreissen“; rud-lo- „roh, wild“ … c. reudh- „reuten, roden“'). POK_full.txt gives 'Root / lemma: reu-2, reus- : ru- … Meaning: to tear out, dig out, open, acquire, etc. … Page(s): 868-871'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"IEW pp.868–871, '2. reu-, reuə-: ru-' (POK_03.txt leaves 104–107)\",\n          \"stance\": \"supports\",\n          \"note\": \"'2. reu-, reuə-: ru- „aufreißen, graben, aufwühlen; ausreißen; raffen“ … Erweiterungen: a. reub- … b. reud- … c. reudh- … d. reuk- … e. reup- … f. reus-. WP. II 351 ff.'\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny Bd. II pp.351–358 (WLD_Bd2_pages.txt lines 23424–23450)\",\n          \"stance\": \"supports\",\n          \"note\": \"Has the same extensions with the same glosses: 'reudh- bes. „reuten, roden“' and 'reup- „ausreißen, zerreißen, brechen“; ai. ropayati … lat. rumpo, -ere, rūpī, ruptum „brechen“'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.vv. reu-2, reup-, reudh-2 (AHD_watkins1985.txt line 897)\",\n          \"stance\": \"supports\",\n          \"note\": \"'reu-2. Also reuə-. To smash, knock down, tear out, dig up, uproot. … [Pok. 2. reu- 868.]'; 'reudh-2. To clear land. … [In Pok. 2. reu- 868.]'; 'reup-. Also reub-. To snatch. … [Pok. 2. reu- 868.]' — the three-way split of exactly Nourai's material.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, IE Comparative Dictionary, s.vv. reudos, reupō (IEC.txt lines 14550, 14574)\",\n          \"stance\": \"supports\",\n          \"note\": \"'reudos (roud-, rud-) \\\"rough, raw, violent\\\". WP II, 351 … (z-gde in) Lat. rudis, adj. \\\"rough, wild\\\"'; 'reupō (rup-) \\\"tear, break, burst, plunder\\\" … Lat. cf. (rumpo, ere), pf. rupi, sup. ruptum … OE reofan \\\"tear, break\\\"; ON rjúfa \\\"break in\\\"'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"raoidya\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Younger Avestan raoiδiia- (Bartholomae's *raoδa-, *raoiδya-) is a -ya- gerundive adjective 'to be made arable, fit to be brought under cultivation', attested in Vidēvdād 6.6: 'if the Mazdayasnians wish to irrigate, plough and dig over a piece of land that is raoiδiia-' (Bartholomae: 'urbar zu machen'), quoted again V 5.7 in the Pahlavi version. It is built to a root *raud-/*rauδ- 'to clear (land)', i.e. PIE *reudh-2 (Pokorny's extension c. of 2. reu-, p.869 — 'reudh- „reuten, roden“. Av. raoidya- „urbar zu machen“'), whose Germanic side gives ON rjóða 'to clear', ryðja 'to clear, root out', OHG riuten 'to clear', riuti 'cleared land', OE ā-ryddan > English rid. Nourai's gloss 'to cultivate land, to be fit for cultivation' renders the gerundive correctly, giving both the verbal and the passive-potential sense. This *reudh- is homonymous with, but unrelated to, *reudh- 'red'. Cheung, whose dictionary covers Iranian verbs only, has no root *raud 'to clear land' (his *(H)raud is 'to tear, break', evidenced only by Pamir forms; his *Hraud 'to grow (bigger)' is YAv. raoδ-, a different word), so he is silent rather than opposed.\",\n          \"derivation_fa\": \"صفتِ اوستایی متأخر raoiδiia- (در بارتولومه *raoδa-, *raoiδya-) صورتی گرونديوی با پسوندِ -ya- است به معنای «آنچه باید آباد شود، شایستهٔ کشت»، در وندیداد ۶٫۶: «اگر مزداپرستان بخواهند زمینی را که raoiδiia- است آبیاری و شخم و کندوکاو کنند» (ترجمهٔ بارتولومه: «urbar zu machen»). این صفت بر ستاکِ *raud-/*rauδ- «پاک کردن و آباد کردنِ زمین» ساخته شده، یعنی *reudh- هندواروپایی (گسترشِ c در پوکورنی، ص ۸۶۹: «reudh- „بیشه‌زدایی، آباد کردن“. اوستایی raoidya- „urbar zu machen“»)، که شاخهٔ ژرمنیِ آن rjóða و ryðja نورس باستان، riuten و riuti آلمانی علیای باستان و ā-ryddan انگلیسی باستان (> rid امروزی) را داده است. معنایی که نورایی آورده («کشت کردنِ زمین، شایستهٔ کشت بودن») هر دو سویهٔ فعلی و مجهول-امکانیِ گروندیو را درست بازمی‌تاباند. این *reudh- تنها هم‌آوای *reudh- «سرخ» است و با آن پیوندی ندارد. چونگ که تنها فعل‌های ایرانی را می‌آورد، ریشهٔ *raud «آباد کردن» ندارد و در این باره خاموش است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1347\",\n              \"status\": \"supports\",\n              \"note\": \"Exact page — Klein's 'rid' stands on the page whose inline marker '1347' heads it (KLN_1966.txt leaf 717): 'rid, tr. v. — ME. ruden, ryden, fr. ON. rydja, \\\"to clear, empty, rid\\\", which is rel. to OHG., MHG. riuten, G. reuten, \\\"to clear land\\\", OHG. riuti, \\\"cleared land\\\" … and prob. cogn. with Avestic rao(i)ϑya, \\\"to cultivate\\\"; prob. fr. I.-E. *reudh-, \\\"to clear land\\\", enlargement of base *reu-, \\\"to dig up\\\", whence also L. ruere, \\\"to dig up\\\".' This is Nourai's arrow verbatim.\"\n            },\n            {\n              \"ref\": \"POK:869\",\n              \"status\": \"supports\",\n              \"note\": \"POK_03.txt leaf 105 (printed p.869): 'c. reudh- „reuten, roden“. Av. raoidya- „urbar zu machen“; aisl. rjōda „reuten, räumen“ … aisl. rydja „roden; aufräumen, ausrotten“, ags. āryddan (engl. rid) „berauben, plündern“ …'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiWb col. 1496 (BRT.txt line 24956)\",\n              \"stance\": \"supports\",\n              \"note\": \"'• j. *raoδa-, *raoiδya-\\\" Adj. (fem. -yā-) „urbar zu machen“: yezi … mazdayasna ząm … raoiδyąm … hixrayaēca karštayaēca parakantayaēca \\\"wenn die M. ein urbar zu machendes Grundstück bewässern, pflügen und umgraben wollen\\\" V. 6.6; zit. 5.7 PūZ.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II p.357 (WLD_Bd2_pages.txt line 23426 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'reudh- bes. „reuten, roden“. Av. raoidya- „urbar zu machen“ (nach Bartholomae Airan.Wb. 1496, ZfdtWtf. 6, 231 zu:) anord. rjōda „reuten, räumen“ … ags. a-ryddan „berauben, plündern“ …' — with the reference to AiWb 1496 that pins the Avestan citation.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etym. Dict. of the Iranian Verb, pp.193–194 (CHEUNG.txt lines 13107–13180)\",\n              \"stance\": \"silent\",\n              \"note\": \"No Iranian verbal root *raud 'to clear land'. Cheung's *(H)raud is 'to tear, break', and he notes 'the evidence for an Ir. root *(H)raud … is limited to modern Pamir forms'; his *Hraud 'to grow (bigger)' is YAv. raoδ- (ruδ-). raoiδiia-, being an adjective, falls outside his scope.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. reudh-2 (AHD_watkins1985.txt line 897)\",\n              \"stance\": \"partial\",\n              \"note\": \"'reudh-2. To clear land. 1. Suffixed zero-grade form *rudh-yo- in Germanic *rudjan in Old Norse rydhja, to clear land: RID. … [In Pok. 2. reu- 868.]' — same root and gloss, but Watkins cites only the Germanic branch, not the Avestan.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"rumpere; rudis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The two Latin words belong to two different enlargements of the same root, exactly as the root box's 'Reup' and 'Reud 2' imply. rumpere 'to break, burst, tear' (perf. rūpī, ppp. ruptum, archaic fut. rupsit) is the nasal-infix present *ru-m-p- to *reup- 'to tear out, break' (Pokorny p.870), beside rūpēs 'steep rock face, cliff' (originally 'torn-off rock') and rūpex 'boor'; the Germanic matches are ON rjúfa, OE rēofan 'to break, tear'. rudis 'unwrought, raw, coarse, rough' belongs instead to extension b. reud- 'zerreissen' (p.869), in the company of rudus, -eris 'crumbled stone, rubble, detritus' and rullus 'coarse, boorish' < *rud-lo-, matched by MIr. rúad 'ruin' and W rhuddion 'bran, refuse'. Ernout-Meillet register both words with Nourai's glosses ('rumpere: briser avec force, rompre'; 'rudis, -e: grossier, brut'), and Mann puts rudis under his root reudos 'rough, raw, violent'.\",\n          \"derivation_fa\": \"این دو واژهٔ لاتین از دو گسترشِ متفاوتِ یک ریشه‌اند، درست همان‌گونه که «Reup» و «Reud 2» در جعبهٔ ریشه اشاره می‌کند. rumpere «شکستن، دریدن» (ماضی rūpī، اسم مفعول ruptum) ستاکِ حالِ نون‌افزودهٔ *ru-m-p- از *reup- «برکندن، شکستن» است (پوکورنی ص ۸۷۰)، در کنارِ rūpēs «پرتگاه، دیوارهٔ سنگیِ شکسته» و rūpex «مردِ ناتراش»؛ همتای ژرمنیِ آن rjúfa نورس باستان و rēofan انگلیسی باستان «شکستن، دریدن» است. اما rudis «ناتراشیده، خام، زبر» به گسترشِ دیگر، یعنی reud- «دریدن» (ص ۸۶۹) تعلق دارد، همراه با rudus «سنگ‌ریزه و آوار» و rullus «درشت، روستایی» از *rud-lo-، و همتاهای ایرلندی میانه rúad «ویرانه» و ولزی rhuddion «سبوس، پس‌ماند». ارنو و مِیه هر دو واژه را با همان معناهای نورایی ثبت کرده‌اند و مان (فرهنگ تطبیقی هندواروپایی) rudis را زیرِ ریشهٔ reudos «زبر، خام، تند» می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:870\",\n              \"status\": \"supports\",\n              \"note\": \"POK_03.txt leaf 106 (the printed '870' appears on leaf 105's end and '871' on leaf 106's end, so this is the p.870/871 opening): 'e. reup- „ausreißen, zerreißen, brechen“; roupā- „Loch, Öffnung“; rūpeis- „Fels“. … lat. rumpō, -ere, rūpī, ruptum „brechen“, rūpes „steile Felswand, Klippe …“.' For rudis see p.869, 'b. reud- „zerreissen“; rud-lo- „roh, wild“. lat. rūdus, -eris n. „zerbröckeltes Gestein, Geröll, Schutt“; auch rudis „unbearbeitet, roh“, rullus „grob, bäurisch“ (*rud-lo-)'.\"\n            },\n            {\n              \"ref\": \"AHD:1537\",\n              \"status\": \"not_checked\",\n              \"note\": \"p.1537 belongs to the 1976 AHD New College appendix, which is not available online (the IA scans of that printing are lending-only). The corresponding entry in the 1985 Watkins reprint reads 'reup-. Also reub-. To snatch. … III. Zero-grade form *rup-. … 2. Nasalized form *ru-m-p- in Latin rumpere, to break (> rūpēs, rock): ROUT, RUPTURE; ABRUPT, BANKRUPT, CORRUPT, DISRUPT, ERUPT, INTERRUPT, IRRUPT … [Pok. 2. reu- 868.]' — it supports rumpere but does not mention rudis.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet, s.vv. rudis and rumpo (LAT.txt lines 54061, 54279)\",\n              \"stance\": \"supports\",\n              \"note\": \"'rudis, -e: grossier, brut. Au sens moral \\\"non dégrossi (opposé à politus …), inexpérimenté, inculte, ignorant, novice\\\". Ancien, usuel et classique.' / 'rumpo, -is, rupi (sur un futur archaïque rupsit …), ruptum, rumpere: briser avec force, rompre (souvent avec une idée accessoire d'arrachement, d'éclatement …).'\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.vv. reudos and reupō (IEC.txt lines 14550, 14574)\",\n              \"stance\": \"supports\",\n              \"note\": \"'reudos (roud-, rud-) \\\"rough, raw, violent\\\". WP II, 351 … (z-gde in) Lat. rudis, adj. \\\"rough, wild\\\"'; 'reupō (rup-) \\\"tear, break, burst, plunder\\\" … Lat. cf. (rumpo, ere), pf. rupi, sup. ruptum'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II p.357 f. (WLD_Bd2_pages.txt line ~23440)\",\n              \"stance\": \"supports\",\n              \"note\": \"'reup- „ausreißen, zerreißen, brechen“; … lat. rumpo, -ere, rūpī, ruptum „brechen“, rūpes „steile Felswand, Klippe, Felskluft, jäher Abgrund“ … rūpex, -icis „ruppiger klotziger Mensch, Rüpel“.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"rupture, abrupt, bankrupt, corrupt, disrupt, interrupt; rough\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The first group is right. rupture ← ME ruptur ← MF/F rupture ← Lat. ruptūra 'a fracture, breach' (to ruptus, ppp. of rumpere); abrupt ← Lat. abruptus (ab- + ruptus), 15th–16th c.; corrupt ← Lat. corruptus (com- + ruptus), c.1300 via OF; disrupt ← Lat. disruptus/dīruptus; interrupt ← Lat. interruptus; bankrupt ← It. banca rotta 'broken bench' (a money-changer's bench broken when he failed), relatinised in English on ruptus. Klein's entry for rupture cross-refers to exactly this list. But 'rough' cannot come from Latin rudis. English rough is inherited Germanic: OE rūh, rūg- 'not smooth to the touch, coarse, hairy, shaggy' < WGmc *rūhwaz (Du. ruig, OHG rūh, MHG ruch, G rauh, rauch), which Pokorny files under his extension d. reuk- on p.870 beside Skt. rūkṣá- 'rough' and Lat. rūga 'wrinkle', and which Klein — the dictionary Nourai himself cites for other nodes — derives from 'I.-E. base *ruq-, *rug-'. The Latin word for 'rough' in the reud- group is rudis, but it never entered English as 'rough' (English borrowed only rude, from the same rudis, in the 14th c.). So the chart is right that 'rough' belongs somewhere under this large root, and right that rudis means 'rough', but wrong to draw English rough out of the Latin box: it is a different extension, a different branch, and no borrowing.\",\n          \"derivation_fa\": \"دستهٔ نخست درست است: rupture از انگلیسی میانه ruptur و فرانسویِ میانه rupture و آن از ruptūra لاتین «شکستگی» (از ruptus، اسم مفعولِ rumpere)؛ abrupt از abruptus، corrupt از corruptus (از راه فرانسوی باستان، حدود ۱۳۰۰)، disrupt از disruptus، interrupt از interruptus، و bankrupt از banca rotta ایتالیایی «نیمکتِ شکسته» که در انگلیسی بر پایهٔ ruptus لاتینی‌سازی شده است. اما «rough» نمی‌تواند از rudis لاتین آمده باشد. rough واژه‌ای است ارثی و ژرمنی: انگلیسی باستان rūh, rūg- «ناهموار، پرمو، زبر» از ژرمنیِ غربیِ *rūhwaz (هلندی ruig، آلمانی علیای باستان rūh، آلمانی rauh)، که پوکورنی آن را در ص ۸۷۰ زیرِ گسترشِ reuk- در کنار rūkṣá- سنسکریت و rūga لاتین «چین» آورده و کلاین — همان فرهنگی که نورایی در گره‌های دیگر بدان ارجاع می‌دهد — از «پایهٔ هندواروپاییِ *ruq-, *rug-» می‌گیرد. از rudis لاتین در انگلیسی تنها rude (سدهٔ چهاردهم) وام گرفته شده، نه rough. پس درست است که «زبر» جایی در این ریشهٔ بزرگ می‌گنجد و درست است که rudis یعنی «زبر»، ولی کشیدنِ roughِ انگلیسی از جعبهٔ لاتین نادرست است: گسترشی دیگر، شاخه‌ای دیگر و بی هیچ وام‌گیری. پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/rough\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:1133,1537\",\n              \"status\": \"partial\",\n              \"note\": \"Both numbers are 1976 AHD New College pages (1537 in the IE appendix, 1133 in the main r- section), and that printing is not accessible online. What can be checked, the 1985 Watkins reprint, lists exactly Nourai's first group under reup- ('ROUT, RUPTURE; ABRUPT, BANKRUPT, CORRUPT, DISRUPT, ERUPT, INTERRUPT, IRRUPT') but contains no entry deriving ROUGH from Latin; grep of AHD_watkins1985.txt for 'ROUGH' as a derivative returns nothing under any reu- root.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 p.1359 s.v. rough; p.1365 s.v. rupture (KLN_1966.txt leaves 723, 726)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'rough, adj. — ME. rouh, rough, ruw, rugh, fr. OE. ruh, \\\"rough, untrimmed, uncultivated\\\", rel. to MDu. ru, ruuch, ru, Du. ruig, OHG. ruh, ruher, MHG. ruch, ruher, G. rauh, rauch, fr. I.-E. base *ruq-, *rug-, whence also Lith. raukas \\\"wrinkle\\\" … OI. rukṣáh \\\"rough\\\", L. ruga \\\"wrinkle\\\".' No Latin rudis anywhere. The rupture entry, by contrast, supplies exactly Nourai's Latin list.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p.870, extension d. reuk- (POK_03.txt leaf 106)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'d. reuk- (z. T. wohl auch reug-, reugh-?) „rupfen“ … mit dem Begriff der (ausgerauften) Wollzotten und der damit verbundenen Rauheit … ai. rūkṣá- „rauh“, ahd. rūh, ags. rūh „rauh, behaart; ungebildet“ … und mit g: lat. rūga „Runzel, Falte“.' English rough descends from ags. rūh here, not from lat. rudis (p.869, extension b).\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"etymonline.com/word/rough (fetched and archived 2026-09-13)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'from Old English ruh, rug- \\\"not smooth to the touch, coarse (of cloth); hairy, shaggy\\\", from West Germanic *rukhwaz … perhaps related to the source of Sanskrit ruksah \\\"rough\\\" …'. Latin rudis is not mentioned at all.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"rutjan; rupja; raubôn; raubô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Four Germanic forms, each a reflex of a different corner of the same root, and all four are in Pokorny and in Watkins. (1) *riutjan / *rudjan 'to clear land, get rid of' < *rudh-yo- to extension c. reudh-: OHG riuten, riuti 'cleared land', ON ryðja 'to clear, tidy, root out' (Pok. 869; Watkins 'Germanic *rudjan in Old Norse rydhja, to clear land: RID'). (2) *rupjan / *ruppjan 'to pluck, rip up' < extension a. reub- / e. reup- with the Germanic expressive gemination (Verschärfung): Goth. raupjan 'to pluck', OE rȳpan 'to plunder', OHG roufen, ME ryppen, Flemish rippen (Pok. 869; Watkins 'Germanic *rupja in Flemish rippen, to rip: RIP'). (3) *raubōn 'to rob', the o-grade *roup- denominative: Goth. bi-raubōn, OHG roubōn, OS rōbon 'rauben'. (4) *raubō / *rauba 'what is stripped off; booty, and hence clothing taken as booty': OE rēaf 'plunder, booty, garment, armour', OHG roub, ON rauf 'gap, hole', with the regular Germanic *p > f/b (Grimm) from *roup-. Nourai's glosses ('to clear land, get rid of'; 'to rip up'; 'to rob'; 'clothes taken as booty') reproduce these sources almost word for word — the last is Watkins's own phrase, 'Germanic *raubō, booty, in Old French robe, robe (> \\\"clothes taken as booty\\\"): ROBE'.\",\n          \"derivation_fa\": \"چهار صورتِ ژرمنی که هر یک بازتابِ گوشه‌ای از همان ریشه است و هر چهار در پوکورنی و واتکینز آمده‌اند. یکم، *riutjan/*rudjan «آباد کردنِ زمین، رهاندن» از *rudh-yo- و گسترشِ reudh-: riuten آلمانی علیای باستان، riuti «زمینِ پاک‌شده»، ryðja نورس باستان (پوکورنی ص ۸۶۹؛ واتکینز: «ژرمنی *rudjan در ryðja نورس باستان: RID»). دوم، *rupjan/*ruppjan «کندن، دریدن» از گسترش‌های reub-/reup- با مشدّدسازیِ بیانیِ ژرمنی: raupjan گوتی «کندن»، rȳpan انگلیسی باستان «تاراج کردن»، roufen آلمانی علیای باستان، ryppen انگلیسی میانه، rippen فلاندری (واتکینز: «ژرمنی *rupja در rippen فلاندری: RIP»). سوم، *raubōn «غارت کردن»، فعلِ اسمیِ پایهٔ o-دارِ *roup-: bi-raubōn گوتی، roubōn آلمانی علیای باستان، rōbon ساکسونی باستان. چهارم، *raubō/*rauba «آنچه از تن کنده شود؛ غنیمت و از همین‌رو جامهٔ غنیمتی»: rēaf انگلیسی باستان «غارت، غنیمت، جامه، زره»، roub آلمانی علیای باستان، با تبدیل قاعده‌مندِ *p ژرمنی به f/b (قانون گریم) از *roup-. معناهایی که نورایی داده تقریباً واژه‌به‌واژه از همین منابع است؛ «جامهٔ گرفته‌شده به غنیمت» عینِ عبارتِ واتکینز است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1347\",\n              \"status\": \"supports\",\n              \"note\": \"Klein p.1347 s.v. rid gives the *riutjan/*rudjan family: 'ON. rydja, \\\"to clear, empty, rid\\\", which is rel. to OHG., MHG. riuten, G. reuten, \\\"to clear land\\\", OHG. riuti, \\\"cleared land\\\", and to OFris. rothia, MLG. roden, MHG. roten, G. roden, \\\"to clear\\\"'.\"\n            },\n            {\n              \"ref\": \"POK:869\",\n              \"status\": \"supports\",\n              \"note\": \"POK_03.txt leaves 105–106 (printed pp.869–871): 'a. reub- „reissen“ … germ. *raup-, *rupp- (mit Verschärfung) in got. raupjan „rupfen“, ags. rīepan „ausplündern“, ahd. roufen … mengl. ryppen, engl. rip „reißen“'; 'c. reudh- … ahd. riuti ds., riuten (*riutjan) „reuten“ … aisl. rydja „roden“'; 'e. reup- … ags. reaf n. „Raub, Beute, Kleid, Rüstung“ (*roupa …), ahd. roub m. ds., zu got. bi-raubōn, ahd. roubōn, as. rōbōn „rauben“'.\"\n            },\n            {\n              \"ref\": \"AHD:1537\",\n              \"status\": \"partial\",\n              \"note\": \"The 1976 appendix page is inaccessible; the 1985 Watkins reprint has all four forms: 'reup-. Also reub-. To snatch. I. Basic form *reub- in Germanic *rupja in Flemish rippen, to rip: RIP. II. O-grade form *roup-. … 2. Germanic *raubōn, to rob … 3. Germanic *raubō, booty, in Old French robe, robe (> \\\"clothes taken as booty\\\"): ROBE'; and 'reudh-2. To clear land. … Germanic *rudjan in Old Norse rydhja, to clear land: RID.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp.869–871, extensions a/c/e of 2. reu- (POK_03.txt leaves 105–106)\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check — all four Germanic stems are printed there.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.vv. reup-, reudh-2 (AHD_watkins1985.txt line 897)\",\n              \"stance\": \"supports\",\n              \"note\": \"Gives *rupja, *raubōn, *raubō and *rudjan under the same root, with Nourai's very glosses.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict., s.v. Reave (SKT.txt line 15714)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Reave, to rob. (E.) M.E. reven … A.S. rēafian, to despoil, lit. to strip. — A.S. rēaf, clothing, a robe, spoil, plunder. — A.S. rēaf, pt. t. of strong verb rēofan, to deprive. + Icel. raufa, to reave, from sb. rauf spoil, which from rauf pt. t. of rjúfa, to break up, violate; G. rauben, to rob, from Raub, plunder. (√RUP.)' — Skeat derives the *raubō(n) group from the root RUP, i.e. Nourai's Reup.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"rid; rip; rob, robber, rover, rubbish, rubble; robe\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"rid: certain — ME ruden/ryden, a 12th–13th c. Norse loan from ON ryðja 'to clear, empty' (Klein p.1347), so 'rid' is the Germanic *rudjan of the parent box. rip: probable — late-ME rippen, from a Low German or Scandinavian source (Frisian rippe, MLG reppen, Flemish rippen, Swed. reppa, Dan. rippe) continuing Gmc *rupjan; Watkins gives exactly 'Germanic *rupja in Flemish rippen, to rip: RIP', while Klein adds 'possibly of imitative origin'. rob, robber, robe: certain but Romance-mediated — ME robben ← OF rober ← Frankish/West-Germanic *raubōn; robe ← OF robe 'booty; booty of garments; gown' ← WGmc *rauba (whence also OProv. rauba, It. roba, Sp. ropa); robber ← OF robere. These reached English through French, not by direct inheritance, which the single arrow hides. rover: certain — late 14c. ← MDu. rover 'robber, pirate' (zeerovere 'sea-robber') to roven 'to rob', from roof 'plunder' = OE rēaf; a Dutch loan. rubbish, rubble: uncertain — first attested c.1400 as Anglo-French rubouses / robeux and ME robyl, robel; Pokorny does put 'engl. rubble, rubbish \\\"Schutt, Abfall\\\"' under extension e. reup- (p.870 f.) and Skeat files 'Rubbish, Rubble' under Reave (i.e. OF robe), but Klein — the dictionary Nourai cites here — relates rubbish instead to rub ('perh. orig. meaning \\\"that which is rubbed off\\\"') and rubble to rubbish, and the OED/Etymonline call the ultimate origin unknown, noting 'there are said to be no apparent cognates in Old French'. So the node is right in the main and overstated only for rubbish/rubble; hence plausible rather than confirmed.\",\n          \"derivation_fa\": \"«rid»: قطعی — انگلیسی میانه ruden/ryden، وام‌واژه‌ای نورسی از سده‌های دوازدهم و سیزدهم از ryðja «پاک کردن، تهی کردن» (کلاین ص ۱۳۴۷)، یعنی همان *rudjanِ جعبهٔ بالا. «rip»: محتمل — rippen در اواخر انگلیسی میانه، از سرچشمه‌ای آلمانی-پست یا اسکاندیناویایی (rippe فریزی، reppen آلمانی پست میانه، rippen فلاندری، reppa سوئدی) که دنبالهٔ *rupjan ژرمنی است؛ واتکینز عیناً «ژرمنی *rupja در rippen فلاندری: RIP» را می‌آورد، هرچند کلاین احتمال آواگون بودن را نیز می‌افزاید. «rob, robber, robe»: قطعی اما با میانجیِ رومی — robben انگلیسی میانه از rober فرانسوی باستان و آن از *raubōnِ فرانکی/ژرمنیِ غربی؛ robe از robe فرانسوی باستان «غنیمت؛ جامهٔ غنیمتی؛ جامه» از *rauba (که rauba پرووانسی، roba ایتالیایی و ropa اسپانیایی نیز از آن است). این‌ها از راه فرانسه به انگلیسی رسیده‌اند، نه از راه ارث — و پیکانِ یگانهٔ نمودار این نکته را می‌پوشاند. «rover»: قطعی — اواخر سدهٔ چهاردهم از rover هلندی میانه «دزد، دزد دریایی» از roven «غارت کردن». «rubbish» و «rubble»: نامطمئن — نخستین بار حدود ۱۴۰۰ به صورت rubouses/robeux در انگلوفرانسه و robyl در انگلیسی میانه؛ پوکورنی «rubble, rubbish انگلیسی» را زیر گسترشِ reup- می‌آورد (ص ۸۷۰ به بعد) و اسکیت هر دو را زیر Reave می‌گذارد، اما کلاین — همان فرهنگی که نورایی اینجا بدان ارجاع می‌دهد — rubbish را به rub می‌بندد و فرهنگ آکسفورد خاستگاه را ناشناخته می‌خواند. پس این گره در کلیت درست است و تنها در rubbish/rubble فراتر از گواهی می‌رود: «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/rubbish\",\n            \"https://www.etymonline.com/word/rover\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:870\",\n              \"status\": \"supports\",\n              \"note\": \"POK_03.txt leaf 106 (printed pp.870–871), extension e. reup-: 'ags. reaf n. „Raub, Beute, Kleid, Rüstung“ … ahd. roub m. ds., zu got. bi-raubōn, ahd. roubōn, as. rōbōn „rauben“ … geminiert ostfries. rubben „kratzen, reiben, rupfen“, nd. rubbelig, rubberig „uneben, rauh“, nhd. ruppig „struppig“, engl. rubble, rubbish „Schutt, Abfall“' — Pokorny does place rubble and rubbish here.\"\n            },\n            {\n              \"ref\": \"KLN\",\n              \"status\": \"partial\",\n              \"note\": \"Klein supports rid (p.1347, ON rydja), rob and robe (p.1353: 'rob … fr. OF. rober … fr. OF. robe, \\\"booty; booty of garments; gown, dress, robe\\\", fr. WTeut. *rauba'; 'robe, n. — ME., fr. OF. robe … see rob') and rover (p.1360: 'rover, n., sea robber, pirate. — ME., fr. MDu. rover … fr. MDu. roven, \\\"to rob, plunder\\\", fr. MDu. roof, \\\"spoil, plunder\\\", which is rel. to OE. reaf'), but contradicts the chart for rubbish and rubble: 'rubbish, n., waste, refuse. — ME. robeux, robous, robys; perh. orig. meaning \\\"that which is rubbed off\\\" and rel. to rub.' / 'rubble, n., broken pieces of stone. — ME. robyl, robel, rubel, prob. rel. to prec. word.'\"\n            },\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. reup-: 'Germanic *rupja in Flemish rippen, to rip: RIP. … 2. Germanic *raubōn, to rob, in: a. Middle Dutch and Middle Low German rōven, to rob: ROVER; b. Old French rober, to rob: ROB … 3. Germanic *raubō, booty, in Old French robe, robe (> \\\"clothes taken as booty\\\"): ROBE.' Four of Nourai's words, with the French/Dutch stages spelled out; RID is under reudh-2. Watkins does not list rubbish/rubble.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 pp.1347 (rid), 1353 (rob, robber, robe), 1360 (rover, rubbish, rubble)\",\n              \"stance\": \"partial\",\n              \"note\": \"See ref_check: supports rid/rob/robe/rover, contradicts the chart on rubbish and rubble by referring them to rub.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.vv. rubbish, rubble and the index entries 'Rob, Robe; see Reave' and 'Rubbish, Rubble; see Reave' (SKT.txt lines 15720, 15721, 16167, 16257)\",\n              \"stance\": \"supports\",\n              \"note\": \"'rubbish … M.E. robeus, robous … Rubbish is, in fact, a corrupt form of the old plural of rubble'; 'rubble … answers exactly to an old form robel, O.F. robel, only found in the pl. robeux … Obviously the dimin. of F. robe in sense of \\\"trash\\\"'; and the cross-index 'Rubbish, Rubble; see Reave' — i.e. Skeat does take them back to OF robe and thus to the root RUP, as Nourai does.\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"etymonline.com/word/rubbish and /word/rover (fetched and archived 2026-09-13)\",\n              \"stance\": \"partial\",\n              \"note\": \"rover: 'from Middle Dutch rover \\\"robber, predator, plunderer\\\" … from Dutch roven \\\"to rob\\\"' — supports. rubbish: 'c.1400, from Anglo-French rubouses … ultimate origin unclear, \\\"there are said to be no apparent cognates in Old French\\\"'; rubble 'possibly connects to Old French robe … though this association is uncertain' — the weak link.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Old Norse\",\n          \"words\": \"ryja; rogg\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both forms stand in Pokorny's main material for 2. reu- on the printed page 868, exactly as cited. ON rýja 'to pull the wool off sheep' is a jan-verb formed straight to the bare root *reu- 'to tear out' (Norw. ru f. 'winter wool' is the corresponding noun; OS rūwi f. 'shaggy pelt' belongs with it). ON rǫgg f., rǫggr m. 'long hair, long wool, shaggy tuft' goes back to Germanic *rawwa- < the suffixed o-grade *rous-o- (Watkins), beside Swedish rugg 'shaggy hair' < *ruwwa-; the geminate -gg- is the regular Norse outcome of *-ww- (Holtzmann's law / Verschärfung). The semantic tie is the one Pokorny points out: the root means 'tear out', and plucked wool and shagginess are what you get from tearing it out — the same idea that gives the 'rough' sense under extension d. reuk-.\",\n          \"derivation_fa\": \"هر دو صورت در بخشِ اصلیِ مدخل «2. reu-» پوکورنی در صفحهٔ چاپیِ ۸۶۸ آمده‌اند، درست همان‌جا که نورایی ارجاع داده است. rýja نورس باستان «کندنِ پشم از گوسفند» فعلی با پسوندِ -jan است که مستقیماً بر خودِ ریشهٔ *reu- «برکندن» ساخته شده (ru نروژی «پشمِ زمستانی» اسمِ همتای آن است). rǫgg (مؤنث) و rǫggr (مذکر) «موی بلند، پشمِ بلند، دستهٔ پشمالو» به ژرمنیِ *rawwa- از پایهٔ o-دارِ پسونددارِ *rous-o- بازمی‌گردد (واتکینز)، در کنارِ rugg سوئدی «موی ژولیده» از *ruwwa-؛ مشدّد شدنِ -gg- برآیندِ قاعده‌مندِ *-ww- در نورسی است (قانون هولتسمان). پیوندِ معنایی همان است که پوکورنی نشان می‌دهد: ریشه یعنی «برکندن»، و پشمِ کنده‌شده و ژولیدگی نتیجهٔ همان برکندن است — همان اندیشه‌ای که در گسترشِ reuk- معنای «زبر» را می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:868\",\n              \"status\": \"supports\",\n              \"note\": \"Exact page. POK_03.txt leaf 104 (the inline printed page number '869' follows at its end, so this is p.868): 'aisl. ryja „den Schafen die Wolle ausreißen“ (norw. rū f. „Winterwolle“), as. rūwi f. „rauhes Fell“; aisl. rǫgg f., rǫggr m. „langes Haar, lange Wolle“ (*rawwa-), schwed. rugg „zottiges Haar“ (*ruwwa-); daraus engl. rug.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p.868 (POK_03.txt leaf 104)\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check — both ON forms with Nourai's glosses.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. reu-2 (AHD_watkins1985.txt line 897)\",\n              \"stance\": \"supports\",\n              \"note\": \"'reu-2. Also reuə-. To smash, knock down, tear out, dig up, uproot. 1. Suffixed o-grade form *rous-o- in Germanic *rawwa- in: a. Old Norse rǫgg, rǫggr, woven tuft of wool: RAG; b. Norwegian rugga, rogga, coarse coverlet, akin to the Scandinavian source of RUG. … [Pok. 2. reu- 868.]'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 p.1363 s.v. rug (KLN_1966.txt leaf 725)\",\n              \"stance\": \"supports\",\n              \"note\": \"'rug, n. — Of Scand. origin. Cp. Swed. rugg, \\\"rough hair\\\", ON. rogg, \\\"tuft, shagginess\\\"; rel. to E. rag and rough and to the next word.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"rug, rugged, rag, ragged\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four are the English side of the Old Norse box, and the route is borrowing rather than inheritance — correctly so, since English has no native reflex of *rawwa-. rag (early 14c., 'a torn scrap of cloth') is from a Scandinavian source, ON rǫgg 'shaggy tuft, rough hair' / Old Danish rag, from Gmc *rawwa-; ragged (c.1300, first 'shaggy, rough') is the -ed adjective to it, and Etymonline notes rag may even be a back-formation from ragged. rug (1550s, first 'coarse woollen cloth', then 'floor covering' from the 1640s) is likewise Scandinavian, from a form like Swedish rugg 'shaggy hair' / Norwegian rugga 'coarse coverlet' < *ruwwa-; rugged (c.1300, of animals, 'shaggy, hairy') is the -ed adjective to rug, whence 'rough, uneven' of ground. Pokorny states the borrowing explicitly on the very page Nourai cites ('schwed. rugg „zottiges Haar“ (*ruwwa-); daraus engl. rug'), and Watkins routes RAG through ON rǫgg and RUG through the Norwegian form.\",\n          \"derivation_fa\": \"هر چهار واژه سویهٔ انگلیسیِ جعبهٔ نورسِ باستان‌اند و راهِ آن‌ها وام‌گیری است نه ارث — و همین درست است، چون انگلیسی بازماندهٔ بومی برای *rawwa- ندارد. «rag» (اوایل سدهٔ چهاردهم، «پارهٔ جامه») از سرچشمه‌ای اسکاندیناویایی است: rǫgg نورس باستان «دستهٔ پشمالو، موی زبر» یا rag دانمارکی کهن، از ژرمنیِ *rawwa-؛ «ragged» (حدود ۱۳۰۰، نخست «پشمالو، زبر») صفتِ -ed دارِ آن است و اتیمانلاین حتی احتمال می‌دهد rag اشتقاقِ پس‌ساز از ragged باشد. «rug» (دههٔ ۱۵۵۰، نخست «پارچهٔ پشمیِ درشت» و از دههٔ ۱۶۴۰ «فرش») نیز اسکاندیناویایی است، از صورتی چون rugg سوئدی «موی ژولیده» یا rugga نروژی «روانداز درشت‌باف» از *ruwwa-؛ «rugged» (حدود ۱۳۰۰، دربارهٔ جانوران: «پشمالو») صفتِ -ed دارِ rug است و از آنجا معنای «ناهموار» برای زمین. پوکورنی این وام‌گیری را در همان صفحه‌ای که نورایی ارجاع داده صریح می‌گوید: «rugg سوئدی … و از آن rug انگلیسی». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/rag\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:868\",\n              \"status\": \"supports\",\n              \"note\": \"POK_03.txt leaf 104 (printed p.868): 'aisl. rǫgg f., rǫggr m. „langes Haar, lange Wolle“ (*rawwa-), schwed. rugg „zottiges Haar“ (*ruwwa-); daraus engl. rug.' Pokorny names the English word on the cited page.\"\n            },\n            {\n              \"ref\": \"KLN:1363\",\n              \"status\": \"supports\",\n              \"note\": \"Klein's 'rug' and 'rugged' stand between the scan's inline page markers '1360' (leaf 725) and '1365' (leaf 727), i.e. on p.1363 as cited: 'rug, n. — Of Scand. origin. Cp. Swed. rugg, \\\"rough hair\\\", ON. rogg, \\\"tuft, shagginess\\\"; rel. to E. rag and rough and to the next word.' / 'rugged, adj. — Formed fr. rug with 1st suff. -ed.'\"\n            },\n            {\n              \"ref\": \"AHD:1077,1134\",\n              \"status\": \"not_checked\",\n              \"note\": \"Main-dictionary pages of the 1976 AHD New College Edition (r- section), which is lending-only on archive.org. The 1985 Watkins reprint carries the same claim in the root entry: 'reu-2 … Old Norse rǫgg, rǫggr, woven tuft of wool: RAG; b. Norwegian rugga, rogga, coarse coverlet, akin to the Scandinavian source of RUG.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW p.868 (POK_03.txt leaf 104)\",\n              \"stance\": \"supports\",\n              \"note\": \"'… schwed. rugg „zottiges Haar“ (*ruwwa-); daraus engl. rug.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. reu-2 (AHD_watkins1985.txt line 897)\",\n              \"stance\": \"supports\",\n              \"note\": \"Routes RAG through ON rǫgg and RUG through Norwegian rugga/rogga, both from Germanic *rawwa- < *rous-o-.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 p.1363 s.vv. rug, rugged\",\n              \"stance\": \"supports\",\n              \"note\": \"'rug … Of Scand. origin … rel. to E. rag and rough'; 'rugged, adj. — Formed fr. rug with 1st suff. -ed.'\"\n            },\n            {\n              \"src\": \"Etymonline\",\n              \"where\": \"etymonline.com/word/rag (fetched and archived 2026-09-13)\",\n              \"stance\": \"supports\",\n              \"note\": \"'probably from a Scandinavian source (compare Old Norse rögg \\\"shaggy tuft, rough hair\\\") … Old Danish rag … Proto-Germanic *rawwa- … PIE root *reuə- (2) \\\"to smash, knock down, tear up, uproot\\\"'; ragged is the adjective, and rag may be a back-formation from it.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:41:37.255Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-423.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:41:43.277Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-423.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 423"
}
```


### [2026-09-14T01:41:44.724Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 8, 'plausible': 4, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 12, 'not_checked': 5, 'partial': 4}
books consulted: {'supports': 23, 'silent': 2, 'partial': 11, 'contradicts': 4} | by book: {'POK': 8, 'KLN': 7, 'Etymonline': 6, 'AHD': 4, 'CHEUNG': 3, 'WLD': 3, 'BRT': 2, 'LAT': 2, 'SKT': 2, 'SOD': 1, 'SYN': 1, 'IEC': 1}
```


## [2026-09-14T01:42:02.993Z] AGENT

Page 423 (book p. 393) verified — `data/verification/page-423.json` written, `verify_check.py 423` shows **0 PROBLEM** lines.

**Counts:** 13/13 nodes · confirmed 8, plausible 4, disputed 1 · 2 roots both confirmed · ref checks: 12 supports, 4 partial, 5 not_checked · 40 `consulted` entries across POK, WLD, AHD/Watkins, KLN, SKT, BRT, CHEUNG, SOD, LAT, IEC, SYN, Etymonline.

**Disputed (1)**
- Reu 2 · node #3 English **rough** (drawn from Latin *rudis*): English *rough* is inherited Germanic, OE *rūh* < WGmc \*rūhwaz, which Pokorny files under extension **d. reuk-** (p. 870) and Klein — Nourai's own source, p. 1359 — under IE \*ruq-/\*rug-. Same root family, wrong branch, and no Latin route (English took only *rude* from *rudis*). The rest of that node (rupture, abrupt, bankrupt, corrupt, disrupt, interrupt ← *rumpere*) is confirmed.

**Transcription_suspect:** none. **Extraction errors:** none — the printed page (rendered and read; copy saved to `data/verification/sources/refs/ocr/BOOK/423.png`) matches `page-423.json` exactly, including `rwš`, `rŭgîre`, `rŭ-mor`, `raubô`.

**Notable weaker links (marked plausible, not errors):**
- Reu 1 nodes #5/#6: Klein's own pp. 1352 f./1364 call *roar* and *rumble* imitative, and Pokorny puts OE *rārian* under the neighbouring root **rei-3** (pp. 859–860), not \*reu-; only ON *rymja* (p. 867) is securely here.
- Reu 1 node #4: *rumor* certain, *riot* "of uncertain origin" (Klein p. 1346); the *rugīre* link is a conjecture.
- Reu 2 node #5: *rid/rip/rob/robe/rover* confirmed (via OF/MDu.), but *rubbish/rubble* are Anglo-French of unknown origin; Pokorny p. 870 f. and Skeat back Nourai, Klein contradicts him.

**Good finds confirming Nourai:** Gharib SOD p. 346 no. 8593 prints "rws-2 rōs ©IE \*reu(s) — (to) roar" — his own source states the arrow (he writes š for her s). Klein p. 1347 s.v. *rid* and Pokorny p. 869 both give Av. *raoiδya-* "urbar zu machen" exactly as charted (Bartholomae AiWb col. 1496, Vd. 6.6). All page numbers he cites (POK 867/868/869/870, KLN 1347/1352/1363/1364, SOD 346) check out against the inline page markers in the scans.

**Not checkable:** AHD:1537 / 1133 / 1077 / 1134 are 1976 New College pages (lending-only on IA); the local Watkins 1985 OCR has lost the body of the `reu-1` entry, so the bare "AHD" on the Latin *rugīre/rūmor* node is `not_checked`.
