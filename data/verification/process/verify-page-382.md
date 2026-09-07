# Verification process log — verify-page-382


## [2026-09-07T20:39:44.348Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 382 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-382.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-382.json. Write /home/sfmqrb/git/rishe/data/verification/page-382.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 382` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:39:47.349Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:39:48.045Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:39:48.063Z] TOOL RESULT

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


## [2026-09-07T20:39:48.423Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-382.txt"
}
```


### [2026-09-07T20:39:48.447Z] TOOL RESULT

```
1	=== PDF page 382 (book page 352) ===
2	--- entry 0 ---
3	ROOT [Old Persian] Pârsa : name of an Aryan (Indo-European) tribe who migrated south to Persia (Iran) about 4000 years ago. Also name of a province south of the Persian Empire  (refs KNT:196)
4	#1 (parent #0) [Persian] refs=BQT; MON5:322; IRN:63 | Pârs, Fârs «پارس ۱ ، فارس» : Persia ; Pâsârgâd «پاسارگاد ، پارسه گاد» : home of the Pârs people | NOTE: Pâsârgâd was also name of an early Iranian tribe.
5	#2 (parent #0) [Greek] refs=SYN:377 | persis : Persia
6	  #3 (parent #2) [Latin] refs=None | persis : Persia, Persian ; malus persica : Persian apple (peach)
7	    #4 (parent #3) [English] refs=AHD:963 | Persia, peach
8	    #5 (parent #3) [French] refs=VOP:120 | pěches : peach ; pěches melba : peach ice cream
9	      #6 (parent #5) [Persian] refs=VOP:120 | pešmelbâ «پشملبا» : a fancy peach ice cream
10	--- entry 1 ---
11	ROOT [Old Persian] Parth, Parni, Parthava, Partia : Parth, Parni: the name of a tribe in Khorâsân who rose to power and pushed the Greeks out of Iran in 250 BC. Parthava, Partia: the province of Parths in N.E. of the Persian Empire.  (refs KNT:196)
12	#1 (parent #0) [Persian] refs=BQT; MON; FSF:117 | pârt «پارت» : an ancient Iranian dynasty ; pahlov «پَهلو ۱» : a Parthian, a strong and brave hero | extra: پهلبد ، پهلوی
13	#2 (parent #0) [English] refs=AHD:955; WEB:1306 | Parthia ; parting shot : thrusts delivered in retreat as Parthian archers used to do
14	#3 (parent #0) [Latin] refs=AHD:952 | pertica pellis : Parthian leather ; particaminum
15	  #4 (parent #3) [Old French] refs=None | parchemin
16	    #5 (parent #4) [English] refs=None | parchment
17	--- entry 2 ---
18	ROOT Parthava -> redirect to Parth
19	--- entry 3 ---
20	ROOT Partia -> redirect to Parth
21	
```


## [2026-09-07T20:39:52.151Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-382.json",
 "description": "Read source JSON for page 382"
}
```


### [2026-09-07T20:39:52.186Z] TOOL RESULT

```
{
  "pdf_page": 382,
  "book_page": 352,
  "entries": [
    {
      "root": {
        "name": "Pârsa",
        "lang": "Old Persian",
        "refs": "KNT:196",
        "gloss": "name of an Aryan (Indo-European) tribe who migrated south to Persia (Iran) about 4000 years ago. Also name of a province south of the Persian Empire"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT; MON5:322; IRN:63",
          "words": [
            {"translit": "Pârs, Fârs", "gloss": "Persia", "script": "پارس ۱ ، فارس"},
            {"translit": "Pâsârgâd", "gloss": "home of the Pârs people", "script": "پاسارگاد ، پارسه گاد"}
          ],
          "script_extra": null,
          "note": "Pâsârgâd was also name of an early Iranian tribe.",
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "SYN:377",
          "words": [
            {"translit": "persis", "gloss": "Persia", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "persis", "gloss": "Persia, Persian", "script": null},
            {"translit": "malus persica", "gloss": "Persian apple (peach)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:963",
          "words": [
            {"translit": "Persia, peach", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "French",
          "refs": "VOP:120",
          "words": [
            {"translit": "pěches", "gloss": "peach", "script": null},
            {"translit": "pěches melba", "gloss": "peach ice cream", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "VOP:120",
          "words": [
            {"translit": "pešmelbâ", "gloss": "a fancy peach ice cream", "script": "پشملبا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Parth, Parni, Parthava, Partia",
        "lang": "Old Persian",
        "refs": "KNT:196",
        "gloss": "Parth, Parni: the name of a tribe in Khorâsân who rose to power and pushed the Greeks out of Iran in 250 BC. Parthava, Partia: the province of Parths in N.E. of the Persian Empire."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT; MON; FSF:117",
          "words": [
            {"translit": "pârt", "gloss": "an ancient Iranian dynasty", "script": "پارت"},
            {"translit": "pahlov", "gloss": "a Parthian, a strong and brave hero", "script": "پَهلو ۱"}
          ],
          "script_extra": "پهلبد ، پهلوی",
          "note": null,
          "quote": {
            "text": "هم از پهلوی، پارس، کوچ و بلوچ - زگیلان جنگی و دشت سروج",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "English",
          "refs": "AHD:955; WEB:1306",
          "words": [
            {"translit": "Parthia", "gloss": null, "script": null},
            {"translit": "parting shot", "gloss": "thrusts delivered in retreat as Parthian archers used to do", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:952",
          "words": [
            {"translit": "pertica pellis", "gloss": "Parthian leather", "script": null},
            {"translit": "particaminum", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Old French",
          "refs": null,
          "words": [
            {"translit": "parchemin", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "parchment", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Parthava", "redirect": "Parth"},
      "nodes": []
    },
    {
      "root": {"name": "Partia", "redirect": "Parth"},
      "nodes": []
    }
  ]
}
```


## [2026-09-07T20:39:53.906Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KNT','BQT','MON','IRN','SYN','AHD','VOP','FSF','WEB','POK','WLD','KLN','SKT','FSD','HRN','HUB','PHD','NYB','IEC','BRT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-07T20:39:55.723Z] TOOL RESULT

```
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-07T20:40:01.285Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py"
}
```


### [2026-09-07T20:40:01.327Z] TOOL RESULT

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


## [2026-09-07T20:40:01.833Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls | head -50 && echo ---- && python3 -c \"\nimport json;d=json.load(open('page-381.json')) if __import__('os').path.exists('page-381.json') else None\nprint(bool(d))\""
}
```


### [2026-09-07T20:40:03.209Z] TOOL RESULT

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
----
False
```


## [2026-09-07T20:40:08.838Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80"
}
```


### [2026-09-07T20:40:08.892Z] TOOL RESULT

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


## [2026-09-07T20:40:09.566Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Pārsa\\|Parsa\\|Parthava\\|Parθava\" KNT.txt | head -40"
}
```


### [2026-09-07T20:40:09.675Z] TOOL RESULT

```
477:(Hamadan) in Media; though the two kings are spoken of in them only as ‘king in Parsa = Persis’, which was quite distinct from Media. They may have been set up in the time of Artaxerxes П as part of an anti-Cyrus propaganda, since Cyrus the Great had dethroned Arsames, and Cyrus the Younger came very near de- feating and killing Artaxerxes II at Cunaxa (cf. JAOS 66.206-12). The gold tablet A?Hc may have been a third in the same series; all three are in Old Persian only. *Cf. especially Schaeder, SbPAW 1931.636-42. 4 They are hardly to be ascribed to Cyrus the Younger, despite Wb. ZDMG 48.653-65 (cf. also KIA lxvii-bax) on CMa, which alone was known to him; for the opposing view, cf. Hz. Klio 8.1 ff. * Though perhaps not much used by him. The other three known inscriptions of Cyrus the Great are in Akkadian; but Strabo 15.3.7-8 (page 730), on the authority of Onesicritus, states that the tomb of Cyrus at Pasargadae bore at least two inscriptions, one being bilingual, Greek and Persian. We need attach no importance to the identification of the languages by Onesicritus, but the account indicates that Cyrus had inscriptions engraved in more than one language; in which case it is unlikely that his own vernacular was omitted. Cf. JAOS 66.206-12; but also Hinz, ZDMG 96.343-9.
780:WZKM 39.92). Pársà AmH 5, for Parsa. asmānām A*Pa З, for asmánam.
1534:*prek- in ufrastam ‘well punished’, *prk- in aparsam ‘I punished’.
1604:aor. niy-aparsam to pIE root *peik-; §102. pIE sir (after u) > pAr. sr > plr. #т > OP
1636:(3) plr. change of p tk to f 0 x before con- sonants ($74.D): рага but fra-, aparsam but -frastam, tuvam but ace. ийт, akariya but cazriyü, drauga adurujiya but duructam.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1822:$150. Noun AND ADJECTIVE STEMS WITH SUF- FIX -ya- are a miscellaneous group. They include ai-va- ‘one’; adjective duru-va-, to verbal root dar-; adj. par-uva-; ethnic Par@a-va-, cf. Parsa-; yd-va-, to relative ya-; har-uva-; visa- and (Med.) vispa-, from pIE *yik-yo-; ji-va- ‘living’, unless the v is somehow radical (cf. §216). On Gau- baruva-, see Lex.:s.v.; on fem. aruva- as abstract, see Lex. s.v.
1974:Pársa ‘Persis, Persia’: including districts Kar- mana, Yauttyd; cities Paisiydéuvddd, perhaps Parsa; towns Uvddaicaya, Kuganaká, Татай, Каха, mountains Arakadrig, Parga.
2006:Partava X Parsa x
2038:Loc. Sg. Parsaiy, Mädaiy, Mudrüyaiy, Ujaiy Unjaiy, Pardavaiy, Arminiyaiy, Asagartaty, Hagmatanaty; with added -à, duvarayd, dastayd, spaémardayd, probably kar Saya, {dalrtanayd; nt. uzmaya.
2445:pIE *prek-, pres. *prk-ske-, OP parsümiy ‘I pun- ish’, Skt. prechami ‘I ask’; imf. OP aparsam, Skt. dprecham; imv. OP parsd, Skt. prechd.
2528:I. The Sigmatic Aorist is seen in niy-aparsam ‘I inscribed’ (or -apiSam?)}, to root pai8-, pIE *peik-; in mid. adarSiy ‘I held’, to root dar-, pIE *dher-; perhaps in pass. -asahya in frasah[ya]. The aorist endings 3d sg. -s-t, pl. -s-nf, may also be respon- sible for the endings of @1$ -diSa" to root ay- (8208); akunaus akunavasa to kar-; adurujiyasa to durujiya-; abaraha to bar-.
2539:II. Thematic stems have subjunctives with the long thematie vowel throughout, Ist sg. and 181 and 3d pl. o, other forms é; 2d and 3d sg. and mid. as in Skt. bhár-àsi -àt -àse -äte : OP zšnāsāhy, Gahy (for *6aháhy), apa-gaudayàhy, \drau\jiyahy, pati-parsühy, pari-barühy (and -Gh*-d13), vainahy; ni-rasütty, xsndsdtiy, pati~parsatiy, bavatiy, vaind- tty; maniyahaty (for variant spellings, see Lex. s.v. ‘man-); maniydtaiy, gaubdtaty, 6adayátaty, yadataiy, vainātaiy. 3d pl. act. as in Skt. -dnis: OP vi-naéaya*tty (restored form).
2563:II. The secondary ending - was attached di- rectly to the thematic vowel -o-: pIE ebhero-m ‘I bore’, Skt. dbharam, Gk. éepor, OP abaram; Skt. dpyccham, OP aparsam. Other OP examples: niy- asddayam, franayam, arasam, etc. When attached to non-thematic stems, the -m became vocalic, and developed in pAr. to -am, a generalization of the antevocalic value, furthered by the identity
2604:I. The second smgular active of thematic stems is the stem without suffix: jivà, Skt. jiva; pari-bará, Skt. bhára, Gk. $€pe; parsa, Skt. prechd, Lat. posce. That of non-thematic stems has an accented -dhi, attached to the zero grade of the root: pIE *i-dht, OP -idiy in paraidiy and paridiy, Skt. tht, Gk. 16; pIE *gthn-dht, OP jadiy, Skt. jaht; OP pädiy, didiy (5129), G-rsnudiy.
2702:A. Expressing place where, without a preposi- tion, as in DB 1.34f pasdva drauga dahyauvā vasiy abava щй Parsaty ша Madaty ша aniyãwā dah- yusued ‘afterwards the Lie waxed great in the country, both in Persia and in Media and in the other provinces’; DB 2.75 duvarayãmaiy basta аййттуа ‘he was held bound at my palace en-
2716:Е. With or without prepositions, to denote place where or within which: DB 1.92 vardanam amu» Ufrātwã ‘a town beside the Euphrates’; DB 3.26 kära Parsa hya vapatüj ‘the Persian army which (was) in the palace’; XPa 13f vasiy aniyaSciy naibam kartam ana Parsé ‘much other good (construction) was built within this (city) Persepolis’.
2760:67. ApPosrTIVES occur in the following cases; lack of examples in the other cases is accidental: nom. DB 1.1, 1.53, and almost everywhere; ace. DB 1.54, DPd 2, DNb 4, etc.; gen. DB 3.59, DPd 9-11, XPe 14, etc.; loc. infrequent, DB 1.34f. More often the appositive, if more than а single word or if to an oblique ease, is expressed by an anacoluthie nominative phrase, followed by a resumptive pronoun or adverb ($314a; 8312). Partial appositives occur as in DB 1.34f pasdva drauga dahyawd vasiy аата щй Parsaiy ша Mädaiy utü aniyãwā dahyušuvā ‘afterward the Lie became great in the country, both in Persia and in Media and in other provinces’; also DB 1.401, 1.48f, DSf 25f ikä avaniya aniyā XL ara- Santis baránà ата X X атаќаті bar snd ‘the rubble
2769:may be used as predicate to any subject:! DB 2.18f кага Parsa шй Майа hya ира mam аһа haw kamnam dha ‘the Persian and Median army which was with me—this was a small thing’; во also DB 1.47 uvaipa saam (referring to Parsam utà Madam ша aniyà dahyàva), DNa 39 ctyakaram aha ava dahyava, DNb 6f avakaram amiy, ОХЬ 27f avā- karam-ca-maiy usiy wa framand, DNb 50 ciyükaram amiy ciyükaram-ca-maiy tonaré. A neu- ter subject may have a masculine substantive as predicate: DNb 11f tya rdstam ava тат kama ‘what is right, that is my desire’.
2799:ПІ. This pronoun as article is used after a noun to introduce modifiers: an appositive substantive alone (DB 1.44, 1.50) or with preceding genitive (XPf 30, DB 1.89); a common adjective (DB 9.25f, DPe 3f, DSf 30f, 37), two successive com- mon adjectives (DSf 11), an ethnic (DBk 2, DB 1.79, 2.21); a superlative with following genitive of the whole (DSf 9); a possessive genitive of a personal name (DB 1.89) or of a pronoun (DB 235, 1.69); a locative substantive (DB 1.81 z5acam tya Babirauv) or an instrumental with en- clitie postposition (DB 3.26 kara Parsa hya v'łāpa- tiy).
2800:IV. This pronoun as article occasionally pre- cedes its noun to attach to it an adjective or a genitive; there are these examples: DB 1.8 and DBa 12f hyà атахат iauma; DB 1.28 tyand mand айй, cf. DNa 21; DB 3.32 hya aniya kāra Parsa; DB 4.87f tyäm imatsam martiyanàm taumam; DB 5.12 tyamsém тай йат; DNa 56f hyd Auramaz- daha framünà; ПОЇ 12f hya тала mia Vistaspa
2804:I. The definite article, properly speaking, is lacking in OP, despite the uses given in the pre- ceding section (ef. Lg. 20.6-8); for kya hyd tya as article function only to attach modifiers to another substantive, or to indicate generic value. Thus we find Ката Parsa utä Мада hya ира mam àha haw kamnam aha ‘the Persian and Median army which was with me, this was a small thing’ (DB 2.181); adam Déarayavaus xidyatiya vazraka ‘I (am) Darius the Great King’ (DB 1.1). It is noticeable
2898:DPe 22 yadiy Ката Parsa pata ahaty.
3041:II. Descriptive adjectives, if attributive, follow their nouns. Exceptions, (a) in a fixed phrase, DNb 23f wradanüm hadugam ‘the Ordinance of Good Regulations’; (b) with a preceding demonstrative, as in DPe 8f hadé апа Рата kara ‘with this Persian army’, DPe 21 imam Parsam Катат (but also DPe 22 kära Parsa, etc.); (c) for emphasis, in DNa 46 Pürsa martiya, DNa 431 Pársahyà marti- yahyà.
3042:III. Attributive adjectives preceded by articu- lar hya follow the same principles; hya is required if ava- precedes the noun, as in avam Катат tyam hamigiyam ‘that rebellious army’ (DB 2.35, etc.). The only instance which precedes is DB 3.32 hya aniya Ката Parsa ‘the rest of the Persian army’.
3430:1 Àriyáramna : xSayaftya : vazraka : xSayaé 2 iya : xsüyafiyànàm : xSayafiya : Parsa
3431:3 : Cispais : xšãyaðiyahyā : риса ; HaxdmaniSah 4 ув : парӣ : Вапу : Áriyáramna : xšāyaðiya 5 :iyam : dahyau§ : Parsa : tya : adam : dárayá 6 miy : hya : uvaspà : umartiyü : mana : baga 7 : vazraka : Auramazda ; frábara : vašnā : Au 8 ramazdàáha : adam : xXàyafiya : iyam : da 9 hyauS : amiy : 80у : Anyaramna
3461:2 апат : xSdyafiya : Parsaiy : xSdyafiya : dahyindm : Vist
3473:14 à : Auramazdáha : adamšām : хќйуабуа : áham : Parsa : Üvja : Babirud : A
3479:22 bartam : abaram : hya : апка : аһа : avam : ufrastam : aparsam : vašnā : Auramazda 23 ha : ima : dahyáva : tyanà : manā : dita : apariyàya : yaðāšām : hacima : абаһ
3487:31 büjiya : avam : Bardiyam : avàja * уаба : Kabüjiya : Bardiyam : avaja : kürahy 32 à : пазу : azdà : abava : (уа : Bardiya : avajata : раѕауа : Kabijiya : Mudráyam 33 : akiyava : уада : Kabūjiya : Mudrayam : aSiyava : pasáva : kara : апка : abava 34 : pasava : drauga : dahyauvi : vasiy : abava : uta : Parsaiy : ша : Mádaiy : ut 35 d:aniy&uvà : dahyuSuvà ; 0àtiy : Dàrayavaus :х3йуайуа : pa
3490:40 àt& : pasiva : kira : haruva : hamigiya : abava : haeà : Kabüjiyà : abiy : avam : 4] aSiyava : uta : Parsa : ша : Mada : uta : aniyà : dahyáva : xfagam : hauv
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3592:49 dam : іу : Därayavauš : xšāyaðiya : pasáva : Vaumisa : nàma : Pārsa : manā : ba
3624:81 iy : Uvaxstrahya : taumiya : pasiva : adam : Кагал : Parsam : ut
3699:12 : I martiya : Frada : пата : Margava : avam : mafüistam : akunavatà : pasá 13 va : adam : fráisayam : DadarSis : пата : Parsa : manā : badaka : Baxtny
3710:26 : Кага : Parsa : һуа : v'fapatiy : hacd : Үайауй : frataram : ha
3712:28 m : a’iyava : hauv : xSayafiya : abava : Parsaly : 05
3715:31 iya : пата : Parsa : mand : badaka : avamSàm : maistam, : aku 32 navam : hya : aniya : kara : Рагза : pasā : mana : аўуауа : Mā
3716:33 dam : разӣуа : Artavardiya : hada : Ката : asiyava : Pārsam ` 34 : yaa : Pársam : parárasa : Ваха : папа : vardanam : Parsaly : а
```


## [2026-09-07T20:40:15.278Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor n in (210,211,212):\n    print('=== leaf',n,'===')\n    print(pages[n][:3000])\nEOF"
}
```


### [2026-09-07T20:40:16.619Z] TOOL RESULT

```
232
=== leaf 210 ===
1) XPh 23.
tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) AmH 5; AsH 13°. tyà npf. DB 1.13, 18; 2.6; 4.33; DPe 9, 14f; DSf 45. tyaiy as npf. (§258.1V) = XPh 31. рё apf. DPe 7; DNa 17, 40; DSe 16. . tyaišām gpf. DSm 6°; XPh 15.
tya nsn. (M0) DB 1.27, 61, 67; 2.91; 3.10, 20, 58, 76; 4.1f, 42, 49°, 53; DNa 48; DNb 2, 11, 29, 54, 56; DSe 31, 43; DSf 36; DS} 5^; D8n 2^; DZe 9, 10; XPa 19; XPb 23; ХРЇ 26, 37, 46; XPg 4; XPh 42; XV 19; AjPa 26. tya-sém DB 1.19; DNa 20; DSe 19°; XPh 17. tya-maiy DNb 48; DSe 52°; DSf 19°; DSs 7^; XPa 19f; XPb 24, 30; XPe 13 bis; XPd 19; XPf 38, 47; X8e 5°; XV 27°; A!Pa 24°; A?He 20. tya-taiy DNb 58. tya-patiy XPa 15. (ya asn. DB 1.44, 72; 4.3, 40, 59, 75, 79; 5.2; DPh 4; DNb 22, 24; DSa 4; DSf 20f, 22°; рө) 2°, 4; DSI 3; DH 3; XPa 14, 15; XPf 41; XPh 43, 49, 52; A’Sa 5^; А4 3; А?На 7. [tya]- ат DNa 36f. tya-maiy DPh 8; DH 6. tya-patiy XPf 40f. {уала isn. DSf 42. {уй npn. in tyã- maiy DNb 13. tyä apn. DB 1.64; DNb 46, 49. tyā-diš DB 1.65.
(2) Def. art., ‘the’: ат asm. DB 1.50, 54, 57, . T8, 89, 95; 2.21, 25f, 35, 41, 46, 55, 61, 69, 87, 97^; 3.7, 18, 38, 46, 625, 67f; 481; DSe 39. tyam- iim DB 5.12".
іуйт asf. DB 1.69, 71; 4.87; DNa 59. tya as asf. ($56. V) AsH 9, A’Sc 6. tyaisám gpf. DPe 3f.
tya nsn. DNa 21; DSe 20°, 38; XPh 19. tya asn. DB 1.81; DSf 11 his; DSm 4° bis; DSp 2°, 8°; DZc 4 bis. tyanā isn. DB 1.23.
(3) Demonst. pron., ‘this’: буй ndm. DSf 14. шай apm. DB 3.73.
уа. conj. ‘that’, nt. sg. of preceding; cf.
similar uses of Gk. öre, Lt. quod, NEng. that, NGm. dass. In various uses ($299):
(1) ‘that’, introducing clause of fact as object, DSf 28 bis, 29.
(2) ‘that’, introducing clause of volition, with opt., DNb 8, 10, 19.
(3) ‘that’, introdueing indirect or direct quota- tion, DD 1.32, 52; DNa asf.
(+) ‘because’, introducing causal clause, DNb 38 (tya-maty).
(5) ‘so that’, introducing result clause, DB 4.34; DNb 7.
187
(6) ma-tya “п order that . . . not, lest, not, DB 4.43, 48, 71, and in md-fya-mdém DB 1.52.
(7) yada-tya ‘where’ XPh 35, cf. yadéya ‘where’ XPh 39.
(8) yafü tya ‘when’ XPh 29.
Odigarct- adj. ‘Thaigarci’, third month, May- June: Elam. sákurrisi$, АКК. simannu (S30, §72, §87, $126, $1521, §165); an etymology as ‘Garlic-Collecting Month’, involving normaliza- tion @digraci-, is given by Justi, ZDMG 51.243 (cf. Bthl. AiW 786). Oäigarcaiš gsm. DB 2.46f.
akata- pte. adj. ‘completed’: Av. sak- ‘(of time) pass’, pIE *keg-; fut. pte. pass. (8244) like Av. yazata- ‘worthy of worship’ (Bv. BSLP 30.1.68-70), passing into past meaning, like Skt. pacalá- ‘cooked’, Gk. dpi-delx-e7os ‘much pointed out, famous’ (Schwyzer, Griech, Gram. 501-2); rather than pres. act. pte. daka"t- made thematic (cf. Bthl. АКМ 22.79-80). @akatam nsn. DB 3.8. 6akalá npn. DB 1.38, 42, 56, 90, 96; 2.26f, 36, 42, 47, 56, 70, 98; 3.19, 39f, 47, 63, 68, 89.
Oalagu- sb. ‘Sattagydia’, a province of the ` Persian Empire: Elam. sa-ad-da-ku-13, Akk. sa- al-ta-qu-u, Gk. Zarrayudia ($07, §87, $120, $158.1, $161.ITa, $204.V). From éata- ‘hundred’, 
=== leaf 211 ===
 word of uncertain meaning, Sb 3.
Sanuvaniya- sb. ‘bowman’: deriv. ($144.IV) of stem in Av. Üanvar/n- ‘bow’, ef. Skt. dhanvan- ‘bow’ (583.11, $114, §155.1V) and Hz. ApI 339.
See also wlanwaniya-.  Ganwaniya.nsm. DNb 42.
188
*
bard- sb. ‘year’: Av. sarad- ‘year’, NPers. säl, Skt. Sardd- ‘autumn’ (§31, 587, $142). For the chronology of the rebellions against Darius, see Hist. App. IV. &ardam asf. DB 5.3. barda gsf. DB 4.4f, 41, 45, 52, 60.
barmi- sb. ‘timber’ (86, 529, $34, $15217): no probable etymology, despite Kónig, Burgbau 52-4; Hz. AMI 3.58; Gray, AJP 53.67-8. barmiš р? 30.
баћ- vb. ‘declare, say’: Ау. sqh-, pres. sanha-, Skt. édsati, Lt. censet, рТЕ *kens- (§87); perhaps lacking the nasal in the OP present ($108.n1; MB Gr. $134, ef. Wackernagel, IF 45.321-7; dubious theories on the pronunciation, Hz. AMI 3.83-6). 6atiy (8131, $213, 5228.1; JAOS 35.332-4) AmH 4, 9; AsH 5; CMb 3; DB 1.3, 6, 8f, 11, 121, 17, 20, 24, 26f, 35, 43, 48, 61, 71, 72, 81, 83, 90; 2.1, 5°, 8, 11, 13, 18, 29, 37, 42, 49, 57, 64, 70, 78, 91, 92; 3.1, 9, 10, 19, 21, 28f, 40, 49, 521, 54, 64, 69, 75, 76, 83; 4.1, 2, 31, 33, 36, 40, 43, 45, 50, 52f, 57, 59, 61, 67, 69, 72, 76, 80, 86, 88; 5.1, 14, 18, 20, 30, 33f; DBa 4, 9, 13f; DPd 5, 12; DPe 5, 18; DPh 3; DNa 15, 30, 47; DNb 5, 22; DSa 3; рва 2f°; DSe 14, 30°, 41, 49°; DSf 8, 55; DSg 2f; DSi 2f; DS} 2, 4°; DSk 3; DSI 1; DSm 3; DSo 2°; DSt 6f; DZc 7; DH 3; XPa 11, 17; XPb 21; ХРе 9; XPd
^ 15; ХРЇ 15, 27, 43; XPg 1; XPh 13, 28, 56; ХР);
XSa 1; X8e 2f°; XV 16; А:Ра 17; D'Sb 3°; Аа 1; A’Sc 1°; A’Sd 2; А?На 1; A?He 7, 15; A?Pa 8, 21, 23. |
аваћат Ist sg. imf. (5181, $132.23, 8213) DB 2.20, 30, 50, 83; 3.14. 85; DNa 37. alaha imf. DB 1.75; 2.10°, 15, 80; 3.25, 57£; 4.8, 11, 13, 16, 19, 21, 24, 21°, 29; DBb 4; DBe 5; DBd 3; DBe 5; DBf 3; DBg 4f; DBh 4; рв: 4; ОВ) 3. éahya- mahy 1st pl. pass. (5220, $280.Г) DB 1.7; DBa 10f. aðahya imf. pass. ($220) DB 1.20, 231; РМа 20; DSe 19°; abahiya (827) XPh 18. " баћу 2d sg. subj. ($181, $222.11, $227.I) DB 4.55, 58. 6aslanaiy inf. ($132.23) DB 1.58f.
bikä- sb. ‘gravel, rubble, broken stone’ ‘(wrongly Konig, Burgbau 50, cf. Kent, JAOS 53.14): probably pIE *higd- (887, $143.IV), ef. Skt. sikata- ‘sand, gravel’ (with Prakrit s for Skt. §, or borrowed from an Iranian dialect, Ву. BSLP 30.1.60-1), and perhaps OP Sikayawatis (with Med. s-), fem. to *$ikayas-vant- (ef. Bv. BSLP 30.1.61; Hz. AMI 3.55-6; Kent, JAOS 51.203). Ка nsf. DSf 25, 28. бат asf. DSi 27.
OLD PERSIAN
Өшта- sb. "Thukhra', father of Otanes (8163.Ib, §164 JIT): Elam. du-uk-kur-ra, Akk. su- uh-ra-’. Perhaps same as Av. suzra- ‘red’, NPers, surz, Skt. $ukrd- "bright ($87, 5108.1, §148.1; ef, Foy, KZ 35.20).  Guzrah|yli gsm. DB 4.83.
Oüravühara- adj. “Thuravahara’, second month, April-May: Elam. turmar, Akk. айайги.
Cpd. of @йга- ‘vigorous’, Av. süra-, Skt. $ra-, Gk. —
kvpos ‘valid’, pIE *hiro- (887), + vàáhara- ‘spring time’, Skt. vdsard- ‘bright’, NPers. bahar ‘spring’, Lith. vásara ‘summer’ (§1181, $126, $148, 5148.1, §154.1; ef.
=== leaf 212 ===
fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.IT) DNa 2, 3 bis, 4; DSf 1f^, 2 bis, 3, 9; DSp 2°; DSt 2°, 3, 3f°, 4°; DZe 1, 2 ter; DE 3, 4, 5, 6; XPa 1f, 2, 3 bis; XPb 3, 4, 5, 6; ХРе 2 bis, 3 bis; XPd 2, 3, 4 bis; XPf 2, 3 bis, 4; XPh 2 bis, 3 bis; XE 3f, 5, 5f, 6; XV 3, 4 bis, 5; A!P2 2°, 3°, 4°, 4f°; А?Не 2, 3, 4 bis; A?Pa 2, 3, 4 bis.
daiy, see -di-.
dawa- sb. (false) divinity, demon’ (cf. Hz. RHRel. 43:.32-7; AMY 8:74-5, ApI 126-30): Av.
^
-
УА $ " Aic hts КҮЧ - EUR EE EE ГЕНЕ ЗЕ, m aad ACCENT add Va, rA a Ra SENS un at Mom o "heat aai Тэ мә GIO Ate a ec ala ie
Rec tae ais 5g AAA, лса mia (n n m VRAT, ЁК te o rre ns"
- eS i.i Nai ie "e Loren чйр ло
LEXICON
daéva-, Skt. devd- ‘deity’, Lt. divos, deus, pIE *deiyo- (876.1IT, $114, 5148.11). See also data- dána-. ата npm. XPh 36, 38, 39.
dat»adàna- sb. ‘sanctuary of false divinities’ (8147.1, $160.Ib): daiwa- + dána- (in derogatory sense, ‘den’, ace. to Hz. AMI 8.75, ApI 181). dawadénam asm. XPh 37f (written -d'av*m? in second copy, cf. $51, Lg. 13.293).
daug- vb., see hadugà-.
dauStar- sb. ‘friend’: NPers. dost, Skt. jostdr- ‘loving’; agent-noun ($154.IT) to root daus-, Av. zaos- ‘enjoy’, Skt. jus-, Lt. gustat ‘tastes’, NEng. choose, pIE *ĝeus- (S88). daustà nsm. (§124.5, 6186.1) DB 4.56, 69, 74; DNb 7,8, 12; DS} 4.
dacara-, see tacara-.
dáta- sb. ‘law’: Av. dáta-, NPers. dat; nt. ptc. to *dd- (8122, §242.1I). See also Vahyazdata-. dātam nsn. DNa 21; DSe 20°, 37; XPh 18f. dala isn. (less probably absn., §172) DB 1.23; XPh 49, 52. [d]ātā npn. DNb 58.
datasa, KT's reading, with first and third characters uncertain, DB 4.71f; read шаш, q.v.
Détuvahya- sb. (§164.V) ‘Datuvahya’, father of Megabyzus ($168.10): Elam. da-ad-du-man-za, АКК. 2a--tu--a; cf. Iz. AMI 1.84n. Dät[u]- vahyahyü gsm. DB 4.85.
Dàdar&- sb. 'Dadarsh?', (1) an Armenian, (2) а Persian, satrap in Bactria: Elam. da-tur-%-18, Akk. da-da-ar-5u. Репу. of darš- ‘dare’, with re- duplication; Skt. dadhyst- ‘bold’ ($30, §76.III, $152.1, §164.1V). Раат пет. DB 2.29, 31f, 48; 3.18, 15. Dédarsim asm. DB 2.33, 38, 44.
idan- vb. ‘flow’: Skt. dhdn-vati. датира] DZe 9 (or danu[taiy] mid., Wb. KIA 104, after al- ternative suggestion of Bthl. AiW 683); $216, §216.n1.
*dan- vb. ‘be acquainted with’, see z$nà-.
dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
ldar- vb. ‘hold; (intrans.) dwell’: Av. dar-, Skt. dhr-, Lt. fir-mus ‘firm’, Lith. daryti ‘to make’, pIE *dher- ($76.11, $122). See also Upadarma-, Dérayavau-, duruva-, Vidarna-. Present stem dàraya- and conj. 58215. dárayümiy Ist sg. (226.1) AmH 5f; AsH 11, 14; DB 1.26; DPh 4f;
189
DNb 14; DH 4. dárayatty DNd 2 (reading cer- tain, acc. to Wb.’s marginal note to AbkSGW 29.- 142). dàáraya"liy 3d pl. (82321) XPh 23f, 24f. adāraya imf. ($2281) DB 1.85;2.9,3.23; DNa 41; DSe 20Ї°; XPh 19; adáraiya DNa 22 ($48;
```


## [2026-09-07T20:40:23.379Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'P[aá]rsa- ?sb|Par[fθ0]ava- ?sb|Parsa- sb', p):\n        print('leaf',i)\nfor i in range(216,222):\n    print('==== leaf',i)\n    print(pages[i][:4000])\nEOF"
}
```


### [2026-09-07T20:40:25.074Z] TOOL RESULT

