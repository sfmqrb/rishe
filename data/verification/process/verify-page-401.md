# Verification process log — verify-page-401


## [2026-09-14T00:52:56.047Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 401 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-401.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-401.json. Write /home/sfmqrb/git/rishe/data/verification/page-401.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 401` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:52:57.191Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:52:58.155Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:52:58.172Z] TOOL RESULT

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


## [2026-09-14T00:52:58.581Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-401.txt"
}
```


### [2026-09-14T00:52:58.601Z] TOOL RESULT

```
1	=== PDF page 401 (book page 371) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pet 2 : to spread  (refs POK:824)
4	#1 (parent #0) [Avestan] refs=POK:824 | pathana, perethu : wide
5	  #2 (parent #1) [Persian] refs=BQT:433 | pahn «پَهن ( پهنا ، پهنه )» : wide
6	#3 (parent #0) [Latin] refs=POK:824 | pandere : to spread out (walk) ; passus : step, pace
7	  #4 (parent #3) [French] refs=None | 
8	    #5 (parent #4) [Persian] refs=MON | pâssâge «پاساژ» ; pâsport «پاسپورت» : passport
9	    #6 (parent #4) [English] refs=AHD | pass, passage, passport, compass, pace
10	#7 (parent #0) [Greek] refs=AHD:980 | petalon : leaf ; patanĕ : platter, a wide plate or pot (pan)
11	  #8 (parent #7) [English] refs=None | petal, pan
12	--- entry 1 ---
13	ROOT [Indo-European] Peu, Peue, Pu 1 : to purify  (refs None)
14	#1 (parent #0) [Avestan] refs=HRN:62 | pâvaka : pure, clean
15	  #2 (parent #1) [Pahlavi] refs=None | 
16	    #3 (parent #2) [Persian] refs=None | pâk «پاک» : clean, pure
17	#4 (parent #0) [Latin] refs=AHD; KLN | pŭrus : clean
18	  #5 (parent #4) [English] refs=None | pure
19	--- entry 2 ---
20	ROOT Peua -> redirect to Pŭ 4
21	--- entry 3 ---
22	ROOT [Indo-European] Peud, Spheud : to press, hasten  (refs POK:998)
23	#1 (parent #0) [Old Iranian] refs=FFD:44 | paud, paud-a : to run
24	  #2 (parent #1) [Pahlavi] refs=FFD:44 | pôy : to run
25	    #3 (parent #2) [Persian] refs=POK:998; ISS:130; MON:826 | pŭ «پو ( پوی ، پویه ، تکاپو )» : running ; pŭyîdan «پوییدن ( پوینده )» : to walk fast ; pŭyâ «پویا ( پویان )» : runner ; pŭyânîdan «پویانیدن ( پویاندن )» : to make animals go fast
26	#4 (parent #0) [Greek] refs=POK:998 | speudo : hasten
27	--- entry 4 ---
28	ROOT Peue -> redirect to Peu
29	
```


## [2026-09-14T00:53:01.271Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-401.json | head -200",
 "description": "Read source JSON"
}
```


### [2026-09-14T00:53:01.361Z] TOOL RESULT

```
{
  "pdf_page": 401,
  "book_page": 371,
  "entries": [
    {
      "root": {
        "name": "Pet 2",
        "lang": "Indo-European",
        "refs": "POK:824",
        "gloss": "to spread"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:824",
          "words": [
            {"translit": "pathana, perethu", "gloss": "wide", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:433",
          "words": [
            {"translit": "pahn", "gloss": "wide", "script": "پَهن ( پهنا ، پهنه )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:824",
          "words": [
            {"translit": "pandere", "gloss": "to spread out (walk)", "script": null},
            {"translit": "passus", "gloss": "step, pace", "script": null}
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
          "refs": "MON",
          "words": [
            {"translit": "pâssâge", "gloss": null, "script": "پاساژ"},
            {"translit": "pâsport", "gloss": "passport", "script": "پاسپورت"}
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
            {"translit": "pass, passage, passport, compass, pace", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:980",
          "words": [
            {"translit": "petalon", "gloss": "leaf", "script": null},
            {"translit": "patanĕ", "gloss": "platter, a wide plate or pot (pan)", "script": null}
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
            {"translit": "petal, pan", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Peu, Peue, Pu 1",
        "lang": "Indo-European",
        "refs": null,
        "gloss": "to purify"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:62",
          "words": [
            {"translit": "pâvaka", "gloss": "pure, clean", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "pâk", "gloss": "clean, pure", "script": "پاک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "pŭrus", "gloss": "clean", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "pure", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Peua",
        "redirect": "Pŭ 4"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Peud, Spheud",
        "lang": "Indo-European",
        "refs": "POK:998",
        "gloss": "to press, hasten"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Iranian",
          "refs": "FFD:44",
          "words": [
            {"translit": "paud, paud-a", "gloss": "to run", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FFD:44",
          "words": [
            {"translit": "pôy", "gloss": "to run", "script": null}
          ],
```


## [2026-09-14T00:53:01.966Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:53:02.024Z] TOOL RESULT

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


## [2026-09-14T00:53:42.887Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','MON','AHD','HRN','KLN','FFD','ISS','BRT','PHD','CHEUNG','WLD','IEC','SYN','SKT','LEW','LAT','ARY','HUB','NYB']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-14T00:53:43.869Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -40 && echo ---- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-385.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-09-14T00:53:44.163Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

CHEUNG null

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
```


### [2026-09-14T00:53:45.099Z] TOOL RESULT

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
----
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
   "w
```


## [2026-09-14T00:53:48.789Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint('---FFD---'); print(json.dumps(d['FFD'],ensure_ascii=False,indent=1))\n\""
}
```


## [2026-09-14T00:53:50.272Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; grep -n \"ausbreiten\" $f | head -20; done"
}
```


### [2026-09-14T00:53:50.383Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
---FFD---
{
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
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"
}
```


### [2026-09-14T00:53:51.428Z] TOOL RESULT

```
== POK_01.txt
2492:kann  mitgewirkt  haben. Mhd.  briisen  , brausen',  brüs  ,das  Brausen^  ndd.  brüsen,  ,brausen,  sieden; eihg    sein    (von    Menschen);    sich   ausbreiten,   neue   Triebe   machen   (von Pflanzen);   besprengen,  bespritzen'    (vgl.  nhd.  Brause)  (daraus   dän.  bruse
2569:got  ungatass  ,ungeregelt'  (ygl.ä-daazog),  mndl.  getes  ,sich fügend,  passend'; •ahd.  Zeiten  .(verteilend)  streuen,  ausbreiten',  nhd.  verzette(l)n,  wohl  auch
2572:anord.    teäja    ,Mist  ausbreiten',    tad:  n.  ,(*ausgebreiteter)   Mist';   ahd.  zot^^ zata  f.  , Zotte,  zusammen  herabhängende  Haare,  Fäden  oder  Wolle'  (davoi^"-* zaturra  ,scortum'),  ags.  toßttec  (expressives  tt)  , Fetzen,  Lumpen',  an.  tqtuti:0A ,Fetzen';  altdän.  tothae,  älter  dän.  und  dän.  mdartl.  tede,  taade  »verzögern '^^| hindern'.
2581:Endlich  mit  w-Vokalismüs:  norw.  dial.  tosa  , zerfasern,  zupfen^  auch  | , pfuschen,  langsam  arbeiten',  tose  .hinfällige  Person',  tos  , Fasern,  zerfa- sertes Tauwerk',  tossa  ,streuen,  ausbreiten',  mengl.  tötüsen  , zerzausen*, mnd.  tosen  , reißen,  zerren',  ahd.  zirzüsön  , zerzausen',  mhd.  züsach  , Ge- strüpp', züse  f.  , Gestrüpp,  Haarlocke'  u.  dgl.;  vielleicht  zu  lat.  dümus , Gestrüpp,  dicht  verwachsener  hoher  Strauch'  (*d^s-mo-s)  und  air.  doss jBusch^
2924:aisl.  iari-a  ,ausbreiten^,  ten-a  ds.
== POK_02.txt
== POK_03.txt
479:pelQ-,    plä-   , breit  und  flach,   ausbreiten;    durch    Druck   oder   Schlag  flach
720:I.  pet-,  pet-,  petQ-  ,ausbreiten',  bes.  die  Arme.
815:I.  plä-k-  :  plQ-k-,  ple-k-  :  plo-k-,  plei-k-  und  pelQ-g-  :  plä-g- :  plo-g  ,breit und  flach,  ausbreiten';  plok-s  , Platte';  Erweiterung  von  peh-  S.  805.
836:nlSt'  (p^^^')f  P^^^-f  P^öt-,  plQt-  ,hreit  und  flach;  ausbreiten',  Erweiterung zu    peld-:plä-    ds.,     s.    dort;    plet-io-j-iä    , Schulterbreite';    pleUos- ,Breite',P^ef3-i23ei2-, Breite';  pleto-no-  ,breit',  p/fs-no-  ds. ;p/fu-  , breit, pltd'Ui  ,die  Große,  Breite';  zum  Vokalverhältnis  vgl.  pläk-  :  piek-  ds. und  pläk-  :  piek-  :  pl^k-  , schlagen'. Arisch  "^pleth-:  ai.  prdthati  ^breitet  aus',  -te  , dehnt  sich  aus,  verbreitet sich',  pT^hd-  m.  ,flache   Hand',  prdthas-  n.  =  av.  frad-ah-   n.   , Breite',   ai. prthü-,    av.  pdi^d-iL-  ,weit,    breit,    geräumig',    fem.    ai.  pftUvi,   av.  pdrdOicl (auch   als  Subst.  , Oberfläche'),    daneben  von  *plt{h)dijL-:  prthivi    f.  ,Erde' (, Erdoberfläche')  =  gr.  IlXaraia,  gall.  GN  Litavl  f.,  gall.-lat.  Letavia,  leg. *Litavia,  ncymr.  Lhjdaw  ,die  Bretagne',  mir.  Letha  ds. ; arm.  lain  ,breit^  (*pletd-no-).
839:cymr.  lled,  com.  les,  bret.  let,  led  m.  , Breite'  (aus  dem  n,  ^pletos  =  ai. prdthas-),  cymr.  lledu,  bret.  ledaff  ,ausbreiten',  air.  lethaim  , dehne  aus, erweitere'  (wohl  auch  air.  leth  n.  , Seite'  usw.),  Kompar.  cymr.  lled ,breiter,  weiter'  (*plet-is),  air.  letha  , breiter',  Positiv  *plt,no-  in  air.  lethan, cymr.  llydan,  bret.  com.  ledan  , breit',  g2l\.  Litana  (^silva),  Litano-hriga-^ mir.  leithe  , Schulter'  [*pletiä)j  mir.  lethech  , Flunder';  air.  less,  cymr.  llys ,Burg'  {*plt-to-?)',
841:lit.  plötyti , ausbreiten',  plötas  , Platte',  plotis  ,Breite',  lett.  platzt,  plest,  dünn aufstreichen';  aksl.  *plasth  ,tortum',  russ. plast  , Schicht'  (Wurzelf.  *plät-); lit.  spleciü,  spUsti  ,breiten,  breitlegen'  (unsicher  wegen  des  anl.  s-,  das  in
1153:got.  raiÄ^  aisl.  re«r,  ags.  riht,  as.  ahd.  reÄ<  ,recht,  gerade'  (=  ar»- rasia-  usw.),  got.  ga-raihtjany  ahd.  WA^en  usw.  ,richten';  aisl.  rUtr^  Gen^; rUtar  ,das  Recht,  Gesetz,  Gericht'  (=  kelt.  *rehtu- ;  wgrm.  durch  das  n.^ des  Partiz.  ahd.  usw.  reU  ,Recht'  ersetzt) ;  got.  raJitön  ,darreichen' ;  Kauju got.  uf-rakjan  ,in  die  Höhe  recken,  ausstrecken',  ahd.  reccken  ,ausstrecken,^ erheben,  reichen,  verursachen,  sagen,  erklären',  nhd.  recken j  as.  rekkian , erzählen,  erklären',  ags.  reccan  (reahte)  ,ausstrecken,  leiten,  erklären,"^ rechnen',  aisl.  rekja  ^strecken,  ausbreiten,  erklären,  verkünden'  (z.  T, iteratives  *rakjan  unter  Verdrängung  von  *regö,  z.  T.  Denominativ);  aisL' rakna  , ausgestreckt  werden,  zur  Besinnung  kommen';
2169:lit.  skleidiiii,  sklelsti,  lett.  skliest  , ausbreiten,   umblättern',  lit.   sklaidaü,  -^
3186:ahd.  sprlzan,  spreiz  ,in  Stücke  splittern,  spritzen*,  aisl.  sprita  ,au*. einander  sperren'  (nach  Fischer,  Die  Lehnwörter  des  Awn.  40  aus  mhi spriten  entlehnt);  norw.  sprita  , spritzen';  mhd.  sprlten  und  (mit  gramm*. tischem  Wechsel)  sprlden  ,sich  ausbreiten,  sich  zerstreuen,  zersplittern* Kaus.  aschwed.  spreda  , zerstreuen,  ausbreiten',  norw.  spreida^  ags.  sprcida% ds.,  ahd.  spreitan,  mhd.  nhd.  spreiten]
3557:3.  stel-,  steig-  , ausbreiten,  flach  hinbreiten';  stlä-to-  , breit'.  /-    J
3750:aksl.  pro-sthrg  -strUi  (russ.  stereth)  ,ausbreiten',  prostram  (*storno-)  ^bltifi strana  , Seite,  Gegend',  russ.  storond  ds.;  aksl.  aruss.  usw.  s^ro^t)  ,Ordllttft|*, strojiti  ,paräre';  ^'  "
3758:trot.  straujan  .streuen',  norw.  streya,  aisl.  strä  ,streuen,  ausbreiten',  ags.
4365:, Spannung'  (*tntis);  über  ravv-  ,sich  ausbreitend'  s.  unter  tenu-m^m
```


## [2026-09-14T00:53:55.030Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '705,760p' POK_03.txt"
}
```


### [2026-09-14T00:53:55.070Z] TOOL RESULT

```
■persnä,  -sni-,  -sno-  , Ferse'.
Ai.  pärsni-  t,  av.  päSna-  n.  , Ferse';  gr.  rttegvi]  f.;  lat.  perna  f.  {^persnd) ,Hinterkeule,  Schweineschinken,  Schenkel,  Bein',  pernls  , schnell'  (mit  der Ferse);  got.  fairsna,  a.s.  f er sna,  ahd.fersana  , Ferse'  {*persna)j  Sigs.fiersin f.  ds.  (*persni-)]  hitt.  parsina  (leg.  parsna)  , Oberschenkel,  Lende',  par§- (a)näi-  ,hocken'  (auf  den  Oberschenkeln).
WP.  II  50  f.,  WH.  II  289  f.,  Pedersen  Hitt.  258.
pertb-  jStange,  Schößling'?
Arm.  ort""  (o-St.)  ,Weinstock,  Rebe';  gr.  TCtood-oq  m.  ,Schößling'  (vgl. -rtTÖlsfiog  :  rtöXefxog  usw.);  vielleicht  lat.  pertica  , Stange',  falls  nicht  aus per-ti-ca  zu  osk.  jpert  ,bis  zu'  aus  *jper-tij  also  ursprüngl.  ,Querholz';  vgl. cech.  jpHska  ds.,  S.  810.
WP.  II  49,  WH.  II  292  f.
I.  pes-  ,blasen,  wehen'  (s.  auch  2.  pes-  ,Staub,  Sand').
Aisl.  fQnn  f.  ,Schneewehe,  Schneehaufe'  (*faznö),  -fenni  n.  ds. ;  als  ,im  Win- de wehender  Faden':  ah d. /aso  m.,fasa  f.  ^Faser,  Franse,  Saum',  sgs.fces(ri) n.  ,Franse',  engl,  feaze  ,Fasern';  aisl.  fqsull  m.  ,B^iid',  mnd.  vese{n),  Spreu, Faser,  Franse',  ndl.  vezel  ,Faden',  ahd.  fesa  ,Spreu,  Spelze',  nhd.  Fehse, dän.  ßcBser^  älter  f{j)es  ,Fasern',  ahd.  fasön  ^untersuchen'  (*zerfasern) ;
824
aksl.  'p^chyrh  ,bulla,  Blase',  'pachati  ,ventilare,  agitare',  russ.  pacÄnui^,  ^' ,wehen',  pdchnuh  ,duften,  riechenS  zapacA^  , Geruch,  Duft' usw. ;  russ.  pds,no  - ,Garnsträhne',  lett.  pudsm(i)s  ,Abteilung  zwischen  zwei  Endpunkten',  .soviel'" man  mit  zwei  Fingern  aus  der  Kunkel  Flachs  zieht';  6ech.-poln.  pochvQ  , ,Schwanz'  (, wedelnd'),  aksl.  o-pash  ds. ;  nasaliert  poln.  p^chnqc  ,anblasen,  J anwehen',  pqcJi,  p^ch  ,Witterung  (des  Hundes')  usw. ;  vielleicht  bulg.  "f; pasmina  ,Rasse'  (vgl.  ai.  tdntu-  ,Faden,  Faser,  Geschlechtsfaden,  Reih, der  Nachkommen,  Nachkommenschaft').
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
Ai.  pdtati  ^fliegt,  wirft  sich,  fällt^  (=  7t€T0j.iaL,  lat.  petö^  acymr.  liedant), Aor.  apaptat'j  petd-  in  Fut.  patisyati,  Supin.  pdtitum^  Partiz.  patitd-)] patdyati  , fliegt^  (=  gr.  7tOTaoi,Lai),  pätdyati  ,läßt  fliegen,  schleudert,  läßt fallen^  (dehnstufig  wie  päta-  m.  ;Flug,  Fall,  Sturz^,  gr.  noiiaoixai  ,flattre^), pra-pat-  , hineilen,  stürzen',  pdtman-  n.  ,Flug,  Pfad,  Bahn^  (:  Tc6Tt.iog^  nora- l^ög)',  av.  pataiti  ,fliegt,  eilt^,  ap.  ud-apatatä  ,erhob  sich^,  av.  patayeiti ,fliegt^,  acapastöis  Inf.  ,hinahzufallen^,  paitipasti-  f.  ,Entgegengehen,  -treten' (vgl.  ai.  ati-patti-  , Zeitablauf'),  von  einem  u-Präs.  parapad-ivant-  ,fortflie- gend  (vom  Pfeil)';  av.  täta-  (*ptätd-),  , fallend  (vom  Regen':  gr.  nrißzog  ds.);
arm.  t'^fcim  ,ich  fliege'  (*pter-i-sko).
gr.  hom.  nstoy,ai  ,fliege'  {iftrö(.irjv) ;  sonst  auch  Trsraf-iaij  emaTO  ,entflog', fcräg,  8ftTr]v,  dor.  ercxav,  Fut.  TtrrjaofxaL]  djyiVTtsrrjg  , schnell  fliegend',  nsrsvjvög, (*7TSTsaav6g)j  TtsTStvög  {^7T.8TBav6g)  ,geflügelj;,  ^üg^Q^,  Ttoir]  ,Flug',  rtOTävög, -Tjvög  ,zum  Fliegen  befähigt,  beflügelt,  fliegend',  noTdo^aL  (und  Ttorso^ai^ s.  oben)  ,flattre',  TtcjrdofxaL  ds.,  rcTTJaig,  bei  Suidas  irvrjfxa  ,Flug',  mrivog, dor.  TitGvög  ,fliegend^;
Stamm  TtEta-,  rtrd-  ,fliegen',  aber  Tters-,  tttj;-,  jttw-  mit  der  Bed. ,fallen' :  nt-TtTo)  (für  *7it-TtTü)  nach  qtrtxü))  , falle' ;  Perf.  TTfWwxcr,  Partiz. TtsrtTTjdyg,  att.  fCBTCxwg  aus  *jte7n;'öi(bg]  äTirvog  (Pind.),  dnir^g  (dor.  inschr.) ,nicht  fallend,  nicht  dem  Falle  ausgesetzt';  TiiTvia  ,falle',  sij-fcsrrjg  ,bequem, günstig',  TtQO-fiETrjg  ,vorwärts  fallend,  geneigt'  (:  ai.  pra-pat-),  Treaog  n. (Gen.  naasog  aus  *n€Teog)  ,cadaver',  nÖTfiog  ,Los,  Schicksal,  bes.  trauriges', noraf-iög  ,Fluß',  eig.  ,Wassersturz';  Ttröiia,  TtrcoaLg  ,Fall'  (:  yrfWwxa); fcrcjüTÖg  jfallend';
mit  der  Bed.-färbung  des  lat.  petere:  gr.  rtirvXog  ,heftige  Bewegung' (:  lat.  petulans]  vgl.  auch  if^Ttsaetv  ,impetum  facere');
endlich  hat  Ttzä-  :  tvtco-  :  rtra-  auch  die  wohl  aus  ,niederstürzen'  entw. Bed.  ,sich  niederducken'  und  , verzagt,  in  Furcht  sein':  y.aTa-TCTrjxriv  ,(die Pferde)  scheuten',  TtsnTrjcog  , geduckt',  TtTola  ,Scheu,  Schrecken'  {^ntcjJ^iöt, vgl.  Arjxd)  Utcba,  *Atc61Xo)v  Rxthog),  TCXo{C)eXv  ,erschrecken,  in  Bestürzung versetzen',  Pass.  ,von  Schrecken  ergriffen  werden';  mit  gutt.  Erw.  mr^GGia (*7rräx-jia))  ,ducke  mich'  (Aor.  zitxr^^a,  dor.  znxa'Aa  auch  trans. , erschrecken'; xaTa-7tTäyid)v),  TiTcoG-Kd^ct)  , ducke  mich  furchtsam,  fliehe',  tztwgglü  (*/rTa>x-
826
(Txtcü)    ds.;    Trrwg;   -xog  ,scheu,   flüchtig^   (m.   .HaseQ,    ablaut.   nzd^   m.  j^ , Feigling';    Gen.  tttöxos;  7tvoj%6g   ^Bettler';  zu  letzteren,   wie  es   scheint "^ auch  arm.  t'aJcöim,  t'ak'eay  ^sich  verbergen';
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
Ai.  Trans,  'punäti,  Med.  pdvate  , reinigt,  läutert  (sichy,  pdvitum]  pavltdr-, pQtar-  m.  ^Reiniger,  Lauterer^,  pavitram  , Läuterungsmittel,  Seihe,  Sieb^: pävana-  , reinigend^,  pävakd-  (auch  paväkd-)  ,lauter^  =  mpers.  pavag^  np. päk  ,lauter,  rein^;  ai.  pütd-  ,rein^,  püti-  f.  ^Reinigung';  ay.  pUitika-  ,zur Läuterung  dienend^;
lat.  pürus  ,rein^  (Bildung  wie  clä-ru-s),  pürgöj  älter  pürigöy  -äre  ,reini- o-en*^;  pätus  ,rein^,  nepus  ,non  pürus'  (*nepüt-s)',  putäre  ,reinigen,  putzen^; mir.  ür  ,neu,  frisch,  edeF,  cymr.  ir  ,frisch,  grün%-  ahä.  foioeUj  m.h.d.  voewen sieben,  Getreide  reinigen^  {*fawjan  =  ai.  pavdyati  , reinigt,  läutert^) ;
unsicher  gr.  tztvov,  rcreöv  ^Wurfschaufel'  (:  ahd.  fowen?).
WP.  II  13,  WH.  II  390  f.
2.  peu-  ,erforschen,  begreifen,  verständig  sein^.
Gr.  vj-Tttog  (*v'r]-7tJ^-Log)  und  vrj-Ttv-TLog  ,unverständig,  kindisch',  TtivvTÖg ,klug',  7CLvv(.i€VT]v '  Gvvexriv  Hes.  (auf  Grund  eines  Präs.  *ni-vv-iii  aus  *7tv- rCfXL)',  lat.  putäre  , rechnen,  berechnen,  vermuten,  meinen*;  aksl.  is-py-U ^perscrutatio^,  pytajg,  -ati  ,scrutäri,  quaerere^
WP.  II  13 f.;  anders  Schwyzer  Gr.  Gr.  1,  6962.
```


## [2026-09-14T00:54:11.930Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK speud ===\" && grep -n \"speud\" POK_03.txt | head -10"
}
```


### [2026-09-14T00:54:11.971Z] TOOL RESULT

```
=== POK speud ===
```


## [2026-09-14T00:54:12.880Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN pak ===\" && grep -n -i \"pâk\\|pak\\b\" HRN.txt | head -30"
}
```


### [2026-09-14T00:54:12.926Z] TOOL RESULT

```
=== HRN pak ===
463:ywpÄ:, ydpak, minj. ydoya; yidg. t/ow?;\
1695:phlv. papak (vergl. Nöldeke, Kärnämak, 35 Note 3;
2653:ai. vidhdvä' *Wittwe'; phlv. vepak d. i. vBvak; lat.
2737:ai. pavakd- 'rein, klar ; phlv. pak, päkih,
3495:tapak 'Esse' (phlv. täpak, ar. fabaq),
5301:phlv. depäk {S«äy. näsäy. 4, i), arm. LW. dipak, syr.
6030:kurd. zive^ arm. ztpak 'Quecksilber*.- 152 —
6732:phlv. sap, saw(ik\ vergl. Sapak, N. pr. (Hörn, Mit-
7021:aw. /svaewa- ^schnell, schnellend'; pblv. sepak d. i.
7319:in der Stammsilbe {kebk aus *kapak) sind sie aber
7611:AUg. entlehnt; echt bei. köpak, n. ßöfay (211)
9991:kürde 'hinlegen', po kurde (pak kerden), fuknrde^
10383:^) Vd. 2 (S2) wird aw. Ortivi' durch dripak wiedergegeben.
16967:Supak 775.
22196:dipak 591.
22461:fapak 372.
```


