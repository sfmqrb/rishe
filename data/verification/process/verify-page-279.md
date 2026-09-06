# Verification process log — verify-page-279


## [2026-09-06T21:28:41.278Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 279 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-279.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-279.json. Write /home/sfmqrb/git/rishe/data/verification/page-279.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 279` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:28:42.663Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T21:28:43.373Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:28:43.389Z] TOOL RESULT

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


## [2026-09-06T21:28:43.734Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-279.txt"
}
```


### [2026-09-06T21:28:43.753Z] TOOL RESULT

```
1	=== PDF page 279 (book page 249) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ksei 2 : bright  (refs WLD1:501; BRT:541)
4	#1 (parent #0) [Avestan] refs=WLD1:501; BQT:788,1320 | xšae-ta, xšôithmi : bright ; hvare-xšâeta : bright sun ☞Sâwel ; yima-xšâetem : brilliant king ☞Yem ; raoč-xšaena, raoxšna : bright light ☞Leuk ; drafša : (bright) banner
5	  #2 (parent #1) [Persian] refs=BQT:756; MON:1425 | šîd «شید» : bright ; xoršîd «خورشید» : brilliant sun ; Jamšîd «جمشید» : "brilliant king", a male name ; draxšîdan «درخشیدن» : to shine ; rowšan «روشن» : bright ; drafšîdan «درفشیدن» : to shine | extra: شیده ، مهشید ، رخشیدن ، رخش ، روشنایی ، درفش ۱
6	  #3 (parent #1) [Avestan] refs=WLD1:501; BQT:1320; SYN:1053 | a-xšae-na : not bright, a dark color, green ☞Ne 1
7	    #4 (parent #3) [Persian] refs=BQT:756; MON:1425; FRS:89 | xašan «خَشَن» : dark blue ; xašîsâr «خَشیسار» : a blue bird with white head | extra: خَشی ، خَشین ، خشینه ، خَشیشار ، خشنسار
8	#5 (parent #0) [Sogdian] refs=SOD:27 | âxs`ynh : green
9	--- entry 1 ---
10	ROOT [Indo-European] Ksei 3 : to settle  (refs POK:626)
11	#1 (parent #0) [Avestan] refs=POK:626 | šaěiti, shiti : living place ; šôithra : land
12	  #2 (parent #1) [None] refs=None | 
13	#3 (parent #0) [Greek] refs=POK:626; AHD:45 | ktizein : to found, establish ; amphi-ktuoness : established around each other ☞Ambhi
14	  #4 (parent #3) [English] refs=KLN:65; AHD | amphictyony : confederation of states in ancient Greece
15	--- entry 2 ---
16	ROOT Ksengio -> redirect to Ghengh
17	
```


## [2026-09-06T21:28:46.756Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-279.json",
 "description": "Read source JSON for page 279"
}
```


### [2026-09-06T21:28:46.810Z] TOOL RESULT

```
{
  "pdf_page": 279,
  "book_page": 249,
  "entries": [
    {
      "root": {
        "name": "Ksei 2",
        "lang": "Indo-European",
        "refs": "WLD1:501; BRT:541",
        "gloss": "bright"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "WLD1:501; BQT:788,1320",
          "words": [
            {"translit": "xšae-ta, xšôithmi", "gloss": "bright", "script": null},
            {"translit": "hvare-xšâeta", "gloss": "bright sun", "script": null, "see": ["Sâwel"]},
            {"translit": "yima-xšâetem", "gloss": "brilliant king", "script": null, "see": ["Yem"]},
            {"translit": "raoč-xšaena, raoxšna", "gloss": "bright light", "script": null, "see": ["Leuk"]},
            {"translit": "drafša", "gloss": "(bright) banner", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:756; MON:1425",
          "words": [
            {"translit": "šîd", "gloss": "bright", "script": "شید"},
            {"translit": "xoršîd", "gloss": "brilliant sun", "script": "خورشید"},
            {"translit": "Jamšîd", "gloss": "\"brilliant king\", a male name", "script": "جمشید"},
            {"translit": "draxšîdan", "gloss": "to shine", "script": "درخشیدن"},
            {"translit": "rowšan", "gloss": "bright", "script": "روشن"},
            {"translit": "drafšîdan", "gloss": "to shine", "script": "درفشیدن"}
          ],
          "script_extra": "شیده ، مهشید ، رخشیدن ، رخش ، روشنایی ، درفش ۱",
          "note": null,
          "quote": {
            "text": "جهان شد ز گرد سواران بنفش - درخشان سنان و درفشان ۱ درفش ۲",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan",
          "refs": "WLD1:501; BQT:1320; SYN:1053",
          "words": [
            {"translit": "a-xšae-na", "gloss": "not bright, a dark color, green", "script": null, "see": ["Ne 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:756; MON:1425; FRS:89",
          "words": [
            {"translit": "xašan", "gloss": "dark blue", "script": "خَشَن"},
            {"translit": "xašîsâr", "gloss": "a blue bird with white head", "script": "خَشیسار"}
          ],
          "script_extra": "خَشی ، خَشین ، خشینه ، خَشیشار ، خشنسار",
          "note": null,
          "quote": {
            "text": "پیاده همی رفت جویان شکار - خشیسار دید اندر آن رودبار",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:27",
          "words": [
            {"translit": "âxs`ynh", "gloss": "green", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ksei 3",
        "lang": "Indo-European",
        "refs": "POK:626",
        "gloss": "to settle"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:626",
          "words": [
            {"translit": "šaěiti, shiti", "gloss": "living place", "script": null},
            {"translit": "šôithra", "gloss": "land", "script": null}
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
          "refs": "POK:626; AHD:45",
          "words": [
            {"translit": "ktizein", "gloss": "to found, establish", "script": null},
            {"translit": "amphi-ktuoness", "gloss": "established around each other", "script": null, "see": ["Ambhi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:65; AHD",
          "words": [
            {"translit": "amphictyony", "gloss": "confederation of states in ancient Greece", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ksengio",
        "redirect": "Ghengh"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T21:28:47.108Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T21:28:47.146Z] TOOL RESULT

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


## [2026-09-06T21:28:51.791Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['WLD','WLD1','BRT','BQT','MON','SYN','FRS','SOD','POK','AHD','KLN']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-06T21:28:52.221Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-259.json"
}
```


### [2026-09-06T21:28:53.637Z] TOOL RESULT

```
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

WLD1 null

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
```


### [2026-09-06T21:28:53.668Z] TOOL RESULT

```
{
  "pdf_page": 259,
  "book_page": 229,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
    {
      "entry": 0,
      "root": "Kerd 1, Kred",
      "verdict": "confirmed",
      "modern_form": "PIE *ḱḗr, oblique stem *ḱr̥d- (root *ḱerd-) 'heart'; with the compound *ḱred-dʰeh₁- 'to place one's heart, trust'",
      "note": "Pokorny p.579 bottom–580 heads the entry exactly '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’', so Nourai's headword 'Kerd 1, Kred', the language label 'Indo-European' and the gloss 'heart' all reproduce his source correctly; AHD (Watkins) has 'kerd-1. Heart. [Pok. kered- 579.]'. The one substantive caveat concerns the 'kred-' half: Pokorny himself (p.580) says the kred-dhē- 'believe' group is 'nicht hierher' (not to be connected with 'heart'), and Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree; modern standard works (Watkins/AHD, de Vaan 2008 s.v. crēdō, Wiktionary) do connect it, analysing *ḱred-dʰeh₁- as 'to place one's heart'. Nourai therefore follows the newer, now dominant, view — but not the page of Pokorny he cites. The Iranian branch has a further complication that the chart passes over: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, Av. zərəd-, PII *ȷ́ʰā́rd) where *ḱ- is expected, 'unexplained voiced aspiration' (Wiktionary), 'mit init. as if fr. IE gh, due to a blend with some other word' (Buck 251).",
      "note_fa": "ریشهٔ هندواروپایی آغازین *ḱḗr (ستاک غیرفاعلی *ḱr̥d-، ریشهٔ *ḱerd-) به معنی «دل، قلب» است و پوکورنی در ص ۵۷۹–۵۸۰ سرواژه را دقیقاً «kerd-, kērd-, kr̥d-, kred-: Herz» آورده؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ محل بحث بخش kred- است: خودِ پوکورنی در ص ۵۸۰ پیوند kred-dhē- «باور داشتن» را با «دل» رد می‌کند و باک و کلاین و ارنو–مه‌یه نیز همین نظر را دارند، اما واتکینز (AHD)، دِ وان و ویکی‌واژه آن را می‌پذیرند و *ḱred-dʰeh₁- را «دل نهادن» می‌دانند؛ یعنی نورایی از دیدگاه نو پیروی کرده است نه از صفحه‌ای که به آن ارجاع داده. نکتهٔ دیگر آنکه در هندوایرانی به جای *ḱ- انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-، اوستایی zərəd-) که هنوز توضیح قطعی ندارد.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r",
        "https://en.wiktionary.org/wiki/credo%23Latin",
        "https://www.etymonline.com/word/heart"
      ],
      "ref_check": [
        {
          "ref": "POK:579",
          "status": "supports",
          "note": "P
```


## [2026-09-06T21:29:10.507Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls; echo ---; grep -n \"k̑þei\\|kþei\\|ksei\" POK_full.txt | head -40"
}
```


### [2026-09-06T21:29:10.569Z] TOOL RESULT

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
---
48832:Root / lemma: kseip-, kseib- 
48854:Root/ lemma: kseiJo^-{*ghseiJo'^-) 
68484:from kk), /7/cce "Speckseite', Old Icelandic flikki6s.. Middle Low German vlicke6s., "Flicke, 
70834:"Speckseite', Old English ryse/m. "bacon, fat, ; Dutch ru/' lax and dry, e.g. of sand, rough' 
79907:"(abgeschnittene) Speckseite', poltlna'haW, Old Church Slavic po/b. Gen. -^"half, side,
```


## [2026-09-06T21:29:11.226Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"xšaēta\\|xsaeta\\|xšaeta\" BRT.txt | head -30"
}
```


### [2026-09-06T21:29:11.278Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:29:17.269Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '48820,48900p' POK_full.txt"
}
```


### [2026-09-06T21:29:17.318Z] TOOL RESULT

```
Material: Middle Irish crotti. " hunch, harp', nir. emit 6s., altbrit.-gall. c/c/Za'harp', cymr. 
crwthm. " hunch, fiddle, violin', crothi. "belly, uterus, vulva'; 

Lithuanian krut'is^ female breast', /r/77///7e "breast', Latvian kruts^\\\\\, breast'. 

Probably to kreu-^ curve ', see below (s)ker-, (s)kereu-^\.uxy\\ 

References: WP. I 485, 489, Specht Indo Germanic Dekl. 772. 
Page(s): 624 

Root / lemma: kseip-, kseib- 

Meaning: to throw, be thrown 

Material: Old Indie ksipati^ throws, flings ', Kaus. ksepayati, ks/pra-h ' qu'\ck, fast'; with 

voiced-nonaspirated Old Church Slavic osiba-jg, -ti^ avert, prevent; turn away ', russ. 

s/t>atb'\hro\N\ s/My "quick, fast', os/batb'chop, cut, reject', os/batbsja' wander'. 

common Old Indie gh- > ks- : Old pers. gh- > xs- : npers. xs- > s- 

Hence Slavic xs- > s- is of npers. origin. 

References: W P. I 501. 

Page(s): 625 

Root / lemma: ks-en-, ks-es- ks-eu- 
See also: see above S. 585 f. under kes- 
Page(s): 625 

Root/ lemma: kseiJo^-{*ghseiJo'^-) 

Meaning: to sway, swing 

Material: Old Indie ksubhyati, ksobhate {ksubhnoti, -nati) " sways, trembles ', ksobhayati^ 

sets in motion ', ksobha-m. " sway, tremor '; Avestan xsaob-'go into raptures, become 

excited ' {xsufsqn), npers. a-suftan, a-softan^ in Bewegung versetzen ', a-sdi? "perplexity, 

tumult '; 

common Old Indie gh- > ks- : Old pers. gh- > xs- : npers. xs- > s- 

poln. chybac^ swing, move to and fro '; chybkT nimble, agile; graceful; sharp, keen, 
rash, hasty'; kir. chybaty^ be ambivalent, have mixed feelings ', chyba {*ksuba) "lack, fault, 
error' etc. 

common Old Indie gh- > ks- : Slavic gh- > ch- 
References: WP. I 502 f., Trautmann 144. 
Page(s): 625 



Root / lemma: kseud- {*gheud-) 

Meaning: to grind in little pieces 

Material: Old Indie ksodati^ stamps, crushes ', ksoda-m. ' push, stamping, crushing; flour, 

powder, mash ', ksudra-^ sma\\\ low, despicable ', compounds ksodTyas-, ksudra-u. 'mote, 

speck'; common Old Indie gh- > ks- : Slavic gh- > ch- 

Old Bulgarian chudt^ smaW; small, evil, bad', compounds chuzdbjb{: Old Indie ksod/yas- 
)■ 

Machek (Slavia 16, 174) takes as originally meaning ' skinny ' an (Czech chudy' poor, 
bad, lean '), which he consequently would place to Old Indie ksudhyat/" starves' , ksodh- 
uka-^ hungry'. 

Old Church Slavic: xudb 'small, insignificant, scanty' [adj o]; A^t/zoV/" worse'; Russian: xudoj 
'thin, lean, bad, full of holes' [adj o]; A-^ze 'worse' 

Maybe alb. {*ksdda-) holle^ poor, bad, lean ' common Slavic- alb. cM? reading; common 
alb. Italic -d- > -A.
```


## [2026-09-06T21:29:18.152Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 626\" POK_full.txt | head; echo ---; grep -n \"Page(s): 625\\|Page(s): 627\" POK_full.txt | head"
}
```


### [2026-09-06T21:29:18.212Z] TOOL RESULT

```
47237:Page(s): 626 
48966:Page(s): 626 
51227:Page(s): 626 
52364:Page(s): 626-627 
---
48848:Page(s): 625 
48852:Page(s): 625 
48874:Page(s): 625 
48905:Page(s): 625 
48931:Page(s): 627 
48985:Page(s): 627 
49017:Page(s): 627-628 
51984:Page(s): 625 
52073:Page(s): 627 
52338:Page(s): 627
```


## [2026-09-06T21:29:21.429Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '48935,48990p' POK_full.txt"
}
```


### [2026-09-06T21:29:21.488Z] TOOL RESULT

```
Root / lemma: ku-, kus- {*k"'uk"'h-) 

Meaning: to kiss 

Note: (compare bu- S. 103) 

Material: Gr. kuveoj, sKuaaa "kiss' (Greek -ne- infix of the present *Ku-v£-a-[pi]). 

Comments: 

Greek infix -ne- : Hittite infix -nin- which is used, like the more frequent suffix -nu-, in order 

to build the causative of some verbs : hark- "to collapse" harnink- "to throw down", istark- 

"to be ill" istarnink- "to make ill". 

With the stop of the consonant shift in onomatopoeic words of Old Icelandic koss. Old 

English coss. Old High German /ri/s "kiss'. Old Icelandic kyssa. Old English cyssan. Old 

High German kussen^V\ss'\ Gothic kukjan. East Frisian /rJ/r/re"/? seems out of it to be 

reshaped in the baby talk; 

Hittite 3. PI. kuwassanz/" they kiss '. (common -wa- infix of the present in Hittite). 

similar Old Indie cusat/" sucks' , cuscusa' munching the food '. 



References: WP. I 465, Kuiper Nasalpras. 151 . 
Page(s): 626 



Root / lemma: kuak- 

Meaning: croaking, quacking 

Material: Gr. koq^ " of the croaking of the frog ', Latin coaxare "quack' (probably imitation of 

Koa^), German quack, quacken^ from frogs; cackle (duck) etc.', Swedish Dialectal kvaka^ 

cackle like a duck ', Old Icelandic /ri/a/ra "chirp, twitter', russ. kvakatb "quack'. 

Maybe alb. {*kuak) kuak'croak'. 



References: WP. I 468. 
Page(s): 627 



Root / lemma: kuat(h)-
```


## [2026-09-06T21:29:21.785Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '47180,47240p' POK_full.txt; echo ===; sed -n '51190,51230p' POK_full.txt"
}
```


### [2026-09-06T21:29:21.844Z] TOOL RESULT

```
Exit code 1

weave together; chain, net. 

Material: Avestan kata-m. " chamber, storeroom, cellar' (: Gothic hel=>jd), npers. kad 

"house', from which Finnish kota; but about Old Norse /ro/' miserable cottage', kytja 

"cottage'. Old English cc»/"cottage, chamber ' etc. see above S. 393 f.; 

Maybe alb. {*kotu-) /ra/^a "stable, basement, cellar', /ra/i//7o'" house, village'. 

Gothic het^jo^ chamber '; 

Church Slavic kotbCb "cella, nest' etc.; whether "residential pit, hole in the earth' the 
original meaning, can be added: 

Maybe alb. /ro/ec "animal shelter' a Slavic loanword. 

gr. KOTuAri, k6tuAo(; " cavity, hole, empty space, hollow ', further " hollow vessel, bowl, 
goblet'; 

Latin catTnus^ a deep vessel of earthenware, bowl ' (Demin. catillus, out of it Gothic 
katils, German Kesser kettle ', out of it again Old Bulgarian kotbib, Lithuanian katilas) = 
Old English heden^ pots and pans, set of cooking utensils '. 

References: WP. I 383 f., WH. I 176, 182. 
Page(s): 586-587 

Root / lemma: kt^eO)- kt^aO)- {*ghde(i)-) 

Meaning: to acquire, possess 

Material: Old Indie ksayati^ owns, controls ' ( *kt^ai-eti) = Avestan xsayat/' has power, 

force, it rules, disposes of what owns ', xsayo^ power'; Old Indie ksatra-n. "power, rule', 

Avestan ap. ksa^ra-n. "power, rule, empire; imperious power' (Proto Aryan neologism to 



ksayati), Old pers. xsayadiya-^ king in the possession of tlie imperious power ' (npers. 
saH), Xsayarsan- " Xerxes ' {xsaya-arsan- " ruling heroes '); common Old Indie gh- > ks- : 
Old pers. gh- > xs- : npers. xs- > s-. 

gr. KTQopai ' acquire ' (= ksayati), Perf. kekthmcii " possess ', kteqvov (with unclear z) " 
possession, property, fortune', poet. Kieap, Dat. PI. KTsaTsaaiv ds., Kinpa n. ' acquisition, 
possession, property', KTr|vo(; n., PI. ' possession, fortune', Sg. " the single piece of cattle '; 
with the same initial sound relation as between kteIvu): gort. KaraaKEvn also Attic OiAo- 
aKnT[r|<;] = -KTriTr|<;; through hybridization from £y-KTr|ai(; and £p-naai(; (: naija) dial. 
syKTaaic; " land acquisition '. 

common Old Indie gh- > ks- : Hittite gh- > tk- : gr. tk- > kt- see Root / lemma: ghdem-, 

ghdom-. Gen.- ablative gh(d)m-es\ "earth'. 

References: WP. I 504, BSL. 38, 143, Schwyzer Gr. Gr. I 325 f., 5196. 

Page(s): 626 

Root / lemma: kha khal 

(eval):1: == not found
```


## [2026-09-06T21:29:29.990Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"ktizo\\|kti(w\\|saeiti\\|soi.ra\\|amphiktyon\\|amphiktion\" POK_full.txt | head -20; echo ===; sed -n '52320,52400p' POK_full.txt"
}
```


### [2026-09-06T21:29:30.063Z] TOOL RESULT

```
Exit code 1
51197:Avestan s///-" residence, settlement'. Old Indie ksetra-, Avestan soi&ra-u. " estate, 
(eval):1: == not found
```


## [2026-09-06T21:29:32.024Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '51160,51200p' POK_full.txt"
}
```


### [2026-09-06T21:29:32.090Z] TOOL RESULT

```
Uralic etymology : 

Alb. {*Reuero-) veri^ north ' 

Proto: *orja 

English meaning: slave 

Finnish: orja 'Sklave, slave ' ( > Saam. L ar'je 'Leibeigener, Knecht, Sklave', oarji (I) 

'Sklave') 

Estonian: ori (gen. orja) 'Sklave, Frohnarbeiter' 

Saam (Lapp): oar'je -rj- (N) 'who, which is found in or belongs to the southwest'; 

southwest, west', ar'jel (L) 'Leute von SiJden', viorje (T) 'Norden', orjal (A) 'Nordwest', 

vu«-<9"rjel«-< (Kid.), vuaTjel«-< (Ko. Not.) 'Nordwesten' ? 

Mordovian: ure (E), ura (M) 'Sklave; Lohndiener', urehde- (E) 'muhsame Arbeit verrichten' 

Udmurt (Votyak): var (S), war (G) 'Sklave, Diener, Knecht' 

Komi (Zyrian): ver (altsyr.) 'cjiyra, pa6', Ud. veres, veres 'Ehemann, Gatte' 

References: WP. I 377, WH. I 190, O. Szemerenyi KZ. 70, 65. 
Page(s): 597 

Root / lemma: Rhei- 



Meaning: to settle 

Material: Old Indie kseti, ks/yat/" stays, dwells ', Avestan sae/t/ds., Old Indie ks/t/-, 

Avestan s///-" residence, settlement'. Old Indie ksetra-, Avestan soi&ra-u. " estate, 

residence ', Old Indie ksema-m. ' quiet, peaceful staying ';
```


## [2026-09-06T21:29:32.623Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=52340 && NR<=52380' POK_full.txt"
}
```


### [2026-09-06T21:29:34.746Z] TOOL RESULT

```
Root / lemma: Ru- {*kehu-) 

Meaning: sharp; pike 

Note: 

Root/ lemma: Ru-{*kehu-)\ "sharp; pike' derived from zero grade of Root/ lemma: aR-, oR- 

: "sharp; stone'. 

Material: Old Indie su-la-m. n. "spit, pike, pointed picket, pole; stechender pain', Armenian 
s/5/r' (from *sulak') "spit, pike, dagger, arrow'. Old Irish cuiT a gnat, midge ', cymr. cylion- 
ends., Latin culex^ mosquito '; 

Old Indie su-ka-m. n" sting of an insect, awn of the corn', Avestan su-ka-t "needle', np. 
sdza/7 "needle', sok' ear, awn'; dubious prakr. osukka/" whets, sharpens '; 

Latin cuneus^ wedge' (due to from ku-no-^cusp, peak'). 



Maybe alb. kunJ'\/\/e6ge' Latin loanword. 

References: WP. I 465, WH. I 302 f., 308. 
Page(s): 626-627 



Root / lemma: Icalo-s {* Icehu-lo-s) 
Meaning: a kind of big fish 
See also: see below under (sjk^alo-s. 
Page(s): 635 



Root / lemma: Icas-io-, -lo- {* IC'ehus-lo-) 

Meaning: basket-work 

Material: Latin qualum{quallus) 'a wicker basket' ( *kuaslom, compare the diminutive:)
```


## [2026-09-06T21:29:42.989Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=51186 && NR<=51235' POK_full.txt"
}
```


### [2026-09-06T21:29:44.990Z] TOOL RESULT

```
References: WP. I 377, WH. I 190, O. Szemerenyi KZ. 70, 65. 
Page(s): 597 

Root / lemma: Rhei- 



Meaning: to settle 

Material: Old Indie kseti, ks/yat/" stays, dwells ', Avestan sae/t/ds., Old Indie ks/t/-, 

Avestan s///-" residence, settlement'. Old Indie ksetra-, Avestan soi&ra-u. " estate, 

residence ', Old Indie ksema-m. ' quiet, peaceful staying '; 

Maybe alb. {*ksati) fshat/ WWage' : Rumanian sa/ 'village, countryside' identical to 

Rumanian coapsa "thigh' : alb. /ro/fe/?^ "thigh' common Rumanian-lllyrian k"hs- > phs-, fs-. 

[see Root/ lemma: koRsa: a part of body (foot, hip. etc..)]. 

Armenian sen. Gen. s//?/" inhabited, farmed, village ' (: gr. KToiva); 

Common Old Indie gh- > ks- : Old pers. gh- > xs- : npers. xs- > s-\ hence Armenian sen " 
village ' is of Persian origin. 

gr. KTi^w " of a city, to found, plant, build; to plant; set up, establish; to create, bring into 
being, bring about; to make so and so; to perpetrate a deed ', £UKTi[j£vo(; " well-built, 
furnished, well-made, of a garden, well-wrought ', £uktito(; ds., ttspiktIovec;, nspiKTirai " 
dwellers around, neighbours ', apcpiKTiovsi; " they that dwell round, next neighbours ' (to 
form afj(piKTuov£(; Lithuanian by Boisacq 525 Anm. 2), ktIgk; " a founding, foundation, a 
doing, an act, a creating, the creation of the universe, that which was created, the creation, 
an authority created or ordained ', rhod. ktoIvq " a local division, township ', also KTiAo(; " 
peaceful, tame; a ram ' (actually " tame, docile, gentle, domesticated '); 

common Old Indie gh- > ks- : Hittite gh- > tk- : gr. tk- > kt- (see Root / lemma: ghdem-, 

ghdom-. Gen.- ablative gh(d)m-es\ earth) 

See also: belongs probably to consecutive: kt^eO)-, kt^aO)- 

Page(s): 626 

Root / lemma: Rik-1 

Meaning: strap 

Material: Old Indie sic-i., s/kya-n. " loop, noose, snare, suspenders ', sa/kya-' 

damascenes, provide with loops ';
```


## [2026-09-06T21:30:01.685Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"xsaeta\\|xšaēta\\|hvare.xs\\|xvar.xs\\|yima.xs\" BRT.txt | head -30; echo \"--- BRT ksi lines:\"; grep -n \"xsae\\|xsai\" BRT.txt | head -30"
}
```


### [2026-09-06T21:30:01.758Z] TOOL RESULT

```
10698:•  j,  xSaeta-  Adj.,  fem.  xsöiSni-"  'licht, strahlend,    glänzend,    herrlich';    i)    vom Licht  usw.:    °ta    rae^A    Ytj.  1;    —    ." *bamya   -«/{als    GS.)    Yt.70. 143;'* usänhfm  .  .  '^nfm  G.  5.  5;  —   'ünyJl usayll  YtÄ35.  2)   von  Göttern  und Menschen:    bfrizanlim    akur^m apqnt    napätptn  Y.  2.  5 ;    —    asis  .  .  srlra 0«(  Ytij.  107;    —    asim    ..    ''inim  Y. 2.14,  Yt/J.  i;  —  arptfplm  ..  ''hnim  YL 5.  1 5 ;  —  am3sanqm    spmtanqm    'tanqm Y.2tf.3;    —    nar/ A?hrpa  .  .'"ta/ie  Yi.8. 13;    —    kainlnS    kikrpa  ..  ''ä-nyä    H.  2. 9;    —  frazantsis   .  .  '^nyä  (GS.)  Yt  ij. 134.          a)   bes.  von    Yima:  yS  yimd  'tö
--- BRT ksi lines:
2488:ultä  kakmäiclt  .  .  däyät  ahurö 44-i6,  27.14;  — yastn  .,  tari.mqstä  .. anying  ahmat  yi  hei  arim  mainyätä  Y. 4j.ii;  —  anyö  akmat  yö janaili  V.5. 34; N.  iS\  —  agustä  (sd.)  vacS  singhamahl aHbyö  yöi  ,  .  alakyä  gaSha  vlm?r?ncaiis (sd.)  aihp  aiibyö  nahiltä  yöi  *zrazda  aa- Afn  tnazdai  Y.j/.  i;  jo.8;  —  alsam  gä- naoiti  v?rfirayrtim  yöi  diin  .  .  /r3yaz?nte YL/O.16;  —  vätöyö/ä (sd.)  1/  aäbyöyöi  Tl.. v»r^syqn  Y.J5.6;  —  vJspaiibyö  aiibyö  yöi .  .  upa.sruttvanii  N.  20;  —  ahe  .  .  yö  nö dussarfkö  AiitaiteY.  10.12  (s.a.);  —  mäoa fiS  a/tmi  /raniliti  (sd.)  yÖ  nö  ..  inrixsaile ^■^5'7i  —  ^y^  *äröi  häkunnim  {'^d^ yayä haiinti  urvqnö  Y.j'^j.  9;  — ■  //  äbya  (statt DP.)"*  bairyeinte  yalsatn  .  .  fräyö  (sd.) '      ■  ■  bei
2498:näitm   (sd.)  .  .  zävan  baxsaiii  .  .   Aaomö  ijes:  ainyö  statt  anbyd}^         Vgl.  zü  aySm. taicit  yöi .  .Y.  0.22;  —  aAmai  ar^Aat  (sd.)  \       ■        „  r-i  .      b         c       -
3553:höchste,  höchstgelegene,  höchststehende':  •  j.  apayant-  AdJT  PPA.:  s.  ap-. upa  dvar»m  xsaiireMtiym{sA.) 'mstn  karj-\    j_    apayantama*    Adj,    'maxime    pro- Aaifl  "..dem  höchstgelegenen  in Ä:"yLj.  pellendus':   'maieca  a»rahe  mainysus  \\, 54.         a)  mit  alahe  und  aiät  'der  höchste  21.  i.
3658:•  j.  ap«m9n),  g.  ap3ni9m  Adv.:  s.  apma-, ■  j.  a-p9r9tö.tanü-  Adj.  'auf  des  Leib kein  Makel  haftet,  makellosen  Leibes"*: Aagat^rnt  gavam  axsaenanqm  'nunqnt  V. 22.4.
3852:Pü.:  fehlt. «  g.  aibi.bairi§ta-  Adj.  'der  zuträglichste, am  meisten  frommende':    vohä   xsainm vairim  bägim  'lim  ^vldlf^mnli  (sd.)  . .  asä anlarp.'araitl  .  .  vahist?nt  Y.5J.  i.
3858:g.  a-bifra-  Adj.  'ohne  Gleichen,  unver- gleichlich' :  raß-träi  vourucasämisA)  döisl (sd.)  msi  yä  vi  -/rä  (NP.)  W  xsaisrakyä tthurä  yä  vanhSuS  asi/  matiauhs  ". .  sollt ihr  mir  die  unvergleichlichen  (Wonnen) eures  Reiches,  o  AA.,  zusichern  als  das Los  des  guten  Sinnes"  Y,j_j.  13''.
4585:•  j,  +antar«.ar98am ''  Adv,  ('zwischen  den Seiten',  sva.)  1) 'innerhalb',  mit  Gen.:  °äjw zrayanhB  V.5.19;  —  ''(am  nmänahe  "V-ff. 33,  Yt./7.6o.  2)  'diesseits':  yas;/  iava masda  kirpnaot  tacar)  *nSit  *tacar>  *'Mm'^ upairi  Avanxsaiüm  "dass  dir  M.  eine Bahn  bereite,  nicht  eine  Bahn  diesseits, (sondern)  Über  dem  Sonnenball"  YL  5, 90.
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
4814:mit  "p.parü,  y  parai''>  'weg-,  fortgehen, sich  entfernen';  a)  absol.:  natrya-san/ta . . para.ili'ii  (2SIA.)  upa.vazanuha  avi  ntnä- n>m  airyamaifii  (sii.)  V,  22.  7;  —  *para.- äip^^  upa.vazala  nairy3.sa»hs  avi  . .  V. 22. 13;  —  zaota  (sd.)  anakaxtö  par^at dqhiUäi  .  .  zao^r)m  raSxsaiti  N.  A'o;  — yezica  *alte  ratavö  *anahaxta  para.tya- yanti^^^  N,  Ai?;  —  uzayeni  psrayaii  V,  2-2. I.  a)  II  militärisch  'ausrücken,  ins  Feld ziehen':  avd^ä/aiy  a'iaAam  paraidiy (2SIA.)  avam  käram  jadty  Bh,_^.3;  2.7, 10; — ara^äsam  a>aA<im  piirait>l(iP'PTA.) avam  käram  . .  jatä  Bh._y.14_:  9,  2,6,14;
4828:mit  frS^''^  i)  'hervorgehen,  -Ireten': aiiihe  haxayB  fräyente  astva(.»r>take  Yt. ■'5-9SJ  — yü'ia  .,  hvanxsaet^m  tarasca harqtn..fraca  iii/i  aiwica  vazaite  ava^a  . . Yt  /0.118.  2)  'vorwärts,  weiter  gehen': fräyantö  tarö  pilüm  ..yim  cinvats  Vyt. 42.  a)  &oiysX  mA  ß-a^a: /rain /raysiii^ irUtim  uzbaröti  äpö  V.6.2T,  — /ra/a  fra- yaniu  n  maoö  (sA)  Y. /O.  14,  ig;  19;  — /rasa  /raya  (aSIA.)!'  vahisDm  a  ahüm binjayanti  (sd.)  ie  ..  V,  7.52;  —  vgl.  Inf. Jrayäi.  3)  'einhergehen'  iyio? paiti  mit Akk.):  yat  ÖS  paiii  ml  asava  frayaf^  .  . aismssastö  .  .  V.J.  i ;  —  äat  liama  yh paiti  frayat^^  tä paiii, .Yi.  lOjiJ).  4)  'be- gehen', mit  Akk.,  a)  einen  Weg:  kaf  tä pa>ä  (sd.)  Jrayqn^  pasvqm  vil  staorqm va  narqm  vä  Y.S.iy,  ii^23,  3.  15;  — likrava  paoirlm  aHa  pa%ä/rayanlu{s\.3Xl Sing.)  V.  Ä19.  b)  eine  Tat:  (aili  tä ^ao^aa  varsta  , .  fralta^''^  apati(a{&i.) anuzvars/a  . .  V.i^.i.
5143:•  j.  a-vas5.x§a9-ra-  Adj.  'der  nicht  nach'. Gefallen  schaltet'  sva,  'in  seiner  Freiheit beschränkt,  unfrei,  abhängig':  vasSjxsairS iylt  asava  -rS  hyät  drvä  .  .  varais  °rB \.S.(s; —  cvqs  främraot  .  .?  vahiäd  xia- yamnJ.  'cvarthm?  amvamm  vahistsmca ■nm:a  'was  für  einer  sprach  aus..?  Der beste  Herrscher.  Zu  was  fiir  einem?  Zu dem  Gerechten  und  Besten  und  Abhängigen" \.ir).2o0).
5566:•  j.  'airyaman-  m.  Name  des  mit  J  (7/r- ,  •  j.  'aurvataspa-  Adj.  'der  schnelle ysmä  isys  beginnenden  Gebets  Y.54.1:  Rosse  hat';  a)  von  ^rar-imd  Äj'ari>.tiiji^u-: 'matiim  mq^ranqm  maBittm  Yt.j.5;  —  Är'ur?  "toffi  YL/0.90;  6.4;  —  'tun  bavähi T-3r/irayn3m. .  ya^asli  antan  ahuna(&A.)  yaia  kiari  Az.  6";  —  am.nakc  hü  yat 'manaiAD.)Vi.24.i;*li.ioj.  a)  sonst |  Vn^  YLJO.  13;  —  hiarsxsaS^m  'ptm mit  isya-.  'mamm  isim  .  .  ßäsB  mq^fvm  Yt  6. 1,6, 12.^4, 1^.81,  \.  16.4;  —  hvar>- ..  b»r?am  Aa',aoxt?m  Vr.2.10;  G,/.6,  S.j^/attJj  °päi  Y.ÜÄ22;  —  hrerixiaiiahe 2.3;  —  tfm..  vJspanqm  sravanhqm  ufard.-\ ..  -pake  Yt.  Ö.o,  Y, 22. 24;  /.  11;  —  Iwan- kainm  fradaiqm  yim  'mamm  tsim  FrW. '  xsaiia  'pa  (VS.)  V,  j/.  5,  b)  von  apqm 4-1',  1 ;  —  'taan^m  isim  . .  maiisüm  o/aAe  napät-.  apqm  napa  -ps  Yt  ig.  51';  — sra-.arahqm  Y.54.2;  Vr.  24,1;  —  °manS  aPqm  napättm  'ptm  Y.  2. 5;  —  apqtn isyehe  hafu{iitä..'manö  isyeke ,.  haililca  ..  nap5  °pa  Y.65.13.  'pä'a  VyLjJ, Vr.24.2;  /.8,  S.7.3.                                    4'>"(?).
5765:•  g.  a-siStay-"  f.  1) 'Verheissung  auf-' (Akk.):  iä^ä  mSt  yqm  yaoi  damam  yaoz- däm  yqm  *Aud3naos  paiüh  saüyat  xsa- %raAya  xnlvä  xsaira  %wSvqs  °tls  (AP.) mazda  "ob  mir  wohl  für  das  Ich  des  ein- sichtigen, das  ich  vervollkomnmen  will, der  Herr  des  Reichs  Verheissungen  auf  die sicheren  Reiche  machen  wird,  einer  (ein Gott)  wie  du,  o  M."  Y.  44. 9-  2)  'Gegen- stand der  Verheissung,  verheissener  Lohn': at  -tä  (LS.)  yao/an/l  (sd.)  il  /lusiUis  .  .  Y. _jo.io.         \\.34-A'  lies  astshm.]
6007:•  j.  az«m,  g.  azSm,  p.  adam  NS.  Fron. 1.  Pers.  'ich'.  Es  wird  gesetzt  i)  wenn auf  dem  Subjekt  ein  besonderer  Nach- druck liegt)  a)  bei  Gegenüberstellung:  1  naiy 'iam  fuümaiy  taumä  Bh.  >^.  1 1 ;  —  11  ima' ttsuam  (sd.)  Aauv  rtiyastaya^  ktftanaty.. pasavr  'dam  niyastäyam  ..  X.  7.3;  —  i^a maätyOe  dta^arynä  . .  äat  azim  manya  . . \\jo.  I  o  s  t ;  —  'Um  iBi  sis  ^pouruyifravsi- vJdl  (sd.)  vJspSt^  anySng  .  .  \.  44.11;  — yä^a  't^m  avata  V3r3%ra  hacane  ya^a vltfie  *anye  aire  Yt.  5.69;  —  b^r^JoyStiti il .  .  strSuica  titäuApmca  .  .  'z^mca  kl  öptp- jttlm  yö  äaiiva  ahurd  mazdä  V.  7.52''; —  S  mann  taumäyä  ^*  paruvam  xfäya- ^t^ä  a/tcT  'dam  navami^  Bh.  7.4;  — ö^J  aäJ  csit  (sd.)  akurS  .  .  ^öti  sara- "^uärg  , ,  a%a  *'ifmhi  yö  mazdayasno .  .  vimrvyi  Y,  12.  6  '*;  Vr.  11.  19";  — yd^a  avat  kvanxsait^m  ..  av<£k>a  'zsmHl.
6074:ys. .  mazdayasnö  aojanö  'sähe  raima  (sd.)  \  13.  42,  Y.  68.  7,  14-  48;  —  a^al  nS  vacö jlsti^amnS  "V .  8.  y, —  uxltie  (sd.)  xraiwe  .  ,  *sixsaimca  (sd.)  .  .  °jvW  haäz  yat vTdrvanahe  °sät  'V.4-AS',  — yaüra  nard  vahiHät  Y.iff.ii.  LS.  'Saya  als  Adv, asavatts  'um  h^tüi  zrazdatsma  (sd.)  YL  j  sbes.  II)  '(dem  heiligen  Recht  ent- y-  'S;  —  tha  5%ravanS  .  .  ma/iyetiU  sprechtnics,  ^/«mässigesj  rechtes,  recht- vanh^s  'sähe  Yt7j.  147;  —  vahistmi  schafTenes  Tun,  Gerechtigkeit,  Recht- °i3m  yatamaide  Vr.  2g.  i ;  —  ySi  'iäi  schaffenhcit';  auch  in  kollekt  Sinn  'alles vaonarp  (sd.)  Y.  26.  4,  S;**  —  yö  yaomwas  einer  recht  tut,  bona  opera'.  i)  im iärayeiti  hs  'hm  iarayeiti  [sA.)  V._J,  31;  ■  gAw.:     huää    (sd.)    'Sim    vohucä    manä
6099:—  mazda  dadät  aAurö  Aaurvatö  amfntä' tasca  .  .  'sahyacä  xsairaAya  sarö  (sd.) vanhSus  vazdvari  mananAS  Y.  31.  21  \  — tä  vi  masdä  .  .  aAurä  'säi  yecä  taifyacä armaill  .  .  i/lffiS'  (sd.)  xsa'^rvm  .  ,  voAä manaaAa  Y.57,  2;  —  tat  vi  ni  Aasaosä^
6239:•  j.  aäava.frazaiitay-  f.  'gläubige  Nach- kommenschaft': haomS  datiaiti  , .  xsaits.' puhrim  Uta  saintTm  Y.g.a.
6298:steht,  dem  das  Paradies  sicher  ist';  im jAwf.:  yaia  i>aH  (sd.)  a^äum  *a<ia  atiAs 'sota  . .  z'ahiäa/u  atihSus  °sava  jasB  Y. j/,i6;  —  jvasHt  nöit  dval  °sava  miSascit fwii  ^axsaitHsd.)  vahistahe  ataksu^"^^  lang er  lebt,  erwirbt  er  sich  das  Anrecht  nicht, ood  - ,"  V,5,6ii — /si!mä{sä.)  asil 'fava ■nrüraja  vaktäd  \.s8.i,^
6715:iB. :  vasS.xsaitä  hyäl . .,  it-a  asti  . .,  kS  asii . ., hau  Olli  . .,  lal  Olli  , .,  yayi  asti  . .,  yö  aiihal . .,
6861:garS  nmartptn  mai^anpm  'rahe  mazdä  V, '5-3*i  Vr.7.  I,  Vt.j.4(?);  —  vahiits aiphul  yö  mana  yat  °rahe  mazda  P.  4"; '^'^•33\  —  "vi  'rahe  mazdä  .  .  gätvS zaranyöjants  V,  ;p.  32;  —  hvarpca  xsai- lahe  .  .  dsi'irahe  'rohe  mazda  Y.  i.ii; 68.  22;  —  raocsbli  .  .  yäis  'rahe  mazdä Y.  5&Ö;  —  uyrpm  kai'aZ.n  p^ar^nS  ..yat
6908:X.  J.  3 ;  Tgl.  aySxhuta-  und  kvanxsaela-.  S. Paul  Prinz.}  302.  —  Vgl.  (^ura-  und  'mai- )   Za    Am.   4    ideographisch    ge-
7543:a.  a)  bes.  neben  Isä-  (sd.):  aj  Äv5 mazda  tzäcä  "zBitisca  yS  . .  *särjs/a  (sd.) "der,  o  M.,  -  Glück  und  Fülle  (wird  ihm), wer.."  ¥.415.5*';  —  P^ra  ..  ahmst  haca Oianhatca . .  axstat . .  iiäca  'sUitUla .  .frada- %>inca  var3da>:?mca  vaxsaifmca..V.g.^3.
7951:airyamanäi:  'mal  ts  saahat  ahurö  mazdS: az3m  yS  ahurS  .  .  "folgendes  tu  dem Airy.  kund:  'AhM.  tut  dir  folgendes  kund: 'Ich  Ah.  .  .'"  V,  22.7f.;  13;  —  S  vaiftä <^urJ'mazdäh<^  °m<^  adam  akunavam: adam  hamataxsaiy  .  .  Bh.  J.  14;  —  'm<^ ly<^  manä  kartam  pasäva''  yd^il  . ..-  ia'- ba/iya^  ..  Bh.j.io;  15,  5.1;!!  —  in  Kon- gruenz mit  dem  Praedikat:  'me  acte  va^a ySi  htnti  bisämrüta:  ahyayäsä  '^.lo.y,  7.
7990:•  j.  is3^§a3Työ.'t«ma-  Adj.  'der  am meisten  nach  der  Herrschaft  verlangt'; is>jxsairS  nama  ahmi  'mS  nama  afimi VL/.,3">.
8441:*105'^;  — ya^a  aztm  'num  xsainm  (sd.)
8738:•  j.,  g.  u£ta  Adv.  'nach  Wunsch,  wie  es gewünscht wird':ri>AB  uxsy3(sd.)  manaukä ..  -ta  tanamW.jj.  10;— '/S  aAmaiyahmüi ui/,1  (sd.)  .  .  matää  dayät . .  tjvlslm  *gat.- tei  (sd.)  vasiml  Y.  43.  i ;  benüut  Vyt 5?>  —  rapBisla  tu  nS  äar?g?mla  °läcä \.4i.4;  —  vasas/a  tß  .  .  'läca  xsaisa V. Ä5;  —  darrfim  jva  Ua  jva  A.  J.  12; —  °la  ahurim  mazdqm  yazamaiäe'Vx.tS. 1;  i^;  —  °/a  astt  'la  afimsi  hyat  asäi vahistiii  as)m  (sd.)  Y.  2".  14;  —  'tä attusalibyB  sp>ntalibyS  yazamaide  Vr.  13. I  (?);  —  mit  Gen.  subj.:  ahä  nS  sazdyäi (sd.)  -ta  Y.  57. 16;  —  'ia  ta  sStS  aiirava .  .  iarai:uströ  Yty.94'\  a)  mit  astt 'er  befindet  sich  .  .,  es  geht  ihm  nach Wunsch';  ySng  usvakl  *°tä  stoi  (sd.)  Y. 46'.  1 6.  A)  als  Subst  'Wohl,  Heil,  Glück': iynt  aksya  (sd.)  dngväitl  °tä  yJ  as3m äädrl\.^i.%;  —  -ta  buyäl  ahmai  naire yas»  . .  Y.  62. 1;  F.g,  Vyt.  jo ;  —  mtatsüm nimravaite  tistryd  . .  °ta^  ml . .  °ta  ä.baväl "..  Heil  wird  mir  zu  teil"  YtÄ'.ag;  — mit  Ellipse  des  Verbs:  'ta  i^a  (i yö  .  .  "Wohl  dir,  o  Manit,  . ."  V,  7.  52; Y.9. 25,  Yt. /7.7,  Vyt. 5.?;  —  'ta  ahmäi naire  mainyäi  . .  yahmai  . .  säär>m  ahmäi naire  mainyai  .  .  yahmai  .  .  "Wohl  dem Manne,  so  denk  ich,  dem  .  .  Weh  dem Mann,  so  denk  ich,  dem  ,  ."  Yl  10. I37f.  a)  mit  asil  "es  ist,  wird  wohl, guf:  ai  aipT  läis  attkaitJ  °tä  "dann  wird es  künftig  woht  werden"  Y.jo.  11.
8932:I  auf  das,  was  künftig  sein  oder  geschehen wird,  daher  sva.  'in  Aussicht  stellen,  ver- !  sprechen,  zusichern' J\  mit  Akk.  der  Sache und  Dat.  der  Person:  yi  mai/yil  yaoi akmiii  ascJt  (sd.)  vahUtä  .  .  vokli  cSisjm manauhä  Y,  46.  i8'>;  —  tarn  spmtil mainyü  mazdil  aJiuril  asiiunScii!s{2S^ih.) yä  ZI  i-ü-.i  vaAi/tä  "und  all  das  Beste,  d.os du  ja  durch  diesen  heiligen  Geist,  o  MAA., dem  ^Äranhänger  versprochen  hast:"  V. 47- Si  3'Z''  —  '^tM  ahniSi  ..  auAaiti (sd.)  yiim  (näml.  gam)  hsi  .  .  x/a^rrä 7'ohu!-ä  cöist  manatihs  yi.."..  Idas  Rind) das  er  durch  seinen  A7.  und  VAf.  ver- sprochen hat,.."  Y.5o.3;^_vJ  ää^a^dyS *}rjs.ratam  xsayas  am-ä  (sd.)  (istä (3SPrM.)s>  Y.^/.s!  a)  Hebendem  Obj. steht  ein  Inf,  dessen  Inhalt  a)  vom  Subj. des  Satzes  gilt;  cürd  mit  dam  *aküm.bis.- ratü}ii{?.i.)ciidi\.44.i6.  '  ß)  vom  Obj.: Ayat  höi  aSä  i'okucä  ^äUt  mananhä xlairöi  hei  haurviitl  am?riiata  ahmüi  stöi dqn  (sd.)  ".  .  da  er  durch  seinen  Am  und VM,  versprochen  hat  (promisit),  in  regno suo  salutem  immortalitatemque  nobts  esse (fore).."V.45.io.  3)'Jmdm.(Dat)  etwas (Akk.)  zuweisen,  zuerkennen,  zueignen': taibys  (sd.)  xsa:^r.m  vohü  (inas  (3SPrA.) maiiatihi  "wird  von  dir  her  VM.  das Reich  zuerkennen?"  Y.  44. 6 ;  —  huxsd^rS.- ^bä  at  xsainm  .  .  dad)maWä  M- mahicii  *hvanmnhm  Y.^5.5*';  SV-A"^',— huxsa>:ro.timliHt  at  xsai<r3m  cisyat  yat ahurili  mazdiii  A.  j-ö*"';  —  stüts  garii  .  . ahuräi  masäüi  .  .  dadjmahicii  ci/m/ihira iicil  vasdayamahl  Y.  41.  j*>;  —  ahuriii masi/äi  vtspä  vehS  Hiiahmi  Y,  12.  i; •o''-  4)  3S.  einasti  in  der  exegetischen
9011:—  'i^B  Hls.n,lsiima?  ya'ia  hiiii  janäiui '"Was  besagt  tuLwl'  'Es  besagt:  wir wollen  sie  schlagen.'"  Y. 61.5.  3)  die direkte  Frage  einleitend  'wie  (ist's)?,  num?, ob  wohl?':  k'  saota  xsaia  vaca  <ips  .  . yazäite  "ob  wohl  der  Z.  mit  dem  gelehrten Spruch  die  . .  Wasser  preisen  wird?"  Y.  li^- gJ';  —  "ürt  mit  yqm  yaoH&d.)  diWiqm  . . saHySl ..  Y.44.9;'2,  11,  13,  14,  17,  18, 2f).2, 50.2,  4)'wann?':  -'> a  agte spiina al'ä.zaeium  (sd.)  .  .  bavan  V.  1^.  44.
9036:11;  —  xsai'am  lya''  gaumäicr  .  .  adins"
9048:•  j.  kaoba-  m,  Name  eines  Lands*':  upa dvarnn  xsairö.sukjm  (sd.)  apanöJtmjm 'hitva  *birizantaya  asavanaya  "bei  dem Pass  -Vj^,  dem  liöchstgelegenen  in  dem hochragenden  heiligen  K."  Yt5.  54.
```


## [2026-09-06T21:30:02.107Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"xšai\\|xsai\\|to shine, gleam\\|XŠAY\" CHEUNG.txt | head -40"
}
```


