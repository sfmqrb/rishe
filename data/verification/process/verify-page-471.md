# Verification process log — verify-page-471


## [2026-09-14T02:28:01.659Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 471 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-471.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-471.json. Write /home/sfmqrb/git/rishe/data/verification/page-471.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 471` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:28:02.569Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:28:03.424Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:28:03.438Z] TOOL RESULT

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


## [2026-09-14T02:28:03.973Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-471.txt"
}
```


### [2026-09-14T02:28:03.993Z] TOOL RESULT

```
1	=== PDF page 471 (book page 441) ===
2	--- entry 0 ---
3	ROOT [Avestan] Spiš : an insect, bug, flea  (refs BQT:1249)
4	#1 (parent #0) [Pahlavi] refs=BQT:1249 | spiš : flea
5	  #2 (parent #1) [Persian] refs=BQT:1249; MON:2022 | šepeš «شپش» : flea | extra: شپشه ، شپشک ، اشپش
6	--- entry 1 ---
7	ROOT [Indo-European] Spongo : fluffy, empty  (refs WLD2:621)
8	#1 (parent #0) [Greek] refs=WLD2:621 | spongos : sponge ; spoggos : sponge
9	  #2 (parent #1) [Pahlavi] refs=SOD:64 | spynj : sponge, hollow, a temporary house, inn
10	    #3 (parent #2) [Persian] refs=VFO:22; BQT:1090 | sepanj «سپنج» : hollow, worthless material world, inn
11	    #4 (parent #2) [Sogdian] refs=SOD:64 | `spnc : inn, rest house
12	  #5 (parent #1) [Arabic] refs=TAD:35 | al-esfanj : sponge
13	    #6 (parent #5) [Persian] refs=BQT:130; MON:269 | esfanj «اسفنج» : sponge
14	  #7 (parent #1) [Latin] refs=KLN:1494 | spongia ; fungus
15	    #8 (parent #7) [English] refs=None | sponge ; fungus
16	--- entry 2 ---
17	ROOT Spreg -> redirect to Spereg
18	--- entry 3 ---
19	ROOT Sprek -> redirect to Spereg
20	--- entry 4 ---
21	ROOT [Indo-European] Spyeu, Sphîeu : to spit  (refs POK:1000)
22	#1 (parent #0) [Persian] refs=POK:1000; BQT:502 | tof «تُف» : spit ; tofang «تُفنگ» : "spitter", gun
23	#2 (parent #0) [Sanskrit] refs=IEC:1005 | sthîvâmî : spit
24	#3 (parent #0) [Germanic] refs=None | 
25	  #4 (parent #3) [English] refs=AHD | spit ; sputter
26	#5 (parent #0) [Greek] refs=IEC:1005 | ptuô : spit
27	--- entry 5 ---
28	ROOT Sqand -> redirect to Skand
29	--- entry 6 ---
30	ROOT Sqombh-no -> redirect to Kamma
31	
```


## [2026-09-14T02:28:06.912Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-471.json",
 "description": "Read source JSON for page 471"
}
```


### [2026-09-14T02:28:06.955Z] TOOL RESULT

```
{
  "pdf_page": 471,
  "book_page": 441,
  "entries": [
    {
      "root": {
        "name": "Spiš",
        "lang": "Avestan",
        "refs": "BQT:1249",
        "gloss": "an insect, bug, flea"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:1249",
          "words": [
            {
              "translit": "spiš",
              "gloss": "flea",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1249; MON:2022",
          "words": [
            {
              "translit": "šepeš",
              "gloss": "flea",
              "script": "شپش"
            }
          ],
          "script_extra": "شپشه ، شپشک ، اشپش",
          "note": null,
          "quote": {
            "text": "جامه ات شویم شپشهایت کشم - شیر پیشت آورم ای محتشم",
            "poet": "Molavî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Spongo",
        "lang": "Indo-European",
        "refs": "WLD2:621",
        "gloss": "fluffy, empty"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "WLD2:621",
          "words": [
            {
              "translit": "spongos",
              "gloss": "sponge",
              "script": null
            },
            {
              "translit": "spoggos",
              "gloss": "sponge",
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
          "refs": "SOD:64",
          "words": [
            {
              "translit": "spynj",
              "gloss": "sponge, hollow, a temporary house, inn",
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
          "refs": "VFO:22; BQT:1090",
          "words": [
            {
              "translit": "sepanj",
              "gloss": "hollow, worthless material world, inn",
              "script": "سپنج"
            }
          ],
          "note": null,
          "quote": {
            "text": "سپنجی سرایست دنیای دون - بسی چون تو میرفت غمگین برون",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Sogdian",
          "refs": "SOD:64",
          "words": [
            {
              "translit": "`spnc",
              "gloss": "inn, rest house",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Arabic",
          "refs": "TAD:35",
          "words": [
            {
              "translit": "al-esfanj",
              "gloss": "sponge",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:130; MON:269",
          "words": [
            {
              "translit": "esfanj",
              "gloss": "sponge",
              "script": "اسفنج"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 1,
          "lang": "Latin",
          "refs": "KLN:1494",
          "words": [
            {
              "translit": "spongia",
              "gloss": null,
              "script": null
            },
            {
              "translit": "fungus",
              "gloss": null,
              "script": null
            }
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
            {
              "translit": "sponge",
              "gloss": null,
              "script": null
            },
            {
              "translit": "fungus",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Spreg",
        "redirect": "Spereg"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sprek",
        "redirect": "Spereg"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Spyeu, Sphîeu",
        "lang": "Indo-European",
        "refs": "POK:1000",
        "gloss": "to spit"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:1000; BQT:502",
          "words": [
            {
              "translit": "tof",
              "gloss": "spit",
              "script": "تُف"
            },
            {
              "translit": "tofang",
              "gloss": "\"spitter\", gun",
              "script": "تُفنگ"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:1005",
          "words": [
            {
              "translit": "sthîvâmî",
              "gloss": "spit",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "spit",
              "gloss": null,
              "script": null
            },
            {
              "translit": "sputter",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:1005",
          "words": [
            {
              "translit": "ptuô",
              "gloss": "spit",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sqand",
        "redirect": "Skand"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sqombh-no",
        "redirect": "Kamma"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T02:28:09.918Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','WLD','SOD','VFO','TAD','KLN','POK','IEC','AHD','PHD','NYB','HRN','HUB','BRT','CHEUNG','ARY','SKT','WEB','FSD','SYN','LKT','PLA','AFM','FVQ']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:600]); print()\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-14T02:28:11.074Z] TOOL RESULT

```
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

VFO MISSING
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
```


## [2026-09-14T02:28:15.692Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(sorted(d.keys()))\n\" ; ls data/verification/ | head -50; echo ---; grep -rn \"VFO\" data/verification/sources/*.json data/verification/sources/*.md 2>/dev/null | head -20"
}
```


## [2026-09-14T02:28:15.730Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,140p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T02:28:16.842Z] TOOL RESULT

```
['AEF', 'AFA', 'AFM', 'AHD', 'AHM', 'AID', 'AIN', 'AKD', 'AKM', 'AMD', 'ARB', 'ARK', 'ARM', 'ARP', 'ARY', 'AVG', 'AWH', 'BLY', 'BQT', 'BRT', 'BST', 'CEL', 'DEV', 'DMO', 'DOZ', 'DRM', 'DVS', 'DZA', 'EAV', 'ETM', 'FAF', 'FFD', 'FIB', 'FNI', 'FRS', 'FSD', 'FSF', 'FVA', 'FVF', 'FVQ', 'FVS', 'FWE', 'GPL', 'HID', 'HJB', 'HRN', 'HUB', 'IEC', 'IRN', 'IRT', 'ISS', 'KAS', 'KFL', 'KGW', 'KLN', 'KNT', 'LAM', 'LAT', 'LEW', 'LKT', 'LST', 'MAG', 'MFL', 'MMF', 'MON', 'MPP', 'MZF', 'NAT', 'NFI', 'NYB', 'OEW', 'OXF', 'PEI', 'PHD', 'PHN', 'PLA', 'POK', 'PRT', 'RCH', 'ROE', 'SAP', 'SBK', 'SDQ', 'SHP', 'SIN', 'SKT', 'SLW', 'SNB', 'SNS', 'SOD', 'SOG', 'SOR', 'SPG', 'SYN', 'TAD', 'TLM', 'TTS', 'TYL', 'TZF', 'UNV', 'VDQ', 'VGH', 'VIE', 'VOP', 'VSF', 'WEB', 'WLD', 'ZAP', 'ZAW', 'ZFS', 'ZMA']
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
---
data/verification/sources/MISSING_REFERENCES.md:110:| VFO | (unresolved abbreviation, probably = VOP) | skipped | — |
```


### [2026-09-14T02:28:16.890Z] TOOL RESULT

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
```


## [2026-09-14T02:28:38.405Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT spis ===\"; grep -n -i \"spis\\|spiš\" BRT.txt | head -30\necho \"=== PHD spis ===\"; grep -n -i \"spiš\\|spis\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== HRN spis/sipis ===\"; grep -n -i \"sipis\\|šipiš\\|Laus\\|spiš\" HRN.txt | head -30"
}
```


### [2026-09-14T02:28:38.497Z] TOOL RESULT

```
=== BRT spis ===
2291:KD.:  Kaspische  Dialekte. (KD)g.!  CiiiiT. (KD)m.!  Afäsandaränü (KD)s.:  Samnäm.
10291:mit  nis  'auf-,  wegfressen',  von  Tieren: spis  (sd.)  . .  yim  tnasyaka  yaom  yav5.hva niigaahinti  vaslra  vasträhva  V.ij.^.
10635:•  j.,  g.  xrafstra-  n.  i)  im  gAw.  'wildes Tier,  Raubtier":  atibyS  mas  äsä  syasdat (sd.)  yentat  ahmat  aurunä  'rH  (AP.)  Y. $4.  9.  a)  im  Plur.  als  Bezeichnung  für die  nicht  sesshaften  Religionsfeinde  und deren  Gölter,  sva.  'Raubgesindel':  anä mq'ira  maxist?in  väurüimaidl  (sd.)  Tä (A'P.)  hizvä  Y.  28.5;  —  pari  *vä  vJspäis pars  vaox?mä  dalviliscil  °räis  maSyäis^ä "losgesagt  haben  wir.  uns  von  allen  Xraf- stra^ (allem  Raubgesindel),  den  Daivas wie  den  Menschen"  "  Y.34. 5 ;  verwendet  Y. ig.  2.  2)  im  jAw,  Bezeichnung  fUr  alle schädlichen  ((/iZÄischen)  Tiere,  bes.  der niederen";  paitUtätie  a/astaca  zBüdiftaca apayantamaheca  a?prahe  mainyius  °ra Yt  21.1;  —  duye  Saite  kahyäcit  ar>rö.- mainyavanqm  "ranqm  ava.janyäl  V.  16. 12;  —  ähva  vyar?hähva  (sd.)  e^mB  'ra ham.bavainti  yim  tnasyäka  spis(sd.  tiqma aojaitt  V.  z/. 3;  —  *maxSiMhrpa  ..*akara- tum-driwyi  (sd.)  ya%a  taehdistäiS  'räis V.  7.  2;  —  Y.  ig.  2:  s.  unter  1.
13582:•)'  Die  Diihar,  Jati,  jäai,  ein  skylhischer Volksstamm,  wohnten  östlich  vom  kaspischen Meer;  vyl.  Geilt.  OK.  2ol,  DsT.  ZA.  2.  554. Bd.  /f.  29  Tcneichnet:  äii  i  pa  diy  (in  Aw.- Buchit.l  dih.
14880:—  %ris  m&tihs  upaia^ayen  raoiamm  -ti nmänahe  V.  7. 14;  —  kimcit  'ti  cah. nqm  (Stverz.)  V. 2. 25  usw.;  —  up3m)m{sdi.) */i  va-fianahe  V.  Ä38;  —  var^ayatmha ..  vispisca  'ii  varfajti  \ .  10.  %;  5';  — aeslaisA.ya  °ti  dumnaca..gaisus\.y.$<); —
15825:•  j.  parSuya-  Adj.  (fem.  'ys-)  'nivalis, Schnee-',  Bezeichnung  bestimmter  Wasser; vispisca  aps  ya  ztmä  .  .  'ya  (NPf.)  *väir- yäsca  Y.  6S.  6.
17654:•  j.  fra-pad-  :fra-bd-  m.  'Vorderteil  des menschlichen  Fusses,  Vorderfiiss',  vom Knöchel  bis  zu  den  Zehenspitzen:  dasiram {hdyum)  'hdtm  V.  8.  67,  68',  69,  <J.  24*;  — yat  nä  paurva  °bda  (AD.)  /rabdöjirajB frama&aiü  "wenn  Jemand  über  die  Spitzen der  Vorderfüsse  um  eines  Vorderfiisses Länge  hinauspisst"  V.  /<?.  40*';  —   °bda
17657:hat :  ia  marl  fa  vinäsiärVi  pes  i  /rapiA /rapai  drahnäi  fräc  mnel  "wenn  man  sündiget Weise  Tor  den  Vorderfuss  einen  Vorderfuss  weit hinauspisst".  Die  Sonde  heisst  Av.35.6  hai pä% mkiihik  "Stehendpissen'.  Das  Pissen  soll  in hockender  Stellung  und  so  geschehen,  dass  der Urin  mischen  den  Fiissen  zu  Boden  geht.  Vgl. die  PüGlosse  in  V.  iS.  44  (bei  Haug  Essajrs  »  374). KompA.  —  n.  präpäd- -OL.  —Yü,-.  frapai,frabd.
21342:speicher": spis  {sA.)  . .  yim  . .  yaom  'vöJtva nUgankmti  V,  77. 3,
23154:—  kat  ta  'ra  yaoidayan  arthfn  V.  7.  1 1 ; Vd.  /2,  20;  —  yim  antar»  'nm  frajasat Csd.)  V.  16.  16;  —  spis  (sd.)  . .  yim  . . nizgaakwti  'ra  i/astrakva  V.  17.  3;F.&
23158:•  j.  vastran-  n.  'Aufbewahrungsort  für Kleider,  Kleiderkammcr' :  spis  (sd.) .  .yim . . yaom  yavS.hva  nizgatikttUt  vastra  'rähva (LP.)"  V.77.3.
23809:*)  Welcher  See  ursprünglich  so  genannt wurde  -  der  Kaspische,  der  Aralsee?—,  ist nicht  festzustellen,  da.  er  jedenfaUs  schon  früh- leilig  sagenhaft  wurde.  Er  gplt  fQr  die  grösste Wasserfläche  und  für  ias  Sammelbecken  aller Wasser.  Zwei  Buchten  und  ein  Aim  des  Sees werden  Yt.  ig,  56,  59,  6z  genannt.  Inmitten des  Sees  stehen  der  Baum  vlspöMs  (sd.)  und  der heULge  Eiel  (s.  xara-  a).  Vgl.  noch  Bd.  13  und West    SBE.  $■    424    unter   'Ocean'.     Mx.  gibt
27064:•  j.  spi§-'>  n.  'Laus,  Milbe  (od.  dgl.)': Sat . .  xrafstra  hqm.bavainti  yiin  masyäia spis{NS.)  nqma  aojaile yim  tnasyäta  yaom yavS.kva  nnganh}nti  vastra  vasträhva ".  .  die  Xr.  . .,  was  die  Leute  'Laus' nennen,  was  den  Leuten  das  Getreide  in den  Speichern  wegfrisst,  die  Kleider  in den  Kammern"  V.iy.^'K
27065:mp.  spis,  sfus,  np.  supiis.  —  Pü.:  spis.  — ')  Oder  aucb  spis-,  —  *)  Grammatisch  geringe Stelle.
=== PHD spis ===
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
PHD.txt:1579:despise tar kardan / menidan.
PHD.txt:2677:louse spiš.
PHD.txt:4781:spihrīg uo ev spenāg wvav spig 135035 spiz- —-Q5 Q335 spīzišn 1^0 2301 spiš ^U" Q335 spitāmān 16” 10 035 spēd-dār `o тез as»
PHD_mackenzie.txt:4617:spis [spyf I (N fipif)] louse.
PHD_mackenzie.txt:4923: ,ow    kardan, -- menidan: abuse, despise.
PHD_mackenzie.txt:6357:    niiydag.                                despise tar kardan I menidan.
PHD_mackenzie.txt:6986: likeness ewsanih, hangosidag, hawan-    louse spis.
PHD_mackenzie.txt:7736:swing wextan.                              thanks azidih, spis; v. gratitude.
PHD_mackenzie.txt:8952:                        ~~               spis                       ""lY CO-'-'
=== HRN spis/sipis ===
4457:491. yi^eSTn 'bläulich, blauschwarz'; vergl. x^sisar (äähn. I,
5507:618. risk 'Lauseei, Nisse' (AM. 141 Zeile 11, 191 Zeile 7).
5508:ai. liksd' 'Ei einer Laus, Nisse' (Nöldeke bei
6191:705. siijJuS, uspus 'Laus', siqms (etc.).
6193:aw. spis 'Laus'; phlv. spis (vd. 17 (8)), sjjus (AV.).
6194:kurd. sipi^ aspe 'Laus' ; afy. spa$a ; oss. sis^ (239) ;
11199:vermittelst des Accentes ist plausibel für die vorkommenden Formen
```


## [2026-09-14T02:28:40.824Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD spanj ===\"; grep -n -i \"spanj\\|spynj\\|spinj\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20\necho \"=== SOD spnc ===\"; grep -n -i \"spnc\\|spanc\\|inn, rest\\|rest house\" SOD.txt | head -30\necho \"=== HRN sipanj ===\"; grep -n -i \"sipang\\|sipanǰ\\|spanǰ\\|sipanj\\|Herberge\" HRN.txt HUB.txt | head -30"
}
```


### [2026-09-14T02:28:40.925Z] TOOL RESULT

```
=== PHD spanj ===
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:2322:hospitality aspinj, mehmānīh, spin- jānagīh.
PHD.txt:2444:inn aspinj.
PHD.txt:4773:spéd spēdag spēdbāg spenāg spóxtan spandan Spandarmad sabuk spul spurrigih spurrig spurdan spūz spēz- spinjānagīh spozgar spūzišn sabz spazg spazgīh spar spar- sprahm sprahmag
NYB_vol2_glossary.txt:700:aspinj [’spne'] lodging 7310. 7512. - MPrth ‘spyn) (A-H III); Aram. lw. Talm ?wspyz’, Syr ’espezzä; Paz. aspanž, aspenj; NP sipanj ‘a halting-place, a shelter’. Cf further Arm. lw. aspnjakan (< aspinj-) ‘landlord, innkeeper’ = Talm *wšpyzkn”, Syr ’espizkänä, 'ešpazgānā; Telegdi 231 sg. V. also spinjanakeh.
NYB_vol2_glossary.txt:3493:spinjanakéh [spne’nkyh] the act of lodg- ing 85°. — V. aspinj. Paz. aspanžanai. Bailey, BSOS VII, 1933, 74-76.
NYB_vol2_glossary.txt:5552:‘spynj: aspinj
NYB_vol2_glossary.txt:6382:asöisn: asöhisn aspanž | ua aspenj | aspinj
NYB_vol2_glossary.txt:6383:aspanžanai: spinjānakēh
NYB_vol2_glossary.txt:7400:sipanj: aspinj
PHD_mackenzie.txt:1230:aspin} ['spnc I p Cspynj, N sipanj] hospitality; inn. 0S.\ \')..J   ~
PHD_mackenzie.txt:4616:spinjana~ih [spnc)nkyh] hospitality.
PHD_mackenzie.txt:6792:hero er, gurd, wir, yal; befitting a ,.....,   hospitality aspinj, mehmanih, spin-
PHD_mackenzie.txt:6879:   inn aspinj.                             item tag.
PHD_mackenzie.txt:8936:spinjanagih   AU ~ ~ ~ \ Q)..1)
PHD_mackenzie.txt:11596:aspinJ               c;,~         hamtan
=== SOD spnc ===
18117:(o)spanc   ©loc.  -yh  =^spnc,  sp'nc,  >spn- 
18244:(o)spanst,  spanst  ?  ^sp'nch,  >spnc 
18307:(o)spancn  ?   ^spnyn^y 
18333:(o)spancn-kocc 
18337:1628  *spnc   M  ^^  <  I^-OW9 
18338:(o)spanc   ©<Parth.  MP  }spynj  ©pi.  -//,  -ynsi 
18344:1965,  244nl>  pi.  "sp'ynsu  GMS  260;  >spncu 
18595:ospancne  ?   Ospnyn'k)  -^spnyn'y 
23505:(o)spinc,  osponc   =Vspnc 
67853:spanc  ©ob.  -yh  ^sptoch 
67961:8894  spncyrspn   C  ^jL^^jIjuL^ 
67962:spancirspan  ?  ©ob.  -y(>\  pi.  -t 
80204:10660  xspncyk   M  <L^ 
=== HRN sipanj ===
HUB.txt:6293:siparl Vollendet' H. 703, oben p. 73; sipanj *Ruheplatz'
HUB.txt:8262:sipanj, syr. aspizkana, mand. spinza aus *aspinj (oben p. 73).
```


## [2026-09-14T02:28:49.040Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD 1628 context ===\"; sed -n '18330,18350p' SOD.txt\necho \"=== SOD_pages find spnc ===\"; grep -n \"1628 \\*spnc\\|spanc\" SOD_pages.txt | head -10\necho \"=== HUB p.73 context ===\"; grep -n -B3 -A12 \"sipanj \\*Ruheplatz\\|sipanj 'Ruheplatz\" HUB.txt | head -60"
}
```


### [2026-09-14T02:28:49.182Z] TOOL RESULT

```
=== SOD 1628 context ===

1627  'spn'ynkwc'k    B  jUo^T 

(o)spancn-kocc 
having  an  iron  beak 
SCE  262 

1628  *spnc   M  ^^  <  I^-OW9 
(o)spanc   ©<Parth.  MP  }spynj  ©pi.  -//,  -ynsi 

=>(spync,  'sp'nch,  'sp'ynst 
inn,  rest  house 
GMS  112,  260;  Hen.  BSOAS  12,  307,  37;  BSOAS 

1965,  244nl>  pi.  "sp'ynsu  GMS  260;  >spncu 

BSOAS  12,  307.37 

1629  >spnd    M  (jj^Jjj* 
spand 

=== SOD_pages find spnc ===
8406:      (o)spanc ©loc. -yh =^spnc, sp'nc, >spn-                           VJ 844; GMS 994
8435:                                                            U*J*"         (o)spancn ? ^spnyn^y
8457:        TSP 6.104                                                         (o)spancn-kocc
8461:     white                                                          1628 *spnc M                          ^^ < I^-OW9
8462:      TSP 3.4, 12, 5.54; STii 10, 19, 23 & etc.                          (o)spanc ©<Parth. MP }spynj ©pi. -//, -ynsi
8590:                ospancne ? Ospnyn'k) -^spnyn'y                          1679 'st'np B                  (<r~^)^
29298:          Intox. 6                                                   spanc ©ob. -yh ^sptoch
29399:      spancirspan ? ©ob. -y(>\ pi. -t                                0<?)serve, (to)respect
=== HUB p.73 context ===
6290-H. 696; supurdan 'anvertrauen H. 697; sipas Dank, Lob'
6291-(Etym.?) H. 698; sipah 'Heer H. 699; sipar 'SchM H. 700;
6292-sipardan *auf etwas treten' H. 701; supurz *Milz H. 702;
6293:siparl Vollendet' H. 703, oben p. 73; sipanj *Ruheplatz'
6294-H. 704, supus *Laus H. 705; sipoxtan *heraustreiben' H. 706;
6295-sipihr 'Himmer H. 707, sipBd weiss' H. 708.
6296-Der Uebergang von sp in sf ist jiinger und wohl dia-
6297-lektisch. Die Araber schreiben zudem sf fiir sp in pers.
6298-(und griech.) W5rtern.
6299-Fiir sp ist schon im Ap. einigemal s eingetreten : visa-
6300-*air neben vispa- (vispazana-^ phi. harvisp); asa- Tferd' in
6301-asabara- *Reiter (np. suvCLr) neben Aspacana {== skr. *agva-
6302-dands^ zd. aspdcind = Tferde-wiinschend'), (h)uvaspa'^ Vis-
6303-tc^spa-j np. asp^ arm. aspet (= "^aspapati-) ; ^asaiara- *Maul-
6304-esel* = np. astar gegen skr. agvatara-] ^saka- *Hund' =
6305-np. sag gegen medisch spaka- {andyt-u bei Hero dot), ka§.
```


## [2026-09-14T02:28:50.075Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 8262 context ===\"; sed -n '8250,8275p' HUB.txt\necho \"=== HRN 705 context ===\"; sed -n '6185,6205p' HRN.txt"
}
```


### [2026-09-14T02:28:50.155Z] TOOL RESULT

```
=== HUB 8262 context ===
ein Artsrunier (Eliac u. s. w.j = zd. mid^ro-aojah- 'mithra-
machtig, phi. geschrieben M(i)trucn ZDMG. 46, 286, sprich:
Mihrojan. Ueber Thavre^ — np. Tabriz siehe § 72.
Also np. parvez = arm. AprvSz (oben p. 40 und § 69)
mit altem z, ebenso wie perdz ^^ arm. Peroz u. s. w. (oben
p. 45).
Damit ist das Vorhandensein des ^ im Phi. erwiesen,
dessen Schrift zwar je ein Zeichen fiir d, S und z, aber
keines fiir / und z hatte (siehe § 118).
5; 123. Nach n erscheint dagegen im Armenischen j:
aparanjan 'Armband' = np. abranjan ; aspnjakan 'der einen
Fremden gastlich aufnimmt, Wirth', phi. paz. aspanj, np.
sipanj, syr. aspizkana, mand. spinza aus *aspinj (oben p. 73).
Das Armenische hat also z im Anlaut sowie inlaut. nach
Vokalen und r, dagegen / nach «.
Hochst auifallig sind nun vier Worter, in denen per-
sischem nf (d. i. ndz) armenisches nj (d. i. ndz) gegeniiber-
steht: Ganjak 'Stadt in Atrpatakan (Faust us, Sebeos) =
^QY^.Ganjak, Ganja, gr. Totfaxa, lat. G^a^a, (?an^ag'a_,Plinius,
Gazaca Ammian, ar ab. /an-s^a, jaznaq u. s. w. Tab. 100; —— 232 —
bfinj^) 'Reis' (Mos. Geogr. ed. Soukry 43, 6 v. u., Galen,
Yaismav.) = np. birinjf, gurinj^), afgh. vrize, skr. vrihi^
(Atharva Veda), gr. ogv'Qa ; — ganj *Schatz' (5. Jhd.) = np.
ganj, phi. ganj Gl. and Ind. 274, skr. LW. ganja-, gr. yd^a,
syr. Nill *Schatz', dazu X*1DT:i --= hebr. "\2u *Schatzmeister'
= arm. ganjavor^ np. ganjvar ; — plinj *Kupfer, Erz' (5. Jhd.)
=== HRN 705 context ===
'Steuern von Kriegsgefangenen , Sklavengeld', serb.
spendza *Aufwand', rumaen. spendze 'Steuer, bulg.
ispenö 'Sklaventaxe' bei Miklosich, Denkschr.
WAW. Band 37, 48 und 38, 130 (dort falsch erklärt).
de Lagarde, Armen. Stud. No. 207 sieht in dem
Worte eine Zusammensetzung mit np. esp *Pferd'.
705. siijJuS, uspus 'Laus', siqms (etc.).
miiz. isftj (H.-Sch.).
aw. spis 'Laus'; phlv. spis (vd. 17 (8)), sjjus (AV.).
kurd. sipi^ aspe 'Laus' ; afy. spa$a ; oss. sis^ (239) ;
wa/. sisy sar. spal.
706. sipöyten^ supö/ten 'einheften {der- Sa'di, Bostän
S. 261 Vers 304); heraustreiben (Sahn. III, 1797
Vers 231; Is. 16, 3, 4)' 0.
phlv. spöj (päz. spöz) 'Aufschub' (Salemann, Mel.
asiat. IX, 247, 248 Note 85), spö/tan^ spöjet 'ent-
fernen, heraustreiben (Men., AV.), spö/tUan; arm. LW.
spidem Verschieben'.
Wenn 'einheften' die Grundbedeutung ist, so Hesse
sich lat. pungö (V^ptig-) vergleichen; doch ist dies
durchaus unsicher.
```


## [2026-09-14T02:28:53.208Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"704\\.\" HRN.txt | head -5; echo ---; sed -n '6160,6195p' HRN.txt"
}
```


### [2026-09-14T02:28:53.270Z] TOOL RESULT

```
6179:704. 8ipe7iJ 'RuhepVdtz, Gasthaus' (8ähn. I, 229 Vers 1791).
13622:sipenj 704.
15629:aspaiij 704.
16864:Sf>aii3äiii'kih 704.
22897:rum. spendze 704.
---
2) Zu arm. sparapet oQx^^^Qa^nyoi vergl. Hübschmann, ZDMG.
35, 133 Note 2.
') In diesem Falle gehen die np. Dialekte mit dem Pehlevl zusammen
und setzen eine ap. Grundform ohne r- Vokal voraus. Die Einstimmig-
keit der Dialekte in der Verwerfung des r- Vokals — alle Ausnahmen
beruhen auf Übertragungen aus der Schriftsprache — haben mich —
zusammengenommen mit dem Material, welches die modernen iranischen
Sprachen liefern sowie einer Vorliebe des Neupersischen für Trübung
ursprünglicher a, 6 in u ~ veranlasst, KZ. 32, 572 folg. dem Altpersischen
den r- Vokal abzusprechen. Ich möchte jetzt jedoch an dieser Meinung
nicht mehr festhalten, zumal da auch das Beläcl noch deutliche Spuren
eines einstigen Besitzes des r- Vokals aufweist.— 156 —
aw. spereza- 'Milz' (ZPGl.) ; pblv. spärz; ai. pWidn-
*Milz\
703. siperl Vollendet', isperl .(Sahn. II, 820 Vers 866).
aw. "^usjjerena-, tis- 4- {/'par- ; LW. chald. N^löDN,
arm. spar.
de Lagarde, Semitica 45. Unsicher, vergl. np.
supürden (No. 697).
704. 8ipe7iJ 'RuhepVdtz, Gasthaus' (8ähn. I, 229 Vers 1791).
plilv. «5paw/ 'Ruheplatz, Asyl' (Men. ; AV.), spun-
jänaklh, arm. LW. aspnjakan Gast', cliald. syr. LW.
rr^'N, prSK^N 'Gasthof, Gasthofbesitzer (de Lagarde,
Semitica 51).
Dazu gehören auch die Lehnworte türk. ispenje
'Steuern von Kriegsgefangenen , Sklavengeld', serb.
spendza *Aufwand', rumaen. spendze 'Steuer, bulg.
ispenö 'Sklaventaxe' bei Miklosich, Denkschr.
WAW. Band 37, 48 und 38, 130 (dort falsch erklärt).
de Lagarde, Armen. Stud. No. 207 sieht in dem
Worte eine Zusammensetzung mit np. esp *Pferd'.
705. siijJuS, uspus 'Laus', siqms (etc.).
miiz. isftj (H.-Sch.).
aw. spis 'Laus'; phlv. spis (vd. 17 (8)), sjjus (AV.).
kurd. sipi^ aspe 'Laus' ; afy. spa$a ; oss. sis^ (239) ;
wa/. sisy sar. spal.
```


## [2026-09-14T02:28:55.171Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN sponge ===\"; grep -n \"spongia\\|sponge, n\\|σπόγγος\\|spoggos\" KLN_1966.txt | head -20\necho \"=== KLN fungus ===\"; grep -n \"^fungus\\|fungus, n\" KLN_1966.txt | head -10"
}
```


### [2026-09-14T02:28:55.295Z] TOOL RESULT

```
=== KLN sponge ===
36366:(med.)  —  Medical  L.,  formed  with  suff.  -itis  fr. Gk.  ajrovSuXcx;,  ‘vertebra’.  See  spondyl. spondylo-,  before  a  vowel  spondyl-,  combining form  meaning  ‘vertebra’.  —  Gk  ottovSuXo-,  fr. (77r6vSuXo?,  ‘vertebra’.  See  spondyl. sponge,  n.  —  ME.,  fr.  OF.  esponge  (F.  eponge), fr.  L.  spongia,  fr.  Gk.  aTtoyyia,  ‘sponge’  (rel. to  airoyvo^,  Att.  rccioyyo;,  of  s.m.),  which — together  with  Arm.  sung,  sunk,  ‘sponge,  cork tree,  pumice  stone’ — is  borrowed  from  an  un¬ known  source.  L.  fungus,  ‘mushroom,  fungus’, is  a  loan  word  fr.  Att.  a'joyyo-.  See  fungus  and cp.  spunk.
36370:spongelet,  n.,  spongiole.  —  Formed  fr.  sponge, n.,  with  dimin.  suff.  -let. spongiform,  adj.,  resembling  a  sponge.  —  Com¬ pounded  of  L.  spongia,  ‘sponge’,  and  forma, ‘form,  shape’.  See  sponge,  n.,  and  form,  n. spongiole,  n.  —  F.,  fr.  L.  spongiola,  ‘rose  gall, small  roots’,  dimin.  of  spongia,  ‘sponge’.  See sponge,  n.,  and  2nd  -ole. spongo-,  combining  form  meaning  ‘sponge’.  — Gk.  crTroyyo-,  fr.  aroyyoc,  ‘sponge’.  See sponge,  n.
=== KLN fungus ===
```


## [2026-09-14T02:29:05.190Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['KLN','WLD','SOD','POK','IEC','AHD','BQT','MON','TAD','HRN','HUB','NYB','PHD','SYN','LKT','AFM','PLA','FVQ','ARY']:\n    v=d[k]; print(k, '|offset:', v.get('page_offset'), '|hint:', str(v.get('lookup_hint'))[:300]); print()\n\""
}
```


### [2026-09-14T02:29:06.252Z] TOOL RESULT

```
KLN |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

WLD |offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). |hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.

SOD |offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) |hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur

POK |offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv

IEC |offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

AHD |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru

BQT |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d

MON |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe

TAD |offset: 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image |hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.

HRN |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

HUB |offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

NYB |offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

PHD |offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

SYN |offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.

LKT |offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.

AFM |offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image |hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').

PLA |offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). |hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)

FVQ |offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) |hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).

ARY |offset: printed page = pdf page + 1 |hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
```


## [2026-09-14T02:29:12.688Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN leaf containing sponge entry ===\"\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'sponge,  n.' in l or 'sponge, n.' in l:\n        print('leaf',i, 'approx pages', 2*(i-12), 2*(i-12)+1)\n        # print page numerals\n        print(re.findall(r'\\b1[45]\\d\\d\\b', l)[:10])\nEOF"
}
```


### [2026-09-14T02:29:13.924Z] TOOL RESULT

```
=== KLN leaf containing sponge entry ===
leaf 793 approx pages 1562 1563
['1588']
```