## [2026-09-14T00:54:16.756Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2725,2745p' HRN.txt && echo \"=== leaf ===\" && python3 - <<'EOF'\np=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt',encoding='utf8',errors='replace').read()\nimport re\n# find line 2737 char offset\nlines=p.split('\\n')\noff=sum(len(l)+1 for l in lines[:2736])\nleaf=p[:off].count('\\f')\nprint('leaf',leaf,'printed page',leaf-21)\nEOF"
}
```


### [2026-09-14T00:54:18.032Z] TOOL RESULT

```
aw. ^paitisahva- [paiti + [/'safih- hat zwar im Awesta
nur die Bedeutung 'beschwören') ; phlv. pasu/ ; arm.
patas/ani 'Antwort*.
276. päSne 'Ferse'.
aw. päsna- 'Ferse'; phlv. päsnak*^ ai. pdrsni-,
kurd. päsüne, päm, päme (ZDMG. 38, 55), päm (JJ.);
af/. pünda ; bei. pünzig, ptnz, n. pTz, pid (306) ; wa/.
päsna, sar. pu/nä 'Ferse'.
syr. LW. j^li/^B 'der Bimstein, mit welchem man
sich im Bade die Fersen reibt', de Lagarde, Ges.
Abh. 73.
277. päk 'rein', paktze,
ai. pavakd- 'rein, klar ; phlv. pak, päkih,
278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
paiti + alüden (s. älüden^ No. 42) ; phlv. pälüt (Bund.),
päz. pälJdan, pälaidan (West, Sik. gum.-Gl.).
bei. LW. palayag^ pälenay 'seihen, worfeln, reinigen'
(292).
^j Vergl. Geldner, Studien I, 16. Bartholomae (briefliche
Mitteilung) verweist mich aber auf aw. parendi- (Indog. Forsch. I, 184)
mit der Grundbedeutung 'Füllser.— 63 —
=== leaf ===
leaf 83 printed page 62
```


## [2026-09-14T00:54:18.317Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK 998 area ===\" && grep -n \"^998$\\|^997$\\|^999$\" POK_03.txt | head && grep -n \"sich in Bewegung setzen\\|sputen\" POK_03.txt | head"
}
```


### [2026-09-14T00:54:20.565Z] TOOL RESULT

```
=== POK 998 area ===
3229:997
3257:999
3023:ags.  spöwan  , gedeihen,  glücken',  ahd.  spuon  ,gelingen*,  germ.  "^spödi- im  ahd.  spuot,  as.  spöd,  ags.  sped  ,Gedeihen,  Beschleunigung,  Eile',  nhd. sich  sputen]  ahd.  usw.  spar  s.  unten;
```


## [2026-09-14T00:54:26.915Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3229,3258p' POK_03.txt"
}
```


### [2026-09-14T00:54:26.959Z] TOOL RESULT

```
997
Ljje  r  unklarer   Geschichte:   ahd.   spehhan,  ags.   specan  , sprechen',  spcec [iedeS    engl,    to   speak,   speech,    mhd.    späht   , Geschwätz,   lauter    Gesang',
^jpehhen  , schwätzen') ;   in   allgemeinerer   Schallbed.   aisl.   spraJca   ^prasseln'
(^raJci  ^Gerücht'),  dän.  sprage  ,k rächen,  knistern'.
Q,  In  anderen  Bedeutungen :
ai.  sphürjati  , bricht  hervor,  kommt  zum  Vorschein'  (s.  oben) ;  parägas {Blütenstaub';
av.  spardga-  , Sproß'  (,von  den  Widerhaken  unterhalb  der  Pfeilspitze'), fraspardya-  , Schößling,  Zweig';
o-r.  acpaQaysofxai  , strotzend  voll  sein,  von  Eutern',  anagyao)  , strotzen (von  Saft,  Milch),  von  Begierde,  Leidenschaft  geschwellt  sein',  aTcagyal' dqya'i''  ^Q^cci  Hes.,  GrtOQyai'  iged-ia^ol  sig  rö  rsy,eh'  Hes.,  daTtdgayogj  äacpä- qayog  Junger  Trieb;  Spargel';
lat.  sparg��,  -ere  ,streuen,  hinstreuen,  sprengen,  spritzen' ;
mnd.  sparJcen  , Funken  sprühen,  funkeln',  ags.  spearcian  ds.  (engl,  sparhle), fpircan  ,Funken  sprühen,  spritzen',  mnd.  sjparke,  ags.  spearca  (engl,  spark) , Funke',  nasaliert  mnd.  spranken  ,funkeln',  mnl.  spranke  ,Funke,  das  Aus- sprUhen,  kleiner  Fleck';
aisl.  sparkr  , lebhaft,  rührig',  aisl.  spr^kr,  norw.  sprWk,  schwed.  dial. spräker  ,lebhaft',  auch  ,strahlend,  glänzend',  dän.  dial.  sprceg  ,hochmütig, prahlend'  {*spregi-) ;  engl,  sprinkle  ,sprengen,  besprengen,  sprühen',  schwed. dial.  spräkkel  , Fleck'  (,*Spritzer'),  spräckla  ,die  Masern',  norw.  und  nisl. sprekla,  mhd.  spreckel  ,(Haut)-fleck',  nasal,  mhd.  sprinkelj  sprenkel , Sprenkel , Fleck';  r-lose  Formen  sind  mnd.  spinkel  =  sprinkel,  mnl.  spekelen  ,be- sprengen',  nl.  spikkel  ,Fleck,  Sprenkel',  ags.  specca  ds.,  lit.  spüogas  ,Fleck, Punkt';  —  ohne  anl.  s,  und  gleichzeitig  als  Variante  neben  '^perk-^  "^prek- ,gesprenkelt'  (S.  820 f.):  dXsl.  freknöttr  ,sommersprossig',  norw.  und  nisl. frekna  , Sommersprosse',  engl,  freak  , gestreift  machen';
ags.  sprcBc  n.  , Sproß,  Zweig',  spranca  m.  ds.  (sprincel  ,basket-snare') ; u  auf  der  •  Bed.  ,prasseln,  knistern,  bersten'  beruht  norw.  sprek  , dürres Reisig',  aisl.  sprek  , morsches  Holz',  ahd.  sprahhula  , Splitter,  Spreu',  mnd. sprok,  sprokkel  ,Reisig' ;  hoU.  spi^okkig  , spröde',  sprokkeln  , bersten',  norw. dial.  sproka,  sprokka  ,Sprung,  Spalt',  3igs.  forspiercan  ,trocknen,  dörren'; mnl.  sporkel , Februar'  (wohl  vom  Knospensprießen,  vgl.  engl,  spring  , Früh- ling'), nd.  sprickel  , Reisig,  trockener  Zweig';
vgl.  auch  ags.  spracen  ,Erle',  norw.  sprake  ,Wacholder',  ahd.  sporah, tpurcha  ds.,  auch  (,zuckend,  schnellend,  elastisch')  ahd.  houue-spranca »locusta  (Heuhüpfer)',  as.  sprinco  ds.,  mnd.  spranke,  sprinke,  sprenkel  ds. ; mhd.  sprinke  ,YogeUaRe^,  nd.  nhd.  Sprenkel  ds.;  ud.  sprenkel  , Klemmholz';
ahd.  springa  ,pedica*,  älter  nhd.  Sprengel  ,  Vogelfalle',  engl,  springe, ^ringle  , Vogelschlinge'  sind  von  springen  beeinflußt;
998  •
lett.  spifgt  ,frisch  werden,  erstarken',  spirg(t)s  , frisch,  munter, spirgsti   (pirgsti)    ,glühende   Kohlen   unter   der  Asche';   spirguUs  ,Sp] (,* Weggespritztes');  spridzinät  ,umherspritzen,  schnellen',  spridzigg  , munter^-    spufguls    ,kleines,   munteres   Kind',   spergans    ,spröde,   mm lit.  sprogis,  lett.  spradzis  , Erdfloh';
D.  ohne  anlaut.  s-  vgl.  noch:  ai.  parjdnya-  ,Regenwolke  (spritzend, sprengend);  der  Regen-  und  Gewittergott'  (s.  oben  S.  819,  823);  airj , Tropfen',  mcjmr.  eiry,  cymr.  eira  , Schnee*,  acorn.  irch,  ncorn.  er^ erch   ds.   (*pargo-,  *pargio-)]   wohl   auch   aksl.  prbga   ,neuer   Kornj des  Weizens',  russ.  pergd  ^Blütenstaub'  u.   dgl.;   aksl.   is-prbgngti  ^ springen',   poln.    pierzgnqc  , bersten,   aufspringen   (Haut)';    nas.    abg.f pr^gnqti  ,hervorsprießen',  prqg^  »Heuschrecke' ;  als  »schnellend'  aksl. jtendicula,  Sprenkel',  russ.  prüga,  pruzina  , Springfeder',  u-prügij  ,eb schnellend,  prall'^  auch  die  Sippe  urslav.  *pregg  , spanne,  spanne  an*, jjoch*,  poln.  poprag  ,Gurt'  usw.
WP.  n  672 ff.,  WH.  II  566  f.,  Trautmann  276  f.,  278  f.,  Yasmer  2, 337^
spergb-,  spregh-,  nas.  sprengb-  ,sich  hastig  bewegen,  eilen,  springva*, Er  weit,  von  sper-  , zucken,  schnellen'.  ••-
Ai.  sprhdyati  ,begehrt,  empfindet  Neid',  av.  ä-spdrdzatä  ,war  bestreb^^
gr.  üTteQxoy.ai  ,einherstürmen,  eilen  (artegxoi.isvog  , eilig,  hastig,  rasek^ ungestüm,  aufgebracht  sein',  OTtegxf^  , dränge,  treibe',  anegxvdg  ,schnä, hastig',  dansQxeg  Adv. , heftig,  leidenschaftlich';  hierher  cymr.Jfraeth  (S.996);
aisl.  springa  ,springen,  hervorbrechen',  ags.  as.  ahd.  springan  ds.  |  K&oi. ahd.  sprengen  ,springen' machen  (ein  Pferd),  (zer) sprengen'  und  ,streueil^ spritzen,  sprenkeln',  aisl.  sprengja  »sprengen',  ags.  sprengan  jausbreitttSj bersten;  sprengen,  säen';  mhd.  sprinc  (-g-)  , Sprung,  Quelle',  ags.  spring , Wasserquell',  engl,  spring  ,ds.,  Sprungfeder,  Knospenspringen,  Frühling'; alte  Ablautform  *sprögh-  in  aisl.  spröga  , springen,  rennen'.
WP.  II  675,  Trautmann  278  f.
(s)p(h)eu-d-  , drücken,  mit  Nachdruck  betreiben,  eilen'.
Npers.  poy  ,Eile'  (iran.  *pauda-),  parth.  pwd  ,Lauf';
gr.  anevöü)  , spute  mich,  eile;  bin  emsig,  strebe,  strenge  mich  an';  tränt, »treibe  an,  beschleunige'  (ursprüngl.  , dränge,  drücke',  wie  in  ajtovSci ,Mörserkeule',  d.  i.  , Zerdrücke^  Hes.);  Gn:ovdrj  f.  ,Eile,  Eifer,  Bestrebung*, GTtovdalog  ,eilig,  eifrig,  fleißig',  aftovöd^o)  , spute  mich,  betreibe  mit  Eifaf*j
vielleicht  alb.  pune  »Arbeit,  Geschäft'  {*pudnä)'j  ^
falls  ^-Erweiterung  einer  Wurzel  speu- :  speu- :  sp^-,  eventuell  zu  ai.  sphä- vayati  »mästet,  verstärkt',  ags.  spöwan  ,gedeihen'  (anders  oben  unter  2. spei-);  vgl.  auch  gr.  iag)vöo)f.ihog  »vollgestopft  mit  Essen',  og)vda)v'  ^X^^^
999
ötl'TjQ'^^  Hes.,  ÖLaocpvduioai '  av^fjffai  Hes. ;  unsicher  gr.  Gcpvt^o)  (Fut.  oq)v^a)) gucke,  bewege  mich  heftig,  fiebere,  strebe  eifrig',  acpvy!.i6g  m.,  ocpv^ig  f. Zuckung,  Puls',  äa(pvy.T6a}  ,bin  ohne  Pulsschlag'  {*^P^'^9-)',
```


## [2026-09-14T00:54:35.495Z] TOOL CALL #15: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['BQT'].get('page_offset')); print('---'); print(d['MON'].get('page_offset')); print('---'); print(d['ISS'].get('page_offset'), d['ISS'].get('lookup_hint'))\n\""
}
```


### [2026-09-14T00:54:36.520Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
---
None
---
DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.
```


## [2026-09-14T00:54:37.507Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n \"pôy\\|poy\\|pūy\\|puy\\|pūdan\\|paud\" FFD_pages_faseng.txt | head -20; echo \"=== fas ===\"; grep -n \"پوی\" FFD_pages.txt | head -20"
}
```


### [2026-09-14T00:54:37.598Z] TOOL RESULT

```
ugrep: warning: FFD_pages_faseng.txt: No such file or directory
=== fas ===
1242:پوییدن
1243:پویید مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
1244:پوی + فارسی میانه 00 < ایرانی باستان 0200-2*. برای 2 > آرای. ريشهٌ 0200
```


## [2026-09-14T00:54:42.407Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && ls && python3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:1241])\nleaf=t[:off].count('\\f')\nprint('leaf(0-based)',leaf,'pdf page',leaf+1,'printed',leaf+1-5)\nblocks=t.split('\\f')\nprint(blocks[leaf][:2500])\nEOF"
}
```


### [2026-09-14T00:54:43.662Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
leaf(0-based) 48 pdf page 49 printed 44
[pdf page 49]
با فعلهای فارسی دری
است» از ایرانی باستان ۳۳-۱۵*. برای 1۵ -> آراست. 8 که صورت ضیف 34108
است» صورت اصلی 007 است» 8 پیش از ۲ به # بدل شده است. 3208 و 002 به معتی
: «نجات دادن» هستند. پوزش فارسی دری بازماندهٌ 88215 فارسی میانه است که هم
«نجات‌دادن) و هم «عذرخواهی‌کردن» معنی می‌دهد. «پوزیدن» به معنی «عذرآوردن و
معذرت خواستن» است.
پوسیدن
(پوسید» مادهٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است.
پوس < ایرانی باستان 0۷8۵*. برای 2 > آرای. 8 برای ساختن ماد آغازی از ريشه
به‌کار می‌رفته است. 0۷ صورت ضعیف ريشةٌ 080 است. ريشهٌ 020 «پوسیدن» معنی
می‌دهد. «پوده» به معنی «پوسیده» از ريشهٌ 020 گرفته شده است. به شرح زیر:
< فارسی میانه 08028 < ایرانی باستان 0-12-12*. برای 1۵ > آراست. 12 پسوند و
صورتی دیگر از 00 است.
بوشیدن ۱
پوشید < فارسی میانه 006810.
پوش ج فارسی میانه 005.
پوییدن
پویید مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
پوی + فارسی میانه 00 < ایرانی باستان 0200-2*. برای 2 > آرای. ريشهٌ 0200
به‌معنی «دوبدن) است. (5 هم در فارسی میانه (دویدن)» معنی می‌دهد.
پیراستن
پیراست < فارسی میانه 0217351 و ۷۲391 0817381 د. ایرانی باستان -21-739م*
است و ۷۱391 ۷۷1-139-18*. برای 18 + آراست. 1 و 2211 هر دو پیشوتد فعلی هستند.
```


## [2026-09-14T00:54:56.111Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf8',errors='replace').read()\nblocks=t.split('\\f')\nprint(len(blocks))\nimport re\nfor i,b in enumerate(blocks):\n    if 640 <= i <= 680 and ('پهن' in b):\n        head=b.split('\\n')[0]\n        print(i, head, 'count', b.count('پهن'))\nEOF"
}
```


## [2026-09-14T00:54:57.244Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"== $f\"; grep -c \"\" $f; grep -n \"پوییدن\\|پویه\\|تکاپو\" $f | head -10; done"
}
```


### [2026-09-14T00:54:57.288Z] TOOL RESULT

```
777
659 ی count 2
679 وجام و شیلةٌ آلوان کنند وگاهی خالی گذارند . count 1
```


### [2026-09-14T00:54:58.345Z] TOOL RESULT

```
== MON_part1.txt
99339
32972:پو: ۲5 [- پوی» ری. پوییدن] (.) رفتار وسط 
33573:پویا: ۲۳۷-5 (ص‌فا. پوییدن) رونده. دونده. 
33574:پویان: «-00۷ (ص‌فا. حا. پوییدن) روان. 
33578:پوییدن] (مص‌م.) (پویانید» پویاند» خواهد 
42789:تکاپو(ری): (۵۱--۱۵۳ (امر.) رفت و 
55357:(.) نوعی دویدن» پویه. 
== MON_part2.txt
94500
40145:مزجات» سرمایه قلبل. تکاپوی آمد و شد با 
89873:رفتاری میان دویدن و رفتن» پویه. با یکك
```


## [2026-09-14T00:55:00.694Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '32965,32985p' MON_part1.txt && echo \"=== 2 ===\" && sed -n '33570,33590p' MON_part1.txt"
}
```


### [2026-09-14T00:55:00.763Z] TOOL RESULT

```
بنیرک: -0201۲ (امر .) (کیا.) گیاهی از 
تیرة بنی رکیان که پابا است و ارتفاعش ۳۰ تا 
۰ سانه نتبمتر و دارای ک رک‌های دراز است 
که به حالت خودرو در جنگل‌ها و اراضی 
غیر مزروع روییده می‌شود. 

پو: ۲5 [- پوی» ری. پوییدن] (.) رفتار وسط 
که نه تند باشد و نه کند» پوبه. دو. 

پوپ: 05۲ (.) تاجی از پر که بر سر بعضی 
از طبور دیده می‌شود؛ کا کل مرغ. (جاد.) 
پوپش. 

پوپش: کد-ع5م [- پوپه - پوپکك - پوپو - 
بویوء کر ] (اصت.) (جاد.) هدهد» شانه‌سر. 
بویک: ۷ [- بویش ] (.) (جان.) هدهد» 
شانه‌سر. دختر یک دوشیز ه. 

پوت: :05 جگر گوسفند. خوراک قلیه که 
از بوت سازند قلیه پوتی 
=== 2 ===
(افا.) در بعضی ترکیبات بجای ,پوینده» آید. 
صح.- در «سکگ پوی» و «گ رک بوی» به 
)۲۳ 
پویا: ۲۳۷-5 (ص‌فا. پوییدن) رونده. دونده. 
پویان: «-00۷ (ص‌فا. حا. پوییدن) روان. 
دوان. 

پویانیدن: ۲۷ [- بوباندن؛ 6 
پوییدن] (مص‌م.) (پویانید» پویاند» خواهد 
پویانید» بپویان» پویاننده» پویانیده) به راه 
بردن (ستور و غیره). 

پسویه: (6-)-۲ (اسص.) (.) رفتاری 
متوسط» رفتن نه به شتاب و نه نرم. 
پوییدد. 0۷-7 (مص‌ل.) (بو بد» یو بده 
خواهد پویبد» بیوی» پوننده» بویا» پویان» 
پوییده) رفتن (نه به شتاب و نه نرم). 

به. (صت.) کلمة تعجب و تحسین؛ خوشا! 
به: : ۵20 (اصت.) آوایی که از دهان بر آرند با 
دم زدن.
```


## [2026-09-14T00:55:02.194Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf8',errors='replace').read()\nblocks=t.split('\\f')\nfor i in (658,659,660):\n    b=blocks[i]\n    print('=== leaf',i,'===')\n    print(b[:1800])\nEOF"
}
```


### [2026-09-14T00:55:03.309Z] TOOL RESULT

```
=== leaf 658 ===
است که کنابه از برابری کردن در عال و فدر
وهر تب باشد.
هلو از دن» کنابه از گربختن ودو
برنافتن- وترلك دادن و اجتناب نمودن و احتراژ
کردن باشد .
بهلو کند ‌ بعنی بهلز نهی کندو کناره
گر ند «دوری نماد ویگریزد ِ
پهلو نهادن م کنایه از خواییدن
پهلوانی- وشهری- وزبان شهری باشد» ومنسوب
به‌پهلوان وزبان فارسی هم 2
بهله بفتح اول وثاك وسکون ثانی ؛
ولات اصقهان وری ودینور باشد ۴ .
پهمز له بازای هوز بروزن احمدك »
خار یشت بز رکب تبر انداز را کویند کد سخول
باشد ,
هن « شح اول و انی بر وزن دهن »
شریکه پسب مهرباتی‌دریستان مادر طفیا نکند.
و بسکون ثانی ممروف است که پشت و پخش
وعریض باشد ۴ . #
باشد .
بهلوی ۲ » بر وزن منئوی ؛ بمعنی
: مر.کب از: پپاو (ء .م) 4 نی ( مسوند قبت ) ؛ معنی تسین آن بارتی است‎ - ٩
سپس بعهنی زبان معمول درعود پارتیان و مدها زبان‌عهد ساساتیان | رف : حقدمهٌ آفای پور داود‎
بو ۲ ۶۳ بر کاب حاشر یمعنی . خروی و سلطنتی 4 امروزه بهلوی‎
بزبانی ابرانی که اصطلاحاً پارسی مباندمینامند اطلاق‌مبشود و آن‌را بردوقمم تقیم کرده‌اند: پهلوی‎
شمالی باپپلوی اشکانی (باصطلاح بر خی‌بارتی) .بهلوی‌جنوبی اپپلوی ساسانی(باصطلاح بعضی‌پارسيك).‎
تاه مایت ۱3 و ۱۲ 77 ۱
اعلیحضرت فقیدرضاشاه
بهاوی » می ازاحمدشاء
( آخر. من دادشاه‌قاجار ۸
در آذر ماء ۱۳۰6
بسلطت ابران سید
و در شهرمور ۱۳۲۴از
سلطئت صتعفی شد
و زمام آمور دا بفرزند
ارشه خود اعلیطرت
محمد رضا شاء دهلوی.
بادشاه کنونی ابران
تفوحض کرد. رك:
یر تقد رعلی شاد
بلدان: اصفهان والری
و همدان و ماه ئهاو ند رت ۱
و آذدبیجان * مفاتیب جدول الفبای پهاوی (ثامل الفبای کنیبه‌ها والفبای نسخ خطی!ا
بیه در سفتته 1۳۳ (بر ها قاطع ات
=== leaf 659 ===
ی
بهنا 4 بروزن مستانه , نوعی‌از میمون
باشد- وکلیچةٌ روغنی را لبز گود .
هنال بروزن کمند. دامی باشدکه‌بدان
آهو گیر ند.
(م ی و - بروزن فدفور » چیزیست مانند
دستنبوی که بزبان عرب آن را حنظل خوانند
وقنامالنمام(۱) همان‌است- ویمعنی بهی‌نیز هست
که خرزحره باشد .
44 س ختح ارل وثانی و تالث . بمعتی
بهن‌است» و آن شیری باشد که سیب مهربانی
بیار دریستان مادر طفیان کند - وبسکون ثانی
چوکان بازی و کوی بازی باشد - و نوعی از
سازند و گوی را در آن نهاده بر خوا اندازند
وچون تزديك بزمین رسد باز بهمان پهنه‌میز نند
[۴ نگذارد که برزهن آید ی تمفصل رسانند ۰
وآن‌را جربی طبطا بکوبند- و پهنی ران آذمی
و حیوانات دیگر باشد از جاب درون و آن را
بربی قطن خوانند - و بمعنی میدان هم آمده
خوانند وچوبی باشد مخروطی تراشیده که‌اطفال
رسمانی برآن پیچند و نوعی برزمین اندازند که
تادیرباز بگردد ۱ .
ی « بنتح اول بر وزن سهی ۰ حنظل
باشد و آنراخریز؛ تلخ‌هم هت و خرزهرمرا
چوکان را نیز گوشد که سر آنرا مانشدکفه یز پهی خوانند ؟ .
بیان بیست ویکم
ی ه بنثح اول و سکون الی » ممروف
است» و آن چیزی‌باشد که بر کمان وزین اسپ
وب تیرجایی که پیکان درآ نکنندیبند. وجربی
عصب کویند. و مضفف پای است که بمربی رجل
خوانشد ۴ - و نشان بای باشد که نقش‌فدم‌است ۴
ودئبال و پس وعقب. و تعافب. و قصد و اراده -
ونشان - و پی‌بردن بعنی نشان یافتن - و بمعنی
برای و بهر بیز حست چنانکه گوبند * از پی
فلان کار» بعنی از برای فلان کار واز بهر فلان
چیز - و بمعتی بار و مرنبه هم آمده است مثل
آنکه گونند فچند پی» مراد آن باشد که چند
مرتبه وچند پار- وتلب و طافت را نیز کفته‌اند -
؟ - باين معتی در اسطلاح علمی
۴ . رك: ا.
بقیه از صفحة 4۳۲
مشق ۰۳۶۹
۴ - پهلوی 09220 2 اونوالا 6 ۸
=== leaf 660 ===
یاب
وبکر او عخفف یه بات دکه درچراغ سوزند
- وشمم تیز سلزند ۷ -
یمیت بروزن سراب. بمعنی پاباباست
که ین‌حوض وته جربا باشد وبعربی قمع رکوبند -
وتهات عرچیز را تز کفتهاعد - و بمعنی تاب
لبادم بر وزن زباده . هعروف است
که قض سواره باشد ۴ - ونام مکی‌از مپرهای
شطرنح عم حست - و نم کلی است ممروف -
از عردم یی سواد باشد یمنی علم و فنلی کسب
تکروه بلشد .
یباده نهادن-کنابه از زبون داتن
وعلجز اتکلشتن باشد . 9۶
ار دشتی- بکسر .اول و زای هوز ۰
دوآنی است که *ن را جربی صل‌الفار خوانند .
کوبنه اکر حوش بخورد میمیرد , و از خواص
او اتت که اک رک رکه بای بربر که آن ,گذارد
حمین که مزدارد لنگه شده باشد وگن سای
توقف کند الیته بفتد وبمیرد .
هیا لش یا کاف . تسیر پیاز است -
مه
وکیاهی را لیز کون دکه ازآن بوربا بافند -
و نوعی از کرز باشدکه سر. آن را با زنجیر
چو کن خوانند ۴ - ونام قربه‌ایت دردامن کوه
معدن لمل ۵ .
یا کیی- املیباشد قیمتی۷ ومنسوب
بقربه مازك را نیز گویند.
فاد یز « بکس لام و سکون تحتالی
و زای نقطه دار . نوعی از از دشتی باشد
بسیار است
ید ۳۹۹
یار موص ح بکسر زای حوز ؛ بیخی
وعنصل واسقیل همان است و بسنی‌آن را قردمانا
گومئد .
پیادی- بروزن حجازی . نوعی از لمل
قیمتی باشد ۷ - ونوعی از گرز هم مت و آن
چنان است که چند کوی فولادی را بچند زنجیر
کنند وآنرا بترکی چوکن کوند ۸ . جد
ی ۷ » بروزن‌سلام» بمعنی خبر وییفامباشد
۱ رگ : بیه . ۴ رگ : بایاپ . ۴ - پارسی باستان ۵06024812
(قس: سانکرت قا0942, ۰۳208۵1162 معرب بیدق) «اسشق ۰۳4۷ و نیزیاده معرب آست.
دقی؟ » ۴ ر: پیازی. ۵ رك : پیاز کی , 1 - محه‌دین ابراهیم بن
ساعد: اصاری درتض‌التخاثر (صس ۱6) کوید: «ومنه (بلخش < لعل) مابشبه الافوت البهرمالی
وحرف بالیاز کی وهو اعلاها واغلاها.» مسحح کتاب درحاشهٌ همان‌صفحه‌نوشته؛ «هبيجيك ارلغویان
قدیم وجدید این‌لقظ رایاد نکردماند وکمه برای ناو از بلخش (لعل) تر کی جقطایی است. »
ویعاست که ییاز کی مسحف «باز کی* است. ۷ - رك: یبا زکی. ۸ ره : پرازك.
٩‏ -< یفام . اوستا 0216182002 * . پهلوی ۳6۵1 , ارمنی 2۵48277 ؛ از ند
0 استق ۳4۸».
۵ از (برای‌اشتفاق
```


## [2026-09-14T00:55:20.730Z] TOOL CALL #22: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:433 --image 2>&1 | tail -40"
}
```


### [2026-09-14T00:55:21.832Z] TOOL RESULT

```
no scan of BQT covers printed page 433 (see 'scans' in refs_online.json)
```


## [2026-09-14T00:55:23.416Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT pathana ===\"; grep -n \"pa&ana\\|paOana\\|paθana\\|pa9ana\" BRT.txt | head -10; echo \"=== BRT p3r39u ===\"; grep -n \"pdrdOu\\|pərəθu\\|pdrdftu\" BRT.txt | head -5; echo \"=== BRT pavaka/puitika ===\"; grep -n \"püitika\\|puitika\\|pavaka\\|pävaka\" BRT.txt | head -10"
}
```


### [2026-09-14T00:55:23.497Z] TOOL RESULT

```
=== BRT pathana ===
=== BRT p3r39u ===
=== BRT pavaka/puitika ===
```


## [2026-09-14T00:55:27.546Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ana- adj\" BRT.txt | head -5; echo \"---\"; grep -on \"pa.ana-\" BRT.txt | sort -t: -k2 | uniq -c -f0 | head -30"
}
```


### [2026-09-14T00:55:28.723Z] TOOL RESULT

```
---
      1 16161:paäana-
      1 22619:paäana-
      1 13424:pamana-
      1 15412:parana-
      1 15704:parana-
      1 16082:parana-
      1 16127:parana-
      1 16201:parana-
      1 17913:parana-
      1 17931:parana-
      1 30304:parana-
      1 5859:parana-
      1 7721:parana-
      1 9251:parana-
      1 29975:patana-
      1 8402:pazana-
```


## [2026-09-14T00:55:31.068Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16155,16170p' BRT.txt; echo \"=== 22619 ===\"; sed -n '22612,22625p' BRT.txt; echo \"=== 29975 ===\"; sed -n '29970,29980p' BRT.txt"
}
```


### [2026-09-14T00:55:31.145Z] TOOL RESULT

```
Sp.  276  n.  —  4)  VgL  zu  ^flAu  Y.  13.  4.    S.  I         j.  pisialt  P.  44  -.  lies  pn-isin/e.
übrigens  Pü.  —  s)  VgL  lU  pir>r,ivayam-.    —  I  ,  :  ■*,/„.  Adi    PPfP  ■  s.  JA»/^         \ t>3Ümat
6|  VgL  aber  Bezzksbmgeb  GGS.  18^8.  268.  ,,1  '^  *;  Aaj.,rnr..  s.  par-,  \j>PSfmai _      y .        ft  .  L       .         TT  .j     I  Vt/4.36:  s.  unter  toÄJä«-.]
•  ].  p3r9nayu!9.har3irn-bav-  ItompV.  'der .     KompA. Unterhaltung,  Pflege  seitens  der  J',  teil-  
haftig  werden':  'buyS  . .  ätarl puira  ahu-  *  J"  f""'  ^^l-.  **««  ^ejnandergezogen, /•j>S.  Y.62.2.  -  ausgestreckt,  -  geofcef.
Komp.  -iar/^ra-  Adj.  ^-*ai^;  S  ^63.  -  PiL:         ^"!"F\  T.-k"  ^'  t'^w'    "'    '^^    *^''^' ^      r         ,-    ,     -  „J   ^      _;  '       -    jt  -  .■         Adi.  'aufgeblüht,  offen'.    Wegen  ir.  p  und  «1.
•  j.  paranävayam-  f.  'vollkommene  Ab-  •  ]■  'paäana-  n-,  p«äaiüi-  f.  'Kampf, Wendung,  Abbitte':  -^J  (NS.)  F./o.  Schlachf:  nivanäat(sd.)  apaydH  [..]  "«a
Komp.:    ifirina-^ava^yam:    —    Pü.:   äfrtna-    (IS.)   ^(/Ä  Yt. /rf.  57;  —   SOnSt  Plur.:   /'*
kän  i).  —  I)  VgL  tu  pirinäyii  V.  3.  42.  (näml.  fravasayö)  yüilyanti    'rtOAu   hai'e
■  j.  *p9r9n«inna-  Adj.,  PPM,:  s.  pargt-  osaAi  . .  Yt/^.  67;  23,  27;  —  li  (näml,
mit  No.  4.  fravasayö)   uyräAu   'nähu   upastqm  hmä
KompE.  dähistä  Yty.  17;  37;   —  Anfraaurvalsö
•  j.  p3nnö.mäh-  m.  Gottheit  des  Voll-  (sd.)  vüsi  "nasima  YL5. 131.  a)  mit monds, Vollmondstags: 'OTifwÄ^M  o/aj'fl/wOT  I^k.  'uro  (den  Preis  von)  —':  yat  baväni Oia/ie  ratüm  Y.  2.  8;  —  -mhuhäi''*  Y.  i.  8;   aiwi.vanyh  tii'irya^'antfm  . .  ahmi  (Sp.4  m.)
dby  Google
897
'psäana-
=== 22619 ===
biisurg  gvzr  mUunaä  baräy  i  dard  i  mardumän.
•  j.  *van-  f.  'Baum':  yaäia  masyayä  vana kasyaiikam»  "nam  (GP.,  als  Obj.)  aiwi.- vgr-mvaiü  (fA.)  V.5.  2^.
Vgl.  vaHä:  —  ai.  vanäm  GP.  —  Pü.:  van. }.  vana  N.p:  lies  ana;  —  l'.SO:  lies  vai'a. ]'.  vana/ma:  s.  ^van-; —  N.pp:  lies  va  naema. j.  T-anaf  F,  ^f. :  lies  vanf.
•  j.  vanatay-  f. 'Sieg':  sraosaAe . .  vanats {Sp.i25ia.)''MttT/(AP.)va»aiü'vafS  alaond vanats  'naitls  vanaintlmca  uparatät?m yazamaide  Y.57.33.
Ablelt.  —  Zum  V.  'van-.—  Ya.-.  pavSnisnik.
•  j,  vanaiti'vant-Adj.  'sieghaft':  sraosahe.. vanats  vanaitxi  'vatB  asaonS  .  .  Y.57.33.
l'ü.:  vätü/är.
•  j.  vanat-paäana-  Adj,  {fenL  °n3-)  'die
Schlacht  gewinnend':  ya'^a  v?r>%rajA  °nS ^/raxitäne  \.g.20;  • —  aJrTnämi  vavamia ■  *'n3'^  (NSra.)''  iuye  vlspim  aurva'hsm  "ich flehe  darum,  als  Gewinner  der  Schlacht ,  siegreich  zu  werden  über  jeden  Feind" A.  i.  10;  —  fravasayS .  .ya  .,  värüsraytoi \'na  Yt./^.4o;  30,  35.
Pü.  {lu  V.):  vämtir  pa  tuiiln,  Sö.  {^a  A): lälako  yuddhtna.  —  ■>  Hds.  •hm  mit  Vw.  — »)  Falich  JN,  JAOS.  TJ.  LXl.
•  j.  vanana-  m.  'Sieger  über  —  (Gen.), ßesieger,  Überwinder':  sraossm  .  .  yS  'nS kayi^ahe  yS  'nS  käthyehe  yS  janta  daevayä
drup  V.57.  15.
Zum  V,  >MM..  — PB.:  vänIISr'i,  SQ.:  aiubhani tälayel  (i.  'van-  No.  16).  —  ')  NpErl.  in SWienAW.  67.  850.  22:  näfaida  kunanda.
•  g.  vananä-  i.  'Sieg":  ku'äirä  ayi  Aahmäi 'nqm  dadh  "welcher  von  den  beiden (Heerschaaren),  wem  wirst  du  den  Sieg verleihen?"  Y.4^.  15.
=== 29975 ===
Et.  ?  —  NA,  trennt.
).  hifoiM  V.  7.  59:  lies  hamia.
•  j.  ham.tapta-  Adj.  (fem.  ■«-)'>,  PPfP.:
S.  top:
■)  S.  tap.  No.  a.
•  j.  ham.patana-  Adj.  'comes,  Gefährte', von  i/an^schen  Wesen:  hau  datvanqm kandvatfnB  .  .  'nd  V.  7.  54;  53.
Zum  V.  fal:  —  Pü. ;    hampallinih.
•  j.  (rfan7ö.)hiim.par3t«m  AbsoL  'mit, bei  (lang  dauernder)  Zurateziehung',  mit  | Akk.:  . .  mqm  narS  paskät  yazmie  ahunm  1 raazdatn     darrfSyaSt^mi^A^la    'tfmca    H.  I
2.  14.'  j
Abgekürit  für  dan-jö.yastimia  ilarriii.lu\m,far- 1 iUmia,  vgl.  unter  [^ir?ü^ao%ra-  und  s.  Pü- ' Erl.  —  f  ü. ;  pa  an  i  öhrtnaiai  dir  yaöinlh  u hanipursatih ,  erl. ;  der  iat»än  iasän  ihrmazd Tai  ya:ihi  u  hampursakih_  i  frSrön  tarl  "lange Zeit  machen  sie  dem  Ohrm.  Veiehrung  und BefiüEung".
•  j.  ham.bar^tar-  vaDhva,m  m.  EN,  eines
```


