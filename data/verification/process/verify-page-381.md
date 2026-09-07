# Verification process log — verify-page-381


## [2026-09-07T20:36:55.871Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 381 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-381.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-381.json. Write /home/sfmqrb/git/rishe/data/verification/page-381.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 381` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:36:58.314Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-07T20:36:58.990Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:36:59.009Z] TOOL RESULT

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


## [2026-09-07T20:36:59.624Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-381.txt"
}
```


### [2026-09-07T20:36:59.643Z] TOOL RESULT

```
1	=== PDF page 381 (book page 351) ===
2	--- entry 0 ---
3	ROOT [Iranian] Pambak, Bambak : cotton  (refs SYN:402)
4	#1 (parent #0) [Pahlavi] refs=BQT:419; MON:814 | panbak, pambak : cotton
5	  #2 (parent #1) [Persian] refs=BQT:419; MON:814 | panbeh «پنبه» : cotton, to have cotton in ears means to be ignorant
6	    #3 (parent #2) [Greek] refs=KLN:185 | bombax : silk cotton
7	      #4 (parent #3) [Latin] refs=KLN:185 | bombyx
8	        #5 (parent #4) [French] refs=None | 
9	          #6 (parent #5) [English] refs=KLN:185 | bombast, bombazine : soft padding
10	#7 (parent #0) [Aramaic] refs=SYN:402 | bambak : cotton
11	--- entry 1 ---
12	ROOT [Indo-European] Parîkâ : sweet heart, fairy  (refs POK:789)
13	#1 (parent #0) [Avestan] refs=POK:789; KLN:1115 | pairikâ : beautiful woman | NOTE: AEF:375 has a discussion on the original meanings of "pairikâ" as a seducer.
14	  #2 (parent #1) [Pahlavi] refs=POK:789; KLN:1115 | parîk : fairy
15	    #3 (parent #2) [Persian] refs=POK:789; KLN:1115; HRN:69; BQT:396,864 | parî «پری» : fairy; beautiful woman | extra: پریسا ، پریدخت ، پریچهر ، پریپوش
16	      #4 (parent #3) [English] refs=KLN:1158; SKT:384 | Peri : fairy
17	#5 (parent #0) [Semitic] refs=None | 
18	  #6 (parent #5) [Arabic] refs=KLN:1115 | Bilqîs : queen of Šaba (Saba) | NOTE: KLN links this word to the other words in the chart but does not provide details.
19	    #7 (parent #6) [Persian] refs=MON5:277 | Belqîs «بلقیس» : queen of Saba
20	#8 (parent #0) [Greek] refs=KLN:1115 | pallas : maiden ; Pallas : a Greek goddess protecting Troy
21	  #9 (parent #8) [Latin] refs=KLN:1115 | 
22	    #10 (parent #9) [English] refs=KLN:1115 | palladium : a metallic element
23	--- entry 2 ---
24	ROOT Parni -> redirect to Parth
25	
```


## [2026-09-07T20:37:04.304Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-381.json",
 "description": "Read source JSON for page 381"
}
```


### [2026-09-07T20:37:04.342Z] TOOL RESULT

```
{
  "pdf_page": 381,
  "book_page": 351,
  "entries": [
    {
      "root": {
        "name": "Pambak, Bambak",
        "lang": "Iranian",
        "refs": "SYN:402",
        "gloss": "cotton"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:419; MON:814",
          "words": [
            {"translit": "panbak, pambak", "gloss": "cotton", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:419; MON:814",
          "words": [
            {"translit": "panbeh", "gloss": "cotton, to have cotton in ears means to be ignorant", "script": "پنبه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نظامی بس کن این گفتار خاموش - چه گویی با جهان پنبه در گوش",
            "poet": "Nezâmî"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Greek",
          "refs": "KLN:185",
          "words": [
            {"translit": "bombax", "gloss": "silk cotton", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "KLN:185",
          "words": [
            {"translit": "bombyx", "gloss": null, "script": null}
          ],
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
          "refs": "KLN:185",
          "words": [
            {"translit": "bombast, bombazine", "gloss": "soft padding", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "SYN:402",
          "words": [
            {"translit": "bambak", "gloss": "cotton", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Parîkâ",
        "lang": "Indo-European",
        "refs": "POK:789",
        "gloss": "sweet heart, fairy"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:789; KLN:1115",
          "words": [
            {"translit": "pairikâ", "gloss": "beautiful woman", "script": null}
          ],
          "script_extra": null,
          "note": "AEF:375 has a discussion on the original meanings of \"pairikâ\" as a seducer.",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "POK:789; KLN:1115",
          "words": [
            {"translit": "parîk", "gloss": "fairy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:789; KLN:1115; HRN:69; BQT:396,864",
          "words": [
            {"translit": "parî", "gloss": "fairy; beautiful woman", "script": "پری"}
          ],
          "script_extra": "پریسا ، پریدخت ، پریچهر ، پریپوش",
          "note": null,
          "quote": {
            "text": "طفیل هستی عشقند آدمیّ و پری - ارادتی بنما تا سعادتی ببری",
            "poet": "Hâfez"
          }
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:1158; SKT:384",
          "words": [
            {"translit": "Peri", "gloss": "fairy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Semitic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Arabic",
          "refs": "KLN:1115",
          "words": [
            {"translit": "Bilqîs", "gloss": "queen of Šaba (Saba)", "script": null}
          ],
          "script_extra": null,
          "note": "KLN links this word to the other words in the chart but does not provide details.",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON5:277",
          "words": [
            {"translit": "Belqîs", "gloss": "queen of Saba", "script": "بلقیس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همچو آن هدیه که بلقیس از سبا - بر سلیمان می فرستاد ای کیا",
            "poet": "Molavî"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:1115",
          "words": [
            {"translit": "pallas", "gloss": "maiden", "script": null},
            {"translit": "Pallas", "gloss": "a Greek goddess protecting Troy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Latin",
          "refs": "KLN:1115",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "KLN:1115",
          "words": [
            {"translit": "palladium", "gloss": "a metallic element", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Parni", "redirect": "Parth"},
      "nodes": []
    }
  ]
}
```


## [2026-09-07T20:37:04.816Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:37:04.854Z] TOOL RESULT

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


## [2026-09-07T20:37:11.797Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['SYN','KLN','POK','BQT','MON','HRN','SKT','WLD','AHD','IEC','PHD','NYB','BRT','LKT','FSD','WEB','ARY','PLA','AFM','FVQ','HUB','AEF','LEW','LAT']:\n    if k in d:\n        print('==',k, json.dumps(d[k], ensure_ascii=False)[:900])\n    else:\n        print('==',k,'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-07T20:37:13.128Z] TOOL RESULT

```
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leave
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword bold at line start; e
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "covers_etymology": true, "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.", "
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
== AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فر
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.", "notes": ""}
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_
```


## [2026-09-07T20:37:23.600Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN cotton section ===\" && grep -n -i \"COTTON\" SYN.txt | head -40",
 "description": "grep SYN for cotton"
}
```


### [2026-09-07T20:37:23.651Z] TOOL RESULT

```
=== SYN cotton section ===
143:Classification. The arrangement of word lists by subjects is an old story. Not to mention the “‘determinatives” or “classifiers” of Sumerian, Chinese, etc., there were in the Indo-European field many such Greek glossaries culminating in the ’Ovouacrixd of Pollux, likewise in Latin (for the Greek and Latin works of this type, cf. Pauly-Wissowa, s.v. Onomastikon), the Sanskrit Amarakoga (all the native glossaries were more or less of this type), similarly Latin-Old English (as Aelfrie’s Vocabulary), Latin—Old High Ger- man (as Heinrici Summarium), Latin-Cornish (the Cottonian Vocabulary), German-Old Prussian, etc. In modern times there have been numerous dic- tionaries of the leading European languages known variously as ‘analogi- cal’, ‘analytical’, ‘ideological’, ‘methodical’, ‘synthetic’, ‘topical’; and, the best known and imitated, Roget’s Thesaurus. Of all these, no two, apart from direct imitations, will agree in the order or classification. For ex- ample, Pollux thought proper to begin with the gods (so in many other lists), passing to man (with the parts of the body), relationship, science and art, hunting, meals, trades, law, town organization, utensils. Aelfric began with agricultural tools, passing to men (by office or craft), diseases, law, in- sects, vessels, drinks, birds, plants, trees, arms, winds, cereals, clothes, physi- cal world, parts of the body, colors. But actually all sorts of miscellaneous items are mixed in. In Roget’s Thesaurus the parallelism of opposites and some of the minor subdivisions may be convenient. But the main groups and larger subdivisions are so comprehensive as to have no obvious co- herence. What may one not find under Motion (e.g. eat, food) or Volition (e.g. clean)! The fact is, of course, that relations are too complex to admit any truly scientific and complete classification (cf. the remark of J espersen, Philosophy of Grammar 34); and, even if such were possible, it would have little relation to our instinctive associations.
9942:‘Cloth’ is considered here primarily as the generic term for fabrics like wool, cotton, linen, etc., but also as a piece of such fabric, ‘a cloth’, some of the words being used mainly or only in the latter sense.
9944:Some of the words listed are less gener- ic than NE cloth, with differentiation be- tween woolen and linen or cotton cloth.
9998:Linen, considered here as a material for clothing parallel to wool, cotton, etc., was originally denoted by the same word as that for the raw material, flax. But ‘linen’ and ‘flax’ are now generally differentiated, partly by parallel forms
10023:SCr. bez, fr. Turk. (orig. Arab.) bez ‘linen or cotton cloth’. Lokotsch 280.
10029:402 SELECTED INDO-EUROPEAN SYNONYMS 6.24 COTTON NG prapraxe Dan. bomuld Lith.  medvilné, bovelna- It. cotone Sw. bomull Lett. kuokvilna Fr. coton ME cotoun, coton SCr. pamuk Sp. algodén NE colton Boh. bavina Rum. bumbac Du. katoen, boomwol Pol. bawelna NIr. _canach, cadas MHG kattiin, boumwolle Russ. chlopok W. colwm NHG  baumuvolle Skt. karpasa- Br. kotoris
10030:European names for cotton are mostly borrowed with the plant from oriental sources.
10032:It. cotone, Fr. coton (> Br. kotofis), Sp. algodén, ME cotoun, coton (> W. colwm), NE cotton, Du. katoen, MHG kattin (NHG kattun ‘calico’).
10036:MHG boumwolle, bounwolle, bowmwol, etc., NHG baumwolle, LG bomwolle, Du. boomwol, lit. ‘tree wool’. Cf. Hdt. 3.106 (of Indian cotton) ra 62 dévpea ra wypia abroi dépe xapmov etpra. But possibly the first part was orig. bamb or bomb fr.
10043:NI. cadas (given first by McKenna s.v. colton), fr. ME cadas (NE caddis) a sort of coarse cotton or wool used in padding, fr. OFr. cadaz, cadas, further orig. unknown. NED s.y. caddis. Macbain 74.
10045:5. Skt. karpdsa-, loanword fr. the same source as Grk. xapmacos, Lat. car- basus ‘fine cotton cloth’, Arab. kerpas, etc. Walde-H. 1.165.
10058:Russ.—ChSl. godovabli, Boh. hedudbt (> Pol. jedwab) fr. Gme., cf. OHG gotawebbi ‘any fine expensive cloth’, gl. also sericum, ON gudvefr, OE godweb ‘velvet, purple, fine cloth’, perh. lit. ‘God’s cloth’, i.e. ‘fine cloth suitable for use in God’s service’, though the first member may be transformed fr. Arab. quin ‘cotton’ (6.24). Berneker 316. Briickner 204.
10468:It. giubba (old word for ‘coat’, now mostly specialized), fr. Arab. gubbah ‘cotton undergarment’ (whence also Fr. jupe ‘skirt?), REW 3951. Lokotsch 737.
10578:Tr. jupe, dim. jupon, fr. Arab, gubbah ‘cotton undergarment?. REW 3951. Iokotsch 737.
10596:Russ. jubka, through Turk. and Pers., fr. Arab. gubbah ‘cotton undergarment’, whence also Fr. jupe (above, 2). Berne- ker 460.
11265:13th cent.) Rum. basma (also Turk. basma ‘printed cloth’. 9 of Nit. ciarsiir (also ‘kerchief’), bor- rowed fr. NE kerchief in some dial. pronunciation. W. cadach (poced), lit. ‘pocket-cloth’, cf, cadach ‘cloth, rag, kerchief’ (= NIv. cadach ‘calico’, prob. : W. cadas, NIr. cadas, fr. ME cadas (NE caddis), with suffix after NIr. canach ‘cotton’ (?). See under ‘cotton’ (6.24). W. hances, fr. a vulgar form of NE handkerchief (cf. hanky).
16757:Grk. orpégw (in late times ousting | tpexw, Which does not occur in the NT or in NG) : orpeBdés ‘twisted, bent’, orpo¢gos ‘string’ (fr. ‘twisted’?), etc., out- j side root connection? Boisacq 919. . Grk. 7vAloow, NG rudAlvw : rbdos ‘knot, callus, bolt’, 7dAn ‘callus, cushion’, ON pollr ‘(young) tree, peg’, OE fol ‘peg’, Skt. uila- ‘tuft, wisp, cotton’, etc., TE *teu- ‘swell’. Walde-P. 1.709f. Boi- sacq 990.
32464:SS are most commonly written. Only the Russ. bumaga, from an oriental word for ‘cotton’, reflects a later process.
32481:4. Russ. bumaga, Ukr. bumaha, of the same orig. as SCr. pamuk, etc. ‘cotton’ (6.24). Berneker 100 f.
```


## [2026-09-07T20:37:24.601Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN bombast ===\" && grep -n -i \"bombast\\|bombazine\\|bombasine\\|bombyx\\|bombax\" KLN_1966.txt | head -30",
 "description": "grep KLN for bombast"
}
```


### [2026-09-07T20:37:24.661Z] TOOL RESULT

```
=== KLN bombast ===
5311:bombardon,  n.,  a  musical  instrument.  —  It.  bom- bar  done,  augment,  of  bombardo,  fr.  bombardare. See  bombard,  n.,  and  -oon. bombasine,  n.  —  See  bombazine, bombast,  n.,  high-sounding  speech.  —  From Bombastic,  lit.  ‘in  the  style  of  Bombastus  Para¬ celsus’  (1493-1541).  The  PN.  Bombast  comes  fr. ML.  bombdeium,  fr.  Gk.  [topjtoxiov,  ‘cotton’. See  Bornbyx.
5312:Derivatives:  bombast-ic,  adj.,  bomhast-ic-al-ly, adv.,  bombast-ry,  n.
5313:bombazine,  bombasine,  n.,  twilled  silk  cloth  with worsted  or  cotton.  —  F.  bombasin,  fr.  ML.  bom¬ bdeium,  fr.  Gk.  naii^axiov,  ‘cotton’.  See  Bom- byx.
5316:Bombyx,  n.,  a  genus  of  moths,  the  silkworm  moth (entomol.)  —  L.  bombyx,  ‘silkworm’,  fr.  Gk. [top. (to',  fr.  (3a(i.jJaxiov,  assimilated  form  of Ttappaxtov,  ‘cotton’,  fr.  Pers.  piinba,  ‘cotton’. Cp.  bombast,  bombazine, bona  fide,  in  good  faith.  —  L.  bond  fide,  abl.  of
16560:grandiloquent,  adj.  —  Formed  with  sulf.  -ent  fr. L.  grandiloquus,  ‘speaking  loftily,  bombastic’, fr.  grandis,  ‘great,  lofty’,  and  loqui,  ‘to  speak’. See  grand  and  loquacious.
17788:highboy,  n.,  a  high  chest  of  drawers.  —  A  hybrid formed  fr.  E.  high  and  F.  bois,  ‘wood’.  See  bush and  cp.  hautboy.  Cp.  also  tallboy,  lowboy, highfalutin,  highfaluting,  adj.,  bombastic;  n., bombast.  —  Of  uncertain  origin, highly,  adv.  —  ME.  heghly,  heyly,  fr.  OE.  healice, formed  fr.  heah,  ‘high’,  with  suff.  -lice.  See  high and  adv.  suff.  -ly.
26604:Orontium,  n.,  a  genus  of  plants,  the  golden  club (bot.)  —  ModL.,  prob.  fr.  Orontes,  a  river  of Syria.  For  the  ending  see  1st  suff.  -ium. orotund,  adj.,  1)  full,  resonant  (said  of  the  voice); 2)  pompous,  bombastic  (said  of  the  style  of utterance).  —  L.  (Horace,  Ars  Poetica,  323)  ore rotundo,  ‘with  a  round  mouth',  abl.  of  os  ro- tundum,  fr.  os,  gen.  oris,  ‘mouth’,  and  neut.  of rotundus,  ‘round’.  See  oral  and  rotund. Derivative:  orotund-ity,  n. orphan,  n.  —  Late  L.  orphanus,  fr.  Gk.  opqnxvoc, ‘without  father  or  mother,  orphaned’,  which  is cogn.  with  L.  orbus,  ‘bereft’,  OI.  arbhah,  ‘weak, child’.  Arm.  orb,  ‘orphan’,  arbaneak,  ‘servant, assistant',  OIr.  orbe,  orpe,  ‘heir’,  OSlav.  rabu, ‘slave’,  rabota,  ‘servitude,  slavery’,  Goth,  arbja, OHG.  arpeo,  erbo,  MHG.,  G.  erbe  (m.), OFris.  erva,  ON.  arfi,  OE.  ierfa,  ‘heir",  Goth. arbi,  OHG.  arbi,  erbi,  MHG.,  G.  erbe  (n.), OFris.  erve,  OS.  erbi,  OE.  ierfe,  ‘inheritance’, Goth,  arbaips,  ‘hardship,  toil,  work’,  OHG. arabeit,  MHG.  arebeit,  arbeit,  of  s.m.,  G.  Arbeit, ‘work’,  OFris.  arbed,  OS.  arabed(i),  ON.  erfidi, OE.  earfod,  ‘hardship,  suffering,  trouble’.  Cp. robot.
31664:rant,  intr.  v.,  to  speak  in  a  bombastic  way.  — Fr.  earlier  (now  obsol.)  ModDu.  ranten,  ‘to dote’.  Cp.  randy.
```


## [2026-09-07T20:37:36.164Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10028,10048p' SYN.txt",
 "description": "Read SYN 6.24 COTTON section"
}
```


### [2026-09-07T20:37:36.220Z] TOOL RESULT

```
Digitized by Arya Samaj Foundation Chennai and eGangotri
402 SELECTED INDO-EUROPEAN SYNONYMS 6.24 COTTON NG prapraxe Dan. bomuld Lith.  medvilné, bovelna- It. cotone Sw. bomull Lett. kuokvilna Fr. coton ME cotoun, coton SCr. pamuk Sp. algodén NE colton Boh. bavina Rum. bumbac Du. katoen, boomwol Pol. bawelna NIr. _canach, cadas MHG kattiin, boumwolle Russ. chlopok W. colwm NHG  baumuvolle Skt. karpasa- Br. kotoris
European names for cotton are mostly borrowed with the plant from oriental sources.
1. Arab. guin, qutun (Sp.-Arab. go- tun). Schrader, Reallex. 1.84. Lo- kotsch, 1272. REW 4796a.
It. cotone, Fr. coton (> Br. kotofis), Sp. algodén, ME cotoun, coton (> W. colwm), NE cotton, Du. katoen, MHG kattin (NHG kattun ‘calico’).
2. An oriental word, perh. orig. Irani- an, represented by Pahl. pambak, Osset. bambag, NPers. panba, Arm. bambak. Schrader, loc. cit. Berneker 100 f.
Hence late Lat. bombazx ‘linteorum aut aliae quaevis quisquiliae’ (Du Cange), bombacitum (> NE bombasine, bombast, Fr. bombasin, etc.), and ap- parently Grk. Boufvt (> Lat. bombyz) ‘silkworm, silk’.
Here also NG prapréx, Rum. bumbac, SCr. pamuk, but by the mediation of different Turkish forms (cf. Berneker, loc. cit.).
MHG boumwolle, bounwolle, bowmwol, etc., NHG baumwolle, LG bomwolle, Du. boomwol, lit. ‘tree wool’. Cf. Hdt. 3.106 (of Indian cotton) ra 62 dévpea ra wypia abroi dépe xapmov etpra. But possibly the first part was orig. bamb or bomb fr.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
the same source as Lat. bombaz, ete, (above) and transformed by popular connection with baum ‘tree’. Falk. Torp 92. :
Dan. bomuld, Sw. bomull, fr. LG bom- wolle with translation of the final mem- ber.
Lith. medvilné, Lett. kuokvilna, lit, ‘tree wool’, semantic borrowings fr. NHG baumwolle.
Pol. bawetna (> Lith. bovelna), Boh. bavina, fr. NHG baumwolle with ba- for baum- and translation of final (cf. Dan. bomuld, above). Briickner 18.
3. NIr. canach (also Gael.) : Ir. ca- nach ‘down, fuzz’, etym.? Macbain 68.
NI. cadas (given first by McKenna s.v. colton), fr. ME cadas (NE caddis) a sort of coarse cotton or wool used in padding, fr. OFr. cadaz, cadas, further orig. unknown. NED s.y. caddis. Macbain 74.
4, Russ. chlopok : chlop’e ‘flocks (of wool), flakes (of snow)’, Boh. chlupaty ‘hairy’, Pol. dial. chtwpy ‘tufts’, other- wise obscure. Berneker 390 f.
5. Skt. karpdsa-, loanword fr. the same source as Grk. xapmacos, Lat. car- basus ‘fine cotton cloth’, Arab. kerpas, etc. Walde-H. 1.165.
of the words for ‘silk’, like the oriental origin. tal word represented 2 ian sirghe, Mongolian sirkek. Et isnate source is dub., the old identification with a Chinese word be- ing unsubstantiated. Cf. Schrader, Reallex. 2.382; Laufer, Sino-Iranica 538 ff, who thinks the word of Iranian origin. Grk. onpixés adj., onpixdy (onp ‘silk- worm’, Dijpes being later back-forma- tions), Lat. séricus adj., séricum, whence Ir. siric, OHG serth. The earliest Grk. reference to ‘silk’, but without the word, is supposed to be Aristot. HA 551°13. Miss Richter, AJA 1929, 27 ff., argues for much earlier use of silk, Pie fat, Russ, Sell, Lith. éilkai, . silkas, borrowed independently
ftom the Orient (rather than through mpixoy, etc)
The Balto-Slavic
```


## [2026-09-07T20:37:38.711Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=5316{n+=gsub(/\\f/,\"\\f\")} END{}' KLN_1966.txt; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# count formfeeds up to line 5316\npre='\\n'.join(lines[:5316])\nprint('formfeeds before line 5316:', pre.count('\\f'))\nEOF",
 "description": "Locate KLN leaf for bombast"
}
```


### [2026-09-07T20:37:40.143Z] TOOL RESULT

```
formfeeds before line 5316: 108
```


## [2026-09-07T20:37:55.656Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (106,107,108,109):\n    p=pages[i]\n    print('--- leaf',i,'len',len(p))\n    print(p[:300].replace('\\n',' | '))\nEOF",
 "description": "Inspect KLN leaves around bombast"
}
```


### [2026-09-07T20:37:57.024Z] TOOL RESULT

```
--- leaf 106 len 11788
erred  to.  Cp.  also  blenny. blennorrhea,  blennorrhoea,  n.,  excessive  discharge of  mucus  ( med .)  —  Medical  L.,  compounded  of blenno-  and  -rrhea. | blenny,  n.,  a  small  seafish.  —  L.  blenttius,  fr.  Gk. (3X£vvoc;,  name  of  a  fish,  fr.  pXlvva,  ‘slime’,  lit. ‘slime  fish’;  
--- leaf 107 len 11874
the  original  meaning  of  base *bhlo-  see  blow,  ‘to  puff’. | Derivatives:  blow,  n.,  blow-er,  n.,  blow-ing.  n. | blow,  stroke,  n.  — -  ME.  blewe,  rel.  to  OS.  bleu- wan,  MDu.,  Du.  blouwen,  OHG.  bliuwan, MHG.  bliuwen,  G.  bleuen,  Goth,  bliggwan,'  to strike’,  fr.  Teut.  *bleu
--- leaf 108 len 11902
unning  to  aid’,  lit.  ‘running  on  hearing  a  cry’, fr.  (3ot),  ‘a  cry,  shout’,  and  -8p6[xoi;,  ‘running’, which  is  rel.  to.  Spoken;,  ‘a  running’.  For  the first  element  see  reboant  and  cp.  Boethusian,  for the  second  see  dromedary. | Boehmeria,  n.,  a  genus  of  plants  of
--- leaf 109 len 11541
  ME.  bond,  a var.  of  band.  See  band,  ‘a  tie’,  and  cp.  the  first element  in  bonspiel. | Derivatives:  bond,  tr.  v.,  bond-ed,  adj. | bond,  n.,  serf  (archaic).  —  ME.  bond,  ‘husband, householder’,  fr.  OE.  bonda,  ‘householder’,  fr. ON.  bondi,  for  biiandi,  ‘householder’,  li
```


## [2026-09-07T20:38:08.485Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN_1971 bombyx/bombast ===\" && grep -n -i \"bombast\\|bombyx\" KLN_1971.txt | head -10",
 "description": "grep KLN 1971 for bombast"
}
```


### [2026-09-07T20:38:08.541Z] TOOL RESULT

```
=== KLN_1971 bombyx/bombast ===
31577:bombast, n., high-sounding speech. — From 
31578:Bombastic, lit.; ‘in the style of Bombast us Para- 
31579:celsus’ (1493- 1 541). The PN. Bombast comes fr. 
31581:See Bombyx. 
31583:Derivatives: bombast-ic, adj., bombast-ic-al-ly , 
31584:adv., bombast-ry, n. 
31602:Bombyx, n., a genus of moths, the silkworm moth 
31603:(entomol.) — L. bombyx , ‘silkworm’, fr. Gk. 
31607:Cp. bombast, bombazine, 
105350:L. grandiloquus , ‘speaking loftily, bombastic’,
```


## [2026-09-07T20:38:09.487Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پنبه\" BQT_v1_pages.txt | head -20",
 "description": "grep BQT v1 for panbeh"
}
```


### [2026-09-07T20:38:09.543Z] TOOL RESULT

```
13568:ابا ك - بکر اولبروزن دلشاد, پنبه زن
17341:باشد که زنان پنبه ای که خواهند بربسند دد
18570:پنبه باند که بعربی فطن خوانند و شحم الارض
21156:- و بکسر اول رسمانی که در محل رشتن پنبه
23437:رمهمثرین محصولات نکن وبرنج و کنف وپنبه وچای است » معلدن آن نفت» زغال سنگه ,
26391:داب زوا هکره پنبه کی - بنم کاف امر است ‏ یعنی
26393:پنبه بز » بنتح اول و بای ابجد بروزن
26395:پنبه در گوش کنابه ازمیدم‌غافل
26398:"وش افکندن ,پنبه در گوش گردت؛حر‌يك
26405:پنبه نهادن - کنایه از فرب دادن
26422:غوزء غکفته پنبه ‏ و آن نبانی است از خانوادة ۷12۱۷۵0666
29037:لته زر دن «کنابه از پنبه را حلاجی
29722:8 صنایع ساجی : پنبه, ابرشم» قالی وم سازی .
32092:کوبند ‏ و پنبه‌ای که آن را بدست از هم
```


## [2026-09-07T20:38:14.082Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26370,26430p' BQT_v1_pages.txt && echo \"----- nearest page tags -----\" && awk 'NR>=26200 && NR<=26440 && /pdf page/{print NR\": \"$0}' BQT_v1_pages.txt",
 "description": "Read BQT panbeh entry"
}
```


### [2026-09-07T20:38:15.366Z] TOOL RESULT

```
از دو قطعه ارچ سفید از جنس پتبه که بروی دهان آویخته با دو نوار پیشت سر کره میززنشد .
زرنستیان ایران آن دا هروبند» لمتد. این برد؛ کوچك که بنا بتوضیحات ضیر پپلوی اوستا باید
دوبند انگشت پاین‌تر ازدهان باشد» دروقتی بکاربرده ممشودکه موبد درمقابل آتش مقدی » اوستا
سراید ومراسم دیتی بجاآورد . استعمال پنام برای آن‌است که نفی وبخار دهن‌بعتصر حقدی‌ترسد.
پنام‌از لوازم آ تربانان (موبدان) است. #يشت ۱ص ۷۹۳ و۲۹۵ ح و۳۵۵4
بتا ! نگارا ! ازچشم بدبترس همی چرا نداری پاخویشتن همی تو ینام ؛
ازین بیت پیداست که مراد همان روبند است نه‌تمویذ (مذ کور درعتن) وفرهنگه‌نویسان
مقر منة چشم بد چنن درك کرده‌اند 1 «کاتها ص۱۲ . زرانشت هرام در اردای وبراف نامه کوبد:
بشد برغخت زر اردای وبراف ۱ پنامی بررخ و کستی‌اش برناف .
۴ بهلوی 0۵0۵ [ ۳202۵10 یناهی. بناه بردن | از ۶02)8۵1 0808۵1 #از
2 * « تیب رکه ۱۱۹ بنقل‌از هوشمان» و رك: اسشق ۳۲۸-۳۲۷ .کردیدن. و ا زکسی بی‌موجب برربدن‌هم؛ 9
نبه کر دن هد کنابه از گررشتن -
و آریزایدن- وپرشان وپرا کنده ساختن‌ومتفرق
گردانیدن باشد - و کنایه از خاموش کردن -
و دقم و محو لمودن - و منکر شدن- و علجز
نعتی دنام هی آور ‌ ۱ ۰
بناهنده؟ بی وزن پرا کنده» بمعنی 1
پتاه گر نده باشد.
بناهیك » بررزن دوانید , یعنی یکی
یناه آورد +
پناهیده- بر وزن جفا پیشه ۰ بمه‌نی گرریدن هم هس .
داب زوا هکره پنبه کی - بنم کاف امر است ‏ یعنی
محو کن- ومنکرشو - و خاموش باشسوبگویز .
پنبه بز » بنتح اول و بای ابجد بروزن
کنده‌یز ۳ حلاج و تداف وشه ژترا گوینث.
پنبه در گوش کنابه ازمیدم‌غافل
وسخن لاشئو باشد .
بنبه در گوش نهادن. , پبه در
"وش افکندن ,پنبه در گوش گردت؛حر‌يك
ممتی دارد که کنابه از غفلت داشتن و سخن
ناشنوون باشد . ۱
فنبه‌دن - بازای هوز بروزنک رکدن,
حلاح ونداف را گوشد ِ
نب ششان «بمنی‌نرم وساف‌وسفیدشدن
باشد - و کنابه از گربختن وعتفرق و پرشان
پنبه نهادن - کنایه از فرب دادن
باشد و کنایه ازراضی ساختن کسی را در امری.-
بابجابی روانه کردن هم هست.
باه و ر « با راو . بی وزن ومعنی ینبه
بز باشد که حلاج و نداف است » چه در فارسی
با بواو وبرعکس تبدیل‌می‌باید, چنانکه درفواید
۰ ۵
اس .
بنج س بفتح اول بر وزن دغج» عددی
است معروف ۴ - و اشاره بحوای خسه هم
هست که ساممه و باصره و ذابقه ولامسه و شامه
باشد - و بکسر اول کرفتن عضوی باشد باس دو
ناخن چنانکه سرد آبد ۵ .
رم پبه -بفتم‌اول و کسر-وم (لهجةم رکزی),پیلوی
۰ 000 02: تارادیا۱۱۳ > گلکی026 0267
7 ی د. س ۲۸ ۰ شهمیرزادی 08۳008 « ۵.
۲ص۱۸۲»! قطن بزبان علمی 055011110):
غوزء غکفته پنبه ‏ و آن نبانی است از خانوادة ۷12۱۷۵0666
. در قاط کرمیر ابران مانئد
بنادر جنوب » صیستّان » بلوچسنان , قسمتی از فاری» خوزستان
و کرمان کاشت‌آن‌را میتوان معمول داشت. ره : فرهنک ووستایی
ص۷۹۶ -۳۲۲ وگل کلاب۳-۲۰۲.یتجاب
پنجاب. بر وزن کنجاب » ولابتی
است از ندوستان. که لاهود و توابع آن
باشد ٩‏ . 2
دوچت انگشت ه معروف است- و نام
----- nearest page tags -----
```


## [2026-09-07T20:38:23.315Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m5 \"pdf page\" BQT_v1_pages.txt; echo \"---\"; head -3 BQT_v1_pages.txt; echo \"--- count ff ---\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds total', t.count(chr(12)))\nlines=t.split('\\n')\nprint('ff before 26391:', '\\n'.join(lines[:26391]).count(chr(12)))\n\"",
 "description": "Check BQT page tag format"
}
```


### [2026-09-07T20:38:24.648Z] TOOL RESULT

```
---
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
--- count ff ---
formfeeds total 776
ff before 26391: 645
```


## [2026-09-07T20:38:29.142Z] TOOL CALL #15: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:419 2>&1 | head -60",
 "description": "Fetch BQT page 419"
}
```


