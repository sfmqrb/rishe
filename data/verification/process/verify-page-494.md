# Verification process log — verify-page-494


## [2026-09-14T03:08:48.695Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 494 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-494.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-494.json. Write /home/sfmqrb/git/rishe/data/verification/page-494.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 494` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:49.750Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:50.485Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:50.499Z] TOOL RESULT

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


## [2026-09-14T03:08:51.032Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-494.txt"
}
```


### [2026-09-14T03:08:51.060Z] TOOL RESULT

```
1	=== PDF page 494 (book page 464) ===
2	--- entry 0 ---
3	ROOT [Caribian] Tabaco : a pipe for smoking, roll of tobacco leaves  (refs KLN:1623)
4	#1 (parent #0) [Persian] refs=MON:1147 | tanbâkŭ «تنباکو ( تمباکو )» : tobacco
5	#2 (parent #0) [Hindustani] refs=KLN:1623 | tambâka : tobacco
6	#3 (parent #0) [Portuguese] refs=KLN:1623 | tabaco
7	  #4 (parent #3) [Spanish] refs=KLN:1623 | tabaco | NOTE: AHD:1350 claims this Spanish word is probably from Arabic "tabâq: a euphoria-causing herb".
8	    #5 (parent #4) [English] refs=KLN:1623; AHD:1350 | tobacco
9	    #6 (parent #4) [French] refs=KLN:1623 | tabac : tobacco ; tabaquiere : snuffbox
10	      #7 (parent #6) [English] refs=KLN:1563 | tabatiere : snuffbox
11	--- entry 1 ---
12	ROOT [Pahlavi] Tabŭrâk : a drum  (refs MON:1025)
13	#1 (parent #0) [Persian] refs=MON:1025 | tabŭrâk «تبوراک ( تبیر ، تبیره )» : a kind of drum
14	  #2 (parent #1) [Arabic] refs=DEV:215; AHD:1313 | tanbŭr : a drum, also a kind of stringed musical instrument
15	    #3 (parent #2) [Persian] refs=MON:1147 | tanbŭr «تنبور ( طنبور )» : a stringed musical instrument ; tonbak «تنبک ( طنبک ، دُنبک )» : a musical drum
16	    #4 (parent #2) [Arabic] refs=DEV:215 | tabŭl : drum ; tabbâl : drummer
17	      #5 (parent #4) [Persian] refs=VFO:23; MON:2211 | tabl «طبل ( طبّال )» : drum
18	    #6 (parent #2) [Old French] refs=None | 
19	      #7 (parent #6) [English] refs=AHD:1025 | tambour ; tambourine ; tambour
20	  #8 (parent #1) [Old French] refs=AHD:1303 | 
21	    #9 (parent #8) [English] refs=AHD:1303 | tabor : a kind of drum ; taboret : a round low stool
22	
```


## [2026-09-14T03:08:52.328Z] AGENT

I'll look at the source JSON and the reference infrastructure.


## [2026-09-14T03:08:53.735Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-494.json",
 "description": "Read source JSON page 494"
}
```


### [2026-09-14T03:08:53.781Z] TOOL RESULT

```
{
  "pdf_page": 494,
  "book_page": 464,
  "entries": [
    {
      "root": {
        "name": "Tabaco",
        "lang": "Caribian",
        "refs": "KLN:1623",
        "gloss": "a pipe for smoking, roll of tobacco leaves"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:1147",
          "words": [
            {"translit": "tanbâkŭ", "gloss": "tobacco", "script": "تنباکو ( تمباکو )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Hindustani",
          "refs": "KLN:1623",
          "words": [
            {"translit": "tambâka", "gloss": "tobacco", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Portuguese",
          "refs": "KLN:1623",
          "words": [
            {"translit": "tabaco", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Spanish",
          "refs": "KLN:1623",
          "words": [
            {"translit": "tabaco", "gloss": null, "script": null}
          ],
          "note": "AHD:1350 claims this Spanish word is probably from Arabic \"tabâq: a euphoria-causing herb\".",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:1623; AHD:1350",
          "words": [
            {"translit": "tobacco", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "French",
          "refs": "KLN:1623",
          "words": [
            {"translit": "tabac", "gloss": "tobacco", "script": null},
            {"translit": "tabaquiere", "gloss": "snuffbox", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "KLN:1563",
          "words": [
            {"translit": "tabatiere", "gloss": "snuffbox", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Tabŭrâk",
        "lang": "Pahlavi",
        "refs": "MON:1025",
        "gloss": "a drum"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:1025",
          "words": [
            {"translit": "tabŭrâk", "gloss": "a kind of drum", "script": "تبوراک ( تبیر ، تبیره )"}
          ],
          "note": null,
          "quote": {
            "text": "پس تبیری دید نزدیک درخت - هرگهی بانگی بجستی تند و سخت",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "DEV:215; AHD:1313",
          "words": [
            {"translit": "tanbŭr", "gloss": "a drum, also a kind of stringed musical instrument", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:1147",
          "words": [
            {"translit": "tanbŭr", "gloss": "a stringed musical instrument", "script": "تنبور ( طنبور )"},
            {"translit": "tonbak", "gloss": "a musical drum", "script": "تنبک ( طنبک ، دُنبک )"}
          ],
          "note": null,
          "quote": {
            "text": "عیسیٰ چو تویی مارا هم کاسهٔ مریم کن - طنبور دل مارا هم نالهٔ سرنا کن",
            "poet": "Molavî"
          }
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Arabic",
          "refs": "DEV:215",
          "words": [
            {"translit": "tabŭl", "gloss": "drum", "script": null},
            {"translit": "tabbâl", "gloss": "drummer", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "VFO:23; MON:2211",
          "words": [
            {"translit": "tabl", "gloss": "drum", "script": "طبل ( طبّال )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 2,
          "lang": "Old French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD:1025",
          "words": [
            {"translit": "tambour", "gloss": null, "script": null},
            {"translit": "tambourine", "gloss": null, "script": null},
            {"translit": "tambour", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 1,
          "lang": "Old French",
          "refs": "AHD:1303",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD:1303",
          "words": [
            {"translit": "tabor", "gloss": "a kind of drum", "script": null},
            {"translit": "taboret", "gloss": "a round low stool", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T03:08:56.444Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','MON','DEV','AHD','VFO','POK','PHD','NYB','HRN','HUB','BQT','ARY','SKT','WEB','FSD','LKT','PHN','LAM','DOZ','FVQ','AFM','PLA','AFA','HJB','AID','TTS','SYN','IEC','WLD']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T03:08:57.515Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
VFO MISSING
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
```


## [2026-09-14T03:09:01.596Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(sorted(d.keys()))\n\" ; grep -rn \"VFO\" --include=*.md --include=*.json data/verification/ | head -20"
}
```


## [2026-09-14T03:09:02.277Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T03:09:02.681Z] TOOL RESULT

```
['AEF', 'AFA', 'AFM', 'AHD', 'AHM', 'AID', 'AIN', 'AKD', 'AKM', 'AMD', 'ARB', 'ARK', 'ARM', 'ARP', 'ARY', 'AVG', 'AWH', 'BLY', 'BQT', 'BRT', 'BST', 'CEL', 'DEV', 'DMO', 'DOZ', 'DRM', 'DVS', 'DZA', 'EAV', 'ETM', 'FAF', 'FFD', 'FIB', 'FNI', 'FRS', 'FSD', 'FSF', 'FVA', 'FVF', 'FVQ', 'FVS', 'FWE', 'GPL', 'HID', 'HJB', 'HRN', 'HUB', 'IEC', 'IRN', 'IRT', 'ISS', 'KAS', 'KFL', 'KGW', 'KLN', 'KNT', 'LAM', 'LAT', 'LEW', 'LKT', 'LST', 'MAG', 'MFL', 'MMF', 'MON', 'MPP', 'MZF', 'NAT', 'NFI', 'NYB', 'OEW', 'OXF', 'PEI', 'PHD', 'PHN', 'PLA', 'POK', 'PRT', 'RCH', 'ROE', 'SAP', 'SBK', 'SDQ', 'SHP', 'SIN', 'SKT', 'SLW', 'SNB', 'SNS', 'SOD', 'SOG', 'SOR', 'SPG', 'SYN', 'TAD', 'TLM', 'TTS', 'TYL', 'TZF', 'UNV', 'VDQ', 'VGH', 'VIE', 'VOP', 'VSF', 'WEB', 'WLD', 'ZAP', 'ZAW', 'ZFS', 'ZMA']
(eval):5: no matches found: --include=*.md
```


### [2026-09-14T03:09:02.732Z] TOOL RESULT

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


## [2026-09-14T03:09:12.699Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re,io\nf='KLN_1966.txt'\nt=open(f,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('KLN pages',len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'\\btobacco\\b',p,re.I):\n        print('leaf',i+1,'tobacco')\nEOF"
}
```


## [2026-09-14T03:09:13.797Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"tambour\\|tabour\\|tanbour\\|tabl\\b\" DEV.txt | head -40"
}
```


### [2026-09-14T03:09:14.313Z] TOOL RESULT

```
KLN pages 903
leaf 133 tobacco
leaf 136 tobacco
leaf 145 tobacco
leaf 156 tobacco
leaf 157 tobacco
leaf 163 tobacco
leaf 262 tobacco
leaf 267 tobacco
leaf 320 tobacco
leaf 400 tobacco
leaf 457 tobacco
leaf 467 tobacco
leaf 492 tobacco
leaf 545 tobacco
leaf 560 tobacco
leaf 620 tobacco
leaf 624 tobacco
leaf 694 tobacco
leaf 760 tobacco
leaf 779 tobacco
leaf 793 tobacco
leaf 829 tobacco
leaf 861 tobacco
```


### [2026-09-14T03:09:14.390Z] TOOL RESULT

```
344:/i3.  Nohach,  lambour  employé  par  les  nécromanciens; du  persan  ooy  nôhat,  sorte  de  tambour.
514:Cet  instrument  jouait  un  rôle  important  dans  le  céré- monial de  la  cour  des  princes  malais  avec  le  tambour, ^ùjS  gancloung ,  la  flûte,  cbr^  saroûni,  les  cymbales, ^Isi nagâra,  etc.  (Voir  le  Chedjarat  malmjou,  p.  IF'^.)
1826:Nacaire.  Ancien  instrument  de  musique  militaire,  sorte de  tambour  ou  de  timbale.  Ital.  gnaccare  (qui  est  le  gna- care  de  Molière,  dans  la  Pastorale  comique);  bas  latin,  na- cara;  bas  grec,  oLvaxapa.  Ce  n'est  point,  comme  on  l'a dit.  l'arabe -AAj  naqJr  ouj^U  nâqdr,  qui  signifient  trom- pette, clairon,  mais  le  persan  s^Uj,  en  arabe  H^ixj  naqâra, timbale  \  Arabe  ou  persan,  le  mot  a  pénétré,  en  conser- vant sa  signification,  non-seulement  en  Europe,  mais aussi  dans  une  partie  de  l'Afrique,  notamment  en  Abys- sinie  et  chez  les  Latoukas  des  bords  du  Nil  Blanc,  au  sud de  Gondokoro ,  comme  on  peut  le  voir  par  les  passages suivants  :  r^  Cependant  la  grande  tymbale  ou  nagareet , qu'on  appelle  le  Lion,  fut  portée  devant  le  palais,  w  (Bruce  , Voyage  en  Nubie,  édit.  Panckouke,  t.  III,  p.  -^iq).  — rt Un  jour,  les  nogaras  battent,  les  trompettes  sonnent,  w (Sam.  White  Baker,  Voyage  à  l'Albert  Nianza,  dans  le  Tour (lu  Monde ^  i'"'^  sem.  1867,  p.  i  5.)
1827:Le  nacaire  faisait  aussi  partie  de  la  musique  royale  des princes  malais  de  Malacca  :  ^;U^:>yi  ^U^^  cy;^^  dU^ yS<>  t^y^Àj  (j^yw  ^<Xo  jjplswyS  ojÎ  /«.aXaUv  (j"ii^  c>À^i  rcSl la  lettre  venait  de  Pasey  ou  de  Harau,  elle  était  reçue avec  tout  l'appareil  royal,  tambour,  flûte,  trompette,  na-
1828:'  Bocthor,  aux  mots  tambour  et  timbale ,  écrit  i\Li3  par  un  double  (^  q, iiarjqâra.  Pauthier,  dans  son  édition  de  Marco  Polo  (t.  P',  p.  2/i5)  compare iitifjâra  au  sanscrit  anakali.
2178:Tambour.  Esp.  tambor,  alambor,  portug.  tambor,  ital. tamburo.  On  disait  autrefois  taboiir  ou  tabur  (comme  aussi labour  in  au  lieu  de  tambouriny.  M.  Dozy  repousse  l'éty- mologie  arabe  ;^^1^  tonboUr,  proposée  par  Engelmann; ce  mot,  au  moyen  âge,  désignait,  dit-il,  une  espèce  de Ivre;  et  si  les  Barbaresques  ont  aujourd'hui  un  grand  tam- bour appelé  ])ar  eux  atambor,  c'est  qu'ils  l'ont  emprunté aux  Espagnols^.  Niebuhr  dit  en  effet  que,  chez  les  Arabes, tanibura  est  le  nom  générique  commun  à  tous  les  instru- ments à  cordes.  Mais  il  convient  de  remarquer  que  ces  ins- truments à  cordes  ne  sont  pas  sans  analogie  avec  les  tam- bours et  les  timbales ,  car  ils  sont  d'ordinaire  formés  d'un corps  creux  sur  lequel  est  tendue  une  peau.  Niebuhr  en décrit  quatre  ou  cinq  de  ce  genre  ^.
2181:-  Les  formes  labour,  tahourin  existent  encore  en  anglais,  où  Ton  trouve aussi  tabrel  et  tabouret.
2185:sens  esl  bien  lamhour,  timbale^  et  qui  est  assurément  iden- tique à  notre  tabnr,  tabour  (on  sait  avec  quelle  facilité  tel Il  (om)  se  remplacent).  Est-ce  le  persan  qui  est  passé  au français  ou  le  français  qui  a  pénétré  en  Orient?  Tabur  est bien  ancien  dans  notre  langue,  puisqu'on  le  trouve  déjà dans  la  chanson  de  Roland,  qui  est  du  xf  siècle;  mais  il est  bien  ancien  aussi  en  persan,  puisqu'il  se  lit  dans  le Chah-nameh,  dont  l'auteur  Firdouci  est  mort  en  l'an  1020: Jlo  Jsj^y  \J^-{J^')  »y^j^ [Chrest. Schanam.  deVullers,p.  58, vers  /i2  1  ).
2186:Les  formes  tambour,  )y^^  tonbour,  sont  certainement des  altérations  de  tabour,  y^j^s  tabir.  Le  persan  a  la  voyelle ou  dans  dî;^'  taboîirâk,  tambourin,  lequel  est,  suivant toute  vraisemblance,  un  diminutif  de  ^y^  tabour,  dans  le- quel s'est  gbssé  fautivement  un  \  â.  (Compar.  dUJ  et  vi)!^  ; voy.  au  mot  Ln.AS.)
2219:Timbale.  Esp.  hmhal,  atamhal,  atahal,  portug.  timbale, alabale ,  ital.  timbaUo ,  taballo.  De  l'arabe  J^b  tabl,  avec l'article  at-tabl,  sorte  de  tambour.  Il  s'est  glissé  un  m  avant le  b ,  comme  dans  labour  devenu  tambour.  Il  est  vraisem- blable du  reste  que  les  formes  timbale,  timbal,  timbaUo, ont  subi  l'influence  du  latin  tympaniim  (Ti^piTraroi^).  Tabl est  d'origine  persane.  On  trouve  un  pluriel  grec  ra^aXa, tç tambour,    timbale  dont   les    Partbes  se  servaient  à  la
2832:Atambor,  esp.  voy.  Tambour.
4383:Tabour,  voy.  Tambour.
4384:Tabur,  voy.  Tambour.
4402:Tambor,  hisp.  voy.  Tambour.
4404:Tambura,  voy.  Tambour. Tamburo,  ital.  voy.  Tambour. Tandoi  p.. Tanzimat.
4685:jK^pers.  voy.  Tambour.
4686:y^  pers.  voy.  Tambour.
4933:iolb  vo\.  Patard. yÀh  voy.  Altaïr. ^-j-iLb  voy.  Tabaschir. J-^i^  voy.  Timbale. iCa^!^  voy.  JMatelas. ^^.jo  voy.  Tarbouch. i^pjc:  voy.  Estragon. ^^  voy.  Matelas. 'is^jo  voy.  Tare. ^jl^Jui.:^^  voy.  Taraxacuin. i^^j^  voy.  Estragon. i^^j^jo  voy.  Taraxacum. ■pioJû  voy.  Tartre. *UJ:>  voy.  Téréniabin. ^^  voy.  Matraca. JJo  voy.  Tasse. ,c«-ik>  voy.  Talisman, ^  voy.  Talc. \y^  voy.  Tambour. A«i)^  turc ,  voy.  Doliman.
```


## [2026-09-14T03:09:23.122Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','DEV','MON','AHD','LKT','PHN','LAM','DOZ','HJB','AID','TTS','PLA','AFM','TAD','ARB','SKT','FSD','WEB']:\n    v=d[k]\n    print('=== ',k)\n    for f in ['page_offset','lookup_hint','local_file','scans','cites']:\n        if f in v: print(' ',f,':',json.dumps(v[f],ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-14T03:09:24.182Z] TOOL RESULT

```
===  KLN
  page_offset : "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt"
  cites : "page number, continuous across the two volumes (1966–67)"
===  DEV
  page_offset : "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "French headword in caps at line start."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt"
===  MON
  page_offset : null
  lookup_hint : "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded 
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"]
  cites : "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
===  AHD
  page_offset : "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page."
  lookup_hint : "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt"
  cites : "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
===  LKT
  page_offset : "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt"
  cites : "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"
===  PHN
  page_offset : "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt"
===  LAM
  page_offset : "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "French headword in caps at line start with running heads like '2 ABRI'."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt"
===  DOZ
  page_offset : "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Dutch headword in caps at line start."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt"
===  HJB
  page_offset : "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt"
  cites : "page number of Hobson-Jobson (1903 ed.)"
===  AID
  page_offset : "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Headword in bold at line start; grep -n '^Word'."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt"
===  TTS
  page_offset : "TTS_pages.txt: 253 leaves; printed page N = leaf N+30."
  lookup_hint : "Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books."
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"]
===  PLA
  page_offset : "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276)."
  lookup_hint : "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"]
  scans : [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "first_printed": 1, "last_printed": 300, "pdf_offset": 0, "lang": "deu+ara"}]
  cites : "page number of Asbaghi, Persische Lehnwörter im Arabischen (1988), alphabetical by Arabic word"
===  AFM
  page_offset : "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image"
  lookup_hint : "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير')."
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"]
  cites : "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
===  TAD
  page_offset : "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image"
  lookup_hint : "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works."
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"]
===  ARB
  page_offset : null
  lookup_hint : "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image."
  local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt"]
===  SKT
  page_offset : "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt"
  cites : "page number of Skeat, Concise Etymological Dictionary"
===  FSD
  page_offset : "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt"
  cites : "page number of Funk & Wagnalls New Standard Dictionary (1940)"
===  WEB
  page_offset : "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  lookup_hint : "Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies."
  local_file : "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt"
  cites : "page number of Webster's New Twentieth Century Dictionary, 2nd ed."
```


## [2026-09-14T03:09:29.347Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(818,830):\n    p=t[i]\n    if 'tobacco,' in p or 'tobacco' in p.lower():\n        print('--- leaf(0based)',i,'1based',i+1)\n        print(p[:1500])\nEOF"
}
```


### [2026-09-14T03:09:30.523Z] TOOL RESULT

```
--- leaf(0based) 828 1based 829
  —  A  hybrid  coined  fr. syphilis  and  -ous,  a  suff.  of  Latin  origin.
syren,  n.  —  See  siren.
Syria,  n.,  name  of  a  country  in  Asia  on  the  Med¬ iterranean  Sea.  —  L.  Syria,  fr.  Gk.  Supla,  ‘Sy¬ ria’,  fr.  Eupiot,  ‘the  Syrians’,  a  name  orig.  given to  the  Assyrians  (see  Herodotus  7,  63),  Suptoi being  an  aphetic  form  of  ’Aaaupiot,,  ‘Assyr¬ ians’,  fr.  ’Aaaupta,  ‘Assyria’.  See  Assyria.
Syriac,  adj.  and  n.,  (pertaining  to)  the  Syrian  lan¬ guage. — L.  SynacMi,  ‘Syrian’,  fr.  Gk.  Suptaxip, fr.  Hop: a.  See  prec.  word  and  -ac.
Syriacism,  n.,  a  Syriac  idiom.  —  See  Syriac  and -ism  and  cp.  Syriasm.
Syrian,  n.  and  adj.  —  ME.  sirien,  fr.  MF.  Sirien (F.  Syrieri),  formed  with  suff.  -ien  fr.  L.  Syrius, ‘Syrian’,  fr.  Syria.  See  Syria  and  -an  and  cp. sorghum.
Syriasm,  n.,  a  Syriac  idiom.  —  Formed  fr.  Gk. Supia^stv,  a  supposed  var.  of  Zupipetv,  ‘to speak  Syriac’,  fr.  Siipop,  ‘Syrian’.  See  Syro-.
syring-,  form  of  syringo-  before  a  vowel.
Syringa,  n.,  a  genus  of  plants:  1)  the  mock  or¬ ange;  later  applied  to  2)  the  lilac.  —  ModL.,  fr. Gk.  aupiv?,  gen.  auptyyop,  ‘pipe,  tube’;  the mock  orange  was  so  called  in  allusion  to  the  use of  its  hollow  stems  for  making  pipes.  See  next word  and  cp.  seringa.
syringe,  n.,  a  narrow  tube  for  injecting  a  liquid  in a  stream.  —  ML.  siringa,  syringa,  fr.  Gk. auptyi;,  gen.  auptyy
```


## [2026-09-14T03:09:31.028Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('DEV.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,p in enumerate(t):\n    if 'Tambour.' in p or 'Timbale.' in p:\n        print('=== leaf0',i,'leaf1',i+1)\n        print(p[:3000])\nEOF"
}
```


### [2026-09-14T03:09:32.090Z] TOOL RESULT

```
leaves 326
=== leaf0 249 leaf1 250
  quand  on  l'agite  (^taf  taJY-
