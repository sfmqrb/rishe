# Verification process log — verify-page-464


## [2026-09-14T02:27:42.266Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 464 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-464.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-464.json. Write /home/sfmqrb/git/rishe/data/verification/page-464.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 464` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:43.374Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:44.344Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:44.380Z] TOOL RESULT

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


## [2026-09-14T02:27:44.834Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-464.txt"
}
```


### [2026-09-14T02:27:44.853Z] TOOL RESULT

```
1	=== PDF page 464 (book page 434) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sol, Solo : whole  (refs POK:979)
4	#1 (parent #0) [Avestan] refs=POK:979 | haurva 1 : whole, all, each ; haurvatât : completeness, perfection
5	  #2 (parent #1) [Persian] refs=BQT:729,2318 | har «هر» : each ; Xordâd «خرداد» : "perfect"
6	#3 (parent #0) [Greek] refs=POK:979; AHD; WEB:286 | holos : whole ; kata-holos : whole, universal ; holo-kaustos : burnt whole ☞Kŭ 1
7	  #4 (parent #3) [Greek] refs=AHD | katholicos : whole undivided church of Christ
8	    #5 (parent #4) [French] refs=AHD | catholique
9	      #6 (parent #5) [Persian] refs=MON:2783 | kâtolîk «کاتولیک» : "general"
10	      #7 (parent #5) [English] refs=None | Catholic
11	    #8 (parent #4) [Arabic] refs=TAD:19 | jâselîq : universal, a rank in the Catholic church.
12	      #9 (parent #8) [Persian] refs=MON:1199; FSF:141 | jâselîq «جاثلیق» : a Catholic rank
13	  #10 (parent #3) [English] refs=AHD | holograph, hologram, holocaust
14	#11 (parent #0) [Latin] refs=AHD | solidus : intact, solid ; salŭs : whole condition, good health (salutation) ; salvus : healthy, safe
15	  #12 (parent #11) [English] refs=AHD | solid ; salute ; safe, save, salvation
16	--- entry 1 ---
17	ROOT Solo -> redirect to Sol
18	--- entry 2 ---
19	ROOT [Greek] Sophos : skilled, wise  (refs AHD:1232)
20	#1 (parent #0) [Greek] refs=AHD:1232 | sophisma : a skilled but false reasoning, fallacy ; philo-sophos : fond of wisdom ☞Bhili
21	  #2 (parent #1) [Arabic] refs=TAD:35,53 | safsatah : fallacy ; falsafah : philosophy
22	    #3 (parent #2) [Persian] refs=MON:1889,2567 | safsateh «سفسطه» : fallacy ; falsafeh «فلسفه» : philosophy | extra: فلاسفه ، فیلسوف
23	  #4 (parent #1) [Latin] refs=None | 
24	    #5 (parent #4) [French] refs=None | 
25	      #6 (parent #5) [English] refs=AHD:1332 | sophist, sophism, sofist, sofism, Sophia sophisticated, sophomore, philosophy,
26	
```


## [2026-09-14T02:27:47.990Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-464.json",
 "description": "Read source JSON page 464"
}
```


### [2026-09-14T02:27:48.044Z] TOOL RESULT

```
{
  "pdf_page": 464,
  "book_page": 434,
  "entries": [
    {
      "root": {
        "name": "Sol, Solo",
        "lang": "Indo-European",
        "refs": "POK:979",
        "gloss": "whole"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:979",
          "words": [
            {"translit": "haurva 1", "gloss": "whole, all, each", "script": null},
            {"translit": "haurvatât", "gloss": "completeness, perfection", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:729,2318",
          "words": [
            {"translit": "har", "gloss": "each", "script": "هر"},
            {"translit": "Xordâd", "gloss": "\"perfect\"", "script": "خرداد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:979; AHD; WEB:286",
          "words": [
            {"translit": "holos", "gloss": "whole", "script": null},
            {"translit": "kata-holos", "gloss": "whole, universal", "script": null},
            {"translit": "holo-kaustos", "gloss": "burnt whole", "script": null, "see": ["Kŭ 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "katholicos", "gloss": "whole undivided church of Christ", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "catholique", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:2783",
          "words": [
            {"translit": "kâtolîk", "gloss": "\"general\"", "script": "کاتولیک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Catholic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 4,
          "lang": "Arabic",
          "refs": "TAD:19",
          "words": [
            {"translit": "jâselîq", "gloss": "universal, a rank in the Catholic church.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:1199; FSF:141",
          "words": [
            {"translit": "jâselîq", "gloss": "a Catholic rank", "script": "جاثلیق"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "زبطریق وز جاثلیقان شهر - هرآنکس کش از مردمی بود بهر",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 10,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "holograph, hologram, holocaust", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "solidus", "gloss": "intact, solid", "script": null},
            {"translit": "salŭs", "gloss": "whole condition, good health (salutation)", "script": null},
            {"translit": "salvus", "gloss": "healthy, safe", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "solid", "gloss": null, "script": null},
            {"translit": "salute", "gloss": null, "script": null},
            {"translit": "safe, save, salvation", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Solo",
        "redirect": "Sol"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sophos",
        "lang": "Greek",
        "refs": "AHD:1232",
        "gloss": "skilled, wise"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1232",
          "words": [
            {"translit": "sophisma", "gloss": "a skilled but false reasoning, fallacy", "script": null},
            {"translit": "philo-sophos", "gloss": "fond of wisdom", "script": null, "see": ["Bhili"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "TAD:35,53",
          "words": [
            {"translit": "safsatah", "gloss": "fallacy", "script": null},
            {"translit": "falsafah", "gloss": "philosophy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:1889,2567",
          "words": [
            {"translit": "safsateh", "gloss": "fallacy", "script": "سفسطه"},
            {"translit": "falsafeh", "gloss": "philosophy", "script": "فلسفه"}
          ],
          "script_extra": "فلاسفه ، فیلسوف",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
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
          "lang": "French",
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
          "refs": "AHD:1332",
          "words": [
            {"translit": "sophist, sophism, sofist, sofism, Sophia sophisticated, sophomore, philosophy,", "gloss": null, "script": null}
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


## [2026-09-14T02:27:50.087Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','WEB','BQT','MON','TAD','FSF','WLD','KLN','HRN','HUB','PHD','NYB','BRT','KNT','IEC','SYN','SKT','FSD','ARY','PLA','AFM','FVQ','LKT','CHEUNG']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-14T02:27:51.256Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
CHEUNG null
```


## [2026-09-14T02:27:54.899Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','WEB','BQT','MON','TAD','FSF']:\n    print('=====',k); print(json.dumps(d.get(k),ensure_ascii=False,indent=1))\n\""
}
```


## [2026-09-14T02:27:55.750Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -80 && echo ---- && sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T02:27:57.182Z] TOOL RESULT

```
===== POK
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
===== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
===== WEB
{
 "title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)",
 "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w",
 "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt",
 "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.",
 "notes": "",
 "cites": "page number of Webster's New Twentieth Century Dictionary, 2nd ed."
}
===== BQT
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
===== MON
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
===== TAD
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
===== FSF
{
 "title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/20220809_20220809_1444",
 "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"
 ],
 "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking",
 "covers_etymology": false,
 "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."
}
```


### [2026-09-14T02:27:57.256Z] TOOL RESULT

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
```


## [2026-09-14T02:28:38.284Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:28:38.353Z] TOOL RESULT

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


## [2026-09-14T02:28:39.177Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\n\""
}
```


### [2026-09-14T02:28:40.278Z] TOOL RESULT

```
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


## [2026-09-14T02:28:50.764Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma sol\"; grep -n -i \"lemma: sol\" POK_full.txt | head -20\necho \"=== POK_03 p979 (leaf ~213-217)\"; for L in 211 212 213 214 215 216 217; do echo \"--- leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' POK_03.txt | head -5; done"
}
```


### [2026-09-14T02:28:51.801Z] TOOL RESULT

```
=== POK_full lemma sol
71342:Root/ lemma: solo-, sol(e)uo-\ "whole, integrate' derived from Root/ lemma: sal-\ "salt; 
79317:Root / lemma: solo-, sol(e)uo- 
79323:Root/ lemma: solo-, sol(e)uo-\ "whole, integrate' derived from Root/ lemma: sal-\ "salt; 
=== POK_03 p979 (leaf ~213-217)
--- leaf 211
en, Gedächtnis',  av.  maraiti,  hismaraiti  ,(be) merkt',  mimara-  , eingedenk';  arm. mormok  ,Bedauern,  Mißvergnügen,  Kummer,  Leid*  (mit  Formans  -ok  von einem  ^mor-mloi^lo-  mit  gebrochener  Red.);  gr.  ixsQpiSQog  ,was  viel  Sinnen, Sorgen  erfordert' ;  [.isgi-taiQU),  fj,€Q^rjQL^(i)  , sorge,  sinne,  zaudere' ;  (xsQfxrjoä  f. jSorge,  Sinnen*,  (j,£QLixv(xa)  ,sorge,  bin  bedacht,  grüble'.  Postverbale  f.i6Qii.tva  f. ,Sorge,  Besorgnis*;  auch  (xaQTvg,  -Qog^  hom.  fi&QTVQogy  kret.  fiaiTVQ-  , Zeuge'? anders  oben  S.  735;
lat.  memor  ,eingedenk*  (vgl.  av.  mimara-  ds.,  ags.  ge-mimor  ds.),  memoria , Gedächtnis' ;  Moria  ,eine  Parze* ;
air.  airm{m)ert  L  ,y erbot',  cymr.  armerth  ^Vorbereitung*,  ('^smert-)^  mir. mertaid  ^richtet  ein',  bret.  merzout  ,gewahr  werden*,  Yannes  armerhein  ,ein- richten*;  gall.  PN  Smerius,  Smertullus,  GN  Smertrios]  Ro-smerta  ,die  Vor- aussehende* ;  abrit.  VN  ^j-iigrai.
aisl.  Mlmir  _,ein  Riese*;  ags.  mimorian  ,sich  erinnern*,  ge-mimor  ^bekannt*, mämrian  ,über  etwas  sinnen*,  ndl.  mijmeren  ,tief  nachsinnen' ;  got.  maürnanj ags.  mumian,  ahd.  mornen  ,sorgen,  ängstlich  besorgt  sein';
alit.  mereti  , sorgen',  dehnstufig  serb.  mdriti  ,sich  kümmern  um',  usw. (*wör-) ;
--- leaf 212
stank',  lit.  smdr[d]vey  alit« smarstas  , Gestank'  (auch  smarste,  smarstvas,  smdrsas  ,schlechteres  Fett*, eigentlich  , schlechtriechendes  Fett'),  apr.  smorde  ,Faulbaum';  aksl.  srnndSti, russ.  smerdeth  ,stinken*,  russ.  smörod  , Gestank*,  smorödina  , Johannisbeere*, poln.  smröd,  öech.  smrad  , Gestank*;  dazu  wahrscheinlich  lat.  merda  ,Kot, Unrat  des  Leibes'.
smerd-  ,stinken'  ist  eine  wohl  schon  idg.   verselbständigte  Anwendung von  (s)merd-  in  nhd.  schmerzen,  lat.  mordere,  s.  mer-,  merd-  ,auf reiben*  (oben  '--j S.  736  f.),  ursprünglich  also  , beißender  Geruch'.  '^----
WP.  II  691,  WH.  II  74  f.,  Trautmann  271,  Vasmer  2,  676,  Specht  KZ 62,  215.  :
smeru-  und  Ähnliches :  , Schmer,  Fett'.
Gr.  wohl  aixvQig  , Schmirgel  zum  Abreiben  und  Polieren',  {(j)i.Lvqit^(a ,poliere  durch  Reiben,  salbe',  ^vqov  n.  ,wohlriechendes  Salböl,  Pflanzensaft*, vielleicht  auch  (a)f.ivQog  ,eine  Art  Aal,  Muräne'  als  , fettig  sich  anfühlend'; lat.  vielleicht  in  medullae  PI.  ,Mark  von  Knochen  und  Pflanzen^,  durch Einfluß  von  medius  aus  *merulla  umgestaltet;  air.  smi(u)r  m.,  Gen.  smera ,Mark*,  cymr.  mer  ,Mark';  aisl.  smigr  n.,  ags.  smeoru,  ahd.  sm&ro  (Gen. smerwes)  ,Schmer,   Fett',  wovon  aisl.  smyria^  smyrva  ,bestreichen,  salben',
--- leaf 213
.  Worte  allenfalls  mit  gh,  worauf  auch  arm.  moyg  ,braun,  dunkel'  als *smougho-  in  Vergleich  käme;  unklar  das  Verhältnis  zu  russ.-ksl.  smagh ,dunkel,  braun',  russ.  smdga  ,Flamme;  Ruß',  dech.  smahnouti  , dörren, schmachten'.
WP.  II  688  f.,  Vasmer  2,  669  f.,  677.
smog-  jSchwer  lastend,  sich  mit  einer  schweren  Last  abmühen'.
Gr.  iiöyog  jMühe,  Anstrengung',  fxoyeqoq  (ajxoyegöv  Hes.)  , mühselig', ^oysü)  , strenge  mich  an',  fxöyig  Adv.  ,kaum'  (ursprünglich  Nom.  Sg.  ,sich mühend'  =  ,nur  mit  Mühe');  fx6xd-og  (*fj,ö^Tog)  m.  , Anstrengung,  Mühe', piox^sTv  ,sich  abmühen',  fiox^rjQÖg  ,mühselig';  (.lox^ög  {*(xo^lög)  , Hebebaum, Hebel',  [xox^-scoj  -svo)  , bewege  fort';  lit.  (zem.)  smagiis  , schwer  zu  tragen oder  zu  ziehen',  lett.  smags,  smagrs  , schwer  von  Gewicht,  lastend'.
WP.  II  692.
--- leaf 214
�v  tö  rajisivöv  Hes.,   das  als  ,Meerestiefe'  zu  verstehen  861? wird;  aber  vTjglöag'  rag  y-oilag  nirgag  Hes.  vielleicht  zu  ner-  , eindringen') .reduktionsstufig  vßQÖg  {^väfsqog)  , rinnend,  fließend',  vasTWQ'  qscov,  noXvQ- Qoog  Hes.,  att.  Vok.  varoQ  m.  , Strom',  vaua  (*vafeixa)  ,Flüssigkeit,  Quelle'/ väa^og  (*väf€a(xög)    ,Wasserlauf,    Quelle,    Bach' ;   mir.    snäu,   snö   ,Strom* (*snäua) ;
5.  von  *sneu-  aus:  vso)  (Fut.  vevaoi-iai)  , schwimme',  lak.  v6a'  Ttrjyi^^ s-vvvd'sv  ixexvvro  Hes.  lat.  nUtriö,  -Ire  , säugen,  nähren',  Ableitung  von einem  *sneU'tri  fem.  ,Milch  fließen  lassend';
als  d-Er Weiterung  von  sneu-  faßt  man  mir.  snüad  (auch  FIN)  ,Fluß'j ,caesaries'  (,*herabfließend'),  mhd.  snuz  , Schnupfen',  norw.  snottj  ags. gesnott  n.  , Katarrh',  aisl.  snyta,  ahd.  snüzen,  nhd.  schneuzen j  norw.  snüi m.  , Schnauze',  nhd.  Schnauze-^
mit  p:  mhd.  snupfe,  aisl.  snoppe  , Schnupfen',  mhd.  snüfen  ,schnaufen', snüben  , schnauben'  u.  dgl. ;  nach  Wissmann,  Nom.  postverb.  178  f.  sind germ.  snuh-,  snup-,  snud-,  snut-j  snug-,  snuk-  lautmalend  (wie  auch  snab-, snap-,  snad-,  snat-,  snalc-,  ebda.  187  f.),  nach  Johannesson  223  f.  gehören sie  zu  snu-  ,schnauben,  pusten',  also  zu  obigem  *swew-;
mit  idg.  t\  mhd.  snudel,  snuder,  snüde  , Schnupfen',  ahd.  snüden  , schnau- ben, schnarchen',  aisl.  snydja  , schnüffeln,  wittern  (vom  Hund)',  snudra, snodra  ds. ;
--- leaf 215
 vfj  ,spinnt'  (*avi^isL',  evvr]  ,nebat',  ivvvriTog  ,gut  gesponnen'  erweisen Anl.  sn-),  Fut.  vrjCTio ;  vrjd^ü)  ,spinne',  vfjf,ia  , Gespinst,  Faden'  (=  lat.  nemen)^ vfjffig  ,das  Spinnen'  (:  ahd.  nät  ,Naht'),  vfiTQOv  , Rocken';  vcj^svogj  vwvra Gramm,  wohl  aus  *v7j-önevog,   ^yrjovTa',
