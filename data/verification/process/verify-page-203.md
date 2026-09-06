# Verification process log — verify-page-203


## [2026-09-06T02:17:41.709Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 203 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-203.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-203.json. Write /home/sfmqrb/git/rishe/data/verification/page-203.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 203` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:17:43.000Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:17:43.811Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:17:43.828Z] TOOL RESULT

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


## [2026-09-06T02:17:44.238Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-203.txt"
}
```


### [2026-09-06T02:17:44.279Z] TOOL RESULT

```
1	=== PDF page 203 (book page 173) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwa, Gwâ, Gwen 2 : to walk, to step, to come, to go  (refs POK:463)  PART 2
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:464,465 | aiwi-gaiti : to come here ☞Ambhi ; ni-jâma : birth, origin, race ; gemton : to give birth to ; gimsenin : birth ; gemmons : born
5	  #2 (parent #1) [None] refs=None | 
6	#3 (parent #0) [Greek] refs=AHD;KLN | bainein : to go, walk, step ; dia-bainein : going across (referring to excessive thirst and urination due to diabetes) ☞Dwo ; akro-bates : stepping on tiptoe ☞Ak
7	  #4 (parent #3) [French] refs=None | 
8	    #5 (parent #4) [Persian] refs=MON:75,1588 |  «دیابت ، آکروبات»
9	  #6 (parent #3) [English] refs=AHD | diabetes, acrobat
10	#7 (parent #0) [French] refs=AHD:110 | basse, bassin : base, bottom
11	  #8 (parent #7) [Persian] refs=VOP:83 | bâsan «باسن» : buttock, hip
12	  #9 (parent #7) [English] refs=AHD:110 | base, basic
13	#10 (parent #0) [Latin] refs=AHD | venîr : to come
14	  #11 (parent #10) [English] refs=None | avenue, event, prevent, invent
15	#12 (parent #0) [Germanic] refs=AHD | kuman : to come
16	  #13 (parent #12) [English] refs=None | come, become, welcome, income
17	#14 (parent #0) [Indo-European] refs=IEC:425 | Ğhumbo : start, move, jump
18	  #15 (parent #14) [Pahlavi] refs=MON:1244 | junbîtan : to move
19	    #16 (parent #15) [Persian] refs=MON:1244; IEC:425 | jonbîdan «جنبیدن» : to move | extra: جنبش ، جنبنده ، جنبان
20	--- entry 1 ---
21	ROOT Gwâ -> redirect to Gwa
22	--- entry 2 ---
23	ROOT [Indo-European] Gwadh : to sink  (refs POK:465)
24	#1 (parent #0) [Avestan] refs=POK:465 | vi-gâthô : ravine, canyon ☞Wi
25	  #2 (parent #1) [None] refs=None | 
26	#3 (parent #0) [Sanskrit] refs=POK:465 | gâhate : immersed ; vi-gâha : depth
27	#4 (parent #0) [Greek] refs=AHD:1519 | bussos 2 : bottom of the sea
28	  #5 (parent #4) [Latin] refs=AHD | abyssus
29	    #6 (parent #5) [English] refs=AHD | abyss : a bottomless void or pit, hell
30	
```


## [2026-09-06T02:17:47.519Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-203.json",
 "description": "Read source JSON for page 203"
}
```


### [2026-09-06T02:17:47.568Z] TOOL RESULT

```
{
  "pdf_page": 203,
  "book_page": 173,
  "entries": [
    {
      "root": {
        "name": "Gwa, Gwâ, Gwen 2",
        "lang": "Indo-European",
        "refs": "POK:463",
        "gloss": "to walk, to step, to come, to go"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:464,465",
          "words": [
            {"translit": "aiwi-gaiti", "gloss": "to come here", "script": null, "see": ["Ambhi"]},
            {"translit": "ni-jâma", "gloss": "birth, origin, race", "script": null},
            {"translit": "gemton", "gloss": "to give birth to", "script": null},
            {"translit": "gimsenin", "gloss": "birth", "script": null},
            {"translit": "gemmons", "gloss": "born", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD;KLN",
          "words": [
            {"translit": "bainein", "gloss": "to go, walk, step", "script": null},
            {"translit": "dia-bainein", "gloss": "going across (referring to excessive thirst and urination due to diabetes)", "script": null, "see": ["Dwo"]},
            {"translit": "akro-bates", "gloss": "stepping on tiptoe", "script": null, "see": ["Ak"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:75,1588",
          "words": [
            {"translit": null, "gloss": null, "script": "دیابت ، آکروبات"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "diabetes, acrobat", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "French",
          "refs": "AHD:110",
          "words": [
            {"translit": "basse, bassin", "gloss": "base, bottom", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "VOP:83",
          "words": [
            {"translit": "bâsan", "gloss": "buttock, hip", "script": "باسن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:110",
          "words": [
            {"translit": "base, basic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "venîr", "gloss": "to come", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "avenue, event, prevent, invent", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "kuman", "gloss": "to come", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "come, become, welcome, income", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "IEC:425",
          "words": [
            {"translit": "Ğhumbo", "gloss": "start, move, jump", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Pahlavi",
          "refs": "MON:1244",
          "words": [
            {"translit": "junbîtan", "gloss": "to move", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:1244; IEC:425",
          "words": [
            {"translit": "jonbîdan", "gloss": "to move", "script": "جنبیدن"}
          ],
          "script_extra": "جنبش ، جنبنده ، جنبان",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gwâ",
        "redirect": "Gwa"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gwadh",
        "lang": "Indo-European",
        "refs": "POK:465",
        "gloss": "to sink"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:465",
          "words": [
            {"translit": "vi-gâthô", "gloss": "ravine, canyon", "script": null, "see": ["Wi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:465",
          "words": [
            {"translit": "gâhate", "gloss": "immersed", "script": null},
            {"translit": "vi-gâha", "gloss": "depth", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1519",
          "words": [
            {"translit": "bussos 2", "gloss": "bottom of the sea", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "abyssus", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "abyss", "gloss": "a bottomless void or pit, hell", "script": null}
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


## [2026-09-06T02:17:49.519Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','IEC','MON','VOP','WLD','SYN','BRT','KNT','PHD','NYB','HRN','HUB','CHEUNG','BQT','ARY','SKT','FSD','WEB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T02:17:51.206Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


## [2026-09-06T02:18:20.659Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo ---- && sed -n '1,80p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T02:18:20.711Z] TOOL RESULT

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
```


## [2026-09-06T02:18:21.737Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-124.json'));print(json.dumps(d['entries'][0],ensure_ascii=False)[:3000])\""
}
```


### [2026-09-06T02:18:23.777Z] TOOL RESULT

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
---
{"entry": 0, "root": "Dhě 2", "verdict": "confirmed", "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)", "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.", "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.", "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"], "ref_check": [{"ref": "AHD:1512", "status": "supports", "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the
```


## [2026-09-06T02:18:27.032Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T02:18:27.081Z] TOOL RESULT

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


## [2026-09-06T02:18:29.616Z] TOOL CALL #8: Bash

```json
{
 "command": "ls site/pages/203.jpg 2>/dev/null; pdftoppm -f 203 -l 203 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg203 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T02:18:32.394Z] TOOL RESULT

```
site/pages/203.jpg
total 26200
drwx------ 2 sfmqrb sfmqrb   12288 Sep  5 22:18 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58105 Sep  5 17:02 build171.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51583 Sep  5 17:08 build173.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59926 Sep  5 17:11 build174.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64448 Sep  5 17:12 build175.py
-rw-rw-r-- 1 sfmqrb sfmqrb   69033 Sep  5 17:13 build177.py
-rw-rw-r-- 1 sfmqrb sfmqrb   75374 Sep  5 17:12 build180.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43965 Sep  5 17:11 build181.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64481 Sep  5 17:11 build182.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47920 Sep  5 17:11 build183.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62604 Sep  5 17:16 build184.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63773 Sep  5 17:17 build186.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62923 Sep  5 22:13 build189.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5391 Sep  5 17:02 g2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2929 Sep  5 17:02 g3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5607 Sep  5 17:02 g4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14924 Sep  5 17:01 geus_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10247 Sep  5 17:01 ghaido_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4197 Sep  5 17:01 ghaido_low.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3536 Sep  5 17:04 jang.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     310 Sep  5 22:16 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb   84301 Sep  5 17:17 mk176.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68808 Sep  5 17:15 mk178.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3293 Sep  5 17:01 n17b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17771 Sep  5 17:01 n17c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7472 Sep  5 17:01 n19.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3278 Sep  5 17:01 n5b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2334 Sep  5 17:01 n5c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  5 17:01 n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161412 Sep  5 17:01 p174hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  173427 Sep  5 17:01 p176hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2762 Sep  5 17:02 p189_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24596 Sep  5 17:02 p189_greek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20222 Sep  5 17:02 p189_khoris.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33994 Sep  5 17:02 p189_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1688 Sep  5 22:17 p190_eb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1093 Sep  5 22:17 p190_emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb  102711 Sep  5 22:17 p190hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5540 Sep  5 22:17 p190_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88207 Sep  5 17:02 pg177.png
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53414 Sep  5 17:03 pg183.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79537 Sep  5 17:09 pg185.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72425 Sep  5 17:08 pg186.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53749 Sep  5 17:02 pg187.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77516 Sep  5 17:01 pg189.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65970 Sep  5 22:17 pg190.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71828 Sep  5 22:17 pg192.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75609 Sep  5 22:18 pg203.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
-rw-rw-r-- 1 sfmqrb sfmqrb     738 Sep  5 17:04 xang.txt
```


## [2026-09-06T02:18:35.652Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg203.png"
}
```


### [2026-09-06T02:18:36.248Z] TOOL RESULT

```

```


## [2026-09-06T02:18:36.245Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:18:56.552Z] TOOL CALL #10: Bash

```json
{
 "command": "grep -rl \"gemton\\|gimsenin\\|gemmons\" data/extracted/batch/ ; echo ---; grep -rn \"\\\"Gwa\" data/extracted/batch/*.json | head -20"
}
```


### [2026-09-06T02:18:56.634Z] TOOL RESULT

```
data/extracted/batch/page-203.json
---
data/extracted/batch/page-203.json:7:        "name": "Gwa, Gwâ, Gwen 2",
data/extracted/batch/page-203.json:213:        "redirect": "Gwa"
data/extracted/batch/page-203.json:219:        "name": "Gwadh",
data/extracted/batch/page-204.json:7:        "name": "Gwag",
data/extracted/batch/page-145.json:324:                "Gwa"
data/extracted/batch/page-202.json:7:        "name": "Gwa, Gwâ, Gwen 2",
data/extracted/batch/page-196.json:170:        "redirect": "Gwa"
data/extracted/batch/page-208.json:112:        "redirect": "Gwa"
data/extracted/batch/page-396.json:79:            {"translit": "paiti-gama", "gloss": "bring forward (a message)", "script": null, "see": ["Gwa"]},
data/extracted/batch/page-393.json:176:            {"translit": "fra-jâma", "gloss": "end of going (destination)", "script": null, "see": ["Gwa"]},
data/extracted/batch/page-365.json:68:            {"translit": "ni-gâma", "gloss": "(place for) inserting down", "script": null, "see": ["Gwa"]},
data/extracted/batch/page-442.json:20:            {"translit": "han-jâmana", "gloss": "come together", "script": null, "see": ["Gwa"]},
data/extracted/batch/page-442.json:21:            {"translit": "han-jâma", "gloss": "come to end", "script": null, "see": ["Gwa"]},
data/extracted/batch/page-442.json:22:            {"translit": "han-gmatana", "gloss": "place to get together", "script": null, "see": ["Gwa"]},
data/extracted/batch/page-442.json:51:            {"translit": "han-gama", "gloss": "at the same time, during", "script": null, "see": ["Gwa"]}
data/extracted/batch/page-42.json:223:                "Gwa"
data/extracted/batch/page-88.json:231:                "Gwa"
data/extracted/batch/page-59.json:84:            {"translit": "â-gam", "gloss": "to come", "script": null, "see": ["Gwa"]},
```


## [2026-09-06T02:18:58.891Z] TOOL CALL #11: Bash

```json
{
 "command": "grep -n \"ni-j\\|nijama\\|ni-jâma\" data/extracted/batch/page-20[0-5].json | head -20; echo ---; python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-202.json'))\nfor e in d['entries']:\n    print('ROOT',e['root'])\n    for n in e['nodes'][:30]:\n        print(' ',n['id'],n['parent'],n['lang'],n['refs'],[ (w.get('translit'),w.get('gloss'),w.get('script')) for w in n['words']])\n\""
}
```


### [2026-09-06T02:19:00.631Z] TOOL RESULT

```
data/extracted/batch/page-203.json:21:            {"translit": "ni-jâma", "gloss": "birth, origin, race", "script": null},
---
ROOT {'name': 'Gwa, Gwâ, Gwen 2', 'lang': 'Indo-European', 'refs': 'POK:463', 'gloss': 'to walk, to step, to come, to go'}
  1 0 Avestan / Old Persian POK:463; KLN:318 [('gam', 'to come, step', None), ('jam, jantu', 'to go', None)]
  2 0 Avestan POK:463 [('gâman', 'step', None), ('a-gam', 'to come', None), ('ni-gama', 'come down (in sheath)', None), ('paiti-gama', 'come forth (with a message)', None)]
  3 2 Persian HRN:11; BQT:434,1765,2223; SPG:217 [('gâm', 'step', 'گام'), ('âmadan', 'to come', 'آمدن ( آینده )'), ('nîyâm', 'sheath', 'نیام'), ('payâm', 'message', 'پیام ( پیامبر ، پیغام ، پیغمبر )')]
  4 0 Avestan BQT:166,1451 [('fra-jâma', 'gone forward (to a destination)', None), ('han-jâma', 'conclusion', None), ('han-jâmana', 'coming together', None)]
  5 4 Persian ETM; FFD [('farjâm', 'end', 'فرجام ( فرجامیدن )'), ('anjâm', 'conclusion', 'انجام ( انجامیدن )'), ('anjoman', 'society, meeting', 'انجمن')]
  6 0 Avestan / Old Persian POK:463; KNT:183 [('gât, gâthu, gâv, gâtuš', 'place, seat, throne', None), ('gâtu-bar', '(baby) carriage', None)]
  7 6 Persian BQT:1771,1773 [('gâh 2', 'place, position, rank', 'گاه ۲')]
  8 6 Arabic FVF:144 [('jâh', 'rank', None)]
  9 8 Persian MON [('jâh', 'position', 'جاه')]
  10 0 Old Persian BQT:2368; KNT:212 [('ham-gmatana, hangmatâna', '(a place for) coming together', None)]
  11 10 Persian BQT:2368 [('Ekbâtân', None, 'اکباتان (همدان)')]
  12 0 Avestan / Old Persian PLA:146; NYB:228; SBK:203 [('jamâna', 'a step (period) of time', None), ('thamân', 'time', None)]
  13 12 Persian MON:1746 [('zamân', 'time', 'زمان')]
  14 12 Arabic PLA:146; NYB:228 [('zamân', 'time', None)]
  15 14 Persian MON:1746 [('mozmen', 'old', 'مزمن'), ('azmaneh', 'times', 'ازمنه')]
  16 0 Avestan / Old Persian BQT:2383 [('gâma', 'a step (period) of time', None), ('han-gâma', 'at the same time, during', None)]
  17 16 Persian BQT:2383 [('hengâm', 'during', 'هنگام')]
```


## [2026-09-06T02:19:24.132Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gimdyti\\|gimti\\|gimimas\" POK_full.txt | head -20; echo \"=== gwem lemma ===\"; grep -n \"g\\ʷem-\\|gṷem-\\|gwem-\" POK_full.txt | head -20"
}
```


### [2026-09-06T02:19:24.199Z] TOOL RESULT

```
38516:Lithuanian gemu, gimti^ be born ' = Latvian dzemu, dzimtds., Lithuanian g/mstu{ior 
=== gwem lemma ===
ugrep: error: error at position 6
(?m)g\ʷem-\|gṷem-\|gwem-
      \___invalid escape
```


## [2026-09-06T02:19:25.420Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"463\\|464\\|465\" POK_full.txt | grep -i \"page\" | head; echo ---; grep -n \"gʷā-\\|gʷem\\|gʷā, gʷem\" POK_full.txt | head -20; echo === ; head -30 POK_full.txt"
}
```


### [2026-09-06T02:19:25.485Z] TOOL RESULT

```
Exit code 1
38377:Page(s): 465 
38525:Page(s): 463-465 
39785:Page(s): 465-466 
---
(eval):1: == not found
```


## [2026-09-06T02:19:29.069Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38440,38530p' POK_full.txt"
}
```


### [2026-09-06T02:19:29.131Z] TOOL RESULT

```
lllyrian g"'- > b-. 

2. g^em- 

Unthematic *(e)-g"em-t {> *e-g"en-t), -g"m-te, -g"m-ent\r\ Old Indie Aor. agan, gan{gior 
/after forms with original *g"'m-, *g"m-; 1. Sg. agamam), agata{*g"'rn-), agman, agmata, 
Gatha-Avestan 3. Sg. Inj. uz-J§n, 3. PI. g^marr, 

Armenian 3. Sg. ekn'he comes ' (= Old Indie agan); about still unclear 1 . Sg. eki, 3. PI. 
ekinsee Meillet Esquisse 134 f.; 

gr. parnv 3. Du., un£ppaaav 3. PI. probably to root form *g"a-\ Note: common lllyrian g"- 
>b-. 



Konj. *g"'emet/"\n Old \nd'\c gam-at, -anti, Ga\ha-/Kves\.av\ Jama'ti, jima'tr, Opt. g"'m-/et\n 
Old Indie gamyat, Avestan jamyat, ap. jamja^ (/for ^ from forms with lengthened grade 
Indo Germanic *g"em-)\ Old English cyme see below; 

thematic: zero grade Old Indie gamati, As/estan Jama/f/" goes' (Old Indie gamayati 
"allows to eome, brings about, causes, makes happen ', Avestan jamaye/t/^ brings to the 
side, flank '), zero grade Old Indie (Opt. Aor.) garnet, gamema, gamemahi, probably also 
Aor. agamat, Perl. Ja-gama'\ walked ' (compare Gothic 1. PI. qemum); Avestan fra-ymal 
(Gatha-Avestan-^^/775]) 'he comes over, joins; ensues, follows as a consequence of, 
happens as a result of ', Old pers. a-gmata, 

Oscan kumbened^ it agrees, came together ', cebnust {irom *ce-benusf) " (nucn^eneni 
', Umbrian benust, benurent' venerit, -int '; Latin Konj. advenam {a\iO\A nior msee below; 
perhaps with analogical -en- after the forms as Latin ven/o, ventum, ven/j; 

Gothic (7//77a/7 (preterit qam, 1. PI. qemum: 0\6 Indie 1. Sg. Peri. Ja-gama), Old High 
German queman an6 (zero grade?) coman= Old English cuman. Old Norse koma^ coxwe'; 
Old English Konj. Prater, (older Optat.) cyme {*g"em-T-tj\ 

Tocharian A kam-, kum-, B kam-, kam-, sem 'come'. 

70-present *g"m-i6\v\ gr. paivw "go' (Put. prjaofjai etc.), Latin Ke/7/o'come' with very old 
alteration from -/t?/- to -/?/■; after Schwyzer Gr. Gr. I 309 could na\so be related to forms as 
Avestan Jantu {*g"'em-tu-), Armenian ekn {*e-g"em-t}\ to Ke/7//77^sstimmt Gothic qemum, 

5^c^present *g"'m-sk6: 0\6 \n6\c gacchati, Avestan jasaiti^ he goes', gr. paoKS "go! 
come!' Tocharian A kumnas^he comes ', Med. kumnastar, B kanmastra. 

Verbaladjektiv: Old Indie gata-h^ gone, departed, left; dead; lost ', Avestan gata-ds., gr. 
pQToq " feasible, able to be carried out ' ( *g"'m-to-s), Latin in-ventus. 

other nominal formation: 

Old \n(i\c gati-hi. " gait ', Avestan aiwi-gati-^ coming along = entry, beginning ', gr. paai(; 
f. " footstep; base' {*g"m-ti-s), Latin con-venti-6^ gathering, assembly, meeting, convention 
', Gothic ^5C7^/77A's " gathering, assembly, meeting, convention ' {*-g"m-tis). Old Norse 
samkundi. ds.. Old High German cumft. Modern High German Ankunft^ arrival, 
appearance, approach, incoming '; Old \n(ii\c gantu-hxx\. " gait, way', Latin adventus, -us' 
arrival, appearance, approach, incoming '; Gothic qums' arrival, appearance, approach, 
incoming ' {*g"'em-/s). Old English cyme. Old High German cumr. Old Indie gamya-' where 



one can go or should go ', Oscan kumbenniefsQe'c\. " meeting, rendezvous, coming, 
together, circuit, congress, assembly, union, session '; Old High German biquami^ 
bequem ' (compare ' digestible '), Old English ^ecu/e/ne "pleasant, fitting'. Old Norse 
kvsemr^ capable or allowed to come '; kvamat ' coming, visit, dropping by; inspection ', 
koma ds.; 

Tocharian A kum-, AB kam-, A kam-, B se/77-"come', A kumnas, Med. kumnastar^ 
comes ', A kakmu, B kekamu^ arrived; resulted '. 

With a meaning- development ' come (to the world) ' = ' be born ': 

Avestan n'hjamayeinti^ be born ' {*ni-Jama- 'birth'); 

gr. £-pa0r| syEvvEGri Hes.; 

alb. pre-gjim " feast in the first birth '; (common pronunciation alb. gj- = Slavic dz-) 

Lithuanian gemu, gimti^ be born ' = Latvian dzemu, dzimtds., Lithuanian g/mstu{ior 
pronunciation see Schuize KZ. 45, 230) = Latvian dzimstu 6s., Lithuanian gimine^ family ', 
^j7/77/5 "birth', gamas^ the innate ', causative gaminti^ generate children, breed cattle ', 
Latvian dzimts^ congenital, existing from birth, innate, inherited ', o'z//775a "birth' = Old 
Prussian gimsenin kVk. Sg. "birth'. Old Prussian gemton^ to give birth to children ', 
^e/77/77c»/7s participle Perf. " born '. 

References: WP. I 675 ff., Meillet Esquisse2 134 f., Schwyzer Gr. Gr. I 309, 689, 7423, 
7072, Trautmann 76, Pedersen Tocharian 170 ff., 221, 234. 
Page(s): 463-465 

Root / lemma: g'^eA^- 
Meaning: to push, hit, harm 

Material: Old Indie gandh-^bump, poke, prick, injure, destroy' (by grammarians), gandha-h
```


## [2026-09-06T02:20:31.592Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38400,38445p' POK_full.txt; echo \"=========== GWADH ===========\"; sed -n '38340,38400p' POK_full.txt"
}
```


### [2026-09-06T02:20:31.657Z] TOOL RESULT

```
"place, couch, long upholstered seat, folding bed; small spare bed; camp bed, seat, 
throne'. Old pers. ga&u6s.\ Old Indie vf-gaman-v\. " footstep ' {prthu-pra-gaman-^ walking 
further '; compare gamin- "going', further formations an ostem gama-h), Avestan ga-man- 
n. " footstep ', Old Indie gaya-m " footstep ' in uru-gaya- " walking further, walking far ' (of 
way), Avestan ^5ya-(Akk. gaim) " footstep ' (with formants -ya-)\ 

Armenian kam " stand ' ( : gr. spnv); 

gr. *pipr|ai, pipat;, sppv see above; pnTappoc; " dance ', pr|TapiJU)v " dancer ' (from 
*pc(TO(; or *paTa " das Fuftaufsetzen ' + appa " structure, composition '); aiJcpiapnTSw, 
Ionian afjcpiapaTEw " dispute, argue, fight ' (" nach zwei Seiten auseinandergehend '), pnija 



n. " footstep ' changing through ablaut pajpot; m. " step, tread; kick, strike or blow delivered 
by the foot; footprint, track, grade, rack, altar'; infinitive pnjJEvai; Pn^oc; m. " doorsill '; 
p£pr|^0(;, Doric p£paAo(;, kyren. papaAo(; ' enterable, unhallowed, not consecrated, not 
sanctified ' (contrast from apaTO(; " immortal, holy'); zero grade p£paiO(; "certainly' (*good 
feasible); pa5r|v Adv. 'in footstep '; pa5oq m. 'way', paGpoq m. 'grade, threshold, footstep 
', paGpov ' foundation ', £ppaTr|<; ' man's shoe '; Note: common lllyrian g"- > b-. 

alb. nga^\ run, drive' {*ga-nid)\ Actually {*ga-snid) nasalized form prevented common 
alb. g- > d-. 

Maybe alb. ngathte's\o\N, lazy (walk)' [common alb. - Old Irish -s > -th] 

Maybe zero grade in alb. gare 'race' < Rumanian goana 'race, battue'. 

Lithuanian dial, got/ "go'; Latvian ^^^^ (preterit to /et) 'I walked ' (places a present *ga/d 
ahead, whosey would be present formant), therefrom iurther gajums ' gait, row'; ga/ta' 
gait ' (with analogical a/, Endzelin Latvian Gr. S. 678); gat/s PI. ' Fluglocher der Bienen '; 
Lithuanian proga' occasion, opportunity, term, deadline (*end of the road)' (prefix *prd + 
ga)\ Lithuanian gatve' road, livestock pasture ', Latvian ^a/i/a'way, passage ' are 
Germanic loanword 

Perhaps here also Celtic words for 'die' (as ' leave, depart ', £k pporajv pnvai), as Old 
Irish baTd'6ea6' { *ba-a- t/irorr\ *g"'a-), at-batb'6\e6' {*-g"'d-t. .), batb'6eat\r\' = cymr. bad 
'pest, pestilence', bret. bad' anesthetization ', corn, badus' phrenetical '; Old Irish bas 
'death' is shaped aiter gnas' consuetude ' etc.. Contrariness of Thurneysen Gr. pp. 547, 
728 is a stem bas- not proved; s. more properly Pedersen Litteris 2. 89 f. Note: common 
lllyrian g"'- > b-. 

2. g^em- 

Unthematic *(e)-g"em-t {> *e-g"en-t), -g"m-te, -g"m-ent\r\ Old Indie Aor. agan, gan{gior 
/after forms with original *g"'m-, *g"m-; 1. Sg. agamam), agata{*g"'rn-), agman, agmata, 
=========== GWADH ===========
Page(s): 367-368 

Root /lemma: 5'"aih- 

Meaning: to sink, submerge 

Material: Old Indie ^^/7a/e "dives, permeates, soaks', participle gac/ha-h^ deep, dense, tight 

', gaha-h'dep\h, the interior '; with a. gahana-, gahvara-' deep, dense', n. "depth, abyss, 

thicket ', dur-gaha-m " wicked place or way'; 

the participle gadha-\s probably analogical form after roots with Old Indie h= Indo 
Germanic gh; gadha- " shallow, having little depth ', m. n. " shallow, ford' is perhaps from 
an Old Indie root noun ga{\.o Indo Germanic g"a-^ gait ') + dha as " granting passage ' to 
define; 

Avestan Akk. PI. vi-ga&o^ canyon, gorge, gulch, ravine, abyss, steep narrow valley 
carved by running water ' (: Old Indie vi-gaha-) " dipping oneself ', zero grade guda- 
"depth'; 



gr. pnaaa, Doric paaaa (*pc(0ja) f. " wooded combe, glen, mostly in the mountain glens, 
gorge, ravine, gulch '; paaaoc; n. ds. (*pa9ao(;), zero grade puGoc;, puaaoc; ' the depth, 
esp. of the sea ' with p instead of y after pnaaa; a^vaooq " with no bottom, bottomless, 
unfathomed ', pa9o(; n. "depth"; p£v0O(; 'depth' secondary after nsvGoq : na9o(;; Note: 
common lllyrian g"'- > b-. 

Old Irish ba{i)dim^ go under, dive, submerge; sink, drown', cymr. boddi^ drown, flood ', 
corn, bedhy. Middle Breton beuziff^ drown '; cymr. diffoddi^ extinguish, annihilate, erase ' 
from *di-spad- ( *dT-eks-bad-). 

Note: 

From Root / lemma: g^aA"^-: to sink, submerge, derived Root/ lemma: b'^au-l . b^J-: to hit. 
References: WP. I 665, Schwyzer Rhein. Mus. 81, 193 ff. 
Page(s): 465 

Root / lemma: g'^a- g^em- 

Meaning: to go, come 

Note: 

Root / lemma: g^'a-, g^em- : "to go, come' from zero grade of Root / lemma: ag- {*heg-): "to 

lead, *drive cattle'. 

Material: Old lndicy/-^5-//"goes' (= gr. *pipr|ai, compare lak. 3. Sg. pipavri, hom. participle 

pipa(; " walking along with big steps ', in addition also hom. pipaaGwv), Aor. a-ga-m " I got 

to, arrived at, reached, got there , left ' (Avestan Injunkt. gal^ he will get to, arrive at ') = 

Armenian kam " stand ', gr. £pr|v, Doric £pav " I undid; (a jacket, package, door, etc.) 

opened, went '; Note: common lllyrian g"- > b-. 

Old Indie ^a/Aa/T? "limb, member, body'; gatu-h^ gait, way, room, place', Avestan gatu-s 
"place, couch, long upholstered seat, folding bed; small spare bed; camp bed, seat,
```


## [2026-09-06T02:20:32.044Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- watkins gwa/gwem ---\"; grep -n -i \"gwā-\\|gwem-\\|gwadh\\|gwa-\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T02:20:32.123Z] TOOL RESULT