Talc.  Esp.  ialcOj  talque,  portug.  talco.  En  arabe,  (^^ talq.  Je  ne  sais  qui  avait  proposé  l'étymologie  allemande talg,  suif,  qu'on  trouve  mentionnée  par  Léman  (^Dict.  dliist. 7iat.  t.  XXXII,  p.  378).  Le  mot  ^^-U©  se  rencontre  dans  l'al- chimie de  Géber,  notamment  au  chapitre  vu  du  IL  livre. ^Talcum,  vox  esse  Arabica  creditur,  significans  stellulas micantes55,  dit  Martin  Ruland^^.  J'ignore  à  quelle  expres- sion arabe  cette  explication  peut  faire  allusion.
Talisman.  C'est  l'arabe  xwAk>  telesm  ou  telsam,  (|ui  re- présente le  grec  TeXeo-jua,  initiation,  mystère.
Talmud.  Grand  ouvrage  qui  contient  un  recueil  des  lois, traditions,  coutumes  des  Juifs.  En  hébreu ,  TiD^n  ^^/rnoW, instruction,  du  verbe  l'ob  hmiul,  apprendre,  ïovmQ  ptli. ilpb  Immad,  enseigner.
Tamarin.   Esp.  et  portug.  tamarindo,  ilal.  lamarindi;Mi\
'   Defréinery,  Journ.  asiat.  janvier  1869,  p.  9^. -  Dozy,  Gloss.  p.  3/1 3. ^   Clavis  Gazojjliyl.  p.  6.
'   Voy.  Francisque  Michel,  apud  Dcfrémery,  Mémoires  d'hist.  orienlale, p.  21 3.
^  Leaic.  alcheniiœ ,  p.  l\()2.
DES  MOTS  D  ORIGINE  ORIENTALE.  215
lliiole  et  les  anciens  botanistes  ra[)|)ellent  lamar  tndi.  Dans un  passage  de  Marco  Polo  cité  par  M.  Littré,  on  lit  tama- ramli :  «Si  donnent  aux  marcheans  à  faire  et  à  boire  une chose  qui  a  nom  tamamndi,  qui  leur  fait  aller  hors  ce (pi'ils  ont  au  ventre,  w  En  effet,  le  tamarin  ou  fruit  du  ta- marinier a  été  souvent  employé  pour  faire  avec  la  casse un  liquide  laxatif ^  C'est  Tarbre  ^^ùJJ>  ^Ji  tamr  hindi,  datte indiemie.  Le  tamarinier  n'est  pas  un  dattier  et  n'offre  au- cune ressemblance  avec  un  arbre  de  cette  espèce;  mais son  fruit  est  une  gousse  qu'on  a  pu  comparer  à  la  datte. Le  mot  tamr,  datte,  se  retrouve  dans  l'espagnol  tumaras, (rochet  de  dattes.
Tambour.  Esp.  tambor,  alambor,  portug.  tambor,  ital. tamburo.  On 
=== leaf0 255 leaf1 256
  aLôI  ^  (fol.  ^-19  recto).  Ce  n'est  pas  là  une  manne,  mais  une li([ueur  (oxymel),  de  liL»-  sik,  vinaigre.
**  On  tirait  autrefois  du  tari  une  espèce  de  sucre  nommô  jagre ,  mot  qui paraît  une  allcraiioii  du  persan  S^  cheker,  sucre.
2i20  DICTIONNAIRE  ÉTYMOLOGIQUE
apporter  à   Bassora  vient  sur  de  petits  buissons  épineux assez  semblables  à  nos  genêts.
Thuban.  Etoile  de  troisième  grandeur  dans  la  constel- lation du  Dragon.  C'est  l'arabe  ^U*j  thoubân,  dragon.
TiBER.  Poudre  d'or,  dans  le  commerce  africain.  Les voyageurs  écrivent  aussi  tihhar,  atihar,  rr  le  tihhar  ou  l'or  pur du  Sennaar  ??,  écrit  Bruce  ^  C'est  l'arabe  ^aj  tihr,  même  sens. La  région  africaine  que  nous  nommons  Côte  d'Or  est  ap- pelée par  les  Arabes  ^/jJi  :>5Aj  helfid  at-tibr,  pays  de  la poudre  d'or.
Timbale.  Esp.  hmhal,  atamhal,  atahal,  portug.  timbale, alabale ,  ital.  timbaUo ,  taballo.  De  l'arabe  J^b  tabl,  avec l'article  at-tabl,  sorte  de  tambour.  Il  s'est  glissé  un  m  avant le  b ,  comme  dans  labour  devenu  tambour.  Il  est  vraisem- blable du  reste  que  les  formes  timbale,  timbal,  timbaUo, ont  subi  l'influence  du  latin  tympaniim  (Ti^piTraroi^).  Tabl est  d'origine  persane.  On  trouve  un  pluriel  grec  ra^aXa, tç tambour,    timbale  dont   les    Partbes  se  servaient  à  la
2    „
guerre
TiNCAL  ou  TiNKAL.  Borax  brut.  Esp.  atincar,  portug. atincal,  tincal.  C'est  l'arabe-persan  JlSJo  tinkâl,  ou  ^\^  tin- kâr^  (en  persan  ;l^ou  tengâr).  Le  tincal  nous  vient  princi- palement de  l'Asie  (Perse,  Tbibet,  Inde).  Il  semble  qu'une sorte  de  confusion  se  soit  établie  entre  le  tinkâr  et  une autre  substanc
=== leaf0 275 leaf1 276
.  Rebec.
Arracife,  esp.  Voy.  Récif.
Arraes,  pg.  voy.  Réis.
Arraez,  esp.  voy.  Réis. Arrafiz,  esp.  voy.  Artichaut.
Arrate,  esp.  voy.  Arralel.
Arratel.
Arrecife,  esp.  voy.  Artichaut.
Arrecife,  hisp.  voy.  Récif.
Arrel,  esp.  voy.  Arratel.
Arrelde,  esj9.  voy.  Arratel.
Arrezafe,  esp.  voy.  Artichaut.
Arriscador,  esp.  voy.  Risque.
Arrisco,  esp.  voy.  Risque.
Arroba,  A/s/;.  voy.  Arrohe.
Arrobe.
Arrobe,  pg.  voy.  Rob.
Arrope,  esp.  voy.  Rob.
Arsanail,  voy.  Arsenal.
Arsenal.
Àpo-ey/xo5,  voy.  Alchimie,  29.
Arsina,  langued.  voy.  Arsenal.
Artichaut.
Articiocco,  ital.  voy.  Artichaut.
ÀpTUTtxd?,  voy.  Artichaut.
Arzel.
Arzena,  ^7a/.  voy.  Arsenal.
Arzenale,  ital.\o\.  Arsenal.
Asagi,  voy.  Alchimie  ,82.
Asangue,  voy.  Astronomie,  if).
Asani,  voy.  Palard.
Aschémie,  voy.  Astronomie,  iG.
Aschère,  voy.  Astronomie,  17.
Ased,  voy.  Alchimie,  26.
Asesino,  esp.  voy.  Assassin.
Asingar,  voy.  Alchimie,  27.
Aslani,  voy.  Patard.
Asoch,  voy.  Azoth,
Assaci,  voy.  Assassin.
Assagaïs,  voy.  Zagaie.
Assassi,  b.  lat.  voy.  Assassin.
Assassin.
Assassino,  pg.  voy.  Assassin.
Assesini,  b.  lat.  voy.  Assassin.
ASSOGLE.
Assucar, /;§•.  voy.  Sucre.
AsTAROTIi.
Astarté,  voy.  Astarolh. Asngar,  voy.  Alchimie,  27. Asugia,  voy.  Astronomie,  18.
î
I
INDEX  DES  MOTS  EUROPEENS.
2/1 1
Alabal ,  esp.  voy.  Timbale.
Alabnle, />/,'•.  voy.  Timbale.
Ataghan,  voy.  Yalaghan.
Alaïr,  voy.  Altaïr.
Atambal,  esp.  voy.  Timbale.
Atambor,  esp.  voy.  Tambour.
Atanor,  esp.  voy.  Athanor.
Atara,  esp.  voy.  Tare.
Vlarasanal,  esp.  voy.  Arsenal.
Afarazana,  esp.  voy.  Arsenal.
Alarfe,  ^.«s/;.  voy.  Téréniabin,  note  -2.
Ataur,  voy.  Astronomie,  ly.
Albair,  voy.  Altaïr.
Athanoh.
Athonor,  voy.  Atbanor.
Atibar,  voy.  Tiber.
Atin ,  voy.  Astronomie ,  1 9.
Atincal,  pg.  voy.  Tincal.
Alincar,  esp.  voy.  Tincal.
Atinkar,  voy.  Alchimie,  9/1,
Alir,  voy.  Astronomie,  19.
Atlé.
Atutia,  hisp.  voy.  Tutie.
Atyr,  voy.  Astronomie,  k).
Aubarde,  voy.  Barde.
Aubère.
Aubergine.
Auberré ,  voy.  Aubère.
Aubricot,  voy.  Abricot.
AUFFE.
Aufïin ,  voy.  Fou.
Aufîn,  voy.  Fou.
Auge.
AvdévTns,  voy.  Efendi.
AUMUSSE.
Au
=== leaf0 295 leaf1 296
um,  lat.  bot.  voy.  Épinard.
Stambecco ,  ital.  voy.  Chébec.
2T/(xfA<,  voy.  Antimoine.
Sucre.
Sucrion,  voy.  Sucre,
Sugar,  angl.  voy.  Sucre.
Sugrégeon,  voy.  Sucre.
Suiker,  holl.  voy.  Sucre.
Sukier,  pol.  voy.  Sucre,
Sultan.
SuUano,  ital.  voy.  Sidtan.
Sumac,
260
DICTIONNAIRE  ÉTYMOLOGIQUE.
Sumach,  voy.  Sumac.
SUHBUL.
Snmmagre,  /?/j'.  voy.  Siiniac.
SUMPIT.
Sunnite.
Suradain,  voy.  Astronomie,  .'^8. I!.vpi}c6v,  voy.  Jargon. Surrapa ,  p^''.  voy.  Sirop. Surmeh,  voy.  Alcool,  note  a. Syricum ,  lat.  voy.  .largon. Syrupus,  b.  lat.  voy.  Sirop.
Tabaisir,  voy.  Tabaschir.
Taballo,  ital.  voy.  Timbale.
Tabaschir.
Tabaxir,  voy.  Tabaschir.
Tabi,  hisp.  ital.  voy.  Tabis.
Tabis.
Tabour,  voy.  Tambour.
Tabur,  voy.  Tambour.
Taça,  pg.  voy.  Tasse.
Taffetas.
Tafilete,  esp.  voy.  Filali.
Talapoin.  Addil.
Talc
Talco,  hisp.  voy.  Talc.
Talg,  ail.  voy.  Talc.
Talisman.
Talmud.
Talpack,  voy.  Colback.
Talque,  esp.  voy.  Talc.
Tamarandi,  voy.  Tamarin.
Tamaras,  esp.  voy.  Tamarin.
Tamarin.
Tamarindi,  ital.  voy.  Tamarin.
Tamarindo,  hisp.  voy.  Tamarin.
Tambaca,  pg.  voy.  Tombac.
Tambor,  hisp.  voy.  Tambour.
T'VMDOUR.
Tambura,  voy.  Tambour. Tamburo,  ital.  voy.  Tambour. Tandoi  p.. Tanzimat.
Tara  ,  hisp.  ital.  voy.  Tare. Taragona,  e.s'/>.  voy.  Kstragon. Tapants,  voy.  Taraxacum. Tarasacon,  voy.  Taraxacum.
Taraxacées,  voy.  Taraxacum. Taraxacon,  voy.  Taraxacum. Taraxacum. Tarbouch.
Tarchon,  voy.  Estragon. Tarcbonante,  voy.  Estragon. Tarchonanlbus,  lat.  bol.  voy.  Estra- gon. Tarcon,  voy.  Estragon. Tare.
Targa,  ital.  voy,  Targe. Targe.
Targone,ùa/.  voy.  Estragon. Targum,  voy.  Drogman. Tari,  vov.  Téréniabin. Tarif.
Tarifa,  hisp.  vOy.  Tarif. Tariffa,  ital.  voy.  Tarif. Tap<;)^o5,  voy.  Boutargue. 'ïé.pi-/ov  ^  voy.  Boutargue. TapHoiatov ,  voy.  Carquois. Tarquais,  voy.  Carquois. T
=== leaf0 296 leaf1 297
artar,  voy.  Tartre. Tartaro,  hisp.  ital.  voy.  Tarhv. Tartarum,  b.  lat.  voy.  Tartre. Tartre. Tasse.
Tatar,  voy.  Turc. Talule,  voy.  Métel. Taza,  esp.  voy.  Tasse. Tazza,  ital.  voy.  Tasse. TéAscr/xa,  voy.  Talisman. Téréniabin.
Térenjubin,  voy.  Téréniabin. Terniabin,  voy.  Téréniabin. Ti^/i^pa,  voy.  Chiffre. T^^vKixvi^eiv,  voy.  Chicane. T^vKÛvtov,  voy.  Chicane. Thérenjabin,  voy.  Téréniabin. Thuban.
Tibbar,  voy.  Tibei-. Tiber.
Timariot,  voy.  Zauii. Timbal ,  r.s/>.  voy.  Tin)l)alc. Timbale.
'F'imballo,  ital.  vov.  Timbale TncAi..
IJNDEX  DES  MOTS  EUROPEENS.
261
Tiiickar,  voy.  Tincal. Tinkal,  voy,  Tincal. Tintenague ,  voy.  Toutenaguc.
ToMAN.
Tomane,  voy.  Toman.
Tombac.
Tombacco,  ital.  voy.  Tombac.
Toimnan,  voy.  Toman.
Toiic ,  voy.  Toug.
Toi' G.
TOUTENAGUE.
Tragon,  voy.  Estragon. Trangébris,  voy.  Téréniabin. Trépang.
Trinca ,  langued.  voy.  Matraca ,  note. Tringibin,  voy.  Téréniabin. Tripan,  voy.  Trépang. Trique,  troquer,  voy.  Matraca ,  noie. Truca,  langued.  voy.  Matraca,  note. Truchement,  voy.  Drogman. Trujaman,  esp.  voy.  Drogman. Trunjibin,  voy.  Téréniabin. Tumbaga,  esp.  voy.  Tombac. Tv(n:avov,  voy.  Timbale. Turbich,  b.  lat.  voy.  Turbilh. Turbit,  esp.  voy.  Turbith.
TURBITH.
Tdrc.
Turcasia,  b.  lat.  voy.  Carquois. Turcasso ,  ital.  voy.  Carquois. Turchimannus,  b.  lat.  voy.  Drog- man. Turcimanno,  ital.  voy.  Drogman. Turcoman,  voy.  Turc. Turpethum,  lat.  bot.  voy.  Turbith. Turquois,  voy.  Carquois. Tutonaga ,  pg.  voy.  Toutenague. Tutia,  hisp.  voy.  Tutie.
TCTIE.
Tulimac,  voy.  Toutenague. Tyrapanum,  voy.  Timbale. Tzukur,  hong.  voy.  Sucre.
Ubi,  voy.  Ubion,  Ad  dit.
Ubion.  Addit.
Uleha.
Uncia ,  lat.  voy*  Ocque.
Upas.
Urdu.
Ursub,  voy.  Alchimie,  7.
Usnea ,  lat.  bot.  voy.  Usnée.
USNÉE.
Usrub,  voy.  Alchimie,  7. Uzifur,  voy.  Alchimie,  kç
=== leaf0 301 leaf1 302
Pastèque.
Joo,  ^i?3  voy.  Baal.
^IjoLj  voy.  Baldaquin.
pISpS  voy.  Bacbuc.
^i-s-iJb  voy.  Bakchich.
3o  turc,  voy.  Bey.
(^JCjJio  f?/rf,  voy.  Bey.
JJio  fmr,  voy.  Bey.
^-jjij  voy.  Balais.
^UlU  voy.  Balzan.
^t-to  ma/,  voy.  Carambolier.
b^  voy.  Ballote.
èj^  mal.  voy.  Baléron.
'J^^bs  voy.  Bélial.
A<Jj  voy.  Belléric.
aLJj  pers.  voy.  Belléric.
^.A.<r  wa/.  voy.  Bambou.
^-jtJ  cyLo  voy.  Bénelnacb.
'^)y^  '"«/•  voy.  Benluiorig.
^  voy.  Bangue.
^jsJLî  voy.  Abricot,  Bonduc.
3jlj  pc^'s.  voy.  Bangue.
(^  voy.  Béni.
^^^  voy.  Boudjou.
,3.=».^  fjor,  voy.  Boudjou.
^^^  voy.  Alchimie,  8  ,  et  Borax.
5r^  pers.  voy.  Borax.
»^^  voy.  Bosan.
j^^  voy.  Palard.
j*.LLi£^  voy.  Grèbe.
J^  voy.  Alchimie,  9.
*J^  "/»fl/.  voy.  Bambou.
(^y<^  voy.  Béhen.
joLo  voy.  Abit,  Bayad.
o^  voy.  Bételgeuse.
-1^  ftwc,  voy.  Baïram.
^■r^pers.  voy.  Vérin.
ji^U  pers.  voy.  Babouche. ^^IxIjLj  pers.  voy.  Aubergine. sISsIjIj  pers.  voy.  iVubergine. yû;^Lj  pers.  voy.  Bézoard. sLi^Upej's.  voy.  Chah. ^^Xjpers.  voy.  Parsis. »>Lj  pers.  voy.  Para. (jkLj  pers.  voy.  Bézoard. ivolj  pers.  voy.  Alphénic. i^yj  pers.  voy.  Péri. HDD  voy.  Pâques. ^"ikj  pers.  voy.  Pilau. ^  pers.  voy.  Punch. □  "«"nS  voy.  Purim. fjj^^^,  pers.  vov.  Babouch,  Tar- bouch.
^\j  pers.  voy.  Téréniabin. (^^"^  pers.  voy.  Téréniabin. j*J  voy.  Tiber.
2()6
DICTIONNAIIIE  ÉTYMOLOGIQUE.
jK^pers.  voy.  Tambour.
y^  pers.  voy.  Tambour.
>Lcj'pe7's.  voy.  Turc.
yS  pers.  voy.  Téréniabin.
jowj  voy.  Turbith.
■^jj  voy.  Tartre.
□3 i
=== leaf0 307 leaf1 308
JoLiLi  voy.  Sécaciil.
■X^  pers.  vov.  T('réniaitin .  noi"'
I
liNDEX  DES  MOTS  ORIEINTAUX.
271
f^jjXii  voy.  Chaland.
^^JLi  voy.  Siroc.
JjjLi  voy.  Siroc.
jUi  voy.  Astronomie,  99.
*-ï-ji.*4  pers.  voy.  Cimeterre.
XIî;,*  voy.  Scheva.
J\y^  voy.  ChewaI,
jg-i  voy.  Cheikh,  Echecs.
yUa^  voy.  Satan.
^Ja-v-i  voy.  Cétérach.
j-^  voy.  Schiite.
45-^Lo  turc,  voy.  Chagrin.
^La3  voy.  Azerbe.
^30sj^  pei's.  voy.  Sadder.
^!js*s  voy.  Soda.
vjsoo  voy.  Zédaron.
^jj^yo  voy.  Astronomie,  38.
(SyJtMS  turc,  voy.  Chagrin.
xJua  voy.  Sofa.
yuo  voy.  Safre,  ChifTre.
SyJuo  voy.  Alchimie,  h'].
Â^^JLo  voy.  Astronomie,  87.
JLo  voy.  Sacre.
âcLl*3  voy.  Arsenal.
^jo  voy.  Astronomie,  i5.
JjsJUs  voy.  Sandai.
èyo  voy.  Soufi.
i^Lô  voy.  Dey. tlXjiô  voy.  Dub. J^-é  voy.  Azerbe. iùuwô  voy.  Aidée.
nlX32î  voy.  Sabaoth. nj22i2J  voy.  Dame-jeanne.
^iio\io  vov.  Mélel.
iolb  vo\.  Patard. yÀh  voy.  Altaïr. ^-j-iLb  voy.  Tabaschir. J-^i^  voy.  Timbale. iCa^!^  voy.  JMatelas. ^^.jo  voy.  Tarbouch. i^pjc:  voy.  Estragon. ^^  voy.  Matelas. 'is^jo  voy.  Tare. ^jl^Jui.:^^  voy.  Taraxacuin. i^^j^  voy.  Estragon. i^^j^jo  voy.  Taraxacum. ■pioJû  voy.  Tartre. *UJ:>  voy.  Téréniabin. ^^  voy.  Matraca. JJo  voy.  Tasse. ,c«-ik>  voy.  Talisman, ^  voy.  Talc. \y^  voy.  Tambour. A«i)^  turc ,  voy.  Doliman.
i^Ui  voy.  Dey.
^U  voy.  Avarie.
^Ic  voy.  Uléma.
pL-c  voy.  Caban.
^y^  voy.  Ast
```


## [2026-09-14T03:09:46.684Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    for pat in [r'^tobacco,', r'^tabatiere', r'tabati', r'^tabor,', r'^tambour', r'^taboret']:\n        if re.search(pat,p,re.M|re.I):\n            print('leaf0',i,'pat',pat)\nEOF"
}
```


### [2026-09-14T03:09:48.440Z] TOOL RESULT

```
leaf0 828 pat tabati
leaf0 829 pat ^taboret
leaf0 831 pat ^tambour
leaf0 860 pat ^tobacco,
leaf0 860 pat tabati
```


## [2026-09-14T03:09:56.428Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (828,829,831,860):\n    p=t[i]\n    print('===== leaf0',i)\n    print(re.sub(r'\\n{2,}','\\n',p)[:2600])\nEOF"
}
```


### [2026-09-14T03:09:57.641Z] TOOL RESULT

```
===== leaf0 828
  —  A  hybrid  coined  fr. syphilis  and  -ous,  a  suff.  of  Latin  origin.
syren,  n.  —  See  siren.
Syria,  n.,  name  of  a  country  in  Asia  on  the  Med¬ iterranean  Sea.  —  L.  Syria,  fr.  Gk.  Supla,  ‘Sy¬ ria’,  fr.  Eupiot,  ‘the  Syrians’,  a  name  orig.  given to  the  Assyrians  (see  Herodotus  7,  63),  Suptoi being  an  aphetic  form  of  ’Aaaupiot,,  ‘Assyr¬ ians’,  fr.  ’Aaaupta,  ‘Assyria’.  See  Assyria.
Syriac,  adj.  and  n.,  (pertaining  to)  the  Syrian  lan¬ guage. — L.  SynacMi,  ‘Syrian’,  fr.  Gk.  Suptaxip, fr.  Hop: a.  See  prec.  word  and  -ac.
Syriacism,  n.,  a  Syriac  idiom.  —  See  Syriac  and -ism  and  cp.  Syriasm.
Syrian,  n.  and  adj.  —  ME.  sirien,  fr.  MF.  Sirien (F.  Syrieri),  formed  with  suff.  -ien  fr.  L.  Syrius, ‘Syrian’,  fr.  Syria.  See  Syria  and  -an  and  cp. sorghum.
Syriasm,  n.,  a  Syriac  idiom.  —  Formed  fr.  Gk. Supia^stv,  a  supposed  var.  of  Zupipetv,  ‘to speak  Syriac’,  fr.  Siipop,  ‘Syrian’.  See  Syro-.
syring-,  form  of  syringo-  before  a  vowel.
Syringa,  n.,  a  genus  of  plants:  1)  the  mock  or¬ ange;  later  applied  to  2)  the  lilac.  —  ModL.,  fr. Gk.  aupiv?,  gen.  auptyyop,  ‘pipe,  tube’;  the mock  orange  was  so  called  in  allusion  to  the  use of  its  hollow  stems  for  making  pipes.  See  next word  and  cp.  seringa.
syringe,  n.,  a  narrow  tube  for  injecting  a  liquid  in a  stream.  —  ML.  siringa,  syringa,  fr.  Gk. auptyi;,  gen.  auptyyop,  ‘pipe,  shepherd’s  pipe, tube,  whistle’.  See  syrinx.
Derivative:  syringe,  tr.  v.
syringeal,  adj.,  pertaining  to  the  syrinx.  —  Form¬ ed  with  adj.  suff.  -al  fr.  Gk.  auptyE,  gen.  aupty- yo p,  ‘pipe,  tube’.  See  syrinx.
syringitis,  n.,  inflammation  of  the  Eustachian tube  (med.)  —  Medical  L.,  formed  fr.  syrinx with  suff.  -itis.
syringo-,  before  a  vowel  syring-,  combining  form meaning  ‘pipe,  fistula;  spine’.  —  Gk.  auptyyo-, aupiyy-,  fr.  aupiyE,  gen.  auptyyop,  ‘pipe, tube’.  See  syrinx.
syringotomy,  n.,  operation  on  the  anal  fistula (med.)  —  Compounded  of  syringo-  and  Gk. -xoptta,  ‘a  cutting  of’,  fr.  xoprf],  ‘a  cutting’.  See -tomy.
syrinx,  n.,  anything  tubular.  —  Gk.  auptyi;,  gen. auptyyop,  ‘pipe,  shepherd’s  pipe,  tube,  whistle’, rel.  to  aupii^Eiv,  ‘to  pipe,  whistle,  hiss’,  from  the I.-E.  imitative  base  *swer-,  *sur-,  *surr-,  ‘to sound’,  whence  also  OI.  svarati,  ‘sounds,  re¬ sounds’,  L.  susurrus,  ‘whisper’.  See  susurration. For  the  suff.  of  aupiyE  cp.  cpoppiiyE,  ‘ly
===== leaf0 829
ntablature, entablement,  taffrail.  Cp.  also  the  first  element in  dolmen.
Derivatives:  table,  tr.  v.,  tableau  (q.v.),  tabl-ed, adj.,  table-ful,  adj.,  tablet  (q.v.),  tablier  (q.v.), tabl-ing,  n.,  tabloid  (q.v.) tableau,  n.,  picture.  —  F.,  ‘picture,  painting’, dimin.  of  table.  F.  dimin.  suff.  -eau  derives  fr.  L. -ellus ;  see  -el.
table-d’hote,  n.,  common  table  for  guests  at  a hotel.  —  F.,  lit.  ‘table  of  the  host’.  See  table  and host,  ‘one  who  receives  guests’, tablet,  n.,  a  small  slab.  —  ME.  tablette,  tablett, fr.  OF.  tablete  (F.  tablette),  dimin.  of  table,  fr. L.  tabula.  See  table  and  -et.
taDiier
tag
1565
Derivatives:  tablet ,  tr.  v.,  tablet-ary ,  adj. tablier,  n.,  an  apron.  —  F.,  lit.  ‘that  which  be¬ longs  to  the  table',  fr.  table,  ‘table’.  See  table  and -ier.
tabloid,  n.,  a  small  tablet  of  medicine;  a  trade¬ mark.  ■ —  A  hybrid  coined  fr.  table  and  Gk. -oEiSf]?,  ‘like’,  fr.  eiSo;,  ‘form,  shape’.  See  -oid. taboo,  tabu,  adj.,  forbidden.  —  Tongan  tabu,  rel. to  Polynesian  tapu,  ‘sacred’.  The  original  mean¬ ing  prob.  was  ‘exceedingly  marked’,  fr.  ta, ‘mark’,  and  pu,  ‘exceedingly’.  See  Encyclopae¬ dia  Britannica,  1947,  vol.  21,  p.  732. Derivatives:  taboo ,  tabu,  n.  and  tr.  v. tabor,  also  tabour,  n.,  a  small  drum  resembling  a tambourine.  —  ME.,  fr.  OF.  tabour,  ‘drum; stool’,  fr.  Arab,  tabul,  pi.  of  tab/,  ‘drum’.  Cp. tambour,  taboret.
taboret,  also  tabouret,  n.,  a  small  tabor,  tabret.  — F.  tabouret,  dimin.  of  OF.  tabour,  ‘drum ;  stool’. See  prec.  word.
tabret,  n.,  a  small  tabor.  —  A  var.  of  prec.  word, tabula,  n.,  table;  tablet.  —  L.  See  table. Derivatives:  tabular  (q.v.),  tabul-ate,  adj.  and tr.  v.,  tabul-at-ed,  adj.,  tabul-at-ion,  n.,  tabulat¬ or,  n.,  tabul-at-ory,  adj.
tabular,  adj.,  having  the  form  of  a  table;  flat.  — L.  tabularis,  ‘of  boards  or  planks’,  fr.  tabula.  See prec.  word.  For  the  ending  see  suff.  -ar. Derivative:  tabular-ly,  adv. tabula  rasa,  an  erased  or  blank  tablet;  a  clean slate;  hence  the  mind  in  its  primary  state,  i.e., before  impressions  are  recorded  on  it  by  ex¬ perience.  —  ML.,  ‘an  erased  tablet',  fr.  L.  tabula, ‘tablet’  (see  table),  and  fern.  pp.  of  radere,  ‘to scrape  away,  erase’  (see  rase).  ML.  tabula  rasa is  a  loan  translation  of  Aristotle’s  mvaxii; fiYPa9°9.  ‘unwritten  tablet’  (see  his  De  anima, 7,  22).
tacamahac,  n.,  1
===== leaf0 831
ve,  adj.  —  A  hybrid  coined  fr.  talk  and -ative,  a  suff.  of  Latin  origin.
Derivatives:  talkative-ly,  adv.,  talkative-ness,  n. talkie,  n.,  a  sound  motion  picture.  —  Formed  fr. talk  on  the  analogy  of  movie.
tall,  adj.  —  Prob.  fr.  ME.  tal,  ‘seemly’,  fr.  OE. getsel,  ‘swift,  prompt,  ready',  later  used  in  the sense  of  ‘handsome,  brave’,  which  is  rel.  to OHG.  gi-zal,  ‘quick’,  Goth,  un-tals,  ‘indocile’, and  prob.  also  to  OE.  talu,  ‘tale’,  ON.  tal, ‘number’,  telja,  ‘to  tell’.  See  tell  and  tale. Derivatives:  tall,  n.,  tall,  adv.,  tall- ness,  n.
tallage,  n.,  tax  paid  by  the  tenant  to  his  lord (Engl.  Feudal  Law).  —  ME.  taillage,  lalliage, tallage,  fr.  OF.  taillage,  lit.  ‘that  which  is  cut’, fr.  taillier  (F.  tailler),  ‘to  cut’.  See  tailor  and -age  and  cp.  tail,  ‘limitation  of  ownership’, tallboy,  n.,  1)  a  high  chest  of  drawers  (British);  2) a  kind  of  tall  chimney  pot.  —  Lit.  ‘high  wood’, fr.  F.  haul  bois,  E.  tall  being  the  translation  of F.  haul  and  E.  boy  a  corruption  of  F.  bois.  See tall  and  bush  and  cp.  highboy,  lowboy  and hautboy.
tallith,  n.,  prayer  shawl  (Jewish  Religion).  — Mishnaic  Heb.  tallith,  ‘covering,  sheet,  cloak; prayer  shawl’,  prob.  fr.  Biblical  Heb.  tillel,  ‘he covered  over,  roofed’  (a  hapax  legomenon  in the  Bible,  occurring  Neh.  3:15),  corresponding to  Heb.  tzalal,  ‘was  covered  with  shade,  was overshadowed,  grew  dark’,  whence  tzel,  ’shad¬ ow,  shade".  Cp.  Aram.  telala,  Ugar.  zh  Arab. gill,  Akkad,  fillu  and  fuliilu,  ‘shadow,  shade’, tallow,  n.  • —  ME.  talgh,  talow,  fr.  MLG.  talch, whence  also  Du.  talk,  G.  Talg.  MLG.  talch meant  perh.  orig.  ‘a  firm,  compact  material’, and  is  rel.  to  Goth,  tulgus,  ‘firm,  solid’,  and cogn.  with  Gk.  4v-8eXexv)?,  ‘forbearing’,  L.  in- dulgere,  ‘to  be  complaisant,  forbearing’.  See
tally
1568
1569
tan
indulge  and  cp.  words  there  referred  to.  For  the development  of  meaning  cp.  Gk.  crreap,  ‘tallow’, which  is  cogn.  with  E.  stone.
Derivatives:  tallow,  tr.  and  intr.  v.,  and  adj., tallow-er,  n.,  tallow-ing,  n.,  tallow-ish,  adj., tallow-y,  adj.,  tallow-i-ness,  n.
tally,  n.,  a  piece  of  wood  with  notches.  —  AF. tallie,  corresponding  to  OF.,  F.  taille,  ‘notch, cut’,  fr.  Anglo-L.  tdlia,  tallia,  fr.  L.  talea,  ‘rod, stick’.  See  tailor  and  cp.  tail,  ‘limitation  of ownership’.
Derivative:  tally,  tr.  and  intr.  v.
tallyho,  n.
===== leaf0 860
rmine  the strength  of’,  fr.  titre,  ‘title;  right;  fineness  (of coinage),  strength,  titer  (of  solution)’,  fr.  OF. title.  See  titer.
Derivative:  titrat-ion,  n. titre,  n.  —  A  var.  of  titer, titter,  intr.  v.,  to  giggle;  n.,  the  act  of  tittering.  — Of  imitative  origin.
tittle,  n.,  mark  placed  over  a  letter.  —  ME.  titel, title,  fr.  L.  titulus.  See  title.  For  sense  develop¬ ment  cp.  tilde.
tittle-tattle,  n.  —  Antiphonic  reduplication  of
tattle.
tittup,  intr.  v.,  to  behave  in  a  lively  manner;  to caper.  —  Of  imitative  origin.
Derivatives:  tittup,  n.,  littupp-y,  adj. titubant,  adj.,  staggering,  tottering.  —  L.  titubdns, gen.  -antis.  See  next  word, titubate,  intr.  v.,  to  stagger,  totter.  —  L.  titubdtus, pp.  of  titubare,  ‘to  stagger,  totter,  reel’,  which  is of  imitative  origin.
titubation,  n.  —  L.  titubatio,  gen.  -onis,  fr.  tituba- tus,  pp.  of  titubare.  See  prec.  word  and  -ion. titular,  adj.,  1)  pertaining  to  a  title;  2)  held  in virtue  of  a  title;  3)  existing  only  in  title.  —  L. *titularis,  fr.  titulus,  ‘title’.  See  title  and  -ar. titulary,  adj.,  titular;  n.,  a  person  who  holds  a
title.  —  See  prec.  word  and  -y  (representing  L. -ius).  Formed  fr.  L.  titulus,  ‘title’  (see  title),  with adj.  suff.  -ary.
Titus,  masc.  PN.  —  L.  For  the  literal  meaning  of this  name  see  Kerenyi  in  Glotta  22,  40  (quoted by  Walde-Hofmann,  LEW.,  II,  686,  s.v.  titulus). tityre-tu,  n.,  name  of  a  gang  of  ruffians  in  London in  the  time  of  the  Restoration.  —  Fr.  L.  Tityre, tu  (“O  Tityrus,  thou”),  the  opening  word  of Virgil’s  first  eclogue.
tizzy,  n.,  a  sixpence  (slang).  —  Corruption  of  tes¬ ter,  name  of  coins.
tmesis,  n.,  separation  of  a  compound  word  by  the intervention  of  a  word  or  words  (gram.)  —  Gk. TjAijcts,  ‘a  cutting’,  fr.  *tm-,  zero  degree  of  I.-E. base  *tem-,  ‘to  cut’,  whence  Tep-vsiv,  ‘to  cut’, to [aV],  ‘a  cutting’.  See  tome  and  cp.  words  there referred  to.
T.N.T.,  trinitrotoluene.  —  Abbreviation  of  the initials  of  the  elements  of  trinitrotoluene, to,  prep.  —  ME.,  fr.  OE.  to,  rel.  to  OS.,  OFris.  to, Du.  toe,  OHG.  zuo,  zua,  zo,  MHG.  zuo,  G.  zu, ‘to’,  from  the  I.-E.  pronominal  base  *do-,  ‘to, toward,  upwards’,  whence  also  L.  do-  in  donee, ‘as  long  as,  while’,  and  -do  in  quandd,  ‘when’. Cp.  I.-E.  *do  in  OSlav.  do,  ‘as  far  as,  to',  and  in OL.  -do,  -du  (in  endo
```


## [2026-09-14T03:10:08.219Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'tabati[^\\n]{0,400}', r'\\ntabor,[^\\n]{0,300}', r'\\ntambour[^\\n]{0,400}', r'\\ntobacco,[^\\n]{0,600}', r'\\ntabret[^\\n]{0,200}', r'\\ntabouret[^\\n]{0,200}']:\n    for m in re.finditer(pat,t,re.I):\n        print('>>>',m.group(0).replace('\\n',' ')[:600]);print()\nEOF"
}
```


