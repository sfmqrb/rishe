# Verification process log — verify-page-415


## [2026-09-14T01:08:54.978Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 415 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-415.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-415.json. Write /home/sfmqrb/git/rishe/data/verification/page-415.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 415` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:08:56.052Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:08:56.898Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:08:57.000Z] TOOL RESULT

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


## [2026-09-14T01:08:57.269Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-415.txt"
}
```


### [2026-09-14T01:08:57.306Z] TOOL RESULT

```
1	=== PDF page 415 (book page 385) ===
2	--- entry 0 ---
3	ROOT [Old Persian] Raika : sand, gravel  (refs HRN:142; BRT)
4	#1 (parent #0) [Pahlavi] refs=PHD:73 | rěg : sand
5	  #2 (parent #1) [Persian] refs=HUB:68; BQT:989; HRN:142 | rîg «ريگ ( ريگزار ، ريگستان )» : sand, gravel
6	--- entry 1 ---
7	ROOT Raud -> redirect to Raup
8	--- entry 2 ---
9	ROOT [Indo-Schythian] Raup, Raud : to sweep away  (refs ISS:251)
10	#1 (parent #0) [Pahlavi] refs=ISS:252 | rôpet, rôp 2 : sweep ; givâk-rôp : "room sweeper", broom ☞Ei
11	  #2 (parent #1) [Persian] refs=ISS:252 | roftan «رُفتن ( روفتن ، روبیدن )» : to sweep | extra: جاروب ، لايروبی
12	#3 (parent #0) [Sogdian] refs=ISS:251 | rwp : to sweep
13	--- entry 3 ---
14	ROOT [Semitic] R.b.b : to be great, large or numerous  (refs VDQ:214; KLN:1293)
15	#1 (parent #0) [Arabic] refs=KLN:1293; VDQ:214 | r.b.b : to be great, also to be thick and dense
16	  #2 (parent #1) [Persian] refs=VDQ:214; FVA:153,155 | rab, rabb «رَب» : master, teacher, developer, God ; morabbâ «مربّا» : developed (food), jam ; robb «رُبّ» : concentrated (dense) juice | extra: ربّانی ، ارباب ، مربّی ، تربیت
17	#3 (parent #0) [Aramaic] refs=KLN:1293 | rabb : great, chief, master
18	  #4 (parent #3) [Pahlavi] refs=VDQ:215 | raba : great respectful | NOTE: This word had entered Pahlavi language in pre-Islamic era.
19	    #5 (parent #4) [None] refs=None | 
20	#6 (parent #0) [Hebrew] refs=KLN:1293 | r.b.b : to be great or numerous ; rabh : great, master ; rabbi : my master
21	  #7 (parent #6) [Greek] refs=None | 
22	    #8 (parent #7) [Latin] refs=None | 
23	      #9 (parent #8) [English] refs=KLN:1293 | rabbi : my master, my teacher, a Jewish title of respect.
24	--- entry 4 ---
25	ROOT Re -> redirect to Ere 1
26	
```


## [2026-09-14T01:09:00.250Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-415.json",
 "description": "Read source JSON for page 415"
}
```


### [2026-09-14T01:09:00.292Z] TOOL RESULT

```
{
  "pdf_page": 415,
  "book_page": 385,
  "entries": [
    {
      "root": {
        "name": "Raika",
        "lang": "Old Persian",
        "refs": "HRN:142; BRT",
        "gloss": "sand, gravel"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "PHD:73",
          "words": [
            {"translit": "rěg", "gloss": "sand", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HUB:68; BQT:989; HRN:142",
          "words": [
            {"translit": "rîg", "gloss": "sand, gravel", "script": "ريگ ( ريگزار ، ريگستان )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "ريگ آموی و درشتی های او - زير پايم پرنيان آيد همی",
            "poet": "Rŭdakî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Raud",
        "redirect": "Raup"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Raup, Raud",
        "lang": "Indo-Schythian",
        "refs": "ISS:251",
        "gloss": "to sweep away"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "ISS:252",
          "words": [
            {"translit": "rôpet, rôp 2", "gloss": "sweep", "script": null},
            {"translit": "givâk-rôp", "gloss": "\"room sweeper\", broom", "script": null, "see": ["Ei"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "ISS:252",
          "words": [
            {"translit": "roftan", "gloss": "to sweep", "script": "رُفتن ( روفتن ، روبیدن )"}
          ],
          "script_extra": "جاروب ، لايروبی",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "ISS:251",
          "words": [
            {"translit": "rwp", "gloss": "to sweep", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "R.b.b",
        "lang": "Semitic",
        "refs": "VDQ:214; KLN:1293",
        "gloss": "to be great, large or numerous"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:1293; VDQ:214",
          "words": [
            {"translit": "r.b.b", "gloss": "to be great, also to be thick and dense", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "VDQ:214; FVA:153,155",
          "words": [
            {"translit": "rab, rabb", "gloss": "master, teacher, developer, God", "script": "رَب"},
            {"translit": "morabbâ", "gloss": "developed (food), jam", "script": "مربّا"},
            {"translit": "robb", "gloss": "concentrated (dense) juice", "script": "رُبّ"}
          ],
          "script_extra": "ربّانی ، ارباب ، مربّی ، تربیت",
          "note": null,
          "quote": {
            "text": "یا رب بقدر قدر تو نشناختم تو را - در حد فکر کوته خود ساختم تورا",
            "poet": "Vajdî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "KLN:1293",
          "words": [
            {"translit": "rabb", "gloss": "great, chief, master", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "VDQ:215",
          "words": [
            {"translit": "raba", "gloss": "great respectful", "script": null}
          ],
          "script_extra": null,
          "note": "This word had entered Pahlavi language in pre-Islamic era.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:1293",
          "words": [
            {"translit": "r.b.b", "gloss": "to be great or numerous", "script": null},
            {"translit": "rabh", "gloss": "great, master", "script": null},
            {"translit": "rabbi", "gloss": "my master", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Greek",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "KLN:1293",
          "words": [
            {"translit": "rabbi", "gloss": "my master, my teacher, a Jewish title of respect.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Re",
        "redirect": "Ere 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:09:00.979Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:09:01.029Z] TOOL RESULT

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


## [2026-09-14T01:09:07.969Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['HRN','BRT','PHD','HUB','BQT','ISS','VDQ','FVA','KLN','MON','SOD','CHEUNG','NYB','AFA','FVQ','ARY']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-14T01:09:08.746Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"raika\\|rēg\\|reg .sand\\|rīg\" HRN.txt | head -40"
}
```


### [2026-09-14T01:09:09.723Z] TOOL RESULT

```
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

CHEUNG null

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


### [2026-09-14T01:09:09.774Z] TOOL RESULT

```
634:ap. araika- Teind'; aw. ara^ka-.
637:Form könnte andernfalls natürlich auch äraika- gelesen
5684:642. reg \Sand' (AM. 242 Zeile 9), rez (Käs. Z. ryz).
```


## [2026-09-14T01:09:14.623Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['HRN','HUB','PHD','ISS','BQT','KLN']:\n    print('=====',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\""
}
```


## [2026-09-14T01:09:15.437Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /642\\. reg/ {print NR}' HRN.txt"
}
```


### [2026-09-14T01:09:15.757Z] TOOL RESULT

```
===== HRN
{
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
 "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
}
===== HUB
{
 "title": "H. Hübschmann, Persische Studien, Strassburg 1895",
 "edition_found": "1895 (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/persischestudie00hbgoog",
 "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt",
 "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.",
 "notes": "Built from djvu.xml (no hocr); OCR quality moderate.",
 "cites": "page number of Hübschmann, Persische Studien (1895)"
}
===== PHD
{
 "title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971",
 "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-concise-pahlavi-dictionary",
 "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).",
 "notes": "",
 "cites": "page number of MacKenzie, A Concise Pahlavi Dictionary (1971)"
}
===== ISS
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
===== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
```


### [2026-09-14T01:09:16.803Z] TOOL RESULT

```
164
```


## [2026-09-14T01:09:20.816Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==164' HRN.txt | sed -n '1,60p'"
}
```


### [2026-09-14T01:09:22.011Z] TOOL RESULT

```
— 142 —
639. rlden *kacken', Praes. rii/^em, rtsten, rtm *), rime.
aw. l/^raf-, avi dim irita *kackt darauf (vd. 5, 1);
phlv. }*ttan, reman, remamh; ai. l/^re-, riyäti *frei
lassen, laufen lassen .
kurd. rltin *kacken'; oss. d. liyun, t. Hin (168); bei.
rii/ay (315).
610. vis (*m) *Bart', rese *Haai'\
aw. ra^sa- zweifelhaft (Hörn, ZDMG. 43, 33,
Jackson, Amer. Journ. of Philology, Vol. XI, 88);
phlv. res *Bart' (AV.), resak *Haar (vd. 7 (28) Gl).
kurd. ruh, ri *Bart'; afy. ^Ira (aus *riSa) bezw.
^ire; oss. d. re/e, t. rt/T (213); wa/. reyis, i^itr. ri/is,
rikis, minj. yarzd,
Vergl. Bartholomae, Studien II, 54, 55.
641. veH') 'Wunde, Geschwür, rese, resTde,
aw. ra^sah' 'Wunde', [/^rars-, ra^ayat 'verwunden ;
phlv. res, resiian ; ai. l^reS-, resat^ reHyati *versehrt
werden ; beschädigen'.
LW. kurd. m; bei. res 'Wunde' (225).
642. reg \Sand' (AM. 242 Zeile 9), rez (Käs. Z. ryz).
LW. (?) kurd. rik^ rig; afy. reg; bei. rek^ n.
re/ (317).
Bartholomae (ZDMG. 46, 301 No. XIX) stellt die
iranischen Worte zu ai. sikata- 'Sand', während sie
Geiger an aw. l/^rafx- (No. 638) anschliessen wollte.
643. rew 'Betrug, List* (Sahn. II, 735 Vers 939), rewäs,
reimen, rlmen 'betrügerisch'^).
ai. rip' 'Betrug* (l/"rep-, lep- 'anschmieren').
Vergl. fireften (No. 829).
») *liem', LW. kurd. afy. rim *Eiter*, bei rgm 'Eiter* (224), wa/.
rim *Schmutz\
2) Der Mftihülvokul ist bezeichnet AM. 231 Zeile 3.
*) *Repmetiy vergl. * Verlorenes Sprachgut* No. 83. Die Volks-
otyraologie macht das Wort zu einer Verkürzung von Ahrlmen. Da die
Bedeutung 'sclimutzig, unrein* dem Worte nach der Überlieferung nicht
zukommt, so wird man os nicht zu phlv. reman^ np. rim (oben No. 039)
zi(5licn dürfen.
```


## [2026-09-14T01:09:22.083Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^rēg\\|^reg \\|rēg \" PHD.txt | head -20; echo ---; awk 'BEGIN{RS=\"\\f\"} NR==95' PHD.txt | sed -n '1,60p'"
}
```


### [2026-09-14T01:09:23.259Z] TOOL RESULT

```
4962:\ 4» rāvīg PA) rāzkirrēg So labag PS lābakkar AS ee lābakkarīh rādīh
---
yng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A b
```


## [2026-09-14T01:09:30.682Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rēg\\|reg \\[\" PHD.txt | head -20; echo \"=== PHD_mackenzie\"; grep -n \"rēg\\|rēg \" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-14T01:09:30.747Z] TOOL RESULT

```
854:artisan hutuxš, kirrēg.
856:arts kirrēgīh.
1111:builder rāz-kirrēg.
1970:Slight parwāz, wāzišn ; (escape) wirēg.
2621:light (n.) payrēg, rošn(ih).
3194:power abzār, amāwandīh, nērēg, 07, stahm, tuwān, zor.
3630:shine brāzīdan, drafšīdan, frēgīh- istan, tāftan, (tābīdan).
3682:skill abzar, hunar, hunarāwandīh, kārāgāhih, kirrēgih, nēzūmānīh.
3683:skilled ` abzarómand, frahixtag, hunarāwand, hunarómand, kār- āgāh, kirrēg.
4962:\ 4» rāvīg PA) rāzkirrēg So labag PS lābakkar AS ee lābakkarīh rādīh
=== PHD_mackenzie
```