### [2026-09-06T21:30:02.179Z] TOOL RESULT

```
1424:OAv. baxsaiti(Y 47.5, Y 50.3, ? Y 18.6), IMPV. med. 2sg. OAv. abaxsohuua (Y 33.10) 
2474:Pres. them.: IND. 2sg. YAv. baxsahe (Y 11.1), 3sg. YAv. baxSaiti, med. 3sg. YAv. baxSaite (Y 10.13), 
2616:*PARTHIAN: br’z- ‘to shine, gleam’ || (+ *ui-) wybr’z- ‘to shine, be lit up’ = Ghilain: 
5576:Pres. {1} them.: INJ. 3sg. OAv. daxsat (Y 43.15); Pres. {2} aia-: OPT. med. 3sg. YAv. aóaxsaiiaeta (Y 
5577:12.5), IMPV. 25р. OAv. «fra»daxsaiia (Y 33.13) 
8897:24), SUBJ. med. 1sg. OAv. haxsai (Y 46.10), med. 1sg. ? YAv. haxsane (V 19.26), OPT. 1sg. YAv. 
8898:haxsaiia (Y 8.7, Y 11.14, Y 52.7), med. Zeg ? Y Av. haxsaesa (V 7.50, V 19.26), 3sg. YAv. haxsoit (Y 
11765:Pres. aja-: IND. 3pl. YAv. aifiiaxsaiieinti (Yt 13.59 Ё), SUBJ. 3sg. YAv. aipiiaxsaiiat (N 77), OPT. 35р. 
11766:Y Av. aißiiaxsaiiöit (Yt 1.19), IMPV. 35р. Y Av. aipiiaxsaiiatu (Y 58.4) 
17581:(V 19.1, V 19.6); Aor. s-: SUBJ. 3sg. med. OAv. maroxsaite (Y 51.10); Partic.: pres. aja- ҮАУ. 
20206:Intens.: pres. IND. med. 3sg. ? Y Av. iririxsaite (Y 65.7) 
24206:Bailey, DKS: 68a, rather goes back to а preform *xsai6ra- (a blend of *хёабга-, Av. 
25051:MED.; Pres. them.: IND. 3sg. ha"taxsataiy <h-t-x-S-t-i-y> (DNb 16), impf. lsg. hamataxsaiy 
27723:Y Av. vaxsaiiato (Y 10.3), SUBJ. 3sg. ҮАУ. aißi.uuaxsaiiät (N 73), ОРТ. 35р. Y Av. aifi.vaxsaiioit (N 81). 
29066:Aor. them.: INJ. Zeg OAv. axso (Y 46.2), SUBJ. med. 1sg. OAv. xsai (Y 28.4); Perf.: IND. med. 3sg. 
29131:Pres. aia-: IND. 2sg. OAv. xsaiiehi (Y 44.15), med. 2sg. YAv. xSaiiehe (Yt 10.29), med. 3sg. ҮАУ. 
29132:xsaiiete, 2р1. OAv. xšalla08 (Y 48.9), med. 3pl. YAv. xsaiiente (Yt 17.7, ms. F1), INJ. med. 3sg. ҮАУ. 
29133:xsaiiata, SUBJ. 15р. (?) OAv. xsaiia (Y 50.9), YAv. xsaiieni (FrW 4.2), 3sg. YAv. xsaiiat (FrW 4.2), 
29134:OPT. 35р. Y Av. xSaiidit (Y 9.5), IMPV. 2sg. (?) OAv. xsaiia (Y 28.7); Aor. them.: INJ. med. 3р1. OAv. 
29136:3р1. OAv. xsöntam (Y 48.5); Partic.: pres. xsaiiant-, pres. med. xSaiiamna- ‘being able to’ (Yt 10.23, Yt 
29137:10.37, Yt 10.110). © YAv. xšaiiðit is discussed by Hoffmann 1976: 607f.; Kellens 1984: 311, fn. 1; 
29138:Kellens 1984а: 270 £.; Paul 1998: 314a f. || With regard to xSaiiamna-, cf. Gershevitch 1959: 178, ad 23: 
29201:*AVESTAN: OAv. xšiið ‘lament’ (Y 31.30), YAv. xSaiias-ca ‘lament, [BMP transl.] 
29238:*xšaip/b ‘to throw, hurl’ 
29396:*xSaip/b ?) 
29672:Iranian forms favour the postulation of two different (Ir.) roots, *xSaip/b ‘to throw, 
29674:*xSaip/b can be connected to Skt. ksep, whereas *xSuaip/b may be related to the IE 
33937:xsaiias-ca, 452 
55330:*xsai 
55608:*xsai 
55641:(s.v.), *xraud, *xsai (s.v.), 
56345:*xsai (s.v.), *zauH (s.v.) 
56907:*xSaip/b 
57039:*nard, *xsai, *zarH (s.v.) 
58219:*suaH, *tau, *uaid’, *xsaip/b 
58386:*bram, *garz, *snaud, *xSai,
```


## [2026-09-06T21:30:10.297Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=10660 && NR<=10760' BRT.txt | cut -c1-400"
}
```


### [2026-09-06T21:30:12.188Z] TOOL RESULT

```
Vgi.  .r^,;»Hm  un<!  xrüra..
•  j.  xrümini  Adv.  'in  grausamer  Weise' xf  gaus  .  .  varai>Tm  (sd.)  fanlam  azaite Ytio.38.
Vgl.  xriima-,  —  Gebildet  wie  ai.  tiipilm.
•  j.,  g.  xrüra-  Adj.  i)  'blutig,  grausig':  'r>m draß^rn  (sd.)  Y.57.  a  5,  Yt.  j.  11 .  2)  'blut- dürstig, grausam':  köi  *dngi'S.dibis  'rät's rämam  (sd.)  dant!  Y.  48. 1 1.
Ko'ropE.  —  ai.  tiäni-  Adj.  —  VrI.  xrü:  — Pü.  {lu  Y.  4X):  ö  d,-.:i,uUn  xiüii/i,  erl.:  rlS; [laYx.  t):  fa  TLxrümb'^,  erl.:/,!  r,-i  koihm  ,
•  j.  xrGzdä-  f  '(Härte  sva.)  Schwierig- keit (zu  beantworten)':  zara>ustrJ  .  . asaril3  aka  maiiai^ha  'dya  (IS.)  IbalsS.- parstanam  (sd.)  V.  iq.  4.
VgL  xnddra:  —  I'ü:.  .xrn-J  ( riansskr.).
j.  xrüid'r  Adj,,  nur  KompA.  1)  'harf. -    2)  'derb   sva.  laut',   von  der  Stimme.
Sva.   xrüidra-;  s.  unter  l/>r>a'.
•  j.  *xruzdi.vaßah- '*   Adj.  'mit  derber,
lauter  Stimme  sprechend':   'iä  (NSm.)  F.
'üzd  (Transskr.)  ffdtvihiihä.   —   D  Hds. 'd.V'.  —  '1  Vgl.  lu  xraoidyah:
•  j.  xrüzdisma-  n.  r)  'harter  Erdboden'; nahyiSi  paitistune  (sd.)  'me  nialy/öi  iiars ■arfdusiiie  V.  A".  8;    —   mayim  ava.kanOis
distitn  'me  vitaslim  rar»dusiiie(&d.)  V.  77, 5.  2)  'Stück  harter  Erde':  saßin  (sd.) vil  .  .  kamcit  vä  "manam  \.g.ii.
Ableit. 'aus  "xriiidi-iam-' Ad'i.  'was  aus  harter Erde  besteht'.  —  Pü. :  saxl  aamJi;  «u  V.  p tu.:  tafii.akij)  I  u  Hl  i.
•  j.  xruzdra-  Adj.  'hart'  (vom  Holz): 'äidranain  msmanam  ä^re  frabarüts  \ . lg.  24.  a)  sva.  'schwierig'  (zu  beant- worten) :  'uidranam  (näml.  framanam) Yt.5.82  0.
Vjjl.  xrao'.diia;  xrfddi',  xrüäij-i  xronSdis/a-, xiairldyah:  —  Pü.:  saxt.  —  »  S.  iSt  V.  /p.4.
•  j.  xrvant-  Adj.  'grauenhaft,  grausig*: 'vantim  äiktvaiibm  urviHnm  pantam  H, 2.17;  —  vairim  . .  yim  'vaiit^m  äi^iva/i- t>m  fi.og.28.
Statt  *xrü'Tiaitl-  geschr. —  Pü.:  vixrün;    s.  tu
■  j.  xrvi-°,  nur  KompA.:  sva.  xrüra-.
D.  i.  xrut'i'.  —  Vgl.  unter  birizf.
•  j.  xrvijTii-  f.  Name  einer  DaSvX:  psniie "/ni  (statt  Akk.)  V.  //.  9.
Fem.  zu  'xni-ffan.  Adj.  "blutig,  grausam  schla- gend, lötend'.  —  Pü.:  fehlt.
•  j.  xrvi-drav-,  xrvi-drav-"  Adj.  'der eine  blutige,  grausige  Holzwaffe  (Keule?) führt',  von  Assma:  aismS  *'vidrus'^  Yt. '!>•  95.;  —  azhmtmca  'vi.dräm  YL  ig. 46;  18.2,  *V.  JO.  13,  ig.AV,  —  aismahe 'vLdrao^  Y.sy.i,  Yt.  Ji.  15,  y.  138,  V. lo.id;  —  aisina  ..  'vI.drvJ''  Y.io.S; —  asima  ..  'vidrvö^''  \t.i-j.$.
Pü. :  xiiidms,  Transskr. ;  Sü. :  Ainii iini/ra i .  — 1)  NA.  hat  auch  x/f7m.dr';  s.  dagegen  Clii. KZ.  jr.  266,  Richter  IF.  5.205.  —  •)  Hds. ,/, vrj-i.  —  3)  LS.  statt  IS.  i  S  -/qT-
•  j.  xrvisyant-  '>  Adj.  (fem.  'yantT-,  'yäli- '') i)  'grausig,  Grauen  erregend':  frai'asay» ,  .  y1    irrpzayeintls    *yanlis  (APf.)   Yt.  IJ.
|33.  2)  'blutdürstig,    grausam':  gaiiahe
\vlvar?zdavatB  yalä  Y.p.30;    —    spaoaA^
dby  Google
54»  xsa-   -
'yantake  Yt  10.  36;  —  i7fi  haSnayä  °ytitis (AP£)  Yt/o.S;  15.49 ■',  /')-54  (wo  "''-O- PPA.,  ans  *xn-is'ya;  den.  Praes.  31.  —  Vgl. ai.  krafi;.  n.  'Aas',  ksl.  Wfol  •Blut'.  —  Vgl. xrii:  —  Pü.  (nach  Dst.):  ifarak  x^äk,  erl.: T/i  iuiiil],);  Sü.!  /liifayili.  ~  ')  Mit  (  Yl.  /J. 33,  /o.  8j  /f,  45  sieht  xriiisy',  %  268.  iz  c —  »)  Ge
•  j-,  g.  xsä-  V.  'lehren'.  Praes.  3  xsa-\ Perf.  I  caxs-.  —  PPfP.  xiSta-,  'xs/a-'\
y^  *urvqiam  min  gair!  (sd.)  äaeil .  . yaiat  islt  .  .  avat  xsäi  (iSKM.)  aesi a'ahyä  Y.  2Ä4;  —  kü^ra  väcS  aoLbüfa (sd.)  "yqm  hl  .-Wjtf(3SPfM.)  as>ra.paitis (sd.)  Y.  65. 9; —  ka^a  zaota  xsäta  vaca apo  . .  yaziite  Y.  65, 9,
mit  (I  dnwS.:  axsS  (zS.)  vat^hiui  asä Xitiin  manatihs  "lehre  (mich)  durch  Ä., wie  man  sich  in  Besitz  des  guten  Sinns setzt"  Y.4tf.2'>.
mit  kam:  s.  akaxsta-,  vgl.  No.  i.
«-'Erweiterung'  aus  lioj-- 3).  —  ai.  ksä-'i),  eatif,
ahtfxita;  das  sich  lu  xsäia-  verhält,  wie  ai, drzaWa-  lu  j.  dila-;  BtHL,  KZ.  ig.  576.  — ■)  Wörtl.:  'Lehre  das  Besilinchmcn  von..'. — i)  Wegen  der  Bedeutungsverschiedenheil  vgl. gr.  iva7-j  und  lal.  doccrc.  —  4)  Das  nicht  mit khyj-  identisch  ist,  wie  eben  das  Aw.  lehrt; Litt.  WklPb,  /J57.  656;   s.  noch  zu  ahnxila-.
•  j.  xsäta-  Adj.,  PPfP.:  s.  xsä-,
•  j,  xSaeta-  Adj.,  fem.  xsöiSni-"  'licht, strahlend,    glänzend,    herrlich';    i)    vom Licht  usw.:    °ta    rae^A    Ytj.  1;    —    ." *bamya   -«/{als    GS.)    Yt.70. 143;'* usänhfm  .  .  '^nfm  G.  5.  5;  —   'ünyJl usayll  YtÄ35.  2)   von  Göttern  und Menschen:    bfrizanlim    akur^m apqnt    napätptn  Y.  2.  5 ;    —    asis  .  .  srlra 0«(  Ytij.  10
Y.5.4,  Yt5.25,    t-J.  31,    /p.34,   V.  2.20,
Az-j;  — yim  yimim  't>m  Yt/p.  31;  — yimäi  °t5i  V./^.  39;  — yimat  haia  "iäi YL/^.35-
KonripA.,  E. ').  —    \'gl.  axsattta-,    - ■Sonne'.  —  Pü.!  rSht.  (lu  Y.  26J:  ; 2  a):  j-am  JS.  —  OS  20?-  2  »E-  —  ")  S.  noch unter  kvanxia^la-,
•  '].  xsaetö.puOrya-  n.  'Besiu  herrlicher
xsaSra-  1  i
542
Söhne':  haomS  daaaiti ..''^rim  Uta  asava.- frasaintTm  X.g.tt.
Ableit  aus  *j:jii//ö^iro- Adj.  —  Pü.:  hurdiiin
fius,  Sü.:  diftimän  putra^.
•  j.  xsao9ah-  n.  'Fluss,  Strömung,  Wasser- Schwall';  airy!>.layamm  .  ,  yahmya  äpu navaya  .  .  °taipha  %waxhnle  Yt  10. 14.
:.  ifidas-  n.  —  Vgl.  lu  xsusla-. j.  xloodrinum  V.  16.  7:  lies  xsävd'. j.  xiaudrim  N.  6!# :  lies  xläud:
•  j.  xsaob-  V.,  nur  Praes.  14  (Inkoh.) vu/sa-^^  'in  Aufregung  geraten', /u/  aspanqm  sri/a  (sd.)  xsufsqn  Yt./o.
j.,  g.  xäaSra-,  p.  xSsO-'a-  n.  'imperium, regnum,  Herrschaft,  Reich';  uzw.  im  Sinn von  1)  "Herrschgewalt,  Obergewalt,  Herr- schermacht'"; i)  I  im  Ap.:  c^ur^mazdä h'am  mann  fmbara''  Bh./.s,i3;  9,  'D.4. 1,17. 1 ;  —  °^^am  iyt^  bäbirauv  hauv  agar- blyaiiJ  Bh.7.  16;  11';  —  vasnä  a^urO^- mazdäA^  imJ'  °h''am  därayämiy  Bh.  /. 9;  9;  —  °'ii''amiim 
dby  Google
543  x5a*ra-  I  3
'hnm^a  YL  13.  88.  a)  mit  Gen.  'über  -' (s.  3  a):  ya>^a  aztm  up^mim  °'^r>in  baväni vispanqm    äaRyunqm    Yt5.  22.  3)   im
gAw. :  ahya  '"kräXa  maziiiäcä  *hvapa- nhäisca  (sd.)  tsm  at  ,  .  yasamaidl  Y.^J/. a;  —  kudä  (sd.)  asim  vohuca  maus '%r)m^ä  Y.  25.  1 1 ;  —  yüism  aäbyS  .  . aogü  data  .  .  '%nmc3  .  .  yl  kuhitts  rä- mqmcS  (sd-)  däl  Y.  2p.  10;  —  isasä  (sd.) . .  maibyö  '"^nm  aojönahvat  yehy3  vfndä (sd.)  vanalmS  *drujim  Y.J/.  4;  benutzt V.ao.  8;  — 
kavä  vistäsps  magaAyä(^.)  'hrä  nasal., astlm  Y.5J.  16;  —  tu  v7  masdil  .  .'dSisä möi  isteis  (%A.)  -'hnm  Y.j/.a;  benutzt Vyt.  46.  b)  mit  InE:  ial  vi  xsair^m kii  Jltis  (sd.)  syadäaiiifi  mazda  Y.  34. j.  2)  'Henschgebiet"';  i)  II  im  Ap.-, mäm  ^ur^mazdi  päluv  utamaiy  °~ii''am via  tyt^  maiui  tartam  X.J.  4;  2.3,  4. 3.  2)   im  jAw.:  ya>a  .  .  
riivänäni  as.faäna  slüi.bax.Hira..as.baourva ni'jatu.pitu  Yt. 5.130;  J7.7;  —  ktthmrti.. uyr?m  '^rtm  x^at/iisajct^m  pouru.spä'i»m,. paitiMdiiäm  Yt.  /o.  109;  111;  —  '%räi hank?r)mö  {%A.)  kaosrava  Yt.  5.  49;  —  iri- ^ini>m  '"inm  zajaiii\t'i.i$o(?)'K  3)im gAw.-.ys  ''^rJ  *gr3hmS  Aisaiat(sd.)  acisla- Ayä  dsmäm  inana*»hs\.3-i.\y  a)  ins- bes.  vom  aiiaris
xäadra-  A  i
544
halt  der  Götter  und  Seligen;  aät'  ii.  oder mit  näherei  Bestimmung  (durch  Adj.  oder Gen.);  a)  im  gAw.:  yn  vi  abi/ra{sd.)  lä '>raiyäY.33.i2; — gaf'iti  vTspä  a  "^röi *yj  vohü  %raostäisd.)  mananhä  Y.34.2;
—  ya^ra  vanhSul  mananhs  Tstä  (sd.) ''hr3mY.46.16;  —  voAs  °^nm  mananhJ mazda  dadat  ahurB  "durch  VM.  wird (ihm)  MAh.  das  Reich  verleihen"  Y.  j/. aij  —  at  mazda  laibyö  °^rptn  voAs manat»h3  *vöivTdaill{sä.)  aeibyS  saste(ad.) y5i  .  .  Y.30.8;  —  a/m  (sd.)  asäi  fo/iu •^nm  manaaha  Y. 46.10;  —  taibyS  '^rvm voAB  ^nas  (sd.)  manaisAä  Y.44-  6; 
—  voAa  kv5  '^ra  as3m  vacaitha  ^ao'i-ana Aapil{sd.)  Y.31.  22;  —  vaAü  "^rvm  vairim bäg}m  aiblJ)airist>m  *vJdll>mnäi  (sd.)  .  , asä  antari.iarain  Y.5J.  i;  —  vohü  °%r3m ISi  mazdä  ahurä  apalmä  vispäi  yavi  Y. 41.2;  —  maiää  .  .  vairya  stöisisd.)  yä 'iwahmT  'Hröi  väcT  Y.  43- 13;  3^.  6,  34. 10,  49-5;  —  ahurä  ,  .  %wahmT  ä  ''hrsi
yavsi  vjspai  fraßtarihs  aiihamä  Y.4^.8; — ka  tsi  vauAsus  mazda  °%raAya  Isti^{sd.) . .  maibyS  aAura  Y.  48.  8;  —  ku^rä  ^wS '•'irä  (NP.)  mazdä  "wo  sind  deine  Reiche, o  Af.?"  Y.  5/.  4;  —  mazdäi  avaj  °^/v« Ayat  Aöi  voAa  vaxsal  (sd.)  manatjAa  Y. 31. 6j  —  apsnd  (sd.)  dar^S.jyäitlm  *ä °%r>m  vaaASui manatfAs  "..  zu  dem  Reich des  VM."  Y
anas/i  (sd.)  Y.  20.  3;  —  voAu  'inm  ya;a- maideYr.  20.  i .  3)  'Herrschaft'  in  konkre- tem Sinn  (nur  Komp.).  A)  als  Gottheit (Am3iaSp3nta)''>;  i)  im  gAw.:  yl  s^visIS (sd.)  ahurä  mazdäscä  ärmaitiUä  ahmcä., manasLil  voAu  ''i:rimca  Y.  33.11;  —  al va  yazäi  . .  mazda  ahurä  Aadä  (sd.)  asä vahistäca  mananha  ""hräca  Y.  50. 4;  — asibyö   mazda 
dby  Google
545
xSaSrH-  A  2
x§a{h-ö.kämyä-
546
ntanauhl  '%r3J  hcUü  paitt.mraot  asä  kuL- haxa  Y.32.  2;  —  mazdä  , .  vokü  uxfya (sd.)  manavAä  °hr3  aiälä  ustä  tanüm Y._jj.  10;  —  yahmi  spfntJ  %wä  mainyU urvafse  jass  mafsds  "ärä  ahmt{s,A.)  voha mananha  Y.43.6;  —  aAmäicä  «ärJ  (als Sah].)  ^^ /asaj  (sA.)  mananha  voha  asaüä Y.3Q.  7;  —  ahmsi  dqn  (sd.)  .  .  mazdä •^rJ  armaitf  ahu
Monatstag:  'Gräfte  vairyehe  aySxlustahe . . S.  1. 4;  vgl.  2. 4,  Y.  i6. 3.  aa)  als  Be- zeichnung des  unter  Xs.%  Obhut  stehenden Metalls,  mit  vairya-  Adj.:  kariasät  fra- käraysil  liyra  '^ra  *vairya  V.g.io;  — °ir3i  vairyli  pairiAarim  pairi^araysil V.ij.ß;  —  ayao/ia&um  vä  srum  vä mfyma(sd.)  '^ra  vairyaV,  16,6;  —  *Aqm.- ivqmca  .  .  (sd.)  *upairispat
Undeutlich:  '^wqm  kainind  vähre yaona '"hra  . ,  jaiöyänte  Yt5.  87;  —  nava  dru- jaiti  '"kra^byS  V.4.  10  PUZ.;  —  '%r?m' Vyt4S;    —    '^rd!    DkB.  131.  '"ir^m
Y,  17. 1 1 :  s.  unter  xldhrS.naptar-.  [Y. ^.10:  lies  mqgHje/'.]
*)  Eiac  PenODifikation  der  o^iaH  sehen  Herrsch- gewalt  ODd  de*  oAuritchen  Reichs.   Im  Awcita
SUTHOLOHAB,  Aldru.  Wb.
tritt  Ai.  nur  wenig  hervor.  Die  Metalle  stehen unter  seinem  Schutz.  Bei  den  letzten  Dingen kämpft  er  nach  Bd.  jo.  29  mit  dem  Dämon Sautva.  Auf  Münien  erscheint  Sala-niar  (PAO- PHOPO,  PAOPHOAP;  s.  Stein  Or&BabRec. iSS^.  I59ff.)  als  Kriegsgott  mit  Helm,  Schild und  Speer.  Vgl.  im  Übrigen  Tikle  Godsdiensl' 2.  136,  JusTi  PrJ.  SS.  75.  JN.  GlrPh.  2.  
KompA.,  E,;  Ableit.  —  Zum  V.  xi^j/)-;  s. dazu  Bthi.  Slud.  /.  4S-  —  »>■  ifoirä-  n.  'Im- perium' ;  np.  saAr  'Stadt'.  —  Pü.  (für  das  Ab- straktum)4);  3^aliiSh,  Sü.:  rSjyam,  tuch  pär- Ihivalä  (Y.  44.  9).  wimilä  (Y.  33.  13)  und räji  (Y.  31.  22,  45-  1  «■  Ö-),  T-ämi  (Y.  33.  lo)s (für  die  Gottheit  und  für  'Metair|4):  sairver, ia
3)  Vgl  unter  'o/a-  mit  der  Litt,  in  No.  3.  —
4)  Doch  stimmt  die  Auffassung  der  Pü. mit  der  meinigen  nicht  überall  zusammen. Übrigens  weicht  auch  Sü.  öfters  von  Pü.  ab.
•  j.  "xäadrata  anhat  mSirSs^  FrW.  8.  2.
•  p.  xSaS-'a-pävan-  m.  'Landvogt,  Satrap': dädarns  natnd' . .  mana  ba'daka^  baxtriya 'päva  Bh.  J.  3;  9.
Zum  V.  fä{y)-;  ai-  'pivait-  Adj.  —  Vgl.  noch
•  j.  xäa(hra'yinya- '>  Adj.  —  ?  — :  a/n- nami  'yane  (VS.)'*  daiAAu.patti  uparai amäi  A. /.  8.
PO.:  iahrriiar.  —  ')  Lesung  unsicher.  — >)  S  368.  32.
•  j.  xäaSrä-  f.  'Gebiet',  spcz.  Tlurdistrikt' '' :
aspö  arsa  .,yj ..  naomyaHt{sd.)  hacit  'ryat aspaltn  varmm  . .  vainaiti  katarB  ayravB (sd.)  va  . .  Yt.i6. 10.
Vgl.  xic&ra-;  s.  aber  No.  I.  —  ')  Unsicher;
vgl.  Yt  14'  33,    wo  naamväSl  hala  dmAhael.
•  j.  xgadrsmCa:  zitirt  die  dritte  Zeile  von Y.  27. 13,  die  mit  arj-ii^w/Äiä  beginnt;  zB. ^.46,65,70.
VgL    'isa\TB.k>nta-.
•  j.  "xäaÖTÖ«  F.  5.
Fu.:  :fiaij\.  —  <)  Kein  selbständige«  Wort, sondern  aus  einem  Komp.  losgelöst.  Tgl. xsi&r5.kämya,  vasäj:sa%ri  usw. ;  BtHL.  IF.  //. 134-
•  j.  xäaSrB.kämyä-  f.  'Sorge,  Besorgtheit
um  die  Herrschaft':  haomB  . .  kmsSnJm apa-xid^rim  (sd.)  nilähaya^  yd  raosta  (sd.) 'mya  (IS.)  Y.p.  24.
Ableit.  aus  iäma-.    —    ai.  kimyä-  f.  —   Pü.:
pa  ^alä}äh  iämaiiä.
db,Google
547
<xäa9TÖ.lMir«ta-
xsapan- a
```


## [2026-09-06T21:30:54.179Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"axsayn\\|xsyn\\|ʾxšyn\\|axs'yn\\|green\" SOD_pages.txt | head -20; echo \"=== SOD leaf for entry 27\"; grep -n \"^\\s*27 \\|  27  \" SOD.txt | head"
}
```