lat.  neöf  nere  {*sne-iö)   ,spinnen',   nemen  , Gespinst,   Gewebe',   netus  ds. ;
mir.  smid  , dreht;  bindet,  quält,  müht  sich  ab';  cymr.  nyddu  ,nere',  corn. nethe,  mbret.  nezaff  ds.  {*sn(i){ö);  mir.  snim  m.  ,das  Spinnen,  Drehen;  Kum- mer'; Abtönung  snö-  in  air.  snäth{e)  , Faden',  bret.  neud  ds. ;  (aber  cymr. ysnoden  ,lace,  band',  corn.  snod  ,vitta'  aus  engl,  snood  ,Haarband');  air. snäthat  ,Nadel',  cymr.  nodwydd  ,acus,  acicula',  acorn.  notuid,  mbret.  na- doez  ,Nadel*;
ahd.  näu  ,nähe*  (=  lat.  neö,  gr.  vfj,  ai.  snäyati^  doch  ohne  s-),  nät  jNahV ; got.  neplttj  aisl.  näl,  ahd.  nädala,  ags.  nädl  f.  ,Nadel'  (aisl.  snälda  , Hand- spindel', wohl  umgestellt  aus  *snäd[i]la)]  *snö'  in  agutn.  snöp,  nschwed. snod{d)  , Schnur',  ags.  snöd  f.  , Kopf  binde'  (:  air.  snäthj  lett.  snäte)-^
lett.  snäjuj  snät  ,locker  zusammendrehen,  spinnen',  snäte,  snäne,  snät{e)ne f.  ,leinene  Decke';  s-los;  ndtns  ,leinen,  zwirnen*,  nät{e)ne  =  snät{e)ne]  *m- als  Schwundstufe  zu  *7iei-  (s.  o.  ai.  nlvi-)  in  lit.  nytis  ,Hevelte  oder  Weber- kamm', lett.  nits  ,Teil  des  Webstuhls',  aksl.  "^nith  , Faden,  Strick',  russ. nith  , Faden',  skr.  niti  , Weber trumm'.
--- leaf 216
, schneien*,  pamir §ugni  ^9nij  , Schnee*,  (*snaiga-)'j  gr.  yicpa  Akk.  ,Schnee*,  hom.  äydwKpo^ ,sehr  beschneit*^  vslq)eL  (ytcpsi)  ,es  schneit',  viq)dg  , Schneeflocke*  (nyertÖ , Schneegestöber*),  lat.  nix,  nivis  jSchnee*,  nivit  ,es  schneit'  (wohl  i);  Nasal- präs, ninguit  (ninxit)  ds.;
ir.  snigid  ,es  tropft,  regnet*,  snige  n.  ,Tropfen,  Fließen*,  snecht(a)e  , Schnee* (zum  ^Formans  vgl.  vicpSTÖg)]  cymr.  nyf  , Schnee',  nyfio  ,schneien';
ahd.  ags.  sniwan  , schneien*  (st.  V.,  Fartiz.  gi-snigan,  vgl.  noch  nhd.  bair, Partiz.  geschniwen ;  sonst  nhd.  schw.  V.),  aisl.  snyr  ,es  schneit'  (Partiz.  snißnn jverschneit') ;  got.  snaiws  , Schnee'  =  ags.  snäw,  ahd.   sneo  (Gen.   snewes)*
lit.  sniegas,  lett.  sniegs  (Vokal  vom  Verb  übernommen)  , Schnee*,  snaXgala ^Schneeflocke',  sniega  ,es  schneit',  Inf.  smgtij  apr.  snaygis  , Schnee',  aksl» sn4g^  , Schnee*.
V^P.  II  695,  WH.  II 169  f.,  Trautmann  272f.,  Vasmer  2,  680,  R.  L.  Turner BSOAS  18,  449 f.;  vgl.  ai.  snihyati  ,wird  feucht,  heftet  sich*,  sneha-  m.  ,Kle- brigkeit,  Öl,  Fett*.
--- leaf 217
g ;  övvQi^saL '  ödvqsr  au  Hes. ; Uihd.  snarren  , schnarren^  schwatzen',  snerren  ^schwatzen',  snurren  ,rauschen, sausen",  snurrcere,  srmrrinc  , Spaßmacher,  Narr',  nhd.  schnarren,  schnurren, Schnurre,  engl,  snarl  ^knurren',  mengl.  snorin,  nengl.  snore  ,schnarchen', mengl.  sneren,  nengl.  sneer  ^verächtlich  lachen';  mengl.  nurnen  /hersagen', ßchwed.  dial.  norna,  nyrna  ,zuflüstern',  aisl.  norn  , Schicksalsgöttin',  mhd. ^arreUj  nerren  ,knurren',  ahd.  narro  ,Narr*;
lit.  niürniuj  niurneti  ,brummen,  knurren';  lett.  nura  ,ein  weinerlicher Mensch',  nurdt  ,brummen,  spinnen  wie  eine  Katze^
Auf  -d\  mengl.  snurtin  ,schnarchen^  mhd.  snarz  , Schnarre,  Wachtel- könig'; lett.  nurdet  , murren,  brummen,  knurren'.
Auf  -g:  norw.  schwed.  snerka  ,prusten,  schnarchen',  schwed.  snurka ,rÖcheln',  mnd.  snorken,  snarken  , schnarchen,  schnauben',  mhd.  snarchen ds.,  nhd.  schnarchen'^  norw.  nurka  ,knarren,  knurren',  ndl.  nurken  ,brum- men,  nörgeln';  lit.  snarglys  , Nasenschleim',  lett.  snurgalas  ds.  (,*rasselnd, röchelnd');  snirguot  , schluchzen;  fauchen  wie  die  Gänse';  lett.  nir^guoties jhöhnisch  lachen',  nui^gt  ,die  Zähne  zeigen';  auch  wohl  lit.  narglyti  ,etwas langsam  tun'  (Bed.  ähnlich  wie  in  Schweiz,  norggen  ,ohne  Erfolg  arbeiten').
Auf  -k:  aisl.  sngrgla  (*snargulön)  , röcheln',  nhd.  nörgeln,  nergeln  ,un- deutlich  sprechen,  mit  verdrießlichem  näselnden  Tone  tadeln';  lit.  niurksaü, -öti  , düster  oder  brütend  dasitzen',  lett.  üurk'et,  nufkstet,  nurkset  ,brummen, murren,  knurren',  n^rka  ,ein  weinerlicher  Mensch',  nafkäet , weinerlich  sein, knarren',  nirkstet  ,knirschen,  ein  Geräusch  machen,  als  ob  etwas  bricht*, mirkt  ,knirschen'.
```


## [2026-09-14T02:28:51.986Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD sol-\"; grep -n \"^sol-\" -A 25 AHD_watkins1985.txt | head -40\necho \"=== AHD sophos\"; grep -n -i \"sophos\\|sophomore\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-14T02:28:52.059Z] TOOL RESULT

```
=== AHD sol-
969:sol-
970-b. metathesized form *nerwo- in Latin nervus, sinew: NERVE; ENERVATE. [Pok. snéu- 977.]
971-sneg-. To creep; creeping thing. 1. Suffixed o-grade form *snog-on- in Germanic *snak-6n- in Old English snaca, snake: SNAKE. 2. Variant Germanic root *sneg- in suf- fixed o-grade form *snag-ila- in Old English snzxg(e)l, sneg(ejl, snail: SNAIL. [Pok. ? sneig- 974.]
972-sneigh-. Snow; to snow. 1. Suffixed o-grade form *snoig’h-o- in Germanic *snaiwaz in Old English sndw, snow: SNOW. 2. Zero-grade form *snigvh- in Latin nix (stem niv-), snow: NEVE, NIVAL, NIVEOUS. [Pok. sneigth- 974.]
973-sneit-. To cut. 1. Germanic *snithan in Dutch snijden, to cut: SNICKERSNEE. 2. Expressive Germanic *snitt-ja- in Middle High German sniz (> German Schnitz), slice: SCHNITZEL. [Pok. sneit- 974.]
974-sner-. Expressive root of various verbs for making noises. 1. Germanic *sner- in North Frisian sneere, scornful remark, perhaps akin to the possible source of SNEER. 2. O-grade form *snor- in Germanic *(s)nor- in: a. Middle High German snurren, to hum, whirr: SCHNORRER; b. German snarchen, to snore: SNORKEL; c. Middle Low German snarren, to snarl: SNARL!; d. Middle English snoren, to snort: SNORE; e. Middle English snorten, to snort: SNORT; f. possibly Old Norse Norn, goddess of fate (< “the whisperer”): NoRN. Compare snu-. [Pok. 1. (s)ner- 975.]
975-(s)ner-. To wind, twist. 1. Suffixed extended zero-grade form *snork- in Germanic *snarh-6n- in: a. Old Norse snara, cord, noose, trap: SNARE}; b. Dutch snaar, string: SNARE?. 2. Proposed by some as a derivative of this root is Germanic *narwa- in Old English nearu, narrow: NARROW. 3. Extended variant form *(s)nark- in Greek narké, cramp, numbness: NARCO-, NARCOSIS, NARCOTIC. [Pok. 2. (s)ner- 975.] sneubh-. To marry. 1. Latin niibere, to marry, take a husband: NUBILE, NUPTIAL; CONNUBIAL. 2. Possibly nasalized zero-grade form *nu-m-bh- in Greek numphé, nymph, bride: NYMPH. [Pok. sneubh- 977.]
976-sneudh-. Mist, cloud. Latin nibés, cloud: NUANCE. [Pok. 2. sneudh- 978.]
977-sneud(h)-. To be sleepy. Expressive root. Compare snu-. Zero-grade form *snud-to- giving *nusto- in Greek nusta- zein, to be sleepy: NYSTAGMOUS. [Pok. 1. sneud(h)- 978.] snu-. Imitative beginning of Germanic words connected with the nose. 1. Germanic *snit-, *snut- in: a. Old English gesnot(t), nasal mucus (ge-, collective prefix; see kom): SNOT; b. Middle Dutch snut(e), snout, akin to the probable source of Middle English snute, snout: SNOUT; c. German Schnauze, snout: SCHNAUZER, SCHNOZZLE. 2. Germanic *snuf- in: a. Low German or Dutch snuffe- len, to sniff at: SNUFFLE; b. Middle Dutch snuffen, to snuffle: SNUFF!; c. Old English *snyflan (> Middle English snyvelen), to run at the nose: SNIVEL; d. Middle English sniffen, to sniff: sNirF. 3. Germanic *snup- in Dutch snoepen, to eat on the sly, pry: SNoop. 4. Ger- manic *snip- in Low German and Dutch snippen, to snap at: snip. 5. Germanic *snap- in Middle Low German and Middle Dutch snappen, to snap at: SNAP. 6. Germanic *snub- in Old Norse snubba, “to snub, turn up one’s nose at,” scold, rebuke: SNUB. 7. Germanic *snak- in Middle Dutch snakken, to snap at, akin to the Low German source of Middle English snacchen, to snatch: SNATCH. [In Pok. snd- 971.] so-. This, that (nominative). For other cases see to-. 1. Greek ho (nominative plural Aoi), the: HOI POLLOI. 2. Feminine form “syd in Germanic *sjé in Old English séo, sie, she: SHE. 3. Compound variant form *sei-ke (*-ke, “that”; see ko-) in Latin sic, thus, so, in that manner: sic}. [Pok. so(s), sd, si 978.] sol-. Also sole-. Whole. I. Basic form *sol-. 1. Suffixed form *sol-ido- in Latin solidus, solid: SOLID; CONSOLI- DATE. 2. Suffixed form *sol-wo- in Greek holos, whole: HOLO-; CATHOLIC. 3. Dialectal geminated form *soll-o-
978-spé-'
979-in: a. Latin sollus, whole, entire, unbroken: SOLICITOUS; b. Latin sollemnis (second element obscure), celebrated at fixed dates (said of religious rites), established, relig- ious, solemn: SOLEMN. II. Variant form *sob-. 1. Suffixed zero-grade form *sb-u- giving *sal-u- in Latin saliis, health, a whole or sound condition: SALUBRIOUS, SALU- TARY, SALUTE. 2. Suffixed zero-grade form “slo-wo- giv- ing *sala-wo- in Latin salvus, whole, safe, healthy, uninjured: SAFE, SAGE?, SALVAGE, SALVO!, SAVE!, SAVE. [Pok. solo- 979.] sp6-1. To thrive, prosper. Contracted from *spea-. 1. Suf- fixed o-grade form *sp6-ti- in Germanic *spddiz in Old English spéd, success: SPEED. 2. Suffixed form *spé-s- in Latin spés (plural spérés), hope, with denominative spérdre, to hope: DESPAIR, ESPERANCE. 3. Suffixed zero-grade form “spo-ro- in Latin prosperus, favorable, prosperous (traditionally regarded as from pro spéré, according to one’s hope; pro-, according to; see per’): PROSPER. [Pok. 3. sp(h)éi- 983.] spé-?. Long, flat piece of wood. Contracted from *speo-. I. Basic form *spé-. 1. Germanic *spé-nu- in: a. Old English spén, chip of wood, splinter: SPOON; b. Old Norse spdnn, shingle, chip: SPANNEW. 2. Possibly Greek sphén, wedge (formation unclear; earliest Greek form *sphdan): SPHENE, SPHENO-. II. Suffixed zero-grade form *spa-dh-. 1. Germanic *spadan in: a. Old English spadu, digging tool: sPADE!; b. Middle High German spat (> German Spat), spar: SPATHIC. 2. Greek spathé, broad blade: SPADE?, SPATHE, SPATULA, SPAY. [Pok. sp(hjé- 980.] spei-. Sharp point. I. Basic form *spei-. 1. Germanic *spituz in Old English spitu, stake on which meat is roasted: sPIT?. 2. Germanic *spitja- in German spitz, pointed: spitz. 3. Germanic *spi-ra- in: a. Old English spir, slender stalk: SPIRE!; ACROSPIRE; b. possibly Mid- dle Dutch spierlinc, a small, slender fish, smelt, akin to the source of Old French esperlinge, smelt: SPARLING. 4. Germanic “spik- in Old Norse spik, nail, perhaps akin to the possible source of Middle English spyk, spike: SPIKE}. 5. Germanic *spil- in Middle Low German spile, wooden peg: SPILE, SPILL?. 6. Suffixed form *spei-nd in Latin spina (> Old French espin), thorn, prickle, spine: SPINE, SPINEL, SPINNEY; PORCUPINE. 7. Suffixed form *spei-kd in Latin spica, point, ear of grain: SPICA, SPICA, SPICULUM, SPIKE?. IT. Extended o-grade form *spoig- in Germanic *spaik6én- in Old English spdca, spoke: SPOKE}. [Pok. 1. sp(hjéi- 981.] (s)peik-. Bird’s name, woodpecker, magpie. 1. Suffixed form *peik-o- in Latin picus, woodpecker: PICARO, (PICKET), (PIKE!), (PIQUE). 2. Suffixed form *peik-d- in Latin pica, magpie: PICA2, PIE2. [Pok. (s)piko- 999.] spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-6n-, watcher, in Old Italian spione, spy: ESPIONAGE. 2. Suffixed form *spek-yo- in Latin specere, to look at: SPECIMEN, SPECIOUS, SPECTA- CLE, SPECTRUM, SPECULATE, SPECULUM; ASPECT, AUS- PICE, CIRCUMSPECT, CONSPICUOUS, DESPISE, EXPECT, FRONTISPIECE, INSPECT, INTROSPECT, PERSPECTIVE, PROSPECT, RESPECT, (RESPITE), RETROSPECT, SUSPECT. 3. Latin speciés, a seeing, sight, form: SPECIES; ESPE- CIAL. 4, Latin -spex (< *-spek-), “he who sees,” in: a. haruspex, diviner (see ghere-); b. auspex, augur (see awi-). 5, Suffixed form *spek-d- in Latin (denominative) déspicari, to despise, look down on (de-, down; see de-): DESPICABLE. 6. Suffixed metathetical form *skep-yo- in Greek skeptesthai, to examine, consider: SKEPTIC. IT. Ex- tended o-grade form “spoko- metathesized in Greek skopos, one who watches, also object of attention, goal, and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE. [Pok. spek- 984.] spel-'. To split, break off. 1. Extended form *speld- in Germanic *spilt- in Middle Dutch spelte, wheat (prob-
980-sper-4
981-ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
982-spere-
983-spréot, pole (< “sprout, stem”): sPRIT; d. Middle English bouspret, bowsprit: BOwsPRIT. 3. Extended form *spreit- in Germanic *spraidjan in Old English sprédan, to spread: SPREAD. II. Basic form *sper-. 1. Suffixed form *sper-yo- in Greek speirein, to scatter: Diaspora. 2. Suf- fixed form *sper-mn in Greek sperma, sperm, seed (< “that which is scattered”): SPERM}. III. O-grade form *spor-. 1. Suffixed form *spor-d- in Greek spora, a sowing, seed: SPORE, SPORO-. 2. Suffixed form *spor-nd- in Greek sporas (stem sporad-), scattered, dispersed: SPORADIC. [Pok. 2. (s)p(hJer- 993.]
984-spere-. Ankle. Zero-grade form *spr(o)-. 1. Germanic suffixed form *spur-6n- in Old English spura, spora, spur: SPUR. 2. Nasalized form “spr-n-o- in Germanic *spurnon in Old English spurnan, spornan, to kick, strike against: SPURN. 3. Germanic suffixed form *spur- am in Middle Dutch spor, spoor, track of an animal: Spoor. [Pok. 1. sp(hJer- 992.]
985-spergh-. To move, hasten, spring. Nasalized root form *sprengh-. 1. Germanic *springan in: a. Old English springan, to spring: SPRING; b. Middle Dutch springen (> Dutch springen and Afrikaans spring), to leap: KLIP- SPRINGER, SPRINGBOK; C. Old High German springan, to jump: GELANDESPRUNG. 2. Germanic causative *sprang- Jan in: a. Old English besprengan, to sprinkle, scatter: BESPRENT; b. Old English *sprencg, snare used to catch game: SPRINGE. [Pok. spergh- 998.]
986-(s)peud-. To push, repulse. 1. Latin pudére, to feel shame: PUDENCY, PUDENDUM; IMPUDENT. 2. Latin repu- dium, a casting off, divorce (re-, off; see re-): REPUDIATE. [In Pok. péu- 827.]
987-sping-. Also ping-. Bird’s name, sparrow, finch. Ger- manic *finki- in Old English finc, finch: FINCH. [Pok. (s)jpingo- 999.]
988-[spirare. To breathe. Latin word of unknown origin, with its derivative spiritus, breath, breath of a god, inspira- tion: SPIRACLE, SPIRIT; ASPIRATE, CESSPOOL, CONSPIRE, EXPIRE, INSPIRE, PERSPIRE, RESPIRE, SUSPIRE, TRAN- SPIRE. [In Pok. peis-, speis- 796.]]
989-splei-. To splice, split. Extension of spel-1. 1. Germanic *fli- in: a. Old English flint, flint: FLINT; b. Norwegian flindra, splinter, akin to the Scandinavian source of Middle English flendris, bits, splinters: FLINDERS. 2. Germanic “*spii- in: a. Middle Dutch splinter, splinter: SPLINTER; b. Middle Dutch splitten, to split: SPLIT; c. Middle Dutch splissen, to splice: SPLICE; d. Middle Low German and Middle Dutch splente, splinte, splint: SPLINT. [Pok. (s)plei- 1000.]
990-(s)poi-mo-. Foam. 1. Variant form *poimo- in Germanic *faimaz in Old English fam, foam: FOAM. 2. Variant form *spoimaé in Latin spiima, foam: SPUME. 3. Suffixed reduced form *poim-ik- in Latin pimex, pumice (from its spongelike appearance): POUNCE?, PUMICE. [Pok. (s)poimno- 1001.]
991-spreg-. To speak. Germanic *sprek-, *spek- (with Ger- manic loss of r) in: a. Old English specan, to speak: SPEAK; b. Germanic compound *bisprekan (*bi-, about; see ambhi) in Old English bisprecan, besprecan, to speak about: BESPEAK; c. Old English spréc, spéc, speech: SPEECH. [In Pok. (s)p(h)ereg- 996.]
992-(s)preg-. To jerk, scatter. 1. Germanic *sprek-, *frek- in: a. Middle Dutch sprenkelen, to sprinkle, akin to the possible source of Middle English sprenklen, to sprinkle: SPRINKLE; b. Old Norse freknur, freckles (< “that which is scattered on the skin”): FRECKLE; C. Swedish dialectal spragg, twig (< “that which is jerked off a branch”), akin to the Scandinavian source of sPpRAG; d. Swedish dialec- tal sprygg, brisk, active, akin to the Scandinavian source of sPRY. 2. Zero-grade form *sprg- in variant *sparg- in Latin spargere, to strew, scatter: SPARGE, SPARSE, SPURRY; ASPERSE, DISPERSE, INTERSPERSE. [Pok. (s)p(h)ereg- 996.]
993-spyeu-. Also speu. To spew, spit. Expressive root. 1. Germanic *spitjan in Old English spittan, to spit:
994-sta-
=== AHD sophos
```


## [2026-09-14T02:29:04.211Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full block\"; sed -n '79310,79360p' POK_full.txt\necho \"=== POK_03 grep solo\"; grep -n \"solo-\\|sollus\\|salvus\" POK_03.txt | head -20"
}
```


### [2026-09-14T02:29:04.305Z] TOOL RESULT

```
=== POK_full block
Page(s): 978 

Root / lemma: soi-to- 
Meaning: sorcery' 
See also: see above S. 891 {se-). 
Page(s): 979 

Root / lemma: solo-, sol(e)uo- 

Meaning: whole, integrate 

Note: 

Root/ lemma: solo-, sol(e)uo-\ "whole, integrate' derived from Root/ lemma: sal-\ "salt; 

salty water'. 

Material: Old Indie sarva-^ unbroken, unmarred, unscathed, undamaged, whole, all, each, 

every ', Avestan haurva-, ap. haruva- " unbroken, unmarred, unscathed, undamaged, 

whole' (= gr. oKoc,, ouKoq, alb. gja/e, compare also Latin salvus). Old Indie sarvatat(i)-^ 

intactness, completeness, entireness, wholeness, welfare, salvation', Avestan haurvatat- 

"Ganzheit, Vollkommenheit, welfare ' (= gr. 6A6Tr|<;); Armenian olj{*solio-) "fit, healthy, 

whole, complete '; gr. Attic oKoc,, Ionian ouAo(; (*6AFo(;) " complete, whole', Vok. ouAs (: 

Latin sa/i/efrom *salve) through reinterpretation to an Imperativ); 

besides with vollerer Formansstufe oKobc, (from *6A£F6(;), oAosTtqi uyiaivsi Hes.; alb. 
gjale, ^/Me "strong, fat, alert, awake, smart', ngjal, ngjairbe\ebe, heal, fatten' {*soluo-); 
zero grade: Latin salvus^beW, fit, healthy, gerettet', salve {see above), Umbrian sal(u)uom 
"salvum', Oscan sa/ai/s "salvus', Paelignian SalauaturPH "Salvator' from * salvo- {*saluuo- 
or *salouo-= gr. oKobc^, Latin salus, -//s"Unverletztheit, haleness, healthiness, 
Wohlergehen', salu-bris "the haleness, healthiness zutraglich', Sallustius (with lengthened 
-/A); besides *solos\x\ soli-dus, soldus ^ dense = gediegen, massiv' and "tight, firm, 
complete, whole', so/dv "dense, filzig', solidare^ to make firm or solid ', Paelignian solois 
"omnibus'; 



Italian *sollos {*sol-no-) in Old Latin sollus '\.o\\is et solidus', Latin sellers, sollemnlsetc, 
Oscan sullus 'omnes'; but cymr. bret. holl, oil, corn. oZ/'whole, all', belong to Old Irish oil 
(above S. 24); Tocharian A salu' complete ', B 5C»/-/77e 'whole'. 

References: WP. II 510 ff., WH. II 471 ff., 555 ff.; 

See also: perhaps in ablaut to sel-, above sel-6S. 900. 

=== POK_03 grep solo
2966:Ai.  sdrva-  ,unversehrt,  ganz,  all,  jeder',  av.  haurva-,  ap.  haruva-  ,un- versehrt,  ganz'  (=  gr.  olog,  ovlog,  alb.  gjale,  vgl.  auch  lat.  salvus),  ai.  sar- vdtat(i-y  , Unversehrtheit,  Wohlfahrt,  Heil',  av.  haurvatät-  , Ganzheit,  Voll- kommenheit, Wohlfahrt*  (=  gr.  SlÖTrjg);  arm.  olj  (*sol{o-)  ,gesund,  ganz, vollständig';  gr.  att.  oXog,  ion.  odXog  {*öXJ^og)  ,vollständig,  ganz',  Vok.  odXs (:  lat.  salve  aus  *salvU)  durch  Umdeutung  zu  einem  Imperativ);
2970:schwundstufig:   lat.   salvus  ,heil,  gesund,  gerettet',   salve  (s.  oben)," sal(u)uom  ,salvum',  osk.  salavs  ,salvus',  päl.  Salauatur  PN  ,Salvatoi *salvo-  (*saluuo-  oder  *salouo-  =  gr.  oloög),  lat.  salüs,  -tis  ^UnverletxtJ^ Gesundheit,  Wohlergehen',  salü-hris  ,der  Gesundheit  zuträglich*,  /Saoii^J (mit  gedehntem  -11-);  daneben  *solos  in  soli-dus,  soldus  ,dicht  =  gedi«f^  I massiv'  und  ,fest,   vollständig,   ganz',   solöx   ,dicht,   filzig',   soUdürt  ^J^ machen',  päl.  solois  ^omnibus' ;
2971:ital.  *sollos  (*sol-no-)  in  altlat.  sollus  ,totus  et  solidus',  lat.  sollers,  wZZ«^; usw.,  osk.  sullus  ,Dmnes';  aber  cjmr.  bret.  holl,  oll,  com.  oll  ^ani^  ||fi gehören  zu  air.  oll  (oben  S.  24);  toch.  A  salu  ,vollständig*,  B  sol-me  ,gt^-
```


## [2026-09-14T02:29:05.670Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT haurva\"; grep -n \"haurva\" BRT.txt | head -30\necho \"=== BRT haurvatat\"; grep -n \"haurvatāt\\|haurvatat\\|hauruuatāt\" BRT.txt | head -20"
}
```


### [2026-09-14T02:29:05.783Z] TOOL RESULT

```
<persisted-output>
Output too large (30.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bjbd3t548.txt

Preview (first 2KB):
=== BRT haurva
3368:—  yaisa  ni  d.ltl  . .  ''i^a  nä  >rJedüm  V. 5^-5>35-^'> — yit^ä  iä^aca  dahms  staota yesnya  haurva  daoaiti  '%a  ratu/rii  N. 3~;  —  yd^a  . .  nminopaitlm  paiti  tard.- pi'iw>m  dai'hyat  'ia  astryäH  "als  ob  er
3397:•  j.  aihaurvan- '':a^a«r»n-,  äSravan-'' m,  'Priester'  im  Al!g e meinen ,  von  dem, der  Priestetqualität  besitzt  und  priester- liche Funktion  verrichten  kann  und  darf: uUa  nS  zlte  -va  .,  zara^uslrS  YLi_y.94;
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['
...
</persisted-output>
```


## [2026-09-14T02:29:13.635Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nimport re\nlines=t.split('\\n')\n# find leaf index of line 2966\noff=sum(len(l)+1 for l in lines[:2965])\nleaf=t[:off].count('\\f')\nprint('leaf(0-based ff count)=',leaf,'-> awk NR==',leaf+1)\nprint(t.split('\\f')[leaf][:1500])\nEOF"
}
```


### [2026-09-14T02:29:14.979Z] TOOL RESULT

```
leaf(0-based ff count)= 220 -> awk NR== 221
av.  höi,  jav.  he,  se,  s^p.  Jaiy,  gr. OL  ,ihm';
daneben  ein  erweit.  St.  s{i)io-,  s^ijiä-:  ai.  5i/a/z  und  (nach  «a)  sya  m. syä  f.,  ap.  Ä?/a^  m.,  hya  f.;  vielleicht  air.  se  ,dies'  aus  *siod,  und  -se,  -sa particula  augens  der  1.  Sg.;  sehr  unsicher  ist  Zurückführung  von  aisl.  siä jdieser'  auf  ein  altes  *sio.
Fem.  *sf:  gr.  l  ,sie'  (Soph.),  air.  sl  ,sieS  got.  si,  ahd.  sl,  si  ,sie';  dazu nach  Rosenfeld,  Forsch,  u.  Fortschr.  29,  176  schwachtonig  si  in  urnord. si-ainaR  Jener',  sa-si  , dieser',  su-si  , diese*,  pat-si  , dieses';  genus-indifferent sind  Akk.  ai.  slm,  av.  hlm,  ap.  sim.
WP.  II  509,  Wackernagel-Debrunner  III  536  ff.,  Schwyzer  Gr.  Gr.  1, 610  f.,  Pedersen  Toch.  113  f.
toi-to-  jZaubereiS  s.  oben  S.  891.
tolo-,  sol(e)uo-  u.  dgl.  ,wohlbehalten,  ganz^
Ai.  sdrva-  ,unversehrt,  ganz,  all,  jeder',  av.  haurva-,  ap.  haruva-  ,un- versehrt,  ganz'  (=  gr.  olog,  ovlog,  alb.  gjale,  vgl.  auch  lat.  salvus),  ai.  sar- vdtat(i-y  , Unversehrtheit,  Wohlfahrt,  Heil',  av.  haurvatät-  , Ganzheit,  Voll- kommenheit, Wohlfahrt*  (=  gr.  SlÖTrjg);  arm.  olj  (*sol{o-)  ,gesund,  ganz, vollständig';  gr.  att.  oXog,  ion.  odXog  {*öXJ^og)  ,vollständig,  ganz',  Vok.  odXs (:  lat.  salve  aus  *salvU)  durch  Umdeutung  zu  einem  Imperativ);
daneben  mit  vollerer  Formansstufe  öXoög  (aus  ^öXeJ^ög),  öXosTrai '  vyialveL Hes.;  alb.  gjale  , kräftig,  fett,
```


## [2026-09-14T02:29:15.134Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT haurva- headword context\"; grep -n \"haurva-\" BRT.txt | head -20\necho \"=== BRT 'Ganzheit'\"; grep -n \"Ganzheit,  Voll\\|Ganzheit\" BRT.txt | head -10"
}
```


### [2026-09-14T02:29:15.203Z] TOOL RESULT

```
=== BRT haurva- headword context
4775:•j.,g.am»rBta'^t-,  amarBtlt-'T.'Unsterb- lichkeit.  Ewigkeif;"'  tit  d^hnaotä  maslm hujyiH5is{sA)  "ntstascä  Y._j2. 5 ;  —  'rstSitl *a^aonö  urvä  also  (sd.)  utayütä , ,  Y.  43. 7 ; 48. 1 ;  —  yä  fyat/^an/t . .  -ntäbm  astmcä *taibyO  danhä  (sd.)  .  .  xs^nm^a  haurva- tätö  Y.34-^i  —  ahmäi  aahat  vahiihm yi  möi  vtdva  vaolat  hai~ilm  mq^r^m  yim haurvatatö  alahyä  'ritatasca  "dem  soll das  Beste  zu  Teil  werden,  der  mir,  ein: Wissender,  ktmd  tut  das  rechte  Wort  Aia^ von  der  Wohlfahrt  und  Unsterblichkeit" Y._3/.6.  a)  bes.  in  Dual  Verbindung  mit
11029:—  laimye  .  ,  uruiiaSca  Yt  i~.  22;  — kaittibyü  . .  xsmatbyaca  Y.  5y.  5 ;  —  haurva- tsts  ,  .  amfr.tälasca  Y.31.  6;  — jyai7u? ,. vasS-itdii^a  Y.5_j.9;  47.6;  —  yaää  hvB arf hat  yl.iyaoianasiäY  .31.16; — akurahya xratSiJ..aiaatca  Y._j2,4; —  yeMi  hatqm ..vanhs .. yärahqmlä ..  Y.2-.\y,  —  as>m  .. manasla  vohü  Y.  28.11;  —  aiaAya  .  . vaahSusca  manat^hs  Y.33.  3;  —  vanhSui manai3hs..syaokana . .  spmtqmia  armaitjm Y.34- 10;  —  Aatiuharyne  . .  hSyUmla  dH- ^nm  Y.ii.\;  —  tä  urvata  ..  :^Uicai> ^miti  Y.30. 11;  —  ;tarff  .  .  gju/cä  urz'a Yt/^S4;  —  masdä  yasrum^a  vahm9m?ä (beide  als  i.  Glied;  Sp.  567  u.)  ..  ^ulca västrpm  Y-33.  7 ;  —  vaahsui  xralüm nat9h3..gSusca*urvq>i»mY.28.\.  a)  in auffdlliger  Stellung:  yS  anhai  asul  . .  hu-
11071:Glieder  sind  verbal:  yBi  ztjvä  (nämL  hitOt) *ar»har3La  bvanticS{sA)\.4^.T.  3)bci allen;  a)  D  im  Ap.;  das  letzte  Mal  steht Uta  statt  cä:  pärsamcä  mädamcä  utä  aniyä dakyiivaf"  Bh.  /.  14.  b)  im  Aw,;  i)  die Glieder  sind  nominal ;  a)  sie  folgen  sich  un- mittelbar: nmänyasca  visyasca  santumasca Y.  if).  18  (s.  dazu  18  aA.);  —  aojasca  v»ty- 'inmca  j^armas^a  lavania  Y.  7/.  8 ;  —  sta- rasca  mäsca  >fe'<i/vi-'(7  YL72,25(s.dagegeni_j. 57);  —  vätftnca  vänmca  tnafy^mca  Jyau- humca  Yt  5.120; — hubprvtlmca  uslaMin- tlmca  vanta.bintTmca  Y.  61. 2  (s.  dagegen  7 ; Sp.  570U.);  —  maziUäsca  vahiitasca  srais- tas^a  asayS  Y.  52.  3;  —  apasca  urvaräsca xadirdsca  Y. A3;  —  asavafom  htnümca bavaniiinla  busyantimla  Yr.lS.i; — vTspayä ..slöis  haihyJica  bavqihyäica  büiyqi^yäica \.6S.i3i  —  nm3nanqmcä  vlsqm^a  satttu- nqmca  dahyunqmca  Y.  Ä  7 ;  —  damayä  anu- matayal'a  aiiuxtayaica  * aim.varstayai^a Y.Ä7;  —  d^aurunqscä  rä^aistiscä  väs- tryqscä  ßuyants  Y.  ig.  3;  Yt  ig.  8;  — ahamca  ratümca  paoirimca  tkaisim  Yt/^J. 152;  —  ha^ra  miiräca  rasnuta  uyraca dämSis  upamana  Yt/_J.  47;  —  vispss^a paiti  vansajls  vTspSsca  paiti  frasparrjJ i'JspSsca  paiti  fravaxsS  Y.  jo.  5 ; — haurva- tasca^  fiö  am)r>täta  gSuica  taSnB  gSusca urunS  ä%rasi-a  aoxtsjiämand  hadisasca  Vr. g.  5;  —  beim  Zahlwort:  navaia  navaittfca navaca  sota  navaca  Aazavra  navasSsca baivqn  Yl;_J.S9.  a)mitTmesis:*«ai/x
24604:1473  viSavä-  —  viS.haurva-  1474
24643:j.  vUspalä  Vyt.  31:  s.  viUSspa-  mit  No.  2. •  j.  viS.haurva-'*  Adj,,  mit  'j/o«-  m. 'Haus-,  Hof  hu  nd' :  kva  asH  sp3  'rvö  dlttyd.- gllus?  .  .  yS  hJhrS.masaii/um  ühwanim haca  vizibyö  parsi/i  sraissmnB  (sd.)  ISyäi v»hrk)m?a  "Bei  wem  ist  der  Hofhund richtig  am  Platz?  .  .  (Bei  dem)  der  eine /(j!i/-<ilange  Wegstrecke  von  seinem  Hof weggeht .."  V.  13. 18;  49',  5.  2i);~spatum .  .  yim  'rum  V.  13. 13,  21,  25;  —  süne 47
29577:•  j,  har-  V.  'Acht  haben  auf  -'.  Praes. 3  hara-,  20  haurva-;  Perf.  i  hankar-.  — Inf.  har>tayat-ca,  Aankmi.
29628:•  j-  (i  S)  haurva-,  p.  haniva-  Adj.  (fem. 'va-")  'ganz';  i)  sva.  'unverletzt,  unversehrt, heil';  dad)mahl  haurvafsavS  .  .  drva  *va (NPm.)  ttüvants  Y.  iß.  6.  2)  sva.  'ge- sammt,  vollständig':  \pasava''  kar<^  °va* /iami'äi''iya^  abava^  Bh.  i.  1 1 ;  1 6 ;  —  °v<^- iim  kära''  avaint/"  Bh.  2, 13,  14;  II  —  'vqm handaitlm  staotanqm  yesnyanqm  Y.  5^'.  8; —  vlsp>m  vacff  fravähm  (sd.)  °rum  vacS ahurahe  mazdä  \.  ig.  14;  —  'vqm  tarasca xlapamm  V.  ;&5,  6;  —  zusammen  mit vTspa-^^:  yO  vtspqm  'vqm  tansm  upanAan- zaiti  V,  6'.  24.  a)  Akk.  in  Verbindung mit  'da-  'etwas  ganz,  vollständig  machen,
29642:j.  haurva-paoirya-  Adj.  —  7  — :  tUrS paoirys  yaxamaide  . .  tisra  paoirya  . .  H/ra 'ya  . ,  tisrattam  'yanam  (soll  heissen)  "die erste  der  drei  ersten  CJäJs . .  die  beiden ersten  der  drei  ersten  Gdhäs  . .  alle  drei ersten  Gä^äs  . .  von  allen  drei  ersten ffaSss  . ."  Vr.  13. 3'».
29644:•  j.  haurva-ßav-  Adj.  'des  Haustiere unversehrt  sind';  pairX . .  dadrmahf  'fsavö (NP.)  Y.5Ä6.
=== BRT 'Ganzheit'
```


## [2026-09-14T02:29:22.894Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29645,29680p' BRT.txt | cut -c1-900"
}
```


### [2026-09-14T02:29:22.946Z] TOOL RESULT

```
PiL:  ^karA  ramak.  —  0  In  den  Hds.  »teht ik  als  Ideogiamm  für  an  'jener';  an  der  Stelle des  Urtextes  war   aber  an  n  vielmehr  har  in
•  j.,  g.  haurvSt-  f.:  s.  unter  haurvatät-.
•  j.  haurvo."päso  fralaostrs  naSrnS.- "paiwa  zardku/in>  N.  64.
A'  und  »'  ('gani-  . .  halb-')  sind  poss.Korop. mit  dem  nämlich«D  Schlassglied,  detsen  rich- tige Lesung  und  Bedeutung  nicht  la  ermitteln ist.     T  kaurvö.f<isä.  —  Pü.:  fehlt, j.,  g.  kaiirvis^i  s.  kaurvaläl: j.  kautvi  P.  33:  lies  kaurvi,  Sp.   179I   O.
•  j.  har^z-  V.  'entlassen'.  Praes.  J Aama-,  ^  hinza-,  1 7  (Ful.)  ^urj^a-",  14 kinzaya-,  27  htmya-,  —  PPfP.  'karsta-; Inf.  'harstayal-(a,  •harstSe,  'Airfzsm.
i)  'entlassen,  entsenden,  ausschicken': tä  (nämL  fravasayS)  htrjzntH  saiavaistm antarf  sam  asmammca  .  .  %rä%räi  Yt 13. 43.  '  a)  '(Wasser)  überlassen',  zur  Be- rieselung: mä^a  ..zqm  kärayin  (sd.)  mä  äpi> JarizayTn  yat  ahmt . .  V.  6'.  2 ;  a,  3.  s)  'mit Wasser    (usw.)    belassen,    benetzen':     s.
dby  Google
'harsia-.  2)  'an  seinem  Orte  belassen,,  la.         Undeutlich:  yä^a    dakmahe  fra-
liegen    lassen':    yezi   altim    iristpm    upa.-  nhanzdit  ii.ji''>{1).
b)r3'%wS.tarwt  (sd)  ava.zattan  ava  aitwt  ■  "'■  'ärjata^,  irjdli,  srjyäu  (Pass.).  j/-tffl*;  np, iristtm  baraym  ava^a  nmänim  h>may>n\  *'^'^'  ma.-V%.:  man,  (zu  N./5): /ö/övf. „  u-jT.  L-  'i^i    s-  noch  No.  2ff.    —    >)   GeeenOber  ai.
".  .  so  sollen  sie_  den  Toten  wegbringen,  .^aiffati.-')  Vh.-.  fa  an  i  hsm  {«})  parähim (und)  folglich  die  Behausung  belassen  |  n  pa /rahis»<'i  pa  raiJh  i  buland.  —  i)  HiiaXic^ (wo  sie  istj"  V.Ä2;3;  — yai,.matäa'  MurySjaoAa  Ata  JCavayb'saa; -v^.  Aaultn. yasna  upain  aitim  iristim  *avi.mam  kar>kS  \  ^-J"  3-  39-  —  <>  Pü.:  fehlt  -  s)  Pü  :  «ikhH, (sd.)  &>rje>'^^  (statt  Plur.)  ^o»«/  .  .  V.5.!  _  6)  ob  aus  iJ/ä%I*A  verderbt? 61.         4)  'durch  die  Seihe  lassen,  durch- 1
seihen,  filtriren':  >4fl(.Ma«fl«ra  Aar-^/yflOT- ,  •  J-  ■»«"f  «««">  -^ar^^j««-  n.  O  Lassen, nanam    ysi    har>^ente'  rakwe    hr^zaitc^"^^^^-        a)  'Durchlassen,  Filtern'. „      j"  j  c,       j        rr  ■         j-  KompE.  ~  Zum  V.  kant-,  —  ai.  lajyaBo-n.,
"und  der  zu  filternden  ZTaöOTazwe ige,  die  j     1,^.  LW.  a/oror/j«  'divonio'. gefiltert  werden  sollen  für  ,."  Vr.  i2.  "" mit  aba:  s.  Inf.
mit  ava  'verzichten   auf  — ,  ablehnen': ,     „ avanhinzämi     *janySis     ünqm    (sd.)     Y. ' 10.  15,
•  j.  Aarsta-  Adj.  (fem.  'fä-),   PPfP.:   S.
ritayat-ca,  'AarftJe,  •hartStSe
mit  aw'  und  fra  '(Samenflüssigkeit)  ent- '  !"£  '("nd)  ^^  entlassen', lassen,  ergiessen  in  -'  (Akk.) :  yö  nairikam  j      mit  apa  'abzulassen,  zu  erlassen':  xsai/nte cihravaitTm  .  .  xsuärä  avi  fraDhanzäiti  1  •*^-  ■  2>«/ö«  attahe  ähä  (sd.)  apatiharstse V.  JÄ  67 ;  *75.  7,  8;   —  yat  ma^yS  mahm  1 V.  5.  26. xÄay-i  aw  franhsmaiti  V.  Ä  32.  mit  «/«  'mit  Wasser  zu  belassen,  zu  be-,
mit  upa  i)  'hinwerfen,  hinfallen  lassen':  übergiessen':  attavat  apB  yavai  aSaeibyö^^ yö  astfm  upaakanzaiti  sünd  vä  para.- '  f näml.  haomaHbyS)  uparthanitse  "so  viel iristahe   . .   V,  ö.  10.  i)    'hinbringen  1  Wasser,  als  man  (braucht)  sie  (die  Haoma-
ZM-'d):  avai  hl  daxma  nsit  uf>aisAarnät\^-^^W)   z"  übergiessen"   N./o<?;  —  upa- Vd.;^;  ig.   Wertlos.         3) 'hegen  lassen':  .»•^«'■■^'''y"'*'''--^^'  ^"'^  haotaa  Vr.5.3. ys   vaslrtm    uparthansaiii   upairi   amm\     ^"r.^'- *""!■■;- ■'■'E'-rfJ:- V '^«>  ^' «rtj/;.«  V.  6.  23.  4)  'mit  Wasser  (usw.)  l     ^^  ,(^-„3^  (,i  v,.)-! p/apar  vadnn  ü»ttio.
belassen,  besprengen':  alte  daxma  upa-^  ~~  d  Attraktion;  s.  Dbr.  ALS.  88.  —  >»  D.i. nhamaSa  .  .  uru^WöMa  (sd.)  V.5.51;'  das  Ideogramm  von  *««i7nM,  Im  Urtext  stand —   s.   noch  Inf.  5)    '(Flüssiges)    ein-i     das  selbe  Won  wie  ^.108.    D«  wurde  lu
,         T  c  *'"•   verstummelt,  wofür  man  dana  das  Ideo-
giessen  in  -  :   S.  In£  .      ^^^^  schrieb.
mit  paiti:  s.  Inf.  I      .  .        v  .  ,.    t^,s     ,«     ,,,
mil>,W   und  /rä   '.ieder  los-,   „,.•)•  l>"»äyMima-  Adj,  PP.7(Ful.)M.:  s. lassen':  a^mf  dim  paiti fraah»rfzat'\rAc:ay  nartz: licss  er  ihn  wieder  los"  ¥.2.5  PüZ.»  •  p.  haldita-    m.   EN.    eines  Anneniers:
mit  pairi    'durchseihen,    filtriren':    äai\araxJ'    näm<^    anniniy^    °tahya  pu%^i^ *äsnatars  {sA.;  naml.  kairim  a»kaf\    yat  hauv  udapataiä  bäbirauv  Bh.j.  13. ..  to«^».  tüiriMnal  N.  75;  -'luum-  .  j    hasiMma-  Adj.  'der  Mehligste':  •»,« ta,r,.har,^mU  Y.  27  .(,•>;  -^  m,^_r„n,m  ^.^,,^    ^^^    „%Uili    rMm    imrm!  Y.
V.  14.  4=^>  Vt.  J.63;  — M^a-ra^ff  ..pairi.- '  ''supetl.  au»  ^kani-t).  —  ai.  .tflK<J«a-  Adj.  -
anhariiäbyB  Yt5.8.  '       Yv..:kandäxtärtumit;rpaahTäkih,  Sü.:  laglm-
mit    /mW    und  fra    '(SaraenflUssigkeit)  '       haHalaniam  punyma  iaslrena.  —  ')  Eine  greu-
enüassen':  "anya.tkaliais^)  näirika pairi      "='"'  Etymologie  bringt  Dst.  ZA.  /.  «3- xsudra  fraipharTsaiW^  Nik.  7.  •  j.hastra- n. 'Versammlung' uzw.  solcher,
mit/^j  i)'(eineWaffe)schwingen,schleu-  die  fUr  sich  einen  gemeinsamen  Gotics- dern(od.dgl.)':  s.  y^flwÄawl'a-.  2)  absol. :  dienst  abhalten  lassen'':  yS  *bil.hastnm 'Samen (flüssigkeit)  ergiessen,  begatten',  von  srävayäti  ratufryS^'>  *%ris.hastnm  srä- 1\tXGa:  y6{ri3.xsiLuströ)  arsnam/rauÄ3r>-  vaysnii^''  ivat  nitimsm  'rtm  aiskai  *ratu- sintqm    mazi^btn    aejS    übaraiti    Vt  14.  fritH  '^ri/*>  "wer  für  eine  Versammlung
BAiTüai-aHAi,  Attüu.  Wh.  57
dby  Google
I79S
haz-
hazanra-
1796
```


## [2026-09-14T02:29:24.890Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD harw\"; grep -n \"harw\\|hordād\\|hordad\\|xwardād\\|Hordād\" PHD.txt PHD_mackenzie.txt | head -25\necho \"=== NYB harw\"; grep -n \"^harw\\|harw \" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T02:29:24.964Z] TOOL RESULT

```
=== PHD harw
PHD.txt:396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
PHD.txt:767:all hamag, hāmist, hamoyén, har(w), harwin, harwisp, hambāstag.
PHD.txt:1719:each harw.
PHD.txt:1812:every harw, wisp.
PHD.txt:4384:Amahraspandan Wahman Ardwahišt (Urd-, Ašwahišt) Šahrewar Spandarmad Hordād Amurdād
PHD_mackenzie.txt:2858:harwin [hlwyn I M hrwyn] pl. all.
PHD_mackenzie.txt:2860:harwlsp [hlwsp' I M hrwsp] all.
PHD_mackenzie.txt:5931:   harwin, harwisp, hambastag.            apple seb.
PHD_mackenzie.txt:6463:each harw.                                   endurance pattugih.
PHD_mackenzie.txt:6518:every harw, wisp.                                  express (juice) hunidan.
PHD_mackenzie.txt:11400:aharwcz                      eu~.,.    azkamagih                  .AQ.Ht' , t)I
PHD_mackenzie.txt:11701:armcstgah     ~~                       harwispin             \t"U'~
PHD_mackenzie.txt:11702:armcst                 ,~              harwisp                  ,q,v~
PHD_mackenzie.txt:11703:xufs- l                   -,~          harwisp                 ,te..u~
PHD_mackenzie.txt:11798:harwin
=== NYB harw
```


## [2026-09-14T02:29:31.430Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"haurvatät\\|haurvatat\\|haurvaiät\\|kaurvatäl\\|haurvatäl\" BRT.txt | head -20"
}
```


### [2026-09-14T02:29:31.492Z] TOOL RESULT

```
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['s'a  spunta  Yt.Ä 38  ist  Einschiebsel,  s.  an-  No.  3.]
4775:•j.,g.am»rBta'^t-,  amarBtlt-'T.'Unsterb- lichkeit.  Ewigkeif;"'  tit  d^hnaotä  maslm hujyiH5is{sA)  "ntstascä  Y._j2. 5 ;  —  'rstSitl *a^aonö  urvä  also  (sd.)  utayütä , ,  Y.  43. 7 ; 48. 1 ;  —  yä  fyat/^an/t . .  -ntäbm  astmcä *taibyO  danhä  (sd.)  .  .  xs^nm^a  haurva- tätö  Y.34-^i  —  ahmäi  aahat  vahiihm yi  möi  vtdva  vaolat  hai~ilm  mq^r^m  yim haurvatatö  alahyä  'ritatasca  "dem  soll das  Beste  zu  Teil  werden,  der  mir,  ein: Wissender,  ktmd  tut  das  rechte  Wort  Aia^ von  der  Wohlfahrt  und  Unsterblichkeit" Y._3/.6.  a)  bes.  in  Dual  Verbindung  mit
4778:;von  Arn.  geschützten  Pflanzen",  in  Dual- verbindung mit  haurvatat-  (sva.  Wasser): 3^ar3%3m  myasdam  haurvatä  °r)tata  gäus huha  haomitnca para.haomamid Y.8.i;j.i, 4.1,  6.1T,  7.26.
6084:(als  Subj.)3>  ya  'sät  gSUs  taiä  (sd.)  mraet Y.4/i.g;'~  mq'ir^m  yim  haurvatatS  'iahyä amsntätaicä  (sd.)  Y.gi.d;  —  kä  "iswöi 'iä  (Vok.)  äka  (sd.)  arpdrfng  isyä  Y.48. 8;  —  daidl  'iä  (Volc)  tqm  ailm  vanhsui ayaptä  manaifhö  Y.  28. 7;  6;  —  yS  vi mazdii  ahurä  pairljasäi  .  .  maibyO  dävBi akvh..  Jj-iT/t/J  (sd.)  'iilihacaY.28.2;sj.i; —  yahä  'sät  hacä  gqm  vJäal  (sd.)  västryS Y.5:.5;  43.14;  —  a/M  ahmai  mazda  'iä a»haüT..  ys..  "und  dem  o  M.,  wird  es (das  Rind)  durch  A.  zu  teil  werden . ., der  .  ."  Y.50.  3;  —  yehya  mUi  'iät  haia vahistsm  . .  valdä  (sd.)  mazdä  Y.5J.  12; 27. 15;  —  yqm  da  . .  °säcä  cBü  raneibyä (sd.)  xinOiim  Y.^i.$;  —  yj  vlänaet  da- iipmcä  (sd.)  aäa'Samli  dangrä  mante  -ia (Instr.)  mazdä  ahurö  ".  .  durch  seinen kundigen  Berater  Aia,  er  MAh."  Y.  46. 17;  3^-  '3;  —  vahista  säsnanqm  (sd.) yqm  .  .  sästl  'sä  ahurJ  Y.  48.  3;  34.  12, 46.  2;  —  maxdä  *yä  da  'iä  vanhSui mayh  (sd.)  manauAs  Y.  4y.  a;  44- ij  — yezl  ahyä  °iä psi  mat  xiayehl  (sd.)  ..mazdä Y.44~  15;  —  at  ahyäi  'iä  mazdä  urvarS vaxiat{sA.)  Y.48. 6;  —  ätrJm  ..  aojSt»hvan- tsm  'iä  Y.34-4'i  —  ^^  adr'ärum  . .  dalnk saoiyantqm  yä  ^haJc?r?tll  'iäcTt  urväxsat (sd.)  y'34.\z;  —  ks  vä  'iä  äfraiiä  (sd.) Y.5/.  11;  44- S;  —  'sät  hacä..  vaidä (sd.)  yS  Im  dat  Y.  45.  4;  —  vidui  (sd.) 'iä  ySm  mazdqm  ahur?tn  Y.  4S-  8 ;  — va»kSui  'iä  Aaozq%7Väi  (sd.)  ä  mananhs Y.45.  9;  —  ärmatsii  kasilt  'sä  hutSntus (sd.)  Y.  49.  S;  —  tSm  vS  'sä  mShmaidt huiJiaxäim  (sd.)  Y.  46.  13;  —  mazdä ahurS  'iä  hui.haxä  ifmvatä  Y.  32.  2 ;  — mazdä  ..%wävqs..  at  ns  fryä  °iä  dazdyäi häkurmä  (sd.)  Y.  44.  i;  —  spmtaHyäiä tur?i.. yehya  urvä  'iä  haiaifl (sd.)  Y.34. 2 ;  44. 1  o,  46- 16;  —  neit  'iahyä  adlvyeintj (sd.)  *hacsna  Y.  44. 13;  —  'iä  vyqm  (sd.) yehyä  hihäui(sd.)  nä  spmtö  Y.4^.  7;  — ärmaitlm  ..hi%qm  (sd.)  'iahyä  Y. ^4- ro; 4ß.  16;  —  tqm  dainqm  .  .  yä  msi  gai'iih •iä  frädBit  haiSmnä\sA)  Y.  44. 10;  43. 6,  34.14,  44-to,  4o-i',  —  'iahyä..  sairJ (sd,)  'iahyä  Virszsm  Y.35.Z;  41.6;  — /praiaaiträi  urväzistqm  (sd.)  'iahyä  da. sarSm  Y.49-8;  5J.  3,  31. 2\;  —  'i^miä ^ fradat.gal%Jm  Y.  j;j.  1 1 ;  —  'ia  (Vok.) kal  %wä  dar}sänl  (sd.)  Y.2ÄS,  45.6,  ;^. 6;  —  humqsdrä  (sd.)  °ia  (Instr.)  yeiä  yä
29638:•  j-,  g.  haurvatat-,  baurvlt-'>  £  'Gani- heil, Vollkommenheit, Wohlfahrt"' :/5  Äaii- "^anä ..  armrftataiftn  astmcä  *taibyS  däahä (Sp.  744)  ..  xsahnmi^^.  544  \L)cä  •vatäts  Y. J4. 1 ;  — yf  msi . .  vaocät  katiim  ma^rpm yim  'vatäiö  asahyä  attantiliai(^A.)cä  Y. ^t.  6.  a)  bes.  in  Doalverbiodung  mit atmnttttat-:  diidl  mdi  .  .  ammtätä  'vä/ä s/Jms'ta  mainya  masdä  twih  utayüti  "gib mir . .  Unsterblichkeit  und  Wohlfidiit  durch den  heiligsten  Geist,  o  M.,  Kraft  und  Be- stand" Y.5/.7;  45.10,  44.18,  47.1;  — 10a  'Vota  amsrftata  yöi  sis  mistüm  aiao- nqm  parS.asü  Joimtam  Yt/.as;  —  matJ (sd.)  ^ra.fmS.hyäi  däidl  °vata  (OD.)  amsrf- mi  Y.5Ä7.  a)  als  Bezeichnung  fdr den  Trank  der  Seligen:  al  IBt  ubs  'vds- (HS.yica  ^anhäi  ä  am7r)talas{iA.)ia  Y. j4.11.  A}alsGottheit"(^M^/fl.^j«/<7), der  die  Sorge  für  die  Wasser  anvertraut  ist (SüEtL:  udaksdhipatih)*'>:  'vatättm  am?s?m spmtpm  Yt  4. 1  o" ;  —  aya  daStaya  fraormSa ahurS  mazdä  .  .frä  vohu  manS . .  as»m  . . x^a%r?m  . .  Srmaitii  frä  'vatät  frä  amirv- latäs  Y. 57.24;  —  vanät  •väs}a^'>  amiri- ihca  uva  h^imca  tarsmmca  Yt  ig.  96 ;  96 ; —  ärmaiUm  .  .  'vataUm  .  .  ammtatätim Y.16.3;  7/.  12,  S.2.6f.;  —  atf/n  da^atn •vatätö  narqm  ai'aonam  aväsca..  Yt.4-r  {f)', ■ — ■  mazdä  dadät  ahurS  "vatB  amfntslascä . .  sarff  (sd.)  Y.  _J/.  2 1 ;  —  dälä  vJ  amir?- tascä  utayäin  (sd.)  'vatäs  (NS.  als  VS.)^ draond  Y.  33.  &;  —  UätS  ra%wS  Yt. 4.0,  11;  2;  —  'vatasca  amir>tathsca yt.4-i(?)-  o)  bes.  in  Dualverbindung mit  amPTitatilt-.  {lya  dastaya  fraormla ahurB  mazdä .  .frä  'rata  (ND.)  amtr^täta Yt.  jo.  92;  —  saröi  buidyäi  (sd.)  'vätä am>r?tätä  Y.  44,  17;  —  upä.jimm  (sd.) •vatä  amtrmtä  (AD.)  Y.  45. 5;  —  yä spftitayä  ärmateii  yä  °vatä  (GD.)  amir}- tätä  Y.  70.  j;  —  'vatäsca**  nS  amintätä gsusca  talnS  .  .  Vr.  <?.  5 ;  —  sp?ntayäi ärwatse  °vatbya  arngntalbya  Y.  /.  2; I.  7.         a)  haurvatais  (näml.  ayari)  heisst
29646:•  j.,  g.  haurvSt-  f.:  s.  unter  haurvatät-.
```


## [2026-09-14T02:29:33.145Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN har\"; grep -n -i \"\\bhar\\b\" HRN.txt | head -15\necho \"=== HRN 1052 / خرداد\"; grep -n -i \"Hurdad\\|Hordad\\|Xurdad\\|haurvatat\" HRN.txt HUB.txt | head -20"
}
```