## [2026-09-14T02:29:14.577Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK spjeu ===\"; grep -n -i \"sp.*ieu-\\|spjeu\\|spÊ³\\|to spit\" POK_full.txt | head -20\necho \"--- lemma search ---\"; grep -n \"lemma: sp\" POK_full.txt | head -40"
}
```


### [2026-09-14T02:29:14.669Z] TOOL RESULT

```
=== POK spjeu ===
80564:Meaning: to spit 
90564:uema-: to spit, vomit. 
90769:Meaning: to spit, vomit 
--- lemma search ---
79425:Root / lemma: spako- 
79439:Root / lemma: speg- 
79459:Root / lemma: speR- 
79518:Root / lemma: spend- 
79594:Root / lemma: speno- steno- p(a)steno- 
79629:Root / lemma: spergh-, spregh-, nasalized sprengh- 
79685:Root / lemma: sper-2(g-) 
79718:Root / lemma: sper-3 
79749:Root / lemma: sp(h)ei. sp(h)iav\6 sp(h)e. sp(h)a-2 
79821:Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- 
79962:Root / lemma: sp(h)e(n)d- 
79985:Root / lemma: sp(h)eng- 
79993:Root/ lemma: sp(h)eng-\ to shine derived from Root/ lemma: *(s)p(h)ereg-, (s)p(h)erag-, 
80030:Root / lemma: sp(h)erd(h)-, (s)p(h)red(h)-, nasalized sp(h)rend(h)- 
80040:Root / lemma: sp(h)erd(h)-, (s)p(h)red(h)-, nasalized sp(h)rend(h)-\ to rush; to spring; 
80093:Root / lemma: sp(h)er-1, sp(h)era- 
80107:Root/ lemma: sp(h)er-1, sp(h)era-\ to make a rash movement, to push away, to rush, 
80290:Root / lemma: sp(h)er-3 
80420:Root / lemma: sp(h)e(i)-3, 5/7A-and sphe-. spha- 
80523:Root / lemma: sp(h)e-, sp(h)a-(<S^-) 
80594:Root / lemma: sp(h)reig- 
80727:Root / lemma: sprei- spreu-
```


## [2026-09-14T02:29:22.147Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in range(790,797):\n    l=leaves[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', l)\n    print(i, nums[:6], l[:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:29:23.346Z] TOOL RESULT

```
790 ['1491'] ument  for  meas¬ uring  blood  pressure  in  the  arteries.  —  Com¬ pounded  of  sphygmo-  and  manometer, sphygmomete
791 ['1492']  (naut.)  — Formed  fr.  spinx,  misreading  of  Sphinx,  the name  of  a  yacht  that  carried  the  sail, spinneret,  
792 []   despite. Derivatives:  spite,  tr.  v.,  spite-ful,  adj.,  spite-ful- ly,  adv.,  spite-ful-ness,  n. spittle,  n.  —
793 [] lunderer.  —  L.  spoliator, ‘pillager,  plunderer,  spoiler’,  fr.  spoliatus,  pp.  of spoliare.  See  spoil,  v.,  an
794 ['1499'] a  with  the  dimin.  suff.  -ala. See  spore  and  -ule. spot,  n.  —  ME.  spotte,  spot,  rel.  to  MDu.  spot, spott
795 [] ask’,  and  to  OE.  spurnan,  ‘to  kick  with  the  foot’ ; see  spurn  and  cp.  speer,  spoor.  It.  sp(e)rone,  F. e
796 ['1501'] quander,  tr.  v.  —  Of  uncertain  origin. Derivatives:  squander-er,  n.,  squander-ing-ly, adv. square,  n.  —  ME.,
```


## [2026-09-14T02:29:29.333Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '80550,80600p' POK_full.txt\necho \"=== fungus in KLN ===\"; grep -n \"fungus,\" KLN_1966.txt | head -5"
}
```


### [2026-09-14T02:29:29.410Z] TOOL RESULT

```
with Morms probably Germanic *spet^a-, speda- in Middle High German sp5/"blattrig 
brechendes rock. Spat, Modern High German dial, also spaad, Dutch spaath. 

References: WP. II 652 f.; 



See also: to sp(h)ei-2, sp(h)e-. 
Page(s): 980 



Root / lemma: (s)p(h)ieu- : (s)pju-, (s)pTu- {*ps(hlieu- < -g"'hieu -) 
Meaning: to spit 

Note: the /losen forms at least partly through dissimilation inyopresent *sp[i]u-id. 
Material: Old Indie sthfvat/ 'sp\t, speitfrom' (originally only, later vorwiegend in compound 
with ni{h)-, dahers- from 5-; 5/-i/dissimil. from sp-v, so that = Gothic speiwan), sthyOta- 
"gespuckt, gespien'; Avestan spama-^ saWva, mucus'; gr. nruu) "spucke', nruaAov, htueAov 
"saliva', nuri^u) (dissimil. from *nTUTi^u)) 'spucke, spritze' (nru:- from *pJu-\ compare with 
Inlautbehandlung the group snicpGuaSu) Theokr. 'despuo'; ijjuttei htuei Hes. with (pl=>-from 
cpG-); Latin spud, -ere, sputum ' spW., spucken', despuo 'spucke from, verschmahe'; Gothic 
speiwan. Old Icelandic spyja. Old English Old Saxon Old High German spTwan'sp\{\ Old 
Icelandic spyta'spW!, (in addition Old Icelandic schw. spotta, Danish spotte. Old Frisian 
spottia. Middle Low German spotten. Old High German spotton' mock '), East Frisian 
S/OJ/e/? 'spucken, sprijhen'. Middle Dutch holl. 5/Oi/i4/e/7 'spucken, spit'; Lithuanian spiauju, 
sp/aut/ 'spW, Old Church S\av'\c p/jujg, pljbvati 6s.\ 

Maybe alb. Geg pshtyj, Tosc peshtyj "sp'\\.\ shpetonj" escape, drip' : Old Indie /rs/Va//'spit' : 
gr. i|JUTT£i; common Old Indie -g"'h- > ks- : gr.- Illyrian - alb. -g"h- > -k"h- > -ps-. 

Armenian /'i//r"saliva', /'/r '5/75/77 'spucke, speie from' (/ kann, although from pt- 
deducible not dem gr. nr < ni gleiehgesetzt become), osset. t'u, npers. tuf, /^/7 'saliva' 
from an Old Indie (Lexikogr.) thutkara-, thuthOas Wiedergabe of Spucklautes 
vergleichbaren Lautgebarde; 

again etwas different Old Indie /rs/V5//(Dhatup.) 'spit, speitfrom', common Old Indie -gh- 
> -/r5- gr. oiaAov, Ionian aisAov 'saliva, slobber', Cypriot oTai (Cod. aiai < *aiFai, Bechtel 
Gr. Dial. I 412, or*aTaai?) nruaai (Cod. nrnaai). flacpioi Hes. 

References: WP. II 683, WH. II 580 f., Trautmann 276, Schwyzer Gr. Gr. 1 , 325, 752, 4. 
Page(s): 999-1000 

Root / lemma: sp(h)reig- 

Meaning: to abound 

Note: compare (s)p(h)ereg- 

Material: Gr. acppiyau) ' to be full of, to abound with, to be bursting with, to be bristling, 
=== fungus in KLN ===
7163:champignon,  n.,  fungus,  mushroom.  — F., formed, with  change  of  suffix,  fr.  OF.  champegnuel, fr.  VL.  *campdniolus,  ‘that  which  grows  in  the field’,  fr.  Late  L.  campaneus,  ‘pertaining  to  the fields’,  fr.  campus,  ‘field’.  See  camp, champion,  n.  —  ME.,  fr.  OF.  champion,  fr.  Late L.  campionem,  acc.  of  campid,  ‘fighter’,  lit.  ‘one who  takes  the  field’,  fr.  L.  campus,  ‘field’.  See camp  and  cp.  champaign.
15550:fungous,  adj.,  spongy.  —  L.  fungosus,  ‘spongy, fungous’,  fr.  fungus.  See  fungus  and  -ous. fungus,  n.,  i)  any  of  a  group  of  plants  including mushrooms,  molds,  mildews,  etc. ;  2)  (med.)  a spongy  morbid  growth.  —  L.,  ‘mushroom’,  fr. Att.  Gk.  ctpoYYo c,  corresponding  to  Gk.  ac.iiy-. Yos,  ‘sponge’.  For  the  change  of  Gk.  09  to /in Latin  cp.  L.  fides,  ‘gut  string;  lyre,  lute’  (if  it derives  fr.  Gk.  <j<pi8es,  ‘sausage’).  Cp.  sponge. Derivative:  fungus-y,  adj. funicle,  n.,  a  small  cord.  —  L.  funiculus,  dimin. of  funis,  ‘rope’,  which  prob.  stands  for  *dhu- nis  and  is  cogn.  with  Gk.  &co(juy5.  ‘tope,
36366:(med.)  —  Medical  L.,  formed  with  suff.  -itis  fr. Gk.  ajrovSuXcx;,  ‘vertebra’.  See  spondyl. spondylo-,  before  a  vowel  spondyl-,  combining form  meaning  ‘vertebra’.  —  Gk  ottovSuXo-,  fr. (77r6vSuXo?,  ‘vertebra’.  See  spondyl. sponge,  n.  —  ME.,  fr.  OF.  esponge  (F.  eponge), fr.  L.  spongia,  fr.  Gk.  aTtoyyia,  ‘sponge’  (rel. to  airoyvo^,  Att.  rccioyyo;,  of  s.m.),  which — together  with  Arm.  sung,  sunk,  ‘sponge,  cork tree,  pumice  stone’ — is  borrowed  from  an  un¬ known  source.  L.  fungus,  ‘mushroom,  fungus’, is  a  loan  word  fr.  Att.  a'joyyo-.  See  fungus  and cp.  spunk.
```


## [2026-09-14T02:29:47.648Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD spyeu ===\"; grep -n -i \"spyeu\\|sp(y)eu\\|spyēu\\|to spit\" AHD_watkins1985.txt | head -20\necho \"=== AHD spong ===\"; grep -n -i \"spong\\|sponge\" AHD_watkins1985.txt | head -10\necho \"=== IEC 1005 ===\"; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in range(515,525):\n    print('--- leaf',i,'---')\n    print(leaves[i][:300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:29:48.856Z] TOOL RESULT

```
=== AHD spyeu ===
981:ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
993:spyeu-. Also speu. To spew, spit. Expressive root. 1. Germanic *spitjan in Old English spittan, to spit:
995:spit!. 2. Germanic *speiw- in Old English spiwan, spio- wan, to spew: SPEW. 3. Germanic *spait- in Old English spatl, spittle: sPITTLE. 4. Germanic *spiit- in: a. Middle English spouten, to spout forth: spout; b. Dutch sputte- ren, to sputter, akin to the probable Low German source of SPUTTER. 5. Zero-grade form *spu- in Latin spuere, to spit: SPUTUM; CUSPIDOR. 6. Zero-grade form *(s)pyu- in Greek ptuein, to spit: HEMOPTYSIS, PTYALIN. [Pok. (s)p(hjieu- 999.] srebh-. To suck, absorb. Zero-grade form *srbh- in: a. Germanic *surp- in altered form in Dutch slurpen, to slurp, lap: SLURP; b. suffixed form *srbh-é- in Latin sorbére, to suck: ABSORB, ADSORB, RESORB. [Pok. srebh- 1001.] srenk-. To snore. O-grade form *sronk- in: a. Greek rhonkos, rhonkhos, a snoring: RHONCHUS; b. Greek rhunkhos, snout, bill, beak: RHYNCHOCEPHALIAN. [Pok. srenk- 1002.] sreu-. To flow. 1. Suffixed o-grade form *srou-mo- in Germanic *straumaz, stream, in: a. Old English stréam, stream: STREAM; b. Dutch stroom, stream: MAELSTROM. 2. Basic form *sreu- in: a. Greek rhein, to flow: RHEO-, -RRHEA; CATARRH, DIARRHEA, HEMORRHOID, RHYOLITE; b. suffixed form *sreu-mn in Greek rheuma, stream, humor of the body: RHEUM. 3. Suffixed zero-grade form *sru-dhmo- in Greek rhuthmos, measure, recurring mo- tion, rhythm: RHYME, RHYTHM. [Pok. sreu- 1003.]
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1595:HEM! kem-2 HEMATOCRIT krei- HEMERALOPIA amer- HEMI- sémi- HEMISTICH  steigh- HEMOPTYSIS spyeuU- HEMORRHOID sreu- HEMP kannabis
2139:PROVE per! PROVENANCE gWa- PROVENDER ghabh- PROVENIENCE gWa- PROVERB wer-& PROVIDE weid- PROVOKE wekw- PROVOST apo- PROW per! PROXIMATE per! PROXY cira PRUINOSE preus- PRUNE? ret- PRURIENT preus- PRURIGO preus- PRURITUS preus- PRY? ghend- PSALM pdl- PSALTERY pol- PSEPHOLOGY bhes-1 PSEUDEPIGRAPHA gerbh- PSEUDOMONAD _men-4 PSEUDONYM n0-men- PSILOMELANE bhes-!, mel-2 PSYCHE bhes-2 PSYCHEDELIC deiw- PSYCHIC bhes-2 PSYCHO- bhes-2 PSYLLA plou- -PTER pet- PTERIDOLOGY pet- PTEROCERCOID pet- PTERYGOID pet- PTISAN pelis-1 PTOMAINE pet- PTOSIS pet- PTYALIN spyeu- PUBERTY pubés PUBERULENT piibés PUBESCENT pubés PUBIC plibés PUBIS plbés PUBLIC populus PUCE plou- PUCKER beu-! PUDENCY (s)peud- PUDENDUM (s)peud- PUEBLO populus PUERILE pau- PUERPERAL pau- PUFF beu-!
2279:SPECIOUS spek- SPECTACLE spek- SPECTRUM spek- SPECULATE spek- SPECULUM spek- SPEECH spreg- SPEED spé-1 SPELL! spel-3 SPELL? spel-3 SPELT! spel-! SPERM! sper-4 SPEW spyeu- SPHENE spé-2 SPHENO- spé-2 SPICA spei- SPICA_ spei- SPICULUM spei- SPIDER (s)pen- SPIKE! spei- SPIKE? spei- SPILE spei- SPILL! spel-1 SPILL? spei- SPIN (s)pen- SPINDLE (s)pen- SPINE spei- SPINEL spei- SPINIFEX dhé-1 SPINNEY spei- SPIRACLE spirare SPIRE! spei- SPIRE? sper-2 SPIRIT spirare SPIT! spyeu- SPIT? spei- SPITTLE spyeu- SPITZ spel- SPLANCHNIC spelgh- SPLEEN spelgh- SPLENDID spel-2 SPLICE splei- SPLINT splei- SPLINTER splei- SPLIT splei- SPOIL spel-1 SPOKE! spei- SPONDEE spend- SPONSOR spend- SPONTANEOUS (s)pen- SPONTOON peuk- SPOON spé-2 SPOOR spere- SPORADIC sper-4 SPORE sper-4 SPORO- sper-4 SPORRAN bursa SPORT per-2 SPOUSE spend- SPOUT spyeu- SPRAG (s)preg- SPRAWL sper-4 SPREAD sper-4 SPREE ghend- SPRING spergh-
2281:SPRINGE spergh- SPRINKLE (8)preg- SPRIT sper-4 SPROUT sper-4 SPRY (s)preg- SPUME (S)poi-mo- SPUR spere- SPURGE peue- SPURN spere- SPURRY (s)preg- SPURT sper-4 SPUTNIK ksun, pent- SPUTTER spyeu- SPUTUM spyeu- SPY spek- SQUAD kWetwer- SQUALENE (8)kWal-o- SQUARE kWetwer- SQUASH2 kwét- SQUAT ag- SQUIRE skei- SQUIRREL ors-, skeoi- STABLE! sta- STABLE? sta- STACK steg- STACTE stag- STADDLE sta- STADHOLDER sta- STAFF! stebh- STAG stegh- STAGE sta- STAGGER steg- STAGNANT stag- STAIN teng-
=== AHD spong ===
874:Norwegian fogg, rank grass, probably akin to the Scandi- navian source of Middle English fog, fogge, aftermath grass: FoG?. 3. Extended variant form *pous- in Ger- manic *fausa- in Low German fussig, spongy: FUZZY. 4. Suffixed form *pu-tri- in Latin puter (stem putri-), rotten: PUTRESCENT, PUTRID; OLLA PODRIDA, (POT- POURRI), PUTREFY. 5. Suffixed form *puw-os- in: a. Lat- in pus, pus: PURULENT, PUS; SUPPURATE; b. Greek puon, puos, pus: PYO-. 6. Greek compound empuein, to suppu- rate (en-, in; see en): EMPYEMA. [Pok. 2. pii- 848.]
990:(s)poi-mo-. Foam. 1. Variant form *poimo- in Germanic *faimaz in Old English fam, foam: FOAM. 2. Variant form *spoimaé in Latin spiima, foam: SPUME. 3. Suffixed reduced form *poim-ik- in Latin pimex, pumice (from its spongelike appearance): POUNCE?, PUMICE. [Pok. (s)poimno- 1001.]
1057:swo-. Pronominal stem; so. Derivative of s(w)e-. 1. Ger- manic *swa- in: a. Old English swd, so: sol; b. Germanic compound *swa-lik-, “so like,” of the same kind (*/ik-, same; see lik-), in Old English swylc, such: sucH. 2. Ad- verbial form *swai in Latin si, if, in quasi (quam, as; see kWo- + si, if): NISI, QUASI. [In Pok. 2. seu- 882.] s(w)okwo-. Resin, juice. Variant form *sokvo- in Greek opos (< *hopos), juice: opruM. [Pok. s(wekvo-s 1044.] swombho-. Spongy. Germanic *swamba- in: a. Middle Low German sump, swamp: SUMP; b. Low German zwamp, swamp, akin to the Low German source of swamp. [Pok. suomb(hjo-s 1052.]
=== IEC 1005 ===
858
--- leaf 515 ---
ti, v. “flog” (pf: periau); Latv. peru, pert, id. (Z-gde in OCS prja, f. ‘quarrel’. Of indeterminate grade in Hitt. parh- mi, v. "drive pero, io (3) breed (Variant: por-) Lat. cf. puer-pera, adj. f. ‘in childbirth’; -pe- rium, n. ‘parturition’; cf. also jüni-perus, gs: 1, f. Cjuniper,, if fr. *jeuni
--- leaf 516 ---
erthu, inf. ‘strive’ perun-, peroun- (?). Cf. perquón- Hitt. perunas "rock mountain’; OCS cf. peru- nú, m. ‘thunderbolt’ perut, peruti (z-gde of per- and uet-, q.v.) “last year’. WP II, 31 Skt. parut, id.; Arm. heru, id.; Myc. & Gk. pérusi, id.; Alb. cf. par-vjét, adv. (“the year before last', fr. *
--- leaf 517 ---
Lat. pesna, f. ‘feather, wing’; Ir. (?) eathar, m. ('ship'. Cf. ‘pinnace’ for sense); (oblique form in) MIr. én, m. ‘bird’; OBr. cf. hataned, pl. (feathers', w. “false? h-) beside atan-oc, adj. ‘winged’; eterin, pl: atar, m. ‘bird’; Br. (oblique form) adan, pl. -éd, m. “a bird, owl or nightingale'?;
--- leaf 518 ---
: pari, prp. (at, over, toward’. (Variant of type *prei in OCS and com. Sl. pri-, Li. prie-). Cf. also Alb. pari, f. ‘nobility’: MIr. aire, s. ‘prow, temple of head, chief, noble’. Comp. in Lat. praeter ‘beside’; Olr. airther *eastern'; E farther & further. WP II, 33-4 poró “forth, before; therefore
--- leaf 519 ---
 pouont- Cypr. cf. pai “altogether, -ever; kasa-pai (queried: *also'); Cz. pevný, adj. ‘firm’; Pol. pewny, pewien, id.; Latv. cf. pa-puve, f. ‘fallow land" (Arm. havat, o-st. “faith” appears to be an Iranian LW) pi ‘on, upon’. Aphetic form of epi, q. v. Skt. pi, pi- (in pi-drbh, -dhà, -nah, etc.); O
--- leaf 520 ---
nger’; pykstü, pýkti, v. ‘be angry; LW in Ir. pioc, pioch, m. ‘droplet; jot; pore & in Alb. pikë ‘point, dot, source of Fr. pique, fr. a Lat. type *picca. A type pīkāið arises in Alb. pikoj, v. ‘drip’; OCz. pikati, inf. ‘urinate’ and in OCS pikanina, pikotyna, f. “urine? pikolos, à, is (pikl-) ‘tip,
--- leaf 521 ---
fig" beside pippalih, f. ‘capsicum, chilli’; pippalah ‘sacred figtree; nipple; pippalam, n. ‘berry, (The variants occur in the river-name Pimpala & Pippalàa); Sp. cf. pimpóllo ‘shoot; beau’; Port. pimpáo, id. beside pimpolho ‘bud’ (LW in E pimple); G Fimmel, Femmel, m. “male hop, male hemp’; Li. cf.
--- leaf 522 ---
, f. ‘chick’; pipizo, v. ‘cheep’; cf. oino-pipés, adj. ‘gasping for wine’; Lat. pipo, åre, v. ‘cheep’ beside ppo. ire, v. ^whim- per; Li. pypiü, pýpti, v. ‘cheep’. Doubtfully to W iâr, Br. jar, Cor. yar, f. Chen, qua *piporà) pis- “mess; messy Per. pih ‘tallow’; LG fies, adj. ‘nasty’; Ukr. cf. po-ps
--- leaf 523 ---
as, fpl. *pease-pud- ding” beside pite, f. id. (and 'dumpling); ON cf. (?) fita, f. ‘fat. Cf. Ir. ithir, f. ‘cornfield’ pit- (2) “drink, juice, liquor; drinking’. Cf. WP IL, 74 and next Skt. pitíh, £. ‘drink’; cf. also pitu-daru “a tree and its resin'; Lat. cf. pitu-ita, f. *discharge; tree-resin'; 
--- leaf 524 ---
-); OE flócan, sv. 7 ‘clap’; floc, n. "Tat, fish, flounder’; OS flokan, OFris. floka, sv. 7 ‘curse’; MHG vluochen, wv. id.; LG fláuken, id. (G fluchen); Du. vloeken, v. id.; vluok, m. ‘curse’ plag- (2) ‘sluggish, dull, lifeless’ Alb. i plogë, i plogët, adj. id.; Cz. cf. plahočit, inf. — se ‘toil’; G
```