```
==== leaf 216
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
naiba- adj. ‘beautiful, (religiously) good’, re- .
placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
naucaina- adj. ‘of cedar’: NPers. nóZ, пдѓап ‘pine cone’; therefore naucaina- ‘pine-cone-shaped’ ($147.11), appropriate to the cedar (König, Burg- bau 53-4; Hz. AMI 3.58). naucaina nsm. DSf 30f. |
nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
7 ыйсы аЙ eet NUI ШЕЛ, АМАА а аз an ШО. Дені. Zr é
DD де 5... anes
LEXICON
‘corpse’, Lt. acc. nec-em ‘destruction’, nocet ‘harms’, pIE *nek- (887).
vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
Nadi"labaira- sb. ‘Nidintu-Bel, a Baby- lonian rebel: Elam. nu-ti-ut-be-ul, Akk. ni-din-ti- йе] (§75.V, §76.V, $107). Naditabaira пзш. DB 1.77, 92f; 2.1; 4.12; DBd 1. Naditabairam asm. DB 1.80, 84; 24, 5. Naditabairahyà gsm. DB 1.85, 89, 95.
napüt- sb. ‘grandson’: Av. Skt. napat-, Lt.’
nepos, pIE *nepot- (875.1, §110, $142). napa nsm. (§124.5, §188.1) AmH 4; DB 1.3; DBa 4; А:Ра 16°.
Nabukudracara- sb. ‘Nebuchadrezzar’, son of Nabonidus; name assumed by the rebels Nidintu- Bel and Arkha: Elam. nab-ku-tur-ra-sir, Akk. nabu-kudurri-ugur (82, 833, §75.V, $128, §163.- VD. Nabukudracara nsm. DB 3.80f, 89; 4.14, 29f; DBd 3f; written Nabukuracara ($52.V) DBi 5f. Nabuk*dracara (822) DB 1.78f, 84, 93.
Nabunaita- sb. ‘Nabonidus’, last king of the New Babylonian Empire, 556-39. в.с: Elam. na- bu-ni-da, Akk. nabü-na'id; Gk. Aaßivnros (Hat. 1.74, ete.). Nabunailahyà gsm. DB 1.79. Na- bunaitahya (§36.1Vb) DB 3.81; 4.14, 30; DBd 5f; DBi 7f.
niman- sb. ‘name’: Ау. náman-, NPers. пат, Skt. náman-, Lt. nomen, pIE *nómen-, cf. Gk. буора, NEng. name ($109, $110, 5155.11). See also Andmaka-. náma^, suffixless lsn. used with mase. and nt. generic nouns to denote specification ($112, $187, §251C, §312): DB 1.28, 30, 36, 37, 74, 77, 92; 2.8f, 9, 14°, 19, 22, 29, 38, 49, 65, 79, 82, 95; 3.5, 12, 13, 22 bis, 31, 34, 44, 51, 56, 78, 84; 4.8, 10, 12f, 15f, 18, 20, 23, 26, 29, 83 bis, 84 bis, 85, 86°; 5.5, 8, 27; DSe 45°; DSf 31, 46; Юле 9; XPf 18, 19; А?Не 14f; A?Pa 19, 20; Sa 2f. nama, either asn. *ndmá ог lsn. лата” (with lengthened grade), specialized for similar use with fem. generic nouns because of similarity of end- ing ($67.1T, $187, §249L, $312; cf. Tm. Lex. 105,
193
with lit.; not with Foy, KZ 35.11, 37.505, IF 12.172n, nor with Debrunner, IF 52.153): DB 1.58, 58f; 2.271, 39, 44, 52, 59, 72; 3.11, 23, 61, 66, 12, 19; 54°.
nay- vb. ‘lead’: Av. nayeitt, Skt. náyati. Conj., §213. anaya imf. DB 2.88; 3.88°; 5.12. [ajnaya" 3d pl. imf. ($232.11) DB 5.28. anayatá imf. mid. as pass. ($235.П) DB 1.82, 2.73; 5.26". Some or all of these are possibly ànay-, from à + nay-. | fra- + nay- ‘lead forth, provide’: fránayam Ist sg. imf. ($226.11) DB 1.87.
nar- sb. ‘man’: Av. Skt. nar-, Gk. дир, cf. Lt. Ner-6; i
==== leaf 217
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
nij- verbal prefix ‘away’: sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niş- ($120); with verb ay- ‘go’.
nipadiy phrasal adv. and prep., ‘on the track of, close after’: prep. ni- + loc. padiy, to pad- ‘foot’ ($76.11, $136, $140, $191.1V). тарайту adv. DB 2.73; prep. with acc. DB 3.73.
nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
194 OLD PERSIAN
niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
niyaSadayam, see had-.
Nisdya- sb. ‘Nisaya’, a district in Media: Elam. nu-is-fa-ja, Akk. ni-is-sa-a-a (5116). Per- haps from ni- ‘down’ + sdya-, to root Av. st- say- Tie’, Skt. §-, Gk. кт. ‘Ties’, pIE *kei-. Nisdya nsm. DB 1.58. |
niXadayam, see had-.
nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
pä- vb. ‘protect’: Av. pà-, pres. рйи, РЫ. pátan, Skt. pà-, pres. pati (ablaut, §122). See also zíacapüvan-. apayaiy lst sg. imf. mid. (Ву. BSLP 33.2.151-2; Kent, Lg. 9.42; S71, $214, $233.1II; wrongly to Skt. pt- ‘swell’, Wb. ЖА 41.820-1) XPf 39. padiy 2d sg. imv. (5208, §237.1) DPe 21f. pätwv (§208, $297.IT) AsH 12, 14; DPd 16; DPh 10; DNa 52; DSe 50; DSf 57; DS} 6°; D8n 2°; роз 7°; DSt 8°; ОН 8; XPa 18, 20; XPb 28; ХРе 12, 15; XPd 18; ХР 45, 48; XPg 13; XPh 57; Хе 5^; XV 25f; А:Ра 226; D'Sa 3; A?Hb^; A?He 19. pätw 3d pl. іту. (§237.1T) A'Sa 5°; A’Sd 4; А?На 6°; A?Pa 25. pála пзш. past ptc. pass. (§242.IT) DPe 22. pati- + pã- mid. ‘protect one’s self against’, with Ласа + abl.: райїрауаш@ (828; not wrongly written, despite MB Gr. §69) 2d sg. imv. mid. ($71, §214, 5297.11) DB 4.38.
paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
paišiyā- sb. ‘script, written text’: deriv. of pai- (§89, §144.V). See also Parsiyduvada-. ри nsf. DB 4.91 (conj. of Kent, JAOS 62.268).
PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps, 
==== leaf 218
with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and Sacred Writings’ (on Pasargadae, ef. also Kónig, RuID 66; but Hz. ApI 275-6, modifying his view ш AMI 1.86n, takes prior element to be pati-, pati- becoming pa&-, with epenthesis; Bthl. AiW 907-8 normal- izes Piši- after the Akk., but gives no etymology). Paisiydwddim asf. DB 3.42. Parsilydluvadayd absf. DB 1.36f.
pa|camàm] adj. ‘fifth’, asf.: wrong restoration of Wb. at DB 5.8 (ef. Kent, JNES 2.109).
pal- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. vérerat, Lt. рені ‘seeks’, pIE *pet-.
ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
66): udapalatà imf. mid. (§84, 8213, 5285.П) DB 1.36, 38, 74, 78; 2.10, 14f; 3.24, 79.
patiy adv., prep., prefix ($140.I, $1911): Av. рай, Gk. (dial.) rori, pIE *poti, cf. pIE *proti in Skt. prát, Gk. Hom. троті, classical rpés (cf. Lg. 20.9-10).
(1) Adv. ‘thereto, again’: DB 2.37, 48, 57; 3.04, 71. pati-maty ($186) DNb 32f.  nai-pati-mà ($133, 5186) DNb 20. yadi-patiy (8136) DNa 38. (ya-patiy XPa 15; XPf 40f.
(2) Prep. (8271) with ace.: DB 52 ‘during’; DNb 22 ‘against? (Hz. ApI 273 reads par[slaiy ‘in court’, sb. to root fraé-); postposed DB 2.62 ‘on’. Encl., with ace. ‘during’ DB 1.20 (8133, $136); with inst. ‘near, at’ DB 2.16°, 3.26; with loc. ‘on, upon’ DB 2.76, 91; 3.52, 92. Ву. BSLP 42.2.70 takes all these as adverbs except DB 2.62, DNb 22.
(3) Prefix with verbs avahya-, ay-, ziay-, jan-, рӣ-, fraf-, d-bar-, zbü-; prior element in nouns palikara-, Patigraband-, perhaps Pátisuvari- and
"* 2 - -
also patiš, patisam.
patikara- sb. ‘picture, (sculptured) likeness’: .
РМ. patkar-, NPers. pátkür-;.pati- + kara- to root
as sata jeu iit И ЗАК
pores agent iain ee Seeman Re NE SS a cet ras ЧЕК ЧАС ve NEMPE
LEXICON 195
kar- ($143.V). patikaram asm. DSn 1°. palikara apm. DB 4.71, 78, 77; DNa 41.
Patigraband- sb. ‘Patigrabana’, a town in Parthia: Elam. pat-t-ig-rdb-ba-na; from pati- + root grab- + suffix (833, $103.IV, §147.1). Pati- graband nsf. DB 3.4f.
Я patipadam phrasal adv. ($191.17) ‘on its base, in its own place’: pati- ($186, $1401) + aec. padam (see pada-; 76.111, $122). DB 1.62.
palis prep. with acc. ‘against’: pati- + adv. -s, ef. Lt. ex, abs, ops- in os-lendó, sups- in sus-tined, Skt. nt and nis, Gk. ато iy, audi audis. See also patisam. DB 1.93; 2.33, 38, 43f, 52f, 58, 67; 3.36, 43, 65.
patisam adv. ‘in addition’: extension of patiš, ef. for formation Ose. per-um ‘without’ to (Lt.) per, and for meaning Gk. трд ё ‘and besides’, Lit. atque from *ad-que ‘and thereto’ (OP patiy, Gk. тро, Lt. ad agree in marking something as an ad- dition). patišam DB 4.89 (p* probable but not certain KT); (раат DB 4.90 (restoration of Konig, Klotho 4.45; see also Kent, JAOS 62.267- 8).
Pàtiwvari- adj. ‘Patischorian’ ($167): Elam. ba-ul-ti-i$-mar-ri4$, АКК. pa-id-di-if-hu-ri-i$, Gk. (рі) llaracxopes. Perhaps pAr. *pati-, with vriddhi ($126), + *suára- ‘(of the plain) before the Hvara Mts.’ ($117), with combination (8$140.VI) of sandhi forms (so Hz. ApI 183-4, who however disregards the d in the penult of the OP). Ран паті nsm. DNe 1.
. раві- sb. ‘path, way’ (676.1, §152.1, $179. III): Av. pab- patá-, Skt. panthan- path-. райт asf. DNa 58.
pad- sb. ‘foot’: Av. Skt. pad-, Gk. roô-, Lt. ped- ($142); in mipadiy, cf. also pada-, páda-, pasti-.
pada- sb. 'footing, step, station': Av. paóa- ‘foot (as measure)’, Skt. padd- ‘step, footstep, place’, Gk. aé&ov ‘ground’; extension of pad- ($143.- П). In Garmapada-, patipadam; see also pad-, рӣйо-.
рӣйа- sb. ‘foot’: LAv. páóa- ‘step, pace’, Skt. pida- ‘foot’, Gt. fotu-, extension of stem in pIE nom. *pdd-s, acc. *pod-m, seen in Gk. Dor. тах ($76.11, §122, $126, $148.П). Cf. also pad-, pada-. püdaibiyà idm. ($189) DNb 41.
par- vb. ‘communicate’: Av. *par- ‘hindureh-, hintibergehen’ (ВЕ. AYW 851), Gk. weipw 
==== leaf 219
‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte. pass. ($242.1) DNb 54 (dubious con]. of Kent, Lg. 15.167, 178-4).
ipara- adj. ‘later’, possibly in hyáparam (q.v.) : Av. para- ‘farther’, Skt. pára- ‘distant’, Gk. qépav ‘beyond’.
nara prep. with acc. ‘beyond’ (§32, $63.1): Av. pard ‘before’, Skt. purds ‘before’, Gk. таро ‘before’; DPe 15; DPh 5; DH 4, See also para- dayadàm, paradraya.
parü postpos. with acc. ‘along’, and verbal prefix ‘forth’ ($132.3): Av. ?pará ‘before’, Skt. purá ‘before, formerly’, Gk. rapá ‘alongside’: in avapard and with ay-, ar-, gam-, bar-.
parauvaty lsn. as sb. ‘in the east’: руи] "Ре 15, a misreading for pr? : d*r^ ye (uninseribed space between r* and y*) = para : dra ya; seeunder paradraya.
paradayadám sb. asf., perhaps ‘pleasant re- treat’ ($55.II, §148.1V): Аа 3. Possibly mis- written руат“ for p'rud*iljme = paridai- dam, Av. patridaéza- ‘Umwallung, Ummauerung' (Bthl. AiW 865), borrowed in Gk. тарабено ‘park’, cf. JAOS 51.229; or for p'r*d'id^am* = paradidam, from ?para ‘beyond’ + didá- ‘wall’ (q.v.), as ‘that which is beyond or behind the wall’ (ef. Scheil 21.93; Bv. BSLP 30.1.67 j'vadiy paradayadám ‘paradis de vie’).
paradraya phrasal adv. ‘across the sea’ ($44, $191.[V): рата ‘beyond’ + acc. draya ‘sea’. DNa 28f; DSe 29°; XPh 24. paradraiya (848) A?P 24 (Hz. ApI 142). As two words, para draya DPe 15 (Cameron, JNES 2.307-8).
parana- adj. ‘former’: deriv. ($147.11) of stem in OP ?para, para (cf. ВЕШ. AiW 854), Av. рагі, рагб, Skt. рига ‘formerly’ (hardly to be normal- ized parna-, with MB Gr. $267, to Gt. faírneis ‘old’). See also dumlaparanam. — paranam asn. as adv. ‘formerly’ DB 1.51, D'Sb 3.
pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
196 OLD PERSIAN
pariyana- sb. ‘superiority’: deriv. ($147.IT) of pariy, in meaning seen in Ау. pairi ‘vorne, über ... hin’, Skt. pári as prefix ‘much, excessively’, cf. Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, Sen 250). pariyanam nsn. DNb 52.
paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
paruva- adj. ‘being before in time or place’ (§35.1[): Av. paurva-, Skt. pürva-, pIE *pruos (868, $150), ef. Gk. Ion. трохоѕ ‘early’. See also paruviyata, paruviyaüd. parwā npm. ‘former’ DB 4.51. parwam asn. as adv. ‘formerly’ DB 1.9; DBa 15f; DSe 43°, 47; XPh 36, 39; paruvam- ciy DB 1.63, 67, 69.
parwnyata, adv. with preceding hacd, ‘from long ago’: *paruviya- (ie. *parvya-, deriv. of paruva-), Av. paouruya-, Skt. pürvyd-, + adv. suffix -la^, Av. -£ó, Skt. -tas, Gk. -ros, Lt. -tus asin funditus, pIE *-los ($191.11). C£. also paruviyatà. DB 1.7, 8, 45; DBa 11, 12.
[paruv|iyafà adv. ‘at first attempt’: *paruviya- (see paruviyala) + adv. suffix -0à, Av. -fa, Skt. -ihà ($191.ID). DSj 3 (conj. of Brandenstein, WZKM 39.49-51; ef. note ad loc.).
paruzana- adj. ‘having many men, or many kinds of men’ (‘having men of all tongues’, Wb. ZfA 44.165, after the Akk.): paru- ‘many’ + zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. poruvzandndm (523.1) XPb 15f; XPd 11. раги zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; XPh 9; XV 12.
Parga- sb. ‘Parga’, a mountain in Persia: Elam. par-rak-qa, NPers. Purg ($30). Parga лет. DB 3.44. |
partara- sb. ‘battle’ (as in Elam. and АКК. versions): extension of -r/n- s
==== leaf 220
tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69-4; not agency noun
‘fighter, foe’ as taken by Wb. KIA 90-1, Bv. Gr. $277; not paratara- ‘foe’, with Wackernagel, KZ 59.29-30, as compar. to [Skt.] pára- ‘distant’ = RV ‘enemy’). partaram asn. DNa 47.
Ратдата- (§29.n2, $31) adj. ‘Parthian’, also тазе, as sb. ‘Parthia’, a province of the Persian Empire: Elam. par-tu-ma, АКК. pa-ar-tu-á, Gk. IIapóià. Extension ($150) of stem seen with vriddhi in Pársa-, but with dialectal difference in the 0/s ($9. VT, 887).
(1) ‘Parthian’: Paréava nsm. DN iv; A?P 4. Par&avaibi$ ipm. DB 2.96. (2) ‘Parthia’: Paréava nsm. DB 1.16; 2.7, 92;
DPe 15; DNa 22; DSe 21°; DSm 8°; XPh 20.
Par8avai ism. DB 2.94° 96°; 3.5, 10. parna-, see duildparanam, parana-. ‘parsa- vb., see fraó-.
?parsa- sb. ‘court’, only in Hz. ApI 278; for his pa[r|saiy lsm. DNb 22, see under patiy.
Pársa- adj. ‘Persian’; also masc. as sb. ‘Persia’, a province of the Persian Empire: Elam. par-sin, АКК. pa-ar-su, Gk. Перо, Пероќа (§9. VI, $87, §126, 5143.11). See also Paréava-. `
(1) ‘Persian’: Pársa nsm. DB 1.49; 2.18, 19, 49; 3.18, 26, 31, 32, 56, 84; 4.16, 26, 83, 84 bis, 85 bis, 86; 5.8°; DPe 22; DNa 18, 46; DN i; DSe 12; DZe 7; XPh 12; A?P 1. Pérsam asm. DB 2.81; 8.2, 29f; DPe 21. Pàrsahyà gsm. DNa 13f, 43; DSe 13; XPh 12. Pérsé ism. DPe 8.
(2) ‘Persia’: Pársa пзш. AsH 3 (for loc., §52.1);
DB 1.14, 41; 2.7; DPd 6f; DSm 6°. Pársam asm. AsH 8f; DB 1.46; 3.33, 34; 49, 28; DZe 12. Pérsam-cé DB 1.66. Pürsá ism. XPa 14 (here ‘Persepolis’, acc. to Cameron, by letter; $166, 6166.1). Pürsà absm. РМа 18, 46f; DSe 17°; Юле 7f, 10; XPh 16. Parsa for lsm. AmH 2 (856.V, §314b; wrongly Hz. AMI 4.132-4, 8.17- 9, as instr. of extent); for пзш. AmH 5 ($53; not nsf. adj., as taken by Hz. AMI 820-1, 34). Pärsaiy lsm. DB 1.2, 34; 2.9; 3.23, 24, 28, 34, 52, 58, 71; DBa 2.
pasü prep. ‘after’, temporal with асе. and local with gen. (Bv. BSLP 33.2.153): Av. paséa, NPers. pds, Skt. paácá, isn. to stem in Lith. (dat.) adv. and prep. різки ‘behind, later, after’ (Foy, KZ 35.26); pIE *po as in Lt. po-lið, positus, Gk. &-vó, + *sg*é, inst. to root noun from *seq*- ‘fol- low’, Av... hacatte, Skt) Gdeate, Gk. trerai, Lt.
See nada lai baa a D Lo AMA tae io at OT IPE Ауаз a зз
~
LEXICON
sequitur (§105; Uhlenbeck, Etym. Wtb. d. altind. Spr., s.v. paced). The s in pasá is OP for Med. $c, Av. sé, from pAr. $c (Ву. Gr. §114; otherwise Mt. Gr. §114). Less probably pAr. *pas (Lith. pds ‘at, to’) from the same *po + adv. -s as in OP patiš, + -cà isn. of stems in -айс-, for -acã (from *-ncà) by influence of contracted forms like Skt. praca (*pra-acd) to ртайс- (*pra-atic-) ‘forward’, cf. similar analogical form in Skt. adv. nica ‘downward’ (for *ni-acd) to пуайс-. Hardly from *pas (as above) + -à after its opposite para ‘before’ (Bthl. AiW 879). Direct cognation with Lith. páskw: is eliminated by the second and third etymologies; with Av. pasta, Skt. paícá, by the third. pasã with gen. DB 3.32; with асе. XPf 31 and in pasdva (q.v.).
pasáva phrasal adv. (§191.IV) ‘after that, afterwards’: pasé + asn. ava (8181). DB 1.27, 30, 32, 33, 34°, 35f, 40, 43, 46, 54, 72, 731, 75, 79, 82, 83, 86, 91, 94; 2.1, 3, 4, 12, 16, 19, 21, 27, 31, 32, 47, 49°, 51, 52, 62, 64, 67, 71, 72, 81, 84f, 94; 3.1,4, 9, 12f, 15, 20, 25, 29, 33, 36f, 41, 50, 59, 70, 73,75, 81, 84, 86, 90f°; 4.5, 35, 91; 5.3, 6, 9, 10f, 13, 21°, 28, 25°, 29; DSe 48; DSf 25; DZe 10; XPh 36; XSe 3; XV 23; А:Ра 21°; Рр 4°. pasãva-šim DB 2.76, 90. pasdva-Saiy DB 2.88.  pasáva-dim DNa 33. pasdva-mary XPh 32.
pasti- sb. ‘foot-soldier’: Skt. pailt-, from pIE *ped- ‘foot’ (OP pad-) + suffix -t&- ($85, 5152.11; Wb. Grab 40, Hz. ApI 94-8). — pasti$ nsm. DNb 48, 45.
pilar- sb. ‘father’: Av. pilar-, NPers. pióür, Skt. pitd
==== leaf 221
r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II); see also hamapilar-. pita пет. ($86.П, $124.5, $186.1T) DB 1.4 bis, 5 bis, 6; 2.93; DBa 5, 6, 6f, 7, 8; DSf 12, 58; XPa 15; ХРе 12; XPf 16, 17, 19, 23, 31, 33, 42; XPg 7; X8a 2; XV 18; А!Ра 20f; D?Sb 4°. pica gsm. ($78, $124.5, $186.If) XPa 20; ХРе 14; XPf 35, 38, 47.
Pirdva- sb. ‘Nile’ (§75.V, $124.II, §166.V]): Pirdva пзш. DZc 9, in naming phrase, anacolu- thic for abl. after Ласа; either ‘Ivory River’, as deriv. adj. to piru- ‘ivory’, or possibly plural ‘The Tusks’ (JAOS 51.209).
miru- sb. ‘ivory’ (§75.V, 5153.1): Elam. pi- ru-§, Akk. pilu-, with cognates (or borrowings) in Eastern Asiatic languages (Przyluski, BSLP
197
27.3.220-2; Scheil, Rev. d’Assyr. 24.120; Bv. BSLP 30.1.62; König, Burgbau 66; Hz. AMI 3.67-8).  piruf пет. DSf 48.
pi-, vb., see paid-.
pisa- sb. ‘raft’: perhaps originally ‘cut mate- rial’, from root pazd- (8143.1II). різ ism. or isn., with collective meaning (§255), DB 5.24.
pisa- or paisa-, vb. stem, see paið-.
Putéya- adj. ‘man of Put, Libyan’ (§75.V, $/6.V, §144.HI); pl., ‘Libya’, a province of the Persian Empire (Cameron, JN ES 2.308-9) : Elam. pu-á-ti-ja-ap, Akk. pu-u-ta (Lg. 18.299, 15.165). Pulüya пет. A?P 27. Putāyā npm. DNa 29f; DSe 29°; XPh 28,
puça- sb. ‘son’: Av. puéra-, Ars. РЬ. рим, N Pers. pus, Skt. pulrá-, Ose. puclo-, рї *putlo- ($64, §75.1,§78,§148.1II). pucansm. AmH 3; AsH 4; CMb 2°; DB 1.8, 28, 39, 53, 74, 78, 79; 2.9; 3.25, 79, 81; 4.9, 14, 28, 30, 83, 84° bis, 85 bis, 86; DBa 3; DBb 6; DBd 6; DBh 7; DBi 8f; DPa 5; DPb; DPe 5; DPh 2; DNa 18, 14; DSa 2; DSb 10; DSe; DSd 2; DSe 12, 13; DSf 7; DSg 2°; DSi 2°; DS} 2°; DSk 3; DSm 2°; DSy 3; DZb 5f; DZec 6; DE 20; DH 2; XPa 10; XPb 20; XPe 9; XPd 14; XPe 4; XPf 14; XPh 11, 12; XPj; XPk; Х5е 2; XE 20; XV 15; A!Pa 15f; АЧ bis; D'Sb 2°; Аба 1, 2 bis, 3 bis; Ab; A?Sc 0° bis; А4 2; A?Ha 2°, 8, 3°, 4, 4°; А?Не 10, 11, 12, 13f, 15; A3Pa 18, 14, 15, 16, 18, 19, 20; Wa 7; Wb 8; We 9; Wd 9; Sa 8°, pucä npm. XPf 28; as nsm. А?НЬ (853; with -a after парӣ, acc. to Brd. WZKM 39.92).
farnah- sb., see Vidafarnah-.
fra- prefix ‘before, forth’ (as prep., not found in OP): Av. fra, Skt. pra, Gk. тро, Lt. prü-fessus, Gt. fra-, pIE *pro ($33, $01, $75.II, $106, $132.3). Found with verbs а1$-, jan-, nay-, var-, má-, sá-, haj-; in nouns framdtar-, framānä-, Fravarti-; in phrasal adv. fraharavam; with suffixes and exten- sions, in fratama-, fratara-, fratara-, fravata, fraxa-.
fratama- adj. ‘foremost’: fra- + superl. suf- fix -lama-, Av. fratama-, Skt. -tama- (4190.11). fratama npm. DB 1.57; 2.77; 3.48f, 51, 74, 90°, 91.
fratara- ad). ‘prior, further’: fra- + comp. suf- fix -tara-, Av. fratara-, Skt. adv. pratardm, Gk. mpotepos (§106, 5190.11). " fratara ism. DNb 38 (Sen 249 needlessly takes as error» for frataram).
198
frataram asn. XPg 11; adv. ‘previously’ DB 3.26, A!Pa 21.
fratarta DB 3.26, incorrect reading for fra- taram (Cameron).
fral- vb. ‘ask, examine, investigate, punish’: Av. fras-, Skt. pra-, Lt. precor, pIE *prek-, with inchoative present, *prk-ske-, OP parsa-, Av. poro- saiti, NPers. pursdd, Skt. precháti, Lt. poscit. Cf. also ufrasta- ufrasta-. parsdémiy 1st sg. (830, $97, $130, $212, 5226.1) ОМ 19. aparsam Ist sg. imf. ($122, 5182.3, $212. $226.П) DB 1.22; 4.67, parsü 2d sg. imv. (8212, 5237.1) DB 4.38, 69. . frabiyaiš opt. pass. ($220, $228.П, $228.11) DNb 21 (not desid. fut. pass., as taken by Hz. Арі 167). pati- + parsa- ‘examine, read’ (on meaning, Bv. DSLP 31.2.71-2): patiparsühy 2d sg. subj. (§222.- II, $227.I) DB 442.  patiparsátiy subj. ($222.11) DB 4.48.
frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl. -thama- in Skt. prathamd- ‘first’. Cf. also uradara
```


## [2026-09-07T20:41:19.536Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor n in (400,401,402):\n    print('=== leaf',n)\n    print(t[n][:2500])\nEOF"
}
```


### [2026-09-07T20:41:20.902Z] TOOL RESULT

```
1545
=== leaf 400
� or ‘lunch’, fr. MLG vrokost, fr. vré ‘early’ and kost ‘food’ (5.12).
Sw. kvdllsvard ‘supper’ fr. kvdll ‘eve- ning’ = ON kveld, and vard = ON verdr ‘meal’ (5.41).
OE morgenmete, wundernmete (cf. above), efenmete, lit. ‘morning-, noon-, evening-food (meal)’.
OE wist ‘food’ (5.12) and feorm ‘food, meal’ (5.12, 5.41) are used for prandium and céna respectively in Lk. 14.12.
ME diner, NE dinner fr. Fr. diner (above, 2).
ME soper, NE supper, fr. OF r. soper (above, 2).
ME (late) brekfast, NE breakfast, epd. of break (ME breke) and fast. Cf. VLat. *disiétinadre, Fr. déjewner, above, 2.
NE lunch, of which luncheon, though quotable from a few years earlier, is an extension, was first used of a ‘hunch, hunk’ (of bacon, bread, etc.), and was prob. a colloq. blend of lump and hunch. Cf. NED s.v.
Du. ontbijé ‘breakfast’, fr. MDu. ontbiten, like OE onbitan ‘partake of’, epd. of bitan ‘bite’. Similarly OHG imbiz (gl. Lat. prandium), epd. of bizan ‘bite’, whence NHG imbiss ‘smack, lunch’.
OHG gowma ‘meal’ (5.41) also renders Lat. prandium and céna.
MHG oruostiicke (also vruoessen), NHG friihstiick ‘breakfast’, fr. vruo ‘early’ and stticke ‘bit’.
MHG, NHG wmittag(s)essen, -mahl ‘midday meal’, MHG abentessen, -mal, ~brot, NHG abendessen, -brot ‘evening meal’ (abendmahl mostly for the Lord’s Supper), all obvious epds. of ‘midday’ or ‘evening’ with ‘food, meal, bread’. For the NHG local usage, cf. Kretsch- mer, Wortgeogr, 63 ff., 336 f,
. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
356 SELECTED INDO-EUROPEAN SYNONYMS
5. Lith. pusryciat (pl.) ‘breakfast’, epd. of pusé ‘half’ (18.34) and rytas ‘morning’ (14.34), so lit. ‘midmorning’ (meal).
Lett. bruokastis ‘breakfast’, fr. MLG vrokost (above, 4). Muhl-Endz. 1.342.
Lett. azaids ‘midday meal’, also local- ly ‘breakfast’ or ‘lunch’, etym.? Miuihl.- Endz. 1.233.
Lith. pietiis (pl.) ‘midday meal, din- ner’, orig. ‘food’: ChSl. pitéti ‘feed’, pista ‘food’, Skt. pitu- ‘food, drink’, etc. (5.12).
Lett. pusdiena ‘midday, noon’ (14.45), hence pl. pusdienas ‘midday meal’. Mihl.-Endz. 3.425.
Lith. vakariené, Lett. vakarinas ‘sup- per’, fr. Lith. vakaras, Lett. vakars ‘evening’.
6. SCr. zajutrak ‘breakfast’, 
=== leaf 401
Russ. zauirak ‘breakfast’ or ‘lunch’ (in which case ‘the first meal’ is pervyj zavtrak ‘first breakfast’, or often simply ¢aj ‘tea’), epd. of za ‘at, for’ etc. and jutro ‘morning’ (14.34).
Boh. snidane, Pol. sniadanie ‘break- fast’, ecpd. of siin- ‘with’ and jad-, IE *ed- ‘eat’. Berneker 273,
ChSI. obédii (in Gospels renders Gri. &picrov ‘the midday meal’, while Grk.
5.51 BREAD Grk.  dpros Goth. Alaifs Lith. duona NG Poul ON braud Lett. maize Lat. panis Dan.  Odr¢d ChSl.  chlébit It. pane Sw.  bréd SCr. kruh, hijeb Fr. pain OE hlaf (bréad) Boh.  chléb Sp. pan ME brede Pol chleb Rum. piine NE bread Russ. chleb Ir. _bairgen, aran Du. brood Skt.  (apipa-, piipa-) Nir. aran OHG hleib, brat Ay. ae W. bara MHG brat Br. bara NHG brot
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
detrvov ‘the evening meal’ jg Tendereq by vecerja; but it is entered in the list under ‘dinner’, since it is the Principa} meal in Slavic, as in) SCr, objed, Po] obiad, Russ. obed, all fr. ob(tt)jad-, per. fect. cpd. of jad-, IE *ed- ‘eat’, Berneker 273.
SCr. ruéak ‘meal’ (5.41), also esp. the principal meal, the noon ‘dinner’, Hence also doruéak ‘breakfast’, cpd. with do. ‘until, beside’.
ChS]. veéerja, SCr. vegera, Boh, vedere ‘supper’ (Pol. wreczerza, Russ, vederja now mostly of the Lord’s Supper), fr, ChSl. vecerii, etc. ‘evening’ (14.36),
Pol. kolacya ‘supper’, fr. Lat. collatis, through a special use among the monks, Cf. It. colazione, above, 2. Briickner 244,
Russ. uzin ‘supper’ : SCr. uzina, Pol. juzyna ‘afternoon or evening lunch’, orig, at noon, fr. jug ‘south’ in sense of ‘noon’ (cf. NHG mittag for ‘south’). Brickner 210.
7. Skt. prataraga- ‘breakfast’, epd. of pratar ‘early morning’ and ac- ‘eat’, But in general Skt. bhojana- ‘meal’ (5.41) was used for any meal.
Av. siirya-, xsafnya- ‘morning, night meal’, fr. siér- ‘morning’, xsapan- ‘night’. Barth. 550, 1586.
pooD AN » ag being the most
om ‘bit, piece’. ae : e shaped ‘ae paked in 2 pan, and this Joat of brea ted in their source. Rela- be reflec 3 of yeast in leavening i u Gme. group Seas doubtful.
1, Grk. épr0s; generally called Oh Sir But the deriv. Tr Gea a
=== leaf 402
papigne Von, fit, prepare’ 1s possible, euuher ei the general sense of prepared (Prellwitz), or through the literal sense as applied to the loaf ‘fitted’ in the bak- ing pot (xXtBavos). For dpros is, from Homer down, distinctively the ‘loaf’, pl. pro ‘loaves’, normally of wheat bread (in Hat. 2.92 of Egyptian loaves made from lotus-root).
The more common diet of the popu- lace (cf. Ath. 137e, etc.) was the pata ‘parley-cake’ (5.52).
In NG Gpros is used of the conse- crated bread in the church, but other- wse displaced by yout, fr. late Grk. Venloy, dim. of Ywyds ‘bit, piece’ : pay a, Yonlov is already a, ‘bit of bread’ ce ee ‘Sop’ in the NT, Jn. the ae rue occurs: frequently in translated eo is” commonly Part at least is alr F ainties ; but in
* Passages quot 1 y simply ‘bread’. gan, so . oted in Moulton-Milli- eee we ee Kretschmer, Glotta
b. buké ‘bread’, fr. Lat. (as Byg ee mouthful, mor / 2 a. '
Teyer, Alb, Etym, we, ss
Some
» Lat, mans Orig, fg me (> Romance words),
feed’ © the root of Lat. pascere
51g) ePulum ‘fodder’ (8.12), BmouLMt ne’ NE food, ete.
Digitized by Arya Samaj Foundation Chennai and eGangotri
D DRINK; COOKING AND UTENSILS 357
3. Ir. bazrgen, W., Br. bara : OE bere ‘barley’, Lat. far ‘spelt’, etc. Walde-P. 2.134. Walde-H. 1.455. Pedersen 1.101.
Ir. ardn, prob.: Ir. arbor ‘grain’, root connection? Stokes 16 (but re- semblance to Grk. apros accidental).
4. Goth. hlazfs, OF hlaf (NE loaf), OHG (h)leib (NHG laib), etc., the old Gmce. word for (loaf of) ‘bread’, orig. ‘loaf’ as in ON Aleifr ‘loaf’ braud-hleifr ‘loaf of bread’, etym. dub., perh. : Grk. k\tBavos, ‘earthen pot for baking bread’, without known root connection. Walde- P. 1.499. Feist 260.
Hence as loanword (less prob. fr. a common source) the general Slavic word, ChSl. chlébt%i, etc., also Lith. kliepas (from WhRuss.), Lett. klatps (fr. LG) ‘large loaf of bread’. Berneker 389. Stender-Petersen 297 ff.
ON braud, OF bréad, OHG brdt, etc., becoming the general Gmc. word at the expense of the preceding, is commonly derived fr. the root of OE bréowan ‘brew’, etc., as if connected with the use of yeast. So Walde-P. 2.168, Falk-Torp 112, Schrader, Reallex. 1.166, ete. But more probable is the view preferred in NED s.v. bread, that the development is from ‘bit, morsel’ (cf. OE gl. bréadru ‘frusta’ and the Northumbrian bréad = OE bitan, Vulgate buccella, Grk. Ywptov in Jn. 13.27, 30; also = aprov, Vulgate panem in Jn. 6.23), just as in Grk. Yo- ulov (above, 1), SCr. kruh (below, 6), and Sc
```