## [2026-09-14T00:55:39.314Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"breit'\" BRT.txt | grep -i \"^.*p\" | head -20; echo \"=== search p3r39u ===\"; grep -on \"p.r.\\(9\\|O\\|ö\\|ft\\|8\\)u-\" BRT.txt | head -20"
}
```


### [2026-09-14T00:55:39.405Z] TOOL RESULT

```
15192:\'e1-  iu  fa\iXiiay-.  —  np.  pahn,  ooss.  fäfän 'breit'.  —  P6.!  /flAo«,  Sü.:  fflhulah,  su- viilarak.  —  ')  Wo  vor  yat  mindestens  ahihA amö  ausgefallen  ist;  vgl.  Yt,  5.  41.
=== search p3r39u ===
```


## [2026-09-14T00:55:41.260Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15180,15200p' BRT.txt"
}
```


### [2026-09-14T00:55:41.308Z] TOOL RESULT

```
•  j.  paidyä-  f.  'Fuss',  1)  der  Menschen: as/ica  gaonah  *dfr)w'haca  ^uruhwqmca •yäsfa(,AP,)/ravaxsascaYt.ij.ii.       2)  der
dby  Google
843
■pa»-
pan£a
844
Tierei  yj  säne  pistr?m  jainti . .  apa  vä  hl 'yqm  lamiiaiti  \'.1J.  10;  —  dasintm'''  hl {oämL  sänS)  'yqm  . .  haoyqm  hi  yqm  upa.- larpniayftt  V.  ij.  33.
Ableit.  aos  =/d,/-.   —   u.  (ädyä-  f.  Tusstrilt".
—  l'ü.:  fäi.~  ')  Suit  fem.;    t^daSina-  No.  I.
•  j.  "paÄ-  V.:  s.  unter  ^pad-,
•  J-  S-  'pa9^  m-,  f.:  s.  unter  pantay-,
•  j.  paO^ma-  Adj.  (fem.  'na-)  'breit,  weil'; sqm  pjriiwTm  •iiqm  Y.  10.  4;  —  tarn p?r?iwim  .  .  yqm  masimca  (sd.)  'namca Vt/J.  9;  —  aiiihh  z>ms  yai  °nayä  Yt io,  9s;  //.  19,  5.38";  —  (t^ra  mihrahe frayanä  (sd.)  ..  *nh  jafrä  Yt/0. 112-
\'e1-  iu  fa\iXiiay-.  —  np.  pahn,  ooss.  fäfän 'breit'.  —  P6.!  /flAo«,  Sü.:  fflhulah,  su- viilarak.  —  ')  Wo  vor  yat  mindestens  ahihA amö  ausgefallen  ist;  vgl.  Yt,  5.  41.
•  j.  pad^nay-  patr.  Adj.  'von  Paiana stammend,  dessen  Nachkomme'(?):  k^n- säspö  .  .  yö  janat  hunavo  yat  "naya  tiava \t.ig.4i.
Ableit.  ins  */^~iaua-  m.  EN-,  vgl.  /.liano- Adj.?  Unsichei.  S.  auch  West  SEE.  24-63 No.  4,  DsT.  ZA.  S.  627  Ko.  60.
•  j.  .  .  nqma  haoa  "pait'anö  ,  .  Vd.  ij.
j.flaiayn'/i  S.  loy :  lies /ai%j-ii/i,  s.  Sp.  S44  tn.
•  j-,  g.  pa9ä-  f.  'Pfad,  Weg':  ■■^?«  x'ä- sijt/lm  (sd.J  Ny.  /.  8;  —  '>ajS  s^äsmayj FrW.5. 1 ;  —  catanrü  ptr^rA  (sd.)  vi'iiira- ysis  avi  ''i:qm  katarasät  YL74;.44;  — äat  yasp  'iws  .  .  ''iqm  jasäiti  vq'kwafsö "wenn  zu  dir  an  den  Weg  herankommt (sva.  dir  in  den  Weg  tritt)  ein  Strauch- dieb" Yt  13.  2o;  —  hat  ta  '"ha  frayqn pasvqm  vä  . .  "sollen  diese  Wege  be- gehen .,?"  V.  A'.  14;  15,  ig,  23; —  iiiritim taaa  aitä  'ha  vlvä'iayaritu  .  .  spätem  V, iV.  16;  17,  18;  — yi  ■  ■  kambist}mca  atte ''i:a  frayqn  pasvasca  .  .  V.j.is; — hu^a ,  .  aiaonqm  "'ia  (NS.?)  .  .  ku%a  Jrjatqm Yt4.4.  '  a)  AS.  mit  V.  d,}-  und  Inf. '(Jemandem)  den  Weg  freigeben,  es  (ihm) freistellen  zu  — ">:  hyat  aßyäi  dada  -^qm Tiis/ryiil  vä  äi/i(sd.)  "als  du  es  ihm  (dem Rind)  freistelltest  .  .  zu  .  ."  Y.  31.  9.
Vfil.  faii/ay.  —  Pü. :  rüi.  —  "  Js.  JAOS.  7^. cxxv  gegen  ZDMG,  46.  305.
•  j,  *payäna-  Adj,,  PPM.:  s.  'päd-.
•  p.  pa9-i-')  f.  'Pfad,  Weg":  ''iOn  'tyäm rostäm  ma  avarad^  (sd.)  D.  6.  6.
```


## [2026-09-14T00:55:52.887Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=800 && NR<=845 && /^[0-9]{3}$/ {print NR\": \"$0}' POK_03.txt"
}
```


### [2026-09-14T00:55:54.012Z] TOOL RESULT

```
808: 831
824: 832
833: 833
```


## [2026-09-14T00:55:54.188Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD ==\"; grep -n \"pahn\\|pōy\\|poy \\|pāk\\|pak \" PHD.txt | head -20; echo \"== PHD_mackenzie ==\"; grep -n \"pahn\\|pōy\\|pāk\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-14T00:55:54.254Z] TOOL RESULT

```
== PHD ==
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
1076:breadth pahnay, wēhmīh.
1097:broad pahn, wéhm.
1247:clean pāk; ritually — pādyāb; v. pure.
3294:purity abēzagīh, agumégih, pākīh, yojdahrih.
4309:why čē rāy, čim (rāy). wickedness dušīh, wattarih. wide frax, pahn, wéhm, wišād. widow wéwag.
4310:width pahnāy, wéhmih. wife narig, zan; Cagar. wild kófig.
4746:pāyag pānāgīh pānāg -bān pänagīh panag pānzdah pākīzag pāk pālāy- pālūdan pālūdag 1-2pärag pārsīg pāsox pāsbānīh pāsbān pazen pāzand pazen pāšnag pāšom
4759:pah, pay pahnāy pahn pāyag paygāl
== PHD_mackenzie ==
3981:pahn [p'hn l I N --] wide, broad.
6092:boundary kanarag, marz, saman,         broad pahn, wehm.
6120:breadth pahnay, wehmih.                bUT1"owing sudgig.
7982:wide frax, pahn, wehm, wisad.          worm kirm.
7984:width pahnay, wehmih.                  worse wattar.
8853:pa)iidan                 "~~Q.)              pahnay                   ....,., t'\)'1)
8855:paliidag                 \~""~cu             pahn                        \l'VV
```


## [2026-09-14T00:56:01.179Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== CHEUNG paud ==\"; grep -n \"paud\\|pauda\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T00:56:01.232Z] TOOL RESULT

```
== CHEUNG paud ==
492:*saucé ‘to burn, light", *rai9! / *frait/9 ‘to die, decompose’, *caud / *paud ‘to run’. 
19851:*(s)peud- > Ir. *paud). From this root also Lat. pavere and Gr. mtota would have 
19855:contaminated with *paud (?). Lat. pavére may have a different origin. This Latin 
19862:302 *paud 
19865:*paud ‘to run’ 
19888:s-: hence they cannot be treated as mere "mobile" s-variants of Ir. *paud, which is 
57662:*gaHz, *paud, *saij, *tac’,
```


## [2026-09-14T00:56:02.896Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD pwd ==\"; grep -n \"pwd\\|pōy\\|poyisn\\|pōyist\" PHD.txt PHD_mackenzie.txt | head; echo \"== NYB ==\"; grep -n \"pōy\\|pwd\\|pōyēt\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T00:56:03.024Z] TOOL RESULT

```
== PHD pwd ==
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD_mackenzie.txt:4264:poy- [pwd- I (P pwd-), N .....,] run.
PHD_mackenzie.txt:7509:running (a.) poyisnig, taziigj (n.) tag.      hiidamansar, diid.
PHD_mackenzie.txt:8733:purrsardag            ,~~\O)                  poyisnig                  \ 'U t"\Y 'Q)
== NYB ==
598:a-pohišn [’pwhän'], a-pēyišn [’pwdän'] having no thirst, not thirsting 5922, 774. 10419. — Paz. apčišn, Skr. v. atrsdvant (Mx); the intervocalic alternation -h-: -y- as usual. Only occurring in the rhymed couple a-söhisn (a-söy-) ~, and formally attracted by the first (g. v.);
```


## [2026-09-14T00:56:07.453Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19840,19900p' CHEUNG.txt"
}
```


### [2026-09-14T00:56:07.502Z] TOOL RESULT

```
*pau ‘to be afraid ?’ 

*PARTHIAN: (+ *us-) ‘sp’w- (caus.-iter. ?) ‘to terrify, affright’, *spwh- (pass.) ‘to be 
terrified’, ‘sp’w ‘terror = DMMPP: 86 f. 

Pres.: IND. 3sg. *‘sp’wyd, 3р1. ‘sp’wynd, IMPV. 2р1. *‘sp’wyd; Partic.: perf. pass. ‘spwd; Pass.: pres. 
IND. 3pl. ‘spwhynd, IMPV. 2pl. ‘spwhyd 

© According to Szmerérenyi, Iranica: 206 f., these Parthian forms represent ОП. 
*us-paua- from an IE root *peu- ‘to run’ (presumably the unenlarged root of 
*(s)peud- > Ir. *paud). From this root also Lat. pavere and Gr. mtota would have 
derived. There are several problems with this postulation. The Parthian forms are 
isolated within IIr. and they look very similar to prm’w- ‘to terrify’ (*miuH ‘to 
move’), perhaps ‘sp’w-, etc. actually reflects *us-mjauHa-, which has been 
contaminated with *paud (?). Lat. pavére may have a different origin. This Latin 
verb (implicitly, also Gr. mio ?), has been connected to an IE root *pieH’- ‘to 
strike’, cf. LIV: l.c. 481 f. 

*PIE— > LIV: – | Pok.: 


302 *paud 


*paud ‘to run’ 

*MIDDLE PERSIAN: BMP pwd- /pöy-/ ‘to run, flow’ 

Inf.: BMP pwytn /poyidan/ 

*PARTHIAN: “pwd- ‘to speed, move quickly, run’ = Ghilain: 65 | DMMPP: 286a 
Pres.: IND. 3pl. *pwdynd {unpublished} 

*KHOTANESE: LKh. pusta- (ppp.) ‘driven’ || (+ *niš-) naspusta- ‘driven, thrown out’ 
= SGS: — 

*SOGDIAN: MSogd. pwt ‘woof? 

*CHORESMIAN: (+ *a-) Буа ‘woof? (14.7) 

*NWIR: NP pöyidan/pöy- ‘to wander; to run; to trot’, NP püd, Nn. puy ‘woof, weft’, 
Tr. pöyetön, Varz. pu ‘carpet weft’ 

*NEIR: ? Wa. bit ‘woof 

© This root is connected to Gr. oneÖ8@ ‘I hurry’, Lith. spüdinti ‘to hasten’, etc. by 
Pokorny, l.c. (but the Ir. forms are omitted in LIV, Lei Both forms have an initial 
s-: hence they cannot be treated as mere "mobile" s-variants of Ir. *paud, which is 
perhaps rather a "Reimbildung" (with e.g. *taud) ? Some etymological references, 
notably Arm. (LW) hrapoyr, hrapurem ‘allure’, Skt. pota- ‘boat’, cited by Bailey are 
hardly tenable, cf. EWAia Ш: 338. Also Pth. pwwd ‘small vessel, skiff’ and MSogd. 
pwtyk’h (misspelled as pwty’kh) ‘ferry, skiff are not genuinely Iranian, being rather 
old borrowings from an Indo-Aryan source (Szemerényi 1957: 628b). 

*PIE — — LIV: 581 | Pok.: 998 

*REFERENCES: Szemerényi, Iranica: 205 ff. MacKenzie, Pahlavi: 69; DKS: 247b, 178a; 
Steblin-Kamenskij 1999: 97; Lecoq 2002: 635a, 669b, 682a
```


## [2026-09-14T00:56:16.729Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD pete ==\"; grep -n \"^pete-\\|^peu\\b\\|^peu-\\|^pet-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T00:56:16.776Z] TOOL RESULT

```
== AHD pete ==
843:pet-
845:pete-
```


## [2026-09-14T00:56:17.852Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ISS/DKS pu ==\"; grep -n \"^pu-\\|^pūy\\|^puy\\|pūta-\\|pauda\" ISS_alt_DKS.txt | head -20"
}
```


### [2026-09-14T00:56:17.923Z] TOOL RESULT

```
== ISS/DKS pu ==
857:āra- ' worthy, valued’, п s-7o ara basava dayi сайтта ' make the honoured wheel of dharma-doctiine to turn'; K 5110 samahüm àrá dana 'samüdhana-trance with the honoured dharma-doctrine (where however arya-dharma- is possible)'; и 106:130 dharma-cakrra ära bgisá ‘шп the honoured dharma-wheel'; їп 5620-1 tta baudasatva viysünvü dyaunvà (not-ra-) ағӣ bisl namasū nàmda ' these bodhisattvas, honoured in bindings (of mind), in dhyana- trances, all of them I revere with obeisance’; =K гот tta baudasatva viysünvü dyaunvü (not- Ной) ата bisü патахй nauda. From *атра- adjective to āra- 'value, worth, price’. Not Prakrit for BS arya- (so proposed SDTY 31) and hence not with āra- as first component in HI 55:6 ürá-paudagalá, BS ürya-pudgala-; in a BS text 1H 63:85 ara-samadrüya ' to the noble sea’; K 99:237 āra- verümca, BS àárya-vairocana-; K 149'14 àra-ttürru, BS ürya-lürü; 1 107'15 àra-majvaüsüri, BS ürya-manjusri; nr Io7'r4 aravalakyaittaifvará, BS àaryavalohitesvara- and elsewhere, See with suffix -ava- M.Parth.T. 'rg'w worthy, fine, glorious, noble (*argaua-), 'rg'uyft' beauty’; metathetic 'gr'w; М.Регѕ.Т. 'gr'w ' worthy, noble, fine’, 'gr'yy ‘beauty’ (ayrayi); Armen. lw argoy “honourable, valuable, effective’, yargem ‘to honour, treasure’, an-arg 'unworthy, ignoble' (-r- from Iranian, IE Pok. 32-3 alg*h-). Here also 11 97:110—11 ca và rrot jsá йтй narau- müvai ‘what honour may issue from the court’; =п 94, 26-7 ca-m và rrvi jsa ara hisiyai, —11 94, 28-9 ca-m хар āra hagrrihatia hamavai, = 97:112-13 ca-m sam ara hagrrihüia hamüvai. Not BS adara- ‘respect’ here, hardly suitable as coming fram the Court,
5973:pa убйас 'cloak'. BS lw Mahávyutpatti 9183 zanduraka Tib. ras bal-gyi stan 'coverlet of cotton (and) wool’, Divyàvadüna 19:23 manduraka-, but Pali Vinaya 1 196-6 majjharu. See BSOAS 26, 1963, 72 ff. This mand- may be connected with Celtic in Lat. mantu-s, mantellum ‘mantel’, whence O.Engl. mentle, OHG mantal; from late Greek џбутіюу, Slav. O.Russ. manütija, O.Slav. manütijica ‘pallium’. Possibly a base man- 'to hang down (?)'. mande ‘woman’, Пі 12352 mande (nom. sing.) gloss to BS nari; п 11021 mandve bema nà ‘the woman received woven cloth’; rt 13622 mandai và kusa а ' seek out one woman’ gloss to Chinese bīka ñau іса la (К. 675*1 nü, older niwo ‘woman’); Manj. 166 ttyä jsa mande hvaida тазја ‘from these it (#йпуа1й) is rightly called female’; HI 13721 khu tti mandai kainą puaisa ' when I then ask for the woman’; gen. sing. t 183, rorvr єй mandyi pūra nt hami ‘what woman has no child’, BS lamba-garbha- ; 1179, 97v5 mandi oidana ' with woman's milk’, BS ksira-; u 777 mandvai va 'for the woman’; п 77:38 mandvai baida; п 77:40 тащіоаї bida padaidaudü ' we made clothes for the woman’; plural, ш 123:63 pharüka mandi brrai ‘many beloved women’, gloss to BS prabhiüta nari priya; II 10977 mangur cu bema nauda ' the women who received woven cloth’; K 36:100-1 sam vari mandi shadadi maysairká ‘on the spot the women made great (noise)'; gen. plur., 1 183, 102v2 mandyam büraña acha ‘illnesses in women's womb’; 1 159, 73vs münsta-ujüm (-im- —-ai-) mandyam ‘of pregnant women’ (see #ra- 'belly, womb"); 1 151, 62v3 mandyüm varajünd püraña acha 'illnesses of the womb, to be experienced by women’, Inflexion, sing. nom. ~e, gen. -i, -yf, plural =£, - (see also s.v. mijse "woman"). Connexion with child birth may indicate a derivation from :ma(i)k- 'to suckle? hence *mantiya- < *ma(i)kantiyá- to Av. magh-, N.Pers. makī- dan, талїйап ‘to suck, taste’, Balōčī mičag ‘ќо suck’, mixta, causative тїїйпау, Zor.P. mičak 'toste', N.Pers. mazah. From a base IE *maik-, mak-, see IE Pok. 698 mak-, māk- ' moist', O.Slav. mokrů ' moist’, тосо, mociti ‘to moisten’, Czech mdákati 'to moisten’. mattüna- ‘Бай, rotted', with mu-, muttüm, I 163, 77v4. mattüna bausa ‘rotten smell’, BS pūta-; Ú 33, 3b2 ратай paskvagta тийпт himye “һе road has again become bad’, From *mudata- > тийа-, matta- with -auna- or gauna- (' colour") to base maud- :mud-, ТЕ Pok. 741-3 meu-, O.Ind. mudird- 'cloud', Greek Búëos ‘moisture’, pude ‘be moist, foul’, with sneu-, MHG smuz, Engl. smut, smotten ‘to foul’, Engl. smut, mud. math- ' churn', see mamth-. mada- ‘intoxication’, dialectal or archaic or possibly BS lw, K 63, 79r3 mada-mayq Ёһаўа süda-bhaujana. Гелда 'intoxicant beverages, sudha-bhojana-food' (BS sudha ' fine food"). To base mad-, see s.v. maya-, meva, maitti. For -d-, see badari. madana, to read та ' here (?)', dana ' seeds, ш 87, 128. ma-däru 'not long, soon’, v 180a12 ma-dàru avasau аузй nvástá yanimá ' soon surely (BS avasyam) I can bring in’; Z 5113 ttyau puñyau атаб ma-daru balysuftu hastamu bvüne 'by these merits surely soon I may awaken to the best bodhi-knowledge'; =Z ir77 avaííó aysu hamatd
6161:müttiña ‘clouds’, plural to "mütünya-, їп 80326 avafü müttiia narrvāmdä 'in the sky (BS akaía-) the dark clouds burst open', in the poem of the Journey. From *mutta- with suffix -ina- and -ya- to base mau-:mu- ‘be moist, be dark’ (see also zuttüm, BS pūta- 'rotten?), with mitta- < *miüta-, beside maud- in O.Ind. mudird- 'cloud'; IE Pok. 741-3 Armen. moutt 'dark; a mist’, тп‘ ат ‘dark’ from meu-t-.
7694:sürai ‘Баа (?)', Manj. бб ausa agapt sa sürat anecvà skajva üttma ' this self (BS atman-) is bad, improper, evil in the impermanent (BS anitya-) samshára-acts' ; Manj. 13 sülia sūrai üttama па ttye 'in pleasure (BS sukha-) evil is not the self of this man'; pejorative from the context, hence possibly from *safra-, *sifra or *sufra ‘rotted’ to Lit. ipti, Smpü ‘be weak’, Ийрїї, Йитрй ‘о corrupt’, as Oss. D. fud, I. fyd 'bad' from pūta- 'rotted' (see s.v. hambūta-), Greek стүттоноп ‘to rot', солтра, отүтгтїк®. Hardly *asuraa- ' not pure’ by loss of a- (as zasa- from anaufa-); possibly süra-a- to sūra- ‘strong’ in bad sense ' violent.
7843:spai-: spy- ‘бе rich, abound, be satisfied, prosperous, complete’, Z 19:18 spaiyd, Z 20:64 spaiye; v 280, 522 ne spaite; ibid. b3 me spaiye; II 11713 püsa hüfala-miüla hà spyüpde ‘тау good roots of merits flourish'; п 76254-5 artha-bhaugá huastanña suhd:nam spyārä ‘possessions (BS artha-bhoga-) with the joy (BS suklta-) of best things abound for them' (suhdma and 3 plur. pronoun -dg); v 64:3 spaivi hiysdä vira ahagta ‘he flourishes at present continuously’; 3 plur. їп 127:22-3 Pilla spaudai 'may merits abound’, Preterite, spata-, Z 20-66 siakrá ne spatá stà ' (the god) Sakra is not sated’; SuvP. 71v4 spa masu jsarij ramna ‘abundant corn and precious stones’ (BS ratna-), BS prabhitta-dhana-dhanya- vicitra-ratnaih; SuvP. 73r1 spa mase päjiñä tsāvi 'abun- dant rich treasuries', BS prabhüta-dhana-dhanya-samrddhi- kogült; 1 175, 92r2 сӣ būri spa hamya tcahausa tcaura acha Ыза jari "however they abound, all the 404 diseases vanish’, BS eyadhi-éatair grastas caturbhi$ catur-
```


## [2026-09-14T00:56:25.112Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '840,860p' AHD_watkins1985.txt; echo \"=== peu ===\"; grep -n \"^peu\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T00:56:25.165Z] TOOL RESULT

```
per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
per-‘. To try, risk (< “to lead over,” “press forward”). A verbal root belonging to the group of per’. 1. Lengthened grade *pér- in Germanic *féraz, danger, in Old English
50
pet-
fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
pete-
ré, feather, in Old English fether, feather: FEATHER. 2. Latin petere, to go toward, seek: -PETAL, PETITION, PETULANT; APPETITE, COMPETE, IMPETUS, PERPETUAL, REPEAT. 3. Suffixed form *pet-nd in Latin penna, pinna, feather, wing: PANACHE, PEN!, PENNA, PENNATE, PEN- NON, PINNA, PINNACLE, PINNATE, PINNATI-, PINNULE. 4. Suffixed form *pet-ro- (see 6ku-). 5. Suffixed form *pet-yo- in Latin propitius, favorable, gracious, originally a religious term meaning “falling or rushing forward,” hence “eager,” “well-disposed” (said of the gods; pro-, forward; see per'): PROPITIOUS. 6. Suffixed zero-grade form *pt-ero- in Greek pteron, feather, wing, and pterux, wing: -PTER; ACANTHOPTERYGIAN, APTERYX, ARCHAEOP- TERYX, COLEOPTERA, MECOPTERAN, PERIPTERAL, PLE- COPTERAN, PTERIDOLOGY, PTEROCERCOID, PTERYGOID. 7. Suffixed zero-grade form “pt-ilo- in Greek ptilon, soft feathers, down, plume: COLEOPTILE. 8. Suffixed variant form *pté-no- in Greek pténos, winged, flying: STEAROP- TENE. 9. Reduplicated form *pi-pt- in Greek piptein, to fall: PTOMAINE, PTOSIS; PERIPETEIA, PROPTOSIS, SYMP- TOM. 10. O-grade form “pof- in Greek potamos (-amo-, Greek suffix), “rushing water,” river: HIPPOPOTAMUS. [Pok. 2. pet- 826.] pete-. To spread. 1. Suffixed o-grade form “pota)-mo- in Germanic *fathmaz, “length of two arms stretched out,” in Old English fethm, fathom: FATHOM. 2. Suffixed (stative) variant zero-grade form *pat-é- in Latin patére, to be open: PATENT, PATULOUS. 3. Variant zero-grade form in nasalized form *pat-no- probably in Latin pan- dere (past participle passus < *pat-to-), to spread out: PACE!, (PAS), (PASS), PASSIM; EXPAND, REPAND. 4. Suf- fixed form *pet-alo- in Greek petalon, leaf: PETAL. 5. Suf- fixed form *pet-ano- in Greek patané (? < *petand), platter, “thing spread out”: (PAELLA), PAN!, PATEN, (PATINA!), (PATINA2). [Pok. 1. pet- 824.] [petra. Cliff. Greek noun. Collective formation from petros, rock, stone (of unknown origin). PETRO-, PET- ROUS; PARSLEY, PETRIFY, SALTPETER.] peu-. To cut, strike, stamp. 1. Suffixed (participial) zero-grade form *pu-to-, cut, struck, in: a. Latin putdre, to prune, clean, settle an account, think over, reflect, consider: PUTAMEN, PUTATIVE; (ACCOUNT), AMPUTATE, COMPUTE, COUNT!, DEPUTE, DISPUTE, IMPUTE, REPUTE; b. possibly Latin puteus, well (> Old English pyét): Prt’. 2. Variant form *pau- in: a. suffixed form *pau-yo- in Latin pavire, to beat: PAVE, (PAVE); b. suffixed (stative) form *paw-é- in Latin pavére, to fear (< “to be struck”): PAVID; C. perhaps Greek paiein, to beat: ANAPEST. [Pok. 3. péu- 827.] peue-. To purify, cleanse. Suffixed zero-grade form *pii-ro- (< *pua-ro-) in Latin purus, pure, and purgdre, to purify (< “piir-igdre; second element agere, to drive; see ag-): PURE, PURGE, PURITAN; COMPURGATION, DEPU- RATE, EXPURGATE, (SPURGE). [Pok. 1. peu- 827.] peuk-. Also peug-. To prick. Zero-grade form “pug-. 1. Suffixed form *pug-no- in Latin pugil, pugilist, and pugnus, fist, with denominative pugndare, to fight with the fist: PONIARD, PUGILISM, PUGIL STICK, PUGNACIOUS; IMPUGN, OPPUGN, REPUGN. 2. Nasalized zero-grade form *pu-n-g- in Latin pungere, to prick: BUNG, POIGNANT, POINT, POINTILLISM, PONTIL, (POUNCE!), (POUNCE?), PUNCHEON!, PUNCTUATE, PUNCTURE, PUNGENT; COM- PUNCTION, EXPUNGE, SPONTOON, TRAPUNTO. 3. Greek pugmé, fist: (PYGMAEAN), PYGMY. [Pok. peuk- 828.] pezd-. To fart. 1. Suffixed form *pezd-i- in Germanic *fistiz, a fart, in Middle English fisten, to fart: FEIST, FIZZLE. 2. Latin pédere, to fart: PETARD. 3. Possibly Latin pédis, louse (? < “foul-smelling insect”): PEDICU- LAR. See also perd-. [Pok. pezd- 829, 2. peis- 796.] peter-. Father. 1. Germanic *fadar in Old English feder (> Middle English fader), father: FATHER; FOREFATHER. 2. Latin pater, father (> patrare, to bring about): PADRE, PATER, PATERNAL, PATRI-, PATRICIAN, PATRIMONY, PA- TRON; EXPATRIATE, IMPETRATE, PERPETRATE. 3. Greek
51
plat-
patér, father: PATRIOT; ALLOPATRIC, EUPATRID, PATRI- ARCH, SYMPATRIC. [Pok. paté(r) 829.]
p(h)ol-. To fall. Suffixed form *phol-no- in Germanic *fallan in: a. Old English feallan, to fall: FALL; b. Ger- manic causative *falljan, “to cause to fall,” strike down, in Old English fellan, fyllan, to cut down: FELL; c. Ger- manic compound *bi-fallan, to fall, happen (*bi-, by, at; see ambhi), in Old English befeallan, to fall: BEFALL. [Pok. phél- 851.]
[phulax. Watcher, guard. Greek noun of unknown origin, related to phulassein (Attic phulattein), to guard, pro- tect. PHYLACTERY, PHYLAXIS; PROPHYLACTIC. ]
pik-. Pitch. Latin pix (stem pic-), pitch: PAY?, PICEOUS, PITCH!; PICOLINE, PITCHBLENDE. [In Pok. pei(a)- 793.]
pilo-. Hair. A possible root. 1. Latin pilus, hair: PELAGE, PILAR, PILE’, PILOSE, PILUS, PLUCK, PLUSH, POILU; CAT- ERPILLAR, DEPILATE. 2. Suffixed reduced form “pil-so- possibly in: a. Latin pilleus, pileus, felt cap: PILEUS, PILLAGE; b. Greek pilos, felt: PILOCARPINE. [Pok. pi-lo- 830.]
pipp-. To peep. Imitative root. 1. Latin pipdre, to chirp (> Old High German pfiffa, pipe): FIFE, PIPE. 2. Latin pipire, to chirp: PIGEON. 3. Gaelic piob, a pipe, in Scot- tish Gaelic piobaireachd, pipe music: PIBROCH. [Pok. pip(p)- 830.]
[pippali. Pepper. Sanskrit noun of unknown origin. Possibly related to pippala, the bo tree. 1. Sanskrit pippali: PEPPER, (PIMPERNEL). 2. Sanskrit pippalam: PEEPUL.]
[pius. Dutiful, devoted, pious. Latin word having cog- nates in other Italic languages. PIACULAR, (PIETA), PI- ETY, PIOUS, PITTANCE, PITY; EXPIATE, IMPIOUS.]
plab-. To flap. Imitative root. Middle English flappen, to flap: FLAP [Pok. plab- 831.]
plak-'. Also plak-. To be flat. Extension of pele-2. 1. Germanic *fléh6 in Old Norse fl6, layer, coating: FLOE. 2. Variant form *pldg- in: a. Germanic *flék- in Old English fléc, flatfish: FLUKE!; b. Germanic *flakaz in Norwegian flak, flat piece, flake, probably akin to the Scandinavian source of Middle English flake, flake: FLAKE}; c. Germanic *flak- in Old Norse flaki, fleki, hurdle: FLAKE?. 3. Extended form *plakd in Germanic *flag6 in Old Norse flaga, layer of stone: FLAG, FLAW}. 4. Possibly suffixed (stative) form *plak-é-, to be calm (as of the flat sea), in Latin placére, to please, be agreeable: PLACEBO, PLACID, PLEA, (PLEAD), PLEASANT, PLEASE; COMPLACENT. 5. Lengthened suffixed form *plak-G- in Latin placdre, to calm (causative of placére): PLACABLE, PLACATE. 6. Nasalized form *pla-n-k- in Latin plancus, flat, flat-footed, whence planca, board: PLANCHET, PLANK, PLANK-SHEER. 7. Variant form *plag- in: a. perhaps Latin plaga, net (? < “something ex- tended”): PLAGIARY; b. Greek plagos, side: PLAGAL, PLAGIO-, PLAYA. 8. Root form *plak- in Greek plax, flat, flat land, surface: PLACENTA, PLACOID. 9. Variant form *pelag- in Greek pelagos, sea: PELAGIC; ARCHIPELAGO. [Pok. 1. pla-k- 831.]
plak-2. To strike. 1. Nasalized variant forms *pla-n-k-, *pla-n-g- in: a. Germanic *flang- in Old Norse flengja, to flog, whip, akin to the Scandinavian source of Middle English flingen, to fling: FLING; b. Latin plangere, to strike (one’s own breast), lament: PLAINT, PLANGENT; COMPLAIN. C. suffixed form *plang-yo- in Greek plazein, to drive away, turn aside: PLANKTON. 2. Variant form *plag- in Latin plaga, a blow, stroke: PLAGUE. 3. Suf- fixed form *pldk-yo- in Greek pléssein, to beat, strike: PLECTRUM, -PLEGIA, PLEXOR; APOPLEXY, CATAPLEXY, PARAPLEGIA. [Pok. 2. pldk- 832.]
plat-. To spread. Extension of pele-?. 1. Variant form *plad- in Germanic *flataz, flat, in: a. Old Norse flatr, flat: rLAT!; b. Old French flater, to flatter: FLATTER!. 2. Suffixed variant form *plad-yo- in Germanic *flatjam in Old English flei(t), floor, dwelling: FLAT?. 3. Basic form *plat- in Germanic *flathd(n), flat cake, in Late Latin
=== peu ===
880:peuor 828.]
```


## [2026-09-14T00:56:25.762Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hrapoyr\" ISS_alt_DKS.txt | head -3"
}
```


### [2026-09-14T00:56:25.809Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:56:40.124Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN pure ==\"; grep -n \"^pure,\\|pure, adj\\|purus\\|pürus\" KLN_1966.txt | head -8; echo \"== KLN petal ==\"; grep -n \"petal, n\\|patane\\|petalon\" KLN_1966.txt | head -8; echo \"== KLN pan ==\"; grep -n \"^pan, n\\|pan, n\\.\" KLN_1966.txt | head -5"
}
```


### [2026-09-14T00:56:40.217Z] TOOL RESULT

```
== KLN pure ==
10944:depurate,  tr.  v.,  to  free  from  impurities.  —  ML. depuratus,  pp.  of  depurare,  ‘to  purify  thorough¬ ly’,  fr.  de-  and  purdre,  ‘to  purify’,  fr.  purus, ‘clean,  pure’.  See  pure  and  verbal  suff.  -ate. Derivatives:  depurat-ion,  n.,  depurat-ive,  adj., depurat-or,  n.,  depurat-ory,  adj. deputation,  n.  —  See  next  word  and  -ation. depute,  tr.  v.  —  F.  deputer,  fr.  L.  deputare,  ‘to cut  off,  prune;  to  esteem,  consider’,  in  Late  L., ‘to  destine,  allot’,  fr.  de-  and  putare,  ‘to  trim, prune,  lop,  clean,  cleanse;  to  think  over,  con¬ sider,  reckon,  count’.  See  putamen  and  cp.  pu¬ tative  and  words  there  referred  to. deputize,  tr.  v.,  to  appoint  as  a  deputy;  intr.  v., to  act  as  a  deputy.  —  Formed  fr.  deputy  with suff.  -ize.
18987:impure,  adj.  —  L.  impurus,  ‘unclean’,  fr.  in-,  ‘not’, and  purus,  ‘clean,  pure’.  See  pure.
18988:Derivatives:  impure-ly,  adv.,  impure-ness,  n. impurity,  n.  —  F.  impurete,  fr.  earlier  impurite, fr.  L.  impuritatem,  acc.  of  impuritas,  ‘unclean¬ ness,  impurity’,  fr.  impurus.  See  prec.  word  and -ity.
31044:purblind,  adj.,  1)  (archaic)  wholly  blind;  2)  partly blind.  —  Fr.  earlier  pure-blind,  ‘completely blind’,  a  hybrid  coined  fr.  pure  (fr.  F.  pur,  fr.  L. purus),  and  blind  (fr.  OE.  blind).
31049:purdah,  n.,  curtain  guarding  women  from  public view  in  India.  —  Hind,  and  Pers.  pardah,  ‘veil’, pure,  adj.  —  ME. pur, pure,  fr.  OF.  (=  F.)  pur,  fr. L.  purus,  ‘pure,  clean’,  which  is  rel.  to  putus , ‘clear,  pure', putare,  'to  cleanse, clean’,  and  cogn. with  OI.  pdvate,  punati,  ‘purifies,  cleanses’, putah ,  ‘pure’,  putih,  ‘purification’,  pavitar-,  ‘pu¬ rifier’,  MIr.  «r,  ‘fresh,  new’,  OHG.  fowen,  ‘to sift’.  See  putative  and  cp.  purblind,  puree,  pur¬ gatory,  purge,  purify,  depurate,  expurgate.  Cp. also  pious  and  words  there  referred  to. Derivatives:  pure,  adv.,  pure-,  pref.  meaning ‘purely’,  pure-ness,  n.
31050:puree,  n.,  mash,  thick  soup.  —  F.,  fr.  purer,  ‘to strain,  pass  through  a  sieve’,  fr.  L.  purare,  ‘to purify’,  fr.  purus.  See  prec.  word, purfle,  tr.  v.,  to  decorate  with  a  border  of  em¬ broidery.  —  ME.  purfiten,  fr.  OF.  porfiler,  pur- filer,  fr.  VL.  *prdfitdre,  fr.  1st  pro-  and  L.filum , ‘thread’.  See  file,  ‘collection  of  papers’,  and  cp. profile.
31057:pounded  of  purus ,  ‘pure',  and  agere,  ‘to  set  in motion,  drive,  lead’.  See  agent,  adj.,  and  cp. spurge,  expurgate.  Cp.  also  the  second  element in  litigate,  navigate.
31059:purification,  n.  —  MF.  (=  F.),  fr.  L.  purificdtio- nem,  acc.  of  purificdtid,  fr.  purificatus,  pp.  of purificare.  See  purify  and  -ion. purificatory,  adj.  —  Late  L.  purificatorius,  ‘tend¬ ing  to  purify’,  fr.  L.  purificatus ,  pp.  of  purificare. See  next  word  and  adj.  suff.  -ory. purify,  tr.  v.,  to  make  pure;  to  cleanse.  —  ME. purifier i,  fr.  OF.  (=  F.)  purifier,  fr.  L.  purificare, ‘to  make  pure,  purify’,  which  is  compounded  of purus,  ‘pure’,  and  -ficare,  fr.  facere,  ‘to  make’. See  pure  and  -fy.
== KLN petal ==
3057:Derivatives:  apertur-al,  apertur-ed,  adjs. apetalous,  adj.,  having  no  petals  ( bot .)  —  Formed fr.  priv.  pref.  a-  and  Gk.  7t6xaXov,  ‘thin  plate of  metal;  leaf’.  See  petalon  and  -ous. Derivative:  apetalous-ness,  n. apex,  n.,  the  highest  point  of  something,  top, summit.  —  L.,  ‘top,  summit,  the  extreme  end  of a  thing;  the  small  rod  at  the  flamen’s  cap’,  lit. ‘something  joined  or  fastened  to’,  formed  with suff.  -ex  fr.  apio,  apere,  ‘to  join,  fasten’ ;  see  apt. For  the  formation  of  apex  fr.  apere,  cp.  vertex, ‘top,  summit’,  fr.  vertere,  ‘to  turn’.  Cp.  peri¬ apical.
14447:‘a  weight".  Cp.  also  expand,  expanse,  pace, pan,  ‘a  broad  vessel",  pandiculation,  pandy, passage,  passim,  passport,  paten,  patent,  patera, patibulary,  patina,  patio,  patulous,  petal,  petalon, Petasites,  petasus,  sur-  pass,  trespass. Derivatives  -.fathom,  tr.  v.  (q  .v.),  fathom-age,  n., fathom-er,  n.,  fathom-less,  adj.,  fathom-less-ly, adv.,  fathom-less-ness ,  n. fathom,  tr.  v.  —  ME.  fadmen ,  fathmen,  fr.  OE. fxdmian ,  ‘to  embrace,  surround,  envelop",  fr. fadm.  See  fathom,  n.
24307:monopetalous,  adj.,  having  one  petal  only  (bot.) —  Compounded  of  mono-  and  Gk.  ti^tixXov,  ‘a thin  plate  of  metal,  leaf’.  See  petalon  and  -ous. monophobia,  n.,  a  morbid  fear  of  being  alone (med.)  — -  Compounded  of  mono-  and  Gk. -<po[3ta,  ‘fear  of’,  fr.  90(80:;,  ‘fear’.  See  -phobia, monophthong,  n.,  a  single  vowel  sound  —  Gk. |xovo<|)fioyyo?,  ‘having  one  sound’,  com¬ pounded  of  povo?,  ‘alone,  single’  (see  mono-), and  cpdoyyo;,  ‘sound,  voice,  vowel’,  which  is rel.  to  99-cyp.ot,  ‘sound,  voice,  speech’,  cp-Diyye- afim,  ‘to  speak  loud;  to  praise,  sing’.  Cp. diphthong,  triphthong.
28369:petalism,  n.,  a  synonym  of  ostracism.  —  Gk. jr£Tx>aa|i.6;,  method  of  temporary  banishment in  Syracuse;  so  called  because  the  names  of those  to  be  banished  were  written  on  olive leaves,  fr.  -etxaov,  ‘leaf’.  See  petalon  and  -ism.
28370:petalite,  n.,  a  silicate  of  aluminum  and  lithium {mineral.)  —  Formed  fr.  Gk.  7T£TaXov,  ‘thin plate  of  metal’  (see  petalon),  with  subst.  suff. -ite.
28372:-y  (fr.  Gk.  -iajfr.  Gk.  TiETaXetS-rji;,  ‘leaflike’,  fr. ttetccXov,  ‘leaf’  and  - c,  ‘like  .  See  petalon and  -ode,  ‘like’.
28374:petalon,  n.,  the  gold  plate  on  the  Jewish  high priest’s  miter.  —  Gk.  tctoiXov,  ‘thin  plate  of metal,  leaf’,  neut.  of  the  adj.  msTaXo?,  ‘spread out’,  rel.  to  TisTavvuvai,  ‘to  spread  out’,  fr.  I.-E. base  *pet-,  ‘to  spread  out’,  whence  also  L.  patere, ‘to  lie  open’,  ON .fadmr,  ‘embrace,  bosom’,  OE. ftedm,  ‘embrace,  bosom,  fathom’.  See  fathom and  cp.  petasus.
28375:Petalostemon,  n.,  the  prairie  clover  {bot.)  — ModL.,  compounded  of  Gk.  TOTaXov,  ‘leaf’, and  cTfj|j.tov,  ‘warp’.  See  prec.  word  and  stamen, -petalous,  combining  form  meaning  ‘having  a certain  number  or  a  certain  shape  of  petals',  as in  dipetalous,  eieutheropetalous  (bot.)  —  ModL. -petalus,  fr.  Gk.  TrexaXov,  ‘leaf’.  See  petalon  and -ous.
== KLN pan ==
```


## [2026-09-14T00:56:41.072Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON passage ==\"; grep -n \"پاساژ\\|پاسپورت\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-14T00:56:41.160Z] TOOL RESULT

```
== MON passage ==
MON_part1.txt:28216:پاسپورت: ۲5:۲0 )٩(‏ پروانه برای 
MON_part1.txt:39405:پاسپورت؟ ج. تذا کر ( کم.)
```


## [2026-09-14T00:56:53.168Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28210,28222p' MON_part1.txt; echo \"=== passage ===\"; grep -n \"اساژ\\|پاساژ\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head"
}
```


### [2026-09-14T00:56:53.256Z] TOOL RESULT

```
پاسبز: 027 (ص‌مر. امر.) مبانجی. 
۳ شوم قدم. 

پاسپار: 0۲ (امر.) پاساره لگد. 
(ص‌مف.) بای سبر» بی سیر ؛ لکدکوب. 
پاسپورت: ۲5:۲0 )٩(‏ پروانه برای 
آزادی رفت و آمد اشخاص از مملکتی به 
مملکت دیگر؛ گذرنامه؛ جواز عبور بته. 
تد‌کره» ساشرد. اجازهة عبور به کشتی 
ازرگانی از آب‌های ساحلی مملکتی. 
پاستوریزه: 6( (مص‌م.) گرم کردن 
آبجو و شراب و شیر و غیره بنایر اصول 
=== passage ===
MON_part2.txt:42396:ماساژ: 2۰27 (.) مالش» مشت و مال. 
MON_part2.txt:78410:گرم و ماساژ) نیز مفید بنظر می‌رسد؛ دار
```


## [2026-09-14T00:56:53.892Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"a  broad  vessel\\|broad  vessel\" KLN_1966.txt | head -5"
}
```


### [2026-09-14T00:56:53.955Z] TOOL RESULT

```
14447:‘a  weight".  Cp.  also  expand,  expanse,  pace, pan,  ‘a  broad  vessel",  pandiculation,  pandy, passage,  passim,  passport,  paten,  patent,  patera, patibulary,  patina,  patio,  patulous,  petal,  petalon, Petasites,  petasus,  sur-  pass,  trespass. Derivatives  -.fathom,  tr.  v.  (q  .v.),  fathom-age,  n., fathom-er,  n.,  fathom-less,  adj.,  fathom-less-ly, adv.,  fathom-less-ness ,  n. fathom,  tr.  v.  —  ME.  fadmen ,  fathmen,  fr.  OE. fxdmian ,  ‘to  embrace,  surround,  envelop",  fr. fadm.  See  fathom,  n.
27088:pan,  n.,  a  broad  vessel.  —  ME.  panne,  fr.  OE. panne,  which,  together  with  ON.,  Swed.  panna, Dan.  pande,  OFris .panne,  OLG. panna  (whence MLG.,  LG.,  MDu.  panne,  Du.  pan),  OHG. phanna,  pfanna  (whence  MHG.,  G.  pfanne), ‘pan’,  is  borrowed  fr.  ML.  panna,  fr.  VL.  *pat- na,  fr.  L.  patina,  ‘broad  dish,  pan’,  ult.  fr.  Gk. rraxavT),  ‘flat  dish’,  which  is  rel.  to  itexavvovaa, ‘to  spread  out’,  fr.  I.-E.  base  *pet-,  ‘to  spread’. See  fathom,  n.,  and  cp.  paten.
```


## [2026-09-14T00:57:08.300Z] TOOL CALL #41: Bash

```json
{
 "command": "head -40 tools/fetch_source.py"
}
```


### [2026-09-14T00:57:08.346Z] TOOL RESULT

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


## [2026-09-14T00:57:14.549Z] TOOL CALL #42: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%88%DB%8C%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pet%CA%B0%E2%82%82-\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%B5%CF%84%CE%B1%CE%BB%CE%BF%CE%BD\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 401 verification\" 2>&1 | tail -3; done"
}
```