### [2026-09-07T20:38:30.432Z] TOOL RESULT

```
no scan of BQT covers printed page 419 (see 'scans' in refs_online.json)
```


## [2026-09-07T20:38:34.037Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "Full BQT ref info"
}
```


### [2026-09-07T20:38:35.299Z] TOOL RESULT

```
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
```


## [2026-09-07T20:38:46.134Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK pairika ===\" && grep -n -i \"pairika\\|pairikā\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt | head -20; echo \"=== POK per- page 789 region ===\"; grep -n \"789\" POK_02.txt | head -5",
 "description": "grep Pokorny for pairika"
}
```


### [2026-09-07T20:38:46.203Z] TOOL RESULT

```
=== POK pairika ===
POK_02.txt:3361:II.  Schwere  Basis   kens-,   kne-i    att.  xy^v,  3.  Sg.  Präs.  xyj,  später^ y,vrj-^üj  ^schabe,  kratze;   jucke^  Kvrjd-fiög,  xvrjaf^ög,  y,v7]G^6v7j  ,das  Jucken*, TivfjaiQ  ,das  Reiben,  Kratzen;  Jucken^,  ycvfja^a  ,AbschabseF,  i^nqaxriQ  ^Schal messer^,  xy^trrtg  ,Schabeisen^  und  ,Rückgrat^  und  ,BrennesseF ;  att.  Kovlaali ,Dämon  des  Geschlechtstriebes^  (auf  ein  ar.  *knäth-  gleicher  Geltung  will' Güntert  KZ.  45,  200  av.  xnaqd-aiti  ,Nanie  einer  Pairika'  zurückfuhren).
POK_full.txt:45460:*knath- same meaning would go back to Avestan xna^&aitr name of a Pairika 'GiJntert 
POK_full.txt:64739:Material: Avestan pairika^ damonische Buhlerin ', mp. parJk, np. yOa/7'Peri' (Iran. *panka); 
=== POK per- page 789 region ===
5048:WP.  II  422,  WH.  351  ff.,  779  f.,  789  f.
5144:WP.  II  389 ff.,  WH.  I  789,  801,  802,  807  f.,  Trautmann  148,  162,  269,  270. anders  über  3.  und  4.  lei-  EM^  553  f.
```


## [2026-09-07T20:38:47.372Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN peri/Pallas/palladium ===\" && grep -n -i \"^peri,\\|peri,  n\\|Pallas\\|palladium\\|pallad\" KLN_1966.txt | head -20; echo \"=== SKT peri ===\"; grep -n -i \"^PERI\\|PERI,\" SKT.txt | head -10",
 "description": "grep KLN and SKT for peri/Pallas"
}
```


### [2026-09-07T20:38:47.458Z] TOOL RESULT

```
=== KLN peri/Pallas/palladium ===
1778:aegis,  egis,  n.,  1)  shield  used  by  Zeus,  later  by Pallas  Athene  (Greek  mythol.) ;  2)  used  figura¬ tively  in  the  sense  of  protection.  —  L.  aegis,  fr. Gk.  <xlyk,  ‘goatskin;  the  skin  shield  of  Zeus’, fr.  all,  gen.  odyo;,  ‘goat’;  see  aego-.  For  this etymology,  suggested  already  by  Herodotus,  see Frisk,  GEW.,  I,  p.  32  s.v.  xtyi;.  Cp.  Aegeus. Cp.  also  Giles.
3731:astatine,  n.,name  of  a  radioactive  element  (chem.) —  Formed  with  chem.  suff.  -ine,  fr.  Gk. aa-ra-rop,  ‘unstable’.  See  prec.  word, asteism,  n.,  genteel  irony.  —  Gk.  &rszeiay.6q, ‘wit,  witticism’,  fr.  aazeloq,  ‘of  the  town’,  fr. Slot j,  ‘town,  city’,  esp.  ‘the  city  of  Athens’,  fr. orig.  faaTu  [cp.  Arcadian  fa aaxuox01  (gen-  of FaacT'V/oc),  ‘protecting  the  city  (of  Athens)', epithet  of  Pallas  Athene],  which  is  cogn.  with OI.  vdstu,  ‘dwelling  place’,  vastu,  vastu,  ‘seat, place,  thing’,  Toch.  A  waft,  ‘house’,  fr.  I.-E. base  *wes-,  ‘to  dwell’.  See  was  and  cp.  words there  referred  to.  Cp.  also  the  first  element  in Astyanax.  For  the  ending  see  suff.  -ism.
3885:attacus,  n.,  a  kind  of  edible  locust.  —  Late  L. (Vulg.,  Lev.  1 1 :22),  fr.  Gk.  otTzocxbq,  mentioned by  Philo  (cp.  dcTTdbtt]!;,  Sept.,  Lev.  11:22). attagen,  n.,  the  Pallas’s  sand  grouse.  —  L.,  name of  a  kind  of  bird,  possibly  the  francolin,  fr.  Gk. arTxyYjv  (also  a-Traya?,  array?,;) ;  of  uncertain, possibly  imitative,  origin, attain,  tr.  and  intr.  v.  —  ME.  atteinen,  attainen, from  the  stem  of  OF.  ataindre ,  ateindre  (F.  at- teindre),  fr.  VL.  *attangere,  corresponding  to L.  attingere,  ‘to  touch,  to  arrive  at’,  fr.  ad-  and tangere,  ‘to  touch*.  See  tangent  and  cp.  attain¬ der,  attaint,  attinge.
26921:paedobaptism,  n.  —  See  pedobaptism. paedology,  n.,  child  study.  —  See  1st  pedology. Paelignian,  n.,  the  language  of  the  Paeligni ,  a people  of  Central  Italy.  —  Formed  with  suff. -an  fr.  L.  Paeligni,  ‘the  Paeligni’,  a  name  prob. rel.  to  paelex,  ‘concubine’,  and  cogn.  with  Gk. ttoXXSS,  ‘boy;  girl’,  TraXXct yet),  ttxkkoadq,  ‘con¬ cubine’,  ntxXk&z,  ‘virgin,  maiden’;  see  Pallas. Accordingly,  Paeligni  orig.  must  have  meant ‘the  sons  of  unmarried  girls’.  See  F.  Altheim, Geschichte  der  lateinischen  Sprache  und  Litera- tur,  pp.  56-58.
27006:palikar,  n.,  a  follower  of  a  Greek  or  Albanian military  chief.  —  ModGk.  TtaXixapi,  ‘boy’, dimin.  of  Gk.  7raXXa£,  gen.  7raXXaxop,  ‘youth’, which  is  rel.  to  mxXXaxf],  TtaXXaxu;,  ‘concu¬ bine’,  and  to  IIxXXxc,  gen.  -aSoq,  epithet  of Athene.  See  Pallas.
27022:Derivatives :  pall ,  tr.  v.,palli-al,  adj ,,pall-ed,  adj. pall,  intr.  v.,  to  become  insipid.  —  ME.  pallen, prob.  aphetic  for  apallen,  ‘to  appall’.  See  appall. Palladian,  adj.,  in  the  style  of  the  Italian  archi¬ tect  Andrea  Palladio  (1518-80).  —  For  the  end¬ ing  see  suff.  -an.
27023:palladium,  n.,  an  image  of  Pallas  Athene  on  the custody  of  which  depended  the  safety  of  the city  of  Troy.  —  L.,  fr.  Gk.  xaXXaSiov,  ‘statue of  Pallas',  dimin.  formed  fr.  IlaXXdti;,  gen. UaX/.iSo;.  a  surname  of  the  goddess  Athene. See  Pallas.
27024:palladium,  n.,  name  of  a  metallic  element.  — ModL.,  coined  by  its  discoverer  the  English chemist  William  Hyde  Wollaston  (1766-1828) in  1 803  fr.  Pallas,  name  of  an  asteroid  discover¬ ed  by  the  German  physician  and  astronomer Heinrich  Wilhelm  Matthaus  Olbers  (1758-1840) in  1802,  and  called  after  the  goddess  Pallas Athene.  See  next  word  and  2nd  -ium  and  cp. prec.  word.
27025:Derivatives:  pallad-ize,  tr.  v.,  pallad-ous,  adj. Pallas,  n.,  a  surname  of  the  Greek  goddess  Ath¬ ene  (Greek  mythol.) — L.  Pallas,  gen.  Palladis,  fr. Gk.  TlaXXdc,  gen.  IlaXXdSo;,  lit.  ‘maiden’ (whence  7taXXct8iov,  ‘statue  of  Pallas’),  which  is rel.  to  rraXXoocT),  nocXXocxfi;,  ‘concubine’.  Gk.
27026:xdXXaJ,  gen.  xaXXaxoi;,  ‘youth,  girl’,  is prob.  a  back  formation  fr.  xaXXooa)  or  7taX- Xaxt? .  (L.  paelex,  ‘concubine  of  a  married  man’, is  perh.  a  loan  word  fr.  Gk.  *naTka£,  a  hypo¬ thetic  secondary  form  of  xdXXaf;. )  Cp.  Avestic pairika,  ‘beautiful  women  seducing  pious  men’ (whence  Middle  Pers.  parik,  ModPers.  pari, ‘fairy’).  Cp.  also  Heb.  pileghesh,  Aram,  pilaqta, ‘concubine’,  and  Arab.  Bilqts,  name  of  the  queen of  Sheba.  All  these  words  are  certainly  related, but  it  is  difficult  to  establish  the  degree  of  their relationship  to  one  another.  The  above  cited I.-E.  words  are  possibly  Sem.  loan  words.  See Gesenius-Buhl,  HWAT.,  p.  642,  and  Ludwig Koehler,  Lexicon  in  Veteris  Testamenti  Libros, p.  761.  Cp.  palladium,  palikar,  Paelignian,  peri, pallasite,  n.,  a  meteorite  (geol.)  —  Named  after the  German  naturalist  and  traveler  Peter  Simon Pallas  (1741-1811),  who  brought  it  to  St.  Peters¬ burg.  For  the  ending  see  subst.  suff.  -ite. pallesthesia,  n.,  sensitiveness  to  vibration  (psy¬ cho!.)  —  ModL.,  compounded  of  Gk.  mxXXctv, to  wield,  brandish,  swing,  quiver’,  and  a!a- Oavsa-Bm,  ‘to  perceive’.  The  first  element  is  rel.  to n6Xor,  ‘lot  cast  from  a  shaken  helmet’,  TraXxAg, ‘brandished',  and  in  gradational  relationship  to TrEXcpl^Etv,  ‘to  shake,  cause  to  tremble',  and  to ttoXsu.o;,  ‘war’;  see  polemic.  For  the  second  ele¬ ment  see  esthesia.
27097:Panama  hat,  a  hat  made  from  the  leaves  of  the screw  pine.  —  A  misnomer,  for  ‘Panama’  hats were  first  made  in  Ecuador,  South  America. The  association  with  Panama  is  due  to  the  cir¬ cumstances  that  orig.  the  city  of  Panama  was the  distributing  center  for  such  hats. Panathenaea,  n.  pi.,  an  ancient  Athenian  festival. — -  L.,  fr.  Gk.  Ila vxfFfjva'.x,  shortened  fr.  Ilav- atHjvoaa  ispa,  prop,  festivities  in  honor  of  the goddess  Pallas  Athena,  fr.  7t:xv-  (see  pan-)  and ’A (Wpo;,  ‘Athena’.  See  Athena.
28143:peri,  n.,  an  imaginary  sprite,  a  fairy.  —  Pers.  pari, ‘angel,  fairy,  genius’.  See  Pallas, peri-,  pref.  meaning  ‘around,  about,  enclosing'. —  Gk.  rapt,  prep,  and  adv.,  ‘around,  about,  be¬ yond’,  cogn.  with  OI.  pari,  ‘around,  about, through’,  L.  per,  ‘through’.  See  per  and  cp. Perea.
=== SKT peri ===
6948:first.  (E.)     A.  S.  fynt  (  ^for-tif), correct  supcrl.  of  forr,  with  vowel- of  c  to>.  +  lce],^fy/r;  Dan.  Swcd.^ formor,    more    in    front.     (E.) early;    XVI  cent;    a  folac  formatioi^ soil    M.  E.  forpuJt,    \.  e.    forcmcpst ; below.     Formed  by  adding  -rrto  thel form-  of  A.  S-form-a,  fir^t  really  a form,    precisely  equivalent    to    L. where  -m-  is  an  Aryan  saperi,  auflrax.
7528:perigee,  point  of  the  moon's  orbit nearest  the  earth,  (Gk.)  From  Gk.  w«/m*, about,  beie  '  near  ;'  7^,  earth.
8544:perihelion,  the  point  of  a  planet's orbit  nearest  the  son.  (Gk.)  Gk.  »ff<, round,  near;  /fAioc«  the  sun.
11489:perimeter,  lit.  'the  roeajtnre  all (L.-Gk.)    Uperime/ros.^G)L.9ttipKtt aGk.  vffu,  round  ;  fUrpair,  a  nteafOre.
13760:PERIPHERY.
13768:Pericardium,  the  sac  surrounding  the hc.*rt.  (L.  —  Ck.)  h.  /cru-arUium.  —  Gk. wtpueAfiiioif.^GV.  wffti,  around  ;  xapMa,  the heart ;  see  Heart.
13769:Pericarp,  a  seed-vessel  (Gk.)  Ck. wiptKiipwtor,  shell  of  fniit.  •-  Gk.  w*pi,  around ; Kapvoi,  fruit ;  see  Harroat.
13770:Pericranium ;  see  Cranium.
13771:Perigee ;  aee  Geography.
13772:Perihelion ;  »ee  Heliacal.
```


## [2026-09-07T20:38:58.862Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '64715,64760p' POK_full.txt",
 "description": "Read Pokorny context for pairika"
}
```


### [2026-09-07T20:38:58.922Z] TOOL RESULT

```
Alb. {*papa) baba " Daddy ' a Greek loanword. 

Gr. nanna Vok., -ou Gen. ' Daddy ', nanaq naTp6(; unoKopiaija, nannoq "grandfather' 

(out of it Latin pappus), nannic((; " Daddies ', nanna^siv " say daddy '; skyth. Zzijc, 

narraToc;; Latin papa, pappa Ch\\d babble word for 'dish, food; father', pappo -are'eaV; 

Modern High German pappen'eat' (with faltering consonant shift going alongside 

neologism). 

References: WP. II 4, WH. II 249, 250; 

See also: compare appa above S. 52. 

Page(s): 789 

Root / lemma: parika 

Meaning: concubine 

Note: only Iran, and Irish 

Material: Avestan pairika^ damonische Buhlerin ', mp. parJk, np. yOa/7'Peri' (Iran. *panka); 

Middle Irish a{i)rech^ concubine '. 

References: Thurneysen IF. 42, 146 f., WP. II 7. 

Page(s): 789 

Root / lemma: pasto- 

Meaning: solid 

Material: Old \v\6\c pastya-m^ residences'; Armenian /75s/(/-stem) "tight, firm'; Old 

Icelandic fastr. Old English faest. Old Saxon fast. Old High German festi. Modern High 

German fest. 

References: W P. II 7 f. 

Page(s): 789
```


## [2026-09-07T20:39:12.323Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT pairika ===\" && grep -n \"pairika\\|pairikā\\|pairikᾱ\" BRT.txt | head -20",
 "description": "grep Bartholomae for pairika"
}
```


### [2026-09-07T20:39:12.371Z] TOOL RESULT

```
=== BRT pairika ===
4190:•  '].  a-ohvä-,  g.  a-hvä-"  f.  i)  'Antrieb des  Willens,  Schaffensdrang,  Lebenskraft' : pairika  yä  duzyäirya  vlspahe  atiksui  .  . ' faröit pairi'in^misA.)  anhvqm  avaAisiiyät\ (sd.)  Yt.Ä54;  —  ava  m!  3zis  .  .  par5it\ fairrbnpm  (sd.)  arihvqm  ava.d}nnqn  sada- 1 yäfi  (sd.)  V.  i5. 19.  2)  'Antrieb  derl Seele,  innerlicher  — ,  Gemütsdrang,  Ge-j müt'"':  kal..*manS  asti  vT/aymii'tfm{s±) anhvqm  vjmar3zist?m  (sd.)  VL  /.  2 ;  —  ' virtzvatca  (sd.)  mat^  vansvatica  attuAa  j 'W.  62,10;  —  ye  kvam  ankvam  yaozdaite\ humatsilia  .  .  V.  ^.2i^>;  si  *PÜZ.,  lO.  19  I PüZ.;  —  dusx'arpnä  . .  asH5  asti  auuhaya  \ (LS.)  ".  .  ist  unfroh  in  seinem  Gemüt"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"  Yt  /o.  9;  —  fora  vi  räki  am?sä spmtn  yasmmcä  rahmtmcä  firä  mana»hä ..  vaiaahä  ..  syat>^anä  ..  dw^iy«  (IS.) » Y.7/.18.
4954:•vat  ki'ari  utuiti  F.^b;  Yt /( 'vam  uiam  G-5.5;  —  haca  'vatbyS  stjnbyö aoi  sam  Yt5.85,  132  (wo  *°vd'J>yö);  — nihmacii  'vailqm  sfärqm  .  .  y.43.;  — hvan  °va  (IS.)  pai:a  .  .  ma  °va  pa^a  .  . starö  'va  pä^a  yHnti  Yt.  /j.  16;  —  "vaiti/ia niüs  "vaiiiha  pairikaya  pattistätayaSca  .  . Y.16.8;  —  Aaca  *'vaMitt  drujat  V.  J*?, 12;  —  "vai  tmidim  parS.ainli  aauAe "den  Lohn  dort  für  die  künftige  Welt" V.p.44;  —  ym  mä  hau  nä  °z-i
4963:'lam  tiadrtabairam  adam Bh.2.i;  5,  J.iö',  ^.1,  5,  ,,  .  _ pairika  yä  äuzyairya  . .  tiitrys  'vqm  pairi- kam  ädanzayeiti  YLÄS4f.;  —  ^artnS apantmaia  . .  aom  (ASn,)  s^anttB  Aangfur- tayata  mihrS  Yt.19. 35;  —  yai  srum paitiJiiruäi  .  .  SdnnjaySti  aom  srUm  . . V.  p.  1 4.  a)  1!  zugleich  voia.usweisend  auf
4970:aväjanam  |  *startä   akatiy  "vaiy  (als  AP.)  mä  dauitH 'vaiy  .  .  parsä  Bh.4'i4i  —  hauv  karam fräiSaytr  .  .  vivana^  nilwa"  pärs^  mann 6a!'dakaf'    karj'uvatiyä    xsa>''apJVt1    abty Bli.j.9;  —  kärJ"  kyi^  hamth^iy^ manä  naiy  gaubataiy  °vam  /adiy'Eh.2.'},io; martiyä  tyaisaty  ..anuHyä  äka'tS 'vaiy {3\sAF.)../rdÄ^/am  Bh.  2. 13.-,        i)  II  auf ein  Relativum  als  dessen  Korrelat:  tya* parsbartam    ä/Sa*    °^a*    adam  pattpadam akunavam    Bh.  t.  14;   —   tyJ'iam    adam aiakam  "vJ^  akunav^tä  D.d.  4 ;  3,  Bh.  l.  7, 4.16,    17,  X.r.  3,  2.3;  —  Uta   ty<^maiy pi^''a^  iatiam  -valciy  (ASn.)  t^urJ'mazdtl patuv    X.7.4;  J.3;    —   kyci'    aparam  .  . Patiparsatiy  °vaky3  . .  Bh.  4-  8;  —  tyaisaiy fi-atamä  anuiiyä  ähc^til  'vaiy  (als  AP.). . frahcTJam  Bh.  3. 1 3 ;  —  tyaiy  panevä  xsäya- hiyä  . .  'vaisäm  naiy  astiy  kartam . .  Bh.  4- 9.11       3)  auf  einen  Satz(inhalt) :  y3  nanm kasyatfke  (sd.)  satthii  da^tti  vfavi  'i'Ot paraiti  (sÄ)  V. /j.  2;  —  ya^a  nSii  .  . kar>tS. .  avasySt  vismteisd.)  °val .  ./rava- lays  Yty.72f.         a)  in  Verbindung  mit ta-  'hie  ille':  ya'isa  azim  häätyene  pu'^rgm daliai  ahmäi  tat  "vat  syapt?m  artdvi.. Ytj.i8f.;(j.S,J5.4,äi,  Vyt.45.        2)vor. ausweisend;  1)  auf  direkte  Rede,  sub- stantivisch: tamatfkil . .  °vat  stuyi:  nSit., xäa  Y.  J2. 3 ;  —  °vat  manawka  maiiiimna : nqm  stavap  Yt5.7;  123,  y.49,  '9- 50;   —  *viövä    'vai   hava    xra'hwa: ml  hiu  nä  .  .  P.  21.         2)  auf  eine erläuternde  oder  ergänzende  nominale  Bei- fügung, a)  adjektivisch,  auch  im  Sinn  unsres Artikels  (des  schwachtonigen 'der'): /a^i- kayäi  yil  aom  puiinm   baraiti  anyahmai arsanai  varsl»m  Yt.  17.58;  —  aat .  .  aom miryjim  /rayrarayati  .  .  parSJars  nqma \.i8.2y,  —  'vä  /ba^sä  .  .  daevaniim  mal- yänqmca  ". .  die  Anfeindungen  der  D.  und Menschen"  Yt. /.  10;  — yasi  tat  paiti  'vä gaiiiä  tayus  .  .  para.baraiti  dasa  ".  ,  was jenes,  das  Anwesen  anlangt.."  V. y.  10; II.         o)    mit   relativischem   Anschluss: *'vau  (NSf.)  pairika  yS   dulyäirya  Yt  8. 54;  —  'vqm  kikrpmt  . ,  yqm  sämake  Yt. y.6i  ;   62,    Y.2O.2,    y.19.14;    —  /la^a *'vadhat  vlsat  yat  tnäsdayamöit  V.  '9- 1 2 ; —  haca  "vaahät  tamia^  yat  datvö.Jatayh V.ig.20\    —    'va   (APn.)  "baEiaza  ..  ya kumäydte  Vr.  9.  3.  b)  substantivisch:
6962:i)  die  Richtung  auf  den  Sprechenden  zu angebend  'her,  heran,  herzu',  nur  in  äca paraca  'her  und  fort'  sva.  'hin  und  her, hin  und  zurück'*':  'hrixsaparim  hahräkgm (sd.)  *xh'ai  xsa/nd  aca  paraia  N.4;  — pairika  ,  .  3ca  paraca  dvaraiH  YtÄ  54; —  v?r>^raynpm  ..  yö ..  äca  paraca  p}r?- saite  Yt.14.4-j.  ")  anschliessend  'dazu, dazu  auch,  und  auch':  a?s^  zi  vnxs  . . */ramrva»ö  a  vacO  afiunS  vairyö  fraoxtd .  .  spanvanti  H. /.4;  —  hä  hama  pairi- säiU  frapaya  (sd.)  daühus  ä  upaosatfh- väsca  Yt ig.\\  —  yS  H  axtÜ  akmäi  yJm axtsysi  (sd.)  dstihg  ^.36.  i ;  —  'kwSi  as *ärmaitis  ^w!  ä  gStt^  tasä  (sd.)  as  Y.31. 9.  a)  wiederholt  'et  ,  .  et',  nach- gestellt: akunm  mazdqm  amruyi  (sd.) nmänake  nmänS.patsis  ratüm  ä  viss  Tlspa- tsis  ratüm  ä'  .  .  daiähupatOts  ratüm  3 Y.  lg.  I.  a)  in  Verbindung  mit  (vor-
7222:\-,  g-",  P-'*.  ä,  j.  »flä),  j.,  g.  a"4>  I)  Adv. )  die  Richtung  auf  den  Sprechenden  zu ngebend  'her,  heran,  herzu',  nur  in  tua paraca  'her  und  fort'  sva.  'hin  und  her, hin  und  zurück''':  %rixsapar3m  hairähm (sd.)  *xsfas  xsafnö  äca  paraiä  N.4;  — pairika  .  .  Sca  paraca  dvaraiti  Yt.  Ä54;
7776:•  j.  """Sifra-'*  m.  'pathicus'"*:  pailif/aiJe arjanqm^a  -ranqm .  .pairikannm  Yt.  13. 1 04.
9128:kaTucS  vlltaspö  Y.^j.a;  —  iava  vistiispö Ytj.  io8  usw.5>;  —  kavaitn  kaviltim  Yt IQ-Ti  usw.»;  —  iavöii  aipivai^A)us  \t. Ij.i3^  nsv/ß;  —  kai'aSm  usaöaium  Vt. 1(^-71  usw.**;  —  kti7-a  usa  VLJ.4S  usw.; —  iavdis  arsnö  Vt.  13.132  usw.** ;  —  iarms fisinaulß  Vt  JJ.  13z  usw.";  —  kavöis byarsiinS  Vt;_j.  132  usw. 5';  —  iavaim syävarsämm  Vt. /fj.?!  usw.*';  —  kavoU haosravaijhahe  Ny.  5.  5  usw. 5';  —  yat baun  Vispe  *d,iri'i.Aaire  kai'c  (NF.)  Vi.  /(?. 71*'.  2)  jAw,  Name  für  gewisse  Feinde des  Volks  und  Glaubens  der  Masdayasn^T: vTspamitn  tbihatqm  tbuuiii  diUvunam  mai- yänamra  y'f'ircum  pairikannmi'a  sä^rmii iaoyiim  {Gl'.)    'iara/nami'a 'Y.  (/■  tS;    Vt.
9310:pairikanamca   'sihram    kkoyam    '>^«fÜ '■*«""""*'  °^''*'' ^t-*  =»■ Y.p.  i8;'Yl  jj.  135;    —    'pänS   X\..'4.i,\*  J-   kaurvö.duma-   Adj.    'mit   kahlem, FrW.  3.  3.  'Unbehaartem  Schwanz':   aspahe  kihrpa  .  .
9574:•  j.  kar«ma-  Adj.,  mit  star-  m.  'Stern-  y-6"i  136;  -  nairyain  kam.varAtJm  .. schnuppe"':  pairika  .  .  ya  slürä  -mJ  ^5  a/ffw^aira/ "/^w  YL  75.39;  — /«iW^am (NP.)  ^/tf«ft'  on/fl^j  a^w  asmanmca  "die  .J"?"'  *^q'iaili  (sd.)  upanhacat  ■'psm  V. y.  ...  die  als  Sternschnuppen  zwischen  /.9;"«y"«  aojishm  baväht  ya>a  'p^m Erde  und  Himmel  stürzen"  YLiy.S.  (statt  NS.)  Az.j.
10570:•  j.  xnad^aiti-  f.  EN.  einer  Pairika,  die  | K^rjsäspa  verRihite";  pairikqm  yam  *°/;''  | yH  upaahacat  k.>ns3spjttt  V. /.9j — janäi^ pairikam  yam  'ti  V.  ig.  5.
12031:\)  'überwinden,  bewältigen':  tistrxm  , . yS  pairika  taurvayeiti  yd  patrika  titära- yeiti  YtiV.8;  40;  —  afar^nS  ..  taurvayeiti anrfm  mainyOm  Yt.  J<?.  2;  2';  —  ya^a taurvayeni  vTspanam  tbisvatqm  ibaisä  Y. g.  18;  Yt.  /.  6',  14.  4,  13.  142;  —  yai mqm  nalHS  taurvayät  Yt  /.  6;  JJ.  56;  — yüi)m  taüa  taurvayata  V}r3hr»m  äänunqm Yt/J.  38;  38;  —  tä  (ND.)  Al taurvayaiptn tiagsaXt.lj.'jS;  —  yä  datbisvatö  dvalsä (sd.)  taurvayämäY.sS.S; — ya^a  valm.. vispä  tbaBsii  taurvayama  Yt/0. 34;  — airyamamm  .  .  vtspa  (baisa  taurvayan- ttm  vtspa  ibaisä  titarintftn  G, /.  6;  — ^aiiWSrB  vastära  .  .  taurvayanta  .  . g/aesa\X.$.\y,  —  asTm  ..  taurvayeinttm viipä  tbaesä  Y.  52.  2.  a)  'andringen gegen  -,  angreifen':  yat  titarat{^SPiA.)  '^
12248:*vairya  V.  5.  i  o ;  —  vispaca  avi  'ra  ( APn.)  j  alät  iiyeiti  Yt  Ä  1 8  -  2 1  und  2  8  f. ;  —  -nm *iumata  (sd.)  Y.3.  35;  —  arstayasai  ■  ■ ,  stänm  rasvantim  :^armat3uhant)m  yaza- huxinuta  "ra  (NP.)  Yt.JO.39;  —  'ratihö \maide  .  .  yS  pairika  Htärayäü  ya  starS astays  Yt  10.  II  i.  k^nma  patanH  aniart    tarn    asmarumca
13887:—  'canAö  (\P.)  ..  dri'gvati>\.4<).ii.; —  Ohne   Obj.:    vldvä    vidusl  mraotü    mä avaiähäi  pairikayai  . .  yä  duiystrya  yamXsVidvä  *aipi'^  djbävayat  ".  .  nicht  länger
14945:•  j.  paiti-tar«tayae-/a  Inf.  '(und)  zu  über- winden, zu  bewältigen':  avaiiihä  pairikayii paitistatayaEla  paitisiaptayalta  *tayal^a  Y. 16.8.
15056:•  j.  paiti-scaptayae-Äi  Inf.  '(und)  sich,  j^jg«.  b) 'abweichend,  ungleichartig': zu  stemmen  gegen-,  zu  unterdrücken':  i^^/ ♦»/,?!)  (APf.)  ♦««'ara  ((^«.aübj/ft' w/w- avaitihs pairikayäi paitiHätayalca 'tayaiia\fri!  pars  upa.däta  *ß-ast3rmte  aratufrii pattÜantaya^a  Y.16.8.  | "wenn  er  ungleichartige  Pflanzenstengel ♦>
15093:•  j.  paitt-ätät^e,  -ätätayae-i^  Inf.  '(und) zu  widerstehen,  zu  bestehen',  uzw,  iAxfl'ische Wesen  und  Anfechtungen;  a)  mit  Akk, •/Äf  ajastaca  tlizdi^taca  .  .  xrafstra  Yt. 21. 1.  b)  mit  Gen.:  't}e  .  .  druj5  'tSe . .  iialsiirtis  Yt.  ij.  129;  'o.Si  ^^°i  '3^^ i3S-'38'°,  142,  Y.6S.B,  60.4,  ?'■  '7'' YL(7.4i,  5.12,  y.130,  131,  136',  137'. 138',  Vr.20.  2,  V.  20.3'J,  S.2.i3i  — avaiAAi  pairikayäi  'fayaSca  paitiscapta- yaica  Y.  16.  8.
15121:•  j,  pait]raog«t-tbaeSah'ya-  n.  '(auf  den Urheber)  sich  zurückwendende  (,  ihn  selber tTe£rende)AnfeiDdung,Fetndscbaft':ii&a(^/ii pairikayai  paitiitatayaiSa  .  .  'iahyäica  Y. /tf.8,  Yt.&5i   (wo  'RyäHaY\
15568:•  j.  pairika'vant-  Adj.  'der  von  P.  um- '     hlnweiien. geben  ist,  es  mit  P.  hält*:  yatulca  yiitu-\ maiqm  pairikäsca  •vatam  YL/1.6.  ]•}■  ma  Af  iar^ma  pairUt^nttm />airi.-
15582:i  si'afranqm  . .  daüanqm  . .  *siß-a- nqm  (Tjanqmca  'Aaaqm  Vt  13. 104;  — •kam  yqm  *xnqiaiH  (sd.)  yä  upartha^at ksnsasfim  V.  /.  9;  ig.  5.  a)  von  Tistryt bekämpft**':  aam  da^qm  .  .  tiltnm  . ODaiiihäi  'kayäi  paitistätayaica  .  .  yi duzyäirya  Yt  &  50  f.;  —  'ka  yä  duiyäirya . .  parsit  pairikiWH  (sd.)  aaki'qm  ava.- kisiayai  .  .  tislryO  . .  avqm  'kqm  ädan- tayäti  YL&S4f,;  —  tiärim  .  .  yJ  'ki tat/rvayeiti  yö  *kä  titärayeiti  yä  stärS ktrsmh  (sd)  patanti  antar7  sqm  asma- n»Mca  Yt  8. 8  ">.  A)  sonst  in  Verbin- dung natyätav-  (sd.,  auch  fdSt):  ya^  mqm nalAs  taurvayJl  . .  nSit  yätavS  naiöa  *ka Yt/. 6;  usw.;  —  paiti.ptnm  ..  vlspe yStavö  'käsca  vispa  *janayä  yä  drvaitis  V. 20.  jo;  usw.;  —  paitistälse  yätunqm  °ka- nqmia  Yt  6.  4;  usw.;  —  Aaia  "yäiai  haca *käi  Yt4-3; — yätulcä  ystumalqm  'iäsöi pairikavatqm  Yt  11. 6.
```


## [2026-09-07T20:39:13.908Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD parig ===\" && grep -n \"^parīg\\|^parīg \\|parīg \\|^pambag\\|pambag\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"parīk\\|parik\\|pambak\\|pambag\" NYB_vol2_glossary.txt | head -20",
 "description": "grep MacKenzie and Nyberg"
}
```