### [2026-09-14T02:29:33.217Z] TOOL RESULT

```
=== HRN har
648:äzartan etc.; ai. [/har- 'zürnen.
1074:bei. haris, har§, harsa *Elle, Länge des Vorderarmes*
1784:oss. haräg *Reiter (54) 2) ; si/n. worj, sar. wurj^ röSn.
3384:von ai. prati + [^har- denken (vergl. pratihdrana- und
4302:(2i)7); bei. n. ffar, /ar, LW. har^) (192); wa/. ;rwr,
5885:) vt. 19, 42 ]int die neuo AuRfj^abe harözuiiem.
6620:OeraT, miuj. sardi, sar haröi, si/n. arrai,
9430:XIII, 69) 'im Ganzen'; aw. haurva-; phlv. har, har[vJsp;
=== HRN 1052 / خرداد
```


## [2026-09-14T02:29:38.327Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9415,9440p' HRN.txt"
}
```


### [2026-09-14T02:29:38.383Z] TOOL RESULT

```
'zerstört, wüst ; Zerstörung, Wüste*, averem 'zerstören,
wüst machen' dazu, aber arm. e steht nur in per-
sischen Lehn Worten für e.
>) Jackson, Amer. Journal of Philology, Vol. XI, 87 folg.
«) Reimt auf sir 'Milch* (Öflhn. I, 240 Vers 1982).
16*244
H.
1088. hämün *Ebene'.
Vergl. ap. aw. hama- 'derselbe, der gleiche', ai.
samd' 'eben, planus, in gleicher Lage befindlich*.
1089. fiaven 'Mörser', (AM. 132 Zeile 6), kaukas.-bergjüd.
heveng, arab. LW. hävun,
aw. hävmia- 'Mörser ; phlv. havan^ arm. LW. havan.
^^90. her* jeder, all'.
ap. haruva- all*, fraharavam (Bartholomae, BB.
XIII, 69) 'im Ganzen'; aw. haurva-; phlv. har, har[vJsp;
ai. sdrva-.
1091. hurrä ^Geschrei' (äähn. I, 17 Vers 66).
mhd. hurra, vergl. hurr (Interjection) , engl. dän.
schwed. franz. hurrn (s. Grimm, Wörterbuch).
Sollten die germanischen Worte, etwa durch
türkische Verniittelung (wo ich ein hurrä aber nicht
nachweisen kann), aus dem Persischen entlehnt sein ?
\ }(^92. hergiz jemals, je*, mit Negation 'niemals'.
ap. Vmkaramöiy *ein Mal' (Darmesteter, Et. ir.
I, 245 ; unsicher) ; phlv. akarc bezw. hakaix, luxharj,
```


## [2026-09-14T02:29:39.570Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY هر\"; grep -n \"^هر\\|هر (\\|«هر»\" incoming/ARY/ARY_pages.txt | head -20\necho \"=== ARY خرداد\"; grep -n \"خرداد\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-14T02:29:39.650Z] TOOL RESULT

```
=== ARY هر
251:هر چا کشت ال
558:هریکك از واژه‌های زبانهای هند و اروپایی از واژه‌ی معینی در زبان هند و اروپایی ناشی شده‌اند.
1096:هرگز به افتخار جاودانی نخواهم رسید. (412418 ,9 ,111۸0 آشیل به جنگ پشت دروازه‌های
4052:۰ ا بهر (به چم "سهم" "قسمت"* و "حصه») .
4977:معنی واژه‌ی ۳08718 در زبان لاتین: یاهر (هریکك از دو تبر عمود چارچوب در).
10603:هر
15340:هر پرانگلیسی ([5لا8(/0): ۷۵۵ 204 ین
16177:هر ی بو
=== ARY خرداد
```


## [2026-09-14T02:29:47.322Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD جاثليق\"; grep -n \"جاثليق\\|جاثلیق\" TAD_pages.txt | head -10\necho \"=== TAD سفسط\"; grep -n \"سفسط\" TAD_pages.txt | head -10\necho \"=== TAD فلسف\"; grep -n \"فلسف\" TAD_pages.txt | head -10"
}
```


### [2026-09-14T02:29:47.405Z] TOOL RESULT

```
=== TAD جاثليق
=== TAD سفسط
=== TAD فلسف
```


## [2026-09-14T02:29:48.803Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF جاثلیق\"; grep -n \"جاثلیق\\|جاثليق\\|بطریق\" FSF_pages.txt | head -10\necho \"=== AFM جاثليق\"; grep -n \"جاثليق\\|فلسف\\|سفسط\" AFM_pages.txt | head -10"
}
```


### [2026-09-14T02:29:48.903Z] TOOL RESULT

```
=== FSF جاثلیق
5178:               ‫بطریق (به کسر اول و سکوندوم)‬              ‫بسیچیده (اسم مفعول از بسیچیدن)‬
5188:‫سکوبا و بطریق و هر مهتری‬
9168:‫‪«- ۲‬جامه مانند کوزه باشد که شراب در‬                         ‫جاثلیق (تازی‪ .‬معرب کاتولیک)‬
9171:‫جام کدوی شراب» (جهانگیری ‪-‬رشیدی ‪-‬‬                   ‫ز بطریق وز جائلیقان شسهر‬
15230:‫ص ‪ ۲۲‬چنین می‌نویسد‪« :‬آنچه معتقد‬                   ‫سکوبا و بطریق و هر مهتری‬
=== AFM جاثليق
```


## [2026-09-14T02:29:55.345Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=9175 && /\\[pdf page/ {p=$0} END{}' FSF_pages.txt >/dev/null\necho \"--- pdf page tag before 9168:\"; awk 'NR<=9168 && /pdf page/ {p=$0} NR==9168{print p}' FSF_pages.txt\nsed -n '9160,9180p' FSF_pages.txt\necho \"=== TAD sample\"; head -c 600 TAD_pages.txt; echo; wc -l TAD_pages.txt TAD.txt"
}
```


### [2026-09-14T02:29:56.564Z] TOOL RESULT

```
--- pdf page tag before 9168:

‫نیایش کنم خاک پای ورا‬                                                    ‫(ناصرء ‪:)۱۲‬‬
 ‫)‪(0-4۳-4۶‬‬                                       ‫ان‬
                                                  ‫وتزبه‬
                                                      ‫رکس‬
                                                        ‫چه نی‬       ‫اهست‬
                                                                       ‫نیده ک‬
                                                                            ‫ترش‬
                                                                              ‫خو‬
‫‪«- ۲‬جامه مانند کوزه باشد که شراب در‬                         ‫جاثلیق (تازی‪ .‬معرب کاتولیک)‬
‫وی کنند» (لخت فسر» صحاح) «صراحی‪.‬‬                            ‫پیشوای ترسایان‪ .‬مسیحیان‪:‬‬

‫جام کدوی شراب» (جهانگیری ‪-‬رشیدی ‪-‬‬                   ‫ز بطریق وز جائلیقان شسهر‬
                            ‫برهان)‪:‬‬         ‫هآرنکس کش از مردمی بودبهر‬
         ‫به مردان بخندد همی روز رزم‬        ‫)‪۵41-۴۵-۶‬‬
‫هم از جامة می به هنگام بزم‬                                                ‫جام‬
‫(‪)۶-۷۵-۹۷۷‬‬                                       ‫د‪:‬‬
                                                  ‫نخم‬
                                                    ‫ننز‬
                                                      ‫نوعی کوس کهبامهرهبزهآ‬
                      ‫‪-۳‬پارجهة نادو خته‪:‬‬               ‫چو بر پشت پیل آن شه نامور‬
               ‫به ایوان‌هاتخت زرین نهید‬     ‫زدی مهره در جام و بستی کمر‬
=== TAD sample
                                     ‫الف‬
           ‫ياكابىاللبناك‬  ‫‪َ8‬‬
                       ‫نببى‬




       ‫لحتل‬
    ‫‪ -‬اا لدم‬  ‫‪1‬‬             ‫تت‬             ‫‪7‬‬   ‫‪:‬‬
     ‫امون‬
‫ظ‬     ‫‪1‬‬



      ‫هني بنشره وتصحيحه وتعليق <واشيه‬
                            ‫ا‬


           ‫الو مان‬
              ‫دام‬    ‫ده ل‬




                    ‫« طبعة ثانية ‪6‬‬




                
  3117 TAD_pages.txt
  3312 TAD.txt
  6429 total
```


## [2026-09-14T02:30:03.149Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (22,23,24,25,26):\n    print('=== leaf',i); print(pages[i][:900])\nEOF"
}
```


### [2026-09-14T02:30:04.226Z] TOOL RESULT

```
leaves 87
=== leaf 22
                                     ‫« بيت ثور » في الارامية أي ببتالنار‬
                               ‫لوهبوزوبدرق‬
                                         ‫تتكارا»‬       ‫كابس‬
‫كدري « ‪ 4 5‬وهو حديد تمزو ج بالقصدير يدق صفائح وتكجي‬
                                                                   ‫صائفه‬
   ‫رق‬
    ‫لسطعند‬
         ‫انحا‬
            ‫وال ‪ -‬فارسي ه ‪:‬وبال ») ويهتومسااقط من الحديد وال‬
                                                     ‫مرادفه حتات وسحالة‬
                             ‫ونيا فارسي وهو حجر يكتحل بمسحوقه‬
‫‪ 0‬معدنية ‏ يقال لهفي الجرمأنية زرنك معان وهو معدن لذن بددّقصفاتم‬

     ‫ل‬                                          ‫عيراني « ‪0‬‬       ‫توراة‬

‫مونى اسة وهو مشتق من « ألراه © أي القى ووضح و « نوره ‪ 4‬في الفارسية‬

                                                            ‫ناهشراعة‬
                               ‫كح اران ( تنكننا ‪
=== leaf 23
                               ‫‪59‬‬   ‫‪9‬‬   ‫‪58‬‬




‫ج جن ‏ فارمبي «جان» وني اللاتينية نتسانددع براد به عند القدماء‬       ‫جان ‏‬
          ‫لارواح الساحة في المواء واجالنففايرسية معناه روح ونفس وحياة‬
                                ‫‪ .‬حدث ‪ -‬عبراني « جديش » معناه قبر‬
‫وق وم‪ُ2‬وزه » أي‬
              ‫فاس‬
                ‫ور‬‫عريواق فارسي ع ركب من ومر » أي‬
‫ا معناه‬    ‫خف وحذاء وففىي الافرنسية ‪6‬طعماوع كالوش مأخوذ م ‪.‬ناليوناني ‪52‬‬
                                         ‫رجل مخنشب مرادفه خف الخفة‬

                                               ‫جرم ‪ -‬فارسيرم أي حار‬
‫ببطالي ‪#1‬ههمماع معتاه لوميمرادفه جريدة وصحيفة الاخبار‬
                                                    ‫حر نال ا‬

                                             ‫ومحضر لا تكتبه العامة في الحوادث‬
      ‫جزدان ‪ -‬فارمي « جزدان » وهو القمطر ومحفظة الاوراق والعديبة‬
                        ‫عوية 
=== leaf 24
                             ‫اوج سد‬



                                  ‫جام‪ -‬فارسي « جام » وهو الكوب‬
             ‫وفي الفارسية ‪ 2‬جَنايان © وهو حب يشبه الماش‬   ‫جلبان‬
                    ‫وف الفارسية ا زنك » وهو جرس صغير‬        ‫‪5‬‬
                               ‫جلخ ‪ -‬فارسي « جاوخ » وهوالمسن‬
                                  ‫جلئار ‪ -‬فارسي معناه زهر الرمان‬
            ‫جلنجين ‪ -‬فارسي معناه ورد وعسل وهو معجون رخو يلعق‬
                 ‫ع ‪ -‬فارسي ‪ 8‬جلفوزه » وهو احلبصنوبر الكبار‬
  ‫انون تق الأؤاية ‪#‬حيقا © اولقفارسة «‪١‬ك‏اوتوف مكرامق‬
                                         ‫كو أي بقرة وميشي أي نعجة‬
‫ست ‪ -‬فارمي ك«ُدّست» وهو حجركريمذو ألوان يقال له فيالعربية‬
                                                     ‫الحجر المشوق‬
‫لول أما ‪#‬سادومع اللاتينية فهو اسمجنسلركلكحرجم وبراد‬         ‫مان‬
                                             ‫به أيضا بذور نفيس
=== leaf 25
                  ‫هفعناه عاموبراد به قائد اليش‬                ‫حترال | أنطالى ‪6‬‬

                            ‫جنس ‪ -‬ونانفىى ‪ 50768‬دفي اللذتينية ‪5‬تاناعع ععنى‬

 ‫حنفيص وخثيف وقنب ‪ -‬ابطالى ماأءموعودقه من اليونانى ‪5‬أطةمصطا‬

                           ‫وهو القنب نفسه ويطلق على نسيج منسوج مخيوط القنب‬
             ‫فارسي ‪ 2‬جنك ‪ 4‬معناهبرئن وهواله من ”لات الطرب‬                    ‫جنك ‪-‬‬


                   ‫‪0‬‬                             ‫‪4‬‬
                                                                                ‫ساماة‬
‫وكان المطل‬        ‫د عراي دين بن هنم ) معتاه وادي ان ‪0‬‬                           ‫عم‬


‫مسي لثلا بعر اسان‬                      ‫علا لسجى نَغت ‪ :‬ونجس التوفث ‪3‬ا‬


         ‫ابنهوابنتهلمولك ؟ ملوك م‪١٠ : 7‬‏ وهو موقم العقاب الابدي بعد الموت‬
     ‫‪2‬‬   ‫‪.‬‬    ‫‪1‬‬        ‫‪.‬‬      ‫‪٠‬‏‬        ‫‪-‬‬        ‫اك‬   ‫ف‬         ‫
=== leaf 26
                                          ‫د‬‫د‬


                                   ‫‪34 0 2‬‬


                              ‫حابالرىفا‪-‬رفسيية « |بره » وهوطائر‬
‫‪4‬اه وبيبضطلق عالىلرمسلسيح لامهم‬
                              ‫‏‪ ١‬حوارون ‪ -‬أرابي« حوارامعن‬
‫يل‬           ‫هدي الأساد وسبالةواووق تبت‬
                                      ‫سر كو كقاء م‬
‫من السحل أي الثوب الابيض الذي كان بليسه العسدون من سدث الور المكدس‬

                                  ‫ظ ‪ .‬الى الاحد الجديد أي الاحد الاول بعد الفصح‬
                              ‫‪1‬‬            ‫‪5‬‬       ‫‪1‬‬
‫حرش ‪ 22‬عبراني « حرش » أي غابة واجم والعامة تقول حرج لقرب‬
                                                                       ‫احرج‬
                                   ‫‪2‬ح ‪1‬‬

                                          ‫خادون ‏ نري معناه المرأةوالسيدة‬
‫خارصتيى ‪ -‬معئاه حجر صينى وهو ضرب عن العادن ‪ .‬غارا
```


## [2026-09-14T02:30:10.741Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,80p tools/ref_page.py"
}
```


### [2026-09-14T02:30:10.800Z] TOOL RESULT

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
    else:
        print(f"no scan of {abbr} covers printed page {page} (see 'scans' in refs_online.json)"); return 1
    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
    if not os.path.exists(pdf):
        print("PDF not found:", pdf); return 1
    lang = scan.get("lang", "fas")
    out_dir = os.path.join(OCR, abbr + vol)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"{page:04d}")
    png, txt = base + ".png", base + ".txt"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
    if not os.path.exists(txt):
        # try the PDF's own text layer first; fall back to tesseract
        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
        text = r.stdout if len(r.stdout.strip()) > 80 else ""
        if not text:
            env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
            text = r.stdout
```


## [2026-09-14T02:30:19.244Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in \"ثليق\" \"اثلي\" \"كاثول\" \"قاثول\" \"لسفة\" \"فلسف\" \"سفسط\" \"سوفسط\" \"فيلسو\"; do echo \"=== $p\"; grep -n \"$p\" TAD_pages.txt | head -5; done\nls incoming | head -40"
}
```


### [2026-09-14T02:30:20.425Z] TOOL RESULT

```
=== ثليق
=== اثلي
=== كاثول
=== قاثول
=== لسفة
=== فلسف
=== سفسط
=== سوفسط
=== فيلسو
2038:           ‫فاسفة ل ونانى ‪11‬معه‪ ]1‬معناه حب المكةومنه تقليف وفيلسوف‬
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
```


## [2026-09-14T02:30:26.289Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:2037])\nleaf=t[:off].count('\\f')\nprint('leaf of line2038 =',leaf)\npages=t.split('\\f')\nprint(pages[leaf][:1200])\nEOF"
}
```


### [2026-09-14T02:30:27.537Z] TOOL RESULT

```
leaf of line2038 = 56
                                  ‫متت‬    ‫اصع‬




           ‫فاسفة ل ونانى ‪11‬معه‪ ]1‬معناه حب المكةومنه تقليف وفيلسوف‬
       ‫‪8‬‬                                     ‫‪5‬‬                             ‫عام‬
 ‫فلفل‪ -‬لنظ هنديحيث منشأ هذا البات الذيحبه شديد الحراقة اوسفيفاة‬
‫آخر له قرونوف اليونانية ‪:‬مهم وهو فىجميم اللغاتبهذاالاسم‬               ‫‏‪ ْ٠‬تسمه وهونات‬
                                                                             ‫ما‬


 ‫فلين‪ -‬وناني ووااه؛ وهو شجر يثبه الاوط قشره ضخم سميك لين‬
                                                 ‫رخف يصنع منهالسداد والصمام‬


 ‫فليون ‪ -‬ايطالي وأهنوناوة! معناه ان صغير وبراد به عندنا الولد الذي محمله‬
                                                                 ‫االعلرامبعفمىودية‬
 ‫وف‬   ‫منار وبراد به المنارة والمشعل فوقبا وى النونانية ‪521‬‬   ‫تصحيف‬        ‫ذثار‬



  ‫الأطالقة م زفوهان انمد ف اهوخا اللمكورة اتاد وه‬
                                   ‫فى « فارس » وهي جزيرة بقرب الاسكندرية‬
              ‫فنجان ‪ -‬فارسي « فنجان وبتكان » وهو قدح صغير من خزف‬
 ‫فندق ‪ 5-3‬ونانيي متقطاء ‪0‬ل‪0‬هقم معناه يشبل اجميع وهو رك من ‪53‬م أي‬
                                     ‫‪0‬‬           ‫ع‬           ‫‪٠‬‬
```


## [2026-09-14T02:30:34.165Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search('سفس|سغس|ففس|سنس|سوفس|شفس', p):\n        print('LEAF',i)\n        for ln in p.split('\\n'):\n            if re.search('سفس|سغس|ففس|سنس|سوفس|شفس', ln): print('   ',ln.strip())\nEOF"
}
```


### [2026-09-14T02:30:35.285Z] TOOL RESULT

```
LEAF 9
    ‫ففسره « بيض المان أو ابن الجنينة ‪ 4‬أما أصل هذا النبات فههنودي فيكون‬
LEAF 30
    ‫رففس‬
LEAF 39
    ‫ناس وسممان نت أرامي ‪ 3‬سفسارا م©عتاه المساوم‬
```


## [2026-09-14T02:30:39.239Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (38,39,40): print('=== LEAF',i); print(t[i][:1400])\n\""
}
```


### [2026-09-14T02:30:40.314Z] TOOL RESULT

```
=== LEAF 38
                                 ‫ا‬
                                 ‫سه‬‫سا‬



‫سربأل وسروال وشروال ‪ -‬فارسي «سربال» معناه فوق القامة وهو لياس‬
                                                               ‫معروف |‬
‫سر جين وسرقين ل‪-‬انيني ‪5‬لن‪ 0©:5‬وني الايطالية معدهاه وهو الدمال‬
                           ‫والزبلى والفرث والسلح والنجو أي الخراء والدمن‬
‫سردين ‪ -‬سمك صغير ‏ نسبة الى سردينيا ( جزيرة في ايطاليا ) ‪«#‬افجهه‬
           ‫عاك نيك لزنت‬       ‫تصغير ‪ 110138‬لان ف سردينيا اعفرهوا نط‬

‫وهو الحربر والشقة‬         ‫شق من الخربر الابيض ‪ -‬وناني‬       ‫‪- 00‬‬

                                                   ‫منه ‪ .‬مأردقه سقة حربر‬

      ‫سرسام ‏ فارسي مر كبمن‪ 2‬سر » أي رأس و « سام» أي ورم‬
     ‫في‬
      ‫خزه»أ‬
          ‫سرموجة ‪ -‬فارسي مركب من « سر » أفيوق و‪١‬‏مو‬
                            ‫سرو ‪ -‬أرامي « شروينا » تعرأب شربين‬
                ‫مسطار ‪ -‬سلافة ‏ فياللانينية ناأونات معناه حمر حديث‬

           ‫الطرات لاتنى ‪53‬امنا‪ 615‬براد به السطل المعروف والسجل أيضًا‬

‫احتلزلات توناني ‪ 0002‬معتاه وفد وحملة وصف" وعدة وجمم وبراد به‬

      ‫ظ‬                                       ‫طائطة من السفن وحملة حربية‬
   ‫معتاه عنود وود لقف عبراتي معناه منصوب‬      ‫بوناني ‪5‬‬      ‫اسطوائة‬

 ‫سفتحة ‪ -‬فارسي وسنت معناه مثقوب وفي الجرمانية ‪ 102:‬معناه حوالة‬
                              ‫سقسطة ‪ -‬بوناني ‪ 329‬معنا » المغا لطة‬

          ‫)مو
=== LEAF 39
                   ‫ناس وسممان نت أرامي ‪ 3‬سفسارا م©عتاه المساوم‬

‫إسفين وسَفين ‪ -‬بوناني ‪ 0618‬معناه مضق ويطلق على سكة ضرب‬
                            ‫اللقود مرادفه قلق يفلق به الخشي والاحجار‬
 ‫مقالةوصقالة ‏عامية ‏ ايطالي «اهعه معناه سسُلَّمِ وبراد به عريش‬
                      ‫ابنائين الذي بقفونعليهحين يبنون ويطينون البيوت‬
   ‫كر فيجيماللذاتبهذا الانظا أصل هنديحيثمنثأقصبالكر‬
‫سكرة ‪ -‬عامي أرامي سوك ماع»ناه _مثلاق أعيما يغلق باهلباب ويقفل‬
                     ‫‪ 32‬عقت باررق سه ورافلسقحدنية‬
 ‫سكريستيا ‏ ايطالي هذاه‪:‬ده معناه مكان مقدس وبراد بغرهفة ملاصقة‬
                                ‫للكنيسة محنظ مهاالاواني والاثزاب المقدسة‬
 ‫كات و تت أي لنا فراعقاين كي انارت أي لمن‬
                                                    ‫أومن ‪80‬دماما نواه‬
 ‫ماحم فارسي « شلسم» وهواللفتاليوناني ومعناهقصاص الجاودوعربيه‬
                                                               ‫الخصّاف‬
     ‫سلاح دار ‪ #3 -‬من سلاحالعربى ودار الفارسي الذي معناه حامل‬
                   ‫ح اراب «ي شليع »ا أي رسولمدنمىسرسل‬
                                                    ‫سلي س‬

‫ولانيني ناتالز مرادفه لحري وهو‬        ‫خاو إشعارويت وناني ‪0‬‬
‫جنس سمك بحري وحهري بلغطول السمكة منهفي “برالدانوب الى ثثلاثةأمتار‬
 ‫ونزن ‪6٠‬؟‏ كلو ومنه نوعكارعناد أى ممنسسّه تخدر بده ومجازاً يطلق على‬
                                                   ‫ّنافة‬ ‫لةنترسىم‬
                                   
=== LEAF 40
                              ‫سس لهاسم سم‬




                            ‫سملت ‪ -‬أيطالي ‪ ©0106716‬وهو الشيد نفسه‬

‫من « اسمان »© أي مهاء و« ثرون » أي لون‬       ‫سمائجوفي ‪ -‬فارسي ‪9‬‬

                                                       ‫مرادفه لون سماوي‬
                                ‫فياليونانية ‪ 560065‬وهو الرماد‬    ‫سماد‬

‫متتدر نديول جد اوناني ‪ 011112‬دابة كالضبي لومبا أسود وأصفر‬

                           ‫تاعيلشمفايء وفي الارض ويقاللهاعروس الماء‬
‫سنبوق وسّنبوك ‪ -‬وفي التركية سبك وفي اليونائية ©‪6‬از‪00‬ه‪ 5‬وفي‬
‫اللاتينية طتصدة مأخوذ من « سنبك » الفارسي الذي معناه طرف الحافر وقد‬
                     ‫يطلق على سفينة صخيرة سميت به لصغرها مرادفه _سبارة‬
                           ‫سئحة ‏ فارسي « سنجه ‪ 4‬معناه عبار المعزان‬