```
--- watkins gwa/gwem ---
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
685:lenk-. To bend. Germanic */engwa- in Old Norse lyng, heather: LinG?. [Pok. lenk- 676.]
839:parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
1280:BE- ambhi BEACON bha-1 BEAD gWhedh- BEADLE bheudh- BEAM bheue- BEAN bha-bha- BEAR! bher-1 BEAR? bher-3 BEARD bhardha BEAT bhau- BEATIFIC deu-2, dhé-1 BEATIFY deu-2 BEATITUDE deu-2 BEAU deu-2 BEAUTY deu-2 BEAVER! bher-3 BECHE-DE-MER mori- BECK? bheg¥- BECKON bha-! BECOME gWa- BED bhedh-
1285:BELLONA duellum BELLOW bhel-4 BELLOWS bhelgh- BELLY bhelgh- BELONEPHOBIA gvel-! BELUGA bhel-1 BELVEDERE deu-2, weid- BEMA gWa-
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1385:coMAl keme- COMB gembh- COMBAT battuere COMBINE dwo- COMBUSTION eus- COME gWa- COMEDO ed- COMEDY wed-2 COMESTIBLE ed- COMFIT dhé-1 COMFORT bhergh-2 COMITIA  ei-1 COMITY smei- COMMA skep- COMMAND man-2 COMMANDO man-2 COMMEMORATE (s)mer-1 COMMENCE ei-1 COMMEND man-? COMMENSURATE mé-2 COMMENT men-! COMMERCE merk-2 COMMINUTE mei-2 COMMISERATE miser COMMIT (s)meit(a)- COMMIX meik- COMMODE med- COMMODIOUS med-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1397:COUPLE ap-! COURAGE kerd-1 COURANTE kers-2 COURIER kers-2 COURSE kers-2 COURT gher-1 COURTEOUS gher-1 COURTESAN gher-1 COURTESY gher-' COURTIER gher-1 COUSIN swesor- COUTH gnd- COUTURE syi- COUVADE keu-2 COVE! ku- COVEN gWa- COVENANT gWa- COVER wer-5 COVET kwép- COVEY keu-2 cow! gWou- cow2 ku- COWER ku- COWSLIP gWou-, sleubh- coxa koksa
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1466:EOSIN aus-! EPACT ag- EPEIROGENY 4pero- EPENTHESIS dhé-1 EPHEBE yégWa- EPHEDRINE sed-1 EPHEMERAL Amer- EPHOR wer-4
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1583:HEAVY kap- HEBDOMAD septm HEBE yégWa- HEBEPHRENIA yégWa- HECATOMB dekm, g¥ou- HECKLE keg-
1682:INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
1683:INTRA- en INTRADOS dorsum, en INTRANSIGENT ag- INTREPID  trep-1 INTRINSIC en, sekw-1 INTRO- en INTRODUCE deuk-, en INTROIT el-1, en INTROMIT en, (s)meit(a)- INTRORSE en, wer-3 INTROSPECT en, spek- INTROVERT wer-3 INTRUDE treud- INTUITION teu- INTUMESCE teue- INTUSSUSCEPTION en, kap- INULIN wel-3 INUNCTION ongw- INUNDATE wed-! INURE op-! INVADE wadh-2 INVAGINATE wag- INVALID! = wal- INVALID2  wal- INVEIGH wegh- INVEIGLE okw- INVENT gWa- INVERT wer-3 INVEST wes-4 INVETERATE wet-2 INVOKE wekw- INVOLVE wel-3 INWARD wer-3 IODOPSIN  okw-
1707:JOY gau- JUBILATE yu-2 JUDGE deik-, yewes- JUDICIAL deik- JUGATE yeug- JUGGERNAUT gWa- JUGGLE yek- JUGGLER yek- JUGULAR yeug- JUGUM yeug- JUICE yeue- JULEP ap-2, wrod- JuLY deiw- JUNCTION yeug- JUNCTURE yeug- JUNIOR yeu- JUNKER kei-2, yeu- JUNTA yeug- JUPITER deiw- JURAL yewes- JURIDICAL deik-, yewes- JURISCONSULT yewes- JURISDICTION deik-, yewes- JURISPRUDENCE yewes- JURIST yewes- JURY! yewes- JUSSIVE yeudh- susTl yewes- JusTiFy dhé-1
1875:MIR mei-4 MIRACLE smei- MIRAGE smei- MIRE meu- MIRROR smei- MIRTH mregh-u- MIs-1_ mei-1, mei-2 MISADVENTURE gWa- MISANTHROPE ner-2 MISCEGENATION gene-, meik- MISCELLANEOUS meik- MISCHIEF kaput MISCIBLE meik- MISCREANT kerd-1 MISER miser MISERABLE miser MISERICORD kerd-1 MISERY miser MISFEASANCE dhé-1 MISHAP kob- MISNOMER nd-men- MISONEISM newo- MISPRISION ghend-, mei-1 MIss! mei-1 MISSEL THRUSH meigh- MISSILE (s)meit(9)- MISSION (s)meit(a)- MISSIVE (s)meit(e)- MIST meigh- MISTAKE mei-1 MISTER meg- MISTLETOE meigh- MISTRAL meg- MISTRESS meg- MITE! = mai-1
2064:PARTERRE ters- PARTICIPATE kap- PARTRIDGE perd- PARTURIENT pere-1 PARURE pere-! PARVENU gWa-, pert PARVOVIRUS pau- Pas pete-
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2139:PROVE per! PROVENANCE gWa- PROVENDER ghabh- PROVENIENCE gWa- PROVERB wer-& PROVIDE weid- PROVOKE wekw- PROVOST apo- PROW per! PROXIMATE per! PROXY cira PRUINOSE preus- PRUNE? ret- PRURIENT preus- PRURIGO preus- PRURITUS preus- PRY? ghend- PSALM pdl- PSALTERY pol- PSEPHOLOGY bhes-1 PSEUDEPIGRAPHA gerbh- PSEUDOMONAD _men-4 PSEUDONYM n0-men- PSILOMELANE bhes-!, mel-2 PSYCHE bhes-2 PSYCHEDELIC deiw- PSYCHIC bhes-2 PSYCHO- bhes-2 PSYLLA plou- -PTER pet- PTERIDOLOGY pet- PTEROCERCOID pet- PTERYGOID pet- PTISAN pelis-1 PTOMAINE pet- PTOSIS pet- PTYALIN spyeu- PUBERTY pubés PUBERULENT piibés PUBESCENT pubés PUBIC plibés PUBIS plbés PUBLIC populus PUCE plou- PUCKER beu-! PUDENCY (s)peud- PUDENDUM (s)peud- PUEBLO populus PUERILE pau- PUERPERAL pau- PUFF beu-!
2181:RETE era-2 RETIARY era-2 RETICENT tak-1 RETICLE era-2 RETICULE ere-2 RETIFORM ere-2 RETINA era-2 RETINACULUM  ten- RETORT! terkw- RETRACT tragh- RETRAL re- RETRIEVE trep-2 RETRO- re- RETROACTIVE ag- RETROCEDE ked- RETROGRADE ghredh- RETROGRESS ghredh- RETRORSE wer-3 RETROSPECT spek- RETURN tera-1 RETUSE (s)teu- REVEAL weg-1 REVEILLE weg-2 REVEL duellum REVENANT gWa- REVENGE deik- REVENUE gWa- REVERBERATE wer-3 REVERE! wer-4 REVERT wer-3 REVEST wes-4 REVIEW weid- REVIVE gWei- REVOKE wekw- REVOLVE wel-3 REVULSION wel-4 REWARD wer-4 RHABDOMANCY wer-3 RHABDOVIRUS wer-3 RHAPSODY wed-2, wer-3 RHEO- sreu- RHETOR wer-6 RHEUM sreu- RHINOCEROS ker-1 RHIZO- wrad- RHIZOBIUM gWei- RHIZOME wrad- RHODIUM wrod- RHODO- wrod- RHODOCHROSITE ghréu- RHODODENDRON deru RHODOPSIN OkW- RHOMBUS_ wer-3 RHONCHUS  srenk- RHYME sreu- RHYNCHOCEPHALIAN srenk- RHYOLITE sreu- RHYTHM = sreu-
2277:SOP seue-2 SOPOR swep-1 SOPORIFIC swep-1 SOPRANINO uper SOPRANO uper SORCERER ser-3 SORDID swordo- SORDINO swer-2 SORE sai- SORITES teue- SORORAL swesor- SORORITY swesor- SORREL! siiro- SORREL? saus- SORROW swergh- SORRY Sai- SORT ser-3 SORTILEGE leg-1, ser-3 SORUS teue- SOTERIOLOGY teue- SOUBRETTE uper SOUFFLE bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
2294:STEP- (s)teu- STEPHANOTIS stebh- STERCORACEOUS  sker-4 STERE ster-1 STEREO- ster-1 STEREOBATE gWa- STERIGMA ster-! STERILE ster-5 STERN! | ster-1 STERN? sta- STERNOCOSTAL kost- STERNUM Ster-2 STERNUTATION _pster- STEROPE ster-3 STERTOR pster- STET sta- STEVEDORE steip- STEWARD wer-4 STICH steigh- STICHOMETRY steigh- STICHOMYTHIA  steigh-
```


## [2026-09-06T02:20:43.445Z] TOOL CALL #17: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\nfor p in ['data/verification/page-190.json','data/verification/page-189.json']:\n    try: d=json.load(open(p))\n    except Exception as e: print(p,e); continue\n    for e in d['entries']:\n        for n in e['nodes']:\n            if not n.get('words'):\n                print(p, json.dumps(n,ensure_ascii=False)[:1200]); break\nEOF"
}
```


### [2026-09-06T02:20:44.996Z] TOOL RESULT

```
data/verification/page-190.json [Errno 2] No such file or directory: 'data/verification/page-190.json'
data/verification/page-189.json {"id": 2, "lang": null, "words": "", "verdict": "unverified", "derivation": "Empty pass-through box: on the printed page (pdf p. 189, book p. 159; see data/verification/sources/refs/ocr/BOOK/189.png) the box to the right of the Avestan box is drawn but left completely blank — no language, no reference, no word. The extraction is faithful to the page; there is nothing to verify. Judging by the layout of the other charts, this slot was meant for the Persian reflex (the expected fillers would be Middle/New Persian forms of the same root, e.g. NP آز/زور-type words), but the book prints nothing.", "derivation_fa": "جعبهٔ خالی: در صفحهٔ چاپی (برگ ۱۸۹ پی‌دی‌اف، ص ۱۵۹ کتاب) خانهٔ کنار جعبهٔ اوستایی کشیده شده اما یکسره سفید مانده است؛ نه نام زبان دارد، نه ارجاع، نه واژه. استخراج داده‌ها امین بوده و چیزی برای راستی‌آزمایی وجود ندارد. به قرینهٔ چیدمان دیگر نمودارها، این خانه جای بازتاب فارسیِ همین ریشه بوده که نویسنده آن را پر نکرده است.", "sources": [], "ref_check": [{"ref": "None", "status": "not_found", "note": "the node carries no reference in the book."}], "consulted": [{"src": "POK", "where": "pp. 440-441", "stance": "silent", "note": "Pokorny's ĝher- entry lists no New Persian continua
```


## [2026-09-06T02:20:45.054Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ghumb ===\"; grep -n -i \"ghumb\\|humbo\\|jumb\" IEC.txt | head -20; echo \"=== PHD jumb ===\"; grep -n -i \"jumb\\|ǰumb\\|junb\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"jumb\\|junb\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-06T02:20:45.143Z] TOOL RESULT

```
=== IEC ghumb ===
554:anguos, om, à (?) ‘limb; gait’. Cf. anguó Skt. (ambig.) ángam; cf. Gk. -ambos in the cpds. thrí-, í-, dithur-, itthumbos (see dhreiu-, i- and eimi, didhur-, suidh-); cf. kher-ámbe (a mollusc: *hand-limb'. Pelasgian wds. accdg. to H. Frisk GEW)
3276:(dhumbo-, radical form of dhumblos in WG Wasser-tump; Norw. dump dell"
4479:gumb- (gumbh-) ‘swelling, lump; lumpy, swollen’; gumbstos ‘swollen’. WP I, 562. Cf. gumbhos, ghumb-, 2humb-, etc. (All forms but Gmc. are ambig.) Arm. (ambig.) kumb (knob, hump’, but equally fr. *kumb-, q.v, cf. Skt. kümbah, etc.); Per. cf. gumbed ‘dome; tumbler, glass’; Oss. cf. gumbul “ball of cheese; MHG kumpf ‘blunt’; G cf. kumpfig ‘potbellied’; ON kumpi ‘Jump’; OCS goba ‘sponge’; Cz. houba *fun- gus’; Li. gumbas ‘tumour’ beside gumbstu, gumbti ‘form a lump’; Latv. gumba (fr. Lith.) ‘swelling’. Cf. OCS gostü (‘dense, compact’, fr. *gumbstos) LW in Finn. kumpu ‘hill’, and in Hung. gomba ‘fungus’
5067:ghumbos, å ‘hump, lump, rump’. (Most of the evidence is ambig. Cf. gumb-) Alb. cf. gumé ‘rock’, and (alleged) i gumbét ‘potbellied’; Swed. gump ‘rump of birds’. For OCS gọba, Li. gumbas, see gumb-
5068:ghumbho ‘bend, incline, lie down’. Cf. ghubh-, ghoubh- Arm. gmem ‘lie down’. Loss of *-bh- as in ca- mem ‘chew’, see ĝombh-); Li. gumbu, gùbti, intr. ‘bend’; Norw. Sw. (ambig.) cf. gubbe “old man’
6136:êĝhüb- (variant of type ĝubh-, q.v. Slavonic forms are ambig.) ‘stir, move MHG gupfen ‘og, jolt; Sw. guppa (‘swing, sway’. Cf. ghumb-); OCS zybljo, zybati (stir, move’. Cf. $übh-. Ambig.); R zybí ‘swell, stir, surge’; zybkij ‘unsteady’. See 2humb-
6144:$humbo (£hub-) “start, move, jump, stir”. Cf. $hüb- Per. jumbam -1dan, intr. “move, stir; MLG E LG gumpen (*jump'. The English wd. derives fr. Norman Fr. implied in Sard. giumpai, cf. the LW jug and MHG gucke, id.). (Isophones: MLG gumpe ‘eddy’; LG gumpe *'cesspool")
8959:Klub-, cf. KIumb- (1) “hop, hobble’ MHG lupfen, lüpfen (2) jump’; Li. SJumbü, Slübti ‘limp’; Slübas, adj. ‘lame’
9719:leu£6, io ‘loosen, crumble, shred’. (Variants: loug-, lug-) Arm. cf. lujc “loose, free, fluid; lucanem, tr. ‘release’; OHG liohhan ‘pluck, têar; MHG liechen & lüchen (OO) ‘tug, pluck, tousle’; refl. withdraw); G leuchen ‘pill flax; hackle’; Pol. cf. luzny (“loose”, adj.); cf. luzem i$c ‘run loose’; (o-gde in) Li. láužiu, -ti ‘break’; Latv. laužu, lauzt, id.; cf. Li. láužas ‘log-pile’; Latv. lauza ‘breakage; jumble; crowd’; Cz. luza ‘ommon herd’; z-gde in MHG lücke, adj. ‘Joose’; extn. in G locker, id. (Isophones: Gallo-Lat. leuga ‘league’ and MHG liechen, lüchen, sv. 2 ‘lock’: ON ljúka, sv. end: z-gde lok, n. rend, loka, f. “lock, latch, bolt’. (EB: DELG: leugaléos confused and untenable)
10882:mlios, iə “jumble, mixture, tangle’. WP II, 294 Gk. mallós ‘flock, tress’; Fris. molje, v. *wal- low’; Sw. mólja ‘jumble’; Norw. mólje, id.; Srb. malje, fpl. (“fluff, down’: Gk. malliá, mal- íon ‘tress, lock, fleece’ & malós ‘shaggy’); Li. milas, m. ‘homespun’; Latv. mila ‘coarse cloth’
14869:*tumult; job lot, jumble'; Du. rommel, id. be-
15718:skinb- ‘bent, twisted; bend, twist, hollow’ Gk. skambós, adj. 'bandy-legged'; cf. skan- in skán-dalon (&bent-device', hence ‘trap’, cf. dolos); denom. in skambóo, v. “twist; Hes. cf. *skambérizontes, mpl. ‘slipping’; Alb. cf. hümbet, mp. ‘subsides’ beside humbon, v. denom. 3s. id.; MHG schumphe, wf. ‘trollop, paramour’; (?) EME skimp, adj. ‘scant’; E to skimp, v. ‘to do negligently’ (from Norse, but unidentified as such); Sw. skumpa, v. ‘hobble’. Cf. o-gde MHG schampf, m. “trick, joke’; Du. schampen, v. 'graze, scrape! beside EMDu. schampen, v. ‘stumble, abuse; E (from Norse?) scamp, v. ‘do negligently’; s. ‘rogue’; & e-gde in MHG schimphen, etc. Cf. skemb- (but without further connexions)
17750:(sthumbos, cf. sthmb-. WP II, 624)
=== PHD jumb ===
PHD.txt:414:jawédan [LOLMN < А l-Imn; ywyt?n' | (P y'wyd?n, M Pyn), N ~] eternally, always. ~ag [-k! | (P -g), N ~a] eternal, perpetual. jawén [S£yn! | № jawin] made of barley. jeh [yh, yyh = Av. jahi-] the Whore, female arch-demon. fiw [суш!, yyw! = Av. fiwya-] (consecrated) milk. *jomā [ywm’y] together with; both. jorda [ywilt’y, 2k | (P yw?rd?w), J *jwrd?r] corn, grain. jo(y) [ywd, ywb! | N ~] stream, channel. Jóy-, -išn, v. Jadan. jud [ywdt' | M jwd] separate, different; anti-. ~ az [N juz] except, apart from. judàg [ywd? h! | N juda] separate, different. ~ih: separation, difference. Jūdan, jóy- [ywtn!, ywd- | M jwwdn, (jw-), (N jawruan)] chew; devour (daevic). „išn: eating (daevic). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk!] schismatic, heretic. ~th: heresy. Juy [усе | N ~] yoke. Jumbāģīh [ywmb’kyh] motion. jumbénidan, jumbén- [ywmbyn-yin'] (cause to) move. jumbidan, jumb- [ywmb-yin' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- [ywmbyh-stn'] be moved. juttar [ywdtl | M jwtr] different, otherwise. --īh: opposite, reverse. Juwān [ywb?n! | (P ywn), N jawàn] young; a youth. ~th: youth. juxt [ywht! | (P ywxt), N juft!] pair, couple.
PHD.txt:2854:motion jumbāgīh, Jumbisn, rawišn; set in — rawagenidan.
PHD.txt:2864:move ēwarzīdan, jumbidan, raftan, wazidan, wihēz-; — quickly šēb-; cause to — jumbēnīdan, wāzīdan.
PHD.txt:2865:moved, be — jumbīhistan.
PHD.txt:2866:movement čandišn, éwarz, jumbišn, wāzišn, wihēz(ag).
PHD.txt:5427:jumbihistan jumbén- jumbénidan jumbidan dumb
PHD.txt:5428:jumbišn
PHD.txt:5444:gurgānīg gursagih gursag durgar jorda jorda 1-2gurdih gurd gurdwar gurdag dum, 1021 joma jomā gumānīh gumānīgīh gumānīg gumān gumāngar gumār- gumārdan gumārdag jumb- dumbēmand jumbāgīh jumbīh-
PHD_mackenzie.txt:3096:Jumbagih [ywmb'kyh] motion.
PHD_mackenzie.txt:3097: Jumbenidan, Jumben- [ywmbyn-ytn l] (cause to) move.
PHD_mackenzie.txt:3098:Jumbidan, Jumb- [ywmb-ytn ' IN,...,] move.
PHD_mackenzie.txt:3100: Jumbihistan, Jumbih- [ywmbyh-stn ' ] be moved.
PHD_mackenzie.txt:7096:minute (of arc) lipi.                          move ewarzidan, jumbidan, raftan,
PHD_mackenzie.txt:7098:miraculous power, having ...... warz~            cause to -- jumbenidan, wiizidan.
PHD_mackenzie.txt:7099:  iiwand.                                      moved, be ...... jumbihistan.
PHD_mackenzie.txt:7100:mirror ewenag.                                 movement eandisn, ewarz, Jumbisn,
PHD_mackenzie.txt:7138:motion jumbiigih, Jumbisn, rawisn;             necessity abayisn.
PHD_mackenzie.txt:10665:dostih                     ..-e" tf,1t,.     Jumbihistan                     -J6 t'
PHD_mackenzie.txt:10667:dost                          It-e.u .-      Jumben-
PHD_mackenzie.txt:10669:1-2dawistan                                  jumbcnidan
=== NYB ===
4456:tyumbišneh [*ywmbšnyh] det. v. n.: star ~ the motion of the stars 109%. — Paz. junb- ‘to move’, v.n. junbasn; junbä ‘mover’ (SGV); NP junbidan; cf MPrth ywb- ‘to lament, to mourn’. — Text: ynbsnyh; it would have been better to correct it to ywnb- = Paz. NP.
6671:junb- etc.: yumbišn
7228:junbīdan: *yumbišnēh
```


## [2026-09-06T02:21:09.271Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG jamb/jumb ===\"; grep -n -i \"ǰamb\\|jamb\\|ǰumb\\|jumb\" CHEUNG.txt | head -20; echo \"=== HRN ===\"; grep -n -i \"unbīdan\\|junb\\|jumb\\|ǧunb\" HRN.txt | head -20; echo \"=== HUB ===\"; grep -n -i \"junb\\|jumb\" HUB.txt | head -10"
}
```


### [2026-09-06T02:21:09.350Z] TOOL RESULT

```
=== CHEUNG jamb/jumb ===
14336:*MIDDLE PERSIAN: MMP jwmb-, BMP ywmb- /jumb-/ ‘to move’, BMP ywmbyn- 
14337:/jumbén-/ (caus.) ‘to cause to move, move [tr.] = DMMPP: 199b 
14339:Pres.: IND. 3sg. BMP ywmbyt /jumbéd/; Partic.: perf. pass. II MMP jwmyst, caus. BMP ywmbynyt 
14340:/jumbénid/; Caus.: pres. IND. 3sg. BMP ywmbynyt /jumbénéd/, IMPV. 2pl. BMP ywmbynyt /jumbénéd/; 
14341:Pass.: pres. IND. 3sg. MMP *jwmbyhyd; Inf.: BMP ywmbstn /jumbistan/ 
29934:*SANSKRIT: jambh ‘to open the jaws wide, snap’ (RV+) = EWAia I: 572 f. 
29936:9 The nominal derivative *zamba- ‘tooth’ (= Skt. jambha-) is also attested in Ir., 
29969:*SANSKRIT: jambh ‘to crush, to destroy’ (RV+) = EWAia I: 572 
35786:ywmb- /jumb-/, 212 
35788:ywmbyn- /jumbén-/, 
51603:Jambh, 463, 464 
=== HRN ===
=== HUB ===
```


## [2026-09-06T02:21:10.687Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC page markers near 6144 ===\"; grep -n \"\\[pdf page\\|^Page\\|^p\\. \" IEC.txt | head -5; awk 'NR>=6100 && NR<=6150' IEC.txt | head -60"
}
```


### [2026-09-06T02:21:12.299Z] TOOL RESULT

```
=== IEC page markers near 6144 ===
ĉhol- (3) (?)
R zolà 'ash, ashes’; Pol. zoła ‘lye, buck’; Li. žălas ‘red-brown’
ĉholg-, see ĝhalg- and cf. WP I, 540
Sholtos, ios, io (&hlt-) “yellow, green". WP I, 625. Cf. ghel-, &hol- (1) and gheleuos Oss. zäldä ‘greensward’; OCS (and com. Sl.) zlatü ‘golden’; zlato, n. ‘gold’; Li. žaltys, gs -čio ‘adder’ beside žalsvas ‘green’; Latv. zaltis, zalktis ‘grass-snake’
$hongholos (-õlos, -ilos) “going, mobile, via-
ble; goer’. Cf. £hengh- Skt. cf. janghalah, 'swift-footed'; Arm. (?) cf. dzandzay (w. assimilated consonants? ‘shal- low’); MHG gengel ‘wide-ranging’; LG gángel ‘rocker on cradle’; ON gọngull ‘restless, mobi- le’. See next
êhonghos, à ‘going; gait, pace, stride, leg’.
WP I, 588. Cf. ghengh- Skt. jánghā ‘lower leg’; janghā-, cpds. “of feet’; Oss. zäng ‘shin; mountain-range'; Go. gagg; MHG ganc, gs ses OE gang; ON ganer, cf. ganga, sv. 7 ‘go’; gengr ‘able to walk’; Li. cf. í-Zanga ‘introduction’; Zangüs “fleet-footed?. (Isophonic: Hindi jhanjhi ‘shell’: Gk. kógkhē, id.)
423
£hor- (ghoros, à) (1) ‘shine, light, ray, beam’. Cf. gherio Slovene zor, zora ‘red of dawn’; Srb. zora ‘dawn’; Li. Zarà, id. beside (archaic) Záras ‘sun- flower’; Latv. zars (2) ‘ray, beam’
hor- (ĉhoros) (2), “line, series, troop’
Gk. khorós ‘round dance’; Li. žãras “line,
troop’; phr: sàvo Zar, “in its turn, on the
other hand’. (Isophonic: Skt. jahra ‘waterfall’) $hordh-, ghort-, see Supt. 2h-
$hornos, à, us ‘gut, string, cord". Cf. WP I, 604 Br. cf. gor, pl. goriju ‘yarn’; OHG garn; OE gearn:Du. garen, id. beside garen, adj. "of yarn, of thread’; ON garn ‘yarn’ beside gorn, pl. garnir, f. ‘gut’; Li. Zarnà ‘gut’; Latv. zarna, id. (Kinship with Lat. hernia and haru-spex uncertain)
8houono- ‘casting, pouring’. See $heu-, 8heumn-, 2huuó, etc. WP I, 563 Skt. hávanam “offering”; Arm. dzawn, i-st “gift, dedication’; Gk. khóanos ‘furnace, crucible’; khoánë ‘hopper, dish, furnace’. Alb. cf. dhun- tí ‘gift. See next
$houos, à “outpour, casting’. WP I, 563. Cf.
9heu-, 8heumn-, £huuo, etc. Skt. havab ‘sacrifice’; Arm. cf. (e-gde) dzev, o-st. ‘shape’; Myc. -kowa (in a cpd. epithet of *oil); Gk. khóos, khoüs “liquid measure, dyke, mound’; khoé *outpour'; cf. also khóo, khónü- mi 'pile up'
&hredó ‘roar, din, resound, shout'. (Variant
of type *ghréd-, cf. ghrodió) (The initial is ex- plicit only in Av. zràd-, otherwise *gh-) Skt. hrade, v. beside hradah ‘din’; Av. zrād-; Ir. (*-é-) greadhal ‘clatter, roar, bustle’; Go. grétan ‘weep’; grets, m. ‘weeping’; MHG gra- zen “cry, bluster’; OE grætan; ON gráta
&hridh- (ghridhst-, $hrdh-) ‘barley, grain’. Cf. ieu-. WP I, 611 Gk. krithé; Alb. drithé, n. (id. fr. *&hridhst-); OE grist ‘grinding of corn’; E grist. (Zero- vocalism implied in Lat. hordeum)
£hr-, &hr-, radical element of &hér- ‘hang’, q. v. Cf. ghrt-
Gk. cf. me-khri (“until : Arm. merdz), and Gk. khár-meé ‘hand-to-hand fighting?
(8hrdis, iə, Indo-Iranian variant of type Krd-
$hor- (horos, à) — ghúl-
10
20
25
30
35
40
45
424
‘heart’, q.v. Cf. WP I, 424, 641 Skt. hrd, hrdayam; Av. zaroóayom; zarozdan; Per. dil; Oss. zárdà)
hrt- (ghrtis, os) ‘gripped, collected; grip, seizure, handful'. Cf. ghër- Skt. cf. sam-hrtih ‘seizure’; -hrtah ‘collected’; Lat. co-hors, gs -hortis (2) ‘band of men (se- mantics of mani-pulum ‘handful, troop")
$hu- radical theme of types gheu-, 8hou-, $huuó, q. V.
êĝhüb- (variant of type ĝubh-, q.v. Slavonic forms are ambig.) ‘stir, move MHG gupfen ‘og, jolt; Sw. guppa (‘swing, sway’. Cf. ghumb-); OCS zybljo, zybati (stir, move’. Cf. $übh-. Ambig.); R zybí ‘swell, stir, surge’; zybkij ‘unsteady’. See 2humb-
&hud- ‘pour, spill, waste, destroy’. Cf. huuó, Sheu-. WP I, 564 Per züdan (2) *erase'; Lat. fudi, pf. of fundo *shed, scatter, hurl down, vanquish; yield, produce'; Go. cf. us-gutnan "be scattered'; MHG gus 'outpour'; güsse ‘flood’; OE gytt, gyte, id.; Sw. gyttja ‘quagmire’; Gk. cf. ko- khudéo (“stream forth’, fr. *&hu-ghud-); Li. cf. žudaŭ, -ýti ‘destroy’: Latv. züdu, zust ‘perish’; zudinaju ‘lose, mislay’; zūdīties ‘fret’. Cf. (am- big.) Av. u(s)-zü10ya- ‘welling-up’. (Isophonic: Oss. zudä, Iron. zíd ‘greedy’; cf. E to guttle; Icel. gutl, n. *gurgling). (For Du. guit ‘rogue’; Norw. gutt “boy” see Supt.)
&hugh-, &hughno ‘stir, shake, tremble, agi- tate' MHG gugen "rock sway’; gogen ‘rampage’; G cf. Gug, Güge ‘prank’; Gmc. LW in Fr. gogue ‘revelry’ beside gogaille, id. (MHG gogel, gol, adj. ‘wanton; lewd joke’, hence E a-gog :Fr. en gogue; Fris. apparently also gol, gul folly’, but OFr. joli ‘gay’, mod. ‘pretty’ is of doubt- ful association in view of Lat. iovialis and gaudiālis as possible though ambig. back- grounds for this wd.). For type ghughnó, cf. ON gugna ‘tremble’; Blg. zázna, id.
£hu-8hu-, redup. theme of ghu-, see ghuuo, and cf. &heuó Arm. dzdzum, s. ‘churn’; dzdzmem, v. ‘churn’; Gk. kokhüzo ‘gush’, beside kokhu- déo, id.
£hul- (1) “bad, violent, evil, wrong
425
Av zurō ‘force’; OPer. züra- “Wrong, evil’; MHG gül ‘nag, jade’; G Gaul, ON cf. gyl-fra ‘witch’; Du. guil “nag, jade; MHG cf. also mir golt, inf. gollen “I detest’; OCS zülü “evil”, adj.; zülo, zlo, n. & zült, f. id.; Li. Zulüs, į-° ‘impudent, obtrusive’; žūlù, Zülti ‘obtrude oneself: OCS zljo, zliti ‘afflict’
£hül- (2) (ghülos, is) “discharge, outpour, WP I, 563 Hind. cf. hüli (allegedly a feast in honour of milkmaids); Arm. dzujl, adj. *melted'; s. “cast, ingot: Gk. khülós “juice, decoction’; Umb. hule, m. (name of a god); W gil, pl. ion *yield; ferment’; (*-ü- in) MHG gülle, G Gülle ‘pud- dle, esp. from dung’; E dial. gowl ‘matter from the eyes"; (in mining also: *coal-sludge"); Icel. cf. gül-sopi *gulping sip”
$humbo (£hub-) “start, move, jump, stir”. Cf. $hüb- Per. jumbam -1dan, intr. “move, stir; MLG E LG gumpen (*jump'. The English wd. derives fr. Norman Fr. implied in Sard. giumpai, cf. the LW jug and MHG gucke, id.). (Isophones: MLG gumpe ‘eddy’; LG gumpe *'cesspool")
$hustos ‘poured, scattered, wasted; outpour, pouring, casting’. Cf. ghu- Gk. khüstos “a decoction of red dye and vine- gar; LG güst, Ger. & Du. gust, Swiss güste ‘barren, non-milch". The extn. *ghus-, cf. $£hu-, etc. is present in OE gorian (2) ‘pour away’; Icel. gos ‘gush, spout’
i-, radical element of type ei-mi ‘go’, q.v. Cf. Hom. Gk. íe ‘he went: EMAIb. u-i, id. (for Alb. u, see seu, seui), OLat. cf. 1-erð & Lat. 1-rem. Cf. also itós, itis. The vocalism of Hitt. iyami ‘go’ is uncertain
-i, an adverbial theme.
Skt. div-i “by day’; Gk. di(w)i, id.; Lat. (Plau- tine) cf. diu, id.; Arm. brni ‘violently’; art mni ‘awake’; heti Con foot’, cf. Lat. pede-pressim, -tentim, cf. Gk. par podí; Lat. pro-pe (*d)
£hül- — -ibhi(s)
20
```


## [2026-09-06T02:21:27.588Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG context ===\"; sed -n '14320,14350p' CHEUNG.txt; echo \"=== HRN unb ===\"; grep -n \"unb\\|umb\" HRN.txt | grep -i \"id\\|bew\\|move\" | head -10"
}
```


### [2026-09-06T02:21:27.661Z] TOOL RESULT

```
=== CHEUNG context ===
nos-/nota ‘to take (in marriage), seize’, Yzgh. n(a)yas-/nayud ‘to seize, catch, take 
(in marriage), buy; to bite [of dogs]’ 

*SANSKRIT: yam ‘to hold, restrain, drive (horses), stretch out’ (RV+) = EWAia II: 
399 

*PIE *jem- ‘to hold’ — LIV: 312 f. | Pok.: 505 


ТЕ COGNATES: ? 
*REFERENCES: КРЕ I: 209b; EVP: 100; IIFL П: 192b, 233a; Abaev, Slovar’ I: 552; EVS: 106a, 52a; 
Werba 1997: 221; NEVP: 100, 58 


*ja(m)b/p ? ‘to move, wander, rove, crawl ?° 

*MIDDLE PERSIAN: MMP jwmb-, BMP ywmb- /jumb-/ ‘to move’, BMP ywmbyn- 
/jumbén-/ (caus.) ‘to cause to move, move [tr.] = DMMPP: 199b 

Pres.: IND. 3sg. BMP ywmbyt /jumbéd/; Partic.: perf. pass. II MMP jwmyst, caus. BMP ywmbynyt 
/jumbénid/; Caus.: pres. IND. 3sg. BMP ywmbynyt /jumbénéd/, IMPV. 2pl. BMP ywmbynyt /jumbénéd/; 
Pass.: pres. IND. 3sg. MMP *jwmbyhyd; Inf.: BMP ywmbstn /jumbistan/ 

*SOGDIAN: BSogd. y B, CSogd. y’b, MSogd. y'B ‘to wander, travel, rove’, CSogd. 
y’b’qcy (obl.) ‘wandering’ || (+ *a-) BSogd. ’’y’Bs- (intr./inch.) ‘to be deceived, 
perverted’, BSogd. ’’y’np-, CSogd. ’ymp- (caus. ?) ‘to pervert, seduce’. 0 BSogd. 
"y'np- does not mean “о commit adultery’, as translated initially by Henning 1939: 
103 (whence connected to Skt. yabh, etc. by Mayrhofer, EWAia II: 398 f.; Kümmel, 
LIV: 309 et al.). The verb is well attested in Sogd. generally and clearly has the 
meaning ‘to pervert, deceive, lead astray, sim.’, cf. e.g. MacKenzie, BSTBL: 75; 
GMS: §653, 827; Sims-Williams 1984: 206b. 
=== HRN unb ===
576:Dazu efröiZiden 'ordnen, das aber ebenfalls unbelegt
1601:137. 7? 'dieser in Ider *hier, Jdrä (unbelegt), tderi (Näs.
6498:746. {2)sumi^ sunb 'Höhle, Loch*, smnhiden^).
7748:892. f/iidäre 'Brett (zum Dachdecken)' (unbelegt).
7943:(vejer) 'richterliche Entscheidung (unbelegt).
10659:*) Np. weida ist unbelegt.
13175:ntthunbiden 1059.
19592:sumbiden 746.
```


## [2026-09-06T02:21:29.630Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT aiwi.gaiti ===\"; grep -n \"aiwi\\.gaiti\\|aiwi-gaiti\\|aiwigaiti\" BRT.txt | head; echo \"=== BRT vigatha ===\"; grep -n \"vī̆\\.gāθ\\|vi\\.gāθ\\|vigāθ\\|gāθō\" BRT.txt | head; echo \"=== BRT nijam ===\"; grep -n \"ni\\.jam\\|nijāma\\|jamaye\" BRT.txt | head"
}
```


### [2026-09-06T02:21:29.714Z] TOOL RESULT

```
=== BRT aiwi.gaiti ===
=== BRT vigatha ===
=== BRT nijam ===
10012:von  den  ASp.  besucht  ist"  G,  2.'hraigta':  ya  mqm  ams  jamayeiti  yo  ..\\, 8.  a)  Des.  'hin  cu  kommen,  hin  zu  ge-  ly.  zo.  Undeutlich:  jimsp^  F.  ly,  — langen  suchen':  mmB  ..aSai  *jih3l^^  aku-  jasäiti  YX.4-i*-  VSIK.  ja-jmvak-  sbes. mn  Ny.M.  2)nutLok,;  namn..aSa-        mita/rt  i)'wegkommen,weggehenvon-'
```


## [2026-09-06T02:21:56.418Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14350,14375p' CHEUNG.txt"
}
```


### [2026-09-06T02:21:56.468Z] TOOL RESULT

```
GMS: §653, 827; Sims-Williams 1984: 206b. 

Pres.: IND. 1sg. dur. CSogd. y'bmsq, 3sg. BSogd. y’Bt, Partic.: pres. BSogd. y’B’k, BSogd. y’B’y, 
MSogd. y’Byy (Sogd.Tales: 473) || (+ *a-) Pres.: IND. 3sg. BSogd. ’’y’Bst, MSogd. ’’yfstt, 3р1. MSogd. 
"yfsnd; Partic.: pres. CSogd. ’ympnyt, perf. pass. BSogd. ’’y’Bt-k, MSogd. ’’yBtyy ‘perverted, false, 


*jaš ? 213 


wrong, heretical’, (Ё) BSogd. ’’y’Btch, CSogd. ’ybty ‘astray’; Caus.: pres. IND. 35р. BSogd. ’’y’npt, fut. 
IND. 3sg. CSogd. ’ymptq’ 

*CHORESMIAN: y’B- ‘to go slowly, crouch’ => Samadi: 254 

*NWIR: NP junbidan/junb- ‘to move, stir, shake [intr.]’, Awrom. jimay-/ jim- ‘to 
move [intr.]’, Gur. -jim- ‘to move, stir [intr.]’, Awrom. jimnay-/jumn- (caus.) ‘to 
rock (a cradle)’, NP junban (ptc.) ‘moving, shaking’ || (+ *4-) NP efudah ‘silly’ (< 
Sogd., Henning 1939: Lc.) 

*NEIR: M. yob-/yéby- (denomin. ?) ‘to dance’ (Zarubin), M. yoba ‘dance’ 

© A root different from the IE ‘futuere’ forms has to be postulated on account of the 
Iranian evidence. According to Schmidt 1992: 113, Toch. A yäw-, B yäp- is 
connected to these IE futuere forms (*Hiab), preserving the more archaic meaning 
‘to enter’. Winter 1998: 185 expresses some reservations, as only one subfamily, the
```


## [2026-09-06T02:21:56.896Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 1059 ===\"; grep -n \"1059\\.\" HRN.txt | head; echo; grep -n \"^1059\\|1059)\" HRN.txt | head"
}
```


### [2026-09-06T02:21:56.964Z] TOOL RESULT

```
=== HRN 1059 ===
9154:1059. nihuften , nuhuften Verbergen', Praes. nihuft-em,
13147:n/ÄSw 1058, 1059.
13148:nihenbiden 1059.
13149:nihuften 1059.
13173:nuhnffen 1059.
13175:ntthunbiden 1059.
16513:.il(i)huftn„ 1059.
17631:9.)p«- 1059.
19459:I njxäftin 1059.
19460:i nj^jiin 1059.

8611:niele% 'Heuschrecke' (Öähn. I, 188 Vers 1059) s. meig
9154:1059. nihuften , nuhuften Verbergen', Praes. nihuft-em,
```


## [2026-09-06T02:22:09.298Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN unbiden ===\"; grep -n \"unbiden\\|umbiden\" HRN.txt | head -20"
}
```


### [2026-09-06T02:22:09.348Z] TOOL RESULT

```
=== HRN unbiden ===
13175:ntthunbiden 1059.
19592:sumbiden 746.
```


## [2026-09-06T02:22:11.458Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 باسن ===\"; grep -n \"باسن\" BQT_v1_pages.txt | head -10; echo \"=== MON ===\"; grep -n \"باسن\" MON_part1.txt MON_part2.txt | head -10; echo \"=== ARY ===\"; grep -n \"باسن\" incoming/ARY/ARY_pages.txt | head; echo \"=== BQT جنبیدن ===\"; grep -n \"جنبیدن\" BQT_v2_pages.txt | head -5; echo \"=== MON جنبیدن ===\"; grep -n \"جنبیدن\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T02:22:11.588Z] TOOL RESULT

```
=== BQT v1 باسن ===
1928:م‌تشرقین فرانسوی که بدانجا رفته اند» اين لفات را دیده و باسنچیدن با
11157:اد و سس باسنبی‌نقطه بروزن‌تجنیس»
11572:د ذاب ۰ ۱ : ۲۷۵-۷۲6 > . ۱ - در اوستا ویارسی باسنان 254 - 25۳0 » ای کلم
14068:افحوسا؟ » باسن بی‌شقطه بالف کشیده.
15096:در زبانهای اوستابی و پارسی باسنان بمعنی پناه و کومكك گرفته‌اند - دالا 121012 احتمال میدهد
18221:و آنٍ معروف باب کر گر است که هنوز موجود میباشد . کف رودخانه را باسنگهای بسیارمسکم
23659:باهنگ بروزن وععتی باسنگه‌است»
26991:هست - و زبان فارسی باسنانی را نیز گوبند که
28520:ئا یسر - باسن بی‌لقطه بروزن بازیگر»
29101:120128 د< بارتولمه ۱۲۳ > و 8610 , از پلرسی باسنان 211502) « بارتولمه ابا * » از
=== MON ===
MON_part2.txt:31386:هی کاق باسن: . (اخ.) گرز فریدون که 
MON_part1.txt:59755:دباسن. 
=== ARY ===
12034:چم اين واژه در زبان لاقین؛ کپل» سرین؛ باسن.
=== BQT جنبیدن ===
2672:‫جنبید = طم اول“ماضی‌جنبیدن‌است ‪-۷‬‬                    ‫=ح اووثلانی بورزن حلب »‬
7056:                   ‫استعمالم کنندا ‪. ۰۷‬‬                 ‫= بضم اول بروزن جنبیدن‪",‬‬     ‫چنییدن‬
13594:‫حنبیكن ب=روزن‌جنبیدن» بمعنی خنبك‬                                 ‫خنیر ةٌدود ناك ‪ -‬کنابه آاسزمان‬
38220:                                                             ‫بفتح‌اول بروزن جنبیدن»‬        ‫سنییدن ‪- ۴‬‬
=== MON جنبیدن ===
MON_part2.txt:3825:مایة رشکك. جنبیدن غیرت کسی: به غیرت 
MON_part2.txt:39985:نااستوار بودن در جای خود و جنبیدن 
MON_part2.txt:41167:خود جنبیدن (مانند کرم و مار). رفت و آمد 
MON_part2.txt:81144:جنبیدن» حرکت کردن. لرزیدن. بر خود 
MON_part2.txt:86037:وزان» وزیده» وزش). جنبیدن هواء حرکت
```


## [2026-09-06T02:22:26.113Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON junb ===\"; grep -n \"junb\\|jumb\\|unbīt\\|unbit\" MON_part1.txt MON_part2.txt | head -20; echo \"=== MON basan ctx ===\"; sed -n '59740,59775p' MON_part1.txt"
}
```


### [2026-09-06T02:22:26.206Z] TOOL RESULT

```
=== MON junb ===
=== MON basan ctx ===
پفیوز» تنبل. 

دیور: 1200۲ [ع.] (.) بادی که از مغرت 
وزد؛ ناد غربی؛ مق. صبا. (تص.) صولتی که 
منشاً آن هوای نفس و استیلای آن بود و 
موجب صدور چیزی باشد که مخالف شرع 
است (کشاف اصطلاحات ۴۱۵؛ فرع. 
سج.) 

دی وری: ]-1:07 (ص.) (عم.) لاات» 
۳ 

دبوس. (ف. -.اا0ا2)وتاداداد [معر . دنوش ] 
(.) عمود آهنین» گرز آهنی؛ چوبدستی 
تفر که‌آسر. ان کشت و گره‌دار باشد؛ ج. 
دباسن. 

دسوسک: 0 (کا.) بنیر کك» 
خبازی» نان کلاغ. 

دبه: ٩«002)-۵(‏ [ع. دب ] (ا.) ظرف چرمین یا 
فلزی که در آن روغن و مانند آن ریزند. 
صراحی کوچک» شيشة کوچک. (مج.) 
اثائه» لوازم. دبه باروت: کیسه‌ای از پوست یا 
محفظه‌ای چوبین یا فلزی که در آن باروت 
کنن. دبه و زنبیل (در) افزودن: خرج کسی 
زیاد شدن. دبه در زیر بای شتر افکندن: 
(کد.) مرتکب امری خطیر شدن. بر سر 
پرخاش آوردن» فتنه انگیختن. 

۵ لسسسسسته دراوردن: ]1.01۵ 


۲" ۱ فرهنگت فارسی سوه ۲ دییسا
```


## [2026-09-06T02:22:27.327Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/git 2>/dev/null; grep -o \"MON_part[12].txt[^\\\"]\\{0,80\\}\" /home/sfmqrb/git/rishe/data/verification/page-1*.json | head -10; echo ===; grep -o \"\\\"src\\\": \\\"MON\\\", \\\"where\\\": \\\"[^\\\"]*\\\"\" /home/sfmqrb/git/rishe/data/verification/page-1*.json | head -10"
}
```


### [2026-09-06T02:22:27.412Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/page-107.json:MON_part1.txt line 51660) and s.v. صولجان (line 90586)
/home/sfmqrb/git/rishe/data/verification/page-107.json:MON_part1.txt lines 34020, 49786, 76631)
/home/sfmqrb/git/rishe/data/verification/page-109.json:MON_part2.txt line 73548)
/home/sfmqrb/git/rishe/data/verification/page-109.json:MON_part1.txt line 62153): \
/home/sfmqrb/git/rishe/data/verification/page-109.json:MON_part1.txt line 62153 s.v. دقل
/home/sfmqrb/git/rishe/data/verification/page-108.json:MON_part1.txt lines 63014-63017): 'دموکرات: [Latin-script French etymon] (ص.) طرفدار دموکراسی
/home/sfmqrb/git/rishe/data/verification/page-108.json:MON_part1.txt lines 59508-59517): 'داو: (ا.) نوبت بازی (شطرنج، برد و مانند آن)، نوبت قمار. نو
/home/sfmqrb/git/rishe/data/verification/page-105.json:MON_part2.txt line 40714)
/home/sfmqrb/git/rishe/data/verification/page-105.json:MON_part1.txt, MON_part2.txt and the Adena two-volume djvu find no occurrence. The Borhan foo
/home/sfmqrb/git/rishe/data/verification/page-105.json:MON_part1.txt lines 13363, 13366); s.v. مستشرق (MON_part2.txt line 56159)
(eval):1: == not found
```


## [2026-09-06T02:22:33.012Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"دیابت\" \"آکروبات\" \"اکروبات\" \"باسن:\" \"جنبیدن:\" \"جنبش\" ; do echo \"=== $w ===\"; grep -n \"$w\" MON_part1.txt MON_part2.txt | head -6; done"
}
```