## [2026-09-14T01:09:31.751Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 95 96 97; do echo \"--- NR=$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' PHD.txt | head -c 600; echo; done"
}
```


### [2026-09-14T01:09:32.831Z] TOOL RESULT

```
--- NR=95
yng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pē
--- NR=96
r-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
puštag 70 ranjfénidan
puštaģ [pwstk'] load (carried on the back). puštībān [pwštykp”n! | N ~] supporter, bodyguard. ~ЛЬ : support, protection.
R
rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies
--- NR=97
idan, ranjén- [/ncyn-ytn'] trouble.
ranjwar 71 rëš
ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] e
```


## [2026-09-14T01:09:37.426Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 98 99 100; do echo \"--- NR=$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' PHD.txt | head -c 1500; echo; done"
}
```


### [2026-09-14T01:09:39.389Z] TOOL RESULT

```
--- NR=98
N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
résag 72 rózig
rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | 
--- NR=99
ighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
rūz-šabān 73 sān
rdz-Saban [YWM, lwc sp’n' | N šabān(a)rēz] day and night. rózwürag [/zvcw?/k!] daily, everyday. róz-ward [/wcwlt'] changeable, fickle. rubüdan, rubāy- [/pwtn!, lp d- | M rbwdn, rb’y-, N ~] snatch, rob. rüdan, rün- [/win', lwn- | (N rūda)] pluck, pull out. rürag [/wlk'] medicinal plant, herb. rustan, rdy- [lwstn', lwd- | M rwst, rwy-, N ~] grow. ~išn: growth. ruwān [lwbn'! | M rwn, N ~] soul. ~ig [-yk! | N ~7] spiritual. ruzd [lwzd | M rwzd, N таза] greedy. ~ih : greed.
sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo | M sd, N ~] hundred. Sadwés [stwys | M sdwys] a star (Fomalhaut ?). ваб [KLBA < A klb | N ~] dog. Zeag [sk!] stone. sag [PR | P g] number. sagén [skyn! | M sygyn] stony. sagr [sg] | N sēr] sated, satiate. «ЛЬ: satiety. sahig [shyk' | M shyg, N sahi] worthy. ~th : worthiness. sahistan, sah- [MDMEN-stn' = A mdmh, V dmh | (M shyd, s‘y-)] seem; seem proper. ~išn: satisfaction. sahm [skm | = M, N ~] terror. ~gin [-k(y)n! | N —gin] terrible. ~genith : terribleness. sahög [shwk'] hare. sāk [s | (N sdw)] tribute. sal [SN T < A fnt | (M sr), N <] year. -sálag [SN TA, oli | N -sala] . . . -years-old. ~ih: age (of... years). salar [srd?] | M ffr, s’r’r, N ~] leader, master. ^h : authority. salwar Leikofl perennial. sāmān [?mn! | = M, N ~] limit, boundary. —Óómand [-’wmnd
--- NR=100
an. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) dan
```


## [2026-09-14T01:09:54.068Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==79' HUB.txt | head -c 2500; echo; echo \"=== grep reg/rig in HUB\"; grep -n \"642\\.\\|rig .Sand\\|reg .Sand\" HUB.txt | head"
}
```


### [2026-09-14T01:09:55.230Z] TOOL RESULT

```
- 68 —
633. Lies runt, rUma fwegen des folgenden m).
634. Dazu sTvend. rTndsk garance' Journ. asiat. 1893,
p. 260.
635. Hier fehlt arm. LW. aroir Messing (aus arsacid. *roJ)
ZDMG. 36, 133. Als Bedeutung von roi giebt Vullers
an: *aes vel stannum fusum', Zenker: *6elbguss,
Glockenspeise', sepid rui *Zinn , Polak, Persien II, 177,
Kosen, Np. Sprachf. 35: *Zink*.
637. Np. rahr = phi. raa^ 'Diener gehort nicht zu ap.
ras.
639. Im Neupers. hat rim immer rim gelaiitet; nur die
Pehleviform war rSm = bal. rem.
640. Da zd. ra^a-, wie jetzt allgemein angenommen wird,
nicht *Bart* heisst (sondern etwa *Spalt' Riss?), so
bleibt die Etymologie dunkel. Nach den LW. bal. rfi,
afgh. ris *Bart' sowie nach echt afgh. ^Ira aus rJia
zu urtheilen, scheint ris die urspr. np. Form, rtso^ die
iranische gewesen zu sein.
642. Np. reg *Sand' = bal. rek = ap. ^rdika- gehOrt gewiss
nicht zu skr. sikata-. Die Form rez in der Bedeutung
*Sand' (Shukovski, Materialy I, p. 137) finde ich bei
Vullers nicht.
645. Np. »dq *das Junge eines Thieres* (aus *05y) = arm.
^'ag (= dzag) *das Junge eines Vogels' = syr. n:1i
junges Huhn'.
647. Unsicher wegen der Bedeutung.
648. Afgh. eor alt (mit r) aus iran. ^2arta-.
648 ***" Im Pehlevi ist natiirlich zdnuk fiir jdnuk zu lesen.
Kurdisch auch a^ndh *Knie' (Socin, kurd. Samml.
II, 281).
649. Ftir zd. jfafra- (= arisch *j[apra-) erscheint (nach KZ.
31, 266) in der Composition die Form jfaiwi- (zd. jfaitm-
vafra- mit tiefem Schnee) = arisch ^jahhir-, zu der skr.
gabhlrd', gambhird- gehort. Das Iranische setzt also
die Wurzeln g^ap und g^abh voraus. Vgl. Nr. 663.

=== grep reg/rig in HUB
2383:642. Np. reg *Sand' = bal. rek = ap. ^rdika- gehOrt gewiss
```


## [2026-09-14T01:09:55.639Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sikatā\\|sikata\" BRT.txt | head -10; echo \"=== BRT raika\"; grep -n -i \"raēka\\|ra\\^ka\\|araika\" BRT.txt | head -20"
}
```


### [2026-09-14T01:09:55.828Z] TOOL RESULT

```
=== BRT raika
```


## [2026-09-14T01:10:10.480Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT Sand\"; grep -n \"'Sand'\\|.Sand.$\" BRT.txt | head -20; echo \"=== CHEUNG raup\"; grep -n -i \"raup\\|\\*raup\\|rufta\\|roftan\" CHEUNG.txt | head -30"
}
```


### [2026-09-14T01:10:11.698Z] TOOL RESULT

```
=== BRT Sand
16346:1  noch  ksl.  priäa  'Sand'  und  arm.  pHiS;  dain Pedersen  IF.  j.  47,  Hbm.  AGr.  /.  501.  — Pü. :  xai.  —  >>  Scheint,  wenn  richtig  bezeagt
30043:'Zum  V,  'haii-.  —  Ut.  liicas  (für  für* ;  Pauu KZ.  iS.  17)»;  ai.  vgl.  liialS.  t.  'Sand'(?>  — Pu.:  AuSi.  —  ")  Neubild,  zum  NSm.  iiiiü nach  j.  •vüvdifAim  zu  g.  vTdus  ($j3o  No.  $), begünstigt  durch  das  vorausgehende  Wort; wegen  i  s.  ^  S.  —  ')  Hds.  Auü;  aber  Pü. Aust.  —  3)  Anders  BcM.  Grdr.  />.  53I.
=== CHEUNG raup
8676:-git-/gin, Soi gir-/a-ir- ‘to take, seize’ || (+ *pati-) NP paóiruftar/paóir- ‘to receive, 
13248:*Hraup 195 
13280:*Hraup ‘to tear, break; to suffer from pain’ 
13302:see *raup. = EWAia II: 469 f., 482 
13304:© To the root *raup a number of forms with a wide range of meanings has been 
13384:<-r->, also in MMP hrwb- ‘to collect, gather; receive’ (< *ham-raup). Incorrect 
14684:similar Skt. connection is semantically implausible (*raup?). The root *jaup may be 
16615:the Pth. verb ywb- ‘to suffer, complaint, lament’ (*raup'), which is semantically not 
20938:*raup 1 319 
20981:*raup! ‘to take away, up, rob, cueillir 
21001:320 *raup2 
21014:Ó In view of the semantic similarity, the root *raup? is perhaps connected with Skt. 
21015:yop. The initial r- of *raup^ should therefore be regarded secondary and may have 
21025:*raup2 ‘to sweep’ 
21045:*NWIR: NP röb-/ruftan ‘to sweep, dust’, Bal. rupt/röp- ‘to sweep up’, Kurd. (Abd.) ti- 
21058:This root is probably originally identical to *raup', which has developed a more 
23977:may be explained differently, v. *raup, *jaup?. 
24932:*MIDDLE PERSIAN: BMP tlwptk /truftag/ ‘stolen’ (MacKenzie, Pahlavi: 84) 
35637:tlwptk /truftag/, 383 
41233:paóiruftan/paóir-, 121 
41421:röb-/ruftan, 320 
55795:*braj,*(H)raud, *Hraup, 
56034:(s.v.), *raup! (s.v.), *skar 
57649:*HuarH, *raup! 
58093:*baid (s.v.), *Hraup, *rais, 
58105:*raup’, *star 
58116:*raup', *zaiH 
58136:*Hraup, *xrau
```


## [2026-09-14T01:10:11.788Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD rwp\"; grep -n \"rwp\" SOD_pages.txt | head -20; echo \"=== HRN roftan\"; grep -n -i \"ruften\\|rüften\\|roften\\|rob\\b\" HRN.txt | head -20"
}
```


### [2026-09-14T01:10:11.860Z] TOOL RESULT

```
=== SOD rwp
8780:       TSP 8.189-, >sk}np\ TSP 2.1150; Wnpvv, VJ n p91,             1751 >skrwp B                   (J>jJlt.)j^\^iKjF^
17575:             good looking                                             4876 krwpr'n M                                    jlijA*
20709:    5918 nyrwps- S                  0-^»->^j> <ooiojjii                 nayuPawe
23762:6986 pr'nyt- M                             O^^U^Ij                     parop ? ©<*pari-Iupa-raupa- =*rwp-
26237:        ace. -w; ob. -y; abl. ->; pi. -/>; ob. pi. n. -tyy     7819 ptr'wpCw)     S =» ptrwp
26299:       C2«51R 6: BSTii 885.6                                         7841 ptrwp M                   JL^iy>i**\s<£sl>\&>ti*.\
28328:           him"; rtywr "and up", rtypr "and in"; STii                   8554 rwpcyk1 B                                    J?1 J**
28388:8553 rwp B, M     ({^ tj^)(ok>ujj*£^^ -{j)o\**
28404:        1936, 584; C2 gloss. 23R4, rwdny, 91R8,                       8580 rwp— B, C                   o^,jj <c*3j i o^>- <o-^^
28410:                                                                      8581 rwps(h)   B, M                                   a\>3j
28424:                                                if 11 'iJtJ?         8582 rwpsy'kh S
36485:          STii 1.27, 6.40; C2, 52V 5; TSP 5.34, 75, 79; S W,    11277 zyrwps-     B                    jjiUzil^l^ <jjiiJuL
=== HRN roftan
2832:290. peölruften 'empfangen, annehmen', jüd.-pers. J nenne,
4962:552. durust 'rauh, grob, stark, durustt,
5431:riibäyende ; ruften 'fegen , gäten', Praes. röb-em,
5564:626. robäh *Fuchs'.
5965:676. zös 'zornig, grob*.
6267:ai. sthürd- 'dick, breit\ sthülä- 'grob, dick, gross,
6370:g. aurob.
13534:ruften 608.
18715:rob 728.
```


## [2026-09-14T01:10:16.507Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20975,21065p' CHEUNG.txt"
}
```


### [2026-09-14T01:10:16.561Z] TOOL RESULT

```
*PIE — = LIV: — | Pok.: 

*REFERENCES: BBB: 566; DKS: 369 


*raup! ‘to take away, up, rob, cueillir 

*MIDDLE PERSIAN: BMP Iwpk /robag/, BMP Iwp /rob/ ‘pillage, plundering’ || (+ 
*ham-) MMP hrwb- ‘to collect, gather; receive’. 0 The cluster *-mr- in MMP hrwb- 
has been assimilated: MMP -rr- <-r->. > DMMPP: 185a 

(+ *ham-) Pres.: IND. 3sg. MMP hrwbyd, SUBJ. 152. MMP hrwb’’n, 2р1. MMP hrwb’d-, IMPV. 25р. 
MMP hrwb; Partic.: perf. pass. I MMP hrwpt, hrwpt, П MMP "hrwbyhyst 

*KHOTANESE: rrv- ‘to remove, peel off? || (+ *ш-) LKh. bur(r)v- (burtivafi-) ‘to 
destroy’ — SGS: 117, 101 

*SOGDIAN: BSogd. гур ‘to gather’, CSogd. гур ‘Өғрібо’, MSogd. гур ‘to harvest? 
Pres.: IND. dur. 1sg. CSogd. rwpmsq, 2sg. CSogd. гуру ‘OepiCetc’, SUBJ. 3р1. MSogd. "rwp’ndt, Impf.: 
IND. 3sg. BSogd. rwp’ 

*CHORESMIAN: rwby- ‘to rob; take away [of horse]’, ? m/rwBY- ‘to take with one’s 
fingertips’ > Samadi: 173 f. 


320 *raup2 


*NWIR: NP rubodan/rubay- ‘to rob, seize, carry off; to withdraw from sight’, (opp) 
rubödah ‘seized, plundered, robbed’, Bal. rupt/röp- ‘to collect’, Gz. rübä-/rübä, ? 
Kurd. fifanin, бгапіп, Awrom. arfáy/-rfán- ‘to snatch’, Gur. (Kand.) rifanin ‘to rob’ 
|| (+ *ш-) Kurd. (Kurm.) guramgure-, gurö-, (Sor.) gurun/guru- ‘to skin, remove 
(skin)’ 

*NEIR: Yghn. rup-, rub-/rüpta, rübda ‘to harvest’ 

*SANSKRIT: ? yop ‘to wipe out, efface, remove, erase’ (RV+) = EWAia II: 420 

Ó In view of the semantic similarity, the root *raup? is perhaps connected with Skt. 
yop. The initial r- of *raup^ should therefore be regarded secondary and may have 
been imported from (for instance) *rauH. As for an IE provenance, Skt. yop is 
connected to Gr. үзү ‘vulture’, which is analysed as a compound *g”u-jup- ‘taking 


away cows’ by Thieme 1954: 569, n. 2, but this analysis remains rather conjectural. 
*REFERENCES: KPF II: 199; Andreev — PeSéereva: 316a; MacKenzie 1966: 88; DKS: 367a; 298a f.; WIM 
II/1: 82; Kümmel 2000: 410 f.; Cabolov 2001: 405 


*raup2 ‘to sweep’ 
*MIDDLE PERSIAN: MMP “rwb-, BMP Iwp- /röb-/ ‘to rub, sweep’ || (+ *ui-) MMP 


wrwb- ‘to sweep down, away’ = DMMPP: 297b, 345b 

Inf.: MMP *rwptn || (+ *ui-) Pass.: pres. IND. 35р. wyrwbyhyd; Inf.: MMP wrwptn 

*PARTHIAN: rwb- ‘to sweep’ (Sundermann 1997: 62, line 40k). Ф On rwbysn 
‘change, Wandel (Mir. Man. III: 875) see *jaup^. > Ghilain: 65 f. | DMMPP: 297b 
Pres.: IND. 35р. *rwbyd {hapax} 

*KHOTANESE: (+ *4-) OKh. arüh- (ärau-) ‘to move, shake’ = SGS: 11 

*SOGDIAN: (+ *upa-/apa-/pari-) BSogd. pr’wp- ‘to sweep’ 

Pres.: SUBJ. 35р. pr’wp’t (Dhy. 1); Inf.: BSogd. pr’wp’y (Dhy. 68) 

*CHORESMIAN: rfš (f.) ‘broom’ 

*NWIR: NP röb-/ruftan ‘to sweep, dust’, Bal. rupt/röp- ‘to sweep up’, Kurd. (Abd.) ti- 
ruf- (supplet. inf. mestén < *Hmarz), Anar. ha-..-ruft/ (impv.) ha-ru, Gz. rön-/ruft, 
rona, Kesh. rutmiin/a-rov-, Khuns. rü-/ruft, Qohr. rüten (supplet. a-reg-, impv. bä- 
rug < *rauj'), Sang. hö-ründen/hö-rün-, Shamerz. be-rüten/rüm-, Von. ruften/er-rü-, 
Zef. bo-ruft/rov- ‘to sweep, wipe’ || (+ *ui-a-) NP jaru ‘broom’ (dial. ?) 

*NEIR: Sh. rüb-/rüvd, Rosh. rub-/rubt ‘to sweep up, shovel’, Pash. rabaj, Bart. rafc 
(Ё) ‘broom’, Yzgh. гаі ‘broom; name of a plant’, Yzgh. rabag ‘wooden shovel’, 
Sangl. ref ‘broom’, Yi. rufó ‘small, soft broom’, M. réfiko ‘mill-broom’, Wa. ropk 
‘trash, garbage’ || (+ *fra-) Yi. faru ‘mill-broom’ 

*MISC: Par. rüy-/rüt ‘to sweep’ 

This root is probably originally identical to *raup', which has developed a more 
specialised meaning ‘to sweep’. 


*rauxsn 321 


*REFERENCES: Zhukovski I: 134a f.; Zhukovskij II: 234b f.; Ivanow 1926: 421; IIFL I: 285b; IIFL II:
```


## [2026-09-14T01:10:17.799Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5420,5445p' HRN.txt; echo \"=== which page\"; awk 'BEGIN{RS=\"\\f\"} /608\\. ruften|ruften .fegen/ {print NR}' HRN.txt"
}
```


### [2026-09-14T01:10:18.898Z] TOOL RESULT

```
Phlv. rayinTtan, räyma, räyln(i)sn, räymitärih (Men.),
jüd.-pers. pJN^NI (Is. 63, 17) sind nicht klar.
607. rah^ ras ^), reh *Weg ; espyes.
skr. vergl. rathyd- Xandstrasse' (spät) 2); phlv. reis,
aspjräs; af/. lär^),
LW. kurd. rl; bei. ra, n. rah (219); af/. räh;
arm. rah.
Gehört hierher auch np. reste^i (phlv. rastan, Men.),
Praes. reh-em^ rehlden u. s. w. 'befreit werden, ent-
kommen', wörtl. 'sich auf den Weg machen'?**)
608. rubüden 'wegnehmen, rauben', Praes. rubay-em,
riibäyende ; ruften 'fegen , gäten', Praes. röb-em,
ai. V^löp' (älter röp-) 'zerbrechen, packen, plündern,
rauben''^); phlv. röp 'Raub' (AV.-GL), kah]rupäl 'Bern-
stein (Säy. näsay. II, 115); got. biyaubön 'berauben'.
bei. röpcifj 'fegen, kehren' (329).
ö hat noch Kää. Z. böröw (Impt.), börowön (Aor.),
rowon (Praes.).
np. rubäyem geht auf älteres *rupäyati zurück.
^) BQ. Rückert bei do Lagarde, Ges. Abh. 51, Note l.
^) Aw. hizvö raiHm (y. 50, 6) beisst iiacb Bartholomae,
KZ. 28, 34 *Lenker der Zunge*, siehe aber Geldncr, KZ 28, 259.
') Aus *ral (Trunipp, Graramar of the Tastö § 7); //är,
Darmesteter, Ch. pop., p. CLXXV, Note 2.
*) AM. 183 Zeile 1 hat aUerdings biriheS,
^) Aw. urüpay^intl (y. 43, lÜJ muss als unsicher bei Seite ge-r
=== which page
157
```


## [2026-09-14T01:10:36.449Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== DKS rrū / raup\"; grep -n \"raup\\|rrū-\\|rrūv\\|rrv-\" ISS_alt_DKS.txt | head -30"
}
```


### [2026-09-14T01:10:36.513Z] TOOL RESULT

```
=== DKS rrū / raup
880:&ürüva ' refuge", ш 139v3 Ra ne mä ne ttrāyākä пе ārūvo hará, BS G37, 34v2 farapam na ca me trünam, ‘so that there is not saviour for me, not refuge’; SuvP. 62v4 hamane aysá ttyüm ttründ ārūva hastama pirma ' may І become the best foremost salvation refuge for them’, BS trátü tegüm bhaveyam са saranyah saragottamah; v 671431 Illarñoa jsaman(e), da ārīūva jsaman(e) “ме go to the (Buddha) for refuge, we go to the dharma-doctrine for refuge’; later ürava, ürva; її 101-7 baiysa ärva jsümanai, dà ärva isvümanai, bisaga ürava tsümanai. From *a-raupa- or *ü-rauda- 'raised place' to raup- 'to ascend' or raud- fto rise’, see s.v. prioa-, Kroraina pirova ' fortress’,
881:&rüh- ‘to move’, participle arotta-, V 338, 62r4 ksei padya Āroita 'shook six ways’, BS G 37, 58r6 sad-viharam prakampitah; у 87vr hvamdà arautta; Z 2:103 arüháte hamtsa ggaryau jsa; Z 27235 nä sü vina pracai másta ürühdte te $fandà balysa; Z 2:66 ürottu yanīndä; noun SuvO. 24r4 anürühà и ayicä ‘inactive and not busy’, BS nisceg]a niroyaparaš ca, Tib. g-yo-ba med-¿in byed-pa med, with ауіса-, BS akrtya-. See cognates s.v. rrühàrd, rauf- beside raup-, see harautta-.
1240:auügyo jsa ' from branches’, Z 245 huska vara Вапћуа ku rrūva aungyo jsa äre pacasía ' dry trees there where the guts remain attached to the branches’, From *ä-van-čä to base van- 'tree', see banltya-. Possibly to compare with Zor.P. ‘ywn’ ' part of a tree’ either *adi-oana- or *ada- vana- (adah- ' under). If the base is auñgya-, but possible is also base auñga-, from *a-vanaka,
1381:kalj- ‘to strike’, v 78, 149r4 tmu dátinau küsu капа 'to-day they beat the drum of the dharma-doctrine', Tib. de &hos-kyi тпа čhen-po rdum-bar hgyur-te; M 35772 kūsi kajindá 'they beat the drum’; Z r483 Raljdndá; noun SuvP. 6irr Rejáma. . .Кйѕӣ, BS paráhananta dundubhim. Participle Ariya-, п 67:45 parasanai baysve krriye ‘with axe his arms were struck'; with negative V 145, 33V5 akrriya; Z 13:114 cu vara binàiia askusta adaunda stana актуа what music there not plucked, not blown, not struck’, = BS арлар йа dundubhayah. Incohative krīs-, SuvP, 6rrr Rrrisáme beda ' at time of beating’, BS aofya- тйпа-. See Rargaka- = haraka-, uskalj-, nasharga-, nagkalj-. From kark- 'to strike’, as in the name of the rapacious birds of prey eagle and vulture, Ау, kahrkāsa-, Zor.P. harhüs, Püzand kargas, Rrgaz, N.Pers. kargas, Yidya karyez, haryəs, Sangl&&t koryöš; with č, Sogd. črks, Oss, cärgäs. The suffix -ara- is used for bird and beast, as O.Ind. lopaía-, Greek dcm, Oss. D. robas, N.Pers. rübüh Чох’, Khotan Saka rrūväsa- ‘jackal’; and murása- ‘peacock’. Other verbs ending in -/j- are tcabalj-, ahalj-, nihalj-, haspalj-.
2465:fiauysira- ‘devoted, intimate, loving’, 11 75:59 bastá hübastá hvaramdai fiauysirà grathä ‘bound, well-bound the right hand, an intimate knot’; ПІ тогы auda mara vai sa iiauysaira hamaunai ‘ир to here indeed may I be intimate for him"; v 384, 911-2 ysaja astyd ñauysera bīyse hvandinai rana 'I hold firmly as an intimate adherent, the jewel of men’; v 66:t4-5 dutakà famysird tsumam(ca uy hharüka ksama ‘іс pleases the daughters, becoming intimate, and being loving (?)'; v 66-8a ñämysirä-vāda pūra du(ra) ‘lovingly nourished sons, daughters’; п 82:58 ñāysaira- vāda vvūvayau drūpadą 'Drüpada lovingly reared, the princess (so vvūvayau from *baga-yauna-)'; =11 79'12 fiamysaira-vüda vūvąyu dryapadá (-ya- for -ñ-); Drüpada from BS Draupadi with secondary -d-; V 243:34 fümysaira diryai khvà jsa па тай 'I have held intimately so that I shall not part from you’ (-@ = -й). If the older form is ñauys-, the base may be "ni-yauz- ‘Бе excited in love or intimacy’; if the older is #ays- the base could be *ni-üz- ' to tie tight’, For yaus- see jih- ' to be enamoured’ from *yauxi-.
3306:dramph-, drauph- 'exert', Sid. 104v3 drümphame jsa BS vyayama-, Tib. bréal, Sid. тут drrauphüme, BS vyayama-, Tib. rcol phod-pa ‘able to exert oneself’. Base dar- ‘hold together’, see also aysdraphai ‘squatting’, hence dramf-: draf- YE *dhr-embh-, IE Pok. 252-4 dher- 'hold', with *drauf- < *drümf-.
4796:sima haişțai hira 'what is the contemptible seizing, grasping, may I not really go to the karma-acts'; K 5162-4 cu prrürva satvüm bünda, dükha зата hast mara...niyümddü yinime "what are graspings upon the beings, woes, sorrows here..., may I quieten them’. From *pará-ü-raupa-, base raup- 'rob, seize'; here prrüril, plur. prrarva dyadic with BS ahara- ‘grasping’. See base raup-, s.v. rrüv-, buriiu- ‘remove’.
4806:prüva- 'fort, розі’, nom. sing. ргӣ, plur. prüva, IV 3v5 mara hamdira prü haurüii 'to be delivered here at the Inner Post’, її 17, sato hamdara prrü tsue 'he went to the Inner Post’; гу 31a2 hadira prrüvasta о the Inner Post’, v 199b.4 леѓса ргӣойзја ‘to the Outer Post’; plural, v 26, {дуз o balsanu, o ciyünu, ci và ksirá prüva ‘or stüpa- monuments or caitya-shrines or what are forts of the сіу’; K 99:255 bisa prriua ysīmā ' houses, forts, covered posts (*zarmya-)'. With -aka-, K 37:125 prrīūvaki ji pa-sse vari уйй samauita 'soo guardsmen yaksa-golbins there appointed’; prizuaa-, K 2110-11 prruvà lista varae pa- sai yaksa ѕатаийа ‘Һе comes to the guardsmen there, 500 appointed yaksa-goblins', parallel to Divyávadaüna 451 11 gulmakam, 4571 gulmaka-sthànam ' guards! post’, Tib. gcan-pahi gnas ‘place of men of the narrow pass'; BS Mahavyutpatti 3803 gaulmika-h, Tib. la-géan-pa. Kroraina lw ріғоба, pirova, piro from older form of Зака prüva. From .*pati-raupa- 'raised place’, Sogd. Man. pirwp, ptr'wpw ‘fort’? (W. B. Henning, BBB p. 93), to base raup-:rup- 'to raise’. For O.Ind. RV тр ‘raised place', see Liebenthal Festschrift, Sino-Indian Studies 5, 1957, 9-10. The same base is in йейоа- ‘refuge’, BS Хагапа-. Khotan Saka -üva- is ambivalent, here either raupa- or rauda- would give -rzva-, older -róva-, the Sogdian may decide. For rauda-, note Baloéi 708 ‘steep bank’, N.Pers. ka-rüd 'well with steep bank’, O.Ind. ródhas- ‘bank’, Possibly Oss. D. buru, I. bru, буги, gen. sing. byrujy ‘enclosure’, whence Inguš bru for 'Vladi- kavkaz’, belongs here with either *abi-raupa- or b- « -. See BSOAS 13, 1951, 924-5 for priva-. For ‘Inner Fort’ note the Ičan Kala of Khiva.
5340:bilga- 'kidney', Z 20:55 spuljei rrūva spi jatárra bilga ysërä 'spleen, intestines, lungs, liver, kidneys, heart'; Sid. 1553 bimga-bamdanvà vind 'pains in the bands of the kidneys’, BS Ruksi-, Tib. mkhal-rked na-ba. Adjective, ш 89:157 bigaji pi ‘fat of kidney’. Base *vróka-, Av. varaðka-, veratka-, Yidya wulya, Waxi wultk, Zor.P. guitk *gurtah, N.Pers. gurdah, Orm. yulkak, Sangledi wolk, gul, Suyni шӣ{с, йш}, Pašto warga (pufta-warga), Kurd. bulk, Oss. D. urg, urg-fiutáj ' with fat of kidneys’, I. ürg (—1üyrg) caritive ürgoj "without kidneys’. The oldest Indian vrkkau (dual) is less archaic with -АА- «tk-, ТЕ Pok. 1157 ger-t- ‘to turn, twist’.
5491:busta 'as a garment is beaten white, so he realized the ksānti-anulomika state’ (BS. hsánti-anulomika- ' conform- able to receptivity’). From base raup- ' to sweep, carry off', *0і-ғаир- > Битӣо-, Sogd. Bud. rwp- ‘pluck’, pr'wp-, pr'rwp ‘sweep’, Chr. rwp-, M.Parth.T. рагшй-, pdrwft ‘to rout’, M. Pers. T. 'wysworwftn ‘throw in', hrwb-, hrwpt- ‘open', wrwbyhyd 'is torn away’; Zor.P. ràpet, givak-rüp 'broom', uz-, zrüpat, zruftak ‘removed’; Bal5ër ràp-, rupta ‘turn’, N.Pers. rób-, ruftan 'sweep', Yayn. гир-, rub-, rupta, rubda 'to reap’, Pašto ratodol, Wanetsi rēb-; Waxi лерд, rapk ‘sweeping’, Рагӣё rzy 'sweep'; Püzand (Мх. 2:182) zrüvaó, Parsi-Sanskrit antarnivesayati. For ‘broom’, N.Pers. fü-rüb, Orm. parawak, Pašto rëboz (*raupaci-), Yidya rufo, faru, Sangl&&i rif, Waxi drapic, dorebé, Yayn. rüpé. Parallel to Manj. 411, see kho ssiyä rrahamüna thonà pajsinde * as the garment is beaten white by the washerman'. See below rrüv-, ro-, prrarü, prrārva.
5839:brruva ‘attained’, Manj. 437 Pays(ü)sta brruva 'having reached bodhi-knowledge', if not from byüda- = byauda-, BS prapta-, possibly *abi-raup- 'rise up to' with par- ticiple *rufta-  *ruta-.
6151:müdai büjve ' being dead (mudaa-) тоо years, he revived’; K 68:202-3 tti khu mudye kidi orea nisti tas of a dead man there is no vipaka-ripening at all'; K 64, 8iv4 müdvü basta ‘bound in dead bodies’; v 188, 7524 mudána hamamgga “like one dead", BS suptau mrta-samau ' asleep, like a dead one’. Adjectives, mudīña-, mudariia-, Z 2744 cile. . -mudifii ' garments of the dead’; Z 2:48 rrūva mudaiña ' ма o£ the dead’. See cognates, s.v. тат-.
6651:rrüta- ‘intestines’, Bid. i21r4 rrutüm jsa, Tib. rgyu-ma; K 18:216, K 26:142 rrūva, К. 35:87 riva, parallel Divya- vadüna 44730 antrüni; Z 2:25 rrūva, Z 20°58 spuljer rrüva ил jatürrà 'spleen, intestines, lungs, livers’. From rauta-, Av. игибшап-, Zor.P. rüt, rütik, N.Pers. rüdah,
6668:rrüv-, rru- ‘remove’, Z 7:33 пе jàta-rangá kūlaina ттоййї kará ‘the natural colour (BS jata-ranga-) is not removed by the beetle at all’. With, preverb, Manj. 411 # vasta burruai ‘clothes are beaten white’, see burūvāñi above and prrarü ' grasping’. From base raup-:rup- 'to remove, sweep away'.
6670:-rüvai 'orifice, mouth, hole', as second component, Sid. тозгт krrimga-rūvai 'anus', BS guda-, Tib. rkub; Sid. 4v3 hrrimga-rümya (loc. sing.) BS guda-, Tib. gian; Sid. 1i21v4-s Akrremga-rüvya, I 89'163 krremgá-rüyá, 1175, 93r3 Arrimga-ritya vini ‘pain in the part’; dyadic of the -rūvai, Sid. 103r1 hrrimga-rüvai hīyai ttaurá .vi tin the orifice of the part’, Tib. rkub-kha-nas. То Sogd. Bud. rwg ‘mouth’, adjective rwfčyk ‘oral’, From *rauf- to base raup-: IE Pok. 870 reup- ‘tear out’, O.Ind. ro-
6672:-rüya — rrusta- 367 pdyati ' breaks off", rúpyati ' have fracture’, ropa- ' hole”, Lit. raupai 'pock-mark', Slav. Serb. гйра 'hole, pit’, For the -f-, note also O.Pers. kaufa- ' mountain', Zor.P. köf to base ТЕ Pok. 591 Aeu-p-, with Lir. kanpas. Here too can be placed Munjàni yurv ' mourh' through *uruv-. Зее also s.v. pili-rüvi.
7084:title baga-, п 82, 58 vvitvayau drüpadq = п 79:12 vilvayum drüpadà “ће royal (princess) Drüpadi'. Hence *baga- Yauna- ‘of royal origin’ with the Indian name replacing "dropadi- (Epic Sanskrit Draupadi) with Prakrit -adi <-ай (as O.Ind. RV nadd- "reed', RV, AV nadd-, later nada- and BS лаја-; and *argada- 'enclosing Баг! > атрафа-, argala-), Ах. yaona- 'place of movement’, O.Ind. yoni- (s.v. gyūna- ' way"). For baga- O.Pers. baga- (glossed by Akkad. ilu ' god!) is Av. baya- ‘distributor’, Parsi-Sanskrit vibitaktar-, Bogd. Bud. fy- rendering BS deva-, plur. By yit, gen. plur. By'u, By'ystn ‘paradise’, ByBn'k 'altar', Byp'wr 'prince', M.Parth.T. bg, plur. bg'n, adjective bg'nyg, abstract bgyft; bgpwhr,'son of a god’; M.Pers.T. by, plur. В", adjective by'nyg, Zor.P. bg, DEM 413:9 im bay ‘this god! = his present majesty’; "Turkish Iw bág, with suffix bdgrák, as proper name (of the
8314:hambrosta- 'penetrate, approach', 3 sing. Z 5:28 kho ju ttavai пазрћапӣ hvandà thatau hà vira hambraustà ' when fever issues in a man, it swiftly penetrates upon him’; preterite, Z 5:103 trámu hà ssàya hambrosta patd balysd samu kho ju рїї ' the Sákya men so approached before the Buddha as a son does’; Z 3:109 hasta hambrostà patána balysá ‘һе approached before the Buddha’. From kam- rafš- or ham-rauff- to base rap- or raup- ‘mount’. See also brah- and priiva-.
8372:harautta 'flown away’, Z 7:46 ku sya harautta їйса pusso pūta bissá 'when the goose (siyä-, BS hamsa-) has flown away, the water altogether is fallen (subsides)'. From base raup- or ràf-, see -rota-, -rautta- (patárotta-, pürautta-, árotta-), and for ' flying! rah- in bráh-, bárüh- “Яу up'; suits better *frarüfta-, in meaning.
8527:hàrü 'raised building; citadel’, Z 22:140 bārā vdtd ütco vaicisde ' (the yaksa-goblin) sprinkles water upon the (city) buildings', parallel Chinese ‘the yahsa cleanses the city’ (see KT vr 410). From "*fraraupa- to prüva- ‘fort’, Kroraina pirova (see above), BS gulmaka-sthüna ; for raup- 'to raise', see Sogd. Man. ptrwp-, ptr'wpw 'castle, royal city’ (*pati-raupa-); and above йтїїшй- (*ü-raupa-) 'refuge'. ТЕ Pok. 684 leu- with increment leudh-, beside here leu-p- ‘rise, grow’, O.Ind. ropdyati, rohati (suppletive), RV тїр 'high place', see H. W. Bailey, W. Liebenthal Festschrift, Indo-Iranian Studies V, 1957, 9-10. Е РЕГ .
```


## [2026-09-14T01:10:37.398Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== DKS gyāg-rōb / broom\"; grep -n -i \"broom\" ISS_alt_DKS.txt | head -20"
}
```