### [2026-09-14T03:10:09.406Z] TOOL RESULT

```
>>> tabatiere,  n.,  a  snuffbox.  —  F.,  fr.  earlier  taba- quibre,  fr.  tabac,  ‘tobacco’.  See  tobacco, tabby,  n.,  a  kind  of  watered  silk.  —  F.  tabis,  fr. Sp.  tabi,  fr.  Arab,  attdbi,  fr.  at-Attabiyd' ,  name of  a  suburb  of  Bagdad,  where  this  kind  of  silk stuff  was  fabricated.  The  suburb  was  named after  Prince  Attab,  a  descendant  of  the  Om- miads.  Cp.  tabinet,  

>>> tabatiere. tobacconist,  n.  —  A  hybrid  coined  from  prec. word,  a  euphonic  n,  and  -ist,  a  suff.  of  Greek origin.

>>>  tambour,  n.,  1)  a  drum;  2)  a  drumlike  frame  for embroidering.  —  F.,  fr.  OF.,  fr.  Arab,  tabul,  pi. of  tabl,  ‘drum' ;  influenced  in  form  by  VArab. tanbur  (=  Classical  Arab,  tunbur),  ‘lute’.  Cp.

>>>  tobacco,  n.  —  Sp.,  Port,  tabaco ,  fr.  Taino  (Carib¬ bean)  tabaco,  ‘pipe  for  smoking;  roll  of  tobacco leaves’ ;  the  English  form  of  the  word  was  prob. influenced  by  Tobago,  name  of  a  West  Indian island ;  cp.  F.  tabac.  It.  tobacco,  G.  Tabak,  Du. tabak.  Hind,  tambaka,  which  all  derive  ult.  fr. Taino  tabaco.  Cp.  also  tabatiere. tobacconist,  n.  —  A  hybrid  coined  from  prec. word,  a  euphonic  n,  and  -ist,  a  suff.  of  Greek origin.

>>>  tabret,  n.,  a  small  tabor.  —  A  var.  of  prec.  word, tabula,  n.,  table;  tablet.  —  L.  See  table. Derivatives:  tabular  (q.v.),  tabul-ate,  adj.  and tr.  v.,  tabul-at-ed,  adj.,  tabul-at-i
```


## [2026-09-14T03:10:24.570Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -ro '\"VFO[:0-9]*\"' data/extracted/batch/ | sed 's/.*batch\\///' | sort | uniq -c | head -30; echo ---; grep -rno 'VFO' data/extracted/*.json 2>/dev/null | head"
}
```


### [2026-09-14T03:10:25.565Z] TOOL RESULT

```
      1 page-173.json:"VFO:25"
      1 page-268.json:"VFO:24"
      1 page-44.json:"VFO:15"