### [2026-09-06T02:22:35.703Z] TOOL RESULT

```
=== دیابت ===
MON_part1.txt:64279:دیابت: »ره (.) (بز.) مرضی که به 
=== آکروبات ===
=== اکروبات ===
=== باسن: ===
MON_part2.txt:31386:هی کاق باسن: . (اخ.) گرز فریدون که 
=== جنبیدن: ===
=== جنبش ===
MON_part2.txt:9996:بودن؛ پذیرای جنبش بودن. قابلیت رژیت: 
MON_part2.txt:17171:حرکت سرین» جنبش سرین به هنگام رقص. 
MON_part2.txt:18650:آوای جنبش مهره و گلوله در مبان طاس و 
MON_part2.txt:29840:جاهنبار معر.] (.) هر یک از جنبش‌های 
MON_part2.txt:39272:لرز: ۱۸۳2 [لرزیدن از تب | (امص.) جنبش 
MON_part2.txt:40344:عده بسیار از هر چیز در حال جنبش: لملمه
```


## [2026-09-06T02:22:43.042Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '64275,64290p' MON_part1.txt; echo \"=== ARY jonbidan ===\"; grep -n \"جنبیدن\\|جنبش\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY context 12034 ===\"; sed -n '12020,12045p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T02:22:43.152Z] TOOL RESULT

```
دی: آ (ق.) روزگسذشته» دبروز. شب 
گذشته» دشبت. 

دیابت: »ره (.) (بز.) مرضی که به 
سبب ازدیاد مقدار خون تولید گردد) 
دیار: ۹۲ [ع. باشنده] (.) کسی» کسی. 
دباری. احدی. 

دیار: 13:۳5 [ع.] (ص. ۱.) دیرنشین» ساکن 
دیر و صومعه. 

دیار: ۲ (ع.] () ج. دار. خانه‌ها» مسا کن. 
شهر» مدینه. سرزمین." 


=== ARY jonbidan ===
121:حاشیه‌ی سرزمین‌های هند و اروپایی را محقق می‌کند و پعید است که جنبش کوچگری هند و
176:بررسی جنبش‌های کوچگرانه‌ی دیگر در دوران‌های تاریخی الگوی کلی این کوج‌ها و پيامدهای
537:پندارهای قدیمی در مورد سرچشمه‌ی زبانها را متزلزل کرد. جنبشی که در دانش زبانشناسی ایجاد شد
15495:چم این واژه در زبان ژرمنی: تکان خوردن؛ جنبیدن» وزن کردن.
=== ARY context 12034 ===
پسگشت‌ها 5 108 :ما05
۳ برهان قاطع : رود
فارسی (۳88514(0): کش, کشال, کشانه (به چم "بغل, آغوش, آسینه آزیربغل", اکشاله:
اوستایی (4723742۷): 1۸ ایر دی کهن (17دلقا 072): ناه
پهلری (۲7ماتق۸ه). ان ولزی (77ق078): 5
پلرچی (7تلحتانلمه): دزندی
سانسکریت (54(8077): پسگشت‌ها هر دای

هتاگکقها بتقکلشا 8 200520
لاتین (7107ل): هه 0 (۸33/۳13) :۵(/25 11۸2
آلمانی کهن (/(4۵ل057 بلعآتز صام): برهان قاطع + ۱۳۳۶ ۱
۱۱۳۹۱ لغت‌نامه دهخدا: ۳ و ۱۸۳۴۷-۸
آلمانی (4۵(0ل652): 112 فرهنگ معین : : ۱۹۷۶
یادداشت:
چم اين واژه در زبان لاقین؛ کپل» سرین؛ باسن.
چم اپن واژه در زبان آلمانی: بند انگشت.
چم این واژه در زبان ایرلندی کهن؛ پا
۹
اوستایی (۹:)۸8742: * سانسکریت (54(5777):
1 ات۴52۸ ,۸0811 87۰ ,1617811۳۸11
پهلری (7ساتتهه): بونانی 078270): لا( ۷۱:۱۱
08۸ ,105117۸0۷ هنت (7[777778(): م ادا
کردی (7۵/54). لا ۱۹
پلرچی (1لتاملم1)1871۸011:)8 ,2011851۸6
سم
[pdf page 405]
```


## [2026-09-06T02:22:59.854Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"کروبات\\|کربات\" MON_part1.txt MON_part2.txt | head; echo \"=== heads of MON parts ===\"; head -3 MON_part1.txt; echo ...; head -3 MON_part2.txt; echo \"=== KLN diabetes/acrobat/base/abyss/byssos ===\"; grep -n -i \"diabetes\\|acrobat\" KLN_1966.txt | head -6"
}
```


### [2026-09-06T02:22:59.942Z] TOOL RESULT

```
MON_part1.txt:19579:توکربات.: باب دندان: غذای مطابق سسلیقه» 
=== heads of MON parts ===
0 
2 

...
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