## [2026-09-07T20:41:21.074Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- PHD pahlaw\"; grep -n -i \"pahlaw\\|pahlav\" PHD.txt | head -20; echo \"--- NYB\"; grep -n -i \"pahlaw\\|Pahlav\" NYB_vol2_glossary.txt | head -20; echo \"--- BRT parθ\"; grep -n -i \"parθava\\|par0ava\\|parθav\" BRT.txt | head -20"
}
```


### [2026-09-07T20:41:21.208Z] TOOL RESULT

```
--- PHD pahlaw
1:A CONCISE PAHLAVI DICTIONARY
13:THE need for even a short Pahlavi-English dictionary has been obvious for many years, particularly to would-be students of the language. The glossarial part of Professor H. S. Nyberg’s Manual of Pahlavi is still eagerly awaited, five years after the publication of Part I, although the ‘archaistic’ tradition of transcription followed therein is no longer universally acceptable. With the partial material at present available, every serious student still has to compile his own dictionary, a formidable task with Pahlavi and made more so by the plethora of different systems of transcription in print. The present dictionary, admittedly introducing yet another transcription, is intended first to relieve the stranger to Pahlavi of the necessity of covering what is now well-travelled ground—the commonest 4,000 simple words— without a unified map, and secondly to urge the practical value of this ‘Sasanian’ transcription for his journeying further. To have included etymologies and textual references would have changed the emphasis of the work, turning it from a map to a historical atlas-cum-gazetteer, besides retarding its appearance unduly. Such a complete dictionary of Pahlavi is nowhere within sight and must remain so until many more texts are adequately edited.
14:For his good counsel on what to include in the dictionary I am most grateful to my friend Dr. P. Gignoux of Paris, for without him many common words would have slipped through my net. Most of the labour of compiling the English index, which will surely be appreciated, was undertaken by my wife. The debt I owe to the teaching of the late Professor W. B. Henning, in connection with Pahlavi and all things Iranian, cannot be expressed in words.
19:ADDENDA ET CORRIGENDA DICTIONARY ENGLISH-PAHLAVI INDEX APPENDIX
24:ALMOST every published list of Pahlavi words contains a number of entries of doubtful nature, the uncertainty lying either in their form, their meaning, or even, occasionally, their very existence. The purpose of this dictionary is to provide the student with a representative vocabulary of Pahlavi in which such uncertain words have been reduced to a minimum and marked. It differs from its predecessors in that the Pahlavi words are given in a phonemic transcription representing, as far as it is deducible from the evidence, the pronunciation they would have had in the third century of our era, the period of the rise of the Sasanian empire. The reasons for this departure from the 'archaistic' tradi- tion of Pahlavi studies I have given elsewhere.! If one reason stands out it is that of practicality, as most corroborative evidence comes from this period.
25:'To reduce the number of doubtful words it has been necessary to concentrate on the simpler vocabulary of such texts as the Kārnāmag i Ardaxsir, Dádestán i Ménog i Xrad, Arda Wiráz nāmag, Bundahisn, and the Pahlavi Texts edited by Jamasp- Asana. Although I have also drawn upon the Pahlavi versions of scriptural texts (Vendidad, Yasna, and Vispered), most of their very special vocabulary has been omitted. So have the many nonce-words and ad hoc compounds of religious texts such as the Dénkard, since it is generally a simple matter to analyse Pahlavi compounds, given the elements and provided that the rules of their construction are understood. Those words calling for inclu- sion whose form or meaning remain doubtful are marked with an asterisk.
26:By its nature the dictionary cannot claim to contain the entire vocabulary of any particular text. Nor is there any express inten- tion of presenting new solutions to the many problems remaining in the Pahlavi texts. Rather the readings of many scholars have
27:r ‘Notes on the transcription of Pahlavi’, Bulletin of the School of Oriental and African Studies, xxx, pt. 1 (1967), 17--29.
31:'The script of the Pahlavi books derives ultimately from that of the official Aramaic of the Achaemenian empire. In the course of time, however, a high degree of ambiguity has developed in the script. Table I shows the development of the letters from Imperial Aramaic (with the transliteration and names of letters commonly used by Semitists), through the distinct forms used in the Parthian and Persian inscriptions of the third century A.D., and the archaic manuscript forms of the Psalter fragment (about seventh century),! to those of the Zoroastrian books. In addition to the multiple values of the letters listed, some of them may represent combinations of letters in certain contexts, e.g. - or 35 for 3+».
36:TABLE I C Imperia | Jet | Pahlavi ep: „M c6 Аз As T A b (bēt) J | — — _) 8 g(gimel) А | g EY n 5 d(dālet) — $9 | 7 3 E eh h (hà) 7) ot се ed » wem Ж. | 2 2 L | z (zayin) ) ) $ € $ ken ]7) | N gv N =? t (të) O уу £ y (vod) x | ) 4 a3 au кыр y | 7 3 ) $ Llame) G y 1 L N nom 5| D| + < pen 05 | 2 |} | 6 рм s(samk) АЈ /7 D A3 V ‘ (ауіп) v 7 = м = W у р (pē) 2 ^» Q a д s(sādē) у y =D tv | es C. q (dčf) P kel = т | -m = ay r (re) Y uL "ORE м aši ap Gin) Ҹи б 22. x PS ET t (tàw) A D y Ki y
40:It is common practice to distinguish the Semitic ideograms in Pahlavi, from the Iranian elements, by transliterating them in capital letters. Thus the same letters va are transliterated lhyk' when they stand for rahig ‘child’, but LHYK! when they represent the ideogram for dür 'far'. However, as the ideograms are often much distorted and disguised forms of the original Aramaic words, it is sufficient for practical purposes to trans- literate them by means of a simplified system.
42:Pahlavi letters are often distorted, or joined irregularly, in such a way that they coincide with other letters, so producing even greater ambiguity. The commonest distortions are here noted by under- or over-lining the letter value intended. ‘Thus:
59:The orthographic principles followed, in seemingly haphazard permutation, in the writing of Pahlavi, besides the ideographic, include the phonetic (within the limits of the alphabet), the his- torical, the pseudo-historical, and. others so indeterminable as scarcely to merit the name. The establishment of the original spelling of a word, therefore, very seldom reveals its pronuncia- tion. To determine this it is necessary to examine all the available comparative evidence.
63:1 But see Kaj Barr, ‘Remarks on the Pahlavi ligatures JO and ў’, Bulletin of the School of Oriental Studies, viii, pt. 2 (1936), 391-403.
69:In seeking an unknown word, or one known only in another transcription, it may be necessary first to find it in the Pahlavi key. The English-Pahlavi index is intended to serve as an aid to memory, and for tracing synonyms, etc., but is emphatically not an English-Pahlavi dictionary.
80:Pahlavi words are always given in bold type. The few entries in ttalics are concessions to another transcription, made for reference.
84:(i) The transliteration of the Pahlavi spelling. In the case of ideograms this is followed immediately by an indication of the Aramaic (A) origin of the spelling. With verbs this can seldom be given more closely than by the form of the Aramaic root.
85:When the Pahlavi spelling of the present stem of a verb coin- cides with part of that of the infinitive, however much they differ in transcription, the transliteration is given in abbreviated form, with a hyphen. Thus skwp-tn' denotes ‘infinitive skwptn' (= &kuftan), present stem kwp- (= škēf-), YMY TWN-tn
89:For ‘learned’ words taken from the Avesta the form which the Pahlavi represents, however corruptly, is quoted (as ‘= Av,').! In such cases the Pahlavi transcriptions are more hypothetical than usual, since they can be no more than probable representa- tions of the contemporary pronunciation of these words.
91:After the vertical stroke the corresponding forms from Mani- chaean Middle Persian (M) and/or Parthian (P) are given wherever possible. The appearance of only a Parthian form does not necessarily imply that the Pahlavi word is of non-Persian origin. It may be that the identical Middle Persian form is not attested in Manichaean script.
--- NYB
2:A MANUAL OF PAHLAVI
13:HENRIK SAMUEL NYBERG A MANUAL OF PAHLAVI
18:The second volume of my Manual of Pahlavi appears at quite a long interval: ten years after the first. The main reason has been the extraordinary amount of fundamental linguistic problems presenting themselves within almost every word, each requiring lengthy and painstaking research. My advanced age has also somewhat impaired my efficiency. -
20:Throughout the text— wherever it has been possible—I have confronted the Book Pahlavi words with their equivalents in Manichean West Iranian, Old Iranian (Avestan, which must in absence of other sources stand for Old Iranian in general) and Old Persian. They have been measured against other West Iranian languages and dialects down to New Persian; last but not least against the Middle Iranian loanwords in Armenian and Aramaic. Etymologies are given only within this framework; other Indo-European languages have been only occasionally quoted.
21:My linguistic analysis has been greatly aided by ihe new and revolutionary insight into the character of Middle Iranian bestowed by the Turfan texts. Thanks to them we have an incomparably firmer grasp of Book Pahlavi than was ever possible before. This glossary is therefore closely linked to the epoch-making research done by the generation of W. B. Henning, H. W. Bailey, E. Benveniste, H. H. Schaeder and others.
24:It goes without saying that I have taken advantage of the useful Special vocabularies composed by Kapadia (Vendidad) and by Dhabhar (Yasna- Visperad), beside his very solid and reliable investigations on Book Pahlavi, and of the special glossaries produced during the new phase of Iranology heralded by the Turfan texts.
38:The Aramaic ideograms used in this Manual are listed here, together with a pre- liminary analysis of the Aramaic lexical material from which they derive. From an Aramaic point of view, most of the forms in which the verbal ideograms appear in Book Pahlavi (as well as in the inscriptions and in the Psalter) are spurious, fabricated as they are by Iranian-speaking scribes and hence without any linguistic foundation. In fact, only impf. forms of the type YKTLWN = YIQT'LUN and some few other forms can claim to be genuine Aramaic. The intricate process by which the Iranian scribes transformed Aramaic forms into purely graphic signs will be dealt with in my new edition of the Frahang i Pahlavik. Here such ideographical forms as have totally fallen out of the Aramaic verbal system will be explained merely by reference to the closest corresponding Aramaic forms or simply to the triconsonantal root, from which the 3d p. sg. perf. can be easily seen, e. g. NKS, pf. N'KAS (NB: — roots as BNY, HZY have the perf. B'NA, HAZA; HDY has HADI).
2888:sense of ‘the highest, the most elevated’ in general, still surviving in pahlavān ‘heroes’, pahlavānī ‘heroic’ in the epic. — Paz. pahalim, pahlum etc., Skr. v. atah- para, atyuttama. FrP, Cod.P fol. 11° p’hlwm: Paz. phälum with the gl. (NP) pšm: yani bihišt. Cf. s. v. Mahlah.
2972:the people of Pars 11416. — In Cat. 12 corrected to phlwbyg’n = Pahlavigän, but v. UJ IX, 1929, 102. Perhaps a simple mistake for pdrsikan, but cf ērānakān and Wwäspuhrakän.
4587:Bible Aramaic Balčehi Bundahišn Book Pahlavi
4627:Abbreviations 234 Abbreviations OAr Old Aryan sg. singular OAram Old. Aramaic Skr Sanskrit obj. object Skr. v. Sanskrit version OInd Old Indian st. stem OIr Old Iranian st.abs. status absolutus OP Old Persian subj. subject opp. opposite, opposed to subju. subjunctive opt. optative subst. substantive (ist, 2nd, 3d) p. person suff. suffix . sup. superlative pap. PEE S. V. (sub voee) under the word pass. passive S patr. patronymic Ww be ne t Paz Pazand - tads (ern) ers. pron. ersonal pronoun ; à Phi Pahlavi SUE ROE pl. plural . pos. positive Talm Talmud(ic) poss. possessive th. thing | postp. postposition trans. transitive prec. preceding pref. prefix ult. (in ultimo) in the end of the prep. preposition page pres. present tense pret. preterite v verso (of a folio) prev. preverb var. various reading, variant pron. pronoun vb. verb, pl. vbs. — verbs Prs Persian WIr West Iranian Prth Parthian viz. (videlicet) namely Ps. Psalms pt: participle w. word, pl. ws. = words r recto (of a folio) rel. adv. relative adverb Yt Yašt
4644:AV — 'The book of Arda Viraf. The Pahlavi text prepared by Destur Hoshanji Jamaspji Asa. Revised and collated with further MSS with an English translation and in- troduction, and an appendix containing the texts and translations of Gosht-i Fryano, and Hadokht-nask by Martin Haug, assisted by E. W. West. London & Bombay 1872.
4645:Glossary and Index of the Pahlavi Texts of the book of Arda Viraf, the tale of Gosht-i Fryano, the Hadokht Nask, and to some extracts from the Din-kard and Nirangastan, prepared from Destur Hoshangji Jamaspji Asa’s Glossary to the Arda Viraf Namah. and from the original texts, with notes on Pahlavi grammar, by E. W. West, revised by Martin Haug. London & Bombay 1874. V. also Paz. AV. AZ = Ayyätkär i Zareràn v. MP I, p. XII sg.
4650:BdA = The Bündahishn. Being a Facsimile of the TD Manuscript No. 2 brought from Persia by Dastur Tirandáz and now preserved in the late Ervad Tahmuras Library, ed. by the late Ervad Tahmuras Dinshaji Anklesaria with an introduction by Behram Gore Tahmuras Anklesaria. Bombay 1908. In The Pahlavi Text Series ... to commemorate the Jubilee of Her late Majesty the Queen Empress of India in 1887 held by the 'Trustees of the Parsi Punchayet, Vol. III.
4662:Cat. — J. Markwart, A Catalogue of the provincial capitals of Eran-shahr (Pahlavi text, version and commentary) ed. by G. Messina. Roma 1931.
4673:Dhabhar, ZKhA = Zand-i Khürtak Avistak, edited by Ervad Bamanji Nasarvanji Dhabhar. Pahlavi Text Series Published by the Trustees of the Parsee Panchayet Funds and Properties No. 3. 1927.
4674:Dhabhar, PYV = Pahlavi Yasna and Vispered. Ed. with an Introduction and a Glossary of Select Terms by Ervad Bamanji Nasarvanji Dhabhar. Pahlavi Text Series ... Nr. 8. 1949.
4677:Dhalla, The Nyaishes: The Nyaishes or Zoroastrian Litanies. Avestan text with the Pahlavi, Sanskrit, Persian and Gujarati versions, ed. by Maneckji Nusserwanji Dhalla. Khordah Avesta. Part I. Columbia University, Indo-Iranian series ed. by A. V. Williams Jackson, Vol. VI. New York 1908.
4681:DkM = The complete text of the Pahlavi Dinkard. Published by ''the Society for the promotion of the researches into the Zoroastrian religion" under the super- vision of Dhanjishah Neherjibhai Madan. I-II, Bombay 1911.
4682:DkMS = Dönkart, A Pahlavi text. Facsimile edition of the Manuscript B of the K. R. Cama Oriental Institute, Bombay. Edited by M. J. Dresden. Wiesbaden 1966. (Quotations refer to the bracketed figures beneath the text, e.g. [196])
--- BRT parθ
```


## [2026-09-07T20:41:32.187Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (420,421,422):\n    print('=== leaf',n)\n    print(t[n][:1800])\nEOF"
}
```


### [2026-09-07T20:41:33.540Z] TOOL RESULT

```
=== leaf 420
ch ‘cab- ee praiseach ‘pottage’) W. ae ca ages (coll. ; sg. bresychen),
. broskva cabbage-turnip’, also NG ity ‘toad’. Ernout-M. 117. Walde- Vendryes py 2278, Pedersen 1.226. a € hib. voc. 118. Berne-
Lat, cau stalk’, th ‘stall’ ete
lis ‘stalk’, esp. ‘cabbage- en ‘cabbage’ : Gri. kavNés : pace It. cavolo, Fr. chou, em), Oy aa » Br. kaol (coll.; sg. kaol-
S.V. cole, sb.1,
Sp. berza, Rum. varza, fr. Lat. viridia ‘green plants’, fr. viridis ‘green’, REW 9367.
3. Ir. braissech, W. bresychen, fr. Lat. brassica (above, 2).
NI. cabdiste, fr. NE cabbage (below, 4). Pedersen 1.230.
4. ON kal, OF cawel, etc., above, 2.
ME caboche, cabache, NE cabbage, fr. OFr. (Pic., Norm.) caboce (Fr. caboche) ‘head’ beside cabosse, deriv. of OFr. boce, boche, bosse ‘swelling, boil, bump’, prob. influenced by derivs. of Lat. caput
‘head’ NED s.v. cabbage, sb1 REW 1191a. Gamillscheg 164. Wartburg 1.469.
Late OHG cabuz, capuz, MHG kap- puz, NHG dial. kappus, kappes (Kretsch- mer, Wortgeogr. 565), like Fr. cabus in chou cabus, fr. deriv. of caput ‘head’. REW 1668. Weigand-H. 1.988.
NHG kraut ‘herb, plant’ (8.53) is usual for ‘cabbage’ in South Germany, and generally in sauerkraut. Kret- schmer, Wortgeogr. 566 ff.
5. Boh., Pol., Russ. kapusta (> Lith. kopustas, Lett. kapuosts), SCr. kupus, fr. deriv. of caput ‘head’ (like Fr. cabus, etc., above, 4), but in form apparently influenced by MLat. compos(i)ta, It. Composta ‘compost’. Berneker 486. Briickner 218.
Boh. zelé: ChSl, zelije ‘vegetables’ (5.65),
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
EE
374 SELECTED INDO-EUROPEAN SYNONYMS
5.70 POTATO NG warara Dan. _kartoffel Lith.  bulvé, ropulé It. patata Sw. potatis Lett. kartupelis (bulbe) Fr. pomme de terre NE potato SCr.  krumpi
=== leaf 421
), W. tatws (pl. fr. NE ‘tatoes), new sg., taten, Sw. potatis (Er. NE pl. potatoes, cf. Hellquist s.v.).
2. Fr. pomme de terre, lit. ‘earth- apple’, and similarly, mostly by imita- tion of the French, Br. aval-douar, Du. aardappel, NHG erdapfel (OHG erd-
5.71 FRUIT Grk. —_pdov, rdpa Goth, <</4e% Lith. vatszat NG dpodro, (6)xwprxd ON aldin Lett.  auglis Lat. pomum, malum Dan. frugt ChSI.  ovoSit It. frutto Sw. — frukt S8Cr. voce Fr. fruit OE ofet » Boh. — ovoce Sp. fruto ME frut Pol.. owoc Rum. poamd, fruct NE fruit Russ. frukt Ir. torad Du. vruchi Skt.  phala- Nir. toradh OHG  obaz Av. ae W. Srwyth, aeron MHG bez Br. Srouez NHG abst
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Icel. gardepli, NG yewpndov (only literary
aphul, MHG ertapfel ‘melon, cucumber’), and clearly a translation of the Frenc yh
3. Sw. dial. jordpdron lit. ‘earth-pear’, and so NHG dial. erdbirne, grundbirne, the latter the source of SCr. krumpir, Berneker 622.
4. NHG kartoffel (> Rum. cartof, Dan. kartoffel, Lett. kartupelis, Pol. kar- tofel, Russ. kartofel’), by dissim. fr. older tartuffel, this fr. It. tartufolo ‘truffle’, used also for ‘potato’. REW 8966. Wei- gand-H. 1.199, Kretschmer, Wort- geogr. 256f. Berneker 491.
5. Lith. bulvé, bulbé, Lett. bulbe, fr. Pol. bulba, bulwa, dial. ‘potato’, this fr. Lat. bulbus ‘bulb’. Berneker 100. Nie- dermann, Wort. u. Sach. 8.67 ff.
Lith. roputé, dim. of ropé ‘turnip’ : ChSl. répa, OHG ruoba, Lat. rapum, Grk. pamus ‘turnip’, Walde-P. 2.341.
Boh. zemdk, Pol. ziemniak, derivs. of zemé, ziemia ‘earth’.
Boh. brambor, fr. bramburk = Bran- denburg as the source of export. So Rum. dial. bandraburcd ‘potato’. Ber- neker 81 ff. Tiktin 154.
¥O
: od here in the cur- pruit’ i NE fruit as a generic pet Stree fruit’, covering apples, pame for This notion i
=== leaf 422
oy’ : Goth. brikjan, OE brican ‘use’, etc. Walde-P. 2.208. Emout-M, 893 f. Walde-H. 1.552. oe os special though not exclusive fla Te ae fruit’, It. frutto, coll. rg eit (> ME ful, NE ret), » Coll. fruta, Rum, fruct, W.
sense. : 1, Grk. #
op AND DRINK; COOKING AND UTENSILS
igitized by Arya Samaj Foundation Chennai and eGangotri
375
ffrwyth, Br. frouez, MLG vrucht (> Dan. frugt, Sw. frukt), Du. vrucht (OHG fruht, NHG frucht only in wider sense ‘product, fruit’), Russ. fruke.
3. MIr. torad, NIv. toradh, also ‘prod- uct, fruit’ in widest sense, (as always W. toreth), cpd. to-rad fr. *to-ret : Ir rethim ‘run’, hence ‘that which comes to one, in-come’. Pedersen 2.600, 677.
W. aeron : Ir. dirne, MBr. trin ‘wild plum’, Goth. akran ‘fruit’ (in widest sense, kaprés), etc. Walde-P. 1.173. Pedersen 1.103.
4. ON aldin: ON ala, Goth., OE alan, Lat. alere, etc. ‘nourish, feed’. Walde-P. 1.86f. Falk-Torp 789 f.
OE ofet, OHG obaz, MHG obez, NHG obst, whence (Briickner 388) ChS]. ovosti, SCr. voée, Boh. ovoce, Pol. owoc, (Russ. ovosé ‘vegetables’), orig. ‘fruit’ in wider sense, as esp. OF ofet, etym. dub. Prell- witz, BB 25.158. G. S. Lane, JEGPh. 32.486 f.
5 Lith. vaisius ‘fruit’ in widest sense (cf. vaisa ‘fertility’, veislus ‘fruitful’, etc.), also but esp. pl. vaiséai ‘fruit’ as intended here : veisti ‘propagate, pro- duce’, Lett. viest ‘nurture, increase’, refl. viesties ‘thrive’, prob. also Gmc. group OE wise ‘sprout, stalk’, ete. Walde-P. 1.242. Mithl.-Endz. 4.670.
Lett. auglis, fr. Lett. augt, Lith. augti ‘grow’ (12.53). Mithl.-Endz. 1.216.
6. Skt. phala-, fr. phal- ‘burst’, hence also ‘ripen, bear fruit’. Walde-P. 2.102
Gib ce 5.72 APPLE ie ne Goth i Ie Hilo oth. apel Lith. obuolys i t  malum ON epli Lett. abuols n | omela Dan. able ChSl. jablitko Sr Pomme Sv. apple SCr. jabuka
```


## [2026-09-07T20:41:34.147Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD pahl\"; grep -n -E \"pahlaw|pahlom|pahl[a-z]* \" PHD.txt | grep -v -i \"pahlavi\\b\" | head -20; echo; echo \"== PHD lines with 'Parthian'\"; grep -n \"Pārs\\|Pars\\b\" PHD.txt | head -10"
}
```


### [2026-09-07T20:41:34.221Z] TOOL RESULT

```
== PHD pahl
3044:Parthian pahlawig.
4760:1 3pahréxtan pahrez l-pahréz- pahlawig pahlüg pahlom pahlomih paygālgar pahast lpüy-

== PHD lines with 'Parthian'
```


## [2026-09-07T20:41:42.044Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in (423,424):\n    print('=== leaf',n)\n    print(t[n][:2500])\nEOF\necho \"########## peach in SYN\"\ngrep -n -i \"peach\\|persica\" SYN.txt | head -20"
}
```


## [2026-09-07T20:41:42.472Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3040,3050p' PHD.txt"
}
```


### [2026-09-07T20:41:43.530Z] TOOL RESULT

```
=== leaf 423
NIv. ptorra, W. peran. Walde-P. 2.75. Er- nout-M. 772. REW 6524. Falk-Torp 862.
2. NG ayAdé,, fr. late Grk. axdds= axpas, -ddos ‘wild pear’, beside éxepios ‘wild pear’, etym.? Walde-P. 1.608.
3. W. gelleigen, pl. gellaig, also gelly-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
2. Grk. yAdov, Dor. H@ov, whence Lat, malum (both also ‘fruit’), prob. of pre. Greek origin. But Lat. malum Was re. placed by VLat. mélum (Pallad., etc.) reborrowed fr. the common Grk. hoy hence It. melo ‘apple tree’, with ney mela ‘apple’, Rum. mdr. Ernout-M 583, Walde-H. 1.218f. REW 5279
3. Fr. pomme, fr. Lat. pomum ‘fruit? (5.71). REW 6645.
Sp. manzana (manzano ‘apple tree’) fr. Lat. mala Matiana, supposed to He named from a person (so Pliny 15,15.1) or a place (so Isid. 17.7.3). REW 5247,
gen, pl. gellyg, perh. fr. (old cpd. of?) gell ‘yellow’.
W. rhwnen, etym.?
4, Lith. kriaugé, OPruss. crausios (pl.), SCr. krugka, Boh. hrugka, Pol. grusza (> Lith. grisia), gruszka, Russ. grusa, all borrowed from some oriental source (cf. Kurd. koré&i, kurési ‘pear’). Berneker 358. Trautmann 140. Briick- ner 160.
Lett. bumbieris, fr. Baltic-German bumbeere, like NE pomepear, fr. Fr. pomme poire. Miihl.-Endz. 1.349.
rom ‘Persian’, indicating the See of the peach, which is ca to China. Cf. Schrader, Reallex. fe
OG ufdov mepotxor, Lat. malum Persicum. From the latter as persicum or persica (orig. neut. pl., used as fem. sg.) come It. pesca, Fr. péche (> ME peche, NE peach > NIr. peitseog; also >Br. pechez coll., sg. pechezenn), Sp. prisco, persigo (not the usual words), Rum. piersicd; OK persoc, MLG persik (> Sw. persika), MHG pfersich, NHG pfirsche (pl. > Dan. fersken), pfirsiche (> Lett. firsikis), etc. Russ. persik (> Lith. persikas) directly fr. the Grk. or Lat. form. The other Slavic forms, a breshva, Boh. broskev, etc., prob.
ough MHG pfersich. REW 64927.
CC-0. In Public Domain. Gu
Digitized by Arya Samaj Foundation Chennai and eGangotri
0OD AND DRINK; COOKING AND UTENSILS 377 I 5.74 PEACH b. Lith. persikas pidov repotnoy ae sede Lett. _firsikis Gr. ixwO 8, .  fersken (O}ifS) By Sines NG ate Persicum er eos SCr. breskva \ Boh broskev ie pesca OE persoc . Tt * — ptche locotén ME peche Pol. brzoskwinia *— durazno, mé NE peach Russ. persik Rum. piersicd Du. _persik me OHG .... Nir. Pause og, fal MUG pfersich f Ce aaa ’ NHG pfirsche, pfirsiche gu _  pechezenn Padi ee Nearly all the words for ‘peach’ come 2. Lat. diiracinus ‘hard-berried’, epd.
of durus ‘hard’ and acinus ‘berry’, w
=== leaf 424
EW 2803.
3. Sp. melocotén : It. melo cotogno, Grk. pfdov xvddmov ‘quince’, but in
Spanish ‘peach’. REW 2436.
4. W. eirinen wlanog, afal gwlanog,
Falk- _ : i eee 214. Berneker 51. Briick- | lit. ‘woolly plum, woolly apple’, fr. the : fuzzy skin of the peach. \ 5.75 FIG TUKo; oko. Goth. smakka Lith. fyga Ticug ON fikja Lett. vgs fico Dan. — figen ChSl. smoky aque Sw. Jikon SCr. smokva 190 OE fic, fic-eppel Boh.  jik, smokva, smokev §moching ME figge Pol. —figa fie NE fig Russ. figa tige Du. vig Digysen, OHG figa enn MHG vige NHG Seige
rukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
378 SELECTED INDO-EUROPEAN SYNONYMS
1. Grk. cixov, (Boet. rixov), Lat. ficus, and also Arm. t'uz ‘fig’, prob. fr. a common Mediterranean source. Lat. ficus is the source of all the other Euro- pean words except the group given un- der 2. Schrader, Reallex. 1.306. Er- nout-M. 356. Walde-H. 1.492. Falk- Torp 215. Pedersen 1.228. Berneker 281.
2. Goth. smakka, ChSl. smoky, SCr. smokva, etc. (once the general Slavic
word, quotable from all the Slavic lan- guages, but now partly replaced by the representatives of Lat. ficus; fr, Slavic also Rum. smochind), prob. fy. some oriental (Caucasian?) source. But some regard Goth. smakka as a Gmc. word (; NHG smecken ‘taste’, ete.), which Kas adopted by the Slavs. Schrader, Real. lex. 1.806. Feist 439. Stender-Petersen 363 (with full Slavic material; for Gme orig.).
5.76 GRAPE Grk. Bérpus, cradudy (pat) Goth. weinabast Lith. keké, vynuogé NG — aragtdt (pya) ON  vinber Lett. k’ekars, vinuoga Lat. ava Dan. drue ChSl. grozdii, groznit It. uva Sw. druva SCr.  grozd Fr. raisin OE winber (1) ge Boh. hrozen Sp. uva ME grape Pol. winogrono Rum.  strugure NE grape Russ. — vinograd Ir. in Du. druif . Skt.  draksa- Nir. __fionchaor OHG _tribo, winberi Av. ‘ W gwinronyn MHG tribe, winber
Br. rezinenn NHG
Some of the words listed, as Grk. Bérpus, cradvd7, are collectives meaning ‘a bunch of grapes, grapes’, the single ‘grape’ being expressed by a different word, as Grk. paé (also ‘berry’). Many others were originally used only in this way, and in general the notion of ‘bunch, cluster’ is a frequent source of the words for ‘grape’. Several are con- nected with words for ‘wine’ or ‘vine’.
1. Grk. Bézpus, without convincing etym. and perh. a loanword fr. a pre- Greek source. Meillet, MSL 15.163. Walde-H. 1.113.
Grk. crag¢vdy, whence cradidvov, NG oraptr : Grk. oréudvda ‘pressed olives or grapes’, doreupns ‘firm, solid
########## peach in SYN
9514:rom ‘Persian’, indicating the See of the peach, which is ca to China. Cf. Schrader, Reallex. fe
9515:OG ufdov mepotxor, Lat. malum Persicum. From the latter as persicum or persica (orig. neut. pl., used as fem. sg.) come It. pesca, Fr. péche (> ME peche, NE peach > NIr. peitseog; also >Br. pechez coll., sg. pechezenn), Sp. prisco, persigo (not the usual words), Rum. piersicd; OK persoc, MLG persik (> Sw. persika), MHG pfersich, NHG pfirsche (pl. > Dan. fersken), pfirsiche (> Lett. firsikis), etc. Russ. persik (> Lith. persikas) directly fr. the Grk. or Lat. form. The other Slavic forms, a breshva, Boh. broskev, etc., prob.
9519:0OD AND DRINK; COOKING AND UTENSILS 377 I 5.74 PEACH b. Lith. persikas pidov repotnoy ae sede Lett. _firsikis Gr. ixwO 8, .  fersken (O}ifS) By Sines NG ate Persicum er eos SCr. breskva \ Boh broskev ie pesca OE persoc . Tt * — ptche locotén ME peche Pol. brzoskwinia *— durazno, mé NE peach Russ. persik Rum. piersicd Du. _persik me OHG .... Nir. Pause og, fal MUG pfersich f Ce aaa ’ NHG pfirsche, pfirsiche gu _  pechezenn Padi ee Nearly all the words for ‘peach’ come 2. Lat. diiracinus ‘hard-berried’, epd.
9520:of durus ‘hard’ and acinus ‘berry’, was applied to fruit with stones, as grapes, peaches, cherries. Hence words in various Romance dialects specialized to ‘grape’, ‘cherry’ or ‘peach’, the latter in Sp. durazno. Hence also late Grk. dwpa- xwov (also dop-) and podaxivoy (LS s.vv., without connecting them), the latter (reg. NG word) with transposition sup- ported by association with péddov ‘rose’, owing to the rosy bloom of the peach. Ernout-M. 291. Walde-H. 1.384. REW 2803.
9522:Spanish ‘peach’. REW 2436.
9524:Falk- _ : i eee 214. Berneker 51. Briick- | lit. ‘woolly plum, woolly apple’, fr. the : fuzzy skin of the peach. \ 5.75 FIG TUKo; oko. Goth. smakka Lith. fyga Ticug ON fikja Lett. vgs fico Dan. — figen ChSl. smoky aque Sw. Jikon SCr. smokva 190 OE fic, fic-eppel Boh.  jik, smokva, smokev §moching ME figge Pol. —figa fie NE fig Russ. figa tige Du. vig Digysen, OHG figa enn MHG vige NHG Seige
```


### [2026-09-07T20:41:43.573Z] TOOL RESULT

```
parasang frasang.
pardon (n.) hilišn.
pardon (v.) histan.
part bahr, bazišn, sraxtag.
Parthian pahlawig.
pārag, pēšag,
ENGLISH-PAHLAVI INDEX
particle xwurdag.
particular ēwāzīg, waspuhragan; in ~ pad nàméist.
partner hambāy, hambaz.
partridge kabk, tihog.
```


## [2026-09-07T20:41:51.740Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pahlawīg\\|pahlawig\\|phlwyk\\|pahlom\\|pahlūg\\|pahlug\" PHD.txt | head; echo \"=== ctx\"; grep -n \"pahlawīg\" PHD.txt | head -3"
}
```


### [2026-09-07T20:41:51.805Z] TOOL RESULT

```
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
3029:Pahlavi pahlawig.
3044:Parthian pahlawig.
3439:rib pahlūg.
4760:1 3pahréxtan pahrez l-pahréz- pahlawig pahlüg pahlom pahlomih paygālgar pahast lpüy-
=== ctx
```