### [2026-09-14T00:57:17.952Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/9860df93f781b106.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DA%A9
/home/sfmqrb/git/rishe/data/verification/sources/web/bd9981cf3bef66ad.txt
### https://en.wiktionary.org/wiki/%D9%BE%D9%88%DB%8C%DB%8C%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/e4879b84bd66d091.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pet%CA%B0%E2%82%82-
/home/sfmqrb/git/rishe/data/verification/sources/web/06d3df39dc8cf7f3.txt
### https://en.wiktionary.org/wiki/%CF%80%CE%B5%CF%84%CE%B1%CE%BB%CE%BF%CE%BD
/home/sfmqrb/git/rishe/data/verification/sources/web/1ec856bc8fff65ff.txt
```


## [2026-09-14T00:57:20.015Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9860df93f781b106 bd9981cf3bef66ad e4879b84bd66d091; do echo \"##### $f\"; grep -n -A25 \"Etymology\" $f.txt | head -60; done"
}
```


### [2026-09-14T00:57:21.089Z] TOOL RESULT

```
##### 9860df93f781b106
73: Etymology 
74-
75- 2.2 
76- Noun 
77-
78- 3 
79- Persian 
80-
81- Toggle Persian subsection 
82-
83- 3.1 
84: Etymology 1 
85-
86- 3.1.1 
87- Pronunciation 
88-
89- 3.1.2 
90- Adjective 
91-
92- 3.1.2.1 
93- Derived terms 
94-
95- 3.1.2.2 
96- Descendants 
97-
98- 3.2 
99: Etymology 2 
100-
101- 3.2.1 
102- Pronunciation 
103-
104- 3.2.2 
105- Noun 
106-
107- 3.3 
108- References 
109-
110- Toggle the table of contents 
111-
112- پهن 
113-
114- 8 languages 
115-
116- فارسی 
117- Na Vosa Vakaviti 
118- Kurdî 
119- Malagasy 
120- Bahasa Melayu 
121- Русский 
122- Türkçe 
123- 中文 
124-
--
249: Etymology
250- [ edit ] 
251-
252- From Persian پهن ( pahn ) .
253-
254- Noun
255- [ edit ] 
##### bd9981cf3bef66ad
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 2 
74- Persian 
75-
76- Toggle Persian subsection 
77-
78- 2.1 
79: Etymology 
80-
81- 2.2 
82- Pronunciation 
83-
84- 2.3 
85- Adjective 
86-
87- 2.3.1 
88- Derived terms 
89-
90- 2.3.2 
91- Descendants 
92-
93- 2.4 
94- References 
95-
96- 3 
97- Urdu 
98-
99- Toggle Urdu subsection 
100-
101- 3.1 
102- Pronunciation 
103-
104- 3.2 
105: Etymology 1 
106-
107- 3.2.1 
108- Adjective 
109-
110- 3.3 
111: Etymology 2 
112-
113- 3.3.1 
114- Noun 
115-
116- 3.4 
117- References 
118-
119- 3.5 
120- Further reading 
121-
##### e4879b84bd66d091
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.4 
74- References 
75-
76- Toggle the table of contents 
77-
78- پوییدن 
79-
80- 3 languages 
81-
82- فارسی 
83- Malagasy 
84- Русский 
85-
86- Entry 
87-
--
141: Etymology
142- [ edit ] 
143-
144- Inherited from Middle Persian [Book Pahlavi needed] ( pwd- /⁠pōy-⁠/ , “ to run ” ) . [ 1 ] 
145-
146- Pronunciation
147- [ edit ] 
148-
149- Vocalised Persian: پویِیدَنْ 
150-
151- ( Classical Persian ) IPA ( key ) : /poː.jiː.ˈdan/ 
152-
153- ( Dari, formal ) IPA ( key ) : [pʰoː.jiː.d̪án] 
154-
155- ( Dari, formal ) IPA ( key ) : [pʰoː.jiː.d̪án] 
156- ( Kabuli ) IPA ( key ) : [pʰoː.jiː.d̪án] 
157-
158- ( Hazaragi ) IPA ( key ) : [pʰʊː.ji.d̪án] 
159-
160- ( Iran, formal ) IPA ( key ) : [pʰuː.jiː.d̪ǽn] 
161-
162- ( Tajik, formal ) IPA ( key ) : [pʰɵ.ji.d̪án] 
163-
164- Rhymes: -an 
165-
166- Readings
```


## [2026-09-14T00:57:24.400Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### pahn\"; sed -n '255,330p' 9860df93f781b106.txt; echo \"#### pak\"; sed -n '150,250p' bd9981cf3bef66ad.txt"
}
```


### [2026-09-14T00:57:24.459Z] TOOL RESULT

```
#### pahn
 [ edit ] 

 پهن • ( pehn ) 

 wide , broad 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( pʾhn' /⁠pahn⁠/ , “ wide, broad ” ) , from Proto-Iranian *páθana- , from Proto-Indo-European *peth₂- ( “ to stretch out, to spread out ” ) (Pokorny). Compare Avestan 𐬞𐬀𐬚𐬀𐬥𐬀- ( paθana- , “ spacious ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈpahn/ 

 ( Dari, formal ) IPA ( key ) : [pʰäɦn] 

 ( Dari, formal ) IPA ( key ) : [pʰäɦn] 
 ( Kabuli ) IPA ( key ) : [pʰɑːn] , [pʰɑːm] 

 ( Hazaragi ) IPA ( key ) : [pʰɔːn] 

 ( Iran, formal ) IPA ( key ) : [pʰæɦn] 

 ( Tajik, formal ) IPA ( key ) : [pʰäɦn] 

 Rhymes: -ahn 

 Readings

 Classical reading ? 

 pahn

 Dari reading ? 

 pahn

 Iranian reading ? 

 pahn

 Tajik reading ? 

 pahn

 Adjective
 [ edit ] 

 پهن • ( pahn ) ( comparative پهن‌تَر , superlative پهن‌تَرین ) 

 wide , broad 
 Synonym: پت و پهن ( pat-o-pahn ) 
 Antonym: باریک ( bârik ) 

 Derived terms
 [ edit ] 

 پت و پهن ( pat-o-pahn ) 
 پهنا ( pahnâ ) 
 پهناور ( pahnâvar ) 

 Descendants
 [ edit ] 

 → Ottoman Turkish: پهن ( pehn ) 

 Etymology 2
 [ edit ] 

 Pronunciation
 [ edit ] 
#### pak

 Entry 

 Discussion 

 English 

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

 See also: باک , باگ , and تاک 

 Central Kurdish
 [ edit ] 

 Etymology
 [ edit ] 

 From Proto-Iranian *pawHākáh , from Proto-Indo-Iranian *pawHākás , from Proto-Indo-European *pewH- .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /paːk/ 

 Adjective
 [ edit ] 

 پاک ( pak ) 

 clean , pure 
 Synonym: خاوێن ( xawên ) 

 chaste 

 innocent , clean-handed , sinless 

 Derived terms
 [ edit ] 

 پاکانە ( pakane ) 
 پاکداوێن ( pakdawên ) 
 پاکژ ( pakij ) 
 پاکی ( pakî ) 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( pʾk' /⁠pāk⁠/ , “ clean, pure, holy ” ) , from Proto-Iranian *pawHākáh , from Proto-Indo-Iranian *pawHākás , from Proto-Indo-European *pewH- ( “ to cleanse, purify ” ) . Cognate with Sanskrit पावक ( pāvaká , “ pure, clean, clear ” ) , Latin purus .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈpaːk/
```


## [2026-09-14T00:57:40.030Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"paθana\\|patane\\|petalon\\|pandō\\|pandere\\|Avestan\\|Persian\" 06d3df39dc8cf7f3.txt | head -30; echo \"=== petalon ===\"; sed -n '100,200p' 1ec856bc8fff65ff.txt"
}
```


### [2026-09-14T00:57:40.086Z] TOOL RESULT

```
=== petalon ===
```


## [2026-09-14T00:57:42.460Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 06d3df39dc8cf7f3.txt 1ec856bc8fff65ff.txt; head -30 06d3df39dc8cf7f3.txt; echo ===; head -20 1ec856bc8fff65ff.txt"
}
```


### [2026-09-14T00:57:42.515Z] TOOL RESULT

```
Exit code 1
180 06d3df39dc8cf7f3.txt
168 1ec856bc8fff65ff.txt
348 total
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pet%CA%B0%E2%82%82-
FETCHED: 2026-09-14T00:57:17Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found(eval):1: == not found
```


## [2026-09-14T00:57:50.095Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peth%E2%82%82-\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%AD%CF%84%CE%B1%CE%BB%CE%BF%CE%BD\" \\\n \"https://en.wiktionary.org/wiki/purus\" \\\n \"https://en.wiktionary.org/wiki/%CF%83%CF%80%CE%B5%CF%8D%CE%B4%CF%89\" \\\n \"https://www.etymonline.com/word/pan\" \\\n \"https://www.etymonline.com/word/passport\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 401 verification\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T00:57:56.529Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peth%E2%82%82-
/home/sfmqrb/git/rishe/data/verification/sources/web/3a35249c451a9ae5.txt
### https://en.wiktionary.org/wiki/%CF%80%CE%AD%CF%84%CE%B1%CE%BB%CE%BF%CE%BD
/home/sfmqrb/git/rishe/data/verification/sources/web/0cebd89b238f1856.txt
### https://en.wiktionary.org/wiki/purus
/home/sfmqrb/git/rishe/data/verification/sources/web/a11383e21ec8e50b.txt
### https://en.wiktionary.org/wiki/%CF%83%CF%80%CE%B5%CF%8D%CE%B4%CF%89
/home/sfmqrb/git/rishe/data/verification/sources/web/9b2ff0421aa04f8d.txt
### https://www.etymonline.com/word/pan
/home/sfmqrb/git/rishe/data/verification/sources/web/15423e4fb5fcf5aa.txt
### https://www.etymonline.com/word/passport
/home/sfmqrb/git/rishe/data/verification/sources/web/cd81aeb410af2b73.txt
```


## [2026-09-14T00:57:58.851Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 3a35249c451a9ae5 0cebd89b238f1856 a11383e21ec8e50b 9b2ff0421aa04f8d; do echo \"##### $f\"; grep -c \"\" $f.txt; done"
}
```


### [2026-09-14T00:57:59.987Z] TOOL RESULT

```
##### 3a35249c451a9ae5
286
##### 0cebd89b238f1856
466
##### a11383e21ec8e50b
447
##### 9b2ff0421aa04f8d
1713
```


## [2026-09-14T00:58:01.963Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### peth2\"; sed -n '120,286p' 3a35249c451a9ae5.txt | grep -v \"^ *$\" | head -80"
}
```


### [2026-09-14T00:58:03.045Z] TOOL RESULT

```
#### peth2
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
 Existing in variations, *pet- , *peth₁- , *peth₂- . [ 1 ] 
 Root
 [ edit ] 
 *peth₂- 
 to spread out 
 to fly ( through the sense ‘spread one’s wings’ ) 
 Alternative reconstructions
 [ edit ] 
 *pet- [ 2 ] 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *peth₂- (69 c, 0 e) 
 *péth₂-e-ti ( thematic root present ) 
 *pe-póth₂-e ( stative ) 
 Proto-Indo-Iranian: *papā́ta 
 Proto-Indo-Aryan: *papā́ta 
 Sanskrit: पपात ( papā́ta ) 
 *pí-pth₂-e-ti ( reduplicated thematic present ) 
 Proto-Hellenic: *píptō 
 Ancient Greek: πίπτω ( píptō ) , πῑ́σσω ( pī́ssō ) — Aeolic Greek: πέφτω ( péfto ) 
 *pt-né-h₂-ti ~ *pt-n-h₂-énti ( nasal-infix present ) [ 3 ] 
 Ancient Greek: πίτνημι ( pítnēmi ) 
 Proto-Italic: *pandō ( “ to spread ” ) ( see there for further descendants )
 *pot(h₂)-éye-ti [ 4 ] 
 Proto-Indo-Iranian: *pāt(H)áyati 
 Proto-Iranian: *pāt(H)áyati 
 Sanskrit: पातयति ( pātáyati , “ to cause to fly, throw, send; to cause to fall, fell; to spill, pour ” ) 
 *péth₂-lom ( “ leaf ” ) 
 Proto-Hellenic: *pétalon 
 Ancient Greek: πέτᾰλον ( pétălon ) ( see there for further descendants )
 Proto-Germanic: *feþlą ( see there for further descendants )
 Proto-Indo-Iranian: *pátram 
 Proto-Indo-Aryan: *pátram 
 Sanskrit: पत्र ( pátra , “ leaf ” ) , पत्त्र ( pattra ) ( see there for further descendants )
 Proto-Iranian: *pátram 
 Avestan: 𐬞𐬀𐬙𐬀𐬭𐬆𐬙𐬀 ( patar ə ta , “ winged ” ) 
 *péth₂-r̥ ( “ feather, wing ” ) ( see there for further descendants )
 Unsorted formations 
 Proto-Albanian: *peta 
 Albanian: pjetë 
 Proto-Armenian: [ 5 ] [ 6 ] 
 Old Armenian: ընթանամ ( əntʻanam ) 
 Proto-Celtic: *ɸanssā 
 Old Irish: éis 
 Irish: éis 
 Proto-Germanic: *faþmaz ( see there for further descendants )
 Hellenic:
 Ancient Greek: πετάννῡμι ( petánnūmi ) , πέτασος ( pétasos ) , πέτηλος ( pétēlos ) , ποταμός ( potamós ) , πότμος ( pótmos ) , πετηνός ( petēnós ) , πτῶμα ( ptôma ) , πτῆσις ( ptêsis ) , πτῶσις ( ptôsis ) , πτωτικός ( ptōtikós ) , πτωτός ( ptōtós ) , πτίλον ( ptílon ) , πατάνη ( patánē ) 
 Italic:
 Latin: pateō ( see there for further descendants )
 Latin: patera ( see there for further descendants )
 Latin: passus ( “ step ” ) ( see there for further descendants )
 ⇒ Latin: impetus , praepes , perpetuus ( see there for further descendants )
 ⇒ ? Latin: propitius ( see there for further descendants )
 ⇒ Latin: petulans , petulcus ( see there for further descendants )
 References
 [ edit ] 
 ^ Sihler, Andrew L. ( 1995 ), New Comparative Grammar of Greek and Latin , Oxford, New York: Oxford University Press, →ISBN , § 122a.note1 
 ^ Mallory, J. P. with Adams, D. Q. ( 2006 ), The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World (Oxford Linguistics), New York: Oxford University Press, →ISBN , page 181 
 ^ De Vaan, Michiel ( 2008 ), “ pandō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 442 
 ^ Kulikov, Leonid ( 2014 ), “Causative Formation”, in Giannakis, Georgios K., editor, Encyclopedia of Ancient Greek Language and Linguistics ‎ [1] , volume 1, Leiden, Boston: Brill, →ISBN , page 275 
 ^ Klingenschmitt, Gert ( 1982 ), Das altarmenische Verbum (in German), Wiesbaden: Dr. Ludwig Reichert Verlag, pages 114–115 
 ^ Rix, Helmut , editor ( 2001 ), “*peth₂”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 479 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/peth₂-&oldid=92171574 "
 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European CeCH-shaped roots 
 Hidden categories: Pages with etymon
```


## [2026-09-14T00:58:10.022Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### petalon\"; grep -n -B2 -A12 \"From πετ\" 0cebd89b238f1856.txt | head -40; echo; echo \"#### purus\"; grep -n -A12 \"Latin\\b\" a11383e21ec8e50b.txt | grep -n -A12 \"pewH\\|puə\\|pūrós\\|Etymology\" | head -40"
}
```


### [2026-09-14T00:58:10.090Z] TOOL RESULT

```
#### petalon