---
(eval):1: no matches found: data/extracted/*.json
```


## [2026-09-14T03:10:26.938Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 494 -l 494 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg494 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg494.png"
}
```


### [2026-09-14T03:10:28.942Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 72008 Sep 13 23:10 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg494.png
```


## [2026-09-14T03:10:34.240Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -l 'VFO' data/verification/*.json 2>/dev/null; echo ---; grep -o '\"ref\": \"VFO[^}]*}' data/verification/*.json 2>/dev/null | head -5; echo ---; python3 - <<'EOF'\nimport re\n# find abbreviation list in the extracted pages: search for 'VFO' in the pdf text\nimport subprocess\nfor p in range(1,30):\n    txt=subprocess.run(['pdftotext','-f',str(p),'-l',str(p),'/home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf','-'],capture_output=True,text=True).stdout\n    if 'VFO' in txt:\n        for line in txt.split('\\n'):\n            if 'VFO' in line or 'VDQ' in line: print(p, line)\nEOF"
}
```


### [2026-09-14T03:10:36.449Z] TOOL RESULT

```
data/verification/page-173.json
data/verification/page-241.json
data/verification/page-268.json
data/verification/page-471.json
data/verification/page-44.json
data/verification/page-77.json
---
---
16 VFO
16 VDQ
23 VDQ
23 VFO
```


## [2026-09-14T03:10:38.944Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftotext -f 16 -l 16 EtymologicalDictionary-persian-english.pdf - | grep -n -A3 -B3 'VFO'; echo =====; grep -o '\"VFO[^\"]*\"[^}]\\{0,300\\}' data/verification/page-173.json | head -3"
}
```


### [2026-09-14T03:10:40.003Z] TOOL RESULT

```
Exit code 1
48-FFD
49-TZF
50-ZFS
51:VFO
52-SOR
53-AKM
54-AMD
(eval):1: ==== not found
```


## [2026-09-14T03:10:42.422Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftotext -f 16 -l 16 -layout EtymologicalDictionary-persian-english.pdf - | sed -n '30,80p'; echo \"=== 23 ===\"; pdftotext -f 23 -l 23 -layout EtymologicalDictionary-persian-english.pdf - | grep -n -B2 -A2 'VFO'"
}
```


### [2026-09-14T03:10:43.481Z] TOOL RESULT

```
Khalîlî K.                 MMF      Laufer B.           SIN      Bartholoma   BRT
Kowsar B.                  SNB      MacKenzie           PHD                   HID
Mehrâvand K.               VSF      Mann S. E.          IEC                   ZAW
Mo`în M.                   MON      Morris W.           AHD      Dozy (Dutch) DOZ
Moshîrî M.                 VOP      Nyberg H.S.         NYB      Dvorak R.    FWK
Nafîsî S.                  DMO      Partridge E.        PRT      Frankel S.   AFA
Nahvî S. M.                FVA      Pei M.              PEI      Horn P.      HRN
Nâtel Khânlarî P.          MZF      Platts J. T. &               Hubschmann   HUB
Noushîn A. H.              FSF         Ranking G.S.A.   GPL      Ibrâhîm J.   KGW
Orânskî & Keshâvarz        MFL      Richardson J.       RCH      Lagarde P.   LAG
Pûr Dâvûd                  FIB      Shipley J. T.       SHP      Liden E      AIN
Râshed Mohassel            DZA                          OEW      Lokotsch K.  LKT
Rokn Zâdeh -                        Skeat W. W.         SKT      Pokorny J.   POK
       Âdamîyyat M.H.      ARK      Speake J.           OXF      Siddiqi A.   SDQ
Sajjâdîyyeh M. A.          IRT      Taylor W.           TYL      Spiegel F.   SPG
                           VIE      Tolman H. C.        TLM                   ARP
Sayyâh A.                  SAP      Unvala J. M.        UNV      Vambery H.   TTS
Tabrîzî M.H.(Borhân)       BQT      Widengren G.        MAG      Walde A.     LEW
Tavoosî M.                 SNS      Withworth G. C.     AID                   WLD
                                    Yule H. &                    Zimmern H    AKD
                                         Burnel A. C.   HJB



A-8
=== 23 ===
18-            Comments (see FVQ). Toos Publishers, Tehran 1372 (1993).
19-
20:102   VFO   M. Ahmad Soltânî, Vâjhgân Fârsî dar Zabânhây ÁûzfZ }£¡ú£Ög fd Áçf£ï x£ôhZz
21-            Orûpâî, Âvây Nûr Press, Tehran, 1372 (1993).
22-
```


## [2026-09-14T03:10:48.466Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg494.png"
}
```


### [2026-09-14T03:10:49.024Z] TOOL RESULT

```

```


## [2026-09-14T03:10:49.015Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:11:02.442Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; pdftoppm -f 494 -l 494 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg494hi && python3 - <<'EOF'\nfrom PIL import Image\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad'\nim=Image.open(S+'/pg494hi.png'); print(im.size)\nw,h=im.size\n# English AHD:1025 box approx at x 880-1200/1545, y 1360-1430/2000 of displayed\nbox=(int(0.55*w),int(0.66*h),int(0.80*w),int(0.72*h))\nim.crop(box).save(S+'/pg494-tambour.png')\nbox2=(int(0.25*w),int(0.185*h),int(0.80*w),int(0.24*h))\nim.crop(box2).save(S+'/pg494-root.png')\nEOF\nls -la $S/*.png"
}
```


### [2026-09-14T03:11:05.604Z] TOOL RESULT

```
<persisted-output>
Output too large (38.2KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/brknlrob1.txt

Preview (first 2KB):
(3400, 4400)
-rw-rw-r-- 1 sfmqrb sfmqrb   92443 Sep 13 21:13 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/391-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  129993 Sep 13 21:11 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21316 Sep 13 21:11 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/394-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44712 Sep 13 21:14 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/400-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116049 Sep 13 21:14 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/400-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99858 Sep 13 21:16 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/404-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91913 Sep 13 21:18 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/411-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34177 Sep 13 21:23 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/412-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79667 Sep 13 21:24 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/414-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110116 Sep 13 21:31 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/417hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88133 Sep 13 21:31 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/417-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12361 Sep 13 21:31 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/417-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45082 Sep 13 21:33 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/421-top.png
...
</persisted-output>
```


## [2026-09-14T03:11:07.823Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg494-tambour.png"
}
```


### [2026-09-14T03:11:07.842Z] TOOL RESULT

```

```


## [2026-09-14T03:11:22.092Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT tabak/tabl/tanbur ===\"; grep -n -i \"tabak\\|tabaco\\|tanbur\\|tunbur\\|tabl,\\|ṭabl\" LKT.txt | head -25\necho \"=== PHN ===\"; grep -n -i \"^TABAC\\|^TAMBOUR\\|^TABATIERE\\|^TIMBALE\" PHN.txt | head\necho \"=== LAM ===\"; grep -n -i \"^TAMBOUR\\|^TABAC\\|tanbour\\|tabour\" LAM.txt | head\necho \"=== DOZ ===\"; grep -n -i \"tabak\\|tamboer\\|tabl\" DOZ.txt | head\necho \"=== SKT ===\"; grep -n -i \"^TOBACCO\\|^TABOR\\|^TAMBOUR\" SKT.txt | head"
}
```


### [2026-09-14T03:11:22.218Z] TOOL RESULT

```
=== LKT tabak/tabl/tanbur ===
905:'Die  Pflanze  Piper  betel  L.  Betelpfetfer' mit  kleinen  roten  Blüten.  Ihre  Blätter werden  von  den  Europäern  Betel  ge- nannt; in  sie  werden  die  Arekanüsse [s.  hier  Nr.  17]  mit  Kalk  eingewickelt und  so  in  ganz  Südasien  als  Narkotikum, ähnlich  wie  bei  uns  der  Kautabak,  viel benutzt.
1195:'Gerber',  ebenso  tk.  debbag;  hieraus rum.  täbäcar  'Loh-  oder  Rotgerber', täbäcärie  'Gerberei',  täbäci  'gerben'; bulg.  tabak  'Gerber'.  Mit  pers.  hänä 'Haus'  [s.  hier  Nr.  809]  ergab  sich  bulg. tabakhana,   serb.   tabakana  'Gerberei'.
1382:'Rauch',  duhän  sariba  'rauchen',  ebenso tk. ;  hieraus  bulg.  serb.  duhan  'Rauch- tabak', poln.  duchan,  klruss.  dochan, Cech.  dohan  'dass.'.
2030:'Gras,  Heu',  später  beng  [s.  hier  Nr.  213] oder  indischer  Hanf,  Cannabis  indica [Über  den  indischen  Hanf  (Haschisch) und  seine  Verwendung  als  narkotisches Genußmittel.  In  Ausland  1863,  Nr.  30  j Ed.  Grimaux,  Du  hachich  ou  chanvre Indien.  Paris  1865];  in  die  europäischen Sprachen  ist  das  Wort  fast  unverändert übergegangen:  frz.  hachiche,  russ.  gasiSf dtsch.  Haschisch.  —  „In  Syrien  steht der  Hasis,  ein  berauschendes  Hanf-  oder Mohnpräparat,  welches  unvermengt  ge- nossen oder  dem  Tabak  beigemengt wird,  bei  den  niederen  Ständen  in Gunst.  Das  Schimpfwort  hassäs  ent- spricht unserem  'Trunkenbold'.  Keines- wegs ist  das  Laster  des  Haschischrauchens derart  verbreitet  wie  bei  uns  der  Ge- nuß der  Spirituosen.  Weit  mehr  als  in Syrien  und  Mesopotamien  ist  das  Hanf-
2033:rauchen  in  Ägypten  verbreitet.  In Marokko  wird  der  Hanf  klf  genannt, klein  geiiackt  und  mit  Tabak  vermischt oder  auch  unvermengt  in  winzig  kleinen Tonköpfchen  aus  etwa  1  Fuß  langen Pfeifen  sehr  viel  geraucht."  Max  Frei- herr V.  Oppenheim,  Vom  Mittelmeer  zum Persischen  Golf  I,  74.  Genaueres  über die  in  Marokko  benutzten  Pfeifen  und die  Art  des  Hanfrauchens  sowie  die  ar. Ausdrücke  dafür  vgl.  MSOS  H,  231 u.  232.  —  Auf  das  oben  erwähnte haMM  hat  SILVESTRE  DE  SAGY  ein weit  verbreitetes  romanisches  Wort zurückgeführt  [de  S.,  Memoire  sur  la dynastie  des  Assassins  et  sur  l'origine de  leur  nom.  Lu  ä  la  seance  publique de  l'Institut  du  7  juillet  1809.  Im  Mo- niteur  no.  210,  an  1809  und  Lettre  de M.  de  S.  au  redacteur  du  Moniteur  sur I'etymologie  du  nom  des  Assassins. Ebenda  no.  359,  an  1809].  Aus  der  Ge- schichte der  Kreuzzüge  ist  der  ,AIte vom  Berge"  bekannt,  der  das  Haupt einer  Sekte  war,  deren  neue  Mitglieder, durch  den  Hanfrausch  fanatisiert,  auf Befehl  ihrer  Obern  selbst  Mordtaten begingen;  aus  dem  ar.  Namen  dieser Sekte  hassäsln  entstand  it.  assassino 'Meuchelmörder',  prov.  asasi,  ansesi, frz.  assassin,  sp.  asesino,  pg.  assassino, rum.  asasin  und  die  dazugehörigen Verba  assassinare  usw.  und  andere  Ab- leitungen. It.  (dial.  Parma)  sasinä  'be- raubt, elend;  Weinbergschnecke'.  — Autiallend  ist,  daß  in  allen  Formen  die beiden  s  verschwunden  sind,  daher schlägt  Lammens  Rem  28  als  Grund- wort den  Namen  des  Gründers  jener meuchelmörderischen  Sekte,  Hasan  ihn §abäh,  vor;  jedoch  scheint  diese  An- nahme nicht  notwendig,  da  im  MA Namen,  die  über  das  Lateinische  ver- breitet wurden,  allgemein  das  s  durch einfaches  s  ersetzten.  [DE  207.  Egui- laz  293.   ML  4074.
2120:'Flasche,  durch  die  zuerst  der  Rauch geht,  wenn  man  Tabak  raucht',  in  Ge- stalt eines  runden  Helmes;  auch  Name der  ganzen 'Wasserpfeife';  ebenso  bind. Hieraus  angloind.  hooka,  frz.  houka  [für die  einfachste  Form  der  Wasserpfeife angloind.  hubble-buhble ,  offenbar  die wallende  Bewegung  des  Wassers  laut- malerisch wiedergebend].  [Devic  DEt 140.    Hobson-Jobson  428  u.  423/424.
2769:'Rauchtabaksbeutel'  [nicht  osm.,  vgl. cag.  kapöak,  kipöak  'hohl,  leer'  vom Stamme  kab  'aufstehen,  anschwellen' Vämbery  TktEtWb  S.  64,  Nr.  71  I],  auch kas.-tat.  kapcyk;  hieraus  russ.  kapsuk 'dass.'.    [Gorjajew  133.
2784:russ.  kisa  'Beutel,  Mantelsack',  kiset 'Tabaksbeutel',  klruss.  kt/sa,  poln.  kiesa 'Geldbeutel'.  Aus  dem  entsprechenden hebr.  Wort  kis  'Beutel'  wurde  gauner- dtsch.  Kies  'Geld'.  [Gorjajew  140.  Bern SlEtWb  503.
2972:Auch  kupj  'Knsten,  Schachtel,  Dose'; hieraus  bulg.  kntija  'Büchse,  Schnupf- tabaksdose, Armenbüchse',  serb.  kutija 'Schachtel' ;  rum.  cutie,  cutiufä,  cutivarä 'Schachtel,  Büchse'.
3105:'Pfeife,  Pfeifenrohr',  ebenso  tk.  lüle; hieraus  rum.  lulea  'Tabakspfeife',  bulg. lula  'Tabakspfeife,  Pfeifenkopf',  serb. lula  'Pfeife,  Pfeifenröhre',  poln.  cech. lulka,  klruss.  l'ul'ka,  russ.  ljul'ka  'Pfeife'. [Gorjajew  198.  Mikl  SlEtWb  176  a. 'Bern  SlEtWb  745.
3672:160s'.  Bengal.  pachapät: Hind.  des  Dekkan  pachoU,  Handelsname der  getrockneten  'Blätter  der  Labiate Pogoslemon  patchouly  Pelletier'  [s.  hier Nr.  1591],  die  der  Minze  verwandt  ist. Sie  werden  als  Zutat  zum  Rauchtabak und  in  sonstiger  ähnlicher  Weise  wie bei  uns  Lawendel  gebraucht.  In  flüssiger Form  kam  das  Parfüm  i.  J.  1844  nach England  und  wurde  bald  weit  verbreitet: engl,  patchouli,  frz.  patchouli,  patchouly, dtsch.  PatschuH.  —  [Die  Ableitung  bei Seiler  DKiL  III,  143,  patchouli  <^  patch leaf  'Blatt  des  Patch'  ist  also  ganz richtig.]    [Hobson  Jobson  683/681.
4274:Ebenso  malayälam  churutfu  'eine  Rolle (Tabak)';  hieraus  angloind.  engl,  che- root  'Zigarre',  bes.  eine  solche,  die  an beiden  Enden  abgestumpft  ist,  wie  es die  indischen  und  die  Manilazigarren früher  waren.   [Hobson-Jobson  188/189.
4430:1962  a.  Tk.  tabak: 'Sohle'  [vom  Stamme  tap  'unten,  Grund, Sohle',  Vämbery  TktEtWb  S.  156,  Nr. 1721;  Kelekian  Kämüs  787  a];  hieraus mit  Verlust  des  Endkonsonanten  sp.  taba 'Art  Würfel  zum  Taba-  oder  Knöchel- spiel'. Man  beachte,  daß  bereits  im Mandschurischen  taba  ein  technischer Ausdruck  im  Knöchelspiel  ist:  'Die flachste  Seite  des  Spielkuochens';  eben-
4753:>  'Rauch',  Vämbery  TklEtWb  S.  181, Nr.  193  II],  'Tabak',  dazu  iütiingü  'Tabak- händler'; hieraus  rum.  tutun  'Rauch, Tabak',  tutungiü  'Tabakhändler',  ttitun- gerie  'Tabakladen',  tutunärit  'Tabak- steuer'; russ.  tjutjun  'Blättertabak, Bauerntabak',  poln.  tutun  'Tabakpflanze, Rauchtabak',  bulg.  iitjun,  bulg.  serb. tutun,  klruss.  t'ut'wi.  'Tabak'.
5698:tabak(hana)  453 ^a&or  1974 tagar  1983 ^o/iM  1994 iöten  2005 ^at^a  2051 tatvan  2052 if/  2060 ^em<;^  2062 tendzera  2066 tenekija  2065 tepcija  2056 tepsija  2056 terzija  2073 <es«e  498 «»war  2079 titjun  2 121 tjumbelek  1971 tteac  2078 tokmak  2087 ^owiritA;  2088 <o/>  2089 iopor  1964 forfca  2091
9614:tabakunn  4oo
=== PHN ===
1532:tambourin et autres instruments. Elles remplissent un rôle
3530:tabac. Voyez au mot Hachighe. — > Chènevis, qui paraît calqué sur
7851:tambour semi-sphérique, et ce lermc doit avoir la même origine
9726:TIMBALE, s. f. (a.)
10915:Timbale, s. f. (a.) — Timbalier, s. m 356
=== LAM ===
5657:tabac est formée d'une noix de coco, ce qui ne serait guère
6231:TabourSf flaûstes jtraverseinnes—
6970:Tambour. Esp : tambor, atambor. Ptg: tambor. Bas laf:
6992:touboâl, avec lequel tabour (i), tabouririy tabouriner, ta-
6995:r (2). De tabour dérive Tabouret. A cause de la commu-
7015:(2) V. Introduction. « Tel noise i avait de tabour z et de tymbres, de
7846:tambour (i). Ce nom-là est morisque. » C'est l'arabe J^l
9828:Tabour
9832:Tabourdeur
9836:Tabouret
=== DOZ ===
194:papegaai , scharlaken , smous , tamboer , tara of tarra, 't Laatste
=== SKT ===
19121:Tambour,  Tamboiirti>e;  tee  Tabour.
19801:Tobacco.  (Span -TUyti.)  %y^n  t(%haro A  word  taken  from  the  language  of  Hayti (Clavigcrn,  Hist,  oT  Mciito).
23325:tabor — tambour.      ^^M
```


## [2026-09-14T03:11:24.711Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n -i \"drum\\|tabūr\\|tabur\\|dahl\" PHD.txt | head -20\necho \"=== NYB ===\"; grep -n -i \"tabūrak\\|tabur\\|drum\" NYB_vol2_glossary.txt | head -20\necho \"=== HRN ===\"; grep -n -i \"tabîra\\|tabira\\|tabîr\\|Trommel\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"Trommel\\|tabîr\" HUB.txt | head -10"
}
```


### [2026-09-14T03:11:24.818Z] TOOL RESULT

```
=== PHD ===
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
597:tru(f)Š [t/wu(p)$ | (P tryff), N turf] sour. truftag [t/wptk'] stolen; intercalary (days). tuhig [twhyk! | M twhyg, ЇЧ tuhi] empty, vain. ~ih : emptiness, void. tumbag [twmbk' | N ~a] drum. tund [twnd | N ~] sharp, violent. ~ih: violence, vehemence. Tür [twl | N ~] one of a people inimical to Eran, Turanian. ~ап [—n! | N ~] (land of) the Turanians. Turk [twlk' | N ~] Turk. tu&t [twst'] silent. tuwān [twb!n! | M twn, N ~] might, power. ~ (+infinitive): it is possible to, one can. ~ag [~k' | N —a] mighty, able. «gar [-kl | N ~] rich. ~garih: richness, wealth. ~ig [-yk'] able. ~igih: ability, power. --sāmān [-s’m’n'] the extent of one’s ability. tuxšáé [twhPk! | M рох р, N tuxsa] diligent. “Аһ: diligence, endeavour. tuxšīdan, tux&- [гол у! | (M. twxf‘yst), N ~] strive, endeavour. ~išn: endeavour, striving.
1701:drum tumbag.
3182:portico dahlīz.
=== NYB ===
3804:tumbak [twmbk'] drum, or kettle-drum 209. — Arm. lw. tmbuk < *tumbuk ‘drum’; NP tanbak, tanbuk, tanbik ( BQ also tun-) ‘bagpipe’, ‘drum’.
=== HRN ===
=== HUB ===
9631:Hier war dvd (avtt i kds *Trommelg^et6n' Fird.
```


## [2026-09-14T03:11:40.434Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN patterns ===\"; grep -n -i \"tabîr\\|tabir\\|tabîra\\|Trommel\\|dunbak\\|tunbak\" HRN.txt | head -20\necho \"=== SKT Tabour ===\"; grep -n -i \"Tabour\" SKT.txt | head\necho \"=== LAM 6965-7020 ===\"; sed -n '6965,7020p' LAM.txt"
}
```


### [2026-09-14T03:11:40.518Z] TOOL RESULT

```
=== HRN patterns ===
=== SKT Tabour ===
19055:K)Ur.  Tabor,  a  small  druio.  (F.- ^Atab.)  F.  tabour  tmod.  F.  tarn- .  —  Spun,  tambor,  atambor  { where  a  ^ e  Arab.  def.  article).  — Ar.ib.  tamhiir^ ]d  of  lute  or  guitar  with  a  long  neck. ix  bnu%  stnng5,  also  a  drum.*  Prob. litative  origta;  cf.  Arab,  iabbdl,  a mrr.  Der.  ta^ur-et  or  tabret,  a i.  form.
19056:nbour,  a  small  dmm-like  frame,  for ■>iderin(;.    (F.  —  Span.  —  Arab.)      F. ■b*',  a  Lanibour,aIso  a  drum;  see  above, nbourlna.   (F.-. span.  — Arab.)     F. mrin,  a  tabour,  dimin.  of  F.  tambour, yxxt  or  dnim  ;  see  Tabour. rulor.  Tabulate ;  see  Table. he  (I),  a  fa-^tening;   sec  Tack. he  (j>.  a  blcmiJi;  see  Tack. It,  silent   vL.)     L.  tacitus.  silent.  > tre,  to  be  silent.  •^Goih.  thahan,  Icel.
19121:Tambour,  Tamboiirti>e;  tee  Tabour.
=== LAM 6965-7020 ===
Voici à propos de J-lfe un spécimen de la science
des étymologistes arabes : « Jii) tîbl • ♦ • o>C Jly I aJ jjé^b
Sur ce mot il y a trois opinions principales... d'après la
deuxième, c'est un mot grec signifiant nœud insoluble ;
d'après la troisième c'est un anagramme de JaL^ » (i).
Tambour. Esp : tambor, atambor. Ptg: tambor. Bas laf:
tabur, taburcium, taburlum. It: tamburo. Il me semble
difficile de dériver ce mot de l'arabe jjlîL tonboûr, qui dans
la langue classique ou parlée n'a jamais désigné qu'une
lyre (2), guitare, ou mandoline, comme traduit M. Bar-
bier de Meynard. La dérivation du persan>J tabîr (3)
me parait également forcée. A toutes ces explications
I II ■ . ■ - . ■■ . . I I »■■■■■ I ■ I ■ I ■ I . « y
ces vers nous rencontrons le mot borax qui déi'We de Tarabe Jjjf boûraq,
même sens, venant lui-même du persan «j^^ boûrah, « On trouve le borax
en Perse » (Trévoux. ) Le pluriel de Jjy est Jj|^ employé quelques li-
gnes plus haut par Mas ^oûdi (175). Tout ce passage est curieux. On y
rencontre plusieurs termes d'alchimie, les éîixirs obj-TV» » les alambics
(de jswVI ) < los cornues, la soUdification du mercure, etc.
(l)**Ar-Râgheb: ^Jikl» SiJij ^\J\ Z\Jl>^ V. aussi jjuîI •Ui» p. 153.
Cet anagramme • rappelle assez-bien celui qu^on fit sur la a révolution fran-
çaise », un Corse te finira.
(2) Mu^arrab. p. 102 et le Kitâb al-Aghânî, pas. Mas^oûdî VIIL 15.
89. 91 etc. Hist. Orient, des crois, pass, Cfr. pourtant le ej^^ ^q
Bâsim le Forgeron (texte, égypt. p. 5 ).
(3) Devic. Dict, étym. s, tambour.234 TANZ
je préfère Tarabe jlL» iabl^ tambour, au pluriel Jji
touboâl, avec lequel tabour (i), tabouririy tabouriner, ta-
bourdeur^ comme on disait autrefois, ont bien de la
ressemblance. Il suffit d'admettre le changement 4© / en
r (2). De tabour dérive Tabouret. A cause de la commu-
nauté d'origine nous faisons suivre ici :
Timbale. E^p : atambal, atabal; en //a/: taballo, vient
encore de J-U \abl, (vulgairem. prononcé iabal. V. Infrod.
Observ. gên.) qui désigne en général un tambour. Les tim-
bales nous sont venues de l'Orient. (Trévoux ). Ici encore
un m s'est glissé avant le bj peut-être sous l'influence du
lat. t/mpanum. Pour expliquer l'insertion de m dans tam-
bour on peut en rapprocher trombe dérivé du latin turbo.
Tandour. Instrument de chauffage chez les Turcs, de
j^ tannoûr (V. athanor et Prov. Arab. 14.) four, duquel
les Turcs ont fait tandoâr. V. jjjUj dans Mallouf.
Tanzimat. Ensemble des réformes administratives
( 1 ) Cette étymologie est assez clairement indiquée dans le Dict. de
Trévoux.— <( Des jarres, dont l'ouverture paraît recouverte d'un parchemin,
et qui cordées sur les côtés comme un tambour étaient sans doute cette
espèce d'instrument nommé taboT't qui dans les premiers siècles s'accor-
dait avec la harpe, et dont on se sert encore en Abyssinie.» Bruce
Voyage en Nubie I, 140. En note on ajoute que l'instrument tahor se nom-
me aussi TàbreL
(2) V. Introduction. « Tel noise i avait de tabour z et de tymbres, de
cornes, de criz etc. » Continuateur de Guillaume de Tyr. ( EKstoriens Occi-
dentaux des Croisades. II. p. 543 .TARB 2J5
' ' ' «^ — —
décrétées par le Sultan Abdul-Medjîd (i). De CjUâiî
. ^ •»
```


## [2026-09-14T03:11:50.873Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la MON_part1.txt MON_part2.txt BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null\necho \"=== MON head ===\"; head -c 600 MON_part1.txt; echo\necho \"=== grep تنباکو ===\"; grep -c \"تنباکو\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null\necho \"=== grep تبیره BQT ===\"; grep -n \"تبیره\\|تبوراک\" BQT_v1_pages.txt | head -5"
}
```


### [2026-09-14T03:11:50.988Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
=== MON head ===
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
=== grep تنباکو ===
MON_part1.txt:2
incoming/MON/MON_2vol_Adena_v1_djvu.txt:2
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
=== grep تبیره BQT ===
```


## [2026-09-14T03:11:58.020Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));v=d['MON'];print(json.dumps(v,ensure_ascii=False,indent=1))\""
}
```


## [2026-09-14T03:11:58.682Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"تنباکو\" MON_part1.txt | head -3 | cut -c1-800"
}
```


### [2026-09-14T03:11:59.071Z] TOOL RESULT

```
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


### [2026-09-14T03:11:59.127Z] TOOL RESULT

```
19993:الای سر قلیان نهند تا تنباکو و آتش را 
59879:دخانیه (غم.)؛ اقسام توتون و تنباکو که برای
```


## [2026-09-14T03:12:05.705Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T03:12:05.712Z] TOOL RESULT

```


```


## [2026-09-14T03:12:08.820Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tobacco",
 "prompt": "Give the full etymology section verbatim: source language (Taino/Carib/Arabic), Spanish tabaco, Portuguese, and any mention of Arabic tabbaq. Also list descendants/related notes."
}
```


## [2026-09-14T03:12:09.813Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tobacco",
 "prompt": "Quote the full etymology entry for tobacco, including any mention of Arabic tabbaq, Taino, Spanish tabaco, Tobago."
}
```


### [2026-09-14T03:12:14.622Z] TOOL RESULT

```
# Etymology of "Tobacco"

**Full Etymology Section:**

The word "tobacco" has been attested since 1588 and was borrowed from Spanish *tabaco*. The Spanish term's origin is debated, potentially deriving from Arabic *ṭubbāq* (referring to *Dittrichia viscosa*), or from Caribbean languages including Kari'na or Taíno. These sources suggest meanings of "roll of tobacco leaves" or "a pipe for smoking tobacco," such as the Taíno *tabago* ("tube for inhaling smoke or powdered intoxicating plants").

**Descendants:**

- Irish: *tobaca*
- Scottish Gaelic: *tombaca*
- Welsh: *tybaco*

**Related Notes:**

The term illustrates significant cross-cultural linguistic exchange, with indigenous Caribbean terminology merging with Spanish colonial language before spreading globally through European languages. The multiple plausible origins reflect historical uncertainty about whether Spanish traders encountered the word in the Americas or adapted existing Arabic botanical terminology.
```


### [2026-09-14T03:12:15.165Z] TOOL RESULT

```
# Etymology of Tobacco

Based on the Online Etymology Dictionary entry, here is the full etymology:

The word **tobacco** entered English in the 1580s from Spanish *tabaco*, which derived from an Arawakan Caribbean language, likely Taino. According to Las Casas (1552), it meant "a roll of tobacco leaves," though Oviedo (1535) suggested it meant "a kind of pipe for smoking tobacco." Scholars favor Las Casas' interpretation.

An alternative native term, *bittin* or *betum* from South America, circulated through 17th-century European languages as *petun* or *petumin*, preserved today in the word "petunia."

The spelling shifted from *ta-* to *to-* during the 18th century. Cultivation began in France around 1556 with imported seeds, and Spain received the plant by 1558.

Regarding Tobago: "The West Indian island of *Tobago* was said to have been named by Columbus in 1498 from Haitian *tambaku* 'pipe,' in reference to the native custom of smoking dried tobacco leaves."

The entry contains no mention of Arabic *tabbaq*.
```


## [2026-09-14T03:12:19.111Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%A8%D8%A7%DA%A9%D9%88",
 "prompt": "Persian تنباکو: give the etymology verbatim (borrowed from what, via which language), pronunciation and meaning."
}
```


## [2026-09-14T03:12:20.871Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B7%D9%86%D8%A8%D9%88%D8%B1",
 "prompt": "Give the Arabic and Persian entries for طنبور: etymology (Persian origin? Aramaic? Akkadian?), meanings, and descendants."
}
```


### [2026-09-14T03:12:23.371Z] TOOL RESULT

```
# Persian تنباکو

**Etymology:** The term was "Borrowed from Portuguese _tabaco_."

**Pronunciation:** In Classical Persian, it's pronounced /tan.baː.ˈkuː/. In Iranian Persian (formal), the IPA is [t̪ʰæm.bɒː.kʰúː].

**Meaning:** This word denotes tobacco, with توتون (tūtūn/tutun) listed as a synonym.
```


### [2026-09-14T03:12:26.377Z] TOOL RESULT

```
# طنبور (Tanbur) - Arabic and Persian Entries

## Arabic Entry

**Etymology:** The word derives from "the Middle Persian ancestor of Classical Persian _تنبور_ (tanbūr)."

**Meanings:**
1. Tanbur (a musical instrument)
2. Archimedes' screw
3. Cylinder (in printing contexts)

**Grammatical Note:** Masculine noun with plural form طَنَابِير (ṭanābīr)

## Persian Entry

**Definition:** Listed as "alternative spelling of _تنبور_ (tambur, 'tanbur (instrument)')"

## Descendants

The term traveled through languages:
- Ottoman Turkish: طنبور (tunbur/tambur)
  - Modern Turkish: tambur
  - Romanian: tambură

**Note:** The Wiktionary entry does not provide information about Aramaic or Akkadian origins—it traces the word's path only from Middle Persian forward.
```


## [2026-09-14T03:12:31.985Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%A8%D9%88%D8%B1",
 "prompt": "Persian تنبور: give etymology verbatim (Middle Persian form? related to tabīra? Greek pandura?), meanings, descendants."
}
```


## [2026-09-14T03:12:33.758Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%A8%DA%A9",
 "prompt": "Persian تنبک (tonbak/donbak): give etymology verbatim, any Middle Persian tumbag, alternative forms دنبک, and meaning."
}
```


### [2026-09-14T03:12:37.980Z] TOOL RESULT

```
# تنبور (Tanbur) - Etymology and Information

## Etymology

The Persian تنبور derives from **Middle Persian** _tambūr_ (in Book Pahlavi and Manichaean forms). According to the Wiktionary source, this word "possibly (with metathesis of consonants) from Ancient Greek πανδοῦρα (pandoûra, 'three-stringed lute')."

## Meanings

In Persian, تنبور refers to a **tanbur**, which is a musical instrument (the entry categorizes it under "Musical instruments").

## Descendants

The Wiktionary entry does not explicitly list descendants of the Persian form. However, it does note that the word appears in multiple related languages with alternative spellings, including طنبور, طنبوره, and طنبار in Persian dialects, as well as related forms in Tajik.

## Related Forms

The entry documents several **alternative forms**: طنبور (tanbūr), طنبوره (tanbūra), and دنبره/دنبوره (various dialectal versions across Persian-speaking regions).
```


### [2026-09-14T03:12:39.224Z] TOOL RESULT

```
# تنبک (Tonbak/Donbak)

## Etymology
According to the Wiktionary entry, this word derives from "Middle Persian tumbag, meaning drum, of imitative origin." It shares roots with Old Armenian թմբուկ (tʻmbuk) and is potentially related to Arabic دَرْبُوكَة (darbūka) and Aramaic forms.

## Meaning
The primary definition given is "tombak" (a percussion instrument), with the synonym ضرب (zarb) also listed.

## Alternative Forms
The entry notes several variant spellings: تمبک (tumbak/tombak), دنبک (dunbak/donbak), and دمبک (dumbak/dombak).

## Linguistic Spread
The word has traveled across multiple languages through Ottoman Turkish derivatives, eventually reaching Turkish, Greek, English (toubeleki), Swahili, and Uyghur—demonstrating the instrument's cultural significance across regions.
```


## [2026-09-14T03:12:47.698Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B7%D8%A8%D9%84",
 "prompt": "Arabic طبل (ṭabl): etymology (native Arabic? Persian? Aramaic?), meaning, derived terms like طبال ṭabbāl, and descendants (Persian طبل, Old French, Spanish atabal)."
}
```


## [2026-09-14T03:12:49.118Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tabor",
 "prompt": "Quote the etymology of tabor, taboret and tambour/tambourine if present on the page: Old French tabour, Arabic tabl or Persian tabir?"
}
```


### [2026-09-14T03:12:53.169Z] TOOL RESULT

```
# Etymology of Tabor, Taboret, and Tambourine

**Tabor:** According to the page, tabor comes from "Old French _tabour_, _tabur_ 'drum; din, noise, commotion' (11c.), probably from Persian _tabir_ 'drum.'"

**Taboret:** The page does not include an etymology for taboret, only mentioning that "Middle English had _tabortete_ 'a small drum.'"

**Tambourine:** The etymology traces back to French _tambourin_, which derives from French _tambour_ "drum," described as "a word altered from Old French _tabour_... by influence of Arabic _tunbur_."

The sources cited are **Persian tabir** (for tabor) and **Arabic tunbur** (influencing tambourine), but not "Arabic tabl" as mentioned in your query.
```


### [2026-09-14T03:12:56.899Z] TOOL RESULT

```
# طبل (Tabl) - Dictionary Entry Summary

## Primary Meanings

The word **طبل** has multiple etymologies and meanings across Arabic and related languages:

1. **Musical Instrument**: "drum," "tom-tom," or a percussive musical device
2. **Drumming Action**: "drumming" or "drumbeat"
3. **Historical Tax**: A territorial or property tax system historically used in al-Andalus and Egypt

## Etymology

The word derives from "Middle Iranian *tabir, tabil" according to the lexicon. A later sense (from mid-8th century onward) traces to Byzantine Greek, ultimately from Latin *tābula*.

## Linguistic Reach

The term appears across multiple language families. Ottoman Turkish adopted it as **طبل** (tabl), while Persian borrowed the form as well. European languages show descendants through Romance pathways, including Spanish **atabal** and French **timbale**.

## Verb Forms

Beyond the noun, Arabic developed verbal forms: **طَبَلَ** (to beat a drum) and **طَبَّلَ** (to drum for someone; to campaign for). The latter can mean "to beat the drum" metaphorically in political contexts.
```


## [2026-09-14T03:13:06.447Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%A8%DB%8C%D8%B1%D9%87",
 "prompt": "Persian تبیره (tabīra): etymology, Middle Persian form, meaning 'drum'. Quote verbatim. If the page does not exist say so."
}
```


## [2026-09-14T03:13:07.559Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=tabor",
 "prompt": "Quote the full American Heritage Dictionary etymology for tabor (and taboret if shown)."
}
```


### [2026-09-14T03:13:07.732Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T03:13:10.983Z] TOOL RESULT

```
# Tabor Etymology

According to the American Heritage Dictionary, the etymology for **tabor** is:

"Middle English _tabour_, from Old French, variant of _tambour_; see TAMBOUR."

The page does not include an entry for "taboret," so I can only provide the tabor etymology as shown.
```


## [2026-09-14T03:13:13.465Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=tambour",
 "prompt": "Quote the full American Heritage Dictionary etymology for tambour, and also tambourine and tambura if shown."
}
```


## [2026-09-14T03:13:14.774Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=tobacco",
 "prompt": "Quote the full American Heritage Dictionary etymology for tobacco — does it mention Arabic tabbaq / a euphoria-causing herb, Spanish tabaco, Taino?"
}
```


### [2026-09-14T03:13:17.409Z] TOOL RESULT

```
Based on the content provided, I can only offer the etymology for **tambour**:

"[Middle English, from Old French, perhaps ultimately from alteration (influenced by Arabic ṭunbūr, ṭanbūr, tambura) of Arabic *tabbūl, hypocoristic form of ṭabl, drum, or ṭubūl, plural of ṭabl; see TABLA, or perhaps ultimately from alteration (influenced by Arabic ṭunbūr, ṭanbūr) of Persian tabīr, tabīra, drum; probably akin to Middle Persian tumbag, and of imitative origin.]"

The entries for **tambourine** and **tambura** are not included in the provided web page content, so I cannot quote their etymologies.
```


### [2026-09-14T03:13:20.238Z] TOOL RESULT

```
# Tobacco Etymology

Yes, the dictionary entry mentions all three sources. Here's the full etymology section:

"[Spanish _tabaco_, probably partly from a Taíno word recorded by a Spanish chronicler as _tabago_, a tube for inhaling smoke or powdered intoxicating plants, and partly from Old Spanish _atabaca, altabaca_, a Mediterranean plant (_Inula viscosa_) having sticky, aromatic leaves widely used in traditional medicine (from Arabic _al-ṭubbāq_ : _al-_, the + _ṭubbāq, ṭabbāq_, the plant _I. viscosa_, from Syriac _dubāqā_, birdlime, elm mucilage used as glue, from _dbaq_, to cling; akin to Arabic _dabiqa_ and Hebrew _dābaq_, to cling).]"

The entry traces tobacco through the Spanish word, which derived partly from a Taíno term for inhaling smoke and partly from Old Spanish words connected to an Arabic plant name (_ṭabbāq_), ultimately linked to Syriac and Semitic roots relating to adhesive substances.
```


## [2026-09-14T03:13:32.946Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB TOBACCO ===\"; grep -n \"^TOBACCO\\|TOBACCO,\" HJB.txt | head\necho \"=== AID tobacco ===\"; grep -n -i \"tambaku\\|tobacco\" AID.txt | head\necho \"=== LKT 1974 ===\"; grep -n \"1974\\.\" LKT.txt | head -3\necho \"=== LKT tabl ===\"; grep -n \"tabl\\b\\|ṭabl\\|tabul\\|tunbur\\|tanbur\" LKT.txt | head -10"
}
```


### [2026-09-14T03:13:33.046Z] TOOL RESULT

```
=== HJB TOBACCO ===
22121:TOBACCO,
22143:TOBACCO,  s.  On  this  subject  we are  not  prepared  to  fumisn  any elaborate  article,  but  merely  to  bring together  a  few  quotations  touching  on the  introduction  of  tobacco  into  India and  the  East,  or  otherwise  of  interest.
22146:TOBACCO.
22148:TOBACCO,
22168:TOBACCO.
=== AID tobacco ===
1030:Bhddu.  [Uriya.]  The  name  of  a degraded  class  of  Uriya  Brdhmans  j they  prepare  tobacco.
1626:Chilam.  [Hindustani.]  The  part  of the  hukka  in  which  the  tobacco  or gdnjd  burns ;   thence  used  also  for the  whole  pipe.
2735:Hamaku.  [Bengali.]  The  name  of a   plant  resembling  tobacco,  but smaller  in  size  and  strorffeer  in  its narcotic  effects.
2867:Hookah.  [Arabic  huqqak.]  An  appa- ratus for  smoking,  consisting  of  a box  in  which  the  tobacco  burns,  a vessel  of  water  through  which  the smoke  passes,  and  a   long  pliant pipe  through  which  it  is  conveyed to  the  mouth.
=== LKT 1974 ===
4452:1974.  Tk.  tabur:
=== LKT tabl ===
4005:17G2.  Pers.  sah: 'König,  Herrscher'  [Horn  NpEt  S.  170, Nr.  772];  hieraus  zur  Bezeichnung  des Kaisers  von  Persien  u.a.  rum.  §ah,  ^ach; russ.  sah,  bulg.  serb.  sah,  öech.  sach, poln.  stach;  frz.  chah;  dtsch.  Schah,  engl. shah.  Aus  dem  beim  Schachspiel  üb- lichen Ausruf:  säh  mät  [s.  hier  Nr.  1443] entstand  allgemein  der  Name  für  dieses Spiel:  rum.  sach,  it.  scacco,  prov.  escac, frz.  ^chec,  gewöhnlich  erhecs,  sp.  jaque [nur  im  Zurufe  jaque  mate],  pg.  xaque; ndl.  schaakspel,  eugl.chpss,  disch.  Schach, Abschach  [in  Lessings  Nathan  II,  1]; russ.  Sah,  bulg.  sah,  cech.  sach,  poln. szach;  das  'Schachbrett'  heißt  danach it.  scacchiero,  frz.  Miiquier,  sp.  jaquel; russ.  Sahmaty;  mhd.  schdchzabel  [<  lat. tabula],  hieraus  dial.  Schachzagel,  Schäf- zagel  [also  volksetymologisch  als  'Schafs- schwanz' gedeutet,  vgl.  Andresen  DVE 29].  Endlich  wurde  aus  afrz.  eschec  zur Bezeichnung  eines  'Zahlscheins'  [Vor- schlag des  Deutschen  Allgemeinen Sprachvereins]  engl,  check,  frz.  cheque.
4445:Ar.  tabl.]
4447:1971.  Ar.  tabl:
```


## [2026-09-14T03:13:36.295Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4435,4475p' LKT.txt\necho \"=== HJB tobacco entry ===\"; sed -n '22143,22150p' HJB.txt | cut -c1-1500"
}
```


### [2026-09-14T03:13:36.391Z] TOOL RESULT

```
'Beil,  Axt'  [Horn  NpEt  S.  84,  Nr.  374], ebenso  tk.  tabar,  tcber;  hieraus  russ. topor  'Beil',  topon'sce  'Stiel  am  Beile', bulg.  öech.  topor,  poln.  topör  'Beil,  Axt' ; rum.  topor  'dass.',  topori^te  'Axtstiel'. —  [Dagegen  kommt  der  Name  Taba- ristan,  die  Landschaft  am  Südufer  des Kaspischen  Meeres,  welche  die  pers. Provinzen  Gilän,  Mäzändärän  u.  Ästärä- bäd  umfaßt,  von  dem  einheimischen Worte  t(tbar  'Gebirge'  und  heißt  mithin 'Gebirgsland',  ZDMG  XLVI,  186.]  [Mikl SlEtWi)  3.-.9a.
1965.  Ar.  tabäsir: 'Bamliuszucker',  d.  h.  zuckerhaltige  Kie- selknollen, die  an  den  Knoten  der  Bam- busstänime  abgeschieden  werden  [selbst aus  dem  Ind.  stammend,  ZDMG  L.  650, und  zwar  von  sskr.  tavakhshira];  hiei- aus  pg.  tabaxir  'Bambuszucker',  t.  dos alfaiates  [aus  ar.  al-liajjät  'der  Schnei- der'] 'Schneiderkreide',  frz.  tebachier, tabaschir  ;  engl,  tabasheer,  dtsch.  Taba- schir.  Über  tk.  tebesir  'Kreide'  wurde rum.  tibi^ir  'dass '  [DE  345.  Eguilaz 497.  Löbel  EITAP  95.  Hobson-Jobsou 887.    Lammens  Rem  231.
1966.  Ar.  tabdil:
'Änderung'  [subsl.  Infin.  von  badala  II 'ändern'],  ebenso  tk.  tebdil  'verstohlen, incognito';  hieraus  rum.  tiptil  'sachte, verstohlen'.
1967.  Ar.  tabi'a:
'Natur,  Gewohnheit',  ebenso  tk.  tabiet; hieraus  rum.  tabiet  'Vorliebe,  Ange- wöhnung', Adj.  mit  tk.  Endung  tabietUü 'bequemlich'.
1968  Ar.  tabih: 'Gekocht',  bes.  'gekochte  Milch";  hieraus pg.  tabefe  'mit  Mehl  und  Zucker  ge- kochte Schatmilch'  [Constancio  Dicc913; DE  34.5.    Eguilaz  4'.i8].
1969.  Ar.  ta'bija: 'Verschanzung,  Bastei',  ebenso  tk.  tabijet 'dass.'  [Kelekian  Kämüs  787;  woraus wieder  ar.  täbije  entstand,  vgl.  SKAW Wien  ph.  h.  Gl.  GV,  435],  hieraus  rum. tabie  'I3astion,  Wall  und  Graben'.
1970.  Ar.  tabik:
'Etwas  aneinander  Passendes';  hieraus sp.pg.  <aft«2Me 'Zwischenwand  aus  Steinen und  Lehm'.  [DE  344.  ML  8512.  Eguilaz 498  [wo  wohl  mit  Unrecht  als  Grund- wort tasbik  angegeben  wird].
Ar.  tabl.]
156
1971.  Ar.  tabl:
'Pauke'  [vgl. hei  HesycliiusTcißaXa 'Pauke' bei  lien  Paitliern] ;  hieraus  mit  ar.  Art. it.  ataballo,  taballo,  sp.  atabal,  p^.  ata- bale,  iiat.  tabal,  nifrz.  attabal  Tauke', prov.  iabalh  'GlockenschwcngeP;  mit siav.  Endung  hulg.  fjuiiibelek,  serb.  ta- lanibak;  ru.«s.  litaicra,  litawry,  pohi. litau-ra  'Pauke';  mit  lat.  tynipanum kontaminiert,  wurde  sp.  titubol,  frz.  tim- bale  'Pauke',  rum.  diblu,  lUplä  'Geige'. [DE  :J07.    Eguilaz  :29.ö.    ML  8513.
197:2.  Polyues.  tabn: 'Unverletzlich';  es  können  für  den  Be- wohner Polynesiens  gottgeweihte  Gegen- stände, Orte,  Personen  sein;  hieraus frz.  tabou,  engl,  taboo  [z.  B.  «  tabooed snbject  of  conrersnfion  'ein  Gesprächs- stoff, an  den  nicht  gerührt  werden  darf], dtsch.  Tabu  [z.  B.  halb  scherzhaft  'das ist  mir  tabu'].
1973.  Tk.-tat.  tabiui:
'Herde';  hieraus  russ.  tabun,  poln.  tabun 'Pferdeherde'.  [Gorjajew  .3.59.  Mikl SlEtWb  346  a.
1974.  Tk.  tabur:
'Heerlager,  Abteilung,  Bataillon'  [vom Stamme  tap  'unten.  Sohle,  Spur  > nachspüren',  vgl.  cag,  tapkur  'die  zum Beutemachen  ausgeschickte  Kolonne', Vämhery  TktEtWh  S.  157,  Nr.  17s!  I]; hieraus  rum.  tabärä  'Heer,  Heerlager'; russ.  tabor  'Lager,  Zigeuneringer',  bulg. serb.  poln.  klruss.  tabor,  cech.  täbor 'Lager',  selbst  im  Dtsch.  Tabor  'ein mehr  oder  weniger  befestigtes  Gebäude, meisliens  am  Ende  des  Ortes  liegend' [in  Österreich,  bes.  im  Salzburgischen, vffl.  Taborcdpe].  [Mikl  SlEtWb  346  a. Löbel  EITAP  90.
1975.  Ar.  täbüt:
'Kasten,  Sarg'  [aus  äg.  tht  'Arche',  ZD MG  XLVI,  123,  woraus  auch  hebr.  tefiä, aram.  te^übä,  nriit  Dissimilation  gr. KißujTÖq  'Arche  >  Kasten';  die  unhalt- baren Ansichten  der  ar.  Gelehrten  über dieser  Wort  und  seine  Erklärung  s. FLEISCHER  in  ßSAW  XVIH,  310]; hieraus  siz.  tabbutu  'Sarg',  sp.  atahud, ataiid  'dass.',  wahrscheinlich  auch  frz. bahnt,  pg.  bahü,  bahul,  sp  baill,  it.  baute. prov.  baue;  russ.  batd  'Koffer,  Kasten' [wofür  ML  1008  als  Ausgan ^'spunkt *ba-ut  mit  ,ganz  unbekanntem"  Etymon ansetzt].  [GrSVociSic  247.  DE"  214. Eguilaz  299.
1976.  Ar.  tadkira:
'Pafä'  [vom  Vb.  d'^ikara  'erinnern,  er- wähnen'], ebenso  tk.  tezkire  'dass.,  Doku- ment'; hieraus  frz.  teskM,  rum.  te§- cherea  Tassierschein,  Beglaubigungs- schreiben'.
1977.  Ar.  tafar:
'Hinterer  Sattelriemeii,  Schwanzriemen'; hieraus  mit  ar.  Art.  sp.  atafurra,  ata- harra,  pg.  ataful  'bunter  Riemen,  den die  Maultiere  als  Schwanzriemen  tragen'. [DE  208.    Eguilaz  299.
1978.  Hebr.  täcpas:
'Ergreifen,  gefangen  nehmen',  dazu  täfüs 'Gefangener';  hieraus  jüd.-dtsch.  Toffis 'Gefangener',  Doufes  'Gefängnis',  auch im  it.  Gergo  tafüs  'Falle,  Gefängnis'. [Ascoli,  Sludi  orientali  e  linguistici  403.
1979.  Berb.  Tafilelt:
Auch  Tafilet,  N.  pr.,  zu  Marokko  ge- hörige Oase  südlich  des  Atlas,  in  der Lederindustrie  heimisch  ist;  hieraus  kat. pg.  tafilet,  sp.  tafilete  'feines  Leder, Saffian'.
1980.  Ar.  taforma:
'Art  Adler'  [vulg.-ar.,  wahrscheinlich  aus dem  Berb.];  hieraus  mit  ar.  Art.  sp.  ata- horma  'Falke  von  aschgrauer  Farbe  mit rotgefleckter  Brust  und  gelben  Beinen'. [DE  209.    Eguilaz  299.    ML  8524.
1981.  Pers.  täftä:
'Zeugsloff'  [eigentlich  'gewoben',  part. pass.  von  täftän  'weben,  drehen,  spinnen' Horn  NpEt  S.  83,  Nr.  372];  hieraus  zur Bezeichnung  eines  bestimmten  Seiden- stoffes rum.  taftä,  it.  taffetä,  frz.  taffetas, pg.  tafetä,  kat.  tafeta,  sp.  iafetdn;  engl. taffeta,  taffeti/,  dtsch.  Ta/fet,  Taft,  ndl. taf;  wohl  auch  poln.  taftaj,  Pferde- decke'; ferner  russ.  tnfta,  poln.  tafta, serb.  tafet  'Taft'.  [ML  8525.  Gorjajew 361.  Karlowicz  427  (mit  tat.  tahtuj  als Grundwort  für  das  poln.  W^ort).
1982.  Tagalog:
N.  pr.,  malayische  Bevölkerung  auf  einem Teile  der  Philippinen,  die  sich  selbst Tagalog  nennen  [aus  der  Partikel  taga 'von  .  .  .  her'  und  ilog  'Flufa',  also  'Fluß- bewohner'];  nach  diesen  Tagalen  ist  eine sehr  feine  Strohsorte  für  Hüte  Togal benannt  [Globus  LXVII,  336].
1983.  Tk.  tagar:
'Ledersack,  Gefäß':  hieraus  russ.  tagar, bulg.  tagar,  serb.  dagara  'Koib'  [vgl. ngr.  TCYCtpi,  mlat.  tagarra].  [Gorjajew 3.59.    Mikl  SlEtWb  346  a.
1984.  Hebr.  tähaö:
'Unten',  modein  ausgesprochen  töfies, von  oberdtsch.  Juden  döhes,  hieraus jüd.-dtsch.  Doches,  Bokes  'Podex'.
1985.  Ar.  tahiu:
'Mehl',  ebenso  {k.  tahyn  'dass.,  Sesani- mehl'  [Kelekian  Kämüs  801a];  hieraus rum.  tahin  'Brei'.
=== HJB tobacco entry ===
TOBACCO,  s.  On  this  subject  we are  not  prepared  to  fumisn  any elaborate  article,  but  merely  to  bring together  a  few  quotations  touching  on the  introduction  of  tobacco  into  India and  the  East,  or  otherwise  of  interest.
[?  c.  1550.—".  .  .  Abu  Kir  would  CMiy the  cloth  to  the  market-street  and  sell  iC and  with  its  price  buy  meat  and  regetables and  iohaooo.  .  .  .**— -Burtoii,  Arab.  jV^^dUt. vii.  210.  The  only  mention  in  the  ^tgikU and  the  insertion  of  some  scribe.]
„  "It  has  happened  to  me  seTersl times,  that  going  through  the  provinces  of Guatemala  and  Nicaragua  1  have  entered the  house  of  an  Indian  who  had  taken  this herb,  which  in  the  Mexican  language  is called  tabacco,  and  immediately  percoiTed
TOBACCO.
925
TOBACCO,
the  sharp  fetid  smell  of  this  tml;^  diabolical and  stinking  smoke,  I  was  obliged  to  go away  in  haste,  and  seek  some  other  place." —Oirolamo  Bemoni,  Hak.  Soc.  p.  81.  [The word  tabaeo  is  from  the  language  of  Hayti, and  meant^  first,  the  pipe,  secondly,  the plant,  thirdly,  the  sleep  which  followed  its use  {kr.  J.  Plait,  9  ser.  N,  d:  Q,  viii.  822).]
1686.—"  Et  hi "  (viz.  Ralph  Lane  and  the first  settlers  in  Viiginia)  "reduces  Indicam illam  plantam  quam  Tabaccam  vocant  et Nicotiam,  qua  contra  cruditates  ab  Indis edocti,  usi  erant,  in  Angliam  primi,  quod suam,  intulerunt.  Ex  illo  sane  tempore  usu coepit  esse  creberrimo,  et  magno  pretio, dum  quam  plurimi  graveolentem  illius fumum,  alii  lascivientes,  alii  valetudini  con- sulentes,  per  tubulum  testaceum  inexplebili aviditate  passim  hauriunt,  et  mox  e  naribus eflSant;  adeo  ut  tabemae  Tabacoanae  non minus  quam  cervisiariae  et  vinariae  passim per  oppida  habeantur.  Ut  Anglorum  cor- pora (quod  salse  ille  dixit)  qui  hao  plants tantoperedelectantur  in  BarDaronimnaturam degenerasse  videantur ;  quum  iisdem  quibus Barbari  delectentur  et  sanari  se  posse credant."  —  OuL  Oamdeni^  Annal.  Bentm Anglicamim  .  .  .  regn.  Muabetha,  ed.  1717, ii.  449.
```


## [2026-09-14T03:13:45.806Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/tanbur",
 "prompt": "Quote what the Encyclopaedia Iranica says about the origin/etymology of the word tanbūr (Middle Persian, Greek pandoura, Akkadian, Arabic ṭunbūr) and its history."
}
```


### [2026-09-14T03:13:46.984Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T03:13:47.014Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tambour",
 "prompt": "English/French tambour: give the etymology verbatim including Old French tabour, Arabic tunbur/tabl, Persian tabir."
}
```


### [2026-09-14T03:13:52.942Z] TOOL RESULT

```
# Etymology of Tambour

Based on the Wiktionary entry, here's the etymological path:

**English tambour** comes from "French _tambour_ ("drum"), from Arabic _ṭunbūr_, from the Middle Persian ancestor of Classical Persian _tanbūr_."

**French tambour** derives from "Arabic _ṭunbūr_ or Persian _tabir_ ("drum")."

The entry notes that English tambour is "a doublet of _tabor_ and _tanbur_" and indicates related terms in Armenian and other languages.

However, the Wiktionary source provided does **not** include explicit references to "Old French tabour" or list "tabl" as a documented etymological stage. The documented chain runs: Modern English/French ← Arabic/Persian ← Middle Persian, without the intermediate Old French form you mentioned appearing in this particular dictionary entry.
```


## [2026-09-14T03:14:01.590Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D8%A8%DB%8C%D8%B1%D9%87/",
 "prompt": "Quote the فرهنگ معین and لغت‌نامه دهخدا entries for تبیره — meaning, origin tag (e.g. [په.] Pahlavi), and any cited forms like تبوراک or تبیر."
}
```


## [2026-09-14T03:14:03.041Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D9%86%D8%A8%DA%A9/",
 "prompt": "Quote the فرهنگ معین entry for تنبک — meaning and origin tag in brackets; also دهخدا if it gives an origin."
}
```


### [2026-09-14T03:14:06.626Z] TOOL RESULT

```
# تبیره - Dictionary Entries

## فرهنگ معین
**Entry:** "(تَ رِ ) (اِ. ) دهل ، کوس ، طبل دو سر."

*Translation:* A two-headed drum; a type of percussion instrument.

---

## لغت‌نامه دهخدا

**Primary definition:** This historical lexicon identifies تبیره as a large drum, synonymous with دهل (dahl), کوس (kos), طبل (tabl), and نقاره (naqqāra).

**Notable variant form cited:** تبیر (tabyīr) - the base form from which تبیره derives.

**Secondary meanings:** The entry also notes a figurative usage referring to sound or noise generally, and includes an archaic reference to a specific structure for waste disposal.

The dictionary supports these definitions through classical Persian poetry citations from authors such as Ferdowsi, Nizami, and Asadi, demonstrating the word's historical usage in martial and ceremonial contexts.
```


### [2026-09-14T03:14:08.905Z] TOOL RESULT

```
# تنبک Entry from Farhangs

## Farhang-e Moein Definition

According to Farhang-e Moein, تنبک is described as:

> "(تُ بَ) (اِ. ) یکی از سازها که به آن ضرب هم گویند. آن را از چوب و سفال یا فلز سازند و در یک سوی آن پوستی نازک کشند"

In essence, it's one of the musical instruments also called ضرب (percussion), made from wood, clay, or metal with a thin membrane stretched on one side.

## Dehkhoda Entry

Dehkhoda provides historical context, noting that تنبک is a small drum-like instrument used by performers and dancers. The entry references classical Persian poetry and describes both its musical application and construction from wood and ceramic materials with stretched skin that players strike with their fingers.

The Dehkhoda entry also mentions an alternate meaning related to eating food with thumb and forefinger, though the primary definition concerns the percussion instrument.
```


## [2026-09-14T03:14:16.126Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D9%86%D8%A8%D8%A7%DA%A9%D9%88/",
 "prompt": "Quote the فرهنگ معین entry for تنباکو — meaning and any origin tag in brackets (e.g. [پرتغالی], [فر.], [اسپانیایی]); also دهخدا's origin note if any."
}
```


## [2026-09-14T03:14:19.232Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 تبیر ===\"; grep -n \"تبیر\" BQT_v1_pages.txt | head -5 | cut -c1-400\necho \"=== BQT v2 طنبور/تنبور ===\"; grep -n \"طنبور\\|تنبور\" BQT_v2_pages.txt BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -8 | cut -c1-300\necho \"=== ARY ===\"; grep -n \"تبیره\\|طبل\\|تنبور\\|تنباکو\" incoming/ARY/ARY_pages.txt | head -10 | cut -c1-300"
}
```


### [2026-09-14T03:14:19.345Z] TOOL RESULT

```
=== BQT v1 تبیر ===
28813:تبیر است که دهل و کوی وطبلو تاره بامد٩۷»‏
28826:۲- زگ تبیر.  ٩۳‏ - وك: کب وطب.
=== BQT v2 طنبور/تنبور ===
incoming/BQT/BQT_v3_pages.txt:784:‎asl‏ طنبور بزرکی که دستهٌ کوتاهی‌داشته ‎ash‏
incoming/BQT/BQT_v3_pages.txt:815:فاخته دای زن وبط ‎oat‏ طنبورزلا. «منوچهری ‎he gals‏
incoming/BQT/BQT_v3_pages.txt:905:کپی چفانه و طنبور و عود و که شاشنگه .
incoming/BQT/BQT_v3_pages.txt:4108:و عود و طنبور ورباب را ‎oly‏ وازند. ۸ تلر
incoming/BQT/BQT_v3_pages.txt:4259:شش آا - با فوقانیبالف کشیده طنبور
incoming/BQT/BQT_v3_pages.txt:4260:شش‌تار را گوبند چتانکه سه تا طنبوره سه تاره
incoming/BQT/BQT_v3_pages.txt:4264:و دال بی قطه (۳) , طنبور شش تار نواختن را
incoming/BQT/BQT_v3_pages.txt:5255:‎ARS‏ - بر وزن کجك » طنبوره را
=== ARY ===
2477:۲- معطی این واژه در برخی زبان‌های هند و اروپایی: اسطبل» محل نگهداری دام. :
2478:۳- واژه‌ی فارسی "اسطبل" از واژه‌ی لاتین 57۸811181 آمده د این واژه‌ی لانین خود یا واژه‌های اوستایی
```


### [2026-09-14T03:14:21.282Z] TOOL RESULT

```
# تنباکو (Tobacco)

## Farhangi Moein Entry

According to Farhangi Moein: "(تَ) (اِ. ) گیاهی است یک ساله ، بومی قارة امریکا که به وسیلة اسپانیایی ها به اروپا برده شده"

This describes tobacco as "an annual plant native to the American continent that was brought to Europe by the Spanish." The entry notes it belongs to the tobacco genus, with dried leaves consumed through smoking and containing the toxic substance nicotine.

## Dehkhoda's Origin Note

Dehkhoda provides historical context, explaining that tobacco arrived in the Indian subcontinent from Europe during the Akbar Shah era, and that the Spanish introduced it to Europe from the island of Tabago. The entry emphasizes tobacco's dangerous toxic alkaloid composition (nicotine) and notes that in most civilized nations, its cultivation and trade remain under government regulation.
```


## [2026-09-14T03:14:25.904Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=28795 && NR<=28830' BQT_v1_pages.txt\necho \"=== page tag ===\"; awk 'NR<=28830 && /\\[pdf page/ {p=$0} END{print p}' BQT_v1_pages.txt"
}
```


### [2026-09-14T03:14:26.948Z] TOOL RESULT

```
واو وکاف » طبقی باش که بقالان اجناس‌ونانبابان
نان در آن نیند ۵ و نام قلعه ای عم هست ور
کتار قازم که حضرت رمالت صلوات ال علیه از
کنارکرفتد؟ .
باه
یه - بفتح اول وانی وظهور حای هوز,
سل سا بر ان
ایم شدماست - و گوشت ت فرم و نازكك را لین
9
نبهر ه - با رای فرشت‌بر وزن طبقحه»
قبیازه ٩‏ - بروزن‌خسیازه. تبولرزی‌را
کوشد که سیب برآمد کی وبزر که شدن سیرز
بهم رسیده باشد » وباین هعنی بجای زای تقطهدار
ذال نقطه دار هم بنظرآعده است
قییر ه بروژن لفس » دهل و کوس‌ونفاره
وطبل را گونند - وخاله‌ای را : یز کفته اند که
سر کین ویلیدیها درآن رده
بر ۵ - بفتح اول بروزن کیره ؛ بممنی
تبیر است که دهل و کوی وطبلو تاره بامد٩۷»‏
وسنیکوابند ثبیره دهلی است کهمیان‌آن باريك
وهردوسرش بهن می‌باشد - وخانه ای که در آن
پلدیها ریز ند۱۴.
لپ « بفتح اول و سکون ثانی ‏ بمعنی
اضطرا اب و بی‌قراری ویی‌آرامی باشد۱۴,
)۱( چش تاموده ۳
۱ رك لك] : ۲۰6 «تبن‌مکه».
- بادنکتی‌چون «می‌از روز کار پیشتر
۴ راه: تبوك.
«مسجم‌البلدان» ور ۳ ص‌
- از: ۶ب سه بازء(ه .
۱ - ییره زن بزد طبل تین
۲- زگ تبیر.  ٩۳‏ - وك: کب وطب.
از تپیدن . رکه: ثابا که .
که اشطر اب دسرازت باشد؟۷.
رس و
تو نبوراکی بدست ومن عکی‌بربط بچنگه.
=== page tag ===
```


## [2026-09-14T03:14:33.208Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" BQT_v1_pages.txt | head -3\nawk 'NR<=28813' BQT_v1_pages.txt | grep -n \"pdf page\" | tail -2"
}
```


### [2026-09-14T03:14:34.245Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:14:37.589Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 BQT_v1_pages.txt | cat -A | head -5 | cut -c1-200\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace')\nlines=t.readlines()\nimport re\n# count form feeds before line 28813\ntxt=''.join(lines[:28813])\nprint('formfeeds before:',txt.count('\\f'))\nprint('total lines',len(lines))\nEOF"
}
```


### [2026-09-14T03:14:38.659Z] TOOL RESULT

```
^LM-[M-1 M-[M-5 M-[M-1! M-[M-1$
7 M-YM-^EM-YM-^HM-YM-^E M-[M-3 M-YM-^DM-XM-'M-YM-^E$
M-YM-^E M-[M-1 0 M-YM-^H M-XM-7M-YM-^B M-XM-5M-YM-^AM-XM-1M-XM-1M-XM-1M-YM-^FM-[M-^LM-XM-'M-XM-9M-XM-/M-XM-1M-[M-^LM-XM-1M-YM-^EM-XM-'M-XM-1M-YM-^HM-[M-^L$
M-[M-0 M-[M-1 "M-[M-3$
M-[M-3$
formfeeds before: 695
total lines 32486
```


## [2026-09-14T03:14:52.618Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON تبوراک/تبیره ===\"; grep -n \"تبوراک\\|تبیره\\|تبیر\" MON_part1.txt | head -8 | cut -c1-300\necho \"=== NYB tabur ===\"; grep -n -i \"tabūr\\|tabur\\|tabīr\" NYB_vol2_glossary.txt | head -10\necho \"=== PHD tab ===\"; grep -n -i \"\\btabl\\|tab[iū]r\" PHD.txt PHD_mackenzie.txt | head -10\necho \"=== FRS/FSF تبیره ===\"; grep -n \"تبیره\\|تبیر\" FRS_pages.txt FSF_pages.txt 2>/dev/null | head -8 | cut -c1-300"
}
```


### [2026-09-14T03:14:52.764Z] TOOL RESULT

```
=== MON تبوراک/تبیره ===
37497:رفتاری؛ ج. تبیرات. 
37743:تبوراک: تاه (.) طبلی کوچک که 
37757:تبیر ه: ()۱۵01۳9 [- تبیر ] (.) دهل» کوس» 
92086:طبل‌زن» طبل‌نواز» تبیر‌زن. 
=== NYB tabur ===
=== PHD tab ===
PHD.txt:31:'The script of the Pahlavi books derives ultimately from that of the official Aramaic of the Achaemenian empire. In the course of time, however, a high degree of ambiguity has developed in the script. Table I shows the development of the letters from Imperial Aramaic (with the transliteration and names of letters commonly used by Semitists), through the distinct forms used in the Parthian and Persian inscriptions of the third century A.D., and the archaic manuscript forms of the Psalter fragment (about seventh century),! to those of the Zoroastrian books. In addition to the multiple values of the letters listed, some of them may represent combinations of letters in certain contexts, e.g. - or 35 for 3+».
PHD.txt:36:TABLE I C Imperia | Jet | Pahlavi ep: „M c6 Аз As T A b (bēt) J | — — _) 8 g(gimel) А | g EY n 5 d(dālet) — $9 | 7 3 E eh h (hà) 7) ot се ed » wem Ж. | 2 2 L | z (zayin) ) ) $ € $ ken ]7) | N gv N =? t (të) O уу £ y (vod) x | ) 4 a3 au кыр y | 7 3 ) $ Llame) G y 1 L N nom 5| D| + < pen 05 | 2 |} | 6 рм s(samk) АЈ /7 D A3 V ‘ (ауіп) v 7 = м = W у р (pē) 2 ^» Q a д s(sādē) у y =D tv | es C. q (dčf) P kel = т | -m = ay r (re) Y uL "ORE м aši ap Gin) Ҹи б 22. x PS ET t (tàw) A D y Ki y
PHD.txt:45:The full scheme of transliteration is given in Table II. 'T'he order is still that of the Aramaic alphabet, taking account of the first value of each letter.
PHD.txt:47:INTRODUCTION xiii TABLE II
PHD.txt:463:maškīzaģ [mfkyck' | N ~a] small mussuck, skin 'table-cloth'.
PHD.txt:595:~ih: bitterness. taxt [2А | N ~] throne. ~ag [-#! | N ~a] tablet, plank, (chess) board. taxtan, taz- [Phtn', tc- | M rem, tz-] run, flow. išnīh : flow. tāxtan, taz- [?Аїп!, Pc- | M Рс-, N ~] cause to run, flow; chase; pour. taxt-gàh [?hig’h | N <] couch. taz-, —išnih, v. taxtan. táz-, v. tāxtan, tazāģ [tc’k'] flowing, running. tāzānaģ [P enh | N tāz(y)āna] whip. tazënidan, tazën- [tcyn-ytn'] = tāxtan. tazidan, taz- [tc-ytn'] = taxtan. Itázig [Pcyk! | N tázi] swift, fast. "Táüzig [Pcyk! | N tāzi] Arab. tēmār [tym] | M tym’r, N ~] sorrow, grief, care. ltërag [tylk' | N tēra] dark, turbid. *térag [tylk'] (mountain) peak, summit. téx [tyh | N téy] sharp edge, ridge; ray. Mēz [tye | M tyz, N ~] quick. ~ih: speed. *téz [tye | (P tyj), N ~] sharp. ~ih: sharpness. *tidag [tytk' | (N dida)] pupil (of eye). tigr [HTY A < А Шу; tgl | M tygr, N tir] arrow. *tihóg [tyh:wk! | N tihi] small grey partridge. tir, v. tigr. Tir [tyl | M tyr, N ~] a god (confused with Tištar); astr. Mercury; cal. 4th month; 13th day. tis [MNDOM < А mnd‘m; ts | M, J tys] thing, affair. «iz [-c | M -yc] (with a negative) по... at all. tišn [tyšn!] thirst. tišnag [tyfnk! | M tyšng, N ~a] thirsty. ~th: thirst. Tištar [гуй | № ~] astr. Sirius. të [LK < A l-k | M tw, N tu] thou, thee. *tóf [twp | N to] layer. tóhmag [twhmk' | M twhmg, N tuxma] seed; stock, family. tom [t(w)m | M tm, N tam] darkness. -tom [-twm | (M. -dwm)] suffix forming superlative adjectives. tóm [twm | (M twhm, N tuxm)] seed, family. tórag [twlk' | N tora] jackal. tūšag [twšk! | N tófa] provisions. tóxtan, töz- [twhtn', twc- | M twz-, N ~] atone, expiate. ~išn: atonement, expiation. tóz [twe | N ~] bark, skin.
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
PHD.txt:3685:skin Carm, dawāl, pēst; tēz; (a.) post- én; ~bag hambān, mašk; ~ 'table- cloth! maškīzag.
PHD.txt:3924:table xwān; ‘table-cloth’ maškīzag.
PHD.txt:3925:tablet taxtag.
=== FRS/FSF تبیره ===
FRS_pages.txt:6856: ‫او بردمانده خيرخی ]‬      ‫چشم زی‬                 ‫کرسنه روباه شد تاآن تبیر‬
FRS_pages.txt:6868:‫‪ - 4‬این‌افت فقطدرع هست بدون مثال‪- ۵. .‬ل ‪ :‬تببرطیل باشدتبیرهنیزگویند»‬
FRS_pages.txt:18479:‫تعریف ؛ ای زن وی ] ‪ ۰‬ه ‪ -‬نْ؛ تبیره طبل دو سر بساشادی»رنسخ این‌لفت را‬
FRS_pages.txt:22361:                                           ‫تبیر ‪۰4۱‬‬         ‫ث‌‬
FRS_pages.txt:22362:                                          ‫تبیره ‪۹۳4‬‬                      ‫ت‪۳‬ا‪۹۰‬‬
FSF_pages.txt:2628:  ‫(‪)۱-۸۳۱-۷۵‬‬                                               ‫همی از تبیره شود گوش کر‬
FSF_pages.txt:10283:                                                                                   ‫(پذیر ه» «وتبیر ه»‪:‬‬
FSF_pages.txt:18366:           ‫از پیت کوس خورده کوه تبیر‬                             ‫آنورد گرز گران‪...‬‬
```


## [2026-09-14T03:14:59.074Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '37735,37775p' MON_part1.txt\necho \"=== طنبور/تنبور in MON ===\"; grep -n \"طنبور\\|تنبور\" MON_part1.txt MON_part2.txt | head -8 | cut -c1-300"
}
```


### [2026-09-14T03:14:59.165Z] TOOL RESULT

```
نبنی: : ۵028۳۴1) [ع. ۰] (مص‌ل.) سر خواندن» 
فرزند گرفتن» به فرزندی پذیرفتن. (امص.) 
فرزند خواندگی. 

و۰۶ مبسدداه) [ع.] (مص‌ل.) جای کرفتن» 
جای ساختن. 

تبوراک: تاه (.) طبلی کوچک که 
زارعان به جهت رمانیدن جانوران از کشتزار 
نوازند. دف» دایره. عربال. طبقی بهن و 
بز رگ از چوب ساخته که بقالان اجناس و 
نانوایان نان در آن نهند. 

شسویب: 20۷]0) [ع.] (مسصم.) بات بات 
کردن کتاب و نوشته» تقسیم کردن کتاب به 
فصول. 

تبیان: (ع.] (مص‌ل.) روشن کردن» 
پیدا کردن» آشکار کردن. (امص.) گزارش؛ 
شرح. 

تبیر ه: ()۱۵01۳9 [- تبیر ] (.) دهل» کوس» 
طبل؛ نقاره. خانه‌ای که در آن بلیدی‌ها 
زبر بل 

تسبین: ۵02(۷00) [ع.] (مسصل.) سجای 
آوردن» شناختن. هویدا شدن» نبا کمن 
(مصم.) بیدا کردن» آشکار کردن. 
تبییضص: ها و سپید کردن. 
پاکنویس کردن؟ ج 

تسیین: ۵0/۲0 2 [ ات9 ۱ مه کردن: 
آشکار کردن» روشن کردن. روشن ِ 
(امص.) روشنگری. روش ن‌گویی؛ ج 
تسینات. 

تنب ۲0 (- تب - تاب] (.) اضطراب؛ 
بی‌قراری» بی آرامی. 

تباک: ها (ا.) اضطراب» بی‌قراری. 
=== طنبور/تنبور in MON ===
MON_part2.txt:60807:عود طنبورء گیتار؛ ج. معازف. 
MON_part1.txt:22129:طنبور ماندی است کاسه تخر کل و دسته 
MON_part1.txt:24751:بلانوش: 5 |ع. ف. - بلانوشنده| ‏ از موسیقی. بلبل طنبور: (مت.) پل طننور و 
MON_part1.txt:43946:تنبور. ۲ [- دنبره - طنبور. معر.] (1.) 
MON_part1.txt:55680:زیر تارهای آلات موسیقی (تار و طنبور و 
MON_part1.txt:61706:بر کاسة عود و طنبور و مانند آن وصل کنند. 
MON_part1.txt:61760:کارد» شمشیر» طنبور؛ عود و غیره. مکتوبی 
MON_part1.txt:81538:(مست.) طنبوری است که سه تار به آن سته
```


## [2026-09-14T03:15:08.198Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '43940,43960p' MON_part1.txt\necho \"=== طبل ===\"; grep -n \"^طبل\\|طبل:\" MON_part2.txt MON_part1.txt | head -5 | cut -c1-200"
}
```


### [2026-09-14T03:15:08.293Z] TOOL RESULT

```
یک لنکگک‌بار خل ل: 

تسد ه: (0-)200-27102) (افا.) چنننده» 
لرزنده. (ا.) بنایی که در حال فرو ریختن 
است. 

تنبور. ۲ [- دنبره - طنبور. معر.] (1.) 
(مس.) یکی از آلت‌های موسیقی 
ذوی‌الاوتار که دسته‌ای دراز و کاسه‌ای 
کو جک مانند سه تار دارد. 

تسشوسه: (0-)2004۵) (ا.) لول سفالین با 
سمنتی کوتاه که در زیر خاک یا میان دیوار 
کار گذارند تا از آن آب عبور کند. 
تنبوک: ۱۵090 [- تتبکک] (ا.) دامن زین و 
تسم رکاب» جناغ زین. 

ننمه: 2020000) [ع.] (مص‌ل.) سدار شدن» 
هوشیار شدن. (امص.) بیداری. بیدار مغزی» 
آگاهی؛ هوشیاری؛ ج. تسهات. 

=== طبل ===
MON_part2.txt:8546:طبله هوا می‌گیرد» برای منم آن فلفل در 
MON_part2.txt:8547:طبله گذارند تا آن را محفوظ دارد. فلفل در 
MON_part2.txt:36117:طبل. 
MON_part1.txt:13753:اصطبل: (اهای [ - اصطل» و۳ 
MON_part1.txt:37758:طبل؛ نقاره. خانه‌ای که در آن بلیدی‌ها
```


## [2026-09-14T03:15:19.653Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%85%D8%A8%D8%A7%DA%A9%D9%88",
 "prompt": "Urdu/Persian تمباکو: give etymology (from Portuguese tabaco?) and meaning; also mention Hindi तंबाकू if linked."
}
```


## [2026-09-14T03:15:20.883Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tabor",
 "prompt": "English tabor: give the etymology verbatim (Old French tabour, Persian tabir?), and any note on taboret/tabouret."
}
```


### [2026-09-14T03:15:23.850Z] TOOL RESULT

```
# Urdu Word: تمباکو (tambākū)

**Meaning:** This term refers to tobacco.

**Etymology:** The Wiktionary entry indicates the word was "Borrowed from Classical Persian _تَنْبَاکُو_ (tanbākū)." However, the page does not trace the etymology further back to Portuguese origins, so I cannot confirm that connection based on this source alone.

**Related Forms:** An alternative spelling exists: تَنْباکُو (tanbākū)

**Cross-linguistic Note:** The entry references a Hindi equivalent: तम्बाकू, which shares the same meaning and appears in the Hindi Wiktionary with similar etymological roots.
```


### [2026-09-14T03:15:27.613Z] TOOL RESULT

```
# Etymology of "Tabor"

**Verbatim Etymology Chain:**

According to the Wiktionary entry, English "tabor" comes "From Middle English, from Old French _tabour_, from Arabic _طُنْبُور_ (ṭunbūr), ultimately from the Middle Persian ancestor of Classical Persian _تنبور_ (tanbūr)."

The entry notes that tabor is "a doublet of _tambour_ and _tanbur_."

**Regarding Taboret/Tabouret:**

The provided content does not mention "taboret" or "tabouret." These related furniture terms (small stools or low tables) are not discussed in this Wiktionary article, which focuses on the musical instrument and military formation meanings of "tabor."
```


## [2026-09-14T03:15:40.272Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/tobacco\" \\\n \"https://www.etymonline.com/word/tobacco\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%A8%D8%A7%DA%A9%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%B7%D9%86%D8%A8%D9%88%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%A8%D9%88%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D9%86%D8%A8%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%D8%B7%D8%A8%D9%84\" \\\n \"https://www.etymonline.com/word/tabor\" \\\n \"https://en.wiktionary.org/wiki/tambour\" \\\n \"https://en.wiktionary.org/wiki/tabor\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D9%85%D8%A8%D8%A7%DA%A9%D9%88\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 494, roots Tabaco / Taburak: tobacco, tanbur, tonbak, tabl, tabor, tambour chains\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T03:15:44.438Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/392f07cabafde350.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/70cdf08743d38017.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/17ec2a3b69e96c0e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73273ac5fd80c16c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3a3d4acd00473873.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e7e25105a435c27.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/645537e76aabebb2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b2fa13620c0ce133.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/758286e49e62c3a3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd12daa9448aecbb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c92ac528f70519ff.txt
```


## [2026-09-14T03:15:49.358Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://www.ahdictionary.com/word/search.html?q=tobacco\" \\\n \"https://www.ahdictionary.com/word/search.html?q=tambour\" \\\n \"https://www.ahdictionary.com/word/search.html?q=tabor\" \\\n \"https://abadis.ir/fatofa/%D8%AA%D8%A8%DB%8C%D8%B1%D9%87/\" \\\n \"https://abadis.ir/fatofa/%D8%AA%D9%86%D8%A8%DA%A9/\" \\\n \"https://abadis.ir/fatofa/%D8%AA%D9%86%D8%A8%D8%A7%DA%A9%D9%88/\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 494: AHD tobacco/tambour/tabor etymologies; Mo'in & Dehkhoda tabire/tonbak/tanbaku\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T03:15:55.056Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3dfc5dc61a7ab7cb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fc2740960b505b87.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a4046628b10b8396.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f8ebdc6e5e99205d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/141fffa2a2d2586e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bdea7e7e9ecbba89.txt
```


## [2026-09-14T03:16:08.711Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 3dfc5dc61a7ab7cb fc2740960b505b87 a4046628b10b8396 f8ebdc6e5e99205d 141fffa2a2d2586e bdea7e7e9ecbba89 392f07cabafde350; do echo -n \"$f \"; wc -c < $f.txt; done\nmkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg494.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/494.png\nls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/494.png"
}
```


### [2026-09-14T03:16:09.728Z] TOOL RESULT

```
3dfc5dc61a7ab7cb 5252
fc2740960b505b87 5254
a4046628b10b8396 4411
f8ebdc6e5e99205d 6284
141fffa2a2d2586e 10200
bdea7e7e9ecbba89 11992
392f07cabafde350 27623
-rw-rw-r-- 1 sfmqrb sfmqrb 72008 Sep 13 23:16 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/494.png
```


## [2026-09-14T03:16:12.189Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-14T03:16:12.246Z] TOOL RESULT

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


## [2026-09-14T03:17:15.254Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA ===\"; grep -n -i \"ṭunbūr\\|tunbur\\|tanbur\\|طنبور\\|ṭabl\\|tabl \\|طبل\" incoming/PLA/PLA_pages.txt | head -12 | cut -c1-300\necho \"=== AFM ===\"; grep -n \"طنبور\\|الطبل\\|طبل\" AFM_pages.txt | head -8 | cut -c1-250\necho \"=== TAD ===\"; grep -n \"طنبور\\|طبل\" TAD_pages.txt | head -6 | cut -c1-250\necho \"=== ARB ===\"; grep -n \"طنبور\\|الطبل\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -6 | cut -c1-250"
}
```


### [2026-09-14T03:17:15.375Z] TOOL RESULT

```
=== PLA ===
287:Musikinstrumente:                     tanbur       "Tambur,        Streichinstrument",                 sanf   "Harfe"
11004:&>-              garb’ : "bitter" pers.zu tal s. tabl u. fahl >
11213:       tanbur             1°,        syr.       Premk        13,
=== AFM ===
192:والكردنة ٠‏ وام الاصطبل فهو تعريب الرومى 562111111153
2895:030 £ اليقة اليل . سني ب على التشبيه. ومئة طنبور 0
3449:3 ܐܕܝܨ حض ومعناه الاصطبل ‏ ܒܝܬܦܣܣܬ/ ܟ
=== TAD ===
=== ARB ===
ARB_mo3rb.txt:12276:)١(‏ « الرعن » الأنف المظيم من الطبل ناه متقدما ٠‏ و « القف » ما أرتفع من الأرض وغلظط 
ARB_mo3rb.txt:20611:"الكرس “بطم اللكاف أيضا ععتى الطبل » وقد نصوا على ذلك ٠‏ وقال أذّى شير : « معرب يه
```


## [2026-09-14T03:17:19.702Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"tanbūr\\|tanbur\\|ṭunbūr\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10 | cut -c1-400\necho \"--- tabl ---\"; grep -n \"tabl\\b\\|ṭabl\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10 | cut -c1-400"
}
```


### [2026-09-14T03:17:19.781Z] TOOL RESULT

```
882:Musikinstrumente: tanbur "Tambur, Streichinstrument", sanf "Harfe" 
14636:tanbur 1°, syr. Premk 13, 
--- tabl ---
924:pers. talh >ar. tabl, pers. zangir — ar. Zanzir 
6163:EN - tel: "bitter" = tabl, falb u. fahl. 
14373:&>- garb’ : "bitter" pers. zu tal s. tabl u. fahl >
```


## [2026-09-14T03:17:25.868Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"tunbur\\|tanbur\\|Laute\" AFA.txt | head -10 | cut -c1-500\necho \"=== PLA page with tanbur headword ===\"; grep -n \"طنبور\" incoming/PLA/PLA_pages.txt incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5 | cut -c1-300"
}
```


### [2026-09-14T03:17:25.948Z] TOOL RESULT

```
281:sein sonst incompatibler Laute *), Abweichungen von der
306:die Zischlaute und Dentale einen meist sicheren Anhalt,
407:bei den Zischlauten und Dentalen als auch bei den übri-
408:gen Lauten Abwoiclumgen von der üblichen Lautvertretung
416:Bei den übrigen Lauten n3DJ?lH=^=-^; B^3> = jüd. ar.
933:schen Lauten vor sich gehen kann, {jas^ kenne ich nur
1218:lauter ungen *^Arüclis zeigen (Levy Nhbr. Wtb. III. 338
1267:unten lautenden Riegel gilt.
1340:Doppelconsonanteii im Anlaute zu vermeiden, miüDS ge-
1341:worden. Die Formen mit anlautendem .1/ aber sind nach
=== PLA page with tanbur headword ===
```


## [2026-09-14T03:17:31.315Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'Musikinstrumente' in p and 'tanbur' in p:\n        print('leaf1',i+1,'printed',i+1-15)\n        idx=p.find('Musikinstrumente')\n        print(p[max(0,idx-500):idx+400])\nEOF"
}
```


### [2026-09-14T03:17:32.386Z] TOOL RESULT

```
leaf1 12 printed -3
   mineralogische            sowie   viele     andere
Bereiche           des       täglichen          Lebens     z.    B.:


Botanik:           amlüg       "Birne",          azädraht         "persischer           Flieder",       asfaräg     "Spargel"
Steuersystem:                 äbär,       aräßa, tasuf,            haräg
Mineralien:              arziz        "Zinn",      &han      "Eisen",           fuläd    "Stahl"
Zoologie:           fil "Elefant",                 bolbol        "Nachtigall".
Musikinstrumente:                     tanbur       "Tambur,        Streichinstrument",                 sanf   "Harfe"


Ortsnamen           sind       hauptsächlich              wegen     der      Vielfalt         ihrer    arabischen       Formen
aufgeführt              z.    B.:


isfähän,           isfahän,           isbahän
od.
istahr,        stahr,          istahr        und    istahr


Der
```


## [2026-09-14T03:17:36.615Z] AGENT

Now I'll write the verification file.


## [2026-09-14T03:27:12.294Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/draft-494.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nAHD = \"https://www.ahdictionary.com/word/search.html?q=\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Tabaco\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Taino (Arawakan, Greater Antilles) tabago / tabaco 'tube for inhaling smoke; roll of tobacco leaves'\",\n \"note\": \"Klein p.1623 s.v. tobacco is verbatim Nourai's root: 'Taino (Caribbean) tabaco, “pipe for smoking; roll of tobacco leaves”'. The language label the book prints, 'Caribian', is Nourai's spelling for Caribbean/Arawakan; the donor language is properly Taino (Arawakan), the language of Hispaniola, not Cariban proper. Modern dictionaries split on the exact sense: Oviedo (1535) reported it as the pipe, Las Casas (1552) as the roll of leaves, and Etymonline/Wiktionary prefer Las Casas; the current AHD adds that Spanish tabaco is 'partly from Old Spanish atabaca, altabaca' < Arabic al-ṭubbāq (Inula viscosa), which is exactly the claim Nourai's own NOTE on node #4 attributes to AHD:1350 — so that note is a faithful report of AHD and is still AHD's view.\",\n \"note_fa\": \"ریشهٔ این خانواده واژهٔ تاینویی (از زبان‌های آراواکی جزایر کارائیب) tabaco/tabago است به معنای «نای دودکش یا لولهٔ برگ توتون پیچیده». کلاین (ص‌۱۶۲۳) دقیقاً همین را می‌آورد؛ برچسب «Caribian» که نورایی به کار برده املای شخصی اوست و زبان وام‌دهنده درست‌تر «تاینو» است. فرهنگ AHD امروز هم می‌گوید بخشی از tabaco اسپانیایی به اسپانیایی کهن atabaca و از آن‌جا به عربی الطُبّاق بازمی‌گردد؛ پس یادداشت نورایی دربارهٔ AHD نقل درستی است. ادعای نورایی دربارهٔ ریشه درست است.\",\n \"sources\": [W+\"tobacco\", \"https://www.etymonline.com/word/tobacco\", AHD+\"tobacco\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1623\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 861 (0-based 860), s.v. tobacco: 'Sp., Port. tabaco, fr. Taino (Caribbean) tabaco, “pipe for smoking; roll of tobacco leaves”; the English form of the word was prob. influenced by Tobago, name of a West Indian island; cp. F. tabac, It. tobacco, G. Tabak, Du. tabak, Hind. tambaka, which all derive ult. fr. Taino tabaco. Cp. also tabatiere.' — every box of Nourai's chart except the Persian one comes from this single entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"SKT.txt line 19801, s.v. Tobacco\", \"stance\": \"supports\",\n    \"note\": \"'Tobacco. (Span.-Hayti.) Span. tabaco. A word taken from the language of Hayti (Clavigero, Hist. of Mexico).'\"},\n   {\"src\": \"HJB\", \"where\": \"HJB.txt line 22143 ff., s.v. TOBACCO\", \"stance\": \"supports\",\n    \"note\": \"'[The word tabaco is from the language of Hayti, and meant, first, the pipe, secondly, the plant, thirdly, the sleep which followed its use (Mr. J. Platt, 9 ser. N. & Q. viii. 322).]'\"},\n   {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. tobacco (current online ed.)\", \"stance\": \"partial\",\n    \"note\": \"'Spanish tabaco, probably partly from a Taíno word recorded by a Spanish chronicler as tabago, a tube for inhaling smoke… and partly from Old Spanish atabaca, altabaca… from Arabic al-ṭubbāq' — a double etymology, so the Caribbean root is only half the story for AHD.\"},\n   {\"src\": \"LKT\", \"where\": \"LKT.txt (Lokotsch) — no numbered entry for tabak/tabaco\", \"stance\": \"silent\",\n    \"note\": \"grep 'tabak|tabaco' finds only compounds (Rauchtabak, tabak 'Gerber' no. 1195, tk. tabak 'Sohle' no. 1962a); Lokotsch has no entry for tobacco because he covers only oriental loans.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\"id\": 1, \"lang\": \"Persian\", \"words\": \"tanbâkŭ «تنباکو ( تمباکو )»\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"NP تنباکو tanbākū 'tobacco' is a 17th-century colonial Wanderwort, but not a direct Persian borrowing from Taino as the arrow from the root box implies. Tobacco reached Safavid Iran c. 1600 by way of the Portuguese Estado da Índia (Hormuz/Goa) and Mughal India — Shah ʿAbbās I banned smoking in 1030/1621 — and the Persian form goes back to Portuguese tabaco through the Indian shape tambākū/tambākū: Wiktionary derives تنباکو straight from Portuguese tabaco. The Persian variant تمباکو that Nourai prints beside it is the Indian nasalised form, and the alternation ن/م before b is the regular Persian/Urdu writing of the labial nasal (Iranian pronunciation [tʰæm.bɑː.kʰuː]). So the etymon is right, the route is compressed: Taino → Spanish/Portuguese → India → Persia.\",\n  \"derivation_fa\": \"«تنباکو» وام‌واژه‌ای است از پرتغالی tabaco که خود از زبان تاینویی جزایر کارائیب گرفته شده است؛ اما راه ورود آن به فارسی مستقیم نبوده است: توتون در حدود ۱۰۰۹/۱۶۰۰ از راه پرتغالیان هرمز و هندوستان به ایران رسید و شاه عباس اول در ۱۰۳۰ ق کشیدن آن را قدغن کرد. صورت «تمباکو» همان شکل هندی واژه است و ابدال ن/م پیش از ب در فارسی و اردو قاعده‌مند است. ادعای نورایی در اصل درست است ولی مسیر وام‌گیری را فشرده کرده است.\",\n  \"sources\": [W+\"%D8%AA%D9%86%D8%A8%D8%A7%DA%A9%D9%88\", \"https://abadis.ir/fatofa/%D8%AA%D9%86%D8%A8%D8%A7%DA%A9%D9%88/\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:1147\", \"status\": \"partial\",\n     \"note\": \"Mo'in's entry exists and matches the gloss — via abadis.ir (فرهنگ معین): 'تنباکو (تَ) (اِ.) گیاهی است یک ساله، بومی قارهٔ امریکا که به وسیلهٔ اسپانیایی‌ها به اروپا برده شده' — but Mo'in gives no donor-language tag there, and the page number of the 6-vol Amir Kabir edition cannot be checked (only the 2-vol Adena abridgement is scanned).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. تنباکو\", \"stance\": \"supports\",\n     \"note\": \"'گیاهی است یک ساله، بومی قارهٔ امریکا که به وسیلهٔ اسپانیایی‌ها به اروپا برده شده' — American origin confirmed.\"},\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 19993, 59879 (2-vol Adena OCR)\", \"stance\": \"partial\",\n     \"note\": \"the word appears only inside other entries ('بالای سر قلیان نهند تا تنباکو و آتش را…'; 'دخانیه… اقسام توتون و تنباکو'); the headword itself was lost in this OCR.\"},\n    {\"src\": \"Dehkhoda (via abadis)\", \"where\": \"abadis.ir لغت‌نامهٔ دهخدا s.v. تنباکو\", \"stance\": \"supports\",\n     \"note\": \"Dehkhoda states tobacco came to India from Europe in Akbar Shah's time and that the Spanish brought it to Europe from the island of Tabago — i.e. the Persian word arrived with the plant, from the West, not from a Caribbean language directly.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 861 s.v. tobacco\", \"stance\": \"silent\",\n     \"note\": \"Klein lists Hind. tambaka but no Persian form; the Persian box is the one box in this chart that Klein does not cover.\"}\n  ]},\n\n {\"id\": 2, \"lang\": \"Hindustani\", \"words\": \"tambâka\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Hindustani (Urdu/Hindi) تمباکو / तम्बाकू tambākū 'tobacco' is Klein's own example: he lists 'Hind. tambaka' among the forms that 'all derive ult. fr. Taino tabaco', so Nourai's arrow reproduces Klein exactly. The immediate donor, however, was Portuguese tabaco, brought to Goa and the Deccan in the late 16th century (tobacco is first recorded in India under Akbar, c. 1604–05); the intrusive -m- before b is an Indic nasalisation of the Portuguese open syllable. Wiktionary goes one step further and makes Urdu تمباکو a borrowing from Classical Persian تنباکو, which would reverse Nourai's implicit Persian/Indian parallelism; either way the ultimate source box is right.\",\n  \"derivation_fa\": \"صورت هندی‌واردوی «تمباکو» همان واژهٔ تاینویی است که از راه پرتغالیان گوا در اواخر سدهٔ دهم/شانزدهم به هند رسیده است؛ کلاین نیز همین را می‌آورد. «م» میانی زادهٔ خیشومی‌شدن هجای باز در زبان‌های هندی است. ویکی‌واژه اردوی تمباکو را وام‌گرفته از فارسی تنباکو می‌داند، که اگر درست باشد جهت پیکان نورایی تغییر می‌کند. در مجموع ادعا با احتیاط پذیرفتنی است.\",\n  \"sources\": [W+\"%D8%AA%D9%85%D8%A8%D8%A7%DA%A9%D9%88\", W+\"tobacco\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1623\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 861 s.v. tobacco: '…cp. F. tabac, It. tobacco, G. Tabak, Du. tabak, Hind. tambaka, which all derive ult. fr. Taino tabaco.' The transliteration 'tambaka' in the chart is Klein's own.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HJB\", \"where\": \"HJB.txt line 22143 ff. s.v. TOBACCO\", \"stance\": \"partial\",\n     \"note\": \"Hobson-Jobson declines an 'elaborate article' and gives only quotations on 'the introduction of tobacco into India and the East'; it confirms the plant and word came to India from the Spanish/Portuguese world, not the reverse.\"},\n    {\"src\": \"AID\", \"where\": \"AID.txt — no headword\", \"stance\": \"silent\",\n     \"note\": \"Whitworth's Anglo-Indian Dictionary has no 'tambaku'/'tobacco' entry; the word occurs only inside Bhaduri, Chilam, Hookah (lines 1030, 1626, 2867).\"},\n    {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. تمباکو (Urdu)\", \"stance\": \"partial\",\n     \"note\": \"'Borrowed from Classical Persian تَنْبَاکُو (tanbākū)' — makes the Indian form secondary to the Persian one.\"}\n  ]},\n\n {\"id\": 3, \"lang\": \"Portuguese\", \"words\": \"tabaco\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Port. tabaco 'tobacco' is one of the two Iberian forms Klein cites side by side ('Sp., Port. tabaco'); it was taken over from the Antillean Taino word in the first half of the 16th century by the same Iberian colonists who reported it (Oviedo 1535, Las Casas 1552) and carried it to Africa, India and Iran. The word is unchanged in shape: Taino tabaco → Port. tabaco, a straight substitution loan with no sound change at all.\",\n  \"derivation_fa\": \"پرتغالی tabaco عیناً همان واژهٔ تاینویی است که در نیمهٔ نخست سدهٔ شانزدهم میلادی به زبان‌های شبه‌جزیرهٔ ایبری راه یافت و هیچ دگرگونی آوایی نیافت. کلاین شکل اسپانیایی و پرتغالی را هم‌عرض می‌آورد. ادعای نورایی درست است.\",\n  \"sources\": [W+\"tobacco\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1623\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 861: 'tobacco, n. — Sp., Port. tabaco, fr. Taino (Caribbean) tabaco…' — Portuguese is named explicitly.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"SKT.txt line 19801\", \"stance\": \"partial\",\n     \"note\": \"Skeat names only 'Span. tabaco'; the Portuguese form is not mentioned, but nothing contradicts it.\"},\n    {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. tobacco\", \"stance\": \"partial\",\n     \"note\": \"AHD routes English through 'Spanish tabaco' only; Portuguese is not part of its chain.\"}\n  ]},\n\n {\"id\": 4, \"lang\": \"Spanish\", \"words\": \"tabaco\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Spanish tabaco itself is not in doubt — it is the form in which the Taino word entered European languages — but the arrow Portuguese → Spanish reverses the accepted priority: the earliest records are Spanish (Oviedo, Historia general 1535; Las Casas 1552), the borrowing took place in the Spanish Antilles, and Klein, Etymonline, AHD and Wiktionary all make Spanish the source (Klein prints 'Sp., Port. tabaco' side by side, not Port. > Sp.). Nourai's own NOTE on this box — that AHD:1350 derives the Spanish word from Arabic ṭabāq, 'a euphoria-causing herb' — is a fair report and still AHD's position: the current edition says tabaco is 'partly from Old Spanish atabaca, altabaca, a Mediterranean plant (Inula viscosa)… from Arabic al-ṭubbāq… from Syriac dubāqā, birdlime'. So Spanish is a blend: a Taino smoking-tube word reinforced by an existing Andalusi-Arabic herb name.\",\n  \"derivation_fa\": \"خود اسپانیایی tabaco مسلّم است، امّا پیکان «پرتغالی ← اسپانیایی» تقدّم تاریخی را وارونه کرده است: کهن‌ترین شواهد (اووییدو ۱۵۳۵ و لاس‌کازاس ۱۵۵۲) اسپانیایی است و کلاین، اتیمانلاین و AHD همه اسپانیایی را سرچشمه می‌دانند. یادداشت خود نورایی دربارهٔ ریشهٔ عربی الطُبّاق نقل درستی از AHD است و همچنان در ویرایش تازه می‌ماند: واژهٔ اسپانیایی آمیزه‌ای است از واژهٔ تاینویی و نام گیاهی عربی‌اندلسی.\",\n  \"sources\": [AHD+\"tobacco\", \"https://www.etymonline.com/word/tobacco\", W+\"tobacco\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1623\", \"status\": \"partial\",\n     \"note\": \"Klein writes 'Sp., Port. tabaco' — the two are coordinated, not chained; he gives no Portuguese → Spanish direction. Klein therefore supports the word but not this arrow.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. tobacco\", \"stance\": \"supports\",\n     \"note\": \"confirms Nourai's NOTE: '…partly from Old Spanish atabaca, altabaca… (from Arabic al-ṭubbāq: al-, the + ṭubbāq, ṭabbāq, the plant I. viscosa, from Syriac dubāqā, birdlime…)'.\"},\n    {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/tobacco\", \"stance\": \"contradicts\",\n     \"note\": \"'from Spanish tabaco, in part from an Arawakan language of the Caribbean' — Spanish, not Portuguese, is the transmitting language; 'The entry contains no mention of Arabic tabbaq.'\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt line 19801\", \"stance\": \"contradicts\",\n     \"note\": \"'Tobacco. (Span.-Hayti.) Span. tabaco' — Skeat's language tag puts Spanish alone between English and Hayti.\"}\n  ]},\n\n {\"id\": 5, \"lang\": \"English\", \"words\": \"tobacco\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English tobacco, first attested 1580s (Klein/Etymonline; Camden 1586 on Ralph Lane bringing 'Indicam illam plantam quam Tabaccam vocant' to England), is the Spanish word taken over whole. The shift of the first vowel from ta- to to- is 18th-century and, on Klein's and Etymonline's account, was helped by the island name Tobago — which Columbus is said to have named in 1498 from a Haitian word for the pipe. Nourai's arrow Spanish → English is exactly Klein's.\",\n  \"derivation_fa\": \"انگلیسی tobacco (نخستین شواهد ۱۵۸۰م) همان واژهٔ اسپانیایی است که بی‌دگرگونی وام گرفته شده؛ تبدیل ta- به to- در سدهٔ هجدهم رخ داده و به باور کلاین و اتیمانلاین زیر تأثیر نام جزیرهٔ Tobago بوده است (ریشه‌شناسی عامیانه). ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/tobacco\", AHD+\"tobacco\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1623\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 861: 'the English form of the word was prob. influenced by Tobago, name of a West Indian island'.\"},\n    {\"ref\": \"AHD:1350\", \"status\": \"supports\",\n     \"note\": \"the 1975 AHD page is not open online, but the current AHD entry for tobacco is the same text Nourai paraphrases ('Spanish tabaco… partly from Arabic al-ṭubbāq'), so the citation is sound in substance.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"SKT.txt line 19801\", \"stance\": \"supports\",\n     \"note\": \"'Tobacco. (Span.-Hayti.)'\"},\n    {\"src\": \"HJB\", \"where\": \"HJB.txt s.v. TOBACCO, quotation from Camden's Annales (1586)\", \"stance\": \"supports\",\n     \"note\": \"'…reduces Indicam illam plantam quam Tabaccam vocant et Nicotiam… in Angliam primi… intulerunt' — dates the English adoption.\"}\n  ]},\n\n {\"id\": 6, \"lang\": \"French\", \"words\": \"tabac; tabaquiere\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"F. tabac 'tobacco' is the Spanish word taken into French about 1600 (earlier herbe à Nicot, from Jean Nicot, who sent seeds from Lisbon to Catherine de' Medici in 1560); Klein cites 'F. tabac' among the direct reflexes of Taino tabaco. The snuffbox word in the chart, tabaquière, is not a blunder: Klein s.v. tabatiere states that modern F. tabatière comes 'fr. earlier tabaquière, fr. tabac' — a regular -ière agent/container suffix on tabac, with later dissimilation of the velar (tabaquière > tabatière).\",\n  \"derivation_fa\": \"فرانسوی tabac حدود سال ۱۶۰۰ از اسپانیایی وام گرفته شد. صورت tabaquière که نورایی می‌آورد خطا نیست؛ کلاین می‌گوید tabatière امروزی از صورت کهن‌تر tabaquière (با پسوند -ière بر tabac) آمده و پس از آن کاف میانی به ت بدل شده است. ادعای نورایی درست است.\",\n  \"sources\": [W+\"tobacco\", \"https://www.etymonline.com/word/tobacco\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1623\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 861 s.v. tobacco: '…cp. F. tabac… Cp. also tabatiere.'; and leaf 829 s.v. tabatiere: 'F., fr. earlier tabaquière, fr. tabac, “tobacco”'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/tobacco\", \"stance\": \"supports\",\n     \"note\": \"'Cultivation began in France around 1556 with imported seeds' — fixes the date of the French adoption.\"},\n    {\"src\": \"PHN\", \"where\": \"PHN.txt — no TABAC headword\", \"stance\": \"silent\",\n     \"note\": \"Pihan's dictionary of French words from Arabic/Persian/Turkish has no article on tabac (only 'tabac' in passing at line 3530, s.v. Hachighe); he did not consider it an oriental loan.\"}\n  ]},\n\n {\"id\": 7, \"lang\": \"English\", \"words\": \"tabatiere\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English tabatiere (also spelt tabatière) 'snuffbox' is a straight 19th-century borrowing of French tabatière, itself from earlier tabaquière 'tobacco-container', from tabac. Klein carries it as an English headword — which is why Nourai's box is English — and gives exactly this chain; the sense 'snuffbox' follows the 18th-century vogue for snuff (tabac à priser). Nourai's page reference KLN:1563 lands in the right place: Klein's tabatiere entry stands on the leaf whose running head numbers are 1564/1565 (leaf 829 of KLN_1966.txt).\",\n  \"derivation_fa\": \"انگلیسی tabatiere «جعبهٔ انفیه» وام‌واژه‌ای است از فرانسوی tabatière که خود از tabaquière و در نهایت از tabac ساخته شده است؛ تحول معنایی «ظرف توتون» ← «قوطی انفیه» به رواج انفیه در سدهٔ هجدهم بازمی‌گردد. ارجاع KLN:1563 نیز درست است. ادعای نورایی درست است.\",\n  \"sources\": [W+\"tobacco\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1563\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 829 (running heads 1564/1565), s.v. tabatiere: 'tabatiere, n., a snuffbox. — F., fr. earlier tabaquière, fr. tabac, “tobacco”. See tobacco.' The page number is right within a page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 861 s.v. tobacco\", \"stance\": \"supports\",\n     \"note\": \"the tobacco entry itself ends 'Cp. also tabatiere', closing the loop between the two boxes.\"},\n    {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt — not separately checked for this minor headword\", \"stance\": \"silent\",\n     \"note\": \"Funk & Wagnalls was not consulted for tabatiere; Klein's entry is unambiguous and no source disputes it.\"}\n  ]}\n]\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Tabŭrâk\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"New Persian تبیر / تبیره tabīr, tabīra 'drum' (dimin. تبوراک tabūrāk); Middle Persian drum word attested is tumbag\",\n \"note\": \"The Iranian drum word is real and old: NP تبیر/تبیره is in Rūdakī and Ferdowsī, Mo'in glosses تبیره 'دهل، کوس، طبل، نقاره' and has a separate entry تبوراک 'طبلی کوچک', and the current AHD reconstructs 'Persian tabīr, tabīra, drum; probably akin to Middle Persian tumbag, and of imitative origin.' What is NOT attested is the headword as Nourai sets it up: MacKenzie's Concise Pahlavi Dictionary knows only tumbag 'drum' (and its index 'drum tumbag'), Nyberg only tumbak; no Pahlavi *tabūrāk is recorded anywhere. Devic, whom Nourai cites for the branch, actually calls تبوراک a late diminutive of tabūr with an intrusive alef ('lequel est, suivant toute vraisemblance, un diminutif de tabour, dans lequel s'est glissé fautivement un ا â'). So the root box should read New Persian tabīr/tabīra, not Pahlavi tabūrāk; the -āk is the New Persian diminutive suffix. A second, larger problem runs through the whole chart: Nourai fuses two different Iranian words — the drum word tabīr/ṭabl and the long-necked lute word tanbūr (MP tambūr) — into one tree.\",\n \"note_fa\": \"واژهٔ ایرانی «تبیر/تبیره» به معنای دهل کهن و اصیل است و در شعر رودکی و فردوسی دیده می‌شود؛ معین نیز تبیره را «دهل، کوس، طبل، نقاره» و تبوراک را «طبلی کوچک» معنی کرده است. امّا صورت «تبوراک» در فارسی میانه (پهلوی) هیچ شاهدی ندارد: مکنزی و نیبرگ تنها tumbag/tumbak «دهل» را ضبط کرده‌اند، و پسوند -اک در تبوراک پسوند تصغیر فارسی نو است (دویک نیز آن را مصغّر tabūr می‌داند که الفی نابجا در آن راه یافته). افزون بر این، نورایی دو واژهٔ جدا را — «تبیر/طبل» (کوبه‌ای) و «تنبور» (زهی) — در یک درخت درهم آمیخته است. بنابراین ریشه با احتیاط پذیرفتنی است.\",\n \"sources\": [AHD+\"tambour\", W+\"%D8%AA%D9%86%D8%A8%DA%A9\", \"https://abadis.ir/fatofa/%D8%AA%D8%A8%DB%8C%D8%B1%D9%87/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1025\", \"status\": \"partial\",\n    \"note\": \"Mo'in does have both words — MON_part1.txt line 37743 'تبوراک… طبلی کوچک که زارعان به جهت رمانیدن جانوران از کشتزار نوازند' and line 37757 'تبیره [= تبیر] دهل، کوس، طبل، نقاره' (the Latin-script form beside تبیره is illegible in this OCR) — but both are New Persian entries; Mo'in nowhere labels tabūrāk Pahlavi, and the page number of the 6-vol edition cannot be checked because only the 2-vol Adena abridgement is scanned.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"PHD.txt line 597 and English index line 1701\", \"stance\": \"contradicts\",\n    \"note\": \"MacKenzie's only Pahlavi drum is 'tumbag [twmbk' | N ~a] drum'; the index reads 'drum tumbag.' There is no tabūrāk, tabīr or ṭabl in the Concise Pahlavi Dictionary.\"},\n   {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 3804\", \"stance\": \"contradicts\",\n    \"note\": \"'tumbak [twmbk'] drum, or kettle-drum 209. — Arm. lw. tmbuk < *tumbuk “drum”; NP tanbak, tanbuk, tanbik (BQ also tun-) “bagpipe”, “drum”.' Nyberg's Pahlavi drum word is tumbak, not tabūrāk.\"},\n   {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt leaf 696 (ت section), s.vv. تبیره / تبیر\", \"stance\": \"supports\",\n    \"note\": \"'تبیره بر وزن نفس، دهل و کوس و نقاره و طبل را گویند'; 'تبیر… بمعنی تبیره است که دهل و کوس و طبل و نقاره باشد' — Borhān-e Qāṭeʿ confirms the New Persian word and its synonyms.\"},\n   {\"src\": \"FRS\", \"where\": \"FRS_pages.txt lines 6868, 22361-22362 (Asadī Ṭūsī, Loghat-e Fors)\", \"stance\": \"supports\",\n    \"note\": \"'تبیر طبل باشد، تبیره نیز گویند' — the word is already lexicalised in the oldest Persian dictionary (11th c.).\"},\n   {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. tambour\", \"stance\": \"partial\",\n    \"note\": \"'…or perhaps ultimately from alteration… of Persian tabīr, tabīra, drum; probably akin to Middle Persian tumbag, and of imitative origin.' The Persian drum word is recognised, but the Middle Persian congener is tumbag, not *tabūrāk.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"] = [\n {\"id\": 1, \"lang\": \"Persian\", \"words\": \"tabŭrâk «تبوراک ( تبیر ، تبیره )»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All three New Persian forms are well attested. تبیر tabīr / تبیره tabīra is the classical word for a large two-headed drum (Rūdakī's verse quoted in the box, 'پس تبیری دید نزدیک درخت…'; also Ferdowsī, Niẓāmī, Asadī Ṭūsī), and تبوراک tabūrāk is its diminutive in -āk, glossed by Mo'in as a small drum farmers beat to scare animals off the fields. The -āk suffix is the ordinary New Persian diminutive (cf. مغاک, سوراخ‌); Devic says as much, adding that the intrusive alef of tabūrāk is a scribal accretion on tabūr. The word is onomatopoeic in origin, akin to MP tumbag (MacKenzie), so 'from the root box' is trivially true — the node is the root, restated in New Persian.\",\n  \"derivation_fa\": \"هر سه صورت در فارسی نو شاهد دارند: «تبیر/تبیره» دهل بزرگ دوسر است (بیت رودکی در همین جعبه، و شواهد فردوسی و اسدی طوسی) و «تبوراک» مصغّر آن با پسوند تصغیر «ـاک» است که معین آن را طبل کوچک کشاورزان برای رماندن جانوران معنی کرده است. این واژه آواواژه (مقلّد صدا) است و با tumbag پهلوی هم‌ریشه است. ادعای نورایی در این گره درست است.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%D8%AA%D8%A8%DB%8C%D8%B1%D9%87/\", AHD+\"tambour\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:1025\", \"status\": \"supports\",\n     \"note\": \"MON_part1.txt line 37743 'تبوراک… طبلی کوچک که زارعان به جهت رمانیدن جانوران از کشتزار نوازند. دف، دایره'; line 37757 'تبیره [= تبیر] دهل، کوس، طبل، نقاره'. Both of Nourai's Persian glosses are Mo'in's own; only the page number is uncheckable.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt leaf 696, s.vv. تبیره / تبیر\", \"stance\": \"supports\",\n     \"note\": \"'تبیره… دهل و کوس و نقاره و طبل را گویند'; the same leaf also has 'تبیره دهلی است که میان آن باریک و هر دو سرش پهن می‌باشد' — the two-headed drum of Mo'in's gloss.\"},\n    {\"src\": \"FSF\", \"where\": \"FSF_pages.txt lines 2628, 18366 (Noushin, Vazhe-namak)\", \"stance\": \"supports\",\n     \"note\": \"Shahnameh lines cited under تبیره: 'همی از تبیره شود گوش کر' — the drum sense in Ferdowsī.\"},\n    {\"src\": \"DEV\", \"where\": \"DEV.txt leaf 250-251, printed p. 215-216, s.v. Tambour\", \"stance\": \"partial\",\n     \"note\": \"'Le persan a la voyelle ou dans تبوراک taboûrâk, tambourin, lequel est, suivant toute vraisemblance, un diminutif de تبور tabour, dans lequel s'est glissé fautivement un ا â.' — confirms the word but makes it secondary, not the ancestor.\"},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt — grep 'tabīr|tabira|Trommel' finds nothing\", \"stance\": \"silent\",\n     \"note\": \"Horn's Grundriss has no article on the drum word.\"}\n  ]},\n\n {\"id\": 2, \"lang\": \"Arabic\", \"words\": \"tanbŭr\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Arabic طُنْبُور ṭunbūr is indeed an Iranian loan — Asbaghi lists tanbur among the Persian Musikinstrumente borrowed into Arabic, and Wiktionary derives the Arabic word 'from the Middle Persian ancestor of Classical Persian تنبور' — but not from this parent. ṭunbūr denotes a long-necked plucked LUTE, and its Persian ancestor is MP tambūr (Manichaean and Book Pahlavi), itself possibly a metathesis of Greek πανδοῦρα pandoûra 'three-stringed lute'. That is a different etymon from the drum word tabīr/tabūrāk of node #1: a percussion word and a chordophone word, with no shared derivation. Devic and Lammens saw this clearly — Lammens: 'il me semble difficile de dériver ce mot de l'arabe طنبور tonboûr, qui dans la langue classique ou parlée n'a jamais désigné qu'une lyre, guitare ou mandoline'. Nourai's own gloss ('a drum, ALSO a kind of stringed musical instrument') papers over the conflation.\",\n  \"derivation_fa\": \"عربی طُنْبُور بی‌گمان وام‌واژه‌ای ایرانی است (اصبغی آن را در فهرست وام‌واژه‌های فارسی می‌آورد)، امّا نه از «تبوراک» کوبه‌ای، بلکه از فارسی میانهٔ tambūr «ساز زهی دسته‌بلند» که خود شاید با قلب (متاتزِ) از یونانی pandoûra آمده باشد. لامنس صریحاً می‌گوید طنبور در عربی هرگز جز ساز زهی معنایی نداشته است. پس نورایی دو واژهٔ جداگانه را یکی گرفته و پژوهش امروزی این پیکان را رد می‌کند.\",\n  \"sources\": [W+\"%D8%B7%D9%86%D8%A8%D9%88%D8%B1\", W+\"%D8%AA%D9%86%D8%A8%D9%88%D8%B1\", AHD+\"tambour\"],\n  \"ref_check\": [\n    {\"ref\": \"DEV:215\", \"status\": \"partial\",\n     \"note\": \"DEV.txt leaf 250-251 = printed pp. 215-216 (the running head 'DES MOTS D'ORIGINE ORIENTALE. 215' stands just above the Tambour article, so Nourai's page is right). Devic writes: 'Les formes tambour, تنبور tonbour, sont certainement des altérations de tabour, تبیر tabir.' He thus makes tanbūr secondary to tabīr — Nourai's direction — but this is Devic's 1876 view, not the modern one.\"},\n    {\"ref\": \"AHD:1313\", \"status\": \"partial\",\n     \"note\": \"the 1975 page is not online; the current AHD s.v. tambour lists 'Arabic ṭunbūr, ṭanbūr, tambura' only as an INFLUENCE on a form derived from Arabic ṭabl or Persian tabīr — it does not derive ṭunbūr from the drum word.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PLA\", \"where\": \"PLA_pages.txt leaf 12 (Asbaghi, Einleitung, list of semantic fields)\", \"stance\": \"supports\",\n     \"note\": \"'Musikinstrumente: tanbur “Tambur, Streichinstrument”, sanf “Harfe”' — Asbaghi counts tanbur among the Persian loanwords in Arabic (index entry 'tanbur 1°, syr. Fränkel 13').\"},\n    {\"src\": \"LAM\", \"where\": \"LAM.txt line 6970 ff., printed p. 233, s.v. Tambour\", \"stance\": \"contradicts\",\n     \"note\": \"'Il me semble difficile de dériver ce mot de l'arabe طنبور tonboûr, qui dans la langue classique ou parlée n'a jamais désigné qu'une lyre, guitare, ou mandoline… La dérivation du persan تبیر tabīr me paraît également forcée.'\"},\n    {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. طنبور (Arabic) and تنبور (Persian)\", \"stance\": \"contradicts\",\n     \"note\": \"Arabic ṭunbūr 'from the Middle Persian ancestor of Classical Persian تنبور'; Persian تنبور 'from Middle Persian tambūr… possibly (with metathesis of consonants) from Ancient Greek πανδοῦρα'. No drum etymon anywhere.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 832 s.v. tambour\", \"stance\": \"partial\",\n     \"note\": \"'F., fr. OF., fr. Arab. tabul, pl. of tabl, “drum”; influenced in form by VArab. tanbur (= Classical Arab. tunbur), “lute”.' Klein keeps ṭunbūr 'lute' strictly apart from ṭabl 'drum'.\"}\n  ]},\n\n {\"id\": 3, \"lang\": \"Persian\", \"words\": \"tanbŭr «تنبور ( طنبور )»; tonbak «تنبک ( طنبک ، دُنبک )»\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Two words, both mis-routed. (a) تنبور tanbūr is not a re-borrowing from Arabic: it is the inherited Persian word, MP tambūr > NP tanbūr, and it is Arabic that took it, not the reverse. What IS a round trip is only the SPELLING طنبور with ط — Mo'in's own entry says so: 'تنبور [= دنبره = طنبور، معرّ.]', i.e. طنبور is the muʿarrab (Arabicised) orthography re-imported into Persian, exactly as with طبل below. (b) تنبک/دنبک tonbak has nothing to do with ṭunbūr at all: it continues MP tumbag/tumbak 'drum' (MacKenzie, Nyberg), an imitative word whose Armenian loan թմբուկ tʼmbuk < *tumbuk proves its Middle Iranian age; Nyberg expressly lists 'NP tanbak, tanbuk, tanbik' as its descendants. The chart's arrow would make an inherited Pahlavi word come back from Arabic in the Islamic period, which the Armenian evidence rules out.\",\n  \"derivation_fa\": \"در این گره دو واژه هست و هر دو مسیرشان نادرست است. الف) «تنبور» وام‌گرفته از عربی نیست؛ میراثی است از فارسی میانه tambūr و عرب آن را از فارسی گرفته؛ آنچهٔ بازگشته فقط املای معرّب «طنبور» است و خود معین می‌نویسد: «تنبور [= دنبره = طنبور، معرّ.]». ب) «تنبک/دنبک» هیچ پیوندی با طنبور ندارد و دنبالهٔ فارسی میانهٔ tumbag/tumbak «دهل» است (مکنزی، نیبرگ)؛ وام‌واژهٔ ارمنی tʼmbuk قدمت ایرانی میانهٔ آن را ثابت می‌کند. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n  \"sources\": [W+\"%D8%AA%D9%86%D8%A8%DA%A9\", W+\"%D8%AA%D9%86%D8%A8%D9%88%D8%B1\", \"https://abadis.ir/fatofa/%D8%AA%D9%86%D8%A8%DA%A9/\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:1147\", \"status\": \"contradicts\",\n     \"note\": \"MON_part1.txt line 43946 s.v. تنبور: 'تنبور. ۲ [= دنبره = طنبور، معرّ.] (ا.) یکی از آلت‌های موسیقی ذوی‌الاوتار که دسته‌ای دراز و کاسه‌ای کوچک مانند سه‌تار دارد.' Mo'in marks طنبور as the muʿarrab of Persian تنبور — i.e. Persian → Arabic, the opposite of the chart's arrow; and for تنبک (abadis, فرهنگ معین) he gives no Arabic tag at all: 'یکی از سازها که به آن ضرب هم گویند…'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 3804 s.v. tumbak\", \"stance\": \"contradicts\",\n     \"note\": \"'tumbak [twmbk'] drum, or kettle-drum 209. — Arm. lw. tmbuk < *tumbuk “drum”; NP tanbak, tanbuk, tanbik (BQ also tun-) “bagpipe”, “drum”.' — NP tonbak descends from Pahlavi, not from Arabic.\"},\n    {\"src\": \"PHD\", \"where\": \"PHD.txt line 597\", \"stance\": \"contradicts\",\n     \"note\": \"'tumbag [twmbk' | N ~a] drum' — MacKenzie derives the New Persian form (N ~a = tumba/tonbak) straight from the Pahlavi word.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. تنبک (Persian)\", \"stance\": \"contradicts\",\n     \"note\": \"'From Middle Persian tumbag, meaning drum, of imitative origin', cognate with Old Armenian թմբուկ; alternative forms تمبک, دنبک, دمبک.\"},\n    {\"src\": \"PLA\", \"where\": \"PLA_pages.txt leaf 12\", \"stance\": \"partial\",\n     \"note\": \"Asbaghi's list of Persian loans in Arabic includes tanbur, which supports the Persian→Arabic direction for that word (the reverse of this node's arrow).\"}\n  ]},\n\n {\"id\": 4, \"lang\": \"Arabic\", \"words\": \"tabŭl; tabbâl\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The words are real but the parentage is wrong twice over. طُبُول ṭubūl is not an independent word: it is the broken plural of طَبْل ṭabl 'drum' (Klein: 'Arab. tabul, pl. of tabl'), and طَبّال ṭabbāl 'drummer' is the faʿʿāl occupational noun of the same root ط-ب-ل. And ṭabl does not come from ṭunbūr: Wiktionary derives it from 'Middle Iranian *tabir, tabil', Devic says flatly 'Tabl est d'origine persane', and Lokotsch (no. 1971) compares Hesychius' ταβάλα 'kettledrum' used by the Parthians. In other words ṭabl is the Arabic reflex of the very word in node #1 (tabīr/tabīl), so this box should hang from #1, not from the lute word #2; and the Arabicised singular, not a plural, is what the Persian box #5 continues.\",\n  \"derivation_fa\": \"هر دو واژه درست‌اند ولی جایشان در درخت نادرست است: «طُبُول» جمع مکسّر «طَبْل» است و «طبّال» صفت شغلی بر وزن فعّال از همان ریشهٔ ط-ب-ل. افزون بر آن، طبل از طنبور نیامده؛ ویکی‌واژه آن را از ایرانی میانهٔ *tabir/tabil می‌داند، دویک می‌گوید «طبل اصل فارسی دارد» و لوکوچ آن را با ταβάλαی هزیخیوس که طبل اشکانیان است می‌سنجد. پس این جعبه باید زیر گرهٔ ۱ (تبیر) می‌آمد نه زیر طنبور.\",\n  \"sources\": [W+\"%D8%B7%D8%A8%D9%84\"],\n  \"ref_check\": [\n    {\"ref\": \"DEV:215\", \"status\": \"partial\",\n     \"note\": \"Devic's Tambour article (printed pp. 215-216) and his Timbale article (p. 220) give the ṭabl material: 'De l'arabe طبل tabl, avec l'article at-tabl, sorte de tambour… Tabl est d'origine persane. On trouve un pluriel grec ταβάλα… dont les Parthes se servaient à la guerre.' He supports the Iranian origin of ṭabl but never derives it from ṭunbūr.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 829 s.v. tabor and leaf 832 s.v. tambour\", \"stance\": \"contradicts\",\n     \"note\": \"'fr. Arab. tabul, pl. of tabl, “drum”' — ṭubūl is a plural of ṭabl, an independent root, not a derivative of ṭunbūr.\"},\n    {\"src\": \"LKT\", \"where\": \"LKT.txt no. 1971 (Ar. tabl)\", \"stance\": \"partial\",\n     \"note\": \"'1971. Ar. tabl: ‚Pauke‘ [vgl. bei Hesychius ταβάλα ‚Pauke‘ bei den Parthern]; hieraus mit ar. Art. it. ataballo, sp. atabal… frz. timbale.' Lokotsch treats ṭabl as an Arabic headword with a Parthian comparison, not as a derivative of ṭunbūr.\"},\n    {\"src\": \"LAM\", \"where\": \"LAM.txt p. 234, s.v. Tambour/Timbale\", \"stance\": \"partial\",\n     \"note\": \"'je préfère l'arabe طبل tabl, tambour, au pluriel طبول touboûl, avec lequel tabour, tabourin… ont bien de la ressemblance' — confirms ṭubūl = plural of ṭabl.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. طبل (Arabic)\", \"stance\": \"partial\",\n     \"note\": \"'The word derives from Middle Iranian *tabir, tabil' — Iranian origin yes, but from the drum word, not the lute word.\"}\n  ]},\n\n {\"id\": 5, \"lang\": \"Persian\", \"words\": \"tabl «طبل ( طبّال )»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"NP طبل ṭabl 'drum' (with طبّال 'ṭabbāl, drummer') is an Arabic loan in Persian, and Nourai is right to draw it as a return arrow: the Arabic طبل itself goes back to a Middle Iranian *tabir/tabil, so طبل is a Persian→Arabic→Persian round trip (a muʿarrab re-import), which is exactly why it is written with ط and ب instead of a native Persian spelling, and why classical Persian keeps the older native تبیره beside it (Ferdowsī uses both). The agent noun طبّال is pure Arabic morphology (faʿʿāl) taken over whole.\",\n  \"derivation_fa\": \"«طبل» و «طبّال» در فارسی وام‌واژهٔ عربی‌اند — املای ط نشانهٔ همین است — ولی خود طبل عربی از ایرانی میانهٔ *tabir/tabil گرفته شده؛ پس این واژه سفری دوره‌ای (فارسی ← عربی ← فارسی) دارد و معرّب بازگشته است. صورت بومی «تبیره» تا روزگار فردوسی در کنار آن زنده ماند. ادعای نورایی درست است.\",\n  \"sources\": [W+\"%D8%B7%D8%A8%D9%84\"],\n  \"ref_check\": [\n    {\"ref\": \"VFO:23\", \"status\": \"not_checked\",\n     \"note\": \"VFO = M. Ahmad Soltānī, Vāžgān-e Fārsī dar Zabānhā-ye Orūpāʾī (واژگان فارسی در زبان‌های اروپایی), Āvā-ye Nūr, Tehran 1372/1993 (Nourai's abbreviation list, pdf p. 23, no. 102). It is not in refs_online.json and no copy is available online or on disk.\"},\n    {\"ref\": \"MON:2211\", \"status\": \"partial\",\n     \"note\": \"Mo'in has طبل as an Arabic-tagged headword (MON_part2.txt line 36117 in the Adena OCR; طبل‌زن/طبل‌نواز glossed تبیر‌زن at MON_part1.txt line 92086, which equates طبل with تبیر), but the 6-vol page number cannot be verified.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"DEV\", \"where\": \"DEV.txt leaf 256, printed p. 220, s.v. Timbale\", \"stance\": \"supports\",\n     \"note\": \"'De l'arabe طبل tabl, avec l'article at-tabl, sorte de tambour… Tabl est d'origine persane.'\"},\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt line 92086\", \"stance\": \"supports\",\n     \"note\": \"'طبل‌زن، طبل‌نواز، تبیر‌زن' — Mo'in glosses the Arabic-based compound with the native تبیر‌زن, showing the two words are felt as one.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. طبل\", \"stance\": \"supports\",\n     \"note\": \"the Arabic entry lists Persian among the languages that borrowed طبل back, alongside Ottoman Turkish طبل and Spanish atabal.\"}\n  ]},\n\n {\"id\": 6, \"lang\": \"Old French\", \"words\": \"\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"A pass-through box with no word printed: the Old French link between the Arabic drum/lute words and English tambour. The form meant is OF tabour, tabur 'drum; din' (11th c., already in the Chanson de Roland: 'de tabours et de tymbres'), which by the 13th-14th c. was nasalised to tambour. The nasal is where Nourai's parent is defensible: Klein, AHD and Etymonline all say the m of tambour comes from the influence of Arabic ṭunbūr/ṭanbūr on an inherited tabour, so ṭunbūr is a real but partial parent — it shaped the word rather than supplied it. Wiktionary alone makes French tambour wholly 'from Arabic ṭunbūr', which is Nourai's reading.\",\n  \"derivation_fa\": \"این جعبهٔ تهی حلقهٔ فرانسوی کهن میان عربی و انگلیسی است؛ صورت مورد نظر tabour/tabur «دهل» است که از سدهٔ ۱۱م میلادی در شانسون دو رولان دیده می‌شود و سپس به tambour خیشومی شده است. کلاین، AHD و اتیمانلاین میم میانی را اثر طنبور عربی می‌دانند، نه اصل واژه؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [W+\"tambour\", AHD+\"tambour\", \"https://www.etymonline.com/word/tabor\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"the box carries no reference in the book (refs=None); nothing to check.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 832 s.v. tambour\", \"stance\": \"partial\",\n     \"note\": \"'F., fr. OF., fr. Arab. tabul, pl. of tabl, “drum”; influenced in form by VArab. tanbur…' — the Old French link is Klein's too, but he makes ṭab(ū)l the source and ṭunbūr only an influence.\"},\n    {\"src\": \"LAM\", \"where\": \"LAM.txt p. 233-234 and n. 2\", \"stance\": \"partial\",\n     \"note\": \"quotes the Old French attestation 'Tel noise i avait de tabour z et de tymbres' (Continuateur de Guillaume de Tyr) and derives tabour from ṭabl with l > r, rejecting tonboûr.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt line 19055 s.v. Tabour\", \"stance\": \"supports\",\n     \"note\": \"'Tabour, Tabor, a small drum. (F.-Span.-Arab.) F. tabour (mod. F. tambour). — Span. tambor, atambor… — Arab. tambur, “kind of lute or guitar with a long neck and three strings, also a drum”.' Skeat routes Old French tabour to Arabic ṭanbūr, as Nourai does.\"}\n  ]},\n\n {\"id\": 7, \"lang\": \"English\", \"words\": \"tambour; tambourine; tambour\",\n  \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"The words themselves are right: E. tambour (ME., from F. tambour) 'drum; drum-shaped embroidery frame' and tambourine (from F. tambourin, diminutive of tambour) are the regular English reflexes, both first recorded in the 16th-18th c. But the box as printed lists 'tambour' TWICE — the third slot is certainly meant for a different derivative, most likely tambourin or tambura/tamboura (both stand next to tambour and tambourine in AHD), and the extraction faithfully reproduced the duplication. The reference is also wrong: AHD:1025 falls far outside the t- band of the 1975 AHD (the chart's other t- boxes cite 1303, 1313, 1350), so the intended page was one of those; this is Nourai's slip, not the scanner's. I verified both on the printed page (pdf p. 494, book p. 464): the book itself prints 'tambour, tambourine, tambour' and '道 AHD:1025'.\",\n  \"derivation_fa\": \"خود واژه‌ها درست‌اند: tambour از فرانسوی tambour و tambourine از tambourin (مصغّر آن). امّا در جعبهٔ کتاب واژهٔ tambour دو بار آمده و جای سومی قاعدتاً باید tambourin یا tambura می‌بود؛ همچنین ارجاع AHD:1025 بیرون از محدودهٔ حرف t در آن فرهنگ است (دیگر جعبه‌ها ۱۳۰۳، ۱۳۱۳، ۱۳۵۰ می‌دهند). تصویر صفحهٔ چاپی (ص ۴۶۴) نشان می‌دهد هر دو خطا از خود کتاب است و خوانش اسکن امانت‌دارانه بوده است: خطای چاپی کتاب.\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"tambour, tambourine, tambour  [box header: English · AHD:1025]\",\n  \"correct_form\": \"tambour; tambourine; tambourin (or tamboura) — and the reference should be AHD:1303/1313, not 1025\",\n  \"sources\": [AHD+\"tambour\", W+\"tambour\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:1025\", \"status\": \"not_found\",\n     \"note\": \"page 1025 of the 1975 AHD New College Edition is in the P-range, not the T-range; the tambour entry must be near 1303-1313 (the pages Nourai himself cites for tabor and tanbur). The 1975 volume is lending-only on archive.org, so the page could not be opened; the current AHD s.v. tambour has the matching text: '[Middle English, from Old French, perhaps ultimately from alteration (influenced by Arabic ṭunbūr, ṭanbūr, tambura) of Arabic *tabbūl, hypocoristic form of ṭabl, drum, or ṭubūl, plural of ṭabl… or perhaps ultimately from alteration… of Persian tabīr, tabīra, drum; probably akin to Middle Persian tumbag…]'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 832 s.v. tambour\", \"stance\": \"supports\",\n     \"note\": \"'tambour, n., 1) a drum; 2) a drumlike frame for embroidering. — F., fr. OF., fr. Arab. tabul, pl. of tabl, “drum”; influenced in form by VArab. tanbur…'\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt lines 19056, 19121\", \"stance\": \"supports\",\n     \"note\": \"'Tambour, a small drum-like frame, for embroidering. (F.-Span.-Arab.)'; 'Tambourine. (F.-Span.-Arab.) F. tambourin, a tabour, dimin. of F. tambour, tabour or drum; see Tabour.'\"},\n    {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. tambour (current ed.)\", \"stance\": \"supports\",\n     \"note\": \"gives both Arabic ṭabl and Persian tabīr routes with ṭunbūr as an influence — the substance of Nourai's box, at a different page number.\"}\n  ]},\n\n {\"id\": 8, \"lang\": \"Old French\", \"words\": \"\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The second empty Old French box is the un-nasalised branch: OF tabour, tabur 'drum; stool', the form behind English tabor and taboret. Etymonline backs Nourai's direct Persian parent — 'from Old French tabour, tabur “drum; din, noise, commotion” (11c.), probably from Persian tabir “drum”' — and Devic argued the same in 1876. The competing and commoner view routes it through Arabic: Klein and Lammens derive OF tabour from ṭabl/ṭubūl, Skeat and Wiktionary from ṭanbūr/ṭunbūr, both by way of Spanish atambor in the crusading and Andalusi contact zone. A Persian word reaching 11th-century France without an Arabic or Byzantine intermediary is historically improbable, so the arrow is acceptable only as shorthand.\",\n  \"derivation_fa\": \"این جعبهٔ تهی شاخهٔ بی‌خیشوم است: فرانسوی کهن tabour/tabur «دهل؛ چهارپایه» که انگلیسی tabor و taboret از آن است. اتیمانلاین همانند نورایی آن را «احتمالاً از فارسی tabīr» می‌داند، ولی کلاین و لامنس از طبل/طبول عربی و اسکیت و ویکی‌واژه از طنبور می‌گیرند؛ رسیدن مستقیم واژه‌ای فارسی به فرانسهٔ سدهٔ ۱۱م بدون واسطهٔ عربی بعید است. با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://www.etymonline.com/word/tabor\", W+\"tabor\", AHD+\"tabor\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:1303\", \"status\": \"partial\",\n     \"note\": \"the 1975 page is lending-only; the current AHD s.v. tabor reads 'Middle English tabour, from Old French, variant of tambour; see TAMBOUR' — it confirms the Old French box but sends the reader to the Arabic/Persian double etymology under tambour rather than straight to Persian.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/tabor\", \"stance\": \"supports\",\n     \"note\": \"'from Old French tabour, tabur “drum; din, noise, commotion” (11c.), probably from Persian tabir “drum”.'\"},\n    {\"src\": \"DEV\", \"where\": \"DEV.txt leaf 250-251, printed pp. 215-216\", \"stance\": \"supports\",\n     \"note\": \"'…qui est assurément identique à notre tabur, tabour… Tabur est bien ancien dans notre langue, puisqu'on le trouve déjà dans la chanson de Roland, qui est du xi⸘ siècle; mais il est bien ancien aussi en persan, puisqu'il se lit dans le Chah-nameh.'\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 829 s.v. tabor\", \"stance\": \"contradicts\",\n     \"note\": \"'tabor, also tabour, n., a small drum… ME., fr. OF. tabour, “drum; stool”, fr. Arab. tabul, pl. of tabl, “drum”' — Klein inserts Arabic where Nourai has Persian.\"},\n    {\"src\": \"LKT\", \"where\": \"LKT.txt no. 1971 (Ar. tabl) and no. 1974 (Tk. tabur)\", \"stance\": \"partial\",\n     \"note\": \"Lokotsch derives the European atabal/timbale family from Ar. ṭabl; his separate no. 1974 'Tk. tabur ‚Heerlager, Bataillon‘' is a homonym unrelated to the drum and should not be confused with this box.\"}\n  ]},\n\n {\"id\": 9, \"lang\": \"English\", \"words\": \"tabor; taboret\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"E. tabor (also tabour) 'a small drum beaten with one hand while the other plays a pipe' is Middle English, borrowed from OF tabour; taboret / tabouret is French tabouret, the diminutive of the same OF tabour. The furniture sense Nourai glosses — 'a round low stool' — is the well-known metonymy: OF tabour already meant both 'drum' and 'stool' (Klein's gloss), because a drum-shaped, skin-topped seat looks like a small tabor; French tabouret has meant 'stool' since the 16th century, and English tabret is a variant of taboret. Both words are exactly where Klein and AHD put them.\",\n  \"derivation_fa\": \"انگلیسی tabor از فرانسوی کهن tabour و taboret از فرانسوی tabouret (مصغّر همان) گرفته شده‌اند. معنای «چهارپایهٔ گرد کوتاه» تحولی مجازی است: خود tabour در فرانسوی کهن هم «دهل» و هم «چهارپایه» بود، زیرا نشیمنگاه گرد پوست‌کشیده به طبل کوچک می‌ماند. ادعای نورایی درست است.\",\n  \"sources\": [AHD+\"tabor\", W+\"tabor\", \"https://www.etymonline.com/word/tabor\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:1303\", \"status\": \"supports\",\n     \"note\": \"the current AHD s.v. tabor ('Middle English tabour, from Old French, variant of tambour') matches the box; the 1975 page 1303 is in the right alphabetical band for tabor, unlike the 1025 of node #7.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 829 (running heads 1564/1565)\", \"stance\": \"supports\",\n     \"note\": \"'tabor, also tabour, n., a small drum resembling a tambourine. — ME., fr. OF. tabour, “drum; stool”… Cp. tambour, taboret.'; 'taboret, also tabouret, n., a small tabor, tabret. — F. tabouret, dimin. of OF. tabour, “drum; stool”.'\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt line 19055\", \"stance\": \"supports\",\n     \"note\": \"'Der. tabour-et or tabret, a dimin. form.'\"},\n    {\"src\": \"LAM\", \"where\": \"LAM.txt p. 234\", \"stance\": \"supports\",\n     \"note\": \"'De tabour dérive Tabouret'; and the footnote 'l'instrument tabor se nomme aussi Tabret'.\"}\n  ]}\n]\n\nout = {\n \"pdf_page\": 494,\n \"book_page\": 464,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [e0, e1]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-494.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/draft-494.py"
}
```


### [2026-09-14T03:27:13.496Z] TOOL RESULT

```
ok
```


## [2026-09-14T03:27:15.862Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-494.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 494"
}
```


### [2026-09-14T03:27:17.035Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'plausible': 4, 'confirmed': 7, 'disputed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'partial': 7, 'supports': 8, 'contradicts': 1, 'not_checked': 2, 'not_found': 1}
books consulted: {'supports': 22, 'partial': 14, 'silent': 5, 'contradicts': 9} | by book: {'KLN': 8, 'SKT': 6, 'Wiktionary': 5, 'LAM': 4, 'MON': 3, 'AHD': 3, 'Etymonline': 3, 'DEV': 3, 'HJB': 2, 'PLA': 2, 'LKT': 2, 'Dehkhoda (via abadis)': 1, 'AID': 1, 'PHN': 1, 'FSD': 1, 'BQT': 1, 'FSF': 1, 'HRN': 1, 'NYB': 1, 'PHD': 1}
```


## [2026-09-14T03:27:34.214Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-494.json` written, valid JSON, `verify_check.py 494` reports **16/16 nodes, 0 PROBLEM lines**.

**Page 494 (book p. 464) — 2 entries, 16 nodes**
- Node verdicts: 7 confirmed, 4 plausible, 4 disputed, 1 transcription_suspect
- Root verdicts: 1 confirmed (Tabaco), 1 plausible (Tabūrāk)
- Ref checks: 8 supports, 7 partial, 1 contradicts, 1 not_found, 2 not_checked

Disputed / flagged items:
- **Tabaco #4 Spanish tabaco** — arrow Portuguese→Spanish reverses the accepted priority; Klein prints "Sp., Port. tabaco" coordinated, Etymonline/AHD/Skeat make Spanish the source. (Nourai's NOTE about AHD's Arabic *al-ṭubbāq* is a faithful report and still AHD's view.)
- **Tabūrāk #2 Arabic tanbūr** — ṭunbūr is a long-necked *lute* from MP *tambūr* (poss. < Gk. pandoûra), not from the drum word tabūrāk; Lammens explicitly rejects the link.
- **Tabūrāk #3 Persian tanbūr / tonbak** — تنبور is inherited (Mo'in: طنبور is the *muʿarrab* spelling, Persian→Arabic); تنبک continues MP *tumbag* (MacKenzie, Nyberg, Arm. tʼmbuk), not Arabic.
- **Tabūrāk #4 Arabic tabūl / tabbāl** — ṭubūl is the plural of ṭabl and ṭabbāl its faʿʿāl agent noun; ṭabl is from Middle Iranian *tabir/tabil, so the box belongs under node #1, not under the lute word.
- **Tabūrāk #7 English tambour/tambourine/tambour** — `transcription_suspect`, `error_in: "book"`: the printed page genuinely repeats "tambour" (third slot should be tambourin/tamboura) **and** prints AHD:1025, outside the t- band (other boxes cite 1303/1313/1350). Verified against the 300/200-dpi render; page image saved to `data/verification/sources/refs/ocr/BOOK/494.png`.

Root caveat recorded: no Pahlavi \*tabūrāk is attested — MacKenzie/Nyberg have only *tumbag/tumbak*; the -āk is a New Persian diminutive (Devic says so), so the root box should read NP tabīr/tabīra.

No extraction errors found — the JSON matches the printed page everywhere, including the duplicated "tambour" and the odd AHD:1025. Note for the owner: **VFO** (`VFO:23`, node #5) is missing from `refs_online.json`; per the book's abbreviation list (pdf p. 23, no. 102) it is M. Ahmad Soltāni, *Vāžgān-e Fārsi dar Zabānhā-ye Orupāʾi*, Āvā-ye Nur, Tehran 1372/1993 — not available anywhere, marked `not_checked`. 17 web sources archived via `fetch_source.py`.