## [2026-09-14T02:30:01.070Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sthiv\\|sthīv\\|ptuo\\|ptuō\\|ptú\\|pjeu\\|pieu\\|spieu\\|spjeu\" IEC.txt | head -20"
}
```


### [2026-09-14T02:30:01.126Z] TOOL RESULT

```
3214:dhubh- (?) (3) (dhubha-?) ‘heed’. Cf. tubhālo- (tubhá-) Hom. a-súphelos ('contemptuous' is ambig.); OE dybbian ‘pay heed'; Cz. dbát, Pol. dbać, id. (but OCz. tbáti points to tubhå-, q.v.)
5325:guóuà “beast, monster” Lat. bova, boa (1) “water-monster, boa’; Du. keu ‘pig’; Cz. cf. o-hava ‘beast’; R cf. plju- gàvyj beastly’; plju- fr. *spieu- 'spit"); Li. cf. guone ‘salamander’
8205:ksneuo (ksneumi) ‘pierce, stab, be sharp, be keen'. Cf. sneu- Skt. kspaumi ‘sharpen’; Gk. cf. ikshneümon (?) (Cichneumondly,, if for ix, gs ikós ‘grub’ + *ksneu- ‘pierce’); Lat. cf. nov-acula ‘razor’; OE sneowan ‘hasten’; cf. sneome: OS sniumo “quickly”; pp. in Skt. ksnutáh, Av. hu-xinuta-; o-gde in MHG snoede ‘contemptuous’; ON snauór ‘bare; impoverished’
13708:pstuio (pstiuio, psth-) ‘spit’. Cf. spuuo, ið. Onomat. WP II, 683 Skt. sthivami, pp: sthyütah, id.; Hind. cf. thuk, s. id.; Per. tuff, s. id.; Oss. tü, s. id.; Arm. t'uK, gs: tko, o-st. id.; t'Knem, v. id.; Gk. ptáo, v. id.; Alb. pshtyj, v. id.; Br. cf. tufa, v. id.
19213:tu- (radical “care, watch") in Gk. cf. a-sü-phelos (écontemptuous' or sim. but ambig. cf. dhubh- (3)); Lat. cf. as-tus, gs: -tüs, m. ‘craftiness’; as-tütus, adj. ‘crafty’ (fr. *ad-tu-); tueor, tueri, v. ‘watch’; OCz. tba, f. “heed”; assim. in Pol. dbaly, Ukr. dbalyj, adj. ‘concerned, careful; Cz. cf. ne-dbaly, adj. («careless': Gk. -süphelos). (NB. OE dybbian, v. “heed? points to a type dhubh-)
```


## [2026-09-14T02:30:02.978Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 leaf 626 (p.621) ===\"\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('n leaves',len(leaves))\nfor i in [625,626,627]:\n    print('=== leaf',i,'===')\n    print(leaves[i][:2500])\nEOF"
}
```


### [2026-09-14T02:30:04.116Z] TOOL RESULT

```
=== WLD Bd2 leaf 626 (p.621) ===
n leaves 725
=== leaf 625 ===
                                                                              ;            ;




                                               (s)teg-                                         621

bedeckt, verschlossen           ;
                                    kompakt,   fest,     dicht^'   (s.   wegen dieser Bed. auch
Hegii- „dick“), otehxixo^ „bedeckend, schiitzend^: lat. tego, -ere „decken,
bedecken“,      tectum        „Dach'‘   (= oxEHxog)^       tegiilum      „Decke, Dach, Hulled
teges, -etis „Decke, ilatte'*, tegula „Dachziegel“,                 toga „Toga'' (iiber lat. tu-
gurium s. Vf. LEWb.^ s. v.); umbr. teJitefim „tegimentum, tectorium^‘
   air. tech (neutraler -es-St., = gr. xeyog)^ acymr. tig^ ncymr. ty^ acorn, ti
„IIaus% abret. boti-tig „KubstalP (zum brit. i s. Pedersen IvG. I 99; PI.
acymr. te, ijcymr. tai)^ auch in air. teg-lach „Hausgenossenschaft‘', cymr.
teulu, acorn, teilu „Pamilie‘'; air. tigerne ,,(Haus)herr‘", cymr. teyrn „rex,
tyrannus'^,     abrit. Cato-tigerni^ gall. Thigernum castrtmi] air. -tuigiur ,^ich
decke“   =   ahd. decchiu (Formenbestand bei Pedersen KGr. II 655; iiber co-
nutghn „construo, architectoP' s. vielmehr u. dengh- „wohin reichen‘" und
dheigh- „Lehm kneten'‘); tuige „stramen‘‘, imthuge „Bedeckung, Beklei-
dung“, cymr. am-do „amiculum, invoJucrum^*, air. etacli (s, Pedersen KG. II
655) „Kleid% cymr. corn, to „Dach‘*, cymr, toi „tegere‘‘
   aisl. pehja ,,decken'', ags. peccan ^bedecken'*, ahd. decchen „decken'^ (Ite-

rativ Hoge^o    ^    air. tuigiur^ unter Verdrangung yon idg. Hego); aisl. pak^

ags. pcec, ahd. dah „Dach‘‘; aisl. pekja „Dach, ahd. deccJii „Decke, Dach^^;
ags. pecen^ as. fhecina ds. (im Germ, also nur Formen mit der Abtonung
idg.             Falk-Torp u.         == Fick III^ 479 stellen hierher auch aisl.
staka, stakka f. „FeH“, norw, taka ,jSchweinshaut^^ aus anord. ^paka^ aisl.
stakkr „Wams“, afries. sfdk .,eine Art ManteP; s. S. 617 oben);
   lit. stiegiii, stiegii .,ein Dach eindecken^' (van AVijk IF. 34, 370 sagt, da8

der Yokalismus dieses Verbums nach Buga Aist. St. I 62 so anzusetzen
sei), apr. steege ,.ScheueF', lit. stiegtojas „Dachdecker“, stogas == apr. stogis

„Dach“.
   Im Slav, keine verlafilichen Entsprechungen; abg. stog^ „Heuschober“
(*„mit einem Wetterschutz iiberdachter Schober“?) scheint eher „*um eine
Stange als Mittelstiitze gehauft‘‘ zu sein (s. steg- jjStange“): abg. ostegz
,,Kleid“, osfe£b .,chlamys“, nasiegny „Sandale“ sind nicht zu trennen von abg.
ostegnqti „(
=== leaf 626 ===
                                  ;




622                                                      (s)teg        stegh-



2. (8)teg- „Stange, Pfahl, Stock, Kniittel,                               Balken“; gegen Vermittlung mit
           steig-       „stechen“ in Bed. und                 Form s. d. am Schlusse.
     Arm, fakn^ gen. faJcan ^Kniittel, Schlagel, Keule“, faJcaiak, fakatat „capi-
tello,      architraYe*^
     lat.   tignum „Bauholz, Balken“ (Liden IF. 18, 498 ff. m. Lit., Vf. LEWb.^
s,   V.;    wenn arm, a im gen. takan usw, aus e ass. ist, kann                               voile Grleich-
heit mit tignum bestehn).
     Aisl.                „Pfahl, Stange“              = ahd.             „Knuttel, Pfahl, Stecken, Pflock“
(das aber zugleicb auch das m. Gregenstuck zu aisl. stika „Stecken“, s. "^steig-
„stechen“)  aschwed. staki „Stange, SpieB'', ags. staca ds., mnd. stake ds.
                    ;


                   s. aber u. steig- „stechen‘*), ahd. stack „Spiefihirsch (mit
(liber ahd. stahhula
noch ungegabelter Geweilistange)“;
  dan. stak „Achel, Granne'*; Denominativ aisl. stjaka „mit einer Stange
stoBen'*, staka „stoBen, anstoBen, straucheln'^, mnd. staken „Pallisaden setzen,
mit einer Stange stofien oder schlagen^*; got. Jileipra-stakeins „Laubhutten-
fest^ eig. „Aufschlagen von Zelten“;
   vom Bilde der Stange genommen ist (iiber afries. ofries. stak „steif, auf-
recht, fest“ s. S. 616), norw. mdartl. staka, stjaka „steif gehn, stolpern”,
nd. stake7'n „steif gehn, stolpern“,
  Yermutlich (doch s. u. stak- „stehn'‘) aisl. stakkr „Schober, kegelformiger
Haufe‘^ (wohl „um eine Stange als Mittelstiitze gebauft“, vgl. ;) mnd. stak
jjschrager Damm aus Pfahlen und Reisig“ (: abg. stog^ „Schober“, Miklo-
sich EWb. 323 f., Falk-Torp u. stak I).
  Lit. stagaras, stegerys „durrer langer Stengel^, lett. stegay stegs „eine
lange Stange, langer Stock, Spie6“.
  Russ, mdartl. stozarz „Stange“, sloven, stezja, stozje ,.Schoberstock“, sioz-
dnje „Turpfosten“, stoMr ds., skr. stozer „Baum auf der Dreschtenne“, osorb.
scezor „Mast“, slov. stoziti se „sicli baumen“, abg. stogz „Heuschober“ (kaum
zu steg „decken^';                     s.       die slav. Sippe auch bei Miklosich EWb. 323 f.); stegz
„Fahne“             (?   s.   u. steg- ,,decken“).                S.   Liden aaO., Falk-Torp u. stage; die
bsl.    Worte konnen auch zu                           ^stegk- „stechen, Stange“ gehoren,          s.   d.


(s)teg-, nas. (s)toiig-, (s)t 9 ng- ^ranzig, lib
=== leaf 627 ===
                                                steb       stemp-                          623

     Nasaliert: mit zweisilbiger Wzform gr. otovv^, -v%og .,Spitze, Xante (eines
Steines, eines Felsens), Spitze der Nagel, der Krallen; Schere“, Gr6vvx^<^*
xa €ig o^v ATjyovra, xal ra axga rcov ovv^cov Hes., oxovv^i* xegaot Hes.
(das -v- ist gewiU ein E-eduktionsvokal, etwa o, nicht nach Siitterlin IF.
25, 70 idg. ii)\ oxd^vg, -vog (auch dora^vg) „Alire“ («                 = ^);
     aisl. stinga, staklc,            ags. stingan „stecken“; got. usstagg         stick aus!“
(nicht in iisstigg zu andern, sondern Typus hlandan, anapraggan,                     Bgm. IF.
33, 284 f.) ; ahd. stanga, aisl. stqng „Stock, Pfahl, Stange“, ags. ste^ig (^stangi-)
ds., nl. steng {stangid[ 7i\-) ds., ahd. stengil „Stengel“; mhd. stimge „Stacher',
stungen „stechen'^
   Vielleicht hieher als „steif wie ein Stock, sich versteifen, steramen, steif
werden“ nnd mit der Intonation einer set-Basis {: orovv^) lit. steng-nij -ti
„sich anstrengen‘‘, refi. „8ich widersetzen", stangiis „widerspenstig“ und
(wenn nicht in Beziehung zu stai- „verdichten“ s, d.), stmgstu, sfingaii,
stlngti „gerinnen, steif, dick werden“, lett, stingstu, stingt „starr, steif, kom-
pakt werden“, stingrs „stramm, starr, zshaltend, gespannt, steif“.
   Vgl. Fick I^ 569, III ^ 480 f., Falk-Torp u. stegg, stang, Ahnlich ^steg-
„Stange“, s. d.


steb- und steb- stob-, nasaliert stemb-;
                          :



stebh- und stebh- stobh-, nasaliert stembh-;
                                  :



step- (auch step-?), nasaliert stemp-.
  Bedeutungsumfang: ,.Pfosten, Pfeiler, Slander, Stamm, Baumstumpf (auch
Busch, Biischel, wohl zunachst von den         um einen Baumstumpf wuchern-
den    W
       urzeltrieben Strunk, Stengel), Stab, z. T. auch (aufragender) Stein^';
                              ;



verbal: „stutzen, versteifen, feststellen, anhalten'^ fauch „hemmen“, was z. T.
auch aus ,,entgegenstemmen“ oder „entgegentreten“ oder „Prugel unter
die PiiBe        werfen“       sein kann)
                                  entwickelt„mit dem FuBe aufstampfen,
                                                                ;


treten      (Tritt,  FuBspur), starapfen (z. T. auch mit einem Pfosten,
                      Stufe,
StoBel); beschimpfen (teils aus mit den Fiifien treten, teils aus steif und
herausfordernd dastehn; aus letzterem wohl hauptsachlich die Bed. prahlen,
groBsprechen), staunen (aus erstarrt dastehen
```


## [2026-09-14T02:30:12.722Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"spongia\\|opoyyog\\|fungus\\|Schwamm\" incoming/WLD/WLD_Bd2_pages.txt | head -30"
}
```


### [2026-09-14T02:30:12.777Z] TOOL RESULT

```
7585:bedly pi. „Schwammchen im Munde“, poln. bedta ,,Schwamm“ (s. Berneker
35550:m. „Schwamm“; daneben germ, "^sivampu- (idg. suombu-; mit h aus hh
35552:Ball (nach der Gestalt) mnd. svamp^ -pes „Schwamm, Pilz‘‘ und got. swamm
35553:acc. „(Wasch-)Schwamm“, ags. swamm m. „Pilz“, mnd. ahd. svam^ -mmes
35554:„Schwamm; Pilz“; von schwammigem Boden engl. swamp jjSumpf*', westfill,
35570:Denominativ eines               „Schwamm“; woher auch a statt o?) bleibt fern.
45222:  Gr. oTioYYog, att. auch ocpoyyog „Schwamm; Driise^’, woraus lat. fungus
45236:Lhlenbeck IF. 13, 215, Vf. LEWb.^ s. v.); arm. sunk, sung „Schwamm,
45253:abg. g(^a ^Schwamm^ in Rechnung gesetzt werden, aber mit TJnrecht,
45258:(ahd. swamp^ -bes „Schwamm'‘); dock hatte die Annahme von germ, siv-
45261:ocpoyyog, fungus^               sivamba- etwa unter "^'sghuongos zu vermitteln suchen.
```


## [2026-09-14T02:30:14.192Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD band3 index spong ===\"; grep -n -i \"spongia\\|spongos\\|fungus\" WLD_band3.txt | head -20\necho \"=== POK_full spong ===\"; grep -n -i \"spong\\|fungus\" POK_full.txt | head -20"
}
```


### [2026-09-14T02:30:14.279Z] TOOL RESULT

```
=== WLD band3 index spong ===
=== POK_full spong ===
7507:again alb. es/7/re "fungus' : Latin esca "food, victuals, esp. as bait'. Prothetic v- added to 
10081:saprophytic fungus of the order Agaricales having an umbrella-lil<e cap with gills on the 
20106:skillet ' seems to be a genuine Germanic word (*d/j.. laz), however, this has sponged in 
30601:Beefsteak fungus. Oak-tongue (a type of mushroom, species of mushroom '), serb. gljiva " 
30602:type of mushroom, fungus '; 
32000:Old Church Slavic ggba' sponge, fungus ', Serbo-Croatian guba' sponge, leprosy ', 
32001:sloven, ggba' sponge, fungus ', gobecm. 'muzzle', acech. huba' sponge ', newer 
32002:"muzzle, lip', russ. guba^ tree-fungus '; besides ^i/i&a'lip'; in Slavic lies intonation change 
60365:Maybe alb. myku^ fungus ' a Latin loanword. 
60379:fungus '; 
84465:Meaning: porous, spongy 
84469:swamp, -besm. ' sponge '; besides Germanic *swampu- (Indo Germanic *suombu-) and 
84471:*swamma- in Old Icelandic sugppr^ sponge; ball (after the shape)'. Middle Low German 
84473:swamp, -pes^ sponge, fungus ' and Gothic swamm f\Vk. "(Wasch-) sponge ', Old English 
84477:swammxw. ' fungus ', Middle Low German svam, -mmes' sponge; fungus '; from 
84480:sumprswamp, marsh' = Old Icelandic soppr^ ball ', Norwegian also " fungus '.
```


## [2026-09-14T02:30:18.047Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'oTioYYog' in l or 'ocpoyyog' in l:\n        print('leaf',i,'-> printed p',i-5)\n        print(l[:2000])\n        break\nEOF"
}
```


### [2026-09-14T02:30:19.170Z] TOOL RESULT

```
leaf 685 -> printed p 680
                                                                                                 ;




                                     (slptqo-    — spongo-                                    681


(s)plqo- „Specht     u. a.   grower e Voger*.
   Ai. pika-h ,,der indische Kuckuck^';                 lat.    pica „Elster“, picus „Specht“;
umbr. pdco „picuin'‘        {ei Scbriftausdruck          fiir   ?, v. Planta I 107); mit anl. s-

ahd. speh^ speht^   aisl.    sp^tr   (fiir   "^spetr)   „Specht“.      Z. B. Fickl^ 148, 481,
Vf. LEWb,^ s. V. ; apr. picle „Kraminetsvogel“,                    Trautmann Apr. 398,
   Man sucht (s. Lit. bei Suolahti Vogeln. 28f,) Wzankniipfung entweder
unter einer Gdbed. „bunf‘ an gr. Tioixikog usw. (s. peig-^ peih- „farbeln“,
wozu apr. picle im Gutt. nicht unmittelbar stimmen wiirde) oder (wegen
des ags. e zu beanstanden) an ags. specca „Fleck'\ oder an lat. pix „Pech‘'
(Hirt IP. 1, 478, nicht einleuchtend); oder an russ. pikat'b „piepsen“ usw.
(s. Iljinskij KZ. 43, 179 und die Schallwz. plp-^ p1-)^ was wegen der An-

wendung auf groBere Vogel, die gerade nicht durch Pieplaute auffallen,
und wegen des anl. germ, s- Bedenken unterliegt; die germ. Worte ab-
zuriicken und zu spei- „spitz'', dt. Speichernagel zu stellen, vom besonders
kraftigen Schnabel des Spechtes, was Falk-Torp u. speite erwagen, leuchtet
aber auch nicht ein, da die Bedeutungsgleichung picus Specht wohl das           :



verlaBlichste an den obigen Zusammenstellungen                       ist,   gleichviel, auf welche
Gdbed. man raten mag ai piha-h, apr. picle konnten immerhin (wenn
                               ;


auch mir nicht wahrscheinlich) abgeriickt werden und Schallworte im Sinne
lljinskis (und Trautmanns) sein. Solite die Bedeutungsgleichheit zwischen
picus und Specht tatsachlich Zufall sein, bliebe Specht auch mit spoken
verkniipfbar.

(s)poiiiino-, -a   „Schaum, Gischt“.
   M.phena-li „Schaum, Feim“; lat. spuma „Schaum, Gischt“, pumex ,,Bims-
stein“ (v
```


## [2026-09-14T02:30:24.337Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nl=leaves[685]\ni=l.find('spongo-',500)\nprint(l[2000:5200])\nEOF"
}
```


### [2026-09-14T02:30:25.425Z] TOOL RESULT

```
on seiner schaumartig porosen Beschafifenheit; s. Vf. LEWb.^ m. Lit.
   Ahd. feim^ ags. fam „Feim, Schaum“; lit. spdine „Schaumstreifen auf
bewegter See“, apr. spoayno „Schaum‘*, abg. pena (russ.            skr. ^jem)
,,Schaum“. Pick KZ. 19, 78; iiber m:n     J. Schmidt Krit. 107 (auch Peder-
sen IF. 5, 80, Charpentier KZ. 40, 464 a. Wegen der lit. und slav. Into-
nation setzt Persson Beitr. 690 Langdiphthong -oi- an, doch kann die Into-
nation durch den Schwund des m vor n bewirkt sein.
   Gegen die versuchte weitere Verkniipfung mit gr. omkogy mragog usw.
s. u. ^spot- „fettig feuchtes“.    —
                                Unannehmbar stellt Holthausen AfneuereSpr.
121,294 fiir lat. spuma^ piimex Yerh, mit mhd. fum .,Schaum'‘ (s. u. 2>w-
„faulen“) zur Wahl.

spongo- „schwammiges, poroses'^
  Gr. oTioYYog, att. auch ocpoyyog „Schwamm; Driise^’, woraus lat. fungus
„Erdschwamm, Pilz** (trotz Pedersen KZ. 40, 209, Persson Beitr. 420 f. Anm. 1
fur Entlehnung beweist zwar nicht lat. w, wohl aber das dem Lw. fides
aus ocfibeg analoge Anlautverhaltnis denn einer Vermittlung unter idg.
                                                  ;


zlk- hh- widerspricht das folgende arm. Wort, der unter idg. sph- ph- das
       :
                                                                                         :


lat.Wort, denn f aus idg. ph- steht nicht fest und bes. ist die Annahme
einer 5-losen Doppelform *phongos nur ein Verlegenheitsausweg; s. auch
Lhlenbeck IF. 13, 215, Vf. LEWb.^ s. v.); arm. sunk, sung „Schwamm,
Korkbaum, Bimsstein‘‘ (Bugge KZ. 32, 64, Pedersen KZ. 38, 200, s. auch
39, 422; trotz Scheftelowitz BB. 28, 283);
```


## [2026-09-14T02:30:31.173Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[685][5200:7000])\nprint(\"=====LEAF686=====\")\nprint(leaves[686][:1200])\nEOF"
}
```


### [2026-09-14T02:30:32.304Z] TOOL RESULT

```
=====LEAF686=====
682                                  spingo-, picgo-   —   (s)pot-, (8)p9t-



     aber auch engl. spunk „Feuerschwamni, Zander, faules Holz“ (Prellwitz^
s.   Y.)wohl als „leuchtend, phosphoreszierend zu         .,glanzen“.

  Kaum hierher alit. spanguoge^^ lit. spanguoU „Moosbeere^' („schwaininig“ ?
Oder „auf schwammigem Moosboden wachsend“?), lett. spengals „Sand-
beere“, spanga „Blase an Handen oder Fiifien^ (Prellwitz aaO.).
    Die Yersuche, spongo- mit suombho-s j^schwammig, poros“ zu vermitteln,
yerdienen kein Yertrauen: Pedersen Materialy i prace 1, 165 ff. (wo auch
lit. gumbos „Erh6hung, Knorren, Gewachs an einem organischen Korper“,

abg. g(^a ^Schwamm^ in Rechnung gesetzt werden, aber mit TJnrecht,
s. Bruckner KZ. 42, 332, Persson Beiti\ 189 f. Anm. und u. geiibh- „biegen“

und gem- ,.greifen“) konstruiert ein idg. sphuongo-, woraus durch Umstel-
lung und Erweichung von ph bin ter I^asal zu bJi sguombho-^ germ, swmnba-
(ahd. swamp^ -bes „Schwamm'‘); dock hatte die Annahme von germ, siv-
aus idg. sgu- eben nur an slav. gqba einen scheinbaren Anhalt. Das arm.
Wort lassen          unberiicksichtigt Luft IvZ. 36, 147                   und Kluge G1   2, 55,   die
ocpoyyog, f
```


## [2026-09-14T02:30:44.749Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 اسفنج ===\"; grep -n \"اسفنج\" BQT_v1_pages.txt | head -10\necho \"=== BQT v1 تف ===\"; grep -n \"^\\s*تف\\b\\|تف (\" BQT_v1_pages.txt | head -10\necho \"=== BQT v2 سپنج ===\"; grep -n \"سپنج\" BQT_v2_pages.txt | head -10\necho \"=== BQT v3 شپش ===\"; grep -n \"شپش\" incoming/BQT/BQT_v3_pages.txt | head -10"
}
```


### [2026-09-14T02:30:44.911Z] TOOL RESULT

```
=== BQT v1 اسفنج ===
9613:بمعنی ابی‌کپن است که اسفنج الب باشد ۴ .
9626:واسفنج الیسر حمانت ۴ .
9635:۴ . رك : اسفنج . ۴ - آورنجن , خلخال . ٩9‏ رضا نمودن با اشارت
12140:اسفنج * - بکس‌اولوسکون انی وفتح
=== BQT v1 تف ===
327:تفاوت لهجهدارد. چنانکه‌تفاوت لپجه میان پارسی باستان واوستایی هم‌موجود
413:تفسیر پپلوی وسپرد . تفسیر پپلوی وندیداد ؛ تفر پپلوی برخی از یشتبا
417:تفسیر پپلوی اوستا نا گزیر از روز گاراشکانیان آغاز شده . اماآنجه
1438:تفاوت لهجه‌های خر اسان و ماوراء النهر
1672:تفت ِ« - دساتسر هه
1744:تفر آن میآید آنچنان که امروزه میدانیم انبیاء سلف چه گفتند. اگر اين
1745:تفید نبود نميدانستیم «کایستنی کارستنی هارستنی وارستنی شالستنی> یعنی
2179:تفاسیر بوده باشد که حاح خلیفه آورده است. ناصر خسرو در سفر نام خود
6170:تفن
7168:تفصیلاتی که لو ند گان عرب در یاب این کیاه آورده اند «خحر باتخاب بن 06( و
=== BQT v2 سپنج ===
21963:‫که‌آن مانند سپنج که خائة علفی‌است بقا وتباتی‬                         ‫دیده گه = بففتحاکرافسی بورزن‬
32932:                             ‫از سال شمی با‬                   ‫استماره سرای سپنج خوانند ‪ - ۴‬وبمعتی‌چرا گاه‬
32954:           ‫‪ ۲‬تاراج آن سبزه پی کرد گم ‪:‬‬                                  ‫‪ - ۴‬سپنج ‪-‬توران پبکانه سم‬
=== BQT v3 شپش ===
2790:شپش
2861:‏ولدیداد دوکونه شپش ‎al‏ شده : یکی ‎SIT‏ درانبارگندم افتد و دیگر ‎Sle SGT‏ پارچه را تیاه
2863:و دومین را ‎yea‏ جامه ,دبوچك‌جامه , کرم‌جامه کوبند «فاب+س ۱۹۹ اما شپش درفارسی‌بجالور کی
14746:جانوری است از کيك و شپش بزرکتر ودرمیان
24437:لام » شپش ‎Pas Sl,‏ ازخواس وی آتت که
37302:ایثها چسبد و مانند شپش خون خورد و بعربی
50626:‎did‏ > بنتح اول وتالث » بمعنی‌شپشه(۱)
```


## [2026-09-14T02:30:50.775Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='incoming/BQT/BQT_v3_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\n# find line numbers -> leaf\nimport re\nleaves=t.split('\\f')\noff=0\nfor i,l in enumerate(leaves):\n    if 'شپش' in l and 'ولدیداد' in l or ('شپش' in l and i<60):\n        tag=re.search(r'\\[pdf page (\\d+)\\]',l)\n        print('leaf',i,'tag',tag.group(1) if tag else None)\n        print(l[:3000])\n        print('-----')\n        if i>5: break\nEOF"
}
```


### [2026-09-14T02:30:51.872Z] TOOL RESULT

```
leaf 39 tag 40
[pdf page 40]
۱۲۸

و سقوطر جزیرهایست ‎Chap‏ بسواحل یمن ۱ -
و ام مسجونی هم هست که آنرا در شب خورند
وخوابند ۴ .
شبیاز ه ۴ ‎pe‏ وزن ‎let‏ » بمعنی
‎ont‏ باشد که مرغ عیسی کوبتدش ۴ .
شبیخون - بسمتی‌تبخون 6 است.وآن

تخت بر دن‌باشدبر سرد شمن چنا که غاف لو بیخبر باشد.

شپش

شییم = پر وژن لدم » ‎om en‏
‎ash‏ .

hes ‏«بروزن کمینه , بسمنی‎ ۱ daa

است که هرچیزشب ‎oul‏ باشد ازآب ونان‌وطعام
و میوه و ‎OT Seal‏ - و شب‌پره را هم گفته اند
که مرغ عیسی باشد ۷ - و صمغ‌درخت‌صنویررا
لیز گویند .

‎ol‏ سوم

‏در شین نقطه داربا بای فارسی‌مشتمل بر بیست و ‎EL‏ لفت

‏شب ه بنتح اول و سکون ‎gt‏ بمعنی
چهنده وخیز کننده باشد ۸ - و بمعنی زود حم
آمده است که عربان عجل گویند.

‎۲

‏شیاشاب ‎S‏ - با ‎yt‏ وشین نقطه‌دار(۱)
بالف کشید» و ببای فارسی زده » آواز و صدای
‎OK‏ تیر باشد که پی در پی در جابی بخورد.

‎teas ys ۱۰ is

‏شبتاك یک اول یر وزن‌خشتك.

‏)4( چك: - ‎ales‏ دار .

‏۱ - رك: سقوطر ۳

‏بمعنی لکد زدن ‎ash‏ خواء اسان بزند و خواه
حیوانات دیگر .

‏شیر ‎SY‏ = بنتح‌اول والی مشدد وسکون

‏رای بی‌نقطه » بلفت سربانی بممنی خوب ‎Cy‏
‏است وبعربی حس نگویند.

‎So ۳ on‏ اول ونالی + جانوری
است ممروف. کوبند ااکر ‎tet‏ را ازسربگیرد

‏۴ - پهلوی 8122018۳ (شربت قند .شیره) «ناوادباه۱5*.

‏۴ از : شب ۳ ‎Gh‏ (بازیدن) (-» ‎tps)‏ سبت وانصاف) قس : شبینه .
۴ - شب بازه , مرغك شب ‎dp‏ است .فرالاوی کوید :

‏تو شب آبی نهان بوی همه روز

‏9 رك: شبخون +

‏همچئانی بفین که شب بازه .» ‎MAYA oD cal‏
۱ - از : شب بنه (دبت) .

‏۲ ره : شب بازه .

‎. 456 ‏«واژه نامه‎ (Cds. cue ‏(قدم‎ Shap ‏-طبری‎ A

‎= (p0) lige oye ‏اسم‎ - ٩

‏۱ - رك: شپیر .

‏شپ شپ .

‎Ve‏ شب‌تك‌ورك : شپ.

‎spish.t,! - ۳‏ » پهلوی نیز ‎Spish‏ دربند۳ فر گرد ۱۷

‏ولدیداد دوکونه شپش ‎al‏ شده : یکی ‎SIT‏ درانبارگندم افتد و دیگر ‎Sle SGT‏ پارچه را تیاه
کند.شتین را درفارسی - چنانکه زمخشری در مقدمة الادب لوشته - شید کندم» ‎Bye‏ کندم
و دومین را ‎yea‏ جامه ,دبوچك‌جامه , کرم‌جامه کوبند «فاب+س ۱۹۹ اما شپش درفارسی‌بجالور کی
اطلاق شر د که دربدن مردم چر کین ‎gous‏ جالوران پدیدآبد وازخون تغذیه کند.قمل.شهمیرزادی
‎sabaj JOS . , ۰6‏ . خواداری ‎Kap GUL « espizh‏ کلپایگان ‎Cty‏ ؛ تهرانی
‎CSI] sb . Shipish‏ > واژ,تانه ۲۳

-----
```


## [2026-09-14T02:31:06.704Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef leaves(p): return open(p,encoding='utf-8',errors='replace').read().split('\\f')\ndef show(p, needle, want=None, maxn=4, chars=2500):\n    ls=leaves(p); n=0\n    for i,l in enumerate(ls):\n        if needle in l:\n            tag=re.search(r'\\[pdf page (\\d+)\\]',l)\n            pg=int(tag.group(1)) if tag else None\n            if want and pg and abs(pg-want)>6: continue\n            print('### file',p,'leaf',i,'pdfpage',pg)\n            print(l[:chars]); print('---')\n            n+=1\n            if n>=maxn: break\nprint(\"======= BQT v2 سپنج (want leaf ~547) =======\")\nshow('BQT_v2_pages.txt','سپنج',maxn=3,chars=1800)\nEOF"
}
```


### [2026-09-14T02:31:07.880Z] TOOL RESULT

```
======= BQT v2 سپنج (want leaf ~547) =======
### file BQT_v2_pages.txt leaf 371 pdfpage None
 ‫در ند‬                                                                                                      ‫‪۱۱‬‬
‫ذیر ننگ س بنتح اول و تایقرشت‬                                         ‫ګلی امت که آنراکاو‬
                                                                                      ‫دبد نگاو =‬
‫وسکون نون وکاف فارسی ک»نایه ازدلبا است که‬                           ‫چشم گوبند ‪ -‬ولوعی از سلاح و جامه باشد که‬
                               ‫عالم سفلی باشد ‪.‬‬                     ‫پوشند ‪ -‬و نام لوعی از انگوز هم‬            ‫ردورزجنگه‬
                                                                    ‫‪ -‬وستارژ دبران را نگیوزیند » واو یکی‬            ‫حت‬
 ‫دیرر ند سور = بفتح اول و کسر‬
‫نقطه » بمعنی دبرتنگه است که‬         ‫‪۳‬‬        ‫هر دو رای‬                ‫از منازل قمراست و بمریی عین‌الئور خوانند ‪.‬‬
               ‫کنابه دابزنا وعالم سقلی باشد ‪.‬‬                        ‫دید گاه = باکاف فارسی‌بروزن نیمه‬
 ‫دیردی ‪ = ۲‬بکر اول و زای هوزء‬                                                          ‫جها»ی نشستن دیده‌بان باشد ‪.‬‬
                                                                                                                 ‫را‬
 ‫بمعمی بسیاریمان وزلد کالی‌کن ‪ -‬ونام روزییست‬                         ‫دیده کنان د بنم کاف و دون بالف‬
                ‫وهفتم است ازماههای ملکی ‪.‬‬                           ‫کشیده وبنون زده " کذابه ازنگاه‪.‬كردن و تأمل‬
                                                                                                ‫لمودن درکاری باشد ‪.‬‬
‫= کنابه ازدتیااست زیرا‬      ‫دار سیتحی‬
‫که‌آن مانند سپنج که خائة علفی‌است بقا وتباتی‬                         ‫دیده گه = بففتحاکرافسی بورزن‬
                                                                    ‫نیمه ره » مخفف دبده گاه است که جلی نشستن‬
                
---
### file BQT_v2_pages.txt leaf 552 pdfpage None
   ‫‪¬ 40‬‬   ‫تس‬
                                                                                                                   ‫سیٍکاد‬

 ‫وآن‬
   ‫است »‬         ‫رلوف‬
                    ‫سينك = بمکرعاو‬                            ‫سیکاه ‪ » ۱‬بکر اول بر وزن افتاد‪.‬‬
‫تخمی باشد که بجهت چشم زخم سوزند ‏ ‪ -‬ونام‬                      ‫بمعتی چکاد است که میان سر وبالای پیشالی‌وسر‬
 ‫کوهی همهت ‪ ۷‬و بعربی کوه را جبل گویند‬                                                           ‫کوه وقلهُ کوه باشد ‪.‬‬
                             ‫‪. ۸‬‬   ‫وسه صیحت‬            ‫‪-‬‬      ‫نسل = بفتح اول وثالی بروزن اجل» سم‬
 ‫سپندار = بکر اول بورژن شکم‌دار‪.‬‬                                                          ‫روایند‪.‬‬
                                                                                                ‫شتر ‪ -‬و ناخن فیل گ‬
 ‫بمعنی‌شمم باشد که مسشوق پرواده است ‪٩‬‏ ونام‬                   ‫سینج ‪ = ۴‬پروزن شکنج ‪ .‬بمعنی‌مهمان‬
 ‫رفتاحن ‪ °‬ومخفف اسیندار هم هست‌وآن‬        ‫گ‬                   ‫باشد ‪ -‬و بمعنی عاریت هم گفته‌اند ‪ -‬و خاله‌ای‬
           ‫بودن‌لیر اعظم‌باشد دربرج‌حوت ‪. ۱‬‬                   ‫باشد که مازرعان ودشت‌بانان درسر غلهزار وفالیز‬
                                                             ‫و امثال آن از چوب و علف سازند ‪ -‬وارام گاه‬
 ‫سیندار هف ‪ ۴‬بم میموسکون‌ذال‬
 ‫لقطه‌دار » بمعنی اسقندارمن است که مامدوازدهم‬
                                                               ‫عاریتی را نگیوزبند ‪ -‬وچون دنیا را بقایی‌ینت‬
                                                               ‫رحکم مهمان خان عاربتی دارد آنرا نبیطزریق‬
   ‫بزای‬
      ‫حم ا‬
         ‫انج‬
           ‫مز پ‬
              ‫رو‬        ‫‪-‬م‬
                         ‫ها‬‫وشد‬
                             ‫از سال شمی با‬                   ‫استماره سرای سپنج 
---
```


## [2026-09-14T02:31:13.228Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[552][1500:6000])\nEOF"
}
```


### [2026-09-14T02:31:14.204Z] TOOL RESULT

```
                                                   ‫رحکم مهمان خان عاربتی دارد آنرا نبیطزریق‬
   ‫بزای‬
      ‫حم ا‬
         ‫انج‬
           ‫مز پ‬
              ‫رو‬        ‫‪-‬م‬
                         ‫ها‬‫وشد‬
                             ‫از سال شمی با‬                   ‫استماره سرای سپنج خوانند ‪ - ۴‬وبمعتی‌چرا گاه‬
 ‫شمسی هم‌هست ‪ .‬این روز را فارسیان بنابر قاعدة‬                 ‫که درآن آب و علف بار‬                      ‫جالوران هم هت‬
 ‫کلیه کهپیش ابشان معمول است که چون امامه‬                       ‫باشد ‪ - ۴‬و پانزده را نگیوزیند چه پاتزده سه‬
 ‫با تام روز موافقآید عید کننده درین روزجشن‬                                                                ‫يننےج است ‪. ۴‬‬
 ‫سازند و عبد لمایند ‪ .‬یك است رخت بوشیدن‬
                                                              ‫سینحاب د بکر اول وفتح‌نالی‌وسکون‬
 ‫و درخت شاندن در این روز باعتقاد ایشان ‪ -‬و‬                    ‫ثالث و جیم بالف کشیده و بای ‪.‬بجد زده ‪ .‬نام‬
 ‫نمعنی زمین‌هم گفته‌اند ‪ -‬و نام فرشته‌ای‌هم‌هت‬
                                                              ‫ولاش است که کاموس کذانی که رستم اورا کشت‬
‫مکل زمین ودرختها وجنگلپا است ومصالح‬
                                  ‫که و‬                         ‫ضابط آن ولابت بود ‪ » 6‬و باین معنی بحذف‬
                          ‫ئن ناء بجع سل وان‬                                           ‫حرف انی هم بنظر | مده است ‪:‬‬


   ‫لبك شبه بود ‪۰‬‬
               ‫ن«سزپنج‬
                     ‫م‪-‬‬‫‪۴‬‬                           ‫‪5‬‬   ‫‪ ۳‬سبکاد‬   ‫ورك‬    ‫‪۳‬‬   ‫ھ‪.‬م‪(.‬‬    ‫«چکاد»‪(.‬‬   ‫ظ ‪ ۰‬عمصحف‬      ‫=‬   ‫‪۱‬‬


                                                                                          ‫فردوسی (طوسی) گوید ‪:‬‬
               ‫سی چون تو میرفت غمگین برون؛‪.‬‬                            ‫دون‬          ‫دای‬    ‫سینجی سرایت‬
   ‫«لفت فری ‪٥٦٣٦٦‬‏ ‪.‬‬
           ‫‪ ۲‬تاراج آن سبزه پی کرد گم ‪:‬‬                                  ‫‪ - ۴‬سپنج ‪-‬توران پبکانه سم‬
   ‫‪.‬‬   ‫نظامی کنجوی‪ «.‬کنجینه‪۸ 4‬‬
   ‫‪ - ۱‬مخفف «اسینده (ھ‪.‬م‪: (.‬‬               ‫‪.‬‬   ‫ولف‬         ‫‪ :‬فپرست‬   ‫رك‬     ‫_‬   ‫®‬            ‫سه‌پنج ‪.‬‬      ‫‪۴‬‬

           ‫از بپر چشم تا ارسد مرورا گزند‬                      ‫دارم صیئف اگر چه‌بر آتش‌همی فکند‬

           ‫ال|‌تچشون‌سیند ‪.‬‬    ‫خچو‬
                                 ‫اهم‬
                                   ‫بی‌‬
                                     ‫ورو‬
                                       ‫با‬                     ‫او را مپند و مجمر ناید همی بکار‬
   ‫حنظلة بادغیسی ‪«.‬سخن وسخنوران ج‪۱‬اص» * ‪۰‬‬
                                       ‫« اسیند» که کوهی بوده درسیستان ‪:‬‬                         ‫مختف‬       ‫‪۲‬‬

                ‫برو تازبان تا بکوه سیند ‪.‬‬                              ‫بخون نربه‌ان کمر را سند‬
   ‫فردوسی طوبی‪«.‬ذاب ‪ ۱‬ص ‪۹۷٩‬‏ ‪.‬‬

   ‫‪8‬ے رلك‪:‬اسیند یار ‪ ۰‬اسیندار ‪۰‬‬                ‫‪- ۹‬مخقف «اسیندار» (ه‪.‬م‪):‬‬                      ‫‪ ۴‬سه‌نند ‪.‬‬    ‫‪۸‬‬

                     ‫بت رك‪ :‬اسیندار مذ ‪۰‬‬       ‫‪۳‬‬               ‫» سیندار هذ ‪.‬‬         ‫رك ‪ :‬اسی‌ندار مد‬     ‫‪"۱‬‬
```


## [2026-09-14T02:31:27.905Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(t):\n    if 'اسفنج' in l and i>300:\n        print('leaf',i, re.search(r'\\[pdf page (\\d+)\\]',l))\n        print(l[:2600]); print('====')\nEOF"
}
```


### [2026-09-14T02:31:29.237Z] TOOL RESULT

```
leaf 346 None
که آنسخها از بدن اوجته برآن کس میخورد
وفرومیرود ؛ و گویندهرچنداورا بز ند فربه‌ترشود.
که خاریشت بر انداز باشد .
اسفا دور بفتح اول وسکون ئانی
و قای بالف کشیده و بای ابجد بواو دسیده
و بای قرشت زده » نام شهرست که ائوشیروان
بثا کرده مود وازحملهٌ هفت شهر مداین است٩‏ 2
اسفار ۰ بقتح اول بر وزن ؛فمار 0 نسام
ولاعتی‌است گویشد دح آنولابت رود اه ات
که بهرسال سه ماه آب دروجارست و باقی اسئم
منقطم باشد - وبسر اول‌نام ربحانی است بنایت
اسفا ثیر « بنتح اول و سکون نون وضم
باشد. وان شهریست که انوشیروان بنا کردموطاق
کسری در انجاست ۷ -
اسفر اج ۴ - بکر اول وتاك و رای
ی نقطه بالف کشیده و بجیم زده » ملفت افدلس
مار چوبه را کویند و ب رکه آن مانند بر که
اک :
باشد » وآن شهرست عشهور در خراسان .
اسفر سب - بفتح اول و رأبع وتگزن
ثالی و ثالث و مين بی‌نقطه و بای ابجد . حیدان
و فا و عرصه را کوند ۲ ۲
اسقر سف - با فا » بر وژن و بمعث
اسفرمپ است که میدان و عرصه وضنا باشد؟ .
جمم کلها و رباحین باشد عموماً و ربحانی است
۱ ۳ رکه : اسپانس.
5ناو250۵]2 .
بقایت خوشبوی که آنرااس نیز گوبند خصوصا:
اسفر نج - باجیم» هعرب اسفرنگه‌است
و آن شهری بود تزدمك بسند سمرقند و مولد
سیف است و بسنی کوبند قربه ات ترديك
7"
اسیفر نگ » با کاف‌فارسی, بروزن‌ومنی
اسفرتج است که قریه‌ای باشد از قرای سمرقند .
اسر و ك « یکر اول و فتح الث وضم
رابع و سکون ثانی و واو و دال ۰ سنگه خوارله
باشد » و آن پرنده است سیاه رنه ببزد کی
کنجثك و چند پرمانند شاخی برسر داردوبعر ی
قطا کویندش. اکراستخوان اورا بسوزانندوپب‌ایند
وبا روغن زبت بجوثانند وبرداه التعلب وسر کچل
بمالئد مو بر آورد . #9
اسفناج دومی « دوایی بائد که
آنرا بعربی قطف وسرمق و بقلةالذهبیه خواشد.
استقا را نافم‌است . اکر جامه ابرشمی رابطبخ
آن بجوشانند باك و یاکیزه گردد .
اسفنج * - بکس‌اولوسکون انی وفتح
الث و نون وجیم ساکن » چیزی است شبهبنمد
کرم خورده و آنرا ابر مرده و اب رکهن کویند
و بعربیرغوة الحجامین
و هرثفه خوانند .
کویند حیوانی است
دربایی بدان جهت که
چون دست بروی نهند
خود را جمم کند و
چون بمیرد حوجه او
را ساحل اندازد » و
بعضی ‏ گویند نباتی
است دربایی . اگر در
شراب میزوح باب صید اسفتج
۴ اژ تازی » از بونانی
6 اسهناج - رکه : اسیناخ .
====
```


## [2026-09-14T02:31:35.030Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[346][2400:5000])\nEOF"
}
```


### [2026-09-14T02:31:36.355Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:31:38.404Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t[346]))\nprint(t[347][:1500])\nEOF"
}
```


### [2026-09-14T02:31:39.545Z] TOOL RESULT

```
1933
۱۳
گذارندآ برامخود کشدوشراب‌رابگذارد,وباخا کتر
آن زخمی را که در ساعت زده باشند خشك بند
کنند » زود لیکو سازد . گرم و خهكت است
در اول و دوم (۱) .
آسفنح است که آمر مرده باشد
اسقنك ۱ - بکر اول وفتح اك‌وسکون
افی و رأبع و دال اسجد ۲ تام ماه دوآزدهم باشد
از سا شسی ۲ و نام الکه‌است درنیشابور -
1 نام داروبی است که ترا حزاراسفتد نیز گویده
و آن نوعی از سداب کوهی باشد و بعربی‌حرمل
" اسقئدار هف ت بر وزن و معت
اسیندارمذ است که‌نام‌امدوازدهم باشدازسال‌شسی.
و للم روژ پنجم آزهر ماه شمسی ۰ و فارسیان این
که مان ابشان متعارفست که چون نام روز با نام
ماه موافق باشد آنروز را عید باید کرد و مبارك
دانت - و نام فرشته است موکل بر ییشپا و
درعتای بو امیر و صاله ماد ایتدان کی میتی
دارد - و بمعثي زمین هم آمده ! ست که سر بی
ارش خوانند ۴ .
اسفند اسشید یک اول وفای دوم»
خردل سفید است ۳
حب‌الرشاد خوانند .
اسفند مد - نم میم ۴
نقطه دار » نام روژسوم (۷) است
و بوسیرن: ۳
اسفندیاره بر وزن و معنی آ-نددار
است که نم پس کشتاسب باشد و او را روبین تن
میکفتند - و بمعنی قدرت حق و لطف یزدان‌هم
هت ورب ماه امفندار و رب روز اسفندار
اسقیك - بر وزن و معنی اسیهید است
کممطلق سیهسالار باشد۷ - ونامی است مخصوس
ملوك فارسیان ۸ .
اسفهبد خوده. بر وزن و معنی
اسیپبد خوره است که باعتقاد اشرافیان فاری شی
ناطقه باشد که آن قوت متکلمة اسانی‌است ٩‏
اسفیجاب - باجيم بروزن استیعاب .نم
3
و۲
اسفیداج باجیم. عمرب اسفیداب است
که زنان برروی مالند و نقاشان و مصوران هم‌کار
قرمایند» وخوردن آ نکشنده نود تا سفیداب
تر
استبی‌ار ‏ مخفف اسفیددار (۳) است
که درخت یده‌باشد وبعربی غرب خوانند ۰ وبصنی
کویند توعی از یده است ٩*‏
اسفیف دشت « اسفید معلوم » و دا
ایجد عفتوح‌وش
```


## [2026-09-14T02:31:46.155Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(724,740):\n    l=t[i]\n    if 'تف' in l:\n        print('### leaf',i); print(l[:1800]); print()\nEOF"
}
```


### [2026-09-14T02:31:47.276Z] TOOL RESULT

```
### leaf 728
کوبندا ‏ و بمعنی خوردلی وآذوقه ورأتب‌هم
آمده است - و بمعتی‌پیمانه هم هست - و نقاه
بر وزن شراره هم عیگویند .
ب‌- بنم هردو تای قرشت و سکون
هر دو غن نقطه دار . چیزی باه مالند کله
و قفیز که غله بدان پیمابند - و بعضی کویند
و بفتح ارل وثالث که تای فرشت باشد هم بمعنی
پيمانةٌ بزر که چهار خرواری باشد» و باین معنی
بجای‌حرف ااث نون هم بنظراهده‌است -وبسنی
کوند بیمانه ای که مك خروار غله بگیرد -
ونان تن را نیز کونند . و باين هعنی بجلی‌غن
آحر خای نقطه دار هم هست که تفتخ باشد ۰
لف » بفتح اول و سکون ثالی ؛ ار
وحرارت و گرمیراگونند؟ - و روشنی ویرنورا
رضم اولآب دهن‌انداختن باشف ۲ .
(۱) چش : هم .
وقدح شراب خوریرا گوند, وباین معنی بجای
حرف اول نون عم گفته‌اند :
هت « بفتح اول بر وژن هفت ۰ ممحنی
گرم وکره‌ی وحرارت باشد؟ - وماضی نفتن‌هم
هست یمن ی کرم کودانید6 - وبهء‌نی تعجیل‌وشتاب
آب تماجی لریزی در تنار
۴ رك : تب وتاب :
زمن او چو دوزخ و زنف آن
چو موی زنگان شده کیای او .
«منوچهری دامغانی ۲ ۷*.
۴ بمعنی اخیردر هندی باسنان۰ 5841۷ ۵ ۰ 8۵01۷8۵16 , کتی 5۳61۷28 ۰ ارمنی
اما ,لابنی 50۷6 ,یوانی ۳۱۷۵ . کردی 466 «نف»,۱۱۷۷ ۱۷۰) رناا لا (یف کردن» تف)؛
اقبانی ۰00 ۰0۵ ۱۵۴۵۱ («ب کردن) ,امتی لا . رخي ۵678 لا , سریعلي 061880 لا
شره درسلحهُ 0٩۱‏

### leaf 729
ات
هم‌آمدساست٩‏ - وکرم رفتن و کرم آمدن و کرم
کته رونت کته ۱ و بت خیم
وخرامان هم هست - و قهر و نب و گرم شدن
ازخشم وقهررا نیز کوبند؟ - و کیاهی‌است‌دوابی
که خوردن بیخ آن مانند تاتوله جنون آورد -
ونام موضعیاست ازمضافات یزد که از کمال صفای
هوا جامغع گرم سپر وسردسیر باشد.
فتن - بر وزن رفتن » مخفف نافتن ۴
ارت که کرم شدن و مکدیگر راکرم کردایدن
باشد
َفقه " « بروزن هفته, بمعنی بسیا رکرم
شده باشد؟ - ومضفف نافثه هم هست که آزرده
ور کوفته شده ومکدر باشد - و نام گیاهی‌است که
خوردن مخ آن جئون آورد ۲
تفته چگر مه کنابه از عاشق باشد -
وکی را نیز گونند که علت دق داشته باشد.
قفتیات - بر وزن تزديك ؛ یشمی باشد
نرم که آبرا از زیر موی بز بشانه برآرنده و از
آن ال وتکیه نمد(») تا انم فند
هر چاع < با رای فرشت وجی‌فارسی
۷ چش : کفته‌اند .
بر وزن نمد داغ . بممنی ساخته و پرداخثه -
ومستعد ومپیا باشد . وباین معنی بجای غین(۳):
فاف هم‌آمده ی
#سی؟ - بنتح اول وسکون ثالی وسین
بی نقطه, کرمی وحرارت را گویند .
شسه() بضم اول وسکون ثانی وفتح
تالث » سیاهی و دافی را گویند که دربشرمواندام
آدمی‌میباشدو آ نراعوام«ماه گرفت» کویشد»وبسربی
کلف خوانند - و بممتی اندوه و بی قراری دل
هم هت - و میل وخواهش بهرچیزی که دیده
شود هرچند که سیر باشند » و این صفت بیشتر
عارم‌زنانآ بسنن؟ ومردان‌تربا کی‌وافیونی‌میشود؛
ویفتح اول هم درست است ۰
آقسیا(ه). بروزن اغنیاه بیونانی" صمغ
سداب کوهی است ؛ و بعضی گویند صمخ سداب
شزاس :
ل قسیدن ۲ ۰ بر وزن : فهسدن » بمتی
گرم شدن باشد .
قسیده4 - بر وزن فهمیده ۰ بفایت
کرم شده را گویند .
(۴) چش: + تقطمدار.
۱ - اسم مفعول از:تفتن (ه .م.).
بدست آهن تفته کردن خمیر
۴ را: :ب وناب وتبسیدن وتفبدن .
۲ - بيونايی 10206 «اد2:
بغیه ازسفح ۵۰۰
رك: افتن. ۴ - اسم‌مفعول از:تفتن:
* - این حالت زئان‌را کگونند.
۷ - از؛ تفی (« ۰ (- بدن
۸ اسم مقمولاز ضیدن («.م.) .
۴ - در اوستا
سوی شهر آزپیش من‌آو تیز وفت.
مولوی بلخی رومي ۰

### leaf 730
قسیله - بر وزن غربیله . جنسی از
پارچة ابربشمی باشد کداز آن فبا وازار وچیزهای
دیگر نیز بدوزند.
فش - بسکون تانی بر وزن کفش ۰
سرزاش و طعنه را کوندا - و بکسر انی
حرارت و کرمی باشد؟ .
فشل - بر وزن مشعل» بمعنی اول نفش
است که طعنه وسرزش باشد .
قشله - یکر ثالث بر وزن امثله ,
قلیه‌ای باشد که از کوشت و تخم مرغ و زردله
وصل یزد » و کشنیز و کندنا در آن ۵
وبسضی گویند عدی‌سبز نیم پخته‌باشد؟ ۰
تشه - بنتح اول واك وسکون انی ۰
بمعتی طعنه وسرزنش باشد - وطعنه‌زدن وسرزنش
کردنرا نیز کوبند۴ .
تقشیله - بر وزن غربیله » بمعنی تفشله
است که قليةٌ با گوشت وتخم‌مرغ وزردك وعسل
باشد » و بی کندم ومویز و کردکان و کشنیز
۱ رك: تفشل ونششه, ۰
۳ ره تفشبله.
تب ۷ وه <<
هم داخل کرده اند و عدس سبز يخته رانیژ
گونده .
لك - نم اول و فتح انی وسکون
کاف » چوب دراز مبان‌خال ی که با کلولةٌ گل‌وزور
ی بدا نکنجتك وامثال آن زنند - و فنگه
آهنی را نیز گفته‌اند 1
هوك ه بر وزن متصود ۰ بمعنی نجدت
باشد » و آن استواری تفضی است در مقام خوف
» بر وزن طعنه » پرده عنکبوت را
گویند .
هنی « بتح اول بروزن بخنی ۰ بمعنی
تفه باشد که پردة عضکیوت‌است -
هو . یم اول و ثانی و سکون واو ؛
آب دهن را گویند - وآب دهن انداختن را نیز
گفته‌اند۷ .
تقو ده بر وزن تنور" بمعنیگل‌بادد
که حربی طن خوانندش .
۵ - تفئیله , کوشت
۹ - رك: شنک ۰
بنشکرده ببرید زن را کلو
۲ ر۵: تفوژ.
روی چونانکه بخته تفشیله .
«لفت فرسی444) رك : خشله.
تفو بر چنان ناشکیبا و .
بوشکور بلخی. «لفت فرس 4*۸*.
آحفه) موب آین‌حدس است ت که کمه از
تف گلا؛ ,ينك 066۷ (تف انداختن) بایسو ند
«2»آمده باشد. رث: مقالةٌ فرای ۳۴96 درباب
کاب:02۲202108۵0 , ۰۱۷16۵865 1.۲
0 02۱ ۲۲2۲۷۸۲0 ۰ 6۲۵۳۵۳۱۵۲
سس
بننگه

### leaf 735
یدای ‌-
از ولات کنجه - و پرده ای ازموسيقی‌باشد .
تگتارا . غتح اول و ای قرشت
بر وزن پرواز » ناختن و دویدن - و جتجو
کردن ماشه .
تگرگ؟ صبفتح اول و ثانی و سکون
رای فرشث وکاف فارسی ۰ معروف است که ژاله
وبخچه باشد - و بفتح دای فرشت بروزن‌نفزك.
تلای
یاه وی دبواررا گویند.
یگ - بفتح اول بر وزن حمل » قوچ
جاعه بثه کنند؟ .
تگمر م اول و فتح میم بس وزن
دختی » تیر تخمار است(۱) » وآن نبری‌باشد که
بجای پیکان کرعی از چوب دارد .
قل » بنتح اول وسکون ثانی , کوه‌یست
ويشتهة بلند راگویند؟ - و هرچیزی که برروی
هم ربخته خرمن کرده باشند - و کنابه از پس
امردمز لف‌ومضخم(۲) باشد» کوبندعربی‌است6 .
تلا توف بفتح اول وثانیبالف کشیده
وفوقانی بواو رسیده و بفا زده » شور و غوغا را
کویند - وکی را نیز کنته اند که خود را
وتفوها .
هر کجا ربدکی بود تگلم
چبر کین(۳) و بلید نگهدارد و از کثافت‌ونجاست
پرهیزنکند ومردم ازونفرت کنندلا .
اج بفتح اول بر وز نکلاح» بانگ
ومتغله وشور وغوغا وغلغله باشد » و باین ءعنی
لاس « بفتح اول بر وزن ممای ,
نام شهرست در تر کستان۸ .
(۳) خم۳:چ رکن.
۴ - پهلوی 28278) «بندهش ۱۳۷
هر کجا کاملی بود خیم .
«لفت فری ۱ ره : تل.
. ۹
٩‏ - زنی پلشت ونلاتوف و اهرمن کردار
۲ - رکه؛ تلانج: ثب‌یامد بردرم دربان باج
نگر نگردی از کرد اوکه کرم آمی .
شهبدبلخی. «لغت فری ۲۷.
در بجنبانید بابانگگ و تلاج .
طبان مرغزی. «لت‌فری ۵۶
لکنی خمش برادر» چو بری ازآب و آذر
ز سبو همان تلاید که درو کنند بائی .

### leaf 737
9 کین
0 هیرین نله » با نون بر وزن چرنده ۰ کچ
است٩‏ - و ثلق وزر ورق را ليز گویند » و طلق زبالرا گوشد بعنی شخص ی که درست تکلم قوادد
ممربآست - ولوعی از قماش هم حست - وبضم | نمود؟ * واو را جربی فأفاً خوانشد .
اول وسکون انی‌غلهای باشب کهآ ن را لوییاخوانند تلنگی ضتح اول و نون و سکون تالی
وبکسراول وفتحثالی‌جامة پیش‌واز وآستین کوتامرا +کاف . میوه ای بود شبیه بشفتالو - و نم اول
یند - و درخت سیب حمرایی را یذ | وکاف‌فارسی مروزن تفن , حاجت و ضروری-
کفته اند که بونانی زعرور و جمربی ذوئلاث | ومیل و خواهشس ویاز و آرزو باشد ۵ . چه
حبات و بثیرازی کیل و درخرامان علف شیران | تلشگی ییازمند وخواهش کننده را گویند و باین
خوانند؟ - وبکسر اول وسکون نانی » زنجبیل | معنی بر وزن خدیکه هم آمده اسکر. رخ یکی
تر و تازه را گونند .9 ید نت اه من واه
تلهی؟ - بنتع اول وسکون ثانی وم | وامتالآن - وخوشةٌکوچك انگور که برخوشة
مکسور شون رده پیش آ خعور و رالات زانگر کلان چسبیده بود - و بکر اود و قح ای
باشد بزبان زند و پازد (۱) و بمربی اف | نام ولایتی‌است از ملك د کن۷ .
کویند . تلنگین بروزن ومعنی‌تر نجبین است»
(۱),چیك: ژند ویاژند..
۱ باین‌معتی لفتی‌است در:نلخ. (هم). ۰. ۴ - قاقادرلاهیجان, زبان کنجشك
5 لات. «تابتی  .>۱۷۳‏ ۴ -هز,1۵1۳120, پپلوی ۷۵0 بینی «بونکر ۱۱۹*.
۴ - در کناب ار۵105) و رك : تمشده . ۵ رکه : تلنگی و له .
۱ - مصحف :تلك (ه ,ما . ۷۳
۵ تلگراف - کی اولودوم» از فرانسه 46168۲28۳6 ( از بونانی 4۵16 بمعني دود
وسد.و 8۲۵016۱2 بمعنی نوشتن) , ابزاری که بدان میتوان مطاب خود را بشخص منظور از
فواسل دور ابلاغ کرد وآن‌هم بوسیلهٌ سیم(با سیم) وهم بدون‌سيم (بی‌سیم) صورت‌میگیرد. فرمتنده
حروف کلمات را ثبدیل بعلائم قراررادی میکند و کیرنده علائم‌را تبدیل بحروف اصلی مینم‌ابد
وبشخص منظور ابلاغ میکند .
تلمبار رکه : قلیثبار .
بقیه از صفحه ۵۰۸
۵ تلسکپ - بکر ارل ودوم وضم چهارم » ازفرانه
6 (از بوتانی ۵16) بمعنی دور و بعید, و 5۳60۳618 .
بمعنی آزمایش کردن ) » آلتی تجومی که برای مشاهده کواکب
بکاررود . دوربن .
۱ لت -بکن اول ودوم وشم‌سوم؛

### leaf 739
قم ع بفتح اول دسکون ثانی ۰ آفنی
امت که در چشم پیدا میشود مانند پرده؛ وآ را
بعربی شاوه
تماجح نم اول بر وزن اعاج ۰
کي درازی را کویند که از پارچه دوزند وبا
از ابربشم بافند .
تماخره - بتح اول وخای نقطه‌دار
و رای بی نقطه . بمعنی‌هزلومزاح ومسخر کی
و ظرافت باشد - و بسکون خای نقطه دار هم
طبعی و غیرآن .
تهساشا؟ - با دار اف کنیده
«دبوان ناسر خسروص۹۵۹ مشون۱.
نظر کردن بچیزی باشد از روی حظ با ازروی
عبرت .9
آمام شدن - بسی باهبا رسیدن
کاری باشد - و کنابه از مردن و فوت شدن‌هم
هت .4 ۱
لهقم ه بنم حر دو فوفانی وج
تومیم , قطای ؟ باشد.وآن دم کاو کوهی‌است
سپاهیانآنرا از تیزه وعلمآویز ند وبر ۷2
بندند؟ - و یکسر هردو فوقانی بحربی سماقی را
گوین که درآش و طعام کنزر6 ۰ ۱
نمیا با خاو بای خن بر وزن مد
ولفة بمعنی بابکدیگر پیادمرفتن است,چون باران برای تفرحاکثر باهم پیاد‌سیر میکنند لهذا در
2
س رکرمی و مشفولی: هو بفرمود تاهمةٌ مطربان و مسض رکان و هزالان و سگان شکاری و بوزنه
وازین جنسپاکه تماشاء ملوك باشد . ازسرای خلافت بیرون کرداد . » «مجمل التواریخ و الصص
ص۳۹۶ وص‌یب؟ . ۴ - بونابی 16۱6 »لانینی 6 (فرانه ۵»6ا6)).
۱ ۴ رك؛ پرچم. ۵ سماق مممولی 0718713 5لا110 است ۶ ابتی ۱۷۳ *.
ورل: لك[:۳۱۸. ۱ - برهان ذبل «هفت‌مرد» بکی‌از 2 «یملضا» باد میکند
ویرواشی آزانن عباتر:موی «تملیضا» بود؛دلی لضت هحیح لستء از همالنت که در زبانهی‌اروای
«یملت» نامیده‌شود. «داسثان اصحاب کهف بو بوسف بنیان. دانشنامه ج۱ ص۳۸*.
6۵ قماشاگاه - بفتح‌اول؛ جای‌نماشا» منظر: *۱ کرملك تماشاگاه خوش‌را باراید» منت
بر کسی تباید نهاد.» «نورورنامه۷۷».
عبر بفتح اول؛ از فرانسه 4100066 از لاتبنی 0۵8۳0۷۳0) نمی
ادارات پنت یم ودرمقایل اخذحق حمل وتقل نامه‌ها وغیره بمحمول الساق کنند .
```


## [2026-09-14T02:32:21.826Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,l in enumerate(t):\n    if '1628' in l and 'spnc' in l:\n        tag=re.search(r'\\[pdf page (\\d+)\\]',l)\n        print('leaf',i,'printed ~',i-66,'tag',tag.group(1) if tag else None)\n        print(l[:1500])\n        break\nEOF"
}
```