#### purus
6:62- Etymology 
7-63-
8-64- 1.2 
9-65- Pronunciation 
10-66-
11-67- 1.3 
12-68- Adjective 
13-69-
14-70- 1.3.1 
15-71- Declension 
16---
17-175: Latin
18-176- [ edit ] 
--
20:178- Etymology
21-179- [ edit ] 
22-180-
23:181- Etymology tree
24-182-
25:183- Proto-Indo-European *pewH- 
26-184- Proto-Italic *pūros 
27-185: Latin purus 
28-186-
29:187: From Proto-Italic *pūros , from Proto-Indo-European *pewH- ( “ to cleanse, purify ” ) [ 1 ] (whence also Latin putus , Latin pius ).
30-188-
31-189- Pronunciation
32-190- [ edit ] 
33-191-
34-192: ( Classical Latin ) IPA ( key ) : [ˈpuː.rʊs] 
35-193-
36-194- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈpuː.rus] 
37-195-
38-196- Adjective
39-197- [ edit ] 
40-198-
41-199- pūrus ( feminine pūra , neuter pūrum , comparative pūrior , superlative pūrissimus , adverb pūrē or pūriter ) ; first / second-declension adjective 
--
76:392: Latin terms derived from the Proto-Indo-European root *pewH- 
77-393: Latin terms inherited from Proto-Indo-European 
78-394: Latin terms derived from Proto-Italic
```


## [2026-09-14T00:58:13.247Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A14 \"^ Etymology$\" 9b2ff0421aa04f8d.txt | head -40"
}
```


### [2026-09-14T00:58:14.371Z] TOOL RESULT

```
176: Etymology
177- [ edit ] 
178-
179- From Proto-Indo-European *spewd- ( “ to press, hurry ” ) . [ 1 ] Cognate with Albanian punë , Lithuanian spáusti , Old Armenian փոյթ ( pʻoytʻ ) .
180-
181- Pronunciation
182- [ edit ] 
183-
184- IPA ( key ) : /spěu̯.dɔː/ → /ˈspeβ.ðo/ → /ˈspev.ðo/ 
185-
186- ( 5 th BCE Attic ) IPA ( key ) : /spěu̯.dɔː/ 
187-
188- ( 1 st CE Egyptian ) IPA ( key ) : /ˈspew.do/ 
189-
190- ( 4 th CE Koine ) IPA ( key ) : /ˈspeβ.ðo/ 
--
1450: Etymology
1451- [ edit ] 
1452-
1453- Learned borrowing from Ancient Greek σπεύδω ( speúdō ) . [ 1 ] 
1454-
1455- Pronunciation
1456- [ edit ] 
1457-
1458- IPA ( key ) : /ˈspe.vðo/ 
1459-
1460- Hyphenation: σπεύ‧δω 
1461-
1462- Verb
1463- [ edit ] 
1464-
```


## [2026-09-14T00:58:19.044Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A10 \"pan (n.)\" 15423e4fb5fcf5aa.txt | head -25; echo \"#### passport\"; grep -n -A10 \"passport (n.)\" cd81aeb410af2b73.txt | head -25"
}
```


### [2026-09-14T00:58:19.116Z] TOOL RESULT

```
56: pan (n.) 
57-
58- "broad, shallow vessel of metal used for domestic purposes," Middle English panne , from Old English panne , earlier ponne (Mercian) "pan," from Proto-Germanic *panno "pan" (source also of Old Norse panna , Old Frisian panne , Middle Dutch panne , Dutch pan , Old Low German panna , Old High German phanna , German pfanne ), probably an early borrowing (4c. or 5c.) from Vulgar Latin *patna. This is supposed to be from Latin patina "shallow pan, dish, stew-pan," from Greek patane "plate, dish," reconstructed (Watkins) to be from a suffixed form of PIE root *pete- "to spread."
59-
60- But both the Latin and Germanic words might be from a substrate language [Boutkan]. Irish panna probably is from English, and Lithuanian panė is from German.
61-
62- The word has been used of any hollow thing shaped somewhat like a pan; the sense of "head, top of the head" is by c. 1300. It was used of pan-shaped parts of mechanical apparatus from c. 1590; hence flash in the pan (see flash (n.1)), a figurative use from early firearms and the "pan" that held the priming. To go out of the (frying) pan into the fire "escape one evil only to fall into a worse" is in Spenser (1596).
63-
64- pan (v.2) 
65-
66- "follow with a camera," 1913 shortening of panoramic in panoramic camera (1878). Meaning "to swing from one object to another in a scene" is from 1931. Related: Panned ; panning .
--
78: "to wash (gravel or sand) in a pan in search of gold," 1839, from pan (n.); thus to pan out "turn out, succeed" (1868) is a figurative use (the expression in the literal sense of "yield gold when washed out in a pan" is by 1849). The meaning "criticize severely" is from 1911, probably from the notion in contemporary slang expressions such as on the pan "under reprimand or criticism" (1923), probably from the notion of being roasted or fried. Related: Panned ; panning .
79- also from 1839 
80-
81- Entries linking to pan 
82-
83- flash (n.1) 
84-
85- 1560s, "sudden burst of flame or light," from flash (v.); originally of lightning. Figuratively (of wit, laughter, anger, etc.) from c. 1600. The meaning "period occupied by a flash, very short time" is from 1620s. The sense of "superficial brilliancy" is attested from 1670s. The meaning "first news report" is from 1857. The comic book character dates to 1940. The meaning "photographic lamp" is from 1913. Flash cube is by 1965.
86-
87- panoramic (adj.) 
88-
--
117: also dish-pan, "pan in which dishes are washed," 1858, from dish (n.) + pan (n.). Dishpan hands "inflamed or sore hands caused by housework" is attested by 1935, an advertiser's phrase. In 1922, Lever Brothers began to advertise Lux in this country to "rid your hands of that dis
#### passport
23: passport (n.) 
24-
25- c. 1500, passe-porte , "authorization to travel through a country," from Old French passeport "authorization to pass through a port" to enter or leave a country (15c.), from passe , imperative of passer "to pass" (see pass (v.)) + port "port" (see port (n.1)). The original sense is obsolete; the meaning "document issued by competent civil authority granting permission to the person named in it to travel in or out of a country or authenticating his right to protection while abroad" is from 1540s. In early use often indicating principally the right to leave one's country.
26- also from c. 1500 
27-
28- Entries linking to passport 
29-
30- pass (v.) 
31-
32- late 13c., passen (transitive), "to go by (something)," also "to cross over," from Old French passer "to pass" (11c.), from Vulgar Latin *passare "to step, walk, pass" (source also of Spanish pasar , Italian passare ), from Latin passus "step, pace" (reconstructed to be from PIE root *pete- "to spread").
33-
```


## [2026-09-14T00:58:27.419Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && for w in \"پهن\" \"پاک\" \"پویید\" \"پو \"; do echo \"=== $w ===\"; grep -n \"$w\" ARY_pages.txt | head -6; done"
}
```


### [2026-09-14T00:58:28.390Z] TOOL RESULT

```
=== پهن ===
=== پاک ===
88:کوج کردهاند. طی این کوج‌های متوالی؛ آریایی‌ه با بومیان هر محل درآمیختند و در نتیجه پاک و
94:این نوادپرستان حتی «اسلاوهاء که به زبان‌های هند و اروپایی تکلم می‌کنند از نظر «پاکی نژادی»
789:سنگ نوشته‌هایی به الفبای رونیکك (۹17210) از آنها در شمال اروپاکشف شده است. این زبان در,
2247:۱ واژه‌های "رد" و "ارت" و "ارنا" در ارستایی به معنی "پاکی" و "تقدس " و "جای مقدس" نیز به کار فه‌اند.
4459:بازگست بد: پاکه.
7487:چم این واژه در زبان آلمانی: بزم برپاکردن.
=== پویید ===
5295:پوی» پوییدن (به چم / ۱۸۱
=== پو  ===
819:(8 70277۸1۸37 یشتر نوشتارهای تخاری عبارتند از ترجمه‌ی منون پو دایی که به الفبای هندی
7999:آلمانی (0870/۸): 7181 9 (188) پو ین
```


## [2026-09-14T00:58:29.231Z] TOOL CALL #54: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B3%D8%A7%DA%98/\" --note \"page 401 entry0 node5: Persian pâsâž from French passage\" 2>&1 | tail -2"
}
```


### [2026-09-14T00:58:31.662Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/345079f784f0897b.txt
```


## [2026-09-14T00:58:35.369Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '5288,5305p' ARY_pages.txt; echo \"=== find leaf ===\"; python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:5294])\nimport re\n# find last [pdf page N] before\nm=[x for x in re.finditer(r'\\[pdf page (\\d+)\\]', t[:off])]\nprint('pdf page', m[-1].group(1) if m else None)\nEOF"
}
```


## [2026-09-14T00:58:36.084Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"پاساژ\" 345079f784f0897b.txt | head -20"
}
```


### [2026-09-14T00:58:36.500Z] TOOL RESULT

```
ساکسونی کهن (543:007 صا0): 71 برهان قاطع : ۹ ۴۲۵
فریزی کهن (الها5ل۲ صا0): 0
ا
یادداشت,
به احتمال زباد واژه‌ی "پوده" (برهان قاطع :: ۴۲۵) هم از همین واجربشه است.
افغانی (پشتو) (4۳011۸1): 6 ولظ سانسکریت (5(/5217):
[pdf page 180]
پوی» پوییدن (به چم / ۱۸۱
مته208 ,-[۲87 لهستانی (0/5/4): ۸۴ ۳۷5
ارمنی (915710): ۳64 ,۲06 روسی (815314): ۳۸7
بونانی (0880): 0 ,۴33110۸ چکه (2807)): ‎٩‏ مها
لاتین ((11ا): ش۸آل ۳87 بشاآن ۲851 آترنی (لتی) (4701491)):
آلمانی (057417): نداد ۳۵۲8 رونام
انگلیسی کهن (201(/5 ضان): پروسی کهن (۳۸۷554۸ ۰:00 88138
8 ,تا
انگلیسی (8701-7370): ۳ پسگشت‌ها 5
دانمارکي (0۸(۷1317): ۳57 48 ۶08۵3
سوئدی (817521/53[7): انا 0 (۳5۴) + همه
=== find leaf ===
pdf page 180
```


### [2026-09-14T00:58:36.563Z] TOOL RESULT

```
4:TITLE: پاساژ - معنی در دیکشنری آبادیس
6:پاساژ - معنی در دیکشنری آبادیس 
10: پاساژ
13: مترادف پاساژ : بازارچه، تیمچه، راهرو، گذرگاه، معبر
21: پاساژ. ( فرانسوی ، اِ ) بازار سرپوشیده که دو در دارد دخول و خروج را. 
39: پاساژ (موسیقی). بخش ( به انگلیسی: Section ) در موسیقی، یک طرح موسیقایی کامل اما غیرمستقل است. انواع بخش شامل: پیش درآمد یا مقدمه، درآمد یا گشایش، تکرار و مرور، آواز، کر، فرجام، خاتمه یا سررسید و اتمام آهسته است. برخی از قطعات شناخته شده تنها از یک یا دو بخش ساخته شده اند. 
40:گذر[ ۱] یا پاساژ ( به انگلیسی: Passage ) طرحی موسیقایی ست، که می تواند از لحاظ استقلال کامل باشد یا نباشد. [ ۲] 
41:در لغت به معنی گذر است. در موسیقی اصطلاحی است برای جمله ای کوچک یا بزرگ که نقش آن برای پیوند یا ارتباط دو قسمت موسیقی است. گاهی پاساژها جنبه ویرتئوزیته به خود می گیرد که نوازنده برای نشان دادن مهارت، استفاده می نماید. در موسیقی ردیف گذرها یا پاساژها معمولاً برای ارتباط بین دو جمله یا دو گوشه موسیقی استفاده می شوند. [ ۳] 
42: wiki: پاساژ (موسیقی) 
48: پاساژ (passage)
49:در موسیقی، اصطلاحی غیرفنی که به تکه ای از قطعۀ موسیقی با طول متغیر اشاره دارد؛ این تکه معمولاً قسمت کوتاهی است که با یک خصوصیت ملودیک یا ساختاری منفرد، مشخص و متمایز شده است. wikijoo: پاساژ 
58: راهرو، تصویب، قطعه، گذرگاه، روی داد، نقل قول، عبور، معبر، سیر، عبارت، انقضاء، گذر، پاساژ، اجازه عبور، حق عبور، کار کردن مزاج، عابر، ممر، سفر دریا، عبارت منتخبه از یک کتاب
76: پاساژ ؛ مفاهیمی که در درون این کلیدواژه نهفته است ؛ ( پاسبانی یا پاسگاهی یا پست دادن در یک پاسارگاد ، پاسخ دادن ، عبور یا گذرگاه و انتقال یا ارسال و فرستادن و کنترل و محاسبه ) یعنی ارسال و انتقالی که همراه با نگهبانی و مراقبت و دیده بانی و محاسبه شده در محل عبور و مرور باشد. 
78:ریشه ی اصلی کلمه ی پاساژ، پاس می باشد. و مفهوم پاس اشاره به یک جریان سیال و پاسکال با حرکت رو به جلو و رو به پیشرفت در یک کال جریان دار را دارد. جهت تایید این مطلب اصطلاح پس از آن در مکالمات در حال استفاده می باشد. که کلمه ی پس در اینجا در جایگاه های کاربردی مختلف اشاره به پیش رو و جلو و آینده دارد. یا اصطلاح پس پریروز به مفهوم روزی که از آن عبور کردیم و به پیش افتادیم. و اصطلاح پس انداز به مفهوم پس انداختن برای آینده.
```