‫منجاب ‪ -‬في الفارسية _سنجاب وفي اليونانية ‪507‬ناهأ!ة وتميه العامة‬
                                                                 ‫قرقدون‬
 ‫منجق ‪ -‬فالينارسية سنجاق وافليتركية سنجاق وفي اليوثانية ‪0016765‬‬
                                        ‫معثاه سمه رمأدفه أواء وعدم ورابة‬
            ‫سندان ‪ -‬في الفارسية ‪ 2‬سندان »© وفي الارامية ‪ 9‬سدانا »‬
‫وهو صمخ ير ينضح ووش أشهار‬              ‫مسندروس ‪ -‬ووناني ‪121‬‬
                       ‫افريقية ويطلق أيضا على رب من المعدن أحمر الاون‬
 ‫لنهما‬
     ‫ينعنلاتنعكا‬
               ‫ولانيني تسطن‪1‬لهاصذة وهو ال‬   ‫ابو ناني ‪0-2‬‬        ‫دل‬
```


## [2026-09-14T02:30:47.235Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport re\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (21,22,23):\n    print('=== LEAF',i)\n    print(t[i])\n\" | head -120"
}
```


### [2026-09-14T02:30:48.512Z] TOOL RESULT

```
=== LEAF 21
                                                            ‫غهرن‬
                                                               ‫صم إ‬
                                                                  ‫مشح‬

                                                            ‫‪0‬‬                             ‫‪8‬‬       ‫‪٠.‬‬       ‫‪0‬‬         ‫‪.‬‏‬
                                                 ‫عقار معطى ضد مهش السباع ‪:‬وهو دواء دم السموم‬


‫‪١‬‏‬             ‫تا ‪ - 00‬لنظهندي براد به لسيعج منحربر أو كان شفاف تزادقة اكيت‬

     ‫ْ‬                                         ‫تفتكه ‪ -‬ترك وهو البارودة والرصاص الذي برى به‬
‫اتق مساه الكتابة عن بعدوهو مركت ‪9‬مفن‪1‬فااغاية ونهاية ‪١‬‏‬
                                                     ‫نن‬‫وف”؟‬
                                                          ‫نغرا‬
                                                             ‫تل‬
                                                                                      ‫وحد و ‪:010‬ع كدب‬

‫"لفون س بوناني معناه الخاطبة عن بعد وهو مركب من ‪506‬ة غاية وتهاية |‬
     ‫ْ‬                                                                            ‫وحد و‪ 8201‬أي صوت‬

‫ثق عن ( ليد » أي عامومنهالتلنود ‪١‬‏‬
                                 ‫اميف ‪ -‬عبرانيمعناهستعيلموهوممشت‬
                                                                         ‫أي كثاب سن المهود وتعليمهم‬

                                                                ‫‪ 5‬ل الف ‪--‬مترك عاميمعناه كسل ‪.‬ان‬
                                      ‫‪:‬‬      ‫‪0‬‬   ‫‪٠.‬‬            ‫‪4‬‬     ‫‪.‬‬                             ‫‪)2‬‏‬
                                   ‫ترك « تنجره » معناهقلارمنبحاس وغيره‬                        ‫س‬      ‫طنحرة‬
                                                                            ‫‪2‬‬                                  ‫سَّ‬
               ‫من‬    ‫منحوتث‬       ‫وهو‬    ‫المور‪ -‬في العيرانية ‪ 8‬ثور »‪ 6‬في الارامية « تنورا »‬




           ‫(‪ 16‬ذكر الفيروزبادي انها فارسية واهل مصر يتولون بفته' وهى عندهم نسيج‬
         ‫من القطن ابيش والصواب الهْت وهو نسيج رفع من القطن ابيش معرب يافته ‪:‬‬
             ‫بالفارسيه واما ماميه السوريين بالتفته' وهى عندهم نسي من الحرربنفأخوذ‪.‬نميو‪٠‬ال‏له اعل‬
               ‫ارقي‬      ‫ملك‬                ‫ل‬              ‫ع‬        ‫ا‬       ‫جر‬                ‫ل‬


                                                                                 ‫عه‬
                      ‫(؟) ويقارما من العرنى ‪ 0-1‬بالطاء من شل الرجل طنبلة ‪ 79‬بعد تعاقل‬
          ‫وهو القدر من الحجارة والتحاس ‪.٠‬‏وقي لكل قدر يطبخ فيها وهو ‪:‬‬                 ‫(‪ )1‬وعربها ‪1‬ول‬

          ‫‪١‬‏‬                                                                ‫مذاكر وهليه قول الى اأطيب التنى‬

          ‫‪0‬‬             ‫اقيق‬      ‫ومرحلنا‬   ‫رعيتها إللا‬   ‫ابت‬             ‫‪0‬‬           ‫وخيليى اذا مرت‬

         ‫ققدتنصئا ذلك الوحش | الذي مركت ‪5‬‬
                                        ‫اى ان هذه اخيل لاترعى الروضةاةلتي مر يبا الا ونحن ‪5‬ا‬
                    ‫التحاس‬   ‫من‬   ‫صشير‬   ‫دست‬   ‫رهو‬   ‫المرجل معناء العر‬   ‫وخارب‬   ‫‪1‬‬      ‫‪2 5‬‬       ‫له وأخذنا فى صضخه‬

=== LEAF 22
                                     ‫« بيت ثور » في الارامية أي ببتالنار‬
                               ‫لوهبوزوبدرق‬
                                         ‫تتكارا»‬       ‫كابس‬
‫كدري « ‪ 4 5‬وهو حديد تمزو ج بالقصدير يدق صفائح وتكجي‬
                                                                   ‫صائفه‬
   ‫رق‬
    ‫لسطعند‬
         ‫انحا‬
            ‫وال ‪ -‬فارسي ه ‪:‬وبال ») ويهتومسااقط من الحديد وال‬
                                                     ‫مرادفه حتات وسحالة‬
                             ‫ونيا فارسي وهو حجر يكتحل بمسحوقه‬
‫‪ 0‬معدنية ‏ يقال لهفي الجرمأنية زرنك معان وهو معدن لذن بددّقصفاتم‬

     ‫ل‬                                          ‫عيراني « ‪0‬‬       ‫توراة‬

‫مونى اسة وهو مشتق من « ألراه © أي القى ووضح و « نوره ‪ 4‬في الفارسية‬

                                                            ‫ناهشراعة‬
                               ‫كح اران ( تنكننا ‪#‬هعناه رياط وشل"‬
‫تبارو ‪ -‬ايطالي ‪:‬دعا من اليونائي دمء‪ 2681:‬معناه مشهد ومنظر مرادفه‬
                      ‫حضر وملهى وملعب ‪ .‬ومكان الممثلينفييقاهل ‪ 4‬شل‬
                                                 ‫‪ -‬انظر دغار‬
                            ‫تفوس ‪ -‬نونابي ‪ 5000‬براد به الى الحرقة‬


                                ‫‪02‬‬   ‫‪2‬‬
‫جائليق ‪ -‬بوناني ‪5‬معةادطفهة معناه عام وجامع ويراد به فيالكنيسة مُتقدام‬
                                                                 ‫الاساقفة‬
             ‫‪ -‬فارسي « جاده » معناه العار‪ 3‬المتاننة ‪ 07‬متو حة‬    ‫خادة‬
                ‫و_‪-‬‬   ‫‪83‬‬

=== LEAF 23
                               ‫‪59‬‬   ‫‪9‬‬   ‫‪58‬‬




‫ج جن ‏ فارمبي «جان» وني اللاتينية نتسانددع براد به عند القدماء‬       ‫جان ‏‬
          ‫لارواح الساحة في المواء واجالنففايرسية معناه روح ونفس وحياة‬
                                ‫‪ .‬حدث ‪ -‬عبراني « جديش » معناه قبر‬
‫وق وم‪ُ2‬وزه » أي‬
              ‫فاس‬
                ‫ور‬‫عريواق فارسي ع ركب من ومر » أي‬
‫ا معناه‬    ‫خف وحذاء وففىي الافرنسية ‪6‬طعماوع كالوش مأخوذ م ‪.‬ناليوناني ‪52‬‬
                                         ‫رجل مخنشب مرادفه خف الخفة‬

                                               ‫جرم ‪ -‬فارسيرم أي حار‬
‫ببطالي ‪#1‬ههمماع معتاه لوميمرادفه جريدة وصحيفة الاخبار‬
                                                    ‫حر نال ا‬

                                             ‫ومحضر لا تكتبه العامة في الحوادث‬
      ‫جزدان ‪ -‬فارمي « جزدان » وهو القمطر ومحفظة الاوراق والعديبة‬
                        ‫عوية ات رك دوين »روسن طريل اناق‬
‫جص ‪( -‬وجَّدص وجفسين وجس وجسين ب)وناني ‪50587‬م وفي اللائينية‬
                          ‫نامرع وهو سلنات الكلس الممتزج بالماء يطلى به‬
‫جغرافية ‪ -‬وناني مركب من‪ 3‬أي أرض و ‪0518‬م أي كتدب ووصف‬
                                                  ‫مرادفه مخطيط الارض ووصتها‬

                     ‫جذت ‪ -‬نري « جُفت »‪6‬معناه زوج خلاف الفرد‬

‫حمل ‏‪ ٠‬فارمي « شتال » وهو نوع من الذئاب صغير الثة وفي اللاتينية‬
                      ‫فنالا نانع أيكلت ذهبي ويرجمته بعضهم بانآوى‬

‫جلاب وجُلاب ‪ -‬فارسي معناء ماء الورد ويزاد به سكر أوعل عفد‬
                                ‫عاء ورد وعطر ونقلا عن الايطالية ءطةءاتبسع‬
```


## [2026-09-14T02:30:59.559Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in (188,189,190):\n    print('=== leaf',i,'(printed ~',i+540,')')\n    print(t[i][:1600])\nEOF"
}
```


### [2026-09-14T02:31:00.855Z] TOOL RESULT

```
leaves 684
=== leaf 188 (printed ~ 728 )
 ‫یر ار —‬                                                                                                     ‫خردر‬

‫وفارسی ‪ ۵‬میباشد ‪ -‬بوستانی سرخ رنگه و فربه‬                        ‫آقتاب است دربرج جوزا ‪ -‬ونام روز شم باشد‬
‫بود وچون بکوبند زرد شود ‪.‬گرم وخشك است‬                            ‫ازهرماه (‪ )۱‬شمسی» وقارسیان درین روزعید(‪)۷‬‬
‫در چهارم کوبند اکر بر عصار انگور بریزند‬                          ‫کتند بتا برقاعد؛ کلیکه(‪ )۳‬مان ابشان مقرر‬
‫سالت خود نگاه دارد ونگذارد که بجوش | دف ‪۰‬‬                        ‫است که چون نام ماه و نام )‪(٤‬‏ روز موافق باشد‬
‫و گر ور آ نی ریزند از شور آن گزندکان‬
                                                                ‫جشن وعید نمایند واين جشن راجثن خرداد کان‬
‫بگریزند ؛ وصحرایی که آنرا بری نز گونداز‬                          ‫خوانند ‪ ۰‬نك است دراین روز طلب حاحات از‬

             ‫فم بوستالی‌است لیکن طبیعت ‏ از‬                      ‫ملاثکه و فرختها کردن وزن خواستن ‪ 7‬و نام‬
                                                                 ‫بر آهای روان‬        ‫فرشته است که مو کل است‪.‬‬
                   ‫ری‬
                    ‫بوستانی‌ندارد کویاهآ نرابتک‬
                                                                 ‫درختان ‪ .‬و امور و مصالحی که در ماه خرداد‬
                       ‫قگچویبند و باماست خورند‬
                   ‫تخم سیندانت که‬                 ‫و فارسی‬
                                                                 ‫واقع شود بده تعلق دارد ‪ -‬و نتامشآکده‌ای بود‬
                                                                                       ‫سار برزکه وعالی ‪١‬‏ ‪.‬‬
              
=== leaf 189 (printed ~ 729 )
 ‫خرده مرده‬                                                                                    ‫‪۷۳۱‬‬
‫عقل و داناو آنکه بهمه چیز برسد اکزلیات‬                 ‫های‬    ‫لفت از اتباع است بمعنی ته باط وچز‬
‫وزئات ‪ -‬و باريك بین ‪ -‬وعیب جوبرا فيز‬
                                   ‫ج‬                   ‫سهل وریزورباشد ودرموبدالقضلا خرد(‪ )۱‬ومورد‬
                               ‫کت ‪:‬‬                    ‫با واو معدوله درئالی بمعنی‌ریزه رزه و ترجمۀ‬
 ‫خر ده کافو ر = کنابه از کواک‬                                                      ‫منکر(‪ )۲‬لوشته‌اند ‪.‬‬
                              ‫وستار گان اشد ‪.‬‬          ‫خر دومند اه بکراول وضم ثالك ‪.‬‬
‫خردهگاه" « با کاف فارسی بالف‬                           ‫ممعذی خردمند است که زبرك و عاقل و صاحب‬
‫کشیده وبها زده » ند گاه سر دست ویای اسب‬                                                        ‫عقل باشد ‪.‬‬
‫واستر وخر وامثال آن باشدکه چدار وبشاوبرآن‬              ‫یشم اول و فتح ثالث ‪٠‬‏ ربزء‬           ‫حرده‬
‫نهند ورسمان برآن بندند ‪ -‬وجاییرا نیز گونند‬             ‫هرچیز رکاویند ‪ - ۴‬وخس وخاشاك وامثالآنرا‬
‫ازسینۀ شتر که دروقت خوابیدن برزمن‌نهد وآن‬              ‫نکیفزته‌اند‪ -‬وشرارء‌اتش راهم گونند ‪ -‬ویمعنی‬
‫مانند کف پای او شده باشد " و باینمعنی‬                  ‫فوس قزح هم بنظرآمده است‪ -‬ونکته گرفتنی‬
‫بحذف های اول هکفمته‌اندکه خردگاه باشد ‪-‬‬
                                                       ‫(‪ )۳‬را نکیوزبند که بکرفتگوی مردم گیرند‬
‫ماةهٌ کوچکی رائیز کوبند که دردرون‬
                                ‫یگ‬  ‫وخ‬
                                  ‫خرد‬                  ‫ازدقیق وباريك هم هست چه‬            
=== leaf 190 (printed ~ 730 )
 ‫‪A‬‬                                                                                  ‫خرد* مینا‬
‫خر د هره ع بفتح‌اول وئالث ؛ معروف‬                ‫خر دة همینا = ممروف است کهمینای‬

‫است کهزهرءٌخر‪-‬وزهرة بزر که‌باشد ‪۴‬سودرختی‬          ‫شکته وریزه رزه شده ‪ - ۱‬کونابه از شراب‬
‫امت که برک آن ببرگاید شبه‌استت لسکن‌از‬                                           ‫لملی هم هت ‪.‬‬
‫برگك ید سطبر تر و گنده تر بود و گل سرخ‬            ‫ونی و سکون زای‬
                                                               ‫خرر = بفتح اول ا‬
‫وسفید کند ‪٩‬‏ » وبت‌پرستان بر گآ نرا بکاربر ند‬     ‫‪ ۴‬از‬       ‫ناد‬
                                                               ‫ور‬‫گوشی‬
                                                                    ‫تقطه دار ‪ ,‬اسباب خرده فر‬
‫وحیوانات اگر بکرت آنرا بخورند هلاك شوند‬            ‫مهره و آینه و شانه و امثال آن چه خرزی‬
‫آونرا بعریی سم الحمار خوانند » و معرب آن‬          ‫خرده فروش‌باشد ‪ -‬ونام شهری و مدینه‌ای هم‬
‫خررهرج باشد ‪ -‬وحنظل را تنہیز گفته‌اند ‪ -‬ونام‬                                          ‫؟ ‪.‬‬     ‫هت‬
‫سیاه وصرح و زهردار ‪ .‬و در‬      ‫کرمی هم هت‬         ‫ورن‬    ‫بفتح اول و تانی ‪۳‬‬   ‫‪-‬‬   ‫خرزدان‬

 ‫ان‬     ‫مژیدالفضلا یمعنی سک انگور هم ا‬
                                                  ‫تمکدان » نام مبارزی بوده‪ 3۳۳‬وبکسرثانی‌هم‬
‫حردی = بفتح اول وئانی کوسر ثالث‬                                                        ‫کگفته‌اند ‪.‬‬
   ‫وسکون تحتانی خ»رده فروش راگونند ‪٩‬‏ ‪.‬‬            ‫خر ره د بر وزن هرزه » آلت تتاسل‬
‫خر ر ین = بروزن پروین ‪ ۰‬چوبی باشد‬                  ‫باشد‪¥ .‬‬   ‫وناتراشده
```


## [2026-09-14T02:31:10.766Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t[180:200],180):\n    if 'خرداد' in p:\n        print('LEAF',i)\n        for ln in p.split('\\n'):\n            if 'خرداد' in ln or re.search(r'[A-Za-z]{4,}', ln): print('   ',ln.strip()[:220])\nEOF"
}
```


### [2026-09-14T02:31:11.836Z] TOOL RESULT

```
LEAF 187
    ‫خرداد‬                                                                                        ‫‪-‬‬
    ‫خرداد ‪ °‬د م اول بروزن مرداد ؛‬                        ‫ثانی وسکون‬   ‫شتح اول و" شف ف‬   ‫=‬       ‫حرد‬
    ‫‏‪ («٥‬گو بد ‪« :‬معنى هذا الاسم (خرداد) ثدات الخلق» وی نام ابزدی از ایزدان دین‌زرشتی‌است‪.‬‬
    ‫نگهبانی سومین ماه سال وششمین روز ماه (شمسی) با اوست ‪ .‬در اوستاو کتب دینی پهلوی خرداد‬
    ‫وامرداد غالبا باهمباد شده‌اند ‪.‬خرداد مظهر کمال اهورمزدا درین جهان و درجهان مینوی‌بخشایش‬
    ‫ابزدی جزای اعمال لیکوکاران است ‪ .‬در عالم مادی‌نگهبانی آب با خردادست‪ .‬بیرونی(آ ارالباقه‬
    ‫كويد ‪« :‬هروذا (خرداد) هوالملك المو کل بتربية الخلق والاشجاروالنبات و ازالقالتجانات‬               ‫‪۰‬‬
LEAF 188
    ‫جشن وعید نمایند واين جشن راجثن خرداد کان‬
    ‫درختان ‪ .‬و امور و مصالحی که در ماه خرداد‬
    ‫(فر) «لك ‪۲‬‬        ‫‪edratuoM‬‏‬           ‫‪۳۳€‬‬    ‫هشتر نکارمر ود ‪.‬گل گلاب ‪(°‬‬
    ‫‪ = ۴‬خردل بری = ‪edratuoM 6823۷125‬‏ (فر)«لك؟ص ‪. ۰ ۹۱‬‬                                                 ‫ص‪.* ۷۱‬‬
    ‫‪ :‬خر دوهند‬      ‫وك‬    ‫>‬               ‫‏‪ dJ» Thlaspi — ۵‬ص ‪۰ ۱‬‬
    ‫‪ .‬دز روز خرداد ازماه خردادجشن‌خر داد گان‬                    ‫عی‌المیاه *‪ .‬متشت چپارم در اوستا بخرداد تعلق دارد‬
    ‫برها متفه ‪ .‬بیرونی در فهرست روزهای ابرانی (در آثارالبافه) روز ششم را «خرداد؟ و در سفدی‬
    ‫‪ ۰‬فخرده آوستا ‪ « ۵۸۲‬فهرس تت هزدسنا » در طبری ماه خرداد را هرماه ‪Hara mãh‬‬         ‫‪۹‬‬
    ‫‪.*۱‬‬    ‫«وس‌ورامن ص‪۲۹۲‬؛‪,‬‬             ‫جهان ازخرمی چون کرم بغداد‪.‬‬                      ‫مه آردیبپشت و روز خرداد‬
```


## [2026-09-14T02:31:17.777Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[187][:3000])\n\""
}
```


### [2026-09-14T02:31:18.896Z] TOOL RESULT

```
 ‫خرداد‬                                                                                        ‫‪-‬‬
                                                                                              ‫‪۲۷‬‬‫‪-‬‬

‫ازختاو ختن کهمشك خوب در آنجا میشود ‪ | -‬و بی‌تشدید ثانی همدرست امت ‪ -‬و بکسر اول‬
‫وفتح ثانی‌بمعنی عفل باشد؟ ‪ -‬وم اول وسکون‬            ‫و نوعی از جامةً آبریشمی هم از آنجا آورند ؛‬
‫»بمعنی کوچك باشد که در مقابل‬        ‫لث‬
                                     ‫ثیاو‬
                                        ‫ان‬          ‫و بجای زای هوز رای قرشت همگفته اندکه بر‬
                               ‫بزر کب امت ‪. ۴‬‬                               ‫وزن شبگیر باشد ‪. ۱‬‬
‫خرداد ‪ °‬د م اول بروزن مرداد ؛‬                        ‫ثانی وسکون‬   ‫شتح اول و" شف ف‬   ‫=‬       ‫حرد‬

                                                    ‫دال ابجد » بمعنی گل تیرۂ چبنده باشد ‪ ۴‬؛‬

 ‫‪« - ۱‬سخن اندر ناحیت خرخیز » مشرق وی ناحیت چین است و دربای اقیالوی هشرقی‬
‫تغزغزست و بعضی از خلخ و مغرب وی از حدود کیماك است و ( در ) امن‬                      ‫وید‬
                                                                                      ‫د و‬
                                                                                        ‫حنوب‬
                                                                                           ‫وج‬
  ‫ناحیت مغك بیار افتد وموبهای بیار وچوب خدنکه‌وچوب خنج و دسته‌کارد ختو خیزد و ملك‬
  ‫ابشانر! خرخیز خاقان خوانتد ‪ « »...‬حدودالمالم‪ 7210161710 = > ۰۵‬د مینورسکی‪ .‬حدود ‪۲۸۲‬‬
                                       ‫‪ «۴‬خرد » گل بود ‪ ۰‬خسروانی گفت ‪:‬‬                       ‫ببعد * ‪.‬‬
         ‫بخرد ‪.‬‬   ‫بردت‬    ‫باز ناکه فرو‬                    ‫آن کجا سرت بر کشید بچرخ‬
    ‫‪ 2‬لغت فری ‪۹‬‬
 ‫رکه ‪« ۵۳۱‬اسفا! ‪۲ :‬‬
                  ‫« ی‬                ‫« بارتولمه ‪۵‬‬    ‫پپلوی )‪ . 8۲5‬اوستا ‪18361 -‬‬         ‫‪۴‬‬
 ‫‪» < ۱ :‬یلزید ‪211‬‬        ‫( عزم » تصمیم » قود مدر که ) « وبلیامز ‪4۴‬‬    ‫مانىكرىت ‪1‬ا‪4۲‬‬           ‫‪۳۸‬‬    ‫ص‬
 ‫‪ - ۴‬پپلوی ‪« 4۲۵۷5‬ناوادیا ‪[ ۷۹۱‬رك ‪. :‬خرده] اورامانی ‪. 4 < 4۲۷7۷‬‬        ‫« مینا‪.»4۳۱‬‬
 ‫اورامان ‪ ۰ ۷۲۱۲‬شهمیرزادی ‪ ۲ . 4« 0۳111‬ص‪.»۷۷۱‬طبری ‪« 011161‬صاب‌طبری ‪ ۵۲۳۰‬کیلکی‬
 ‫هم ‪ ۰ 0711‬معرب آن خردة «نفس» هرن خرد فارسی را از اوستایی ‪) 2/۵72۷‬ندانته«اسفا‪۲: ۱‬‬
                                                                                        ‫‪:‬‬    ‫ص ‪۸۹۲۹‬‬

         ‫خردش چنان بکوفت که خاکش‌غبار کرد‪.‬‬            ‫چند استخوان که هاون دوران روز کار‬
  ‫سعدی‌شیواژی‪.‬‬
  ‫اوستا )‪ 20۵۷۳۱2۱۲‬مر کب از دو جزو ‪ :‬هئوروه صفت است‬               ‫‪,‬‬    ‫‏* بهلوی ‪1‬‬
  ‫بمعنی رسا * همه » درست؛ کامل؛ دریارسی باستان ‪2۷11۲811‬درف‌ارسی هر » جزو دوم اها سود‬
  ‫دال براسم مجرد موث ؛بنایرین هئوروتات بمعنی کمال‌ورسابی است ‪.‬ابورسمان دارلآباارقیه (س‬
  ‫‏‪ («٥‬گو بد ‪« :‬معنى هذا الاسم (خرداد) ثدات الخلق» وی نام ابزدی از ایزدان دین‌زرشتی‌است‪.‬‬
  ‫نگهبانی سومین ماه سال وششمین روز ماه (شمسی) با اوست ‪ .‬در اوستاو کتب دینی پهلوی خرداد‬
  ‫وامرداد غالبا باهمباد شده‌اند
```


## [2026-09-14T02:31:28.473Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('pages',len(t))\nfor i,p in enumerate(t):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in (400,401,402):\n        print('=== idx',i,m.group(0),'printed ~',int(m.group(1))+1917)\n        print(p[:1800])\nEOF"
}
```


### [2026-09-14T02:31:29.842Z] TOOL RESULT

```
pages 553
=== idx 399 [pdf page 400] printed ~ 2317
[pdf page 400]
بیان پنجم
در های هوز با دال ابجد مشتمل بر هشت لغت وکنایت

هدبه ‎٩‏ » بنتم اول وبای ابجدوسکون ده * « بنم اول و فتح ثالی » بممنی
ثانی » جانوری است پر دست و پا و آنراهوام | حق و راست و درست باشد چنانکه بیهوده تالحق
خرخدا (۱) میگوبند . خوردن‌آن باشراب‌پرقان | و باطل وهرزء راکوبند - و بمعای فا همهم پنظن
را نافم است . آمده است که.نفض نقصاست .

هدمان ۴ » بنتح اول وسکون ثانی دی - بنتح ارل وسکون‌نانی وتحتانی,

: ال بمعنی دیمه باغد و آن زراعتی است که از آب
ومیم بالف کشیده و بنئون زده » بمعنی ابثاراست 9
وآن‌از نود با زگرفتن وبدیگری صرف کر ون() | باران حاصل میشود - ودرعربی چاروابیرا کوبند
باقن َ 7 که بجهت قریانی يمکهٌ معظمه فرستند اعم از
و شتر وکوسفند ‎٩‏ .

هدنج * - بنتح اول و ثانی و سکون هدنه ی 2

8 ات خنگه راکوشد بسن اس که بر وزن مدینه » بممنی زشه

بون وجیم» اسب راکوبند یمنی اسپی پایه باشد که نردبان است ۷ .
موی او سفید باشد. هدية دندان - کنابه از زری است

هدنگ ۴ « بر وزن خدنکه » بمعتی | که بمدازآنکه جممی ازاقرا و ماکین‌راشیافت
هدنج اس ت که اسب خنگه باشد. کرده باشند پرسم هدیه پایغان دهند ۸ +

(۱) خم۱ : خرخدای . (۷) خم ‎٩‏ : نمودن .

- «هدبه (بفتح اول ودوم وسوم)هی‌الدودالنی تکون تحت‌الجرار وتجمع نفهاوتمتدربره
واسمه بالعريية حمار قبان» «عقار ۰۱۷۰ ۳ 610200746 (فش) (8561109 8ع0819) . معنی‌بام
او جریی « خری که مانند کلوله میغلطد > است و ترجهداست از بند ]1 ۰ ۳۵ از دسقوریدی
(بمعنی : خرانی که در زیر خمره‌های آب‌اند) «عقار ۹۲۰ف» .

۴ -ظ . برساختهٌ فرقةٌ آذ رکیوان . ۴ <* هدنکه (ه.م.) ور4: جهانگیری.

۴ < هد (هم.) * فوده (هم.) زقس : بیهوده » پیهفه . هل احق
باشد. . رود کی (سمرقندی) کوید :

مهر جوبی (خواهی) ز من وبیمهری هده خواعی ز من و ببهده‌ای .»
«لفت فری ی ۹4۳4۸

فرهنگه نظام همین بیت را به قطران (تیریزی) سبت داده و برای معثی دوم ( فاینده)
خاهد آورده امت . در دیوان قطران باهتمام محند نخجوانی نبریز ۱۳۳۳ این بیت را لیافتم -

۹ - باین معتی هدی بفتح اول و کسردوم وتقدید سوم است . ر
=== idx 400 [pdf page 401] printed ~ 2318
[pdf page 401]
بیان ششم
در های هوز با رای بی نقطه مشتمل بر شصت و هفت لغت و کنایت
مر « بفتح اول وسکون انی؛کلمه‌است. | کلمه‌ایست که شبانان کوسفند رابسوی خودخوانند
که افاده ممنی عموم دهد هسچو هرجا وهرکس | - و درعربی نام زنی بوده است - وکربه را نیز
و مانند آن ۱ - و دانه‌ای هم هت که در مبان | کویند که دشمن موش است ‎٩‏ .
کندم میروید و خوردن آن ضرر دارد و آنرا هرا » بفتح اولوئانی‌مشددبالف کشیده.
بنابرین ازکندم جدا کنند ۴ - و پلفت پیلوی حلیله را کونند وآن دوائی است ممروف‌وبهترین
بستی کنند ۴ باشد که فاعل است - و ترچمةٌ آن کابلی باشد - و کلولهای طلا ونقره را ابیز
کل هت ۴ - ودرعربی‌معنی ناخوت ومکروه کویندکه در زین و پراق اسب بکاربرند اعم از
شمردن وخوب نداستن باشد - وبضم‌اول» بمهنی [ لجام وسیته بند و غیره ۷ - وجم‌اول بمعنی‌ترس
آزجای درآمدن وترسیدن بپاشد9 - وبکر اول» | و بیم باشد ۸ - و درخشیدن راالیز کوبند -
۹ - پارسی باستان - 387۵0۷8 (سمه) . 5۳8138۳8۷812 (چماً . مجموعاً) » اوستا
-2۲۷8 ۰ پهلوی 397 ۰ ۷19 ] 14۲ » هندی باستان - 54۳۷8 « اسشق ۱۹۹۹ > ور :
منای ‎۲۷٩‏ : ۲ . در اوستا 1321۲۷2 صفت است بمعنی رسا . همه . درست (تمام:,کامل) . در
پارسی باستان 138۳۷8. همان است که درفارسی«هر» شده مانند: هرچیز.ه ر کر . برسنگه ليشتةٌ
بهستان (کتیبهٌ بیستون) 138۳8۷8/0 - 118 از همین ريشه آمده است بمعنی روبهم » فراهم.در
گزارش پهلوی اوستا ( < زند ) هرجا که 1121۲۷8 آمده . در پپلوی به «هما4» ( < همه )
کردانیده شده است «قاب ص۵۷ و رك : خرداد (جزو اول) ؛ کردی 16۲ (هر , همه) , زازا
0 665- 36۲8 (هر کس) «ژابا س44۱)؛ گیلکی 128۳ . ۴ - جهانگیری‌یز
چنین‌آورده . رشیدی نوبسد: «لیکن درلسخةٌ سروری گفته که جنم هاء‌است.» قول سروری‌آینست:
هر, دانه‌ای باشد که درمیان کندم روید وخوردن آن مطربود » وبخاطرمیرس د که باین هعنی پم
هاه باشد.» -ظ . «کنند» مدحف «کنه» است , چه ورد هزوارش 387
که آبرا 6۵02 , 6202 81۵01 خراده‌اند «یونکرس۱۱*۰(عمن‌کلمه است که محققان‌پپلوی
دان ۴۲۶ , 117 > 50118 خوانند «بیب ر که۹۱۰۳ ۰ قی :کل [عر]) ظ. دریکی از مآ
=== idx 401 [pdf page 402] printed ~ 2319
[pdf page 402]
۳۱۹۳ حرش
وبمعنی آوازمهیب باشد مانندآوازسباع ووخوش۹؛ هراسندگان ۷ - تالبان ر سالحان
و پاین معنی بفتح اول هم درست است - وبکسر | وعتقیان و ترسندکان وپشیمان شدکان باشد.
اول » بمعنی فرو ریختن وآواز وصدای‌فروریختن هراسه ۸ < بکر اول و فتح سین می
باشد ۴ - وبحذف تشدیدءنام شهربست درخرآسان | نقطه .آنچه مردم را بدان ترسانند - و چوییر|
مقهور بهرات ۴ . نیز کویند که درمیان زراعت بریای کنندوصورتها

هرات » بروزن سفات , بخت نيك را و چیزها بر آن اصب سمازند با جانوران ژبانکار
کوبند پمنی‌نيك بخت- ونام‌شهربست درملك(٩)‏ | بجانب زراعت تیایند وآرا بمریی مخغدا ر کویند.
خراسان ۴ . وبفتح اول هم درست است .

هراس « بفتح ول وسکون‌سین بی ناطه. هراسیدن* « بمعنی ترسیدن وواهیه
نام درختی است خاردار - وبکی اول بمعنی‌ترس | کردن باشد ‏
و بیم باشد ‎٩‏ - و اهر بترسیدن و بیم بردن هم هراش - بفتح اول وسکون آخ رکه
هت بمثی بترس٩‏ ؛ و بان معنی بفتح اول هم | .شین نقطه داراست؛ بممنی قی واستفراغوشکوقه
آمده است . باشد*۱- وبتازی برهم انداختن سکها باشد از

(۱) خم۱ : - ملك .

۹ - اسم صوت . قی : افقانی 8۵۳8-80۳8 (صد! وغوغا) « خوبشمان۱*۹۱* و رك :
اسشق - هوبشمان ۱*۹۱ . قی : هربن (آوازهپیب) ؛ ترکی «هرای» (#ر‌باد » كومك خواستن,
اطلاع دادن بشخصی چیزی را) « جفتایی‌س ۴۵۱۵ :

ز هرین حمله ز هرای تیخ شده آب خون در دل تند میخ.

نظامی کنجوی « کنجینهٌ کنجوی ۰4۱۹

درل :جح ۰۱ ۴ < هرات (ه.م.) ۳ فریو (هم.) # اهری :

بهرای کنجش چو پدرام کرد به پهلو زباش «هری» نام کرد .

ظامی کنجوی «رشیدی» .

۴ < هرا (ه.م.)* هری (م.م.) * هریو (ه.م.) .در اوستا ۰۳12۳26۷2 پلرسمی
باستان 712۳81۷8 *اغپیگل ۵ ۲4 » پپلوی 118۳810 » 113۳8۷ « مار کوارت . شهرستانهای
ابران س۱۱* . [16] 111۳24 (هراتی) «اونوالا<۹؟) ؛ نام شهری بخراسان قدیم » که اکتون
درشمال غربی افغانتان ودر کنار هری رود راقع است . .8 - «هرای: تری بود . فردوسی
( طوسی ) کوید :

پیزدان هر آن کی که شد ناسپای پدلش آندر آید ز هر مو هرای »
« لغت فرس ص۱۹۱ ورله: تذ کرة الاولیاء چاپ اروپا جاص۸۸ی۰۱۲

‎٩‏ -
```


## [2026-09-14T02:31:41.637Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"catholic\" \"holocaust\" \"hologram\" \"holograph\" ; do echo \"=== $w\"; grep -n -i -m3 \"^$w\\|^ *$w,\" KLN_1966.txt | head -5; done\necho \"--- catholic ctx\"; grep -n -i \"catholic\" KLN_1966.txt | head -8"
}
```


### [2026-09-14T02:31:42.777Z] TOOL RESULT

```
=== catholic
6814:catholic,  adj.  —  F.  catholique,  fr.  Eccles.  L.  catho- licus,  fr.  Gk.  xxffoXixo?,  ‘general,  universal’,  fr. xxffoXoo  =  xxff’  0X00,  ‘on  the  whole,  in  general’, fr.  xxtx,  ‘according  to’  (see  cata-),  and  oXop, ‘whole’,  which  stands  for  *5Xfop,  fr.  I.-E.  base *sol-wos,  whence  also  L.  salvus,  ‘saved,  pre¬ served,  safe’.  See  safe  and  cp.  holo-.  Cp.  also catholicon.
6816:catholicity,  n.,  1)  the  quality  of  being  catholic;
6818:catholicon,  n.,  a  remedy  for  all  diseases.  —  Gk. xocffoXixov,  neut.  of  xaffoX'.xop,  ‘general,  uni¬ versal’.  See  catholic.
=== holocaust
17952:holocaust,  n.,  1)  a  burnt  offering;  2)  complete destruction  by  fire;  3)  a  great  destruction.  — - F.  holocauste,  fr.  L.  holocaustum,  fr.  Gk.  6X6- xauoxov,  lit.  ‘a  thing  wholly  burnt’,  neut.  of  the adj.  6X6x0010x04,  which  is  compounded  of  8X0?, ‘whole’  (see  holo-),  and  xouctt6 4,  verbal  adj.  of xodciv  (for  *xifiEiv),  ‘to  bum’.  See  caustic. Derivatives:  holocaust-al,  holocaust-ic,  adjs. holograph,  n.,  a  document  written  entirely  by  the person  from  whom  it  proceeds.  —  Late  L.  holo¬ graphs  (whence  also  F.  holographe),  fr.  Gk. oXdypocqiop,  ‘written  in  full,  written  entirely  by the  same  hand’,  which  is  compounded  of  6X04, ‘whole’  (see  holo-),  and  -ypatpo;,  fr.  Ypa<peiv,  ‘to write’.  See  -graph.
=== hologram
=== holograph
--- catholic ctx
1041:Roman  Catholic  Church
5061:biretta,  n.,  a  square  cap  worn  by  the  Roman Catholic  clergy.  —  It.  berretta,  fr.  Late  L.  birrus, also  birrum,  ‘large  cloak  with  a  hood’,  which  is of  Gaulish  origin;  cp.  Mir.  berr,  W.  byrr,  ‘short’. Cp.  barret,  beret,  burnous, birr,  intr.  v.,  to  whir.  —  Of  imitative  origin, birrellism,  n.,  style  resembling  that  of  Augustine Birrell  (1850-1933).  —  For  the  ending  see suff.  -ism.
5613:brevi-,  combining  form  meaning  ‘short’.  —  L. breve-,  fr.  brevis,  ‘short’.  See  brief,  adj. breviary,  n.,  a  short  prayer  book  used  by  priests in  the  Roman  Catholic  Church.  —  L.  brevia- rium,  ‘summary’,  neut.  of  the  adjective  brevi- arius,  ‘abridged’,  used  as  a  noun,  fr.  brevidre, ‘to  shorten,  abbreviate’,  fr.  brevis,  ‘short’.  See brief,  adj.,  and  subst.  suff.  -ary  and  cp.  brevet, abbreviate.  Cp.  also  brimborion. brevier,  n.,  a  size  of  small  type,  between  bour¬ geois  and  minion  ( typogr .)  —  Lit.  ‘the  breviary type"  (cp.  G.  Brevier,  ‘breviary’);  so  called  be¬ cause  this  type  was  used  originally  in  printing breviaries.
6814:catholic,  adj.  —  F.  catholique,  fr.  Eccles.  L.  catho- licus,  fr.  Gk.  xxffoXixo?,  ‘general,  universal’,  fr. xxffoXoo  =  xxff’  0X00,  ‘on  the  whole,  in  general’, fr.  xxtx,  ‘according  to’  (see  cata-),  and  oXop, ‘whole’,  which  stands  for  *5Xfop,  fr.  I.-E.  base *sol-wos,  whence  also  L.  salvus,  ‘saved,  pre¬ served,  safe’.  See  safe  and  cp.  holo-.  Cp.  also catholicon.
6815:Derivatives:  catholic,  n.,  catholic-al,  adj.,  catho- lic-al-ly,  adv.,  catholic-ism,  n.,  catholic-ize,  tr.  v., catholic-iz-er,  n.,  catholic-ly,  adv.
6816:catholicity,  n.,  1)  the  quality  of  being  catholic;
6817:z)  universality;  3)  ( usually  cap.)  Catholicism.  — Coined  by  Coleridge  fr.  catholic  and  suff.  -ity on  analogy  of  F.  catholicite  which  was  coined by  Theodore-Agrippa  d’Aubigne  (1552-1630) fr.  catholique,  ‘Catholic’.
6818:catholicon,  n.,  a  remedy  for  all  diseases.  —  Gk. xocffoXixov,  neut.  of  xaffoX'.xop,  ‘general,  uni¬ versal’.  See  catholic.
```


## [2026-09-14T02:31:43.320Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN sophist\"; grep -n -i \"sophist\\b\" KLN_1966.txt | head -6\necho \"=== KLN sophomore\"; grep -n -i \"sophomore\" KLN_1966.txt SKT.txt | head -6\necho \"=== KLN safe\"; grep -n \"^safe\\|salvus\" KLN_1966.txt | head -8"
}
```