=== KLN diabetes/acrobat/base/abyss/byssos ===
74:batophobia,  n.,  a  morbid  fear  of  being  at  great  heights  or  passing  near  high  objects  (med.)  —  Medical  L., compounded  of  Gk.  (ia to?,  ‘passable’,  verbal  adj.  of  patveiv,  ‘to  go’,  and  -yofiri,  fr.  ip6(3o<;,  ‘fear’. See  base,  n.  and  phobia.  The  association  of  Gk  {Ja-ro?  with  height  is  due  to  a  connection  of  this word  with  the  second  element  in  acrobat.  (Acrobats  are  used  to  display  their  art  in  the  height.) A  more  adequate  name  for  this  condition  is  hypsophobia.
1497:acrid,  adj.  —  A  blend  of  L.  deer  (fern,  acris ,  neut. acre),  ‘sharp,  bitter’,  and  acidus,  ‘sour’,  which are  both  related  to  L.  acus,  ‘needle’,  acies,  ‘sharp edge,  point,  the  front  of  an  army,  line  of  battle, battle  array’,  acuere,  ‘to  sharpen’,  fr.  I.-E.  base *ak-,  *aq-,  ‘sharp,  pointed’,  whence  also  Oscan acrid  (=  L.  deriter),  ‘sharply’,  Umbr.  per-acri, ‘fruitful,  fertile’,  Gk.  axpop,  ‘at  the  farthest  point, highest;  pointed’,  4x4),  ‘a  point,  edge’,  4x1?,  ‘a point’,  axavS-a,  ‘thorn,  prickle’,  4 kwv,  ‘a  jave¬ lin’,  4x|X(ov,  ‘an  anvil’,  OI.  asrih,  ‘edge’,  asman-, ‘stone,  rock,  sky’,  Avestic,  asman-,  of  s.m.  Lith. akmuo,  ‘stone’,  asmuo  ,‘sharpness’,  OSlav.  kamy (a  metathesized  form),  ‘stone’,  OIr.  er  (for •akros ),  ‘high’,  Arm.  as-eln,  ‘stone’  (the  force of  the  suff.  -eln  is  yet  unknown),  ON.  hamarr, OE.  hamor,  hamer,  etc.,  ‘hammer’.  Cp.  Gk. axpodtopai,  ‘I  hear,  listen’,  prop,  ‘have  a  sharp hearing’,  in  which  the  first  element  is  rel.  to Sxpo p,  ‘pointed,  sharp’.  —  Cp.  the  gradational variant  base  *oq-,  whence  Gk.  6£u p,  ‘sharp’, oxpip,  ‘peak,  hilltop',  OL.  ocris,  ‘a  rugged,  stony mountain’,  L.  mediocris,  ‘middling,  moderate, indifferent,  tolerable'  (orig.  ‘being  half-way  up the  height  of  a  mountain’),  occa,  ‘a  harrow’, OSlav.  ostru,  Lith.  aitrus  (for  *okro,  with  in¬ serted  /),  ‘sharp’,  Mir.  ochar,  W.  ochr,  ochyr, ‘edge,  corner,  border’.  Cp.  awn,  eager,  ear  of corn,  edge,  egg,  ‘to  urge’,  hammer.  Cp.  also Acaena,  acantha,  acanthion,  acantho-,  Accipi- ter,  acerb,  acescent,  acetum,  acid,  Acipenser, acme,  acne,  Acocanthera,  acor,  Acreinae,  acri¬ mony,  aero-,  acroama,  acrobat,  acropolis,  Ac¬
1503:acrisia,  n.,  condition  of  disease  with  no  symp¬ toms  to  establish  the  diagnosis.  —  Gk.  axptaloi, ‘want  of  judgment’,  fr.  axpixop,  ‘not  judged’, fr.  4-  (see  priv.  pref.  a-)  and  xpixop,  ‘separated, chosen,  decided,  judged’,  verbal  adj.  of  xpfveiv, ‘to  separate,  choose,  decide,  judge’.  See  critic, acritical,  adj.  —  Formed  with  adj.  suff.  -al  fr. Gk.  icxpiTop,  ‘not  judged’.  See  prec.  word, aero-,  acr-,  combining  form  meaning  ‘pertaining to  the  end,  extreme’.  — ■  Gk.  4xpo-,  fr.  dtxpop, ‘at  the  end,  at  the  top,  outermost’,  fr.  4x4), ‘edge’ ;  cogn.  with  L.  acer,  ‘sharp’,  OSlav.  ostru, Lith.  aStrus,  of  s.m.,  OIr.  er,  ‘high’.  See  acrid and  cp.  words  there  referred  to. acroama,  n.,  oral  teaching;  esoteric  teaching.  — L.,  fr.  Gk.  4xp6ajj.a,  lit.  ‘that  which  is  heard (with  pleasure)’,  fr.  4xpo4opxi,  ‘I  hear’,  orig. ‘I  have  a  sharp  hearing',  fr.  *4xp-ouct4,  ‘a  sharp hearing’,  compounded  of  Sxpop,  ‘pointed, sharp’,  and  Ion.,  Att.  oop,  gen.  ouaxop,  cor¬ responding  to  Gk.  o5p,  gen.  <8x6?,  ‘ear’.  For the  first  element  see  acrid  and  cp.  acropolis.  For the  second  element  see  ear,  ‘the  organ  of  hear¬ ing’,  and  cp.  oto-.  For  the  ending  see  suff.  -ma. acroama  tic,  adj.,  oral;  esoteric.  —  Gk.  4xpoa- (j.axix6p,  ‘pertaining  to  hearing’,  fr.  4xpoapa, ‘that  which  is  heard’.  See  prec.  word  and  -atic. Derivative:  acroamatic-s,  n. acrobat,  n.  —  F.  acrobate,  fr.  Gk.  4xpo(3axop, ‘walking  on  tiptoe’,  fr.  Sxpop,  ‘at  the  end,  outer¬ most,  highest’,  and  pax-,  ‘going’,  from  the  stem of  Patvav,  ‘to  go,  walk’.  (Cp.  (foxfip,  ‘passable’, verbal  adj.  of  (JatvEiv.)  For  the  first  element see  aero-,  for  the  second  see  base,  n.,  and  cp. the  second  element  in  aerobatics.
1504:Derivatives:  acrobat-ic,  adj.,  acrobat-ic-al-ly , adv.,  acrobat-ics,  n.,  acrobat-ism.  n. acrocarpous,  adj.,  bearing  fruit  at  the  end  of  the stalk  ( bot .)  —  Gk.  4xp6xap7rop,  ‘bearing  fruit at  the  top’,  compounded  of  Sxpop,  ‘at  the  end, outermost,  highest’,  and  xaprrfip,  ‘fruit’.  See aero-  and  carpel.  For  E.  -ous,  as  equivalent  to Gk.  -op,  see  -ous.
1625:adiabatic,  adj.,  impassable.  —  Formed  with  suff. ic-  fr.  Gk.  iSiipaTOi;,  ‘not  to  be  passed’,  fr. x-  (see  priv.  pref.  a-)  and  SiafSxToi;,  ‘to  be passed’,  verbal  adj.  of  8ia^xivEi.v,  ‘to  step across,  step  over’,  fr.  Six  (see  dia-)  and flodveiv.  ‘to  go,  to  pass’.  See  base,  n.,  and  cp. diabetes.
1806:aerobatics,  n.,  acrobatic  tricks  performed  with aircraft.  —  Coined  on  analogy  of  acrobatics  fr. aero-  and  the  stem  of  [JxEveiv,  ‘to  go’.  See  acro¬ bat  and  cp.  words  there  referred  to.  For  the  end¬ ing  see  suff.  -ics.
```


## [2026-09-06T02:23:00.016Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T02:23:00.023Z] TOOL RESULT

```


```


## [2026-09-06T02:23:06.087Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nfor pat in [r'\\ndiabetes,',r'\\nbase,\\s+n\\.',r'\\nbasin,',r'\\nbass\\b',r'\\nabyss,',r'\\nbyssus',r'\\nbasis,']:\n    m=re.search(pat,t)\n    print('=====',pat, m.start() if m else None)\n    if m: print(t[m.start():m.start()+1400].replace('\\n',' ')[:1400])\nEOF"
}
```


### [2026-09-06T02:23:07.673Z] TOOL RESULT

```
===== \ndiabetes, None
===== \nbase,\s+n\. 963104
 base,  n.,  bottom;  foundation,  pedestal.  —  F.,  fr. L.  basis,  fr.  Gk.  (idci^,  ‘a  stepping,  step,  pede¬ stal,  foot,  base’,  from  the  stem  of  (3aivto,  ‘I  go’, which  prob.  stands  for  *(3avLCt>,  fr.  *P<x|z-io), fr.  l.-E.  base  *gwem-,  'to  go;  to  come’,  whence also  L.  venio  (prob.  for  *gwmio),  ‘I  come’,  Goth. qiman,  OE.  cuman,  ‘to  come’.  See  come  and  cp. venue,  ‘arrival’.  Cp.  also  basis,  abasia,  acrobat, aerobatics,  amphisbaena,  Anabaena,  anabas,  ana¬ basis,  -bates,  bathmism,  batophobia,  bema,  cata- basis,  diabase,  adiabatic,  diabetes,  ecbatic,  gyno- base,  hyperbaton,  metabasis,  Odobenus,  Ori- batidae,  parabasis,  presby-,  stereobate,  stylobate. As  a  term  of  chemistry  base  was  introduced  by the  French  chemist  Guillaume-Fran^ois  Rou- elle  (1703-70)  in  1 754- Derivatives  ;  base,  tr.  v.,  to  form  a  base  for; intr.  v.,  to  be  based  (on  or  upon  something); base-ment,  n. base,  adj.  —  ME.  bas ,  fr.  OF  (=  F.)  bas,  ‘low’, fr.  Late  L.  bassus,  ‘thick  fat,  stumpy’  (in  classical L.  occurring  only  as  a  cognomen);  of  un¬ certain  origin.  Cp.  abase,  bass  (music),  basset, basso,  bassoon,  debase. Derivatives:  base-ly,  adv.,  base-ness,  n. bash,  tr.  v.,  to  strike  violently.  —  Of  imitative origin.  Cp.  Swed.  basa,  Dan.  baske,  ‘to  strike’, bashaw, 
===== \nbasin, None
===== \nbass\b 968948
 bass,  adj.  and  n.  ( mus .)  —  It.  basso,  fr.  Late  L. bassus,  ‘low’.  See  base,  adj.,  and  cp.  bassoon and  the  second  element  in  contrabass. bassanite,  n.,  an  anhydrous  calcium  sulfate  (min¬ eral.)  —  Named  after  F.  Bctssani,  professor  of geology  in  Naples.  For  the  ending  see  subst. suff.  -ite. bassarid,  n.,  a  maenad  ( Greek  mythol.)  —  Gk. pacraapl?,  gen.  -iSa?,  fr.  pacraxpx,  ‘fox’,  a  word of  unknown  etymology;  so  called  because  their dresses  were  made  of  foxskins. basset,  n.,  a  variety  of  small  hound.  —  F.,  formed with  dimin.  suff.  -et  fr.  bas,  ‘low’.  See  base,  adj. bassetite,  n.,  a  phosphate  of  calcium  and  uranium (mineral.)  —  Named  after  the  Basset  mines  in Cornwall. bassinet,  n.,  cradle.  —  Usually  derived  fr.  F.  bas¬ sinet,  ‘a  little  basin’,  dim.  of  bassin,  fr.  OF.  bacin (see  basin).  This  derivation,  however,  does  not account  for  the  sense  of  the  English  word.  Ac¬ cording  to  my  opinion,  E.  bassinet  is  a  blend  of F.  barcelonnette ,  ‘a  little  cradle’  (a  collateral form  of  bercelonnette,  fr.  bercer ,  ‘to  rock’),  and F.  bassinet,  ‘a  little  basin’, basso,  n.,  a  bass  voice.  —  It.  See  bass  (nuts.). bassoon,  n.,  a  woodwind  instrument.  —  F.  bas¬ so  n,  fr.  It.  bassone,  fr.  basso.  See  bass  (mus.) and  -oon. bas
===== \nabyss, None
===== \nbyssus 1351915
 byssus,  n.  —  L.,  fr.  Gk.  puaeog,  ‘fine  white  linen’, a  Semitic  loan  word.  Cp.  Heb.  biitz,  of  s.m.,  fr. Sem.  *b-w-f  {*b-w-tz),  ‘to  be  white,  to  surpass in  whiteness’,  whence  Heb.  betzdh,  Arab,  bayda1', ‘egg’.  Cp.  W.  Muss-Amolt,  Semitic  words  in Greek  and  Latin,  in  Transactions  of  the  Ameri¬ can  Philol.  Association,  23,  80,  Note  19. Derivatives:  byss-al,  adj.,  byss-in,  n.,  byssine (Q.v.) Byzantine,  adj.,  pertaining  to  Byzantium.  —  L. Byzantinus,  fr.  Byzantium,  name  of  the  capital of  the  Eastern  Roman  Empire.  Cp.  bezant.  For the  ending  see  suff.  -ine  (representing  L.  -inus). Derivative:  Byzantin-ism,  n. 217 cacology I ia cab,  n.,  a  Hebrew  dry  measure.  ■ —  Heb.  qabh. rel.  to  Aram.-Syr.  qabba,  Arab,  qabb,  name  of  a measure  of  capacity,  from  the  Sem.  base  *q-b-b, 'to  be  hollow’. cab,  n.,  carriage.  —  Abbreviation  of  cabriolet. Derivative :  cab,  intr.  v. cab,  tr.  v.,  to  crib  (slang).  —  Short  for  cabbage, ‘to  pilfer’. cabal,  n.,  a  secret  intrigue.  —  F.  cabale ,  fr.  Late L.  cabbala,  fr.  Mishnaic  Heb.  qabbaldh,  'recep¬ tion;  doctrine  received’,  fr.  Heb.  qibbel,  ‘he  re¬ ceived,  accepted’,  rel.  to  Aram.  qebhel,  q'bhe'l, ‘before’,  Syr.  men  qlbhdl,  ‘opposite’,  Aram.- Syr.  qabbel,  ‘he  received,  accepted’,  Arab,  qdbila, ‘was  in  
===== \nbasis, None
```


## [2026-09-06T02:23:15.513Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nfor pat in [r'abyss,\\s+n',r'basin,\\s+n',r'diabetes',r'\\bbasis,\\s+n',r'venue,\\s+n']:\n    for m in list(re.finditer(pat,t))[:2]:\n        print('=====',pat,m.start())\n        print(t[m.start():m.start()+900].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T02:23:17.661Z] TOOL RESULT

```
===== abyss,\s+n 87830
abyss,  n.  —  L.  abyssus,  ‘bottomless  pit’,  fr.  Gk &(Juccroc;  (scil.  Aluvt]),  ‘bottomless,  unfath¬ omed  (pool)’,  fr.  a-  (see  priv.  pref.  a-)  and (3uaa6?,  ‘depth,  bottom’,  which  is  related  to (Julios,  of  s.m.  Cp.  abysm. Derivative:  abyss-al,  adj. Abyssinia,  n.  —  ModL.  Abyssinia,  Latinized  form of  Arab.  lidbashah,  ‘Abyssinia’.  Cp.  bubshi. Derivatives:  Abyssini-an,  adj.  and  n. ac-,  assimilated  form  of  ad-  before  c  and  q. -ac,  suff.,  corresponding  in  meaning  to  suff.  -ic. —  Fr.  F.  -aque,  or  directly  fr.  L.  -acus,  fr.  Gk. -axo ?. acacia,  n.  —  L.  acacia,  fr.  Gk.  axaxia,  shittah tree’,  which,  like  axaxaXl s,  ‘gall  of  the  Oriental tamarisk’,  is  of  foreign,  prob.  Egyptian  origin. Both  axaxia  and  axaxaXii;  were  prob.  influenced in  form  by  oixavfta,  ‘thorn,  prickle’,  and  other Greek  derivatives 
===== basin,\s+n 967326
basin,  n.  — ■  ME.,  fr.  OF.  bacin,  bassin  (F.  bassin), fr.  VL.  *baccinum,  fr.  bacchinon  (cited  by  Gre¬ gory  of  Tours  as  a  vulgar  word),  fr.  *bacca, ‘a  water  vessel’  (whence  F.  bac,  ‘vat’).  See back,  ‘vat’,  and  cp.  next  word, basinet,  n.,  a  light  steel  helmet,  later  made  with a  visor.  —  ME.,  fr.  OF.  baciner,  bassinet  (F.  bas¬ sinet),  dimin.  of  bacin,  bassin  (F.  bassin ),  ‘basin’. See  prec.  word  and  -et,  and  cp.  bassinet, basis,  n.  —  L.,  fr.  Gk.  pa  at?.  See  base,  n. bask,  intr.  and  tr.  v.  —  ME.  basken,  fr.  ON.  bada- sk,  a  reflexive  verb  lit.  meaning  ‘to  bathe  one¬ self’,  fr.  bada,  ‘to  bathe’  (see  bathe),  and  reflex, suff.  -sk. basket,  n.  —  ME.,  fr.  L.  bascauda,  ‘a  brazen  ves¬ sel’,  referred  to  by  the  Roman  poet  Martial  as  an OBrit.  word;  cogn.  with  L .  fascis,  ‘bun
===== diabetes 185624
diabetes. Adiantum,  n.,  a  genus  of  plants,  the  maidenhair fern  (bat.)  —  L.,  fr.  Gk.  aSiavrov,  ‘maiden¬ hair’,  lit.  ‘unwetted’,  fr.  a-  (see  priv.  pref.  a-) and  Suxivciv  (for  *8tfavietv),  ‘to  wet,  mois¬ ten’,  which  is  prob.  rel.  to  Seueiv,  ‘to  wet, moisten’. adiaphoretic,  adj.,  preventing  perspiration  (med.) —  Gk.  ocSiatpopYjTiao?,  ‘not  promoting  perspi¬ ration’.  See  priv.  pref.  a-  and  diaphoretic. Derivative:  adiaphoretic,  n.,  an  adiaphoretic agent. adiaphoresis,  n.,  absence  of  perspiration  (med.)  — Medical  L.  See  priv.  pref.  a-  and  diaphoresis, adiaphoron,  n.  (pi.  adiaphora),  a  thing  indifferent from  the  ecclesiastical  point  of  view.  —  Gk. aStaipopov,  neut.  of  aSidhpopo?,  ‘indifferent’.  See next  word. adiaphorous,  adj.,  indifferent.  —  Gk.  aSttxcpopoi;, ‘not  different,  indifferent’,  fr.  a-  (se
===== diabetes 963700
diabetes,  ecbatic,  gyno- base,  hyperbaton,  metabasis,  Odobenus,  Ori- batidae,  parabasis,  presby-,  stereobate,  stylobate. As  a  term  of  chemistry  base  was  introduced  by the  French  chemist  Guillaume-Fran^ois  Rou- elle  (1703-70)  in  1 754- Derivatives  ;  base,  tr.  v.,  to  form  a  base  for; intr.  v.,  to  be  based  (on  or  upon  something); base-ment,  n. base,  adj.  —  ME.  bas ,  fr.  OF  (=  F.)  bas,  ‘low’, fr.  Late  L.  bassus,  ‘thick  fat,  stumpy’  (in  classical L.  occurring  only  as  a  cognomen);  of  un¬ certain  origin.  Cp.  abase,  bass  (music),  basset, basso,  bassoon,  debase. Derivatives:  base-ly,  adv.,  base-ness,  n. bash,  tr.  v.,  to  strike  violently.  —  Of  imitative origin.  Cp.  Swed.  basa,  Dan.  baske,  ‘to  strike’, bashaw,  n.  —  A  variant  of  pasha  (q.v.) bashful,  adj.  —  Aphetic  for  abash-ful.  See  abash an
===== \bbasis,\s+n 967816
basis,  n.  —  L.,  fr.  Gk.  pa  at?.  See  base,  n. bask,  intr.  and  tr.  v.  —  ME.  basken,  fr.  ON.  bada- sk,  a  reflexive  verb  lit.  meaning  ‘to  bathe  one¬ self’,  fr.  bada,  ‘to  bathe’  (see  bathe),  and  reflex, suff.  -sk. basket,  n.  —  ME.,  fr.  L.  bascauda,  ‘a  brazen  ves¬ sel’,  referred  to  by  the  Roman  poet  Martial  as  an OBrit.  word;  cogn.  with  L .  fascis,  ‘bundle,  fag¬ got’  ;  see  fasces.  The  orig.  meaning  of  bascauda was  prob.  ‘wicker  basket’, bason,  n.  —  A  variant  of  basin. 152  f  153 Basque,  n.  and  adj.  —  F.,  fr.  Sp.  vasco,  adj.,  fr. vasedn,  n.,  fr.  L.  Vascones,  name  of  the  ancient inhabitants  of  the  Pyrenees.  According  to  Wil¬ helm  von  Humboldt,  the  name  Vascdnes  orig. meant  ‘Foresters’.  Cp.  Gascon, bas-relief,  n.,  low  relief.  —  F.,  fr.  bas,  ‘low’,  and relief,  ‘raised  work’, 
===== venue,\s+n 857433
venue,  n. —  F.,  prop.  fern.  pp.  of  avenir,  ‘to  come to’,  fr.  L.  advenire,  fr.  ad-  and  venire,  ‘to  come’. See  venue,  ‘arrival’,  and  cp.  advene,  advent, aver,  tr.  v.  —  F.  averer,  fr.  OF.  averer,  fr.  a,  ‘to’ (see  4),  and  voire,  ‘true’,  fr.  L.  verus,  ‘true’.  Cp. OProven?.  averer,  aveirar.  It.  averare,  and  see very. average,  n.,  1)  loss  incurred  by  damage  at  sea; 2)  an  equitable  division  of  such  loss  among  all the  parties  interested;  3)  an  arithmetical  mean. —  F.  avarie,  ‘damage  to  ship’,  fr.  It.  avaria, fr.  Sp.  averia,  fr.  Arab.  ‘ awdrfva ",  ‘merchandise damaged  by  sea  water’,  fr.  ‘ awdr ,  Tent,  tear; flaw;  damaged  goods’. Derivatives:  average,  adj.  and  tr.  v. average,  n.,  feudal  service  ( Old  English  law)  — ME.,  fr.  ML.  averagium,  fr.  ML.  avera,  fr.  OF. oevre,  ovre  (F.  oeuvr
===== venue,\s+n 8190506
venue,  n.  —  ME.,  fr.  MF.  revenue ,  prop.  fem. of  revenu  (whence  F.  revenu,  ‘revenue’),  pp.  of revenir,  ‘to  come  back,  return’.  See  revenant. reverberant,  adj.,  reverberating.  —  L.  reverberdns, gen.  -antis,  pres.  part,  of  reverberate.  See  next word  and  -ant. reverberate,  tr,  v.,  to  throw  back;  to  cause  to  re¬ echo  ;  intr.  v.,  to  re-echo.  —  L.  reverberatus,  pp. of  reverberate,  ‘to  strike  back,  repel,  cause  to rebound',  fr.  re-  and  verberare,  'to  beat’,  fr.  ver- bera  (pi.)  ‘rods,  lashes,  strokes’,  which  is  rel.  to L.  verbena,  usually  pi.  verhenae,  ‘leaves  and branches  of  laurel’.  See  vervain  and  verbal  suff. -ate. Derivatives:  reverberat-ing,  adj.,  reverberation (q.v.),  reverberat-ive,  adj.,  reverberat-or,  n.,  re- verberat-ory,  adj. reverberation,  n.  —  ME.  reverberacioun,  fr.  MF. (=  F.)
```


## [2026-09-06T02:23:31.070Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7emt",
 "prompt": "What is the reconstructed PIE root for 'to come/go' (gʷem-)? Give its form, meaning, and listed descendants (Avestan, Old Persian, Greek bainō, Latin veniō, Gothic qiman, Lithuanian gimti, Old Prussian)."
}
```


## [2026-09-06T02:23:32.955Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A8%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full etymology of Persian جنبیدن (jonbidan): Middle Persian form, Proto-Iranian reconstruction, cited authorities (Cheung, Hasandust, MacKenzie), and any PIE root mentioned."
}
```


### [2026-09-06T02:23:32.978Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:23:39.363Z] TOOL RESULT

```
# Etymology of Persian جنبیدن (jonbidan)

**Middle Persian:** The entry indicates the form comes from Middle Persian, though it notes "Book Pahlavi needed" for the script representation: ywmb-ytn' /⁠jumbīdan⁠/

**Proto-Iranian:** The reconstruction given is *Hyámbdi* ("to move around")

**Proto-Indo-European:** The ultimate root is *h₃yebʰ-* ("to enter into")

**Cited Authority:** The only explicit scholarly source referenced is Cheung's 2007 work: "Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill"

The entry does not cite Hasandust or MacKenzie as authorities on this particular word's etymology. The entry's etymological chain shows a semantic evolution from the PIE notion of "entering into" through the Proto-Iranian sense of "moving around" to the modern Persian meanings of shaking, vibrating, or fidgeting.
```


## [2026-09-06T02:23:46.552Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7emh%E2%82%81-",
 "prompt": "Give the root's form, meaning, and its listed descendants: Proto-Indo-Iranian/Avestan, Greek βαίνω, Latin veniō, Proto-Germanic *kwemaną, Balto-Slavic (Lithuanian gimti, Old Prussian). Quote the Old Prussian forms if listed."
}
```


## [2026-09-06T02:23:46.972Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/base",
 "prompt": "Give the etymologies of base (n.), base (adj.), and basin as Etymonline gives them, including the PIE roots cited."
}
```


### [2026-09-06T02:23:48.571Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:24:12.946Z] TOOL RESULT

```
# Etymology Summary

**Base (n.):** From Old French *bas* "depth" (12c.), from Latin *basis* "foundation," from Greek *basis* "a stepping, a step, that on which one steps or stands, pedestal," from *bainein* "to go, walk, step" (from PIE root *\*gwa-* "to go, come").

**Base (adj.):** From late 14c. Old French *bas* "low, lowly, mean," from Late Latin *bassus* "thick, stumpy, low," of uncertain origin, possibly from Oscan, Celtic, or related to Greek *basson*, comparative of *bathys* "deep."

**Basin:** The webpage content provided does not include an etymology entry for "basin." Only the etymologies for base (n.), base (adj.), and base (v.) are presented.
```


## [2026-09-06T02:24:19.064Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7em-",
 "prompt": "Give the root's form and meaning and list the descendants by branch (Indo-Iranian/Avestan/Old Persian, Hellenic βαίνω, Latin veniō, Germanic *kwemaną, Baltic: Lithuanian gimti, Old Prussian forms)."
}
```


## [2026-09-06T02:24:19.567Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/basin",
 "prompt": "Give the etymology of basin, and of bassinet if present."
}
```


### [2026-09-06T02:24:24.687Z] TOOL RESULT

```
# Proto-Indo-European Root *gʷem-

## Root Form and Meaning

The reconstructed root is **\*gʷem-** (perfective aspect), meaning "to come" or "to step."

## Key Descendants by Branch

**Indo-Iranian:**
- Sanskrit: गम् (gam) and गामयति (gāmáyati, "to cause to go")

**Hellenic:**
- The page does not list Greek descendants for this particular root

**Italic:**
- Not explicitly listed on this page

**Germanic:**
- Not detailed in the provided content

**Baltic:**
- Lithuanian: giminė̃ ("family, kin; genus; gender")
- Lithuanian: gỹmis ("birth; nature; face")

**Other branches:**
- Albanian: gati
- Armenian: եկ (ek)
- Tocharian A and B: kum-, käm-

The etymology suggests this root may relate to **\*gʷeh₂-**, with similar gradation patterns seen in comparable root pairs.
```


### [2026-09-06T02:24:26.815Z] TOOL RESULT

```
# Etymology of Basin and Bassinet

**Basin:**
The word "basin" dates to around 1200, deriving from Old French *bacin* (Modern French *bassin*), which came from Vulgar Latin *baccinum*. The ultimate origin is uncertain, though it may trace to *bacca* meaning "water vessel," possibly from Gaulish origins. The geological sense referring to "a tract of country drained by one river" emerged in 1830.

**Bassinet:**
This term, meaning "wicker cradle," entered English in 1854 from French *bassinet*, a diminutive of *bassin* (which itself derives from basin). As one source notes, "the English word is from French *bercelonette*, double diminutive of *berceau* 'cradle,' altered by *bassin* 'basin.'" Notably, Middle English had an earlier *bacinet* around 1300 referring to "a hemispherical helmet."

Both words share a common linguistic ancestry through Romance language developments of the same Latin-rooted stem.
```


## [2026-09-06T02:24:31.821Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gemton",
 "prompt": "Is gemton an Old Prussian word? Give its language, meaning and etymology."
}
```


## [2026-09-06T02:24:32.574Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/diabetes",
 "prompt": "Give the etymology of diabetes: Greek diabetes, diabainein, dia- + bainein, date of English attestation, and any medical-sense history."
}
```


### [2026-09-06T02:24:33.608Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:24:38.690Z] TOOL RESULT

```
# Etymology of Diabetes

**Greek Origins:**
The word comes from late Greek *diabetes*, literally meaning "a passer-through, siphon." It was named by Aretaeus the Cappadocian, a 2nd-century Alexandrian physician.

**Word Components:**
The term breaks down into two Greek elements: *dia-* ("through") combined with *bainein* ("to go, walk, step"). Both trace back to Proto-Indo-European roots.

**English Attestation:**
The medical term entered English in the 1560s, initially describing "a set of affections characterized by abnormal discharge of urine."

**Medical History:**
The condition was colloquially known in older English as "pissing evil." Today it's typically restricted to *diabetes mellitus*, characterized by excessive sugar in urine. Interestingly, in classical Greek, *diabetes* also referred to "a drafting compass," based on the geometric position of the legs.
```


## [2026-09-06T02:24:46.862Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; echo \"=== search gemton ===\"; grep -n \"gemton\\|gimsenin\\|gemmons\" WLD_Bd1_pages.txt | head; echo \"=== search gwem ===\"; grep -n \"gemton\\|gimsenin\" WLD_Bd1_1930_dli_70244_djvu.txt | head"
}
```


### [2026-09-06T02:24:46.944Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
=== search gemton ===
64055:burt"    = apr. gimsenin aec. sg. ,,Geburt", apr. gemton „gebaren", gcmmons
=== search gwem ===
42631:burt" = apr. gimsenin aec. sg. ,,Geburt", apr. gemton „gebaren", gcmmons
```


## [2026-09-06T02:24:47.052Z] TOOL CALL #44: WebSearch

```json
{
 "query": "Old Prussian \"gemton\" \"gimsenin\" \"gemmons\" born birth Prussian Enchiridion"
}
```


### [2026-09-06T02:25:29.589Z] TOOL RESULT

```
Web search results for query: "Old Prussian "gemton" "gimsenin" "gemmons" born birth Prussian Enchiridion"

Links: [{"title":"Indo-European etymology : List with all references","url":"https://starlingdb.org/cgi-bin/etymology.cgi?single=1&basename=%2Fdata%2Fie%2Fpiet&text_number=1753&root=config"},{"title":"(PDF) \"Case system and translation strategy in the Old Prussian Enchiridion\"","url":"https://www.researchgate.net/publication/278810544_Case_system_and_translation_strategy_in_the_Old_Prussian_Enchiridion"},{"title":"The Phonemes of the Old Prussian Enchiridion","url":"https://www.tandfonline.com/doi/pdf/10.1080/00437956.1964.11659820"},{"title":"Prussian Enchiridion - Frederik Kortlandt","url":"https://www.kortlandt.nl/editions/ench.html"},{"title":"Old Prussians","url":"https://en.wikipedia.org/wiki/Old_Prussians"},{"title":"Enchiridion","url":"https://en.wikipedia.org/wiki/Enchiridion"},{"title":"(PDF) Prussica","url":"https://www.academia.edu/29434230/Prussica"}]

Based on the search results, I found information about these Old Prussian words:

Old Prussian "gemton" means 'to give birth' (gebären), "gimsenin" means 'birth' (Geburt), and "gemmons" means 'born' (geboren).

These words appear in linguistic and etymological databases documenting Old Prussian vocabulary. The Enchiridion (1561) is the longest document in Old Prussian and is a translation of Martin Luther's Enchiridion by a German cleric named Abel Will, who was assisted by a Prussian informant, Paul Megott.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T02:25:39.608Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk 'NR>=64040 && NR<=64060' WLD_Bd1_pages.txt; echo \"--- page tag ---\"; awk 'NR<=64055 && /\\[pdf page/ {p=$0} END{}' WLD_Bd1_pages.txt; grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | awk -F: '$1<64055' | tail -2"
}
```


### [2026-09-06T02:25:41.292Z] TOOL RESULT

```
vermogen eine solche nicht zu sichern.
    Mir. beitn „Schritt“ (Fick II 4 160)                         =
                                              beinm ,,Schlag", s. Bd. II S. 137.
    Unter Annahme einer Bed.-Entwieklung „(zur Welt) kommen"                 „ge-                    =
boren werden" reiht Bechtel Sinnl. Wahrn. 87, Endzelin KZ. 44, 61,
sowie Miihlenbach - Endzelin Lett.-D. Wb. I 550 auch folgende, haupt-
sachlich bait. Sippe an: lit. gcmii , gimti „geboren werden = lett. dzemu
dz'tmt ds., lit. ghnstu (zum Akzent siehe Schulze KZ. 45, 230) = lett.
dz'imstu ds., lit. gimme ..Familie", gfjmis „Geburt“, gdmas „Angebornes“,
ganvmti     Kinder erzeugen, Yieh ziichten" lett. dz'tmts ,.angeboren, erb-
                 ,;


gehorig, leibeigen", dzimums „Geschlecht, Nachkommenschaft", dz'imsa „ Ge-
burt"    = apr. gimsenin aec. sg. ,,Geburt", apr. gemton „gebaren", gcmmons
ppa. „geboren“; dazu nach Endzelin aaO. alb pregim „Gastmahl bei der      .


Geburt eines Erstgeborenen" (wenn urverwandt) und nach Bartholomae
Airan. Wb. 1081 av. nijamayeinti, wenn „sie bringen zum Gebaren" (von
--- page tag ---
```