### [2026-09-06T21:30:54.241Z] TOOL RESULT

```
3472:A green leaf (y^Jj)           Acta Iranica. Vol. 28, 1988.    BSOAS     Bulletin of the School of Oriental and
5378:560 'ptrtn'ynch B                           >jfoiA               Anc. Lett. 4.8; Sund. A green leaf, AI 1988 pl8l,
5755:                                                                             greenish
5763:     festival, feast                                       0*y               green, greenish
5769:     GcOslander                                                              greenish-haired
28575:8620 rxsynyt}yr-kyrd S                               JjjuCl           blameworthy, reprehensible
33247:                                                                              =^wnx*n, wxsyn
33260:        wiser6ar ? ©*wsyr- ? ©perf.                                         wsayne ©vereOraYna =»wnx>n, wxsyn
33423:10264 wxsyn                                                        place
36885:       green
36892:       green                                                          BBB  pl22;127Hen. Cosm. 307.1; GMS 1237, 1649;
38434:green            707, 11401 1140                handtowel     3639
38437:green                 70e5d, 707                handwriting         3644                  haunch    9364
=== SOD leaf for entry 27
7810:27  Mbwx  rwc   M  {^Iz^j^J)^^  jjj*jjjoU 
11924:27 
29232:C2,  102V  27  n  pl78;  BSTii  831,  27 
36130:Yw*nqryt(y),  C2,  54R20,  27  V26 
53045:Benv.  Et.  1,  301;  BSTii  854.4:  C2,  7V  27  p54 
109147:27
```


## [2026-09-06T21:30:55.069Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"amphictyon\" KLN_1966.txt SKT.txt AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T21:30:55.132Z] TOOL RESULT

```
KLN_1966.txt:2537:amphictyonic,  adj.,  pertaining  to  an  amphicty- ony.  —  L.  amphictyonicus,  fr.  Gk.  dpupixtuovi.- X04,  fr.  djjtcptxTuovla.  See  next  word  and  -ic. amphictyons,  n.  pi.,  deputies  to  an  amphictyonic council. — L.  amphictyones ,  fr.  Gk.  dpupotriiovEg. See  next  word.
KLN_1966.txt:2538:amphictyony,  n.,  confederation  of  states  in  an¬ cient  Greece,  established  around  a  common center.  —  Gk.  dp9txxuovtx,  ‘the  Amphictyonic League’,  fr.  dp-tpixtijoveg,  ‘amphictyons’,  fr. earlier  djupixxioveg,  ‘they  that  dwell  round about’.  For  the  first  element  see  amphi-.  The second  element  is  rel.  to  Gk.  xxl^eiv,  ‘to  create, found’,  xxlmg,  ‘a  founding,  settling’,  xxolva, xxotva,  ‘habitation,  township’,  and  cogn.  with OI.  kyeti,  ksiyati,  ‘abides,  dwells’,  ksitih,  ‘dwel¬ ling  place’.  Arm.  shen,  ‘inhabited’  (pp.) amphigory,  amphigouri,  n.,  a  nonsense  verse.  — F.  amphigouri,  of  unknown  origin.
```


## [2026-09-06T21:31:03.450Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ynh\" SOD.txt | grep -i \"green\\|blue\" | head -20; echo \"=== try axs\"; grep -n \"^[0-9]* *.x[s§]>yn\\|.x[s§]'yn\\|xs>ynh\" SOD.txt | head -20"
}
```


### [2026-09-06T21:31:03.513Z] TOOL RESULT

```
=== try axs
```


## [2026-09-06T21:31:04.265Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"tkei\\|kthei\\|to settle\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T21:31:04.311Z] TOOL RESULT

```
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
1011:steigh-. To stride, step, rise. I. Basic form *steigh-. 1. Germanic *stigan in Old English stigan, to go up, rise: sty. 2. Germanic compound *stig-raipaz, “mount-rope” (*raipaz, rope; see rei-1), in Old English stigrdp, stirrup: STIRRUP. II. Zero-grade form *stigh-. 1. Germanic *sti- gila- in Old English stigel, series of steps: STILE!. 2. Suf- fixed form *stigh-to- in Germanic *stihtan, “to place on a step or base,” in Old English stiht/i)an, to settle, arrange:
1094:tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *()koi-mo- in Germanic *haimaz, home, in: a. Old Eng- lish hdm, home: HOME; b. Old Norse heimr, home: NIFLHEIM; C. Middle Dutch hame, hame (< “covering”): HAME; d. Old French ham, village, home: HAMLET; e. Germanic *haimatjan, to go or bring home, in Old French hanter, to frequent, haunt: HAUNT. 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHYCTYONY. 3. Probable zero-grade form *tki- in Latin si- in suffixed form *si-tu- in situs, location: SITUATE, SITUS. [Pok. 1. hei- 589, Athei- 539.] to-. Demonstrative pronoun. For the nominative singular see so-. 1. Germanic *thé- in: a. Old English thé, thy (instrumental case), by the: THE!, THE?; NATHELESS; b. Middle Dutch de, the: pEcoy. 2. Germanic *thauh, “for all that,” in Old Norse thd, though, akin to the Scandinavian source of Middle English though, though: THOUGH. 3. Germanic *thasi- in Old English thes, this, this: (THESE), THIS. 4. Germanic *thana- in Old English thanne, thenne, thenne, than, then: THAN, THEN. 5. Ger- manic *thanana- in Old English thanon, thence: THENCE. 6. Germanic *thér in Old English ther, thér, there: THERE. 7. Germanic *thathro in Old English theder, thider, thither: THITHER. 8. Germanic nomina- tive plural *thai in Old English tha and Old Norse their, they: THEY. 9. Germanic genitive plural *thaira in Old Norse their(r)a, theirs: THEIR. 10. Germanic dative plural *thaimiz in Old Norse theim and Old English thém, them: THEM. 11. Extended neuter form *tod- in: a. Ger- manic *that in Old English thet, that: THAT, (THOSE); b. Greek to, the: TAUTO-. 12. Germanic *thus- in Old English thus, thus: THUS. 13. Adverbial (originally accu- sative) form *tam in Latin tandem, at last, so much (> Anglo-Norman tant): TANDEM, TANTAMOUNT. 14. Suf- fixed reduced form *t-dli- in Latin tdlis (plural tdlés), such: TALES. [Pok. 1. to- 1086.] tolky-. To speak. Metathesized form *tlokv- in Latin loqui, to speak: LOCUTION, LOQUACIOUS; ALLOCUTION, CIRCUMLOCUTION, COLLOQUIUM, (COLLOQUY), ELOCU- TION, GRANDILOQUENCE, INTERLOCUTION, MAGNIL- OQUENT, OBLOQUY, PROLOCUTOR, SOLILOQUY, VENTRILOQUISM. [Pok. tolk¥- 1088.] tong-. To think, feel. 1. Germanic *thank6n in: a. Old English thancian, to thank: THANK; b. Old English thencan, to think: THINK. 2. Germanic *(ga)thauht- (*ga-, collective prefix; see kom) in Old English (ge)- thoht, thought: THOUGHT. 3. Germanic factitive *thunk- Jan in Old English thyncan (third person singular present indicative thyncth), to seem: METHINKS. [Pok. 1. tong- 1088.] tragh-. To draw, drag, move. Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, TRAVE; ARCHITRAVE. [Pok. treb- 1090.] trei-. Three. I. Nominative plural form *treyes. 1. Ger- manic *thrijiz in Old English thrie, thréo, thri, three, with its derivatives thriga, thriwa, thrice, and thritig, thirty, and thréotine, thirteen: THREE, THRICE, THIRTY, THIRTEEN. 2. Latin trés (> Italian tre and French trois), three: TREY, TRIO; TRAMMEL, TRECENTO, TREPHINE, TRIUMVIR, TROCAR. II. Zero-grade form *tri-. 1. Suffixed form *tri-tyo- in: a. Germanic *thridjaz, third, in (i) Old English thrid(d)a, thirdda, third: THIRD (ii) Old Norse thrithi, third: RIDING?; b. Latin tertius (neuter tertium), third: TERCEL, TERCET, TERTIAN, TERTIARY, TIERCE; SESTERCE. 2. Latin évi-, three: TRI-, TRIPLE. 3. Greek t7i-, three: TRI-; TRICLINIUM, TRICROTIC, TRIDACTYL, TRI- GLYPH, TRITONE. 4. Sanskrit tri, three: TRIMURTI.
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1638:HOMAGE dhghem- HOMBRE dhghem- HOME tkei-
1914:NIBBLE ken-2 NICE ne, skei- NICHE nizdo- NICKNAME aug-? NICTITATE kneigh- NIDDERING nei- NIDE_ nizdo- NIDIFY dhé-1, nizdo- NIDUS nizdo- NIECE nepot- NIELLO negW-ro- NIFLHEIM nebh-, tkei- NIGGARD_ ken-2 NIGH néhw-iz NIGHT nekw-t- NIGHTINGALE ghel-1 NIGHTMARE mer-2 NIGRESCENCE neg¥-ro- NIGRITUDE neg¥-ro- NIGROSINE negW-ro- NIHILISM ne NIHILITY ne
2265:SITAR ten-, trei- SITH sé@-2 SITUATE tkei- situs tkei-
```


## [2026-09-06T21:31:13.622Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"green\" SOD.txt | head -30"
}
```


### [2026-09-06T21:31:13.664Z] TOOL RESULT

```
6685:A  green  leaf  (y^Jj)    Acta  Iranica.  Vol.  28,  1988. 
11204:Anc.  Lett.  4.8;  Sund.  A  green  leaf,  AI  1988  pl8l, 
12076:greenish 
12085:green,  greenish 
12092:greenish-haired 
85495:green 
85502:green 
90126:green     707,  11401,  11402 
90127:greenish    705,  707 
90128:greenish-haired     708
```


## [2026-09-06T21:31:14.966Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 589\" POK_full.txt | head; grep -n \"Root / lemma: Rei-1\\|lemma: Rei-\" POK_full.txt | head"
}
```


### [2026-09-06T21:31:15.026Z] TOOL RESULT

```
47070:Root/ lemma: kei-\ to move, go, departure, *die, derived from Root/ lemma: Rei-1\ to lie 
49573:Root / lemma: Rei-1 
49668:Root / lemma: Rei-2 
50999:Root / lemma: Rei-b'^- 
51015:Root / lemma: Rei-gh-
```


## [2026-09-06T21:31:19.240Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=12060 && NR<=12100' SOD.txt"
}
```


### [2026-09-06T21:31:20.748Z] TOOL RESULT

```
(o)yriw   ©f.n.;  ob.  -y   =>yryw,  yr'ywCh) 

body,  person 

Hen.  Talcs,  481,  51;  W-Li;  MDii 

704  TRZY    B,  S  (o>>  >-^  j-O^Xrr-'crt 
orti  ?   0HRZY)   ©Idg.   ^'rty1,  >XRZY(n),  rtyms 

then 

S  W,  C2pl83 

705  'ys'yn'k   B  (^.-J^^/ <>^ 
axsene   Oys'yn'y) 

greenish 

SCE  353;  TSP  3.33,  46 

706  'ys'yn'y  =^  'ys'yn'k 

707  Vjnh   B,S  J^,^^ 
axsen,  axsen  ?   Oysyn)   ©Av.  axsaena 

green,  greenish 

MDiii  47.8;  Bailey.  Prolexis,  20 

708  »Ys'yn  wrs>k   B  JJiy> 
axsen-warse 

greenish-haired 
SCE  88 

709  'ysyknSh   S 

axsekand 

AkhsekatOiame  of  a  city) 
MDii  p!45  n2;  MDiii  p30  n  2
```


## [2026-09-06T21:31:27.120Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"707  'ys'yn\\|707 'ys'yn\\|Vjnh\" SOD_pages.txt | head; echo ---; awk '/707[ ]+.ys.yn/{print NR\": \"$0}' SOD_pages.txt | head"
}
```


### [2026-09-06T21:31:28.805Z] TOOL RESULT

```
5759:692 >yc C => »yjc                                                        707 Vjnh     B,S                                  J^,^^
---
```


## [2026-09-06T21:31:31.530Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=5759' SOD_pages.txt | grep -c $'\\f'; echo \"---tags\"; awk 'NR<=5760' SOD_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -3"
}
```


### [2026-09-06T21:31:33.386Z] TOOL RESULT

```
91
---tags
```


## [2026-09-06T21:31:39.359Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; ls; grep -o \"\\[pdf page [0-9]*\\]\" WLD_Bd1_pages.txt | head -3; grep -c $'\\f' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T21:31:40.926Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
887
```


## [2026-09-06T21:31:43.311Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; for n in 500 505 510 515; do echo \"### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' WLD_Bd1_pages.txt | head -6; done"
}
```


### [2026-09-06T21:31:44.957Z] TOOL RESULT

```
### leaf 500
                                                                                                 l                                   .                  ,;




                                                                              klei-                                                               491
### leaf 505
496                    qleg-, qlog-, qlag-, qlang-; qleg-; ql5q-, qlsq-; qleig-; qleiq-



     lit.   sluoju, slaviaii, sluoti „fegen, wischen", Uuota „Besen“, lett. sluota ds.,
                                                      1
### leaf 510
                                          qsei-   — qseu-, qsneu-, qneu-, sneu-                                         501


qsei- „licht“.
  Av. xsae-ta-,                f.   xsov&ni- „licht, strahlend, herrlich", a-xsae-na- „dunkel-
farbig" (eig. „nicht licht“, Bartholomae IP. 5, 360 Anm.                     1 ); xsaeta-  aisl.               =
### leaf 515
506                                                        arm(o-, -a)                     — q«as-

  av. xsyo gen. von      „Hinsckwinden, Elend, Not“, xsayo                                                                     Inf. ,,um    zu
verderben" (Bthl. ZDMG. 50, 72!, Wb, 550f., 554);
     gr. ep. p&tvco , att. <p&h'<x> (*<p{Hvfco,s. o.) „vernichte“, meist intr. „schwinde
                     (
```


## [2026-09-06T21:31:51.304Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==510' WLD_Bd1_pages.txt | head -60"
}
```


### [2026-09-06T21:31:53.112Z] TOOL RESULT

```
                                          qsei-   — qseu-, qsneu-, qneu-, sneu-                                         501


qsei- „licht“.
  Av. xsae-ta-,                f.   xsov&ni- „licht, strahlend, herrlich", a-xsae-na- „dunkel-
farbig" (eig. „nicht licht“, Bartholomae IP. 5, 360 Anm.                     1 ); xsaeta-  aisl.               =
seidr „merlangus carbonarius, Kohlfisch"? Fick III 4 422,                                    Falk-Torp unter
sei    zw.

qseip-, qseib- „werfen, schwingend schleudern, in schwingender heftiger
        Bewegung sein“.
      Ai. ksipati         „wirft,         schleudert",          kaus. ksepayati, ksipra-h         ,.schnell“;           mit
Media        aksl.       oiiba-jq ,        -ti    ,,sich       abwenden",     russ. sibatz   „werfen‘\          sibkij
..schnell", osibdfo „abschlagen“, osi-batbsja „sich irren“.                             Zupitza BB. 25, 93 f.
Aber ahd. sib                  ,,Sieb“     (Wood IF. 13, 120            :   sieben durch Worfein bewerk-
stelligt)    wohl zu *seip- „ausgiefien, sieben '.
      Uber den wenig iiberzeugenden Yersuch, qseip-, -b- mit sneip-, -b- (ahd.
siva fan, av. xswiwra- usw.) und mit ueip, -b- (ai. vepate, lat. vihi are usw.)
mittelst eines Anlautes qsu- oder squ- zu vermitteln, s. unter diesen Wzln.
  Uberhaupt auf ganz anderer Anschauung beruht gr. oxomog,                                              dt.    Scheibe
usw. (s. u. sqei- ,,schneiden“, Wzf. sqei-p-).

qseu-, qsu-(??) und sqeu   squ- (besser sqheu-, sqhu-).
                                                  ,
                                                                                             z.   T. mit       /- For-

    mantien, etwa „Gezweig, Gestriipp"?
   Lit. sfcuja „Tannennadel und -zapfen", lett. shuja „Tannenreisig", nach
Miklosich EW. 92 zu russ chvoja f., chvoj m. ,.Nadeln und Zweige der
Nadelholzer", klr. chvoja „Tangel, Nadelbaum", skr. hv'oja ,,Baumzweig,
bes. junger, zarter Zweig“ usw. Anlautwechsel sq-          qs- ist trotz Uhlenbeck
                                                           i
                                                                                    :



IF. 7, 9S weniger wahrscheinlicb, als Pedersens KZ. 3S. 394, Jagic-Fest-
        1




sehrift 2 1 8 f , Annahme von si. ch-
                     .
                                                                  =
                                            qh, so dafi die Sippe mit sqh-      qh-                                 :



anzusetzen ist      neben sqtt-ia (lit.) und qsu-oki (si.) als 3. Ablautform viel-
                           ;



leicht sqou-io- in russ. chujz „penis“ (Berneker 408).            Auf *squ-iid mit
<-Weiterbildung fiihrt man zuriick ir. see „Hagedorn“, Gpl. sciad *squ -                                        i
```


## [2026-09-06T21:32:06.386Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD\"; grep -n -i \"xwarsed\\|šēd\\|sed 'sun\\|drafš\\|drafs\\|draxš\\|drxs\\|rōšn\\|rosn\\|axšēn\\|axsen\" PHD.txt | head -30"
}
```


### [2026-09-06T21:32:06.431Z] TOOL RESULT

```
=== PHD
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
643:waxSendag [zwhšndk! | P wxsyndg] blazing, burning.
665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
925:banner drafš, nīšān.
1022:bliss šēdā, xwā(h)rīh.
1092:bright rēšn, šēd, P niság.
3630:shine brāzīdan, drafšīdan, frēgīh- istan, tāftan, (tābīdan).
3740:sorghum gahl, gāwars. sorrel (horse) šēd.
4064:tremble Candidan, drafšīdan, larz- idan.
4555:jaw! Jawēnī šēwan frēst-Ī frēstādan? hil-t hilišnī hištanī šagr, šīr šīrēnīh šīrēn šēb šēb- šēbāg šēbišn šīšag šēdā šēd uzwānī šnāxtan šnāy- šnās- šnāyēn- šnāyēnīdan
4919:lawzēnag rūzīg rozwürag rozan ranjwar rozward rozgar ranjag, rozag rozbinag roz-Saban rosnih rēšn rūšnag rūšngar rodbar rodigan rodig 12го rüdan abàg! rūstūg
5261:v waxšgar м ну а wixšayišnīh wixšayišnīg wisšayišn T?waxsidan waxSendag
5361:garmowar garmowarih *dramanag garmscr darbās drubustih drubust drafš
5362:drafš-
5363:drafšīdan
```


## [2026-09-06T21:32:07.470Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN\"; grep -n -i \"chorschid\\|hvare\\|dirafs\\|dirafš\\;\\|rosan\\|rausan\\|šid\\|schid\" HRN.txt | head -30"
}
```


### [2026-09-06T21:32:07.524Z] TOOL RESULT

```
=== HRN
4566:aw. hvare./sa^tem ^strahlende Sonne'; phlv. ;^"'arset
5606:rosan^ rösanili, roSnäk, arm. LW. r. s/iakuH, rösnntitin,
```


## [2026-09-06T21:32:17.849Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=4555 && NR<=4575' HRN.txt; echo \"=== rosan\"; awk 'NR>=5596 && NR<=5615' HRN.txt"
}
```


## [2026-09-06T21:32:18.854Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"dirafš\\|dirafs\\|diraxs\\|drafsa\\|derafs\" HRN.txt HUB.txt | head -20"
}
```


### [2026-09-06T21:32:19.566Z] TOOL RESULT

```
*) So korrigirt D armesteter, 6t. ir. I, 136.
') Yergl. Bartholomae ZDMG. 44, 552, Hübschmann ebenda
557, Geiger, Lautlehre d. Bei. § 15, 3. Uraprachliche Dialekt-
Verschiedenheit.
«) Ebenso Fr. Müller, WZKM. 5, r>7.- 112 —
aw. Iwar-; phlv. vergl. ;K?/r[pa;Y7// hez\^\ /var[varätt',
ai. svar.
kurd. /or, hilr[efaü; af;'. mar, nmar (Darmesteter>
Chants pop. XXXII); oss. d. yor, t. /Tir (306); si/n.
yer, yiv.
506. x^irsed 'Sonne'.
aw. hvare./sa^tem ^strahlende Sonne'; phlv. ;^"'arset
bezw. ;^?/r8rf, auch y^'arhsel (vergl. Hörn, Mitteilungen,
Heft IV, 34 No. 31).
507. y^itrden (FirdüsT, AM.: p^^'t'/v/ew ^)) essen, trinken',
/uräk, /^(lt\, /unl'i, /uris,
Kää. /ürfdri; /ürest,
ap. vergl. fxa()Tt\y6oa dy&Qomofdyog Ktesias; aw.
i/^X^'a)'-, yntraiti *essen'; phlv. /^'arfan, /^'ar(i)siij
yyartar, y^är etc., bezw. yurtan, arm. LW. yortlk
*Essen, Speise* (d. i. phlv. yurtik, AV.).
=== rosan
licht, Sonne* (824) ; wa/. räiij 'Flamme'.
LW. seldsch. iiruz\if uriiz[yn^ Salemann, Noch
einmal die seldschukischen Verse, Mel. asiat. X, 211;
vergl. yrys 'Glück' ebendas.
630. rözen 'Fenster'.
aw. raoöana- 'Fenster ; phlv. röcan ; ai. röcanä'
(nur 'Licht, hell').
631. vöseti 'leuchtend, hell', rösna^ rösem.
g. rmnäye,
ap. vergl. hoidv/]^); aw. ruoysna' 'leuchtend'; phlv.
rosan^ rösanili, roSnäk, arm. LW. r. s/iakuH, rösnntitin,
LW. af/. rö/cifi, rö/näl; bei. rösani^ rösanal (324);
si;n. rosnagd 'Tageslicht*, sangl. rösnäi 'Feuer.
Vergl. No. 610.
632. röyen ^Butter, Öl*.
Käs. rüyän, rö.
aw. raoyna- 'Ol'; phlv. rökan (d. i. röyan^ päz.
raoyftn), royan (PPGL).
kurd. rrin\ bei. (LW. ?) rogan^ rögan, n. röya/i,
röyin (327); LW. wa;<. rilgfi, royim, minj. royün,
```


### [2026-09-06T21:32:19.613Z] TOOL RESULT

```
HUB.txt:2117:553. Sicher ist hier nur die Gleichung: np. dirafS = phi.
HUB.txt:2118:drafs = arm. draus =■ zd. drafSa- Banner, Fahne.
HUB.txt:2120:ungliicklich. Np. dirafStdan *to flash' JRAS. 1894,
HUB.txt:6062:arm. pUnj; diraz ^) 'lang = zd. drajah-; diraxt *Baum'; dirafs
HUB.txt:6552:tafsldan *heiss werden*, zd. tafsaf, lat. tepesco, u. s. w.; dirafs
HUB.txt:6553:*Fahne, Banner, zd.drafsa-; farman Befehr = phi. /ramflw,
HUB.txt:6603:arab. pers. zift; drauS Tahne, Banner = np. dirafs, zd.
HUB.txt:6604:drafsa-) karatis, karos *Eppich', np. karafs; kausik, kdsik
HUB.txt:8407:laut: dirafs 'Banner -= zd. drafsa-, arm. dram. Jungeren
HRN.txt:4971:aw. drafsa- 'Banner -); phlv. draß^ arm. LW. draus;
HRN.txt:14876:drafsa- 558.
```


## [2026-09-06T21:32:32.125Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=4960 && NR<=4985' HRN.txt; echo \"=== HUB 553\"; awk 'NR>=2100 && NR<=2135' HUB.txt"
}
```


### [2026-09-06T21:32:33.728Z] TOOL RESULT