### [2026-09-14T02:31:43.417Z] TOOL RESULT

```
=== KLN sophist
10677:deipnosophist,  n.,  one  learned  in  the  art  of  din¬ ing.  —  Gk.  SEt7rvoaocpiaTT)<;,  compounded  of Seitcvov,  ‘dinner’,  and  cotpia-rijc,  ‘a  learned man’,  fr.  0098?,  ‘skilled,  clever,  wise’.  See  dcip- no-  and  sophist.  A£t7rvo<jo9taTaL  (pi.)  is  the  title of  a  work  by  Athenaeus.
10678:Derivative:  deipnosophist-ic,  adj. deism,  n.,  the  belief  that  God  has  created  the world  but  has  no  immediate  relation  with  it.  — F.  deisme,  a  hybrid  coined  by  Pascal  (1623-62) fr.  L.  Deus,  ‘God’,  and  -isme,  a  suff.  of  Greek origin.  See  deity  and  -ism. deist,  n.,  an  adherent  of  deism.  —  F.  deiste,  a hybrid  word.  See  prec.  word  and  -ist. Derivatives:  deist-ic,  deist-ic-al,  adjs.,  deist-ic- al-ly,  adv.
16458:Derivatives:  gorge,  intr.  and  tr.  v.,  gorg-ed,  adj. gorgeous,  adj.  —  OF.  gorgias,  ‘finely  dressed, luxurious’,  formed  from  the  name  of  Gorgias, a  Greek  sophist  and  rhetorician  (about  483- 375),  who  took  pleasure  in  showing  off  his luxury.
16931:Gymnorhina,  n,  a  genus  of  birds,  the  piping  crow (ornithol.)  —  ModL,  prop,  ‘having  naked  nos¬ trils’,  compounded  of  gymno-  and  Gk.  ptc, gen.  plvd;,  ‘nose’.  See  rhino-  and  cp.  next  word, gymnorhinal,  adj,  having  naked  nostrils  (said  of crows).  —  See  prec.  word  and  rhinal, gymnosophist,  n,  member  of  a  sect  of  philo¬ sophers  in  ancient  India,  who  walked  naked.  • — L.  gynmosophistae  (pi.),  fr.  Gk.  yj|ivoao9iaTai (pi.),  which  is  compounded  of  yupivop,  ‘naked’, and  the  pi.  of  0091  nxrfi,  ‘philosopher’.  See gymno-  and  sophist.
27161:pansophist,  n.  —  See  prec.  word  and  sophist, pansophy,  n.,  universal  wisdom.  —  See  panso¬ phism  and  -y  (representing  Gk.  -ia).
28540:philosophic,  philosophical,  adj.  —  L.  philosophicus, fr.  Gk.  91X00091x65,  fr.  91X000915,  ‘philosophy’. See  philosophy  and  -ic,  resp.  also  -al. philosophism,  n.,  sophistry.  —  F.  philo  sophisme, formed  fr.  philosophic  with  suff.  -isme.  See philosophy  and  -ism  and  cp.  sophism, philosophist,  n.,  a  sophist.  • —  F.  philosophiste, formed  fr.  philosophic  with  suff.  -iste.  See  phi¬ losophy  and  -ist  and  cp.  prec.  word, philosophize,  intr.  v.  —  See  philosophy  and  -ize.
=== KLN sophomore
KLN_1966.txt:35928:Derivative:  sop,  tr.  and  intr.  v.,  to  dip  (bread), etc.  into  liquid,  sopp-er,  n.,  sopp-ing,  adj.  and  n. soph,  n. — Abbreviation  of  sophister  or  sophomore. Sopherim,  n.  pi.,  1)  the  Hebrew  scribes,  orig. copyists  and  interpreters  of  the  Bible;  in  a  special sense;  2)  a  body  of  teachers  who  interpreted  the Law  in  the  last  centuries  of  the  second  Common¬ wealth.  —  Heb.  soph6  rim,  ‘scribes’,  pi.  of  sopher, lit.  ‘bookman’,  denominated  fr.  sepher,  ‘book’. See  Sepher  Torah.
KLN_1966.txt:35930:0096?,  ‘wise’.  See  next  word, sophism,  n.  —  ME.  sophime,  fr.  OF.  soffime,  so- phime,  sophisnte  (F.  sophisme),  fr.  L.  sophisma, fr.  Gk.  o6oL<T|xa,  from  the  stem  of  ooqj^csv,  ‘to make  wise,  instruct’,  aofpi^ecrDai,  ‘to  become wise;  to  devise,  cleverly,  play  subtle  tricks’,  fr. 009 6c,  ‘clever,  skilled,  prudent,  cunning,  learn¬ ed,  wise’,  which  is  of  uncertain  origin.  Cp.  So¬ phia,  sophist,  sophisticate,  the  first  element  in sophomore  and  the  second  element  in  panso¬
KLN_1966.txt:35936:sophistication,  n.  —  ME.  sophisticacioun,  fr.  ML. sophisticatio,  gen.  -onis,  fr.  sophistiedtus,  pp.  of sophisticate.  See  prec.  word  and  -ion. sophistry,  n.,  clever  but  unsound  reasoning.  — ME.  sophistrie,  fr.  OF.  sophisterie,  sophistrie  (F. sophisterie ),  fr.  sophiste.  See  sophist  and  -ry. sophomore,  n.,  a  second  year  student  at  an  Amer¬ ican  university.  —  Alteration  of  obsolete  so- phumer,  formed  fr.  sophume,  an  old  var.  of  so¬ phism,  fr.  Gk.  06910510:,  ‘cunning  contrivance, device,  invention’,  fr.  0090c,  ‘clever,  skilful, wise’ ;  see  sophism.  The  change  of  sophumer  to sophomore  was  due  to' a  popular  misconception of  the  former  word  as  a  compound  of  0096;, ‘clever’,  and  p<op6i;,  ‘foolish,  dull’.
=== KLN safe
6814:catholic,  adj.  —  F.  catholique,  fr.  Eccles.  L.  catho- licus,  fr.  Gk.  xxffoXixo?,  ‘general,  universal’,  fr. xxffoXoo  =  xxff’  0X00,  ‘on  the  whole,  in  general’, fr.  xxtx,  ‘according  to’  (see  cata-),  and  oXop, ‘whole’,  which  stands  for  *5Xfop,  fr.  I.-E.  base *sol-wos,  whence  also  L.  salvus,  ‘saved,  pre¬ served,  safe’.  See  safe  and  cp.  holo-.  Cp.  also catholicon.
17794:which  the  robber  is  supposed  to  bring  his  victim to  a  sudden  stop, hfira,  n.  —  See  hegira. hike,  intr.  v.  —  Prob.  a  var.  of  hitch, hilarious,  adj.,  merry,  gay.  —  Formed  with  suff. -ous  fr.  L.  hilarus,  hilaris,  ‘cheerful,  gay’,  fr.  Gk. !Xap6<;,  of  s.m.,  which  is  rel.  to  *(Xr,aL  (for  *ai- aXir)-p,i),  ‘I  am  gracious’  (only  in  the  imper. : Homeric  “Xvjfh,  Dor.  iXafk,  Aeol.  eXXalH,  ‘be gracious!’),  tXaav.ou.at  (for  *ai-aXa-axop.at),  ‘I appease,  propitiate,  reconcile  to  myself’,  Les- bic  tXXaoc,  Homeric  iXa(f)o<;,  Laconic  tX-qfos, Att.  IXeta?,  ‘propitious,  gracious’,  and  cogn. with  L.  solari,  ‘to  comfort’,  salvus,  ‘whole,  safe’, OE.  stelig,  gesxlig,  ‘happy,  fortunate’.  See  silly and  cp.  words  there  referred  to.  Cp.  also  Hilary, exhilarate.
33472:safe,  adj.  —  ME.  sauf,  saf  fr.  OF.  salf,  sauf (F.  sauf),  fr.  L.  salvus,  ‘saved,  preserved,  safe, well,  sound’,  which  is  rel.  to  salus,  ‘sound  con¬ dition,  welfare,  well-being,  health,  safety’,  salu- hris,  ‘health-giving,  healthful’,  solidus,  soldus, ‘firm,  compact'  OL.  sollus,  ‘whole,  entire’,  and cognate  with  OI.  sarvah,  ‘uninjured,  intact, whole,  entire’,  Avestic  haurva-,  ‘uninjured,  in¬ tact',  Toch.  A  salu,  B.  solme,  ‘whole,  entire’, Arm.  o4j,  ‘healthful,  entire’,  Gk.  oXcs  (for *8Xfos),  ‘whole’,  Alb.  gale,  ‘strong,  fat,  vigor¬ ous’.  Cp.  sage,  name  of  a  plant,  salutary,  saluta¬ tion,  salute,  salvage,  salvation,  salve,  ‘hail’, Salvia,  salvo,  save,  silly,  soldo,  solemn,  solicit, solid,  solidus,  sou.  Cp.  also  holo-  and  the  second element  in  catholic.
33473:Derivatives:  safe,  n.,  safe-ly,  adv.,  safe-ness,  n. safe-conduct,  n.  —  Anglicized  fr.  F.  sauf-conduit, fr.  L.  salvus  conductus.  See  safe  and  conduct. Derivative:  safe-conduct,  tr.  v. safeguard,  n.  —  Late  ME.  saufgarde,  fr.  MF.  (= F.)  sauvegarde,  ‘safekeeping,  safeguard’,  fr.  OF. salve  sauve  (F.  sauve),  fern,  of  salf,  sauf  (F.  sauf), ‘safe’  and  garde,  ‘a  keeping’.  See  safe  and  guard and  cp.  sagger.
33476:safety,  n.  —  ME.  sauvete,  saufte,  fr.  MF.  (=  F.) sauvete,  fr.  OF.  salvete ,  sauvete,  fr.  ML.  salvitd- tem,  acc.  of  salvitas,  ‘safety’,  fr.  L.  salvus.  See safe  and  -ty.
33488:salvus,  ‘safe,  whole’.  Salvia  lit.  means ‘the  sav¬ ing  plant’.  See  safe  and  cp.  Salvia, sagger,  saggar,  n.,  1)  a  protective  box  of  fire  clay in  which  finer  ceramic  articles  are  enclosed while  baking;  2)  the  clay  of  which  it  is  made.  — Prob.  a  contraction  of  safeguard.
33587:salute,  tr.  and  intr.  v.  —  ME.  saluten,  fr.  L.  salu¬ tare,  ‘to  greet’,  fr.  salits,  gen.  salutis,  ‘welfare, health,  safety,  a  wish  for  somebody’s  welfare,  a greeting’,  which  is  rel.  to  salvus,  ‘safe’.  See  safe and  cp.  words  there  referred  to. salute,  n.  —  ME.  salut,  fr.  OF.  (=  F.)  salut,  fr.
33590:salvage,  n.  —  F.  salvage  (now  sauvetage),  fr.  MF. salvage,  fr.  salver  (F.  sauver ),  ‘to  save’,  fr.  L. salvare,  ‘to  save',  fr.  salvus,  ‘safe’.  See  safe  and -age.
```


## [2026-09-14T02:31:58.476Z] TOOL CALL #37: Bash

```json
{
 "command": "pdftoppm -f 464 -l 464 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg464 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg464.png"
}
```


### [2026-09-14T02:32:00.138Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 77174 Sep 13 22:32 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg464.png
```


## [2026-09-14T02:32:00.542Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN whole/all\"; grep -n \"13.1[0-9] \" SYN.txt | head -5\ngrep -n \"solidus\\|sollus\\|salvus\" LEW_1910.txt LAT.txt | head -12\necho \"=== IEC solo\"; grep -n \"^solo-\\|^sol-\\|solu̯o\" IEC.txt | head -10"
}
```


### [2026-09-14T02:32:00.651Z] TOOL RESULT

```
=== SYN whole/all
8025:Sp. cansado, pple. of cansar ‘tire’ (now trans.; refl. ‘get tired’), this (not : Fr. casser ‘break’ ifr. Lat. quassare ‘shake’, as Diez 91, REW 6939, but) = It. cansare ‘avoid’, fr. Lat. campsdre ‘turn aside from’, fr. Grk. xaépyar aor. Of kaurrw ‘bend’ (9.14). So Korting, Menéndez Pidal, C. C. Rice, Language 13.18 f., 19.154, Leo Spitzer, Language 14.205 f., Wartburg 2.156. Lat. campsdare occurs in Ennius in the nautical sense of doub- ling a headland (frequent in Grk.), then only in late Latin in more general sense of ‘turn aside from’ e.g. ut de via cam- semus Pereprinatio 10.8 and in many Blosses, The semantic development in Spanish was prob. (otherwise Rice) oan > ‘cease’ > ‘get hired INe ra as ie > es atl oie re 4 € association is there, ‘get tired? ae cho Russ. ustavat! 0 Slensich » ustate get tired, cease’ =
23351:13.11 Quantity
23352:13.12 Numper
23353:13.13 WHOLE
23354:13.14 Every; Au (pl.)
LAT.txt:5291:sollers : habile, adroit, ingenieux (cf. sollus); sollertia.
LAT.txt:13507:cf. solidus. Cf.peruinca.
LAT.txt:31584:est forme d'apres fragosus', labidus (Vitr.) d'apres solidus', labilis
LAT.txt:52738:an supra morem si densa requiras; Coi. 3,9,6 rara seges; k solidus
LAT.txt:55218:Sans le suffixe -wo-, on a en latin m£me solidus, avec -I- simple
LAT.txt:55219:(cf.osq.suluh "omninO"?) et sollus, avec -l- g^minee, ce dernier
LAT.txt:55228:pareil en tout a lat. sollus, gall.XoII; il y a -I- simple dans ala-
LAT.txt:55230:1 'ensemble des hommes"), ce qui rappelle lat.sollus: solidus. - M.
LAT.txt:58360:(i/«4 da solidus), d'ob A basse 4 poque siliquatarius "percepteur d'an
LAT.txt:59004:solidus (avec vocalisme int 4 rieur e,- soledas CIL I a 1539),-a,
LAT.txt:59013:Sous Constantin, solidus, soldus (sc.nummus) a ddsignd une pibce
LAT.txt:59017:il est bien repr 4 sent 4 en britt.: gall .sullt, etc. L'adj. solidus
=== IEC solo
```


## [2026-09-14T02:32:03.629Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg464.png"
}
```


### [2026-09-14T02:32:04.212Z] TOOL RESULT

```

```


## [2026-09-14T02:32:04.203Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:32:38.339Z] TOOL CALL #40: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T02:32:38.346Z] TOOL RESULT

```


```


## [2026-09-14T02:32:41.288Z] TOOL CALL #41: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg464.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/464.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-14T02:32:41.430Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-14T02:32:47.927Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/s%C3%B3lh%E2%82%82wos",
 "prompt": "Give the reconstructed PIE form, its meaning, and the list of descendants (especially Proto-Indo-Iranian/Avestan, Greek, Latin). Quote the etymology/derivation notes verbatim."
}
```


### [2026-09-14T02:32:49.321Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:32:49.402Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%87%D8%B1",
 "prompt": "For the Persian entry هر (har): quote the etymology section verbatim (Middle Persian, Old Persian, Avestan, Proto-Iranian forms) and the meaning."
}
```


## [2026-09-14T02:32:51.465Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A7%D8%AB%D9%84%D9%8A%D9%82",
 "prompt": "Quote the Arabic entry جاثليق: etymology (Greek katholikos, any Syriac intermediary), meaning, and any usage notes."
}
```


### [2026-09-14T02:32:52.734Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:32:53.055Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/catholic",
 "prompt": "Quote the full etymology of 'catholic', including Greek katholikos, katholou, Latin catholicus, Old French catholique, and dates."
}
```


### [2026-09-14T02:32:55.465Z] TOOL RESULT

```
# Persian Entry for هر (har)

**Etymology:** The word derives from Middle Persian (script needed) with the form KRA, and earlier from Proto-Iranian *hárwah. It traces back to Proto-Indo-Iranian *sárwas ("whole, all, entire"), ultimately from Proto-Indo-European *solh₂-wó-s.

**Meaning:** The determiner هر (har) means "each" or "every" in Persian.
```


### [2026-09-14T02:32:58.489Z] TOOL RESULT

```
# Etymology of "Catholic"

The word "catholic" originates from mid-14c. French *catholique*, derived from Church Latin *catholicus* meaning "universal, general." This Latin term came from Greek *katholikos*, formed from the phrase *kath' holou* ("on the whole, in general"), combining *kata* ("about") with the genitive of *holos* ("whole").

**Key timeline:**
- **Mid-14c.**: The adjective entered English as *catholik*, referring to "doctrines of the ancient Church," literally "universally accepted"
- **1550s**: The general sense of "embracing all, universal" is documented in English
- **c. 1554**: Protestants began applying the capitalized form to the Church in Rome following the Reformation
- **1560s**: The noun form emerged, denoting "member of the Roman Catholic church"
- **1580s**: The meaning expanded to include "not narrow-minded or bigoted"

The Latin word was rendered in Old English as *eallgeleaflic*, and Medieval Latin *catholicus* became practically synonymous with *Christianus*, meaning "constituting or conforming to the church, its faith and organization."
```


## [2026-09-14T02:33:04.251Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/solh%E2%82%82w%C3%B3s",
 "prompt": "Give the reconstructed PIE form, meaning, and descendants (Indo-Iranian, Greek, Latin, Armenian, Tocharian) verbatim."
}
```


### [2026-09-14T02:33:05.552Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:33:06.368Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3%D9%81%D8%A9",
 "prompt": "Quote the Arabic entry فلسفة: etymology (Greek philosophia, any Syriac mediation), root f-l-s-f, derived terms like فيلسوف and تفلسف."
}
```


## [2026-09-14T02:33:07.841Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%81%D8%B3%D8%B7%D8%A9",
 "prompt": "Quote the Arabic entry سفسطة: etymology (Greek sophistes/sophisma), meaning, and related forms."
}
```


## [2026-09-14T02:33:08.730Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sophomore",
 "prompt": "Quote the full etymology of 'sophomore' and of 'sophist'/'sophism' if shown."
}
```


### [2026-09-14T02:33:12.335Z] TOOL RESULT

```
# Arabic Entry: سفسطة (safsaṭa)

**Etymology:**
The word derives from a verbal noun of "safsaṭa" (to be a sophist), which itself comes from "safsaṭāʔiyy" (sophist). The Wiktionary entry does not explicitly mention Greek origins.

**Meaning:**
"(philosophy) sophism, sophistry (fallacious reasoning or argumentation)"

**Related Forms:**
The entry documents descendants across multiple languages:
- Azerbaijani: səfsətə
- Ottoman Turkish/Turkish: safsata
- Tatar: сафсата
- Uzbek: safsata

**Note:** While the term's ultimate origin likely traces to Greek (sophistēs/sophisma), this specific Wiktionary article focuses on the Arabic verbal noun formation and its documented linguistic descendants rather than providing etymological commentary on Greek roots.
```


### [2026-09-14T02:33:12.656Z] TOOL RESULT

```
# فلسفة (Philosophy) - Etymology and Linguistic Details

Based on the Wiktionary entry, here's what's documented about this Arabic term:

## Etymology

The word فلسفة (falsafa) derives from the root ف ل س ف (f-l-s-f) and represents "the verbal noun of فَلْسَفَ (falsafa, 'to philosophize')." The entry indicates it was either constructed based on فيلسوف (faylasūf, meaning "philosopher"), or borrowed directly from Ancient Greek φιλοσοφία (philosophía).

## Linguistic Classification

The term functions as a feminine noun with sound feminine plural forms (فَلْسَفَات - falsafāt). It follows triptote declension patterns typical of Arabic nouns ending in -ة.

## Semantic Reach

The word meaning "philosophy" has expanded across numerous languages through the centuries, including Ottoman Turkish, Persian, Swahili, Turkmen, Uzbek, and various Caucasian and Central Asian languages, demonstrating how this concept traveled along historical trade and cultural exchange routes.
```


### [2026-09-14T02:33:14.530Z] TOOL RESULT

```
# Etymology of Sophomore and Sophism

## Sophomore

The word originates in the 1680s as "student in the second year of university study," derived from the earlier term *sophumer* (1650s). It traces back through *sophume*, an archaic variant of sophism, ultimately from Greek *sophistēs* meaning "a master of one's craft; a wise or prudent man."

The modern form likely developed through folk etymology, combining Greek *sophos* ("wise") + *mōros* ("foolish, dull"), "as if in allusion to the exaggerated opinion which students at this age are apt to have of their wisdom."

## Sophism

According to the page's related content, sophism originates in the "mid-14c., sophime, 'subtle but fallacious argument devised for purposes of deceit or to exercise one's ingenuity,' from Old French sophime, sofisme 'a fallacy, false argument.'" It derives from Latin *sophisma* and Greek *sophisma*, meaning "clever device, skillful."

The term connects to the Greek root *sophos* (wise), reflecting its evolution from describing intellectual exercises to denoting deceptive reasoning.
```


## [2026-09-14T02:33:21.150Z] TOOL CALL #50: WebSearch

```json
{
 "query": "wiktionary Reconstruction Proto-Indo-European solh₂wós whole Avestan haurva Greek holos",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


## [2026-09-14T02:33:23.591Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%AA%D9%88%D9%84%DB%8C%DA%A9/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for کاتولیک verbatim, including any origin tag such as [فر.] or [یو.], and also the Dehkhoda entry if shown."
}
```


## [2026-09-14T02:33:25.603Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AC%D8%A7%D8%AB%D9%84%DB%8C%D9%82/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for جاثلیق verbatim including the origin tag, and the Dehkhoda entry (especially any statement that it is معرب of Greek/Latin catholicos)."
}
```


### [2026-09-14T02:33:27.279Z] TOOL RESULT

```
Web search results for query: "wiktionary Reconstruction Proto-Indo-European solh₂wós whole Avestan haurva Greek holos"

Links: [{"title":"ὅλος - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%BD%85%CE%BB%CE%BF%CF%82"},{"title":"Reconstruction:Proto-Italic/salawos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Italic/salawos"},{"title":"هر - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%87%D8%B1"},{"title":"Reconstruction:Proto-Indo-European/geH- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/geH-"},{"title":"Reconstruction:Proto-Indo-European/h₁óynos - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3ynos"},{"title":"Reconstruction:Proto-Indo-European/éǵh₂ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%A9%C7%B5h%E2%82%82"},{"title":"gjallë - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/gjall%C3%AB"},{"title":"Reconstruction:Proto-Indo-European/solh₂- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/solh%E2%82%82-"},{"title":"όλος - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CF%8C%CE%BB%CE%BF%CF%82"},{"title":"सर्व - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A4%B0%E0%A5%8D%E0%A4%B5"}]

I found several relevant Wiktionary entries related to your search query. Here's what the results show:

The Greek word ὅλος (hólos, "whole") comes from Proto-Indo-European *solh₂wós, which derives from *solh₂- ("whole"). 

Cognates of this root include Sanskrit सर्व (sárva), Avestan 𐬵𐬀𐬎𐬭𐬬𐬀 (haurva), Latin salvus, and sollus.

The search results also include a dedicated Wiktionary reconstruction page for Proto-Indo-European *solh₂-, which means "whole".

Additionally, the Persian word هر (her) derives from Proto-Iranian, with Avestan 𐬵𐬀𐬎𐬭𐬬𐬀 (haurva, "whole, each") coming from Proto-Indo-Iranian *sárwas ("whole, all, entire"), which itself comes from Proto-Indo-European *solh₂wós.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-14T02:33:28.277Z] TOOL RESULT

```
# Definitions of کاتولیک (Catholic)

## Dehkhoda Dictionary Entry
The etymological source traces back to Greek "katholikos" meaning "universal and comprehensive," originally applied to bishops' leaders. Today, it refers to "a sect of Christians who recognize the Pope as their religious leader."

## Mo'in Dictionary Entry
"(تُ) [فر.] (اِ.) دارای مذهب کاتولیک، کسانی از پیروان مسیح که به پاپ عقیده دارند و از او اطاعت می کنند."

This entry indicates those adhering to Catholicism are followers of Christ who believe in and obey the Pope. The abbreviations show it's French origin [فر.], with Persian pronunciation marked as (تُ).
```


### [2026-09-14T02:33:30.928Z] TOOL RESULT

```
# Entries for جاثلیق

## Farhang-e Mo'in (Mo'in Dictionary)

The entry states: *"(ثِ ) \[ معر. \] (اِ. ) پیشوای ترسایان"* (indicating it is معرب/borrowed, and defines it as "leader of Nestorians").

## Dehkhoda Entry

The Dehkhoda dictionary begins its entry by defining جاثلیق as: *"قاضی ترسایان"* (judge of Nestorians), and notes it is *"معرب"* (borrowed/Arabicized). While the entry discusses various meanings and historical references, it does not explicitly state in the provided text that جاثلیق derives from Greek or Latin catholicos. However, the "Dāneshnāme-ye Āzād-e Fārsī" section does clarify: *"واژه جاثلیق از کلمه کاتولیک گرفته شده است"* (the word جاثلیق is derived from the word catholicos).
```


## [2026-09-14T02:33:37.701Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BD%85%CE%BB%CE%BF%CF%82",
 "prompt": "Quote the Ancient Greek entry ὅλος: etymology verbatim (PIE *solh₂wós, *hólwos, cognates), meaning, and derived terms including καθόλου and καθολικός and ὁλόκαυστος."
}
```


## [2026-09-14T02:33:39.932Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%81%D8%B3%D8%B7%D9%87/",
 "prompt": "Quote the فرهنگ معین entry for سفسطه verbatim with its origin tag, and any Dehkhoda note on its Greek origin (سوفسطا / سوفسطائی)."
}
```


## [2026-09-14T02:33:41.532Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D9%84%D8%B3%D9%81%D9%87/",
 "prompt": "Quote the فرهنگ معین entry for فلسفه verbatim with its origin tag (e.g. [ع. یو.]) and any note that it is from Greek philosophia; also quote the Dehkhoda note."
}
```


### [2026-09-14T02:33:42.795Z] TOOL RESULT