## [2026-09-06T02:25:41.701Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT gaiti ===\"; grep -n \"gaiti\" BRT.txt | head -8; echo \"=== BRT gāθa/gatha ===\"; grep -n \"vīgāθ\\|vi-gāθ\\|gāθō\\|gāϑ\" BRT.txt | head -8; echo \"=== SKT base/abyss ===\"; grep -n -i \"^base\\|^abyss\\|Base, a foundation\\|Abyss\" SKT.txt | head -8"
}
```


### [2026-09-06T02:25:41.795Z] TOOL RESULT

```
=== BRT gaiti ===
3782:•  j.  aiwLgatay-  f.  'Herzukommen',  sva. 'Eintreten,  Beginnen':  pas:a  hamS  'gaitim .  .  pasca  z»m3  .  .  'gaitim  V.(j.6;  —  l^ma- tiham  vä  *°gats  (LS.)  '*  "bei  Einbruch  der Dunkelheit"  V.Ä4.
10344:np,  gäm,  gr.  jSffin.  —  ')  Hds.  gaitia'.  —  >)  Pü. :
11626:g,  pnghaüiä  Y.  31.  14 ;  s.  gaiti;  Sp.  493
13839:•  j.  duigainti'tara- Adj.  'der  stinkendere': välö  ..  dusgaititis  'rS  anyaHbyB  vätalibyS H.2.2S.
18884:Vd,/}";  —  ya^qmca  pars  mafyaia  ahoi- ta^a^a{&A.)..gaitinqm  'mqm{AS.)  däian Yt  IQ.  6;  —  yä  vs  vamtkU  (nämL  äp5) ahurS  mazdä  *°mqm'^  dadäi  .  .  täii  vi yazamaiäl  Y.  ^JÄ  4;  —  tq  yazsi  ifaii •w»ir/(IPO  pairicä  jasüi  (sd.)  vanta  Y. 57,22;  —  hyat  vä  töi  'manqtn  vözObm atan  . .  tä  äjoj  pairijasumaidi  Y.  j6'.  3;
=== BRT gāθa/gatha ===
=== SKT base/abyss ===
287:Abyss,  a  bottomless  ^If.   (L.  *  ( Milton.   L.  a^jjMj.^Gk.  d^mraot,  botf less.  —  Gk,  d-,  short  for  d*--,  neg.  pi $vaa6s,  depth,  akin  to  Bathos. (9\  Un-  (I).
5640:Base.  (F.)  M.  E  wr-O.  F.  aiu,  ease. Cf.  llal.  agiCf  Port,  azo,  case.  Grig,  vin- known.
15618:Base,  Base,  to  Krapc,  %Sbuoe^  (] M.  E.  roxeny  Co  scrape.  — K,  raurr.w rasitre,  to  gnue,  to  demolish,  *!.* supine  of  radtrt,   to  scrape. BodsDt.
18357:base  STAND. +  1*  ji/are\  Gk.  iflr^v,*  1 vtowl,  Kuss-  stoiaU,  Ski.  jy^J,  lo  slund. (^STA.)  For  allied  words,  sec  btalo. Der.  ftami,  >b. ;  sfiinilis/t,  put  foi  s/unU- dish,  a  standing  dish  for  pen  and  ink.
21929:A-  (9),  in  abyss.  (Gk.)    See  An-  faV
```


## [2026-09-06T02:25:56.773Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT nijamay ===\"; grep -n \"nijamay\\|nijamai\\|jamayeinti\" BRT.txt | head -5; echo \"=== BRT vigatha variants ===\"; grep -n \"vlgä\\|vigä\\|vi\\.gä\\|ffägö\\|gä&ö\" BRT.txt | head -10; echo \"=== col near 3782 ===\"; awk 'NR<3790 && /Sp\\. *[0-9]/ {l=NR\": \"$0} END{print l}' BRT.txt"
}
```


## [2026-09-06T02:25:57.809Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | awk -F: '$1<64055 {last=$0} END{print last}'; grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | awk -F: '$1>64055 {print; exit}'"
}
```


### [2026-09-06T02:25:58.349Z] TOOL RESULT

```
=== BRT nijamay ===
=== BRT vigatha variants ===
=== col near 3782 ===
2099: 3Vt:  Drei  Yasht  aus  dem  Zendavesta.     Stuttgart   1884. Gtr.j  Mäßkän  i  Yvisl  i  fryän.    (Vgl  Sp.  1299  o.) GGA.:  Göttingische  Gelehrte  Anzeigen. Ggs.:  WGeigek.
```


### [2026-09-06T02:25:59.926Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:26:08.057Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT Schlucht ===\"; grep -n \"Schlucht\" BRT.txt | head -10; echo \"=== WLD pages format ===\"; head -c 300 incoming/WLD/WLD_Bd1_pages.txt; echo; python3 -c \"\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf8',errors='replace').read().split(chr(10))\nprint(len(d))\nimport re\n# find nearest preceding standalone number line\nfor i in range(64054,64000,-1):\n    if re.fullmatch(r'\\s*\\d{1,4}\\s*', d[i]): print('num line',i,repr(d[i])); break\n\""
}
```


### [2026-09-06T02:26:09.606Z] TOOL RESULT

```
=== BRT Schlucht ===
23913:•  j.  va*wya-  .\dj.  'in  Beziehung  zur  ^T  f':  Y"  ■^''^'^'L^^^*'- "  ,X8'-  1  ^'^w „  ■"  ,  "  ,'  ,  ■'.,  ,„  .  .  ,.°  Adi.  'sich  eintaachend',  gr.  ^^i«  'Schlucht' Heerde  stehend,  zu  ihr  gehöng":  bttys  'ys      ,bgm.  Grdr.»  /.  606).  —  üvi.:  jud  gäh.
=== WLD pages format ===
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
                LIBRARY
ACCESSION NO. jj03?7
CALL No. gJ3 Wafjpok
                 f_
D.G.A. 79
                      ALOIS WALDE


VERGLEICHENDES WftRTERBDCH
                         
81975
```


## [2026-09-06T02:26:15.504Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23905,23920p' BRT.txt"
}
```


### [2026-09-06T02:26:15.567Z] TOOL RESULT

```
geringe  Stelle.
•  j,  VE^S'waesa-  m.  'Strauchdieb';  yasp %W3  . .  pa'iqm  fsd.)  jasaiti  'sB  Yt  13.  ao.
Komp.;  vq%-wa--^*isa-  'eig.  'den  Heerden  nach- stellend'; Btkl.  ZDMG.  4^.  303.
•  j.  vad^vö.dä-  Adj.  Ileerden  schenkend': mi^rym  ..  yS  'd,'r  '^1.10.6$.  •    J-    vi-kusra-    Adj.    'sich    auseinander
')  Vgl  Yt.  10.  28.  '  wölbend':  atn.vasarmn  (sd.) . .  'rfm  aoarät
•  j.  vadw5.rrä3ana-  Adj.  (fem  'nä-)  'die  ««»«J/  Aankusr^m  uparat  namät  V.  14. 7. Heerden    fördernd,    mehrend':    aridvm      P^- =  J^  ^''■'*-
süram  ..  'nam  Y.  6j.  i.  "  J-   vi-galK    f.   'Einsenkung,  Schluchf;
Pü.:  ramak  fräj^hotär.  "ä^  (AP.)   morfzat  kaofanqm   Yt/rf.  JI.
•  j.  va*wya-  .\dj.  'in  Beziehung  zur  ^T  f':  Y"  ■^''^'^'L^^^*'- "  ,X8'-  1  ^'^w „  ■"  ,  "  ,'  ,  ■'.,  ,„  .  .  ,.°  Adi.  'sich  eintaachend',  gr.  ^^i«  'Schlucht' Heerde  stehend,  zu  ihr  gehöng":  bttys  'ys      ,bgm.  Grdr.»  /.  606).  —  üvi.:  jud  gäh.
KompE.- Ableit  ««s  v^%'u,a..  -  Vü.-.  rama-   "  J-  vi-gi>r»ptay-  f  'Ergreifen,  Gefangen- m-,  s.  noch  No.  —  '>  So  nennt  sich  AhM.;   nähme,  -schafV;  nairyam  ham.varnUm  .  .
Pü.  er]. :  iuia  ramak  i  martumän  u  gdsfandän  ys   narqm   'ii](LS.yii  ianvS  baoxtänm   da-
vas  sui,  vam  in  »am  hat  an,  Zaiti    ",  .  die   den  Kriegern  auch   in  der
g.  vqs  V.  4s.  4:  s.  'van:  Gefangenschaft  einen  Retter  der  Person
•  i-.  g-  VI'',  j.,  p.  vi',  i.,%-vy',  v-'^iy  schast"  vr.7.3.
1)  Adv.  (nur  KompA);    i)  'auseinander'.      Zum  V.  grat-,  S  5J  n.  —  Pü.;  s  ham  grißär^
2)  'abseits,  getrennt  von—'.         3)  'cntge-      '*""-
```


## [2026-09-06T02:26:29.004Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B3%D9%86/",
 "prompt": "What do Dehkhoda (لغت‌نامه دهخدا) and Mo'in (فرهنگ معین) say about the Persian word باسن? Quote the definitions and any etymology or citations from classical poetry, and whether it is marked as a European/French loanword."
}
```


## [2026-09-06T02:26:31.182Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B2%CF%85%CF%83%CF%83%CF%8C%CF%82",
 "prompt": "Give the Ancient Greek βυσσός: meaning, etymology, relation to βαθύς/βυθός and to ἄβυσσος, and whether a PIE root *gʷādʰ- is cited."
}
```


### [2026-09-06T02:26:36.407Z] TOOL RESULT

```
# Ancient Greek βυσσός

Based on the Wiktionary content provided, here's what can be determined:

**Meaning:** The entry defines βυσσός as "alternative form of βυθός (bŭthós)" — though the specific meaning of βυθός itself is not detailed in this excerpt.

**Etymology:** The page does not provide etymological information.

**Relations:** The entry notes a variant relationship to βυθός, and references an alternative spelling βύσσος (with different accentuation). However, no information about ἄβυσσος (abyss) or connections between these terms appears in the provided content.

**PIE Root:** There is no mention of *gʷādʰ- or any Proto-Indo-European roots in this entry.

The references section cites scholarly lexicons (Liddell & Scott, Bailly, etc.), but the actual etymological and comparative material from those sources is not reproduced in this Wiktionary excerpt.
```


### [2026-09-06T02:26:36.693Z] TOOL RESULT

```
# Definitions from Persian Dictionaries

**Dehkhoda (لغت‌نامه دهخدا):**

The dictionary provides two entries. The first states: "بمعنی لگن خاصره. استخوان بندی لگن خاصره" (meaning the pelvic basin and its skeletal structure), and explicitly marks it as a French loanword. The second entry identifies it as a musical instrument—a woodwind flute-like device invented around 1480 in Padua, constructed typically from maple wood, with variants featuring different numbers of finger holes and keys.

**Mo'in (فرهنگ معین):**

This dictionary offers a more anatomical description: "برجستگی در پشت بدن بالاتر از ران و پایین تر از کمر" (a prominence on the back of the body, higher than the thigh and lower than the waist).

**Etymology Notes:**

Both sources mark the anatomical meaning as derived from French. Dehkhoda explicitly labels it as "( فرانسوی ، اِ )" indicating a European/French origin. The page contains user suggestions proposing a Turkish etymological connection to the verb "basmak" (to press), though this remains speculative.
```


## [2026-09-06T02:27:05.100Z] TOOL CALL #53: Bash

```json
{
 "command": "grep -o \"\\\"translit\\\": \\\"[a-zâîôû-]*îr[e]\\?\\\"\" data/extracted/batch/*.json | sort | uniq -c | sort -rn | head -20; echo \"=== how many Latin nodes use -îre ===\"; grep -o \"venîre\\|audîre\\|dicîre\" data/extracted/batch/*.json | sort | uniq -c | head"
}
```


### [2026-09-06T02:27:05.191Z] TOOL RESULT

```
      2 data/extracted/batch/page-553.json:"translit": "vazîr"
      2 data/extracted/batch/page-534.json:"translit": "asâtîr"
      2 data/extracted/batch/page-533.json:"translit": "vîr"
      2 data/extracted/batch/page-39.json:"translit": "asîr"
      2 data/extracted/batch/page-268.json:"translit": "qîr"
      2 data/extracted/batch/page-196.json:"translit": "tazvîr"
      1 data/extracted/batch/page-90.json:"translit": "ferîre"
      1 data/extracted/batch/page-74.json:"translit": "parîr"
      1 data/extracted/batch/page-552.json:"translit": "bahâ-gîr"
      1 data/extracted/batch/page-546.json:"translit": "op-erîre"
      1 data/extracted/batch/page-546.json:"translit": "ap-erîre"
      1 data/extracted/batch/page-525.json:"translit": "vâgîre"
      1 data/extracted/batch/page-51.json:"translit": "ambi-îre"
      1 data/extracted/batch/page-496.json:"translit": "tartîr"
      1 data/extracted/batch/page-478.json:"translit": "tîr"
      1 data/extracted/batch/page-473.json:"translit": "sîr"
      1 data/extracted/batch/page-440.json:"translit": "zîr"
      1 data/extracted/batch/page-439.json:"translit": "scîre"
      1 data/extracted/batch/page-405.json:"translit": "santîr"
      1 data/extracted/batch/page-390.json:"translit": "pîr"
=== how many Latin nodes use -îre ===
```


## [2026-09-06T02:27:07.528Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%DA%A9%D8%B1%D9%88%D8%A8%D8%A7%D8%AA/",
 "prompt": "What do Dehkhoda and Mo'in say about Persian آکروبات — meaning and stated language of origin (French?)? Quote briefly."
}
```


### [2026-09-06T02:27:10.520Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T02:27:27.617Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef show(f,pats,n=500):\n    t=open(f,encoding='utf8',errors='replace').read()\n    for p in pats:\n        m=re.search(p,t,re.I)\n        print('###',f,p,bool(m))\n        if m: print(re.sub(r'\\s+',' ',t[m.start():m.start()+n]))\nshow('SKT.txt',[r'Acrobat[.,]',r'Diabetes',r'Come[.,]\\s*\\(E',r'Avenue'])\nshow('FSD_vol1.txt',[r'ac.?ro.?bat\\b',r'a.?byss\\b'],400)\nEOF"
}
```


### [2026-09-06T02:27:29.712Z] TOOL RESULT

```
### SKT.txt Acrobat[.,] True
acrobat, a tnmbler. (Gk.; or F. — r-k.) F. Oitobatc. - Gk. ^pofiA-nft, lit. one who wnUs on tiptoe— Gk. atipo-tr, a point, neul. of dx-pot, pointed ; and Bar^s, verbal adj. of Baivfiv, to walk ; see Oomo. acropolis, a diadel. (Gk.) Lit. ' u^jper city J * Gk. Siepo-i, pointed, upper ; and viSAij, a city ; sec Police. acrostic, a short poem in which the initial letters spelt a word. (Gk.) Gk. dx^totfTiYiof.— >C*K.&po-f. pointed, also f
### SKT.txt Diabetes False
### SKT.txt Come[.,]\s*\(E True
Come. (E.) A. S. cumoM, pL t cam, pp. fum^w.-f Da. komen, led. >wwa, Dan. kommtt Sw. komma, Goth, kwiman^ G. kommen, L. utn irt f_gu^n ire*), Gk. 3air- f iv (p-amivcty*) ; ikt. ^'aw, to go, ^J, to go. (VGA.) become. (£.) A. S. btaiman, to arrive, hoppcn, turn out, bcfall.+Goth. bikxtnm- an\ cf. G. bt'p/iM, suitable, becoming. comely. (E) A. S. ryjw//r, comely. - A. S. eyf»u, suitable^ from cumam, to come ; and //r, like. Income, ga
### SKT.txt Avenue True
avenue. (P\ — L.) F. avenutt advenut, access; hence an apptonch lo a house (e&p. one shaded by tict-sl. — F. avenir, to come to.— L. ad, to; uenire, to come. contravene, to hinder. (L.) I.ow I.. tonirauenire, to oppose ; to break a law. — L. contra, against ; uenire, to come. convene, to as^iemble. (F. — L.) F. tonvenir, to assemble. — L. ron'Uenirt, to come tOiiclh(?r. oonvenlent, suitable. (F. — L.) From stem of X*. canueniens, sui
### FSD_vol1.txt ac.?ro.?bat\b True
ac'ro-bat, 1 ak'ro-bat; 2 &c'ro-b5t, n. 1. One xvho practises extraordinary gymuastic feats, ns ropo-danc- mg, lofty tumbling, and the like. 2. Figuratively, one who makes surprizing changes in his political or other attitudes and relations. 3. A phalanger (genus j4cro- bates), as the flying mouse (.4. pvfjmxus). Seo petau- rist. [< F. acro&afe, <
### FSD_vol1.txt a.?byss\b True
abyss, a-byme't. sojourn, to \ remain temporarily Itve.dicM ccMe, tc ibavc a A.bIm,e_,cch< ! a-bim'i-lek: 2 a-Wm'e-I5c. n. Bib. 1. permanent home. See endure, best. Ant., abandon, The name or tlt]e 0( Eevera, ppmstine kings. 2. King of avoid, depart, for/eltv : [orfe . tfm. S ! I.. Shecbem; son of Gideon. (Heb., father-klng.] proceed, reiect, re
```


## [2026-09-06T02:27:37.449Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gam-\\b\\|agmatā\\|jamiyā\\|jam-\" KNT.txt | head -12"
}
```


### [2026-09-06T02:27:37.490Z] TOOL RESULT

```
631:Before enclitics, a final nasal which would otherwise be written, is retained: (батса = gaibām-cã; zXagam-Sim, paruvam-ciy, adam-&im.
2408:pIE *g*em- in opt. Skt. gam-yat, OP a-jamiyat (cf. $101).
2547:I. Non-thematic stems have optatives with pIE 4&- in the sg. act., -i- in other forms. The ~é- suffix, which alone appears in extant OP, became -1;- after two consonants even in pIE; and in OP even 4é- was of necessity written -iyd- after any consonant except h (§25). Examples: 2d sg. b-1ya*; 3d sg. b-iya', d-jam-iyd', avd-jan-tya', perf. cazr- туй!
```


## [2026-09-06T02:27:39.348Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D8%A2%DA%A9%D8%B1%D9%88%D8%A8%D8%A7%D8%AA",
 "prompt": "What entries exist for آکروبات (Dehkhoda, Moin, Amid)? Quote the definition and stated origin language (French?)."
}
```


### [2026-09-06T02:27:44.992Z] TOOL RESULT

```
# Entries for آکروبات

Based on the page content, here are the dictionary entries found:

**Moin Dictionary:**
"بندباز، ورزشکاری که کارهایی مانند بندبازی ، ژیمناستیک و ... را انجام می دهد"
(Origin noted as French: رُ [فر.])

**Amid Dictionary:**
"ورزشکاری که حرکات موزون و دشوار از قبیل بندبازی، ژیمناستیک، و مانند آن‌ها انجام بدهد"

**Sereh Dictionary:**
"بندباز"

The Moin entry explicitly marks the origin as French [فر.], indicating this is a French loanword adopted into Persian.
```


## [2026-09-06T02:27:55.261Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef show(f,pats,n=600):\n    t=open(f,encoding='utf8',errors='replace').read()\n    for p in pats:\n        m=re.search(p,t)\n        print('###',f,p,bool(m))\n        if m: print(re.sub(r'\\s+',' ',t[m.start():m.start()+n]))\nshow('LEW_1910.txt',[r'\\nvenio',r'venio,\\s*-ire',r'abyssus'])\nshow('LAT.txt',[r'uenio',r'\\nvenio',r'abyssus'])\nEOF"
}
```


### [2026-09-06T02:27:56.890Z] TOOL RESULT

```
### LEW_1910.txt \nvenio False
### LEW_1910.txt venio,\s*-ire False
### LEW_1910.txt abyssus False
### LAT.txt uenio True
uenio/aduenio; amo/adamo "je m' 4 prends de"; adolesco "je grandis". Meme sens dans les adjectifs composds: uncus/aduncus; edo/adesus "entam 4 ". II exprime aussi 1'addition: do, addo; iungo, adiungo; d'ou provient sans doute le sens intensif signale par Aulu-Gelle 6,7,5 "quod ad prae- adagiS 14 uerbium tum ferine acueretur, cum significaret eTuxacHv quam intentionem nos dicimus, sicut "adfabre", et "admodum" et "adprobe" dicuntur. " Cf. aussi apprime, adaugeo, etc. Enfin il semble que ad serve k exprimer parfois un seus moyen; aais cette valeur est beaucoup moins nette; cf.Barbelenet, loc.lau
### LAT.txt \nvenio False
### LAT.txt abyssus True
abyssus, -I f.: = gr. a^uaaoc "abime". Nom atteste avant les Pferes de l'tigli se. A pass 4 par 1 'interm 4 diaire de l'6glise sons une forme sa- vante dans les l.rom. qni attestent egalement nn donblet popnlaire *abismus , cf.M.L.31 et 56; et en iri. abis, britt .affxoys. ac: v. atque, sons at. acaunumarga (aeauno-) , -ae f.: espbce de marne pierrense, Plin.17, 44. Mot celtique; cf. Acaunus nom de lien chez les Nantnates. Acca: terne dn langage enfantin designant la maman, cf.skr.ofefea, gr. ’A xxw "mater Cereris" . De m£me qne ce demi er, employ^ comme nom propre, et pass£ dans la legende, y
```


## [2026-09-06T02:28:05.808Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('LAT.txt',encoding='utf8',errors='replace').read()\nfor m in list(re.finditer(r'uenio,',t))[:3]:\n    print('###',m.start()); print(re.sub(r'\\s+',' ',t[m.start()-200:m.start()+700]))\ns=open('SYN.txt',encoding='utf8',errors='replace').read()\nfor p in [r'10\\.48\\s+COME',r'\\nCOME\\b']:\n    m=re.search(p,s)\n    print('### SYN',p,bool(m))\n    if m: print(re.sub(r'\\s+',' ',s[m.start():m.start()+700]))\nEOF"
}
```


## [2026-09-06T02:28:07.071Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D8%AF%DB%8C%D8%A7%D8%A8%D8%AA",
 "prompt": "What do Moin/Amid/Dehkhoda say about دیابت — meaning and stated origin language (French/Greek)? Quote briefly."
}
```


### [2026-09-06T02:28:07.405Z] TOOL RESULT

```
### 1183135
etre' mis en vente" (en face de perdo, uendo ). Alors, comme dans le cas de uideo, aspicio, la langue a recouru k d'autres verbea pour expriaer 1'id^e d^aller" dans les coaposes: cf. ingredior, internuenio, etc. abeo: s'en aller de; skr. apa-eti, gr. a 7 i-ek|ii>, got. afiddja. Souvent confondu avec habeo dans les ass., nalgr <5 les recoaaandations des granaairiens. Conposes double, poetique: transabeo. ( cf. transabigo). Derives: abitus,-us m., abitio (arch. et rare), Abeona, noa ou epi- thbte de deebs'e, cite par Tert. et St-Aug., a cote de Adeona, cf. Pom 5 na\ abitorium "latrina publica" (inscr.) adeo: aller vers, s'approcher, aborder; aditus,-us m., adit io,-onis (rare). ambio: v. ce aot. ant(e)eo: aller devant, depasser (sens propre et figur^).Scande toujours anteo, antire, l'e de ante est purement graphique, comme celui de de dans deesse. Un doublet ancien, ant ideo est dans Plaut
### 1832742
ei.Danielsson, 383 et s., a rapproche avec vraisemblance ignosc&de skr. anujHa "permettre". Ignosco renfer- merait un pr^verbe in- comparable au skr .anu-, que M. Leumann propose de voir aussi dans inuenio, inuideo. Que ignosco n'apparaissait pas aux Latins comme pouvant signifier "ignorer", ceci resuite d'un emploi comme celui qu 1 en fait S^nbque, Const.14,3 maiore animo non agnouit quam ignouisset. ignotus: v. n< 5 sc< 5 . Ilex, -icis f.: yeuse, chene vert. Depuis Ennius. Les langues romanes attestent aussi un doublet elex, sans dou*le d*origine dia- lectale, cf.M.L.4259, Einf.^, p.148. Derives: Iliceus , M.L. 4262, et celt.: irl.ilecde; ilicetum, M.L. 42615 ilicinus , cf. M.L.4263 *iliclna ; llignus, Iligneus. M. Cuny, IF 26,21, a suppose un mot "mediterraneen" qui se retrou- verait dans le second terme de gr. OM.yi.XbXjs, sorte de chene a glands coraestibles. Ilia, -ium n.pl.(declin
### 1858568
, cf. M.L.45i3a), interdum, interdiu (cf. dies), qui ont plutot le sens temporel. Comme pr 4 verbe, inter- (intel- devant un l qui suit: intel-lego), a le sens de: i° "entre", inter-calo,-cedo,-pono,-uenio, etc.; 3 0 "par intervalles, de temps en temps", inter-aestuG,-mitt 0 ,-uls 5 ', 3 0 enfin dans quelques composes, inter, comme per, introduit une id 4 e de pri- vation, de destruction, de mort; cf. intereS, interficis, interimo {cf. pereo, perimo)', aussi interdico. Ce dernier sens est ancien, comme le montre 1 'existence dans les gathas de l'Avesta de antar 3 -mruye (v. in terdIcd). Toutefois, 1 'origine n 1 en est pas aussi claire que pour per. Peut-etre faut-il partir de la valeur speciale prise par interdlcG (ou ses 4 quivalents) dans la langue religieuse, ou l'inter- diction, la prohibition devait etre marquee a 1'origine moins par le verbe lui-meme que par 1'ablatif qui 1'accomp
### SYN 10\.48\s+COME True
10.48 COME ®xouat, aor. #\Bov Goth. giman Lith. aleili Fexonas, Q0r. Fpba ON koma Lett. nakt (atiet) ene Dan. komme ChSl. priti, grestt : vil Sw. komma SCr. doi : ed OB cunan Boh. prijiti, prichdzeti Rum ie ME come Pol. przyj8é, przychodzi¢ I thee . NE come Russ. pridti, prichodit’ Nir, Shin Hicim Du. komen Skt. (@)gam-, (G-)i-, ete. ¥, dyfod (g OHG queman, coman Av. (@-)jam- del ie daeth, MHG komen, kumen don(e), : NHG kommen CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar Digitized by Arya Samaj Foundation Chennai and eGangotri a | | | 696 SELECTED INDO-EUROPEAN SYNONYMS 1. For the Latin, Romance, Ger- manic, and Indo-Iranian words, repre- senting IE *g“em-, and for the gen
### SYN \nCOME\b False
```


### [2026-09-06T02:28:12.067Z] TOOL RESULT

```
# Definitions of دیابت (Diabetes)

**Dehkhoda Dictionary:**
"مرض قند" (disease of sugar); notes French origin with the term "دولاب" (wheel), describing a condition resulting from decreased insulin secretion.

**Moein Dictionary:**
Describes it as "مرضی که به واسطة زیاد شدن مقدار قند خون" (a disease caused by increased blood sugar), characterized by excessive thirst and increased urination.

**Amid Dictionary:**
Simply states "مرض مرض قند" (the disease of sugar/diabetes).

**Origin:** All three sources indicate **French origin** for this term, though the sources don't explicitly mention Greek etymology in the excerpts provided.
```


## [2026-09-06T02:28:31.761Z] TOOL CALL #61: Bash

```json
{
 "command": "ls data/verification/page-20*.json 2>/dev/null; grep -o '\"name\": \"Gwen[^\"]*\"' data/extracted/batch/*.json | sort | uniq -c; echo ---; python3 -c \"\nimport json;d=json.load(open('data/verification/page-202.json'));e=d['entries'][0];print(e['verdict']);print(e['note'][:1500]);print('---FA---');print(e.get('note_fa','')[:600])\" 2>/dev/null || echo \"no 202 verification\""
}
```


### [2026-09-06T02:28:33.420Z] TOOL RESULT

```
(eval):1: no matches found: data/verification/page-20*.json
      1 data/extracted/batch/page-208.json:"name": "Gwen 1, Gwenâ, Gwŭnâ"
      1 data/extracted/batch/page-208.json:"name": "Gwen 2"
      1 data/extracted/batch/page-208.json:"name": "Gwenâ"
---
no 202 verification
```


## [2026-09-06T02:28:41.265Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-208.json'))\nfor e in d['entries']: print(e['root'])\n\"; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD gwadh ===\"; grep -n \"gäha\\|gahate\\|vigäthö\\|βῆσσα\\|Einsenkung\" incoming/WLD/WLD_Bd1_pages.txt | head -8"
}
```


### [2026-09-06T02:28:42.919Z] TOOL RESULT

```
{'name': 'Gwen 1, Gwenâ, Gwŭnâ', 'lang': 'Indo-European', 'refs': 'POK:473', 'gloss': 'woman, female'}
{'name': 'Gwen 2', 'redirect': 'Gwa'}
{'name': 'Gwenâ', 'redirect': 'Gwen 1'}
{'name': 'Gwer 1', 'lang': 'Indo-European', 'refs': 'POK:476', 'gloss': 'heavy'}
=== WLD gwadh ===
63869:Grdr. d. iran. Phil. I 10;, jafrat-s ..Yertiefung, Einsenkung" (J. Schmidt
```


## [2026-09-06T02:28:46.935Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"Schlucht\\|untertauchen\\|eintauchen\" WLD_Bd1_pages.txt | head -12"
}
```


### [2026-09-06T02:28:46.984Z] TOOL RESULT

```
2384:„Bergtal, Schlucht, Graben, Kanal, Meerenge“ *) aksl nlijt, lit. mtlgs und        :           .
5476:mung“ (= gr. to dyy.og „Tal, Schlucht“), aukasdm „Seite, Weiche; anku-
25228:nor          ,    -Cm ,,untertauchen“, unncdor „Taucher“;
50335: 23, 238;    s.   vielmehr u. *q“<:bh- „eintauchen", *q*embh- „tief‘‘). — Yerfehlt      ist
52422:    Gr. yva/.ov „Hohlung,                 Wolbung, Schlucht                       1'
53787: ,,Schlucht,Abgrund"; ags. geap „weit, geraumig"; geopan ,.in sich auf-
57114:     Gr. yaoddoa „ErdriS, Erdspalte,                        Schlucht"; yagaoom,                              att. -ttco    „spitze,
58185:anklammern"), ahd. klinga nhd. Klinge .,enge Schlucht, Klamm" (auch
62020: grem- .,feucht               sein),       untertauchen, untersinken".
62028: gramzdeti ds., gramzdinii, gramzdbiti untertauchen. versenken", gramzdiis
62045:  .jUntersenken, untertauchen", russ. gruziib,, versenken, eintauchen, befrachten".
62619:schale" und Schlucht, Schluft die aber wohl zu schliefen (z. B. Falk-Torp
```


## [2026-09-06T02:28:56.197Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"gähate\\|gahate\\|gäha\\|gadha\" WLD_Bd1_pages.txt | head -12; echo \"--- lines 63860-63880 ---\"; sed -n '63860,63875p' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T02:28:56.268Z] TOOL RESULT

```
63000:      Ai. gdhate       „taucht, dringt ein“,      ptc.   gadha-   „tief,       stark,   fest",   gcthd-lt
63029:ein sicherer Beweis ffir altes dh ist gadha- nicht, da man auf einer „Un-
--- lines 63860-63880 ---
*yWrmbh-.            zeigt das Arische (wobei im ai. das   der Tiefstufe                       (j


oder o-Stufe                   durcbgeftihrt         ist.      gegeniiber av. j der e-Stufe)        :   ai.   gabhird-,
(jumbhlrd- „tief", tjumbht              yamhhdra- n. ,,Tiefe, Abgrund“, gabhd
                                                ;
                                                    ymibhan
m. ..vulva", jabh i-sak AY. adv. vielleicht ..tief unten oder innen", av. jaiwi-
vafra- Adj. ,.mit tiefem Schnee". jafni- „tief" fuber f = w s. Bartholomae
Grdr. d. iran. Phil. I 10;, jafrat-s ..Yertiefung, Einsenkung" (J. Schmidt
KZ. 25. 88. Bartholomae BB. 15. 10, (.'aland KZ. 31, 267 Anm. 2).
   Fernzuhalten ist ai. gillutle „tauchcn, eindringen" Ptc. qadha- s. auch                (
                                                                                                              ;
```