### [2026-09-14T02:32:22.852Z] TOOL RESULT

```
leaf 129 printed ~ 63 tag None
 'sp^nSv'k

       TSP 6.146                                                          horse covering, horse armour                      64
                                                                          MDii pl94
 1612 'sp'yn'w'k B
      (o)spenawe ^'sp'w^wy                                           1624 >spn'yn     B                           jl^x'J^
      revolution                                     ^i.
                                                            U*J*"         (o)spancn ? ^spnyn^y
       TSP 11.21
                                            oiilptA fwj^U;) ^jj^-         SCE   362
                                                                          (<?/)iron
 1613 Vyn(h)        B,S
      (o)spen ? =*sp'yn                                              1625 'spn'yn'k    B                          jo^^T
      revolt
                                                                          (o)spanenc (spn^yny 'spnyn'k) ©Khwar.
      TSP 9.14; Frag. Len. 81.16                                            as pant; Khot. hissana-, Oss. afsan-, Past.
 1614 'sp'ynst    S                          U6i?J>a <UI^jU^                aspina, Sughn. sepen>, Parth. dsunen\ Pahl.
      (o)spanst, spanst ? ^sp'nch, >spnc                                    }s(y)n ^spnyn'y, spn'yn*k
      inns
      GMS 260                                                             SCE  205, 275; Bailey. Prolexis. 419
```


## [2026-09-14T02:32:23.503Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON شپش ===\"; grep -n \"شپش\" MON_part1.txt MON_part2.txt | head -10\necho \"=== MON اسفنج ===\"; grep -n \"اسفنج\" MON_part1.txt MON_part2.txt | head -10\necho \"=== TAD اسفنج ===\"; grep -n \"سفنج\" TAD_pages.txt TAD.txt 2>/dev/null | head -10"
}
```


### [2026-09-14T02:32:23.614Z] TOOL RESULT

```
=== MON شپش ===
MON_part2.txt:14853:قمل: لسهر(ع.] (.) (جاد.) شپش 
MON_part2.txt:33723:کردن شپش بکار می‌برند؛ سنبل ختایی 
MON_part2.txt:47348:شپشکك گندم. 
MON_part1.txt:45663:به وسیلةً شپش سرایت کند و چون علایم 
MON_part1.txt:54858:مخصوصی که از گزیدن شپش يا کبک یا 
MON_part1.txt:84199:و تیفوس و غیره می‌باشد. شپش انکل انسان 
MON_part1.txt:84212:دگردیسی است. در انسان دو نوع شپش 
MON_part1.txt:84217:است و دیگری شپش 
MON_part1.txt:84219:لباس خارج می‌شود. تخم هر دو گونه شپش 
=== MON اسفنج ===
MON_part2.txt:2717:سحاب. ابر سفید؛ ج. غمام؛ غمائم. اسفنج 
MON_part2.txt:3884:ج. عبوم. مه. اسفنج دویانین: 
MON_part2.txt:3892:تایب نو یکی اسفنج. 
MON_part2.txt:19443:فرامی‌نی‌فرها و اسفنج‌ها و مرجان‌ها و 
MON_part2.txt:64115:که رآس آن بر جسته و اسفنجی است. این 
MON_part1.txt:12849:اسفنج: لها (معر. اسپنگ - اسپنج» 
MON_part1.txt:12851:بی‌مهرگان که تشکیل رده اسفنج‌ها ر 
MON_part1.txt:12853:بی‌قرینه و ساده‌ترین پر یاخته می‌باشد. اسفنج 
MON_part1.txt:12854:آهکی: (جان.) اسفنجی که استخوان‌بندیش 
MON_part1.txt:20719:نسج اسفنجی. 
=== TAD اسفنج ===
```


## [2026-09-14T02:32:33.868Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON اسفنج entry ===\"; sed -n '12840,12870p' MON_part1.txt\necho \"=== MON شپش entry ===\"; sed -n '84185,84230p' MON_part1.txt"
}
```


### [2026-09-14T02:32:34.050Z] TOOL RESULT

```
=== MON اسفنج entry ===
است» اسفل سافلین. 

اسفناج: لقجدئعی [ - شست و اسپاناخ 
اسپناج - اسفناج] (ا.) (گیا.) گیاهی است 
سر دسته گیاهان تیره اسفناجیان» جزو دو 
لپه یی‌های بی‌برگ» گل‌های آن خوشه‌یی» 
سبز رنگ و کوچک» دارای ۵ پرچم و ۵ 
کاس رگ بهم چسیده است. 

اسفنج: لها (معر. اسپنگ - اسپنج» 
فشرده] (۱.) (جان.) جانوری است جزو 
بی‌مهرگان که تشکیل رده اسفنج‌ها ر 
می‌دهد و آن جزو جانوران گیاهی شکل و 
بی‌قرینه و ساده‌ترین پر یاخته می‌باشد. اسفنج 
آهکی: (جان.) اسفنجی که استخوان‌بندیش 
از جنس مواد آهکی است. 

اسفند: 0 ([- اسپند - سپند] (.) [- 
اسپندارمد. اسفندارمد] ماه دوازدهم سال 
شمسی و ماه سوم زمستان. روز پنجم از هر 
ماه شمسی. (اخ.) یکی از امشاسپندان 
نماینده بردباری و سازش اهورا و نگاهبان 
زمین. ( گیا.) گیاهی است از تبرةٌ سدابیان که 
بیشتر در نواحی مرکزی و شرقی و جنوبی و 


غربی آسیا در آب و هوای بحرالرومی یا 
معتدل و نواحی استوایی می‌روید؛ اسپند» 
سیند» حرمله» سداب بری. 

اس‌فیداج: لاه [سعر. سپیتاگ - 
=== MON شپش entry ===
کشیدن تصویری از روی کسی باچیزی به 
شرطی که با اصل مطابقت ت کامل داشته باشد. 
شسسسبیه یز دان؛ 80 (ع. ف. 
شب گرداننده] (ص فا .) کا رگردان نمایش‌ های 
مذهبی» تعز یه گر دان. 

شیپ و ش: 8-۳14 [- شب بوش] (امر.) کلاه 
و طاقیه. بالاپوش. لحاف. 

نسیش: 5 (- اشیش] (.) (جسان.) 
خسره‌ای ۱ از راسته نیم‌بالان که به علت 
زندگی انگلی فاقد بال شده جزو انگل‌های 
خارجی و خطرناکك مسحصسوب است زبرا 
حامل میکرب برخی امراض از قبیل تب زرد 
و تیفوس و غیره می‌باشد. شپش انکل انسان 
است و در جامة اشخاص کف و دور از 
بهداشت زندگی می‌کند. قطعات دهانی این 
حشره سوراخ کننده است. شاخک‌هایش 
کوتاه و چشم‌ها کوچک است با اصلا و جود 
ندارد. سر این حشره نسبة دراز و پاهایش 


فرهنگ فارسی معیر شیخون 


کوتاه است و اکثر دارای ۲ بند است که به 
قلابی منتهی می‌شوند. این حیوان بودن 
دگردیسی است. در انسان دو نوع شپش 
دیده می‌شود: یکی شیش سر است که در 
سم 7 
ذبلای موها زندگی می‌کند و تیره رنگ 
م 
است و دیگری شپش 
سر بزرگنراست و در موقع نیش زدن از درز 
لباس خارج می‌شود. تخم هر دو گونه شپش 
۳9 و ۲۶ 
دانه‌های سفیدی در قاعدة موها با درز لاس 


گذاشته می‌شود و پس از چند روز بچه‌ها از 
تخم‌ها خارج می‌شوند. بعد از ۳ هفته بالغ 
شده قادر به تخم ریزی می‌باشند؛ اشیش 
شپ‌شپ: 327 [- شپاشاپ] (اصت.) 
صدا و اواز اصابت تیرهای پیابی. (ص.) 
مضطرب؛ بی‌تمکین.
```


## [2026-09-14T02:32:47.561Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM اسفنج ===\"; grep -n \"سفنج\\|سفنك\" AFM_pages.txt | head -10\necho \"=== PLA isfang ===\"; grep -n -i \"isfang\\|isfanǧ\\|isfang\\|spanǧ\\|aspinǧ\\|Schwamm\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== LKT spongos ===\"; grep -n -i \"spongos\\|isfang\\|Schwamm\" LKT.txt | head -20"
}
```


### [2026-09-14T02:32:47.693Z] TOOL RESULT

```
=== AFM اسفنج ===
=== PLA isfang ===
=== LKT spongos ===
575:[Aus  dem  pers.  bäd  'Wind'  [Horn  Np- Et  S.  35,  Nr.  151]  und  ar.  ward  'Rose']. Eine  Pflanze  (Komposite)  aus  dpr  Gat- tung Echinops  'Kugeldistel'.  Hieraus frz.  bidigar  'Schwamm,  der  auf  den Rosensträuchern  durch  den  Stich  eines Insektes  bewirkt  wird'.    [Devic  DEt  63.
1589:[Vom  Vb.  gaffa  II  'tiocknen',  also  eigent- lich 'die  Trocknerin']  'Wischlappen, Schwamm';  hieraus  mit  ar.  Art.  und
3099:lo33a.  Arab.  luf: 'Eine  Arumart,  Arum  arisarum',  Einheits- nomen lüfa;  hieraus  mit  Übertragung auf  eine  ähnliche  Pflanze  sp.  lufa  [Dicc Gast  1284  a]  zur  Bezeichnung  einer  den Cucurbitaceen  zugehörigen  Pflanze,  Luffa cylindrica,  aus  deren  trockenem  Faser- gewebe der  Früchte  der  sog.  vegeta- bilische Schwamm  hergestellt  wird, welcher  als  Schwamm,  Einlegesohle  oder zu  ähnlichen  Zwecken  benutzt  wird. Engl,  loofah,  dtsch.  L?i/^rt(kürbis  und -schwamm).  —  [Ableitung  aus  ar.  luffäh 'eine  Art  Eierpflanze'  scheint  weniger zu  passen,  auch  existiert  das  in  MWiD 84  angeführte  pg.  lufa  wohl  nicht.]
5812:Luffa(schwamm)  1338  a
```


## [2026-09-14T02:32:51.753Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la | grep -i tad; echo ---; ls ocr 2>/dev/null | head -30\necho \"=== TAD head ===\"; head -c 1200 TAD_pages.txt 2>/dev/null"
}
```


### [2026-09-14T02:32:51.826Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb   243285 Sep  4 14:06 TAD_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb   151889 Sep  4 14:06 TAD.txt
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
=== TAD head ===
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




                    ‫حل '‬
                    ‫ذكرى الذ ممردص‬
 ‫الى الكير بروحه ونكرة‬        ‫الى من حك العلويغاد على الاادب‬

 ‫وقلبه ؛ الى من حب اطق وشرف الحق ولا نخاف فسيبيل المقلومةلاتم‬
                                  ‫والى الصديق الصادق فىكرم انلساانية‬


                  ‫عابلممل ي بنابت اباظ‬
                         ‫اهدي هذا الكتاب‬

               ‫المخلص‬

       ‫امم تيووسب�
```


## [2026-09-14T02:32:54.357Z] TOOL CALL #39: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py TAD:35 --image 2>&1 | head -80"
}
```


### [2026-09-14T02:32:55.643Z] TOOL RESULT

```
no scan of TAD covers printed page 35 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:32:58.256Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in range(36,45):\n    print('### leaf',i)\n    print(t[i][:900])\nEOF"
}
```


### [2026-09-14T02:32:59.411Z] TOOL RESULT

```
leaves 87
### leaf 36
                                    ‫سس للإفةسس‬

                                      ‫إزميل ‪ 5‬وناني ‪ 1105‬وه المجة‬

                                     ‫زناف ونال عوتديعا تضق رات‬
 ‫انيرك ‪ -‬نري « تزِبَرِك » وهو قوس محنديد للتحريك مرادفه النابض‬
           ‫وهو شريط من فولاذ يلف على حور ى الساعة ‪9‬بعمتد" فبحرك دوالي‪-‬ها‬
                     ‫وهو صداء الحديد والتحاس‬          ‫فارسي ‪ 0‬كار‬        ‫ا‬

 ‫يل ‪ -‬نات هندى الاصل وهو في جميعاللغات بلفظط واحد أترء‪612012‬‬

                                    ‫جره يحفرة العموهو ينبتفىالبلاد الحارة‬
 ‫‪:‬بجفر ‪ -‬وناني نهةدهاا وفي الايطالية ‪,0‬طدهنه وهو معدن بصّاص‬
  ‫حاصل منازدواج الزئيق بالكبريت ومسحوفه لونه أحمر ناصع إستعمله المصورون‬
  ‫ويطلق على نفس أحمريكتب يه ويطلق أيضاً على تراب أحمر يقال لادلفعيبرانية‬
                                             ‫د شثر » جبل وتدهن به الجدران‬
  ‫زتجير ‪ -‬فارسي ‪ 9‬زنجير» معناهسلسلة و ‪2
### leaf 37
                                   ‫‪ 00‬لك‬



                               ‫‪6‬‬    ‫سس‬   ‫«‬




‫معناء مشطرعون ‪:‬وكترفاء وهومشدى"مناشر (‪١‬‏ يلقل شرقا) ومعناة أعرق‬
                                                                           ‫ع‬

                                                                  ‫وأضرم‬
 ‫وهو السثرة بليسها‬     ‫اكد عامى ل للاتيجى ‪ 1101895‬ونوناني ‪5‬‬

                                                        ‫الرجل فوق ثيابه ‪7‬‬
                                                                  ‫ما امي‬

              ‫يصنع ملهالخرز‬        ‫ورد‬
                                     ‫سوحج‬
                                        ‫أوه‬
                                          ‫ار‪-‬سي ‪ 8‬شَبَه ‪6‬‬
                                                        ‫فعم‬
                                                          ‫سي‬
                          
### leaf 38
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
                ‫مسطار ‪
### leaf 39
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
                                                               ‫ال
### leaf 40
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
                                                                 ‫ق
### leaf 41
‫وهو رياب‬      ‫ستعاير وستطور ت في التركية« سانطور » وناني‪161‬‬

                                                                      ‫لهعشرة أوتار‬
  ‫جرم‬
    ‫رنه‬
      ‫‪6‬أي‬
        ‫فوت‬
          ‫شمعار‪ -‬اشوري مركب من « شينا» أي اثنان و « نار‬
                                        ‫باليونانيةوذد‪:‬ةادمهوع‪ 12‬أيبايلنمهرين‬
   ‫‪ 8‬‏‪68‬من‪ 812‬اليوناني معنا كتب السيرة والترجمة والتاريخ‬‫‪8‬تك‪7‬سار‬
                                                              ‫س‬
            ‫ستكه ‪ --‬تسرُيو«نكى » معناه حربة وسنان أي نصل الرمح‬
‫سلمورة ‪ --‬نري «سالاموره» معناه ماء مالحيكيسفيهالميك وهو ماخوذ‬
‫‪5‬مأنن‪:‬ه‪ 105‬الايطالي الذي معناه ماء ديف فيه ملحكثير وتقصد به العامة‬
                                                        ‫السمك المملح‬
‫و‪ -- 0‬في اليونانية ‪5‬ن» واهولعث وى الاراية كود ا رمواافت‬
                                                                          
### leaf 42
                                        ‫لوم ل‬
                                                                                     ‫‪-‬‬
                        ‫سيف ‪ -‬ووناني ‪5‬وألى وهو القاضب والقاطع والماضي‬

                           ‫سمكارة ‪ 1‬اسيانى ‪0502‬هاه وهو اقافة من اتتبخ‬

‫سيمة وسماء وسيمياء ن‪-‬ونانى ‪ 8016853‬معناه علامة ونوافقه فى العربية‬
                                                                               ‫واسمسمة‬
‫سيمونية س نسبة الى سيمون أي سمعان الساحر وبراد ما التجارة بالاشياء‬
                                                                    ‫المقدسة لاجل الربح‬
‫ر‪-‬يب عاملياعفنرنسية والاصح قيما مسب الاصلاليوناني‬
                                                ‫ع‪-‬‬‫تما‬
                                                    ‫سي‬
                          ‫غ‪ 01‬ومعناه حركة مرادفه الصور المتحركة أوالاشباح‬

                                      
### leaf 43
                                  ‫أبنت‬

 ‫فارسي «شاه ثراه‪ 6‬أى ملك البقول وهو نبات ورقهنافم للجرب‬         ‫شاهترج‬
     ‫وهو المزمار من قصب وغيره ينفخ فيه‬      ‫فياه ‪ --‬عامي بوناني ‪2‬‬

                     ‫شور ‪ -‬عبراني « شلوفار ‪ 6‬معناه جيل وهو البوق‬
                                    ‫ارامي « شوشبينا »‬   ‫شيين واثبين ‪-‬‬

                         ‫شتلة ‏ ارامي « شتلتا » عر بيهغرس وغراصس‬

‫«ششححممايمتا © براد بكتهاب صلوات الكبنة‬
                                      ‫ششححيمة ‏ ارامي و‬
                                                      ‫و‬
 ‫ومعتاهالاسود لانه فى الاصلكان جلدا مجلد أسود ‪ .‬قال العلامة القرداحي معناه‬
                                                                    ‫السادحة‬

 ‫‪#‬حتور ونخت ع‪-‬ابي انكليزى ‪60‬لا ( بلفظ بدت ) وهو سفينة صغيرة‬
                                                        ‫خفيفة سريعة للتمرزه‬
 ‫‪0‬‬    ‫طلاة اللانينيأى ن
### leaf 44
  ‫| دودة القر فقط أما الشرنقة فاسمبا ‪01022‬هط بالابطالية‪ .‬انلممسلجة اما تهعيريب‬        ‫‪١‬‬

 ‫‪5, 5‬ذ‪1‬ةة تمدع اليونالي وهو دودة الثَز المقتولة فىيجوف الشر نقة وقد عر بها العامة‬
‫فلادخل لهامبذه المادة اذ الهادويةتتخذ أنفسها بيتا‬          ‫فة‬
                                                            ‫رما‬
                                                              ‫سانّ‪.‬أ‬
                                                                   ‫لمز‬
                                                                     ‫از ج‬
                                                                        ‫جد‬
                                           ‫من دقاق العبدان وتدخله فتموث فيه‬
                         ‫ششم ‪ -‬دواء لامين ‪--‬فارسي د جثم » معناه عن‬

  ‫ششمه ‏ عابي فارسي «جشمه» معناه عينالماء مرادفه ممستراح ومرحاض‬

                                           ‫رىسية « شست »‬
```


## [2026-09-14T02:33:09.869Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"سفن\" TAD_pages.txt | head -20; echo \"=== spongos in TAD ===\"; grep -n -i \"spongos\\|5100\\|اسفنج\" TAD.txt | head"
}
```


### [2026-09-14T02:33:09.988Z] TOOL RESULT

```
203:                    ‫معتأد عله حربية وطائفة سفن‬      ‫اسطول ‪ 8-3‬وناني ‪8‬‬
560:                          ‫اسفن‬
597:                                                      ‫اولرابتحجار السفنالخ‬
1400:      ‫ظ‬                                       ‫طائطة من السفن وحملة حربية‬
2419: ‫مك‬    ‫واول‬      ‫سفن روا كدكا نت فى دحلة ‪ .‬واستممل الشيخ ابرادم اليازجى اه‬
=== spongos in TAD ===
```


## [2026-09-14T02:33:13.617Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\n# find leaf containing line 560\ntxt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nprint(repr(lines[555:570]))\n# which leaf\npos=sum(len(l)+1 for l in lines[:559])\nleaf=txt[:pos].count('\\f')\nprint('leaf',leaf)\nprint(t[leaf][:1500])\nEOF"
}
```