```
# Ancient Greek ὅλος Entry

**Etymology:**
The word derives from "Proto-Indo-European *solh₂wós, from *solh₂- ('whole')." Related words include Sanskrit sárva, Avestan haurva, Latin salvus and sollus.

**Meaning:**
The adjective conveys several senses: "whole, entire, perfect, complete"; "absolute, utter"; "generally, on the whole"; when negated, "at all"; and "actually."

**Derived Terms:**
The page lists ὁλοσχερής (holoskherḗs) and ὅλως (hólōs) as derived forms. However, the document does not include entries for καθόλου, καθολικός, or ὁλόκαυστος—these terms do not appear in the provided Wiktionary content.
```


### [2026-09-14T02:33:45.450Z] TOOL RESULT

```
# فرهنگ معین Entry for سفسطه

**Origin Tag:** (سَ سَ طِ ) ( اِ. )

**Definition:** "(سَ سَ طِ ) ( اِ. ) مغالطه کردن برای وارونه نشان دادن حقایق"

This entry translates to: engaging in fallacious reasoning to distort or reverse the presentation of truths.

## Dehkhoda Reference to Greek Origins

While the Dehkhoda entry does not explicitly reference "سوفسطا" or "سوفسطائی" in its main text, the Islamic Encyclopedia section (دانشنامه اسلامی) within this document discusses **سوفسطائیان** (Sophists) as the originators of this philosophical school, noting that "سفسطه" or "سوفسطاییگری" represents their intellectual approach—one that denies the possibility of certain knowledge about reality.

The document establishes that the term derives from the Greek Sophist tradition, though a direct etymological note attributing it to Greek origins is not prominently featured in the Dehkhoda section itself.
```


### [2026-09-14T02:33:48.229Z] TOOL RESULT

```
# فلسفه (Philosophy)

## From Farhangs-e Moein:

**(فَ لْ سَ فِ) [ع.] (اِ.)** 
- "حکمت، دانشی که موضوع آن هستی و وجود است" (wisdom; knowledge whose subject is being and existence)
- "علت، دلیل" (cause; reason)
- "فلسفه بافی" as idiom: allusion to expressing views distant from logic

## From Dehkhoda's Lexicon:

The entry explains that philosophy derives from Greek origins, combining "philos" (friend, lover) and "sophia" (wisdom). Dehkhoda notes it represents "علم به حقایق موجودات به اندازه توانایی بشر" (knowledge of realities of existents within human capacity).

The classical division encompasses practical philosophy (ethics, household management, civil governance) and theoretical philosophy (divided into lower, middle, and higher branches addressing material, mathematical, and metaphysical subjects respectively).

---

**Note:** The page reflects multiple traditional Persian equivalents proposed by contributors, including خردشناسی and فرزانش, though these remain less standardized than the established term فلسفه.
```


## [2026-09-14T02:34:01.700Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%D9%87%D8%B1\" \"https://www.etymonline.com/word/catholic\" \"https://www.etymonline.com/word/sophomore\" \"https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3%D9%81%D8%A9\" \"https://en.wiktionary.org/wiki/%D8%B3%D9%81%D8%B3%D8%B7%D8%A9\" \"https://en.wiktionary.org/wiki/%E1%BD%85%CE%BB%CE%BF%CF%82\" \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%AA%D9%88%D9%84%DB%8C%DA%A9/\" \"https://abadis.ir/fatofa/%D8%AC%D8%A7%D8%AB%D9%84%DB%8C%D9%82/\" \"https://abadis.ir/fatofa/%D8%B3%D9%81%D8%B3%D8%B7%D9%87/\" \"https://abadis.ir/fatofa/%D9%81%D9%84%D8%B3%D9%81%D9%87/\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/solh%E2%82%82-\"; do python3 tools/fetch_source.py \"$u\" --note \"page 464, roots Sol / Sophos: har, catholic, sophomore, falsafa, safsata, holos, katolik, jaseliq, Mo'in entries, PIE *solh2-\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T02:34:12.107Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2ea8152cf8a70a37.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb33ad262db6ffa2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f2a38fa65cab00ab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b2da7c6ca99911b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/abff3d937f81ac40.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f0371968a8fd7f77.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/70cf4f7007f7bbe0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fe45ce99be7c64e9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/676922fbd0c42e56.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e3245a1e0bdcc669.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65788da2c53d572a.txt
```


## [2026-09-14T02:34:30.671Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT haruva\"; grep -n \"haruva\" KNT_full.txt KNT.txt | head -6\necho \"=== WLD Bd2 solo\"; grep -n -i \"solo-\\|sol(e)uo\\|salvus\" incoming/WLD/WLD_Bd2_pages.txt | head -8\necho \"=== SYN 13.13\"; grep -n \"13\\.13\" SYN.txt | head -5\necho \"=== AFA jathaliq\"; grep -n -i \"athalīq\\|atalīq\\|Katholikos\\|katholikos\\|ja.taliq\" AFA.txt | head -8"
}
```


### [2026-09-14T02:34:30.781Z] TOOL RESULT

```
=== KNT haruva
KNT.txt:607:II. For OP -атш- we find the following ex- amples: haruva-, once written fra-haravam; Skt. sárva-
KNT.txt:1346:§107. PIE 1 became pAr. r, and therefore was indistinguishable from pIE r in the Aryan lan- guages, unless a cognate from another ТЕ branch can be adduced. pIE *selyo- ‘all’, OP haruva-, Av. haurva-, Skt.
KNT.txt:1412:OP haruva- ‘all’, Skt. sárva-.
KNT.txt:2240:pronominal antya-, haruva-, һата, $203; for the
KNT.txt:2274:In loc. (pIE) *-dhe: ada-, avada, ida, [haruvadā], dürada.
KNT.txt:2298:(1) Semi-pronominal adjectives: aniya- ‘other’, haruva- ‘all’, hama- ‘one and the same’.
=== WLD Bd2 solo
3605:^paluos^       *polmSy wie salviis aus ^soluos^ s. ^solo-; -lu- zu -ll- unter
33667:  Gleichsetzung mit          "^solo- „wohlbelialten, heil, ganz“ (gr, oXog, lat.
33669:       salvus^ usw.) vertritt z, B. Yanicek aaO., Fick 1^ 564, 11^ 304, III*
33672:436, Palk-Torp u. salig\ sie scheint mir, obwohl laL salvus^ solus einzelne
33881:510                             songli(o-, -a),       sonqo-   —   solo-, sol(e)uo-
33947:solo-, sol(e))ao- u. dgl. „wohlbehalten, ganz‘\
33949:versehrt, ganz“         {= gr. okog, ovXog, alb. gah, vgl. auch lat. salvus)y ai. sar-
33955:                                          solo-, 8ol(e)uo-                                511
=== SYN 13.13
23353:13.13 WHOLE
23429:13.13 WHOLE
28759:Goth. aljan (renders fos as ‘jeal- ousy’, Rom. 13.13, otherwise ‘zeal’) = ON eljan ‘energy, endurance’, OE ellen ‘strength, vigor, courage’, OHG ellen ‘zeal, strength’, etc., etym. dub., perh. : Lat. alacer ‘lively, eager, glad’. Walde- P. 1.156. Falk-Torp 188. Feist 38. Walde-H. 1.25.
=== AFA jathaliq
```