```
Anders Fr. Müller, WZKM. 5, 66; vergl. aber
unter np. dire/t (No. 548).
552. durust 'rauh, grob, stark, durustt,
ap. iXrfars- 'wagen', adarmans, darsma 'heftig, sehr';
aw. \/dar€S' 'wagen', darsi-; ai. \/dharS', dhfmoii
'J Unter sozen (Öcitc HDJ.— 123 —
Als eine Bestätigung für diese Etymologie dient der
Umstand, dass Herr Prof. Nöldeke mir dieselbe
ebenfalls mitteilte; er war besonders von ai. (Ißtä- in
der Bedeutung *keck, frech' ausgegangen ^).
553. direfS Fahne, Banner'.
aw. drafsa- 'Banner -); phlv. draß^ arm. LW. draus;
ai. drapsd' 'Tropfen*.
oss. LW. (jrisa Tahne (von JStackelberg, Fünf
oss. Erz. 81).
Die ursprüngliche Bedeutung von ar. drapsd- ist
unsicher; Fick, Vorgl. Wörtbch. ^ I, 241, setzt
zweifelnd 'flutend, wallend' als solche an. Np. direfs
soll auch *Blitz, Glanz' bedeuten, vergl. direßän,
direfsiden, jüd.-pers. t^l^E»*!"! (Is. 41, 25) (phlv. draßntk
zitternd', AV. , drafset Bund.); in dieser Bedeutung
scheint ein Zusammenhang mit np. duru/s (so hiutet
die ursprüngliche Vokalisation), diiriiysün, duruyßlden
V
vorhanden zu sein, wie denn auch im 8<ähnäme oft
die Formen in den Varianten durcheinander gehen
=== HUB 553
^dagra- = ^dayra-, das zu der wurde wie zd. anayrandm
= phi. np. aneran^ zd. tiyri- = np. t%r ist.
548. Etymologie dunkel.
550. Etymologie dunkel.^ 61 —
551. Aus ap. *duruva8ti' ware np. durost geworden, vgl.
dur6d (Nr. 555) aus *duiruvata;t'. FUr skr. drdhd- 'fest,
hart, stark, dauerhaft, ganz' (WZKM. 7, 374) = zd.
^dareida- oder *dareSta^ ware im Persischen *dis^ zu
erwarten. Ich kann np. durust ganz, voUstandig,
richtig, wahr, gesund*, paz. durust, drust ganz, voU-
standig Min. Gl. 66 (LW. bal. drust^ afgh. drast ganz,
vollstandig' u. s. w.) nur auf ein iran. "^drusta- = skr.
*drutta-- u. s. w. zuriickfiihren.
552. Np. duruSt rauh, grob, derb, hart (afgh. LW. durust
'rauh, hart streng, miirrisch) setzt ein iran. ^drusta^
voraus. Aus ^drsta^ (= skr. dhr^fd^ *keck, frech*) ware
np. *dist geworden.
553. Sicher ist hier nur die Gleichung: np. dirafS = phi.
drafs = arm. draus =■ zd. drafSa- Banner, Fahne.
Die Vermutung uber die Etym. von np. duruxs ist sehr
ungliicklich. Np. dirafStdan *to flash' JRAS. 1894,
p. 461.
554. Zu damidn *Heilmittel, Mittel* gehort auch arm.
LW. darman *Verpflegung, Pflege, Nahrungsmittel,
Proviant, Futter (ursp. Tnterhalt* von Wzi. dhar
*halten).
555. In den citierten Versen reimt durod SLuf furdd und
xod, aber im Paz. erscheint drud (Min. Gl. 64, Shk. 242).
Das Wort gehSrt zupadrUd (Horn Nr. 288), das bei
Fird. I, 167, v. 689 auf pUd *subtemen', nach N5ldeke
meist auf WSrter mit -ud (wie numud) reimt. Dazu
arm. LW. druat in druati-R 'Lob, Preis, Lobeserhebung ,
druatem lobe, preise'.
556. Np. durudan, diravtdan ernten, mahen, schneiden',
(Fird. I, 18, 12; 22,49), praes. diravam weistauf eine
Wurzel iran. drU. Will man das Wort zu gr. ipenw
```


## [2026-09-06T21:32:44.121Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"drafs\\|draxs\\|\\*drab\\|DRAB\" CHEUNG.txt | head -25"
}
```


### [2026-09-06T21:32:44.171Z] TOOL RESULT

```
4972:9 A separate root *drab-, drap-, with the meanings to sew, join, cut’ < IE *drep- ‘to 
4974:nominal formation Y Av. drafSa- ‘banner’, etc. would contain this root according to 
5851:*drafS ? ‘to "behave" like a banner, fly up, shine, tremble ?' 
5853:*AVESTAN: YAv. drafsa- ‘banner’ (Y 10.14, Y 57.25, Yt 1.11, etc.) 
5877:nominal *drafs/sa- ‘flag, banner’ ?, cf. MP drafs, NP dirafs (> dirafsidan ‘to shine; 
5982:*MIDDLE PERSIAN: ? BMP drp- /drab-/ ‘to wear’ (cf. DKS: 119b, s.v. dausvera 
5985:Pres.: IND. 3pl. BMP drpynd /drabénd/ 
5995:cloth’ ~ Skt. dräpi-. The well-attested ‘flag’ forms, Y Av. drafSa- ‘banner’, etc. may 
6003:drébe ‘frock’, Cz. zdraby ‘rags’, "Illyr." *drap(p)- (^ Gallo-Romance drappus 
25773:‘to stumble, slip’, Pash. drabal ‘to shake, press down’ (LW ?), trap ‘leap, jump’ (< 
33375:drafsa-, 60, 75, 77 
34811:/drafs-/, 75 
35101:dlfš /drafs/, 75 
35115:drp- /drab-/, 77 
47405:drabol, 396 
52510:drabanas, 77 
53217:zdraby, 77 
55752:*drafs 
56624:*drafs 
57819:*diHp, *drafs, *Huah', 
58241:*Cat, *drafs, *rarz, *Orah,
```


## [2026-09-06T21:32:44.838Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"1053\" SYN.txt | head -5; echo \"=== leaf for p1053 = 1053+24=1077\"; awk 'BEGIN{RS=\"\\f\"} NR==1077' SYN.txt | head -40"
}
```


### [2026-09-06T21:32:46.549Z] TOOL RESULT

```
8647:MHG, NHG topf: MLG dop(pe) ‘shell, husk’, further connection dub. Falk-Torp 148. Weigand-H. 2.1053.
14696:(as Miklosich, Berneker). Puscariu 1053. Tiktin 963.
26674:1053
30632:MLG dusen, dosen ‘pass by without thought’, etc., fr. a parallel extension of the root in OF déaf ‘deaf’? and dumb ‘dumb’ (4.95, 4.96). Walde-P. 1.845. Weigand-H. 1.398, 2.1053f. Franck-v. W. 144.
=== leaf for p1053 = 1053+24=1077
 beside adv. dat. in OHG mor- gane, MHG morgen(e), NHG, Du. mor- gen. Weigand-H. 2.219. Franck-v. W. 422f. NED s.v. tomorrow.
Goth. gistradagis (adv. gen.) : OE geostra-deg, etc. ‘yesterday’ (14.49), renders atpuv Mt. 6.30, with puzzling shift of meaning if not merely a blunder in translating. Cf. Brugmann, op. cit. p. 15.
5. Lith. ryto(j), Lett. rit, ritu, ria, orig. ‘in the morning’, fr. Lith. rytas, Lett. rits ‘morning’.
6. ChSI. uéré loc. sing. (renders reg. atpiov in Gospels), also phrase za utra (but in Gospels only ‘early in the morn- ing, tpwt’), similarly SCr. sjutra, Boh. zejtra, Russ. zavira, but Pol. simply jutro (acc. as. adv.), all fr. ChSl. utro, etc. ‘morning’. Berneker 462.
7. Skt. cvas: Av. sir- ‘morning’. Walde-P. 1.368. Walde-H. 1.285. Brug-
mann, op. cit., p. 17.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
14.49 YESTERDAY
Grk. —_xés, Ex0és Goth. . Lith. vakar NG xrés, éxrés, Wes ON i g@r Lett. vakar Lat. —heri Dan. 7 gaar ChSl.  v%%era It. teri Sw. t gdr SCr.  juéer Fr. hier Or geostran dag Boh.  véera Sp. ayer ME __yister(n)day Pol. wezoraj Rum. tert NE yesterday Russ. véera Ir. indhé Du. gisteren Skt. hyas Nir. indé, iné OHG - gesteron Av. te W. doe MHG gester(n)
Br. dec’h NHG gestern
Most of the words for ‘yesterday’ be- long to an inherited group, pointing clearly to an IE adv. of this meaning. The others (the Balto-Slavic, and pop. NG) meant orig. ‘in the evening’ or ‘ate’, whence ‘in the past evening’, and with extension to the entire day ‘yester- day’. Cf. the parallel but forward shift in the history of words for ‘tomorrow’ (14.48).
1. IE *hes, etc. (variant init. com- binations). Walde-P. 1.664. Ernout- M. 449. Walde-H. 1.642f. Falk-Torp 292.
Grk. x6és, and éxéés, adj. xOtés, xGeowds; Lat. herz, later hert (> Ro- mance words), adj. hesternus; Ir. in- dhe, NIr. indé, ine, W. doe, Br. dec’h (cf. Pedersen 1.67, 89, 2.25); (Goth. gistra- dagis, 11.48), OE giestron, usually geo- stran, giostran deg (with geostra adj.), ME yister(n)day, NE yesterday, OHG
gesteron, gesteren, gestre, MHG gester(n), NHG gestern, Du. gisteren; without deriv. suffix and in ablaut ON 7 g@r, 7 gjar, Dan. % gaar, Sw. i gar; Skt. hyas and adj. hyastana-, NPers. di, dig, dine; Alb. dje. On the supposed meaning ‘tomorrow’ of ON 7 g@r, and ‘day after tomorrow’ of OHG é-gestern, é-gestra, often quoted in connection with Goth. gistra-dagis, cf. Brugmann, op. cit. pp. 11 ff.
2. NG pop. yés (not fr. x6és, but) fr. 6yé ‘late’ (14.17), first specialized to ‘late yesterday, yesterday evening’ (as still in some dial.), then extended to ‘yesterday’. Hatzidakis, Mec. 1.122.
3. Lith., Lett. vakar (orig. loc. sg.), Ch8SI. viéera, viiéera, SCr. jucer, etc., gen- eral Slavic (prob. old instr. sg.) fr. the Balto-Slavie word for ‘evening’ (14.46). Walde-P. 1.311. Va
```


## [2026-09-06T21:32:51.991Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"GREEN\\|15\\.68\\|15\\.66\" SYN.txt | head -10"
}
```


### [2026-09-06T21:32:52.043Z] TOOL RESULT

```
9362:4. NIr. glasraidh, deriv. of glass ‘green’ (15.68).
9429:3. Dan. rédlég, Sw. rédlok, epd. of words for ‘red’ (15.66) and ‘leek’ (ON laukr, OE léac, etc.).
13160:Boh. zelina, Pol. ziele : ChSI, Zelent ‘green’ (15.68), zelije ‘vegetables’ (5.65) Lith. Zolé ‘grass’ and ‘herb’, ete, :
15388:SCr., Boh. Russ. rudnik, fr. ruda, ‘ore’, orig. ‘red ore’ : ChSI. rtidrti (15.66).
25868:15.66 Rep
25870:15.68 GREEN
26619:Lett. krasa, esp. ‘beautiful complex- ion, beauty’, as ‘color’ also krass (Lith. krosa ‘color’, in Kurschat krosas, is no longer used, neither form in Lalis or NSB), fr. the Slavic, ChSl., Russ. krasa ‘beauty’, cf. Russ, kraska ‘paint’ (9.88), krasnyj ‘red’ (15.66). Miihl.-Endz. 2.267. Berneker 607 f.
26716:aed Walde-P. 2.322. Emout-M. 671. Goth : dub, NIr. dubh, W., Br. du: ; cufs, ON daufr, etc. ‘deaf’, Grk. blind, dark’, rS¢os ‘smoke, vapor, » thd ‘smoke, burn slowly’, fr. ~ extension of *dheu- seen also fuscus ‘dark’, etc., 15.68). 1’, here prob. fr. ‘confused,
26729:1056 SELECTED INDO-EUROPEAN SYNONYMS 15.66 RED Grk. — épvOpéds Goth. raups Lith. raudonas NG KOoxxtvos ON rauodr, rjodr Lett. sarkans Lat. ruber (rufus, russus) Dan. rd ChSl.  Giiminy, (Giveni, It. TOsso Sw. rod ritdrit) : Fr, rouge OE réad, réod SCr.  crven Sp. rojo ME reed Boh. — éerveny Rum. rosiu NE red Pol. —czerwony Ir, derg, ritiad Du. rood Russ. krasnyj NIr.  dearg, ruadh OHG rat Skt. rakta-, lohita- W. coch, rhudd MHG rat Av. raoisita- Br. ruz NHG rot
26765:Ir. glass ‘blue-gray, green-gray’ (e.g. ‘blue’ of the eye, Windisch, Tain 1.5550; ‘sray’ of mist, id. 1.5042, 5058; ‘green’ of garlic, Anc. Laws 2.254, 1.9), NIr. glas ‘green, gray, bluish-gray’ (Dinneen), W. glas ‘blue’, but also ‘gray, green’ (Spur- rell), Br. glas ‘green, blue, gray’ (cf. Gall. glastum ‘name of a plant’), see under ‘green’ (15.68).
```


## [2026-09-06T21:32:58.746Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"axsaena\\|aysaena\\|axsaina\" SYN.txt | head; echo \"=== page 1053 header\"; grep -n \"^1053 \\|1053 SELECTED\\|SYNONYMS 1053\" SYN.txt | head"
}
```


### [2026-09-06T21:32:58.805Z] TOOL RESULT

```
=== page 1053 header
```


## [2026-09-06T21:33:01.606Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=25860 && NR<=25885' SYN.txt; echo \"=== find 1052/1054 headers\"; grep -n \"105[0-9] SELECTED\\|SYNONYMS 105[0-9]\" SYN.txt | head"
}
```


### [2026-09-06T21:33:03.525Z] TOOL RESULT

```
For the purposes of our discussion it is Fett to follow the time-honored oom of the senses as smell, taste, ae ng, sight, and touch, ignoring the ‘t en technical elaboration of the old Ouch’,
Aan the spheres of the several tions Ga are certain logical distinc- Some ie find linguistic expression in Which Suages and not in others and for ay eoreover, work out differently Buistie » Several Senses as regards lin-
°nsciousness of the relations.
Digitized by Arya Samaj Foundation Chennai and eGangotri
CHAPTER 15 SENSE PERCEPTION
15.57 Bricut
15.61 Cotor (sb.) 15.62 Lieut (in Color) 15.63 Dark (in Color) 15.64 Waite
15.65 Buack
15.66 Rep
15.67 BLUE
15.68 GREEN
15.69 YELLOW
15.71 Toucs (vb.) 15.72 Fret (vb.), Feat or 15.73 Toucs (sb. subj.) 15.74 Harp
15.75 Sort
15.76 RoucH
15.77 SMoorH
15.78 SHARP
15.79 Buonr, Duty 15.81 Heavy
15.82 Licut (in Weight) 15.83 Wet, Dame 15.84 Dry
15.85 Hot, WARM 15.86 Cop
15.87 CLEAN
15.88 Dirty, SoILED
First, the difference between the sub- jective and the objective notions. These terms (hereafter subj., obj.) apply to both the noun and the verb, and so are preferable to transitive and intransitive, which are applicable only to the verb. NE smell and taste, as verbs or nouns, are used both subjectively, with refer- ence to the person perceiving, and objec- tively, with reference to the object which stimulates the sense. I smell the rose, taste the apple and it smells sweet, tastes good, and similarly a person’s sense of
1017
CC-0. In Public Domain. Gurukul Kangri Collection, Haridt
Digitized by Arya Samaj Foundation Chennai and eGangotri
=== find 1052/1054 headers
26581:1050 SELECTED INDO-EUROPEAN SYNONYMS
26684:1054 SELECTED INDO-EUROPEAN SYN ONYMS 15.64 WHITE Grk. —_Aeuxds (&pyés) Goth. hweits Lith.  balias NG aompos ON hvitr Lett. balts Lat. albus, candidus Dan. huid ChSl. bal It. bianco Sw. hvit SCr. _bijel Fr. blanc OE hwit Boh.  bily Sp. blanco ME — whit Pol. bialy Rum. alb NE white Russ.  belyj Ir. Jind, gel, ban Du. wit Skt. gukra-, cveta-, arjung- NIr. ban, geal, fionn OHG  (h)wiz Av. spaéta-, curiae co W. gwyn, can MHG wiz Br. gwenn, kann NHG weiss
26729:1056 SELECTED INDO-EUROPEAN SYNONYMS 15.66 RED Grk. — épvOpéds Goth. raups Lith. raudonas NG KOoxxtvos ON rauodr, rjodr Lett. sarkans Lat. ruber (rufus, russus) Dan. rd ChSl.  Giiminy, (Giveni, It. TOsso Sw. rod ritdrit) : Fr, rouge OE réad, réod SCr.  crven Sp. rojo ME reed Boh. — éerveny Rum. rosiu NE red Pol. —czerwony Ir, derg, ritiad Du. rood Russ. krasnyj NIr.  dearg, ruadh OHG rat Skt. rakta-, lohita- W. coch, rhudd MHG rat Av. raoisita- Br. ruz NHG rot
26769:1058 SELECTED INDO-EUROPEAN SYN ONYMS
```


## [2026-09-06T21:33:08.621Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=26640 && NR<=26690' SYN.txt"
}
```


### [2026-09-06T21:33:10.149Z] TOOL RESULT

```
3. NIr. éadtrom, ‘light’ in weight (15.82), also ‘light’ in color (Dinneen McKenna), doubtless after the double use of NE light in which two different words are merged.
ME pale (NE also Sometimes in this sense, as pale blue, etc., cf. NED S.V, fr. OF r. pale, Lat. pallidus ‘pallid,.pale’ ‘ Grk. zedtés ‘livid’, odds ‘gray’, Skt, palita- ‘gray, hoary’, pandu- ‘whitish yellow, white’, OE fealo, OHG falo, Lith. palvas ‘fallow’ (‘light brownish or red- dish yellow’), ChSI. plavii (renders Aeukds Jn. 4.35, but with reference to fields of grain, hence here also ‘yellowish’), Walde-P. 2.53 f. Ernout-M..725.
15.63 DARK (in Color) Grk. —_péAas, xedarvds Goth.~ i... Lith. tamsus NG Babbs, oxodpos ON dékkr Lett. tums Lat. fuscus, pullus Dan. mérk, dunkel ChSl.  timinit It. scuro, cupo Sw. mork, dunkel SCr.  taman Fr. foncé, sombre OE wann. (deorc) Boh. temny Sp. obscuro ME dark, wan, dosc Pol. ciemny Rum. inchis NE dark Russ. temnyj Tr. dorche, temen Du. donker Skt. krsna-, ¢yama-, Nir. dorcha OHG  tunchal tamasa- W. tywyll MHG _ tunkel Av. axSaéna- Br. du NHG dunkel
Many of the words for ‘dark’ in color are the same as those for ‘dark’ = ‘lack- ing light’, these again mostly connected with the sbs. for ‘darkness’ already dis- cussed in 1.62. Some are the same as, or derived from, those for ‘black’; some rest on the notion of ‘deep’; others are of various sources.
1. TE *tem-, etc., as in sbs. for ‘dark- ness’ (1.62). Walde-P. 1.720f,
Ir. temen, temnide (here also W. tywyll? cf. ref. in 1.62); Lith. tamsus, Lett. tumss; ChSl. timtni, SCr. taman, etc., general Slavic; Skt. tamasa- (AV 11.9.22).
2. Grk. uédas, xedauvds ‘black’ (15.65), also ‘dark’ in color,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
NG ats ‘deep’ (12.67), also ‘dark’ in color. Cf. It. cupo, Fr. foncé, and NE deep in deep red, deep dyed, etc.
NG oxodpos, fr. It. scuro (below).
3. Lat. fuscus : ME dosc, dusk ‘dark, dark-colored’ (NE dusk sb., dusky adj.), Skt. dhisara- ‘dust-colored’, etc., prob. fr. the root in Grk. éiw ‘blow, storm, rage’, Skt. dhvaris- ‘go to pieces, fall ruin’, OHG tunist, dunst ‘storm, vapor OE dist ‘dust’, etc. Semantic develop-
ment from ‘hazy, dusty, smoky’ to ‘dust-, smoke-colored’, etc. Walde-P. 1.846. Ermout-M. 405, WaldeH. 1.572.
Lat. pullus : pallére ‘be pale’, pallidus
‘d’, etc. (see 15.62). Walde-P. pall M. 725, 823.
fr. Lat. obsci- rk, lacking light’, as orig. ‘covered’ G soitr ‘shelter’, etc. fr. the root in » Walde-P. 2.547. Er-
? ale inout 953, Brn Sp. o(b)scuro,
It. scuras rus‘d
ean ‘tub, cask’).
ne Pics, pple. of foncer ‘deepen (a sta! make darker’, orig. ‘furnish with a bottom’, fr. fond, OFr. fons ‘bottom’, fr, Lat. fundus ‘bottom’. REW 3585.
Wartburg 3.870, 874.
Fr. sombre, prob. postverbal to an OFr. *sombrer, fr. VLat. subumbrare, fr. umbra ‘shade’. REW 8405. Gamill- scheg 806 f.
Rum. tnchis, lit. ‘closed’, pple. of in- chide ‘shut, close’, and so used as oppo- site of deschis ‘open’ and ‘light’ (15.62).
4, Ir. dorche, see under sorche ‘bright’ (15.57).
Ir. temen, W. tywyll, above, 1.
Br. du ‘black’ (15.65), also ‘dark’, as glas du ‘dark green’.
5. ON dékkr, OS dunkar, Du. donker, OHG tunchal, MHG tunkel, NHG dun- kel (> Dan., Sw. dunkel), see under ‘darkness’ (1.62).
Dan. mgrk, Sw. mérk : ON myrkr, i ‘dark’ and ‘darkness’, etc.
OE wann, ME wan (NE wan now ey ‘pale, pallid’), etym.? NED s.v. an,
ee deore (but mostly of absence of
= not of color, except of clouds,
a. &te.), ME, NE dark, see under arkness’ (1.62),
ME dose : Lat. fuscus (above, 3).
SENSE PERCEPTION
Digitized by Arya Samaj Foundation Chennai and eGangotri
1053
6. Skt. krsna-, gyama ‘black’ (15.65), also ‘dark’ in color.
Av. axgaéna-, neg. cpd. : rsaéta- ‘bright’ (15.57). Barth. 51.
15.64-15.69. Abstract color names are late in linguistic history. They are generally lacking in languages of primi- tive peoples, whose notion of color is closely bound up with that of a specific object, as, for example, ‘white’ with snow or milk, ‘blue’ with the sky, ‘green’ with plant life, etc. Many of the words dis- cussed below, and others, like NE orange, violet, have just such an origin.
Tn the IE period the development had probably not advanced much beyond this stage, and even in historical times there is still much fluctuation and over- lapping in the application of color words. There is only one group of cognates that is so widespread and consistent in mean- ing as to point clearly to an IE color name with definite application, namely the group for ‘red’. There are some cases of agreement between two branches in words applied to the same color, and there are some extensive groups from a common root but applied to a variety of colors, so that the primary application is obscure. The most con- spicuous interchange is in words for ‘green’ and ‘yellow’, perhaps because they were applied to vegetation like grass, cereals, etc., which changed from green to yellow.
For the Skt. terms, of Macdonell- Keith 2.246 f.
Wood’s Color-Names (Halle, 1902) covers a vast range of material and deals with the remoter root connections.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Oss ee te Jn arr
Digitized by Arya Samaj Foundation Chennai and eGangotri
1054 SELECTED INDO-EUROPEAN SYN ONYMS 15.64 WHITE Grk. —_Aeuxds (&pyés) Goth. hweits Lith.  balias NG aompos ON hvitr Lett. balts Lat. albus, candidus Dan. huid ChSl. bal It. bianco Sw. hvit SCr. _bijel Fr. blanc OE hwit Boh.  bily Sp. blanco ME — whit Pol. bialy Rum. alb NE white Russ.  belyj Ir. Jind, gel, ban Du. wit Skt. gukra-, cveta-, arjung- NIr. ban, geal, fionn OHG  (h)wiz Av. spaéta-, curiae co W. gwyn, can MHG wiz Br. gwenn, kann NHG weiss
Most of the words for ‘white’ come from the notion of ‘bright’.
1. Grk. Aevxés : Lat. lx, OF léoht, etc. ‘ight’ (1.61), Lat. lacére, Skt. ruc-, etc. ‘shine’ (15.56), IE *leuk-. Walde-P. 2.408 ff.
Grk. apyés ‘glistening, white’ (also apyis, apynes, apyervds), Skt. arjuna- ‘light, white’, Toch. A arki, Hitt. narkis ‘white’, fr. the root seen in words for ‘silver’, Grk. épyupos, Lat. argentum, etc. (9.65). Walde-H. 1.66; 848.
Byz., NG dozpos, fr. Lat. asper ‘rough’ as used of work in bas-relief, as aspera pocula, esp. coins as nummi asperz (cf. Thes. 2.809), hence Byz. dozmpos or dompov name of a coin, esp. a silver coin, and from the latter the use as adj. for ‘white’. Psichari, MSL 6.312f. G. Meyer, Neugr. Stud. 3.12.
2. Lat. albus (> Rum. alb), Umbr. alfu ‘alba’ : Grk. ad¢és ‘dull-white lep- rosy’, dAdots* evxobs (Hesych.), OHG albiz, ON elpir ‘swan’, etc., IE *albho-. Walde-P. 1.93. Ernout-M. 31f. Walde- H. 1.26 f.
Lat. candidus ‘bright’ (15.57), also ‘white’.
```


## [2026-09-06T21:33:21.705Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o \"\\[pdf page [0-9]*\\]\" BQT_v2_pages.txt | head -3; grep -c $'\\f' BQT_v2_pages.txt; head -20 BQT_v2_pages.txt"
}
```


### [2026-09-06T21:33:23.515Z] TOOL RESULT

```
680
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬

                      ‫‪۴2 ۱‬‬

                  ‫رک یمن‬
                  ‫م سارو کی و ررك‬


                 ‫جلررومدا‬
             ‫چاپ دوم فروردین ‪۳۴۳۱‬‬
                 ‫با تجدید نظر کامل‬
          ‫بسرمایه کتابفروشی ابن سیتناپران‬
```


## [2026-09-06T21:33:27.433Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:756 --image 2>&1 | head -60"
}
```


### [2026-09-06T21:33:29.247Z] TOOL RESULT

```
no scan of BQT covers printed page 756 (see 'scans' in refs_online.json)
```


## [2026-09-06T21:33:31.484Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\""
}
```


### [2026-09-06T21:33:33.500Z] TOOL RESULT

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


## [2026-09-06T21:33:37.576Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==217' BQT_v2_pages.txt | head -80"
}
```


### [2026-09-06T21:33:39.504Z] TOOL RESULT

```
                                               ‫بیان ددواهرم‬

                           ‫وبعریی ورق‌النیل خوالند‬
 ‫خطر یه = بروزن‌هسابه‪ .‬جامهپشمن‬                         ‫جملةٌ هفت خط جام جم ‪ ,‬وآنرا خط سياه نیز‬
                                                                                                          ‫وت‬
 ‫درویثان است که رسمانها ویشمها اآنز‌آوخته‬
                                ‫باشد ‪٩‬‏ ‪3.‬‬               ‫خط اشات ه ام خط پنجم است از‬
‫خطی که تازه از رخارة‬            ‫سبز ‪-‬‬    ‫خط‬                        ‫جام چمشید »آ‪,‬آوتراخط خطر گوند ‪.‬‬
‫خوبان برآمده باشد ‪ -‬و نوشته و خطی را لیز‬                 ‫خط اول ‪ -‬کتابه از الف است که‬                     ‫‪.‬‬
 ‫کوبند که‌ازعالم(‪)4‬غیب مرقوم‌شده باشدیعنی کی‬                         ‫حرف اول حروف تهجی باشد‪ -‬ک‬
                                                          ‫ونابه از عرش‬
 ‫که توشته است ‪-‬‬
              ‫نداند که از کجا آمده اعت و‬                                  ‫‪.‬‬   ‫اعظم ‪ -‬ومكة معظمه هم هت‬
 ‫وخط شب رانیز کودند که خط سیاه است واا‬
                                                         ‫خط بر خود دادن ‪ -‬کنابه از‬
                 ‫یند ‪.‬‬ ‫گقوهم‬
                           ‫یزر‬
                             ‫خمط ا‬                                             ‫موچلکا وسجل لوشتن باشد ‪.‬‬
 ‫نادبه از خط یز باشد‬
                   ‫خط سکام‬
                                                                              ‫جملهةً حفت خط جام جمشید ‪.‬‬
‫ولام‬   ‫‪-‬‬   ‫بمعتی‌خط سداه‌است‬    ‫‪-‬‬   ‫شب‬   ‫حط‬
                                                         ‫)(( انت‬   ‫نام خط دوم‬       ‫بغد‌اد‪.‬‬          ‫خط‬
‫یکی از خطوط حام جم هم هت که خط ازرق‬                                ‫‪.‬‬   ‫اند‬
                                                                         ‫‌ول‬
                                                                           ‫ها‬‫فیتخط‬
                                                                                 ‫ازجام جم ؛ وگبعض‬
                                          ‫باشد (‪. )۵‬‬
                                                          ‫خط جور ۔ نامخط اول جام جم‌است‬
                                                                                ‫که خط لب جام باشد ‪.‬‬
 ‫سار‬       ‫خطر‬   ‫و‬   ‫خوف‬   ‫آن‬   ‫خطی است که در‬      ‫و‬

                                              ‫باشد ‪.‬‬    ‫) » بمعنی قدر‬ ‫‪۳‬‬ ‫(‬ ‫ر‬ ‫ظ‬ ‫ن‬ ‫ن‬ ‫خطره بر وز‬
                                                         ‫ومذزلت وشان وش وکت وعظمت باشد ‪ -‬وبمعنی‬
‫درلونه ‪ -‬نام خط هفتم است‬
                       ‫خط قف‬                                                                ‫آفت ‪-‬‬
                                                                                         ‫کودش‬
                                                                                      ‫روار‬
                                                                                   ‫ویی‪-‬‬
                                                          ‫دراسب دوالی ‪-‬‬        ‫وتن‬
                                                                                 ‫س‬
                                         ‫از جام جم ‪.‬‬
                                                         ‫وشرط درتبراندازی عربی است و‪-‬وسمه را فيز‬
 ‫خط کاسه گر(‪ - )7‬نام شخشطم‌است‬                           ‫گوبند ؛ وآن بر گی باشدکه بدان خضاب کنند‬

   ‫(ع)چك‪,‬‬              ‫(‪)e‬‏ چك‪.‬چش‪ :‬سطی ‪.‬‬               ‫)‪ (۱‬چك ‪ :‬دوم‪.‬‬      ‫‪۱‬‬      ‫)‪ ۱‬چك‪ :‬سوم‪.‬‬
                       ‫(‪ )۰‬خم‪ : ۱‬کاسگر ‪.‬‬               ‫(‪. )۵‬چك » چش ‪ :‬است ‪.‬‬             ‫عالم ‪.‬‬       ‫چش ‪- :‬‬

                                                 ‫همین معنیرا در «ختوانه» (ه‪.‬م‪ ).‬وو‬               ‫‪۱‬‬
       ‫‪ ۵‬خط ریحان‪,‬خط ریحالی ‪ -‬یکی از اقسام خطوط مشهور متأخران «محمد قروینی‬
                       ‫دبوان حافظص قکوءح ‪4‬بنقل از تلخیص کشف الظنون دعنروان(علالخط) » ‪:‬‬
                 ‫هزار شش لگارد ز خط ریحالی ‪.‬‬
  ‫د حافظ شیرازی ص قکو»‬
 ‫(برهان فاطع‪)۰۰۱‬‬
```