## [2026-09-07T20:41:52.451Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Pahlaw\\b\\|pahlaw \" PHD_pages.txt | head -20; echo \"=== search p section\"; grep -n \"parasang\\|frasang\" PHD_pages.txt | head"
}
```


### [2026-09-07T20:41:52.516Z] TOOL RESULT

```
3977:pahlawig [.p'hlwbyk I I (M phlw'nyg), N pahlaw(an)i] Parthian j Pahlavi.
=== search p section
2323:fra8an~ [plsng I N farsang] parasang (4 Roman miles).
2865:   light); a measure of length (= frasang, or 1- frasang, I mile).
7243:parasang frasang.                         (u)spurrig.
8076:                       ii.       = frasang
8077:            I frasang            = 4 'miles'              'parasang'
8659:frawahr                      ~~Q)        frasang                       -,~Q)
```


## [2026-09-07T20:42:03.563Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -h -o '{\"ref\": \"AHD:[0-9]*\", \"status\": \"[a-z_]*\", \"note\": \"[^\"]\\{0,200\\}' page-3*.json | head -12; echo ====; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'));import sys\nprint(json.dumps(d['AHD'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-07T20:42:04.787Z] TOOL RESULT

```
Exit code 1
{"ref": "AHD:1526", "status": "supports", "note": "Nourai's page is the 1976 AHD appendix (not open online), but the same Watkins entry stands in AHD_watkins1985.txt line 680: 'lēk-. To tear … 2. Suffixed form *lak-ero- in Latin lacer, torn: LACERATE.
{"ref": "AHD:1526", "status": "supports", "note": "Nourai's 1976-appendix page is not open, but the same entry is AHD_watkins1985.txt line 687: 'lep-1. To peel. 1. Greek lepein, to peel … 3. Suffixed variant form *lap-aro- in Greek laparos, soft: LAPA
{"ref": "AHD:1526", "status": "supports", "note": "Same entry in AHD_watkins1985.txt line 687: 'lep-1. To peel. … 3. Suffixed variant form *lap-aro- in Greek laparos, soft: LAPAROTOMY. [Pok. 2. lep- 678.]' — Nourai's gloss 'soft' is Watkins's own word
{"ref": "AHD:780", "status": "partial", "note": "Nourai's AHD page numbers on this page (780, 793) are pages of the 1975 New College main dictionary, which is not the volume on disk; the Indo-European appendix content is checkable and supports the f
{"ref": "AHD:867", "status": "supports", "note": "The 1975 New College body volume is not on disk, but its etymology survives verbatim in the current online AHD s.v. myna: '[Hindi mainā, perhaps from Sanskrit madanaḥ, from madana-, delightful, joyful
{"ref": "AHD:805", "status": "supports", "note": "The 1975 body volume is not on disk, but the AHD etymology is unchanged online s.v. matte: '[French, curdled milk, matte, from feminine of obsolete mat, compact, from Old French, dull, from Latin matt
{"ref": "AHD:805", "status": "supports", "note": "Current AHD s.v. matte: '[French, curdled milk, matte, from feminine of obsolete mat, compact, from Old French, dull, from Latin mattus, stupefied; see MAT2.]' — the chart's route exactly, with AHD's 
{"ref": "AHD:817", "status": "partial", "note": "AHD:817 is a page of the 1975 New College Edition main dictionary (the alphabetical mel- range), which is not on disk — only Watkins's IE-roots appendix is (AHD_watkins1985.txt). What the appendix doe
{"ref": "AHD:834", "status": "not_checked", "note": "AHD:834 is a page of the main dictionary of the American Heritage Dictionary, New College Edition (1975/76). Only the Indo-European Roots appendix of that edition is on disk (AHD_watkins1985.txt), and
{"ref": "AHD:860", "status": "not_checked", "note": "AHD:860 is a page of the main A-Z text of the American Heritage Dictionary, New College Edition (1975/76), which is not on disk; the only local AHD file is AHD_watkins1985.txt, i.e. Watkins' Indo-Euro
{"ref": "AHD:1529", "status": "supports", "note": "The page number belongs to the 1976 New College appendix, which is not open online; the corresponding entry in Watkins 1985 (AHD_watkins1985.txt line 753) is 'mer-2, To rub away, harm ... [Pok. 4. mer
{"ref": "AHD:872", "status": "not_checked", "note": "AHD:872 is a page of the 1975/76 New College Edition main dictionary (the entry nanus/nano-), which is not openly available (the IA copies americanheritage0000dict, americanheritag00morr etc. are lend
(eval):1: === not found
```


## [2026-09-07T20:42:17.484Z] TOOL CALL #20: Bash

```json
{
 "command": "sed -n 1,60p /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-07T20:42:17.528Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-07T20:42:19.494Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WEB Parthian\"; grep -n -i \"parthian\" WEB.txt | head -10; echo \"== WEB parchment\"; grep -n -i \"^parchment\\|parchment,\" WEB.txt | head -5; echo \"== HRN pahlav\"; grep -n -i \"pahlav\\|Pahlaw\" HRN.txt | head -20; echo \"== HUB\"; grep -n -i \"pahlav\\|Parthava\\|Pahlaw\" HUB.txt | head -20"
}
```


### [2026-09-07T20:42:19.594Z] TOOL RESULT

```
== WEB Parthian
ugrep: warning: WEB.txt: No such file or directory
== WEB parchment
ugrep: warning: WEB.txt: No such file or directory
== HRN pahlav
1943:Men. 2, 158, 165 (West, Pahlavi Texts^ 22 Note 2,
2701:West, Pahlavi Texts» 142 Note 10.
3249:ap. Parfhava-; phlv. pahlav (gehört etwa auch
3333:*) Vergl, Hang, Essay on Pahlavi, 61 (PPÖL).
== HUB
1491:343. Hier fehlen die n5tigsten Eriauterungen zu pahlav
4439:arab. qubad; Pahlav = ap. /;a^-^a«?rt- ; navasard 'Neujahr' etc
5819:307; Pahlav 'Parthien' --=^ ap. Pardava-; fadarv Tasan' H.
6363:3. Jhd., Haug, Essay on Pahlavi p. 4, syr. pDDinN am
7042:hausen, Parthava und Pahl. p. 45 fig.; ZDMG. 31, 562);
7374:§ 97. Ap. rd- ist (iiber rA) zu hi geworden: pahlav^
7375:urspr. = Parthien (ZDMG. 31, 558), pahlavi parthisch',
7376:arm. Pahlav-) {Palliav) Tarthien, Farther, pahlavik {pal-
9424:= np. ptd *Briicke' = ap. *prd^U' , zd. peretu-; Pahlav
9425:*Parthien, arm. Pahlav — ap. Par&ava-; d<A»7 vierzig'; pahlil
```


## [2026-09-07T20:42:25.692Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | sed -n '80,140p'"
}
```


### [2026-09-07T20:42:25.739Z] TOOL RESULT

```
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
```


## [2026-09-07T20:42:26.653Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- HUB 7370-7380\"; sed -n '7370,7380p' HUB.txt; echo \"--- HUB 5815-5822\"; sed -n '5815,5822p' HUB.txt; echo \"--- HRN 3245-3255\"; sed -n '3245,3255p' HRN.txt"
}
```


### [2026-09-07T20:42:26.723Z] TOOL RESULT

```
--- HUB 7370-7380
Name aus dem Avesta ins Mittelpersische zu einer Zeit
gekommen, als dieses den Laut if nicht mehr besass und
daher durch / wiedergab? Vgl. russisch Fedor = gr.
QeodiOQog; Mar/a =■ gr. Mdg&a.
§ 97. Ap. rd- ist (iiber rA) zu hi geworden: pahlav^
urspr. = Parthien (ZDMG. 31, 558), pahlavi parthisch',
arm. Pahlav-) {Palliav) Tarthien, Farther, pahlavik {pal-
havik) 'parthisch* = ap. Pard^ava- *Parthien', gr. Ildg&ot
u. s. w. ; pul = ptthl *Brucke' = ap. *pr9u' = zd. perefu-
(wie ap. gd&U' = zd. gatu- u. s. w.,. siehe § 89 und 95) ;
*) Dazu soil nach Horn Nr. 407 t€ra 'finster' gehSren, was ioh
--- HUB 5815-5822
8. oben p. 116, Anm. 2.— 165 —
56; bavar *Qlsiuhe\ paz.vdwar^ arm. vaver; 6e/;ar 'zelmtausend'
H. 262; bSva Wittwe H. 268; parvezan *Sieb' H. 249; paroar
*Stair H. 304: parvus: 'Flug' H. 305; parvez *siegreich' H.
307; Pahlav 'Parthien' --=^ ap. Pardava-; fadarv Tasan' H.
379, oben p. 47; tuvan Sermogend' H. 401; javecl Wig
H. 414; javan, juvan Miingling H. 429; jOi, jo ^Kaiial* H.
431; damdan 'laufen H. 585; duoest 'zweihiindert' H. 586;
--- HRN 3245-3255
pärsü, wa/. pürs, kurm. parsü, oss. fars 'Seite, Strich,
Gegend' (278) lässt sich np. pehlü lautlich nicht direkt
zusammenstellen.
343. peJilev, pehletan 'Held'^).
ap. Parfhava-; phlv. pahlav (gehört etwa auch
pahlum hierher?).
344. peh/Ti' 'weit, breit', pehnä.
Käs. pen, pahdn, pan,
aw. pa^ana^ 'weit, breit; phlv. pahan, pahnäi^
pahnäk.
kurd. pän ; af;\ plan ; oss. d. fafan t. fäfdn 'Breite,
```


## [2026-09-07T20:42:37.081Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSF پهلو\"; grep -n \"پهلو\" FSF_pages.txt | head -20"
}
```


### [2026-09-07T20:42:37.135Z] TOOL RESULT

```
== FSF پهلو
119: ‫پس از ترور ناموفق محمدرضا پهلوی در بهمن ‪ ۸۲۳۱۰‬عبدالحسین نوشین در‬
370: ‫وهلوی واژه را قیدکرده‌ام گواه‌به گاهاز نامه‌های پهلوی شاهدهایی‬
844:‫نژاد» نجیب سرشت‪ .‬پهلوی‪ :‬آزات‪1222 .‬‬
1007:             ‫جهان را کزردار بد شرم نیست‬                  ‫ز بس خواهشش پهلوان نرم شد‬
1368:                  ‫پهلوی آفرین (باسکون فا)‬                ‫سل ھی او با مق کون‬
1412:                  ‫‪-۱‬آفرین و نیایش کردن‪:‬‬                  ‫اگر تاجدارست اگر پهلوان‬
1745:‫چنین گفت با پهلوان گزین‬                       ‫«شتاب زدگی اندر کارها از کاردیو است و‬
1792: ‫پهلوی‪ :‬آهوک (با واو بیان ضمه) )‪613‬‬                    ‫مکن پیشدستی تو در جنگ ما‬
1806:‫اسو (بهاشباع واو) لائ به معنی تند و‬         ‫بیتبالاگفتارپهلوانپسازپایاننبرد‬
1997:  ‫به شعر آری از دفتر پهلوی‬                                                            ‫اختوکرای‬
2048:‫در فرهنگ‌ها معنی فقیر و بی‌چیز و‬           ‫گشتاسب پس از توصیف پهلوانی و‬
2071:           ‫اگر پهلوانی ندانی زبان‬             ‫شم اند بت شاهاران زین‬
2075:‫معنی تند و تیز و چالاک و دلیر و پهلوان‪.‬‬        ‫(‪)۵-۸۸۳-۰۸۵۲‬‬
2076: ‫پهلوی‪ :‬اروند (نک پورداود‪ .‬یادداشت‌های‬                                                ‫اغرنده‬
2078:‫گاتهاص ‪ )۸۳۳‬کوه الوند نیز بهپهلوی‬               ‫آشفته و خشمآلود (لغت فرس ‪-‬صحاح)‪:‬‬
2256:       ‫نه استد کس آن پهلوان شاه را‬                            ‫بزد نیزهگشتاسپ بر جوشنش‬
2539: ‫‏‪ ham-par‬پهلوی همنارتن ‪natrabnoh‬‏‬                 ‫اگر چند دارد هنرها بسی‬
2591: ‫نسباشد» (صحاح) پهلوی‪( 47 :‬حسرو‬                 ‫که بنشستی به تنهایی گرستی‬
2874:          ‫نیامده است‪ .‬لخت فرس این وا‬             ‫پهلوی انوشک ‪ 61205602‬مرکب از الف و‬
3129:             ‫کپههدلووان آامیددر به‌جنگ‬         ‫گرداوژن گردانکن‪ ...‬پهلوی ‪:02۵‬‬
```


## [2026-09-07T20:42:38.532Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT v1 پارس\"; grep -n \"^پارس\\|پارس :\\|پارس .\" BQT_v1_pages.txt | head -20; echo \"== BQT v1 پهلو\"; grep -n \"پهلو\" BQT_v1_pages.txt | head -10; echo \"== MON files\"; ls -la MON_part1.txt MON_part2.txt | cat"
}
```


### [2026-09-07T20:42:38.622Z] TOOL RESULT

```
== BQT v1 پارس
175:پارسی باستان و ۱۶۱ رده بابلی و ۹۵۰ رده عیلامی است .
910:پارسی نوست.
911:پارسی نو زبان شپر های شرقی و تاجیکان ناحیه ایران خاوری »
1248:پارسی کوییم یعنی اين کشش ز آن‌طر فآید که آمداین چشش.
1251:پارسی گو گر چه‌تازی‌خوشتررست عشق‌راخودصدزبان دیگر است.
2786:الادو به در فپارس کتا بغانه های معرو ف که در دست داشتم
3059:پارسی ببمد و*۱۸ بعد» نقل کرده‌ایم ور که: زردشت درمتن وحاشیه . م.م.
3275:پارسی (بمعنی‌ناسوخته) مأخون است وهوبشمان مخالف ابن‌قول است.رك: فرهنگه‌ارمنیآجاربان.
8995:پارسی‌میانه ]۱16 «بارنولمه ۱۳۳۲: پهلوی 8۷8 «اونوالا ۳۲4». ۷9 اوستائی و۷26 ساسکریت
23092:پارسی باستان (کتیبه‌های هضامنشی) 2752 : ام مکی از اقوام ابرانی مقیم جذوب ایران که نام
23124:پارسی (فارسی) شامل
23127:پارسی‌میانه (پهلوی),
23128:پارسی نو ( فار-ی
25313:پارسی باستانی و معرب آن براهیم است٩‏ .
25468:پارسی لیز: مجشلك» بژشك .
27444:پارسی پیسه شده بمعنی ابلق و دورنک : سفید وسیاه. پیسی که در نازی بر صکویند نام بیماربی
28998:آنرا بونانبان «پرس پولیس» نامیدماند , وآن درمرو دشت پارس قریب بيك فرسنگی خرابه های
== BQT v1 پهلو
299:از دست رفته » در تفس پهلوی اوستا ( << زند) و نوشتهای پپلوی و باز ند
338:و بنام دوشغال کره‌تکه ۸۲۵۸۱۵1۵ ودمنکه 6۵ ۱۵۵۱۱۵ :2] -درپهلوی کلیلت
374:پهلوی بما رسیده » نسبة بسیار کم است ومیتوان گفت ناچیزاست. درتألیفات
375:نویسندگان ایرانی وعرب فرون پیش » نامپای بسیاری از کنب پهلوی‌یادشده
384:سبب دیگری که از ذخرء هنگفت کتب پهلوی روز گار ساسانیان‌بی بهپره
404:اما چند نوشته پپلوی ‏ از [ نجمله تفیر پهلوی و ندیداد وتفیر پپلوی بسا
405:که یادخواهیم کرد- وچند کتاب دیگر پهلوی که لقات آ نپادرفهرستی یادشده-
409:باید تفسیر اوستا ( زند ) را یاد کرد . تفسیر یا گزارش پهلوی اوستا مانند
427:از تفیر پهلوی اوستا (--زند ) که بگذریم سنکنیشتهایی که از خود
463:فرهنگ‌اوئیم (0170))-فر هنک پهلو يك- شهر ستا نپایایر ان - اردا و بر اقنامه
== MON files
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
```


## [2026-09-07T20:42:43.876Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23075,23135p' BQT_v1_pages.txt"
}
```


### [2026-09-07T20:42:43.926Z] TOOL RESULT

```
پار او - بارای بالف کشیده وبواو زده .
زت بر و مرژال را گونند - و نام بلو کیت از
پار د۸- بضم دال وسکون‌هيم» رانگی‌را
چاروا دوزند وبریس ران چارو! اندازند » وی
کوبند چرمی باشد که بریس زین اسب بندند
وبرزیر دم‌اسب اندازند. واين اسح است .
پار س - بسکون الث بروزن و حعنی
۳ هس یابه ۹ ۳ ۰
۴ رك : یادیاو .
۶ با 2202۷ . وآن مثل وضوست تزد مسلمانان. زرتفتب ی که میخواهد پادباب کند نضت
بك «خشنوتره اهورهه مزداو» (بخشنودی اهور مزدا) م‌خواند ویس از آن یکبار « اشم وهو...»
میسراید . آنگاه روی.ودستها وپاهای خودرا میشومد» از آن پسکشتی نو مبکند و بترئیب عقرد
کمربند خود می کتاید ودعای مخصوصآرا میخواند وباردیگر پدورکمر می‌بندد. «خرده اوسنا
۹ مح ۱*. ۱ رك : لت‌نامه ویازیر. .  .‏ ۷ 2 در: پارسال» پارینء قس مانسکربت
۸ ( در سال گذشته ) ؛ ارمتی 0۵ ( سال گذشته ) , کردی ۵ . افنانی ۳۵۲۵5 ,
استی 18۲8 ۰ 18808 ( در مال پیش ) » وخی ۳8۳0 ۰ سریکلی 2۳۷۷15 ( قس بونانی
61 ) بارسی باستان2 ۳8۲۷۷ (سابقا), اوستا 8211۲۷2 « اسشق ۲۷۰ *. ۸ - در
پارسی باستان (کتیبه‌های هضامنشی) 2752 : ام مکی از اقوام ابرانی مقیم جذوب ایران که نام
بقبه درصفحةً ۳۰
۵ پارت - پارسی‌باستان ۳۵۲4118۷2 مقر قوم پارت ( خراسان قدیم )- خود قوم پارت
ازاقوام ابرانی؛ کلم بهلو وهلوی (ه .م) ازین دام مشتق است.
۵ پارتی - منسوب بپارت , ازفوم پارت- زبان پارتی زبان پهلوی اشکانی را گونند .
رك : پهلوی ورد : مقدمهٌ آقای پورداود برهمین کتاب .۳9
۱ با نگ - بسکون الت بی وزن
آپرنگ » به‌نی امک ات و آن چیزی
باشد که در يك که ترازو نهند نا با کفهٌ دمگر
برایر شود .
وصفاهان و کرمان و بزد را نیز گفته‌اند و نام
جانورست شکاری کوچکتر ازپلاک واورا بوزهم
منگویند- ونام پس پهلوبن سام‌هم هست. گویند
که اصطخر بناکرد؛ اوست . ۱
یدسا «بارابع بالف کنیده. پرهیز کار
و دور از معاصی و ذمايم را کویند ٩‏ -
و بمعنی پارسی هم آمده است وجمع آن‌پارسیان
بار سه بقتح رابم‌بروزن دلوچه. بمعنی
کدابی باشد . ۶
۱ ۳ «یکی از ملوله بی‌انصاف بارسابی را فر سك که ازعبادت‌ها کدام فاضلتیست ٩‏
«کلتان ۳۰ ». ۴ - پارسیان جمم پارسی‌است نه جمم پارما . حافظ پارسایان را بمعنی
ابرانیان در برابر تاز مان آورده :
تازیان را غم احوال گرانباران نست مارسایان مددی تاخوش وآسان بروم. حافظ
حصحح فز وی ص ٩۷۷‏ و ره : فهرست‌همانکتاب ص ۳۹۶.
» پارسی - تّ
پیلوی ۳۵۲5۱۲ 4 دج که ادا
۱ ۳*۴ <, ۱۰ ی ّ
*او نوالاء۵۹»؛منسوب ض " ۱
بپاری. از مردم پاری
( فاری ) - زرئشتی
مخصوصاً زرتشتی میم
ی .اهر الس بت
پارسی (فارسی) شامل
سمزبان است: پارسی
باستان ) .م ) ۰
پارسی‌میانه (پهلوی),
پارسی نو ( فار-ی
بعداز اسلام) » وچون
مطلقا زبان بارسی
بقبه در صفحهٌ ۳۵۱
تخت جمشید . سیاهیان مادی ویارسی ( از چپ براست دوم وچپارم بارسی هستند )
بقیه ازصفحه ۳:۵
مقر ابشانرا نیز پاری نامیده‌اند . از اين فوم دوخاندان بزرک در دورة قبل از اسلام بشاهنشاهی
رسیدماند , هخامنشیان وساسانبان . ممرب‌آن «فاری» است ؛ بونانیان نام ۳635۵ را از نام این
```


## [2026-09-07T20:42:59.556Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT پاسارگاد\"; grep -n \"پاسارگاد\\|پارسه گاد\\|پاسارکاد\" BQT_v1_pages.txt BQT_v2_pages.txt | head; echo \"== BQT پشملبا/هلو\"; grep -n \"پشملبا\" *_pages.txt | head; echo \"== MON head\"; head -c 600 MON_part1.txt; echo; echo \"== MON پارت\"; grep -n \"پارت\\b\" MON_part1.txt | head -5"
}
```


### [2026-09-07T20:42:59.725Z] TOOL RESULT

```
== BQT پاسارگاد
== BQT پشملبا/هلو
== MON head
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
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی 
== MON پارت
1941:آپارتمان: 0 (.) (معم.) قسمتی 
6638:اپارتمان: 0 (ا.) ساختمان چند 
27903:پارت: ۲8۳ (.) (جاذ.) پرنده‌ای از راستة پا 
27912:پارتی: آ-03:0 (ص‌نسه.) منسوب به پارت. 
27913:از قوم پارت؛ از مردم پارت. زبان مردم
```


## [2026-09-07T20:42:59.996Z] TOOL CALL #28: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py IRN:63 --image 2>&1 | tail -40"
}
```


### [2026-09-07T20:43:05.957Z] TOOL RESULT

```
(no exact page map; using offset 11 -> pdf page 74; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/IRN/0063.png
REF: IRN:63  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 74  OCR-lang: fas

نقش بالدار کورش

اين نقش برجسته که تصویرها وعکسهای متعددی از آن باقی مانده است»
تندیس کورش در دشت مرغاب استء» وخود دشت مرغاب بهمین مناسبت‌نامگذاری
شده است» زیرا مردم از زمانهای قدیم پیکر برجستةٌ کورش را بابالها ی که برشانه
دارد» بصورت مرغی آسمانی تصورکرده‌اند ونام آنجا را مرغاب گذاشته‌ائد .

دشت مرغاب در پاسارگاد واقعم شده است وپاسارگاد میهن وخاستگاه خود
کورش است.

بطوریکه هرودوت مینویسد : پاسارگادیان یکی از قبایل پارسی بودند که
از قبایل دیگر شریف‌تر وبرتر بودند و بهمین مناسبت نام ناحیه‌ا ی که آنها بعد از
مهاجرنشان در آنجا قرا رگرفته‌اند پاسارگاد نامیده شده است ,

واژه پاسارگاد در یونانی بصورت پاسارگادای 32۵788۵8 آمده و بعد در
زبان انگلیسی بصورت 72827820462 ودر زبان فرانسوی بصورت ۳29278206 پاسارگاد
تلفظ میشود.

این واژه مر کب از دو جزء است: جزء نخستین آن پاسار» همان پارسه ۲38۸
اس ت که قلب شده است وجزء دوم آن» «گده» را میتوان به سه طریق تحلیل کرد .

یکی اینکه در اصل «گرد» بوده استء در اینصورت پاسارگاد به معنی‌حصار
و بارو وقلعه پارسیان است.

اما | گربصورت« کرده»و « کرته»» بوده باشدء» بمعنی‌ساخته پارسیان وروستای
پارسیان است . مانند جزء دوم در واژه (دستکرد) و(دستجرد)وغیره .همچنین ممکن
است جزء دوم آن یک «کد» و «گد» قدیمی باشد که بصور تکند بمعنی روستا
وشهر هنوز هم در آذربایجان بکار می‌رود ودر نامهای سمرقند وتاشکند وغیره هم
دیده میشود . در این صورت پاسارگاد به معنی روستا یا شهر پارسیان است .

بل
```


## [2026-09-07T20:43:19.261Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27900,27925p' MON_part1.txt; echo \"=== پهلو in MON\"; grep -n \"^پهلو\\|پهلوان:\\|پهلوی:\\|پهلو:\" MON_part1.txt MON_part2.txt | head -12"
}
```


### [2026-09-07T20:43:19.334Z] TOOL RESULT

```
پاراه: 22-0 (امر.) گذرگاه؛ معبر . 

پارت: ۲8۳ (.) (جاذ.) پرنده‌ای از راستة پا 
بلندان که دارای منقاری طویل و استخوان 
کف پایش طویل و برهنه و انگشتانش نیز 
دراز و جدا| از هم است. قدش متوسط و 
تقر یبا به اندازة یکك کبک است. این پرنده 
در نیمکر ة شمالی زمین در چین و هندوستان 
و دیگر نواحی آسیای مرکزی و اروپا و 
آمریکا می‌زید؛ نوک دراز» بلوه. 

پارتی: آ-03:0 (ص‌نسه.) منسوب به پارت. 
از قوم پارت؛ از مردم پارت. زبان مردم 
بارت؛ زبان پهلوی اشکانی. 

تساو نی 2111 (۱.) دسته» گر وه فر قه» 
جمعیت. قسمت» بجش. حامی؛ طر فدار؛ 
پشتیبان؛ طر فدار دی‌نفود. 

پارج: ۵ (.) آب پاش بزرگك. ظرف 
آبخوری سر گشاد سفالین یا بلورین و یا 
فلری. 

پارچه: (*)2:2م [پار - پاره + چه. پس. 
تص.] (ا.مصف.) باره» تکه» قطعه: یک پارچه 
=== پهلو in MON
MON_part1.txt:139:پهلوی) منصوب گردید و خطابه‌ای تحت عنوان «هورقلیام به زبان فرانسه ایراد 
MON_part1.txt:4033:آکندن پهلو: فربه شدن. آکندن یال: قوی 
MON_part1.txt:4052:آکنده پهلو: [11-.2 (ص‌مر.) سخت فر به» 
MON_part1.txt:14014:پهلو» دنده‌ها. (هس.) هر یکث از خطوط 
MON_part1.txt:19970:پهلو و نفریت و بیماری‌های حاد ریوی بکار 
MON_part1.txt:22368:پهلو یکدیگر زدن. پهلو به پهلو زدن» 
MON_part1.txt:26581:پهلوی وهیجک و پنجه وپنج‌وه و گاه و 
MON_part1.txt:33610:پهلو: تاطهم (.) (جاد.) دو طرف سینه و 
MON_part1.txt:33619:پهلوی ناز خفتن: در ستر راحت و آسایش 
MON_part1.txt:33624:پهلو: رم« قاتاجم [ج بهله. ب. وم بارت ] 
MON_part1.txt:33642:پهلوان: ۳۰01۵۲-20 (ص‌نسب. امر.) منسوب 
MON_part1.txt:33655:پهلو ان پنه: (۵-)02:۱02-.0 (امر.) مسخر ه‌ای
```


## [2026-09-07T20:43:20.069Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/ 2>/dev/null; ls incoming/ARY 2>/dev/null | head; echo ---; ls ocr | head -30"
}
```


### [2026-09-07T20:43:20.126Z] TOOL RESULT

```
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
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
---
AFM
ARY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
TAD
```


## [2026-09-07T20:43:26.813Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33605,33660p' MON_part1.txt"
}
```


### [2026-09-07T20:43:26.858Z] TOOL RESULT

```
پهرو: ۲۳5 (.) وصله» پینه» دربی. 
پسهره. (0-)02۲۸ (.) باس محافظطت» 
نگهبانی. 

پهلو: تاطهم (.) (جاد.) دو طرف سینه و 
شکم» جنب؟ ج. بهلوها» بهلوان. شکم» 
بطن. جنب» نزدیکك» در جوار. نزد» پیش. 
(رض.) ضلع. ضح. فرهنگستان نیز «یهلوم را 
بجای ضلع پذ برفته. نفع» فابده» سود. بهلوی 
چرب: پهلو و جانبی که چرب باشد. سود 
بسیار» فایدة کثیر. از پهلوی کسی کاری 
کردن: کاری به کمکك وی کردن. از پهلوی 
رن رو کرو ی 
پهلوی ناز خفتن: در ستر راحت و آسایش 
غنودن. پهلوی کسی راه رفتن: در عرض او 
رفتن» برابر او رفتن. پهلوی کسی را خاریدن: 
کاستن از وی. 

پهلو: رم« قاتاجم [ج بهله. ب. وم بارت ] 
(ص. .) پارت. در عهد ساسانی عنوان و 
لقب رسای خاندان‌های «قارن» و «سورن» 
و راسپاهبذ» که از نژاد اشکانیان بودند: 
قارن پهلو» سورن‌پهلو» اسیاهبذ بهلو. همان 
گونه که اسم «ماد» - قوم بزرگ شمال و 
شمال غربی ایران - بعد‌ها صورت «ماه» 
(بهلوی ماد) به عده‌ای از شهر ها مانند: 
ماه‌نهاوند» ماه‌یصر ه ما کو فه ماهی‌دشت و 
غبره اطلاق شده. نمز نام «بهل»» «بهلو و 
«پهله, به عده‌ای از شهرها و نواحیی که با 
وم مذ کور رابطه داشتند» اطلاق گر دیده از 
آن جمله: پهل‌شاهسدان که ارشک بزرگك» 
موّسس سلسلهة اشکانی در آنجا سلطنت را 
بدست گرفت (ظاهراً گرگان کنونی)؛ بعدها 
«پهلو» به معنی شهر گرفته شده. دلیر» 
شجاع» گرد بهلوان. 

پهلوان: ۳۰01۵۲-20 (ص‌نسب. امر.) منسوب 
به بهلو. سخت توانا و دلیر» شجاع. درشت 


اندام» عظیم جثه. درشت گوی. مرد اصلی 


که در داستانی شرح اعمال او روایت شود 
قهرمان. کشتی‌گیر. پهلوان پایتخت: رئیس 
بهلوانان» پهلوان بهلوانان. بهلوان جهان: 
بزرگترین پهلوان دنیا. قهرمان عالم» جهان 
بهلوان. 

پهلو ان پنه: (۵-)02:۱02-.0 (امر.) مسخر ه‌ای 
که تمام تن خود را به پنبه گیرد و خودبا 
حلاجی که کمان در دست دارد به رقص 
درآید و حلاج در میان رقص اند ک اند کك 
بهلوان را با زدن کمان برهنه کند بعنی تمام 
پنبه‌های بدن او را بر باد دهد.
```


## [2026-09-07T20:43:27.213Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"پارس\\|پهلو\\|پارت\" ARY_pages.txt | head -20"
}
```


### [2026-09-07T20:43:27.261Z] TOOL RESULT

```
18:واژه‌ی فارسی وجود دارد که ریشه‌پابی آنها تا حد پهلوی و اوستایی و حتی پارسی‌باستان پیگیری
21:۲- کوشش کرده‌ام که پیگیری واژه‌های فارسی را در این مسیر انجام دهم: فارسی -> پهلوی >"
22:ارستایی -> پارسی‌باستان -> هند و اروپایی. ولی به دلائلی که در دیباچه آمده همیشه تتوانسته‌ام شاهد
23:اوستایی با پارسی‌باستان (و گهگان حتی شاهد پهلوی) واژه را ارائه دهم.
25:نیز آورده‌ام تا خویشی زبان‌های ایرانی امروز و رابطه‌ی آنها با پهلوی و اوستایی و پارسی‌باستان و
36:امیدوارم که این کتاب دوست‌داران زبان پارسی و زبانشناسی را خوش آید.
225:لا در زبان‌های هند و ایرانی این واژه بدین صورت است (فارسی: مار؛ کردی: +۸۸7 پهلوی:
240:۱ وجود دارد و این زبانها نیز (به ویژه پارسی کهن و اوستایی) شباهت زیادی با زبانهای شبیه قاروی.
316:نیستند. مثلاً ریشه‌ی هند و اروپابی --۳01" (فارسی: کوه؛ اوستایی: 4617077۸ پارسی کهن
436:قرار داد جیمز پارسونز انگلیسی (۳۸1۹80118 7۸/88) بود. او در کناب قطور خود
439:زیر که اعداد از یک تا ده و سپس صد را در چندین زبان نشان می‌دهد نخستین بار توسط پارسوئز .. .
523:باشند. همچنین زبان پارسی کهن را نیز می‌توان جزء این خانواده مسحسوب نمود.
525:بر ویلیام جونز به ریشه‌ی مشترک این زبانها اشاره کرد ولی او هم مانند جیمز پارسونز به
576:۱-فارسی: زانو > پهلوی: - پارسی کهن:2۸17171۸ + اوستایی: 8770717 *هند و
691:نخستین اشاره به اقوام ایرانی (مادها و پارس‌ها) در متون آسودی وابسته به قرن نهم پیش از
692:میلاد آمده است. در این متون ذ کر شده است که شاهان پارسی به «شلمنسر» :
694:این متون چنین برداشت می‌شود که مادها و پارس‌ها تازه‌واردانی بودند که قبل از حدود قرن نهم پیش
726:است ولی چون شمار اینان معدود است شمار واژگان پارسی کهن نیز بهمان نسبت محدود است. پس . .
727:از گذشت زمان» پارسی کهن تبدیل به پارسی میانه (پهلوی) شد. پهلوی زبان ایرانیان در دوران .. ؛
729:ترکی) ز همچنین بهواسطه‌ی تطور طبیعی زبان» زبان پهلوی تبدیل ه فارسی نوین شد. امروزه مد
```


## [2026-09-07T20:43:43.321Z] TOOL CALL #33: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/peach\" \"https://www.etymonline.com/word/parchment\" \"https://www.etymonline.com/word/Parthian\"; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 382, roots Pârsa/Parth: peach, parchment, Parthian chains\" ; done"
}
```


## [2026-09-07T20:43:45.327Z] TOOL CALL #34: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88%D8%A7%D9%86\" \"https://en.wiktionary.org/wiki/Pasargadae\" \"https://en.wiktionary.org/wiki/peach\"; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 382: Parthian pahlavan; Pasargadae; peach\"; done"
}
```


### [2026-09-07T20:43:45.722Z] TOOL RESULT

```
### https://www.etymonline.com/word/peach
/home/sfmqrb/git/rishe/data/verification/sources/web/06a709e521e9343d.txt
### https://www.etymonline.com/word/parchment
/home/sfmqrb/git/rishe/data/verification/sources/web/0bb20166ac12233b.txt
### https://www.etymonline.com/word/Parthian
/home/sfmqrb/git/rishe/data/verification/sources/web/9a4f13522ca30d1e.txt
```


### [2026-09-07T20:43:48.787Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88%D8%A7%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/0df702ee5f15c7e2.txt
### https://en.wiktionary.org/wiki/Pasargadae
/home/sfmqrb/git/rishe/data/verification/sources/web/911751edc51e8147.txt
### https://en.wiktionary.org/wiki/peach
/home/sfmqrb/git/rishe/data/verification/sources/web/86f6a84461a16253.txt
```


## [2026-09-07T20:43:51.988Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 06a709e521e9343d 0bb20166ac12233b 9a4f13522ca30d1e; do echo \"########## $f\"; grep -n -i -m1 -A30 \"peach\\|parchment\\|Parthian\" $f.txt | head -60; done"
}
```


### [2026-09-07T20:43:53.311Z] TOOL RESULT

```
########## 06a709e521e9343d
1:URL: https://www.etymonline.com/word/peach
2-FETCHED: 2026-09-07T20:43:44Z
3-STATUS: 200
########## 0bb20166ac12233b
1:URL: https://www.etymonline.com/word/parchment
2-FETCHED: 2026-09-07T20:43:45Z
3-STATUS: 200
########## 9a4f13522ca30d1e
1:URL: https://www.etymonline.com/word/Parthian
2-FETCHED: 2026-09-07T20:43:45Z
3-STATUS: 200
```


## [2026-09-07T20:43:56.781Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 06a709e521e9343d 0bb20166ac12233b 9a4f13522ca30d1e; do echo \"########## $f\"; sed -n '1,80p' $f.txt; done"
}
```


### [2026-09-07T20:43:58.036Z] TOOL RESULT

```
########## 06a709e521e9343d
URL: https://www.etymonline.com/word/peach
FETCHED: 2026-09-07T20:43:44Z
STATUS: 200
TITLE: Peach - Etymology, Origin & Meaning

Peach - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of peach 

 peach (n.) 

 c. 1400 peche, peoche , "fleshy fruit of the peach tree" (late 12c. as a surname), from Old French pesche "peach, peach tree" (Old North French peske , Modern French pêche ), and directly from Medieval Latin pesca , from Late Latin pessica , variant of persica "peach, peach tree," from Latin mālum Persicum , literally "Persian apple," translating Greek Persikon malon , from Persis "Persia" (see Persian ).

 Old English had it as persue, persoe , directly from Latin. In ancient Greek Persikos could mean "Persian" or "the peach." The tree is native to China, but reached Europe via Persia. By 1663 William Penn observed peaches in cultivation on American plantations. Meaning "attractive woman" is attested from 1754; that of "good person" is by 1904. Peaches and cream in reference to a type of complexion is from 1901. Peach blossom as the delicate pink hue of the peach blossom is from 1702. Georgia has been the Peach State since 1939, though it was noted as a leading peach-grower by 1908.
 also from c. 1400 

 peach (v.) 

 "to inform against, betray one's accomplices," 1560s (earlier pechen , "to accuse, indict, bring to trial," c. 1400), a shortening of appeach , empeach , obsolete variants of impeach . For form, compare peal (v.), also Middle English pelour "an accuser," from appellour . Related: Peached ; peaching; peacher .
 also from 1560s 

 Entries linking to peach 

 impeach (v.) 

 formerly also empeach , late 14c., empechen , "to impede, hinder, prevent;" early 15c., "cause to be stuck, run (a ship) aground," also "prevent (from doing something)," from Anglo-French empecher , Old French empeechier "to hinder, stop, impede; capture, trap, ensnare" (12c., Modern French empêcher ), from Late Latin impedicare "to fetter, catch, entangle," from assimilated form of in- "into, in" (from PIE root *en "in") + Latin pedica "a shackle, fetter," from pes (genitive pedis ) "foot" (from PIE root *ped- "foot").

 In law, at first in a broad sense, "to accuse, bring charges against" from late 14c.; more specifically, of the king or the House of Commons, "to bring formal accusation of treason or other high crime against (someone)" from mid-15c. The sense of "accuse a public officer of misconduct" had emerged from this by 1560s. The sense shift is perhaps via Medieval Latin confusion of impedicare with Latin impetere "attack, accuse" (see impetus ), which is from the Latin verb petere "aim for, rush at" (from PIE root *pet- "to rush, to fly").

 The Middle English verb apechen , probably from an Anglo-French variant of the source of impeach , was used from early 14c. in the sense "to accuse (someone), to charge (someone with an offense)." Related: Impeached ; impeaching .

 peal (v.) 

 1630s, "sound loudly, resound" (intransitive), from peal (n.). Transitive sense of "to utter or cause to ring loudly and sonorously" is by 1714. Related: Pealed ; pealing .

 Persian 
 peachy 
 See All Related Words (5) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 talk 

 c. 1200, talken, "speak, discourse, say something," probably a diminutive or frequentative form related to Middle English tale "story," and ultimately from the same source as tale (q.v.), with rare English formative -k (compare hark from hear, stalk from steal, smirk from smile) 

 tattle 

 late 15c., in Caxton's translation of "Reynard the Fox," "to stammer, prattle like a baby," senses now obsolete, probably from Middle Flemish tatelen "to stutter," parallel to Middle Dutch, Middle Low German, East Frisian tateren "to chatter, babble," Middle English tatteren "spe

 blab 

 mid-15c., blabben, "to talk idly and foolishly, talk too much," apparently from Middle English noun blabbe "one who does not control his tongue" (late 13c.), which probably is echoic (compare Old Norse blabbra, Danish blabbre "babble," German plappern "to babble"). It is attested

 drupe 

 stone-fruit," one with a fleshy or soft outer part and a hard nut or stone at the center (as a plum, cherry, apricot, or peach...

 apricot 

 Latin praecoquis early-ripe, can probably be attributed to the fact that the fruit was considered a variety of peach that...

 tell 

 Sense of "to reveal or disclose" is from c. 1400; that of "to act as an informer, to 'peach' " is recorded from 1901....

########## 0bb20166ac12233b
URL: https://www.etymonline.com/word/parchment
FETCHED: 2026-09-07T20:43:45Z
STATUS: 200
TITLE: Parchment - Etymology, Origin & Meaning

Parchment - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of parchment 

 parchment (n.) 

 c. 1300, parchemin (c. 1200 as a surname), "the skin of sheep or goats prepared for use as writing material," from Old French parchemin (11c., Old North French parcamin ) and directly from Medieval Latin pergamentum, percamentum , from Late Latin pergamena "parchment," a noun use of an adjective (as in pergamena charta , attested in Pliny), from Late Greek pergamenon "of Pergamon," from Pergamon "Pergamum" (modern Bergama), the city in Mysia in Asia Minor where parchment supposedly first was adopted as a substitute for papyrus in 2c. B.C.E.

 The form of the word was possibly influenced in Vulgar Latin by Latin parthica (pellis) "Parthian (leather)." The unetymological Middle English -t probably is by influence of words in -ent (compare ancient ) and by influence of Medieval Latin collateral form pergamentum .

 Technological advances in the production of cheap paper eventually restricted parchment's use largely to formal documents, hence parchment in the sense of "a certificate" (by 1888).
 also from c. 1300 

 Entries linking to parchment 

 ancient (adj.) 

 late 14c., auncyen , of persons, "very old;" c. 1400, of things, "having lasted from a remote period," from Old French ancien "old, long-standing, ancient," from Vulgar Latin *anteanus , literally "from before," adjectivization of Latin ante "before, in front of, against" (from PIE *anti "against," locative singular of root *ant- "front, forehead").

 From early 15c. as "existing or occurring in times long past." Specifically, in history, "belonging to the period before the fall of the Western Roman Empire" (c. 1600, contrasted with medieval and modern ). In English law, "from before the Norman Conquest."

 As a noun, "very old person," late 14c.; "one who lived in former ages," 1530s. Ancient of Days "supreme being" is from Daniel vii.9. Related: Anciently .

 *

 The unetymological -t dates from 15c. and probably is from confusion with or by influence of words in -ent, -ant (suffix of nouns formed from present participles of verbs in first Latin conjugation).

 The same process affected cormorant , parchment , pageant , peasant (in French), pheasant , tyrant (in French), also talaunt , former Middle English variant of talon , etc.and perhaps also currant , truant , pennant , allowing them to "simulate Latin endings to which, etymologically, they have no right." [Fitzedward Hall, "Modern English," 1873]

 -ent 

 word-forming element making adjectives from nouns or verbs, from French -ent and directly from Latin -entem (nominative -ens ), present-participle ending of verbs in -ere / -ire . Old French changed it in many words to -ant , but after c. 1500 some of these in English were changed back to what was supposed to be correct Latin. See -ant .

 biblio- 

 word-forming element meaning "book" or sometimes "Bible," from Greek biblion "paper, scroll," also the ordinary word for "a book as a division of a larger work;" originally a diminutive of byblos "Egyptian papyrus." This is perhaps from Byblos , the Phoenician port from which Egyptian papyrus was exported to Greece (modern Jebeil, in Lebanon; for sense evolution compare parchment ). Or the place name might be from the Greek word, which then would be probably of Egyptian origin. Compare Bible . Latin liber (see library ) and English book also are ultimately from plant-words.

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 scroll 

 c. 1400, scroule, scrowell, "roll of parchment or paper" used for writing, an altered (by association with rolle "roll")...of scrowe (c. 1200), from Anglo-French escrowe, Old French escroe, escroele "scrap, strip or roll of parchment," from Frankish...

 roll 

 c. 1200, rolle, "rolled-up piece of parchment or paper, scroll" (especially one inscribed with an official record), from...Old French rolle "document, parchment scroll, decree" (12c.), Medieval Latin rotulus "a roll of paper" (source also of Spanish...

 palimpsest 

 "parchment from which earlier writing has been removed to clear it for new writing," 1660s, from Latin palimpsestus, from...

 indenture 

 Such contracts (especially between master craftsmen and apprentices) were written in full identical versions on a sheet of parchment...

 quire 

 quaier, caier "sheet of paper folded in four" (Modern French cahier), from Medieval Latin quaternum, "set of four sheets of parchment...

 tambourine 
########## 9a4f13522ca30d1e
URL: https://www.etymonline.com/word/Parthian
FETCHED: 2026-09-07T20:43:45Z
STATUS: 200
TITLE: Parthian - Etymology, Origin & Meaning

Parthian - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of Parthian 

 Parthian (n.) 

 1520s, native or inhabitant of Parthia (ancient kingdom northeast of Persia in western Asia), from Old Persian Parthava- "Parthian," dialectal variant of the stem Parsa- , source of Persia . Partienes (plural) "Parthians" is attested from c. 1300.

 As an adjective, "of or pertaining to the Parthians," by 1580s. The phrase Parthian shot is a figurative reference to their horsemen, who were expert at racing forward, turning, and shooting arrows backward at the moment of retreat. The exact phrase is attested by 1832; the image itself was in use long before (for example Parthian fight , 1630s).

 Or, like the Parthian, I shall flying fight ["Cymbeline," Act I, Scene VII]
 also from 1520s 

 Entries linking to Parthian 

 Persia 

 c. 1200, Perse , "land of the Persians," from Latin Persia "Persia," from Greek Persis , from Old Persian Parsa (cognate with Persian Fars , Hebrew Paras , Arabic Faris ).

 Pahlavi (n.) 

 1773, Iranian language spoken in Persia 3c.-10c., the language of the sacred books of the Zoroastrians, from Persian Pahlavi , from Old Persian Parthava "Parthia" (see Parthian ).

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 parchment 

 The form of the word was possibly influenced in Vulgar Latin by Latin parthica (pellis) "Parthian (leather)."...

 Asian 

 late 14c., "inhabitant of Asia (Minor)," from Latin Asianus (adjective and noun, "belonging to the province of Asia;" "an inhabitant of Asia"), from Greek Asianos "Asiatic," from Asia (see Asia). It ousted Asiatic as the preferred term mid-20c. The term "Asiatic" has come to be 

 fight 

 Old English feohtan "to combat, contend with weapons, strive; attack; gain by fighting, win" (intransitive; class III strong verb; past tense feaht, past participle fohten), from Proto-Germanic *fe(u)hta (source also of Old High German fehtan, German fechten, Middle Dutch and Dut

 Albuquerque 

 city in New Mexico, founded 1706 and named for Spanish administrator and viceroy of Mexico Francisco Fernández de la Cueva, Duque de Alburquerque (1617-1676); the name subsequently was altered by association with Portuguese hero Alfonso d'Albuquerque (1453-1515), the "Portuguese 

 Gothic 

 "of the Goths," the ancient Germanic people, "pertaining to the Goths or their language," 1610s, from Late Latin Gothicus, from Gothi, Greek Gothoi (see Goth). Old English had Gotisc. As a noun, "the language of the Goths," from 1757. Gothic was used by 17c. scholars to mean "Ger

 icon 

 also ikon, 1570s, "image, figure, picture," also "statue," from Late Latin icon, from Greek eikon "likeness, image, portrait; image in a mirror; a semblance, phantom image;" in philosophy, "an image in the mind," related to eikenai "be like, look like," which is of uncertain orig

 election 

 c. 1300, eleccioun, "act of choosing" someone to occupy a position, elevation to office" (whether by one person or a body of electors); also "the holding of a vote by a body of electors by established procedure; the time and place of such a vote," from Anglo-French eleccioun, Old

 loop 

 late 14c., "a fold or doubling of cloth, rope, leather, cord, etc.," of uncertain origin. OED favors a Celtic origin (compare Gaelic lub "bend," Irish lubiam), which in English was perhaps influenced by or blended with Old Norse hlaup "a leap, run" (see leap (v.)). As a feature o

 mood 

 "emotional condition, state of mind as regards passion or feeling," c. 1300, from Old English mod "heart, frame of mind, spirit; courage, arrogance, pride; power, violence" (also used to translate Latin animus, mens), from Proto-Germanic *mōda- (source also of Old Saxon mod "mind
```


## [2026-09-07T20:44:29.316Z] TOOL CALL #37: Bash

```json
{
 "command": "for u in \"https://www.ahdictionary.com/word/search.html?q=parchment\" \"https://www.ahdictionary.com/word/search.html?q=peach\" \"https://www.ahdictionary.com/word/search.html?q=Parthian\" \"https://www.etymonline.com/word/parting\"; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 382: AHD:952 parchment, AHD:963 peach, AHD:955 Parthian/parting shot\"; done"
}
```


## [2026-09-07T20:44:30.673Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### pahlavan\"; sed -n '1,120p' 0df702ee5f15c7e2.txt | grep -n -i -B3 -A20 \"Etymology\" | head -60"
}
```


### [2026-09-07T20:44:32.013Z] TOOL RESULT

```
### https://www.ahdictionary.com/word/search.html?q=parchment
/home/sfmqrb/git/rishe/data/verification/sources/web/de0a53b891e147ce.txt
### https://www.ahdictionary.com/word/search.html?q=peach
/home/sfmqrb/git/rishe/data/verification/sources/web/011b62dde870a80d.txt
### https://www.ahdictionary.com/word/search.html?q=Parthian
/home/sfmqrb/git/rishe/data/verification/sources/web/46de964006f4ef2a.txt
### https://www.etymonline.com/word/parting
/home/sfmqrb/git/rishe/data/verification/sources/web/b6b751e1585aaf67.txt
```


### [2026-09-07T20:44:32.059Z] TOOL RESULT

```
##### pahlavan
59- Toggle Ottoman Turkish subsection 
60-
61- 1.1 
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
75-
76- 2 
77- Persian 
78-
79- Toggle Persian subsection 
80-
81- 2.1 
82- Alternative forms 
83-
84- 2.2 
85: Etymology 
86-
87- 2.3 
88- Pronunciation 
89-
90- 2.4 
91- Noun 
92-
93- 2.4.1 
94- Derived terms 
95-
96- 2.4.2 
97- Related terms 
98-
99- 2.4.3 
100- Descendants 
101-
102- 2.5 
103- Proper noun 
104-
105- Toggle the table of contents
```


## [2026-09-07T20:44:35.317Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk 'NR>105' 0df702ee5f15c7e2.txt | grep -n -A12 \"^ Persian\" | head -80"
}
```


### [2026-09-07T20:44:36.785Z] TOOL RESULT

```
141: Persian
142- [ edit ] 
143-
144: Persian Wikipedia has an article on: پهلوان 
145-
146- Wikipedia fa 
147-
148- Alternative forms
149- [ edit ] 
150-
151- پهلوون ( pahlevun ) ( eye-dialect ) 
152-
153- Etymology
154- [ edit ] 
155-
156- Ultimately from the name of the Parthians . Compare پهلو ( pahlav ) , پهلوی ( pahlavi ) .
--
292: Persian terms with IPA pronunciation 
293- Rhymes:Persian/aːn 
294- Rhymes:Persian/aːn/3 syllables 
295: Persian lemmas 
296: Persian nouns 
297: Persian terms with archaic senses 
298: Persian proper nouns 
299: Persian surnames 
300-
301- Hidden categories: Pages with entries 
302- Pages with 2 entries 
303- Bengali terms with non-redundant manual transliterations 
304-
305- This page was last edited on 5 May 2026, at 21:59.
306-
307- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
308-
309- Privacy policy 
310-
311- About Wiktionary
```


## [2026-09-07T20:44:37.262Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in de0a53b891e147ce 011b62dde870a80d 46de964006f4ef2a; do echo \"##### $f\"; grep -n -i \"Parthica\\|pergam\\|Persicum\\|Parthav\\|Middle English\\|Old French\" $f.txt | head -12; done; echo \"##### parting\"; grep -n -i -A6 \"parting\" b6b751e1585aaf67.txt | head -40"
}
```


### [2026-09-07T20:44:38.645Z] TOOL RESULT

```
##### de0a53b891e147ce
50: [Middle English parchemin, parchement (influenced by Medieval Latin pergamentum ), from Old French parchemin , from Late Latin pergam ī na , variant of Latin pergam ē na , from feminine of Pergam ē nus , of Pergamum, from Greek Pergam ē nos , after Pergamon (Pergamum).]
##### 011b62dde870a80d
52: [Middle English peche , from Old French, a peach, from Latin persica , peach tree, from Greek persik ē , from feminine of Persikos , Persian; see PERSE .]
66: [Middle English pechen , from apechen , to accuse (probably from Anglo-Norman *anpecher , from Late Latin impedic ā re , to entangle; see IMPEACH ) and from empechen , to accuse; see IMPEACH .]
##### 46de964006f4ef2a
##### parting
1:URL: https://www.etymonline.com/word/parting
2-FETCHED: 2026-09-07T20:44:31Z
3-STATUS: 200
4:TITLE: Parting - Etymology, Origin & Meaning
5-
6:Parting - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
--
21: Origin and history of parting 
22-
23: parting (n.) 
24-
25- mid-13c., "the act of going away, departure;" c. 1300, "separation of persons, leave-taking," also "the act of dividing or putting asunder; distribution, apportionment;" verbal noun from part (v.). From late 14c. as "the act or process of dividing; a division or separation; a dividing line, a point or place of separation or division."
26- also from mid-13c. 
27-
28: Entries linking to parting 
29-
30- part (v.) 
31-
32- c. 1200, parten "to depart, leave;" late 13c., "cause (things, persons) to separate;" from Old French partir "to divide, separate" (10c.), from Latin partire / partiri "to share, part, distribute, divide," from pars "a part, piece, a share" (from PIE root *pere- (2) "to grant, allot").
33-
34: Meaning "divide" (something), especially "divide by cutting or cleaving" is from c. 1300; that of "to share something" (with others) is from early 14c. Of persons, "to separate from one another," early 14c., also intransitive, "draw or hold (persons) apart, separate by intervening." Intransitive sense of "become disunited" is from early 14c.; that of "be divided or severed" is from 1570s. Meaning "to separate the hair, comb the hair away from a dividing line" is attested from 1610s. Related: Parted ; parting . To part with "surrender" is from 1580s; earlier it meant "to share with" (mid-13c.).
35-
36- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
37-
38- More to explore
39-
40- leave 
--
50: it was said to the party left (farewell was to the party setting forth), but in English it came to be used as a general parting...Compare the native parting salutation good-bye, a contraction of God be with ye....
51-
52- severance 
53-
54: difference," also, of apprentices, "release from previous obligations," from Anglo-French, from Old French sevrance "separation, parting...
55-
```


## [2026-09-07T20:44:51.924Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### AHD Parthian file\"; sed -n '20,70p' 46de964006f4ef2a.txt; echo \"### wikt Pasargadae\"; grep -n -i -A10 \"Etymology\" 911751edc51e8147.txt | head -40"
}
```


### [2026-09-07T20:44:51.978Z] TOOL RESULT

```
### AHD Parthian file

-->
 AMERICAN HERITAGE DICTIONARY APP
 The new American Heritage Dictionary app is now available for 
 iOS and Android. 

 THE AMERICAN HERITAGE DICTIONARY BLOG
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.

 OPEN DICTIONARY PROJECT

 Share your ideas for new words and new meanings of old words!

 Start Sharing Now! 

 --> See word lists from the best-selling 100 Words Series!
 Find out more! 

 INTERESTED IN DICTIONARIES?
 Check out the Dictionary Society of North America at http://www.dictionarysociety.com 

 Par·thi·an (pär  th ē - ə n) 
 Share: 

 Tweet 

 adj. 1. Of or relating to Parthia or its people, language, or culture.
 2. Delivered in or as if in retreat: "a Parthian volley of expletives from Uncle Billy" (Bret Harte). 

 n. 1. A native or inhabitant of Parthia.
 2. The Iranian language of the Parthians.

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatment of Indo-European roots and the English words derived from them is available in our Dictionary of Indo-European Roots .

 American Heritage Dictionary Products
 The American Heritage Dictionary, 5th Edition

 The American Heritage Dictionary of Idioms

 The American Heritage Roget's Thesaurus

 Curious George's Dictionary

 The American Heritage Children's Dictionary

### wikt Pasargadae
62: Etymology 
63-
64- 1.2 
65- Proper noun 
66-
67- 1.2.1 
68- Translations 
69-
70- 2 
71- Latin 
72-
--
76: Etymology 
77-
78- 2.2 
79- Pronunciation 
80-
81- 2.3 
82- Proper noun 
83-
84- 2.3.1 
85- Declension 
86-
--
163: Etymology
164- [ edit ] 
165-
166- Borrowed from Latin Pasargadae , from Ancient Greek Πασαργάδαι ( Pasargádai ) , ultimately from Old Persian *Pāθragadā . Doublet of Pasargad .
167-
168- Proper noun
169- [ edit ] 
170-
171- Pasargadae 
172-
173- ( historical ) An ancient city of Persia , a capital of the Achaemenid Empire .
--
221: Etymology
222- [ edit ] 
223-
224- Borrowed from Ancient Greek Πασαργάδαι ( Pasargádai ) , from Old Persian *Pāθragadā .
```


## [2026-09-07T20:44:53.342Z] TOOL CALL #42: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/parting_shot\" \"https://en.wiktionary.org/wiki/Parthian_shot\" \"https://en.wiktionary.org/wiki/p%C3%AAche_Melba\"; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 382: parting shot / Parthian shot / peche Melba\"; done"
}
```


### [2026-09-07T20:44:56.281Z] TOOL RESULT

```
Exit code 1
### https://en.wiktionary.org/wiki/parting_shot
/home/sfmqrb/git/rishe/data/verification/sources/web/a6743c07dae52e0c.txt
### https://en.wiktionary.org/wiki/Parthian_shot
/home/sfmqrb/git/rishe/data/verification/sources/web/ab62cce6ec083b54.txt
### https://en.wiktionary.org/wiki/p%C3%AAche_Melba
/home/sfmqrb/git/rishe/data/verification/sources/web/10a472dfd05a9fb2.txt
```


## [2026-09-07T20:45:05.760Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in a6743c07dae52e0c ab62cce6ec083b54 10a472dfd05a9fb2; do echo \"##### $f\"; grep -n -A8 \"^ Etymology$\" $f.txt | sed -n '1,40p'; done"
}
```


### [2026-09-07T20:45:07.019Z] TOOL RESULT

```
##### a6743c07dae52e0c
143: Etymology
144- [ edit ] 
145-
146- Believed to be a variation of Parthian shot , referring to a military maneuver in which Parthian troops retreating on horseback turned back to face the enemy and shot while retreating. [ 1 ] [ 2 ] 
147-
148- Pronunciation
149- [ edit ] 
150-
151- Audio ( Australia ) : ( file ) 
##### ab62cce6ec083b54
136: Etymology
137- [ edit ] 
138-
139- The military tactic was made famous in Rome by the Parthians , an empire on their eastern border.
140-
141- Noun
142- [ edit ] 
143-
144- Parthian shot ( plural Parthian shots ) 
##### 10a472dfd05a9fb2
```


## [2026-09-07T20:45:07.460Z] TOOL CALL #44: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/pasargadae\" --note \"page 382: Pasargadae name etymology\" ; timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88\" --note \"page 382: Persian pahlav/pahlu\""
}
```


### [2026-09-07T20:45:14.756Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ff7e9b1baa06d2b4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/93eaf6e5d0758898.txt
```


## [2026-09-07T20:45:19.098Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### iranica\"; grep -n -i \"name\\|etymolog\\|Pasargadai\\|Pāθra\\|camp\" ff7e9b1baa06d2b4.txt | head -25; echo; echo \"### wikt پهلو\"; grep -n -B2 -A10 \"^ Etymology\" 93eaf6e5d0758898.txt | head -60"
}
```


### [2026-09-07T20:45:19.179Z] TOOL RESULT

```
### iranica
57: The Name. In 1967, shortly before the completion of his monograph on the Achaemenid Elamite “fortification tablets” found at Persepolis, R. T. Hallock came to realize (D. Stronach, personal communication) that the toponym Batrakata(s), which appears in this and other variant spellings on seven of the tablets, could well represent the Elamite form of the name of Cyrus’ capital.  As Hallock (1969, p. 676) went on to indicate, this attractive possibility (first suggested by the relative closeness of the Elamite name to the well-known Greek form of the name, Pasargadai) finds a degree of corroboration in the contents of the tablets in question (dated to the years 497-491) in that they refer, inter alia , to a “royal treasury” and to “royal stores” at this location (see BATRAKATAŠ ), the name is first mentioned by Herodotus (i.125), who relates that this was the name of the most renowned of the Persian tribes. But since Herodotus fails to mention Pasargadae as a place-name, the possibility that this claim was based on erroneous information cannot be completely discounted.  For many years the only additional support for the name as a tribal designation came from the claims of two much later classical writers (see, e.g., Ptolemy, vi.8.12), to the effect that there was a tribe of this name in Carmania, and to Hans Triedler’s not unreasonable conclusion (1962, col. 778) that the tribe in question could have migrated to this new location. Subsequently, Ilya Gershevitch, in response to the fact that the Greek name happens to occur in a plural form (such as could conceivably refer to a tribal entity as well as to the site), and in response to the newly available Elamite etymologies contained in the fortification tablets, has suggested that the original Iranian tribal name could have held the meaning “those who wield solid clubs” (Gershevitch, 1969, p. 168).
58: In the main, however, scholarly debate has concentrated on the likely spelling and meaning of the Iranian place-name that stand behind the classical place-name. In this context, most commentators have taken the view that there could have been a metathesis in the form of the name and they have presumed that, in its original form, it would have begun with the spelling “Parsa.” (For hypothetical reconstructions based on this premise, see Stronach, 1978, pp. 280-81 and Boucharlat, 2004, p. 352).  It is most unlikely, however, that the readily recognizable form “Parsa” would have undergone a transformation into something else (Martin Schwartz, private communication); and, beyond this, the character of the newly discovered Elamite name, combined with the weight of classical testimony (rehearsed in detail in Triedler, 1962) would seem to rule out the likelihood of the proposed metathesis.  If evidence to the contrary is sought, one has to refer either to the first century writings of Quintus Curtius (where the spelling “Parsagada” is attested) or to an explanation given, presumably by a Persian informant, to the historian of the late fourth century BCE, Anaximenes of Lampsakos, to the effect that the name of Cyrus’ capital meant “encampment of the Persians” (Anaximenes, Frag. 19J).  Moreover, as A. D. H. Bivar (1978, p. 162) has pointed out, the reading “…psrgd[h]” in an Aramaic summary of a very fragmentary, longer Greek text on a Seleucid milestone that was discovered on the Tall-i Takht in the early 1960s (Stronach, 1978, pl. 136) supports the view that the site was known to the Greeks of the fourth century BCE by a name with the spelling “‘Pasargadai’ rather than… ‘Parsagada’—the variant spelling offered by Quintus Curtius.  In addition, the long-popular belief that the name of Cyrus’ capital once began with the spelling “Parsa” finds little support on historical grounds.  As the inscriptions of Darius I (522-486 BCE) make plain, it was this latter monarch who chose to underline the explicitly Persian character of his patrimony: a circumstance that led him to rename the ancient highland of southwestern Iran (formerly Anshan ) as “Parsa” and, above all else, to bestow the same name on his new home-capital, Persepolis.
59: Early Travelers. Lying squarely on the traditional route from Shiraz to the north of Persia, the ruins of Pasargadae were long known to travelers to the Middle East. As early as 1474 the Venetian Giosafat Barbaro writes of “the tomb of the Mother of Solomon,” the local designation for the structure that would later be identified as the tomb of Cyrus, and a century later Albrecht von Mandelslo included an illustration of the tomb in his account of his visit to Fārs ( FIGURE 1 ). The Dutch traveler Jan Struys, who visited the site in 1672, gives further details about the role of the tomb as an object of female devotion (Struys, p. 331), a theme that recurs in the accounts of nearly all visitors to the site until the early twentieth century. James Morier, the British emissary to the Persian court, included a detailed description of several of the standing features at Pasargadae in the vivid account of his travels published in 1812 (Morier, p. 144). Struck by the resemblance between the tomb of the Mother of Solomon and classical descriptions of the tomb of Cyrus, Morier was also the first writer to give serious consideration to the possibility that the site should be identified as the ancient city of Pasargadae. He ventured the suggestion only to reject it, however, on the grounds that the site was too far north to match Persian geography as described by Pliny and other classical writers.  A few years later, however, Morier’s  suggestion was revived by Robert Ker Porter, the first visitor to attempt to take account of the testimony of Pasargadae’s still visible inscriptions.  An accomplished artist, Porter sent a drawing of one of the site’s trilingual cuneiform inscriptions to the pioneer decipherer of Old Persian, Georg Friedrich Grotefend .  When Grotefend was able to identify the presence of the name of Cyrus (cf. Barnett, p. 22), Porter concluded that “in comparing… the account given by Arrian of the Tomb of Cyrus at Pasargadae” with the still mysterious monument on the Murghab Plain, the resemblance between the two was “too exact not to bear an instant conviction” that they were “portraits of one and the same place” (Porter, p. 502).
77: The doorway reliefs from Palace P are both stylistically and thematically different from those at the rest of the site. Here we see a king dressed in a long pleated robe adorned with gold inlays, followed by an attendant. Inscriptions on the pleats of the robe identify the depicted monarch as Cyrus but the style of the pleats can be associated with the reign of Darius, and all current evidence suggests that Darius sought to reify his connection with the heritage of Cyrus by completing several elements of Cyrus’ unfinished program of construction, creating these gold-enriched reliefs and inscribing Cyrus’ name, here and elsewhere, in a number of key locations (Stronach, 1997, p. 355; see also “Inscriptions and Chronology,” below).
89: Apart from these considerations, R. Borger and W. Hinz’s discovery that the name of Darius could be detected in the fragmentary CMb inscription (a trilingual inscription that once stood above each of the Palace P doorway reliefs) was another decisive factor. Especially in the context of the new findings of the 1970s it underscored the fact that the first person CMa inscription was now the one complete “Cyrus Murghab” text where the agency of Darius, not Cyrus, remained to be demonstrated.
102: Idem, “Pasargadai (Pasargades),” Reallexikon der Assyriologie und Vorderasiatischen Archäologie 10, 2004, pp. 351-63.
109: I. Gershevitch, “Iranian names and nouns in Elamite garb,” Transactions of the PhilologicalSociety , 1969, pp. 165-200.
148: H. Triedler, “Pasargadai,” Realencyclopädie der classischen Altertumswissenschaft 9, 1962, pp. 777-79.

### wikt پهلو
60-
61- 1.1 
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
--
80-
81- 2.1 
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
--
95-
96- 2.2 
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
--
174- [ edit ] 
175-
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
--
217- [ edit ] 
218-
219: Etymology 1
220- [ edit ]
```


## [2026-09-07T20:45:28.222Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '215,275p' 93eaf6e5d0758898.txt"
}
```


### [2026-09-07T20:45:28.267Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 Inherited from Middle Persian [script needed] ( pʾhlwk' /⁠pahlūg⁠/ ) , from Old Persian *parθukah , suffixed from Proto-Iranian *párcuš ( “ rib ” ) . [ 1 ] Compare Northern Kurdish parsû ( “ rib ” ) , Sanskrit पर्शु ( parśu , “ rib ” ) , Russian пе́рси ( pérsi , “ bosom ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /pah.ˈluː/ 

 ( Dari, formal ) IPA ( key ) : [pʰäɦ.lúː] 

 ( Dari, formal ) IPA ( key ) : [pʰäɦ.lúː] 
 ( Kabuli ) IPA ( key ) : [pʰɑː.lúː] 

 ( Hazaragi ) IPA ( key ) : [pʰɔː.lú] 

 ( Iran, formal ) IPA ( key ) : [pʰæɦ.lúː] 

 ( Tajik, formal ) IPA ( key ) : [pʰäɦ.lɵ́] 

 Rhymes: -uː 

 Readings

 Classical reading ? 

 pahlū

 Dari reading ? 

 pahlū

 Iranian reading ? 

 pahlu

 Tajik reading ? 

 pahlü

 Noun
 [ edit ] 

 پهلو • ( pahlu ) ( Tajik spelling паҳлӯ ) 

 side ; flank (of the body)
 Synonyms: کنار ( kenâr ) , بغل ( baġal ) 

 side ; beside 
 Synonyms: کنار ( kenâr ) , جنب ( janb ) 

 ( military ) flank (of an army)

 ( geometry ) side 
 Synonym: ضلع ( zel' )
```


## [2026-09-07T20:45:31.072Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '275,330p' 93eaf6e5d0758898.txt"
}
```


### [2026-09-07T20:45:31.114Z] TOOL RESULT

```
 Derived terms
 [ edit ] 

 پهلو به پهلو ( pahlu be pahlu , “ side by side ” ) 
 پهلو زدن ( pahlu zadan , “ to emulate; to vie ” ) 

 Descendants
 [ edit ] 

 → Hindustani: 
 Hindi: पहलू ( pahlū ) , पहल ( pahal ) 
 Urdu: پہلو ( pahlū ) , پہل ( pahal ) 

 → Ottoman Turkish: پهلو ( pehlû ) Turkish: pehlu 

 Etymology 2
 [ edit ] 

 Inherited from Middle Persian [Term?] ( /⁠pahlaw⁠/ ) , from Old Persian 𐎱𐎼𐎰𐎺 ( p-r-θ-v /⁠Parθavaʰ⁠/ , “ Parthian ” ) ; see there for more.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /pah.ˈlaw/ 

 ( Dari, formal ) IPA ( key ) : [pʰäɦ.láw] 

 ( Dari, formal ) IPA ( key ) : [pʰäɦ.láw] 
 ( Kabuli ) IPA ( key ) : [pʰɑː.láw] 

 ( Hazaragi ) IPA ( key ) : [pʰɔː.láw] 

 ( Iran, formal ) IPA ( key ) : [pʰæɦ.lów] 

 ( Tajik, formal ) IPA ( key ) : [pʰäɦ.láw] 

 Rhymes: -aw 

 Readings

 Classical reading ? 

 pahlaw

 Dari reading ? 

 pahlaw

 Iranian reading ? 

 pahlov

 Tajik reading ? 

 pahlav
