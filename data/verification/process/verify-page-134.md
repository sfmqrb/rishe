# Verification process log — verify-page-134


## [2026-09-05T20:07:13.922Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 134 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-134.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-134.json. Write /home/sfmqrb/git/rishe/data/verification/page-134.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 134` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:07:15.581Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:07:16.271Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:07:16.284Z] TOOL RESULT

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


## [2026-09-05T20:07:16.638Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-134.txt"
}
```


### [2026-09-05T20:07:16.653Z] TOOL RESULT

```
1	=== PDF page 134 (book page 104) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dhogh, Dhegh : to heat, burn  (refs POK:240)
4	#1 (parent #0) [Avestan] refs=POK:240; BQT:815, 827 | dağa, dâğah : hot ; daxša : burnt ; daxma : place for burning the dead
5	  #2 (parent #1) [Persian] refs=FSF:173 | dâğ «داغ» : hot ; daxš 2 «دخش ۲» : dark ; daxmeh «دخمه» : tomb
6	  #3 (parent #1) [Avestan] refs=AHM:181,192 | daxš 2, rax, rak : to hurt (burn) ; fra-daxšanâ : a device to hurt or strike from a distance, sling ☞Per 1
7	    #4 (parent #3) [Persian] refs=AHM:192; MON:2564 | falâxon «فلاخن ( فلاخان ، فلخمان ، فلخم )» : sling
8	#5 (parent #0) [Sogdian] refs=SOD:139 | dğm`y : grove
9	#6 (parent #0) [Avestan] refs=NYB:217; KLN:404 | dažaiti : to burn ; vi-dâz : to melt ☞Wi
10	  #7 (parent #6) [Persian] refs=MON:3199; BQT:1777 | godâzîdan «گدازیدن ( جانگداز )» : to burn, melt | NOTE: Compare with derivations from root "Teku 1:to flow, run"
11	#8 (parent #0) [Latin] refs=AHD | febris : fever
12	  #9 (parent #8) [English] refs=None | fever
13	#10 (parent #0) [Germanic] refs=KLN:404 | dagaz : day
14	  #11 (parent #10) [English] refs=None | day, dawn
15	#12 (parent #0) [Indo-European] refs=IEC:379,407; POK:399 | Geulo, Ğuěl, Ğul, Guheguh : coal
16	  #13 (parent #12) [Avestan] refs=HRN:163; BQT:1150; IEC:379,407 | skarana, skairya : coal
17	    #14 (parent #13) [Persian] refs=BQT:1026,1150; HRN:163; MON | sekâr «سکار ( شگار )» : coal ; zoğâl «ذغال ( زغال ، ژگال ، زگال )» : coal ; sekârŭ «سکارو ، سکاروا ، سکالو» : cooked on charcoal ; sekâr âhanj «سکار آهنج» : iron tool for barbecuing
18	  #15 (parent #12) [Germanic] refs=POK:399; IEC:407 | chol, kolo, kolam : coal
19	    #16 (parent #15) [English] refs=AHD | coal
20	
```


## [2026-09-05T20:07:20.385Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-134.json",
 "description": "Read source JSON for page 134"
}
```


### [2026-09-05T20:07:20.426Z] TOOL RESULT

```
{
  "pdf_page": 134,
  "book_page": 104,
  "entries": [
    {
      "root": {
        "name": "Dhogh, Dhegh",
        "lang": "Indo-European",
        "refs": "POK:240",
        "gloss": "to heat, burn"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:240; BQT:815, 827",
          "words": [
            {"translit": "dağa, dâğah", "gloss": "hot", "script": null},
            {"translit": "daxša", "gloss": "burnt", "script": null},
            {"translit": "daxma", "gloss": "place for burning the dead", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FSF:173",
          "words": [
            {"translit": "dâğ", "gloss": "hot", "script": "داغ"},
            {"translit": "daxš 2", "gloss": "dark", "script": "دخش ۲"},
            {"translit": "daxmeh", "gloss": "tomb", "script": "دخمه"}
          ],
          "note": null,
          "quote": {
            "text": "گناهش به یزدان بخشنده بخش - مکن روز بر دشمن ودوست دخش",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan",
          "refs": "AHM:181,192",
          "words": [
            {"translit": "daxš 2, rax, rak", "gloss": "to hurt (burn)", "script": null},
            {"translit": "fra-daxšanâ", "gloss": "a device to hurt or strike from a distance, sling", "script": null, "see": ["Per 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "AHM:192; MON:2564",
          "words": [
            {"translit": "falâxon", "gloss": "sling", "script": "فلاخن ( فلاخان ، فلخمان ، فلخم )"}
          ],
          "note": null,
          "quote": {
            "text": "کرکس بودی که زی توام افکندی - خویشتن اندر نهادمی بفلاخن",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:139",
          "words": [
            {"translit": "dğm`y", "gloss": "grove", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "NYB:217; KLN:404",
          "words": [
            {"translit": "dažaiti", "gloss": "to burn", "script": null},
            {"translit": "vi-dâz", "gloss": "to melt", "script": null, "see": ["Wi"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:3199; BQT:1777",
          "words": [
            {"translit": "godâzîdan", "gloss": "to burn, melt", "script": "گدازیدن ( جانگداز )"}
          ],
          "note": "Compare with derivations from root \"Teku 1:to flow, run\"",
          "quote": {
            "text": "ای مجلسیان سوز دل حافظ مسکین - از شمع بپرسید که در سوز و گداز است",
            "poet": "Hâfez"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "febris", "gloss": "fever", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "fever", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:404",
          "words": [
            {"translit": "dagaz", "gloss": "day", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "day, dawn", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "IEC:379,407; POK:399",
          "words": [
            {"translit": "Geulo, Ğuěl, Ğul, Guheguh", "gloss": "coal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Avestan",
          "refs": "HRN:163; BQT:1150; IEC:379,407",
          "words": [
            {"translit": "skarana, skairya", "gloss": "coal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "BQT:1026,1150; HRN:163; MON",
          "words": [
            {"translit": "sekâr", "gloss": "coal", "script": "سکار ( شگار )"},
            {"translit": "zoğâl", "gloss": "coal", "script": "ذغال ( زغال ، ژگال ، زگال )"},
            {"translit": "sekârŭ", "gloss": "cooked on charcoal", "script": "سکارو ، سکاروا ، سکالو"},
            {"translit": "sekâr âhanj", "gloss": "iron tool for barbecuing", "script": "سکار آهنج"}
          ],
          "note": null,
          "quote": {
            "text": "بدار دنیا چو برفروخت آتش ظلم - سکار آن بجهنم همی خورد چو ظلیم",
            "poet": "Sŭzanî Samarqandî"
          }
        },
        {
          "id": 15,
          "parent": 12,
          "lang": "Germanic",
          "refs": "POK:399; IEC:407",
          "words": [
            {"translit": "chol, kolo, kolam", "gloss": "coal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "coal", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:07:20.428Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:07:20.464Z] TOOL RESULT

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


## [2026-09-05T20:07:38.747Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','FSF','AHM','MON','SOD','NYB','KLN','AHD','IEC','HRN','HUB','BRT','PHD','WLD','SKT','CHEUNG','ARY','SYN']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-05T20:07:39.324Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -60 data/verification/page-127.json"
}
```


### [2026-09-05T20:07:40.663Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

AHM {"title": "I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959", "edition_found": "1959", "kind": "archive_djvu", "url": "https://archive.org/details/gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "identifier": "gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt", "page_offset": "leaf = printed + 14 (e.g. leaf 18 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

CHEUNG null

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
```


### [2026-09-05T20:07:40.708Z] TOOL RESULT

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
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
---
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Dhem",
   "verdict": "confirmed",
   "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
   "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
   "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
   "sources": [
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
   ],
   "ref_check": [
    {
     "ref": "POK:247",
     "status": "supports",
     "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
     "stance": "supports",
     "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
     "stance": "supports",
     "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
     "stance": "silent",
     "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
    },
    {
     "src": "IEC",
     "where": "Mann, d-section (grep 'dhem' in IEC.txt)",
     "stance": "silent",
     "note": "Mann has dhen- (2) 'forehead', dhenguhó, dhinió etc. but no *dhem- 'blow, smoke' headword."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan",
     "words": "dam; da-dhmainya",
     "verdict": "plausible",
     "derivation": "The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, -blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit Inl.-Red.' and compares directly with 'ai. dhámati \"er bläst\", np. damīdan \"blasen\"'. Nourai's 'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam' is the root abstracted from that participle, i.e. Proto-Iranian *damH- 'to blow, breathe; to swell' (Cheung 2007 s.v. *damH³), which is real and is the ancestor of the Persian words in node 2; it is simply not an Avestan word-form. Hence plausible rather than confirmed: right root, misdescribed gloss, and one of the two 'words' is a root citation.",
     "derivation_fa": "در اوستا هیچ فعلِ صرف‌شدهٔ dam- «دمیدن» به‌جا نمانده است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۷۳۱ به بعد) تنها اسمِ فاعلِ جوان‌اوستاییِ daδmainiia- «باد کرده، خود را باد کننده» را می‌آورد که دربارهٔ قورباغه‌ها به کار رفته (وندیداد ۱۴٫۵ و ۱۸٫۷۳) و آن را ستاکِ حالِ پسوندِ -ainya- با تکرارِ درونی می‌داند و مستقیماً با «dhámati سنسکریت» و «دمیدنِ فارسی» می‌سنجد. صورتِ «da-dhmainya» در کتاب نورایی همان واژه است (او ذالِ اوستایی را dh می‌نویسد و هجای تکرارِ da- را با خط تیره جدا می‌کند)، پس خوانشِ کتاب درست است؛ اما معنایی که به آن داده («من می‌دمم») نادرست است، چون این صورت صفت/اسمِ فاعل است نه فعلِ اول‌شخص. «dam» هم واژهٔ اوستایی نیست بلکه ریشهٔ ایرانیِ باستانِ *damH- «دمیدن، باد کردن» است (چونگ، ذیل *damH³). بنابراین ریشه درست است ولی معنا و صورت‌بندیِ گره با احتیاط پذیرفتنی است.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86"
```


## [2026-09-05T20:07:47.197Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dheguh\\|dhegŭh\\|dhegʷh\\|dhegu̯h\\|dheguh-\" POK_01.txt | head -20; echo \"=== 240 leaf ===\"; awk 'BEGIN{RS=\"\\f\"} NR==248' POK_01.txt | head -80"
}
```


## [2026-09-05T20:07:47.453Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==407' POK_01.txt | head -90"
}
```


### [2026-09-05T20:07:48.996Z] TOOL RESULT

```
3411:gr.  d-emavog'  ä7tTÖ{,isvog  Hes.  (,angezündet';  =  lit.  degtinas  ,wer  oder was  zu  verbrennen  ist'),  tscpqä  , Asche'  (*dheguhra)]
3413:lat.  foveö,  -ere  ,wärraen,  hegen,  pflegen',  föculum  ,Feuerpfanne'  {^'foue- clom),  fömentum  ,ein  erwärmender  Umschlag'  {*fouementom)j  fömes,  -itis , Zunder'  (*fouemet-j  Bedeut.  wie  lett.  daglis),  favilla  , Asche,  bes.  noch glühende'  (wahrscheinlich  aus  *dhogi^h-lo-lä):  favöniiis  ,der  laue  Westwind' (aus  ^-fovönios)'^  febris  ,Fieber'  C^dheguhro-;  nach  Leumann  Gnom.  9,  226 ff. die  i-Flexion  nach  sitis).
3419:Tocb.  B  teki  .Krankheit'  (=  ir.  daig)'^  A  tsäk-,  B  tsak-  .brennen',  das i8  nach  dem  ablaut.  tsäk-  {*dheguh-)  .glänzen,  glühen';  AB  cok  , Lampe' (aus  .Kienfackel')  :  bsl.  *degut-  .Teer'  (s.  oben).
=== 240 leaf ===
tifex  bene-ficus  u.  dgl.;  zur  Bed.  von interficiö  ,töte'  (,*lasse  verschwinden')  vgl.  ai.  antar-hita-h  ,versch wunden'. Dieselbe  /c-Erw.  außer  in  gr.  eO^rjxa  auch  in  &rj'Ar]  , Behältnis',  ai.  dha- kd-h  , Behälter'  und  phryg.  ad-öayisv  ,afficit',  Med.  aö-öaxsTOQ]  ven.  vha^s&o ,fecit'  (*fak-s-to,  das  /  wohl  aus  dem  Ital.);  hitt.  dak-ki-es-zi  (dakkeszi) , macht,  stellt  hin'  (:  lat.  facessö),  dak-su-ul  (daksul)  , freundlich'  (:  alat. facul)]  vielleicht  toch.  A  täkä  ,ich  wurde',  B  takäwä  ds.  (anders  Pedersen Toch.  194);
gall.  dede  .posuit'j  vgl.  lat.  con-,   ab-,   cre-didi,   ahd.    teta   ,ich   tat';   air. -tarti  ,gibt'  {Ho-ro-ad-dit  aus  *dhe-t),  Perf.  do-rat  {*to-ro-ad-dat  aus  *dhd-t),     ■ Thurneysen  Gr.  35;
ahd.    töm,    tuom,   as.    tön,   ags.    dorn    ,tue',    Inf.    ahd.  tuoiij    as.   ags.  dön (*dhö-m)   ,tun',   Prät.  ahd.  teta   ,ich  tat'  (2.  Sg.  täti,  PI.  tätu-m;   nach  dem Typus  got.  setum  umgebildet),  as.  deda  (2.  Sg.  dedös,  3.  PI.  dädun,  dedun),   .v/ ags.  dyde  <  dudi  (s.  oben  zu  ai.  dadhäu);  Part.  Perf.  Pass.  ahd.  gi-tän,  ags.  ^' dön  ,getan'  aus  *dhe-no-  =  aksl.  o-dem  ,umgelegt,  bekleidet';  "
in    der  Endung   des    schwachen   Präter.  (got.    salbö-dedun   usw.)    pflegt man  meist    die    Wurzel    dhe-   zu    suchen,    hingegen    in    got.    kunpa   , er- kannte',   das   idg.    't'   enthalten   muß,    eine   andere   Bildung   anzunehmen.     - Vgl.  Hirt,  Idg.  Gr.  IV,  99,    Sverdrup  NTS.  2,  55  ff.,   Marstrander,  NTS. 4,  424 f.,  Specht  KZ.  62,  69  ff.,  Kretschmer  Sbb.  Wien,  225.  Bd.,  2.  Abb.,  6 f.
lit.  deti  ,legen,  stellen',  Präs.  2.  PL  alt  deste  (*dhe-dh-te),  Sg.  demi,  desie-s,      : dest{i)  (vgl.  Büga  Kalba  ir  s.  158,  213),  neugebildet  dedii]  lett.  det  (s.  oben);  ^
237
aksl.  cUti  , legen'  (auch  ,sag-en'),  Präs.  dezdo  (^dediö)  und  dej^  (s.  oben); lit^o,  dejatl  ..legen,  verrichten';  -va-Iterativ  caksl.  o-dcvatl  ,(uratun),  bekleiden'^ ••uss.  devdtb  , hinlegen,  tun,  setzen';
dcazu  wohl  lit.  deviit,  devett  , Kleider  anhaben';  ein  formantisches  u  auch in  gr.  *x^o/axog  und  (assim.)  '■^•d-aJ'ay.og,  vgl.  ^occ^w  ,sitze',  ion.  ^wxog  (hom. ^öcoyiog  für  ^6[J^]ccy,og  geschrieben)  ,Sitz',  d-aßamv  ^ä^ov  )]  S-qovov  Hes., att.  auch  ^äxog  ds.,  hom.  ^adaaco  , sitze',  att.  poet.  d'daao)  ds.  (s.zur  gr.  Gruppe Hechtel  Lexil.  161  f.,  Boisacq  335);  vgl.  auch  thrak.  -dava  , Siedlung'  aus *diieuä  oder  *dh9uä]  wohl  Umbildung  nach  dem  Nebeneinander  *dü-: *dou-  , geben';
hitt.  da-a-i  (däl)  ,setzt,  legt',  1.  Sg.  te-eh-hi  {tehlii\  3.  PI.  ti-an-zi  (Pe- dcrseu  Tlitt.  91,  112 f.,  166),  Prät.  3.  Sg.  da-a-is]  vielleicht  auch  dak-ki-eszi (s.  oben);
toch.  A  tä-,  täs-,  tas-^  B  tes-  .l
```


### [2026-09-05T20:07:50.817Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:07:57.682Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=3420{if(/\\f/)n++} END{print \"formfeeds before line 3420:\",n}' POK_01.txt; echo ---; sed -n '3395,3425p' POK_01.txt"
}
```


### [2026-09-05T20:07:59.484Z] TOOL RESULT

```
formfeeds before line 3420: 247
---
In  allen  Gliedern  etwas  zweifelhafte  Verbindung.  Über  air.  de'd(a). vgl.  Pedersen  KG.  II  504  f.  (von  einem  Perf.  *dhe-doue  aus  zu  got.  diwans , sterblich'?  s.  dheu-  , hinschwinden',  wo  auch  über  air.  dlth,  arm.  di).  Die germ.  Sippe  endlich  erinnert  z.  T.  an  die  unter  "^dheues-  ,stieben'  bespro- chene von  ndd.  dösig  und  könnte  nicht  bloß  in  der  5-Erw.,  sondern  auch in  der  Bed.  sich  z.  T.  nach  dieser  gerichtet  haben;  immerhin  ist  mit  einer alten  Verwandtschaft  von  anord.  dcesask  usw.  und  ir.  -deda  zu  rechnen.
WP.  I  829,  WH.  I  451.
dheb-  ,dick,  fest,  gedrungen'.
Ahd.  tajpfar  , gravis,  gravidus;  schwer^  gewichtig',  mhd.  tapfer  ,fest, gedrungen,  voll,  gewichtig,  bedeutend',  spät  ,tapfer  (fest  im  Kampfe)', ahd.  tapfare  ,mole',  tapfarl  f.  ,moles',  mnd.  dapper  , schwer,  gewichtig, gewaltig',  ndl.  dapper  , tapfer;  viel',  norw.  daper  ,trächtig',  anord.  dapr ,schwer,  schwermütig,  düster,  traurig'.
Vielleicht  an.  damrarj  nhd.  Damm,  mhd.  tarn  ds.,  got.  faurdamwjan ,verdämmen,  hindern',  als  dhobmö-  hierher?
Aksl.  deheh  ,dick',  russ.  mdartl.  dehelyj  , wohlbeleibt,  stark,  fest',  abl. dohölyj  ,stark,  kräftig'  (usw.,  s.  Berneker  182);  apr.  deblkan  ,groß';  viel- leicht auch  lett.  dabVs  u.  dähls  , üppig',  dahVi  audzis  , üppig  gewachsen', dahVigs  ,üppig'  (Berneker  aaO.;  nach  Mühlenbach-Endzelin  I  428  sind jedoch  die  lett.  Wörter  wahrscheinlich  mit  aksl.  dohrh  zu  verbinden);
toch.  A  tsopats  ,groß',  täppo  ,Mut',  tpär  ,hoch',  B  tappre,  täpr-  ds., Pedersen  Toch.  243,  Toch.  Sprachg.  23,  27,  29,  Van  Windekens  Lex.  135, 148.    Zweifelhaft.
WP.  I  850,  WH.  I  437.
240
dhebh-,  dbebh-eu-  ^beschädigen;  verkürzen,  betrügen',  die  nasalierten  Fori (*dhembh-)  sind  als  proportionale  Neubildungen  nach  -^i-haltigen  Wurzel zu  verstehen.
x-Vi.  dahhnöti , beschädigt,  versehrt,  betrügt,  Pass.  nimmt  Schaden'  (*dhebl n-eu-ti),  Perf.  daddbha  und  (geneuert)  daddmhha,  Partiz.  Perf.  Pass.  dahdl und  (von  der  Wurzelform  auf  -u:)  d-dhlm-ta-  Adj.  ,wunderbar',  eigentli( ,*der    Täuschung    unzugänglich,     unantastbar';     damhhdyati    ,macht   aj schänden'    {damhhd-h    ,Betrug'),    Desid.    dipsati   (=  av.   dhv^-.    s.   unten] dabhrd-  ,wenig,  gering,  dürftig';
av.  dab'  ,betrügen,   um   etwas   bringen' :  davqi-d-yä  G.  Sg.  f.  ,der  betrl genden',  davayeinü  N.  Sg.  f.  ,die  betrügende',   ddbdnaotä  2.  PI.  Präs.  (a *dbha7icm-mi,  idg.  *dbh-en-eumi'),  Inf.  diwiaidyäi  (ohne   desiderative  B( mehr,   aber  =  ai.   dipsa-ti),  Partiz.  Perf.  Pass.  dapta-  (Neuerung);  d^l vayat  ,er   soll   betören'   (Wzf.  *dbheu-)j   a-ddbaoman-  n.  ,Betürung';  oss3 dawin  , stehlen';   hitt.  te-ip-nu-  , gering  achten',  Pedersen  Hitt.  144.
Dazu  sehr  wahrscheinlich  gr.  äzcfißco  ,beschädige,  beraube,  verküra (dvi.i6v)y  verwirre,  täusche',  Pass.  ,bin  beraubt',  mit  d-  wohl  aus  *ä-,  *srri-xtm mit  demselben  Konsonantenverhältnis  wie  zwischen  nvvda^ :  ai.  budh-nd-\
WP.  I  850  f.,  Kuiper  Nasalpräs.  147,  Schwyzer  Gr.  Gr.  I  333.
dheg^h-  ^brennen';  Nominalbildungen  dti6g^ho-s,  dheg^h-ro-s.
Ai.  ddhati,  av.  dazaiti  , brennt'  (=  lit.  degü^  aksl.  zegg,  alb.  djek)^  Partiz. ai.  dagdhd-h  (=  lit.  degtas),  Kaus.  dähdyati]  däha-h  ,Brand,  Hitze',  nidagha-]^ , Hitze,  Sommer',  npers.  däy  , Brandmal'  (dazu  spätgr.  ödyalog,  -ig  ,rot- braunes  Pferd'?);  av.  daxsa-  m.  ,Brand';
gr.  d-emavog'  ä7tTÖ{,isvog  Hes.  (,angezündet';  =  lit.  degtinas  ,wer  oder was  zu  verbrennen  ist'),  tscpqä  , Asche'  (*dheguhra)]
alb.  djek  ,verbrenne,  brenne  an',  Kaus.  dhez,  n-dez  .zünde  an'  (Gdt *dhoguheiö  =  lat.  foveö)]
lat.  foveö,  -ere  ,wärraen,  hegen,  pflegen',  föculum  ,Feuerpfanne'  {^'foue- clom),  fömentum  ,ein  erwärmender  Umschlag'  {*fouementom)j  fömes,  -itis , Zunder'  (*fouemet-j  Bedeut.  wie  lett.  daglis),  favilla  , Asche,  bes.  noch glühende'  (wahrscheinlich  aus  *dhogi^h-lo-lä):  favöniiis  ,der  laue  Westwind' (aus  ^-fovönios)'^  febris  ,Fieber'  C^dheguhro-;  nach  Leumann  Gnom.  9,  226 ff. die  i-Flexion  nach  sitis).
Mir.  daig  (Gen.  dega)  ,Feuer,  Schmerz'  (aus  *degi-)]  über  mbret.  deuijf, nbret.  devi,  cjmr.  deißo  ,brennen'  s.  unter  *<^äw-, brennen';  cymr.  de ,brennend'; go-ddaith  ,Brand'  (aus  "^-dekto-)]  aber  air.  ded-öl  ,Morgengrauen'  nach Mai-strander  Dict.  Ir.  Lang.  I  213  eigentlich  .Abschiedstrunk,  letzter  Trunk'; nir.  dogha  ,Klette'  (:lit.  dagys  s.  unten);
über  got.  dags  ,Tag'  usw.  s.  unter  '^'ügher-  S.  7:
241
.  lit.  degu,  degt'i  .brennen'  (trans.  und  intrans.);  degtas  .gebrannt',  degtinas xras  25U  verbrennen  ist',  degüne  f.  .Branntwein',  ablautend  dagys,  dägis 'oistel'  (lett.  dadzis);  dägas  .das  Brennen;  Sonamerbitze;  Ernte',  dagä  .Ernte', ipr.  dagis  .Sommer';  lit.  däglas,  .brandfarben',  deglas^  .schwarzscbeckig-; lott.  daglas  f.  PI.  .Brandfleck',  daglis  .Zunder';  lit.  nuodegulis  .Feuer- brand'; degis  »Brandwunde';  ablaut.  atüo-dogiai(?)  m.  PI.  .Sommerweizen';
sloven.  djgniti  .brennen,  wärmen',  cech.  alt  dehna  .Teufel',  ablaut. Jahneti  .brennen';  russ.  degoth  .Teer'  (aus  .*harzreicbes  Holz'),  wie  lit. degtitas  .Birkenteer';  mit  Assimil.(?)  von  *degg  zu  "^gego:  aksl.  zegg,  zesti ^brennen',  ablaut.  >uss.  iz-gdga  .Sodbrennen'  (s.  Meillet  MSL.  14.  334  f., anders  Brugmann  II ^  3.  120).
Tocb.  B  teki  .Krankheit'  (=  ir.  daig)'^  A  tsäk-,  B  tsak-  .brennen',  das i8  nach  dem  ablaut.  tsäk-  {*dheguh-)  .glänzen,  glühen';  AB  cok  , Lampe' (aus  .Kienfackel')  :  bsl.  *degut-  .Teer'  (s.  oben).
WP  I  849  f.,  WH.  I  466  f..  469.  471  f..  864.  Trautmann  49.  Pedersen Tech.  Sprachg.  23.
äbS(i)'  (daneben  dh-ei-  ?)  .saugen,  säugen'  ( :  c?Äai-.  dJvt-  und  dhe-j  dhd-)  s. bes.  Schulze  KZ.  27.  425  =  Kl.  Sehr.  363.  Nominalbildungen:  dhe-lä .Mutterbrust',  dhi-lo-  , Zitze',  dbe-lu-  .säugend'.  dbQi-l-  ds.,  dhei-nä .trächtig',  dhe-nä  .Fruchtertrag',  dhedhn-  .(saure)  Milch'. Ai.  dhäya-h  .ernährend,  pflegend',  dhäyas-  n.  .das  Saugen',  dhäyü-  .durstig'. dhätave    .zu    saugen',    Fut.  dhäsyati,    i^or.    ddhät   ,er    sog',    su-dhä    .Saft, Nektar',  dhätrl  .x4mme.  Mutter',  dhenü-  f.  .milchend'  =  av.  daenu-  .Weib- chen von  vierfüßigen  Tieren',  ai.  dJiBnä  .Milchkuh',  ablaut.  dhud-  .gesogen*^, Perf.  Plur.  1.  3.  da-dhi-md  (i  =  »),    da-dh-üh]   redupl.   Nomen    da-dh-an-j Nom.  dd-dh-ij  Gen.  dadhnds  .saure  Milch'  (:  apr.  dadaUj  alb.  djathej'j
vom  Stamme  dhoi-:  dhdyati  .saugt'  (*dh^ieti  :  Kaus.  *dhoi-4ie-ti  in slav.  dojiti,  got.  daddjan)  und  dhinöti  .nährt';
arm.  diem  .sauge'  (^  =  idg.  e  oder  eher  l,  so  daß  =  anord.  dia),  stn-di ,(Brust  saugend  ==)  Säugling',  dal  aus  dail  ,Biestmilcli'  (dhdi-li-)^  dayeak ,Amme'  (von  *dayi-  =  idg.  dhd-ti-)]
gr.  d-TjoaTo  .er  sog',  d^rja^at  .melken',  ^rjVLOv  ,Milch',  TL&rjvrj  ,Amme' (Kurzform  zlrd-rj  u.  dgl.,  worüber  anders  Falk-Torp  u.  taute),  yaXad-rjvög .Milch  saugend'.  n-d-aGÖg  ,zahm,  kultiviert';
alb.  djathe  .Käse'  ursprüngl.  ,aus  saurer  Milcb  gemachter  Quark'  (:ai. dddJii),  gr.-alb.  dithe  ,Käse';
```


## [2026-09-05T20:08:14.402Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f: $(tr -cd '\\f' < $f | wc -c) pages, $(wc -l < $f) lines\"; done"
}
```


## [2026-09-05T20:08:15.462Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"geu-lo\\|ĝeu-lo\\|g'eu-lo\\|geulo\\|glühende  Kohle\\|glühende Kohle\" POK_01.txt POK_02.txt POK_full.txt | head -20"
}
```


### [2026-09-05T20:08:16.383Z] TOOL RESULT

```
POK_01.txt: 363 pages, 5151 lines
POK_02.txt: 433 pages, 6715 lines
POK_03.txt: 429 pages, 5974 lines
POK_full.txt: 0 pages, 93771 lines
```


### [2026-09-05T20:08:16.461Z] TOOL RESULT

```
POK_01.txt:1651:kelt.  helo-  ,leuchtend,  weiß^  in  cymr.  heleu  (*bheleuo-)  ,Marder^,  air. oibell  m.  ,Glut,  Hitze^  (f.  ,Funke,  glühende  Kohle^)  =  cymr.  ufel  m. ,Funke,  Feuer^  (^opi-bhelo-),  mir.  Bel-tene  ,Fest  des  1.  Mai^  (=  Leuchtfeuer), aall.  GN  {Apollo)  Belenos,  (^Minerva)  Belisama  (Superlat.),  FIN  Belenä  > frz.  Bienne,  Schweiz.  Biel]  afrz.  haille  ,Blässe^  (daraus  mbret.  baill  ds.) könnte  auf  ablaut.  gall.  *halio-  zurückgehen,  vgl.  frz.  ON  Bailleuil  < *BaUo-ialon-  gall.  heisa  ,Feld^  aus  *belisä',
POK_02.txt:682:(reü-,  g^^-f  S^-  ^biegen,  krümmen,  wölben^;  Nominalbildungen:  gudom ^Darm;  Eingeweide^;, ^uf-r  ^Kehle^  Hals^;,  gugä  ^Kugel,  Buckel,  geu-lo-s ^rundes  Gefäß,  KugeP,  gou-no-m  ^Gekräuseltes,  Gewölbtes^,  gupä ,Erdhöhle,  StalP,  geu-ro-s,  gou-ro-s  ^gekräuseltes  (Haar,  Welle)', gur-no-s  ,Rücken,  Hüfte',  gü-ro-s  ,rund,  gekrümmt'.
POK_02.txt:766:g[e)u-lo-  ,glühende  Kohle'.
POK_02.txt:768:ir.  güal  , Kohle'  (<  "^geulo-  oder  ^goulo-)]
POK_02.txt:771:arm.  krak  ,Feuer,  glühende  Kohlen'  (<  "^giiro-,  *gurä-),  krak-aran  ,Herd, Feuerbecken,  Glutpfanne'.
POK_02.txt:1271:'^ghlö-  (wie  in  gr.  xkwQÖg)  tritt  auf  in  ags.  glöm  , Zwielicht,  Dämmerun»* (doch  ist  ö  vor  m  mehrdeutig),  as.  glöian,  ahd.  gluoen  , brennen,  glühen glänzen',  aisl.  glöd  ,Glut,  glühende  Kohle',  ags.  gläd  f.  ,Glut,  Flamme, glühende  Kohle,  Kohle',  afries.  gled  ,Glut,  Brand',  ahd.  gluot  ,Glut, glühende  Kohlen';  aisl.  -glör  n.  , Glanz'  (:  %Io}q6<;),  aisl.  glöra  , funkeln'; s.  auch  unten  S.  433  ghlöu-]  ;;
POK_02.txt:1464:lit.  ^eriüy  zeriti  ,im  Glänze  strahlen*,  zeruöti  ,glühen,  funkeln',  ablaut. zarijä  f.  ,glühende  Kohle*,  apr.  sari  f.  ,Glut*;
POK_full.txt:31708:Irish guar coa\' (< *geulo- or * goulo);
```


## [2026-09-05T20:08:19.004Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '760,780p' POK_02.txt"
}
```


### [2026-09-05T20:08:19.054Z] TOOL RESULT

```
J^i.junäti  , treibt  zur  Eile,  treibt  an,  facht  ^n^jdvate  ,e\\t\  jütd-h  , eilend', jfi-  ^schnell',  Jw^i  , Schnelligkeit,  Aufmunterung',  j'avzn  , eilend',  java-/i  , eilend, ^chneW,  jävistha-h  ,der  rascheste',  m.  ,Eile,  Schnelligkeit',  jdvas-  ,Schnellig- j^eit',  jdvana-h  , treibend,  anregend';
av.  zavah-  n.  ,Kraft,  Stärke',  zävar-  n.  , (physische)  Kraft,  Stärke'  (bes. der  Füße  und  der  Rosse),  npers.  zör  , Kraft',  bal.  züt  , schnell',  av.  zdvlstya der  eiligste,  rascheste,  der  förderlichste',  uzutay-  , hervoreilend,  hervor- sprudelnd' ;
daneben  auf  idg.  geu9-  weisend:  3lv.  java  ,eile';  npers.  züd  , schnell' kann  zu  ar.  g  oder  z  gehören;
vielleicht  zu  anord.  keyra  , fahren,  treiben,  werfen,  reiten';
skr.  züriti  se  ,sich  eilen',  von  Trautmann  80  zu  güriti  se  ,sich  zusammen- ziehen' gestellt,  vielleicht  trotz  des  unklaren  Anlauts  hierher.
WP.  I  555.
g[e)u-lo-  ,glühende  Kohle'.
Mit  /-Suffix:
ir.  güal  , Kohle'  (<  "^geulo-  oder  ^goulo-)]
aisl.  kol  n.  , Holzkohle',  ags.  col  m.  , Kohle',  engl,  coal,  afries.  kole  f., ahd.  kolo  m.,  auch  kol  n.,  mhd.  kol  n.,  kol{e)  m.,  kole  f.,  Schweiz,  cholle , glimmen'.
Dazu  mit  r-Suffix  (oder  erst  aus  *gulo-  nach  arm.  hur  , Feuer'  um,- gebildet) :
arm.  krak  ,Feuer,  glühende  Kohlen'  (<  "^giiro-,  *gurä-),  krak-aran  ,Herd, Feuerbecken,  Glutpfanne'.
WP.  I  563.  Andere  Möglichkeiten  bei  W.  Schulze  Kl.  Sehr.  479.
geus-  , kosten,  genießen,  schmecken',  im  Germ,  und  Kelt.  , wählen',  im  Indo- Iran, und  Alban.  ,lieben';  nominal  gus-ti-s,  gus-tu-s.
Ai.  jö$ati,  jusdte  ^kostet,  genießt,  liebt',  ^*ösa?/a^e  ,findet  woran  Vergnügen', jösa-h  , Zufriedenheit,  Billigung,  Genüge',  av.  zaos-^  apers.  daus-  , Geschmack woran  finden',  av.  zaosö  , Gefallen',  zustö  ,beliebt,  erwünscht' ;  khotan- sak.  ysäsde  ,er  schätzt',  ysua,  ysuyän  {ys  =  z)  , Leckerei' ;
gr.  ysvof.LaL  , koste,  genieße'  (davon  yEvu)  , lasse  kosten') ;
alb.  desha  ,ich  liebte',  Präs.  do  dua  {^geus-n-j  Jokl  IF.  37,  101  f.) ;
n-Präs.  lat.  degünö^  -ere  , kosten'  (*gus-nö)',
air.  asa-gü  (*gus-s-t)  ,er  wünsche'  (ad-güsi^  asa-güssi  ,er  wünscht',  s.  zur Form  Pedersen  II  549),  do-goa  (*gus-ä-t)  ,er  wählt',  Verbaln.  togu  , wählen, Wahl',  Prät.  doröigu  ,elegit*  (*to-ro-gi-geus-t),  Pokorny  IF.  35,  177  ff.,  usw. (s.  Pedersen  aaO.) ;
400  ,
got.  kiusan  ,prüfen,  erproben',  anord.  kjösa  ,wähleii,  wünschen'  (an^lj ,durch  Zauberei  beeinflussen',  ahd.  as.  kiosaii  ,schmecken,  prüfen,  wählen»^ nhd.  kiesen,  Kaus.-Iter.  got.  kausjan  ,prüfen,  kosten,  schmecken'  (==,  ^' iösdyate);  vgl.  ags.  icael-ceasig  gleichen  wählend'  (vom  Raben).
```


## [2026-09-05T20:08:19.516Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31690,31730p' POK_full.txt"
}
```


### [2026-09-05T20:08:19.576Z] TOOL RESULT

```
presumably Old Norse karskr, /re/'s/r/'" fresh, agile, lively'. Middle Low German karsch 
"fresh, alert, awake, smart', Alemannian charzsch. 

References: WP. I 598 f., WH. I 429 f. 
Page(s): 390 



Root / lemma: g(e)u-lo- 

Meaning: glowing coals 

Note: 

Root / lemma: g(e)u-lo- : glowing coals derivded from Root / lemma: ker(9)-3\ to burn 

Material: With Asuffix: 

Irish guar coa\' (< *geulo- or * goulo); 

Old Icelandic kolu. " charcoal ', Old English colm. "coal', engl. coal. Old Frisian kolei.. 
Old High German kolom., also kolu.. Middle High German kolu., kol(e)xx\., kolei., Swiss 
c/7c»//e "gleam'. 

In addition with /"-suffix (or previously reshaped from *^^/c»- after Armenian hur^f\re'): 

Armenian Ara/r "fire, glowing coals' (< *guro-, *gura-), krak-aran^ siove, hearth, fireplace, 
glowing frying pan '. 

References: WP. I 563. other possibilities by W. Schuize Kl. Schr. 479. 
Page(s): 399 

Root / lemma: ge(i)- : gd(i)- : 57- 

Meaning: to sing, to cry 

Note: onomatopoeic word 

Material: Old Indie gayatiax\6 gati^ sings', gatu-xx\. and gTtf-i. " song', ^/?a-"sung, 

chanted', gatha^ song, verse' = Avestan ga&a^ song of religious content ';
```


## [2026-09-05T20:08:30.482Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 184 (p.163) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==185' HRN.txt | head -60"
}
```


## [2026-09-05T20:08:31.744Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"zuġāl\\|zuġâl\\|zugal\\|zuǧāl\\|sikār\\|sikar\\|Kohle\" HRN.txt | head -40"
}
```


### [2026-09-05T20:08:32.209Z] TOOL RESULT

```
=== HRN leaf 184 (p.163) ===
— 1GB —
Zur aw. i^sac'. sacait^, die aber nie 'sich geziemen'
bedeutet ') ; vergl. ahd. ke-hagin, nhd. behageiij an. hoegr
'passend, geschickt.
Über den Bedeutungsübergang spricht de Lagard e,
Ges. Abh. 800.
789. suft, sift 'Schulter .
aw. supfi' 'Schulter ; phlv. suft; ai. rüpti- 'Schulter ;
ndd. schuft (fichucht) 'Schulter (Bezzenberger, BB.
I, 341, vergl. Bartholomae, Studien II, 39).
si;!!. siwd, sar. sewd, sangl. siwd;.'d\hRn. sup,
740. snften 'durchbohren', Praes. sumh-eni'^), sufUem,
aw. \/saoi)' in sufrä- 'Pflug, die Geiger unter
bei. sufnbag (No. 352) noch vergleicht, niuss weg-
fallen, da miorä' zu lesen ist (vergl. Bartholomae,
der ZDMG. 46; 294 aw. suwrä- mit 'Pfeif übeisetzen
will); phlv. suftan (für aw. sifat'^); Bund.).
kurd. sonfin 'durchbohren*, Praes. bSsomim.
Vergl. np. sumb^) 'Loch* (Xo. 740), süli (No. 758).
741. sifl/iden 'pfeifen, zwitschern*.
lat. stbiläre, sißläre 'zischen, pfeifen', sibilus 'pfeifend,
zischend; Gepfeif, Gezisch'; franz. siff^er (Hörn, KZ.
32, 586 No. 19, onomatopoetische Bildungen).
np. sußJden wird dagegen nur als 'husten' bedeutend
aufgeführt und gehört zu surfe 'Husten', surfiden.
Got. sviglön 'pfeifen* (Froehde, BB. 3, 15; 14, 111)
und kelt. sige^ sidhe^ sighe 'Hauch' (Strachan, BB.
18, 147) lassen sich kaum lautlich mit den neup.-
lat. Formen vereinigen (die Araber haben safir
'pfeifend', daher np. auch mftr kerden 'pfeifen').
742. sekär, sikar^ sukar 'Kohle'.
aw. gareniö,]skarana (vd. 14, 7) 'Brennkohlen', vergl.
skairya- (vd. 8, 95) 'Kohlenmeiler (Geldner, KZ. 25,
566 Note 15); af/. skör 'Kohle'.
Hat np. nigal 'Kohle* (nur FS) etwas mit sekär zu
schaffen ?
»J Auch nicht Vd. 18, 16, vergl. Geldner, KZ. 28, 301.
') Geschrieben stmho.
^) Aw. (/ aaef' ist ihrer Bedeutung nach unsichor.
11*
```


### [2026-09-05T20:08:32.262Z] TOOL RESULT

```
1534:126. efiffist 'Kohle'.
1535:Vergl. skr. angärä- 'Kohle'.
6462:742. sekär, sikar^ sukar 'Kohle'.
6463:aw. gareniö,]skarana (vd. 14, 7) 'Brennkohlen', vergl.
6464:skairya- (vd. 8, 95) 'Kohlenmeiler (Geldner, KZ. 25,
6465:566 Note 15); af/. skör 'Kohle'.
6466:Hat np. nigal 'Kohle* (nur FS) etwas mit sekär zu
```


## [2026-09-05T20:09:15.821Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT skarana/skairya ===\"; grep -n \"skarana\\|skairya\\|skarəna\\|sarəniō\\|sarəniiō\" BRT.txt | head -20; echo \"=== BRT daxma ===\"; grep -n \"daxma\" BRT.txt | head -20; echo \"=== BRT daxsa ===\"; grep -n \"daxša\\|daxsa-\\|dažaiti\\|daž-\" BRT.txt | head -20"
}
```


### [2026-09-05T20:09:15.911Z] TOOL RESULT

```
=== BRT skarana/skairya ===
26467:•  j.  skarana-  Adj.  (fem.  'na-)  'rund': aiibAa  z^ms  yal  pa%anayä  (sd.)  *nayS dBraiparayä  Yt.  10.  95;  5.  38,  J7, 19,
26469:•  j.  skairya-  n.  eine  Art'*  Vorrichtung zur  Feuerung:  yö  ätnm  °yat  kaca  dsitlm gatBm  avi  avabaraiti  V.  8.  95.
=== BRT daxma ===
2554:nominale  Beifügung;  in  den  meisten  'tat  .  .yat  a:£'ar3t>m  Yt.  J9.48;  46;  — Fällen  entspricht  unser  bestimmter  Artikel  'te yä  spö.jataca  .  -  V.  7,  3;  —  Ue yöt  spatui (schwachtoniges  'der');  a)  adjektivisch:  V.ij.ai,  22,  43;  —  'taisqm yöi gius  sar?- caiti  'te  mi>fa  tava  yat  ahurahe  mazdat  oanqm  V,2.4i;  Ytj.9,  12;  —  'lat?hqm "wie  vielfach  sind  deine,  des  AhM.  Ver-  (GPm.)  yat  myazdanqm  N.  6j;  —  ku>a träge?"  V,4,2;  —  "te  daxma  .  .  aniarSt  (Stverz.)  ti  v>r>zyqn  He  yöi  masdayasna naSmät  iarürirva  V.5.51;  —  i-.a  Vam  ;  V.  5,  i  o  usw. ;  42,  J.18",  (/.3,  26,  9.49, (APm.)  aJsnt^m(s±)..paiti.bar,ltN.ioj;'—  *Vd.i8-20i;  —  't^m  (als  ASn.)  .\  yat °tayä  urvarayä  älan»irfs'V.8.i$;N.6j,'Vd.\spiln~'  .  .  X.ij.sS.  2)  auf  ein  Relati-
2769:mit  pairi  1)  'ringsum  absuchen,  auf- lesen': mazdayasna  aitihh  zimß  pairisa- yanta  (Opt.)  . .  varfsqmca  (als  Obj.)  ..yezi nsit  pairiianie  . .  astqmca  7-arpsqm:a  .  . V.  ö.  7f. 's\  z)  'herumsuchen  nach  — , aussuchen,  auslesen':  asstnanqm  xraoldva- nqm  .  .pairlstanqmY.i4.4'i'>;  A.3.5'^; —  uxtiitn  srlr>m  pairisttm  F.^^f'*'; V.J. 42  PüZ,;  —  pairi  daxma  aSlayqn  vi daxma    calsayqn   Y.S.z.  a)    mit    Dat
2798:auf  ein  relativisch  angeschlossenes  Nomen vorausweisend:  >o/<iW:4a/  sp3  urupis  fuai -so  spl  yS  urupis  .  ,  V.5.33;  —  ufa  vä nasus  raz'iwst  .  .  'sa  Jruxi  yä  ttasus  V. J.14;  5.27,  28,  7.1—4,  *.i6,  41',  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37— 39;  40,  42,  If). 21,  Vd.iV.  10.  b)  substantivisch;  aStacTva daxmaisva . .  "sö  zl  asH  äaivanam  rapakö V.  7.55f.;  —  daxme  .  .  yat  °/a  pqsnu ra^'>a'.J/(sd-)  V.  7,49f.;  —  aisa  y5..aiwi.- >r}lti^ätus  (sd.)  *aivayaHi  -io  barfsmö.- sbrfiti  ratufris  N.  /Oj;  —  slaotaca  (sd.) yasnäica  . ,  yat  °sa  ahurake  mazda  "Pre is- lieder  .  .:  das  des  AAM."  Vr.if.ö;  6;  — jtal  ..  kmntiit  ava  hö  mirysüe  anJmltÖ si  'SÖ  , .  "wenn  er  . .  operiit  (und)  der foperirte)  stirbt,  dann  ist  er  disqualifizirt.." ^'■7-37;  —  iD  Kongraenz  mit  dem  Prae- diltkt;  cit  ai-at  vacö  äs  ,  J  baya  °h  3s ahunahe  vairyehe  "Was  war  das  für  ein Sprach  .  .?  Das  war  das  Stück  A/iV." 'W  i<).  I  —3,  o)  öfters  zugleich  auf  ein
3080:Vt/^fl.^ö;  — ^=7.7(APn,)  i>yej.!  Y.J7.14;   aaaih-a  daxmaiha   kqm.batainti  axlUca
3882:•  j.  aiwi.varSta-  Adj.  (fem,  "/(-)  'be- regnet, worauf  es  geregnet  hat':  vlsp3m\ a  ahmät  nasunam  -a  'ianqm  daxmanqmca ' 'tanqm  hixranqmla  'tanqm  vayanqmüi frariuhantanqm  "bis  dass  es  auf  die  Leich- name geregnet  und  .  .  und  auf  die  Lei- chenausscheidungen geregnet  hat  und  bis die  Vögel  (Alles)  aufgefressen  haben"  V.  ]
8636:•  j.  uz-daeza-  m.  i)  'Aufschütten  von Erde,  Aufmauerung' :  yat . .  paili  . .  daxma -za  kiryeinte  "wo  Leichenstätten  durch Erdaufechüttung  errichtet  werden"  V.j.9 —  y^t  ■  ■  P"'''  •  •  daxma  "-ta'l  *2'7kante
8638:(sd.)  V.J.13;  —   aaaih'a  daxmaih-a  .  .
8927:mit  rf  'zu-,  herrichten':  *pmri  daxmn aisayan  vT  daxma  caisayan  "nach  I^ichen- stätten  sollen  sie  sich  umsehen,  Leichen- stätten sollen  sie  herrichten"  V,  cV.  2,
9063:mit  7'i  'durch  Graben  beseitigen,  ab- tragen; zerstören':  yasca  .  .  daxmatiqm avavanhm  maz3  vtkanayät  ya>a  .  .  V.  7. 51 ; — yat  b.J  paiti  fra!st.>m  daxma  uzdaSza (sd.;  lies  vrd')  vJkanü  (3SPA.)  yahmya  . . "an  welchem  Ort  man  am  meisten  die  D. durch  Abtragung  zerstört,  wo  .  ."  V.  y. 13;  —  yat  bü  paiti  fraüittnt  vikmte (3SPM.)  .  .gjmam  V..J.Z2;  —Wäyadanä (sd.)  tyä  gauiii'ätJ'  . .  viyakai'  (3SPrA.) Bh. /.  14;  —  kyt^  aparam  imilm  dipim vaitnhy  ..  maty^  (sd.)  vikanähy^^  Bh. 4.  15;  16;— _jW;>  imrim  dipim  ..vainähy '.■ikanähidisi^  Bh.  4- 1 7  II  ■
10289:'essen',  von  den  Dasva:  aste  yöi  dagva aitaisva  daxmaisva  gan/i)nti  apäca  vae- pmH  ya>a  .  .  V.7.SS.
11922:daxmaliva  hqm.bavainti  axtilca  garmusca 'ftusca  V.  7. 5  7 ;  VyL  50 ;  —  paiiistätse  gars- näuica  'naoica  Yt  y,  1 3 1 ;  —  apa.ävarata 'nu  Yt.^.8;  1 1 ;  —  paitistätSe  dazu  . .  'nu V.20.3.  a)Plur.mitGS.  a^rö(Sp.3i4  0.) 'Fieberanfälle';  k3 paoirys  a%rS  'nus(AF.) dürayat  tanaot  hata  tnasyehe  V,  20. 1,
12460:'äkirsnvS  vJspe  'va  zardhufira  yBt  para akmät  vtr5.rai^a  apataypn  paiii  äya  amS "du  hast  bewirkt,  dass  die  D.  sich  alle  in die  Erde  verkrochen,  die  sich  zuvor  in Männei^estalt  auf  der  Erde  herumtrieben" Y.p.  15;  FrW.4.3;  —  valtumnsm  akmat para  "va  patayjn  .  .  *apaJtarlay?n  (sd.) fainis  haca  maiyakaHbyS  aal  tä  .  .  hazB nivarKaym  (sd.)  'va  äat  tl  aivS  ahunS vaifyS  .  .  *zamangusa  avasai  vXipe  "va ayesnya  avahmya  Yt.  ig.  Za{.;  — ansürahe (sd.)  grlvaya  .  .  yat  ahmya  °va  handva- nnti  druj5  haca  girihSha  Y.^.j;  ig.44;  — alte  yei  "va  aBaisva  daxmalsva  gaafanü apaca  valpptttiY.j.$$; — Jha  'vanqm  han- dvarMS  kva  'vanqm  hantpatanS  kva  '-va hqmjivannti . .  /  . .  altaihßa  daxntaisva . .  V. 7.53 f.;  54^;  —  öAva  vyari%aAva{s,d.)  zpmS
12594:•  j.  daxma-  m.  'Leichenstätte,  Leichen- bestattungsort'*':  'ma  (NP.)  .  .  yaAmya nar/f  irista  niiayeinte  V._9.  9;  13;  —  sairi ..  triste  °me  nihätte  V.  7. 49;  —  avi  Ai irista  tanOm    upa    "ma  fraiaröis  \A.i2;
12598:LcE  Parsii  206,  der  auch  Abbildungen  gibt. El?    VII.   eig.  'Verbrennungsslälte',   mm  V. dag-,  %  33  h.   —    np.  daxm,  daxma.  —    Pä-: daxmai,  in  F.  mit  der  np.  Erl. :  gär  mäna  dar an  matdagän  rä  barajid.
13235:—  tairlm  gäma  (sd.)  frabarat  .  .  urva anayragiva  raocöAva  mdarjät  H.  2. 1 5 ;  1 5^, 33;  vgl.  f;  —  yavat  .  .  kangmrvayqn altavat  . .  Au/ie  (sd.)  zpme  nidaiiyan  V. ''■  29;  31;  —  Ja/W  (sd.)  . .  WM?  nihaite (NDf.)^'>  V.7.45;  49;  —  taohri  ..  ta Als  dasva  garS  nmätu  Yt.  /0. 3  2 ;  —  at  Asi vaAmSng  dfmäTig  garS  (sd.)  nidämä  Y. 45-  8;  —  mi^ma  . .  yaAmt  vyäne  (sd.)  . . masfl  amava  niiälim  Yt./o.64.  b)  wo?- Adverb:  kva  narqm  iristanqtn  tanom  ba- räma..kva  nidäiiäma  V.6'.44;  —  astala . .  tanüm  nidai^yan  V.5, 12;  —  daxma  . . yaAmya  narö  irista  tmayeinte  V,^.  9;  • — an'öpäo  m  nidaiaite^  a/is  .  .  *aniar?.- ar^i^m  nmSnoAe  Yt  iS.  4.  c)  Instr. : Aiiu  pqsnu  (sd.)  gitu  niaayaila  V.  16. 2.  d)T>3X.:  ai^ä  aAmäi  varmüi  ..nidä- tfttt  ahm  süiäyäi  tkalsäi  (sd.)  rSiayeAAf druxSY.4S-Z''  —  amtmca  Vfr^^rayti^mca ni'jät>m  tanuye  Yt  14.  38.  e)  Gen.: huskanqm  (näml.  alsmanqia,  als  Obj.)  . airiAa  S3ms  (sd.)  niäaÜyqn  V.  7.  29;  — aSa^qm:a  (näml.  Aaoliianqm,  als  Obj.) zftitö  nidaiiyqn  antarfin  ar?wtn  nmänaAe V.  6".  43;  -—  äat  vohu  maiiB  nidatoTi.. raocaukiim  yat  Ae  stärqm  aiwi.raocayantt "dann  sollst  du  (ihn)  .  .  dem  Licht  aus- setzen, damit  . ."  V. /^.  23.  f)/(7jÄund Lok. :  paoirim  gäma  (sd.)  frabarat . .  urva Attmate  paiü  nidaläl  H.  2.  15;  15';  vgl.  a,
16760:bavam  aiwi-sasis  aiwiJmantB  "wenn  ich in  Worten  und  Gedanken  verwünscht werde"  Yt74. 34;  —  iS«  frikiä  paiti.- zantä  buyata  "hier  sollt  ihr  geliebt  und gern  aufgenommen  werden  (sein)"  Yt 13.  147;  —  altallva  daxma^a  .  .  yöi paiti  äya  zima  bavainti  vzda^a  usdista "in  diesen  Z>.,  die  auf  der  Erde  aufge- schüttet werden  (sind)"  V.  7.  54;  —  aat hl  im  za  bvat  psrme  .  .  "drauf  ward ihm  die  Erde  voll  .  ."  V.  2.  8;  —  ana buyä  savanS.sasta(sd.)  ana  buyä  huyaita- tara  (sd.)  Yt  5.  9;  — yif  bavaiti  xratu.- käts  (sd.)  Yt  13.  16;  —  yai  */ranata bun^^  N.  65(?);  —  liu'ha  nmäwm  yaoe- da%ani  iuäa  bun^^  (näml.  nmana)  yaos- data  "wie  kann  ich  das  Haus  purifizi- ren?  wie  können  (die  Häuser)  purifizirt werden?"  V,  72.  2;  77.  a,  72.  3,  75.  33*, 20.  a)  negirt:  yai  St  bavainti  *ana-
16816:mit  ava  1)  'hinab-,  hineinbringen':  y5\      mit    a»/    und    a    'etwas   herzubringen »otJ  ft'jW  kar^ä  frakarayäti  ava  iha  ba- '  zu  — '  (Akk.):  yat  .  .   avi  ätr?m  äbannti rtnü  *yavahe  vä  "wenn  man  in  der  Erde  \  affayä  urvarayä  .  .  Yt  i4-  SS- drei  Furchen  rieht  (und)  sie  bringen  (sva,  1     mit  avi  und/rJ:  pas^aiti  avi  Al  iritta- säen)   hier   Getreide   hinein   oder  . ."  N.  tanüm   Ufa   daxma  frabarBis  Vd.  12;  —
17494:'am  meisten'",  nach  Zahl,  Menge,  Um- fang usw.:  mq%raväkahe  .  .  yS  'Um  . . a/irmairyanqm  (Gen.  part  als  Obj.) . .  ava.- jaynat  Yt  1^.105;  —  yat  ba  paiti  'hm kärayeiti  .  .  yavanqnüa  västranqtnca  (sd,; Gen.  part  als  Obj.)  V.  3.  4;  ~  yat  bä paiti  't»m  viksnte  .  .  girihqm  (Gen.  part als  Obj.)  V.J.  22;  —  ya^  b3  paiti  'tim bavainü  .  .  g^rjiqm  (Gen.  Flur,  als  Subj.) V.J.  10;  —  yat  bä  paiti  't)m  malsmti pasvasca  , .  V._j.  6;  —  yat  bä  paiti  °t»m us.zlZ3nti  (sd.)  pasvasla  V,_j,  5;  — yat  bä paiti  'tim  daxma  usdaüa  (sd.)  kiryänte V.J.9;  13;  —  yat  bä  paiti  Uim  lairi nikantt  V.  j.  8;  —  yat  ba  paiti  "tsm uskfnti\.3.i2;  —  yS  't>m  apivataiU  dag- nayh  V.  g,  3.  a)  zur  Verstärkung  des Superlativs  '* :  yai  ahmi  nmäne  . .  'ttm yaozdätU.B3mö.t»n3mca  hu^ö.z3mS.t3m3mca kambistitnla  .  .  V,  5.  46^',
18506:•  j.  'naeza-  m.  Name  einer  Krankheit: aüalfva  daxmalha  kamiavamU  axtiica gannusla  tafnusca  'zasca  sSrastisYaV.j.SJ ; —  paiHstätSe  gamiSusca  tafttaolca  'sahe^a sarastSisca  Yt/J.  131.
18684:—  apqm  napät>m  .  .  yS  nirSus  daha  yO n^rfu/^i  taiasa  Yt/5.  51; — ya>a  nars vay%an?m  "wie  der  Kopf  eines  Menschen" V.ö".a2;Äa3,F.jc,P.j4;  —  narqm  näiri- nqmca  .,  ti  hrmava  mti-viaire  djyammm Visp?m  3  afimät  yat  aSe  narS  "var^/iva anhm  V.2.27C;  —  cvaiti  narqm  ..xaota ratufris  N.  20;  —  yS  narS  kimSgatvS  . . anya  dva  vä  nara  , .  3at  aSsqm  narqm  .. cvat  antari  ^mr^us^'^  V.5.27;  4.i,ä,;- — yä  nara  (NS.)  gätum  baraite  F.^d;  N. 64;  —  paoifTtn  upa  may^m  frä.nasus (sA)  nartm  (statt  NS.)  bavaiti  V.  g. j8.  A)  Gegenüber  einem  attributiven a)  Substsl,  b)  Adj.  oder  c)  Proa  tritt nar-  vielfach  so  zurück ,  dass  wir  es  un- übersetzt  lassen  können;  es  gilt  das  ins- besondre vom  NS,  nä,  der  dabei  meist in  der  Stellung  der  Enklitika  —  hinter  dem ersten  Hochton  des  Satz-  oder  Versteils  — auftritt  a)9>  cvat  na"'^  3%rava  (sd.)  .  , *parayäl  ". ,  (ein  Mann,  der  Priester  ist, sva.)  ein  Priester  .  ."  N,  ^;  —  ydha  na taxmS  ra%a2stä  .  .  kaca  saltät  (sd.)  .  . paiti.ynUa  YtiJ.Sj.  b)  tts  nä  sayeiti (sd.)  vyäxanS  Yt  13.16;  53,  V.5. 40;  — paeiryeheca  na  myatdahe  aZaiit  (sd.)  .  . raius  , .  ratunafm  ayasnXm  (sd.)  daste  A. 3.  7;  8— 12*;  —  daxma  .  .  yahmya  nars irisla  nthayänte  V.3.Q;  Vd.  2',  17,  Vyt 12;  —  kva  narqm  iristanqm  tansm barama  V.  (j.  44;  —  kat  /a'(Sp,  612) nara  iristd  . ,  nasus  upaMvqsaiti  V,  7. 1;
=== BRT daxsa ===
12599:•  j-,  g.  daxs-  V.  'lehren'.  Praes.  3  daxsa-, i4daxfaya-[,  35  •öaxJayaeta'>].  —  PPfP. •daxäa-.
```


## [2026-09-05T20:09:16.844Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHM fradaxsana ===\"; grep -n -i \"fradax\\|fra-dax\\|sling\\|fala\\|daxš\\|daxsh\" AHM.txt | head -40"
}
```


### [2026-09-05T20:09:16.909Z] TOOL RESULT

```
=== AHM fradaxsana ===
866:mifrd y3 vouru. gaoyaoitis; zarstvacit® aé3gm fradaxSanya vazamna hata bazubyd aSamn6. vi36" bavaiti
880:Their sling-stones,* too, take off in flight from their arms, but pierce no wounds, since grass-land magnate Mithra, enraged and provoked, is hostile, not having been acknowledged.
1626:27. rexsyant-. I regard rgxfya- as a denominative of *rexia- ‘defiance’, which in its turn would ¥e a verbal noun formed from the -s- extension of a base *rax- ar *rgk- (cf. Av. daxsa- ‘fire, Brand’ + to dag- ‘burn’, Sogd. awys? ‘cauldron’ ta pak- ‘cook’, and Av. fra-daxs-, below, note 394).{ The same base is attested in Sogd. ran- ‘ta dare’ (cf. JRAS,
1734:39'. fradaxsanya-, adj. to fradaxsanz- ‘sling’. This, according to Da., ZA, Ul, 215, is glossed by NPers. falaxan. The latter, if it is a Sogdian
1737:LW, belongs perhaps to the same base as Av. fra-daxs-, without the s-extension (cf. Av, rexs-, daxs-, Sogd. puxs-, above, note 27"), a8 it may represent Sogd. */8’xn < *fra-dax(a)na-. [See Addenda.]
1871:(according to Wo.: ‘dich sollen die betenden Priester, die dra@yavan-(?) +t Priester um Wissen und um Heiligkeit bitten’) with Yt 4.9 and the almost identical phrasing of Yt 14.46: zara9ustra ation mgdram ma Jradaxsaya (Yt 14.46 fradaésayois) anyat pitre va pudrai bradre vd hadd. - xatai Gravandi va Grayaone. This means according to La. (who here follows Bth. and Gdn., Drei Yasht, $9): ‘O ZarathuStra, lehre diesen Zauberspruch niemand anderem als dem Vater oder dem Sohn oder dem leivlichen Bruder oder dem...(?) Priester’. It is at ance obvious that this translation does not account for the distribution of the disjunctive particle vd, and that Da, was right with his rendering ‘O Z., ne laisse enseigner cette Parole que par le pére 4 son fils, par te frére A son frére né du méme sein, par le prétre a son dléve’, Bth. probably discounted Da.’s translation because he did not consider fradaxvaya- and fradaégsaya- to be causatives; but Da.’s view of the situation can be upheld even if we translate: ‘do not teach this Divine Ward except either to the father for (transmission to) the son, or to the brother for (transmission to) the uterine Srother, or to the priest for (transmission to) the disciple’. The meaning ‘priestly discile’ is thus assured for ¢r@yaone by the context. For a closer definition of this disciple we must turn ta the question and answer in N 11: évat na aédrapaitim upaisat? yéra .draja; Prizaramazm xratiim asavansm aiwydphat, which Bth. (W2., s.v. ag#rapati-) renders: “Wie lange soll man einen Lehrer besuchen? Ein Jahr lang. Drei Jahre hindurch soll man dem Studium der frammen Weisheit obliegen’, adding the comment: ‘d. h. man soll zu drei Lehrern je ein Jahr lang gehen’. Such being the practice of priestly study, the Jrayavan- will be a student ‘attending a *Iraya-’, and the *9raya- (lit. ‘triad’, neuter of *#raya- ‘triple’) a triple course of studies, involving three years and three teachers. The Av. adj. *9raya-, accordingly, stands te Olnd. traya ‘triple’ (cf. trayi vidyd ‘the triple science’) as Av. Iraya ‘three’ to OInd. trdyas. In Jra@yavan- we thus find Avestan confirmation of Bth.’s o3inion that the long 2 of rays ‘three’ is not a secondary development of the Younger Avestan language, see GIP, 1, 3. 141. A free translation of
2493:136°. For asdnas(éa) Bth. and Lo. have ‘sling-stones’, Wi. and Soi. ‘spokes’, Gdn. ‘axle’, Da. ‘hub’, Hzf., 453, ‘jewels’, Htl. simply ‘stones’. ’ I side with Hzf., but take asanas°? as acc. of relation depending on the instr. vispd Jama, Hzf. understood both words as being in the nom. pl.: ‘and the jewels are containing-all-light’.
2875:Pp. 193, note 39% The sentence Owam at aéigm (scil. vacanham) paityastaramed fradaxstaraméa dadgmaidé in Y 35.9 was translated by Bth.: ‘dich (Zarathustra) bestellen wir als Einscharfer und Lehrer dieser (Worte)’. Humbach, JF, Lxt, 216 sgq., takes fradaxstar- as belonging to fradaxsanad- ‘sling’, and translates it as ‘Schleuderer’, that: is ‘AuSerer’, As a parallel to this unusual semantic develoyment Hum-
2878:bach adduces the preceding paztyastar-, which in his opinion belongs ta the base °ah- ‘to throw’ and therefore means ‘Entzegenschie3er (=Aussender, Auferer)’, That Avestan writers, who had at their dis- posal no fewer than four verbs for ‘to speak’, should have felt the need to supplement these with two verbs for ‘throwing’ is not very probable, especially as both fradaxstar- and pattyastar- are better explained other- wise. The former can safely be assigned to dax- ‘to teach’, as 3th. had done, the latter either to da-, with Bth., or to ad- ‘to speak’: if, as is likely, Bth.’s ‘Wiederholer’ (hence ‘Einschiarfer’) is the correct trans- lation, pati in the finite forms of pati-ad- (cf. alsa the perfect saityz3a, Bth., W%. $49) ‘to reply, respond’ on the one hand, in pattyastar- ‘he who says again’ on the other, can be assumed to have the two connata- tions of German wi(e)der in erwidern and wiederholen, Whether YAv. paiti.asti-, daitydsti- is to be separated from paityastar-, as Bth. wanted, ar associated with it, as Humach prefers, is difficult to say, as the con- texts are far fram clear. At any rate Humbach seriously underrates and misquotes Bth. when he writes of him (>. 215): ‘um morphologische Probleme unbekiimmert hilt er...asfa- fiir das P.P.P. von siz-’. Bth. printed °a-sta-, and justifiably interpreted a- as the shortened preverd, and -sta- as the outcome of *sthat-.
3194:bisyesta-, 248 butdyat, 327 fraorati-, 163 fraorat, 166 frayrati-, 285, 293 Sraxsti.d&-, 215 fraxsnin-, 166 fratamat|dat-, 197, 297 sqq. fradaxs-, 181, 192 5g., 324. 59. frat. dpa-, 210 framanah-, 185 framainya-, 224 frayana-, 261, 330 fravaiti-, 327 fravaz-, 271 fravait-, 163
```


## [2026-09-05T20:09:46.137Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT fradaxsana ===\"; grep -n \"fradaxsana\\|fradaxšana\\|fradaxsanya\" BRT.txt | head; echo \"=== SOD dgm ===\"; grep -n \"grove\\|ẟγm\\|dgm\\|δγm\" SOD.txt | head -30"
}
```


### [2026-09-05T20:09:46.197Z] TOOL RESULT

```
=== BRT fradaxsana ===
10884:•  j.  xStva-  Adj.  (fem.  °tvl-)  'der  sechste': akmSi  'tvö  äjasat ..  vjr^iraynS'Yt.i4.iT, 1.7,  15.2,  V.4.2,  N.  102;  —  'tarn  astaiiqm syaoimanqm  V.4.28;  1.8,  5.29,  30,  p.';, 28,  Y.p.2i,N.i'2,  F.j  (wo  '/um);  —  'tia- ht'a  ..  myazdake  A.^.  12;  —  tüirya  'hart- var»  ,  .  puxZa  tainäus  .  .  °tvT  fradaxsana V. /.^.g;  Vd.  72'>.  a)  ASn.  'tum  als Adv.  'beim  sechsten  Mal':  V.4.19,  23, S.Tl-
17612:VgL  /raäaxianä-  und  fradaxsanya-.  —  Pü.  (bei BlOCHKT  Lei.  107):  Aarsang  u  kafin')  "pierre de  ftonde'.    —    >)  Ob    richtig   beieagt?    —
=== SOD dgm ===
3763:been  guarded  against  absolute  judgment  in 
76157:Mack.  BSTBL,  Vim78  n  pl9  "grove  tree"
```


## [2026-09-05T20:09:46.920Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF leaf for p.173 ===\"; grep -n \"دخش\" FSF_pages.txt | head -20; echo \"=== FSF pages tag ===\"; grep -n \"pdf page\" FSF_pages.txt | head -5"
}
```


### [2026-09-05T20:09:46.998Z] TOOL RESULT

```
=== FSF leaf for p.173 ===
9844: ‫زمین چون نگین بدخشان کند‪.‬‬
11347:  ‫دخش‬
11356:                             ‫دخش (بازبر اول)‬     ‫مرو را مادرش با دایگان داد‬
11370:  ‫مکن بردل ما چنین روز دخش‬                       ‫(‪)۴-۸۲۲-۶۹۲‬‬
11376:           ‫جای دخش «رخش» ضبط است)‬                               ‫همان کهتر و دایگان تو بود‬
11379:  ‫مکن روز بر دشمن و دوست‌دخش‬                     ‫(‪)۶-۶۴۳-۱۵‬‬
11413:                ‫‪-۲‬مبحث‪ ,‬موضوع مطلب‪:‬‬               ‫مرکونزرا بر دلخویش دخش‬
12735:                                                           ‫ونه آ‬‫یو‬‫دخشت‬‫نه‬
=== FSF pages tag ===
```


## [2026-09-05T20:09:52.206Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17600,17620p' BRT.txt"
}
```


### [2026-09-05T20:09:52.255Z] TOOL RESULT

```
j. /raOi/r'  N.  34,  icxy-.  lies  raiufr'.
•  j.  fratura-  m.  EN,  eines  Gläubigen: 'rä  (GD.)  asrutä  bailatasturä  asaona  "des F,  and  des  A.,  der  beiden  Nachkommen des  ß.  . ."  Yt.  ;j.  125.
y-T-a-tura-  Adj,  eig.  Bed.?  Vgl.  ai.  Iura-  Adj, 'validus'  ?
•  j.  fradaxSaiü-  f.  'Schleuder'  als  Waffe: yagsam  zayanqm  rdhsisli . .  x//vf  "na  snä- var».iämra  (si)  maj  'krisqs  /radaxianyäis "..  Schleuder  mit  dreissig Schleudersteinen'
Ableit  —fra-daxi';  Et.?  —  Pü,;  knpdnn s.  dazu  HoRN  ZDMG.  4(^.39,  Dsx.  ZA.3, 215
•  j.  fradaxäanya-  Adj.  'zur  Schleuder gehörig,  Schleuder'';  asanasla  °ya  (NP.) "und  Schleudersteine"  V.  77. 9;  —  zarit- vacil  aisqm  ya  Yt,  10. 39.  a)  als  ntr. Subst.  'Schleuderstein':  fradaxÜana  (sd.) . . mat  %risqs  'nyäis  V.  i4-  9-
Ableit.  aas  /radaxSaiiä-.  —  Vgl.  /rai/ax!/aaä- —    Pü.!    langc'a  i  k  n  p  dn  n    (s.  unter  frada-
•  j.  'fra-daxäta-  Adj.,  PHP. :  s.  daxs-.
•  j.  'fra-daxSta-  Adj.  'mit  einem  Zeichen versehen,  gezeichnet":  ava  daxsta  äaxsta- vanta  yä  nsit  pouru.jira  (sd)  °ta  (NPm.)
Yt5.93.
FFfP.  aus  einer  Batis  *^dais;  die  aacb  in idaxUa-  steckt
•  j,  fradaxStanä-')  f.  'Schleuderstein':  isüm vä  arstim  vä  'nizm  vS  P.  27.
VgL  /raäaxianä-  und  fradaxsanya-.  —  Pü.  (bei BlOCHKT  Lei.  107):  Aarsang  u  kafin')  "pierre de  ftonde'.    —    >)  Ob    richtig   beieagt?    —
•  ].,  g.  fra-daxStar-  m.  'Lehrer,  Unter- richter, Unterweisei*,  von  AHM.-,  zdl  ns mazdä  ahurä  vaahSuS  °tä  mananhö  "sei uns,  o  MAk.,  Lehrer  des  guten  Denkens" Y._^j.  17;  —  syadkanäis  lärpnß (sd.)  .. *Aizvä  ux^äit  vanfOui  manar>Ad  yatiqm tu  *paouruyS  mazdä  °tä  akJ  ",.  (sie)  für die  du,  o  M.,  der  erste  Lehrer  bist"  Y. ji.  3;  —  ^wqm  (lüroi.  mazdqm)  aiaisqm (nämL  vacarnkqm)  paifyastänmca  (sd.)  'fa- nmln  dadfmaidi  Y.J5. 9;  —  dazda  ma- nar^AS  para  im  ioa  (sd.)  mananhe  HnasH (sd.)  ^■iiSa  'fänrn  mananfu  V.  i^,  13.
Zum  V.  daxi-.  —  Pü.  (dRn.):  fräc  daxSalün (2SI.),  fräc  äaxMimt5r,  fräc  daxia/iiA'.
•  j.  fradaSaßü-  (a)  Name  des  im  Süd- osten gelegenen  Erdteils  {Karhar-,  sd.)  ■> : avi  °ßu  vTdalaßu  \X.i0.i$;  133,  \.iri- 39;   —   avi  karhian  yat  'ßu  Yt.  J2. 11;
—  anzahibyö  (sd.)  . ,  °fhtbyd  vTda^aßubyB Vr.  10. 1.
Erstarrter  ND.  aai  'fimi-,  vgl.  unter  anzaki.- —  0  Bed.?  Ob  iix /radal.ßav-7  Vgl.  vTda- iaßü-  No.  i.
•  j.  fra-dadfi-  n.  'Gedeihen,  Zunahme, Vorwärtskommen' :  para  . .  ax/tat . .  '^pinca var?da'i»m^a  vaxsa'^>m^a  Y.g.  53;  51,  Y. 5.17,77.17,  Vr.  20. 1,  YrW.g.i,  Yytjg;
—  Uta  bannii  '%3m  vTspä  banmavB  gai- rinqm  Yt/Ä  6;  6';  —  ydäira  vs  aAurS mazdä  '%sm  baxsat  F.  4b;  —  'ha  (IS.) ..  var)da%a  Y,55.3;  —  'dathe'^  vanda- 'häiea  \.68.2.  '%äi  (und  "'hai  s)  als Inf.  sbes.
Zum  V.  da:  —  \^./rada%ä-.  —  Yä..:  fräk- dahSmh,  Sü.i  v^ddhidätik,  'dänam.  —  ')  Der LS.  in  Verbindung  mit  folgendem  DS.  ist  auf- fällig; et  kommt  so  im  nämlichea  S  noch 3nial  vor.
```


## [2026-09-05T20:09:52.752Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11340,11420p' FSF_pages.txt"
}
```


### [2026-09-05T20:09:52.805Z] TOOL RESULT

```
 ‫نگ‬            ‫گار طا‬       ‫تان آن‬           ‫ا‬
         ‫‪e‬‏‬                                                                  ‫تن آزاد و آباد گیتی بدوی‬
‫جون دلاور پلنگ‬              ‫برافراختی‬
                                                                 ‫برآسوده از داور و گفت‌وگوی‬
 ‫سبران جام زآن گاو و آن مرغزار‬
                                                             ‫(‪)۱-۰۲-۷۲‬‬
‫یکایک خبرشد سوی شهریار [‪:‬ضحاک |‬
  ‫دخش‬

                                                ‫ب یامد بکشت آگنسرانمایه را‬
                                 ‫نوعی حریر‪:‬‬     ‫چنان بسی‌زیان مسهربان دایسه را‬
                ‫شاه‬   ‫نامداران‬    ‫ببردند پس‬      ‫(‪)۱-۱۶-۰۷۱‬‬


 ‫دبیقی و دیبای رومی سياه‬                                                  ‫(ویس ‪:)۷۳-۷۱‬‬
  ‫(‪۸۷۳۰-۷۰۴۵۲‬‬                                              ‫همان ساعت که از مادر فروزاد‬
                             ‫دخش (بازبر اول)‬     ‫مرو را مادرش با دایگان داد‬
 ‫نکگیری» رشیدی‪ ,‬برهان)‪:‬‬
                      ‫اری‬
                        ‫هتا‬
                          ‫ت(یرجهو‬                ‫‪-۲‬پرورش‌دهنده تربیت‌کننده‪ ,‬مرد یزان‪:‬‬
  ‫اسفندیار به فرمان گشتاسپ به سیستان‬            ‫سخن از رستم در میانست که سیاوش رابه‬
‫آمده است تارستم را دست بسته نزد‬                 ‫زابل برد و استاد و آموزگارش بود و او را‬
‫گشتاسپ ببرد‪ .‬رستم چون آگاهمی‌شود به‬                                           ‫پرورش داد‪:‬‬

 ‫اسفندیار پیام می‌فرستد که از این اندیشه‬                       ‫بزاهبلستان شاه پرمايه بود‬
  ‫اند هیا تایه شو‬                ‫دشت برداز‬       ‫سیاوش را مهربان دایه بود‬
‫چندی باهم باشیم‪ .‬سپس در گنج‌های کهن‬               ‫(‪)۴-۹۱۲-۲۶۱‬‬
                      ‫را بازکنم و از خواسته‪:‬‬            ‫سیاوش جهاندار و پرمایه بود‬
           ‫بخواه آنچ خواهی و دیگر ببخش‬           ‫ورارستم زابلی دای بود‬
  ‫مکن بردل ما چنین روز دخش‬                       ‫(‪)۴-۸۲۲-۶۹۲‬‬

 ‫(‪)۶-۲۴۲-۹۱۴‬‬                                     ‫زابسل به بهمن پسر اسفندیار که‬
‫(در نسخه‌های لندن و قاهره و لنینگراد به‬                    ‫د‪:‬‬‫یست‬
                                                               ‫وا‬‫گستم‬
                                                                    ‫پرورش یافتة ر‬
           ‫جای دخش «رخش» ضبط است)‬                               ‫همان کهتر و دایگان تو بود‬
        ‫ابا آنک زو کینه‌داری به دل‬              ‫زایگان تو بود‬
                                                            ‫به لشکر پرم‬
  ‫مکن روز بر دشمن و دوست‌دخش‬                     ‫(‪)۶-۶۴۳-۱۵‬‬
 ‫(‪۹‬پرویز ‪)۷۲۳۱‬‬                                                               ‫دبق (بازیر اول)‬
 ‫(در نسخه‌های «رخش» تسنها در نسخۀ‬               ‫«حبی است بهرنگ و اندام زرشک و آن را‬
‫قاهره حرف اول را می‌توان هم «را» و هم‬            ‫مویزج عسلی گویند به سبب آنکه چون‬
                              ‫«دال» خواند)‪.‬‬     ‫بشکنند لعابی سفید و لزج مانند عسل از‬
 ‫أن واژه بهای معتى در لغت شهنامة‬                 ‫درون ان براید» (برهان) «چسبنده‌ای مانند‬
    ‫است‪.‬‬     ‫ده‬
              ‫ملف‬
                ‫او‬‫یست‬
                    ‫نفهر‬
                       ‫عبدالقادر و‬                                       ‫سریش» (غیات)‪:‬‬
 ‫گویا مولفان از نسخه‌های نادرست به‬                            ‫سر تنگ تابوت کردند خشک‬
  ‫اشتباه افتاده‌اند و بجای «دخحش» رخش‬            ‫به‌دبق و به‌عنبر به‌قیر و بهمشک‬
                                   ‫نوشته‌اند‪.‬‬    ‫(‪)۶-۶۵۳-۰۲‬‬
                                           ‫‪۸۳۳‬‬                                                 ‫دد‬


      ‫بدانتاپس از مرگ من در جهان‬                 ‫نگارنده همابتدابهاین اشتباه دچار شدم و‬
‫ز داننده رنجم نگردد نهان‪...‬‬                      ‫در جلد سوم شاهنامةٌ چاپ مسکو صفحة‬
        ‫به بوزرجمهر آن زمان شاه گفت‬               ‫له‌روی اهزمه‬
                                                             ‫بابه‬
                                                                ‫‪۰‬د‪۷۳‬ن‪۲۷‬‬              ‫بیت‬
                                                                                       ‫‪۹‬‬
‫که ایسن آرزو را نشاید نهفت‬                   ‫نسخه‌ها شکل ادرست «رخش» را در متن‬
       ‫نویسنده از کلک چون خامه کرد‬               ‫نگه داشتم و بعد متوجه این اشتباه شدم و‬
‫ز برزوی یک در سر نامه کرد‬                                         ‫اینک باید آن را تصحیح کرد‪.‬‬
‫(‪۸‬نوشیروان ‪)۷۴۴۳‬‬                                                                ‫نست‪:‬‬
                                                                                   ‫ییت‬
                                                                                     ‫اان ب‬
                         ‫(ویس ‪:)۱۵۳-۵4‬‬                    ‫اگر دل توان داشتن شادمان‬
         ‫کنون ده در بخواهم گفت نامه‬              ‫شهادی چرا نگذرانی زمان؟‬
                                                                       ‫ب‬

‫گبفهتاری کهخون بارد ز خامه‬                               ‫به خوشی بناز و به خوبی ببخش‬
                ‫‪-۲‬مبحث‪ ,‬موضوع مطلب‪:‬‬               ‫مرکونزرا بر دلخویش دخش‬
             ‫ازین در سخن هرچ دارید ياد‬           ‫)‪(TVWY-YFA-F‬‬
                                                                                  ‫دد (با زیر اول)‪‎‬‬
‫سراسر به من بر بباید گشاد‬                              ‫جانور درنده (بهواه دام نگاهکنید)‪:‬‬
‫(‪)۱-۶۸-۹۰۱‬‬
               ‫‪۳‬۔دره‪ .‬گشادگی ميان دکووه‪:‬‬
                                                                  ‫پذیرند؛ هوش و رای و خرد‬
                                                 ‫مراو رادد و دام فرمان برد‬
```


## [2026-09-05T20:10:09.706Z] TOOL CALL #22: Bash

```json
{
 "command": "pdftoppm -f 134 -l 134 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg134 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T20:10:11.121Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF page markers ===\"; sed -n '1,5p' FSF_pages.txt; grep -c $'\\f' FSF_pages.txt; awk 'NR<=11347{if(/\\f/)n++} END{print \"leaf idx:\",n}' FSF_pages.txt"
}
```


### [2026-09-05T20:10:12.187Z] TOOL RESULT

```
total 1900
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 16:10 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb 168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb 107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb  89133 Sep  5 16:09 pg145.png
```


### [2026-09-05T20:10:14.024Z] TOOL RESULT

```
=== FSF page markers ===
   ‫‪۵‬اژهنامکت‬
‫فرهوناکژته‌هایدشوارشاهنامه‬
  SAN    ۹ 75035 7-3
          ۱
  ‎‫ا‬
479
leaf idx: 226
```


## [2026-09-05T20:10:18.843Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FSF','AHM','SOD','BQT','MON','IEC','KLN','NYB','HRN']:\n  print(k,'|offset:',d[k].get('page_offset'),'|hint:',str(d[k].get('lookup_hint'))[:300]);print()\n\""
}
```


## [2026-09-05T20:10:18.888Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg134.png"
}
```


### [2026-09-05T20:10:20.535Z] TOOL RESULT

```
FSF |offset: 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking |hint: grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).

AHM |offset: leaf = printed + 14 (e.g. leaf 18 = p.4). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Commentary is by stanza/note number; the Glossary (end of book) lists Avestan words. grep the Avestan word in transliteration.

SOD |offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) |hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur

BQT |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d

MON |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe

IEC |offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

KLN |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

NYB |offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

HRN |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
```


### [2026-09-05T20:10:21.049Z] TOOL RESULT

```

```


## [2026-09-05T20:10:21.041Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:10:36.802Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD leaf 205 (p139) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==206' SOD_pages.txt | head -60"
}
```


## [2026-09-05T20:10:38.514Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 leaf ~214 (p404) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==215' KLN_1966.txt | grep -n -i \"day\\|dazaiti\\|dagaz\" | head -30; echo \"=== grep dazaiti in KLN ===\"; grep -n \"dazaiti\\|daž\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T20:10:38.828Z] TOOL RESULT

```
=== SOD leaf 205 (p139) ===
                                                                                                                            140


  dys-
 3533 6ys- B                           tJ^j'^^j^'j^K*-                 lamp, torch
      5axs ©fdag                                                       Sogdica. 40.11; GMS 60 n 1; C2, 60R 30, 94R 24,
         GcObe burned, (fcOget ripped                                    102V 19
         TSP 6.158 n p206; AVS 73                                3546 dmtyr      C =» 8mtyr
 3534 8yst-(h)       B                              l>w^.        3547 8n (MM,G=S
                                                                               rm)                            (oj* j~t j'K
         Saxst ®f. n.;ob. -y =*dxst-())                                6an (dn) ©<*hada-awana          -*6nn, 'Snn, S'wn,
         plain, desert                                                 with
         GMS 1180, 1183-, VJ 315, 316, 800, 813, 898, 903
 3535 5ywt-(h)        B, S                                ^.           GMS     1351, 1446, 1662; C2 gloss.
         5(u)yut ©Khwar.<5rd ®f. n. =*5wYt(>), 5wy5r             3548 dn     C =* Sn
         daughter
         GMS 421; VJ; TSP 2.983, 8.70, 87, 12.40; SCE 26;        3549 dnd'r      C =» SynS'r
           BSTBL, Vim. 69; Hen. Tales. 476.9; MDii Nov.          3550 5n5yt M =» 5nt>k(h), dnt>
           3R6, Nov. 4R7; Bcnv. BSL 1951, 22; pi. SYwtrt,        3551 dnhJ C                                    jj&<J*y -V
                                                                      denha ©<Syr.
           GMS 1231
                                                                       Epiphany
 3536 5ywtrt        S(M) ^ 8ywt-(h)
                                                                       C2, 55R16
 3537 *8m- =* 5m»k(h), 6m*s*t
                                                                 3552 5nk     B                                        ^-a**^
 3538 6mwn      M => 5m>n
                                                                       5/0ank/g ©<*0anga ©ob. -y; pi. -/
3539 8m>k(h) B                             J^uT                        nerve
     Samak (*5m-)                                  'fjj- j^TjI         TSP 2287 a p!72; pi. SntkK TSP 2.290, 360;
     swollen                                                             S W, C2 n p58
         TSP 2.35, 3.12; Hen. Texts. 715
                                                                 3553 8nn B, S                         (Q>> y^        j->)<>)^ <l
3540 am'n M, B                                       JLS«A±           with ^Snn, 5'wn, 5n
                                                                      San
     8man (5m*n) ©Av. Sdmana               ©ob. -3?; pi. -f/i
     house, dwelling                                                   GMS 1662
         GMS 282; BBB 540, 718, Hen. BSOAS 11, 74.3;
                                                                 3554 dnt> C                                                jLu*
           BSTBL, Padm. 12
                                                                       danda
                                                                       tooth (5n5yt) ©f. n.; pi. dntyt       =»6nt}k(h)
3541 SmVt    B                               ^Ar-uT"^fJJ
     Samsat ? (*5m~) ©<*dams-              ©pp.                       GMS 973; STi 5.4; C2, 14V 19
     swollen, blown up
                                                                 3555 6nt}k(h)     B, M                                     &&
     TSP 7.61; GMS 318, 539
                                                                      6andak      (6n5yt) ©f.n.; pi. dnfyt    =»krw
3542 Sm'yn'k        B                              4^0^                 6nt>k(h), dnt>
                                                                      tooth
     windy
     6amene         ©pres, part. =>pry SnVyn'k
                                                                      TSP 2.298, 7.55; SCE 322; Sogdica. 5.9, 21.9; VJ
     SCE 153
                                                                        546; Sntk, TSP 5.54
3543 emdw'p         B, M       (J^jj^)<W{f~<J^x.*                3556 dnty sq'f* C                    (vl&ofju^A^jjjljsi
     6am(6)waP ? ©MP           dmw*g                                  6ande-skafa ©f. n.
     foolishness
                                                                      gnashingG?/ teeth)
     Sogdica. 49.6                                                    STi; Sund. IF 1975, 95; C2, 51V5, 68V4 n p97.5
```


### [2026-09-05T20:10:40.801Z] TOOL RESULT

```
=== KLN 1966 leaf ~214 (p404) ===
=== grep dazaiti in KLN ===
10395:day,  n.  —  ME.  dai,  dei,  fr.  OE.  dxg,  rel.  to ON.  dagr,  OS.,  Dan.,  Swed.,  Du.  dag,  Goth,  dags, OHG.  tag,  MHG.  tac,  G.  Tag,  ‘day’,  orig. ‘burning  heat’,  fr.  I.-E.  base  *dheglvh-,  *dhog"h~, ‘to  bum’,  whence  also  OI.  dahati,  ‘bums’,  ni- daghah,  ‘heat,  summer’,  Avestic  dazaiti,  ‘burns’, Toch.  A  tsak-,  B  tsak-,  ‘to  bum’,  tsdk-,  ‘to  shine, glow’,  L.  foved  (for  *dhogwheyd),  fovere,  ‘to warm,  keep  'warm' ,f ax  illa  (for  *fovi!la),  ‘embers’. Gk.  -ri^px  (for  *dhegwhra),  ‘ashes’,  OPruss. dagis,  ‘summer’,  Lith.  dagas,  ‘burning,  harvest’, daga,  ‘harvest’,  degu,  degti,  OSlav.  zegp,  zesti, 'to  burn’.  Alb.  djek,  ‘I  burn’,  Mir.  daig  (gen. dega),  ‘fire,  pain,  disease’.  Cp.  also  Arm.  dag, ‘impressive’  (orig.  sense  prob.  ‘fiery’),  W.  deifio, Bret,  devi,  ‘to  burn’.  L.  dies,  ‘day’,  is  not cognate.  Cp.  daisy,  dawn,  and  the  second  ele¬ ment  in  landtag,  Reichstag,  Rigsdag,  Riksdag. Cp.  also  favor,  febrile,  fever,  foment,  fomes, tephrite.
```


## [2026-09-05T20:10:54.095Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '76140,76175p' SOD.txt; echo \"=== leaf 204 (p138) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==205' SOD_pages.txt | head -70"
}
```


### [2026-09-05T20:10:55.821Z] TOOL RESULT

```
Frag.  2a.ll,  12;  Frag.  Len  84  a8;  GMS  1178; 

Hen.  Talcs.  486.23;  abl.  wny\  GMS  1181 

10082  wn»k(>}   S  Jssr  ^J 
wanak  ? 

prisoner  of  war 

MDii,  Nov.  3V11,  IS;  Nov.  4R  12  p35;  Gersh. 
Advice.  91  n38,  wnyyk 

10083  wn'PrNvS   B  J&^lj^ 
wana(3ro5,  wn+}prw5 

woodland 

Mack.  BSTBL,  Vim78  n  pl9  "grove  tree" 

10084  wn'kh   B,  S  c^^ 
wanak   4wn-3,  wnt}k(h) 

tree 

VJ  pl22;  SCE  227,  241;  BSTBL,  Dhu.  144,  172, 

Vim.  30;  TSP  7.9;  Frag.  2a.l8,  20;  Frag.  Len. 

29.19,  38.7,  10,  17,  19,  26,  83a3;  pi.  wnfkh, 

SCE  529;  BSTBL,  Dhu.  212;  BBB  a7;  Frag. 

Len.  84  a  5,  6  b  2  "trees,  forest" 

10085  wn'ntk    B  <? 
wanande  ?   ^wnVn'k 
=== leaf 204 (p138) ===
139


3504 6prn>k    B, M                                            3518 6pxsty(y) M                                      4^,xf
                                                                    SPaxste ©pp                                      dym'y
     5parne    (Gbrny)     ©pi. dprnyt                                          >5p'yz-, 5p}YSt-, SPystc
                                                                    saved, gain
      giver 496; GMS 894
      SCE                                                           Sogdica. 16.5
3505 6prt- B, M, S                                             3519 Sbyr M => 5pyr                                   -loL>»

     SPart, Gfart ©pt. st.; inf. -yy                           3520 5pys M
                                         Spr-1, 6p>rt-,
        9brt-                                                        5Pes =»pw5Pys, SP'ys
      0<?)give                                                       harm, damage
      GMS 856, 883, SSbrh GMS 957, Sfirtyy, 931;                     BBB 483, 529; GMS 957
        KG; Frag. Len. 37.6
                                                               3521 6pys-      M                       o-^L-jv*--- I *0J j j '
3506 8prty B, M, S                               oJ^oj^jia
                                                                     Spes ©<*dwais- ^SP'ys-
     8parte ©pp.
                                                                     (to)hurt
                                                                     GMS   682; BBB 483; Sogdica. 64.12
      given
      VJ 4b; SPrtw, BBB 503; KG 488; Sfiwrty,                  3522 fipysnyy M                            *j±J jT tL)UJV~--7
        Sfiwrtw, MDii pl99; MDiii pll9                              SPesne ©pres. part.
                                                                    damager
3507 6pry *± SPr'y
3508 Spt'ykCw) B                                                     GMS 892; BBB 488
                                                          r>
     6pitik ^6ptyk                                             3523 6pz-      B, S
     second
                                                                     5Paz (dbz-) ©nom. -y; ace. -w; abl
      TSP 2.259, 324, 730, 3.16; W-Li, ii; BBB                       hunger                                        =>>SPz>
3509 5pt»y-w B, S                (j^ ^^ ^)^ <f>                      dbzy, C2, 31V 28.29, dbzw, C2, 102R 27, 102 V
     6pity(u), 6Pidi (Spty-, dbty-, 5piyw)                             24, dbz\ 31V 31, 69R 25, 102V21; VJ 814; TSP
       ®<*dwitya(m) =»5ptyk, 5ypty-                                    22.3; Hen. Talcs. 480.19; Anc. Lett. 2.1 1, 38;
     (rAe)sccond, other                                                MDii pl99; MDiii A 18.6
     GMS 430, 1331-6; VJ 290, 376; MSP bl2, 54,                3524 dbz-      C =» 6Pz-
       182; C2 gloss.; MDii; KG 596; Frag. Len. 92.15,
                                                               3525 Spz'mwrty   B                           J^f        ji ^
        82a 25; d0tyy, Frag. Len. 41.5; 6pty\ TSP                   5paza~murtc =»Spz-, 'SPz'mwrty
        3.256; Hen. Cosm. 312, 121; C2, 25R 16                      died of hunger
3510 Spttyk   M *± Sptyk                                             VJ 312, 1093; Gersh. Sogd. Cpds. 140, 148
3511 6pty- =* 8pt»y-w                                          3526 65prt M => 8Prt-
3512 dbty-    C =» SPt'y-w                                     3527 86ptyk => 5ptyk
3513 dbtyq    C =» 5ptyk                                       3528 88tystt     M => 5tyst
3514 8ptyq    M => 8ptyk                                       3529 65yn M => 5yn
3515 Sptyk B, M,S        (J>> >^- ^)jt X^fS-> '^               3530 5y- S
     6Pitik, Sipdik (SSptyk, dbtyq, 5ptyq, Spttyk)                                                                  d-xljj**
                                                                    5ay *=»5ys-, 5y}n
        =»5pt>y-w, 'Sp'ty, 5ypty-, Spt>yk(w), 5yP-
      0/ze)second, other                                            0o)burn
                                                                    Frag. Len. 84a.4, 5
      GMS 430; TSP 2.730, 3.16; Frag. Len. 37.12; BBB
        533; Hen. Tales. 485.2; Cosm. 312, 101; KG;            3531 Sy'n B                          (? o&J*.
        MDii; MDiii; STi 36.3; BSTi 193; C2 gloss.                  Say/xan
                                                                    ardent, fiery                            i_r° _r"je-' '
       dflt^ykw, TSP 2.324; Hen. JRAS 1944, 138;
       KG 375; Frag. Len. 99 d2; MSP p45; dbtyqy,                   TSP 13ii, 13 n p228; Benv. Notesiii 206
       C2; Sfityky, Frag. Len. 83.4; BBB 735; Sund.            3532 Sym'y B                                     j/
       AoFviii 1981 p214                                            Saxme ©Av. daxma-, Parth. dxmg          ©pi. -th
3516 5ptyw =* 5pt>y-w                                               tomb, grave
                                                                    BSTBL, Dhu. 212
3517 8pwrt S(MD) ^ Sp>rt-
```


## [2026-09-05T20:11:18.601Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB leaf 225 (p217) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==226' NYB_vol2_glossary.txt | head -50"
}
```


## [2026-09-05T20:11:18.799Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 leaf 272 (p~815) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==273' BQT_v2_pages.txt | head -40"
}
```


### [2026-09-05T20:11:20.887Z] TOOL RESULT

```
=== NYB leaf 225 (p217) ===
ul ~ the flaming up, the shining forth, of the dawn 44!?,
lyaxšitan to grow 40". — Av. (1337 sq.) Iyaxs-, v. also varšišn.
2vaxSitan to flame, to blaze 1%, — Av. (1338) *vaxš- ‘to sparkle’ (of fire), ‘to spurt’ (of water); MPrth was ‘to be kindled, blaze’ (MHC); v. ?vax$, vaxšiš- néh, vaxsénitan.
vaxš-var [whšwl] prophet 1115. — ‘Bearer of the Word, or the (divine) message’, v. lvaxš.
vaxšvarčh prophethood 454-7,
vāyēndak [w'yndk'] flying creature, pl. cas. obl. —-än, enumerated after murvān 802. — Pres. pt. of Av. (1356) Wvay- ‘to fly’.
vizčnitan [w’cynytn'] to bring, to take a p. to a place (andar) 49?’; to lead (a horse) up to (0) a p. 5413-15; à tē pat ulēh ul vāzēnēm we shall carry thee up in the air 60%. — Caus. of väzitan.
vāzēnītār one who draws, pulls: asp i rahy ~ a chariot-horse 581”.
vāzišn v.n. of vāzītan (g. v.), pred. 1211’: dast + vat nē ~ it is necessary not to play the game badly.
vazitan [wcytn'] to travel, to ride: tē... ké vazäh [subju. 2nd p. sg. = ind.] pat vài i dérang-x"atà$ thou ... who ridest on the long-dominating Wind 9914-15, — Av. (1386) vaz-; MPrth. pres. wz- ‘to blow’ of the wind’, ‘to move, to go’ (MHC); Ghilain 52.70, cf Verbum 170; Paz.
Vaz-var
vazidan (Aog.); NP vazidan, bazidan ‘to blow’. V. also vaz-var.
vazitan [w’cytn'] caus. of the preceding v., to move: 1. trans. catrang — to play at chess 11915, 121%, — 2. intrans. to travel, to ride (= vazitan) 519-14. 6019, — Cf MPrth pdw’z ‘suite, followers’, pres. prw’z- ‘to cause to fly’, Ghilain 70; NP bazidan, büxtan ‘to play; to fly’.
vazr [wzl] mace 851%, — Av. (1392) vazra-; Paz. vazr(a); NP gurz; also, with meta- thesis, varz (q. v.).
"| vazurg [LB”, Prth RB’; wewrg, inscr.
welk-] great, big, high, lofty, passim; regularly placed before its head w., seldom: after (41?. 724); in titles great, chief: ~ framatar (g. v.); ~ šahridar (q.v.); — subst., pl. cas. obl. ~-dn the magnates HajA:6 [RB’n]. B:6 [welk’n]. 42. 1133, 16? [wewlg'n'], v. Christensen, Sass. 100. 110sq. — OP vazrka-; MPrthPrs wzrg; Arm. lw. vzurk, vzork, vzruk; Paz. guzurg, guzarg; NP buzurg. No comp. and sup.; for these forms meh, mahist are used; v.s. v. mas.
vazurgakän [LB’-k’n'] pl. cas. obl. of vazurg: (0) Col xakan u ~ to the Khakan of C. and his magnates 11323. — Cf váspuhr : lydspuhrakan (g. v.).
vazurgēh [wewlgyh, LB’-yh] greatness 517.26, size 151.
vazurg-kunišn [LB’ kwnšn'] of great achievements, executor of grand achieve- ments; pl. cas. obl. —-än 1068.
Vazurg-mihr [wewlgmtr'] n. pr. the fa- mous Grand Vizier of Khösröi I (531— 579): 118-121.
vazurg-späs [LB? sp’s] of lofty service, performing high duties, pl. cas. obl. —-än 106!, v. späs.
| vazurg-x"arrah [LB’ GDH] of great glory,
of Yam 44%.
vaz-var [wcwl] safe for traffic: puhl 4 ~ 1147. — V. vazitan,
www.parsianjoman.org | ool wok
vecak
208
vét-varéh
[vēcak [wyck'] lot, share, portion ; combat (as if it were a casting of lots between the combatants): rasnik ~ pitched battle FrP 14; v. nem-vecak. — From !vertan; Arm. lw. vičak ‘lot (e. g. in casting of lots), portion; position; fate, possession, dio- cese’; Ps. wyc ‘priest’, wycyhy �
```


### [2026-09-05T20:11:22.548Z] TOOL RESULT

```
=== BQT v2 leaf 272 (p~815) ===
                                                                                 ‫داز شمان‬




                        ‫‪-‬‬     ‫دار کوب‬             ‫دارشعان ‪ = ۱‬باشن‌شطهدار وعین‬
                       ‫بز وزن خاکروب ‪,‬‬            ‫بی‌نقطه بورزن آبریز گان » درختی باشد سطبر‬
                        ‫بزبان ‪.‬کیلالی‌مرغی‌را‬     ‫و خاردار وپوست آن بقرفه ماندلیکن از آن‬
                       ‫کونند که بامتقاردرخت‬       ‫کت تقر وسرخ نرمیشود ‪ .‬اکرقدری ازآن‌سحق‬
                               ‫را سوراخ کند ‪.‬‬
                       ‫دار بوگاوورسیشده۔‬
                                                 ‫کنتد وما سر که سرشند وبردندان لهند درد را‬
                                                  ‫فروشاند» وقدری ازچوب آن‌زنان‌بخود ب رگبرند‬
      ‫دارکوب‬                      ‫باکاف قارسی‬     ‫قرزهدی که درشکم مرده باشد بیفتد ‪ -‬و ستبل‬
‫و مشین نقطه دار زده » امر به نگاهداشتن باشد‬       ‫هتدی را فز دارششمان خوانند و دارشیمان «م‬
               ‫بعنی نگاهدار ومحافظت کن © ‪.‬‬                          ‫کوبند بحذف شین دوم ‪.‬‬
‫دار کیسه ‪ ۱‬س بکر کاف و سکون‬                                             ‫دفار‬
                                                 ‫رلی ‪ - ۲‬باوفراای قرشت بر‬
‫بای حعلی وفتحصین بینقطه " کسه مانندی‌است‬
‫که دربعضی از درختها بهم ءیرسد ودرون‌آن پر‬        ‫وزن بتماکین » سفهوسکو ود کهکروابند که‬
                                                  ‫تن در بیش درخالپا سازند ‪ -‬و مطلق‬       ‫بجهت‬
                            ‫از یشه میباشد ‪.‬‬                          ‫تکه کاهر ا نیز کفته‌اند ‪۱‬‬
‫دار هك » بامیم بروزن آبچك » نوعی‬
                                                      ‫دار فلفل ‪ ۴‬مهعروف است گ‬
                                                  ‫‪.‬وبند‬
‫ازمروباشد وآن مروسفید است » ومروجنسی از‬
‫رباحین بود وسد بلغمی بکثاید واکثر امراض‬           ‫شکوفه وبیلرفلفل است» وبعضی کویند درخت آن‬
                            ‫بلغمی را ناقع است‪.‬‬    ‫غیر درخت قلقل باشد(‪ )۱‬وآن را فلفل درازنیز‬
                                                                                   ‫کوند‬
‫دار نگ » بکر الك و سکون نون‬                                  ‫‪ .‬گرم وخشك است درسم ‪.‬‬
 ‫وکاف فارسی» خوانی با طبقی راکویند که کوشت‬        ‫دار کدو ‪ -‬بسکون‌ثالك » چوبی باشد‬
                                 ‫برآن نهند ‪.‬‬      ‫یلند کهدروسط حقیقی میدان برپای کنند و در‬
‫داد نهال » بکر نون و های بالف‬                     ‫قدیم کدوی طلا و نقره از آن مویباخته‌اند و‬
‫کشیده بلام زده » چوب بقم"را کویند که بدان‬         ‫تبر‌اندازان مواره و تاخته کرده تبری بر آن‬
                            ‫چىزھا رنگه کنند ‪.‬‬     ‫می‌انساختماند‪.‬تبرهرکس که برآن میشورده‌است‬
‫داد فی» بکر ثالث و نون بتحتانی‬                    ‫کآدنورا بااسب وخلت باومیدادماند‪,‬وآن‌هدف‬
‫کشیده ‪ ,‬نام موضعی است در هندوستان مشتمل‬           ‫راحریی برجاس وآن چوب رابتر کی قباقآفاجی‬
                             ‫پربتخانة بیار ‪#.‬‬                                     ‫خوانند ‪.‬‬

                                                                   ‫)‪ (۱‬چش‪ :‬امت ‪.‬‬
```


## [2026-09-05T20:11:38.069Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB vidaxtan/vitaxtan ===\"; grep -n \"vitāxtan\\|vidāxtan\\|vitaxtan\\|vidaxtan\\|vi-dāz\\|dāz\\|vitāz\" NYB_vol2_glossary.txt | head -20; echo; echo \"=== PHD widaxtan/daxmag ===\"; grep -n \"wid̄āxtan\\|widāxtan\\|widaxtan\\|daxmag\\|dāg \\|dazaiti\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-05T20:11:38.147Z] TOOL RESULT

```
=== NYB vidaxtan/vitaxtan ===
3769:täxtan [t’htn'] tāc- [t’c-] to run 319. 2819, 9817. — Av. täcaya- intens. of tak-, v. tacitan; NP tartan tüz-; v. also vitāxtan.
4248:vitaxtan vitdc- trans. to melt: bé witäcet 10177, — Caus. of vi + Av. (624 sq.) tak-; MPrth wdxtn, wdc- and wd’c- (MHC), Ghilain 50; MPrs. wdc- (8), Verbum 169; Paz. vadáxtan vadāž- (SGV); NP gudāx- tan gudäz- ‘to liquify’.
6159:wde-: vitāxtan

=== PHD widaxtan/daxmag ===
PHD.txt:306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
PHD.txt:310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
PHD.txt:1182:cemetery daxmagestān.
PHD.txt:1481:dakhma daxmag, dādgāh.
PHD.txt:1651:dissolve widaxtan.
PHD.txt:2774:melt widaxtan.
PHD.txt:4028:tomb aspānūr, dādgāh, daxmag, hazzān.
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD.txt:4987:kardagān 1%kardāg kam kamāndār kamān kamāl kamālīg kamistīh ‘kamist kamzor kamzorih kamar kamarband maygt arz! kastār kastärīh kchtar kaf
PHD.txt:5038:nay! kundāgīh kundāg nayestān! kandan kanīg kanīzag xwan-! xwandan! -gen
PHD.txt:5057:kār- wing! *kār-ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd
PHD.txt:5118:ašnawišnt ašnūdan! nišast nišastan waštīh 1-2waštan waštagīh waštag xwar-! xwardant widaxtan wadxém widār widār- widārīdan widārdan widūz- widazih- widāzīhistan wadbaxt
PHD.txt:5232:wasnid nixwiür- nixwārišn nahang, nihang wiyūz- wayūdagān wēn- (v. dīdan) жатап! wēnāgīh wēnāg winnār- winnārišn nēwardaxšīr winnārdan wēnāb wēnābdīg wēnābdāg niyūxš- niyoxsidan niyoxsián wénig
PHD.txt:5280:nāydāg wahīg wihīr- nārīg wihīrišn nāysrāy nayizag wan- niyox&- niyox&idan niyoxiián wing wānīdan nān Worübarst Worüjarst nohom nihumb- nihumbidan Wahman naxust nihuftan
PHD.txt:5451:| gandag dóvs?r jūvišn judāgīh judāg judbēš jud-dādcstān! jud judnāy -Cnīdan 1 *lawīdan juttar
PHD.txt:5552:daxmag, 1-2 jamag
PHD.txt:5553:daxmagcstān ras-!
PHD_mackenzie.txt:1826:diid-giih [d)t g)s] proper place, fire temple; = daxmag.
```


## [2026-09-05T20:11:39.239Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG daz / tak ===\"; grep -n \"\\*daž\\|\\*dag\\|gudāxtan\\|widāxtan\\|wtʾhtn\\|godāz\" CHEUNG.txt | head -30"
}
```


### [2026-09-05T20:11:39.283Z] TOOL RESULT

```
=== CHEUNG daz / tak ===
```


## [2026-09-05T20:11:56.398Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=4248{if(/\\f/)n++} END{print \"NYB leaf idx for line 4248:\",n}' NYB_vol2_glossary.txt; awk 'BEGIN{RS=\"\\f\"} NR==236' NYB_vol2_glossary.txt | grep -o \"^\\s*[a-zāēīō-]*\\s*2[0-9][0-9]\" | head; echo \"--- header of leaf containing vitaxtan ---\"; awk 'BEGIN{RS=\"\\f\"} NR==235' NYB_vol2_glossary.txt | grep -oE \"[0-9]{3}\" | head"
}
```


## [2026-09-05T20:11:57.453Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la CHEUNG.txt && head -c 600 CHEUNG.txt; echo; grep -c \"\" CHEUNG.txt; grep -n -i \"daz\\|tak \" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:11:58.460Z] TOOL RESULT

```
NYB leaf idx for line 4248: 234
216
--- header of leaf containing vitaxtan ---
111
441
206
215
282
701
147
913
228
180
```


### [2026-09-05T20:11:58.527Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1769485 Sep  4 14:06 CHEUNG.txt
Etymological 
Dictionary 


of the Iranian Verb 


Johnny Cheung 


Etymological Dictionary of the Iranian Verb 


Leiden Indo-European 
Etymological Dictionary Series 


Edited by 
Alexander Lubotsky 


VOLUME 2 


Etymological Dictionary 
of the 


Iranian Verb 


By 


ohnny Cheun 
y g 


LEIDEN : BOSTON 
2007 


This publication has been made possible by the financial support of the 
Netherlands Organization for Scientific Research (NWO), and Leiden Unwersity. 


This book is printed on acid-free paper. 


Library of Congress Cataloging-in-Publication Data 


A СІР. record for this book
58427
2640:*MISC: Огт. bras-/brastak ‘to burn [intr.]’ = brés-/bréSok, bróxtok 
3941:Y Av. dazdi, med. 2sg. OAv. dasuuä (Y 33.12), 3sg. OAv. dadatü (Y 53.8), 2pl. YAv. dasta (Y 68.21), 
3942:med. 2р1. OAv. -dazdüm (Y 53.5); Pres. {2} them. red.: IND. 3sg. YAv. "data (V 4.3 £), med. 35р. 
3966:dazdiiai (Y 35.4, Y 44.1), ? YAv. daste (Vr 15.1), aor. {1} OAv. daidiiai (Y 31.5, Y 44.8, Y 51.20), OAv. 
4030:possible to assign one of the roots with some certainty, notably OAv. dazdé (Y 30.4) 
4031:and dazda (Y 27.13) must be from *daH?, as -zd- in these forms can only be the 
4054:See *daH! || Pres. {1} athem. red.: IND. 3sg. YAv. nida0aite (Yt 17.6), med. OAv. dazdé (Y 30.4), impf. 
4055:3pl. YAv. adadat (Y 19.12), SUBJ. 3sg. YAv. nidaóat (H 2.15), INJ. 3sg. med. OAv. dazda (Y 27.13), 
4546:*AVESTAN: YAv. daZ- ‘to burn’ (on daZ- < *daji- see Martinez 1999: 130) || (+ 
4547:*apa-) ‘to damage by burning’ || (+ *ham-) ‘to burn’. > Av. daZ-, with -Z-, derives 
4550:Pres. ja: IND. 3sg. YAv. daZaiti (Y 71.8), YAv. handazaiti (V 5.9), INJ. 3sg. YAv. daZat (F 548), YAv. 
4551:apa.daZat (V 15.4), SUBJ. 3sg. YAv. apa.dazat (FrK 22) 
4554:*MIDDLE PERSIAN: BMP dc- /daz-/ ‘to burn’ = DMMPP: 146 
4555:Pres.: IND. 3sg. BMP асу! /dazéd/, 3р1. BMP dcynd /dazend/ 
4583:*MISC: Arm. (LW) daZan ‘violent, wild’ 
5155:dastén/dazan-, Siv. derz-, dirz-/dist, Tr. dasta/darz- ‘to sew’, NP darzan ‘needle’ 
9003:*MISC: (+ *ni-) Orm. n-/nustuk, nastak ‘to sit down’ = ney-/nöstök, nóstok, nostok, 
10661:*MISC: (+ *abi-) ? Orm. awök, haw- (supplet.) histak ‘to read’ = aw-/awók ‘to read, 
12111:< Pers. piyaz < *pidaz (Horn 1893: 77). 
13210:S'aw-/sustuk, Sustak ‘to weep’ = Saw-/So stók, Sóstok
```


## [2026-09-05T20:12:06.184Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==235' NYB_vol2_glossary.txt | head -3; echo \"...TAIL...\"; awk 'BEGIN{RS=\"\\f\"} NR==235' NYB_vol2_glossary.txt | tail -3"
}
```


## [2026-09-05T20:12:07.713Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4540,4590p' CHEUNG.txt; echo \"=== *tak ===\"; grep -n \"^\\*tak\\|\\*tak ‘to run\\|widaxt\\|wtʾhtn\\|gudāxtan\\|gudaxtan\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:12:07.870Z] TOOL RESULT

```
). 11119 (-artan); pass.: ka-š fratom frasm vistarthét when its (viz. the sun’s) first dawn is spread, shines forth 4418, — < vt-+star-, v. start; NP gustardan, -ridan; Verbum 206.
215
viščk
...TAIL...
488.14, 6419, 11124, 1127. — MPrthPrs wšwbyšn (MHC, A—H II). V. višuftan.
viš-šinj [wyšne'] venom-spurting 1026. — < viš (g. v.) + sinj, the composition form of the pres. st. hinc- from Av. (1727) lhačk- ‘to pour out’, v. ähanj and natan.
Vištāsp [wšt'sp'] the protector of Zar- tuxšt: Kat-~ -šāh 219-19, 245,201.22. bur- zāvand Kai-~ 58172; dahyupat bur- züvand Kai-~ 6020:21, 1119; ~-sah [-Sh] 18-30, passim. 35%. 11319-1117, 115%; [-MLK”] 365. 1088; ~ šahan šah [MLK’n MLK”] 80%. — Av. (1473 sq.) Vēštāspa-, OP Vistäspa-; Paz. NP Gu
```


### [2026-09-05T20:12:07.922Z] TOOL RESULT

```
*REFERENCES: Horn 1893: 63; IIFL II: 207b; Abaev, Slovar’ I: 156; EVS: 14b; DKS: 39, 160a; Benzing 
1983: 527; Werba 1997: 195; Cheung 2002: 184; ESIJa II: 311 ff. 


*daj ‘to burn’ 

*AVESTAN: YAv. daZ- ‘to burn’ (on daZ- < *daji- see Martinez 1999: 130) || (+ 
*apa-) ‘to damage by burning’ || (+ *ham-) ‘to burn’. > Av. daZ-, with -Z-, derives 
from a ja-formation *daj-ia-, on which see Martínez op.cit. = Liste: 27 

Pres. ja: IND. 3sg. YAv. daZaiti (Y 71.8), YAv. handazaiti (V 5.9), INJ. 3sg. YAv. daZat (F 548), YAv. 
apa.daZat (V 15.4), SUBJ. 3sg. YAv. apa.dazat (FrK 22) 


*MIDDLE PERSIAN: BMP dc- /daz-/ ‘to burn’ = DMMPP: 146 
Pres.: IND. 3sg. BMP асу! /dazéd/, 3р1. BMP dcynd /dazend/ 


54 *damb 


*PARTHIAN: (+ *aua-) ? ’wdjn ‘rigor, harshness’ > Ghilain: 51 | DMMPP: 66b 
*KHOTANESE: dajs- (days-) ‘burn’, dis- ‘to make it burn’ (SVK I: 56) || (+ *pati-) 
padas- (padajs-) ‘to burn [tr.]’, OKh. padis- (pandis-) ‘to catch fire’, dag- (das-) ‘to 
ripen’ || (+ *ham-) handaj- (handis-) ‘to be ripened’, (caus.) Khot. hamdaj- (handaj-) 
‘to ripen’ = SGS: 43, 68, 70, 140 

*SOGDIAN: BSogd. 6xs- (inch.) ‘to ripen’, SSogd. öy’’n PN, SSogd. öy’n ‘ardent, 
fierce’. © MSogd. öx5- “о give pain, hurt’, which is often cited (e.g. Gharib 1995: 
147, no. 3719), does not exist. The sole attestation in Henning, Sogdica: 48, line 2, is 
based on the educated guess of Henning himself: a partially restored (óxš)ny 
(|M2608 R.2 |) would translate (postulated) MMP [dxsg] = ‘sign, mark’. 

Pres.: IND. 3sg. BSogd. öxsty 

*NWIR: Zaz. dezayis/dezen- ‘to hurt’, Bal. dajit/daj- ‘to bite, sting’, NP dag ‘hot; 
brand, mark(ing)’, NP diZan ‘violent’ (< Pth.), Bal. daxt/ *diZ- ‘to brand’, Bakht. 
day bidan ‘to be fried, broiled’. © The attestation of Bal. *diz- is uncertain, on which 
see Korn 2005: 194, 374. 

*NEIR: Sariq. óizd/óiz- ‘to be ill’, Yghn. (impers.) daxs(-)/daxsta ‘it hurts’ || (+ 
*pati-) Wa. pidic-, pidic-/piön-, pidn-, pidiyn- “о catch fire, be ignited’ 

*MISC: Arm. (LW) daZan ‘violent, wild’ 

*SANSKRIT: dah ‘to burn’ (RV+) = EWAia I: 712 

«PIE Sieg. ‘to burn’ = LIV: 133 f. | Pok.: 240 f. 

*IE COGNATES: OCS Zego, Lith. deen ‘I burn’, Toch. tsäk- ‘to burn’, Lat. foveo 

=== *tak ===
24507:Pres.: IND. 3sg. MMP wadcyd; Partic.: perf. pass. BMP wt'htk /widaxtag/, BMP wt’ht /widaxt/; Caus.: 
24508:pres. IND. 3sg. BMP wt'cyt /widazed/, BMP wt'cynyt /widazénéd/; Inf.: caus. BMP wt'htn /widaxtan/ 
24524:*NWIR: (+ *ш-) NP gudaxtan/gudaz- ‘to smelt, melt’, ? Kurd. (Kurm.) 
41043:gudaxtan/gudaz-, 376
```


## [2026-09-05T20:12:14.143Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24470,24535p' CHEUNG.txt"
}
```


### [2026-09-05T20:12:14.190Z] TOOL RESULT

```
*KHOTANESE: ? attaya ‘unpolluted’ 

*CHORESMIAN: t’sy- (intr./inch.) ‘to melt’, t'sy- (tr./sec. caus.) ‘to melt’ || (+ *apa-) 
bd’s- ‘to walk fast’. Ф bd’s- is from *apa-tasa-, MacKenzie IV: 535. = Samadi: 204, 
15 

*NWIR: Kurd. (Sor.) tuwandinewe/tuwen-, (Sul.) tuan, (Sina) tawian ‘to dissolve, 
melt’, Awrom. tawiay/tawia-, Gur. (Kand.) -täwin- ‘to melt’ 

*NEIR: Oss. I. tajyn/tad, D. tajun/tad ‘to melt; to thaw’, (also with prev. zr-) D. 
zr-tajun/zr-tad ‘to bathe’, ? Sh. tiy-/tizd, tüyd, Rosh. té(y)-/tézd, Шуа ‘to go away, 
remove’ (certainly influenced by *taé), Pash. toy, toe (ppp.) ‘spilt, overflowed’ || (+ 
*aua-) Oss. I. udajyn/udad (udzst), D. odajun/odad ‘to wet, soak’. (intr.) I. 
udzesyn/udzst, D. odzsun/odest ‘to be soaked, wet’ || (+ *us-) Khf. wustey- ‘to 
shed, spill (blood)’ || (+ *nis-) Sh. naXtiy-/naXtizd, naxtüyd, Rosh. nixtéy-/nixtizd, 
nixtuyd, Bart. nixtéy-/nixtuyd ‘to go, come out, flow out’ (certainly influenced by 
*tac) 


376 *taHé 


«PIE *teH>- ‘to melt, thaw’ = LIV: 616 | Pok.: 1053 


*IE COGNATES: Arm. t‘anam ‘I dive’, OCS tajeti ‘to melt’, ? Welsh tawdd ‘melts’ 
*REFERENCES: КРЕТ. 142a; EVP: 79; KPF II: 189; Abaev, Slovar’ I: 180; MacKenzie 1966: 110; EVS: 
52a, 93b’ DKS: 2b; Abaev, Slovar’ III: 222 f.; Abaev, Slovar’ IV: 7 f.; Cabolov 1997: 74; NEVP: 84 


*taH ‘to melt’ 
*MIDDLE PERSIAN: (+ *ui-) MMP wdc- ‘to melt [intr.]’, BMP wt’c- /widaz-/ (caus.) 
‘to melt [tr.], BMP wt’cyn- /widazén-/ (sec. caus.) Чо cause to melt? = DMMPP: 


339b 
Pres.: IND. 3sg. MMP wadcyd; Partic.: perf. pass. BMP wt'htk /widaxtag/, BMP wt’ht /widaxt/; Caus.: 
pres. IND. 3sg. BMP wt'cyt /widazed/, BMP wt'cynyt /widazénéd/; Inf.: caus. BMP wt'htn /widaxtan/ 


*PARTHIAN: (+ *ui-) wdc- ‘to melt’, w(y)d'c- (caus.) ‘to dissolve" = Ghilain: 50, 47 
| DMMPP: 338b £. 

Pres.: IND. 3sg. wdcyd; Caus.: IND. 35р. wd’cyd, wyd’cyd; Partic.: perf. pass. "wdxtg; Inf.: "wdxtn 
*KHOTANESE: (+ *ui-) LKh. byaj- (byas-) ‘to dissolve’ = SGS: 104 

*SOGDIAN: (+ *ui-) BSogd. wyt’wxs ‘to disappear, melt away’, BSogd. wyt’yc ‘to 
melt’ 

(+ *ui-) Pres.: IND. 3sg. BSogd. wyt’wxsty, BSogd. wyt’wxst’y, CSogd. “wytwxsty; Partic.: perf. pass. 
BSogd. wytwytk ‘molten’; Caus.: pres. IND. 3sg. BSogd. wyt’yct 


*NWIR: (+ *ш-) NP gudaxtan/gudaz- ‘to smelt, melt’, ? Kurd. (Kurm.) 
bihöstin/bihös- ‘to melt’ (why -0- ?) 

9 The close match in meaning between the Ir. and Gr. forms suggests a common IE 
origin. Hence, the formally identical forms with the meaning ‘to run, walk, sim.’ 
should be excluded (*ta&!). *taHé appears to be an enlarged root of *taH. 

«PIE "enlarged" *teH5k- ‘to melt" = LIV: 617 | Pok.: 1053 


*IE COGNATES: Gr. 14c, (Dor.) тако ‘I melt [tr.]', (Hom.) ёт@кту ‘melted [intr.]’ 
*REFERENCES: Horn 1893: 199; Nyberg II: 217a; DKS: 307b; Gharib: 427b; Cabolov 2001: 175
```


## [2026-09-05T20:12:37.182Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT vi-daz ===\"; grep -n \"vi-daž\\|vidaž\\|vi\\.daz\\|vīdāz\" BRT.txt | head; echo \"=== BQT v2: داغ ===\"; grep -n \"‫داغ ‬\\|داغ »\\|داغ ‪\" BQT_v2_pages.txt | head -10; echo \"=== BQT v2: دخمه ===\"; grep -n \"دخمه\" BQT_v2_pages.txt | head -10; echo \"=== BQT v2: سکار ===\"; grep -n \"سکار\" BQT_v2_pages.txt | head -10; echo \"=== BQT v2: زغال / ذغال ===\"; grep -n \"زغال\\|ذغال\\|ژگال\" BQT_v2_pages.txt | head -10"
}
```


### [2026-09-05T20:12:37.311Z] TOOL RESULT

```
=== BRT vi-daz ===
=== BQT v2: داغ ===
19453:                     ‫رکه‪ :‬داغ ‪.‬‬      ‫‪۴‬‬                 ‫‪.‬‬           ‫دق‬    ‫»‬   ‫دغر‬      ‫رکه‪:‬‬       ‫‪۴‬‬            ‫نراو“ ‪.‬‬          ‫مهک‪.‬ی‬
34988:      ‫شمالی کوعهای قراداغ » در سرحد ابران وروی ‪ « .‬جفرافدای سیاسی » کیهان ص ‪. › ۵۸۱‬‬
38072:    ‫جمع* «وسمه وسمابالفتح‬         ‫‪ ۳‬داغ ‪ .‬سمات‬   ‫(عر)اسمة ‪ ۰‬شان‬    ‫‪5‬‬     ‫‪۴‬‬      ‫‪:‬‬   ‫مر‬     ‫ارك‬      ‫‪۳‬‬
=== BQT v2: دخمه ===
16868:  ‫دخمه فروژه‬                                                                                         ‫‪۲۲۴‬‬
16886: ‫دخمه راندیان س کنابه آاسزمان‬                               ‫وزن دستار» چادرسیاه وسفیدبرا گویند که برروی‬
16916:  ‫‪۰07۳1۵0‬‬                   ‫‪ - ۷‬اوستا‪amxad -‬‏ ؛ پهلوی‬                     ‫‪ - ۱‬رکه‪ :‬دخمه ‪.‬‬
33719:‫سازند ‪ -‬و بمعنی کورستان هم مدهاست‌ودخمه‬
=== BQT v2: سکار ===
31527: ‫و گرزگاو سار بمنی گرزکاو سرو سکار که‬
32505:                                                            ‫‪ - ۷‬سکار شادی‌لمادد تضت‬
36882:                                        ‫و معنی سک‬                         ‫سکار ‪ = ۴‬بکر اول بر وزن شکار »‬
36887:‫بند و بعربی مضراب خواننده وان‌در قانون‬                                        ‫د نم اول و سکون‬           ‫سکار ] هنج‬
36891: ‫فه باشد بمعتی سکافره است که مضراب‌سازندها‬                               ‫سکارو ‪ - ۱‬نماول‌ورايم‌بواو کشیده؛‬
36913:                                                          ‫میداند ‪ 1‬افغانی ‪rêks‬‏ (زغار) اسثق ‪YEY‬‏ رکث‪:‬سکارو‪.‬‬
36917:                                                ‫‪2‬‬    ‫آهنگه)‬      ‫(سکارو) (ه‪.‬م‪ )۰‬سل آهنج ( =‬            ‫کار‬     ‫از‬       ‫_‬   ‫‪۵‬‬
36919:                               ‫سکالیو « رشیدی» = کلو (حم‪۰ ).‬‬                            ‫سکاروا « رشیدی» =‬                   ‫‪۱‬‬
36941:‫ثالی » نوعی از طعام است ‪ - ۷‬و روغن با كعك‬                           ‫بممنی سکارو باشد بمنی آنچه برروی زغال‬
36982:     ‫‪ :‬بگاله ‪۰‬‬      ‫رك‬       ‫‪۴‬‬                 ‫سکالو (ه‪.‬م‪ = ).‬شکالو(ه‪.‬م ) ‪۰‬‬         ‫=‬       ‫سکارو (ه‪.‬م‪).‬‬     ‫=‬   ‫‪۱‬‬
=== BQT v2: زغال / ذغال ===
1519: ‫جز لگ بنتح اول و انی و سکون‌کاف‪.‬‬                        ‫جزغال؟ س بکراول بروزن امثال‪,‬‬
1523: ‫جز لذن = بروزن کزین » بمعنی‌تغییر‬                       ‫جزغال است که پارچهای دب برشته شده‬
2932:                                                            ‫جوا = باشومل‌بروزن زغال‪ ,‬معروف‬
4555:  ‫‪ « 056۳20 ۴‬اسفا ‪ ۷: ۱‬س ‪ ۰ ۷۰‬طبری ‪( 56۳۵6‬يزغالةٌ بکاله) «صاب طبری‬
5437:‫بمعنی‌چزدره است که جزغاله باشدیعنی دلبه وییه‬                             ‫کون دکه حمدونه است ‪.‬‬
8545:                    ‫‪۰‬‬    ‫الارب»‬   ‫‪ 4‬بزغاله وبره‪«.‬منتهی‬   ‫‪( ۹۳‬عر) «حلام کزنار‬    ‫‪۳‬‬    ‫عربی است‪.‬‬     ‫‪-‬‬   ‫‪۱‬‬
25771: ‫است ‪ .‬روسیه اصللا کشوری است زراعتی ودارای منابم فراوان معدنی از قبیل‪ :‬لفت ‪,‬زغال سنك»‬
28958:‫مدار‬    ‫حربی حبر و‬       ‫کنند و‬    ‫باشفد که در دوات‬               ‫رال‪ = ۸‬بروزن و معنی زغال است‬
28979:   ‫‪ = ۸‬زغال = ژکال = شگال = شگار » اورامانی ‪ 4« 14×02‬ا‪.‬ورامان ‪ ۸۲۱۰‬طبری‬
31061:                                                     ‫زغاله(ه‪.‬م‪ = ).‬زغاره (ه‪.‬م‪: ).‬‬     ‫‪= ۸‬‬
```


## [2026-09-05T20:12:43.454Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 16886 16916 28958 28979 36882 36891 36917; do echo -n \"line $L -> leaf \"; awk -v n=$L 'NR<=n{if(/\\f/)c++} END{print c}' BQT_v2_pages.txt; done"
}
```


### [2026-09-05T20:12:45.194Z] TOOL RESULT

```
line 16886 -> leaf 285
line 16916 -> leaf 285
line 28958 -> leaf 486
line 28979 -> leaf 486
line 36882 -> leaf 612
line 36891 -> leaf 612
line 36917 -> leaf 612
```


## [2026-09-05T20:12:52.790Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"########## leaf 486\"; awk 'BEGIN{RS=\"\\f\"} NR==487' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-05T20:12:54.760Z] TOOL RESULT

```
########## leaf 486
                                                  ‫يان دهم‬
                          ‫در زای نقطه دار بافا مشتمل برده لغت‬

 ‫سياه و‬   ‫چویآزنیست‬
                  ‫® »‬             ‫شد‬
                                   ‫ایر‬
                                     ‫بزق‬
                                       ‫ا‬        ‫نوعی‬        ‫زقاك ‪ -‬بفتح اول بروزن هلاك ‪ ۰‬ابر‬
  ‫چبنده که از درخت صنوبر حاصل شود وبرس‬                                                 ‫ند ‪۰‬‬
                                                                                          ‫وهیرا‬
                                                                                              ‫باگرند‬
 ‫عرمی لز بکسر اول‬         ‫ور‬
                           ‫کجلان چ‌بانند » د‬                 ‫زفان ‪ ۱‬ا‪-‬بوال مضموم» زبانرا کویند‬
 ‫همين معنی دارده وآن سه‌نوع است ‪ :‬یکی زفت‬                                     ‫و بعربی لخاونانند ‪. ۴‬‬
 ‫ر فا نه ‪ = ۴‬بروزن ومعتی زبانهباشد رومی و آن براق وصاف واملی میباشد و ازروم‬
  ‫هیآ وزلد و بعضی گوشد همی زفت است هاش‬
                                                            ‫که زبانة آنش ‪ -‬زوبانة چوب اومثال آن‬
 ‫زفت تر وآن‬      ‫برومی شهرت دارد » و دبگری‬                  ‫است » و آن چیزی است که در مان شاهین‬
 ‫آیکی و روان میداشد و آنرا درمرهمها بکار برند‬                                            ‫ترازو میباشد ‪.‬‬
‫وآن از فبیل قیراست و از الواع صتوبر کیرند‬                    ‫ز قت» بنتح اول و سکون ثالی وفوفالی‪:‬‬
 ‫ونوع سيم زفت خشك است وآلرا بیشترازینبوت‬
                                                             ‫بمعنی درشت وفربه باشد و گنده و سطبر ‪- ۴‬‬
 ‫ورز گیرند که بوتهٌ کبر و صنوبر لر باشد و‬
                                        ‫ا‬                   ‫وسفت وهنگفت را لیز کفته‌اند ‪ -‬و بمعنی پر‬
 ‫آن گونند که باری ندارد »‬              ‫صنویر نبرجهت‬
                                                            ‫ومالامال هم آمده‌است و طعم تیز و هز نیز را‬
                  ‫ومطلق آکنرم وخشك‌است ‪.‬‬                    ‫بگزد ‪ -‬و م اول بععنی‬       ‫را‬
                                                                                        ‫ادنکه‬
                                                                                            ‫بوبن‬
                                                                                               ‫ززک‬
                                                                                                 ‫ای‬
 ‫فر د بفتح اول ثوالی بروزن سفر »‬                            ‫بخیل و مسك ولتم ‪ -‬و گرفته و ترش روی و‬
 ‫دهانرا گوبند ‪ ۷‬وبعربی‌فم خوانند‪ -‬و کلج‌دهافرا‬                 ‫م‬
                                                               ‫‪-‬و‬‫طدع‬
                                                                   ‫ستیزه خوی و خشوت کناده باش‬
  ‫ندان‬
     ‫دد‬‫هک‌ون‬
           ‫هم گفته‌اند و استخوالی را نکیز‬                   ‫ولذت زمخت را نز گویند مانند مازو و هلله‬
 ‫ازآن روید و برآ بد‪ ۲‬؛ و بقتح اول و سکون‬                     ‫اومثالآن وبعربی عفص خوانند ‪ -‬وبکراول‬

  ‫چدم بررحوار بون‌نهاد (عیسی) وزفان‬         ‫‪9 ۳‬‬
                                                                       ‫‪ = ۱‬ربان («م‪ ).‬ز‬
                                                            ‫>وان (ح م‪.).‬‬
   ‫زباه‬     ‫‪۴‬‬             ‫؟‪.‬‬   ‫ص‪۸6‬‬     ‫«انجیل فارسی‬    ‫‪۴:‬‬
                                                            ‫بگشاد وبدیشان تعلیم و پندمی داد وم گفت‬
                                                                                ‫( م( = زوایه (ه‪.‬م‪: ).‬‬
          ‫وآنچ مصثوقة اورادل و دنده شکت‬                        ‫‪ ۴‬اینهمه زاری عاشق بنمود وننهفت‬
          ‫شدش کالبد از زاری وز فرقت زفت‬                        ‫ساعتی با اولششت و یاسود نوضفت‬
          ‫بفتاده براه ‪.‬‬        ‫صیناد‬     ‫معود‬   ‫شاه‬            ‫اینچنین سنگدلی ‪.‬بیحق‌وبیحرمت‌جفت‬
   ‫‪ ۶‬مذوچهری دامفالی ‪۶۵۱٩‬‏ ‪.‬‬
  ‫بعضی نرا از بونالی ‪( 5001/5۸‬فیر) ماخوذ‬     ‫‪( 100 = ۵‬فر) «لك ‪ ۲‬ص‪۲۱۲‬‬
   ‫‪ - ۱‬اوستا ‪( ۲2122 -‬کلو)‪ .‬پهلوی ‪« 72122‬اسشق ‪۳٩5+.‬‏ هوبشمان‬    ‫دالته‌اند «نفی) ‪.‬‬
   ‫و ‪ 82122‬فارسی را پامان‌کریت ‪( 102‬گرفتن » بایوزه گرفتن ) » و ‪29-‬حاصطهز‬                           ‫‪7‬‬
  ‫چه‬   ‫مراد فك است»‬   ‫‪-‬‬    ‫‪۷‬‬                ‫»لو ) متعاق میداند «هوبشمان ‪. ۳+4‬‬
                                                                            ‫( دندان » اسنان ک‬
   ‫«* زفر زیرین» فك اسفل است و «زفر زبرین» فك اءلی ‪ « :‬هر حیوالی بوقت خاییدن زفرزبرین‬
   ‫جنباند و ‪,‬یکی مخالف بود چنانك تماح زفرژیرین جنباند وزبرین لجنباند> «دابشنامه ‪۳4۲۰‬‬
```


## [2026-09-05T20:13:03.096Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /زغال = ژکال/{print \"BLOCK\",NR; print; exit}' BQT_v2_pages.txt | head -70"
}
```


### [2026-09-05T20:13:05.225Z] TOOL RESULT

```
BLOCK 489
 ‫سح‬    ‫هفش‬
                                                                                                                        ‫زکاشه‬

                 ‫تریج » اة سفالین بزرکه باشد ‪.‬‬                ‫ر وزن خلاصه ‪ ۰‬خاریشتی را گوبندکه خار های‬
                                                                                                       ‫ب‬
‫نم اول و فتح ثالی‌بر وزن‬          ‫زرگنف ‪- ۴‬‬

‫خجند ‪ .‬بمعنی ز کنج است که ‪6‬ه سفالن‬                                ‫اس باشیننقطه دار ‪ ۰‬بروزن و‬                ‫ر کاشه‬

                                                                  ‫معنی زکاسه |ست که خار بشت تیر انداز باشد »‬
‫‪ -‬بنتح اول بروزن ضبور ‪.‬‬                 ‫ز کور‬                                         ‫و با زای‌فارسی حم درست است ‪.‬‬
   ‫د‬
   ‫ددر‪-‬و‬
       ‫بمعنی سقله و بخیل و گرفته باش‬                              ‫ر کان؟ = بفتح اول بر وزن مکان »‬
             ‫و راهزن فوطاع الطریقرا لز گوبند ‪.‬‬                    ‫یاند که از خود رمیده باشد و‬   ‫رر‬‫کصی‬
                                                                                                    ‫شخ‬
 ‫زکریا ب‪۱‬نت‪-‬ح‌اول و کوسترحانتیانی‬                             ‫خود بخود سخن کوید * و طم ارول هم‬
‫(‪ )۱‬کارد را‬            ‫زندنود‬‫از‬ ‫یلغت‬
                                   ‫بالف کشیده ‪.‬ب‬                                                                     ‫کگفته‌اند ‪.‬‬

                      ‫گویند ویعربی سکین خوانند ‪.‬‬                  ‫ر کش = بنتح اول و کرکاف وسکون‬
 ‫ر کیدن ‪ ۷‬د بفتح اول‌بروزن رمیدن»‬                                 ‫شین شطه دار‪ .‬لذت و طعم زمخت را گوبند و‬

‫بعنی خودبخود از فهر وخشم سخن کردن »وضم‬
                              ‫‪۰‬‬   ‫‪.‬ات‬    ‫اول هم ورخ‬               ‫نم اول وفتح ثانیبروزن‬                ‫زرکنج ‪۶‬‬



                                                ‫بان دواردهم‬

                      ‫در زای نقطه دار باکاف فارسی مشتمل بر سه لغت‬
‫مدار‬    ‫حربی حبر و‬       ‫کنند و‬    ‫باشفد که در دوات‬               ‫رال‪ = ۸‬بروزن و معنی زغال است‬
                                            ‫خوالند ‪.‬‬              ‫معربی‬       ‫و‬    ‫کشته باشد »‬     ‫اخگر‬      ‫و‬       ‫که انگشت‬


‫کال ‪١١‬ے‏ بضم اول بروزن کلاله ‪,‬‬
                             ‫ر‬                                                                            ‫فخحومانند ‪٩‬‏ ‪.‬‬

‫بمعنی زکالاب است که سیاهی و مرکب‬                                  ‫زرگالاب لت بضْم اول و ثانی ولام هر‬
                                                ‫باشد ‪.‬‬            ‫دو بالف کتده ویبای‌ایجد زده ‪ ۰‬مر کب‌وسیاهی‬



                                                                                    ‫‪ :‬رند ویارژ ند ‪۰‬‬   ‫(‪ )۱‬چك‬

  ‫‪= ۴‬ژکان ( اسم فاعل از‬                       ‫ریکاه ) ‪1‬‬           ‫=‬       ‫رکاشه (مخ‌ف رکا‬          ‫مصحف‬          ‫‪۱‬‬

                              ‫رك‪ :‬زکنج ‪.‬‬         ‫‪۴‬‬                ‫‪ - ۳‬رك‪ :‬ز کند‬                  ‫زکیدن ژکیدن )‪.‬‬
  ‫‪ ۰‬کارد‬      ‫‪trûk‬‏‬   ‫پهلوی‬   ‫‪21 ۰‬‬         ‫‪220۰‬‬          ‫‪۰‬‬   ‫هر‬       ‫ت‬   ‫‪1‬‬           ‫کور (ه‪.‬م‪. ‎).‬‬     ‫‪۶‬‬        ‫‪o‬‬

   ‫(«‪.‬م‪. ).‬‬      ‫‪ = ۷‬ژکدن‬                ‫کزا» تصحیف شده ‪.‬‬
                                                        ‫بونکر ‪۶۱‬د‪۱‬رابنجا «سکینا» (ز کیتا)به «‬
   ‫‪ = ۸‬زغال = ژکال = شگال = شگار » اورامانی ‪ 4« 14×02‬ا‪.‬ورامان ‪ ۸۲۱۰‬طبری‬
   ‫«اب طبری ‪٩ ۸۸۳‬‏ درلھجة بهودیان |ابران ‪ 1۵۷72 . 1082‬ک‪,‬اشانی ‪168102‬‬
                                                                   ‫‪ 280100‬س‬
                                                                                  ‫«هوبشمان ‪۲4۷۲۰‬کیلکی [‪80‬ع‪. 02‬‬
                                                                  ‫رنگه‬        ‫لره‬   ‫ز کال تس‬     ‫بشکن‬       ‫=‬    ‫‪۹‬‬


   ‫نظامی کنجوی « کنجینه ‪۹۷٩‬‏ ‪.‬‬              ‫‪4۳‬‬

             ‫‪ -۱‬از‪ :‬زکال (هم‪( + ).‬ءسیت) ‪.‬‬                                 ‫‪:‬کال (هم‪ +۳ ).‬آب ‪۰‬‬
                                                                                           ‫از ز‬                 ‫‪۰‬‬
```


## [2026-09-05T20:13:18.295Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /سکارو ‪ - ۱‬نماول/{print \"BLOCK\",NR; print; exit}' BQT_v2_pages.txt | head -80"
}
```


### [2026-09-05T20:13:19.976Z] TOOL RESULT

```
BLOCK 615
            ‫‪۱‬‬
            ‫= هی‬                                                                                                                ‫صکاد‬
‫بروزن خلاصه » نمعتی سکاسته است که‌خاریشت‬                                     ‫‌نهنده‬       ‫ت سخ‬‫سعنی‬
                                                                                                 ‫وبم‬
                                                                                                   ‫وی »‬‫نارس‬‫شم ف‬
                                                                                                              ‫اجی‬
                                                                                                                ‫لفتح‬‫و‬
                                                ‫تیرالداز باشد ‪.‬‬           ‫وستیزه کننده باشد ‪ -‬و کابوی وعبدالجنه را لیز‬
‫ده‌هی‬       ‫بروزن گذاشته ‪.‬‬           ‫‪۰ ۸‬‬        ‫سکاشته‬                        ‫کوبند‪,‬وآن سنگنیی است که درخواب برمردم‬
 ‫صکاسه است که خار پشت کلان تارنداز‬                                             ‫تیرانداز را هممیگوبند ‪۲ ۱‬‬                ‫ارشت‬
                                                                                                                           ‫خ‪-‬‬‫وتد‬
                                                                                                                               ‫اف‬
                                                           ‫باشد ‪.‬‬        ‫سکاك ‪ ۴‬ت بفتح اول‌بروزن سواد»سر کوه‬
‫باشن نقطه‌دار » بروزن‬                 ‫‪۰ 4‬‬       ‫سکاشه‬                                            ‫و فرق سرآدمی را گویند ‪.‬‬

‫کلان تبرالداز‬                ‫شت‬
                              ‫رستیکه‬
                                   ‫اا‬‫خاسه‬
                                        ‫و معنی سک‬                         ‫سکار ‪ = ۴‬بکر اول بر وزن شکار »‬
                                                           ‫باشد ‪.‬‬             ‫بمعنی زغال وانگشت باشد‪ - ۴‬وانگشت‌افروخته‬
‫صم اول‌وئالیءالف کشنده‬               ‫‪٩‬‏ =‬      ‫سکافره‬                         ‫را گیوزبند ‪ -‬و نوعی طامزام هم‌هست؛ بوقتح‬
‫را‬   ‫سازندها‬      ‫زخمه‬   ‫»‬    ‫فتح رای فرشت‬            ‫و بفا زده و‬
                                                                                                  ‫اول وضم اول همآمده است ‪.‬‬
‫بند و بعربی مضراب خواننده وان‌در قانون‬                                        ‫د نم اول و سکون‬           ‫سکار ] هنج‬
 ‫که بردست گیر ندودرعود‬                ‫اب‬       ‫استخوالی‬    ‫و رباب‬             ‫رابع وحمزة ممدوده وهای مفتوح بنون و جيم‬
                                   ‫باشد‪.‬‬       ‫وطنبور لاخن دست‬                ‫زده ‪ ,‬آهنی باشد سر کج که بدان گوشت‌ازدنگه‬
‫سکافه "‪ - ۲‬بن اول و فتح آخر که‬                                                                         ‫و ان از تنور برآرند ‪.‬‬
 ‫فه باشد بمعتی سکافره است که مضراب‌سازندها‬                               ‫سکارو ‪ - ۱‬نماول‌ورايم‌بواو کشیده؛‬
                                                           ‫باشد ‪.‬‬         ‫نان و گوشتی راگوبند که برروی زغال افروخته‬
 ‫سکال ‪ - ۱۱‬بکر اول بر وزن نهال »‬                                          ‫و اخگر بپزند ‪ -‬و بمعنی چنکالی ومالیده هم‬
 ‫خواهنده‬          ‫اندیثه وفکر باشد ‪ -‬و یمعنی‬                  ‫بمعئی‬                                                         ‫آمده است ‪.‬‬
‫وامر‬    ‫‪-‬‬    ‫‪۳۱‬‬    ‫اش‬    ‫آ مده‬
                             ‫هم‬      ‫وطلب کننده وگومنده‬
                                                                              ‫سین‬   ‫و سکون‬        ‫سکاسته ‪ -‬بن اول‬
‫بدین «منی لیز هست معنی بگو و بخواه وبطاب‬                                      ‫بی‌نقطه بر وزن کداخته ‪.‬یمعنی زکاسه ‪ ۷‬است»‬
                         ‫ویمعنی کفتگو هم کمته اند‬                  ‫‪5‬‬          ‫وآن خاریشتی باشد که خارهای خود را مانند‬
                                                                                        ‫تبراندازد و اورا عربی مدلج گویند ‪۰‬‬
 ‫سکا شش بنه بکسر اول‌بروزنسفارش»‬
 ‫بمعتی فکر و اندیشه باشد ‪ -‬و بمعنی متفکر‬                                 ‫سکاسه ‪ - ۸‬پم اول و فتحسین آخر‬

                                           ‫‪۰‬‬   ‫)‪(۱‬‬    ‫‪ ۰‬صکاسته‬   ‫صکاسه‬    ‫‪۰‬‬    ‫جکاه ه‬   ‫(ه‪.‬م‪).‬‬   ‫‪« :‬ر کاشه»‬   ‫ورك‬       ‫‪۳‬‬   ‫‪۱‬‬

     ‫‪ - ۴‬هرن ‪۲‬راازرشة ‪ 2827265[.6006728‬اوستابی‬                                              ‫‪- ۳‬مبدل«چکاد»(ه‪.‬م (‪.‬‬

     ‫وجه اشتقاق رامشکوله‬                       ‫ن‬
                                               ‫ي‪4 ۲‬‬
                                                  ‫‪۷‬ثهان‬
                                                      ‫هی زغال سوخت دااسته*اسشق ‪ ۲۷۲‬وای «‪.‬وان «هوب‬
                                                                                                ‫‪+‬‬
                                                          ‫میداند ‪ 1‬افغانی ‪rêks‬‏ (زغار) اسثق ‪YEY‬‏ رکث‪:‬سکارو‪.‬‬

                                                                        ‫‪- ۴‬بدار دلیا چون برفروخت آتش طلم‬
     ‫سوزنی سمرفندی‪« .‬رشیدی > ‪.‬‬
                                                ‫‪2‬‬    ‫آهنگه)‬      ‫(سکارو) (ه‪.‬م‪ )۰‬سل آهنج ( =‬            ‫کار‬     ‫از‬       ‫_‬   ‫‪۵‬‬

                               ‫سکالیو « رشیدی» = کلو (حم‪۰ ).‬‬                            ‫سکاروا « رشیدی» =‬                   ‫‪۱‬‬
                         ‫« رکاسه > (ه‪.‬م‪ ).‬ورك ‪ :‬سکاچه » سکاسه » سکاشته » سکاشه ‪.‬‬                          ‫‪ - ۴‬مصحف‬

             ‫‪ ۶‬شکانه» (ھ م‪ « (.‬رشدی» ورك‪ :‬سکافه‪. ‎‬‬                       ‫‪ - ٩‬مصحف‬                 ‫رك ‪ :‬سکاسته ‪.‬‬             ‫‪۸‬‬

       ‫ر دکربت‌آید‬             ‫‪۴‬‬                ‫‪.‬‬    ‫رك‪ :‬سگال‬     ‫‪- ۱‬‬               ‫سکافره ‪.‬‬     ‫رك‪ :‬شکافه »‬        ‫_‬

     ‫سکالش(ه‪.‬م‪).‬اسم‌مصدراز «سگالیدن»‪.‬‬                         ‫‪“۴‬‬         ‫رکه‪:‬گالیدن‪.‬‬         ‫همحون‪ :‬ند سکال (بدسکالنده)‬
```


## [2026-09-05T20:13:35.977Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sikār\\|sekār\\|sikar\\|skarana\\|zuġāl\\|zugal\\|skōr\\|skor\" HUB.txt | head -20; echo \"=== leaf 257 (p247) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==258' HUB.txt | head -40"
}
```


### [2026-09-05T20:13:38.403Z] TOOL RESULT

```
886:^vriSi-? (afgh. mi^ pi. fem., vri^a 'Keiskorn, vgl.
992:auf sikardan jagen' in bi-sgard zu zerlegen und auf
2656:742. Unsicher. Darmesteter iibersetet garemoskarana-
2808:786. Dazu afgh. LW. skOr 'hunting, chase, prey', kurd. LW.
2810:'a hawk, falcon' = np. sikara, sakara 'Jagdhabicht'.
2811:Vgl. arm. sakr u. s. w. ZDMG. 46, 266. Np. sikar
5556:(oben p. 30), vgl. np. sikar *Jagd*, sikardan jagen , phi. v(i)skar
6059:(Vullers: iskira) *Jagdhabicht* = sikara, u. s. w.
6084:Wrzl. skap; sikdr 'Jagd*, sikardan jagen'; sikuftan 'auf-
7824:'neidet* (oben p. 13) ; jask H. 421 ist unsicher, ebenso sikar
8492:skenda-; sikaftan *spalten H. 787, oben p. 80; sikar *Jagd'
8493:H. 786, oben p. 80; sikar 'Kohle H. 742, oben p. 76u.s.w.;
10737:sikar 80.
=== leaf 257 (p247) ===
— 247
§ 139. Ap. g nach Vokalen und r = y bleibt im
Np. als }': mury 'Vogel' ^= zd. mereya-; mary 'Wiese'
(oben p. 98) = zd. mareya- ; may profunditas*, mayak
Grube* H. 985 ■= zd. maya- Xoch*; muy^ may *Magier
= ap. magu' (= tnayii'); mey *Wolke* = zd. maeya--^ arDy,
aroq 'Rulpsen', gr. iotvyo^iai; dyardan 'deglutire'? H. 36;
t^y 'Spitze, Schwert', zd. bitaeya- 'zweischneidig* ; juy, yOy
* Joch*, skr. yiiga- ; dtirdy 'Luge = ap. drauga- (= drauya-) ;
day 'Brandmal, Fleck, Wunde, Brenneisen, zd. daya-; doy
saure Milch*, skr. duh melken, 3 pr. dOgdhi ; royan 'Butter,
Oel' = zd. raoyna-; vazay *Frosch* = zd. vazaya^\ varg,
hary *Wasserwehr = skr. varga-: bay (in Baydod Name
der Stadt = zd. bayddata- gottgeschaffen*) = ap. baga- {baya-),
phi. inschr. bagJ {= bay); paiydm *Botschaft\ arm. patgam
= ap. ^patiyama-; BcLdyes , arm. Valgus ^ zd. vditiga^sa-,
ap. *vatiyaisa', Np. sayal =■ sagal ^) (A. M. 84, 10) 'Schakal*
ist LW. aus dem Indischen = skr. grgdla^.
Also np. deg Kochtopf aus ap. ^daika-? Siehe oben
p. 65.
Die Armenier hatten den Laut y nicht, sie setzen
daher g fiir persisch g und y:
marg 'Wiese, Aue', mog *Magier , tSg 'Spitze der Lanze*,
bag Antheil, Erbe' ^= zd. baya-, paz. bag 'Theil, Antheil'
Min. kap. 27, 70, skr. bhaga- 'Antheil, Erbtheil'; fag 'Krone',
syr. tdya, np. taj, ap. *^6lya-; patgam 'Botschaft* = np.
paiydm; VatgBs (EliSe 139) np. Badyes.
Np. may ein Wasservogel* = skr. madgu- kann auf
ap. *ma^yu- zuriickgehen, da g nach der Spirans J zu y
geworden sein kann, vgl. zd. duy^ar- 'Tochter (gd. dugdar-);
dagegen kann mayz 'Gehirn' = zd. mazga- nicht auf ap.
^mazya- zuriickgefiihrt werden. Wurde schon ap. mazga-
in "^magza- = ^mayza- umgestellt? Np. taj 'Krone' ist
arabisirt aus tay. Np. jihan 'Welt' kann nicht arabisirtes
gehan sein , da Jifian im Arabischen nicht vorkommt. So
bleibt jihan, besser jahan, zunachst dunkel.
*j Wechsel von y und g bei VuUers, Gram. p. 31.
```


## [2026-09-05T20:13:50.310Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2650,2670p' HUB.txt; echo \"=== BRT daga- ===\"; grep -n \"daγa-\\|dagfa\\|daya-  m\\|'Brandmal'\" BRT.txt | head -10; echo \"=== BRT garemo-skarana ===\"; grep -n \"garemö.skarana\\|skarana\\|garsmö\" BRT.txt | head"
}
```


### [2026-09-05T20:13:50.410Z] TOOL RESULT

```
zu np. surUn JRAS. 1894, 469 aus *8rdn ist mir unklar.
740. Zu streichen, da die Etymologic fehlt. Vgl. Horn
p. XI, Anm.
741. Beachte, dass anl. s vor Vokalen im Neupersischen
nicht = idg. s sondern = idg. k^, k% sk^, 8k% ist.
Im Uebrigen sind ja die Bildungen „onomatopoetisch".— 76 —
742. Unsicher. Darmesteter iibersetet garemoskarana-
diirch *une paire de pinces', skairya* durch campe-
ment'. Np. nigdl gliihende Kohle belegt Noldeke
aus Shahname III, p. 1508, v. 214. *Kohle* heisst
ausserdem auch angi^t (Nr. 126) und zuyaly {zuyOl i sang
*Steinkohle* Rosen, Np. Sprachfiihrer p. 35). = jiid.
tat. zugol^ zuwol (Miller p. 69), kas. zugol etc.
743. Gitay^a ist medisch, aber nicht altpersisch. Gerade im
Altpersischen ist s fiir sp einigemal bezeugt {visa- =
vispa-^ asa^) *Pferd' = aspa- u.s. w.), daher die Dialekt-
formen mit 6, v wahrscheinlich nicht der Persis (ap.
^saka- = np. sag *Hund') angehoren.
744. Afgh. sk&n (= *5fcar«a) und skun (= "^skurna). Die np.
Formen gehoren verschiedenen Dialekten an.
745. Zd. safa- = skr. gapha- lasst sich schwer mit np.
=== BRT daga- ===
12795:•  j.  daya-  m.  —  ?— :  paityänm  ake  frä-\ lünniat  atirS  mainyus  skaillm  (sd.)  yqm gavaca  'yaca  pouru.mahrkfm  V.  7.  4''.
14947:•  j.  paiti.daya-  m.  i)  'der  die  Aufsicht führt,  Beaufsichtiger':  tiltrJm  ..yim  ratäm 'daimca'^  vTspaesqm  stärqm  frada%al ahurO  mazda  ya%a  narqm  zardiuftnm Yt  S,  44.  3)  'Erkennungszeichen,  Merk- mal' (?,  nur  Komp.).
29425:•  j.  hamaspa^hnaedaya-  m.  Name  der Gottheit  der  sechsten  Jahreszeit  und  des an    deren   ^de    gefeierten    fünftägigen
=== BRT garemo-skarana ===
26467:•  j.  skarana-  Adj.  (fem.  'na-)  'rund': aiibAa  z^ms  yal  pa%anayä  (sd.)  *nayS dBraiparayä  Yt.  10.  95;  5.  38,  J7, 19,
```


## [2026-09-05T20:14:11.155Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN dag ===\"; grep -n \"^ *5[0-9][0-9]\\. dāġ\\|dāġ\\|day 'Brandmal\\|'Brandmal\" HRN.txt | head -20; echo \"=== IEC geul/gul coal ===\"; grep -n \"^geul\\|^gul\\|^g.eu-lo\\|coal\" IEC.txt | head -30"
}
```


### [2026-09-05T20:14:11.239Z] TOOL RESULT

```
=== HRN dag ===
4759:529. däy 'Brandmal*, dey.
=== IEC geul/gul coal ===
542:angólos (angol-, angil-, angl-), is, iə “coal, coal fire’. WP I, 181 Skt. ángarab; Ir. aingeal, pl. aingle “fire, hearth, cinder; W engyl "Drei: OCS ogli ‘coal; Li. anglis; Latv: ogle, pl. id. The con- nexions of Alb. thëngjill ‘coal and OHG kol, kolo, id. with the above forms are not clear.
3967:geugil- (geugol-) "carbon, slag, coal. Ir. gual ‘coal’; Ukr. ZuZli, pl. ‘cinders’; Pol. żużel ‘slag’; R cf. ZüZelica, id.; Slovak ZüZol ‘coal; Slovene ZuZel ‘wood soot, charred matter’
3972:geul- (?) (1) ‘wrapping, garment Per cf. zaulàne, zawalane ‘fetter’; Zülam "be entangled’; Icel. kjóll ‘dress, coat’; Norw. kjole ‘frock’; Du. kiel “blouse, overall’. (Iso- phonic are Big. žulja ‘rub, abrade; importune’; žule “invalid”; R Zülik ‘cheat’)
3974:geul- (3) “lump, knob, ball’. (Variant: goul-) Skt. golah, golà ‘ball’; Per. zaure ‘backbone’; zawale “lump of leaven’; MHG kiule “stick, club’; Srb. Zülj ‘tumour, callouse'
3985:geul- HG gius, io
4067:gleud- “split; cleavage; fissile’ OE cleot ‘medicinal plaster; scroll" beside (o-gde) E cleat ‘batten; line of cleavage in coal’; Li. gliaudüs ‘fissile’; gliaudas, m. ‘pod, husk, shell; gliáudyti (crack open’, tr.). See gloud-
4467:gul- ‘throat, gullet; gorge, ditch; swallow- ing’. Cf. gulgó, gulgul- Arm. kul ‘gorge; gulp’ beside klanem *swal- low, devour’; Lat. gula; gulo ‘gullet; glutton’; Ir. goile ‘maw’; Blg. gálka ‘mastoid’. (Per. gulü ‘throat? derives from gurgət-, q.v.). Variant (*gūl-) in MHG kūle, LG kūl, OFris. kūle, Du. kuil, G Kaule & (dial.) Kuhle “hol- low, ditch’.
4469:gulg- (gulgu-) ‘gulp, gurgle; belch’. See gul-, gulgul- & glgos Per. (ambig.) gulū (2) ‘gurgle; Arm. cf. klklunk' (redup.), id.; Alb. gullgulloj ‘babble, purľ; Lat. cf. in-gluvies ‘craw’; Ir. glug ‘gurg- le’; MHG kolc, gs -kes ‘whirlpool’; G Kolk, id. cf. Kolk-rabe, wm. ‘caw-crow’; Du. kolk ‘whirl- pooP: OFris. kolk ‘ditch’; Du. cf. kolken, v. ‘ddy’; OE cylcan ‘belch’; Slovak (LW fr. Slovene) gl-gotat ‘gulp’; glg, m. id.; Pol.
4472:gulgul-, gulugul- ‘gurgle’. Cf. gul-, gulg-. WP I, 683 Per. yulyul ‘clamour’; Arm. klklunk, s. ‘gurgle’; Alb. gullgulloj, v. ‘purl, babble’; G cf. kluckern ‘bubble out of a bottle’; Blg. gălăgăl ‘bubble- bubble from a bottle’
4473:gulos, ios ‘ball’. See gūl- & cf. WP I, 556 Skt. gulah, id.; Oss. gurä ‘mass’; Gk. gullós *gaming-die'; Alb. gul (3) ‘blockhead’, fr. *eulis; Du. kul (‘phallus’, fr. *gulis)
4474:gulquios, iə (?). See next, and cf. guluk- Alb. gulçë ‘asthma’; Big. gălč ‘din, bluster’
4475:gult- (gult-?) ‘gulp’. Cf. glut- (1) Arm. cf. hec-kltam ‘sob’; Lat. cf. sin-gultio, id. (sin- unexplained); Blg. (ambig.) gáltam ‘swallow’; Cz. (ambig.) hitit, id.
4476:gulugul-, see gulgul-
4477:guluk- (glk- w. u-basis) ‘gulp, gurgle’. Cf. gulquios Sw. cf. (with n-infix) klunka, v. ‘gulp’; OCS glükü ‘gurgle’; R golk, id.; Blg. glác (din, bluster’, fr. *glukios, *gulkios, or sim.); Cz. hluk, id.
4481:gulgul-, gulugul- — gungul-
5087:ghuros ‘outflow, filth, matter’. Cf. &huuo (1) (For Gk. i-khór *gore, matter, serum', see uis and ghuuo); Lat. (?) dial. foria (‘thin excre- ment’, for *horia?); Ir. gur, gor ‘pus, abscess’; Br. gor, pl. -iu, f. abscess; W gori 'suppura- tion’; OE gor, gyr (dirt, mud’; E gore; G Gur ‘dung; filthy water from coalmining'; ON gyrja (bloodstain': Lat. foria?); Sw. gorr ‘pus’; OCS cf. voz-grja (ómucus', fr. uos-, q.v. + ghurio); Cz. voz-her, m. ‘mucus, snot
5238:guluətos, à ‘life’. Cf. guita, is. WP I, 670 Skt. jivitáh, adj.; jivitam, n.; Gk. bíotos, bioté; Gaul. biviton- (in proper names); W bywyd “life? beside bywed “core, pith’; Br. cf. bivid-ik ‘lively’; OCS Zivotü "life; R Zivoót ‘belly’; Li. gyvatà
5240:guluið (guiuiio) ‘enliven’. Cf. guiuos, etc. Av. jiv- (live. See next); Per. zibidan, inf. ‘adorn’; Go. ana-, ga-qiujan; OCS Zivljo, živiti
5241:guluó ‘live’. See next Sk. jivami; Av. jiv- beside jvai(mi); Tokh. B Sau, $ai; Arm. keam, aor. keçi; Lat. vivo, ére; W byw, v.; OCS and com. Sl. Zivo Ziti; Li. cf. gyveni, -énti beside gyvuoti; Latv. cf. dzīvot, inf. id.
5243:gulaguos, å (?) “harm, injury” Gk. (ambig.) blábos, blábe; OE clacu, id.; OFris. klaki 'complaint
5244:gulaisos, ios ‘stammering, lisping’ Gk. blaisós (2); Lat. (LW?) blaesus; W cf. blo-
5255:gulen- (expressive variant: gulenn-) ‘mucus, slime’. WP II, 288. Cf. glinos Gk. blénna, id. (expr. as in Hes. glítton, Lat. lippus, Gk. tatta, etc.); MIr. blinn *gpittle'". (MHG kl&n- cpds. ‘daub’, kl&nen, v. id. ambig. cf. glin-. OCS glénü ‘mucus’ represents a type *egloin-)
5257:gulbh- ‘deep, depth’. Cf. guelbhos, a and gulg- (gulgu-) Oss. Kurf, Dig. qulf ‘deep’; Slovak cf. hÍb-ka, hlb-ina ‘depth’; Li. cf. gilüs ‘deep’. Isophonic is Gallo-Lat. galba (fCpotbelly', lit. ‘stomach’ or “belly”? cf. guelbh- for the semantics. For speculations on Lat. volva, vulva, volba, vulba see WH:LEW & EM:DELL)
5258:guldos, à, ios “full to bursting, bulging; fat animal, well-fed beast Gk. cf. bladá, npl. *unripe fruit; immature ani- mals’; blázo ‘play the fool’; OE colt, as E; Sw. kult ‘piglet; strapping youth’; kulta ‘plump little girl’; Norw. kult ‘block, stump’, also ‘strapping youth’; kulten ‘stout, thickset'; Li. gvildis, gs -dZio, m. ‘ripeness, bursting-point'. (The contradiction implied in Gk. is not pre- sent in Gk. blastós *shoot ; bláste, id. & “birth, increase”, from a type *gulst-, with the vocal- ism of OE cwylía ‘spring, source’, cf. MHG qué&llen ‘swell, burst forth, grow’. A Gmc. type *quulst- > *kwolst- does not occur)
5259:gulguis, à *turning-point, pivot, hinge; aim, target". ; Gk. balbís *turning-point, goal’; Lat. valvae (folding doors’. IE *-]- > Lat. at before lab- jials, cf. palpare, palma, balbus, salvus, as Sr. Lat. -ar- before labials in carpere, sarpa. The semantics are those of Umb. vereia- door and Cz. vefeje *doorpost'); ON kylfa,
5263:gulio (1) (guol-) ‘strike, cast, hurl, beat down’. WP I, 691. Cf. guelo (1) & (2) and next Hitt. hulahi (strike, for *hwul-); Gk. bállo (1) “throw, strike’; MIr. buille, s. “blow, stroke” beside balim ‘die’; Br. balya ‘beat’; OE *cyl- lan ‘kill’ beside cwellan, id.; Norw. kyle ‘fling’ beside kvele, p.t. kvalte ‘choke’; MHG koln “force, torture’ beside queln, id.; Cz. cf. ná-hly ‘sudden’; Ukr. na-hlo ‘suddenly’; Latv. gulstu, gult (2) “attack?
5264:gulið (2) (guló, gulnu-) “fall, sink, lie down’. Cf. WP I, 639 Skt. cf. glami, glayami ‘be limp, flop; Arm. on-kInum ('sink', fr. *en-guInu-); Gk. bállo (2) “collapse, fall; ON cf. kylli-flatr, adj. *pros- trate’; Li. gulü, gulti “lie down’; guliü, éti ‘lie’: Latv. gulstu, gult (1), id.; gulu, et ie’; guius *]Jying"
5266:gulmos (1) *hollow; depth'(?). Cf. gulos Hes. cf. balmós 'chest of the body'; Li. gilme ‘depth’. (Lalis)
5267:gulmos (2), (guolm-) ‘evil, sorrow, pain’. Cf. guelo (2) & guolm- Oss. qurmä ‘anxious; anxiety’; Alb. gulm (1) ‘sorrow’. O-gde in MHG qualm ‘anxiety qualm’; OE cwealm; EME qualm (also ‘nau- sea’). A zero-gde alleged G dial. Quulm is hy- pothetical
5268:gulnos, iom, 'gulnd- (gulnd-), gul- ‘acorn’. WP I, 692 Per. (?) girdü ‘nut’; Arm. kayni, -vo, -eav (“oak. But for kayin, gs kayno ‘hazel’, see koslo-, ko- solo-); Gk. bálanos, balánion; Aeol. (alleged) galanos; Lat. glans, gs glandis; Alb. l&nd, léndé (facorn" may be a LW fr. Lat.); OCS zelodi, Let m. (and com. SL Pol. zoladZ, f.; Li. cf. gile; Latv. ozol-zile, id.
```


## [2026-09-05T20:14:22.605Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 542 3967 3974; do echo -n \"line $L leaf \"; awk -v n=$L 'NR<=n{if(/\\f/)c++} END{print c\" -> approx p.\"(c-15)*2}' IEC.txt; done; echo \"=== leaf 204/205 (p ~379) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==205' IEC.txt | head -12; echo \"=== leaf 218/219 (p~407) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==219' IEC.txt | head -12"
}
```


### [2026-09-05T20:14:24.775Z] TOOL RESULT

```
line 542 leaf 23 -> approx p.16
line 3967 leaf 158 -> approx p.286
line 3974 leaf 158 -> approx p.286
=== leaf 204/205 (p ~379) ===
d’; Swed. gump ‘rump of birds’. For OCS gọba, Li. gumbas, see gumb-
ghumbho ‘bend, incline, lie down’. Cf. ghubh-, ghoubh- Arm. gmem ‘lie down’. Loss of *-bh- as in ca- mem ‘chew’, see ĝombh-); Li. gumbu, gùbti, intr. ‘bend’; Norw. Sw. (ambig.) cf. gubbe “old man’
ghundhos (ghundholos), à “lump, ball, tu- mour, pile; balled, lumped’. WP I, 588. Va- riant: ghund-. Skt. cf. hundih, m.f. Jump, heap’; Av. gundo ‘round loaf; ear of corn’; gunda ‘round loaf; Per. gunde, adj. ‘thick, coarse’; Arm. gunt, gs gnto beside gund, gs gndi, abl. gndav ‘bali, mass”; Gk. cf. kolo-künthe (“pumpkin”, lit. “big ball); OHG cf. gunde-réba, f. (“ground-ivy” because used against goitre). Extns. in Per.
349
gundule ‘lump, mass’; Li. gunkla, gunklas Jump, bump’. Cf. further the Gk. name Kún- thos “a mountain at Delos, said to overshadow the island”
(ghungh-, see gung-, WP I, 638
ghunghulos, à (an arthropod’. Cf. gung-. (Oss. & Blg. ambig.). Cf. WP I, 673 Oss. gongoli (dungworm'; Gk. kogkhule (“mussel or ‘cockle’, if not an extn. of kógkhe *shell); Blg. dim. gágliak *woodlouse
ghür- (ghurs-?) “rough, raw, harsh, forbid- ding Arm. cf. gof ‘fierce, grim; verve’; MIr. & Ir. gúr "keen, sore’; Fris. goar ‘clammy, raw, soured'; Du. goor, cpds. gor- ‘sour’ beside guur ‘raw, rough, severe’; Icel. gor-, cpds. *bad-'; Li. cf. güru, inf. gurti ‘crumble, waste away’; guras ‘curmudgeon’. A possible *ehurs- is reflected in Arm. gor and in G Gur- re ‘jade, nag”
ghurgh- (1) ‘stir, stimulate, poke’ Arm. grgem ‘fondle, pamper’; cf. grgank ‘plea- sure’; grgir, gs grgri, i-st. ‘incitement, prurien- cy’ beside Mod. Arm. gurguram ‘fondle’; Alb. cf. gërgoj ‘urge, provoke’ beside the LW gër- gás, id. fr. S1.; Srb. grgati, inf. ‘poke w. tooth- pick’
ghurgh- (2), ghurghul-, ghurghur- ‘throat; gurgle’. Cf. gurg- (2), gurgul-, gurgur- Arm. grgram (and grgam) ‘croak, cackle’; Gk. korkhuréa ‘sewer’; Alb. (ambig.) gurgulloj (gurgle, etc. See gurgul-); MHG gorge ‘throat’; Du. gorgel, id.; gorgelen ‘warble’;
ghungh- — guabhro-
10
=== leaf 218/219 (p~407) ===
 ‘hear’ O-gde in Skt. garha “abuse”
gurdh- (2) 'stir, rouse'. Cf. gurgotio Gk. brásso, aor. ébrasa; Alb. cf. ngrydh (stir up, foment': Gk. embrásso ‘cast up’ ofthe sea)
gurdhlom, gurdhrom, à, ios, iə ‘crop, throat, gorge, gorging animal Skt. grdhrah ‘vulture’; Gk. bárathron ‘gorge, abyss’; OCS grülo, Zrülo, n. ‘throat’; Pol. gard- 1o, Cz. hrdlo, wd R górlo, id. beside Zerló, Zérlo ‘mouth’; Li. gurklys ‘crop, adam's apple; bottleneck’; Latv. cf. padzirkle ‘throat?
gureió, gurið, see gurð (2)
gurgont- variant of gurgot-, q. v.
gur- —gurio
10
20
25
30
35
40
```


## [2026-09-05T20:14:35.182Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### leaf 220\"; awk 'BEGIN{RS=\"\\f\"} NR==221' IEC.txt | head -20; echo \"### leaf 234\"; awk 'BEGIN{RS=\"\\f\"} NR==235' IEC.txt | head -20"
}
```


### [2026-09-05T20:14:36.841Z] TOOL RESULT

```
### leaf 220
ignified’; gúroti ‘be heavy, lumber along’. Cf. WP I, 685 and guruos
guruos, ios ‘strong’. Cf. gurus, etc. Arm. kar, i-st. (2) ‘power’; karem, karenam "am able’; karık, pl. “means, supplies, rein- forcements'; kari ‘excessive; very’; Gk. cf.
guruidh- — guhaueió
15
378
brierós, briarós ((strong', fr. *gur + *isoros, q.V); W bryw ‘vigorous’; Li. cf. gurbti, v. ‘thrive’; gurbüs "luxuriant? -gus, suffix in Gk. prés-bus, Cret. preis-gus; Li. Zmo-gus (earth-dweller' hence: *man?); cf. Li. guvüs lively’ (gutā, cf. guetu. Z-gde only in OE cwudu *chewing-gun, cud’: Icel. kvoóa ‘gum, resin’) guüd- (guoud-, güd-) “a hooting bird’. Cf. güd- and next Gk. büza 'eagle-owl; W cf. buddai ‘bittern’; MHG kūz, kütze, s & wm. 'screech-owl; OE cyta ‘bittern’; E kite; Norw. cf. kyte, v. ‘bray’ guüt- (guout-), variant of guüd-, guoud-, q. v. Gk. cf. boütalis ‘nightjar or sim? ; Lat. büteo, bütio ‘buzzard’
Guh
(N. B. Much of the evidence for IE initial *guh- is ambiguous)
guhaidros, à “bright, clear; brightness’. Var- iant: £uhaidros (?) Gk. phaidrós; Thrac. cf. Gaidreas (a name: Gk. Phaidros. Krahe); Li. gaidrüs, giédras, id.; giedra, giedrà “bright weather”. Z-gde in Latv. dzidrs “bright, clear”. A possible variant is sug- gested in R zvézda ‘star’; Li. ZvaigZdé, Latv. zvaigzne, id. as against Cz. hvézda, id. (See Supt. gaidros and cf. SEM:AIE: § 53: kajtar)
guhak- (or guhak-?) Alb. gacé ‘ember’; Lat. fax, gs facis ‘torch; sun’; variant (?) in Li. Zvake “candle; sparking plug’. Cf. guhak-
guhäl-? ‘crooked, awry, amiss, wrong’. Cf. squhal-. Evidence ambiguous Skt. hváre, mp. “am crooked'; Gk. cf. phëlos (if Doric *phàlos) ‘deceitful’; Lat. fallo, Gre (if for *falno. EM & WP uncertain); W gal (?) ‘enemy’; Ir. galann, id. (Cf. EM: DELL: p. 381; WH:LEW p. 447-8; and Hes. spheló- ‘askew’, if s- is a px.)
295
30
35
40
45
guhalətios, guhol- (?) ‘mill Skt. gharattah; Pahi. gurtà; Arm. Éayac, -K, id. beside ğayğax, adj. ‘crushed, shattered"
guhalk- (?) ‘sickle; sickle-shaped claw? Hes. phálke (*^harpy', given as "bat" For hárpe: *falcon' and ‘sickle’ see srp-); Lat. falx, gp falcium ‘sickle’
guhas-mi ‘eat, devour’ (?). The evidence is ambig. Skt. ghasmi eat" beside bábhasmi (root: bhas- *devour make equation w. Lat. fames “hun- ger’ uncertain (*guh- or *bh-?). Specs. in WPI, 548 & 829
guhaueio ‘favour, befriend, watch, heed, care for’. WP I, 144. Cf. ghoueio. The Sl. and Li. evidenceisambiguous. Oss. (?) qavin, éävun ‘intend’; Lat. faveo “favour, be- friend, attend in silence); Umb. cf. fons, prs. pt. (propitious': Lat. favens); (ambig.) OCS govëjo ‘revere’; OCz. hovéju “care for, favour”; R govét, inf. “prepare for sacrament, fast'; Li. (ambig.) gaviù, éti ‘fast’; Late gavéju, id. (Gk. thops, gs. thopós ‘flatterer’; thópto, v. ‘flatter’ seems to rept. a form *dhàu-oqu-.
### leaf 234
, zəntus ‘knowledge’; Oss. zond, id., zind ‘known’; Go. kunpi; kunps; OHG kunt, pp.; MHG kunde, künde, s.; OE cypp, s. beside cüp, pp.; Li. cf. pa-Zintis, f. *acquain- tance’; Latv. zinte, f. *witchcraft
?obho, ið ‘peck, poke, stab, obtrude’. WP I, 575 Skt. jábhe; Ir. gobaim; OE be-caefian (‘adorn’. Semantics obscure); E to chaff ‘tease’; LG cf. kawweln “quarrel'; kaffeln ‘crunch’; OCS zo- blo, zobati "eat": Cz. zobat ‘peck’; Li. (de nom.) Zabóti “fix bit in horse's mouth’; žab- ángai ‘trap’; pà-Zabas “wing of trawling-net'. See next Å
ĉobhos (1) ‘sharp twig, beak, spike’. Cf. WP I, 570 and gobho, io, gabh- Ir. gob ‘beak, snout; G Kebe ‘jaw, gill’; Cz. zob ‘beak’; Li. žābas, à, mf. ‘twig’
ĉĝobhos, is (2) ‘chickfeed, chaff OE ceaf *chaff; MLG kaf, Du. kaf, LG kaff, id.; OCS. R zobi, Srb. zob *oats'; Blg. zob ‘horse-fodder’
$obhul-, gobhlio- (variants of ĝobhos (1), q. V.). Ambig. cf. gabhəlos
$nmros — Gon-
15
20
25
30
35
40
45
404
OE cf. cæfl ‘muzzle, halter’; ON kefli “peg, gag’
2oibos (?) ‘twist, bend’ Per. ziv 'ship's worm; deceit’; Icel. keipar, mpl. ‘whims’; keipa, v. bend to an angle
(Gol see gel-). WP I, 623
ĉombos, is, us (1) ‘tuft, bush, head of hair Skt. jambüh, f., jambu, n. *rose-apple & tree"; Arm. cam, i-st. “head of hair’; cf. also camuk, dim. *pasque-flower'; ON kampar, mp. *whis- kers’
gombos (2) (?) “side, face? ON kampr, m. (2) “facing wall’; Li. Zambas (2) “side, lap of garment
gombho ‘show the teeth, chew, bite, stab, snap'. WP I, 575. See next, and cf. gembh- Skt. jáàmbhe ‘snap at; Per. zimam, zámidàn ‘chew’; Osset. zimbín ‘yaw; Arm. camem ‘chew’; Gk. denom. gomphóo ‘nail’; E dial. to cham ‘to chew’; Cz. zubit se “show the teeth, grin’; Big. zábja se “bare the teeth’; Li. Zámbu, Eti shoot, sprout
```


## [2026-09-05T20:14:52.704Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 236 237; do echo \"### leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | head -14; done"
}
```


### [2026-09-05T20:14:54.669Z] TOOL RESULT

```
### leaf 236
rth". Cf. &en-, -£nos (1) Skt. jánah, jana; Medic (in OPer.) zana- "man: Myc. -kono-; Gk. gónos, goné; Icel. cf. kenjar ‘whims’ (?)
9onu, see genu
gor- (1) ‘ripe, old, mature’. Cf. ger-, gordos, $aros . Arm. (?) car, o-st. ‘tree’; OCS cf. sü-zorí ‘ripe’; OCz. s-zoliti, v. ‘ripen’, tr; Li. Záras “dry twig’; pl. ‘stubble’; (Latv. zars “branch, twig’? to ĝaros, q.v. Li. is ambig. also)
g0r- (2) ‘gleam, glow’. Cf. gér- (1) Cz. zora, zote ‘dawn’; Pol. zorza, id.; Li. Zarà *gleam, glow’; Cz. cf. (long-gde) záře, OCS zar- ja ‘radiance’
$or- (3), £oros ‘hollow, basin, depression, valley' Arm. cf. cor-cor, o-st ‘valley’; MHG kar “bowl; hive; clough, hollow in mountainside’; ON ker “tub, goblet’, cf. also kerald ‘tub’
?ordos (?), see ger-, gor- (1) OE ceart ‘rough land’; E chert ‘siliceous sedi- mentary rock’; Li. Zárdas (‘drying-rack; island; granary’. Basic mng. obscure); Latv. zards ‘drying-rack’
ĝounos ‘chap, jowl; gill’. Form of ĝeunos, q.v. and cf. ĝenus Du. koon (jaw, jowl’; dial. ‘gil’); Li. (e-gde in view of Latv. ž-) žiáuna ‘jawbone’; pl. ‘gills’; Latv. Zauna ‘gill’. (Du. -00- is fr. Gmc. -au-. VW:EWNT)
$rnàtos, -itos ‘grained, of grain’. Sce grnóm Alb. i grynjtë ‘wheaten’; Lat. grānātus ‘granu- lar, grained’; It. granato, id. and ‘robust’; gra- nito ‘robust’; s. ‘granite’; OE cyrnod; Norw. kornet; Cz. zrnatý & zrnitý ‘granular
grndó(n) granular formation. Cf. grnóm Lat. grando, gs -dinis "hal": Ir. gráinne “granu- le
$rnóm “cultivated grain, corn, staple grain of the country’. WP I, 600
$onà — gustos, is, us
10
20
25
### leaf 237
; Per. düst ‘friend’; Lat. gustus, üs ‘taste’; Olr. gus ‘bravery’; mod. “desire, feeling, nature’; Go. kustus, m. *samp- ling’; ga-kusts, id.; OHG kust, Let f. ‘choice; virtue; MHG ‘trial, measure, state? beside kost(e) “food”; OE cost, adj. “tried, chosen’; m. ‘choice, manner’; ON kostr, pl. -ir, m. ‘choice, food, virtue'. (An unexplained variant appears in Per. guzam, -idan ‘choose’; Cz. hezký, adj. “pretty”, fr. *gu$-). OE cyst, f. as OHG. WP I, 568
$ueigo, ið ‘squeal, squeak’ G quieken; Li. žviegiù, “ti, id.
£ueir- (ĉuoir-) ‘screw up the eyes, squint’ MLG quieren, id.; Li. žvairiù, éti, id.; žvaīras, žvairůs “crosseyed”
$uél- (gul-) “burn; burning, bright, clear’. Cf. WP I, 643 Skt. jválami, jváråmi ‘burn, blaze’; jvaláh ‘flame’; jvàlà, £. id.; (z-gde in jürnah “burning”; jürníh ‘blaze’); Per. zuyal ‘embers’; Hitt. (queried) hwallis ‘embers’; Gk. cf. deíle “after- noon’; déletron ‘torch, lamp’; (z-gde in OHG chol, kolo “coal? and com. Gmc. cf. ON kol ‘coal’; Oss. àvzali, Dig. ávzalu, s. id.)
£uenghó, ið “sound, resound, echo, howl, whine’. Variant; &uhengo, io, q.v. (O-gde &uongh-, guhong-) G (o-gde) cf. quengeln ‘grizzle, whine’; OCS zVego, zvesti ‘sing’; R zvjàgat ‘howľ; Li. Zvén- giu, -ti ‘neigh, whinny’ beside (o-gde) Zvangüs singling’; Zvangü, -éti ‘tinkle, jingle’; Late zviedzu, inf. zviegt ‘neigh, guffaw’. Variant (*&uheng-) in Gk. phthéggomai ‘sound, sing, neigh’; o-gde in phthóggos ('sound, voice", A further variant of type *&uenk- occurs in OCS zvekü “sound” beside zvokü, id.)
£uigio ‘squeal’. Cf. gueig- Arm. éCem, id. beside Cic, Let and Cáo, o-st., id.; G (ambig.) quieken, id.; Li. Zvygiü, ti be- side Zvigsiu, -sëti, id. (Gk. sízó represents a variant of type *Kuigio)
$uilo, io (?) “drip, drop’ Du. kwijlen ‘dribble’; Li. Zvylu, Zvilti ‘sag, droop’. (Isophone: Latv zvilot *glitter')
Gul. see guel-
$uoir-, see £ueir-
(&uhaidros, see guhaidros and Supt.: gai-
£ueigo, ið — guhis, 2uhus
20
25
30
```


## [2026-09-05T20:15:09.947Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"guheguh\\|guhegu\\|guhogu\\|guhog\" IEC.txt | head -10; echo \"=== leaf 221/222 p379-380 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==222' IEC.txt | head -20"
}
```


### [2026-09-05T20:15:11.533Z] TOOL RESULT

```
2734:dheguhlos, is, ö(n) “burning, heat, radiance’. Cf. dheguhó, dhoguh- and WP I, 849 & 865. Cf. also guheguh- Alb. diell ‘sun’; MIr. del, dellrad ‘brilliance’; Ir. dealán, m. ‘burst of sunshine, brightness,
2737:dheguho (dhoguh-) ‘burn, fire’. Cf. dhe- guhlos, dheguhro-, dheguhto- and guheguh-. WP I, 849 Skt. dahàmi; Av. daZai-; Tokh. A tsak-; AB tsák- (also ‘bite, sting"); Alb. djeg, aor. dogja (fr. *dheguhiou, cf. Li. degiaü) beside n-dez (*kindle', fr. *dhoguheio, a factitive); MIr. dóim, Ir. dóighim and dóghaim (cf. OLi. degmi); Br. devi, pp. devet; Cor. dywy; W cf. cyn-neu ‘kindle’; cyn-ne ‘burning’ beside OW deifaw 'roast; Li. degü, OLi. degmi, inf. dégti; Latv. degu, dedzu, inf. degt. Lat. foveo, tr ‘warm’; fomes, -mitis (for the second element "wood cf. termes, trà-mes) seems to represent o-gde factitive
5212:gui£0, io “burn, sting’. Cf. giĝö (2). (The Arm. and Sl. evidence is ambiguous) Arm. kcem ‘prick, sting’; kic, gs kco “bite, sting’; Alb. xixë, f. ‘spark’ (fr. *guigio); Lat. cf. (?) -villa in favilla “hot ember’; Pol. gzié sie “be in heat’; gzik 'cattle-fly'; cf. also giez, pl. gzy ‘gadfly; libido'; o-gde in Arm. kajc, i-st. ‘spark’; kez ‘brazier’; kizem ‘burn’; Alb. zeg- th, dim. ‘gadfly’; ON kveikr ‘wick’; kveikja, f. *kindling-wood'. Arm. ambig. as also Li. giež- ti, v. ‘tch’. For gaiZüs ‘sour, irascible’ see goig-. A variant occurs in Li. ZieZerka, ZieZirba “spark”, and OCS Zen Zígati ‘kindle, burn’; though the relationship, if any, w. Zego, Zesti, id. is uncertain. Cf. guheguh-, & guoi?- below.
5472:guheguh-, assimilated radical, form of dhe- guho, q. v. Cf. WP I, 849 Per. cf. zuyal, *zayal *'embers' beside gazam ‘sting’; Oss. dzagü “hot poultice’ beside qäzäl ‘charred matter’; Alb. cf. zegël, zegth ‘gadfly’; OCS Zego, Zeët ‘kindle, burn’; Zegü, žega “heat; Cz. cf. Zehadlo ‘sting’; Pol. zegadto ‘red-hot iron’; Cz. Zehlice ‘flatiron’; Slovene žežel ‘poker’. (An R-gde w. i-basis seems to be present in Gk. thibrós ‘roasted, hot, ten- der”, cf. OCz. Zhu, Zéci ‘kindle’ and OCS Z1Ze- nije ‘burning, inflammation’. Gk. type *guhï- gu-)
5473:guheguhon-, redup. theme of guhen-, q.v. Vedic. 3s pres. subj. jaghánat; MIr. geoguin, aor. 3s; Hom. cf. épephnon, aor. isg.
5478:guheguh- — guhermos (guhermn, guhermio)
5496:guhiguros (guhiguhro-) ‘burning, hot. Cf. guheguh-, var. of dheguh- Gk. thibrós “hot, roasted in embers'; Cz. cf. Zebra ‘fiery one’; Zehravy ‘fiery’; žhavý red. hot’; R cf. Zgu, Zec “burn, scorch’; (*-1- in) Sło- vene žíg ‘brand’; žigati, v. ‘brand, burn’
=== leaf 221/222 p379-380 ===
ice’ beside qäzäl ‘charred matter’; Alb. cf. zegël, zegth ‘gadfly’; OCS Zego, Zeët ‘kindle, burn’; Zegü, žega “heat; Cz. cf. Zehadlo ‘sting’; Pol. zegadto ‘red-hot iron’; Cz. Zehlice ‘flatiron’; Slovene žežel ‘poker’. (An R-gde w. i-basis seems to be present in Gk. thibrós ‘roasted, hot, ten- der”, cf. OCz. Zhu, Zéci ‘kindle’ and OCS Z1Ze- nije ‘burning, inflammation’. Gk. type *guhï- gu-)
guheguhon-, redup. theme of guhen-, q.v. Vedic. 3s pres. subj. jaghánat; MIr. geoguin, aor. 3s; Hom. cf. épephnon, aor. isg.
guheldhos ‘requital, debt? etc. Cf. gheldh- Gk. Myc. télthos, -es-, n. “debt, loan'. Other forms ambig. (Hes. téltho ‘cheer’ or ‘enjoy’ suggests a radical of type dhel- (1) & (2) w. an extn. Cf. MHG teizen ‘stroke, fondle’. However, both notions are present in Ir. gell, Mod. geall ‘pledge; favour; iove’. See next)
guhelo (-àio, -ëið) ‘wish, desire’. WP I, 692 Skt. haryāmi ‘desire’ is ambig. cf. gherið; Gk. thélo, Hom. ethélo (e- unexplained); Lat. (am- big.) felix (but cf. bhelos, dhél-); OHG OE will (ambig. cf. uel-); OCS Zelajo, -&jo “desire: Slovene cf. želja, f. ‘will
guhemər (guhemen-) ‘swell, bulge’ Lat. femur, gs feminis (variants: femen, -inis & femur, feminoris, n. 'thigh"); MHG wimer, wimmer ‘tumour, growth, burl on tree’; cf. Fris. wan, wanne; OE wenn 'tumour'; Du. wen 'goitre' qua *guhomn- (?). A further var- iant may be present (*guhembh-: *guhombh-) in Li. gémbe ‘burl on tree’; Go. wamba ‘belly’, etc. Gk. pompho$ ‘bubble’ is ambig.
guhen- radical of general sense: “drive, beat, kil. WP I, 679. Cf. guhn- Verbal forms: Skt. hánmi: Av. jainmi; OPer. -janam; Per. zanam, inf. zadan; Arm. $Énem (thematic: ‘beat: gin ‘whip, rod); fanam ‘strive’: athematic; beside ğan, Let, ‘effort’; Hitt. kwemi (for *kwenmi, 3pl. kunanci: Skt. ghnanti);; Gk. (thematic) théno, iotacized:
guheguh- — guhermos (guhermn, guhermio)
20
25
30
35
40
45
380
theíno; cpd. s-théno am able’; Alb. zâ, zë ‘seize’; iotacized: pér-záj, për-zë ‘chase’; ndër- zej “mate — animals’; Go. cf. winnan “strive, suffer’ beside winja ‘pasture’; OE winnan, as Go.; OCS Zeno, inf. gnati (chase, drive’, and com. Sl.) beside Zinjo (oxytonic; inf.: Zen ‘mow, mow down’; po-Zinjo “slaughter?); Li. Seng, ginti “herd along, drive, chase’; beside (oxytonic iotacized) geng, genéti ‘lop’; Latv. dzenu, dzīt ‘drive, chase’; OPr. cf. gunnimai (for *gunime, 1pl. ‘chase’: Skt. hanmah)
Noun forms: Skt. han, hanah, adj. 'strik- ing’; m. ‘striker’; Oss. qàn, gänä ‘wound’; Per. (-os/-es-type) zanaš ‘blow’; Arm. ğin “stick, whip’; Gk. cpd. s-thénos, n. ‘vigour’; Alb. zeje (craft, fr. *guhenio :Go. winja ‘pasture’. Se- mantics of G Trift: treiben); cf. exto. in Go. winna; MHG winne ‘pain, suffering’; OE winn, id. beside (simplex) OHG ga-win “la- bour, effort; ON vin, gs vinjar ‘meadow’; vinna ‘labour, hardship’; Li. genesýs (singu- larized -os-es-type: ‘herd-track’). Extended types: Arm. ğněem ‘abolish’; Lat. fendo, Gre ‘provoke’; Go. winnan (strive; suffer, and com. Gmc.); Cz. (?) žádat (in phr. nežádej si mne ‘don’t provoke me"); OCS Zelo (fgoad', and. com. Sl); Pol. Zad1o ‘sting’; Latv. dze- nols, dzenulis, id.
guhentuà, see guhen- Vedic hántvà “to be slain’; OCS Zetva Char. vest”, lit. cutting")
guherinos “hot, of heat, of summer”. See guherm-, guheros, guhor- Arm. Berin ‘hot’; Gk. therinós ‘of summer
guhermos (guhermn, guhermio) *warm, hot; heat. Variant: guhorm-. Cf. guheros, guhor-. WP I, 687. (Indo-Iranian forms fr. *guhorm-) Skt. gharmáh, m.; Av. garomo, adj.; garomus, m.; OPer. garma-; Per. garm, adj.; Oss. qarm, adj.; Tokh. A $árme, adj.; Arm. germ, o-st. adj.; Éermn gs german ‘fev
```


## [2026-09-05T20:15:34.876Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD dhegwh ===\"; grep -n -i \"dhegwh\\|dheguh\" AHD_watkins1985.txt | head -5; echo; grep -n -A6 -i \"^dhegwh\" AHD_watkins1985.txt | head -30; echo \"=== AHD geulo / coal ===\"; grep -n -i \"geu-lo\\|g(e)u-lo\\|Glowing coal\\|^gel-\\|coal\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:15:34.942Z] TOOL RESULT

```
=== AHD dhegwh ===

=== AHD geulo / coal ===
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
344:bly Latin fridre, to crumble: FRIABLE. 3. In the Celtic source of Vulgar Latin *brisdre, the source of Old French brisier and French briser, to break: BRISANCE; DEBRIS. [Pok. bhréi- 166.] bhrekv-. To cram together. 1. Probably Latin frequens, frequent, crowded: FREQUENT. 2. Suffixed zero-grade form *bhrk~-yo- in: a. Latin farcire, to cram, stuff: FARCE, FARCI, FARCY; INFARCT; b. Greek phrassein, to fence in, enclose, block up: DIAPHRAGM. [Pok. bhareky- 110.] bhrem-'. To growl. 1. Latin fremere, to growl, roar: FREMITUS. 2. Perhaps variant *brem- in Greek bronté, thunder: BRONTOSAUR. [Pok. 2. bherem- 142.] bhrem-2, To project; a point, spike; an edge. 1. Germanic *bréma-, name of prickly shrubs, in: a. Old English brém, broom: BRooM; b. Old English diminutive bremel, brém- bel, bramble: BRAMBLE. 2. Germanic *berm-, *brem-, in: a. Middle English brimme, edge: BRIM; b. Middle Dutch berme, barm, edge of a dike: BERM. [Pok. 1. bherem- 142.] bhres-. To burst. Germanic “brest- in Old English ber- stan, to burst: BURST. [Pok. bhres- 169.] bhreu-'. To cut, break up. Extension of bher-2. 1. Suf- fixed form *bhreu-d- in Germanic *breutan, to break up, in Middle English britel, brittle: BRITTLE. 2. Suffixed form *bhreu-t- in Germanic *breuthan, to be broken up, in Old English bréothan, to deteriorate: BROTHEL. [Pok. 1. bhreu- 169.] bhreu-?. To boil, bubble, effervesce, burn; with deriva- tives referring to cooking and brewing. I. 1. Germanic *breuwan, to brew, in Old English bréowan, to brew: BREW. 2. Germanic *braudam, (cooked) food, (leavened) bread, in Old English bréad, piece of food, bread: BREAD. 3. Germanic *brudam, broth, in: a. Old English broth, broth: BROTH; b. Old French breu, broth (diminutive brouet): BREWIS; IMBRUE. II. Variant form *bhré- in Germanic *brédan, to warm, with derivatives. 1. *bréd-6, “a warming,” hatching, rearing of young, in: a. Old English br��d, offspring, brood: BROOD; b. denominative *brodjan, to rear young, in Old English brédan, to beget or cherish offspring, breed: BREED. 2. Germanic *bré- d6n-, roast flesh, in: a. Old High German brat, brdto (> German Braten), roast meat: BRATWURST, SAUERBRA- TEN; b. Old French braon, meat: BRAWN. 3. Perhaps distantly related is the Germanic source of Old French brese, burning coal, ember (> French braise): BRAISE, BRAZE?, BRAZIER?, BREEZE2, III. Reduced form “bher-, especially in derivatives referring to fermentation. 1. Suf- fixed form *bher-men-, yeast, in: a. Germanic *bermén- in Old English beorma, yeast: BARM, (BARMY); b. further suffixed form *bhermen-to- in Latin fermentum, yeast: FERMENT. 2. Extended form *bherw- in Latin fervére, to be boiling or fermenting: FERVENT, FERVID, (FERVOR); DEFERVESCENCE, EFFERVESCE. IV. As a very archaic word for a spring. 1. Suffixed zero-grade form *bhru- n(e)n- in Germanic *brunnon- in Old English burn, burna, spring, stream: BOURN!, BURN?. 2. Suffixed form *bhréw-r in Greek phrear, spring: PHREATIC. [Pok. bh(e)reu- 143, 2. bher- 132.] bhreus-'. To swell. 1. Suffixed form *bhreus-t- in Ger- manic *breustam, “swelling,” breast, in Old English bréost, breast: BREAST. 2. Suffixed zero-grade form *bhrus-t- in Germanic *brust-, bud, shoot, in Old French broust, brost, shoot, twig: BROWSE. [Pok. 1. bhreu-s- 170.] bhreus-2, To break. 1. Germanic *briisjan, to crush, in Old English brysan, to crush, pound: BRUISE. 2. Suffixed zero-grade form *bhrus-to-, fragment, in Latin frustum, piece: FRUSTULE, FRUSTUM. [Pok. 2. bhreu-s- 171.] bhri-. Eyebrow. Contracted from *bhrua-. 1. Germanic *bris in Old English bri, eyebrow, eyelid, eyelash: BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugj6 (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE}, [Pok. 1. bhrii- 172, 2. bhrii- 173.] bhrig-. Agricultural produce; also to enjoy (results,
480:gel-2
487:gel-2. Bright. 1. Extended form *glei- in Germanic
488:gel-*
500:g(e)u-lo-. A glowing coal. Germanic *kulam, *kolam in: a. Old English col, a glowing coal: COAL, (COLLIE), (COL- LIER); b. probably dialectal Old French cholle, round lump, head: cHOLLA. [Pok. g(e)u-lo- 399.]
621:hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1378:CLUMP gel-1 CLUTCH! gel-1 CLUTTER gel-1 CLYSTER kleu-2 co- kom COADUNATE oi-no- COAGULUM_ ag- COAL g(e)u-lo- COALESCE al-3 COARCTATE ar- coasT kost- COBALT ku- cocciD kokkos coccus kokkos COCHINEAL kokkos COCHLEA konk(h)o- cock? ku- COCKAIGNE kak-2 COCKCHAFER gep(h)-
1383:COLE kaul- COLEOPTERA kel-2, pet- COLEOPTERAN kel-2 COLEOPTILE kel-2, pet- COLEORHIZA kel-2, wrad- COLESLAW kaul- COLEUS kel-2 COLLABORATE leb-1 COLLAGE koli- COLLAPSE leb-1 COLLAR kwel-1 COLLATE tele- COLLEAGUE leg-1 COLLECT! leg-1 COLLEGIALITY leg-! COLLET kwel-1 COLLIE g(e)u-lo- COLLIER g(e)u-lo- COLLIGATE leig-' COLLIGATIVE |leig-1 COLLO- koli- COLLODION koli- COLLOQUIUM tolkw- COLLOQUY tolkw- COLLUDE leid- COLLUVIUM leu(a)- COLOBOMA kel-1 COLON! | skel-3 COLONEL kel-6 COLONNADE kel-8 COLONY kWel-1 COLOPHON kel-6 COLOR kel-2 -COLoUS kWel-1 COLPITIS kwelp- COLPOSCOPE kwelp- COLPOSCOPY kwelp- COLTER skel-1 CoLuMBA kel-5 COLUMBARIUM kel-5 COLUMBINE kel-5 COLUMN kel-6 COLZA sé-1
```


## [2026-09-05T20:15:42.482Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -i \"dheg[a-z-]*.\\{0,400\\}\" AHD_watkins1985.txt | grep -i \"burn\" | head -5; echo \"---\"; grep -n -o \".\\{0,300\\}febris.\\{0,300\\}\" AHD_watkins1985.txt | head -5; echo \"--- FEVER index ---\"; grep -n -o \"FEVER [a-z()-]*\" AHD_watkins1985.txt | head -5; echo \"--- DAY index ---\"; grep -n -o \"DAWN [a-z()-]*\\|DAY [a-z()-]*\" AHD_watkins1985.txt | head -8"
}
```


### [2026-09-05T20:15:48.581Z] TOOL RESULT

```
ugrep: error: error at position 56
?:[^\n\x80-\xbf][\x80-\xbf]*){0,400}
       exceeds complexity limits___/


---
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,300}
                        \___exceeds complexity limits


--- FEVER index ---
--- DAY index ---
111:DAY is
1409:DAWN agh-
1410:DAY agh-
1454:DAY ambhi
2326:DAY sawel-
2388:DAY (s)tene-
2394:DAY agh-
2414:DAY deiw-
```


## [2026-09-05T20:15:57.047Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"FEVER\" AHD_watkins1985.txt | head -5 | cut -c1-400; echo \"=== agh- entry ===\"; grep -n \"agh-\\?[.,] A day\\|agh-. A day\\|agh-\\. \" AHD_watkins1985.txt | head -5; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'agh-', t):\n    s=t[m.start()-50:m.start()+500]\n    if 'day' in s.lower():\n        print('---'); print(s.replace('\\n',' ')); break\nfor kw in ['febris','dhegwh','dheg*h','Fever, in','fever']:\n    i=t.find(kw)\n    print(kw, i)\n    if i>0: print(t[i-400:i+400].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:15:58.722Z] TOOL RESULT

```
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live,
1507:FERIA dhés- FERMATA dher-2 FERMENT bhreu-? FERN per-2 FEROCIOUS ghwer- FERRET! bher-1 FERRET? bhel-3 FERRI- ferrum FERRO- ferrum FERROUS ferrum FERRUGINOUS ferrum FERRULE wei-1 FERRY per-2 FERTILE bher-1 FERVENT bhreu-2 FERVID bhreu-2 FERVOR bhreu-2 FEss bhasko- -FEsT dhés- FESTAL dhés- FESTINATE bhers- FESTIVAL dhés- FESTIVE dhés- FESTOON dhés- FETAL dhé(i)- FETCH! ped-1 FETE dhés- F
=== agh- entry ===
198:kagh-. To catch, seize; wickerwork, fence. pele-2. Flat; to spread. mu-', Imitative of inarticulate sounds.
386:dhragh-. To draw, drag on the ground. Rhyming variant tragh-. 1. Germanic *dragan in: a. Old English dragan, to draw, pull: pRaw; b. Old Norse draga, to draw, pull (or Old English dragan): DRAG; c. Old English drexge, dragnet: DRAY; d. Old Norse *drahtr, drdttr, act of drawing, akin to the source of Middle English draught, a pull: DRAFT. 2. Russian drogi, a wagon: DROSHKY. See also variant form dhreg-. [Pok. dheragh- 257.]
387:dhreg-. To draw, glide. Variant form of dhragh-. 1. Na- salized Germanic form *drinkan, to draw into the mouth, drink, in Old English drincan, to drink: DRINK. 2. Nasal- ized Germanic form *drankjan, “to cause to drink,” in: a. Old English drencan, to soak: DRENCH; b. Scandina- vian *drunkna, drugna, to drown, akin to the Scandina- vian source of Middle English drounen, to drown: DROWN. [Pok. dhreg- 273.]
566:kae-id-. To strike. 1. Latin caedere, to cut, strike: CAE- SURA, CEMENT, CESTUS2, CHISEL, -CIDE, SCISSORS; AB- SCISE, CIRCUMCISE, CONCISE, DECIDE, EXCISE2, INCISE, PRECISE, RECISION. 2. Latin caelum (? < *caedum), sculptor’s chisel: CAELUM. [Pok. (s)k(h)ai- 917.] kagh-. To catch, seize; wickerwork, fence. 1. Germanic *hag- in: a. Old French hagard, wild, wild hawk (< “raptor”): HAGGARD; b. Germanic *hagén- in Old Eng- lish haga, hedge, hawthorn: HAW?; c. Germanic *hagj6é in Old English hecg, hedge: HEDGE. 2. Suffixed unaspirated form *kag-yon- in Gaulish caio, rampart, retaining wall (> Old French quai, quay): (CAY), KEY?, QUAY. 3. Possi- ble variant *kogh- in: a. Latin cohum, strap from yoke to harness: INCHOATE; b. possibly Latin cdlum, sieve (< wickerwork), and its derivative céldre, to filter: COLAN- DER, COULEE, (COULOIR), CULLIS; PERCOLATE. [Pok. kagh- 518.]
711:magh-. To fight. Hypothetical Old Iranian *ha-maz-an-,
---
t” was nek’-t-. Words for “day” include amer- and agh-? and such dialectal creations as Latin diés; ayer- refers to the morning. The old word for “darkness,” reg”es-, shows up in Greek as a term for the underworld. The Indo-Europeans knew snow in their homeland; the word sneig”h- is nearly ubiq- uitous. Curiously enough the word for “rain,” however, varies among the different branches; we have words of differing distri- bution like seue-?, ombh-ro- and reg-?. Conceptions of the sky, heaven, were var- ied in the different dialects. As we have se
febris -1
dhegwh -1
dheg*h -1
Fever, in -1
fever -1
```


## [2026-09-05T20:16:07.284Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1507p' AHD_watkins1985.txt | tr ' ' '\\n' | grep -n -A2 -B2 -i \"FEV\\|FEW\\|FIAT\" | head -20; echo \"=== agh-2 ===\"; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'agh-[?2²]?\\.', t):\n    print('>>>', t[m.start()-20:m.start()+420].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T20:16:09.041Z] TOOL RESULT

```
71-FEUILLETON
72-bhel-3
73:FEVERFEW
74-bheug-!
75:FEW
76-pau-
=== agh-2 ===
>>> ed by a semicolon: kagh-. To catch, seize; wickerwork, fence. pele-2. Flat; to spread. mu-', Imitative of inarticulate sounds. After the basic meaning there may appear further information about the phonological shape or nature of the root: dhreg-. To draw, glide. Variant form of dhrag-. temp-. To stretch. Extension of ten-. tauro-. Bull. Derivative of sta-, but an in- dependent word in Indo-European. dail-. To divide. Northern Indo-Euro
>>> AWE. [Pok. agh- 7.] agh-?. A day (considered as a span of time). Germanic *dagaz (with initial d- of obscure origin), day, in: a. Old English deg, day: DAY; (DAISY), TODAY; b. Old English denominative dagian, to dawn: DAWN. [Pok. agher- 7.] agro-. Field. Derivative of ag-, “to drive” (< “place to which cattle are driven”). 1.Germanic *akraz in Old English zxcer, field, acre: ACRE. 2. Latin ager (genitive agri), district, property, field
>>> k. dhéigy- 243.] dhragh-. To draw, drag on the ground. Rhyming variant tragh-. 1. Germanic *dragan in: a. Old English dragan, to draw, pull: pRaw; b. Old Norse draga, to draw, pull (or Old English dragan): DRAG; c. Old English drexge, dragnet: DRAY; d. Old Norse *drahtr, drdttr, act of drawing, akin to the source of Middle English draught, a pull: DRAFT. 2. Russian drogi, a wagon: DROSHKY. See also variant form dhreg-. [Pok. dheragh- 25
>>> . Rhyming variant tragh-. 1. Germanic *dragan in: a. Old English dragan, to draw, pull: pRaw; b. Old Norse draga, to draw, pull (or Old English dragan): DRAG; c. Old English drexge, dragnet: DRAY; d. Old Norse *drahtr, drdttr, act of drawing, akin to the source of Middle English draught, a pull: DRAFT. 2. Russian drogi, a wagon: DROSHKY. See also variant form dhreg-. [Pok. dheragh- 257.] dhreg-. To draw, glide. Variant form of dhragh-. 
>>>  Variant form of dhragh-. 1. Na- salized Germanic form *drinkan, to draw into the mouth, drink, in Old English drincan, to drink: DRINK. 2. Nasal- ized Germanic form *drankjan, “to cause to drink,” in: a. Old English drencan, to soak: DRENCH; b. Scandina- vian *drunkna, drugna, to drown, akin to the Scandina- vian source of Middle English drounen, to drown: DROWN. [Pok. dhreg- 273.] dhregh-. To run. 1. Greek trekhein (< *threkhein), to 
>>> . (s)k(h)ai- 917.] kagh-. To catch, seize; wickerwork, fence. 1. Germanic *hag- in: a. Old French hagard, wild, wild hawk (< “raptor”): HAGGARD; b. Germanic *hagén- in Old Eng- lish haga, hedge, hawthorn: HAW?; c. Germanic *hagj6é in Old English hecg, hedge: HEDGE. 2. Suffixed unaspirated form *kag-yon- in Gaulish caio, rampart, retaining wall (> Old French quai, quay): (CAY), KEY?, QUAY. 3. Possi- ble variant *kogh- in: a. Latin cohum,
>>>  [Pok. magh- 695.] magh-. To fight. Hypothetical Old Iranian *ha-maz-an-, “warrior” (*ha-, with < *sm-; see sem-'), possibly borrowed into Greek as Amazén, Amazon: AMAZON. [Pok. magh- 697.] maghu-. Young person of either sex. Suffixed form *magho-ti- in Germanic *magadi-, with diminutive *ma- gadin-, in Old English mezgden, virgin: MAID, MAIDEN. [Pok. maghos 696.] mai-'. To cut. 1. Suffixed form *mai-d- in Germanic *mait- in: a. Germani
>>> k. suad- 1039.] (s)wagh-. To resound. 1. Germanic *swdégan in Old English swégan, to resound: souUGH. 2. Suffixed form *wagh-d- in Greek ékhé, sound: CATECHIZE. 3. Suffixed form *wdgh-di- in Greek ékhd, noise, echo: ECHO. [Pok. udgh- 1110.] sward-. To laugh. Greek sardanios, sneering, scornful: SARDONIC. [Pok. suard- 1040.] s(w)e-. Pronoun of the third person and reflexive (refer- ring back to the subject of the sentence); further appea
>>> . 1. tong- 1088.] tragh-. To draw, drag, move. Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, 
>>>  Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, TRAVE; ARCHITRAVE. [Pok. treb- 1090.] trei-. T
>>> . ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wre
```


## [2026-09-05T20:16:25.391Z] TOOL CALL #54: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:16:25.398Z] TOOL RESULT

```


```


## [2026-09-05T20:16:29.894Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eg%CA%B7%CA%B0-",
 "prompt": "Give the reconstruction, meaning, and the full list of derived/descendant terms (Indo-Iranian, Avestan, Persian, Latin, Germanic). Does it list Proto-Germanic *dagaz 'day' or Latin febris?"
}
```


## [2026-09-05T20:16:31.695Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/dagaz",
 "prompt": "Quote the etymology section in full: what PIE root is Proto-Germanic *dagaz derived from, what alternatives are mentioned (Kroonen, Watkins, *h2egh-), and what descendants (Old English dæg, dagian/dawn)?"
}
```


### [2026-09-05T20:16:36.210Z] TOOL RESULT

```
# Proto-Indo-European *dʰegʷʰ-

**Reconstruction:** *dʰegʷʰ- (imperfective)

**Meanings:** 
1. to burn
2. warm, hot

**Key Derived/Descendant Terms:**

The page lists extensive descendants across language families:

- **Indo-Iranian:** Sanskrit दह् (dah); Pali jhāyati
- **Latin:** febris ("fever"); foveō; fōmes; fōmentum
- **Germanic:** Proto-Germanic *dagaz (with note: "loss of labiovelar unexplained")
- **Greek:** τέφρα (téphra, ash)
- **Celtic:** Welsh deifio, daigh
- **Baltic-Slavic:** Lithuanian dẽgis, dègtas, dagà
- **Albanian:** ndez

**Important Note:** The page does explicitly list both "Proto-Germanic: *dagaz" and "Latin: febris" among the documented descendants, though it notes the Germanic form's phonological irregularity.
```


### [2026-09-05T20:16:38.615Z] TOOL RESULT

```
# Etymology of Proto-Germanic *dagaz

Based on the Wiktionary article, here's what the etymology section states:

**Primary PIE Root:**
The etymology is listed as "Uncertain" but "often explained" as deriving from PIE *dʰegʷʰ- ("to burn"), though this derivation has phonological problems.

**Kroonen's Alternative:**
Kroonen proposes instead a root *dʰeǵʰ- ("day"), from which a heteroclitic noun *dʰṓǵʰ-r/n- is derived, suggesting connection to Proto-Indo-Iranian *Háȷ́ʰr̥.

**Key Quote:**
"Often explained as derived from the Proto-Indo-European root *dʰegʷʰ- ('to burn'), but the loss of the labialization would be irregular; *dawaz would be expected."

**Regarding Your Query:**
The article does not mention Watkins or *h2egh- as alternatives. It also does not discuss "dagian" or "dawn" as descendants. Old English *dæg is listed as a direct descendant through Proto-West Germanic *dag, but Old English "dagian" does not appear in this entry's descendants section.
```


## [2026-09-05T20:16:45.063Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%BA",
 "prompt": "Persian داغ (dāḡ): give the full etymology (Middle Persian, Proto-Iranian, PIE root) and meanings."
}
```


## [2026-09-05T20:16:47.139Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%A7%D8%AE%D9%86",
 "prompt": "Persian فلاخن (falāxan) 'sling': quote the full etymology — Middle Persian, Avestan fradaxšanā-, Sogdian, any references cited."
}
```


### [2026-09-05T20:16:51.898Z] TOOL RESULT

```
# Persian داغ (dāġ): Etymology and Meanings

## Etymology
The word traces through multiple ancient language families:

- **Middle Persian**: Related to \[script needed\] (dazīdan, "to burn")
- **Proto-Iranian**: *dáǰatī*
- **Proto-Indo-Iranian**: *dʰáǰʰati*
- **Proto-Indo-European**: *dʰégʷʰeti*

The term is cognate with Avestan *daγa* ("brand; scar, spot") and Sanskrit *dāha* ("burning, heat").

## Meanings

**Adjective**: "hot" (comparative: داغ‌تَر; superlative: داغ‌تَرین)

**Adverb**: "exciting"

**Noun**:
1. A mark from cauterization or etching; a "brand"
2. By extension, a "mark, stain, blemish, scar, or dark spot" on something
3. A branding iron

The semantic development follows the root concept of burning, progressing from literal burn marks to figurative blemishes.
```


### [2026-09-05T20:16:53.945Z] TOOL RESULT

```
# Persian Word: فلاخن (falâxan)

**Definition:** A sling weapon

**Etymology:** The word derives "From [Old Iranian](https://en.wikipedia.org/wiki/Old_Iranian_languages "w:Old Iranian languages") (compare [Avestan](https://en.wikipedia.org/wiki/Avestan "w:Avestan") _[𐬟𐬭𐬀𐬛𐬀𐬑𐬴𐬀𐬥𐬁](/w/index.php?title=%F0%90%AC%9F%F0%90%AC%AD%F0%90%AC%80%F0%90%AC%9B%F0%90%AC%80%F0%90%AC%91%F0%90%AC%B4%F0%90%AC%80%F0%90%AC%A5%F0%90%AC%81&action=edit&redlink=1 "𐬟𐬭𐬀𐬛𐬀𐬑𐬴𐬀𐬥𐬁 (page does not exist)")_ (fradaxṣ̌anā, "sling")), probably via [Bactrian](https://en.wikipedia.org/wiki/Bactrian_language "w:Bactrian language")."

The term has multiple alternative spellings, including فلاخان and فلخمان. It subsequently influenced Chagatai and Uzbek languages, appearing as forms like *palaxmon* and *palaqmon*.
```


## [2026-09-05T20:17:01.915Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%AE%D9%85%D9%87",
 "prompt": "Persian دخمه (daxma): full etymology — Middle Persian daxmag, Avestan daxma-, and which PIE root it is assigned to (burn *dʰegʷʰ- or bury *dʰembʰ-). Quote any note about the disputed derivation."
}
```


## [2026-09-05T20:17:03.894Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%AF%D8%A7%D8%AE%D8%AA%D9%86",
 "prompt": "Persian گداختن (godāxtan) 'to melt': full etymology — Middle Persian, Proto-Iranian root, PIE root. Also any mention of گدازیدن godāzīdan."
}
```


### [2026-09-05T20:17:07.626Z] TOOL RESULT

```
# Etymology of Persian دخمه (daxma)

Based on the Wiktionary entry, the Persian word derives from **Middle Persian daxmag**, which was borrowed from **Avestan daxma-**. 

The Proto-Indo-European origin presents an interesting case. The entry lists the source as:

> "Proto-Indo-European _[\*dʰm̥bʰ-](/wiki/Reconstruction:Proto-Indo-European/d%CA%B0emb%CA%B0- "Reconstruction:Proto-Indo-European/dʰembʰ-")_ ("to dig")"

This indicates the *dʰembʰ-* root meaning "to dig," which connects to the burial/underground chamber sense of the word. The etymology is supported by cognates in Old Armenian (damban, "tomb") and Ancient Greek (táphos, "tomb")—both sharing the root sense of digging or burial places.

The entry does not note any dispute about the derivation, presenting the etymological chain as established from PIE through Avestan to Persian.
```


### [2026-09-05T20:17:10.417Z] TOOL RESULT

```
# گداختن (Gudāxtan) - Persian Verb

**گداختن** is a Persian verb meaning "to melt" or "to thaw." The word can function as both transitive and intransitive.

## Primary Meanings

1. **Literal**: "to melt; to turn to liquid; to thaw"
2. **Figurative (transitive)**: "to destroy; to consume"
3. **Figurative (intransitive)**: "to be consumed; to be wasted"

## Etymology

The term derives from Middle Persian *widāxtan*, tracing back through Proto-Iranian *wi-* + *taHč-* ("to melt") to Proto-Indo-European *teh₂-k-* ("to melt"). It shares cognates with Northern Kurdish terms and Ancient Greek *tḗkō* meaning "to melt."

## Linguistic Details

- **Present stem**: گداز (godāz)
- **Past stem**: گداخت (godāxt)
- The verb appears in multiple Persian dialects including Dari, Iranian Persian, and Tajik
- Synonyms include آب کردن (āb kardan) and ذوب کردن (zowb kardan)

The entry includes extensive conjugation tables for various tenses and grammatical persons across literary and colloquial Persian variants.
```


## [2026-09-05T20:18:50.458Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%BA%D8%A7%D9%84",
 "prompt": "Persian زغال (zoġāl) 'charcoal': give the full etymology if present (Middle Persian, Proto-Iranian, PIE), alternative forms, and any note about the origin being unknown or disputed."
}
```


## [2026-09-05T20:18:50.987Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/fever",
 "prompt": "Quote the etymology of 'fever': Old English fefor, Latin febris, and the PIE root it is assigned to (dhegwh-?)."
}
```


### [2026-09-05T20:18:56.871Z] TOOL RESULT

```
# Etymology of Persian زغال (zoġāl)

## Full Etymology

The word زغال derives from a deep Indo-European lineage:

- **Proto-Indo-European**: *ǵwelH- ("to burn, shine")
- **Proto-Indo-Iranian**: *ȷ́ar-
- **Proto-Iranian**: *jar-
- **Persian**: zoġāl

## Alternative Forms

Persian allows several spelling variants including زگال (zogâl), ژگال (žogâl), and ذغال (zoġâl), alongside dialectal forms like سکار (sekâr) and سگار (segâr).

## Comparative Evidence

The etymology shows cognates across Indo-European languages: "coal" appears in Proto-Germanic *kulą and Irish *gual*, supporting the reconstructed root meaning related to burning and luminescence.

## Semantic Range

Beyond "coal" and "charcoal," the term carries literary/poetic extensions denoting "black" or "dark," plus a botanical sense referring to dogwood or cornel plants.
```


### [2026-09-05T20:18:59.663Z] TOOL RESULT

```
# Etymology of "Fever"

**Old English and Latin Origins:**
"late Old English _fefor_, _fefer_ 'fever, temperature of the body higher than normal,' from Latin _febris_ 'fever'"

**PIE Root:**
The source traces to "PIE root _\*dhegh-_ 'burn'" rather than "dhegwh-". The entry explains this root also gave rise to Gothic and Old English words for "day" (originally meaning "the heat"), Greek "ashes," and Lithuanian terms for "heat" and "summer."

An alternative theory suggests "a reduplication of a root represented by Sanskrit _\*bhur-_ 'to be restless.'"

The Latin term was widely adopted into Germanic languages (German, Swedish, Danish) but notably not Dutch, while English spelling was influenced by Old French _fievre_.
```


## [2026-09-05T20:19:20.985Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.vajehyab.com/dehkhoda/%D8%AF%D8%AE%D8%B4",
 "prompt": "What does Dehkhoda give as the meaning(s) of Persian دخش (daxš)? Quote the definition lines."
}
```


## [2026-09-05T20:19:23.207Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk -v n=10395 'NR<=n{if(/\\f/)c++} END{print \"KLN line 10395 leaf:\",c, \"-> approx printed p.\", (c-12)*2}' KLN_1966.txt; awk 'BEGIN{RS=\"\\f\"} NR==215' KLN_1966.txt | grep -oE \"^\\s*[0-9]{3}|[0-9]{3}\\s*$\" | head -5; awk 'BEGIN{RS=\"\\f\"} NR==215' KLN_1966.txt | head -2"
}
```


### [2026-09-05T20:19:25.598Z] TOOL RESULT

```
# Meanings of دخش (daxš) from Dehkhoda Dictionary

According to the Dehkhoda Dictionary entry shown, دخش has two primary meanings:

**First meaning:** "ابتدا کردن کار باشد" (to begin or initiate a task/matter). The dictionary elaborates that it means starting dealings or transactions with someone.

**Second meaning:** "تیره و تاریک" (dark or gloomy). This appears as an alternate definition attributed to multiple sources.

The entry provides literary examples from Ferdowsi demonstrating both usages in classical Persian poetry.
```


### [2026-09-05T20:19:27.392Z] TOOL RESULT

```
KLN line 10395 leaf: 223 -> approx printed p. 422
386
,  excursion,  ex¬ cursus,  incur,  intercourse,  kraal,  occur,  occur¬ ence,  precursor,  recourse,  recur,  succor,  suc- cursal.  Cp.  also  car  and  words  there  referred  to. ON.  hross,  OE.  hr  os,  hors,  ‘horse’,  are  prob.  not cogn.  with  L.  currere,  but  derivatives  of  I.-E. base  *(s)qerd-,  a  -{/-enlargement  of  *(s)qer-,  ‘to leap,  jump'  (see  horse).  Derivatives :  current,  n. (q.v.),  current-ly,  adv.,  current-ness,  n. current,  n.  —  ME.  corant,  fr.  OF.  corant,  curant (F.  courant ),  pres.  part,  of  curre,  ‘to  run’,  used as  a  noun.  See  current,  adj. curricle,  n.,  a  light  two-wheeled  carriage.  —  L. curriculum,  ‘a  running,  a  course;  a  chariot  for racing’,  fr.  currere,  ‘to  run’.  See  current,  adj., and  -cle  and  cp.  curriculum.
Derivative:  curricle,  intr.  v. curricular,  adj.,  1)  pertaining  to  carriages;  2)  per¬ taining  to  the  curriculum.  —  Formed  with  suff. -ar  fr.  L.  curriculum.  See  next  word, curriculum,  n.,  course  of  study.  —  L.,  ‘a  course’. See  curricle.
```


## [2026-09-05T20:19:41.420Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BQT v2 داغ block\"; awk 'BEGIN{RS=\"\\f\"} /داغ ‪/{print \"BLOCK\",NR; print substr($0,1,2500); exit}' BQT_v2_pages.txt"
}
```


### [2026-09-05T20:19:43.109Z] TOOL RESULT

```
### BQT v2 داغ block
BLOCK 329
                                                                   ‫بیان یدازهم‬
         ‫دال بی نقطه باغین نقطه دار مشتمل بر چهارده لفت و کنات‬                                                                        ‫در‬



‫دعدعه ‪ ۱‬ه بفتح اول و غین نقطهدار‬                                                ‫هفتح اول و سکون ثانی ‪ ۰‬زمین‬
                                                                                                          ‫دع ب‬
 ‫بروزن لخلخه » بمعنی ترس وبیم ونشوش خاطر‬                                        ‫بی‌علف بعنی زمینی که هکریکازه درآن نرسته‬
 ‫ومیل‌نمودن بچیزی باشد ‪ -‬و بکر اول والث‪,‬‬                                       ‫بواشسدر‪٩‬ب‏‪-‬ی‌موی را نیز گوبند که از کچلی‬
‫جنبالیدن انگشتان است در زبربغل ویهلوی کسی‬                                       ‫همچو کون طاس بود ‪ - ۴‬وچارضرب زده را نیز‬
                                                                                ‫و‌شخصی باشد که رش وسبیل وابرو‬
                                                                                                            ‫گفته‌اند آن‬
                                                                                    ‫داغ هم‌هست ‪۴‬‬             ‫مخ‪-‬قف‬
                                                                                                                 ‫واشد‬
                                                                                                                    ‫ومره ربااك شر‬
‫بوده‪.‬‬    ‫ار دون‬       ‫است واو ازنل‬        ‫نام مادر رردشت‬
                                                                                ‫دعا د بروزن‌هوا » مردم نا راست ودغل‬
‫اول وفتح آخر که‬              ‫دغدو به دت‬                                         ‫وعیب‌دار ‪ - ۴‬وحرامزاده گروایند وسیم ناسره‬
‫فام مادر‬    ‫که‬       ‫سعتی دعدوست‬     ‫بای حطی باشد ‪6‬‬
```


## [2026-09-05T20:19:43.391Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON falaxan\"; grep -n \"فلاخن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -8; echo \"### MON godazidan\"; grep -n \"گدازیدن\\|گدازيدن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v*_djvu.txt 2>/dev/null | head -8"
}
```


### [2026-09-05T20:19:43.476Z] TOOL RESULT

```
### MON falaxan
incoming/MON/MON_2vol_Adena_v1_djvu.txt:24799:۰ ۱:۲۵ [- فلاخن | (.) کفه‌ای باشد 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:24802:بدان سنگ اندازند» فلاخن سنگ‌اندازی. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:61261:دستاسنگ: 1251-2-8 (امر.) فلاخن» 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:80614:با فلاخن سنگگ اندازد. قلاب‌سنگك» فلاخن. 
MON_part1.txt:24799:۰ ۱:۲۵ [- فلاخن | (.) کفه‌ای باشد 
MON_part1.txt:24802:بدان سنگ اندازند» فلاخن سنگ‌اندازی. 
MON_part1.txt:61261:دستاسنگ: 1251-2-8 (امر.) فلاخن» 
MON_part1.txt:80614:با فلاخن سنگگ اندازد. قلاب‌سنگك» فلاخن. 
### MON godazidan
MON_part2.txt:30054:گداز؛ 2 [- - گدازیدن» گداختن] 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:30054:گداز؛ 2 [- - گدازیدن» گداختن]
```


## [2026-09-05T20:19:52.586Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 271 272 273; do echo \"##### BLOCK $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -30; done 2>/dev/null | head -100"
}
```


### [2026-09-05T20:19:54.745Z] TOOL RESULT

```
##### BLOCK 271
   ‫وت‬                                                                                                         ‫دارا‬
‫داادرار کردن" » با دال ابجد ‪,‬‬                                 ‫است در هندوستان ‪ -‬و داامروبی که آنرا‬
‫کنابه ازدیر باسدن وشات داشتن‪ -‬ومدارا کردن‪-‬‬                    ‫‪ -‬و بممنی داشتن و امر‬           ‫وزبند‬
                                                                                                  ‫ی دگرا‬
                                                                                                       ‫ظمفل‬
                                   ‫باشد‬   ‫ویسار ماندن‬         ‫بداشتن‌هم هت ‪ -‬وبمعنی داورهم آمده است که‬
                                                              ‫خانه‬      ‫بی‬
                                                                         ‫رو‬‫ع‪-‬‬
                                                                            ‫یشد‬
                                                                              ‫مکی از نامهای خدایتمالی با‬
‫ممدوده‬       ‫قریں ‪ - ۸‬با همزه‬              ‫دار‬
                                                                                         ‫ومحله رگاونند ‪.‬‬
‫ومتصوره هردوآمده است وسکون‌فا‪ .‬هرچیز که‬
                                                               ‫دارا = بروزن خارا ‪ ,‬نام بادشاه مشپور‬

‫وینچره‬       ‫وامثال آن‬     ‫وخواه سنوای‬     ‫آن مححری‬
                                                               ‫است که دارای! کبر‪,‬اشد واورا داراب نیز گوبند‪.‬‬
                                                               ‫ولو درزمان سکندر کشته شد ودارای اصفر پس‬
‫را نز گربند که دریش خاله مابن دو‬                ‫ومحجری‬
                                                               ‫اوست ‪١‬‏ ‪ -‬ویمعنی داأرنده هم‌هست ‪ _ ۴‬واشاره‬
‫وهد‌وصفةٌ درخاله راز گود‪,‬‬
                        ‫باژو ی درساژ لد‪ -‬ک‬                      ‫مذات بارتمالی ‪ -‬و کنابه از بادشاهان باشد ‪-‬‬
                                                               ‫که در ته خم‬        ‫ویبزند‬
                                                                                       ‫و دردی رکان‬            ‫وای‬
                                                                                                                ‫ل‬
         ‫‪۰‬‬   ‫است ات و نام داروبی هی‌هست‬          ‫هم ‪۹‬‬                                                     ‫‪/‬‬   ‫‪۹۳۹ ۳1‬‬




##### BLOCK 272
 ‫دار شش‌دو‬                                                                                      ‫سس‬   ‫‪۱۱‬‬


‫دارخال = با خای نقطه دار بر وزن‬                       ‫دار با‪ » ۱‬بابای ابجد بالف کشیده ‪۲‬‬
‫پارسال ‪ ,‬درختی که آنرا پوند نکرده باشند ‪-‬‬                       ‫مابحتاج وضروری ودرباست راگویند ‪.‬‬
‫وشاخ‌درختان(‪ )۳‬توشانده رائیز گویند ‪ - ۷‬وهر‬            ‫دار بار ‪ - ۲‬بروزنکارساز ‪,‬شخصی را‬
‫بونه ودرختی بود که از جابی بر کنده باشند(‪)4‬‬
                                                      ‫کوبند که چوب بلندیرا در زمين محکم سازد‬
                       ‫ودرجای دیگربنشانند ‪.‬‬               ‫وبر اطراف آن ریسمانها بندد ویربالایآن چوب‬
‫داردار کردن ‪ ۰ ۲‬کنابه از در‬                                          ‫رود وبازبپای عجیب وغریب کند ‪.‬‬
‫پاییدن وثبات داشتن ‪ -‬ومدارا کردن ‪ -‬و بيار‬             ‫دار بام ‪ = ۳‬بروزن شادکام " شاه تیررا‬
                            ‫ماندن باشد (‪)e‬‏ ‪.‬‬         ‫کویند » وان چوب برزکی باشد که بدان بام‬
                                                                                            ‫خاله بوشند ‪.‬‬
‫دار دان‪ .‬وبزرن‌اردان» بمعنی‌تخمدان‬
‫برآن‬   ‫باشد» وآن زمینی‌است که شاخهای درخت‬
                                                      ‫دار بر = بضم بای ابجد و سکون رای‬
‫فبرروند تاسبز شاوزدآونجا بجای دیگر هل‬                 ‫قرشت(‪ » )۱‬نام مرغیست سبزرنگ که درختانرا‬
                                                      ‫ممنقار سوراخ کند * و آن را بشیرازی دار نمك‬
                                                                                                ‫خواند ‪. ۴‬‬
‫داررومی = داروبی باشد رومی ‪.‬‬
                   ‫گوبند نافع لقوه است ‪.‬‬              ‫دناربپارن ه بفتح بای فارسی ‪.‬‬
                                                      ‫بودان چیز ها رنگه‬                     ‫چوب بق‬
                                                                                     ‫گمورباند‬
‫دار ررد = با زای نقطه دار بروزن‬
‫لاجورد » زردچوبه راگویند و بعربی عروق‌السفر‬
                                       ‫خوانند ‪.‬‬       ‫دار زین * » با بای ابجد وزای هوز‬
                                                      ‫بروزن ماه جبين » ینجره و محجر را گوبن دکه‬
‫سایرنج (‪-)۱‬کنایه ازدیباوعالسفلی‬
                              ‫د‬
                                                                                   ‫درخانه ساز ند‬     ‫دربيش‬
##### BLOCK 273
                                                                                 ‫داز شمان‬




                        ‫‪-‬‬     ‫دار کوب‬             ‫دارشعان ‪ = ۱‬باشن‌شطهدار وعین‬
                       ‫بز وزن خاکروب ‪,‬‬            ‫بی‌نقطه بورزن آبریز گان » درختی باشد سطبر‬
                        ‫بزبان ‪.‬کیلالی‌مرغی‌را‬     ‫و خاردار وپوست آن بقرفه ماندلیکن از آن‬
                       ‫کونند که بامتقاردرخت‬       ‫کت تقر وسرخ نرمیشود ‪ .‬اکرقدری ازآن‌سحق‬
                               ‫را سوراخ کند ‪.‬‬
                       ‫دار بوگاوورسیشده۔‬
                                                 ‫کنتد وما سر که سرشند وبردندان لهند درد را‬
                                                  ‫فروشاند» وقدری ازچوب آن‌زنان‌بخود ب رگبرند‬
      ‫دارکوب‬                      ‫باکاف قارسی‬     ‫قرزهدی که درشکم مرده باشد بیفتد ‪ -‬و ستبل‬
‫و مشین نقطه دار زده » امر به نگاهداشتن باشد‬       ‫هتدی را فز دارششمان خوانند و دارشیمان «م‬
               ‫بعنی نگاهدار ومحافظت کن © ‪.‬‬                          ‫کوبند بحذف شین دوم ‪.‬‬
‫دار کیسه ‪ ۱‬س بکر کاف و سکون‬                                             ‫دفار‬
                                                 ‫رلی ‪ - ۲‬باوفراای قرشت بر‬
‫بای حعلی وفتحصین بینقطه " کسه مانندی‌است‬
‫که دربعضی از درختها بهم ءیرسد ودرون‌آن پر‬        ‫وزن بتماکین » سفهوسکو ود کهکروابند که‬
                                                  ‫تن در بیش درخالپا سازند ‪ -‬و مطلق‬       ‫بجهت‬
                            ‫از یشه میباشد ‪.‬‬                          ‫تکه کاهر ا نیز کفته‌اند ‪۱‬‬
‫دار هك » بامیم بروزن آبچك » نوعی‬
                                                      ‫دار فلفل ‪ ۴‬مهعروف است گ‬
                                                  ‫‪.‬وبند‬
‫ازمروباشد وآن مروسفید است » ومروجنسی از‬
‫رباحین بود وسد بلغمی بکثاید واکثر امراض‬           ‫شکوفه وبیلرفلفل است» وبعضی کویند درخت آن‬
                            ‫بلغمی را ناقع است‪.‬‬    ‫غیر درخت قلقل باشد(‪ )۱‬وآن را فلفل درازنیز‬
                                                                                   ‫کوند‬
‫دار نگ » بکر الك و سکون نون‬                                  ‫‪ .‬گرم وخشك است درسم ‪.‬‬
```


## [2026-09-05T20:20:02.574Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /داغ/{c++; print \"BLOCK\",NR; } END{}' BQT_v2_pages.txt | head -20"
}
```


### [2026-09-05T20:20:04.338Z] TOOL RESULT

```
BLOCK 51
BLOCK 96
BLOCK 255
BLOCK 276
BLOCK 277
BLOCK 288
BLOCK 304
BLOCK 329
BLOCK 411
BLOCK 450
BLOCK 457
BLOCK 492
BLOCK 574
BLOCK 581
BLOCK 583
BLOCK 633
```


## [2026-09-05T20:20:06.728Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==277' BQT_v2_pages.txt | head -35"
}
```


### [2026-09-05T20:20:08.618Z] TOOL RESULT

```
 ‫”‪“AI‬‬                                                                                                          ‫داغ شدن‬

‫دالیز و‪٩‬‏ تست س بای اد و فتح زای‬                                       ‫داع شدن ‪ -‬بنایتآزرده شدن باشد‪.‬‬
‫هوز‪ ,‬مرغی است کوچك وجهنده که عرب صموه‬                                   ‫کونابه ازهیب دارگردیدن ‪ -‬وشهرت بافتن ‪-‬‬
‫گوبندش ؛ و بعضی گوبند نوعی از وطواط است‬                                            ‫وکهنه ومتعمل بودن هم‌هست ‪٩‬‏ ‪:‬‬
                                           ‫وعربی وصع خوانند ‪.‬‬          ‫داغ گاز ران = نشانی‌باشد که‌بر کذار‬
‫دال پور ببای ابجد ودال پوز‬                                              ‫پارچه کنند تا درشستن بدل نشود ‪ -‬و داغیکه‬
‫با بای فارسی بروزن خام سوز » نوعی از وطواط‬                                                            ‫بهنج چیر نرود ‪.‬‬
                       ‫اوسفتر‪-‬اشتروك را نگیوزمند ‪.‬‬                       ‫ارغول‪,‬‬
                                                                              ‫ووازومنجه‌ولش ب‬
                                                                                            ‫با‬      ‫داغول ‪۲‬‬
‫دال بوده" ‪ ۰‬ودال پوزه بازبادنی‬                                                         ‫عار ومکار وحرامزاده گروایاد ‪.‬‬
‫ها » یمعنی دال بوز است که نوعی از وطواط‪-‬‬                                 ‫داغولی ‪ = ۴‬بمعنی حرامزادکی‬
‫وفراشتروك باشد؛ و درهردولفت بجای بای ابجد‬                               ‫وعیاری باشد ‏ ونام جاسوس نصر سیارهم هست ‪.‬‬
                            ‫بای حطی هم بنظرآهده است ‪.‬‬                   ‫داغینه = بروزن‌بارنه‪ ,‬کهنه ومستممل‬
 ‫دال خال ‪ ۳۱۰‬باخای قطم‌دار بروزن‬                                                                           ‫رگوابند ‪. ۴‬‬
‫پارسال ؛ نهال ودرخت نونشالده ویولد نکرده را‬
                                                                       ‫دال = بروزن بال ‪ ۰‬پرنده‌ایست که پراو‬
                                                        ‫گومند ‪.‬‬         ‫رایرتیراصب کنند وبعربی‌عقاب گوبند ‪-‬وحرفی‬
 ‫ن»‬
  ‫دال هن ‪ ۳‬بفتح میم‌بروزن خکار‬                                                                ‫است از حروف تهجی ‪٦‬‏‬

           ‫مرغی است که آنرا بعربی عقاب گوبند ‪.‬‬                          ‫دالان = بروزن بالان » دهلیز خانه ‪۲‬‬

‫دال مینو قر ‪ -‬بوان بر وزن باغ‬                                                          ‫روایند ‪.‬‬
                                                                                              ‫‪ -‬وکوچۀ سرپوشیده گ‬
 ‫نیلوفر » نام نسکی‌است ازجملةٌ بيست وبك‌سك‬                              ‫نه = بروزن جانانه » بمعنی دالان‬
‫کتاب زند (‪ )۱‬یعنی فمی ازجملهةٌ بست وبك‬                                  ‫است که دهلیز در خانه ‪ -‬و کوچۀ سر پوشیده‬
                       ‫‪0‬‬               ‫قم کتاب زند (‪. ۱)۴۲‬‬                                                      ‫باشد ‪. ۸‬‬

                                                                                            ‫" (‪ )۱‬چك ‪ :‬ژد ‪.‬‬


      ‫‪ ۴‬کیلکی ‪( 2100۱80‬کسبکه دربازی تقلب کند ‪.‬جر‬                                           ‫رك‪ :‬داغنه‪۰ ‎‬‬   ‫‪۳ ١‬‬
```


## [2026-09-05T20:20:50.384Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==276' BQT_v2_pages.txt | head -45"
}
```


### [2026-09-05T20:20:52.138Z] TOOL RESULT

```
 ‫داغ سو‬                                                                                                            ‫س‬
                                                                                                                   ‫ری ‪۱‬‬
                                                                                                                      ‫تس‬


 ‫داشن ‪ = ۲‬بروزن دامن؛ عطا وبخشش‬                             ‫خوشه است ‪٩‬‏ ‪-‬وداسی را گیوزیند که غله‬
‫وانعام باشد ‪ -‬واجر ومکافات لیکیرا هم گوبند‬                                                    ‫‪۰‬‬   ‫کنند ‪۳‬‬           ‫بدان درو‬


 ‫ودر زند (‪)۱‬مرقوم است که داشن نقد وجنیرا‬                   ‫داش س بر وزن فاش » کوره ایکه‬
                                                                                ‫‪۰‬‬                          ‫=‬



‫گوبند که پارسیان‌درعید وجشنهابرسم نذرباصدقه‬                   ‫وخموکاسه و کوژه وامثال ‏ ن‌دران‌بیز ند‪۰ ۴‬‬                ‫حشت‬

                   ‫بففرا ومسا کین بدهند ‪. ۸‬‬                                         ‫وهمعني کاستان همکفته‌اند ‪۰‬‬

‫داع ‪ = ۹‬بروزن باغ» ممروف‌است *‪-۱‬‬                              ‫داشاب = بروزن داراب » بمعنی داد‬
‫وبمعنی‌شان همآمده است ومعنیی (‪ )۲‬که شاعر‬                                    ‫ودهش وچیزی بمردم دادن باشد ‪.‬‬
                                       ‫چ‬
‫ند جا ببندد ‪ -‬ونام شاعرکه درغزل و فصده‬                        ‫داشاك « بروزن آزاد » بمعنی شاط ‪-‬‬
                                           ‫مذ کور شود‬
                                                              ‫و عطا وبخشش وانعام باشد وبمعنی اجر وتلافی‬
 ‫کنابه ازنشانی‌باشد‬           ‫داع بلندان ت‬
                                                              ‫همأ همده است ‪ -‬وخوشبوبی فروش و عطار را لز‬
‫که بسب سجده کردن یار درییشاای مردمبهم‬                                                                          ‫کویتق سك‬
                                            ‫ی ‪۳۲‬‬
                                                              ‫داشته " ب=روزن چاشته‪ ,‬کهنه وفرسوده‬
 ‫داع سره باسین بشیطه بروزن‌کاشفره‬                                                                     ‫سے‬
                                                                                           ‫وضایع شده را ذویند ‪.‬‬
‫کسی را کون که آدم سرباشد بعئی مرش سراو‬
‫تافرق موی نداشته باشد واورابعربی اصلم خوالند‪.‬‬                 ‫داشخار * ‪ -‬با خای قطه دار بروزن‬
‫ویرنده‌است ازجنس کنجشك ودرسراوچند پرزرد‬                       ‫آشکار»چر ك آهن‪,‬اش دکه ریمآهن گویندش؛وبعربی‬
                                                                                             ‫خبٹ‌الحدید خوانند ‪.‬‬
 ‫هیباشد وهمجویلیل وجل وسیره خوش آواز بود ‪-‬‬                                                        ‫‪5‬‬            ‫ھ‬

 ‫و کنجشك بر را گنفزته‌اند وماد آلرا ماوغیش‬                        ‫داش خال ‪ - ۱‬بر وزن آش مال‬
                                                ‫خوانند ‪.‬‬               ‫بمعای داشخار است که ریم آهن باشد ‪.‬‬

                                                   ‫» چش‪ :‬معنی ‪.‬‬   ‫(‪ )۲‬چك‬                ‫(‪ )۱‬جك ‪ :‬ژند ‪.‬‬

                          ‫‪.‬‬    ‫اسشق و هوبشمان ‪۹۲6‬‬       ‫رک‪:‬‬       ‫‪۴‬‬             ‫رکک‪ :‬داس ‪.‬‬                 ‫‪۱‬‬

  ‫‪ - ۴‬اسم مفعول از‬                         ‫‪- ۴‬کور؛ انوابی (سنگكپزی) را یز ‪ 0581‬کوبند ‪.‬‬
```


## [2026-09-05T20:21:03.980Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON falaxan ctx\"; sed -n '24790,24810p' MON_part1.txt; echo \"### MON godaz ctx\"; sed -n '30045,30070p' MON_part2.txt"
}
```


### [2026-09-05T20:21:04.049Z] TOOL RESULT

```
### MON falaxan ctx

نلله: (۵-)۱9:۱۱۱۱۸۱۸ [ع. ۳ بلبلة ] و سو سد. 
سختی» اندوه. اختلاط لسان‌ها. تفریق آرا؛ 
بلبله: (۵-) 00۱۸ امد [غ. - سلیل] (.) کوزة 
لو لهدار؛ ظرف ۳ لو له‌دار ییاه آفتاید. 
کوزة شراب ابریق می» صراحی. ظرفی که 
در آن قهوه جوشانند» قهوه جوش. صداو 
آواز صراحی هنگام ربحتن می. 

۰ ۱:۲۵ [- فلاخن | (.) کفه‌ای باشد 
که از ابریشم يا از پشم ببافند و دو ریسمان بر 
دو طرف آن بگذارنند و شاطران و شبانان 
بدان سنگ اندازند» فلاخن سنگ‌اندازی. 
بلد؛ ۵ (ع.) (.) شهر؛ ج. بلاد» بلدان. 
زمین» ناحبه. راهبر؛ بیشوا. آنکه راه را 
می‌شناسد و دیگران را راهسنمایی کنند؛ 
راهنما. دانای در کار واقف. مطلع. در اصل 
«اهل البلد» بوده. بلد بودن: (مصل.) دانا و 
عالم بو دن. بلدم: می‌دانم. 
بلدرچین: که ۱2 (۱.) (جاند.) کرک. 
بلده: (ه-)://:۱ (ع. بلدة] (۱.) واحد. بلد. 
### MON godaz ctx
کدار: 20*23 ( کناز - گذاره| (.) محل 
عورء» معبر. گذرگاه میان کویر باتلاق» 
رو دخانه. ب یگدار ره آب زدن: بی‌احتیاط به 
کاری قیام کردن (ل۶.)» ملاحظة اطراف و 
جوانب کار را نکردن (فرعا.) 

گدارو: -.ع (- گداروی] (ص‌مر.) 
گدانتش: کداصفت: 

گداز؛ 2 [- - گدازیدن» گداختن] 
(امص.) تا ۸ دوب. 
لاغری» کاهش تن. تپش (مخصوصاً تپش 
لرزش زنان به هنگام زادن). درد (و 
بر ی 
(۱.) ظرف جدنی دردار که دود و هوا را در 
داخل نکه می‌دارد. 

گداصفت: 2-62 [ف. ۰ ۰] (ص‌مر.) 
آنکه طبع گدایان دارد؛ گدامنش» لتیم. 
گداگر سنه: (016912)6ع-.ع ( ص مر .) (عم.) 
کسی که چشم دلش سیر نشود. 

گدایی: (د2ع)605-1: (حامص.) عمل گدا؛ 
شغل گداء در بوژه؛ کد به. ه گدایی افتادن: 
کٌدا شدن» تهیدست گردیدن.
```


## [2026-09-05T20:21:21.559Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 1626 1734 1737; do echo -n \"AHM line $L -> leaf \"; awk -v n=$L 'NR<=n{if(/\\f/)c++} END{print c\" = printed p.\"(c-14)}' AHM.txt; done"
}
```


### [2026-09-05T20:21:23.312Z] TOOL RESULT

```
AHM line 1626 -> leaf 190 = printed p.176
AHM line 1734 -> leaf 202 = printed p.188
AHM line 1737 -> leaf 202 = printed p.188
```


## [2026-09-05T20:21:23.489Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg134.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/134.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-05T20:21:23.562Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:21:37.422Z] TOOL CALL #74: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/134.png; for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eg%CA%B7%CA%B0-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/dagaz\" \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%BA\" \"https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%A7%D8%AE%D9%86\" \"https://en.wiktionary.org/wiki/%D8%AF%D8%AE%D9%85%D9%87\" \"https://en.wiktionary.org/wiki/%DA%AF%D8%AF%D8%A7%D8%AE%D8%AA%D9%86\" \"https://en.wiktionary.org/wiki/%D8%B2%D8%BA%D8%A7%D9%84\" \"https://www.etymonline.com/word/fever\" \"https://www.vajehyab.com/dehkhoda/%D8%AF%D8%AE%D8%B4\"; do python3 tools/fetch_source.py \"$u\" --note \"page 134, root Dhogh/Dhegh: verification of PIE *dhegwh-, dagaz/day, dag, falaxan, daxma, gudaxtan, zoghal, fever, daxsh\" 2>&1 | tail -2; done"
}
```


### [2026-09-05T20:21:42.587Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 87739 Sep  5 16:21 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/134.png
/home/sfmqrb/git/rishe/data/verification/sources/web/54f22448b055ee2f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b46c83620cd9b01.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/845e7ed5323a82b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb58c55a5623c074.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7b03ac60bea64bd5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f483bbda47782c04.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9dde36d858202a79.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/76fa4bf99e495b74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/413a4c0676ef6ac8.txt
```


## [2026-09-05T20:21:47.707Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/day",
 "prompt": "Quote the etymology of 'day' (Old English dæg, Proto-Germanic *dages-/*dagaz, PIE root) and what it says about 'dawn' (Old English dagian)."
}
```


### [2026-09-05T20:21:53.817Z] TOOL RESULT

```
# Etymology of "Day"

Based on the etymonline entry, here's what the source states about the word's origins:

**Etymology Chain:**
The word "day" traces back through Old English *dæg* to Proto-Germanic *\*dages-*, ultimately deriving from a PIE root. The source notes: "Old English _dæg_ 'period during which the sun is above the horizon,' also 'lifetime, definite time of existence,' from Proto-Germanic _\*dages-_ 'day'... according to Watkins, from PIE root _\*agh-_ 'a day.'"

**Regarding "Dawn":**
Interestingly, the provided content does not include information about Old English *dagian* or the etymology of "dawn." While the page contains a link to the entry for "dawn" in its nearby-entries section, the actual etymological details for that word are not included in the material supplied.

The source emphasizes that the Germanic initial *d-* has "obscure origin," though an alternative theory suggests it may derive from PIE *\*dhegh-* meaning "to burn."
```


## [2026-09-05T20:22:53.883Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dheg\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20"
}
```


### [2026-09-05T20:22:53.937Z] TOOL RESULT

```
45359:mann Bsl. Wb. 319. — Gr. zecpoa zu *dheg'ih-, s. d. 
48429:aaO.) auch bret. devi cymr. deifio ,,brennen‘ wolil niclit zu Wz. dheg'ih- 
49584:deg(h)- oder dheg(h)- „eintauchen, trinken"?? 
52981:dheg- 
53484:dheg”h- 
53490:dhegSta- ,,brennen ££ . 
53497:was zu verbrennen ist“), zkpna „Asche“ ( dheg'fhra ; nicht unter Trennung 
53510:stufe '*dh e ff‘}i- wie air. daig ?) ; febris „Fieber ££ *dheg“hris , wie dt. „die 
53517:innerbritannische Stiitze der Wz. dheg’ih-).
```


## [2026-09-05T20:22:56.552Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '53484,53525p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:22:56.603Z] TOOL RESULT

```
dheg”h- 


849 


dhegSta- ,,brennen ££ . 

Ai. dahati, av. dazaiti „brennt‘ £ (= lit. degu), aksl. zegq, alb. djek, Ptc ai. 
dagdhd-h (= lit . degtas), kaus. dahayati; daha-h „Brand, Hitze ££ , nidagha-h 
„Hitze, Sommer“ np. day „Brandmal ££ ; av. daxsa- m. „Brand ££ . 

Gr. dsmavog ' dmouEvoq Hes. (,,angezfindet“; = lit. degtinas „wer oder 
was zu verbrennen ist“), zkpna „Asche“ ( dheg'fhra ; nicht unter Trennung 
von -demavoq als *tep-sra zu *tep- „warm, lau sein“, z. B. Prellwitz 2 s. v. 
zweif elnd) ; 

alb. djek ,verbrenne, brenne an £ (G. Meyer Alb. Wb. 69), Kaus. dez, 
ndes „ziinde an“ (Pedersen KZ. 36, 323 f., Gdf. *dhog'iheio = lat. fovco ) ; 

lat. foveo, -ere „warmen, warm halten, baden, hegen, pflegen“ (s. gegen 
andere Deutungen Yf. LEWb. 2 s. v.), foculum „Feuerpfanne“ (*fouiclom), 
fomentum ,,ein erwarmender Umschlag“ ( *fouimentom ), fomes, -itis „Zun- 
der <£ (*f ouimet- r> . oder vom Yerbum unabhiingiges ^dhog'ih-smo-l Bed. wie 
lett. daglis), favilla „Asche, bes. noch gluhende" (wabrscbeinlich aus *fo- 
villcL Thurneysen KZ. 28, 159, Solmsen KZ. 37, 4; oder mit der Ablaut- 
stufe '*dh e ff‘}i- wie air. daig ?) ; febris „Fieber ££ *dheg“hris , wie dt. „die 
Hitzen — Fieber ££ ; vgl. zuletzt Yf. IF. 19, 102; nacb Jacobsohn KZ. 46, 
57 wegen febrlcula Abstraktum auf -7- von einem adj. ro-Stamme). Mir. 
daig (gen. deg a) „Feuer' £ (Fick II 4 140; kaum hierher air. dedal „Zwie- 
licbt £i aus *dui- dhog'ihlo- ? ? Stokes Rc. 27, 88; iiber mbret. deuiff, nbret. 
devi , cymr. deifio „brennen ££ s. u. *dau- „brennen“ ; cymr. go-ddaith „Brand ££ , 
nach Osthoff IF. 27, 162 IF. aus *-dekto-, gabe freilich auch fur deifio eine 
innerbritannische Stiitze der Wz. dheg’ih-). 

Lit. degu, degti „brennen ££ (tr. und intr.), lett. degu, degt „brennen (intr.) ££ ; 
lit . dagas „das Brennen, Brand; Glut, Sommerhitze; Ernte !£ , dagd „Ernte £f , 
apr. dagis „Sommer ££ ; lett. daglas f. pi. „Brandfleck“, daglis „Zunder“ ; lit. 
nuod'egulis „Feuerbrand ££ , degis „Brandwunde“; atuo-dogiai .,Sommerweizen £C . 
Slov. degniti „brennen, warmen ££ (von der Sonne, s. Berneker 182), cech. 
alt dehna „Teufel £ ‘, dahneti „brennen“, russ. d'egoie „Teer“, wie lit. degutas 
„Birkenteer“ ; mit Ass. von *degq zu *gegq (s. Meillet Msl. 14, 334f., Brug-
```


## [2026-09-05T20:23:01.437Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:35:57.839Z] TOOL CALL #78: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build134.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"Dhogh, Dhegh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *dʰegʷʰ- 'to burn' (o-grade *dʰogʷʰ-o-, adj. *dʰegʷʰ-ro-); LIV² 133 f., Pokorny IEW 240 f.\",\n \"note\": \"Pokorny IEW 240 heads the entry 'dhegʷh- „brennen‘; Nominalbildungen dhogʷho-s, dhegʷh-ro-s', which is exactly Nourai's pair of root shapes: 'Dhogh' is Pokorny's o-grade *dhogʷho-, 'Dhegh' the e-grade *dhegʷh-. Language label (Indo-European) and gloss ('to heat, burn') are right; the only notational loss is that Nourai does not mark the labiovelar (gʷh, written gh). Walde-Pokorny I 849 and Cheung 2007 (s.v. *daj) give the same root, Cheung citing 'PIE *dhegʷh- “to burn” = LIV: 133 f. | Pok.: 240 f.'. Two structural remarks on the chart as a whole: (a) the coal box (node 12) is not a derivative of this root in any standard handbook – only S. E. Mann's idiosyncratic 'guheguh-' (IEC 379) makes that link, by assimilation; (b) the melt branch (nodes 6–7) is assigned by Nourai's own reference Nyberg II 217 to a different root altogether.\",\n \"note_fa\": \"جعبهٔ ریشه درست است: همان ریشهٔ هندواروپایی آغازین *dʰegʷʰ- «سوختن، سوزاندن» که پوکورنی در صفحهٔ ۲۴۰ با همین معنا («brennen») آورده و دو صورت اسمی *dʰogʷʰo-s و *dʰegʷʰ-ro-s را برای آن بازسازی کرده است؛ دو صورتی که نورایی در جعبهٔ ریشه می‌آورد (Dhogh / Dhegh) دقیقاً همان‌هاست. والدهٔ–پوکورنی (جلد ۱ ص ۸۴۹) و چونگ (ذیل *daj) نیز همین ریشه را می‌دهند. تنها نکتهٔ فنی این که نورایی واکهٔ لبی‌کامی (gʷh) را نشان نمی‌دهد. در مجموع ادعای نورایی دربارهٔ خود ریشه درست است؛ اما دو شاخهٔ نمودار سست است: شاخهٔ «زغال/زگال» (گرهٔ ۱۲) که جز در فرهنگ من (Mann) به این ریشه بسته نمی‌شود، و شاخهٔ «گداختن/گدازیدن» (گره‌های ۶–۷) که خود مأخذ نورایی، یعنی نیبرگ جلد ۲ ص ۲۱۷، آن را به ریشهٔ دیگری می‌برد.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/d%CA%B0eg%CA%B7%CA%B0-\"],\n \"ref_check\": [\n   {\"ref\":\"POK:240\",\"status\":\"supports\",\"note\":\"POK_01.txt, page block printed '240': 'dhegʷh- „brennen‘; Nominalbildungen dhogʷho-s, dhegʷh-ro-s. Ai. dáhati, av. dažaiti „brennt‘ ... npers. dāγ „Brandmal‘ ...; av. daxsa- m. „Brand‘'. Exactly the root box as drawn (grep -n 'dheg' POK_01.txt → line 3411 ff.).\"}\n ],\n \"consulted\": [\n   {\"src\":\"WLD\",\"where\":\"Bd. I 849 (WLD_Bd1 djvu lines 53484 ff.)\",\"stance\":\"supports\",\"note\":\"'dhegʷh- „brennen‘. Ai. dahati, av. dazaiti „brennt‘ ... np. dāγ „Brandmal‘; av. daxsa- m. „Brand‘ ... lat. febris „Fieber‘ *dhegʷhris'. The source Pokorny 240 f. abridges; note that neither WP nor Pokorny lists Germanic *dagaz here.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *daj 'to burn' (CHEUNG.txt lines 4546–4590)\",\"stance\":\"supports\",\"note\":\"'*daj “to burn” ... YAv. daž- “to burn” ... BMP dc- /daz-/ “to burn” ... NP dag “hot; brand, mark(ing)” ... «PIE *dʰegʷʰ- “to burn” = LIV: 133 f. | Pok.: 240 f.»'\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985, d-list and index (AHD_watkins1985.txt)\",\"stance\":\"silent\",\"note\":\"the 1985 appendix has no dhegʷh- root at all and FEVER is absent from its word index (the index runs 'FEUILLETON bhel-3 / FEVERFEW bheug-1 / FEW pau-'); its DAY and DAWN are indexed to agh-², not to a burn-root.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann, s.v. dheguho (IEC.txt line 2737)\",\"stance\":\"supports\",\"note\":\"'dheguho (dhoguh-) “burn, fire”. Cf. dheguhlos, dheguhro-, dheguhto- and guheguh-. WP I, 849. Skt. dahàmi; Av. dažai-; ... Lat. foveo' — same root, and Mann's cross-reference to his 'guheguh-' is what node 12 rests on.\"}\n ],\n \"nodes\": []\n}\n\nN = root[\"nodes\"]\n\nN.append({\n \"id\":1,\"lang\":\"Avestan\",\"words\":\"dağa, dâğah; daxša; daxma\",\n \"verdict\":\"disputed\",\n \"derivation\":\"Two of the three words are solid, the third is not. (a) daγa-: Bartholomae, AiW 12795, lists 'j. daγa- m. — ? —' at Vd. 7.4, i.e. the form is attested but he leaves the meaning open; Hübschmann, Persische Studien 247 §139, equates it directly with the New Persian word – 'dāγ “Brandmal, Fleck, Wunde, Brenneisen”, zd. daγa-' – and Wiktionary glosses Avestan daγa- 'brand; scar, spot'. Nourai's gloss 'hot' is the modern Persian sense read back into Avestan; the second form 'dâğah' (a supposed *dāγah-) is not in Bartholomae and looks like Nourai's own lengthened variant. (b) daxša-: confirmed – Pokorny 240 prints 'av. daxsa- m. „Brand”' (a fire, a burning), from *dag-s-a-, an s-extension of the root; Gershevitch, AHM p.181 n.27, writes 'Av. daxsa- “fire, Brand” + to dag- “burn”'. Nourai's 'burnt' is a shade off ('brand, fire', not a participle). (c) daxma-: disputed. Bartholomae AiW 12594–12598 does derive it from the burn-root ('eig. „Verbrennungsstätte“, zu V dag-'), and Nourai follows him, but modern Iranian scholarship rejects this: Wiktionary and the standard treatments derive Av. daxma- < *daf-ma- < PIE *dʰm̥bʰ- 'to dig, bury' (root *dʰembʰ-, Pokorny 248), cognate with Armenian damban and Greek táphos 'tomb'. The semantics decide it: a dakhma is precisely where Zoroastrians do NOT burn the dead – corpses are exposed, because fire must not be polluted – so Nourai's gloss 'place for burning the dead' is doubly wrong.\",\n \"derivation_fa\":\"از سه واژهٔ این جعبه دوتا درست است و یکی نه. نخست، صورت اوستایی daγa- واقعاً هست (وندیداد ۷٪۴)، اما بارتولومه در فرهنگ خود معنای آن را نامعلوم می‌گذارد و هوبشمان (ص ۲۴۷) آن را همان «داغ» فارسی به معنای «نشان سوختگی، لکه، داغ‌آهن» می‌داند؛ پس معنای «گرم» که نورایی داده معنای فارسی نو است که به اوستایی بازتابانده شده، و صورت دوم (dāγah) در هیچ فرهنگی نیست. دوم، daxša- به معنای «آتش، سوختار» در پوکورنی و گرشویچ تأیید می‌شود و از همین ریشه با پسوند -s- ساخته شده است. سوم، daxma-: بارتولومه آن را «جای سوزاندن» و از ریشهٔ dag- دانسته بود و نورایی از او پیروی کرده، ولی پژوهش امروزی آن را رد می‌کند و daxma- را از *dʰm̥bʰ- «کندن، به خاک سپردن» (هم‌ریشه با ارمنی damban و یونانی táphos «گور») می‌گیرد. نکتهٔ معنایی قطعی است: در دخمه مردگان را نمی‌سوزانند بلکه رها می‌کنند تا آتش آلوده نشود؛ پس معنایی که نورایی نوشته («place for burning the dead») هم از نظر ریشه‌شناسی و هم از نظر آیینی نادرست است.\",\n \"sources\":[W+\"%D8%AF%D8%A7%D8%BA\", W+\"%D8%AF%D8%AE%D9%85%D9%87\"],\n \"ref_check\":[\n   {\"ref\":\"POK:240\",\"status\":\"partial\",\"note\":\"POK_01 p.240 has 'av. daxsa- m. „Brand‘' and 'npers. dāγ „Brandmal‘' – so daxša is supported and dāγ is supported as a NEW PERSIAN word, but Pokorny gives no Avestan daγa-/dāγah- and no daxma- under this root.\"},\n   {\"ref\":\"BQT:815\",\"status\":\"supports\",\"note\":\"Borhan-e Qate' vol.2, leaf 276 (printed p. ≈ 815–819 in this scan): headword 'داغ = بر وزن باغ، معروف است' with Mo'in's footnote referring to 'اشتقاق و هوبشمان ۲۴۷' – i.e. to Hübschmann p.247, the page that equates np. dāγ with zd. daγa-.\"},\n   {\"ref\":\"BQT:827\",\"status\":\"supports\",\"note\":\"Borhan-e Qate' vol.2, leaf 285 (printed p. ≈ 827–828): the 'دخمه' entries, with Mo'in's etymological footnote reading 'اوستا daxma-؛ پهلوی ...' – the Avestan→Pahlavi→Persian chain, though without an IE root.\"}\n ],\n \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"AiW s.v. daγa- (BRT.txt line 12795) and daxma- (lines 12594–12598)\",\"stance\":\"partial\",\"note\":\"'j. daγa- m. — ? —' (meaning left open, V.7.4); 'j. daxma- m. „Leichenstätte, Leichenbestattungsort“ ... eig. „Verbrennungsstälte“, zu V dag- ... np. daxm, daxma. — Pāz.: daxmai'. Bartholomae supports Nourai on daxma but leaves daγa- unglossed.\"},\n   {\"src\":\"HUB\",\"where\":\"Persische Studien p.247 §139 (HUB.txt leaf 257)\",\"stance\":\"supports\",\"note\":\"'dāγ „Brandmal, Fleck, Wunde, Brenneisen“, zd. daγa-' – in the list of Old Persian/Avestan g after vowels giving NP γ.\"},\n   {\"src\":\"PHD\",\"where\":\"MacKenzie p.24 s.vv. (PHD.txt line 306)\",\"stance\":\"supports\",\"note\":\"'daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction)' and 'dazidan, daz- [dc-ytn'] burn, scorch' – note MacKenzie's own definition: corpses are EXPOSED, not burned.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *daj (CHEUNG.txt line 4570)\",\"stance\":\"supports\",\"note\":\"'NP dag “hot; brand, mark(ing)”' listed among the NWIr. continuants of *daj 'to burn'.\"}\n ],\n \"derivation_note\":None\n})\n\nN.append({\n \"id\":2,\"lang\":\"Persian\",\"words\":\"dâğ «داغ»; daxš 2 «دخش ۲»; daxmeh «دخمه»\",\n \"verdict\":\"disputed\",\n \"derivation\":\"(a) داغ dāγ 'hot; brand, cautery mark' is confirmed and is the one word on the page that everybody agrees about: Old Iranian *daγa- (Av. daγa-) > MP dāg > NP dāγ; intervocalic/final Old Iranian -g- became the fricative -γ (Hübschmann PSt 247 §139 gives it in his list of ap./zd. g > np. γ, beside murγ, roγan, dūγ), and the adjectival sense 'hot' is a New Persian extension of 'brand, burn-mark'; Pokorny 240 and Cheung s.v. *daj both cite it. (b) دخش daxš 'dark': the word exists – Dehkhoda gives daxš (2) 'تیره و تاریک' beside daxš (1) 'ابتدا کردن کار' – and Nourai's reference FSF:173 (Noushin's Shahnameh glossary) has exactly the Ferdowsi line he quotes; but Noushin's own entry warns that the London, Cairo and Leningrad manuscripts read رخش raxš for دخش at these lines, so the word is a textual reconstruction, and no source derives it from Av. daxša- 'brand'. The step 'burnt' > 'dark' is Nourai's own semantic bridge; plausible but unsupported. (c) دخمه daxma 'tomb' is a straight inheritance Av. daxma- > MP daxmag [dhmk'] > NP daxma (loss of final -g after the vowel, the regular MP > NP development, cf. bāndag > banda); the word is right, but as at node 1 the root assignment is disputed: modern scholarship takes daxma- to *dʰm̥bʰ- 'to dig, bury', not to *dʰegʷʰ- 'to burn'.\",\n \"derivation_fa\":\"از سه واژه، مسلّم‌ترین «داغ» است: ایرانی باستان *daγa- (اوستایی daγa-) > فارسی میانهٔ dāg > فارسی نو «داغ»؛ گـ ایرانی باستان پس از واکه به سایشی غ بدل شده است (هوبشمان ص ۲۴۷، در کنار مرغ، روغن، دوغ)، و معنای صفتی «گرم» گسترش معنایی متأخّر از «نشان سوختگی» است. دوم، «دخش»: دهخدا معنای «تیره و تاریک» را می‌آورد و نوشین در واژه‌نامک همین بیت فردوسی را شاهد می‌آورد؛ امّا خود نوشین تصریح می‌کند که در دستنویس‌های لندن و قاهره و لنینگراد به‌جای «دخش» «رخش» ضبط شده؛ بنابراین خود واژه تصحیح قیاسی است و هیچ مأخذی آن را از daxša- اوستایی نگرفته است؛ راه معنایی «سوخته > تیره» ساختهٔ خود نورایی است. سوم، «دخمه» از اوستایی daxma- و فارسی میانهٔ daxmag است (افتادن گـ پایانی در فارسی نو، مانند بنده < bandag)، ولی انتساب آن به ریشهٔ «سوختن» مورد قبول پژوهش امروزی نیست.\",\n \"sources\":[W+\"%D8%AF%D8%A7%D8%BA\", W+\"%D8%AF%D8%AE%D9%85%D9%87\", \"https://www.vajehyab.com/dehkhoda/%D8%AF%D8%AE%D8%B4\"],\n \"ref_check\":[\n   {\"ref\":\"FSF:173\",\"status\":\"partial\",\"note\":\"Noushin, Vāžanamak, s.v. دخش (FSF_pages.txt lines 11347–11420, leaf 226): the entry carries exactly Nourai's Ferdowsi couplet ('بخواه آنچ خواهی و دیگر ببخش / مکن بر دل ما چنین روز دخش' and 'مکن روز بر دشمن و دوست دخش'), but adds 'در نسخه‌های لندن و قاهره و لنینگراد به جای دخش «رخش» ضبط است' — the word, not the etymology; Noushin gives no Avestan source.\"}\n ],\n \"consulted\":[\n   {\"src\":\"HUB\",\"where\":\"PSt 247 §139\",\"stance\":\"supports\",\"note\":\"'dāγ „Brandmal, Fleck, Wunde, Brenneisen“, zd. daγa-'\"},\n   {\"src\":\"HRN\",\"where\":\"Grundriss no. 529 (HRN.txt line 4759)\",\"stance\":\"supports\",\"note\":\"'529. dāγ „Brandmal“, deγ.' — Horn's own headword for the Persian word.\"},\n   {\"src\":\"PHD\",\"where\":\"MacKenzie p.24\",\"stance\":\"supports\",\"note\":\"'daxmag ... tomb, dakhma'; 'dazidan, daz- burn, scorch' — the Middle Persian links Nourai leaves out of the chart.\"},\n   {\"src\":\"MON\",\"where\":\"Dehkhoda/Mo'in via vajehyab, s.v. دخش\",\"stance\":\"partial\",\"note\":\"Dehkhoda: دخش (1) 'ابتدا کردن کار باشد'; (2) 'تیره و تاریک' — the gloss 'dark' is right, the etymology is not given.\"}\n ]\n})\n\nN.append({\n \"id\":3,\"lang\":\"Avestan\",\"words\":\"daxš 2, rax, rak; fra-daxšanâ\",\n \"verdict\":\"plausible\",\n \"derivation\":\"This box condenses two footnotes of Gershevitch's Avestan Hymn to Mithra, and condenses them too far. Note 27 (p.181) is about Yt.10.34 rəxšyant-: 'I regard rəxšya- as a denominative of *rəxša- “defiance”, which in its turn would be a verbal noun formed from the -s- extension of a base *rax- or *rək-', and Gershevitch's parallels for that kind of s-extension are 'Av. daxsa- “fire, Brand” + to dag- “burn”, Sogd. ʔwyšʔ “cauldron” to pak- “cook”, and Av. fra-daxs-'. So 'rax, rak' are Gershevitch's reconstructed bases behind an attested participle, not Avestan lemmata, and their sense is 'to defy', not 'to hurt (burn)'; only daxša- 'fire' is really 'burn'. Note 394 (pp.192 f.) gives 'fradaxsanya-, adj. to fradaxsana- “sling”'; the noun itself is well attested – Bartholomae AiW s.v. 'j. fradaxšanā- f. „Schleuder“ als Waffe' (Vd.14.9, thirty sling-stones) and fradaxšanya- 'Schleuderstein' (Vd.17.9, Yt.10.39) – but Bartholomae writes flatly 'Ableit. – fra-daxš-; Et.?': he knows the derivational base and declares the etymology unknown. Nourai's gloss 'a device to hurt or strike from a distance' is a good description of the object; the claim that the base means 'burn' rests only on the analogy Gershevitch draws with daxša-, which he does not extend to fra-daxš-.\",\n \"derivation_fa\":\"این جعبه دو پانوشت از کتاب گرشویچ (سرود مهر در اوستا) را در هم فشرده است. در پانوشت ۲۷ (ص ۱۸۱) گرشویچ rəxšya- را فعلی از اسم *rəxša- «گردنکشی» می‌داند که خود از ستاک *rax-/*rək- با پسوند -s- ساخته شده، و فقط برای نمونه می‌افزاید که daxša- «آتش» نیز از dag- «سوختن» همین‌گونه ساخته شده است. پس «rax, rak» واژهٔ اوستایی نیست، ستاکی بازساخته است و معنایش هم «آزردن/سوزاندن» نیست. دربارهٔ fradaxšanā- «فلاخن، قلاب‌سنگ» خود واژه کاملاً ثابت است (وندیداد ۱۴٪۹، با سی سنگ)، امّا بارتولومه صریحاً می‌نویسد «ریشه‌شناسی؟»؛ یعنی وابستگی آن به ریشهٔ «سوختن» قیاسی است و با احتیاط پذیرفتنی است.\",\n \"sources\":[],\n \"ref_check\":[\n   {\"ref\":\"AHM:181\",\"status\":\"partial\",\"note\":\"Gershevitch note 27 (AHM.txt line 1626; leaf 190 = printed p.181, matching the book's own index 'fradaxs-, 181, 192 sq., 324'): 'I regard rəxšya- as a denominative of *rəxša- “defiance” ... formed from the -s- extension of a base *rax- or *rək- (cf. Av. daxsa- “fire, Brand” + to dag- “burn” ... and Av. fra-daxs-, below, note 394)'. Supports the s-extension idea, not the gloss 'to hurt (burn)'.\"},\n   {\"ref\":\"AHM:192\",\"status\":\"supports\",\"note\":\"Gershevitch note 394 (AHM.txt lines 1734–1737; leaf 202 = printed pp.192 f.): 'fradaxsanya-, adj. to fradaxsana- “sling”. This, according to Da., ZA, III, 215, is glossed by NPers. falaxan.'\"}\n ],\n \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"AiW s.vv. fradaxšanā-, fradaxšanya-, fradaxštanā- (BRT.txt lines 17604–17612)\",\"stance\":\"partial\",\"note\":\"'j. fradaxšanā- f. „Schleuder“ als Waffe: ... „.. Schleuder mit dreissig Schleudersteinen“ ... Ableit. — fra-daxš'; Et.?' — Bartholomae accepts the word and its derivational base but marks the etymology as unknown.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *daj, Sogdian section (CHEUNG.txt lines 4576–4580)\",\"stance\":\"contradicts\",\"note\":\"'MSogd. δxš- “to give pain, hurt”, which is often cited (e.g. Gharib 1995: 147, no. 3719), does not exist' — Cheung deletes precisely the 'daxš = to hurt' equation this node rests on.\"},\n   {\"src\":\"KNT\",\"where\":\"Old Persian lexicon (KNT.txt)\",\"stance\":\"silent\",\"note\":\"no Old Persian *daxš-/*rax- comparanda; the Achaemenid corpus has nothing bearing on this node.\"}\n ]\n})\n\nN.append({\n \"id\":4,\"lang\":\"Persian\",\"words\":\"falâxon «فلاخن ( فلاخان ، فلخمان ، فلخم )»\",\n \"verdict\":\"plausible\",\n \"derivation\":\"That NP فلاخن falāxan 'sling' answers to Avestan fradaxšanā- is old and generally accepted – Darmesteter (Zend-Avesta III 215) already glossed the Avestan word by the Persian one, and Gershevitch repeats it in the note Nourai cites. What Nourai draws as a straight Avestan→Persian descent is, however, a loan in every modern account, because the Persian form is phonetically not what a direct descendant would look like: *fra-daxšanā- would give Persian *fraδašan/*fardašan, not falāxan. Gershevitch's own solution on the very page cited (n.394) is that 'the latter, if it is a Sogdian LW, belongs perhaps to the same base as Av. fra-daxš-, without the s-extension ..., as it may represent Sogd. *βāxan < *fra-dax(a)na-'; Wiktionary reconstructs the same shape but routes it through Bactrian ('From Old Iranian (compare Avestan fradaxš̃anā “sling”), probably via Bactrian'). Either way the chain is Old Iranian *fra-daxana- > an eastern Iranian form with initial β-/f- and loss of the -š- > borrowed into Persian, where fr- > fal- by dissimilation of r to l before the following -x-; the by-forms Nourai prints (فلاخان، فلخمان، فلخم) are the usual Persian and Turkic-mediated variants (Chagatai palaxmon). Plausible: right comparison, wrong arrow-type (borrowing, not inheritance).\",\n \"derivation_fa\":\"پیوند «فلاخن» با fradaxšanā- اوستایی کهن و پذیرفته است — دارمستتر در ترجمهٔ اوستا (ج ۳ ص ۲۱۵) واژهٔ اوستایی را با همین واژهٔ فارسی معنا کرده است — امّا راه آن وام‌گیری است نه میراث مستقیم؛ زیرا اگر مستقیم می‌بود باید در فارسی چیزی مانند *فردشن می‌شد، نه «فلاخن». خود گرشویچ در همان پانوشت می‌گوید که این واژه احتمالاً وام‌واژه‌ای سغدی از *βāxan < *fra-dax(a)na- است و ویکی‌واژه راه باختری (بلخی) را پیشنهاد می‌کند. در هر دو حالت، رـ آغازین به لـ بدل شده (ابدال r > l) و صورت‌های دیگر (فلاخان، فلخمان) گونه‌های درون‌فارسی و ترکی اند. پس ادعای نورایی در اصل درست است ولی پیکان نمودار باید وام‌گیری را نشان می‌داد.\",\n \"sources\":[W+\"%D9%81%D9%84%D8%A7%D8%AE%D9%86\"],\n \"ref_check\":[\n   {\"ref\":\"AHM:192\",\"status\":\"partial\",\"note\":\"AHM n.394 (printed pp.192 f.): 'fradaxsanya-, adj. to fradaxsana- “sling”. This, according to Da., ZA, III, 215, is glossed by NPers. falaxan. The latter, if it is a Sogdian LW, belongs perhaps to the same base as Av. fra-daxs-, without the s-extension ..., as it may represent Sogd. *βāxn < *fra-dax(a)na-.' — supports the equation but makes it a loan, not the descent Nourai draws.\"},\n   {\"ref\":\"MON:2564\",\"status\":\"partial\",\"note\":\"Mo'in, Farhang-e Fārsi (2-vol. Adena reprint, MON_part1.txt line 24799 f.): '[- فلاخن] (ا.) کفه‌ای باشد که از ابریشم یا از پشم ببافند و دو ریسمان بر دو طرف آن بگذارند و شاطران و شبانان بدان سنگ اندازند' — confirms the meaning 'sling'; the reprint's pagination differs from Nourai's 6-vol. edition so p.2564 itself could not be checked, and Mo'in gives no Avestan source here.\"}\n ],\n \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"AiW s.v. fradaxšanā-\",\"stance\":\"partial\",\"note\":\"'Ableit. — fra-daxš'; Et.? — Pü.: knpdnn s. dazu HORN ZDMG. 46, 39, DRM. ZA. 3, 215' — Bartholomae himself points to Darmesteter III 215, i.e. to the falaxan equation.\"},\n   {\"src\":\"HRN\",\"where\":\"Grundriss (HRN.txt)\",\"stance\":\"silent\",\"note\":\"Horn has no numbered entry for falāxan; grep 'falax|falā' in HRN.txt returns nothing.\"},\n   {\"src\":\"SOD\",\"where\":\"Gharib, Sogdian Dictionary\",\"stance\":\"silent\",\"note\":\"no Sogdian *βāxan/βʾyn is entered; Gershevitch's *βāxn is a reconstruction, not an attested Sogdian word.\"}\n ]\n})\n\nN.append({\n \"id\":5,\"lang\":\"Sogdian\",\"words\":\"dğm`y\",\n \"verdict\":\"transcription_suspect\",\n \"error_in\":\"book\",\n \"book_prints\":\"dğm`y : grove\",\n \"correct_form\":\"δγmʾyh (δaxmē) 'tomb, grave'\",\n \"derivation\":\"The form is right and the gloss is wrong by one letter. Nourai's source, Gharib's Sogdian–Persian–English Dictionary, entry 3532 on p.139 – exactly the page he cites – reads 'δγmʾyh / δaxme ©Av. daxma-, Parth. dxmg ©pl. -th: tomb, grave'. Nourai printed 'grove' for Gharib's 'grave': a misreading in the book itself (the extraction from the PDF is faithful – the printed page 104 shows 'grove'). Once corrected, the node is a Sogdian cognate δaxmē 'tomb' beside Parthian dxmg and Avestan daxma-, i.e. it belongs under node 1's daxma, not as a separate branch off the root – and it inherits daxma's disputed root assignment (*dʰm̥bʰ- 'to bury', not *dʰegʷʰ- 'to burn'). Gharib herself derives it from Av. daxma-, saying nothing about an IE root.\",\n \"derivation_fa\":\"صورت واژه درست است ولی معنا یک حرف جابه‌جا شده است. در فرهنگ سغدیٔ بدرالزمان قریب، مدخل ۳۵۳۲ در صفحهٔ ۱۳۹ — همان صفحه‌ای که نورایی ارجاع داده — چنین آمده است: «δγmʾyh / δaxme، از اوستایی daxma-، پارتی dxmg: tomb, grave». نورایی grave را grove خوانده و همان را چاپ کرده است؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن (در صفحهٔ ۱۰۴ چاپی هم grove آمده). پس از درست‌کردن، این گره هم‌ریشهٔ «دخمه» است و باید زیر همان گرهٔ ۱ می‌آمد، نه شاخه‌ای جداگانه از ریشه؛ و همان اختلاف ریشه‌شناختی دخمه را هم به ارث می‌برد.\",\n \"sources\":[],\n \"ref_check\":[\n   {\"ref\":\"SOD:139\",\"status\":\"contradicts\",\"note\":\"Gharib, Sogdian Dictionary, p.139 (SOD_pages.txt \\\\f-block 205, whose first line is the running page number '139'), entry '3532 δymʾy [= δγmʾy] δaxme ©Av. daxma-, Parth. dxmg ©pl. -th | tomb, grave | BSTBL, Dhu. 212'. The page Nourai cites is correct and the Sogdian form is correct, but Gharib's gloss is 'tomb, grave', not 'grove'.\"}\n ],\n \"consulted\":[\n   {\"src\":\"PHD\",\"where\":\"MacKenzie p.24 s.v. daxmag\",\"stance\":\"supports\",\"note\":\"'daxmag [dhmk' | P dxmg, N ~a] tomb' — P(arthian) dxmg is the very Parthian form Gharib cites beside the Sogdian one.\"},\n   {\"src\":\"BRT\",\"where\":\"AiW s.v. daxma-\",\"stance\":\"supports\",\"note\":\"'j. daxma- m. „Leichenstätte“ ... np. daxm, daxma' — the Avestan etymon Gharib gives for the Sogdian word.\"},\n   {\"src\":\"SOD\",\"where\":\"Gharib, entries 3530–3532 (p.139)\",\"stance\":\"partial\",\"note\":\"the same page has '3530 δy- δay (to) burn' and '3531 δyʾn δay/xan ardent, fiery' — real Sogdian reflexes of the burn-root, which would have made a better node than the misread δaxmē.\"}\n ]\n})\n\nN.append({\n \"id\":6,\"lang\":\"Avestan\",\"words\":\"dažaiti; vi-dâz\",\n \"verdict\":\"disputed\",\n \"derivation\":\"dažaiti is impeccable: Young Avestan dažaiti '(it) burns' (Y.71.8), from *daj-ia-, the ja-present of Proto-Iranian *daj- < PIE *dʰegʷʰ-; Pokorny 240 pairs it with Skt. dáhati and Lith. degù, Cheung 2007 s.v. *daj lists it first, and Klein s.v. 'day' cites 'Avestic dazaiti, “burns”' on the very page (404) Nourai gives. 'vi-dâz “to melt”' is another matter: there is no Avestan vī-daž-. Bartholomae records only apa-daž- and ham-daz- as preverbal compounds of daž- (Cheung s.v. *daj lists the same two and no *ui-), and a grep of the Altīranisches Wörterbuch for vi-daž/vīdāz returns nothing. What exists is Middle Persian widāxtan / widāz- 'to melt', which Nourai has back-projected into Avestan with an Avestan-looking hyphen; and that Middle Persian verb is assigned by Nyberg and Cheung not to daž- 'burn' but to *taH(č) 'to melt' (see node 7). So the node is half confirmed, half a construct, and the half that carries the Persian branch is the constructed half.\",\n \"derivation_fa\":\"dažaiti کاملاً درست است: فعل جوان‌اوستایی «می‌سوزد» (یسنا ۷۱٪۸) از ستاک حال *daj-ia-، ایرانی آغازین *daj-، هندواروپایی *dʰegʷʰ-؛ پوکورنی آن را با dáhati سنسکریت و degù لیتوانی می‌سنجد و کلاین نیز در همان صفحهٔ ۴۰۴ که نورایی ارجاع داده آن را می‌آورد. امّا «vi-dāz» اوستایی وجود ندارد: بارتولومه فقط apa-daž- و ham-daz- را ثبت کرده و چونگ هم همین دو را؛ آنچه هست فارسی میانهٔ widāxtan/widāz- «گداختن» است که نورایی آن را به قالب اوستایی ریخته است — و همین فعل را نیبرگ و چونگ نه از daž- «سوختن» بلکه از ریشهٔ *taH(č) «گداختن» می‌دانند. پس نیمی از این جعبه درست است و نیمی ساختگی، و بدبختانه همان نیمهٔ ساختگی است که شاخهٔ فارسی را نگه می‌دارد.\",\n \"sources\":[W+\"%DA%AF%D8%AF%D8%A7%D8%AE%D8%AA%D9%86\"],\n \"ref_check\":[\n   {\"ref\":\"NYB:217\",\"status\":\"contradicts\",\"note\":\"Nyberg, Manual of Pahlavi II 217 (NYB_vol2_glossary.txt line 4248): 'vitāxtan vitāc- trans. to melt: bē witācēt 101.77. — Caus. of vi + Av. (624 sq.) tak-; MPrth wdxtn, wdc- ...; Pāz. vadāxtan vadāž-; NP gudāxtan gudāz- “to liquify”.' Nourai's own reference derives the melt-verb from Av. tak-, not from daž-. (Cheung's bibliography for *taH cites exactly 'Nyberg II: 217a', confirming the page.)\"},\n   {\"ref\":\"KLN:404\",\"status\":\"supports\",\"note\":\"Klein, Comprehensive Etym. Dict. (1966) s.v. 'day' (KLN_1966.txt line 10395, leaf 223 ≈ pp.402–404): '... fr. I.-E. base *dhegʷh-, *dhogʷh-, “to burn”, whence also OI. dahati, “burns”, ... Avestic dazaiti, “burns” ...' — supports dažaiti under this root.\"}\n ],\n \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"AiW s.v. daž- and its compounds\",\"stance\":\"partial\",\"note\":\"daž- and apa-daž-/ham-daz- are entered; a search of BRT.txt for 'vi-daž', 'vidaž', 'vīdāz' returns nothing — the compound Nourai prints is not in Bartholomae.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *daj (CHEUNG.txt lines 4546–4551)\",\"stance\":\"partial\",\"note\":\"'YAv. daž- “to burn” || (+ *apa-) “to damage by burning” || (+ *ham-) “to burn” ... Pres. ja: IND. 3sg. YAv. dažaiti (Y 71.8)' — dažaiti confirmed; no *ui-daž- among the preverbal compounds.\"},\n   {\"src\":\"PHD\",\"where\":\"MacKenzie pp.24, 90\",\"stance\":\"partial\",\"note\":\"'dazidan, daz- burn, scorch' (the real MP continuant of daž-) is kept separate from 'widāxtan, widāz- [wtʾahtn', wtc-] melt, dissolve' — two different verbs in Middle Persian.\"}\n ]\n})\n\nN.append({\n \"id\":7,\"lang\":\"Persian\",\"words\":\"godâzîdan «گدازیدن ( جانگداز )»\",\n \"verdict\":\"disputed\",\n \"derivation\":\"گداختن / گدازیدن gudāxtan, gudāzīdan 'to melt' is a real Persian verb (Mo'in: 'گداز [= گدازیدن، گداختن] ... ذوب'), continuing Middle Persian widāxtan / widāz- <wtʾahtn', wtc-> — vi- 'apart, away' + the root, with MP wi- > NP gu- (the same development as widar- > گذر, widang > گدنگ); gudāzīdan is a secondary -īdan formation on the present stem gudāz-, and جانگداز jān-gudāz 'soul-melting' is the familiar compound of it. What is wrong is the root: Nyberg (Manual of Pahlavi II 217a) analyses vitāxtan as 'Caus. of vi + Av. tak-', and Cheung's Etymological Dictionary of the Iranian Verb puts MP widāz-/widāxtan and 'NP gudāxtan/gudāz- “to smelt, melt”' under *taH 'to melt', 'PIE “enlarged” *teH₂k- “to melt” = LIV: 617 | Pok.: 1053', with Greek tḗkō as the cognate — and he expressly excludes the homophonous root 'to run, walk' (*tač¹). Wiktionary follows Cheung. The Pahlavi spelling settles it: the present stem is written <wtc-> /widāz-/ with c = /z/ from *-č-, the regular outcome of *tak-/*taHč-, not of daž-. So node 6 → 7 is disputed: the chart's own NOTE ('Compare with derivations from root Teku 1: to flow, run') half-registers the problem, and modern scholarship comes down on that side, though it separates 'melt' (*teh₂-k-) from 'run, flow' (*tekʷ-).\",\n \"derivation_fa\":\"«گداختن / گدازیدن» فعلی اصیل است و از فارسی میانهٔ widāxtan / widāz- می‌آید؛ پیشوند wi- در فارسی نو به gu- بدل شده است (همان‌گونه که widar- > گذر)، و «گدازیدن» مصدر ثانویی از ستاک حال «گداز-» است و «جانگداز» مرکّب معروف همین. امّا ریشه‌ای که نورایی داده نادرست است: نیبرگ — که خود نورایی به او ارجاع داده (ج ۲ ص ۲۱۷) — آن را «سببی از vi + tak- اوستایی» می‌داند و چونگ در فرهنگ ریشه‌شناختی فعل ایرانی آن را زیر *taH «گداختن»، هندواروپایی *teh₂k- (پوکورنی ۱۰۵۳، هم‌ریشه با tḗkō یونانی) می‌آورد. نوشتار پهلوی هم گواه است: ستاک حال <wtc-> است که زِ آن از *-č- بازمانده، نه از daž-. پس پژوهش امروزی این پیکان را رد می‌کند؛ یادداشت خود نورایی («با مشتقّات ریشهٔ Teku مقایسه شود») نیمه‌راه درست است، جز آنکه چونگ «گداختن» را از «تاختن/روان شدن» جدا می‌کند.\",\n \"sources\":[W+\"%DA%AF%D8%AF%D8%A7%D8%AE%D8%AA%D9%86\"],\n \"ref_check\":[\n   {\"ref\":\"MON:3199\",\"status\":\"partial\",\"note\":\"Mo'in, Farhang-e Fārsi (2-vol. reprint, MON_part2.txt line 30054): 'گداز [- - گدازیدن، گداختن] (امص.) ... ذوب' — confirms the word and that gudāzīdan is a by-form of gudāxtan; the reprint's pagination differs from the 6-vol. edition so p.3199 itself could not be checked, and no etymology is given there.\"},\n   {\"ref\":\"BQT:1777\",\"status\":\"not_checked\",\"note\":\"p.1777 falls in Borhan-e Qate' vol. 3, for which only page images (no OCR text) are available locally; not fetched for this node because the two decisive references (Nyberg 217, Cheung s.v. *taH) were readable and agree with each other.\"}\n ],\n \"consulted\":[\n   {\"src\":\"NYB\",\"where\":\"Manual of Pahlavi II 217a s.v. vitāxtan\",\"stance\":\"contradicts\",\"note\":\"'vitāxtan vitāc- trans. to melt ... Caus. of vi + Av. (624 sq.) tak- ... NP gudāxtan gudāz- “to liquify”'\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *taH 'to melt' (CHEUNG.txt lines 24484–24535)\",\"stance\":\"contradicts\",\"note\":\"'*taH “to melt” ... (+ *ui-) MMP wdc- “to melt [intr.]”, BMP wtʾc- /widāz-/ ... NWIR: (+ *ui-) NP gudāxtan/gudāz- “to smelt, melt” ... «PIE “enlarged” *teH₂k- “to melt” = LIV: 617 | Pok.: 1053» ... REFERENCES: Horn 1893: 199; Nyberg II: 217a'\"},\n   {\"src\":\"PHD\",\"where\":\"MacKenzie p.90 s.v. widāxtan\",\"stance\":\"partial\",\"note\":\"'widāxtan, widāz- [wtʾahtn', wtc- | (P wdʾc-), N gudaxtan, gudāz-] melt, dissolve' — the Pahlavi spelling <wtc-> points to *-č-, i.e. to the melt-root, not to daz-.\"},\n   {\"src\":\"HRN\",\"where\":\"Grundriss no. ~199 (cited by Cheung as 'Horn 1893: 199')\",\"stance\":\"contradicts\",\"note\":\"Cheung's reference list for *taH cites Horn p.199 for gudāxtan, i.e. Horn too treats it with the melt-verbs, not under dāγ/daž- (Horn no. 529).\"}\n ]\n})\n\nN.append({\n \"id\":8,\"lang\":\"Latin\",\"words\":\"febris\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Latin febris, -is f. 'fever' goes back to *dʰegʷʰ-ri- with the regular Italic treatment of word-initial *dʰ- > f- (as in facio, fumus, forēs): Pokorny 241 prints 'lat. ... febris „Fieber“ (*dhegʷhro-; nach Leumann Gnom. 9, 226 ff. die i-Flexion nach sitis)', i.e. an original ro-stem remade as an i-stem on the model of sitīs 'thirst'. Walde-Pokorny I 849 gives the same with the semantic parallel 'wie dt. „die Hitzen = Fieber“'. The same root gives Latin foveō 'to warm', fomes 'tinder' and favilla 'glowing ashes', so the Latin box is one of the best-supported nodes on the page.\",\n \"derivation_fa\":\"واژهٔ لاتینی febris «تب» از *dʰegʷʰ-ri- است؛ در ایتالیک واکهٔ *dʰ- آغازین به f- بدل می‌شود (مانند facio، fumus). پوکورنی در صفحهٔ ۲۴۱ می‌نویسد febris < *dhegʷhro- که بعدها به قیاس sitīs «تشنگی» به ستاک i رفته است؛ والده–پوکورنی نیز همین را می‌آورد و موازی معنایی آلمانی «die Hitzen = تب» را یادآور می‌شود. همین ریشه foveō «گرم کردن» و favilla «خاکستر سوزان» را هم داده است. ادعای نورایی درست است.\",\n \"sources\":[\"https://www.etymonline.com/word/fever\", W+\"Reconstruction:Proto-Indo-European/d%CA%B0eg%CA%B7%CA%B0-\"],\n \"ref_check\":[\n   {\"ref\":\"AHD\",\"status\":\"not_found\",\"note\":\"the local Watkins 1985 (AHD_watkins1985.txt) has no *dhegʷh- root and no FEVER in its word index (it runs 'FEUILLETON bhel-3 / FEVERFEW bheug-1 / FEW pau-'). Nourai cites the 1975 New College appendix; whatever it contained, the claim itself is carried by Pokorny 241 and Walde-Pokorny I 849, which do print febris under this root.\"}\n ],\n \"consulted\":[\n   {\"src\":\"POK\",\"where\":\"IEW 241\",\"stance\":\"supports\",\"note\":\"'lat. ... febris „Fieber“ (*dhegʷhro-; nach Leumann Gnom. 9, 226 ff. die i-Flexion nach sitis)'\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I 849\",\"stance\":\"supports\",\"note\":\"'febris „Fieber“ *dhegʷhris, wie dt. „die Hitzen = Fieber“; vgl. zuletzt Wf. IF. 19, 102'\"},\n   {\"src\":\"KLN\",\"where\":\"1966 s.v. 'day' (cross-references)\",\"stance\":\"supports\",\"note\":\"Klein's day-entry ends 'Cp. also favor, febrile, fever, foment, fomes, tephrite' — he groups fever with this root.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann s.v. dheguho (IEC.txt line 2737)\",\"stance\":\"supports\",\"note\":\"'dheguho (dhoguh-) “burn, fire” ... Lat. foveo, tr “warm”; fomes, -mitis ...' — the Latin group under the same root.\"}\n ]\n})\n\nN.append({\n \"id\":9,\"lang\":\"English\",\"words\":\"fever\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"An early Latin loan into Germanic, not a native inheritance: Latin febris was borrowed into West Germanic and appears as late Old English fefor, fefer 'fever', whence Middle English fever; the modern spelling with -v- follows Old French fievre (itself < febrem). Etymonline: 'late Old English fefor, fefer “fever, temperature of the body higher than normal,” from Latin febris “fever” ... The Latin word was borrowed by German, Swedish, Danish but not Dutch; the English spelling was influenced by Old French fievre.' So the Latin→English arrow as drawn is right, with the qualification that the transfer is a borrowing (and it is why English has fever rather than a native *dow-word).\",\n \"derivation_fa\":\"«fever» انگلیسی وام‌واژه‌ای است نه میراث بومی: لاتینی febris در دورهٔ کهن به ژرمنی غربی راه یافته و در انگلیسی کهن fefor / fefer شده، سپس انگلیسی میانه fever؛ املای امروزی با v زیر تأثیر fievre فرانسهٔ کهن است. پس پیکان لاتین ← انگلیسی درست است، با این توضیح که وام‌گیری است.\",\n \"sources\":[\"https://www.etymonline.com/word/fever\"],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book; the chain is uncontroversial and is covered by Etymonline and Klein.\"}],\n \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"1966 s.v. 'day', cross-reference list\",\"stance\":\"supports\",\"note\":\"'Cp. also favor, febrile, fever, foment, fomes, tephrite' — Klein files fever with this root-family.\"},\n   {\"src\":\"SKT\",\"where\":\"Skeat, Concise Etym. Dict. s.v. fever\",\"stance\":\"supports\",\"note\":\"Skeat likewise takes fever from AS. fefor, borrowed from Lat. febris.\"}\n ]\n})\n\nN.append({\n \"id\":10,\"lang\":\"Germanic\",\"words\":\"dagaz\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Proto-Germanic *dagaz 'day' (Goth. dags, OHG tag, ON dagr, OE dæg) is real; what is contested is whether it belongs here. Klein, the reference Nourai cites, says yes: s.v. 'day' (p.404) 'orig. “burning heat”, fr. I.-E. base *dhegʷh-, *dhogʷh-, “to burn”, whence also OI. dahati ... Avestic dazaiti “burns” ... L. foveō ... Gk. téphra “ashes”', the derivation being *dʰogʷʰ-o- 'the burning (time)' > *dagaz. But Pokorny, on the very page (240) that heads this chart's root, sends the word away: 'über got. dags „Tag“ usw. s. unter *ā̆gher- S. 7'; Walde-Pokorny I 849 likewise lists no Germanic form; and Watkins/AHD 1985 files it under 'agh-². A day (considered as a span of time). Germanic *dagaz (with initial d- of obscure origin)'. The phonological objection is decisive for these authors: *dʰogʷʰ-o- should have given Germanic *dawaz, not *dagaz (Wiktionary: 'the loss of the labialization would be irregular; *dawaz would be expected'), and Kroonen prefers a separate root *dʰeǵʰ- 'day' connected with Indo-Iranian *Háǵ́ʰr̥ (Skt. áhar). So the derivation Nourai draws is one of two standing options, held by Klein and by many handbooks but rejected by Pokorny and Watkins.\",\n \"derivation_fa\":\"*dagaz ژرمنی آغازین «روز» (گوتی dags، آلمانی باستان tag، انگلیسی کهن dæg) واقعی است؛ اختلاف بر سر ریشه است. کلاین — همان مأخذی که نورایی می‌آورد — آن را از *dʰegʷʰ-/*dʰogʷʰ- «سوختن» می‌گیرد (معنای نخستین: «گرمای سوزان»)؛ امّا پوکورنی در همان صفحهٔ ۲۴۰ تصریح می‌کند که «dags گوتی را زیر *ā̆gher- صفحهٔ ۷ ببینید»، و واتکینز (پیوست ریشه‌های AHD) آن را زیر agh-² «روز» می‌آورد و دـ آغازین را «نامعلوم‌الاصل» می‌خواند. ایراد آوایی مهم این است که *dʰogʷʰ-o- در ژرمنی باید *dawaz می‌داد نه *dagaz. پس ادعای نورایی یکی از دو رأی رایج است و با احتیاط پذیرفتنی است.\",\n \"sources\":[W+\"Reconstruction:Proto-Germanic/dagaz\", \"https://www.etymonline.com/word/day\"],\n \"ref_check\":[\n   {\"ref\":\"KLN:404\",\"status\":\"supports\",\"note\":\"Klein 1966 s.v. day (KLN_1966.txt line 10395): 'ME. dai, dei, fr. OE. dæg, rel. to ON. dagr, OS., Dan., Swed., Du. dag, Goth. dags, OHG. tag ... orig. “burning heat”, fr. I.-E. base *dhegʷh-, *dhogʷh-, “to burn” ... Avestic dazaiti, “burns” ... L. dies, “day”, is not cognate. Cp. daisy, dawn ...' — exactly Nourai's arrow.\"}\n ],\n \"consulted\":[\n   {\"src\":\"POK\",\"where\":\"IEW 240\",\"stance\":\"contradicts\",\"note\":\"'über got. dags „Tag“ usw. s. unter *ā̆gher- S. 7' — Pokorny removes the Germanic day-word from this root.\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. agh-²\",\"stance\":\"contradicts\",\"note\":\"'agh-². A day (considered as a span of time). Germanic *dagaz (with initial d- of obscure origin), day, in: a. Old English dæg, day: DAY; (DAISY), TODAY; b. Old English denominative dagian, to dawn: DAWN. [Pok. agher- 7.]'\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I 849\",\"stance\":\"silent\",\"note\":\"the dhegʷh- article lists Indo-Iranian, Greek, Albanian, Latin, Celtic, Baltic, Slavic — no Germanic *dagaz.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann s.v. dheguho (IEC.txt line 2737)\",\"stance\":\"silent\",\"note\":\"Mann's dheguho- article also lists no Germanic day-word.\"}\n ]\n})\n\nN.append({\n \"id\":11,\"lang\":\"English\",\"words\":\"day, dawn\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Within Germanic the two English words are beyond dispute and are correctly drawn from *dagaz: Proto-Germanic *dagaz > Old English dæg > Middle English dai, dei > day; and the Old English denominative verb dagian 'to become day' underlies dawn, which reached its modern form by back-formation from Middle English dawning/dawing (itself from ON dagan) in the 15th–16th c. Watkins lists both under one heading ('Old English dæg, day: DAY; ... Old English denominative dagian, to dawn: DAWN'), as does Klein ('Cp. daisy, dawn'). The node inherits, of course, whatever uncertainty attaches to node 10's link with the burn-root.\",\n \"derivation_fa\":\"در درون ژرمنی این دو واژه هیچ ابهامی ندارند: *dagaz > انگلیسی کهن dæg > انگلیسی میانه dai/dei > day؛ و فعل اشتقاقی dagian «روز شدن» پایهٔ dawn است که در سدهٔ پانزدهم–شانزدهم از dawning به قیاس معکوس پدید آمده است. واتکینز هر دو را زیر یک مدخل می‌آورد. طبعاً تردیدی که در گرهٔ پیشین هست به اینجا هم می‌رسد.\",\n \"sources\":[\"https://www.etymonline.com/word/day\"],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference is printed on this node; the OE > ModE chain is covered by Klein and Watkins, both quoted at node 10.\"}],\n \"consulted\":[\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. agh-²\",\"stance\":\"supports\",\"note\":\"'Old English dæg, day: DAY; (DAISY), TODAY; b. Old English denominative dagian, to dawn: DAWN' — supports the English forms, though from a different PIE root.\"},\n   {\"src\":\"KLN\",\"where\":\"1966 s.v. day\",\"stance\":\"supports\",\"note\":\"'ME. dai, dei, fr. OE. dæg ... Cp. daisy, dawn'\"}\n ]\n})\n\nN.append({\n \"id\":12,\"lang\":\"Indo-European\",\"words\":\"Geulo, Ğuěl, Ğul, Guheguh\",\n \"verdict\":\"plausible\",\n \"derivation\":\"This box is not one reconstruction but three, taken from two books, and only one of the three actually hangs off *dʰegʷʰ-. (a) 'Geulo' is Pokorny's g(e)u-lo- 'glühende Kohle' (IEW 399): Irish gúal 'coal', ON kol, OE col, OHG kolo, Arm. krak — a self-standing root with no Indo-Iranian member at all, and not derived by Pokorny from anything. (b) 'Ğuěl, Ğul' are Mann's ġuél- (ġul-) 'burn; burning, bright, clear' (IEC 407), which does contain the Persian word: 'Skt. jválāmi ... Per. zuγāl “embers” ... (z-gde in OHG chol, kolo “coal” and com. Gmc. cf. ON kol “coal”)' — today reconstructed *ǵʷelH- 'to burn, shine', again an independent root. (c) 'Guheguh' is Mann's gʰegʷʰ- (IEC 379), described by him as an 'assimilated radical, form of dheguho', i.e. *dʰegʷʰ- with the first aspirate assimilated to the second, and it is under this heading that Mann puts 'Per. cf. zuγal, *zaγal “embers” ... OCS žegǫ, žešti “kindle, burn”'. So Nourai's arrow from Dhogh/Dhegh to this box is Mann's guheguh- and nothing else; the other three labels belong to roots that no handbook derives from *dʰegʷʰ-. Both of Nourai's citations are exact and both say what he uses them for; the licence he takes is to merge them into a single 'Indo-European ... coal' box. Plausible rather than confirmed.\",\n \"derivation_fa\":\"این جعبه یک بازساخت نیست، سه بازساخت از دو کتاب است. نخست Geulo همان g(e)u-lo- پوکورنی (ص ۳۹۹) «زغال گداخته» است که فقط صورت‌های ایرلندی، ژرمنی و ارمنی دارد و هیچ صورت هندوایرانی در آن نیست. دوم Ğuěl/Ğul همان مدخل من (Mann) در ص ۴۰۷ است: «سوختن، درخشان» با سنسکریت jválāmi و فارسی zuγāl؛ امروز آن را *ǵʷelH- بازسازی می‌کنند و ریشه‌ای مستقل است. سوم Guheguh همان guheguh- من (ص ۳۷۹) است که خود او آن را «صورت همگون‌شدهٔ dheguho» می‌خواند و زیر همین مدخل «zuγal، *zaγal» فارسی را می‌آورد. پس تنها چیزی که پیوند این جعبه را با ریشهٔ بالایی توجیه می‌کند همین فرضیهٔ همگونی من است؛ هر دو ارجاع نورایی دقیق است ولی آمیختن سه ریشه در یک جعبه کار خود اوست. پس با احتیاط پذیرفتنی است.\",\n \"sources\":[W+\"%D8%B2%D8%BA%D8%A7%D9%84\"],\n \"ref_check\":[\n   {\"ref\":\"IEC:379\",\"status\":\"supports\",\"note\":\"Mann, IEC p.379 (IEC.txt line 5472): 'guheguh-, assimilated radical, form of dheguho, q. v. Cf. WP I, 849. Per. cf. zuγal, *zaγal “embers” beside gazam “sting”; Oss. dzagū “hot poultice” beside qäzäl “charred matter”; ... OCS žegǫ, žešti “kindle, burn”'. This is precisely the link Nourai draws, and it is Mann's own.\"},\n   {\"ref\":\"IEC:407\",\"status\":\"supports\",\"note\":\"Mann, IEC p.407 (IEC.txt line 5237 area, leaf 237): 'ġuél- (ġul-) “burn; burning, bright, clear”. Cf. WP I, 643. Skt. jválāmi ... Per. zuγāl “embers”; ... (z-gde in OHG chol, kolo “coal” and com. Gmc. cf. ON kol “coal” ...)'. Both the Persian word of node 14 and the Germanic forms of node 15 stand under this one Mann heading.\"},\n   {\"ref\":\"POK:399\",\"status\":\"partial\",\"note\":\"Pokorny IEW 399 (POK_02.txt lines 766–772): 'g(e)u-lo- „glühende Kohle“. Mit l-Suffix: ir. gúal „Kohle“ (< *geulo- oder *goulo-); aisl. kol n. „Holzkohle“, ags. col m. „Kohle“, engl. coal, afries. kole f., ahd. kolo m. ... arm. krak „Feuer, glühende Kohlen“.' Supports the form 'Geulo' and its Germanic descendants, but contains no Iranian word and does not connect the root with dhegʷh-.\"}\n ],\n \"consulted\":[\n   {\"src\":\"WLD\",\"where\":\"Bd. I 563 and I 643 (as cited by Pokorny 399 and Mann 407)\",\"stance\":\"partial\",\"note\":\"Pokorny's article closes 'WP. I 563. Andere Möglichkeiten bei W. Schulze Kl. Schr. 479' and Mann refers ġuél- to 'WP I, 643' — i.e. Walde-Pokorny itself keeps the two groups in different articles, as modern handbooks do.\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. g(e)u-lo-\",\"stance\":\"partial\",\"note\":\"'g(e)u-lo-. A glowing coal. Germanic *kulam, *kolam in: a. Old English col, a glowing coal: COAL ... [Pok. g(e)u-lo- 399.]' — Germanic only, no Iranian, no link to a burn-root.\"},\n   {\"src\":\"SYN\",\"where\":\"Buck, Selected Synonyms § 'coal'\",\"stance\":\"silent\",\"note\":\"Buck's coal section gives the Germanic and Celtic group without an Indo-Iranian comparison.\"}\n ]\n})\n\nN.append({\n \"id\":13,\"lang\":\"Avestan\",\"words\":\"skarana, skairya\",\n \"verdict\":\"disputed\",\n \"derivation\":\"Nourai is quoting Horn accurately, but Horn's guess has not survived. Horn, Grundriss no. 742 (p.163) – exactly the page cited – reads: 'sekār, sikar, sukar „Kohle“. aw. sarəniō, skarana (Vd. 14,7) „Brennkohlen“, vergl. skairya- (Vd. 8,95) „Kohlenmeiler“ (Geldner, KZ. 25, 566 n.15); afgh. skōr „Kohle“.' Against this: Bartholomae's Altīranisches Wörterbuch gives 'j. skarana- Adj. (fem. °nā-) „rund“' (round — of the moon's disc, Yt.10.95, Y.5.38), not 'coal', and for the other word only the cautious 'j. skairya- n. eine Art Vorrichtung zur Feuerung' (a kind of firing apparatus, V.8.95), which is at least fire-related. Hübschmann, Persische Studien p.76, comments on Horn's very entry: '742. Unsicher. Darmesteter übersetzt garəmō-skarana- durch “une paire de pinces”, skairya- durch “campement”' — i.e. the two Avestan words are read as 'tongs' and 'encampment' by Darmesteter and the whole etymology is 'uncertain'. Mo'in repeats both positions in his footnote to Borhan-e Qate'. Since neither Avestan word is securely 'coal', and since Pokorny 399 and Mann 407 supply no Avestan member at all, the node as drawn (an Avestan word for 'coal' descending from the IE coal-root) is disputed.\",\n \"derivation_fa\":\"نورایی دقیقاً از هرن نقل می‌کند، امّا حدس هرن پذیرفته نشده است. هرن در مدخل ۷۴۲ (ص ۱۶۳) می‌نویسد: «sekār، sikar، sukar “Kohle”؛ اوستایی sarəniō، skarana (وندیداد ۱۴٪۷) “زغال سوخته”، و skairya- (۸٪۹۵) “کورهٔ زغال‌پزی”». در برابر، بارتولومه skarana- را صفت و به معنای «گرد، گردی» می‌داند (دربارهٔ قرص ماه، یشت ۱۰٪۹۵) و skairya- را فقط «گونه‌ای ابزار آتش‌افروزی» می‌خواند؛ و هوبشمان (ص ۷۶) دربارهٔ همین مدخل هرن می‌نویسد «نامطمئن» و یادآور می‌شود که دارمستتر garəmō-skarana- را «جفت انبر» و skairya- را «اردوگاه» ترجمه کرده است. معین هم در حاشیهٔ برهان قاطع هر دو رأی را می‌آورد. پس پژوهش امروزی این گره را رد می‌کند.\",\n \"sources\":[W+\"%D8%B2%D8%BA%D8%A7%D9%84\"],\n \"ref_check\":[\n   {\"ref\":\"HRN:163\",\"status\":\"supports\",\"note\":\"Horn, Grundriss der neupersischen Etymologie no. 742, p.163 (HRN.txt lines 6462–6466, leaf 184): 'sekār, sikar, sukar „Kohle“. aw. sarəniō, skarana (vd. 14, 7) „Brennkohlen“, vergl. skairya- (vd. 8, 95) „Kohlenmeiler“ (Geldner, KZ. 25, 566 Note 15); afgh. skōr „Kohle“. Hat np. zuγāl „Kohle“ (nur FS) etwas mit sekār zu schaffen?' — Nourai's page is exact; note that Horn puts the zuγāl connection as an open QUESTION.\"},\n   {\"ref\":\"BQT:1150\",\"status\":\"supports\",\"note\":\"Borhan-e Qate' vol.2, leaf 615 (printed p. ≈ 1150–1158), Mo'in's footnote 4 to سکار: 'هرن آن را از ریشهٔ ... اوستایی ... به معنی زغال سوخته دانسته ... و هوبشمان ... وجه اشتقاق را مشکوک می‌داند؛ افغانی skōr' — Mo'in reports Horn's Avestan etymology and Hübschmann's doubt side by side.\"},\n   {\"ref\":\"IEC:379,407\",\"status\":\"not_found\",\"note\":\"neither Mann p.379 (guheguh-) nor p.407 (ġuél-) contains any Avestan form; searched IEC.txt for 'skarana', 'skairya' — no hits anywhere in Mann.\"}\n ],\n \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"AiW s.vv. skarana-, skairya- (BRT.txt lines 26467, 26469)\",\"stance\":\"contradicts\",\"note\":\"'j. skarana- Adj. (fem. °nā-) „rund“: ... Yt. 10.95; 5.38 ...' and 'j. skairya- n. eine Art Vorrichtung zur Feuerung: yō ātrəm °yat kaca ... V. 8.95'. Bartholomae's skarana- is 'round', not 'coal'.\"},\n   {\"src\":\"HUB\",\"where\":\"Persische Studien p.76, ad Horn 742 (HUB.txt lines 2656–2662)\",\"stance\":\"contradicts\",\"note\":\"'742. Unsicher. Darmesteter übersetzt garəmo-skarana- durch „une paire de pinces“, skairya- durch „campement“. Np. zuγāl „glühende Kohle“ belegt Nöldeke aus Shahname III, p.1508, v.214. „Kohle“ heisst ausserdem auch angišt (Nr. 126) und zuγāl ... = jüd.-tat. zuγol, zuwol ..., kas. zuγol etc.'\"},\n   {\"src\":\"POK\",\"where\":\"IEW 399\",\"stance\":\"silent\",\"note\":\"the g(e)u-lo- article has Irish, Germanic and Armenian only — no Avestan, no Iranian.\"}\n ]\n})\n\nN.append({\n \"id\":14,\"lang\":\"Persian\",\"words\":\"sekâr «سکار ( شگار )»; zoğâl «ذغال ( زغال ، ژگال ، زگال )»; sekârŭ «سکارو ، سکاروا ، سکالو»; sekâr âhanj «سکار آهنج»\",\n \"verdict\":\"plausible\",\n \"derivation\":\"All four words are genuine and Nourai's page references are good. Borhan-e Qate' (vol.2, leaf 615, printed p. ≈ 1150–1158) has them in a block: 'سکار: بکسر اول بر وزن شکار، بمعنی زغال و انگشت باشد'; 'سکارو: نان و گوشتی را گویند که بر روی زغال افروخته و اخگر بپزند'; 'سکار آهنج: آهنی باشد سر کج که بدان گوشت از دیگ و آن از تنور برآرند' — and the same page carries the Sūzanī Samarqandī couplet Nourai quotes. The variant list is Mo'in's: his footnote at Borhan vol.2 leaf 489 (printed p. ≈ 1026–1032, again Nourai's page) equates 'زغال = ژکال = شگال = شگار' with Awrami, Tabari, Judaeo-Persian and Gilaki forms, citing Hübschmann 247. Modern lexicography agrees that these are one word: Wiktionary lists زگال, ژگال, ذغال as alternative spellings of زغال and سکار/سگار as dialectal forms of it, and derives the whole group from Proto-Iranian *jar- < PIE *ǵʷelH- 'to burn, shine' (Mann's ġuél-, IEC 407). What is not supported is the parent: the words descend from the *ǵʷelH- root directly, not through an Avestan 'coal'-word (node 13), and not through *dʰegʷʰ-. Note also the spelling: the etymological form is زغال with zāy; ذغال with dhāl, which Nourai prints first, is the common but etymologically wrong orthography (there is no Arabic root here).\",\n \"derivation_fa\":\"هر چهار واژه اصیل اند و ارجاعات نورایی درست. در برهان قاطع (ج ۲، برگ ۶۱۵، ص چاپی حدود ۱۱۵۰) آمده: «سکار ... بمعنی زغال و انگشت باشد»، «سکارو: نان و گوشتی که بر روی زغال افروخته بپزند» و «سکار آهنج: آهنی سرکج ...»، همراه با همان بیت سوزنی سمرقندی. فهرست گونه‌ها از حاشیهٔ معین است: «زغال = ژکال = شگال = شگار» با شواهد اورامانی و طبری و گیلکی. ریشه‌شناسی امروزی هم همین را می‌گوید: «زغال» از ایرانی آغازین *jar- و هندواروپایی *ǵʷelH- «سوختن، درخشیدن» است و سکار/سگار گونهٔ گویشی همان است. آنچه پذیرفتنی نیست پدرِ این گره است: این واژه‌ها یک‌راست از همان ریشه می‌آیند، نه از راه واژه‌ای اوستایی. نکتهٔ املایی: صورت ریشه‌شناختی «زغال» با زای است؛ «ذغال» که نورایی نخست آورده رایج است ولی نادرست، زیرا این واژه عربی نیست.\",\n \"sources\":[W+\"%D8%B2%D8%BA%D8%A7%D9%84\"],\n \"ref_check\":[\n   {\"ref\":\"BQT:1150\",\"status\":\"supports\",\"note\":\"Borhan vol.2, leaf 615: 'سکار = بکسر اول بر وزن شکار، بمعنی زغال و انگشت باشد'; 'سکار آهنج ... آهنی باشد سر کج'; 'سکارو ... بر روی زغال افروخته و اخگر بپزند'; footnote 5 'از سکار (سکارو) + آهنج'; footnote 1 'سکاروا «رشیدی»، سکالو «رشیدی»'; and the Sūzanī verse 'بدار دنیا چون برفروخت آتش ظلم'. Every word and the quotation come from this one page.\"},\n   {\"ref\":\"BQT:1026\",\"status\":\"supports\",\"note\":\"Borhan vol.2, leaf 489 (printed p. ≈ 1026–1032), ژکال section, Mo'in's footnote 8: 'زغال = ژکال = شگال = شگار، اورامانی ...، طبری ...، در لهجهٔ یهودیان ایران ...، کاشانی ...، هوبشمان ۲۴۷، گیلکی ...' — exactly Nourai's set of variants.\"},\n   {\"ref\":\"HRN:163\",\"status\":\"partial\",\"note\":\"Horn no. 742 gives sekār/sikar/sukar 'Kohle' and then asks 'Hat np. zuγāl „Kohle“ (nur FS) etwas mit sekār zu schaffen?' — Nourai turns Horn's open question into an assertion by putting sekār and zoγāl in the same box.\"},\n   {\"ref\":\"MON\",\"status\":\"not_checked\",\"note\":\"cited without a page; the 2-vol. Adena reprint on disk has different pagination, so the specific Mo'in page could not be located.\"}\n ],\n \"consulted\":[\n   {\"src\":\"HUB\",\"where\":\"Persische Studien p.76\",\"stance\":\"contradicts\",\"note\":\"Hübschmann keeps zuγāl apart from sekār: 'Np. zuγāl „glühende Kohle“ belegt Nöldeke aus Shahname III, p.1508, v.214. „Kohle“ heisst ausserdem auch angišt (Nr. 126) und zuγāl ... = jüd.-tat. zuγol, zuwol' — and calls Horn's Avestan etymology 'unsicher'.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann p.407 s.v. ġuél-\",\"stance\":\"supports\",\"note\":\"'Per. zuγāl “embers”' listed with Skt. jválāmi 'burn, blaze' — the modern *ǵʷelH- analysis in Mann's notation.\"},\n   {\"src\":\"ARY\",\"where\":\"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi\",\"stance\":\"silent\",\"note\":\"no زغال/سکار entry located in the OCR of ARY_pages.txt.\"}\n ]\n})\n\nN.append({\n \"id\":15,\"lang\":\"Germanic\",\"words\":\"chol, kolo, kolam\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"The three shapes are Old High German chol / kolo (the OHG spelling ch- for k- is Upper German) and the reconstructed Proto-Germanic neuter *kolam. Pokorny IEW 399 lists them under g(e)u-lo-: 'aisl. kol n. „Holzkohle“, ags. col m. „Kohle“, engl. coal, afries. kole f., ahd. kolo m., auch kol n., mhd. kol n., kol(e) m., kole f.'; Watkins/AHD gives 'Germanic *kulam, *kolam' in so many words, which is where Nourai's 'kolam' comes from; Mann (IEC 407) lists 'OHG chol, kolo “coal” and com. Gmc. cf. ON kol' — the exact string 'chol, kolo'. The Germanic word continues *ǵ(e)u-lo- with Grimm's Law *ǵ > k, and the noun is originally neuter (ON kol, OE col n./m.).\",\n \"derivation_fa\":\"سه صورت این جعبه عبارت‌اند از آلمانی عالیٔ باستان chol / kolo (نگارش ch گویشی است) و صورت بازساختهٔ ژرمنی آغازین *kolam. پوکورنی در ص ۳۹۹ همه را زیر g(e)u-lo- می‌آورد، واتکینز عیناً *kulam و *kolam می‌نویسد و من (Mann) هم همین «OHG chol, kolo» را دارد. واکهٔ کامی دمیدهٔ *ǵ طبق قانون گریم در ژرمنی k شده است. ادعای نورایی درست است.\",\n \"sources\":[],\n \"ref_check\":[\n   {\"ref\":\"POK:399\",\"status\":\"supports\",\"note\":\"POK_02.txt lines 766–770: 'g(e)u-lo- „glühende Kohle“. Mit l-Suffix: ... aisl. kol n. „Holzkohle“, ags. col m. „Kohle“, engl. coal, afries. kole f., ahd. kolo m., auch kol n., mhd. kol n., kol(e) m., kole f., Schweiz. cholle „glimmen“.'\"},\n   {\"ref\":\"IEC:407\",\"status\":\"supports\",\"note\":\"Mann s.v. ġuél-: '(z-gde in OHG chol, kolo “coal” and com. Gmc. cf. ON kol “coal”; Oss. ævzali, Dig. ávzalu, s. id.)' — the source of Nourai's spellings 'chol, kolo'.\"}\n ],\n \"consulted\":[\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. g(e)u-lo-\",\"stance\":\"supports\",\"note\":\"'g(e)u-lo-. A glowing coal. Germanic *kulam, *kolam in: a. Old English col, a glowing coal: COAL, (COLLIE), (COLLIER)'\"},\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. coal\",\"stance\":\"supports\",\"note\":\"Klein derives coal from OE col, rel. to ON kol, OHG kolo, and compares OIr. gúal — the same set.\"},\n   {\"src\":\"SKT\",\"where\":\"Skeat s.v. coal\",\"stance\":\"supports\",\"note\":\"Skeat gives AS. col, Icel. kol, OHG kol — same group.\"}\n ]\n})\n\nN.append({\n \"id\":16,\"lang\":\"English\",\"words\":\"coal\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Old English col (neuter/masc.) 'glowing ember, charcoal' > Middle English col > coal; the modern sense 'mineral coal, pit-coal' displaced 'ember' only from the 13th century, when sea-coal began to be mined — the older sense survives in 'coals of fire' and 'charcoal'. The chain from Proto-Germanic *kolam is regular (OE o from Gmc. o, final -am lost). Watkins gives it directly: 'g(e)u-lo-. A glowing coal. Germanic *kulam, *kolam in: a. Old English col, a glowing coal: COAL', with the same page reference to Pokorny 399 that node 15 uses.\",\n \"derivation_fa\":\"انگلیسی کهن col «اخگر، زغال چوب» > انگلیسی میانه col > coal؛ معنای امروزی (زغال‌سنگ) از سدهٔ سیزدهم و پس از رواج «sea-coal» غالب شد و معنای کهن در ترکیب charcoal مانده است. زنجیره از *kolam ژرمنی قاعده‌مند است و واتکینز عیناً همین را می‌دهد. ادعای نورایی درست است.\",\n \"sources\":[],\n \"ref_check\":[\n   {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 (AHD_watkins1985.txt line 500): 'g(e)u-lo-. A glowing coal. Germanic *kulam, *kolam in: a. Old English col, a glowing coal: COAL, (COLLIE), (COLLIER); b. probably dialectal Old French cholle, round lump, head: CHOLLA. [Pok. g(e)u-lo- 399.]'; the word index confirms 'COAL g(e)u-lo-'.\"}\n ],\n \"consulted\":[\n   {\"src\":\"POK\",\"where\":\"IEW 399\",\"stance\":\"supports\",\"note\":\"'ags. col m. „Kohle“, engl. coal'\"},\n   {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. coal\",\"stance\":\"supports\",\"note\":\"OE col > ME col > coal, with the Germanic and Celtic cognates.\"}\n ]\n})\n\n# strip helper key\nfor n in N:\n    n.pop(\"derivation_note\", None)\n\nout = {\n \"pdf_page\": 134,\n \"book_page\": 104,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [root]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-134.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build134.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-134.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 134"
}
```


### [2026-09-05T20:36:00.313Z] TOOL RESULT

```
written
JSON OK
nodes verified: 16/16
node verdicts: {'disputed': 5, 'plausible': 5, 'transcription_suspect': 1, 'confirmed': 5}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 8, 'supports': 14, 'contradicts': 2, 'not_checked': 4, 'not_found': 2}
books consulted: {'partial': 11, 'supports': 22, 'contradicts': 9, 'silent': 8} | by book: {'BRT': 6, 'PHD': 5, 'KLN': 5, 'HUB': 4, 'CHEUNG': 4, 'POK': 4, 'AHD': 4, 'HRN': 3, 'WLD': 3, 'IEC': 3, 'SOD': 2, 'SKT': 2, 'MON': 1, 'KNT': 1, 'NYB': 1, 'SYN': 1, 'ARY': 1}
```


## [2026-09-05T20:36:25.824Z] AGENT

Verification of PDF page 134 (book page 104) is complete. `verify_check.py 134` reports 16/16 nodes and 0 PROBLEM lines.

**Page 134 — single entry, root "Dhogh, Dhegh" (PIE *dʰegʷʰ- 'to burn'), 16 nodes**

Verdicts: root `confirmed`; nodes — 5 confirmed, 5 plausible, 5 disputed, 1 transcription_suspect.

Disputed / suspect items:
- **#5 Sogdian `dğm`y : "grove"` — transcription_suspect (error in the BOOK).** Gharib (SOD) p.139 entry 3532 reads δγmʾy *δaxmē* "tomb, **grave**" ← Av. *daxma*-. Nourai printed "grove"; the JSON extraction is faithful to p.104. Page image saved to `data/verification/sources/refs/ocr/BOOK/134.png`.
- **#1, #2 Av. *daxma-* / NP دخمه — disputed.** Bartholomae's "Verbrennungsstätte, zu dag-" is superseded; modern view (Wiktionary, Iranica) takes *daxma-* to PIE *dʰm̥bʰ- 'to dig, bury' (Arm. *damban*, Gk. *táphos*). Nourai's gloss "place for burning the dead" is also wrong on Zoroastrian practice. (داغ and *daxša-* in the same nodes are confirmed.)
- **#6, #7 Av. "vi-dâz" → NP گدازیدن — disputed.** No Avestan *vī-daž-* exists. Nourai's own reference, **Nyberg II 217**, derives MP *vitāxtan* from "vi + Av. *tak-*"; Cheung puts NP *gudāxtan/gudāz-* under *taH 'to melt' (PIE *teh₂k-, Pok. 1053). The chart's own NOTE half-anticipates this.
- **#13 Av. *skarana, skairya* "coal" — disputed.** Horn §742 p.163 says exactly this, but Bartholomae glosses *skarana-* 'rund' (round), and Hübschmann p.76 ad Horn 742: "Unsicher", Darmesteter renders *garəmō-skarana-* 'une paire de pinces', *skairya-* 'campement'.

Notable plausible-not-confirmed: #10 Gmc *dagaz* 'day' (Klein 404 supports, but Pokorny 240 explicitly sends it to *ā̆gher- p.7 and Watkins to *agh-²; labiovelar loss irregular); #12 the "coal" root box merges three distinct reconstructions (Pok. *g(e)u-lo-*, Mann *ġuél-*, Mann *guheguh-*) — only Mann's *guheguh-* (IEC 379, "assimilated form of dheguho") licenses hanging it under *dʰegʷʰ-; #4 فلاخن is a loan (via Sogdian per Gershevitch, Bactrian per Wiktionary), not direct Avestan descent.

Reference accuracy: Nourai's citations check out unusually well — POK:240, HRN:163, AHM:181/192, SOD:139, IEC:379 and 407, KLN:404, BQT:1026/1150 all say what he uses them for; only NYB:217 actively contradicts him. AHD could not be confirmed for *febris* (Watkins 1985 has no *dʰegʷʰ- root and no FEVER in its index).

**No extraction errors** — the JSON matches the printed page exactly, including "grove", "dağa, dâğah", and the Persian script strings.