## [2026-09-06T02:29:00.047Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '62990,63030p' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T02:29:00.106Z] TOOL RESULT

```
und bei Fick II 4 56 genannte mir. baes „Laune, Torheit" s. aber Peder-
sen KG. 1 56), Bgm. II 2 1, 201, 539, Boisacq u. cpaiog cpaidgog, Trautmann,




aaO. — Verfehlt ist Siebs KZ. 37, 319 Yermittlungsversuch mit sqai-t, -d-
„hell, leuchtend"           durch s-Vorschlag,

gSadli- „eintauchen, untersinken".
      Ai. gdhate       „taucht, dringt ein“,      ptc.   gadha-   „tief,       stark,   fest",   gcthd-lt
„Tiefe, das Innere", gadhd - „eine Furt darbietend, seicht", n. m. „Untiefe,
Furt" (? s. u.); mit d = 7 ai. gdhana-, gdhvara - „tief, dicht", n. „Tiefe, Ab-
grund, Dickicht", durgdlia-m „boser Ort oder Weg"; gr. /iijooa dor. fiaooa               ,

„Talgrund, Schlucht"; air. baidim ,,tauche unter, ertranke", cymr. boddi
„mergere, mergi, immergendo suffoeare vel suffocari", corn, bedhy, bret.
beuziff , ertranken“.
              ;



      Ygl. Fick II 4 161         (mit abliegendem),      Wackernagel Ai. Gr. 15, 217                 (ein
statt horn. PyoeTo          ,;
                              ging, bestieg" einzusetzendes pgooezo
                                                               aber nicht an-     ist

zuerkennen), XJhlenbeck Ai. Wb. 79, 80; kaum verwandt ist isl. kod „Fisch-
brut" (Fick III 4 44 f., Falk-Torp 570; sei „Grundfisch, im seichten Wasser
sich aufhaltender Fisch“).
   Unsicher bes. hinsichtlich der ind. Sippe ptc. gadlia-, lautgesetzlich auf
                                                              :




Wzauslaut gh weisend, mufi bei obiger Auffassung des li als idg. dh als
Analogiebildung nach Wurzeln mit ai. h                    =
                                              idg. ijh gedeutet werden; und
ein sicherer Beweis ffir altes dh ist gadha- nicht, da man auf einer „Un-
tiefe, Furt" eigentlich gerade nicht untersinkt und Deutung aus einem
```