```


## [2026-09-07T20:45:52.809Z] TOOL CALL #48: Bash

```json
{
 "command": "pdftoppm -f 382 -l 382 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg382 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg382.png"
}
```


## [2026-09-07T20:45:54.581Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSF page 117 tag\"; grep -n \"pdf page\" FSF_pages.txt | sed -n '110,130p'; echo \"== BRT parsa/pahlav\"; grep -n -i \"Pársa-\\|Parsa-\\|Pahlav\" BRT.txt | head -10; echo \"== MON پارس headword\"; grep -n \"^پارس:\\|پارس: \" MON_part1.txt | head"
}
```


### [2026-09-07T20:45:54.682Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 71714 Sep  7 16:45 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg382.png
```


### [2026-09-07T20:45:54.762Z] TOOL RESULT

```
== FSF page 117 tag
== BRT parsa/pahlav
2037:Über  die  philologischen  Grundsätze,  nach  denen  ich  mein  Wörterbuch  fürs Awestische  ausgearbeitet  habe,  mag  es  selber  Auskunft  gebea  Man  wird  finden, dass  die  Tradition'  überall  berücksichtigt  und  dass  sie  auch  da  zu  Wort  gekommen ist,  wo  sie  ganz  offenkundig  fehl  geht.  Ausser  den  veröffentlichten  Pahlavi-,  neu- persischen  und  Sanskrit-Übersetzungen  —  soweit  sie  mir  zugänglich  waren^*  — ,  habe ich  auch  einige  nur  handschriftlich  vorhandene  benutzt  und  ausgezogen,  insbesondere eine  neupersische  zu  Yt  14,  die  sich  in  M  4  findet.
2046:Das  Neupersische  ist,  wo  es  sich  um  Exegese  handelt,  nach  modemer  Aussprache umschrieben,  dagegen  bei  Anführungen  zu  etymologischem  Zweck  in  frühneupersischer Lautform.  Wegen  meiner  Transskription  der  Fahlaviwörter  vergleiche  man  die  in Wiener  Zeitschr,  für  die  Kunde  des  Morgenlandes  XIV.  S.  i8o  aufgestellten  Leit- Mtze;  Wörter,  die  ich  nicht  lesen  konnte,  sind  in  Steildruck  gegeben,  unter Berücksichtigung  der  getrennten  oder  verbundenen  Schreibung  der  Zeichen,  wobei selbstverständlich  für  die  mehrdeutigen  Zeichen  stets  der  selbe  Buchstabe  erscheint, z.  B.  d:  für  das  als  d,  g,  y,  r  usw.  lesbare  Zeichen,  da:  fdr  die  als  d<i,ya,  ih,  /  usw. lesbare  Zeichen  Verbindung.  Wer  mit  der  Fahlavischrift  vertraut  ist,  wird  sich  danach die  Originalform  des  Wortes  ohne  MUhe  herstellen  können.  'Fäzand'lesungen  sind in  Pahlavi  umgesetzt
2085:Toten  Verehrung:    Über  Totenverehrung   bei   einigen  indögernianijchen  Völkern.     Amsterdam 1888. Daeab(PSahj*na)  PahlVend.:  The   Pahlavi  Version  of  ihe  Avesta.     Bombay  1895. D.:  Dariui(-In Schrift);  s.  S.  v. Dbr.:  BDelbkOck.
2118:IF.:  Indogermanische  Forschungen.    Herausgeg.  von  KBRUGUAnn  und  WStreitberg.   Strassburg. IFAni.:  Anzeiger  usw.,  Beiblatt  zu  den  IF. JA:  Journal  Asiatiquc.     Paris. Jamaspji  (MJamaspAsana)  Dict.O:  Pahlavi  GujarSti  and  English  Diclionary.     Bombay   1877 ff.
2135:G.:  The   five  Zoroastrion  GSthSs  wilh  the  Zend,   Pahlavi,    Sanskrit   and   Perüan  Text«    and Traoslations.   1-eipzig  1895. USL:  Htmoires  de  la  Socittj  de  Lingniitique.    Paris. MS.:  MaiiräyariiiamAiiä,
2153:Upsala  1894. (R)vonPlanta  OUD.  :  Grammatik  der  oskisch-nmb tischen  Dialekte.     Stratsborg  i8gi,  1897. PPGI. :    An    o!d   Pahlavi-Paiand   Glossary.     Edited   ,.    by   HoshangjiJamaspji,    rcvised    ..   by
2179:V...  PdZ.:  Stat  der  Pahlavi&bersetiung  (Pa.)  mm  VUevdät. Vt.:  V^ai;  s.  S.  VIU.  I.
2409:O  hinter  Fü.  hei  Wörtern  aas  P.  bedeutet,  dass  die  Pahlaviübersetrong  weder  bei  Dakmesteteb noch  bei  Blochet  mitgeleilt  ist.
15815:•  j.  *parsa-''  m.  'Getreideähre,  Ähre': mqnay^n  ahe  yaä^a  nä  sai?mca  hazar?r»mca ,  .  'l'anqm'^  *nijat3irt  hyat  ".  .  als  ob  ein Mann  auf  hundert  und  tausend  . .  Ähren einschlüge"  Yt. /j.  71''.
25884:lende  du  pahlavi  iiWar'.  —  »  Wo  Hds.  so-
== MON پارس headword
27939:پارس: صق (اخ.) نامی قومی ایرانی ساکن 
27944:پارس: 2« [تر. ء بارس (.) یوزپلنگ. 
27945:پارس: 0 (اصت.) آواز سک» عوعوه
```


## [2026-09-07T20:45:58.854Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27930,27960p' MON_part1.txt"
}
```


### [2026-09-07T20:45:58.905Z] TOOL RESULT

```
باردان فرهنگ فارسی معین ۳۱۳ 
پاردان: 0 (امر.) جوال. تنگ» ظرف ماه. روزهای پارسی: سی روز ماه شمسی 
شراب. شراب. اپرانیان: «هر مزد» بهمن» اردیبهشت» شهریور 


پاردم: 0 ([ - پاره‌دم ] (امر.) چرمی که 
بر زین يا پالان می‌دوزند و زير دم اسب یا 
پس ران چاربا می‌انداز ند؛ رانکی» قشقون. 
پارس: صق (اخ.) نامی قومی ایرانی ساکن 
جنوب ایران. (تد.) یک در ارآ زار 
مذکو بارسی: (ند.) یک تن ابرانی» یرای 
(اح.) مسکن قوم مذ‌کور. 

پارس: 2« [تر. ء بارس (.) یوزپلنگ. 
پارس: 0 (اصت.) آواز سک» عوعوه 
هفهف» وغواغ» وعوع» وک وک نوف. 
پارسا: 2:05 [- پارسای] (ص.) آنکه از 
گناهان پرهیزد و به طاعت و عبادت و قناعت 
عمر گذارد) پرهیز کار» با کدامن» زاهد» 
مستقی. دبندار» مستد.ین» مسقدس. عارف» 
دانشمند) مق. ناپارسا؛ ج. بارسایان. 
پارسال: 027*51 (امر.) سال گذشته» پار. 
پارس ئیل: ۲-11 (تر. - بارس ثیل] (امر.) 
سال پلنگ» یکی ار سال‌های دوازده گٌانة 
بر کان: 

پارسنگ: 02۲-8 [- باره‌سنگک] (امر.) 
سنگی که در یک کفهة ترازو گذارند تا با 
کفه دیگر برابر گردد؛ پاسنگث» پاهنگ. 
پارسه: (6-)02152 [- بر سه ] (امر.) گدایی؛
```


## [2026-09-07T20:45:59.331Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg382.png"
}
```


### [2026-09-07T20:45:59.761Z] TOOL RESULT

```

```


## [2026-09-07T20:45:59.759Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:46:23.393Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بلوچ\" FSF_pages.txt | head -10; echo \"=== headword pahlav in FSF\"; grep -n \"پهلو‪\\|پهلو:\\|پهلو ‪\" FSF_pages.txt | head -10; echo \"=== count pages\"; grep -c \"\" FSF_pages.txt; grep -n \"\\[pdf page\" FSF_pages.txt | head -3"
}
```


## [2026-09-07T20:46:23.418Z] TOOL CALL #53: ToolSearch

```json
{
 "query": "select:WebSearch,WebFetch",
 "max_results": 3
}
```


### [2026-09-07T20:46:23.441Z] TOOL RESULT

```


```


### [2026-09-07T20:46:23.508Z] TOOL RESULT

```
10715:             ‫زردان کوچ و بلوچ‬
18302:‫(دربار؛ بلوچ کووچ کوارنامه و زباناین‬                                                    ‫ک‪-‬وکوی‬
18343:                                ‫فرهنگ‌ها‪.‬‬                    ‫هم از پهلو پارس و کوچ و بلوچ‬
=== headword pahlav in FSF
=== count pages
23569
```


## [2026-09-07T20:46:31.128Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18325,18360p' FSF_pages.txt; echo \"=== formfeeds?\"; python3 -c \"\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nprint('pages',t.count('\\f'))\nimport re\n# find which page contains line 18343\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:18342])\nprint('page index', t[:idx].count('\\f'))\n\""
}
```


### [2026-09-07T20:46:32.714Z] TOOL RESULT

```
                 ‫شده تیر بالا کمان‌وار کوژ‬                                  ‫(اسدی ‪:)۶۱۱-۰۲‬‬
‫کمان دو ابرو شده سیم توز‬                                     ‫تو در پای پیلان بدی خاشه روب‬
                                  ‫کوس‬               ‫کواره کشی پیشه» با رنج کووب‬
                        ‫ه‪:‬‬
                         ‫ر‪.‬بزخم‬
                              ‫ضکوب‬
                                 ‫‪-۱‬‬                                                    ‫کبوچلوچ‬
 ‫«کوس آنست که دوکس فراهم زنند و‬                    ‫دو قبیلۀ ایرانی که در فرهنگ‌ها و نوشته‌ها‬
‫دوش به دوش به قوت به هم زنند» (لغت‬                 ‫نام آذه ابا هم می‌آید‪ .‬از آنجمله در‬
 ‫فرس) «کوس انست که دو تن به قوت‬                                                       ‫شاهنامه‪:‬‬

‫دوش و پهلو بهعمد يابهسهو برهم زنند»‬                          ‫سوار‬    ‫ران‬
                                                                       ‫اآن‬
                                                                         ‫داز‬
                                                                           ‫مرد‬
                                                                             ‫اک‬‫نین‬
                                                                                 ‫گز‬
 ‫(صحاح) و هم‌چنین است در دیگر‬                      ‫دلیران جنگی ده و دو هزار‬
                                ‫فرهنگ‌ها‪.‬‬                    ‫هم از پهلو پارس و کوچ و بلوچ‬
 ‫ولی ازگواه‌های زیرین آشکار است که‬                  ‫سروچ‬         ‫ت‬
                                                                 ‫شو‬‫دگی‬
                                                                     ‫زیلان جن‬
                                                                            ‫گ‬
‫معنی «کوس» در سروده‌های سخنوران از‬                 ‫(‪۳-۲۴-۶۱‬ع‪)6‬‬
 ‫آنچه کهدر فرهنگ‌ها آمده است دامنه‌اش‬              ‫بودند و‬       ‫وج‬
                                                                  ‫لچو‬
                                                                    ‫بزکو‬
                                                                       ‫(سیاست‌نامه ‪ ۸04‬ا‬
                              ‫فراخ‌تر است‪:‬‬                          ‫نةست»‬
                                                                        ‫اوست‬
                                                                           ‫م پی‬
                                                                              ‫رایت‬
                                                                                 ‫ک ول‬
                                                                                    ‫ان‬
                                            ‫‪۳۷۰‬‬                                      ‫کوشان‬

=== formfeeds?
pages 484
page index 372
```


## [2026-09-07T20:46:39.149Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (118,119,120):\n    print('==== page-index',i)\n    print(t[i][:2000])\nEOF"
}
```


### [2026-09-07T20:46:40.614Z] TOOL RESULT

```
==== page-index 118
 ‫گت‬
  ‫رینو‬
     ‫بو‬


                                     ‫بویژه‬                       ‫بومهین (به فتح میم) ب=ومهن‬

                              ‫‪e‬‬     ‫‏‪a‬‬                                       ‫زمین‌لرزه‪:‬‬
                ‫مرا مهربانیست بر مرد جنگ‬                    ‫یکی بومهین خیزد از ناگهان‬
 ‫هه داز ی اک‬                                 ‫بروبومشان پاک گردد نهان‬
 ‫(‪)۴-۳۱۲-۶۸‬‬                                   ‫(‪)۱-۰۲۲-۰۷۲۱‬‬

                ‫بوی و رنک = رنگ و بوی‬                                 ‫(اسدی ‪:)۶۳۳-۲۱‬‬
‫‪-۱‬رنگ گل و بوی آن» مطلق گل و بوی‬                           ‫برآمد یکی بومهن نیمشب‬
                                             ‫تو گفتی زمین دارد از لرزه تب‬
                                  ‫خوش‪:‬‬
              ‫یکی جام پر گمریفته به جنگ‬                                                ‫بوی‬

‫بهسربرزده دستهُ بوی و رنگ‬                                                          ‫عطر‪:‬‬
 ‫(‪)۲-۶۰۲-۹۲۱۳‬‬                                         ‫همی می‌چکد گویی از روی تو‬
       ‫غریونده نای و خروشنده چنگ‬             ‫عبیرست گویی مگر بوی تو‬
‫به دست اندرون دستۀ بوی و رنگ‬                  ‫(‪)۱-۷۶۱-۲۸۴‬‬

‫‏)‪(YFA-YF-F‬‬                                        ‫ز بس بوی و بس رنگ و آب روان‬
         ‫یکی دسته دادی کتایون بدوی‬            ‫همی نوشد از باد گفتی روان‬
‫و زو بستدی دستۀ رنگ و بوی‬                     ‫(‪)۳-۲۹۱-۲۵۹۲‬‬
‫(‪)۶-۱۲۰-۰۱۳۲‬‬                                                            ‫(اسدی ‪:)۸۷-۷۱‬‬
                          ‫(حافظ ‪:)۶۴۴-۸‬‬              ‫ازو آن سزید از تواینبدکهبود‬
    ‫قبای حسن فروشی تو را برازد و بس‬          ‫که ازمشک بوی آید از کاه دود‬
‫که همچو گل همه آیین رنگ و بوداری‬              ‫بوی (باپیش اول دوم شخص مفرد افزعل‬
                            ‫(حافظ ‪:)۰۳۴‬‬                          ‫مضارع از بودن)‬
  ‫ذخیره‌ای بنه از رنگ و بوی فصل بهار‬                                      ‫بمعهنی باشی‪:‬‬
‫که می‌رسند ز پی رهزنان بهمن و دی‬                            ‫بهدو هفته بايد کهایدر بوی
==== page-index 119
                                               ‫‪1۹‬‬                                         ‫بویه‬


                    ‫منوچهر بهاو می‌گوید‪:‬‬                   ‫کگهوری ندیدم به خوبی چنوی‬
         ‫خاست‬     ‫تو را بویۂ دخت مهراب‬               ‫بدان سرفرازی و آن رنگ و بوی‬
                                                     ‫(‪)۴-۲۱۳-۶۶۱‬‬
 ‫(‪)۱-۴۲۲-۹۱۳۱‬‬
                                                           ‫همان ناممن باز گردد به ننگ‬
‫(یعنی‪ :‬تو آرزوی دیدار رودابه را داری» و‬             ‫نماند ز مندر جهان بوی و رنگ‬
‫دلت در بند و اندیشۀ جان و روان سام که‬                ‫(‪)۶-۷۶۲-۳۲۸‬‬
                   ‫در انتظار تست نیست)‪.‬‬             ‫رستم پس از آنکه در نبرداول بااسفندیار‬
                                                    ‫شکست خورده و زخمی شده است» به‬
    ‫و بی‌معنی است‪:‬‬      ‫آورده‌اند کهنادرست‬                                  ‫زواره گوید‪:‬‬
                                                           ‫بدو گفت رو پیش دستان بگوی‬
 ‫دلت خواهش سام نيرم کحجاست»‬                          ‫کزین دودة سام شد رنگ و بوی‬
                                                     ‫‪۸۲۹۸۵۱۱۳‬‬

 ‫چسنین آرزو را نشاید نسهفت‬                                         ‫‪-۳‬آرایش روی و موی بزک‪:‬‬
 ‫(‪)۴-۲۱۳۰-۹۷۱‬‬
                         ‫(اسدی ‪:)۲۱۲-۸۴‬‬
                                                          ‫پس پرده اندر یکی ماهروی‬
                                                    ‫چو خورشید تابان پر از رنگ و بوی‬
      ‫دلاور نپذرفت ازو هرچه گفت‬
                                                    ‫(‪۲-۲۷۱-۵‬ع‪)6‬‬
‫که بد در دلش بويه روی جفت‬
                                                                           ‫(اسدی ‪:)۲۰۱-۰۳‬‬
                          ‫(ویس ‪:)۵۷۲-۷۲‬‬

                                                           ‫کنون در پس پرده باببوی و رنگ‬
       ‫خروشان و نوان بابویه جفت‬
 ‫ز بی‌صبری و دلتنگی همی گفت‪...‬‬
                                                     ‫نشستی تو بناز و شویت به جنگ‬
                          ‫(
==== page-index 120
        ‫بسی باره و دژ که کردیم پست‬                ‫ای بسیار داشته باشد» (برهان)‪:‬‬
                                                                              ‫بمته و‬
                                                                                   ‫قی‬
‫نیاورد کس دست من زير دست‪...‬‬                                ‫جهاندار بنشست بر تخت عاج‬
         ‫اگر سال گشتی فزون اهزار‬                 ‫هاگیر تاج‬
                                                         ‫آن‬‫بیاویختند ب‬
‫سرانجام کار‪.‬‬         ‫ادهد‬
                        ‫و بو‬
                           ‫خین‬
                             ‫هم‬                  ‫(‪۸‬هرمزد ‪)۶۵۱‬‬

                                         ‫بهایی‬            ‫بگفت و فرود آمدازخنگ عاج‬

‫فروشی‪ ,‬فروختنی» برای فروش» قابل‬                  ‫تاج‬     ‫ینر‬
                                                           ‫گآ‬‫ارفت‬
                                                                ‫هرگ‬
                                                                  ‫بسرب‬
                                                                     ‫ز‬
                                      ‫فروش‪:‬‬      ‫(‪۹‬پرویز‪(FA ‎‬‬

    ‫بیژن در توران زمین در چاه زندانیست‪.‬‬                                                     ‫بهانه‬
 ‫کیخسرو رستم را برای رهایی او بسیج‬               ‫‪-۱‬دستاویز سبب و علت» عذر یا دلیل‬
‫می‌کند و می‌پرسد از گنج و لشکر و‬                 ‫ناپسندیده و بی‌جاء «دفع دادن به حیلت و‬

 ‫پهلوان هرچه و هرکهرا می‌خواهی بگو‪.‬‬                                     ‫چاپلوسی» (صحاح)‪:‬‬
                           ‫رستم پاسخ می‌دهد‪:‬‬         ‫و لیکن چو پیمان چنین بد نخست‬
        ‫کلید چنین بند باشد فریب‬                   ‫بهانه نشاید به بیداد جست‬
 ‫نباید برین کار كردن نهيب‬                        ‫‏)‪(A‘T-YT1-¥‬‬

              ‫تیغ و سنان‬     ‫ننهگام گرزست ‏‬
                                          ‫ه‬                              ‫(ناصر ‪:)۹۹۳-۳۱‬‬
 ‫بدینکار بايد کشیدن عنان‬                                        ‫ب
```


## [2026-09-07T20:46:51.252Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'پهلو' in p and 110<=i<=150:\n        print('=== page-index',i, 'count', p.count('پهلو'))\nfor i in (117,118,119,120,121):\n    pass\n# print header lines of pages 112..126 to locate printed numbers\nimport re\nfor i in range(112,128):\n    head=pages[i].strip().split('\\n')[0][:80]\n    print(i, repr(head))\nEOF"
}
```


### [2026-09-07T20:46:52.521Z] TOOL RESULT

```
=== page-index 115 count 1
=== page-index 117 count 1
=== page-index 120 count 1
=== page-index 128 count 2
=== page-index 132 count 3
=== page-index 133 count 1
=== page-index 135 count 2
=== page-index 137 count 1
=== page-index 139 count 3
=== page-index 141 count 5
=== page-index 142 count 1
=== page-index 145 count 1
=== page-index 147 count 1
=== page-index 148 count 2
=== page-index 150 count 1
112 '\u202bبناکام\u202c'
113 '\u202b\u202a1۰\u202c\u202c'
114 '\u202b(منوچهری \u202a:)۹۲\u202c\u202c        \u202bفرس و صحاحالفرس نیامده است\u202a .\u202cدر\u202c'
115 '\u202bبنیاد\u202c'
116 '\u202bبوس\u202c                                        \u202b\u202a۱۱۳\u202c\u202c'
117 '\u202bبوش\u202c'
118 '\u202bگت\u202c'
119 '\u202b\u202a1۹\u202c\u202c                                         \u202bبویه\u202c'
120 '\u202bبسی باره و دژ که کردیم پست\u202c                \u202bای بسیار داشته باشد» (برهان)\u202a:\u202c\u202c'
121 '\u202bبه بیجاره\u202c'
122 '\u202bپرستش بھی بر کنم زین جهان\u202c                            \u202bشبی چون شبه روی شسته به '
123 '\u202b\u202a۱۳۰\u202c\u202c                                           \u202bپیجاده\u202c'
124 '\u202bبیران\u202c                                           \u202b\u202a۳\u202c\u202c'
125 '\u202b\u202aY۲\u202c\u202c                                           \u202bپیراه\u202c'
126 '\u202bبیغاره\u202c'
127 '\u202b\u202a۱۳۴\u202c\u202c                                               \u202bبیغوله\u202c'
```


## [2026-09-07T20:47:02.637Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (139,141,148):\n    print('==== page-index',i)\n    print(t[i][:1400])\nEOF"
}
```