### [2026-09-07T20:39:13.975Z] TOOL RESULT

```
=== PHD parig ===
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:1411:cotton pambag; (a.) pambagén.
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD_mackenzie.txt:4002:pambag [pmbk I N panba] cotton.
PHD_mackenzie.txt:6275:contain parwastan.                           cotton pambag; (a.) pambagen.
PHD_mackenzie.txt:8597:paseman                 \~Q)            pambagcn                 \~cU
PHD_mackenzie.txt:8598:pisiz                      u-'UCl>      pambag                      ~Q,)
=== NYB ===
353:another vb.: äsärihed (Antia: āšārihed). Skr. v. pariksiyate with the explanation aksamo bhavati.
2034:hu-āyēzišn [hw'ywešn'] of good endeav- our, efficiently furthering the activities of the different classes of the community 5027, according to the gl.: ku kar i aparik veh dānēt kartan ‘that is: it knows how to do the work of the others [not only that of the cattle-breeders] in the best manner’. — To be read with -z-, not -ž-, v. dyoz-.
2957:parik [plyk] sorceress, witch, pl. cas. obl. ~-n 8714.21, 0027, — Av. (863 sq.) patrikd-; Arm. lw. parik; MPrthPrs pryg; Paz. fart (SGV); NP pari.
2958:parikéh the art, practices of sorceresses 4518,
3925:vāparīkānihistan
3938:vaparikanéh [w’plyk’nyh] truth, trust- worthiness 361. — Two ws. of kindred meanings have intersected here: 1. *vā- vara- ‘choice’, ‘adoption of the true faith’, hence ‘conviction, belief, faith’, from Av. (1360 sqq.) ?var-, pres. vävar-, vdur-; 2. *päpara- ‘fulfilment, realization of the conviction or the faith chosen’, hence ‘the realized faith: truth, validity’, from Av. (850) ?par- ‘to fill, to fulfil, to perform (e. g. an act of piety)’, pres. pāfr-, the zero-stage of *päpar-. Original *pa- para- became *väpara- through dissimi- lation, certainly prompted by the in- fluence of *vàvara- whose meaning falls within the same semantic range. In Prth
3943:vaparikanihistan [~-k’nyhstn'] to be made a believer, to be converted to the
3945:vaparikanihistan
3946:true religion 369. — Pass. of *vāparīkānē- natan, v. the preceding w.
5257:pairikä: parik
5269:?par-, pafr-: vaparikančh
6151:w’br, wbryg, w’bryg’n: vāparīkānēh
6156:w'wrydn: vaparikanéh
6553:farī: parīk
6844:vafringani: vāparīkānēh
6872:vāwar: vāparīkānēh
7053:bavar, bavaridan: vaparikanéh
7317:pari: parik
```


## [2026-09-07T20:39:24.822Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD parig ===\" && grep -n \"parīg\\|parig \\[\" PHD.txt PHD_mackenzie.txt | head -10; echo; echo \"=== HRN pari ===\"; grep -n \"parī\\|pari '\\|Peri\\|Fee\" HRN.txt | sed -n '1,30p'",
 "description": "grep PHD parig and Horn pari"
}
```


### [2026-09-07T20:39:24.893Z] TOOL RESULT

```
=== PHD parig ===
PHD.txt:542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
PHD.txt:4325:witch parīg.
PHD_mackenzie.txt:4035: parig [plyk l I M pryg, N pari] witch.

=== HRN pari ===
591:inschriften 2, 238, Ar. Periode 284) findet sich noch bei
1633:^) Vergl. Spiegel, Arische Periode, 103; die Bedeutung *Diener*
2443:ap. "^bumimadana- (Spiegel, Ar. Periode 68).
2478:Spiegel, Ar, Periode 93 vergleicht ai. vasnd-
3382:Spiegel, Ar. Periode, 229.
4175:cihr, cihrak, cihrakömand 'die Merkmale der Periode
5013:und mit Spiegel, Arische Periode, 70 gr. Ooftko
5662:*J SpiegePs Erklärung, Ar. Periode 35, ist lautlich pfanz uu-
7307:aw. kapasti- (Spiegel, zuletzt Ar. Periode 46);
8141:art: Bos Gaurus* (Spiegel, Ar. Periode 55); phlv. gör
```


## [2026-09-07T20:39:30.100Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('total leaves',len(pages))\nfor i in (89,90,91):\n    print('===== leaf',i,'(printed p.',i-21,') =====')\n    print(pages[i][:3000])\nEOF",
 "description": "Print Horn leaf 90"
}
```


### [2026-09-07T20:39:31.324Z] TOOL RESULT

```
total leaves 412
===== leaf 89 (printed p. 68 ) =====
— 68 —
kurd, per e; af}'. parün; oss. vergl. /ar- (274, 1);
bei. paran- 'darüber hinaus gehend' (284).*
304. pervär *Stair^).
aw. *2)airivära?ia-, vergl. pairi.vära- 'Wall*, 'Stall'
(vd. 2, 26 vielleicht, Bartholomae); phlv. {pä-amün-)
parvär,
eS05. perväi^ 'Flug .
aw. pairi (oder para) — V^vciz-, 'herum- bezw. weg-
fliegen , vergl. vazaiti er fliegt*.
306. jyerwerden ernähren, erziehen*, periveris, perwer'tden,
pari -f- y^hhar-; phlv. partoarfan, partvar(i)sn,
307. pervez 'siegreich*.
phlv. aparvej 'siegreich'; wohl zu «r^i, be.ze (No. 253)?
Dann perwez.
308. pervfn 'Plejaden*.
aw. paoiryaeinyas\ca (yt. 8, 12), de Lagarde, Beitr.
z. altb. Lex. 56.
af/. peröne; bei. panvar 'Plejaden (Dam es, 54).
309. perhey(ten 'sich enthalten ; sich hüten', Praes. perliez-etn^
perhez, perheztden^).
aw. palti + [/ra^c- 'verlassen'; phlv. pahre/tan
'sich enthalten', pahrej, pahrej(i)sn.
kurd. pärlstin, dispärise 'ist enthaltsam, enthält sich*.
^) Die persischen Original Wörterbücher geben für hervär (No. 210)
und pervär (die de Lagarde schon geschieden hat) zusammen die
folgenden Formen an : pervär^ perräre, perbär, perbärff perbäl, perbcUe^
fervür^ ferväre (vergl. No. 82S)^ fet'väl^ ferväle . von denen die mit/
beginnenden in dieser Bedeutung gewiss falsch sind. Als Beleg für
die Bedeutung *Stall* dient ein Vers des Xäqänl (Metrum: Munsarih).
röz^ beperrär^ büd^ färbe ez an sude cünin
seb tSn-t himär^ däst läylr ez an sude dun an
^) Die Annahme , dass np. pärsä 'enthaltsam , fromm*, aus
*perhezä (eine solche Form construirt sich Darmesteter, Et. ir. I,
115, NB. ohne Stern) contrahirt sei, ist durchaus unstatthaft. Pärsä
bedeutet überhaupt nicht 'enthaltsam', sondern ursprünglich nur *brav*
(vergl. Sahn. I, 35 Vers 15, 70 Vers 158 u. o.), es bezeichnet gewiss
eigentlich den Pärsen.
===== leaf 90 (printed p. 69 ) =====
— 69 — '
810. perl 'Perl, guter Genius*.
aw. pairlkä' *Hure'; phlv. parlk, arm. LW. parik,
LW. af/. parT.
Nach Bartholomae, BB. 15, 9 ist die SiW. pairikä-
ursprünglich *die Fremde'.
811. perer Vorgestern, perejröz, pere\seb.
Kilo, perc; pere]sdl, pe7^i]söUf per]sew^ pörijsd.
aw. '^parö.ayare; phlv. parer.
kurd. picne (Houtum-Schindler), per; oss. vergl.
fal'iväre 'im vorvorigen Jahre' (274, 2); bei. parerl^
paireri^ n. paln (285).
812. piSmanj pemän^ ptizmän (8ähn. I, 359 Note 2, Calc.)
'bereuend', pesiman,
ap. patü r *wawc/- ; phlv. pasTmän (paz. pasemän) ;
ai. /)ra^^ -i- y/'yw^w- 'erwiedern, entgegenhalten'.
Die Entstehung der Form pesJmän ist ganz unklar ;
piz'' scheint aber sicher auf patis hinzuweisen. Der
Wechsel von z und s findet sich auch sonst dialectisch.
313. pi^fnurden, pezmurden 'erschlaffen, verblühein', pilOTi:!
(Is. 16, 8 u. ö.), plzmertden (Vis und Rämin, S. 47
V
Vers 16), pizmeranlden (Sahn. 85 Vers 433).
ap. paus bezw. aw. aiwis j- \^mar-,
piZ' Scheint wegen jüd.-pers. V\^ ein alter Fehler
für biZ" zu sein, (de Lagarde, Persische Studien,
75), doch findet sich piz- auch in pizöhiden und Ab-
leitungen (No. 314) und in pizmän (No. 312). Jeden-
falls spricht man heute p" (W o 1 1 a s t o n) ; das b
des Gazophylacium's (s. v. infracidirsi) kann
nichts beweisen. — Im Wesentlichen übereinstimmend
ist die Auffassung Nöldeke's, ZDMG. 45, 106
Anm. 3, welche ich erst nachträglich zu Gesicht
bekommen habe.
814. pizohlden 'erforschen, nachfragen*, pizöh, pizöhis^).
Reime z. B. Sahn I, 73 Vers 215, Sälin. I, 140 Vers 198. Die
Wörterbücher wissea nichts mehr voa einem Majhülvooal.
===== leaf 91 (printed p. 70 ) =====
70 ~
phlv. ^patv(i)hltan , vergl. u^v(i)hTtan^ vd. 19 (16),
nv(i)himtan ^).
aw. *paitis + 1 [/'va^d-^ caeday^mi] ai. prati +
i/^ved'.
Np. h aus altem d zwischen Vokalen z. B. auch in
/'ähem aus ^svädämL Die gleiche Behandlung von d
und d (bei letzterem häufige Fälle des Übergangs in h)
zeigt, dass das d zwischen Vokalen im Persischen
ebenfalls spirantisch gesprochen wurde, daher auch
keine Scheidung im Altpersischen durch besondere
Buchstaben ; vergl. auch die allgemein durchgeführte
Spirans d bei AM., also im älteren Neupersisch, über
die Behandlung im Reim siehe Rückert, ZDM6. 8,
285, 286, 10, 263.
315. pes 'hinter, nachher, pesin 'letzter.
Käs. peCj pdc]es, pes.
ap. pasa, 'hinter', pasäva 'nachher ; aw. pasda 'nach',
paskät nachher, hinter , pasne 'hinter' ; phlv. paSj pasTn
'letzter ; ai. pagdd *hinter, nachher , pagcdt Von hinten,
hernach*.
kurd. püstve, pfisl; af/. LW. pas; oss. d. fastäge, t.
fästäg 'hinterer, nachher, zuletzt, am Ende' (280) ; bei.
pas^ Comp, pastara (287).
316. pest 'niedrig, nnoilN (Is. 2, 9; 11, 17).
ai. vergl. üpastiä, upastis 'Untergebener .
Bartholomae (briefliche Mitteilung).
LW. wa/. past, siyn. pist,
317. pistän 'Brust (der Frau)'.
a.w./stana' *Brust'; phlv. p(i)stan (vd. 9 (71)), pistän
(vd. 15 (26) 61.); ai. stdna-; arm. stin (H. No. 259).
LW. af/. pistän.
Vergl. Bartholomae, Indog. Forsch. I, 187 Anm. 2.
318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
1517 Vers 358 2), 1523 Vers 473).
*) So lese ich statt nvedlnltan.
*) An den beiden ersten SteUen vielleicht für puser zu emendireD,
doch kann bei puser wie bei pider die Izäfe fehlen, vergl. Landauer
zu S. 1517 Note 4.
```


## [2026-09-07T20:39:44.743Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"863\\b\" BRT.txt | head -10; echo \"=== leaf of line 15582 ===\"; python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('ff before 15582:', '\\n'.join(lines[:15582]).count(chr(12)))\n\"",
 "description": "Locate Bartholomae pairika column"
}
```


### [2026-09-07T20:39:46.094Z] TOOL RESULT

```
2182:Gt->:  A  Sanskrit  Grammar.     Second  Edition.    Leipzig  18S9. (F^)WiHDisciiHANN  ZSt. :  Zoroastrische  Slndien.    Berlin  1863. WklFh.:  Wochenschrift  für  Uaisischc  Philologie.     Berlin. Wn.:  PATackernacei-
15561:863  pairiuxSatay-  —  *pairLg^vatah-  864
=== leaf of line 15582 ===
ff before 15582: 490
```


## [2026-09-07T20:39:46.352Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(614,624):\n    p=pages[i]\n    if 'پری' in p:\n        print('=== leaf',i,'(printed ~p.',i-222,') ===')\n        print(p[:2500])\nEOF",
 "description": "Find BQT pari entry"
}
```


### [2026-09-07T20:39:47.648Z] TOOL RESULT

```
=== leaf 615 (printed ~p. 393 ) ===
و قری وییم وباگك٩‏ -و سروب رکه را نی زکوین
و بمعنی داشتن (۱) و فرات - و پرداخت -
و پرورش - و پرواز هم آ مده‌است.
رواد ۲ « بر وزن خروار » جالوری
بائد کهآ نرا در جای خوبی بندلد و خوراك لابق
دهند نا فربه شود - وخانهة تابسئانی‌وخاناباد گیر
دار را نیز گویند بهء‌نی اطراف آن ثمام پنجره
داشته باشد - و خانه‌ای را نیز گوبند که‌بربالای
خالاً ددگر ساخته باشند و اطرافآن بازباشد -
و بمعن ی گنجینه هم آمده است - و تختهابی را
کویند که سقف خانه را بدان بپوشند - و بول
و پیشاب بیمار را نیز گوبن که پیش طبیب‌برند.
پر وادهه بروژن انگاره » بمعنی‌پروار
است که خانةٌ تابتانی - و بالاخانه  -‏ وکنجیته.
و تختهای خانه پوشیدن باشد - و بمعنی عودسوز
سو فارورة بیمار- وپرورش افته شدم و فربه نیز
آمده است و بعربی حسمن گویند؟ ۰
رواد ۴ ۰ بر وزن شییاز , ممروف
است که از بربدن باد - و بمعنی نثار هم حست
وآن زری باشد که بر فرامین پادشاعان پاشند -
و بمعئی نور و برتو و روشنابی هم آ منده تا
(۱) خم ۳: داستن .
۱ -شرح این‌فقصه مگر شمح‌برآرد بزبان
پرولزه
ونثیمن ونششگاء مرغان بلشده - و چوهایی‌را
نیز کویند هریك(۱) بىقدار سه وجب طول که
بجهت پوشیدن خانه بر بالای چویهای بزر که
ترديك بهم بچینند و بوربا برویآن پوشندوخاه
بزبر بوربا ریز ند وتزد مین سیر بود لزجاب
ناسوت بشریت بجانب لاهوت حیقت .
پرواده بر وزن خمیازه » توشه
وطعامی را گویند که در سیر وشکر و سفر همراه
بردارند و با از دنبال بیاورند - و درعنه را یز
گونشد ‏ که از بي عروی ریزند و جامبا آتی
برآ نها زنشد -وآتش یکه بیش‌پیشعروی‌آتروزند
و آنثی که فارسیسان در حنگامیکه عووس را
بداهاد سیردندی سفروختندی )۳ ودأمن عروی
و داماد را بهم‌بسته‌بر کردآنآعش‌طوف‌قرمودندی.
و بمعنی عیش و خرمی هم آمده است - و ورق
نقره وطلایی رانیز کوند که ترابجپت شارنموون
رزه ریزه کرده‌باشند چهشخصی کهزر ورق‌س ازد
آنرا پروازه گر میگوبند - و جضی ورق طلا
واقره را گوبن دکه قاشان کار قرماشه و شامد
بری نآ نست که درشیراز غخصی که نکانمیساز.
بعنی ورق طلا و نفره را بر روی پوست حی -
چسباند پرواژه گر میخوانند, اعلم -
‌) چش: باقروختندی..
ورنه پروانه نعارد مسخن هروانی-
«حافط شیرازی۳4۹».
۴ - هرن *بروار» فارسی رابمعنی اصطبل آورده و گوید: دراوستا 02171۷2۲202 ۵ قی :
2 . 21۴1 (باروء طوبله)؛ پهلوی ۳3۲۷27 ودرحاشبه امن‌یت خاقانی شروانی راکه برولررا
بممنی اصطبل آورده » بادکند :
روزیپروادبود فربه ازآن شدچنین شب‌تن بیمار داشت لاغی ازآن شد چنان.
«اسشق ۳۰4 و «ینیری واره» مر کیت از : هنیری دیشو ند ( پیرآمون ) - واره لژمستر ۷۵۲
بنامدادن؛ جمعً بعنی کردا گرد یداه داده وازاطراف درتحت حمایت؛ وىمعنیخانةً تاستانی ویاد گیر
و کنجینه وتخه‌های سقف خاله‌همه ازین رشه است. اما اطلاق‌آن مجانوری که اورا حرجامی مند‌تد
وپروری کنند تافربه شود» من‌باب اطلاق حال باسم محل است. ر: بروار . ۱
۴ اوسئا 08161 ( 0272 ۲۳ ۷22 (در پیرامون پریدن ) قی:
ت۷22۵
=== leaf 620 (printed ~p. 398 ) ===
پرهازه .
و پر؛ آسیا (۱) و دولاب و امثال آن باشد -
وبسمنی‌پهلو نیز بنظر آمدم‌است که‌بعربی جنب
خوانند .
پر هازه - بر وزن دروازه . چوب
پومیده و رکوی سوخنه باشد که بربالای‌سنکه
چشاق گذاشته چشماق (۲) بدان زنند نا آتشل
درآن افتد .
پرهام - بر وزن فرجام » نامی است
پارسی باستانی و معرب آن براهیم است٩‏ .
پر هتن - بفتح الك و سکون خای
غطه دار بر وزن برجستن » بمعنی ادب کردن
عاشف 6 فبکن تالث هم‌آمده است؟ ۲
سهوده را گوبند - و جامه ای که از تاش
۱ - ركگ : ایرهام .
و حرارت آتش رنگه کردانیده شوختن ترديك
رسمه باشد ۰
. فر هون - بروزن مجنون. دایرم وهر
چیز میان‌خالی را گوبشد مانندچنبر وطوقوحالة
ماه و امتاز آن۴ ۰
ثر هیلقن - بر وزن‌انگیختن» بمعنی
ادب کردن باشد.
پر هیز * ه بر وزن پرویز » آست
که بعریی حذر و احتراز میکویند؟ - و ترد
محققیناجتناب از ماسویاه تمودن باشدوبمعنی
تری و بیم و نگاهداشت‌خود ازمضرت. و بمعنی
تفاوت هم بنظر آمده ات
ری ۲ بننع اول وکر ثانی وسکون
نحتانی , همروف است که قیض دیو باشد -
جهل کشبده بگردجان تو پرهون.
تاصرخسرو بلخی. «لفت نامه».
۱ - چهل روز با لشکر اویز بود
۵ پپلوی 0۸۲۳۵6
کهی رزم ر که روی برهیز بود .
فردوسی‌طوسی. «لفت‌نامه».
باهمال خود انسائرا می‌فر سمف. دراومتا بری جنس موّث «حادو» مصوب شده که ازطرف اهریمن
گماشته شده تاییروان مزدیسنا رااز داه راست مثحرف سازد. همجن پربان درزمرة میاه اهردمن
خدزمین وآب وگیاه وستوران و آنش درکارند . همانها بشکل ستار کان دباله دار بانشثر فرعتة.
باران در ستیزماند ناوی راز بارس گی بازدارند وزمین رااز خشکی وبران سازه. ( از بادداتهای
استاد پورداود ورك: بشنها ۱ص ۳۰-۲۹) . درپهلوی ۳2116 ارمنی ۳2۲3» اففانی [۳8۲«اسشق
۳۰( «بی رکه ۱ , خوانساری ۳6۲6 ۶ سالنامةٌ فررهنکه کلپابگان ۷» گیلکی 03 در
ادییات پارسی بنوعی‌از زنان ج نکه نبایت خوبرو باشند» اطلاق‌شده «غیاث‌اللغات» :
پری هفته رخ ودیو در کرشمة حسن بسوخت دیده ژ حیرت که امن چه بو لسجی است.
«حافظ شیر ازی ص 66۵.
=== leaf 621 (printed ~p. 399 ) ===
ومشفف پربر هم هست که پربروز باشد که روز
پیش‌دیروز است؟ سومضارع مخاطی‌پربدن باشد
وبشم اول بمعنی پر ومملو بودن .
پری‌افسای افونگی باشد یمنی
صاحب تسخیر و شخصی که از برای تسخیر جن
افسون خواند .
فر 43۳۵ - بروزن ددیجه , لیف خرعا را
کون وازآن رسمان تابند .
ممدوله بروزن برشان » انونگر و شخ یکه
تخیر جن کرده باشد .
بر بدا بفتح اول بروزن خریدار »
کسی را گویند که جن‌داشته باشد ودختر یکه
اف ون گران چیزها بخوانند و بدو بدمند نا او
برقص دراید . و از ماضی و متقبل چیز ها
بگوید - ودیوانه و مجنون‌را هم کفته‌اند- و جا
ومقام دیورا لیز گوبند .
بر یف حت » بروزن همیگفت: نام دختر
۰سام نریمان عاشق او شد
وزال ازو بهم رسید. ۵
بر ثر 9
دیروز باشد که روز حال روز سیم است .
لِز ه بانحتانی مجهول بر وزن عویز .
فرباد و فتان را کویند ۴ و سیزه که در کنار
جوی و رودخانه و تالاب و جایی‌که آب بیار
باشد برویف و پرویزن را نیز گفته‌اند که ۳۳
پر یز ن «بروزن کشیدن» مخفف پرویزن
ات 15 آردیز باشد ۲ ۴
پر سای باسین بی‌نقطه. مخذف پری
افنا: ات که پر مقوان و وگن و دتقی .مه
بر سود ه با سین بی نقطه بر وزن
پربروزه نام دبری ومعدی بوده در زمان خسرو
چرویز » وبعضی گویند نام مقامیست که شیرین از
دشت آبخوك با نجا رفت.
پر وی بانحتالی‌مجپول بروزن کشیش»
پرشان ۴ - وپرشانکننده را کوبند ۵ - وامر
بدین معنی هم هست معتی پربشان کن و از
هم بپاشی- و پربشان کردن واز هم جدا نمودن‌را
نیز کفته اند - ویمعنی پربشانی و آشفنگی حم
اهلد ات #2
۴ - ازپریزت چنان بلرزدکوه
۷
مانند : خالك برش :
باد برسده نوهم نرسد
که زمين بومپن بلرزاند . علی فرقدی.
« لفت نامه *.
5 - در کلمات من کت
طیران کردن:
آن زاغ را نگه کن چون پرد
شه درصفحً ۳۹۸
=== leaf 622 (printed ~p. 400 ) ===
ح‌ِ ۰ 4 بت .
سازد ٩‏ ,
فر لصو ع اب وزن کئبدن مشتف
برمشان باشد ۴ - و بمعی افشاندن و برشان
کردن هم‌آمده است .
۱ پر یشیك ه مانی پربشیدن است یعنی
پرشان کرد و براکنده ساخت ٩‏ .
بر شین « بر وزن پری دسن .
سمنی بدحاوپریشان کردایدن و بیخود گشتن
بائد ؟ .
پریشیده ۴
ممعنی بر شان شده و برباد داده و عتفرق ساخته
بر وزن پری دنله ۰
باشد .
فری گر فت - کسی راگونن که جن
باو ار شده باشد و او از مفیبات خبر دهد و از
ماضی و مستقبل گوید » و دزد برده بیدا کند»
و هر چیز که در خاطر " بگنرانی و ازو بیرسی
بگوبد. واکی خوابی دیده باشی وآنرا فراموش
کرده باشی ازو بپرسی جواب کوبد و تعبیر
نمابد. وازاحوال غایب لیزخبردهد» وبعربی آورا
کاهن خواشد .
فر لون» بر وزن آفیون » علتی باشد
باخارشی که آن را کسر گویند. و بعریی جرب
خواند ۵ .
ز اخقی ه بفتح اول بر وزن نباختن ,
بععنی گداختن باشد» و بکسر اول هم آعده
است ۰
۱ پز اوه بر وزن کساوه . داشی
و کوره‌ای را کوب که در آن ظروف سفالن
۱ رك: ‏ یشیدن . ۴ - رل : فرنفان.
زچندین ال وچندین زر که برپاشی وپرشی
۴ - اسم مفعول از پریشیدن (ه .م.)
شقل لغت ناهد؟.
وخشت وگچ وآهاث بز ند.
پز ی فقن ۱ « بابای فارسی ونون وتای
فرشت بروزن پهلو شکن, بز بان ژند و بازند(۱)
بممنی دادن باشدکه در مقابل گرفتن است .
و پزپونمی یعنی میدهم ويزپونید یعلی بدهید.
عجب باشد که‌باشد درجهان‌تنگی ودروشی!
فرخی میستانی. «لفتِ نامه».
شه ازسفحهٌ ۳۹۷
«لفت نامه * .
```