### [2026-09-14T01:10:37.458Z] TOOL RESULT

```
=== DKS gyāg-rōb / broom
5104:Rs). From base vaxš-:uxš- tto pour out (water, or fire or dust), to moisten', Av. vaxzsyente vaxsa ' moisten with a flow’, Yašt rg:go paiti uzuxsane ‘I will gush out (with flames)’, átra-vaxs- ' under-firepriest' (either varš- ' make fire burn’ or ' make fire increase), O.Ind. u&sdti' moisten’. IE Pok. 1118 ueg"- ‘moist, moisten', O.Norse vokva, vehkyja ‘pour out (blood)'; for ‘dust’ note also Yidya parwaxié (*pari-vaxfaka-) ‘broom’. The name HWaxan, Waxi is Waxi ши ‘Wakhān’ < *vaxiu-. For 'moisten" and 'flow', note O.Ind. usad- (3 sing. undtti) beside Armen. get (gen. plur. getoc', getic') 'river', to IE Pok. 78-80 aued-. 'The base Ау. vas- is in meaning unsuitable for bassa-. For the forms of the name Vaksu, see BSOAS 13, 1950, 402.
5491:busta 'as a garment is beaten white, so he realized the ksānti-anulomika state’ (BS. hsánti-anulomika- ' conform- able to receptivity’). From base raup- ' to sweep, carry off', *0і-ғаир- > Битӣо-, Sogd. Bud. rwp- ‘pluck’, pr'wp-, pr'rwp ‘sweep’, Chr. rwp-, M.Parth.T. рагшй-, pdrwft ‘to rout’, M. Pers. T. 'wysworwftn ‘throw in', hrwb-, hrwpt- ‘open', wrwbyhyd 'is torn away’; Zor.P. ràpet, givak-rüp 'broom', uz-, zrüpat, zruftak ‘removed’; Bal5ër ràp-, rupta ‘turn’, N.Pers. rób-, ruftan 'sweep', Yayn. гир-, rub-, rupta, rubda 'to reap’, Pašto ratodol, Wanetsi rēb-; Waxi лерд, rapk ‘sweeping’, Рагӣё rzy 'sweep'; Püzand (Мх. 2:182) zrüvaó, Parsi-Sanskrit antarnivesayati. For ‘broom’, N.Pers. fü-rüb, Orm. parawak, Pašto rëboz (*raupaci-), Yidya rufo, faru, Sangl&&i rif, Waxi drapic, dorebé, Yayn. rüpé. Parallel to Manj. 411, see kho ssiyä rrahamüna thonà pajsinde * as the garment is beaten white by the washerman'. See below rrüv-, ro-, prrarü, prrārva.
```


## [2026-09-14T01:11:20.336Z] TOOL CALL #22: Bash

```json
{
 "command": "ls site/pages/415.jpg 2>/dev/null; pdftoppm -f 415 -l 415 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg415 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg415.png"
}
```


## [2026-09-14T01:11:21.230Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==658' KLN_1966.txt | grep -n -i \"rabbi\\|rab\" | head -30"
}
```


### [2026-09-14T01:11:22.488Z] TOOL RESULT

```
site/pages/415.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 73449 Sep 13 21:11 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg415.png
```


### [2026-09-14T01:11:23.738Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:11:25.951Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^rabbi,\" KLN_1966.txt; grep -n \"^rabbi,\" KLN_1971.txt"
}
```


### [2026-09-14T01:11:26.034Z] TOOL RESULT

```
198889:rabbi, n. — Late L., fr. Gk. fr. Mishnaic
```


## [2026-09-14T01:11:27.156Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg415.png"
}
```


### [2026-09-14T01:11:27.959Z] TOOL RESULT

```

```


## [2026-09-14T01:11:27.942Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:11:38.734Z] TOOL CALL #26: Bash

```json
{
 "command": "grep -ho \"Indo-Sc[a-z]*\\|Indo-Sch[a-z]*\" data/extracted/batch/*.json | sort | uniq -c"
}
```


### [2026-09-14T01:11:38.813Z] TOOL RESULT

```
     13 Indo-Schythian
```


## [2026-09-14T01:11:39.532Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '198880,198900p' KLN_1966.txt"
}
```


### [2026-09-14T01:11:39.618Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:11:44.974Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -Hn \"^rabbi,\" KLN_1966.txt KLN_1971.txt; echo \"---1971 context\"; sed -n '198885,198905p' KLN_1971.txt"
}
```


### [2026-09-14T01:11:45.148Z] TOOL RESULT

```
KLN_1971.txt:198889:rabbi, n. — Late L., fr. Gk. fr. Mishnaic 
---1971 context
battre , ‘to beat back’. See rebate, v. 

Derivative: rabbet , tr. v. 

rabbi, n. — Late L., fr. Gk. fr. Mishnaic 

Heb. rabbi , ‘my master’, title of respect, formed 
with -f, pronom. suff. of the 1st person in the 
singular, fr. rabh , ‘chief, master, teacher’, which 
derives fr. Heb. rabh , ‘much, many, great’, from 
stem r-b-b, ‘to be great or numerous’, whence 
also robh, ‘multitude, abundance, greatness’, 
r 6 bhabha h , ‘multitude, ten thousand, myriad’, 
ribbo , ‘ten thousand, myriad’, Heb. rabh is rel. 
to Aram.-Syr. rabh, ‘great; chief, master, teach- 
er’, Akkad. rab, ‘chief, captain’, Arab, rabba, 
‘was great or dense’, rabb, ‘master’, Ethiop. 
rababa , ‘it spread’. Cp. rabban, the second word 
in Ahabah Rabba and the first element in 
Jeroboam, Rabmag and Rabshakeh. 
rabbin, n., rabbi. — F. rabbin or ML. rabbinus,
```


## [2026-09-14T01:11:50.564Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rabbi, n\\.\" KLN_1966.txt | head; echo ---; awk 'BEGIN{RS=\"\\f\"} /rabbi, n\\./ {print NR}' KLN_1966.txt"
}
```


### [2026-09-14T01:11:51.770Z] TOOL RESULT

```
---
```


## [2026-09-14T01:11:54.093Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rabbi\" KLN_1966.txt | head -20; echo \"=== leaf count\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' KLN_1966.txt"
}
```


### [2026-09-14T01:11:55.218Z] TOOL RESULT

```
35:This  project  materialized  in  Toronto  where  I  settled  together  with  my  sister  Elizabeth  and her  husband,  and  where  my  friends  established  the  congregation  Beth  Yitshak,  which  was named  after  my  Father  of  blessed  memory,  and  chose  me  for  their  rabbi.
2031:rabh.  'great’  (whence  Mishnaic  Heb.  rabh, ‘master’).  See  rabbi  and  cp.  the  first  element  in •aroboam.
5856:bun,  n.,  the  tail  of  a  rabbit.  —  Of  uncertain  ori¬ gin.  Cp.  bunny.
5871:Derivative :  bunker,  tr.  v. bunkum,  buncombe,  often  shortened  to  bunk,  n., speechmaking  for  effect;  insincere  talk; hum¬ bug.  —  From  Buncombe ,  name  of  a  county  in North  Carolina,  one  of  whose  representatives was  said  to  have  spoken  frequently  in  Congress, merely  to  impress  his  constituents, bunny,  n.,  pet  name  for  a  rabbit.  —  Formed  fr.
5872:bun,  ‘rabbit’,  with  dimin.  suff.  -y. bunodont,  adj.,  having  tubercles  in  the  teeth  (ap¬ plied  to  the  pig  and  the  hippopotamus).  —  Com¬ pounded  of  Gk.  (iovv'j',  ‘mound,  hill’,  and 68<iv,  gen.  bSovzoq,  ‘tooth’.  The  first  element  is, according  to  Herodotus,  4,199,  a  Cyrenaic  loan word.  For  the  second  element  see  odonto-. Bunsen  burner.  —  Named  after  its  inventor,  the German  chemist  Professor  Robert  Wilhelm Bunsen  (1811-99).
9089:cony,  coney,  n.,  a  rabbit.  —  ME.  coning,  coni,  fr. OF.  conin,  fr.  L.  cunicutus,  ‘rabbit’,  a  word  of Sp. -Iberian  origin.  Cp.  Basque  unchi,  ‘rabbit’. Cp.  also  cuniculus.  The  alteration  of  OF.  -in to  ME.  -ing  is  due  to  a  change  of  suff. ;  cp.  pud¬ ding,  fr.  F.  boudin.
9509:Derivatives:  cozi-ly,  adv.,  cozi-ness,  n. crab,  n.,  a  crustacean.  —  ME.  crabbe,  fr.  OE. crabba,  rel.  to  ON.  krabbi,  MLG.  krabbe,  MDu. crabbe,  Du.  krab,  ‘crab’,  OHG.  krebi3,  MHG. krebes,  G.  Krebs,  ‘crayfish’.  These  words  lit. mean  ’the  scratcher’,  and  are  rel.  to  Du.  krab- belen,  ‘to  scratch’.  See  crawl  and  cp.  crab,  ‘crab apple’.  Cp.  also  OF.  crevice,  escrevice  (F. ecrevisse),  ‘crayfish’,  which  derive  fr.  OHG. krebi3  (see  crayfish).
9583:Derivatives:  crawl,  n.,  crawl-er,  n.,  crawl-ing, adj.  and  n.,  crawl-ing-ly,  adv. crawl,  n.,  an  enclosure  in  water  for  turtles.  —  Du. kraal.  See  kraal  and  cp.  corral, crayfish,  also  crawfish,  n.  —  ME.  crevise,  crevis, fr.  OF.  crevice  (also  escrevice,  whence  F.  ecre- visse),  fr.  Frankish  *krabitja,  *krebitja,  dimin. forms  rel.  to  OS.  krebit,  MDu.  crevet,  Du. kreeft,  OHG.  krehiy,,  MHG.  krebe 3,  G.  Krebs, and  to  LG.  krabbe,  Du.  krab,  ON.  krabbi,  OE. crabba,  ‘crab’.  See  crab,  ‘crustacean’, crayon,  n.,  a  stick  of  colored  chalk.  —  F.,  ‘pen¬ cil’,  orig.  ‘a  chalk  pencil’,  derived  fr.  craie, ‘chalk’,  fr.  L.  creta,  lit.  ’sifted  earth’,  fr.  (terra) creta,  fern.  pp.  of  cernere,  ‘to  sift’  (see  certain). The  usual  derivation  of  Latin  creta,  ‘chalk’, from  Creta,  the  Latin  name  of  the  isle  of  Crete, is  erroneous.  Any  Latin  derivative  of  the  island name  Creta  must  needs  have  a  Latin  suff.  If creta,  ‘chalk’,  were  really  a  derivative  of  the island  name  Creta,  its  form  should  be  cretica  or cretensis,  etc.  (for  terra  Cretica  or  Cretensis,  lit. ‘earth  of  Crete’).  Confusion  with  the  isle  of Crete  is  prob.  due  to  the  fact  that  Cimolus  (Gk. KlpcoXo?),  one  of  the  islands  of  the  Cretan  Sea, was  famous  for  the  chalk  produced  there  (see cimolite).  For  the  sense  development  of  L.  creta, ‘chalk’,  lit.  ‘sifted  earth’,  cp.  OSlav.  melu , ‘lime’,  and  Russ,  melu,  ‘chalk’,  fr.  OSlav.  meljq, mleti,  ‘to  grind’.  Cp.  It.  creta,  OProven?.,  Catal., Sp.,  Port,  greda,  MLG.  krite,  MDu.  (=  Du.) krijt,  OS.  krida,  MHG.  kride  (G.  Kreide),  Bret. creiz,  etc.,  which  all  derive  fr.  L.  creta.  The  word crayon  was  introduced  into  English  by  the  Eng¬ lish  diarist  John  Evelyn  (1620-1706).
9921:cuneiform,  adj.  —  Lit.  ‘wedge-shaped’,  com¬ pounded  of  L.  cuneus,  ‘wedge’,  and  forma, ‘form,  shape’.  See  coin  and  form,  n.  The  name cuneiform  was  first  applied  to  the  characters  of the  ancient  inscriptions  of  Assyria  and  Persia by  the  explorer  Engelbert  Kampfer  (1651-1716). Derivative:  cuneiform,  n. cuniculus,  n.,  an  underground  passage.  —  L., ‘rabbit,  rabbit  burrowing,  underground  pas¬ sage,  hole,  pit,  cavity’.  See  cony  and  -cuius. Cunila,  n.,  a  genus  of  plants  of  the  mint  family (hot.)  —  L.  cunila,  ‘name  of  a  plant,  a  species of  origanum’,  fr.  Gk.  xov(X7j,  which  is  of  un¬ certain  origin.  OE.  cunele,  ‘thyme’,  OS.  que- nela,  Du.  kwendel,  OHG.  chonela,  quenela  (G. Quendel ),  of  s.m.,  are  Latin  loan  words, cunner,  n.,  either  of  two  fishes  of  the  family  of wrasses.  —  Of  uncertain  origin, cunning,  adj.  —  ME.,  ‘knowing’,  pres.  part,  of cunnen,  ‘to  know’.  See  the  verbs  con  and  can and  cp.  canny,  uncouth.
10267:daman,  n.,  a  small  rabbitlike  mammal  (Procavia syriaca),  the  cony  of  the  English  version  of  the Bible  (see  e.g.  Lev.  11:5).  —  Arab,  damdn  Is- rd'il,  ‘sheep  of  Israel’.
17027:hagfish,  n.,  a  marine  cyclostome  (Myxine  gluti- nosa).  —  Compounded  of  hag,  ‘witch’,  and  fish, haggadah,  haggada,  n„  1)  rabbinical  teaching  of an  edifying  character ;  popular  lecture ;  the  oppo¬ site  of  halakah;  2)  the  narrative  of  the  Exodus read  at  the  Seder  on  the  first  two  nights  of  Pass- over;  3)  the  book  containing  this  narrative  and the  ritual  of  the  Seder.  —  Talm.  Heb.  haggadhdh.
20115:jacket,  n.  —  OF.  jaquet  (F.  jaquette),  dimin.  of jaque.  See  jack,  ‘a  sleeveless  coat’,  and  -et. jack  rabbit,  a  long  eared  American  hare.  — Short  for  jackass  rabbit;  so  called  in  allusion to  its  long  ears.  Cp.  its  earlier  names  mule-eared rabbit,  mule  rabbit.
20240:jerkin,  n.,  a  jacket.  —  Of  uncertain  origin. Jeroboam,  name  of  two  kings  in  Israel  (Bible)  — Heb.  Yarobh'dm,  lit.  meaning  ‘let  the  people  in¬ crease’,  fr.  yarSbh,  3rd  person  sing,  imperf.  of base  r-b-b,  ‘to  become  many,  to  increase’,  and 'am,  ‘people’.  For  the  first  element  see  rabbi, for  the  second  see  Amhaarez.  See  Martin  Noth, Die  israelitischen  Personennamen  im  Rahmen der  gemeinsemitischen  Namengebung,  206,  and G.  Buchanan  Gray,  Studies  in  Hebrew  Proper Names,  59.
21016:Lagomorpha,  n.pl.,  an  order  of  rodent  mammals including  the  hares,  rabbits  and  pikas  (zool.)  — ModL.,  compounded  of  lago-  and  Gk.  [zopepr), ‘form,  shape’.  See  morpho-. lagoon,  n.,  a  shallow  pond  connected  with  a  lake or  sea.  —  F.  lagune,  fr.  It.  laguna,  fr.  L.  lacuna, ‘pool,  pond’.  See  lacuna, lagophthalmos,  lagophthalmus,  n.,  a  morbid  con¬ dition  in  which  the  eyes  cannot  be  entirely  closed (med.)  —  Medical  L.,  fr.  Gk.  Xay6ohij:A(J.oc,  lit. ‘hare-eyed’,  fr.  Xay  cot;,  ‘hare’,  and  6(pffaXp.o;, ‘eye’ ;  so  called  from  the  belief  that  hares  cannot close  their  eyes  entirely.  See  lago-  and  ophthal- mo-  and  cp.  exophthalmos.
24073:mitzvah,  n.,  a  Biblical  or  rabbinical  command¬ ment  ( Jewish  religion).  —  Heb.  mitzwdh,  ‘com-
31486:raad,  n.,  legislative  body  in  the  former  Orange Free  State.  —  Du.  raad,  ‘advice,  counsel;  coun¬ cil’,  fr.  MDu.  reel,  reed,  rel.  to  OE.  reed,  OS.  rad, ON.  rad,  OFris.  red,  OHG.,  MHG.  rat,  G.  Bat, ‘advice,  council’,  OE.  riedan,  ‘to  advise,  counsel, discuss,  deliberate,  guess,  interpret,  read’.  See read  and  cp.  the  second  element  in  Volksraad. rabban,  n.,  distinguishing  title  given  to  patriarchs and  the  presidents  of  the  Sanhedrin  since  the time  of  Gamaliel  the  Elder,  who  was  the  first  to bear  this  title.  —  Aram,  rabban,  lit.  ‘our  teacher’, fr.  rabh,  ‘master,  teacher’,  which  is  rel.  to Mishnaic  Heb.  rabh,  of  s.m.  See  rabbi, rabbet,  n.,  a  groove  cut  out  of  the  edge  of  any¬ thing  (carpentry). —  ME.  rabet,  fr.  OF.  (=  F.) rabat,  ‘a  beating  back’,  back  formation  fr.  ra- battre,  ‘to  beat  back’.  See  rebate,  v.
31487:Derivative:  rabbet,  tr.  v. rabbi,  n.  —  Late  L.,  fr.  Gk.  pocPfii,  fr.  Mishnaic Heb.  rabbt,  ‘my  master’,  title  of  respect,  formed with  -;,  pronom.  suff.  of  the  1st  person  in  the singular,  fr.  rabh,  ‘chief,  master,  teacher’,  which derives  fr.  Heb.  rabh,  ‘much,  many,  great’,  from stem  r-b-b,  ‘to  be  great  or  numerous’,  whence also  robh,  ‘multitude,  abundance,  greatness’, rebhabhdH,  ‘multitude,  ten  thousand,  myriad’, ribbo,  ‘ten  thousand,  myriad’,  Heb.  rabh  is  rel. to  Aram. -Syr.  rabh,  ‘great;  chief,  master,  teach¬ er’,  Akkad,  rab,  ‘chief,  captain’,  Arab,  rdbba, ‘was  great  or  dense’,  rabb,  ‘master’,  Ethiop. rabdba,  ‘it  spread’.  Cp.  rabban,  the  second  word in  Ahabah  Rabba  and  the  first  element  in Jeroboam,  Rabmag  and  Rabshakeh. rabbin,  n.,  rabbi.  —  F.  rabbin  or  ML.  rabbinus, fr.  Late  L.  rabbi.  See  rabbi, rabbinate,  n.,  the  office  of  a  rabbi.  —  Formed  fr. rabbin  with  subst.  suff.  -ate. rabbinic,  rabbinical,  adj.  —  F.  rabbinique,  fr.  rab¬ bin,  ‘rabbi*.  See  rabbin  and  -ic,  resp.  also  -al. Derivative:  rabbinic-al-ly,  adv. rabbinism,  n.,  the  whole  of  the  teaching  of  the rabbis.  —  Formed  fr.  rabbin  with  suff.  -ism.  Cp. F.  rabbinisme.
31488:rabbinist,  or  rabbinite,  n.,  a  Jew  adhering  to  the oral  laws  laid  down  in  the  Talmud  and  to  the traditions  of  the  rabbis,  in  opposition  to  the Karaites.  —  Formed  fr.  rabbin  with  suff.  -ist, resp.  subst.  suff.  -ite.
31489:Derivatives:  rabbinist-ic,  rabbinist-ic-al,  adjs. rabbit,  n.  —  ME.  rabet,  ‘young  of  the  cony’,  of uncertain  origin.  It  derives  perh.  fr.  OF.  (=  F.) robot,  ‘carpenter’s  plane’,  prob.  orig.  ‘rabbit’ (cp.  F.  rabouillere,  ‘rabbit’s  hole’),  whence  ‘the animal  resembling  a  plane,  rabbit’.  It  is  also possible  that  ME.  rabet  comes  fr.  MDu.  robbe, ‘rabbit’,  whence  also  Walloon  robete,  ‘rabbit’. MDu.  robbe  prob.  derives  fr.  Rob,  dimin.  of
31490:Robert.  For  sense  development  cp.  robin,  which derives  fr.  Robin,  another  dimin.  of  Robert. Derivatives :  rabbit,  intr.  and  tr.  v.,  rabbit-y,  adj. rabble,  n.,  mob.  —  ME.  rabel,  ‘a  pack  of  animals’. The  word  prob.  denoted  originally  ‘a  noisy crowd  of  animals’  and  is  related  to  rabble,  ‘to gabble’.
=== leaf count
903
```


## [2026-09-14T01:12:00.609Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /rabbi,  n\\./ {print NR}' KLN_1966.txt"
}
```


### [2026-09-14T01:12:01.708Z] TOOL RESULT

```
689
```


## [2026-09-14T01:12:09.110Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=687 && NR<=690 {print \"=== leaf\",NR; print substr($0,1,300)}' KLN_1966.txt"
}
```


### [2026-09-14T01:12:10.183Z] TOOL RESULT

```
=== leaf 687
query  with  suff.  -ist.
quern,  n.,  a  primitive  hand  mill.  —  ME.  querne, fr.  OE.  cweorn,  rel.  to  ON.  kvern,  Dan.  kvsern, Swed.  qvarn,  OFris.  quern ,  Du.  kweern,  OHG. quirn,  chwirna,  Goth,  qairnus  (in  asiluqairnus), and  cogn.  with  OI.  grava,  ‘stone  to  crush  the
=== leaf 688
 one  in the  middle.  —  L.  quincunx,  gen.  quinquncis,  ‘five twelfths',  abbreviation  of  *quinqu(e)-uncis,  ‘five twelfths’,  fr.  quinque,  ‘five’,  and  uncia,  ‘ounce’. See  quinque-,  ounce,  ‘a  weight’,  and  cp.  uncia. quinetum,  n.,  a  mixture  of  alkaloids  fro
=== leaf 689
sp.  also  -al. Derivative:  quixotic-al-ly,  adv. quixotism,  n.,  extravagant  chivalry.  —  See  prec. word  and  -ism.
quixotry,  n.,  quixotism.  —  See  quixotic  and  -ry. quiz,  n.,  1)  an  odd-looking  person  (rare);  2)  a practical  joke;  3)  a  questioning.  —  Of  uncertain ori
=== leaf 690
upbearer',  fr.  rab,  ‘chief’,  and  shaqu,  pi. shaqe,  ‘cupbearer’  (see  ZDMG.,  53,  pp.  1 16  If.) For  Akkad,  rab  see  rabbi  and  cp.  the  first  ele¬ ment  in  prec.  word.  Akkad,  shaqu,  ‘high’,  is  of unknown  etymology.  Akkad,  shaqu,  ‘cupbearer’, derives  fr.
```


## [2026-09-14T01:12:20.843Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=685 && NR<=695 {n=NR; while (match($0,/[0-9]{4}/)) { print n, substr($0,RSTART,4); $0=substr($0,RSTART+4)} }' KLN_1966.txt | head -40"
}
```