### [2026-09-14T02:33:14.693Z] TOOL RESULT

```
['                                                           \u202bربط عل السهم\u202c', '', ' \u202bوشاه بندر معناه\u202c      \u202bىء\u202c', '                       \u202bطعلى\u202c', '                          \u202bاسفن\u202c', '                             \u202bشط ال\u202c', '                                 \u202bلمرب\u202c', '                                    \u202bاناه\u202c', '                                       \u202bار\u202a-\u202cسى « بندر ©مع\u202c', '                                                      \u202bفدر\u202c', '                                                        \u202bبن\u202c', '                                                               \u202bرئيس التجار\u202c', '                                     \u202b\u202a7\u202c\u202c                           \u202bد\u202c', '                      \u202bأي اليوم الخسون\u202c    \u202bمم يونانى \u202a65\u202c\u202c', '']
leaf 16
‫من ‪0110‬م تفاح‬      ‫حت ابطالى ‪010002‬وم أي فاح ذهى ‪05 .‬‬               ‫ادو‬
                                ‫و‪ 0500‬من ذهب ويقال له‪ 2‬الاسبانية ‪10‬‬

                     ‫ترك ه باشك اولى» وهونباث مسبت منوم‬              ‫ابنج‬


                                   ‫بنجرة ‪ -‬فارسي « ينجره » أي شباك‬


‫العلاملكيير‪--‬فارسي ‪ 2‬بند ‪ 26‬ممنأه عقدة ورباط دعي كذا لانه‬
                                                                              ‫‪0‬‬
                                                           ‫ربط عل السهم‬

 ‫وشاه بندر معناه‬      ‫ىء‬
                       ‫طعلى‬
                          ‫اسفن‬
                             ‫شط ال‬
                                 ‫لمرب‬
                                    ‫اناه‬
                                       ‫ار‪-‬سى « بندر ©مع‬
                                                      ‫فدر‬
                                                        ‫بن‬
                                                               ‫رئيس التجار‬
                                     ‫‪7‬‬                           ‫د‬
                      ‫أي اليوم الخسون‬    ‫مم يونانى ‪65‬‬

 ‫من بند‬    ‫وي او‬          ‫عامية من الايطالية ‪202‬‬     ‫بتذبره ومند بره ل‬

                                            ‫الفارسية مرادفبا راية وعام ولواء‬
 ‫ايطالي مساعدة ‪ 5‬وهو دهن البان نقل من بان العربيية الى لغات‬     ‫‪-‬‬    ‫شين‬


  ‫اوربا ت فمي سنةه‪ | 81‬كتشفوا عاللىمركاب من فح الكيمياونوا امام‬
 ‫‪ 0‬وأطلقوا عليهاسمبعزين مرادفه‬
```


## [2026-09-14T02:33:29.501Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"فنج\\|سفنج\\|إسفنج\" TAD_pages.txt | head; echo \"--- leaf39 full ---\"\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[39])\nEOF"
}
```


### [2026-09-14T02:33:30.605Z] TOOL RESULT

```
215:                                      ‫معنا‬          ‫إمفنج ‪ -‬يوناني ‪5‬‬
2057:              ‫فنجان ‪ -‬فارسي « فنجان وبتكان » وهو قدح صغير من خزف‬
--- leaf39 full ---
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
                                                                ‫اين‬
                                                                  ‫قذ‬
```


## [2026-09-14T02:33:35.957Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\npos=sum(len(l)+1 for l in lines[:214])\nleaf=txt[:pos].count('\\f')\nprint('leaf',leaf)\nt=txt.split('\\f')\nprint(t[leaf])\nEOF"
}
```


### [2026-09-14T02:33:37.430Z] TOOL RESULT

```
leaf 6
‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬
                                                            ‫خرافات وحكابات‬
                                     ‫استبرق ‪ -‬فارسي معناه الديباج الغديظ‬
                                   ‫اسرب ‪ -‬فارسي «سيرب» معناه رصاص‬
        ‫إسطيل واصطيل ‪ -‬لاتيني ‪#‬دااناطهاة معناه مأوى الخيل والدواب‬
‫خا لان | رانم كن من ‪ 807653‬أى ك كب وهلاةطه‪:‬ذا أُخذ وكان‬
 ‫الفلكيون القدماء يعرفون حركة الكوكب مبذه الآلة ويعينورن موضعه‬
                                                             ‫ويعيسون ارتقاعه‬

                       ‫يونالي تاواع ‪ 1015‬معئاه عنصر وأعيل‬     ‫ب‬
                                                                      ‫د‪5‬ي‬
                                                                        ‫‪95‬‬

                    ‫معتأد عله حربية وطائفة سفن‬      ‫اسطول ‪ 8-3‬وناني ‪8‬‬


‫ملدابةمرادفهمودوقابمة‬
                    ‫اسطوانة ‪ 5-3‬فارسي ‪ 0‬أستون « هماه دعامة وقوات ا‬


                                                            ‫ايضا فيالطبيعيات‬
‫نحري جسمه متخلخل‬          ‫اون‬
                            ‫و وه‬
                               ‫ينعصر‬
                                   ‫حه م‬
                                      ‫معنا‬          ‫إمفنج ‪ -‬يوناني ‪5‬‬



‫يوناني وومزمء ‪5‬أمء معناه فى الاصل الملاحظ والمدير وفى عرف‬          ‫انيف‬

                                                 ‫الكنيسة الذي له كل الكبنوت‬
 ‫إسكلة ‪ -‬ايطالي مادء‪ 5‬وهو معدول عن ‪ 38‬أى دراج وبراد به طالسةن‬


‫أ وفى اللاتينية ‪151010111‬قن‪ 5‬معناء مقعد‬   ‫إسكمله ‪7-3‬رى د اسكله »> فنا‬

           ‫معناهشككلورسمووب وزي ولبسة‬             ‫سكيم _‪ -‬يوناقي ‪200‬‬
```


## [2026-09-14T02:33:54.776Z] TOOL CALL #45: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-14T02:33:54.828Z] TOOL RESULT

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


## [2026-09-14T02:34:00.582Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%BE%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D9%86%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/%CF%83%CF%80%CF%8C%CE%B3%CE%B3%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D9%81%D9%86%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D9%81\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 471 verification\" ;\ndone"
}
```


### [2026-09-14T02:34:10.418Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/cba61506a04a00f8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6112c2fd9c14de5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/be81ed742fe3ae5b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d5762e07bacb8f06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec7ae1088daa25e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1350dfbb7ff4bbd5.txt
```


## [2026-09-14T02:34:13.019Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"########## شپش ##########\"; grep -n -A25 \"^Persian\" cba61506a04a00f8.txt | head -60\necho \"########## سپنج ##########\"; head -c 3000 d6112c2fd9c14de5.txt"
}
```


### [2026-09-14T02:34:13.086Z] TOOL RESULT

```
########## شپش ##########
########## سپنج ##########
URL: https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D9%86%D8%AC
FETCHED: 2026-09-14T02:34:03Z
STATUS: 200
TITLE: سپنج - Wiktionary, the free dictionary

سپنج - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Pashto 

 Toggle Pashto subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Declension 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 2.4 
 Further reading 

 Toggle the table of contents 

 سپنج 

 5 languages 

 فارسی 
 Hrvatski 
 Bahasa Indonesia 
 Malagasy 
 Русский 

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

 Pashto
 [ edit ] 

 Etymology
 [ edit ] 

 A loan from English sponge .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /spəŋd͡ʒ/ 

 Noun
 [ edit ] 

 سپنج • ( spanj )  m 

 sponge 

 Declension
 [ edit ] 

 Declension of سپنج 

 singular

 plural

 direct

 سپنج ( spanj ) 

 سپنجونه ( spanjuna ) 

 oblique

 سپنج ( spanj ) 

 سپنجونو ( spanjuno ) 

 vocative

 سپنجه ( spanja ) 

 سپنجونو ( spanjuno ) 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( ʾspnc /⁠aspinǰ⁠/ , “ hospitality; inn ” ) . Cognate with Parthian 𐫙𐫘𐫛𐫏𐫗𐫋 ( ʿspynj , “ hostel, place to stay ” ) and akin to Classical Syriac ܐܫܦܙܟܢܐ ( ʾšpzknʾ , “ majordomo; host ” ) , ܐܫܦܙܐ ( ʾešpezzā , “ lodging, small house ” ) , Jewish Babylonian Aramaic אוּשְׁפִּיזָא ( ʾūšpīzā , “ id. ” ) , Old Armenian ասպ(ա)նջական ( asp(a)nǰakan , “ hospitable; host ” ) , Old Georgian მასპინძელი ( masṗinʒeli , “ host ” ) , Iranian borrowings.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /si.ˈpand͡ʒ/ 

 ( Dari, formal ) IPA ( key ) : [sɪ.pʰänd͡ʒ] 

 ( Dari, formal ) IPA ( key ) : [sɪ.pʰänd͡ʒ] 
 ( Kabuli ) IPA ( key ) : [sɪ.pʰänd͡ʒ] 

 ( Hazaragi ) IPA ( key ) : [si.pʰänd͡ʒ̥] 

 ( Iran, formal ) IPA ( key ) : [se.pʰænd͡ʒ̥] 

 ( Tajik, formal ) IPA ( key ) : [si.pʰänd͡ʒ] 

 Rhymes: -and͡ʒ 

 Readings

 Classical reading ? 

 sipanj

 Dari reading ? 

 sipanj
```


## [2026-09-14T02:34:22.781Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('cba61506a04a00f8.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(t[i:i+2500])\nEOF"
}
```


### [2026-09-14T02:34:24.003Z] TOOL RESULT

```
From Wiktionary, the free dictionary

 See also: سبس and سپس 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: شپش 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 پش ( paš ) ( dialectal , Sistan ) 

 Etymology
 [ edit ] 

 From Middle Persian 𐭮𐭯𐭩𐭱 ( spiš , “ louse ” ) , borrowed from Old Median *spišah , from Proto-Iranian *cwíšah .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʃi.ˈpiʃ/ , /ʃu.ˈpuʃ/ 

 ( Dari, formal ) IPA ( key ) : [ʃɪ.pʰɪ́ʃ] 

 ( Dari, formal ) IPA ( key ) : [ʃɪ.pʰɪ́ʃ] 
 ( Kabuli ) IPA ( key ) : [ʃɪ.pʰɪ́ʃ] 

 ( Hazaragi ) IPA ( key ) : [ʃi.pʰíʃ] 

 ( Iran, formal ) IPA ( key ) : [ʃe.pʰéʃ] 

 ( Tajik, formal ) IPA ( key ) : [ʃä.búʃ] 

 Rhymes: -iʃ , -uʃ 

 Readings

 Classical reading ? 

 šipiš, šupuš

 Dari reading ? 

 šipiš

 Iranian reading ? 

 šepeš

 Tajik reading ? 

 šabuš

 Dari

 شپش 

 Iranian Persian

 Tajik

 шабуш(к) 

 Noun
 [ edit ] 

 شپش • ( šepeš ) ( plural شپش‌ها ) 

 louse 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=شپش&oldid=92301478 "

 Categories : Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
 Persian terms derived from Old Median 
 Persian terms derived from Proto-Iranian 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/iʃ 
 Rhymes:Persian/iʃ/2 syllables 
 Rhymes:Persian/uʃ 
 Rhymes:Persian/uʃ/2 syllables 
 Persian lemmas 
 Persian nouns 
 Persian palindromes 

 Hidden categories: Middle Persian terms with non-redundant manual transliterations 
 Pages with entries 
 Pages with 1 entry 

 This page was last edited on 25 August 2026, at 02:10.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 شپش 

 15 languages 

 Add topic
```


## [2026-09-14T02:34:37.191Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in ec7ae1088daa25e0.txt 1350dfbb7ff4bbd5.txt be81ed742fe3ae5b.txt; do\necho \"############ $f\"\npython3 - \"$f\" <<'EOF'\nimport sys\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(t[i:i+3000])\nEOF\ndone"
}
```


### [2026-09-14T02:34:38.660Z] TOOL RESULT

```
############ ec7ae1088daa25e0.txt
From Wiktionary, the free dictionary

 See also: تفنك 

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 تفک ( tofak ) 

 Etymology
 [ edit ] 

 Borrowed most likely from Chagatai or Khorezmian Turkic and borrowed at least semantically also from Ottoman Turkish تفنك ( tüfenk ) , cognate to Karakhanid [script needed] ( tüwek ) in the Dīwān Luḡāt at-Turk meaning a blowpipe propelling pebbles to kill birds, so called by onomatopoeia mimicking the sound made when it is puffed : Tüf! See Azerbaijani tüfəng for cognates. The terminus ante quem the tüfenk in the meaning of a matchlock -gun has resounded in Persian lands is the end of the Battle of Çaldıran where the Safavids incurred resounding defeat because of the Ottoman use of – then expensive – firearms to devastate the Persians as resolutely as never before because of the new Shia threat .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /tu.ˈfanɡ/ 

 ( Dari, formal ) IPA ( key ) : [t̪ʰʊ.fäŋɡ] 

 ( Dari, formal ) IPA ( key ) : [t̪ʰʊ.fäŋɡ] 
 ( Kabuli ) IPA ( key ) : [t̪ʰʊ.fäŋɡ] 

 ( Hazaragi ) IPA ( key ) : [t̪ʰu.fäŋɡ̥] 

 ( Iran, formal ) IPA ( key ) : [t̪ʰo.fæɲɡʲ̥] 

 ( Tajik, formal ) IPA ( key ) : [t̪ʰu.fäŋɡ] 

 Rhymes: -anɡ 

 Readings

 Classical reading ? 

 tufang

 Dari reading ? 

 tufang

 Iranian reading ? 

 tofang

 Tajik reading ? 

 tufang

 Noun
 [ edit ] 

 تفنگ • ( tufang / tofang ) ( plural تفنگ‌ها ( tufang-hā / tofang-hâ ) , Tajik spelling туфанг ) 

 musket 

 firearm , gun 
 Synonym: اسلحه گرم ( aslahe garm ) 

 Derived terms
 [ edit ] 

 تفنگ‌دار ( tofang-dâr ) , تفنگدار ( tofangdâr ) 

 تفنگچی ( tofangči ) 

 Descendants
 [ edit ] 

 → Bakhtiari: تفنگ ( tofang ) 

 → Bashkardi: 
 Minabi: تفنگ ( tofang ) 

 → Hindustani: 
 Hindi: तुफ़ंग ( tufaṅg ) 
 Urdu: تفنگ ( tufáng ) 

 → Kermanic: 
 Abuzeydabadi: tafang 
 Abyanehi: tofang 
 Hanjani, Yarandi: tefeng 

 → Pashto: تفنگ ( tufáng ) , توپک ( topák ) 

 → Parachi: تفنگ ( tofang ) 

 References
 [ edit ] 

 Vullers, Johann August ( 1855 ), “ تفنگ ”, in Lexicon Persico-Latinum etymologicum cum linguis maxime cognatis Sanscrita et Zendica et Pehlevica comparatum, e lexicis persice scriptis Borhâni Qâtiu, Haft Qulzum et Bahâri agam et persico-turcico Farhangi-Shuûrî confectum, adhibitis etiam Castelli, Meninski, Richardson et aliorum operibus et auctoritate scriptorum Persicorum adauctum ‎ [1] (in Latin), volume I, Gießen: J. Ricker, page 451a 

 Urdu
 [ edit ] 

 A painting of Mughal Emperor Jahangir holding a تفنگ ( tufáng , "gun", "rifle") after slaying a nilgai during a royal hunt. 
 Alternative forms
 [ edit ] 

 توپَک ( topak ) , تُوپَک ( tūpak ) , تُپَک ( tupak ) , تُفَک ( tufak ) 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian تفنگ ( tufang ) , perhaps from Khorezmian Turkic , but more likely via Chagatai through the Mughal Empire whose rulers were initially Chagatai-speaking, and established one of the three " gunpowder empires " alongside the Ottoman Empire and Safavid Iran . The word is its
############ 1350dfbb7ff4bbd5.txt
From Wiktionary, the free dictionary

 See also: بق and تق 

 Arabic
 [ edit ] 

 Verb
 [ edit ] 

 تَفِ • ( tafi ) ( form I ) /ta.fi/ 

 inflection of وَفَى ( wafā ) : 
 second-person masculine singular non-past active jussive 

 third-person feminine singular non-past active jussive 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 From Proto-Iranian , from Proto-Indo-Iranian , from Proto-Indo-European *(s)ptyēw- ( “ to spit, vomit ” ) . Akin to Ossetian ту ( tu , “ spittle ” ) , Sanskrit ष्ठीवति ( ṣṭhīvati , “ to spit ” ) , Armenian թուք ( tʻukʻ , “ spit, spittle ” ) , Serbo-Croatian pljuvati ( “ to spit ” ) , Ancient Greek πτύω ( ptúō , “ to spit out ” ) , Latin spuō ( “ to spit ” ) , English spew .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈtuf/ 

 ( Dari, formal ) IPA ( key ) : [t̪ʰʊf] 

 ( Dari, formal ) IPA ( key ) : [t̪ʰʊf] 
 ( Kabuli ) IPA ( key ) : [t̪ʰʊf] 

 ( Hazaragi ) IPA ( key ) : [t̪ʰuf] 

 ( Iran, formal ) IPA ( key ) : [t̪ʰof] 

 ( Tajik, formal ) IPA ( key ) : [t̪ʰuf] 

 Rhymes: -uf 

 Readings

 Classical reading ? 

 tuf

 Dari reading ? 

 tuf

 Iranian reading ? 

 tof

 Tajik reading ? 

 tuf

 Noun
 [ edit ] 

 تف • ( tof ) 

 spittle , spit 
 Synonym: خیو ( xayu ) 

 Derived terms
 [ edit ] 

 تف کردن ( tof kardan ) 

 تفدان ( tofdân ) 

 Etymology 2
 [ edit ] 

 Related to Old Armenian տապ ( tap , “ heat ” ) , an Iranian borrowing. Related to تب ( tab ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈtaf/ 

 ( Dari, formal ) IPA ( key ) : [t̪ʰäf] 

 ( Dari, formal ) IPA ( key ) : [t̪ʰäf] 
 ( Kabuli ) IPA ( key ) : [t̪ʰäf] 

 ( Hazaragi ) IPA ( key ) : [t̪ʰäf] 

 ( Iran, formal ) IPA ( key ) : [t̪ʰæf] 

 ( Tajik, formal ) IPA ( key ) : [t̪ʰäf] 

 Rhymes: -af 

 Readings

 Classical reading ? 

 taf

 Dari reading ? 

 taf

 Iranian reading ? 

 taf

 Tajik reading ? 

 taf

 Noun
 [ edit ] 

 تف • ( taf ) 

 flame , heat , warmth 

 Derived terms
 [ edit ] 

 تف دادن ( taf dâdan ) 

 References
 [ edit ] 

 Steingass, Francis Joseph ( 1892 ), “ تف ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 

 South Levantine Arabic
 [ edit ] 

 Root 

 ت ف ف 

 1 term 

 Etymology
 [ edit ] 

 Imitative of spitting. Form II means “to utter a тьфу ( tʹfu ) ” (as a common interjection nowadays goes in Russian ).

 Pronunciation
 [ edit ] 

 IPA ( key ) : /taff/ , [taf] 

 Audio ( al-Lidd ) : ( file ) 

 Verb
 [ edit ] 

 تفّ • ( taff ) I ( present بتفّ ( bitiff, bitoff ) ) 

 to spit 

 Usage notes
 [ edit ] 

 The non-past forms of this verb are typically pronounced with the vowel “i” by Palestinians and “u” by Jordanians. [ 1 ] 

 Conjugation
 [ edit ] 

 Conjugation of تف 

 singular

 plural

 1 st person

 2 nd person

 3 rd person

 1 st person

 2 nd person

 3 rd person

 past

 m 

 تفّيت ( taffēt ) 

 تفّيت ( taffēt ) 

 تفّ ( taff ) 

 تفّينا ( taffēna ) 

 تفّيتو ( taffētu ) 

 تفّو ( taffu ) 

 f 

 تفّيتي ( taffēti ) 

 ت
############ be81ed742fe3ae5b.txt
From Wiktionary, the free dictionary

 See also: إسفنج and اسفنجی 

 Gawar-Bati
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Pashto اسفنج or Urdu اسفنج , from Persian اسفنج , Arabic إِسْفَنْج ( ʔisfanj ) , ultimately Ancient Greek σπόγγος ( spóngos ) .

 Noun
 [ edit ] 

 اسفنج ( isfanj ) 

 sponge 

 foam 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: اسفنج 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 سفنج ( sefanj ) , اسپنج ( espanj ) , اسپنگ ( espang ) 

 Etymology
 [ edit ] 

 Etymology tree

 Pre-Greek bor. 
 Ancient Greek σπόγγος ( spóngos ) bor. 
 Arabic إِسْفَنْج ( ʔisfanj ) bor. 
 Persian اسفنج 

 Borrowed from Arabic إِسْفَنْج ( ʔisfanj ) , borrowed from Ancient Greek σπόγγος ( spóngos ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔis.ˈfand͡ʒ/ 

 ( Dari, formal ) IPA ( key ) : [ʔɪs.fánd͡ʒ] 

 ( Dari, formal ) IPA ( key ) : [ʔɪs.fánd͡ʒ] 
 ( Kabuli ) IPA ( key ) : [ʔɪs.fánd͡ʒ] 

 ( Hazaragi ) IPA ( key ) : [ʔis.fánd͡ʒ̥] 

 ( Iran, formal ) IPA ( key ) : [ʔes.fǽnd͡ʒ̥] 

 ( Tajik, formal ) IPA ( key ) : [ʔis.fánd͡ʒ] 

 Rhymes: -and͡ʒ 

 Readings

 Classical reading ? 

 isfanj

 Dari reading ? 

 isfanj

 Iranian reading ? 

 esfanj

 Tajik reading ? 

 isfanj

 Noun
 [ edit ] 

 اسفنج • ( isfanj / esfanj ) ( plural اسفنج‌ها ( isfanj-hā / esfanj-hâ ) , Tajik spelling исфанҷ ) 

 sponge 

 Derived terms
 [ edit ] 

 سنگ اسپنگ ( sang-e espang , “ cystolith ” ) ( in Burhān-i-Qāṭiʿ . [ 1 ] )

 Descendants
 [ edit ] 

 → Hindustani: 
 Hindi: इस्फ़ंज ( isfañj ) 
 Urdu: اِسْفَن٘ج ( isfañj ) 

 References
 [ edit ] 

 ^ Ben xalaf tabrizi, Mohammad Hosayn, Editor: Mohammad Moin, Burhān-i-Qāṭiʿ (برهان قاطع) (In Persian), V:II, Amir Kabir pub., Tehran, 1958 →ISBN 

 Urdu
 [ edit ] 

 Etymology
 [ edit ] 

 Etymology tree

 Pre-Greek bor. 
 Ancient Greek σπόγγος ( spóngos ) bor. 
 Arabic إِسْفَنْج ( ʔisfanj ) bor. 
 Classical Persian اِسْفَنْج ( isfanj ) bor. 
 Urdu اسفنج 

 Borrowed from Classical Persian اِسْفَنْج ( isfanj ) , borrowed from Arabic إِسْفَنْج ( ʔisfanj ) , borrowed from Ancient Greek σπόγγος ( spóngos ) .

 Pronunciation
 [ edit ] 

 ( Standard Urdu ) IPA ( key ) : /ɪs.fənd͡ʒ/ 

 Noun
 [ edit ] 

 اِسْفَن٘ج • ( isfañj )  m ( Hindi spelling इस्फ़ंज ) 

 sponge 

 a yeast dumpling.

 Retrieved from " https://en.wiktionary.org/w/index.php?title=اسفنج&oldid=89719814 "

 Categories : Gawar-Bati terms borrowed from Pashto 
 Gawar-Bati terms derived from Pashto 
 Gawar-Bati terms borrowed from Urdu 
 Gawar-Bati terms derived from Urdu 
 Gawar-Bati terms derived from Persian 
 Gawar-Bati terms derived from Arabic 
 Gawar-Bati terms derived from Ancient Greek 
 Gawar-Bati lemmas 
 Gawar-Bati nouns 
 Persian terms borrowed from Arabic 
 Persian terms derived from a Pre-Greek substrate 
 Persian terms derived from Ancient Greek 
 Persian terms derived from Arabic 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/and͡ʒ 
 Rhymes:Persian/and͡ʒ/2 syllables 
 Persian lemmas 
 Persian nouns 
 Urdu t
```


## [2026-09-14T02:34:51.859Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('d5762e07bacb8f06.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(t[i:i+1800])\nEOF"
}
```


### [2026-09-14T02:34:52.972Z] TOOL RESULT

```
From Wiktionary, the free dictionary

 Ancient Greek
 [ edit ] 

 Alternative forms
 [ edit ] 

 σφόγγος ( sphóngos ) — Attic 

 Etymology
 [ edit ] 

 Together with Latin fungus ( “ mushroom, fungus ” ) and Old Armenian սունկն ( sunkn , “ tree-mushroom ” ) a Mediterranean-Pontic Pre-Greek substrate loanword. [ 1 ] 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /spóŋ.ɡos/ → /ˈspoŋ.ɡos/ → /ˈspoŋ.ɡos/ 

 ( 5 th BCE Attic ) IPA ( key ) : /spóŋ.ɡos/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈspoŋ.ɡos/ 

 ( 4 th CE Koine ) IPA ( key ) : /ˈspoŋ.ɡos/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /ˈspoŋ.ɡos/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈspoŋ.ɡos/ 

 Noun
 [ edit ] 

 σπόγγος • ( spóngos )  m ( genitive σπόγγου , diminutive σπογγῐ́ον ) ; second declension 

 sponge 
 c. 800 BCE – 600 BCE , Homer , Iliad 18.414–415 : σπόγγῳ δ’ ἀμφὶ πρόσωπα καὶ ἄμφω χεῖρ’ ἀπομόργνυ
αὐχένα τε στιβαρὸν καὶ στήθεα λαχνήεντα spóngōi d’ amphì prósōpa kaì ámphō kheîr’ apomórgnu
aukhéna te stibaròn kaì stḗthea lakhnḗenta With a sponge did he wipe both sides of his face and both his hands down,
as well as his stout neck and his shaggy chest 

 ( anatomy ) tonsil 

 Declension
 [ edit ] 

 Second declension of ὁ σπόγγος ; τοῦ σπόγγου ( Attic )

 Case / #

 Singular

 Dual

 Plural

 Nominative

 ὁ σπόγγος 
 ho spóngos 

 τὼ σπόγγω 
 tṑ spóngō 

 οἱ σπόγγοι 
 hoi spóngoi 

 Genitive

 τοῦ σπόγγου 
 toû spóngou 

 τοῖν σπόγγοιν 
 toîn spóngoin 

 τῶν σπόγγων 
 tôn spóngōn 

 Dative

 τῷ σπόγγῳ 
 tōî spóngōi 

 τοῖν σπόγγοιν 
 toîn spóngoin 

 τοῖς σπόγγοις 
 toîs spóngois 

 Accusative

 τὸν σπόγγον 
 tòn spóngon 

 τὼ σπόγγω 
 tṑ spóngō 

 τοὺς σπόγγους 
 toùs spóngous 

 Vocative

 σπόγγε 
 spónge 

 σπόγγω 
 spóngō 

 σπόγγοι 
 spóngoi 

 Notes:

 This table gives Attic inflectional endings. For
```


## [2026-09-14T02:34:53.934Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN tuf ===\"; grep -n \"tuf\\|Speichel\" HRN.txt | head -20\necho \"=== HUB tuf ===\"; grep -n \"tuf\\b\\|Speichel\" HUB.txt | head -10\necho \"=== CHEUNG tuf/spit ===\"; grep -n -i \"to spit\\|θwais\\|spit'\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T02:34:54.022Z] TOOL RESULT

```
=== HRN tuf ===
521:a sei durch ab beeinflusst, während is Abstufung des
619:Zu arm. orc 'Speichel, Erbrochenes*, orcam erbrechen,
2755:281. päl^ pä Tuss ; vergl. paye 'Stufe', päym.
2756:aw. päda- 'Puss* ; phlv. pCLT *Fuss', päyah *Stufe' ; ai.
3658:390. fü/ 'Speichel*, tufek{'% dehen)^ tiifke (Gazoph. s. v.
3659:saliva), tufü, tuh, tuhü,
3661:III, 34; Studien II, 42); got. speivan; arm. tüiß 'Speichel';
3663:kurd. tef 'Speichel', tiw, tuw^ tu, tiik 'Spucken,
3664:Speichel*; afy. tu, tük, tükal spucken*; oss. ft* (251);
3665:wa;^. tuf cerak, sar. tu ceigao 'spucken'.
4663:517. x^?/'^» yJ^ 'Speichel', ylin (Gazophyhicium s. v.
7568:der schwachen Wurzelstufe, Bartholomae, ib. 367
9811:Zwischenstufe ag(g)uru zwischen agru und *((ngarif.
11083:196. tuf/ 'stark, Held', takik (für aw. ta/ma-)^ takikth,
=== HUB tuf ===
=== CHEUNG tuf/spit ===
12820:Oss. D. lixsun/lixst ‘to spit’, ? Wa. rox(n) ‘excrements; defecating' || (+ *aua-) Sariq. 
19464:*KHOTANESE: (+ *nis-) LKh. naspul- ‘to hiss’ or ‘to spit’ {hapax}. Ф Khot. pulafii 
26065:*PARTHIAN: ? wf- ‘to spit’. Ò Differently Ghilain (l.c.), who connects the Pth. form 
27042:«PIE *uemH;- ‘to vomit, to spit out’? => LIV: 680 | Pok.: 1146
```


## [2026-09-14T02:34:58.614Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3650,3672p' HRN.txt"
}
```


### [2026-09-14T02:34:58.663Z] TOOL RESULT

```
kurd. ti, tmi; afy. tami; bei. tminacj, tünag, n. ftmi
'durstig, fun 'Durst' (396); wa/. tax, ^^'/^j sar. tür^
tiirt, si/n. täsna, täsnagl, yidg. triisna.
389. fest 'Becken, Untertasse*, teste, arab. LW. ^as^
aw. tasta^ Schaale, Tasse'; phlv. tast, arm. LW.
tust, tastak,
afy. LW. tust, bei. LW. ^äs (270), aus arab. tas^);
§i/n. sar. tödö (^tastaka-),
390. fü/ 'Speichel*, tufek{'% dehen)^ tiifke (Gazoph. s. v.
saliva), tufü, tuh, tuhü,
ai. i/^sthlv-, sthivati (vergl. Bartholomae, Ar.Forsch.
III, 34; Studien II, 42); got. speivan; arm. tüiß 'Speichel';
lat. spuö; gr. nzvo).
kurd. tef 'Speichel', tiw, tuw^ tu, tiik 'Spucken,
Speichel*; afy. tu, tük, tükal spucken*; oss. ft* (251);
wa;^. tuf cerak, sar. tu ceigao 'spucken'.
891. tek 'schnell, Lauf, tekiden, tekT,
aw. taka^ 'Lauf "'^) ; zu V^tak-, tac- wie ta/ten (No. 368).
(Metr. Hezej)
juz medh-^ fU terhencU büved Iierci nüvesem
her dem qel^i ez yäfe ü terkende sUceste Sözenl.
*) Hieraus auch arm. tas, ital. tazza, franz. lasse, nhd. Tasse
(Hübsohmann, ZDMG. 35, 129).
```


## [2026-09-14T02:35:07.230Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"شپش\" \"سپنج\" \"اسفنج\" \"تفنگ\"; do echo \"=== ARY $w ===\"; grep -n \"$w\" incoming/ARY/ARY_pages.txt | head -5; done\necho \"=== ARY تف ===\"; grep -n \"^تف\\b\\|تف :\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== ARY latin index ===\"; grep -n -i \"SPYEU\\|SPONGO\\|SPIS\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T02:35:08.368Z] TOOL RESULT

```
=== ARY شپش ===
9033:شک (به چم "*تخم شپش!") / ۳۰۷
=== ARY سپنج ===
=== ARY اسفنج ===
=== ARY تفنگ ===
13289:چم این واژه در زبان هلندی: ته تفنگ. ۰
=== ARY تف ===
48:تفریباً همه‌ی زبانهای اروپا و فلات ایران و بخش شمالی شبیه قاروی هند می‌شود. کوچگری
1019:تفریبی مشخص می‌کنند. ۱ :
5820:تف» تفت» تفتان» تافتن» نفسیدن / ۱۹۹
=== ARY latin index ===
```


## [2026-09-14T02:35:09.298Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN louse/spit ===\"; grep -n \"LOUSE\\|SPIT\\b\" SYN.txt | head -10\necho \"=== IEC spuuo ===\"; grep -n \"^spuuo\\|spuuo (\" IEC.txt | head -5\necho \"=== NYB spis ===\"; grep -n -i \"spis\\|spi§\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T02:35:09.391Z] TOOL RESULT

```
=== SYN louse/spit ===
6803:4.56 SPIT (vb.)
=== IEC spuuo ===
=== NYB spis ===
793:(Mx 158’; 71% an unexplained vb. ajihašn), Skr. v. nindä; from Olr *ava-vaina- (v. ditan) ‘to look down on, to despise a p.’, whence, through syncope, *avvén > üvén- (or possibly, through haplology, avén-), or, with contraction, 6-vén- attested DkM 4761: ^wwynytn! = dvénitan, opp. bur- ž(ēn)ītan (Cod. K 43, fol. 179 v., adds here another dictum: hdn i apoxsäyisn nē Pwwynin' =] övenisn u hàn i ūvēnišn nē buržišn ‘he who is to be shown mercy shall not be disgraced, and he who is to shall not be praised’). Henning paved the way for the correct understanding by pointing to the MPrth vb. ’bwyn- ‘to blame’ < *apa-vaina- (Iranistik 99, n. 1), which is, however, only a synonym of, but not formally iden- tical with, āvēn-. — This vb. must thus be carefully distinguished from forms with a- privativum + ven-: a-venisneh DkM 110? as opposed to venisn ‘the act of seeing’; Paz. avinasni 1. < -ik, kr v. adrsya, 2. < -čh: adrsyatva, SGV VIII, 28—34.
```


## [2026-09-14T02:35:12.541Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6803,6850p' SYN.txt"
}
```


### [2026-09-14T02:35:12.594Z] TOOL RESULT

```
4.56 SPIT (vb.)
Grk.  rriw Goth. speiwan Lith. spiauti NG ss griw ON hrekja, spyta Lett. spl/aut Lat. spuere Dan. spyite ChSl.  pljtvati It. spulare Sw. spotta SCr.  pljuvati Fr. cracher OE sp@lan, hr@can, spyt- Boh. _ plivati Sp. escupir tan Pol. plué Rum.  scuipa ME spete, spite (reche) Russ. plevat’ Tr. saile (sb.) NE spit Skt. sthiv- NIr.  sailighim Du. spuwen Av. spama- (sb.) W. poert OHG = spiwan
Br. skopa, tufa MHG spi(w)en
NHG  speien, spucken
The majority of the words for ‘spit’ are of imitative origin, and most of these belong to an inherited group, which, though partly affected by new imitative associations, clearly reflect an IE ex- pression.
1. IE *spyéu-, spyu-, etc. Most of the forms included here are derivable by regular phonetic processes from init. *spy-, but some owe their form to new associations. Walde-P. 2.683. Ernout- M. 969.
Grk. rriw, NG pop. drive, drs, $7; Lat. spuere, frequent. sputare (> It. spu- tare, OF r. espuer); Goth. speiwan, Du. spuwen, OHG spiwan, spian, MHG spi(w)en, spiien, NHG speien (in the older language also ‘spew, vomit’, as chiefly OE spiwan, ON spyja, cf. 4.57), ON spyta, Dan. spytte, Sw. spotta, OE spyt- tan, ME spitte, NE spit, OE spztan, ME spete, NHG spucken (Weigand-H. 2.936, Falk-Torp 1187, 1138); Lith. spiauti, Lett. spl’aut; ChSl. plyivati, etc., general
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
or THE B sniv-, sft (Av. spammer
m. tk‘anem. tive *krak,
OFr. escopir (> Br. sko- qa (Maced.-Rum. ascu- h disputed, but prob. fr. mh VLat deformation (with metathe- a ie sc-p) of Lat. conspuere (cf. a Ra _ REW 8014. Puscariu
566. - ce Ir. saile, N saliva ‘spittle’. denom. NIr. sez guage vb. ‘spit’ ren
escupi,
Sp.
P Mi acy muc
Ir. seile ‘spittle’, fr. Lat. Pedersen 1.211. Hence lighim, but in older lan- dered by locutions
Digitized by Arya Samaj Foundation Chennai and eGangotri
ODY; BODILY FUNCTIONS AND CONDITIONS 265
as do-biur (fo-cerdim, laim, etc.) mo saile, and commonly also NIr. gabhaim (cui- rim, caithim) mo sheile lit. ‘put (cast, etc.) my spit’.
W. poeri (poer sb.), orig.?
Br. skopa, fr. OF r. escopir (above, 2). Henry 243.
Br. tufa, prob. of imitative orig. Henry 274.
4. ON hrekja, OE hrécan, ME reche (NE retch, reach), also ‘hawk, clear the throat’ (as mostly OHG rachisén, MHG rdchsenen) : OE hr&ca, ON hraka ‘spit- tle’, OF hraca, OHG rahho ‘throat’, etc., all of imitative orig. (cf. Skt. kharj- ‘creak’, etc.). Walde-P. 2.415. Falk- Torp 381, 867.
4.57 VOMIT (vb.)
thw Goth. Lith. vemti a rd ON spyja Lett. vert — Lat.  vomere Dan.  Obrekke sig ChSl. bljtvatt It. vomilare, recere Sw. krakas SCr.  bljuvatt Tr. vomir OE spiwan Boh.  ddviti, blitz Sp. _ vomitar ME spewe (vomyte) Pol. womttowaé Rum. vdrsa, vomita NE vomit, spew Russ.  blevat', izrygat’ Ir. scéim Du. braken Skt. vam-, chrd- Nir.  scéithim OHG (ar)spiwan Av. vam- W. —cyfogi, chwydu MHG spiwen, (sich brechen) Br.  c’houeda, dislonka NHG _ sich (er)brechen
Beside the usual word for ‘vomit’, generally avoided in polite speech, there ate in most of the modern languages a number of euphemistic expressions corre- sponding to NE throw up, as Dan. kaste a Sy. kasta upp, NHG auswerfen, Boh. whnouli, Pol. womitowaé etc., or ‘re- lect, give back, cai rendre (la gorge), Pecially in Slayi T. povraciti,
tear, pull out? Such | out
t
‘ ay " Tecere in oo vomit’, a ‘ ntrast ;
Te not Included in the list a rape
CC-0. In Public Domain. Gu
1. IE *wem-. Walde-P. 1.262f. Er- nout-M. 1133 f.
Grk. éuéw; Lat. vomere (> Fr. vomir; Lat. frequent. vomitare > It. vomitare, Sp. vomitar, Rum. vomita); Lith. vemti, Lett. vemt; Skt., Av. vam-.
2. NG tepvd, fr. Grk. é-epaw ‘evacu- ate (by purge or vomit)’, ‘disgorge’ (-epaw only in cpds., cf. ax-epaw ‘pour out a fluid’, etc.), fr. the root in Skt. rasa- ‘sap, fluid’, Lat. rds ‘dew’, ete. Walde- P. 1.149. Hatzidakis, Mec. 1.292.
3. It. recere, fr. Lat. reicere ‘throw back’ (¢acere ‘throw’). REW 7183.
Rum. vdrsa (and refl. se vdrsa), lit. ‘pour’ (= Fy. verser, etc.), fr. Lat. ver- sare ‘turn’. REW 9242. Puscariu 1861.
rukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
266 SELECTED INDO-EUROPEAN SYNONYMS
4. Ir. scéim, NIr. scéithim (fr. vbl. n. sceith), W. chwydu, Br. c’houeda, c’houedi : ON skiia, OE scitan, NE shit, etc. (4.66), fr. extensions of IE *skei- ‘di- vide, separate’, in Skt. chyati ‘cuts off’, Lat. sctre ‘know, decide’ (orig. ‘sepa- rate’), etc. Walde-P. 2.541 f. Pedersen 1.77.
W. cyfogi, prob. cpd. cyf-ogi : MBr. heugel ‘belch’, Br. heug ‘aversion, repug- nance’, perh. orig. imitative (cf. glottal contraction as NE hic). Henry 162.
Br. dislonka, lit. ‘un-swallow’, epd. of lonka : W. llyncu, Ir. slucim ‘swallow’ Walde-P.: 2.711. Pedersen 1.151.
5. ON spyja, OF spiwan, ME spewe, NE spew, OHG spiwan, arspiwan, MHG spiwen, spien, see under ‘spit’, 4.56.
Dan. brekke sig, fr. LG stk braken = MHG sich brechen (once ‘vomere’ in Lexer s.v.), NHG sich (er)brechen (cf. OE brecan, refl. ‘retch, hawk’), lit. ‘break one’s self’. Falk-Torp 110.
Sw. krdkas of imitative orig. Hellquist 518.
NE vomit, late ME vomyte, either fr. the sb. (quotable somewhat earlier), this fr. OFr. vomit(e), Lat. vomitus, or
directly fr. an OFr. form of Lat. VOMItare (above, 1). NED s.v.
Du. braken : breken ‘break’ (= NHG brechen, etc., above). Franck-y, W. 89.
```


## [2026-09-14T02:35:21.093Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://www.etymonline.com/word/sponge\" \"https://www.etymonline.com/word/fungus\" \"https://www.etymonline.com/word/spit\" \"https://www.etymonline.com/word/sputter\"; do python3 tools/fetch_source.py \"$u\" --note \"page 471: Spongo / Spyeu entries\"; done"
}
```


### [2026-09-14T02:35:23.412Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/db3cdd7b321a3da5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94cc1a17e8156231.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7a1ad2ba51e8b140.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c13e702b6fa993b5.txt
```