## [2026-09-06T21:33:51.756Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in خشیسار خشین خشنسار خشی خورشید جمشید درفشیدن; do echo \"### $w\"; grep -n \"$w\" BQT_v2_pages.txt | head -4; done"
}
```


### [2026-09-06T21:33:53.848Z] TOOL RESULT

```
### خشیسار
### خشین
12527:‫و بشاین نقطه دار همآمده است چه در فارسی‬                           ‫پوشند ‪ -‬وبکر اول مخفف خشین است» ‪ ۰‬آن‬
12654:  ‫‪ - ۲‬مصحف خشنسار (ه‪.‬م‪ ).‬و(خشینسار‬                 ‫مخفف | خشیج (ھ‪.‬م‪(.‬‬           ‫خشیج»‬         ‫جمم‬      ‫‪-‬‬   ‫‪۹‬‬
12662: ‫میماندچه خشین بازسیاه رنگه؛ وساربه‌عنی مالند‬             ‫بای فارسی وسکون‬     ‫بقح‬     ‫=‬   ‫ند‬     ‫حشن‬
12666: ‫خشینه = بروزن دفینه ‪ ۰‬بمعنی خشین‬
### خشنسار
12654:  ‫‪ - ۲‬مصحف خشنسار (ه‪.‬م‪ ).‬و(خشینسار‬                 ‫مخفف | خشیج (ھ‪.‬م‪(.‬‬           ‫خشیج»‬         ‫جمم‬      ‫‪-‬‬   ‫‪۹‬‬
### خشی
2358:   ‫وخشیارشا ودیگر یادشاعان هخامنشی را بجم(جمتید) انتاب داده اند و نام «تخت جمشید» خود‬
9089:  ‫عالم بود ‪ .‬از تألِفات وی ميزان الحكمة در فلفه است که خشی از آن در‬                                ‫اد‬
12525: ‫بزر کهتیرء رن میانسرسفید باشد و ترکان‬                            ‫خشی ه بنتح اول بروزن چمن گ‪.‬یاهی‬
12527:‫و بشاین نقطه دار همآمده است چه در فارسی‬                           ‫پوشند ‪ -‬وبکر اول مخفف خشین است» ‪ ۰‬آن‬
### خورشید
655:‫جان است » و خورشید در عرف ایشان روج‬
664:‫جامه دنریلزدت «کنایه ازمزت‬                      ‫جامه خورشید » کنابه از زمین‬
1084:‫جییره = بر وزن کبیره ؛ مستعد شدن‬                         ‫جبة خورشید و ماه د کنابه از‬
2547:      ‫در ودا یمه(جم) پسرخورشید ونضتین بشری است که مرکه‌براو چیره شده » بردوزخ حکومت‬
### جمشید
705: ‫ردنر مزبور بمناسبت شهرت جمشید وبکی داستن او باسلیمان * جاممزبور را‬
2340:‫وجمشید همهست ‪ . ۴‬لیکن درجایی که بانگین | میشود اسکندر ‪ -‬و بمعنی مردمك چشم هم‌بنظر‬
2357:  ‫شبیه بود و ایرانان م رکز جمشید داستانی‌را کشور فاری‌مبداننته‌اند و آثاربافی ماندء داربوش‬
2358:   ‫وخشیارشا ودیگر یادشاعان هخامنشی را بجم(جمتید) انتاب داده اند و نام «تخت جمشید» خود‬
### درفشیدن
17585:        ‫‪۱‬‬                                            ‫‪ ۲‬اسم فاعل از« درفشیدن» («‪.‬م‪: ).‬‬
```


## [2026-09-06T21:33:58.263Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 12525 12662 17585; do n=$(head -n $L BQT_v2_pages.txt | grep -c $'\\f'); echo \"line $L -> leaf $n -> printed $((n+540))\"; done"
}
```


### [2026-09-06T21:34:00.162Z] TOOL RESULT

```
line 12525 -> leaf 213 -> printed 753
line 12662 -> leaf 215 -> printed 755
line 17585 -> leaf 296 -> printed 836
```


## [2026-09-06T21:34:04.688Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==216' BQT_v2_pages.txt"
}
```


### [2026-09-06T21:34:06.300Z] TOOL RESULT

```
  ‫جع بت چدم‬                                                                                          ‫~ ‪۷۷‬‬


 ‫بنند که ییاز سیامرنگه‬    ‫وآ‬ ‫گهت‬
                               ‫را خشن سار بج‬
 ‫میماندچه خشین بازسیاه رنگه؛ وساربه‌عنی مالند‬             ‫بای فارسی وسکون‬     ‫بقح‬     ‫=‬   ‫ند‬     ‫حشن‬

                                             ‫باشف ‪.‬‬

 ‫خشینه = بروزن دفینه ‪ ۰‬بمعنی خشین‬
 ‫است که هر چیز سباه رنگه مابل (‪ )۱‬بکیودی‬
                                                          ‫ا وی زک نوی ار اچ ات ران‬
                                                          ‫بمفتی کبودرتگڭ‬     ‫خسن‬     ‫باشف جه‬    ‫می‬      ‫کیودرنگف‬

‫باشد ‪ - ۴‬و بازبرا نیز گوبند که پشت اوکبود‬                                       ‫وید یمعئی غلواح باشد ‪.‬‬
‫و ثیره رنگگ بود ؛ و بعضی گوبند مرغابی سیاه‬
‫رنگ است‪ .‬بکبودی مابل ‪ - ۴‬و بمعنی سفید‬                     ‫خشین ساد؟ ‪ -‬با سین بی نقطه بر‬
 ‫گلوهیند‬
       ‫و خودرنگ‌هم بمنظدرهآ‌است کهآ نرا م‬                ‫باشد که شت او‬      ‫نوعی از مرعای‬           ‫وزن زم‌ندار‬

                         ‫مشدد ‪.‬‬         ‫امم‬
                                          ‫لمی‬
                                            ‫وتح‬
                                              ‫بف‬          ‫داردواو‬   ‫سفیدی‬   ‫سرخال‬    ‫ویرمان‬     ‫ساه رنگف است‬




                                                 ‫بیان بدارهم‬

          ‫برسه لغت و کنات‬               ‫در خای نقطه دار با صاد بی‌نقطه مشتمل‬


       ‫ضدیتی که باهم دارند ‪.‬‬   ‫ار بعه است ببب‬             ‫وسل »‬       ‫» بنتح اول بورذزن‬             ‫حصل‬
 ‫چشم ‪ ۰‬کنابه از کطان‬        ‫حصم بك‬
                                                             ‫نرد وشرط وییمان درتیراندازی و گروبندی(‪)۲‬‬
‫است ‪ -‬و دجال را لگیوزبند ‪ -‬و بمعنی دلهم‬
                                                             ‫قمار نیزهست‪ = ۹‬ویمه‌نی کمبتین هم بنظرآمده‬
‫هت که بعربی قلب خوانند ‪ -‬وکنایه ازآسمان‬                                                                 ‫است ‪. ۷‬‬
                                             ‫باشد ‪.‬‬
                                                             ‫خصمان سفلي ‪ -‬کنابه از عناصر‬




                                             ‫(‪ )۲‬چش ‪ + :‬در ‪.‬‬                   ‫(‪ )۱‬جك ‪ :‬مائل‪.‬‬

                  ‫« افئین »‬    ‫مصحف‬      ‫‪,‬‬   ‫ظ‬    ‫حدود العالم و معجم البلدان نیامده ‪.‬‬      ‫در‬   ‫‪-‬‬   ‫‪۱‬‬

                         ‫(و‪ -‬م‪(.‬‬    ‫خشسار‬         ‫) =‬    ‫(ه‪.‬م‪٣+ (.‬‏ سار ) سر‬        ‫از ‪ 2‬خشن‬    ‫‪_۴‬‬

                                  ‫گتاکن (مروزی) گو ف ‪:۰‬‬             ‫جر مه رنك دود‬    ‫(خشمته‪.‬‬    ‫‪۳ ۳‬‬


               ‫که فرستد لبای حور المین‪».‬‬                             ‫خشننه را بهار‬    ‫کوهار‬

   ‫ورك ‪ :‬خشن ‪.‬‬    ‫‪۶‬‬     ‫«لفت فرس‬

               ‫(عر)‪ .‬رك ‪ :‬فاموس وشرح آن ‪:‬‬                ‫‪6‬‬            ‫رك ‪ :‬خشن » خشن ‪.‬‬              ‫‪۴‬‬

  ‫و نیز درعربی‌یکی‬      ‫‪۱‬‬           ‫‪.‬‬    ‫خصلت اصاف زخصلش مجوی ‪ .‬نظامی گنجوی «گنجینه ‪۲۵‬‬
                                                                  ‫ازنامهای لۇلۇ ‪«.‬الجماهر ببرونی‪. ۷۰۱‬‬
```


## [2026-09-06T21:34:23.458Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/279.jpg 2>/dev/null; pdftoppm -f 279 -l 279 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg279 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T21:34:25.606Z] TOOL RESULT

```
site/pages/279.jpg
total 23664
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:34 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     484 Sep  6 17:33 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb   97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb   41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb 8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb   25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb  105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb  122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70575 Sep  6 17:34 pg282.png
```


## [2026-09-06T21:34:29.005Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg279.png"
}
```


### [2026-09-06T21:34:29.352Z] TOOL RESULT

```

```


## [2026-09-06T21:34:29.349Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T21:34:44.085Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 279 -l 279 -r 600 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg279hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg279hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.20*w),int(0.135*h),int(0.50*w),int(0.165*h))).save('$S/p279_xsaeta.png')\nim.crop((int(0.20*w),int(0.455*h),int(0.60*w),int(0.52*h))).save('$S/p279_greek.png')\n\""
}
```


### [2026-09-06T21:34:48.218Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-06T21:34:50.596Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p279_xsaeta.png"
}
```


### [2026-09-06T21:34:50.612Z] TOOL RESULT

```

```


## [2026-09-06T21:34:53.962Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg279hi.png'); w,h=im.size\nim.crop((int(0.21*w),int(0.155*h),int(0.42*w),int(0.175*h))).resize((int(0.21*w*2),int(0.02*h*2))).save('$S/p279_word.png')\n\""
}
```


### [2026-09-06T21:34:55.997Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:34:58.373Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p279_word.png"
}
```


### [2026-09-06T21:34:58.442Z] TOOL RESULT

```

```


## [2026-09-06T21:34:58.440Z] INPUT

[Image: original 2142x264, displayed at 2000x246. Multiply coordinates by 1.07 to map to original image.]


## [2026-09-06T21:35:08.345Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==249' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-06T21:35:10.182Z] TOOL RESULT

```
           ‫ات‬
            ‫سپو‬                                                                                                       ‫خوره‬


 ‫خورة استخر »‪.‬خورة داراب » خورة شایور‪ .‬خورة‬                               ‫بوری است از جالب خهای تعالی که بر خلابق‬
 ‫قباد ‪ - ۴‬و ناممرضی است مهلك وانرا بعربی‬                                  ‫بوسله آن فادر شو ند بر باست‬     ‫که‬    ‫فار مشود‬

 ‫جذام خوانند؟ ‪ .-‬ویفتح اول وسطون وفتح ثالث‬                                ‫وضمتها ‪ .‬و ازین نورآ نجه خاص است‬            ‫وخ_فتها‬
 ‫است که‬               ‫درختی‬    ‫آڼ‬    ‫‪9‬‬   ‫‪۰‬‬
                                             ‫خر زهره کروایند ‪۴‬‬             ‫بیادشاهان بزر که عالم و عادل تعلق مبگیرو ‪-‬‬
     ‫رت اف سای ‪۶‬‬                                      ‫و‬    ‫کان‬
     ‫بمعنی پابمال هم آمده اس‬                      ‫و‬   ‫دفلی خوانند ‪-‬‬        ‫<سد‬   ‫حکمای فری‌فاری رایپنج حصه کرده‌اند وه‬

‫ار‬        ‫|نرا بر‬
                ‫ا‬       ‫کد‬     ‫‪۵‬‬    ‫ی‬
                                    ‫اول نوعی از جوال ا ت‬       ‫وسم‬       ‫‪ :‬خورءا ردشیر ‪.‬‬   ‫ترهب‬
                                                                                              ‫نام نهادهأ ند ماين ت‬   ‫را خوره‬




     ‫=) است ( رک ‪ :‬خورة آردشیر) مجازاً‬
                                     ‫‪ - ۱‬ماین معنی نیز مأخوز ازه‌منی خوره ف(ر‬
     ‫خوره ( = خره ) را یمعئی ناجیه و بخش گرفته اند و اختصاص بقاری ندارد ‪ .‬معرب آن‬
     ‫«ولات پاری بنج کورندت ‪ .‬هر کورتی بیادشاهی که نهار آن‬                                                  ‫«کورة » است‬
         ‫‪۰‬ورة دارایجرد ک‪.‬ورء اردشر‬
                                 ‫کورت بکاغرادزها‌واست‌بازخوانده‌اند برین جملت‪ :‬کورة اصطخر ک‬
     ‫خوره » کورة شاپورخوره ‪ .‬کورة قبادخوره ؛ وهر کورتی ازین پنج کورت چند شهرونواحی است ‪».‬‬
     ‫‪ ۴‬باین معنی از ‪ :‬خور (خوردن ) ‪» +‬‬          ‫د فارسنامة این‌البلخی ‪ › ۱۲۱‬و ركه ‪ :‬خره ‪.‬‬
     ‫بخورد ودناابونددگمراتند زنگه‌ودیو کودغاتغر ابا‬                          ‫(یوند نبت واتصاف) هرچیزی که ‪0‬‬
     ‫‪.‬‬      ‫ود‬    ‫»‬    ‫خر ره‬   ‫‪۰‬‬    ‫حوره‬     ‫رک‬              ‫(ظم‌الاطباء) ‪ .‬راجح بجذام ‪ ,‬رکه ‪:‬بحرالجواهر ‪.‬‬
                                                                                                         ‫وجذام نا‬
                                                                                                    ‫دقیقی (طوسی)گفت ‪:‬‬
                                                                      ‫دفلی است دشمن من و من شهد چان نواز‬
                ‫چون شهد طمم حنظل وخوره بجا ( کجا ‪ ۰‬دهخدا ) نور“‬
         ‫‪٩‬‏ ‪.‬‬    ‫لفت فرس ‪۶۱6‬‬

                                    ‫ب‪-‬اين معنی معرب آن «خرح » باضمول و فتح دوم ت«فس» ‪.‬‬
                                                                                                      ‫شه از صفحه ‪۹۸۷‬‬
     ‫سران و بزرکان کشور است ‪ .‬در زامیادبشت اخزورة ( فر ) هوشنگ ونهمورت و جمنید ودیگر‬
     ‫روز گار بادشاهی ‪1-۳‬‬                     ‫از سپری شدن‬      ‫بادشاهان دبشدادی و کیانی تا گناس ماد شده است ‪ .‬یں‬
     ‫کاب وک خو (فر) بکسی تعلق تناما اھورمروا آغرا ا دوز راخ برای آبزانان‬
     ‫نگاه دارد وسوشبانت ‪( 6۳290505‬موعود زرتشتی ) از فر امزدی برخوردار شود و اکزنار‬
                                                              ‫ویتی را پراز راستی و داد کند ‪.‬‬
                                                                                           ‫درباچة هامون برخیزد گ‬
         ‫شبخ اشراق سهروردی ازقول زردشت نکقنلد‪« :‬خره نورت که ارذات خداوندی ساطم میگردد‬
     ‫کدیگر رباست بابند و بمعونت آن هربك بر عملی و صناعتی متمک نگردد *‬    ‫یر‬
                                                                          ‫و بدان مردم ب‬
      ‫‪+‬کمةالاشراق ‪٩ ۲۷۳ ۱۷۳‬‏ ونیزسهروردی دررسالةٌ ‪ ۶‬برتونامه » آرد ‪ :‬وهر یادتاهی حکمت‬ ‫ح‬
         ‫بداند وبرنشاش‌ونقدبس نورالانوارمداومت کند‪ .‬چنانکه گفتیم اورااخره کیانی> دهد و‪#‬نفوررانی»‬
     ‫بخشند و «بارق الهی » اورا کسوت هیبت وبهاه بپوشاند ورئیس طبیه‌ی عالم شود ‪ .‬واو را از عالم‬
     ‫اعلی تصرترسد وخواب والهام اوسکمالرسد‪ « * .‬هانری کرین‪ .‬روابطحکمت اشراق وفلفةٌ ابران‬
     ‫باستان ‪ .‬از انتشارات انجمن ابرانشناسی شمار‪#‬ص‪ ° » :۸‬حکمت اشراق ‪ .‬بقلم نگارنده ‪ .‬تهران‬
                                                                 ‫ره ‪:‬فر ‪.‬کیان خره " ورج ‪.‬‬
                                                                                        ‫‪ . ۹‬ص‌‪»۵۲-۰۳‬و ک‬
     ‫هبارن فاطع‪)۴۰۱‬‬
                  ‫(‬
```


## [2026-09-06T21:35:19.369Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 246 247 248; do echo \"##### leaf $((n-1)) printed $((n-1+540))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n \"خورشید\\|خرشید\\|hvar\\|xšaēta\\|xsaeta\\|Xvar\" | head -10; done"
}
```


### [2026-09-06T21:35:21.046Z] TOOL RESULT

```
##### leaf 245 printed 785
54:   ‫بمناسبت نام فرشتةُ مزبور روز بازدهم هرماه ‪(.‬خورشید) با (خور) با ( خیر ) روز نامیده میشود‪.‬‬
##### leaf 246 printed 786
35:                 ‫‪ - 1‬بدان مناسبت کهکوبند عیسی درآسمان چهارم فرین خورشید است ‪:‬‬
36:              ‫سابة خورشید سواران طلب ‪.‬‬              ‫رنج خود و راحت باران طلب‬
51:          ‫‏‪ «hvara xshaeta‬یولهپ ‪ ۷2751264‬ةغل( باتفآینعمب )ناشخرد هکر ‪ :‬روخ و‬
##### leaf 247 printed 787
```


## [2026-09-06T21:35:26.472Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==246' BQT_v2_pages.txt | sed -n '40,70p'"
}
```


### [2026-09-06T21:35:28.380Z] TOOL RESULT

```
          ‫رك ‪ :‬خور » خورای ‪.‬‬        ‫‪۱‬‬          ‫‪ ۶‬خورنگه » و خورنق» («‪.‬م‪).‬‬         ‫مخفف‬
                                                                                     ‫‪_ ۵‬‬



                           ‫خوارخوارآب همی پالاید ‏ آن خورآ بهباشد ‪ ,‬عنصری (بلخی) گفت ‪:‬‬
        ‫که (چو) بسیار گردد بيك باراوی‪».‬‬              ‫ز جوی خورابه تکومتر بگوی‬
   ‫‪.‬‬   ‫دفت فرس ‪ ۱۳‬ورك ‪۲۰۵:‬‬
                         ‫ل‬
                             ‫رکه‪ :‬خوره خورا‪۰ ‎‬‬      ‫‪٩‬‬           ‫رك ‪ :‬خروه » خود خروه ‪.‬‬           ‫‪۸‬‬


                                                                          ‫حزهٌ ‪۹۸۷‬‬    ‫فا‬‫صبه‬
                                                                                          ‫بق‬
   ‫بمناسبت نام فرشتةُ مزبور روز بازدهم هرماه ‪(.‬خورشید) با (خور) با ( خیر ) روز نامیده میشود‪.‬‬
                                                                          ‫سرونی‌درفهرست‬
  ‫روزهای ایرانی ایشروز را (خور) ودرسفدی(خویر) و درخوارزمی (اخیر)یاد کرده‪.‬‬
        ‫زرشتیان ابران ابن روز را (خیر) نامند‪ .‬در بیت ذبل بمعنی آفتاب وفرشته هردو آمده ‪:‬‬
       ‫بسان‌خور که‌نگهبان فرص‌خور باشد‪.‬‬           ‫تو یاسبان سلیل پربوشت میباش‬
    ‫خروانی «روز شماری ‪.۰,۹۷-۳۳‬‬
```


## [2026-09-06T21:35:31.145Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==246' BQT_v2_pages.txt | sed -n '45,60p' | cat -A | head -0; awk 'BEGIN{RS=\"\\f\"} NR==246' BQT_v2_pages.txt | sed -n '48,58p'"
}
```


### [2026-09-06T21:35:33.427Z] TOOL RESULT

```
                         ‫ل‬
                             ‫رکه‪ :‬خوره خورا‪۰ ‎‬‬      ‫‪٩‬‬           ‫رك ‪ :‬خروه » خود خروه ‪.‬‬           ‫‪۸‬‬


                                                                          ‫حزهٌ ‪۹۸۷‬‬    ‫فا‬‫صبه‬
                                                                                          ‫بق‬
   ‫بمناسبت نام فرشتةُ مزبور روز بازدهم هرماه ‪(.‬خورشید) با (خور) با ( خیر ) روز نامیده میشود‪.‬‬
                                                                          ‫سرونی‌درفهرست‬
  ‫روزهای ایرانی ایشروز را (خور) ودرسفدی(خویر) و درخوارزمی (اخیر)یاد کرده‪.‬‬
        ‫زرشتیان ابران ابن روز را (خیر) نامند‪ .‬در بیت ذبل بمعنی آفتاب وفرشته هردو آمده ‪:‬‬
       ‫بسان‌خور که‌نگهبان فرص‌خور باشد‪.‬‬           ‫تو یاسبان سلیل پربوشت میباش‬
```


## [2026-09-06T21:35:36.541Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==246' BQT_v2_pages.txt | grep -n -B3 -A3 \"hvara\""
}
```


### [2026-09-06T21:35:38.465Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:35:40.637Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hvara xshaeta\\|hvara\" BQT_v2_pages.txt | head; "
}
```


### [2026-09-06T21:35:40.695Z] TOOL RESULT

```
14588:          ‫‏‪ «hvara xshaeta‬یولهپ ‪ ۷2751264‬ةغل( باتفآینعمب )ناشخرد هکر ‪ :‬روخ و‬
```


## [2026-09-06T21:35:43.309Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; n=$(head -n 14588 BQT_v2_pages.txt | grep -c $'\\f'); echo \"leaf $n printed $((n+540))\"; sed -n '14575,14600p' BQT_v2_pages.txt"
}
```


### [2026-09-06T21:35:45.375Z] TOOL RESULT

```
leaf 246 printed 786

       ‫‪ #‬خورد ی ‪ -‬بروزن بردن» اوسنا ‪( 1872۷ .18۷۳3-‬اکل ) » بپلوی ‪02172۷‬‬
       ‫ارمنی ع ‪kitrox‬‏ (‪۱‬کل‌طعام)‪ .‬کردی‪ (0۳1۲۷۲, 0۳1۳1۱۳‬کل)‪.‬افتانی ‪. 12۲05‬استی ‪۲1۷8۷5‬‬
   ‫‪.‬سرربکلی ‪ 0718-۲05‬سگلیسی ‪« 777 012‬اسشق ‪۷۰6»9‬اسفا‪:۱‬‬                      ‫‪2‬ی‪11‬‬
                                                                              ‫‪-‬منج‬
                                                                                 ‫‪۲‬ی و‬
                                                                                    ‫‪ 0‬مشغن‬
   ‫رگ‪-‬ے‪۰۷۳۱‬‏ «بونکر ه‪٩ ۷‬‏ < که ‪.‬‬
                               ‫‪۸۳‬‬‫‪٣‬ص‏ ‪ ۰۵۰۳ ۰۰۹۲ ۱۵‬روکه‪ :‬فهرست» «مسینا ‪ ۹۳۱‬ن‪٩‬یب‬
       ‫است ‪ ۰۱‬؛زاگلو فرودادن وبلعیدن نذا »ک‪۱‬ل‪ :‬فروباه پیشتر رفت وماهی خوردن گرفت ‪« »۰‬سند‬
                                            ‫بادنامه‪ .‬ظهیری‪ - »۸4‬آشامیدن ‪ -‬تلف کردن» برباد دادن‪.‬‬
  ‫‪ #‬حورشید ‏ بضم اول وواو ممدوله از خ‪:‬ور (آقتاب )(هم‪ + ).‬شید ( هم‪ ) ۰‬اوستا‬
  ‫هکر ‪ :‬زور‬
          ‫‏‪ «hvara xshaeta‬یولهپ ‪ ۷2751264‬ةغل( باتفآینعمب )ناشخرد هکر ‪ :‬روخ و‬
                                                                                  ‫شماری ص ‪: ۹۲-۳۳‬‬
                     ‫بوتس اندر دهان ماهی شد‬                 ‫قخروصرشید درسیاعی شد‬
       ‫«کلتان‪.»۲۲‬‬
 ‫خوره‬                                                                                                ‫اس‬


‫مودلد به دیر‪ ۴‬موسوم ساختند چه‌بزبان پهلوی‬            ‫حور ههر ‪ -‬من اول و سکون ثالی‬
                     ‫‪:‬‬   ‫را دیر گوند‬   ‫)‪۱‬‬   ‫گنف‬     ‫نام‬   ‫‪0‬‬   ‫بی لقطهٌ زده‬       ‫مھا ورای‬   ‫میم مکور‬      ‫‪£‬‬   ‫وئالت‬


‫خور نگاه ‪ .‬با انی معدوله یر وزن‬                                           ‫شمشیرسلیمانعلیهالسلام است ‪.‬‬
‫بهرام‬   ‫که عمارت‬   ‫انت‬   ‫یمعئی خورلق‬   ‫قدمگاه ‪۰‬‬
```


## [2026-09-06T21:35:55.517Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; grep -n \"xshaeta\\|xsaeta\\|shaeta\\|khshaeta\" BQT_v3_pages.txt BQT_v3_pages_faseng.txt | head -20"
}
```


### [2026-09-06T21:35:55.566Z] TOOL RESULT

```
ugrep: warning: BQT_v3_pages_faseng.txt: No such file or directory
```


## [2026-09-06T21:35:57.769Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; ls; grep -n \"\\[pdf page 11[0-9]\\]\" BQT_v3_pages.txt | head"
}
```


### [2026-09-06T21:35:57.822Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
8399:[pdf page 110]
8497:[pdf page 111]
8575:[pdf page 112]
8686:[pdf page 113]
8745:[pdf page 114]
8762:[pdf page 115]
8767:[pdf page 116]
8865:[pdf page 117]
8967:[pdf page 118]
9053:[pdf page 119]
```


## [2026-09-06T21:36:00.711Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 -c \"\nimport json;m=json.load(open('BQT_v3_pagemap.json'))\nprint(type(m), list(m)[:5] if isinstance(m,dict) else m[:5])\n\" ; echo ---; sed -n '8745,8790p' BQT_v3_pages.txt"
}
```


### [2026-09-06T21:36:02.551Z] TOOL RESULT

```
<class 'dict'> ['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
---
[pdf page 114]
‎AD cen oh‏ چم

‎3 6 SO ۳ ٩ ۵ ۰
4
a
3

‎ats
‎۳

‎۷
‎9

‎۱3 ‏اقلا‎ bib per

‎Pd
[pdf page 115]
۱۳۷۳ fake

۱ خر ‎be;‏
‏ز کتاب سفرنامه فردریچاردز - ترجمه مهین دخت صبا دروازه قر آن ‏ شیر از
[pdf page 116]
lee

ازآن قطره قطره‌شیر بچکد - ربا الی‌مجهول
کنابه از مردم دلیر وشجاع ‎ples‏ باشد.

شیراوژن ۱ - با واو و زای ‎rot‏
‏بر وزن و مملی شیر افنکن است که کنابه از
مردم شجاع و مردانه باشد - و نام شخصی هم
بوده است .

شیر با ۲ » با ‎tt‏ ممروف و بای ابجد
بالف کشیده؛ شیربرنج را گوبند وآن شلدماندی
است که از برنج و شیر کوسفند با ‎WF‏ پزند ؛
‎yin‏ کوبند شیربا شیریست که آلرا ‎AL‏ زشد
تا چون جفرات بته کردد و بعدازآن میوء های
خشك درآن ریز ند ‎amy‏ اززمالی خور ندودوراغ
رانیز کوبند. وآن‌ماستی باشد که‌در آن‌شیر کوسفند
و کاو ریزند و ‎LT‏ بعربی شیراز خوانند ۴ -

شیر بخشیر © بنتح بای ایجد وسکون
خای نقطه‌دار (۱) و شین فرشت بتحتالی کشیده
و ‎hy oly‏ زده » نام ‎gh‏ است درابی
و آلرا از هندوستان آورند . طبیعت آن کرم
```


## [2026-09-06T21:36:08.051Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 900 python3 tools/ref_page.py BQT:1320 --image 2>&1 | tail -50"
}
```


### [2026-09-06T21:36:16.548Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 115; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1320.png
REF: BQT:1320  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 115  OCR-lang: fas

براین صلطط -۱۳۲۳- 1 شرا
۳ 7 ظ ۳ :7 امه ۱ وی 1
اس اس و ات
لد فک 38
رب سه چ یی ۷
نس وه مکی
ی ار - ,: +2 مرو ود ۲
۱ 3 هچ ه
28 ۲ 1 ۹ س اِ
» 2 ی 9 .۰ ...۱
اه ج ۳ له سح ی ۲ : وت د ۵
1 ید ۳
7 مت دص
2 1 ۸ 4 ۳۱ 7 1 :
رت پات 9 ۲ ۲
۹ ده خح. ما ۹
ری ۴ و
۹ [ ون سم 3
: سمخ ۳4 ۰
: 7۳ ۲ ۰
۳ از ۱ ز 3
: 73 ۳ و رک 7 ۰
وهکا مه ۳
: رت 1 1 درم ۰ 0 9
سا "مخ ۰
۰ 17 ‌
```


## [2026-09-06T21:36:20.857Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 900 python3 tools/ref_page.py BQT:1320 --pdf-page 112 --image 2>&1 | head -30"
}
```


### [2026-09-06T21:36:22.767Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1320.png
REF: BQT:1320  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 115  OCR-lang: fas

براین صلطط -۱۳۲۳- 1 شرا
۳ 7 ظ ۳ :7 امه ۱ وی 1
اس اس و ات
لد فک 38
رب سه چ یی ۷
نس وه مکی
ی ار - ,: +2 مرو ود ۲
۱ 3 هچ ه
28 ۲ 1 ۹ س اِ
» 2 ی 9 .۰ ...۱
اه ج ۳ له سح ی ۲ : وت د ۵
1 ید ۳
7 مت دص
2 1 ۸ 4 ۳۱ 7 1 :
رت پات 9 ۲ ۲
۹ ده خح. ما ۹
ری ۴ و
۹ [ ون سم 3
: سمخ ۳4 ۰
: 7۳ ۲ ۰
۳ از ۱ ز 3
: 73 ۳ و رک 7 ۰
وهکا مه ۳
: رت 1 1 درم ۰ 0 9
سا "مخ ۰
۰ 17 ‌
```


## [2026-09-06T21:36:27.350Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 112 -l 112 -r 250 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $S/bqt_v3_112 && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/bqt_v3_112.png'); print(im.size)\""
}
```


### [2026-09-06T21:36:29.773Z] TOOL RESULT

```
(1375, 2122)
```


## [2026-09-06T21:36:31.929Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_v3_112.png"
}
```


### [2026-09-06T21:36:32.320Z] TOOL RESULT

```

```


## [2026-09-06T21:36:32.317Z] INPUT

[Image: original 1375x2122, displayed at 1296x2000. Multiply coordinates by 1.06 to map to original image.]


## [2026-09-06T21:36:38.609Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 111 -l 111 -r 250 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $S/bqt_v3_111"
}
```


### [2026-09-06T21:36:41.146Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:36:43.457Z] TOOL CALL #71: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_v3_111.png"
}
```


### [2026-09-06T21:36:43.918Z] TOOL RESULT

```

```


## [2026-09-06T21:36:43.915Z] INPUT

[Image: original 1375x2122, displayed at 1296x2000. Multiply coordinates by 1.06 to map to original image.]


## [2026-09-06T21:37:04.308Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FRS خشیسار\"; grep -n \"خشیسار\\|خشین\\|خشی\\b\\|خشنسار\" FRS.txt FRS_pages.txt | head -10; echo \"=== MON\"; grep -n \"خشین\\|خشیسار\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T21:37:04.387Z] TOOL RESULT

```
=== FRS خشیسار
FRS.txt:436:الفراغ عن‌تسو بدهذهالنسخة الَطیفة المرغوبة سدعبداسعیفمحتدالبدخشی 
FRS.txt:1353:گزبده‌چهار توست‌بدو در جها نهان همارا بآخشیج همارا بکار زار 
FRS.txt:4324:تا نبود چون همای فر خ‌کرکس همچو نباشد بشبه۳ باز خشین بند 
FRS.txt:5475:از آن کردار گز مردم رباید عقاب تیز برباید خشنسار 
FRS.txt:5492:س : خشنسار صرغی است بوک آیی تبره گون سرسپید وخشن بمعنی سپید بود ۰ 67 
FRS.txt:7207:‌غکی بود کوچك و لوش خشیه1 بود و ثيك نتواند بریده ۰ و در 
FRS.txt:7225:بود * سس + تزمرغی بود کوچك ۰ بلون خشینه و برجهد وآن مرغ تيك نتوان بربدن 
FRS.txt:8601:فرو خیز بدن بود » گویند بشخشید یعنی بخیز ید [ ابوشکو رگوید : 
FRS.txt:8618:شود کویند برشخشید ۰ : شخش کسی باشد که از نشستگاه خوبش فروخبزد گویند 
FRS.txt:8620:خوش شخشید . ۳ - انیت فقط در ث و چ هست 6 - این ببت فقط درس آمده 
=== MON
incoming/MON/MON_2vol_Adena_v1_djvu.txt:20332:باز خشین: (جاد.) نوعی از باز که پشت آن 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:25245:بمز ۱200 0 0 اوای درشت و خشین 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:56669:خشین فرهنگ فارسی معیر ۹ 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:56672:حشین: []۵ [- خشی - خشینه ] (ص.) 
MON_part1.txt:20332:باز خشین: (جاد.) نوعی از باز که پشت آن 
MON_part1.txt:25245:بمز ۱200 0 0 اوای درشت و خشین 
MON_part1.txt:56669:خشین فرهنگ فارسی معیر ۹ 
MON_part1.txt:56672:حشین: []۵ [- خشی - خشینه ] (ص.)
```


## [2026-09-06T21:37:07.538Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5470,5500p' FRS.txt; echo \"=== MON\"; sed -n '56660,56690p' MON_part1.txt"
}
```


### [2026-09-06T21:37:07.601Z] TOOL RESULT

```
ام ۱۵ 
یهار ۱ 
م‌غی است 4 آبی ؛ سرسیید » و خشن سید بود » دقیقی گفت : 