### [2026-09-14T01:12:21.823Z] TOOL RESULT

```
685 1648
685 1650
685 1926
686 1286
686 1730
686 1287
686 1400
687 1288
687 1640
688 1822
688 1853
688 1816
689 1780
689 1494
689 1553
689 1294
689 1295
690 1859
690 1906
690 1867
690 1934
690 1898
690 1297
691 1781
691 1826
691 1788
691 1855
691 1296
692 1298
692 1706
693 1300
693 1483
693 1520
693 1707
694 1879
695 1830
695 1596
```


## [2026-09-14T01:12:36.800Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"rabbānī\\|rabbani\\|Rabbāni\\|rabb\\b\" FVQ_pages.txt | head -30"
}
```


### [2026-09-14T01:12:36.861Z] TOOL RESULT

```
5158:(rabbani) sich nicht zu Herren ihror Glaubens^enossen zii machen, sondern ihre
```


## [2026-09-14T01:12:39.785Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"rabban\\|Rabbi\\b\\|rabb\" FVQ_pages.txt | head -30; echo \"=== leaf of 5158\"; awk 'BEGIN{RS=\"\\f\"} /rabbani/ {print NR}' FVQ_pages.txt"
}
```


### [2026-09-14T01:12:40.967Z] TOOL RESULT

```
508:< J! VI j&. Rabbi of the Community, and many traditions give wonder-
1243:understood, and he quotes a line from Ibn k Abd Rabbihi, who in his
1324:they were far better acquainted with the Rabbinic writings than
1984:it means /%A>-jiJ (Nawawl, 127), which is not far from the Rabbinic
2158:used in the Rabbinic writings as a title of honour, e.g. Mish. Sanh. 60 ^
2943:to the work of the Prophets (1 Sam. x, 7, 9 ; Ex. iii, 12). In the Rabbinic
2982:use in the Rabbinic writings. D. H. Miiller, however (WZKM, i, 23),
3139:of the Syr. Ltioa 1 a turret, and perhaps of the Rabbinic *p3TlIl,
3449:used in the Targums and Rabbinic literature for HSn. Geiger has been
3889:eyebrow, and is fairly common in the Rabbinic writings. Similarly
4009:commoner for Paradise in the Rabbinic writings than in Syriac.FOREIGN VOCABULARY OF THE QUR'AN 105
4854:in the Rabbinic writings in connection with the exposition of Scripture,
4963:use the Rabbinic WH, Syr. U*?> and Mand. WH, all meaning
4987:Rabbinte WH OF = THH DV that on the surface it seems obviously
5037:Arm. tj-ffinup,* in Aram. *")J*H, which occurs both in the Rabbinic
5107:as illustrated by Ar. v^j to increase, ^j thick juice, the Rabbinic
5136:,^\-\ J (Rabbdni).
5138:Rabbi.
5146:origin, and Geiger, 51, would derive it from the Rabbinic ]3"1, a
5158:(rabbani) sich nicht zu Herren ihror Glaubens^enossen zii machen, sondern ihre
5163:Rabbi is Rabban". The difficulty in accepting (i^-[j as a direct
5876:Targums and Rabbinical writings for both a short time x and an hour,
5894:in Pirke Rabbi Eliezer, xlv, 3 was hidden within the calf and lowed to
5951:derivation from Rabbinic material (Horovitz, KU, 115; JPN, 157),
6215:the Rabbinic writings means mantle, 5 and gave rise to the verbal
6497:sovereignty, dominion, like the Rabbinic X3B/1E7 and rTtttDvlEJ.
6829:the Rabbinic use of P)^ n W.
6930:In the Rabbinic writings ]B{# is used in this sense, as are the Gk.
7104:by SIKOUOS in the LXX. In the Rabbinic Xp'HS the sense of piety
7385:Geiger, 56, sought its origin in the Rabbinic ffiJMD error which is
=== leaf of 5158
155
```


## [2026-09-14T01:12:43.981Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5100,5175p' FVQ_pages.txt"
}
```


### [2026-09-14T01:12:44.038Z] TOOL RESULT

```
and that as Geiger, 17, 18, noted, 2 it is a play on S?"1 and J1JO, and
reflects the Prophet's annoyance at the mockery of the Jews.
(Eatib).
Occurs very frequently, e.g. i, 1.
Lord, master.
The root 33*1 is common Semitic, probably meaning to be thick,
* >
as illustrated by Ar. v^j to increase, ^j thick juice, the Rabbinic
23") grease, beside the Eth. ^flfl to expand, extend. The souse of
great, however, which is so common in Heb. and Aram., and from which
the meaning Lord has developed, does not occur in Ar. or in Eth. save
as a borrowing. 3 This sense seems to have developed in the N. Semitic
area, and Margoliouth, ERE, vi, 248, notes that s^j meaning Lord
or Master must have been borrowed from the Jews or Christians.
The borrowing was probably from Aram, for it was from an Aram.
source that the word passed into Middle Persian, as witness the
Phlv. ideogram -m) rabd meaning great, venerable, splendid (PPGl,
1 as-Suyutl, Itq* 320, quoting Abu Na'Im's Dala'il an-Nubuwwa. Cf. Mutaw, 5$.
2 Vide, also Palmer, Qoran, i, 14 ; and Dvorak, Fremdw, 31 ; Horovitz, JPN, 204.
3 It occurs, however, in Sab. fl), though this, like Eth. lM t and dlfl'J, may
be from the Aram. Torrey, Foundation, 52, claims that ^} is purely Arabic.FOREIGN VOCABULARY OF THE QUR^AN 137
190 ; Frakang, Glossary, 106), which occurs as early as the Sasaniau
inscriptions, \vhere ^3(l| is synonymous with the Fazend -M>Q>
iwzurg. 1 We find H"l very frequently in the Aramaic inscriptions,
e.g. plfl I*] "chief of the market", K^TI 31 u chief of the
army ", NrP*12?Q 31 " camp master ", etc., 2 though its use in
connection with deities is rarer, 3 names like /fcOT meaning " El
is great '* rather than u El is Lord ". The special development of its
use with God was in the Syriac of the Christian communities, and as
Sprenger, Leben, i, 299, suggests, it was doubtless under Syr. influence
that Muhammad uses it as lie does in the Qur'an. 4 It was commonly
used, however, both of human chieftains and of the deity in pre-
Islamic days, as is evident from the old poetry, and from its use in
the inscriptions (Hyckmans, Noms propres, i, 196; Rossini, Ghssarium,
235).
* .1 ^-^
,^\-\ J (Rabbdni).
iii, 73 ; v, 48, 68.
Rabbi.
The passages are all late, and the reference is to Jewish teachers,
as was recognized by the Commentators. Most of the Muslim
authorities take it as an Arabic word, a derivative from ^j (cf. TA,
i, 260 ; Raghib, Mufmdat, 183 ; and Zam. on iii, 73). Some, however,
knew that it was a foreign word, though they were doubtful whether
its origin was Hebrew or Syriac. 5
As it refers to Jewish teachers we naturally look for a Jewish
origin, and Geiger, 51, would derive it from the Rabbinic ]3"1, a
later form of ^31 used as a title of honour for distinguished teachers, 6
1 West, Glossary, 133 ; Herzfeld, Paikuli, Glossary, 240.
2 See Cook, Glowary, under the various titles. So Phon. 31. Cf. Harris, Glossary,
145.
3 Though in the S. Arabian inscriptions we find 1 nil), MlnXM), etc.
(see Ryckmans, Nnws propres, i, 248), and there is a similar use in the Ras Shamra
tablets.
4 Hirschfelcl, New Researches, 30, however, argues that the dominant influence
was Jewish. See also Horovitz, JPX, 199, 200.
5 Vide. al-Jawaliqi, Mu'arrab, 72 ; as-Suyuti, Itq, 320 ; Aluzhir, i, 130 ; al-Khafaji, 94.
6 Hirschfeld, Beitragc, 51 n., says : " Muhammad ermahnt die Kabbinen
(rabbani) sich nicht zu Herren ihror Glaubens^enossen zii machen, sondern ihre
Wiirde lediglich auf das Studium der Schrift zu beschranken, vgl. ix, 31." Vide
also von Kremer, Ideen, 226 n.138 FOREIGN VOCABULARY OF THE QUR ? AN
so that there grew up the saying ]3*1 ^ITIQ /n3 " greater than
m *i
Rabbi is Rabban". The difficulty in accepting (i^-[j as a direct
derivative from 13*1, however, is the final (^, which as Horovitz,
KU, 63, admits, seems to point to a Christian origin. In Jno, xx, 16 ;
Mk, x, 51, we find the form pa/3/3oui>/ (6 Xtytrcu,
or pafitS&vei, which seems to be formed from the Targumic 113"] , l
and it was this form that came to be commonly used in the Christian
communities of the East, viz. Syr. *jUQO> ; Eth. ^fl-fc ; Arm.
fLu/fipiL^.2 The Syr. -uaoi was very widely used, and as Pautz,
Offenbarung, 78, n. 4, notes, lioi was commonly used for a doctor of
learning, and the dim. *jJQ2) was not uncommonly used as a title
of reverence for priests and monks, so that we may conclude that the
Qur'anic word, as to its form, is probably of Syriac origin. 3
j (EM).
```


## [2026-09-14T01:13:01.337Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==450' BQT_v2_pages.txt | head -c 1800"
}
```


### [2026-09-14T01:13:02.379Z] TOOL RESULT

```
  ‫زر‬                                                                                                       ‫‪۷‬‬

‫اول زای‬     ‫مردی هم بوده است؟ ‪ -‬ویجای حرف‬               ‫ر جر = با ثالی مجهول بروزن دمگره‬
               ‫قطه‌دار (‪ )۲‬هم بنظر‌آمده است ‪.‬‬           ‫نوعی از پازهر باشد ومعرب آن فادزهر است ‪.‬‬
‫رید کان ‪ = ۴‬بر وزن کردکان ‪ .‬غلام‬                         ‫رین ‪ - ۲‬بكر اول وثالكث و سکون‬
                                                        ‫حبوانات دنگ رکه اسهال‬        ‫» آدمی و‬            ‫ثالی ونون‬
                  ‫بچگان و پسرکالرا گوبند ‪¥.‬‬
                                                               ‫کاری کند ‪۰‬‬    ‫داشته باشد و آلوده‬          ‫وشکم رو‬

‫رار هیکر اول و سکون ثانی محجهول‬
‫وکام‬      ‫وزای قطه‌دار » جرعه وییمانه ‪ -‬ونعمت ‏‬          ‫= ریاکولوثالت‌بروزن بی‌چیزه‬                 ‫بر‬
                                                                                                      ‫ر‬
 ‫‪ -‬ورحمت باشد ‪ ۱‬و‪-‬خرده‬                ‫اد‬
                                       ‫را و‬
                                          ‫مهو‬
                                            ‫و‬            ‫را‬    ‫کنند و‬   ‫چوبی که کاوآهن را بر آن نص‬


 ‫وریزه را نکیوزین
```


## [2026-09-14T01:13:05.526Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ریگ\" BQT_v2_pages.txt | head -20; echo \"=== leaves\"; awk 'BEGIN{RS=\"\\f\"} /ریگ/ {print NR}' BQT_v2_pages.txt | head -20"
}
```


### [2026-09-14T01:13:06.774Z] TOOL RESULT

```
9501:                                                           ‫بلوط‌الارض باشد » وآن کیاحی است سبز ریگ‬
9649:              ‫خامة ریگ را بخون سیراب‪.‬‬                              ‫کرده ازحلق‌دشمنان چونحات‬            ‫ت‬
10035:‫بفتح اول وثانی سَحتالی زرسده‬              ‫خییو م‬                ‫وییچیده را نگیوزبند ‪ -‬وبمعنی‌تل‌ریگه ونود‬
10039:‫ریگ راکوبند ؛ و با بای فارسی گهفمته‌اند ؛‬
11279:                                                                                         ‫ریگر‬
17749:   ‫‪ - ۱‬بباوی ‪80۵۲1‬‬                     ‫‪ ۵‬بانن حعنی «ریگ» انت‬                        ‫‪.‬‬   ‫اسم صوت‬   ‫‪_ ۴‬‬      ‫(«‪.‬م‪.).‬‬
18150:                                                          ‫دریگان ‪ ۱‬بااك مجهول کواف‬
18169:  ‫فی‌ذ کرها لانها ای تسمی عندنا دربجانات سنها؛‪ .‬وهمو درالتنهیم (س ‪ )4۰4‬آرد‪«:‬دریگان‌چست؟‬
18175:  ‫هم را» وسپس بیرونی جدول خداوندان وجوه ودریگان رائت کرده است ‪ .‬رك ‪ :‬التاهیمص ‪404‬‬
18196:                                                                  ‫‪ #‬دیرجان ‪ -‬رك ‪ :‬دریگان ‪.‬‬
18939:  ‫سار | منال ودستگز ار(دستگذار)‪.‬‬         ‫نت‬           ‫ردست‬                 ‫زرای تست خرد را دلیل وباریگر‬         ‫‪۴‬‬
25140:   ‫‪ -‬رك ‪ :‬ریگ آوردن ورنگه بر آوردن ‪۰‬‬                      ‫‪.‬‬     ‫ده‬
25149:         ‫رك ‪ :‬رنه » رنگه آوردن ‪۱‬‬           ‫‪_ 4‬‬         ‫ریگ بر آوردن ‪۰‬‬         ‫‪ :‬ریگ‬    ‫رك‬    ‫‪¥‬‬
25151:   ‫* رلگرو ‪ -‬بقتح اول وچپارم » از ‪ ::‬ریگب ‪ +‬رز (رزیدن) (ه‪.‬م‪ .).‬کسکه بارچه وجز‬
25924:       ‫کم‬‫وزن هرشبینه » نرانایکوبند ‪٣‬‏ خ‬                    ‫روغن بریگ ربختن ‪ -‬کنابه‬
26600: ‫دستار باشد ‪ -‬وبمعنی رنکگ بپشته و ریگ نهاره‬           ‫وقطره قطره‌شراب اآزن میچکیده باشد لیزریش‬
26656:‫بر وزن شیراز » نوعی از‬          ‫ر بمار س‬                              ‫ریگاسه ‪ ۴‬م با ای مجپول سوین‬
26663: ‫باکاف‌فارسی ‪ ۰‬بروزن‬     ‫‪ ۲‬هننگ س‬        ‫رلم‬                         ‫ریگ روان = بکس کاف فارسی »‬
26665:                                      ‫وم‬                              ‫ریگی است که درجانب جذوب میباشد و پدوسته‬
26666:                                                                      ‫روان است ‪ .‬گوند آن ریگ تمام نقره است‬
=== leaves
164
166
173
194
302
310
321
426
441
452
453
454
460
463
472
517
526
578
612
613
```


## [2026-09-14T01:13:15.959Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=26670{if(/\\f/) c++} END{print \"leaf(0-based form-feeds before line):\",c}' BQT_v2_pages.txt; awk 'BEGIN{RS=\"\\f\"} /ریگ روان/ {print NR}' BQT_v2_pages.txt"
}
```


### [2026-09-14T01:13:17.076Z] TOOL RESULT

```
leaf(0-based form-feeds before line): 450
453
```


## [2026-09-14T01:13:25.208Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 449 450 451 452; do echo \"=== block $n (printed ~$((n-1+540)))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n \"ریگ\\|reg\\|rēg\\|ماسه\\|پهلوی\" | head -20; done"
}
```


### [2026-09-14T01:13:26.375Z] TOOL RESULT

```
=== block 449 (printed ~988)
=== block 450 (printed ~989)
34:   ‫ظ ‪ .‬مراد « ردك خوش آرزو» قهرمان رسالهٌ پهلوی « خسروقدادان و ربدكك وی »‬                            ‫‪۴‬‬
50:       ‫‪ ( 621206231 ,6681-‬بیرون ربختن) » پهلوی‪ » 0806۲ .‬لائینی ‪ .61211011‬هندی باستان‌رمشةٌ‬
=== block 451 (printed ~990)
59:  ‫رسته بمعنی مرده «بشتها‬         ‫=‬    ‫در پهلوی رستك‬      ‫‪-‬‬    ‫‪۹‬‬          ‫اول‪ ,‬خرامیدن» « منتهی الارب» ‪.‬‬
=== block 452 (printed ~991)
14: ‫دستار باشد ‪ -‬وبمعنی رنکگ بپشته و ریگ نهاره‬           ‫وقطره قطره‌شراب اآزن میچکیده باشد لیزریش‬
47:  ‫‪ - ۴‬پهلوی ‪( 2۵15۵۲‬مو) «اسشق ‪1۰٤٥‬ء‏ بازند ‪ 6051۲‬پ»ارسی رسکه ( بکر اول )‬
```


## [2026-09-14T01:13:32.235Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==453' BQT_v2_pages.txt | tail -25"
}
```


### [2026-09-14T01:13:33.370Z] TOOL RESULT

```
                                                                                                        ‫ب‬
         ‫دراول ودوم > وبعضی گوبند بونانی است‪.‬‬                         ‫کضویبند ربلو شنجار است» و آن‬
                                                                                                 ‫باشد » و بع‬
 ‫ھن د بفتح اول والك و سکون ثانی‬
                              ‫ر‬                                       ‫رستنیی باشدکه بر کهآن سیاه وبیخش سطبربود ‪.‬‬
 ‫ولون » محیل ومکار ودغا باز و کینه‌ور باشد‪-۱٩‬‏‬                                                                        ‫آفه اعلم‬

                                                                                            ‫)‪ (۱‬چش ‪ :‬ریخاشه ‪.‬‬

   ‫‪ = ۳‬ریکاشه(هم‪ = ,).‬رکاےه = رکاشه‪.‬‬                  ‫رك‪ :‬رایک‪.‬‬              ‫؟‬           ‫‪ -‬ر ک‪:‬ح‪٩‬‏ صفحهفبل‪.‬‬     ‫‏‪۱٩‬‬

    ‫‪ - ۹‬شکل پهلوی ‪= 0167‬‬                      ‫‪۰‬‬   ‫رك ‪ :‬سقنقور‬           ‫=‬    ‫‪۵‬‬             ‫= ریکاسه (ھ‪ .‬م(‬      ‫‪۳‬‬

 ‫و محفف‬     ‫مصحف‬        ‫رك ‪ :‬ریم آهن ‪ ۰‬رم آودكث »> رىمن ‪ ۰‬زریمه ‪۷.‬‬                            ‫بلوچی ‪ « 0۲6۲‬هو شمان ‪۴۹‬‬

‫یو ن‪1‬ان‪7‬ی‪ [50761-62‬یعنی شاخ( دار ) ] کرکدن «فرهنک ہونالی ‪ -‬انگلیسی دل رامکات» ‪.‬‬
   ‫هرن‬    ‫‪-۱‬‬            ‫‪ :‬ریماز ‪.‬‬   ‫رك‬   ‫‪-°‬‬                ‫‪.‬‬   ‫رم‪‎‬‬    ‫رك ‪:‬‬       ‫‪-‬‬   ‫‪٩‬‬
                                                                                               ‫‪ _ ۵‬رك ‪ :‬ریمز ‪.‬‬
                    ‫‪:‬‬    ‫‪‘<۴4‬‬   ‫ته دانته «اسشق‬         ‫همر‬           ‫(«‪.‬م‪ ).‬و «ریواین>‬       ‫را بافریو»‬   ‫این معتی‬    ‫رمن“‬


                 ‫بتك خیزند عبانان ريمن ‪.‬‬                                         ‫چو هنگام عزایم زی معزم‬
         ‫‪ ۵‬منوچهری دامفالی ‪۸‬ه * ‪.‬‬
         ‫( برهای فاطع ‪) ۳۱‬‬
```


## [2026-09-14T01:13:44.131Z] TOOL CALL #42: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T01:13:44.136Z] TOOL RESULT

```


```


## [2026-09-14T01:13:46.477Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON ریگ\"; grep -n \"ریگ \\[\\|ریگ (\\|ریگ ‪\" MON_part1.txt MON_part2.txt | head -10; echo \"=== MON رفتن\"; grep -n \"رُفتن\\|روفتن\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-14T01:13:46.565Z] TOOL RESULT

```
=== MON ریگ
MON_part1.txt:55175:(عموماً) و تل ریگ (خصوصا). 
MON_part1.txt:80668:روی ریگ (سنگك خرد) گرم در داخل 
=== MON رفتن
MON_part2.txt:27181:کنس: 1315 [ع.] (مص‌م.) روفتن خانه را 
MON_part2.txt:41421:را به چیزی مالیدن برای خوردن آن» روفتن 
MON_part1.txt:28466:تنقیح. روفتن» تمیز کردن» نظیف کردن. 
MON_part1.txt:55052:و خاشاک و آشغال که به سبب روفتن جایی 
MON_part1.txt:67959:رفستن: «۲0۲1 [- روفتن - روبیدن] 
MON_part1.txt:67963:روفتن» رویدن» جارو کردن. ادارة (دایرة) 
MON_part1.txt:68835:روب‌یدن: 200-1420 (- روفتن - رفتن ] 
MON_part1.txt:68837:جاروب کردن» روفتن» رفتن. 
MON_part1.txt:69221:روفتن: 21190656 [- رفتن - روبیدن]
```


## [2026-09-14T01:13:51.695Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '67955,67966p;68833,68840p;69218,69226p' MON_part1.txt"
}
```


### [2026-09-14T01:13:51.761Z] TOOL RESULT

```
(عم.) چه بگوید؟ کاری ندارد. 


فاء 
رفستن: «۲0۲1 [- روفتن - روبیدن] 
(مسص ع.) (رفت» روسد» خواهد رفت» 
بروب» روبنده» رفته). 
رفت‌وروب: -۲0۲۲-۵ (مص خم.) 
روفتن» رویدن» جارو کردن. ادارة (دایرة) 
رفت‌وروب: شعبه‌ای از شهرداری که به امر 
نظافت خیابان‌ها و کوچه‌ها رسیدگی کند. 
رفته: (0-)۱۸-]۲۸ (امف.) حرکت کرده» روان 
(امر.) پارچه‌ای که زنان به وسیلةٌ آن صورت 
خود را بوشانند روی‌نند» نقاب. پنام. 
روب‌یدن: 200-1420 (- روفتن - رفتن ] 
(مسصم.) پاک ساختن از گرد و غبار؛ 
جاروب کردن» روفتن» رفتن. 
روپسسوش: ۲0-۳54 [- روپ سوشنده - 
روی‌پوش] (ص‌فا.) آنچه که ظاهر و روی 
چیزی را بپوشاند. آنچه که صور تی مشخص 

روغنگر عصار. 

روفتن: 21190656 [- رفتن - روبیدن] 

(مص م.) رفتن» روبیدن» پاک کردن خاک و 

خاشا کك.
```


## [2026-09-14T01:13:53.243Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '55170,55180p' MON_part1.txt; echo \"=== MON رب\"; grep -n \"^رب:\\|رب: \\|مربا:\\|مُربا\\|مربی:\" MON_part1.txt MON_part2.txt | head -15"
}
```


### [2026-09-14T01:13:53.355Z] TOOL RESULT