## [2026-09-07T20:40:02.447Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\np=pages[490]\ni=p.find('863')\nprint(p[max(0,i-200):i+3000])\nEOF",
 "description": "Print Bartholomae col 863-864"
}
```


### [2026-09-07T20:40:03.887Z] TOOL RESULT

```
leaves 1041
*kä  titärayeiti  yä  stärS ktrsmh  (sd)  patanti  antar7  sqm  asma- n»Mca  Yt  8. 8  ">.  A)  sonst  in  Verbin- dung natyätav-  (sd.,  auch  fdSt):  ya^  mqm nalAs  taurvayJl  . .  nSit  yätavS  naiöa  *ka Yt/. 6;  usw.;  —  paiti.ptnm  ..  vlspe yStavö  'käsca  vispa  *janayä  yä  drvaitis  V. 20.  jo;  usw.;  —  paitistälse  yätunqm  °ka- nqmia  Yt  6.  4;  usw.;  —  Aaia  "yäiai  haca *käi  Yt4-3; — yätulcä  ystumalqm  'iäsöi pairikavatqm  Yt  11. 6.
*)  Das  weibliche  Gegenstück  de*  ^ä/iir-(sd.).
ob,Google
865
"pain.g3r«myat
pain-spatay-
866
•  j.  paoityäi  dahmanqm  "pairLgvrvmyai *pah>yäti  N.  ioj.
Nach  Pü.  zum  V.  grab-;  also  'girimby''!  — Pa.;  fratam  kac  dahmän  ke  apar  glrlt pätixiäh
•  j.  pairi.}a9«n-  Adj.  'herumgehend',  vom Priester,  der  auch  ausserhalb  des  Lands Dienst  tut');  daiAhäurvaisim  Sstäya  Au- mäim  '%n?m  astüya  Vr.j.  3;  —  *daiti- häurvassahe  . .  humäyeke  '^nd  Vyt.  ij;  — ava  baiiaza  ,  .  htimäyehe  °%tiS  Vr.  ^.  2.
Abteil,  aus  *Jiairi.ja%a-  m.,  zum  V.  gam-;  ai. v^.  lamgalhä-  m.  —  Vü. :  pa  apar  raiilniA.  — >)  Im  Gegen*.  lu  daiiikäurvaäa;  %A.  and  Tgl. J*aiii.a.jt^ra-,
•  j.  pairLtaxtay-  f.  'Henimlaufcn':  °tS (LS.)  paurvaHlya  ya%a  apsrinäyus  "im HerunüaufeD  um  die  beiden  Vorausgehen- den (ist  der  Hund)  wie  ein  Kind"  V,  y.
{ atgkvqm    *avaji»r?nqm    sadayati  (sd.)    V, /(?.  19.        M'sMxc:  pas!a  frasaxtahe  (sd.)
mafyehe pasca p''^  d>r>mnH (^^.T^o)  daiva V.  ig.  2  8.
ASn.  aus  *pain%na-  Adj.,  AbleiL  aus  pairi; s.  WH.  Gr.>  S  "4S  E-  !■■  -  Pü-  ("  V.  18): laiiin,  (zu  V.  ig):  «.  bei  dinninti.  —  ')  Lesung nicht  recht  sicher;   "L ^ pairiinfta,   K  l  pturi'
j.  paoiri.fraväxlö  N.  gS:  lies  paaura./r'. •  j.  pairLfrisa-  m.  'Herumfragen':    usta tt  nöii  Sa  (IS.)  »niuxlftn  *p»r3sahi  väHm ''nicht  brauchst  du  nach  dem  wahren  Wort herumzufragen"  Y.5.25".
Zum  V,  fras:  —  Vgl  ai.  fraiam  {prdlipräia jahi;  Bloumfield  5BE.  42.  305),  mp.  äfräs, paiifräs.    —    Vä.:  hal fräi  ptrsakVt.    —    •)  S.
8(?J.
•l  ö  pti;    daiu    i
^  nodeutlichc
•  j.  '^pairi.ta£ahi '>  Inl  'im  Lauf  zu  um- kreisen, zu  umlaufen',  mit  Akk.:  yaval alte  späna  bis  hapta  nmana  f  havqn  \ 'Sobald  die  Hunde  zweimal  sieben  Häuser umlaufen  können"  V.  25. 45.
Zam  V.  tak-,  —  iSynt.  s.  IF.  lO.  193,  —  Pü. : perämen  api  laxlär  hinä.  —  ')  NA.  getrennt.
•  j.pairi.daeza-m.,Plur.'einerings-,rundura gehende,  sich  zusamuienschliessende  Um- wallung, Ummauerung':  aSa^a  hl  aiie  ySi maxäayains  aiAhä  z»mö  'tan  pairi.dal- sayqn  V.^j.  18.
np.  päliz  'Garlen'  [  vgl.  gr.  LW.  iib^!*«o(.  — Pü.  i  pa  pirivtSn  daMimh.
•  j.  pairLdahyav-  Adj,  (auch  mask.)  'der vor  dem  Land  ist':  mi^nm  °yüm  (ASm.) . .  aipiJaRyüm  Yt.  10. 144.
Npfi. :  a  pB  i  Aar  lahr  asl.
•  j.  pairid'wa-  Adj.  'um  was  man  herum- gehen, dem  man  ausweichen,  was  man vermeiden  kann'"
```


## [2026-09-07T20:40:10.760Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[490]\nprint(p[:2600])\nEOF",
 "description": "Print start of BRT leaf 490"
}
```


### [2026-09-07T20:40:12.086Z] TOOL RESULT

```
*kä  titärayeiti  yä  stärS ktrsmh  (sd)  patanti  antar7  sqm  asma- n»Mca  Yt  8. 8  ">.  A)  sonst  in  Verbin- dung natyätav-  (sd.,  auch  fdSt):  ya^  mqm nalAs  taurvayJl  . .  nSit  yätavS  naiöa  *ka Yt/. 6;  usw.;  —  paiti.ptnm  ..  vlspe yStavö  'käsca  vispa  *janayä  yä  drvaitis  V. 20.  jo;  usw.;  —  paitistälse  yätunqm  °ka- nqmia  Yt  6.  4;  usw.;  —  Aaia  "yäiai  haca *käi  Yt4-3; — yätulcä  ystumalqm  'iäsöi pairikavatqm  Yt  11. 6.
*)  Das  weibliche  Gegenstück  de*  ^ä/iir-(sd.).
ob,Google
865
"pain.g3r«myat
pain-spatay-
866
•  j.  paoityäi  dahmanqm  "pairLgvrvmyai *pah>yäti  N.  ioj.
Nach  Pü.  zum  V.  grab-;  also  'girimby''!  — Pa.;  fratam  kac  dahmän  ke  apar  glrlt pätixiäh
•  j.  pairi.}a9«n-  Adj.  'herumgehend',  vom Priester,  der  auch  ausserhalb  des  Lands Dienst  tut');  daiAhäurvaisim  Sstäya  Au- mäim  '%n?m  astüya  Vr.j.  3;  —  *daiti- häurvassahe  . .  humäyeke  '^nd  Vyt.  ij;  — ava  baiiaza  ,  .  htimäyehe  °%tiS  Vr.  ^.  2.
Abteil,  aus  *Jiairi.ja%a-  m.,  zum  V.  gam-;  ai. v^.  lamgalhä-  m.  —  Vü. :  pa  apar  raiilniA.  — >)  Im  Gegen*.  lu  daiiikäurvaäa;  %A.  and  Tgl. J*aiii.a.jt^ra-,
•  j.  pairLtaxtay-  f.  'Henimlaufcn':  °tS (LS.)  paurvaHlya  ya%a  apsrinäyus  "im HerunüaufeD  um  die  beiden  Vorausgehen- den (ist  der  Hund)  wie  ein  Kind"  V,  y.
{ atgkvqm    *avaji»r?nqm    sadayati  (sd.)    V, /(?.  19.        M'sMxc:  pas!a  frasaxtahe  (sd.)
mafyehe pasca p''^  d>r>mnH (^^.T^o)  daiva V.  ig.  2  8.
ASn.  aus  *pain%na-  Adj.,  AbleiL  aus  pairi; s.  WH.  Gr.>  S  "4S  E-  !■■  -  Pü-  ("  V.  18): laiiin,  (zu  V.  ig):  «.  bei  dinninti.  —  ')  Lesung nicht  recht  sicher;   "L ^ pairiinfta,   K  l  pturi'
j.  paoiri.fraväxlö  N.  gS:  lies  paaura./r'. •  j.  pairLfrisa-  m.  'Herumfragen':    usta tt  nöii  Sa  (IS.)  »niuxlftn  *p»r3sahi  väHm ''nicht  brauchst  du  nach  dem  wahren  Wort herumzufragen"  Y.5.25".
Zum  V,  fras:  —  Vgl  ai.  fraiam  {prdlipräia jahi;  Bloumfield  5BE.  42.  305),  mp.  äfräs, paiifräs.    —    Vä.:  hal fräi  ptrsakVt.    —    •)  S.
8(?J.
•l  ö  pti;    daiu    i
^  nodeutlichc
•  j.  '^pairi.ta£ahi '>  Inl  'im  Lauf  zu  um- kreisen, zu  umlaufen',  mit  Akk.:  yaval alte  späna  bis  hapta  nmana  f  havqn  \ 'Sobald  die  Hunde  zweimal  sieben  Häuser umlaufen  können"  V.  25. 45.
Zam  V.  tak-,  —  iSynt.  s.  IF.  lO.  193,  —  Pü. : perämen  api  laxlär  hinä.  —  ')  NA.  getrennt.
•  j.pairi.daeza-m.,Plur.'einerings-,rundura gehende,  sich  zusamuienschliessende  Um- wallung, Ummauerung':  aSa^a  hl  aiie  ySi maxäa
```


## [2026-09-07T20:40:18.088Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[489]\ni=p.find('pairika-')\nif i<0: i=p.find('pairik')\nprint('...',p[max(0,i-1500):i+2500])\nEOF",
 "description": "Print BRT pairika- headword"
}
```


### [2026-09-07T20:40:19.432Z] TOOL RESULT

```
...  s.  PüErL  zn  YL  ^.  lO  (jWrö y«^;  mit  n^de».Iichi^  Erl.  -  0  T  •«*«- 1 "'"  *'^  ^  i'"!^*  J'^"'^^  '^",  *'^' "'«) ^«/,.  -  •)  Es  «hrint  sich  lun  dDc  beson-  '""*J","?^*^-=  *1?«:  °'^-.339-  VgL  noch  "). dere  Art  des  Vortr.g.  der  Cä^Js  m  handeln  .  7.  ',^.^"""  *^'"  ^^  ^"^  "'"°"  8*™«""; oder   tuD    diieii  Vortrag  bei  besonderer  Ge-
KompE.;  Ableit  —  El.?»)  —  ttp.  pari.  — V^:  parii.  Sä.:  räifasl,  (TaeisX)  mahäräifaii; %.  noch  *)  und  Mo.  i.  —  ')  Darauf  geht  die NpüErL  tn  Yt  /.  10:  pari  an  bäiaj  ia  ..  bar ätiHäH  n  ta  tanün  Ingardad,  in  Sü.:  maiäräi- foji  , .  iiSit  patälädifH  bkramiUt.  —  ')  Die Kildänng  BB.  15.  S  wird  durch  mp.  parii, np./ari  nnwahrtcbeinlich,  die  auf  ir.  *parUä-
legenheit.  1
•  j.  yl>  vanAaiii  vanmäs^a  "pairiurus- 1 viätis  N.pz.
Ob  yXLpairiMrtiislüi  S.  vL^rvistay-.  —  Pn. :  öiäit ki  nümmiäid  *iiihtmtVt  i  hrtäi  pizmnknl?)
•  j.  pairika'vant-  Adj.  'der  von  P.  um- '     hlnweiien. geben  ist,  es  mit  P.  hält*:  yatulca  yiitu-\ maiqm  pairikäsca  •vatam  YL/1.6.  ]•}■  ma  Af  iar^ma  pairUt^nttm />airi.-
Pil:  patU  mar/  k  iw;  TgL  tu  yötumaiii:       ,  k^nntli    narS    oahtH     alavanS    V.    t^.
•  j.  pairLkara-  m.  'Umfiirchiuig,  rings henmigehender  Furchstrich ,  -streifen': xia^räi  vairysi  'nm  fairiJiärayöis  (Sp. 449  n»)  V.  17.  6.  |
Zum   V.  ^iar-.    —    np.   TgL  pargär  "Zirkel': Hbm.  PSt.  39.    —    Pü.:  pa  pitc      ~     ■-    ■  -
Sü. ;  flu  an  harsm  pa  apar  niÜriiiüA  (lie» : iirreminiAl)  apar  tirreHfk*!,  erL:  ape  ktSA. — ■)  Die  Stelle  tat  mir  grammatisch  and  inhalt- lich Unverstand  lieh.  Die  Dber^etinngen  bciSp. (».  Komm.  I-  432),  Hauc  Essijs'  334  und  Dst. ZA.  3. 365  sind  mit  dem  Wortlaut  dei  Textes nicht  an  vereinbaren.  —  *)  Pü.  nimmt  also ^W.- iirfntS  aU  aS.  lom  V.  kartt-,  was  ja  an  sich möglich  wäre.
*   y   mä    ht  bansma  pairiMsntsm  (sd.) pairlkgrantiS  ,  .  V.  ig.  ig:  — ?— . g.  pairigae*a-  n.  'Umfassung  des  An-
s.  lu  pairLkari
•  j.  pairUcar&i-  m.  IJmfurchung,  rings henmigehender  Furchstrich,  -streifen':  'Am pairiAarsöit  (sd.)  tUs5  na  V.jg.  at.
Vh.:  pa  pfrämön  iätisHihi   vgL  ZM  puiriJiara-.
•  j.  pairikä-  t  'Zauberin,  Heie'*>:  ptnne
'kam  yä  aüi  ätnm  äpsm  sqm  ..  V,  11, 1  »eseos,  Vorhof;  Vorhalle"':  aii'J  r  ist 9;  —  miir»m  .  .  hamamänm  'kanqm\"><"'^"f^*^f'»'iny7uscä*va^fi3tisvispä  data Yt /o.  26;  — aiai^ha  mal avaitiAä  'iayäi\'P^<'^J><*^'l  it»rys  syaoHana  ..•^ixsmüva/S paitistiiiayaica..\.i6.i>\ — paiHstütSe ofa-  vahmi   maxää  gardbis  itülqm  "und  samt
dem  Denken  alle  Werke  des  guten  Siims und  des  heiligen  Manns, , . :  verbringt  sie in  deine  Vorhalle  auf  das  Gebet  an  euch, o  M-,  samt  den  Uedem  des  Lobs"  Y. 34.  a'>.
Ableit.  la  pairi.\-ga{%ä-;  vgL  No.  1.  —  Pü.: ape    rasim    S   in  i  imäi    Hyäyisn   ckrmatd  .  . 111/in  anjar  garöttnän  itäjrem,  —    ')  Ich  ver- weise für  meine  Fassung  des  Worts  und  der ganien   Stelle   auf  V.  38.  11  (s.  '/J(j>   mit No.  4),  4g.   10  (s.  dam.  mit  No.  3I,  37. 13  (s. äii^ar-*)).   Der  ■heilige  Mann'  ist  ZitmäHi/rit, der  'gute  Sinn'  seine  Anhingenchaft;  f^röbS ifiiqm  ergänzt  mamiifkä  und  i(j^SflM  tu  der bekannten  Drei  bei  t. •  j.  ■•■pairi.gä.-vacah-"  Adj.   'der   seine Worte  ringsum  singt
```


## [2026-09-07T20:40:32.550Z] TOOL CALL #29: Bash

```json
{
 "command": "pdftoppm -f 381 -l 381 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg381 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg381.png",
 "description": "Render PDF page 381"
}
```


### [2026-09-07T20:40:34.347Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75771 Sep  7 16:40 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg381.png
```


## [2026-09-07T20:40:34.580Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON panbeh ===\" && grep -n \"پنبه\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10; echo \"=== MON belqis ===\"; grep -n \"بلقیس\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10",
 "description": "grep Mo'in"
}
```


### [2026-09-07T20:40:34.671Z] TOOL RESULT

```
=== MON panbeh ===
MON_part1.txt:2082:آتش افروزند (مانند پنبه» خار» هیزم)؛ آ نکن 
MON_part1.txt:3710:پنبه پیچیده و گرد کرده برای ریسیدن. 
MON_part1.txt:9741:و رویه که قدری پنبه در میان دارد. گاهی سر 
MON_part1.txt:10231:است پنبه‌ یی به رنگك خاکستری. 
MON_part1.txt:16256:از دهانة چوب پنبهٌ آن عبور می‌کند و منتهی 
MON_part1.txt:20698:رشتن گلوله کرده باشند؛ پنبهٌ زده شده؛ غند» 
MON_part1.txt:21464:ردن پشم ا پنبهه حلاجی کردن. 
MON_part1.txt:23005:بز؛ (۲922 (ع.] (۱.) جامةٌ کتانی یا پنبه‌یی 
MON_part1.txt:23841:ممکن است کوتینی و یا چوب پنبه‌ای شوند. 
MON_part1.txt:25412:پنبه‌ای که بدان شمشیر را حمایل کنند و با بر 
=== MON belqis ===
```


## [2026-09-07T20:40:40.062Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg381.png"
}
```


### [2026-09-07T20:40:40.491Z] TOOL RESULT

```

```


## [2026-09-07T20:40:40.489Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:40:53.606Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-07T20:40:53.612Z] TOOL RESULT

```


```


## [2026-09-07T20:40:56.318Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT pambak/baumwolle/bombast ===\"; grep -n -i \"pambak\\|panba\\|bombast\\|bombazin\\|Baumwolle\" LKT.txt | head -20; echo \"=== LKT peri/pari ===\"; grep -n -i \"^[0-9]*\\. *peri\\|Fee'\\|pairika\" LKT.txt | head -10",
 "description": "grep Lokotsch"
}
```


### [2026-09-07T20:40:56.384Z] TOOL RESULT

```
=== LKT pambak/baumwolle/bombast ===
327:[Kelekian  Kämos  31]  'gestreifte)',  bunter BaumwoUstofi'  [auch  ins  Ar.  überge- gangen, vgl.  SBKAW  Wien  CHI,  189:  'ge- streifter Stoff  aus  Baumwolle  u.  Seide']; hieraus  rum.  alagea  'feiner  gedruckter Kattun'.
520:Npr.  Ein  Urenkel  von  UMAIJJA,  dem Stammvater  der  Umaijjadendynastie, gab  einem  Stadtviertel  Bagdads  den Namen,  also  al-'aifäbija.  In  diesem Viertel  wurden  die  bunten  StolTe  aus Seide  und  Baumwolle  hergestellt,  die nach  dem  Ursprungsorte  einfach  'Attäbl- Stoffe  genannt  wurden.  Hieraus  mit W eglassung  des  ar.  Art.  it.  sp.  pg.  tabi, frz.  tabis  [wozu  das  Vb.  tabiser  'wäs-
571:'Gürtel  od.  Frauenmantel  ohne  Ärmel'; hieraus  pg.  bedeni  'maurischer  Mantel, Regenmantel  aus  Leder,  Spartgras  oder Binsen  [Constancio  Dicc  167  b]  und  siz. piddemia  'Frauenmantel  aus  Leinen  od. Baumwolle'  [in  scherzendem  Tone  od. vei-ächtlichem  Sinne  gebraucht].  [GrS- VociSic  243.
1767:'Art  Stoff'  [Pijn  195b,  vollständig  käin ginggmxg  'gestreiftes  Baumwollenzeug', wohl  ursprünglich  javanesisch  'ver- bleichend, vergänglich'];  hieraus  anglo- ind.  engl,  gingham  'Baumwollstoff  aus gefärbtem  Garn,  gestreift,  kariert  oder in  anderen  Mustern',  familiär  auch 'Sonnenschirm',  ndl.  gingam,  gingang, dtsch.  Bchwed.  dän.  gingang,  dtsch.  Ging- gang, Ginghati ;  frz.  guinyan,  guinganip, sp.  gingen,  pg.  giiingäo,  it.  guingano, ghingano.  —  [Französische  Etymologen führen  den  Namen  auf  die  trz.  Stadt Guingamp  [Dep.  Cötes  du  Nord]  zurück, wo  tatsächlich  Textilindustrie  betrieben wird.]   [JAOS  XVII,  142/144.
1798:737.  Ar.  gubba: 'Baumwollenes  Unterkleid'  [Dozy  V6tem i07ff.\;  hieraus  mit  verschiedenartiger Bedeutungsentwicklung :  it.  giuppa  (alt), giubba  'Jacke,  Wams',  frz.  jupe,  jupon 'Frauenrock,  Unterrock',  demin.  it.  giu- betto,  gitibetta,  augm.  it.  giuppone,  siz. jippuni;  prov.  jubo,  kat.  gipö,  sp.jubön, pg.  jubäo,  gibäo,  rum.  giubca  'langes Oberkleid  der  Bauern',  ^ubea,  sp.  aljuba,
2038:beherrschten.  Aus  dem  tk.  Grundwort entstand:  russ.  Kitai  'China',  kitaika 'BaumwüUstofif,  Nanking  [s.  hier  Nr. 1554]',  poln.  kitaj  'chin.  I3aumwollen- zeug  oder  Glanzleinwand',  kitajha  'Taf- fet',  klruss.  kytaj,  kytajka  'Taflet,  Seiden- zeug', bulg.  kitajka  'Nanking',  serb. Kitaj  'China',  citajka  'baumwollener Stoff';  rum.  chitaiü  'Wollfutter'.  [Hob- son  Jobson  274.   Bern  SlEtWb  505/506.
2534:1067.  Mal.  käpok: 'Baumwollkattun'  [Fijn  171;  aus  dem Jav.] ;  hieraus  frz.  capoc,  der  Baum  capo- qiiier;  dtsch.  Kap>ock  'eine  Art  seiden- artiger Baumwolle'  aus  Ostindien,  die man  nicht  spinnt,  sondern  nach  Art der  Watte  verwendet.    [Devic  DEt  82.
2973:1272.  4r.  kutnn: 'Baumwolle',  vulg.  koton  [selbst  Fremd- wort, wohl  äg.  oder  ind.  ZDMG  L,  633; vgl.  hebr.  kuttöne^,  woraus  gr.  x'^div; hieraus  wahrscheinlich  dtsch.  Kittel]; hieraus  it.  cotone,  sp.  algodön,  pg.  algo- däo,  frz.  coton  'Baumwolle';  pg.  cotäo 'Panzerhemd  mit  großen  Maschen',  prov. alcoto  'Wams,  das  die  Ritter  unter  der Rüstung  trugen  und  das  innen  mit  Kattun gefüttert  war',  afrz.  auqueton,  nfrz.  ho- queton  'gestepptes  Wams  aus  BaumwoU- zeug';  mndl.  acotoen  'dass.',  ndl.  katoen, dtsch.  Kattun,  Katun  'Baumwollstoff, engl,  cotfon;  poln.  katun,  cech.  kartoun. —  Aus  dem  ar.  Adj.  kutiini  'baumwollen' wurde  tk.  ktdny  'Halbzeug  von  Satin und  Baumwolle'  [Kelekian  Kämüs  965  b] ; hieraus  russ.  kutnja  'asiatisches  halb- seidenes Zeug'.  [DE  127.  Eguilaz  162. ML  6910.  Lammens  Rem  264.  Bern SlEtWb  653.    MWiD  94.
3128:1345.  Ar.  inadrasa: 'Hochschule'  [vom  Vb.  darasa  'studieren' mit  Präfix  ma-  des  Ortes],  als  N.  pr. Name  der  Stadt  Madras  an  der  mittleren Ostküste  Vorderindiens.  Hieraus  die Bezeichnung  für  einen  dort  verfertigten hellen  Stoff  mit  seidenen  Quer-  und baumwollenen  Längsfäden:  engl,  (ver- altet) madras,  frz.  madras  'halbseidenes Zeug'.    (Hobson-Jobson  .532/534.
3195:'Stoff  aus  feiner,  weißer  Baumwolle', der  Musseline  ähnlich;  hieraus  engl. muhmil  und  durch  Verkürzung  auf  eine Silbe  engl.  muH,  dtsch.  Mull.
3425:Klassische  Form:  Mausil  [Suffix  »na-des Ortes  und  Vb.  wasala  'vereinigen',  also eigentlich:  'Ort,  wo  etwas  vereinigt  wird', nämlich  Vereinigungsstelle  der  Wege  aus dem  oberen  Mesopotamien  und  dem 'Irak],  früher  Fabrikort  eines  feinen, weißen  baumwollenen  Gewebes  [den  die Araber  heute  säs  nennen,  s.  WETZ- STEIN in  ZUMG  XXII,  161].  Hieraus it  mussolo,  mussolina  'Nesseltuch',  frz. mousseline,  sp.  muselina,  pg.  musselina, murselina,  rum.  muselina ;  dtsch.  Mus- seline, ndl.  mousselien,  engl,  muslin; bulg.  muselina,  serb.  muselin,  öech. muselin,  poln.  muslin.  Heutzutage  gibt es  sowohl  Woll-  wie  Ba  um  wo II- musseline.  [DE  325.  Eguilaz  491.  ML 5700.    Hobson-Jobson  600/601.
3578:N.  pr.,  große  Stadt  am  Unterlauf  des Jang-tse-kjang,  wörtlich  'südlicher  Hof, d.  h.  Hauptstadt  des  Südens  [wie  Peking 'Hauptstadt  des  Nordens'];  nach  dieser Stadt  wurde  ein  baumwollener  Stoff  von bräunlich-gelber  Farbe  mit  meist  ka- riertem Muster  benannt,  da  er  hier  ur- sprünglich ausgeführt  wurde  Engl. 7iankin,narikeen,  disch.  Nanking,  Nankin, ndl.  nanking;  frz.  nankin;  poln.  serb. nankin,  6e  'h.  nankyn,  aber  russ.  nanka 'chines.  Leinwand'.  [Hobson  Jobson  6 16. Hirth  ChinFW  209.
3701:1617.  Pers.  piiiibä: 'Baumwolle',  hieraus  tk.  pembe  'dass., rosafarben';  hieraus  rum.  pambria 'Schafwolle',  jmnbeii  'blaßrot'.  Aus  der pers.  Form  pänbäk  ergaben  sich  tk. pambuk  'Baumwolle'  und  gr.  udiußaE, ■iraiißdKiov  'dass.';  hieraus  rum.  bumbac, buig.  bubak,  serb.  panmk  'Baumwolle', FUSS,  bumaga,  klruss.  buniaha,  bamaha 'Papier'  sowie  mlat.  bambaqium,  it.  bam- bagin  'Baumwolle';  aus  lat.  bombacium wurde  frz.  bombasin,  engl,  bombasine, bombazine;  dtsch.  Bombasin,  russ.  bu- mazeja  'Art  Barchent'.  [Bern  SIEtWb 100/lül.
3730:'Paradies'  ['Wonnegarten'  aus  altpers. pairidaeza  'Umzäunung,  Garten'],  gr. irapdbeiooq,  lat.  paradisum;  hieraus  frz. paradis,  sp.  paraiso,  it.  paradiso,  rum. paradis;  engl,  paradise,  dtsch.  Paradies. Lautgesetzlich  entwickelt  mit  volks- etymologischer Umgestaltung  trz.  parvis 'Vorhof  der  Kirche'.  Nfrz.  paradis  war bei  den  Mysterien bühnen  im  Gegensatz zur  im  Vordergrunde  gelegenen  Hölle ein  Platz  auf  einer  Anhöhe  des  Hinter- grundes, jetzt  der  oberste  Teil  des  Zu- schauerraums auf  der  Galerie  [sonst  frz. poulailler;  vgl.  dtsch.  'Himmelreich, engl,  up  among  the  Gods].  Vgl.  Otto Driesen,  Der  Ursprung  des  Harlekin. Berlin  1904.  (Forschungen  zur  neueren Literaturgeschichte,  herausgegeben  von Muncker.  XXV.)  S.  83, 163iJ.  Fers,  pärgal: 'Leichtes  Linnen  oder  Kleidungsstück daraus';  hieraus  sp.  percal  [Dicc  Gast 1531  c]  'Baumwollstoff',  weiß  oder  bunt, mehr  oder  weniger  fein,  percalina  'ein- farbiges percal',  frz.  percal,  perkal,  per- caline  'weifses  Baumwollenzeug';  dtsch. Perkal.
4219:'Behälter,  bes.  Scheide  für  den  Kris; Art  Rock'  [Pijn  127  ;  vielleicht  aus  sskr. särana];  hieraus  engl,  sarong,  dtsch. Sarong  'ein  langer  Rock,  gewöhnlich von  buntem  Seidenstoff  oder  Baumwolle', das  Hauptbekleidungsstück  der  Malayen und  Javanesen,  ndl.  saroeng.  [Hobson- Jobson  796.
4318:'Matratze ;  langes,  breites,  mit  Baumwolle gefüttertes  Polster,  auf  dem  man  bequem sitzen  kann'  [Kelekian  Kämüs  732b]; hieraus  rum.  saltea  'dass.'.
4790:gandin  'eine  Art  Mull ;  ein  glattes,  feines Baumwollengewebe  dichter  als  Musselin'. [Mfi  9082.  Karabacek,  Über  einige  Be- nennungen mittelalterlicher  Gewebe. I.  Wien  1882.  S.  21/22.
6012:bombazine  1617
=== LKT peri/pari ===
2153:'Wasserkrug',  besonders  für  die  vor- geschriebenen Waschungen  der  Muslimen gebraucht  [aus  dem  Pers.,  doch  kennt man  das  pers.  Grundwort  noch  nicht, vgl.  de  Lagarde,  Gesammelte  Abhand- lungen S.  7];  tk.  ebenso;  hieraus  rum. ibric  'Wasserkrug,  Wasserkanne',  it. bricco  'Zinnkanne  für  Kaffee',  bulg.  serb. ibrik  'Waschkanne,  Krug',  serb.  imbrik, Y)o]n.imb)yk,  imhryczek  'Tee-  oder  Kaffee- kanne', klruss.  imbrycek  'dass.'.  [ML 4253.    Bern  SlEtWb  419.
2278:'Wind,  Lähmung,Rheumatismus'  [Stamm jil,jel  'Wind,  windig'  Vämbery  TktEtWb S.  131,  Nr.  1421];  hieraus  rum.  tele,  ele 'Lähmung,  böse  Fee'.  [Löbel  EITAP 55.
3734:'Guter  Genius'  [Horn  NpEt  S.  69,  Nr.  310 im  Gegensatz  zu  dlw,  s.  hier  Nr.  509; vielleicht  Weiterbildung  von  pers.  pärr 'Flügel'  ebenda  S.  65,  Nr.  293,  also  etwa 'geflügelt'];  hieraus  sp.  peri,  frz.  piri; engl,  peri  [womit  natürlich  trotz  der gleichen  Bedeutung  fairy  <^  frz.  feerie <  lat.  fatum  nichts  zu  tun  hat],  dtsch. Peri  'gute  Fee'.  [Eguilaz  470.  Devic DEt  185/186.
```


## [2026-09-07T20:41:16.631Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT peri fairy ===\" && grep -n -i \"Peri, a fairy\\|Peri,\\|a fairy\" SKT.txt | head -20; echo \"=== SKT bombast ===\"; grep -n -i \"bombast\\|bombasin\\|bombyx\" SKT.txt | head -10",
 "description": "grep Skeat"
}
```


### [2026-09-07T20:41:16.693Z] TOOL RESULT

```
=== SKT peri fairy ===
6948:first.  (E.)     A.  S.  fynt  (  ^for-tif), correct  supcrl.  of  forr,  with  vowel- of  c  to>.  +  lce],^fy/r;  Dan.  Swcd.^ formor,    more    in    front.     (E.) early;    XVI  cent;    a  folac  formatioi^ soil    M.  E.  forpuJt,    \.  e.    forcmcpst ; below.     Formed  by  adding  -rrto  thel form-  of  A.  S-form-a,  fir^t  really  a form,    precisely  equivalent    to    L. where  -m-  is  an  Aryan  saperi,  auflrax.
19312:Temple  (2). Tempt;  see  Tenable. Ten,  (E.)  A,  S.  tin,  also  tyn,  tUn,  ten. +  Da.  tiern^  IceL  //«,  Dan.  /i.  Swcd  tie, Goth,  iaihun,  G,  uMn,  L.  diam,  Gk.  Uitti, Lith.  dhtimtis,  Kusk.  desiatt,  W.  fl!r/,  Irish and  Gael.  t/fiVA,  Peri,  i/a^,  Skt.  dacan. (Aryan  DAKAN.)
23617:b^hau,   I'artce,    pasha    (^lacha,    pashaw, saw),  peri,  »aih  Ca)>  Kpoy,  ibab,  shawl,
=== SKT bombast ===
2015:BOMBAST.
23501:ItaiioH  from  Greek :  arcltipelago,  bai^ lone,  bombast,  catncomb,  gondola,  (copel
```


## [2026-09-07T20:41:19.219Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A8%D9%87",
 "prompt": "Give the full Persian etymology section for پنبه (panba/pambe) 'cotton': Middle Persian form, Proto-Iranian reconstruction, and any note about borrowings into Greek/Armenian/Aramaic/Arabic."
}
```


### [2026-09-07T20:41:23.853Z] TOOL RESULT

```
# Persian Etymology for پنبه (panba/panbe)

Based on the Wiktionary article provided, here is the Persian etymology section:

**Source form:** The word derives from Middle Persian *pmbk'* (pambag), meaning "cotton."

**Etymology statement:** According to the article, the Persian term comes directly "From Middle Persian *pmbk'* (pambag, 'cotton')."

**Limitations of provided content:** The Wiktionary entry does not include:
- Proto-Iranian reconstructions
- Information about borrowings into Greek, Armenian, Aramaic, or Arabic
- Deeper etymological analysis beyond the Middle Persian origin

The article focuses on the descent of this word into descendant languages (Georgian, Kurdish, Ottoman Turkish, Northern Luri, Hindustani, and Zazaki) rather than its earlier prehistory or borrowing patterns into other ancient languages.
```


## [2026-09-07T20:41:30.022Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (403,404,405):\n    p=pages[i]\n    print('=== leaf',i,'(p.',i-20,') ===')\n    print(p[:1200])\nEOF",
 "description": "Print Skeat leaf for p.384"
}
```


### [2026-09-07T20:41:31.259Z] TOOL RESULT

```
leaves 657
=== leaf 403 (p. 383 ) ===
  dust.
Puma,  a  quadruped.  (Peruvian.)  Peruv. puma.
Pumioe  ;  see  Spume.
Pummel,  the  same  as  pommtl\  see Fomade.
Pump  (i),  a  machine  for  raising  water. <F.-Teut.-L.)  U.li..pump€.~Y.pompc. —  G. /ffffi/r,  also  spelt  piumpt,  which  is the  older  and  fuller  form.  Cf.  pror.  G. plumptn,  tu  pump.  p.  The  G.  piumpen  also means  to  plump,  (all  plump,  move  suddenly and  violently,  from  the  plunging  action  of the  piston.  It  is  tbeicfore  aUicd  to  K. PlULmp  ^j),  and  to  Plumb,  and  is  ulti- mately of  Latin  origin.  7.  WV  even  find prov.  Y., plump,  to  pump,  Com./y«M/^.  to pump;  cf.  )^.  plombtr,  tu  sound  with  a plummet ;  and  cf.  Fltmse.  We  also  find Uw.pomp,  Svfcd.  pump,  Dan  pompe.  Rust. pcmpa,  a  pump,  all  borrowed  words;  and Vthc  wcajccnni  forms)  Span,  and  Port. bcm^,  a  pump.
Pump  (a),  a  thin-solcd  shoe;  see  Pomp.
Piuxkplon,  Fumpkiu,  a  kind  of  gourd. (F.  —  L.-»Gk,)  The  old  forms  are /»«• pioH  and  pompcn.  —  F.  pompon,  '  a  pumpion or  melon  ;  *  Cot.  —  L.  pepontm,  ace.  of  /^/o, a  large  melon.  — Gk.  vtaav,  a  kind  of  melon. eaten  quite  ripe.  — Gk.  ircrut-.  m
=== leaf 404 (p. 384 ) ===
  appunctare,  to  repair,  appoint, settle  a  dispote  ;  Ducan^re.  —  L.  ap-  {ad) ; l^w  L.  putiffare,  to  mark  by  a  point,  from Low  L.  punrfu,  a  prick,  fern,  of  punc/uj, pp. ;  sec  point  ( (wlow).    Der.  disappoint.
counterpoint,  the  coniposuu;  of  music hi  putB.  (F.  «  L.)    O.  F.  nminpeimt,  *  a
inui
PUNGENT
ground  or  plain    ^'  
The  lit.  sense  is  /
the/«#/Jor  dots  ^•^ :  •
noltt,  ajid  were  placed  tax  slavo  ote*
against  each  other  in  compositions
or  more  parts.  —  F.  centre,  against ;
a  point:  see  point  (.below).
compunction,  remorse.  (F  — L.)  O compufution.  —  Low  L  ftcc  mnfmtutitm
—  ll  compunctiu,  pp.  of  ccmptif$£i,  to remorse,  pass,  of  compungtrt,  to  pridt L.  £om-  {cum) ;  pungtre,  to  prick.
expunge.  (L.>    L.  ex-pungtrt,  to out.  blot  out    In  MSS.,  crpumr/fm word   is  denoted  by  dotJ  under  it, cxputh't-ioH.
poignant.  (F.  -  L,^  F.  /»tfM stjnj2;tng.  pres.  part,  ot pcindnt,  Co  pndb L.  pungrre,  to  prick.
point.  (F.  -  L.)  M  SipeiMt.  • pot'nt.  poiitct,  a  point,  pTxck.^l*.  pumM orig.  neut.  of  punttus^  pp.  of  pttnga% prick.
pounce  (iV  to  seize  with  th
=== leaf 405 (p. 385 ) ===
olly,  Tw.  Nt..  v.  86,
Purchase .-  see  Capacious.
Pure.  (F.-L.)  F.  pur.  masc,  pttn^ fern.,  pore.  —  L. /wrwj,  pure.  Cf.  Skt,/i/, to  purify.     fVPU.)
expurgate.  (L.)  From  pp.  of  L. txpurgare,  to  purify  thoroughly. —  L.  /.r, thoroughly;  purgart,  to  purge,  purify; see  piiTge  (below).
purge.  (F.  —  L.>  F.  purgtr.  •  L. purpart,  to  purify.  I.,  purpart  ^ pur-igare (Plautu.^).  —  L. /«'•-«/,  pure;  <2^/r/.  to  make. purl^.  (F.  -  L.)  F.  purifier.  -  L. purifirare^  to  make  pure.  —  L.  puri-,  for purus,  pure;  Jaeere^  to  moke.  Dor. pu  rific-at~icn,
piu-itajL  (L.)  A  barlmrons  word,  to Hesipiiate  one  who  aimed  at  great  purity ol  life  :  see  below,
purity.  (F.  -  L.)  M.  K.  purtttt.~V. puretf,  'purity;'  Col.  — L.  ace.  purttaifm, pureness.- L. /i#rw/.  pure.
npurge,  a  plant.  (F.  —  L.)  Named from  its  corroding  (atKl  so  cleansing  away) wart*.  —  O.  F.  spurge,  espurge.  *  O.  F. tsputger,  to  purge  away.  —  L.  ex-purgart, tu  cleanse  away  :  see  purge  ^abovc).
Purl  (i),  to  flow  with  a  raurmuriu sound.  (Scand.)  Swed.  porla.  to  purU bubble  as  a  stream  :  a  frequent,  form  f
```


## [2026-09-07T20:41:41.754Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (23501,23617):\n    print('line',ln,'-> leaf', '\\n'.join(lines[:ln]).count('\\f'))\npages=t.split('\\f')\ni='\\n'.join(lines[:23617]).count('\\f')\nprint('=== leaf',i,'(p.',i-20,') ===')\nprint(pages[i][:2500])\nEOF",
 "description": "Locate Skeat Persian-words list page"
}
```


### [2026-09-07T20:41:43.044Z] TOOL RESULT

```
line 23501 -> leaf 636
line 23617 -> leaf 639
=== leaf 639 (p. 619 ) ===
 Curiously  enough,  there  Is  only  om Iglilh  word  which  can  be  traced  to  Lithuanian,  and  the  mtroductton  of  it  into fUsh  is  due  to  the  fact  that  it  had  been  borrowed  from  that  laagoage  by  the  Danes, '  it  talk.
French  from  Ifalian  from  Latin  from Greek  from  O.  Persian :  rice.
Spanish  from  Latin  from  Greek  from  ^ Persian:  pistachio  (pistacho).
Frc$ick    from     Lai  in    from    Pcrsianil peach  (0.
French  from  Low  Latin  from  Persian  \ zcdoary.
Jtalian  from  f^rsian :  sciaietar  (< icr)  ?.
14.  Words  of  PERSIAN  origin.
flertiani  bang  (t),  barbican?,  bashitw, LT,  caravan,  caravansary',  dervia  (der- bi.  divan,  durbar,  6rman,  ghoul,  bonri, leal,  jasmine  ijetsambe),  Lascar,  mohur,
b^hau,   I'artce,    pasha    (^lacha,    pashaw, saw),  peri,  »aih  Ca)>  Kpoy,  ibab,  shawl,
fftrntrntani  from    Persian-.    lamindar,
Creek  from  Persian :  cinnabar  (dnoper). l^Uinfrom  Greek  from  Persian :  aspara* I,  gypsum,  laudanum,  Magi,  tiar>y f^enek  from  Latin  from  Greek  from rsian:  caper  (2),  jujube,  ma^ic,  myrtle, XwA'ue,  parria,  satsaif,  ''£*''-
Freneh  from  Italian  from  Persian:  car- case (^carcass),  jargonelle,  mommy,  orange« rebeck,  taffeta  (u(^tV^^.
French    from    S;«nuK    from    P«r»a» ]ulep,  (arabanA.
VI.     DISTRIBUTION   OF  WORDS,   ETC.
1
I
Portuguese  from  Persian :  pagoda,  v»- rnnHa  (verandah")?.
French  from  Portuptese  from  Persian  : be?  Oft  r.
French  from  Persian:  check,  chcckci (chequer),  checkers  (chequers),  che^s  ex- chequer, jar  (a),  lemoo,  lime  (3),  ounce (2)  ?,  rook  {%\  scarlet.
Dutch  from  Persian :  gherkin.
15.  Word*  of  SANSKRIT  origin.
Sanskrit',  avatar,  banyan,  brahmin  (brah- man), champak,  pundit,  lajnb,  Sanskrit^ nittec,  Veda.
I^tin  from  Greek  from  Sanskrit :  hemp, pepper,
French  from  iMtn  from  Greek  from Sanskrit;  beryl,  briUioiit,  ginger,  mace (a),  saccharine.
Fretuh  from  Latin  from  Greek  from Persian  from  Satukrit:  naid.
French  from  Spanish  from  Latin  from Greek  from  Persian  from  Sanskrit :  in- digo.
French  from  Latin  from  Persian  from Sanskrit:   musk.
Lorn  Latin  from  Arabic  fr^A borax.
Frettek  from  S/anish  from Persian:    hatard.    tahour    (tal hour?,  tambourine?.     FerkaPi
Spanish  from    TurkUk  frot lilac.
French   from    Arakir  from atmc
French  from  ftaiian  from  Latin  from
fro
catel\  muscadine.
Persian  from   Sans
```


## [2026-09-07T20:41:52.704Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'Peri\\b',p) and ('fairy' in p or 'Pers' in p) and 350<i<420:\n        print('=== leaf',i,'(p.',i-20,') ===')\n        for m in re.finditer(r'Peri\\b',p):\n            print('   ...',p[max(0,m.start()-200):m.start()+250].replace('\\n',' '))\nEOF",
 "description": "Find Skeat Peri entry"
}
```


### [2026-09-07T20:41:54.269Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:41:59.585Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 300<i<430 and re.search(r'[Pp]er[il][,.]',p) and ('fairy' in p.lower() or 'Pers.' in p):\n        hits=[m for m in re.finditer(r'[Pp]er[il][,.]',p)]\n        print('=== leaf',i,'(p.',i-20,')', len(hits))\n        for m in hits[:4]:\n            print('   ...',p[max(0,m.start()-150):m.start()+200].replace('\\n',' '))\nEOF",
 "description": "Search Skeat for peri fairy entry"
}
```


### [2026-09-07T20:42:00.913Z] TOOL RESULT

```
=== leaf 368 (p. 348 ) 1
   ...  where  forurt  is cognate  with  E.  Bore,  q.  v. Perform ;  see  Fomiah. Ferfuxne ;  see  Fume. Perfunctory ;  sec  Funotion. Perhaps :  see  Hap. Perl,  a  fairy.  (Per*.)  Per*. /ar/.  a  fairy. Lit.  '  winged ; '  from  Pere.  yvar,  a  wing. feather.     (V"PAT.) Perl-,  prvfix.  round.  (Gk.)  Gk.  irtfi, arouod.  about.  -^  Skt.  pari,
```


## [2026-09-07T20:42:10.185Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bombast",
 "prompt": "Give the full etymology of bombast, and any related entries shown for bombazine and bombyx: the Medieval Latin, Greek and Persian forms and the semantic development."
}
```


## [2026-09-07T20:42:11.012Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/peri",
 "prompt": "Give the English etymology of \"peri\" (fairy): source Persian word, Middle Persian, Avestan forms, and date of borrowing into English."
}
```


### [2026-09-07T20:42:16.742Z] TOOL RESULT

```
# Etymology of Bombast and Related Terms

## Bombast

**Origins:** The term evolved from "cotton padding" (1570s) through earlier forms:
- **bombace** (1550s): "raw cotton"
- **Old French bombace**: "cotton, cotton wadding"
- **Late Latin bombacem**: corruption of **bombax** ("cotton")
- **Latin bombyx**: "silk" (from Greek)
- **Greek bombyx**: "silk, silkworm"

**Ultimate Source:** "Some oriental word, perhaps related to Iranian *pambak* (modern *panba*) or Armenian *bambok*, perhaps ultimately from a PIE root meaning 'to twist, wind.'"

**Semantic Development:** The meaning extended from "stuffing and padding for clothes or upholstery" to "pompous, empty speech" (1580s).

## Bombazine

Traced through Medieval Latin *bombacinium* and Late Latin *bombycinium* (neuter of *bombycinius*, "silken"), ultimately deriving from the same Greek *bombyx* source. Originally referred to "raw cotton" (1550s), then shifted to describe "twilled or corded dress material woven of silk and wool" (1570s).

## Bombyx

Simply the Latin and Greek term for "the silkworm" (late 14c.), providing the root shared across all three entries.
```


### [2026-09-07T20:42:19.115Z] TOOL RESULT

```
# Etymology of "Peri" (Fairy)

**Source Language:** Persian

**Etymology Chain:**
According to the Wiktionary entry, English "peri" was "Borrowed from Ottoman Turkish _پری_ (peri), from Persian _پری_ (pari)."

**Persian Origins:**
The Persian word derives from Middle Persian _plyk'_ (parīg, "witch").

**Date of Borrowing:**
The page does not specify when the word entered English from Ottoman Turkish, only that it came through that intermediary language.

**Note on Avestan:**
The Wiktionary article does not mention Avestan forms in its etymological discussion of the English term.
```


## [2026-09-07T20:42:25.959Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C",
 "prompt": "Give the Persian etymology of پری (parī) 'fairy': Middle Persian, Old/Proto-Iranian, Avestan forms and any cognates or references cited (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-07T20:42:28.098Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%82%D9%8A%D8%B3",
 "prompt": "Give the Arabic etymology of بلقيس (Bilqīs), the Queen of Sheba: what origin do the sources propose (Greek pallakis? Hebrew pilegesh? South Arabian?) and any cited authorities."
}
```


### [2026-09-07T20:42:29.513Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:42:33.438Z] TOOL RESULT

```
# Persian Etymology of پری (parī) 'Fairy'

Based on the Wiktionary entry, here's the etymological chain:

**Middle Persian**: The term derives from Middle Persian *plyk'* (parīg), meaning "witch."

**Old Persian**: Ultimately traced to Old Persian *\*parikā*.

**Avestan**: Related form *𐬞𐬀𐬌𐬭𐬌𐬐𐬁* (pairikā), defined as "sorceress, witch."

**Cognates cited**:
- Manichaean Middle Persian *𐫛𐫡𐫏𐫃* (pryg)
- Sogdian *pṛʿyk-* ("female demoness")
- Old Armenian *պարիկ* (parik)

**Proto-Indo-European root**: The entry references *\*parīkā*, potentially connected to the root *\*pelē-* ("to fill"), with comparisons to Latin *plēnus* ("full").

**Referenced scholars**: MacKenzie's *Concise Pahlavi Dictionary* and Bartholomae's *Altiranisches Wörterbuch* are cited as authoritative etymological sources.
```


## [2026-09-07T20:42:36.879Z] TOOL CALL #44: WebSearch

```json
{
 "query": "Bilqis etymology Queen of Sheba name Greek pallakis concubine origin"
}
```


## [2026-09-07T20:42:37.607Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/palladium",
 "prompt": "Give the etymology of palladium (both the statue of Pallas and the chemical element), and the etymology of Pallas given in related entries."
}
```


### [2026-09-07T20:42:42.986Z] TOOL RESULT

```
# Etymology of Palladium and Pallas

## Palladium (the statue)
Originating around 1600, this term refers to "a sacred image of Pallas Athene" that supposedly stood in Troy's citadel. The word traces back through Old French *palladion* and Latin *palladium* to Greek *Palladion*, derived from *Palladios* meaning "of Pallas." The city's safety was believed to depend on this artifact.

## Palladium (the chemical element)
Named in 1803 by William Hyde Wollaston after the asteroid Pallas, which had been discovered the previous year by German astronomer Olbers.

## Pallas
According to the related entries, Pallas was a Greek goddess name, another designation for Athene. The name literally means "little maiden" and relates to *pallake* ("concubine"). The asteroid bearing this name was discovered in 1802 by Olbers and Bremen.
```


### [2026-09-07T20:42:44.948Z] TOOL RESULT

```
Web search results for query: "Bilqis etymology Queen of Sheba name Greek pallakis concubine origin"

Links: [{"title":"Queen of Sheba and Her Mighty Throne (Chapter 1) - The Unforgettable Queens of Islam","url":"https://www.cambridge.org/core/books/unforgettable-queens-of-islam/queen-of-sheba-and-her-mighty-throne/D543C25499C20ECE1F05707874DECD45"},{"title":"Meaning of the name Balqis","url":"https://www.wisdomlib.org/names/balqis"},{"title":"Meaning of the name Balkis","url":"https://www.wisdomlib.org/names/balkis"},{"title":"Belkıs - Nişanyan Adlar","url":"https://www.nisanyanadlar.com/isim/Belk%C4%B1s"},{"title":"Balkis, Queen of Sheba (Sorcerer Supreme)","url":"http://www.marvunapp.com/Appendix8/balkis-queen-sheba-sorcerer_supreme.html"},{"title":"Queen of Sheba - World History Edu","url":"https://worldhistoryedu.com/queen-of-sheba/"},{"title":"Balqis","url":"https://en.wikipedia.org/wiki/Balqis"},{"title":"Queen of Sheba","url":"https://en.wikipedia.org/wiki/Queen_of_Sheba"},{"title":"Bilkisu","url":"https://en.wikipedia.org/wiki/Bilkisu"},{"title":"Bilquis بلقيس - Scarlet woman, Whore of Babylon | Ars Magine","url":"https://arsmagine.com/others/bilquis/"}]

Based on the search results, here's what I found regarding the etymology of Bilqis and its connection to the Queen of Sheba:

## Etymology and Origin

The origin and meaning of the name is unclear, though Montgomery Watt suggests that it may be rooted in the Greek term pallakis, and its Hebrew equivalent, pilegesh – Arabic bilqis – meaning "concubine". The name Bilqis/Belkıs appears in Arabic sources starting from the 9th century, and it is generally accepted that this name is derived from Greek pallakís ("concubine").

However, there are alternative theories about the name's origin. Some suggest it is a derivative of the Greek pallakis (meaning concubine or mistress), while others trace it to the Arabic root b-l-q, associated with whiteness or brightness, or suggest it is an Arabicized form of a South Arabian title.

## Historical Context

Muslim commentators like Al-Tabari, Al-Zamakhshari, and Al-Baydawi expand on the story, naming her Bilqis, possibly derived from Greek "pallakis" or Hebrew "pilegesh" (concubine). Notably, the Quran refers to her as "a woman ruling them," without naming her, so the name Bilqis was added by later Islamic scholars rather than appearing in the original religious texts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:42:56.779Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%80%CE%AC%CE%BB%CE%BB%CE%B1%CE%BE",
 "prompt": "Give the Ancient Greek etymology of πάλλαξ (pallax) 'youth, girl' and of related παλλακή/παλλακίς 'concubine': what does Beekes or the cited literature say about its origin (Pre-Greek? Indo-Iranian? Semitic?), and is Avestan pairikā or Persian parī mentioned?"
}
```


## [2026-09-07T20:42:58.712Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%A0%CE%B1%CE%BB%CE%BB%CE%AC%CF%82",
 "prompt": "Give the Ancient Greek etymology of Παλλάς (Pallas), epithet of Athena: proposed origins and whether it is connected to πάλλαξ 'maiden'."
}
```


### [2026-09-07T20:43:03.922Z] TOOL RESULT

```
# Etymology of Παλλάς (Pallas)

According to the Wiktionary entry, Παλλάς is "Likely derived from πάλλω (pállō), meaning 'to brandish'" and was given to Athena as an epithet meaning "she who brandishes" a spear.

The document does not discuss any connection to πάλλαξ ('maiden'), nor does it propose alternative etymological origins. The entry presents only the single derivation from the verb meaning to brandish as the likely source.
```


### [2026-09-07T20:43:04.034Z] TOOL RESULT

```
# Etymology of πάλλαξ (pallax)

Based on the Wiktionary entry provided, the etymology information is limited:

The article states that πάλλαξ is "Probably a back-formation from παλλακή (pallakḗ, 'concubine')."

The sole reference cited is Robert S. P. Beekes' *Etymological Dictionary of Greek* (2010), which notes: "παλλακή (> DER > πάλλαξ)" on page 1147.

**What the source does NOT contain:**

The webpage does not provide further etymological analysis beyond identifying it as a back-formation. There is no discussion in the provided content regarding:
- Pre-Greek origins
- Indo-Iranian connections
- Semitic origins
- References to Avestan *pairikā* or Persian *parī*

To obtain answers about deeper etymological origins and potential connections to Iranian languages, one would need to consult Beekes' full dictionary entry directly, as the Wiktionary article only presents a summary of his conclusions.
```


## [2026-09-07T20:43:16.819Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 parika ===\"; grep -n -i \"parika\\|pairika\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10; echo \"=== WLD band3 index ===\"; grep -n -i \"pairika\\|parika\" WLD_band3.txt | head -10; echo \"=== IEC ===\"; grep -n -i \"parika\\|pairika\" IEC.txt | head -10; echo \"=== AHD watkins ===\"; grep -n -i \"parika\\|pairika\\|pambak\" AHD_watkins1985.txt | head -10",
 "description": "grep WLD, Mann, Watkins"
}
```


### [2026-09-07T20:43:16.916Z] TOOL RESULT

```
=== WLD Bd2 parika ===
472:Av. 'pairika „die Frommen durch Liebeskiinste vom Glauben abspenstig 
486:mit lat. Parca aus "^parika, Ich halte an obiger Zsstellung fest. Mit 
=== WLD band3 index ===
=== IEC ===
=== AHD watkins ===
```


## [2026-09-07T20:43:17.952Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA Baumwolle ===\"; grep -n -i \"Baumwolle\" AFA.txt | head -20; echo \"=== AFM pambak ===\"; grep -n \"قطن\" AFM.txt | head -10",
 "description": "grep Fraenkel and Addi Shir"
}
```


### [2026-09-07T20:43:18.017Z] TOOL RESULT

```
=== AFA Baumwolle ===
1982:r U s »Baumwolle" (bei Gauh. schon mit einem Verse
3194:zur Aufbewahrung Ton Baumwolle" aus jüd. HS^p. [Dies
5261:. A **< (A4däd 19; 170) »Baumwolle** ist gewiss kein echt
=== AFM pambak ===
807:د ( البرس) 2 ܚܚ وهو القطن 
2008:( جورّق) القطن : 0 
2256:١‏ ܚܨܢ( تعر يب ܘ“ ܩ حب القطن 
2314:( ܐ ) ܨ خض وهو ثوب من غ القطن يلس فوق الدرع ܕܚ 4 ܒܨ 
5434:ات ذا القطن 0 فرنكل ( ص 158 التعلية رومسة الاصل 
5435:مننائم ܓ وما الككر باس ععنى 00 ن القطن الابيض فعرب عن اليوثاق
```


## [2026-09-07T20:43:23.577Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '455,500p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \"=== leaf ===\"; python3 -c \"\nt=open('incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('ff before 472:', '\\n'.join(lines[:472]).count(chr(12)))\n\"",
 "description": "Read Walde-Pokorny pairika passage"
}
```


### [2026-09-07T20:43:25.030Z] TOOL RESULT

```
fuolenj ags. gi-folian, ags. felan „fuhlen“ (abg. pahch „Daumen^^, russ. 
pdlec „Pinger‘'^, dial, pdlec „Daumen^^ beruhen aber, da woh.1 ^Daumen"^, 
nicht „ Finger liberhaupt*-^ die eig. Bed. war, eher auf einem '^p(}i)olos „dick^‘, 
8. phel- „schwellen^^). Recht unsichere Verkniipfungen. 

Vgl. Curtius 730, Pick 148, 573, III^ 236, Vf. LEWb.^ 556 {palpo\ 
Franck -van Wijk 753 (voelen). Mladenov IF. 35, 134 will von „betasten, 
fuhlen^^ zu „untersuchen, suchen^^ in np. paltdan „to purify; to see, inquire, 
search*^^, bulg. pdlam ^suche*-^ gelangen(??). — Trotz aisl. falma „Lappen, 
unsicher betasten, zittern, vor Schrecken verdutzt sein*’^ besteht kaum Be- 
ziehung tm pel- usw. (I'ickKZ.19^ 263, Liden BB. 21, 95 Anm.); 

falma ist letzterer Gruppe zuzuteilen. 

palia-q-, pali-q- (junges) „Madchen, auch (gr.) Knabe“ und verwandte 
Formen. 

Av. 'pairika „die Frommen durch Liebeskiinste vom Glauben abspenstig 
machende schone Frauen^^, mp. parlky np. pari „Peri“ (iran. parlka ) ; gr. 
TiaXXaxig^ jial/Mxiq „Beischlaferin, Kebsweib“ (Gdlf. vgl. das 

aus einem mdartl. ’^Tiaika^ entlehnte lat. paelex ds. und die Parallelbildung 
peToa^ aus "^pegiax-)^ ursprgl. ohne schlimmen Nebensinn, vgl. Trd/Aaf, 
(jon.j jidkXr]^ „Knabe, Madchen^^ (die auf naig folgende Altersstufe), Jiak- 
Xdxiov * peigdxiov Hes., HakXdg Beiwort der Athene, auch (nach Strabo) 
von den Griechen im agypt. Theben als sakraler Ausdruck fiir naQ'&hog 
gebraucht, naklddtov eigentlich „Puppchen — weibliches Idol*^ 

Ygl. Vf. IF. 39, 85fiF. m. Lit. Giintert KZ. H. 5, 201 verband iran. 
'^parlka als „Gottinnen der Fruchtbarkeit“ mit ai. parl-nali ,,Fulle, Reich- 
tum-^, parJ-man- „Fulle“ {f'pel- ,4dllen^^), Kalypso 259 f. als„Geburtsgottinnen^ 
mit lat. Parca aus "^parika, Ich halte an obiger Zsstellung fest. Mit 
gr. nibXog ,,Fohlen“, dt. Fohlen hat die Gruppe nichts zu tun (s. u. poti- 
„klein^). 

pas6“S „Yerwandter^^ 

Gr. Jirjogj dor. jrddg „Yerwandter"^, 7iad)Tai‘ ovyyeveTg leit. pari-clda 

(daraus parri-cala) „Morder an nahen Yerwandten^^ Frohde BB. 8, 164. 
Ob in Beziehung zum Lallworte pa{pay. (Andeutung bei Fick I^ 472). 

Langobard. fara ,,Geschlecht''^ (Schrader Sprvgl.^ 579) hat nach Kogel 
ZfdA. 37, 217fF. (anders Henning ebda. 304) a. so daB auszuschlieBen. 

pasto* „fest'^ 
=== leaf ===
ff before 472: 0
```


## [2026-09-07T20:43:42.741Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5255,5270p' AFA.txt; echo \"=== WLD Bd2 page for pallaq ===\"; grep -n \"pallā-q-\\|palia-q-\\|pallaq\" incoming/WLD/WLD_Bd2_pages.txt | head; python3 -c \"\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\npages=t.split(chr(12))\nfor i,p in enumerate(pages[:30]):\n    if 'pairika' in p:\n        print('leaf',i)\n        print(p[:200])\n\"",
 "description": "Read AFA cotton and locate WLD page"
}
```


### [2026-09-07T20:43:44.131Z] TOOL RESULT

```
(durch die doppelte Vocalisatiousmöglicbkeit schon verdäch-
tigt) übernommen aus 'HID l-r^ Low 226. — Ob das145
synonyme hj (Low LI.) aas xißrov entstanden ist? Dies
aus ^n*^?? — .(M*i«5^» Eppich** kann aus dem arara. KDä'lS
\sa^fA Low 222 oder direct aus pers. kara/s Lagarde Ges.
Abb. 61 in*s Arabische gewandert sein.
. A **< (A4däd 19; 170) »Baumwolle** ist gewiss kein echt
arabisches Wort, sondern M^ohl aus ffosst/piumyo^ffiTisw ent-
lehnt. Daraus ist dann iy*i^ erst umgestellt yielleicht mit
Anklingen an ^L«5^. Oiier ist xopviTtov Parthej Vocab.
567 das Original für das arabische und griechische Wort?
^^Ji^ »Birne** ist schon tou den Arabern (Mu^arrab
p. 133) als fremd erkannt; es geht zunächst zurück auf
UAl&fi Low 208 — . »LuJ »Bohne** schon ron den Arabern
(Mu^arrab p. 134) als fi'emd erkannt, ist Entlehnung aus
K*3^^ linrS Low 234, schon an der Form als solche
=== WLD Bd2 page for pallaq ===
443:palia-q-,   pali-q- (junges) „Madchen, auch (gr.) Knabe“ und verwandte
leaf 11
                                              palia-q     pasto-


{^ipaXa „das Zupfen“              acpdco „beruhre^^, FickBB. 28, 102, B^eclitel LeviL 336),
xpakkco „schnelle (die Saite, die  Sehne
```


## [2026-09-07T20:43:56.401Z] TOOL CALL #52: WebSearch

```json
{
 "query": "Syriac Aramaic word for cotton \"bambak\" ܒܡܒܟ Armenian bambak Middle Persian pambag loanword"
}
```


## [2026-09-07T20:43:57.780Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D9%86%D8%A8%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for پنبه exactly, including any bracketed origin tag such as [په.] (Pahlavi), and any Latin-script form given."
}
```


### [2026-09-07T20:44:03.121Z] TOOL RESULT

```
# فرهنگ معین Entry for پنبه

According to Farhang-e Mo'in, the entry reads:

**(پَ بِ ) (اِ. ) گیاهی علفی و یک ساله که از غوزة آن ریسمان و پارچه درست کنند.**

The dictionary identifies it as an annual herbaceous plant whose fibers are used to produce thread and fabric. The entry also includes figurative meanings related to gently persuading someone toward ruin without their awareness.
```


### [2026-09-07T20:44:03.491Z] TOOL RESULT

```
Web search results for query: "Syriac Aramaic word for cotton "bambak" ܒܡܒܟ Armenian bambak Middle Persian pambag loanword"

Links: [{"title":"List of English words of Persian origin - Wikipedia","url":"https://en.wikipedia.org/wiki/Persian_loanwords_in_English"},{"title":"Syriac Language","url":"https://gedsh.bethmardutho.org/Syriac-Language"},{"title":"pmbk' - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/pmbk'"},{"title":"Babak (given name)","url":"https://en.wikipedia.org/wiki/Babak_(given_name)"},{"title":"History of Syriac | Beth Mardutho","url":"https://bethmardutho.org/syriac-history/"},{"title":"Syriac language","url":"https://en.wikipedia.org/wiki/Syriac_language"},{"title":"Middle Persian literature","url":"https://en.wikipedia.org/wiki/Middle_Persian_literature"},{"title":"Ancient Jewish History: Aramaic","url":"https://jewishvirtuallibrary.org/aramaic"},{"title":"Aramaic Loan-words in Middle Persian on JSTOR","url":"https://www.jstor.org/stable/24049218"}]

Based on the search results, I found relevant information about the cotton terminology across these languages:

The word "bambak" appears in Medieval Greek (βαμβάκ), derived from Medieval Latin bambac- and bambax, probably from a Turkish word (now pamuk for cotton) that has Persian origins related to Persian pamba (cotton).

The Middle Persian word "pambag" is documented in etymological sources, and it appears in etymological chains showing relationships to Ancient Greek forms (bámbax, bámbēx, bámbix, pámbax) and Late Latin forms (bombax, bambax, bombix, bambix).

The search results also confirm that Syriac borrowed lexemes from Middle Persian, which would support the connection between the Syriac "bambak" (ܒܡܒܟ) and the Middle Persian "pambag" as a loanword relationship.

The ultimate origin of this word family is unknown, though it appears to represent an ancient term for cotton that traveled across multiple languages and writing systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:44:12.310Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/pmbk%27",
 "prompt": "Give the full Middle Persian entry pmbk' (pambag) 'cotton': etymology, and the complete list of descendants/borrowings — Ancient/Byzantine Greek forms, Latin forms, Armenian, Aramaic/Syriac, Arabic, Turkish, and New Persian."
}
```


### [2026-09-07T20:44:19.837Z] TOOL RESULT

```
# Middle Persian pmbk' (pambag) – Cotton

## Etymology

The term relates to "Ancient Greek *bómbux* (silk-worm)" and "Khotanese *mamṃa-* (cotton (?))," ultimately deriving from "*bamba-*" with unknown ultimate origins.

## Descendants & Borrowings

**Greek Forms:**
- Ancient Greek: *bámbax, bámbēx, bámbix, pámbax*

**Latin:**
- Late Latin: *bombax, bambax, bombix, bambix, *bombacum*

**Romance Languages:**
- Italian: Bambaci, Bombaci
- Sicilian: Bammaci, Bummaci
- Romanian/Aromanian: *bumbac*
- Romansh: *bambesch*

**Persian & Related:**
- Persian: *panbe*
- Gilaki: *panba*
- Gurani: *pama*

**Turkish & Caucasian:**
- Ottoman Turkish: *penbe, pamuk*
- Turkish: *pamuk, pembe*
- Azerbaijani: *pambıq*
- Albanian: *pambuk*

**Slavic & Other European:**
- Bulgarian: *pamúk*
- Serbo-Croatian: *pamuk*
- Hungarian: *pamut*

**Armenian:**
- Old/Middle/Modern Armenian: *bambak*

**Aramaic:**
- Classical Syriac: *palbaḡ*

**Arabic:**
- *bamba, bambaj*

**Caucasian & Central Asian:**
- Ossetian: *bæmbæg, bæmpæg*
- Ingush: *boambi*
- Bashkir/Kazakh/Kyrgyz/Turkmen/Uzbek variants
```


## [2026-09-07T20:44:33.128Z] TOOL CALL #55: Bash

```json
{
 "command": "sed -n '1,160p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T20:44:33.175Z] TOOL RESULT

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


## [2026-09-07T20:44:48.730Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN panba/pumba ===\"; grep -n -i \"panba\\|pumba\\|pamba\\|Baumwolle\" HRN.txt | head -10; echo \"=== HUB ===\"; grep -n -i \"panba\\|pambak\\|Baumwolle\\|pari '\\|pairika\" HUB.txt | head -10; echo \"=== NYB pambak ===\"; grep -n -i \"pambak\\|pambag\\|panba\" NYB_vol2_glossary.txt NYB_vol1.txt | head -5",
 "description": "grep Horn/Hübschmann/Nyberg for cotton"
}
```


### [2026-09-07T20:44:48.803Z] TOOL RESULT

```
=== HRN panba/pumba ===
3873:kurd. yüma 'grobes baumwollenes Zeug (H,-Sch.);
=== HUB ===
1320:pargar 'Halskette' zu zd. pairikara- vd. 17, 6 = Turche'
1365:310. Zd. pairika- schlechtweg durch *Hure' zu iibersetzen,
1366:ist falsch. Die Pairika s sind Teufelinnen, die die
1370:np. pari 'Fee, EngeF.
9122:sitanba; bambak 'Baumwolle' = np. panba, paz. panba Min.
9123:Gl. 154, phi. pambak Bdh. 65, 10; gmbef 'Kuppel* = np.
=== NYB pambak ===
```


## [2026-09-07T20:44:51.329Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW bombyx ===\"; grep -n -i \"bombyx\\|bombax\" LEW_1910.txt LAT.txt | head -10; echo \"=== LEW paelex ===\"; grep -n -i \"paelex\\|paelic\" LEW_1910.txt LAT.txt | head -6; echo \"=== FVQ Bilqis ===\"; grep -n -i \"Bilqis\\|Bilqīs\\|Sheba\\|Saba\" FVQ.txt | head -10",
 "description": "grep Walde-Hofmann, Ernout-Meillet, Jeffery"
}
```


### [2026-09-07T20:44:51.408Z] TOOL RESULT

```
=== LEW bombyx ===
LAT.txt:7465:Ennius) an grec (fc>p,( 3 oc;. M.L. 1199; cf .bombax.
LAT.txt:7469:bombyx, -Icis m .(bonbix, bumbix, bumbicis; bambis ): ver k soie.
LAT.txt:7472:formes romanes remontent k bonbix, bombax , attestA seniement dans la
=== LEW paelex ===
LAT.txt:14315:un intera^diaire etrusque, cf. SSturnus, Saeturnus, et scaena, paelex),
LAT.txt:32818:pellicdtor "qui pellicit ad fraudem", P.F.335,11 (ou bien de paelexf)
LAT.txt:44472:crime (Suet. Calig.36,8; Inscr. ). Derivd hybride de Tiaiyvoov "jeu" .paelex
LAT.txt:44474:paelex ( pel(l)ex \; pelica, Gloss.),-icis f.: pelices nunc quidem
LAT.txt:44481:D^riv£: paelicStus, -us m.: concubinage..
LAT.txt:44482:La graphie la mieux attestee est paelex', pellex est du a un rap-
=== FVQ Bilqis ===
426:Mordtmann und Miiller. Sabaische Denkmdler. Wien, 1883. 
703:Madyan, Saba', and many of the commonest religious terms Shaitan, 
1685:from the inscriptions of the Minaean, Sabaean, Himyaritic, and other 
1721:3 Vide Blau, '* Die Wanclcrung der sabaischon Volkcrstamme," ZDMG, xxii 
4828:entered Arabic from the Sabaean, but we have no inscriptional evidence 
5867:equivalents of Heb. "132?; Akk. sabam; Sab. )I18 4 ; Ar. j\f; 
7363:3 The name ^4* in Sabaean and in the Safaite inscriptions (Ryckmans, Noms 
10113:(Saba 9 ). 
10116:Saba'. 
10124:occurs in the Cuneiform inscriptions as Sub* a and Saba\ 2 in Greek us
```


## [2026-09-07T20:45:00.497Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB 1360-1375 ===\"; sed -n '1360,1375p' HUB.txt; echo \"=== HUB 9115-9128 ===\"; sed -n '9115,9128p' HUB.txt; echo \"=== leaves ===\"; python3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (1365,9122):\n    print(ln,'-> leaf', '\\n'.join(lines[:ln]).count(chr(12)), 'printed p.', '\\n'.join(lines[:ln]).count(chr(12))-10)\n\"",
 "description": "Read Hübschmann passages"
}
```


## [2026-09-07T20:45:01.352Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7460,7478p' LAT.txt; echo \"=== paelex ===\"; sed -n '44472,44492p' LAT.txt",
 "description": "Read Ernout-Meillet bombyx and paelex"
}
```


### [2026-09-07T20:45:01.911Z] TOOL RESULT

```
=== HUB 1360-1375 ===
p. 51, Anm. 16. Von dieser Pehleviform fiihrt kein
Weg zu Fr. Muller' s (WZKM. 6, 185) zd. ^paiti-ra^d-
Verlassen*", dem doch nur np. *pairextan entsprechen
wiirde. — Arm. pahrez 'Fasten' ist einmal im 14. Jhd.
belegt.
310. Zd. pairika- schlechtweg durch *Hure' zu iibersetzen,
ist falsch. Die Pairika s sind Teufelinnen, die die
Frommen zu verfuhren und vom rechten Glauben ab-
wendig zu machen suchen; phi. parlk bose Fee'
Bdh. Gl. 108, arm. parik ein Fabelwesen' (Eznik 97, 98),
np. pari 'Fee, EngeF.
312. Die Form piSman u. s. w. ist verkiirzt aus paslman, das
auch ins Afgh. {pa§Tmcin Veuig') iibergegangen ist. Vgl.
paz. poSetnan repentant', paSSmam 'penitence' Shk. 263,
Min. Gl. 157, phi. paSSmdnlh 'Reue* Phi. Min. p. 5, Z. X5,— 41 —
Die Sanskritubersetzung giebt das paz. Wort durch
=== HUB 9115-9128 ===
(Min. til. 10-13, Shk. 229—280), hanjaman Min. Gl. 99,
hangam Shk. 249 ; phi. anbdr, andam, angdrtan, hangam,
hanjaman Gl. and Ind. 43, 53, 52, 48 u. s. w. Die arm.
Lehnworter haben gleichfalls n fiir urspr. m, aber m vor 6,
das im Arm. bilabial war: ambar 'Speicher, amharem ich
speichere auf, hambar Speicher'; ambox *Menge, Volk* =
np. anboh; stambak 'streng, tyrannisch, widerspenstig* = np.
sitanba; bambak 'Baumwolle' = np. panba, paz. panba Min.
Gl. 154, phi. pambak Bdh. 65, 10; gmbef 'Kuppel* = np.
gmibad (syr. LW., Noldeke, Pers. Stud. II, 41); smpatak
Triifstein* = np. sunbada, arab. stmbadaj u. s. w. ; angam
-nial = np. hangam 'Zeit'; angarem Vechne an == np. an-
garam; andacem *untersuche' , np. andaz *Plan'; andam
*Glied* = np. andam; andarj 'Testament* = np. andarz
=== leaves ===
1365 -> leaf 50 printed p. 40
9122 -> leaf 265 printed p. 255
```


### [2026-09-07T20:45:01.971Z] TOOL RESULT

```
- i 3 o -
cadent. M.L.1196.
boluto, -as, -are: stercus egerere. Mot de la Mnlom. Chiron., sans
donte tire de ( 3 oXl.Xoc;. DerivA: bolutdtio.
bombus, -I m.: bourdonnement, bruit. Emprnnt ancien (deja dans
Ennius) an grec (fc>p,( 3 oc;. M.L. 1199; cf .bombax.
Derives et composAs: bombo, -onis m. : bourdon (Gloss.); bombisonus;
bonbio,-is; bombltio; bombisco, -is; bombilo,-as; bombosus ; bombicus;
bombico, -as , etc., attestAs tous k basae Apoqne.
bombyx, -Icis m .(bonbix, bumbix, bumbicis; bambis ): ver k soie.
Emprnnt an gr. ( 3 o(J.( 3 urapproche par 1 'Atymologie popnlaire de bombus,
cf. CGL II 570,31 bonbix: uermis qui a sono uocis nomen accepit. Les
formes romanes remontent k bonbix, bombax , attestA seniement dans la
1 . ecrite comme interpection empruntAe, gr. ( 3 op.| 3 o(.E,; M.L.1303 et i*oo
bonbyceus, et anssi i bambdx, suppose par la forme bambacis des gloses:
lanae similes flores arborum-, cf. M.L.933.
bonus, -a, -u* (de duenos, duonus , formes encore attestees k l'A-
poque archalque, cf. Thes. II 3079,34sqq.): bon. Le comparatif et le
snperlatif sont emprnntAs a d'antres racines: melior, optimus. Le
=== paelex ===
crime (Suet. Calig.36,8; Inscr. ). Derivd hybride de Tiaiyvoov "jeu" .paelex
- 840 -
paelex ( pel(l)ex \; pelica, Gloss.),-icis f.: pelices nunc quidem
appellantur alienis succumbentes non solum feminae, sed etiam mares
(cf. Suet., Caes.49). Antiqui proprie eam pelicem nominabant quae uxorem
habenti nubebat, P.F.248,1; "maitresse d'un homme marie, concubine",
puis "maitresse" en g^n^ral. Correspond a gr. raxXXai;, 7 KxXXcoct}, cf.
Paul. Dig.50,1G,144, avec lequel il est peut-etre en rapport. Iri.
c ai la.
D^riv£: paelicStus, -us m.: concubinage..
La graphie la mieux attestee est paelex', pellex est du a un rap-
prochement populaire soit avec pellis (cf. scortum), soit avec pellicii
( cf. pe 11 icStor). An cien (lex Numae), usuel. Non roman. Sans doute em-
prunte a une langue non i.-e. Outre le gr. mXXaEj, on rapproche 1 'hebreu
pi.leges "maitresse". Selon M. Ni edermann, Vox Roman. 1940, p.iOG,
1' emprunt aurait eu lieu k une date anterieure k la rupture de 1'unite
i.-e. puisque des correspondants des termes latin et grec sont fournis
par 1 1 avest. pairikd, nom donne k la femme seductrice qui cherche k
faire tomber en faute les hommes pieux, et par iri. airech, dat. airig
"concubine". Une influence etrusque est possible, cf. crapula,
paeminSsus: v. pSminisus.
```


## [2026-09-07T20:45:19.475Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"پنبه\" ARY_pages.txt | head -10; echo \"=== pari ===\"; grep -n \"^پری\\|پری \" ARY_pages.txt | head -10; echo \"=== latin index ===\"; grep -n -i \"PANBE\\|PAMBAK\\|PARI\\b\" ARY_latin_index_pages.txt | head -10",
 "description": "grep Aryanpur"
}
```


### [2026-09-07T20:45:19.547Z] TOOL RESULT

```
=== pari ===
=== latin index ===
2093:UPARI, UPARA :(SANSKRIT) 2» Sit. UPARIY — (OLD PERSIAN) sul, 4 |
4396:PARADIS :(RUMANIAN) go *PARI+DEHMI :(SANSKRIT) 2a Sie
4729:(OLD PERSIAN) «ly gd p\ PARI AFGHAN) (24) gil
5256:nee (FPA: QbU abe 2) hay ('35" 9"& 5" pp 4) PARI-AUZHAH
5259:ERI- AGAULISH) JF PARI- (SANSKRIT) cy Sule
11283:PER, PRE- PARIY, PARI, PER-
11285:PRO- s(CZECH) Soy PRA, PARI, (SANSKRIT) <4 Suite
```


## [2026-09-07T20:45:30.485Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%84%D9%82%DB%8C%D8%B3/",
 "prompt": "Quote any entry for بلقیس, especially from فرهنگ معین or دهخدا: who she was and any statement of the name's origin."
}
```


### [2026-09-07T20:45:37.743Z] TOOL RESULT

```
# Bilqis: Identity and Name Origins

## Who She Was

According to Dehkhoda's dictionary entry, Bilqis was "the daughter of Hdhad ibn Sharahbil, from the tribe of Yafar ibn Saksak, from Himyar," and served as queen of the Sabaean kingdom in Yemen. She was a contemporary of Prophet Solomon and, according Islamic narratives, became his wife.

## Name Origin

The dictionaries present multiple theories about the name's etymology:

**Uncertain origins:** "The true origin of the name Bilqis is not definitively known." Scholars have proposed several sources:

- A possible Greek term *pallakhis* (meaning virgin or concubine)
- Greek origins related to a musical instrument
- An Avestan word *pairika* from the Achaemenid period, which later became "peri" (fairy) in Persian

The consensus among etymologists is that "this word entered Hebrew and subsequently became *Bilqis* in Arabic."

**Notable distinction:** The Qur'an (27:20-44) references the Queen of Sheba but never names her. Islamic scholars and commentators later attributed the name Bilqis to this figure, though the exact historical period when this naming occurred remains unclear.
```


## [2026-09-07T20:45:45.316Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Queen_of_Sheba",
 "prompt": "Quote what the article says about the origin of the name Bilqis (Montgomery Watt, Greek pallakis, Hebrew pilegesh)."
}
```


## [2026-09-07T20:45:48.138Z] TOOL CALL #63: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg381.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/381.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/381.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-07T20:45:50.149Z] TOOL RESULT

```
# Origin of the Name Bilqis

According to the article, some Muslim commentators propose that the name "Bilqīs" derives from Greek *pallakís* or the Hebraized *pilegesh*, meaning "[concubine](https://en.wikipedia.org/wiki/Concubine "Concubine")".

The article states: "probably derived from [Greek](https://en.wikipedia.org/wiki/Greek_language "Greek language"): παλλακίς, [romanized](https://en.wikipedia.org/wiki/Romanization_of_Greek "Romanization of Greek"): _pallakis_ or the Hebraised _pilegesh_"

This etymological theory suggests the Queen's name has linguistic roots connecting her title to the concept of a royal consort or concubine across multiple ancient languages.
```


### [2026-09-07T20:45:50.204Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75771 Sep  7 16:45 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/381.png
```


## [2026-09-07T20:45:58.403Z] TOOL CALL #64: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A8%D9%87\" \\\n \"https://www.etymonline.com/word/bombast\" \\\n \"https://en.wiktionary.org/wiki/peri\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C\" \\\n \"https://www.etymonline.com/word/palladium\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%AC%CE%BB%CE%BB%CE%B1%CE%BE\" \\\n \"https://en.wiktionary.org/wiki/%CE%A0%CE%B1%CE%BB%CE%BB%CE%AC%CF%82\" \\\n \"https://en.wiktionary.org/wiki/pmbk%27\" \\\n \"https://abadis.ir/fatofa/%D9%BE%D9%86%D8%A8%D9%87/\" \\\n \"https://abadis.ir/fatofa/%D8%A8%D9%84%D9%82%DB%8C%D8%B3/\" \\\n \"https://en.wikipedia.org/wiki/Queen_of_Sheba\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"pdf page 381 (Pambak/Parika): source for cotton and pari/Pallas/Bilqis chains\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-07T20:46:06.160Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/79e828a3a3352e00.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/553c542587304ede.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f8feb98988f09792.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ab7c5d4990c9e20.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1096d07c99e0556b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/72b41dc6d575d136.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fd2a64b0fb986361.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3907dc2d0cc9c666.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8c4fb3f50e7ba023.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/56c2c92cd093d272.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e4ecafa079281e3a.txt
```


## [2026-09-07T20:47:03.590Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (5311,27025,28143):\n    lf='\\n'.join(lines[:ln]).count(chr(12))\n    print(ln,'leaf',lf,'-> approx printed p.', 2*(lf-12))\n\"",
 "description": "Compute Klein page estimates"
}
```


### [2026-09-07T20:47:05.013Z] TOOL RESULT

```
5311 leaf 108 -> approx printed p. 192
27025 leaf 596 -> approx printed p. 1168
28143 leaf 618 -> approx printed p. 1212
```


## [2026-09-07T20:54:52.700Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write381.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PANBEH = \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A8%D9%87\"\nW_PMBK   = \"https://en.wiktionary.org/wiki/pmbk%27\"\nE_BOMB   = \"https://www.etymonline.com/word/bombast\"\nW_PERI   = \"https://en.wiktionary.org/wiki/peri\"\nW_PARI   = \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DB%8C\"\nE_PALL   = \"https://www.etymonline.com/word/palladium\"\nW_PALLAX = \"https://en.wiktionary.org/wiki/%CF%80%CE%AC%CE%BB%CE%BB%CE%B1%CE%BE\"\nW_PALLAS = \"https://en.wiktionary.org/wiki/%CE%A0%CE%B1%CE%BB%CE%BB%CE%AC%CF%82\"\nA_PANBEH = \"https://abadis.ir/fatofa/%D9%BE%D9%86%D8%A8%D9%87/\"\nA_BELQIS = \"https://abadis.ir/fatofa/%D8%A8%D9%84%D9%82%DB%8C%D8%B3/\"\nWP_SHEBA = \"https://en.wikipedia.org/wiki/Queen_of_Sheba\"\n\ndata = {\n  \"pdf_page\": 381,\n  \"book_page\": 351,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Pambak, Bambak\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Middle Persian pambag [pmbk'] 'cotton' (Proto-Iranian/Wanderwort *pamba-/*bamba-)\",\n      \"note\": \"The Iranian etymon is genuine — MacKenzie's Concise Pahlavi Dictionary has 'pambag [pmbk'] cotton', Hübschmann quotes phl. pambak from Bundahišn 65,10 — and Buck's cited page 402 (6.24 COTTON) says in so many words: 'An oriental word, perh. orig. Iranian, represented by Pahl. pambak, Osset. bambag, NPers. panba, Arm. bambak.' Two reservations keep this from a flat 'confirmed'. (1) Buck's 'perh.' is real: Wiktionary's Middle Persian entry treats the family (Gk. bámbax, Khotanese mamṃa-, MP pambag) as going back to an unanalysable *bamba- of unknown ultimate origin — a Wanderwort travelling with the plant, not a securely Iranian formation. (2) The variant Nourai puts in the root box as a second Iranian form, 'Bambak', is in fact the shape the word takes in the languages that BORROWED it (Armenian bambak, Ossetic bambag, Gk. bámbax); no Iranian language of Iran has b-. The b-forms belong one level down, not in the root box. The rest of the chart (Pahlavi > Persian > Greek > Latin > French > English) is the standard account, given almost verbatim by Lokotsch no. 1617 and by Buck himself.\",\n      \"note_fa\": \"ریشهٔ «پنبه» در ایرانی است: در فارسی میانه pambag (نوشتار pmbk') و در بندهش pambak آمده و مکنزی و هوبشمان هر دو آن را ثبت کرده‌اند. باک (SYN ص ۴۰۲، بخش ۶٫۲۴ «پنبه») می‌نویسد این واژه‌ای شرقی است «شاید در اصل ایرانی» و صورت‌های پهلوی pambak، آسی bambag، فارسی نو panba و ارمنی bambak را برمی‌شمارد. دو نکته اما جای احتیاط دارد: نخست آنکه خاستگاه نهایی این واژه ناشناخته است و آن را واژهٔ سرگردان (Wanderwort) می‌دانند که همراه خودِ گیاه از زبانی به زبانی رفته است؛ دوم آنکه صورت «Bambak» که نورایی در جعبهٔ ریشه در کنار Pambak نهاده، صورت ایرانی نیست بلکه شکل وام‌گرفتهٔ آن در ارمنی و آسی و یونانی است. بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n      \"sources\": [W_PANBEH, W_PMBK, E_BOMB],\n      \"ref_check\": [\n        {\"ref\": \"SYN:402\", \"status\": \"supports\", \"note\": \"Buck, Selected Synonyms, p.402 = section 6.24 COTTON (running head reads '402 SELECTED INDO-EUROPEAN SYNONYMS 6.24 COTTON' in refs/SYN.txt line 10029). Para. 2: 'An oriental word, perh. orig. Iranian, represented by Pahl. pambak, Osset. bambag, NPers. panba, Arm. bambak. Schrader, loc. cit. Berneker 100 f.' — exactly Nourai's root, except that Buck's fourth form is ARMENIAN, not Aramaic (see node #7).\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"SYN\", \"where\": \"p.402, 6.24 COTTON\", \"stance\": \"supports\", \"note\": \"'Hence late Lat. bombax ... bombacium (> NE bombasine, bombast, Fr. bombasin, etc.), and apparently Grk. βόμβυξ (> Lat. bombyx) \\\"silkworm, silk\\\".' Buck makes bombax LATE LATIN, not Greek.\"},\n        {\"src\": \"PHD\", \"where\": \"p.65 s.v. pambag\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'pambag [pmbk' | N panba] cotton. ~ēn [-yn'] (made of) cotton.' (grep '^pambag' in refs/PHD_mackenzie.txt line 4002).\"},\n        {\"src\": \"LKT\", \"where\": \"no. 1617\", \"stance\": \"supports\", \"note\": \"Lokotsch: 'Pers. pumbä \\\"Baumwolle\\\" ... Aus der pers. Form pānbāk ergaben sich tk. pambuk \\\"Baumwolle\\\" und gr. πάμβαξ, παμβάκιον \\\"dass.\\\"; hieraus rum. bumbac, bulg. bubak, serb. pamuk, russ. bumaga \\\"Papier\\\" sowie mlat. bambacium, it. bambagia; aus lat. bombacium wurde frz. bombasin, engl. bombasine, bombazine.'\"},\n        {\"src\": \"HUB\", \"where\": \"p.255\", \"stance\": \"partial\", \"note\": \"Hübschmann lists 'bambak \\\"Baumwolle\\\" = np. panba, paz. panba Min. Gl. 154, phl. pambak Bdh. 65,10' in his catalogue of ARMENIAN loanwords with n>m before b — i.e. bambak is Armenian, from Pahlavi pambak.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"panbak, pambak\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Book Pahlavi writes the word pmbk', which MacKenzie normalises pambag and Hübschmann (following the older transcription of Bundahišn 65,10) pambak; the two spellings Nourai prints, panbak and pambak, are simply the same word with the nasal written n or m before the labial. The Pahlavi final -ak/-ag is the ordinary Middle Persian suffix -ag (< Old Iranian *-aka-), which regularly appears as -ak in the older Pahlavi transcriptions and as -ag in MacKenzie's. The word is attested in the Bundahišn's chapter on plants and passed from Middle Persian into Armenian (bambak), Ossetic (bambag) and Syriac.\",\n          \"derivation_fa\": \"در فارسی میانه این واژه به خط پهلوی pmbk' نوشته می‌شود؛ مکنزی آن را pambag و هوبشمان (به پیروی از آوانویسی کهن‌تر بندهش ۶۵٬۱۰) pambak می‌خواند. دو صورت panbak و pambak که نورایی آورده در واقع یک واژه‌اند و تفاوتشان تنها در نوشتن «ن» یا «م» پیش از واکِ لبیِ b است. پسوند ‑ak/‑ag همان پسوند رایج فارسی میانه (از ایرانی باستان ‑aka‑) است. این واژه از فارسی میانه به ارمنی (bambak)، آسی (bambag) و سریانی وام رفته است. ادعای نورایی درست است.\",\n          \"sources\": [W_PMBK],\n          \"ref_check\": [\n            {\"ref\": \"BQT:419\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, the پنبه entry (refs/BQT_v1_pages.txt leaf 645 ≈ printed p.420, so Nourai's 419 is right within the scan offset). Mo'in's footnote opens 'پنبه ‑ بفتح اول و کسر ... (لهجهٔ مرکزی), پهلوی [pambak] ...' and ends with the Latin scientific name Gossypium — i.e. Mo'in expressly gives the Pahlavi etymon.\"},\n            {\"ref\": \"MON:814\", \"status\": \"partial\", \"note\": \"Mo'in, Farhang-e Farsi: the online text of the entry (abadis.ir/fatofa/پنبه, section فرهنگ معین) reads '(پَ بِ) (اِ.) گیاهی علفی و یک ساله که از غوزهٔ آن ریسمان و پارچه درست کنند' — the headword is there but the web version strips the bracketed origin tag and the Latin-script Pahlavi form that the print edition carries, so the etymology on p.814 could not be read directly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p.65 s.v. pambag\", \"stance\": \"supports\", \"note\": \"'pambag [pmbk' | N panba] cotton' — MacKenzie's normalisation of exactly Nourai's form.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary (Part II)\", \"stance\": \"silent\", \"note\": \"grep -i 'pambak|pambag|panba' in refs/NYB_vol2_glossary.txt returns nothing; the word is not in Nyberg's Manual glossary.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.255\", \"stance\": \"supports\", \"note\": \"'phl. pambak Bdh. 65, 10' — Hübschmann cites the Bundahišn attestation of the Pahlavi word.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"panbeh «پنبه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"MP pambag > NP panba/panbe «پنبه»: the Middle Persian suffix -ag lost its final -g in New Persian (pambag > panba, as MP kanārag > kanāra, MP nāmag > nāma), and the labial nasal was assimilated in spelling to n before b (پنبه, pronounced [pambe]); modern Tehrani pronunciation is panbe/pambe, Gilaki keeps panba. Wiktionary states flatly 'From Middle Persian pmbk' (pambag, cotton)'. The idiom Nourai glosses — پنبه در گوش داشتن 'to have cotton in one's ears' = to be wilfully deaf/ignorant — is a genuine Persian expression, listed in Borhan-e Qate' itself ('پنبه در گوش، کنایه از مردم غافل و سخن ناشنو') and illustrated by the Nezāmi line the book quotes.\",\n          \"derivation_fa\": \"«پنبه» بازماندهٔ مستقیم فارسی میانهٔ pambag است؛ گافِ پایانی پسوند ‑ag در گذر به فارسی نو افتاده (مانند nāmag > نامه و kanārag > کناره) و «م» در املا پیش از «ب» به «ن» بدل شده، هرچند تلفظ همچنان [pambe] است (در گیلکی panba). ویکی‌واژه نیز آن را «از فارسی میانهٔ pambag» می‌داند. کنایهٔ «پنبه در گوش داشتن» که نورایی آورده در خودِ برهان قاطع آمده است: «پنبه در گوش، کنایه از مردم غافل و سخن ناشنو». ادعای نورایی درست است.\",\n          \"sources\": [W_PANBEH, A_PANBEH],\n          \"ref_check\": [\n            {\"ref\": \"BQT:419\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 645 (≈ printed p.420) carries the whole پنبه nest: 'پنبه در گوش کنایه از مردم غافل و سخن ناشنو باشد', 'پنبه‌زن ... حلاج و ندّاف', and Mo'in's footnote with the Pahlavi form and 'قطن بزبان علمی Gossypium'.\"},\n            {\"ref\": \"MON:814\", \"status\": \"partial\", \"note\": \"Mo'in's entry read online (abadis.ir/fatofa/پنبه): the definition matches, but the printed page's origin tag/Latin forms are not reproduced online.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss, grep 'panba|pumba|Baumwolle'\", \"stance\": \"silent\", \"note\": \"Horn has no entry for panba; the only hit is 'kurd. yūma \\\"grobes baumwollenes Zeug\\\"' (line 3873), unrelated.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.255\", \"stance\": \"supports\", \"note\": \"'bambak \\\"Baumwolle\\\" = np. panba, paz. panba Min. Gl. 154, phl. pambak Bdh. 65,10' — Hübschmann's own equation NP panba = Phl. pambak.\"},\n            {\"src\": \"BQT\", \"where\": \"vol.1 p.~420 s.v. پنبه\", \"stance\": \"supports\", \"note\": \"Mo'in's etymological footnote gives the Pahlavi antecedent under the headword.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"bombax\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"bombax\",\n          \"correct_form\": \"bámbax / pámbax (βάμβαξ / πάμβαξ); bombax is Late Latin\",\n          \"derivation\": \"A Greek word for cotton borrowed from Iranian is real, but it is not spelled bombax. Byzantine/late Ancient Greek has βάμβαξ (bámbax), with the by-forms βάμβηξ, βάμβιξ and πάμβαξ (pámbax) — the last preserving the Iranian p- — plus the derivative βαμβάκιον/παμβάκιον 'cotton wadding'; these came from Middle Persian pambag, in Greek-speaking territory probably through the Syriac/Anatolian cotton trade of late antiquity. The form with -o-, bombax (gen. bombacem, whence bombacium), is LATE LATIN: Buck's own page 402, the page Nourai cites for the root, says 'Hence late Lat. bombax ... bombacium', and Ernout-Meillet s.v. bombyx notes 'Les formes romanes remontent à bonbix, bombax, attesté seulement dans la langue écrite ... et aussi à bambax, supposé par la forme bambacis des gloses'. Klein on the cited page likewise writes 'ML. bombacium, fr. Gk. βαμβάκιον, cotton' and 'Gk. βόμβυξ, fr. βαμβάκιον, assimilated form of παμβάκιον, cotton, fr. Pers. pamba, cotton' — never 'Gk. bombax'. The printed page 351 of the dictionary really does read 'Greek | bombax : silk cotton', so the extraction is faithful and the error is the author's: he has given the Late Latin form a Greek label and has taken the gloss 'silk cotton' from the modern botanical genus Bombax (the silk-cotton tree) rather than from the Greek word, which means plain cotton.\",\n          \"derivation_fa\": \"یونانیِ βάμβαξ (bámbax) و گونه‌های آن βάμβηξ، βάμβιξ و πάμβαξ (pámbax، با پـِ ایرانی) و مشتق βαμβάκιον «پنبهٔ حلاجی‌شده» همگی وام‌واژه‌هایی از فارسی میانهٔ pambag اند و در اواخر دورهٔ باستان از راه بازرگانی پنبه در شام و آناتولی به یونانی رفته‌اند. اما صورتِ با «ـُ»، یعنی bombax، یونانی نیست بلکه لاتینی متأخر است: خودِ باک در همان صفحهٔ ۴۰۲ می‌نویسد «Hence late Lat. bombax … bombacium» و ارنو ـ مه‌یه نیز آن را لاتینی می‌داند؛ کلاین هم در صفحهٔ مورد استناد نورایی می‌نویسد «ML. bombacium, fr. Gk. βαμβάκιον». تصویر صفحهٔ ۳۵۱ چاپی نشان می‌دهد که در خودِ کتاب «Greek bombax» چاپ شده است؛ پس خطای خوانش اسکن نیست، خطای چاپ/نویسندهٔ کتاب است: نورایی صورت لاتینی متأخر را یونانی خوانده و معنی «silk cotton» را هم از نام جنس گیاه‌شناسیِ Bombax (درخت پنبهٔ ابریشمی) گرفته، نه از واژهٔ یونانی که معنی‌اش «پنبه» ساده است.\",\n          \"sources\": [W_PMBK, E_BOMB],\n          \"ref_check\": [\n            {\"ref\": \"KLN:185\", \"status\": \"partial\", \"note\": \"Klein s.v. Bombyx (refs/KLN_1966.txt line 5316): 'L. bombyx, silkworm, fr. Gk. βόμβυξ, fr. βαμβάκιον, assimilated form of παμβάκιον, cotton, fr. Pers. pamba, cotton'; s.v. bombazine (line 5313): 'F. bombasin, fr. ML. bombacium, fr. Gk. βαμβάκιον, cotton'. Klein confirms the Persian>Greek borrowing and the whole chain, but his Greek forms are βαμβάκιον/παμβάκιον and βόμβυξ — he never gives a Greek 'bombax'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SYN\", \"where\": \"p.402, 6.24 COTTON para. 2\", \"stance\": \"contradicts\", \"note\": \"'Hence late Lat. bombax \\\"linteorum aut aliae quaevis quisquiliae\\\" (Du Cange), bombacitum [read bombacium] (> NE bombasine, bombast, Fr. bombasin, etc.), and apparently Grk. βόμβυξ (> Lat. bombyx)' — bombax is explicitly Late Latin for Buck.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1617\", \"stance\": \"partial\", \"note\": \"Lokotsch has the Greek forms as 'gr. πάμβαξ, παμβάκιον' from Pers. pānbāk, and the Latin as 'mlat. bambacium ... lat. bombacium' — again p-/bamb- in Greek, bomb- in Latin.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. bombyx (p.~130)\", \"stance\": \"contradicts\", \"note\": \"'Les formes romanes remontent à bonbix, bombax, attesté seulement dans la l. écrite ... et aussi à bambax, supposé par la forme bambacis des gloses' — bombax/bambax are treated as Latin forms.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"bombyx\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin bombyx, -ycis 'silkworm, silk' is a real word, borrowed from Greek βόμβυξ, and Klein — Nourai's source here — does make it the Latin outlet of the cotton word: 'L. bombyx, silkworm, fr. Gk. βόμβυξ, fr. βαμβάκιον, assimilated form of παμβάκιον, cotton, fr. Pers. pamba'. But two qualifications. (1) Buck, more cautiously, says only that Gk. βόμβυξ is 'apparently' from the same oriental source, and Ernout-Meillet note that Latin bombyx was reshaped by popular etymology after bombus 'buzzing' ('CGL II 570,31 bombix: uermis qui a sono uocis nomen accepit'); the silkworm word and the cotton word were not originally the same and got confused only in late Latin. (2) The English words at the end of the chart do NOT descend from bombyx but from the cotton branch, Late Latin bombax/bombacem, bombacium (see node #6). So the arrow bombax > bombyx is Klein's, but the arrow bombyx > French > bombast is not: the true intermediate is bombacem.\",\n          \"derivation_fa\": \"لاتینیِ bombyx, -ycis «کرم ابریشم، ابریشم» واژه‌ای واقعی و وام‌گرفته از یونانیِ βόμβυξ است، و کلاین ــ منبع نورایی ــ نیز همان را دنبالهٔ واژهٔ پنبه می‌داند: «L. bombyx … fr. Gk. βόμβυξ, fr. βαμβάκιον … fr. Pers. pamba». اما دو نکته: نخست، باک محتاطانه‌تر می‌گوید βόμβυξ «ظاهراً» از همان خاستگاه شرقی است، و ارنو ـ مه‌یه یادآور می‌شوند که صورت لاتینی زیر تأثیر ریشه‌شناسی عامیانه با bombus «وزوز» شکل گرفته است؛ یعنی نام کرم ابریشم و نام پنبه در اصل یکی نبوده‌اند و تنها در لاتینی متأخر درهم آمیخته‌اند. دوم، واژه‌های انگلیسیِ پایان نمودار از bombyx نمی‌آیند بلکه از شاخهٔ پنبه، یعنی لاتینی متأخر bombax / bombacem / bombacium. پس این حلقه با احتیاط پذیرفتنی است.\",\n          \"sources\": [E_BOMB],\n          \"ref_check\": [\n            {\"ref\": \"KLN:185\", \"status\": \"supports\", \"note\": \"Klein s.v. Bombyx: 'L. bombyx, silkworm, fr. Gk. βόμβυξ, fr. βαμβάκιον, assimilated form of παμβάκιον, cotton, fr. Pers. pamba, cotton. Cp. bombast, bombazine.' — precisely the arrow Nourai draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. bombyx\", \"stance\": \"partial\", \"note\": \"'bombyx, -ĭcis m. (bonbix, bumbix, bumbicis; bambis): ver à soie. Emprunt au gr. βόμβυξ, rapproché par l'étymologie populaire de bombus' — Latin from Greek, but contaminated with bombus.\"},\n            {\"src\": \"SYN\", \"where\": \"p.402\", \"stance\": \"partial\", \"note\": \"'and apparently Grk. βόμβυξ (> Lat. bombyx) \\\"silkworm, silk\\\"' — Buck's 'apparently' marks the link to the cotton word as uncertain.\"},\n            {\"src\": \"WEB\", \"where\": \"grep 'bombyx' in refs/WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"no usable entry recovered from the OCR of Webster vol. 1.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box, and a correct one: the French link in the chain is real and well documented. Old French had bombace 'cotton, cotton wadding' (from Late Latin bombacem, accusative of bombax), which is the immediate source of English bombace/bombast; and French bombasin (from Medieval Latin bombacinium) is the immediate source of English bombazine. Etymonline gives exactly this: bombast < 1550s bombace 'raw cotton' < Old French bombace < Late Latin bombacem.\",\n          \"derivation_fa\": \"این جعبه تهی است و تنها حلقهٔ واسطه را نشان می‌دهد؛ و درست هم هست: در فرانسهٔ کهن bombace «پنبه، لایی پنبه‌ای» (از لاتینی متأخر bombacem، حالت مفعولی bombax) وجود داشته که خاستگاه مستقیم bombace/bombast انگلیسی است، و bombasin فرانسوی (از لاتینی میانهٔ bombacinium) خاستگاه bombazine انگلیسی. اتیمآنلاین همین زنجیره را می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [E_BOMB],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; it is an unlabelled transmission step.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1617\", \"stance\": \"supports\", \"note\": \"'aus lat. bombacium wurde frz. bombasin, engl. bombasine, bombazine; dtsch. Bombasin'.\"},\n            {\"src\": \"SYN\", \"where\": \"p.402\", \"stance\": \"supports\", \"note\": \"'bombacium (> NE bombasine, bombast, Fr. bombasin, etc.)' — Buck puts French bombasin in the same chain.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"bombast, bombazine\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English bombace 'raw cotton' (1550s) > bombast 'cotton stuffing, padding for clothes' (1570s), then figuratively 'inflated, padded speech' (1580s) — the semantic shift is from the tailor's wadding to the rhetorician's; the -t is an excrescent English addition to bombace. bombazine (also bombasine, 1550s 'raw cotton', 1570s 'twilled dress material of silk and worsted') is from French bombasin < Medieval Latin bombacinium. Klein's cited entry adds the story that bombast is 'lit. in the style of Bombastus Paracelsus', but he immediately says 'The PN. Bombast comes fr. ML. bombacium, fr. Gk. βαμβάκιον, cotton' — so even in Klein the cotton word is the ultimate source, and the Paracelsus link is a later association, treated by Etymonline as unnecessary. Nourai's gloss 'soft padding' is the 16th-century literal sense, correct.\",\n          \"derivation_fa\": \"در انگلیسی bombace «پنبهٔ خام» (دههٔ ۱۵۵۰) به bombast «لایی پنبه‌ای جامه» (دههٔ ۱۵۷۰) و سپس به معنی مجازیِ «سخنِ پرطمطراق و پوک» (دههٔ ۱۵۸۰) رسید؛ یعنی تحول معنایی از «لایی خیاط» به «پُرگوییِ خطیب». صورت bombazine (از فرانسوی bombasin و لاتینی میانهٔ bombacinium) نیز نخست «پنبهٔ خام» و سپس نام پارچه‌ای از ابریشم و پشم شد. کلاین در همان مدخل داستان انتساب به «بومباستوس پاراسلسوس» را می‌آورد اما بی‌درنگ می‌افزاید که خودِ آن نام خانوادگی از ML. bombacium و یونانی βαμβάκιον «پنبه» است. معنی «soft padding» که نورایی آورده همان معنی تحت‌اللفظی سدهٔ شانزدهم است. ادعای نورایی درست است.\",\n          \"sources\": [E_BOMB],\n          \"ref_check\": [\n            {\"ref\": \"KLN:185\", \"status\": \"supports\", \"note\": \"Klein: 'bombast, n., high-sounding speech. — From Bombastic, lit. in the style of Bombastus Paracelsus (1493-1541). The PN. Bombast comes fr. ML. bombacium, fr. Gk. βαμβάκιον, cotton. See Bombyx.' and 'bombazine, bombasine, n., twilled silk cloth with worsted or cotton. — F. bombasin, fr. ML. bombacium, fr. Gk. βαμβάκιον, cotton.' (refs/KLN_1966.txt lines 5311-5313).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"index of words 'Italian from Greek: ... bombast' (p.619 list)\", \"stance\": \"partial\", \"note\": \"Skeat's distribution list files bombast under 'Italian from Greek'; his concise entry could not be recovered legibly from the two-column OCR.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1617 (index entry 'bombazine 1617')\", \"stance\": \"supports\", \"note\": \"Lokotsch derives engl. bombasine, bombazine from frz. bombasin < lat. bombacium, in the same article as Pers. pānbāk.\"},\n            {\"src\": \"SYN\", \"where\": \"p.402\", \"stance\": \"supports\", \"note\": \"'bombacium (> NE bombasine, bombast ...)'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Aramaic\",\n          \"words\": \"bambak\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"Aramaic | bambak : cotton\",\n          \"correct_form\": \"Armenian bambak (Buck's 'Arm.')\",\n          \"derivation\": \"The reference Nourai attaches to this box gives the word away. Buck, p.402, the page cited, lists 'Pahl. pambak, Osset. bambag, NPers. panba, Arm. bambak' — 'Arm.' is Buck's standard abbreviation for ARMENIAN, and Armenian bambak 'cotton' is a well-known Middle Iranian loan: Hübschmann puts it in his list of Armenian borrowings that show n>m before b ('bambak \\\"Baumwolle\\\" = np. panba, paz. panba, phl. pambak Bdh. 65,10', Persische Studien p.255). Aramaic did borrow the word, but in a different shape — Wiktionary's Middle Persian entry gives Classical Syriac palbaḡ, not bambak — and Buck's page mentions no Aramaic at all. The printed page 351 does read 'Aramaic ... bambak : cotton', so the JSON is faithful; the mistake is the author's, an expansion of Buck's 'Arm.' as Aramaic instead of Armenian. Read as Armenian, the arrow is correct: Middle Persian pambak > Armenian bambak, one of the several hundred Middle Iranian loans in Classical Armenian.\",\n          \"derivation_fa\": \"خودِ ارجاعی که نورایی به این جعبه بسته، پرده از خطا برمی‌دارد: باک در صفحهٔ ۴۰۲ (همان صفحهٔ مورد استناد) صورت‌های «Pahl. pambak, Osset. bambag, NPers. panba, Arm. bambak» را برمی‌شمارد و «.Arm» در آن کتاب کوتاه‌نوشتِ «ارمنی» است، نه آرامی. bambak ارمنی از وام‌واژه‌های شناختهٔ ایرانی میانه در ارمنی است و هوبشمان (پژوهش‌های فارسی، ص ۲۵۵) آن را در فهرست وام‌واژه‌های ارمنی با ابدال n>m پیش از b آورده است. آرامی نیز این واژه را وام گرفته اما به صورتی دیگر (سریانی کلاسیک palbaḡ بنا بر ویکی‌واژه)، و در صفحهٔ باک هیچ نامی از آرامی نیست. تصویر صفحهٔ ۳۵۱ چاپی نشان می‌دهد که در کتاب «Aramaic bambak» چاپ شده؛ پس خطای استخراج نیست، خطای خودِ کتاب است: نویسنده «.Arm» را «آرامی» خوانده است. اگر «ارمنی» بخوانیم، پیکان درست است.\",\n          \"sources\": [W_PMBK],\n          \"ref_check\": [\n            {\"ref\": \"SYN:402\", \"status\": \"contradicts\", \"note\": \"Buck p.402 (6.24 COTTON, para. 2) has 'Arm. bambak' = Armenian; there is no Aramaic form anywhere on the page, and its language list (NG, Dan., Lith., It., Sw., Lett., Fr., ME, SCr., Sp., Boh., Rum., Du., Pol., NIr., MHG, Russ., W., NHG, Skt., Br.) contains no Semitic language at all.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.255\", \"stance\": \"contradicts\", \"note\": \"Hübschmann lists bambak among the ARMENIAN loanwords: 'bambak \\\"Baumwolle\\\" = np. panba, paz. panba Min. Gl. 154, phl. pambak Bdh. 65,10'.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"grep 'Baumwolle' finds only the discussion of Arabic قطن ('ist gewiss kein echt arabisches Wort', line 5261) and of a vessel 'zur Aufbewahrung von Baumwolle'; Fraenkel has no Aramaic bambak.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1617\", \"stance\": \"silent\", \"note\": \"Lokotsch's long list of borrowings from Pers. pānbāk (Turkish, Greek, Latin, Romance, Slavic, Romanian) does not include Aramaic.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Parîkâ\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Iranian *parikā- 'sorceress, demoness' (Pokorny IEW 789 'parika- concubine, only Iranian and Irish'; the wider IE grouping is Walde-Pokorny II 7 *pallā-q-/*pali-q- 'young girl')\",\n      \"note\": \"The cited page is exactly right and says almost exactly this — Pokorny, IEW p.789: 'Root/lemma: parika. Meaning: concubine. Note: only Iranian and Irish. Material: Avestan pairikā \\\"dämonische Buhlerin\\\", mp. parīk, np. parī \\\"Peri\\\" (iran. *parikā-); Middle Irish a(i)rech \\\"concubine\\\". References: Thurneysen IF. 42, 146 f., WP. II 7.' Two things follow. (1) Pokorny's gloss is 'concubine' and his header says the lemma is confined to Iranian and Irish; Nourai's 'sweet heart, fairy' is the softened New-Persian sense read back into the proto-language, and calling the box 'Indo-European' overstates a lemma that Pokorny himself restricts to two branches. (2) The Greek arm of Nourai's chart (Pallas, pallax) is NOT in Pokorny 1959; it is in the older Walde-Pokorny II 7, where the lemma is 'pallā-q-, pali-q- \\\"(junges) Mädchen, auch (gr.) Knabe\\\"' and Av. pairikā, mp. parīk, np. parī stand alongside gr. παλλακίς, παλλακή, πάλλαξ, Παλλάς and Lat. paelex. So Nourai's chart reproduces the 1927 Walde-Pokorny grouping, which Pokorny quietly abandoned in 1959. Bartholomae marks the etymology of pairikā- simply 'Et.?', and Ernout-Meillet think the Greek and Latin words are 'sans doute emprunté à une langue non i.-e.' — the opposite direction from an inherited IE root.\",\n      \"note_fa\": \"صفحهٔ مورد استناد دقیقاً درست است: پوکورنی در فرهنگ ریشه‌شناختی هندواروپایی، ص ۷۸۹ می‌آورد: «ریشه: parika، معنی: کنیزک/معشوقه، یادداشت: تنها ایرانی و ایرلندی؛ مادّه: اوستایی pairikā «زن اغواگر دیوسان»، فارسی میانه parīk، فارسی نو parī، ایرانی *parikā-؛ ایرلندی میانه a(i)rech». دو نکته: نخست، معنایی که پوکورنی می‌دهد «کنیزک» است و دامنهٔ ریشه را به دو شاخه محدود می‌کند؛ پس عنوان «هندواروپایی» و معنی «sweet heart, fairy» که نورایی نهاده، معنای متأخرِ فارسی است که به دورهٔ آغازین بازتابانده شده. دوم، شاخهٔ یونانی نمودار (Pallas، pallax) در پوکورنی ۱۹۵۹ نیست؛ در والده ـ پوکورنی، جلد دوم ص ۷ است، آنجا که ریشهٔ *pallā-q-/*pali-q- «دخترِ جوان» هم pairikā اوستایی و parīk و parī را دربر می‌گیرد و هم παλλακίς و πάλλαξ و Παλλάς یونانی و paelex لاتینی را. بنابراین نمودار نورایی بازتاب دسته‌بندی سال ۱۹۲۷ است که پوکورنی خود در ۱۹۵۹ از آن دست کشیده. بارتولومه ریشهٔ pairikā- را با علامت «Et.?» ناشناخته می‌داند و ارنو ـ مه‌یه واژهٔ یونانی و لاتینی را «بی‌گمان وام از زبانی غیرهندواروپایی» می‌شمارند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n      \"sources\": [W_PARI, W_PALLAX],\n      \"ref_check\": [\n        {\"ref\": \"POK:789\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.789 (refs/POK_full.txt lines 64729-64736, the entry tagged 'Page(s): 789'): 'Root / lemma: parika | Meaning: concubine | Note: only Iran. and Irish | Material: Avestan pairikā \\\"dämonische Buhlerin\\\", mp. parīk, np. parī \\\"Peri\\\" (Iran. *parikā-); Middle Irish a(i)rech \\\"concubine\\\". References: Thurneysen IF. 42, 146 f., WP. II 7.' The page and lemma are exactly as cited; only the gloss and the 'Indo-European' scope are Nourai's own.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p.7, lemma 'pallā-q-, pali-q-'\", \"stance\": \"supports\", \"note\": \"'pallā-q-, pali-q- (junges) \\\"Mädchen, auch (gr.) Knabe\\\" und verwandte Formen. Av. pairikā \\\"die Frommen durch Liebeskünste vom Glauben abspenstig machende schöne Frauen\\\", mp. parīk, np. parī \\\"Peri\\\" (iran. *parīkā); gr. παλλακίς, παλλακή \\\"Beischläferin, Kebsweib\\\" ... lat. paelex ... πάλλαξ ... Παλλάς Beiwort der Athene' — this, not Pokorny 1959, is the source of Nourai's whole chart including the Greek branch. (refs/incoming/WLD/WLD_Bd2_pages.txt leaf 11, running head 'palia-q  pasto-').\"},\n        {\"src\": \"BRT\", \"where\": \"col. 863\", \"stance\": \"partial\", \"note\": \"Bartholomae, AiW col. 863: 'pairikā- f. \\\"Zauberin, Hexe\\\"' with the footnote 'Das weibliche Gegenstück des yātu-'; and 'Et.? — np. parī. — Pahl.: parīk ... Die Erklärung BB. 15,9 wird durch mp. parīk, np. parī unwahrscheinlich, die auf ir. *parikā- [weisen]'. Bartholomae confirms the Iranian reconstruction but leaves the etymology open.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, grep 'parika|pairika'\", \"stance\": \"silent\", \"note\": \"no such root in the American Heritage IE appendix — consistent with Pokorny's note that the lemma is Iranian-and-Irish only.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, grep 'parika|pairika'\", \"stance\": \"silent\", \"note\": \"Mann's Indo-European Comparative Dictionary has no entry for the root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"pairikâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan pairikā- is real and frequent (Yt. 8.8, 8.54, Yt. 5, Vd. 1.9, 19.5, Y. 16.8 etc.), but its meaning is not 'beautiful woman'. Bartholomae, AiW col. 863, glosses it 'Zauberin, Hexe' — sorceress, witch — and notes in a footnote that she is 'das weibliche Gegenstück des yātu-', the female counterpart of the male sorcerer; in the Yašts the pairikās are meteor-demons whom Tištrya fights and who bring drought (pairika yā duž́yāirya 'the pairikā of bad harvests'). Hübschmann puts the point sharply at Persische Studien p.40, commenting on Horn's no. 310: 'Zd. pairika- schlechtweg durch \\\"Hure\\\" zu übersetzen, ist falsch. Die Pairikas sind Teufelinnen, die die Frommen zu verführen und vom rechten Glauben abwendig zu machen suchen' — she-devils who seduce the pious and turn them from the true faith. That is the discussion Nourai's NOTE points to (AEF:375 = Khaleqi Motlaq's Persian translation of Horn with Hübschmann's notes), and the note is right: the seducer sense is the original one, and 'beautiful woman' is a much later, New-Persian development. Morphologically the word is a feminine in -ā- to a stem *pari-ka-, but Bartholomae writes 'Et.?' and expressly withdraws his own earlier explanation ('die Fremde', BB 15,9) as made improbable by mp. parīk, np. parī, which point to Iranian *parikā-.\",\n          \"derivation_fa\": \"pairikā- اوستایی واژه‌ای واقعی و پربسامد است (یشت ۸٬۸ و ۸٬۵۴، یشت ۵، وندیداد ۱٬۹ و ۱۹٬۵، یسنا ۱۶٬۸ و…)، اما معنایش «زن زیبا» نیست. بارتولومه در ستون ۸۶۳ آن را «جادوگرِ زن، ساحره» معنی می‌کند و در پانوشت می‌افزاید که پری «همتای مادینهٔ yātu (جادوگر مرد)» است؛ در یشت‌ها پریان دیوانِ شهاب‌گونه‌اند که تیشتر با آنان می‌جنگد و خشک‌سالی می‌آورند (pairika yā duž́yāirya «پریِ بدسالی»). هوبشمان در پژوهش‌های فارسی ص ۴۰، در حاشیهٔ شمارهٔ ۳۱۰ هرن، صریح می‌گوید: ترجمهٔ pairika- به «روسپی» نادرست است؛ پریان دیوزنانی‌اند که می‌کوشند پرهیزگاران را بفریبند و از راه راست بگردانند. همین است آن بحثی که یادداشت نورایی (AEF:375، ترجمهٔ فارسی هرن به قلم خالقی مطلق) بدان اشاره دارد و یادداشت درست است: معنی «اغواگر» کهن‌تر است و «زن زیبا» تحولی بسیار متأخر در فارسی نو. از نظر ساخت، واژه مؤنثِ ‑ā‑ بر ستاک *pari-ka- است، اما بارتولومه ریشه را با «Et.?» ناشناخته می‌گذارد و توضیح پیشین خودش («بیگانه») را پس می‌گیرد.\",\n          \"sources\": [W_PARI],\n          \"ref_check\": [\n            {\"ref\": \"POK:789\", \"status\": \"partial\", \"note\": \"Pokorny p.789 has 'Avestan pairikā \\\"dämonische Buhlerin\\\"' — demonic seductress, not 'beautiful woman'.\"},\n            {\"ref\": \"KLN:1115\", \"status\": \"partial\", \"note\": \"Klein s.v. Pallas (refs/KLN_1966.txt line 27026): 'Cp. Avestic pairika, \\\"beautiful women seducing pious men\\\" (whence Middle Pers. parik, ModPers. pari, \\\"fairy\\\")' — Klein's gloss is where Nourai's 'beautiful woman' comes from, but Klein keeps the essential 'seducing pious men'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 863 s.v. pairikā-\", \"stance\": \"partial\", \"note\": \"'j. pairikā- f. \\\"Zauberin, Hexe\\\"'; footnote 'Das weibliche Gegenstück des yātu-'; 'Et.? — np. parī. — Pahl.: parīk.' Confirms form and Iranian descent, contradicts the gloss 'beautiful woman'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.40 (ad Horn 310)\", \"stance\": \"partial\", \"note\": \"'Zd. pairika- schlechtweg durch \\\"Hure\\\" zu übersetzen, ist falsch. Die Pairikas sind Teufelinnen, die die Frommen zu verführen und vom rechten Glauben abwendig zu machen suchen; phl. parīk \\\"böse Fee\\\" Bdh. Gl. 108, arm. parik \\\"ein Fabelwesen\\\" (Eznik 97, 98), np. parī \\\"Fee, Engel\\\".'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.7\", \"stance\": \"supports\", \"note\": \"'Av. pairika \\\"die Frommen durch Liebeskünste vom Glauben abspenstig machende schöne Frauen\\\", mp. parīk, np. parī \\\"Peri\\\" (iran. *parīkā)' — Walde-Pokorny's gloss is the closest of all to Nourai's 'beautiful woman', because it keeps both the beauty and the seduction.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"parîk\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. pairikā- > Middle Persian parīk/parīg, written plyk' in Book Pahlavi and pryg in Manichaean Middle Persian: Old Iranian *pari-kā- lost the internal -i- of pairi- through syncope in the Middle Iranian period and the feminine ending -ā was dropped with the collapse of grammatical gender, giving parīk with compensatory long ī. MacKenzie prints 'parīg [plyk' | M pryg, N parī] witch'; Nyberg's glossary has 'parīk [plyk] sorceress, witch, pl. obl. -ān ... — Av. (863 sq.) pairikā-; Arm. lw. parik; MPrthPrs pryg; Paz. parī (SGV); NP parī', and adds the derivative parīkīh 'the art, practices of sorceresses'. The Pahlavi word still means 'witch, demoness', as in Avestan; Nourai's gloss 'fairy' is the New Persian sense.\",\n          \"derivation_fa\": \"pairikā- اوستایی در فارسی میانه به parīk/parīg بدل شده که در پهلوی کتابی plyk' و در فارسی میانهٔ مانوی pryg نوشته می‌شود: واکهٔ میانیِ pairi- در دورهٔ ایرانی میانه افتاده و پایانهٔ مؤنثِ ‑ā با از میان رفتن جنس دستوری حذف شده و «ای» کشیده بر جای مانده است. مکنزی می‌آورد: «parīg [plyk' | M pryg, N parī] witch»؛ نیبرگ در واژه‌نامهٔ خود می‌نویسد: «parīk [plyk] ساحره، جادوگر… ــ اوستایی (۸۶۳ به بعد) pairikā-؛ وام‌واژهٔ ارمنی parik؛ پارتی/فارسی مانوی pryg؛ پازند parī؛ فارسی نو parī»، و مشتق parīkīh «جادوگری» را نیز ثبت کرده است. معنی پهلوی همچنان «جادوگر، دیوزن» است و «fairy» معنای فارسی نو است. ادعای نورایی درست است.\",\n          \"sources\": [W_PARI],\n          \"ref_check\": [\n            {\"ref\": \"POK:789\", \"status\": \"supports\", \"note\": \"Pokorny p.789: 'mp. parīk' in the chain Avestan pairikā > mp. parīk > np. parī.\"},\n            {\"ref\": \"KLN:1115\", \"status\": \"supports\", \"note\": \"Klein s.v. Pallas: '(whence Middle Pers. parik, ModPers. pari, \\\"fairy\\\")'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p.65 s.v. parīg\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'parīg [plyk' | M pryg, N parī] witch' (refs/PHD_mackenzie.txt line 4035); the English-Pahlavi index has 'witch parīg'.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. parīk\", \"stance\": \"supports\", \"note\": \"'parīk [plyk] sorceress, witch, pl. cas. obl. ~-n 8714.21, 0027. — Av. (863 sq.) pairikā-; Arm. lw. parik; MPrthPrs pryg; Paz. parī (SGV); NP parī.' plus 'parīkīh the art, practices of sorceresses'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"parî «پری»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"MP parīk > NP parī «پری»: final -k of Middle Persian -īk regularly falls in New Persian (MP tārīk > tārī alongside tārīk, MP nēk > nēk but MP -īk > -ī in this class), and Pāzand already has parī. Horn's Grundriss no. 310 (p.69), the page Nourai cites, sets it out in one line: 'perī \\\"Peri, guter Genius\\\". aw. pairīkā- \\\"Hure\\\"; phlv. parīk, arm. LW. parik, LW. afġ. parī.' Mo'in's footnote in Borhan-e Qate' (printed p. ~398, Nourai's 396) gives 'پهلوی parīk، ارمنی parik، افغانی parī' and explains that in Avestan the pairikā is a female 'sorcerer' set on by Ahriman to turn the Mazdayasnians from the straight path, that pairikās belong to Ahriman's host and take the form of comets to fight the rain, and that 'in Persian literature the word came to be applied to a kind of extremely beautiful woman'. That last sentence is the semantic history in a nutshell: demoness > enchantress > fairy > beauty. The compounds Nourai adds — پریسا 'fairy-like', پریدخت 'fairy-daughter', پریچهر 'fairy-faced', پری‌پوش — are all built on the aesthetic sense and are ordinary New Persian bahuvrīhi/compound formations.\",\n          \"derivation_fa\": \"«پری» بازماندهٔ parīk فارسی میانه است: کافِ پایانی ‑īk در فارسی نو می‌افتد و در پازند نیز پیش‌تر parī آمده است. هرن در شمارهٔ ۳۱۰ (ص ۶۹) ــ همان صفحه‌ای که نورایی یاد کرده ــ می‌نویسد: «perī «پری، فرشتهٔ نیک». اوستایی pairīkā-؛ پهلوی parīk؛ وام‌واژهٔ ارمنی parik؛ افغانی parī». معین نیز در حاشیهٔ برهان قاطع (ص ۳۹۸ چاپی، ارجاع نورایی ۳۹۶) صورت‌های «پهلوی parīk، ارمنی parik، افغانی parī» را می‌آورد و توضیح می‌دهد که «در اوستا پری جنس مؤنث «جادو» محسوب شده که از طرف اهریمن گماشته شده تا پیروان مزدیسنا را از راه راست منحرف سازد… همچنین پریان در زمرهٔ سپاه اهریمن… به شکل ستارگان دنباله‌دار با باران در ستیزند» و می‌افزاید «در ادبیات پارسی به نوعی از زنان که نهایت خوبرو باشند اطلاق شده». همین است تاریخ تحول معنایی: دیوزن ← افسونگر ← پری ← زیبارو. ترکیب‌های پریسا، پریدخت، پریچهر و پری‌پوش همه بر همین معنای زیبایی‌شناختی ساخته شده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [W_PARI],\n          \"ref_check\": [\n            {\"ref\": \"POK:789\", \"status\": \"supports\", \"note\": \"'np. parī \\\"Peri\\\" (Iran. *parikā-)'.\"},\n            {\"ref\": \"KLN:1115\", \"status\": \"supports\", \"note\": \"Klein s.v. Pallas: 'ModPers. pari, \\\"fairy\\\"'.\"},\n            {\"ref\": \"HRN:69\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 310, on printed p.69 (refs/HRN.txt leaf 90, offset leaf = printed + 21): '310. perī \\\"Peri, guter Genius\\\". aw. pairīkā- \\\"Hure\\\"; phlv. parīk, arm. LW. parik, LW. afġ. parī. Nach Bartholomae, BB. 15, 9 ist die SiW. pairikā- ursprünglich \\\"die Fremde\\\".' Exactly Nourai's chain.\"},\n            {\"ref\": \"BQT:396,864\", \"status\": \"partial\", \"note\": \"The پری article with Mo'in's long etymological footnote sits at BQT_v1_pages.txt leaf 620 ≈ printed p.398 (the scan offset drifts by 2-3 pages, so Nourai's 396 is right): 'در پهلوی parīk ارمنی parik افغانی [parī] «اسشق ۳۰۴»… گیلکی… در ادبیات پارسی بنوعی از زنان که نهایت خوبرو باشند اطلاق شده «غیاث‌اللغات»'. The second number, 864, falls in vol. 2 (ث/ج onward) and cannot be a second پری entry; it was not located.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 310, p.69\", \"stance\": \"supports\", \"note\": \"See ref_check; Horn is the classical statement of the chain.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.40\", \"stance\": \"supports\", \"note\": \"'phl. parīk \\\"böse Fee\\\" Bdh. Gl. 108, arm. parik \\\"ein Fabelwesen\\\" (Eznik 97, 98), np. parī \\\"Fee, Engel\\\".'\"},\n            {\"src\": \"BQT\", \"where\": \"vol.1 p.~398 s.v. پری\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote (quoted above) with the Pahlavi, Armenian, Afghan and Gilaki forms and the Avestan background.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's Persian OCR yields no clean پری headword; the Latin index shows only garbled 'PARI (AFGHAN)' fragments (line 4729) that cannot be quoted responsibly.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"Peri\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English peri 'a beautiful, benevolent sprite of Persian myth' is a literary borrowing of Persian parī, taken in through Ottoman Turkish peri (so Wiktionary) and popularised by the orientalising Romantics — decisively by Thomas Moore's 'Paradise and the Peri' in Lalla Rookh (1817). Skeat's entry, which Nourai cites, reads 'Peri, a fairy. (Pers.) Pers. parī, a fairy. Lit. \\\"winged;\\\" from Pers. par, a wing, feather. (√PAT.)'. Skeat's derivation of parī from par 'wing' is a folk etymology — Lokotsch repeats it as a guess ('vielleicht Weiterbildung von pers. pärr \\\"Flügel\\\" ... also etwa \\\"geflügelt\\\"') — and is excluded by the Avestan and Pahlavi evidence (pairikā-, parīk); Bartholomae, Horn and Nyberg all give the pairikā- descent instead. Lokotsch also warns that English fairy, despite the identical meaning, has nothing to do with peri (it is from OFr. faerie < Lat. fata). Nourai's arrow Persian > English is thus right; only the transmission through Turkish is left out.\",\n          \"derivation_fa\": \"واژهٔ انگلیسیِ peri وام‌واژه‌ای ادبی از «پری» فارسی است که بنا بر ویکی‌واژه از راه ترکی عثمانی peri وارد انگلیسی شده و با شعر «بهشت و پری» از توماس مور در «لالا رُخ» (۱۸۱۷) رواج یافته است. اسکیت که نورایی به او ارجاع می‌دهد می‌نویسد: «Peri, a fairy. (Pers.) Pers. parī, a fairy. Lit. \\\"winged\\\"; from Pers. par, a wing». اما اشتقاق parī از «پر» ریشه‌شناسی عامیانه است ــ لوکوچ نیز آن را تنها به گمان می‌آورد ــ و شواهد اوستایی و پهلوی (pairikā-، parīk) آن را رد می‌کنند. لوکوچ همچنین هشدار می‌دهد که fairy انگلیسی با آنکه هم‌معناست هیچ پیوندی با peri ندارد و از faerie فرانسهٔ کهن و fata لاتینی است. پس پیکان «فارسی ← انگلیسی» درست است و تنها واسطهٔ ترکی از قلم افتاده.\",\n          \"sources\": [W_PERI, W_PARI],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1158\", \"status\": \"supports\", \"note\": \"Klein (refs/KLN_1966.txt line 28143): 'peri, n., an imaginary sprite, a fairy. — Pers. pari, \\\"angel, fairy, genius\\\". See Pallas.' Exactly Nourai's arrow, and Klein's cross-reference to Pallas is why Nourai's chart joins the two branches.\"},\n            {\"ref\": \"SKT:384\", \"status\": \"partial\", \"note\": \"Skeat's entry is real but on p.348, not 384 (refs/SKT.txt leaf 368; leaf = printed + 20): 'Perl [=Peri], a fairy. (Pers.) Pers. parī, a fairy. Lit. \\\"winged;\\\" from Pers. par, a wing, feather. (√PAT.)' — the borrowing is confirmed, the internal Persian etymology is not (see derivation). Skeat's p.384 is the 'Pungent/Pure' spread; his appendix list of Persian-origin words, which also includes peri, is on p.619.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. peri\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n            {\"src\": \"SKT\", \"where\": \"p.348 s.v. Peri\", \"stance\": \"partial\", \"note\": \"See ref_check; borrowing right, inner etymology wrong.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1618\", \"stance\": \"supports\", \"note\": \"'\\\"Guter Genius\\\" [Horn NpEt S. 69, Nr. 310 ...]; hieraus sp. peri, frz. péri; engl. peri [womit natürlich trotz der gleichen Bedeutung fairy < frz. féerie < lat. fatum nichts zu tun hat], dtsch. Peri \\\"gute Fee\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Semitic\",\n          \"words\": \"\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"An empty pass-through box whose function is to hang the Arabic Bilqīs off the Indo-European root — and that is precisely the step no source supports, including the one Nourai cites for the box below it. Klein, s.v. Pallas, groups Gk. Pallas/pallax/pallakis, Lat. paelex, Av. pairikā, Heb. pileghesh, Aram. pilaqtā 'concubine' and Arab. Bilqīs, and then says: 'All these words are certainly related, but it is difficult to establish the degree of their relationship to one another. The above cited I.-E. words are POSSIBLY SEM. LOAN WORDS.' In other words Klein's tentative direction is Semitic > Indo-European, the reverse of the arrow drawn here. Ernout-Meillet, s.v. paelex, agree: 'Sans doute emprunté à une langue non i.-e. Outre le gr. πάλλαξ, on rapproche l'hébreu pileges \\\"maîtresse\\\".' No modern authority derives a Semitic word from Iranian *parikā-, and Pokorny's p.789 lemma contains no Semitic material at all. The box should be an arrow pointing the other way, or no arrow at all.\",\n          \"derivation_fa\": \"این جعبهٔ تهی تنها برای آن است که «بلقیس» عربی را به ریشهٔ هندواروپایی بیاویزد ــ و همین گام است که هیچ منبعی، حتی منبعی که خودِ نورایی برای جعبهٔ زیرین آورده، تأیید نمی‌کند. کلاین در مدخل Pallas واژه‌های یونانی Pallas/pallax/pallakis، لاتینی paelex، اوستایی pairikā، عبری pileghesh، آرامی pilaqtā «کنیزک» و عربی Bilqīs را کنار هم می‌نهد و می‌افزاید: «همهٔ این واژه‌ها بی‌گمان با هم خویشاوندند اما تعیین درجهٔ خویشاوندی دشوار است؛ واژه‌های هندواروپاییِ یادشده احتمالاً وام‌واژه‌های سامی‌اند». یعنی جهتِ احتمالیِ کلاین «سامی ← هندواروپایی» است، درست وارونهٔ پیکان این نمودار. ارنو ـ مه‌یه نیز در مدخل paelex همین را می‌گویند. هیچ پژوهشگر امروزی واژه‌ای سامی را از *parikā ایرانی نمی‌گیرد و در صفحهٔ ۷۸۹ پوکورنی هیچ مادّهٔ سامی نیست. پژوهش امروزی این حلقه را رد می‌کند.\",\n          \"sources\": [W_PALLAX],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai attaches no reference to this box; the only reference on the branch is the KLN:1115 of the Arabic box below, which as quoted says the opposite.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Pallas\", \"stance\": \"contradicts\", \"note\": \"'All these words are certainly related, but it is difficult to establish the degree of their relationship to one another. The above cited I.-E. words are possibly Sem. loan words. See Gesenius-Buhl, HWAT., p. 642, and Ludwig Koehler, Lexicon in Veteris Testamenti Libros, p. 761.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. paelex, p.840\", \"stance\": \"contradicts\", \"note\": \"'Sans doute emprunté à une langue non i.-e. Outre le gr. πάλλαξ, on rapproche l'hébreu pileges \\\"maîtresse\\\".' The IE words are the borrowers, not the lenders.\"},\n            {\"src\": \"POK\", \"where\": \"p.789 s.v. parika\", \"stance\": \"silent\", \"note\": \"'Note: only Iran. and Irish' — no Semitic branch is recognised.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Arabic\",\n          \"words\": \"Bilqîs\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Bilqīs (بلقيس) is the name Islamic exegesis gave to the unnamed Queen of Sheba of Qur'an 27:20-44; it is absent from the Qur'an itself and first appears in Arabic sources from the 9th century (Ṭabarī, Zamakhsharī, Bayḍāwī). The dominant modern explanation, going back to W. Montgomery Watt and accepted in the Encyclopaedia of Islam, is that Bilqīs is a distortion of Greek παλλακίς (pallakís) 'concubine' or of its Hebrew counterpart פילגש pilegeš — the queen having been remembered in Jewish and Christian legend as Solomon's concubine, the appellative was mistaken for a name. Competing suggestions derive it from the Arabic root b-l-q (whiteness, brightness) or from an Arabicised South Arabian title. What no one proposes is Nourai's route, a descent from an Indo-European/Iranian *parikā- through an unspecified 'Semitic' stage. Klein, the reference cited, mentions 'Arab. Bilqīs, name of the queen of Sheba' in his Pallas nest but expressly declines to specify the relationship, and the chart's own NOTE concedes this. Note that if Bilqīs really is from παλλακίς, then it is connected to the Greek box of this same chart — but as a borrowing FROM Greek, not as a sister of it under an IE root.\",\n          \"derivation_fa\": \"«بلقیس» نامی است که تفسیر اسلامی به ملکهٔ بی‌نامِ سبا در قرآن (نمل ۲۰–۴۴) داده است؛ این نام در خودِ قرآن نیست و از سدهٔ سوم هجری در منابع عربی (طبری، زمخشری، بیضاوی) پیدا می‌شود. توضیح رایج امروزی که به مونتگمری وات بازمی‌گردد و در دائرةالمعارف اسلام پذیرفته شده این است که «بلقیس» تحریفِ یونانیِ παλλακίς «کنیزک، مُتعه» یا معادل عبری آن פילגש (pilegeš) است: در افسانه‌های یهودی و مسیحی ملکهٔ سبا را زنِ صیغه‌ای سلیمان می‌دانستند و این صفت بعدها اسم خاص انگاشته شد. دهخدا نیز همین را نقل می‌کند. فرض‌های رقیب آن را از ریشهٔ عربی ب‑ل‑ق (سپیدی) یا از لقبی سبئیِ معرّب می‌گیرند. اما هیچ‌کس راهی را که نورایی رسم کرده ــ فروآمدن از *parikā هندواروپایی/ایرانی از راه گامی نامعیّن به نام «سامی» ــ پیشنهاد نکرده است. کلاین هم که مأخذ اوست تنها نام را در کنار Pallas می‌آورد و از تعیین نسبت سر باز می‌زند، چنانکه یادداشت خودِ نمودار اذعان دارد. پژوهش امروزی این حلقه را رد می‌کند.\",\n          \"sources\": [WP_SHEBA, A_BELQIS, W_PALLAX],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1115\", \"status\": \"partial\", \"note\": \"Klein s.v. Pallas does name 'Arab. Bilqīs, name of the queen of Sheba' among the words he groups with Gk. Pallas and Av. pairikā, but adds 'it is difficult to establish the degree of their relationship' and that the IE words may be the borrowers. So Klein supports an association, not the descent Nourai draws. Nourai's own NOTE ('KLN links this word to the other words in the chart but does not provide details') is an accurate report of the reference.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\", \"note\": \"grep 'Bilqis|Sheba|Saba' in refs/FVQ.txt returns only the Sabaean/Saba' place-name discussions; Bilqīs has no entry, as expected since the name does not occur in the Qur'an.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. Pallas\", \"stance\": \"partial\", \"note\": \"See ref_check.\"},\n            {\"src\": \"MON\", \"where\": \"Dehkhoda/Mo'in via abadis.ir s.v. بلقیس\", \"stance\": \"partial\", \"note\": \"The Persian dictionaries report that 'the true origin of the name Bilqis is not definitively known', and list Greek pallakhis 'concubine', a Greek instrument name, and an Avestan pairikā theory, concluding that the word entered Hebrew and thence Arabic as Bilqīs — i.e. Nourai's link is one of several rival guesses recorded there, not the accepted one.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"Belqîs «بلقیس»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"As a step in itself this arrow is unimpeachable: Persian بلقیس Belqīs is the Arabic name Bilqīs taken over unchanged in spelling, with the ordinary Persian reading of a short a/i in the first syllable as e (Belqīs), and it entered Persian with the Qur'anic story of Solomon and the Queen of Sheba, through tafsīr and qiṣaṣ al-anbiyāʾ literature from the 4th/10th century onwards. It is a proper name, not a common noun, and it belongs to the large class of Persian religious vocabulary borrowed from Arabic. The Rumi couplet the book quotes ('همچو آن هدیه که بلقیس از سبا / بر سلیمان می‌فرستاد ای کیا', Masnavi) is a good illustration of its currency in classical Persian. What remains disputed is not this step but the two above it (nodes #5 and #6).\",\n          \"derivation_fa\": \"این حلقه به‌تنهایی بی‌اشکال است: «بلقیس» فارسی همان نام عربی Bilqīs است که بی‌هیچ دگرگونی در املا وام گرفته شده و تنها واکهٔ نخست در خوانش فارسی به «ـِ» بدل شده است. این نام همراه با داستان قرآنیِ سلیمان و ملکهٔ سبا و از راه ادب تفسیر و قصص‌الانبیا از سدهٔ چهارم هجری به فارسی راه یافته و از شمار وام‌واژه‌های دینیِ عربی در فارسی است. بیت مولوی که کتاب آورده («همچو آن هدیه که بلقیس از سبا / بر سلیمان می‌فرستاد ای کیا») گواه رواج آن در ادب کلاسیک است. آنچه محل مناقشه است این حلقه نیست، بلکه دو حلقهٔ بالای آن (گره‌های ۵ و ۶) است.\",\n          \"sources\": [A_BELQIS, WP_SHEBA],\n          \"ref_check\": [\n            {\"ref\": \"MON5:277\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 is the a'lam (proper-names) volume; only the two-volume Adena abridgement is on disk and it omits the a'lam volumes (grep 'بلقیس' in MON_part1/2 and the Adena djvu returns nothing), and vajehyab/abadis reproduce only the lexicon volumes. The entry could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir s.v. بلقیس (Dehkhoda + Mo'in sections)\", \"stance\": \"supports\", \"note\": \"'بلقیس دختر هدهاد بن شرحبیل، از قبیلهٔ یعفر بن سکسک، از حمیر' — queen of Saba in Yemen, contemporary of Solomon; the Persian lexica carry the name exactly as Nourai's box has it.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery\", \"stance\": \"silent\", \"note\": \"no entry (the name is post-Qur'anic).\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Greek\",\n          \"words\": \"pallas; Pallas\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two words are packed into this box. (a) πάλλαξ (pállax) 'youth, girl', with παλλακή/παλλακίς 'concubine': these are real Greek words, but Beekes (EDG 2010, p.1147, followed by Wiktionary) makes πάλλαξ a back-formation from παλλακή, and παλλακή itself is not inherited — Ernout-Meillet, discussing its Latin counterpart paelex, judge the group 'sans doute emprunté à une langue non i.-e.' and compare Hebrew pilegeš. (b) Παλλάς, the epithet of Athena which Klein glosses 'lit. maiden': Wiktionary and the standard handbooks derive it rather from πάλλω 'to brandish', i.e. 'she who brandishes (the spear)', and Nourai's gloss 'a Greek goddess protecting Troy' is in any case off — the Palladion protected Troy, but Athena Pallas was famously Troy's enemy in the Iliad and the patron of the Greeks; what the Trojans kept was her image. The connection with Iranian pairikā/parī that the chart draws is the 1927 Walde-Pokorny position (Bd. II p.7, where Av. pairikā stands under the same lemma as παλλακίς, πάλλαξ and Παλλάς) — Pokorny 1959, the reference Nourai actually cites for the root, dropped it and confined *parika- to Iranian and Irish. Modern Greek etymology (Beekes) knows nothing of an Iranian source.\",\n          \"derivation_fa\": \"در این جعبه دو واژه درهم آمده است. نخست πάλλαξ «جوان، دختر» و παλλακή/παλλακίς «کنیزک، متعه»: این‌ها واژه‌های واقعی یونانی‌اند اما بیکس (فرهنگ ریشه‌شناختی یونانی ۲۰۱۰، ص ۱۱۴۷) πάλλαξ را ساختِ پس‌گشته از παλλακή می‌داند و خودِ παλλακή را ارثی نمی‌شمارد؛ ارنو ـ مه‌یه نیز در بحث از paelex لاتینی این گروه را «بی‌گمان وام از زبانی غیرهندواروپایی» می‌دانند و با pilegeš عبری می‌سنجند. دوم Παλλάς لقب آتنا که کلاین آن را «دوشیزه» معنی می‌کند؛ ویکی‌واژه و کتاب‌های مرجع آن را از πάλλω «به اهتزاز درآوردن (نیزه)» می‌گیرند. افزون بر این، معنی‌ای که نورایی داده («ایزدبانوی یونانی نگهبان تروا») نادرست است: در ایلیاد آتنا دشمن تروا و پشتیبان یونانیان است؛ آنچه از تروا نگهبانی می‌کرد پیکرهٔ او (پالادیوم) بود. پیوندی هم که نمودار میان این واژه‌ها و pairikā ایرانی می‌کشد از آنِ والده ـ پوکورنیِ ۱۹۲۷ (جلد دوم ص ۷) است؛ پوکورنیِ ۱۹۵۹ ــ همان مأخذی که نورایی برای ریشه آورده ــ آن را کنار گذاشت. پژوهش امروزی این حلقه را رد می‌کند.\",\n          \"sources\": [W_PALLAX, W_PALLAS],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1115\", \"status\": \"supports\", \"note\": \"Klein s.v. Pallas: 'L. Pallas, gen. Palladis, fr. Gk. Παλλάς, gen. Παλλάδος, lit. \\\"maiden\\\" (whence παλλάδιον, \\\"statue of Pallas\\\"), which is rel. to παλλακή, παλλακίς, \\\"concubine\\\". Gk. πάλλαξ, gen. πάλλακος, \\\"youth, girl\\\", is prob. a back formation fr. παλλακή or παλλακίς. ... Cp. Avestic pairika ... Cp. also Heb. pileghesh, Aram. pilaqtā, \\\"concubine\\\", and Arab. Bilqīs...' — Klein does say what Nourai's box says; it is Klein's grouping that modern Greek etymology rejects.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p.7\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny put 'gr. παλλακίς, παλλακή \\\"Beischläferin, Kebsweib\\\" ... πάλλαξ ... Παλλάς Beiwort der Athene' under the same lemma as Av. pairikā — the 1927 grouping Nourai follows.\"},\n            {\"src\": \"POK\", \"where\": \"p.789 s.v. parika\", \"stance\": \"contradicts\", \"note\": \"'Note: only Iran. and Irish' — the Greek material has been removed from the lemma Nourai cites.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. paelex, p.840\", \"stance\": \"partial\", \"note\": \"'Correspond à gr. πάλλας, παλλακή ... Sans doute emprunté à une langue non i.-e. ... Selon M. Niedermann, Vox Roman. 1940, p.106, l'emprunt aurait eu lieu à une date antérieure à la rupture de l'unité i.-e. puisque des correspondants des termes latin et grec sont fournis par l'avest. pairikā ... et par irl. airech ... \\\"concubine\\\".' The comparison exists but is framed as a shared loan from a non-IE source, not as inheritance from an IE root.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"An empty relay box. The Latin step is real: Latin took over Παλλάς as Pallas, gen. Palladis, and παλλάδιον as palladium 'the image of Pallas Athena in the citadel of Troy, on whose safekeeping the city's safety depended' (Klein s.v. palladium; Etymonline dates the English word to c. 1600, via Old French palladion). Latin also has the independently borrowed paelex 'concubine' beside Gk. πάλλαξ. So as a transmission link Greek > Latin > English the box is correct; it is only the parentage of the Greek box above it (node #8) that is disputed, which is why this is plausible rather than confirmed.\",\n          \"derivation_fa\": \"این جعبهٔ تهی تنها حلقهٔ واسطه است و گامِ لاتینی آن واقعی است: لاتینی Παλλάς را به صورت Pallas, -adis و παλλάδιον را به صورت palladium «پیکرهٔ آتنا در ارگ تروا که ایمنی شهر بدان بسته بود» وام گرفته است (کلاین، مدخل palladium؛ اتیمآنلاین واژهٔ انگلیسی را حدود ۱۶۰۰ از طریق فرانسهٔ کهن palladion می‌داند). در لاتینی paelex «کنیزک» نیز جداگانه در کنار πάλλαξ یونانی هست. پس حلقهٔ «یونانی ← لاتینی ← انگلیسی» درست است و تنها تبارِ جعبهٔ یونانیِ بالای آن (گره ۸) محل مناقشه است؛ از این رو این حلقه با احتیاط پذیرفتنی است.\",\n          \"sources\": [E_PALL],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1115\", \"status\": \"supports\", \"note\": \"Klein s.v. palladium (1): 'L., fr. Gk. παλλάδιον, \\\"statue of Pallas\\\", dimin. formed fr. Παλλάς, gen. Παλλάδος, a surname of the goddess Athene'; and s.v. Pallas: 'L. Pallas, gen. Palladis, fr. Gk. Παλλάς'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. paelex, p.840\", \"stance\": \"partial\", \"note\": \"Latin paelex 'maîtresse d'un homme marié, concubine' corresponds to Gk. παλλακίς; 'Non roman. Sans doute emprunté à une langue non i.-e.'\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. Paelignian\", \"stance\": \"supports\", \"note\": \"'L. Paelignī ... a name prob. rel. to paelex, \\\"concubine\\\", and cogn. with Gk. πάλλαξ, \\\"boy; girl\\\", παλλακή, παλλακίς, \\\"concubine\\\", πάλλας, \\\"virgin, maiden\\\"; see Pallas.'\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"palladium\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English has two words palladium and the chart's gloss picks the second. (1) palladium 'the sacred image of Pallas Athena in Troy', c. 1600, from Old French palladion < Latin palladium < Gk. παλλάδιον — that one really is the Latin word handed down, and Klein's cited page has it. (2) palladium the chemical element (Pd), which is NOT inherited from Latin at all: it is a Modern Latin coinage made in 1803 by William Hyde Wollaston, who named his new metal after the asteroid Pallas discovered the year before by H. W. M. Olbers, itself named for the goddess. Klein says exactly this ('ModL., coined by its discoverer ... in 1803 fr. Pallas, name of an asteroid discovered ... in 1802, and called after the goddess Pallas Athene'), and Etymonline agrees. So the arrow 'Latin > English palladium (a metallic element)' compresses a nineteenth-century learned coinage into an inherited descent; the ultimate name-giver is the goddess, but the route is Wollaston's neologism, not transmission through Latin and French.\",\n          \"derivation_fa\": \"در انگلیسی دو واژهٔ palladium هست و معنایی که نمودار داده به دومی مربوط است. نخست palladium «پیکرهٔ مقدس آتنا در تروا»، حدود سال ۱۶۰۰، از palladion فرانسهٔ کهن و palladium لاتینی و παλλάδιον یونانی ــ این یکی به‌راستی همان واژهٔ لاتینی است. دوم palladium نام عنصر شیمیایی (Pd) که هیچ از لاتینی به ارث نرسیده، بلکه واژه‌سازی لاتینیِ نو است: ویلیام هاید ولاستون در ۱۸۰۳ فلز تازه‌اش را به نام سیارکِ Pallas نامید که اُلبرس سالی پیش‌تر کشف کرده و آن را از نام ایزدبانو گرفته بود. کلاین دقیقاً همین را می‌گوید و اتیمآنلاین نیز. بنابراین پیکانِ «لاتینی ← انگلیسی palladium (عنصر فلزی)» یک واژه‌سازی سدهٔ نوزدهمی را به شکل توارث زبانی نشان داده است؛ نام‌گذارِ نهایی همان ایزدبانوست، اما راهِ آن نوواژهٔ ولاستون است نه گذر از لاتینی و فرانسوی. با احتیاط پذیرفتنی است.\",\n          \"sources\": [E_PALL],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1115\", \"status\": \"partial\", \"note\": \"Klein has both entries on the cited page: 'palladium, n., an image of Pallas Athene on the custody of which depended the safety of the city of Troy. — L., fr. Gk. παλλάδιον' and 'palladium, n., name of a metallic element. — ModL., coined by its discoverer the English chemist William Hyde Wollaston (1766-1828) in 1803 fr. Pallas, name of an asteroid discovered by ... Olbers (1758-1840) in 1802, and called after the goddess Pallas Athene.' Klein supports the connection to Pallas but makes the element a 1803 ModL coinage, not a Latin inheritance.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. palladium (both entries)\", \"stance\": \"partial\", \"note\": \"See ref_check.\"},\n            {\"src\": \"WEB\", \"where\": \"grep 'palladium' in refs/WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"nothing usable recovered from the OCR.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-381.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write381.py",
 "description": "Write verification JSON for page 381"
}
```


### [2026-09-07T20:54:54.218Z] TOOL RESULT

```
written
```


## [2026-09-07T20:54:59.266Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-381.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 381",
 "description": "Validate and run verify_check"
}
```


### [2026-09-07T20:55:00.615Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 8, 'transcription_suspect': 2, 'plausible': 4, 'disputed': 3}
root verdicts: {'plausible': 2}
ref checks: {'supports': 12, 'partial': 9, 'not_checked': 3, 'contradicts': 1}
books consulted: {'supports': 19, 'silent': 10, 'contradicts': 6, 'partial': 12} | by book: {'HUB': 5, 'LKT': 5, 'LAT': 5, 'KLN': 5, 'SYN': 4, 'PHD': 2, 'NYB': 2, 'HRN': 2, 'BQT': 2, 'WEB': 2, 'SKT': 2, 'WLD': 2, 'POK': 2, 'FVQ': 2, 'MON': 2, 'AFA': 1, 'BRT': 1, 'ARY': 1}
```


## [2026-09-07T20:55:18.809Z] AGENT

Page 381 (book p. 351) verified: 2 entries, 17 nodes, 0 PROBLEM lines from `verify_check.py`.

**Counts** — roots: 2 plausible. Nodes: 8 confirmed, 4 plausible, 3 disputed, 2 transcription_suspect. Ref checks: 12 supports / 9 partial / 1 contradicts / 3 not_checked. 18 books consulted.

**transcription_suspect / disputed items**

- *Pambak* #3 Greek `bombax` — **transcription_suspect, error in the book.** Greek is βάμβαξ/πάμβαξ (+ βαμβάκιον); `bombax` is Late Latin, as Buck's own p.402 (the page Nourai cites for the root) and Ernout-Meillet s.v. *bombyx* both say. Gloss "silk cotton" is taken from the botanical genus *Bombax*.
- *Pambak* #7 `Aramaic bambak` — **transcription_suspect, error in the book.** Buck p.402 reads "Arm. bambak" = **Armenian**; Hübschmann (PSt p.255) lists *bambak* among Armenian loans from Phl. *pambak*. Syriac has a different form (*palbaḡ*). Nourai expanded "Arm." as Aramaic.
- *Parîkâ* #5 `[Semitic]` (empty relay) — **disputed.** Klein, the only reference on the branch, says the IE words are "possibly Sem. loan words" — the reverse of the arrow drawn.
- *Parîkâ* #6 Arabic `Bilqîs` — **disputed.** Modern view (Watt, EI, Wikipedia, Dehkhoda): from Gk. παλλακίς / Heb. *pilegeš* 'concubine', a 9th-c. exegetical name; no descent from Iranian *parikā-.
- *Parîkâ* #8 Greek `pallas / Pallas` — **disputed.** Beekes makes πάλλαξ a back-formation of παλλακή (non-IE loan); Παλλάς is from πάλλω 'brandish'. Also the gloss is wrong: Athena Pallas was Troy's *enemy*; the Palladion protected Troy.

**Extraction errors for the owner: none.** The printed page 351 (image saved to `data/verification/sources/refs/ocr/BOOK/381.png`) matches the JSON exactly, including "Greek bombax" and "Aramaic bambak".

**Useful finding on the second root:** Nourai's whole *Parîkâ* chart (Iranian + Greek + Semitic in one tree) is the **Walde-Pokorny II 7** lemma `pallā-q-, pali-q-` of 1927, not Pokorny 1959 — POK:789 does have `parika` "concubine" but flags it "only Iranian and Irish" and contains no Greek or Semitic material. Ref-page notes: SKT:384 for *Peri* is actually Skeat p.348; BQT:864 (second number for پری) could not be located (vol. 2 range, wrong alphabet section); MON5:277 unreadable (Mo'in vol. 5 *aʿlām* not available in any local or online copy).