## [2026-09-14T02:35:25.399Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor idx in [27064]:\n    ctx='\\n'.join(lines[idx-40:idx+3])\n    cols=re.findall(r'\\b1[5-8]\\d\\d\\b',ctx)\n    print('cols near:',cols[-12:])\nprint('---')\n# leaf\npos=sum(len(l)+1 for l in lines[:27063])\nprint('leaf',t[:pos].count('\\f'))\nEOF\necho \"=== HRN leaf for 390 ===\"\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:3657])\nleaf=t[:pos].count('\\f')\nprint('leaf',leaf,'printed p',leaf-21)\npos2=sum(len(l)+1 for l in lines[:6178])\nleaf2=t[:pos2].count('\\f')\nprint('sipanj/spis leaf',leaf2,'printed p',leaf2-21)\nEOF"
}
```


### [2026-09-14T02:35:26.432Z] TOOL RESULT

```
cols near: ['1626']
---
leaf 886
=== HRN leaf for 390 ===
leaf 108 printed p 87
sipanj/spis leaf 177 printed p 156
```


## [2026-09-14T02:35:35.320Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in db3cdd7b321a3da5 94cc1a17e8156231 7a1ad2ba51e8b140 c13e702b6fa993b5; do echo \"##### $f\"; python3 - $f.txt <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('Advertisement')\nseg=t[:6000]\n# crude: find the definition block\nm=re.search(r'(?s)(\\(n\\.\\)|\\(v\\.\\)).{0,1400}', t[t.find('TITLE:'):])\nprint(m.group(0)[:1400] if m else seg[:1200])\nEOF\ndone"
}
```


### [2026-09-14T02:35:36.535Z] TOOL RESULT

```
##### db3cdd7b321a3da5
(n.) 

 Old English sponge , spunge , "absorbent and porous part of certain aquatic organisms," from Latin spongia "a sponge," also "sea animal from which a sponge comes," from Greek spongia , which is related to spongos "sponge," which is of unknown origin; Beekes calls it "an old Wanderwort." "Probably a loanword from a non-IE language, borrowed independently into Greek, Latin and Armenian in a form *sphong- " [de Vaan]. The Latin word is the source of Old Saxon spunsia , Middle Dutch spongie , Old French esponge , Spanish esponja , Italian spugna .

 In English the word is used in reference to the marine animal from 1530s; of any sponge-like substance from c. 1600. Figurative use in reference to one who absorbs without discrimination is by c. 1600. The meaning "one who persistently and parasitically lives on others" is by 1838 (compare the verb, and see sponger ).

 To throw in the sponge "quit, submit" (1860) is from prizefighting, in reference to the sponges used to cleanse the faces of combatants between rounds (compare later throw in the towel ). Sponge-cake , light and sweet, is attested by 1801, so called for its substance.

 sponge (v.) 

 late 14c., spongen , "to soak up with a sponge," also (transitive) "to cleanse or wipe with a sponge," from sponge (n.) and perhaps in part from Latin spongiare . The intransitive sense "dive for sponges, gather sponges where they g
##### 94cc1a17e8156231
(n.) 

 1520s, "a mushroom," from Latin fungus "a mushroom, fungus;" used in English at first as a learned alternative to mushroom ( funge was used in this sense late 14c.). The Latin word is believed to be cognate with (or derived from) Greek sphongos , the Attic form of spongos "sponge" (see sponge (n.)). "Probably a loanword from a non-IE language, borrowed independently into Greek, Latin and Armenian in a form *sphong- ...." [de Vaan]
 also from 1520s 

 Entries linking to fungus 

 sponge (n.) 

 Old English sponge , spunge , "absorbent and porous part of certain aquatic organisms," from Latin spongia "a sponge," also "sea animal from which a sponge comes," from Greek spongia , which is related to spongos "sponge," which is of unknown origin; Beekes calls it "an old Wanderwort." "Probably a loanword from a non-IE language, borrowed independently into Greek, Latin and Armenian in a form *sphong- " [de Vaan]. The Latin word is the source of Old Saxon spunsia , Middle Dutch spongie , Old French esponge , Spanish esponja , Italian spugna .

 In English the word is used in reference to the marine animal from 1530s; of any sponge-like substance from c. 1600. Figurative use in reference to one who absorbs without discrimination is by c. 1600. The meaning "one who persistently and parasitically lives on others" is by 1838 (compare the verb, and see sponger ).

 To throw in the spo
##### 7a1ad2ba51e8b140
(v.)).

 Not the usual Old English word; spætlan (see spittle ) and spiwan are more common; all are considered to be from the same root. To spit (especially at someone) as a gesture of contempt is in Old English. Related: Spat ; spitting . Also compare spitting image .

 spit (n.1) 

 [saliva], early 14c., "fluid secreted by the glands of the mouth," from spit (v.1). By 1650s as "an act of spitting."

 The meaning "the very likeness, exact image" in modern use is attested from 1805 (compare spitting image , under the verb); compare French craché in same sense. Spit-curl , "lock of hair curled and lying flat on the temple" (1831), was originally colloquial or vulgar. The military phrase spit and polish indicating precise correctness (often derogatory) is recorded by 1895.
 also from early 14c. 

 spit (n.2) 

 [sharp-pointed rod or bar for roasting meat], late Old English spitu "a spit" in cooking, from Proto-Germanic *spituz , (source also of Middle Dutch and Dutch spit , Swedish spett (which perhaps is from Low German), Old High German spiz , German Spieß "roasting spit," German spitz "pointed" (from PIE *spei- "sharp point;" see spike (n.1)).

 This is also the word meaning "sandy point or long, narrow shoal running from a shore into a sea" (1670s). Old French espois , Spanish espeto "spit," Italian spiedo , spiede "a spear" are Germanic loan-words.

 spit (v.2) 

 [put on a 
##### c13e702b6fa993b5
(v.) 

 1590s, "emit in small amounts or flashes, spit with explosive sounds," cognate with Dutch sputteren , West Frisian sputterje , from Proto-Germanic *sput- (see spout (v.)).

 The meaning "speak rapidly and vehemently, seem to spit words, utter with spit flying" is from 1670s. Related: Sputtered ; sputtering . The noun is attested from 1670s, "noisy and confused talk," by 1837 as "act of sputtering."
 also from 1590s 

 Entries linking to sputter 

 spout (v.) 

 "issue forcibly; spit out" as a liquid, early 14c., spouten , a common Germanic word, ultimately imitative, related to Middle Dutch spoiten "to spout" (Dutch spuiten "to flow, spout"), North Frisian spütji "spout, squirt," Swedish sputa "to spout," from Proto-Germanic *sput- (from PIE *sp(y)eu- "to spew, spit;" see spew (v.)).

 The colloquial meaning "to talk, declaim, speak volubly" is from 1610s; the dismissive sense of "make great, lengthy speeches of little matter" is by 1756. Related: Spouted ; spouting .

 splutter (n.) 

 1670s, "bustle, confusion, noise, fuss," perhaps a variant of sputter , intensified by the consonant cluster of splash , splatter , etc.

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 scramble 

 1580s (intransitive), "make one's way by clambering, etc., struggle or wriggle along," also "strive with others o
```


## [2026-09-14T02:35:44.921Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('7a1ad2ba51e8b140.txt',encoding='utf-8').read()\ni=t.find('spit (v.1)')\nprint(t[i-200:i+900])\nEOF"
}
```


### [2026-09-14T02:35:46.022Z] TOOL RESULT

```
 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of spit 

 spit (v.1) 

 [expectorate] Old English spittan (Anglian), spætan (West Saxon), "expel (saliva) from the mouth," transitive and intransitive, past tense *spytte , from Proto-Germanic *spitjan , from PIE *sp(y)eu- (of imitative origin; see spew (v.)).

 Not the usual Old English word; spætlan (see spittle ) and spiwan are more common; all are considered to be from the same root. To spit (especially at someone) as a gesture of contempt is in Old English. Related: Spat ; spitting . Also compare spitting image .

 spit (n.1) 

 [saliva], early 14c., "fluid secreted by the glands of the mouth," from spit (v.1). By 1650s as "an act of spitting."

 The meaning "the very likeness, exact image" in modern use is attested from 1805 (compare spitting image , under the verb); compare French craché in same sense. Spit-curl , "lock of hair curled and lying flat on the temple" (1831), was originally col
```


## [2026-09-14T02:35:56.389Z] TOOL CALL #60: Bash

```json
{
 "command": "pdftoppm -f 471 -l 471 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg471 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg471.png"
}
```


### [2026-09-14T02:35:58.085Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 73795 Sep 13 22:35 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg471.png
```


## [2026-09-14T02:36:00.153Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg471.png"
}
```


### [2026-09-14T02:36:00.689Z] TOOL RESULT

```

```


## [2026-09-14T02:36:00.665Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:36:14.266Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg471.png data/verification/sources/refs/ocr/BOOK/471.png\ncd data/verification/sources/refs\npython3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [219,568]:\n    pos=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=t[:pos].count('\\f')\n    print('line',ln,'leaf',leaf,'printed p',leaf-21)\nEOF"
}
```


### [2026-09-14T02:36:15.372Z] TOOL RESULT

```
line 219 leaf 34 printed p 13
line 568 leaf 101 printed p 80
```


## [2026-09-14T02:36:24.404Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:13707])\nleaf=t[:pos].count('\\f')\nprint('leaf',leaf,'printed pages ~',2*(leaf-15),2*(leaf-15)+1)\nprint(lines[13707][:400])\nEOF"
}
```


### [2026-09-14T02:36:25.575Z] TOOL RESULT

```
leaf 558 printed pages ~ 1086 1087
pstuio (pstiuio, psth-) ‘spit’. Cf. spuuo, ið. Onomat. WP II, 683 Skt. sthivami, pp: sthyütah, id.; Hind. cf. thuk, s. id.; Per. tuff, s. id.; Oss. tü, s. id.; Arm. t'uK, gs: tko, o-st. id.; t'Knem, v. id.; Gk. ptáo, v. id.; Alb. pshtyj, v. id.; Br. cf. tufa, v. id.
```


## [2026-09-14T02:36:41.842Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^spiuo\\|^speiuo\\|^spuuo\\|spuuo\\|^ptu\" IEC.txt | head -10\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaf517 sample:'); print(t[517][:200])\nEOF"
}
```


### [2026-09-14T02:36:42.973Z] TOOL RESULT

```
13708:pstuio (pstiuio, psth-) ‘spit’. Cf. spuuo, ið. Onomat. WP II, 683 Skt. sthivami, pp: sthyütah, id.; Hind. cf. thuk, s. id.; Per. tuff, s. id.; Oss. tü, s. id.; Arm. t'uK, gs: tko, o-st. id.; t'Knem, v. id.; Gk. ptáo, v. id.; Alb. pshtyj, v. id.; Br. cf. tufa, v. id.
leaf517 sample:
Lat. pesna, f. ‘feather, wing’; Ir. (?) eathar, m. ('ship'. Cf. ‘pinnace’ for sense); (oblique form in) MIr. én, m. ‘bird’; OBr. cf. hataned, pl. (feathers', w. “false? h-) beside atan-oc, adj. ‘winge
```