از آن کردار گز مردم رباید عقاب تیز برباید خشنسار 
-ا 9 
بهار 
بتخانه بود فرالاوی گفت : 
نه همچون ر خ خوبت کل بهار نه چون توبنیکوی ۲ بت بهار" 
| فرخی کوید : 
چه شهر شهرو بدو اندرون سرای سرای 
چه کاخ کاخ و بدو اندرون بهاربهار) 
۶ذحار 
سرخی باشد که زنان در روی هالند و آنرا کلگونه خوانند [ کسائی کوید : 
لاله بغنحار بز کقبه هد وروی این خوید بر کشید سرازخوید" ] 


چوبی ست که درختش بسی بلند نبود و از وی آلت پیشه وران سازند 


اق حا ار هرق انیت ری بو که رشن رات وتا تیه گون بسیامی زند ؛ 
س : خشنسار صرغی است بوک آیی تبره گون سرسپید وخشن بمعنی سپید بود ۰ 67 
ان‌اغت را ندارد . ۲ -س : بخویبی + 0 
4 - این پیت فقط در هست . چ لغت بهار را ندارد . : غنجار سرخی 
اد هویج ۰ س (مثل‌متن) ۰ چ این لفت‌را ندارد ۰ ٩‏ -ن بدون 
کر قائل این ست را شاهد آورده : 
ز خون رح بغتجار بندود خور ز کرد اند آورد چادر سر 

۷- س : شمشاد چویست درختش بلند باشد [ گذا] و از چوبش آاتها سازند پبشه 
وران که سخت باشد وزرد » چ اين لغت را ندارد ۰ ثن ( در حاشبه ) این لغت را 
=== MON
تندخویی» درشتجوبی. 
ِِ ۱ (مص‌ل.) تر سیدن» بیم 
۱ ترس» خوف. بیم. ضح.- (اخلاق 
اج #قوونین توقع و انتظار 
امر مکروهی در آینده که گاه بواسطة 
ارتکاب کثرت جنابت است و گاه بو اسطة 
معرفت جلال خدا است. 


خشین فرهنگ فارسی معیر ۹ 


حشین: []۵ [- خشی - خشینه ] (ص.) 
کسود رنگ» تبره رنگ. سیاه رنگ. (.) 
بازی که پشت آن کبود و تیره و چشم‌هایش 
سباه رنگ بود؛ بازی که نه سباه باشد نه 
سپید. 

خصاء: ته«(ع. ف. خصا] (مصم.) اخته 
کردن؛ خایه کشیدن. 

خصام: 7( [ع.] (مسصل.) دشمنی 
کردن. نزاغ کردن. (امص.) دشمنی. نزاع» 
جدال. 

خصایص: 22۷25( [ع. - خصائص ] (.) 
ج. خسصصه؛ خاصت‌ها» اختصاصات» 
شابستگی‌ها» سزاواری‌ها. 

خشصب: اد« [ع.] (.) بسیاری ثبات» 
فراوانی گیاه و سبزه» فراخی سال. خصب
```


## [2026-09-06T21:37:28.024Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^خورشید\\|خورشید:\" MON_part1.txt MON_part2.txt | head -5; echo \"=== shid\"; grep -n \"^شید:\\|شید: \" MON_part1.txt MON_part2.txt | head -5; echo \"=== derafsh\"; grep -n \"^درفش:\\|درفش: \\|درفشیدن\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-06T21:37:28.144Z] TOOL RESULT

```
MON_part2.txt:7579:خورشید) و فصل گرما را پیش می آورد؛ بر 
MON_part2.txt:7581:خورشید هم بیش از هر وقت مایلتر به سطح 
MON_part2.txt:7668:خورشید مرکز آن است و کر خاکی ما 
MON_part2.txt:22155:خورشید آویزند. 
MON_part2.txt:24386:خورشید قرار می‌گیرد) پدید می‌آید. این 
=== shid
MON_part2.txt:49395:اسروی معشوق. محراب جمشید: ( کد.) 
MON_part2.txt:54236:خورشید: (کد.) آسمان چهارم. (کذ.) دنیا. 
MON_part2.txt:58208:مشید: «۷:۲٩‏ (ع.] (اسف.) گچ یا امک 
MON_part2.txt:69492:مهشید: ۵۱-4 [- ماه‌شید] (امر.) بر تو 
MON_part2.txt:74123:می‌کنند. نبض خورشید: (کن.) خطوط 
=== derafsh
MON_part1.txt:38851:تخته خط کش درفش: تخته‌ای است به شکل 
MON_part1.txt:60512:درفش: 5 (- دروش ] (.( آلتی آهنین 
MON_part1.txt:60516:درفش: 85 (.) سبرق» علم؛ علامت»
```


## [2026-09-06T21:37:31.591Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '60508,60530p' MON_part1.txt; echo \"=== mahshid\"; sed -n '69488,69500p' MON_part2.txt"
}
```


### [2026-09-06T21:37:31.663Z] TOOL RESULT

```
درغم: 0121-7۳9 .( (مت.) نعمه و نوایی 
است از موسیقی که در حالت غم شنونده 
نوازند تا وی از غم بیرون آید. 
درغوش: (قد. کمکتاود [- درو ش ] 
درفش: 5 (- دروش ] (.( آلتی آهنین 
و نوک نب دارای دسته‌ای چوبین که 
دادن سوزن استعمال کنند. 

درفش: 85 (.) سبرق» علم؛ علامت» 
رابت (سیاه). فوطه‌ای که در روز جنگ ۳ 
بالای دستار جود سجن ؟ دو لغه. 

در فش: ٩2۲068‏ ,۵07۸13 [- درخش] (.) نورء 
فروغ» روشنایی. (ص.) درخشان» در خشنده. 
درفنحی: ادلصصعه [- فدرنچک - 
فرنجکک] (ا.) کرانبی که در خوات بر مردم 
افتد؛ کابوس» بختک. 

درف (6-) دود [ع.] .( سیری که از 
سیر ؟ ۳ درق. 

درک؛: (ع.] (مسصم.) درب فتن» 
اندر یافتن» بی بردن» در رسدن. (امص.) 
=== mahshid


زنان. 

مهشید: ۵۱-4 [- ماه‌شید] (امر.) بر تو 
قمر» ماهتاب. 

مهضوم. ه۵2 [ع.] (امف.) غدای تحلیل 
رفته» هضم سك ۵. 


مهفهفه: ۵۱۵/۱۵۲۵6۵ (ع. مسهفهفة ] 
(ص.) زن باریک میان؛ ج. مهفهفات.
```


## [2026-09-06T21:37:36.776Z] TOOL CALL #76: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T21:37:36.785Z] TOOL RESULT

```


```


## [2026-09-06T21:37:41.860Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF",
 "prompt": "Give the full Persian etymology section for خورشید: Middle Persian, Avestan forms, the analysis of the second element -šēd, and any Proto-Iranian/PIE reconstruction cited."
}
```


## [2026-09-06T21:37:43.735Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AE%D8%B4%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full etymology for Persian درخشیدن (draxšīdan): Middle Persian form, Proto-Iranian root, relation to درفش, and any PIE root cited."
}
```


### [2026-09-06T21:37:50.005Z] TOOL RESULT

```
# Persian Etymology of خورشید

**Inherited Source:** The word derives from Middle Persian 𐭧𐭥𐭫𐭱𐭩𐭲 (ḥwlšyt /xwar(x)šēd/).

**Avestan Comparison:** The entry cites Avestan 𐬵𐬎𐬎𐬀𐬭𐬆-𐬑𐬱𐬀𐬉𐬙𐬀 (huuarə-xšaēta-), meaning "bright sun (an epithet)."

**Morphological Analysis:** Through surface analysis, the word breaks into خور (xwar/xor, "sun") + شید (šēd/šid, "shine").

**Proto-Iranian Reconstruction:** The entry presents the form *huHarxšaytah, tracing back through Proto-Iranian stages.

**PIE Root:** The ultimate origin traces to Proto-Indo-European *sóh₂wl̥ (the sun), flowing through Proto-Indo-Iranian *súHar and Proto-Iranian *húHar.

**Related Cognates:** The first element connects to خراسان (Khurasan, a Persian province name, etymologically referencing the east where the sun rises), while the second element parallels Old Armenian աշխէտ (ašxēt).
```


### [2026-09-06T21:37:50.467Z] TOOL RESULT

```
# Etymology of Persian درخشیدن (deraxšidan)

Based on the Wiktionary entry, here's the full etymology:

**Merger of two verbs:** The word combines two near-synonymous terms:

1. **درفشیدن (derafšidan)** - "to glitter; to tremble; to flutter," derived from Middle Persian drafš meaning "banner; flag"

2. **رخشیدن (raxšidan)** - "to shine," sourced from Sogdian roxšan meaning "bright"

**Related languages:** The entry notes the word is "akin to Central Kurdish درەوشان (drewşan, 'to glitter')."

**Proto-Iranian connection:** While the Wiktionary article doesn't explicitly cite a PIE root, it traces the components back through Middle Persian and Sogdian, indicating an Indo-European language family lineage. The Middle Persian element drafš (flag/banner) and Sogdian roxšan (bright) represent the etymological bedrock provided in this source.

The entry emphasizes this represents a linguistic merger of two related verbs with overlapping meanings, rather than a single straight-line descent.
```


## [2026-09-06T21:37:59.527Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B4%D9%86",
 "prompt": "Give the Persian etymology of روشن (rowšan): Middle Persian form, Avestan raoxšna-, Proto-Iranian and PIE root cited."
}
```


## [2026-09-06T21:38:01.387Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%85%D8%B4%DB%8C%D8%AF",
 "prompt": "Give the etymology of Persian جمشید (Jamšid): Avestan Yima xšaēta, Middle Persian form, meaning of each element."
}
```


### [2026-09-06T21:38:04.627Z] TOOL RESULT

```
# Persian Etymology of روشن (rowšan)

According to the Wiktionary entry, روشن derives from **Middle Persian** _lwšn'_ (rōšn, "light; bright, light"), which came from **Old Persian** _*rauxšnā_.

The ultimate origin traces back through **Proto-Iranian** _*ráwxšnaH_ and **Proto-Indo-Iranian** _*ráwkšnaH_ to **Proto-Indo-European** _*lówksneh₂_, meaning "moon."

The entry notes this word is a doublet of رخشان (raxšân, "bright") and لوخن (loxan, "moon, moonlight"), with cognates appearing in Latin _lūna_, Armenian _lusin_, and Old Church Slavonic _luna_.
```


### [2026-09-06T21:38:06.929Z] TOOL RESULT

```
# Etymology of Persian جمشید (Jamšid)

The word traces back through multiple language stages:

**Avestan origin:** The Avestan form is "𐬫𐬌𐬨𐬀⸱𐬑𐬱𐬀𐬉𐬙𐬀" (yima.xšaēta), which combines two elements:
- *yima* means "Yama; twin, pair"
- *xšaēta* means "bright, shining"

**Middle Persian:** The form became "ymšyt'" (jamšēd), inherited from the Avestan compound.

**Proto-Iranian roots:** The etymology ultimately derives from "yamHáh" (Yama; twin, pair) plus "xšaytah" (bright, shining).

**Proto-Indo-European:** The deepest root is "yemHós," traced to Proto-Indo-European origins.

The name thus literally combines concepts of "twin" or "pair" with "brightness" or "shining," reflecting the mythological significance of Jamshid in Iranian tradition.
```


## [2026-09-06T21:38:10.811Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/x%C5%A1aytah",
 "prompt": "Give the full etymology and descendants of Proto-Iranian *xšaytah — what root or PIE etymon is it derived from, and what Avestan/Middle Persian/New Persian descendants are listed?"
}
```


## [2026-09-06T21:38:12.099Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/amphictyony",
 "prompt": "Give the full etymology of English amphictyony, including the Greek forms and the connection to ktizein / PIE root."
}
```


### [2026-09-06T21:38:17.132Z] TOOL RESULT

```
# Proto-Iranian *xšaytah Etymology and Descendants

## Etymology
The entry states the origin is **"Unknown."** No Proto-Indo-European root or earlier etymon is provided.

## Descendants

**Avestan:**
- xšaēta (masculine form)
- xšōiθnī (feminine, meaning "glowing, radiant")

**Middle Persian:**
- šyt' /šēd/ ("bright; sorrel horse")

**New Persian:**
- شید (šīd, "splendid, brilliant")

**Other branches:**
- Ossetian (both Digor and Iron dialects)
- Kurdish dialects (Northern and Central)
- Old Armenian: աշխէտ (ašxēt, "reddish [of horses]")
- Old Georgian: ხსედი (xsedi)

The word fundamentally means "bright" or "shining," with secondary applications to horse coloring in several descendant languages.
```


### [2026-09-06T21:38:18.223Z] TOOL RESULT

```
# Etymology of Amphictyony

Based on the Wiktionary entry provided, the English term **amphictyony** derives from Ancient Greek through the following pathway:

The word comes from Ancient Greek *ἀμφικτυονία* (amphiktuonía), which is a compound of two elements:

1. **ἀμφί** (amphí) — meaning "around" or "near"
2. **κτίζω** (ktízō) — meaning "I found" or "people"

The entry states: "From Ancient Greek _ἀμφικτυονία_ (amphiktuonía), from _ἀμφί_ (amphí, 'around, near') + _κτίζω_ (ktízō, 'I found, people')."

Unfortunately, the provided source does not include information about the Proto-Indo-European root underlying *ktízō*. To obtain that etymological connection, one would need to consult additional references beyond this Wiktionary entry.
```


## [2026-09-06T21:38:28.235Z] TOOL CALL #83: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CF%84%CE%AF%CE%B6%CF%89",
 "prompt": "Give the full etymology of Ancient Greek κτίζω: the PIE root reconstructed, cognates in Sanskrit/Avestan, and any note from Beekes."
}
```


## [2026-09-06T21:38:29.664Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/t%E1%B8%B1ey-",
 "prompt": "Give the meaning, descendants (Greek, Indo-Iranian, Germanic) and any notes for PIE *tḱey-."
}
```


### [2026-09-06T21:38:34.087Z] TOOL RESULT

```
# Etymology of Ancient Greek κτίζω

**PIE Root:** The word derives from Proto-Indo-European *tḱey- meaning "to settle."

**Cognates:**
- Sanskrit: क्षेति (kṣéti)
- Avestan: 𐬱𐬀𐬉𐬌𐬙𐬌 (šaēiti)
- Old Armenian: շէն (šēn) – acquired through Iranian borrowing

**Beekes' Note:** According to the Etymological Dictionary of Greek, this root is documented in "Beekes, Robert S. P. (2010), 'κτίζω', in Etymological Dictionary of Greek" as part of the Leiden Indo-European Etymological Dictionary Series, pages 791-792.
```


### [2026-09-06T21:38:36.784Z] TOOL RESULT

```
# PIE *tḱey-

**Meaning:**
The root denotes three related concepts: "to cultivate," "to settle," and "to live." It functions as an imperfective verb root.

**Descendants:**

*Greek:* Ancient Greek κτίζω (ktízō, "to found/build") and related terms like κτίσις (ktísis, "foundation")

*Indo-Iranian:* Sanskrit क्षेम (kṣema, "welfare/safety") and क्षिति (kṣití, "earth/dwelling"); Avestan forms like šaiiana

*Germanic:* Proto-Germanic *haimaz, ancestor of English "home" and related words

**Notes:**
The root was "reanalysed" from an earlier form *tḱéyti, itself derived from *teḱ- ("to sire, beget") plus the *-éyti present suffix. Multiple grammatical formations exist, including s-aorists, denominative presents, and agent noun formations. The root appears across numerous Indo-European language families with consistent semantic development from "settle/inhabit" concepts.
```


## [2026-09-06T21:38:45.079Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"a-xsaena\\|axsaena-\\|a-x§aena\\|xsaena\" BRT.txt | head -10"
}
```


### [2026-09-06T21:38:45.129Z] TOOL RESULT

```
3658:•  j.  ap«m9n),  g.  ap3ni9m  Adv.:  s.  apma-, ■  j.  a-p9r9tö.tanü-  Adj.  'auf  des  Leib kein  Makel  haftet,  makellosen  Leibes"*: Aagat^rnt  gavam  axsaenanqm  'nunqnt  V. 22.4.
```


## [2026-09-06T21:38:48.374Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"dunkelfarbig\\|xsaSna\\|x§a?na\\|a-xsaSna\" BRT.txt | head -10; echo \"=== search near col 51\"; grep -n \"axsae\" BRT.txt | head"
}
```


### [2026-09-06T21:38:48.439Z] TOOL RESULT

```
3135:•  j.  a-x£acna-  Adj.  'dunkelfarbig':  ansö °nS  Aog.  73;  —  gavqm  °nanqm  V.  22. 4,
13489:•  j.  dasgra-  Adj.,  Beiwort  von  Pferd und  Rind,  wohl  Farbenbezeichnung,  etwa 'dunkelfarbig* ".
13492:Ableit.  aus  "däsgraifa-  m.  EN.,  Komp.;  "ra- .ifospa;  eig.  'der  dunkelfarbige  Rosse  hat'.  — ■)  Oder  ist  •fcii  GS.  (nach  der  /-Dekl.)  aus dätgräsfiJ-  m.  EN.  (eig.  'der  dunkelfarbige Stuten  hat'}?
13494:Eig.  'der  dunkelfarbige  Rinder  beshzt'.
=== search near col 51
3658:•  j.  ap«m9n),  g.  ap3ni9m  Adv.:  s.  apma-, ■  j.  a-p9r9tö.tanü-  Adj.  'auf  des  Leib kein  Makel  haftet,  makellosen  Leibes"*: Aagat^rnt  gavam  axsaenanqm  'nunqnt  V. 22.4.
```


## [2026-09-06T21:38:51.239Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=3130 && NR<=3142' BRT.txt | cut -c1-700"
}
```


### [2026-09-06T21:38:53.413Z] TOOL RESULT

```
El.?>).  —  arm.  LW.  or/.  —  Fö.;  FaJiiii  erL: viii/aiii,  (in  N.  75):  dar/;  Npü.:  ÜmärT.  — 1).  Hds.  •/jm.  —  '}  BN.  Slud.  I.  366.
j.  axUm  N.  75:  lies  axitm,
j.  axtö  N.  20\  lies  haxlö,
•  j.  axtya-  m.  EN.  eines  Ungläubigen, der  dem  YSista  (sd.)  99  Fragen  stellt: "/fffi  duzdim  l^maiskuniim  YL5,82;  — fralna  (sd.)  .  .  navaca  navaillmca  . .  yat .  .  ptr^sal  'h'ö  duida  t>mat3ukh  Yt5.82.
Et.  und  Bed.  ?
•  j.  a-x£acna-  Adj.  'dunkelfarbig':  ansö °nS  Aog.  73;  —  gavqm  °nanqm  V.  22. 4,
Eig.  'nichllicht',  vgl.  xsa'la-;  Bthl,  IV.  S- 360. —  mp.  (Pü.)  axicn,  ap-jaliii;  DST.  fttlr.
2.  53,  Hbu.  ZDMG.  JiJ.  427-
•  p,  a-xäata-  Adj.  (fem.  °/3-)  'unverletzt, ungestört':  Ayi^  duvaislam  ÜyätW  'tl hauvciy  . .  nirasitliy  (sd.)  , .  "Wohlbehagen, auf  sehr  lange  Zeit  hinaus  ungestört,  es wird  sich  . .  einstellen  . ."  D,  5. 3.
PPfP.  lam  ai.  V.  ifuaMi  'et  verlelzt',  gr,  «ri/ju; ; Bgu.  GrGt.3  123.  —  ai.  äifola-  Adj.
•  j.  a-xsapan-  f.  'Abenddunkel,  "xsafni x/afnJm  is>mn~'  "im  Abenddunkel  sich das  Abendmahl  suchend"  Yt  14.  zo.
Kig.  'was  bis  zur  Nacht  hin  reicht,  an  die Nacht  grenzt'.  —  Npü.:  dar  Aar  Sai.
g.  axSajfanr,  j.   axsaj-amir :   lies  nj-iV".  !
```


## [2026-09-06T21:39:03.001Z] TOOL CALL #88: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4",
 "prompt": "Give all Persian etymology sections for درفش (both 'banner' and 'awl' and 'brightness' if present): Middle Persian forms, Avestan drafša-, Sanskrit cognates, and any root cited."
}
```


## [2026-09-06T21:39:04.149Z] TOOL CALL #89: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D8%AF",
 "prompt": "Give the Persian etymology of شید (šīd) 'light, brightness': Middle Persian, Avestan and Proto-Iranian forms cited."
}
```


### [2026-09-06T21:39:10.193Z] TOOL RESULT

```
# Persian Etymology of شید

Based on the Wiktionary entry, here is the etymological chain:

**Proto-Iranian origin:** The word traces back to Proto-Iranian *[\*xšaytah](/wiki/Reconstruction:Proto-Iranian/x%C5%A1aytah "Reconstruction:Proto-Iranian/xšaytah") meaning "bright, shining."

**Middle Persian form:** It was inherited from Middle Persian (šyt' /⁠šēd⁠/), which carried the meanings "bright; sorrel (horse)."

**Modern Persian:** The contemporary form شید maintains the sense of luminosity, defined as "splendid, brilliant, bright, luminous" when used as an adjective, or "shine, radiance" when functioning as a noun.

The etymological trajectory demonstrates consistent semantic preservation across these language stages, with the root consistently encoding concepts related to brightness and radiance from its Proto-Iranian foundation through to modern Persian usage.
```


### [2026-09-06T21:39:10.272Z] TOOL RESULT

```
# Persian Etymology for درفش (Drafš)

**Middle Persian Origin:**
"Inherited from Middle Persian [Book Pahlavi needed] (dlpš /⁠drafš⁠/, 'banner')"

**Proto-Iranian Root:**
Possibly derived from Proto-Iranian *drafš- meaning "to behave like a banner, fly up, shine, tremble"

**Proto-Indo-European Root:**
Potentially traced to PIE *drep- ("to cut, tear off (a piece)")

**Avestan Cognate:**
The word appears as 𐬛𐬭𐬀𐬟𐬱𐬀- (drafša-) in Avestan texts

**Sanskrit Cognate:**
Related to द्रप्स (drapsá) in Sanskrit

**Note on Meanings:**
The etymology section documents the word's primary meanings as "standard, ensign, colours, banner" and secondarily as "awl." The brightness/shine sense noted in Urdu appears to derive from the Proto-Iranian root's connotations of shining and trembling, though this semantic development isn't explicitly detailed in the etymology section provided.
```


## [2026-09-06T21:39:23.599Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AE%D8%B4%DB%8C%D8%AF%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B4%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%AC%D9%85%D8%B4%DB%8C%D8%AF' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/x%C5%A1aytah' \\\n 'https://en.wiktionary.org/wiki/amphictyony' \\\n 'https://en.wiktionary.org/wiki/%CE%BA%CF%84%CE%AF%CE%B6%CF%89' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/t%E1%B8%B1ey-' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%81%D8%B4' \\\n 'https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D8%AF' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 279 (book p.249), roots Ksei 2 / Ksei 3 — verification of xsaeta/xorsid/Jamsid/rowsan/draxsidan/drafs and Greek ktizein > amphictyony' 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T21:39:28.682Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/759393d8a6ff9320.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6210ba498a88c950.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/376f55f4e7406605.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/afa136369c747ee1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8b30cef5e5f18af0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d195620e32741a45.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/31b2d662b1abd0d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/acc6fd901ca285c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f2027aaa926815f4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a116553c60373364.txt
```


## [2026-09-06T21:39:45.381Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK data/verification/sources/refs/ocr/BQT\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg279.png data/verification/sources/refs/ocr/BOOK/279.png\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_v3_111.png data/verification/sources/refs/ocr/BQT/1320.png\ncat > data/verification/sources/refs/ocr/BQT/1320.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, vol. 3, printed page ۱۳۲۰ = PDF page 111 of BQT_v3_picofile.pdf\n (the tool's default offset gives pdf 115 = printed ۱۳۲۳; correct offset here is printed = pdf + 1209).\n Read from the page image by eye — Persian OCR unusable.]\n\nHeadword (right column, bottom):\nشید ۳ - بکسر اول و سکون ثانی مجهول و دال ، بمعنی نور باشد مطلقاً که آن روشنایی ...\n\nMo'in's etymological footnote ۳ (bottom of the page):\n۳ - اوستا xshaeta (درخشان)، پهلوی shēt «استق ۸۰۱»، در ارمنی ashxēt (سرخ قهوه‌ای)\n[در اسب]، پهلوی shēt-vars (سرخ‌مو)، کردی shē (روباه)، shi (کرد [اسب])\n«هوبشمان ۸۰۱» همین کلمه است که در «خورشید» و «جمشید» آمده.\n\nOther headwords on the same page: شیبوی ، شیتره ، شیخ ، شیخ نجدی ، شیدا ، شیداب ،\nشید اسپهبد ، شیدان ، شیدآهرمن. Footnote ۴ (on شیدا) derives it from Aramaic/Akkadian\nshedu (نام عفریتی)، عبری shed، آرامی shēdâ (دیو) — citing H. Zimmern,\nAkkadische Fremdwörter, Leipzig 1917, s. 69 — i.e. a different word from شید «نور».\nEOF\nls -la data/verification/sources/refs/ocr/BOOK/279.png data/verification/sources/refs/ocr/BQT/1320.*"
}
```


### [2026-09-06T21:39:45.472Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  75777 Sep  6 17:39 data/verification/sources/refs/ocr/BOOK/279.png
-rw-rw-r-- 1 sfmqrb sfmqrb 100817 Sep  6 17:39 data/verification/sources/refs/ocr/BQT/1320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    615 Sep  6 17:36 data/verification/sources/refs/ocr/BQT/1320.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   1262 Sep  6 17:39 data/verification/sources/refs/ocr/BQT/1320.vision.txt
```


## [2026-09-06T21:39:48.212Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T21:39:48.245Z] TOOL RESULT

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


## [2026-09-06T21:40:47.718Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; python3 -c \"\nimport json,glob\nfor f in sorted(glob.glob('page-2*.json'))[-8:]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if not n.get('words'):\n                print(f, e['root'], n['id'], n['verdict'], '|', n['derivation'][:220]); print()\n\" 2>/dev/null | head -40"
}
```


### [2026-09-06T21:40:49.582Z] TOOL RESULT

```
page-270.json Kleu 1 10 unverified | An empty box on the printed page (checked on the 300-dpi render, copied to data/verification/sources/refs/ocr/BOOK/270.png): the rectangle drawn to the right of the Pahlavi du-srav box carries no language label, no word,

page-270.json Kleu 1 17 confirmed | An empty pass-through box; the French forms Nourai means are esclave 'slave' (Old French esclave, 12th-13th c., from Medieval Latin sclavus, with the prosthetic e- French regularly puts before Latin s + consonant, as in 

page-271.json Klěu 2, Klâu 3 plausible | The empty pass-through box stands for Jewish/Christian Aramaic אַקְלִידָא ʾaqlīdā, Syriac ܐܩܠܝܕܐ ʾaqlīdā 'key', the form through which the Greek word reached Arabic. It is not an inherited Indo-European descendant of the

page-272.json Klou-ni 5 unverified | Empty pass-through box: on the printed page an arrow leaves the 'Old Persian slaunis' box and ends in a wide, completely blank rectangle to its right (verified on the 200 dpi render of pdf page 272). There is no language

page-275.json Krei 2 unverified | Blank box in the printed chart (p.245), drawn to the right of the Avestan srî/srîra/sra-yah box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extraction and was added b

page-276.json Kreu, Qreu, Qreus, Qruwes, Qrus 3 plausible | An empty pass-through box: Nourai posits an Arabic intermediary between Latin/Greek Caucasus and Persian qafqāz but prints no Arabic form. The form he must intend is Arabic al-Qawqāz القوقاز (also قبق al-Qabq in the earl

page-276.json Kreu, Qreu, Qreus, Qruwes, Qrus 21 unverified | Blank box in the printed chart (p.246), drawn to the right of the Avestan xrŭ/xrŭra/xrŭždra box with an arrow from it; no language label or word. Nothing to verify. The box was missing from the extraction and was added b
```


## [2026-09-06T21:40:55.861Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; python3 -c \"\nimport json,glob\nc=0\nfor f in sorted(glob.glob('page-2*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if n['verdict']=='transcription_suspect':\n                print(f, n['id'], n.get('words'), '| error_in=',n.get('error_in'),'| book_prints=',n.get('book_prints'),'| correct=',n.get('correct_form'))\n                c+=1\nprint('total',c)\n\" 2>/dev/null | tail -25"
}
```


### [2026-09-06T21:40:57.989Z] TOOL RESULT

```
page-252.json 1 kalix | error_in= book | book_prints= kalix | correct= kúlix (Ancient Greek κύλιξ, gen. κύλικος)
page-252.json 4 gladiyator | error_in= book | book_prints= gladiyator | correct= gladiateur
page-252.json 6 clamitas | error_in= book | book_prints= clamitas | correct= calamitās
page-254.json 1 kan 2, kaine, kainîn, kaimyâ : young girl; kan-yâ, kain-ika : small woman | error_in= book | book_prints= kaimyâ | correct= kainyâ
page-255.json 6 censur | error_in= book | book_prints= censur : censor | correct= censure (F., 'censorship'); F. censeur = 'censor'
page-256.json 19 carrot, cheek, corner, horn | error_in= book | book_prints= carrot, cheek, corner, horn | correct= carrot, cheer, corner, horn
page-258.json 3 kirsman : black | error_in= book | book_prints= Old Persian [POK:583] kirsman : black | correct= Old Prussian kirsnan (acc. sg. of *kirsnas) 'black'
page-263.json 9 au-šaudîhtwei | error_in= book | book_prints= Old Persian ▭ POK:588 | au-šaudîhtwei : to trust | correct= Old Prussian auschaudītwei (au-schaudīt-wei) 'to trust'
page-263.json 11 akavein; kudos | error_in= book | book_prints= akavein : to hear | correct= akouein (ἀκούειν)
page-263.json 17 haujjan; skauuon | error_in= book | book_prints= haujjan : to hear | correct= hausjan / Proto-Germanic *hauzjan(ą) (Gothic hausjan)
page-264.json 1 nekŭkîdan «نکوهیدن» | error_in= book | book_prints= nekŭkîdan | correct= nekūhīdan (nikūhīdan) «نکوهیدن»
page-264.json 3 sčŭten | error_in= book | book_prints= sčŭten | correct= schuten / shouten (ME)
page-267.json 1 šiphâ, čiphâ | error_in= book | book_prints= šiphâ, čiphâ : twig, hair | correct= śiphā (older transcription çiphā) — one Sanskrit word, not two
page-267.json 3 xiphos | error_in= book | book_prints= xiphos : branch, rod | correct= kiphos (Messenian κίφος n.) 'στέφανος, wreath' — the Greek word Pokorny actually gives under this root
page-268.json 7 qîr; târ | error_in= book | book_prints= târ : tar | correct= qâr «قار»
page-268.json 13 kiton | error_in= book | book_prints= kiton : cotton shirt | correct= khitōn (χιτών), Ion. kithōn (κιθών) 'linen tunic'
page-269.json 9 clinic | error_in= book | book_prints= clinic | correct= clinique
page-269.json 12 clîmâre; cliěns | error_in= book | book_prints= clîmâre | correct= clīnāre
page-270.json 15 slabnovus | error_in= book | book_prints= slabnovus | correct= Σκλαβηνός (Sklabēnós), pl. Σκλαβηνοί; short form Σκλάβος (Sklábos)
page-270.json 16 slavous | error_in= book | book_prints= slavous | correct= Sclavus 'a Slav' / sclavus 'slave' (also Slavus)
page-271.json 1 kleiein : to close; kleidos, kleiss : key | error_in= book | book_prints= kleidos, kleiss | correct= kleidos, kleis (κλείς, gen. κλειδός)
page-272.json 4 slaunis | error_in= book | book_prints= Old Persian ▯ POK:608 | slaunis : buttock | correct= Old Prussian slaunis 'thigh' (cf. Lithuanian šlaunis)
page-276.json 6 cros; crystacus | error_in= book | book_prints= cros : frost / crystacus : ice | correct= Gk. κρύος krýos 'frost' ; κρύσταλλος krýstallos 'ice, crystal'
page-276.json 12 xrŭ, xrŭm; xrŭra; xrŭma, xrŭta, xrus; xrŭždra | error_in= book | book_prints= xrūždra : heart | correct= Av. xrūždra- 'hard' (Bartholomae/Pokorny German 'hart')
total 58
```


## [2026-09-06T21:41:05.070Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=2500 && NR<=2545' KLN_1966.txt | grep -n \"^[0-9]\\{1,4\\}$\\|page\\|^ *[0-9]\\{2,4\\} \" | head; echo \"---\"; sed -n '2525,2540p' KLN_1966.txt | cut -c1-120"
}
```


### [2026-09-06T21:41:06.776Z] TOOL RESULT

```
1:65
---
amour,  n.,  a  love  affair.  —  F.,  ‘love’,  fr.  L.  amorem, acc.  of  amor,  ‘love’,  fr.  amare,  ‘to 
ampangabeite,  n.,  a  complex  tantalo-mobate  (mm- eral.)  —  Named  after  Ampangabe  in  Madagas¬ car.  For  the 
ampelideous,  adj.,  pertaining  to  the  vine  family. — Compounded  of  Gk.  SpneXog,  ‘vine’,  and  elSos, ‘
Ampelopsis,  n.,  a  genus  of  plants  of  the  grape family  (bot.)  —  ModL.,  lit.  ‘looking  like  vine’, com
ampere,  n.,  unit  of  force  of  the  electric  current.  — F., named  after  the  French  physicist  Andre-Marie Am
ampersand,  n.,  the  symbol  &  (=  and).  Cor¬ ruption  of  the  partly  English,  partly  Latin phrase  ‘and  per 
amphi-,  before  a  vowel  amph-,  pref.  meaning ‘both,  on  both  sides,  of  both  kinds'.  —  Gk. dp.91.-,  dptp
Amphibia,  n.  pi.,  a  class  of  vertebrates.  —  ModL. See  next  word.
Derivatives:  amphibian,  adj.  and  n. amphibious,  adj.,  living  both  on  land  and  in  water. —  Gk.  dpuplfliog
Derivative:  amphibol-ic,  adj. amphibology,  n.,  an  ambiguous  statement.  —  F, amphibologie,  fr.  ML.  amphibolo
Amphicarpa,  n.,  a  genus  of  vines  (bot.)  —  ModL., fr.  Gk.  dp9txap7toi;,  ‘having  fruits  on  both
sides’,  which  is  compounded  of  dptpt-  (see  am¬ phi-)  and  xapirog,  ‘fruit’.  See  carpel.  For  E.  -ous
amphictyonic,  adj.,  pertaining  to  an  amphicty- ony.  —  L.  amphictyonicus,  fr.  Gk.  dpupixtuovi.- X04,  fr.  d
amphictyony,  n.,  confederation  of  states  in  an¬ cient  Greece,  established  around  a  common center.  —  Gk. 
Derivative:  amphigor-ic,  adj. amphimixis,  n.,  union  of  the  germ  cells  of  two individuals  ( biol .)  —  Comp
Amphion,  n.,  son  of  Zeus  and  Antiope,  king  of Thebes  and  husband  of  Niobe  (Greek  mythol.)
```


## [2026-09-06T21:41:16.131Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### FSD amphictyony\"; grep -n -o \"amphictyony[^|]\\{0,200\\}\" FSD_vol1.txt | head -3; echo \"### WEB\"; grep -n -o \"amphictyony[^|]\\{0,200\\}\" WEB_vol1.txt | head -3; echo \"### IEC ksei/kthei\"; grep -n \"ksei-\\|kthei\\|kṣeti\\|kseti\" IEC.txt | head -8"
}
```


### [2026-09-06T21:41:17.994Z] TOOL RESULT

```
### FSD amphictyony
15162:amphictyony  or  its  members or  delegates;  as,  an  amp  hid  yonic  city  or  council,  in- pMd'jor.ic  is  sometimes  applied  humorously  or  ironically  to any  body  of  persons  conferring  together,  e
### WEB
6862:amphictyony. amphictyonic council; in ancient Greece, an assembly composed of delegates from the states associated in an amphictyony. am-phic’ty-6-ny, n. in ancient Greece, a con- federation of states establishe
### IEC ksei/kthei
4384:grugió (grugidio, grugdio) ‘creak, crack, grind, crunch’. See next Gk. grüzo, v. *grumble'; adj. gruktós; MHG krochzen, v. ‘crack, bang; croak’; Norw. cf. krykje, s. ‘kittiwake’; Li. grugzdu, den. v. ‘crunch’; grukseti, id.
5940:$hauk- (ghiauk-) ‘gape; open jaws, gap, space’. Cf. &hiia- and cpds. Lat. faux, usu. pl. fauces, gp -ium *open jaws, estuary’ (f- for *8h-, as in fütilis, see &hü-); Li. cf. Ziáukseti, ZiáukCioti *heave, belch; bark'. Cf. the radical in Li. Ziauturai “open jaws
19516:equivalence of Li. tvinkseti: tunkseti ‘pulsate’; tvirsóti: tursóti "lounge"; tviróti ‘enclose’: tu- réti ‘have’. Thus also Lat. festinàre: torrens, festus, in-, mani-: re-, ob-türáre; E twitch: G zwicken, zwacken, zucken etc. sug- gest a parallel evolution of forms with and without *-u-. Cf. also Li. tvyl- :tyl- ‘quiet’
```


## [2026-09-06T21:41:18.925Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### NYB\"; grep -n \"šēt\\|set 'bright\\|drafš\\|axšēn\\|xvaršēt\\|xwaršēd\" NYB_vol2_glossary.txt | head -10; echo \"### HUB xorsid\"; grep -n \"^.\\{0,40\\}xursed\\|xursed\\|hvarexsaeta\\|xsaeta\" HUB.txt | head -10"
}
```


### [2026-09-06T21:41:21.038Z] TOOL RESULT

```
### NYB
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
781:āvaštan [HTYMWN-tn'] to seal, pt. = pret. pass. 3d p. sg. āvašt 19%; pt. āvašīt [HTYMWN-yt'] sealed up 11722; [pai- tāmbarān (*wbšt' =) ävast the seal of the prophets, of Muhammad, = Arab xdtamu l-nabīyīn, DkM 291%]. — Reading according to Henning, BSOAS XI, 1946, 725 sq. FrP ch. 23 gives for the ideogr. the gl. >wbstn' (var. *whstn'), to which Cod. U, adds the pres. forms 3d p. sg. "pbéyt! = āvašēt, Ist p. pl. "wb'šym = āvāšēm (or possibly "obhšym = āvaxšēm); it should, however, be observed that the Paz. readings are throughout anbaš-, anbiš-, thus ’nb$-, not °wbš-, so Bthl was fully exeused in his reading and etymo- logy (MirM II, 37-38), which Henning seems not quite to have understood (Bthl. translated it ‘festmachen’ but used this w. in & juridieal sense: 'to make & document valid before the law' through applying one's seal on it, which is in fact not far from the truth, v. Nyberg, By- zantion XXX VIII, 1968, 119-122).
1328:drafš [dlpš] banner 2722. 298-16, — Av, (771 sq.) drafša-; MPrth drjš (A-H III, cf MHC 119 n. 1 and Gloss. s. v.); Arm. lw. drauš; NP dirafs.
1865:hàn [ZK], with emphasizing particle hän-ic [ZK-c; on ZK-p, ZK-py 5113-15 v.s. v.-p], dem. pron., sg. and pl., refer- ring to what is distant from the speaker, or already mentioned; independent, or adj. placed before its headw. (exception: viyük han HajB: 9); the adj. han may be replaced by hàn t, properly ‘that which is’: hàn + "sih that *splendour 125-26; han i Vidrafš + yātūk 25%; han à yamak 571%; esp. if -c is added to it: hün-ic i dar-band 241; hān-ic i Hutēs
2026:hēšītan to dry, to wither (intr.): pres. 3d p. sg. hēšēt [hwšyt'] 9612-13, 9811, hošet [hwšty] 128%. — Av. (1738) hao$-; MPrth pres. hwš-, xwš- (MHC); Bal husay; NP xoSidan. V. also husk.
2080:Hušētar [hwšytl] the first of the three still unborn sons of Zartuxšt who will appear in the trimillenial apocalyptic period: 7114. 9619.17.39. — Paz. Hušečar; from Av. (384) Uxsyat.orata-.
2081:Hušētarmāh [hwšytlm”h] the second ap- ocalyptic son of Zartuxšt who will appear after Hušētar: 7114, 988-14.16, 999. 11017. — Paz. Huseöarmäh; from Av. (384) Uz- šyat.nomah-, cf the spelling ?wšytnms DkM 44! (-ms inverse spelling of -mah).
2095:*hu-vaxm [hww’hm] “of good swing", epithet of the varz ‘mace’ (v. vazr) carried by Keresāspa 100%. — Renders Av. (1832) hu-nwiata- "well swung’, epithet of the vazra- of Mithra (Yt. 65. 10132) and of the vazra- in general (Yt. 10%. 1372); < m + vaeg-, v.s. v. ?vextan. Reading hypothet- ical, no Paz. reading being known to me. I take it as *hu-vexm < "hu-vataman- from *véxtan < vaig- (q. v.), which has been largely confounded with !vextan < vaik-; *huvērm > hu-vaxm (or perhaps better *hu-vahm) cf s. v. mahmän. As to véxtan as a battle term cf 254. — As Bthl (Wb 1832) has given quite misleading information about the Phl. w. I put here the notice he quotes in its correct form. It is found in the Phl Xvaršēt ntyāyišn (= Yt 6) in Zand-i Khürtak Avistäk ed. by Dhabhar, p. 21 $ 15: ké yast Ohur- mazd % amarg api-š yast Mihr 4 fragoyot . . . (l. 14) api-§ yast vazr i *hu- vazm | pat kamär apar i dévan | i Mihr frägöyöt (e: *huvaxméh € ku bāstān eton dàret: mēnēyīhā be šavet, vināskārān pã- tifrās bē kunét, u menöyihä apäc 6 kantir äyet) ‘he who has worshipped Ohurmazd the Immortal... has (at the same time) worshipped Mihr (the god) of wide (l. 14) and he has wor- shipped: the mace of good swing on the skulls of the devs, owned by Mihr of wide pasturages (its being “‘of good swing" means that it constantly behaves in the following manner: spiritually it goes off and punishes the sinners, and spiritually it returns to the quiver [sheath?])? NP v. xub nihädah, Skr. v. su-niyukta (Dhalla, The Nyaishes, 1908, p. 50). l
2358:kuštan [kwštn', NKSWN-tn'], pres. pass. 3d p. sg. kwšhyt' = kusihet 981-3 used as an opt. (hence the neg. mā), but the form is obscure, one would expect the imp. kušēt: to kill, to slaughter 258. 275, 3214. 9413, 10715; perf. pass. kust hat 981. — = NP; Av. (432) fra-kaoš-, pres. -kuša-; MPrs kwst (pt.), kwš-, Verbum 168.
2417:mänenak [m’nynk'] *rainy, *rain-bear- ing: avr i ~ 891%. — In a collection of Av. glosses with Phl. translation, PT 72 (defectively rendered by Barthelemy, GA 55, and utilized in this form in AirWb as „FrBy”) we find: mano: mihr(a)g pädak — staro : star pādak — mänhö: mah padak — hwarö : xvaršēt pādak — anagrd raocá: hàn i asar [i] rösn i "a"atdat; v. also FrO VII awra: mihr(a)g (q.v.) Hence it follows that mäna- signifies the lowest of the celestial spheres, that next above
### HUB xorsid
8318:pataxsah ^), paz. padisah Shk. 262 ; xursed *Sonne', zd. hvare-
```


## [2026-09-06T21:41:28.937Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8310,8325p' HUB.txt; echo \"=== NYB xvarset\"; grep -n \"xvaršēt\\|xvarset\" NYB_vol2_glossary.txt | head -4"
}
```


### [2026-09-06T21:41:28.984Z] TOOL RESULT

```
'beredt (oben p. 82, 83), zd. xsva^wa-; sSd 'Sonne*, zd. xsa^ta-;
§%r *Milch* = skr. kslra- ; sustan Vaschen H. 782 , oben
p. 79 ; mar *Gatte H. 796, oben p. 82 ; isnOsa 'Niesen H.
90, oben p. 15.
Nach Praefixen und in Komp. : nis^b abwarts, unten ,
phi. nisSpak Untergang (oben p. 101) = zd. '^nixsvaepa-
H. 1034; Osuftan erregt werden, phi. asdp Terwirrung',
iran. xsup^ skr. ksvbh (oben p. 7); padsdh *K5nig, phi.
pataxsah ^), paz. padisah Shk. 262 ; xursed *Sonne', zd. hvare-
xsaet^m, syr. noch 1tt?D*lD = xvarxs(^d Hoffmann, Aus-
ziige p. 150, Nr. 1212; ArdasTr = phi. Artaxsa&r,
Keine Ausnahme ist xaszn *blaulich', das nicht mit xs
anlautete, da es ---- zd. axsa^na- und also aus *axsen um-
gestellt ist (§ 62).
b) inlautend vor Konsonanten: rosan 'hell* zd.
raoxsna- ; dsna 'bekannt* = ap. *axsnaka-'^ phi. dsnak ; astl
=== NYB xvarset
2417:mänenak [m’nynk'] *rainy, *rain-bear- ing: avr i ~ 891%. — In a collection of Av. glosses with Phl. translation, PT 72 (defectively rendered by Barthelemy, GA 55, and utilized in this form in AirWb as „FrBy”) we find: mano: mihr(a)g pädak — staro : star pādak — mänhö: mah padak — hwarö : xvaršēt pādak — anagrd raocá: hàn i asar [i] rösn i "a"atdat; v. also FrO VII awra: mihr(a)g (q.v.) Hence it follows that mäna- signifies the lowest of the celestial spheres, that next above
```


## [2026-09-06T21:41:39.876Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=8180 && NR<=8330' HUB.txt | grep -n -- \"^ *[-—] *[0-9]\\{1,3\\} *[-—]\\| [0-9]\\{2,3\\} $\" | tail -5; echo ---; awk 'NR>=8250 && NR<=8320' HUB.txt | grep -n \"§ *2[0-9][0-9]\\|^ *[0-9]\\{2,3\\}\\.\" | head"
}
```


### [2026-09-06T21:41:42.200Z] TOOL RESULT

```
---
```


## [2026-09-06T21:42:06.584Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"þqei\\|qþei\\|kseti\\|ksiyati\\|ktizo\\|kti^w\\|soi&ra\\|soidra\" WLD_Bd1_pages.txt | head -10; echo \"--- leaf 512-514\"; for n in 512 513 514; do echo \"### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' WLD_Bd1_pages.txt | head -8; done"
}
```


### [2026-09-06T21:42:08.453Z] TOOL RESULT

```
61706:lit. grukseti
78608:chend atmen“, duksas „Seufzer“, dukseti, duksduti „hauchen, atmen, seufzen“;
--- leaf 512-514
### leaf 512
               -




                                                             kser-       — ksuelp-                                                 503

von wilden Kindern; Possen reiBen, Zoten angeben" (vgl. dt. Schwank zu
### leaf 513
504                                                          kpei            qpep)-, qpe i)-


     DaB mit Anlaut k[s]u- auch ags. hwilpe „ein schreiender Meervogel",
ndl.  wulp ,.Regenpfeifer“, nd. {reycn- wilp, ivalp, wolp ds verwandt seien    )



### leaf 514
                                          i                                                             :                                                     ;




                                                                 qpen-            — q”hpei-                                                              505

Kretschmer aaO.; Yermittlung mit der Sippe von na/ia, gxdoaodai                                                                                         siehe
```


## [2026-09-06T21:42:10.992Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==513' WLD_Bd1_pages.txt | head -40"
}
```


### [2026-09-06T21:42:13.131Z] TOOL RESULT

```
504                                                          kpei            qpep)-, qpe i)-


     DaB mit Anlaut k[s]u- auch ags. hwilpe „ein schreiender Meervogel",