### [2026-09-07T20:47:03.924Z] TOOL RESULT

```
==== page-index 139
                                                ‫‪۱۳۹‬‬                                        ‫‪7‬پتباره‬



           ‫شتابنده جمله‪ .‬کهیک دم زدن‬                           ‫اگر خفته‌ای زود برجهبه پای‬
‫نپاید کسی را برادر نه یار‬                              ‫وگر خود بپایی زمانی مپای‬
              ‫‪-۳‬پایدار و جاویدان بودن‪:‬‬                                         ‫(ویس ‪:)۵۷۴-۶۵‬‬
                          ‫(ناصر ‪:)۲۲۴-4‬‬                        ‫چو او شد من به مرو اندر بپایم‬
    ‫آنجا [ آنجهان] کهشوی همی بپایدت‬                   ‫بسهانه سازم از درد دو بایم‬
 ‫ویسنجای همیشه می نپایی‬                               ‫(ترجمة تفسیر طبری ‪ :)۴۸۱‬ساعتی بپای‬
                        ‫(ویس ‪:)۵۵۴-۹۶‬‬                                     ‫تابا تو سخنی گویم‪.‬‬
            ‫جهان هرگز به حالی بر نپاید‬                 ‫‪-۲‬مواظب و مراقب بودن‪ ,‬در نظر داشتن»‬
‫پس هر روز روز دیگر آید‬                                ‫نگهبانی کردن‪ .‬در بندو بهفکر کسی یا‬
‫(سیاست‌نامه ‪ :)۸۱‬کهملک بکافر بپاید و با‬                                           ‫چیزی بودن‪:‬‬
                           ‫یمد‪.‬‬
                              ‫اظل‬
                                ‫سنتمپو‬                ‫افراسیاب به تحریک و فریب گرسیوز به‬
                 ‫پتباره (بروزن همسایه) پ=تیار‬         ‫کینه‌جویی سیاوش می‌آید‪ .‬سیاوش نیز که‬
‫اصل این واژه اوستایی است‪ .‬پائیتی آر‬                   ‫گرفتار نیرن
==== page-index 141
                     ‫بهواژة درشت نگاه کنید‪.‬‬                    ‫ست‬
                                                                ‫رد و‬
                                                                   ‫کی ب‬
                                                                      ‫ندیو‬
                                                                         ‫مگاه‬
                                                                            ‫دژ آ‬
                             ‫(ویس ‪:)۳۷۴-۰۲‬‬           ‫ست‬
                                                      ‫رز تو‬
                                                          ‫ترش‬
                                                            ‫رهل‬
                                                              ‫بالا چ‬
                                                                   ‫بهب‬
        ‫به چونین خوش زمان نوغز هنگام‬                             ‫گرشاسب بهپاسخ گفت‪:‬‬
‫که‌گیتی تازه بود و روز پدرام‬                             ‫ازین زشت پتیاره چندین چه باک‬
                                         ‫پدرود‬   ‫همین دم ز کوهش کشم در مغاک‬
‫پهلوی‪ 2 1۵0۳0 :‬مرکب از ھم = با ب‪10:4 +‬‬           ‫‪-۴‬به معنی گزیر‪ .‬چاره کههدریچیک از‬
‫به معنی آرزومندی تندرستی و خوشی و‬                                     ‫فرهنگ‌ها نیامده است‪:‬‬
‫و‬    ‫«خسرو‬    ‫کامیابی‪ .‬در پایان نامه پهلوی‬               ‫بدو گفت رستم که دل شاد دار‬
==== page-index 148
 ‫پرهیز‬                                          ‫‪۱۳۵‬‬


            ‫بدو گفت یاری ده‌اند و خورش‬                 ‫دیگر در بیت دوم بجای کردگار‪« .‬پهلوان»‬

 ‫که مرد از شهورش‌ها کندپرورش‬                          ‫آمدهو نیز مصراع دوم بیت دوم و مصراع‬
 ‫(‪)۴-۷۴۸۱‬‬                                             ‫اول بیت سوم افتاده و این دو بیت بهاین‬

                      ‫پروز (بهفتح اول و سوم)‬                                  ‫شکل درامده است‪:‬‬

                  ‫نژاد گوهر اصل و نسب‪:‬‬                            ‫نخست آفرین کرد یڑ پهلوان‬

             ‫بدو گفت من خویش گرسیوزم‬                  ‫که بیدار دل‌باش و روشن روان‬
 ‫به شاه آفریدون کشد پروزم‬                             ‫تکته اول آنکه واریانت تسه لندن‬
 ‫(‪)۲-۸-۵۳‬‬                                              ‫چون‪-۱ :‬در‬        ‫ررسد‬
                                                                           ‫‌ نظ‬
                                                                              ‫یبه‬‫مست‬
                                                                                   ‫در‬

               ‫پس پردة شهریار جهان‬                    ‫شاهنامه معمولاً نامه‌هاباآفرین برکردگار‬
 ‫سه ماهست با زیور اندر نهان‬                           ‫آغاز می‌شود؛ ‪-۲‬کلمه نسخت در بيت‬
              ‫سه اندر شبستان گرسیوزند‬                  ‫دوم که در همه نسخه‌ها هست؛ مستلزم‬

  ‫که از مام و از باب باپروزند‬
```


## [2026-09-07T20:47:26.242Z] TOOL CALL #58: WebSearch

```json
{
 "query": "\"پشملبا\" OR \"پش ملبا\" بستنی هلو فرانسوی"
}
```


## [2026-09-07T20:47:28.702Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"melba\\|Etymology\" 10a472dfd05a9fb2.txt | head -20; echo ===; timeout 120 python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Peach_Melba\" --note \"page 382: pêche Melba dessert, Escoffier/Nellie Melba\" 2>/dev/null || (timeout 120 python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Peach_Melba\" --note \"page 382: peche Melba dessert\")"
}
```


### [2026-09-07T20:47:34.439Z] TOOL RESULT

```
Web search results for query: ""پشملبا" OR "پش ملبا" بستنی هلو فرانسوی"

Links: [{"title":"طرز تهیه پش ملبا (پیچ ملبا)؛ دسر کلاسیک هلو و بستنی - مجله اکالا","url":"https://blog.okala.com/peche-melba-dessert/"},{"title":"پش‌ملبا 🍑 Pêche Melba(Peach Melba) - 𝑆𝑎𝑖𝑛𝑎🌈🏡ساینا","url":"https://cookpad.com/ir/%D8%AF%D8%B3%D8%AA%D9%88%D8%B1%20%D8%BA%D8%B0%D8%A7/24923176"},{"title":"طرز تهیه پشملبا (پیچ ملبا) ؛ دسر فرانسوی نوستالژیک - کتاب کاله","url":"https://kalleh.com/book/recipe/%D8%B7%D8%B1%D8%B2-%D8%AA%D9%87%DB%8C%D9%87-%D9%BE%D8%B4%D9%85%D9%84%D8%A8%D8%A7-%D9%BE%DB%8C%DA%86-%D9%85%D9%84%D8%A8%D8%A7-%D8%9B-%D8%AF%D8%B3%D8%B1-%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%88%DB%8C/"},{"title":"طرز تهیه پشملبا - کالُری","url":"https://kalory.ir/409-%D9%BE%D8%B4%D9%85%D9%84%D8%A8%D8%A7"},{"title":"طرز تهیه پشملبا (پیچ ملبا) – مستر آشپز","url":"https://www.mr-ashpaz.ir/2020/11/21/%D8%B7%D8%B1%D8%B2-%D8%AA%D9%87%DB%8C%D9%87-%D9%BE%D8%B4%D9%85%D9%84%D8%A8%D8%A7-%D9%BE%DB%8C%DA%86-%D9%85%D9%84%D8%A8%D8%A7/"},{"title":"طرز تهیه پشملبا (پیچ ملبا) ؛ دسر فرانسوی نوستالژیک - انجمن آقای شرفی","url":"https://forum-mrsharafi.1com.ir/post/%D8%B7%D8%B1%D8%B2-%D8%AA%D9%87%DB%8C%D9%87-%D9%BE%D8%B4%D9%85%D9%84%D8%A8%D8%A7-%D9%BE%DB%8C%DA%86-%D9%85%D9%84%D8%A8%D8%A7-%D8%AF%D8%B3%D8%B1-1214"}]

Based on the search results, here's what I found about پشملبا (Pêche Melba):

## تعریف دسر

پش‌ملبا یا پیچ‌ملبا دسری از هلو و سس تمشک با بستنی وانیلی‌ست. این دسر یکی از اصیل‌ترین، شیک‌ترین و خوش‌طعم‌ترین دسرهای فرانسوی و کلاسیک جهان است.

## تاریخچه

این دسر در سال ۱۸۹۲ یا ۱۸۹۳ توسط سرآشپز فرانسوی آگوست اسکوفیر در هتل ساووی لندن، به افتخار نلی ملبا، خواننده سوپرانو استرالیایی، اختراع شد. در نسخه ابتدایی سرآشپز از قوهایی یخی روی دسر استفاده کرده بود، پس از آن اسکوفر در 1900 تصمیم گرفت تا سس قرمز تمشک را به آن افزود.

## نحوه سرو

برای سرو، دو عدد از نیمه‌های هلو را در هر بشقاب بگذارید و روی آن آن را با یک قاشق غذاخوری بستنی وانیلی پر کنید.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-07T20:47:35.590Z] TOOL RESULT

```
Exit code 1
1:URL: https://en.wiktionary.org/wiki/p%C3%AAche_Melba
(eval):1: == not found
```


## [2026-09-07T20:47:45.035Z] TOOL CALL #60: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Peach_Melba\" --note \"page 382 node 5/6: peche Melba created by Escoffier 1892-93 for Nellie Melba\"; timeout 120 python3 tools/fetch_source.py \"https://blog.okala.com/peche-melba-dessert/\" --note \"page 382 node 6: Persian پش ملبا / پشملبا as the Persian name of the French dessert\""
}
```


### [2026-09-07T20:47:48.883Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/81bd9f11624b835a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2acc86ba92d7e5c4.txt
```


## [2026-09-07T20:47:52.340Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -m4 \"Escoffier\\|Melba was\\|1892\\|1893\" 81bd9f11624b835a.txt | head; echo \"=== okala\"; grep -n -m5 \"پش\" 2acc86ba92d7e5c4.txt | head -5"
}
```


### [2026-09-07T20:47:52.394Z] TOOL RESULT

```
180: Created by Auguste Escoffier 
184: Peach Melba ( French : pêche Melba , pronounced [ pɛʃ mɛlba ] ) is a dessert of peaches and raspberry sauce with vanilla ice cream. It was invented in 1892 or 1893 by the French chef Auguste Escoffier at the Savoy Hotel , London, to honour the Australian soprano Nellie Melba . [ 1 ] [ 2 ] 
189: In 1892, operatic soprano Nellie Melba was performing in Wagner's opera Lohengrin at Covent Garden . The Duke of Orléans gave a dinner party at the Savoy to celebrate her triumph. For the occasion, Escoffier presented Nellie with a dessert of fresh peaches served over vanilla ice cream in a silver dish perched atop an ice sculpture of a swan, which is featured in the opera. He originally called the dish Pêche au cygne , or "peach with a swan." [ 2 ] 
191: A few years later Escoffier created a new version of the dessert: when Escoffier and César Ritz opened the Ritz Carlton in London (after both were sacked from the Savoy for alleged larceny, embezzlement, and fraud), [ 3 ] Escoffier changed the recipe slightly by adding a topping of sweetened raspberry purée and renamed the dish Pêche Melba . [ 2 ] 
=== okala
4:TITLE: طرز تهیه پش ملبا (پیچ ملبا)؛ دسر کلاسیک هلو و بستنی - مجله اکالا
6:طرز تهیه پش ملبا (پیچ ملبا)؛ دسر کلاسیک هلو و بستنی - مجله اکالا جستجو... 
39: خانه آشپزی طرز تهیه پش ملبا (پیچ ملبا)؛ دسر کلاسیک هلو و بستنی برچسب ها
41: طرز تهیه پش ملبا (پیچ ملبا)؛ دسر کلاسیک هلو و بستنی 
53: دسر پش ملبا یا پیج ملیا یک دسر کلاسیک با هلو و بستنی است. این دسر که به انگلیسی به عنوان pêche melba شناخته می‌شود یکی از اصیل‌ترین، شیک‌ترین و خوش‌طعم‌ترین دسرهای فرانسوی و کلاسیک جهان است. در این مطلب از مجله اکالا ، با طرز تهیه پش ملبا خانگی به همراه نکات کامل نگهداری و فوت‌وفن‌های طرز تهیه آن آشنا می‌شویم.
```


## [2026-09-07T20:48:09.779Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WEB_vol1 Parthian\"; grep -n -i \"parthian\" WEB_vol1.txt | head -5; echo \"== WEB_vol1 range: last headword-ish\"; tail -c 400 WEB_vol1.txt; echo; echo \"== KLN peach\"; grep -n -i \"peach, n\\.\\|^peach\\b\\|peach ‘\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T20:48:09.861Z] TOOL RESULT

```
== WEB_vol1 Parthian
== WEB_vol1 range: last headword-ish
andum. [Obs.]
3. a written statement of facts submitted to a person or persons in authority, as to Congress; a statement of facts accompanied with a petition. à
4. memory; remembrance; that which is or may be remembered. [Obs.]
5. in diplomacy, an informal state paper, used in negotiations, and containing such documents as circulars sent to foreign agents, answers to the communications of amba
== KLN peach
27769:peach,  intr.  v.,  to  inform  against  (slang)  —  Aphet- ic  for  appeach  (q.v.)
```


## [2026-09-07T20:48:11.197Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN parchment\"; grep -n -i \"parchment\" KLN_1966.txt | head -5; echo \"== SKT peach/parchment\"; grep -n -i \"PEACH\\|PARCHMENT\" SKT.txt | head -8; echo \"== BRT Parsa\"; grep -n \"P[aá]rsa\\|Pārsa\" BRT.txt | head -8"
}
```


### [2026-09-07T20:48:11.291Z] TOOL RESULT

```
== KLN parchment
4911:name  of  the  city  (lit.  ‘frontier  town’;  cp.  Heb. glbhul,  ‘frontier,  boundary’,  Arab .jabal,  ‘moun¬ tain’,  and  see  javali).  Cp.  Jubayl,  the  actual Arabic  name  of  ancient  Gebhal.  ( Jubayl  prop, is  a  dimin.  formed  from  the  original  name  of  the city.)  For  the  sense  development  of  Bible  fr. Byblos  cp.  parchment.
15152:Derivatives:  foreign-er,  n.,  foreign-ism,  n., foreign-ly,  adv.,  foreign-ness,  n. forel,  forrel,  n.,  a  kind  of  parchment  used  for book  covers.  —  ME.  forel,  fr.  OF.  forrel  (F. fourreau),  ‘sheath’,  dimin.  of  OF.  fuerre  (F. feurre),  ‘fodder,  straw’.  See  forage,  n. foremost,  adj.  —  OE.  formest,  frymest,  a  super¬ lative  of  forma,  ‘first’,  which  stands  for  for-ma and  itself  is  a  superl.  of  fore;  see  fore,  adv.  OE. forma  is  rel.  to  OE .fram,  ‘forward;  from’,  ON. framr,  ‘excellent’,  OS.  formo,  ON.  from-  (in compounds),  Goth,  fruma,  ‘first’,  OS.,  OHG. fruma,  ‘advantage,  profit’,  MHG.  vrum,  ‘zea¬ lous,  able’,  G.fromm,  ‘pious,  devout’,  and  cogn. with  Gk.  7rp6jj.o5,  ‘foremost  man’,  L.  primus, Lith.  pirmas,  ‘first’.  For  the  etymology  of  the double  superb  suff.  appearing  in  OE.  formest see  after-most.  The  change  of  e  (in  OE.  formest) to  o  (in  E.  foremost)  is  due  to  an  erroneous  as¬ sociation  with  most.  Cp.  -most  and  words  there referred  to.  Cp.  also  first,  former,  frame,  from, frow,  furnish.  Cp.  also  prandial,  prime,  prow, ‘the  bow  of  a  ship'.
23419:membrane,  n.  — -  L.  membrana,  ‘fine  skin,  mem¬ brane,  parchment’,  fr.  membrum ;  see  member. The  orig.  meaning  of  L.  membrana  was  ‘that which  covers  the  members  (or  a  member)  of  the body’.
23791:mezuzah,  mezuza,  n.,  a  small  roll  of  parchment containing  Deut.  6:4-9  (the  Shema),  and  Deut. 11:13-21,  affixed  to  the  doorpost  of  every  room, on  the  right  side  of  the  entrance  (Jewish  religion).
27008:palimpsest,  n.,  a  parchment  from  which  the  ear¬ lier  writing  has  been  removed  to  make  room  for the  next. — L.palimpsestus.ft.  Gk.  7raXifzi(,Y)CT'ros, ‘scraped  again’ (whence  the  noun  7iaXt|/.^''loTov, ‘a  palimpsest’),  compounded  of  toxXiv,  ‘again’, and  verbal  adj.  of  ■jjvjv,  ‘to  touch  on  the  surface, to  rub’.  For  the  first  element  see  prec.  word.  The second  element  is  rel.  to  Gk.  (Jjapito;  (for pto;),  ‘sand’,  Dor.  4I“?09>  ‘small
== SKT peach/parchment
13265:Parchment.  (F.-L.-Gfc.)  M  E./v^ chimin.  —  F.  parchemin.  —  L.  pergamina, p<r;^mtna^  parchment ;  fern,  of  L.  Perpi- men «j,  belonging  to  I'crgo m os  ( wh ere parchment  was  firit  invented).  ~  Gk. inpyn^i}y4l,  parchment,  from  nip-ya^ot^  Hip- TQ/Jor,  Pergamus,  in  Mysia  of  A<:ia  Minor.
13332:poach  (I),  a  fruit.  (F.  -  L.  -  Pert.'; M.  E  pickt.  -  O.  F.  pischi,  a  peach.  -  L. ptrsicHm,  a  peach ;  so  called  from  growing oD  the  Persua  arbor^  Persian  tree.  —  Pers. Pdrs,  Persia.
13524:Peach  (i).  a  fruit ;  see  Pari
13525:Peach  (2);  short  for  M.E. im^Kach ;  sec  Pedal.
13599:despatch,  dispatch.  (F.-Ll  1^ orig.  sense  was  *to  remove  a  hbdrans. Better  speUiiig,  despatch ^Q.  F.  dupKhA (F.  dJp^cher\  to  hasten,  despatch. -0.^ des'  (L.  dis-\  apart,  away;  -pe. hinder.  This  O.  F.  -pescher despesckir  Coldest  form  despci.k impescher,  answering  to  l^w  L. care*  and  impediraref  of  whicti occurs  with  the  sense  *  to  put  liini the  way;*  both  from  L.  peJict^  • clog,  which  is  from  L„ped;  stem  offK foot.     See  impeach  (below).
13601:impeach,  to  charge  with  a —  L.)    The  original  aeoac  was  'lo as,    '  to   impeach    and    stop   their ,  Holland,  Ir.  of  Pliny,  b.  x\.  c,  3-0- tmpescker,  *to  hinder,  stop,  bar,  in Cot.     Older  .sfielling  emptischtr^ $  is  adventitious,  Littr^  andSchdcr it  with  ProT.  emptdiffir,  aod  defff* forms  from  Low  L.  impedieart^  to L.  im-  (for  in),  on,  upon ;  ptditAt  % from  pedi',  crude  form  of  /«,  a At   the  sojne  time,  the  Span Ital.  impofa'are.  to  delay,  ue  1 L.    frequent,    form    of    L.    1! impaetus),    to    biitd.    fasten; These  two  sets  of  wonii   may conTused.     bee  do*^!  ^r).
13608:sh  (2),  to  inform  against.  (F.  — L.) or  M.  E.  aptchin^  to  impeach,  a of  im^Jun,  to  impeach^  by  the Bpa  of  prefix  a-  (L.  ttJ)  for  im*  ^L. ft  impaaoh  (.above). ^ftL  iSpan.-Ital.-L.  om^  G.) Hb/fu/,  '  the  ba&c  of  a  pillar,' W  Not  a  Span,  word,  but  wholly cd  from  Ixii.  fiieJejtixJie,  *a  footislall ^  [threshold]  of  a  door;'  Floho. MDompomidcd  from  L./«</irm,  ace. y&ot;  and  G.  stail,  a  stall;  see
21043:ft  roll.  ■  book.  (F.-L.)    F. uolumtn,  a  toll,  scroll:  hence, parchment  roll.  —  L.  U9lu-,  as pp,  of  Molutrt^  to  roll
== BRT Parsa
20302:•  p.  mäda-  Adj.,  bezeichnet  ein  Volk, 'mediscb;  Meder*;  naiy  ähJ'  martiya^ naiy  pars<^  naiy  "d^  Bh.  i.  13;  —  karam psnam  uta  'dam  Bh._j,6,  2.14;  6;  — käram  tyam  °dam  Bh.  2. 6 ;  5 ;  —  i  fravartis namd'  *dc^  Bh.  4.  a;  2.  $,  14,  3.  14;  — avadä  Aamaranam  aiunaus  Aadä  'daibis; Äyo*  'daiiuvä  mdhisia*  aÄa*  hauv  . .  Bh. 2, 6.  a)  Sing.  (koL)  für  Volk  und  Land: pasavs^  draugt^  vasiy  aiava*  uls  pärsaiy Uta  'daiy  uta  amyTuvH  dakyuiüva  Bh. j.io;  12,  II,  14;  —  imä  dakyavcl'  .. Parsal  . .  'da*  Bh.2.a;  1.6,  D.5.2,  6.3;
```


## [2026-09-07T20:48:25.093Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN persicum/pergamena\"; grep -n -i \"persicum\\|pergamena\\|Parthica\" KLN_1966.txt | head -6; echo; echo \"== BRT pärsa- headword\"; grep -n \"p\\.  *p[äa]rsa-\\|pärsa- \" BRT.txt | head -6; echo \"== BRT parθava OCR variants\"; grep -n -i \"parGava\\|parQava\\|par6ava\\|pardava\\|par9ava\" BRT.txt | head -6"
}
```


### [2026-09-07T20:48:25.185Z] TOOL RESULT

```
== KLN persicum/pergamena
27374:parchment,  n.  —  ME.  parchemin,  fr.  OF.  (=  F.) parchemin,  fr.  L.  Pergamena,  Pergamina,  ‘parch¬ ment’,  shortened  for  Pergamena  charta  (so  in Pliny),  fr.  Gk.  nepyapoiVT],  ‘(skin)  of  Perga- mon’,  fr.  IIspya[jt,ov,  ‘Pergamon’,  the  famous town  in  Mysia  in  Asia  Minor,  now  called Bergama.  F.  parchemin  was  influenced  in  form by  an  association  with  L.  Parthica  (pellis),  ‘skin from  the  land  of  the  Parthians’.  The  alteration of  ME.  parchemin  into  E.  parchment  is  due  to  a confusion  of  the  ending  -min  with  the  suff.  -ment (fr.  L.  -mentum)  and  was  prob.  suggested  by ML.  pergamentum,  ‘parchment’,  which  occurs in  England  already  in  the  X  cent.,  and  which  it¬ self  owes  its  form  to  a  confusion  of  the  ending -menum  ( in  L.  Pergamenum)  with  the  suff.  -men¬ tum.  Cp.  parch.
27768:Derivatives:  peaceable  (q.v.),  peaceful,  adj., peace-ful-ly,  adv.,  peace-ful-ttess,  n.,  peace-less, adj ,,peace-less-ly,  adv., peace-Iess-ness,  n. peaceable,  adj.  —  ME.  peisible,  fr.  OF.  (=  F.) paisible,  fr.  pais,  ‘peace’.  See  peace  and  -able. Derivatives :  peaceabl-y,  adv.,  peaceable-ness,  n. peach,  n.,  the  fruit  of  the  tree  Amygdalus  Persica. —  ME.  peche,  fr.  OF.  pesche  (F.  peche),  fr. Late  L.  persica,  taken  for  a  fern.  sing,  noun,  but orig.  pi.  of  L.  Persicum  ( malum  or  pomurn), ‘Persian  apple’,  resp.  ‘Persian  fruit’,  fr.  Persia, ‘Persia’;  cp.  It.pe.rca,  Rum.  pierseca,  O  Proven?. persega,  presega,  Catal.  presec,  which  all  derive fr.  VL.  persica.  Cp.  Parsee,  Persian,  perse. Derivatives:  peach-en,  adj.,  peach-er,  n  ^peach- cry,  n.,  peach-let,  n.  peach-y,  adj.,  peach-i-ness, n.
28136:pergameneous,  adj.,  resembling  parchment.  — Formed  fr.  L.  Pergamena  ( charta ),  ‘parchment’, lit.  ‘paper  of  Pergamum'.  See  parchment  and -eous.
28272:Derivative:  Persic,  n.,  the  Persian  language. Persicaria,  n.,  a  genus  of  herbs  (bot.)  —  ModL. Persicaria,  fr.  L .persicum,  ‘peach’.  See  peach,  n. persicary,  n.,  any  plant  of  the  genus  Persicaria.  — See  prec.  word.

== BRT pärsa- headword
16043:•  p,  pärsa-  Adj.,  bezeichnet  ein  Volk 'persisch;  Perser':  naiy  ahi^  martiyj'  naiy "frf*  naiy  msdi^  Bh.  /.  13;  —  'sahyä  marti' yafyä  . .  arstii  D.  £.  4;  4;  —  imam  karam 'tarn  pädiy  (sd.)  yadiy  kär<^  °faf*  /ato* akatiy  D.5.  3;  Bh.^.  i,  5,  6;  —  karam °sam  Uta  mädam  Bh, j,  6,  3, 14;  6;  —  Aadä anä  °sS  iäräD.5.2;  —  adam  däray<^vt^us . ,  'f rf*  "saltya  puVa'  D,  6".  j ;  —  adam  'ja* amiy  D.  17. 3;  —  dädarsis  nänui'  °si^ manä  ba'dakt^  Bh._3,3;  6,  9,  3.6,  la,  4.x\ iS,\  5. 1.         a)  Sing.  (koUekt.)  für  Volk;
== BRT parθava OCR variants
```


## [2026-09-07T20:48:35.693Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN Persian\"; sed -n '28270,28276p' KLN_1966.txt | head -20; grep -n -i \"Persian,  adj\\|Persia',\" KLN_1966.txt | head -5; echo \"== BRT Parther\"; grep -n \"Parther\\|Parthien\" BRT.txt | head -8"
}
```


### [2026-09-07T20:48:35.780Z] TOOL RESULT

```
== KLN Persian
Persian,  adj.  and  n.  —  ME.  Persien,  fr.  F.  persien, fr.  L.  Persia.  See  prec.  word  and  -an.
Persic,  adj.,  pertaining  to  Persia  or  its  language (obsol.)  —  L.  Persicus,  fr.  Persia.  See  Persia  and adj.  suff'.  -ic.
Derivative:  Persic,  n.,  the  Persian  language. Persicaria,  n.,  a  genus  of  herbs  (bot.)  —  ModL. Persicaria,  fr.  L .persicum,  ‘peach’.  See  peach,  n. persicary,  n.,  any  plant  of  the  genus  Persicaria.  — See  prec.  word.
persiennes,  n.  pi.,  outside  shutters  for  windows. —  F.,  prop.  pi.  fern,  of  persien,  Persian’,  used as  a  noun.  See  Persian.
persiflage,  n.,  banter,  raillery.  —  F.,  fr.  persifter, ‘to  banter’,  fr.  L.  per  (see  per-)  and  siffler,  ‘to hiss,  whistle,  whizz',  fr.  L.  sifilare,  a  collateral form  of  sibilare,  ‘to  hiss,  whistle’.  See  sibilant and  -age.  The  word  persiflage  was  introduced into  English  by  Lord  Chesterfield  (1694-1773). persimmon,  n.,  the  date  plum.  —  A  compound word  of  Algonquian  origin;  lit.  ‘dried  fruit’. Persis,  fern.  PN.  —  L.,  fr.  Gk.  IlEpoi;,  lit.  ‘a  Per¬ sian  woman’,  rel  to  nipoigc,  ‘Persian’.  See Persia.
persist,  intr.  v.  —  MF.  (=  F.)  persister,  ft.  L. persistere,  ‘to  continue  steadfastly,  remain  ,  fr. per-  and  sistere,  ‘to  cause  to  stand  still,  to place;  to  stand  still,  stand’,  from  the  reduplicat¬ ed  base  of  stare,  ‘to  stand’.  See  assist  and  cp. words  there  referred  to.
Derivatives:  persist-er,  n.,  persist-ing,  adj., persist-ing-ly,  adv.
28270:Persian,  adj.  and  n.  —  ME.  Persien,  fr.  F.  persien, fr.  L.  Persia.  See  prec.  word  and  -an.
== BRT Parther
14927:•  p.  pati'grabanä-  f."'  Name  einer  Stadt inParthien:  °na''  näm<^  vardanam parka- vaiy  Bh.  _j.  i.
24441:•  p.  vispa'^izatay-  f.  Name  einer  Stadt in  Parthien:  'tis  näma^  vardanam  paria- vaiy  avadä  hamaranam  akunavt^  Bb. 2.16.
```


## [2026-09-07T20:48:44.801Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bezeichnet  ein  Volk\" BRT.txt | head; echo ===; sed -n '16044,16050p' BRT.txt"
}
```


### [2026-09-07T20:48:44.849Z] TOOL RESULT

```
Exit code 1
9223:sichereKorr.  d«  N  A     Grammatisch  verwahr-    ,         ^arka-   Adj.,  bezeichnet  ein  Volk'»: loste  Stelle.  —  4)  Vel.  lu  'vah-,  ■  j   i  k    \.  j  7
9688:•  p.  kuäiya-  Adj.,  bezeichnet  ein  Volk,  '•heua,% 268.12,%.    -faiaiteht  N.7o,F,  26,  V.
12329:•  j.,  g.  'tura-''  Adj.,  bezeichnet  ein  Volk '/arisch,  TürtT  ( TJOranier)' :  y^  mqm  (näml. ailm)  'ra  paxdayanta  asu.atpa  naotaraia
16043:•  p,  pärsa-  Adj.,  bezeichnet  ein  Volk 'persisch;  Perser':  naiy  ahi^  martiyj'  naiy "frf*  naiy  msdi^  Bh.  /.  13;  —  'sahyä  marti' yafyä  . .  arstii  D.  £.  4;  4;  —  imam  karam 'tarn  pädiy  (sd.)  yadiy  kär<^  °faf*  /ato* akatiy  D.5.  3;  Bh.^.  i,  5,  6;  —  karam °sam  Uta  mädam  Bh, j,  6,  3, 14;  6;  —  Aadä anä  °sS  iäräD.5.2;  —  adam  däray<^vt^us . ,  'f rf*  "saltya  puVa'  D,  6".  j ;  —  adam  'ja* amiy  D.  17. 3;  —  dädarsis  nänui'  °si^ manä  ba'dakt^  Bh._3,3;  6,  9,  3.6,  la,  4.x\ iS,\  5. 1.         a)  Sing.  (koUekt.)  für  Volk;
16437:•  p.  pu"tiya- Adj.,  bezeichnet  ein  Volk'': imä  dahyävJ"  tyü  adam  agarbayam  . .  'yä iusiyä  matiyä  karkä  D.  6.  3,
19521:•  p.  maka-  Adj.,  bezeichnet  ein  Volk, Ol  Mä<ä»'>;  Sing,  in  koUekt  Sinn:  ima dahyäva'^  tyH  manä  patiyaiia"  .  .  hatagvi harJ'uvatii  'ia"  Bh.  1.6;  D,  J.  2.
19559:•  p.  maäya-  Adj.,  bezeichnet  ein  Volk'*: ima  dahySvJ'  fyä  adam  agarbäyam  , .  'yS (NPm.)  D.ff.3;  —  iyam  (sd.)  'ya  D./o(?).
20302:•  p.  mäda-  Adj.,  bezeichnet  ein  Volk, 'mediscb;  Meder*;  naiy  ähJ'  martiya^ naiy  pars<^  naiy  "d^  Bh.  i.  13;  —  karam psnam  uta  'dam  Bh._j,6,  2.14;  6;  — käram  tyam  °dam  Bh.  2. 6 ;  5 ;  —  i  fravartis namd'  *dc^  Bh.  4.  a;  2.  $,  14,  3.  14;  — avadä  Aamaranam  aiunaus  Aadä  'daibis; Äyo*  'daiiuvä  mdhisia*  aÄa*  hauv  . .  Bh. 2, 6.  a)  Sing.  (koL)  für  Volk  und  Land: pasavs^  draugt^  vasiy  aiava*  uls  pärsaiy Uta  'daiy  uta  amyTuvH  dakyuiüva  Bh. j.io;  12,  II,  14;  —  imä  dakyavcl'  .. Parsal  . .  'da*  Bh.2.a;  1.6,  D.5.2,  6.3;
20574:•  p.  mudräya-  Adj.,  bezeichnet  ein  Volk 'ägyptisch;  Ägypter';  Plur.  und  Sing. (kollekt)  als  Bezeichnung  fUr  Volk  und Land:  imä  dahyävc^  tyä  adam  *adatiiy..
25898:■  p.  saka-  Adj.,  bezeichnet  ein  Volk 'Sake,  Skythe'*':  iyam  sku'ki^  hyi^  'kJ' Bh,k;S.j; —  'kä  *Aaumavaria  (sd.)  'kä tigraxauda  (sd.)  .  .  *ka  tyaiy  *tara^drayc^ (sd.)  D.  6. 3;  5.  a.  a)  Sing,  in  kollekt. Sinn :  ima  dahyäv(^  tyä  mana  paHyaisi^ ..  -itf*  Bh.l.6;2.2.
(eval):1: == not found
```


## [2026-09-07T20:49:06.656Z] TOOL CALL #67: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Parni\" --note \"page 382 entry 1 root: Parni tribe, Dahae confederacy, conquered Parthia\"; timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%F0%90%8E%B1%F0%90%8E%A0%F0%90%8E%BC%F0%90%8E%BF\" --note \"page 382: Old Persian Pārsa entry\""
}
```


### [2026-09-07T20:49:08.963Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/caf5be54bc5f5eee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1dbdb6bf84e08f3e.txt
```


## [2026-09-07T20:49:14.267Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### Parni\"; grep -n -m6 -i \"Parni\\|Dahae\\|Arsac\" caf5be54bc5f5eee.txt | head -12; echo; echo \"### OP Parsa\"; grep -n -A6 \"Etymology\" 1dbdb6bf84e08f3e.txt | sed -n '1,30p'"
}
```


### [2026-09-07T20:49:14.342Z] TOOL RESULT

```
### Parni
1:URL: https://en.wikipedia.org/wiki/Parni
4:TITLE: Parni - Wikipedia
6:Parni - Wikipedia 
85: Parni 
171: This article is about the ethnic group. For the village in Saare County, Estonia, see Pärni . For the town in Shirak Province, Armenia, see Anushavan . For the town in Lori Province, Armenia, see Mets Parni .
175: The Parni ( / ˈ p ɑːr n aɪ / ; Ancient Greek : Πάρνοι , Parnoi ), Aparni ( / ə ˈ p ɑːr n aɪ / ; Ἄπαρνοι, Aparnoi ) or Parnians were an East Iranian people [ 1 ] [ 2 ] who lived around the Ochus [ 3 ] [ 2 ] [ 4 ] ( Ancient Greek : Ὧχος Okhos ) ( Tejen ) River, southeast of the Caspian Sea in Central Asia . It is believed that their original homeland may have been what is now southern Russia in Eastern Europe , from where they emigrated with other Scythian tribes. [ 2 ] The Parni were one of the three tribes of the Dahae confederacy. 

### OP Parsa
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.3 
68- Proper noun 
--
143: Etymology
144- [ edit ] 
145-
146- Uncertain; possibly:
147-
148- related to Sanskrit पर्शु ( Parśu ) , the name of a warrior tribe, [ 1 ] (see below)
149-
```


## [2026-09-07T20:49:16.510Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '143,200p' 1dbdb6bf84e08f3e.txt"
}
```


### [2026-09-07T20:49:16.552Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 Uncertain; possibly:

 related to Sanskrit पर्शु ( Parśu ) , the name of a warrior tribe, [ 1 ] (see below)

 or Sanskrit परशु ( paraśu , “ hatchet, axe ” ) , [ 2 ] 

 or from Proto-Iranian *párcuš ( “ rib ” ) , compare Sanskrit पर्शु ( parśu , “ rib; sickle ” ) , [ 3 ] पार्श्व ( pārśva , “ the region of the ribs, immediate neighbourhood ” ) . [ 4 ] 

 Noun
 [ edit ] 

 𐎱𐎠𐎼𐎿 ( Pārsaʰ⁠ )  m 

 a Persian 

 Proper noun
 [ edit ] 

 𐎱𐎠𐎼𐎿 ( Pārsaʰ⁠ )  m 

 Fars , Farsistan , Pars , Parsistan , Persia , Persis 

 Persepolis 

 Descendants
 [ edit ] 

 ( taking Old Persian as representative of all Old Iranian ) 

 Middle Persian: 
 Inscriptional Pahlavi script: 𐭯𐭠𐭫𐭮𐭩 ( pʾlsy ) , 𐭯𐭠𐭥𐭮𐭩 ( pʾrsy /⁠Pārs⁠/ ) Classical Persian: پَارْس ( pārs ) ( see there for further descendants )
 → Arabic: فَارِس ( fāris ) → Classical Persian: فَارْس ( fārs ) ( see there for further descendants )

 → Early Middle Chinese: 波斯 ( pa-si ) 
 → Parthian: ( /⁠Pārs⁠/ ) Manichaean script: 𐫛𐫀𐫡𐫘 ( pʾrs ) Inscriptional Parthian script: 𐭐𐭀𐭓𐭎 ( pʾrs ) 
 → Sogdian: Syriac script: ܦܐܪܣ ( pʾrs /⁠Pārs⁠/ ) 

 → Akkadian: [ 5 ] 
 Late Babylonian: 𒉺𒅈𒊓𒀀𒀀 ( pa-ar-sa-a-a /⁠Parsāya⁠/ ) , 𒉺𒅈𒋢 ( pa-ar-su /⁠Parsu⁠/ ) , 𒌓𒊑𒊓𒀀 ( par-ri-sa-a /⁠Parisā⁠/ ) , 𒌓𒊓 ( par-sa /⁠Parsa⁠/ ) , 𒌓𒊓𒀀𒀀 ( par-sa-a-a /⁠Parsāya⁠/ ) , 𒌓𒋢 ( par-su /⁠Parsu⁠/ ) , 𒌓𒍪 ( par-sú /⁠Parsu⁠/ ) 

 → Aramaic: [ 5 ] 
 Biblical Aramaic: פָּרָס ( pārās ) 

 Imperial Aramaic: 𐡐𐡓𐡎 ( prs ) , 𐡐𐡓𐡎𐡉 ( prsy ) 

 → Hebrew: פָּרָס ( parás ) 

 → Egyptian: 
 Late Egyptian: 

 ( prs ) , 

 ( prs ) , 

 ( prsꜣ ) , [ 6 ]
```