## [2026-09-14T00:58:49.184Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]', t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\nprint(d[180][:1800])\nEOF"
}
```


## [2026-09-14T00:58:50.112Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"پهنا\\|بهن\\|پهن\" ARY_pages.txt ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T00:58:50.443Z] TOOL RESULT

```
پوی» پوییدن (به چم / ۱۸۱
مته208 ,-[۲87 لهستانی (0/5/4): ۸۴ ۳۷5
ارمنی (915710): ۳64 ,۲06 روسی (815314): ۳۸7
بونانی (0880): 0 ,۴33110۸ چکه (2807)): ‎٩‏ مها
لاتین ((11ا): ش۸آل ۳87 بشاآن ۲851 آترنی (لتی) (4701491)):
آلمانی (057417): نداد ۳۵۲8 رونام
انگلیسی کهن (201(/5 ضان): پروسی کهن (۳۸۷554۸ ۰:00 88138
8 ,تا
انگلیسی (8701-7370): ۳ پسگشت‌ها 5
دانمارکي (0۸(۷1317): ۳57 48 ۶08۵3
سوئدی (817521/53[7): انا 0 (۳5۴) + همه
نروژی (۵/07(7501۸(۷+ ۳05۸ 1 (855) :0008
هلندی (01704): 7 ,80 لغت‌نامه دهخدا: ‏ ۵۶۶۵ و ۵۸۰۳ و ۵۶۶۳
اسلاوی کهن (ع1/ما5 8677 7ل) (0): برهان قاطع 9 ۴۸
1 ها فرهنگ معین : دیا دنا هرن
بادداشت:
چم کلی واژه‌های اين فهرست: دمیدن» دم آهنگری» بادکردگی» بادکردن؛ تاول.
پپلوی (/تماتنمم: ۰ ۳0۷1911۲10 ,20 نروژی (077501۸/: ۳05۸
سانسکریت. (54۸5507): لینرانی (40۷لهلابط7ل):
9 ,8۳738۷۸۷۸7 71 5۳۸100
آرمنی (/(۸۵15): - اد دا ما آلبانی (۵۸اللهقلهم. االزا یا
یونانی 6۶۵8/0): ۰ 8۳81700 ,87300
الاتین (710)(شاید) ار ان پسگشت‌ها 5
۱ ایسلند ی کیره (۸0 ۲ باباایی 5 صا۵): 998999 ۶080800
+ 8۳07۸ ,87707 9 ,13 (ن81) :18 2/(قکل ۸/۸
نورس گهن (ت۸08 0ا0): ار ان 8 (878) 51
ساکسونی کهن ((2430 ۰:00 8۳107 اراد و( :لح 2 هگا
آلمانی کهن (0872/۸2 07اب 82102:0120 برهان قاطع ؛ ۴7۹
آلمانی (028۵۷): 35 فرهنگ معین + ۸۴۳-۴
انگلیسی کهن (20/08/8 02: 8۳03۷۸0۷ لغت‌نامه دهخدا : ۳ و ۵۸۲۵
```


### [2026-09-14T00:58:50.497Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:59:10.346Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HUB pak/pahn ==\"; grep -n \"pāk\\|pak \\|pahn\" HUB.txt | head -10; echo \"== NYB ==\"; grep -n \"pahn\\|pāk\\b\\|pāk \" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T00:59:10.414Z] TOOL RESULT

```
== HUB pak/pahn ==
652:mit* (Min. Gl. 25, Shk. 232), phi. *apak (in apakth
1582:372. Arm. tapak heisst 'Bratpfanne' und ist = phi. fapak^ arab.
2513:683. Arm. zipak (spat belegt) wird moderne Schreibweise fiir
2904:1st phi. sSpak von mir und Darmesteter richtig fiir
2905:s(a)pak der Ausgabe (Phi. Vd. 207, Z. 6 und 7 v. u.)
3103:864. Np. kulba = kurba *Bude' aus phi. "^kurpak = arm.
3104:krpak 'Werkstatt, Laden, Schenke', Apg. 28, 15 u. s. w.,
3539:1015. Dazu arm. LW. anapak ungemischt, rein (vom Wein).
3547:arm. napak 'Moschusbeutel' (bei Moses, Geogr. ed.
3620:(Miller p. 74) aus phi. *napak 'gehort', geht auf den
== NYB ==
439:and [’nd] so much, so many: én ~ this much 64°; all this, all these 351. 623. 6572.24; hac én ~ sal apāc since so many years 1674; han ~ dušman all these ene- mies (sg. as with numerals) 249; 10426, 11923; — ~ cand as much (big, large, high, etc.) as: 3119-15, 935. (935 without ~); ~ cand yašt-ē (as much as =) at least some ceremonies 659; — hän <... cand as much (many, long, ete.) as 92°. 997. 10027, 10324-25; 2 ~ dranäi pahnāi cand han i nn hast twice the length (and) breadth of it as it is now 10024-25; 7000 han ~ cand
490:lapik [’p’k] helper, pl. cas. obl. —-àn (used as a cas. rect.) 1069. — < *upäka-, subst. derived from *upānk-, v. apäc (2) and the next w.; Skr upäka ‘adjacent, neighbouring’; v. also apākēk.
497:apākēh [’p’kyh] 1. company; pat ~ together 5712, — 2. backward movement: pat ~ back 418; v. pat-apākēnītan. — 3. help, assistance 5919-20, 729-26 (opp. ha- mēstārēh). — V. lapāk and ?apäk. Paz. āvāgī. V. also apar-apākēh.
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
1289:dit [TW B, inscr. TWB] 1. the second, the other: rēc i ~ 83; či 1 ~ the other 12118; &vak apāk ~ 104?* etc. ;évak 6 (61) ~ 1009-13 ete. — 2. adv., also ~-ic, for the second time, again 46*3 etc.; further, then 515; back P2:10; — 1116 v. dit. — Shortened from **ditī < *ditīya-, SW form of Olr *dvitiya- ‘second’, OP duvitiya-, Gath. Av. (963sg.) daibitya- for *dbitiya-; MPrs dwdy = dudi for *didi through in-
1330:drahm [ZWZN] a silver coin, the drachm 68. 119%, — From Gr špaxun. In Sassanian time its weight was 4.25 gr. silver. drahnai [dlhn?y], dranäi [dln’y] length 6514, 9616, etc. — From draž; the form is influenced by pahnäi (q. v.). Paz. dranäe (SGV).
1883:handixtan [hnd*htn'] handdc- 1. apāc ~ to bring together again, to reunite, with apāk ‘with’: apāk apastak apāc handāxt reunited (them) with the Avesta 1091, 11119-20, — 2. to measure, to calculate (the horoscope) 7$. — 3. impers.: api-m
1934:*hārēftan [h'lyptn'] *hārēf-; [h'lyp-] 1. to mix, referring to the coition 4315: after ēvak apar, apāk dit, apar ēstāt hend 6 én kar 4314-15 (v. ?apük 2) the narrator continues api-šan MDM hareft: as the construction is pass. we expect here a subj.; this is probably hidden in MDM which is, in that case, the wrong ideogr. for aw. ’pl = "pr or ?c] = "cr, or the like, signifying ‘the genital fluid’ : the fluids from their genital organs were mixed together, with the gl. kū-šān pat takoš (g. v.) frac grift ‘that is: they clasped tightly’. — 2. to infect: api-š 61 dit Zartuxst pas andarg haxt ka hārēft ēstāt purr gaz (etc.) and Z. saw her from behind, between her thighs, (and saw) that they were in- fected, full of snakes (ete.) 5726-581, — 3. to attach, to assign a th. to (6) a p,: whenever Pourušāsp desires to have a divine service ‘performed yazišn 6 yas- taran härefät he shall assign the service to (true) ministrants 5314-15, with the gl. ki 6 yazāt ke apāyet yastan that is: that one shall perform the divine service to whom it pertains to perform such service’, ef s. v. bahr. — (1483) ham.raedwayeiti ‘to mix, to mingle, to infect’, from which the signi- fication ‘to attach’ was easily derived (cf the simplex vb. in the expression kahrpam raēdwayeiti ‘assumes a visible shape’ Yt. 813); a den. of rae0wa- ‘mixture, muddle’. *ham-ra- > hara-, cf (1529) rgroma- < *ramrama- (the Av. spelling ham- is a compromise between hq- and ham-); *har- in Milr > har-. The Milr vb. be- longs to the NW linguistic area: raēdw- > réf- is a normal NW development. As the vb. is a den., the pres. st. kārēf- must be regarded as the primordial form, and
2131:jāyišn [y?dšn'], 70!? jahišn [yhšn'] For- tune, luck, dispensation 2?!. 145; ~ u zaman <i> brihenišn rād 14'?, v. zaman; murvāk ~ i névak augury (and) good Fortune (i.e., good Fortune revealed through augury) 18!; pat névak ~ <u> yazdän hayyārēh with good fortune and the help of the gods 121-4; 121°; pat ~ hayyārēh i pat martömän xrat veh For- tune (giving aid to =) favouring men, wisdom is the best thing [she gives] 7012-13, Skr. v. siddheh sahāyatāyai ma- nusyanam buddhih uttamā; cf ke [for ka] ~ hayyär pat martömän cis + xrat veh when Fortune (is a helper to =) favours men, wisdom is the best of things PT 675-5, with the explanation cé hakar par- kast xvāstak be šavēt aivāp cahārpād be mirét xrat bē mānēt for if wealth dwindles and is lost or animals die wisdom remains; pātixšāi han névaktar i... xrat u dānišn nēvak api-$ ~ hayyäreh apāk that ruler
2220:kārēcār [k'lyc'l] battle, combat 1198, with: ~ % 8?9, 4 apäk 108%; pat ~ bē dzatan to kill in battle 9722; ~ xtinrécisnéh (q.v.) 1312-13, kéasisn u kārēcār 901; ~ kartan to fight 25-29, passim. 511. 95!1; vas ~ u ozanišn apāk ... kart 138-4; ~ dästan to keep contending, wrestling 329-19; be 0 m~ ìi... šutan to engage in battle with 9617-18 ete. — MPrs kryer, krer (S); Paz. kārīžār, NP kürzür; käre- cas. obl. of kar < OP kära- ‘army’, + cär from Av. (449) 5kar- ‘to move’, cf NP caridan ‘to graze’ and vicar-.
```


## [2026-09-14T00:59:11.520Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW pando ==\"; grep -n \"pandō\\|pando,\\|patina\" LEW_1910.txt | head -8; echo \"== LAT ==\"; grep -n \"pando\\|passus\\|patina\\|purus\" LAT.txt | head -10"
}
```


### [2026-09-14T00:59:11.576Z] TOOL RESULT

```
== LEW pando ==
== LAT ==
26604:une ^chelle, un escalier; marche (pour le differencier de passus)":
27331:duitate forsitan mille quingentos passus, cf.Lofstedt, Komment.
39623:appellatur lautus et purus. En realite, il semble qu'il y ait eu deux
40628:nifds*, nefandus, nSfSrius, nSf astus, neparcunt, ne pus glos<? non. purus,
41177:nepus ( u?):non purus, P.F.163,15* Si la glose est exacte, nepus
41179:skr. putah, d'une racine *pewa-/pu-, qu'on a dans purus . Le second
44837:pando
44878:pando, -is, pandi (attestA seulement par Priscien et dans les
44891:4,3). M.L.Ci93. De IA pando,-ds: [s 1 ]inflechir; repandus : retrouss< 5 ,
44899:passus, -a, -um: ouvert, £cart 4 ; usite surtout dans 1'expression tech-
```


## [2026-09-14T00:59:14.482Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '44878,44915p' LAT.txt; echo \"=== purus ===\"; grep -n \"^purus\\|purus, -a, -um\" LAT.txt | head -5"
}
```


### [2026-09-14T00:59:14.550Z] TOOL RESULT

```
pando, -is, pandi (attestA seulement par Priscien et dans les
composes; ne semble pas employA par les auteurs. La forme A redou-
blement pe-pend-i aura AtA AvitAe par suite de son homonymie avec
le pf. de pends), passum (et forme analogique pSnsum, de IA Pansa
"qui marche les pieds ecartes", surnom romain, et les doublets dispes-
sus et dispSnsus), pandere: etendre, deployer, Acarter; par suite
"ouvrir" (en Acartant, different de aperire "ouvrir en Stant un cou-
vercle, operculum "). UsitA de tout temps. Conservi dans quelques
dialectes italiens, cf. M.L.6189.pangB
848
Derives et composes en pand- et en pass-i pandus, -a, -um (est a pandt),
comme -legus a legS: ecart 4 , qui s'onTre; par suite "dejete, evase,
inflechi, arrondi, concave", epithete d'une deesse, Dea Panda (Arn.,
4,3). M.L.Ci93. De IA pando,-ds: [s 1 ]inflechir; repandus : retrouss< 5 ,
d'ou repandirostrus (Pac.); Pandana porta dicta est Romae, quod semper
pateret , P.F.246^ 15; pandex : qui semper pandit ora ad potandum, CGL
V 607,15; de la pandiculus d^u provient le denominatif: pandiculor,
-aris: -ri dicuntur qui toto corpore oscitantes extenduntur, eo quod
pandi fiunt, P.F.246,16, cf.M.L.6191; pandicularis: dicebatur dies
idem et communicarius, in quo omnibus dis communiter sacrificabatur,
P. F.346,18.
passus, -a, -um: ouvert, £cart 4 ; usite surtout dans 1'expression tech-
nique passa uua "raisin sec" (qui s r e st fendille en s^chant au soleil),
d'ou passum (ac.ulnum) "vin de raisins secs", M.L.6370; et 6305
pansus ; passim adv. : en se repandant fa et la; en desordre; passdrius,
-a,-um: — ficus "figue etalee et sech^e au soleil" (tardif); passdles:
— et oues et gallinae appellantur quod passim pascuntur, P.F.349,4;
passiuus: qui se trouve 9A et la, r^pandu, commun (b.lat.), conservi
dans une fexpression sarde, cf.M.L.6369; passus,-us m. (et tardif,
passus,-i): proprement "ecartement des jambes", d'ou "espace compris
entre cet ecartement; pas; mesure de longueur". Panroman. M.L.6371.
Celt.: iri. pass, spass, cassan. De la *passdre attestd par les 1 .
romanes, M.L.6267, compassdre 3095, *expassSre 3033, etc.
De pando: dispando: 4 tendre en tous sens, ecarteler (pcp. dispessus
Lucr.); expando, M.L.3030, et 3031 *expandicare', oppando (< 5 poq. imp . ) ;
praepando', repand 5 (Apul.)j prSpansus (id.).
Pas d'«Stymologie claire, a moins qu'on ne rapproche pate5 et qu f on
n'admette, dans la racine, une alternance entre dentale sourde et
=== purus ===
51127:purus, -a, -um: pur, sans tache, sans souillure; et "pur de";
```


## [2026-09-14T00:59:20.671Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '51127,51160p' LAT.txt"
}
```


### [2026-09-14T00:59:20.726Z] TOOL RESULT

```
purus, -a, -um: pur, sans tache, sans souillure; et "pur de";
par suite "net, sans m<?lange", "exempt de". L'adjectif appartient
surtout k la langue religieuse; cf. plus bas l'emploi et le sens
de purare et purimenstriS . Correspond exactement k gr. xocGoipoc. — An¬
cien, panroman (sauf roumain), M.L.G8G4. Celt.: iri. cirptir; britt .pur.- 9C7 “
pusus
D 4 riv 4 s: puro, -as,-are (= xaBoapoo), supplant 4 i l' 4 poque historique
par purgB, pUrifico, mais conserve dans une glose de Festus, 354,y,
prophetas in Adrasto Iulius nominat antistites fanorum, oraculorumque
interpretes (3): 11 cum capita uiridi lauro uelare inperant prophetae,
sancta ita caste qui purant sacra ", et qui est atteste par le temoi-
gnage des langues romanes, M.L.68g7 et 3S76a depurare; c£. aussi
impuratus, populaire, employe comme terme d'injure par Plaute et
Terence, et repris par Apule e; pure (superlatif puri me atteste
dans Fest., P.F.301,7 purime tetinero: purissime tenuero), conserv 4
en roman avec le sens de "seulement 11 , M.L.6858; puriter; puritas
(rare et tardif d'aprbs xaBapoTric), M.L.6860; purefacio (Non.); puri-
ficus, pUrific 5 ,-ficatio,-ficatSrius ( 4 poq.imp.); impurus, impuritia,
-tas; purimenstrio: esse dicuntur qui sacrorum causa toto mense in,
caerimoniis sunt, i.e. puri sint certis rebus carendo, Fest.398,13.
Sur putus et nepus, v. ces mots.
Lat. piirus appartient a la racine dissyllabique de akr.pavitdi
"celui qui purifie", pavitram "instrument de purification", putah
"purifie", punati "il purifie". C'est un terme de la langue religieuse
qui, comme nombre d'autres de mSie genre, s'est perdu ailleurs. Le
mot celtique, irl.i Ir, gall.tr "vert, frais", que l'on a rapprocbe,
est pareil pour la forme a purus; le sens serait explicable i la
rigueur. Cf. peut-8tre nepus; mais le rapprocbement de putus fait
difficult 4 .
Le rapport entre purare et purgare rappelle celui qui existe entre
iurB et iurgdre; mais dans ce dernier couple, les sens ont diverge.
pQs, puris n. (pl. pUra dans Plin.): pus. S'emploie aussi comme
terme d'injure (Lucii., Hor.). M.L. 6865.
D 4 riv 4 s: purulentus (d 4 jA dans Cat.); d'ou purulentia (tardif);
```


## [2026-09-14T00:59:28.229Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT ==\"; grep -n \"^Petal\\|Petal,\\|^Pan,\\|Pan, a\\|^Pure\\|Pure,\\|^Pass\\|Pass,\" SKT.txt | head -12"
}
```


### [2026-09-14T00:59:28.293Z] TOOL RESULT

```
== SKT ==
13384:Passover.  (L.-Gk.-Heb.) *  \^  faj<ka.  -»  Ck.  waax^'^ ing  over ;  the  pa^sovcr  ; .^Hth.pdra^A.ht  passed  over, dash,  (Scand)  Swed.  dial, ibblc  in  water,  Norweg.  /foslitf water,  tumble,  work  hard  : Dan.  daske,  to  sUp,  boxes,  to haksQ^  to  box:  tee  Box  (,.l)> is  a  mere  vaiiaul.     Aud  see
15194:Pure.  (F.-L.)  F.  pur.  masc,  pttn^ fern.,  pore.  —  L. /wrwj,  pure.  Cf.  Skt,/i/, to  purify.     fVPU.)
```


## [2026-09-14T00:59:30.157Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC ==\"; grep -n \"petalom\\|petālom\\|petanā\\|speudō\\|speud\" IEC.txt | head -12; echo \"== SYN ==\"; grep -n \"12.61\\|BROAD, WIDE\\|CLEAN\\b\" SYN.txt | head -10"
}
```


### [2026-09-14T00:59:30.220Z] TOOL RESULT

```
== IEC ==
16825:speudó (sph-) ‘press, urge, hasten’. Cf. spheutó. WP II, 659. (Var. speust-) Arm. cf. put'am, v. Chur, fr. *speust-, cf. Li. spaüstas ‘pushbutton’ and spaüste, f. stamp, franker’); out. gs: puto, o-st. ‘haste, zeal’; Alb. cf. fus, aor: futa, v. ( thrust’, fr. *speutio, sph- but *speudio possible); MBr. cf. füden, f. ‘fright’; Cor. (?) foes, f. (fortune, fr. *speust-?); W ffwd, m. (*dash, haste’, fr. *spu- tos) beside ffull, pl. -ion, m. id. (fr. a type *speudlios, cf. Li. spaudulýs, gs: -io, m. *pres- sure"); (o-gde in) Li. spáudZiu, inf. spáusti, v. “press, squeeze’. (Isophonic: OHG epioz OS spiot, OE spéot, ON spjót, Sw. spjut, n. ‘lance, javelin’)
16895:spoudà (spud-) “pressure, haste’. WP II, 659. Cf. speud- and next Gk. spoudé, f. ‘haste, zeal'; Li. spaudá, f. “press?
16896:spoustos (theme: spoud-, cf. speud-) Arm. Gut, gs: puto, o-st. ‘haste, effort’; Li. spáustas, pp. “pressed, printed”; spaustùvas, m. 'screw-press'
16981:spüd- (sphüd-) ‘stab; dart, dash forth, thrust'. Cf. speud-, spoud- Alb. (ambig.) fus, aor. futa, v. (thrust", from speud- or sputio); Du. spuiten, tr. ‘inject; intr. ‘spurt’; ME spouten, v. ‘spout; Sw. sputa, v. id.; Li. spüdZiu, spüdéti, v. (“have stitch in the side: ON spýta, v. inf. ‘to skewer’; mod. ‘to spurt’). Nominal types: Du. spuit, f. ‘squirt, jet, waterspout'; Li. spüdus, adj. ‘tight; spüdis, gs: spüdZio, m. ‘squeeze’
16989:(sput-, sphut-, cf. speud-, spoust-. Ambig. in Alb. fus, aor. futa, v. ‘thrust’; fútje, f. ‘thrust’; cf. W ffwd, m. ‘impulse, dash, rush’; ffwdan, f. ‘bustle, fuss’. Isophone in W ffwtog, f. ‘docked tail, stump of tail
17312:-stos (-stom) (1) noun-formant, extending verbal root, giving an active mng. Cf. Av. basto (“bundle?: bhendh-); Per. baste ‘bound’; Arm. Gut. gs; put'o (“haste, zeal: speud-); Alb. bisht (*tail': bhid-); Go. maíh- stus, m. (dung': migh-); Du. mest, G Mist, id.; E. Du. mist (fog: migh-); G. EM dunst, Du. dons, OE düst (vapour: dhum-); Go. lustus (/desire': Iubh-); MHG list, sm. & sf. id.; luste, adj. “pleasant? (see next); OHG herbist, sm. (harvest, autumn": kárp-); G Rost (rust: rudh-); MHG last, sm., OE hlæst, sn. (“bur- den": cf. OHG. OE hladan, sv. 6); OCS otü- pustü ((remission': paus-); Cz. rost, m. Cgrowth': ordh- or ard-); Li. spaüstas (“press- button’: speud-)
== SYN ==
1269:now the common generic word (muir prevailing in the name of special seas, as the Irish Sea, etc.) etym. disputed the old comparison with Ir. ferg ‘anger’ and the dxeavds Ovepyotvos of Ptolemy is phonetically difficult. Stokes 273. ’ Ber- gin, Eriu 3.86. Pedersen 2.669 f. Walde- P. 1.289. Perh. best taken as fr. *foirsge : fairsiung ‘wide’ (12.61). So Thurney- sen, Z. celt. Ph. 11.312, Gram. 95.
20181:1. Fr. emprunter, Rum. tmprumuta (the latter also ‘lend’), fr. VLat. *im- promituare, deriv. of Lat. promituwm ‘a loan’ (epd. of mutwum, cf. 12.61). REW 4319. Gamillscheg 354.
22043:2. Lat. latus (> It. lato, Sp. lado, OFr. lez, Rum. arch. laturi), prob. fr, another grade of the root in Lat. latus ‘wide’ (12.61). Walde-P. 2.497. Walde- H. 1.772. Otherwise Ernout-M. 598.
22232:NHG weit, fr. adj. weit ‘spacious, far’, OHG wit ‘spacious, wide, broad’, general Gmc. in latter sense (12.61). Develop- ment fr. ‘it is a wide distance to B’ to ‘it is far to B’, and then also ‘B is far’, only NHG and still partially distin- guished fr. fern. Paul, Deutsches Wtb. 639.
22509:discussed here, seem to have some such di central notion, see under Grk. navies et ‘thin, sparse’ (12.66). we Be LONG | Lith. ilgas ) Lett. gar’§ yo ChSl. | dliigit SCr. dug Boh. dlouhy me an dlinnyj : ar Sep sn : Av. daraga-, mas- bel me ‘hi 4. Sp. largo, fr. Lat. largus ‘abundant? (cf. Fr. large, ete. ‘broad’, 12.61). 5. Ir. cian ‘long, far, distant’, as sb. ‘long time’, etym.? Deriv. fr. pron, Gi stem in Ir. cé ‘this’, Grk. éxet ‘there’, No Lat. -ce, etc. (Stokes 75, Rozwadowski, i Quaest. gram. 10) not convincing. I,
22562:12.61 WIDE, BROAD
22805:2. Derivs. of IE *pela-, *pla- with no- tion of ‘spread out flat’, seen in Lith. ploti ‘flatten’ etc., also in several words for ‘wide, broad’ (12.61). Walde-P. 2.61, 90f., 99f. Ernout-M. 776. REW 6581, 6586. Falk-Torp 230.
25880:15.87 CLEAN
27322:s 15.87 CLEAN kabapd XBaphs Goth. hrains Lith. Svarus, Gystas mundus Aas ON hreinn Lett. firs, glits Bulilo, netio Dan. ren ChSl.  Sistit Propre, net Sw. ren SCr. ist limpig OE cl@ne Boh. Gisty curat ME lene Pol. czysty glan NE clean Russ. éistyj glan Du. rein, zuiver Skt.  cuddha- glan OHG  reini, subar Av. ‘ ue MHG reine, siiber
```


## [2026-09-14T00:59:35.493Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22562,22600p' SYN.txt | head -50; echo \"=== search pahn in SYN ===\"; grep -n \"pahn\\|paθana\\|pathana\" SYN.txt | head"
}
```


### [2026-09-14T00:59:35.553Z] TOOL RESULT

```
12.61 WIDE, BROAD
Grk. — xAarts, ebpts Goth. braibs Lith. platus
NG tAatts, papdbs ON bretdr, vidr Lett. plats
Lat. latus Dan. bred, vid ChSl. Srokit
It. largo Sw. bred, vid SCr. Sirok
Fr. large OE° brad, wid Boh. &Siroky
Sp. ancho ME brood, wid Pol. _—szeroki Rum. lat (larg) NE wide, broad Russ. Srokij
Ir. lethan, fairsiung Du. _ breed, wijd Skt. prthu-, uru- NIr. — leathan OHG breit, wit Ay. poradu-, padana- W. Ulydan, eang MHG breit, wit
Br. ledan NHG breit
Words for ‘wide, broad’ rest on the more general notion of ‘spread out, spa- cious, extensive’, and the specialization to extent in a given direction, that is ‘wide’ in distinction from ‘long’ and the opposite of ‘narrow’, is only partial. For all of them may also be used in the more general sense. In the two Gmc. groups represented by NE broad and wide the wider sense is generally stronger in the Second group, and dominant in NHG
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
weit, which is no longer used as the oppo- site of eng ‘narrow’, while, conversely, NE wide is the technical term in actual measurement (e.g. siz inches wide by three feet long).
1. IE *pjtu-, *pjino-, etc., fr. an ex tension of *pel- (*pela-, *pla-, etc.) De words for ‘spread out, flat’ as Lat. pla- nus ‘flat’, ChSI. polje ‘field’, OB feld ‘field’, ete. Walde-P. 2.99f., 61f. Thurneysen, Gram. 129, 131.
polly lethan, Nit. leathan,
ork. teal 1 an (beside W. led, Be
f. llyda ns Lith. platus, Lett. plats; spread ny. poragu-; Arm. lian.
+yru-, etc., root con-
(in cpds. as vouru- bays’, vouru-gao-
yal (possessiD 3 Byz, NG gapdis, orig. dub. G. Meyer Neugr. Stud. 4.94, connects with NG dial. papéos ‘large (meal-)bag ; jggnword fr. Ital. fardo or its source Amb, farda ‘bundle of goods’. Hatzi- dakis, Mec. 2.29, suggests deriv. fr, digpadts with semantic extension through ‘copious in speech’ > ‘wide’ in gneral. But the actual use of the rare dgpadjs connotes skill, rather than
copiousness, of speech.
4, Lat. latus (> Rum. lat), prob. fr. ‘ulatos (cf. stlatta, Festus) : ChSl. sttlati ‘spread out’, stelt, postelja ‘bed’. Walde- P, 2.643, Ernout-M. 527f. Walde-H. 1.172,
Tt. largo, Fr. large (Rum. larg ‘exten- Sve, spacious’, but under influence of Fr. large Sometimes used for lat ‘wide’, cf. Tiktin s.v.), fr. Lat. largus ‘abundant, ‘pious’, etym.?  Ernout-M. 524. Walde-H. 1.764. REW 4919,
DP. ancho, fr. Lat. amplus ‘large, spa-
SP ATIAL RELATIONS: PLACE, FORM, SIZE
Digitized by Arya Samaj Foundation Chennai and eGangotri
885
cious, abundant’, etym.? Ernout-M. 47. Walde-H. 1.42. REW 4380.
5. Ir. lethan, etc., above, 1.
Ir. fairsiung, W. eang ‘broad, ample’, epds. (Ir. for-ess-, W. ess-) of *enghi-, etc. : OE enge ‘narrow’, etc. (12.62). Walde- P. 1.62. Pedersen 2.10.
6. Goth. braibs, ON breidr, OE brad, etc., general Gmc.; cf. Goth. us-braidjan ‘spread out’, etc., OHG breta ‘the flat hand’, etym. dub. Walde-P. 2.194. Falk-Torp 100. Feist 104.
ON vidr, OF wid, etc., general Gmc., except Goth., perh. fr. *wi-ito-, epd. of *wi- ‘apart, away’ (Skt. v-, etc.) and pple. of IE *ei- ‘go’ (Skt. 7-, Grk. eft), in form = Skt. vita- (vi-ita-) ‘gone, lack- ing, without’, but with development of ‘gone apart’ to ‘extensive, wide’. Walde- P. 1.108. Falk-Torp 1373.
7. Lith. platus, Lett. plats, above, 1.
8. ChSl. Sroku (reg. for wAarbs in Supr., Ps.; in Gospels Mt. 7.13 for etpi- xwpos, while warts is rendered by pro- strani, lit. ‘spread out’ = SCr. prostran ‘extensive, spacious’) etc., general Slav- ic, etym.? (Brickner 547 : Goth. skeirs ‘clear’, etc. improbable.)
9. Skt. prthu-, Av. parafu-, above, 1. Skt. uru-, above, 2.
Av. pasana- (with 6 for ¢ fr. paradu-), NPers. pahn: Grk. werdvviy: ‘spread out’, Lat. patére ‘stand open’, pandere ‘spread out, open’. Walde-P. 2.18.
12.62 NARROW
z 4 ae Gath. aggwus Bh Saabs ankélas an, N rengr, engr ett. Saurs trl Dan. ed, trang, smal ChSl.  qziikit, tésnit boy Helo Sw. smal, trdng SCr. _uzak, tjesan estrecho, ango OE nearu, enge, smal Boh.  tizky, tésny rime, ing ae ME ___narowe, streit, smal Pol.  wazki, ciasny Oil, cumun NE narrow Russ. uzkij, tesnyj cumhang, he Du. nauw, smal, eng Skt.  anhu-, avistirna-
» CUfyng OHG engi, angi, smal Av. sm at
K, striz MHG enge, smal
=== search pahn in SYN ===
22596:Av. pasana- (with 6 for ¢ fr. paradu-), NPers. pahn: Grk. werdvviy: ‘spread out’, Lat. patére ‘stand open’, pandere ‘spread out, open’. Walde-P. 2.18.
```


## [2026-09-14T00:59:45.345Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read()\nb=t.split('\\f')\nprint(len(b))\nfor i,x in enumerate(b[:40]):\n    if 'pet' in x or 'peu' in x:\n        print('---leaf',i, x[:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T00:59:46.484Z] TOOL RESULT

```
725
---leaf 5 (pais?): pis- „zerstaiDpfen, zermalmen^^                      (bes.   Gretreide);   zum    Sachlichen      vgl. Meringer AYS. I 3ff.   Ai. pind^i             „zerreibt,        zerstampft'^   (3, pi.  
---leaf 10 6                                        panq      pal-    Z.    gr.            mit Unrecht als ursprgl. angenommenen Bed. j,be-             Lautg. 7 If.                                     sie ist nu
---leaf 11                                               palia-q     pasto-   {^ipaXa „das Zupfen“              acpdco „beruhre^^, FickBB. 28, 102, B^eclitel LeviL 336), xpakkco „schnelle (die Saite, die  Sehne 
---leaf 14 10                                                        peig-   und peik   berger BB. 27, 176   zwei ursprgl. ganz versch. Sippen anzunehmen, einer- seits „inalen, biint“ (nach Bezz. „das Aufreifien
---leaf 15                                          peiiri(i-)   — peu-                                          11   Fick III^ und Vf. aaO.), dock ist auch dies ganz unsicher.         Yielfach            — unan
---leaf 16 12                              peu-: p0u-(pau-): pS-   (\\i.piiiuti ^schaumen*’^).   B. bei Pickll^ 53 (die      kelfc.   Worter nicht nach Pedersen KG. I 61 zu            j,anziehen^‘ als j,deckende
---leaf 17                                                     peu-                                                   13   1.  pen- ^reinigen, lautern, sieben^^ (auch set- Basis        pu).    Ai. pavaiEj  pundi
---leaf 18 14                                  peuor, gen. pu-n-es, loc. puueni        Identitat unserer            Wz.                             als „helle sein“ oder „klar machen^^ mit „reinigen^^       hat 
---leaf 19                                         ;                                                     peak- uud peug-                                          5   wandtschaft mit dt. Span (Kretschmer KZ. 3   
---leaf 21                                                                                                                   17   \ 2it.pedo^ -ere, pexl ^^^mmQn^\pecten,-inis               wmh, petenata „pecti- 
---leaf 22                                                                                                       ;     18                                           pet- (peta-)   Gom. pdbas^ hxet pihi ^backen^, 
---leaf 23                                                                                                   ;                                                     pet-                                            
---leaf 24                                                                                                                       ;     ^0                                                             pet-   448 f.
---leaf 25                                               pet-                                           21   sen KZ. 39, 343, 348, -Liden Arm. St. 114,                     Osthoff MU. YI, 18).    Gr. vtio jz£TQi
---leaf 26                                                                                                               ;     22                                                  (ped-) : ped : pSd«    feder“
```


## [2026-09-14T00:59:50.156Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read()\nb=t.split('\\f')\nprint(\"=== leaf 17 (p.13) peu- reinigen ===\")\nprint(b[17][:1600])\nprint(\"=== leaf 22 (p.18) pet- ===\")\nprint(b[22][:1600])\nEOF"
}
```


### [2026-09-14T00:59:51.487Z] TOOL RESULT

```
=== leaf 17 (p.13) peu- reinigen ===
                                                    peu-                                                   13


1.  pen- ^reinigen, lautern, sieben^^ (auch set- Basis        pu).
   Ai. pavaiEj  pundii ^reinigt, lauterfc (sich)^^, pdvitunr,      polar- m.
„Reiniger, Lauterer**^, pacitram „Lauterungsinittel, Seihe, Sieb"^ ^arana-                 ;


„reinigend^^, pdvaka- (und nach der ved. Metrik auch pamkd-) ^,lauter*^
(you fliissigen Dingen, erst spater auch vom Feuer, uud daher keine Stiitze
fur die Verkniipfung des idg. '’^peuor „Peuer“ mit unserer Wz., s, Bartho-
lomae PBrB. 41, 272 a 2)             = mp. pavag^ np.             „lauter,        rein^^       ai.    ptlia-

„rein‘^, piiti-h    f.   ^Reinigung"^
        pUrus ^rein*-^ (Bildung wie da-ru-s)^        alter        -are „reinigeii'*
(daU letzteres nach Thumeysen IF. 31, 2751. vielmehr vom ital. ''^pfir „Feuer*^
abstamme als „durch Feuer rein machen^^ und sioh erst sekundar der
Bed. von purus j,rein^‘ genahrt habe, ist doch sehr unwahrscheinlich gegen                      ;


analoge Auffassung von purus als einer Riickbildung aus purare. das ur-
sprgl. j,durch Feuer reinigen“ gewesen sei, s. Yf. LEWb.^ s. v., Thur-
neysen aaO.); piihis „rein, lupits „non purus*^ (Paul. Fest. aus "^'neputos)^     ;



piifare             putzen“ (k^nxn              =
                                       piitare „schneiden"^, s. pen- ,,schlagen^^),
ahd. foiceyi, mhd. vcRwen „sieben, Getreide reinigen'*^ i^fawjan         ai. pavd-    =
yati ,,reinigt, lautert“).
  Gr. TiTvovj Tixeov jA^urfschaufeP^ [\fowcn, Prellwitz    - s. v.) 
=== leaf 22 (p.18) pet- ===
                                                                                                      ;




18                                           pet- (peta-)


Gom. pdbas^ hxet pihi ^backen^, hretpobet „gebacken“, cy mr, poeth (*q^e-
qHos) „bei6“, bret. poaz „gekocht ‘^5 cymr. poptiryes ^.pistrix^, corn, peber^
bret. pober „Backer‘^; aus lat. coctura stammt air. cuchtar „caupona; Kiiche^^
(das u nach cucann); ags. (Liden IF. 18, 412f.) a-figen „ger6stet^‘;
lit. (umgestellt, s. oben dgro-xoTiog) hepii, 'kepti^ lett. mpt „backen, braten^^,

aber ohne Umstellung apr. pectis „Ofenschaufel“ (nicht in pelih zu andern,
V. Osten-Sacken IF. 33, 239f.)=abg. peUh „Ofen‘‘; abg. pekq, pcsti ds.,

pekii „Hitze^^, poH „SchweiB“ {^poq^to-^ Zupitza KZ. 35, 266).
    Wesentlich nach Curtins 465 f.             —
                                         Uber gr. OTixog „gebraten, gekocht’^
(wohl nicht aus 6 -j- pq^tos) s, Boisacq s. y.

1 .   pet- (pete-) „ausbreiten, bes. die Arme“.
      Av. pa'&ana- „weit, breit^^           fiir t   wohl nach pdre&ii- ds.); gr. jieTdvvvpi
(ijihaoa)^ mxvrjpif mrvco „breite aus‘\               nhaapa „Yorhang, Decke^, Tihaoog
„breitkrampiger Hut“, ntiakog „ausgebreitet“                        (; lat.     patiihis^   ahd. fedel-
gold)^ nexakov „Platte, Blatt“, jzaxdvr] „Schusser^ (ass. aus "^Tiexdvd^ J. Schmidt
KZ.      32,   355 ff.;   daraus   lat.   potincC)^   nExayvov^
                                                     ass. ndxayvov ^^noxrjQtov
IxTihaXov^^ (s. dazu Solmsen KZ. 42, 212f.);      pando, -ere,
```


## [2026-09-14T01:00:01.683Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read()\nb=t.split('\\f')\nfor i,x in enumerate(b):\n    if 'speud' in x.lower() and i>600:\n        print('leaf',i,'|',x[:120].replace('\\n',' '))\nEOF\ngrep -n \"speud\" WLD_Bd2_1927_dli_106624_djvu.txt | head -5"
}
```


### [2026-09-14T01:00:02.860Z] TOOL RESULT

```
leaf 663 |                                    speud- — spek-                           659  „lfager‘ 118 W.         anderer Anschau
42821:speud- — spek- 
42869:ausdehnen*' gleichsetzt, zieht er zu unserm speud- auch ahd. spio^^ aisl.
```


## [2026-09-14T01:00:05.467Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read()\nb=t.split('\\f')\nprint(b[662][-1800:])\nprint(\"=====663=====\")\nprint(b[663][:1200])\nEOF"
}
```


### [2026-09-14T01:00:06.572Z] TOOL RESULT

```
 (fembleibt mnd. 5^i^ew„verdrie6en“ WoodIF. 22, 145) und
(mit t) lit. speiciu, speTsti „umringen“, spieciUy spiestl „schwarmen“, spintu,
spisti „in Schwarmen ausbrechen, von Bienen“ (eigentlich „sich zusammen-
drangen“), lett. spiets „Bienenschwarm“ (mit dem Ptc, lit. spistas ,,ge-
drangt^^ setzte Pick EZ. 19, 253, Yf. LEWb.^ lat. spissus gleich), wobei
die Bedeutung „drangen, pressen“ auch z. T. auf .,ein-, zusammen-spannen‘‘
beruhen mag; vgl. auch lett. spaile, spailis „Strich, Schwaden des Mahers
(die zusammengedrangte Graszeile)“ (-Z- vielleicht aus -dZ'), lit. spieloti
„Zeug in den Eahrahmen einspannen?^, lett. spailes „gespaltener Stecken
zum Einklemmen z. B. einer Schlange, Polter“, spile, spilis „eine Zwicke,
Zwickeisen; Holznagel, die die Bretter der Schiffswand zusammenhalten
gespaltener     Stecken         zum Krebsfang;              Not, Yerlegenheit“      (wie   spruohts
„Klemme“: priezu „8panne“),                   spilis       auch „zeltartig   zum Schutz gegen
die   Sonne ausgespannte Leinwand“,                    spllet   „klemmen—zwicken, spannen^.
   Mit ^-Formantien
                 spaigle „gespaltener Stecken zum Krebsfang, Krebsgaber‘
   lett. spaiglis,
(in  der Anschauung verschieden von spaiguVi, lit. speiglia% unter sp&i-
„8pitz“) ; germ, mit der Bedeutung „ausspannen                           =
                                                       spreizen“ : nhd. mdartl.
spaichen ,,au8schreiten“, etwas ausspaichen „mit Schritten oder ausgespannten
Pingem ausmessen^, norw. mdartl. speika „mit steifen (gespannten) Beiuen
gehn“, spika „widerspenstig sein“ (vgl. oben lett. s^te „Trotz“) ; gr. opiyyco
„sclinure ein, klemme ein‘‘, oipiyxrtjQ „Sclmur, Band; Muske!* (das damit
von Froehde BB. 21, 325 und Persson 399f., 408 f. verglichene aisL sptkr

=====663=====
                                   speud- — spek-                           659

„lfager‘ 118 W.         anderer Anschauung entsprungen, s. u. spei- „spitz“) ;
                  ist wohl

Tielleicht mir. sen „Netz“ (wenn *spig-no- „das ausgespreitete'^ Stokes BB.
19, 108).


spend- „drucken, pressen; iibertragen: mit STachdruck betreiben (urgere
     opus), eilen (s’empresser).
   Gr. onsvdco „spute mich, eile; bemuhe mich, bin emsig, strenge mich
an, strebe; trans, treibe an, beschleunige, arbeite auf etwas eifrig hin‘^,
Gdbed. „drangen, driicken^" noch in anovda^' alexQt^avog Hes. („Morser-
keule" als „Zerdrucker“) ; ojcovdr] „Eile, Hast; Eifer, Bestrebung‘‘, gjtov-
daiog „eilig, eifrig, tatig, fleiBig^,   onovddCco „sich sputen, emsig sein, mit
Eifer betreiben, jemandes Interesse fordern^^;
  Lit. spdiidziu, spdusti „drucken“, iter, spdudyti, spaudd „Presse^‘ usw.,
spudinti „eilen, sich davonmachen^, paspudeti „sicb qualen, sich abmiihen'*
(Pick BB. 29, 197, Bechtel Lexil. 302);
   alb. piine „ Arbeit, Geschaft“ (^spudna, G. Meyer Wb. 357) ; wohl auch
arm. poif^ gen. putoy „Eifer“ (Hiibschmann Arm. Gr. I 501 ; t statt t            =
idg. d durch Ass, an den aspirierten Anlant?
```


## [2026-09-14T01:00:19.776Z] TOOL CALL #70: Bash

```json
{
 "command": "ls site/pages/401.jpg 2>/dev/null || pdftoppm -f 401 -l 401 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg401-401 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-14T01:00:20.996Z] TOOL RESULT

```
site/pages/401.jpg
total 3820
drwx------ 2 sfmqrb sfmqrb   4096 Sep 13 21:00 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    592 Sep 13 20:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  95654 Sep 13 20:53 bqt390_436_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  34040 Sep 13 20:54 bqt390_436_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 124665 Sep 13 20:53 bqt390_662_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  93636 Sep 13 20:53 bqt390_662_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 537986 Sep 13 20:53 bqt390_n436.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527696 Sep 13 20:53 bqt390_n662.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   2291 Sep 13 20:56 c404-empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4255 Sep 13 20:56 c404-patil.png
-rw-rw-r-- 1 sfmqrb sfmqrb  34837 Sep 13 20:57 c404-pest.png
-rw-rw-r-- 1 sfmqrb sfmqrb  46825 Sep 13 20:57 c404-symp2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  34820 Sep 13 20:56 c404-symp.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3627 Sep 13 20:54 crop14-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4873 Sep 13 20:54 crop18-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb  20203 Sep 13 20:57 edit_about.py
-rw-rw-r-- 1 sfmqrb sfmqrb 120893 Sep 13 20:58 pg390b.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  39607 Sep 13 20:58 pg390b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 113843 Sep 13 20:57 pg391big.png
-rw-rw-r-- 1 sfmqrb sfmqrb  18836 Sep 13 20:57 pg391crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  81140 Sep 13 20:57 pg391.png
-rw-rw-r-- 1 sfmqrb sfmqrb  34659 Sep 13 20:58 pg391root.png
-rw-rw-r-- 1 sfmqrb sfmqrb  21174 Sep 13 20:58 pg391sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75438 Sep 13 20:56 pg392.png
-rw-rw-r-- 1 sfmqrb sfmqrb 101976 Sep 13 20:57 pg393.png
-rw-rw-r-- 1 sfmqrb sfmqrb 145431 Sep 13 20:54 pg394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96039 Sep 13 20:53 pg394.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72433 Sep 13 20:54 pg397.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77067 Sep 13 20:55 pg398.png
-rw-rw-r-- 1 sfmqrb sfmqrb  85891 Sep 13 21:00 pg399-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb  45417 Sep 13 21:00 pg399-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb  64776 Sep 13 20:54 pg399.png
-rw-rw-r-- 1 sfmqrb sfmqrb  43498 Sep 13 21:00 pg399-sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb 167174 Sep 13 20:58 pg400big.png
-rw-rw-r-- 1 sfmqrb sfmqrb  24547 Sep 13 20:58 pg400_fa_heli.png
-rw-rw-r-- 1 sfmqrb sfmqrb  23086 Sep 13 20:58 pg400_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  14689 Sep 13 20:58 pg400_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb  32600 Sep 13 20:58 pg400_kasak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  35662 Sep 13 20:58 pg400_kasak3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  22852 Sep 13 20:58 pg400_kasak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79028 Sep 13 20:57 pg400.png
-rw-rw-r-- 1 sfmqrb sfmqrb 136264 Sep 13 20:56 pg404hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71542 Sep 13 20:56 pg404.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63962 Sep 13 20:58 pg405.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63610 Sep 13 20:57 pg406.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79866 Sep 13 20:59 pg407.png
-rw-rw-r-- 1 sfmqrb sfmqrb  21327 Sep 13 20:55 pg408-ampus.png
-rw-rw-r-- 1 sfmqrb sfmqrb  33681 Sep 13 20:55 pg408-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78365 Sep 13 20:54 pg408.png
-rw-rw-r-- 1 sfmqrb sfmqrb     40 Sep 13 20:53 queue.txt
```


## [2026-09-14T01:00:22.667Z] TOOL CALL #71: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/401.jpg"
}
```


### [2026-09-14T01:00:22.692Z] TOOL RESULT

```

```


## [2026-09-14T01:00:34.559Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-401.json'));print(json.dumps(d['entries'][3],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T01:00:37.045Z] TOOL RESULT

```
{
 "root": {
  "name": "Peud, Spheud",
  "lang": "Indo-European",
  "refs": "POK:998",
  "gloss": "to press, hasten"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Old Iranian",
   "refs": "FFD:44",
   "words": [
    {
     "translit": "paud, paud-a",
     "gloss": "to run",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 2,
   "parent": 1,
   "lang": "Pahlavi",
   "refs": "FFD:44",
   "words": [
    {
     "translit": "pôy",
     "gloss": "to run",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  },
  {
   "id": 3,
   "parent": 2,
   "lang": "Persian",
   "refs": "POK:998; ISS:130; MON:826",
   "words": [
    {
     "translit": "pŭ",
     "gloss": "running",
     "script": "پو ( پوی ، پویه ، تکاپو )"
    },
    {
     "translit": "pŭyîdan",
     "gloss": "to walk fast",
     "script": "پوییدن ( پوینده )"
    },
    {
     "translit": "pŭyâ",
     "gloss": "runner",
     "script": "پویا ( پویان )"
    },
    {
     "translit": "pŭyânîdan",
     "gloss": "to make animals go fast",
     "script": "پویانیدن ( پویاندن )"
    }
   ],
   "note": null,
   "quote": {
    "text": "نبد راه بر کوه از هیچ روی - بگشتم بسی گرد او پوی پوی",
    "poet": "Ferdowsî"
   }
  },
  {
   "id": 4,
   "parent": 0,
   "lang": "Greek",
   "refs": "POK:998",
   "words": [
    {
     "translit": "speudo",
     "gloss": "hasten",
     "script": null
    }
   ],
   "note": null,
   "quote": null
  }
 ]
}
```


## [2026-09-14T01:00:58.721Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf8',errors='replace').read()\nb=t.split('\\f')\nfor i in (658,659):\n    print('='*20,'leaf',i,'len',len(b[i]))\n    print(b[i][1500:])\nEOF"
}
```


### [2026-09-14T01:00:59.785Z] TOOL RESULT

```
==================== leaf 658 len 1437

==================== leaf 659 len 1489
```


## [2026-09-14T01:01:18.312Z] TOOL CALL #74: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-14T01:01:18.377Z] TOOL RESULT

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


## [2026-09-14T01:01:20.581Z] TOOL CALL #75: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-14T01:01:20.653Z] TOOL RESULT

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


## [2026-09-14T01:01:54.362Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN pahn ==\"; grep -n \"pahn\" HRN.txt | head -5; echo \"== HUB pahn ==\"; grep -n \"pahn\" HUB.txt | head -5; echo \"== MON pak/pahn ==\"; grep -n \"^پاک:\\|^پهن:\" MON_part1.txt | head -5"
}
```


### [2026-09-14T01:01:54.450Z] TOOL RESULT

```
== HRN pahn ==
3253:aw. pa^ana^ 'weit, breit; phlv. pahan, pahnäi^
3254:pahnäk.
16580:pahnai 344.
== HUB pahn ==
4369:(Aogemad.), zd. duye suite; pahn Veit, 'breit*, zd, pad ana-; phi.
7217:ap. *maidwd7i^ zu zd. ma^dana- ^Wohnung ; pahn *weit',
9652:'Lllnge', pahn-a *Breite*, rOsan-a *Helle' JRAS.
== MON pak/pahn ==
28344:پاک: (ص.) بی آلابش؛ با کبزه» نمازی» 
33713:پهن: ۰ 0200 (رص.) فراخ» گشاد؛ وسیع؛ متد. 
33720:پهن: ۲۱۰ [- پهنه] (.) شیری که به سبب 
33722:پهن: : 006 () (عم.) فضلهةٌ اسب و استر و
```


## [2026-09-14T01:01:59.050Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3248,3258p' HRN.txt; echo \"---leaf---\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n'); off=sum(len(l)+1 for l in lines[:3252]); leaf=t[:off].count('\\f'); print('leaf',leaf,'printed',leaf-21)\nEOF\necho \"=== HUB leaf ===\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n'); off=sum(len(l)+1 for l in lines[:4368]); leaf=t[:off].count('\\f'); print('leaf',leaf,'printed',leaf-10)\nEOF\nsed -n '4365,4372p' HUB.txt"
}
```


### [2026-09-14T01:02:00.320Z] TOOL RESULT

```
343. peJilev, pehletan 'Held'^).
ap. Parfhava-; phlv. pahlav (gehört etwa auch
pahlum hierher?).
344. peh/Ti' 'weit, breit', pehnä.
Käs. pen, pahdn, pan,
aw. pa^ana^ 'weit, breit; phlv. pahan, pahnäi^
pahnäk.
kurd. pän ; af;\ plan ; oss. d. fafan t. fäfdn 'Breite,
breit' (281); bei. patan (289).
345. {i)pei-, Praefix.
ap. patli/ 'zu, gegen etc.'; aw. paiti; phlv. pat-^ pät-
---leaf---
leaf 97 printed 76
=== HUB leaf ===
leaf 135 printed 125
folgenden ai contrahirte a nicht ausfallen konnte.
Ohne Kegel ist der Schwund von inlautendem a in btst
zwanzig, bal. gUt, paz. vTst Min. Gl. 217, afgh. LW. vi5t,
semn. vtst etc., zd. visaiti; duvest zweihundert*, paz. duest
(Aogemad.), zd. duye suite; pahn Veit, 'breit*, zd, pad ana-; phi.
Yazd als Name (arm. Yazd bei Laz. Pharp.) und in Namen
{Yazdpanah etc.) = zd. yazata-; np. yazdan 'Gott*, paz. yaz-
dan Min. Gl. 220, eigentlich plur. von yazd = zd. yazata-
```


## [2026-09-14T01:02:06.510Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:13:00.486Z] TOOL CALL #78: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-401.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\ndata = {\n \"pdf_page\": 401,\n \"book_page\": 371,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------- ENTRY 0 : Pet 2 ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Pet 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *peth₂- 'to spread out' (Pokorny 824 '1. pet-, petə- ‚ausbreiten’, bes. die Arme'; Watkins/AHD 'petə-. To spread')\",\n \"note\": \"Nourai's headword, language label, gloss and page citation are all exact. Pokorny IEW p.824 heads the entry '1. pet-, pet-, petə- ‚ausbreiten’, bes. die Arme' and lists under it Av. paθana-, Gr. πετάννυμι / πέταλον / πατάνη, Lat. pateō, pandō, passus, Germ. *faθmaz. Nourai's numbering 'Pet 2' answers Pokorny's 1. pet- 'spread' (his 'Pet 1' is Pokorny's 2. pet- 'fly, fall', p.826); modern handbooks (Rix LIV 479, Wiktionary, De Vaan) merge the two into one root *peth₂- 'to spread out; (hence) to fly', so the split Nourai inherits from Pokorny is now usually abandoned — but nothing on this chart depends on it.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *peth₂- «گستردن، پهن کردن» است که پوکورنی در صفحهٔ ۸۲۴ با سرواژهٔ «1. pet-, petə- ausbreiten» آورده و واتکینز نیز در پیوست ریشه‌های AHD همین را با معنای «to spread» ثبت کرده است. نام ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همه درست است. تنها نکته آنکه تقسیم پوکورنی به دو ریشهٔ pet- «پهن کردن» و pet- «پریدن» در پژوهش امروزی (ریکس LIV، دِ‌وان، ویکی‌واژه) برافتاده و هر دو را یک ریشه می‌دانند. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peth%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:824\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt (printed p.824-825, between the page numerals '824' and '825'): 'I. pet-, pet-, petə- ‚ausbreiten’, bes. die Arme. Av. paθana- ‚weit, breit’ (das θ- nach pərəθu- ds.); gr. … πέταλον n. ‚Platte, Blatt’, πατάνη f. ‚Schüssel’ (aus *πετάνā; daraus lat. patina ds.); lat. pateō, -ēre … dazu pandō, -ere ‚öffne, breite aus’ … passus m. ‚Schritt, Klafter’. WP. II 18.' Every branch Nourai draws is on that page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 18 (WLD_Bd2_pages.txt leaf 22, running head 'pet- (petə-)')\", \"stance\": \"supports\",\n    \"note\": \"'1. pet- (petə-) ‚ausbreiten, bes. die Arme’. Av. pa’θana- ‚weit, breit’ (θ für t wohl nach pəreθu- ds.); gr. πετάννυμι … πέταλον ‚Platte, Blatt’, πατάνη ‚Schüssel’ … daraus lat. patina; lat. pando, -ere' — the source Pokorny 824 abbreviates.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. petə-\", \"stance\": \"supports\",\n    \"note\": \"'petə-. To spread. … 3. Variant zero-grade form in nasalized form *pat-no- probably in Latin pandere (past participle passus < *pat-to-), to spread out: PACE¹, (PAS), (PASS), PASSIM; EXPAND, REPAND. 4. Suffixed form *pet-alo- in Greek petalon, leaf: PETAL. 5. Suffixed form *pet-ano- in Greek patanē (? < *petanā), platter, “thing spread out”: (PAELLA), PAN¹, PATEN … [Pok. 1. pet- 824.]' — Nourai's whole chart in one line.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 12.61 'wide, broad', pp.884-885\", \"stance\": \"supports\",\n    \"note\": \"'Av. paθana- (with θ for t fr. pərəθu-), NPers. pahn: Grk. πετάννυμι ‚spread out’, Lat. patēre ‚stand open’, pandere ‚spread out, open’. Walde-P. 2.18.'\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"pathana, perethu\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Avestan paθana- adj. 'wide, broad, spacious' (Y.10.4 səm pərəθwīm paθanām; Yt.10.95) is a -na- adjective of the root, and Bartholomae AiW cols. 843-844 s.v. paθana- 'breit, weit' himself carries the chain forward: 'np. pahn, oss. fätän ‚breit’. — Pū.: pahan.' That half of the node is correct. The second word is not: Av. pərəθu- 'wide, broad' (fem. pərəθwī) is the exact cognate of Sanskrit pṛthú- and goes back to *pl̥th₂ú-, i.e. to the quite different root *pleth₂- 'flat, broad' (Pokorny p.833 'plet-, plət- ‚breit und flach; ausbreiten’'; Buck 12.61 §1). The two roots touch only in that Pokorny and Walde-Pokorny explain the unexpected θ of paθana- (for regular *patana-) as analogical after pərəθu- — a contamination, not a derivation. Nourai has evidently read that note as licence to put both words in one box.\",\n \"derivation_fa\": \"صورت اوستایی paθana- «پهن، فراخ» واقعی است و بارتولومه در فرهنگ ایرانی باستان (ستون ۸۴۳) خود آن را به «پهن» فارسی نو و pahan پهلوی پیوند می‌دهد. اما واژهٔ دوم، pərəθu- «پهن»، از این ریشه نیست؛ هم‌ریشهٔ pṛthú- سنسکریت و بازماندهٔ *pl̥th₂ú- از ریشهٔ *pleth₂- «پهن و هموار» (پوکورنی ۸۳۳) است. پوکورنی و والده تنها می‌گویند که ثِ در paθana- (به جای *patana-) بر قیاس pərəθu- پیدا شده، یعنی همگونی قیاسی، نه اشتقاق. پس نیمی از این خانه درست و نیمی نادرست است — ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:824\", \"status\": \"partial\",\n    \"note\": \"p.824 has only 'Av. paθana- ‚weit, breit’ (das θ- nach pərəθu- ds.)'. pərəθu- itself is entered nine pages later, p.833: 'ai. pṛthú-, av. pərəθu- ‚weit, breit’' under 'plet-, plət- ‚breit und flach; ausbreiten’'. So POK:824 supports pathana but contradicts the inclusion of perethu.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 843-844 s.v. paθana-\", \"stance\": \"supports\",\n    \"note\": \"'j. paθana- Adj. (fem. -nā-) ‚breit, weit’ … Vgl. zu pərəθway-. — np. pahn, oss. fätän ‚breit’. — Pū.: pahan, Sū.: pahulah.' Bartholomae only 'compares' (vgl.) pərəθu-, he does not equate the two.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 12.61, p.885\", \"stance\": \"contradicts\",\n    \"note\": \"Buck lists 'Skt. pṛthú-, Av. pərəθu-' under §1 'IE *pl̥tu-, *pl̥tno-, fr. an extension of *pel-' and puts 'Av. paθana- (with θ for t fr. pərəθu-), NPers. pahn' in a separate paragraph with Gr. πετάννυμι / Lat. pandere. Explicitly two roots.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 18\", \"stance\": \"partial\",\n    \"note\": \"'Av. paθana- ‚weit, breit’ (θ für t wohl nach pəreθu- ds.)' — same wording, same restriction.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"pahn\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Iranian *páθana- (Av. paθana-) > Middle Persian pahn [pʾhṅ' /pahn/] 'wide, broad' (MacKenzie CPD s.v.), with the regular Middle Persian treatment of intervocalic -θ- > -h- and subsequent syncope of the unstressed vowel (*paθana- > *pahan > pahn); Hübschmann, Persische Studien p.125 cites exactly this word as an example of the loss of an internal a. New Persian پهن pahn continues MP unchanged, and the chart's bracketed derivatives are the regular abstracts: پهنا pahnā 'width' < MP pahnāy (Horn no.344 'phlv. pahan, pahnāi, pahnāk'), پهنه pahne 'expanse, surface'.\",\n \"derivation_fa\": \"«پهن» از فارسی میانهٔ pahn ، از ایرانی باستان *páθana- (اوستایی paθana-) است. ثِ میان‌واکه‌ای در فارسی میانه به هِ بدل شده و سپس واکهٔ کوتاه پایانی افتاده است: *paθana- > *pahan > pahn؛ هوبشمان (پژوهش‌های فارسی، ص ۱۲۵) همین واژه را نمونهٔ حذف الف میانی آورده است. مکنزی نیز pahn «پهن، فراخ» و pahnāy «پهنا» را در فرهنگ کوچک پهلوی ثبت کرده و هرن (شمارهٔ ۳۴۴) صورت‌های pahan و pahnāi و pahnāk را. مشتقات «پهنا» و «پهنه» هم همین ستاک‌اند. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:433\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt form-feed leaf 659 is printed p.433 (its footnote block opens 'بقیه از صفحهٔ ۴۳۲'); it carries the headwords پهنا and پهنه — exactly the two bracketed derivatives on Nourai's chart — while پهن itself ends the preceding page 432 ('وبسکون ثانی معروف است که پشت و پخش وعریض باشد' with an etymological footnote marker). Mo'in's footnote itself is unreadable in this OCR and no page image of Borhan vol.1 p.433 exists in the local library (tools/ref_page.py BQT:433 answers 'no scan covers printed page 433').\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.65\", \"stance\": \"supports\",\n    \"note\": \"'pahn [pʾhṅ' | N ~] wide, broad. ~āy [-’d | N —ā] width, breadth.'\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no.344, p.76\", \"stance\": \"supports\",\n    \"note\": \"'344. pehn ‚weit, breit’, pehnā. … aw. paθana- ‚weit, breit’; phlv. pahan, pahnāi, pahnāk. kurd. pān; afġ. plān; oss. fätän.'\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.125\", \"stance\": \"supports\",\n    \"note\": \"listed among words showing loss of an internal a: 'pahn ‚weit, breit’, zd. paθana-'.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. پهن\", \"stance\": \"supports\",\n    \"note\": \"'پهن: [pahn] (ص.) فراخ، گشاد، وسیع، ممتد' (MON_part1.txt line 33713) — same gloss as the chart.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"pandere; passus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin pandō, pandere 'to spread out, open' is the nasal-infix present of the root, *pat-n-o- beside stative pateō 'to stand open' (Pokorny 824 explains the t : d alternation as an old athematic inflection, after Kuiper, Nasalpräs. 163; Wiktionary/De Vaan set up Proto-Italic *pandō < *pt-né-h₂-ti). Its participle is passus < *pat-tos, and from the participle comes the noun passus, -ūs, which Ernout-Meillet (p.848) define as 'proprement ‚écartement des jambes’, d'où ‚espace compris entre cet écartement; pas; mesure de longueur’' — i.e. the 'step, pace' of the chart, and the Roman pace of five feet. Nourai's parenthesis '(walk)' on pandere is his own shorthand for that development, not a Latin meaning.\",\n \"derivation_fa\": \"فعل لاتین pandō/pandere «گستردن، گشودن» ستاک حالِ میان‌افزودهٔ خیشومی این ریشه است (*pt-né-h₂-ti) در کنار pateō «باز بودن». صفت مفعولی آن passus (از *pat-tos) است و از همین صفت، اسم passus «گام» ساخته شده که ارنو-میه‌یه (ص ۸۴۸) معنای اصلی‌اش را «فاصلهٔ گشودن دو پا» می‌داند. پس هر دو واژهٔ این خانه درست است و ادعای نورایی پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peth%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:824\", \"status\": \"supports\",\n    \"note\": \"'lat. pateō, -ēre ‚sich erstrecken, offenstehen’; dazu pandō, -ere ‚öffne, breite aus’ (der Wechsel t : d erklärt sich durch alte athemat. Flexion nach Kuiper, Nasalpräs. 163), passus m. ‚Schritt, Klafter’.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, DELL p.848 s.vv. pando, passus\", \"stance\": \"supports\",\n    \"note\": \"'pando, -is, pandi … passum … pandere: étendre, déployer, écarter; par suite ‚ouvrir’ … passus,-us m. … proprement ‚écartement des jambes’, d'où ‚espace compris entre cet écartement; pas; mesure de longueur’. Panroman.' E-M add the caution 'Pas d'étymologie claire, à moins qu'on ne rapproche pateō'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. petə- §3\", \"stance\": \"supports\",\n    \"note\": \"'Variant zero-grade form in nasalized form *pat-no- probably in Latin pandere (past participle passus < *pat-to-), to spread out'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 18\", \"stance\": \"supports\", \"note\": \"'lat. pando, -ere' listed under 1. pet- with pateō and passus.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box (it is blank on the printed page too): the Romance stage between Latin passus and the modern words. Vulgar Latin built a denominative *passāre 'to step, walk' on passus (Ernout-Meillet p.848: 'De là *passāre attesté par les langues romanes, M.L.6267, compassāre 3095'), whence Old French passer (11th c.), the deverbal noun passage (12th c., 'act of passing; way through'), the compound passe-port (15th c., 'permission to pass through a port') and compas < *com-passāre 'to pace out together'.\",\n \"derivation_fa\": \"این خانه در کتاب نیز تهی است و تنها مرحلهٔ فرانسوی را نشان می‌دهد. در لاتین عامیانه از passus فعل *passāre «گام برداشتن، گذشتن» ساخته شد که در فرانسه‌ی کهن passer شد، و از آن passage «گذر، گذرگاه»، passe-port «اجازهٔ گذشتن از بندر» و compas (از *com-passāre) پدید آمد.\",\n \"sources\": [\"https://www.etymonline.com/word/passport\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet p.848\", \"stance\": \"supports\",\n    \"note\": \"'De là *passāre attesté par les l. romanes, M.L.6267, compassāre 3095, *expassāre 3033, etc.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. fathom (cross-reference list)\", \"stance\": \"supports\",\n    \"note\": \"'Cp. also expand, expanse, pace, pan ‚a broad vessel’, … passage, passim, passport, paten, patent, patera, patina, patio, patulous, petal, petalon … surpass, trespass' — Klein files the whole French/English family under the same I.-E. base.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"pâssâge; pâsport\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Two modern European loans that entered Persian through French in the Qajar/early Pahlavi period, not through the older Arabic or Turkish channels. پاساژ pāsāž 'covered shopping arcade' is French passage (the Parisian 'passage couvert' of the 19th c.); Dehkhoda marks it flatly 'پاساژ. (فرانسوی، اِ) بازار سرپوشیده که دو در دارد'. پاسپورت pāsport is French passeport, with French -e- of passe- dropped in the Persian shape and final -t retained; Mo'in glosses it 'پروانه برای آزادی رفت و آمد اشخاص … گذرنامه' and it now competes with the calque گذرنامه. Nourai's Latin-letter 'pâssâge' reproduces the French spelling rather than the Persian pronunciation, which is pāsāž.\",\n \"derivation_fa\": \"«پاساژ» و «پاسپورت» وام‌واژه‌های فرانسویاند که در دورهٔ قاجار و پهلوی اول وارد فارسی شدند: passage و passeport. دهخدا صریحاً می‌نویسد «پاساژ. (فرانسوی، اِ) بازار سرپوشیده که دو در دارد» و معین «پاسپورت» را «پروانه برای آزادی رفت و آمد اشخاص … گذرنامه». تلفظ فارسی «پاساژ» pāsāž است و آوانویسی نورایی (pâssâge) رونوشتِ املای فرانسوی است نه تلفظ فارسی. ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B3%D8%A7%DA%98/\", \"https://www.etymonline.com/word/passport\"],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"partial\",\n    \"note\": \"Mo'in has 'پاسپورت: [Fr.] پروانه برای آزادی رفت و آمد اشخاص از مملکتی به مملکت دیگر؛ گذرنامه؛ جواز عبور' (MON_part1.txt line 28216), which is Nourai's claim; پاساژ does not occur anywhere in the OCR of Mo'in's lexicon volumes (grep 'اساژ' finds only ماساژ). Nourai cites 'MON' without a page, so the second word cannot be tied to a page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. پاسپورت\", \"stance\": \"supports\", \"note\": \"see ref_check; entry present with a foreign-origin tag and the gloss 'گذرنامه'.\"},\n   {\"src\": \"DEHKHODA (via abadis.ir)\", \"where\": \"abadis.ir/fatofa/پاساژ/\", \"stance\": \"supports\",\n    \"note\": \"'پاساژ. (فرانسوی ، اِ) بازار سرپوشیده که دو در دارد دخول و خروج را.' — explicit French label.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep پاساژ / پاسپورت)\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's IE-roots dictionary covers inherited vocabulary only; neither modern loan appears.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"pass, passage, passport, compass, pace\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are Old French borrowings on the Latin passus stem. pass: ME passen (late 13c.) < OF passer < VL *passāre < passus. passage: ME (c.1300) < OF passage < passer + -age. passport: c.1500 passe-porte < OF passeport 'authorization to pass through a port', passe (imperative of passer) + port; the modern 'travel document' sense is from the 1540s. compass: ME < OF compas < VL *compassāre 'to pace out, measure by steps' (com- + passus), whence both 'circuit, extent' and the drawing/ mariner's instrument. pace: ME pas < OF pas < Latin passus, -ūs directly. Nourai's 'AHD' citation is apt: Watkins files PACE¹, PAS, PASS, PASSIM, EXPAND, REPAND under petə-.\",\n \"derivation_fa\": \"هر پنج واژهٔ انگلیسی از راه فرانسه‌ی کهن و از ستاک لاتین passus آمده‌اند: pass از passer، passage از همان با پسوند -age، passport از passe-port «اجازهٔ گذشتن از بندر» (حدود ۱۵۰۰ میلادی، معنای امروزین از دههٔ ۱۵۴۰)، compass از لاتین عامیانه *compassāre «با گام پیمودن» و pace مستقیماً از passus. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/passport\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. petə- §3: 'Latin pandere (past participle passus < *pat-to-) … : PACE¹, (PAS), (PASS), PASSIM; EXPAND, REPAND.' The chart's compass and passport are transparent compounds of the same passus.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. fathom\", \"stance\": \"supports\", \"note\": \"'Cp. also expand, expanse, pace, pan … passage, passim, passport … surpass, trespass.'\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/passport (with pass v.)\", \"stance\": \"supports\",\n    \"note\": \"'passport (n.) c.1500, passe-porte, ‚authorization to travel through a country’, from Old French passeport ‚authorization to pass through a port’ … from passe, imperative of passer ‚to pass’ + port'; 'pass (v.) … from Old French passer (11c.), from Vulgar Latin *passare ‚to step, walk, pass’, from Latin passus ‚step, pace’ (… PIE root *pete- ‚to spread”).'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., grep 'Pass'\", \"stance\": \"silent\",\n    \"note\": \"the OCR of this copy garbles the Pass/Passage headwords (only 'Passover' is legible), so Skeat could not be quoted.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Greek\", \"words\": \"petalon; patanĕ\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"πέταλον 'leaf, thin plate' is the neuter of the adjective πέταλος 'outspread, flat', built on the same stem as πετάννυμι 'I spread out' (< *peth₂-lo-, Wiktionary *péth₂-lom). πατάνη 'flat dish, platter' is from *πετάνā by assimilation of the first vowel (J. Schmidt KZ 32, 355ff., accepted by Walde-Pokorny II 18 and Pokorny 824), literally 'the spread-out thing'; Latin borrowed it as patina. Nourai's page reference AHD:980 is to the body of the 1975 New College dictionary (the pan/patina range), not to the root appendix, but Watkins's appendix entry says the same thing in full.\",\n \"derivation_fa\": \"πέταλον «برگ، ورقهٔ نازک» صورت خنثای صفت πέταλος «پهن‌شده» است، از همان ستاک πετάννυμι «می‌گسترم» (از *peth₂-lo-). πατάνη «بشقاب پهن» از *πετάνā با همگونی واکهٔ نخست پدید آمده (ی. اشمیت، به تأیید والده-پوکورنی) و لاتین آن را به صورت patina وام گرفت. هر دو واژه از همین ریشه‌اند و ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peth%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:980\", \"status\": \"supports\",\n    \"note\": \"the substance is in Watkins's appendix s.v. petə-: '4. Suffixed form *pet-alo- in Greek petalon, leaf: PETAL. 5. Suffixed form *pet-ano- in Greek patanē (? < *petanā), platter, “thing spread out”: (PAELLA), PAN¹, PATEN, (PATINA¹), (PATINA²).' p.980 is a page of the dictionary proper (the 1975 New College edition), which is not in the local library; the 1985 standalone appendix used here is the same text.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny p.824\", \"stance\": \"supports\",\n    \"note\": \"'πέταλον n. ‚Platte, Blatt’, πατάνη f. ‚Schüssel’ (aus *πετάνā; daraus lat. patina ds.)'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. petalon\", \"stance\": \"supports\",\n    \"note\": \"'petalon … Gk. πέταλον, ‚thin plate of metal, leaf’, neut. of the adj. πέταλος, ‚spread out’, rel. to πετάννυναι, ‚to spread out’, fr. I.-E. base *pet-, ‚to spread out’, whence also L. patēre …'\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 18\", \"stance\": \"supports\",\n    \"note\": \"'πέταλον ‚Platte, Blatt’, πατάνη ‚Schüssel’ (ass. aus *πετάνā, J. Schmidt KZ. 32, 355ff.; daraus lat. patina)'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"petal, pan\",\n \"verdict\": \"plausible\",\n \"derivation\": \"petal is certain: New Latin petalum (Tournefort, 1700) from Greek πέταλον, taken into English as a botanical term in 1704 — a learned borrowing, not an inherited word, and Nourai's single arrow Greek > English is fair for it. pan is not certain. Klein derives it as the chart does: 'ME. panne, fr. OE. panne … borrowed fr. ML. panna, fr. VL. *patna, fr. L. patina ‚broad dish, pan’, ult. fr. Gk. πατάνη'; Watkins puts PAN¹ under petə- likewise. But the word is common West Germanic (OHG pfanna, ON panna, Du. pan), which requires the loan to be very early (4th-5th c.), and Etymonline, following Boutkan, warns that 'both the Latin and Germanic words might be from a substrate language'. So the node is right for petal and only probable for pan; and if the loan is real it ran Greek > Latin > Vulgar Latin > West Germanic > Old English, not Greek > English.\",\n \"derivation_fa\": \"«petal» وام‌واژه‌ای عالمانه است: از لاتین نوین petalum (تورنفور، ۱۷۰۰) از πέταλον یونانی، که در ۱۷۰۴ وارد انگلیسی شد. ولی «pan» قطعی نیست: کلاین و واتکینز آن را از πατάνη از راه patina لاتین و *patna در لاتین عامیانه می‌دانند، ولی این واژه در همهٔ زبان‌های ژرمنی باختری هست و بوتکان (به نقل Etymonline) احتمال می‌دهد هر دو صورت لاتین و ژرمنی از زبانی بومی (زیرلایه) آمده باشند. افزون بر این، اگر هم وام باشد راهش یونانی > لاتین > ژرمنی باختری > انگلیسی کهن بوده است، نه یک کمان مستقیم. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/pan\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. pan, n.\", \"stance\": \"supports\",\n    \"note\": \"'pan, n., a broad vessel. — ME. panne, fr. OE. panne, which, together with ON., Swed. panna, Dan. pande, OFris. panne, OLG. panna … OHG. phanna, pfanna … is borrowed fr. ML. panna, fr. VL. *patna, fr. L. patina, ‚broad dish, pan’, ult. fr. Gk. πατάνη, ‚flat dish’.'\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/pan\", \"stance\": \"partial\",\n    \"note\": \"'probably an early borrowing (4c. or 5c.) from Vulgar Latin *patna. This is supposed to be from Latin patina … from Greek patane … But both the Latin and Germanic words might be from a substrate language [Boutkan].'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. petə- §5\", \"stance\": \"supports\",\n    \"note\": \"'Greek patanē … : (PAELLA), PAN¹, PATEN, (PATINA¹), (PATINA²)' — and §4 gives PETAL.\"}\n ]\n})\n\ndata[\"entries\"].append(e0)\n\n# ---------------- ENTRY 1 : Peu, Peue, Pu 1 ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Peu, Peue, Pu 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *pewH- 'to cleanse, purify' (Pokorny 827 'peu-, peuə-: pū- ‚reinigen, läutern, sieben’; pū-ro-, pu-to- ‚rein’'; Watkins 'peuə-. To purify, cleanse')\",\n \"note\": \"The chart gives no reference for this root, but it is Pokorny p.827 '1. peu-' — the very page whose entry runs 'pāvaká- … ‚lauter’ = mpers. pavāg, np. pāk ‚lauter, rein’; … lat. pūrus ‚rein’', i.e. both of Nourai's branches in two lines. His three headword variants 'Peu, Peue, Pu 1' reproduce Pokorny's own 'peu-, peuə-, pū-'. Modern notation writes the root *pewH-, the laryngeal explaining the long ū of *pū-ro- (< *puH-ro-) and the ā of Indo-Iranian *pawHa-. Root, language label and gloss correct.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *pewH- «پاک کردن، پالودن» است؛ پوکورنی در صفحهٔ ۸۲۷ آن را با همین سه گونهٔ peu-, peuə-, pū- آورده که نورایی عیناً رونوشت کرده است، هرچند مأخذی نداده. همان صفحه هر دو شاخهٔ این نمودار را دارد: «pāvaká- … = mpers. pavāg, np. pāk» و «lat. pūrus». در نوشتار امروزی، حنجره‌ای (لارنگال) پایانی ریشه کشیدگی واکهٔ *pū-ro- و آی هندوایرانی را توضیح می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/purus\", \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"Nourai gives the root box no reference. The standard place is Pokorny p.827 (verified below under the nodes) and Watkins/AHD s.v. peuə-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny p.827\", \"stance\": \"supports\",\n    \"note\": \"'peu-, peuə-: pū- ‚reinigen, läutern, sieben’; pū-ro-, pu-to- ‚rein’. Ai. Trans. punāti, Med. pávate ‚reinigt, läutert (sich)’ …'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. peuə-\", \"stance\": \"supports\",\n    \"note\": \"'peuə-. To purify, cleanse. Suffixed zero-grade form *pū-ro- (< *puə-ro-) in Latin purus, pure, and purgāre … : PURE, PURGE, PURITAN … [Pok. 1. peu- 827.]'\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 13\", \"stance\": \"supports\",\n    \"note\": \"'1. peu- ‚reinigen, läutern, sieben’ (auch set-Basis pū). Ai. pavate, punāti … pāvaka- … = mp. pavāg, np. pāk ‚lauter, rein’ … lat. pūrus ‚rein’.'\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"pâvaka\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The form is real but the language label is wrong, and the printed page (site/pages/401.jpg) really does say 'Avestan', so this is Nourai's error, not the extraction's. pāvaká- 'pure, clear; purifying' (an epithet of Agni, hence also 'fire') is SANSKRIT, and every source that has the word says so: Pokorny 827 prints it under 'Ai.' (= altindisch) — 'pāvaká- (auch pavāká-) ‚lauter’ = mpers. pavāg, np. pāk'; Walde-Pokorny II 13 the same; Horn, Grundriss no.277 writes 'ai. pavaka- ‚rein, klar’; phlv. pāk'. Avestan has no *pāvaka-; Bartholomae's AiW has instead pūiti-ka- 'serving for purification' (Pokorny quotes 'av. pūītika-'). The Iranian ancestor of pāk is therefore a Proto-Iranian *pawHāka-, the exact counterpart of the Indic word rather than a borrowing from it; it happens to be attested only in Middle Persian. So the derivation root > *pāvaka- > Pahlavi > pāk is sound in substance; only the box's language name should read Sanskrit (or Proto-Indo-Iranian).\",\n \"derivation_fa\": \"صورت pāvaká- «پاک، پالاینده» واقعی است ولی اوستایی نیست؛ سنسکریت است (لقب اگنی). پوکورنی (ص ۸۲۷)، والده-پوکورنی (II ۱۳) و هرن (شمارهٔ ۲۷۷) هر سه آن را زیر «هندی باستان» می‌آورند. در اوستا چنین واژه‌ای نیست؛ آنچه هست pūītika- «پالاینده» است. نیای ایرانی «پاک» صورت بازسازیٔ *pawHāka- است، هم‌ریشهٔ واژهٔ سنسکریت و نه وام از آن. بنابراین راهِ اشتقاق درست است ولی برچسب زبانی خانه باید «سنسکریت» باشد نه «اوستایی» — این خطای خود کتاب است، نه خطای خوانش اسکن (تصویر صفحهٔ ۳۷۱ را دیدیم).\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:62\", \"status\": \"partial\",\n    \"note\": \"Horn, Grundriss p.62 (HRN.txt form-feed leaf 83), no. 277: 'pāk ‚rein’, pākīze. ai. pavaka- ‚rein, klar’; phlv. pāk, pākīh.' The page and the etymon are exactly Nourai's, but Horn labels the comparandum 'ai.' = Old Indic, never Avestan.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny p.827\", \"stance\": \"contradicts\",\n    \"note\": \"'Ai. … pāvaká- (auch pavāká-) ‚lauter’ = mpers. pavāg, np. pāk ‚lauter, rein’; … av. pūītika- ‚zur Läuterung dienend’.' The Avestan member of this root is pūītika-, not *pāvaka-.\"},\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch (grep 'pāvaka', 'pavaka', 'pūitika')\", \"stance\": \"silent\",\n    \"note\": \"no entry *pāvaka- can be found in Bartholomae's dictionary in any OCR spelling; the Avestan lexicon has no such word.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 13\", \"stance\": \"contradicts\",\n    \"note\": \"'pāvaka- (und nach der ved. Metrik auch pavāká-) ‚lauter’ … = mp. pavāg, np. [pāk] ‚lauter, rein’' — filed under Ai. (Sanskrit).\"},\n   {\"src\": \"WIKTIONARY\", \"where\": \"en.wiktionary.org s.v. پاک\", \"stance\": \"partial\",\n    \"note\": \"'from Proto-Iranian *pawHākáh, from Proto-Indo-Iranian *pawHākás, from Proto-Indo-European *pewH- … Cognate with Sanskrit पावक (pāvaká) …' — the Sanskrit word is a cognate, not the ancestor.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box in the book, standing for the Middle Persian stage, which the sources supply: Pokorny 827 and Walde-Pokorny II 13 both write 'mpers. pavāg, np. pāk' — the older spelling pavāg preserves the -w- of *pawHāka- before it contracted; MacKenzie's Concise Pahlavi Dictionary records the contracted Book Pahlavi form 'pāk [DKY' (< Aramaic dkY); pʾk | = M, N ~] clean, pure, holy. ~īh: purity', i.e. the word could be written with the Aramaic heterogram DKY' as well as phonetically. Horn no.277 likewise 'phlv. pāk, pākīh'.\",\n \"derivation_fa\": \"این خانه در کتاب تهی است و تنها مرحلهٔ فارسی میانه را نشان می‌دهد. پوکورنی و والده صورت کهن‌تر pavāg را می‌آورند که واو میانی *pawHāka- در آن هنوز مانده، و مکنزی صورت پسین pāk را ثبت کرده که در پهلوی کتابی هم به هزوارش آرامی DKY' و هم آوانگارانه pʾk نوشته می‌شده است. هرن نیز phlv. pāk, pākīh دارد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DA%A9\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.64\", \"stance\": \"supports\",\n    \"note\": \"'pāk [DKYʼ < A ˓ky; pʾk | = M, N ~] clean, pure, holy. ~īh: purity, holiness. pākīzag [pʾkyckʼ | N ~a] pure.'\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny p.827\", \"stance\": \"supports\", \"note\": \"'= mpers. pavāg, np. pāk ‚lauter, rein’'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (grep 'pāk')\", \"stance\": \"silent\",\n    \"note\": \"the glossary of Nyberg's selected texts happens not to contain pāk; the searches return only apāk 'with' and similar.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"pâk\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian پاک pāk 'clean, pure' continues Middle Persian pāk without change; the whole chain is Proto-Indo-European *pewH- > Proto-Indo-Iranian *pawHākás > Proto-Iranian *pawHākáh > MP pavāg / pāk > NP pāk, the -w- of the suffix -āka- dropping between vowels and the two a's contracting to ā. The derived abstract پاکی pākī answers MP pākīh and پاکیزه pākīza MP pākīzag; Kurdish pâk is the same inherited word, not a Persian loan. The chart's gloss 'clean, pure' is Mo'in's own ('پاک: (ص.) بی‌آلایش، پاکیزه، نمازی').\",\n \"derivation_fa\": \"«پاک» فارسی نو همان pāk فارسی میانه است که بی‌دگرگونی باقی مانده؛ زنجیره چنین است: *pewH- هندواروپایی > *pawHāka- هندوایرانی/ایرانی باستان > pavāg/pāk پهلوی > «پاک». واو میان‌واکه‌ای افتاده و دو الف در هم ادغام شده است. مشتقات «پاکی» (پهلوی pākīh) و «پاکیزه» (پهلوی pākīzag) هم همین راه را رفته‌اند. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DA%A9\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book; HRN:62 on the parent box covers it ('pāk ‚rein’, pākīze').\"}],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no.277, p.62\", \"stance\": \"supports\",\n    \"note\": \"'277. pāk ‚rein’, pākīze. ai. pavaka- ‚rein, klar’; phlv. pāk, pākīh.'\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. پاک\", \"stance\": \"supports\",\n    \"note\": \"'پاک: (ص.) بی‌آلایش؛ پاکیزه، نمازی' (MON_part1.txt line 28344) — the chart's gloss.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.64\", \"stance\": \"supports\", \"note\": \"'pāk … | = M, N ~' — explicitly identical in Manichaean MP and New Persian.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"pūrus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin pūrus 'clean, pure, unstained' is the zero-grade *puH-ro- of the root (Proto-Italic *pūros), built like clārus; beside it stand pūtus 'pure', nepus 'non purus' and putāre 'to clean, prune'. Ernout-Meillet stress that it belongs above all to religious language and connect it to 'la racine dissyllabique de skr. pavitár- ‚celui qui purifie’, pavitram, pūtaḥ ‚purifié’, punāti ‚il purifie’' — the same Indic paradigm Pokorny 827 lists, and to which pāk on the other branch of this chart belongs.\",\n \"derivation_fa\": \"pūrus لاتین «پاک، بی‌آلایش» صورت صفرِ ریشه (*puH-ro-) است، از ایتالیایی آغازین *pūros، هم‌ساخت با clārus. ارنو-میه‌یه آن را واژه‌ای دینی می‌دانند و با pavitár- و punāti و pūtaḥ سنسکریت پیوند می‌دهند — همان خانواده‌ای که «پاک» فارسی نیز از آن است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/purus\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. peuə-: 'Suffixed zero-grade form *pū-ro- (< *puə-ro-) in Latin purus, pure, and purgāre, to purify … : PURE, PURGE, PURITAN; COMPURGATION, DEPURATE, EXPURGATE, (SPURGE). [Pok. 1. peu- 827.]'\"},\n   {\"ref\": \"KLN\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. pure: 'L. purus, ‚pure, clean’, which is rel. to putus, ‚clear, pure’, putare, ‚to cleanse, clean’, and cogn. with OI. pávate, punāti, ‚purifies, cleanses’, pūtaḥ, ‚pure’ … MIr. úr, ‚fresh, new’, OHG. fowen, ‚to sift’.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, DELL s.v. purus\", \"stance\": \"supports\",\n    \"note\": \"'Lat. pūrus appartient à la racine dissyllabique de skr. pavitár- ‚celui qui purifie’, pavitram ‚instrument de purification’, pūtaḥ ‚purifié’, punāti ‚il purifie’. C'est un terme de la langue religieuse …'\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny p.827\", \"stance\": \"supports\",\n    \"note\": \"'lat. pūrus ‚rein’ (Bildung wie clā-ru-s), pūrgō, älter pūrigō, -āre ‚reinigen’; pūtus ‚rein’, nepus ‚non pūrus’.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"pure\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle English pur, pure (c.1300) from Old French (= Modern French) pur, fem. pure, from Latin pūrus; a straightforward Norman-French transmission, with the family purify, purity, purge (< purgāre), purée all coming the same way. Klein and Skeat give exactly this, and Watkins files PURE, PURGE, PURITAN under peuə-.\",\n \"derivation_fa\": \"«pure» انگلیسی از انگلیسی میانه pur/pure، از فرانسه‌ی کهن pur و آن از pūrus لاتین است؛ راهی کاملاً معمول برای وام‌واژه‌های نورمن-فرانسوی. هم‌خانواده‌هایش purify و purity و purge نیز همین راه را آمده‌اند. کلاین و اسکیت همین را می‌گویند و ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/purus\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference; the parent box's 'AHD; KLN' covers the word (both list PURE).\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. pure, adj.\", \"stance\": \"supports\",\n    \"note\": \"'pure, adj. — ME. pur, pure, fr. OF. (= F.) pur, fr. L. purus, ‚pure, clean’ … Cp. purblind, purée, purgatory, purge, purify, depurate, expurgate.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Pure\", \"stance\": \"supports\",\n    \"note\": \"'Pure. (F.—L.) F. pur, masc., pure, fem. — L. purus, pure. Cf. Skt. pū, to purify. (√PEU.)'\"}\n ]\n})\n\ndata[\"entries\"].append(e1)\n\n# ---------------- ENTRY 3 : Peud, Spheud ----------------\ne3 = {\n \"entry\": 3,\n \"root\": \"Peud, Spheud\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *(s)pewd- 'to press, hasten' (Pokorny 998 '(s)p(h)eu-d- ‚drücken, mit Nachdruck betreiben, eilen’'; Wiktionary *spewd-)\",\n \"note\": \"Nourai's two headword shapes 'Peud, Spheud' render Pokorny's bracketed '(s)p(h)eu-d-', and Pokorny p.998 does put the Iranian and the Greek under one root — he opens the entry with 'Npers. pōy ‚Eile’ (iran. *pauda-), parth. pwd ‚Lauf’' and only then gives σπεύδω. That is why the root is verified, not disputed. But the equation is not secure: Cheung (Etym. Dict. of the Iranian Verb, 2007, p.302) points out that Greek σπεύδω and Lithuanian spūdinti both require an initial s-, so Iranian *paud cannot simply be the s-less variant, and he suggests it may be a 'Reimbildung' (e.g. after *taud). Rix's LIV omits the Iranian forms, Wiktionary reconstructs *spewd- with obligatory s-, and Walde-Pokorny II 659 (the 1927 predecessor) knew no Iranian members at all — the Persian material was added by Pokorny only in 1959. So: real root, correct gloss, correct page; the Iranian-Greek link is accepted by Pokorny but questioned since.\",\n \"note_fa\": \"سرواژهٔ دوگانهٔ «Peud, Spheud» برگردان همان «(s)p(h)eu-d-» پوکورنی (ص ۹۹۸) است و پوکورنی خود این مقاله را با «Npers. pōy ‚Eile’ (iran. *pauda-), parth. pwd ‚Lauf’» آغاز می‌کند و سپس σπεύδω را می‌آورد؛ پس مأخذ نورایی دقیق است. اما چونگ (۲۰۰۷، ص ۳۰۲) یادآور می‌شود که هم یونانی و هم لیتوانیایی سِ آغازین دارند و بنابراین *paud ایرانی را نمی‌توان صرفاً گونهٔ بی‌سِ آن شمرد؛ او احتمال می‌دهد ساخته‌ای قیاسی/قافیه‌ساز باشد. در والده-پوکورنی (II ۶۵۹) هنوز هیچ صورت ایرانی ذکر نشده بود. پس ریشه و معنا درست است ولی پیوند ایرانی-یونانی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%CF%83%CF%80%CE%B5%CF%8D%CE%B4%CF%89\"],\n \"ref_check\": [\n   {\"ref\": \"POK:998\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt, printed p.998: '(s)p(h)eu-d- ‚drücken, mit Nachdruck betreiben, eilen’. Npers. poy ‚Eile’ (iran. *pauda-), parth. pwd ‚Lauf’; gr. σπεύδω ‚spute mich, eile; bin emsig, strebe, strenge mich an’ … σπουδή f. ‚Eile, Eifer’ … vielleicht alb. punë ‚Arbeit’.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, p.302 s.v. *paud\", \"stance\": \"partial\",\n    \"note\": \"'This root is connected to Gr. σπεύδω ‚I hurry’, Lith. spūdinti ‚to hasten’, etc. by Pokorny, l.c. (but the Ir. forms are omitted in LIV). Both forms have an initial s-: hence they cannot be treated as mere “mobile” s-variants of Ir. *paud, which is perhaps rather a “Reimbildung” (with e.g. *taud)? … *PIE — LIV: 581 | Pok.: 998.'\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 659\", \"stance\": \"silent\",\n    \"note\": \"'speud- ‚drücken, pressen; übertragen: mit Nachdruck betreiben (urgere opus), eilen’' with Gr. σπεύδω, Lith. spáudžiu, Alb. punë, Arm. poytʿ — and no Iranian form and no s-less variant.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dict. s.v. speudó (sph-)\", \"stance\": \"silent\",\n    \"note\": \"'speudó (sph-) ‚press, urge, hasten’. Cf. spheutó. WP II, 659 … Gk. … Arm. pʿutʿ … Alb. fus … Li. spáudžiu.' Mann also cites no Iranian cognate.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Old Iranian\", \"words\": \"paud, paud-a\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The Old Iranian verbal root *paud- 'to run, speed' with its thematic present stem *pauda-, exactly as Abolghasemi sets it out on the cited page and as Pokorny writes it ('iran. *pauda-'). Cheung's Etymological Dictionary of the Iranian Verb heads the entry '*paud ‚to run”' and gathers the whole Iranian family under it: Parthian pwd- 'to speed, move quickly, run', Khotanese pusta- (ppp.) 'driven', Sogdian pwt, Chorasmian (+*a-) βyd, NP pōyīdan, Wakhi bīt. The two forms in the box are the root and its present stem, not two separate words.\",\n \"derivation_fa\": \"ریشهٔ فعلی ایرانی باستان *paud- «دویدن، شتافتن» و ستاک حال آن *pauda- است — دو صورتی که در خانه آمده، یکی ریشه و دیگری ستاک، نه دو واژهٔ جداگانه. پوکورنی نیز همین «iran. *pauda-» را می‌نویسد و چونگ زیر مدخل *paud خویشاوندان آن را در پارتی (pwd-)، ختنی (pusta-)، سغدی (pwt)، خوارزمی و وخی برمی‌شمارد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D9%88%DB%8C%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"FFD:44\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi, Mādde-hā-ye fe'l-hā-ye fārsi-ye dari p.44 = PDF p.49 (incoming/FFD/FFD_pages.txt leaf 48), s.v. پوییدن: 'پویید مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است. پوی < فارسی میانه [pōy] < ایرانی باستان *[pauda-] … ریشهٔ [paud] به‌معنی «دویدن» است.' (the Latin-script etyma come through as digits in the Persian-model OCR, but the Persian frame is unambiguous and matches Nourai's two boxes word for word).\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, p.302\", \"stance\": \"supports\",\n    \"note\": \"'*paud ‚to run’. *MIDDLE PERSIAN: BMP pwd- /pōy-/ ‚to run, flow’ … *PARTHIAN: pwd- ‚to speed, move quickly, run’ … *KHOTANESE: LKh. pusta- (ppp.) ‚driven’ … *NWIR: NP pōyīdan/pōy- ‚to wander; to run; to trot’.'\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny p.998\", \"stance\": \"supports\", \"note\": \"'Npers. poy ‚Eile’ (iran. *pauda-), parth. pwd ‚Lauf’.'\"},\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch (grep paud-, puδ-)\", \"stance\": \"silent\",\n    \"note\": \"the root is not attested in Avestan or Old Persian, so Bartholomae has no entry; 'Old Iranian' here is a reconstruction, correctly labelled.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"pôy\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian pōy- 'to run', written pwd- in Book Pahlavi (the spelling still shows the -d of *pauda-, while the pronunciation had already gone *pauda- > *pōy- by the regular Middle Persian change of intervocalic -d- > -y- after the diphthong au > ō). MacKenzie's Concise Pahlavi Dictionary has 'pōy- [pwd- | (P pwd-), N ~] run. ~išnīg: running', giving in one line the Parthian parallel and the identity with New Persian; the infinitive is pwāytn /pōyīdan/ (Cheung). Nourai's 'pôy' is this form.\",\n \"derivation_fa\": \"فارسی میانه pōy- «دویدن»، در پهلوی کتابی pwd- نوشته می‌شود؛ املا هنوز دالِ *pauda- را نگاه داشته، در حالی که تلفظ بر پایهٔ دو دگرگونی معمول فارسی میانه — au > ō و دالِ میان‌واکه‌ای > ی — به pōy رسیده بود. مکنزی می‌نویسد: «pōy- [pwd- | (P pwd-), N ~] run»، یعنی همان صورت در پارتی و فارسی نو. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D9%88%DB%8C%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"FFD:44\", \"status\": \"supports\",\n    \"note\": \"same entry, p.44 s.v. پوییدن: 'پوی < فارسی میانه [pōy] < ایرانی باستان *[pauda-]' — the Pahlavi step is exactly where Nourai puts it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.69\", \"stance\": \"supports\",\n    \"note\": \"'pōy- [pwd- | (P pwd-), N ~] run. ~išnīg: running.' (Cheung cites the same page: 'MacKenzie, Pahlavi: 69'.)\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, p.302\", \"stance\": \"supports\",\n    \"note\": \"'*MIDDLE PERSIAN: BMP pwd- /pōy-/ ‚to run, flow’. Inf.: BMP pwytn /pōyīdan/.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (grep 'pōy', 'pwd')\", \"stance\": \"silent\",\n    \"note\": \"the verb does not occur in the texts Nyberg glosses; the only hits are the unrelated a-pēyišn 'not thirsting'.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"pū; pūyîdan; pūyâ; pūyânîdan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are one Persian verbal family on the inherited present stem پوی pōy/pūy < MP pōy- < *pauda-. پوییدن pūyīdan 'to go at a trot, walk fast, roam' is the New Persian infinitive (Wiktionary: 'Inherited from Middle Persian pwd- /pōy-/, ‚to run”'), with a secondary past stem pūyīd built from the present stem, which is precisely what Abolghasemi says on the cited page ('پویید مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است'). پو pū / پویه pūye is the deverbal noun 'a trot, a gait between walking and running' (Mo'in: 'رفتار وسط که نه تند باشد و نه کند، پویه، دو'), whence the compound تکاپو tak-ā-pū 'running to and fro'. پویا pūyā / پویان pūyān are the present participles in -ā / -ān. پویانیدن pūyānīdan is the causative in -ānīd-, and Mo'in's gloss confirms Nourai's unusual 'to make animals go fast' word for word: 'به راه بردن (ستور و غیره)'. The Ferdowsi line printed in the box ('نبد راه بر کوه از هیچ روی / بگشتم بسی گرد او پوی پوی') uses the noun adverbially.\",\n \"derivation_fa\": \"هر چهار واژه یک خانواده‌اند بر ستاک حالِ میراثی «پوی» (از pōy پهلوی، از *pauda-). «پوییدن» مصدر فارسی نو است و مادهٔ ماضی آن (پویید) — به گفتهٔ ابوالقاسمی در همان صفحهٔ ۴۴ — «جعلی» و ساخته از مادهٔ مضارع است. «پو» و «پویه» اسم مصدری‌اند به معنی دویدنِ میانه (معین: «رفتار وسط که نه تند باشد و نه کند») و از همین «تکاپو» ساخته شده؛ «پویا» و «پویان» صفت فاعلی، و «پویانیدن/پویاندن» سببی (متعدی) است که معین دقیقاً به «به راه بردن (ستور و غیره)» معنی کرده و همین معنای نامعمول در نمودار نورایی آمده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D9%88%DB%8C%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:998\", \"status\": \"supports\", \"note\": \"'Npers. poy ‚Eile’ (iran. *pauda-)' — the chart's پو 'running' on the same page.\"},\n   {\"ref\": \"MON:826\", \"status\": \"supports\",\n    \"note\": \"Mo'in has the whole set consecutively: 'پو: [pū] [= پوی، رک. پوییدن] (ا.) رفتار وسط که نه تند باشد و نه کند، پویه، دو'; 'پویا: (ص فا. پوییدن) رونده، دونده'; 'پویان: (ص فا. حا. پوییدن) روان، دوان'; 'پویانیدن: [= پویاندن …] (مص م.) … به راه بردن (ستور و غیره)'; 'پویه: (ا مص.) رفتاری متوسط، رفتن نه به شتاب و نه نرم'; 'پوییدن: (مص ل.) … رفتن (نه به شتاب و نه نرم)' (MON_part1.txt lines 32972, 33573-33580). The gloss of پویانیدن matches Nourai's 'to make animals go fast' exactly. The printed page number 826 could not be checked: the local OCR of Mo'in carries no page markers.\"},\n   {\"ref\": \"ISS:130\", \"status\": \"not_checked\",\n    \"note\": \"Bailey, Indo-Scythian Studies vol. VI (1967) is not online (refs_online.json: 'Khotanese Texts VI itself is not online'), and the substitute Dictionary of Khotan Saka has no pū-/pūy- headword findable by grep. Cheung p.302 does cite Bailey for this root — and rejects part of it: 'Some etymological references, notably Arm. (LW) hrapoyr … Skt. pota- ‚boat’, cited by Bailey are hardly tenable, cf. EWAia III: 338.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, p.302\", \"stance\": \"supports\",\n    \"note\": \"'*NWIR: NP pōyīdan/pōy- ‚to wander; to run; to trot’, NP pūd, Nn. puy ‚woof, weft’, Tr. pōyetōn, Varz. pu ‚carpet weft’.'\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, پو … پوییدن\", \"stance\": \"supports\", \"note\": \"see ref_check; all four headwords present with Nourai's glosses.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, p.181\", \"stance\": \"partial\",\n    \"note\": \"an entry headed 'پوی، پوییدن' stands on p.181 (ARY_pages.txt, [pdf page 180]) with a cognate list by language (یونانی / لاتین / ارمنی / لهستانی …) and citations to برهان قاطع and فرهنگ معین, but the Latin-script forms are illegible in this OCR, so the reconstruction he gives cannot be quoted.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (grep pōy, pūyīdan)\", \"stance\": \"silent\",\n    \"note\": \"Horn has no numbered entry for this verb.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Greek\", \"words\": \"speudo\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Ancient Greek σπεύδω 'I hurry, am eager, exert myself', transitive 'urge on, hasten (something)', with the noun σπουδή 'haste, zeal' and σπουδαῖος 'earnest'. Pokorny 998 derives it from the same root as Iranian *pauda- and reconstructs the original sense as 'press, squeeze', pointing to σπουδά 'pestle' (Hesychius) — which is where Nourai's root gloss 'to press, hasten' comes from. The Greek word itself is not in doubt (cognates Lithuanian spáudžiu 'press', Albanian punë, Armenian փոյթ pʿoytʿ); what is in doubt is the arrow from this root to Iranian: Greek and Lithuanian both require initial s-, so Wiktionary reconstructs *spewd- with the s- as integral and Cheung 302 concludes that Ir. *paud 'cannot be treated as a mere “mobile” s-variant'. Hence plausible rather than confirmed: the node is right if Pokorny's root is right, and it is the shakier half of that root.\",\n \"derivation_fa\": \"σπεύδω یونانی «شتافتن، کوشیدن» (با اسم σπουδή «شتاب، جدیت») واژه‌ای است قطعی و هم‌ریشه با spáudžiu لیتوانی «فشردن» و punë آلبانیایی. پوکورنی معنای نخستین را «فشار دادن» می‌داند (با استناد به σπουδά «دستهٔ هاون») و همین معنای دوگانه به نمودار نورایی راه یافته است. اما چون یونانی و لیتوانیایی هر دو سِ آغازین می‌خواهند، پیوستن آن به ریشهٔ ایرانی *paud قطعی نیست؛ پس این خانه با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%CF%83%CF%80%CE%B5%CF%8D%CE%B4%CF%89\"],\n \"ref_check\": [\n   {\"ref\": \"POK:998\", \"status\": \"supports\",\n    \"note\": \"'gr. σπεύδω ‚spute mich, eile; bin emsig, strebe, strenge mich an’; trans. ‚treibe an, beschleunige’ (ursprüngl. ‚dränge, drücke’, wie in σπουδά ‚Mörserkeule’ … Hes.); σπουδή f. ‚Eile, Eifer, Bestrebung’.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"WIKTIONARY\", \"where\": \"en.wiktionary.org s.v. σπεύδω\", \"stance\": \"partial\",\n    \"note\": \"'From Proto-Indo-European *spewd- (“to press, hurry”). Cognate with Albanian punë, Lithuanian spáusti, Old Armenian փոյթ (pʿoytʿ).' The reconstruction keeps the s-, and no Iranian cognate is listed.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. speudó (sph-)\", \"stance\": \"supports\",\n    \"note\": \"'speudó (sph-) ‚press, urge, hasten’. … WP II, 659' — Mann's headword shape 'speud- (sph-)' is the source of Nourai's second variant 'Spheud'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 659\", \"stance\": \"supports\",\n    \"note\": \"'speud- ‚drücken, pressen; übertragen: mit Nachdruck betreiben (urgere opus), eilen’. Gr. σπεύδω … σπουδή ‚Eile, Hast; Eifer’.'\"}\n ]\n})\n\ndata[\"entries\"].append(e3)\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-401.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-401.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-401.json > /dev/null && echo \"valid json\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 401"
}
```


### [2026-09-14T01:13:01.935Z] TOOL RESULT

```
written
valid json
nodes verified: 17/17
node verdicts: {'plausible': 3, 'confirmed': 13, 'disputed': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'partial': 3, 'supports': 11, 'not_checked': 6}
books consulted: {'supports': 36, 'contradicts': 3, 'partial': 5, 'silent': 7} | by book: {'WLD': 5, 'KLN': 5, 'POK': 5, 'PHD': 4, 'MON': 4, 'BRT': 3, 'HRN': 3, 'LAT': 3, 'CHEUNG': 3, 'AHD': 2, 'ARY': 2, 'ETYMONLINE': 2, 'SKT': 2, 'WIKTIONARY': 2, 'NYB': 2, 'SYN': 1, 'HUB': 1, 'DEHKHODA (via abadis.ir)': 1, 'IEC': 1}
```


## [2026-09-14T01:13:10.224Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-401.json'))\nfor e in d['entries']:\n    assert e.get('note_fa'), e['entry']\n    assert e.get('ref_check') is not None and e.get('consulted')\n    for n in e['nodes']:\n        assert n.get('derivation_fa'), (e['entry'],n['id'])\n        assert n.get('ref_check') and n.get('consulted'), (e['entry'],n['id'])\nprint('all fa/ref_check/consulted present; nodes:', sum(len(e['nodes']) for e in d['entries']))\n\""
}
```


### [2026-09-14T01:13:11.646Z] TOOL RESULT

```
all fa/ref_check/consulted present; nodes: 17
```


## [2026-09-14T01:13:33.202Z] AGENT

Page 401 (book p. 371) verified — `data/verification/page-401.json`, `verify_check.py 401` shows **0 PROBLEM lines**.

**Counts** — 3 entries (1 redirect skipped), 17 nodes.
- Node verdicts: confirmed 13, plausible 3, disputed 1
- Root verdicts: confirmed 2 (Pet 2, Peu), plausible 1 (Peud/Spheud)
- Ref checks: supports 11, partial 3, not_checked 6 · Books consulted: 51 entries across POK, WLD, AHD, KLN, BRT, HRN, HUB, PHD, NYB, CHEUNG, LAT, SYN, IEC, MON, BQT, ARY, SKT, Etymonline, Wiktionary, Dehkhoda

**Disputed / flagged**
- *Peu, Peue, Pu 1* #1 "[Avestan] pâvaka" — **disputed**: pāvaká- is Sanskrit, not Avestan. Pokorny 827, Walde-Pokorny II 13 and Horn no. 277 all file it under "Ai."; Avestan's member of this root is pūitika-. The Iranian ancestor of pāk is Proto-Iranian *pawHāka- (Wiktionary), a cognate of the Indic word, not a borrowing. The derivation itself (root → Pahlavi pavāg/pāk → NP pāk) is sound; only the language label is wrong.
- *Pet 2* #1 "pathana, perethu" — plausible: paθana- is right (Bartholomae col. 843 himself gives "np. pahn"), but Av. pərəθu- belongs to *pleth₂- (Pokorny 833, Buck 12.61 §1); Pokorny/WP only say paθana-'s θ is analogical after pərəθu-.
- *Pet 2* #8 "pan" — plausible: Klein/Watkins derive it from Gk. patanē via L. patina → VL *patna → WGmc, but Etymonline (after Boutkan) allows a substrate source for both the Latin and Germanic words; the route is also Greek→Latin→WGmc→OE, not a direct arrow.
- *Peud, Spheud* root and #4 "speudo" — plausible: Pokorny 998 does unite Npers. pōy (iran. *pauda-) with Gr. σπεύδω, but Cheung 2007:302 objects that Greek and Lithuanian both require initial s-, LIV omits the Iranian forms, and Walde-Pokorny II 659 listed no Iranian member at all.

**Extraction errors: none.** I read `site/pages/401.jpg`; the JSON is faithful throughout, including the empty French/Pahlavi pass-through boxes and the Ferdowsi line on the پو node. The "Avestan pâvaka" mislabel is printed in the book itself.

**Notes for the owner**
- BQT:433 could only be checked in OCR — `tools/ref_page.py BQT:433` reports no scan covers Borhan vol. 1 p. 433; leaf 659 of `BQT_v1_pages.txt` is that page (its footnote block opens «بقیه از صفحهٔ ۴۳۲») and carries پهنا/پهنه, but Mo'in's footnote is unreadable.
- MON:826 verified by content, not page: the local Mo'in OCR has no page markers. Mo'in's gloss of پویانیدن («به راه بردن (ستور و غیره)») matches Nourai's odd "to make animals go fast" exactly.
- ISS:130 not checkable (Bailey, Khotanese Texts VI is not online); Cheung cites Bailey for this root and rejects part of his comparanda.