```
خاموشی: -۲2:04 (حامص.) سکوت» 
بیصدایی. بی‌زبانی» گنگی. آرامی. انطفاء. 
خامه: (0)مهق:د (.) ابر بشم خام؛ ابر یشم 
ناتاییده. چریی که روی شیر جمع گردد؛ 
سرشیر. نیی که با آن چیز نویسند؛ قلم. توده 
(عموماً) و تل ریگ (خصوصا). 
خامه‌زن: .۲ [- خامهز ننده] (ص‌فا.) 
نقاش» صورتگر. 

خان: 20 (.) خانه» سرا. کاروانسرا. لانة 
زنبور» کندو. شیار داخل لولةً تفنگ. 
=== MON رب
MON_part1.txt:1609:آب‌طسرب: 20-0 (ف. ۰ ۰ (امر.) 
MON_part1.txt:2260:آخرچرب: 207-0 (اسر.) نعمت 
MON_part1.txt:2262:آخرچرب: 0۲-0 (ص‌ مر .) آنکه در 
MON_part1.txt:8573:اخرب: 23 [ع.] (ص.) (عر.) ۲ سس 
MON_part1.txt:9361:ارب: 2۳20 [غ.] (.) حاجت» قصد» 
MON_part1.txt:10171:قلب» میمنه» میسره و ساقه. ارکان حرب: 
MON_part1.txt:14713:اغرب: 20رد [ع.] (ص تفضد.) شکیفتار: 
MON_part1.txt:15481:افرب: ات2 [ع.] (ص تفض.) ی 
MON_part1.txt:33615:چرب: پهلو و جانبی که چرب باشد. سود 
MON_part1.txt:35406:رب: (کد.) عزرائیل. پیک سپید و سیاه: شب 
MON_part1.txt:37931:تسجارب: 76[ [ع. ۰] (.) 3 تحجر به ) 
MON_part1.txt:38264:تحارب: 300 [ع.] (مسص‌ل.) درهم 
MON_part1.txt:39306:تدرب: ۱۵27۲0 [ع.] (مص‌ل.) بار امدن» 
MON_part1.txt:39690:ترب: ۱0:0 (.) (گیا.) گیاهی است از تبرة 
MON_part1.txt:41230:تضارب: ۱22۵0 [ع.] (مص‌ل.) یکدیگر
```


## [2026-09-14T01:13:59.587Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%DB%8C%DA%AF",
 "prompt": "Give the full Persian etymology section for ریگ (rig) 'sand': what Middle Persian, Proto-Iranian and Old Persian forms are given, and what cognates/sources are cited?"
}
```


## [2026-09-14T01:14:01.853Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%81%D8%AA%D9%86",
 "prompt": "Is there an entry for Persian رفتن meaning 'to sweep' (roftan / ruftan, also روفتن، روبیدن)? Give its etymology: Middle Persian, Proto-Iranian root, cognates, and any cited sources."
}
```


### [2026-09-14T01:14:04.217Z] TOOL RESULT

```
# Persian Etymology of ریگ (rig)

Based on the Wiktionary entry provided, here's what the etymology section states:

**Middle Persian form:** The entry indicates the word comes from Middle Persian, but notes "[Book Pahlavi needed]" with the form listed as "lyk' /⁠rēg⁠/" meaning "sand."

**Proto-Indo-European origin:** According to the source, the word is "ultimately inherited from a derivative of Proto-Indo-European *h₃reyH-" meaning "to flow."

**Attribution:** The etymological analysis crediting the Proto-Indo-European connection is attributed to Korn.

**No Old Persian or Proto-Iranian forms are explicitly provided** in this etymology section. The entry jumps directly from Middle Persian to the Proto-Indo-European reconstruction without documenting intermediate stages or forms from those language periods.
```


### [2026-09-14T01:14:07.778Z] TOOL RESULT

```
# Persian رفتن (to sweep)

Yes, there is an entry for the verb رفتن with the meaning "to sweep" (roftan/ruftan). This represents Etymology 2 in the Wiktionary article.

## Etymology

**Middle Persian origin:** The term derives from Middle Persian *lwp-* (rōb-).

**Proto-Iranian root:** It comes from Proto-Iranian *raup-*, meaning "to sweep," which likely represents a semantic specialization of the Proto-Iranian root meaning "to take away, rob."

**Cognates and related terms:** The article notes possible connections to Vedic Sanskrit *योप्* (yop, "to wipe out, efface, remove") and Ancient Greek *γῡ́ψ* (gū́ps, "vulture"). The verb is cognate with Baluchi *روپگ* (rópag, "to sweep, broom").

## Cited Sources

The Wiktionary entry cites:
- MacKenzie, D. N. (1971), *A concise Pahlavi dictionary*
- Cheung, Johnny (2007), *Etymological Dictionary of the Iranian Verb*
```


## [2026-09-14T01:14:16.068Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%A8%D8%A7",
 "prompt": "Give the etymology of Persian مربا (morabbā) 'jam': which Arabic word and Arabic root is it from (ر ب ب or ر ب و)? Also report anything on رب (rob/rabb)."
}
```


## [2026-09-14T01:14:17.196Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rabbi",
 "prompt": "Give the full etymology of English 'rabbi': the chain Hebrew > Greek > Latin > English, dates, and the Hebrew root."
}
```


### [2026-09-14T01:14:20.009Z] TOOL RESULT

```
# Etymology of Persian مربا (morabbā)

Based on the Wiktionary entry:

**Arabic Source:** The word derives from Arabic مُرَبَّى (murabbā), which itself comes from the Arabic verb رَبَّى (rabbā).

**Arabic Root:** The entry explicitly states it comes from "the Arabic root ر ب و" (r-b-w), not ر ب ب.

**Regarding رب (rob/rabb):** The page does not provide information about this related term or its relationship to مربا.

The etymology tree shows the progression: Arabic rabbā → Arabic murabbā → Persian morabbā, with the meaning being "jam," "preserve," or "murabba" (a type of fruit preserve).
```


### [2026-09-14T01:14:22.930Z] TOOL RESULT

```
# Etymology of English "Rabbi"

**Hebrew Root:** The word derives from the Semitic root *r-b-b* meaning "to be great or numerous," with the noun *rabh* signifying "master, great one."

**Language Chain:**

1. **Hebrew (Mishnaic):** *rabbi* — literally "my master" (combining *rabh* + the first-person singular suffix *-i*)

2. **Greek:** *rhabbi* — direct transliteration from Hebrew

3. **Latin:** *rabbi* (Late Latin) — borrowed from the Greek form

4. **English:** *rabbi* — entered in the early 14c., initially appearing "in late Old English in biblical context only, as a form of address."

**Key Development:** An alternative form *rabbin* (appearing by the 1520s) influenced the development of related terms like *rabbinical* (1610s-1620s), likely through French *rabbin* or Medieval Latin *rabbinus*.

The term originally denoted a "Jewish doctor of religious law" and was used as a title for spiritual teachers.
```


## [2026-09-14T01:14:29.988Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%A8",
 "prompt": "Report the Arabic entries: رَبّ (rabb) 'lord, master' — its etymology and root; and رُبّ (rubb) 'thickened juice, syrup' — etymology and root. Also any Persian section for رب."
}
```


## [2026-09-14T01:14:31.392Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=28380 && NR<=28430' SOD_pages.txt | sed -n '1,60p'"
}
```


### [2026-09-14T01:14:36.274Z] TOOL RESULT

```
# Arabic Entries: رب (rab)

## رَبّ (rabb) - "Lord, Master"

**Etymology & Root:**
The term derives from Proto-Semitic *rabb-, with the Semitic root ر ب ب (r b b). It shares cognates with Hebrew רַב (ráv, "rabbi"). The word encompasses meanings of master, lord, king, sovereign, owner, and as a religious term, refers to God or deity.

## رُبّ (rubb) - "Thickened Juice"

**Etymology & Root:**
This noun originates from the same Semitic root ر ب ب (r b b), though its semantic field differs significantly. The term denotes thickened fruit juice, syrup, mash, or pulp—a culinary preparation rather than a title or authority figure.

## Persian Section: رب

The Persian entry includes two etymologies, both borrowed from Arabic:

1. **رب (rab)** as proper noun/noun meaning "the Lord" or "God" (now obsolete in common usage except for divine reference)
2. **رب (rob)** borrowed from Arabic رُبّ, meaning "tomato sauce"

Modern Persian prefers ارباب (arbâb) for "lord" in secular contexts.
```


### [2026-09-14T01:14:37.431Z] TOOL RESULT

```
        MSP bl65                                                               Frag. Len. pl08; inf. ->y, Dhy. 196; AVS 114
                                                                        8563 rwd C =» rw5
8552 rw'rtyh M
                                                                        8564 rw8>k B                              (•JUiJJ)^Ui.l/
     r(u)war0ya ? ©<Av. urvaOra ^rw'rt                                       ro5e, roSak ?
     delicacy
        Sogdica. 2.16, Add.                                                  plant, herb
                                                                             TSP 3214: Frag. 3.4
8553 rwp B, M     ({^ tj^)(ok>ujj*£^^ -{j)o\**
     ru|3 ©Av. uruOwan; Parth. rumb ©ob. -yh                            8565 rwdny      C =» rw6ny(y)
     mouth                                                              8566 rw5n-      M                                    j-^.jj
        TSP 5.109, 6.44, 9.110, 116, 15.28; BBB 592                          roSan ©caus. st. =^rw5-
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
                                                                             ob.
                                                                             rwbs;-y(h)
                                                                                     Oss. robds; Skt. lopasd; *raupasa ©f. n.;
 8569 rwSynch B
y     roSenc ©f. adj. ^rwSy^k
                                                       J5UJ                fox
       (o/)brass, brazen
                                                                           GMS 121; TSP 2.772, 13.18; Frag. Len. 68, 18, 19;
       SCE 229; GMS 1058
                                                                             SCE 149; Hen. Tales. 475.15
8570 rwyn
                                                if 11 'iJtJ?         8582 rwpsy'kh S
       royn   ©Av. raoYna*, Pahl. roYn\ Khwar. rYn%                                                       *bj(<f ^js) <u*bj
                                                                          rupasyak
          Yaghn. ruYin ©ob. -y(y) =»Y>W rwyn                              (related to)fox
       fat, oil
                                                                           MDii B-3, 13, 14-5 p71, 73nl2-3; MDiii p63
       TSP 2.897; BSTBL, Padm. 40, 54, Dhy. 279; STi
```


## [2026-09-14T01:14:52.289Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB rōb/rōp\"; grep -n \"rōb\\|rōp\\|ruftan\" NYB_vol2_glossary.txt | head -20; echo \"=== PHD RBA / wuzurg\"; grep -n \"RBA\\|wuzurg\" PHD.txt | head -10"
}
```


### [2026-09-14T01:14:52.363Z] TOOL RESULT

```
=== NYB rōb/rōp
3029:patigriftan [ptglptn', MKBLWN-], pati- gruftan [ptglwptn'] pačir- [MKBLWN-, ptyl-], pt. = pret. pass. 3d p. sg. patigrift [ptglpt'; MKBLWN.t, MKBLWN-x, 2876, 299. 611; -x, 21, 18%] patigruft [ptglwpt'] 5811. 6015: to receive, to ac- cept, to take up, often with the prev. frac: 1. Bastvar (PLK”) pat dast fräc patigrift B. caught *the battle-axe (just swung by the attacking enemy) with his hand 2875-26; barak xvēš pat dast frac patirét he himself takes command of the steed (by grasping the reins) with his hand 299. — 2. en den i mäzdesnän hac Ohurmazd patigrift he received the Maz- dayasnian religion from O. 18%2?sq. 1919, ete.; hàn 4 Evak frāc patigrift u apārīk hac dastavar hist the one (doctrine) he accepted and the other he excluded from the canon 10954. — 3. to agree 215; to accept, to comply with 381; göbiön ~ to receive the (divine) command 5811, 6028. — 4. pat fradandeh ~ to adopt as one's son 275; pat zanēh ~ to espouse 161; pat nikühdareh ~ to take charge of 8213. — 5. kē hac šmāh hàn patirét marnjénitan ? who among you takes it upon himself to slay this man? 4217; oišan-ic . . . baxtan
3031:received it (the earthly riches) from O, in order to distribute it 7914-15, — 6. Ohur- mazd ... hakarc anākēh nē patīrēt O. is never subject to Evil 772 (cf. Arab la yaqbalu); 794-5. — From pati + Av. OP grab-, v. griftan; MPrth pdgryfin pdgyrw-; MPrs pdyryfin pdyr-, v. Verbum 205, Ghilain 89; Paz. padiraftan padir-, NP pačiruftan pačir-.
3341:rop [lwp'] pillage, plundering 108%. — Cf NP ruftan rob- ‘to sweep’.
3799:neh u burtäreh u ~ 11214. — Av. (643) tarop- ‘to steal’. subju. trofyāt (Y.115; a hapax) < *trpydt with secondary develop- ment of -r- to -ra- (tr- is only secondary in Olr) Cf NP tarb, tarfand ‘deceit, fraud, lie’. As the BP derivatives of this root semantically agree with Av., whereas the derivatives outside this group have other, non-technical significations, the former must be regarded as borrowed from Av., and consequently tlpt is best interpreted as trift, not as tirft as Bthl has it. This is confirmed by the parallel form tlwpt = truft with -ri- > -ru- be- cause of the labial. I give here the BP forms known to me: 1. inf. tlwptn! = truftan DkM 364U (+ bwrtan, cf 11214 just quoted); 2. tlpt'l = triftär Phl. Y 291: 3. tlwptk = truftak BAA p. 2418; 4. tlptkyh = triftakéh, v. above; 5. tlp- tynytn' = trifténitan "to commit theft’ Phl Y. 115 (translation of trofyāt); 6. tlpt = trift ‘theft’ explaining Av. (638) taya-.
3863:uspurrikiha [wspwlykyh’] in a perfect, consummate manner 1064. — It ought to be spelt *ws, but cf uzruftan and s. v. uzītan, also yst*tn' for ’yst-, estätan.
7295:padiruftan, padir-: patigriftan
=== PHD RBA / wuzurg
657:wizürd-wars [wc'/t' wls] with parted hair. wizāstan, wizāy- [wyz'stn!, wyz'd- | M wy2’y-, N guzáy-] injure, impair, prejudice. ~išn: injury. ~išnīg: injurious. wizén [wcyn! | N guzin] choice. wizend [wz(y)nd | M wzynd, N guzand] hurt, harm, injury. wizéngar [wcynkl] chooser; selective. | wizidan, wizin- [weytn', wcyn- | M weyd, N guzīdan, guzīn-| choose, select, prefer, discriminate. wizihidan, wizīh- [w(y)cyh-ytn'] be separated. „išn(īh): separation; dawn(ing). wizin- , v. wizidan. wizir [weyl] decision, judgement. wiziristan, wizir- [wcyl-stn! | J bzyr-, N guzir-) be able to dispense with, avoid. ~iSnig : avoidable. wizistan [westn' | M weyst] teach. wizóstan, wizóh/y- [wewstn', wewd- | (J bzwb-, N pizohidan)] examine, investigate. -~i§n : investigation. wizüdan [wyzwin'] = wizastan. wizurd [wewlt'] valid, genuine, true. ~th: validity, truth. Wērūbaršt [w’wklwblst' = Av. wouru.barasti-] the north-western con- tinent of the earth. Wērūjaršt [w>wklwelft' = Av. wouru.jarasti-] the north-eastern con- tinent of the earth. wurróyistan, wurróy- [H YMNN-stn! < A hymn, У °тп | M wrwyst, (wrw-), J *brwy-, grww-, N brw-, girawidan] believe; choose. —išn [wlwdén'] belief. wuzurg [LBA < Arb’; wc(w)lg | M wzrg, N buzurg] big, great. ~ith: size, greatness. wuzurg-framadar [LBA plm't I) prime minister.
994:big wuzurg, stabr.
2144:great meh, wuzurg.
2147:greatness wuzurgih.
2816:minister dastwar; prime — wuzurg- framádar.
3222:prime minister wuzurg-framādār,
3679:size wuzurgih, zahā, zahih.
4944:daw-! Jdawistan! Jdawidan! (215) wuzurg!
4945:wuzurgih!
4946:wuzurg-framā idir Ww ud pd
```


## [2026-09-14T01:14:53.362Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB rēg\"; grep -n \"rēg\\|rēk\" NYB_vol2_glossary.txt | head -10; echo \"=== PHD gyāg\"; grep -n \"gyāg\" PHD.txt | head -5"
}
```


### [2026-09-14T01:14:53.442Z] TOOL RESULT

```
=== NYB rēg
4180:virēk [wlyk'] flight 1°. 821, from
7356:rauyan: rēgn
=== PHD gyāg
1102:broom gyāg-rēb.
3136:place(n.) gah, gyāg; proper ~ dādgāh.
4305:where kū (gyāg).
```


## [2026-09-14T01:15:12.239Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT rabbi\"; grep -n \"^Rabbi\\|Rabbi,\" SKT.txt | head -5; echo \"=== AFA rabb\"; grep -n \"rabb\\|Rabb\" AFA.txt | head -10; echo \"=== KNT raika\"; grep -n -i \"raika\\|sand\" KNT.txt | head -10"
}
```


### [2026-09-14T01:15:12.355Z] TOOL RESULT

```
=== SKT rabbi
=== AFA rabb
1685:lers IL 985 zusammen stellt. (Manduisch i<3SX^II Sidr. Rabb.
2494:Rabbi Samuel weiss auch sonst mehrfach gerade über Meer-
2623:1) Als •Kranz* z. B. Wnjikra Rabb. s«ct. 22. Mitte: »er sib eine Pflanze.
4568:Der »rabbinische" (aramäische, im babyl. Talmud übliche)
7109:unserer neueren Agg. gesammelt hat, noch Rabbinowitz bemerken übrigens au
7334:aus dem der Rabbi Wein trank. Uasi erklart schon rich-
7538:— Noch ein specifisch arabbcher Ausdruck ist hier zu er-
7547:Arabbchen erhalten Lh »anlegen** (vom Schiffe) und daher
7630:enrieeen, gegenikber einem Codex Rabbinowiti*a, der cintr Ahlettnng von ftV2
10051:Commentar des Rabbi Samuel b. Meir zum Pentateuch (ed«
=== KNT raika
97:X CONTENTS . 673. The pIE Stops in Proto-Aryan....... 28. $121. The Ablaut Grades of the Vowels.... 42 $74. The pIE Stops in Proto-Iranian. ..... 29° $122. Ablaut Variation within the Root. ... 43 $75. The pIE Labial Stops in OP......... 29: $123. Funetional Ablaut Variation within $76. The pIE Dental Stops in OP... ..... 30 : the Verbal Воо{................... 43 $77. pIE ¢ before сопѕопапіз............. 31: $124. Functional Ablaut Variation within MB. PAL Urs ке ы ete ovatis 31: the last Stem-Syllable of Nouns. . . . . 43 $79. pAr. é after врігапів................ al 5125, Guna and Vriddhi.................. 44 S80 PIE оне ү 32 $120. Vriddhi as а Formative............. 44 $81. рЇЁйи............................ 32 8127, Брепіћевіз........................ 45 882 е) О, TEE 32 $428. Апар!ухз......................... 45 §83. Other Developments of Non-Final Den- $129. Наріоіору......................... 45 tal SUODS ee ГО ОС 32 $430. Shortening of Long Consonants...... 45 §84. Final Пепіајв..................... . 92 8131. Contraction of Vowels.............. 46 $85. The Dental Clusters /st(h) and dzd(h). 32 5132. Consonantal Variation.............. 46 $86. The pIE Palatal Ѕіорв.............. 33 $188. Епейыз........................... 46 $87. pIE & before vowels................ 33 8134. The Phonetics of Enclisis. ........... 41 $88. pIE ў and фћ...................... 39 8135. The -d before enclitic............... 47 $89. pIE &...............5.2........... 34 $136. The -iy before enclitic............... 47 890. pIE Би............................ 94 8137. The -wv before enclitic.............. 47 691, pIE @ш........................... 34 8138. Consonants before enclities.......... 47 802. pIE &............................ 34 $139. Contraction of Vowels in Sandhi..... 47 $98. pIE Й............................ 34 $140. Sandhi in Connection with Prefixes... 47 804. РЁ®ЕЙ............................ 34 Appendix to Chapter III. The Ori- $95. pIE km and ўћт................... 35 gins of ОР Sounds................ 48 $96. pIE £n gn фМм..................... 35 897. рЇЕзЁ............................ 35 Снартев IV. 398. e = bad i Labores n 35 Formation OF Noun AND ÁDJECTIVE STEMS $99. рАт.Бап@ф....................... 35 14 Noun and Adjective Stems. ......... 49 $100. pAr. kk... sss 36 $142. Root Nouns and Adjectives.......... 50 $101. pAr. g and ў, gh and fh. . ........... 36 $143. Noun and Adjective Stems with the- STU: OP US еа ые» Ыы да toc rA 36 ШАЙ «s oad os vene уч» heads 50 $108. pAr. k апа g before consonants....... 37 $144. Noun and Adjective Stems vith suffix 8104. pAr. бр. 37 E ae een 50 $105. The Cluster -8-6-................... 37 $145. Noun and Adjective Stems with suffix $106. pIE r. .... ЖОЛ ce onis ol bes a8 T EPOR PET 51 О РО S ortis tes toon 38 $146. Noun and Adjective Stems with suffix 6108. The pIE Мавыв.................... 38 Д оо Ье ОТ 51 $109. pE т............................ 38 8147, Noun and Adjective Stems with suffix S110; DPE moe I" 39 ME EEE A TE E 51 $111. OP Unwritten Medial Nasals........ 39 5148, Noun and Adjective Stems with suffix $112. OP Final n... 39 =, ЖКК E ERECTO 51 SUR Mm 39 $149. Noun and Adjective Stems with suffix РИИ КОКОС 39 Spe uc p bet uaa bea Г Г 51 30580007 TEES 40 $150. Noun and Adjective Stems with suffix JUNO C 40 ЕЛ ЖКН КОКО — € 51 ТИ Ыр S du at trata ches SOM e e 40 $151. Noun and Adjective Stems with mis- JE ULP оао 41 cellaneous -a- suffixes....... 52 BE EDO v HE 4] $152. Noun and Adjective Stems sin in
365:pIE -s g*- and -d q*- in sandhi, before front vowel, became Med. с, Av. šč, OP s (shown by Pahlavi only) and remade c; $105.
399:masc. kašciy, nt. cifciy, avaSciy, aniyasciy, with Sc from -s q*- and -d g*- respectively, in sandhi; no specific reason сап be assigned for the borrowing by OP of this type.
708:Cf. also the sandhi phenomena of düraiapiy DNa 12, dürayapiy DNa 46, and the same as two words, diraty ариу.
1111:The preposition абу seems to be a sandhi doublet of айу; see Lex. s.v.
1128:Final -d disappeared after 1, as in the enel. OP -cly, Skt. cid, pIE q*id; OP лаш ‘not’, Av. лб, from *ne + id. After и the final t seems to be retained as § in OP akunaus ‘he made’, adarsnaus ‘he dared’, Skt. ákrnot ddhysnot; but this § is better taken as an extension of the s of the aorist, after which -t would be lost. The prefix ud ‘up’, which appears unchanged before a vowel in ud- apatatā ‘he rose up (in rebellion)’, suffers com- plete assimilation of the d in uzma- ‘stake’ (from *ud-zma-), and became us- in us-taSand- ‘stair- case’ in the dental cluster (585).
1129:For the sandhi combination of final 0 with initial с, see §105.
1330:cf. Av. paséa, Skt. pased. The evidence of Sasa- nian Pahlavi shows that this value alone is pho- netic in OP (Bv. Gr. §114), and that the -&- which is seen in some sandhi combinations, be- longs rather to Median: OP kaSevy ‘anyone’ from pIE *q*0s-q*id; manaš-clä] DNb 32 from *menos-
1333:The sandhi product of -d c- has a similar varia- tion: OP s (not attested) and remade c (§130), Med. $c; there are the following examples: pIE *ed-q*id, ОР aciy ‘then’, Av. а/с. plE *7od-q*id, ОР yaciy ‘when’, Av. yatčit. pIE *g#d-gtid, OP cišciy ‘anything’, with Med.
1425:Final s was subject in Aryan to various sandhi developments other than - and -h; these are best seen in Sanskrit. But Iranian generalized -§ and -h and shows only these values and their direct phonetic developments, except for a few combinations with enclitics (the OP examples are in §105). Skt. words and forms will be cited with -s and -h in order to show clearly their rela- tion to the OP words and forms with which they are compared.
```


## [2026-09-14T01:15:13.395Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"ریگ\" ARY_pages.txt | head -10; echo \"=== latin index\"; grep -n -i \"REG\\b\\|RIG\\b\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T01:15:13.469Z] TOOL RESULT

```
620:پیشین ترین نوشتارها به این زبانها دریگ وداء (870-۷780۸) است که قدمت آن به ۱۵۰۰
=== latin index
604:NBe+ 4 OT Cn WS Cael (RIG-VEDA) clay oS ao ls gpl 4 WSEAS op Fonts
921:REIKS:e5 3 FRIG: 45 5.5 | KRALI
1256:Sate WNL eed 9 Falsts eee cat pas le ep dy call OLT bes rig gl
1860:*REG., *(ER-) (INDO-EUROPEAN) «gilig,)\ y i
1888:SIL die thy *REG- setts SIL a cal lin a el a ela! Glanjly bib POKORNY -F
2233:*AREG., *ARG-, *ARGU., *RGHI- (INDO-EUROPEAN) igilag,} 9
2949:MACKENZIE: (RAIN) 129 URIG, WAR. «(OLDENGLISH) 3455-381
3028:BEREG (RUSSIAN) gy BOLAN ATATIC) Sts
3029:BRIG OLD IRISH) 348 543 2) BARHAYATI — -(SANSKRIT) Suite
3425:BERIG (LITHUANIAN) gg PAR (TOKHARIAN A) A 565
```


## [2026-09-14T01:15:23.075Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt; do echo \"=== $f\"; grep -n \"rab-bi\\|rabbi, n\\|rab'bi\" $f | head -3; done"
}
```