## [2026-09-07T20:49:24.129Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '200,240p' 1dbdb6bf84e08f3e.txt"
}
```


### [2026-09-07T20:49:24.174Z] TOOL RESULT

```
 ( prsꜣ ) , [ 6 ] 

 ( prwsꜣ ) [ 7 ] 

 Demotic Egyptian: ⁠ ⁠ ( prs ) 

 → Elamite: [ 5 ] 
 Achaemenid Elamite: 𒁀𒅕𒐼 ( ba-ir-šá /⁠Bairša⁠/ ) , 𒁇𒌍 ( bar-šip /⁠Baršip⁠/ ) , 𒁇𒋤 ( bar-šir₈ /⁠Baršir⁠/ ) , 𒁀𒅕𒆪 ( ba-ir-da /⁠Bairda⁠/ ) , 𒁀𒅕𒆜𒐼 ( ba-ir-iš-šá /⁠Bairiša⁠/ ) , 𒁀𒅕𒊓𒀭 ( ba-ir-sa-an /⁠Bairsan⁠/ ) , 𒁀𒅕𒐼𒀭 ( ba-ir-šá-an /⁠Bairšan⁠/ ) , 𒁀𒅕𒃻𒀾 ( ba-ir-šá-áš /⁠Bairšaš⁠/ ) , 𒁀𒅕𒐼𒆜 ( ba-ir-šá-iš /⁠Bairšaiš⁠/ ) , 𒁀𒅕𒐼𒌝 ( ba-ir-šá-um /⁠Bairšaum⁠/ ) , 𒁀𒅕𒍝 ( ba-ir-za /⁠Bairza⁠/ ) , 𒁀𒊏𒊏𒆜𒐼𒀭 ( ba-ra-iš-šá-an /⁠Baraišan⁠/ ) , 𒁇𒃻𒀭 ( bar-šá-an /⁠Baršan⁠/ ) , 𒁇𒋤𒌇𒁁 ( bar-šir₈-ráš-be /⁠Barširášbe⁠/ ) 

 → Ancient Greek: Πέρσης ( Pérsēs ) Greek: Πέρσης ( Pérsis ) 
 → Latin: Persa , Persēs Catalan: persa 
 ⇒ Danish: perser 
 → Dutch: Pers 
 Galician: persa 
 ⇒ German: Perser 
 → Hungarian: perzsa 
 Italian: persa 
 Middle French: Perse French: Perse Haitian Creole: Pès 

 ⇒ Norwegian: Norwegian Bokmål: perser Norwegian Nynorsk: persar 
 Portuguese: persa 
 Spanish: persa → Tagalog: Persa 

 ⇒ Swedish: perser 
 ⇒ Latin: Persia → Albanian: Persië 
 Asturian: Persia 
 → Belarusian: Пе́рсія ( Pjérsija ) 
 → Bulgarian: Пе́рсия ( Pérsija ) 
 Catalan: Pèrsia 
 → Czech: Persie 
 → English: Persia 
 → German: Persien 
 → Finnish: Persia 
 → Icelandic: Persía 
 Italian: Persia 
 → Macedonian: Персија ( Persija ) 
 Middle French: Perse , Persie French: Perse Haitian Creole: Pès 

 French: Persie 

 Occitan: Pèrsia
```


## [2026-09-07T20:50:28.760Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN Parthian\"; grep -n -i \"Parthian\" KLN_1966.txt | head -5; echo \"== پهلبد\"; grep -n \"پهلبد\\|فهلبذ\" BQT_v1_pages.txt BQT_v2_pages.txt MON_part1.txt MON_part2.txt | head -5; echo \"== FSD parchment/peach vol3\"; grep -n -i \"Parthica\\|pergamena\" FSD_vol3.txt | head -3"
}
```


### [2026-09-07T20:50:28.856Z] TOOL RESULT

```
== KLN Parthian
27374:parchment,  n.  —  ME.  parchemin,  fr.  OF.  (=  F.) parchemin,  fr.  L.  Pergamena,  Pergamina,  ‘parch¬ ment’,  shortened  for  Pergamena  charta  (so  in Pliny),  fr.  Gk.  nepyapoiVT],  ‘(skin)  of  Perga- mon’,  fr.  IIspya[jt,ov,  ‘Pergamon’,  the  famous town  in  Mysia  in  Asia  Minor,  now  called Bergama.  F.  parchemin  was  influenced  in  form by  an  association  with  L.  Parthica  (pellis),  ‘skin from  the  land  of  the  Parthians’.  The  alteration of  ME.  parchemin  into  E.  parchment  is  due  to  a confusion  of  the  ending  -min  with  the  suff.  -ment (fr.  L.  -mentum)  and  was  prob.  suggested  by ML.  pergamentum,  ‘parchment’,  which  occurs in  England  already  in  the  X  cent.,  and  which  it¬ self  owes  its  form  to  a  confusion  of  the  ending -menum  ( in  L.  Pergamenum)  with  the  suff.  -men¬ tum.  Cp.  parch.
27529:Derivative:  parthenogenetic-al-ly,  adv. Parthenon,  n.,  name  of  the  temple  of  the  goddess Athena  on  the  Acropolis  at  Athens.  —  L.,  fr. Gk.  ITapDevcov,  prop,  ‘temple  of  Athena,  the virgin’,  fr.  trapflibo:;,  ‘virgin’.  See  parthenic. Parthian,  adj.,  of  Parthia.  —  Formed  with  suff. -an  fr.  Parthia,  name  of  an  ancient  kingdom, northeast  of  Persia.  Parthian  shot  is  a  ‘parting shot’ ;  so  called  from  the  habit  of  Parthian  horse¬ men  to  shoot  backward  while  retiring. Derivative:  Parthian,  n.
== پهلبد
== FSD parchment/peach vol3
121137:• L pergamena, < Or. Pergamtnf, Pergamon, Per-
```


## [2026-09-07T20:50:31.946Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg382.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/382.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3; grep -l '\"refs\": null' /home/sfmqrb/git/rishe/data/extracted/batch/page-380.json >/dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-380.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        print(n['id'], json.dumps(n.get('ref_check'),ensure_ascii=False)[:200])\n\" 2>/dev/null | head -8"
}
```


### [2026-09-07T20:50:33.350Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
1 [{"ref": "BQT:202", "status": "supports", "note": "BQT_v1_pages.txt leaf 422 (printed p. 201, footnotes continued «بقیه در صفحهٔ ۲۰۲» / «بقیه از صفحهٔ ۲۰۱» on the facing leaf, so the entry spreads ove
2 [{"ref": "BQT:202", "status": "supports", "note": "BQT_v1_pages.txt leaf 422 (printed p. 201-202), s.v. «باب»: «… و بمعنی پدر هم آمده است که بعربی والد گویند ؟ وباین معنی بلغت زند وپازند (۱) بابای فار
3 [{"ref": "AHD", "status": "supports", "note": "AHD_watkins1985.txt s.v. pā-: '3. Extended form *pāt- in: a. Germanic *fōd-, food, in Old English foda, food: FOOD; b. Germanic denominative *fōdjan, to 
4 [{"ref": "AHD", "status": "supports", "note": "AHD_watkins1985.txt s.v. pā-: '1. Suffixed form *pā-trom in Germanic *fōdram in: a. Old English fōdor, fodder: FODDER; b. Old French feurre, fodder: FORA
5 [{"ref": "POK:847", "status": "not_found", "note": "POK_full.txt: the lemmas whose 'Page(s):' line reads 847 are 'ptel(e)ia — Meaning: a kind of tree' and 'pū-1, peu-, pou-, also phu- — Meaning: to bl
6 [{"ref": "AHD", "status": "supports", "note": "AHD_watkins1985.txt s.v. poti-: 'Latin potis, powerful, able (> potestas, power): PODESTA, POSSESS, POWER … Latin compound posse … : POSSIBLE, POTENT; (I
7 [{"ref": "AHD", "status": "partial", "note": "AHD_watkins1985.txt s.v. pəter-: '3. Greek patḗr, father: PATRIOT; ALLOPATRIC, EUPATRID, PATRIARCH, SYMPATRIC. [Pok. pətē(r) 829.]' — supports pater. But 
8 [{"ref": "AHD", "status": "partial", "note": "AHD_watkins1985.txt s.v. pəter-: 'Greek patḗr, father: PATRIOT …' — supports patriot. But POPE and PAPA are indexed to the separate root: 'papa. A child's
```


## [2026-09-07T20:50:49.489Z] TOOL CALL #73: WebSearch

```json
{
 "query": "پهلبد معنی لغت‌نامه دهخدا رامشگر خسرو پرویز باربد"
}
```


## [2026-09-07T20:50:49.768Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '121130,121142p' FSD_vol3.txt"
}
```


### [2026-09-07T20:50:49.825Z] TOOL RESULT

```
A few frasuiAiitjiof lTom«r.TliueydidMi.Euripiileii Ballunt, and
other aullioni an* ezlaul on broken papyrus Ivavtsi. Inii all our
eonipleUo hum of fint-rate autbur* are written on another mate-
rial, parchment JaMae Gow Companton lo School Claenee,
Hook* p lU Imaom 1888 ]
2. A formal writing on parrhment $. In eofTee-cuI-
tiire, a tough envelop of the berry I < F
• L pergamena, < Or. Pergamtnf, Pergamon, Per-
gurnum, a city of Asia Minor, whence parchment wax
nmt brought 1 - rotton parrhiueot, a material made by
troatliig cotton-nijers with dlluU>d sulfuric acid and coni-
puctlng the product by rollers Into sheets p. coffee, same
us PARCHMENT. 3 uarch*iuetit*dlii.iease*, n Bumc as
```


### [2026-09-07T20:50:59.261Z] TOOL RESULT

```
Web search results for query: "پهلبد معنی لغت‌نامه دهخدا رامشگر خسرو پرویز باربد"

Links: [{"title":"پهلبد - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%BE%D9%87%D9%84%D8%A8%D8%AF/"},{"title":"معنی باربد | لغت‌نامه دهخدا","url":"http://www.vajehyab.com/dehkhoda/%D8%A8%D8%A7%D8%B1%D8%A8%D8%AF-2"},{"title":"معنی باربد | لغت‌نامه دهخدا | واژه یاب","url":"https://vajehyab.com/dehkhoda/%D8%A8%D8%A7%D8%B1%D8%A8%D8%AF"},{"title":"باربد - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B1%D8%A8%D8%AF/"},{"title":"باربد | در فرهنگ لغات ها (دهخدا،معین و ... ) + سایر منابع اطلاعاتی | جدول یاب","url":"https://www.jadvalyab.ir/fa2fa/%D8%A8%D8%A7%D8%B1%D8%A8%D8%AF"},{"title":"باربد موسیقیدان بزرگ دوره ساسانی","url":"https://www.beytoote.com/art/artist/barbad-great2-musician.html"},{"title":"معنی باربد | لغت نامه دهخدا | پارسی ویکی","url":"https://www.parsi.wiki/fa/wiki/153336/%D8%A8%D8%A7%D8%B1%D8%A8%D8%AF"}]

بر اساس نتایج جستجو، معنی کلمه «پهلبد» در لغت‌نامه دهخدا به شرح زیر است:

پهلبد نام باربد نوازندۀ مشهور دورۀ خسروپرویز است که به خطا بصورت «پهلبد» در فارسی و «فهلبد» در عربی نگاشته شده است.

باربد نوازندۀ مشهور دورۀ خسروپرویز بود که بر اساس روایت ثعالبی روزی به سرکش رئیس و سردستۀ رامشگران مجالس خصوصی خسروپرویز خبر رسید که جوانی مروی که زبردست‌ترین نوازندگان عود است و صدائی خوش دارد بدربار آمده تا بعنوان رامشگر بحضور شاه بار یابد.

باربد جهرمی در فن بربطنوازی استاد بوده و بنای لحون و اغانی خود را در مجلس خسروپرویز بر نثر نهاده بود، و این قسم اغانی و لحون را خسروانی خوانند.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:51:14.272Z] TOOL CALL #75: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%BE%D9%87%D9%84%D8%A8%D8%AF/\" --note \"page 382 entry1 node1: Dehkhoda on پهلبد (= Barbad, erroneous spelling)\" && cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m3 \"پهلبد\" $(ls -t | head -1) | head -5"
}
```


### [2026-09-07T20:51:16.844Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/05d8a10ecf09b7c3.txt
4:TITLE: پهلبد - معنی در دیکشنری آبادیس
6:پهلبد - معنی در دیکشنری آبادیس 
10: پهلبد
```