## [2026-09-14T02:36:53.669Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:699])\nleaf=t[:pos].count('\\f')\nprint('leaf',leaf,'printed p',leaf-8)\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d.get('VOP'),ensure_ascii=False)[:500])\"\ngrep -n \"VFO\" /home/sfmqrb/git/rishe/data/verification/sources/MISSING_REFERENCES.md"
}
```


### [2026-09-14T02:36:54.694Z] TOOL RESULT

```
leaf 41 printed p 33
{"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google 
110:| VFO | (unresolved abbreviation, probably = VOP) | skipped | — |
```


## [2026-09-14T02:37:00.573Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:6802])\nleaf=t[:pos].count('\\f')\nprint('SPIT leaf',leaf,'printed p',leaf-24)\nEOF\ngrep -n \"LOUSE\" SYN.txt | head -5"
}
```


### [2026-09-14T02:37:01.724Z] TOOL RESULT

```
SPIT leaf 302 printed p 278
```


## [2026-09-14T02:37:05.295Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:37:05.346Z] TOOL RESULT

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


## [2026-09-14T02:37:07.633Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:37:07.687Z] TOOL RESULT

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


## [2026-09-14T02:42:44.373Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-471.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SEPESH = \"https://en.wiktionary.org/wiki/%D8%B4%D9%BE%D8%B4\"\nW_SEPANJ = \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D9%86%D8%AC\"\nW_ESFANJ = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%AC\"\nW_SPONGOS = \"https://en.wiktionary.org/wiki/%CF%83%CF%80%CF%8C%CE%B3%CE%B3%CE%BF%CF%82\"\nW_TOFANG = \"https://en.wiktionary.org/wiki/%D8%AA%D9%81%D9%86%DA%AF\"\nW_TOF = \"https://en.wiktionary.org/wiki/%D8%AA%D9%81\"\nE_SPONGE = \"https://www.etymonline.com/word/sponge\"\nE_FUNGUS = \"https://www.etymonline.com/word/fungus\"\nE_SPIT = \"https://www.etymonline.com/word/spit\"\nE_SPUTTER = \"https://www.etymonline.com/word/sputter\"\n\ndoc = {\n \"pdf_page\": 471,\n \"book_page\": 441,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Spiš\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Avestan spiš- n. 'louse' (Vd. 17.3); Proto-Iranian *cwiš-/*spiš-\",\n \"note\": (\"The word and the language label are right: Bartholomae's Altiranisches Wörterbuch has \"\n          \"'j. spiš- n. \\\"Laus, Milbe (od. dgl.)\\\"', attested only in Vendidad 17.3 (the xrafstra \"\n          \"'which men call spiš, which eats the grain in the granaries and the clothes in the \"\n          \"wardrobes'), with the note 'mp. spiš, sfuš, np. supuš'. The GLOSS is what is wrong: \"\n          \"spiš- is specifically 'louse', not 'flea' (Av. for 'flea' is not this word; NP for flea \"\n          \"is kayk/keyk). Nourai's own source, Mo'in's footnote in Borhan-e Qate' p.1249, says the \"\n          \"same: 'پهلوی نیز spiš، در بند ۳ فرگرد ۱۷ وندیداد دو گونه شپش یاد شده' and then defines the \"\n          \"Persian word as the blood-sucking parasite of dirty human bodies. Modern work \"\n          \"(Wiktionary, after Hasandust) reconstructs Proto-Iranian *cwíšah and treats NP šepeš as \"\n          \"an Old Median form *spišah taken into Persian — which is why it has sp-/šp- and not the \"\n          \"Persian reflex; Avestan spiš- is then strictly the cognate rather than the ancestor. \"\n          \"Verdict plausible: right etymon and right chain, wrong gloss.\"),\n \"note_fa\": (\"ریشهٔ اوستایی spiš- «شپش» واقعی است و بارتولومه (ستون ۱۶۲۶) آن را تنها از بند ۳ فرگرد ۱۷ \"\n             \"وندیداد آورده است: جانور موذی‌ای که «مردم آن را spiš می‌نامند» و غلهٔ انبارها و جامهٔ \"\n             \"گنجه‌ها را تباه می‌کند. اما معنایی که نورایی داده («کک/flea») نادرست است؛ معنی دقیق آن \"\n             \"«شپش» است و کک در فارسی واژهٔ دیگری (کیک) دارد. معین نیز در حاشیهٔ برهان قاطع (ص ۱۲۴۹) \"\n             \"همین را می‌گوید و شپش را انگل خون‌خوار تن آدمی می‌داند. پژوهش امروزی ایرانی باستان *cwíšah \"\n             \"را بازسازی می‌کند و صورت فارسی نو را وام از گونهٔ مادی *spišah می‌شمارد؛ پس اوستایی spiš- \"\n             \"به‌دقت «هم‌ریشه» است نه «نیای» آن. داوری: ادعای نورایی با احتیاط پذیرفتنی است، جز در معنا.\"),\n \"sources\": [W_SEPESH],\n \"ref_check\": [\n   {\"ref\": \"BQT:1249\", \"status\": \"supports\",\n    \"note\": (\"Borhan-e Qate' (Mo'in) p.1249 = BQT_v3_pages.txt leaf 39 ([pdf page 40], printed \"\n             \"1249 = pdf+1209): headword «شپش» with Mo'in's footnote 13 'šapeš — spiš، پهلوی نیز \"\n             \"spiš، در بند ۳ فرگرد ۱۷ وندیداد دو گونه شپش یاد شده: یکی آنکه درانبار گندم افتد و دیگر \"\n             \"آنکه جامه را تباه کند'، plus the dialect forms 'خوانساری espizh، تهرانی shipish'. \"\n             \"Exactly Nourai's Avestan→Pahlavi→Persian chain — but Mo'in's gloss is 'louse'.\")}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. ~1626 s.v. spiš- (BRT.txt line 27064)\", \"stance\": \"partial\",\n    \"note\": \"'j. spiš-? n. \\\"Laus, Milbe (od. dgl.)\\\" ... yim masyāka spiš nąma aojaite ... V.17.3' + 'mp. spiš, sfuš, np. supuš' — confirms the word and the chain, contradicts the gloss 'flea'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 705, p. 156\", \"stance\": \"partial\",\n    \"note\": \"'705. supuš, uspuš \\\"Laus\\\", šipuš (etc.) ... aw. spiš \\\"Laus\\\"; phlv. spiš (vd. 17 (8)), spuš (AV.); kurd. sipi, aspe \\\"Laus\\\"; afγ. spaža; oss. sis' — same chain, gloss 'Laus' = louse.\"},\n   {\"src\": \"PHD\", \"where\": \"leaf 101 (≈ p.80) s.v. spiš\", \"stance\": \"partial\",\n    \"note\": \"MacKenzie: 'spiš [spyš | (N šipiš)] louse.' — the Pahlavi form and the NP outcome, glossed 'louse' not 'flea'.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt l.84199 s.v. شپش\", \"stance\": \"partial\",\n    \"note\": \"'شپش: [- اشپش] (ا.) (جان.) حشره‌ای از راستهٔ نیم‌بالان که به علت زندگی انگلی فاقد بال شده ... شپش انگل انسان است' — louse; also lists the variant اشپش that Nourai prints.\"},\n   {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep spiš/spyš\", \"stance\": \"silent\",\n    \"note\": \"Nyberg's Pahlavi glossary has no entry for spiš (the word does not occur in his texts).\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"spiš\", \"verdict\": \"plausible\",\n \"derivation\": (\"Middle Persian spiš (Book Pahlavi spyš) continues Old Iranian *spiš- unchanged: a \"\n   \"monosyllabic i-stem with no intervocalic consonant to lenite, so Av. spiš- and MP spiš are \"\n   \"formally identical. MacKenzie's Concise Pahlavi Dictionary gives 'spiš [spyš | (N šipiš)] \"\n   \"louse', and Horn (no. 705) cites 'phlv. spiš (vd. 17(8)), spuš (AV.)' — the second form, with \"\n   \"u from the labial environment, is the one that feeds NP supuš/šupuš. The gloss in the chart, \"\n   \"'flea', is wrong: every source glosses MP spiš 'louse' (Pahlavi for 'flea' is kayk).\"),\n \"derivation_fa\": (\"فارسی میانه spiš (به خط پهلوی spyš) دنبالهٔ بی‌تغییر ایرانی باستان *spiš- است؛ چون \"\n   \"واژه تک‌هجایی است و هیچ همخوان میان‌واکه‌ای ندارد که نرم شود، صورت اوستایی و پهلوی یکی مانده است. \"\n   \"مکنزی آن را «spiš شپش» ضبط کرده و هرن (شمارهٔ ۷۰۵) گونهٔ spuš را هم از ارداویراف‌نامه می‌آورد که \"\n   \"خاستگاه supuš/šupuš فارسی است. معنای «کک» در نمودار نادرست است؛ همهٔ منابع آن را «شپش» معنی کرده‌اند.\"),\n \"sources\": [W_SEPESH],\n \"ref_check\": [\n   {\"ref\": \"BQT:1249\", \"status\": \"supports\",\n    \"note\": \"Mo'in's footnote on p.1249 writes 'پهلوی نیز spiš' next to the Avestan citation — precisely this arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"leaf 101 (≈ p.80)\", \"stance\": \"partial\",\n    \"note\": \"'spiš [spyš | (N šipiš)] louse' (and the English index, PHD.txt l.2677: 'louse spiš.') — form right, gloss 'louse'.\"},\n   {\"src\": \"NYB\", \"where\": \"vol. II glossary, grep 'spiš'\", \"stance\": \"silent\",\n    \"note\": \"no entry; Nyberg's glossary covers only the texts he edits.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 705, p. 156\", \"stance\": \"supports\",\n    \"note\": \"'phlv. spiš (vd. 17 (8)), spuš (AV.)'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"šepeš «شپش»\", \"verdict\": \"plausible\",\n \"derivation\": (\"NP شپش šepeš (classical šipiš/šupuš, Tajik šabuš) comes from MP spiš by the normal \"\n   \"New Persian breaking of an initial sp- cluster with an anaptyctic vowel (sp- > sip-, cf. sipāh, \"\n   \"sipihr) and by assimilation of the first sibilant to the second: sipiš > šipiš. Hübschmann \"\n   \"(Pers. Stud. p.73) lists exactly this pair, 'supuš \\\"Laus\\\" H. 705', among the sp-/sf- words. \"\n   \"Wiktionary (after Hasandust) adds the prehistory: Proto-Iranian *cwíšah > Old Median *spišah, \"\n   \"borrowed into Persian — the sp-, not the expected Persian reflex, betrays the Median route, so \"\n   \"Avestan spiš- in the chart's top box is a cognate rather than a literal ancestor. The variants \"\n   \"Nourai prints are real and separate: شپشه šepeše 'grain weevil' (the Vendidad's granary louse; \"\n   \"Mo'in cites Zamakhshari's شپش گندم), شپشک šepešak 'scale insect (on plants)', اشپش ešpeš the \"\n   \"older/alternative form. The gloss 'flea' is the one error: شپش is 'louse'.\"),\n \"derivation_fa\": (\"«شپش» (تلفظ کلاسیک šipiš/šupuš، تاجیکی شابوش) از فارسی میانهٔ spiš است: خوشهٔ آغازین \"\n   \"sp- در فارسی نو با واکهٔ میانجی شکسته می‌شود (سپاه، سپهر) و سپس سین نخست به شین دوم همگون می‌گردد: \"\n   \"sipiš ← šipiš. هوبشمان (مطالعات ایرانی، ص ۷۳) همین جفت را در میان واژه‌های sp-/sf- آورده است. بر پایهٔ \"\n   \"ویکی‌واژه و حسن‌دوست، ایرانی باستان *cwíšah و صورت مادی *spišah در میان است؛ همین «سپ» نشان می‌دهد که \"\n   \"واژه از گویشی مادی به فارسی رسیده و اوستایی spiš- هم‌ریشه است نه نیای مستقیم. گونه‌های «شپشه» (شپشِ \"\n   \"گندم) و «شپشک» (آفت گیاهی) و «اشپش» همگی درست‌اند. تنها خطا، معنای «کک» است؛ شپش «louse» است.\"),\n \"sources\": [W_SEPESH],\n \"ref_check\": [\n   {\"ref\": \"BQT:1249\", \"status\": \"supports\",\n    \"note\": \"BQT_v3 leaf 39 ([pdf page 40] = printed 1249) carries the headword «شپش» and Mo'in's etymological footnote with Pahlavi spiš, Vd. 17.3 and the dialect forms — the whole arrow.\"},\n   {\"ref\": \"MON:2022\", \"status\": \"partial\",\n    \"note\": \"Mo'in, Farhang-e Farsi s.v. شپش (MON_part1.txt l.84199): '[- اشپش] (ا.) (جان.) حشره‌ای از راستهٔ نیم‌بالان ... شپش انگل انسان است' — confirms the word and the variant اشپش, but glosses it 'louse' and gives no etymology in this OCR.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 705, p. 156\", \"stance\": \"supports\",\n    \"note\": \"'705. supuš, uspuš \\\"Laus\\\", šipuš (etc.) ... māz. isfij' — the NP forms and the Iranian cognates (Kurd. sipi, Afgh. spaža, Oss. sis).\"},\n   {\"src\": \"HUB\", \"where\": \"p. 73 (list of sp- words), HUB.txt l.6294\", \"stance\": \"supports\",\n    \"note\": \"'... sipanj \\\"Ruheplatz\\\" H. 704, supuš \\\"Laus\\\" H. 705; sipoxtan ...' — Hübschmann files supuš with the regular sp- > sip- group.\"},\n   {\"src\": \"MON\", \"where\": \"s.v. شپش\", \"stance\": \"partial\",\n    \"note\": \"louse, ectoparasite of man; variant اشپش.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep شپش\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's IE-roots dictionary has no شپش headword (only an incidental 'شک (به چم تخم شپش)').\"}\n ]\n})\ndoc[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Spongo\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"not an IE root: Greek σπόγγος / Attic σφόγγος 'sponge', a Pre-Greek (Mediterranean) Wanderwort\",\n \"note\": (\"Two problems. (a) The page number: Walde-Pokorny II 621 is the entry '(s)teg-' \"\n          \"(WLD_Bd2_pages.txt leaf 625, running head '(s)teg- 621'); the lemma 'spongo- \"\n          \"\\\"schwammiges, poröses\\\"' is at WP II 681-682 (leaf 685, running head '(s)pīqo- — \"\n          \"spongo- 681'). The printed book itself reads 'WLD2:621' (see the page image), so this \"\n          \"is Nourai's slip, not an extraction error. (b) The substance: even Walde-Pokorny, who \"\n          \"list the form as a lemma, say Gk. σπόγγος/σφόγγος was borrowed into Latin as fungus and \"\n          \"reject the attempts to connect it with Germanic *swamba-; Klein s.v. sponge says the \"\n          \"Greek word 'is borrowed from an unknown source', and de Vaan/Beekes call it 'probably a \"\n          \"loanword from a non-IE language, borrowed independently into Greek, Latin and Armenian \"\n          \"in a form *sphong-', 'an old Wanderwort'. So there is no Indo-European root *spongo-, \"\n          \"and the gloss 'fluffy, empty' is Nourai's own (WP gloss: 'spongy, porous'). Nourai then \"\n          \"hangs the unrelated Iranian family sepanj / aspinǰ 'inn' on this box, which is the \"\n          \"page's main error.\"),\n \"note_fa\": (\"این ریشه از دو سو نادرست است. نخست ارجاع: صفحهٔ ۶۲۱ جلد دوم والده-پوکورنی مدخل (s)teg- \"\n             \"است و مدخل spongo- «اسفنجی، متخلخل» در ص ۶۸۱–۶۸۲ همان جلد آمده؛ کتاب چاپی هم «WLD2:621» \"\n             \"دارد، پس لغزش از خود نورایی است نه از استخراج. دوم اصل مطلب: σπόγγος یونانی (گونهٔ آتیکی \"\n             \"σφόγγος) ریشهٔ هندواروپایی ندارد؛ کلاین آن را «وام‌واژه‌ای از منبعی ناشناخته» می‌خواند و \"\n             \"بیکس و دِ فان آن را واژه‌ای پیش‌یونانی و «Wanderwort» مدیترانه‌ای می‌دانند که جداگانه به \"\n             \"یونانی و لاتینی و ارمنی راه یافته است. افزون بر این، معنای «fluffy, empty» ساختهٔ نورایی \"\n             \"است؛ گلاس والده-پوکورنی «متخلخل» است. بدتر آنکه خانوادهٔ ایرانی «سپنج/aspinǰ» (مهمان‌خانه) \"\n             \"نیز بی‌هیچ پیوندی زیر همین ریشه گذاشته شده. داوری: پژوهش امروزی این ریشه را رد می‌کند.\"),\n \"sources\": [W_SPONGOS, E_SPONGE, E_FUNGUS],\n \"ref_check\": [\n   {\"ref\": \"WLD2:621\", \"status\": \"not_found\",\n    \"note\": (\"WP II 621 (WLD_Bd2_pages.txt leaf 625) is '(s)teg- \\\"decken\\\"' — no sponge. The real \"\n             \"place is WP II 681: 'spongo- \\\"schwammiges, poröses\\\". Gr. σπόγγος, att. auch σφόγγος \"\n             \"\\\"Schwamm; Drüse\\\", woraus lat. fungus \\\"Erdschwamm, Pilz\\\" ... arm. sunk, sung'. \"\n             \"There WP add: 'Die Versuche, spongo- mit suombho-s \\\"schwammig, porös\\\" zu vermitteln, \"\n             \"verdienen kein Vertrauen' — i.e. even WP do not offer an IE etymology.\")}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 681-682 (WLD_Bd2_pages.txt leaf 685)\", \"stance\": \"partial\",\n    \"note\": \"has the lemma 'spongo- \\\"schwammiges, poröses\\\"' but only as a Greek/Latin/Armenian group with a borrowing relation, no IE reconstruction; gloss 'porous', not 'fluffy, empty'.\"},\n   {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'spong'\", \"stance\": \"silent\",\n    \"note\": \"Pokorny 1959 has no *spongo- lemma at all (only suomb(h)o-s 'porous, spongy' p.1052 for the Germanic swamp-words) — he dropped WP's entry.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, grep 'spong'\", \"stance\": \"silent\",\n    \"note\": \"Watkins has no sponge root; SPONGE is absent from the index of English words with IE roots.\"},\n   {\"src\": \"KLN\", \"where\": \"vol. II ~p.1495 s.v. sponge, n.\", \"stance\": \"contradicts\",\n    \"note\": \"'fr. Gk. σπογγιά \\\"sponge\\\" (rel. to σπόγγος, Att. σφόγγος, of s.m.), which — together with Arm. sung, sunk ... — is borrowed from an unknown source.'\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Greek\", \"words\": \"spongos; spoggos\", \"verdict\": \"plausible\",\n \"derivation\": (\"The Greek word is real and is the source of everything downstream: σπόγγος (Ionic/\"\n   \"Koine), Attic σφόγγος, 'sponge', already in Homer (Il. 18.414, Hephaistos wipes his face 'with \"\n   \"a sponge'), later also 'tonsil'. Nourai's two entries are not two words: 'spoggos' is simply a \"\n   \"letter-for-letter transliteration of σπόγγος in which the digraph -γγ- (pronounced [ŋg]) is \"\n   \"rendered -gg-, while 'spongos' renders the same -γγ- as -ng-. What is not right is the arrow \"\n   \"from an Indo-European root: Beekes calls σπόγγος 'an old Wanderwort' and de Vaan 'probably a \"\n   \"loanword from a non-IE language, borrowed independently into Greek, Latin and Armenian in a \"\n   \"form *sphong-'; the σπ-/σφ- doublet inside Greek itself is the classic signature of a \"\n   \"substrate word. Hence: word confirmed, parentage disputed.\"),\n \"derivation_fa\": (\"واژهٔ یونانی σπόγγος (گونهٔ آتیکی σφόγγος) «اسفنج» راست است و سرچشمهٔ همهٔ شاخه‌های \"\n   \"پایین‌دست؛ نخستین کاربردش در ایلیاد ۱۸٫۴۱۴ است. اما آنچه نورایی دو واژه شمرده، یکی است: «spoggos» \"\n   \"تنها آوانگاری حرف‌به‌حرف همان σπόγγος است که در آن -γγ- را gg- نوشته‌اند و «spongos» همان را ng-. \"\n   \"پیوند آن با ریشه‌ای هندواروپایی پذیرفتنی نیست: بیکس آن را «Wanderwort» کهن و دِ فان وام‌واژه‌ای \"\n   \"غیرهندواروپایی می‌داند که به‌گونهٔ *sphong- جداگانه وارد یونانی و لاتینی و ارمنی شده است؛ دوگانگی \"\n   \"σπ-/σφ- در خودِ یونانی نشانهٔ آشکار واژه‌های زیرلایه‌ای است. پس واژه درست است و نسب‌نامه‌اش نادرست.\"),\n \"sources\": [W_SPONGOS, E_SPONGE],\n \"ref_check\": [\n   {\"ref\": \"WLD2:621\", \"status\": \"not_found\",\n    \"note\": \"p.621 of WP II is '(s)teg-'; the Greek word is treated at WP II 681 ('Gr. σπόγγος, att. auch σφόγγος \\\"Schwamm; Drüse\\\"'), which does have the two Greek variants but not as an IE inheritance.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 681\", \"stance\": \"partial\",\n    \"note\": \"'Gr. σπόγγος, att. auch σφόγγος \\\"Schwamm; Drüse\\\", woraus lat. fungus' — the Greek forms, with Latin as a loan from Greek.\"},\n   {\"src\": \"KLN\", \"where\": \"vol. II ~p.1495 s.v. sponge\", \"stance\": \"partial\",\n    \"note\": \"'Gk. σπογγιά \\\"sponge\\\" (rel. to σπόγγος, Att. σφόγγος, of s.m.) ... borrowed from an unknown source.'\"},\n   {\"src\": \"IEC\", \"where\": \"IEC.txt, grep 'spong'\", \"stance\": \"silent\",\n    \"note\": \"Mann has no spong- headword.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"spynj\", \"verdict\": \"disputed\",\n \"derivation\": (\"This arrow is wrong twice over. The Pahlavi word is ʾspynj = aspinǰ, and it means \"\n   \"only 'hospitality; inn' (MacKenzie, Concise Pahlavi Dictionary, leaf 34 ≈ p.13: 'aspinj [ʾspnc \"\n   \"| P (ʾspynj), N sipanj] hospitality; inn'; derivative spinjānagīh 'the act of lodging'). It \"\n   \"never means 'sponge' or 'hollow'; Nourai has imported those glosses from the Greek box above. \"\n   \"And it is not from σπόγγος: Nyberg (Manual of Pahlavi II, p. 33 s.v. aspinj) files it as an \"\n   \"Aramaic loanword — 'MPrth ʾspynj; Aram. lw. Talm. ʾwšpyzʾ, Syr. ʾespezzā; Paz. aspanž; NP \"\n   \"sipanj \\\"a halting-place\\\"; cf. Arm. lw. aspnjakan \\\"innkeeper\\\"' — while Wiktionary and the \"\n   \"Iranian-loanwords-in-Syriac literature run the borrowing the other way (MP aspinǰ > Syr. \"\n   \"ʾešpezzā, JBA ʾūšpīzā, Arm. asp(a)nǰakan, Old Georgian masṗinʒeli). Either way the ultimate \"\n   \"background is the Aramaic/Latin 'hospitium' sphere of guest-lodging, and no source connects it \"\n   \"with the Greek word for a sponge. Phonetically the derivation also fails: σπόγγος has no \"\n   \"affricate to give the -nǰ of aspinǰ.\"),\n \"derivation_fa\": (\"این پیکان از دو جهت نادرست است. صورت پهلوی ʾspynj یعنی aspinǰ است و تنها معنای \"\n   \"«مهمان‌نوازی؛ مهمان‌سرا» دارد (مکنزی، ص ۱۳: «aspinj hospitality; inn»؛ مشتق آن spinjānagīh «میزبانی»)؛ \"\n   \"معناهای «اسفنج» و «تهی» را نورایی از جعبهٔ یونانیِ بالا به آن بخشیده است. دیگر آنکه از σπόγγος \"\n   \"نیامده: نیبرگ (راهنمای پهلوی، ج ۲، ص ۳۳) آن را وام‌واژه‌ای آرامی می‌داند (تلمودی ʾwšpyzʾ، سریانی \"\n   \"ʾespezzā، ارمنی aspnǰakan)، و ویکی‌واژه و پژوهش‌های وام‌واژه‌های ایرانی در سریانی جهت وام‌گیری را \"\n   \"وارونه می‌بینند (از فارسی میانه به آرامی). در هر دو روایت سخن از حوزهٔ معنایی «مهمان‌خانه» است نه \"\n   \"«اسفنج». از نظر آوایی هم σπόγγος هیچ همخوان سایشی‌-انسدادی ندارد که به -نج aspinǰ بدل شود. \"\n   \"داوری: پژوهش امروزی این اشتقاق را رد می‌کند.\"),\n \"sources\": [W_SEPANJ],\n \"ref_check\": [\n   {\"ref\": \"SOD:64\", \"status\": \"partial\",\n    \"note\": (\"Gharib, Sogdian Dictionary p.64 (SOD_pages.txt leaf 129, the printed numeral 64 is on \"\n             \"the page) entry no. 1628 '*spnc M: (ʾ)spanc ©<Parth. MP ʾspynj ... inn, rest house'. \"\n             \"It confirms the Pahlavi/Parthian form ʾspynj and its meaning 'inn' — and therefore \"\n             \"contradicts the glosses 'sponge, hollow' and gives no Greek source.\")}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"leaf 34 (≈ p.13) s.v. aspinj\", \"stance\": \"contradicts\",\n    \"note\": \"'aspinj [ʾspnc | P (ʾspynj), N sipanj] hospitality; inn' — and PHD's English index 'inn aspinj', 'hospitality aspinj, mehmānīh, spinjānagīh'. No 'sponge', no 'hollow'.\"},\n   {\"src\": \"NYB\", \"where\": \"vol. II glossary p. 33 s.v. aspinj\", \"stance\": \"contradicts\",\n    \"note\": \"'aspinj [ʾspnčʾ] lodging 73.10, 75.12. — MPrth ʾspynj (A-H III); Aram. lw. Talm ʾwšpyzʾ, Syr ʾespezzā; Paz. aspanž, aspenj; NP sipanj \\\"a halting-place, a shelter\\\". Cf. further Arm. lw. aspnjakan ... = Talm ʾwšpyzknʾ' — a Semitic, not a Greek, connection.\"},\n   {\"src\": \"HUB\", \"where\": \"§123, p. 231 (HUB.txt l.8262)\", \"stance\": \"contradicts\",\n    \"note\": \"'aspnjakan \\\"der einen Fremden gastlich aufnimmt, Wirth\\\", phl. paz. aspanj, np. sipanj, syr. aspizkana, mand. spinza aus *aspinj' — treats the whole family as one Iranian/Aramaic word for 'host', unrelated to σπόγγος.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"sepanj «سپنج»\", \"verdict\": \"plausible\",\n \"derivation\": (\"The step itself is regular and well attested: MP aspinǰ > NP sipanǰ/sepanj by loss \"\n   \"of the prothetic a- (aphaeresis, as in ustuxān ~ NP stun-type variation) and the usual \"\n   \"anaptyxis in the sp- cluster; Horn no. 704 (p.156) gives 'sipenj \\\"Ruheplatz, Gasthaus\\\" \"\n   \"(Šāhn. I 229 v.1791); phlv. aspanj \\\"Ruheplatz, Asyl\\\" (Mēnōg; Ardā Wirāz), spinjānakīh, arm. \"\n   \"LW. aspnjakan \\\"Gast\\\", chald. syr. LW. \\\"Gasthof\\\"'. The glosses, however, are Nourai's \"\n   \"over-reading. Borhan-e Qate' (p.~1095, BQT_v2 leaf 552) defines سپنج as 'مهمان' (guest), \"\n   \"'عاریت' (a thing lent), 'a hut that farmers and field-watchers build of wood and grass', 'a \"\n   \"borrowed resting-place' and only then explains the metaphor: 'because the world has no \"\n   \"permanence and is like a borrowed guest-house, they call it سرای سپنج' — which is exactly \"\n   \"Nourai's Ferdowsi line 'سپنجی سرایست دنیای دون'. So 'worthless material world' is a literary \"\n   \"metaphor, not a lexical meaning, and 'hollow' is not a meaning of the word at all; it was \"\n   \"back-formed from the Greek 'sponge' box. Verdict plausible: the MP > NP edge is right, its \"\n   \"glosses and its ultimate ancestry are not.\"),\n \"derivation_fa\": (\"خودِ این گام قاعده‌مند و مستند است: فارسی میانه aspinǰ با افتادن «اَ»ی آغازین و \"\n   \"میانجی‌گرفتن خوشهٔ sp- به «سپنج» فارسی نو رسیده است؛ هرن (شمارهٔ ۷۰۴، ص ۱۵۶) همین را می‌آورد: \"\n   \"«sipenj «آرام‌گاه، مهمان‌خانه» (شاهنامه)؛ پهلوی aspanj؛ ارمنی aspnjakan «مهمان»؛ وام سریانی-کلدانی \"\n   \"«مهمان‌خانه»». اما معناهای نمودار برساختهٔ نورایی است: برهان قاطع (ص ۱۰۹۰–۱۰۹۵) سپنج را «مهمان»، \"\n   \"«عاریت»، «کپری که برزگران و دشت‌بانان از چوب و علف سازند» و «آرام‌گاه عاریتی» می‌داند و سپس می‌افزاید \"\n   \"«چون دنیا را بقایی نیست و حکم مهمان‌خانهٔ عاریتی دارد آن را نیز به طریق استعاره سرای سپنج خوانند» — \"\n   \"درست همان بیت فردوسی که نورایی نقل کرده. پس «جهان دون» استعاره است نه معنای واژه، و «تهی/hollow» \"\n   \"اصلاً معنای سپنج نیست و از جعبهٔ «اسفنج» یونانی به آن سرایت کرده است.\"),\n \"sources\": [W_SEPANJ],\n \"ref_check\": [\n   {\"ref\": \"BQT:1090\", \"status\": \"partial\",\n    \"note\": (\"Borhan-e Qate' (Mo'in), BQT_v2_pages.txt leaf 552 (printed ≈ 1095, i.e. Nourai's 1090 \"\n             \"within the scan's ±5 drift): «سپنج - بروزن شکنج. بمعنی مهمان باشد - و بمعنی عاریت هم \"\n             \"گفته‌اند - و خانه‌ای باشد که مزارعان و دشت‌بانان ... از چوب و علف سازند - و آرام‌گاه عاریتی \"\n             \"را نیز گویند - و چون دنیا را بقایی نیست ... آن را نیز بطریق استعاره سرای سپنج خوانند», \"\n             \"with the Ferdowsi verse «سپنجی سرایست دنیای دون - بسی چون تو میرفت غمگین برون» that \"\n             \"Nourai quotes. The word and the quotation are confirmed; no etymology is offered, and \"\n             \"no 'hollow' sense.\")},\n   {\"ref\": \"VFO:22\", \"status\": \"not_checked\",\n    \"note\": \"VFO is an unresolved abbreviation in this project (MISSING_REFERENCES.md: 'probably = VOP', Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, 1371) and no copy exists online or on disk. Tellingly, Nourai cites a dictionary of EUROPEAN loanwords in Persian for سپنج — which is precisely the classification the other sources reject.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 704, p. 156\", \"stance\": \"supports\",\n    \"note\": \"'704. sipenj \\\"Ruheplatz, Gasthaus\\\" (Šāhn. I, 229 v.1791). phlv. aspanj \\\"Ruheplatz, Asyl\\\" (Mēn.; AV.), spinjānakīh, arm. LW. aspnjakan \\\"Gast\\\", chald. syr. LW. ... (de Lagarde, Semitica 51). Dazu die Lehnworte türk. ispenje, serb. spendža, rum. spendze, bulg. ispenč.'\"},\n   {\"src\": \"HUB\", \"where\": \"p.73 and §123 p.231\", \"stance\": \"supports\",\n    \"note\": \"lists 'sipanj \\\"Ruheplatz\\\" H. 704' among the regular sp- > sip- words and reconstructs the family from *aspinj.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 2, printed ≈1090-1095\", \"stance\": \"partial\",\n    \"note\": \"senses 'guest / loan / hut / borrowed resting place / (metaphor) the transient world'; no 'hollow'.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab/MON_part*, grep سپنج\", \"stance\": \"silent\",\n    \"note\": \"not found in the available OCR of Mo'in's lexicon volumes.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"`spnc\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Gharib's Sogdian Dictionary, entry 1628 on p.64, reads '*spnc M: (ʾ)spanc \"\n   \"©<Parth. MP ʾspynj ©pl. -tt, -ynst ... inn, rest house (GMS 112, 260; Henning BSOAS 12, 307)'. \"\n   \"So the Manichaean-Sogdian word ʾspnc /(ʾ)spanč/ is explicitly a borrowing from Parthian/Middle \"\n   \"Persian ʾspynj — exactly the arrow drawn (parent = the Pahlavi box), with Sogdian -č for \"\n   \"western Iranian -ǰ, the regular substitution in Sogdian loans from Parthian. Gharib also lists \"\n   \"the derivatives ʾspʾnch/ʾspʾynst 'inns'. The gloss 'inn, rest house' is verbatim hers. Only the \"\n   \"grandparent (Greek σπόγγος) is wrong; this edge is right.\"),\n \"derivation_fa\": (\"در فرهنگ سغدی بدرالزمان قریب، مدخل ۱۶۲۸ در ص ۶۴: «*spnc (M): (ʾ)spanc، از پارتی/\"\n   \"فارسی میانه ʾspynj، جمع -tt، ‑ynst؛ مهمان‌خانه، کاروان‌سرا». پس واژهٔ سغدی مانوی ʾspnc خود قریب آن را \"\n   \"وام از ʾspynj غربی‌ایرانی می‌داند — درست همان پیکانی که نورایی کشیده است؛ «چ» سغدی به‌جای «ج» غربی، \"\n   \"جانشینی معمول در وام‌واژه‌های سغدی از پارتی است. تنها نیای بالادست (σπόγγος یونانی) نادرست است و این \"\n   \"حلقه درست است.\"),\n \"sources\": [W_SEPANJ],\n \"ref_check\": [\n   {\"ref\": \"SOD:64\", \"status\": \"supports\",\n    \"note\": \"SOD_pages.txt leaf 129 (printed numeral 64 visible on the page), entry 1628: '*spnc M ... (ʾ)spanc ©<Parth. MP ʾspynj ©pl. -tt, -ynst => ʾspync, ʾspʾnch, ʾspʾynst — inn, rest house. GMS 112, 260; Hen. BSOAS 12, 307.37'. Nourai's SOD:64 is a page number here, and it is correct.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"p.64 no. 1628 (+ no. 1614 ʾspʾynst 'inns')\", \"stance\": \"supports\",\n    \"note\": \"'(ʾ)spanc ©<Parth. MP ʾspynj ... inn, rest house'.\"},\n   {\"src\": \"NYB\", \"where\": \"vol. II p.33 s.v. aspinj\", \"stance\": \"supports\",\n    \"note\": \"'MPrth ʾspynj' — the Parthian form Gharib derives the Sogdian from.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Arabic\", \"words\": \"al-esfanj\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Arabic إِسْفَنْج ʾisfanj 'sponge' (the chart's 'al-esfanj' is the word with the \"\n   \"definite article al-) is a loan from Greek σπόγγος: Greek σπ- is regularly rendered in Arabic \"\n   \"by is-/us- + f, because Arabic has no /p/ and breaks up the initial cluster with a prothetic \"\n   \"vowel (cf. إسطبل isṭabl < stabulum, أسطول usṭūl < στόλος); -γγ- [ŋg] is taken over as -nǧ. The \"\n   \"route is the usual Hellenistic-medical one — the sponge is a standing item of Greek materia \"\n   \"medica and surgery — most likely through Syriac ʾespōgā. Tobia al-Unaysi, whom Nourai cites, \"\n   \"has the entry in so many words: 'إسفنج - يوناني σπόγγος ... نحري جسمه متخلخل' ('Greek \"\n   \"spongos ... a sea creature whose body is porous'). Wiktionary's etymology tree: Pre-Greek > \"\n   \"Ancient Greek σπόγγος > Arabic إسفنج.\"),\n \"derivation_fa\": (\"«إسفنج» عربی (در نمودار با حرف تعریف: al-esfanj) وام‌واژه‌ای از σπόγγος یونانی است. \"\n   \"عربی «پ» ندارد و خوشهٔ آغازین σπ- را با واکهٔ افزوده و «ف» می‌گیرد (مانند إسطبل از stabulum و أسطول \"\n   \"از στόλος)، و -γγ- را «نج» می‌نویسد. راه وام‌گیری همان راه پزشکی یونانی‌مآبانه است — اسفنج از اقلام \"\n   \"همیشگی داروشناسی و جراحی یونانی است — به احتمال از رهگذر سریانی ʾespōgā. طوبیا العنیسی، همان مرجعی \"\n   \"که نورایی یاد کرده، عیناً می‌نویسد: «إسفنج ـ يوناني σπόγγος ... بحري جسمه متخلخل». داوری: ادعای \"\n   \"نورایی درست است.\"),\n \"sources\": [W_ESFANJ, W_SPONGOS],\n \"ref_check\": [\n   {\"ref\": \"TAD:35\", \"status\": \"partial\",\n    \"note\": (\"The entry exists and says exactly what the arrow says — TAD_pages.txt leaf 6: «إسفنج ـ \"\n             \"يوناني [σπόγγος] معناه ... بحري جسمه متخلخل» — but it sits at the very start of the \"\n             \"alif section of the 1932 Cairo scan (leaf 6 ≈ printed p.2), not on p.35 of this \"\n             \"edition; leaf 39 (≈ p.35) carries the sīn words (إسفين وسَفين ـ يوناني σφήν). Content \"\n             \"supports, page number does not match the edition on disk (Nourai used the Library of \"\n             \"Lebanon reprint).\")}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"vol. II ~p.1495 s.v. sponge\", \"stance\": \"partial\",\n    \"note\": \"gives Gk σπόγγος/σφόγγος as the etymon of the whole Mediterranean family (Klein does not treat the Arabic word, but supplies the Greek source).\"},\n   {\"src\": \"AFM\", \"where\": \"AFM_pages.txt, grep سفنج\", \"stance\": \"silent\",\n    \"note\": \"Addi Shir's Persian-Arabic loanword dictionary has no إسفنج entry — consistent with it being a Greek, not a Persian, loan into Arabic.\"},\n   {\"src\": \"PLA\", \"where\": \"PLA_pages.txt, grep isfang/Schwamm\", \"stance\": \"silent\",\n    \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, does not list إسفنج either.\"},\n   {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt, grep sfnj\", \"stance\": \"silent\",\n    \"note\": \"not a Qur'anic word; Jeffery has no entry.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"esfanj «اسفنج»\", \"verdict\": \"confirmed\",\n \"derivation\": (\"NP اسفنج esfanj 'sponge' is the Arabic word taken back into Persian — a plain \"\n   \"Arabic loan, not an inheritance: Persian would never itself produce -sf- from Greek σπ-. Mo'in \"\n   \"says so in his footnote to the Borhan-e Qate' entry (p.~130, BQT_v1 leaf 346): the entry \"\n   \"«اسفنج - چیزی است شبیه به نمد کرم‌خورده ... و بعربی رغوة الحجامین» carries the note «از تازی، از \"\n   \"یونانی» ('from Arabic, from Greek'). In his own Farhang-e Farsi he tags it «معرّب اسپنگ - \"\n   \"اسپنج» — i.e. he thinks the Arabic form is an Arabicisation of an Iranian espang/espanj, which \"\n   \"would make it a round trip; Wiktionary keeps the simpler line, Pre-Greek > Gk σπόγγος > Ar. \"\n   \"إسفنج > Pers. اسفنج, and lists اسپنج/اسپنگ as Persian variants. Either way the Arabic step that \"\n   \"Nourai draws is right.\"),\n \"derivation_fa\": (\"«اسفنج» فارسی وام‌واژه‌ای از عربی است و نه میراث ایرانی؛ فارسی هرگز از σπ- یونانی \"\n   \"خوشهٔ «سف» نمی‌سازد. معین در حاشیهٔ برهان قاطع (ص ۱۳۰) زیر مدخل «اسفنج» می‌نویسد «از تازی، از یونانی». \"\n   \"در فرهنگ فارسی خود اما آن را «معرّب اسپنگ ـ اسپنج» می‌داند، یعنی رفت‌وبرگشتی فارسی←عربی←فارسی؛ \"\n   \"ویکی‌واژه ساده‌تر می‌گوید: پیش‌یونانی ← σπόγγος ← إسفنج عربی ← اسفنج فارسی، و اسپنج/اسپنگ را گونه‌های \"\n   \"فارسی می‌شمارد. در هر دو روایت، حلقهٔ عربیِ نمودار درست است.\"),\n \"sources\": [W_ESFANJ],\n \"ref_check\": [\n   {\"ref\": \"BQT:130\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 346 (printed ≈ 126-136, i.e. Nourai's 130): headword «اسفنج ـ بکسر اول و سکون ثانی ... چیزی است شبیه بنمد کرم خورده ... و بعربی رغوة الحجامین ... گویند حیوانی است دریایی», with Mo'in's footnote «از تازی، از یونانی» — exactly the Greek > Arabic > Persian route.\"},\n   {\"ref\": \"MON:269\", \"status\": \"partial\",\n    \"note\": \"Mo'in, Farhang-e Farsi s.v. اسفنج (MON_part1.txt l.12849): «اسفنج: [معر. اسپنگ - اسپنج، فشرده] (ا.) (جان.) جانوری است جزو بی‌مهرگان ...» — confirms the word and an Arabicisation tag, but makes the Arabic form a معرّب of Iranian espang rather than of Greek.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 1 ≈ p.130\", \"stance\": \"supports\", \"note\": \"«از تازی، از یونانی».\"},\n   {\"src\": \"MON\", \"where\": \"s.v. اسفنج\", \"stance\": \"partial\", \"note\": \"«معر. اسپنگ - اسپنج».\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt, grep isfanǧ/sipanǧ\", \"stance\": \"silent\",\n    \"note\": \"Horn has no اسفنج entry (he excludes plain Arabic loans).\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Latin\", \"words\": \"spongia; fungus\", \"verdict\": \"plausible\",\n \"derivation\": (\"Latin spongia 'sponge' is a straightforward borrowing of Greek σπογγιά (the \"\n   \"-ια derivative of σπόγγος), taken over with the Greek meaning; that half is uncontroversial \"\n   \"(Klein s.v. sponge). Latin fungus 'mushroom, fungus' is the disputed half. Klein and \"\n   \"Walde-Pokorny make it a loan from the Attic form: WP II 681 'Gr. σπόγγος, att. auch σφόγγος \"\n   \"..., woraus lat. fungus', arguing that the initial correspondence σφ- : f- is the same as in \"\n   \"the loan fidēs : σφίδες; Klein s.v. fungus: 'L., \\\"mushroom\\\", fr. Att. Gk. σφόγγος, \"\n   \"corresponding to Gk. σπόγγος, \\\"sponge\\\"'. De Vaan and Beekes instead take Greek, Latin and \"\n   \"Armenian sunk to be three independent borrowings of one non-IE Mediterranean word *sphong-, \"\n   \"so Latin fungus would be a sibling of σφόγγος rather than its descendant. The chart's arrow is \"\n   \"thus the older, still-defensible view — plausible, not settled.\"),\n \"derivation_fa\": (\"spongia لاتینی بی‌هیچ دشواری وام از σπογγιά یونانی (مشتقِ ‑ια از σπόγγος) است و این \"\n   \"بخش مناقشه‌ای ندارد. مناقشه بر سر fungus «قارچ» است: کلاین و والده-پوکورنی آن را وام از گونهٔ \"\n   \"آتیکی σφόγγος می‌دانند (والده-پوکورنی، ج۲ ص۶۸۱: «σπόγγος یونانی، در آتیکی σφόγγος، که lat. fungus \"\n   \"از آن است»)، با استناد به همان تناظر σφ- : f- که در وام‌واژهٔ fidēs دیده می‌شود. در برابر، دِ فان و \"\n   \"بیکس یونانی و لاتینی و ارمنی sunk را سه وام‌گیری مستقل از یک واژهٔ غیرهندواروپایی مدیترانه‌ای \"\n   \"*sphong- می‌شمارند؛ در آن صورت fungus خواهرِ σφόγγος است نه فرزند آن. پس پیکان نمودار دیدگاه کهن‌تر \"\n   \"و هنوز دفاع‌پذیر است: با احتیاط پذیرفتنی.\"),\n \"sources\": [E_FUNGUS, E_SPONGE, W_SPONGOS],\n \"ref_check\": [\n   {\"ref\": \"KLN:1494\", \"status\": \"supports\",\n    \"note\": \"Klein 1966, vol. II, the 'sponge' entry falls on KLN_1966.txt leaf 793, between the page numerals 1492 (leaf 791) and 1499 (leaf 794), i.e. pp. 1495-1496 — Nourai's 1494 is right to within a page. Text: 'sponge, n. — ME., fr. OF. esponge (F. éponge), fr. L. spongia, fr. Gk. σπογγιά ... L. fungus, \\\"mushroom, fungus\\\", is a loan word fr. Att. σφόγγος.' Both of Nourai's Latin words, with the Greek source.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. fungus (KLN_1966.txt l.15550) and s.v. sponge\", \"stance\": \"supports\",\n    \"note\": \"'fungus ... — L., \\\"mushroom\\\", fr. Att. Gk. σφόγγος, corresponding to Gk. σπόγγος, \\\"sponge\\\". For the change of Gk. σφ to f in Latin cp. L. fidēs.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 681\", \"stance\": \"supports\",\n    \"note\": \"'Gr. σπόγγος, att. auch σφόγγος \\\"Schwamm; Drüse\\\", woraus lat. fungus \\\"Erdschwamm, Pilz\\\"' with a long footnote defending the borrowing against Pedersen and Persson.\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline (archived) s.v. fungus\", \"stance\": \"partial\",\n    \"note\": \"'The Latin word is believed to be cognate with (or derived from) Greek sphongos ... \\\"Probably a loanword from a non-IE language, borrowed independently into Greek, Latin and Armenian in a form *sphong-\\\" [de Vaan]' — leaves both options open, prefers independent borrowing.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"sponge; fungus\", \"verdict\": \"confirmed\",\n \"derivation\": (\"English sponge is Old English sponge/spunge, borrowed from Latin spongia already \"\n   \"in the Old English period (a learned/ecclesiastical word — the sponge of the Crucifixion), and \"\n   \"reinforced in Middle English by Old French esponge (Modern French éponge), itself from the \"\n   \"same Latin word; the Latin form also gave OS spunsia, MDu. spongie, Sp. esponja, It. spugna. \"\n   \"The marine-animal sense is English from the 1530s. English fungus is a direct sixteenth-century \"\n   \"learned borrowing of Latin fungus (1520s, 'a mushroom'), used at first as a bookish alternative \"\n   \"to mushroom. Both words therefore descend from the Latin box exactly as drawn.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسی sponge همان spunge/sponge انگلیسی کهن است که در همان دوره از spongia \"\n   \"لاتینی وام گرفته شد (واژه‌ای کلیسایی: اسفنجِ روایت مصلوب‌شدن) و در انگلیسی میانه با esponge فرانسهٔ کهن \"\n   \"(éponge امروزی) تقویت شد؛ همان صورت لاتینی esponja اسپانیایی و spugna ایتالیایی را هم داده است. \"\n   \"معنی «جانور دریایی» در انگلیسی از دههٔ ۱۵۳۰ پیدا شده است. fungus وام مستقیم و کتابی سدهٔ شانزدهم \"\n   \"(حدود ۱۵۲۰) از fungus لاتینی است که نخست به‌جای mushroom به کار می‌رفت. پس هر دو واژه دقیقاً همان‌گونه \"\n   \"که نمودار نشان می‌دهد از جعبهٔ لاتینی می‌آیند. داوری: درست است.\"),\n \"sources\": [E_SPONGE, E_FUNGUS],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"the node carries no reference in the book; checked independently against Klein and Etymonline (both archived/quoted below).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"vol. II ~p.1495 s.v. sponge, n.\", \"stance\": \"supports\",\n    \"note\": \"'sponge, n. — ME., fr. OF. esponge (F. éponge), fr. L. spongia, fr. Gk. σπογγιά.'\"},\n   {\"src\": \"WEB\", \"where\": \"Etymonline (archived) s.vv. sponge, fungus\", \"stance\": \"supports\",\n    \"note\": \"'Old English sponge, spunge ... from Latin spongia'; 'fungus: 1520s, \\\"a mushroom\\\", from Latin fungus ... used in English at first as a learned alternative to mushroom'.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. sponge\", \"stance\": \"supports\",\n    \"note\": \"Skeat likewise takes sponge from L. spongia < Gk σπογγιά.\"}\n ]\n})\ndoc[\"entries\"].append(e1)\njson.dump(doc, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/part1-471.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(doc[\"entries\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-471.py"
}
```


### [2026-09-14T02:42:45.772Z] TOOL RESULT

```
ok 2
```


## [2026-09-14T02:42:51.235Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Sponge\\|sponge,\" SKT.txt | head -5; echo ---; grep -n \"Fungus\\|fungus,\" SKT.txt | head -5\necho \"=== FSD/WEB sponge ===\"; grep -n \"spongia\" FSD_vol4.txt WEB*.txt 2>/dev/null | head -5; ls | grep -i \"^WEB\""
}
```


### [2026-09-14T02:42:51.342Z] TOOL RESULT