### [2026-09-14T01:15:24.327Z] TOOL RESULT

```
=== FSD_vol1.txt
10792:a-ke'nl-um*  n.  Same  as  achenium.  a-kene't.  Ak-rab'bim,  1   ak-rab’lm;  2   &k-rGb'Ira,  n.  Bib.  A   pass  In
81394:crab1,  v.  [crabbed;  crab'bino.]  I.  t.  1.  [Prov.  Eng.] To  cudgel  or  beat,  as  with  a   crab-stick.  2f-  To  make surly  or  sour;  irritate.
81399:etc.),  the  lazy  c.  ( Parthenope  horrida),  and  the  swift  c.,  crab'bing*,  1   krab'ip;  2   crab'lng,  n.  The  act  or  business  of a   land  species,  especially  one  of  the  genus  Ocypoda.  For  catching  crabs.
=== FSD_vol2.txt
1852:‘i.  One  of  various  lioetuid  luotha;  a   Quaker.  [Color  of ^   undyed  cloth,  <   F.  drop,-  see  nR.tPE.J  —   drab'bish, «.
=== FSD_vol3.txt
211914:seiiiiilliix thut nt a hare a burelipped mouth rab'bit- rab'lt. 1 rat/it, 2 r&bMt, n I. [Prov Kng ] A wooden
=== FSD_vol4.txt
4417:It  could  make  some  shift  to  scrabble  and  sprawl  jn  tho  water Bunyan  Works,  Grace  Abounding  p   54  [n  o   A   co  1871  1 rvar  of  8CRAPPLE,  freq  of  scrape,  p   ]   scrab'let. scrab'bic,  n   1.  A   scrabbling  or  scrambhng  2.  A   scrib- ble, a   scrawly  document  or  picture scrabc,  1   skrCb,  2   serfib,  n   (Scot  ]   The  Manx  shearwater scrab'er,  i   skrCb'or,  2   serflb’er,  n   (Scot]  Tho  black guillemot
=== WEB_vol1.txt
```


## [2026-09-14T01:15:26.546Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '211900,211925p' FSD_vol3.txt | grep -n -i \"rab'bi\\|rabbi\" "
}
```


### [2026-09-14T01:15:26.660Z] TOOL RESULT

```
12:A hutch or coup In which tame rabbits ra'^bi-ru 'bl-a, I rd*bi-ra'bi-a; 2 ril'’bi-n}M)1-n. n A liitianold
15:seiiiiilliix thut nt a hare a burelipped mouth rab'bit- rab'lt. 1 rat/it, 2 r&bMt, n I. [Prov Kng ] A wooden
19:Wales rab'blt-root", n Wild Marsaparllla — rabbit's* Ifleb , head of the Maxi ]
```


## [2026-09-14T01:15:29.313Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Heb  rabbi\\|Heb rabbi\\|my master\" FSD_vol3.txt | head -5; echo ---; sed -n '211880,211900p' FSD_vol3.txt | grep -n -i \"rabbi\" "
}
```


### [2026-09-14T01:15:29.458Z] TOOL RESULT

```
---
```


## [2026-09-14T01:15:52.779Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%DB%8C%DA%AF' --note 'page 415, root Raika, Persian rig sand: MP rēg, PIE *h3reyH- per Korn' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%D9%81%D8%AA%D9%86' --note 'page 415, root Raup, Persian roftan to sweep: MP rōb-, PIr *raup-, Cheung 2007' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%A8%D8%A7' --note 'page 415, root R.b.b, Persian morabbā: from Arabic murabbā, root r-b-w not r-b-b' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%D8%A8' --note 'page 415, root R.b.b: Arabic rabb and rubb, Proto-Semitic *rabb-, Persian rab/rob' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/rabbi' --note 'page 415, root R.b.b, English rabbi: Hebrew rabbi > Greek > Late Latin > English' 2>&1 | tail -3"
}
```


### [2026-09-14T01:15:56.285Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0206b6de9c92e682.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0b39be7b8983e00c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1a52b5d2dd2cea23.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec1aaab2898dec05.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/390c6d1dfd274e3b.txt
```


## [2026-09-14T01:16:06.289Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 415 -l 415 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg415hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg415hi.png'); print(im.size)\nw,h=im.size\n# empty box approx x 0.60-0.79, y 0.555-0.62 of page\nim.crop((int(0.55*w),int(0.53*h),int(0.85*w),int(0.63*h))).save('pg415-emptybox.png')\n\"; ls"
}
```


### [2026-09-14T01:16:08.796Z] TOOL RESULT

```
(2550, 3300)
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
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
pg418hi.png
pg418.png
pg418-raj2.png
pg418-raj3.png
pg418-rajidan.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
```


## [2026-09-14T01:16:11.875Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg415-emptybox.png"
}
```


### [2026-09-14T01:16:11.893Z] TOOL RESULT

```

```


## [2026-09-14T01:16:18.054Z] TOOL CALL #62: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:16:18.112Z] TOOL RESULT

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


## [2026-09-14T01:16:20.221Z] TOOL CALL #63: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:16:20.268Z] TOOL RESULT

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


## [2026-09-14T01:17:30.747Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON مربا/رب\"; grep -n \"مربا:\\|مربی:\\|رب:\" MON_part1.txt MON_part2.txt | head -10; echo \"=== MON ریگ:\"; grep -n \"ریگ:\" MON_part1.txt MON_part2.txt | head -5; echo \"=== NYB LBA\"; grep -n \"LBA\\|wuzurg\\|vazurg\" NYB_vol2_glossary.txt | head -8"
}
```


### [2026-09-14T01:17:30.863Z] TOOL RESULT

```
=== MON مربا/رب
MON_part2.txt:174:غارب: 0 (ع.] (افا.) غروب کننده 
MON_part2.txt:998:غظرب: ۳۳0 [ع. ۰] (مسصل 0( پنهان شسدن» 
MON_part2.txt:3748:غیر مجرب: ناازموده» تحربه نادیده» خام؛ 
MON_part2.txt:4161:فوارس. فارس عرب: آنکه الفاظ عرس را د 
MON_part2.txt:4169:زبان مردم ایران. (نجا.) مورب: پشت 
MON_part2.txt:12129:فرب: ۳۳ [ع.] (مص‌ل.) نزدیک شدن؛ 
MON_part2.txt:13403:تطرب: ۲۵0 [ع.] (.) (بر.) ناخوشیی که 
MON_part2.txt:14287:ترکیات اسمی: قلم سرب: قلم فرنگی. قلم 
MON_part2.txt:21633:کرب: 12۵ [ع.] (.) اندوه دم گیر» عم 
MON_part2.txt:30626:گرپ‌گرب: 0۲0-۵ (اصت.) صدای 
=== MON ریگ:
MON_part2.txt:53053:مرده‌ریگ: 12- ۰ [- مرده‌ری - مردری] 
MON_part1.txt:17201:انتریگ: و۳ (.) (نم. رمان) وقایع و 
=== NYB LBA
124:K’L’: GALA voice KN: K'-*AN now KBYR (inscr., Ps.), KBYR: KABBIR great KDB’: KI DBA (B pronounced v) lie KDMWN-: (QDM) pa‘‘el QADDEM to rise early KHDH: KA-HADA ‘as one’ = together KLB': KALBA dog KLSH: KARSEH his belly KLYT’: QELLAYTA cell KLYTN-, KRYTN-: QRY (old QR») to call KN: KEN so KNY?: QANYA reed KR?: KOLLA all
1001:bitaxš [bythš] the Grand Vizier, of Jä- mäsp at Vištāsp's court 21—24. 2713; of the corresponding official at Arjasp’s court 2511, 287... A Prth. Arsacid title, adopted by the Sassanid kings of the 3d c., but later replaced by vazurg framatär (v. the 2nd w.); survived in independent Armenia governed by Arsacids (until A. D. 430) and in Georgia. Sas. inser. Prth byths, Prs bythšy KZSPrth a) 1. 23, b) l. 25, c) l. 27 = Prs ll. 29. 31. 33 Gr. v. a) Bde (in the list of the late Artaxšēr's officials), b) miridēng of Shapur’s own vizier, c)
1095:eak [ck'] the top of the skull; of a sheep: the extremity of the head = the nose and the chin 1028. — NP cak ‘the lower jaw and chin', but Bal. prep. cak*-à *upon'. cand [end] 1. interrogative: how much? how many? 2412-13, 629. 8313. ki... ~ in- direct interr. 213-4 — 2. relative: as much, as many as: ---šān tuvān dätan as much as they are able to bestow 79%; apärik ~ vazurg-kunisndn the other performers
1530:framatar [prmt?l] commander, leader: the title of the Grand Vizier is vazurg ~ F:
2347:kurušk [kwlwšk'] ewe, of a big species of sheep 509-11, — Zsprm X, 20 in telling this story: meš kurušk i šīr-pistān "with milk in her udder’. Also kwryšk' = Paz. kurišk, koriák, BdA, p. 959-1? = BdJ2918— 303: meš 5 sratak: han i pat-dumb, han 4 a-dumb, u sak meš, u meš *takilé [tkly ; Paz. tagr, tgar] <u> kurišk tmeš, ke srub vazurg, asp homänäk, 3 köf [BdA corrected from tan, BdJ Paz. koh] dārēt api-š 6 bārak girénd, cigēn gobet ku Mānušcihr + amāh niyak kurišk-ē pat bārak dāšt [sak
2559:*mih(a)rg [mytlg; Vd. 21? mtlg] cloud, the sphere of the clouds 21”. — Existing in the sphere called in Av. mäna-, v.s. v. mänenak. -g is to be explained in the same way as in andarg, vastarg, vistarg, vazurg: the suff. -ka- was added directly to the stem (cf arišk, husk) and -k- voiced by contact with the preceding -r-; -tl- is no doubt the archaistic spelling -0r- for Milr -hr.; original form consequently *miür-ka > mihrg and then perhaps with secondary vowel miharg, cf *vazrka- > vazurg ete. Possibly derived from M36ra-, cf Yt. 109! where he is praised as the giver of rain; not identical with MTL? (for Prth MTR’) varan, FrP 1.
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3097:sert PWN = pat before ~); ~ rdyénitan to form family connections 6319; ~ kar- tan id. (apäk with) 706; ~ u tohm extrac- tion, descent 625. 632; descendants 63%; ~ u tóhmak % vazurg high lineage 72*; ~ cas. rect. pl. offspring 941°. - MPrs pywn = paivann; Paz. paévand; NP paivand. From patvastan.
```


## [2026-09-14T01:17:31.700Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK reup\"; grep -n \"reup-\\|reu-p-\\|^reup\" POK_full.txt | head -10"
}
```


### [2026-09-14T01:17:31.762Z] TOOL RESULT

```
=== POK reup
22904:d^reup-:0\6 Saxon drubon, druvon^ be grieving '; Latvian drupu, drupV zerfallen, in 
31628:greu-p-:QX. ypunoq " hook-nosed, aquiline, hooked, writhed, crooked, humped, with a 
48657:Root / lemma: kreup- 
70786:e. reup- ^ausre'\Q>en, tear, break, rupture'; roupa-^ho\e, aperture ', rupeis-xocV! . 
76537:(s)keru-p-, (s)kreu-p-: 
76549:See also: compare also kreup- above S. 623. 
80847:Root / lemma: sreup- 
86161:7. treup-:gr. Tpunaw ' drill, wimble, bore a hole, durchbohre', rpunavov 'borer', rpunri
```


## [2026-09-14T01:17:38.087Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '70760,70800p' POK_full.txt | head -50"
}
```


### [2026-09-14T01:17:38.148Z] TOOL RESULT

```
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
```


## [2026-09-14T01:17:38.964Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"RB’\\|RB'\\|RBA\\|RABBA\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T01:17:39.027Z] TOOL RESULT

```
55:LB’: ’ARBÄ for >A RBA‘ four
138:LB’: RABBA great, cf RB?
4067:"| vazurg [LB”, Prth RB’; wewrg, inscr.
4068:welk-] great, big, high, lofty, passim; regularly placed before its head w., seldom: after (41?. 724); in titles great, chief: ~ framatar (g. v.); ~ šahridar (q.v.); — subst., pl. cas. obl. ~-dn the magnates HajA:6 [RB’n]. B:6 [welk’n]. 42. 1133, 16? [wewlg'n'], v. Christensen, Sass. 100. 110sq. — OP vazrka-; MPrthPrs wzrg; Arm. lw. vzurk, vzork, vzruk; Paz. guzurg, guzarg; NP buzurg. No comp. and sup.; for these forms meh, mahist are used; v.s. v. mas.
```


## [2026-09-14T01:17:48.924Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<70790 && /Root \\/ lemma:/ {l=NR\": \"$0} END{print l}' POK_full.txt; awk 'NR>70700 && NR<70790 && /Page.*:|Pages/ {print NR\": \"$0}' POK_full.txt | head"
}
```


### [2026-09-14T01:17:50.074Z] TOOL RESULT

```
70664: Root / lemma: reu-2, reus- : ru-
```


