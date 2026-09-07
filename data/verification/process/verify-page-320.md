# Verification process log — verify-page-320


## [2026-09-07T15:49:09.825Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 320 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-320.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-320.json. Write /home/sfmqrb/git/rishe/data/verification/page-320.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 320` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:11.883Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T15:49:12.629Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:12.644Z] TOOL RESULT

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


## [2026-09-07T15:49:13.223Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-320.txt"
}
```


### [2026-09-07T15:49:13.239Z] TOOL RESULT

```
1	=== PDF page 320 (book page 290) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Mâk : long, thin, slender  (refs POK:699)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:699; KNT:201; SYN:880 | mas : long ; masah : length, size ; mas-yâ 2 : longer ☞Yah 5 ; mas-yah : greater ☞Yah 5 ; mas-išta : longest ☞Isto ; math-išta : the supreme | NOTE: Compare with root "Meg: great".
5	  #2 (parent #1) [Persian] refs=HRN:224; BQT:2002,2058 | meh 2 «مه ۲» : great ; mehast «مهست» : greatest ; meznâ «میزنا» : balance, scale | NOTE: "meznâ" was not found in MON. Also see Root "Meg: great"
6	#3 (parent #0) [Greek] refs=AHD | makros : long ; makedonios : tall ones, people from the highlanders (an area north of Greece), Macedonia
7	  #4 (parent #3) [Persian] refs=MON5:2007 | Maqdûnîyyeh «مقدونیه» : Macedonia
8	  #5 (parent #3) [Latin] refs=None | 
9	    #6 (parent #5) [English] refs=None | Macedonia
10	  #7 (parent #3) [English] refs=None | macro-, macron
11	#8 (parent #0) [Latin] refs=AHD | macer : thin
12	  #9 (parent #8) [English] refs=None | meager
13	--- entry 1 ---
14	ROOT [Indo-European] Mako : house fly  (refs POK:699)
15	#1 (parent #0) [Avestan] refs=POK:699; SYN:193 | maxši : house fly | NOTE: SYN:193 claims an imitative origin (Indo-European "Mu", "Mus").
16	  #2 (parent #1) [Pahlavi] refs=HRN:221; SNS:238; ISS:278 | maxš : house fly ; makas, magas : fly
17	    #3 (parent #2) [Persian] refs=BQT:2029; HRN:221 | magas «مگس» : house fly
18	#4 (parent #0) [Sogdian] refs=ISS:278 | mwğšk : house fly
19	--- entry 2 ---
20	ROOT [Sumerian] Mana : an ancient unit of weight  (refs AKD:20,21; KLN:982)
21	#1 (parent #0) [Akkadian] refs=AKD:20,21 | mânu : unit of weight
22	  #2 (parent #1) [Sanskrit] refs=KLN:949 | manâ
23	    #3 (parent #2) [Persian] refs=BQT:2035 | man 2 «من ۲» : a unit of weight equal to 3 kilograms
24	  #4 (parent #1) [Greek] refs=None | mna
25	    #5 (parent #4) [Latin] refs=None | mina
26	      #6 (parent #5) [English] refs=AHD:834; KLN:982 | mina, mine : old units of weight and money
27	
```


## [2026-09-07T15:49:16.890Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-320.json",
 "description": "Read source JSON for page 320"
}
```


### [2026-09-07T15:49:16.931Z] TOOL RESULT

```
{
  "pdf_page": 320,
  "book_page": 290,
  "entries": [
    {
      "root": {
        "name": "Mâk",
        "lang": "Indo-European",
        "refs": "POK:699",
        "gloss": "long, thin, slender",
        "note": "This root may be related to \"Meg: great\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:699; KNT:201; SYN:880",
          "words": [
            {"translit": "mas", "gloss": "long", "script": null},
            {"translit": "masah", "gloss": "length, size", "script": null},
            {"translit": "mas-yâ 2", "gloss": "longer", "script": null, "see": ["Yah 5"]},
            {"translit": "mas-yah", "gloss": "greater", "script": null, "see": ["Yah 5"]},
            {"translit": "mas-išta", "gloss": "longest", "script": null, "see": ["Isto"]},
            {"translit": "math-išta", "gloss": "the supreme", "script": null}
          ],
          "script_extra": null,
          "note": "Compare with root \"Meg: great\".",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:224; BQT:2002,2058",
          "words": [
            {"translit": "meh 2", "gloss": "great", "script": "مه ۲"},
            {"translit": "mehast", "gloss": "greatest", "script": "مهست"},
            {"translit": "meznâ", "gloss": "balance, scale", "script": "میزنا"}
          ],
          "script_extra": null,
          "note": "\"meznâ\" was not found in MON. Also see Root \"Meg: great\"",
          "quote": {"text": "ز شاه جهاندار خورشید دهر - مهست و سرافراز و گیرنده شهر", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "makros", "gloss": "long", "script": null},
            {"translit": "makedonios", "gloss": "tall ones, people from the highlanders (an area north of Greece), Macedonia", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON5:2007",
          "words": [
            {"translit": "Maqdûnîyyeh", "gloss": "Macedonia", "script": "مقدونیه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Macedonia", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "macro-, macron", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "macer", "gloss": "thin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "meager", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mako",
        "lang": "Indo-European",
        "refs": "POK:699",
        "gloss": "house fly"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:699; SYN:193",
          "words": [
            {"translit": "maxši", "gloss": "house fly", "script": null}
          ],
          "script_extra": null,
          "note": "SYN:193 claims an imitative origin (Indo-European \"Mu\", \"Mus\").",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:221; SNS:238; ISS:278",
          "words": [
            {"translit": "maxš", "gloss": "house fly", "script": null},
            {"translit": "makas, magas", "gloss": "fly", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:2029; HRN:221",
          "words": [
            {"translit": "magas", "gloss": "house fly", "script": "مگس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "ISS:278",
          "words": [
            {"translit": "mwğšk", "gloss": "house fly", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mana",
        "lang": "Sumerian",
        "refs": "AKD:20,21; KLN:982",
        "gloss": "an ancient unit of weight"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Akkadian",
          "refs": "AKD:20,21",
          "words": [
            {"translit": "mânu", "gloss": "unit of weight", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Sanskrit",
          "refs": "KLN:949",
          "words": [
            {"translit": "manâ", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:2035",
          "words": [
            {"translit": "man 2", "gloss": "a unit of weight equal to 3 kilograms", "script": "من ۲"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Greek",
          "refs": null,
          "words": [
            {"translit": "mna", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "mina", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:834; KLN:982",
          "words": [
            {"translit": "mina, mine", "gloss": "old units of weight and money", "script": null}
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


## [2026-09-07T15:49:19.157Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','SYN','HRN','BQT','MON','AHD','AKD','KLN','SNS','ISS','PHD','NYB','WLD','IEC','SOD','ARY','HUB','BRT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-07T15:49:20.654Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
```


## [2026-09-07T15:49:25.644Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T15:49:25.695Z] TOOL RESULT

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


## [2026-09-07T15:49:26.023Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T15:49:26.105Z] TOOL RESULT

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


## [2026-09-07T15:49:30.879Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=354 && NR<=357 {print \"=== leaf \"NR\" ===\"; print}' POK_02.txt | head -200",
 "description": "Print Pokorny leaf around p.699"
}
```


### [2026-09-07T15:49:32.185Z] TOOL RESULT

```
=== leaf 354 ===
g';
ir.  lö-chasair  ,Regen'  (*Zowo-);  air.  lüaith,  cjmr.  lludio,  corn.  lusow, bret.  ludu  , Asche'  (*lou-tu-i-  , Waschmittel');  mc.  glau,  cymr.  gwlaw  ,Regen'j
aisl.  laudr  n.  , Lauge,  Seifenschaum,  Schaum',  ags.  leapor  , Seifenschaum' (Hou-tro-)j  ahd.  louga,  nhd.  Lauge,  ags.  leah  ds.,  aisl.  laug  f.  ,Bade- wasser'  {Hou-kä),  ablaut.  ahd.  luhhen  , waschen'  (*luk-)'^
hitt.  la-hu-uz-zi  (lauzi)  , gießt  aus'.
WP.  II  441,  WH.  773  ff.;    0.  Szemerenyi  KZ.  70,  57  f.
iäs,  Gen.  luu-ös  ,Laus'  (*Tier?),  oft  tabuistisch  entstellt.
Abrit.  Huuä  >  louä  >  cymr.  Hau  , Läuse'  (Sg.  Heuen),  corn.  low  bret, laou,  Vannes  leu  ds.;
ags.  mnd.  ahd.  aisl.  lüs  f.  ,Laus';  aisl.  lyski  f.  ^Läusekrankheit' ;
mit  tabuistischer  Entstellung:  ai.  yü-kä,  pali  ü-kä,  prakrit  wä;  lit.  u-t% und  (mit  Ablaut  und  Reduplikation)  vievesa,  vievesä  f.;  ksl.  v^äb,  serb. väs.  Gen.  vesi  und  üs,  usw.  (*wsi-);
über  toch.  B  luwa  ,Tier',  PL  Iwäsa  s.  Pedersen  Toch.  72;  vgl.  dän. olyr  ,Tier'  und  ,Laus';  oder  zu  aksl.  lov^  oben  S.  655?
WP.  II  443,  Specht  Idg.  Dekl.  44,  Trautmann  336,  Lohmann  ZceltPh. 19,  62  ff.
M.
^a-  (erweitert  mäi-?)  ,mit  der  Hand  winken^ ;  aus  ^verstohlen  zuwinken* dann  ^vorspiegeln^  betrügen,  zaubernd
Ai.  '^^y^  ^Verwandlung,  Truggestalt,  Betrug,  Illusion^  (oder  zu  3.  me-?);
a-v.  (xrjvvo),  dor.  {xärvcü  ,zeige  an,  verrate^  aus  *ij.ä-vv-ixi  , winke  mit  der Hand^;  s-Erweiterung  (j,aiojj.aL  , berühre,  untersuche^,  Fut.  fxdaaoixaL,  iTtl- aacrtog  ,berührt^  =  ,befleckt',  iiaaxrjQ,  ^aargög  , Sucher,  Nachforscher^, uaatQOTtög  ,Kuppler'',  ^dang,  ^itaarij  , Peitsche,  Geißel;  f- Er  Weiterung /iari; ^Verfehlung^  (*m9-ta),  (.idrrjv^  dor.  -av  ,vergeblich^,  (.idzaiog  , eitel,  nichtig^;
lit.  möjuj  möti  ,mit  der  Hand  winken,  ein  Zeichen  geben^,  lett:  mäjuj mät  ds.,  mddit  ,mit  der  Hand  winken^,  mddities  , Gaukelei  treiben',  mddzi ^Gaukelbilder';  mit  s-Erweiterung  lit.  mäsinti  ,locken',  mosüoti  ,schwenken, schwingen',  mostagüoti  ds.,  mösteretij  mösteleti  ,winken' ;
slav.  *maJ2,  *majati  (an  Stelle  von  *mati  nach  dem  balt.-slav.  Präteri- talstamm  *mäiä-)  in  abg.  na-majq,  -majati  
=== leaf 355 ===
,zuwinken',  po-mavati,  -mangti ds.,  russ.  na-mdjath  , durch  Zeichen  anzeigen,  betrügen',  mit  Formans -mo-:  serb.  mdmlm,  mdmiti  ,locken';  mit  Formans  -no-:  russ.  mafin,  manith , anlocken,  täuschen'  (aus  dem  Slav.  stammen  lit.  monai  PI.  , Zauberei', lett.  mänit  ,betrügen')  ;•  mit  Formans  -rä-:  russ.-ksl.  mara  , Gemütsbewegung', poln.  mara  ,Täuschung',  usw. ;  s-Erweiterung  in :  ksl.  machaju,  machati ,yentilare',  usw.;  t-Erweiterung  in:  aserb.  matam,  matati  ,anlocken',  cech. mdtati  ,als  Gespenst  spuken',  usw.
WP.  II  219  f.,  WH.  II  33,  Trautmann  166.
2.  mä-  ,gut,  zu  guter  Zeit,  rechtzeitig'.
Mit  Formans  -no-  alat.  mänus  ,gut',  immänis  ,schrecklich',  adverbial mäne,  mänl  ,früh';  hierher  auch  mänes  f.  ,die  abgeschiedenen  Seelen', später  , Unterwelt,  Tod';  vielleicht  phryg.  (j,rjv  ,abgeschiedene  Seele',  ^avla „*xaAiJ";  oder  gehört  lat.  mänes  zu  gr.  (^rjvig,  dor.  (,iävig  , Groll'?  vgl.  S.  727.
Mit  f-Formantien:  lat.  Mätüta  ,die  Göttin  der  Frühe,  der  Morgenhelle, aber  auch  der  Reife',  matütlnus  ,morgendlich',  mätürus  ,rechtzeitig;  zeitig =  reif  (beruhen  auf  *mä-tu-j  etwa  ,gute,  gelegene  Zeit'),  osk.  Maatüis (*Mätls  =  ,dl  Mänes')]  reduktionsstufig  vielleicht  kelt.  *mä-ti-  in  air.  maith, cymr.  mad,  corn.  mas^  mbret.  matj  nbret.  mad  ,gut'  und  gall.  PN  Mati- donnusj   Teuto-matos;  auch  air.  maithid  ,verzeiht'.
WP.  II  220  f.,  WH.  II  27  f.,  53  f.
694    .
5-  mä  Lallwort  für  ^Mutter',  redupl.  mämä,  mammä]  z.  T.  (Dissimilation ?\ mänä,  mannä  zweifelhaften  Alters.
Ai.  mä  ^Mutter';
dor.  (.lä  „^^r£^/"  (in  (xä  yä  ,o  Mutter  Erde*,  Aisch.),  wovon  ion.  att.  jt/ßj-^ ^Mutter,  Amme,  Hebamme^,  dor.  _, Großmutter';  abgeleitet  mnd.  möje  ,Mutter. Schwester',  ahd.  holz-muoja  ,Hexe';
ai.  mäma-  Vokativ  m.  ,Onkel'  (von  *mäma  , Mutterschwester') ;  nperg mäm,  mämä,  mäml  ,Mutter' ;  arm.  mam  ^Großmutter'  (gr.  Lw.  wie  j>ap?\. gr.  (xdfifj-a  Lallvokativ,  wovon  ion.  att.  i-iccfAf^rj  ^Mutter',  f-iay-iiia  ^Mutter*» lat.  mamma  Kosewort  ,Mama,  Mutter',  auch  ,Mutterbrust',  mamilla  ,Brust- warze' ;  alb.  meme  gQ^.  mame  ,Mutter' ;  ir.  cjmr.  corn.  bret.  mam  jMutter* air.  muimme  , Pflegemutter'  {*mammiä);  nhd.  alem.  mamme  , Mutter',  ab- lautend ahd.  muoma  ,Mutterschwester',  nhd.  Muhme]  lit.  mamä,  momä lett.  mäma  ds. ;  russ.  (u
=== leaf 356 ===
sw.)  mäma  ,Mama,  Mutter' ;  hitt.  Gottheit  ikfaTnwiO' vgl.  kleinasiat.  Mrjvj],  ngr.  (.idvva  ,Mutter',  aisl.  möna  ,Mutter',  mnd.  möne. möme  , Mutterschwester'.
WP.  II  221  f.,  WH.  II  21  f.,  Trautmann  168;  mä  ist(?)  Grundlage  von mäter-  (s.  dort).
tnad-  ,naß,  triefen;  auch  von  Fett  triefen,  vollsaftig,  fett,  gemästet';  mad-do- ,Mästung'.
Ai.  mddati,  mddate  ,wallen,  sprudeln,  fröhlich  sein',  mädyati,  mamdtti, mdndati  ds.,  mdda-  m.  ,Rauschtrank'  =  av.  maSa-  , Rauschtrank,  Rausch- begeisterung', ai.  mattd-  ,trunken,  freudig,  erregt',  av.  mad-  {maöaitlj madayaTdha)  ,sich  berauschen,  sich  ergötzen  an' ;  ai.  madgu-  ,ein  bestimmter Wasservogel,  ein  Fisch'  =  np.  mäy  ,ein  Wasservogel',  ai.  mdtsya-  m.,  av. masya  ,Fisch'  (,der  nasse' ;  Ableitung  von  einem  -es-St.  *mades-) ;  ai.  medas- n.  ,Fett',  medana-  n.  ,Mästung',  mBdyati^  midate  ,wird  fett',  medya-  ,fett' (meda-  aus  *mazda-,  idg.  *mad-do-  oder  *mad[e\z-do-  und  =  ahd.  mast ,Mästung';  die  spez.  Bed.  ,Mästung'  also  in  dieser  Bildung  bereits  idg.); mdstu-  n.  ,saurer  Rahm'  (^mad-stu-),  npers.  maskah  ,frische  Butter' (*mad-sk-?)-  ai.  mddya-,  madird-  ,berauschend';
skyth.   Maröag  ,Donau',   PN  BlaSvrjg,  VN  MaTvxhai  ,Donauan wohner';
arm.  matai  ,jung,  frisch,  zart';  macun  , saure,  geronnene  Milch'  (*madio- 4-  arm.  Suff,  -wn);  macanim,  macnum  ,hafte  an,  gerinne';  weitere  iran. Worte  für  Dickmilch  u.  dgl.,  so  npers.  mast  ,saure  Milch',  mäsldan  ,ge- rinnen',  usw. ;
gr.  [j.adad)  »zerfließe,  löse  mich  auf,  verliere  die  Haare';  [j-aöagög  , feucht'; dagegen  fj,a^ög  , Brustwarze'  (=  ahd.  mast,  *mad'-d6s),  ^aorög  ,Brust' (*mad-tös),  i^iaad-ög  ds.  (Umbildung  nach  OTfjd'og  ,Brust');
695
alb.  'manj  (*madnio)  ,mäste^  maim  ,fett^,  maze  ,Rahm,  Sahne,  Haut  auf jer  Milch^  {*madia))  madh  ^Maismehlbrei^,  ablautend  module,  motule  ,Erbse^, jnodhe  ,Lolch^;
lat.  madeö,  -ere  ^naß  sein,  von  Nässe  triefen,  reifen,  voll  sein%  mattus trunken'  {*madi-to-s)'^
air.  maidim  ^breche  (intr.),  gehe  in  Stücke'  (eigentlich  ^fließe  auseinander, zergehe';  formell  =  lat.  madeo) ;  in-madae  ^vergeblich,  ohne  Erfolg'  (dazu wohl  c.  maddeu  ,erlassen,  verzeihen',  abret.  in  madau  ,pessum' ;  gäl.  maistir ,urina' (*7Mac?-^rz-);  mir.  mät  f.  , Schwein'  (*mäddä  ,Mast-Schwßin')  ;
=== leaf 357 ===

ahd.  mast  ,Futter,  Mästung,  Eichelmast',  nhd.  Mast,  Mästung,  ags.  mcBst
,Buchecker';  got.  mats  ,Speise',  aisl.  matr  m.,  ags.  mete  m.,  ahd.  maz  n.
ds.  (nhd.  noch   in  Messer  aus   ahd.  mezzi-rahs),  sowie   got.  matjan  , essen,
fressen',  aisl.  metja  , schlürfen',  ags.  mettan  , füttern',  mnd.  mat(e)   ,Kame-
rad,  bes.   in   der   Seemannssprache'  (Maat),  ahd.  gamazzo  ,Kamerad',  eig.
;.!   ,*Essensgenosse';    dazu   auch   mnd.    met   ,Schweinefleisch',   nnd.  mett  ,ge-
•     hacktes  Fleisch'  als  ,*saftiges,  breiiges  Fleisch',  ahd.  (eig.  ndd.)  Mettivurst
:     (aus  andd.  *matja-)-  ablautend  ags.  as.  mos  , Brei,  Speise',  ahd..  wwo5  ,ge-
kochte,  bes.  breiige  Speise,  Essen  überhaupt',  nhd.  Mus,  Gemüse  (*mädso-).
WP.  II  231  f.,  WH.  II  6f. ;    Kuiper  Nasalpräs.  140.
magh- :  znägh-  ,können,  vermögen,  helfen';  magh-ti-  , Macht'.
Ai.  maghd-  , Macht,  Kraft,  Reichtum,  Gabe',  maghdvan-,  maghdvat- ,kräftig',  iran.  magu-,  apers.  magus  , Magier,  Zauberer'  (daraus  gr.  (.layog, lat.  magus);
arm.  marthankh  ,Hilfsmittel'  (*mag-thra-)]
gr.  (.ifjxog  n.  (dor.  iiä^og),  poet.  (.ifjxaQ  , Hilfsmittel',  (.irjxavrj^  dor.  iiG^avä (>  lat.  machina)  ,Hilf smittel,  Werkzeug,  List' ;
got.  ags.  magan,  aisl.  mega,  maga,  muga,  afries.  muga,  mnd.  mögen,  ahd. magan^  mugan  ,mögen','  1.  Sg.  Präs.  got.  as.  ahd.  mag,  aisl.  mä,  ags.  mseg, afries.  mei;  aisl.  magn,  meg{i)n  n.  , Macht,  Hauptsache',  ags.  masgen,  ahd., as.  magan,  megin  ds.;  got.  mahts  f.  , Macht,  Kraft',  ahd.  as.  mäht,  ags. meaht,  might,  aisl.  mättr  ds. ;
lit.  mägulas  , zahlreich,  viel*;
aksl.  mogg,  mosti  ,können,  vermögen',  jpo-moHi,  Iterat.  po-magati , helfen' usw.,  aksl.  mosth,  russ.  moch  usw.  ,Macht,  Stärke'  (=  got.  mahts).
WP.  II  227,  Trautmann  164 f.,  H.  Güntert,  Weltkönig  108 f.;  falls E.  Fraenkel  (Lexis  1,  169  f.)  richtig  gr.  ^ifjxog  mit  lit.  moJceti  ,können, verstehen'  auf  eine  Wz.  mäkh-  zurückführt,  könnten  die  anderen  Wörter auch  auf  megh- :  mogh-  zurückgehen ;  vgl.  toch.  A  mokats  ,mächtig'.
696
maghos,  -ä  jung^,  maghu-  ^^Knabe,  JüDgliDg,  unverheiratet^  und  zugehörige  # Fem. -Bildungen,  wie  magho-ti-  j'unge  Weiblichkeit^  #
Av.   mayava-  _,unverheiratet' ;  ?f
alb.  makth  junger    Hase^;
kelt.  *magus  in  gall.  PN  Magu-rlx,  urir.  (Ogam)  Maguno-,  air.  mang,  rriug ^Sklave^;  corn.  maw,  bret.  mao  ^Jüngling,  Diener^,  cymr.  meu-dwy  ^Ej^. Siedler*  (
```


## [2026-09-07T15:49:40.924Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=358 && NR<=363 {print \"=== leaf \"NR\" ===\"; print}' POK_02.txt",
 "description": "Print Pokorny leaves 358-363"
}
```


### [2026-09-07T15:49:42.164Z] TOOL RESULT

```
=== leaf 358 ===
eig.  ,Diener  Gottes^);  Fem.  corn.  mowes  ^Mädchen^,  bret.  maouez ,Frau^;  kelt.  -smo-  Ableitung  in  air.  mäm,  mäam(m)  Jugum,  servitus'- Abstraktum  kelt.  *magot-a]ctä  ^Jungfernschaft,  junge  Weiblichkeit^  (weiter« gebildet  aus  *maghotis  =  got.  magaps,  woraus  kelt.  *maJi^k'^ot-aktä  durch Kontamination  mit  mak'ük'!^o-  ,Kind')  in  mir.  ingen  maccdacJit  ^junges erwachsenes  Mädchen^,  air.  ro-macdact  gl.  ,superadulta^,  mcymr.  macliteit\ acorn.  mahtheid  ^virgo^,  mcorn.  maghteth,  maghtyth  ds._,  bret.  matez  ,Dienst- mädchen^;  Koseform  *magguos  in  gall.  Mapo-no-s  GN,  acymr.  map,  ncjmr.  mal  /, ,Sohn^;  doppelte  Verschärfung  in  urir.  maqqas,  air.  macc,  nir.  mac  ,Sobn'j
got.  magus  ,Knabe^,  aisl.  mggr  ,Sohn,  junger  Mann^,  as.  magu  ,Knabe', ags.  mago  ,Sohn,  Mann,  Diener^;  Fem.  *wa(y)ifi  in  got.  mawi  ,Mädchen' (Gen.  maujös),  aisl.  mär  (Akk.  mey)  , Mädchen^,  Demin.  got.  mawilö,  aisl. meyla,  ags.  meotcle  ^kleines  Mädchen^ ;  Abstraktum  *maghotis  junge  Weib- lichkeit^, woraus  konkret  ,Mädchen^,  in  got.  magaps  ,junge  Frau^,  ags. mcßgep  (engL  maid),  as.  magath,  ahd.  magad,  nhd.  Magd,  Demin.  Mädchen] lett.  mac  (aus  ma§s)  ,klein^
WR  II  228,  Feist  3  339.
mag-  , kneten,  drücken,  streichend
Gr.  fxayfivaL,  i-ie^-iayiievirj  zu  ixdaao)  (zum  Präs.  s.  mendk-  ,kneten^),  (xaysvg ,der  Knetende^,  f^aylg  f.  .geknetete  Masse^,  (.idysigog  (eigentlich  ndyiqoq) ,Koch',  (.laySccXla  ,Stückchen  Brot  zum  Fettab wischen*^;  f.idyiTQci  f.  ,Backtrog';
mir.  maistrid  ,buttert^  (*magis-tr-),  bret.  meza  ,kneten^,  cymr.  maeddu ,kämpfen,  stoßend  durcheinandermischen^  (*maged-) ;
abg.  mazQj  mazati  ,salben,  schmieren*,  russ.  mazh  ,Salbe^,  abg.  maslo ,Butter,  Öl,  Salbe*  {*mag-slo-),  masth  ,Salbe,  Fett*  (*mag-sti-),  lett.  iz-muözet ^überlisten,  zum  Narren  halten*;
mit  bes.  Anwendung  auf  den  Lehmbau  die  Sippe  von  nhd.  machen  (aus ,kneten,  formen,  zusammenfügen,  von  der  mit  Lehm  verstrichenen  Wand; geformt,  passend),  as.  {gi)-makön  ,machen,  errichten,  bauen*,  ahd.  mahhön ds.,  nhd.  machen,  ags.  macian  ,machen,  verursachen* ;  as.  gemaco  , Genosse, Seinesgleichen*,  ahd.  gimahho  ,socius*  (gimahha  ,conjux*),  ags.  maca  ds., gemcecca  ,ds.,  Gatte*  (aisl.  maki  ,aequalis*  ist  ndd.  Lw.),  ahd.  ga-mah,  gi-mah ,zugehörig,  passend,  bequem*  (^maÄ  , Verbindung,  häusliche  Bequemlichkeit, Gemach*),  un-gamah  ,malus,  minus  idoneus*,  ags.  ge-mcec  ,passend,  tauglich.
697
(aisl.  makr  ^passend,  bequem^  ist  ndd.  Lw.);  afries.  mek  n.  ^Verheiratung^;, jjiekere   ^Ehenunterhändler^^    mhd.   mechele    , Kuppelei^ ;    aus    germ.    *makö stammt  lat.  mac{h)iö  ,Maurer';   daraus  rom.  *matsiö,   woher  wieder  ahd. stein-
=== leaf 359 ===
mezzo  ,Steinmetz^ WP.  n  226 f.,  WH.  II  3,  Trautmann  173;  vgl.  2.  mak-  und  menk-.
0agh'  .kämpfend
Gr.  ld(xa^ü)Vj  Lw.  durch  äol.  Vermittlung  aus  einem  iran.  Volksnamen *ha-mazan-  , Krieger^,  vgl.  äf.ia^ay,aQav  ( :  ar.  kar-  , machen^) '  Ttolsf-istv. n€Q(^cci^  Hes.  und  ä^a^avwdsq '  al  ^rjXsai  (vom  VN  Hamazan-) ;  gr.  (j,dxojAaL ^kämpfe^,  (.idxr]  ;Kampf,  Schlacht^^  (.iccxaiga  , Schwert^  Messer^  (fem.  zu *liax(ov  ,schneidend^?  Oder  semit.  Lw.^  zu  hebr.  mekherah  ^Schwert^?).
WP.  II  227,  WH.  II  3,  4.
X.  mai-  ,hauen,  abhauen,  mit  einem  scharfen  Werkzeug  bearbeiten'^,  wohl eigentlich  wai-  und  s-lose  Form  neben  smei-  :  smdi-  :  srrvt-  ^schnitzen, mit  einem  scharfen  Werkzeug  arbeitend
1.  Air.  mdel  ,kahl,  stumpf,  ohne  Hörner^,  acymr.  mail  ^mutilum^,  ncymr. moel  ,calvuS;  glaber^  {^mai-lo-s  , abgehackt^) ;
2.  d-Er Weiterung:  got.  maitan  ^hauen,  schneiden^  aisl.  meita,  ahd.  meizan ^schneiden^,  aisl.  meitill  tu.,  ahd.  meizil  , Meißel^;  ahd.  stein-meizo  , Stein- metz^; dazu  ags.  mite,  ahd.  mlza  ^Milbe^  (wohl  zu  gr.  [xldag  ^Made^),  viel- leicht auch  ags.  se-mette,  engl,  ant,  emmet,  ahd.  ä-meiza  , Ameise^  (^Abschnei- der^);  ob  auch  abg.  medh  ;Erz^,  russ.  mädh  , Kupfer^?
3.  ^-Erweiterung:  ai.  mtthati  , verletzt*^  (expressives  th),  gr.  (.litvXog  ,ver- stümmelt,  ohne  Hörner^;,  (.uaiuXlco  ^zerstückle  (Fleisch/ ;  aisl.  meida  , kör- perlich verletzen,  verstümmeln;  vernichten'^;,  mhd.  meidem  ^männliches Pferd^  (eig.  ^Kastrat^)^  got.  *gamaip-s  ^verkrüppelt^,  wozu  (wohl  nach  dem Hofnarren)  ahd.  gimeit  ^verrückt^,  mhd.  in  bonam  partem  gewendet  gemeit ^lebensfroh;  keck,  schön,  lieV,  as.  gimed,  ags.  gemäd,  maeded  ^verrückt^, engl,  mad  ds. ;
alit.  ap-maitinti  ^verwunden',  lett.  mäität  ^verderben,  vernichten*^,  lit. maltelis  ^verschnittener,  gemästeter  Eber^,  apr.  nomaytis  ^verschnittener Eber^,  ismaitint  ,verlieren^  (wie  it.  perdere)-  anders  Mühlenbach-Endzelin II  552.
WP.  II  212;  Holthausen  Altwestn.  Wb.  193,  194.
2.  mai-  (moi-?)  ;beflecken;  beschmutzen'?
Gr.  (.ualvü)  (Aor.  i^ilav)  ;beflecke;  besudle^,  fiiaa^a  n.  ,Befleckung'; (XLagög  (*miu97'os?)  ;besudelt';  ^LaL-q)6vog  ,mit  Mord  befleckt^;
ags.  mal  n.  ,Fleck;  MakeF;  ahd.  meü  n.,  meila  f.  ds. ;  lit.  PI.  mieles, lett.  mteles  ;Hefe';  vielleicht  .auch  lit.  mdiva  ^Sumpfwiese^?
WP.  II  243.
698
mak-  etwa  ,Haut-,  Lederbeutel'.
Cjmr.  megin  , Blasebalg^  {^makmä)-^
ahd.  mago  ^Mageu^,  ags.  maga,  engl,  wau;, Kropf,  Magen^,  aisl.  magi  ,Mao-en».
lit.  mäkaSj  mekeris  , Geldbeutel^;  lett.  maks,  Demin.  macinSj  maJcelu ,Beutel,  Tasch
=== leaf 360 ===
e^,  makstis  ^Scheide^,  lit.  maksnä  ^Futteral^,  makUis  ^Scheide (des  Degens  oder  Messers)^,  apr.  danti-max  , Zahnfleisch^;  aksl.  mo^%rui ^Beutel' ;
unsicher  ist  Zugehörigkeit  von  air.  men  (aus  *makno-  oder  ^mekncA ,Mund,  Bucht',  menaigte  ,qui  inhiant^
WP.  II  225,  Trautmann  166.
1.  mäk-  ,naß;  feuchtend
Arm.  mör  ,Kot,  Schlamm,  Sumpft  (*mak-ri-)  ]  alb.  make  ,Leim,  Haut auf  Flüssigkeiten^;
lit.  makone  ,Pfütze^,  makentij  maknöti  ,durch  Kot  waten',  wohl  auch  lett. mäkuonis  , Bewölkung,  dunkle  Wolke',  apmäkties  ,sich  umwölken';
abg.  mokr^  ,naß,  feucht',  mocg,  -iti  „ßgsxsLv^^  russ.  möknuth  ,naß  werden' mocüh,  Iterat.  mdcivath  ,naß  machen,  anfeuchten',  mocd  ,Urin',  mo^aq , feuchter,  sumpfiger  Ort';  vgl.  ligur.  FIN  Macra^  span.  FIN  Magro]
dehnstufig  slav.  *makaJQ,  *makati  in  öech.  mdkati,  mdceti  ,nässen',  usw.
WP.  II  224  f.,  Berneker  II  8,  69  f.,  Trautmann  167.
2,  mäk-  ,kneten,  quetschen,  drücken'.
Lett.  mäcu,  mäkt  ,drängen,  drücken,  plagen,  quälen',  cech.  mack-dm, -ati  , drücken,  pressen'  (Deminutivbildung,  ein  einfaches  *makati  voraus- setzend) ;
lat.  *maccare  aus  *mäcäre,  vorausgesetzt  von  ital.  ammaccare  ,quetschen', usw.,  vgl.  Meyer-Lübke  REW  5196;
hierher  auch  lat.  mäcei-ia,  mäceries  f.  ,Mauer  als  Umfriedigung  um Garten,  Weinberge  usw.'  (als  ,aus  Lehm  geknetete,  mit  Lehm  gebundene Mauer',  vgl.  Tstxogiß'ngö)]  dazu  mäceräre  , einweichen,  mürbe  beizen'.
Vgl.  die  ähnlichen  Wurzeln  menk-  und  mag-.
WP.  II  224,  WH.  II  2  f.,  5.
mäk{en)-  ,Mohn'?
Gr.  ixrf/.ojv,  dor.  f.i6y.(üv  ,Mohn' ;  ahd.  as.  mäho,  mhd.  mähen^  man  und mit  gramm.  Wechsel  ahd.  mägo,  mhd.  mage,  nhd.  hair.  magen  ,Mohn', ndd.  man,  ndl.  maan-kop,  aschwed.  val-mughi,  -moghi  ,Mohn'  (im  ersten Gliede  *ivalxa-  Betäubung') ;  mlat.  mahonus  ,Mohn'  und  lit.  magöne  — woneben  dunkles  aguonä  —  stammt  aus  dem  Germ.,  apr.  moke  aus  dem Poln. ;  ksl.  (usw.)  mak^  ,Mohn'.
WP.  II  225,  Trautmann  166.
r
B  699
I     toaio'  0^6^  n2ok-o-(-lo-,  -ko-,  Deminutivformantien)  ^Stechfliege,  Mucket
P  ^i.  maädha-  m.  ^Stechfliege,  Mücke^,  lit.  masalas  ,Mücke^,   lett.  masalas
Roßfliege*^,  wozu  russ.  mosölith  ,plagen,  zudringlich  anbetteln'  (vom  Bilde
Jes  zudringlichen  Mückenschwarms),  und  mit  anderm  Formans  (*mos^th?)
osorb.    raoscic   so,   moscec   so   ^wimmeln   (wie  ein   Mückenschwarm)',  sowie
wohl  auch  lit.  maUju,  -ti  ,ein  Kind  zeugen';
vgl.  mit   Velar   die   arische   Sippe  von  ai.  mdJcsa-  m.,  maksa  f.  , Fliege' a,v.  maxsi-  , Fliege,  Mücke'  usw.,  und  lit.  mäkatas  ^Kriebelmücke'. WP.  TT  225,  Specht  Idg.  Dekl.  43  f.,  Trau
=== leaf 361 ===
tmann  170.
mäk-  :  mok-  ,lang  und  dünn,  schlank' ;  mskrös  ds.
Av.  mas-  ;lang',  Komp.  masyä  ,der  größere',  Sup.  masista-^  ap.  mad-iHa- ^der  höchste',  av.  masah-  n.  ,Länge,  Größe'  {*mas-  für  *mis-  aus  idg.  mds- durch  Einfluß  von  mazyä  ^größer' :  f-isyag),  gr.  ^(^ooco,  ^äoawv  (*^ä7iiwv)  neben ^äaaov  (nach  Etaoov  ,näher')  ,länger',  iir^yLiOToq  ,der  längste',  fA,7Jy.og,  dor. [.lä-aog  n.  , Länge',  Mdxsra  , Hochland',  May.£dövsg  daher  ^Hochländer', ^ayieövög  , schlank',  nachhom.  ^rjy.edavög  ds.,  (.lav^gög  ,lang'  (=  lat.  macer , dt.  mager)-  vielleicht  (.id'/,aQ  n.  , Glückseligkeit';
lat.  macer,  -cra,  -crum  ,mager',  maceö,  -ere  ,mager  sein',  macies  f.  ^Ma- gerkeit' ;
vielleicht  hierher  air.  mer  m.  ,Finger'  {*makro-)]
ahd.  magar,  3i,gs.  mceger,  aisl.  magr  ,mager';  dazu  mit  Z-Suffix  hitt. 7na-ak-la-an-te-e§  (maklantes)  Nom.  PI.  ,mager'.
WP.  II  223  f.,  WH.  II  2,  Benveniste  BSL.  33,   140  f.
makh-o-Sf  -(s)lo-  , ausgelassen'?
Ai.  makhd-  ,munter,  lustig,  ausgelassen',  m.  ,Freudenbezeigung,  Feier'; gr.  (.idx^og  ,geil,  üppig  (von  Weibern);  in  wilder  Lust  tobend'. WP.  II  226.
mand-  ,Rutenverflechtung  als  Hürde,  Band  aus  Reisern  gedreht'?
Ai.  mandurä  ,Pferdestall',  mandirdm  n.  ,Haus,  Gemach';  gr.  (illjr.  ?) Hdvöqa  f.  ,Pferch,  Stall,  Hürde',  {.idvdalog  ,Riegel';  thrak.  ^lavöd-Kr^g  , Garben- band';  illyr.  ON  Mandurium  oder  Manduria  (Calabrien);  falls  Grund- bedeutung ,Pferdestall,  Pferdezaum',  vielleicht  zu  inendo-  ,Tierjunges', S.  729.
WP.  IT  234,  Krähe  Festgabe  Bulle  205  f.
mä-no-,  mä-ni-  , feucht,  naß'.
Lat.  mänö,  -äre  ,fließen,  strömen',  daher  , entspringen' ;  bret.  Vannes  man ,Moos,  Flechte',  cymr.  mawn  ,Torf'  aus  brit.  *möm-,  woraus  entlehnt  air.
700
möin   f.    ^Moos,   Sumpf,    Torf^;    vielleicht    dazu    ablaut.    asächs.    -mannia -mennia  in  FIN  und  ON,  wie  Throtmennia  ,Dortmund^,  usw. WP.  11  224,  WH.  II  30f.,  J.  Loth  RC  42,  91  f.
manu-s  oder  monu-s  ,Mann,  Menscht
Ai.  manu-,  mdnus-  , Mensch,  Mann^  (auch  , Ahnherr  der  Menschen'),  av im  PN  Manus-cid-ra-,  urgerm.  *manuaz  im  PN  Mannus  (Tacitus),  Stamm- vater der  Deutschen,  got.  manna  (Gen.  mans),  aisl.  madr,  mannr,  a^ afries.  ahd.  mann  ,Mann',  got.  mannisJcs,  aisl.  mennskr,  ags.  ahd.  mennUc ,menschlich^;  ahd.  mannisho  usw.  ,Mensch^;  aksl.  moh,  russ.  muz  ,Mann* (*mangia-y  Suffix  ähnlich  wie  in  lit.  zmo-g-üs  ,Mensch^).
WP.  II  266,  Trautmann  169;  vielleicht  zu  3.  men-  ^denken^
marko-  _,Pferd^;  nur  kelt.  und  g-erm.
Ir.  marc,  cymr.  usw.  march  ,Pferd^,  gall.  y.aQY.av  Akk.  Sg.,  Marco- durum  ON;
ahd.  marali,  ags.  mearTi,  aisl.  marr  ,Pferd'  (nhd.  in  Marschall,  -stalV)^ fem.  ahd.  meriha,  ags.  miere,  aisl.  merr,  nhd.  Mähre.
WP
=== leaf 362 ===
.  II  235.
1.  matb-    oder    moth-  in  Worten   für   nagendes,   beißendes    Gewürm   oder
Ungeziefer?? Arm.  mat'il  ,Laus^;  got.  mapa,  m.  ahd.  mado,  ags.  mada  ,Wurm,  Made', aisl.  mapJcr  ds.,  aschwed.  matk,  finn.  Lw.  matikka  ,Würmchen^ WP.  II  228,  H.  Petersson  z.  Kenntnis  der  Heterokl.  32  f.
2.  mat-  etwa  ,Hacke,  Schlegel'.
Ai.    matyd-   n.    ;,Egge   oder   Kolben    oder    dgl.',   matlkrta-    ,geeggt  oder  H gewalzt^ ;  lat.  mateola  ,Werkzeug  zum  Einschlagen  in  die  Erde'  (im  Roman, lebt  nicht  deminuiertes  *mattea  ,KeuleQ;  ahd.  (gl.)  medela  , Pflügt  (Lehmann AfneuereSpr.  119,   188);    aus   vlat.   mattiuca:    ags.    mattoc,   engl,   mattock , Hacke',  abg.  motyka  ,Hacke^;
WP.  II  229,  WH.  II  49.
mäter-  ,Mutter^,  beruht  auf  dem  Lall  wort  mä,  s.  dort.
Ai.  mätär-  ,Mutter^,  av.  mätar-,  arm.  mair  ds.  (Gen.  maur  ==  gr.  [irjTQÖg usw.);  aphrjg.  Nom.  Akk.  (.larag,  (.lazegav,  Gen.  fj,aTSos^j  gr.  f-ii^TTjQ,  dor. IxätriQ  (mit  verschobenem  Nominativakzent  wie  dvydrrjQ)',  dazu  hom. j7](.iriTTjQ,  thess.  Jaf.iixÜT8QL',  alb.  motre  , Schwester^  (ursprüngl.  ,die  ältere, Mutterstelle  vertretende  Schwester');  lat.  mäter,  -tris  ,Mutter,  Amme, Quelle',  osk.  maatreis,  umbr.  matrer  ,matris^;  gall.(?)  Margsßo  ,Matribus'; air.  mäthir  , Mutter'  (cymr.  modrydaf  ,Bienenstock'  mit  hydaf  ,Nest  wilder
701
ßienen'  als  2.  Glied);  abd.  muoter,  ags.  mödor,  aisl.  mödir  ^Mutter*;  lit.  möte /Gen.  alit.  motes,  lit.  motefs)  ^Weib,  Ehefrau^  (mötyna  ,Mutter^,  motera prauenzimmer,  WeiV),  lett.  mäte  ,Mutter',  apr.  müti,  mothe  ,Mutter^ ipoinatre  , Stiefmutter^) ;  aksl.  mati  (Gen.  matere)  ,Mutter*;  tocb.  A  mäcar, ß  mäcer.
An  Ableitungen  (z.  B.  mätruuiä)  vgl. :
ai.  matrka-  .mütterlich',  m.  ,Mutters  Bruder',  mätrlcä  ,Mutter,  Groß- mutter^; aber  ncymr.  modryb  ,Muttersschwester',  acymr.  modrep-ed  PL, abret.  motrep,  nbret.  moereb  ds.  {*inätroh*J^ä.,  zu  ok^-  ,sehen^,  als  ,wie  eine Mutter  aussehend^);
o-r.  ftrjTQa  f.  ^Gebärmutter,  Mark  der  Pflanzen',  lat.  matrlx  ,Gebärmutter ; Zuchttier^,  ahd.  muo^ar  ,Baucli  einer  Schlange^,  andd.  möder,  afries.  möther jBrustbinde  der  Frauen^,  mhd.  müeder,  nhd.  Mieder;
arm.  mauru,  Gen.  maurui  , Stiefmutter^  (*mätruuiä  ==)  gr.  ^rjTQvtd  ,Stief- mutter^,  zum  w-St.  erweitert  in  ags.  modrige,  afries.  mödire,  mnd.  m'ödder ,Mutters  Schwester^  (*mödruuiön-,  ahd.  muotera  ds.  nach  muoter  um- gebildet?), mit  hochstuf.  Formans  *mätrö[ü']- :  gr.  fxrjTQwg,  -w[/]og,  dor. ^ätQOig  , Oheim  oder  Großvater  mütterlicherseits^,  ^rjTQWLog  ,mütterlich' (B
=== leaf 363 ===
ed.  nach  f-irjzrjQ  verändert);
lat.  mätröna  ,Ehefrau' ;  mätertera  ,Mutters  Schwester^  (*mätro-tera)] mäteria,  mäteries  ,Schößlinge  von  Fruchtbäumen,  Bauholz,  Nutzholz, Material^;  gall.  FIN  MätrÖna  ,Marne^=  cjmr.  GN  Modron  f.
slav.  *mätero-  in  russ.  materöj  ,außerordentlich,  groß,  stark,  fest',  serb. mätor  ,alt,  bes.  von  Tieren^,  abg.  materhstvo  „nosaßsTov^'^  (:  lat.  mäteries).
WP.  II  229  f.,  WH.  II  49  ff.,  Berneker  II  25,' Trautmann  170  f.
mau-ro-  ,matt,  schwach,  lichtschwach,  dunkel';  auch  m(a)ud-  ds.
Gr.  {d:)idavQ6g  ,schwach;  nebelhaft;  blind',  (d)fxavQ6(jt)  »entkräfte,  schwäche, verdunkle' ;
anord.  meyrr  ,mürbe^;
russ.  (s)muryj  , dunkelgrau',  chmüra  , dunkle  Wolke',  dech.  chmouriti, smoufiti  se  ,sich  trüben,  sauer  sehen'  (u.  dgl.);
vielleicht  dazu  gr.  df-ivögög  , dunkel,  schwer  zu  erkennen,  schwach',  äfxv- dgöo)  ,verdunkle,  schwäche',  äf-ivögörrig  ,Undeutlichkeit,  Schwäche',  aksl. ^z-m^däti,  u-m^dngti  , schwach  werden'.
WP.  II  223.
mazdo-s  , Stange,  Mast'.
Lat.  malus  m.  ,Mast,  Mastbaum'  (mit  ,sabin.'  Z  =  d  aus  *mädos,  *mazdos oder  Anlehnung  an  pälus)  ==  ahd.  mast  ,Stange,  Fahnen-  oder  Speer- stange,   bes.   Mastbaum',   ags.  mcest  (aus   mnd.   mast  stammt  norw.  was^r
702
jMastbaum*);  mir.  maide  , Stock'  (air.  *maite,  d.  i.  *maidde^  aus  *mazdio  ^ air.  matan  , Keule',  mir.  ad-mat,  nir.  adhmad   ,Bauholz'.    Als  germ.  Lehn* wort    betrachtet    Schrader    RP    168    abg.   mosti    ,Knüppelbrücke',    russ   ^ mostovdja  ,Pflaster',  po-mos<^  , Diele';  eher  ist  es  ein  urverwandtes  Kollek* tiv  *mazd-to-  , Stangenwerk'. WP.  II  935  f.,  WH.  II  19.
1.  me-  oblique   Form   des   Pers.-Pron.  der   1.  Sg. ;    Nom.  ßg.   eg{h)om   ,ich*  —
(S.  291).
Gen.  betont  *ine-nie  ,von  mir,  meiner'  in  ai.  mdma-j  dissimil.  *me'n^ in  av.  mana,  apers.  manä ;  cymr.  /?/",  Bret.  ma,  Vannes  me  (als  Posses- siv);  ksl.  mene,  lit.  mane'^  anders  dissimil.  *eme  in  arm.  im,  gr.  hom. il^islOy  usw. ;  7^
Dat.  betont  me-ghi  ,mir'  in  ai.  mdhy-a(m)^  lat.  miÄi,  umbr.  mehe]  arm. inj  aus  *emegh- ;  enklit.  moi  (auch  als  Gen.)  in  ai.  me,  me,  av.  me,  gthar. moi;  gr.  ^wot;  air.  infig.  und  suffig.  Pron.  -m-;  alit.  mi,  apr.  maiy;  hitt.  -mi*
Akk.    1226   in   ai.    av.    mä  (enklit.),    arm.    is   (*em.e-^e?),   lat.   me(d),  gr.  ^- i(.i€,  (xe;  air.  messe,  me  (,ich'),  infig.  und  suffig.  Pron.  -m-  (cymr.  mi  ,ich* mit  i  nach  ^i  ,du') ;    i22e-i22   in  ai.  betont  mäm,  av.  mq/m,  alb.  mwa,  mw«, apr.  mie«,  aksl.  m^;  mit  -ge  erweit.  gr.  ifie-ye,  ven.  mexo,  got.  miÄ;,  mich*, usw.,  hitt.  am
```


## [2026-09-07T15:50:04.916Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la POK_full.txt && grep -n -i \"maksa\\|mak.sa\\|Stechfliege\" POK_full.txt | head -30",
 "description": "Search POK_full for fly root"
}
```


### [2026-09-07T15:50:04.978Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
57360:compare with velar the Aryan family of Old Indie maksa- m., maksat 'fly', Avestan
```


## [2026-09-07T15:50:06.246Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"699\" POK_full.txt | head -20; echo ---; grep -n -i \"makros\\|mager\" POK_full.txt | head -20",
 "description": "Explore POK_full structure"
}
```


### [2026-09-07T15:50:06.327Z] TOOL RESULT

```
40320:References: WP. I 699. 
40650:References: WP. I 699, WH. I 617 f. 
57320:Page(s): 699 
57365:Page(s): 699 
57388:Page(s): 699 
57587:Page(s): 699 
57701:Page(s): 699-700 
77929:References: WP. II 707, SchwyzerGr. Gr. 1, 649, 698, 699. 
79082:References: WP. II 699 ff., WH. II 165, Trautmann 197, Vasmer2, 213 f. 
86239:References: WP. I 732 ff., WH. II 671 f., 699, Mayrhofer 1, 480, 483, 484, 487, 497, 503, 
87226:References: WP. I 755, WH. II 699. 
---
29782:large', Serbo-Croatian gdlem^b\<^, large', russ. dial. goljamyj^\\\<^\\, mager' and Adv. 
57575:MaKp6(; "long' (= Latin macer, German mager^Mn'); perhaps iJOKap n. " blessedness, 
70202:See also: in addition rkl=>os 'bear' as ' damager '. 
71223:interprets the bear as " destroyer, damager ', to Old Indie raksas- n. " destruction ', 
75356:hard, rough, unbeugsam', aK£Ai(pp6(; 'ausgetrocknet, abgemagert', aKAr|cpp6(; 'small and 
75570:creature', skrumpa ' magere cow', engl. 5/7/7/77^ "toddler' (besides with Germanic -/77/77-: Old 
75580:High German Swiss barpf magere cow, boses woman'; here Old Icelandic harpa. Old 
75588:"cramp'. Old Icelandic /7/'(9/0/0/'"Distrikt', Norwegian /'5/77yC>"magerer person', engl. dial, rump 
75589:"magere cow'; (but Norwegian rump^ dull mountain top; buttocks ', Middle Low German 
77342:High German 5caofc» 'damage', noun agentis Old English sceada^ damager, devil'. Old 
77346:Saxon scatho, Old High German scado^ damager, fiend'; witli gradation oas in imperfect
```


## [2026-09-07T15:50:10.162Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '57330,57400p' POK_full.txt; echo \"=====MAK=====\"; sed -n '57550,57600p' POK_full.txt",
 "description": "Print POK_full p.699 entries"
}
```


### [2026-09-07T15:50:10.235Z] TOOL RESULT

```
Old High German mago' stomach ', Old English maga, engl. maw'craw, stomach', Old 
Icelandic /775^/"stomach'; 

Lithuanian makas, mekeris^ pocket, purse '; Latvian maks, Demin. macins, makelis 
"bag, pouch ', makstis^ a scabbard, sheath ', Lithuanian maksna^ sheath ', makstis^ a 
scabbard, sheath (of sword or knife)'. Old Prussian dant/'-max' gums, gingiva '; Old Church 
Slavic mosbna^bag '; 

doubtful is affiliation of Old Irish men {from *makno- or *mekno-) 'mouth, bay', menaigte 
" qui inhiant '. 

References: WP. II 225, Trautmann 166. 
Page(s): 698 

Root / lemma: mahRo- or mohR-o- {*mahgho-) 

Meaning: a kind of fly 

Note: (-/o- -ko-, diminutive formants) 

Material: Old Indie masaka-m. "horsefly, biting housefly, mosquito ', Lithuanian masalas^ 

mosquito ', Latvian masalas' measles ', wherefore russ. mosolitb 'plague, torment, beg 

obtrusively ' (of the form of obtrusive swarm of mosquitoes), and with other forms 

( *mosbtbl) Upper Serbian moscic so, moscec so " to swarm (as a swarm of mosquitoes) ', 

as well as probably also Lithuanian masoju, -//'beget a child '; 

compare with velar the Aryan family of Old Indie maksa- m., maksat 'fly', Avestan 
maxs/-l\y, mosquito ' etc., and Lithuanian makatas' blackfly '. common Old Indie gh- > 
ks- : Old pers. gh- > xs- : npers. xs- > s- 

References: WP. II 225, Specht Indo Germanic Dekl. 43 f., Trautmann 170. 
Page(s): 699 

Root / lemma: mahnd- 

Meaning: hurdle, plaited twigs, horse fence, stable 

Note: 



Root / lemma: rnand-: hurdle, plaited twigs, horse fence, stable, derived from Root/ 
lemma: mend- mond-{mQd-l)\ to suck (breast), to feed; breast. 
Material: Old Indie mandura^ stable ', mandiramu. 'house, chamber'; gr. (Illyrian?) 
pav5pa f. 'corral, pen, fold, stall, hurdle ', \\bNbaKoQ, 'bar, bolt'; thrak. [jav5aKr|<; ' 
Garbenband '; Illyrian PN Mandurium or Mandur/a {Ca\abnen); whether primary meaning ' 
stable, horse fence ', perhaps to mendo-' the young of an animal ', S. 729 (mend-). 

Note: 

The inanimate suffix -ur- . Old Indie mandura^ stable ' : UAupioi , oi, lllyrians, UAupia , n, 
lllyria, also'lAAupi? , n. Adj. 'lAAupiKO^ , n, 6v, Illyrian: -kx\, the region or province of lllyria, 
'lAAupi^io , speak the Illyrian language, 'IAAupia:--hence Adv. 'lAAupiaii. 
References: WP. II 234, Krahe Festgabe Bulle 205 f. 
Page(s): 699 

Root / lemma: mahnu-sor mohnu-s 
Meaning: man 

Material: Old Indie manu-, manus-' person, man, husband' (also ' male ancestor of the 
people'), Avestan in PN Manus-ci&ra-, proto Germanic *manuaz\n PN A^5/7/7i/s (Tacitus), 
ancestor of the Germans, Gothic manna {Ger\. mans), Old Icelandic madr, mannr. Old 
English Old Frisian Old High German mann^rr\ar\, husband', Gothic mannisks. Old 
Icelandic mennskr. Old English Old High German mennisc^ human, of human beings, of 
people; humane'; Old High German mann/sko etc. 'person'; Old Church Slavic mozb, russ. 
muz'mar\, husband' {*mang/a-, suffix similarly as in Lithuanian 27770-^-^5 'person'). 
Maybe the root word is related to the name of the moon in PIE; Mene/aus 'rr\oor\ god?'; 
=====MAK=====
Material: Lett, macu, makt'urge, push, press, plague, torment, smite', Czech mack-am, - 

atr press ' (diminutive formation, assuming a basic *makati); 

here also Latin maceria, macen'est " a wall of soft clay, enclosure, wall '; in addition 
macerare^ to make soft, make tender, soften, soak, steep, macerate'. 

References: WP. II 224, WH. II 2 f., 5. 

See also: compare the similar roots menk- and 7775^-. 

Page(s): 698 

Root / lemma: mahR- : mahR- 



Meaning: long, slender 

Material: Avestan mas-long', compounds masya' the great ', Sup. masista-, ap. madista- 
" the highest ', Avestan masah-n. "length, greatness, bulk, extent' ( */775S- for */77/s- from 
Indo Germanic /77a5- through influence of mazya' further, extra, in additional amounts, 
more ': M£YC«;). Qf- V^OQbi, jjaaawv (*fjaKiu)v) besides paaaov (after aaaov ' nearer, closer 
') "langer', pr|KiaTO(; ' the longest ', fjr|KO(;, Doric poKOt; n. "length', MaKsra ' highlands, 
mountains ', MokeSovec; hence ' highlander', |jaK£5v6(; " slim ', nachhom. |jr|K£5av6c; ds., 
MaKp6(; "long' (= Latin macer, German mager^Mn'); perhaps iJOKap n. " blessedness, 
happiness, felicity, good fortune '; 

Latin macer, -era, -crum '\ean', maceo, -ere^ to be lean, meagre ', mac/est " leanness, 
thinness, meagreness, atrophy '; 

perhaps here Old Irish merm. 'finger' {*makro-); 

Old High German magar. Old English maeger. Old Icelandic magr'\ean'; in addition with 
Asuffix Hittite ma-ak-la-an-te-es {maklantes) Nom. PI. 'lean'. 

References: WP. II 223 f., WH. II 2, Benveniste BSL. 33, 140 f. 
Page(s): 699 

Root / lemma: mah-1 

Meaning: to beckon with the hand; to deceive 

Note: (extended maih-1) 

Material: Old Indie maya^ transformation, dream image, phantasm, ghost, deceit, illusion ' 

(or to 3. me-1); 

gr. pnvuoj, Doric pavOw ' zeige an, verrate ' from *|ja-vu-|ji ' wave with the hand '; s- 
extension paiopai 'touch, inspect'. Put. \\doao\\a\, tu\-\xaGioc, 'touched' = 'stained',
```


## [2026-09-07T15:50:26.975Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT leaf 216 (p.201) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==216' KNT.txt | head -60; echo \"=== KNT grep maOista/mathista ===\"; grep -n -i \"mathista\\|ma0ista\\|maOista\\|maθišta\\|maθista\" KNT.txt | head -20",
 "description": "Kent p.201 and maθišta"
}
```


## [2026-09-07T15:50:27.752Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 904 (p.880) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==904' SYN.txt | head -70",
 "description": "Buck p.880"
}
```


### [2026-09-07T15:50:28.378Z] TOOL RESULT

```
=== KNT leaf 216 (p.201) ===
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).
duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, Bthl. AYW 767), pres. druZasti, sb. druzé ‘principle of evil, devil’, Skt. drúhyatí ‘deceives’, Gm. trügen, pIE *dhrugh- (876.111). See alsodrauga-. adu- rujiya imf. (§101, $103.IV, $113, 5128, 4132.1, 2, 3, $214, 5228.11) DB 1.39, 78; 3.80; 4.8, 10f, 13, 16, 18, 21, 24, 261, 29; DBb 2; DBc 2; DBd 2; DBe 3f; DBf 1; DBg 2; DBh 2f; ОВ! 2f; DB} 2f. adurujiyasa" 3d pl. imf. ($214, §218.1, $232.III) DB 4.34f. duruxiam nsn. past pte. pass. ($103.IV, $122, $128, 8132.1, 3, $242.I) DNb 52, 5f; asn. DB 4.44f, 49f.
duruva- adj. ‘firm, secure’: Av. drva-, Skt. dhruvd-; deriv. to root in OP ‘dar- ($122, $128, $150). durwä nsf. DB 4.39.
duvatsta- adj. ‘very long, very far’: superl. to dūra- ($156.IIL, §190.11 $191.0; МВ Gr. $275), ef. Skt. davisthd- with slightly different formation.
192 OLD PERSIAN
duvais[ta]m asn. as adv. ‘for a long time’ DPe 23 (cf. remarks s.v. hyà).
duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvarayd-maiy lsn. ($186) DB 2.75; 89f.
duvari- sb. ‘portico, colonnade’: duvar- ‘door’ + varði- ‘cover, protection’, to root var- ‘cover’, with haplology ($34, $129, $152.IV, §160.Ia; ВЫ. AIW 766). duvarfim asm. XPa 12.
duvitdparanam adv. ‘one after the other, in succession’, a meaning agreeing with Elam. Samak- mar ‘ex ordine’: duvità ($191.11, $204.IT), MPers. dit ‘one or other of two’ (Bthl., quoted by Tm. Lex. 102), ef. OP duviliyam ‘a second time’, Skt. 0015 ‘twice’, Lt. bis, + paranam ‘before, previ- ously’ (Tm. 1.е., and Vdt. Stud. 1.8). This is better than Tm.’s "long aforetime', adv. duvità ong’, GAv. дайа, Skt. dvità (cf. OP duvaistam), + paranam (as above); also than KT's duvità- parnam ‘in two lines’, contaming the cognate of Skt. parnd- ‘wing’ (supported by Wb. ZDMG 61.724-5, KIA 10-1, and by Hz. AMI 1.112n). DB1.10; DBa 17.
duvitiya- adj. ‘second’: GAv. daibitya-, LAv. bitya-, Skt. dvitiya-, pLE *dyitiio- (676.11, 51441, 5204.1). See also duwilàáparanam. дилат, asn, as adv. ‘a second time’, DB 2.87f, 57, 3.77; as inner obj., ‘a second (uprising), DB 3.24 (not duvitiya-ma udapalalà ‘was second to rise up from me’, as Bthl. AiW 964 takes it, since udapatatà nowhere else takes an expression of the person against whom uprising is made).
duš- insep. prefix ʻi: Av. dui-, Skt. dus-, Gk. dve- ($76.Ш); in dušiyāra-, duskarta-.
dusiyara- sb. ‘evil year, bad harvest, famine’: duš- + yar- ‘year’ made thematic, Av. ydr-, Gk. ёра ‘season’, NGm. Jahr ($140.VIT, $143.IT). dušiyāram nsn. DPd 19. dudiyard absn. DPd 17.
| du$karia- ad). ‘ill-done’, opposite of naiba- (Hz. ApI 1434): duš- + karta- ‘done, made’, past pte. pass. tokar-. duskartam nsn. DSe 31f; XPh 42. draug- vb., see duruj- and draujiya-.
drauga- sb. *the Lie", the evil force opposed to Ahuramazda, Ávestan Druj: Av. draoga-, NPers.
dury, Skt. drógha- droha- ‘(malicious) injury’, pIE *dhrougho-, cf. NGm. Trug ‘deceit’, and OP duruj-, draujana-, draujiya- (870, 576.11, $101, $108.IV, $106, $122, $128, 5132.2, 3, $143.I, V). drauga nsm. DB 1.34, 434; DPd 20. draugà absm. DB 437; DPd 17f.
draujana- adj. ‘deceitful’, i.e. ‘adherent of the Lie’: deriv. of drauga- (§101, 5132.2, 5147.1), cf. GAv. drogvant- ‘adherent of the Dru? (Hz. Apl 140-1). draujana nsm. DB 4.38, 63, 68. drauja- nam asm. DNb 12.
draujiya- vb. ‘regard as a lie’, denom. to drauga- (S217). [Отау уау 2d sg. subj. (§222.11, §227.1) DB 4.43.
drayah- sb. ‘sea’: Av. zrayah-, NPers. dáryà, ·
Skt. jrdyas- ‘expanse’, pIE *órejos- (§88, $113, $128, $156.II). Decl, §185.1. See also para- draya. draya asn. DB 5.23; DP
=== KNT grep maOista/mathista ===
```


### [2026-09-07T15:50:29.830Z] TOOL RESULT

```
=== SYN leaf 904 (p.880) ===
E *fei-. Walde-P. 1.358 ff. Grk. keluat, 38g. xetrac = Skt. cele, Av. saéte. Byz., NG xetrouat (so, not xolrouac as if fr. sb. orn) with shift to thematic type and xer- fr. old 3sg. xetrax (?). Hatzidakis, Mec. 1.316 f.
3. Lat. tacére (> It. giacere, Fr. gésir, Sp. yacer, Rum. zace), orig. ‘throw one- self, be thrown down’ : iacere ‘throw’, Grk. tue ‘throw’. Cf. Sp. echarse ‘throw oneself down, lie down’. Walde-
P. 1.199. Ernout-M. 466. Walde-H., 1.666 f. REW 4562.
Of the Romance derivs. of iacére, Fr. gésir is obs. except in certain forms, Rum. zace is now in restricted use (esp. ‘lie dead, lie ill’ etc.), and in general ‘lie’ de- noting the situation ‘be lying’ (in bed) is often expressed by phrases. Fr. éire couché : coucher ‘put to bed’, se coucher ‘lie down’, fr. Lat. collocare ‘put, place’ (12.12). Similarly Rum. fi (or sta) culcat : culca of same origin. Sp. estar acostado : acostar ‘put to bed, lie down’, deriv. of Lat. costa ‘side, rib’.
Lat. cubare : Goth. hups, OE hype ‘hip’ and with different root extensions Grk. xir7w ‘bend forward, stoop’ and many other words denoting a bent pos! tion. Walde-P. 1.370 ff. Ernout-M. 287. Walde-H. 1.298.
4, Ir. laigim, NIr. luighim, above, 1.
W. gorwedd, Corn. gorwedha, Br. gourveza, prob. epd. of W. gor, Br. ae ‘over’ (*upor, Pedersen 1.246), but root
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
—_— eae o>
pest ed eee 4a ee
Digitized by Arya Samaj
5, Goth.
1. . let : Lith. guo- 10, ett. gu ee pith. aa se , Lett. guola ‘nest’,
rest P i ; prood’, perh. Grk.
Goth. standan
Foundation Chennai and eGangotri
. PLACE, FORM, SIZE 835
ywreds ‘hole’. Walde-P. 1.639. Miuhl.- Endz. 1.679.
7. ChSl. lezati, ete., above, 1. 8. Skt. ci-, 3sg. gete, Av. 3sg. sade,
above, 2.
12.15 STAND (vb. intr.)
Lith.  stovelz Lett.  stavet
ropat ON standa as Dan.  staa Chsl. stojalt (ar ¢) in piedi Sw. std SCr. —stojati stare (essen OE standan, stondan Boh. _ stati aire debout ME ___ stande, stonde Pol. _staé eslar de pre a NE stand Russ.  stojat’ , slain BeGoe Du. staan Skt.  stha- duairsiur OHG _ stantan, stan Avy. sta- seosuighi MHG stan
Ul som) enn he zao NHG _ stehen
1, IB *sta+ in different formations variously distributed as regards usage be- ineen 1) ‘stand’ = “be standing’, 2) ‘take astand, stand up’, and 3) ‘cause to stand, set up’. Walde-P. 2.603 ff. Ernout-M. 979 ff. Grk. torapat, beside trans. torn; new pres., formed to perf. éornxa in orka (NT), NG oréxw (Hatzidakis Mec. 1279); Lat. stare (> It. stare, OFr. eter, Sp, estar, Rum. sta, mostly in sec- ondary sense ‘be’, etc.; for ‘stand’ in phrases); Ir. duairsiur fr. cpd. of re- ee form (Pedersen 2.628 ff.), fate hy ae Miz. sessam (Pedersen 1,¢,): h ae uplicated form (Walde-p ae ere also with m- suffix -4.006. Pedersen 1.79) W. saf
"The Toot is pj : a ina Biber Biven in this form *std-, here
to fvoi : "AG. Burt avoid repeating the clums Special eg ae the Skt. th is due to mee former Presence ording to current theory, the
of i larly 997 By oo laryngeal. Simi-
‘stamina�
```


## [2026-09-07T15:50:39.482Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT leaf 225 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==225' KNT.txt | grep -o -i \"ma[θΘ0Oθ]i[sš]ta[^.]\\{0,200\\}\" | head; echo \"---full---\"; awk 'BEGIN{RS=\"\\f\"} NR==225' KNT.txt | head -40",
 "description": "Kent p.201"
}
```


### [2026-09-07T15:50:41.015Z] TOOL RESULT

```
=== KNT leaf 225 ===
---full---
2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54, 60, 68, 86, 97^; 3.6, 17, 37, 45, 62, 67 (written ar?r^, 854.11), 87; 4.61, 62; DNa 50f; DSf 19°, 32; XPh 33, 45. abara” 3d pl. imf. ($10, $40, $84, $106, 8232.1) DPe 10; DSe 18°; DSf 34. aba- raha” 3d pl. imf. ($10, $218, $282.11) DNa 19f; XPh 17 (written орт, §54.1). abara"tà 3d pl. imf. mid. ($10, $236.II) DB 1.19. abariya imf. pass. (535.1, $220, $228.IT) DSf 23°, 31f, 35, 36, 38f, 40, 48, 45. abariya" 3d pl. imf. pass. ($220, 8232.11) DSf 41, 47.  baratuv imv. (5237.П) AmH 11^; DPd 14; DSk 5. аталаш inf. ($238) DNb 41.
à + bar- ‘perform’: dbaratiy ($218, $228.1) DNb 25. Cf. also Hz. Ар] 110-1, who refers to à-bar- certain other forms listed above as augmented forms of uncompounded bar-.
pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
pari- + bar- ‘protect, preserve’ (cf. Hz. Ар 112-3): paribarümiy Ist sg. (8226.]) DNb 17. paribarühy 2d sg. subj. ($27, $136, §222.IT, 4227.1) DB 4.78; paribaráh*-di$ (827, etc.) DB 4.74. pari- barā 2d sg. imv. (5237.1) DB 4.72, 88.
fra- + bar- ‘proffer, grant’: frábara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DPh 8; DNa 33; DSf 11; DSm 3°; DSp 2°; D8s 6; DZc 4; DH 7; A’He 18f, 20.
bara- sb. ‘bearmg, bearer’: Av. -bara-, Skt. -bhara-, Gk. -фороѕ, pIE "bhoros ($32, $122, $1431, ҮТ), to root bar- ‘bear’, in aritibara-, takabara-, vacabara-; also bāra- ‘borne by, rider of’, with vriddhi (8122, $126, 5148.1), in asabdra-, ef, usabüri-. See Hz. Ар] 95.
bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
Bardiya- sb. Smerdis’, brother of Cambyses ($16411): Elam. bir-h-ia, АКК. bar-zi-ia, Gk. Урёрӧ ($29.02, $30). Репу. (§144.1V) of OP bard- ‘be high’ (575.11): ‘The Exalted’. Bardiya пет. DB 1.30, 32, 39, 52f; 3.25, 35, 54; 4.9, 27, 82; DBb 4f; DBh 5. Bardiyam asm. DB 1.31 bis, 51.
barSan- sb. ‘height, depth’ (S81): Av. barazan- .
(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
bav- vb. ‘become, be’: present stem bava- (8213), Av. bavatti, Skt. bhdvati, Gk. ote ‘grows’, Lt. fut ‘I was’, Lith. butt ‘to be’, NEng. be, pIE *bheu-. See also büm:-. bavatiy (§122, §228.1) XPh 55, 56. bæa"ty 3d pl. ($232.1) DNb 14 (башайу in 2d copy, Hz. ApI 115; ef. $48). abavam Ist sg. imf. DB 1.28, 60, 72; 4.5; 5.4^; DSm 6°; XPf 35, 36f; XPh 30; XSe 4°. abava imf. ($228.IT) DB 1.32, 38, 34, 40, 48, 77, 80; 2.16f, 17, 80, 94; 3.10, 11, 20, 27, 28, 76, 82, 83; 5.5, M^, 30; DSf 25; XPf 26.  abava^ 3d pl. imf. ($112, $232.IT) DB 1.76; 2.7, 93; 3.78; 4.34. bavātiy sub). ($222.11, §228.1) DNa 43, 45f; DNb 59 (Lg. 15.74; confirmed by photograph, JNES 444). [biyjä 2d sg. opt. ($114, $218.11, $223.I, $227.11) DB 4.69. буй opt. Cbhy-net, Bv. Gr. $232, comparing Av. buyd{ from *bhu-iët; but ВЫ. Gdr. IP 1. $143 takes as *bhy-i48t, = Lt. fiet, which may be either non-thematie opt. or thematic subj.; $114, $122, 5208, $218.II, §223.1, $228. ID) DB 4.56 bis, 58, 59, 741, 75, 78f, 79°.
bigna-, in d-bigna-, see Bagabigna-.
biimi- sb. ‘earth (= world or ground)’: Av. bümi-, NPers. büm, Skt. (RV) nom. bháümi bhümis; deriv. of root bhav- (see bav-) in grade bhi-, cf. Skt. aor. ábhüt, Gk. ёфо ($11, $65, §152.1V, §179.- IIT).
LEXICON
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28.
```


## [2026-09-07T15:50:47.669Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ma[0OθΘ6]i[sš$]ta\\|mathista\\|maO-i\\|greatest\" KNT.txt | head -20; echo \"---\"; for n in 227 228 229 230 231; do echo \"== leaf $n ==\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KNT.txt | head -3; done",
 "description": "Find maθišta in Kent"
}
```


### [2026-09-07T15:50:49.012Z] TOOL RESULT

```
345:88. New Iranian includes the Iranian lan- guages from about 900 лр. onward; its greatest monument is the national epic of Persia, the Shih Namah or Book of Kings, composed by Firdausi about the year 1000. The languages of this period are the following:
1150:injures’, Lt. nocet, Skt. ndsdyalt. pIE *mak- in OP тойа ‘greatest’, Av. masista-
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
1907:1 The greatest part of this class consists of those whose first part is an inseparable adverb-or a prepositional pre- fix; under our plan these are not here considered ($159).
2248:Superl. nsm. ma£isla ‘greatest’, asm. тай ат, with -isto-; cf. Av. masista-, Gk. Dor. дйкитто to px pos.
2693:үшалпаһуа máhya XIV raucabiš бакаіа üha 44 days of the month Viyakhna were past’; DB 1.49 ngiy amazam taumayà Каёсту ‘not anyone of our family’, cf. amáxam taumäyä DB 1.28f depending directly on Kabügiyà; Ра 1f hya mah Ча bagünam the greatest of the gods’.
3049:Other exceptions belong exclusively to govern- mental and religious formulas: xsdyahiya zSayatt- убпат ‘kings of kings’, zSaya&rya dahyandm ‘king of countries’, hya тайа bagünàm ‘the greatest of gods’, vašnā Auramazdahe ‘by the will of Ahura- mazda’. It is possible that the postposition of the genitive in these phrases is a Median usage.
3449:$2. 5-14. Saith Arsames the King: Ahuramazda, great god, the greatest of gods, made me king. He bestowed on me the land Persia, with good people, : with good horses. By the favor of Ahuramazda I 1 hold this land. Me may Ahuramazda protect, and my royal house, and this land which I hold, may he protect.
3626:83 Sim : ma6istam : akunavam : avatàSàm : a&aham : paraità : К
4061:$1. 1-5. Great Ahuramazda, the greatest of gods—he created Darius the King, he bestowed
4101:$2. 3-10. Saith Darius the King: This is the kingdom which 1 hold, from the Scythians who are beyond Sogdiana, thence unto Ethiopia; from Sind, thence unto Sardis—which Ahuramazda the greatest of the gods bestowed upon me. Me may Ahuramazda protect, and my royal house.
4286:$8а. 8-12. Saith Darius the King: Ahuramazda, the greatest of the gods—he created me; he made me king; he bestowed upon me this kingdom,
4355:greatest of the gods—he created Darius the King,
4530:$4. 27-43. Saith Xerxes the King: Other song — of Darius there were, (but)—thus unto Ahura- mazda was the desire—Darius my father made me _ the greatest after himself. When my father Darius went away from the throne, by the will of Ahura. mazda I became king on my father’s throne. When I became king, I built much excellent (construc- tion). What had been built by my father, that I protected, and other building f added. What more- over I built, and what my father built, all that by the favor of Ahuramazda we built.
4903:In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius had a number of sons, but—-as was Ahuramazda’s desire—he made Xerxes (presumably not his eldest son, though this is not stated in the inscription) the ‘greatest after himself; and when Darius ‘went from the throne,’ Xerxes—as was Ahuramazda's desire—became king on the throne of his father.
5761:mabista- adj. ‘greatest’, equal to ‘crown prince’ in XPf (Speiser ap. Kent, Lg. 9.40-1; Hz. Apl 254-8): Av. masista-, NPers. mähist, Gk. ppxio ros ‘longest’ (radical vowel after that in anxos Jength"); superl. to pIE *mak-ros, Gk. накр, Lt. macer ‘thin’, pLE root *mak- (887) ‘be long and slender’ + superl.,suffix.<ste-) (S117, $156.11,
---
== leaf 227 ==
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32.
Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado.
(1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm. DSf 50, 54. Майа] ipm. DB 2.23. MddatSuva lpm. DB 2.23.
== leaf 228 ==
ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36.
EU: ET TORR ON |
INS SEE cals la pen X AN, ae ete. ЫЗ, Ses f. Av m ee Sm SN Ie e mne -
== leaf 229 ==
so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a province: Elam. mu-is-sa-ri-ia, АКК. mi-sir (S6, §76.V).
(1) ‘Egyptian’: Mudrdya nsm. А?Р 19. Mudráyà npm. DSf 50f, 52, 55.
(2) ‘Egyptians’, as province: Mudräyā npm. DPe 11f.
== leaf 230 ==
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39.
lwadé- conj. ‘where’: GAv yada, Skt. yada; probably rel. nt. pAr. #00 + postpos. 4. уайд- tya XPh 35f ($133, $296; cf. yaa tya ХР 29); yadàyà XPh 39 (perhaps error in writing, §55.1; but ef. Hz. AMI 8.66, ApI 358, Nyberg Rel. 477-8).
*Yadd- sb. ‘Yada’, probably ‘Anshan’ (as shown by the Elam. translation 3.3 an-za-an.mar, read by Cameron; cf. §166.n2): not an abstract yadà- ‘loyalty’ to root yad- (q.v.), as commonly taken (wrongly also Foy; KZ 35.43; Hüsing, ОГЛ
== leaf 231 ==
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $192.
```


## [2026-09-07T15:51:03.750Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 948 949 950; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' SYN.txt | head -50; done",
 "description": "Buck around p.880"
}
```


### [2026-09-07T15:51:05.013Z] TOOL RESULT

```
=== leaf 948 ===
. Meil- let, Etudes 221. Miklosich 273.
SCr. oblik, lik: ChSl. lice ‘face, cheek’, etc. (4.204). Berneker 719 f.
Boh. tvar : ChSl. tvort ‘condition, ap- pearance’, tvoriti ‘make’, etc. (9.11). Miklosich 366.
Boh. podoba : Slov. podoba ‘picture, appearance’, Pol. podoba ‘similarity’, ChSl. po-doba jesti, po-dobajett ‘it is fitting’, etc. Berneker 203 f.
Pol. ksztatt, fr. NHG gestalt (above). Briickner 278.
Pol. postaé : staé ‘stand’. Brickner 432.
Russ. vid, see above, 5.
7. Skt. rupa- : varpas- ‘image, form’? Uhlenbeck 252, 275. Walde-P. 1.276 (without ripa-).
Skt. akara-, akrti- fr. kr- ‘do, make’.
Av. vaesi- : vid- ‘recognize, know’, Grk. dos ‘form’, etc. (above, 1). Barth. 1321.
Av. kahrp-, also esp. ‘body (of men and gods)’ : Skt. krp- ‘form, appearance, beauty’ (only inst. sg. krpa), Lat. corpus ‘body’, etc. Walde-P. 1.486. Barth. 467 ff.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
876 SELECTED INDO-EUROPEAN SYNONYMS 12.52 SIZE
I kyo Goth. mikilei Lith. didumas, did bé ees ON | storleikr Toke, Uelume Lat. magnitidd Dan. _ sigrrelse ChSI.  veliéije, veltétsturje It. grandezza Sw. storlek SCr. _ velitina Fr. grandeur OE micelness Boh.  velikost’ Sp. tamaiio ME mikelnes, syse Pol. wielkogé Rum. médrime NE size Russ. _velitina Ir. méeit Du. grootte Skt. mdna-, mahas- Nir. méid OHG = mihheli, grizi Av. mazah-, masah- W. maint MHG graze, michel Br. ment NHG grésse
Most of the words for ‘size’ are ob- vious derivs. of the adjectives for ‘large, big’ (12.55), that is, ‘bigness’ is used for ‘the degree of bigness’, as Grk. péyeOos : peyas, Lat. magnitudd : magnus, Goth. mikilei : mikils, etc.—all the words list- ed, with the following exceptions:
1. Sp. tamajio, sb. of adj. tamazio ‘so large’ (Lat. tam magnus ‘so large’). REW 8552.
2. Ir. méit, NIr. méid, W. maint, Br. ment, perh. *manti, old abstract forma- tion fr. root in Ir. mar ‘large’ (12.55). Pedersen 1.242 f., 2.48. Walde-P. 2.238.
3. ME syse, NE size, fr. OFr. sise, cise for assise lit. ‘act of settling or fixing something’ (esp. assessments, levies, etc.), pple. of OFr. asseir ‘sit at, set down, settle’ (Lat. adsidére). The mod- ern sense is late in ME, earlier ‘assize’ then esp. ‘regulation of amount, quan- tity (of a tax, etc.)’ and ‘fixed quantity or size’. NED s.yv. size, sb.!.
4. Skt. mana-, esp. cpds. parimana-, pramdana-, lit. ‘measure’ : md- ‘measure’ (12.54).
12.53 GROW
(= Increase in Size) Grk.  abkdvopat Goth. wahsjan Lith.  augti NG Heyaddvw, attavw ON vaza Lett.  augt Lat. _créscere, augéscere Dan.  vokse ChSl.  rasti It. crescere Sw. vdxa SCr. —_rasti Fr. crottre OE weazan Boh. riisti Sp. crecer ME _waze, growe Pol. rosnqé Rum. cresle NE grow Russ. rasti Ir. Gsaim, forbiur Du. —_groeien, wassen Skt.  urdh-, rudh-, uks- Nir. fasaim OHG wahsan Ay. varad-, rud-, uxs- W. tyfu MHG wahsen Br. kreski NHG  wachsen
Most of the words for ‘grow’ were probably used primarily with reference to plant life, as is demonstrably the 
=== leaf 949 ===
case for NE grow.
1. IE *aweg- (*aug-, *ug-, and with ~s- extension *aweks-, etc., orig. desid. formation). Walde-P. 1.22f. Ernout- M. 88 ff. Walde-H, 1.82 f., 850. Falk- Torp 1390. Feist 67, 541.
Grk. avéavw, also attw, aéfw (*aétw) ‘increase’ (trans.) with mid. avtdvopat etc. ‘grow’ (intr., but NG attavw trans. and intr.); Lat. augére ‘increase’ trans., rarely also intr. ‘grow’, inchoat. augescere intr.; Goth. wahsjan, OE weazan etc. general Gme. (NE waz of the moon, but mostly arch.); Lith. augli, Lett. augt; Skt. uks-, Av. uxs- (88g. pres. uasyeili);
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
gpATIAL RELATIONS:
A oks- tgrow’ OSM B aulsu ‘old’ , s re yeyard¥@ fr. peyados ‘large 9, NGr.
(284) rascere (> It. crescere, Fr. : cer, Rum. creste) : creare BP a Arm. sernem ‘beget’, i feed’, Grk. Kopéokw, atiate’. Walde-P. 1.408. 39, Walde-H. 1.288. : Lie asaim, Ir. fasaim, ef. Ir. as canth’, perb- (with loss of init. w in cue - Goth. wahsjan, ete.
© api) fr. *woks- a hi G.S. Lane, Language 13.21. ?
otherwise Strachan, IF 2.370.
Ir forbiur, cpd. of birw ‘carry’ and for ft, hence lit. ‘carry on’. Pedersen 9407 f.
V. fu : Lat. tumere ‘swell, be swoll- a, fr, an extension of the root *éu- in Sut, fduli ‘is strong’, ChSl. tyéz “become fat’, etc, Walde-P. 1.708. Ernout-M. 1064.
Br. kreski, prob. fr. Lat. créscere. Henry 81. Loth, Mots lat. 154 (with sme question on account of the short vorel),
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 877 5. ME growe, NE grow, Du. groeien, but OE gréwan, ON gréa, OHG gruoan only ‘grow’ (of plants), ‘spring up, be- come green, etc.’ : MHG gruose ‘shoot of a plant, sap’, Goth., ON, OHG gras OE graes ‘grass’, ON grenn, OE gréne, OHG gruoni ‘green’, Lat. gramen ‘grass’. Walde-P. 1.645f. NED s.v. grow, vb. 6. ChSl. rasti, etc., general Slavic (Pol. r6sé replaced in present by rosnqé), fr. *ord(h)-t-, prob. : Lat. arduus ‘steep, high’, Ir. ard, Av. aradwa- ‘high’. Walde-P. 1.149. Briickner 463.
7. Skt. vrdh- act. and caus. ‘make grow or thrive, elevate’, mid. ‘grow, thrive’, Av. varad- act. (and mid.) ‘make grow or thrive, increase’, mid. and pass. ‘grow, thrive’ : ardhva- ‘up- ward, upright, raised, elevated’, Grk. dps ‘upright, straight’, Slavic roditi ‘bear’. Walde-P. 1.289.
Skt. rudh-, ruh-, Av. rud- (pres. 3pl. Skt. rodhanti, Av. raodanti) : Goth. liu- dan ‘grow up’ (of seed, Mk. 4.27), OK léodan, OHG ar-liotan ‘spring, grow’ (of plants), ON lodinn ‘grown over, hairy’. Walde-P. 2.416.
12.54 MEASURE (vb.) hope Goth. mitan Lith. matuoli, mieruott pees ON mela Lett. merit métiré Dan. maale ChSl.  mériti pzere Sw. miata SCr.  mjeriti i OE metan Boh. méritt ; file ME mete, mesure Pol. —-mierzyé oma NE measure Russ. merit’ Neate, Du. —_meten Skt.  md- mesur(o) OHG mezzan Av.  ma- muzula MHG mezzen All th NHG ~ messen he of a for ‘measure’ are fro
=== leaf 950 ===
m Skt., Av. md-; Grk. sb. pérpov (: Skt. aby relate d E roots, themselves prob- | ma-tra-~m as Skt. da-ira-m : Av. dda-6ra- LT oy timately . m) whence vb. perpéew; Lat. mélirt liter mostly the nouns and verbs, the | through a sb. *méti- (cf. OE med ‘meas- n Indo. Tani Tough the nouns, except | ure’, Grk. paris ‘plan, wisdom’), VLat. OUt-M, e Walde-P. 2.237. Er- | *matire (>Sp., Port. medir), pple. Ton 6g Be REW 5508, 5552. Falk- | ménsus (hence ménsura sb. and late de-
e —-— = . teker 2.50, nom. ménsirare >It. misurare, Fr.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
878
mesurer, Rum. mdsura); ON mela, Dan. maale (ON mal, Dan. maal, Sw. mdl ‘measure, point of time, meal, etc.’); Lith. matuoti; ChSI. sb. méra, whence vb. mériti, etc., general Slavic (hence Lith. mieruolt, Lett. mérit); here (?) Toch. A me- (SSS 456, but B form lacking).
W. mesur, mesuro, Br. muzula, fr. sbs. W. mesur, Br. muzul, MBr. mesur, fr. Lat. ménsura. Loth, Mots lat. 187.
ME mesure, NE measure fr. Fr. me- surer.
SELECTED INDO-EUROPEAN SYNONYMS
2. IE *med- in words for ‘measure’ and esp. ‘measure, estimate with the mind, reflect.’ Walde-P. 2.259. Bp. nout-M. 599. Walde-H. 2.55 f. Feist 363.
Tr. domidiur (vbl. noun tomus, Ny. tomhas, hence témhaisim), epd. of midiur ‘judge’; Goth. mitan, OB metan, OHG mezzan, etc., general Gmc. (but ON meta ‘value, estimate’) : Grk. Hédouat ‘be mindful of’, Lat. medérz ‘care for’, esp. ‘heal’, meditarz ‘reflect upon’.
12.55 LARGE, BIG (GREAT)
Grk, péyas Goth. mikils Lith. didis, didelis NG peyddos ON storr, mikill Lett. Liels
Lat. magnus, grandis Dan. stor ChSl.  velijt, velikit It. grande, grosso Sw. slor SCr. _velik
Fr. grand, gros OE micel Boh.  vel(i)ky
Sp. grande ME mikel, grete (bigg) Pol. wielki
Rum. mare NE large, big (great) Russ.  bol’§oj (velikij) Ir. mar, bras(s), oll Du. groot Skt. mahant-, mah- NIr. mar OHG = mihhil, groz Av. mazant-, maz-, W. mawr MHG gréz, michel masan-; OPers. Br. bras NHG gross vazarka-
Many of the words for ‘large, big’ be- long to inherited groups, one of them so widespread as to leave no doubt that it reflects the chief IE expression for ‘great, large’ with the familiar extensions be- yond the notion of size.
Yet this group is represented in the present European languages only by NG Heyahos or by dialect forms like NE mickle and muckle (also NE much but no longer used of size). As Lat. magnus was replaced by grandis, so Goth. mikils, OE micel, etc., were replaced in Scan- dinavian by ON storr, Dan., Sw. stor, in West Gme. by the group represented by NE great, which in turn is now used mostly in secondary senses or with emotional value, and with re
```


## [2026-09-07T15:51:09.963Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 952 953; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' SYN.txt; done 2>/dev/null | head -80",
 "description": "Buck p.880 'long'"
}
```


### [2026-09-07T15:51:11.521Z] TOOL RESULT

```
=== leaf 952 ===
ar- gus ‘abundant, copious’, etym.? Er- nout-M. 524. Walde-H. 1.764. REW 4912. NED s.v.
6. Lith. didis, didelis, etym. dub.; pos- sibly through ‘conspicuous’ : Skt. didi- ‘shining’, di- ‘shine’, etc. Walde-P. 1.772.
Lett. liels (Lith. lielas obs., not in NSB), prob. through ‘tall’ fr. ‘slender’ : Lith. leilas ‘slender, thin’, leinas ‘thin, flexible’, ete. Walde-P. 2.388. Mihl.- Endz. 2.501 f.
7. ChSl. velijt, velikti, SCr. velik, Boh. vel(i)ky, Pol. wielki (but Russ. velikij now used like NE great and replaced by bol'soj with reference to size) beside *yeli- in ChSl. velimi ‘very’, velt-lépit ‘ueyadorperns’, and *valii-, Russ. valom ‘in abundance’, valovoj ‘wholesale’, prob. - Grk. és ‘in crowds, sufficiently’, ctdw, Att. etd ‘pack close’, etc. Walde- P. 1.296. Otherwise Brickner 616 f.( : ChS]. veléi ‘order’, Lat. velle ‘wish’, etc.).
Russ. bol’soj, new positive to old comp. bol’$ij, ChSl. bolijt, fem. bolisi ‘greater’ (positive velijt, velikt, above) : Skt. baliyas- ‘stronger’, bala- ‘strength’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
880
Grk. BeAriwy, Bédrepos ‘better’, Lat. deé- bilis ‘weak’. Walde-P. 2.110. Walde- H. 1.327. Berneker 72.
8. Skt. mahani-, mah-, Av. mazant-, maz-, above, 1.
Ay. masan- ‘great, significant’, masit-, masita- ‘great, large’, masyah- ‘greater’,
SELECTED INDO-EUROPEAN SYNONYMS
masah- ‘length, size’, and mas- ong’ . Grk. paxpés ‘long’ (12.57). Walde-p. 2.223. Barth. 1154 ff.
OPers. vazarka- (‘great’ king and ‘great’ = ‘large’ earth) : Skt, vaja- ‘speed, vigor, contest’, vajra- ‘thunder- bolt’, Av. vazra- ‘club’, Lat. vegére ‘set in
masista-, OPers. maéista- ‘greatest’, be- | motion, excite’. Walde-P. 1.246 f, side masan- ‘greatness, importance’, | Barth. 1390.
12.56 SMALL, LITTLE Grk. —_pixpés Goth. leztils (smals) Lith.  maizas NG mtxpds ON litill, smar (smalr) Lett. mazs Lat. parvus Dan. lille, pl. smaa ChSl.  malit (chudit) It. piccolo Sw. liten, pl. smd SCr. mali, malen Fr. pelit OE ljtel, smal Boh. maly Sp. pequefio, chico ME litel, smal Pol. = maly Rum. mic NE small, little Russ. malyj Ir. becc Du. klein Skt. alpa-, kgudra- Nir. _ beag OHG _ luzzil, smah(i), smal Av. kasu- W. bach, bychan MHG litzel, smal, smehe, Br. bihan klein
NHG Klein
There is no widespread inherited group for ‘small’ parallel to that for ‘large’, and the majority of the words are of uncertain origin. Several seem to be based upon expressive (symbolic) sylla- bles. ‘Crushed, ground (fine)’ is the cer- tain source for one word and a possible one forsome others. A peculiar develop- ment from ‘bright, shining’ through ‘clean, delicate, fine, thin’, etc., is seen in NHG klein vs. NE clean.
Words for ‘small’ naturally develop Secondary opprobrious senses
=== leaf 953 ===
, ‘petty, trivial, mean’, etc. Conversely, for cer- tain groups (Goth. leitils, etc., and OE lytel, etc.) in which the majority of the cognates have the notion of ‘deceit, abuse’ or the like, one must reckon with the possibility that this is the more origi- nal and ‘small’ in the literal sense sec- ondary (cf. the history of ‘tight’ and ‘left’, 12.41, 12.42),
1. Grk. pixpés, Ion., early Att. opt- kpés, also hypocoristic puxxds (attested
as Dor., Boeot. and prob. widespread pop. form, as in proper names Mixkos etc.) : Lat. mica ‘crumb, little bit’, ON smar ‘little’, OHG smahi ‘little, insignifi- cant’, perh. fr. an extension of a root *smé-, *sméi- in words for ‘smear, rub’. Walde-P. 2.685 f. Boisacq 885. Falk- Torp 1075.
2. Lat. parvus (also ‘little’ in quan- tity) : Grk. radpos ‘little’, pl. ‘few’, Lat. pauct, Goth. fawai, etc. ‘few’ (13.17). Walde-P. 2.75. Ernout-M. 737, 742.
Replaced in pop. Lat. and the Ro- mance languages as ‘small’ by a variety of obscure forms apparently based on expressive syllables like *pikk, *pitl, *pits, etc. REW 6494, 6544, 6550. Goldberger, Glotta 18.52.
Late Lat. pisinnus (first in Att. Labeo for ‘child’, in Peregrinatio a pisinno = e puero; ecclesia pisinna ‘small church’, also in Marc. Emp., Isid., etc., cf. App: Prob. pusillus non pisinnus), pitinnus
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
spATIAL RELATIONS:
* ulus (Anton. Itin.). ; matio 197.
6 i ; sastedt ee ocino, ef. Rum. pic
Ih a uittle child’, Calabr. pikka (op Pr” ntity)’, ete
ey, Cat.) petit, cf. Rum. : self small, hide’, It. dial. 4» ‘little’ (in amount),
fi0, Port. pequeno. (beside other Romance ob. fr. an expressive ¢ikk, pikk, etc. REW 2451b, (p. 806). Or fr. Lat. ciccum in its
Densusianu 1.201. Puscariu 1067. REW 5559. 3. Ir. bece, bec, NIr. beag, W. bach, bychan, Br. bihan, etym. dub. Walde-P. 1160, Pedersen 1.3885. Stokes 166. 4, Goth. leitils, ON litill, Dan. lille (for liden, older lidel), Sw. liten, ef. ON i adv. ‘little, badly’, prob. : Goth. lita retey' OHG liz ‘pretext’, lizzon, tain simulate’, MHG liz, litze ‘humor’, St connections dub., perh. Grk. \or- vis ‘abuse, revile’. TE *leid- beside a i ‘eud- with similar semantic re- 1p. A the following. Walde-P. Saas 640f. Feist 328. i ce » ME litel, NE little, OHG luz- Goth, lin me biteel, liitze, prob. : OF Iop heaped liutat ‘conjur- mes on Fark: ON gta ‘dishonor, : 1 CHS. Dua er Russ. ludit’ ‘de- ief also Te an SCr. lud ‘foolish’, T. lita ‘little finger’. Walde- Goth a orp 641. lite gny mals ( i oN §malr ae ly Super. smalisia), “ONE onal, Ou
```


## [2026-09-07T15:51:18.173Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 264 265 266; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' SYN.txt; done 2>/dev/null | head -90",
 "description": "Buck p.193 fly"
}
```


### [2026-09-07T15:51:19.552Z] TOOL RESULT

```
=== leaf 264 ===
tw
Digitized by Arya Samaj Foundation Chennai and eGangotri_ .
ternal ear), deriv. of ofr ‘hear’, fr. Lat. audire ‘hear’.
3. Ir. cliias, NIv. cluas, W. clust : ON hlust ‘ear’ (beside eyra, cf. Vigfusson s.v.), OE hlyst ‘hearing’, hlystan ‘hear, listen’ (NE listen), etc. fr. IE *fKleu-s-, beside *kleu- in Skt. gru-, Grk. kdb ‘hear’, etc., from which root also Skt, grotra- ‘hearing, ear’, Toch. A klots, B klautso ‘ear’ (SSS, 128, 129). Walde- P. 1.494 f. Pedersen 1.80,
Br. skouarn, Corn. scovarn, W. ysgy- farn (obs.), etym. dub., but perh., fr. a *skeu- beside IE *keu- in Grk. xotw ‘per- ceive, hear’, Lat. cavére ‘beware’, Goth. hausjan ‘hear’, OF scéawian ‘look at’, etc. (15.41, 15.52). Henry 243. Win- disch ap. Ernault, Dict. étym. 377. Less probably Pedersen 2.53.
4, Skt. karna-, Av. karana- (of evil beings), etym.? Walde-P, 1.412, 495.
Av. gaosa-, OPers. gauga- (NPers. gos ‘ear’) : Av. gus ‘hear’, Skt. ghosa- ‘noise’, ghosati ‘sounds, calls’. Walde-P. 1.569.
Ay. us (dual), above, 1.
an inherited group. The others are scure origin.
ae Dies nas-. Walde-P. 2.318. Emout-M. 653, 659. Falk-Torp 779 f. Lat. nasus (> It. naso, Fr. nez, Rum. nas), also pl. narés ‘nostrils, nose’, late sg, naris (>Sp. nariz); ON sg. ngs nostril’, pl. nasar ‘nostrils, nose’, OE nosu, nasu, OHG nasa, etc., general Gme.; Lith. nosis, OPruss. nozy; ChSl. nosit, etc., general Slavic; Skt. nas-,; nas- (in RV only dual, nom. nasd, gen. nasos), Ay., OPers, nah- (sg. and dual in Av., sg. in OPers.). The meaning ‘nostril’ is implied by the early use of dual or pl. forms, but is not necessarily older than ‘nose’, For it may be abstracted from the latter, and the dual was favored by i ae in the case of ‘eyes’, ‘ears’, 2. Grk. pts, gen. pivds, also pl. pives ostrils, nose’ (like Lat. narés), etym.? . Seng ane either : Pr TAG ES i c, (Boisacq 842) or : with query) i ete. (Walde-P. 1.140
Possible, the word being
n
Digitized by Arya Samaj Foundation Chennai and eGangotri
am BODY; BODILY FUNCTIONS AND CONDITIONS 227
gprs OF T 4.23 NOSE Lith. nosis Goth. .--- pis ON nasar Lett. deguns Gre im Dan. nase Chsl. nosit nasus Sw. nisa SCr. nos naso OE nosu Boh. nos nez ME _~ nose Pol. nos nariz NE nose Russ. os Rum. nas Du. neus Skt. nas-, ghrana- sron OHG nasa Av. nah- sron MHG nase i NHG nase Tl Most of the words for ‘nose’ belong to | then orig. a vulgar epithet, displacing Mo:
the IE word, like the following which displaced it in turn.
NG porn, fr. Grk. pizis used by Aris- tot. (HA 52415 ff.) for an organ of the cuttlefish connected with the ink sac, and attested as a vulgar term for ‘snout, n
=== leaf 265 ===
ose’ by Eust., Comm. 950 (oi ri piva pirw xadécavres), prob. : Lith. mute, Skt. mukha- ‘mouth,’ etc. (4.24). Walde-P. 2.310.
3. Ir. srén = W. ffroen, Br. fron ‘nos- tril’ (here in some way Br. fri ‘nose’, MBr. fry), fr. *skrok-na-, prob. : Skt. srakva- ‘corner of the mouth’, and fr. the root in Ir. srennim, Grk. peyxo, péyxw ‘snore, snort’, of imitative origin. Walde-P. 2.705. Pedersen 1.82. Lewis- Pedersen 22.
W. trwyn, OCorn. trein, perh. fr. an imitative group parallel to the preceding (cf. Grk. sbyxos ‘pig’s snout’). Pedersen 1.82. Morris Jones 156.
4. Lett. deguns, etym.?
5. Skt. ghrdna- ‘smell’ and ‘nose’, fr. ghra-~ ‘smell’ (15.21).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
228 SELECTED INDO-EUROPEAN SYNONYMS
4.24 MOUTH Grk.  orépa Goth. munps Lith.  burna NG oroya ON munnr (midr) Lett. mute Lat. Gs Dan. mund ChSl. usta It. bocca Sw. mun SCr. usta Fr. bouche OE mip Boh. iista Sp. boca ME mouthe Pol. usta, geba Rum. gurd NE mouth Russ. rot Ir. gin, béoil Du. mond Skt. mukha-, Gs-, ete, NIr. _béal OHG mund Ay. Gh-, zafar- W. geneu MHG munt Br. genou NHG mund
The IE word for ‘mouth’ persisted in several languages in the literal sense, in some others in secondary uses, but was to a large extent replaced by other words. Most of these were originally ex- pressions applied to the mouth of ani- mals and vulgarly of persons, like Lat. rostrum, NHG maul, NE jaw, snout, mug, and many others (not included in the list, except where they have become standard words for ‘mouth’). There is frequent association between ‘mouth’ and ‘throat’, ‘jaw’, ‘check’, ‘chin’ or ‘lip’.
1. IE *0(u)s-, *aus-. Walde-P. 1.168. Ernout-M. 714 f.
Lat. ds (also dstiwm ‘door, entrance, river-mouth’, dra ‘edge, coast’); Ir. a (rare); OPruss. austo (Lith. uostas ‘river- mouth’); ChSl. usta, etc., general Slavic (but Russ. usta obs.); Skt. as-, dsan-, asya-, Av. ah- (also Skt. ostha-, Av. aosta- ‘lip’); cf. also ON ass ‘river- mouth’, OF Gr ‘beginning’, dra ‘edge, bank’, etc. But Hitt. ais, gen. issas ‘mouth (Sturtevant, Hitt. Gloss, with refs.) points to a parallel *ais-.
2. Grk. orbpa: Av. staman- ‘dog’s mouth’, W. safn ‘mouth, jaws’ (of ani- mals), MBr. staffn, Br. staon ‘palate’, root connection? Walde-P. 2.648. Ped- ersen 1.78.
3. It. bocca, Fr. bouche, Sp. boca, fr. Lat. bucca ‘puffed-out cheek’ (4.208) and also a pop. substitute for ds (cf. Thes.
s.v.). Ernout-M.110. Walde-H. 2.120, REW 1357.
Rum. gurd (so Alb. gojé ‘mouth’, Fr, gueule ‘mouth, jaws’ of animals, in some dial. common word for ‘mouth’), fr. Lat, gula ‘throat, gullet’ (4.29).
Lat. gurges ‘whirlpool’, late gurga, has through ‘throat’ (Fr. gorge) given dial, words for ‘mouth’; likewise Lat. rastrum ‘beak, snout, mouth’ (of animals, vul- garly of persons), as ORum. rost. REW 3921, 7386.
4. Ir. gin, W. geneu (beside gen ‘chin’), Br. genou : Lat. gena, Goth. kinn
=== leaf 266 ===
us ‘cheek’, etc. (4.207).
Ir. béoil, NIr. béal, see bel ‘lip’ (4.25).
5. Goth. munps, OE mip, OHG mund, ete., general Gmc., prob. : Lat. mentum ‘chin’, etc. (4.209), rather than : Lat. mandere ‘chew’, as preferred in Walde-P. 2.270, Falk-Torp 738. Feist 368. Ernout-M. 608.
6. Lith. burna: Bulg. biirna ‘lip’, Arm. beran ‘mouth’, Ir. bern ‘cleft, gap’, Grk. dapayt ‘cleft, ravine’, ¢dapvyt ‘throat’, etc. Walde-P. 2.159. Traut- mann 40.
Lett. mute: Skt. mukha- ‘mouth’, etc. (below, 8).
7. ChSl. usta, etc., above, 1.
Pol. geba : Boh. huba, SCr. gubica (both ‘mouth’ only in derogatory sense, ‘mug’), Russ. guba ‘lip’, ChSl. gaba ‘sponge’, Lith. gumbas ‘swelling, protu-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
——aaEEoEEeEEEeEeEeEeEeEOeGGeeeee ee
; Lett. gumba ‘{umor’, sa pera 568. Brickner 138 ff. (Ber- a ae akes two separate groups.) ,; Chsl. rit ‘peak’, SCr. rt a Boh. ret ‘Jip’, etc., these Lee oe. ‘projection’ (whence a th’ or ‘Lip’ through ‘snout’ of ‘ante ae Lat. ort? ‘rise’, Okt. T$va~- ‘thigh’, we S. Lane, AJPh. 54.64.
a git, (beside as-, etc., above, 1)
Digitized by Arya Samaj Foundation Chennai and eGangotri
DY; BODILY FUNCTIONS AND CONDITIONS 229
mukha- : Lett. mute ‘mouth’, OHG mi- la, NHG maul ‘mouth’ (of animals, vul- garly of persons), Lett. maut ‘roar’, etc., an imitative group based on an utterance like Grk. pb, Lat. mu. Walde-P. 2.309 ff.
Skt. vadana-, vaktra- ‘mouth’ as organ of speech, fr. vad-, vac- ‘speak’ (18.21).
Av. zafar- ‘mouth’ (of evil beings) : OE ceafl, NHG kiefer ‘jaw’. Walde-P. 1.570f. Barth. 1657.
4.25 LIP
Gr. xethos Goth. wairiloém (dat. pl.) ar lipa
ie ck ON vorr tt.  lipa ss ala Dan. abe ChSl. ustina - * Jabbro Sw. léppe SCr. usne fr eure OE weler, lippa Boh. vet (pysk) Sp.  labio ME — lippe Pol. warga Rum. buzd NE lp Russ. guba Ir. bal Du. lip Skt. ostha- Nir. _ béal, puisin OHG leffur, lefs Ay. aosta
W. — guefus (weft) MAG: ieee) Br.  gweuz, muzell NHG lppe
Some of the words for ‘lip’ are from the notion of ‘hanging down’ or ‘pro- jecting’. Several are connected with words for ‘mouth’, the lips being the visible part of the mouth.
1. Grk. xefdos, Dor. xfdos, Aeol. XMos (*xédvos; cf. also xedtvn), NG xe (based on pl. 7& xelAn) : ON gjolnar gills’, root connection? Walde-P. 1.682, Falk-Torp 319.
2. Lat. labrum (> It. labro), pl labra, late as f Fike ae em. sg. (> Fr. lévre), ae Sp. labio) : OB lippa, NE 10) fs leffur, lefs, NHG lippe (fr.
» Cle. (see list), root connection un-
Certain, but more prob. : Skt. lamb-
h St Lat. labare ‘slip’, ete. (on IC side, cf, below, 5) than : Lat
mb re sry ba a cg gue. 2.384, Er- 1808 re * Walde-H, 1.738 f. REW ; 18. Falk-Torp 672.
UM. buz¢ R (Cf. below, 3) or like Al
```


## [2026-09-07T15:51:27.230Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"maksi\\|maks-\\|maxs\\|FLY (sb\\|3.82\\|3.83\" SYN.txt | head -20",
 "description": "Find Buck fly section"
}
```


### [2026-09-07T15:51:27.296Z] TOOL RESULT

```
2247:Lett. sérkuocin’¥ (still the usual word?), cpd. of sérs ‘sulphur’ and kuocin's: kuoks ‘tree, stick’. Muhl.- Endz. 3.829.
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
5112:3.82 BEE Grk. pation Goths \3.-..'. Lith. bite, bitis NG pe\ooa ON byfluga Lett. bite Lat. apis Dan. ChSl.  btéela It. ape, pecchia Sw. bi SCr.  pvela Fr. abeille OE béo Boh.  véela Sp. abeja ME ibe Pol. —_pszezola Rum. albind NE bee Russ. péela Ir. bech Du. bez Skt. bhramara-, ali- Nir. beach OHG bia, bini Av. Sieiers W. gwenynen MHG bine Br. gwenanenn NHG biene
5133:3.83 FLY (sb.)
5135:ChSl. mucha SCr. muha Boh. moucha Pol. mucha Russ. mucha Skt. makgsa- Av. maxsi-
5139:4. Skt. maksa-, Av. maxsi- prob. of imitative orig., like the group above, 1. Uhlenbeck 209.
12049:; ‘urniture’ (NED s.v., 2). cae (fr. OF r. mobles) ‘movable prope rty’ covered ‘furniture but never became specialized like the Fr. word. NB furniture, formerly of more gen- eral scope, ‘furnishing, furnishings, im- plements’, etc., fr. Fr. fourniture ‘fur- ishing, provision’, deriv. of fournir ‘supply, provide’, this fr. OHG frum- men ‘perform, accomplish’, deriv. of from ‘further’. Wartburg 3.829 ff. NED sv. OHG giziugali, caziucali (gl. Lat. supoller), deriv. of giziug ‘material’ (NHG zeug); OHG gizawi (also gl. supel- let), whence NHG gezdhe ‘miner’s tools’ : OF geatwe ‘trappings, ornaments, etc.’, a ol ‘make’, ete. Falk-Torp ite ae e-P. 1.779. But whether fierce ee were used for ‘house MEG a5 oubtful. va (> ies husgerete, MLG hus- - husgeraad, Sw. husgerdd),
14226:common, OFr. ete; REW 3482) brecan, etc. (below, Emout-M. 386 fe
14499:It. stendere, Fr. étendre, Sp. tender, all lit. ‘stretch, stretch out’, fr. Lat. ten- dere ‘stretch’ (9.32) orepds. REW 3083.
17159:OFr. floter, Fr. flotter (> Sp. flotar), prob. deriv. of flot ‘wave’, this fr. an OF rank. form corresponding to OF fléd ‘flowing, flood’. Wartburg 3.638 ff. Somewhat otherwise, as to the precise Gme. source, REW 3383, Gamillscheg 426.
23847:QUANTITY AND NUMBER 937 13.832 ONE Goth. ains Lith. vienas ds ON einn Lett. viens tyas Dan. en ChSl. jedint anus Sw. en SCr. jedan uno OE an Boh. jeden un ME oon Pol. jeden uno NE one Russ. odin oun Du. een Skt.  eka- gen OHG ein Av. aéva-, OPers. aiva aon MHG ein oun H i f a NHG em . ; 1B *oi-no-, ete-, derivs. of a pro- *oi-wo-. Av. aéva-, OPers. aiva-; cf. Al gi- beside 7- in Lat. zs, etc. | Grk. ofos, Cypr. offos ‘alone’, and Skt. Mt 1101, Ernout-M. 1127 f. eva ‘thus’,
24569:Grk. _ réxa, abrixa, ebPéws Goth. sprauté; suns Lith. greit; luojau NG oé Alyo, ypiyopa, ON bralt, fljott Lett. driz; tilin YAnyopa; dpéows Dan.  snart; straks ChSl.  skoro; abtje Lat. moz; statim Sw. snart; strax SCr. skoro; odmah It. presto; subito OE sdna, hreedlice Boh.  brzo; hned Fr. bientét; aussitét, ME sone Pol. rychlo; zaraz lout de suite NE soon; immediately, Russ.  skoro; tottas Sp. luego, presto, pronto etc. Skt. maksi; sadyas Rum. indaté Du. weldra, spoedig; dade- Av. mosu Ir. mos- lijk, onmiddellijk NIr. go gairid; laithreach OHG sar, baldé W. yn fuan; yn y fan MHG 4, balde Br. hebdale, bremaik, NHG bald; sofort, sogleich kerkent
24638:8. Skt. maksi, Av. mosu, above, 1.
29380:2. Lat. fidus, fidélis (> It. fedele, OFr. feoil, and feel, feal, Fr. fidéle, Sp. fel. REW 3283), above, 1.
33390:13382 SELECTED INDO-EUROPEAN SYNONYMS
34516:Fr. flotte (> It. flotta, frotta, Sp., Port. flota, Rum. floté) fr. OE flota (below, 4). REW 3383 a. Gamillscheg 426.
```


## [2026-09-07T15:51:30.329Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5125,5150p' SYN.txt",
 "description": "Buck 3.83 FLY entry"
}
```


### [2026-09-07T15:51:30.399Z] TOOL RESULT

```
Digitized by Arya Samaj Foundation Chennai and eGangotri a
Goth. .--- ta ON fluga Gee fae Dan. flue N t musca Sw. fluga Lar nosed OE _fleoge It. mouche ME _ flye e mosca NE fy Het mused Du. _—vlieg en oe OC ie fr. cui : M oliege ab guybedyn, cylionyn NHG fliege
ee he ‘fly’ there is a wide- for the Uy ace of ae group, probably of imi- tative origin. Another group, but ony Gme., is derived from the verb for ‘fly’, with early specialization. ea
1. IE *mu-, *mus-, prob. of imitative orig., with reference to the humming. Walde-P. 2.311. Ernout-M. 646. Falk- Torp 744.
Crk. pvta (*uvo1a), NG pop. piya; Lat. musca (> Romance words); here, but as ‘midge’ ON my, OE mycg, OHG muc- ca, etc. (NHG miicke also locally ‘fly’); Lith. musé, Lett. musa, OPruss. muso; ChSI. mucha, etc., general Slavic.
spread
Digitized by Arya Samaj Foundation Chennai and eGangotri
ANIMALS 193
3.83 FLY (sb.)
Lith. musé Lett. musa
ChSl. mucha SCr. muha Boh. moucha Pol. mucha Russ. mucha Skt. makgsa- Av. maxsi-
2. Ir. cuil, W. cylionyn, Br. kelien- enn : Lat. culex ‘midge’, prob. Skt. gula- ‘spit, pike’, ete. Walde-P. 1.33. Pedersen 1.147.
W. gwybedyn, coll. pl. gwybed, early gwydbed (Morris Jones 180), etym.?
3. ON fluga, OF fléoge, OHG fliuga, etc., general Gmc., fr. the Gme. vb. for ‘fly’, OE fléogan, etc. (10.37), with early and general (though not complete) spe- cialization.
4. Skt. maksa-, Av. maxsi- prob. of imitative orig., like the group above, 1. Uhlenbeck 209.
3.84 WORM Gtk. oxdiAné Goth. mapa (waurms) Lith. kirmele a oKoUNARL ON ormr, madkr Lett. tarps ; 3 «vermis Dan. orm ChSl. ériivt th me Sw. mask SCr. crv Sp ead OE wyrm, wurm Boh.  éerv Rum, yf ae ME ~~ werm, wurm Pol. robak TK neg NE worm Russ. éerv’ Nir. Beat: 2 Du. worm Skt.  krmi- We bin i, » Chutmh OHG wurm Ay. (karama-), NPers. Br. tle Nee wurm _ kirm
wurm
in Majority of the words for ‘worm’ “Ong to one or the other of two groups,
alike j ike in suffix but from different roots of these frou , Words are bas
A few are con- ‘bore’ or ‘
dmnn ; rustle,
the Woodworm, have applied at first to
Several of the words were also used frequently of, some even specialized to, the ‘snake’.
1. IE *wrmi-, fr. *wer- in words for ‘turn, twist’, seen esp. in the extension *wer-t-, in Lat. vertere, etc. (10.12). Walde-P. 1.271. Ernout-M. 1090. NED s.v. worm, sb.
Lat. vermis (> Romance words);
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
```


## [2026-09-07T15:51:37.828Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 242 (p.221) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==242' HRN.txt; echo; echo \"=== HRN leaf 245 (p.224) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==245' HRN.txt",
 "description": "Horn pages 221 and 224"
}
```


### [2026-09-07T15:51:39.115Z] TOOL RESULT

```
=== HRN leaf 242 (p.221) ===
— 220 —
kurd. miMnk, mizl, mujüal (H.-Sch.) ^Augenwimpern';
bei. micäc, n. misäs ^Augenwimpern*, daneben LW.
mizayän (236).
ai. nimis' 'Blinzeln, Zwinkern des Auges*, skr. nMsa-,
das Bartholomae ZDMG. 44, 553 vergleicht, stimmt
lautlich nicht zu np. kurd. i, g. /, bei. c (für letzteres
erscheint im nb. regulär s, vergl. Geiger, Dialekt-
spaltung, 83).
981. ^nest 'betrunken* 0-
aw. vergl. mada- 'Kausch trank* ; phlv. mast (PV.);
ai. mattd- 'trunken', vergl. |/"fwad-, mddati 'froh sein,
sich berauschen'.
Allgemein entlehnt; oss. d. mast, t. mäsf 'Galle,
Zorn' (181) ist wegen des Bedeutungswechsels un-
sicher.
982. ^nust 'Faust*.
mäz. mis (*nitist).
aw. musti.[masah' 'faustgross* ; phlv. must (vd. 17
(18) Gl.) 2), mtistih (AV.), must (PPGl.); ai. musti-,
kurd. mist, miste/c; af/. mmt^ müt; bei. LW. mtist
(172) ; wa;k'. mösty sar. mut
983. tniiSten 'reiben*.
aw. [/^marz-j marezaiti *fegen'; phlv. mmt^ mmt
(vd. 4 (7) (26) für aw. marsta-); ai. l/'mar/-, mdrsfi
'abwischen'.
kurd. mistin 'fegen'; af/. mu/al; bei. musag, n. musay
'reiben*, kratzen, streichen, salben, mahlen' (244).
Eine Doublette zu np. maltden (No. 962).
984. muy, möy 'Magier, Feueranbeter*^), möbed,
ap. magu-; aw. -moyu- in moyu.fbis-? (vergl. Geldner,
*) Irgendjemand hat, wie mir Herr Prof. Nöldeke sagt, irgendwo
(die SteUe war augenblicklich nicht aufzufinden) das als arabisch geltende
medhüs 'sinnlos* für ein persisches Wort (|/ mad' + hös 'Verstand, 8inn*J
erklärt. Ich denke aber, dann könnte es nur mesthös lauten.
') Ganz falsch war natürlich meine Bemerkung ZDMG. 48, 36
Note 34.
') Im späteren Neupersisch ist der Magier zum '(ohristl.) Mönch*
und besonders zum 'Kneipwirt, Zecher* geworden (H ä f i ? häufig), vergl.
auch muybece^ muyän u. a. m.

=== HRN leaf 245 (p.224) ===
~ 223 —
Eine Sonderstellung nimmt im Iranischen — vergl.
auch arm. mrjimn, mrjiun (H. No. 207) — oss. d.
nniljvg, t. mäljig 'Ameise' ein.
994. tnöze 'Schuh', arab. LW. manzaj.
aw. [/^maoc^ mit paiti 'anziehen (sc. Schuhe)*, vergl.
framv/ti' *das Ausziehen (der Schuhe)'; phlv. tnööak
(Men. ; arm. LW. muöak), vergl. mök (chald. LW.
NpID), auch patmö/tan 'anziehen'; ai. [/^möö- mit ä,
prati anziehen (irgend ein Kleidungsstück)*, mit upa
*Schuhe anziehen*.
LW. afy. möza ; bei. müzag, n. mözay 'Socken, Stiefel,
Beinkleider* (174).
995. ninS *Maus*.
g. muSk,
ai. müs~, skr. müsaka-, mfisika- *Maus, Ratte*; arm.
mvkn 'Maus' (H. No. 206).
kurd. fni§ik, misk; Si{y. mayak, maya 'Ratte', maya-
küfai 'Maus, junge Ratte*; oss. d. miste, t. mist (189);
bei. musk, n. milsk (245).
996. möT 'Haar' ^).
g. mld.
phlv. mö, möd bezw. möf; bei. müd^ mtd, n. mi^
'Haar (eines Menschen), Ziegenhaar' (247).
i tritt sonst dialektisch im Np. nur für ursprüng-
liches ü, nicht für ö ein, doch giebt es Ausnahmen;
man wird also trotz g. bei. mtd doch eine ap. Grund-
form *mauda- annehmen müssen 2).
997. möye 'Weinen, Klage', möylden,
aw. vergl. amayavä' 'Leid'; phlv. wöyaÄ:; ai. vergl.
dmtvä'.
Die von Darmesteter, Et. ir. H. 169, ver-
glichenen aw. ai. Worte lassen sich mit np. möye
lautlich nicht vereinigen, und auch Bartholomae,
») Reimt auf röt, 8ähn. III, 1074 Vers 161, auf jöi, Vis und
RAmln, Seite 84 Yers 16.
*j Ganz unmöglich ist Spiegel 's Erklärung, Ar. Per. 61 (vergl.
Bartholomae, ZDMG. 42, 155^.
```


## [2026-09-07T15:51:47.346Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"magas\\|magaS\\|Fliege\" HRN.txt | head -20; echo \"=== leaf 243 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==243' HRN.txt; echo \"=== leaf 246 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==246' HRN.txt",
 "description": "Horn magas and pp.221,224"
}
```


### [2026-09-07T15:51:48.639Z] TOOL RESULT

```
8590:989. meges 'Fliege', jüd.-pers. Mo (Is. 7, 18)«).
8591:aw. vergl. ma/si- 'Fliege, Mücke' ; phlv. magas (vd. 1
8604:n. mahisk 'Fliege, Mücke' (222) ; wa;^'- ^clcs, minj. moya,
9858:mehr auf die Fliege oder Wespe (wenn das ädnui- Obst ist) als auf
=== leaf 243 ===
— 221 —
Ved. Stud. II, 19); phlv. magu, magupat (arm. LW.
mog^ mogpet, movpetan movpet), daneben maupat (syr.
LW. NtOSID, daraus gr. Mavlnväg d. i. Mavmxäg und
Mavinvüv&d d. i. Mavmvovx^ä, Nöldeke, Karnämak
59 Note 4); ar. LW. majüs (Plur.).
985. mey 'Tiefe, Fluss''), meyak 'Graben, Grube* (Sahn. I,
174 Vers 817).
aw. maya- 'Loch'; phlv. may,
986. meyz 'Gehirn*.
Kä§. magz, magzL
aw. mazga- 'Gehirn'; phlv. mazg; ai. majjdn- 'Mark*.
af;'. mayz, Plur. mayza 'Gehirn'; oss. (LW.?) mayz
(174); bei. mazg (229); sar. muig 'Knochenmark', da-
gegen sar. moyz, siyn. mayz 'Gehirn' wohl LW.
987. unuft unbedeutend, umsonst erhalten'.
ai. l/'möC' ^befreien, wegwerfen* (also mtikta- etwas
Weggeworfenes', wie np. Juft aus yuktd-), Darme-
steter, Et. ir. I, 88 Note 2.
Die entlehnten nslov. muhte 'sorglos', serb. mukte,
muktice 'umsonst', ^wwiton^i 'schmarotzen' (Miklosich,
SWAW. Band 35, 129; 37, 86; 38, 176) würden die
ursprüngliche Form dann nachträglich wieder ent-
wickelt haben.
Unsicher.
988. meger 'wenn nicht, ausser, vielleicht'.
me nicht' + eger (No. 106), päz. ma agar (Aog.).
989. meges 'Fliege', jüd.-pers. Mo (Is. 7, 18)«).
aw. vergl. ma/si- 'Fliege, Mücke' ; phlv. magas (vd. 1
^) Den aus dem F§ bei Vullers abgedruckten Sahnämevers
konnte mir Herr Dr. Landauer nicht nachweisen.
') Z statt 8 findet sich dialektisch häufig: z. B. besbäs (AM. 55),
bezhäz oder semärüy, zemärüy oder kusbura^ kuzbura(YvL\\eT8); sepes
(jüd.-pers.) statt zi pes, vergl. si pester (Vullers); Käs. üzü d. i. an
8än; kauk.-bergjüd. zürnai sonst sürnm u. v. a. m. Umgekehrt steht
8 für z im ar. LW. sauswjird *ein Tuch', wörtlich *nadelgefertigt*
(sözengird), de Goeje, Bibl. geogr. arab. IV, 266. Ebenso wechseln
z und s, z. B. /äksi^ -/äkkl (Vullers, vergl. auch ebenda s. v. j^vhe und
=== leaf 246 ===
— 224 —
Studien, II, 178, befriedigt nicht, da er müye^ nicht
7nöye, als np. Form ansieht.
Fr. Müller, (WZKM. 5, 65) construirt eine *[/maud-
mit einem ap. "^matida-- als Grundform und identi-
ficirt np. möye mit arm. moir 'Bettelei', eigentlich
Torjammern', moiracik 'bettelnd' ; dazu auch np. mit st
*Klage*, mustmeud,
998. me (geschrieben meh) nicht* (prohibitiv).
ap. aw. ai. ma 'nicht' (fifj); päz. mo ; arm. mi 'dass
nicht* (H. No. 200).
kurd. me-; afy. ma-; oss. d. t. ma- nicht' (prohi-
bitiv) (173).
999. mih gross*, mehist ^), mihtnj mihter.
g. mas gross*, master.
ap. vergl. ma&ista- grösster*; aw. masyao grösser*;
phlv. mas gross, grösser, grössest', masist, mas(i)st,
vergl. 7nas[mayan *Grossmagier (AlbSnlnl), masTh%
mahist, päz. meh (PPGL); arm. vergl. mec gross' (H.
No. 191).
af/. masar 'älter, Herr*.
Vergl. zu bih (No. 241).
1000. mihr *Sonne; Liebe', mihr[ban 'freundlich, wohl-
wollend*.
ap. Mid^ra^, vergl. Vaulmisa-; aw. Mi&ra-, mi&ra^
'Vertrag*; phlv. mür, päz. mihir (vergl. Meherdates,
Tac, MsQfiBQorig^ Proc, skr. LW. mihird- *Sonne');
ai. Mitrd", mitrd- 'Freund*.
minj. mira 'Sonne.
1001. muhr 'Siegel; Siegelring,
skr. mudrd- 'Siegel, Siegelring; phlv. mutrOk d. i.
mudrak 'B,ing'(?), vd. 2 (18) Gl.^), nmdar, muhr 'Siegel'
(PPGL), chald. LW. piniD, arm. LW. murhak.
LW. kurd. mör (H.-Sch.); oss. mi/ur; bei. vergl.
murdan, murdänay 'Finger* (No. 242).
^) Belege aus dem äähnäme (Maoan) bei Noldeke, ZDMO.,
46, 139.
*) P.-Vend. masäi (vergl. dräjlh^ No. 547).
*j Darmesteter, 6t. ir. I, 93 Note 3 (sehr unsicher).
```


## [2026-09-07T15:52:05.120Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==244' HRN.txt | head -40",
 "description": "Horn p.222 continuation"
}
```


## [2026-09-07T15:52:06.898Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; do echo \"== $f\"; grep -o \"\\[pdf page [0-9]*\\]\" $f | head -2; grep -o \"\\[pdf page [0-9]*\\]\" $f | tail -2; wc -l $f; done",
 "description": "Inspect BQT vol3-5 page files"
}
```


### [2026-09-07T15:52:06.999Z] TOOL RESULT

```
— 222 ~
(16)), makas (Bahmyt.), mo/s (nur Umschreibung des
Awesta Wortes) ; ai. vergl. mäksa-j mdksikä-.
kurd. mis (LW. magäs'BiQne'); bei. makask, magisk,
n. mahisk 'Fliege, Mücke' (222) ; wa;^'- ^clcs, minj. moya,
np. meges ist wie die sämmtlichen anderen neu-
iranischen Worte ausser kurd. mis nicht direct mit
aw. ma/si-, ai. mdksa' (^2«) vereinbar.
990. mul Wein'.
ai. fn^d[vtka- 'Weintraube' (Hübschmann, ZDM6.
35, 133 Note 2).
niele% 'Heuschrecke' (Öähn. I, 188 Vers 1059) s. meig
(No. 1010).
991. {\)fnen *ich', men^ 'Eigenliebe, Übermut'.
ap. manä meiner (Gen. sg.); aw. mana; ksl. mene.
991**^ {2)men 'ein Gewicht' ^), ar. LW. mann,
skr. vergl. niäna- 'Maass (ganz allgemein), Maass-
stab, Gewicht', dann auch ein bestimmtes Gewicht'.
Oder zu ai. mand- 'ein best. Gewicht (Gold)', gr. ^«v«,
lat. mina, die semitische LW. sind, vergl. akkad. mana
(Schrader, Sprachvergl. und Urgesch.- 206 folg., 252)?
992. meniS, menisn (Wörterbücher) 'Sinn, Charakter,
vergl. dus[men, rr^^DirilD (Is. 12, 1).
ap. vergl. 'Jlpiaj/LisvTjg (Plutarch); aw. manah-^ dm-
manah-; phlv. dusman, vergl. men(i)sn; ai. rndnas-,
skr. durmanas.
993. mör 'Ameise', mürce-),
g. möirik 'schwarze Ameise'; Käs. V. möröund,
aw. maoiri- 'Ameise'; phlv. mör.
LW. (?) kurd. mürt^ merü (vergl. np. mtrük, nicht
belegt); afy. bei. (248) mör, n. möHk "Ameise*, vergl.
auch mörag 'Korn an der Flinte' (?); echt yidg. mur-
yäh (BB. Vn, 198).
^) Genaue Angaben über die verschiedenen gebräuchlichen Mens
findet man bei F. Stolze und F. C. Andreas, Die Handelsverhältnisse
Persiens (Petermann^s Mitteilungen, Ergänzungsheft Ko. 77), S. 83.
*) Keimt auf hör fäähn. I, 508 Vers 135), vergl. auch das reimende
hemcü mör bezör.
```


### [2026-09-07T15:52:08.659Z] TOOL RESULT

```
== incoming/BQT/BQT_v3_pages.txt
[pdf page 1]
[pdf page 2]
[pdf page 720]
[pdf page 721]
51425 incoming/BQT/BQT_v3_pages.txt
== incoming/BQT/BQT_v4_pages.txt
[pdf page 1]
[pdf page 2]
[pdf page 552]
[pdf page 553]
22553 incoming/BQT/BQT_v4_pages.txt
== incoming/BQT/BQT_v5_pages.txt
[pdf page 1]
[pdf page 2]
[pdf page 292]
[pdf page 293]
10090 incoming/BQT/BQT_v5_pages.txt
```


## [2026-09-07T15:52:15.537Z] TOOL CALL #25: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py",
 "description": "Read ref_page.py header"
}
```


### [2026-09-07T15:52:15.584Z] TOOL RESULT

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


## [2026-09-07T15:52:18.765Z] TOOL CALL #26: Bash

```json
{
 "command": "for p in 2002 2029 2035 2058; do echo \"########## BQT:$p ##########\"; timeout 300 python3 tools/ref_page.py BQT:$p --image 2>&1 | head -60; done",
 "description": "Fetch BQT cited pages"
}
```


### [2026-09-07T15:52:41.835Z] TOOL RESULT

```
########## BQT:2002 ##########
(no exact page map; using offset -1917 -> pdf page 85; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2002.png
REF: BQT:2002  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 85  OCR-lang: fas

م زکو ۱ و
و سکون ثالی و فوقالی » مسجد را کوبند که | بالف کشیده . بلفت زند بمعنی‌ترازوباشد وبعربی
بفارسی خالهٌ خدا و بعربی بیت‌الٌ خواشد ۱ . میزا ن گوبند .

م ز کو ای اول و فتح بالی و کاف مزنده * بروزن رونده» کوزه 1 بخوریرا
مشدد و غیر مشدد بواو کشیده . نوعی از طعام | کوبند - و پمعنی مکیدلی هم‌آمده است ‎٩‏ -
است . ومکنده را نز کوبند که فاعل باشد چه مزیدن

هز که < بکر اول وافتح کاف افارسی, بمعنی مکیدن است .
حوای تیره راکویند ۴ . مز نگ - با کاف فارسی بر وزن

مزمل - بنم اون وفتح ثانی ‏ وکسرمیم ارسطو » خارپشت را گونند و آن جالورست
ِ وسکون لام ۱ لوله‌ای ار ی مشهور ۷ 4

چون برجاب راست پیچند آب از آن ۰ ی
روان شود وا گر بطرف چپ گردانند باینتد واين مزید » پرورل و همنی مکید باشد که
لوله را ببشتر درحمامها وآب انبارهای‌سرپوشيده ماضی مکیدن است ۸ - ودر عربی ابمعنی اضافه
صب‌کنند ۴ - و با تشدید انی وثالث, درعربی و زیاده کرده شده باشد ‎٩‏ .
بمعنی درجامه پیچیده باشد ۴ . مزیدن *۱- بر وزن و معنی مکیدن

زا * -:بکر اول وسکون ثانی‌ویون | باشد .

۹ - تو هشرف تری زهر هردم همچو بیت الحرم زهر مزکت .

سوزنی سمرقندی « رشیدی *.

۴ - رك : رشیدی. ۴ - در قاموسهای عربی‌باین معنی نیامده؛ ولی دربین‌النهرین
هنوز ۶ مزمله > بهمین معنی استممال شود :

پیروزه همچو سیم کشیده فرو رود از کوعهٌ مزمل زرین بابدان .

۰ ازرقی‌هروی ۶« جهانگیری > ورك : رشیدی.

۴ - رك : اقرب الموارد » قطرالمحیط » منتهی‌الارب .

8 -هز . 32288 , 13221808 ۰ پهلوی 18۵۳2206 ( ترازو ) ۶ پونکر ص ۰۱۱۷
ی : میزان (عر) . ‎٩‏ - باین معنی نیست و صحیح بمعنی آخراست که اسم فاعل باشد .

۷ - رك : مرنگو. ۸ -رك : مزبدن . ‎٩‏ -رك : اقرب الموارد :
منتعی‌الارب . پهلوی 17116112 ۰ کردی ۲۳1418 ۰ 11201770 ( مکیدن ) »بلوچی
8 طع 215۳۵ ( مکیدن ) . از ربعة -71360/0 ( مکیدن ) * اسشق ۹۷۹ «وبشمان
هه گوید : ريشة این کلمه » چنانکه از اشکال لهجه‌بی برمياید ۴ . ۳۱6 ( 186
قس : کردی ۳6۲۵2۳۵ ۰ پهلوی 10802۴ با 121627 . بازند 17112 , 131208 ) است .
همچنین 73221080 بجای 7721210128 بکار رفته است .

0 هزه - بفتح اول و دوم ( درلهجة مرکزی بکر دوم )ءپهلوی 602 ۰ 1210816
« تاوادیا ۱۹۳ > ۰ کردی ع 13626 ( ذوق . طعم ) « ژاباص ۳۹۷ ۰ قس : عربی « مزة [ بفتح
اول ] یکبار مکیدن » « منتهی‌الارب * رك : مزیدن ؛ کیفبتی که از چشیدن , جویدن ولوشیدن
ادرا شود مثل شیرینی» شوری , تلخی و جزآنها - بمعنی مزبدن هم آمده - آنچه با مشروب
خورند ( از قبیل آجیل » سبزی و غیره ).

(برهان قاطع ۳۵۳)

########## BQT:2029 ##########
(no exact page map; using offset -1917 -> pdf page 112; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2029.png
REF: BQT:2029  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 112  OCR-lang: fas

-۷۹- مگل
که نهایتمبالفه کردن درکاری ومعامله‌ای وطلبی باشد که پیش کی است .
بیان بیست ودویم
در میم با کاف فارسی مشتّمل بر پنج لغت و کنایت
هگ - بنتح‌اوز وسکون‌انی,جماعتی‌اند مس پر الیدن «کنایه از کسادی
که ایغان در سواحل بعضی از بحور میباشند - | بازار باشد. .
و بلفت زند و پازند (۱) درخت و نغل خرما را مس گیر * - بر وزن نفی‌کیر .
گوبند ‎٩‏ .
۲ عنکبوت را گوند ۰
مگر < بفتح اول وثانی وسکون رای مگل » بنتم اول ثانی وسکون ۷
قرشت, ترجمةٌ الا است وازبرای استثنا میآید ۳ بح ود وی وستوت ۲۳ ۰
- و در مقام شك وکمان استعمال میکنند ۴ ی | بمعنی وزق و غوك باشد - و بکسر نانی , زلورا
درمقام شین وتحقیق-و گاهیدرمغامبقین-وتمنی ر گوبند وآن کرمی است سیاه رلکه. خون فاسد
هم میآید .۸ را از بدن واضای مردم بمکد .
(۷) چك : ژد و پاژد .. 1
- هز. 88). پهلوی 5(8277738۷) (خرما) «یونکرص۱۱۸* قس:ت4. ونگه درمتن به
« هگ > تصحیف شده است. ۴ - پپلوی 8812۵7۲ 18 ( شاید ) ۸« نیب رکه س ۰۹۱
از : م ( علامت نفی ؛ نهی ) + اکر (ه.م.) , پازند 8887 138 « اسشق ۰۶۹۸۸ کردی ع
7 (اگرنه , انفاقاً ) ‎٩‏ ژابا س ۸*4 >. ۴ -گوبند : همه‌آمدند مگرجمشید.
۴ - و باشد » بود » شاید :
مگر صاحبدلی روزی برحمت کند درکار (حق) دروبشان دعائی .
2 کلتان ص ۰.۹۱۵
8 - از : مگی+ کیر (کیرانده) .
۰ مس ‌- بح اول ودوم » قيی اوستابی-187801 (مگی ۰ پعه) ۰ پپلوی 38
5 تب 28250 ( فقط در غرح کلمات اوستایی ) » بلوچی 3286281 ۰ 15ق328 ۰
8 ( مگی . بعه؟ ۰ وخی 28165 . منجی 3208108 « اسشق ۱۹۸۹ ساسکرت
طفعاهط , شقطکاه ( بش )و شغانطگ‌گاهت , اضای 2226 ( مگی ) از۲اطی8 02
«هوبشمان ۹۸۹ . دراوراق مانوی ( پارتی ) 77389 ( مگس ) « هنینگه. فپرست کلمات پارسی
میاه , 8505 ۱۳ 1 س ۸۵) اکردی 750 ۰ 12620 ۰ 9 ۰ زازا 65 رنه
«زاباص ۳۹۹ » کیلکی 1۳28827 ؛ حشره‌ای از راستهٌ دوبالان؛ ۲ |
دارای خرطومی که رای آن برجسته و اسفنجی است . دو چشم یرال سس
مر کب‌بز رکه ودوشاخك کوچك کوتاه ويك جفت بال‌دارد. یاهای 5 ار یک
مگس بچنگالها و بادکش‌هایی ختم میشود . مگس با خرطوهش
هرچیز مایع را میمکد و ازآن تغذبه میکند و برروی زیاله و .مکی
کنافات تخم میکند .

########## BQT:2035 ##########
(no exact page map; using offset -1917 -> pdf page 118; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2035.png
REF: BQT:2035  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 118  OCR-lang: fas

ی ۳و
عیبی وعلتی راگوبند که مخصوس چشم است . مهن ۴ - بنتح اول وکس‌انی وسکون
ممالان ۱ - یک اول و سکون تابی‌و | نون » بزبان ترند و پازند (۲) بمعتی چه بافد
لام بالف کشیده و بنون زده, نام پدران هستودان | جنانکه هر کاء گوبند ممن‌میگویی‌اراده‌آن باشد
است واوپادشاه تمامآذربایجان بوده واورا امیر(۱) | که چه میگوبی .
مملان میگفته‌اند . ۰ ممول ۴ « بفتح اول وبانی بواو رسیدم
مملخت ۲ « بفتح اول بروزن ب.بخت. | و بلام زده » هنم ازدرنکه نمودن وتأخیر کردن
کفش و پای افزار باشد ؛ و باین معنی هملخت | باشد پمنی درلکه وتأخیرمکن . چه مول بمعنی
نی زآمده اس ت که بجای میم اول ها باشد. تأخیر و درلگه است .
بیان بیست و پنجم
در میم با نون مشتمل بر هفتاد و هفت لغت و کنایت
من بغتح اول و سکون ثالی: معروف | استاری پاتزده مثقال ۷ که مجموع من ششصد
است وآن وزلی باشد معین‌درهرجایی9 » وآنچه | مثقال باشد بوزن تبریز واهر مثقالی شش دالگه
درین زمان متمارف است چهل استاز است۹ وه" ِ ودانگی هفت حبه وحبه‌ای‌بوزن‌یکجوه ؛ وباین

(۷) چك » چش : امیره (۱) . (۷) چك : ژند و پازند .

‎٩‏ - ابومنسور غرف‌الدین مملان بن وهودان ( امیرسیتد‌الدوله .وشرف‌المله ایومنصور)
این‌محمد روادی از امرای سلسلهٌ معروف به « وهسودانیان > با « روادبان > که بر ناحيةٌ شامل
طارم و سمیران و تبریز و مراغه وگنجه حکومت داشته‌اند , وامملان از ۶۵۰ تا ۵۱۱ پادتاهی
واز سلجوقیان پیروی‌م ی کرد . ۶ لفیسی . رودکی ج ۲ 4-۷۸۳ >

‏۴ - مسحف «هیلخت» (۸م.) ‏ ۴ - هز. 538792 ۰ 22)1(۳88 :38322
پیلوی 28 ( چه » کدام ؟ ) « پونکر سس ۰۶۱۱۷ ۴ - هی از «مولیدن» (هم.)

‏8 -قی : ساسکریت -32288 ( مقیای » وزن » وزنی معین ) با از هندی باستان
4 ( وزنی معین [طلا] ) » بونانی 3288 ۰ لانینی 22188 » قس : کدی 32888 معرب
« من » « اسشق ۹۹۱ 018 > .:درزبان شومری ( قوم غیرسامی وغیرآربایی ) لفت 12882 بجای
مابده , واز آنان با کدیان رسیده » 13280 گفتند. ودرعبری 1328۴3 شده است. «من» اساسا
وزنی بوده وسپس لام پولی کردید و بمرور زمان تزد افوام مختلف » ارزشهای مختلف پیداکرد -
رك : هرمزد نامه 2-۲۹۳ . ‎۹٩‏ - رد : استار. ۷ - اکنون هرسیر را ۱۹متقال
کيرند. ۸ - اکنون نیز « من تبریز »4*۳ سیر ۳ ۹۶۰ متقال ۳ ۳کیل وکرم ؛ «من
خاء:» ۲.۳ من‌پبریز ۳ ‎٩‏ کیل وگرم ؛ « من ری »۲۷۳ من شاء ۳ ۱۲ کپل و کرم ؛ امن شرعی» :۳
۱۸۰ متقال . رك : فرهنگه نظام ورك : حاشیةٌ مد :

########## BQT:2058 ##########
(no exact page map; using offset -1917 -> pdf page 141; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2058.png
REF: BQT:2058  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 141  OCR-lang: fas

موبهة زال له
تحتانی + گربه با توحه را گوبند - وناله وزاری مو لیدن ؟ (۱) - بروزن‌روییدن(؟)»
را نیز کفته‌اند . بمعنی گربه ولوحه کردن وگریستن باشد.
موی ذال - با زای نقطه دار بالف مویینه ۴ (۲) - بنتم نون » پوسین
کشیده و بلام زده » نام نوی و لحتی باشد که راکوبند مطلقاً خواء سنجاب وخواه سمور وقاقم
تمه و ْ وامثال آن باشد - و مو لین (۳) ۵و پوستین
مویه گر بفتح‌کاف فارسی , نوحه دوز را میگویند ۰ ۱
کننده راگونند . َ
بیان بیمت 9و هفتم
در میم با ها مشتمل بر هفتاد و هشت لغت و کنات
۹۸۵ - بفتح اول و ظهورئانی . مخقف ماء | ودرنفرین ودعا هردواستعمال میشود همچومپیناد۹
است که قمر‌باشد 9 - و بخفای ثانی » بمعتی نه | - وبمعنی قلم وكلك هم بنظرآمده است - وتل
باشد که حرف نفی‌است وبعربی‌لا کوبند ؛ وافاده | ریگ را نی ز کویند - و بکر اول وظهورئانی »
معدوم شدن ونابو دکردیدن هم میکند مثل «مه | بمعنی بزرکه باشد ۷ چه بزرکتر را مهتن
این ماند ومه آن > پعنی نه این ماند و نه‌آن ؛ خوانند - و بمعنی میغ ونزم هم‌آمده است وآن
() چش : موئیدن . (۷) چش : روئیدن . (۳) چش : موئینه .
۱ - بلفظ پارمی وچینی و خماخرو بلحن موبهٌ زال و قصیدء لغزی .
« منوچهری دامفانی ص ۰۱۱۲
۴ - از : موبه + کر ( پوند شقل و مبالفه ). ۴ - از : موی (موبل۸هم.] )
+یدن ( پوند مصدری ) . رك : اسشق ۹۹۷ ؛ دارمستتر . تتبعات ج۲ ۰۱۹۹
۴ - از : موی +ینه ( پسوند نبت ) . 8 رك : ماه .
‎٩‏ - پپلوی 7138 (علامت نهی ) ۱ 1172 338 ( مکن ) ؛ ابرانی باستان 132 «بارتولمه
۵ نیب رکه ص ۱۶۳ > ؛ پارسی باستان واوستا و هندی باستان 3242 (نه) » پازند 132 ۰
آرمنی 3۵1 (که نیست) » اففانی -1238 » استی -1338 ( مه ء علامت نغی ) « اسشق۹۹۸* کردی
6 ( نه, مه [علامت نهی ] ( «زابا 4*۹ پشتو 118 «بلیو ص۱۵۹ .ور4: مقدمهٌ موْلف ص‌به.
۷ - پهلوی 1360 ( بزرکتر ) » پارسی باستان -2۵1[01(20 5 » ایرانی باستان
‎278٩1720‏ « نیب رک م۱۱۸۸ اوستا 1325220 (بز رکتر) . نیزپهلوی 1288 ( بز رکه .
بزرکتر » بز رکترین ) » 388151 ۰ 73388)1(81 ۰ قس : 1328]13281020 ( بز رکه و رئیس
مفان ) ؛ ۵118۳ , پازد 12610 , ارمنی 13360 ( بز رک ) . افغانی 13-28827 ( ارشد:آقا)
«اسشق۹۹۹*. صیفهٌ عالی‌از۰561 پازند, غ2[0653, 13212881 * پارسی باستان 71722110181012
است . در کردی 112911۳ ( بزرکتر ) » کاشانی 13218547 ۰ 11118867167 آهده ۶ هوبشمان
۹ > ؛ خواناری 308527 ( بزرکتر ) « سالنامه کلپایگان ‎4٩‏ > . نایینی 17128518
(بز رکه) ,کبری پزد 1335 . ر4 : ...,6ل8120228 ۲۵۵ 1۵ ۲۵ 2 ۵۵ 310165 ,۳96
( .0.1 .1 ,۷ 10040-17801 )
( برهان قاطع ۳۹۰ )
```


## [2026-09-07T15:53:26.923Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AKD leaves 27-30 ===\"; for n in 27 28 29 30; do echo \"--- leaf $n ---\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' AKD.txt | head -30; done",
 "description": "Zimmern pp.19-22"
}
```


### [2026-09-07T15:53:28.200Z] TOOL RESULT

```
=== AKD leaves 27-30 ===
--- leaf 27 ---
,  wie  wohl  auch  schon in  der  urspr.  Bed.  Silber  (s.  dazu  unten  S.  59),  so  besonders  in  der  Bed.
1)  Von  qanä  gründen,  schaffen  (hebr.  imd  arab.)  viell.  ganz  zu  trennen.
2)  Allerdings  ist  zu  bemerken,  daß  im  Akk.  qanü  Rohr,  zwar  als  Längenmaß  (s. unten  S.  22),  jedoch  in  der  Bed.  Wage  gerade  nicht  üblich  Lst.  Andererseits  scheint  auch das  Akk.,  wenn  auch  als  selteneres  Wort,  ein  Verbum  qanü  erwerben,  zu  kennen.
3)  Urverwandt  mit  hebr.  usw.  jsp,  wsp  hinzufügen.
4)  Eig.  Besitzer,  Pto.  von  raSü  in  Besitz  nehmen,  das  wohl  mit  hebr.  järas,  aram. jerat,  ai'ab.  warita,  äth.  warasa  in  Besitz  nehmen,  erben,  gleichzusetzen  ist.  Dagegen  ist aram.  raiä  Macht,  Erlaubnis  haben;  Kaus.  gestatten,  verleihen,  wohl  erst  <;;^  akk.  raSü.
5)  Hier  hätte  sich  also,  bei  unserer  Annahme,  das  urspr.  r  gehalten,  gegenüber  dem H  des  Hebr.  u.  Arab.
3
      18      
Geld  erst  auf  deu  gleichen  Sprachgebrauch  von  akk.  kaspti  zurückgehen. —  Beachtenswert  ist  auch  die  hebr.  Kedensart  ba-Jcäsep  male  in  vollem Betrage,  die  wohl  dii'ekt  in  Anlehnung  an  die  gleichbedeutende  akk.  Redens- art ana  kasap  gamirti  od.  ana  simi  gamri  (<^  sum.  sam  til-la)  entstanden  ist.
akk.  maluru  Kaufpreis  (von  mahäru  einnehmen,  s.  S.  16)  :  >  hebr. m9htr  O  ägypt.  mhr).  —  Weniger  sicher  ist,  ob  etwa  auch  hebr.  möhar, aram.  nidlirö  O  armen,  mahr),  mnhrä,  arab.  /««/(»•  Kaufpreis,  den  der  Bräuti- gam an  den  Yater  der  Braut  zahlt,  auf  eine  Übernahme  des  gleichen  akk. niaJuru  in  früherer  Zeit  zumckgeht.
akk.  simii,  simtu  Kauf,  Kaufpreis,  Wert  (von  sämti  kaufen,  das wahrsch.  <<  sum.  sam,  und  von.sr7w«M,  St.  .syV«,  festsetzen,  wahrsch.  zu  trennen)  : ;>  w'ohl  aram.  Sum  abschätzen,  südarab.  S^m  kaufen.
Für  die  spez.  Bed.  Summe  des  hebr.  ros  (Kopf,  Haupt),  wie  die Bed.  Summe,  Kapital  des  aram.  rcsä,  arab.  ras  könnte  das  akk.  qaqqadu (Kopf)  in  der  Bed.  Summe,  Kapital,  ähnlich  auch  res  (makkurij,  vorbildlich gewesen  sein.  Doch  könnte  hier,  im  Hinblick  auf  die  gleiche  Bed.  von xKfalt]  imd  Caput,  die  doch  kaum  aus  dem  Semit,  stammen  wird,  auch beiderseits  eine  unabhängige  Entwicklung  vorliegen.
Das  im  Akk.  übliche  Wort  für  das  Anwachsen  der  Zinsen,  rabn, eig.  großwerden,  wachsen,  büdet  wohl  erst  den  Ausgangspunkt  fiii-  hebr. marhä  u.  tarhit  Zins,  aram.  rehhUft  (daraus  jüd.-deutsch  Bebhes  ?),  arab.  rihan.
akk.  Imhullu,  auch  Ijahullu,  Schuld,  Zins  :  >  hebr.  habol  Pfand, jüd
--- leaf 28 ---
.-aram.  hibbtilä,  liibbiiljä  Zins,  syr.  htihla  Schuld,  Zins  (]>-  arab.  Ijabl Schuld,  Darlehen,  'ahhala  darleihen).
[Dagegen  ist  es  bei  hebr.  'äbot^  'abtU  Pfand,  und  den  davon  abge- leiteten Verbalformen  unsicher,  ob  es  sich  um  ein  mit  akk.  ubbutu,  ubhutu binden,  fesseln,  vereinzelt  viel!  auch  vei'pfän4en,  urverwandtes  Wort  handelt, oder  ob  auch  hier  Entlehnung  bezw.  Anlehnung  auf  der  einen  oder  der anderen  Seite  vorliegt.]
akk.  maskanu  Pfand'  :  >.  aram.  maskönä,  meskänä,  maskäna  Pfand, masken  zum  Pfand  geben   (>>  arab.  muskän  Pfand,  massaka  bürgen).
akk.  paqadu  jem.  etwas  ins  Depot  übergeben,  piupiddü  Depositum:
1)  Eig.  Depositum,  von  Sakänu  niederlegen,  wie  hebr.  tasüviet-jsd  von  siim;  also nicht  von  msk  abzuleiten.  In  iilterer  Zeit  hat  maSkami  auch  die  Bed.  Lagerhaus, Speicher;  daraus  wohl  sicher  durch  Entlelmung  hebr.  miskanot  Vorratshäuser.  S.  auch noch  unten  S.  30  zu  Sakänii.
      10
davon  wohl  beeinflußt  hebr.  pfiqad,  piqqadon,   aram.  luqdöm^  imqdänä  in dieser  Bed.
akk.  dannitu  Schriftstück,  Geschäftsurkunde  :  häufig  wiederge- geben durch  dnt  in  den  aram.  Beischriften  assyrischer  Geschäftsurkunden. '
akk.  nibsu  Urkunde  :  >  ägypt.-aram.  nhz  Quittung,  womit  auch sonstiges  aram.  nibsa  Los,  identisch  sein  wird.
akk.  satrirti  Schriftstück,  Urkunde  :  >  wohl  das  häufige  str  Ur- kunde in  aram.  Beischriften  auf  assyr.  Geschäftsurkimden ,  sowie  auch sonst  aram.  .idtdra.     S.  im  übrigen  zu  satäru  schreiben,  unten  S.  29.
akk.  Sipru  (von  suparii  senden)  Sendung,  briefliche  Sendung, Schriftstück  :  >  hebr.  seper,  sipr-,  aram.  siprö  Buch,  spez.  auch  in  der Bed.  Geschäftsurkunde.  -
akk.  egirtu  Brief,  Schriftstück  :  ]>■  aram.  'iggärri  Brief,  spez.  auch in  der  Bed.  Schriftstück,  Gescliäftsurkunde,  so  in  aram.  Beischriften  zu assyr.  Geschäftsurkunden  und  auch  sonst.     S.  zu  egirtu  auch   oben  S.  10.
[akk.  srpti  Schreiben,  Brief  :  dieses  speziell  nur  in  der  altbab. Zeit  sich  findende  seltenere  Wort  scheint  umgekehrt  damals  aus  südsemit. Gebiet  mit  von  dort  einwandernden  Stämmen  ins  Babylonische  eingedrungen zu  sein.  Vgl.  äth.  sal/afa  schreiben,  und  das  erst  aus  dem  Südarab.  ins Xordaral).  eingedrungene  arab.  mashaf,  mmhafB\xch,  saJnfat  beschriebenes Blatt]
akk.  diippu,  tuppu  Tafel,  Schriftstück  (<^  sum.  daib
--- leaf 29 ---
),  wozu  dappu Brett,  wohl  nur  eine  Variante  büdet :  >  aram.  dappfi  Brett,  Tafel,  Blatt- seite, auch  ägypt.-aram.  tp  Brett  O  wohl  arab.  daff  u.  faff  Brett,  Seite, daffat  Buchdeckel),  südarab.  ff'  Tafel.  Vgl.  auch  unten  S.  29  zu  tupsarru Tafelschreiber  u.  liebr.  tipsar.  —  Ferner  ]>  altpers.  dipi  Inschrift  (wozu viell.  neupers.  dehir  Schreilier,  diivun  Buch),  elam.  tuppi  Inschrift,  lud. dipi  (lipi)  Schrift.
akk.  giitu  Tafel,  Urkunde  (<<;  siun.  gida  eig.  wohl  lange  Tafel): >>  aram.  gitfä,  geUä  Urkunde,  Testament,  Scheidebrief  O  arab.  qitt  Buch, Scheck).  akk.  nijäru  Papyrusurkunde  (auch  im  Akk.  viell.  Fremdw.) :
>  neuhebr.  najär  Papier,  Pergament.  akk.  urMnu  Scliilf,  Papyrus-
1)  Ob  viell.  auch  so,  und  nicht  als  pron.  dem.,  das  dnh  in  der  Aufschrift  zu  der Geschäftsurkunde  des  aram.  Pap.  28  (Nr.  30)  aus  Elephantitie  aufzufassen  ist?
2)  Weniger  sicher  ist,  ob  etwa  auch  neuhebr.  sdhcr  i  Quittung  hierher  zu  ziehen  ist.
3*
      20      
Urkunde  :  >  wohl  aram.  'urbänä,  'arhänä  Schilf,  Papyrus.  S.  uoch unten  S.  56  zu  urhänu.
Das  übliche  akk.  Wort  für  Siegel,  hmuJchi,  hat,  wie  es  scheint, nur  im  Armen,  als  hiiJc'  Eingang  gefundeh.
[Dagegen  liegt  hebr.  fabhaat,  aram.  tib'ä,  fdb'ä  Siegelring  (das  wohl auf  ägypt.  db'-t  Siegel,  zui'ückgeht)  im  Akk.  wohl  nur  als  westsemit.  Fw. in  der  Form  titnhui,  timbuttu  vor.  i  S.  auch  noch  unten  S.  30  zu  tim- buttii  als  Musikinsti'ument.]
akk.  maklmru  Habe,  Besitz,  mit  der  Nebenform  namJmrru  :  >  wohl liebr.  mäkar  verkaufen  O  ägypt.  mJcr''  Kaufmann),  mäher  u.  mimlcär  Ver- kauf, Ware,  syr.  m^kar  kaufen.    S.  femer  oben  S.  16  zu  tantJcaru  Kaufmann.
akk.pron.  indef.  memeni  (so  namentlich  später  neben  dem  in  älterer Zeit  dafür  üblicheren  minimv)  „irgend  etwas"  i.  S.  v.  Besitz,  Habe  :  > walu'sch.,  der  Form  nach  aber  wohl  das  aram.  pron.  indef.,  späthebr.  iiiämon (Sir.  31,8),  aram.  mamöna,  neutest.  fiafjwväg  „Mammon".
akk.  nikasu^  Habe,  Vermögen  :  >  aram.  niksm  Schätze,  Reich- tum O  wahrsch.  erst  späthebr.  ndhäsim),  viell.  auch  südarab.  nskm.
akk.  nisirfu  Schatz  (von  nasäru  bewahren)  :  fraglich,  ob  etwa  hier- auf liebr.  'dsär,  PI.  'dsärot,  aram.  'au-prä  Vorrat,  Schatz,  zurückgellt.  ^
Zu  blt  nakamti  Seh  atz  haus,  hebr.  bet  nakot,  s.  oben  S.  8.
Zu  hebr.  usw.  saguUä  
--- leaf 30 ---
und  rdkvs  Eigentum,  Besitz  s.  unten  S.  41.
alck.  Msu,  auch  kläu,  Geldbeutel :  >  hebr.  Ms,  aram.  htsä  O  arab. Ms,  äth.  Ms,  pers.  tee,  griech.  xlai?,  wohl  auch  jüd.-deutsch  Kies  Geld). —  Auch  hebr.  'abnS  Ms  (Gewichts) steine  des  Beutels,  wird  direkt  akk. aban  Msi  nachgebildet  sein.
Zu  akk.  kaspu  i.  d.  Bed.  Geld  s.  oben  S.  17 f.
Zu  akk.  hura.su  Gold  s.  unten  S.  58  f..  —  Dem  akk.  htirOm  sagrn (sagiru)  gediegenes  (eig.  verschlossenes)  Gold,  ist  hebr.  zaMb  sägür  mit gleicher  Bed.  wohl  direkt  nachgebildet.
akk.  manu  Mine  (fragUch  ob  <  sum.  mana,  oder  ob  dies  <<^  akk.
1)  Ein  angebliches  schon  altbabyl.  iehltu  Siegel,  ist  nicht  gesichert.
2)  Sehr  fraglich,  ob  ursprünglich  Schlachtvieh   bedeutend,  vielmehi'  wahrsch.   von nakäsu  (den  Kopf)  abschneiden,  ganz  zu  trennen  und  viell.  sum.  Ursprungs.
3)  Formell  würde  besser  massartu  als  Vorbild  passen;  aber  dieses  bed.  eben  nicht Schatz,  sondern  "Wache.    Übrigens  kennt  das  Akk.  viell.  auch  einen  St.  asäru  aufhäufen.
      21      
mann,  dann  manu  Mine  viell.  von  mann  zählen,  minu  Zahl)  :  >  hebr. rmne  O  ägypt.  mn  (mano)),  aram.  manjrl  (auch  in  mawe  Dan.  5,25  f.  „Mene- tekel" urspr.  vorliegend)  (^  arab.  mana[n)),  angelilich  ind.  manä,  griech. fivä,  lat.  mina,  „Mine".  —  Dem  akk.  ina  mane  .<•«  tamhari  nach  der  Mine des  Kaufmanns,  wird  hebr.  Jcäsep  'ober  las-sdher  direkt  nachgebildet  sein.
akk.  s^iqlu  Sekel  (von  'mqolii  wägen,  darwägen,  zahlen,  vgl.  oben S.  17  und  unten  S.  23)  :  >  hebr.  säqel,  Siql-,  altaram.  sql,  später  fdqel  (so aucli  Dan.  5,25.27  „Menetekel"  urspr.  vorliegend),  tiqlä,  griech.  aiyXog  (als Bez.  einer  pere.  Silbermünze),  alxlos;  (für  das  hebr.  .sage?  bei  LXX).
akk.  parsu  Halbmine  (von  par(7isu  teilen)  :  >  neuhebr.  parüs,  alt- aram. prs,  auch  p^-s  (auch  parsin  Dan.  5,25.28.  urspr.  vorliegend).
akk.  haUüru'-,  ein  Unterteil  des  Sekel  :  >>  ägypt-aram.  [ilr.
akk.  girü,  ein  Unterteil  (V24)  des  Sekel  :  >-  wohl  liebr.  gerä  i/,o Sekel.
Ob  etwa  auch  das  Wort  für  Talent,  hebr.  hiMär,  phön.  hkr,  aram. kakharä  (ägypt. -aram.  knJcr)  (]>  armen.  ¥ank'ar),  südarab.  Jcrkr,  griech. xiyxccQ-eg  (Josephus),  auf  ein  alck.  *kaJckaru  zurückgeht,  ist  noch  unsicher. -
[Ob  griech.  Sagstxög  (Bez.  für  eine  persische  Goldmünze),  hebr. 'ädarkön,  später  darkön,  syr.  dsrikönci,  auf  eine  babyl.  Vorlage,  etwa  ein akk.  dariku^  zurückgeht,  ist  sehr  fraglich.  Das  Wort  ist  vielmehr  wohl pers.  Ursprungs,  hat  aber  andererseits  auch  nichts  mit
```


## [2026-09-07T15:53:42.115Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mina, n\\. a\\|mina, n\\.\\|mna\\b\" KLN_1966.txt | head -20; echo \"=== manA ===\"; grep -n \"man[aā]h*, *n\\.\\|Akkau*d\\. man\" KLN_1966.txt | head -20",
 "description": "Klein mina entry"
}
```


### [2026-09-07T15:53:42.185Z] TOOL RESULT

```
2908:antenati,  n.  pi.,  persons  born  before  a  certain event  (law).  —  Formed  fr.  ante-  and  L.  ndti,  pi. of  natus,  ‘born’.  See  prec.  word, antenna,  n.  —  ModL.,  feeler  or  horn  of  an  in¬ sect',  fr.  L.  antemna,  antenna,  ‘sail  yard’ .which  is of  uncertain  origin.  It  is  perh.  a  contraction  of *an(a)tempna,  ‘that  which  is  stretched,  extend¬ ed',  fr.  l.-E.  base  *temp-,  ‘to  stretch,  extend’.  See temple,  ‘place  of  worship’,  and  cp.  next  word. Derivative:  antenn-al,  adj.
8297:columella,  n.,  a  part  resembling  a  column  (anal., zool.  and  bot.)  —  L.,  dimin.  of  columna.  See next  word  and  -ella.
8298:column,  n.  —  L.  columna,  ‘pillar,  column’,  prob. standing  for  *qelom(e)na,  ‘that  which  rises’, fern,  passive  part,  formed  fr.  I.-E.  base  *qel-,  ‘to rise,  be  elevated',  whence  also  columen,  culmen, ‘top,  summit,  gable’,  ce/ms, ‘high,  lofty ,  elevated’, excellere,  ‘to  rise,  excel’,  collis  (iot*col-n-is),  ‘a
8299:hill’,  OI.  kiitam  (for  kultarri),  ‘top,  skull’  (orig. ‘elevation’),  Gk.  xoXrovoi;,  xoXcivT),  ‘hill’,  xo- Xocpcbv,  ‘top,  end',  Lith.  kdlnas,  Lett,  kalns, ‘mountain’,  Lith.  kalva,  Lett,  kalva,  ‘hill’,  Lith. keliu,  kelti,  Lett,  celu,  celt,  ‘to  raise,  lift’,  OSlav. celo,  ‘forehead’,  celesinu,  ‘particular,  peculiar’. OS.  holm,  ‘hill’,  OE.  holm,  ‘island,  wave,  sea’. Cp.  hill,  holm.  Cp.  also  colliculus,  colline, colonel,  colonnade,  colophon,  culminate,  excel. For  the  participial  suff.  in  L.  columna  (for *qelo-mend)  see  alumnus  and  cp.  words  there referred  to.
8300:Derivatives:  columnar  (q.v.),  column-ed,  adj. columnar,  adj.,  formed  in  columns.  —  L.  colum- naris,  ‘rising  in  the  form  of  a  pillar’,  fr.  columna. See  prec.  word  and  -ar. columniform,  adj.  —  See  column  and  -form, colure,  n.,  one  of  the  two  celestial  circles  intersect¬ ing  each  other  at  the  poles  ( astron .)  —  Late  L. coluri  (pL),  fr.  Gk.  al  xoXoupot  (scil.  ypanpou), ‘the  colures’,  lit.  ‘the  truncated  (lines)’,  pi.  of xoXo’jpo;,  ‘dock-tailed’,  which  is  compounded of  xoXo?,  ‘docked,  mutilated,  curtailed’,  and oupd,  ‘tail’  (see  colobium  and  uro-,  ‘tail-’);  so called  because  in  Greece  their  lower  part  is always  ‘cut  off’  (i.e.  beneath  the  horizon). Colutea,  n.,  a  genus  of  plants  of  the  pea  family (hot.)  —  ModL.,  fr.  Gk.  xoXouteS,  xoXoit££, xoXcoTed,  name  of  a  tree.
9895:crown’,  fr.  L.  culmen,  gen.  culminis,  contracted form  of  columen,  gen.  columinis,  ‘the  top  of  an object,  summit’,  which  is  rel.  to  columna,  ‘pillar, column’.  See  column  and  verbal  suff.  -ate  and cp.  hill.
17798:Hildegard(e),  fem.  PN.  —  OHG.  Hildegard,  lit. ‘protecting  battle  maid’,  compounded  of  hildi, ‘war,  battle’,  and  *gard,  ‘to  enclose,  protect’. For  the  first  element  see  Hilda,  for  the  second see  yard,  ‘enclosure’,  and  cp.  garden, hilding,  n.,  a  base  wretch;  adj.  base  (archaic).  — • Formed  with  suff.  -tag  fr.  OE.  hyldan,  heldan, ‘to  lean,  incline,  bend  down’.  See  heel,  ‘to  lean’, hill,  n.  —  ME.  hil,  hut,  hull,  fr.  OE.  hyll,  rel.  to MDu.  hille,  LG.  hull,  ‘hill’,  ON.  hallr,  ‘stone’, Goth,  hallus,  ‘rock’,  ON.  holmr,  OE.  holm, ‘rising  land,  island’,  fr.  I.-E.  base  *qel-,  ‘to  rise, be  elevated’,  whence  also  OI.  kiitam  (for  kul- tam),  ‘top,  skull’  (orig.  ‘elevation’),  Gk.  xoXo>v6?, xo Xd>v7),  L.  collis,  ‘hill’,  columen,  ‘top’,  columna, ‘column’.  See  column  and  cp.  holm.  Cp.  also hillock.
18098:horripilation,  n.,  bristling  of  the  hair.  —  L.  horri- pilatio,  gen.  -dnis,  fr.  horripilat  {-um),  pp.  stem of  horripilare.  See  prec.  word  and  -ion. horror,  n.  —  ME.  honour,  fr.  OF.  orror,  horror, horrour  (F.  horreur),  fr.  L.  horrorem,  acc.  of horror,  ‘bristling,  roughness,  rudeness,  shaking, trembling’,  fr.  horrere,  ‘to  stand  on  end,  bristle, shake,  shudder,  shiver,  tremble’,  fr.  I.-E.  base *ghers-,  ‘to  bristle’,  whence  also  L.  hirsutus, ‘shaggy,  prickly,  bristly’,  OI.  hdrsate,  hfsyati, ‘bristles’,  Avestic  zarshayamna-,  ‘ruffling  one’s feathers’.  Base  *ghers-  is  an  enlarged  form  of base  *gher-,  which  appears  in  Gk.  xhP>  gen. X'r)p6<;,  L.  er  (for  *hers),  gen.  eris,  ‘hedgehog’, lit.  ‘the  prickly  creature’.  See  urchin  and  cp. Chersonese,  -choerus,  hideous,  hircine,  hirsute, hispid,  Hordeum  and  the  second  element  in Hypochaeris.  Cp.  also  hearse, horror-stricken,  horror-struck,  adj.  —  Compound¬ ed  of  horror  and  the  pp.  of  strike, hors  de  combat,  out  of  the  combat;  disabled.  —
19647:intercolumniation,  n.,  the  space  between  two columns  (archil.)  —  Formed  with  suff.  -ation fr.  L.  intercolumnium,  ‘the  space  between  two columns’,  fr.  inter-  and  columna.  See  column, intercourse,  n.  —  ME.  intercurse,  fr.  OF.  entre- cours,  ‘exchange,  commerce’,  fr.  Late  L.  inter- cursus  (gen.  -us),  ‘a  running  between  or  amongst’, fr.  L.  intercursus,  pp.  of  intercurrere,  ‘to  run  be¬ tween  or  amongst’,  fr.  inter-  and  currere,  ‘to run’  (see  current,  adj.);  remodeled  after  L. intercursus.
21446:Lemna,  n.,  a  genus  of  plants,  the  duckweed  (bot.)
21449:Lemnaceae,  n.  pi.,  the  duckweed  family  (bot.)  — Formed  fr.  Lemna  with  suff.  -aceae. lemnaceous,  adj.  —  See  prec.  word  and  -aceous. lemniscate,  n.  (geom.)  —  Late  L.  lemniscatus, ‘adorned  with  ribbons’,  fr.  lemniscus,  ‘ribbon’, fr.  Gk.  Xr^vtaxo?,  of  s.m.  See  next  word  and adj.  suff.  -ate.
33624:‘the  same’,  rel.  to  OE.  same,  adv.  (in  same  swa, ‘similarly’,  swa  same  swa,  ‘just  as’),  OS.  sama, samo,  OHG.  sama,  adj.  and  adv.,  Goth,  sama, adj.,  OHG.  samant,  MHG.  sament,  samt, ‘together’,  G.  samt,  ‘together  with’,  Goth. samana,  ‘together’,  OE.  samnian,  OS.  samnon, ON.  samna,  OFris.  samnia,  MLG.,  MDu. samenen,  OHG.  samanon,  MLG.,  MHG.  sa- melen,  G.  sammeln,  Du.  tamelen,  ‘to  collect’, lit.  ‘to  bring  together',  OE.  tosamne,  OS.  te- samne,  OFris.  tosamene,  Du.  tezamen,  OHG.  zi- samane,  MHG.  zesamene,  G.  zusammen, ‘together’,  fr.  I.-E.  base  *sem-,  *sm-,  ‘one, together’,  whence  also  OI.  samah,  ‘even,  level, similar,  equal,  the  same,  identical’,  Avestic hama,  ‘similar,  the  same’,  OI.  samam,  ‘together’, sa-k(t,  Avestic  ha-k^r^t,  ‘at  once,  once’,  OI.  sel¬ dom,  Avestic  ha-da,  ‘always’,  OI.  sa-,  Avestic ha-,  OI.  sam-,  Avestic  ham,  ‘with’,  Toch.  A Soma,  B.  fomo,  ‘the  same,  similar’,  B.  fe-me,  A fas,  ‘one’,  Gk.  &\io,  ‘together  with,  at  the  same time  with’,  ojjio?,  ‘one  and  the  same’,  opoio? (Old  Att.  6p.oio?),  ‘like,  resembling’,  ouou, ‘together’,  6|xaX6q,  ‘even’,  el?  (for  *ep.-?,  I-E. *sem-s),  neut.  (for  *£(*,  I--E-  *sem-),  fern, piia  (for  I.-E.  *sm-iye),  ‘one’,  L.  semel,
=== manA ===
```


## [2026-09-07T15:53:48.000Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mina,\\|maneh\\|Heb.  m[aā]neh\\|μνᾶ\\|mna,\" KLN_1966.txt | head -20; echo \"=== 1971 ===\"; grep -n \"mina,\\|maneh\" KLN_1971.txt | head -20",
 "description": "Klein mina search"
}
```


### [2026-09-07T15:53:48.073Z] TOOL RESULT

```
2145:ale,  n.  —  OE.  ealo,  alo,  rel.  to  ON.  67,  and  cogn. with  L.  alumen,  ‘alum’,  fr.  I.-E.  base  *alu-, ‘bitter’.  OPruss.  alu,  ‘mead’,  Lith.  aids,  OSlav, old,  ‘beer’,  are  Teut.  loan  words.  Cp.  alum, alumina,  aluta,  alutaceous. aleatory,  adj.,  depending  on  chance.  L.  dlea- tdrius,  ‘pertaining  to  a  gamester’,  fr.  alea,  ‘die, game  of  hazard’,  prob.  meaning  orig.  ‘mere chance',  and  derived  fr.  Gk.  iXsoq,  a  collateral form  of  vjXeo^,  ‘wandering  in  mind,  distraught, foolish’.  See  Aleochara  and  the  adj.  suffixes  -ate and  -ory.
2374:alum,  n.  —  OF.  alum  (whence  F.  alun),  fr.  L. alumen,  ‘alum’,  lit.  ‘bitter  salt’,  cogn.  with  Gk. aXuSoLjiot;,  ‘bitter’,  OE.  ealo,  alo,  ‘ale’,  ON. 61,  of  s.m.  See  ale  and  cp.  alumina,  aluta,  alu- taceous.
2375:Derivative:  alum,  tr.  v. atumin-,  form  of  alumino-  before  a  vowel, alumina,  n.,  aluminum  oxide  ( chem .)  —  Fr.  L.
2450:ambush,  n.  —  OF.  embusche  (F.  embuche),  back formation  fr.  embuscher.  See  prec.  word, arnbushment,  n.  —  OF.  embuschement,  fr.  em¬ buscher.  See  ambush,  v.,  and  -ment. ameen, n,,  official,  inspector  (Anglo-Ind.)  — Hind. amin,  fr.  Arab,  amtn,  lit.  ‘trustworthy’,  fr.  amina, ‘he  was  steady,  firm,  trustworthy’  (whence  A'ma- na,  ‘he  believed’);  rel.  to  Heb.  amen,  ‘verily, truly’.  See  amen.
2455:amellus,  n.,  name  of  a  flower.  —  L.,  ‘the  purple Italian  starwort',  a  word  of  Gaulish  origin  (see G.-D.Dottin,  La  langue  gauloise,  p.226).  The derivation  of  this  word  from  the  river  name Mella,  as  suggested  by  Servius  in  his  commen¬ tary  on  Virgil  4,  271,  is  folk  etymology, amen,  interj.,  n.,  adv.  and  tr.  v.  —  OE.,  fr.  Eccles. L.  amen,  fr.  Eccles.  Gk.  ap.7)v,  fr.  Heb.  amen, ‘verily,  truly,  certainly’,  from  stem  a-m-n,  ‘to  be trustworthy,  confirm,  support’,  whence  also aman,  ‘he  supported,  nourished’,  heemln,  ‘be believed’,  emundh,  ‘firmness,  fidelity’,  umndm , omndm,  ‘verily,  truly,  emith  (for  *ementh),  sta¬ bility,  truth’.  Cp.  the  related  Syr.  ammin,  ‘strong, enduring’,  Aram,  hemanuthd,  Syr.  haymanuthd, ‘faithfulness,  truth’,  Arab,  dmina,  ‘he  was  safe’.
2908:antenati,  n.  pi.,  persons  born  before  a  certain event  (law).  —  Formed  fr.  ante-  and  L.  ndti,  pi. of  natus,  ‘born’.  See  prec.  word, antenna,  n.  —  ModL.,  feeler  or  horn  of  an  in¬ sect',  fr.  L.  antemna,  antenna,  ‘sail  yard’ .which  is of  uncertain  origin.  It  is  perh.  a  contraction  of *an(a)tempna,  ‘that  which  is  stretched,  extend¬ ed',  fr.  l.-E.  base  *temp-,  ‘to  stretch,  extend’.  See temple,  ‘place  of  worship’,  and  cp.  next  word. Derivative:  antenn-al,  adj.
3625:Asimina,  n.,  a  genus  of  trees,  the  North  American papaw  (bot l)  —  ModL.,  fr.  Can.  F.  assiminier , ‘papaw  tree’,  fr.  Illinois  Indian  rassimina. asinego,  n.,  a  little  ass,  a  fool.  Sp.  asnico,  di- min.  of  asno,  ‘an  ass’,  fr.  L.  asinus,  of  s.m.  See next  word.
6126:calamary,  n.,  squid.  —  L.  calamdrius,  ‘pertaining to  a  pen’,  fr.  calamus,  ‘reed,  pen’,  fr.  Gk.  y.diXa- p.0?,  prob.  an  assimilated  form  of  orig.  *x9X:x- jioc,  and,  accordingly,  cognate  with  L.  culmus, ‘stock,  stem’.  See  culm,  ‘stem  of  grasses’,  and cp.  words  there  referred  to.  Cp.  also  the  first element  in  calamint,  caramel, calamine,  n.,  a  kind  of  zinc  ore.  —  F.,  fr.  ML. calamina,  fr.  L.  cadmia,  fr.  Gk.  xxSfrsia,  ‘cala¬ mine’,  fr.  KiSixo;,  ‘Cadmus’,  the  founder  of Thebes ;  so  called  because  this  mineral  was  found first  in  the  vicinity  of  Thebes.  See  Cadmus, cadmium.
6523:Cardamine,  n.,  a  genus  of  plants  of  the  mustard family  (hot.)  —  ModL.,  fr.  L.  cardamina,  fr.  Gk. xxpSxaivr,,  ‘a  kind  of  cress',  a  word  formed  by Dioseorides  fr.  xxpSxpov,  ‘cress",  which  is  of  un¬ certain  origin.  Cp.  next  word, cardamom,  cardamum,  n.,  an  aromatic  fruit.  — F.  cardamome,  fr.  L.  cardamomum,  fr.  Gk.  xxp- Sipcaizov,  which  is  compounded  of  xxp8x|iZ)V, ‘cress’,  and  xpeopov,  ‘a  spice  plant'.  See  Carda¬ mine  and  Amomus.  The  contraction  of  the  two elements  into  xap8xu.cju.ov  from  *xxp8xux:j.o>- t xov  is  due  to  haplology.
8298:column,  n.  —  L.  columna,  ‘pillar,  column’,  prob. standing  for  *qelom(e)na,  ‘that  which  rises’, fern,  passive  part,  formed  fr.  I.-E.  base  *qel-,  ‘to rise,  be  elevated',  whence  also  columen,  culmen, ‘top,  summit,  gable’,  ce/ms, ‘high,  lofty ,  elevated’, excellere,  ‘to  rise,  excel’,  collis  (iot*col-n-is),  ‘a
9785:Derivative:  crumbl-y,  adj. crumen,  n.,  the  name  of  the  suborbital  gland  in deer  and  antelopes.  —  L.  crumina,  crumena, ‘purse,  bag’,  fr.  Gk.  ypOpiea,  ypupieia.  See  crumb, crump,  tr.  and  intr.  v.,  to  crunch.  —  Of  imitative origin.
9895:crown’,  fr.  L.  culmen,  gen.  culminis,  contracted form  of  columen,  gen.  columinis,  ‘the  top  of  an object,  summit’,  which  is  rel.  to  columna,  ‘pillar, column’.  See  column  and  verbal  suff.  -ate  and cp.  hill.
10276:dame,  n.,  a  noble  lady.  —  ME.  dame,  tr.  OF. (=  F.)  dame,  fr.  L.  domina,  ‘the  mistress  of  a household’,  fern,  of  dominus,  ‘lord’,  prop,  ‘own¬ er  of  the  house’,  and  rel.  to  domus,  ‘house’.  For the  form  cp.  tribunus,  fr.  tribus,  ‘tribe’.  Dominus is  only  indirectly  rel.  to  domare,  ‘to  tame’  (see dome  and  cp.  dominate);  but  was  directly  in¬ fluenced  in  meaning  by  it.  See  Walde-Pokorny,
10288:damsel,  n.,  a  girl.  —  ME.  dameisele,  fr.  OF.  da- meisele,  damoiselle,  ‘a  woman  of  noble  birth’ (whence  F.  demoiselle,  ‘young  lady’),  fr.  VL. *dominicella,  dimin.  of  L.  domina,  ‘mistress’ (see  dame),  fern,  of  dominus,  ‘master,  lord’.  See dominus,  dome,  ‘building’,  and  cp.  damoiseau, demoiselle,  doncella,  donzella,  mademoiselle.  For the  ending  see  suff.  -el.
10794:Derivatives:  demograph-ic,  demograph-ic-al, adjs.,  demograph-ic-al-Iy,  adv.,  demograph-ist,  n. demoiselle,  n.,  1)  a  damsel  (archaic);  2)  a  small crane  of  N.  Africa;  the  Numidian  crane.  —  F. fr.  OF.  dameiselle,  damoiselle,  fr.  VL.  *domini- cella,  dimin.  of  domina,  ‘mistress,  lady’,  fern, of  L.  dominus,  ‘lord’,  fr.  domus,  ‘house’.  See dome  and  cp.  dame.  Cp.  also  damsel,  damoiseau, doncella,  donzella ;  cp.  also  Don. demolish,  tr.  v.  —  Fr.  OF.  demoliss-,  pres.  part, stem  of  demolir  (F.  demolir),  ‘to  pull  down, overthrow,  destroy,  demolish’,  fr.  L.  demdiiri, ‘to  throw  or  pull  down,  overthrow,  demolish’, fr.  de-  and  moliri,  ‘to  construct’,  fr.  moles,  ‘mass, heap’.  See  mole,  ‘mound’,  and  verbal  suff.  -ish. Derivatives:  demolish-er,  n.,  demotish-ment,  n. demolition,  n.  —  F.  demolition,  fr.  L.  demdlitio- nem,  acc.  of  demdlitio,  ‘a  pulling  down’,  fr.  de- molitus,  pp.  of  demoliri.  See  prec.  word  and  -ion. demon,  n.  —  L.  daemon,  ‘a  spirit’,  in  Eccles.  L. ‘an  evil  spirit’,  fr.  Gk.  Saipttov,  ‘god,  goddess’, lit.  ‘a  divider,  distributor  (of  men’s  destinies)’, which  is  rel.  to  Saleoflat,  ‘to  divide,  distribute; to  feed  on’,  Sodq,  Sxlxq,  Soaxuq,  ‘meal,  ban¬ quet’,  Saivuvat,  ‘to  give  a  banquet  or  feast’, Sat^eiv,  ‘to  cleave  asunder,  rend,  divide’,  Sijjjtoq, ‘district,  country,  land,  people’,  fr.  I.-E.  base *da-,  *dai-,  *dl-,  *de-,  ‘to  cut  off,  separate,  di¬ vide,  distribute’,  whence  also  OE.  tid,  ‘time’, tima,  ‘time,  date’,  prop,  ‘division  of  time’.  See tide  and  cp.  demagogue,  deme,  democracy,  de¬ mos.  Cp.  also  eudaemonic,  pandemonium,  geo¬ desy.  Cp.  also  dah.  For  a  derivative  of  *df-t-, a  -/-enlargement  of  base  *de-,  see  datolite. demon-,  form  of  demono-  before  a  vowel, demonetization,  n.  —  F.  demonetisation,  fr.  de- monetiser.  See  next  word  and  -ation. demonetize,  tr.  v.,  to  deprive  of  monetary  value. —  F.  demonetiser,  fr.  de-  (used  in  the  privative sense  of  this  prefix),  and  monetiser.  See  de-  and monetize.
12063:Dona,  n.,  a  Spanish  title  given  to  a  married woman.  —  Sp.,  ‘lady,  madam’,  fr.  L.  domina, ‘mistress’,  fern,  of  dominus,  ‘master,  lord’.  See dominus  and  cp.  dame  and  words  there  re¬ ferred  to.
12069:doncella,  n.,  1)  a  wrasslike  fish:  2)  name  of timber  trees  in  W.  Indies.  —  Sp.,  lit.  ‘damsel’, fr.  VL.  *dominicella,  dimin.  of  L.  domina,  ‘mis¬ tress’.  See  damsel  and  cp.  words  there  referred to.
12076:donzel,  n.,  squire,  page  (archaic).  —  It.  donzello, fr.  VL.  *dominicello,  dimin.  of  L.  dominus, ‘master,  lord’.  See  damoiseau  and  cp.  next  word, donzella,  n.,  damsel.  —  It.,  fr.  VL.  *dominicella, dimin.  of  L.  domina,  ‘mistress’.  See  doncella.
12380:Derivative:  duellist-ic,  adj. duenna,  n.,  an  elderly  woman;  a  chaperon.  — Sp.  dueha,  fr.  L.  domina,  ‘mistress*.  See  dame, duet,  n.  —  F.,  fr.  It.  duetto,  ‘duet’,  dimin.  of  due, ‘two’,  fr.  L.  duo\  see  duo  and  -et  and  cp.  tercet, quartet,  quintet,  sextet.
12684:effeminate,  adj.  —  L.  effemindtus,  ‘womanish, effeminate’,  pp.  of  effeminare,  ‘to  make  woman¬ ish,  to  enervate’,  formed  fr.  ist  ex-  and  femina, ‘woman’.  See  feminine  and  verbal  suff.  -ate. Derivatives:  effeminate,  n.,  effeminate-ly,  adv., effeminate-ness,  n.
=== 1971 ===
10737:alumina, aluta, alutaceous. 
12417:61 , of s.m. See ale and cp. alumina, aluta, alu- 
12422:alumina, n., aluminum oxide ( chem .) — Fr. L. 
12444:med. and pass, part., and L. fe-mina, ‘woman’, 
12981:amin , fr. Arab, am In, lit. ‘trustworthy*, fr. amina, 
13037:‘faithfulness, truth’, Arab, amina, ‘he was safe’, 
20766:Asimina, n., a genus of trees, the North American 
36937:calamina, fr. L. cadmia, fr. Gk. xa$(zeux, ‘cala- 
39639:family (bot.) — ModL., fr. L. cardamina, fr. Gk. 
63832:( = F.) dame , fr. L. domina, ‘the mistress of a 
63937:*dominicella , dimin. of L. domina, ‘mistress’ 
67443:cella , dimin. of domina, ‘mistress, lady’, fem. 
75367:fr. VL. *dominicella, dimin. of L. domina, ‘mis- 
75410:dimin. of L. domina, ‘mistress’. See doncella. 
79340:ish, to enervate*, formed fr. 1st ex- and femina, 
91227:fe-ldre, ‘to suck’, fe-mina, ‘a woman’, fi-lius , 
91580:L. femella, dimin. of femina, ‘woman; female 
91607:femininus , ‘feminine’, fr. femina, ‘woman’, orig. 
91622:nine. — OF. feminite , fr. L. femina, ‘woman’. 
91627:femina, ‘woman* (see feminine), and -ize, a suff.
```


## [2026-09-07T15:53:55.529Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^mina\\|  mina  \\|mine,  n\\.,  a  weight\\|Akkad\\.  man\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== macron/macro ===\"; grep -n \"macron,\\|macro-,\\|meager,\\|meagre,\\|Macedonia\" KLN_1966.txt | head -10",
 "description": "Klein mina/macron search"
}
```


### [2026-09-07T15:53:55.629Z] TOOL RESULT

```
KLN_1971.txt:55367:minalis , fr. L. conterminus. See next word and 
KLN_1971.txt:59931:minate. There is no connection between L. 
KLN_1971.txt:59941:minalist, n., criminality (q.v.) 
KLN_1971.txt:67841:mination), fr. L. denominationem, acc. of denomi- 
KLN_1971.txt:67848:minalion-al-ize, tr. v. 
KLN_1971.txt:67852:minate and -ive. 
KLN_1971.txt:68925:minate’, fr. de- and sinere, ‘to set down; to 
KLN_1971.txt:69429:minative), fr. L. determinate , pp. of determi- 
KLN_1971.txt:72844:minans, gen. -antis, pres. part, of discriminare. 
KLN_1971.txt:92195:mina, ‘a woman’, lit., ‘she who suckles \fe-ldre, 
KLN_1971.txt:122407:minabilis. See determinable. 
KLN_1971.txt:122410:minabl-y, adv. 
KLN_1971.txt:128723:minated fr. yashQr ~ ydshdr, ‘straight, right, 
KLN_1971.txt:132098:minata. See kola. 
KLN_1971.txt:141224:minate. 
KLN_1971.txt:141503:minate’, fr. L. lustrare, ‘to light, illuminate’. See 
KLN_1971.txt:141534:mination’, fr. I.-E. base *leuq-, ‘to emit light, to 
KLN_1971.txt:141538:mination, inspection, review, mustering, expia- 
KLN_1971.txt:144248:minatory. Cp. also moniliform. 
KLN_1971.txt:151789:mina, n., an ancient unit of weight and money. — 
=== macron/macro ===
4783:Berenice,  fern.  PN.  —  L.  Berenice,  fr.  Bepevfx-q, Macedonian  var.  of  Gk.  <J>Epevfx7j,  lit.  ‘bringer of  victory’,  fr.  tpepeiv,  ‘to  bring’,  and  vfxv), ‘victory’.  See  bear,  ‘to  carry’,  and  Nike,  and  cp. Veronica.  Cp.  also  varnish.
14045:exilian,  exilic,  adj.,  pertaining  to  the  exile  of  the Jews  in  Babylonia,  —  Formed  with  suff.  -ian, resp.  -ic,  fr.  L.  exilium.  See  exile,  ‘banishment’, exility,  n.,  slenderness.  —  L.  exilitas,  ‘smallness, thinness,  meagemess,  slenderness’,  fr.  extlis, ‘small,  thin,  meager,  slender’,  which  prob. stands  for  *ex-bg-slis  and  is  rel.  to  exiguus, ‘small,  scanty,  petty’.  See  exiguous  and  -ity. eximious,  adj.,  choice,  excellent.  —  L.  eximius , ‘select,  choice’,  lit.  ‘taken  out’,  fr.  eximere,  ‘to take  out,  take  away’,  fr.  ist  ex-  and  emere,  ‘to take,  buy’.  See  exempt,  v.  For  E.  -ous,  as equivalent  to  L.  -us,  see  suff.  -ous.
22446:Derivative;  mace,  tr.  v.,  to  strike  with  a  mace, mace,  n.,  a  spice  consisting  of  the  dried  outer covering  of  nutmeg.  —  ME.  macis,  fr.  F.  macis, fr.  Late  L.  macis,  which  is  prob.  a  scribal  error for  L.  macir,  ‘red  bark  of  an  Indian  root’,  fr.  Gk. paxip,  a  word  of  uncertain  origin.  The  -s  in  F. macis  was  mistaken  for  the  plural  suff.  and  ac¬ cordingly  dropped  in  English, mace,  n.,  swindling;  tr.  and  intr.  v.,  to  swindle (slang).  —  Of  uncertain  origin, macedoine,  n.,  a  dish  of  fruit  or  vegetables  em¬ bedded  in  jelly.  —  F.,  fr.  Macedoine,  fr.  L.  Ma¬ cedonia,  fr.  Macedones,  ‘the  Macedonians’,  fr. Gk.  MaxeSovec,  of  s.m. ;  so  called  facetiously  in allusion  to  the  medley  of  nations  of  different origin  by  which  Macedonia  was  inhabited.  See next  word.
22447:Macedonian,  adj.  and  n.  —  Formed  with  suff.  -an fr.  L.  Macedonius,  fr.  Gk.  MxxeSovioc,  ‘Mace¬ donian’,  fr.  MaxcSovs?,  ‘the  Macedonians’,  lit. ‘the  Highlanders’,  or  ‘the  Tall  Ones’,  rel.  to |tax£Sv6s,  ‘long,  tali’,  and  to  [taxp6?,  ‘long, large'.  See  macro-.
22473:macr-,  form  of  macro-  before  a  vowel. macram£,  n.,  a  kind  of  ornamental  work  embroi¬ dered  into  knots.  —  Turk,  maqrama,  ‘handker¬ chief’,  fr.  Arab.  mlqramJ',  ‘embroidered  veil’, macro-,  before  a  vowel  macr-,  combining  form meaning  ‘long’.  —  Gk.  p.axpo-,  pootp-,  fr.  pa- xpoc,  ‘long,  large’,  cogn.  with  L.  macer,  ‘lean, thin’,  ON.  magr,  OE.  mzger,  ‘lean,_thin’,^fr. I.-E.  *mikrds,  derivative  of  base  *mdk-,  *m  k-, ‘long,  thin’,  whence  also  Gk.  [itjxo?,  length  , juaxE-Sv-oc,  ‘long,  tali’.  See  meager  and  cp. Macedonian,  meco-.
22478:macrocosm,  n.,  the  great  world,  the  universe.  — F.  macrocosme,  compounded  of  macro-  and  Gk. xoap.o<;,  ‘world’.  See  cosmos  and  cp.  microcosm, macron,  n.,  a  short  horizontal  line  placed  over  a vowel  to  indicate  its  length.  —  Gk.  paxpov, neut.  of  tj.ay.p6q,  ‘long’.  See  macro-, macroscopic,  also  macroscopical,  adj.,  large enough  to  be  seen  by  the  naked  eye.  —  Com¬ pounded  of  macro-  and  Gk.  axomriv,  ‘to  look at,  examine’  (see  -scope),  and  sulf.  -ic,  resp.  also -al.  Cp.  microscope.
22959:marjoram,  n.,  name  of  a  plant.  —  ME.  majoran, fr.  OF.  majorane  (F.  marjolaine),  tr.  ML.  majo- rana,  fr.  L.  amaracus,  fr.  Gk.  apapaxo;,  ‘mar¬ joram’,  which,  together  with  Macedonian  Gk. afixpu,  ’marjoram',  prob.  derives  from  a  lan¬ guage  of  India.  Cp.  OI.  maruvah,  maruvakah, ‘marjoram’. ML.  majorana  (fr.  L.  amaracus)  owes its  form  to  a  confusion  with  L.  major,  contpar. of  magmis,  ‘great,  large’  (see  major,  adj.) Marjorie,  Marjory,  fern.  PN.  —  Collateral  forms of  Margery  (q.v.)
23229:Derivative:  meadow-y,  adj. meager,  meagre,  adj.  —  ME.  megre,  fr.  OF. maigre,  magre,  megre  (F.  maigre),  fr.  L.  macer, ‘lean,  thin’,  which  is  cogn.  with  Gk.  paxp6?, ‘long’,  OE.  mseger,  ON.  magr,  MDu.  magher, Du  mager,  OHG.  magar,  MHG.,  G.  mager, ‘lean,  thin’,  fr.  I.-E.  base  *mlkrds,  a  derivative of  base  *mdk;  *msk-,  ‘long,  thin’,  whence  also Avestic  mas-,  ‘long’,  masah-,  ‘length,  size’.  Cp. als0 — with  /-sutf. — Hitt,  maklanza,  ‘thin,  mea¬ ger’.  Cp.  emaciate,  Macedonian,  macro-,  maigre, malinger,  meco-.
26227:Olympiad,  n.,  a  period  of  four  years,  reckoned from  one  celebration  of  the  Olympic  games  to the  next;  used  by  the  ancient  Greeks  in  com¬ puting  time.  —  F.  olympiade,  fr.  L.  Olympiadem, gen.  Olympiads,  fr.  Gk.  ’OXuuTuac,  gen. ’OXupmuxSo?,  fr.  ’OXupmiS  (scil.  X“P“),  a  dis¬ trict  in  Elis  in  ancient  Greece,  where  theOlympic games  were  held,  prop.  fem.  of  the  adj.  ’OXup- 7uo<;,  ‘Olympian’.  See  next  word  and  -ad. Olympian,  adj.,  1)  pertaining  to  Mount  Olympus in  Macedonia;  2)  heavenly;  godlike;  3)  per¬ taining  to  Olympia  in  Elis  in  ancient  Greece, where  the  Olympian  games  were  held ;  4)  desig¬ nating  the  Olympian  games.  —  Late  L.  Olym- pidnus,  Olympias,  fr.  Gk.  ’  OXOp— 10c ,  ‘pertain¬ ing  to  Olympus  or  Olympia',  fr.  "OXupTrop.  See Olympus  and  cp.  Olympic.
26231:Olympus,  n.,  a  mountain  in  Macedonia,  the fabled  dwelling  place  of  the  twelve  great  gods  of ancient  Greece.  —  L.,  fr.  Gk.  "Okounoc,  which is  of  unknown  etymology, om-,  form  of  omo-  before  a  vowel.
```


## [2026-09-07T15:54:06.019Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '151780,151805p' KLN_1971.txt; echo \"=== mine (weight) ===\"; grep -n \"mine, n., a weight\\|mine , n\\.\" KLN_1971.txt | head",
 "description": "Klein mina entry 1971"
}
```


### [2026-09-07T15:54:06.103Z] TOOL RESULT

```
Mimus, n., a genus of birds, the mockingbird 
(ornithol.) — L. mimus, ‘mime’. See mime. 
Mimusops, n., a genus of tropical trees of the 
sapodilla family (bot.) — ModL., compounded 
of Gk. ;jup.d>, gen. pupLous, ‘ape’ (fr. (jujaos, 
‘imitator’), and gen. dmo?, ‘face’. See mime 
and -ops. 

mina, n., an ancient unit of weight and money. — 
L., fr. Gk. pLva, which is of Sem. origin. Cp. 
Akkad, manu (fr. Sumer, mana) and Heb. 
mand h , Bi >lical Aram. m g #e(Dan. 5 : 25), Aram.- 
Syr. manya (whence Arab, manan), Ugar. mn, 
which are borrowed fr. Akkad, manu. Cp. mine, 
‘unit of weight’. Cp. also maund, ‘unit of weight’, 
mina, n., a myna. — See myna. 

Mina, fern PN. — Shortened fr. Wilhelmina. 
minacious, cidj., threatening. — Formed with suff. 
-ous fr. L. mindx, gen. -dcis, ‘threatening’, fr. 
minari, ‘to threaten’. See minatory. 

Minaean, adj. — Formed with suff. -an fr. L. 
Minaei (pi.), a people in South Arabia, fr. Gk. 
Mivatoi, fr. Arab. Ma'dn; they are mentioned 
=== mine (weight) ===
```


## [2026-09-07T15:54:16.581Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"maund\" KLN_1971.txt | head; echo ---; grep -n \"maund\" KLN_1966.txt | head",
 "description": "Klein maund entry"
}
```


### [2026-09-07T15:54:16.646Z] TOOL RESULT

```
101980:(bot.) — ME. germaunder , fr. OF. germandree , 
129367:jardyne almaunde , lit. ‘garden almond’, fr. OF. 
143962:man, n., a unit of weight. — See maund. 
144141:commend, countermand, demand, maundy, re- 
146880:maund, also man, n., a unit of weight used in India, 
146884:maund, n., a hand basket. — ME. maund fr. MF. 
146888:maund, tr. and intr. v., to beg {slang). — Prob. fr. 
146893:maunder, intr. v., 1) to wander about aimlessly; 
146894:2) to mutter, mumble. — Prob. freq. of maund, 
146897:Derivative: maunder-er , n. 
---
16058:Derivatives:  Germanic  (q.v.),  German-ism,  n., German-ist,  n. ,  German-ist-ic,  ad}.,German-ize,  tr. and  intr.  v.,  German-iz-ation,  n.,German-iz-er,n. germander,  n.,  any  plant  of  the  genus  Teucrium ( bot .)  —  ME.  germaunder,  fr.  OF.  germandree, fr.  ML.  germandra,  fr.  earlier  gamandria,  fr. MGk.  /ajxavSpudt,  fr.  Gk.  yap.al8pu?,  ‘german¬ der’,  lit.  ‘tree  on  the  ground’,  fr.  xapuxt,  ‘on  the ground’,  and  8p5 q,  ‘oak  tree,  tree’.  See  chamae- and  dryad.
20369:Jordan  almond,  n.  —  Transformation  of  ME. jardyne  almaunde,  lit.  ‘garden  almond  ,  fr.  OF. jardin ,  ‘garden’,  and  almande,  ‘almond  ;  see jardiniere  and  almond.  The  change  of  ME.  jar- dyne  to  Jordan  is  due  to  folk  etymology, jordanite,  n.,  a  lead  arsenic  sulfide  (mineral.)  —
22738:Derivatives:  man,  tr.  v.,  man-ful,  adj.,  man-ful- ly,  adv.,  man-ful-ness,  n.,  man-hood ,  n.,  man-ly, adj.,  man-li-ness,  n.,  mann-ish,  adj.,  mann-ish-ly, adv.,  mann-ish-ness,  n. man,  n.,  a  unit  of  weight.  —  See  maund. manacle,  n.,  handcuff.  —  ME.  manicle,  fr.  OF. manicle,  lit.  ‘a  little  hand’,  fr.  L.  manicula,  dimin. of  manus,  ‘hand’.  See  manual,  adj.,  and  -cle. Derivative:  manacle,  tr.  v.
22760:mandarin,  n.,  ])orange;tangerine;2)deep orange dye.  —  From  prec.  word;  so  called  in  allusion to  the  yellow  robe  worn  by  a  mandarin, mandatary,  n.,  a  person  to  whom  a  mandate  has been  given ;  a  state  to  which  a  mandate  has  been given.  —  L.  manddtarius,  ‘one  to  whom  a  charge or  commission  is  given’,  fr.  mandatus,  pp.  of mandare.  See  next  word  and  -ary. mandate,  n.  —  MF.  (  —  F.)  mandat,  fr.  L.  manda- tum,  ‘commission,  order’,  prop.  neut.  pp.  of mandare,  ‘to  commit  to  one  s  charge,  enjoin, command',  lit.  ‘to  give  into  one  s  hand  ,  fr. manus,  ‘hand’,  and  dare,  ‘to  give  .  See  manual and  date,  ‘point  of  time',  and  cp.  command, commend,  countermand,  demand,  maundy,  re¬ mand.
23129:maund
23168:Derivatives :  maul,  mall,  tr.  v.,  maul-er,  n. maulstick,  also  mahlstick,  n.,  a  long  rod  used  by painters.  —  Du.  maalstok,  lit.  ‘painting  stick’, compounded  of  malen,  ‘to  paint’,  and  stok, ‘stick’.  The  first  element  is  rel.  to  ON.  maria, OHG.  maldn,  malen,  MHG.  mdten,  G.  malen, ‘to  paint’,  OE.  mal,  ‘mark,  stain’;  see  mole, ‘spot’.  For  the  second  element  see  stock,  stick, maund,  also  man,  n.,a  unit  of  weight  used  in  India, Persia  and  Turkey.  —  Hind,  and  Pers.  man, ‘mina’,  fr.  OI.  mana,  which  is  of  Sem.  origin. See  mina,  ‘unit  of  weight’, maund,  n.,  a  hand  basket.  —  ME.  maund  fr.  MF.
23170:maund
23172:Cp.  F.  marine,  ‘hand  basket ,  which  derives  fr. MDu.  mantle,  avar.  of  mande. maund,  tr.  and  intr.  v.,  to  beg  (slang).  —  Prob.  fr.
23174:maunder,  intr.  v.,  1)  to  wander  about  aimlessly;
23175:2)  to  mutter,  mumble.  —  Prob.  freq.  of  maund,
```


## [2026-09-07T15:54:26.492Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"meager\\|macron\\|Macedon\" AHD_watkins1985.txt | head -10; echo \"=== root mak ===\"; grep -n \"^mak\\|mak-\\.\\|mā̆k-\\|mak- \" AHD_watkins1985.txt | head -10",
 "description": "Watkins AHD root mak-"
}
```


### [2026-09-07T15:54:26.549Z] TOOL RESULT

```
720:mak-. Long, thin. 1. Zero-grade form *mak- becoming *mak- in suffixed form *mak-ro- in: a. Latin macer, thin: MAIGRE, MEAGER; EMACIATE; b. Greek makros, long, large: MACRO-, MACRON; AMPHIMACER. 2. Suffixed form *mdk-es- in Greek mékos, length: MECOPTERAN, PARA- MECIUM. [Pok. mak- 699.]
823:peie-. Also pei-. To be fat, swell. 1. Extended o-grade form *poid- in Germanic *faitaz, plump, fat, in derivative Germanic verb *faitjan, to fatten, whence Germanic past participle *faitidaz, fattened, in Old English f#t/t), fat: FAT. 2. Possibly suffixed zero-grade form *pi-tu- in Latin pituita, moisture exuded from trees, gum, phlegm: PIP 5, PITUITARY, PITUITOUS. 3. Possibly suffixed zero-grade form “pi-nu- in Latin pinus, pine tree (yielding a resin): PINE!, PINEAL, PINON, PINNACE; PINA CLOTH. 4. Suffixed zero-grade form *pi-won- in Greek pidn, fat: PROPIONIC ACID. 5. Suffixed zero-grade form *pi-wer-, “fat, fertile,” in: a. *Iwer-ii, the prehistoric Celtic name for Ireland, in Old English Jras, the Irish: (ERSE), IRISH; b. * Piwer-id in Greek Pieria, a region of Macedonia: PIERIAN SPRING. [Pok. pei()- 793.]
1789:MACKLE macula MACLE macula MACRO- mak- MACROCOSM kes-3 MACRON mak- MACULA macula MACULATE macula MACULE macula
1834:MEADOW mé-4 MEAGER mak-
=== root mak ===
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
709:mag-. Also mak-. To knead, fashion, fit. 1. Germanic *mak- in: a. Germanic verb *makén, to fashion, fit, in (i) Old English macian, to make: MAKE (ii) Old French mason, mason: MASON; b. Germanic compound noun *ga-mak-(j)6n (*ga-, with, together; see kom), “he who is fitted with (another),” in Old English gemzcca, mate, spouse: MATCH}, 2. Germanic nasalized form *mangjan, to knead together, in: a. Old English mengan, to mix: MINGLE; b. Old English gemang (ge-, together; see kom), mixture, crowd: AMONG, MONGREL. 3. Suffixed form *mak-yo- in Greek massein (aorist stem mag-), to knead, hence magma, unguent: MAGMA. 4, Suffixed length- ened-grade form *mdg-ya- in Greek maza, a (kneaded) lump, barley cake: MASS; (AMASS), MAZAEDIUM. 5. Suf- fixed lengthened-grade form *mék-ero- in Latin macerdre, to tenderize, to soften (food) by steeping: MACERATE. [Pok. mag- 696, 2. madk- 698, men(a)k- 730.]
718:mak-'. Poppy. Probably borrowed into Indo-European, as the plant is of Mediterranean origin. Lengthened-grade form *mék- in Greek mékén, poppy: MECONIUM. [Pok. mak(en)- 698.]
719:mak-2. (Leather) bag. Germanic form *magon-, bag, stomach, in Old English maga, stomach: Maw. [Pok. mak- 698.]
720:mak-. Long, thin. 1. Zero-grade form *mak- becoming *mak- in suffixed form *mak-ro- in: a. Latin macer, thin: MAIGRE, MEAGER; EMACIATE; b. Greek makros, long, large: MACRO-, MACRON; AMPHIMACER. 2. Suffixed form *mdk-es- in Greek mékos, length: MECOPTERAN, PARA- MECIUM. [Pok. mak- 699.]
955:5. Suffixed form *lag-no- in Greek lagnos, lustful, lasciv- ious (> lagneia, lust, lasciviousness): ALGOLAGNIA. 6. Variant form */ég- in Greek légein, to leave off: CATALECTIC. [Pok. (s)lég- 959.] sleidh-. To slip, slide. 1. Germanic *s/idan, to slip, slide, in Old English s/idan, to slide: SLIDE. 2. Germanic *slid- in: a. Middle Low German sledde, a sled, sledge: SLED; b. Middle Dutch s/éde, a sled: SLEIGH; C. Middle Dutch sleedse, sleigh: SLEDGE. sleng”h-. To slide, make slide, sling, throw. 1. Germanic strong verb *slingwan and derived suffixed noun form *slingw-6- in Old Frisian slinge, sling, akin to the possi- ble source of Middle English sling, sling: SLING}; (SLING- SHOT). 2. Germanic variant strong verb *slinkan in Old English slincan, to creep: SLINK. 3. Suffixed o-grade form *slongh-ri-ko- in Latin lumbricus, intestinal worm, earthworm: LUMBRICOID. [In Pok. (sjleidh- 960, slenk- 961.] sleu-. Hypothetical base of a group of distantly related Germanic derivatives with various suffixes. 1. Germanic *slii-m- in Old English slima, sleep: SLUMBER. 2. Prob- ably Germanic *slautjan- in Old English “s/léte, sleet: SLEET. 3. Germanic *slus- in Norwegian slusk, sloppy weather, probably akin to the possible Scandinavian source of SLUSH. 4. Germanic *sleura- in Middle High German slier, mud, slime: SCHLIEREN. 5. Extended form *sleug- in Germanic ‘*sluk-, *slug- in: a. Norwegian dialectal slugg and Swedish dialectal slagga, slow-mov- ing animal or person, probably akin to the source of Middle English slugge, a sluggard, and sluggen, to be idle: SLUG?, SLUGGARD; b. Dutch /og, lazy, slack: LOGY. [Pok. (s)leu- 962.] sleubh-. To slide, slip. I. Basic form *sleubh-. 1. Ger- manic *slewb- in Old English s/éf, siif, slief, sleeve (into which the arm slips): SLEEVE. 2. Suffixed form *sleubh- ro- in Latin Jibricus, slippery: LUBRICATE, LUBRICITY, LUBRICIOUS. II. Variant Germanic form *sleup-. 1. Ger- manic *slup- in: a. Old English slypa, slyppe, slipa, slime, slimy substance: SLIP’; COWSLIP, OXLIP; b. Old English *sloppe, liquid food (perhaps > Middle English sloppe, a muddy place): sLoP!; c. Old English (ofer)slop, surplice (perhaps > Middle English sloppe, a kind of garment): SLOP?. 2. Germanic *s/aup- in Dutch sloep, sloop (< “gliding boat”): sLoop. [Pok. sleub(h)- 963.] sli-. Bluish. Contracted from *s/is-. 1. O-grade form *sloi- in Germanic *slaihw6n in Old English s/ah, sla, sloe (< “bluish fruit”): SLOE. 2. Suffixed form *sli-wo- in Latin livére, to be bluish: Livip. 3. Suffixed form *s/i-wd- in Serbo-Croatian sijiva, plum: sLivovitz. [Pok. (s)li- 965.] sloug-. Help, service. Celtic and Balto-Slavic. Suffixed form *sloug-o- in Old Irish slag, slog, army, host, whence Gaelic sluagh, army, host: SLEW!, SLOGAN. [Pok. slougo- 965.] smé-. To smear. Contracted from *smeo-. 1. Extended root *smeid- (< *smea-id-) in Germanic *smitan in Old English smitan, to daub, smear, pollute: SMITE. (2. At- tributed by some to this root, but more likely to be of unknown origin, is the Germanic root *mas-, spot, speck, in: a. Middle Dutch masel, pustule, spot, akin to the source of Middle English masel, measles-spot: MEASLES; b. Old French masere, mazre, knot in wood: MAZER.) 3. Attributed by some to this root, but perhaps distinct, is root *smik-, small, in: a. Latin mica, crumb, small piece, grain: MICA; b. Greek (s)mikros, small: MICRO-, MICRON; CHYLOMICRON, OMICRON. [Pok. smé- 966.] smeg-. To taste. Germanic *smak- in: a. Old English smzxc, flavor, taste: SMACK?; b. Middle Dutch and Mid- dle Low German smacken, to taste, make a sound with the lips while tasting food, akin to the source of SMACK!. [Pok. smeg(h)- 967.] smei-. To laugh, smile. 1. Germanic reshaped forms *smer-, *smar- in Old English smercian (with -k- forma- tive), to smile: SMIRK. 2. Germanic extended form *smil- in Swedish smila, to smile, probably akin to the Scandi-
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1454:ELUANT leu(@)- ELUCIDATE leuk- ELUDE leid- ELUTE leu(a)- ELUVIUM leu(a)- ELYTRON wel-3 EMACIATE mak- EMANATE ma-3 EMANCIPATE man-2 EMASCULATE mas EMBASSAGE ag- EMBASSY ag- EMBELLISH deu-2 EMBER eUS- EMBER DAY ambhi, rei-3 EMBLEM gWele-1 EMBLEMENTS bhel-3 EMBOUCHURE beu-! EMBRACE mregh-u- EMBROCATE mergh- EMEND mend- EMERGE mezg-! EMERITUS (s)mer-2 EMESIS weme- EMETIC weme- EMIGRATE mei-! EMINENT men-2 EMIT (s)meit(9)- EMMET mai-1 EMOLLIENT mel-1 EMOTION meue- EMPEROR pere-! EMPHASIS bha-' EMPHYSEMA pu-! EMPIRIC per-4 EMPLOY plek- EMPORIUM per-2 EMPRISE ghend- EMPTY med- EMPYEMA pu-2 EMPYREAL pil- EMULSION melg- EMUNCTORY meug-2 EN-! en
1789:MACKLE macula MACLE macula MACRO- mak- MACROCOSM kes-3 MACRON mak- MACULA macula MACULATE macula MACULE macula
2059:-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- PARALLAX al-1 PARALLEL al-1 PARALLELEPIPED ped-! PARALOGISM leg-1 PARALYSIS leu PARAMECIUM mak- PARAMOUNT ad-, per! PARAMOUR amma, pert PARANOIA nous PARAPET peg- PARAPHERNALIA bher-1 PARAPHRASE gWhren- PARAPLEGIA plak-2 PARASOL pere-1, sawel- PARATAXIS tag- PARBOIL beu-! PARCAE pera-1 PARCEL pere-2 PARCENER pere-2 PARDON d6-
```


## [2026-09-07T15:54:39.942Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ISS_alt_DKS mwgsk/maxs ===\"; grep -n \"mwγšk\\|mwgsk\\|mwyšk\\|magas\\|maxš\\|maxsi\\|makṣa\" ISS_alt_DKS.txt | head -20; echo; echo \"=== SNS ===\"; grep -n \"maxš\\|maxs\\|magas\\|mags\" SNS.txt SNS_pages.txt | head -10; echo; echo \"=== PHD ===\"; grep -n \"magas\\|maxš\\|makas\" PHD.txt PHD_mackenzie.txt | head -10; echo; echo \"=== NYB ===\"; grep -n \"magas\\|maxš\\|makas\" NYB_vol2_glossary.txt | head -10; echo; echo \"=== SOD ===\"; grep -n \"mwγšk\\|mwgšk\\|mwgsk\\|house fly\\|fly\" SOD_pages.txt | head -20",
 "description": "Search Iranian sources for fly words"
}
```


### [2026-09-07T15:54:40.060Z] TOOL RESULT

```
=== ISS_alt_DKS mwgsk/maxs ===
6045:тай{а- ‘bee’ or ‘fly’, Sid. rogr+ mata, BS maksika- ' bee', Tib. sbran-ma ' fly, bee’; Sid. 109r4 smáta-vattala ' excre- ment of bees’, BS màkstka-vitka-, Tib. sbrau-mali rtug- фа; Z 2225 kho ju mate mahst virá 'like bees on honey’; III 73:171; 181 qva; LII 73:180 má, gen. plur. ш 73:182 тӣойт; with pronoun yi, ш 73:178 mot. From *maxši- > *mëssa- > mata (see also hoassa-, hyāta-), to Av. зпахй- ‘fly’, Zor.P. maxš, Yidya maxšë, тӧхї, ' mosquito", Orm. maii, misi *Йу'; Sogd. Bud. mwyšk-, O.Ind. maksa-. Variants are *mukasa-, Zor.P. makas, magas, N.Pers. magas, Yidya moyuso, magusa, Pašto majai (*masyaka-). IE Pok, 699 mako- ‘midge’, O.Ind. masáka-, Lit. mäšalas; with -s- as above.

=== SNS ===
SNS.txt:8391:ltfA ;,; tf i :maxs par: ^>^* 
SNS.txt:13511:.,j-£« :maxs: -*0-"^ 
SNS.txt:13512:l**>»j UiW>. 1112)maksika- : ^j*- maxsl-: fc. 
SNS.txt:13518:>u"&.* 'j^^-i :maxs par: ^W-*o-j-^ 
SNS_pages.txt:5463:                                         i :maxs par:       ^>^*
SNS_pages.txt:9466:                                                                                                                                   .,j-£«   :maxs:      -*0-"^
SNS_pages.txt:9467:                                                                             l**>»j         UiW>. 1112)maksika-           :   ^j*- maxsl-:
SNS_pages.txt:9475:                                                                                                            >u"&.* 'j^^-i :maxs         par:  •   V.

=== PHD ===
PHD.txt:439:~ith: femininity. *madag [mtk' | (M myg, N māya)] essence, substance. ~ig [-yÀ!] essential. ~war [-w/] essential, especial, principal. madan [mtn! | M mdn] come. madār [т comer. mādar [AMYtl < А т-у; mtl | M mdr, N ~] mother. imādayān [m!tgd?n! | М m'dy'n] book. *mādayān [m tyd?n'] essence, basis, core; essential, chief. mādayār [m tgd’l] steward; (chess) rook, castle. mādišt [m’tyst'] *matter, protoplasm. mādīyān [m’tyg?n | N ~] mare. may [my | N ~] hole, pit. magas [mks | P mgs, N ~] fly. ~ i angubén: honey-bee. magind [mkn'd | M mgyn(d)] shield, protection.
PHD.txt:464:maxš [тї] Яу.
PHD.txt:961:bee magas i angubén.
PHD.txt:1982:fly (n.) magas, maxš.
PHD.txt:2303:honey angubén; ~-bee magas i angubén.
PHD.txt:4847:mazgit mizné may magas padīr-! padīrišnī padiriftant magind makog 1-2mar marg margomand margarzān margīh
PHD.txt:4883:māzdēsn mahist, māst māzandar māš, maxš roynt
PHD_mackenzie.txt:3411:magas [mks I P mgs, N .......] fly.
PHD_mackenzie.txt:6041:bee magas i anguben.                        bitterness taxlih.
PHD_mackenzie.txt:6609:final(ly) abdom, pascn.                    fly (n.) magas, maxs.

=== NYB ===
2369:BP makas, NP magas ‘fly’; Av. (1112) maxsi-, Kurd. més; cf Sogd. 45.
5227:maé0ana-: mahmančh mahrka-: marg Mahrküsa: Markus maičyšna-: miyan maidy6.zaromaya-: maióyozarm mainyaoya-: mönöi mairya-: ?mar, mérak maxši-: *macäh Iman-: mčnitan, 6mét 2man-: mandan manah-: hešm-manihš Manuš-ciEra-: Manucihr maodanö.kara-: mustā- pät Imar- (mirya- morota-): murtan ?mar-: amar ?mar- + avis: ošmurtan maroz-: marzihistan maroza- -- pana-: marz- pan Maryu (Mouru-): Marv maršo.kara: "maškar mas-, Masan-: mas masya-: mahik mašya-: mart mafra-: mānsr mafra-sponta: mahras- pand (fra-)may-: framātan (ni-ymāy-: ni-mütan (pati-ymāy: patmān mazdayasna-: mazdēsn mazga-: mazg meroždā-, meroždika-: āmuržītan midaoxta- (mi€oxta): mitöxt miOra-: mihr
6278:xistan: axistan makas: *macah pätkös: pätkust razmik āyozišn: äyöz- *takile: kurušk
7253:magar: hakar magas: *macāh mayz: mazg

=== SOD ===
5245: 508 'ps'nywnch B             JL,J<iioJH^i^J                                            gam- ©impf. flyPm ^fs'm-
5444:      VJ 49c, 476; TSP 7.40, 120, 188; 'flyJnkVw, VJ                  GMS 90, 571; TSP n 212; SCE 412; BSTBL, Dhy
7584:      ornament ?, fly-whisk ?                                   c/^'1332 'psypw     S =» 'ps'ypw, psypw'pky*
11287:                                                                                P(o)zaxu ©^flyj+axu     ^bz'xwq
11721:                                                                         (ro)fly
11728:                                                                         bird, flying parwazane (brwz'ny)
12251:     SCE 272; GMS 384; flycty, BBB 517; gen. pi.                  out, outside, apart, except
12255:                                                                     1393; adv. flykw, TSP 2.469 n pi 75
12273:               C2, 94V8                                                                     flykp>rck, Dhu. 173; GMS 1013
12295:               STi 21.9; GMS 1116; C2 gloss.                                              GMS 463; BBB 640; flykys'n Anc. Lett. 3.7;
12331: 3015 bynt1 C                                                         fiyrt(w)&r~, flyr&r, pyrt&r-, byrd'r-, VJ;
12373:       GMS 1100; flyrWnty, VV-Li                                   GMS 463; STi 70.13; Sund. AoFviii 1981 p214;
14912:                                                                       (to)fly                  ©impf. frywz =»Prwz~
15618:4169 yr-3 B, S                                   >                          gadfly
16086:  xwary/e =»zyny Yw>ry                  cr-* *i5j*j*-              Ywbd'r~y STi 43.14; pres. inf. Ywfly, Dhy. 320;
19509:                                                                   fly, mosquito
23926:                                                                    parPerat ©pt. St.; perf. prflyrtfw) <?V-
24013:      SCE 400; Sogdica. 2 1.1 6b 23; GMS 498, 668;                           parPer    ©< * p a                ©impf pryfly
24313:                                                              flying
24325:7171 prm't^k    S ^ prm>t>y                                   (ro)fly
```


## [2026-09-07T15:55:04.583Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB context ===\"; sed -n '2360,2375p' NYB_vol2_glossary.txt; echo; echo \"=== SNS page tag ===\"; awk 'NR<=9467 && /\\[pdf page/ {p=$0} END{}' SNS_pages.txt; grep -n \"\\[pdf page\" SNS_pages.txt | awk -F: '$1<9467' | tail -3; echo; echo \"=== SOD mwgsk ===\"; grep -n \"mwyšk\\|mwySk\\|mwgšk\\|mw.šk\\|mwys\" SOD_pages.txt | head -10",
 "description": "NYB, SNS page, SOD lookups"
}
```


### [2026-09-07T15:55:05.914Z] TOOL RESULT

```
=== NYB context ===
Kai-~ 1148. — From East Ir. *Druväspa-, whose initial d- had, as usual in East Ir., the spirantic pronunciation 6- which passed to l-; attested on coins of the king Kaniška in the form APOOACIIO as the name of a deity, Christensen, Sass. 38— 41; Benveniste, JA 228, 1936, 234. Cf the Av. female deity (783) Drvdspa-.
sentence; it is never governed by a prep.; when it is attached to kü introducing a direct speech this in itself must have had the independent form am (q.v.): guft kū-m bē āmurž 3114, direct speech: am bē dmurž ; — cigón-am guft 121"; c&-m zešt par cašm hah for thou art disgusting for me to look at 3111712; han-am pāšom ax"àn Œa-
www-parsianjoman.org | ool wok
-m
rödmän dah give me that blissful world, the G. 325-5; vahist-om u Garödmän be dah 339-19; kär-om tč framäyeh please do thy duty towards me 27%; apar-p-im ravišn I must climb up 40?%; — poss. pron.: Hutos i-m xvah H. (who is) my sister 2422; (man ...) ke-m fradand ... (me) whose child 1275 (v.s. v. kē B); api-m den katém? which is my religion? 629-10, etc.; — if the encl. belongs to a prep. this is placed later in the sentence and takes the form of the corresponding adv. if there is one: cé-m anākēh vas patiš kunēnd for they will do much harm to me 954 (-m patiš; patiš, q.v., adv. of pat); — attached to a vb.: a) to an imp. as its dir. obj.: pat āzātēh dar-om 6%, v.s. v. daštan; b) to a pret. pass. as its agent, repeating the independent agent man placed before the vb.: man kart-om I did it, it was I that did it 374-5 (twice); through the influence of NP kardam the scribe analyzed this -om as the Ist p. sg. of h- ‘to be’ and spelt it krt' HWH-wm. — In 31? api-m of the MSS must be a simple mistake for api-š; as to 2675 v.s.v. ham. — Av. (1101sq.) mēž, OP -maiy; -m MPrthPrsPazNP. The Man. texts regu- larly have the vowel -o- before -m: -wm = -om, and this is probably also valid for BP, though no vowel is written here (Paz. varying: -am, -um, -im).
mà PL] not, with the imp. and the subju. in an optative sense: mà kun! mā baš etc. ; imp. with the ending -ē: mā 6 änöd rave! 441; ma framäye 5774-5, ete.; pl. mā dārēt! mà ranjénét! ma ‘BYDWN-x, = kunēt 82-13; — subju.: hàn rēc mà bavā ku may that day never come when 13%; -t garān mā sahät 35%, v. sahistan; mà xin YHMTWN-d = rasünd 26% etc. — Com- mon Iranian.
*macäh [mc'"h], macäi [me’y] an Ahri- manic animal 9674. 981%. — Not identified. Possibly to be connected with the ws. denoting ‘fly’: Pastö mac, mac ‘gad-fly’;
122
magu-pat
BP makas, NP magas ‘fly’; Av. (1112) maxsi-, Kurd. més; cf Sogd. 45.
mad [HML’] wine 61%. — Av. (1114) maču-; NW w., ideogr. HMR; v.s.v. has. FrP 5 HML’ = mad (Cod. K in Paz.); NP mai.
Mad [m?d] Media 1158. — OP mada-; KZŠPrth m?d; Arm. lw. mar-k*.
Madinak [mdynk'] Medina 11519.
magü [mgw, inscr.], magük [mgwk], még [mwg FrP 13] a Magus, a Magian: Nar- sahē i magi P1:7; cas. obl. magve in magvé-mart [mgwymlt'] pl. cas. rect. the Magians 20°; pl. cas. obl. mög-martän [mwgmlt?n'] 28; magüné [mgwny] pl. cas. rect. 108!!, cas. obl. 11215. — OP magu-, nom. magus, whence Syr. lw. mgüsä, Arab majüs-; Av. only once in the compound (1176) moyu-ibiš- ‘enemy of the Magi. The authentie Milr forms are: 1. NW mög, whence the Arm. lw. mog, NP möy, pl. méydn; 2. SW mov-, v. s. v. magupat. The other forms are archaisms preserved as learned spellings. The pl. maguné re- presents the old gen. pl. of the u-stems: OP *magūnām > *magün + the common ending -é of the cas. obl. sg. spuriously added, ef örsäneh rād 5814 (v.s. v. ētšān and rdd); another ex. of the pl. cas. obl. in -ün is MPrs dušmynwn < *dušmainyū- nam (S; Bthl, ZairWb 152-153). The reading mgwmy is warranted by the in- scriptions.
magu-pat [mgwpt'] chief of the Magi, or: chief Magian, of the head of the Zoroas- trian priesthood 1104; in this sense com- monly ~-dn ~ 10-12, passim; 168. 100?; — a Zoroastrian priest of this class in general: dastavardn u dätavaran u hēr- patün u ~-dn 1078, — The Olr form preserved as an archaic spelling; the authentic Milr forms are: 1. NW mogpat, Arm. lw. mogpet; 2. SW movpat, Arm. lw. also movpet (Etiša), Syr. lw. mwpt?, mwhpt’, mwhbi? ; NP mobad. V. s. v. ‘pat.
www .parsianjoman.org IN n !

=== SNS page tag ===

=== SOD mwgsk ===
19506:     TSP 6.51                                                 5518 mwysk(>)    B                           ^^
```


## [2026-09-07T15:55:13.136Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19495,19520p' SOD_pages.txt; echo \"--- page tag ---\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<19506' | tail -2",
 "description": "SOD mwγšk entry and page"
}
```


### [2026-09-07T15:55:14.527Z] TOOL RESULT

```
                                         bjt^y1
                                                                   magian house
      mu
      this Ortymw) ©OP imam ^'mw, mwn'w,   'my2                    ace. -fw, C2, IV, 17, 29; loc. -ty, C2, 1R25
                                                              5517 mwypt(w) C, S                                          j*y
      GMS 1401, 1466, TSP; STii 7, 30.33; KG; S W,
        TPS 1994, 43-50                                             muy-pat (mwhbt*) ©*magu-pati           -^mywpt
                                                                    Zoroastrian priest
5507 mwc'k* B                             jf j^T i^ »U-i            C2; Frag. Len. 68, 10, 11; -w, BSTii 843.20, 21,
     mocak **>mwj}k, mwz'k', mwck                                     873.2, 875.12
     teacher
     TSP 6.51                                                 5518 mwysk(>)    B                           ^^
                                                                   muxsk ©*maxsika; Pahl. maxs ©ob. -y, ->
5508 mwck B, M, S                     jtfj^ToU-f
                                                                   fly, mosquito
     moce, moc(a)k/e ©<*maucaka-; Khwar. mwey                      TSP 2.390; SCE 364; GMS 113, 165, 975, 1182 n 2
       ©ob. -y; ob. pi. -ty ^mwc^                             5519 mwyy^ C
     teacher
                                                                   muyyak
      GMS 397, 810, 976; TSP; BSTBL; W-Li; mwck\                                                                    l^jPXfi

        BSTBL; Frag. Len. 44.2; -w, Frag. Len. 81.4; ob.           magian cult
                                                                   C2, 1V23, 24, 27
       mweky, Dhu. 183; pi. ob. mwckty* TSP 6.191;
                                                              5520 mwyyst C
       Bailey. *hamauk-; Mack. *maucaka
--- page tag ---
```


## [2026-09-07T15:55:27.069Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 SOD_pages.txt | cat -A | head -5; echo ---; grep -n -m3 \"page\" SOD_pages.txt | head; echo \"=== SNS ===\"; grep -n -m3 \"page\" SNS_pages.txt | head",
 "description": "Check page tag format"
}
```


### [2026-09-07T15:55:27.144Z] TOOL RESULT

```
 SOGDIAN$
DICTIONARY$
Sogdian - Persian - English$
---
1946:grammatical identifiers to help differentiate the forms. Adding the references with page
2086:    The English Meaning comprises the next line of           the page and line or paragraph is added. For certain
2986:defective in showing Sogdian vowels in quality and                       The phonemic charts on the following pages give
=== SNS ===
```


## [2026-09-07T15:55:34.507Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,ln in [(\"SNS_pages.txt\",9466),(\"SOD_pages.txt\",19506)]:\n    txt=open(f,encoding='utf-8',errors='replace').read().split(\"\\n\")\n    pre=\"\\n\".join(txt[:ln])\n    print(f, \"form-feeds before:\", pre.count(\"\\f\"))\nEOF",
 "description": "Compute leaf numbers"
}
```


### [2026-09-07T15:55:35.861Z] TOOL RESULT

```
SNS_pages.txt form-feeds before: 136
SOD_pages.txt form-feeds before: 286
```


## [2026-09-07T15:55:43.741Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nprint(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['ISS'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('MON'),ensure_ascii=False,indent=1))\n\"",
 "description": "SNS/ISS/MON ref metadata"
}
```


### [2026-09-07T15:55:45.110Z] TOOL RESULT

```
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
{
 "title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967",
 "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute",
 "kind": "google_books_preview+archive_restricted",
 "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)",
 "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only",
 "local_file": null,
 "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.",
 "notes": "Tried IA ('indo-scythian', 'zambasta', 'khotanese texts'), Google Books API. || RE-SEARCH 2026-09: preview only (Google Books partial view of the 2009 reprint — usable for spot checks); no open full text. A dokumen.pub upload exists (not used)."
}
{
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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
```


## [2026-09-07T15:55:56.326Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT col 1112 maxsi / 1154 mas ===\"; grep -n \"maxši\\|maxsi-\\|ma%ši\" BRT.txt | head -5; echo \"--- mas- ---\"; grep -n \"masyah\\|masista\\|masah-\" BRT.txt | head -8",
 "description": "Bartholomae maxši and mas"
}
```


### [2026-09-07T15:55:56.380Z] TOOL RESULT

```
=== BRT col 1112 maxsi / 1154 mas ===
--- mas- ---
5270:frmmmfnd,    ?&.-.  frahrui-anlil^).    —    "3)^1311 *nh-al\  Btml,  IF.  ts.  :o6.  —  >*)  Pü.:  undeut- lich, wohl  Transskr. •  j..  g.  'ar-  V.  'gewähren'.     Praes.  10 snnav :  3r3nv—,     PrP.     tn/iavi'^;     Perf. PPfP.  Jr^/Ä-  (s.  /r»-). )    'gewähren'     sva.    'zu    teil    werden lassen':  Aa  ahmai  aus  Prvnävi'^  "welches Los  wurde  ihm  zu  teil?"  Y.5.3;  4;  — ■a'^a   nS   masistasca  .  .   asayö  »nnavanie (3PKM.)    Y.52.3;    —     asöii..    yä    ni äras'il  (sd.)  jnnavataeca  (3SKM)  Y.fö^. 3.  2)   'gewähren'    sva.    'gewährleisten,
6486:•  j.  aäti.masah-  Adj.  'von  der  Grösse einer  A.':  äat  pitSus  ydi:a  cdijiciärS  'sS N.  (7^(?);  —  taltim  dauru  . . nyäzaym  (sd.) +°jj')  xraoidvaAe  bti'  altavatö  var>dvahe "ein  .  .  Stück  Holz  .  .  von  der  Grösse" einer  Ä.  aus  hartem,  doppelt  so  gross'' aus  weichem"  V.  13. 30.
7086:•  j.  ä.gao§Ö.-masah-  Adj.  'des  Grösse zum  Ohr  geht,  so  gross  wie  man  es  beim Ohr,  dh.  über  der  Schulter  trägt':  alsma- nqmcil . .  'sSbii  qxmS.fianS.masSbÜ  sasts.- /rilnB.masibJ^  {xiAa^.  siati)  A..9.5.
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
7813:•  j.  ^mö.fränö.-masah-  Adj.  'des  Grösse den  gebogenen  Arm  fUlU',  d.  i,  'so  gross wie  man  es  unterm  Arm  trägt':  alsmanqm- ät  . .  °s}6t^  (näml.  stäir^  A.j.5.
10910:masista  xsnaoma  x'nävayäliV.3.iz;g.^2^; —  äai  tum  nishti>ail..ttar»m^a  asavamm kuxsnvqnS  H.2.13,  Vyt55(wo  ^kjt/h- vänB)-,  —  yS  neu  narsm  aiavamm  .. xsnaosta  vä  xsnävayeite  va  '2.4g;  —  ya- '^raca  x^nätS  asavaYi-i^.^C;  —  xi'nüta- htcit  atbislaAe  i&A.)  ..  manS  yaezayäti'^X. /O.iii;  —  xsnüiS  (NPm.)'*  asdonqm urväfßs  pärayeinli  V. /p.31;  —  yat  alsS nä  .  .  haca  alibyS  nmanaHbyS  xsnütS aUii'ß parayäl  V.5.39;  —  ka%a  ^wa mazää  xsnaosäi  aAurä  "wie  kann  ich  dich zufrieden  stellen,  o  AfAA.f"  Y.46,1;  — ndii  xhtSvayeili  ahurim  mazäqm  .  .  ys mazdqm  tarS  manyete  \t  lO.i^q;  6.4;  — yagcä  xsnaespn  (3PKA.)  ahursm  Aaihyäii /y/joianäi/  fraorit  mazdqm  "und  die, welche  gern  mit  rechtem  Tun  AcAÄhM. zufrieden  stellen"  Y,_jo.  5;  —  tistrjm  .. yj  äa\äiti  kuxlnvqnäi  .  .  ayapta  jaio- yantäi  . .  maiyai  ".  .  dem,  der  (ihn)  zu- frieden stellt  .  ."  Yt  &  49;  7J.  24;  — HstrJm  .  .  yezi  . .  bavaitt  yaltö  xSnaiß frihs  paiti.zanlS  Yt.8.4z;  10.120,  Y.ig. 40;  — yaAmäi  xsnütS  bavaiti  mikrS  ,  . yakmäi  IbistB  bavatti  (sd.)  Yt  JO.87;  28, Y.  62.  9;  —  yä^a  . .  anäzarstä  xsnütA  . . a/bisti  yBbm  (näml.  fravasayö)  . .  /ra- cara'iwe\ti3.ZA;  S^  63.  'S^',  iS7';  — xlnuta  F.5;  —  vaT3h3uS xratüm  manaahS yä  xsnyvTsa  g^s^ä*urvqmm  "aufdass  ich den  Willen  des  VM.  befriedige  und  die Seele  des  Rinds"  Y.  28.  \;  —  mazdä  asä xsmüksm  vilnm  xsnaohmnB  "o  M.  und A.,  indem  ich  es  eurem  Willen  recht machen  will"  Y.  ^.  18.  a)  Des.  'zu- frieden stellen,  zu  Gefallen  sein  wollen': nsit  nä  pouräs  (sd.)  drpgvatö  Ayäi  ^ixs- n  uiS  Y.43.11;  —  ys  masying  Hxsn  uiö .  .  gäul  bagä  x^ürsmnS  (sd.)  Y,  J2,  8;  — y}  dusprJ^rJi  (sd.)  Bxsnusä  (iS.)  Y.  4g. I.  a)  mit  Dat  comm.  'Jemands  Zu- friedenheit gewinnen  wollen  für  — ':  tSm nS  vokB  mal  manavhcl  axiriusö  "des  Zu- friedenheit sollst  du  uns  zu  gewinnen suchen,  sammt  der  des   VM."  Y.  45. 9.
14732:u  fasimärTk  'Anütge  und  Verieidig'^rg"  und  i^-o«/-''  sbes.  s)  Tcr��nken,  beleidigen", vicir  II  ditawarik  "Entscheid  und  Urteil';  (lu  mit  Akk.:  ratavS  vJspe  masista  ,  .  yai  vS i  t):  dätmoar;  {t^  3):  dSlinaarih,  etL;  "icir.^ ^^f/j/gg^^  _  „gfig„^g  ^  .j,acargAa  . .  syaeÜFfta .SQ. :  ayäyai.    Zu  F.  S  wird  gesagt,  liaiii  be- 1  ,        azaosa  V  7  3  a  ■  2 1  ■  —  ahuräne
14779:•  j.  tbiSifi-  tn.  'Glied'  des  Fingers;  kasil^take imahmahe,  masistake)  »rszvB  fraltnum  °iis V. 6.10(12,  i4),iÄ44PüZ.
```


## [2026-09-07T15:55:59.272Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"makros\\|mākros\\|mak-ro\\|macer\" IEC.txt | head -8; echo \"=== WLD Bd2 p223/225 ===\"; grep -n \"makros\\|maksi\\|maxsi\" incoming/WLD/WLD_Bd2_pages.txt | head -8; echo \"=== SKT meagre ===\"; grep -n -i \"meagre\\|macer\" SKT.txt | head -5; echo \"=== LEW macer ===\"; grep -n \"macer,\" LEW_1910.txt LAT.txt | head -5",
 "description": "Mann, Walde-Pokorny, Skeat, Walde Latin"
}
```


### [2026-09-07T15:55:59.381Z] TOOL RESULT

```
=== IEC ===
10282:Oss. mågúr ‘poor’; Hitt. cf. (variant) maklanc, makla- ‘lean, thin’; Gk. makrós ‘long; Lat. macer, f: macra ‘lean; barren’; OHG magar, OE mæger, ON magr, f: mọgr ‘lean’
10369:mātēr (màter-, mātr) (1) ‘mother’. Cf. maté and mati. WP II, 229 Skt. matt; Ober matar; Per. madar; Oss. cf. mad, madà; Tokh. macar, B macer; Arm. majr, gs mawr, ab. s. marb; Myc. matere(i), ds; Gk. méter, gs métrós; Doric mater; Phryg. māte- res, pl.; Alb. motër 'sister'!; Lat. mater, gs matris; Osc. maatreís, gs; Umb. matrer, gs; (?) Faliscan materei, ds; Olr. máthir, Ir. má- thair, gs máithre; Gaul. matre-bo, dpl.; W cf. modr-yb (“aunt', fr. *màtriqua); OHG muoter; OE moóor, ds meóer; ON móðir, gs móður & moeór; OCS materi beside mati, gs matere; Slovak mat, mati & mater; R mat, gs materi; Li. móte, gs móters & móteris, f. ‘woman’; cf. móčia ‘mother; Latv. (isophone) materes, pl. Cmotherwort', bot.)
=== WLD Bd2 p223/225 ===
14742:Velar die arische Sippe von ai. mdksa- m. maksa „Fliege" av. maxsi- „Fliege,
20068:        maksiibhih. Sup. maksfdama-: mit Xas.         ai. mawksu „bald‘': av. mosn
=== SKT meagre ===
599:alchemist^s  uuignun  of  mala^ma,  a  molli- fying application ;  jwrh*^  with  Arab,  al \  '■the)  prcfixerU^Gk.  /ia\a7/ia,  an  emol- lient. *Gk.  itoXaacup  (for  it^KnK-yuv),  to soflcn.  -Gk.  ^laAoiwSr,  soft.    (^MAR.) Amanuensis.  (L.)    See  Manual. Amaranth,  an  unfadinE  flower.     (L.- Gk.)     Properly  amarant,  as  in  Milton  ;  but -anth  is  due  to  confusion  with  Greek  d*"^!, a  flower.  M  L.  amamu/us.  «Gk.  dfiapavror, unfading,  or  as  sb.  unfading  flower. —.Gk. d;  not;  and  fiapalvnv,  to  fade.    (^M.\R.) A.ma8S.  (F.  —  L.  —  Gk. )     See  Macerate. Amatory.  (L.)      L.  ama/oriiu,  loving, —  I.,  amator,  a  lover. —  I,,  amare,  to  love; with  suflix  -tor.    (VKAM.)
8251:haggard  (a\  Inn,  meagre  (E.)  Orig kagg^d,  i.e.  hag-like,  from  hag.  'The ghostly  prudes  with  MaggtJ  face/  Gray, A  Lonfj  Story,  near  end.  Btisspelt  by  con- fusion with  the  word  below.
9448::k .  KofT ;  se«  Shear. ^H«'^.;      Heb   yahM^ith.  or, ly,  yakavth,  ( iod  ,  see  article of  the  Bible, meagre.    (L.)    X^  iWif r.diy.
10862:I*  (0* «  Hnd  of  spice.  (F.-L.-Gk. .T)  F.  moiii,  mace.  It  &eemstoha%T KBfiued  with  O.  F.  macer.  which  '  is ■oe»  as  many  imagine,  but  a  reddish, iticaJI,  and  a&liinccnt  rind  of  a  ceitain llDoC  :*  Cot.  Both  prob.  from  L  macer, I  La.  the  '  rind  of  a  crrat  root,  which k Che  name  of  the  tree  itself,'  Holland, PUcy,  aii.  8.*Gk.  itaMtp;  donbtle&s Item  oiigfin.  Cf.  Skt  makura,  a  bud, io%opa  rlen^i).  Arabian  jasmine. to  soften  by  steeping.  iL.) il»  mofirare.  to  steep;  fre- bate  m^c-.'^K\x%&.  moikitt, r««iv.  to  knead ;  Skt. (V  MAK.) lo  hMp  up.  (F,  •  L.  *  Gk.) to  heap  up.  -  F.  4  masH,  Into
10864:mao&roiU,  maooaronL  (Ital.  *  L.) O.  Ital.  maccanmi,  *  a  kinde  of  paste mente  j '  Florio.  Prob.  from  O.  luL mafcartt  *to  bruise,  batter,  to  pester/ Florio ;  i.e.  to  reduce  to  pulp. «-  ll  sMr*, base  of  macerart,  to  macerate.  Der. macaroHU,  i.  c.  in  a  confused  or  mixed state  (applied  to  a  jumble  of  lan^agcs).
=== LEW macer ===
LAT.txt:19647:vre". Joint i exiguus, k macer, k inanis, k ieiunus. 0 ppos 4 k tumens,
LAT.txt:35473:macer, -cra (-cera Ital.), -erum: maigre. Ancien, usuel. Panro-
LAT.txt:35479:(Pl .), macritas (Vitr.)j permacer, permaceo (Enn.); macescS, emacescS- 669 ~
LAT.txt:35487:le voit par lea gloaea: macer, Xeuxoc,, et macero , Xeraruvo) ( 4 . cotd
```


## [2026-09-07T15:56:10.009Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC context ===\"; sed -n '10275,10285p' IEC.txt; echo; echo \"=== WLD Bd2 fly ctx ===\"; sed -n '14730,14750p' incoming/WLD/WLD_Bd2_pages.txt; echo; echo \"=== WLD Bd2 mak- long ===\"; grep -n \"lang und dünn\\|schlank\\|mager\" incoming/WLD/WLD_Bd2_pages.txt | head -8",
 "description": "Mann headword and Walde-Pokorny contexts"
}
```


### [2026-09-07T15:56:10.093Z] TOOL RESULT

```
=== IEC context ===
20
25
30
35
40
45
728
Oss. mågúr ‘poor’; Hitt. cf. (variant) maklanc, makla- ‘lean, thin’; Gk. makrós ‘long; Lat. macer, f: macra ‘lean; barren’; OHG magar, OE mæger, ON magr, f: mọgr ‘lean’
maks- “evil, hate, anger’. See Supt; M Sk. maksàmi (2) ‘be angry’; Arm. maxam, v. ‘envy, grudge’; maxank, s. id.; OCS cf. mo&tij ‘worse’; mošti, fpl. ‘carrion’
mak- (variant of mak- (3) ?, cf. makrós) Av. mas ‘wide, big’; maso, gs -àh- ‘size’; Gk. cf. másson ‘bigger, more, longer, further. (Other forms ambig. See mak- (3))
mál- ‘like, prefer; better. Cf. mel- Gk. cf. mála ‘very’; Hitt. malahhi, malesk(imi) “like, prefer, approve of; Li. cf. malonas, adj. ‘kind’. (E-gde in Gk. réie moi “it concerns me & Lat. melius, adv. "better, Cf. also Gk. mállon, adv. “more

=== WLD Bd2 fly ctx ===
s. u. maq- „Haut-, Lederbeutel".



niaqo- oder moq-0-(-Zo-, -Ao-, Deminutivformantien) „Stechfliege, Miicke".
   Ai. maedka- m. „Stechfliege, Miicke", lit. maszalal „Mucken", lett. masalas
,,K<^fifli6gen" (Bezzenberger BB. 16, 120), wozu russ. mosolUh, mosolyzith
,,plagen, zudringlich anbetteln" (vom Bilde des zudringlichen Miicken-
sch warms), und mit anderm Formans (ymos^thl:) osorb. moscic so, moscec
so „wimmeln (ursprgl. wie oin Miickenschwarm)", sowie wohl auch lit.
maszdju, -ti ,,ein Kind zeugen" (Zubaty AfslPh. 16, 400).
   Wohl schallmalend (wie auch mu-, 7nus- in Worten fiir Fliege), vgl. mit
Velar die arische Sippe von ai. mdksa- m. maksa „Fliege" av. maxsi- „Fliege,
Miicke" usw.(s. IThlenbeck Ai, Wb. 209, Bartholomae Airan. Wb. 1    12).
                                                                      1


  Unannehmbar legt Petersson LUA. 1915. 9f.: 1916, 45f. ein mak- „stechen,
verletzen" zugrunde.
226                           maqh-o-s, “{s)lo-   — mag-


=== WLD Bd2 mak- long ===
14071:mit Bed.-Entw. von .,blaB” zu „mager. schwaclr' nach Trautmann auch
14588:mak-:mok- „lang und diinn, schlank“. mdkros.
14603:lang''? anders Debrunner GGA. 1910, 12), juaxedvog „schlank", /uaxgog „lang'‘
14607:glaublich.    Lat.   macer,    -cra^    -cruni   „mager“, maceo,      -ere       „mager   sein",
14608:niacies ..Magerkeit".  Ahd. magar, ags. mcegcr, aisl. magr „mager“ (Entl.
15871:gering, mager“ eher aus dem Komparativ riickgebildet); komp. got. min-
16508:7nzgnidb ..verderben'',                   mozgmdh „abmagerm*', abg. m^zditi ,.schwachen‘S russ.
16728:schmeidig,   schmuck^% mhd. gesmiicket „schlank'^      Ygl. iiber die germ.
```


## [2026-09-07T15:56:12.998Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14585,14615p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Walde-Pokorny mak- long entry"
}
```


### [2026-09-07T15:56:13.069Z] TOOL RESULT

```
(nicht zugehoriges bei Miklosich EWb. 206) als c^-Erweiterung damit in
Zusammenhang (Prellwitz^ 35).

mak-:mok- „lang und diinn, schlank“. mdkros.
  Ay. mas- „lang'', Komp. masyd „der gr66ere“, Sup. masiMa-, ap, ma’&iUa-
„der hochste“, aY. masah- n. „Lange, Grofie“ {^mas- fiir                aus idg.
mjs- durch EinfluS Yon mazy a „gr6fier“ yeyag und Yon kasyd ,.kleiner“
                                                    :



erwagt Osthoff MU. VI 131); fiaaoco, judoocov {judoGov nach doaor „naher“,
s. zuletzt Osthoff MU. VI 61 f., 131) „langer“, fnqyuoTog „der langste'*, /nfjy.og.

dor. jbidyog n. „Lange“, yy]yvvco „Yerlangere“. 7tegifiJii)yi]g „sehr lang oder
                       Maxera (Pick BB. 26, 242) ,,Hochland“, Maxedoveg
hoch^', TiegifjiYixETog ds.,
daher „Hochlander'‘ (auch horn. d-juai-pidxETog nach Bechtel Lex. 34 ,,sehr
lang''? anders Debrunner GGA. 1910, 12), juaxedvog „schlank", /uaxgog „lang'‘
(^ lat. maeer. dt. niager; W. Meyer KZ. 28, 175 nennt zw. auch ir. 7nac-
raidhV. i. galar O’Clery); dafi hingegen juaxag „Gluckseligkeit“, fidxdg,
judxagg ,,gluckselig" auf einer Gdbed. „Gro6e" beruhen sollen, ist nicht
glaublich.    Lat.   macer,    -cra^    -cruni   „mager“, maceo,      -ere       „mager   sein",
niacies ..Magerkeit".  Ahd. magar, ags. mcegcr, aisl. magr „mager“ (Entl.
aus einem Yulgarlat.-italien. magro ist nicht erweislich, s. Kluge® undWeU
gand-Hirt s. y.). Der Bed. halber ganz fraglich ist Strachans BB. 17, 299;
20, 21 Gleichsetzung von ir. mer „Finger'^ mit gr, jxaxgog (s. auch u.
ma- ;..gut“)-
  Ygl. Curtius 161, Fick I^ 101, 279, 508, III^ 304, Prellwitz u. ixaxgog^
Yf. LEWb.2 u. macer,
   Aber lit. mokHy -cU „k6nnen, zahlen". lett. makti^ mdztt „Yerstehen, konnen",
```


## [2026-09-07T15:56:19.238Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T15:56:19.245Z] TOOL RESULT

```


```


## [2026-09-07T15:56:23.268Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%DA%AF%D8%B3",
 "prompt": "Give the full Persian etymology section for مگس (magas): Middle Persian form, Proto-Iranian/Avestan ancestor, cognates, and any cited references."
}
```


## [2026-09-07T15:56:25.248Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C4%B8s-",
 "prompt": "What is this reconstruction page about? Give the reconstructed PIE form for 'fly (insect)', its meaning and descendants (Indo-Iranian, Avestan, Sanskrit, Persian)."
}
```


### [2026-09-07T15:56:27.006Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T15:56:27.889Z] TOOL RESULT

```
# Persian Etymology of مگس (magas)

**Middle Persian Form:** The word derives from Middle Persian (mks /magas/).

**Proto-Iranian Ancestor:** It comes from Proto-Iranian *makácaH, which ultimately traces back to Proto-Indo-Iranian *mákš meaning "fly."

**Cognates:** The entry notes a comparison with Sanskrit मशक (maśaka), sharing the same root meaning.

**Etymology Path:** "From Middle Persian (mks /magas/), from Proto-Iranian *makácaH, ultimately from Proto-Indo-Iranian *mákš ('fly')" as the page indicates through its structured etymology tree.

The word entered various descendant languages including Khalaj, Ottoman Turkish, Hindustani, Pashto, and Central Kurdish, demonstrating its widespread influence across language families in the region.
```


## [2026-09-07T15:56:33.109Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/mak%C3%A1%C4%8DaH",
 "prompt": "Give the reconstruction, meaning, etymology (Proto-Indo-Iranian ancestor) and the full descendant list (Middle Persian, Persian, Sogdian, Khotanese, Pashto, Balochi etc.), plus any cited references."
}
```


## [2026-09-07T15:56:34.626Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%87",
 "prompt": "Give the Persian entry for مه: the etymology of meh 'great/greater' (Middle Persian, Old Persian maθišta, Avestan), and any related words like مهست/مهین/مهتر. Quote the etymology text."
}
```


### [2026-09-07T15:56:34.954Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T15:56:40.266Z] TOOL RESULT

```
# Persian Entry for مه (meh - "great/greater")

## Etymology

The word مه (meh) meaning "great" comes from Middle Persian. According to the source:

"From Middle Persian 𐫖𐫏𐫆 (myẖ /⁠meh⁠/), from Proto-Iranian *majā́, from Proto-Indo-Iranian *maȷ́ʰā́, from Proto-Indo-European *méǵh₂s ("great")."

The entry notes cognate relationships with English words like "mickle" and "much," Latin "magnus," and Ancient Greek "μέγας" (mégas).

## Related Words

The Wiktionary article lists derived terms under this etymology:
- **مهتر** (mehtar)
- **مه‌مانگ** (meh-mâng)
- **مه‌بانگ** (meh-bâng)

## Additional Context

This sense is marked as **archaic** in modern Persian usage, appearing both as an adjective meaning "big" or "great" and as a noun with similar meanings.
```


## [2026-09-07T15:57:06.712Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mahist\\|meh \\[\\|mas \\[\\|meh\\b\" PHD.txt | head -20; echo \"=== NYB mas ===\"; grep -n \"^mas\\|mas, Masan\\|mahist\\|meh \" NYB_vol2_glossary.txt | head -20",
 "description": "MacKenzie and Nyberg mas/meh"
}
```


### [2026-09-07T15:57:06.799Z] TOOL RESULT

```
227:azbāy- [*2b*d-] invoke. ~išn: invocation. azd [zd | = M] known. Azdahag Pcydi’k' | M ?zdh?g, (N aždahā)] a legendary ‘dragon’ king, Dahāg. azdénidan, azdén- Pzdyn-ytn'] inform. azēr [%cdl | N zér] below, under. azg [22 | N аху) branch. aziš [hcf | М *cy$, 22у] from him, it; postposition (= az) from, ~-keh [-ks] inferior, subordinate. ~-meh [-ms] superior. āz-kāmaģ [?ck’mk'] greedy. ~ih: greediness. azmüdan, azmāy- ['zmwtn!,?zm'd- | N 2~] = uzmüdan. aznawar Pzrw/l | M ?zn] noble. azraw-, v. azruftan. azray- ['zr'd-] adorn. azruftan, azraw- [)zlwp-tn! | M *zrw-] go out, be extinguished. āzurdan [Pcwltn! | N ~] = āzārdan, āzwar [?*cwl | N ~] greedy. ~ih: greed.
306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
444:mahist [msst!, mhst! | M mhyst, N ~] greatest. makóg [mkwk' | M mkwg, N mako(k)] boat. mālīdan [m’lytn' | N ~] = muštan.
477:meh [ms | M mhy, myh, N ~] great(er), old(er).
479:mehénidan, mehēn- [msyn-ytn'] increase, magnify. ~iSn: increase.
734:adult dād-meh, purnāy.
1746:elder dadmeh, mehtar.
2144:great meh, wuzurg.
2146:greatest ayre, mahist.
2410:increase (n.) abzón, abzāyišn, fra- dahišnih, mehēnišn.
2411:increase (vi)  abzüdan, wālidan, waxšīdan; (vt.) mehénidan.
2698:magnify mehénidan.
2972:old kahwan, meh, pir; v. age.
3893:superior ` abar(ag)  abaragān(ag), abarīg(ān); azi&meh.
4842:Čē-ēwēnag! саһ -masāy mehtar mehtarih mehén- mehénidan mehēnišn mast mistan
4883:māzdēsn mahist, māst māzandar māš, maxš roynt
4885:mādayār mādišt mādagīh mādagīg 1*mādag mādagwar mādar Abt, mex ābgēnag! mēhan mēzd may, meh Sahrestan! ‘mahist men- moymard! menidan mënög
5543:dādwar Sy тех dādwarīh xD у мехо Чачап, gādan 19545 āy-! - ot āmadan! VV Wrens jādūgīh AD SAMA jādūg VS MAT jādag-gūwīh A yr SU jadag-gow — SP 5tex5 jadag (EI EI dādmeh +36 ONS dādestān w^ FO) Per
=== NYB mas ===
788:avdom [’pdwm] last 4415. 469, 495.20; adv. in the end, finally, ultimately 729. 10119; pat ~ id. 69; cas. obl. pat avdomeh id. 7718, — OIr *apa-tama-, borrowed in B.- Ar. ’appetom Ezr. 443; MPrs 'bdum, pd ’bdwmyy (S); Paz. awadum, awadim.
888:bägö-baxt [b'gwbht'] divine providence 777118. cf the definition Mx ch. 249-77: äsn baxt han bavēt i hac fratomeh bat Estet, u bagdbaxt hàn i dit-ic baxsend “innate bazt is that which has been allotted from the very beginning, and ~ is that which they
1283:dipivar [dpywr] secretary ŠPrs: 9. 15. Pl: 7; pl. eas. obl. —-an mahist the chief secretary 1119. 1821. 1925, — FrP 15, MS K dpywl (= dipīvar). Olr "dipi-vara- from OP dipi- ‘inscription’, BP dyp ‘document’, MPrth dyb ‘letter’ + "vara- from Av. (1360) 'var- ‘to cover, to hide, to preserve’, thus ‘he who preserves the documents’. Early contracted to dipir: Arm lw. dpir Yoxupaveóc; KZSPrth 1. 24 dpyrwpt = Prs l. 29 dpyrpt, Gr. trans- literation diBuporr, ‘chief secretary’; M PrthPrs dbyr; NP dibir, dabir (but Paz. "diver, v. next w.). Cf Bailey, BSOS VII, 1933, 76-77.
2380:mahist [mhst'] v. mas.
2469:mas
2478:mas [ms] great, big, also used as comp. (+ hac ‘than’), sup. masist [msst'] and mahist [mhst']: kū-š sok mas bit hac apürik gäv its hoofs were bigger than (those of) the other cows 49?-? (gl.); great of rank 38. 52%; ~ martin (pl. cas.
2482:mas
2483:w., pl. cas. obl. hacis-—-àn men of higher rank than oneself, one’s superiors 704; pus i ~ the eldest son 318; nātrīk i ~ the First Lady (of the harem) 4121; kunom ~ hac I shall do greater things than... 5214; pat han 1 ~ gobišn in a loud voice 4521; — masist kirpak 6971; masist rah the most excellent way 761’; dipivaran mahist the Head Scribe 1118, 1821, 19%; mahist aštak 36°; — adv. by far 977°, — Av. (1154) mas-, masan-, comp. (1156) masyah-, sup. (1155) masista-; OP *ma- Oan-, comp. *madyah-, sup. madišta-; hence in Milr: NW mas (MPrth only adv.), comp. masdtar (v. the next w.), sup. masišt (MPrth msyšt), but SW "mah . (not attested so far), comp. mahy, méh (MPrs mhy A-H I) Paz. meh, mehe, „mahi; NP mih (used as pos.), sup. mahist (MPrs mhystg ‘presbyter’ A-H II). BP has taken over NW mas as pos. and comp., and as sup. both SW mahist and NW masist, but developed, according to the SW rule: -št- > -st-, to masist, a hybrid between SW and NW. Possibly, however, -s- was pronounced -h- through- out in SW; Paz. only mahest.
2484:masatoréh [ms'twlyh] the stage of an adult, of a child who has reached maturity 6525. — Abstr. of masātar, ErP 30 ms*tl (var. mstl, mstwl, ms'twl) explained by | dát-mas ‘great of age, of mature age’. Borrowed from NW: MPrth ms’dr 'great- er, of higher rank’; the vocalisation -twl(yh) shows that it has lost its character of a comp. in SW. — Paz. mehädar through association with meh.
2485:maséh [msyh] greatness 4716,
2486:mastok [mstwk'] drunk, drunken 708. — mast, MPrthPrs mst, NP mast, pt. of Av. (1113) mad-, + suff. -ök, v. s. v. n&vakök. Paz. mastuk.
4068:welk-] great, big, high, lofty, passim; regularly placed before its head w., seldom: after (41?. 724); in titles great, chief: ~ framatar (g. v.); ~ šahridar (q.v.); — subst., pl. cas. obl. ~-dn the magnates HajA:6 [RB’n]. B:6 [welk’n]. 42. 1133, 16? [wewlg'n'], v. Christensen, Sass. 100. 110sq. — OP vazrka-; MPrthPrs wzrg; Arm. lw. vzurk, vzork, vzruk; Paz. guzurg, guzarg; NP buzurg. No comp. and sup.; for these forms meh, mahist are used; v.s. v. mas.
4221:tviščk [wSyk] distressed, to be read in this way 1912 instead of my *ny’dk'; distressful, tormenting, or the like: ni- part <i> tvišek 1079, thus to be read in- stead of nplt' w g'dk' (West: dahik). — This w. has not been recognized by Ind- ian text editors though it is found in the MSS; cf andar bimeh hac āmār u tars ~ in fright of the Reckoning and tor- menting fear DD ch. 27? (p. 49), where Anklesaria has *wyhyk' in the text, but quotes in the critical apparatus wšyk from Cod. K 35 and still another MS. This form is now confirmed beyond
6714:mastük: mastök
7257:mih (mahist): mas mihmän: mahmančh mir: mérak miyànji: miyànjikeh mizd, muzd: mizd mčbad: magu-pat mü, müy: mod muhrah: muhrak müq: mök
```


## [2026-09-07T15:57:37.303Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && python3 -c \"\nfrom PIL import Image\nim=Image.open('2002.png'); print(im.size)\nw,h=im.size\n# crop the region around the مزنا headword: OCR showed it near top-left column area; crop left half top\nim.crop((0,0,w//2,int(h*0.20))).resize((w//2*2, int(h*0.20)*2)).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2002_a.png')\nim.crop((0,int(h*0.62),w,h)).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2002_foot.png')\n\"",
 "description": "Crop BQT 2002 image"
}
```


### [2026-09-07T15:57:39.245Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-07T15:57:41.968Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2002_a.png"
}
```


### [2026-09-07T15:57:41.992Z] TOOL RESULT

```

```


## [2026-09-07T15:58:01.063Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && python3 -c \"\nfrom PIL import Image\nim=Image.open('2002.png'); w,h=im.size\nim.crop((int(w*0.05),int(h*0.60),int(w*0.98),int(h*0.72))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2002_f1.png')\n\"",
 "description": "Crop BQT 2002 footnote area"
}
```


### [2026-09-07T15:58:03.576Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T15:58:06.603Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2002_f1.png"
}
```


### [2026-09-07T15:58:06.620Z] TOOL RESULT

```

```


## [2026-09-07T15:58:34.101Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mina",
 "prompt": "Give the English etymology of \"mina\" (ancient unit of weight), and any Latin/Ancient Greek/Akkadian/Sumerian forms mentioned. Also any Akkadian manû entry details."
}
```


## [2026-09-07T15:58:35.516Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mina",
 "prompt": "Give the full etymology entry for \"mina\" (unit of weight) and if present \"mine\" as a unit of weight; note Greek mna, Latin mina, Semitic/Akkadian/Sumerian sources."
}
```


### [2026-09-07T15:58:40.658Z] TOOL RESULT

```
# Etymology of "Mina" (Ancient Unit of Weight)

## English Etymology

According to the Wiktionary entry, the English word "mina" was "Borrowed from Latin _mina_, from Ancient Greek _μνᾶ_ (mnâ, 'mna')."

## Related Forms Mentioned

The entry notes connections to other ancient weight units:
- **Biblical Hebrew**: _מָנֶה_ (māne), appearing in the related term "maneh"
- **Ancient Greek**: _μνᾶ_ (mnâ)
- **Latin**: _mina_

## Historical Context

The historical sense describes it as "a monetary unit of ancient Greece and the Middle East, originally equivalent to the weight of a mina of silver" and "a unit of weight of varying value used in the ancient Middle East, especially Babylonia, Mesopotamia and Egypt; also an ancient Greek measure of weight equivalent to 1/60th of a talent, approximately 400-700 grams."

**Note**: The provided document does not include specific Akkadian or Sumerian etymological details, nor does it contain an entry for Akkadian "manû."
```


### [2026-09-07T15:58:40.712Z] TOOL RESULT

```
# Etymology of "Mina" as Unit of Weight

Based on the provided content, there is **no etymological entry for "mina" as a unit of weight** on this page. 

The page only contains an entry for "mina" (or "mynah") as a talking starling bird from India, which derives from "Hindi _maina_ 'a starling,' from Sanskrit _madana-_ 'delightful, joyful.'"

However, the "More to explore" section does reference a related monetary unit. Under the "shekel" entry, there is a brief mention that the shekel is "equal to one-sixtieth of a mina," but this appears to be referring to the ancient Babylonian unit of measurement rather than providing its etymology.

The page does not include etymological information about:
- Greek "mna"
- Latin "mina" (as a weight)
- Semitic, Akkadian, or Sumerian origins of the unit
- "Mine" as a unit of weight

To find comprehensive etymological coverage of the mina as an ancient unit of weight and its various linguistic sources, you would need to consult additional etymological resources.
```


## [2026-09-07T15:58:47.012Z] TOOL CALL #56: WebSearch

```json
{
 "query": "Akkadian manû mina weight loanword Sumerian ma-na borrowed from Akkadian CAD"
}
```


## [2026-09-07T15:58:47.020Z] TOOL CALL #57: WebSearch

```json
{
 "query": "Frahang i Pahlavig huzvarish mzynʾ tarāzūg balance Aramaic scales"
}
```


### [2026-09-07T15:58:54.287Z] TOOL RESULT

```
Web search results for query: "Akkadian manû mina weight loanword Sumerian ma-na borrowed from Akkadian CAD"

Links: [{"title":"𒈠𒈾 - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%F0%92%88%A0%F0%92%88%BE"},{"title":"Sumerian compound-sign words - initials L through R","url":"https://www.sumerian.org/suml-r.htm"},{"title":"mina - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/mina"},{"title":"Mina (unit)","url":"https://en.wikipedia.org/wiki/Mina_(unit)"},{"title":"Ma (cuneiform)","url":"https://en.wikipedia.org/wiki/Ma_(cuneiform)"},{"title":"Sexagesimal Calculations in Ancient Sumer","url":"https://arxiv.org/pdf/2207.12102"},{"title":"On Sumerian Loanwords in Akkadian. Part I","url":"https://www.researchgate.net/publication/330696042_On_Sumerian_Loanwords_in_Akkadian_Part_I"},{"title":"mna - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/mna"},{"title":"Kajamanu","url":"https://en.wikipedia.org/wiki/Kajamanu"},{"title":"Physics:Mina (unit) - HandWiki","url":"https://handwiki.org/wiki/Physics:Mina_(unit)"}]

Based on the search results, here's what I found regarding the relationship between Akkadian manû (mina) and Sumerian ma-na:

The Sumerian ma-na (a unit of weight weighing about 500±40 grams) was possibly borrowed from Akkadian manû. The Sumerian ma-na is a unit of weight measure, mina, of approximately 500 grams (equal to 60 gín), and has been in use since the Akkadian period, with 2 ma-na equaling 1 sìla of water.

The connection is further supported by the fact that from earliest Sumerian times, a mina was a unit of weight, and by the time of Ur-Nammu (shortly before 2000 BCE), the mina had a value of 1⁄60 talent as well as 60 shekels.

It's worth noting that the borrowing direction is somewhat complex in this case, as both languages were in contact during the relevant periods. The sources indicate that the Sumerian term ma-na is considered "probably a loanword from Akkadian," though this represents contact between closely related Mesopotamian cultures and time periods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-07T15:58:56.556Z] TOOL RESULT

```
Web search results for query: "Frahang i Pahlavig huzvarish mzynʾ tarāzūg balance Aramaic scales"

Links: [{"title":"FRAHANG Ī PAHLAWĪG - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/frahang-i-pahlawig/"},{"title":"The Frahang i Pahlavîk by Junker, Heinrich F. J. (Ed.): g Paperback (1912) First edition. | ERIC CHAIM KLINE, BOOKSELLER (ABAA ILAB)","url":"https://www.abebooks.com/first-edition/Frahang-Pahlav%C3%AEk-Junker-Heinrich-Carl-Winter/12021741946/bd"},{"title":"The Frahang i Pahlavîk by Heinrich F. J. Junker on Eric Chaim Kline, Bookseller - Old and Rare Books","url":"https://www.klinebooks.com/pages/books/37176/heinrich-f-j-junker/the-frahang-i-pahlavik"},{"title":"Frahang-i Pahlavig","url":"https://en.wikipedia.org/wiki/Frahang-i_Pahlavig"},{"title":"Talk:Frahang-i Pahlavig - Wikipedia","url":"https://en.wikipedia.org/wiki/Talk:Frahang-i_Pahlavig"},{"title":"Religion:Frahang-i Pahlavig - HandWiki","url":"https://handwiki.org/wiki/Religion:Frahang-i_Pahlavig"},{"title":"huzvarishn in a sentence - huzvarishn sentence","url":"https://eng.ichacha.net/zaoju/huzvarishn.html"}]

Based on the search results, I can provide you with information about the Frahang-i Pahlavig and its related terms:

## Frahang-i Pahlavig

The Frahang-i Pahlavig is a Pahlavi dictionary and anonymous glossary of some five hundred mostly Aramaic heterograms (ideograms), in the form used by Zoroastrians in writing Middle Persian (Book Pahlavi), each explained by a "phonetic" writing of the corresponding Persian word.

## Huzvarish (Huzvarishn)

The glossary encompasses approximately five hundred Semitic language heterograms called huzwārišn, which probably means 'obsoleteness, antiquity, or archaism'. For example, the Frahang gives the huzvarishn KLB', the Aramaic consonantal text for 'dog', to be read as the Persian word for 'dog', sag.

Regarding the specific terms "mzynʾ" (possibly referring to "balance" or "scales") and "tarāzūg" - while these terms appear in your search query and relate to Aramaic scales and measurements, the search results do not contain specific information about these particular terms in the context of the Frahang-i Pahlavig. You may need to consult specialized academic sources on Pahlavi lexicography or Aramaic metrology for more detailed information about these specific glosses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T15:59:06.405Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%92%88%A0%F0%92%88%BE",
 "prompt": "Give the Sumerian entry for 𒈠𒈾 (ma-na): meaning, and the etymology statement about borrowing from Akkadian manû. Quote exactly."
}
```


## [2026-09-07T15:59:08.761Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CE%BF%CE%BD%CE%AF%CE%B1",
 "prompt": "Give the Ancient Greek etymology of Μακεδονία / Μακεδών / μακεδνός: is it derived from μακρός / PIE *meh2k- 'long, tall'? Quote the etymology and any alternative views."
}
```


### [2026-09-07T15:59:11.308Z] TOOL RESULT

```
# Sumerian Entry: 𒈠𒈾 (ma-na)

**Meaning:**
"mina, a Sumerian unit of weight, weighing about 500±40 grams"

**Etymology Statement on Akkadian Borrowing:**
"Possibly borrowed from Akkadian 𒈠𒉡𒌑 (manû)."

The source also notes in the references that this is described as "Probably a loanword from Akkadian" according to MA Powell's academic work on dimensions and weights.
```


### [2026-09-07T15:59:14.729Z] TOOL RESULT

```
# Etymology of Μακεδονία

Based on the Wiktionary content provided, the etymology section states:

**Ancient Greek Etymology:**
"From _[Μᾰκεδών](/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CF%8E%CE%BD#Ancient_Greek)_ (Măkedṓn, 'Macedonian') +‎ _[\-ῐ́ᾱ](/wiki/-%CE%AF%CE%B1#Ancient_Greek)_ (\-ĭ́ā)."

## Key Finding

The entry does **not** propose a connection to μακρός (makros, "long") or the Proto-Indo-European root *meh2k-. Instead, it traces the word as a derivative formation from the ethnic term Μακεδών (Macedonian) plus the feminine suffix -ία.

The "Further reading" section references scholarly works including Beekes' *Etymological Dictionary of Greek*, but the actual etymological analysis linking the root to Proto-Indo-European origins is not presented in this excerpt. The page focuses on the morphological breakdown rather than addressing deeper etymological debates about the ultimate origin of the Macedonian ethnonym itself.
```


## [2026-09-07T15:59:21.050Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CF%8E%CE%BD",
 "prompt": "Give the Ancient Greek etymology of Μακεδών: what root is it from (μακεδνός, μακρός, PIE *meh2ḱ-)? Quote the etymology text and any alternative/Beekes view."
}
```


## [2026-09-07T15:59:21.980Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/meager",
 "prompt": "Give the full etymology entry for \"meager\"/\"meagre\" (Latin macer, PIE root, cognates). Also quote the *mak- root entry if shown."
}
```


### [2026-09-07T15:59:26.919Z] TOOL RESULT

```
# Ancient Greek Etymology of Μακεδών

## Root and Origin

The word Μακεδών derives from **μακεδνός** (măkednós, meaning "tall, slim"), which traces back to the Proto-Indo-European root **\*meh₂ḱ-** meaning "long, slender."

## Etymology Quote

According to the source: "Related to _μᾰκεδνός_ (măkednós, 'tall, slim'), which is derived from Proto-Indo-European _\*meh₂ḱ-_ ('long, slender')."

## Related Terms

The etymology connects to several cognate words including Doric Greek μᾶκος and Attic Greek μῆκος (both meaning "length"), as well as similar roots in Latin (macer, "meagre") and Proto-Germanic (\*magraz, "lean, meager").

## Tribal Name Interpretation

The root meaning has been applied to the Macedonian tribal name, which is "commonly explained as having originally meant 'the tall ones' or 'highlanders' in Greek."

**Note:** The source does not present an alternative "Beekes view" distinct from the primary etymology—Beekes is cited as the authority supporting the μακεδνός etymology.
```


### [2026-09-07T15:59:27.507Z] TOOL RESULT

```
# Etymology of Meager/Meagre

**Main Entry:**
The term "meager" dates to the late 14c., deriving from Old French *megre/maigre* ("thin"), which came from Latin *macrum* (nominative *macer*) meaning "lean, thin." This Latin root traces back to the PIE root *\*mak-* ("long, thin").

**Key Quote:**
"lean, thin, emaciated" (of persons or animals), from Old French *megre*, *maigre* "thin" (12c.), from Latin *macrum* (nominative *macer*) "lean, thin"

**Cognates:**
Germanic languages contain related words—Old Norse *magr*, Old High German *magar*, German *mager*, Dutch *mager*, and Old English *mæger*—derived directly from the PIE root through Proto-Germanic *\*magras* rather than through Latin.

**Extended Meaning:**
The application to material things (land, food) emerged in the early 15c.

**Related Word:**
The entry notes comparison to "emaciate," which shares the same Latin root *macer* ("thin").
```


## [2026-09-07T15:59:34.270Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%86#Persian",
 "prompt": "Give the Persian entry for من: is there a sense 'a unit of weight (maund)'? Give its etymology (Middle Persian, Sanskrit manā, Akkadian, Semitic)."
}
```


## [2026-09-07T15:59:35.053Z] TOOL CALL #63: WebSearch

```json
{
 "query": "مقدونیه ریشه یونانی Μακεδονία معرب مقدونية عربی"
}
```


### [2026-09-07T15:59:40.785Z] TOOL RESULT

```
# Persian Entry for من

Based on the Wiktionary content provided, **the Persian entry does not include a sense meaning 'a unit of weight (maund)'**. 

The Persian section shows only **Etymology 1**, which covers the pronoun meaning "I/me." The article is truncated at that point, so additional etymologies or noun senses are not displayed in the provided text.

However, the **Arabic entry** (Etymology 4) does document this unit of measurement. That entry states: "a historical unit of mass – translatable as mina or maund – varying usually between ca. 1–3 kilograms."

## Etymology Information Available

The Persian etymology traces back through: "Middle Persian [character] (man, 'me (early), I (later)'), from Old Persian [character], from Proto-Iranian *ajám, from Proto-Indo-Iranian *aȷ́ʰám, from Proto-Indo-European *eǵh₂óm."

The Sanskrit and Akkadian etymologies mentioned in your question are **not present** in the Persian section shown here, though they may appear in other language sections not fully displayed.
```


### [2026-09-07T15:59:45.255Z] TOOL RESULT

```
Web search results for query: "مقدونیه ریشه یونانی Μακεδονία معرب مقدونية عربی"

Links: [{"title":"مقدونیه (یونان) - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D9%82%D8%AF%D9%88%D9%86%DB%8C%D9%87_(%DB%8C%D9%88%D9%86%D8%A7%D9%86)"},{"title":"مقدونیه (استان رومی) - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D9%82%D8%AF%D9%88%D9%86%DB%8C%D9%87_(%D8%B1%D9%88%D9%85)"},{"title":"مقدونیه - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%85%D9%82%D8%AF%D9%88%D9%86%DB%8C%D9%87/"},{"title":"مقدونیه غربی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D9%82%D8%AF%D9%88%D9%86%DB%8C%D9%87_%D8%BA%D8%B1%D8%A8%DB%8C"},{"title":"مقدونیه هخامنشی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D9%82%D8%AF%D9%88%D9%86%DB%8C%D9%87_%D9%87%D8%AE%D8%A7%D9%85%D9%86%D8%B4%DB%8C"},{"title":"مقدونیه باستان - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D9%82%D8%AF%D9%88%D9%86%DB%8C%D9%87_%D8%A8%D8%A7%D8%B3%D8%AA%D8%A7%D9%86"},{"title":"مقدونیه (ناحیه) - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D9%82%D8%AF%D9%88%D9%86%DB%8C%D9%87_(%D9%86%D8%A7%D8%AD%DB%8C%D9%87)"},{"title":"مقدونیه شمالی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D9%82%D8%AF%D9%88%D9%86%DB%8C%D9%87_%D8%B4%D9%85%D8%A7%D9%84%DB%8C"},{"title":"مقدونیه زادگاه اسکندر؛ سفرنامه، ویزا و راهنمای سفر","url":"https://www.safarnevesht.com/macedonia/"}]

بناءً على نتائج البحث، إليك معلومات عن مقدونيه وجذورها اللغوية:

مقدونيه منطقة جغرافية تقع في اليونان بالقرب من تسالونيكي في جنوب شرقي قارة أوروبا، واسمها باليونانية Μακεδονία (Makedonía).

مقدونيه ناحية جغرافية وتاريخية في شبه جزيرة البلقان في جنوب شرق أوروبا، وتشمل المنطقة اليوم أجزاءً من ستة دول: اليونان وجمهورية مقدونيا وبلغاريا وألبانيا وصربيا وكوسوفو.

بخصوص الأصل التاريخي، مقدونيه باستان كانت سرزمينًا في شمال شبه جزيرة اليونان في البلقان، وكان سكانها من نسل غير يوناني، وخليط من النسل التراقي والمتوسطي، وكانت لغتهم قريبة من اللغة اليونانية.

بخصوص المصطلح العربي "مقدونية"، فإن الكلمة الفارسية "مقدونيه" والعربية "مقدونية" هي تعريب مباشر من الاسم اليوناني Μακεδονία.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T15:59:52.757Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY مگس ===\"; grep -n \"مگس\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY مه/مهتر ===\"; grep -n \"مهتر\\|^مه \\|مِه\" incoming/ARY/ARY_pages.txt | head -8; echo \"=== ARY MAK ===\"; grep -n \"MAK\\|MEGH\\|MEG\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Aryanpur lookups"
}
```


### [2026-09-07T15:59:52.829Z] TOOL RESULT

```
=== ARY مگس ===
=== ARY مه/مهتر ===
14324:مه مهتر / ۴۳۸۳
=== ARY MAK ===
3576:ARONS, WAREN (GREEK) gh VARMAK, | :(OLD RERSIAN) dlls y+ 34
9417:JMAKA AFGHAN] (2%), sual ‘ZAMIK (PAHLAVI) «5 shy
11664:(D0) 111, (MAKE) 122 KANAG, KANAGH | :(@ALUCHD irs ay
11872:BARNHART: K’AMAK ARMENIAN) |!
13248:AMA, AMAH, EMA (PAHLAVI) Shy AHMAKEM, AHMA :(AVESTAN) ol!
13258:NASU:(OLD CHURCH SLAVIC) op 53 %+1 ASMAKA, NAS, ASMAN
13278:MAYR, MAIR (ARMENIAN) «+! MAK RURDISH) 52,5
13818:MEGA, MAGA, MUGA, MA (PAHLAVI) 65 3h,
13846:MARROW HENGLISH) galSl MEGZ, MEJU KURDISH) «53,5
13869:MUCKE GERMAN) (glsT MAKHSHI HAVESTAN) glee 3|
```


## [2026-09-07T15:59:54.023Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB magas/mes ===\"; grep -n \"magas\\|maxsi\\|Fliege\" HUB.txt | head -8; echo \"=== HUB mih/mahist ===\"; grep -n \"mahist\\|masista\\|mihtar\\|mih \" HUB.txt | head -8",
 "description": "Hübschmann lookups"
}
```


### [2026-09-07T15:59:54.078Z] TOOL RESULT

```
=== HUB magas/mes ===
348:Holle und der Fliege ist. Uebersetzt man ereyant- mit
8469:Unklar ist das Verhaltniss von np. magas 'Fliege* =
10546:magas 98, 237.
=== HUB mih/mahist ===
1122:np. mih gross : zd. masyah^, ^) hih klein : zd. kasyah-,
4021:iiber np. mih gross', ap. wa^- im sup. mat^ista-, kih *klein',
4496:mih 'gross* = paz. meh *gross, grSsser Min. Gl. 138,
4525:hih = phi. v9h zu erklSren, nicht aber mih und kih (= phi. m-£ und k^s.)
7490:Np. mih gross* = paz. meh Shk. 258, phi. ina&, ap.
8445:= zd. xsvasti- ; pist 'Mehl' = skr. pista- ; mahist (ZDM6.
8456:Shk. 257 = np. mahist (siehe oben) = ap. madista- ; balist
```


## [2026-09-07T16:00:03.792Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB 8469 ===\"; sed -n '8465,8480p' HUB.txt; echo \"=== HUB 7490 ===\"; sed -n '7485,7500p' HUB.txt; echo \"=== leaves ===\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split(\"\\n\")\nfor ln in (1122,4021,7490,8445,8456,8469):\n    print(ln, \"leaf\", \"\\n\".join(t[:ln]).count(\"\\f\")+1)\nEOF",
 "description": "Hübschmann contexts and pages"
}
```


### [2026-09-07T16:00:05.420Z] TOOL RESULT

```
=== HUB 8469 ===
arm. -sat als 2. Glied von Ortsnamen {Artasat^ Ervandasat
= Ardashir's 'Freude', Ervand's Freude), idg. kl^ySti-;
Sudan gehen*, pr. savam^ ap. asiyavam, Wrzl. cyu -=- idg.
Ic^yu.
Unklar ist das Verhaltniss von np. magas 'Fliege* =
phi. makas Gl. and Ind. 215, bal. makask = ap. ^makasa-
{= skr. ^makaga- oder '^makaska-, vgl. np. pas = ap. pasa
'hinter : zd. paskat?) zu afgh. mac^) = iran. ^maika- (oben
p. 98) und zd. *max$i, gen. maxsya, skr. maksa-, maksikil-,
Vielleicht ist arisch ^makaga- neben ^makga- anzusetzen.
Kapitel 24: ap. k.
Ap. k (= idg. k^) bleibt im Np. als k im Anlaut sowie
inlautend nach tonlosen Konsonanten, wird aber zu g nach
t5nenden Lauten. Im Aiislaut bleibt es oder wird g oder
schwindet.
§ 133. Ap. k bleibt im Anlaut und nach s, s und dem
=== HUB 7490 ===
Im Phi. erscheint hier (wie fiir ap. & = iran. ^,
arisch th, t) dasjenige Zeichen, dem ich oben § 95 den Laut-
werth ^ zugeschrieben habe und das ich im Unterschied
von dem gew5hnlichen s (fiir den Laut s = ap. s) hier
durch & umschreiben will.
Np. mih gross* = paz. meh Shk. 258, phi. ina&, ap.
sup. ma^ista- (aber zd. mas- gross , masyd 'grosser , masdh-— 211 —
*Gro8se*, dial, mas in inasmuydn *Gross-magier (Barbier
de Meynard, Diction, p. 33, Alblruni, Uebersetzung
p. 214), g. maSy semn. mestn ZDM6. 32, 538, kas. mussdr
Shuk. p. 75, kurd. masttr *gr5sser', Socin, Samml. II, 337);
kih *klein' = pfiz. keh Shk. 253, phi. ka&, also ap. *ka&U'
(aber zd. kasu-^ kasy& *kleiner, g. kasUk, semn. kes^n, ka§.
kessdr Shuk. 176, bal. kisan u. s. w.); dah zehn' = pfiz.
dah zehn , dahum der zehnte* =- phi. dahum Phi. Min. 21,
6, Bdh. Gl. 149, arm. dah-ekan (5. Jhd.) 'dgax/nfj, dtjvdgiov,
=== leaves ===
1122 leaf 45
4021 leaf 126
7490 leaf 221
8445 leaf 247
8456 leaf 248
8469 leaf 248
```


## [2026-09-07T16:00:23.340Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index 13860-13875 ===\"; sed -n '13860,13875p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== ARY pages: search MAKHSHI ===\"; grep -n \"MAKHSHI\\|MAKAS\\|MAGAS\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY مه entry 14324 ctx ===\"; sed -n '14318,14332p' incoming/ARY/ARY_pages.txt",
 "description": "Aryanpur entries"
}
```


### [2026-09-07T16:00:23.408Z] TOOL RESULT

```
=== ARY latin index 13860-13875 ===
[pdf page 475]
ok | we
‘MACKENZIE: REFERENCES beth ‘
(BRAIN) 105, (MAROW) 123 POKORNY: ~=—S*S~S*~S~«SB
Buc hy . 215 BARNHART:
tof ONIONS. (MARROW) 557 (MARROW) 635-636
“| swear: (MARROW) 363 DELAMARRE:
my _ tebb aby (MOELLE, CERVELLE) 148
BST ra |
MUCKE GERMAN) (glsT MAKHSHI HAVESTAN) glee 3|
HOLD ENGLISH) oS galS\ PAHLAVI) 5 shy,
MYGG, MYCG, MYCGE MAKHSH, MAGAS, MAKAS
MIDGE ENGLISH) gudSsi MESH, MYSH KURDISH) 53,5
MYG H(DANISH) Sails ABALUCHI) gx se
MYGG SWEDISH) al yo MAGISK, MAKASH, MAHISK
MYGG NORWEGIAN) (539 5 MECH, MAC (AFGHAN) (5-4) glsi\
=== ARY pages: search MAKHSHI ===
=== ARY مه entry 14324 ctx ===
بازگت به: ماهیچه.
پارسي باستان (2۳8۹1/۷ 0/0): ۸۸17013۸ 1
پهلوی (۳۸/4]4۲7): 310011۸36 ,110۸6 ارمنی (۸84871۸01): 101
سانسکریت (5977): ۸5 یونانی 0782/0): را
[pdf page 482]
۹
مه مهتر / ۴۳۸۳
لاتین (/712بمل): ,۸۸610 هتیت (4177778): 1106۸۰
فرائسه (ا888(/0: 3 انا
اسپانیایی (32۸15[7): دا انا پسگشت‌ها 5
ایتالپایی ((طل7): 11( و 2۶050000
آلمانی کهن ((227۵4۸ الا (ا0): 0 (0۸613) تدارا مت
لدم شا 1 (۸/8۲۸310) ۰ قل2لاقق لا
آلمانی (058۸4۸): قرده دا برهان قاطع + یدیما
یادداشت.
```


## [2026-09-07T16:00:40.523Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in مقدونیه مزنا میزنا مهست مگس; do echo \"=== $w ===\"; grep -c \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; done",
 "description": "Mo'in 2-vol greps"
}
```


### [2026-09-07T16:00:42.089Z] TOOL RESULT

```
=== مقدونیه ===
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
=== مزنا ===
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part1.txt:0
=== میزنا ===
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
=== مهست ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part2.txt:2
MON_part1.txt:0
=== مگس ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:14
MON_part1.txt:14
MON_part2.txt:24
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24
```


## [2026-09-07T16:00:43.603Z] TOOL CALL #69: Bash

```json
{
 "command": "ls site/pages/320.jpg 2>/dev/null; pdftoppm -f 320 -l 320 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320 && echo OK && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320.png",
 "description": "Render PDF page 320"
}
```


### [2026-09-07T16:00:45.381Z] TOOL RESULT

```
site/pages/320.jpg
OK
-rw-rw-r-- 1 sfmqrb sfmqrb 80891 Sep  7 12:00 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320.png
```


## [2026-09-07T16:00:49.458Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"مهست\" MON_part2.txt | head -4; echo \"=== مگس MON ===\"; grep -n \"مگس\" MON_part2.txt | head -6",
 "description": "Mo'in mehast and magas entries"
}
```


### [2026-09-07T16:00:49.528Z] TOOL RESULT

```
69481:مهست: (اعه)اکه-(02)۳00 | - مهشت. 
69485:مهستی : ])۱۱۵68 ,(22۵۱-56)1)66)61 [ف. ع. 
=== مگس MON ===
2829:غمگسار: ۲ )0 - [ع. ف. - غم گسار نده ] 
2834:اصطلاحات؛ لغ.) بادةٌ غمگسار: شرابی که 
3273:غسورمگس: 1-0 (ا.) (جاد.) 
19998:کست: ۲۵۰ ,۲۵ (ا.) زنبور عسل» مگس 
20495:مگس محفوظ نگهداشت. در صورت ابتلا 
29922:گبت: ۰«ءو (.) (جاد.) زنبور عسل» مگس
```


## [2026-09-07T16:00:55.024Z] TOOL CALL #71: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320.png"
}
```


### [2026-09-07T16:00:55.458Z] TOOL RESULT

```

```


## [2026-09-07T16:00:55.455Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T16:01:11.935Z] TOOL CALL #72: Bash

```json
{
 "command": "pdftoppm -f 320 -l 320 -r 500 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320hi.png'); w,h=im.size; print(w,h)\nim.crop((int(w*0.60),int(h*0.14),int(w*0.80),int(h*0.20))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_meh.png')\nim.crop((int(w*0.50),int(h*0.24),int(w*0.80),int(h*0.29))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_maqd.png')\n\"",
 "description": "Zoom Persian boxes on page 320"
}
```


### [2026-09-07T16:01:15.753Z] TOOL RESULT

```
4250 5500
```


## [2026-09-07T16:01:19.738Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_meh.png"
}
```


### [2026-09-07T16:01:19.752Z] TOOL RESULT

```

```


## [2026-09-07T16:01:24.829Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320hi.png'); w,h=im.size\nc=im.crop((int(w*0.68),int(h*0.175),int(w*0.80),int(h*0.205)))\nc=c.resize((c.width*3,c.height*3), Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_mezna.png')\nprint(c.size)\n\"",
 "description": "Zoom meznâ script"
}
```


### [2026-09-07T16:01:26.576Z] TOOL RESULT

```
(1530, 495)
```


## [2026-09-07T16:01:29.891Z] TOOL CALL #75: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_mezna.png"
}
```


### [2026-09-07T16:01:29.911Z] TOOL RESULT

```

```


## [2026-09-07T16:01:36.216Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320hi.png'); w,h=im.size\nc=im.crop((int(w*0.68),int(h*0.198),int(w*0.80),int(h*0.222)))\nc=c.resize((c.width*3,c.height*3), Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_mezna2.png')\n\"",
 "description": "Zoom meznâ line"
}
```


### [2026-09-07T16:01:37.952Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T16:01:41.673Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_mezna2.png"
}
```


### [2026-09-07T16:01:41.691Z] TOOL RESULT

```

```


## [2026-09-07T16:01:58.393Z] TOOL CALL #78: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_maqd.png"
}
```


### [2026-09-07T16:01:58.407Z] TOOL RESULT

```

```


## [2026-09-07T16:02:03.671Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320hi.png'); w,h=im.size\nc=im.crop((int(w*0.52),int(h*0.262),int(w*0.80),int(h*0.282)))\nc=c.resize((int(c.width*2),int(c.height*2)), Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_maqd2.png')\n\"",
 "description": "Zoom Maqdunîyyeh line"
}
```


### [2026-09-07T16:02:05.437Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T16:02:08.281Z] TOOL CALL #80: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_maqd2.png"
}
```


### [2026-09-07T16:02:08.347Z] TOOL RESULT

```

```


## [2026-09-07T16:02:08.345Z] INPUT

[Image: original 2380x218, displayed at 2000x183. Multiply coordinates by 1.19 to map to original image.]


## [2026-09-07T16:02:14.399Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320hi.png'); w,h=im.size\nc=im.crop((int(w*0.52),int(h*0.278),int(w*0.80),int(h*0.300)))\nc=c.resize((int(c.width*2),int(c.height*2)), Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_maqd3.png')\n\"",
 "description": "Zoom Maqdunîyyeh word line"
}
```


### [2026-09-07T16:02:16.011Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T16:02:19.494Z] TOOL CALL #82: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/z_maqd3.png"
}
```


### [2026-09-07T16:02:19.580Z] TOOL RESULT

```

```


## [2026-09-07T16:02:19.578Z] INPUT

[Image: original 2380x242, displayed at 2000x203. Multiply coordinates by 1.19 to map to original image.]


## [2026-09-07T16:02:32.123Z] TOOL CALL #83: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D9%85%DA%AF%D8%B3' \\\n 'https://en.wiktionary.org/wiki/%D9%85%D9%87' \\\n 'https://en.wiktionary.org/wiki/mina' \\\n 'https://en.wiktionary.org/wiki/%F0%92%88%A0%F0%92%88%BE' \\\n 'https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CF%8E%CE%BD' \\\n 'https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CE%BF%CE%BD%CE%AF%CE%B1' \\\n 'https://www.etymonline.com/word/meager' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 320 (Mâk / Mako / Mana): verification of magas, meh, mina, Sumerian mana, Makedon, meager' 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-07T16:02:35.723Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7f77ff2974ccd8fa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ad9cc73b4e26ac0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/34a0bddc104d4ee3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/724a26ba814fbae6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/89caa4fa2fa19d31.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/13da706ecad297ce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06852d2a8b308072.txt
```


## [2026-09-07T16:02:46.623Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '35470,35492p' LAT.txt; echo \"=== SNS entry ===\"; sed -n '13505,13520p' SNS.txt",
 "description": "Ernout-Meillet macer; SNS maxš entry"
}
```


### [2026-09-07T16:02:46.682Z] TOOL RESULT

```
lotas <h> ortorum et castelli f macelli - , cf. Goetz-Schoell ad loc.
Emprunt ancien au grec. Hesychiua donne jiooceXa* (ppa^arax, Spucpotxoi,;
liooteXoC • Spucpaxxoc. Le mot grec est lui-meme emprunte au semitique.
macer, -cra (-cera Ital.), -erum: maigre. Ancien, usuel. Panro-
man (et germanique?). M.L.5303.
Derivas: maceo,-es "macie infestari" (Plaut. ), rare; macor,-oris m.
(Pacuvius), maciSs (class.); macilentus (arch. et postclass.) sana
doute d'apros gracilentus; macio,-as Itardif) qui aemble posterieur
a emacid (Col.Plin.); macellus (Lucii.), macriculus (Varr.); macritudo
(Pl .), macritas (Vitr.)j permacer, permaceo (Enn.); macescS, emacescS- 669 ~
machina.
(formd 8ur maces) et maqrSscd,-is (formd sur macer), M.L.5310, ema-
cr&scQ (Celse); mace fac id (Evagr.).
II n'y a pas d’adj. madidus; macor est a peine attestd, de m£m‘e
lea diminutifs nape Ilus, macriculus) le substantif usite eat macies ,
qui a triomphd, peut-etre gr$.ce a. l f appui de tabSs, de sena voisin.
Lea Latina dtablissaient une parenti entre macer et mScerS, comme on
le voit par lea gloaea: macer, Xeuxoc,, et macero , Xeraruvo) ( 4 . cotd
de (icxpauvu)). La parenti n’existe pas plus qu'elle n f existe entre cdrus
et c&res.
Cf. hitt.mafelant-"minee" (v. Benveniste SSL XXXIII p.140); gr. [Uxxpoc
"long", oh l*a reprdsente i.-e. 9, comme on le voit par le substantif
dor. yJxHOQ, ion.-att. p,TpcoS "longueur"; pour le sena, ef. (j,axe8voC "long,
=== SNS entry ===


10 



.,j-£« :maxs: -*0-"^ 
l**>»j UiW>. 1112)maksika- : ^j*- maxsl-: fc. 

*T/**S Henning. BSOS. IX. 1, p. 85. 



>u"&.* 'j^^-i :maxs par: ^W-*o-j-^
```


## [2026-09-07T16:04:02.218Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg320.png data/verification/sources/refs/ocr/BOOK/320.png && cat > data/verification/sources/refs/ocr/BQT/2002.vision.txt <<'EOF'\n[read from the page image data/verification/sources/refs/ocr/BQT/2002.png — Borhan-e Qate', ed. Mo'in, printed page 2002 (header \"-۲۰۰۲-\" visible at the top of the leaf)]\n\nHeadword (last entry of the right-hand column, running over into the left column,\nbetween «مزمل» and «مزنده»):\n\n  مِزنا (۵) - بکسر اول و سکون ثانی و نون ... بالف کشیده ، بلغت زند بمعنی ترازو باشد\n  و بعربی میزان گویند .\n\n  [i.e. \"mezna: with kasra on the first letter, sukun on the second and a nun ...,\n  with a long alef; in the Zand language it means 'balance/scales', and in Arabic\n  they say mīzān.\"]\n\n  N.B. the printed headword is «مِزنا» (mim + kasra, zā, nun, alef) — there is NO yā;\n  the vowel is written only as the kasra diacritic.\n\nMo'in's etymological footnote 5 on the same page (bottom of page, first footnote line):\n\n  ۵ ـ هز . mazînâ ، maznâ . پهلوی tarâzûk ( ترازو ) ، یونکر ص ۱۱۷ ،\n     قس : میزان (عر) .\n\n  [i.e. \"5 — huzvāreš (هز. = هزوارش, Aramaic heterogram) mazînâ, maznâ;\n   Pahlavi tarâzûk ('balance'), Junker p. 117; compare Arabic mīzān.\"]\n\nNeighbouring footnote 10 (for مزیدن), quoted here only to show the footnote numbering:\n  ۱۰ـ پهلوی mîzhim ، کردی micîtan ، mîtin ( مکیدن ) ، بلوچی micag ، mishagh ( مکیدن ) .\n     از ریشهٔ meq/c_ ( مکیدن ) ، اسشق ۹۷۹ ، هوبشمان ...\nEOF\necho written; ls -la data/verification/sources/refs/ocr/BOOK/320.png data/verification/sources/refs/ocr/BQT/2002.vision.txt",
 "description": "Save vision transcription and book page image"
}
```


### [2026-09-07T16:04:03.694Z] TOOL RESULT

```
written
-rw-rw-r-- 1 sfmqrb sfmqrb 80891 Sep  7 12:04 data/verification/sources/refs/ocr/BOOK/320.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1505 Sep  7 12:04 data/verification/sources/refs/ocr/BQT/2002.vision.txt
```


## [2026-09-07T16:04:26.134Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i -E \"FVQ|AFM|PLA|LKT|AFA|WEB|FSD\" ; echo \"---\"; for f in FVQ.txt AFM.txt PLA.txt LKT.txt; do [ -f $f ] && { echo \"== $f mina/man/maqdun ==\"; grep -n -i \"mina\\b\\|manā\\|مقدون\\|منا\" $f | head -4; }; done",
 "description": "Check Semitic reference files"
}
```


### [2026-09-07T16:04:27.439Z] TOOL RESULT

```
AFA.txt
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
FVQ_pages.txt
FVQ.txt
LKT.txt
WEB_vol1.txt
---
== FVQ.txt mina/man/maqdun ==
380:Ubersicht uber die Bildung der Nomina. Gottingen, 1889. 
4258:ties in the way of this. Lidzbarski, ZR, i, 86, would make it a denomina- 
5177:being found also in Amharic, Tigre, and Tigriiia, meaning light, illumina- 
7047:and Tarafa, Mrfalkiqa, 38. The sense of to reap, however, is denomina- 
== AFM.txt mina/man/maqdun ==
375:( الاوسينداج والاوسفيداج ) بياض.الرضاص 3 تعريب سيد نلك وممناء” 
484:+ (الأمد) يقال ما أمدك 35 5 7 امد ومعناها الزمنان 
820:انان حشدثة دققة نشه 4 الرطنة تكن قضنامنا خر 
1259:واعل منة < 5 ححط» اي باب العين ويوافقة اللاتيني هالتمنام 
== LKT.txt mina/man/maqdun ==
282:Einheitsnomen  "agamt  'Barbar,  Fremder, Nichtaraber',  besonders  'Perser'.  Tk. agemi;  hieraus  rum.  agemiu,  ageamiü 'unbewandert,  Anfänger';  poln.  (alt)  ad- ziamski  'persisch'  in  Verbindung  mit Substantiven  wie  'Teppich,  Kostüm, Sattel'.  —  Altit.  agemina,  mittelfrz.  aze- mine  'Ziselierarbeit'.  Das  sp.  aljamia, lengua  aljamiada,  bezeichnet  die  Sprache der  Moriscos,  zu  deren  Eigentümlich- keiten es  gehörte,  daß  in  ihr  viele arabische  Ausdrücke,  z.  T.  mit  spanischer Endung,  sowie  Arabismen  und  alt- spanische Wörter  vorkommen,  die  sonst schon  außer  Gebrauch  gekommen  waren. Da  diese  Sprache  mit  arabischer  Schrift geschrieben  wurde,  sind  textos  aljamia- dos  also  spanische  Schriftstücke,  die arabisch  geschrieben  sind,  z.  B.  das Poema  de  Yosuf,  vgl.  Ad.  Zauner,  Alt- spanisches Elementarbuch. ^  Heidel- berg 1921.  S.  155.  [DE  145.  ML  298. ZromPh  XXXIl,  41.  XXXIII,  62.  Kar- lovvicz  435.
851:293.  Hebr.  b§s§m: 'Balsamstaude,  Balsam',  eine  Handels- ware, welche  die  Griechen  nebst  dem Namen  von  den  Phöniziern  erhielten. Gr.  ßd\aa|nov,  lat.  balsamum;  hieraus  it. balsamo,  balsimo,  asp.  blasmo,  sp.  pg. balsamo,  prov.  balme,  frz.  bäume  [aber pikardisch  bäm  'Minze'],  rum.  baisam; dtsch.  Balsam,  ndl.  balsem,  engl,  bahn; russ.  bal'sam,  bulg.  serb.  poln.  baisam, cech.  baisam,  balzam.  —  Aus  demselben Grundwort  mlat.  bisamum,  dtsch.  Bisam, cech.  poln.  pizmo  'Moschus'.  —  Vgl. noch  Balsamine,  Impatiens  Balsamina, engl,  halsamine,  baisam.  [Kluge  34  u. 54.  G.  Schvveinfurth,  Über  Balsam  und Myrrhe  1893.
1239:jeanne  [mit  volkrielyinologischer  Umge- stalluug],  sp.  dainajuana,  kat.  damajana; engl,  demi-john  'Korbflasche'.  Der  ge- naue Gang  der  gegenseitigen  Entleh- nungen ist  noch  nicht  klargestellt,  da- her sind  zahlreiche  andere  Etymologien aufgestellt  worden,  die  aber  weit  weniger befriedigen  [aus  lat.  dimidiana,  aus lat.  domina  und  galbma  >  frz.  dame und  jaune  u.  a.  m.].  [Devic  DEt  101/102. Lammens  Rem  94/95.  RomForsch  III, 497.    ZfromPh  II,  35i2.
1827:'Schiffstau,  Seil';  hieraus  mit  partieller Assimilation  der  Liquida  l  ait.  gumina, it.  gomena,  sp.  pg.  gümena,  frz.  goumhne, gumhie  'Ankerlau'.  —  [Die  Form  ar. gainal  ML  3666  paßt  wegen  der  Voka- lisation lautlich  nicht.]
```


## [2026-09-07T16:04:37.083Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"المن\\b\\|( المن )\\|(المن)\" AFM.txt | head -5; echo \"=== WEB mina ===\"; grep -n -i \"mina, n\\..*weight\\|mina.*Gr\\. mna\\|mna\\b\" WEB_vol1.txt | head -5; echo \"=== FSD mina ===\"; grep -n \"mina\" FSD_vol3.txt 2>/dev/null | head -5",
 "description": "Addi Shir, Webster, F&W checks"
}
```


### [2026-09-07T16:04:37.183Z] TOOL RESULT

```
259:( 5:01 قال £ حيط 1 ܫܐ ݇( 1 3.15 الذى £ 0501 المنطقة وما 
461:وقال !)ܝܣ : هو دواء هندي يشبه المندق الاان فيه ;; ,80 قليلا الى الغسبرة ما هو 
662:(المبر) الأسد المندي 5 في شفاء 0 +ابر جسن :من السماع دخيل في 
1122:الخبار المندي وهو المعروف عند الاطاء طرثوث رب الأرض ولت ٠‏ الرياح. 10 4 
1147:( المنحكشت ) فاسي محض وهو القرتقل ٠‏ والق رنمل تعر نب 70.007 1000100010 
=== WEB mina ===
7191:r riv., and anér, andros, mna] in botany, without stamens: said of
21033:blie’point/ér, n.a shark, Lamna glauca, of the
21492:boll’worm, n. the larva of the mot ture bo armigera, which ravages the imna
23936:dock, broad’spread (-spred), a. widespread. broad’spread/ing, a. spreading widely. broad/stone, n. same as ashler. broad/sword (-sord), n. a sword with a broad blade and a cutting edge. _ $ broad’tail, n, 1.a thick-tailed sheep of Asia Minor; karakul. 2. the flat, wavy pelt of its lamb; astrakhan. _ 3. any parrot of the genus Platycercus, with broad tail feathers. : broad’throat, 7. a broadbill (sense 3). broad/-tread (-tred), a. having a wide face; as, a broad-tread car wheel. x Broad/way, n. [from Broadway, a street in = New York City, known for its theaters, etc.] the New York commercial theater or enter- tainment industry, or its life, world, etc. broad/wise, adv. in the direction of the breadth, brob, n. a specially shaped spike used to hold an abutting timber in place. $ Brob-ding-nag/i-an, a. eon Brobdingnag, a country of giants, in Swift's Gulliver's Travels.| igantic; of great height. | Bro! Snemna tn, n. a giant. bro-cade’, n. (Sp. brocado, from LL. brocare, to embroider, stitch.] a rich cloth with a raised design woven into it, as of silk, velvet, gold, or silver. X bröçäde’, v.t.; brocaded, pt., pp.; brocading, ppr. to weave a raised design into (cloth). bro-cad’ed, a. 1. woven like or into brocade. 2. decorated or covered with brocade. bro-cade’ shell, a parti-colored cone shell, Conus geographicus. bro/cage, n. see brokerage.
37390:series ot columns; L. columna, a column.]} in
=== FSD mina ===
1501:or suborder of wglthognathous birds with the terminal or
1616:crog'ra-phy, a 1. Examination with the unaided eye' op-
2052:The domination of the eprishUy Julae
2209:loclcal seminary (Methodist Eplooupal). founded In 1800
2270:(It., <L mea domina, see madam] manlon'at.- ma^*
```


## [2026-09-07T16:07:13.255Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"SKT Macedon:\"; grep -c -i \"macedon\" SKT.txt; echo \"SKT meagre entry:\"; sed -n '9448p' SKT.txt; echo \"IEC maksa/fly:\"; grep -n \"maksa\\|maks-\\|mak-o\\|gnat\\|midge\" IEC.txt | head -6; echo \"AHD fly root:\"; grep -n -i \"gnat\\|midge\\|Fly\\.\" AHD_watkins1985.txt | head -5",
 "description": "Skeat, Mann, AHD final checks"
}
```


### [2026-09-07T16:07:13.342Z] TOOL RESULT

```
SKT Macedon:
0
SKT meagre entry:
:k .  KofT ;  se«  Shear. ^H«'^.;      Heb   yahM^ith.  or, ly,  yakavth,  ( iod  ,  see  article of  the  Bible, meagre.    (L.)    X^  iWif r.diy.
IEC maksa/fly:
44:In his Grammatica linguae Anglicanae, dated 1651, Dr. Wallis correctly equated 37 English words with their Latin and Greek cognates. These were reproduced by Dr. Samuel Johnson in the fifth edition of his Dictionary of the English Language (1773) with a comment as follows, translated from Wallis's Latin:
718:arnu-mi (arneu-mi, ornu-, rnu-) 'strive for, reach, get’. WP I, 77 Skt. rnómi (get, reach" For other senses see ornu-); Arm. arnum, aor. ari ‘get, receive"; v-aranem ('seize', fr. *apo-ar-); cf. ar ‘seizure’; v-ar ('armour', but see armn- above); Gk. árnumi, árnumai; Ir. cf. i-arraim ‘seek, want, ask); OHG arnon ‘get; MHG er-arnen (id. and ‘garner; earn; rescue); OE earnian; ON árna (1) ‘get, earn’. (The Gmc. forms are ambig.; for alternatives see Feist GEW and Holthausen AEEW). A doubtful cognate is Hitt. harnaus (“harnus? '*birthchair, lit. ‘re- ceptacle'?) ('arnu-)
905:(N.B. Words containing IE *-b- are far fewer than those with IE *-bh-. A degree of am- biguity arises with alleged cognates from Iranian, Albanian, Celtic, Baltic and Slavon- ic, and especially with citations from Hit- tite and Tokharian, where (initial) *p, *b and *bh are represented similarly).
945:bimbos, å (?) Skt. bimbah, am “disc, mirror, picture; lizard’; bimba ‘red gourg’; It. bimbo, bimba ‘infant’; SEGer. Pimpf 'youngster; LG cf. pimps ‘youngster, midget’; EME cf. pimping “tiny, puny’
1897:bhŭið, bhuiið “bring into being; become, be’. WP II, 141. Skt. bhūyé, Av. buye :Gk. phúð, phuío; Alb. bij ‘sprout, grow’; mbij, id. (fr. *en-bhuiio); beside buj “quarter; lodge’; Lat. fio, fieri; (Osc. Diet 3pl.), cf. (probably) im-buo ‘impregnate’; Ir. bia, biad (impers. ‘will be’), W byddaf, 3s bydd; OBr. bi ‘will be’; OE būan, büian ‘dwell’; ON búa beside byggva ‘dwell; populate’; Latv. biju ‘I was? beside da-būju (‘reach’: ON búa, id.); OCS cf. bije ‘substance’ beside by (3s. ‘was’). (For Lat. -bundus (mira-, vaga-, mori-) cf. im-buð (lit.? ‘cause to be’)). See bhū-
2592:(dupio ‘dive, duck, enter”. Only Gk. in z-gde. See doup-) Gk. düpto, id.; düptes 'diver. O-gde in G zaufen (‘walk backward', cf. Gk. doüpos *arse"), and in Big. dung ‘enter’. (The G form represents a form *doub-, with uncertain cognates in Sl. Celt. & Li.)
AHD fly root:
67:All of these forms, spoken of as cognates, provide evidence for the phonetic shape of the prehistoric Indo-European word for “daughter-in-law” that is their common an- cestor. Sanskrit, Germanic, and Slavic agree
121:(INEBRIATED), was without etymology until a cognate turned up in the Hittite verb meaning “to drink”; both are derived from the root 6g”h-.
125:The cognate languages give evidence for demonstrative and interrogative pronouns. Both have also developed into relative pro- nouns in different languages. The most per- sistent and widespread pronominal stems are to- and k“o-, which are preserved in the English demonstrative and interrogative- relative pronouns and adverbs beginning with th- (THIS, THEN) and wh- (WHO, WHICH, WHEN).
131:The other celestial bodies recognized were the sun, sawel-, and the stars, ster-3. There is evidence from several traditions for similar designations of the constellation Ursa Major, though these may not go back to the earliest Indo-European times. The movement of the sun dictated the names for the points of the compass. EAST is derived from a verbal root aus-', “to shine,” as is the word for “dawn” (Latin Aurora), divinized since Indo- European times on the evidence of Greek, Lithuanian, and Sanskrit. The setting sun furnished the word for “evening” and “west”:
137:A word for the earth can be reconstructed as dhghem- (*dheghom). Other terms of lesser distribution designated forest or uncul- tivated land, like kaito- and welt- (wILD). Swampy or boggy terrain was apparently also familiar, from the evidence of the roots sel-es-, pele-', and *mdno-. But since none of these runs through the whole family, it would not be justifiable to infer anything from them regarding the terrain of a hypo- thetical original homeland of the Indo- Europeans.
```


## [2026-09-07T16:17:43.476Z] TOOL CALL #89: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-320.json <<'JSONEOF'\n{\n  \"pdf_page\": 320,\n  \"book_page\": 290,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Mâk\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *meh₂ḱ- (older notation *māḱ- : *məḱ-) 'long and thin, slender', with the derivative *m̥ḱrós 'long'\",\n      \"note\": \"Pokorny IEW 699 carries this root verbatim: 'māḱ- : məḱ- „lang und dünn, schlank“; m̥ḱrós ds.' — the language label (Indo-European) and Nourai's gloss ('long, thin, slender') reproduce Pokorny word for word, and Watkins/AHD prints the same as 'māk-. Long, thin.' In current laryngeal notation the root is *meh₂ḱ-. Nourai's added note 'This root may be related to \\\"Meg: great\\\"' is itself well founded rather than a hedge: on the very same Pokorny page it is said that Av. mas- stands for the expected *mə̄s- '*mas- für *mis- aus idg. mə̄s- durch Einfluß von mazyā „größer“ : μέγας', i.e. the comparatives of *meh₂ḱ- 'long' and of *méǵh₂- 'great' contaminated each other already in Avestan — which is exactly why the Persian descendants of the two roots (meh, mehast) are hard to keep apart and why Wiktionary assigns مه to the other root (see node #2).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *meh₂ḱ- (در نگارش کهنِ پوکورنی *māḱ- : *məḱ-) به معنی «دراز و باریک، کشیده» است و مشتقِ *m̥ḱrós از آن ساخته شده. پوکورنی در صفحهٔ ۶۹۹ عیناً همین ریشه را با همین معنا آورده و واتکینز (AHD) نیز آن را «māk-: long, thin» ثبت کرده است؛ پس نامِ ریشه، برچسبِ زبان و معنایی که نورایی داده هر سه درست است. یادداشتِ نورایی که «این ریشه شاید با ریشهٔ Meg: great پیوند داشته باشد» نیز پذیرفتنی است، زیرا پوکورنی در همان صفحه می‌گوید صورتِ اوستایی mas- به جای *mə̄s- زیرِ تأثیرِ mazyah- «بزرگ‌تر» (از ریشهٔ *méǵh₂-) پدید آمده است؛ یعنی صیغه‌های تفضیلیِ این دو ریشه از دورهٔ اوستایی درهم آمیخته‌اند. ادعای نورایی دربارهٔ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CF%8E%CE%BD\",\n        \"https://www.etymonline.com/word/meager\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:699\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 361 (printed p.699, the page number '699' is printed on leaf 360): 'māk- : mok- „lang und dünn, schlank“; məkrós ds. — Av. mas- „lang“, Komp. masyā „der größere“, Sup. masista-, ap. maθ-išta- „der höchste“, av. masah- n. „Länge, Größe“ ... gr. μῆκος, dor. μᾶκος n. „Länge“, Μάκετα „Hochland“, Μακεδόνες daher „Hochländer“, μακεδνός „schlank“, μακρός „lang“ (= lat. macer, dt. mager) ... lat. macer, -cra, -crum „mager“ ... WP. II 223 f., WH. II 2.' Grep pattern: grep -n 'makros|mager' POK_full.txt -> line 57575, 'Page(s): 699'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 223 f. (incoming/WLD/WLD_Bd2_pages.txt line 14588)\", \"stance\": \"supports\", \"note\": \"'mak-:mok- „lang und dünn, schlank“. mákros. — Ay. mas- „lang“, Komp. masyā „der größere“, Sup. masišta-, ap. maθišta- „der höchste“, av. masah- n. „Länge, Größe“ ... Lat. macer, -cra, -crum „mager“, maceo, -ere „mager sein“, macies „Magerkeit“. Ahd. magar, ags. mæger, aisl. magr „mager“.' This is the WP II 223f. that Pokorny 699 cites.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. māk- (AHD_watkins1985.txt line 720)\", \"stance\": \"supports\", \"note\": \"'māk-. Long, thin. 1. Zero-grade form *mək- becoming *mak- in suffixed form *mak-ro- in: a. Latin macer, thin: MAIGRE, MEAGER; EMACIATE; b. Greek makros, long, large: MACRO-, MACRON; AMPHIMACER. 2. Suffixed form *māk-es- in Greek mēkos, length: MECOPTERAN, PARAMECIUM. [Pok. māk- 699.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, cols. ~728 (IEC.txt lines 10282, 10284)\", \"stance\": \"partial\", \"note\": \"Mann splits the material: one entry gives 'Hitt. maklanc, makla- „lean, thin“; Gk. makrós „long“; Lat. macer, f: macra „lean; barren“; OHG magar, OE mæger, ON magr „lean“', and a separate lemma 'mak- (variant of mak- (3)?, cf. makrós) Av. mas „wide, big“; masō, gs -āh- „size“; Gk. cf. másson „bigger, more, longer, further“' — same forms, but he is not sure the Iranian and the Greek/Latin belong to one lemma.\"},\n        {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. macer (LAT.txt lines 35473-35492)\", \"stance\": \"supports\", \"note\": \"'macer, -cra, -erum: maigre. Ancien, usuel. Panroman ... Cf. hitt. maklant- „mince“ (v. Benveniste BSL XXXIII p.140); gr. μακρός „long“, où l'a représente i.-e. ə, comme on le voit par le substantif dor. μᾶκος, ion.-att. μῆκος „longueur“; pour le sens, cf. μακεδνός „long“ ...'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"mas; masah; mas-yâ 2; mas-yah; mas-išta; math-išta\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six forms are one Old Iranian paradigm built on *meh₂ḱ-. Av. mas- 'long, great' is the positive (used in Middle Iranian also as a comparative); masah- n. 'length, size' is the s-stem abstract *maḱ-es-, the exact formation of Gk. mêkos/Dor. mâkos 'length'; masyah- 'greater, longer' is the comparative *maḱ-yos- (nom. sg. masc. masyā̊) — Nourai's 'mas-yâ 2' and 'mas-yah' are one and the same word cited twice, once in the nominative and once as the stem; masišta- 'greatest, longest' is the superlative *maḱ-isto-. Old Persian shows the regular South-West Iranian outcome of Proto-Aryan *ś (< PIE *ḱ) before a dental, namely θ: maθišta- 'greatest, supreme', which is the standing epithet of Ahuramazda in the inscriptions (hya maθišta bagānām 'the greatest of the gods', DPh, DEa, XPh) and in XPf designates the heir apparent. Kent derives it exactly as the chart does ('superl. to pIE *mak-ros ... pIE root *mak- „be long and slender“ + superl. suffix -išta-'), and Buck lists the whole set under 'large, big'. Nourai's 'math-išta' writes θ as 'th'; the form is right.\",\n          \"derivation_fa\": \"این شش صورت، همه اجزای یک صرفِ ایرانی باستان از ریشهٔ *meh₂ḱ- هستند: اوستایی mas- «دراز، بزرگ» (ساده)، masah- (نامِ مصدرِ ستاکِ -s) «درازی، اندازه» از *maḱ-es- که هم‌ساختِ یونانی mêkos است، صفتِ برترِ masyah- (نهادیِ مفردِ مذکر masyā̊) «درازتر، بزرگ‌تر» از *maḱ-yos-، و صفتِ برترینِ masišta- از *maḱ-isto-. در پارسی باستان، *ś ایرانی (< ḱ هندواروپایی) پیش از دندانی به θ بدل شده و maθišta- «برترین، بزرگ‌ترین» را داده که در سنگ‌نوشته‌ها لقبِ اهورامزدا است (hya maθišta bagānām «بزرگ‌ترینِ خدایان») و در کتیبهٔ XPf به معنی «ولیعهد» به کار رفته. آنچه نورایی «mas-yâ ۲» و «mas-yah» نوشته در واقع یک واژه است که دو بار، یک بار در حالتِ نهادی و یک بار به‌صورتِ ستاک، آمده است. کِنت و باک هر دو همین صرف را می‌آورند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CF%8E%CE%BD\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:699\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 361: 'Av. mas- „lang“, Komp. masyā „der größere“, Sup. masista-, ap. maθ-išta- „der höchste“, av. masah- n. „Länge, Größe“' — every one of Nourai's forms, in Nourai's order.\"},\n            {\"ref\": \"KNT:201\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon s.v. maθišta- (KNT.txt line 5761, leaf 226-227, the 'm' stretch of the Lexicon, pp. 201-202): 'maθišta- adj. „greatest“, equal to „crown prince“ in XPf ...: Av. masišta-, NPers. mahist, Gk. μήκιστος „longest“ (radical vowel after that in μῆκος „length“); superl. to pIE *mak-ros, Gk. μακρός, Lt. macer „thin“, pIE root *mak- „be long and slender“ + superl. suffix -išta-'. Kent §117 adds 'OP maθišta- „greatest“, Av. masišta-, Gk. μήκιστος „longest“' as his example of pAr. ś > OP θ.\"},\n            {\"ref\": \"SYN:880\", \"status\": \"supports\", \"note\": \"Buck, Selected Synonyms 12.55 'large, big (great)', printed p.880 (SYN.txt leaf 952): 'Av. masan- „great, significant“, masit-, masita- „great, large“, masyah- „greater“, masišta-, OPers. maθišta- „greatest“, beside masan- „greatness, importance“, masah- „length, size“, and mas- „long“ : Grk. μακρός „long“ (12.57). Walde-P. 2.223. Barth. 1154 ff.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiran. Wb. cols. 1154-1156 (cited as such by Nyberg and Buck); BRT.txt lines 6486, 7086, 10910\", \"stance\": \"supports\", \"note\": \"Bartholomae's own columns are hard to reach in this OCR, but the derived compounds are legible and attest masah- 'Größe' directly: 'j. asti.masah- Adj. „von der Grösse einer A[hle]“' and 'j. ā.gaošō.masah- Adj. „dessen Grösse zum Ohr geht, so gross wie man es beim Ohr trägt“' (V. 13.30, Ā. 9.5), and masišta is quoted repeatedly in running text ('ratavō vīspe masišta', 'masišta xšnaoma'). Buck (SYN:880) and Nyberg both cite 'Barth. 1154 ff.' / 'Av. (1154) mas-, (1156) masyah-, (1155) masišta-' for these entries.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.122-123 s.v. mas (NYB_vol2_glossary.txt lines 2478-2483)\", \"stance\": \"supports\", \"note\": \"'mas [ms] great, big, also used as comp. ... sup. masist [msst'] and mahist [mhst'] ... — Av. (1154) mas-, masan-, comp. (1156) masyah-, sup. (1155) masišta-; OP *maθan-, comp. *maθyah-, sup. maθišta-; hence in MIr: NW mas ..., sup. masišt (MPrth msyšt), but SW *mah (not attested so far), comp. mahy, mēh ..., NP mih (used as pos.), sup. mahist.'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, entry 'mak- (variant of mak- (3)?, cf. makrós)' (IEC.txt line 10284)\", \"stance\": \"partial\", \"note\": \"'Av. mas „wide, big“; masō, gs -āh- „size“; Gk. cf. másson „bigger, more, longer, further“. (Other forms ambig. See mak- (3))' — Mann has the Avestan forms but flags the connection to the Greek/Latin lemma as uncertain.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"meh 2 «مه ۲»; mehast «مهست»; meznâ «میزنا»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the three words belong here; the third does not, and Nourai's own reference says so. (a) NP مِه meh 'great, greater' and (b) مِهست mehast/mehest 'greatest' do continue this root. Middle Persian inherited the North-West positive/comparative mas and the South-West *mah, comp. mahy > mēh, sup. mahist; Nyberg sets it out in full (see consulted) and MacKenzie's dictionary has 'meh [ms | M mhy, myh, N ~] great(er), old(er)' and 'mahist [msst', mhst' | M mhyst, N ~] greatest'. Phonetically: Old Iranian intervocalic -sy- of masyah- gave South-West MP -h-, so *mahyah > mah/mēh > NP meh, and the superlative masišta- gave mahist > NP mahist/mehest, i.e. Nourai's mehast — the form in the Ferdowsi line he quotes (ز شاه جهاندار خورشید دهر / مهست و سرافراز و گیرنده شهر). Horn no. 999 and Mo'in's footnote to Borhan-e Qate' p.2058 give exactly this. English Wiktionary instead derives مه from Proto-Iranian *majā́ < PIE *méǵh₂s 'great'; that is a real minority position, but the Iranological tradition (Horn 1893, Hübschmann 1895, Nyberg 1974, MacKenzie 1971, Moʿin) is unanimous for mas-/maθišta-, and Pokorny 699 already explains the crossing of the two paradigms in Avestan, so Nourai's chart plus his cross-reference to 'Meg: great' is the better description. (c) مِزنا meznā 'balance, scales' has nothing to do with this root. Nourai's own cited page prints مِزنا and Moʿin's footnote 5 reads 'هز. mazînâ، maznâ. پهلوی tarâzûk (ترازو)، یونکر ص ۱۱۷، قس: میزان (عر)' — that is, it is a huzvārišn, one of the Aramaic heterograms of the Frahang ī Pahlavīg (Junker p.117) written <mzynʾ> and read out as Pahlavi tarāzūg 'balance'. The word is Aramaic, from the common Semitic root w-z-n 'to weigh' (Heb. mōznayim, Arab. mīzān — precisely the comparison Moʿin draws), not Iranian mas- 'long, great'. Nourai's own note that meznâ 'was not found in MON' is correct: the Moʿin text on disk has no such entry, though it does have مهست. Separately, the JSON's Persian script for this word, «میزنا», is not what the book prints: the printed page has «مِزنا», with the vowel written only as a kasra under the mīm.\",\n          \"derivation_fa\": \"از سه واژهٔ این خانه، دو تا درست‌اند و یکی نادرست. «مِه» (بزرگ، بزرگ‌تر) و «مِهست/مِهِست» (بزرگ‌ترین) به‌درستی از همین ریشه‌اند: در فارسی میانه صورتِ شمالِ‌غربیِ mas و صورتِ جنوبِ‌غربیِ *mah با صفتِ برترِ mahy > mēh و برترینِ mahist در کار بوده است. از نظر آوایی، -sy- ایرانی باستان در فارسی میانهٔ جنوبِ‌غربی به -h- بدل شده و از masyah- اوستایی صورتِ mah/mēh و سپس «مِه» فارسی نو، و از masišta- صورتِ mahist و «مهست» به دست آمده؛ همان صورتی که در بیتِ فردوسیِ نقل‌شده در نمودار آمده است. هرن (شمارهٔ ۹۹۹)، هوبشمان (صفحهٔ ۲۱۱)، نیبرگ، مکنزی و حاشیهٔ معین بر برهان قاطع (ص ۲۰۵۸) همه همین را می‌گویند؛ ویکی‌واژه «مه» را به ریشهٔ دیگر (*méǵh₂s «بزرگ») می‌برد که نظرِ اقلیت است و پوکورنی خود درآمیختنِ این دو صیغه را در اوستایی توضیح داده است. اما «مِزنا» به معنی «ترازو» هرگز به این ریشه تعلق ندارد: در همان صفحهٔ ۲۰۰۲ برهان قاطع که نورایی به آن ارجاع می‌دهد، حاشیهٔ ۵ معین می‌نویسد «هز. mazînâ، maznâ. پهلوی tarâzûk (ترازو)، یونکر ص ۱۱۷، قس: میزان (عر)»؛ یعنی این واژه یک هزوارش است — از هزوارش‌های آرامیِ فرهنگِ پهلویگ که <mzynʾ> نوشته و tarāzūg خوانده می‌شد — و از ریشهٔ سامیِ و-ز-ن است (عبری mōznayim، عربی میزان). پس این بخش از ادعای نورایی را پژوهشِ امروزی و حتی مرجعِ خودِ او رد می‌کند. افزون بر این، املای «میزنا» در داده‌های استخراج‌شده با چاپِ کتاب نمی‌خواند: در صفحهٔ چاپی «مِزنا» آمده و آن «ی» در واقع کسرهٔ زیر «م» است — خطای خوانشِ اسکن.\",\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"مِزنا\",\n          \"correct_form\": \"مِزنا (meznā)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:224\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 999, printed p.224 (HRN.txt leaf 246): 'mih „gross“, mehist, mihīn, mihtar. g. mas „gross“, master. ap. vergl. maθišta- „grösster“; aw. masyah „grösser“; phlv. mas „gross, grösser, grössest“, masist, mas(i)st, vergl. mas-maγān „Grossmagier“ (Albērūnī), masīh, mahist, pāz. meh (PPGl.); arm. vergl. mec „gross“.' Covers meh and mehast; it says nothing about meznâ.\"},\n            {\"ref\": \"BQT:2002\", \"status\": \"contradicts\", \"note\": \"Borhan-e Qateʿ, ed. Moʿin, printed p.2002 (read from the page image, transcription saved as refs/ocr/BQT/2002.vision.txt). The headword is «مِزنا» — 'بلغت زند بمعنی ترازو باشد و بعربی میزان گویند' — and Moʿin's footnote 5 is: 'هز. mazînâ، maznâ. پهلوی tarâzûk (ترازو)، یونکر ص ۱۱۷، قس: میزان (عر)'. 'هز.' = هزوارش: the word is an Aramaic heterogram of the Frahang ī Pahlavīg read as Pahlavi tarāzūg 'balance', cognate with Arabic mīzān — the opposite of a derivative of Avestan mas- 'long'.\"},\n            {\"ref\": \"BQT:2058\", \"status\": \"supports\", \"note\": \"Borhan-e Qateʿ p.2058 s.v. «مه»: 'و بکسر اول و ظهور ثانی، بمعنی بزرگ باشد چه بزرگتر را مهتر خوانند', with Moʿin's footnote 7: 'پهلوی mas (بزرگتر)، پارسی باستان maθišta، ایرانی باستان *mazyah- «نیبرگ ص ۱۱۸»، اوستا masyah (بزرگتر). نیز پهلوی mas (بزرگ، بزرگتر، بزرگترین)، masist، mas(i)st ...؛ mahist، پازند meh، ارمنی mec (بزرگ) ... صیغهٔ عالی از mas: پازند mahist/mehist، پارسی باستان maθišta است. در کردی mezin (بزرگتر) ...'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.122-123 s.v. mas (NYB_vol2_glossary.txt line 2483)\", \"stance\": \"supports\", \"note\": \"'... hence in MIr: NW mas (MPrth only adv.), comp. masātar, sup. masišt (MPrth msyšt), but SW *mah (not attested so far), comp. mahy, mēh (MPrs mhy) Paz. meh, mehe, mahi; NP mih (used as pos.), sup. mahist (MPrs mhystg „presbyter“). BP has taken over NW mas as pos. and comp., and as sup. both SW mahist and NW masist ... Possibly, however, -s- was pronounced -h- throughout in SW; Paz. only mahest.' The decisive statement that NP meh/mahist come from Av. mas-/masišta- and OP maθišta-.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary pp.54, 55 (PHD.txt lines 444, 477)\", \"stance\": \"supports\", \"note\": \"'mahist [msst', mhst' | M mhyst, N ~] greatest' and 'meh [ms | M mhy, myh, N ~] great(er), old(er)'; also 'mehēnīdan, mehēn- increase, magnify' and the English index 'great meh, wuzurg / greatest ayōz, mahist'. Nothing s.v. any meznā.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.211 (HUB.txt leaf 221) and p.116\", \"stance\": \"supports\", \"note\": \"'Np. mih „gross“ = pāz. meh Shk. 258, phl. maθ, ap. sup. maθišta- (aber zd. mas- „gross“, masyā̊ „grösser“, masāh- „Grösse“, dial. mas in mas-muγān „Gross-magier“ ..., kurd. mastir „grösser“)'; and p.116 'über np. mih „gross“, ap. maθ- im sup. maθišta-, kih „klein“'; p.238 'mahist ... = np. mahist = ap. maθišta-'.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, entry 4383 «مه / مهتر», printed p.483 (incoming/ARY/ARY_pages.txt pdf page 482)\", \"stance\": \"partial\", \"note\": \"Aryanpur's entry gives 'پارسی باستان: MATHISHTA؛ پهلوی: MAHIST, MAHE؛ ارمنی: MEC' — i.e. the maθišta- line that Nourai draws — but in the same entry he also lists Sanskrit MAH, Greek mega- and Latin MAGNUS, i.e. he merges this root with 'Meg: great'. That merger is precisely what Nourai's cross-reference note warns about.\"},\n            {\"src\": \"MON\", \"where\": \"Moʿin (2-vol. Adena condensation) line 69481; grep of MON_part1/2 for مزنا/میزنا\", \"stance\": \"partial\", \"note\": \"'مهست: ... | ـ مهشت.' — Moʿin does have مهست (referred to مهشت), so mehast is a real dictionary word; but grep for «مزنا» and «میزنا» in MON_part1.txt / MON_part2.txt returns 0 hits, which confirms Nourai's own note that 'meznâ was not found in MON'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"makros; makedonios\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. μακρός 'long, large' is the regular reflex of the zero-grade suffixed derivative *m̥ḱ-ró- (Watkins: '*mək- becoming *mak- in suffixed form *mak-ro-'), beside μῆκος / Dor. μᾶκος 'length' < *māḱ-es- and the superlative μήκιστος 'longest'. The ethnonym Μακεδόνες is standardly explained as 'the tall ones' or 'the highlanders': it is built to μακεδνός 'tall, slim' (already Od. 7.106, of poplars), and goes with the place-name Μάκετα 'highland'; from Μακεδών come the adjective Μακεδόνιος (Nourai's 'makedonios') and the country-name Μακεδονία. Pokorny prints the chain on the cited page — 'Μάκετα „Hochland“, Μακεδόνες daher „Hochländer“, μακεδνός „schlank“, μακρός „lang“' — and Klein s.v. Macedonian: 'fr. Gk. Μακεδόνες, „the Macedonians“, lit. „the Highlanders“, or „the Tall Ones“, rel. to μακεδνός „long, tall“, and to μακρός „long, large“.' Wiktionary derives Μακεδών from μακεδνός < PIE *meh₂ḱ- 'long, slender', citing Beekes. Nourai's gloss for 'makedonios' runs the ethnonym, the adjective and the toponym together, but the derivation is right.\",\n          \"derivation_fa\": \"یونانی μακρός «دراز، بزرگ» بازماندهٔ منظمِ *m̥ḱ-ró- (درجهٔ صفرِ ریشه با پسوندِ -ro-) است، در کنارِ μῆκος / دوری μᾶκος «درازی» از *māḱ-es- و صفتِ برترینِ μήκιστος. نامِ قومیِ Μακεδόνες را از دیرباز «بلندقدان» یا «کوه‌نشینان» تفسیر کرده‌اند: این نام بر پایهٔ μακεδνός «بلند، باریک‌اندام» (که در اودیسه ۷٫۱۰۶ آمده) ساخته شده و با نامِ جایِ Μάκετα «سرزمینِ بلند» هم‌خانواده است؛ از Μακεδών صفتِ Μακεδόνιος و نامِ سرزمینِ Μακεδονία پدید آمده. پوکورنی همین زنجیره را در ص ۶۹۹ آورده و کلاین نیز می‌نویسد Μακεδόνες تحتِ‌اللفظ «کوه‌نشینان» یا «بلندقدان» است و با μακεδνός و μακρός پیوند دارد. ادعای نورایی درست است؛ تنها معنایی که او برای makedonios نوشته سه چیز (نامِ قوم، صفت و نامِ سرزمین) را در هم آمیخته است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CF%8E%CE%BD\",\n            \"https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CE%BF%CE%BD%CE%AF%CE%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. māk- (AHD_watkins1985.txt line 720): '... b. Greek makros, long, large: MACRO-, MACRON; AMPHIMACER. 2. Suffixed form *māk-es- in Greek mēkos, length ... [Pok. māk- 699.]' Watkins does not mention Macedonia; Klein and Pokorny do (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. Macedonian, macedoine, macro- (KLN_1966.txt lines 22446, 22447, 22473)\", \"stance\": \"supports\", \"note\": \"'Macedonian ... fr. L. Macedonius, fr. Gk. Μακεδόνιος, „Macedonian“, fr. Μακεδόνες, „the Macedonians“, lit. „the Highlanders“, or „the Tall Ones“, rel. to μακεδνός, „long, tall“, and to μακρός, „long, large“. See macro-.' And 'macro- ... fr. μακρός, „long, large“, cogn. with L. macer „lean, thin“ ... fr. I.-E. *m̥krós, derivative of base *māk-, *mək-, „long, thin“, whence also Gk. μῆκος „length“, μακεδνός „long, tall“.'\"},\n            {\"src\": \"POK\", \"where\": \"IEW p.699 (POK_02.txt leaf 361)\", \"stance\": \"supports\", \"note\": \"'gr. μᾶσσω, μάσσων ... μήκιστος „der längste“, μῆκος, dor. μᾶκος n. „Länge“, Μάκετα „Hochland“, Μακεδόνες daher „Hochländer“, μακεδνός „schlank“, μακρός „lang“ (= lat. macer, dt. mager)'.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde–Pokorny Bd. II 223 (WLD_Bd2_pages.txt line 14603)\", \"stance\": \"supports\", \"note\": \"'... Μάκετα (Fick BB. 26, 242) „Hochland“, Μακεδόνες daher „Hochländer“ ..., μακεδνός „schlank“, μακρός „lang“ (= lat. macer, dt. mager)'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"Maqdûnîyyeh «مقدونیه»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"مقدونیه is the Islamic-period Persian name of Macedonia, taken over from Arabic مقدونية Maqdūniyya, which in turn renders Greek Μακεδονία — mediated by Syriac (ܡܩܕܘܢܝܐ, the form of the Alexander romance and of church history), which is what gives the word its qāf for Greek kappa. Persian then substituted its own ending -iyye for Arabic -iyya, exactly as in رومیه، سوریه، اسکندریه. So the ultimate source Nourai names (Greek) is right, but the arrow drawn straight from Greek to Persian skips the Aramaic/Arabic leg that actually shaped the form: hence 'plausible' rather than 'confirmed'. Nourai's cited page could not be checked: Moʿin's six-volume Farhang-e Farsi is not online at all, its aʿlām volumes (MON5/MON6) are absent from vajehyab and abadis, and the two-volume Moʿin condensation on disk has no entry مقدونیه.\",\n          \"derivation_fa\": \"«مقدونیه» نامِ دورهٔ اسلامیِ مکدونیا است که فارسی آن را از عربیِ «مقدونية» گرفته و عربی خود آن را از یونانیِ Μακεδονία، با واسطهٔ سریانی (ܡܩܕܘܢܝܐ، صورتِ اسکندرنامه و تاریخ‌های کلیسایی) وام گرفته است؛ همین واسطه است که «ق» را به جای کافِ یونانی نشانده. سپس پایانهٔ عربیِ -iyya در فارسی به «-یه» بدل شده، مانندِ رومیه، سوریه و اسکندریه. بنابراین سرچشمهٔ نهایی که نورایی گفته (یونانی) درست است، اما پیکانی که یکسر از یونانی به فارسی کشیده شده، حلقهٔ آرامی–عربی را که شکلِ واژه را ساخته نادیده گرفته است؛ از این رو داوری «با احتیاط پذیرفتنی است». ارجاعِ خودِ نورایی (معین، جلد ۵، ص ۲۰۰۷) قابلِ بررسی نبود، زیرا مجلدهای اعلامِ فرهنگِ معین در دسترسِ برخط نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CE%BF%CE%BD%CE%AF%CE%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON5:2007\", \"status\": \"not_checked\", \"note\": \"Moʿin, Farhang-e Farsi vol. 5 (اعلام) p.2007 is not accessible: the six-volume Amir Kabir edition has no scan on archive.org / Google Books / HathiTrust, and vajehyab and abadis carry only Moʿin's lexicon volumes, not the proper-name volumes (see refs_online.json s.v. MON).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. macedoine and Macedonian (KLN_1966.txt lines 22446-22447)\", \"stance\": \"supports\", \"note\": \"'F. Macédoine, fr. L. Macedonia, fr. Macedones, „the Macedonians“, fr. Gk. Μακεδόνες' — Klein confirms the Greek toponym behind every European and, by the same route, every Near-Eastern form; he has nothing on the Arabic form.\"},\n            {\"src\": \"MON\", \"where\": \"grep «مقدونیه» in MON_part1.txt, MON_part2.txt and incoming/MON/MON_2vol_Adena_v1/v2_djvu.txt\", \"stance\": \"silent\", \"note\": \"0 hits in all four files: the two-volume Moʿin condensation, which is all that is digitised, drops the proper names, so the entry Nourai cites cannot be reached this way either.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (LKT.txt)\", \"stance\": \"silent\", \"note\": \"grep for «مقدون» / 'Maqdun' returns nothing: Lokotsch registers Orientalisms in European languages, not Graecisms in Persian, so the direction of borrowing here falls outside his book.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box, standing for Latin Macedonia (with Macedones 'the Macedonians', Macedonicus), borrowed from Greek Μακεδονία / Μακεδόνες. Rome had the name from the Macedonian wars and made it the official name of a province in 146 BCE, from which it passed unchanged into all the western languages. Klein s.v. macedoine gives the leg exactly: 'fr. L. Macedonia, fr. Macedones, „the Macedonians“, fr. Gk. Μακεδόνες'. The box carries no word and no reference in the book.\",\n          \"derivation_fa\": \"این خانه در کتاب تهی است و تنها حلقهٔ لاتینِ زنجیره را نشان می‌دهد: لاتین Macedonia (و Macedones «مکدونیان»، Macedonicus) وام‌واژه‌ای از یونانیِ Μακεδονία / Μακεδόνες است. رومیان این نام را در جنگ‌های مکدونی شناختند و در ۱۴۶ پیش از میلاد نامِ رسمیِ یکی از استان‌های خود کردند و از همان راه به همهٔ زبان‌های اروپایی رسید. کلاین همین حلقه را می‌آورد. ادعای نورایی درست است؛ این خانه نه واژه‌ای دارد و نه ارجاعی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CE%BF%CE%BD%CE%AF%CE%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no refs= in the book, so there is no citation of Nourai's to check.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. macedoine, Macedonian (KLN_1966.txt line 22446)\", \"stance\": \"supports\", \"note\": \"'F., fr. Macédoine, fr. L. Macedonia, fr. Macedones, „the Macedonians“, fr. Gk. Μακεδόνες, of s.m.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt)\", \"stance\": \"silent\", \"note\": \"grep -c -i 'macedon' SKT.txt = 0. Skeat's concise dictionary excludes proper names, so it can neither confirm nor deny this box.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"Macedonia\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Macedonia is the Latin name taken over unchanged in learned use (with Macedonian, first in Middle English as Macedoine after Old French, whence also the culinary macedoine 'medley of diced fruit or vegetables', so called facetiously in allusion to the mixture of peoples in Macedonia). Klein: 'Macedonian, adj. and n. — Formed with suff. -an fr. L. Macedonius, fr. Gk. Μακεδόνιος, „Macedonian“, fr. Μακεδόνες, „the Macedonians“, lit. „the Highlanders“, or „the Tall Ones“.' So English 'Macedonia' is at four removes from the root: *meh₂ḱ- > μακεδνός > Μακεδόνες > Μακεδονία > L. Macedonia > E. Macedonia.\",\n          \"derivation_fa\": \"«Macedonia» در انگلیسی همان نامِ لاتین است که بی‌تغییر در کاربردِ کتابی به کار رفته؛ صفتِ Macedonian از لاتینِ Macedonius و آن از یونانیِ Μακεδόνιος است، و صورتِ فرانسویِ Macédoine در انگلیسی به معنیِ آشِ میوه یا سبزیِ خردشده هم به کار می‌رود، به شوخی از بابتِ آمیختگیِ اقوامِ مکدونیه. بنابراین زنجیره چنین است: *meh₂ḱ- > μακεδνός > Μακεδόνες > Μακεδονία > لاتین Macedonia > انگلیسی Macedonia. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CE%BF%CE%BD%CE%AF%CE%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no refs= in the book.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. Macedonian, macedoine (KLN_1966.txt lines 22446-22447)\", \"stance\": \"supports\", \"note\": \"'Macedonian, adj. and n. — Formed with suff. -an fr. L. Macedonius, fr. Gk. Μακεδόνιος ... fr. Μακεδόνες, „the Macedonians“, lit. „the Highlanders“, or „the Tall Ones“, rel. to μακεδνός ... and to μακρός.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat (SKT.txt)\", \"stance\": \"silent\", \"note\": \"no entry (proper names are outside Skeat's scope); grep -c -i 'macedon' = 0.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"macro-, macron\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are direct scholarly borrowings of the Greek word. The combining form macro- (before a vowel macr-) is Gk. μακρο-, μακρ-, from μακρός 'long, large' — macrocosm, macroscopic, macroeconomics, and in prosody amphimacer. The macron, the bar written over a long vowel, is Gk. μακρόν, the neuter of μακρός, i.e. '(the) long (one)', a grammarians' term. Watkins lists MACRO- and MACRON under māk-; Klein s.v. macro-: 'Gk. μακρο-, μακρ-, fr. μακρός, „long, large“, cogn. with L. macer „lean, thin“ ... fr. I.-E. *m̥krós, derivative of base *māk-, *mək-, „long, thin“', and s.v. macron: 'Gk. μακρόν, neut. of μακρός, „long“.'\",\n          \"derivation_fa\": \"هر دو واژه وام‌گیریِ دانشورانه و مستقیم از یونانی‌اند: پیشوندِ macro- (پیش از واکه macr-) همان μακρο-/μακρ- یونانی از μακρός «دراز، بزرگ» است (macrocosm، macroscopic)، و macron نامِ خطِ افقی‌ای است که بر واکهٔ بلند می‌گذارند و همان μακρόν، صورتِ خنثای μακρός، یعنی «(حرفِ) بلند» است — اصطلاحی از دستورنویسانِ یونانی. واتکینز هر دو را ذیلِ ریشهٔ māk- می‌آورد و کلاین نیز همین را می‌گوید. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%9C%CE%B1%CE%BA%CE%B5%CE%B4%CF%8E%CE%BD\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no refs= in the book; the parent Greek box cites AHD, which does list MACRO- and MACRON under māk-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. māk- and index (AHD_watkins1985.txt lines 720, 1789)\", \"stance\": \"supports\", \"note\": \"'b. Greek makros, long, large: MACRO-, MACRON; AMPHIMACER'; index: 'MACRO- māk- ... MACRON māk-'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. macro-, macron (KLN_1966.txt lines 22473, 22478)\", \"stance\": \"supports\", \"note\": \"'macro-, before a vowel macr-, combining form meaning „long“. — Gk. μακρο-, μακρ-, fr. μακρός, „long, large“, cogn. with L. macer, „lean, thin“, ON. magr, OE. mæger, „lean, thin“, fr. I.-E. *m̥krós, derivative of base *māk-, *mək-, „long, thin“'; 'macron, n., a short horizontal line placed over a vowel to indicate its length. — Gk. μακρόν, neut. of μακρός, „long“.'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"macer\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin macer, -cra, -crum 'lean, thin' is the Italic member of the same *m̥ḱ-ró- formation that gave Gk. μακρός, with the semantic specialisation 'long and thin' > 'thin, lean' (the Germanic cognates OHG magar, OE mæger, ON magr, G mager, Du. mager have exactly the same sense, and are inherited, not borrowed from Latin). Beside it Latin has maceō, -ēre 'to be lean' and maciēs 'leanness', and the compound ēmaciāre 'to make lean' (English emaciate). Watkins: 'Zero-grade form *mək- becoming *mak- in suffixed form *mak-ro- in: a. Latin macer, thin: MAIGRE, MEAGER; EMACIATE'; Pokorny prints 'μακρός „lang“ (= lat. macer, dt. mager) ... Lat. macer, -cra, -crum „mager“, maceō, -ēre „mager sein“, maciēs f. „Magerkeit“'. Ernout–Meillet warn only against the ancient folk-connection with mācerāre 'to soften by steeping', which is a different word.\",\n          \"derivation_fa\": \"لاتین macer, -cra, -crum «لاغر، باریک» عضوِ ایتالیکِ همان ساختِ *m̥ḱ-ró- است که در یونانی μακρός را داده، با این تحولِ معنایی که «دراز و باریک» به «باریک، لاغر» گرایید؛ هم‌ریشه‌های ژرمنیِ آن (آلمانیِ باستان magar، انگلیسیِ باستان mæger، ایسلندیِ باستان magr، آلمانیِ mager) نیز همین معنا را دارند و وام‌واژه از لاتین نیستند. در کنارِ آن لاتین maceō «لاغر بودن» و maciēs «لاغری» و ēmaciāre «لاغر کردن» (انگلیسی emaciate) را دارد. واتکینز و پوکورنی هر دو macer را در همین ریشه می‌گذارند؛ ارنو–مِیه تنها هشدار می‌دهد که پیوندِ عامیانهٔ macer با mācerāre «خیساندن» نادرست است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/meager\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. māk- (AHD_watkins1985.txt line 720): '1. Zero-grade form *mək- becoming *mak- in suffixed form *mak-ro- in: a. Latin macer, thin: MAIGRE, MEAGER; EMACIATE.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW p.699 (POK_02.txt leaf 361)\", \"stance\": \"supports\", \"note\": \"'lat. macer, -cra, -crum „mager“, maceō, -ēre „mager sein“, maciēs f. „Magerkeit“ ... WP. II 223 f., WH. II 2.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. macer (LAT.txt lines 35473-35492)\", \"stance\": \"supports\", \"note\": \"'macer, -cra (-cera Ital.), -erum: maigre. Ancien, usuel. Panroman (et germanique?) ... Cf. hitt. maklant- „mince“; gr. μακρός „long“, où l'a représente i.-e. ə, comme on le voit par le substantif dor. μᾶκος, ion.-att. μῆκος „longueur“ ... Les Latins établissaient une parenté entre macer et mācerē, comme on le voit par les gloses ... La parenté n'existe pas.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. macro- and meager (KLN_1966.txt lines 22473, 23229)\", \"stance\": \"supports\", \"note\": \"'... cogn. with L. macer, „lean, thin“ ... fr. I.-E. *m̥krós, derivative of base *māk-, *mək-, „long, thin“, whence also Avestic mas-, „long“, masah-, „length, size“.'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"meager\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English meager/meagre is late 14th-century, from Old French megre, maigre 'thin' (12th c., mod. F. maigre), from Latin macrum, accusative of macer 'lean, thin'; the sense was first 'lean, emaciated' of people and animals and only from the early 15th century transferred to land, food and, later, to quantities and arguments. The inherited Germanic cognates (OE mæger, whence dialectal English meagre-looking, and ON magr, OHG magar) had the same meaning but are not the source of the English word, which came in through French. Etymonline: 'late 14c., from Old French megre, maigre „thin“ (12c.), from Latin macrum (nominative macer) „lean, thin“ ... from PIE root *mak- „long, thin“'; Klein: 'meager, meagre, adj. — ME. megre, fr. OF. maigre, magre, megre (F. maigre), fr. L. macer, „lean, thin“ ... fr. I.-E. base *m̥krós, a derivative of base *māk-, *mək-, „long, thin“, whence also Avestic mas-, „long“, masah-, „length, size“' — Klein thus draws Nourai's own chart, Avestan mas- and English meager on one root.\",\n          \"derivation_fa\": \"«meager/meagre» انگلیسی از اواخرِ سدهٔ چهاردهم است و از فرانسهٔ باستانِ megre/maigre «لاغر» (سدهٔ دوازدهم) گرفته شده که خود از لاتینِ macrum، حالتِ مفعولیِ macer «لاغر»، است. نخست دربارهٔ انسان و جانور به معنیِ «لاغر، نزار» به کار می‌رفت و از آغازِ سدهٔ پانزدهم به زمین و خوراک و سپس به مقدار و دلیل هم تعمیم یافت. هم‌ریشه‌های ژرمنیِ ارثی (انگلیسیِ باستان mæger و آلمانیِ باستان magar) همین معنا را داشتند اما سرچشمهٔ واژهٔ انگلیسیِ امروزی نیستند؛ راهِ ورود از فرانسه بوده است. اتیمونلاین و کلاین هر دو همین را می‌گویند و کلاین در همان مدخل، اوستایی mas- «دراز» و masah- «درازی، اندازه» را نیز هم‌ریشهٔ آن می‌شمارد — یعنی درست همان نموداری که نورایی کشیده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/meager\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no refs= in the book; the parent Latin box cites AHD, whose māk- entry lists MAIGRE, MEAGER, EMACIATE.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. meager, meagre (KLN_1966.txt line 23229)\", \"stance\": \"supports\", \"note\": \"'meager, meagre, adj. — ME. megre, fr. OF. maigre, magre, megre (F. maigre), fr. L. macer, „lean, thin“, which is cogn. with Gk. μακρός, „long“, OE. mæger, ON. magr, MDu. magher, Du. mager, OHG. magar, MHG., G. mager, „lean, thin“, fr. I.-E. base *m̥krós, a derivative of base *māk-, *mək-, „long, thin“, whence also Avestic mas-, „long“, masah-, „length, size“. Cp. also — with l-suff. — Hitt. maklanza, „thin, meager“. Cp. emaciate, Macedonian, macro-, maigre, malinger, meco-.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. meagre (SKT.txt line 9448)\", \"stance\": \"supports\", \"note\": \"the OCR is badly damaged but the entry is there: 'meagre. (L.) ... L. macer, dry [read: lean]' — Skeat too takes it straight from Latin macer.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index (AHD_watkins1985.txt line 1834)\", \"stance\": \"supports\", \"note\": \"'MEAGER māk-'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Mako\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *maḱ-o- / *moḱ-o- 'gnat, midge, biting fly' (Pokorny 699), beside the velar Indo-Iranian *makš- / *makš-ī- 'fly' (PII *mákš-)\",\n      \"note\": \"'Mako' is Pokorny's own headword on the cited page: 'maḱo- oder moḱ-o- (-lo-, -ko-, Deminutivformantien) „Stechfliege, Mücke“' — Skt. maśáka- 'biting fly, gnat', Lith. mašalas 'gnat', Latv. masalas 'horse-fly' — followed by 'vgl. mit Velar die arische Sippe von ai. mákṣa- m., mákṣā f. „Fliege“, av. maxši- „Fliege, Mücke“ usw., und lit. mākatas „Kriebelmücke“'. So the root, its language label and its page are all correct, and Bailey cites it the same way ('IE Pok. 699 maḱo- „midge“'). Two refinements: (i) the gloss is properly 'gnat, midge, biting fly' rather than specifically 'house fly'; (ii) strictly, the Indo-Iranian *makš- words have a velar where the European words have a palatal, so Pokorny attaches them as a velar variant rather than as straight descendants — the family is a cluster of parallel formations rather than one regular etymon. That is unsurprising, because both Pokorny and Buck regard the whole group as onomatopoeic: 'Wohl schallmalend (wie auch mu-, mus- in Worten für Fliege)' (WP II 225), 'prob. of imitative orig., like the group above' (Buck 3.83, the group being IE *mu-, *mus- 'with reference to the humming'). Nourai's own NOTE on node #1 records exactly this and is right to.\",\n      \"note_fa\": \"«Mako» عیناً سرواژهٔ پوکورنی در همان صفحهٔ ۶۹۹ است: «maḱo- یا moḱ-o- (با پسوندهای تصغیرِ -lo- و -ko-) به معنیِ مگسِ گزنده، پشه»، با شواهدِ سنسکریت maśáka- «پشه»، لیتوانیایی mašalas و لتونیایی masalas؛ و پوکورنی بی‌درنگ می‌افزاید: «با کامیِ ولاری بسنجید خانوادهٔ آریاییِ سنسکریت mákṣā «مگس» و اوستایی maxši- «مگس، پشه»». بیلی نیز در فرهنگِ ختنیِ خود همین ارجاع را می‌دهد. دو نکتهٔ اصلاحی: نخست آنکه معنایِ دقیقِ ریشه «پشه، مگسِ گزنده» است نه ویژهٔ «مگسِ خانگی»؛ دوم آنکه صورت‌های هندوایرانی همخوانِ ولاری دارند در برابرِ کامیِ صورت‌های اروپایی، پس پوکورنی آن‌ها را «گونهٔ ولاری» می‌شمارد نه بازماندهٔ مستقیم. این هم شگفت نیست، چون هم پوکورنی و هم باک این خانواده را نام‌آوا (ریشه‌شناسیِ آواگون، از وزوزِ حشره) می‌دانند و باک آن را با *mu-/*mus- (لاتین musca) یکی می‌گیرد. یادداشتِ خودِ نورایی در خانهٔ ۱ همین را ثبت کرده و بجاست. ادعای نورایی دربارهٔ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%85%DA%AF%D8%B3\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:699\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 360 (the printed '699' opens this entry) / POK_full.txt lines 57345-57366: 'Root/lemma: maḱo- or moḱ-o-. Meaning: a kind of fly. Note: (-lo-, -ko-, diminutive formants). Material: Old Indic maśáka- m. „horsefly, biting housefly, mosquito“, Lithuanian mašalas „mosquito“, Latvian masalas ... compare with velar the Aryan family of Old Indic mákṣa- m., mákṣā „fly“, Avestan maxši- „fly, mosquito“ etc., and Lithuanian mākatas „blackfly“. References: WP. II 225, Specht Idg. Dekl. 43 f., Trautmann 170. Page(s): 699.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Walde–Pokorny Bd. II 225 (WLD_Bd2_pages.txt lines 14734-14745)\", \"stance\": \"supports\", \"note\": \"'maḱo- oder moḱ-o-(-lo-, -ko-, Deminutivformantien) „Stechfliege, Mücke“. Ai. maśáka- m. „Stechfliege, Mücke“, lit. mašalai „Mücken“, lett. masalas „Roßfliegen“ ... Wohl schallmalend (wie auch mu-, mus- in Worten für Fliege), vgl. mit Velar die arische Sippe von ai. mákṣa- m. mákṣā „Fliege“ av. maxši- „Fliege, Mücke“ usw. (s. Uhlenbeck Ai. Wb. 209, Bartholomae Airan. Wb. 1112). ... Unannehmbar legt Petersson ein mak- „stechen, verletzen“ zugrunde.' This is the WP II 225 Pokorny cites, and it gives Bartholomae col. 1112 for maxši-.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, the three mak- lemmas (AHD_watkins1985.txt lines 718-720)\", \"stance\": \"silent\", \"note\": \"Watkins has māk-¹ 'poppy', māk-² '(leather) bag' and māk- 'long, thin', but NO root for 'fly': the whole group is absent from the AHD appendix, presumably because it left no English descendant. A grep for 'gnat|midge|Fly.' in AHD_watkins1985.txt finds nothing relevant.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, An Indo-European Comparative Dictionary (IEC.txt)\", \"stance\": \"silent\", \"note\": \"grep for 'maksa|maks-|mak-o|gnat|midge' finds no lemma for 'fly/gnat' — Mann does not set up this root.\"},\n        {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka s.v. mata- (ISS_alt_DKS.txt line 6045)\", \"stance\": \"supports\", \"note\": \"'From *maxši- > *mëšša- > mata ..., to Av. maxši- „fly“, Zor.P. maxš ...; Sogd. Bud. mwγšk-, O.Ind. mákṣa-. Variants are *mukasa-, Zor.P. makas, magas, N.Pers. magas ... IE Pok. 699 maḱo- „midge“, O.Ind. maśáka-, Lit. mãšalas; with -s- as above.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"maxši\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan maxši- f. 'fly, gnat, mosquito' (Bartholomae, Altiranisches Wörterbuch col. 1112, cited as '(1112) maxši-' by Nyberg and by the Šāyast nē Šāyast glossary) is the exact equivalent of Sanskrit mákṣā / mákṣī 'fly', i.e. Proto-Indo-Iranian *mákš- with the feminine ī-stem inflection; the -xš- of the Avestan spelling is the regular Iranian outcome of Indo-Iranian *-kš-. Pokorny attaches this Aryan set to *maḱo- 699 as its velar variant, and Buck, on the page Nourai cites, prints 'Skt. mákṣā-, Av. maxši- prob. of imitative orig., like the group above' — 'the group above' being 'IE *mu-, *mus-, prob. of imitative orig., with reference to the humming' (Gk. muia, Lat. musca, ChSl. mucha). So Nourai's own NOTE ('SYN:193 claims an imitative origin (Indo-European \\\"Mu\\\", \\\"Mus\\\")') is an accurate report, and modern scholarship sides with Buck: both *maḱ-/*makš- and *mu-/*mus- are independent onomatopoeic creations for the buzzing insect rather than one inherited PIE noun, which is why the family shows so many irregular variants (*makša-, *makaša-, *makasa-, *mukasa-).\",\n          \"derivation_fa\": \"اوستایی maxši- (مؤنث) «مگس، پشه» — بارتولومه، فرهنگِ ایرانیِ باستان، ستونِ ۱۱۱۲، که نیبرگ و واژه‌نامهٔ شایست‌نه‌شایست هر دو به همین ستون ارجاع می‌دهند — برابرِ دقیقِ سنسکریت mákṣā/mákṣī «مگس» است، یعنی هندوایرانیِ آغازین *mákš- با صرفِ ستاکِ مؤنثِ -ī؛ خوشهٔ -xš- در اوستایی بازتابِ منظمِ *-kš- هندوایرانی است. پوکورنی این خانوادهٔ آریایی را به‌عنوانِ «گونهٔ ولاری» به ریشهٔ maḱo- (ص ۶۹۹) می‌بندد، و باک در همان صفحهٔ ۱۹۳ که نورایی به آن ارجاع داده می‌نویسد این واژه‌ها «احتمالاً خاستگاهِ آواگون دارند، مانندِ گروهِ پیشین» — و گروهِ پیشین *mu-/*mus- است (یونانی muia، لاتین musca، اسلاوی mucha). پس یادداشتِ نورایی درست گزارش شده و پژوهشِ امروزی هم با باک همراه است: این دو خانواده دو ساختِ نام‌آوایِ مستقل‌اند نه یک نامِ ارثیِ هندواروپایی، و همین است که این‌همه گونهٔ بی‌قاعده (*makša-، *makaša-، *makasa-، *mukasa-) در آن دیده می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%DA%AF%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:699\", \"status\": \"supports\", \"note\": \"IEW 699 (POK_full.txt line 57364): 'compare with velar the Aryan family of Old Indic mákṣa- m., mákṣā „fly“, Avestan maxši- „fly, mosquito“ etc.'\"},\n            {\"ref\": \"SYN:193\", \"status\": \"supports\", \"note\": \"Buck, Selected Synonyms 3.83 'FLY (sb.)', printed p.193 (SYN.txt lines 5133-5139): the table lists 'Skt. mákṣa-, Av. maxši-'; the discussion reads '1. IE *mu-, *mus-, prob. of imitative orig., with reference to the humming. Walde-P. 2.311 ... Grk. μυῖα, Lat. musca ... ChSl. mucha' and '4. Skt. mákṣa-, Av. maxši- prob. of imitative orig., like the group above, 1. Uhlenbeck 209.' Nourai's note reports this correctly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. 1112 (BRT.txt)\", \"stance\": \"silent\", \"note\": \"I could not reach the entry itself: greps for 'maxši|maxsi-' in the Bartholomae OCR return nothing (the columns around 1100 are badly degraded). The column number is however cited for maxši- 'Fliege' by three independent books on disk — Walde–Pokorny II 225 ('Bartholomae Airan. Wb. 1112'), Nyberg II 122 ('Av. (1112) maxši-') and the SNS glossary ('maxšī-: (1112) makṣikā-') — so the reference is secure even though the page is unreadable here.\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. mata- (ISS_alt_DKS.txt line 6045)\", \"stance\": \"supports\", \"note\": \"'... to Av. maxši- „fly“, Zor.P. maxš, Yidγa maxšē, mōxī „mosquito“, Orm. maši, miši „fly“; Sogd. Bud. mwγšk-, O.Ind. mákṣa-.' Bailey also cites the Khotanese development *maxši- > *mëšša- > mata- 'bee, fly'.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde–Pokorny Bd. II 225 (WLD_Bd2_pages.txt line 14742)\", \"stance\": \"supports\", \"note\": \"'vgl. mit Velar die arische Sippe von ai. mákṣa- m. mákṣā „Fliege“ av. maxši- „Fliege, Mücke“ usw. (s. Uhlenbeck Ai. Wb. 209, Bartholomae Airan. Wb. 1112).'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"maxš; makas, magas\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both Pahlavi words are real and both mean 'fly': MacKenzie's dictionary has 'maxš [mhš] fly' and 'magas [mks | P mgs, N ~] fly. ~ ī angubēn: honey-bee', and Nyberg, under the unidentified Ahrimanic creature *macāh, cites 'BP makas, NP magas „fly“; Av. (1112) maxši-, Kurd. mēš'. The Šāyast nē Šāyast glossary that Nourai cites has maxš with 'Av. maxšī-, (1112), Skt. makṣikā-' and the compound maxš-par. The reservation concerns the route, not the root. MP maxš is the direct, regular descendant of Avestan/Proto-Iranian *maxši-. makas/magas cannot be: Hübschmann says so in as many words — 'Unklar ist das Verhältniss von np. magas „Fliege“ = phl. makas ..., bal. makask = ap. *makasa- (= skr. *makaśa- oder *makaska-) zu afgh. mač = iran. *maiša- und zd. *maxši, gen. maxšya, skr. mákṣa-, makṣikā-. Vielleicht ist arisch *makaśa- neben *makša- anzusetzen' — and Bailey lists makas/magas as 'Variants ... *mukasa-', while Wiktionary reconstructs a separate Proto-Iranian *makácaH for magas. In other words makas/magas continue the *-ḱ- formation (Pokorny's maḱ-o- proper, cf. Skt. maśáka-, Balochi makask/magisk/mahisk, Yidγa maγusa, Pashto maǰai < *mašyaka-), a sister of maxši- rather than its child. Nourai puts the right words in the right box but draws one arrow where two parallel lines are needed.\",\n          \"derivation_fa\": \"هر دو واژهٔ پهلوی راست‌اند و هر دو «مگس» معنی می‌دهند: مکنزی maxš و magas را (با ترکیبِ magas ī angubēn «زنبورِ عسل») ثبت کرده و نیبرگ ذیلِ *macāh می‌نویسد «پهلوی کتابی makas، فارسی نو magas «مگس»؛ اوستایی (۱۱۱۲) maxši-، کردی mēš»؛ واژه‌نامهٔ شایست‌نه‌شایست هم maxš را با ارجاع به maxšī- اوستایی و makṣikā- سنسکریت و ترکیبِ maxš-par آورده است. تردید بر سرِ ریشه نیست، بر سرِ راهِ تحول است: maxš بازماندهٔ مستقیم و منظمِ *maxši- است، اما makas/magas نمی‌تواند باشد. هوبشمان (ص ۲۳۸) صریح می‌گوید: «نسبتِ فارسی نو magas = پهلوی makas و بلوچی makask با اوستایی maxši- روشن نیست؛ شاید باید در آریایی *makaśa- را در کنارِ *makša- نشاند.» بیلی نیز makas/magas را «گونه» می‌شمارد و ویکی‌واژه برای magas ایرانیِ آغازینِ جداگانه‌ای (*makácaH) بازمی‌سازد. یعنی makas/magas از ساختِ کامیِ *maḱ-o- (قسِ سنسکریت maśáka-، بلوچی makask/magisk/mahisk، یدغه maγusa، پشتو maǰai) می‌آید که خواهرِ *maxši- است نه فرزندِ آن. نورایی واژه‌ها را در خانهٔ درست گذاشته اما یک پیکان کشیده آنجا که به دو خطِ موازی نیاز بود؛ پس ادعای او با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%DA%AF%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:221\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 989, printed pp.221-222 (HRN.txt leaves 243-244): 'meges „Fliege“, jüd.-pers. mks (Is. 7,18). aw. vergl. maxši- „Fliege, Mücke“; phlv. magas (Vd. 1 (16)), makas (Bahmyt.), maxš (nur Umschreibung des Awesta-Wortes); ai. vergl. mākṣa-, mákṣikā-. kurd. mēš (LW. magās „Biene“); bal. makask, magisk, n. mahisk „Fliege, Mücke“ (222); waxī maks, minj. maγa. — np. meges ist wie die sämmtlichen anderen neuiranischen Worte ausser kurd. mēš nicht direct mit aw. maxši-, ai. mákṣa- vereinbar.' Horn thus gives Nourai's three Pahlavi forms, and adds exactly the reservation stated above.\"},\n            {\"ref\": \"SNS:238\", \"status\": \"supports\", \"note\": \"Tavoosi, Vāže-nāme-ye Šāyast nē Šāyast, glossary entry maxš (SNS.txt lines 13511-13518 = leaf 137 of 242; the printed page number is not legible in this OCR, so I cannot confirm '238' itself): 'maxš: ... | maxšī-: (1112) makṣika- ... | Henning, BSOS IX.1, p.85 ... | maxš par: ...'. The glossary does have Pahlavi maxš 'fly' with the Avestan and Sanskrit comparanda, i.e. it says what Nourai's arrow says.\"},\n            {\"ref\": \"ISS:278\", \"status\": \"supports\", \"note\": \"Bailey's Khotanese Texts VI (Indo-Scythian Studies) is not online; the standard substitute, Bailey's Dictionary of Khotan Saka, covers the same material s.v. mata- (ISS_alt_DKS.txt line 6045): '... to Av. maxši- „fly“, Zor.P. maxš ...; Sogd. Bud. mwγšk-, O.Ind. mákṣa-. Variants are *mukasa-, Zor.P. makas, magas, N.Pers. magas, Yidγa moγuso, maγusa, Pašto maǰai (*mašyaka-). IE Pok. 699 maḱo- „midge“.' Every form in Nourai's Pahlavi box appears here, with the same root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary pp.53, 54 and the English index (PHD.txt lines 439, 464, 1982)\", \"stance\": \"supports\", \"note\": \"'magas [mks | P mgs, N ~] fly. ~ ī angubēn: honey-bee'; 'maxš [mhš] fly'; index 'fly (n.) magas, maxš'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.121 s.v. *macāh (NYB_vol2_glossary.txt line 2369)\", \"stance\": \"supports\", \"note\": \"'*macāh [mcʾh], macāi [mcʾy] an Ahrimanic animal 967⁴, 981⁵. — Not identified. Possibly to be connected with the ws. denoting „fly“: Paštō mac, māc „gad-fly“; BP makas, NP magas „fly“; Av. (1112) maxši-, Kurd. mēš; cf Sogd. 45.'\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.238 (HUB.txt leaf 248, line 8469)\", \"stance\": \"partial\", \"note\": \"'Unklar ist das Verhältniss von np. magas „Fliege“ = phl. makas Gl. and Ind. 215, bal. makask = ap. *makasa- (= skr. *makaśa- oder *makaska-, vgl. np. pas = ap. pasa „hinter“ : zd. paskāt?) zu afgh. mač = iran. *maiša- (oben p. 98) und zd. *maxši, gen. maxšya, skr. mákṣa-, makṣikā-. Vielleicht ist arisch *makaśa- neben *makša- anzusetzen.' — the words are all here, but Hübschmann refuses the single line of descent the chart draws.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index printed p.476 (incoming/ARY/ARY_latin_index_pages.txt pdf page 475, lines 13869-13872)\", \"stance\": \"supports\", \"note\": \"the index block for مگس reads 'MAKHSHI (AVESTAN) ... (PAHLAVI) MAKHSH, MAGAS, MAKAS ... MESH, MYSH (KURDISH) ... (BALUCHI) MAGISK, MAKASH, MAHISK ... MECH, MAC (AFGHAN)', beside German Mücke and English midge/mygg — i.e. Aryanpur, an independent modern Persian handbook, gives exactly Nourai's Avestan and Pahlavi forms.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"magas «مگس»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP مگس magas 'fly' continues Middle Persian magas <mks> without change (MacKenzie marks it 'N ~', i.e. identical in New Persian); the Manichaean Middle Persian/Parthian form mwγš is attested in the Turfan fragments (Henning), and the modern Iranian dialects have the whole spread: Kurdish mēš, Balochi magisk/makask/mahisk, Wakhi maks, Munji maγa, Gilaki mešgar. Moʿin's footnote to Borhan-e Qateʿ p.2029 lays out the same material as Nourai's chart, and derives the word ultimately from Avestan maxši-. The word has been productive in Persian (مگس‌ران, شیرین‌مگس, مگسک) and was carried outward as a loan into Ottoman Turkish, Hindustani and Khalaj.\",\n          \"derivation_fa\": \"«مگس» فارسی نو دنبالهٔ بی‌تغییرِ فارسی میانهٔ magas (نوشتهٔ <mks>) است؛ مکنزی هم آن را با نشانهٔ «N ~» یعنی «در فارسی نو همان» می‌آورد. صورتِ فارسی میانهٔ مانوی و پارتیِ mwγš در پاره‌نوشته‌های تورفان گواهی شده (هنینگ)، و گویش‌های ایرانیِ امروز همهٔ گونه‌ها را نشان می‌دهند: کردی mēš، بلوچی magisk/makask/mahisk، وخی maks، منجی maγa، گیلکی mešgar. حاشیهٔ معین بر برهان قاطع (ص ۲۰۲۹) همان مواد را می‌آورد که در نمودارِ نورایی است و واژه را در نهایت به maxši- اوستایی می‌رساند. این واژه در فارسی زایا بوده (مگس‌ران، مگسک) و از فارسی به ترکیِ عثمانی، هندوستانی و خلجی وام رفته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%DA%AF%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2029\", \"status\": \"supports\", \"note\": \"Borhan-e Qateʿ, ed. Moʿin, printed p.2029 (rendered and OCR'd as refs/ocr/BQT/2029.png/.txt), footnote to «مگس»: 'مگس ـ بفتح اول و دوم، قس اوستایی maxši- (مگس، پشه)، پهلوی magas / makas (فقط در شرح کلمات اوستایی)، بلوچی magasak/makask/mahisk (مگس، پشه)، وخی maks، منجی maγoka، «اسشق ۱۹۸۹»، سانسکریت makṣa-, makṣikā (پشه) ... هوبشمان ...، در اوراق مانوی (پارتی) mwγš (مگس) «هنینگ، فهرست کلمات پارسی میانه ...»، کردی mēš ...؛ حشره‌ای از راستهٔ دوبالان ...'\"},\n            {\"ref\": \"HRN:221\", \"status\": \"supports\", \"note\": \"Horn no. 989, p.221: 'meges „Fliege“ ... phlv. magas' — Horn's 'meges' is the same New Persian word (his transcription of مگس).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.53 (PHD.txt line 439)\", \"stance\": \"supports\", \"note\": \"'magas [mks | P mgs, N ~] fly' — the 'N ~' means New Persian has the identical form.\"},\n            {\"src\": \"MON\", \"where\": \"Moʿin, 2-vol. condensation (MON_part1.txt 14 hits, MON_part2.txt 24 hits for «مگس»)\", \"stance\": \"supports\", \"note\": \"مگس and its compounds are current dictionary Persian in Moʿin (e.g. 'زنبور عسل، مگس' in the definitions of کست and گبت); the word's existence and meaning are not in doubt.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index p.476 (incoming/ARY/ARY_latin_index_pages.txt line 13869)\", \"stance\": \"supports\", \"note\": \"the مگس index block gives 'MAKHSHI (AVESTAN)' and '(PAHLAVI) MAKHSH, MAGAS, MAKAS' as the ancestry of the Persian word.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"mwğšk\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Buddhist Sogdian mwγšk(ʾ) /muxšk/ 'fly, mosquito' is Gharib's entry 5518, glossed and etymologised there as '← *maxšika-; Pahl. maxš' with references to TSP 2.390, SCE 364 and Gershevitch's Grammar of Manichean Sogdian §§113, 165, 975. It is *maxši- extended by the very common Sogdian suffix -k (< Old Iranian *-ka-), the same suffix as in Pahlavi/NP magas-ak; Bailey cites it in the same breath as the Avestan and Middle Persian forms ('Sogd. Bud. mwγšk-'). Because Sogdian is a sister of Avestan and not its descendant, Nourai's drawing the Sogdian box straight from the root rather than through the Avestan box is the correct way to chart it. One small point of form: the book prints 'mwǧšk' and the extracted data 'mwğšk', where the standard transliteration is mwγšk (Sogdian gamma).\",\n          \"derivation_fa\": \"سغدیِ بودایی mwγšk(ʾ)، خوانده /muxšk/، «مگس، پشه» است؛ در فرهنگِ سغدیِ بدرالزمان قریب مدخلِ ۵۵۱۸ است و همان‌جا ریشه‌شناسیِ آن آمده: «از *maxšika-؛ قس پهلوی maxš»، با ارجاع به TSP 2.390 و SCE 364 و دستورِ سغدیِ مانویِ گرشویچ. این صورت همان *maxši- است با پسوندِ بسیار پربسامدِ سغدیِ -k (از *-ka- ایرانی باستان)، همان پسوندی که در magas-ak پهلوی و فارسی هم دیده می‌شود؛ بیلی نیز آن را در کنارِ صورت‌های اوستایی و فارسی میانه می‌آورد. چون سغدی خواهرِ اوستایی است و نه بازماندهٔ آن، کشیدنِ پیکان از خودِ ریشه به خانهٔ سغدی — چنانکه نورایی کرده — درست است. یک نکتهٔ کوچکِ نگارشی: کتاب «mwǧšk» چاپ کرده و دادهٔ استخراجی «mwğšk» دارد، در حالی که آوانگاریِ متعارف mwγšk (با گامای سغدی) است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%DA%AF%D8%B3\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ISS:278\", \"status\": \"supports\", \"note\": \"Khotanese Texts VI itself is not online (see refs_online.json s.v. ISS); Bailey's Dictionary of Khotan Saka, the standard substitute, gives the same claim s.v. mata- (ISS_alt_DKS.txt line 6045): 'to Av. maxši- „fly“, Zor.P. maxš ...; Sogd. Bud. mwγšk-, O.Ind. mákṣa-.' Nourai citing ISS:278 for both his Pahlavi and his Sogdian box is consistent with Bailey treating them in one paragraph.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary entry 5518 (SOD_pages.txt lines 19506-19510, leaf 287 ≈ printed p.221)\", \"stance\": \"supports\", \"note\": \"'5518 mwγšk(ʾ) B — muxšk ← *maxšika-; Pahl. maxš — fly, mosquito. TSP 2.390; SCE 364; GMS 113, 165, 975, 1182 n 2.'\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. mata- (ISS_alt_DKS.txt line 6045)\", \"stance\": \"supports\", \"note\": \"'Sogd. Bud. mwγšk-' listed among the direct continuations of *maxši-, together with Zor.P. maxš, Yidγa maxšē and Ormuri maši.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Mana\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Akkadian manû(m) 'mina' (60 shekels, c. 500 g), a derivative of manû 'to count'; Sumerian ma-na on the current view a loan FROM Akkadian rather than its source\",\n      \"note\": \"The unit and its name are certain; the direction of the very first arrow is not. Klein, whom Nourai cites for the root box, does say 'Akkad. manû (fr. Sumer. mana)', and Moʿin's footnote in Borhan-e Qateʿ p.2035 says the same at greater length ('در زبان سومری ... لغت manā ... و از آنان به اکدیان رسیده، manā گفتند'). But Nourai's other reference for the root box, Zimmern's Akkadische Fremdwörter pp.20-21, explicitly refuses to decide: 'akk. manû „Mine“ (fraglich ob < sum. mana, oder ob dies << akk. manû, dann manû „Mine“ viell. von manû „zählen“, minu „Zahl“)'. Present-day Assyriology takes the second option: Sumerian ma-na is 'probably a loanword from Akkadian' (M. A. Powell, Maße und Gewichte, followed by Wiktionary s.v. 𒈠𒈾), the Akkadian noun being built on the verb manû 'to count, reckon' (cf. minûtu 'number'), which gives it a transparent Semitic etymology that Sumerian ma-na lacks. Nourai's root box therefore records the older consensus and may well have the arrow the wrong way round; everything from Akkadian onwards is uncontroversial. Note also that this is one of Nourai's non-Indo-European root boxes: the language label 'Sumerian' is a real language, not a reconstruction, so the box makes a historical rather than a comparative claim, and it is that historical claim which modern Assyriology reverses.\",\n      \"note_fa\": \"خودِ یکا و نامِ آن قطعی است، اما جهتِ نخستین پیکان نه. کلاین — که نورایی برای همین خانه به او ارجاع می‌دهد — می‌نویسد «اکدی manû (از سومری mana)»، و حاشیهٔ معین بر برهان قاطع (ص ۲۰۳۵) نیز مشروح‌تر همین را می‌گوید: «در زبان سومری ... لغتِ manā ... و از آنان به اکدیان رسیده، manā گفتند». اما مرجعِ دیگرِ خودِ نورایی، تسیمرن در «وام‌واژه‌های اکدی» ص ۲۰–۲۱، صریحاً از داوری پرهیز می‌کند: «اکدی manû „مینا“ (روشن نیست از سومریِ mana آمده یا سومری از اکدی؛ در صورتِ دوم manû شاید از manû „شمردن“ و minu „شمار“ باشد)». آشورشناسیِ امروز گزینهٔ دوم را برگزیده است: سومریِ ma-na «به احتمالِ زیاد وام‌واژه از اکدی است» (پاول، مقیاس‌ها و وزن‌ها؛ و ویکی‌واژه ذیلِ 𒈠𒈾)، و نامِ اکدی بر پایهٔ فعلِ manû «شمردن» ساخته شده که ریشه‌شناسیِ سامیِ روشنی به آن می‌دهد و سومری چنین چیزی ندارد. پس این خانه دیدگاهِ کهن‌تر را ثبت کرده و شاید پیکان را برعکس کشیده باشد؛ از اکدی به بعد هیچ اختلافی نیست. داوری: با احتیاط پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%F0%92%88%A0%F0%92%88%BE\",\n        \"https://en.wiktionary.org/wiki/mina\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"AKD:20,21\", \"status\": \"partial\", \"note\": \"Zimmern, Akkadische Fremdwörter, printed pp.20-21 (AKD.txt leaves 29-30): 'akk. manû Mine (fraglich ob < sum. mana, oder ob dies << akk. manû, dann manû Mine viell. von manû zählen, minu Zahl) : > hebr. māne (> ägypt. mn (mano)), aram. manyā (auch in mᵉnē Dan. 5,25 f. „Menetekel“ urspr. vorliegend) (> arab. mana(n)), angeblich ind. manā, griech. μνᾶ, lat. mina, „Mine“.' Zimmern has the whole downstream chain, but he does NOT assert the Sumerian origin Nourai's root box asserts — he calls it 'fraglich' and offers a purely Akkadian alternative.\"},\n        {\"ref\": \"KLN:982\", \"status\": \"supports\", \"note\": \"Klein s.v. mina (KLN_1971.txt line 151789, = KLN 1966 p.982): 'mina, n., an ancient unit of weight and money. — L., fr. Gk. μνᾶ, which is of Sem. origin. Cp. Akkad. manû (fr. Sumer. mana) and Heb. mānēh, Biblical Aram. mᵉnē (Dan. 5:25), Aram.-Syr. manyā (whence Arab. manan), Ugar. mn, which are borrowed fr. Akkad. manû. Cp. mine, „unit of weight“. Cp. also maund, „unit of weight“.' Klein's parenthesis '(fr. Sumer. mana)' is exactly Nourai's root box.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ, ed. Moʿin, printed p.2035, footnote 5 to «من» (refs/ocr/BQT/2035.png/.txt)\", \"stance\": \"supports\", \"note\": \"'قس: سانسکریت māna- (مقیاس، وزن، وزنی معین) یا از هندی باستان manā (وزنی معین [طلا])، یونانی mnā، لاتینی mina، قس: اکدی manā معرب «من» ... در زبان شومری (قوم غیرسامی و غیرآریایی) لغت manā ... و از آنان به اکدیان رسیده، manā گفتند. و در عبری māneh شده است. «من» اساساً وزنی بوده و سپس نام پولی گردید و بمرور زمان نزد اقوام مختلف، ارزشهای مختلف پیدا کرد ـ رک: هرمزدنامه ۲۹۳.' Moʿin gives Nourai's entire chart, Sumerian root box included.\"},\n        {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 991b, printed p.222 (HRN.txt leaf 244)\", \"stance\": \"partial\", \"note\": \"'(2)men „ein Gewicht“, ar. LW. mann. skr. vergl. māna- „Maass (ganz allgemein), Maassstab, Gewicht“, dann auch „ein bestimmtes Gewicht“. Oder zu ai. manā- „ein best. Gewicht (Gold)“, gr. μνᾶ, lat. mina, die semitische LW. sind, vergl. akkad. mana (Schrader, Sprachvergl. und Urgesch.² 206 folg., 252)?' Horn has the whole chain but with a question mark, and he does not commit to a Sumerian starting point.\"},\n        {\"src\": \"FVQ\", \"where\": \"Jeffery, The Foreign Vocabulary of the Qurʾān (FVQ.txt)\", \"stance\": \"silent\", \"note\": \"greps for 'mina', 'manā' and 'maneh' return nothing relevant: the mina is not a Qurʾānic word (the Qurʾān uses miṯqāl and qinṭār), so Jeffery has no entry.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Akkadian\",\n          \"words\": \"mânu\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Akkadian manû(m) — Nourai's 'mânu' — is the mina, the standard Mesopotamian weight of 60 shekels = 1/60 talent, about 500 g, attested from the Old Akkadian period onwards through the whole cuneiform tradition. Morphologically it is a noun to the verb manû 'to count, reckon, assign' (cf. minûtu, minu 'number'), which is why current Assyriology treats it as native Semitic and Sumerian ma-na as the borrower. From Akkadian it spread over the whole ancient Near East: Hebrew מָנֶה māneh, Biblical Aramaic מְנֵא mᵉnē (the mᵉnē of the writing on the wall, Dan. 5:25), Aramaic–Syriac manyā (whence Arabic mann/manan), Ugaritic mn, Egyptian mn — and, at the other end, Greek μνᾶ. Zimmern's list on the cited pages and Klein's article s.v. mina are identical in content, and Zimmern adds the calque 'akk. ina mane ša tamkāri „nach der Mine des Kaufmanns“ = hebr. kesep ʿōbēr las-sōḥēr'.\",\n          \"derivation_fa\": \"اکدی manû(m) — همان «mânu» نورایی — نامِ «مینا» است، یکایِ استاندارِ وزن در میان‌رودان: ۶۰ شِکِل یا یک‌شصتمِ تالِنت، نزدیک به ۵۰۰ گرم، که از دورهٔ اکدیِ باستان تا پایانِ سنتِ میخی گواهی شده است. از نظرِ ساختی، این واژه اسمی است از فعلِ manû «شمردن، برشمردن» (قس minûtu «شمار»)، و همین است که آشورشناسیِ امروز آن را سامیِ اصیل و سومریِ ma-na را وام‌گیرنده می‌شمارد. از اکدی به سراسرِ خاورِ نزدیکِ باستان رفت: عبری māneh، آرامیِ کتابِ مقدس mᵉnē (همان «مِنِه» در نوشتهٔ روی دیوار، دانیال ۵:۲۵)، آرامی–سریانی manyā (و از آن عربی مَنّ)، اوگاریتی mn، مصری mn، و در سویِ دیگر یونانی μνᾶ. فهرستِ تسیمرن در همان صفحه‌ها و مدخلِ کلاین ذیلِ mina یکی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/mina\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AKD:20,21\", \"status\": \"supports\", \"note\": \"Zimmern pp.20-21 (AKD.txt leaves 29-30): 'akk. manû Mine ... : > hebr. māne (> ägypt. mn (mano)), aram. manyā (auch in mᵉnē Dan. 5,25 f. „Menetekel“ urspr. vorliegend) (> arab. mana(n)), angeblich ind. manā, griech. μνᾶ, lat. mina, „Mine“. — Dem akk. ina mane ša tamkāri „nach der Mine des Kaufmanns“, wird hebr. kesep ʿōbēr las-sōḥēr direkt nachgebildet sein.' Zimmern also lists the neighbouring units šiqlu > šeqel/σίγλος, parsu 'Halbmine' > prs/parsin, girû '1/24 shekel' > gerā — the whole Daniel 5:25 series.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. mina (KLN_1971.txt line 151789 = 1966 p.982)\", \"stance\": \"supports\", \"note\": \"'... Cp. Akkad. manû (fr. Sumer. mana) and Heb. mānēh, Biblical Aram. mᵉnē (Dan. 5:25), Aram.-Syr. manyā (whence Arab. manan), Ugar. mn, which are borrowed fr. Akkad. manû.' Klein makes Akkadian manû the source of every other Semitic and of Greek.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ p.2035 footnote 5\", \"stance\": \"supports\", \"note\": \"'قس: ... اکدی manā معرب «من» ... و در عبری māneh شده است' — Moʿin too routes Hebrew and Arabic through the Akkadian form.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān (FVQ.txt)\", \"stance\": \"silent\", \"note\": \"no entry: the mina is not Qurʾānic vocabulary; greps for 'mina'/'manā' return only unrelated matches ('denomina-', 'illumina-').\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"manâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sanskrit manā́ is a weight (specifically of gold) and is itself a Semitic loan; beside it stands the native māna- 'measure, measuring-rod, weight', a regular derivative of mā- 'to measure', which is a different word and should be kept apart. The link Nourai draws is genuinely in the literature: Klein's article on the very page cited (p.949, s.v. maund) reads 'maund, also man, n., a unit of weight used in India, Persia and Turkey. — Hind. and Pers. man, „mina“, fr. OI manā, which is of Sem. origin. See mina, „unit of weight“' — i.e. Klein really does send Persian man through an Old Indian manā of Semitic origin. But every source hedges it. Horn no. 991b offers Skt. māna- first and only then, with a question mark, 'Oder zu ai. manā- „ein best. Gewicht (Gold)“, gr. μνᾶ, lat. mina, die semitische LW. sind, vergl. akkad. mana?'; Zimmern is blunter and writes 'angeblich ind. manā' — 'allegedly Indian manā'. Historically the Indic detour is also hard to motivate: the mina reached Iran through Mesopotamia and the Achaemenid administration, and Persian man could as easily be a direct take-over of Aramaic manyā. So the arrow Akkadian → Sanskrit → Persian is one defensible reading of the evidence rather than the established route: hence 'plausible'.\",\n          \"derivation_fa\": \"سنسکریت manā́ نامِ وزنی (به‌ویژه وزنِ طلا) است و خود وام‌واژه‌ای سامی است؛ در کنارِ آن māna- «پیمانه، مقیاس، وزن» ایستاده که مشتقی ارثی از mā- «پیمودن» است و واژهٔ دیگری است و نباید با آن آمیخته شود. پیوندی که نورایی کشیده در ادبیاتِ موضوع واقعاً هست: کلاین در همان صفحهٔ ۹۴۹ که نورایی به آن ارجاع می‌دهد، ذیلِ maund می‌نویسد «هندی و فارسی man „مینا“، از هندیِ باستان manā که خاستگاهِ سامی دارد». اما همهٔ منابع آن را با احتیاط می‌آورند: هرن (شمارهٔ ۹۹۱ب) نخست māna- را پیش می‌گذارد و سپس با علامتِ سؤال «یا به سنسکریت manā- (وزنی معین از طلا)، یونانی μνᾶ، لاتینی mina که وام‌واژه‌های سامی‌اند، قس اکدی mana؟»، و تسیمرن صریح‌تر می‌نویسد «به گفتهٔ برخی، هندیِ manā» (angeblich). از نظرِ تاریخی هم گذر از هند دشوار می‌نماید: مینا از راهِ میان‌رودان و دیوانِ هخامنشی به ایران رسیده و «من» فارسی می‌تواند وام‌گیریِ مستقیم از آرامیِ manyā باشد. پس این حلقه با احتیاط پذیرفتنی است، نه راهِ مسلّم.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/mina\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:949\", \"status\": \"supports\", \"note\": \"Klein s.v. maund (KLN_1966.txt line 23168, printed p.949; the same entry in KLN_1971.txt line 146880): 'maund, also man, n., a unit of weight used in India, Persia and Turkey. — Hind. and Pers. man, „mina“, fr. OI manā, which is of Sem. origin. See mina, „unit of weight“.' Klein also has the cross-entry 'man, n., a unit of weight. — See maund.' This is precisely Nourai's Sanskrit → Persian arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 991b, p.222 (HRN.txt leaf 244)\", \"stance\": \"partial\", \"note\": \"'skr. vergl. māna- „Maass ..., Gewicht“, dann auch „ein bestimmtes Gewicht“. Oder zu ai. manā- „ein best. Gewicht (Gold)“, gr. μνᾶ, lat. mina, die semitische LW. sind, vergl. akkad. mana?' — Horn offers the Indic link only as an alternative, with a question mark, and keeps māna- and manā- apart.\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern p.21 (AKD.txt leaf 30)\", \"stance\": \"partial\", \"note\": \"'... angeblich ind. manā, griech. μνᾶ, lat. mina' — 'allegedly Indian manā'. Zimmern lists the Sanskrit form but marks it as a claim he will not vouch for.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ p.2035 footnote 5\", \"stance\": \"supports\", \"note\": \"'قس: سانسکریت māna- (مقیاس، وزن، وزنی معین) یا از هندی باستان manā (وزنی معین [طلا])' — Moʿin gives both the Sanskrit forms as possible sources of Persian «من», which is Nourai's route.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"man 2 «من ۲»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP مَن man is the standard Persian and Central Asian weight, Arabicised as مَنّ mann and carried into India as maund. Borhan-e Qateʿ p.2035 — Nourai's own citation — defines it ('وزنی باشد معین در هر جایی، و آنچه درین زمان متعارف است چهل استار است ...'), and Moʿin's footnote 8 on the same page fixes the modern values that give Nourai his gloss: man-e Tabrīz = 40 sīr ≈ 3 kg, man-e šāh = 2 man-e Tabrīz ≈ 6 kg, man-e Rey = 2 man-e šāh ≈ 12 kg, man-e šarʿī = 180 mithqāl. So '3 kilograms' is the man-e Tabrīz, the commonest reckoning. Horn registers the word as his no. 991b '(2)men „ein Gewicht“, ar. LW. mann' and separates it explicitly from (1)men 'I' — hence the '2' in Nourai's headword, which follows the same practice as Borhan/Moʿin's «من ۲». The word is a Semitic loan of Achaemenid or earlier date, whichever intermediary is preferred (Aramaic manyā directly, or Skt. manā as in node #2); it never had anything to do with Iranian *man- 'to think' or the pronoun man 'I'.\",\n          \"derivation_fa\": \"«مَن» فارسی نامِ رایج‌ترین یکایِ وزن در ایران و آسیای میانه است که در عربی «مَنّ» معرّب شده و در هند به‌صورتِ maund درآمده است. برهان قاطع در ص ۲۰۳۵ — همان ارجاعِ خودِ نورایی — آن را چنین تعریف می‌کند: «وزنی باشد معین در هر جایی، و آنچه درین زمان متعارف است چهل استار است»، و حاشیهٔ ۸ معین در همان صفحه اندازه‌های امروزی را می‌دهد که معنیِ نورایی از آن‌جا آمده: منِ تبریز = ۴۰ سیر ≈ ۳ کیلوگرم، منِ شاه = ۲ منِ تبریز ≈ ۶ کیلوگرم، منِ ری = ۲ منِ شاه ≈ ۱۲ کیلوگرم، منِ شرعی = ۱۸۰ مثقال. پس «۳ کیلوگرم» همان منِ تبریز است. هرن این واژه را با شمارهٔ ۹۹۱ب ثبت کرده («men ۲ = وزنی؛ وام‌واژهٔ عربی mann») و آن را از «مَن» به معنیِ ضمیرِ اول‌شخص جدا کرده — و همین است سببِ عددِ «۲» در سرواژهٔ نورایی، به پیرویِ «من ۲» برهان و معین. این واژه وام‌واژه‌ای سامی است، از هر واسطه‌ای که آمده باشد، و هیچ ربطی به ریشهٔ ایرانیِ *man- «اندیشیدن» یا ضمیرِ من ندارد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/mina\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2035\", \"status\": \"supports\", \"note\": \"Borhan-e Qateʿ, ed. Moʿin, printed p.2035 (refs/ocr/BQT/2035.png/.txt), s.v. «من»: 'بفتح اول و سکون ثانی، معروف است و آن وزنی باشد معین در هر جایی، و آنچه درین زمان متعارف است چهل استار است ...' with footnote 5 giving 'سانسکریت māna- ... هندی باستان manā ... یونانی mnā، لاتینی mina ... اکدی manā معرب «من» ... در زبان شومری ... و در عبری māneh شده است' and footnote 8 'اکنون نیز «من تبریز» = ۴۰ سیر = ... = ۳ کیلوگرم؛ «من شاه» = ۲ من تبریز = ۶ کیلوگرم؛ «من ری» = ۲ من شاه = ۱۲ کیلوگرم؛ «من شرعی» = ۱۸۰ مثقال. رک: فرهنگ نظام.' Both the etymology and the '3 kilograms' are Nourai's page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 991b, p.222 (HRN.txt leaf 244)\", \"stance\": \"supports\", \"note\": \"'991ᵇ (2)men „ein Gewicht“, ar. LW. mann.' with the footnote 'Genaue Angaben über die verschiedenen gebräuchlichen Menn findet man bei F. Stolze und F. C. Andreas, Die Handelsverhältnisse Persiens, S. 83.' Horn numbers it separately from (1)men 'ich', as Nourai's 'man 2' does.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. maund / man (KLN_1966.txt lines 22738, 23168)\", \"stance\": \"supports\", \"note\": \"'man, n., a unit of weight. — See maund.' / 'maund, also man, n., a unit of weight used in India, Persia and Turkey. — Hind. and Pers. man, „mina“, fr. OI manā, which is of Sem. origin.' Klein confirms the Persian word and its value as the Near-Eastern mina.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"mna\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek μνᾶ (Ionic μνέα, Attic μνᾶ), the mina = 100 drachmas = 1/60 of a talent, is a Semitic loanword taken over together with the Babylonian weight system, presumably through Phoenician intermediaries in the archaic period; it is already an everyday commercial word in the 5th century. The Greek form has lost the first vowel of manā (mnā), the normal treatment when a Semitic CaCā noun is borrowed with the accent on the second syllable (cf. μνᾶ beside Hebrew māneh). Zimmern's list on AKD:21 ends 'griech. μνᾶ, lat. mina, „Mine“'; Klein: 'L., fr. Gk. μνᾶ, which is of Sem. origin.' Nourai draws the Greek box straight from Akkadian, which is right in substance — Greek did not get the word through Sanskrit or Persian, and Klein makes exactly the same connection.\",\n          \"derivation_fa\": \"یونانی μνᾶ (یونیایی μνέα) نامِ «مینا» است: صد دراخما یا یک‌شصتمِ تالِنت. این واژه وام‌واژه‌ای سامی است که همراه با نظامِ وزنِ بابلی، احتمالاً به واسطهٔ فنیقیان، در دورهٔ آرکائیک به یونانی رسیده و در سدهٔ پنجم پیش از میلاد واژه‌ای بازاری و روزمره است. صورتِ یونانی واکهٔ نخستِ manā را از دست داده (manā > mnā)، که رفتارِ عادیِ یونانی با اسم‌های سامیِ CaCā با تکیه بر هجای دوم است. تسیمرن در ص ۲۱ فهرستِ خود را با «یونانی μνᾶ، لاتینی mina» می‌بندد و کلاین می‌نویسد «لاتین mina از یونانیِ μνᾶ که خاستگاهِ سامی دارد». پیکانی که نورایی از اکدی به یونانی کشیده در ماهیت درست است: یونانی این واژه را نه از سنسکریت و نه از فارسی نگرفته. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/mina\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no refs= in the book; the root box's KLN:982 and AKD:20,21 both cover this step (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. mina (KLN_1971.txt line 151789 = 1966 p.982)\", \"stance\": \"supports\", \"note\": \"'mina, n., an ancient unit of weight and money. — L., fr. Gk. μνᾶ, which is of Sem. origin. Cp. Akkad. manû ...'\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern p.21 (AKD.txt leaf 30)\", \"stance\": \"supports\", \"note\": \"the list of forms derived from akk. manû ends '... griech. μνᾶ, lat. mina, „Mine“.'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"mina\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin mina 'a Greek weight and coin, the mina' is a straightforward borrowing of Greek μνᾶ, current from Plautus onwards (where minae are always Greek money, as befits comedies set in Greek cities); the Latin form supplies the initial vowel that Greek had dropped, i.e. mi-na for mnā, in the usual Latin manner with initial clusters foreign to it. It is to be kept strictly apart from the homonymous Latin mina 'threat' (to minārī) and from mina 'a lamprey'. Klein: 'mina ... L., fr. Gk. μνᾶ'; Zimmern likewise closes his chain with 'lat. mina'.\",\n          \"derivation_fa\": \"لاتین mina «مینا، وزن و سکهٔ یونانی» وام‌گیریِ سادهٔ یونانیِ μνᾶ است و از پلاوتوس به بعد در متونِ لاتین دیده می‌شود (در کمدی‌های او minae همیشه پولِ یونانی است). صورتِ لاتین واکهٔ آغازینی را که یونانی انداخته بود بازمی‌گرداند، یعنی mi-na در برابرِ mnā، به همان شیوهٔ همیشگیِ لاتین در برخورد با خوشه‌های آغازینِ بیگانه. این واژه را باید به‌دقت از همنامِ آن، لاتین mina «تهدید» (از minārī)، و از mina «مارماهی» جدا داشت. کلاین می‌نویسد «لاتین mina از یونانیِ μνᾶ» و تسیمرن نیز زنجیرهٔ خود را با «لاتین mina» می‌بندد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/mina\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no refs= in the book.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. mina (KLN_1971.txt line 151789)\", \"stance\": \"supports\", \"note\": \"'mina, n., an ancient unit of weight and money. — L., fr. Gk. μνᾶ, which is of Sem. origin.'\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern p.21 (AKD.txt leaf 30)\", \"stance\": \"supports\", \"note\": \"'... griech. μνᾶ, lat. mina, „Mine“' — Zimmern's chain ends in exactly the Greek → Latin step this box draws.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"mina, mine\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English mina 'an ancient unit of weight and money' is a learned borrowing of Latin mina (used in translations of the Bible and of classical authors, and in metrology), and the doublet mine — also spelt myne in earlier English — is the same Latin word taken over through French; both senses Nourai gives ('old units of weight and money') are right, since the mina was a weight first and a money-of-account second. Klein p.982, the page Nourai cites, is exactly this entry and ends 'Cp. mine, „unit of weight“. Cp. also maund, „unit of weight“', which ties this box back to node #3: English mina/mine and English maund (= Persian man) are ultimately the same Akkadian word arriving by two different roads, one through Greek and Latin, the other through Sanskrit/Persian and Hindustani. Wiktionary: 'Borrowed from Latin mina, from Ancient Greek μνᾶ (mnâ)', glossing it as 'a unit of weight of varying value used in the ancient Middle East ... also an ancient Greek measure of weight equivalent to 1/60th of a talent' and 'a monetary unit of ancient Greece and the Middle East'. The mina of Luke 19:13 ('ten pounds' in the AV) is the same word.\",\n          \"derivation_fa\": \"«mina» در انگلیسی وام‌واژه‌ای کتابی از لاتینِ mina است که در ترجمه‌های کتابِ مقدس و متونِ کلاسیک و در مبحثِ اوزان به کار می‌رود، و دوگانهٔ آن «mine» (در انگلیسیِ کهن‌تر myne) همان واژهٔ لاتین است که از راهِ فرانسه گرفته شده. هر دو معنایی که نورایی داده («یکاهای کهنِ وزن و پول») درست است، زیرا مینا نخست وزن بود و سپس واحدِ حساب و پول شد. کلاین در ص ۹۸۲ — همان صفحه‌ای که نورایی به آن ارجاع می‌دهد — همین مدخل را دارد و در پایان می‌نویسد «قس mine و همچنین maund»، و همین یادداشت این خانه را به خانهٔ ۳ گره می‌زند: «mina/mine» انگلیسی و «maund» انگلیسی (که همان «من» فارسی است) در نهایت یک واژهٔ اکدی‌اند که از دو راه رسیده‌اند، یکی از راهِ یونانی و لاتین و دیگری از راهِ سنسکریت/فارسی و هندوستانی. ویکی‌واژه نیز می‌نویسد «وام‌گرفته از لاتین mina، از یونانیِ باستان μνᾶ». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/mina\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:834\", \"status\": \"not_checked\", \"note\": \"AHD:834 is a page of the main dictionary of the American Heritage Dictionary, New College Edition (1975/76). Only the Indo-European Roots appendix of that edition is on disk (AHD_watkins1985.txt), and the appendix by its nature has no entry for a Semitic loanword; the New College main text is not available (see refs_online.json s.v. AHD). Klein:982, cited alongside it, does cover the claim.\"},\n            {\"ref\": \"KLN:982\", \"status\": \"supports\", \"note\": \"Klein s.v. mina (KLN_1971.txt line 151789 = 1966 p.982): 'mina, n., an ancient unit of weight and money. — L., fr. Gk. μνᾶ, which is of Sem. origin. Cp. Akkad. manû (fr. Sumer. mana) and Heb. mānēh, Biblical Aram. mᵉnē (Dan. 5:25), Aram.-Syr. manyā (whence Arab. manan), Ugar. mn, which are borrowed fr. Akkad. manû. Cp. mine, „unit of weight“. Cp. also maund, „unit of weight“.' Both of Nourai's English words and his gloss come straight from this entry.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. mina and maund (KLN_1971.txt lines 151789, 146880)\", \"stance\": \"supports\", \"note\": \"see the quotation above; Klein's own cross-references mina → mine → maund reproduce the whole of Nourai's entry 2.\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern pp.20-21 (AKD.txt leaves 29-30)\", \"stance\": \"supports\", \"note\": \"Zimmern's chain akk. manû > ... > griech. μνᾶ, lat. mina underlies the English word, though Zimmern of course stops at Latin.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-320.json > /dev/null && echo \"JSON OK\"",
 "description": "Write verification JSON for page 320"
}
```


### [2026-09-07T16:17:45.092Z] TOOL RESULT

```
JSON OK
```


## [2026-09-07T16:17:49.283Z] TOOL CALL #90: Bash

```json
{
 "command": "python3 tools/verify_check.py 320",
 "description": "Run verify_check for page 320"
}
```


### [2026-09-07T16:17:50.640Z] TOOL RESULT

```
nodes verified: 19/19
node verdicts: {'confirmed': 15, 'disputed': 1, 'plausible': 3}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 19, 'contradicts': 1, 'not_checked': 8}
books consulted: {'supports': 40, 'partial': 6, 'silent': 6} | by book: {'KLN': 12, 'AKD': 4, 'NYB': 3, 'PHD': 3, 'ARY': 3, 'MON': 3, 'SKT': 3, 'BRT': 2, 'HUB': 2, 'POK': 2, 'WLD': 2, 'AHD': 2, 'ISS_alt_DKS': 2, 'BQT': 2, 'HRN': 2, 'IEC': 1, 'LKT': 1, 'LAT': 1, 'SOD': 1, 'FVQ': 1}
```


## [2026-09-07T16:18:10.997Z] AGENT

Done. `python3 tools/verify_check.py 320` → 19/19 nodes, 0 PROBLEM lines.

**Page 320 (book p. 290) — 3 entries, 19 nodes**
- Node verdicts: 15 confirmed, 3 plausible, 1 disputed. Root verdicts: 2 confirmed (Mâk, Mako), 1 plausible (Mana).
- Ref checks: 19 supports, 1 contradicts, 8 not_checked. Books consulted: 40 supports / 6 partial / 6 silent.

**disputed**
- Mâk #2, Persian `meznâ «مزنا»` "balance, scale" — not from this root at all. Nourai's own cited page (BQT:2002) prints مِزنا with Moʿin's footnote "هز. mazînâ, maznâ. پهلوی tarâzûk (ترازو)، یونکر ص ۱۱۷، قس: میزان (عر)": it is an Aramaic *huzvārišn* of the Frahang ī Pahlavīg read as Pahlavi *tarāzūg*, from Semitic w-z-n (cf. Arab. mīzān). `meh` and `mehast` in the same node are confirmed (Horn 999, Hübschmann 211, Nyberg s.v. mas, MacKenzie, BQT:2058) — note Wiktionary's rival derivation of مه from *méǵh₂s is the minority view.

**plausible (not disputed, but route differs)**
- Mana root: Zimmern (AKD:20,21, Nourai's own ref) refuses to decide the Sumerian→Akkadian direction; modern Assyriology has Sum. ma-na as a loan *from* Akk. manû (< manû "to count").
- Mana #2 Sanskrit `manâ`: Klein:949 does support it, but Horn (991b) and Zimmern ("angeblich ind. manā") hedge; Persian man may come straight from Aramaic manyā.
- Mako #2 Pahlavi `makas, magas`: only `maxš` descends from Av. maxši-; makas/magas reflect a sister *makaśa-/*makáčaH (Hübschmann p.238 "Unklar ist das Verhältniss…"; Bailey "Variants").

**extraction errors for the owner to fix (JSON ≠ printed page 320)**
- Entry 0 node #2: JSON script `«میزنا»`; the book prints `«مِزنا»` — the kasra under the mīm was read as a yā.
- Entry 0 node #4: JSON `Maqdûnîyyeh`; the book prints `Maqdŭnîyyeh` (breve, not circumflex).
- Minor: entry 1 node #4 `mwğšk`; book prints `mwǧšk` (standard transliteration mwγšk).

Artefacts added: page image `data/verification/sources/refs/ocr/BOOK/320.png`, vision transcription `…/ocr/BQT/2002.vision.txt`, BQT pages 2002/2029/2035/2058 cached, 7 web sources archived via `fetch_source.py`.