## [2026-09-14T02:34:31.677Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT 55210-55235\"; sed -n '55210,55235p' LAT.txt\necho \"=== LAT 59000-59020\"; sed -n '59000,59020p' LAT.txt"
}
```


### [2026-09-14T02:34:31.756Z] TOOL RESULT

```
=== LAT 55210-55235
trouve dans osq.craXaFc, salavs "saluus", ombr. saluvom "saluum", etc.;
et dans le nom de notion lat.saZus, qui est ancien (v. BSL 98, p.401045
samlu s
et suiv. ), tandis que a.v. haurv atds , qui y repond pour le sens, est
un derive secondaire de haurvo. Les mots italicjuea supposent une
forne de suffixe a voyelle initiale; cf.gr. 0X00S. Le vocalisme a
degre zero est sans doute ancien dans ces formes, et l'o radical
de gr.oXoog doit etre pris a oXo£.
Sans le suffixe -wo-, on a en latin m£me solidus, avec -I- simple
(cf.osq.suluh "omninO"?) et sollus, avec -l- g^minee, ce dernier
se retrouvant largement en osque: sullus "omnes". La forme -ll- est
du type des formes expressives k gemin^es, qui est courant en italique.
La gemination se retrouve dans le nom propre Sallustius. De m§me
ga.ll. holi "tout entier". Comme la racine n'est p as dissyll abi que,
irl.slan "entier, sain et sauf" ne s'explique pas directement; comme
sanus s'associe k saluus ( salua ac sana sunt, Pl.Mer.x76), il peut
y avoir dans irl.slan une contamination.
Dans got. alis "TOXg, oXo£", etc.,il y a, sans s initial, un mot
pareil en tout a lat. sollus, gall.XoII; il y a -I- simple dans ala-
au premi er terme de composes (got. in allaim alamannam "dans tout
1 'ensemble des hommes"), ce qui rappelle lat.sollus: solidus. - M.
H.Pedersen, V.Gr.d.kelt.Spr .,1 p.411, enseigne que la forme sans
s- initial de irl.uile "tout, entier" resuite d'un passage de s- a
h- en celtique; 1'irlandais a en effet une orthographe ftwile,etle
gallois a holi et ol "tout entier". Quant a arm. olj, equivalent a
lat. saluus pour le sens, on ne saarait dire s'il y a eu un s- initial.
=== LAT 59000-59020
de cas connu oi un -d- issu de *-dh- serait reprdsentd par lat.-I-}
sinon, l f on penserait A rappeler le *swedh- du gr. eiidCa, etc. (v. sous
suSscd.
soliar: v. solium.
solidus (avec vocalisme int 4 rieur e,- soledas CIL I a 1539),-a,
-um: 1® solide, massif, plein ( solida columna, solida cornua), par
suite "ferne, rdsistant" (sens physique et moral)} subst. solidum
n."solide", t. de g 4 om 4 trie, solida traduit xa axepea} a 8 "entier,
complet ( integer, tStus), total" solida taurorum uiscera, Vg., Ae.
6 ,a$ 35 uos quibus... solidae suo stant robore uires, id., ibid.3,639,
fr 4 quent dans la 1. du droit: solidam successionem obtinere} in solidum
actid, et solidum n., e.g. Cic. Eab.Post.17,46 ita bona ueneant ut
solidum suum cuique soluatur. Ancien (Enn., Pl.), classique, usuel.
Sous Constantin, solidus, soldus (sc.nummus) a ddsignd une pibce
d r or massif dont le titre, le poids, et par suite la valeur absolue,
demeuraient invariables. Le mot dans ce sens a eu une grande fortune
dans les 1 . romanes, cf.M.L.8069, soldus, et MeiUet, BSL 66, p.84}
il est bien repr 4 sent 4 en britt.: gall .sullt, etc. L'adj. solidus
par contre n 1 est repr 4 sent 4 par des formes populaires qu'en Italie,
cf.M.L. ibid.
Derives et compos 4 s: soliditdsi solidit 4 et "totalit 4 " (class.,
```


## [2026-09-14T02:34:42.678Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB catholic\"; grep -n -i \"catholic\" WEB_vol1.txt | head -5\necho \"=== WEB holos\"; grep -n \"ho'los\\|holos\\|holo-\" WEB_vol1.txt | head -8\necho \"=== AFM/AFA جاثل\"; grep -n \"جاثل\" AFM_pages.txt AFA.txt ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -8"
}
```


### [2026-09-14T02:34:42.770Z] TOOL RESULT

```
=== WEB catholic
577:ab-bé’ (4-ba’), n. [Fr., from abba.] in a monas- tic sense, an abbot; the superior of an abbey: but more generally, a title given to Roman Catholic clergy without any determinate rank or Office.
806:ab’lē-gāte, n. in the Roman Catholic Church, a papal envoy of high rank, entrusted with important diplomatic missions; also, the en- voy who bears to a newly created cardinal his insignia of office.
831:6. in the Roman Catholic Church, a small quantity of wine and water which is used to wash the chalice and the priest’s fingers after the Communion, and which then, as contain- ing portions of the consecrated elements, is drunk by the priest.
1128:3. in the Roman Catholic and Orthodox Eastern Churches, a remission of sins, for- mally given by a priest after penance by the sinner.
1129:4. in the Roman Catholic Church, the act of absolving from excommunication or freeing a person from its penalties on his reconcilia- tion to the church.
=== WEB holos
5585:all, a. [AS. all, al; D. al, alle; W. oll; Arm. oll; Gr. holos; O.H.G. alanc, entire, complete.]
5646:Rare. P al’bane, n. the stitchwort, Alsine holostea.
16240:Biar-thol’6-mew fair, a fair at West Smith- field, England, held annually at Bartholo- mewtide from 1133 to 1855.
19617:tates. bird of ill omen; (a) a bearer of bad news; 6) an unlucky person. ird of Jove; the eagle. bird of Juno; the peacock. | bird of Minerva or bird of night; the owl. bird of paradise; (a) a beautiful bird of the enus Paradisea, native in the Orient and ‘ew Guinea. One of the better known species has the head and back part of the neck.lemon- colored, the throat emerald green, the breast black, and the wings of a chestnut color. (b) in : Australia, the lyrebird, so named by early Gaps settlers; (c) in astronomy, a small constella- tion of the southern heavens. | bird of passage; a bird that migrates at the changes of season in spring and autumn; hence, anyone who roams about constantly. bird of peace; the dove. : bird of prey; any of a number of flesh-eating birds, as the eagle, hawk, owl, vulture, etc. birds of a feather; persons having like tastes or characteristics. : : $ early. bird; one who arrives or rises early. [Colloq.] 3 3 ; man-of-war bird; a raptorial sea bird, Fre- gata aguila, with a strong hooked bill and small webbed feet. bird, v.7. to catch or shoot birds. bird’bath, n. a basinlike garden ornament for birds to bathe in. bird’bolt, n. an arrow, broad and blunt at the end, for KUDE birds by concussion, without injuring the plumage. bird cage, a cage made of wires, small sticks, or wicker, for confining birds. : bird/call, n. 1. the sound or song of a bird. 2. an imitation of this. 3. a device for imitating bird sounds. ; bird cher’ry, a European tree or shrub, Pru- 2 nus Padus, bearing small black fruit; also, the i fruit of this tree. : bird dog, any dog trained to hunt birds, as a pointer, setter, or retriever. bird duf’fér, one who alters the color or form of living or stuffed birds by artificial processes, usually with intent to deceive. bird’-eyed, a. quick-sighted; catching a glance as one goes. bird fan’ci-Er, one who is interested in birds; parnadany, one who keeps, breeds, or trains irds, especially cage birds. bird’-foot, n. bird’s-foot. bird grass, a weed of the buckwheat family, with jointed stems, narrow leaves, and spikes of tiny, greenish flowers; knotgrass. bird’house”, n. 1. a small box, often resem- bling a house, for birds to live in. 2. a building for exhibiting birds. bird’ie, n. 1.a small bird: a child’s word. 2. in golf, a score of one stroke under par for any hole. bird/i-kin, n. one of the young of a bird. bird’ing, n. the hunting of birds. bird‘let, n. a small or very young bird. bird/like, a. resembling a bird. bird/lime, n. 1. a sticky substance, usually made of the juice of holly bark or mistletoe berries, extracted by boiling. It is used to pest birds by smearing it on the twigs of a sh. _ 2. anything that ensnares or prevents “escape. bird’lime, v.t. to ensnare and capture by the use of birdlime. bird/ling, n. same as birdlet. bird louse, a parasitic wingless insect infesting birds and some mammals. bird’man, x.; pl. bird’men, 1. a person whose work deals with birds, as an ornitholo- ‘gist or taxidermist. ___ 2. an aviator. [Colloq.] bird mite, a small parasitic mite, occurring in species and mainly infesting birds. rd pep’pér, a species of Capsicum (Capsicum baccatum), a pepper g small red fruit. Pant a plant flourishing in Mexico, | bears a yellow flower suggestive of a
29412:Gr. katholikos; kata, down, completely, and holos, whole.]
32814:chol-, cholo-.
32819:chol’é-, cholo-.
32845:1. bilious; causing bilious 2. easily heey: seats anger; as, a choleric man, : 3. angry; indicating an BET; as, a choleric speech, chol’ér-i¢-ly, adv. in ae angrily, chol’Gr-i¢-ness, n. irascibility: ness, c s, n. irascibility; anger; peevish. chol’ér-i.form, a. resembling chol chol ér-ig/e-nous, a. A eee cholera. ¢- producing or generating chol’ér-ine, n. 1. a mild fo: Harr era; also, the initial diarhen latie chol. gemie cholera. Stage of epi. . the precursory sym chol/ér-oid, a. E chops cholera cho-les-ter’ic, a, pertaining to chole obtained from it; as, cholesteric aci T or chō-les’tēr-in, chö-les’tēr-ine, n ke aro i 3 u chō-les’tēr-öl, z. [from chole-, and solid, stiff; and -ol.] a crystalli ' CHOH, found EO art Ta fatty alcohol, blood, nerve tissue, and bile: some gall gats, o pure R stones cho’li-amb, ch6-li-am/bic, n. 5 choliambic; Gr. chdliambos, fare ice ghambus, charos, lame, and iambos, an ambu Tan iambic verse in poetry having as ntl Ee or last foot, 4 Paepomdeeintio cholic, a. T. cholé, bile. ini denved from the bile. ] pertaining to or cholic acid; a compound found i ; of the bile which may be h Se Be rag ota, 4 aris chöõ'’line, ‘en hol-, and -ine.] a vis iqui ptomaine, CsH1:02N, aed in ae aoe and vegetable tissues: a vitamin of the B pelt G3 ), n. [Sp. lit., sk chol’la (-ya), n. [Sp. lit., skull, head. i cactus with cylindrical stems, oe fee southwestern United States, chol’6-, [Gr. cholé, cholos, bile.) a combining form meaning bile, gall, as in chololith: also chol-, chole-. chol’/6-chrome, n. [cholo-, and Gr. chroma, color.] a bile pigment of any kind. cHoloidiie, a. pertaining to bile; as, choloidic acid. chol’6-lith, n. [cholo-, and -lith.] a gallstone. chol-6-phae’in, n. [cholo-, and Gr. phaios, dusky, gray.] same as bilirubin. chol’try, chéul’try, n. [Anglo-Ind. from Ma- layalam chawat?, an inn.] a Hindu caravan- sary for the use of travelers. chon/’dral, a. (Gr. chondros, cartilage, grain.] pertaining to cartilage; cartilaginous. chon"dri-fi-ca’tion, 7. [chondr-, and L. facere, to make.] the process of being converted into cartilage; the state of being chondrified. chon/dri-f¥, v.t.; chondrified, pt., pp.; chon- drifying, ppr. to convert into cartilage. chon/dri-f¥, v.i. to be converted into cartilage. chon/dri-gen, n. [chondr- and Gr, -genés, pro- ducing.] the substance of hyaline cartilage from which chondrin is obtained after long boiling in water. chon-drig/e-nous, a. [chondr-, and Gr. -genes, producing.] yielding chondrin. chon/drin, chon/drine, n. [Gr. chondros, cat- tilage.] a transparent substance similar to gelatin, without taste, odor, or color, ob- tained by long boiling of cartilaginous tissue with water. It is largely used as an ingredient of commercial gelatin. 5 chon/dri-6-some”, n. [from Gr. chondrion, little cartilage; and -some.] in biology, any, o various very small structures found in dif- ferent forms in the cytoplasm of cells. chon/drite, n. a meteoric stone having chon- drules in its composition. 3 chon-drit/ic, a. granular in structure; having the peculiar granular structure characteristic of the meteorites called chondrites. . chon-dri’tis, n. inflammation of cartilage Or cartilaginous tissue. 6 fe chon/dr6-, [from Gr. chondros, a grain, carti- lage.] a combining form meaning of cartilage: also, before a vowel, chondr-. chon/dro-blast, n. [chondro-, and Gr. blastos, & bud, shoot.] a cell that produces cartilage. Chon-dré-den/drén, n. [chondro-, and ae dendron, a tree.] a small genus of woody ee or high-climbing shrubs, with large leat of indigenous to Brazil and Peru., The TOO a Chondrodendron tomentosum yields pee o! Drava, a drug formerly taken for diseas the bladder. F chon’drö:dīte, n. [Gr. chondros, a. grain of wheat, cartilage.] a light yellow, brittle
=== AFM/AFA جاثل
```


## [2026-09-14T02:34:43.335Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23429,23460p' SYN.txt | cut -c1-400"
}
```


### [2026-09-14T02:34:43.395Z] TOOL RESULT

```
13.13 WHOLE
Grk. — Gdos, was Goth. alls Lith. visas (Gielas) NG dos, SASKAT POS, ON allr Lett.  viss
édaxepos Dan. hel, al ChSI]. vist Lat.  {6lus, omnis, integer Sw. hel, all SCr. cio, sau It. intero, tutto _ OE eal(l) Boh.  celzj, viechen Fr. entier, tout ME hole, al Pol. caly, wszystek Sp. entero, todo NE whole all Russ. celyj, ves’ Rum. intreg, tot Du. geheel, gansch, al Skt.  sarva-, krisna-, saka- Ir. (h)uile OHG al, ganz la-, vigva- NIr. _iomlan, go léir, ar fad MHG al, ganz Av. haurva
On the various notions involving to- tality, and their expressions, cf. Brug- mann, Ausdriicke fiir den Begriff der Totalitat, and Sapir, Totality (Language Monograph 1930). The broad distinc- tion between the collective ‘whole’ and the individualizing ‘every’, pl. ‘all’, is the most important, and even this is only partially observed in linguistic expres- sion (ef. NE all in all day a
In several cases ‘whole’ comes from an earlier attested ‘whole in body, sound, well’ (so NE whole and its cognates; NHG ganz, etc.; Lat. integer ‘intact, whole’ most commonly in body), and in these, and a few of. the other words listed, there is no confusion with ‘every; all’. In some others, ‘whole’ is clearly the more original and mainly the domi- nant sense, but with seconda
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
‘all? and, through that, in I. tevery’ (Grk. ddos only 86: G pl. dou ‘all’, and the ‘whole’ and ‘every’, ’, but later ex- . fall’). In
ups eth similar development
> the singular is used for Re a’ the plural for ‘all’ (so oe Lat. omnis, the Gme. all- Git: 7d the group Lith. visas, Chil. my Skt vigua-, etc.). All these words aah appearing also and TOK en spicuously in the list for ‘every’, pl. all’, iscussed here.
Ds. *sql-no-, etc. Walde-P. 25104. Emout-M. 891. Pedersen 1,413. Grk. dos, Hom. oddos (*6\fos) ‘shole’, NG 8dos (also ofdos) ‘whole’, but pl. do ‘all’; Lat. salvus early ‘yhole’, usually ‘safe, well, sound’, Osc. sullus, pl. ‘all’; Tr. (h)uile, W., Br. holl, Corn. oll ‘whole’, pl. ‘all’; but Nit. mostly gach wile ‘every’ (gach ‘each’), with pl. na h-uile ‘
» SKt. cvd- ‘swell’, Grk. xuéw ‘be
Pre s Lire, “ips ‘power’, etc. Walde-P.
put prob
; » aS follows: Grk. Complete, perfect, sound’, Whole’ in of KMjpos ‘lot? is simply Is) and Neg times (cf. quotations in
t. NG. Grk. dxépavos ‘un-
QUANTITY AND NUMBER
igitized by Arya Samaj Foundation Chennai and eGangotri
919 mixed’ (: xepdvvipe ‘mix’) is also ‘in- tact, perfect’, hence (blend with dios) NG pop. éddkepos, dddxepos ‘whole’.
3. Lat. tétus ‘whole’ (>Sp. todo; VLat. téttus > It. tutto, Fr. tout, Rum. tot; sg. ‘all’ = ‘whole’ and, except It., ‘every’; pl. ‘all’), prob. fr. *toweto- ‘packed full’(?), fr. the root *teu- in Skt. tu- ‘be strong’, Lat. twmére ‘swell’, etc. Walde-P. 1.707. Brugmann, Totalitat 55. Ernout-M. 1049 f. (without above etym.).
Lat. omnis ‘every’ (> It. ogni ‘every’) and also ‘whole’, pl. ‘all’, etym. dub. Ernout-M. 702f. Brugmann, Totalitit 64 ff.
Lat. integer ‘intact, whole’ (> It. intero, Fr. entier, Sp. entero, Rum. in- treg), neg. epd. of the root of tangere ‘touch’. Walde-P. 1.703. Ernout-M. 1016. Walde-H. 1.708.
4, Ir. (h)uile, W., Br. holl, above, 1.
Niv. iomlan ‘whole’ = MIr. immlan ‘full, complete’, cpd. of lan ‘full’ (13.21).
NI. léir, usually as adv. go léir with sg. ‘whole’, with pl. ‘all’ (@ go léir ‘it en- tirely, all of it’, iad go léir ‘they entirely, all of them’), Ir. colléir ‘wholly’ : W. llwyr ‘entirely, entire’. Stokes 242, Mac- bain 227 without further connection. Atkinson, Pass. and Hom. Gloss. 781 f. equates with /éir ‘visible’ as ‘visibly’ > ‘wholly’.
NIr. ar fad, lit. ‘in length’, but com- monly ‘altogether, whole’ (an scéal ar fad ‘the whole story’).
W. cyfan, cpd. of cy (= cyf-, Ir. com-, Lat. com-) and mutated form of man ‘place’. Evans, 8.v.
W. cwbl, Corn. cowal, etym. dub. Loth, RC 87.37 f. (vs. Morris Jones 310).
5. Goth. alls, ON allr, OE eall, etc., general Gmc., outside connections dub., perh. : Lith. aliat adv. ‘all-, completely’ in aliat vienas ‘every one’, aliat metai ‘every year’ (NSB), if these are not fr.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
920
Gme. Mikkola, BB 25.73 ff. Walde-P. 1.90 (but Osc. allo almost certainly not ‘tota’). Feist 40.
The general usage of this group is sg.
```


## [2026-09-14T02:34:53.659Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('WEB_vol1.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:29411])\nleaf=t[:off].count('\\f')\nprint('leaf',leaf)\nseg=t.split('\\f')[leaf]\nimport re\nprint(seg[:300].replace('\\n',' | '))\nprint('...')\ni=seg.find('katholikos')\nprint(seg[max(0,i-700):i+300])\nEOF"
}
```


### [2026-09-14T02:34:54.913Z] TOOL RESULT

```
leaf 313
pendicular | line.] of or pertaining to a cathetus. | cath’e-tér, n. (LL. catheter; Gr. kathelér, a | catheter, a plug; from kathienai, to let down, thrust in; kata, down, and hienai, to send.] in surgery, a tubular metal or rubber instru- ment inserted into the bladder, to draw off the urine, when the na
...
egative electrode.
cathode particle; an electron.
cathode rays; the stream of electrons pro- jected from the surface of a cathode: cathode rays produce X rays when they strike solids.
cathode-ray iube; a vacuum tube in which cathode rays are produced.
ca-thod/ic, a. [Gr. kathodos, going down.] per-
taining to a cathode; emanating from or hav- ing its origin in a cathode.
ca-thod/6-graph, n. [Gr. kathodos, going down,
and graphein, to write.] a picture showing the internal appearance of an opaque body, usually produced by X rays: called also a radiograph.
cat’hōle, a hole in the stern of a ome for the
passage of a hawser or cable. [Rare.
cath/6-lic, a. [L. catholicus, universal, general;
Gr. katholikos; kata, down, completely, and holos, whole.]
1. universal; general; all-inclusive.
2. liberal; not narrow-minded, partial, or bigoted; as, a catholic man; catholic principles.
3. [C-] pertaining to or affecting the Roman Catholics; as, Catholic emancipation.
4. of the universal Christian c
```


## [2026-09-14T02:35:09.467Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- FVQ falsafa/safsata\"; grep -n -i \"falsafa\\|safsat\\|jathal\\|philosoph\" FVQ_pages.txt | head -6\necho \"--- AFM فلسف/سفسط\"; grep -n \"فلسف\\|سفسط\\|جاثل\" AFM_pages.txt | head -6\necho \"--- LKT\"; grep -n -i \"katholik\\|philosoph\\|Sophist\" LKT.txt | head -6\necho \"--- KLN philosophy\"; grep -n \"^philosophy,\" KLN_1966.txt | head -3"
}
```


### [2026-09-14T02:35:09.569Z] TOOL RESULT

```
--- FVQ falsafa/safsata
12535:giving a r6sum6 of the different philosophical systemswith a refutation of the same from the Jain standpoint
12552:prevailing Philosophical Schools by .Iayaras*i : edited by
12563:mita, a Buddhist philosophical work : odited by Prof.
--- AFM فلسف/سفسط
--- LKT
141:SBKAW  =  Sitzungsberichte  der  Kais.  Akademie  der  Wissenschaften  in  Wieiu Philosophisch-historische  Glasse.    Wien.    (Nach  Bänden  zitiert.)
153:ZAkkFW  =  Heinrieh  Zimmern,  Akkadische  Fremdwörter  als  Beweis  für  baby- lonischen lüilturt  influß.  Leipzig  1915.  (Sonderdruck  aus  dem  Renunziations- progranim  der  Philosophischen  Fakultät  der  Universität  Leipzig  tür  1913/14.)
2151:N.  pr.,  berühmter  ar.  Philosoph  und  Po- lyhistor (t  1037);  bei  den  jüdischen Spaniern  Aben-Sina  genannt,  hieraus die  verlateinte  Form  Ävicenna.  Ein Baum  der  Mangrove- Vegetation,  aus  der Familie  der  Verbenaceen,  heißt  lat. Ävieennia,  frz.  avicenniee  [verwandt  mit Tectonia  grandis,  s.  hier  säg  Nr.  1766]. [Devic  DEt  51.    Lammens  Rem  32.
2569:Frucht  eines  ostindischen  Baumes,  Aver- rhoa  carambola  und  A.  bilimbi  [nach  dem ar.Philosophen  MUHAMMAD  IBN  RUSD, verlateint  Averroes  (1126/1198),  be- nannt, vgl.  Brockelmann,  Geschichte  der :ir.  Literatur.  Leipzig  1901.  S.  184/185; bilimbi  aus  mal.  halimbang  'eine  Frucht'] ; hieraus  frz.  caramboUer,  pg.  carambola (auf  den  kanarischen  Inseln  carabeli) [Constancio  Dicc  222  b].  [Devic  DEt 83.    MMM  13.
3612:1573.  Sskr.  iiirväna: 'Ausgeblasen'  wie  eine  Kerze.  In  der Philosophie  der  Buddhisten  ist  dieses Wort  der  technische  Ausdruck  für  den Zustand  geworden,  nach  dem  sie  als  die Krone  und  das  Ziel  aller  Tugenden streben:  das  Aufhören  der  sinnhchen Existenz.  Mit  dem  wachsenden  Interesse für  den  Buddhismus  i.st  der  Ausdruck in  Europa,  bes.  durch  Schopenhauer, überall  verbreitet  worden,  z.  B.  engl. nirvana,  dtsch.  Nirtvana.
--- KLN philosophy
```


## [2026-09-14T02:35:15.074Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"philosophy,  n\" KLN_1966.txt | head -3\ngrep -n \"Sophia,  \\|sophisticate,\" KLN_1966.txt | head -4\necho \"=== SKT catholic/holocaust\"; grep -n -i \"^Catholic\\|Catholic, adj\\|holocaust\" SKT.txt | head -5"
}
```


### [2026-09-14T02:35:15.167Z] TOOL RESULT

```
28541:Derivative:  philosophiz-ation,  n. philosophy,  n.  —  ME.  philosophic,  fr.  OF.  philo¬ sophic,  filosofie  (F.  philosophic),  fr.  L.philosophia, fr.  Gk.  91X0009I5,  ‘love  of  wisdom,  philoso¬ phy’,  fr.  91X600905,  ‘lover  of  wisdom,  philos¬ opher'.  See  philosopher  and  -y  (representing  Gk. -la).
35929:Sophia,  fern.  PN.  —  Fr.  Gk.  009(5,  ‘wisdom’,  fr.
35930:0096?,  ‘wise’.  See  next  word, sophism,  n.  —  ME.  sophime,  fr.  OF.  soffime,  so- phime,  sophisnte  (F.  sophisme),  fr.  L.  sophisma, fr.  Gk.  o6oL<T|xa,  from  the  stem  of  ooqj^csv,  ‘to make  wise,  instruct’,  aofpi^ecrDai,  ‘to  become wise;  to  devise,  cleverly,  play  subtle  tricks’,  fr. 009 6c,  ‘clever,  skilled,  prudent,  cunning,  learn¬ ed,  wise’,  which  is  of  uncertain  origin.  Cp.  So¬ phia,  sophist,  sophisticate,  the  first  element  in sophomore  and  the  second  element  in  panso¬
35934:sophisticate,  tr.  v.,  1)  to  render  sophistical;  2)  to falsify;  3)  to  make  artificial  or  worldly-wise; intr.  v.,  to  practice  sophistication;  n.,  a  sophis¬ ticated  person.  —  ML.  sophisticate,  pp.  of  so¬ phisticate,  ‘to  sophisticate’.  See  prec.  word  and verbal  suff.  -ate.
=== SKT catholic/holocaust
3123:Catholic.  tL.-Gk.)  L.  catkoHats  (Ter- tulliari).  —  Gk.  jcoSoAucm,  nnivei^al.  — Gk. ita9j\-ov,  adv.,  on  the  whole,  in  general.— Gk.  jtatf-,  for  «iit>t,  accoiding  to;  and 5Xow,  gen.  of  o\ot.  whole.
3144:cautariao.   (F.  •  Low  U  —  Gk^ caittcriser. ^Lovf  L.  cautcnaart.  to  scar Gk.  ifam^/KciftiK  to  sear  — Gk.  ♦nv^, a  branding-iiou.  — Gk   xttUw,  II holocaust.  (L.-Gk.)   L.  : Gca.  xxii.  8.  — Gk.  6KiiKavtrrQv,  .. burnt    whole;  ncut.  of  ^K.'.nnviTai,  Um whole. —  Gk.  t\o-f,  whole;  and  Kolt^w^ burn.
8768:Holocaust ;  see  Caustio.
```


## [2026-09-14T02:36:59.120Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:9167])\nleaf=t[:off].count('\\f')\nprint('FSF leaf of جاثلیق line:',leaf,'of',t.count('\\f')+1)\nEOF\necho \"=== SKT safe\"; grep -n -i \"^Safe\\.\\|Safe.  (F\" SKT.txt | head -3\necho \"=== SKT solid\"; grep -n -i \"Solid\\.  (F\\|^Solid\" SKT.txt | head -3\necho \"=== LAT sophisma\"; grep -n -i \"sophisma\\|sophista\\|philosophia\" LAT.txt | head -5"
}
```


### [2026-09-14T02:37:00.403Z] TOOL RESULT

```
FSF leaf of جاثلیق line: 186 of 485
=== SKT safe
16442:safe.  (F.  -  L.)  M.  E.  samf.  -  F.  sauf, safe  — L.  saluum,  ace.  of  saluut,  safe.
=== SKT solid
17759:Solid.  (F.-L.)  F.  ufidi.~t,.  seU'ifum, Bcc,  of  soliJuSy  firm.  Allied  lo  O.  Lat. Melius,  whole;  sec  Solemn.  Der.  ioliJ- ar-i-ty,  'n  word  which  we  owe  to  the  F. communists,  and  which  »ignifies  a  fellow- ship in  gain  and  loss,  a  being,  so  to  speak. all  in  ihe  same  bottom.'  Trench.  AUo solid'ify,  from  F.  soiidificr,  to  render solid.
=== LAT sophisma
12164:gr. 7 toXkTkxoC e.g. Cic.Pin.4,5, eum locum in philosophia, quem ciuilem
39171:pertinet ad mores, quos riOr} Graeci uocant, nos eam partem philosophiae
40241:generale: Cic.Diu.3,1,3, Magnus locus philosophiaeque proprius a Platone,
47348:philosophia, -ae f .:* philo sophie; philosophus,-i m. (et philo¬
56608:habitus animorum et instituta philosophiae circa disciplinam" , Ae.
```


## [2026-09-14T02:37:06.295Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:46:38.474Z] AGENT

I'll write the verification file now.


## [2026-09-14T02:58:26.551Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-464.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Sol, Solo\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *solh₂-wó-s 'whole, unharmed, intact' (adjective to the root *solh₂- 'whole'); Pokorny 979 prints it 'solo-, sol(e)u̥o- u. dgl. „wohlbehalten, ganz“', Watkins/AHD 'sol-, also solə-. Whole.'\",\n \"note\": \"Both the headword pair and the gloss are taken verbatim from Nourai's two sources: Pokorny IEW p.979 has the double headword 'solo-, sol(e)u̥o-' (hence Nourai's 'Sol, Solo', with the cross-reference entry 'Solo → see Sol' on the same page) and glosses it 'wohlbehalten, ganz' = 'safe and sound, whole'; Watkins (AHD) writes 'sol-. Also solə-. Whole. [Pok. solo- 979.]' In modern laryngealist notation the root is *solh₂-, the adjective *solh₂-wó-s (Wiktionary, s.v. ὅλος and هر). The 'Indo-European' language label, the root and the gloss are all correct. One small printing point on this page: the book prints the Latin word as 'salŭsps' — in fact 'salŭs' with a breve, salŭs — where Latin has salūs (gen. salūtis) with a long ū; the extraction is faithful to the page, the quantity mark is the book's own slip.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *solh₂- «همه، تمام، درست و بی‌گزند» و صفت مشتق از آن *solh₂-wó-s است. پوکورنی در صفحهٔ ۹۷۹ سرواژه را دوگانه «solo-, sol(e)u̥o-» آورده و معنای آن را «wohlbehalten, ganz» (تندرست، کامل) نوشته است؛ همین سبب شده که نورایی دو صورت Sol و Solo را کنار هم بگذارد. برچسب زبانی، ریشه و معنا هر سه درست است و ادعای نورایی پذیرفتنی است. تنها نکتهٔ چاپی: واژهٔ لاتین در کتاب salŭs با نشانهٔ کوتاهی آمده، در حالی که درست آن salūs است (خطای چاپی کتاب، نه خطای خوانش اسکن).\",\n \"sources\": [W + \"%E1%BD%85%CE%BB%CE%BF%CF%82\",\n             \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/solh%E2%82%82-\",\n             W + \"%D9%87%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"POK:979\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW p.979 (local POK_03.txt, form-feed leaf 221): 'solo-, sol(e)u̥o- u. dgl. „wohlbehalten, ganz“. Ai. sárva- ‚unversehrt, ganz, all, jeder‘, av. haurva-, ap. haruva- ‚unversehrt, ganz‘ (= gr. ὅλος, oὐλος, alb. gjalë, vgl. auch lat. salvus) ... WP. II 510 ff., WH. II 471 ff.' Exactly Nourai's root, page number exact.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. sol- (AHD_watkins1985.txt lines 977-979)\", \"stance\": \"supports\",\n    \"note\": \"'sol-. Also solə-. Whole. I. Basic form *sol-. 1. Suffixed form *sol-ido- in Latin solidus, solid: SOLID; CONSOLIDATE. 2. Suffixed form *sol-wo- in Greek holos, whole: HOLO-; CATHOLIC. 3. Dialectal geminated form *soll-o- ... II. Variant form *solə-. 1. ... Latin salus ... SALUBRIOUS, SALUTARY, SALUTE. 2. ... Latin salvus ... SAFE, SAGE, SALVAGE, SALVO, SAVE. [Pok. solo- 979.]' — this single entry is the skeleton of Nourai's whole chart.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 510-511 (WLD_Bd2_pages.txt lines 33881-33955)\", \"stance\": \"supports\",\n    \"note\": \"Headword 'solo-, sol(e)u̥o- u. dgl. „wohlbehalten, ganz“' with the same Indo-Iranian, Greek and Latin material; this is the page Pokorny refers to as 'WP. II 510 ff.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 13.13 WHOLE, pp. 918-919\", \"stance\": \"supports\",\n    \"note\": \"'Ds. *sql-no-, etc. Walde-P. 2.510 ... Grk. ὅλος, Hom. oὐλος (*ὅλφος) ‚whole‘ ... Lat. salvus early ‚whole‘, usually ‚safe, well, sound‘, Osc. sullus, pl. ‚all‘'; the table for 13.13 lists 'Av. haurva' and 'Skt. sarva-'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. salvus (LAT.txt lines 55210-55232)\", \"stance\": \"supports\",\n    \"note\": \"'... a.v. haurvatāt, qui y répond pour le sens, est un dérivé secondaire de haurvo-. ... Sans le suffixe -wo-, on a en latin même solidus, avec -l- simple ... et sollus, avec -l- géminée' — Latin salvus/salūs and solidus/sollus are one root with Av. haurva-.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n{\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"haurva 1; haurvatât\", \"verdict\": \"confirmed\",\n \"derivation\": \"PIE *solh₂-wó-s > Proto-Indo-Iranian *sárwas (Skt. sárva- 'whole, all, every') > Proto-Iranian *hárwa- (regular Iranian *s- > h- before a vowel) > Avestan haurva- 'unharmed, intact; entire, all', Old Persian haruva- 'all' (the Avestan spelling au before r is the usual Avestan rendering of *ar, cf. Av. pouru- : Skt. purú-). From it the feminine abstract in -tāt- (the Indo-Iranian suffix of *sarvátāti-, Gk. -της in ὁλότης): Av. haurvatāt- 'wholeness, completeness, welfare', personified as Haurvatāt, the Amaša Spənta of health who guards the waters, and always paired with Amərətat- 'immortality'. Nourai's two words and their glosses are exactly Bartholomae's.\",\n \"derivation_fa\": \"صفت هندواروپایی *solh₂-wó-s در هندوایرانی به *sárwas رسید (سنسکریت sárva-) و در ایرانی باستان با ابدال قاعده‌مند s آغازین به h به صورت *hárwa- درآمد؛ از این‌رو اوستایی haurva- «بی‌گزند، تمام، همه» و پارسی باستان haruva- (نوشتار au در اوستا همان *ar است، مانند pouru- در برابر purú- سنسکریت). از همین ستاک با پسوند اسم مجرد مؤنث -tāt- واژهٔ haurvatāt- «کمال، رسایی، به‌زیستی» ساخته شده که نام یکی از امشاسپندان و نگهبان آب‌هاست و همواره با امرداد (Amərətat-) همراه می‌آید. ادعای نورایی عین مدخل بارتولومه و درست است.\",\n \"sources\": [W + \"%D9%87%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"POK:979\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 221 (p.979): 'av. haurva-, ap. haruva- ‚unversehrt, ganz‘ ... av. haurvatät- ‚Ganzheit, Vollkommenheit, Wohlfahrt‘ (= gr. ὁλότης)' — word for word Nourai's two glosses.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. haurva-, haurvatāt- (BRT.txt lines 29628 and 29638; cols. c.1789-1792, the next page's running heads are 1795/1796)\", \"stance\": \"supports\",\n    \"note\": \"'j. (i S) haurva-, p. haruva- Adj. ‚ganz‘; 1) sva. ‚unverletzt, unversehrt, heil‘; 2) sva. ‚gesammt, vollständig‘' and 'j., g. haurvatāt-, haurvāt- f. ‚Ganzheit, Vollkommenheit, Wohlfahrt‘ ... als Gottheit, der die Sorge für die Wasser anvertraut ist'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §107 and lexicon (KNT.txt lines 607, 1346, 1412)\", \"stance\": \"supports\",\n    \"note\": \"'pIE *sel̥ḵo- ‚all‘, OP haruva-, Av. haurva-, Skt. [sarva-]' and 'OP haruva- ‚all‘, Skt. sárva-'; also 'for OP -aru- we find the following examples: haruva-, once written fra-haravam'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 13.13 WHOLE, table p. 918\", \"stance\": \"supports\",\n    \"note\": \"The comparative table for 'WHOLE' lists 'Av. haurva' beside 'Skt. sarva-' and 'Grk. ὅλος', i.e. the same equation Nourai draws.\"}\n ]\n},\n{\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"har «هر»; Xordâd «خرداد»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Av. haurva- / OP haruva- > Middle Persian har(w) (PHD: 'har(w) [KRA < Aram. ʾẔP; hl | Man. hrw, NP har] all, each, every'; the Pahlavi Zand renders Avestan haurva- by ham(ag) 'all') > New Persian هر har 'each, every', with regular loss of the final -w of the MP cluster -rw in unstressed position (cf. MP harwisp beside har). Xordād continues the abstract: Av. haurvatāt- > MP Hordād/Xordād (the Amaša Spənta and the name of the third month and of the sixth day of every month) > NP خرداد. Nourai's gloss '\\\"perfect\\\"' for Xordād is a loose rendering of Mo'in's 'کمال و رسایی' ('perfection, completeness') — the word is the abstract noun, not the adjective, which is why he puts it in quotation marks.\",\n \"derivation_fa\": \"«هر» از فارسی میانهٔ har(w)، از پارسی باستان haruva- و اوستایی haurva- است؛ واکهٔ پایانی و واو خوشه (-rw) در فارسی نو افتاده است (سنجیدنی با harwisp پهلوی). «خرداد» دنبالهٔ haurvatāt- اوستایی است که در پهلوی Hordād شده و نام امشاسپند نگهبان آب، نام ماه سوم و روز ششم هر ماه است. معین در حاشیهٔ برهان قاطع (ص ۷۲۹) همین را می‌نویسد: «هئوروتات بمعنی کمال و رسایی است»؛ پس معنای «کامل» که نورایی در گیومه آورده تقریبی است ولی نادرست نیست. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D9%87%D8%B1\", \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%AA%D9%88%D9%84%DB%8C%DA%A9/\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:729\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in, s.v. خرداد (BQT_v2_pages.txt leaf 187 = printed p.729; the running head of leaf 189 reads ۷۳۱, so printed = leaf + 542). Mo'in's footnote: 'پهلوی ... اوستا haurvatāt مرکب از دو جزو: هئوروه صفت است بمعنی رسا، همه، درست، کامل، در پارسی باستان haruva، در فارسی هر؛ جزو دوم ـتات پسوند دال براسم مجرد مؤنث؛ بنابراین هئوروتات بمعنی کمال و رسایی است' — both of Nourai's arrows (Av. → har and Av. → Xordād) on one page.\"},\n   {\"ref\": \"BQT:2318\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' s.v. هر (BQT_v4_pages.txt [pdf page 401] = printed 2318, offset +1917). Mo'in's footnote: 'پارسی باستان haruva ... اوستا haurva-، پهلوی har ... هندی باستان sarva- ... در اوستا haurva صفت است بمعنی رسا، همه، درست (تمام، کامل). در پارسی باستان haruva همان است که در فارسی «هر» شده ... و رک: خرداد (جزو اول)' — Mo'in himself cross-refers the two entries Nourai cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 43 s.v. har(w) (PHD.txt line 396)\", \"stance\": \"supports\",\n    \"note\": \"'har(w) [KRA < A ʾP; hl | M hrw, N har] all, each, every'; also 'harwisp [hlwspʾ | M hrwsp] all' and, in the English-Pahlavi part, 'each harw', 'every harw, wisp'. The Amahraspand list on p. 4384 of the file names 'Hordād' among Wahman, Ardwahišt, Šahrewar, Spandarmad, Hordād, Amurdād.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 1090, p. 244\", \"stance\": \"supports\",\n    \"note\": \"'1090. har „jeder, all“. ap. haruva- ‚all‘, fraharavam (Bartholomae, BB XIII, 69) ‚im Ganzen‘; aw. haurva-; phlv. har, har[v]sp; ai. sárva-.' — the same chain.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/هر (Persian section)\", \"stance\": \"supports\",\n    \"note\": \"'From Middle Persian (KRA), from Proto-Iranian *hárwah, from Proto-Indo-Iranian *sárwas (“whole, all, entire”), ultimately from Proto-Indo-European *solh₂-wó-s'; the determiner means 'each, every'.\"}\n ]\n},\n{\n \"id\": 3, \"lang\": \"Greek\", \"words\": \"holos; kata-holos; holo-kaustos\", \"verdict\": \"confirmed\",\n \"derivation\": \"PIE *solh₂-wó-s > pre-Greek *hólwos > Attic ὅλος hólos 'whole, entire' (Ionic/Homeric oὖλος with compensatory lengthening after the loss of digamma -φ-; initial *s- > h- is the regular Greek change). 'kata-holos' is Nourai's citation form of the adverbial phrase κατὰ ὅλου > καθόλου kath'hólou 'on the whole, in general' (elision of κατά before the rough breathing gives the aspirated θ), from which the adjective καθολικός is built. ὁλόκαυστος / ὁλόκαυστον 'wholly burnt (offering)' = hólos + the verbal adjective of καίειν 'to burn' (Nourai's cross-reference '☞ Kŭ 1' points to his root for that verb); it is the Septuagint's word for the whole burnt sacrifice.\",\n \"derivation_fa\": \"در یونانی *solh₂-wó-s به *hólwos و سپس به ὅλος (hólos) «همه، تمام» رسیده است؛ s آغازین هندواروپایی به دمش (h) بدل شده و دیگامای میانی افتاده است (صورت ایونی oὖλος با کشش جبرانی). صورت «kata-holos» در نمودار، همان ترکیب قیدی κατὰ ὅλου > καθόλου «روی هم رفته، به‌طور کلی» است که در آن کاف پیش از دمش به ث (θ) بدل شده است. ὁλόκαυστος «سراسر سوخته» نیز از holos و صفت مفعولی καίειν «سوزاندن» ساخته شده و اصطلاح ترجمهٔ سبعینیه برای قربانی تمام‌سوخته است. ادعای نورایی درست است.\",\n \"sources\": [W + \"%E1%BD%85%CE%BB%CE%BF%CF%82\", \"https://www.etymonline.com/word/catholic\"],\n \"ref_check\": [\n   {\"ref\": \"POK:979\", \"status\": \"supports\",\n    \"note\": \"POK p.979: 'gr. att. ὅλος, ion. oὖλος (*ὅλφος) ‚vollständig, ganz‘' (POK_03.txt leaf 221).\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. sol-: '2. Suffixed form *sol-wo- in Greek holos, whole: HOLO-; CATHOLIC.'\"},\n   {\"ref\": \"WEB:286\", \"status\": \"supports\",\n    \"note\": \"Webster's New Twentieth Century, 2nd ed., s.v. cath'o-lic (WEB_vol1.txt leaf 313): '[L. catholicus, universal, general; Gr. katholikos; kata, down, completely, and holos, whole.]' — the content is exactly what the arrow claims; the printed page number could not be confirmed because the OCR of this scan carries no page numerals, but 'catholic' falls in the right part of the volume for p. 286.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. catholic (KLN_1966.txt line 6814)\", \"stance\": \"supports\",\n    \"note\": \"'... fr. Gk. καθολικός, ‚general, universal‘, fr. καθόλου = καθ’ ὅλου, ‚on the whole, in general‘, fr. κατά, ‚according to‘ ... and ὅλος, ‚whole‘, which stands for *ὅλφος, fr. I.-E. base *sol-wos, whence also L. salvus'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Catholic and Holocaust (SKT.txt lines 3123, 3144)\", \"stance\": \"supports\",\n    \"note\": \"'Catholic. (L.-Gk.) L. catholicus (Tertullian). — Gk. καθολικός, universal. — Gk. καθόλου, adv., on the whole, in general. — Gk. καθ-, for κατά, according to; and ὅλου, gen. of ὅλος, whole' and 'holocaust ... Gk. ὁλόκαυστον, burnt whole ... ὅλος, whole; and καίω, burn'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 13.13, p. 919\", \"stance\": \"supports\",\n    \"note\": \"'Grk. ὅλος, Hom. oὖλος (*ὅλφος) ‚whole‘, NG ὅλος ... but pl. ὅλοι ‚all‘.'\"}\n ]\n},\n{\n \"id\": 4, \"lang\": \"Greek\", \"words\": \"katholicos\", \"verdict\": \"plausible\",\n \"derivation\": \"Greek καθολικός katholikós 'general, universal' is a normal -ικός adjective to καθόλου (Aristotle already uses it of 'general' propositions). The derivation from node #3 is exact. What is loose is the gloss and the spelling: the word does not mean 'the whole undivided church of Christ' — that is the later ecclesiastical application of it in the phrase ἡ καθολικὴ ἐκκλησία 'the universal church', first in Ignatius of Antioch, Smyrn. 8.2 (c. 110 CE) and standard from the Nicene creed on; and 'katholicos' with Latin c- is the Latinized transliteration (Gk. κ = k), the form that also happens to be the English title 'Catholicos' for the eastern primate. Hence 'plausible': the arrow is right, the gloss anticipates a meaning the Greek adjective acquired only in Christian use.\",\n \"derivation_fa\": \"καθολικός صفتی است با پسوند -ικός از καθόλου، به معنای «کلی، همگانی»؛ ارسطو آن را در منطق برای قضایای کلی به کار برده است. پیوند آن با گره پیشین درست است، اما معنایی که نورایی می‌دهد («کلیسای یکپارچهٔ مسیح») معنای خود واژه نیست بلکه کاربرد کلیسایی آن در ترکیب «کلیسای جامع» است که نخست در نامهٔ ایگناتیوس انطاکی (حدود ۱۱۰ م.) دیده می‌شود. نگارش با c نیز لاتینی‌شدهٔ حرف کاپای یونانی است. بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/catholic\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. sol-, branch 'Greek holos, whole: HOLO-; CATHOLIC' — AHD derives CATHOLIC from holos exactly as drawn; it does not comment on the ecclesiastical sense.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. catholic and catholicon (KLN_1966.txt lines 6814, 6818)\", \"stance\": \"supports\",\n    \"note\": \"'Gk. καθολικός, ‚general, universal‘' — Klein's gloss is 'general, universal', not 'church'.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's 2nd ed. s.v. catholic (WEB_vol1.txt leaf 313)\", \"stance\": \"supports\",\n    \"note\": \"'Gr. katholikos; kata, down, completely, and holos, whole. 1. universal; general; all-inclusive ... 4. of the universal Christian church' — the church sense is listed as a secondary, later sense.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Catholic (SKT.txt line 3123)\", \"stance\": \"supports\",\n    \"note\": \"'L. catholicus (Tertullian) — Gk. καθολικός, universal' — the Christian use dates from Tertullian/Ignatius, i.e. it is an application, not the lexical meaning.\"}\n ]\n},\n{\n \"id\": 5, \"lang\": \"French\", \"words\": \"catholique\", \"verdict\": \"confirmed\",\n \"derivation\": \"Greek καθολικός was taken into Ecclesiastical Latin as catholicus (Tertullian, c. 200 CE, then the creeds), and Latin catholicus gave Old French catholique (13th c.), which is the immediate source both of Middle English catholik (mid-14c.) and — much later — of Persian کاتولیک. The chart's Greek → French arrow silently passes through Church Latin; that is the only inexactness, and Nourai's own AHD reference shows the same shortcut.\",\n \"derivation_fa\": \"واژهٔ یونانی καθολικός از راه لاتین کلیسایی (catholicus، نزد ترتولیان در حدود ۲۰۰ م.) به فرانسهٔ قدیم catholique (سدهٔ ۱۳ م.) راه یافت و همین صورت فرانسوی منبع مستقیم انگلیسی Catholic و سپس فارسی «کاتولیک» است. تنها نکته آن که نمودار حلقهٔ لاتین را نیاورده است؛ در مجموع ادعا درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/catholic\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins's sol- entry gives only 'Greek holos ... CATHOLIC' and names no French or Latin relay; the French link itself comes from the standard dictionaries (Klein, Etymonline), not from AHD.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. catholic (KLN_1966.txt line 6814)\", \"stance\": \"supports\",\n    \"note\": \"'catholic, adj. — F. catholique, fr. Eccles. L. catholicus, fr. Gk. καθολικός' — exactly the chain Greek > Latin > French.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/catholic\", \"stance\": \"supports\",\n    \"note\": \"'mid-14c., from Old French catholique, from Church Latin catholicus “universal, general,” from Greek katholikos, from phrase kath’ holou “on the whole, in general”'; Protestant use of capitalized 'Catholic' for Rome from c. 1554.\"}\n ]\n},\n{\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"kâtolîk «کاتولیک»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Persian کاتولیک kātolīk is a modern (19th-20th c.) loan from French catholique, taken in with the wave of French vocabulary that entered Persian through the Dār al-Fonūn and the press; Mo'in tags the entry '[فر.]' = French. The French -que was dropped and the stress-final -ik retained, giving kātolīk, not *kātolīkī. It is thus a doublet of the far older جاثلیق (node #9), which reached Persian from the same Greek word by the Syriac-Arabic route a thousand years earlier; Nourai's gloss '\\\"general\\\"' renders the etymological, not the current, sense.\",\n \"derivation_fa\": \"«کاتولیک» وام‌واژه‌ای نو است از فرانسهٔ catholique که در سدهٔ سیزدهم و چهاردهم هجری از راه دارالفنون و مطبوعات وارد فارسی شده است؛ معین نیز مدخل را با نشانهٔ [فر.] آورده است. این واژه دوگانهٔ (doublet) «جاثلیق» است که همان کلمهٔ یونانی را هزار سال پیش‌تر از راه سریانی و عربی به فارسی رسانده بود. معنای «عام، کلی» که نورایی در گیومه آورده معنای ریشه‌ای است نه معنای امروزی آن. ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%AA%D9%88%D9%84%DB%8C%DA%A9/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2783\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Fārsi s.v. کاتولیک (text read on abadis.ir/fatofa/کاتولیک, section فرهنگ معین): '(تُ) [فر.] (اِ.) دارای مذهب کاتولیک، کسانی از پیروان مسیح که به پاپ عقیده دارند و از او اطاعت می‌کنند'. The tag [فر.] = French is precisely Nourai's arrow. The printed page 2783 itself cannot be checked: no scan of the 6-volume Mo'in is online (refs_online.json, MON notes).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"vajehyab/abadis text of Mo'in s.v. کاتولیک\", \"stance\": \"supports\",\n    \"note\": \"Origin tag '[فر.]' (French) on the entry.\"},\n   {\"src\": \"DKH\", \"where\": \"Dehkhoda s.v. کاتولیک (via abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"Dehkhoda traces the word to Greek 'katholikos' 'universal and comprehensive', originally the title of the head of the bishops, now 'a Christian denomination that recognises the Pope' — i.e. the same Greek etymon Nourai gives, with the French form as the modern vehicle.\"}\n ]\n},\n{\n \"id\": 7, \"lang\": \"English\", \"words\": \"Catholic\", \"verdict\": \"confirmed\",\n \"derivation\": \"Middle English catholik (mid-14c., 'of the ancient undivided Church') from Old French catholique and Church Latin catholicus; the general sense 'embracing all, universal' is attested from the 1550s, and the capitalised 'Catholic' for the Church of Rome from c. 1554, after the Reformation made the label contested. Old English had rendered Latin catholicus by the calque eallgeleaflic 'all-believing'.\",\n \"derivation_fa\": \"انگلیسی Catholic از فرانسهٔ قدیم catholique و لاتین کلیسایی catholicus است و نخست در میانهٔ سدهٔ ۱۴ م. به معنای «مربوط به کلیسای کهن و یکپارچه» به کار رفته؛ معنای عام «همگانی» از دههٔ ۱۵۵۰ و کاربرد آن برای کلیسای روم از حدود ۱۵۵۴ م. رواج یافته است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/catholic\"],\n \"ref_check\": [\n   {\"ref\": \"none\", \"status\": \"not_checked\",\n    \"note\": \"The chart gives no reference for this node (refs=None); the chain is covered by the AHD citation of its parent.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. catholic (KLN_1966.txt line 6814)\", \"stance\": \"supports\",\n    \"note\": \"'catholic, adj. — F. catholique, fr. Eccles. L. catholicus' — English directly from French, as drawn.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/catholic\", \"stance\": \"supports\",\n    \"note\": \"'mid-14c., catholik, “of the doctrines of the ancient Church”, literally “universally accepted”, from French catholique ... 1550s “embracing all, universal”; c. 1554 Protestants began applying the capitalized form to the Church in Rome'.\"}\n ]\n},\n{\n \"id\": 8, \"lang\": \"Arabic\", \"words\": \"jâselîq\", \"verdict\": \"plausible\",\n \"derivation\": \"Arabic جاثليق jāṭalīq / jāthalīq is indeed Greek καθολικός, but not taken straight from Greek: it came through Syriac ܩܛܘܘܠܝܩܐ qāthōlīqā / gāthōlīqā, the title of the primate of the Church of the East resident at Seleucia-Ctesiphon in the Sasanian empire, which is why the Arabic word means not 'universal' in the abstract but 'catholicos, head of the Nestorian (and Armenian) church' — the sense Nourai's own gloss gives second. The Greek/Syriac θ/ṯ is kept as Arabic ث, the initial κ appears as ج (through the Syriac g-/q- variant), and the ending -ικός is fitted to the Arabic pattern fāʿalīl. Two smaller points make this 'plausible' rather than 'confirmed': the transliteration 'jâselîq' with s is the Persian reading of ث, not the Arabic one (jāthalīq), and the Syriac stage is missing from the chart.\",\n \"derivation_fa\": \"«جاثلیق» در عربی معرّب καθολικός یونانی است، اما نه مستقیم، بلکه از راه سریانی qāthōlīqā که لقب پیشوای کلیسای شرق در تیسفون بوده است؛ به همین سبب معنای عربی آن نه «عام» بلکه «مقدّم الأساقفه» است. ثای عربی برابر θ یونانی، جیم برابر کاپا (از راه گونهٔ سریانی g-) و پایانه بر وزن فاعلیل قالب گرفته است. دو نکته سبب می‌شود حکم را «با احتیاط پذیرفتنی» بدانیم: آوانگاری jâselîq خوانش فارسی ث است نه عربی، و حلقهٔ سریانی در نمودار نیامده است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D8%AC%D8%A7%D8%AB%D9%84%DB%8C%D9%82/\"],\n \"ref_check\": [\n   {\"ref\": \"TAD:19\", \"status\": \"supports\",\n    \"note\": \"al-Unaysi, Tafsīr al-alfāẓ al-dākhila, s.v. جاثليق (TAD_pages.txt leaf 22, printed ≈ p.18-19): 'جاثليق - يوناني [καθολικός] معناه عام وجامع ويراد به في الكنيسة مقدّام الأساقفة' — word for word Nourai's gloss 'universal, a rank in the Catholic church'. The page number matches within the volume's ±1 leaf offset.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON/DKH\", \"where\": \"Mo'in and Dehkhoda s.v. جاثلیق (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"Mo'in: '(ثِ) [معر.] (اِ.) پیشوای ترسایان'; the Dānešnāme section states 'واژه جاثلیق از کلمه کاتولیک گرفته شده است'.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an (FVQ_pages.txt, grep 'jathal', 'falsafa')\", \"stance\": \"silent\",\n    \"note\": \"No entry — the word is not Qur'anic, so Jeffery has nothing on it.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba (AFM_pages.txt, grep 'جاثل')\", \"stance\": \"silent\",\n    \"note\": \"No entry; Addi Shir covers Persian words arabicised, and jāthalīq is Greek/Syriac, not Persian, so its absence is itself consistent with the Greek origin.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch (LKT.txt, grep 'katholik')\", \"stance\": \"silent\",\n    \"note\": \"No entry — Lokotsch registers oriental words that entered European languages, not the reverse direction.\"}\n ]\n},\n{\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"jâselîq «جاثلیق»\", \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian جاثلیق jāselīq (Persian reads the Arabic ث as s) is the Arabic word of node #8 taken over whole, with the Arabic broken plural جاثلیقان also formed with the Persian plural -ان in Ferdowsi's line quoted on the chart, 'ز بطریق وز جاثلیقان شهر / هر آنکس کش از مردمی بود بهر' — it stands there beside بطریق (patriarch, Gk. πατριάρχης), i.e. in the Shahnameh's list of Christian dignitaries. Since the Catholicos of the Church of the East sat at Ctesiphon under the Sasanians, the word was at home in Persian by the 10th century; it means 'primate of the Christians', exactly Nourai's 'a Catholic rank'.\",\n \"derivation_fa\": \"«جاثلیق» در فارسی وام‌واژه‌ای عربی است (و ث آن در فارسی s خوانده می‌شود) که از سدهٔ چهارم هجری در متون فارسی دیده می‌شود؛ فردوسی آن را با جمع فارسی ـان به کار برده است: «ز بطریق وز جاثلیقان شهر». نوشین در واژه‌نامک می‌نویسد: «جاثلیق (تازی. معرب کاتولیک) پیشوای ترسایان، مسیحیان». از آنجا که جاثلیق کلیسای شرق در تیسفون می‌نشست، این لقب در ایران ساسانی و پس از آن آشنا بوده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D8%AC%D8%A7%D8%AB%D9%84%DB%8C%D9%82/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1199\", \"status\": \"supports\",\n    \"note\": \"Mo'in s.v. جاثلیق (text on abadis.ir/fatofa/جاثلیق, فرهنگ معین): '(ثِ) [معر.] (اِ.) پیشوای ترسایان' — tagged معرّب (arabicised), matching Nourai's Arabic → Persian arrow. The printed page cannot be verified (no scan of the 6-vol Mo'in online).\"},\n   {\"ref\": \"FSF:141\", \"status\": \"supports\",\n    \"note\": \"Noushin, Vāženamak s.v. جاثلیق (FSF_pages.txt, form-feed leaf 186 of 485): 'جاثلیق (تازی. معرب کاتولیک) پیشوای ترسایان. مسیحیان: ز بطریق وز جاثلیقان شهر / هر آنکس کش از مردمی بود بهر' — the source of both Nourai's gloss and his Ferdowsi quotation. With the scan's ~45 leaves of front matter, leaf 186 corresponds to printed p. 141, i.e. Nourai's number.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FSF\", \"where\": \"Vāženamak, leaf 186\", \"stance\": \"supports\",\n    \"note\": \"'جاثلیق (تازی. معرب کاتولیک)' with the Shahnameh line — an independent Persian source for the same derivation.\"},\n   {\"src\": \"DKH\", \"where\": \"Dehkhoda s.v. جاثلیق (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"'قاضی ترسایان ... معرب'; the Persian free encyclopaedia section adds 'واژه جاثلیق از کلمه کاتولیک گرفته شده است'.\"}\n ]\n},\n{\n \"id\": 10, \"lang\": \"English\", \"words\": \"holograph, hologram, holocaust\", \"verdict\": \"confirmed\",\n \"derivation\": \"All three are learned holo- compounds of Greek ὅλος. holocaust: Gk. ὁλόκαυστον (the Septuagint's word for the whole burnt offering, e.g. Gen. 22:8) > Latin holocaustum > Old French holocauste > Middle English (13c.) 'burnt offering'; the sense 'wholesale slaughter' is 17c., 'mass slaughter by fire' 1833, and the Nazi genocide sense only from 1957. holograph: Late Latin holographus (Gk. ὁλόγραφος 'written entirely by the same hand'), a term of Roman-law testament practice, in English from the 17c. hologram is the youngest: coined in 1948-49 by Dennis Gabor from holo- + -gram, on the model of telegram, for a recording of the whole wavefront.\",\n \"derivation_fa\": \"هر سه واژه ساخته‌های علمی با پیشوند holo- (از ὅλος یونانی) هستند. holocaust از ὁλόκαυστον (اصطلاح ترجمهٔ سبعینیه برای قربانی تمام‌سوخته) از راه لاتین holocaustum و فرانسهٔ قدیم به انگلیسی رسیده و معنای «کشتار یهودیان» آن تنها از ۱۹۵۷ رواج یافته است؛ holograph از ὁλόγραφος «یکسره به خط خود نوشته»؛ و hologram واژه‌ای نو است که دنیس گابور در ۱۹۴۸–۱۹۴۹ از holo- و -gram ساخت. ادعای نورایی درست است.\",\n \"sources\": [W + \"%E1%BD%85%CE%BB%CE%BF%CF%82\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins s.v. sol- lists the English outcomes of Greek holos as 'HOLO-; CATHOLIC' — the combining form covers holograph/hologram/holocaust, but the three words are not named individually in the root entry (holocaust's second element is filed under the root for Gk. kaiein).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. holocaust, holograph (KLN_1966.txt line 17952)\", \"stance\": \"supports\",\n    \"note\": \"'holocaust ... F. holocauste, fr. L. holocaustum, fr. Gk. ὁλόκαυστον, lit. ‚a thing wholly burnt‘ ... compounded of ὅλος, ‚whole‘, and καυστός, verbal adj. of καίειν, ‚to burn‘'; 'holograph ... Late L. holographus ... fr. Gk. ὁλόγραφος, ‚written in full, written entirely by the same hand‘'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. holocaust (SKT.txt lines 3144, 8768)\", \"stance\": \"supports\",\n    \"note\": \"'holocaust. (L.-Gk.) ... Gen. xxii. 8. — Gk. ὁλόκαυστον, burnt whole ... ὅλος, whole; and καίω, burn' — note the Septuagint reference.\"}\n ]\n},\n{\n \"id\": 11, \"lang\": \"Latin\", \"words\": \"solidus; salŭs; salvus\", \"verdict\": \"confirmed\",\n \"derivation\": \"Three Latin continuations of the same root, in different grades and suffixes, exactly as Watkins sets them out: (a) *sol-ido- > solidus 'dense, firm, whole' (the older spelling soledus is attested in CIL I² 1539), beside the geminated Italic *sol-no- > Old Latin sollus 'whole' (Oscan sullus 'omnes'); (b) the laryngeal variant *solh₂-u- (Watkins's *solə-) in zero grade *sḷ-u- > *sal-u- giving salūs, gen. salūtis 'sound condition, welfare, greeting'; (c) *sḷh₂-wo- > *salawo- > salvus 'safe, sound', matching Oscan salavs, Umbrian saluvom and pointing to the same *-wo- suffix as Greek ὅλος and Avestan haurva-. Ernout-Meillet add that Avestan haurvatāt- is the semantic counterpart of salūs. The book prints 'salŭs' with a breve; the Latin is salūs with long ū.\",\n \"derivation_fa\": \"سه واژهٔ لاتینی از یک ریشه و با سه ساخت گوناگون‌اند: solidus از *sol-ido- (گونهٔ کهن soledus)، در کنار sollus لاتین کهن از *sol-no-؛ salūs از گونهٔ صفر *sḷ-u- > *salu-؛ و salvus از *sḷh₂-wo- > *salawo- که همان پسوند *-wo- را دارد که در ὅλος یونانی و haurva- اوستایی دیده می‌شود (مقایسه با اسکی salavs و اومبریایی saluvom). ارنو‌مییه می‌افزاید که haurvatāt اوستایی از نظر معنا برابر salūs است. ادعای نورایی درست است؛ تنها نشانهٔ کمیت در salŭs چاپ کتاب نادرست است (درست: salūs).\",\n \"sources\": [W + \"%E1%BD%85%CE%BB%CE%BF%CF%82\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. sol-: 'I.1. Suffixed form *sol-ido- in Latin solidus, solid ... II. Variant form *solə-. 1. Suffixed zero-grade form *sḷ-u- giving *sal-u- in Latin salus, health, a whole or sound condition ... 2. Suffixed form *sḷə-wo- giving *sala-wo- in Latin salvus, whole, safe, healthy, uninjured.' All three of Nourai's Latin words, in this order.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. salvus and solidus (LAT.txt lines 55210-55232, 59004-59019)\", \"stance\": \"supports\",\n    \"note\": \"'Sans le suffixe -wo-, on a en latin même solidus, avec -l- simple ... et sollus, avec -l- géminée ... la gemination se retrouve dans le nom propre Sallustius'; and on solidus: 'solide, massif, plein ... Sous Constantin, solidus, soldus (sc. nummus) a désigné une pièce d'or massif'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. safe (KLN_1966.txt line 33472)\", \"stance\": \"supports\",\n    \"note\": \"'L. salvus ... which is rel. to salus, ‚sound condition, welfare, well-being, health, safety‘, salubris ..., solidus, soldus, ‚firm, compact‘, OL. sollus, ‚whole, entire‘, and cognate with OI. sarvah ..., Avestic haurva-, ..., Gk. ὅλος (for *ὅλφος), ‚whole‘' — Klein groups exactly Nourai's three Latin words with the Avestan and Greek ones.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde-Hofmann, local OCR LEW_1910.txt (grep 'solidus|sollus|salvus')\", \"stance\": \"silent\",\n    \"note\": \"The local OCR of Walde's Lateinisches etymologisches Wörterbuch returns no hit for these headwords (the s- fascicle is missing/illegible in this scan), so it could not be used; Pokorny's reference 'WH. II 471 ff., 555 ff.' points to the relevant pages.\"}\n ]\n},\n{\n \"id\": 12, \"lang\": \"English\", \"words\": \"solid; salute; safe, save, salvation\", \"verdict\": \"confirmed\",\n \"derivation\": \"solid: Old French solide from Latin solidus, in English from the late 14c. (and the coin solidus gives also soldier, solder, sou). salute: directly from Latin salūtāre 'to greet', from salūs 'welfare, a wish for someone's welfare', in English from the 14c. safe: Middle English sauf from Old French sauf < Latin salvus. save: Old French salver/sauver < Late Latin salvāre 'to make safe', a Christian-Latin coinage on salvus. salvation: Old French salvacion < Late Latin salvātiōnem, the Church's rendering of Greek sōtēría. All five thus continue node #11 through Old French, and Nourai's grouping is correct.\",\n \"derivation_fa\": \"solid از راه فرانسهٔ قدیم از solidus لاتین؛ salute از salūtāre «درود گفتن» (از salūs)؛ safe از فرانسهٔ قدیم sauf از salvus؛ save از salver فرانسهٔ قدیم از salvāre لاتین متأخر؛ و salvation از salvātiōnem که در لاتین کلیسایی برابر σωτηρία یونانی ساخته شد. همهٔ این واژه‌ها از راه فرانسهٔ قدیم به انگلیسی رسیده‌اند و دسته‌بندی نورایی درست است.\",\n \"sources\": [W + \"%E1%BD%85%CE%BB%CE%BF%CF%82\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. sol- lists precisely these English words: 'SOLID; CONSOLIDATE ... SALUBRIOUS, SALUTARY, SALUTE ... SAFE, SAGE², SALVAGE, SALVO¹, SAVE¹, SAVE².'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. safe, salute, salvage (KLN_1966.txt lines 33472, 33587, 33590)\", \"stance\": \"supports\",\n    \"note\": \"'safe, adj. — ME. sauf, saf, fr. OF. salf, sauf (F. sauf), fr. L. salvus'; 'salute, tr. and intr. v. — ME. saluten, fr. L. salutare, ‚to greet‘, fr. salus, gen. salutis'; 'salvage ... fr. salver (F. sauver), ‚to save‘, fr. L. salvare, fr. salvus'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. safe and Solid (SKT.txt lines 16442, 17759)\", \"stance\": \"supports\",\n    \"note\": \"'safe. (F. - L.) M. E. sauf. — F. sauf, safe — L. saluum, acc. of saluus, safe.'; 'Solid. (F.-L.) F. solide, [L.] solidum, acc. of solidus, firm. Allied to O. Lat. sollus, whole; see Solemn.'\"}\n ]\n}\n]\n\ne2 = {\n \"entry\": 2,\n \"root\": \"Sophos\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Ancient Greek σοφός sophós 'skilled in a craft, clever, wise' — a Greek word with no accepted Indo-European etymology\",\n \"note\": \"The root box is right as far as it goes: σοφός is a real Greek adjective, first of practical skill (Homer's σοφίη of a carpenter, Il. 15.412) and then of wisdom generally, and Nourai correctly labels the box 'Greek' rather than 'Indo-European' — there is no PIE root behind it. Klein says outright that σοφός 'is of uncertain origin'; Beekes classes it as Pre-Greek, and Watkins's Indo-European appendix has no entry for it (grep for 'sophos' in AHD_watkins1985.txt returns nothing), which is consistent: Nourai's 'AHD:1232' must be a page of the main dictionary of the 1975/76 New College Edition (s.v. sophism/sophist), not of the roots appendix at pp. 1505-1550. Note also that the English node further down cites 'AHD:1332' for the same block of words; since sophist/sophism occupy one page of the dictionary, one of the two numbers (most likely 1332) is a misprint in the book.\",\n \"note_fa\": \"سرواژهٔ این نمودار واژه‌ای یونانی است: σοφός «چیره‌دست، دانا» که نخست دربارهٔ مهارت عملی به کار می‌رفت و سپس معنای حکمت گرفت. نکتهٔ مهم آنکه این واژه ریشهٔ هندواروپایی شناخته‌ای ندارد؛ کلاین می‌نویسد «of uncertain origin» و بیکس آن را پیشایونانی (Pre-Greek) می‌داند؛ پیوست ریشه‌های واتکینز نیز مدخلی برای آن ندارد. پس برچسب «یونانی» درست است و ارجاع AHD:1232 باید به متن اصلی فرهنگ آمریکن هریتیج باشد نه پیوست ریشه‌ها. ادعای نورایی دربارهٔ خود واژه درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/sophomore\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1232\", \"status\": \"not_checked\",\n    \"note\": \"Nourai's page refers to the 1975/76 AHD New College Edition, which is not open online (only lending copies; see refs_online.json s.v. AHD). The local proxy, Watkins 1985 'The American Heritage Dictionary of Indo-European Roots', has no entry for sophos — as expected, since the word has no IE root; so the citation cannot be to the roots appendix.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. sophism (KLN_1966.txt line 35930)\", \"stance\": \"partial\",\n    \"note\": \"'fr. σοφός, ‚clever, skilled, prudent, cunning, learned, wise‘, which is of uncertain origin' — confirms the Greek word and its meaning, but denies it an established etymology, which Nourai's root box does not claim either.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, whole file (grep 'sophos')\", \"stance\": \"silent\",\n    \"note\": \"No root entry for sophos anywhere in the IE-roots appendix.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/sophomore (with the linked sophism entry)\", \"stance\": \"supports\",\n    \"note\": \"'Greek sophistes “a master of one's craft; a wise or prudent man”', 'Greek sophos (wise)' — same meaning range as Nourai's gloss 'skilled, wise'.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"] = [\n{\n \"id\": 1, \"lang\": \"Greek\", \"words\": \"sophisma; philo-sophos\", \"verdict\": \"confirmed\",\n \"derivation\": \"σόφισμα sóphisma is the -μα noun of σοφίζεσθαι 'to be clever, devise cleverly', denominative of σοφός; its first sense is 'clever device, acquired skill' (Pindar, Herodotus) and only with the fifth-century σοφισταί and Plato's and Aristotle's polemic does it settle into 'captious argument, fallacy' — Aristotle's Σοφιστικοὶ ἔλεγχοι is the text that fixes the pejorative meaning, and that is why Nourai glosses it 'a skilled but false reasoning'. φιλόσοφος is a compound of φίλος 'loving' (Nourai's cross-reference '☞ Bhili') + σοφός, 'lover of wisdom', with its abstract φιλοσοφία; both are the direct source of the Arabic and European words below.\",\n \"derivation_fa\": \"σόφισμα اسم مصدری با پسوند -μα از فعل σοφίζεσθαι «زیرکی کردن، تدبیر ساختن» است که خود از σοφός ساخته شده؛ معنای نخستین آن «تدبیر زیرکانه، مهارت» بوده و معنای «مغالطه» را پس از سوفسطاییان و نقد افلاطون و ارسطو (رسالهٔ سوفسطایی) گرفته است. φιλόσοφος نیز مرکب است از φίλος «دوستدار» و σοφός، با اسم مصدر φιλοσοφία، و همین دو سرچشمهٔ مستقیم واژه‌های عربی و اروپایی بعدی‌اند. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/sophomore\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1232\", \"status\": \"not_checked\",\n    \"note\": \"Same as for the root: the 1975/76 New College Edition is not online, and the Watkins roots appendix (the part of AHD that is available) has no sophos entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. sophism (KLN_1966.txt line 35930)\", \"stance\": \"supports\",\n    \"note\": \"'fr. Gk. σόφισμα, from the stem of σοφίζειν, ‚to make wise, instruct‘, σοφίζεσθαι, ‚to become wise; to devise cleverly, play subtle tricks‘, fr. σοφός'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. philosophy (KLN_1966.txt line 28541)\", \"stance\": \"supports\",\n    \"note\": \"'fr. Gk. φιλοσοφία, ‚love of wisdom, philosophy‘, fr. φιλόσοφος, ‚lover of wisdom, philosopher‘' — Nourai's 'philo-sophos: fond of wisdom' exactly.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. philosophia (LAT.txt line 47348)\", \"stance\": \"supports\",\n    \"note\": \"'philosophia, -ae f.: philosophie; philosophus, -i m.' — listed among the Greek borrowings of Latin, the relay used by node #4.\"}\n ]\n},\n{\n \"id\": 2, \"lang\": \"Arabic\", \"words\": \"safsatah; falsafah\", \"verdict\": \"plausible\",\n \"derivation\": \"Both are Greek words arabicised during the 8th-10th c. translation movement, mostly through Syriac intermediaries (Ḥunayn b. Isḥāq and his school). فلسفة falsafa 'philosophy' is φιλοσοφία reshaped into a quadriliteral verbal noun: the loan فيلسوف faylasūf (φιλόσοφος, pl. فلاسفة falāsifa) yielded a root f-l-s-f with the verb فَلْسَفَ and its maṣdar falsafa on the pattern faʿlala. سفسطة safsaṭa 'sophistry' is the same operation on a root s-f-s-ṭ; here, however, the sources point to σοφιστής (Arabic سوفسطائي sūfisṭāʾī, the regular Arabic name of the sophists) rather than to σόφισμα as the immediate model — Wiktionary derives safsaṭa from safsaṭāʾī, not from sophisma. That is the one soft point in the node; the Greek origin and the meanings are certain, so 'plausible'.\",\n \"derivation_fa\": \"هر دو واژه معرّب یونانی‌اند و در دوران نهضت ترجمه (سدهٔ دوم تا چهارم هجری) بیشتر از راه سریانی وارد عربی شدند. «فلسفه» از φιλοσοφία است؛ نخست «فیلسوف» (φιλόσοφος، جمع مکسر فلاسفه) وام گرفته شد و از آن ریشهٔ رباعی ف‌ل‌س‌ف با فعل فَلْسَفَ و مصدر فَلْسَفَة بر وزن فَعْلَلَة ساخته شد. «سفسطه» نیز همین فرایند را با ریشهٔ س‌ف‌س‌ط طی کرده است، اما منبع مستقیم آن به گفتهٔ منابع امروزی σοφιστής («سوفسطائی») است نه σόφισμα. پس ادعای نورایی در اصل درست و در جزئیات با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D9%81%D9%84%D8%B3%D9%81%D8%A9\", W + \"%D8%B3%D9%81%D8%B3%D8%B7%D8%A9\"],\n \"ref_check\": [\n   {\"ref\": \"TAD:35\", \"status\": \"supports\",\n    \"note\": \"al-Unaysi s.v. سفسطة (TAD_pages.txt leaf 38, printed ≈ 33-35; OCR renders the headword 'سقسطة'): 'سفسطة - يوناني [σοφ-] معناه المغالطة' — Greek origin, gloss 'fallacy', as the chart says.\"},\n   {\"ref\": \"TAD:53\", \"status\": \"supports\",\n    \"note\": \"al-Unaysi s.v. فلسفة (TAD_pages.txt leaf 56, printed ≈ 50-52, within the volume's offset margin): 'فلسفة - يوناني [φιλοσοφία] معناه حب الحكمة ومنه تفلسف وفيلسوف' — 'from it tafalsafa and faylasūf', i.e. the quadriliteral root built on the Greek loan.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/فلسفة and /سفسطة\", \"stance\": \"partial\",\n    \"note\": \"فلسفة: 'verbal noun of فَلْسَفَ (falsafa), either back-formed from فيلسوف (faylasūf) or borrowed from Ancient Greek φιλοσοφία' — supports. سفسطة: 'verbal noun of safsaṭa (to be a sophist), from سفسطائي safsaṭāʾī (sophist)' — i.e. from σοφιστής, not from σόφισμα as the chart draws it.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery (FVQ_pages.txt, grep 'falsafa', 'safsat')\", \"stance\": \"silent\",\n    \"note\": \"No entries — neither word is Qur'anic; both are post-conquest learned loans.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir (AFM_pages.txt, grep 'فلسف', 'سفسط')\", \"stance\": \"silent\",\n    \"note\": \"No entries; Addi Shir lists Persian, not Greek, loans in Arabic.\"}\n ]\n},\n{\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"safsateh «سفسطه»; falsafeh «فلسفه» (extra: فلاسفه ، فیلسوف)\", \"verdict\": \"confirmed\",\n \"derivation\": \"Persian took both words ready-made from Arabic, with the Arabic tāʾ marbūṭa read as final -e (falsafa > falsafe, safsaṭa > safsate); Mo'in tags فلسفه '[ع.]' (Arabic). The extra forms in the box are the Arabic plural فلاسفه falāsefe (broken plural of فیلسوف) and فیلسوف faylasūf itself, the direct arabicisation of φιλόσοφος. Historically this is a round trip through the Iranian world rather than a simple import: the falsafa tradition that gave Persian these words was made largely by Iranians (Kendī's circle, Fārābī, Ibn Sīnā) writing in Arabic, but the words themselves are Arabic-mediated Greek, exactly as the chart shows.\",\n \"derivation_fa\": \"«فلسفه» و «سفسطه» را فارسی آماده از عربی گرفته است و تاء مربوطهٔ عربی در فارسی ـه (e) خوانده می‌شود؛ معین مدخل «فلسفه» را با نشانهٔ [ع.] آورده است. دو صورت افزودهٔ نمودار یعنی «فلاسفه» (جمع مکسر فیلسوف) و «فیلسوف» (معرّب φιλόσοφος) نیز همین راه را پیموده‌اند. درخور توجه آنکه سنت فلسفهٔ اسلامی را بیشتر ایرانیان (فارابی، ابن‌سینا) به عربی ساختند، ولی خود واژه‌ها یونانی‌اند و از راه عربی به فارسی رسیده‌اند. ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D9%81%D9%84%D8%B3%D9%81%D9%87/\", \"https://abadis.ir/fatofa/%D8%B3%D9%81%D8%B3%D8%B7%D9%87/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1889\", \"status\": \"supports\",\n    \"note\": \"Mo'in s.v. سفسطه (text on abadis.ir/fatofa/سفسطه, فرهنگ معین): '(سَ سَ طِ) (اِ.) مغالطه کردن برای وارونه نشان دادن حقایق' — same gloss as the chart ('fallacy'); the printed page cannot be checked (no scan of the 6-vol Mo'in online).\"},\n   {\"ref\": \"MON:2567\", \"status\": \"supports\",\n    \"note\": \"Mo'in s.v. فلسفه: '(فَ لْ سَ فِ) [ع.] (اِ.) حکمت، دانشی که موضوع آن هستی و وجود است' — the tag [ع.] (Arabic) is precisely Nourai's Arabic → Persian arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"DKH\", \"where\": \"Dehkhoda s.v. فلسفه (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"Dehkhoda derives it from Greek, 'philos' (friend, lover) + 'sophia' (wisdom), and defines it 'علم به حقایق موجودات به اندازه توانایی بشر'.\"},\n   {\"src\": \"DKH/Encyclopaedia\", \"where\": \"abadis.ir/fatofa/سفسطه, دانشنامه اسلامی section\", \"stance\": \"supports\",\n    \"note\": \"Ties سفسطه to the سوفسطائیان (the Greek sophists) and their doctrine — the Greek origin of the Persian word is uncontroversial.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/فلسفة (descendants)\", \"stance\": \"supports\",\n    \"note\": \"Lists Persian among the descendants of Arabic فلسفة, along with Ottoman Turkish, Uzbek, Swahili etc.\"}\n ]\n},\n{\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box: the Latin relay of the Greek words, i.e. sophisma, sophista, sophisticus and philosophia/philosophus, all taken into Latin from Greek in the late Republic (Cicero uses philosophia throughout and complains at having to coin Latin equivalents). No form is printed in the box, and none is needed: Latin simply transmits the Greek words to French.\",\n \"derivation_fa\": \"این خانه در کتاب تهی است و تنها حلقهٔ انتقال را نشان می‌دهد: لاتین واژه‌های sophisma، sophista و philosophia را در سدهٔ یکم پیش از میلاد از یونانی وام گرفت (سیسرون پیوسته philosophia را به کار می‌برد) و آن‌ها را به فرانسه رساند. ادعا درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/sophomore\"],\n \"ref_check\": [\n   {\"ref\": \"none\", \"status\": \"not_checked\",\n    \"note\": \"The box carries no reference in the book (refs=None).\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. philosophia (LAT.txt line 47348)\", \"stance\": \"supports\",\n    \"note\": \"'philosophia, -ae f.: philosophie; philosophus, -i m.' — Greek loans in Latin.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. sophism (KLN_1966.txt line 35930)\", \"stance\": \"supports\",\n    \"note\": \"'fr. OF. soffime, sophime, sophisme (F. sophisme), fr. L. sophisma, fr. Gk. σόφισμα' — the Latin stage is explicit.\"}\n ]\n},\n{\n \"id\": 5, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": \"The second empty pass-through box: Old French sophime/soffime/sofisme (12th-13th c., > F. sophisme), sophiste and philosophie, from the Latin forms; these are the immediate sources of Middle English sophime (mid-14c.) and philosophie. The Old French spellings with f rather than ph, incidentally, are the closest thing in the sources to the 'sofist, sofism' of the English box below.\",\n \"derivation_fa\": \"خانهٔ تهی دوم: فرانسهٔ قدیم sophime/soffime/sofisme، sophiste و philosophie از صورت‌های لاتین، که سرچشمهٔ مستقیم صورت‌های انگلیسی میانه (sophime، میانهٔ سدهٔ ۱۴ م.) هستند. گفتنی است که همین نگارش‌های فرانسهٔ قدیم با f (نه ph) تنها شباهتی است که برای صورت‌های «sofist, sofism» در خانهٔ انگلیسی می‌توان یافت. ادعا درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/sophomore\"],\n \"ref_check\": [\n   {\"ref\": \"none\", \"status\": \"not_checked\",\n    \"note\": \"The box carries no reference in the book (refs=None).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. sophism, sophistry (KLN_1966.txt lines 35930, 35936)\", \"stance\": \"supports\",\n    \"note\": \"'ME. sophime, fr. OF. soffime, sophime, sophisme (F. sophisme)'; 'sophistry ... ME. sophistrie, fr. OF. sophisterie, sophistrie, fr. sophiste'.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/sophomore (sophism section)\", \"stance\": \"supports\",\n    \"note\": \"'mid-14c., sophime ... from Old French sophime, sofisme “a fallacy, false argument”'.\"}\n ]\n},\n{\n \"id\": 6, \"lang\": \"English\", \"words\": \"sophist, sophism, sofist, sofism, Sophia sophisticated, sophomore, philosophy,\", \"verdict\": \"transcription_suspect\",\n \"derivation\": \"Most of the box is correct and needs no comment: sophist (L. sophista < Gk. σοφιστής), sophism (ME sophime < OF sophisme < L sophisma), sophisticated (ML sophisticatus), philosophy (ME philosophie < OF < L philosophia). Two items need it. (a) 'sofist, sofism' are not English words — no such spellings are recorded in Klein, Skeat, Webster or the OED; the printed page really does show them (I checked the page image), so this is the book's own oddity, not a scanning error: Nourai has doubled his entry with an f-spelling, presumably the Persian/phonetic rendering of the same two words (cf. the Old French f-forms sofisme). (b) 'Sophia' does not come through Latin and French at all: it is taken straight from Greek σοφία 'wisdom' (Klein: 'Sophia, fem. PN. — Fr. Gk. σοφία, ‚wisdom‘'). One further nuance: 'sophomore' is only indirectly from sophism — it is an alteration of 17th-c. sophumer (from sophume, a variant of sophism), reshaped as if it were σοφός 'wise' + μωρός 'foolish' by folk etymology, and it never passed through French.\",\n \"derivation_fa\": \"بیشتر واژه‌های این خانه درست اند (sophist، sophism، sophisticated، philosophy از راه لاتین و فرانسه)، اما دو نکته هست: یکم آنکه «sofist» و «sofism» صورت‌های انگلیسی نیستند و در هیچ فرهنگی (کلاین، اسکیت، وبستر) ثبت نشده‌اند؛ با دیدن تصویر صفحهٔ چاپی روشن شد که همین دو صورت در خود کتاب چاپ شده، پس خطای خوانش اسکن نیست بلکه لغزش نویسنده است (شاید نگارش آوایی/فارسی همان دو واژه). دوم آنکه Sophia از راه لاتین و فرانسه نیامده، بلکه مستقیم از σοφία یونانی گرفته شده است. همچنین sophomore به واسطهٔ sophumer از sophism آمده و سپس به ریشه‌شناسی عامیانه چنان دگرگون شده که گویی از σοφός «دانا» و μωρός «نادان» ساخته شده باشد.\",\n \"error_in\": \"book\",\n \"book_prints\": \"sophist, sophism, sofist, sofism, Sophia sophisticated, sophomore, philosophy,\",\n \"correct_form\": \"sophist, sophism, Sophia, sophisticated, sophomore, philosophy\",\n \"sources\": [\"https://www.etymonline.com/word/sophomore\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1332\", \"status\": \"not_checked\",\n    \"note\": \"The 1975/76 New College Edition is not online. The number is also internally suspect: the root and the Greek node of the same chart cite AHD:1232 for the same word family, and sophism/sophist occupy a single opening of that dictionary, so 1332 looks like a misprint for 1232 in the book.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. sophism, Sophia, sophisticate, sophomore (KLN_1966.txt lines 35928-35936)\", \"stance\": \"partial\",\n    \"note\": \"'Sophia, fem. PN. — Fr. Gk. σοφία, ‚wisdom‘, fr. σοφός, ‚wise‘' (no French stage); 'sophomore ... Alteration of obsolete sophumer, formed fr. sophume, an old var. of sophism ... The change of sophumer to sophomore was due to a popular misconception of the former word as a compound of σοφός, ‚clever‘, and μωρός, ‚foolish, dull‘.' Klein has no 'sofist'/'sofism'.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/sophomore\", \"stance\": \"partial\",\n    \"note\": \"'1680s, “student in the second year of university study”, from earlier sophumer (1650s), from sophume, archaic variant of sophism ... folk etymology from Greek sophos “wise” + moros “foolish, dull”' — no French relay, and no f-spellings.\"},\n   {\"src\": \"SKT/WEB\", \"where\": \"Skeat and Webster's 2nd ed. (grep 'sofist', 'sofism')\", \"stance\": \"silent\",\n    \"note\": \"Neither dictionary records 'sofist' or 'sofism' as English words, confirming that these two items in the book's list are not standard forms.\"}\n ]\n}\n]\n\ndoc = {\n \"pdf_page\": 464,\n \"book_page\": 434,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [e0, e2]\n}\n\nimport io\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-464.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-464.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-464.json > /dev/null && echo \"valid JSON\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 464"
}
```


### [2026-09-14T02:58:27.955Z] TOOL RESULT

```
written
valid JSON
nodes verified: 18/18
node verdicts: {'confirmed': 14, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 17, 'partial': 2, 'not_checked': 5}
books consulted: {'supports': 37, 'silent': 7, 'partial': 3} | by book: {'KLN': 12, 'SKT': 4, 'Etymonline': 4, 'Wiktionary': 3, 'DKH': 3, 'LAT': 3, 'SYN': 2, 'FVQ': 2, 'AFM': 2, 'BRT': 1, 'KNT': 1, 'PHD': 1, 'HRN': 1, 'WEB': 1, 'MON': 1, 'MON/DKH': 1, 'LKT': 1, 'FSF': 1, 'LEW': 1, 'DKH/Encyclopaedia': 1, 'SKT/WEB': 1}
```


## [2026-09-14T02:58:33.699Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json, io\np=\"data/verification/page-464.json\"\nd=json.load(open(p,encoding=\"utf-8\"))\nn=d[\"entries\"][0][\"note\"]\nd[\"entries\"][0][\"note\"]=n.replace(\"the book prints the Latin word as 'salŭsps' — in fact 'salŭs' with a breve, salŭs —\",\"the book prints the Latin word with a breve, 'salŭs' —\")\nassert \"salŭsps\" not in d[\"entries\"][0][\"note\"]\nwith io.open(p,\"w\",encoding=\"utf-8\") as f: json.dump(d,f,ensure_ascii=False,indent=1)\nprint(d[\"entries\"][0][\"note\"][-260:])\nEOF\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 464 | tail -3"
}
```


### [2026-09-14T02:58:34.841Z] TOOL RESULT

```
t and the gloss are all correct. One small printing point on this page: the book prints the Latin word with a breve, 'salŭs' — where Latin has salūs (gen. salūtis) with a long ū; the extraction is faithful to the page, the quantity mark is the book's own slip.
root verdicts: {'confirmed': 2}
ref checks: {'supports': 17, 'partial': 2, 'not_checked': 5}
books consulted: {'supports': 37, 'silent': 7, 'partial': 3} | by book: {'KLN': 12, 'SKT': 4, 'Etymonline': 4, 'Wiktionary': 3, 'DKH': 3, 'LAT': 3, 'SYN': 2, 'FVQ': 2, 'AFM': 2, 'BRT': 1, 'KNT': 1, 'PHD': 1, 'HRN': 1, 'WEB': 1, 'MON': 1, 'MON/DKH': 1, 'LKT': 1, 'FSF': 1, 'LEW': 1, 'DKH/Encyclopaedia': 1, 'SKT/WEB': 1}
```


## [2026-09-14T02:58:51.620Z] AGENT

Page 464 (book p. 434) verified — `data/verification/page-464.json`, `verify_check.py 464` shows 0 PROBLEM lines.

**Counts:** 18/18 nodes — 14 confirmed, 3 plausible, 1 transcription_suspect. Both roots confirmed. Ref checks: 17 supports, 2 partial, 5 not_checked. 47 `consulted` entries across 21 books.

**Flagged items**
- `transcription_suspect` — Sophos, entry 2 node #6 (English): the book prints "sophist, sophism, **sofist, sofism**, Sophia sophisticated, sophomore, philosophy". `sofist`/`sofism` are not English words (absent from Klein, Skeat, Webster). `error_in: "book"` — I checked the printed page image (copied to `data/verification/sources/refs/ocr/BOOK/464.png`); the extraction is faithful. Also noted there: *Sophia* comes straight from Greek σοφία, not via Latin/French, and *sophomore* is an alteration of *sophumer* (folk-etymologised as sophos + mōros), not a French loan.
- `plausible` — Sol #4 Greek *katholicos*: gloss "whole undivided church of Christ" is the later ecclesiastical application (ἡ καθολικὴ ἐκκλησία, Ignatius c. 110 CE), not the adjective's meaning ("general, universal"); spelling is Latinised.
- `plausible` — Sol #8 Arabic *jāthalīq*: really from Greek katholikos but via **Syriac** qāthōlīqā (title of the Catholicos of Seleucia-Ctesiphon), which the chart omits; "jâselîq" is the Persian reading of ث.
- `plausible` — Sophos #2 Arabic: *falsafa* ← φιλοσοφία is solid, but *safsaṭa* is derived by modern sources from σοφιστής / سوفسطائي, not from σόφισμα as drawn.

**No extraction errors** — the JSON matches the printed page everywhere I checked (including "haurva 1", "Xordâd", the Ferdowsi verse, and the odd English word list).

**Notable reference findings:** BQT:729 and BQT:2318 are exact — Mo'in's own footnotes on خرداد and هر give Av. haurvatāt- / haruva- → «هر» and cross-refer each other. TAD:19/35/53 all located and supporting (OCR headwords mangled; found on leaves 22, 38, 56). FSF:141 located (leaf 186) with the very Ferdowsi line Nourai quotes. Two AHD page numbers are unverifiable (the 1975/76 New College Edition is not online) and internally inconsistent: AHD:1232 for the Sophos root vs AHD:1332 for the same word family in the English box — likely a misprint in the book. Minor book slip: Latin printed "salŭs" for salūs.