```
7216:Fung:u8,  a  spnngy  plant  (L,-Gk.)  I* fungus  (pntfbrjr/wM^Hj).  —  GV-otpCryyot,  At- tic form  of  ait6yy<»,  a  sponge ;  see  Sponge. Funnel.  (F.-L)  M.E.  >w?/.  Pmb from  on  O.  F.  fonil*,  preserved  in  Bret _/t>Hw//.  a  funnel,  and  short  for  tnfonil^.^ L.  infundibulum.  a  funnel. Pur,  (F.-O.  Low  G.)  M.E.  >nv.- O.  K,  forttt  futrrt,  a  sheath,  case ;  cf. Span,  forro,  lining  lor  clothes,  Ital./ft//rv, lininy,  fur,  scablird.  —  Gulh.  fodr,  scab- bard, orig.  '  protection  ;'  Iccl.y^ffr,  linixig ; allied  to  G.futter,  which  (like  Icel.y^) also  means  'fodder.'  Allied  lo  Fodder; the  senses  of  feeding  and  protecting  being connected.
18159:Sponge.  (F.-L.-Gk.)  O.F.  apongt (F.  i^/mijfr).  — L.  spoti^a.  ^GV.  avoyyia,  a sponge;  aiso  amuy^t  (Attic  ff ■^'1 7Tf«t).  + L.  fungus,  a  fungus  (from  its  »pongy  na- ture).    Prob.  allied  la  Swamp.
18982:swamp.  (Scand.)  Not  ai The/  is  excrescent.  *  Don.  Swi sponge,  funj^us;  (hence  applied ground,  which  seems  to  be  exda
18983:E.  use).  4*  ^1-  H-  G.  rwatH,  sm schtvamm,  a  sponge,  fungus;  Dt Goth.  nvamfHj,  sponge;  Low  G. rzvamf;  funpus ;  A.  S.  swam,  funr from  v'lsWAM,  loswim.  0.  FarS lo  Gk.  co^iKf>ii%,  spong)',  Goth^ swamp ;  and  even  tu  Sponi also  prov.  E.  swank,  stvau^.  a as  E.  swank :  £.  swamp ::  Gk.
21393:Whlak.  to  move  or  sweep  quickly. (Scand.)  The  h  is  Intru&ive.  It  is  pro- perly xviik,  orig.  to  wipe,  brush,  sweep, csp-  with  a  quick  motion,  as  when  using a  tight  brush :  the  h  was  due  to  confusion with  whit,  whir,  whirl,  Ac^Dan.  viike, to  wipe.  rub.  sponge,  from  visk,  a  wisp, rubber;  SwctL  viska,  to  wipe,  also  to  wag (or  whisk)  the  tail,  from  viska,  'a  whisk, a  small  broom,^  Widegrea;  Icel.  visk,  a wisp  of  hay,  something  lo  wipe  with,  a rubber.  +  G.  wischen, '  to  wipe,  wisk,  rub.' Fliigcl ;  from  the  $b.  loisch,  '  a  whiik, clout,'  id.  ^.  Thesb.  which  thus  appears as  Icel.  visk,  Swed.  viska,  G.  wisch,  meant orig.  'a  washer;'  from  the  Tcul.  base WASK,  to  wash;  see  Waah.  Der. whiik'tr,  from  the  likeness  to  a  small brush.  '  Nestor  brtish^d  her  with  his  tvhiik- ers\'  Drjden,  Troilus,  iv.  a.  Mho whisk-y, a  light  gig.  cosily  whiskid  aXonc.
---
18159:Sponge.  (F.-L.-Gk.)  O.F.  apongt (F.  i^/mijfr).  — L.  spoti^a.  ^GV.  avoyyia,  a sponge;  aiso  amuy^t  (Attic  ff ■^'1 7Tf«t).  + L.  fungus,  a  fungus  (from  its  »pongy  na- ture).    Prob.  allied  la  Swamp.
20272:tTc-i.  pt.   of  pro-tubcrar^,  to  blilp  CM , pro,  forward  ;  tuber,  a  swcUiac* truffle.  (F.-L.)     F./n^.tSboAl a  round  edible  fungus,  fouau  imdMli Span,  tru/a,  a  trufBe.    The  P.  frafitH trufa^    answer   to    L,    ^    tub<f^  uw whence  was  formed  a  F.  fern.  sb.  *•'* ea!iily  altered  to  tru^i.     \Vc  also  fwt turtufo,  a    tiufilc    »   L.   ttrr^  tukfi tiufilc  uf  the  eaith.     AikI  •««  TrllU. Tuck  (1),  to  lold  or  gatkrr  tvfc UicM  ;  *ec  Tow  (I) Tuok  \,i),  a  ripier ;  sec  Stlok  (i)
=== FSD/WEB sponge ===
WEB_vol1.txt:26332:Cal-ci-spon’gi-ae, n.pl. [L. calx, calcis, lime, and spongia, a sponge.] a division of the sponges having three-rayed calcareous needles or spicules.
WEB_vol1.txt:72471:cartilage.] elastic cartilage. fi’bro-ciir-ti-lag/i-nous, a. composed of fibrocartilage. fi’brd-chon-dros/té-Al, a. [fibro-, and Gr, chondros, gristle, and osteon, bone.] made up of fibrous tissue, cartilage, and bone: said of the human skeleton. fi’broid, a. [fibr-, and -oid.] like, composed of, or forming fibrous tissue. fibroid degeneration; a breaking down of nor- mal, healthy tissue into fibroid tissue. fibroid phthisis; a kind of phthisis which in- volves the formation of fibroid tissue in the lungs. fi’/broid, n. a fibrous tumor. fi/bro-in, n. [fibro-, and -in.] a white albumi- noid of which cobwebs and raw silk are mainly composed. fi/bro-lite, n. [fibro-, and Gr. lithos, stone.] a mineral of a white or gray color, composed chiefly of aluminum silicate: also called sillimanite and bucholzite. fi’bré-ma, 7.; pl. fi-brd’mas, fi-brd’ma-ta, [Mod. L., from fibr-, and eur a nonmalig- nant tumor composed largely of fibrous tissue. fi-brom/a-tous, a. of, like, or containing a fibroma. fi-bro’sis, n. [Mod. L., from fibr- and -osis.] an abnormal increase in the amount of fibrous connective tissue in an organ, part, or tissue. Fi-bro-spon/gi-ae, n.pl. [fibro-, and L, spongia, a sponge.] a former classification of sponges with a fibrous skeleton, including the common commercial sponge. fi’brous, a. 1.composed or consisting of fibers; as, a fibrous body or substance. 2. of the nature of fibers or fila- y ments; as, fibrous roots. N T 7 FIBROUS ROOT
WEB_vol1.txt:78366:frog’bit, n. either of two related plants, Hy- drocharis morsus-ranz of Europe and Limno- bium spongia of the United States: written also frog’s-bil.
WEB_vol1.txt:93185:Hy’a-lo-spon’gi-ae, n.pl. [hyalo-, and Gr. spongia, a sponge.] a family of siliceous sponges in which the skeleton is composed of six-rayed spicules becoming ultimately united together. The species are found at great depths of the ocean.
FSD_vol4.txt:11028:SU"l-cI-spoa'gI-Jc,  1   sU  i-si-spen'Ji-l,  2   slli-cl-spdn'gl-g,  n   pi Spong  The  Silicea  [   <   silici-  +   L   spongia,  sponge  ] sIFl-cIte,  1   sllh-salt,  2   siri-clt,  n   Same  as  ferrosiucox. sl-Il'cl-um*  1   si-llSh'i-um,  2   sI-Ush'l-Qm,  n   Chem  Same as  SILICON  sin-curat.
WEB_vol1.txt
```


## [2026-09-14T02:46:47.255Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\np='/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/part1-471.json'\nd=json.load(open(p))\n# fix src labels + SKT quote\nfor e in d[\"entries\"]:\n    for n in e[\"nodes\"]:\n        for c in n.get(\"consulted\",[]):\n            if c[\"src\"]==\"WEB\" and \"Etymonline\" in c[\"where\"]:\n                c[\"src\"]=\"ETYMONLINE\"\n            if c[\"src\"]==\"SKT\":\n                c[\"where\"]=\"SKT.txt l.18159 s.v. Sponge and l.7216 s.v. Fungus\"\n                c[\"note\"]=(\"'Sponge. (F.-L.-Gk.) O.F. esponge (F. éponge). — L. spongia. — Gk. σπογγιά, \"\n                           \"a sponge; also σπόγγος (Attic σφόγγος). + L. fungus, a fungus (from its spongy \"\n                           \"nature).' and 'Fungus, a spongy plant (L.-Gk.) L. fungus. — Gk. σφόγγος, Attic \"\n                           \"form of σπόγγος, a sponge; see Sponge.'\")\njson.dump(d,open(p,'w'),ensure_ascii=False,indent=1)\nprint('patched')\nPYEOF"
}
```


### [2026-09-14T02:46:48.373Z] TOOL RESULT

```
patched
```


## [2026-09-14T02:49:29.414Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build2-471.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nP='/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/part1-471.json'\ndoc=json.load(open(P))\n\nW_TOFANG = \"https://en.wiktionary.org/wiki/%D8%AA%D9%81%D9%86%DA%AF\"\nW_TOF = \"https://en.wiktionary.org/wiki/%D8%AA%D9%81\"\nE_SPIT = \"https://www.etymonline.com/word/spit\"\nE_SPUTTER = \"https://www.etymonline.com/word/sputter\"\n\ne4 = {\n \"entry\": 4,\n \"root\": \"Spyeu, Sphîeu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *(s)p(h)i̯eu- : *(s)pi̯u-, *(s)pīu- 'to spit' (Pokorny 999-1000); Watkins *spyeu-\",\n \"note\": (\"Right root, right language label, right gloss, right page. Pokorny's lemma reads 'Root/\"\n          \"lemma: (s)p(h)ieu- : (s)pju-, (s)pīu-. Meaning: to spit', Pages 999-1000, with material \"\n          \"Skt. sthīvati, Av. spāma- 'saliva', Gk. πτύω, Lat. spuō/sputum, Goth. speiwan, Lith. \"\n          \"spiauju, OCS pljujǫ — which is exactly the set of daughters Nourai draws. Nourai's two \"\n          \"headwords 'Spyeu, Sphîeu' are simply Pokorny's parenthesised variant sp(h)ieu- written \"\n          \"out twice. Watkins/AHD has the same root as 'spyeu-. Also speu. To spew, spit. Expressive \"\n          \"root. [Pok. (s)p(h)ieu- 999.]', and Buck §4.56 SPIT (pp. 264-265) says 'IE *spyéu-, \"\n          \"spyu-, etc. ... The majority of the words for spit are of imitative origin, and most of \"\n          \"these belong to an inherited group which ... clearly reflect an IE expression.' The one \"\n          \"caveat worth recording is that all three authorities call the root imitative/expressive, \"\n          \"so 'descent' from it is looser than for an ordinary root — this matters for the Persian \"\n          \"branch (node #1).\"),\n \"note_fa\": (\"ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همه درست است. پوکورنی در ص ۹۹۹–۱۰۰۰ مدخل \"\n             \"«(s)p(h)ieu- : (s)pju-, (s)pīu- «تف کردن»» را آورده و شواهدش سنسکریت sthīvati، اوستایی \"\n             \"spāma- «آب دهان»، یونانی πτύω، لاتینی spuō/sputum، گوتی speiwan، لیتوانیایی spiauju و \"\n             \"اسلاوی کهن pljujǫ است — دقیقاً همان شاخه‌هایی که نورایی کشیده. دو صورتِ «Spyeu, Sphîeu» \"\n             \"چیزی جز نوشتنِ جداگانهٔ همان sp(h)ieu- پوکورنی نیست. واتکینز (AHD) نیز آن را «spyeu-، \"\n             \"ریشه‌ای بیانگر/صوتی» می‌نامد و باک (بند ۴٫۵۶، ص ۲۶۴–۲۶۵) می‌گوید بیشتر واژه‌های «تف کردن» \"\n             \"خاستگاه تقلید صوتی دارند ولی این گروه ارثی و هندواروپایی است. همین «صوتی» بودن ریشه است \"\n             \"که در شاخهٔ فارسی (گرهٔ ۱) دردسر می‌آفریند. داوری: ادعای نورایی درست است.\"),\n \"sources\": [W_TOF, E_SPIT],\n \"ref_check\": [\n   {\"ref\": \"POK:1000\", \"status\": \"supports\",\n    \"note\": (\"Pokorny, IEW 'Root / lemma: (s)p(h)ieu- : (s)pju-, (s)pīu-. Meaning: to spit ... \"\n             \"References: WP. II 683, WH. II 580 f. ... Page(s): 999-1000' (POK_full.txt around \"\n             \"l.80556). The cited page is the second page of the entry.\")}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW pp. 999-1000\", \"stance\": \"supports\",\n    \"note\": \"'Old Indic sthīvati \\\"spit\\\" ... Avestan spāma- \\\"saliva, mucus\\\"; gr. πτύω \\\"spucke\\\" ... Latin spuō, -ere, sputum; Gothic speiwan ... Lithuanian spiauju.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 683 (cited by Pokorny as the WP locus)\", \"stance\": \"supports\",\n    \"note\": \"Pokorny's own reference line 'WP. II 683' — the Walde-Pokorny treatment of the same root.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. spyeu- (AHD_watkins1985.txt l.993)\", \"stance\": \"supports\",\n    \"note\": \"'spyeu-. Also speu. To spew, spit. Expressive root. ... [Pok. (s)p(h)ieu- 999.]'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §4.56 SPIT, pp. 264-265\", \"stance\": \"supports\",\n    \"note\": \"'1. IE *spyéu-, spyu-, etc. Most of the forms included here are derivable by regular phonetic processes from init. *spy-. Walde-P. 2.683.' Table lists Skt. sthiv-, Av. spāma- (sb.), Grk. πτύω, Lat. spuere, Goth. speiwan, NE spit.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. pstuio, ≈ p.1086 (IEC.txt leaf 558)\", \"stance\": \"partial\",\n    \"note\": \"'pstuio (pstiuio, psth-) \\\"spit\\\". Cf. spuuo, id. Onomat. WP II, 683. Skt. sthivami ...; Per. tuff ...; Gk. ptúo ...' — same family, but Mann sets it up as an onomatopoeic *pstuio rather than *spyeu-.\"}\n ],\n \"nodes\": []\n}\n\ne4[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"tof «تُف»; tofang «تُفنگ»\", \"verdict\": \"disputed\",\n \"derivation\": (\"Two different problems. (a) تف tof 'spit': Horn no. 390 (p.87) files NP tuf \"\n   \"'Speichel' with Skt. √sthīv-, Goth. speiwan, Arm. tʿukʿ, Lat. spuō, Gk. πτύω, and Wiktionary \"\n   \"derives it from Proto-Iranian < PIE *(s)ptyēw-. But Pokorny, on the very page Nourai cites, \"\n   \"explicitly refuses the regular derivation: 'osset. tʿu, npers. tuf, tuh \\\"Speichel\\\" von einer \"\n   \"dem ai. (lexikogr.) thūtkāra-, thūthū als Wiedergabe des Spucklautes vergleichbaren \"\n   \"Lautgebärde' — i.e. NP tuf and Ossetic tʿu are treated as NEW imitative coinages of the \"\n   \"spitting noise, parallel to but not descended from *(s)pyeu-. Phonology backs Pokorny: an \"\n   \"inherited *spyu- would not surface in Persian as t-, whereas a fresh sound-gesture tuf! \"\n   \"explains the t- and the -f at a stroke. (b) تفنگ tofang is worse. It is first a blow-pipe for \"\n   \"shooting clay pellets at birds (so Borhan-e Qate' p.502: «تفنگ ... چوب دراز میان‌خالی که با \"\n   \"گلولهٔ گل و زور دهان بدان گنجشک و امثال آن زنند - و تفنگ آهنی را نیز گفته‌اند»), and only after \"\n   \"Chaldiran (1514) the matchlock. Mo'in's own footnote there calls the derivation from تف a mere \"\n   \"guess («این حدس است که کلمه از تف ... با پسوند -نگ آمده باشد»). Wiktionary and the Turkological \"\n   \"literature derive it from Chaghatay/Khwarezmian Turkic tüfeng, cognate with Karakhanid tüwek \"\n   \"'pellet blow-pipe' in the Dīwān Luḡāt at-Turk, itself onomatopoeic from the puffing noise \"\n   \"Tüf!. So 'spitter' is the right image but the wrong language: the coinage is Turkic, and the \"\n   \"Persian word is a loan back from it.\"),\n \"derivation_fa\": (\"دو مسئلهٔ جداگانه. الف) «تُف»: هرن (شمارهٔ ۳۹۰، ص ۸۷) tuf فارسی را کنار sthīv- \"\n   \"سنسکریت، speiwan گوتی، tʿukʿ ارمنی، spuō لاتینی و πτύω یونانی می‌نشاند و ویکی‌واژه آن را از ایرانی \"\n   \"باستان و در نهایت از *(s)ptyēw- هندواروپایی می‌گیرد. اما پوکورنی در همان صفحه‌ای که نورایی ارجاع \"\n   \"داده، اشتقاق قاعده‌مند را رد می‌کند: «tʿu آسی و tuf/tuh فارسی نو از حرکتِ آواییِ (Lautgebärde) مانندِ \"\n   \"thūtkāra- و thūthū در سنسکریتِ فرهنگ‌نویسان است» — یعنی واژه‌ای تقلیدیِ نوساخته است، نه بازماندهٔ \"\n   \"*spyeu-. آواشناسی هم با پوکورنی است: *spyu- ارثی در فارسی «ت» نمی‌دهد. ب) «تفنگ» دشوارتر است: \"\n   \"نخست «چوب دراز میان‌خالی که با گلولهٔ گِل و زورِ دهان بدان گنجشک زنند» بوده (برهان قاطع، ص ۵۰۲) و \"\n   \"پس از چالدران معنای سلاح آتشین گرفته. معین در همان حاشیه تصریح می‌کند «این حدس است که کلمه از تف \"\n   \"با پسوند ‑نگ آمده باشد». ویکی‌واژه و ترک‌شناسان آن را وام از تُرکیِ جغتایی/خوارزمی tüfeng می‌دانند، \"\n   \"هم‌ریشه با tüwek قراخانی در دیوان لغات الترک به معنی «زنبورک/لولهٔ دمشی»، که خود از آوای «تُف!» \"\n   \"ساخته شده است. پس تصویرِ «تف‌کننده» درست است اما زبانِ سازنده تُرکی است نه فارسی؛ فارسی آن را \"\n   \"بازوام گرفته است. داوری: پژوهش امروزی این گره را رد می‌کند.\"),\n \"sources\": [W_TOF, W_TOFANG],\n \"ref_check\": [\n   {\"ref\": \"POK:1000\", \"status\": \"contradicts\",\n    \"note\": (\"The page Nourai cites is the page that denies his arrow: Pokorny p.1000 'Armenian \"\n             \"tʿukʿ \\\"saliva\\\", tʿkʿanem \\\"spucke, speie aus\\\" ... osset. tʿu, npers. tuf, tuh \"\n             \"\\\"Speichel\\\" von einer dem ai. (lexikogr.) thūtkāra-, thūthū als Wiedergabe des \"\n             \"Spucklautes vergleichbaren Lautgebärde' — a parallel imitative formation, not a \"\n             \"reflex. Pokorny says nothing at all about tofang.\")},\n   {\"ref\": \"BQT:502\", \"status\": \"partial\",\n    \"note\": (\"BQT_v1_pages.txt leaf 730 = printed p.502: the «تفنگ» entry («چوب دراز میان‌خالی که با \"\n             \"گلولهٔ گل و زور دهان بدان گنجشک و امثال آن زنند») with Mo'in's footnote calling the \"\n             \"tof + ‑ang derivation a guess and referring to R. Frye's review article. Two pages \"\n             \"earlier (leaf 728 ≈ p.500) the «تف» entry has Mo'in's cognate footnote: «به معنی اخیر \"\n             \"در هندی باستان ṣṭhīv-, ṣṭhīvati ... ارمنی tʿu, لاتینی spuō, یونانی ptuō, کردی tef». \"\n             \"So Borhan supports 'tof' as an IE cognate but explicitly hedges 'tofang'.\")}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 390, p. 87\", \"stance\": \"supports\",\n    \"note\": \"'390. tuf \\\"Speichel\\\", tufek (\\\"spucken\\\"), tüfke (Gazoph. s.v. saliva), tufu, tuh, tuhu. ai. √sthīv-, sthīvati ...; got. speiwan; arm. tʿukʿ; lat. spuō; gr. πτύω. kurd. tef \\\"Speichel\\\" ...' — Horn's dialect form tufek is the blow-pipe/spitting derivative.\"},\n   {\"src\": \"BQT\", \"where\": \"vol.1 pp. 500 and 502\", \"stance\": \"partial\",\n    \"note\": \"IE cognates given for تف; the تفنگ etymology explicitly marked as a guess.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt, grep 'to spit'\", \"stance\": \"silent\",\n    \"note\": \"Cheung's Etymological Dictionary of the Iranian Verb has no root *spyau-/*θway- yielding tuf; the only 'spit' entries are Ossetic lixsun and a Parthian wf- — he does not set up an Iranian verb behind تف.\"},\n   {\"src\": \"HUB\", \"where\": \"HUB.txt, grep 'tuf'\", \"stance\": \"silent\",\n    \"note\": \"Hübschmann's Persische Studien does not discuss Horn no. 390.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep تفنگ/تف\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's IE-roots dictionary lists تف only under the homonym تفت/تافتن 'heat' (p.199), not under a 'spit' root, and has no تفنگ headword.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Sanskrit\", \"words\": \"sthîvâmî\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Sanskrit ṣṭhīvati 'spits' (Nourai's 'sthîvâmî' is the 1st sg. ṣṭhīvāmi of the same \"\n   \"class-I present) is the standard Indo-Aryan witness for the root. The initial ṣṭh- instead of \"\n   \"expected sp- is the classic crux: Pokorny explains it as dissimilation of *sp-y- ('sthīvati \"\n   \"... ursprünglich nur, später vorwiegend in compound with ni(h)-, daher s- from ṣ-; ṣṭ- \"\n   \"dissimil. from sp-, so that = Gothic speiwan'), so ṣṭhīv- and Gothic speiwan are one and the \"\n   \"same formation. Mann files the pair under his onomatopoeic headword pstuio: 'Skt. sthīvami, \"\n   \"pp. sthyūtah'. The past participle ṣṭhyūta- shows the zero grade *(s)pyū- that also gives Gk. \"\n   \"πτύω, which ties node #2 and node #5 together.\"),\n \"derivation_fa\": (\"سنسکریت ṣṭhīvati «تف می‌کند» (صورتی که نورایی آورده، ṣṭhīvāmi، همان اول‌شخص مفرد \"\n   \"همین فعل است) گواه اصلی هندوآریایی این ریشه است. دشواری کار در آغازهٔ ṣṭh- به‌جای sp- مورد انتظار \"\n   \"است؛ پوکورنی آن را ناهمگونی (dissimilation) از *sp-y- می‌داند و از همین رو ṣṭhīv- را دقیقاً برابر \"\n   \"speiwan گوتی می‌شمارد. اسم مفعول ṣṭhyūta- درجهٔ صفر *(s)pyū- را نشان می‌دهد، همان درجه‌ای که πτύω \"\n   \"یونانی (گرهٔ ۵) از آن ساخته شده است. داوری: درست است.\"),\n \"sources\": [W_TOF],\n \"ref_check\": [\n   {\"ref\": \"IEC:1005\", \"status\": \"not_found\",\n    \"note\": (\"Mann does have the word — 'pstuio (pstiuio, psth-) \\\"spit\\\". Cf. spuuo, id. Onomat. \"\n             \"WP II, 683. Skt. sthivami, pp: sthyūtah, id.; Hind. cf. thuk; Per. tuff; Oss. tü; \"\n             \"Arm. tʿukʿ; Gk. ptúo; Alb. pshtyj; Br. cf. tufa' — but at IEC.txt leaf 558, i.e. \"\n             \"printed p. ~1086 (the offset leaf = p/2 + 15 is exact: leaf 412 = p.794, leaf 650 = \"\n             \"p.1270). Printed p.1005 (leaf 517) carries the per-/pari-/pesna- entries, nothing \"\n             \"about spitting. Either Nourai mis-copied the number or he used a different \"\n             \"pagination; the substance of the citation is nonetheless in Mann.\")}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW pp.999-1000\", \"stance\": \"supports\",\n    \"note\": \"'Old Indic sthīvati \\\"spit, speit from\\\" ... sthyūta- \\\"gespuckt, gespien\\\"' equated with Gothic speiwan.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann ≈ p.1086 s.v. pstuio\", \"stance\": \"supports\",\n    \"note\": \"'Skt. sthivami, pp: sthyütah, id.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §4.56 SPIT, p.264\", \"stance\": \"supports\",\n    \"note\": \"the comparative table gives 'Skt. sthiv-' as the Sanskrit word for 'spit'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. spyeu-\", \"stance\": \"silent\",\n    \"note\": \"Watkins lists only the Germanic, Latin and Greek reflexes (he cites Sanskrit only rarely), so no confirmation from AHD.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Germanic\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": (\"An empty pass-through box: Proto-Germanic is the intermediate stage between the \"\n   \"PIE root and the English words in node #4. Watkins reconstructs three parallel Germanic \"\n   \"formations from *spyeu-: *spitjan (> OE spittan), *speiw- (> OE spīwan 'spew'), *spait- (> OE \"\n   \"spātl 'spittle') and *sput- (> ME spouten, Du. sputteren). The e-grade verb *spīwaną is the \"\n   \"inherited one (Goth. speiwan, ON spýja, OHG spīwan); the geminated/expressive *spitjan and \"\n   \"*sput- are Germanic-internal remakes of the same sound-image, which is why Etymonline calls \"\n   \"the root 'of imitative origin'.\"),\n \"derivation_fa\": (\"این جعبه تهی است و تنها حلقهٔ میانی میان ریشهٔ هندواروپایی و واژه‌های انگلیسیِ گرهٔ ۴ \"\n   \"را نشان می‌دهد. واتکینز از *spyeu- سه ساخت ژرمنی موازی بازسازی می‌کند: *spitjan (← spittan انگلیسی \"\n   \"کهن)، *speiw- (← spīwan «تف کردن/قی کردن») و *spait- (← spātl «آب دهان»)، و نیز *sput- (← spouten \"\n   \"انگلیسی میانه و sputteren هلندی). فعل *spīwaną با درجهٔ e صورت ارثی است (گوتی speiwan، نورس کهن \"\n   \"spýja، آلمانی علیای کهن spīwan) و گونه‌های مشدد و بیانگرِ *spitjan و *sput- بازسازی‌های درون‌ژرمنی \"\n   \"همان تصویر آوایی‌اند. داوری: درست است.\"),\n \"sources\": [E_SPIT],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"no reference is printed in this box; checked against Pokorny, Watkins and Etymonline instead (quoted below).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW pp.999-1000\", \"stance\": \"supports\",\n    \"note\": \"'Gothic speiwan. Old Icelandic spyja. Old English Old Saxon Old High German spīwan \\\"spit\\\"; Old Icelandic spýta; ... Old High German spotton \\\"mock\\\"; Middle Dutch spouden \\\"spucken, spit\\\".'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. spyeu-\", \"stance\": \"supports\",\n    \"note\": \"'1. Germanic *spitjan in Old English spittan ... 2. Germanic *speiw- in Old English spiwan ... 3. Germanic *spait- in Old English spatl ... 4. Germanic *sput- in: a. Middle English spouten; b. Dutch sputteren.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §4.56, p.264\", \"stance\": \"supports\",\n    \"note\": \"'Goth. speiwan, Du. spuwen, OHG spiwan, MHG spi(w)en, NHG speien ... ON spýta, Dan. spytte, Sw. spotta, OE spyttan, ME spitte, NE spit.'\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"spit; sputter\", \"verdict\": \"confirmed\",\n \"derivation\": (\"English spit is Old English spittan (Anglian) / spætan (West Saxon) 'expel saliva \"\n   \"from the mouth', from Proto-Germanic *spitjan, a j-present built on the same imitative base; \"\n   \"it was not even the usual Old English verb (spǣtlan and spīwan were commoner) and won out only \"\n   \"in Middle English. Sputter, 1590s, is from the other Germanic extension *sput-: it is either a \"\n   \"Low German/Dutch loan (Du. sputteren, W.Fris. sputterje) or an English formation on the same \"\n   \"pattern as spout (ME spouten, MDu. spoiten). Watkins puts both under the root — 'Germanic \"\n   \"*spitjan in Old English spittan, to spit: SPIT1 ... 4. Germanic *sput- in ... Dutch sputteren, \"\n   \"to sputter, akin to the probable Low German source of SPUTTER' — so the AHD reference Nourai \"\n   \"cites here is exact for both words.\"),\n \"derivation_fa\": (\"انگلیسی spit از spittan (گویش انگلی) و spætan (وست‌ساکسون) در انگلیسی کهن است، از \"\n   \"*spitjan ژرمنی آغازین، فعلی با پسوند ‑j بر همان پایهٔ تقلیدی؛ حتی در انگلیسی کهن هم فعل رایج نبود \"\n   \"(spǣtlan و spīwan رایج‌تر بودند) و تنها در انگلیسی میانه چیره شد. sputter از دههٔ ۱۵۹۰ و از گسترهٔ \"\n   \"دیگر ژرمنی یعنی *sput- است: یا وام از آلمانی سفلی/هلندی sputteren است یا ساختی انگلیسی بر همان \"\n   \"الگوی spout. واتکینز هر دو را زیر همین ریشه آورده است، پس ارجاع AHD که نورایی داده برای هر دو \"\n   \"واژه دقیق است. داوری: درست است.\"),\n \"sources\": [E_SPIT, E_SPUTTER],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": (\"Watkins 1985, s.v. spyeu- (AHD_watkins1985.txt ll.993-995): '1. Germanic *spitjan in \"\n             \"Old English spittan, to spit: SPIT1 ... 4. Germanic *sput- in: a. Middle English \"\n             \"spouten, to spout forth: SPOUT; b. Dutch sputteren, to sputter, akin to the probable \"\n             \"Low German source of SPUTTER.' The AHD index confirms 'SPIT1 spyeu-' and 'SPUTTER \"\n             \"spyeu-'.\")}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. spyeu- and the English index\", \"stance\": \"supports\",\n    \"note\": \"SPIT1, SPITTLE, SPEW, SPOUT, SPUTUM and SPUTTER are all listed under spyeu-.\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"archived s.vv. spit (v.1), sputter\", \"stance\": \"supports\",\n    \"note\": \"'spit (v.1) ... Old English spittan (Anglian), spætan (West Saxon) ... from Proto-Germanic *spitjan, from PIE *sp(y)eu- (of imitative origin)'; 'sputter (v.) 1590s ... cognate with Dutch sputteren, West Frisian sputterje, from Proto-Germanic *sput-'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §4.56, p.264\", \"stance\": \"supports\",\n    \"note\": \"'OE spyttan, ME spitte, NE spit' listed in the inherited group.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. spit\", \"stance\": \"supports\",\n    \"note\": \"Klein likewise derives spit from OE spittan and groups it with spew, spittle.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Greek\", \"words\": \"ptuô\", \"verdict\": \"confirmed\",\n \"derivation\": (\"Greek πτύω 'I spit' goes back to the zero grade *(s)pyu- of the root: initial \"\n   \"*spy- gives Greek πτ- (with loss of s- and the regular Greek treatment of the yod cluster), \"\n   \"and the same stem yields πτύαλον/πτυελον 'saliva' (hence English ptyalin) and the compound \"\n   \"noun in ἡμό-πτυσις 'spitting of blood' (English hemoptysis). Pokorny states it in so many \"\n   \"words — 'gr. πτύω \\\"spucke\\\", πτύαλον, πτυελον \\\"saliva\\\", πυτίζω (dissimil. from *πτυτίζω) \"\n   \"... (πτυ- from *pyu-)' — and Watkins repeats it: '6. Zero-grade form *(s)pyu- in Greek ptuein, \"\n   \"to spit: HEMOPTYSIS, PTYALIN.' Nourai's 'ptuô' is the ordinary transliteration of πτύω.\"),\n \"derivation_fa\": (\"یونانی πτύω «تف می‌کنم» از درجهٔ صفر *(s)pyu- این ریشه است: خوشهٔ آغازین *spy- در \"\n   \"یونانی به πτ- بدل می‌شود (با افتادن s- و تحول قاعده‌مند خوشهٔ همراه یای واکه‌ای)، و از همین ستاک \"\n   \"πτύαλον «آب دهان» (ریشهٔ ptyalin انگلیسی) و ἡμόπτυσις «خون‌تفی» (hemoptysis) ساخته شده است. پوکورنی \"\n   \"صریح می‌گوید «πτυ- از *pyu-» و واتکینز نیز می‌نویسد «درجهٔ صفر *(s)pyu- در ptuein یونانی». صورت \"\n   \"«ptuô» در نمودار همان آوانگاری معمول πτύω است. داوری: درست است.\"),\n \"sources\": [W_TOF],\n \"ref_check\": [\n   {\"ref\": \"IEC:1005\", \"status\": \"not_found\",\n    \"note\": \"Mann's entry containing 'Gk. ptúo, v. id.' is s.v. pstuio at ≈ p.1086 (IEC.txt leaf 558), not p.1005 (leaf 517 = the per-/pari- entries). The content of the citation is genuine, the page number is not.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW pp.999-1000\", \"stance\": \"supports\",\n    \"note\": \"'gr. πτύω \\\"spucke\\\", πτύαλον, πτυελον \\\"saliva\\\", πυτίζω ... (πτυ- from *pyu-)'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. spyeu-\", \"stance\": \"supports\",\n    \"note\": \"'6. Zero-grade form *(s)pyu- in Greek ptuein, to spit: HEMOPTYSIS, PTYALIN.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §4.56, p.264\", \"stance\": \"supports\",\n    \"note\": \"the table's Greek entry for SPIT is πτύω, with NG pop. φτύνω.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann ≈ p.1086 s.v. pstuio\", \"stance\": \"supports\",\n    \"note\": \"'Gk. ptúo, v. id.' in the same entry as Skt. sthivami and Pers. tuff.\"}\n ]\n})\n\ndoc[\"entries\"].append(e4)\nout='/home/sfmqrb/git/rishe/data/verification/page-471.json'\njson.dump(doc, open(out,'w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint('written', out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build2-471.py\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-471.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 471"
}
```


### [2026-09-14T02:49:30.700Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-471.json
JSON OK
nodes verified: 15/15
node verdicts: {'plausible': 5, 'disputed': 2, 'confirmed': 8}
root verdicts: {'plausible': 1, 'disputed': 1, 'confirmed': 1}
ref checks: {'supports': 6, 'partial': 6, 'not_found': 3, 'not_checked': 3, 'contradicts': 1}
books consulted: {'partial': 9, 'silent': 12, 'supports': 28, 'contradicts': 3} | by book: {'HRN': 5, 'KLN': 5, 'HUB': 4, 'SYN': 4, 'AHD': 4, 'NYB': 3, 'MON': 3, 'IEC': 3, 'BQT': 3, 'ETYMONLINE': 3, 'POK': 3, 'PHD': 2, 'ARY': 2, 'WLD': 2, 'SOD': 1, 'AFM': 1, 'PLA': 1, 'FVQ': 1, 'SKT': 1, 'CHEUNG': 1}
```


## [2026-09-14T02:49:52.853Z] AGENT

Page 471 verified — `/home/sfmqrb/git/rishe/data/verification/page-471.json` written, `verify_check.py 471` reports 15/15 nodes, **0 PROBLEM lines**.

**Counts** — nodes: 8 confirmed, 5 plausible, 2 disputed. Roots: 1 confirmed, 1 plausible, 1 disputed. Ref checks: 6 supports, 6 partial, 1 contradicts, 3 not_found, 3 not_checked.

**Disputed / problem items**
- **ROOT `Spongo` (IE, "fluffy, empty")** — there is no PIE root. Gk. σπόγγος/Attic σφόγγος is a Pre-Greek Mediterranean Wanderwort (Beekes; de Vaan "borrowed independently into Greek, Latin and Armenian in a form *sphong-"; Klein "borrowed from an unknown source"). Even Walde-Pokorny, the cited authority, offers no IE etymology, and their gloss is "porous", not "fluffy, empty".
- **`Spongo` #2 Pahlavi `spynj`** — the whole Iranian branch is misfiled. MP ʾspynj = *aspinǰ* means only "hospitality; inn" (MacKenzie p.13), never "sponge/hollow"; Nyberg p.33 calls it an Aramaic loan (Talm. ʾwšpyzʾ, Syr. ʾespezzā), Wiktionary/Ciancaglini reverse the direction — nobody connects it with σπόγγος, and σπόγγος has no affricate to give -nǰ. Nodes #3 (sepanj) and #4 (Sogdian) inherit the error; the MP→NP and MP→Sogdian edges themselves are fine (Gharib SOD p.64 no.1628 explicitly: "(ʾ)spanc < Parth. MP ʾspynj").
- **`Spyeu` #1 Persian `tof`, `tofang`** — POK:1000, the page Nourai cites, **contradicts** him: Pokorny puts NP *tuf* / Oss. tʿu with Skt. thūtkāra- as a *new* imitative Lautgebärde, not a reflex (an inherited *spyu- would not give t-). *tofang* is worse: originally a pellet blow-pipe (BQT p.502), from Chaghatay/Khwarezmian Turkic *tüfeng* (cf. Karakhanid *tüwek*); Mo'in's own footnote there calls the tof + -ang derivation "a guess".

**Other findings (no extraction errors — the JSON is faithful to the printed page, checked on the 300dpi render, copied to `data/verification/sources/refs/ocr/BOOK/471.png`)**
- `WLD2:621` is Nourai's own misprint: WP II 621 = "(s)teg-"; the `spongo-` lemma is WP II **681**. The book prints 621.
- `IEC:1005` (twice) does not exist: Mann's entry `pstuio` "spit" (with Skt. sthivami, Gk. ptúo, Per. tuff) is at ≈ p.1086.
- `TAD:35` — the إسفنج entry is genuine ("يوناني σπόγγος") but sits near p.2 of the 1932 Cairo scan, not p.35.
- Glosses in entry 0: Av./MP/NP *spiš/šepeš* mean **louse**, not "flea" (Bartholomae "Laus", Horn 705, MacKenzie, Mo'in) — hence the root and both nodes are `plausible` rather than confirmed.
- `VFO:22` is unresolvable (project's MISSING_REFERENCES: probably = Moshiri's dictionary of *European* loanwords — itself a hint at how sepanj got misclassified).