## [2026-09-07T20:51:19.909Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"پهلبد\" 05d8a10ecf09b7c3.txt | sed -n '1,12p' | cut -c1-300"
}
```


### [2026-09-07T20:51:19.963Z] TOOL RESULT

```
4:TITLE: پهلبد - معنی در دیکشنری آبادیس
6:پهلبد - معنی در دیکشنری آبادیس 
10: پهلبد
16: اسم: پهلبد (پسر) (فارسی) (تلفظ: pahlbod) (فارسی: پَهلبد) (انگلیسی: pahlbod) 
32: پهلبد تغییر یافته ی پهربد می باشد . پهر به معنای مراقبت محافظت نگهبانی دیدبانی است که پا واژه پرهیز همریشه می باشد . زیرا واژه ی پرهیز تغییر یافته ی پهریچ می باشد . که
34: پهلبد. ( اسم خاص ) الف. نام باربد نوازندۀ مشهور دورۀ خسروپرویز است که به خطا بصورت «پهلبد» در فارسی و «فهلبد» در عربی نگاشته شده است. برای اطلاعات بیشتر، رجوع شود به «
```


## [2026-09-07T20:52:08.311Z] AGENT

Now I'll write the verification file.


## [2026-09-07T20:57:45.326Z] TOOL CALL #77: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-382.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 382,\n \"book_page\": 352,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Pârsa\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Old Persian Pārsa- adj./m. 'Persian; Persia (Persis, later Fārs)' (Kent, Old Persian, Lexicon p. 196)\",\n   \"note\": (\"The root box is genuine: Kent p. 196 has 'Pārsa- adj. ‘Persian’; also masc. as sb. ‘Persia’, a province of the \"\n     \"Persian Empire: Elam. par-šin, Akk. pa-ar-su, Gk. Πέρσαι, Περσία', and Bartholomae AiW likewise lists OP pārsa- 'persisch; Perser'. \"\n     \"Two details of Nourai's gloss are loose. (a) '4000 years ago' is far too early: the Iranian tribes reach the plateau c. 1500–1000 BCE, \"\n     \"and the people appear in Assyrian records as Parsua/Parsuaš only from 843 BCE. (b) Pārsa is the south-western highland (Persis/Fārs), \"\n     \"and, as Stronach notes in Encyclopaedia Iranica, it was Darius I who applied the name Parsa to the old region of Anšan and to his new \"\n     \"capital; the wording 'a province south of the Persian Empire' is a modern simplification. The further etymology of Pārsa- itself is \"\n     \"unsettled (Wiktionary lists Skt. Parśu- as a tribal name, paraśu- 'axe', or Proto-Iranian *párcuš 'rib'); Nourai wisely leaves it \"\n     \"unanalysed. Note also that Kent derives Parθava- (Nourai's next root) from the same stem, so entries 0 and 1 of this page are in fact \"\n     \"one root in two dialect shapes.\"),\n   \"note_fa\": (\"«پارسَه» (Pārsa) در پارسی باستان هم صفت است به معنی «پارسی» و هم نام سرزمین پارس؛ کنت در واژه‌نامهٔ پارسی باستان (ص ۱۹۶) و \"\n     \"بارتولومه در فرهنگ ایرانی باستان همین را آورده‌اند و صورت‌های عیلامی par-šin و اکدی pa-ar-su و یونانی Πέρσαι را گواه می‌گیرند. \"\n     \"پس ریشه و برچسب زبانی درست است، اما دو نکته در شرح نورایی سست است: نخست آنکه «حدود ۴۰۰۰ سال پیش» زودتر از واقع است، زیرا کوچ تیره‌های \"\n     \"ایرانی به فلات را حدود ۱۵۰۰ تا ۱۰۰۰ پیش از میلاد می‌دانند و نخستین یاد از پارس‌ها در متون آشوری به ۸۴۳ پ.م. بازمی‌گردد؛ دوم آنکه بنا بر \"\n     \"دانشنامهٔ ایرانیکا این داریوش بزرگ بود که نام «پارسَه» را بر سرزمین انشان و بر پایتخت نوی خود نهاد. ریشهٔ خودِ Pārsa هنوز روشن نیست \"\n     \"(پیوند با پَرشو سنسکریت یا ایرانی آغازین *párcuš «دنده»). ادعای نورایی در کلیّت درست است ولی جزئیات تاریخی آن باید تصحیح شود.\"),\n   \"sources\": [\n     \"https://en.wiktionary.org/wiki/%F0%90%8E%B1%F0%90%8E%A0%F0%90%8E%BC%F0%90%8E%BF\",\n     \"https://www.iranicaonline.org/articles/pasargadae\",\n     \"https://www.etymonline.com/word/Parthian\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"KNT:196\", \"status\": \"supports\",\n      \"note\": (\"KNT.txt form-feed leaf 220 (the leaf that carries printed pp. 196–197 of the Lexicon), s.v.: 'Pārsa- adj. ‘Persian’; also masc. \"\n        \"as sb. ‘Persia’, a province of the Persian Empire: Elam. par-šin, Akk. pa-ar-su, Gk. Πέρσαι, Περσία (§9.VI, §87, §126, §143.II). \"\n        \"See also Parθava-.' Exactly the root, language label and double sense (people / province) that Nourai's box gives.\")}\n   ],\n   \"consulted\": [\n     {\"src\": \"KNT\", \"where\": \"p. 196 s.v. Pārsa- (KNT.txt leaf 220)\", \"stance\": \"supports\",\n      \"note\": \"'Pārsa- adj. ‘Persian’; also masc. as sb. ‘Persia’ … Gk. Πέρσαι, Περσία. See also Parθava-.'\"},\n     {\"src\": \"BRT\", \"where\": \"AiW s.v. p. pārsa- (BRT.txt line 16043)\", \"stance\": \"supports\",\n      \"note\": \"'p. pārsa- Adj., bezeichnet ein Volk ‘persisch; Perser’', with the Bisotun and Naqš-e Rostam passages — confirms the Old Persian form and label.\"},\n     {\"src\": \"BQT\", \"where\": \"Mo'in's footnote s.v. پارس, BQT_v1_pages.txt line 23092\", \"stance\": \"supports\",\n      \"note\": \"«در پارسی باستان (کتیبه‌های هخامنشی) Pārsa: نام یکی از اقوام ایرانی مقیم جنوب ایران که نام مقر ایشان را نیز پارس نامیده‌اند … معرّب آن «فارس» است؛ یونانیان نام … را از نام این [قوم گرفته‌اند]».\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"Pârs, Fârs; Pâsârgâd\", \"verdict\": \"disputed\",\n     \"derivation\": (\"Pārs/Fārs is confirmed: OP Pārsa- > Middle Persian Pārs (inscriptional pʾrsy /Pārs/, also Parthian pʾrs, Sogdian pʾrs) > New \"\n        \"Persian پارس; Arabic, having no /p/, took it as فارس (fāris/Fārs), and that Arabicised form was re-borrowed into Persian as فارس, so \"\n        \"پارس ~ فارس are a native/Arabic-mediated doublet — exactly what Mo'in says in his Borhān-e Qāṭe' footnote («معرّب آن فارس است»). \"\n        \"Pâsârgâd is the problem. Deriving Pāsārgād from Pārsa (pārsa- + gard/kard/kad 'fort, settlement', with metathesis pārsa- > pāsār-) is \"\n        \"the classical and the traditional Persian explanation — Anaximenes of Lampsakos (4th c. BCE) was told it meant 'encampment of the \"\n        \"Persians', Quintus Curtius writes Parsagada, and Farahvashi (IRN:63) reproduces it — but modern Iranology rejects it: the Achaemenid \"\n        \"Elamite fortification tablets give Batrakata(š) for Cyrus' capital, every Greek witness has Pasargadai, and Martin Schwartz's objection \"\n        \"(quoted by Stronach in Encyclopaedia Iranica) is that a transparent 'Parsa' would not have been deformed; the reconstruction now \"\n        \"preferred is OP *Pāθragadā (so also Wiktionary), and Gershevitch reads the tribal name as 'those who wield solid clubs'. Nourai's NOTE \"\n        \"is nevertheless right: Herodotus i.125 names the Pasargadae as the most renowned of the Persian tribes. The spelling «پارسه گاد» in the \"\n        \"chart is itself a product of that folk etymology.\"),\n     \"derivation_fa\": (\"«پارس» دنبالهٔ راست پارسی باستان Pārsa است: فارسی میانه Pārs (پهلوی کتیبه‌ای pʾrsy، پارتی و سغدی pʾrs) و سپس فارسی نو «پارس»؛ \"\n        \"چون در عربی واج «پ» نیست، این نام «فارس» معرّب شد و همان صورت معرّب دوباره به فارسی بازگشت، چنان‌که معین در حاشیهٔ برهان قاطع می‌نویسد «معرّب \"\n        \"آن فارس است». اما دربارهٔ «پاسارگاد» ادعای نورایی پذیرفتنی نیست: گرفتنِ پاسارگاد از «پارسَه + گَرد/کَد» با قلبِ pārsa > pāsār همان ریشه‌شناسیِ \"\n        \"کهن و عامیانه است که آناکسیمنس و کوینتوس کورتیوس (Parsagada) و در روزگار ما فره‌وشی (ایرانویج ص ۶۳) آورده‌اند؛ ولی ایران‌شناسی امروز، با \"\n        \"تکیه بر صورت عیلامیِ Batrakata(š) در گل‌نوشته‌های تخت جمشید و ثبات صورت یونانی Pasargadai، صورت *Pāθragadā را بازسازی می‌کند و قلبِ پیشنهادی \"\n        \"را رد می‌کند (استروناخ در ایرانیکا از قول مارتین شوارتز). یادداشت نورایی که پاسارگاد نام یکی از تیره‌های پارسی هم بوده درست است (هرودوت، ۱۲۵/۱).\"),\n     \"sources\": [\n       \"https://www.iranicaonline.org/articles/pasargadae\",\n       \"https://en.wiktionary.org/wiki/Pasargadae\",\n       \"https://en.wiktionary.org/wiki/%F0%90%8E%B1%F0%90%8E%A0%F0%90%8E%BC%F0%90%8E%BF\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"BQT\", \"status\": \"supports\",\n        \"note\": (\"Borhān-e Qāṭe' with Mo'in's footnotes, s.v. پارس (BQT_v1_pages.txt line 23092): «در پارسی باستان (کتیبه‌های هخامنشی) Pārsa: نام یکی از \"\n          \"اقوام ایرانی مقیم جنوب ایران که نام مقر ایشانرا نیز پارس نامیده‌اند … معرّب آن «فارس» است؛ یونانیان نام … را از نام این قوم [گرفته‌اند]» — \"\n          \"supports Pārs/Fārs; the footnote says nothing about Pāsārgād.\")},\n       {\"ref\": \"MON5:322\", \"status\": \"not_checked\",\n        \"note\": (\"Mo'in vol. 5 (اعلام) is not on disk and is not carried by vajehyab/abadis. The lexicon volumes are (MON_part1.txt line 27939), and there \"\n          \"s.v. پارس Mo'in writes «نام قومی ایرانی ساکن جنوب ایران … (اِخ.) مسکن قوم مذکور» — i.e. the same tribe/province equation, but that is not the \"\n          \"cited page.\")},\n       {\"ref\": \"IRN:63\", \"status\": \"supports\",\n        \"note\": (\"Farahvashi, Iranvij p. 63 (rendered with tools/ref_page.py IRN:63 --image, pdf page 74; cached under sources/refs/ocr/IRN/0063.png): \"\n          \"«واژه پاسارگاد … مرکب از دو جزء است: جزء نخستین آن پاسار، همان پارسه Pārsa است که قلب شده است و جزء دوم آن «گد» … در این صورت پاسارگاد به معنی \"\n          \"روستا یا شهر پارسیان است»، and just above it «هرودوت مینویسد: پاسارگادیان یکی از قبایل پارسی بودند که از قبایل دیگر شریف‌تر … بودند» — this is \"\n          \"precisely Nourai's node and his NOTE, so the reference does support him; it is the derivation itself that modern scholarship rejects.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"Mo'in's footnote s.v. پارس (BQT_v1_pages.txt l. 23092)\", \"stance\": \"partial\",\n        \"note\": \"Supports Pārs/Fārs («معرّب آن فارس است»); silent on Pāsārgād (grep for پاسارگاد in BQT_v1/v2_pages.txt returns nothing).\"},\n       {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. پارس (MON_part1.txt l. 27939)\", \"stance\": \"supports\",\n        \"note\": \"«پارس: (اِخ.) نام قومی ایرانی ساکن جنوب ایران … (اِخ.) مسکن قوم مذکور» — tribe name transferred to the land, as in the chart.\"},\n       {\"src\": \"IRN\", \"where\": \"Iranvij p. 63\", \"stance\": \"supports\",\n        \"note\": \"«جزء نخستین آن پاسار، همان پارسه Pārsa است که قلب شده است» — Farahvashi's metathesis account, the one Nourai follows.\"},\n       {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (Aryanpur, Hend-o-Orupāyi roots)\", \"stance\": \"silent\",\n        \"note\": \"grep پارس / پاسارگاد finds only running text about پارسی باستان; the book has no headword for the ethnonym.\"},\n       {\"src\": \"Encyclopaedia Iranica\", \"where\": \"s.v. PASARGADAE, 'The Name'\", \"stance\": \"contradicts\",\n        \"note\": (\"'It is most unlikely, however, that the readily recognizable form “Parsa” would have undergone a transformation into something \"\n          \"else (Martin Schwartz, private communication) … the character of the newly discovered Elamite name [Batrakata(š)] … would seem to rule out the \"\n          \"likelihood of the proposed metathesis.'\")}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Greek\", \"words\": \"persis\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Ancient Greek Περσίς (Persís), gen. Περσίδος, 'Persia', beside Πέρσης 'a Persian' / Πέρσαι, is the Ionians' rendering of Old Persian \"\n        \"Pārsa-, taken over in the 6th c. BCE with Achaemenid contact and current in literature from Aeschylus' Πέρσαι (472 BCE) and Herodotus onward. \"\n        \"Kent lists 'Gk. Πέρσαι, Περσία' among the foreign renderings of Pārsa- itself. Greek renders the Iranian long ā of the first syllable with e \"\n        \"(Πέρσ-), whereas the neighbouring ethnonym Παρθία keeps a; the vocalism is usually put down to the shape in which the name reached Ionia \"\n        \"(through Median/Elamite intermediaries) rather than to a Greek sound law. Nourai's citation of Buck is to the PEACH article, not to the \"\n        \"ethnonym itself.\"),\n     \"derivation_fa\": (\"یونانی باستان Περσίς (پرسیس) «پارس» و Πέρσης «پارسی» وام‌واژه‌ای است از پارسی باستان Pārsa که یونانیانِ ایونی در سدهٔ ششم پ.م. با \"\n        \"برخورد با هخامنشیان گرفتند؛ از «پارسیانِ» آیسخولوس (۴۷۲ پ.م.) و هرودوت به بعد در ادب یونانی رایج است و کنت نیز در ذیل Pārsa- صورت‌های Πέρσαι و \"\n        \"Περσία را می‌آورد. آوای «ا»ی ایرانی در یونانی به e بدل شده (Πέρσ-) در حالی که در Παρθία همان a مانده است؛ این را نه قاعدهٔ آوایی یونانی، بلکه \"\n        \"صورتی می‌دانند که نام از راه واسطه‌های مادی/عیلامی به ایونیه رسیده است. ادعای نورایی در این گره درست است.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%F0%90%8E%B1%F0%90%8E%A0%F0%90%8E%BC%F0%90%8E%BF\",\n       \"https://www.etymonline.com/word/Parthian\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"SYN:377\", \"status\": \"partial\",\n        \"note\": (\"Buck p. 377 (SYN.txt leaf 423, section 5.74 PEACH) reads 'Nearly all the words for ‘peach’ come from ‘Persian’, indicating the \"\n          \"source of the peach … Grk. μῆλον περσικόν, Lat. malum Persicum. From the latter as persicum or persica … come It. pesca, Fr. pêche (> ME peche, \"\n          \"NE peach)'. The page therefore documents the peach chain of nodes 3–5 splendidly, but it discusses the adjective Περσικός, not the place-name \"\n          \"Περσίς that this node states.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"SYN\", \"where\": \"Buck 5.74 PEACH, p. 377\", \"stance\": \"partial\",\n        \"note\": \"'μῆλον περσικόν, Lat. malum Persicum' — the Greek adjective 'Persian' as the source of the European peach words.\"},\n       {\"src\": \"KNT\", \"where\": \"p. 196 s.v. Pārsa-\", \"stance\": \"supports\",\n        \"note\": \"Kent gives 'Gk. Πέρσαι, Περσία' as the Greek reflexes of OP Pārsa-.\"},\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 28272 s.v. Persis / Persian\", \"stance\": \"supports\",\n        \"note\": \"'Persis, fern. PN. — L., fr. Gk. Πέρσις, lit. ‘a Persian woman’, rel. to Πέρσης, ‘Persian’. See Persia.'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Latin\", \"words\": \"persis; malus persica\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin took both the place-name and the fruit-name from Greek. Persis, -idis f. (and the commoner Persia) is a straight loan of Περσίς; \"\n        \"mālum Persicum 'Persian apple' calques Greek μῆλον περσικόν, the peach being known at Rome from the 1st c. CE (Pliny, NH 15.45, discusses the \"\n        \"persica) as a fruit that reached the Mediterranean from Iran, though the tree is native to China. The neuter plural Persica was reinterpreted as a \"\n        \"feminine singular persica, whence Late Latin pessica; Klein: 'Late L. persica, taken for a fem. sing. noun, but orig. pl. of L. Persicum (malum or \"\n        \"pomum), ‘Persian apple’'. The node carries no reference of its own in the book.\"),\n     \"derivation_fa\": (\"لاتین هم نام سرزمین و هم نام میوه را از یونانی گرفت: Persis (و صورت رایج‌تر Persia) وام مستقیم Περσίς است، و mālum Persicum «سیب \"\n        \"پارسی» گرته‌برداری از μῆλον περσικόν یونانی است؛ هلو از سدهٔ نخست میلادی در روم شناخته بود (پلینیوس، تاریخ طبیعی ۱۵٫۴۵) و آن را میوه‌ای می‌دانستند \"\n        \"که از راه ایران به مدیترانه رسیده است، هرچند خاستگاه درخت چین است. سپس جمعِ خنثای Persica را مفردِ مؤنث persica پنداشتند و از آن لاتینِ متأخر \"\n        \"pessica پدید آمد (کلاین). این گره درست است، هرچند نورایی برای آن مأخذی نیاورده است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/peach\"],\n     \"ref_check\": [\n       {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n        \"note\": \"The chart gives no reference for this Latin node; the claim was checked against Buck 5.74 (SYN p. 377), Klein s.v. peach and Skeat s.v. peach instead.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 27768 s.v. peach, n.\", \"stance\": \"supports\",\n        \"note\": \"'ME. peche, fr. OF. pesche (F. pêche), fr. Late L. persica, taken for a fem. sing. noun, but orig. pl. of L. Persicum (malum or pomum), ‘Persian apple’ … fr. Persia.'\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Peach (SKT.txt l. 13332)\", \"stance\": \"supports\",\n        \"note\": \"'M.E. peche. — O.F. pesche, a peach. — L. persicum, a peach; so called from growing on the Persica arbor, Persian tree. — Pers. Pārs, Persia.'\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 5.74, p. 377\", \"stance\": \"supports\",\n        \"note\": \"'Grk. μῆλον περσικόν, Lat. malum Persicum.'\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"Persia, peach\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Persia is correctly drawn from Latin: Middle English Perse (c. 1200), later Persia, from Latin Persia < Greek Περσίς < OP Pārsa \"\n        \"(Etymonline s.v. Persia). Peach, however, did not come into English from Latin directly, as the arrow implies: it is ME peche/peoche (c. 1400) \"\n        \"from Old French pesche (mod. pêche), i.e. through the French node #5 of this very chart, from Medieval Latin pesca / Late Latin pessica for \"\n        \"persica. English did once have a direct Latin loan — Old English persoc/persue — but it died out and is not the ancestor of peach. So the node's \"\n        \"words are right and their ultimate source is right; only the immediate parent of 'peach' is misdrawn.\"),\n     \"derivation_fa\": (\"«Persia» درست از لاتین گرفته شده است: انگلیسی میانه Perse (حدود ۱۲۰۰ م) و سپس Persia از لاتین Persia از یونانی Περσίς از پارسی \"\n        \"باستان Pārsa. اما «peach» یکراست از لاتین به انگلیسی نرسیده است: صورت انگلیسی میانه peche (حدود ۱۴۰۰ م) وام‌واژه‌ای است از فرانسهٔ کهن pesche \"\n        \"(فرانسهٔ امروز pêche)، یعنی از همان گرهِ فرانسویِ شمارهٔ ۵ همین نمودار. انگلیسی کهن وام مستقیمی از لاتین داشت (persoc) که از میان رفت و نیای \"\n        \"peach نیست. پس واژه‌ها و خاستگاه دورشان درست است و تنها پیکانِ «لاتین ← انگلیسی» برای peach نادرست کشیده شده است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/peach\",\n       \"https://www.ahdictionary.com/word/search.html?q=peach\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD:963\", \"status\": \"partial\",\n        \"note\": (\"AHD:963 is a page of the 1975/76 New College main dictionary, which is not on disk (only Watkins's IE-roots appendix is). The current AHD \"\n          \"entry, fetched from ahdictionary.com, reads: '[Middle English peche, from Old French, a peach, from Latin persica, peach tree, from Greek \"\n          \"persikē, from feminine of Persikos, Persian; see PERSE.]' — it supports the Greek/Latin ancestry but routes English peach through Old French, \"\n          \"not straight from Latin as the chart's arrow does.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. peach, n. and Persian, adj. (KLN_1966.txt ll. 27768, 28270)\", \"stance\": \"partial\",\n        \"note\": \"'peach … ME. peche, fr. OF. pesche' (via French); 'Persian, adj. and n. — ME. Persien, fr. F. persien, fr. L. Persia.'\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Peach (1)\", \"stance\": \"partial\",\n        \"note\": \"'M.E. peche. — O.F. pesche' — again through Old French, though Skeat's chain ends in 'Pers. Pārs, Persia'.\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 5.74, p. 377\", \"stance\": \"partial\",\n        \"note\": \"'Fr. pêche (> ME peche, NE peach)' — Buck too makes French the immediate source of the English word.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"French\", \"words\": \"pěches; pěches melba\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": (\"The derivation is right but the form printed is not French. Latin persica > Late Latin pessica > Old French pesche (11th–12th c.), where \"\n        \"intervocalic -rs- assimilated and pre-consonantal s was later lost, the loss being marked in the modern spelling by the circumflex: pêche. So the \"\n        \"word is pêche (sg.), and the dessert is pêche Melba — created by Auguste Escoffier at the Savoy in London in 1892/93 for the Australian soprano \"\n        \"Nellie Melba (first as pêche au cygne, renamed pêche Melba when he added the raspberry purée at the Carlton). The book prints 'pěches' and 'pěches \"\n        \"melba' with a caron and a plural -s: the caron is Nourai's habitual substitute for the French circumflex (the extraction is faithful to the page — \"\n        \"see the rendered page at data/verification/sources/refs/ocr/BOOK/382.png), and 'melba' should be capitalised as a person's name.\"),\n     \"derivation_fa\": (\"خودِ گشتِ آوایی درست است ولی صورتِ چاپ‌شده فرانسوی نیست: از لاتینِ persica به لاتینِ متأخر pessica و سپس فرانسهٔ کهن pesche رسیده‌ایم؛ \"\n        \"«س» پیش از همخوان بعدها افتاده و نشانهٔ آن در املای امروز، هجای کشیدهٔ ê است: pêche. پس صورت درست مفردِ pêche است و نام آن دسر pêche Melba، که \"\n        \"اوگوست اسکوفیه در سال ۱۸۹۲/۹۳ در هتل ساووی لندن به افتخار نلی ملبا، سوپرانوی استرالیایی، ساخت. کتاب «pěches» و «pěches melba» چاپ کرده است؛ نشانهٔ \"\n        \"«ˇ» جانشین همیشگیِ نورایی برای «ˆ» فرانسوی است و «س» جمع هم زائد است. این خطای چاپیِ کتاب است، نه خطای خوانشِ اسکن (تصویر صفحه بازبینی شد).\"),\n     \"error_in\": \"book\",\n     \"book_prints\": \"pěches : peach ; pěches melba : peach ice cream\",\n     \"correct_form\": \"pêche 'peach' ; pêche Melba\",\n     \"sources\": [\n       \"https://en.wikipedia.org/wiki/Peach_Melba\",\n       \"https://www.etymonline.com/word/peach\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"VOP:120\", \"status\": \"not_checked\",\n        \"note\": \"Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (Alborz 1371) — refs_online.json records kind 'none': no scan, no ebook, no catalogue copy found, so the page cannot be read.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. peach, n.\", \"stance\": \"supports\",\n        \"note\": \"'fr. OF. pesche (F. pêche)' — with the circumflex, i.e. pêche, not 'pěches'.\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 5.74, p. 377\", \"stance\": \"supports\",\n        \"note\": \"'Fr. pêche' listed as the French word for peach.\"},\n       {\"src\": \"Wikipedia (Peach Melba)\", \"where\": \"en.wikipedia.org/wiki/Peach_Melba\", \"stance\": \"supports\",\n        \"note\": \"'Peach Melba (French: pêche Melba …) … invented in 1892 or 1893 by the French chef Auguste Escoffier at the Savoy Hotel, London, to honour the Australian soprano Nellie Melba.'\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Persian\", \"words\": \"pešmelbâ\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian پش‌ملبا / پشملبا (pešmelbā), also written پیچ‌ملبا, is a 20th-century loan of French pêche Melba, taken over with the restaurant \"\n        \"and confectionery vocabulary that entered Persian from French; پش renders French pêche [pɛʃ] with the š that Persian hears at the end of the \"\n        \"French word, and ملبا is the singer's stage name Melba (itself from Melbourne). Persian cookery sites still describe it as «دسر کلاسیک فرانسوی» of \"\n        \"peaches, raspberry sauce and vanilla ice cream, and give exactly Escoffier's 1892/93 story. Only the first element belongs to this chart's root: \"\n        \"پش < pêche < persica < Περσικόν < Pārsa; the second element has nothing to do with Persia.\"),\n     \"derivation_fa\": (\"«پش‌ملبا» (و املای رایج «پشملبا» و نیز «پیچ‌ملبا») وام‌واژه‌ای است سدهٔ چهاردهمی/بیستمی از فرانسوی pêche Melba که همراه با واژگان \"\n        \"رستوران و شیرینی‌پزی از فرانسه به فارسی آمد؛ «پش» همان pêche فرانسوی است و «ملبا» نام هنری نلی ملبا (برگرفته از شهر ملبورن). منابع آشپزی فارسی نیز \"\n        \"آن را «دسر کلاسیک فرانسوی» از هلو و سس تمشک و بستنی وانیلی می‌خوانند و همان داستان اسکوفیه در ۱۸۹۲/۹۳ را می‌آورند. تنها جزء نخستِ این ترکیب به \"\n        \"ریشهٔ همین نمودار بازمی‌گردد (پش < pêche < persica < Περσικόν < Pārsa) و جزء دوم هیچ پیوندی با پارس ندارد. ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://blog.okala.com/peche-melba-dessert/\",\n       \"https://en.wikipedia.org/wiki/Peach_Melba\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"VOP:120\", \"status\": \"not_checked\",\n        \"note\": \"Moshiri's dictionary of European words in Persian is not available in any form (refs_online.json: kind 'none'); the Persian word was checked against current Persian usage instead.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"BQT_v1/v2_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"grep پشملبا / ملبا finds nothing — a 17th-century dictionary would not have a 19th-century French dessert.\"},\n       {\"src\": \"MON\", \"where\": \"MON_part1/part2.txt\", \"stance\": \"silent\",\n        \"note\": \"grep پشملبا returns nothing in the Mo'in lexicon text on disk.\"},\n       {\"src\": \"web (Okala magazine, Persian)\", \"where\": \"blog.okala.com/peche-melba-dessert\", \"stance\": \"supports\",\n        \"note\": \"«دسر پش ملبا یا پیچ ملبا یک دسر کلاسیک با هلو و بستنی است. این دسر که به … pêche melba شناخته می‌شود …» — the Persian word, and its French source, in current use.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Parth, Parni, Parthava, Partia\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Old Persian Parθava- adj. 'Parthian', m. 'Parthia' (Kent p. 196); Greek Πάρθοι/Παρθία, Latin Parthia\",\n   \"note\": (\"The Old Persian word is real and Kent p. 196 gives it exactly: 'Parθava- adj. ‘Parthian’, also masc. as sb. ‘Parthia’, a province of \"\n     \"the Persian Empire: Elam. par-tu-ma, Akk. pa-ar-tu-ú, Gk. Παρθία. Extension of stem seen with vriddhi in Pārsa-, but with dialectal difference in \"\n     \"the θ/s.' Three qualifications. (1) 'Parth' and 'Partia' are the English/Latin shapes of the name, not Old Persian forms; the OP forms are Parθava- \"\n     \"(nom. Parθava, loc. Parθavaiy, attested at Bisotun and Naqš-e Rostam, also in Bartholomae's AiW). (2) 'Parni' is a different name: the Πάρνοι/Ἄπαρνοι \"\n     \"were an East Iranian tribe of the Dahae confederacy living on the Ochus (Tejen) east of the Caspian; they conquered the satrapy of Parthava and their \"\n     \"Arsacid chiefs then took the name of the province — so Parni and Parθava are historically connected but not the same word. (3) The date is loose: \"\n     \"Arsaces' revolt is put at 247 or 238 BCE, and the Seleucid Greeks were driven out of the Iranian plateau only under Mithridates I, c. 148–141 BCE. \"\n     \"Since Kent derives Parθava- from the same stem as Pārsa-, this root and entry 0 are ultimately one.\"),\n   \"note_fa\": (\"صورت پارسی باستان درست است و کنت در ص ۱۹۶ همان را می‌آورد: «Parθava- صفت «پارتی» و اسم «پارت»، ایالتی از شاهنشاهی هخامنشی؛ عیلامی par-tu-ma، \"\n     \"اکدی pa-ar-tu-ú، یونانی Παρθία؛ گسترشِ همان ستاکی که در Pārsa- با وریدی دیده می‌شود، با اختلاف گویشیِ θ/s». سه نکته را باید افزود: نخست آنکه \"\n     \"«Parth» و «Partia» صورت‌های انگلیسی و لاتینی‌اند نه پارسی باستان (صورت‌های کتیبه‌ای Parθava و Parθavaiy است). دوم آنکه «پَرنی» (Πάρνοι/Ἄπαρνοι) نام \"\n     \"دیگری است: تیره‌ای ایرانیِ شرقی از اتحادیهٔ دَهه در کنارهٔ رود اُخوس که ساتراپیِ پَرثَوَه را گرفتند و سپس نام آن ایالت را بر خود نهادند؛ پس پیوند \"\n     \"تاریخی هست ولی این دو یک واژه نیستند. سوم آنکه تاریخ ۲۵۰ پ.م. تقریبی است (خیزش اَرشک را ۲۴۷ یا ۲۳۸ پ.م. می‌دانند) و بیرون‌راندن سلوکیان از فلات \"\n     \"ایران در زمان مهرداد یکم (حدود ۱۴۸–۱۴۱ پ.م.) رخ داد. چون کنت Parθava را از همان ستاک Pārsa می‌داند، این ریشه و ریشهٔ نخست این صفحه در اصل یکی‌اند.\"),\n   \"sources\": [\n     \"https://www.etymonline.com/word/Parthian\",\n     \"https://en.wikipedia.org/wiki/Parni\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"KNT:196\", \"status\": \"supports\",\n      \"note\": (\"KNT.txt leaf 220 (printed p. 196), s.v.: 'Parθava- adj. ‘Parthian’, also masc. as sb. ‘Parthia’, a province of the Persian Empire: \"\n        \"Elam. par-tu-ma, Akk. pa-ar-tu-ú, Gk. Παρθία. Extension (§150) of stem seen with vriddhi in Pārsa-, but with dialectal difference in the θ/s.' \"\n        \"Supports the Old Persian root and the province sense; Kent says nothing about the Parni.\")}\n   ],\n   \"consulted\": [\n     {\"src\": \"KNT\", \"where\": \"p. 196 s.v. Parθava-\", \"stance\": \"supports\",\n      \"note\": \"Gives Parθava nsm. at DB 1.16; 2.7, 92; DPe 15; DNa 22 etc., and derives it from the same stem as Pārsa-.\"},\n     {\"src\": \"BRT\", \"where\": \"AiW, OP entries citing parθavaiy (BRT.txt ll. 14927, 24441)\", \"stance\": \"supports\",\n      \"note\": \"'p. pati-grabanā- f. Name einer Stadt in Parthien: … vardanam parθavaiy Bh. 3.1' — Bartholomae attests the OP locative Parθavaiy 'in Parthia'.\"},\n     {\"src\": \"Wikipedia (Parni)\", \"where\": \"en.wikipedia.org/wiki/Parni\", \"stance\": \"contradicts\",\n      \"note\": \"'The Parni (Ancient Greek: Πάρνοι), Aparni … were an East Iranian people who lived around the Ochus … one of the three tribes of the Dahae confederacy' — not a Khorasani Persian tribe and not the same name as Parθava.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"pârt; pahlov\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"پارت (pārt) is a modern learned re-adoption of the ancient name (through European scholarship and the cuneiform decipherments), used in \"\n        \"Persian for the Arsacid people and dynasty; Mo'in's lexicon has «پارتی: منسوب به پارت … زبان پهلوی اشکانی». پهلو (pahlav/pahlov) is the inherited \"\n        \"reflex: Old Persian Parθava- > Middle Persian pahlaw, by the regular north-western development in which OP -rθ- passes through -rh- to -hl- — \"\n        \"Hübschmann §97 states it in so many words ('Ap. rθ ist (über rh) zu hl geworden: pahlav ursprünglich = Parthien … = ap. Parθava-'), and Horn no. 343 \"\n        \"s.v. pehlev, pehlevān gives 'ap. Parθava-; phlv. pahlav'. MacKenzie has pahlawīg 'Parthian; Pahlavi', and Nyberg records pahlavān 'heroes' in the \"\n        \"epic. Because the Arsacid grandees (Kārin, Sūrēn, Espahbad) were styled pahlav, the word slid from 'Parthian' to 'grandee, champion, hero', whence \"\n        \"پهلوان — exactly Mo'in's entry «پهلو [پهلوی pahlav، از پارت] … دلیر، شجاع، گرد، پهلوان». Of the extra forms in the box, پهلوی is pahlavī 'Parthian; \"\n        \"the Pahlavi language'; پهلبد is less certain — Dehkhoda treats it as an erroneous writing of باربد, Khosrow II's minstrel (Arabic فهلبذ). Nourai is \"\n        \"right to number the headword پَهلو ۱, since the homograph پهلو 'side, rib' is a different word (MP pahlūg < Proto-Iranian *pārću-/*párcuš 'rib'), \"\n        \"which Horn (no. 342) and MacKenzie keep apart from pahlaw.\"),\n     \"derivation_fa\": (\"«پارت» وام‌گیریِ دوبارهٔ نوین و کتابی از همان نام باستانی است که پس از خوانده‌شدن خط میخی به فارسی راه یافت و امروز نام قوم و دودمان \"\n        \"اشکانی است (معین: «پارتی: منسوب به پارت … زبان پهلوی اشکانی»). اما «پهلو» بازماندهٔ طبیعیِ آن است: پارسی باستان Parθava > فارسی میانه pahlaw، با \"\n        \"تحوّل شناخته‌شدهٔ -rθ- به -hl- (از راه -rh-)؛ هوبشمان در بند ۹۷ همین را می‌نویسد و هرن (شمارهٔ ۳۴۳) ذیل «پهلو، پهلوان» می‌آورد «ap. Parθava-؛ \"\n        \"پهلوی pahlav». مکنزی pahlawīg «پارتی، پهلوی» را ثبت کرده و نیبرگ pahlavān را در حماسه. چون بزرگانِ اشکانی (کارن، سورن، اسپاهبذ) «پهلو» خوانده \"\n        \"می‌شدند، معنی از «پارتی» به «بزرگ‌زاده، دلاور، پهلوان» گرایید؛ معین نیز می‌نویسد «پهلو [پهلوی pahlav، از پارت] … دلیر، شجاع، گرد، پهلوان». از \"\n        \"صورت‌های افزودهٔ کادر، «پهلوی» همان pahlavī است، ولی «پهلبد» تردیدآمیز است و دهخدا آن را نگارشِ نادرستِ «باربد» می‌داند. شمارهٔ «پَهلو ۱» درست \"\n        \"گذاشته شده، زیرا هم‌نگاشتِ «پهلو» به معنی «تهیگاه، دنده» واژهٔ دیگری است (فارسی میانه pahlūg از ایرانی آغازین *párcuš «دنده») که هرن (۳۴۲) و \"\n        \"مکنزی از pahlaw جدایش می‌کنند.\"),\n     \"sources\": [\n       \"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88\",\n       \"https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88%D8%A7%D9%86\",\n       \"https://abadis.ir/fatofa/%D9%BE%D9%87%D9%84%D8%A8%D8%AF/\",\n       \"https://www.etymonline.com/word/Parthian\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"BQT\", \"status\": \"supports\",\n        \"note\": (\"Borhān-e Qāṭe', Mo'in's footnote s.v. پارت (BQT_v1_pages.txt line 23117): «پارت – پارسی باستان Parθava مقرّ قوم پارت (خراسان قدیم) – خود \"\n          \"قوم پارت از اقوام ایرانی؛ کلمهٔ پهلو و پهلوی (ه‍.م) ازین نام مشتق است» — literally Nourai's arrow.\")},\n       {\"ref\": \"MON\", \"status\": \"supports\",\n        \"note\": (\"Mo'in, Farhang-e Fārsi s.v. پهلو (MON_part1.txt l. 33624): «پهلو [پهلوی pahlav، از پارت] (ص. اِ.) پارت. در عهد ساسانی عنوان و لقب رؤسای \"\n          \"خاندان‌های «قارن» و «سورن» و «اسپاهبذ» که از نژاد اشکانیان بودند … دلیر، شجاع، گرد، پهلوان» — the same word and the same semantic path.\")},\n       {\"ref\": \"FSF:117\", \"status\": \"not_found\",\n        \"note\": (\"Nushin's Vāže-nāmak on disk (FSF_pages.txt): the pages numbered in the 113–120 range are still in the ب section (بوس p. 113, بویه, بهانه), \"\n          \"so no پهلو entry can stand on p. 117 of this printing. The Ferdowsi line Nourai quotes does occur in the book, s.v. کوچ و بلوچ (form-feed page \"\n          \"372, printed ~370): «هم از پهلو پارس و کوچ و بلوچ / ز گیلان جنگی و دشت سروچ» — note that Nourai's quotation prints پهلوی for پهلو and سروج for \"\n          \"the rhyme-word سروچ.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"HUB\", \"where\": \"Persische Studien §97 (HUB.txt l. 7374)\", \"stance\": \"supports\",\n        \"note\": \"'Ap. rθ ist (über rh) zu hl geworden: pahlav urspr. = Parthien (ZDMG 31,558), pahlavī ‘parthisch’, arm. Pahlav … = ap. Parθava- ‘Parthien’, gr. Πάρθοι.'\"},\n       {\"src\": \"HRN\", \"where\": \"Grundriss no. 343 (HRN.txt l. 3249)\", \"stance\": \"supports\",\n        \"note\": \"'343. pehlev, pehlevān ‘Held’. ap. Parθava-; phlv. pahlav' — and in no. 342 just above, Horn keeps np. pehlū ‘Seite’ (Skt. pārśva-, oss. fars) apart from it.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p. 66 s.v. pahlawīg / pahlūg (PHD_pages.txt l. 3977, PHD.txt l. 540)\", \"stance\": \"supports\",\n        \"note\": \"'pahlawīg [pʾhlwbyk’ | N pahlaw(ān)ī] Parthian; Pahlavi' beside 'pahlūg [pʾhlwk’ | N pahlū] side, rib' — the two homographs distinguished in Middle Persian.\"},\n       {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt l. 2888)\", \"stance\": \"partial\",\n        \"note\": \"'… still surviving in pahlavān ‘heroes’, pahlavānī ‘heroic’ in the epic' — attests the semantic outcome (there s.v. pāhlom, a different but neighbouring word).\"},\n       {\"src\": \"MON\", \"where\": \"s.v. پهلو and پهلوان (MON_part1.txt ll. 33624, 33642)\", \"stance\": \"supports\",\n        \"note\": \"«پهلو [پهلوی pahlav، از پارت] … دلیر، شجاع، گرد، پهلوان»؛ «پهلوان: منسوب به پهلو».\"},\n       {\"src\": \"Wiktionary\", \"where\": \"s.v. پهلو (Persian, Etymology 2) and پهلوان\", \"stance\": \"supports\",\n        \"note\": \"'Inherited from Middle Persian /pahlaw/, from Old Persian 𐎱𐎼𐎰𐎺 (Parθavaʰ, ‘Parthian’)'; پهلوان 'Ultimately from the name of the Parthians'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"English\", \"words\": \"Parthia; parting shot\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Parthia is straightforward: English Parthia/Parthian (1520s) from Latin Parthia, Greek Παρθία, from OP Parθava- (Etymonline: 'from Old \"\n        \"Persian Parthava- ‘Parthian’, dialectal variant of the stem Parsa-, source of Persia'); the older plural Partienes is attested c. 1300. \"\n        \"'Parting shot' is the weaker half. The tactic is genuine and gave English 'Parthian shot' (the image is in use from the 1630s, 'Parthian fight'; the \"\n        \"exact phrase by 1832) for the arrow the Parthian horseman looses backwards while retreating. Klein states flatly that 'Parthian shot is a ‘parting \"\n        \"shot’; so called from the habit of Parthian horsemen to shoot backward while retiring', and Wiktionary calls parting shot 'believed to be a \"\n        \"variation of Parthian shot'; but 'parting shot' is later (1894) and is perfectly analysable as English parting + shot, so lexicographers usually \"\n        \"present the equation as a probable folk-etymological reshaping rather than a derivation. Hence plausible, not confirmed.\"),\n     \"derivation_fa\": (\"«Parthia» بی‌گمان درست است: انگلیسی Parthia/Parthian (سدهٔ شانزدهم) از لاتین Parthia و یونانی Παρθία از پارسی باستان Parθava (اتیمانلاین: \"\n        \"«از پارسی باستان Parthava، گونهٔ گویشیِ همان ستاکِ Parsa»). اما «parting shot» سست‌تر است: شگردِ تیراندازیِ سوارانِ پارتی به‌هنگام واپس‌نشینی واقعی \"\n        \"است و در انگلیسی «Parthian shot» را پدید آورده (تصویرش از سدهٔ هفدهم و خودِ عبارت از ۱۸۳۲)؛ کلاین نیز می‌نویسد «Parthian shot همان parting shot است». \"\n        \"ولی «parting shot» دیرتر (۱۸۹۴) پیدا شده و در انگلیسی به‌سادگی «parting + shot» تحلیل‌پذیر است، از این‌رو فرهنگ‌نویسان آن را بیشتر «ریشه‌شناسی عامیانه» \"\n        \"و بازسازیِ صوریِ Parthian shot می‌دانند تا اشتقاق مستقیم. پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/Parthian\",\n       \"https://en.wiktionary.org/wiki/parting_shot\",\n       \"https://en.wiktionary.org/wiki/Parthian_shot\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD:955\", \"status\": \"partial\",\n        \"note\": (\"AHD:955 belongs to the 1975/76 New College main dictionary, which is not on disk. The current AHD entry (ahdictionary.com) reads 'Par·thi·an \"\n          \"adj. 1. Of or relating to Parthia … 2. Delivered in or as if in retreat: “a Parthian volley of expletives from Uncle Billy” (Bret Harte)' — it \"\n          \"confirms the Parthian-retreat sense but gives no etymology for 'parting shot'.\")},\n       {\"ref\": \"WEB:1306\", \"status\": \"not_checked\",\n        \"note\": \"Only volume 1 (A–M; the local WEB_vol1.txt ends in the memo- range) of Webster's New Twentieth Century, 2nd ed. is on disk, so p. 1306 (the Par- range, vol. 2) cannot be read; grep 'Parthian' in WEB_vol1.txt returns nothing.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 27529 s.v. Parthian\", \"stance\": \"supports\",\n        \"note\": \"'Parthian, adj., of Parthia. — Formed with suff. -an fr. Parthia … Parthian shot is a ‘parting shot’; so called from the habit of Parthian horsemen to shoot backward while retiring.'\"},\n       {\"src\": \"Etymonline\", \"where\": \"s.v. Parthian\", \"stance\": \"partial\",\n        \"note\": \"'from Old Persian Parthava- ‘Parthian’, dialectal variant of the stem Parsa- … The exact phrase [Parthian shot] is attested by 1832' — supports Parthia, dates the phrase, does not mention parting shot.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"s.v. parting shot\", \"stance\": \"partial\",\n        \"note\": \"'Believed to be a variation of Parthian shot, referring to a military maneuver in which Parthian troops retreating on horseback turned back to face the enemy and shot while retreating.'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Latin\", \"words\": \"pertica pellis; particaminum\", \"verdict\": \"disputed\",\n     \"derivation\": (\"Two things are wrong here. First the form: the Latin for 'Parthian leather' is Parthica (pellis) — pertica in Latin means 'a pole, measuring \"\n        \"rod' — and the Vulgar Latin blend is *particamīnum; the printed page (see data/verification/sources/refs/ocr/BOOK/382.png) really does read 'pertica \"\n        \"pellis' and 'particaminum', so the extraction is faithful and the slip is the book's. Second and more important, parchment is not a Parthian word. \"\n        \"Its etymon is the city of Pergamon in Mysia, where skin is said to have replaced papyrus in the 2nd c. BCE: Greek περγαμηνή (χάρτης) > Late Latin \"\n        \"pergamēna/pergamīna (Pliny's pergamena charta) > Medieval Latin pergamentum/percamentum. Klein sets it out and adds the only role Parthica has: 'F. \"\n        \"parchemin was influenced in form by an association with L. Parthica (pellis), ‘skin from the land of the Parthians’.' Skeat and Funk & Wagnalls give \"\n        \"Pergamon alone; Etymonline says the form 'was possibly influenced in Vulgar Latin by Latin parthica (pellis)'; the current AHD entry drops Parthica \"\n        \"altogether. So the Parthian element is a contaminating association, not the source, and the chart's arrow — Parthian leather → parchemin → parchment \"\n        \"— states as the etymology what the sources allow only as an influence on the form.\"),\n     \"derivation_fa\": (\"دو اشکال در این گره هست. نخست صورتِ واژه: «چرم پارتی» در لاتین Parthica (pellis) است — pertica در لاتین «چوب‌دست، ترکه» معنی می‌دهد — و \"\n        \"صورت آمیختهٔ لاتین عامیانه *particamīnum است؛ تصویر صفحهٔ چاپی (در ocr/BOOK/382.png) نشان می‌دهد که خودِ کتاب «pertica pellis» و «particaminum» چاپ \"\n        \"کرده است، پس این خطای چاپیِ کتاب است نه خطای خوانشِ اسکن. دوم و مهم‌تر آنکه parchment اساساً واژه‌ای پارتی نیست: خاستگاه آن شهر «پرگاموم» در میسیا \"\n        \"است که گویند در سدهٔ دوم پ.م. در آنجا پوست جای پاپیروس را گرفت: یونانی περγαμηνή، لاتین متأخر pergamēna، لاتین میانه pergamentum. کلاین همین را \"\n        \"می‌آورد و نقش Parthica را تنها «اثرگذاری صوری» می‌داند؛ اسکیت و فانک‌ووگنالز فقط پرگاموم را می‌آورند و ویراست امروزی AHD نام پارت را یکسره حذف کرده \"\n        \"است. پس پژوهش امروزی ادعای نورایی را رد می‌کند و «پارتی‌بودن» را تنها آمیختگی صوری می‌شمارد.\"),\n     \"error_in\": \"book\",\n     \"book_prints\": \"pertica pellis : Parthian leather ; particaminum\",\n     \"correct_form\": \"Parthica (pellis) 'Parthian leather'; Vulgar Latin *particamīnum\",\n     \"sources\": [\n       \"https://www.etymonline.com/word/parchment\",\n       \"https://www.ahdictionary.com/word/search.html?q=parchment\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD:952\", \"status\": \"contradicts\",\n        \"note\": (\"AHD:952 is a page of the 1975/76 New College main dictionary (not on disk; earlier AHD editions did print a blend etymology). What is \"\n          \"checkable, the current AHD entry, reads: '[Middle English parchemin, parchement (influenced by Medieval Latin pergamentum), from Old French \"\n          \"parchemin, from Late Latin pergamīna, variant of Latin pergamēna, from feminine of Pergamēnus, of Pergamum, from Greek Pergamēnos, after \"\n          \"Pergamon (Pergamum).]' — no Parthian element at all.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 27374 s.v. parchment\", \"stance\": \"partial\",\n        \"note\": \"'fr. L. Pergamena, Pergamina … fr. Gk. περγαμηνή ‘(skin) of Pergamon’ … F. parchemin was influenced in form by an association with L. Parthica (pellis), ‘skin from the land of the Parthians’.'\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Parchment (SKT.txt l. 13265)\", \"stance\": \"contradicts\",\n        \"note\": \"'M.E. parchemin. — F. parchemin. — L. pergamina, pergamena, parchment; fem. of L. Pergamenus, belonging to Pergamos (where parchment was first invented). — Gk. περγαμηνή' — Parthia not mentioned.\"},\n       {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. parchment (FSD_vol3.txt l. 121137)\", \"stance\": \"contradicts\",\n        \"note\": \"'< F … < L pergamena, < Gr. Pergamēnē, Pergamon, Pergamum, a city of Asia Minor, whence parchment was first brought.'\"},\n       {\"src\": \"Etymonline\", \"where\": \"s.v. parchment\", \"stance\": \"partial\",\n        \"note\": \"'from Late Latin pergamena ‘parchment’ … The form of the word was possibly influenced in Vulgar Latin by Latin parthica (pellis) ‘Parthian (leather)’.'\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Old French\", \"words\": \"parchemin\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Old French parchemin (11th c., Old North French parcamin) is real and is indeed the immediate source of the English word, but it continues \"\n        \"Late Latin pergamīna / Medieval Latin pergamentum, not a Parthian word: the shift of the first syllable per- > par- and the -c- are what the \"\n        \"Vulgar-Latin association with Parthica (pellis) is invoked to explain (Klein: 'F. parchemin was influenced in form by an association with L. Parthica \"\n        \"(pellis)'), which is why Vulgar Latin *particamīnum is reconstructed as a blend. The node is thus correct as a word and as a link to #5, but its \"\n        \"parentage in the chart (a purely Parthian Latin form) is only half of the accepted account. No reference is given for the node.\"),\n     \"derivation_fa\": (\"«parchemin» فرانسهٔ کهن (سدهٔ یازدهم) واژه‌ای واقعی است و همان است که به انگلیسی رسیده؛ اما دنبالهٔ لاتینِ متأخرِ pergamīna و لاتینِ \"\n        \"میانهٔ pergamentum است، نه واژه‌ای پارتی. تبدیل هجای نخست per- به par- و پیدایشِ -c- را همان «آمیختگی» با Parthica (pellis) در لاتین عامیانه توضیح \"\n        \"می‌دهند و به همین سبب صورت آمیختهٔ *particamīnum را بازسازی می‌کنند (کلاین). پس خودِ واژه و پیوندش با «parchment» درست است، ولی نیای آن در نمودار \"\n        \"(صورتی سراسر پارتی) تنها نیمی از تبیینِ پذیرفته‌شده است. نورایی برای این گره مأخذی نیاورده است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/parchment\"],\n     \"ref_check\": [\n       {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n        \"note\": \"The chart cites no reference for the Old French node; checked against Klein s.v. parchment, Skeat s.v. Parchment and Etymonline instead.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. parchment\", \"stance\": \"partial\",\n        \"note\": \"'ME. parchemin, fr. OF. (= F.) parchemin, fr. L. Pergamena, Pergamina' + the note on the Parthica influence on the French form.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Parchment\", \"stance\": \"partial\",\n        \"note\": \"'M.E. parchemin. — F. parchemin. — L. pergamina' — the Old French word affirmed, its Latin source Pergamene.\"},\n       {\"src\": \"Etymonline\", \"where\": \"s.v. parchment\", \"stance\": \"partial\",\n        \"note\": \"'from Old French parchemin (11c., Old North French parcamin) and directly from Medieval Latin pergamentum, percamentum.'\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"parchment\", \"verdict\": \"plausible\",\n     \"derivation\": (\"English parchment (c. 1300, parchemin; a surname already c. 1200) does come straight from Old French parchemin, so the last arrow of the \"\n        \"chart is sound; the unetymological final -t of the modern spelling arose in the 15th c. by analogy with the many nouns in -ent/-ant (as in ancient, \"\n        \"pageant, pheasant) and under the influence of Medieval Latin pergamentum (Klein; Etymonline). What is not sound is the ancestry the chart assigns \"\n        \"further up: the word means 'Pergamene (skin)', and the Parthians enter only through the formal contamination discussed at node #3.\"),\n     \"derivation_fa\": (\"انگلیسی parchment (نخست به صورت parchemin، حدود ۱۳۰۰ م) یکراست از فرانسهٔ کهن parchemin آمده است، پس واپسین پیکانِ نمودار درست است؛ \"\n        \"«t» پایانیِ املای امروزی در سدهٔ پانزدهم و به قیاس با واژه‌های پرشمارِ پایان‌یافته به -ent/-ant (مانند ancient و pheasant) و به اثرِ لاتینِ میانهٔ \"\n        \"pergamentum افزوده شده است (کلاین و اتیمانلاین). آنچه درست نیست، نیای دورترِ آن در نمودار است: این واژه یعنی «پوستِ پرگامومی» و پای پارتیان تنها \"\n        \"از راه همان آمیختگیِ صوریِ یادشده در گرهٔ ۳ به میان آمده است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/parchment\"],\n     \"ref_check\": [\n       {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n        \"note\": \"No reference is given for this node; checked against Klein s.v. parchment, Skeat s.v. Parchment, Funk & Wagnalls s.v. parchment and Etymonline.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. parchment\", \"stance\": \"supports\",\n        \"note\": \"'The alteration of ME. parchemin into E. parchment is due to a confusion of the ending -min with the suff. -ment (fr. L. -mentum) and was prob. suggested by ML. pergamentum.'\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Parchment\", \"stance\": \"supports\",\n        \"note\": \"'M.E. parchemin. — F. parchemin' — the French word as the immediate source of the English one.\"},\n       {\"src\": \"Etymonline\", \"where\": \"s.v. parchment\", \"stance\": \"supports\",\n        \"note\": \"'c. 1300, parchemin … from Old French parchemin … The unetymological Middle English -t probably is by influence of words in -ent.'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-382.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-382.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-382.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 382"
}
```


### [2026-09-07T20:57:47.228Z] TOOL RESULT

```
written
JSON OK
nodes verified: 11/11
node verdicts: {'disputed': 2, 'confirmed': 4, 'plausible': 4, 'transcription_suspect': 1}
root verdicts: {'plausible': 2}
ref checks: {'supports': 4, 'not_checked': 7, 'partial': 3, 'not_found': 1, 'contradicts': 1}
books consulted: {'partial': 13, 'supports': 20, 'silent': 3, 'contradicts': 3} | by book: {'KLN': 8, 'SKT': 5, 'SYN': 4, 'Etymonline': 4, 'MON': 3, 'BQT': 2, 'Wiktionary': 2, 'IRN': 1, 'ARY': 1, 'Encyclopaedia Iranica': 1, 'KNT': 1, 'Wikipedia (Peach Melba)': 1, 'web (Okala magazine, Persian)': 1, 'HUB': 1, 'HRN': 1, 'PHD': 1, 'NYB': 1, 'FSD': 1}
```


## [2026-09-07T20:57:57.706Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nidx={json.loads(l)['url'] for l in open('data/verification/sources/web/index.jsonl',encoding='utf-8')}\nd=json.load(open('data/verification/page-382.json'))\nurls=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources': urls.update(v)\n            else: walk(v)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(d)\nfor u in sorted(urls):\n    print('OK ' if u in idx else 'MISSING ', u)\nEOF"
}
```


### [2026-09-07T20:57:59.133Z] TOOL RESULT

```
OK  https://abadis.ir/fatofa/%D9%BE%D9%87%D9%84%D8%A8%D8%AF/
OK  https://blog.okala.com/peche-melba-dessert/
OK  https://en.wikipedia.org/wiki/Parni
OK  https://en.wikipedia.org/wiki/Peach_Melba
OK  https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88
OK  https://en.wiktionary.org/wiki/%D9%BE%D9%87%D9%84%D9%88%D8%A7%D9%86
OK  https://en.wiktionary.org/wiki/%F0%90%8E%B1%F0%90%8E%A0%F0%90%8E%BC%F0%90%8E%BF
OK  https://en.wiktionary.org/wiki/Parthian_shot
OK  https://en.wiktionary.org/wiki/Pasargadae
OK  https://en.wiktionary.org/wiki/parting_shot
OK  https://www.ahdictionary.com/word/search.html?q=parchment
OK  https://www.ahdictionary.com/word/search.html?q=peach
OK  https://www.etymonline.com/word/Parthian
OK  https://www.etymonline.com/word/parchment
OK  https://www.etymonline.com/word/peach
OK  https://www.iranicaonline.org/articles/pasargadae
```


## [2026-09-07T20:58:17.422Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-382.json` written; `verify_check.py 382` reports 11/11 nodes, 0 PROBLEM lines.

**Page 382 (book p. 352) — 2 entries, 11 nodes**
- Node verdicts: 4 confirmed, 4 plausible, 2 disputed, 1 transcription_suspect. Both roots: plausible.
- Ref checks: 4 supports, 3 partial, 1 contradicts, 1 not_found, 7 not_checked (VOP has no copy anywhere; MON5 = Mo'in vol. 5 a'lam not on disk; WEB:1306 is in Webster vol. 2, only vol. 1 A–M is on disk; three nodes cite nothing).

**disputed**
- Pârsa #1 (Pâsârgâd): Pārs/Fārs is solid (BQT "معرّب آن فارس است"; Wiktionary MP Pārs → Ar. فارس), but Pāsārgād < Pārsa + gard is the classical folk etymology (Anaximenes, Q. Curtius, Farahvashi IRN:63); Iranica (Stronach/Schwartz, Elamite Batrakata(š)) rejects the metathesis and reconstructs OP *Pāθragadā. Nourai's NOTE (tribe name, Hdt. i.125) is right.
- Parth #3 (Latin "pertica pellis / particaminum"): parchment is from Pergamon (Gk. περγαμηνή > LLat. pergamēna); Parthica (pellis) only influenced the form (Klein), and the current AHD, Skeat and Funk & Wagnalls drop Parthia entirely. Nodes #4–#5 downgraded to plausible for the same reason.

**transcription_suspect**
- Pârsa #5 (French): book prints "pěches / pěches melba"; correct is pêche / pêche Melba (Escoffier 1892-93, Nellie Melba). `error_in: book` — the page image confirms the caron is Nourai's own, extraction faithful. Same for "pertica" in Parth #3 (book's misprint for Parthica).

**No extraction errors** — the JSON matches the printed page throughout (page image saved to `data/verification/sources/refs/ocr/BOOK/382.png`).

Other findings worth noting: Kent p. 196 derives Parθava- from the same stem as Pārsa-, so entries 0 and 1 are one root in two dialect shapes; "Parni" (Gk. Πάρνοι, a Dahae tribe) is not the same name as Parθava; FSF:117 is not_found (p. 117 of the local Vāže-nāmak is still in the ب section — the Ferdowsi line Nourai quotes stands on p. ~370 s.v. کوچ و بلوچ, and reads پهلو/سروچ, not Nourai's پهلوی/سروج).