## [2026-09-14T01:17:53.005Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '70664,70690p' POK_full.txt; echo \"...\"; awk 'NR>70664 && NR<70900 && /868|869|870|871/ {print NR\": \"substr($0,1,120)}' POK_full.txt | head"
}
```


### [2026-09-14T01:17:54.141Z] TOOL RESULT

```
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
...
70773: (as S. 868 Old Icelandic rqg^: Old Indie ruksa- "rough', common Old Indie -gh- > ks- : Gr. - 
70854: Page(s): 868-871 
70864: Page(s): 871 
70869: Page(s): 871
```


## [2026-09-14T01:18:00.321Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg415hi.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/415.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/415.png"
}
```


### [2026-09-14T01:18:00.409Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78342 Sep 13 21:18 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/415.png
```


## [2026-09-14T01:24:03.775Z] TOOL CALL #71: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-415.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 415,\n \"book_page\": 385,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Raika\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Old/Proto-Iranian *raika- (< *raiHka-) 'sand' — a reconstruction, not an attested Old Persian word; > MP rēg > NP rīg\",\n   \"note\": \"The starred form is Hübschmann's: Pers. Studien p.68 no.642 'Np. rēg ‚Sand‘ = bal. rek = ap. *raika-'. Nourai's root box reproduces that reconstruction but prints it without the asterisk and labels it flatly 'Old Persian'; no such word is attested in the Old Persian inscriptions (Kent's lexicon has no word for 'sand'), so the label should read 'Old Iranian (reconstructed)'. The gloss 'sand, gravel' is right. Modern work (Korn, cited on Wiktionary; cf. Hasandust) takes MP rēg from a -ka- derivative of PIE *h₃reyH- 'to flow', i.e. *raiH-ka- 'that which flows/streams' — compatible with, and more explicit than, Nourai's *raika-. Horn p.142 also records the rival 19th-c. proposal (Bartholomae, ZDMG 46, 301 no. XIX) linking the Iranian words to Skt. sikatā- 'sand', which Hübschmann rejects ('gehört gewiss nicht zu skr. sikata-'); modern scholarship follows Hübschmann. The Rudakī line quoted in the box is from Bū-ye Jūy-e Mūliyān; the book prints «ریگ آموی و درشتی های او», where the received text reads «ریگ آموی و درشتیِ راهِ او» — a quotation variant, not an etymological problem.\",\n   \"note_fa\": \"ریشهٔ این خانواده صورتِ بازساختهٔ *raika- (ایرانی باستان) است که نخست هوبشمان در «پژوهش‌های فارسی» (ص ۶۸، ذیل شمارهٔ ۶۴۲ هرن) پیشنهاد کرد: «فارسی نو rēg = بلوچی rēk = ایرانی باستان *raika-». این صورت در کتیبه‌های پارسی باستان گواهی نشده است، پس برچسبِ «پارسی باستان» در کتاب باید «ایرانی باستانِ بازسازی‌شده» خوانده شود؛ معنای «شن، ریگ» درست است. ریشه‌شناسی امروزی (کرن، به نقل ویکی‌واژه؛ نیز حسن‌دوست) آن را از *raiH-ka- از ریشهٔ هندواروپایی آغازین *h₃reyH- «روان شدن، جاری شدن» می‌گیرد که با پیشنهاد نورایی ناسازگار نیست. پیوند کهنِ بارتولومه با سنسکریت sikatā- «شن» را هوبشمان به‌صراحت رد کرده و پژوهش امروزی نیز آن را نپذیرفته است. کوتاه: ادعای نورایی با احتیاط پذیرفتنی است، به شرط آنکه ستاره (*) و عنوانِ درستِ زبان افزوده شود.\",\n   \"sources\": [W+\"%D8%B1%DB%8C%DA%AF\"],\n   \"ref_check\": [\n    {\"ref\": \"HRN:142\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.142 (local HRN.txt, form-feed block 164 = printed 142), entry '642. rēg ‚Sand‘ (AM. 242 Zeile 9), rez (Käs. Z. ryz)' with the note that Bartholomae (ZDMG 46, 301 No. XIX) 'stellt die iranischen Worte zu ai. sikata- ‚Sand‘'. Horn gives the NP word and its Iranian cognates, i.e. exactly the material of the chart, though the starred Old Persian form itself is Hübschmann's, not Horn's.\"},\n    {\"ref\": \"BRT\", \"status\": \"not_found\", \"note\": \"Bartholomae, Altiranisches Wörterbuch: grep of BRT.txt for 'raēka', 'ra^ka', 'araika' returns nothing; the AiW has no Avestan or Old Persian entry for a word 'sand' of this shape (the only 'Sand' hits are in unrelated articles, lines 16346 and 30043). Nourai cites BRT without a column number; his source is presumably Bartholomae's ZDMG 46, 301 note, which Horn p.142 quotes and Hübschmann rejects.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.68, no. 642\", \"stance\": \"supports\", \"note\": \"'642. Np. rēg ‚Sand‘ = bal. rek = ap. *raika- gehört gewiss nicht zu skr. sikata-.' This is the direct source of Nourai's root box (local HUB.txt, block 79 = printed p.68).\"},\n    {\"src\": \"KNT\", \"where\": \"Old Persian lexicon\", \"stance\": \"silent\", \"note\": \"grep of KNT.txt for 'raika' and for an OP word glossed 'sand' finds nothing — the form is unattested in the Achaemenid corpus, which is why it must carry an asterisk.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. ریگ\", \"stance\": \"partial\", \"note\": \"'From Middle Persian lyk′ /rēg/ ‚sand‘ … ultimately inherited from a derivative of Proto-Indo-European *h₃reyH- ‚to flow‘ (Korn)'; gives no Old Persian form, i.e. supports the etymon but not the 'Old Persian' label.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"rěg\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian rēg (Book Pahlavi lyk′) 'sand' is well attested and is the regular continuation of Old Iranian *raika-: intervocalic/postvocalic *-k- is preserved after the diphthong, and OIr. *ai monophthongises to MP ē (as in *daiza- > diz, *gaiθā- > gēhān). MacKenzie's Concise Pahlavi Dictionary prints 'rēg [lyk′ | N ~] sand', and Nyberg's vazurg-type spellings confirm the same orthographic habit. Nourai's transliteration 'rěg' (with a breve) is his house notation for majhūl ē and is not an error.\",\n     \"derivation_fa\": \"فارسی میانه (پهلوی) rēg، به خط کتابی lyk'، «شن». این صورت دنبالهٔ منظمِ ایرانی باستان *raika- است: دوواکهٔ *ai در فارسی میانه به ē تک‌واکه شده (مانند *daiza- > diz) و ک میانی پس از دوواکه محفوظ مانده است. مکنزی در «فرهنگ کوچک پهلوی» می‌آورد: rēg [lyk'] «شن». نشانهٔ ě در کتاب نورایی همان ای مجهول است و خطا نیست. ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%B1%DB%8C%DA%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"PHD:73\", \"status\": \"partial\", \"note\": \"MacKenzie does have the word — 'rēg [lyk′ | N ~] sand' (OCR 'тёр [/yā! | N ~] sand') — but it stands on p.71, not p.73: in PHD.txt the entry sits in the form-feed block whose running head is 'rēšag 72 rózig' and immediately before it, i.e. p.71; p.73 (block with head 'rūz-šabān 73 sān') runs from rūz-šabān to sān and contains no rēg. Substance supported, page reference off by two.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p.71 s.v. rēg\", \"stance\": \"supports\", \"note\": \"'rēg [lyk′ | N ~] sand' — Middle Persian form and gloss exactly as in the chart.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for 'rēg'/'rēk' returns only virēk 'flight' and rauyan: rēgn — the word does not occur in Nyberg's text corpus, so he is silent, not contrary.\"},\n      {\"src\": \"HRN\", \"where\": \"p.142 no.642\", \"stance\": \"supports\", \"note\": \"Horn's entry heads the Middle Persian/New Persian word together: '642. rēg ‚Sand‘ … LW. (?) kurd. rik, rig; afγ. reg; bel. rek'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"rîg\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP ریگ rīg 'sand, gravel' continues MP rēg directly: Middle Persian majhūl ē is written with ی and, in the eastern/standard modern pronunciation, has fallen together with ī (rēg > rīg), exactly as MP šēr > šīr, MP dēv > dīv. The chart's further forms are transparent New Persian derivatives: ریگزار rīg-zār 'sandy tract' with the place-suffix -zār (< MP -zār 'field'), and ریگستان rīg-estān 'sand desert' with -estān (< OIr. *-stāna- 'place'). Mo'in's footnote to Borhān-e Qāṭeʿ gives the Pahlavi antecedent and the Balochi cognate and refers the reader to Hübschmann, which is the same chain the chart draws.\",\n     \"derivation_fa\": \"«ریگ» در فارسی نو دنبالهٔ مستقیم rēg فارسی میانه است؛ ای مجهولِ فارسی میانه در فارسی نوِ معیار با ای معروف یکی شده و rēg به rīg بدل شده است (همان‌گونه که šēr > šīr و dēv > dīv). «ریگزار» و «ریگستان» ساخت‌های سرراست فارسی نو با پسوندهای مکان ‑زار و ‑ستان (از *-stāna- ایرانی باستان) اند. معین در حاشیهٔ برهان قاطع همین زنجیره را می‌آورد: «شکل پهلوی rēg… بلوچی rēk، هوبشمان ۶۸». ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%B1%DB%8C%DA%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"HUB:68\", \"status\": \"supports\", \"note\": \"Hübschmann, Persische Studien p.68: '642. Np. rēg ‚Sand‘ = bal. rek = ap. *raika- …' — the New Persian word, its Balochi cognate and the reconstructed Old Iranian etymon, i.e. the whole chart in one line.\"},\n      {\"ref\": \"BQT:989\", \"status\": \"partial\", \"note\": \"Mo'in's etymological footnote to ریگ is in BQT_v2_pages.txt at form-feed block 453 (printed ≈ 992 on the verified 'printed = leaf + 540' offset), a couple of pages after Nourai's 989: '۹ - شکل پهلوی rēg' (OCR '0167') and '… بلوچی rēk، هوبشمان ۶۸'. Substance exactly as charted (Pahlavi rēg, Balochi rēk, citing Hübschmann p.68); only the page number is slightly off / the offset uncertain by 2-3 leaves.\"},\n      {\"ref\": \"HRN:142\", \"status\": \"supports\", \"note\": \"Horn p.142 no.642 lists the New Persian word rēg 'Sand' with the variant rez and the Kurdish/Afghan/Balochi cognates.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (OCR MON_part1/2)\", \"stance\": \"silent\", \"note\": \"grep for 'ریگ:' as a headword in MON_part1.txt/MON_part2.txt returns no lexicon entry (only compounds inside other articles, e.g. line 55175 'تل ریگ'); the OCR of the ر section is defective here, so Mo'in is recorded as silent rather than contrary.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt for 'ریگ' gives only one unrelated hit (line 620, 'ریگ‌ودا' = Rig-Veda); no headword ریگ.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. ریگ\", \"stance\": \"supports\", \"note\": \"'From Middle Persian lyk′ /rēg/ ‚sand‘', ultimately a derivative of PIE *h₃reyH- 'to flow' (Korn).\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Raup, Raud\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Proto-Iranian *raup- 'to take away, snatch; (specialised) to sweep' (Cheung *raup¹ / *raup²), from PIE *reup- 'to tear out, break' (Pokorny 868-871, esp. 870)\",\n   \"note\": \"The base is genuine and Bailey does operate with it ('base raup- ‚to sweep, carry off‘', Dictionary of Khotan Saka s.v. burūvāñi). Two reservations. (1) 'Indo-Schythian' is not a language: it is Nourai's shorthand for Bailey's Indo-Scythian Studies (Khotanese Texts VI), and the reconstruction it holds is a general Iranian one (Cheung reconstructs *raup² 'to sweep' as a semantic specialisation of *raup¹ 'to take away, rob'), ultimately PIE *reup-. (2) The variant 'Raud' is not supported for the meaning 'to sweep away': Bailey pairs raup-/raud- only in the quite different family of āṛūva- 'refuge' and prūva- 'fort' (< *ā-raupa- or *ā-rauda-, 'to ascend / to rise'), and Cheung has no *raud 'sweep'. Nourai's cross-reference entry 'Raud → see Raup' therefore merges two different bases. The spelling 'Indo-Schythian' is the book's own (it occurs 13 times across the extracted corpus), not a scan error.\",\n   \"note_fa\": \"ریشهٔ *raup- ایرانی آغازین («ربودن، برگرفتن»؛ در معنای خاص‌شده «رُفتن») واقعی است و چونگ آن را با دو شمارهٔ *raup¹ و *raup² می‌آورد؛ خاستگاه دورترش هندواروپایی آغازین *reup- «کندن، دریدن» است (پوکورنی ۸۶۸–۸۷۱). دو نکته: نخست آنکه «هندوسکایی» نام زبان نیست، بلکه کوتاه‌نوشتِ نورایی برای کتاب «پژوهش‌های هندوسکایی» بیلی است و این بازسازی سراسرِ ایرانی است نه ویژهٔ ختنی. دوم آنکه گونهٔ «Raud» در معنای «رُفتن» پشتوانه ندارد؛ بیلی raup-/raud- را تنها در خانوادهٔ دیگری (āṛūva- «پناهگاه»، prūva- «دژ») کنار هم می‌گذارد که معنای «برآمدن، بالا رفتن» دارد. پس ارجاعِ «Raud ← Raup» دو ریشهٔ جدا را در هم آمیخته است: ادعای نورایی با احتیاط پذیرفتنی است.\",\n   \"sources\": [W+\"%D8%B1%D9%81%D8%AA%D9%86\"],\n   \"ref_check\": [\n    {\"ref\": \"ISS:251\", \"status\": \"not_checked\", \"note\": \"Bailey, Indo-Scythian Studies / Khotanese Texts VI is not available in full text anywhere permitted (refs_online.json: Google Books partial preview and HathiTrust search-only). The substance was checked instead in Bailey's own Dictionary of Khotan Saka (local ISS_alt_DKS.txt), which restates the same etymology: 'From base raup- ‚to sweep, carry off‘, *vi-raup- > burūv-, Sogd. Bud. rwp- ‚pluck‘, pr′wp-, pr′rwp ‚sweep‘ … Zor.P. rōpet, gīvāk-rūp ‚broom‘ … N.Pers. rōb-, ruftan ‚sweep‘' (line 5491).\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb pp.319-321, s.v. *raup¹ and *raup²\", \"stance\": \"partial\", \"note\": \"'*raup² ‚to sweep‘ … MMP *rwb-, BMP lwp- /rōb-/ ‚to rub, sweep‘ … NP rōb-/ruftan … This root is probably originally identical to *raup¹, which has developed a more specialised meaning ‚to sweep‘.' Supports the base, but knows no *raud 'to sweep'.\"},\n    {\"src\": \"POK\", \"where\": \"Root/lemma reu-2, reus- : ru-, pp.868-871 (extension 'e. reup-')\", \"stance\": \"supports\", \"note\": \"'e. reup- ‚ausreißen, tear, break, rupture‘; roupa- ‚hole, aperture‘ … Old Indic ropayati ‚causes rupture‘ … Latin rumpo' — the PIE base Bailey cites as 'IE Pok. 870 reup- ‚tear out‘' (DKS s.v. -rūvai).\"},\n    {\"src\": \"ISS_alt_DKS\", \"where\": \"Dictionary of Khotan Saka, s.v. burūvāñi and rrūv-, ro-\", \"stance\": \"supports\", \"note\": \"'From base raup-:rup- ‚to remove, sweep away‘' (s.v. rrūv-) and the long cognate list at burūvāñi quoted above — Bailey's own presentation of the root that Nourai labels 'Indo-Schythian'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"rôpet, rôp 2; givâk-rôp\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both forms are genuine Middle Persian. (a) rōpēt/rōbēd (Book Pahlavi lwp-, 3sg. pres. of the verb whose infinitive is rōftan) 'sweeps' — MacKenzie: 'rōb- [lwp- | N ruftan, ~] rub, sweep'; the -ft- of the infinitive is the regular outcome of stem-final -b/-p plus the past suffix -t. (b) 'rōp 2' is Nourai's copy of Bailey's homonym numbering: beside the verb stands the noun rōb/rōp 'robbery, plunder' (MacKenzie 'rōb [lwp] robbery'; Nyberg 'rōp [lwp′] pillage, plundering … Cf NP ruftan rōb- ‚to sweep‘'), the *raup¹ 'take away' branch. (c) gīwāk-rōp = gyāg-rōb, literally 'place-sweeper', i.e. 'broom'; gyāg (gywʾk) 'place' + the verbal stem rōb — MacKenzie's English index has 'broom gyāg-rōb'. Bailey spells the first element gīvāk after the Book Pahlavi orthography gywʾk, which is why the chart's form looks unfamiliar; it is not a misprint.\",\n     \"derivation_fa\": \"هر دو صورت پهلوی راستین‌اند. rōpēt (به خط پهلوی lwp-، سوم‌شخص مفرد حال از مصدر rōftan) «می‌رُوبد»؛ مکنزی می‌آورد: rōb- [lwp-] «رُفتن، پاک کردن»، و ‑ft‑ در مصدر پیامد منظم همنشینی ب/پ پایانیِ ستاک با پسوند گذشتهٔ ‑t است. «rōp ۲» شمارهٔ هم‌آواییِ بیلی است: در کنار فعل، نامِ rōp «غارت، ربایش» می‌ایستد (نیبرگ: rōp [lwp'] «غارت»… «سنجیده شود با فارسی نو رفتن، رُوب‑»). gīwāk-rōp همان gyāg-rōb «جاروب» است، تحت‌اللفظ «جای‌رُوب»: gyāg «جای» + ستاک rōb؛ نمایهٔ انگلیسی مکنزی نیز دارد: «broom gyāg-rōb». املای gīwāk از خط پهلویِ gywʾk گرفته شده و خطای چاپی نیست. ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%B1%D9%81%D8%AA%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"ISS:252\", \"status\": \"not_checked\", \"note\": \"Khotanese Texts VI p.252 not obtainable (see the root-level note). Bailey's equivalent passage in the Dictionary of Khotan Saka names precisely these two forms: '… Zor.P. rōpet, gīvāk-rūp ‚broom‘, uz-, zrūpat, zruftak ‚removed‘' (ISS_alt_DKS.txt line 5491), so the chart reproduces Bailey faithfully.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p.71 s.v. rōb-, rōb; English index 'broom'\", \"stance\": \"supports\", \"note\": \"'rōb- [lwp- | N ruftan, ~] rub, sweep'; 'rōb [lwp] robbery'; index: 'broom gyāg-rōb' — all three of Nourai's Pahlavi items.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. rōp\", \"stance\": \"supports\", \"note\": \"'rōp [lwp′] pillage, plundering 108². — Cf NP ruftan rōb- ‚to sweep‘.' Confirms the 'rōp 2' noun and its link to the sweeping verb.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *raup², Middle Persian section\", \"stance\": \"supports\", \"note\": \"'MMP *rwb-, BMP lwp- /rōb-/ ‚to rub, sweep‘; Inf.: MMP *rwptn' — Manichaean and Book Middle Persian attestations of exactly this stem.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"roftan\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP رفتن/روفتن ruftan ~ rōftan 'to sweep' (present stem rōb-, روب) is the direct continuation of MP rōftan, rōb-; the majhūl ō of the Middle Persian infinitive gives both the spelling روفتن and the contracted رفتن (the latter homographic with, but etymologically unrelated to, رفتن 'to go' < *raθ-/*hraw-). روبیدن rūbīdan is a New Persian back-formation: the present stem rōb-/rūb- plus the productive infinitive suffix -īdan, exactly the pattern Mo'in registers ('رفتن rōftan [= روفتن = روبیدن]'; 'روبیدن [= روفتن = رفتن]'). The chart's extra words belong here too: جاروب jārūb 'broom' is Cheung's *ui-a-raup- (he lists 'NP jārū ‚broom‘' under *raup²) and لایروبی lāy-rūbī 'dredging' is لای 'silt' + the same stem rūb + -ī.\",\n     \"derivation_fa\": \"«رُفتن/روفتن» دنبالهٔ مستقیم rōftan فارسی میانه است با ستاک حالِ «روب‑» (rōb-). واوِ مجهولِ مصدرِ فارسی میانه هم املای «روفتن» را پدید آورده و هم صورت کوتاه‌شدهٔ «رفتن» را که تنها در نوشتار با «رفتن» (به معنی «راه سپردن») یکسان است و با آن هم‌ریشه نیست. «روبیدن» ساختِ نوترِ فارسی است: ستاک حال «روب» + پسوند مصدری زایای ‑یدن؛ معین همین سه‌گانه را ثبت کرده است: «رفتن rōftan [= روفتن = روبیدن]». «جاروب» نیز از *ui-a-raup- (چونگ: jārū در فارسی نو) و «لایروبی» از «لای» + «روب» + «ی» است. ادعای نورایی درست است.\",\n     \"sources\": [W+\"%D8%B1%D9%81%D8%AA%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"ISS:252\", \"status\": \"not_checked\", \"note\": \"ISS p.252 unobtainable; the corresponding Bailey passage (DKS line 5491) reads 'N.Pers. rōb-, ruftan ‚sweep‘ … For ‚broom‘, N.Pers. jā-rūb' — both the verb and the compound Nourai puts in this box.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.vv. رفتن, روفتن, روبیدن\", \"stance\": \"supports\", \"note\": \"'رفتن: rōftan [- روفتن - روبیدن] (مص م.)'; 'روفتن: rōftan [- رفتن - روبیدن] رفتن، روبیدن، پاک کردن خاک و خاشاک'; 'روبیدن: [- روفتن - رفتن] جاروب کردن، روفتن، رفتن' (MON_part1.txt lines 67959, 69221, 68835) — Mo'in equates exactly the three variants the chart prints.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *raup², NWIR section (p.320)\", \"stance\": \"supports\", \"note\": \"'NP rōb-/ruftan ‚to sweep, dust‘, Bal. rupt/röp- ‚to sweep up‘ … || (+ *ui-a-) NP jaru ‚broom‘'.\"},\n      {\"src\": \"HRN\", \"where\": \"p.135 no.608\", \"stance\": \"supports\", \"note\": \"'608. rubūden ‚wegnehmen, rauben‘, Praes. rubāy-em …; ruften ‚fegen, gäten‘, Praes. rōb-em … phlv. rōp ‚Raub‘ (AV.-Gl.), kahrupāl ‚Bernstein‘' — Horn already joins NP ruftan to Pahlavi rōp, as the chart does.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Sogdian\",\n     \"words\": \"rwp\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Sogdian rwp- is real and is from the same *raup-, but the gloss 'to sweep' is the root meaning rather than the meaning of the attested Sogdian simplex. Gharib's dictionary (no. 8580) gives 'rwp- B, C: rōp, © *raup-, Pahl. rōb; (?) pick up', and Cheung files Buddhist Sogdian rwp 'to gather', Christian Sogdian rwp 'θερίζω (to reap)' and Manichaean Sogdian rwp 'to harvest' under *raup¹ 'to take away', while the sense 'to sweep' appears in Sogdian only with a preverb: BSogd. pr′wp- (Dhyāna text), pr′rwp. Bailey states the same distribution: 'Sogd. Bud. rwp- ‚pluck‘, pr′wp-, pr′rwp ‚sweep‘'. So the arrow root → Sogdian is correct; only the gloss inside the box is too narrow a rendering of the Sogdian evidence.\",\n     \"derivation_fa\": \"ستاک سغدی rwp- راستین است و از همان *raup- ایرانی آغازین می‌آید؛ اما معنای «رُفتن» معنای ریشه است، نه معنای صورتِ سادهٔ سغدی. قریب (شمارهٔ ۸۵۸۰) می‌آورد: «rwp- سغدی بودایی و مسیحی، rōp، از *raup-، پهلوی rōb، (؟) برگرفتن». چونگ نیز rwp سغدی بودایی «گرد آوردن»، سغدی مسیحی «دروییدن» و سغدی مانوی «درو کردن» را ذیل *raup¹ «ربودن، برگرفتن» می‌آورد و «رُفتن» در سغدی تنها با پیشوند دیده می‌شود: pr'wp-. بیلی هم همین را می‌گوید: «سغدی بودایی rwp- ‚چیدن‘، pr'wp- ‚رُفتن‘». پس پیکانِ ریشه ← سغدی درست است و تنها معنای درون جعبه تنگ‌تر از گواهی‌هاست: با احتیاط پذیرفتنی است.\",\n     \"sources\": [W+\"%D8%B1%D9%81%D8%AA%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"ISS:251\", \"status\": \"not_checked\", \"note\": \"ISS p.251 unobtainable; Bailey's DKS (line 5491) gives 'Sogd. Bud. rwp- ‚pluck‘, pr′wp-, pr′rwp ‚sweep‘, Chr. rwp-', i.e. he cites Sogdian rwp- for this root exactly as the chart does but glosses the simplex 'pluck'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 8580 (also 8553, 8581)\", \"stance\": \"partial\", \"note\": \"'8580 rwp— B, C | rōp ©*raup-, Pahl. rōb | (?)pick up | VJ 695; STi 47.17, 48.21' — same etymon and same Pahlavi comparison, but the gloss is 'pick up', not 'sweep'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *raup¹ (Sogdian section) and *raup² (Sogdian section)\", \"stance\": \"partial\", \"note\": \"'*SOGDIAN: BSogd. rwp ‚to gather‘, CSogd. rwp ‚θερίζω‘, MSogd. rwp ‚to harvest‘' under *raup¹; under *raup² only '(+ *upa-/apa-/pari-) BSogd. pr′wp- ‚to sweep‘'.\"},\n      {\"src\": \"ISS_alt_DKS\", \"where\": \"s.v. burūvāñi\", \"stance\": \"supports\", \"note\": \"Bailey's cognate list places Sogdian rwp- squarely in the raup- 'sweep, carry off' family, which is the arrow the chart draws.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"R.b.b\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Common Semitic root r-b-b, Proto-Semitic *rabb- 'to be much, thick, numerous' > (North-West Semitic) 'to be great; lord, master'\",\n   \"note\": \"The root is real and common Semitic, and Klein's article s.v. rabbi is exactly the chart's tree. The gloss needs a nuance that Nourai's own cited reference supplies: Jeffery (FVQ 136-138 = VDQ 214-215) writes 'The root r-b-b is common Semitic, probably meaning to be thick, as illustrated by Ar. rabba to increase, rubb thick juice, the Rabbinic rbb grease, beside the Eth. to expand, extend. The sense of great, however, which is so common in Heb. and Aram., and from which the meaning Lord has developed, does not occur in Ar. or in Eth. save as a borrowing.' So 'to be great, large or numerous' is the North-West Semitic development, not the reconstructable Proto-Semitic sense; 'to be thick, dense, much' is. The Hebrew > Greek > Latin > English branch is uncontroversial.\",\n   \"note_fa\": \"ریشهٔ سه‌واکِ ر ب ب ریشه‌ای سامی مشترک است و مدخل «rabbi» در فرهنگ کلاین همان درختی را می‌کشد که نورایی کشیده است. اما معنای بازسازی‌شدهٔ آغازین، چنان‌که جفری (منبعِ خودِ نورایی) می‌نویسد، «انبوه و غلیظ بودن» است نه «بزرگ بودن»: «معنای بزرگ که در عبری و آرامی چنین رایج است و معنای «خداوند/ربّ» از آن برآمده، در عربی و حبشی جز به‌صورت وام‌واژه دیده نمی‌شود». پس عنوانِ جعبهٔ ریشه اندکی پس‌وپیش افتاده است: با احتیاط پذیرفتنی است. شاخهٔ عبری ← یونانی ← لاتینی ← انگلیسی بی‌مناقشه است.\",\n   \"sources\": [W+\"%D8%B1%D8%A8\", \"https://www.etymonline.com/word/rabbi\"],\n   \"ref_check\": [\n    {\"ref\": \"VDQ:214\", \"status\": \"supports\", \"note\": \"VDQ is Badreh'i's Persian translation of Jeffery; noorlib's viewer is JavaScript-only, so the substance was checked in the original, FVQ pp.136-137 (FVQ_pages.txt block 155): 'The root r-b-b is common Semitic, probably meaning to be thick … The sense of great, however … does not occur in Ar. or in Eth. save as a borrowing.' Supports the root box, with the gloss caveat above.\"},\n    {\"ref\": \"KLN:1293\", \"status\": \"supports\", \"note\": \"Klein s.v. rabbi (KLN_1966.txt block 689, the leaf carrying printed pp.1293-1295; same text in the 1971 one-volume ed. line 198889): '… fr. rabh, ‚chief, master, teacher‘, which derives fr. Heb. rabh, ‚much, many, great‘, from stem r-b-b, ‚to be great or numerous‘ … Heb. rabh is rel. to Aram.-Syr. rabh … Akkad. rab … Arab. rabba, ‚was great or dense‘, rabb, ‚master‘, Ethiop. rababa, ‚it spread‘.' This single article underwrites the Semitic root box and the Arabic, Aramaic, Hebrew and English boxes.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. rabbi, rabban (1966 pp.1293-1295)\", \"stance\": \"supports\", \"note\": \"quoted above; 'rabban, n. … Aram. rabban, lit. ‚our teacher‘, fr. rabh, ‚master, teacher‘'.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an, pp.136-138 s.vv. رب and ربّانی\", \"stance\": \"partial\", \"note\": \"supports the root but restricts the 'great/Lord' sense to North-West Semitic; quoted above.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. رب (Arabic)\", \"stance\": \"supports\", \"note\": \"Arabic رَبّ (rabb) 'lord, master' from Proto-Semitic *rabb-, root ر ب ب, cognate with Hebrew רַב.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Arabic\",\n     \"words\": \"r.b.b\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Arabic ر ب ب is certainly the same root, but the two halves of Nourai's gloss have different standing. 'To be thick and dense' is the native Arabic value: رَبَّ 'to increase, thicken', رُبّ 'thickened juice'. 'To be great / lord' is, on Jeffery's argument (following Margoliouth, ERE vi 248), a sense borrowed into Arabic from Jewish and Christian Aramaic: 'the sense of great … does not occur in Ar. or in Eth. save as a borrowing … رب meaning Lord or Master must have been borrowed from the Jews or Christians', and the Qur'anic usage of رَبّ for God is, per Sprenger, under Syriac influence. Klein, by contrast, simply lists 'Arab. rabba, ‚was great or dense‘' as a cognate. So the arrow Semitic → Arabic is right, the internal gloss half-right.\",\n     \"derivation_fa\": \"ریشهٔ عربیِ ر ب ب همان ریشهٔ سامی است، اما دو نیمهٔ معنایی که نورایی آورده جایگاه یکسان ندارند. «غلیظ و انبوه بودن» معنای بومیِ عربی است: رَبَّ «افزودن، غلیظ شدن»، رُبّ «افشرهٔ غلیظ». اما معنای «بزرگ بودن، خداوندگار» بنا بر استدلال جفری (به پیروی از مارگلیوث) وام‌گرفته از آرامیِ یهودی و مسیحی است: «معنای بزرگ… در عربی جز به‌صورت وام دیده نمی‌شود» و کاربرد قرآنیِ «رَبّ» برای خداوند به تأثیر سریانی بازمی‌گردد. کلاین اما تنها «rabba عربی، بزرگ یا غلیظ بودن» را هم‌ریشه می‌شمارد. پس پیکانِ سامی ← عربی درست است و معنای درون جعبه نیمه‌درست: با احتیاط پذیرفتنی است.\",\n     \"sources\": [W+\"%D8%B1%D8%A8\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1293\", \"status\": \"supports\", \"note\": \"'Arab. rabba, ‚was great or dense‘, rabb, ‚master‘' — literally Nourai's double gloss ('to be great, also to be thick and dense').\"},\n      {\"ref\": \"VDQ:214\", \"status\": \"partial\", \"note\": \"checked through FVQ pp.136-137: the Arabic root is there, but Jeffery explicitly denies that the 'great' sense is native Arabic ('save as a borrowing'), so the box's first gloss is a loan-sense rather than an inherited one.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"pp.136-137 s.v. رب\", \"stance\": \"partial\", \"note\": \"'as illustrated by Ar. رب to increase, رُبّ thick juice … Margoliouth, ERE, vi, 248, notes that رب meaning Lord or Master must have been borrowed from the Jews or Christians.'\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. rabbi\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.vv. رَبّ and رُبّ (Arabic)\", \"stance\": \"supports\", \"note\": \"both nouns are assigned to the Semitic root ر ب ب, رَبّ 'lord, master' < Proto-Semitic *rabb-, رُبّ 'thickened juice, syrup' from the same root.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"rab, rabb; morabbâ; robb\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Two of the three words are correct, one is not. (a) رَب/رَبّ rabb 'lord, master, God' is a straightforward Arabic loan in Persian (Qur'anic رَبّ), root ر ب ب — confirmed. (b) رُبّ robb 'thickened juice, concentrate' is likewise a loan of Arabic رُبّ, the very word Jeffery quotes as the native Arabic value of the root — confirmed. (c) مربّا morabbā 'jam' does NOT belong to ر ب ب: it is Arabic مُرَبَّى murabbā, the passive participle of the form-II verb رَبَّى rabbā 'to rear, raise; to preserve in sugar', whose root is ر ب و/ر ب ي, and the same goes for the words Nourai adds in the margin, مربّی morabbī 'tutor' and تربیت tarbiyat 'upbringing' (verbal noun تَرْبِيَة of the same رَبَّى). Classical Arabic lexicography does treat رَبَّ 'to rear' and رَبَّى as one semantic family, which is presumably why Nourai files them together, but the morphological root is different, and Wiktionary assigns مربا explicitly to 'the Arabic root ر ب و'. Of the margin words only ربّانی rabbānī and ارباب arbāb (plural of رَبّ) are genuinely ر ب ب.\",\n     \"derivation_fa\": \"از سه واژهٔ این جعبه دو تا درست است و یکی نه. «رَبّ» («خداوند، صاحب») وام‌واژهٔ سرراست عربی از ریشهٔ ر ب ب است؛ «رُبّ» («افشرهٔ غلیظ، رب انار و گوجه») نیز از همان ریشه و همان واژه‌ای است که جفری آن را نمونهٔ معنای بومیِ عربیِ ریشه می‌شمارد. اما «مربّا» به ریشهٔ ر ب ب نمی‌رسد: صورت عربیِ آن مُرَبَّی، اسم مفعولِ بابِ تفعیلِ «رَبَّی» (پروراندن، در شکر پروردن) از ریشهٔ ر ب و/ر ب ی است؛ همین حکم دربارهٔ «مربّی» و «تربیت» (مصدرِ تَرْبِیَة از همان رَبَّی) نیز صادق است. فرهنگ‌نویسان کهنِ عرب «رَبَّ» و «رَبَّی» را یک خانوادهٔ معنایی می‌گرفتند و شاید نورایی از همین‌رو آن‌ها را یک‌جا آورده، ولی ریشهٔ صرفی‌شان یکی نیست و ویکی‌واژه «مربا» را صریحاً به ریشهٔ ر ب و می‌بندد. از واژه‌های حاشیه تنها «ربّانی» و «ارباب» (جمعِ رَبّ) به‌راستی از ر ب ب اند. پژوهش امروزی این بخش از ادعای نورایی را رد می‌کند.\",\n     \"sources\": [W+\"%D9%85%D8%B1%D8%A8%D8%A7\", W+\"%D8%B1%D8%A8\"],\n     \"ref_check\": [\n      {\"ref\": \"VDQ:214\", \"status\": \"partial\", \"note\": \"via FVQ pp.136-137: Jeffery documents Arabic رَبّ 'Lord, master' (the Qur'anic word behind Persian رَب) and رُبّ 'thick juice', i.e. words (a) and (c) of the box, but says nothing that would attach مربّا/تربیت to r-b-b.\"},\n      {\"ref\": \"FVA:153,155\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e vāžehā-ye ʿarabi dar fārsi (1368) — refs_online.json records that no digital copy exists on any permitted platform (re-searched 2026-09), so pp.153 and 155 could not be seen.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. مربا (Persian)\", \"stance\": \"contradicts\", \"note\": \"'From Arabic مُرَبَّى (murabbā), from رَبَّى (rabbā), from the Arabic root ر ب و' — not ر ب ب.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. رب (Persian section)\", \"stance\": \"supports\", \"note\": \"two Persian etymologies, both borrowings from Arabic: رب (rab) 'the Lord, God' and رب (rob) from Arabic رُبّ 'concentrate, sauce'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. rabbi\", \"stance\": \"supports\", \"note\": \"'Arab. rabba ‚was great or dense‘, rabb ‚master‘' — covers rabb and robb, and says nothing of murabbā.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Aramaic\",\n     \"words\": \"rabb\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Aramaic/Syriac rab, emphatic rabbā (רַב, רַבָּא) 'great; chief, master, teacher' is the best-attested branch of the root and the pivot of the whole chart: Klein, 'Heb. rabh is rel. to Aram.-Syr. rabh, ‚great; chief, master, teacher‘'. Jeffery documents it in the Aramaic inscriptions in exactly the 'chief of X' titles the box glosses: 'rb šwq ‚chief of the market‘, rb ḥylʾ ‚chief of the army‘, rb mšryth ‚camp master‘'. Nourai's spelling 'rabb' with a doubled -bb is the Arabic-style geminate; the Aramaic absolute state is rab, the emphatic rabbā.\",\n     \"derivation_fa\": \"آرامی/سریانیِ rab، حالت مفعولِ rabbā (רַב، רַבָּא) «بزرگ؛ سرور، سرکرده، آموزگار» گواهی‌شده‌ترین شاخهٔ این ریشه و لولای کل نمودار است. کلاین می‌نویسد: «rabh عبری با rabh آرامی‑سریانی ‚بزرگ؛ سرور، آموزگار‘ خویشاوند است». جفری هم آن را در کتیبه‌های آرامی در همان ترکیب‌های «سرِ فلان» می‌آورد: «rb šwq ‚بازارسالار‘، rb ḥylʾ ‚سپه‌سالار‘، rb mšryth ‚اردوسالار‘». املای «rabb» با ب مشدد به شیوهٔ عربی است؛ صورت مطلقِ آرامی rab و صورت مفعولی rabbā است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/rabbi\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1293\", \"status\": \"supports\", \"note\": \"'Heb. rabh is rel. to Aram.-Syr. rabh, ‚great; chief, master, teacher‘, Akkad. rab, ‚chief, captain‘' (KLN_1966 block 689).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"p.137\", \"stance\": \"supports\", \"note\": \"'We find רב very frequently in the Aramaic inscriptions, e.g. rb šwq ‚chief of the market‘, rb ḥylʾ ‚chief of the army‘, rb mšryth ‚camp master‘ … The special development of its use with God was in the Syriac of the Christian communities.'\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"grep of AFA.txt for 'rabb' returns only 'Rabbi Samuel', 'rabbinische', 'Wajjikra Rabb.' and OCR noise ('arabbcher'); Fraenkel has no article on رب among the Aramaic loanwords he treats.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. rabban\", \"stance\": \"supports\", \"note\": \"'Aram. rabban, lit. ‚our teacher‘, fr. rabh, ‚master, teacher‘.'\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"raba\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"This is the Aramaic heterogram (ideogram) RBʾ / rabā, written in Book Pahlavi and in the Sasanian inscriptions but READ as the Iranian word wuzurg/vazurg 'great'. Jeffery says so in the very passage Nourai cites: 'it was from an Aram. source that the word passed into Middle Persian, as witness the Phlv. ideogram rabā meaning great, venerable, splendid (PPGl, 190; Frahang, Glossary, 106), which occurs as early as the Sasanian inscriptions, where it is synonymous with the Pāzand wuzurg.' MacKenzie writes the same heterogram LBA: 'wuzurg [LBA < A rbʾ; wc(w)lg | M wzrg, N buzurg] big, great', and Nyberg's list of heterograms has 'LBʾ: RABBĀ great, cf RBʾ' with the entry 'vazurg [LBʾ, Prth RBʾ; wzwrg, inscr. wclk-] great, big, high'. Nourai's note that the word entered Pahlavi in pre-Islamic times is exactly right (Achaemenid-Aramaic chancery practice, continued in the 3rd-century Sasanian inscriptions); the one thing worth adding is that it was never a spoken Middle Persian word — it is a logogram for wuzurg.\",\n     \"derivation_fa\": \"این صورت هُزوارشِ (ایدئوگرام) آرامیِ RBʾ / rabā است که در پهلویِ کتابی و کتیبه‌های ساسانی نوشته می‌شد اما واژهٔ ایرانیِ wuzurg/vazurg «بزرگ» خوانده می‌شد. جفری در همان صفحه‌ای که نورایی ارجاع داده می‌نویسد: «این واژه از سرچشمه‌ای آرامی به فارسی میانه راه یافته است، چنان‌که هُزوارشِ پهلویِ rabā به معنی بزرگ و ارجمند گواهی می‌دهد… که از کتیبه‌های ساسانی به این سو دیده می‌شود و هم‌ارزِ wuzurg پازند است». مکنزی همین را با نویسهٔ LBA می‌آورد: «wuzurg [LBA < آرامی rbʾ] بزرگ»، و نیبرگ در فهرست هزوارش‌ها: «LBʾ: RABBĀ بزرگ» و «vazurg [LBʾ، پارتی RBʾ]». یادداشت نورایی دربارهٔ ورودِ پیش از اسلامِ این واژه درست است؛ تنها باید افزود که این واژه هرگز واژهٔ گفتاریِ فارسی میانه نبوده، بلکه نویسه‌ای برای «وزرگ» است. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"VDQ:215\", \"status\": \"supports\", \"note\": \"checked through the original, FVQ p.137 (FVQ_pages.txt block 155): 'as witness the Phlv. ideogram rabā meaning great, venerable, splendid (PPGl, 190; Frahang, Glossary, 106), which occurs as early as the Sasanian inscriptions, where it is synonymous with the Pāzand wuzurg' — the source of both the form 'raba', the gloss and Nourai's pre-Islamic note.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. wuzurg\", \"stance\": \"supports\", \"note\": \"'wuzurg [LBA < A rbʾ; wc(w)lg | M wzrg, N buzurg] big, great' — the Aramaic heterogram spelled out.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, heterogram list and s.v. vazurg\", \"stance\": \"supports\", \"note\": \"'LBʾ: RABBĀ great, cf RBʾ'; 'vazurg [LBʾ, Prth RBʾ; wzwrg, inscr. wclk-] great, big, high, lofty … OP vazrka-; MPrth/MPrs wzrg; Paz. guzurg; NP buzurg' — and the Parthian inscriptional spelling RBʾ confirms pre-Islamic use.\"},\n      {\"src\": \"FVQ\", \"where\": \"p.137\", \"stance\": \"supports\", \"note\": \"quoted above.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": null,\n     \"words\": \"\",\n     \"verdict\": \"unverified\",\n     \"derivation\": \"Empty pass-through box: the printed page really does show a blank double-ruled frame to the right of the Pahlavi 'raba' box, with an arrow pointing into it and no language label, no word and no reference. I rendered pdf page 415 at 300 dpi and cropped the area to be sure (copy kept at data/verification/sources/refs/ocr/BOOK/415.png); the extraction is faithful, the blank is the book's own — presumably a New Persian box the author left unfilled. There is nothing to verify. If a word were expected there it would be Persian بزرگ or a title such as رب/ارباب, but that is guesswork and is not asserted.\",\n     \"derivation_fa\": \"جعبهٔ تهی: در صفحهٔ چاپی، کنارِ جعبهٔ پهلوی «raba» یک قاب دوخطی کاملاً خالی با پیکانی به‌سویش دیده می‌شود، بی‌نام زبان، بی‌واژه و بی‌ارجاع. تصویر صفحه را با تفکیک ۳۰۰ نقطه بر اینچ برگرداندم و همان ناحیه را بزرگ کردم تا مطمئن شوم: استخراج داده وفادار است و این تهی‌بودن از خودِ کتاب است (احتمالاً جعبهٔ فارسی نو که نویسنده پر نکرده). پس چیزی برای سنجیدن نیست؛ نه خطای خوانش اسکن است و نه ادعایی که بتوان دربارهٔ آن داوری کرد.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BOOK\", \"where\": \"pdf page 415, 300 dpi render, right-hand box of the Aramaic/Pahlavi row\", \"stance\": \"silent\", \"note\": \"blank double-ruled frame, no text; image saved as data/verification/sources/refs/ocr/BOOK/415.png.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Hebrew\",\n     \"words\": \"r.b.b; rabh; rabbi\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All three items are Klein's, verbatim: Hebrew stem r-b-b 'to be great or numerous'; רַב rabh 'much, many, great', whence the Mishnaic noun rabh 'chief, master, teacher'; and רַבִּי rabbī 'my master', rabh plus the 1st-person singular pronominal suffix -ī, used from the Mishnaic period as a title of address for a teacher of the Law (Matt. 23:7-8 records the usage). Klein also derives from the same stem robh 'multitude', rebhābhāh 'ten thousand', ribbō 'myriad'.\",\n     \"derivation_fa\": \"هر سه واژه از مدخلِ کلاین‌اند: ستاکِ عبریِ r-b-b «بزرگ یا بسیار بودن»؛ رَب (רַב) «بسیار، بزرگ» که در عبریِ میشنایی به معنای «سرور، آموزگار» به کار رفته؛ و رَبّی (רַבִּי) «سرورِ من»، یعنی rabh + پسوندِ ضمیریِ اول‌شخص مفرد ‑ی، که از دورهٔ میشنا عنوانِ خطاب به آموزگارِ شریعت بوده است (انجیل متی ۲۳:۷–۸ همین کاربرد را ثبت کرده). کلاین از همین ستاک robh «انبوهی»، rebhābhāh «ده‌هزار» و ribbō «بی‌شمار» را نیز می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/rabbi\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1293\", \"status\": \"supports\", \"note\": \"'Mishnaic Heb. rabbī, ‚my master‘, title of respect, formed with -ī, pronom. suff. of the 1st person in the singular, fr. rabh, ‚chief, master, teacher‘, which derives fr. Heb. rabh, ‚much, many, great‘, from stem r-b-b, ‚to be great or numerous‘.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. rabbi and s.v. Jeroboam\", \"stance\": \"supports\", \"note\": \"s.v. Jeroboam Klein cites the same 'base r-b-b, ‚to become many, to increase‘' for the Hebrew verb yārōbh.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. rabbi\", \"stance\": \"supports\", \"note\": \"'Semitic root r-b-b ‚to be great or numerous‘ … Hebrew rabbi ‚my master‘, from rabh ‚master, great one‘ + -i, first person singular suffix.'\"},\n      {\"src\": \"FVQ\", \"where\": \"pp.137-138\", \"stance\": \"supports\", \"note\": \"Jeffery on Arabic ربّانی: 'Geiger, 51, would derive it from the Rabbinic rbn, a later form of rby used as a title of honour for distinguished teachers.'\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Greek\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through box; the word intended is Greek ῥαββί (rhabbí), the New Testament transliteration of Mishnaic Hebrew rabbī (Matt. 23:7-8; John 1:38 'Ῥαββί, ὃ λέγεται … Διδάσκαλε'), beside the Aramaic-based ῥαββουνί (Mark 10:51, John 20:16) which Jeffery discusses. Greek had no way of writing the Semitic gemination other than -ββ-, and the initial ῥ- carries the rough breathing automatically. Klein's chain 'Late L., fr. Gk., fr. Mishnaic Heb. rabbī' is exactly this step.\",\n     \"derivation_fa\": \"جعبهٔ گذرِ تهی؛ واژهٔ مورد نظر یونانیِ ῥαββί (rhabbí) است، آوانگاشتِ عهد جدید از rabbī عبریِ میشنایی (متی ۲۳:۷–۸؛ یوحنا ۱:۳۸)، در کنار صورتِ آرامی‌بنیادِ ῥαββουνί (مرقس ۱۰:۵۱، یوحنا ۲۰:۱۶) که جفری از آن سخن می‌گوید. یونانی برای نمایشِ تشدیدِ سامی چاره‌ای جز ‑ββ‑ نداشت و ῥ آغازین نیز خودبه‌خود دمِ درشت می‌گیرد. زنجیرهٔ کلاین («لاتینیِ متأخر، از یونانی، از عبریِ میشنایی rabbī») دقیقاً همین گام است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/rabbi\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference of its own; it is covered by the KLN:1293 citation of the English box.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. rabbi\", \"stance\": \"supports\", \"note\": \"'rabbi, n. — Late L., fr. Gk. ῥαββί, fr. Mishnaic Heb. rabbī.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. rabbi\", \"stance\": \"supports\", \"note\": \"'Greek rhabbi — direct transliteration from Hebrew.'\"},\n      {\"src\": \"FVQ\", \"where\": \"p.138\", \"stance\": \"supports\", \"note\": \"'In Jno. xx, 16; Mk. x, 51, we find the form ῥαββουνί … which seems to be formed from the Targumic rbwn.'\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Latin\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through box for Late Latin rabbī, the form of the Vulgate and of the Latin Fathers, taken over unchanged from Greek ῥαββί (Jerome renders John 1:38 'Rabbi, quod dicitur interpretatum Magister'). It is an ecclesiastical borrowing of the 4th-5th century, not an inherited Latin word, which is why it keeps the Semitic shape intact. Klein: 'Late L., fr. Gk.'; Medieval Latin also formed rabbinus, whence French rabbin and English rabbin.\",\n     \"derivation_fa\": \"جعبهٔ گذرِ تهی برای لاتینیِ متأخرِ rabbī، صورتِ ولگات و پدران کلیسا، که بی‌هیچ دگرگونی از یونانیِ ῥαββί گرفته شده است (ژروم در یوحنا ۱:۳۸ می‌آورد: «Rabbi, quod dicitur interpretatum Magister»). این وام‌واژه‌ای کلیسایی از سدهٔ چهارم–پنجم میلادی است، نه واژه‌ای موروثی در لاتینی، و از همین‌رو ساختِ سامیِ خود را دست‌نخورده نگاه داشته است. کلاین: «لاتینیِ متأخر، از یونانی»؛ در لاتینیِ میانه صورتِ rabbinus نیز ساخته شد که فرانسویِ rabbin و انگلیسیِ rabbin از آن است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/rabbi\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference in the box; covered by KLN:1293 on the English box.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.vv. rabbi, rabbin\", \"stance\": \"supports\", \"note\": \"'rabbin, n., rabbi. — F. rabbin or ML. rabbinus, fr. Late L. rabbi.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. rabbi\", \"stance\": \"supports\", \"note\": \"'Latin rabbi (Late Latin) — borrowed from the Greek form.'\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"English\",\n     \"words\": \"rabbi\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English rabbi is a learned biblical borrowing: it appears in late Old English only in scriptural contexts as a form of address, and as an ordinary noun from the early 14th century, always through Late Latin rabbī (Vulgate) from Greek ῥαββί from Mishnaic Hebrew rabbī 'my master'. The literal sense 'my master' is fossilised — English rabbi never means 'my' anything, the possessive suffix having been lexicalised in the Hebrew title itself. The by-form rabbin (1520s) via French rabbin/ML rabbinus gave the adjective rabbinical (1610s-20s). Nourai's gloss 'my master, my teacher, a Jewish title of respect' is Klein's wording.\",\n     \"derivation_fa\": \"«rabbi» در انگلیسی وام‌واژه‌ای کتاب‌مقدسی و کتابی است: در انگلیسیِ باستانِ متأخر تنها در بافتِ کتاب مقدس و به‌عنوان صورتِ خطاب دیده می‌شود و از آغاز سدهٔ چهاردهم اسمِ معمولی می‌شود؛ راهش همواره از لاتینیِ متأخرِ rabbī (ولگات) از یونانیِ ῥαββί از rabbī عبریِ میشنایی «سرورِ من» بوده است. معنای تحت‌اللفظیِ «سرورِ من» سنگ‌واره شده است، زیرا پسوندِ ملکی در خودِ عنوانِ عبری واژگانی شده بود. صورتِ دیگرش rabbin (دههٔ ۱۵۲۰) از راه فرانسوی و لاتینی میانه، صفتِ rabbinical را پدید آورد. معنایی که نورایی آورده عیناً واژه‌های کلاین است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/rabbi\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1293\", \"status\": \"supports\", \"note\": \"Klein's article s.v. rabbi (KLN_1966 block 689 = printed pp.1293-1295) gives the whole chain and the gloss 'my master, title of respect'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. rabbi\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. rabbi\", \"stance\": \"supports\", \"note\": \"'in late Old English in biblical context only, as a form of address'; as a noun 'early 14c.'; rabbin 1520s; rabbinical 1610s-1620s.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt for 'Rabbi' returns nothing — Skeat's concise edition has no entry for the word.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary vol. 3\", \"stance\": \"silent\", \"note\": \"the R pages are present (rabbit, rabbi-ra'bi-a etc. at line 211914) but the OCR of the 'rab'bi' entry itself is unreadable, so nothing usable could be quoted.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-415.json\"\nwith open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-415.py"
}
```


### [2026-09-14T01:24:05.009Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-415.py", line 228, in <module>
    "lang": null,
            ^^^^
NameError: name 'null' is not defined
```


## [2026-09-14T01:24:08.243Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && sed -i 's/\"lang\": null,/\"lang\": None,/' build-415.py && python3 build-415.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-415.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 415"
}
```


### [2026-09-14T01:24:09.514Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-415.json
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 10, 'plausible': 2, 'disputed': 1, 'unverified': 1}
root verdicts: {'plausible': 3}
ref checks: {'partial': 4, 'supports': 7, 'not_checked': 7}
books consulted: {'supports': 29, 'silent': 7, 'partial': 3, 'contradicts': 1} | by book: {'KLN': 7, 'FVQ': 5, 'Wiktionary': 4, 'Etymonline': 4, 'PHD': 3, 'NYB': 3, 'CHEUNG': 3, 'HRN': 2, 'MON': 2, 'ARY': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'AFA': 1, 'BOOK': 1, 'SKT': 1, 'FSD': 1}
```


## [2026-09-14T01:24:25.401Z] AGENT

Done. `data/verification/page-415.json` written; `verify_check.py 415` reports 14/14 nodes, 0 PROBLEM lines.

**Page 415 (book p. 385) — 3 non-redirect entries, 14 nodes**
- Root verdicts: plausible 3
- Node verdicts: confirmed 10, plausible 2, disputed 1, unverified 1
- Ref checks: supports 7, partial 4, not_checked 7 (ISS = Bailey, *Khotanese Texts VI*, not online — substance checked in his *Dictionary of Khotan Saka*; VDQ is JS-only on noorlib — checked through Jeffery FVQ, the original; FVA has no digital copy anywhere)

Flagged items:
- **disputed — R.b.b, node #2 (Persian مربّا morabbā)**: مربا (and the margin words مربّی، تربیت) are Arabic مُرَبَّى / تَرْبِيَة from رَبَّى, root **ر ب و**, not ر ب ب; رَبّ and رُبّ in the same box are correct.
- No `transcription_suspect` nodes; no extraction errors. Two things the owner may still want to know:
  - Node #5 of R.b.b is genuinely a **blank box in the printed book** (verified on a 300-dpi render, saved to `data/verification/sources/refs/ocr/BOOK/415.png`) — the JSON is faithful.
  - "Indo-Schythian" is the book's own spelling (13 occurrences corpus-wide), not a scan error.

Other substantive notes carried in the file: the root **Raika** is Hübschmann's reconstruction *ap. \*raika-* (Pers. Studien p.68), unattested in Old Persian and printed without an asterisk; modern work takes it from PIE \*h₃reyH-. **Raud** as a variant of **Raup** "to sweep" is unsupported (Bailey's raup-/raud- pairing belongs to the 'rise, raised place' family). Sogdian *rwp* attests 'gather/reap', 'sweep' only with a preverb (pr'wp-). Pahlavi *raba* is confirmed as the Aramaic heterogram RBʾ/LBA read *wuzurg* (MacKenzie, Nyberg, Jeffery). Page-number slips in Nourai's citations: PHD:73 → the entry rēg is on p.71; BQT:989 → Mo'in's footnote sits ~2-3 pages later in the vol. 2 scan.