ndl.  wulp ,.Regenpfeifer“, nd. {reycn- wilp, ivalp, wolp ds verwandt seien    )




(-p
    - aus -pp- aus -jm-h, ist ein schwanke Konstruktion; wohl zu aisl.
hvellr ,.gellend" usw. (s. qkeZ).


kpei-        ,,siedeln, sich                ansiedeln, eine Niederlassung griinden".
     Ai. kheti, kbiyati ,,weilt, wohnt”, av. saeiti ds..                                            ai. ksiti-,              av. iiti- „Wohn-
platz,       Siedelung”,                ai.       ksetra -,         av. soidr'- n. ,,Grundbesitz, \Yohnplatz“, ai.
kitma- m. ,.ruhiges Verweilen";
  arm. (Hiibschmann StraBburger Festschrift 1901, 70 f.              bUn, Gen sini                                       !




..bewohnt. bebaut, bliihend, Dorf, Weiler” (vgl.bes.gr, y.xoivu)\
  gr. y.xpm ,,grflnde‘‘, evy.xif.ievog ..wohl gebaut (Haus, Stadt', wohl an-
gebaut, bestellt (Land/      ex-y.xtxog ds., TxsQixxiovsg, jzEgiy.ztzcu ,.Umwohner,
                                                    -
                                                        ,



Nachbarn". auq ly.rioveg .,herumwohnende‘' (zur Form apcpiy.xvovsg Lit. bei
Boisacq 525 Anm. 2        y.xLoig  ,,Anbauung, Ansiedelung“, y.xoiva iRhodos,
                                              ,



Karpathos) „\Vohnsitz, Gemeindebezirk”, auch y.xiXog „ruhig, still'' (eigentl.
„an die Siedelung gebannt, gezakmt" nach Osthoff, Patrubany’S Sprachw.
Abh. II 72 ff., 30 f. Par. I 68; nicht zu lat silco nach Froehde BB. 21, 329,
```


## [2026-09-06T21:52:21.748Z] TOOL CALL #102: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk279.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nU_XORSID = W + \"%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF\"\nU_DARAX  = W + \"%D8%AF%D8%B1%D8%AE%D8%B4%DB%8C%D8%AF%D9%86\"\nU_ROWSAN = W + \"%D8%B1%D9%88%D8%B4%D9%86\"\nU_JAM    = W + \"%D8%AC%D9%85%D8%B4%DB%8C%D8%AF\"\nU_PIR    = W + \"Reconstruction:Proto-Iranian/x%C5%A1aytah\"\nU_AMPH   = W + \"amphictyony\"\nU_KTIZO  = W + \"%CE%BA%CF%84%CE%AF%CE%B6%CF%89\"\nU_TKEY   = W + \"Reconstruction:Proto-Indo-European/t%E1%B8%B1ey-\"\nU_DERAFS = W + \"%D8%AF%D8%B1%D9%81%D8%B4\"\nU_SID    = W + \"%D8%B4%DB%8C%D8%AF\"\n\ndoc = {\n \"pdf_page\": 279,\n \"book_page\": 249,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n\n # ------------------------------------------------------------------ entry 0\n {\n  \"entry\": 0,\n  \"root\": \"Ksei 2\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Walde–Pokorny I 501 *qsei- 'bright' (an Iranian-only reconstruction); modern handbooks go back only to Proto-Iranian *xšaytáh 'bright, shining', origin beyond Iranian unknown\",\n  \"note\": \"The headword, the language label 'Indo-European' and the gloss 'bright' are copied faithfully from Nourai's first reference: Walde–Pokorny, Vergleichendes Wörterbuch I 501 opens an entry 'qsei- „licht“' and puts under it exactly the two Avestan items of this chart — 'Av. xšae-ta-, f. xšōiθni- „licht, strahlend, herrlich“, a-xšae-na- „dunkelfarbig“ (eig. „nicht licht“)'. The problem is that the root is Iranian-internal: Walde–Pokorny's only non-Iranian comparison on that page is Old Norse seiðr 'coalfish', which they themselves mark 'zw.' (doubtful), and Pokorny's own IEW of 1959 dropped the entry — pp. 625–626 have only kseip- 'to throw', kseu-, kseud- 'to grind' and kt̍e(i)- 'to acquire, possess', no 'bright' root; Watkins/AHD has no such root either. Wiktionary reconstructs Proto-Iranian *xšaytáh 'bright, shining' and gives its further etymology as 'unknown'; a frequently voiced alternative connects xšaēta- with the verb xšay- 'to have power, rule' (Av. xšayeiti, OP xšāyaθiya-), which would explain why Bartholomae glosses the adjective both 'glänzend' and 'herrlich' and why it is the standing epithet of the sun and of king Yima. So: the Iranian word-family Nourai assembles is real and correctly assembled, but 'Ksei 2' is not a securely reconstructible Indo-European root — hence 'plausible' rather than 'confirmed'. Two further cross-cutting points, argued at the nodes: raoxšna- and drafša- in node #1 (and rowašan/daraḵšīdan/darafašīdan in node #2) do not belong to this root at all, and the Avestan word in node #1 printed 'xšôithmi' is a misprint for xšōiθnī-.\",\n  \"note_fa\": \"سرواژهٔ «Ksei 2» و معنای «درخشان» را نورایی عیناً از والدهٔ‌پوکورنی (جلد ۱، ص ۵۰۱) گرفته است؛ آنجا زیر مدخل «qsei- „licht“» همین دو واژهٔ اوستایی آمده است: xšaēta- (مؤنّث xšōiθnī-) «روشن، درخشان» و a-xšaēna- «تیره‌رنگ، در اصل „ناروشن“». امّا این ریشه درون‌ایرانی است: تنها شاهد غیرایرانیٔ والدهٔ‌پوکورنی یعنی نرسی باستان seiðr را خود آنان «مشکوک» خوانده‌اند، پوکورنی در چاپ ۱۹۵۹ این مدخل را یکسره حذف کرده و واتکینز (AHD) نیز چنین ریشه‌ای ندارد. پژوهش امروزی (ویکی‌واژه) تنها تا ایرانی آغازین *xšaytáh «درخشان» پیش می‌رود و ریشهٔ فراتر از آن را ناشناخته می‌داند؛ برخی نیز xšaēta- را به ستاک xšay- «فرمان راندن، توانا بودن» می‌بندند که توجیه می‌کند چرا بارتولومه آن را هم «glänzend» و هم «herrlich» معنا کرده است. پس خانوادهٔ ایرانیٔ این نمودار درست است، امّا «Ksei 2» ریشهٔ هندواروپایی مسلّمی نیست: ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [U_PIR, U_SID],\n  \"ref_check\": [\n    {\"ref\": \"WLD1:501\", \"status\": \"supports\",\n     \"note\": \"Walde–Pokorny Bd. I p.501 (WLD_Bd1_pages.txt leaf 510, header 'qsei- — qseu-, qsneu-, qneu-, sneu- 501'): 'qsei- „licht“. Av. xšae-ta-, f. xšōiθni- „licht, strahlend, herrlich“, a-xšae-na- „dunkelfarbig“ (eig. „nicht licht“, Bartholomae IF. 5, 360 Anm. 1); xšaeta- = aisl. seiðr „merlangus carbonarius, Kohlfisch“? ... zw.' — exactly Nourai's root, label and gloss, with the ON comparison flagged doubtful.\"},\n    {\"ref\": \"BRT:541\", \"status\": \"supports\",\n     \"note\": \"Bartholomae, Altiranisches Wörterbuch col. 541–542 (BRT.txt line 10698): 'j. xšaeta- Adj., fem. xšōiθni- „licht, strahlend, glänzend, herrlich“; 1) vom Licht usw. ... 2) von Göttern und Menschen ... a) bes. von Yima: yō yimō xšaētō'. The column number Nourai gives is right.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW pp. 625–626\", \"stance\": \"silent\",\n     \"note\": \"Pokorny 1959 has no 'bright' root here: the ks-/kš- entries around the cited pages are 'kseip-, kseib- „to throw“' (625), 'kseu-, kseud-' (625) and 'kt̍e(i)-, kt̍a(i)- „to acquire, possess“' (626, with Av. xšayati, xšaθra-). The 1927 Walde–Pokorny entry qsei- was abandoned in the 1959 revision.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, Appendix of IE roots\", \"stance\": \"silent\",\n     \"note\": \"grep of AHD_watkins1985.txt for 'ksei'/'to shine, bright' returns no root of this shape; Watkins's only kš- root in this area is 'tkei-. To settle, dwell, be home'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 15.63, p.1053\", \"stance\": \"partial\",\n     \"note\": \"Buck prints 'Av. axšaéna-, neg. cpd. : xšaéta- „bright“ (15.57). Barth. 51' — he confirms the Avestan pair but reconstructs nothing above Iranian.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. šēd, xwar(x)šēd\", \"stance\": \"supports\",\n     \"note\": \"'šēd [šyt | N ~] bright; sorrel (horse)'; 'xwar(x)šēd [hwl(h)šyt' | M xwrxšyd, N xuršēd] sun' — the Middle Persian link in the chain is exactly as drawn.\"}\n  ],\n  \"nodes\": [\n\n  {\n   \"id\": 1, \"lang\": \"Avestan\",\n   \"words\": \"xšae-ta, xšôithmi; hvare-xšâeta; yima-xšâetem; raoč-xšaena, raoxšna; drafša\",\n   \"verdict\": \"transcription_suspect\",\n   \"derivation\": \"Av. xšaēta- 'bright, shining, glorious', fem. xšōiθnī-, is the head of the family; Bartholomae AiW 541–542 gives it verbatim, with the two compounds Nourai lists: huuarə.xšaēta- 'the shining sun' (Yt.6.1, 6.4, Y.22.24, always of the sun as a divinity) and yima- xšaēta- 'the brilliant Yima' (yō yimō xšaētō, Yt.19.31 etc.). Those two are confirmed by every source consulted. THREE things are wrong with the box, however. (a) The second form printed, 'xšôithmi', is not an Avestan word: it is a misprint for the feminine xšōiθnī- — both of Nourai's own references print it correctly (WLD I 501 'f. xšōiθni-', BRT 541 'fem. xšōiθni-'), and the 300-dpi render of the printed page shows the book itself has 'xšôithmi' with an m, so the extraction is faithful and the error is the author's/typesetter's (n set as m). (b) Av. raoxšna- 'bright' (and the raoč-/raok- variant) is not from this root: it is *rauk-s-na-, a -na- derivative of raok-/rauc- 'to shine' (PIE *lewk-), where -xš- is simply the contact of k and s — Nourai's own '☞ Leuk' concedes this, and Walde–Pokorny I 501 does not list it under qsei-. (c) Av. drafša- 'banner' (Y.10.14, Yt.1.11) is matched by Skt. drapsa- and by MP drafš, Arm. loanword drauš; Horn no.553, Hübschmann 553 and Nyberg II s.v. drafš all derive it that way, and Cheung sets up an Iranian *drafš '?to behave like a banner, fly up, shine, tremble' with a possible link to PIE *drep- 'to cut/tear off'. Its 'brightness' sense is secondary (a banner flashing/fluttering), not evidence for *ksei-.\",\n   \"derivation_fa\": \"پایهٔ این خانواده صفت اوستایی xšaēta- «روشن، درخشان، شکوهمند» است که مؤنّث آن xšōiθnī- می‌شود؛ بارتولومه (ستون ۵۴۱) همین را با دو ترکیب huuarə.xšaēta- «خورشید درخشان» و yima.xšaēta- «جمّ درخشان» می‌آورد و این دو تردیدناپذیرند. امّا سه ایراد: ۱) صورت چاپی «xšôithmi» واژهٔ اوستایی نیست و غلط چاپیٔ xšōiθnī- است (هر دو مأخذ خود نورایی درست آورده‌اند؛ از روی تصویر صفحهٔ چاپی دیدیم که خطا از خود کتاب است نه از خوانش اسکن). ۲) raoxšna- «روشن» از این ریشه نیست؛ صورت اصلی آن *rauk-s-na- از ستاک raok- «درخشیدن» (هندواروپایی *lewk-) است و «xš» در آن حاصل برخورد k و s است، نه ریشهٔ *ksei-. ۳) drafša- «درفش، پرچم» به گواهی هرن، هوبشمان، نیبرگ و چونگ هم‌ریشهٔ سنسکریت drapsa- است و معنای «درخشش» در آن ثانوی است.\",\n   \"error_in\": \"book\",\n   \"book_prints\": \"xšae-ta, xšôithmi : bright\",\n   \"correct_form\": \"xšaēta-, fem. xšōiθnī- (xšôithnî) 'bright, shining'\",\n   \"sources\": [U_XORSID, U_JAM, U_PIR, U_DERAFS],\n   \"ref_check\": [\n     {\"ref\": \"WLD1:501\", \"status\": \"partial\",\n      \"note\": \"p.501 has 'Av. xšae-ta-, f. xšōiθni- „licht, strahlend, herrlich“' and a-xšae-na-, and prints the feminine with -n-, not -m-; it does NOT list hvarə-xšaēta-, yima-xšaēta-, raoxšna- or drafša- under this root, so the last two words of the box have no support from the reference cited for them.\"},\n     {\"ref\": \"BQT:788\", \"status\": \"supports\",\n      \"note\": \"Borhan-e Qate', Mo'in's ed., s.v. خورشید (BQT_v2_pages.txt leaf 246, printed p.786 by the +540 running-head offset — i.e. Nourai's 788 is within the ±2–3 drift the offset note warns about): 'خورشید — بضم اول و واو معدوله، از خور (آفتاب) + شید؛ اوستا «hvara xshaeta» پهلوی xvaršēt ... بمعنی آفتاب درخشان'.\"},\n     {\"ref\": \"BQT:1320\", \"status\": \"supports\",\n      \"note\": \"Borhan vol.3 printed p.۱۳۲۰ = PDF page 111 (read from the page image; saved to data/verification/sources/refs/ocr/BQT/1320.png and .vision.txt). Headword «شید ۳» with Mo'in's footnote: 'اوستا xshaeta (درخشان)، پهلوی shēt، در ارمنی ashxēt (سرخ قهوه‌ای) [در اسب] ... «هوبشمان ۸۰۱» همین کلمه است که در «خورشید» و «جمشید» آمده'. The default tool offset (pdf 115) lands on printed 1323; use --pdf-page 111.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BRT\", \"where\": \"AiW col. 541–542 s.v. xšaeta-\", \"stance\": \"supports\",\n      \"note\": \"'xšaeta- Adj., fem. xšōiθni- „licht, strahlend, glänzend, herrlich“ ... a) bes. von Yima: yō yimō xšaētō'; hvarə.xšaēta- has its own entry (BRT.txt line 4752: 'hvarə.xšaitahe ‘sāhe raōcahe Yt.6.0, Y.22.24'). Also col. 51 'a-xšaena- „dunkelfarbig“ ... eig. „nicht licht“, vgl. xšaēta-'.\"},\n     {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 27, 96, 79\", \"stance\": \"supports\",\n      \"note\": \"'drafš [dlpš | P drfš, N ~] banner'; 'drafšīdan, drafš- 1. shine; 2. tremble'; 'šēd bright; sorrel (horse)'; 'xwar(x)šēd ... sun' — MacKenzie keeps drafš 'banner' and šēd 'bright' as separate lexemes.\"},\n     {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary s.v. drafš\", \"stance\": \"contradicts\",\n      \"note\": \"'drafš [dlpš] banner 27:22, 29:8-16. — Av. (771 sq.) drafša-; MPrth drfš; Arm. lw. drauš; NP dirafs.' Nyberg files drafš with Av. drafša- (AiW col. 771), not with xšaēta- (col. 541).\"},\n     {\"src\": \"HRN\", \"where\": \"Grundriss nos. 506, 553, 631\", \"stance\": \"partial\",\n      \"note\": \"No.506 'xʷaršēd „Sonne“. aw. hvare.xšaētəm „strahlende Sonne“; phlv. xʷaršēt bzw. xuršēd' (supports the sun compound), but No.553 'direš „Fahne, Banner“. aw. drafša-; phlv. drafš; ai. drapsa- „Tropfen“' and No.631 'rōšan „leuchtend, hell“ ... aw. raoxšna-' put the other two words elsewhere.\"},\n     {\"src\": \"CHEUNG\", \"where\": \"s.v. *drafš\", \"stance\": \"contradicts\",\n      \"note\": \"Cheung sets up '*drafš ? “to ‘behave’ like a banner, fly up, shine, tremble ?”' with 'YAv. drafša- ‘banner’ (Y 10.14, Y 57.25, Yt 1.11)', nominal *drafš/sa- 'flag, banner', MP drafš, NP dirafs (> dirafsīdan 'to shine') — a root of its own, and possibly IE *drep-.\"}\n   ]\n  },\n\n  {\n   \"id\": 2, \"lang\": \"Persian\",\n   \"words\": \"šîd; xoršîd; Jamšîd; draxšîdan; rowšan; drafšîdan\",\n   \"verdict\": \"disputed\",\n   \"derivation\": \"Three of the six words are exactly right and three are misfiled. RIGHT: شید šīd 'brightness' < MP šyt' /šēd/ 'bright; sorrel (horse)' < Av. xšaēta- — Iranian initial xš- regularly loses the x in Persian (Hübschmann, Persische Studien: 'šēd „Sonne“, zd. xšaēta-'), and MP ē gives NP ī. خورشید xoršīd < MP xwar(x)šēd (Pahl. hwl(h)šyt', Manich. xwrxšyd) < Av. huuarə.xšaēta- 'the shining sun', first element xʷar 'sun' (PIE *soh2wl-); Mo'in's footnote in Borhan-e Qate' prints precisely 'اوستا hvara xshaeta پهلوی xvaršēt'. جمشید Jamšīd < MP ymšyt' /Jamšēd/ < Av. yima.xšaēta-, Yima (= Skt. Yama, PIE *yemH-ós 'twin') + xšaēta-, so literally 'Yima the brilliant' — the extras شیده and مهشید (Mo'in: 'مهشید [= ماه‌شید] پرتو قمر، ماهتاب') belong here too. WRONG: روشن rowšan < MP lwšn' /rōšn/ < OIran. *rauxšna- (Av. raoxšna-) < PIIr. *ráwkšnaH < PIE *lówksneh2 'moon' (Lat. lūna, OCS luna, Arm. lusin), a doublet of رخشان; Horn no.631 and Hübschmann file it under raoxšna-, not under xšaēta-. درخشیدن draxšīdan is, on Wiktionary's analysis, a blend of درفشیدن darafšīdan (to MP drafš 'banner') with رخشیدن raxšīdan (< Sogd. rwxšnh rōxšan 'bright', i.e. the same *rauk-s-na-) — which is why the chart's own extras رخشیدن، رخش، روشنایی sit next to it; درفشیدن darafšīdan and درفش likewise go with Av. drafša-/Skt. drapsa- (Mo'in: 'درفش [= درخش] نور، فروغ، روشنایی'). Hence 'disputed' for the box as a whole.\",\n   \"derivation_fa\": \"از شش واژهٔ این جعبه سه تا درست است و سه تا نادرست. درست: «شید» از فارسی میانهٔ شید شēd از اوستایی xšaēta- (xš- آغازین ایرانی در فارسی به ش تبدیل می‌شود؛ هوبشمان)؛ «خورشید» از فارسی میانهٔ xwar(x)šēd از اوستایی huuarə.xšaēta- «آفتاب درخشان»؛ «جمشید» از yima.xšaēta- «جمّ درخشان». نادرست: «روشن» از فارسی میانهٔ rōšn و ایرانی باستان *rauxšna- (اوستایی raoxšna-) است که به ریشهٔ *lewk- می‌رسد و دوگانهٔ «رخشان» است (هرن شمارهٔ ۶۳۱)؛ «درخشیدن» به تحلیل ویکی‌واژه آمیزهٔ «درفشیدن» (از درفش) و «رخشیدن» (از سغدی rōxšan) است؛ و «درفشیدن» نیز از درفش (اوستایی drafša-، سنسکریت drapsa-). پس در این جعبه نیمی از ادعای نورایی را پژوهش امروزی رد می‌کند.\",\n   \"sources\": [U_XORSID, U_JAM, U_SID, U_ROWSAN, U_DARAX, U_DERAFS],\n   \"ref_check\": [\n     {\"ref\": \"BQT:756\", \"status\": \"not_found\",\n      \"note\": \"By the verified vol.2 offset (printed = leaf + 540) printed p.756 is in the خط entries (خط ریحان، خط سبز ...); the words of this box are scattered over خورشید (p.786, leaf 246), درفشیدن (p.836, leaf 296) and شید (vol.3 p.1320). p.756 belongs to the خشن/خشین group of node #4, whose card carries the same reference — the two boxes appear to share a single mis-copied citation.\"},\n     {\"ref\": \"MON:1425\", \"status\": \"not_checked\",\n      \"note\": \"Nourai's MON page numbers are the 6-vol Amir Kabir 1363 lexicon; only the 2-vol Adena reprint is on disk (different pagination). The entries themselves are there and agree — e.g. 'مهشید [= ماه‌شید] (امر.) پرتو قمر، ماهتاب' and 'درفش [= درخش] (ا.) نور، فروغ، روشنایی' (MON_part1.txt line 60517) — but the cited page cannot be confirmed.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"HUB\", \"where\": \"Persische Studien, Lautlehre §61 (anlautendes xš-)\", \"stance\": \"supports\",\n      \"note\": \"'šēd „Sonne“, zd. xšaēta-; ... xuršēd „Sonne“, zd. hvare-xšaētəm, syr. noch ... = xvarxšēd' (HUB.txt lines 8310–8319). Two lines further down Hübschmann files 'rōšan „hell“ zd. raoxšna-' under a different rule (-xš- before a consonant), i.e. not with xšaēta-.\"},\n     {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. šēd, xwar(x)šēd, drafš(īdan), rōšn\", \"stance\": \"partial\",\n      \"note\": \"supplies each Middle Persian link ('šēd ... bright', 'xwar(x)šēd ... sun', 'drafš ... banner', 'drafšīdan ... 1. shine; 2. tremble', 'bright rōšn, šēd') but keeps drafš- and rōšn apart from šēd.\"},\n     {\"src\": \"HRN\", \"where\": \"nos. 506, 553, 631\", \"stance\": \"partial\",\n      \"note\": \"supports xoršīd (no.506) but derives rōšan from Av. raoxšna- (no.631) and dirafs from Av. drafša- (no.553), with the remark that np. dirafsīdan 'to flash' is connected with duruxs, on which Hübschmann (553) comments 'Die Vermutung über die Etym. von np. duruxš ist sehr unglücklich.'\"},\n     {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (Adena 2-vol reprint) s.vv. درفش، مهشید\", \"stance\": \"partial\",\n      \"note\": \"'درفش: [= درخش] (ا.) نور، فروغ، روشنایی. (ص.) درخشان، درخشنده' — Mo'in equates درفش and درخش (so the doublet draxšīdan/drafšīdan is real) but gives no Avestan xšaēta- source for them.\"},\n     {\"src\": \"BQT\", \"where\": \"vol.2 p.786 s.v. خورشید; vol.3 p.1320 s.v. شید\", \"stance\": \"supports\",\n      \"note\": \"Mo'in's two footnotes give the whole chain for شید / خورشید / جمشید: 'اوستا xshaeta (درخشان)، پهلوی shēt ... همین کلمه است که در «خورشید» و «جمشید» آمده'.\"}\n   ]\n  },\n\n  {\n   \"id\": 3, \"lang\": \"Avestan\",\n   \"words\": \"a-xšae-na\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"Av. a-xšaēna- 'dark-coloured' (Aog. 73 'the dark man'; Vd. 22.4 gauúam axšaēnanąm 'of dark-coloured cattle') is a privative compound of a- (the zero-grade IE negation *n̥-, Nourai's '☞ Ne 1') and a -na- stem beside xšaēta-. Bartholomae AiW col. 51 states Nourai's arrow verbatim: 'a-xšaena- Adj. „dunkelfarbig“ ... Eig. „nicht licht“, vgl. xšaēta-', adding the Pahlavi gloss axšēn; Walde–Pokorny I 501 repeats it under qsei-, and Buck 15.63 p.1053 — the exact page cited — prints 'Av. axšaéna-, neg. cpd. : xšaéta- “bright” (15.57). Barth. 51.' The semantic route is 'not bright' > 'dark' > the dark end of the blue-green band, which is why the Persian and Sogdian reflexes come out as 'dark blue' and 'green' respectively. Structurally the box is drawn from #1 rather than from the root, which is right: the negation is built on the xšaēta- stem itself.\",\n   \"derivation_fa\": \"صفت اوستایی a-xšaēna- «تیره‌رنگ» ترکیبی سلبی است: پیشوند نفی a- (همان *n̥- هندواروپایی) + ستاکی از همان ریشهٔ xšaēta-. بارتولومه در ستون ۵۱ دقیقاً می‌نویسد: «در اصل „ناروشن“، سنجیده شود با xšaēta-» و صورت فارسی میانهٔ axšēn را می‌افزاید؛ باک نیز در همان صفحهٔ ۱۰۵۳ که نورایی ارجاع داده همین را می‌آورد. تحول معنایی از «ناروشن» به «تیره» و سپس به دامنهٔ کبود–سبز است. ادعای نورایی درست است.\",\n   \"sources\": [U_PIR],\n   \"ref_check\": [\n     {\"ref\": \"WLD1:501\", \"status\": \"supports\",\n      \"note\": \"p.501 under qsei-: 'a-xšae-na- „dunkelfarbig“ (eig. „nicht licht“, Bartholomae IF. 5, 360 Anm. 1)'.\"},\n     {\"ref\": \"SYN:1053\", \"status\": \"supports\",\n      \"note\": \"Buck, Selected Synonyms, 15.63 DARK (in Color), p.1053 (SYN.txt leaf for printed 1053, the recto between the 1052/1054 running heads): 'Av. axšaéna-, neg. cpd. : xšaéta- “bright” (15.57). Barth. 51.' The Avestan word is even the entry's Avestan lemma in the head table.\"},\n     {\"ref\": \"BQT:1320\", \"status\": \"partial\",\n      \"note\": \"Borhan vol.3 p.1320 (read from the page image) has Mo'in's footnote on شید giving Av. xshaeta 'drakhšān', i.e. the positive base, but nothing about a-xšaēna-; the Persian reflexes of the negated form are treated at خشین/خشن in vol.2 (pp. 753–755), not here.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BRT\", \"where\": \"AiW col. 51 s.v. a-xšaena-\", \"stance\": \"supports\",\n      \"note\": \"'j. a-xšaena- Adj. „dunkelfarbig“: anšō °nō Aog. 73; — gavąm °nanąm V. 22.4. — Eig. „nicht licht“, vgl. xšaēta-; Bthl. IF. 5.360. — mp. (Pü.) axšēn' (BRT.txt line 3135).\"},\n     {\"src\": \"SOD\", \"where\": \"Gharib no. 707\", \"stance\": \"supports\",\n      \"note\": \"'707 ʾaxšʾynh B,S — axšēn ... ⊙Av. axšaena — green, greenish' — an independent Iranian witness that the compound existed in East Iranian too.\"},\n     {\"src\": \"HUB\", \"where\": \"Persische Studien, §62\", \"stance\": \"supports\",\n      \"note\": \"'Keine Ausnahme ist xašīn „bläulich“, das nicht mit xš anlautete, da es = zd. axšaēna- und also aus *axšēn umgestellt ist (§62)'.\"}\n   ]\n  },\n\n  {\n   \"id\": 4, \"lang\": \"Persian\",\n   \"words\": \"xašan; xašîsâr\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"NP خشین xašīn (variants خشی xašī, خشینه xašīna, خشن xaš(a)n) 'dark blue, livid, blackish' continues MP axšēn < Av. axšaēna-, with loss of the unstressed initial a-; Hübschmann states this explicitly — 'Keine Ausnahme ist xašīn „bläulich“, das nicht mit xš anlautete, da es = zd. axšaēna- und also aus *axšēn umgestellt ist'. Borhan-e Qate' (vol.2 pp.753–755, the pages Nourai's BQT:756 points at) has 'خشن ... بمعنی کبودرنگ' and 'خشینه ... بمعنی خشین است که هر چیز سیاه‌رنگه مایل بکبودی باشد'; Mo'in's Farhang has 'خشین [= خشی – خشینه] (ص.) کبودرنگ، تیره‌رنگ، سیاه‌رنگ'. The bird name خشیسار / خشین‌سار / خشن‌سار is that adjective + سار 'head' — Mo'in's footnote on the same page: 'از خشن (ه.م) + سار (سر) = خشسار' — i.e. 'dark-head'; Borhan describes it as 'نوعی از مرغابی ... پشت او سیاه‌رنگ است و بر میان سر خال سپیدی دارد', matching Nourai's gloss 'a blue bird with white head'. Asadi Tusi's Loghat-e Fors (Nourai's FRS:89) has the headword خشنسار 'a water bird, white-headed', with Daqiqi's line 'عقاب تیز برباید خشنسار'. Two small caveats: the primary lexical shapes are خشین/خشین‌سار (Nourai's خَشَن and خَشیسار are the Borhan variants), and the identical-looking Arabic خَشِن 'rough' is a wholly unrelated homograph.\",\n   \"derivation_fa\": \"«خشین» (و گونه‌های خشی، خشینه، خشن) به معنی «کبودرنگ، تیره‌رنگ» دنبالهٔ فارسی میانهٔ axšēn از اوستایی a-xšaēna- است که همزهٔ آغازین بی‌تأکید آن افتاده است؛ هوبشمان همین را صریح می‌گوید. برهان قاطع (ص ۷۵۳–۷۵۵) و فرهنگ معین معنای «کبودرنگ» را تأیید می‌کنند، و حاشیهٔ معین بر همان صفحه می‌نویسد: «از خشن + سار (سر)»؛ یعنی «خشین‌سار» مرغابی‌ای است با پشت سیاه و خال سپید بر سر. لغت فرس اسدی نیز ذیل «خشنسار» با شاهد دقیقی همین را دارد. ادعای نورایی درست است؛ تنها باید متوجّه بود که «خَشِن» عربی به معنی «زبر» هم‌نگاشتی اتفاقی است و ربطی به این واژه ندارد.\",\n   \"sources\": [U_PIR],\n   \"ref_check\": [\n     {\"ref\": \"BQT:756\", \"status\": \"supports\",\n      \"note\": \"Borhan-e Qate', Mo'in's ed., vol.2: خشی/خشین at leaf 213 = printed p.753 and خشن/خشینه/خشین‌سار at leaf 215 = printed p.755 (BQT_v2_pages.txt lines 12525, 12654–12666) — within the ±2–3 drift of the running-head offset, so Nourai's 756 is right. Text: 'خشن ... بمعنی کبودرنگ باشد'; 'خشینه = بروزن دفینه، بمعنی خشین است که هر چیز سیاه‌رنگه مایل بکبودی باشد'; 'خشین‌سار ... نوعی از مرغابی ... پشت او سیاه‌رنگ است و بر میان سر خال سپیدی دارد'; footnote '۴ – از خشن (ه.م) + سار (سر) = خشسار'.\"},\n     {\"ref\": \"FRS:89\", \"status\": \"supports\",\n      \"note\": \"Asadi Tusi, Loghat-e Fors, s.v. خشنسار (FRS.txt lines 5473–5492; the local scan is Eqbal's 1319 ed., different pagination from the 1365 Kharazmi ed. Nourai cites): 'مرغی است آبی؛ سرسپید ... دقیقی گفت: از آن کردار کز مردم رباید / عقاب تیز برباید خشنسار', with the editors' variant note 'خشنسار مرغی است بزرگ آبی تیره‌گون سرسپید'.\"},\n     {\"ref\": \"MON:1425\", \"status\": \"partial\",\n      \"note\": \"The cited Amir Kabir pagination is not on disk, but the entry is: Mo'in, Farhang-e Farsi (Adena reprint, MON_part1.txt line 56672) 'خشین: [= خشی – خشینه] (ص.) کبودرنگ، تیره‌رنگ، سیاه‌رنگ. (ا.) بازی که پشت آن کبود و تیره و چشمهایش سیاه‌رنگ بود'.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"HUB\", \"where\": \"Persische Studien §62\", \"stance\": \"supports\",\n      \"note\": \"'Keine Ausnahme ist xašīn „bläulich“, das nicht mit xš anlautete, da es = zd. axšaēna- und also aus *axšēn umgestellt ist' — the exact Persian < Avestan step Nourai draws.\"},\n     {\"src\": \"BRT\", \"where\": \"AiW col. 51\", \"stance\": \"supports\",\n      \"note\": \"gives the Pahlavi intermediary: 'mp. (Pü.) axšēn' under a-xšaena-.\"},\n     {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. خشین\", \"stance\": \"supports\",\n      \"note\": \"'کبودرنگ، تیره‌رنگ، سیاه‌رنگ' — the colour is 'dark/livid blue', matching Nourai's 'dark blue'.\"},\n     {\"src\": \"FRS\", \"where\": \"Loghat-e Fors s.v. خشنسار\", \"stance\": \"supports\",\n      \"note\": \"11th-c. attestation of the bird name with Daqiqi's verse; note that the oldest lexicographic shape is خشنسار, not Nourai's خشیسار.\"},\n     {\"src\": \"HRN\", \"where\": \"Grundriss\", \"stance\": \"silent\",\n      \"note\": \"grep of HRN.txt for xašīn/xašan/xašīsār finds no numbered entry; Horn does not treat this word.\"}\n   ]\n  },\n\n  {\n   \"id\": 5, \"lang\": \"Sogdian\",\n   \"words\": \"âxs`ynh\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"Sogdian ʾaxšʾynh (Buddhist and Christian Sogdian), read axšēn, 'green, greenish' is the East-Iranian cognate of Av. a-xšaēna-, with the same 'not bright' > 'dark' > 'green' shift the Persian word shows on the blue side. Nourai's own reference states the derivation: Gharib, Sogdian Dictionary, entry no. 707 (printed page ~26–27, i.e. his 'SOD:27') reads '707 ʾaxšʾynh B,S — axšēn, axšēn ? (ʾaxšyn) ⊙Av. axšaena — green, greenish. MDiii 47.8; Bailey, Prolexis, 20', with the neighbouring entries 705 ʾaxšʾynʾak 'greenish' and 708 ʾaxšʾyn wrsʾak 'greenish-haired'. One structural quibble: the arrow is drawn from the root box, but the Sogdian is the sister of the Avestan privative compound (a- + xšaena-), so it should hang from box #3; Gharib himself refers it to Av. axšaena-, not to a bare root.\",\n   \"derivation_fa\": \"واژهٔ سغدی ʾaxšʾynh (خوانده axšēn) «سبز، مایل به سبز» هم‌ریشهٔ مستقیم a-xšaēna- اوستایی است؛ همان تحول معنایی «ناروشن ← تیره ← سبز/کبود» که در فارسی «خشین» دیدیم. خودِ مأخذ نورایی، یعنی فرهنگ سغدیٔ بدرالزمان قریب (مدخل ۷۰۷، ص ۲۶–۲۷)، صریحاً می‌نویسد «⊙اوستایی axšaena». تنها ایراد ساختاری آن است که این جعبه باید از جعبهٔ a-xšaēna- منشعب می‌شد نه از خودِ ریشه. ادعای نورایی درست است.\",\n   \"sources\": [U_PIR],\n   \"ref_check\": [\n     {\"ref\": \"SOD:27\", \"status\": \"supports\",\n      \"note\": \"Gharib, Sogdian–Persian–English Dictionary, entry 707 (SOD.txt lines 12085–12090; the entry falls on SOD_pages.txt leaf 92, and with the documented 'printed ≈ leaf − 66' offset that is printed p.26 — Nourai's SOD:27 within one page): '707 ʾaxšʾynh B,S | axšēn, axšēn ? (ʾaxšyn) ⊙Av. axšaena | green, greenish | MDiii 47.8; Bailey, Prolexis, 20'.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"SOD\", \"where\": \"nos. 705–708\", \"stance\": \"supports\",\n      \"note\": \"the whole small family is there: '705 ʾaxšʾynʾak B ... greenish', '706 ʾaxšʾynʾy = ʾaxšʾynʾak', '707 ʾaxšʾynh ... green, greenish', '708 ʾaxšʾyn wrsʾak ... greenish-haired'.\"},\n     {\"src\": \"BRT\", \"where\": \"AiW col. 51\", \"stance\": \"supports\",\n      \"note\": \"the Avestan source word 'a-xšaena- „dunkelfarbig“ ... eig. „nicht licht“' with MP axšēn — the same form the Sogdian reflects.\"},\n     {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka\", \"stance\": \"silent\",\n      \"note\": \"grep for axšēn/axšaena in ISS_alt_DKS.txt returns nothing usable; Gharib's own reference is to Bailey, Prolexis p.20, which is not in the local library.\"}\n   ]\n  }\n  ]\n },\n\n # ------------------------------------------------------------------ entry 1\n {\n  \"entry\": 1,\n  \"root\": \"Ksei 3\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *tḱey- 'to settle, dwell, cultivate' (Pokorny 626 k̍tʰei-; Walde–Pokorny I 504 kθei-)\",\n  \"note\": \"Pokorny's IEW p.626 heads an entry (transliterated in the local database dump as 'Rhei-') 'to settle', whose material is exactly Nourai's: 'Old Indic kṣeti, kṣiyati “stays, dwells”, Avestan šaēiti ds., Old Indic kṣiti-, Avestan šiti- “residence, settlement”, Old Indic kṣetra-, Avestan šōiθra- n. “estate, residence” ... gr. κτίζω “to found” ... ἀμφικτίονες “they that dwell round”'. Walde–Pokorny I 504 has the same entry under 'kθei-'. Modern practice writes the root *tḱey- (the cluster is *tḱ-, giving Skt kṣ- and Iranian š-, Greek metathesised kt-), and Wiktionary and Beekes (EDG 791–792, s.v. κτίζω) reconstruct it that way; some (Wiktionary) further analyse *tḱéy-ti as built to *teḱ- 'to sire, beget'. Root, language label and gloss are all correct — the only thing to note is that Nourai's spelling 'Ksei 3' follows the Indic/Iranian reflex rather than the reconstructed *tḱ-, and that the page he cites (626) also carries Pokorny's neighbouring root kt̍e(i)- 'to acquire, possess' (Av. xšayati, xšaθra-), with which Pokorny says this one 'belongs probably'.\",\n  \"note_fa\": \"ریشهٔ پوکورنی در صفحهٔ ۶۲۶ دقیقاً همین مدخل است: سنسکریت kṣeti «می‌ماند، ساکن است»، اوستایی šaēiti، سنسکریت kṣetra- و اوستایی šōiθra- «سرزمین، جایگاه» و یونانی κτίζω «بنیاد نهادن». امروز این ریشه را *tḱey- می‌نویسند؛ خوشهٔ *tḱ- در هندی به kṣ-، در ایرانی به ش و در یونانی با قلب به kt- بدل می‌شود. نام ریشه، برچسب زبانی و معنا هر سه درست است؛ ادعای نورایی درست است.\",\n  \"sources\": [U_TKEY, U_KTIZO],\n  \"ref_check\": [\n    {\"ref\": \"POK:626\", \"status\": \"supports\",\n     \"note\": \"IEW p.626 (POK_full.txt lines 51189–51227): 'Root/lemma: k̍θei- | Meaning: to settle | Material: Old Indic kṣeti, kṣiyati “stays, dwells”, Avestan šaēiti ds., ... Avestan šiti- “residence, settlement” ... Avestan šōiθra- n. “estate, residence” ... gr. κτίζω “of a city, to found” ... ἀμφικτίονες “they that dwell round, next neighbours” (to form ἀμφικτύονες Lit. by Boisacq 525 Anm. 2) | Page(s): 626'. Every word of Nourai's chart is on that page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.504\", \"stance\": \"supports\",\n     \"note\": \"'kθei- „siedeln, sich ansiedeln, eine Niederlassung gründen“. Ai. kṣeti, kṣiyati „weilt, wohnt“, av. šaēiti ds., ai. kṣiti-, av. šiti- „Wohnplatz, Siedelung“, ai. kṣetra-, av. šōiθrə- n. „Grundbesitz, Wohnplatz“ ... gr. κτίζω „gründe“ ... ἀμφικτίονες „herumwohnende“ (zur Form ἀμφικτύονες Lit. bei Boisacq 525 Anm. 2)' (WLD_Bd1_pages.txt leaf 513).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. tkei-\", \"stance\": \"supports\",\n     \"note\": \"'tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *(t)koi-mo- in Germanic *haimaz, home ... 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHICTYONY. 3. Probable zero-grade form *tki- in Latin si- in ... situs ... [Pok. 1. k̍ei- 589, tk̍ei- 539.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dictionary\", \"stance\": \"silent\",\n     \"note\": \"grep of IEC.txt for 'kthei', 'ksei-', 'kseti', 'kṣeti' returns no matching lemma; Mann's dictionary is not usable for this root in the local OCR.\"}\n  ],\n  \"nodes\": [\n\n  {\n   \"id\": 1, \"lang\": \"Avestan\",\n   \"words\": \"šaěiti, shiti; šôithra\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"Av. šaēiti '(he) dwells' is the thematic present of the root (PIr. *šai- < PIE *tḱey-), exactly cognate with Skt. kṣéti: the Indo-Iranian cluster *tḱ gives kṣ in Indic but š in Iranian, which is why Sanskrit has kṣ- and Avestan š- throughout the pair. The chart's second word 'shiti' is Av. šiti- 'dwelling place, settlement' (= Skt. kṣiti-), a ti-abstract of the same root — Nourai simply spells the same š twice over (šaēiti / shiti), which is careless but not wrong. šōiθra- n. 'settlement, land, home district' (= Skt. kṣétra- 'field') is the -tra- instrument/place noun; it survives in Middle Iranian šahr and thence NP شهر 'city, country'. Pokorny 626 and Walde–Pokorny I 504 both list šaēiti, šiti- and šōiθra- in exactly this order; the glosses 'living place' and 'land' match 'Wohnplatz, Siedelung' and 'Grundbesitz, Wohnplatz'.\",\n   \"derivation_fa\": \"فعل اوستایی šaēiti «می‌نشیند، ساکن است» زمان حال همین ریشه است، برابر سنسکریت kṣéti؛ خوشهٔ *tḱ هندوایرانی در هندی به kṣ و در ایرانی به ش بدل می‌شود. واژهٔ دوم نمودار («shiti») همان šiti- «جایگاه، مسکن» است که نورایی آن را با رسم‌الخط دیگری نوشته است. šōiθra- «سرزمین، آبادی» (برابر سنسکریت kṣétra-) ساخته با پسوند -tra- است و همان است که در ایرانی میانه šahr و در فارسی نو «شهر» شده است. پوکورنی و والده هر دو همین سه واژه را به همین ترتیب می‌آورند؛ ادعای نورایی درست است.\",\n   \"sources\": [U_TKEY, U_KTIZO],\n   \"ref_check\": [\n     {\"ref\": \"POK:626\", \"status\": \"supports\",\n      \"note\": \"'Old Indic kṣeti, kṣiyati “stays, dwells”, Avestan šaēiti ds., Old Indic kṣiti-, Avestan šiti- “residence, settlement”, Old Indic kṣetra-, Avestan šōiθra- n. “estate, residence”' — word for word Nourai's box.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I 504\", \"stance\": \"supports\",\n      \"note\": \"'av. šaēiti ... av. šiti- „Wohnplatz, Siedelung“ ... av. šōiθrə- n. „Grundbesitz, Wohnplatz“'.\"},\n     {\"src\": \"BRT\", \"where\": \"AiW s.vv. šaēiti / šōiθra-\", \"stance\": \"supports\",\n      \"note\": \"Bartholomae's dictionary is the source Pokorny and Walde quote for these forms; the same lemmas (šōiθra- 'Wohnstatt, Landschaft', with the derivative šōiθrō.pati-) stand in AiW under šay-/ši-.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins s.v. tkei-\", \"stance\": \"partial\",\n      \"note\": \"Watkins gives the root and the Greek and Germanic branches but cites no Avestan forms, so it corroborates the root, not the individual Avestan words.\"}\n   ]\n  },\n\n  {\n   \"id\": 2, \"lang\": None,\n   \"words\": \"\",\n   \"verdict\": \"unverified\",\n   \"derivation\": \"An empty box on the printed page: on the 200/600-dpi render of pdf page 279 (copied to data/verification/sources/refs/ocr/BOOK/279.png) a wide, completely blank rectangle is drawn to the right of the Avestan šaēiti/šōiθra box, with the arrow from it, but it carries no language label, no reference and no word. The extraction is faithful (lang null, refs null, words []). Nothing can be verified. What Nourai must have meant to put there is the Persian continuation of šōiθra-, i.e. MP šahr 'land, country; city' > NP شهر (MacKenzie: 'šahr [štr' | M šr, N ~] land, country; city'), which is the one well-known New Persian reflex of this root.\",\n   \"derivation_fa\": \"این جعبه در صفحهٔ چاپی کاملاً خالی است: در تصویر صفحهٔ ۲۷۹ پی‌دی‌اف مستطیلی پهن و بی‌متن در کنار جعبهٔ اوستایی رسم شده است، بدون نام زبان، بدون مأخذ و بدون واژه؛ استخراج نیز همین را درست ثبت کرده است. چیزی برای ارزیابی وجود ندارد. احتمالاً جای بازماندهٔ فارسیٔ šōiθra- بوده است، یعنی فارسی میانهٔ šahr و فارسی نو «شهر».\",\n   \"sources\": [],\n   \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference of its own.\"}],\n   \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. šahr\", \"stance\": \"silent\",\n      \"note\": \"'šahr [štr' | M šr, N ~] land, country; city' — quoted only to identify what the blank box would have held; it says nothing about Nourai's arrow, since there is no arrow content.\"},\n     {\"src\": \"POK\", \"where\": \"IEW 626\", \"stance\": \"silent\",\n      \"note\": \"no Persian reflex is named at all on the cited page, so the blank cannot be filled from Nourai's own reference either.\"}\n   ]\n  },\n\n  {\n   \"id\": 3, \"lang\": \"Greek\",\n   \"words\": \"ktizein; amphi-ktuoness\",\n   \"verdict\": \"transcription_suspect\",\n   \"derivation\": \"Gk. κτίζω ktízō, inf. κτίζειν 'to found, settle, build (a city)' (Hom. εὐκτίμενος 'well-built', κτίσις 'a founding', Rhod. κτοίνα 'township') is the zero grade *tḱi- of the root, with the regular Greek metathesis *tḱ- > kt-; Watkins states it in those words ('Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHICTYONY') and Beekes, EDG 791–792 s.v. κτίζω gives *tḱey- with Skt. kṣéti and Av. šaēiti as cognates. The compound is ἀμφικτίονες amphiktíones 'those who dwell round about' = ἀμφί 'on both sides, around' (Nourai's '☞ Ambhi') + the participle of that verb, later remodelled as ἀμφικτύονες with an unexplained -υ- (Boisacq 525 n.2, cited by both Pokorny and Walde–Pokorny). The gloss Nourai gives, 'established around each other', is a paraphrase rather than a translation — the word means 'dwelling around (a sanctuary)'. TRANSCRIPTION: the printed page really has 'amphi-ktuoness' with a doubled final -s (checked on the 600-dpi render, saved as data/verification/sources/refs/ocr/BOOK/279.png), which is not a possible transliteration of ἀμφικτύονες; the extraction copied the book correctly, so the slip is the book's.\",\n   \"derivation_fa\": \"یونانی κτίζω (مصدر κτίζειν) «بنیاد نهادن، آباد کردن» از درجهٔ صفرِ ریشه (*tḱi-) ساخته شده و خوشهٔ آغازین در یونانی قلب شده و kt- گشته است؛ واتکینز و بیکس (EDG ۷۹۱–۷۹۲) همین را می‌گویند. ترکیب ἀμφικτίονες «پیرامون‌نشینان» از ἀμφί «پیرامون» + اسم فاعل همین فعل است و بعدها به صورت ἀμφικτύονες درآمده که واکهٔ υ آن توضیح روشنی ندارد. نکتهٔ مهم: صورت چاپی «amphi-ktuoness» با دو s در پایان آوانویسیٔ ممکنی نیست؛ از روی تصویر صفحه دیدیم که خطا در خودِ کتاب است، نه در خوانش اسکن.\",\n   \"error_in\": \"book\",\n   \"book_prints\": \"amphi-ktuoness : established around each other\",\n   \"correct_form\": \"amphi-ktuones = ἀμφικτύονες (older ἀμφικτίονες) 'dwellers round about, neighbours'\",\n   \"sources\": [U_KTIZO, U_TKEY, U_AMPH],\n   \"ref_check\": [\n     {\"ref\": \"POK:626\", \"status\": \"supports\",\n      \"note\": \"'gr. κτίζω “of a city, to found, plant, build”, εὐκτίμενος “well-built” ... περικτίονες, περικτίται “dwellers around, neighbours”, ἀμφικτίονες “they that dwell round, next neighbours” (to form ἀμφικτύονες Lit. by Boisacq 525 Anm. 2)'.\"},\n     {\"ref\": \"AHD:45\", \"status\": \"supports\",\n      \"note\": \"Watkins's appendix s.v. tkei-: '2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHICTYONY' (and the reverse index 'AMPHYCTYONY tkei-'). tkei- is near the end of the alphabetical appendix, consistent with Nourai's p.45 of the AHD 1975 root list.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. I 504\", \"stance\": \"supports\",\n      \"note\": \"'gr. κτίζω „gründe“, εὐκτίμενος „wohl gebaut“ ... ἀμφικτίονες „herumwohnende“ ... κτίσις „Anbauung, Ansiedelung“, κτοίνα (Rhodos, Karpathos) „Wohnsitz, Gemeindebezirk“'.\"},\n     {\"src\": \"KLN\", \"where\": \"Klein p.65 s.v. amphictyony\", \"stance\": \"supports\",\n      \"note\": \"'fr. ἀμφικτύονες, “amphictyons”, fr. earlier ἀμφικτίονες, “they that dwell round about” ... The second element is rel. to Gk. κτίζειν, “to create, found” ... and cogn. with OI. kṣeti, kṣiyati, “abides, dwells” ... Arm. shen, “inhabited”' — note Klein also prints ἀμφικτύονες with one final -s.\"},\n     {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\",\n      \"note\": \"grep of SKT.txt for 'amphictyon' returns nothing; Skeat has no entry for this learned word.\"}\n   ]\n  },\n\n  {\n   \"id\": 4, \"lang\": \"English\",\n   \"words\": \"amphictyony\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": \"English amphictyony 'a confederation of neighbouring Greek states around a common sanctuary (Delphi, Delos, Anthela)' is a 17th–19th-c. learned borrowing of Gk. ἀμφικτυονία amphiktuonía, the abstract in -ία to ἀμφικτύονες, taken over through Latin amphictyones/amphictyonicus (hence the adjective amphictyonic, from L. amphictyonicus < Gk. ἀμφικτυονικός). Nourai's gloss is Klein's wording verbatim — Klein p.65: 'amphictyony, n., confederation of states in ancient Greece, established around a common center'. The route Greek > (Latin) > English is uncontroversial and is given identically by Funk & Wagnalls and Webster.\",\n   \"derivation_fa\": \"واژهٔ انگلیسی amphictyony «اتحادیهٔ دولت‌شهرهای یونانی پیرامون یک پرستشگاه (دلفی، دلوس)» وام‌واژه‌ای عالمانه از یونانی ἀμφικτυονία است که از راه لاتینی (amphictyones، amphictyonicus) به انگلیسی راه یافته است. معنایی که نورایی داده عیناً عبارت کلاین در صفحهٔ ۶۵ است. ادعای نورایی درست است.\",\n   \"sources\": [U_AMPH, U_KTIZO],\n   \"ref_check\": [\n     {\"ref\": \"KLN:65\", \"status\": \"supports\",\n      \"note\": \"Klein, A Comprehensive Etymological Dictionary, p.65 (KLN_1966.txt line 2538, the page marker '65' stands a few lines above): 'amphictyony, n., confederation of states in ancient Greece, established around a common center. — Gk. ἀμφικτυονία, “the Amphictyonic League”, fr. ἀμφικτύονες ... For the first element see amphi-. The second element is rel. to Gk. κτίζειν'. Nourai's gloss is copied from this line.\"},\n     {\"ref\": \"AHD\", \"status\": \"supports\",\n      \"note\": \"Watkins's reverse index lists 'AMPHYCTYONY tkei-' (sic, with the misprint AMPHYCTYONY in the 1985 printing) and the root entry names the word among the English derivatives.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, s.v. amphictyonic\", \"stance\": \"supports\",\n      \"note\": \"'amphictyony or its members or delegates; as, an amphictyonic city or council ... sometimes applied humorously or ironically to any body of persons conferring together'.\"},\n     {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. amphictyony\", \"stance\": \"supports\",\n      \"note\": \"'am-phic’ty-o-ny, n. in ancient Greece, a confederation of states establishe[d] ...; amphictyonic council: in ancient Greece, an assembly composed of delegates from the states associated in an amphictyony'.\"},\n     {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"silent\",\n      \"note\": \"no entry (grep 'amphictyon' in SKT.txt returns nothing).\"}\n   ]\n  }\n  ]\n }\n ]\n}\n\nimport io\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-279.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk279.py"
}
```


### [2026-09-06T21:52:24.583Z] TOOL RESULT

```
ok
```


## [2026-09-06T21:52:29.407Z] TOOL CALL #103: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-279.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 279"
}
```


### [2026-09-06T21:52:31.224Z] TOOL RESULT

```
JSON OK
nodes verified: 9/9
node verdicts: {'transcription_suspect': 2, 'disputed': 1, 'confirmed': 5, 'unverified': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'partial': 3, 'supports': 12, 'not_found': 1, 'not_checked': 2}
books consulted: {'supports': 19, 'contradicts': 2, 'partial': 5, 'silent': 6} | by book: {'BRT': 5, 'PHD': 3, 'HRN': 3, 'HUB': 3, 'MON': 2, 'SOD': 2, 'WLD': 2, 'SKT': 2, 'NYB': 1, 'CHEUNG': 1, 'BQT': 1, 'FRS': 1, 'ISS_alt_DKS': 1, 'AHD': 1, 'POK': 1, 'KLN': 1, 'FSD': 1, 'WEB': 1}
```


## [2026-09-06T21:52:54.911Z] AGENT

Done. `python3 tools/verify_check.py 279` reports **0 PROBLEM lines** (9/9 nodes).

**Page 279 (book p. 249) — verdicts**
- Roots: 1 confirmed (Ksei 3), 1 plausible (Ksei 2)
- Nodes: 5 confirmed, 1 disputed, 2 transcription_suspect, 1 unverified (blank box)
- Ref checks: 12 supports, 3 partial, 1 not_found, 2 not_checked · 18 books consulted

**Root Ksei 2 "bright" — plausible.** WLD I 501 really does head "qsei- „licht“" with Av. xšaēta-/a-xšaēna-, so Nourai copied his source faithfully; but the root is Iranian-only (WP's sole outside witness, ON *seiðr*, is marked doubtful), Pokorny 1959 dropped the entry, Watkins has no such root, and Wiktionary reconstructs only PIr *xšaytáh with origin "unknown".

**Disputed / flagged items**
- *Ksei 2, #2 Persian (disputed)* — šīd, xoršīd, Jamšīd are confirmed (Av. xšaēta- / huuarə.xšaēta- / yima.xšaēta-, MP šēd / xwar(x)šēd / Jamšēd); but **rowšan** is from Av. raoxšna- < PIE *lówksneh₂ (Horn 631, Hübschmann), **draxšīdan** is a blend of derafšīdan (< MP drafš 'banner') + raxšīdan (< Sogd. rōxšan), and **drafšīdan** goes with Av. drafša- / Skt drapsá- (Horn 553, Nyberg, Cheung *drafš). Half the box does not belong to this root.
- *Ksei 2, #1 Avestan (transcription_suspect)* — book prints **"xšôithmi"**; correct is xšōiθnī-, the fem. of xšaēta- (both of Nourai's own refs, WLD I 501 and BRT 541, print it with -n-). `error_in: book`; extraction is faithful. Same node also carries the misfiled raoxšna- and drafša-.
- *Ksei 3, #3 Greek (transcription_suspect)* — book prints **"amphi-ktuoness"** (doubled -s); correct amphi-ktuones = ἀμφικτύονες (older ἀμφικτίονες). `error_in: book`.

**Extraction errors for the owner: none.** The JSON matches the printed page everywhere I checked (refs, Persian script extras, the two Ferdowsi quotes, the blank pass-through box in Ksei 3).

**Reference-lookup notes worth keeping**
- `BQT:1320` (Borhan vol. 3, s.v. شید, Mo'in's footnote "اوستا xshaeta … همین کلمه است که در خورشید و جمشید آمده") is at **PDF page 111**, not the 115 the default offset gives — `ref_page.py BQT:1320` lands on printed 1323. Page image + transcript saved to `data/verification/sources/refs/ocr/BQT/1320.png` / `1320.vision.txt`.
- `BQT:756` on node #2 is a mis-copied citation: p. 756 is the خط entries; it is the correct page for node #4 (خشن/خشین‌سار, printed 753–755). Node #2's words are on 786 (خورشید), 836 (درفشیدن) and 1320 (شید).
- Book page render archived at `data/verification/sources/refs/ocr/BOOK/279.png`; 10 Wiktionary pages archived via `fetch_source.py`.