## [2026-09-06T02:29:16.459Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '538,540p' AHD_watkins1985.txt | cut -c1-2500"
}
```


### [2026-09-06T02:29:16.508Z] TOOL RESULT

```
24
g”elbh-
(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living
```


## [2026-09-06T02:29:20.883Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '534,537p' AHD_watkins1985.txt | tail -c 2000"
}
```


### [2026-09-06T02:29:20.932Z] TOOL RESULT

```
greut-. To compress, push. 1. Germanic *kridan in Old English criidan, to press, hasten: CROWD!, 2. Germanic *krudam in Old English crod, a squeezing (> Middle English crud, crudde): CRUD, CURD. [Pok. greut- 406.]
gre-no-. Grain. 1. Germanic *kornam in: a. Old English corn, grain: CORN}; b. Old English derivative noun cyr- nel, seed, pip: KERNEL; c. Old High German korn, grain: EINKORN. 2. Latin grdnum, grain: GARNER, GRAIN, GRAM2, GRANADILLA, GRANARY, GRANGE, GRANITE, GRANULE, GRENADE; FILIGREE. [In Pok. ger- 390.]
gru-. To grunt. Imitative. 1. Germanic *grun- in Old English grunnian, to grunt, probably akin to Old English grunettan, to grunt: GRUNT. 2. Germanic intensive form *grunnatjan in Old High German grunniz6n, to grunt: GRUDGE. 3. Latin grunnire, grundire, to grunt: GRUNION. [Pok. gru- 406.]
gva-. Also grem-. To go, come. 1. Germanic *kuman in: a. Old English cuman, to come: COME; b. Germanic *kumo6n-, he who comes, a guest, in compound *wil-ku- mon-, a desirable guest (*wil-, desirable; see wel-2), in Old English wilcuma, a welcome guest, and wilcume, the greeting of welcome: WELCOME; C. compound *bi-kuman, to arrive, come to be (*bi-, intensive prefix; see ambhi), in Old English becuman, to become: BECOME. 2. Suffixed form *g“(e)m-yo- in Latin venire, to come: VENIRE, VENUE; ADVENT, (ADVENTITIOUS), (ADVENTURE), (AVE- NUE), CIRCUMVENT, CONTRAVENE, CONVENE, (CONVEN- IENT), (CONVENT), (CONVENTICLE), (CONVENTION),
```


## [2026-09-06T02:29:35.058Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A8%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7em-\" \\\n \"https://www.etymonline.com/word/base\" \\\n \"https://www.etymonline.com/word/basin\" \\\n \"https://www.etymonline.com/word/diabetes\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 203 (Gwa/Gwadh): root gwem-, jonbidan, base/basin, diabetes\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T02:29:38.746Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fce73d245c5d48f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bc22963085cc8cf1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bbad3a91ecba2441.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/095f43820b2b7312.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f9a38e6f67daac5a.txt
```


## [2026-09-06T02:29:46.728Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \\\n \"https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B3%D9%86/\" \\\n \"https://vajehyab.com/?q=%D8%A2%DA%A9%D8%B1%D9%88%D8%A8%D8%A7%D8%AA\" \\\n \"https://vajehyab.com/?q=%D8%AF%DB%8C%D8%A7%D8%A8%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%CE%B2%CF%85%CF%83%CF%83%CF%8C%CF%82\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 203 (Gwa/Gwadh): basan French loan, akrobat/diabet in Moin, Greek byssos\" 2>&1 | tail -2; done; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg203.png data/verification/sources/refs/ocr/BOOK/203.png && ls -la data/verification/sources/refs/ocr/BOOK/203.png"
}
```


### [2026-09-06T02:29:50.839Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d843706bf8784295.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/594e643548e6c280.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3f5cab0166aedc9c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/640d4f804a4c9de4.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 75609 Sep  5 22:29 data/verification/sources/refs/ocr/BOOK/203.png
```


## [2026-09-06T02:32:07.497Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON جنبید ===\"; grep -c \"جنبید\" MON_part1.txt MON_part2.txt; grep -n \"جنبید\" MON_part2.txt | head -5; echo \"=== MON جنبان/جنبنده ===\"; grep -n \"جنبنده\\|جنبان\" MON_part1.txt MON_part2.txt | head -5; echo \"=== WLD gumb ===\"; grep -n \"Schwellung\\|gumbas\" incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-09-06T02:32:07.621Z] TOOL RESULT

```
=== MON جنبید ===
MON_part2.txt:5
MON_part1.txt:13
3825:مایة رشکك. جنبیدن غیرت کسی: به غیرت 
39985:نااستوار بودن در جای خود و جنبیدن 
41167:خود جنبیدن (مانند کرم و مار). رفت و آمد 
81144:جنبیدن» حرکت کردن. لرزیدن. بر خود 
86037:وزان» وزیده» وزش). جنبیدن هواء حرکت 
=== MON جنبان/جنبنده ===
MON_part2.txt:889:غر: :[- قر] (ا.) جنباندن جزو یا تمام بدن 
MON_part2.txt:891:اطوار. غر و غمزه: جنبانیدن جزو یا تمام 
MON_part2.txt:964:جنبانیدن برای با کك کردن دهن؛ مضمضه 
MON_part2.txt:2473:2 7۵۱۷۸۱66 [- غلغلیچه] (۱.) جنبانیدن 
MON_part2.txt:18462:تحریکك سرین آن را جنبانند و به دوش 
=== WLD gumb ===
34089:1. keu- einerseits „schwellen, Schwellung,    Wolbung", andererseits „Hohlung,
52658:                 die             Leisten”      Schwellungen versehen
53090:entziindete Schwellung der Haut                                                                              -
63578:1. gHet-              „Schwellung. Rundung 4                          (Erweiterung von gen- „biegen“?                                                  s.    d,).
63586:zwischen dem und tj»ct- „Schwellung“ Worte fur Mund, Lippe vermitteln
```


## [2026-09-06T02:32:43.190Z] AGENT

Now I'll write the verification file.


## [2026-09-06T02:40:31.513Z] TOOL CALL #71: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build203.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nR = \"/home/sfmqrb/git/rishe/data/verification/sources/refs/\"\n\nW_WIKT_JONB = \"https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A8%DB%8C%D8%AF%D9%86\"\nW_WIKT_GWEM = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7em-\"\nW_ETY_BASE = \"https://www.etymonline.com/word/base\"\nW_ETY_BASIN = \"https://www.etymonline.com/word/basin\"\nW_ETY_DIAB = \"https://www.etymonline.com/word/diabetes\"\nW_ABADIS_BASAN = \"https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B3%D9%86/\"\nW_VAJEH_AKRO = \"https://vajehyab.com/?q=%D8%A2%DA%A9%D8%B1%D9%88%D8%A8%D8%A7%D8%AA\"\nW_VAJEH_DIAB = \"https://vajehyab.com/?q=%D8%AF%DB%8C%D8%A7%D8%A8%D8%AA\"\nW_WIKT_BUSSOS = \"https://en.wiktionary.org/wiki/%CE%B2%CF%85%CF%83%CF%83%CF%8C%CF%82\"\n\ne0nodes = [\n{\n \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"aiwi-gaiti; ni-jâma; gemton; gimsenin; gemmons\",\n \"verdict\": \"disputed\",\n \"error_in\": \"book\",\n \"book_prints\": \"all five words in one box headed 'Avestan / Old Persian  POK:464,465'\",\n \"derivation\": \"Two of the five words are Iranian and right; three are not Iranian at all. (1) Av. aiwi.gaiti- f. is a *-ti- abstract of the root gam-/jam- 'to come' (< *gʷm̥-ti-, the same formation as Greek basis and Gothic gaqumths); Bartholomae s.v. aiwi.gatay- glosses it 'Herzukommen', i.e. 'coming hither, entering, beginning' (V.6.6), and Pokorny p.465 cites 'Avestan aiwi-gati- \\\"coming along = entry, beginning\\\"' — so Nourai's 'to come here' is accurate. (2) ni-jama- is not an attested word but Pokorny's own reconstruction: p.465, in the paragraph 'With a meaning-development \\\"come (to the world)\\\" = \\\"be born\\\"', reads 'Avestan ni-jamayeinti \\\"be born\\\" (*ni-jama- \\\"birth\\\")' (Bartholomae AiW 1081). Nourai's added glosses 'origin, race' have no support: NP nezhad 'race' is *ni-zata- from zan- 'to be born', a different root. (3) gemton, gimsenin and gemmons are OLD PRUSSIAN (Baltic), not Avestan or Old Persian. They stand, with exactly these glosses, in the Baltic paragraph of the same Pokorny page: 'Old Prussian gimsenin Akk. Sg. \\\"birth\\\". Old Prussian gemton \\\"to give birth to children\\\", gemmons participle Perf. \\\"born\\\"', next to Lithuanian gemu/gimti 'be born'; Walde-Pokorny I 675 has them marked 'apr.' (altpreussisch). Nourai copied the whole Pokorny paragraph into an Iranian box and so mislabels a Baltic sub-group as Avestan/Old Persian. The page image (data/verification/sources/refs/ocr/BOOK/203.png) shows the extraction is faithful: the error is the book's. For the Old Persian half of the label the root itself is fine — Kent (Old Persian, §101) derives OP a-jamiya from PIE *gʷem- — but the box lists no Old Persian form.\",\n \"derivation_fa\": \"از پنج واژهٔ این خانه تنها دو تای نخست ایرانی است. aiwi.gaiti- اوستایی اسمِ ساخته‌شده با پسوند *-ti- از ستاک gam-/jam- «آمدن» است (از *gʷm̥-ti-، همان ساختی که basis یونانی دارد)؛ بارتولومه آن را «Herzukommen» یعنی «فرارسیدن، درآمدن، آغازیدن» معنی کرده و پوکورنی هم در ص ۴۶۵ همین را آورده است. ni-jāma- واژهٔ گواهی‌شده نیست بلکه بازساخت خودِ پوکورنی از فعل اوستایی nijamayeinti «زاده می‌شوند» است، بر پایهٔ تحول معنایی «به جهان آمدن ← زاده شدن»؛ اما معنای افزودهٔ «نژاد، اصل» پشتوانه ندارد، چون «نژاد» فارسی از *ni-zāta- و ریشهٔ zan- «زادن» است. سه واژهٔ gemton و gimsenin و gemmons اصلاً ایرانی نیستند: این‌ها پروسیِ کهن (شاخهٔ بالتیک) هستند و نورایی آن‌ها را با همان معانی از بند بالتیکِ همان صفحهٔ پوکورنی برداشته و در خانهٔ «اوستایی/پارسی باستان» نشانده است؛ والده-پوکورنی (ج۱ ص ۶۷۵) نیز آن‌ها را با نشانهٔ apr. (پروسی کهن) آورده است. تصویر صفحهٔ چاپی نشان می‌دهد استخراج امین بوده و خطا از خودِ کتاب است.\",\n \"sources\": [W_WIKT_GWEM],\n \"ref_check\": [\n   {\"ref\": \"POK:464\", \"status\": \"supports\", \"note\": \"Pokorny p.464-465 (POK_full.txt lines 38480-38520) has 'Avestan aiwi-gati- \\\"coming along = entry, beginning\\\"' and, under the birth-development, 'Avestan ni-jamayeinti \\\"be born\\\" (*ni-jama- \\\"birth\\\")' — the two Iranian items of the box.\"},\n   {\"ref\": \"POK:465\", \"status\": \"partial\", \"note\": \"the same page is also the source of gemton/gimsenin/gemmons, but Pokorny labels them 'Old Prussian' ('Old Prussian gimsenin Akk. Sg. \\\"birth\\\". Old Prussian gemton \\\"to give birth to children\\\", gemmons participle Perf. \\\"born\\\"', POK_full.txt line 38519-38521), not Avestan/Old Persian.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. aiwi.gatay- (BRT.txt line 3782)\", \"stance\": \"supports\", \"note\": \"'j. aiwi.gatay- f. \\\"Herzukommen\\\", sva. \\\"Eintreten, Beginnen\\\": pasca hama 'gaitim .. pasca zima 'gaitim V.6.6' — Bartholomae's Avestan aiwi.gaiti-, exactly Nourai's word and sense.\"},\n   {\"src\": \"KNT\", \"where\": \"§101 (KNT.txt line 2408)\", \"stance\": \"supports\", \"note\": \"Kent: 'pIE *gʷem- in opt. Skt. gam-yat, OP a-jamiya' — the Old Persian half of the box label is legitimate for jam- forms, though none is printed.\"},\n   {\"src\": \"WLD\", \"where\": \"WP I 675 (WLD_Bd1_pages.txt line 64055)\", \"stance\": \"contradicts\", \"note\": \"'... dzimsa \\\"Geburt\\\" = apr. gimsenin acc. sg. \\\"Geburt\\\", apr. gemton \\\"gebaren\\\", gemmons ppa. \\\"geboren\\\"; ... und nach Bartholomae Airan. Wb. 1081 av. nijamayeinti' — the three words are altpreussisch, and even the attachment of the whole Baltic group to gʷem- is only 'unter Annahme einer Bed.-Entwicklung \\\"(zur Welt) kommen\\\" = \\\"geboren werden\\\"' (Bechtel, Endzelin).\"}\n ]\n},\n{\n \"id\": 2, \"lang\": None, \"words\": \"\", \"verdict\": \"unverified\",\n \"derivation\": \"Empty pass-through box. On the printed page (pdf p. 203, book p. 173; see data/verification/sources/refs/ocr/BOOK/203.png) the large rectangle to the right of the Avestan/Old Persian box is drawn but left completely blank — no language, no reference, no word. The extraction is faithful; there is nothing to verify. By the layout of the other charts this slot was meant for the Persian outcome of the Iranian forms (Part 1, on book p. 172, carries them: gam, amadan, niyam, payam etc.).\",\n \"derivation_fa\": \"خانهٔ خالیِ واسط: در صفحهٔ چاپی (برگ ۲۰۳ پی‌دی‌اف، ص ۱۷۳ کتاب) مستطیل بزرگِ کنارِ جعبهٔ اوستایی/پارسی باستان کشیده شده اما یکسره سفید مانده است؛ نه نام زبان دارد، نه ارجاع، نه واژه. استخراج امین بوده و چیزی برای راستی‌آزمایی نیست. به قرینهٔ چیدمان دیگر نمودارها، این خانه جای بازتاب‌های فارسی بوده که نویسنده آن‌ها را در «بخش ۱» (ص ۱۷۲: گام، آمدن، نیام، پیام) آورده است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_found\", \"note\": \"the node carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 463-465\", \"stance\": \"silent\", \"note\": \"nothing to look up: the box is blank.\"},\n   {\"src\": \"BRT\", \"where\": \"-\", \"stance\": \"silent\", \"note\": \"no form printed in the box to check.\"}\n ]\n},\n{\n \"id\": 3, \"lang\": \"Greek\",\n \"words\": \"bainein; dia-bainein; akro-bates\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Gk. bainein (βαίνω) 'to go, walk, step' is the yo-present of the zero grade, *gʷm̥-yō > *banyō > bainō (Watkins: 'Suffixed zero-grade form *gʷm̥-yo- in Greek bainein'), with aorist ebēn from the *gʷā- variant; the nominal basis (< *gʷm̥-ti-) 'a stepping, pedestal' belongs to it. dia-bainein 'to step across, pass through' (dia 'through' + bainein) gives the agent noun diabētēs 'a passer-through, siphon', the disease name coined by Aretaeus of Cappadocia (2nd c. CE) because the body seems to pass water straight through; Nourai's gloss describes the disease, not the verb, which simply means 'to step across'. akro-batēs 'one who walks on tiptoe' = akros 'topmost, at the point' + -batēs (< *gʷm̥-to-) 'goer'; Klein s.v. acrobat: 'Gk. akrobatos, walking on tiptoe, fr. akros ... and bat-, going, from the stem of bainein'.\",\n \"derivation_fa\": \"βαίνω یونانی فعلِ ساخته‌شده با پسوند -yo- بر پایهٔ درجهٔ صفرِ ریشه است (*gʷm̥-yō ← bainō) و ماضی سادهٔ ebēn آن از گونهٔ *gʷā- می‌آید؛ اسمِ βάσις «گام، پایه» (از *gʷm̥-ti-) نیز از همین‌جاست. διαβαίνω یعنی «از عرض گذشتن» و نام بیماری از اسمِ διαβήτης «سیفون، آنچه [آب] از آن می‌گذرد» است که آرتایوسِ کاپادوکیایی در سدهٔ دوم میلادی بر این بیماری نهاد؛ پس معنایی که نورایی برای dia-bainein نوشته در حقیقت معنای همان اسم است نه معنای فعل. ἀκροβάτης «نوک‌پا رونده» از ἄκρος «نوک، بالا» و -βάτης «رونده» ساخته شده است. ادعای نورایی در این خانه درست است و کلاین و واتکینز هر دو آن را تأیید می‌کنند.\",\n \"sources\": [W_ETY_DIAB],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins, gʷā- entry (AHD_watkins1985.txt line 540): '3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein, to go, walk, step, with basis (< *gʷm̥-ti-) ... and -batēs ...: BASE1, BASIS; ABASIA, ACROBAT, ADIABATIC ... DIABETES'.\"},\n   {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein s.v. base, n. (KLN_1966.txt offset 963104): 'Gk. basis ... from the stem of bainō, \\\"I go\\\" ... fr. I.-E. base *gʷem-, \\\"to go; to come\\\"'; s.v. acrobat: 'F. acrobate, fr. Gk. akrobatos, \\\"walking on tiptoe\\\"'; s.v. adiabatic: 'diabatos, verbal adj. of diabainein, \\\"to step across\\\" ... cp. diabetes'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.v. acrobat, come\", \"stance\": \"supports\", \"note\": \"Skeat: 'acrobat ... Gk. akrobates, lit. one who walks on tiptoe ... and batēs, verbal adj. of bainein, to walk; see Come'; s.v. Come he groups 'Goth. kwiman, G. kommen, L. uenire, Gk. bainein, Skt. gam'.\"},\n   {\"src\": \"FSD\", \"where\": \"s.v. acrobat (FSD_vol1.txt)\", \"stance\": \"supports\", \"note\": \"'ac-ro-bat ... [< F. acrobate, <' — Funk & Wagnalls routes the English word through French from the Greek.\"}\n ]\n},\n{\n \"id\": 4, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box: the printed page shows a French box with no word in it, standing between the Greek box and the Persian one. The forms it stands for are French diabète (a learned borrowing of Late Latin diabētēs, Greek diabētēs, in medical French from the 14th c. onward) and acrobate (borrowed from Greek akrobatēs in 1688 and popularised in the 19th c.). Both are the actual etyma of the two Persian words in the next box, so the intermediate step the box marks is real even though it is blank.\",\n \"derivation_fa\": \"خانهٔ فرانسویِ خالی است: در صفحهٔ چاپی جعبه‌ای بدون واژه میان خانهٔ یونانی و خانهٔ فارسی کشیده شده و تنها نقشِ واسطه دارد. صورت‌های مقصود diabète و acrobate فرانسوی‌اند؛ اولی وام‌واژه‌ای عالمانه از لاتینِ متأخر diabētēs (از یونانی) در زبان پزشکی فرانسه و دومی وام‌گیریِ مستقیم از یونانی akrobatēs در سدهٔ هفدهم است. چون همین دو واژه ریشهٔ بی‌واسطهٔ «دیابت» و «آکروبات» فارسی‌اند، این حلقهٔ میانی—هرچند خالی—درست است.\",\n \"sources\": [W_ETY_DIAB],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_found\", \"note\": \"the box carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. acrobat\", \"stance\": \"supports\", \"note\": \"'acrobat, n. — F. acrobate, fr. Gk. akrobatos' — Klein makes French the intermediary, as the chart does.\"},\n   {\"src\": \"FSD\", \"where\": \"s.v. acrobat\", \"stance\": \"supports\", \"note\": \"'[< F. acrobate ...]'.\"}\n ]\n},\n{\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"«دیابت ، آکروبات»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both words are 20th-century French loans, not Greek or Arabic ones. NP diyabet 'دیابت' renders French diabète (French final -e mute, so Persian ends in -ت); NP akrobat 'آکروبات' renders French acrobate, with the Persian initial آ for French a- and the same stress-final shape as the French word. They came in with French-medium medicine and French-medium theatre/circus vocabulary in the late Qajar and early Pahlavi decades. Mo'in marks آکروبات explicitly '[فر.]' ('بندباز، ورزشکاری که کارهایی مانند بندبازی، ژیمناستیک ... را انجام می‌دهد') and gives دیابت as 'مرضی که به واسطهٔ زیاد شدن مقدار قند خون ...', with Dehkhoda likewise labelling it French; so the arrow French → Persian is exactly what the Persian lexicographical tradition says.\",\n \"derivation_fa\": \"هر دو واژه وام‌واژهٔ فرانسوی سدهٔ اخیرند، نه یونانی و نه معرّب. «دیابت» برگردانِ diabète فرانسوی است (ـهٔ پایانیِ ناخوانای فرانسوی می‌افتد و واژه به «ت» ختم می‌شود) و «آکروبات» برگردانِ acrobate است. راه ورودشان زبان پزشکی و سپس سیرک و نمایشِ فرانسوی‌مآب در اواخر قاجار و اوایل پهلوی بوده است. معین در برابر «آکروبات» نشانهٔ [فر.] گذاشته و «دیابت» را نیز فرانسوی دانسته و دهخدا هم همین را می‌گوید؛ بنابراین پیکانِ فرانسوی ← فارسی دقیقاً همان چیزی است که فرهنگ‌نویسی فارسی می‌گوید و ادعای نورایی درست است.\",\n \"sources\": [W_VAJEH_AKRO, W_VAJEH_DIAB],\n \"ref_check\": [\n   {\"ref\": \"MON:75\", \"status\": \"supports\", \"note\": \"Mo'in s.v. آکروبات (read through vajehyab, the Mo'in section): 'رُ [فر.] بندباز، ورزشکاری که کارهایی مانند بندبازی، ژیمناستیک و ... را انجام می‌دهد' — '[فر.]' = French, i.e. Mo'in's own page (vol. 1, p. 75 of the alef section) says what the arrow says.\"},\n   {\"ref\": \"MON:1588\", \"status\": \"supports\", \"note\": \"Mo'in s.v. دیابت: 'مرضی که به واسطهٔ زیاد شدن مقدار قند خون ...' with French origin; the local OCR has the entry too (MON_part1.txt line 64279: 'دیابت: ... (بز.) مرضی که به سبب ازدیاد مقدار خون تولید گردد'), though the OCR carries no page numbers so p.1588 itself could not be re-counted.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. آکروبات, دیابت (vajehyab)\", \"stance\": \"supports\", \"note\": \"'[فر.]' on آکروبات; دیابت given as a French medical term.\"},\n   {\"src\": \"BQT\", \"where\": \"grep of BQT_v1/v2_pages.txt\", \"stance\": \"silent\", \"note\": \"neither word occurs in Borhan-e Qate' (1062 AH), as expected for 20th-century Europeanisms.\"}\n ]\n},\n{\n \"id\": 6, \"lang\": \"English\", \"words\": \"diabetes, acrobat\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"diabetes entered English in the 1560s from medical Latin diabētēs, from Greek diabētēs 'siphon, passer-through' (dia- + bainein); the older English name of the complaint was 'the pissing evil'. acrobat is 1825 in English, from French acrobate, from Greek akrobatēs — so for this word the French box above is not decorative but the actual route. Watkins files both under the same root: 'BASE1, BASIS; ABASIA, ACROBAT, ADIABATIC ... DIABETES' in the gʷā- entry, and the AHD index lines read 'ACROBAT gʷā-' and 'DIABETES gʷā-'.\",\n \"derivation_fa\": \"«diabetes» در دههٔ ۱۵۶۰ از لاتینِ پزشکی diabētēs و آن از یونانی diabētēs «سیفون، گذرنده» وارد انگلیسی شده است؛ نام کهن‌ترِ همین بیماری در انگلیسی «pissing evil» بود. «acrobat» در ۱۸۲۵ و از راه فرانسوی acrobate به انگلیسی رسیده است، پس برای این واژه خانهٔ فرانسویِ بالای نمودار مسیر واقعی است. واتکینز در پیوستِ AHD هر دو را زیر همین ریشه آورده است؛ ادعای نورایی درست است.\",\n \"sources\": [W_ETY_DIAB],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD/Watkins index (AHD_watkins1985.txt lines 1217, 1424): 'ACROBAT gʷā-' ... 'DIABETES gʷā-'; the root entry lists both.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. acrobat, adiabatic\", \"stance\": \"supports\", \"note\": \"'acrobat, n. — F. acrobate, fr. Gk. akrobatos ... For the second element see base, n.'; adiabatic cross-refers to diabetes.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. acrobat\", \"stance\": \"supports\", \"note\": \"'acrobat, a tumbler. (Gk.; or F. — Gk.) F. acrobate. — Gk. akrobates ... batēs, verbal adj. of bainein, to walk'.\"}\n ]\n},\n{\n \"id\": 7, \"lang\": \"French\", \"words\": \"basse, bassin\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Neither French word belongs to this root. (a) basse is the feminine of bas 'low', from Late Latin bassus 'thick, stumpy, low' — a word known in classical Latin only as a cognomen and of uncertain origin (Oscan? Celtic?); Klein s.v. base, adj.: 'ME. bas, fr. OF (= F.) bas, \\\"low\\\", fr. Late L. bassus, \\\"thick fat, stumpy\\\" ... of uncertain origin', and Watkins keeps a separate non-Indo-European headword 'bassus' for it (index: 'ABASE bassus', 'BASE2 bassus', 'BAS-RELIEF bassus', 'BASSET bassus', 'BASSO bassus'). (b) bassin is from Old French bacin, Vulgar Latin *baccinum (Gregory of Tours cites bacchinon as a vulgar word), from *bacca 'water vessel', probably Gaulish — Klein s.v. basin, and Etymonline s.v. basin. What Nourai actually needed in this box is French base, the learned borrowing of Latin basis (Greek basis) — that is the word from which English base and basic come. The cited reference AHD:110 is the dictionary page for base/basis, which supports the English box below but not the two French words printed here.\",\n \"derivation_fa\": \"هیچ‌یک از دو واژهٔ فرانسویِ این خانه به این ریشه نمی‌رسد. basse مؤنثِ bas «پست، کوتاه» است و از لاتینِ متأخر bassus «کلفت، کوتاه» می‌آید که در لاتینِ کلاسیک تنها به‌عنوان لقب دیده شده و اصلش نامعلوم است (شاید اوسکی یا سلتی)؛ کلاین آن را جدا از base آورده و واتکینز نیز برای آن مدخلِ جداگانه و غیرهندواروپاییِ bassus ساخته است. bassin هم از فرانسویِ کهن bacin و لاتینِ عامیانهٔ *baccinum از *bacca «ظرف آب» (احتمالاً گالی) است. آنچه نورایی در این خانه لازم داشته واژهٔ فرانسویِ base است، یعنی وام‌واژهٔ عالمانهٔ basis لاتین/یونانی، که ریشهٔ base و basic انگلیسی است. ارجاع AHD:110 نیز صفحهٔ فرهنگ برای base/basis است و خانهٔ انگلیسیِ زیرین را تأیید می‌کند نه این دو واژهٔ فرانسوی. پژوهش امروزی این حلقه را رد می‌کند.\",\n \"sources\": [W_ETY_BASE, W_ETY_BASIN],\n \"ref_check\": [{\"ref\": \"AHD:110\", \"status\": \"partial\", \"note\": \"AHD p.110 is the base/basic page of the dictionary proper; Watkins's appendix does derive BASE1 and BASIS from gʷā-, but files bas/basse under a separate headword 'bassus' (index lines 'ABASE bassus', 'BASE2 bassus'), and has nothing that would attach bassin to this root.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. base adj. and basin (KLN_1966.txt offsets 963104, 967326)\", \"stance\": \"contradicts\", \"note\": \"'base, adj. — ... fr. Late L. bassus ... of uncertain origin'; 'basin, n. — ME., fr. OF. bacin, bassin (F. bassin), fr. VL. *baccinum, fr. bacchinon ... fr. *bacca, \\\"a water vessel\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index s.v. BASE2, ABASE\", \"stance\": \"contradicts\", \"note\": \"the appendix's own index sends bas-words to 'bassus', a Latin word not derived from any IE root, and only BASE1/BASIS to gʷā-.\"},\n   {\"src\": \"WEB\", \"where\": \"-\", \"stance\": \"silent\", \"note\": \"Webster vol. 1 (A-) OCR on disk was not searchable for these entries; not used.\"}\n ]\n},\n{\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"bâsan «باسن»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The immediate step drawn here is right: Persian باسن 'buttock, hip' is a French loan. Dehkhoda's entry reads '(فرانسوی، اِ) بمعنی لگن خاصره، استخوان‌بندی لگن خاصره' — i.e. French bassin in its anatomical sense 'pelvis' (French bassin = 'basin' and, in anatomy, 'pelvis'); Persian narrowed/lowered the sense to 'hip, buttock' (Mo'in: 'برجستگی در پشت بدن بالاتر از ران و پایین‌تر از کمر'). What fails is the chain above it: bassin is from Vulgar Latin *baccinum, not from Greek bainein (see node #7), so باسن does not belong to this root at all — it is a 20th-century Europeanism, not an inherited Iranian word. (A folk suggestion connecting it to Turkish basmak 'to press' circulates online but has no scholarly backing.) Nourai's reference VOP:83 (Moshiri, Farhang-e vazheha-ye orupayi dar farsi) is precisely a dictionary of European loans in Persian, which fits the loan claim.\",\n \"derivation_fa\": \"پیکانِ بی‌واسطهٔ این خانه درست است: «باسن» فارسی وام‌واژه‌ای فرانسوی است. دهخدا خودِ مدخل را «(فرانسوی، اِ) بمعنی لگن خاصره، استخوان‌بندی لگن خاصره» آورده، یعنی همان bassin فرانسوی که در کالبدشناسی «لگن» معنی می‌دهد؛ فارسی معنا را به «سرین، کفل» فروکاسته است (معین: «برجستگی در پشت بدن بالاتر از ران و پایین‌تر از کمر»). آنچه نادرست است زنجیرهٔ بالادستی است: bassin از لاتینِ عامیانهٔ *baccinum می‌آید نه از bainein یونانی، پس «باسن» اصلاً به این ریشه تعلق ندارد و واژه‌ای اروپایی از سدهٔ اخیر است، نه میراثِ ایرانی. ارجاع نورایی به VOP (فرهنگ واژه‌های اروپایی در فارسیِ مشیری) با همین وام‌واژه‌بودن سازگار است، هرچند نسخه‌ای از آن در دسترس نبود.\",\n \"sources\": [W_ABADIS_BASAN],\n \"ref_check\": [{\"ref\": \"VOP:83\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (1371) — refs_online.json records that no copy could be found online or offline (kind: none), so p.83 could not be read.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. باسن (abadis, Mo'in section)\", \"stance\": \"supports\", \"note\": \"'برجستگی در پشت بدن بالاتر از ران و پایین‌تر از کمر'; Dehkhoda on the same page marks the word '(فرانسوی، اِ)' — an explicit French loan, as the arrow says. The local Mo'in OCR files have no باسن headword (grep of MON_part1/2).\"},\n   {\"src\": \"ARY\", \"where\": \"p. 405 (ARY_pages.txt line 12034)\", \"stance\": \"silent\", \"note\": \"Aryanpur uses باسن only as a gloss for Latin coxa in the entry for کش; he gives no Indo-European etymology for باسن itself, i.e. he does not treat it as an inherited word.\"},\n   {\"src\": \"BQT\", \"where\": \"grep of BQT_v1_pages.txt\", \"stance\": \"silent\", \"note\": \"no باسن 'buttock' headword in Borhan-e Qate' — consistent with a modern European loan rather than a classical Persian word.\"}\n ]\n},\n{\n \"id\": 9, \"lang\": \"English\", \"words\": \"base, basic\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The word and the root are right, the French form drawn above it is not. English base (n.) is 14th-c., from Old French/French base, a learned borrowing of Latin basis, itself Greek basis 'a stepping, that on which one stands, pedestal' < *gʷm̥-ti- from bainein; basic is a 19th-c. English derivative (first in chemistry, 1842, on base in Rouelle's 1754 chemical sense). Watkins puts BASE1 and BASIS under gʷā- and AHD p.110 is that dictionary page. But the parent box prints basse and bassin, which are different French words (see #7); the correct intermediary is French base. Note too that English base (adj.) 'low, mean' is the bassus word and is not from this root — a distinction Nourai's chart blurs.\",\n \"derivation_fa\": \"واژه و ریشه درست‌اند، اما صورتِ فرانسویِ بالای آن نادرست است. base انگلیسی از سدهٔ چهاردهم و از base فرانسوی است که خود وام‌واژهٔ عالمانهٔ basis لاتین و آن از βάσις یونانی «گام، پایه» (از *gʷm̥-ti- و ستاک bainein) است؛ basic ساختی انگلیسی از سدهٔ نوزدهم است (نخست در شیمی، ۱۸۴۲). واتکینز BASE1 و BASIS را زیر همین ریشه آورده و AHD:110 هم همان صفحهٔ فرهنگ است. اما خانهٔ مادر basse و bassin را چاپ کرده که واژه‌هایی دیگرند؛ واسطهٔ درست base فرانسوی است. افزون بر این، base انگلیسی به معنای «پست» از bassus می‌آید و به این ریشه ربطی ندارد—تمایزی که نمودار آن را مخدوش کرده است.\",\n \"sources\": [W_ETY_BASE],\n \"ref_check\": [{\"ref\": \"AHD:110\", \"status\": \"supports\", \"note\": \"Watkins gʷā- entry: 'Greek bainein ... with basis (< *gʷm̥-ti-), a stepping, tread, base ...: BASE1, BASIS'; index 'BASE1 gʷā-'.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. base n. and basis\", \"stance\": \"supports\", \"note\": \"'base, n., bottom; foundation, pedestal. — F., fr. L. basis, fr. Gk. basis ... from the stem of bainō ... fr. I.-E. base *gʷem-'; 'basis, n. — L., fr. Gk. basis. See base, n.'\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. base\", \"stance\": \"partial\", \"note\": \"Skeat's short entry 'Base. (F.)' is badly OCR'd and in the concise edition is conflated with the adjective; it adds nothing against Klein.\"}\n ]\n},\n{\n \"id\": 10, \"lang\": \"Latin\", \"words\": \"venîr\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"venîr : to come\",\n \"correct_form\": \"venîre (Latin venīre, 1sg veniō)\",\n \"derivation\": \"The etymology is right, the form is a misprint. Latin has veniō, venīre 'to come' from *gʷ(e)m-yō (Watkins: '2. Suffixed form *gʷ(e)m-yo- in Latin venire, to come'), with Pokorny p.464 noting the 'very old alteration from -mi̯- to -ni̯-' and the analogical -en- of the paradigm. The page prints 'venîr' without the final -e, which is neither Latin nor Nourai's own convention: elsewhere he writes Latin infinitives out in full with -îre (ferîre p.90, ap-erîre / op-erîre p.546, scîre p.439, ambi-îre p.51). The page image (data/verification/sources/refs/ocr/BOOK/203.png) shows the JSON copies the page exactly, so this is the book's typo, not an extraction error.\",\n \"derivation_fa\": \"ریشه‌شناسی درست است اما صورتِ واژه غلط چاپی است. لاتین veniō / venīre «آمدن» از *gʷ(e)m-yō است؛ واتکینز همین را می‌گوید و پوکورنی در ص ۴۶۴ به تبدیل کهنِ -mi̯- به -ni̯- و -en- قیاسیِ صرفِ فعل اشاره می‌کند. صفحهٔ چاپی «venîr» را بدون ـهٔ پایانی آورده که نه لاتین است و نه با شیوهٔ خودِ نورایی می‌خواند: او در جاهای دیگر مصدرِ لاتین را کامل و با -îre می‌نویسد (ferîre، ap-erîre، scîre، ambi-îre). تصویر صفحه نشان می‌دهد داده‌ها امین استخراج شده‌اند؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 537: 'gʷā-. Also gʷem-. To go, come. ... 2. Suffixed form *gʷ(e)m-yo- in Latin venire, to come: VENIRE, VENUE; ADVENT ...' — the Latin form is venire, with -e.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. avenue / venue\", \"stance\": \"supports\", \"note\": \"'avenue, n. — F., prop. fem. pp. of avenir, \\\"to come to\\\", fr. L. advenire, fr. ad- and venire, \\\"to come\\\"' — Klein's Latin lemma is venire.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt)\", \"stance\": \"silent\", \"note\": \"the OCR of Ernout-Meillet yields only compounds (interuenio, inuenio, aduenio); the uenio headword itself could not be located in the scanned text.\"},\n   {\"src\": \"POK\", \"where\": \"p. 464 (POK_full.txt line 38495)\", \"stance\": \"supports\", \"note\": \"'yo-present *gʷm̥-yō: gr. bainō \\\"go\\\", Latin venio \\\"come\\\" with very old alteration from -mi̯- to -ni̯-'.\"}\n ]\n},\n{\n \"id\": 11, \"lang\": \"English\", \"words\": \"avenue, event, prevent, invent\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are Latin venīre compounds taken over through French or directly from Latin: avenue (1600s) is French avenue, feminine past participle of avenir 'to come to' < Latin advenīre, first 'a way of approach', then the tree-lined approach to a house; event is Latin ēventus 'outcome' (ē-venīre 'to come out'), 1570s; prevent is Latin praevenīre 'to come before, anticipate' (the older English sense 'to act before' survives in 'prevenient grace'); invent is Latin invenīre 'to come upon, find', whence 'devise'. Watkins lists AVENUE, EVENT, INVENT, PREVENT in the gʷā- entry's Latin section.\",\n \"derivation_fa\": \"هر چهار واژه از ترکیب‌های venīre لاتین‌اند که یا از راه فرانسوی و یا مستقیم از لاتین به انگلیسی رسیده‌اند: avenue همان صفتِ مفعولیِ مؤنثِ avenir فرانسوی از advenīre لاتین است و نخست «راهِ رسیدن» و سپس «خیابانِ درخت‌کاری‌شدهٔ منتهی به خانه» معنی داده؛ event از ēventus «برآمد» (ē-venīre)؛ prevent از praevenīre «پیش‌تر آمدن»؛ و invent از invenīre «بر چیزی رسیدن، یافتن». واتکینز هر چهار را در بخشِ لاتینِ همین ریشه فهرست کرده است؛ ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_found\", \"note\": \"the box carries no reference; the parent's AHD covers it.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins gʷā- entry and index\", \"stance\": \"supports\", \"note\": \"'... EVENT, INTERVENE, INVENT, ... PREVENIENT, PREVENT, ... (AVENUE) ...'; index: 'AVENUE gʷā-', 'INVENT gʷā-', 'PREVENT gʷā-'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. avenue\", \"stance\": \"supports\", \"note\": \"'avenue. (F. — L.) F. avenue, advenue, access; hence an approach to a house ... — F. avenir, to come to. — L. ad, to; uenire, to come.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. avenue\", \"stance\": \"supports\", \"note\": \"'F., prop. fem. pp. of avenir ... fr. L. advenire'.\"}\n ]\n},\n{\n \"id\": 12, \"lang\": \"Germanic\", \"words\": \"kuman\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Nourai's 'kuman' is Watkins's form verbatim: 'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman in: a. Old English cuman, to come'. In fuller terms the Proto-Germanic verb is *kwemaną (Gothic qiman, Old High German queman) from full-grade *gʷem-, beside the zero-grade variant *kuman < *gʷm̥- that gives Old English cuman, Old Norse koma, Old High German coman — Grimm's law turning PIE *gʷ into Germanic *kw/*k. So 'Germanic kuman \\\"to come\\\"' is right, though it is the zero-grade by-form rather than the base verb.\",\n \"derivation_fa\": \"صورتِ «kuman» عیناً همان است که واتکینز آورده: «ژرمنی *kuman، در انگلیسی کهن cuman \\\"آمدن\\\"». به بیان دقیق‌تر فعلِ ژرمنیِ آغازین *kwemaną است (گوتیک qiman، آلمانی علیای کهن queman) از درجهٔ کاملِ *gʷem-، در کنار گونهٔ درجه‌صفرِ *kuman از *gʷm̥- که انگلیسی کهن cuman و نورس کهن koma و آلمانی علیای کهن coman از آن است؛ *gʷ هندواروپایی بر پایهٔ قانون گریم در ژرمنی به kw/k بدل شده است. پس «ژرمنی kuman» درست است، هرچند گونهٔ درجه‌صفر است نه فعلِ پایه.\",\n \"sources\": [W_WIKT_GWEM],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 537: '1. Germanic *kuman in: a. Old English cuman, to come: COME; b. Germanic *kumōn-, he who comes, a guest, in compound *wil-kumon- ...: WELCOME; c. compound *bi-kuman ...: BECOME.'\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. base n. / come\", \"stance\": \"supports\", \"note\": \"Klein derives 'Goth. qiman, OE. cuman, \\\"to come\\\"' from I.-E. *gʷem- in the same breath as Greek bainō and Latin venio.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 10.48 COME\", \"stance\": \"supports\", \"note\": \"Buck's table for 'come' aligns Goth. qiman, ON koma, OE cuman, NHG kommen with Lat. uenio, Gk. bainō, Skt. gam-, Av. (ā-)jam-, 'representing IE *gʷem-'.\"}\n ]\n},\n{\n \"id\": 13, \"lang\": \"English\", \"words\": \"come, become, welcome, income\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"come is Old English cuman > Middle English comen; become is Old English becuman 'to arrive, happen, turn out' (bi- + cuman), whose modern sense 'to come to be' is a Middle English development; welcome reshapes Old English wilcuma 'a welcome guest' / wilcume 'the greeting' (wil- 'desire, pleasure' + cuma 'comer') under the influence of well and come, helped by Old French bien venu; income is a native Middle English compound of in + come (first 'a coming in', then 'revenue', 14th-15th c.), not a separate inheritance. Watkins's index lists COME, BECOME and WELCOME under gʷā-.\",\n \"derivation_fa\": \"come از cuman انگلیسی کهن است؛ become از becuman «رسیدن، پیش آمدن» (bi- + cuman) که معنای امروزیِ «شدن» تحولی میانه‌انگلیسی است؛ welcome بازساختِ wilcuma «مهمانِ خوش‌آمده» (wil- «خواست، خوشی» + cuma «آینده») است که زیر تأثیر well و come و نیز bien venu فرانسوی به این شکل درآمده؛ و income ترکیبی بومی از in + come در انگلیسی میانه است («درآمدن» و سپس «درآمد»)، نه میراثی جداگانه. واتکینز COME و BECOME و WELCOME را زیر همین ریشه آورده است؛ ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_found\", \"note\": \"the box carries no reference; covered by the parent's AHD.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins gʷā- entry\", \"stance\": \"supports\", \"note\": \"'*wil-kumon-, a desirable guest ... in Old English wilcuma ...: WELCOME; c. compound *bi-kuman ... in Old English becuman, to become: BECOME.'\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. come, become, income\", \"stance\": \"supports\", \"note\": \"'Come. (E.) A.S. cuman ... become. (E.) A.S. becuman, to arrive, happen, turn out, befall ... income' — Skeat groups the same four.\"}\n ]\n},\n{\n \"id\": 14, \"lang\": \"Indo-European\", \"words\": \"Ğhumbo\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The lemma is real but belongs to a different root. Mann, Indo-European Comparative Dictionary p.425, has 'ǵhumbo (ǵhub-) \\\"start, move, jump, stir\\\". Cf. ǵhūb-. Per. jumbam, -īdan, intr. \\\"move, stir\\\"; MLG, E, LG gumpen \\\"jump\\\"' — Nourai's form and gloss are copied from it word for word, so IEC:425 does support the existence of the node and its Persian tie. But Mann's headword begins with a palatal ǵh- and sits in his ǵhūb- / ǵhugh- 'stir, shake, agitate' family (IEC 424-425), not with gʷā-/gʷem-; Pokorny's gʷā-, gʷem- article (463-465) contains no such extension and no Iranian jumb- word, and Watkins's gʷā- entry has nothing of the kind either. Attaching Ğhumbo to Gwa as a daughter box is therefore Nourai's own step, unsupported by his own source. Phonologically it is also awkward: a PIE palatal *ǵh would give Iranian z-, not j-, so a Persian jumb- cannot continue Mann's ǵhumb- as written.\",\n \"derivation_fa\": \"خودِ مدخل واقعی است اما به ریشهٔ دیگری تعلق دارد. مان در فرهنگ تطبیقی هندواروپایی، ص ۴۲۵، آورده است: «ǵhumbo (ǵhub-) \\\"آغازیدن، جنبیدن، جستن\\\"؛ فارسی jumbam، -īdan \\\"جنبیدن\\\"؛ آلمانی سفلای میانه gumpen \\\"جستن\\\"» — یعنی صورت و معنایی که نورایی نوشته عیناً از همان‌جاست و ارجاع IEC:425 در این حد درست است. اما سرواژهٔ مان با ǵh کامی آغاز می‌شود و در خانوادهٔ ǵhūb-/ǵhugh- «جنباندن، لرزاندن» جای دارد، نه در ریشهٔ gʷā-/gʷem-؛ پوکورنی در مقالهٔ gʷā-, gʷem- (ص ۴۶۳–۴۶۵) نه چنین گسترشی دارد و نه هیچ واژهٔ ایرانیِ jumb-، و واتکینز نیز چیزی از این دست ندارد. پس وصل‌کردن Ğhumbo به Gwa کارِ خودِ نورایی است و منبعِ خودش آن را تأیید نمی‌کند. از نظر آوایی نیز *ǵh هندواروپایی در ایرانی z می‌دهد نه j، پس jumb- فارسی نمی‌تواند دنبالهٔ ǵhumb- باشد.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"IEC:425\", \"status\": \"partial\", \"note\": \"Mann p.425 (IEC.txt line 6144, between the page markers 424 and the ǵhustos entry): 'ǵhumbo (ǵhub-) \\\"start, move, jump, stir\\\". Cf. ǵhūb-. Per. jumbam -īdan, intr. \\\"move, stir\\\"; MLG E LG gumpen (\\\"jump\\\")'. The lemma and the Persian link are Mann's; the placement under gʷā- is not.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 463-465 (gʷā-, gʷem-)\", \"stance\": \"silent\", \"note\": \"Pokorny's article lists no *ghumb- extension and no Iranian jumb-/junb- form anywhere.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins gʷā- entry\", \"stance\": \"silent\", \"note\": \"the six numbered sections of gʷā- (Germanic *kuman, Latin venire, Greek bainein, *pres-gʷu-, bēma, Sanskrit jigāti) contain nothing comparable.\"},\n   {\"src\": \"IEC\", \"where\": \"pp. 424-425\", \"stance\": \"partial\", \"note\": \"the neighbouring lemmas ǵhūb- 'stir, move' and ǵhugh- 'stir, shake, tremble, agitate' show where Mann himself files this word — in a palatal *ǵh- family, far from gʷem-.\"}\n ]\n},\n{\n \"id\": 15, \"lang\": \"Pahlavi\", \"words\": \"junbîtan\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Pahlavi word is genuine. MacKenzie's Concise Pahlavi Dictionary has 'jumbidan, jumb- [ywmb-ytn' | N ~] move', with jumbēnīdan 'to cause to move', jumbišn 'motion', jumbāgīh 'motion' and jumbīhistan 'to be moved'; Manichaean MP has jwmb-. Nourai's 'junbîtan' is the Pazand/Book-Pahlavi reading of the same ywmb-ytn': n for the nasal before b (as Nyberg's Pazand junb-) and the older -tan for MacKenzie's -īdan. Whose root it is, though, is another matter: Cheung (Etymological Dictionary of the Iranian Verb) sets up a separate Iranian root *ja(m)b/p 'to move, wander, rove' (MMP jwmb-, BMP ywmb-, Sogdian γʾβ- 'to wander, travel', Chorasmian γʾβ- 'to go slowly'), and Wiktionary reconstructs Proto-Iranian *Hyámbdi 'to move around' from PIE *h₃yebʰ- 'to enter into' — an initial *y- (> Persian j-), not *gʷ-. Mann alone (Nourai's reference) links the word to a European 'jump' group. So the box is right about the word and about its Persian continuation, and only doubtful about its ancestry.\",\n \"derivation_fa\": \"واژهٔ پهلوی اصیل است. مکنزی در فرهنگ کوچک پهلوی آورده است: «jumbīdan, jumb- [ywmb-ytn'] جنبیدن»، همراه با jumbēnīdan «جنباندن»، jumbišn «جنبش»، jumbāgīh «حرکت» و jumbīhistan «جنبانده شدن»؛ در فارسی میانهٔ مانوی نیز jwmb- هست. صورتِ «junbîtan» نورایی همان ywmb-ytn' است که به شیوهٔ پازند خوانده شده (n به جای m پیش از b، چنان‌که نیبرگ junb- می‌آورد) و پایانهٔ کهن‌تر -tan را نگاه داشته است. اما دربارهٔ ریشه: چونگ ریشهٔ ایرانیِ جداگانهٔ *ja(m)b/p «جنبیدن، گشتن» را می‌نهد (سغدی γʾβ- «سفر کردن، گشتن»، خوارزمی γʾβ-) و ویکی‌واژه ایرانیِ آغازین *Hyámbdi از *h₃yebʰ- هندواروپایی را بازمی‌سازد — یعنی آغازهٔ *y (که در فارسی j می‌دهد) نه *gʷ. تنها مان (منبعِ خودِ نورایی) این واژه را به گروهِ اروپاییِ «جستن» می‌بندد. پس خانه در خودِ واژه و در ادامهٔ فارسی‌اش درست است و تنها در نیاکِ آن جای تردید دارد.\",\n \"sources\": [W_WIKT_JONB],\n \"ref_check\": [{\"ref\": \"MON:1244\", \"status\": \"not_found\", \"note\": \"Mo'in's page could not be checked: the local Mo'in OCR (MON_part1/2.txt) has no جنبیدن headword — the word occurs only inside other entries (e.g. lines 81144, 41167) — and the files carry no page numbers, so p.1244 could not be located. Mo'in's Pahlavi bracket for جنبیدن is the likely support, since MacKenzie's jumbīdan agrees with it.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"s.v. jumbidan (PHD.txt line 414)\", \"stance\": \"supports\", \"note\": \"'jumbāgīh [ywmb'kyh] motion. jumbēnīdan, jumbēn- [ywmbyn-ytn'] (cause to) move. jumbidan, jumb- [ywmb-ytn' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- be moved.'\"},\n   {\"src\": \"NYB\", \"where\": \"II, s.v. yumbišnēh (NYB_vol2_glossary.txt line 4456)\", \"stance\": \"supports\", \"note\": \"'Paz. junb- \\\"to move\\\", v.n. junbašn; junbā \\\"mover\\\" (SGV); NP junbīdan; cf. MPrth ywb- \\\"to lament\\\" ... it would have been better to correct it to ywnb- = Paz. NP' — Nyberg's Pazand junb- is exactly Nourai's spelling.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *ja(m)b/p (CHEUNG.txt lines 14334-14360)\", \"stance\": \"partial\", \"note\": \"'*ja(m)b/p ? \\\"to move, wander, rove, crawl?\\\" MIDDLE PERSIAN: MMP jwmb-, BMP ywmb- /jumb-/ \\\"to move\\\" ... SOGDIAN: γʾβ- \\\"to wander, travel, rove\\\"' — the MP verb is confirmed, but under an Iranian root of its own, with no gʷem- connection.\"}\n ]\n},\n{\n \"id\": 16, \"lang\": \"Persian\", \"words\": \"jonbîdan «جنبیدن» (also جنبش ، جنبنده ، جنبان)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Pahlavi → Persian step is beyond doubt: MP jumbīdan (ywmb-ytn') continues directly as NP جنبیدن jonbīdan (classically junbīdan), present stem جنب- jonb-, with the usual m ~ n fluctuation before b in the Persian script tradition. The derivatives in the box are the regular ones: جنبش = present stem + the verbal-noun suffix -iš (like کوشش, روش); جنبنده = present stem + participial -anda, 'that which moves, a living creature' (Qur'anic دابّه is rendered by it); جنبان = present stem + -ān, 'moving, shaking', familiar from منارجنبان of Isfahan. Nourai's references support this much (Mann p.425 himself cites 'Per. jumbam, -īdan'). What remains open is the ancestry: Cheung 2007 files the verb under an Iranian root *ja(m)b/p 'to move, wander' with Sogdian γʾβ-, and Wiktionary derives it from Proto-Iranian *Hyámbdi < PIE *h₃yebʰ- 'to enter into'; on either view it has nothing to do with gʷem- 'to come', and the chart's ultimate root attachment fails (see #14).\",\n \"derivation_fa\": \"پیوندِ پهلوی به فارسی جای تردید ندارد: jumbīdan فارسی میانه (ywmb-ytn') مستقیماً «جنبیدن» فارسی نو شده است، با ستاک حالِ «جنب-» و همان نوسانِ همیشگیِ m ~ n پیش از b در خط فارسی. مشتق‌های داخل خانه هم کاملاً قاعده‌مندند: «جنبش» = ستاک حال + پسوند اسم‌مصدرسازِ -ش (مانند کوشش و روش)؛ «جنبنده» = ستاک حال + -نده، به معنای «آنچه می‌جنبد، جانور» (برابرِ «دابّه» در ترجمه‌های قرآن)؛ «جنبان» = ستاک حال + -ان، چنان‌که در «منارجنبان» اصفهان. تا همین‌جا منابعِ خودِ نورایی هم پشتیبان‌اند (مان در ص ۴۲۵ خودش «Per. jumbam, -īdan» را آورده). آنچه ناروشن می‌ماند نیاکِ واژه است: چونگ (۲۰۰۷) آن را زیر ریشهٔ ایرانیِ *ja(m)b/p «جنبیدن، گشتن» با سغدیِ γʾβ- می‌آورد و ویکی‌واژه از ایرانیِ آغازین *Hyámbdi و *h₃yebʰ- هندواروپایی می‌گیرد؛ بنا بر هر دو، این واژه با gʷem- «آمدن» بستگی ندارد و انتسابِ نمودار به ریشهٔ Gwa نادرست است.\",\n \"sources\": [W_WIKT_JONB],\n \"ref_check\": [\n   {\"ref\": \"MON:1244\", \"status\": \"not_found\", \"note\": \"same as node #15: the OCR'd Mo'in on disk has no جنبیدن headword and no page numbers, so the cited page could not be read; the claim (Pahlavi junbītan > NP jonbīdan) is nevertheless what MacKenzie and Nyberg give.\"},\n   {\"ref\": \"IEC:425\", \"status\": \"partial\", \"note\": \"Mann p.425 does cite 'Per. jumbam -īdan, intr. \\\"move, stir\\\"' under ǵhumbo — so the reference supports the Persian word being tied to that lemma, but the lemma is not a branch of gʷā- (see node #14).\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *ja(m)b/p, NWIR section\", \"stance\": \"contradicts\", \"note\": \"'NP junbīdan/junb- \\\"to move, stir, shake [intr.]\\\", Awrom. jimay-/jim-, Gur. -jim-, Awrom. jimnay-/jumn- (caus.) \\\"to rock (a cradle)\\\", NP junbān (ptc.) \\\"moving, shaking\\\"' — Cheung's Iranian root, not gʷem-; he even lists Nourai's جنبان.\"},\n   {\"src\": \"PHD\", \"where\": \"s.v. jumbidan\", \"stance\": \"supports\", \"note\": \"'jumbidan, jumb- [ywmb-ytn' | N ~] move' — the 'N ~' means the New Persian form is identical, exactly the arrow drawn here.\"},\n   {\"src\": \"HRN\", \"where\": \"grep of HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no article on junbīdan (the index entries around no. 1059 are nihuften/nuhuften); Hübschmann's Persische Studien likewise yields nothing for junb-/jumb-.\"},\n   {\"src\": \"MON\", \"where\": \"grep of MON_part1/2.txt\", \"stance\": \"silent\", \"note\": \"the OCR contains جنبیدن only inside other definitions (e.g. 'جنبیدن، حرکت کردن، لرزیدن' line 81144), not as a headword with its etymological bracket.\"}\n ]\n}\n]\n\ne2nodes = [\n{\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"vi-gâthô\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Bartholomae's Altiranisches Wörterbuch has 'vi-gāθ- f. \\\"Einsenkung, Schlucht\\\"' ('sinking-in, ravine'), attested in the accusative plural in Yašt 19.31 (vīgāθō ... kaofanąm, the gorges of the mountains); the word is vī- 'apart, asunder' (Nourai's cross-reference to Wi is right: Av. vī- = PIE *wi-) + the root noun gāθ- of gā(d)-/gāh- 'to sink, plunge', the exact Iranian match of Sanskrit vi-gāha-. Pokorny p.465 quotes it in that very form: 'Avestan Akk. Pl. vi-gāθō \\\"canyon, gorge, gulch, ravine\\\" (: Old Indic vi-gāha-)'. Nourai's -ô is the accusative-plural ending -ō that Pokorny prints, so the form is faithfully taken over, and 'ravine, canyon' is the right gloss.\",\n \"derivation_fa\": \"بارتولومه در فرهنگ ایرانی باستان مدخلِ «vi-gāθ- مؤنث، \\\"فرورفتگی، درّه\\\"» را دارد که در یشت ۱۹ بند ۳۱ به صورت رایی جمع (vīgāθō ... kaofanąm، درّه‌های کوه‌ها) گواهی شده است؛ واژه از پیشوند vī- «جدا، از هم» (ارجاع نورایی به Wi درست است: vī- اوستایی همان *wi- هندواروپایی است) و اسمِ ریشه‌ایِ gāθ- از ستاکِ gā(d)-/gāh- «فرو رفتن» ساخته شده و برابرِ دقیقِ vi-gāha- سنسکریت است. پوکورنی نیز در ص ۴۶۵ همین صورت را می‌آورد. پایانهٔ -ô در نوشتهٔ نورایی همان نشانهٔ رایی جمع است که پوکورنی چاپ کرده؛ پس صورت و معنا هر دو درست‌اند.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"POK:465\", \"status\": \"supports\", \"note\": \"POK_full.txt line ~38352: 'Avestan Akk. Pl. vi-gaθō \\\"canyon, gorge, gulch, ravine, abyss, steep narrow valley carved by running water\\\" (: Old Indic vi-gāha-)' under the lemma gʷādh-.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. vi-gāθ- (BRT.txt line 23913)\", \"stance\": \"supports\", \"note\": \"'j. vi-gāθ- f. \\\"Einsenkung, Schlucht\\\": ... morəzat kaofanąm Yt.19.31' — Bartholomae's own entry, with the Yašt citation.\"},\n   {\"src\": \"WLD\", \"where\": \"WP I 665 (WLD_Bd1_pages.txt line 62996 ff.)\", \"stance\": \"partial\", \"note\": \"Walde-Pokorny's gʷādh- article ('gʷādh- \\\"eintauchen, untersinken\\\". Ai. gāhate \\\"taucht, dringt ein\\\" ... gr. bēssa dor. bassa \\\"Talgrund, Schlucht\\\" ...') does not yet cite the Avestan word; Pokorny added vi-gāθō only in the 1959 IEW.\"},\n   {\"src\": \"KNT\", \"where\": \"-\", \"stance\": \"silent\", \"note\": \"Kent's Old Persian lexicon has no corresponding OP form.\"}\n ]\n},\n{\n \"id\": 2, \"lang\": None, \"words\": \"\", \"verdict\": \"unverified\",\n \"derivation\": \"Empty pass-through box: on the printed page (data/verification/sources/refs/ocr/BOOK/203.png) the rectangle to the right of the Avestan box in the Gwadh chart is drawn but left blank — no language, no reference, no word. The extraction is faithful and there is nothing to verify; by the layout of the other charts the slot was meant for a Persian reflex of vi-gāθ-, which Persian does not in fact preserve.\",\n \"derivation_fa\": \"خانهٔ خالیِ واسط: در صفحهٔ چاپی، مستطیلِ کنارِ جعبهٔ اوستایی در نمودار Gwadh کشیده شده اما سفید مانده است؛ نه نام زبان دارد، نه ارجاع و نه واژه. استخراج امین بوده و چیزی برای بررسی نیست. به قرینهٔ چیدمانِ دیگر نمودارها، این خانه جای بازتابِ فارسیِ vi-gāθ- بوده که در فارسی بازمانده‌ای ندارد.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_found\", \"note\": \"the node carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 465\", \"stance\": \"silent\", \"note\": \"Pokorny lists no Iranian continuation of gʷādh- beyond the Avestan word.\"},\n   {\"src\": \"MON\", \"where\": \"-\", \"stance\": \"silent\", \"note\": \"nothing printed in the box to look up.\"}\n ]\n},\n{\n \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"gâhate; vi-gâha\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit gā́hate (RV+) is a middle present 'plunges into, dives, bathes in, penetrates', the Indic match of Avestan gāθ-; its participle gāḍha- means 'deep, dense'. vi-gāha- m. is the nominal derivative 'plunging into, depth' (with vi- 'apart, through'), the exact counterpart of Avestan vi-gāθ-. Pokorny p.465 opens the article with them: 'Old Indic gāhate \\\"dives, permeates, soaks\\\", participle gāḍha-h \\\"deep, dense, tight\\\", gāha-h \\\"depth, the interior\\\"'. Nourai's gloss 'immersed' for gāhate is a little loose — it is an active-sense middle, 'he plunges' — and 'depth' for vi-gāha is right.\",\n \"derivation_fa\": \"gā́hate سنسکریت (از ریگ‌ودا به بعد) فعلی است در وجهِ میانه به معنای «فرو می‌رود، شنا می‌کند، نفوذ می‌کند» و برابرِ هندیِ gāθ- اوستایی است؛ صفتِ مفعولیِ آن gāḍha- «ژرف، انبوه» است. vi-gāha- نیز اسمِ مشتق به معنای «فرورفتن، ژرفا» است و دقیقاً هم‌ساختِ vi-gāθ- اوستایی. پوکورنی مقالهٔ ص ۴۶۵ را با همین صورت‌ها آغاز می‌کند. تنها نکته آنکه معنای «immersed» که نورایی برای gāhate نوشته اندکی نادقیق است؛ فعل معنای فاعلی دارد: «فرو می‌رود». در مجموع ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"POK:465\", \"status\": \"supports\", \"note\": \"POK_full.txt (lemma gʷādh-, p.465): 'Old Indic gāhate \\\"dives, permeates, soaks\\\", participle gāḍha-h \\\"deep, dense, tight\\\", gāha-h \\\"depth, the interior\\\"; ... vi-gāha-'.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"WP I 665\", \"stance\": \"supports\", \"note\": \"'Ai. gāhate \\\"taucht, dringt ein\\\", ptc. gadha- \\\"tief, stark, fest\\\", gāha-h \\\"Tiefe, das Innere\\\" ... ai. gāhana-, gāhvara- \\\"tief, dicht\\\", n. \\\"Tiefe, Abgrund, Dickicht\\\"' (WLD_Bd1_pages.txt line 63000).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins gʷadh-\", \"stance\": \"partial\", \"note\": \"Watkins keeps only the Greek material and calls the root 'Possible'; he does not cite the Sanskrit, though it is the backbone of Pokorny's article.\"}\n ]\n},\n{\n \"id\": 4, \"lang\": \"Greek\", \"words\": \"bussos 2\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Greek byssos (βυσσός) 'the depth, especially of the sea' is real, and Nourai's '2' correctly keeps it apart from the homonym býssos 'fine linen', a Semitic loan (Hebrew būṣ; Klein s.v. byssus). Pokorny derives it from the zero grade *gʷudh-yo-, with β for the expected γ taken over from βῆσσα 'wooded glen', and Watkins agrees: 'Suffixed variant form *gʷdh-yo- in Greek bussos, bottom of the sea: ABYSS' — but he prefixes the whole root with 'gʷadh-. To sink. Possible root.' Modern Greek etymology is more sceptical still: Beekes treats the βαθύς / βένθος / βυσσός / βυθός group as formally irregular and probably Pre-Greek, and Wiktionary's entry for βυσσός says only 'alternative form of βυθός', with no PIE root at all. So the derivation is the standard handbook one that Nourai reports, but it is not secure.\",\n \"derivation_fa\": \"βυσσός یونانی به معنای «ژرفا، به‌ویژه ژرفای دریا» واژه‌ای واقعی است و شمارهٔ «۲» که نورایی گذاشته درست آن را از هم‌آوایش βύσσος «کتانِ نازک» جدا می‌کند که وام‌واژه‌ای سامی است (عبری būṣ؛ کلاین). پوکورنی آن را از درجهٔ صفرِ *gʷudh-yo- می‌گیرد و β آغازین را قیاسی از βῆσσα «درّه» می‌داند، و واتکینز هم همین را می‌آورد، اما خودِ ریشه را «ریشهٔ محتمل» می‌خواند. ریشه‌شناسیِ امروزیِ یونانی محتاط‌تر است: بیکس گروهِ βαθύς/βένθος/βυσσός را از نظر ساختاری بی‌قاعده و احتمالاً پیش‌یونانی می‌داند و ویکی‌واژه βυσσός را تنها «گونهٔ دیگرِ βυθός» می‌نامد بی‌آنکه ریشه‌ای هندواروپایی بدهد. پس گزارش نورایی همان گزارشِ کتاب‌های مرجع است، ولی این پیوند قطعی نیست: با احتیاط پذیرفتنی است.\",\n \"sources\": [W_WIKT_BUSSOS],\n \"ref_check\": [{\"ref\": \"AHD:1519\", \"status\": \"supports\", \"note\": \"Watkins (AHD_watkins1985.txt line 540): 'gʷadh-. To sink. Possible root. ... 3. Suffixed variant form *gʷdh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gʷādh- 465.]' — p.1519 is the appendix page for this root in the 1975 AHD.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 465\", \"stance\": \"supports\", \"note\": \"'zero grade bythos, byssos \\\"the depth, esp. of the sea\\\" with β instead of γ after bēssa'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. abyss, byssus\", \"stance\": \"partial\", \"note\": \"'abyss ... fr. Gk. abyssos ... fr. a- and byssos, \\\"depth, bottom\\\", which is related to bythos' — Klein relates byssos to bythos but offers no IE root; his byssus entry shows the unrelated Semitic homonym.\"},\n   {\"src\": \"WLD\", \"where\": \"WP I 665\", \"stance\": \"silent\", \"note\": \"the older Walde-Pokorny article cites only Greek bēssa/bassa 'Talgrund, Schlucht' for this root, not byssos.\"}\n ]\n},\n{\n \"id\": 5, \"lang\": \"Latin\", \"words\": \"abyssus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek ábyssos, feminine adjective 'bottomless' (a- privative + byssos) used elliptically for '(the) bottomless (deep)', was taken over as Latin abyssus. Ernout-Meillet: 'abyssus, -ī f.: = gr. ábyssos \\\"abîme\\\". Nom attesté avant les Pères de l'Église. A passé par l'intermédiaire de l'église sous une forme savante dans les langues romanes, qui attestent également un doublet populaire *abismus'. The vehicle was the Septuagint, where ábyssos renders Hebrew tehôm 'the deep' (Gen. 1:2), and then the Vulgate and Christian Latin; the popular Vulgar Latin doublet *abismus gave Old French abisme, English abysm.\",\n \"derivation_fa\": \"صفتِ مؤنثِ یونانیِ ábyssos «بی‌ته» (پیشوند نفیِ a- + byssos «ژرفا») که به‌تنهایی و به‌جای «ژرفای بی‌پایان» به کار می‌رفت، به لاتین abyssus راه یافت. ارنو و مِیه می‌نویسند: «abyssus مؤنث = ábyssos یونانی \\\"مغاک\\\"؛ پیش از پدرانِ کلیسا هم گواهی شده و از راه کلیسا به صورتی عالمانه وارد زبان‌های رمانس شده، در کنارِ دوگانهٔ عامیانهٔ *abismus». مسیرِ انتقال ترجمهٔ سبعینی است که در آن ábyssos برابرِ «تِهوم» عبری (پیدایش ۱:۲) نشسته و سپس وولگاتا و لاتینِ مسیحی؛ گونهٔ عامیانهٔ *abismus هم abisme فرانسویِ کهن و abysm انگلیسی را داده است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins's gʷadh- entry ends the chain at ABYSS via Greek bussos; the AHD index line reads 'ABYSS gʷadh-'.\"}],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. abyssus (LAT.txt)\", \"stance\": \"supports\", \"note\": \"'abyssus, -ī f.: = gr. abussos \\\"abime\\\". Nom attesté avant les Pères de l'église. A passé par l'intermédiaire de l'église sous une forme savante dans les l.rom. qui attestent également un doublet populaire *abismus'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. abyss\", \"stance\": \"supports\", \"note\": \"'L. abyssus, \\\"bottomless pit\\\", fr. Gk. abyssos (scil. limnē), \\\"bottomless, unfathomed (pool)\\\"'.\"}\n ]\n},\n{\n \"id\": 6, \"lang\": \"English\", \"words\": \"abyss\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English abyss is a late-14th-century learned borrowing of Late Latin abyssus (the older English word, abysm, came through Old French abisme from the Vulgar Latin doublet *abismus). Klein: 'abyss, n. — L. abyssus, \\\"bottomless pit\\\", fr. Gk. abyssos'. Nourai's gloss 'a bottomless void or pit, hell' is the Biblical and Miltonic sense: in the Vulgate and the English Bibles the abyssus is both the primeval deep of Genesis and the pit of Revelation, which is where the 'hell' sense comes from.\",\n \"derivation_fa\": \"«abyss» انگلیسی وام‌واژه‌ای عالمانه از اواخر سدهٔ چهاردهم است، برگرفته از abyssus لاتینِ متأخر؛ صورتِ کهن‌ترِ انگلیسی یعنی abysm از راه abisme فرانسویِ کهن و از گونهٔ عامیانهٔ *abismus آمده بود. کلاین می‌نویسد: «abyss از abyssus لاتین \\\"چاهِ بی‌ته\\\"، از abyssos یونانی». معنایی که نورایی نوشته («مغاکِ بی‌ته، دوزخ») همان کاربردِ کتاب‌مقدسی و میلتونی است: در وولگاتا و ترجمه‌های انگلیسیِ کتاب مقدس، abyssus هم ژرفای آغازینِ سفر پیدایش است و هم چاهِ مکاشفه، و معنای «دوزخ» از همین‌جا آمده است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD index (AHD_watkins1985.txt line 1208): 'ABYSS gʷadh-'; the root entry names ABYSS as the English outcome of Greek bussos.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. abyss (KLN_1966.txt offset 87830)\", \"stance\": \"supports\", \"note\": \"'abyss, n. — L. abyssus, \\\"bottomless pit\\\", fr. Gk. abyssos (scil. limnē) ... fr. a- (see priv. pref. a-) and byssos, \\\"depth, bottom\\\" ... Cp. abysm.'\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Abyss (SKT.txt line 287)\", \"stance\": \"supports\", \"note\": \"'Abyss, a bottomless gulf. (L. — Gk.) L. abyssus. — Gk. abyssos, bottomless. — Gk. a-, neg. pref., and byssos, depth, akin to Bathos.'\"}\n ]\n}\n]\n\ndata = {\n \"pdf_page\": 203,\n \"book_page\": 173,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Gwa, Gwâ, Gwen 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gʷem- / *gʷeh₂- 'to go, come, step' (Pokorny 463-465 gʷā-, gʷem-; Watkins gʷā-)\",\n   \"note\": \"The root box is right on all three counts. Pokorny's lemma reads 'Root / lemma: gʷā-, gʷem-, Meaning: to go, come' with 'Page(s): 463-465', so 'POK:463' is the first page of exactly this article, and Nourai's gloss 'to walk, to step, to come, to go' reproduces it. Watkins's appendix has 'gʷā-. Also gʷem-. To go, come. ... [Pok. gʷā- 463.]'. The three-part name needs one caveat: 'Gwen 2' is Nourai's own label, not a Pokorny lemma — Pokorny's gʷen- (p.473) is 'woman', which Nourai keeps separately as Gwen 1 (book p.178), and the -en- of Latin veniō is called analogical by Pokorny himself ('perhaps with analogical -en- after the forms as Latin venio'); page 208 of the pdf accordingly redirects 'Gwen 2' to 'Gwa'. Within the chart, the Greek, Latin, Germanic and English boxes are all straight out of Watkins and are right. Three things need correcting. (1) Node #1 mixes languages: gemton, gimsenin and gemmons are Old Prussian, taken with their glosses from the Baltic paragraph of Pokorny p.465, and are printed in a box headed 'Avestan / Old Persian'. (2) Node #7's French basse and bassin do not belong to this root at all — basse is Late Latin bassus 'low' (origin unknown, kept as a separate non-IE headword by Watkins), bassin is Vulgar Latin *baccinum 'water vessel'; the French word Nourai needed is base, and with it the Persian باسن of node #8 (a real French loan, per Dehkhoda) drops out of the root as well. (3) Node #14's 'Ğhumbo' is copied verbatim from Mann IEC 425, but Mann files it under palatal ǵhūb- 'stir, move', not under gʷem-, and Cheung 2007 and Wiktionary derive Persian جنبیدن from an Iranian *ja(m)b/p / *Hyámbdi (PIE *h₃yebʰ-) instead — so the whole jonbīdan branch hangs off the wrong root. One printing slip: node #10 prints Latin 'venîr' for venîre.\",\n   \"note_fa\": \"خودِ ریشه کاملاً درست است: پوکورنی مادهٔ «gʷā-, gʷem- به معنای رفتن و آمدن» را در صفحات ۴۶۳–۴۶۵ آورده و ارجاع POK:463 نخستین صفحهٔ همین مقاله است؛ واتکینز نیز در پیوستِ AHD همین را می‌گوید. تنها نکته آنکه «Gwen 2» نامی است که خودِ نورایی ساخته و مادهٔ پوکورنی نیست — gʷen- در پوکورنی (ص ۴۷۳) به معنای «زن» است که نورایی آن را جداگانه Gwen 1 نامیده — و پوکورنی -en- در veniō لاتین را قیاسی می‌داند. خانه‌های یونانی، لاتین، ژرمنی و انگلیسیِ نمودار همه درست‌اند، اما سه لغزش هست: ۱) در خانهٔ ۱ سه واژهٔ gemton و gimsenin و gemmons پروسیِ کهن‌اند نه اوستایی/پارسی باستان؛ ۲) در خانهٔ ۷ واژه‌های فرانسویِ basse و bassin اصلاً به این ریشه نمی‌رسند (basse از bassus لاتینِ متأخر و bassin از *baccinum) و در نتیجه «باسن» فارسی — که به‌درستی وام‌واژهٔ فرانسوی است — نیز از این ریشه بیرون می‌افتد؛ ۳) «Ğhumbo» در خانهٔ ۱۴ عیناً از مانِ ص ۴۲۵ گرفته شده اما مان آن را زیر ǵhūb- می‌آورد، و چونگ و ویکی‌واژه «جنبیدن» را از ریشهٔ ایرانیِ *ja(m)b/p (و *h₃yebʰ- هندواروپایی) می‌گیرند؛ پس کلِ شاخهٔ «جنبیدن» به ریشهٔ نادرست بسته شده است. یک خطای چاپی هم هست: در خانهٔ ۱۰ به‌جای venîre نوشته شده venîr.\",\n   \"sources\": [W_WIKT_GWEM],\n   \"ref_check\": [{\"ref\": \"POK:463\", \"status\": \"supports\", \"note\": \"POK_full.txt (line 38525 area): 'Root / lemma: gʷā-, gʷem-; Meaning: to go, come; ... References: WP. I 675 ff. ... Page(s): 463-465' — Nourai's page number is the article's first page and his gloss is Pokorny's.\"}],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"WP I 675 ff. (WLD_Bd1_pages.txt lines 64040-64060)\", \"stance\": \"supports\", \"note\": \"the same root, with the Baltic 'be born' group attached only 'unter Annahme einer Bed.-Entwicklung \\\"(zur Welt) kommen\\\" = \\\"geboren werden\\\"' (Bechtel, Endzelin, Mühlenbach-Endzelin).\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷā- (AHD_watkins1985.txt line 537)\", \"stance\": \"supports\", \"note\": \"'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman ... 2. Suffixed form *gʷ(e)m-yo- in Latin venire ... 3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein ... [Pok. gʷā- 463.]' — the four upper boxes of the chart are this entry in order.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 10.48 'COME'\", \"stance\": \"supports\", \"note\": \"'For the Latin, Romance, Germanic, and Indo-Iranian words, representing IE *gʷem- ...' with Goth. qiman, OE cuman, Lat. uenio, Gk. bainō, Skt. gam-, Av. (ā-)jam- in one table.\"}\n   ],\n   \"nodes\": e0nodes\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Gwadh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gʷādʰ- 'to sink, submerge' (Pokorny 465; Watkins gʷadh-, 'possible root')\",\n   \"note\": \"Correct as a report of the handbooks: Pokorny's lemma is 'Root/lemma: gʷādh-, Meaning: to sink, submerge ... Page(s): 465', built on Sanskrit gāhate, Avestan vi-gāθō, Greek bēssa/bathys/byssos and Old Irish báidim; Walde-Pokorny I 665 has the same root with the same gloss ('eintauchen, untersinken'). Nourai's 'to sink' and 'POK:465' are exact. Two caveats worth recording: Watkins prints 'gʷadh-. To sink. Possible root.', i.e. the AHD itself marks it as uncertain, and the Greek members of the family (βαθύς, βένθος, βυσσός, βυθός) are formally irregular — Beekes and current Greek etymology regard them as probably Pre-Greek. The chart's four content boxes (Avestan, Sanskrit, Greek, Latin/English) each check out individually, the Greek one with that reservation.\",\n   \"note_fa\": \"این ریشه، چنان‌که کتاب‌های مرجع می‌گویند، درست گزارش شده است: پوکورنی مادهٔ gʷādh- «فرو رفتن، غرق شدن» را در ص ۴۶۵ آورده و آن را بر پایهٔ gāhate سنسکریت، vi-gāθō اوستایی، βῆσσα و βαθύς و βυσσός یونانی و báidim ایرلندیِ کهن ساخته است؛ والده-پوکورنی (ج۱ ص ۶۶۵) نیز همین ریشه را با همین معنا دارد. پس «to sink» و ارجاع POK:465 هر دو دقیق‌اند. دو ملاحظه را باید ثبت کرد: واتکینز خودش می‌نویسد «gʷadh- فرو رفتن. ریشهٔ محتمل»، یعنی AHD آن را قطعی نمی‌داند؛ و اعضای یونانیِ این خانواده از نظر آوایی بی‌قاعده‌اند و ریشه‌شناسیِ امروزی (بیکس) آن‌ها را احتمالاً پیش‌یونانی می‌شمارد. چهار خانهٔ نمودار جداگانه درست‌اند، با همین احتیاط دربارهٔ خانهٔ یونانی.\",\n   \"sources\": [W_WIKT_BUSSOS],\n   \"ref_check\": [{\"ref\": \"POK:465\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 38344-38377: 'Root /lemma: gʷādh-; Meaning: to sink, submerge; Material: Old Indic gāhate ... Avestan Akk. Pl. vi-gaθō ... zero grade bythos, byssos ... References: WP. I 665 ... Page(s): 465'.\"}],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"WP I 665 (WLD_Bd1_pages.txt line 62996)\", \"stance\": \"supports\", \"note\": \"'gʷādh- \\\"eintauchen, untersinken\\\". Ai. gāhate \\\"taucht, dringt ein\\\" ... gr. bēssa dor. bassa \\\"Talgrund, Schlucht\\\"; air. baidim \\\"tauche unter, ertranke\\\"' — the same root, though without the Avestan and byssos material.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷadh- (line 540)\", \"stance\": \"partial\", \"note\": \"'gʷadh-. To sink. Possible root.' — supports the root but explicitly labels it uncertain, which Nourai's box does not.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann\", \"stance\": \"silent\", \"note\": \"no corresponding lemma was found in Mann's dictionary for this root.\"}\n   ],\n   \"nodes\": e2nodes\n  }\n ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-203.json\"\nwith open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build203.py && python3 -m json.tool data/verification/page-203.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 203"
}
```


### [2026-09-06T02:40:33.965Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-203.json
JSON OK
nodes verified: 22/22
node verdicts: {'disputed': 3, 'unverified': 2, 'confirmed': 11, 'plausible': 5, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'partial': 4, 'not_found': 7, 'not_checked': 1}
books consulted: {'supports': 30, 'contradicts': 4, 'silent': 15, 'partial': 6} | by book: {'KLN': 10, 'SKT': 6, 'POK': 5, 'AHD': 5, 'WLD': 4, 'MON': 4, 'BRT': 3, 'KNT': 2, 'FSD': 2, 'BQT': 2, 'LAT': 2, 'PHD': 2, 'CHEUNG': 2, 'WEB': 1, 'ARY': 1, 'SYN': 1, 'IEC': 1, 'NYB': 1, 'HRN': 1}
```


## [2026-09-06T02:40:44.013Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-203.json'))\nfor e in d['entries']:\n    print(e['entry'],e['root'],e['verdict'],'nodes',len(e['nodes']))\n    for n in e['nodes']:\n        print('  #%d'%n['id'],n['verdict'],'|',(n['words'] or '(empty)')[:40],'| fa',len(n['derivation_fa']),'| refs',len(n['ref_check']),'| cons',len(n['consulted']))\n\" && git status --short"
}
```


### [2026-09-06T02:40:45.670Z] TOOL RESULT

```
0 Gwa, Gwâ, Gwen 2 confirmed nodes 16
  #1 disputed | aiwi-gaiti; ni-jâma; gemton; gimsenin; g | fa 908 | refs 2 | cons 3
  #2 unverified | (empty) | fa 370 | refs 1 | cons 2
  #3 confirmed | bainein; dia-bainein; akro-bates | fa 590 | refs 2 | cons 2
  #4 confirmed | (empty) | fa 416 | refs 1 | cons 2
  #5 confirmed | «دیابت ، آکروبات» | fa 504 | refs 2 | cons 2
  #6 confirmed | diabetes, acrobat | fa 371 | refs 1 | cons 2
  #7 disputed | basse, bassin | fa 715 | refs 1 | cons 3
  #8 plausible | bâsan «باسن» | fa 646 | refs 1 | cons 3
  #9 plausible | base, basic | fa 575 | refs 1 | cons 2
  #10 transcription_suspect | venîr | fa 488 | refs 1 | cons 3
  #11 confirmed | avenue, event, prevent, invent | fa 452 | refs 1 | cons 3
  #12 confirmed | kuman | fa 447 | refs 1 | cons 2
  #13 confirmed | come, become, welcome, income | fa 462 | refs 1 | cons 2
  #14 disputed | Ğhumbo | fa 730 | refs 1 | cons 3
  #15 plausible | junbîtan | fa 796 | refs 1 | cons 3
  #16 plausible | jonbîdan «جنبیدن» (also جنبش ، جنبنده ،  | fa 812 | refs 2 | cons 4
2 Gwadh confirmed nodes 6
  #1 confirmed | vi-gâthô | fa 519 | refs 1 | cons 3
  #2 unverified | (empty) | fa 291 | refs 1 | cons 2
  #3 confirmed | gâhate; vi-gâha | fa 465 | refs 1 | cons 2
  #4 plausible | bussos 2 | fa 671 | refs 1 | cons 3
  #5 confirmed | abyssus | fa 553 | refs 1 | cons 2
  #6 confirmed | abyss | fa 489 | refs 1 | cons 2
?? data/verification/page-203.json
```


## [2026-09-06T02:41:04.669Z] AGENT

Page 203 (book p. 173) verified — `data/verification/page-203.json` written, `verify_check.py 203` reports 22/22 nodes, 0 PROBLEM lines.

**Verdicts:** roots 2 confirmed. Nodes: 11 confirmed, 5 plausible, 3 disputed, 1 transcription_suspect, 2 unverified (the two blank pass-through boxes).

**Disputed / flagged**
- **Gwa #1 (Avestan/Old Persian box)** — `gemton`, `gimsenin`, `gemmons` are **Old Prussian**, not Iranian: Nourai copied Pokorny p.465's Baltic paragraph (glosses and all) into an Iranian box; Walde-Pokorny I 675 marks them "apr." Only `aiwi-gaiti` (Bartholomae, "Herzukommen") and `ni-jāma` (Pokorny's reconstruction from Av. nijamayeinti) are Iranian; the added gloss "origin, race" is unsupported (that is *ni-zāta- > نژاد).
- **Gwa #7 (French basse, bassin)** — neither belongs to this root: `basse` < Late Latin *bassus* (unknown origin; Watkins keeps a separate non-IE headword "bassus"), `bassin` < VL *baccinum* < *bacca* (Klein, Etymonline). The word needed here is French *base*; consequently #9 (base, basic) is only *plausible* (right root, wrong French parent), and #8 باسن — a genuine French loan, Dehkhoda: "(فرانسوی) لگن خاصره" — falls outside the root.
- **Gwa #14 (Ğhumbo)** — form and gloss are verbatim Mann IEC 425, but Mann files it under palatal *ǵhūb-* "stir, move", not gʷem-; Cheung 2007 gives Iranian *ja(m)b/p (Sogd. γʾβ-) and Wiktionary PIr *Hyámbdi < PIE *h₃yebʰ-. So the whole جنبیدن branch (#15 Pahlavi jumbīdan, #16 جنبیدن — both real and correctly linked to each other) hangs off the wrong root.
- **Gwa #10 `venîr`** — transcription_suspect, `error_in: book`: the page really prints "venîr" (image archived at `data/verification/sources/refs/ocr/BOOK/203.png`); Latin is *venīre*, and Nourai elsewhere writes -îre (ferîre, scîre, ap-erîre). Faithful extraction, author's typo.

**No extraction errors found** — the JSON matches the printed page everywhere, including the two blank boxes and the Persian scripts.

Nine web pages archived via `fetch_source.py`; local books used: POK, WLD, AHD/Watkins, IEC, SYN, KLN, SKT, FSD, LAT, BRT, KNT, PHD, NYB, CHEUNG, HRN, MON, BQT, ARY. VOP:83 remains unchecked (no copy of Moshiri exists anywhere per refs_online.json); MON:1244 not_found (the local Mo'in OCR has no جنبیدن headword and no page numbers). The file is uncommitted.
