# Verification process log — verify-page-291


## [2026-09-06T22:06:15.139Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 291 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-291.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-291.json. Write /home/sfmqrb/git/rishe/data/verification/page-291.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 291` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:06:16.599Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:06:17.308Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:06:17.324Z] TOOL RESULT

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


## [2026-09-06T22:06:17.507Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-291.txt"
}
```


### [2026-09-06T22:06:17.521Z] TOOL RESULT

```
1	=== PDF page 291 (book page 261) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kwel, Qwel : to, move around, dwell  (refs POK:640)  PART 2
4	#1 (parent #0) [Greek] refs=AHD | ku-klos : wheel ; telos : end of a cycle, far away ; telesma : mystery
5	  #2 (parent #1) [Arabic] refs=None | 
6	    #3 (parent #2) [Persian] refs=MON:2232 | telesm «طلسم» : mystery, spell
7	  #4 (parent #1) [French] refs=None | 
8	    #5 (parent #4) [Persian] refs=MON |  | extra: سیکل ، سیلندر ، تلسکوپ ، تلویزیون ، تلگراف
9	  #6 (parent #1) [English] refs=None | cycle, cylinder, encyclopedia ; tele-, teletype, telescope, television, telegraph
10	#7 (parent #0) [Russian] refs=SYN:724; AHD | koleso : wheel ; kaljaska : carriage
11	  #8 (parent #7) [Persian] refs=MON:2861 | kâleskeh «کالسکه» : carriage
12	#9 (parent #0) [German] refs=AHD | hwe-hula : wheel
13	  #10 (parent #9) [English] refs=None | wheel
14	#11 (parent #0) [Latin] refs=AHD | col-ere : to inhabit ; col-lum : neck
15	  #12 (parent #11) [English] refs=None | colony, culture, clown ; collar
16	--- entry 1 ---
17	ROOT [Indo-European] Kwen 1 : holy  (refs POK:630)
18	#1 (parent #0) [Avestan] refs=KLN:746; SYN:1476; HRN:210; BQT:121,210 | spenta : holy, also an herb ; spento-dâto : holy creation ☞Dô 2 ; gao-spenta : holy domestic animal, sheep ☞Gwou
19	  #2 (parent #1) [Persian] refs=None | esfand «اسفند» : an aromatic plant ; Esfandîyâr «اسفندیار» : "holy creation", a name ; gŭsfand «گوسفند» : sheep
20	  #3 (parent #1) [Greek] refs=KLN:7 | apsinthion : an herb
21	    #4 (parent #3) [Arabic] refs=TAD:4 | afsantîn
22	      #5 (parent #4) [Persian] refs=MON:316 | afsantîn «افسنتین» : an herb
23	#6 (parent #0) [Germanic] refs=AHD; KLN:746 | hun-slam : holy
24	  #7 (parent #6) [English] refs=None | housel : communion
25	
```


## [2026-09-06T22:06:20.593Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-291.json",
 "description": "Read source JSON page 291"
}
```


### [2026-09-06T22:06:20.628Z] TOOL RESULT

```
{
  "pdf_page": 291,
  "book_page": 261,
  "entries": [
    {
      "root": {
        "name": "Kwel, Qwel",
        "lang": "Indo-European",
        "refs": "POK:640",
        "gloss": "to, move around, dwell"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "ku-klos", "gloss": "wheel", "script": null},
            {"translit": "telos", "gloss": "end of a cycle, far away", "script": null},
            {"translit": "telesma", "gloss": "mystery", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2232",
          "words": [
            {"translit": "telesm", "gloss": "mystery, spell", "script": "طلسم"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
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
          "refs": "MON",
          "words": [],
          "script_extra": "سیکل ، سیلندر ، تلسکوپ ، تلویزیون ، تلگراف",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cycle, cylinder, encyclopedia", "gloss": null, "script": null},
            {"translit": "tele-, teletype, telescope, television, telegraph", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Russian",
          "refs": "SYN:724; AHD",
          "words": [
            {"translit": "koleso", "gloss": "wheel", "script": null},
            {"translit": "kaljaska", "gloss": "carriage", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:2861",
          "words": [
            {"translit": "kâleskeh", "gloss": "carriage", "script": "کالسکه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "German",
          "refs": "AHD",
          "words": [
            {"translit": "hwe-hula", "gloss": "wheel", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "wheel", "gloss": null, "script": null}
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
            {"translit": "col-ere", "gloss": "to inhabit", "script": null},
            {"translit": "col-lum", "gloss": "neck", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "colony, culture, clown", "gloss": null, "script": null},
            {"translit": "collar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kwen 1",
        "lang": "Indo-European",
        "refs": "POK:630",
        "gloss": "holy"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:746; SYN:1476; HRN:210; BQT:121,210",
          "words": [
            {"translit": "spenta", "gloss": "holy, also an herb", "script": null},
            {"translit": "spento-dâto", "gloss": "holy creation", "script": null, "see": ["Dô 2"]},
            {"translit": "gao-spenta", "gloss": "holy domestic animal, sheep", "script": null, "see": ["Gwou"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "esfand", "gloss": "an aromatic plant", "script": "اسفند"},
            {"translit": "Esfandîyâr", "gloss": "\"holy creation\", a name", "script": "اسفندیار"},
            {"translit": "gŭsfand", "gloss": "sheep", "script": "گوسفند"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Greek",
          "refs": "KLN:7",
          "words": [
            {"translit": "apsinthion", "gloss": "an herb", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "TAD:4",
          "words": [
            {"translit": "afsantîn", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:316",
          "words": [
            {"translit": "afsantîn", "gloss": "an herb", "script": "افسنتین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN:746",
          "words": [
            {"translit": "hun-slam", "gloss": "holy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "housel", "gloss": "communion", "script": null}
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


## [2026-09-06T22:06:21.339Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:06:21.411Z] TOOL RESULT

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
```


## [2026-09-06T22:07:17.608Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo ---- && sed -n 1,60p tools/verify_check.py",
 "description": "List verification dir and check tool"
}
```


### [2026-09-06T22:07:17.652Z] TOOL RESULT

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
----
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
```


## [2026-09-06T22:07:19.569Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','SYN','KLN','MON','TAD','HRN','BQT','LEW','LAT','BRT','PHD','SKT','WLD','IEC','SOD','FSD','WEB','LKT','PLA','AFM','FVQ','NYB','HUB','ARY','DEV','PHN','AFA']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\"",
 "description": "Dump refs_online metadata"
}
```


### [2026-09-06T22:07:21.376Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
```


## [2026-09-06T22:07:26.859Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','SYN','MON','TAD']:\n    v=d[k]; print(k, '|', v.get('page_offset'), '|', str(v.get('lookup_hint'))[:400]); print()\n\"",
 "description": "Show page offsets"
}
```


## [2026-09-06T22:07:27.063Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60",
 "description": "List refs dir"
}
```


### [2026-09-06T22:07:28.848Z] TOOL RESULT

```
POK | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d

AHD | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.

KLN | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

SYN | leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.

MON | None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab

TAD | 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
```


### [2026-09-06T22:07:28.882Z] TOOL RESULT

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
```


## [2026-09-06T22:07:32.804Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 63[0-9]\" POK_full.txt | head -20; echo ====; grep -n \"Page(s): 64[0-2]\" POK_full.txt | head -20",
 "description": "Find Pokorny pages 630 and 640"
}
```


### [2026-09-06T22:07:32.848Z] TOOL RESULT

```
Exit code 1
47303:Page(s): 634 
49029:Page(s): 630 
49049:Page(s): 630 
49071:Page(s): 630 
49109:Page(s): 631 
49136:Page(s): 632 
49155:Page(s): 632 
49183:Page(s): 633 
52187:Page(s): 630 
52197:Page(s): 631 
52227:Page(s): 631-632 
52326:Page(s): 632-633 
52371:Page(s): 635 
52393:Page(s): 635 
52549:Page(s): 636-637 
52578:Page(s): 637-638 
52608:Page(s): 638 
52636:Page(s): 638-639 
52640:Page(s): 636 
52758:Page(s): 639-640 
(eval):1: === not found
```


## [2026-09-06T22:07:33.920Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: k[ʷu]\" POK_full.txt | head -40",
 "description": "Find kw lemmas in Pokorny dump"
}
```


### [2026-09-06T22:07:33.968Z] TOOL RESULT

```
16304:Root/ lemma: bu-\ "lip, kiss' derived from Root/ lemma: ku-, kus-{*k"uk'"h-)\ "to kiss' 
46468:with -t- formant of Root/ lemma: kures-, kuers-, kufs-\ wood, trees. 
48907:Root / lemma: kuku 
48935:Root / lemma: ku-, kus- {*k"'uk"'h-) 
48970:Root / lemma: kuak- 
48989:Root / lemma: kuat(h)- 
49019:Root / lemma: kueiek- or kelak-, kolak- 
49031:Root/ lemma: kuelp-1, kuelb-. kijjp/b-. klup/b- 
49051:Root / lemma: kuelp-2 
49073:Root/ lemma: kuerp-, also kuerb-{* (s)k(u)er-p^ 
49079:Root / lemma: kuerp-, also kuerb- : to turn, wind, derived from a suffixed Root / lemma: 
49111:Root / lemma: kuet- : kuat- : kut- 
49140:Root / lemma: kuoi-, kuT- 
49157:Root / lemma: kures- kuers- kujrs- 
69203:Root/ lemma: puR-2\ "to enclose, put together' derived from Root/ lemma: ku-, kus-
```


## [2026-09-06T22:07:40.417Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=52100 && NR<=52800 && /lemma:|Page\\(s\\)|Meaning/' POK_full.txt | head -80",
 "description": "Pokorny lemmas around pages 630-640"
}
```


### [2026-09-06T22:07:42.067Z] TOOL RESULT

```
Page(s): 628 
Root / lemma: Ruei-2{*R"ehu^ Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to hiss, whistle, etc.. 
Page(s): 628 
Root/ lemma: ^t/eAr- (nasalized Ruenk-) : Ruk-{*R'^ehuk-) 
Meaning: to gape 
Page(s): 629 
Root / lemma: Ruel- {*k''ehul-) 
Meaning: muddy 
Page(s): 629 
Root / lemma: Ruen- {*k"ehu-) 
Meaning: to celebrate; saint 
Page(s): 630 
Root /lemma: RuenA'^-ro-, -no-{*k"ehu6'^-ro^ 
Meaning: a kind of plant 
Page(s): 631 
Root / lemma: Rues- Rus- {*k"'ehus-) 
Meaning: to puff, sigh 
Page(s): 631-632 
Root/ lemma: Ruon-, Run-{*k'^ehun-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: dog (*animal with a strong sense of smell) 
Meaning: dog' 
Page(s): 632-633 
Root / lemma: Rud"^- {*kehud^-) 
Meaning: dirt 
Page(s): 627 
Root / lemma: Ru- {*kehu-) 
Meaning: sharp; pike 
Root/ lemma: Ru-{*kehu-)\ "sharp; pike' derived from zero grade of Root/ lemma: aR-, oR- 
Page(s): 626-627 
Root / lemma: Icalo-s {* Icehu-lo-s) 
Meaning: a kind of big fish 
Page(s): 635 
Root / lemma: Icas-io-, -lo- {* IC'ehus-lo-) 
Meaning: basket-work 
Page(s): 635 
Root/ lemma: k''as-. k^as- {* k'^ehus-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to cough 
Page(s): 649 
Root / lemma: k''ei-1(t){*k''ehu-tj Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to observe; to appreciate 
Page(s): 636-637 
Root / lemma: k''ei-2{*k''ehu-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to pile, stow, gather 
Page(s): 637-638 
Root / lemma: Iceia-, k''lie-{*IC'ehu-es) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to rest quietly, quiet, peaceful 
Page(s): 638 
Root / lemma: IceR-, IcoR-, IceR-s- {* k^ehuR-s-) 
Meaning: to seem, see, show 
Page(s): 638-639 
Root / lemma: k^'e-l {*k''ehu-) 
Page(s): 636 
Root /lemma: k^el-l, k''el9-{*k'^ehulah-) 
Meaning: to turn; wheel; neck? 
Page(s): 639-640 
Root / lemma: lrel-2{*k''ehul-) 
Meaning: far (with regard to place and time) 
Page(s): 640 
Root / lemma: k''el-3{*k''ehul-) 
Meaning: swarm, flock, shoal, school, clan, herd, crowd
```


## [2026-09-06T22:07:53.663Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: Ruen- \\|Ruen-\" POK_full.txt | head; echo ====; sed -n '/Root \\/ lemma: Ruen- {\\*k\"ehu-)/,/^Page(s): 630/p' POK_full.txt | head -60",
 "description": "Print Pokorny kwen entry"
}
```


## [2026-09-06T22:07:54.662Z] TOOL CALL #13: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-290.json'))\nfor e in d['entries']:\n    print(e['root'], e.get('part'))\n\"",
 "description": "Check page 290 roots for Kwel part 1"
}
```


### [2026-09-06T22:07:55.309Z] TOOL RESULT

```
Exit code 1
52169:Root / lemma: Ruen- {*k"ehu-) 
(eval):1: === not found
```


### [2026-09-06T22:07:57.110Z] TOOL RESULT

```
{'name': 'Kweit', 'redirect': 'Kuei'} None
{'name': 'Kwek, Qwek', 'lang': 'Indo-European', 'refs': 'POK:638', 'gloss': 'to appear, see, show'} None
{'name': 'Kwel, Qwel', 'lang': 'Indo-European', 'refs': 'POK:640', 'gloss': 'to move around, dwell'} 1
```


## [2026-09-06T22:08:01.658Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52165,52200p' POK_full.txt",
 "description": "Print Pokorny kwen block"
}
```


### [2026-09-06T22:08:01.705Z] TOOL RESULT

```
Maybe alb. {*Rue/-k) thuk ' mortar ' 
References: WP. I 473. 
Page(s): 629 

Root / lemma: Ruen- {*k"ehu-) 

Meaning: to celebrate; saint 

Material: Avestan spa/7/a-"holy' (= Lithuanian sventas. Old Church Slavic si/^/b "holy'), 

compounds Superl. Avestan span-yah, spanista-^ sacred, holiest ', es^stem Avestan 

spanah-v\. " holiness'; 

probably Gothic hunslu. "sacrifice, oblation'. Old English hus/n. " sacrament' {Run-s-lo- 

); 

Lithuanian si/e/7/a5"holy'. Old Prussian swenta-\'r\ PN, Old Church Slavic sv^th, russ. 
svjatq/6s.; further to Latvian si///7e/"hold festivities, sanctify '. 

References: WP. I 471, Trautmann 311, W. Schuize Kl. Schr. 366. 
Page(s): 630 

Root /lemma: RuenA'^-ro-, -no-{*k"ehu6'^-ro^ 
Meaning: a kind of plant 

Material: Latin combretum^ a kind of rush'; nir. cuinneog^ Angelica silvestris ' (common 
Celtic -ns-, -nt- > -nn-), (Marstrander ZceltPh. 7, 359); based on Ruon&^na= Old Icelandic 
hugnn^ Angelica silvestris ' from Ruon6!^-na, Danish faro. quander6s., Swiss 
Wannebobbeir arum maculatum ', Lithuanian svendraiP\. "a kind of reed, Typhalatifolia '. 
References: WP. I 472, WH. I 253. 
Page(s): 631
```


## [2026-09-06T22:08:02.025Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52700,52790p' POK_full.txt",
 "description": "Print Pokorny kwel block"
}
```


### [2026-09-06T22:08:02.072Z] TOOL RESULT

```
absorber, concave sun-dial (called polos from being shaped like the vault of heaven), on 
which the shadow was cast by the interpreter, head-dress, worn by goddesses ', ttoAeu) 
"go about, range ouer, haunt, revolve, turn up the earth with the plough, plough ', 
aiJcpinoAoq ' maid (Hom.), servant' = Latin anculus^ a man-servant ', ain6Ao(; ' nanny goat 
shepherd ', GeottoAeu) ' minister in things divine ' (besides Geh-koAoc; 'priest'); with k in 
(3ouk6Ao(; " tending kine, worshipper of Dionysos in bull-form, in pi., title of play by 
Cratinus, Osorapi devotee of Sarapis, cattle shepherd ' = Middle Irish buachaill, cymr. 
i&^^a//"herdsman, shepherd' from *k"'o/{/Jos\N\t\r\ labialization after u, 

Maybe alb. ,^5/7^ "herdsman, shepherd' a Celtic loanword. 

ttoAeuu) " turn or go about, the planet presiding ouer a day, turn up the soil with the plough 
' (yf|v " plough up '), Ionian Attic sninoAnq ' on the surface, on the top, uppermost ', spnoAn 
"merchandise, traffic, purchase, gain made by traffic, profit '; nwAsofjai " go up and down 
or to and fro: hence, go or come frequently '; naAiv " of Place, back, backwards, of Time, 
again, once more, in turn ' (Akk. a *TTaAiq ' turn '); kukAo^ see below; the gr. n-forms 
contain probably partly Indo Germanic pe/-see below; 

Latin co/o, -ere^ to till, tend, care for, cultivate ' {*k"eld)\ colonus' a husbandman, tiller 
of the soil ', //7cc»/e/'e "inhabit, to be at home, abide, dwell ', incola^ an inhabitant, resident ', 
inquilTnus^ of foreign birth ', Esquiliae^ the largest of the seven hills of Rome '; about 
anculus " a man-servant ' see above; 

colus, -ust m. or -/"f. "distaff' {*k"elos^ spindle'), collus, -/"m. (Old Latin), collum, -/"n. " 
the neck, the neck (of a flask or bottle), (of the poppy), mountain ridge ' {*k"ol-so-, Gothic 
ha Is); 

Old Irish cur cart ' (Dual. *k^old); Middle Irish coir head' = 

Old Church Slavic kolou.. Gen. /ro/ese "wheel', PI. kola 'cart ' (mixture from k^olo-m. 
and k"eles-v\.)\ 

Icelclo-, k^olclo-il) "wheel' in: 

In a- grade: 

Old Indie cakra-m. n. (pronunciation secondary) " cartwheel, disc, circle ', Avestan 
caxra-m. "wheel'. 

In zero- grade: 



gr. KUKAoq " circle ', PI. kukAoi and kukAq " wheels ' 

In e- grade: 

Old Icelandic hjol, hvel {*k"ek"elon-, Germanic *hweh(w)ula-) n., Old English hweol {ev\Q\. 
wheel), besides hweowol, ^n/eo^o/ (Germanic *hweg{v\/}ula-). Middle Low German wel 
"wheel'; also Frisian fiar\s probably eine dissimilation-form for *hwewla-\ compare also 
Phrygian kIkApiv " big, giant bear ' ('cart '), Lithuanian kaklas, Latvian kokis " neck '; 
Tocharian A kukal, B kokale " cart '. 

Lengthened grade perhaps (as ' twiddled, twisted, rotated, revved, revolved, round ') 
Old Icelandic hva//an6 hollru. (latter from dem Dat. PI. holumiroxw hvalum) 'roundish hill'. 

References: WP. I 514 f., WH. I 45, 245 ff., 250, 846, Trautmann 125. 
Page(s): 639-640 

Root / lemma: lrel-2{*k''ehul-) 

Meaning: far (with regard to place and time) 

Material: 

In a- grade: 

Old Indie carama- ' the last, extreme ', ciras 'chronologically long', gr. naAai ' for a long 

time, since long ago ' (naAai6(; 'old', naAairspoc;, -TaTO(;). 

In e- grade: 

gr. Tf|A£, Aeolic irnAui 'afar, wide' (thAo-Gev, -0i, -as), cymr. corn. bret. peiraiaf {*k"el-s-o- 

?), cymr. pellaFihe extreme'. 

References: WP. I 517. 

Page(s): 640 

Root / lemma: k''el-3{*k''ehul-) 

Meaning: swarm, flock, shoal, school, clan, herd, crowd 

Material: 

In o- grade: 

Old Indie kula-mv\. 'herd, bulk, mass; gender, sex';
```


## [2026-09-06T22:08:15.174Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^kwel-\\|^kwel\\|^kwen-\\|kwel-1\\|kwel-2\" AHD_watkins1985.txt | head -20",
 "description": "Find AHD kwel/kwen roots"
}
```


### [2026-09-06T22:08:15.241Z] TOOL RESULT

```
651:kwelek-
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1295:BIB pd(i)- BIBLIOPOLE pel-5 BIBLIOTHECA dhé-1 BIBULOUS pd(i)- BICAMERAL kamer- BICEPS kaput BICORN ker-1 BICYCLE kwel-1
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1382:COL kwel-1 COLANDER kagh- COLCANNON kaul-, weid- COLD gel-3
1383:COLE kaul- COLEOPTERA kel-2, pet- COLEOPTERAN kel-2 COLEOPTILE kel-2, pet- COLEORHIZA kel-2, wrad- COLESLAW kaul- COLEUS kel-2 COLLABORATE leb-1 COLLAGE koli- COLLAPSE leb-1 COLLAR kwel-1 COLLATE tele- COLLEAGUE leg-1 COLLECT! leg-1 COLLEGIALITY leg-! COLLET kwel-1 COLLIE g(e)u-lo- COLLIER g(e)u-lo- COLLIGATE leig-' COLLIGATIVE |leig-1 COLLO- koli- COLLODION koli- COLLOQUIUM tolkw- COLLOQUY tolkw- COLLUDE leid- COLLUVIUM leu(a)- COLOBOMA kel-1 COLON! | skel-3 COLONEL kel-6 COLONNADE kel-8 COLONY kWel-1 COLOPHON kel-6 COLOR kel-2 -COLoUS kWel-1 COLPITIS kwelp- COLPOSCOPE kwelp- COLPOSCOPY kwelp- COLTER skel-1 CoLuMBA kel-5 COLUMBARIUM kel-5 COLUMBINE kel-5 COLUMN kel-6 COLZA sé-1
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1788:MACERATE mag- MACHICOLATE kWel-1 MACHICOLATION kwel-1 MACHINE magh-1 MACHO mas
2039:PALEO- kwel-2 PALETTE pag- PALFREY pert, reidh-
2040:PALIMPSEST bhes-1, kwel-1 PALINDROME der-1, kwel-1
2041:PALINGENESIS kwel-1 PALINODE kvel-1 PALISADE pag- PALLID pel-2 PALL-MALL bhel-2, mele- PALLOR pel-2 PALM! pele-2 PALM? pele-2 PALOMINO pel-2 PALP pol- PALPABLE pol- PALPATE! pdl- PALPEBRAL pol- PALPITATE pdl- PALSGRAVE gravo- PALUDAL pele-!
2112:POINT peuk- POINT-DEVICE weidh- POINTILLISM peuk- POISE! (s)pen- POISON pO(i)- POKE’ beu-1 PoLack pele-2 POLE! kwel-1
2125:POST- apo- POSTBELLUM duellum POSTERIOR apo- POSTICHE apo- POSTMERIDIAN deiw- POST-MORTEM apo-, mer-2 POSTPARTUM _pere-1 POSTSCRIPT skribh- POSTULATE prek- POSTURE apo- POTABLE p0(i)- POTATION pd(i)- POTATORY pd(i)- POTENT poti- POTION po(i)- POTPOURRI pu-2 POUCH beu-! POULARD pau- POULTICE pel-1 POUNCE! peuk- POUNCE? (s)poi-mo- POUNCE3 peuk- POUND! (s)pen- POUNDS bend- POUSETTE pel-6 POUT beu-! POVERTY pau- POWDER pel-1 POWER poti- PRAAM per! PRACTICAL prak- PRACTICE prak- PRAEDIAL wadh-1 PRAEMUNIRE mei-3 PRAENOMEN no-men- PRAETOR ei-1 PRAGMATIC prak- PRAISE per-6 PRANDIAL ed- PRATINCOLE kwel-1 PRAXIS prak-
2140:Puc’ ped-1 PUGILISM peuk- PUGIL STICK peuk- PUGNACIOUS peuk- PUISNE apo-, gene- PUKKA pekw- PULICIDE plou- PULLET pau- PULLEY kwel-1 PULMONARY pleu- PULSATE pel-6 PULSE! pel-6 PULSE? pel-1 PULVERIZE pel-1 PUMICE (s)poi-mo- PUMPKIN pekw- PUNCH? penk¥e PUNCHEON! peuk- PUNCTUATE peuk- PUNCTURE peuk- PUNGENT peuk- PUNISH kWej-1 PUNITORY kvei-1 PUNKA peg- PUNT! pent-
2349:TEAR? dakru- TECHNICAL teks- TECHNOLOGY teks- TECTONIC teks- TECTRIX (s)teg- TECTUM (s)teg- TEEM! deuk- TEEN? deu-3 TEETER der-1 TEETOTUM teuta- TEGMEN (s)teg- TEGMENTUM (s)teg- TEGULAR (s)teg- TEGUMENT (s)teg- TEIGLACH dheigh- 'TELAMON tele- TELANGIECTASIA ten- TELE- kwel-2 TELEKINESIS kei-3 TELEOLOGY kWel-1 TELEOST kWel-1, ost- TELESCOPE spek- TELEUTOSPORE kwel-1 TELIC kwel-1 TELIUM kwel-1 TELL del-2 TELLURIAN tel- TELLURIC tel- TELLURION tel- TELLURIUM tel- TELLURO- tel- TELO- kwel-1 TELPHER bher-1 TEMERARIOUS teme- TEMERITY teme- TEMPLE! tem- TEMPLE? temp- TEMPLES tem-
```


## [2026-09-06T22:08:27.281Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"kwel-1\\..\\{0,3200\\}\" AHD_watkins1985.txt | head -3",
 "description": "Print AHD kwel-1 entry"
}
```


### [2026-09-06T22:08:29.202Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:08:31.615Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kwel-1\\|kwel-2\\|kvel-1\\|kWel-1\" AHD_watkins1985.txt | cut -c1-8 | head -20",
 "description": "Locate AHD kwel entry lines"
}
```


### [2026-09-06T22:08:31.665Z] TOOL RESULT

```
650:kwed
1208:ABA
1242:ANA
1295:BIB
1324:BRI
1357:CHO
1382:COL
1383:COL
1402:CUB
1406:cUs
1416:DEC
1456:ENA
1462:ENT
1579:HAG
1679:INN
1788:MAC
2039:PAL
2040:PAL
2041:PAL
2112:PO
```


## [2026-09-06T22:08:34.233Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('kwel-1')\nprint(t[i-200:i+4200])\nEOF",
 "description": "Print AHD kwel-1 full entry"
}
```


### [2026-09-06T22:08:36.019Z] TOOL RESULT

```
dh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
ACHE ag-es- ACHENE ghai- ACHERON eghero- ACHOLIA ghel-2 ACHROMATIC ghréu- ACICULA ak- ACID ak-
ACLINIC LINE klei- ACME ak-
ACNE ak-
ACORN 6g- ACOUSTIC keu-1 ACQUAINT gnd- ACQUIESCE kWeje-2 ACQUIRE quaerere ACRE agro- ACRID ak- ACRIMONY ak- ACRO- ak- ACROBAT ak-, g¥a- ACROMEGALY meg- ACROMELIC mel-3 ACROMION ak-, omeso- ACROPOLIS pele-3 ACROSPIRE ak-, spel- ACROSTIC  steigh- ACT ag-
ACTINO- nekw-t- ACUITY ak- ACUMEN = ak- ACUTE ak-
AD- ad-
-AD ad-
ADAGE 6@g- ADAMANT deme-2 ADD d6-
ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
AGIO al-1 AGITATE ag- AGLET ak- AGMINATE ag- AGNAIL angh- AGNATE gene- AGNI egni- _ AGNOMEN no-men- AGNOSIA gnd- AGO ghé- -AGOGUE ag- AGONY ag- AGORA! ger-1 AGORAPHOBIA ger-! AGRAFFE ger-2 AGRAPHA gerbh- AGRAPHIA gerbh- AGRARIAN agro- AGREE gWere-3 AGRESTAL agro- AGRIA agro- AGRICULTURE agfo- AGRIOECOLOGY agro- AGRIOLOGY agro- AGROSTOLOGY agro- AHIMSA ghei-i, ne AHRIMAN men-1
AnuRA MazpDa_ansu-, men-1
AID ad-
AIL agh-! AIOLI elaia AIR wer-2 AIRPLANE pelo-2 AISLE aks- AITCHBONE not-
81
ALA aks-
ALAR aks- ALARM al-1, ar- ALARY aks-
ALAS 16-2 ALASTOR [adh- ALATE aks-
ALB albho- ALBEDO albho- ALBESCENT albho- ALBINO albho- ALBITE albho- ALBUM albho- ALBUMEN albho- ALBURNUM _albho- ALDER el-2 ALDERMAN al-3 ALE alu-
ALERT al-1 ALEURONE al-4 ALEXIA feg-1 ALEXIPHARMIC alek- ALGOLAGNIA  slég- ALIAS al-1 “ ALIBI al-1, kWo- ALIBLE al-3 ALIEN al-1 ALIFORM_ aks- ALIKE fik- ALIMENT al-3 ALIMONY al-3 ALIPHATIC leip- ALIQUOT al-1, kwo- ALL al-5
ALLEGE ag-, leg-1 ALLEGORY al-!, ger-1 ALLELOMORPH al-1 ALLERGY werg- ALLEVIATE legh- ALLEY! al-2 ALLIGATOR al-1 ALLITERATE deph- ALLITERATION deph- ALLO- al-1 ALLOCUTION tolkw- ALLOMERISM (s)mer-2 ALLOPATRIC  peter- ALLOT kleu-3 ALLOY leig-1 ALLUDE |leid- ALLUVION leu(e)-
ALOFT an!, leup- ALONE oi-no- ALONG §ant- ALOPECIA wip-é- ALPENHORN ker-1 ALPENSTOCK (s)teu- ALPHOSIS albho- ALSO al-5
ALT al-3
ALTER al-1 ALTERCATE al-1 ALTERNATE al-1 ALTHEA al-3 ALTHORN  ker-1 ALTIMETER al-3 ALTITUDE al-3 ALTO al-3 ALTOCUMULUS _al-3 ALTOSTRATUS _al-3 ALTRICIAL al-3 ALTRUISM al-1 ALULA aks- ALUMNUS al-3 ALVEOLUS aulo- ALWAYS wegh- ALYSSUM wikwo- AM es-
AMAH amma AMANUENSIS man-2 AMARANTH mer-2 AMARELLE om- AMARETTO om- AMASS mag- AMATEUR amma
AMATIVE
AMATIVE amma AMATORY amma AMAZON magh-2 AMBAGE ag- AMBASSADOR ag- AMBERGRIS gher-3 AMBI- ambhi AMBIDEXTROUS deks- AMBIENT ei-1 AMBIGUOUS ag- AMBITION ei-1
AMBLYGONITE genu-1, mel-1
AMBLYOPIA mel-1 AMBROSIA mer-2 AMBSACE ambho AMBULATE al-2 AMBUSCADE busk- AMBUSH busk- AMELIORATE mel-4 AMENABLE men-2 AMEND mend- AMENORRHEA mé-2 AMENT! = ap-1 AMENT2
```


## [2026-09-06T22:08:41.091Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '645,651p' AHD_watkins1985.txt | cut -c1-6000",
 "description": "Print AHD lines 645-651"
}
```


### [2026-09-06T22:08:41.136Z] TOOL RESULT

```
kret-2. To beat. O-grade form *krot- in Greek krotein, to strike, beat: DICROTISM, TRICROTIC. [Pok. 2. kret- 621.] kreue='. Raw flesh. 1. Lengthened-grade form *kréw- in Germanic *hréwaz in Old English hréaw, raw: RAW. 2. Suffixed form *krewo-s- in Greek kreas, flesh: CRE- ATINE, CREODONT, CREOSOTE, PANCREAS. 3. Suffixed zero-grade form *krii-do- (< *krua-do-) in: a. Latin cridus, bloody, raw: CRUDE; ECRU, RECRUDESCE; b. Lat- in cridélis, cruel: CRUEL. [Pok. 1. A. kreu- 621.]
kreue-2. To push, strike. 1. Germanic *hrewwan in Old
kreup-
English hréowan, to distress, grieve: RUE!, RUTH. 2. Ex- tended o-grade form *krous- in Greek krouein, to strike: ANACRUSIS. [Pok. 3. kreu- 622.] kreup-. Scab; to become encrusted. 1. Germanic *hrub- in: a. Middle Low German ruffelen, to crumple, akin to the Germanic source of Middle English ruffelen, to ruffle, roughen: RUFFLE}; b. Germanic compound *ga-hrub- (*ga-, intensive prefix; see kom) in Middle Dutch grof, harsh: GRuFF. 2. Suffixed o-grade form *kroup-d in Serbo-Croatian krupa, groats (perhaps > German Graupe, barley): GRAUPEL. [Pok. kreup- 623.] kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in: a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN, CRUSTACEOUS, CRUS- TOSE; b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.] kreut-. Also kreudh-. Reed. Germanic *hreuda- in Old English hréod, reed: REED. [Pok. kreut- 623.] kropo-. Roof. Germanic *hréfam in Old English hrdf, roof: ROOF. [Pok. krdpo- 616.] krut-. Musical instrument. 1. Germanic *Arut- in Old French rote, a stringed instrument: ROTE3, 2. Geminated form *krutté in Welsh crwth, an ancient Celtic instru- ment: CROwD?. [Pok. krut- 624.] ksero-. Dry. 1. Lengthened-grade form *kséro- in Greek xéros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHAL- MIA. 2. Perhaps suffixed variant form “kseres-no- in Latin serénus, serene, bright, clear: SERENE. [Pok. ksero- 625.] ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: syN-. 2. Russian so-, s-, with, in sputnik, fellow traveler (see pent-): SPUTNIK. [In Pok. 2. sem- 902.] ku-. Hypothetical base of a variety of conceivably related Germanic words meaning “a hollow space or place, enclosing object, round object, lump,” and some other derivative denotations. 1. Germanic *kubdn-, hut, shed, room, in: a. Old English cofa, bedchamber, closet: COVE!; b. Middle Dutch cubbe, “pen, stall,” fish basket, akin to the probable source of CUBBY; C. Germanic compound *kubawald-, probably “house ruler,” household god (wald-, power; see wal-), in Middle High German kobolt, an underground goblin: COBALT, KOBOLD. 2. Germanic *kutam in Old English cot, cottage: COT?, (COTTAGE). 3. Germanic *kutdn- in Old English cote, shelter: CoTE!. 4. Germanic *k(e)ud- in: a. Old English codd, bag, husk: cop?; b. Old English cudele, cuttlefish (from its ink bag): CUTTLE. 5. Germanic k(e)ut- in Old English *cieter, intestines (probably > Middle English chiterling): cx1T- TERLINGS. 6. Germanic *kukk- in Middle English cok, haycock, pile of straw: cock?. 7. Germanic *kuk- in Old English cicen, chicken: CHICKEN. 8. Germanic *kugg- in Swedish kugge, cog, akin to the possible Scandinavian source of Middle English cogge, cog: coc}. 9. Germanic *kuggila in Old English cycgel, rod, cudgel: CUDGEL. 10. Germanic *keulaz in: a. Low German kielswin, keel- son: KEELSON; b. Middle Dutch iel, ship, keel of a ship: KEEL?, 11. Germanic *kijp- in Middle Dutch kipe, cask, tub, basket: COOPER. 12. Germanic *kunt- in Middle Low German kunte, vulva, akin to the Low German source of Middle English cunte, vulva: CUNT. 13. Germanic kird- in Icelandic kiird, to crouch, lie in wait, akin to the Scandinavian source of Middle English couren, to cower: COWER. 14. Possibly Old Norse kiiga, to oppress, akin to the probable source of cow?. [In Pok. géu- 393.] kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: Kiss. [Pok. ku-, kus- 626.] kwat-. To ferment, be sour. Possible root. Suffixed vari- ant form *kwét-so- in Common Slavic *kvasi in Russian kvas, kvass: Kvass. [Pok. kuat(h)- 627.] kwe, And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]
k“el-2
kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
kwelek-
```


## [2026-09-06T22:08:56.419Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN housel ===\"; grep -n \"^housel\\|housel,\" KLN_1966.txt | head -5; echo \"=== KLN absinth ===\"; grep -n \"^absinth\\|absinthe,\" KLN_1966.txt | head -5; echo \"=== KLN clown ===\"; grep -n \"^clown\" KLN_1966.txt | head -5; echo \"=== KLN talisman ===\"; grep -n \"^talisman\" KLN_1966.txt | head -5; echo \"=== KLN calash/caleche ===\"; grep -n \"^calash\\|^caleche\\|^calèche\" KLN_1966.txt | head -5",
 "description": "Grep Klein headwords"
}
```


### [2026-09-06T22:08:56.534Z] TOOL RESULT

```
=== KLN housel ===
18149:Derivatives:  hour-ly,  adj.  and  adv. houri,  n.,  a  nymph  of  the  Moslem  Paradise;  (fig.) a  seductive  woman.  —  F.,  fr.  Pers.  hurt,  fr. Arab,  hur,  pi.  of  ahwar,  fern,  haurd ’,  ‘having beautiful  black  eyes’,  fr.  fiawira,  ‘had  black eyes’,  which  is  rel.  to  Heb.  hawar,  Aram.-Syr. hdwdr,  ‘was  white’,  Heb.  hur,  ‘white  stuff’,  hori, ‘white  bread’.  The  -i  in  Pers.  hurt  is  a  formative element  serving  to  denote  the  singular, house,  n.  —  ME.  hus,  hous,  fr.  OE.  hits,  rel.  to OS.,  ON.,  OFris.,  OHG.  MHG,  Ads,  Du.Au/s,G. Haus,  Goth.  -Aur(in  the  compound^MdAnj.'temp- le\  lit.  ‘the  house  of  God’);  orig.  ‘shelter’,  fr. I.-E.  *qeus-,  -s-enlargement  of  base  *qeu-,  ‘to cover,  hide’.  See  hide,  v.  and  cp.  hoard,  hose, hut.  Cp.  also  husk,  the  first  element  in  husband, husting  and  the  second  element  in  caboose, house,  tr.  and  intr.  v.  —  OE.  husian,  ‘to  take  into a  house’,  fr.  hus,  ‘house’.  See  house,  n. housecarl,  n.,  member  of  the  bodyguard  of  a Danish  or  early  English  king  or  nobleman (hist.)  —  OE.  huscarl,  fr.  ON.  huskarl,  which  is compounded  of  ON.  hus,  ‘house’,  and  karl, ‘man’.  See  house  and  churl, housel,  n.,  the  Eucharist  (obsol.)  —  ME.  husel, fr.  OE.  husel,  ‘the  Eucharist’,  rel.  to  ON.  husl, of  s.m.,  Goth,  hunsl,  ‘sacrifice’,  and  prob.  cogn. with  Lith.  svehtas.  OSlav.  svetu,  OPruss.  swints, ‘holy’,  Lett,  svinet,  ‘to  hallow,  celebrate’, Avestic  splnta-,  ‘holy’.
18150:housel,  tr.  v.,  to  administer  the  Eucharist  to.  — ME.  huslen,  fr.  OE.  huslian,  fr.  husel,  ‘the Eucharist’.  Cp.  ON.  hiisla,  ‘to  administer  the Eucharist’,  Goth,  hunsljan,  ‘to  sacrifice’,  which also  are  denominatives,  and  see  housel,  n. housewife,  n.  —  ME.  houswif  fr.  hous,  ‘house’,
=== KLN absinth ===
1241:absent,  tr.  v.,  to  keep  (oneself)  away.  —  F.  ab- senter,  fr.  L.  absentare,  ‘to  cause  one  to  be  ab¬ sent’,  fr.  absens,  gen.  absentis.  See  absent,  adj. absinth,  absinthe,  n.,  wormwood.  —  F.  absinthe, fr.  Gk.  d<|av(hov,  ‘wormwood’,  which  is  of OPers.  origin;  cp.  ModPers.  aspand,  sipartd, of  s.m.
=== KLN clown ===
=== KLN talisman ===
38052:talisman,  n.,  amulet;  charm.  —  F.  talisman,  fr. Sp.  talisman,  fr.  VArab.  tilsaman,  pi.  of  tilsam, which  corresponds  to  Classical  Arabic  tllasm,  a loan  word  fr.  Late  Gk.  T^XeojjLa,  ‘consecration, mystery’,  fr.  Gk.  TeXenpia,  ‘payment’,  fr.  teXeiv, ‘to  fulfil,  perform;  to  pay;  to  initiate  into  mys¬ teries’,  fr.  t£Xo;,  ‘fulfilment,  end’.  See  tele-. Derivatives:  talisman-ic,  talisman-ic-al,  adjs., talisman-ic-al-ly,  adv.
=== KLN calash/caleche ===
6134:calash,  n.,  a  kind  of  carriage.  —  F.  caleche,  fr. Czech  kolesa,  ‘wheels,  carriage’,  pi.  of  koleso, ‘wheel’,  fr.  kolo,  ‘wheel’,  which  is  rel.  to  OPruss. kelan,  ‘wheel’,  and  cogn.  with  Gk.  xuxXo;, ‘circle’,  OE.  hweogol,  hweol,  ‘wheel’.  See  wheel and  cp.  words  there  referred  to.
```


## [2026-09-06T22:09:12.346Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in طلسم کالسکه افسنتین اسپند گوسفند; do echo \"=== $w MON_part1\"; grep -c \"$w\" MON_part1.txt; echo \"=== $w MON_part2\"; grep -c \"$w\" MON_part2.txt; done",
 "description": "Count Persian words in Mo'in OCR"
}
```


## [2026-09-06T22:09:13.153Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 210 leaf 231 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==232' HRN.txt | head -60",
 "description": "Print Horn p.210"
}
```


### [2026-09-06T22:09:14.093Z] TOOL RESULT

```
=== طلسم MON_part1
6
=== طلسم MON_part2
4
=== کالسکه MON_part1
2
=== کالسکه MON_part2
4
=== افسنتین MON_part1
0
=== افسنتین MON_part2
0
=== اسپند MON_part1
9
=== اسپند MON_part2
1
=== گوسفند MON_part1
89
=== گوسفند MON_part2
85
```


### [2026-09-06T22:09:15.967Z] TOOL RESULT

```
=== HRN 210 leaf 231 ===
— 210 —
gör 'Grab*, dagegen, das Geiger neuerdings (Lautl.
des Bai. 53) mit ai. ghörd- grausig, furchtbar ver-
glichen hat, ist nach Nöldeke, Pers. Stud. II, 41 ein
semitisches Lehnwort. Beiläufig bemerkt, ist türk. LW.
g*aur wohl nicht arab. kaßr (Hübschmann unter oss.
d. gaur, t. daur, S. 123), sondern vielmehr neupers.
gebr, gahr^) (vergl. Geiger, bei. LW. gaur, No. 81,
wo allerdings phlv. gabrä (semitisch!, nur *Mann
bedeutend) nicht als Grundform stehen durfte).
939. guvälfden, gevaltden (falsch k"*) wachsen* (unbelegt);
vergl. bällden (No. 173).
ai. vi + {/^vardh- ^heranwachsen, gedeihen ; ist schon
im PehlevT verschwunden.
940. guvah, guva *Zeuge'.
ai. vi + \/^ka^- Intens, ausschauen, erschauen, wahr-
nehmen'; phlv. gukäs 'Zeuge', gtikasih (M^n.), arm. LW.
vkay *Zeuge', vkayem 'ich bezeuge* 2).
941. gösäle 'Kalb'.
ai. vatsd' 'Kalb, Jährling*.
käfir. vatsala, si^n. botsöri 'Jährling' (Tomaschek,
S. 765).
Das ö in gösäle stammt von go 'Kuh' (No. 888).
942. göspendj gösfend 'Kleinvieh, Schaaf, Widder, Ziege'.
aw. gaospenta- (vd. 21, 1); phlv. göspaud.
943. gas 'Ohr*.
ap. gausa- 'Ohr'; aw. gaosa- 'Ohr*; phlv. gös; ai.
ghoSa- 'Lärm, Getön .
kurd. güh; afy. yvay; oss. d. yos, t. qüs (94); bei.
gös (125); wa/. yws, yis etc.
np. gösvär^ ^öst^äre 'Ohrgehänge*: aw. frä.[gaosävara-,
mat,[gaosävare; phlv. gösvär,
944. gast 'Fleisch*.
aw. gäv, Nom. gän§ 'Fleisch' ; phlv. göst^ göstm (GFr.).
LW. afy. yva/a 'Fleisch'; kurd. güst; bei. gö$t, n.
göM (128); wa/. gust, minj. yös, sar. gü^t, siyn. goß,
^) Zuerst hat dies wohl Bückert, ZDMG. 10, 183 ausgesprochen.
«) Vergl. Fr. Müller, WZKM. 5, 263.
```


## [2026-09-06T22:09:24.392Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"طلسم\" MON_part1.txt | head -8 | cut -c1-400; echo \"==== KALESKEH\"; grep -n \"کالسکه\" MON_part1.txt MON_part2.txt | head -8 | cut -c1-400",
 "description": "Grep Mo'in for telesm and kaleskeh"
}
```


### [2026-09-06T22:09:24.466Z] TOOL RESULT

```
29379:گویند که در آن اسما و طلسمات و تعویذ 
40797:ویب نام طلسمی است. علم تشت و 
43746:طلسمی که برای دفع چشم زخم به گردن 
92984:سر دفاین و خزاین تعبیه کنند» ج. طلسمات» 
92985:طلاسم. طلسم مزعفر: تعویذی که به زعفران 
92986:نویسند. طلسم کسی‌یا چیزی شکستن: (عم.) 
==== KALESKEH
MON_part2.txt:19265:کالسکه 
MON_part2.txt:19280:کالسکه: (0-)۲۵:ع۱2۱ (ا.) گر دونه‌ای مرکب 
MON_part2.txt:19282:مسافران نشینند) و جای کالسکه‌چی و چند 
MON_part2.txt:19284:باز: کالسکه‌ای که سقف ندارد با سقف آن 
MON_part1.txt:32075:که بر دیوار با کرسی و تخت و کالسکه و 
MON_part1.txt:95392:کالسکه.
```


## [2026-09-06T22:09:25.477Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));v=d['BQT'];print(v.get('page_offset'));print(v.get('lookup_hint'))\"",
 "description": "BQT page offsets"
}
```


### [2026-09-06T22:09:27.332Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-06T22:09:36.372Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- kaleskeh ---\"; sed -n '19276,19288p' MON_part2.txt; echo \"--- telesm ---\"; sed -n '92978,92992p' MON_part1.txt",
 "description": "Print Mo'in contexts"
}
```


### [2026-09-06T22:09:36.438Z] TOOL RESULT

```
--- kaleskeh ---
بزرگ: واحد مقیاس برای حرارت و آن 
مقدار گرمایی است که یک لیتر آب را یک 
درجه گرم کند. 

کالسکه: (0-)۲۵:ع۱2۱ (ا.) گر دونه‌ای مرکب 
از یک اطلاق چهار چرخه (که در داخل آن 
مسافران نشینند) و جای کالسکه‌چی و چند 
اسب (که اطاق را حمل کنند.) کالسکةً سر 
باز: کالسکه‌ای که سقف ندارد با سقف آن 
را بر داشته باشند. 

کالفتن: 2۱0۲12۰ (مصل.) آشفته شدن» 
پریشان حال گشتن. شیدا شدن» دیوانه گشتن. 
--- telesm ---
: صععاع) [ع. معر.] (.) عمل خارق 
عادت که مبداً آن را قوای فعال آسمانی و 
قوای منفعلةٌ زمینی دانند و بدان آمور عجیب 
و غریب پدید آورند. نوشته‌ای شامل اشکال 
و ادعیه که به توسط آن عملی خارق عادت 
انجام دهند. شکل و صورتی عجیب که بر 
سر دفاین و خزاین تعبیه کنند» ج. طلسمات» 
طلاسم. طلسم مزعفر: تعویذی که به زعفران 
نویسند. طلسم کسی‌یا چیزی شکستن: (عم.) 
کره از کار وی باز شدن. 
طلعت؛: :ها [ع. طلعه ] (مسصم.) دیدن» 
ریت کردن. (امص.) ریت. () روی» 
وجه. طلوع» بر آمدن (ستاره). 
طلق: بدا (معر. تلک] (ا.) (زه.) سنگی 
است معدنی که از گروه مسجاور میکا و از
```


## [2026-09-06T22:09:44.849Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اسفند\\b\" BQT_v1_pages.txt | head -20 | cut -c1-200; echo \"=== leaf tags\"; grep -n \"اسپند\" BQT_v1_pages.txt | head -20 | cut -c1-200",
 "description": "Grep Borhan vol1 for esfand/espand"
}
```


### [2026-09-06T22:09:44.918Z] TOOL RESULT

```
567:۷-سخنر | نی استادبنو نیست در اسفندم ۳۷۲ ۱در « 1 نستیتوی‌فر | نسه وایر آن > تهر ان.
837:- [سمان؛ مر سبند << مار اسفنده "اونرغ <انیر ان ۴
3388:میگویند که درزمان بهمن اسفندبارچون مردم ازاطراف عالم بدر گاء اومیآمدند وزبان یسکدیگررا
3513:خبانیدن )» هر ( ذیل : وغیدا ) ۰ هزار اسفند ( ذیل: صندل دانه )» هلل
8383:بی ۲ اه کردند از آن کارزار پی شاه را » فرخ اسفندبار. فردوسی ۶ لفت نامه *.
10418:محبوس داشت عافبت اسفندبارین کشتاسب روئه
10471:از ۵ شیر - نام بهمن بن‌اسفندبار پدرداراب
11016:نام سثار؛ مشتری است - و نام پسر اسفندیار
11615:قظرسی نیز اسفند . 18۱98 112۲۳0812 این گیاء در اغل نفاط ابران خود روست . «فرهنگه
11632:ذال نقطه دار. بروزن ومعنی اسفندارمن است که
11650:که در ماه و روز اسفندار وافع مشود بدو علق
11663:سفندارهت ۰ اسفندارمث و کاه سَخفف صیند ار واسفنه ۰ باب از دوحزه : میند که صقت است
11670:زمین با اوست . سروای لام بنجمین روز ماه را در فپرست روز های ابرانی « اسفندارمد * و در
12175:اسفند اسشید یک اول وفای دوم»
12178:اسفند مد - نم میم ۴
12181:اسفندیاره بر وزن و معنی آ-نددار
12184:هت ورب ماه امفندار و رب روز اسفندار
14867:اسفندیار هم هستِ که بسر بهمن باشد .
14871:ات تلم بسرزاده اسفندبار
15374:«رهارلهه۲۱۷ و روز اول پنجهةٌ دزدیده را بنام این کاتها خوانده‌اند . رك . اشتود واسفندمن .
=== leaf tags
11669:مزداست و ماتند دیگر امشاسپندان واسطةٌ آفربد گار و آفرید گانست و در جهان خاکی نگهبانی
13796:علامت‌تفی و11966[(8 از ربشة 1512۴ (مردن), جزه دوم سپنته (اسپند) بمعنی مقدس, جمعاً بمنی
15619:ستابش » و بفرشتگانی اطلاق مبشد که از جهت رتبه و منزات دون‌امشاسپندان حستند . این واژه
```


## [2026-09-06T22:09:58.393Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf boundaries\nleaf=0; out={}\nfor i,l in enumerate(lines,1):\n    if '\\f' in l: leaf+=l.count('\\f')\n    out[i]=leaf\nfor n in (11615,11632,13796,12175,14867):\n    print(n, 'leaf',out[n])\n# print pdf page tags near\nfor n in (11615,13796):\n    seg='\\n'.join(lines[n-40:n+5])\n    m=re.findall(r'\\[pdf page \\d+\\]',seg)\n    print(n,m[:5])\nEOF",
 "description": "Map Borhan lines to leaves"
}
```


### [2026-09-06T22:10:00.114Z] TOOL RESULT

```
11615 leaf 332
11632 leaf 335
13796 leaf 379
12175 leaf 347
14867 leaf 401
11615 []
13796 []
```


## [2026-09-06T22:10:05.664Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==333' BQT_v1_pages.txt | head -60",
 "description": "Print Borhan leaf 332"
}
```


### [2026-09-06T22:10:07.511Z] TOOL RESULT

```
قطونا باشد ۷ » و معنی ت رکیبی آن گوش اسب ۱
است ۰ چه غول بدمنی کوش هم آعده است ؛
وجط یکونند چون ب رکه آن بگوش اسب‌شبه
و معنی اسفناج است »
و آن سبزی باش د که در
آش و هله کنند , سرفه
است‌بنابرین اسب‌غول خوانند و بضی بشپش‌تشبیه | دا نافع ات (,
کرده اند , و جتح اول هم درست است . اسینانج .
باجیم مر وزن اصفهانك »
بمعنی اسفناح ننک 5
سبزی آش باشد ۴ . اسیناخ ( اسپناج )
ا سید ه معروفاست و (۲) آن دانه‌ای
باشد که بجپت چشم زخم در آش ریزند ۵ .
اسیندار بمعنی شمح باشد که معشوق
اسیلفج « بنتم اول و م لام و سکون ‏
ثانی و ثالث و نون و جیم ۴ کیاهی است (۱)
دوابی که آنرا صفاهان شنك و در خراسان‌رش
یزخال دار و بعرمی لحیةالنیس خوانند . طبیعت
آن سرد و خشك است » خون بینی و جمم‌اعضا
ببندد و ربهای کهنه را نافم باشد و فرحه
اععارا سود دارد » و آذناب‌النیل همان است . 4
پروانه است - و نام پکشناسب هم هست ٩‏
اسناخ ۴ باخای نقطه دار 1 بروزن
-ء بودن لیراعظم باشد دربرج حوت و 5
(۱) چك : - است . (۲) چش : کد.
لِ - جهانگری بمعنی پبخال آورده ۰ دلیلی ندارد چه در قدیم توبن فرهتگها مانند
حلشة قرهنگه اسدی تخجواتی بمعنی بزرقطونا ضبط کر‌ده‌اند واين شمریهرامی را شاهد! وردماند:
هیجگاه نارم بخانه کرد مقام ازانکه خانه پراز اسیغول جانور است .
واسیخول در شمرمذ کور بی‌شك بمعنی ماس است . « لفت‌نامه > -
۴ حکیم مومن وصاحب مخزن‌الادوبه « املنج > آورده اند . « لفت‌نامه » .
؟ - بلت‌علمی 50102012 بانگلی 5۳18260 با 50101286, بفرانسه 60102۲05
با لمانی01024کوعربی اسفاناخ» وفارسی‌اسیناخ»اسیناج» اسینانج,اسپاناج.اسپانج» اسباناج» اسباناخ‌ودد
طبری اسینا «واژه نامه۲۸> حمه‌ازيك ربشه است. داودشرسر انطا کی‌درتذ کرخود گوید : اسفاناج
مرب عن‌فارسية هواسباناح * ۰ دربونانی 5۳1081108 « اختینگاس » وآن از تیر* اسفناجیان ؛
ودارای ربشة قرمز دنگ وب رگهای خوراکی و کلهای نرومادء آن جداست . « کل گلاب4 ۰*۲۷
ی فرحنگه روستایی ۱۸-۱۸۳ > . ۴ راد : اسیناج ۱ ۵ در اوستا ٩۳۵1۵‏
بمعتی مقدس < بارتولمه۱۹۱۹ > ۰ طبری 65۳021 « واژه‌نامه ۷۷ ۰۲ کیلکی ٩۳20-4202‏ ,
قظرسی نیز اسفند . 18۱98 112۲۳0812 این گیاء در اغل نفاط ابران خود روست . «فرهنگه
روستابی۱۸4 * . ۱ ره : اسیندبار. ۷ ر4: امیندارمة .
خبه از صفحة ۱۱4۹
پورداود . بقما ۲ : ۱۲ * پهلوی 25۳25 « اونوالا ۲۸۰ > .
۵ اسبله - با سیلی 212015 51۷0۲135 از ماهیان
استخواندار که بچةٌ ماهیان پربهارا میخورد واز همین نظر ماهی
مسیارمضری‌است وقسمت عمده زند گانیرا در کودالهای‌رودخانه‌ها
سرسبرد ۵ ددیای خزد 64۱۳۳ اسله
( برهان قاطع ۳۰ )
```


## [2026-09-06T22:10:19.160Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"افسنت\\|افسنطین\\|افستین\" BQT_v1_pages.txt | head -10 | cut -c1-200; echo \"=== leaf around 425\"; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (420,425,428,430):\n    print('--- leaf',i,'---')\n    print(t[i][:300])\nEOF",
 "description": "Find afsantin and leaves near p.210"
}
```


### [2026-09-06T22:10:20.786Z] TOOL RESULT

```
=== leaf around 425
--- leaf 420 ---
ایولز
ایو اد « بانانی مجهول بر وزن شیرازه
بمعتی آراسته و بیراسته باشه ۱ .
بسعنی ابواز است که آراسته و پیراسته باشد ۳ .
الوان ه بروز نکوان . صقه و طاق را
بند ۴ ,:
ابوانس بفتح‌اول وسکون ثانی‌وثالث
بالف کشیده و نون مکسود بین بی‌نقطةٌ ده .نام
شهری باشد از فریگگ ؛ و در آن شهر کیسای
است که هر سال در وفت ت
--- leaf 425 ---
ی ۷۰ ‌-
پاخر و بنتحالت وسکون رای‌بی‌هطه
و زای نقطه‌دار , نام فصبهابست در خراسان ونم
کوشه‌نی باشد از چهل و حشت کوش موسیقی .
باخسه - با سین بی‌هطه‌بروزن باغچه.
راهی باشد بفیر از راء ثعارف خانهای که از آن
راه نز آهد و رفت نوان‌کرد - و نثتر حجام را
نیز گوشد .
باخود - بروزن کافور , نلبجد ایراهیم
کگویند س
--- leaf 428 ---
 هریداب‎
باك بره » بنتح بای ابجد و رای‌فرخت.
نام روز یست و دوم )۱( همن حاه باشف. کو بند
عفت سال درابران باد نیامد» درین‌روز شبانی‌پیش
کسری آعد هکفت دوشآ نمقدار باد آمد کهعوی
بروشت کوسفندان بچنبید » پی حد آندوزشاطی
کردند و خوشحالی لمودند. و باین تام شهرت
۳
بایر ۵ - بنتح بای‌فارسی و رای‌قرشت.
ترا چوب 
--- leaf 430 ---
باد وح
که جربی بادروج گویند ؛ د بسی کوبند بادرو
تره‌ایست که بر کش بسپرغم میماند و بوی ترنج
میدهد
پاددوج - بسکون جیم .کل بتان
افروز باشد و بویدن آن عطه آورد وکز دن
عقرب را نافع باشد , و آثرا پعربی ضومردهفرح
القبالمحزون (۱) خوانئد » وبعن ی کوندریحان
کوهی است ٩‏
بادرو ده ت بفتح‌زای نقطه‌دار ۰ بمعتی
هرر
```


## [2026-09-06T22:10:46.142Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(418,442):\n    seg=t[i]\n    hits=[w for w in ('سپند','اسپند','اسفند','گوسفند','مقدس') if w in seg]\n    head=' '.join(seg.split()[:6])\n    print(i, hits, head[:70])\nEOF",
 "description": "Scan Borhan leaves 418-441"
}
```


### [2026-09-06T22:10:47.988Z] TOOL RESULT

```
418 [] ابلا ومردمان و جماعت را نیز
419 [] دنق و نام ییت النفدس هم‌هست
420 [] ایولز ایو اد « بانانی مجهول
421 [] و شش لت و نات بیان
422 [] ۱ بابادشاه دست زدن ۱ متشه
423 [] بت ۷۲۰۳ ح- قلعهٌ آن شهر
424 [] ودریجة کوچك را گوند» وظاهراً ابن
425 [] ی ۷۰ ‌- پاخر و بنتحالت
426 [] نکن مم ینظر آعده است ٩‏
427 [] سب ۰ ۷ -- و او
428 [] هریداب‎ باك بره » بنتح بای
429 [] نت و ۵ ٩‏ حه باددر
430 [] باد وح که جربی بادروج گویند
431 [] است که عوام یازهر کوبند و
432 [] مار از اعمال هرات و اصل
433 [] کوننه بادام پلیله که خاطران بر
434 [] بلدهرزه از طرق مشرق است بجاب
435 [] مج وا باران بر س رگذارند
436 [] با خوانند و آنراکبوتر بیار دوست
437 ['گوسفند'] ۲۱۷ طرز و روش ٩‏ -و
438 [] با ۱ - ۷۱۸ - و
439 [] نشطه‌دار بالف کشیده و یکاف زده
440 [] برداعتن مردم میگیرد . باز داشتی
441 [] اک بار یجه‌رو م ود نگ
```


## [2026-09-06T22:10:55.622Z] TOOL CALL #32: Bash

```json
{
 "command": "ls site/pages/291.jpg 2>/dev/null; pdftoppm -f 291 -l 291 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg291 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 291"
}
```


### [2026-09-06T22:10:58.063Z] TOOL RESULT

```
site/pages/291.jpg
total 117256
drwx------ 3 sfmqrb sfmqrb     4096 Sep  6 18:10 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      682 Sep  6 18:06 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    31044 Sep  6 17:50 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    18004 Sep  6 17:56 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90831 Sep  6 18:04 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
```


## [2026-09-06T22:11:01.655Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg291.png"
}
```


### [2026-09-06T22:11:02.088Z] TOOL RESULT

```

```


## [2026-09-06T22:11:02.086Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:11:15.792Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 291 -l 291 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg291hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg291hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.19*w),int(0.095*h),int(0.50*w),int(0.13*h))).resize((int(0.31*w*2),int(0.035*h*2))).save('p291_root.png')\nim.crop((int(0.60*w),int(0.44*h),int(0.80*w),int(0.50*h))).save('p291_esfand.png')\n\"",
 "description": "Crop root gloss region"
}
```


### [2026-09-06T22:11:19.304Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T22:11:21.357Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p291_root.png"
}
```


### [2026-09-06T22:11:21.436Z] TOOL RESULT

```

```


## [2026-09-06T22:11:21.434Z] INPUT

[Image: original 2108x308, displayed at 2000x292. Multiply coordinates by 1.05 to map to original image.]


## [2026-09-06T22:11:41.255Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 748 (p.724) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==749' SYN.txt | head -50",
 "description": "Print Buck p.724"
}
```


## [2026-09-06T22:11:42.286Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 1500 (p.1476) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1501' SYN.txt | head -60",
 "description": "Print Buck p.1476"
}
```


### [2026-09-06T22:11:42.962Z] TOOL RESULT

```
=== SYN leaf 748 (p.724) ===
 kle’ : ON skorpinn ‘shrunken’, fr. an ex- tension of *(s)ker- ‘twist, turn’. Walde- P. 21.588. Falk-Torp 1032.
ON skridna: skrida ‘creep, crawl’ (10.41).
(OE glidan) ME, NE glide (only rare- ly ‘slide’), MLG gliden (> Dan. glide, Sw. glida), Du. glijden, MHG gliten, NHG gleiten, perh. fr. *ghleidh-, beside *ghlend-, ghladh, etc. in words for ‘shin- ing, smooth’, etc. (through ‘smooth’ to ‘slippery’, cf. OE gled ‘shining, bright, glad’ : OHG glat ‘smooth’, fr. *ghladh-). Walde-P. 1.627. Franck-v. W. 203.
OE slipan, OHG slupfan, MHG sliipfen, NHG schlipfen : Goth. shupan, OHG sliofan ‘slip, creep in’, IE *(s)leub- in Lat. labricus ‘slippery’, ete. Walde-P. 2.710f. Feist 438.
6. Lith. slysti, Lett. slidét, above, 1.
Lith. Gauzti, Giuozti, prob. of imita- tive origin.
7, SCr. klizati se, ete., the Slavic group, above, 1.
8. Skt. srp-, nearest equivalent, but chiefly ‘creep, crawl’ (10.41).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
688 SELECTED INDO-EUROPEAN SYNONYMS 10.48 JUMP, LEAP (vb.)
be Goth. -hlaupan Lith. Sokti ne Sg se ON _ st¢kkva, hlaupa Lett. eke Lat. _ salire Dan.  hoppe, springe ChSI. — skotit? It. saltare Sw. hoppa SCr. — skotitz Fr. sauter OE hléapan, springan Boh.  skotitz Sp. saltar, brincar ME _lepe, springe : Pol. skoczyé Rum. sdrz NE jump, leap, spring Russ. prygnut’, sko&it Ir. lingim Du. springen Skt. skand-, pru- Nir. =‘ léimim, lingim OHG _ springan Av. in W. neidio, llamu MHG springen Br. lammet NHG springen
1. TE *sel- or *sal-. Walde-P. 2.505. Ernout-M. 888 f. REW 7540, 7551.
Grk. aAdopat; Lat. saltre ‘jump’ (> Rum. sdrt), saltare ‘dance’ (> It. sal- lare, Fr. sauter, Sp. saltar ‘jump’), Toch. A sdl- ‘hop, jump’ (SSS 477); perh. Skt. ucchalati (*ud-sal-) ‘rushes up’.
2. Grk. mydaw, NG 775d : Skt. pad- ‘go, fall’, ChSl. pasti ‘fall’ (10.23), fr. the same root as Grk. rots, zodés, Skt. pad-, etc. ‘foot’. Walde-P. 2.23.
3. Lat. salire, etc., above, 1.
Sp. brincar: Cat. vinclar, blincar ‘bend’ (intr.), deriv. of Lat. vinculum ‘chain, bond’. REW 9341.
4. Ir. lingim, vbl. n. léim = W. llam, Br. lamm ‘a leap’ (*Ing-smen), whence NIr. léimim, W. lamu, Br. lammet (-al, -out) : Skt. laghu-, raghu- ‘quick, swift’, Grk. haxts ‘small, little’, TE *leg“h-. Walde-P. 2.426. Pedersen 2.368.
W. neidio: Br. nijal, MCorn. nyge ‘fly’ (10.37).
5. Goth. -Alawpan (only epd. us- hlaupan ‘jump up’), ON hlaupa, OF hléapan, ME lepe, NE leap = OHG hlaufan, NHG laufen ‘run’ (this meaning also in OE and late ON), etym. dub., perh. : Lith. Slubas ‘limping’, slubuoti ‘limp’, IE *flou-b-, extension of *flou- in Skt. crona- ‘lame’, Lith. slumas ‘limp- ing’. Walde-P. 1.473 f. Feist 532f.
ON ségkkva, also ‘burst, spring apart, spurt’ : Goth. stiggan ‘hit, collide with’, OE stincan,
```


### [2026-09-06T22:11:44.670Z] TOOL RESULT

```
=== SYN leaf 1500 (p.1476) ===
, kiiriss, panzier NHG panzer, kirass
Here are included the main words for armor protecting the trunk of the body, regardless of the changing material or form, ranging from the single front plate (as orig. NE breastplate) to the full cors- let or coat-of-mail. A few of the words reflect simply the notion of ‘covering, protection’ and so would be equally ap- plicable to all forms. But more are based upon either the material used or the part of the body protected, especially the breast, but in some cases originally the belly or the neck—such names being unaffected by subsequent changes of material or form.
1. Grk. @&pat (‘corslet? Hom.; only Secondarily the part covered ‘trunk, chest’), perh. : Skt. dharaka- ‘recep-
tacle’ fr. IE *dher- ‘hold’. 1.858. Boisacq 361.
2. Lat. lérica, prob. deriv. of lérum ‘thong, strap’. Walde-H. 1.822. Other- wise, as loanword fr. unknown source, Ernout-M. 562.
OFr. halberz, hausberc (> It. usbergo), hauberc, Fr. haubert (> ME hauberc, haubert), orig. protecting the neck and shoulders, then lengthened to a full coat-of-mail, fr. OHG halsberg, epd. of hals ‘neck’ and berg : bergan ‘cover, pro- tect?. REW 4009. Gamillscheg 510. NED s.v. hauberk.
It. corazza (> Sp. coraza, Fr. cutrasse > Rum. cutrasd), deriv. of Lat. corium ‘leather’. REW 2233. Gamillscheg 284.
Rum. platosd, formed fr. a loanword
Valde-P.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1400 like MHG platte ‘plate-armor’. Tiktin 1184.
3. Ir. lairech, NIr. liireach, W. llurig, fr. Lat. lorica. Wendryes, De hib. voc. 152. Loth, Mots lat. 183.
NI. uchtphlata, transl. of NE breast- plate (ucht ‘breast’, 4.40).
W. dwyfronneg, deriv. of dwyfron ‘breast’ (4.40), after NE breastplate. Also direct loanword brestblad. Parry- Williams 82.
Br. hobregon, fr. Fr. haubergeon, dim. of OF r. hauberc (above, 2).
4, Goth. brunjo, ON brynja (Dan. brynje, Sw. brynja revived), OE byrne, ME brunie, brinie, OHG brunna, MHG briinne (NHG revived), early Gme. loanword fr. Celtic word for ‘breast’, Ir. bruinne, etc. (4.40). Feist 107f. Falk- Torp 110. NED s.v. brinie.
ME bristplate, NE breastplate, orig. single plate for the breast, but actually not so restricted in use.
ME hauberc, fr. (above, 2).
ME curas, NE cuirass, Dan., Sw. kyras, Du. kuras, MHG kiiriss, NHG kiirass, fr. Fr. cuirasse (above, 2).
NE corslet, fr. Fr. corselet, dim. of cors ‘body’. NED s.v.
MHG panzier, NHG panzer (now esp. ‘armored equipment’, as also Du. pantser), MLG panser (> Dan. panser, Sw. parisar), fr. It. panciera ‘belly- armor’, deriv. of pancia, Lat. pantex ‘paunch’. REW 6207. Falk-Torp 813. Weigand-H. 2.366.
Du. borstharnas, lit. ‘breast-armor’ (harnas, 20.32).
OFr. hauberc
d Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
5. Lith. antkritis (neolog. in place of pancerius, fr. NHG panzer), cpd. of ant ‘on’ and kriitis ‘b
```


## [2026-09-06T22:11:53.014Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"10\\.76 WHEEL\\|10\\.76\" SYN.txt | head -5 | cut -c1-200; echo ===; grep -n \"HOLY, SACRED\\|22\\.4[0-9]\" SYN.txt | head -8 | cut -c1-200",
 "description": "Find Buck sections wheel and holy"
}
```


### [2026-09-06T22:11:53.079Z] TOOL RESULT

```
Exit code 1
11183:Russ. kol’co, dim. of kolo ‘circle, whee|’ (obs. or dial.) = ChSl. kolo ‘wheep (10.76). Berneker 548.
16624:M wb.) 10.54 OverTAKE oll pen Gb.) 10.55 Arrive, REACH 10.12 ae AROUND 10.56 APPRoAcH (vb.) 40.18 Wino, WRAP (vb.) 10.57 ENTER 10.14 Ron (7b.) 10.61 Carry (BEaR) 10,15 rairb.) 10.62 Brine re Rus
18303:Lith. ratai, Lett. radi, lit. ‘wheels’, pl. of ratas, rats ‘wheel’ (10.76). Cf. ChSI.
18304:kola (below, 7) and Toch. A kukal, B kokale ‘wagon’ : Skt. cakra-, Gri. Kbndo ‘wheel’ (10.76). ;
18306:Lett. divrici (esp. ‘two-wheeled cart? also rid, Mithl.-Endz. 3.522), opd. of div- for divi ‘two’ and form related to ritents ‘wheel’ (10.76). Likewise diy. ritenis ‘bicycle’ and �
(eval):1: == not found
```


## [2026-09-06T22:11:55.877Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"WHEEL\" SYN.txt | head -15 | cut -c1-150",
 "description": "Find WHEEL section in Buck"
}
```


### [2026-09-06T22:11:55.926Z] TOOL RESULT

```
16624:M wb.) 10.54 OverTAKE oll pen Gb.) 10.55 Arrive, REACH 10.12 ae AROUND 10.56 APPRoAcH (vb.) 40.18 Wino, WRAP (vb.) 10.57 ENTER 10.14 Ron (7b.) 1
18315:10.76 WHEEL Grk. —_zpoxés (xbxdos) Goth. .... Lith. ratas, tekinis ‘ NG —zpoxés, pda ON —hwel, hjal, hvel Lett. rats, ritenis, skritul
```


## [2026-09-06T22:11:58.324Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18315,18345p' SYN.txt | cut -c1-1500",
 "description": "Print Buck 10.76 WHEEL"
}
```


### [2026-09-06T22:11:58.385Z] TOOL RESULT

```
10.76 WHEEL Grk. —_zpoxés (xbxdos) Goth. .... Lith. ratas, tekinis ‘ NG —zpoxés, pda ON —hwel, hjal, hvel Lett. rats, ritenis, skritulis Lat. rota Dan. jul ChSl. kolo It. —ruota Sw.  hjul SCr. kolo, totak, kotat Fr. roue OE hwéol Boh. kolo Sp. rueda ME _hwele, whele Pol. kolo Rum.  roaté NE wheel Russ. koleso Ir. droch, roth Du. wiel Skt. cakra- NIr. roth OHG rad Av. éazra- W. olwyn, rhod MHG rat Br. rod NHG rad
Words for ‘wheel’ include an inherited group derived from a root for ‘turn’ and others from roots meaning ‘run’ or ‘roll’,
1. IE *kvelo-s, *kolo-s, redupl. *keeklo-s, fr. *kvel- in Skt. car- ‘move,
wander’, Grk. wédouat ‘be in motion’, etc. Walde-P. 1.514 ff. Falk-Torp 413. ON hvel; OPruss. kelan; ChSl., SCt.s
Boh. kolo, Pol. koto, Russ. koleso; Grk.
? kixdos ‘ring, circle’, also rarely ‘wheel
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
yoTlON; ai Fakes 93.340, mostly 1 Or
e hjul, OF jg, Hom: a a], Dan., SW. Ms wei ON ad a "wool, ME hwele, i ee el; Skt. cakra-,
u. Wr ipheles * i och. A kukdl, B kokale garrd-s
Ay. & 3 : - in Ir. rethim ‘ago ‘vs, of 1B +reth- 1D. ’
_ (10.46). Walde-P.
7 okt, ralhar, AS Ven. roda = It. ruota.
gr. Stud. 2.77. = : Grk. rpé- | Grk. tpoxés = Ir. droch oe etc. (10.46). Walde-P. 1.874. : 4, Ir. roth, W. rhod, Br. rod, above, 2. Ir. droch, above, 3.
G, Meyer, Neu
COMOTION, TRANS
igitized by Arya Samaj Foundation Chennai and eGangotri
PORTATION, NAVIGATION 725
W. olwyn, etym. dub. Walde-P. 1.301.
5. Lith. ratas, Lett. rats, above, 2.
Lith. tekinis : tekéti ‘run’, (10.46).
Lett. ritenis : ritindt, rietet, rist ‘roll’ (10.15). Miuhl.-Endz. 3.532.
Lett. skritulis : Lith. skritulys ‘circle, knee-pan’, skrylis, OPruss. scritayle ‘fel- loe’, Lith. skriestt ‘make a circle’, OE scribe ‘course’, scrid ‘carriage’, fr. ex- tensions of *sker- in words for ‘turn, bend’. Miuihl.-Endz. 3.894. Walde-P. 2.571.
6. SCr. toéak : tok, ChSl. toki ‘flow’, but through the sense of ‘run’ as in ChSI. teka, testi ‘run, flow’ (10.46).
SCr. kotaé : kotrljati, Russ. katit’, etc. ‘roll’ (10.15). Berneker 591.
7. Skt. cakra-, Av. Caxra-, above, 1.
10.77 AXLE Crk, kay Goths Wer-rr Lith. ais NG atv, &fwvas ON oxull, oxultré Lett. ass Iat. aris Dan. aksel ChSl. ost It. sala, asse Sw. axel SCr. _osovina, os Fr. essteu OE eax Boh. néprava Sp. — eje ME az, azletre, axtre Pol. 0& Rum. osie NE axle Russ. os’ I _ferlas Du. as Skt. akgsa- ie acastdir OHG ahsa Av. ieee Reet MHG ahse T.  ahel NHG achse
. With few exceptions, the words for ee te to an inherited group. =e rive, of IE *aks-, this prob. fr. piwee drive’ in Skt. a7- I, Gere, et ne » ete, (10.65). Walde-P 1.37 Nout-M. 9 “ties & i Walde-H. 1.89. wy Osu; Lat. axis (> It ; . asse, Sp. aan Si (fr. VLat. *axalis), Tr tte »VLat, ae ; OE eaz, ME ax, singl ; beam’), NE dial. HG. a in New England), Du, pn ahse, NHG achse: Moving ct ass; ChSI. ost, SCr.
oh. psa ‘axis’), Pol.
Moulder) Oy Skt. aksq- ( Av. ie Mle-tre NE vag orul-ré (> ME
» Dan, aksel, Sw. azel
```


## [2026-09-06T22:12:05.778Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"SACRED\" SYN.txt | head -10 | cut -c1-200",
 "description": "Find Buck HOLY/SACRED section"
}
```


### [2026-09-06T22:12:05.833Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:12:09.084Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sventas\\|Sventas\\|Svetu\\|svetii\\|spenta\\|spanta\" SYN.txt | head -10 | cut -c1-300",
 "description": "Grep Buck for spenta/sventas"
}
```


### [2026-09-06T22:12:09.132Z] TOOL RESULT

```
18755:avépa is rendered by NIr ni Shuil fear agam, W. nid oes gennyf wr, and Br. nem eus pried ebet ‘there is not a hus- band to me’; so also Lett. man vira nav, Russ. u menja net muza ‘there-is-not a husband to me’. Skt. as- or bha- with the gen. may be ‘have’ or ‘own’, cf. tasya g
```


## [2026-09-06T22:12:13.665Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l SYN.txt && tail -3 SYN.txt | cut -c1-300; echo ===; grep -n \"22\\.4[0-9] \\|HOLY\" SYN.txt | head",
 "description": "Check Buck file extent"
}
```


### [2026-09-06T22:12:13.731Z] TOOL RESULT

```
Exit code 1
35875 SYN.txt
Tr. fiadu, acc. fiadna (Laws, Gloss. 356), Nir. fiadhnéidh; Goth. weitwops (perf. act. pple.), ON viini, Dan. vidne, Sw. vitine, OF gewita, (ge)witnes, ME witnesse, NE witness (ON, OE also and orig. ‘testimony’ and so still NE, esp. bear witness), OHG giwizzo; ChSl. stivéd- ételt (prefix sti-
2. Grk. paprus, gen. -vpos (nom. also ndprup, Hom. pdprupos), NG pédprupas : peéptuva ‘care’, Lat. memor ‘mindful of’, Skt. smr- ‘remember’, ete. Prob. based on *yap-rv- (IE -iu- suffix in abstracts, etc.) orig. ‘testimony’. Walde-P. 2.689. Boisacq 612.
3. Lat. testis, lit. ‘the third’ (= Ir. triss ‘third’), fr. *tristi- : trés ‘three’. Cf. Osc. irstus ‘testés’ (fr. *tris-to-), tris- taamentud ‘testamentd’. Hence testi- montium ‘testimony��� > It. (lea
(eval):1: == not found
```


## [2026-09-06T22:12:17.994Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -ni \"sacred\\|holy\" SYN.txt | sed -n '1,20p' | cut -c1-180",
 "description": "Grep Buck for holy/sacred"
}
```


### [2026-09-06T22:12:18.046Z] TOOL RESULT

```
1647:3. Ir. nem, NIr. neamh (now mostly ‘heaven’), W. nef (now ‘heaven’), Br. nen (also env) : ChSl. nebo ‘sky’, Grk. yégos ‘cloud’, etc. (below, 5 and 1.73)? So R
2462:Boh. hoch, short form of holec ‘bald head’, holek ‘(beardless) young man’ : holy ‘bald’, ChSl. golz ‘bare’, etc. Hence also fem. holka ‘girl’. Similarly So
8292:Fy. nu OE nacod; ber Boh. nahy; holy Sp desnudo ME naked, bare Pol nagt; goli Rum. gol NE naked; bare Russ. nagoj; golyj Tr. nocht; lomm Du. naakt; bloot Skt. nagna- NIr. —n
8311:7. ChSl. gol, SCr. go, Boh. holy, Pol. goli, Russ. golyj : OE calu, OHG kalo, etc. ‘bald’ (4.93). Walde-P. 1.537 f. Berneker 325 f.
9138:SY,), : ia 77. Gamillscheg s.v. | er the sacred ‘cake’ : Skt. dravinas- ‘wealth, property’. Barth. 770. Crk ; 5.53 DOUGH ao. Goth. dai Shun, tondpr ON, daigs Lith. min
11278:6. SCr. maramica, dim. of marama, mahrama ‘rag, cloth’, orig. ‘veil (of a married woman)’, through Turk. fr. Arab. mahrama ‘holy, forbidden, wife’ : Arab. haram �
11983:ae ON arinn, Dan. arne : Lat. Gra, 7. Skt. agnikunda-, cpd. of agni- oe asi- ‘altar’ (orig. ‘fire- | ‘fire’ and kunda- ‘pot, vessel for coals’, : G ! ie BS. dry
13323:Sacred to Ju iter’ . Fall-Torp 182,
13642:wealth’, Skt. apas-, dpas- ‘work esp. ‘sacred act’, Ay. hv-apah- + deed’, ON afl, OF afol ‘power’, OR @fnay ‘perform’, OHG woba ‘festival’, BS Walde-P. 
15913:Paint’, ang a puree of) the verbs for | Gri. ekdy ‘a likeness! (: fouxa ‘be | discussion : ae been covered by the | like’), used of a picture or a statue, NG i 85. Ot
15925:6. ChSl. obrazit ‘form, kind, image’ (reg. word for eixav; Jagié, Entstehungs. gesch. 309), Boh., Pol. obraz (Pol, > Lith. abrozas ‘holy picture, ikon’), orig ‘an 
18755:avépa is rendered by NIr ni Shuil fear agam, W. nid oes gennyf wr, and Br. nem eus pried ebet ‘there is not a hus- band to me’; so also Lett. man vira nav, Russ. u menja
23788:7. Skt. bhaga-, also ‘portion, share, al- lotment’, Av. baga-, baya- ‘share, lot’, baya- ‘part, piece’ (of the holy word) : Skt. bhaj- ‘deal out, divide, distri
24210:J. 1p aM refi; ChSl. troj2, neut. Sg. oY, iatter @SP- general Slavic; Skt. iris in Ved. tray? vidya ‘the triple fraydrs the group of three holy actions.
27501:Many parts of the body or bodily ac- tions are associated with emotions. Notably the heart, the words for which are universally used to denote the seat of emotion or ‘tempe
27520:The distinction between ‘soul’ and ‘spirit’? (or NE ghost in Holy Ghost), which became current in Christian ter- minology (Grk. pix} vs. avedua, Lat. anima ys. spirit
27548:OE gast, ME gost (NE ghost in Holy
28896:NHG herrlichkeit (‘glory’ as ‘splendor, majesty’, used by Luther for 6déa, gloria in this sense, e.g. Mt. 6.13), fr. herrlich ‘magnificent, glorious’, OHG hérli
29659:. TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1177 3 and so, rather than For the numerous other Indo-Iranian 7 jnscr- 4 5) = ¢ ’ ¢ J Dsiva y, elsewhere) : Ir. noib ‘holy’
29756:ve a rla- ‘suitable, right’, beside sb. " "= OPers. arta-, Av. asa- ‘truth, in religious sense, whence Skt. rl@van-, AV: asdvan- just, meneoue; holy’, all fr. root in
```


## [2026-09-06T22:12:24.763Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1476\\|22\\.32\\|RELIGION\" SYN.txt | head -20 | cut -c1-200",
 "description": "Locate Buck p.1476 / religion chapter"
}
```


### [2026-09-06T22:12:24.826Z] TOOL RESULT

```
226:RELIGION AND SUPERSTITION
```


## [2026-09-06T22:12:28.759Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sventas\\|iventas\\|Sventas\\|svetu\\|svetii\\|svet7\\|Sventa\" SYN.txt | head -10 | cut -c1-300; echo \"=== find 'HOLY' section header\"; grep -n \"22\\.[0-9]\" SYN.txt | tail -30 | cut -c1-160",
 "description": "Search Buck for Lith sventas"
}
```


### [2026-09-06T22:12:28.883Z] TOOL RESULT

```
=== find 'HOLY' section header
1241:Ir. dobur (rare, but cf. dobur-chu ‘ot- ter’, lit. ‘water dog’), W. dwfr, Br. dour (Celt. *dubro-) : 60Bpis* @4hacoa Schol. Theocer. (prob. Illyr.)
1257:2. Grk. @4\acca, the main word at all periods, fr. *@4da-x-1a (ef. dadayxav’ $adhaccay Hesych., presumably a Maced. form) or the like : 94Xapos ‘inner 
1640:For the use of these words as ‘heaven’, see 22.31.
1647:3. Ir. nem, NIr. neamh (now mostly ‘heaven’), W. nef (now ‘heaven’), Br. nen (also env) : ChSl. nebo ‘sky’, Grk. yégos ‘cloud’, etc. (belo
1995:‘baptism’), fr. Ir. baitsim, NIr. baistim ‘baptize’ (22.25). K. Meyer, Contrib. 169.
4528:some unexplained phonetic features and taken as an Illyr. loanword by Kretsch- mer, Glotta 22.120); Lat. equus (with fem. equa ‘mare’); Ir. ech, Gall. 
8955:OE feorm ‘food, provisions’ (5.12), also ‘feast, meal’, translating apioroy, prandium in Mt, 22.4 and Sdetmvoy, céna in Mk. 6.21, Lk. 14,12, 16, h
10675:NE trousers, earlier trouses, pl. of trouse, this fr. Ir. or Gael. triubhas (pro- nounced as NIr. trits, Sc. trews), this prob. fr. OFr. trebus, MLat. tub
10948:‘glove’ (Hom; ete.), oF for the arm, Kleeve’, fr. xelp ‘hand’. NG xepoxre (also xep-), fr. Byz. yepoprt (Chron. Mor.), xetpopriov (Du Cange), th
12216:2, Lat, agricola, epd.. of ager ‘field’ (6.12) and the root of colere ‘cultivate, ae Ernout-M. 22.205. Walde-
12466:Skt. lafigala~- (RV+) perh. with lan. gula- ‘tail, penis’ : Lith. linguoti ‘swing rock’, Walde-P. 2.436. Otherwise, a, loanword fr. a pre-Aryan la
14914:sen <9 ‘building, house’ (pl. lin 22.13) and the root of ne ‘de make’. Fr. bastir, fr. a Gme. *bast- tan ‘bind’, deriv. of OHG d 7 best ‘bas
19682:4. For ON peningr and Goth. skatts (quotable only for a particular coin; the passage Mt. 22.19 lacking), OE sceait, OHG scaz, see under ‘money’ (11.43
19686:6. ChSl. sklezt (renders vouicua Mt. 22.19), cf. Pol. szelqg name of different old Polish coins, Russ. Seleg ‘counter’, etc., fr. the Gme., cf. Goth. 
19904:3. Ir. foigde ‘begging’ (related form for ‘beggar’ apparently not quotable), vbl. noun fr. epd. of guidim ‘ask for, pray’ (22.17). Pedersen 2.
20432:oe ei (tenders ¢épos Rom. tedairan therwise Royla ‘collection’) : oth, ie together’, bairan ‘bear’. E mat (ont (for ré\os and TEhwVLOV), dis.
21243:2. NG Batw, aor. Bada, the pop. equivalent of NE put, fr. Gr. Béd\d\w ‘throw’, which is also occasionally ‘put? (LS s.v. A Il 6). The same semantic
23231:visu ‘on both sides’, but conflicting with the development of orig. c¢ in tés ‘ar- row’, 20.25 and vads ‘temple’, 22.13). Prellwitz s.v. Wal
28540:22.184 ff.
29387:5), fr, rane my mostly. im religious Mg 88 ‘faith, belief? (22.11).
31361:Ir. amaires, NIr. amhras, lit. ‘dis- belief’, neg. to Ir. ires(s) ‘belief, faith’ (22.11). Cf. Grk. amorla, above, 1.
31967:Cf. also words for ‘pray’ (22.17), of which several are the same as those listed here, and some of the others are also used in a nonreligious sense as
31981:Ir. guidim, mostly ‘pray’, see 22.17.
31999:ChSI., SCr. molitt ‘ask, beg’, refi. ‘pray’, see under ‘pray’ (22.17).
32006:Av., OPers. jad- ‘beseech, pray for’, see under ‘pray’ (22.17).
32227:W. bygwth, orig. ‘frighten’, deriv. of bwg ‘goblin, ghost’ (22.45).
32380:Lett. burts, orig. ‘magic sign’ = Lith. burtas ‘lot’, pl. ‘sorcery’ : Lett. burt, Lith. burti ‘enchant, bewitch’, etc. (22.42). Miihl.-End
34147:6. ChSl. pirja (didovexia Lk. 22.24; also ras-pirja, sq-ptrja, sti~pori), Russ. rasprja, Boh., Russ. spor, Pol. spér : ChSl. piréti se ‘strive, conten
```


## [2026-09-06T22:12:38.379Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hunsl\\|husl\\|hAsl\" SYN.txt | head -5 | cut -c1-400; echo \"=== TOC\"; sed -n '220,260p' SYN.txt | cut -c1-500",
 "description": "Search Buck for hunsl and TOC"
}
```


### [2026-09-06T22:12:38.457Z] TOOL RESULT

```
=== TOC
. Emorion (wits Some Paysicat Expressions oF EMoTION); TEMPERAMENTAL, Morat, anp ArstaEtic Notions .
. Minn, TooucHr .
- Vocan Urrmrance, SPEECH; READING AND WRITING
- Turerroriat, Socrat, AND PoxiticaL Divisions; SocraL RELATIONS
. WARFARE
. Law 22.
RELIGION AND SUPERSTITION
InpEx or Heapines .
xix
sii CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ont NO FF
135 196 326 392 455 486
536 661 739 829 916 953 1017
1084 1197 1247 1301 1370 1419 1462
1505
>= ~="Digitized by Arya Samaj Foundation Chennai and eGangotri
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
———- : Digitized by Arya Samaj Foundation Chennai and eGangotri
|
EXPLANATIONS
ABBREVIATIONS FOR LANGUAGES AND DIALECTS
Afghan
Akkadian (-Babylonian-Assyrian) Albanian
American Spanish
. Anglo-French
Arabic
Aramaic
Arcadian
Argolic
Armenian
Attic
Avestan
Boeotian
Bohemian (=Czech, a better term, but Boh. more convenient abbreviation)
Breton (modern)
Bulgarian
Byzantine (= Middle Greek)
Catalan
Church Slavic
Corinthian
Cornish
```


## [2026-09-06T22:12:42.846Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sanctus\\|sacer\\|äyıos\\|hagios\\|éyos\" SYN.txt | head -12 | cut -c1-250",
 "description": "Search Buck for sanctus/sacer"
}
```


### [2026-09-06T22:12:42.907Z] TOOL RESULT

```
11535:5. Ir. tech, NIr. teach, W. ty, Br. ti : Grk. aréyos, réyos ‘roof’, créyw, Lat, tegere ‘cover’, NHG dach ‘roof’, ete. (7.15). Walde-P. 1.620 ff. Pedersen 1.98 f. Cf. Cret. créya ‘house’ (so in Law Code, where olxia is ‘hou
11681:1. In Greek ‘a room’ is generally ex- pressed by words that are also used for ‘house, dwelling’ (7.12), as olkos, otkmua d6pos, Sua, dwyartov, réyos (properly ‘roof’ 7.62), or words denoting a special room, aS davépmy ‘man’s r
11915:7.28 ROOF Grk. (a)réyos, oréyn, dpod7 Goth. hrot Lith. stogas NG oréyn, axe ON pak (hrot) Lett. jumis Int, — téclum Dan. tag ChSl.  krovit, strécha re lello Sw. tak SCr. _ krov ri i OE pac, hrof Boh. _ strecha, krov a i 0, techado ME rof
19783:npovéyos ON arfi, erfingi, arftaki Lett. mantinieks
31770:3. Grk. défs, orig. ‘speech, diction, style’, whence ‘single word or phrase’ (Aristot., etc.), then usual gram. term for ‘word’ and so in NG : déyw ‘speak, say’ (18.21). Hence also Grk. déyos, used of a, verbal expression or 
31786:ChSl. slovo (reg. for Aéyos), Boh., Russ. slovo, Pol. stowo : slava ‘fame’, Av. sravah- ‘word, teaching, saying’, Skt. ¢ravas- ‘praise, fame’, Grk. KXéos, Ir. cla ‘fame’, etc., fr. the root of ChSI. slygati, Skt. ¢ru-, etc. 
31896:1, Grk. duodoyéw ‘agree with, admit, Confess’ (NG chiefly in eccl. usage), deriv, Of duédoyos ‘agreeing, correspond- ng’; epd. of dués ‘same’ and déyos ‘reck- oning, reason, etc.’ ih th Tapadéxouar, in class. Grk. usually �
34049:2. Grk. véyos, in early use often ‘custom’, hence ‘law’ (21.11) : vénw ‘deal out, allot’, Goth., etc. niman ‘take’. Walde-P. 2.330. Boisacq 662 f.
35571:Grk. vouixés, adj. ‘pertaining to the law’ (deriv. of véyos 11.11), is also used as sb., often rendered ‘lawyer’, but most- ly denoting one learned in the law (in
35823:2. Lat. reus (> It., Sp. reo ‘culprit’), prob. fr. *réyos, old gen. to rés (Skt. ras, gen. rdyas) ‘legal matter, lawsuit’
```


## [2026-09-06T22:12:54.727Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT spenta ===\"; grep -n \"spenta\\|sp∂nta\\|spәnta\" BRT.txt | head -8 | cut -c1-300; echo \"=== BRT gaospenta ===\"; grep -n \"gaospenta\\|gao-spenta\\|gaosp\" BRT.txt | head -5 | cut -c1-300; echo \"=== PHD ===\"; grep -n \"gōspand\\|gospand\\|spand\\b\" PHD.txt PHD_mackenzie.txt | head -10 | cut -c1-250",
 "description": "Grep Bartholomae and MacKenzie"
}
```


### [2026-09-06T22:12:54.813Z] TOOL RESULT

```
=== BRT spenta ===
=== BRT gaospenta ===
2782:{upa  mit  Akic.);  para  n  *gaosp}nta  ...will,  cupiti  potens,  glücklich':  am^rstäiti baodasla  urvän^mca  */rai^ämahi  nazdista  '■  *asaonö  urvä  °sö  "in  Ewigkeit  (wird)  die upa  >war}sta  raoca  V.34.  [Seele    des  -4Aanhängers    glücklich    sein"
8245:•  J->  S->  P-  UP^  1)  Praea  i)  mit  Akk.; a)  räumlich,  a)  "hin  -  zu':  mi%r)m  yO  .  . fravazaiU  Aaea  karsvar»  yat  arjsaAi  'pa karsvar»  yat  ifaniraitm  Yt  lO.  67;  — "iräyS  °pa  naz'a.paötm  (sd.)  asatUi ..bar^is V.9,11;  Vd.J2;  —  ui'trö  .  .  yS  kapm aip
10132:;  V.  ig.  41,  Yt  ig.  60';  —  n;imasj  « gaosp^nta^  tumas?  U *gaoAu}ia^^  ^>  V.  2A1, *V.34;  —  y!  . .  yazai  (sd.)  apa  . .  'iulcä västrät  acistsm  mantüm{sd.)  Y.^.  4;  — US  Sus  stuyl  täyäatcä  AazanAatcä  Y,  12. 2;  —  aipi.jatS {sd^  'am  Auhaf>A»m'>^ 
13299:•  j.,  g.  dätar-  :  dahr-  m.j  j.  däJhri-  f. i)  'der,  die  gibt,  schenkt',  mit  Akk.  der Sache  und  a)  Dat  der  Person:  lumasp  te gaosp?nta  .  ,  'ärö  baxlim  (sd.)  . .  asaone V.  2J.  1  '>;  —  ava.jasa  aridvJ . .  avaahe  . . aridrai  yazimnäi  jaloyanfäi  '>r
14460:idswyilHim  FrW.  2.  i ;  —  'naAe  ithwyanBif Vt./j.i3i,  *FrW.2.i,  3i  —  vm pu'^rff ähwyanSi!  vXsS  sarayä  'nö  Yt.5, 33,  17. 35;  —  vartnfm  yim  cahrugaospm  yakmäi tayata  'nB  Janta  aSsis  i/aAäiät  V. /.  17; —  'rur  yS  janal  aiim  äahäk^m  Y.g.jt; Yt.  j^  40
=== PHD ===
PHD.txt:189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān 
PHD.txt:191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdā
PHD.txt:214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] im
PHD.txt:382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Hao
PHD.txt:455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household memb
PHD.txt:566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M
PHD.txt:583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hy
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [w
PHD.txt:1173:cattle gēspand, stör.
```


## [2026-09-06T22:13:02.196Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gēspand\\|gospand\\|gwspnd\\|gōspand\" PHD.txt | head -5 | cut -c1-300; echo \"=== spand PHD\"; grep -n \"spand \\[\" PHD.txt | head -5 | cut -c1-300; echo \"=== BRT spnta\"; grep -nE \"sp.nta-|sp.nta\\b\" BRT.txt | head -6 | cut -c1-250",
 "description": "Find gospand in MacKenzie and spenta in Bartholomae"
}
```


### [2026-09-06T22:13:02.282Z] TOOL RESULT

```
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onag
1173:cattle gēspand, stör.
5440:gospandéihrag "Šā Ca» 10335 P
=== spand PHD
189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ:
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onag
455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] ab
=== BRT spnta
191:Ich  würde  bei  solcher  Sachlage  sinnloser  Raumvergeudung  geziehen  werden müssen,  hätte  ich  bei  jedem  Wort  die  ganze  Reihe  der  gleichen  oder  ähnlichen Fundatellen  aufgeführt  Wohl  aber  muss  man  gegebenen  Falls  in  de
2492:aohqm  saoi:ranqm  vinditayä  mävöya  nipä- rayeinti  .  .  Yt  77.54;  —  vTspanqm/a  att-  • kam   aiaonqm  alaoninqm^a  .  .  ya^qn zaoyasca  fravasayö  Yt./J.i48;    148; .  .  aAmat  haca  nmänilt  .  .  ya^ra  .  .  1 staoiti  Y.
2782:{upa  mit  Akic.);  para  n  *gaosp}nta  ...will,  cupiti  potens,  glücklich':  am^rstäiti baodasla  urvän^mca  */rai^ämahi  nazdista  '■  *asaonö  urvä  °sö  "in  Ewigkeit  (wird)  die upa  >war}sta  raoca  V.34.  [Seele    des  -4Aa
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.
4754:—  yal:iä  ro  data  °/il  (VP.)  spsntä  a^iä na  >räzäa?n  Y.5#.  5;  II.  iZ,  14.  i,  42.1, • — ■  mai^amnt  . .  yat  ksrmlun  "la  (NS.) sp>nta  vispe  hazaesaYLio.$i;  7.3',  /0.92, y.ga,  Y. 57.^23,  60.6;  —  /ml  '/ä 
4755:—  vTspe  vS  '/a  spmta  staota  zaota  .  .yüS- makim  yasnäica  . .  yat  'lanqm  spmianqm Vr.5.1;  2/,2,Y./2.i',  52.4,  Yt_).3,  4!.if.^ V-p:.i2,4ß,  *Vd.20,  V.  12,2;  —  äat  mraot ahurS  maeda:  ahmakim  tiqma  yat  'fanqm ipgnt
```


## [2026-09-06T22:13:17.273Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT Talisman ===\"; grep -n \"Talisman\\|tilsam\\|tilasm\" LKT.txt | head -5 | cut -c1-600; echo \"=== LKT Kalesche ===\"; grep -n \"Kalesche\\|kolesa\\|Kalesk\" LKT.txt | head -5 | cut -c1-600; echo \"=== LKT Wermut/Absinth ===\"; grep -n \"Absinth\\|afsantin\\|Wermut\" LKT.txt | head -5 | cut -c1-600",
 "description": "Grep Lokotsch"
}
```


### [2026-09-06T22:13:17.344Z] TOOL RESULT

```
=== LKT Talisman ===
4660:'Zauberbild'  [aus  gr.  TeXeopa],  vulg.-ar. tilsam,  pers.  tilism,  plr.  tilismän ;  hieraus it.  talismano,  frz.  sp.  pg.  talisman,  sp.  ta- lisma,  pg.  talismao ;  engl.  ndl.  talisman, Aisch.  lali^man  ;  russ.  talisman.  [Eguilaz 501.    Lammens  Rem  233.    ML  8622.
5495:takwlm  1999 'ta'lab  12001 talak  "lOO'A taläk  2U04 'talbls  ;200ü taira  5>007 ta'lim  !2008 tama'  !2009 /awäm  2010 tamannä  "iOll towr  2013 fawiwr  483.  2015 tannln  2018 tannür  2019 tantana  2020 teraf  2023 ia;-«Ä«  2024 tarahsakün  2025 taranguhvn  2028 <ar6  1344.  2030 terÖMS  2031 iarfä'  2032 targama  2033 targumän  2033 ia>7i  2024 torÄM»  2034 iarfrfa  2036 taV?/'  2037 tarllta  2038 tarirna  2039 iarsl'  170ß iartifo  2041 ^ösr«;  2044 tasannug  579 tasblk  1970 iasßm  2008 te^6lÄ;a  2046 iawr  2048 tausija  2050 tawätur  2053 <ay»n  1994 ßft  2074
5881:Tabaschir  1965 To&m  133 Trtfcor  1974 Trtt^f  1972 Tabnrett  483 Tw/f^i  1981 rrt/-^  1981 TagaK  Stroh)  1982 Taz/Mw  1990 Talisman  2077 TaZfc  2003 Tamarinde  2013 Tamariske  2013 Tamtam  2014 Tarife  2017 Tanner  j.  20 19 T«m  2024 Tarbusch  2031 Trtrty  2037 tärkis  mhd.  2081 ^rtroc^•  2024 2044
=== LKT Kalesche ===
=== LKT Wermut/Absinth ===
```


## [2026-09-06T22:13:18.035Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD afsantin ===\"; grep -n \"أفسنتين\\|افسنتين\\|أفسنتي\" TAD.txt TAD_pages.txt | head -10 | cut -c1-400",
 "description": "Grep TAD for afsantin"
}
```


### [2026-09-06T22:13:18.090Z] TOOL RESULT

```
=== TAD afsantin ===
```


## [2026-09-06T22:13:25.651Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la TAD*; echo \"=== leaves\"; python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(6,13):\n    print('--- leaf',i,'---')\n    print(t[i][:600])\nEOF",
 "description": "Inspect TAD leaves near p.4"
}
```


### [2026-09-06T22:13:28.344Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 243285 Sep  4 14:06 TAD_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 151889 Sep  4 14:06 TAD.txt
=== leaves
87
--- leaf 6 ---
‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬
                                                            ‫خرافات وحكابات‬
                                     ‫استبرق ‪ -‬فارسي معناه الديباج الغديظ‬
                                   ‫اسرب ‪ -‬فارسي «سيرب» معناه رصاص‬
        ‫إسطيل واصطيل ‪ -‬لاتيني ‪#‬دااناطهاة معناه مأوى الخيل والدواب‬
‫خا لان | رانم كن من ‪ 807653‬أى ك كب وهلاةطه‪:‬ذا أُخذ وكان‬
 ‫الفلكيون القدماء يعرفون حركة الكوكب مبذه الآلة ويعينورن موضعه‬
                                                             ‫ويعيسون ارتقاعه‬

                     
--- leaf 7 ---
 ‫إرفج ‪ -‬تعريب علتهة؛ الجرماني الذيمعناهحر" وهوالسشمعب غرني‬
‫جرمانيا الذي دوخ غاليا سنة ‪ 584‬ومماها داعمه؛ ‪,‬ععده‪ :‬فدخل هذا الاسمإلى‬
                                               ‫بلادنا إبان الهروب الصليبية‬
 ‫معمخورائط ب يوئاني ‪ 52114‬وهو اسملجار حامل الكرة الارضية‬        ‫طلس‬
                      ‫فارسي < أفراز‪ 6‬معناهمرتفععربيهطنف‬         ‫ار‬

 ‫إفسنتين ‏ ووناني دا غمزومج معناه لاذع وهو ثبات ورقهكورق الصعتر‬

                                                                 ‫راطم‬
                                ‫افندي ‪ -‬نري ‪ 0‬اذنذئ م‪6‬عتأة السداك‬

  ‫يك ‪ -‬في اللائين
--- leaf 8 ---
                             ‫|قنوم ارامية ‪ 9 72‬قَدُوما ‪ 4‬معناه الشخص‬
 ‫في الفارسية ل‪2‬نكر» وفىاليونانية اله عرببها المرساة والموجل‬           ‫اجر‬

 ‫جيل يوناني‪#‬وألعههدوع (إوتجيليون )معناه خير بشارة وبشرى فرح‬
‫(نكليس ) عريها الجرى‬
                   ‫نقليسوحتكلس ‪ -‬يوناني ‪59‬ا‪600‬ي» إ‬
                                                               ‫والثلقوالصباور‬
        ‫هنا أراعى « عرب » أايلغرب‬
                                ‫صلةلولك‬
                                      ‫أجتا‬
                                         ‫اوريا ‏ ايطالي ‪#‬مه‬
                               
--- leaf 9 ---
                                    ‫‪5‬‬

                                 ‫درن »‪6‬‬

           ‫بايا في اللاتينية همهم وهو تضعيف أب مقلوبا أي بايا‬
‫(كوين‬
    ‫ل الارض ت‬   ‫كسا‬
                  ‫نلل‬‫بأبللى ‏ دعي اسمهابابللان الرب هناك بلب‬
                ‫« بابيلو » أيباالباله‬   ‫ووت‬
                                          ‫نيةحفب‬
                                               ‫مشور‬
                                                  ‫‏‪ 4:١‬أ)مافي الا‬
‫يابج ‏ فارسي « بابوش » معناه غطاء الرجل وهو داس يلبس في الرجل‬
                        ‫باور ‪. 7‬يطالي عنندمة؟ معناه مخار امدر
--- leaf 10 ---
                                 ‫م‬‫ميه‬
                                    ‫م ل‬




‫وممامدم أي قاس وهو‬
                 ‫مكب م‪6‬ن‪ 5008‬أي قل د‬
                                   ‫باروسيرت يوناني ر‬
                                           ‫تستعمل لنرقة قن الوا وطذعاه‬
‫بارون ‪ -‬ايطاني مهن أصله من لغة جرمانيا ااقديمة ةط ومعناه رجل‬
‫حر كان يتولى قدي أراضي الامراء اعا هو الآن لقب شرف دون الكونت‬
                                                       ‫وهوآخر الالقاب‬
           ‫باز وبازي ‪ -‬فارسي عر بيهالصقر والعقاب واللاعة والحياقية‬
                                                
--- leaf 11 ---
                                                              ‫عت ات‬


 ‫بأميا ‪ -‬نبات له قرون تطبخ أصله من أهريكا الحو ببة واسمه هناك هطتترمع‬
 ‫و ‪40362‬دمع وعرنوه ياميا لويتئوه ‪1‬اناء وأطل! أي غاذق إزجة وهو من قصيلة‬
                                                                                                                          ‫الخعامي‬

                                                        ‫‪-‬مي « بير ب»راد به هعنردي‬    ‫ار‬‫يفبر‬
                                                 ‫بيغاء ‏ أصل هذا الطائر من الهند واسمه هندي‬
                                 ‫موف المفسول‬
   
--- leaf 12 ---
                                 ‫عت اب‬


                                ‫رجيس ‪ -‬اسمالسيار لمشئري بالفارسية‬
 ‫ايطالي ‪ 35618200‬معناه سثر الباب أصله فارسي « برده (أي ‪5‬‬       ‫رداه‬

                                                           ‫وسجف وغطاء‬
‫ريد ‪ -‬فارسي دن ردن أي دل وهومذكورفيسفراستيروكان مستعملا‬

 ‫قبل ‪5‬ال‪626‬؟ اللاتيني الذي أنشاهاو عوطس لنقل الرسائل وفى الايطالية ‪8150‬م‬
                                                        ‫وقد عرلوه بوسطة‬
                    ‫برد س حامية‪ --‬تركي « برداخ » أي صل وجلا‬
                                   ‫ردي ‪ -‬مصرية وهو نبات
```


## [2026-09-06T22:13:44.794Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py",
 "description": "Read fetch_source.py"
}
```


### [2026-09-06T22:13:44.830Z] TOOL RESULT

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


## [2026-09-06T22:13:56.436Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/talisman\" \\\n \"https://www.etymonline.com/word/cycle\" \\\n \"https://www.etymonline.com/word/cylinder\" \\\n \"https://www.etymonline.com/word/clown\" \\\n \"https://www.etymonline.com/word/colony\" \\\n \"https://www.etymonline.com/word/collar\" \\\n \"https://www.etymonline.com/word/wheel\" \\\n \"https://www.etymonline.com/word/tele-\" \\\n \"https://www.etymonline.com/word/absinthe\" \\\n \"https://www.etymonline.com/word/housel\" ; do echo \"## $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 291 (book 261), roots Kwel/Kwen 1: English/Greek/Latin derivations\" ; done",
 "description": "Archive etymonline pages"
}
```


### [2026-09-06T22:14:02.244Z] TOOL RESULT

```
## https://www.etymonline.com/word/talisman
/home/sfmqrb/git/rishe/data/verification/sources/web/675915c99a44ae95.txt
## https://www.etymonline.com/word/cycle
/home/sfmqrb/git/rishe/data/verification/sources/web/c5c99748ffb432f3.txt
## https://www.etymonline.com/word/cylinder
/home/sfmqrb/git/rishe/data/verification/sources/web/a322eb65d9e34bd4.txt
## https://www.etymonline.com/word/clown
/home/sfmqrb/git/rishe/data/verification/sources/web/b536c776d56897de.txt
## https://www.etymonline.com/word/colony
/home/sfmqrb/git/rishe/data/verification/sources/web/fd3a642277f5257a.txt
## https://www.etymonline.com/word/collar
/home/sfmqrb/git/rishe/data/verification/sources/web/0c476a0722ef1893.txt
## https://www.etymonline.com/word/wheel
/home/sfmqrb/git/rishe/data/verification/sources/web/457a3ed881f3305f.txt
## https://www.etymonline.com/word/tele-
/home/sfmqrb/git/rishe/data/verification/sources/web/06c42d7f355488fb.txt
## https://www.etymonline.com/word/absinthe
/home/sfmqrb/git/rishe/data/verification/sources/web/9926a9a5a6ceaaab.txt
## https://www.etymonline.com/word/housel
/home/sfmqrb/git/rishe/data/verification/sources/web/888797f11db661d4.txt
```


## [2026-09-06T22:14:05.736Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 675915c99a44ae95 c5c99748ffb432f3 a322eb65d9e34bd4 b536c776d56897de; do echo \"##### $f\"; head -c 2500 $f.txt | tr -s ' \\n' ' \\n'; echo; done",
 "description": "Read etymonline talisman/cycle/cylinder/clown"
}
```


### [2026-09-06T22:14:07.308Z] TOOL RESULT

```
##### 675915c99a44ae95
URL: https://www.etymonline.com/word/talisman
FETCHED: 2026-09-06T22:13:58Z
STATUS: 200
TITLE: Talisman - Etymology, Origin & Meaning
Talisman - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of talisman 
 talisman (n.) 
 1630s, "magical figure cut or engraved on stone or metal under certain observances," from French talisman , in part via Arabic tilsam (plural tilsaman ), from Byzantine Greek telesma "talisman, religious rite, payment," earlier "consecration, ceremony," originally in ancient Greek "completion," from telein "perform (religious rites), pay (tax), fulfill," from telos "end, fulfillment, completion" (see telos ).
 The figurative sense of "any means of attainment of extraordinary results" is by 1784. The Arabic word also was borrowed into Turkish, Persian, Hindi. Related: Talismanic ; talismanical .
 also from 1630s 
 Entries linking to talisman 
 telos (n.) 
 "ultimate object or aim," 1904, in biology, from Greek telos "the end, limit, goal, fulfillment, completion," from PIE *kwel-es- , suffixed form of root *kwel- (1) "revolve, move round; sojourn, dwell," perhaps via the notion of "turning point (of a race-course, a field)."
 *kwel- (1) 
 also *kwelə- , Proto-Indo-European root meaning "revolve, move round; sojourn, dwell."
 It might form all or part of: accolade ; ancillary ; atelo- ; bazaar ; bicycle ; bucolic ; chakra ; chukker ; collar ; collet ; colonial ; colony ; cult ; cultivate ; culture ; cyclamen ; cycle ; cyclo- ; cyclone ; Cyclops ; decollete ; encyclical ; encyclopedia ; entelechy ; epicycle ; hauberk ; hawse ; inquiline ; kultur ; lapidocolous ; nidicolous ; palimpsest ; palindrome ; palinode ; pole (n.2) "ends of Earth's axis;" pulley ; rickshaw ; talisman ; teleology ; telic ; telophase ; telos ; torticollis ; wheel .
 It might also be the source of: Sanskrit cakram "circle, wheel," carati "he moves, wanders;" Avestan caraiti "applies himself," c'axra "chariot, wagon;" Greek kyklos "circle, wheel, any circular body, circular motion, cycle of events," polos "a round axis" (PIE *kw- becomes Greek p- before some vowels), polein "move around;" Latin colere "to frequent, dwell in, to cultivate, move around," cultus "tended, cultivated," hence also "polished," colonus "husbandman, tenant farmer, settler, colonist;" Lithuanian kelia
##### c5c99748ffb432f3
URL: https://www.etymonline.com/word/cycle
FETCHED: 2026-09-06T22:13:59Z
STATUS: 200
TITLE: Cycle - Etymology, Origin & Meaning
Cycle - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.
 About
 Who Did This 
 Sources 
 Introduction 
 Links 
 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 
 Apps
Get Chrome Extension 
Get iOS App 
Get Android App 
 Dark
 Auto
 Light
 Terms of Services Privacy Policy 
 English (English) 
 © 2001–2026 Douglas Harper & Talia Felix 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of cycle 
 cycle (n.) 
 late 14c., cicle , "perpetual circulating period of time, on the completion of which certain phenomena return in the same order," especially and originally in reference to astronomical phenomena, from Old French cicle and directly from Late Latin cyclus , from Greek kyklos "circle, wheel, any circular body," also "circular motion, cycle of events," from PIE kw(e)-kwl-o- , a suffixed, reduplicated form of the root *kwel- (1) "to revolve, move round."
 From 1660s as "any recurring round of operations or events" (as in life cycle ). From 1821 as "single complete period in a cycle." Extended by 1842 to "any long period of years, an age." In literary use, "the aggregate of the legends or traditions around some real or mythical event or character" (1835).
 By 1884 as "recurring series of oscillations or operations in an engine, etc." From 1870 as short for motorcycle ; by 1881 as short for bicycle or tricycle .
 also from late 14c. 
 cycle (v.) 
 1842, "revolve in cycles, occur or recur in cycles," from cycle (n.). Meaning "to ride a bicycle" is by 1881 (implied in cycling ). Related: Cycled .
 also from 1842 
 Entries linking to cycle 
 bicycle (n.) 
 1868, from bi- "two" + a Latinized form of Greek kyklos "circle, wheel" (see cycle (n.)), on the pattern of tricycle ; both the word and the vehicle superseding earlier velocipede .
 The English word is said in some dictionaries to be probably not from French, but the 1868 citations are in a French context:
 The velocipedes, about which the Parisians have run mad at the present moment, are of various kinds. ... The two wheel velocipedes, the bicycles as they are styled, 
##### a322eb65d9e34bd4
URL: https://www.etymonline.com/word/cylinder
FETCHED: 2026-09-06T22:13:59Z
STATUS: 200
TITLE: Cylinder - Etymology, Origin & Meaning
Cylinder - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of cylinder 
 cylinder (n.) 
 late 14c., chilindre , "portable sundial in the shape of a cylinder with a conical top," from Old French cylindre (14c.) and directly from Latin cylindrus "roller, cylinder," from Greek kylindros "a cylinder, roller, roll," from kylindein "to roll," which is of unknown origin.
 From 1560s as "a solid figure which may be conceived as generated by the revolution of a rectangle about one of its sides." From 1690s as "chamber of a steam engine in which the force of the steam is exerted on the piston." By 1849 as "part of a revolver which contains the chamber for the cartridges." By 1878 as "cylindrical record for a phonograph."
 also from late 14c. 
 Entries linking to cylinder 
 calender (n.) 
 "machine consisting of close-set revolving cylinders or rolls which smooths and presses paper, cloth, etc.," 1510s (late 13c. in calenderer , surname of persons who use such a machine), from Old French calandreur , from Medieval Latin calendra "cloth-pressing machine," so called from the shape of the machine used, from Latin cylindrus , from Greek kylindros "roll, cylinder" (see cylinder ).
 cylindrical (adj.) 
 "having the form or properties of a cylinder," 1640s, probably from cylindric (but this is attested only from 1680s), from Latinized form of Greek kylindrikos , from kylindros (see cylinder ) + -al (1).
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 reciprocating 
 A form of engine in which the piston and piston-rod move back and forth in a straight line, absolutely relative to the cylinder..., as in oscillating-cylinder engines: in contradistinction to rotary engine....
 roundness 
 Roundness applies with equal freedom to a circle, a sphere, a cylinder, or a cone, and, by extension, to forms that by approach...
 pith 
 Old English piþa "central cylinder of the stems of plants," also, figuratively, "essential part, quintessence, condensed...
 spool 
 early 14c., spole, "weaver's bobbin, cylinder with a projecting disk at one end for winding thread upon," from Ol
##### b536c776d56897de
URL: https://www.etymonline.com/word/clown
FETCHED: 2026-09-06T22:13:59Z
STATUS: 200
TITLE: Clown - Etymology, Origin & Meaning
Clown - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of clown 
 clown (n.) 
 1560s, clowne , also cloyne , "man of rustic or coarse manners, boor, peasant," a word of obscure origin; the original form and pronunciation are uncertain. Perhaps it is from Scandinavian dialect (compare Icelandic klunni "clumsy, boorish fellow;" Swedish kluns "a hard knob; a clumsy fellow," Danish klunt "log, block"), or from Low German (compare North Frisian klönne "clumsy person," Dutch kloen ). OED (1989) describes it as "a word meaning originally 'clod, clot, lump', which like those words themselves ..., has been applied in various langs. to a clumsy boor, a lout."
 The theory that it is from Latin colonus "colonist, farmer" is less likely, but awareness of the Latin word might have influenced the sense development in English.
 The meaning "professional fool, professional or habitual jester" is attested by c. 1600. "The pantomime clown represents a blend of the Shakes[pearean] rustic with one of the stock types of the It[alian] comedy" [Weekley]. The meaning "contemptible person" is from 1920s. Fem. form clowness is attested from 1801.
 also from 1560s 
 clown (v.) 
 c. 1600, "to play the clown onstage," from clown (n.); colloquial sense of "to behave inappropriately" (as in clown around , 1932) is attested by 1928, perhaps from the theatrical slang sense of "play a (non-comical) part farcically or comically" (1891). Related: Clowned ; clowning .
 also from c. 1600 
 Entries linking to clown 
 clownage (n.) 
 1580s, "function or manners of a stage clown or jester," from clown (n.) + -age . From 1630s as "actions or behavior of a rustic."
 clownery (n.) 
 1580s, "condition or character of a clown; ill-breeding, rudeness of manners," from clown (n.) + -ery . From 1823 as "performance of a comic clown."
 clownify 
 clowning 
 clownish 
 See All Related Words (5) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Share clown 
 ‘ cite ’ 
 Page URL :
 https://www.etymonline.com/word/clown Copy 
 HTML Link :
 <a href="https://www.etymonline.com/word/clown">Etymology of clown by etymonline<
```


## [2026-09-06T22:14:15.271Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in fd3a642277f5257a 0c476a0722ef1893 457a3ed881f3305f 06c42d7f355488fb; do echo \"##### $f\"; sed -n '1,40p' $f.txt | grep -A6 \"Origin and history\" | head -20; done",
 "description": "Read colony/collar/wheel/tele- etymonline"
}
```


### [2026-09-06T22:14:17.459Z] TOOL RESULT

```
##### fd3a642277f5257a
 Origin and history of colony 

 colony (n.) 

 late 14c., "ancient Roman settlement outside Italy," from Latin colonia "settled land, farm, landed estate," from colonus "husbandman, tenant farmer, settler in new land," from colere "to cultivate, to till; to inhabit; to frequent, practice, respect; tend, guard," from PIE root *kwel- (1) "revolve, move round; sojourn, dwell" (source also of Latin -cola "inhabitant"). Also used by the Romans to translate Greek apoikia "people from home."

 In reference to modern situations, "company or body of people who migrate from their native country to cultivate and inhabit a new place while remaining subject to the mother country," attested from 1540s. Meaning "a country or district colonized" is by 1610s.
##### 0c476a0722ef1893
 Origin and history of collar 

 collar (n.) 

 c. 1300, coler, coller , "neck armor, gorget, something worn about the neck," from Old French coler "neck, collar" (12c., Modern French collier ), from Latin collare "necklace, band or chain for the neck," from collum "the neck," from PIE *kwol-o- "neck" (source also of Old Norse and Middle Dutch hals "neck"), literally "that on which the head turns," from root *kwel- (1) "revolve, move round."

 The spelling was re-Latinized in early modern English. From late 14c. as "border at the neck of a garment," also "band put around the neck of a dog or other animal for purposes of restraint or identification." From mid-15c. as "neck-band forming part of the harness of a horse or other draught-animal."
##### 457a3ed881f3305f
##### 06c42d7f355488fb
```


## [2026-09-06T22:14:20.966Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 457a3ed881f3305f 06c42d7f355488fb 9926a9a5a6ceaaab 888797f11db661d4; do echo \"##### $f\"; grep -o \"Origin and history of.\\{0,1400\\}\" $f.txt | head -1; echo; done",
 "description": "Read wheel/tele-/absinthe/housel"
}
```


### [2026-09-06T22:14:22.970Z] TOOL RESULT

```
##### 457a3ed881f3305f
Origin and history of wheel 

##### 06c42d7f355488fb
Origin and history of tele- 

##### 9926a9a5a6ceaaab
Origin and history of absinthe 

##### 888797f11db661d4
```


## [2026-09-06T22:14:26.329Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 457a3ed881f3305f 06c42d7f355488fb 9926a9a5a6ceaaab 888797f11db661d4; do echo \"##### $f\"; awk '/Origin and history of/{p=1} p{print} /Entries linking to/{if(p) exit}' $f.txt | head -30; echo; done",
 "description": "Read main entries wheel/tele/absinthe/housel"
}
```


### [2026-09-06T22:14:28.276Z] TOOL RESULT

```
##### 457a3ed881f3305f
 Origin and history of wheel 

 wheel (n.) 

 Middle English whele , disk or circular frame attached to the axle of a vehicle to help it go, from Old English hweol , hweogol , from Proto-Germanic *hwewlaz (source also of Old Norse hvel , Old Swedish hiughl , Old Frisian hwel , Middle Dutch weel ), from PIE *kw(e)-kwl-o- "wheel, circle," suffixed, reduplicated form of root *kwel- (1) "revolve, move round; sojourn, dwell."

 The figurative sense is by early 14c. To go on wheels in figurative use, implying rapid and continuous action, is by 1540s.

 Also from c. 1200 as an instrument of torture, variously used. Of cheese made in a circular form by 1977. The phrase wheel of fortune is attested from early 15c. (the image of Fortune's wheel is in English from 12c.).

 Wheels is by 1959 in slang as "automobile." Earlier wheels was "machinery," hence "motive power, principle of life." Wheel as slang for "important person, big shot" is by 1933, American English. The U.S. wheel-bug is so called by 1815.

 wheel (v.) 

 c. 1200, whelen , "turn like a wheel, turn on or as on an axis or about a center," c. 1200, from wheel (n.); the transitive sense of "cause to move in a circle, cause to turn as on an axis" is attested from late 14c. As "turn and face a different direction," by 1630s. Related: Wheeled ; wheeling .
 also from c. 1200 

 Entries linking to wheel 

##### 06c42d7f355488fb
 Origin and history of tele- 

 tele- 

 before vowels properly tel- , word-forming element of Greek origin meaning "far, far off, operating over distance," from Greek tēle "far off, afar, at or to a distance," related to teleos (genitive telos ) "end, goal, completion, result" (from PIE root *kwel- (2) "far" in space or time).

 The element also could mean "telegraph" by mid-19c. ( teleprinter ); "telephone" by late 19c. ( telecopier ), "television" by 1928 ( tele-talkie , "motion picture broadcast by television"); and "by electronic means" by 1981 ( teleshopping , originally hypothetical).
 also from c. 1940 

 Entries linking to tele- 

##### 9926a9a5a6ceaaab
 Origin and history of absinthe 

 absinthe (n.) 

 also absinth (though properly that means "wormwood"), "bitter, pale-green alcoholic liqueur distilled from wine mixed with wormwood" ( Artemisia Absinthium ), 1842, from French absinthe , "essence of wormwood" (short for extrait d'absinthe ) from Latin absinthum "wormwood," from Greek apsinthion , which is perhaps from Persian (compare Persian aspand , of the same meaning). The wormwood plant itself is figurative of "bitter" sorrow; it was known as absinth in English from c. 1500; Old English used the word in the Latin form. The drink itself attained popularity from its heavy use by French soldiers in Algiers. Related: Absinthal ; absinthic ; absinthism .

 also from 1842 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 wormwood 

 c. 1400, folk etymology of Old English wermod "wormwood, absinthe," related to vermouth, but the ultimate etymology is unknown...

 cordial 

 c. 1400, "of or pertaining to the heart" (a sense now obsolete or rare, replaced by cardiac), from Medieval Latin cordialis "of or for the heart," from Latin cor (genitive cordis) "heart," from PIE root *kerd- "heart." Meaning "heartfelt, proceeding from the heart as the supposed

 common 

 c. 1300, "belonging to all, owned or used jointly, general, of a public nature or character," from Old French comun "common, general, free, open, public" (9c., Modern French commun), from Latin communis "in common, public, shared by all or many; general, not specific; familiar, n

 old 

 Old English ald (Anglian), eald (West Saxon, Kentish) "antique, of ancient origin, belonging to antiquity, primeval; long in existence or use; near the end of the normal span of life; elder, mature, experienced," from Proto-Germanic *althaz "grown up, adult" (source also of Old F

 man 


##### 888797f11db661d4
```


## [2026-09-06T22:14:42.456Z] TOOL CALL #60: Bash

```json
{
 "command": "head -5 data/verification/sources/web/888797f11db661d4.txt; echo; for u in \\\n \"https://en.wiktionary.org/wiki/housel\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%BE%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B3%D9%81%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%B3%DA%A9%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%B7%D9%84%D8%B3%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%E1%BC%80%CF%88%CE%AF%CE%BD%CE%B8%CE%B9%CE%BF%CE%BD\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%AF%DB%8C%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7ek%CA%B7los\" ; do echo \"## $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 291 (book 261), roots Kwel/Kwen 1: Persian/Greek/English nodes\"; done",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-06T22:14:47.246Z] TOOL RESULT

```
Exit code 1
URL: https://www.etymonline.com/word/housel
FETCHED: 2026-09-06T22:14:02Z
STATUS: 200
TITLE: Etymonline - Online Etymology Dictionary


## https://en.wiktionary.org/wiki/housel
/home/sfmqrb/git/rishe/data/verification/sources/web/49f58b4e6beef2e1.txt
## https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%BE%D9%86%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/1a31e685263d6f54.txt
## https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B3%D9%81%D9%86%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/e319a036534237ab.txt
## https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%B3%DA%A9%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/40bdd446e7f4bf5d.txt
## https://en.wiktionary.org/wiki/%D8%B7%D9%84%D8%B3%D9%85
/home/sfmqrb/git/rishe/data/verification/sources/web/13512d9f1832628d.txt
## https://en.wiktionary.org/wiki/%E1%BC%80%CF%88%CE%AF%CE%BD%CE%B8%CE%B9%CE%BF%CE%BD
/home/sfmqrb/git/rishe/data/verification/sources/web/966369a701e8a180.txt
## https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%AF%DB%8C%D8%A7%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/a578272715f31e02.txt
## https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7ek%CA%B7los
/home/sfmqrb/git/rishe/data/verification/sources/web/82f314bbbf744f53.txt
```


## [2026-09-06T22:14:50.628Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 49f58b4e6beef2e1 1a31e685263d6f54 e319a036534237ab 40bdd446e7f4bf5d; do echo \"##### $f\"; grep -o \"Etymology.\\{0,900\\}\" $f.txt | head -2; echo; done",
 "description": "Read Wiktionary housel/espand/gusfand/kaleske"
}
```


### [2026-09-06T22:14:52.166Z] TOOL RESULT

```
##### 49f58b4e6beef2e1
Etymology 1 
Etymology 2 

##### 1a31e685263d6f54

##### e319a036534237ab
Etymology 
Etymology 

##### 40bdd446e7f4bf5d
Etymology 
Etymology
```


## [2026-09-06T22:14:55.876Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in e319a036534237ab 40bdd446e7f4bf5d 13512d9f1832628d 966369a701e8a180 a578272715f31e02 1a31e685263d6f54; do echo \"##### $f\"; python3 - \"$f.txt\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8',errors='replace').read()\ni=t.find('Etymology')\nprint(t[max(0,i-200):i+1200].replace('\\n\\n','\\n'))\nEOF\necho; done",
 "description": "Read Wiktionary etymologies"
}
```


### [2026-09-06T22:14:57.464Z] TOOL RESULT

```
##### e319a036534237ab
t 
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
 Persian 
 Toggle Persian subsection 
 1.1 
 Alternative forms 
 1.2 
 Etymology 
 1.3 
 Pronunciation 
 1.4 
 Noun 
 1.4.1 
 Descendants 
 1.5 
 See also 
 2 
 Urdu 
 Toggle Urdu subsection 
 2.1 
 Etymology 
 2.2 
 Pronunciation 
 2.3 
 Noun 
 2.4 
 Further reading 
 Toggle the table of contents 
 گوسفند 
 23 languages 
 العربية 
 Azərbaycanca 
 বাংলা 
 فارسی 
 Français 
 Magyar 
 Bahasa Indonesia 
 Italiano 
 ಕನ್ನಡ 
 한국어 
 Kurdî 
 ລາວ 
 Lietuvių 
 Malagasy 
 Norsk bokmål 
 Polski 
 Română 
 Русский 
 Sängö 
 Slovenščina 
 Türkçe 
 閩南語 / Bân-lâm-gí 
 中文 
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
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: گوسفند 
 Wikipedia fa 
 Alternative forms
 [ edit ] 
 گوسپند ( gōspand  / guspand ) 
 Etymology
 [ edit ] 
 From Middle Persian KYNA ( gōspand , “ sheep, small cattle ” ) , fro

##### 40bdd446e7f4bf5d
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
 Persian 
 Toggle Persian subsection 
 1.1 
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.4 
 References 
 Toggle the table of contents 
 کالسکه 
 2 languages 
 فارسی 
 Malagasy 
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
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: کالسکه 
 Wikipedia fa 
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Indo-European *kʷelh₁- 
 Proto-Indo-European *-os 
 Proto-Slavic *kolo der. 
 Russian коля́ска ( koljáska ) 
 Persian کالسکه 
 From Russian коля́ска ( koljáska ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /kaːles.ˈka/ 
 ( Dari, formal ) IPA ( key ) : [kʰɑːleskʰä] 
 ( Dari, formal ) IPA ( key ) : [kʰɑːleskʰä] 
 ( Kabuli ) IPA ( key ) : [kʰɑːleskʰä] 
 ( Hazaragi ) IPA ( key ) : [kʰɔːleskʰä] 
 ( Iran, formal ) IPA ( key ) : [kʰɒːleskʰʲe] 

##### 13512d9f1832628d

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
 Arabic 
 Toggle Arabic subsection 
 1.1 
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Declension 
 1.3.2 
 Related terms 
 1.3.3 
 Descendants 
 2 
 Ottoman Turkish 
 Toggle Ottoman Turkish subsection 
 2.1 
 Alternative forms 
 2.2 
 Etymology 
 2.3 
 Noun 
 2.3.1 
 Derived terms 
 2.3.2 
 Descendants 
 2.4 
 Further reading 
 3 
 Persian 
 Toggle Persian subsection 
 3.1 
 Etymology 
 3.2 
 Pronunciation 
 3.3 
 Noun 
 3.3.1 
 Related terms 
 3.4 
 Further reading 
 Toggle the table of contents 
 طلسم 
 7 languages 
 فارسی 
 Magyar 
 Bahasa Indonesia 
 Malagasy 
 Polski 
 پښتو 
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
 Arabic
 [ edit ] 
 Root 
 ط ل س م ( ṭ l s m ) 
 2 terms 
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Indo-European *kʷelh₁- 
 Proto-Hellenic *kʷélos

##### 966369a701e8a180

 Personal tools 
 Donations 
 Create account 
 Log in 
 Contents
 move to sidebar 
 hide 
 Beginning
 1 
 Ancient Greek 
 Toggle Ancient Greek subsection 
 1.1 
 Alternative forms 
 1.2 
 Etymology 
 1.3 
 Pronunciation 
 1.4 
 Noun 
 1.4.1 
 Inflection 
 1.4.2 
 Derived terms 
 1.4.3 
 Descendants 
 1.5 
 References 
 1.6 
 Further reading 
 Toggle the table of contents 
 ἀψίνθιον 
 8 languages 
 Deutsch 
 Ελληνικά 
 Français 
 Italiano 
 한국어 
 Latviešu 
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
 See also: αψίνθιον 
 Ancient Greek
 [ edit ] 
 ἀψίνθιον 
 Alternative forms
 [ edit ] 
 ἄψινθος ( ápsinthos ) , ἀψινθία ( apsinthía ) , ἀψινθή ( apsinthḗ ) , ἀψίνθιν ( apsínthin ) , ἀσπίνθιον ( aspínthion ) 
 Etymology
 [ edit ] 
 According to Beekes, the cluster -ινθ- ( -inth- ) suggests a Pre-Greek source, as seen in τέρμινθος ( términthos , “ terebinth ” ) , ἐρέβινθος ( erébinthos , “ chickpea ” ) , μίνθη ( mínthē , “ mint ” ) , 

##### a578272715f31e02
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
 Persian 
 Toggle Persian subsection 
 1.1 
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Proper noun 
 2 
 Urdu 
 Toggle Urdu subsection 
 2.1 
 Etymology 
 2.2 
 Proper noun 
 Toggle the table of contents 
 اسفندیار 
 5 languages 
 বাংলা 
 فارسی 
 Kurdî 
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
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: اسفندیار 
 Wikipedia fa 
 Etymology
 [ edit ] 
 From Middle Persian [Term?] ( /⁠spandadāt⁠/ ) , in turn derived from Avestan 𐬯𐬞𐬆𐬥𐬙𐬋𐬜𐬁𐬙𐬀 ( spəntōδāta , literally “ given by Amesha Spenta ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ʔis.fan.di.ˈjaːr/ 
 ( Dari, formal ) IPA ( key ) : [ʔɪs.fän̪.d̪i.jɑ́ːɾ] 
 ( Dari, formal ) IPA ( key ) : [ʔɪs.fän̪.d̪i.jɑ́ːɾ] 
 ( Kabuli ) IPA ( key ) : [ʔɪs.fän̪.d̪i.jɑ́ːɾ] 
 ( Hazarag

##### 1a31e685263d6f54
URL: https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%BE%D9%86%D8%AF
FETCHED: 2026-09-06T22:14:44Z
STATUS: -1
TITLE: 
FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T22:15:09.227Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%AF\" --note \"page 291 (book 261), Kwen 1: Persian esfand (Peganum harmala) etymology\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%86%D8%AA%DB%8C%D9%86\" --note \"page 291 (book 261), Kwen 1: Persian afsantin\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/s%C3%BCantah\" --note \"page 291, Proto-Iranian spanta\"",
 "description": "Fetch more Wiktionary pages"
}
```


### [2026-09-06T22:15:12.343Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/2e723eec41b0e095.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e98011dbfe24d506.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f292ba345a7312cd.txt
```


## [2026-09-06T22:15:15.892Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 2e723eec41b0e095 e98011dbfe24d506 f292ba345a7312cd; do echo \"##### $f\"; python3 - \"$f.txt\" <<'EOF'\nimport sys\nt=open(sys.argv[1],encoding='utf-8',errors='replace').read()\ni=t.find('From Wiktionary, the free dictionary')\nprint(t[:200] if i<0 else t[i:i+1500])\nEOF\necho; done",
 "description": "Read esfand/afsantin/proto-iranian"
}
```


### [2026-09-06T22:15:17.599Z] TOOL RESULT

```
##### 2e723eec41b0e095
From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: اسفند 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 اسپند 

 سپند 

 Etymology 1
 [ edit ] 

 A contraction of اسفندارمذ , اسفندارمزد , from Middle Persian spndrmt’ ( Spandarmad , literally “ holy thought ” ) ; name of the fourth Amahraspand (divine deity) in Zoroastrianism and a Goddess. Compare Old Armenian սանդարամետ ( sandaramet ) , սպանդարամետ ( spandaramet ) , Iranian borrowings.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔis.ˈfand/ 

 ( Dari, formal ) IPA ( key ) : [ʔɪs.fän̪d̪] 

 ( Dari, formal ) IPA ( key ) : [ʔɪs.fän̪d̪] 
 ( Kabuli ) IPA ( key ) : [ʔɪs.fän̪d̪] 

 ( Hazaragi ) IPA ( key ) : [ʔis.fän̪d̪̥] 

 ( Iran, formal ) IPA ( key ) : [ʔes.fæn̪d̪̥] 

 ( Tajik, formal ) IPA ( key ) : [ʔis.fän̪d̪] 

 Rhymes: -and 

 Readings

 Classical reading ? 

 isfand

 Dari reading ? 

 isfand

 Iranian reading ? 

 esfand

 Tajik reading ? 

 isfand

 Audio ( Iran ) : ( file ) 

 Audio ( Iran ) : ( file ) 

 Proper noun
 [ edit ] 

 اسفند • ( isfand  / esfand ) ( Tajik spelling исфанд ) 

 Esfand ( the twelfth solar month of the Persian calendar ) 

 Name of the fifth day of any month of the solar Persian calendar.

 Coordinate terms
 [ edit ] 

 Persian months edit 
 فروردین ( farwardīn  / farvardin ) 
 اردیبهشت ( urdībihišt  / ordibehešt ) 
 خرداد ( xurdād  / xordâd ) 
 تیر ( tīr  / tir ) 
 مرداد ( murdād  / mordâd ) 
 شهریور ( šahrēwar  / šahrivar ) 


##### e98011dbfe24d506
URL: https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%86%D8%AA%DB%8C%D9%86
FETCHED: 2026-09-06T22:15:11Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found

##### f292ba345a7312cd
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/s%C3%BCantah
FETCHED: 2026-09-06T22:15:12Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T22:15:22.343Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -o \"Etymology 2.\\{0,900\\}\" 2e723eec41b0e095.txt | head -1; echo \"=== harmala\"; grep -o \"harmala.\\{0,300\\}\" 2e723eec41b0e095.txt | head -3",
 "description": "Find Etymology 2 for esfand"
}
```


### [2026-09-06T22:15:23.859Z] TOOL RESULT

```
Etymology 2 
=== harmala
harmala )
```


## [2026-09-06T22:15:26.800Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('2e723eec41b0e095.txt',encoding='utf-8',errors='replace').read()\ni=t.rfind('Etymology 2')\nprint(t[i:i+1400])\nEOF",
 "description": "Print esfand Etymology 2"
}
```


### [2026-09-06T22:15:28.311Z] TOOL RESULT

```
Etymology 2
 [ edit ] 

 From Middle Persian [script needed] ( spand ) , ultimately from Proto-Iranian *cwantaH ( “ holy ” ) (compare Avestan 𐬯𐬞𐬆𐬧𐬙𐬀 ( spəṇta , “ holy ” ) , because the plant is used in fumigation against evil eye. Ultimately from Proto-Indo-European *ḱwen- . Cognate to Pashto سپېلني ( spelaní ) .

 Noun
 [ edit ] 

 اسفند • ( esfand ) 

 wild rue ( Peganum harmala )

 Descendants
 [ edit ] 

 → Ottoman Turkish: اسفند 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=اسفند&oldid=91989502 "

 Categories : Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/and 
 Rhymes:Persian/and/2 syllables 
 Persian terms with audio pronunciation 
 Persian lemmas 
 Persian proper nouns 
 fa:Persian months 
 Persian terms derived from Proto-Iranian 
 Persian nouns 
 fa:Rue family plants 

 Hidden categories: Persian terms in nonstandard scripts 
 Persian links with redundant wikilinks 
 Persian links with redundant alt parameters 
 Persian links with manual fragments 
 Pages with entries 
 Pages with 1 entry 
 Requests for native script for Middle Persian terms 

 This page was last edited on 14 August 2026, at 15:39.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agr
```


## [2026-09-06T22:15:34.182Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nfor f,key in [('e319a036534237ab.txt','From Middle Persian KYNA'),('966369a701e8a180.txt','According to Beekes')]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    i=t.find(key); print('#####',f); print(t[i:i+1400]); print()\nEOF",
 "description": "Read gusfand and apsinthion etymologies"
}
```


### [2026-09-06T22:15:35.793Z] TOOL RESULT

```
##### e319a036534237ab.txt
From Middle Persian KYNA ( gōspand , “ sheep, small cattle ” ) , from Avestan 𐬔𐬀𐬊-𐬯𐬞𐬆𐬧𐬙𐬀- ( gao-spəṇta- , “ beneficent cow ” ) , a compound of 𐬔𐬀𐬊- ( gao- , “ cow ” ) + 𐬯𐬞𐬆𐬧𐬙𐬀 ( spəṇta , “ holy ” ) , compare گاو ( gāw  / gâv ) and سپند ( sipand  / sepand ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ɡoːs.ˈfand/ , /ɡoːs.ˈpand/ 

 ( Dari, formal ) IPA ( key ) : [ɡoːs.fán̪d̪] , [ɡoːs.pʰán̪d̪] 

 ( Dari, formal ) IPA ( key ) : [ɡoːs.fán̪d̪] , [ɡoːs.pʰán̪d̪] 
 ( Kabuli ) IPA ( key ) : [ɡoːs.fán̪d̪] , [ɡoːs.pʰán̪d̪] 

 ( Hazaragi ) IPA ( key ) : [ɡʊːs.fán̪d̪̥] , [ɡʊːs.pʰán̪d̪̥] 

 ( Iran, formal ) IPA ( key ) : [ɡ̥uːs.fǽn̪d̪̥] , [ɡ̥uːs.pʰǽn̪d̪̥] 

 ( Tajik, formal ) IPA ( key ) : [ɡɵs.fán̪d̪] , [ɡɵs.pʰán̪d̪] 

 Rhymes: -and 

 Readings

 Classical reading ? 

 gōsfánd, gōspánd

 Dari reading ? 

 gōsfand, gōspand

 Iranian reading ? 

 gusfand, guspand

 Tajik reading ? 

 güsfand, güspand

 ( dialectal , Sabzevar ) IPA ( key ) : /ɡuːsˈfend/ 

 Noun
 [ edit ] 

 گوسفند • ( gōsfand / gusfand ) ( plural گوسفندها ( gōsfand-hā / gusfand-hâ ) , or گوسفندان ( gōsfandān / gusfandân ) , Tajik spelling гӯсфанд ) 

 sheep 

 Descendants
 [ edit ] 

 Judeo-Tat: gusbənd 

 See also
 [ edit ] 

 میش ( mīš  / miš ) 

 Urdu
 [ edit ] 

 Etymology
 [ edit ] 

 Etymology tree

 Avestan 𐬔𐬀𐬊-𐬯𐬞𐬆𐬧𐬙𐬀 ( gao-spəṇta ) der. 
 Middle Persian [script needed] ( KYNA ) 
 Classical Persian

##### 966369a701e8a180.txt
According to Beekes, the cluster -ινθ- ( -inth- ) suggests a Pre-Greek source, as seen in τέρμινθος ( términthos , “ terebinth ” ) , ἐρέβινθος ( erébinthos , “ chickpea ” ) , μίνθη ( mínthē , “ mint ” ) , ὑάκινθος ( huákinthos , “ hyacinth ” ) , πλίνθος ( plínthos , “ brick ” ) , μήρινθος ( mḗrinthos , “ cord, line ” ) , κήρινθος ( kḗrinthos , “ bee bread ” ) , and λαβύρινθος ( labúrinthos , “ labyrinth ” ) . [ 1 ] [ 2 ] Also, the variant ἀσπίνθιον ( aspínthion ) with /sp/ instead of /ps/ may point to borrowing from Pre-Greek. [ 3 ] [ 4 ] Related to the source of Old Armenian աւշինդր ( awšindr , “ wormwood ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ap.sín.tʰi.on/ → /apˈsin.θi.on/ → /apˈsin.θi.on/ 

 ( 5 th BCE Attic ) IPA ( key ) : /ap.sín.tʰi.on/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /apˈsin.tʰi.on/ 

 ( 4 th CE Koine ) IPA ( key ) : /apˈsin.θi.on/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /apˈsin.θi.on/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /apˈsin.θi.on/ 

 Noun
 [ edit ] 

 ἀψίνθιον • ( apsínthion )  n ( genitive ἀψινθίου ) ; second declension 

 wormwood ( Artemisia absinthium )
 Synonym: ἀρτεμισίᾱ ( artemisíā ) 
 c. 370 BCE , Xenophon , Anabasis 1.5.1 : Ἐν τούτῳ δὲ τῷ τόπῳ ἦν μὲν ἡ γῆ πεδίον ἅπαν ὁμαλὲς ὥσπερ θάλαττα, ἀψινθίου δὲ πλῆρες· En toútōi dè tōî tópōi ên mèn hē gê pedíon hápan homalès hṓsper thálatta, apsinthíou dè plêres; In this region the groun
```


## [2026-09-06T22:15:49.542Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA Absinth\"; grep -n \"Absinth\\|afsantin\\|Afsantin\\|apsinthion\\|Wermut\" AFA.txt | head -6 | cut -c1-500; echo \"=== AFM\"; grep -n \"افسنتين\\|أفسنتين\\|افسنتین\" AFM.txt AFM_pages.txt | head -5 | cut -c1-300; echo \"=== KLN wormwood\"; grep -n \"^wormwood\" KLN_1966.txt | head -2 | cut -c1-400",
 "description": "Grep Fraenkel/Addi Shir/Klein for afsantin"
}
```


### [2026-09-06T22:15:49.627Z] TOOL RESULT

```
=== AFA Absinth
=== AFM
=== KLN wormwood
```


## [2026-09-06T22:15:53.164Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"افسنت\" *.txt 2>/dev/null | head -10 | cut -c1-250; echo \"=== latin translit\"; grep -ni \"afsant\\|absint\\|apsint\" AFA.txt LKT.txt PHN.txt DEV.txt 2>/dev/null | head -10 | cut -c1-300",
 "description": "Broad grep for afsantin"
}
```


### [2026-09-06T22:15:53.257Z] TOOL RESULT

```
BQT_alt_v1.txt:22698:افسنتن ۴ 
BQT_alt_v1.txt:22706:دارد . افسنتی 
=== latin translit
AFA.txt:5867:De vinis: 18 apsinthi 17 conditum 19 rosathi.
```


## [2026-09-06T22:16:03.952Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"افسنت\\|افسنطین\\|افسنطن\" BQT_v1_pages.txt | head; echo \"=== alt v1 context\"; sed -n '22690,22712p' BQT_alt_v1.txt | cut -c1-200",
 "description": "Find afsantin in Borhan"
}
```


### [2026-09-06T22:16:04.029Z] TOOL RESULT

```
=== alt v1 context
اقسرسگزی - یکس مین بی فطه 
و سکون کاف فارسی و زای نقطه دار بتحتانی 
رسیده » نام سازی باشد که نوازند - ونام تصنیفی 
وقولی است ازصنیفات بارید . 

افسر شدن - کنابه از یادشاه شدن 
باشث . 

افسنتن ۴ 
بکسر الك و سکون 
نون و فوفانی بتحتانی 
رسیده وینون‌زده: توعی 
از بوی مادران کوهی 
است .کل آن بافعوان 
وتلخی آن صبر تزديك 
است ۰ دردچشم‌را سود 
دارد . افسنتی 


افسوس؟ ح با وار مجپول بر وزنه 


محبوی » پنعتی ظلم و ستم - ویراهی باشد - .
```


## [2026-09-06T22:16:14.604Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(336,424):\n    if 'افس' in t[i] or 'افسن' in t[i]:\n        print(i, ' '.join(t[i].split()[:12])[:120])\nEOF",
 "description": "Find afs- leaves in Borhan v1"
}
```


### [2026-09-06T22:16:16.515Z] TOOL RESULT

```
364 آفری کشوث و نخم آنرا بذرالکشوث خوانند . فواق را تافع است
365 ات وافرا یمرن الیل خوالند . اسر ۵لن؟ « بر وزن افشردن
372 آزامه ناه روند بخورند سل را منعطم سازد . واکر اژدو درهم
392 اگارده است که افسانه و سر گذشت باشد . انگاده ۱ ه
394 انگشت ب حرف‌نهادن - کنابه ازعیب کر فتن ودکته گیری کردن باشد
410 اهزون اهز ون - ختح اول بر وذن محزون » بازاینده و
```


## [2026-09-06T22:16:35.446Z] TOOL CALL #72: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D9%84%D8%B3%DA%A9%D9%87/\" \"https://abadis.ir/fatofa/%D8%A7%D9%81%D8%B3%D9%86%D8%AA%DB%8C%D9%86/\" \"https://abadis.ir/fatofa/%D8%B7%D9%84%D8%B3%D9%85/\"; do echo \"## $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 291 (book 261): Mo'in entries for kaleskeh / afsantin / telesm\"; done",
 "description": "Fetch abadis Mo'in entries"
}
```


### [2026-09-06T22:16:41.840Z] TOOL RESULT

```
## https://abadis.ir/fatofa/%DA%A9%D8%A7%D9%84%D8%B3%DA%A9%D9%87/
/home/sfmqrb/git/rishe/data/verification/sources/web/2d423771386f6704.txt
## https://abadis.ir/fatofa/%D8%A7%D9%81%D8%B3%D9%86%D8%AA%DB%8C%D9%86/
/home/sfmqrb/git/rishe/data/verification/sources/web/3d69cead59ab4e58.txt
## https://abadis.ir/fatofa/%D8%B7%D9%84%D8%B3%D9%85/
/home/sfmqrb/git/rishe/data/verification/sources/web/77622037fbfab311.txt
```


## [2026-09-06T22:16:45.342Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 2d423771386f6704 3d69cead59ab4e58 77622037fbfab311; do echo \"##### $f\"; grep -o \"فرهنگ معین.\\{0,500\\}\" $f.txt | head -2; echo \"---\"; grep -o \"روس.\\{0,120\\}\\|یونان.\\{0,150\\}\" $f.txt | head -5; echo; done",
 "description": "Read Mo'in entries from abadis"
}
```


### [2026-09-06T22:16:47.149Z] TOOL RESULT

```
##### 2d423771386f6704
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
---
روسی ، اِ ) ازکلمه کالسکای روسی گرفته شده است و اصل آن شاید از«کاررزا» یا «کاررُزا»ی ایتالیایی و کالُش آلمانی است. ( یادداش
روسی است. ( از فرهنگ نظام ). مأخوذ از روسی ، گردون چهارچرخه اطاق دار. ( ناظم الاطباء ). 
روسی، یکی ازوسائل نقلیه روپوشیده که دارای چهارچرخ است وبوسیله دواسبیابیشترحرکت میکند
روس . ] (اِ. )۱ - اتاقکی که ~دارای چهار چرخ می باشد و به وسیلة ~یک اسب یا بیشتر حرکت می کند. ۲ - چهارچرخه ای که برای حمل و 
روسی، از روسی: коля́ска ) [ ۱] یا درشکه یکی از وسایل نقلیه است. 

##### 3d69cead59ab4e58
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
---
روس نوشته اند، در آثار بقراط، دیوسقوریدس، پلینی، و جالینوس از این گیاه نام برده شده است که شاید در مواردی منظور گونه های دی

##### 77622037fbfab311
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
---
یونانی طلسما ) دستگاهی به علم حیل کرده. آنچه خیالهای موهوم بشکل عجیب در نظر می آرند و نیز شکلی و صورتی عجیب که بر سر دفائن و خزائن تعبیه کنند. ( از مؤیدو 
یونانی است ، عربی نیست ، چه در تقدیر عربی بودن بکسرتین آمدن این لفظ وجهی ندارد چرا که این وزن در کلام عرب نیامده ، اگر عربی بودی به کسر اول و فتح ثانی بر و
یونانی به معنای گره ناگشودنی.۳. برگردانده «مُسلّط». بنابراین، طلسم همان مسلط است و علت نامگذاری طلسم به این نام، چیرگی طلسم بر فرد طلسم شده است. 
یونانی: τέλεσμα ) یک باور خرافی است که می تواند هر شیء یا نگاره ای متشکل از واژگان، شمارگان، اشکال و جداول دارای قدرت مذهبی یا جادویی باشد که هدف آن محافظت
یونانی τέλεσμα ( telesma ) است به معنی «تکمیل، آیین مذهبی، پرداخت»، که از طریق عربی طلسم ( طلسم، جمع: طلاسم ) وارد فارسی شده است. ریشه آغازین عبارت فعل tel
```


## [2026-09-06T22:16:54.271Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -o \"افسنتین.\\{0,300\\}\" 3d69cead59ab4e58.txt | head -6",
 "description": "Read abadis afsantin"
}
```


### [2026-09-06T22:16:55.765Z] TOOL RESULT

```
افسنتین - معنی در دیکشنری آبادیس
افسنتین - معنی در دیکشنری آبادیس 
افسنتین
افسنتین. [ اَ س َ ] ( معرب ، اِ ) اپسنتین. نوعی از بوی مادران کوهی است درد چشم را سود دارد و گل آن به اقحوان و تلخی آن بصبر نزدیک است. ( از برهان ) ( آنندراج ). زریره. دارای سه قسم و هر سه رادر طب مانند محرکات و ادویه ضد کرم استعمال میکنند. نباتیست مابین شجر و گیاه شبیه ببابونه گاوچشم. رجوع به تحفه حکیم مو
افسنتین را بر روی اوراق پاپیروس نوشته اند، در آثار بقراط، دیوسقوریدس، پلینی، و جالینوس از این گیاه نام برده شده است که شاید در مواردی منظور گونه های دیگری از جنس آرتمیزیا بوده است. این گیاه در مناطق گرم و خشک مدیترانه به خوبی رشد می کند. در قرون وسطا، پرورش آن در سرزمین پهناوری در شمال اروپا، از شبه جزیرۀ 
افسنتین در طی قرون قبل با اختلاف اندکی با موارد استفادۀ امروزی آن شباهت دارد، مثلاً از این گیاه به عنوان هضم کننده، تب بُر، رفع خنازیر، یرقان، آب آوردن، فلج، رماتیسم، دفع کِرْم و حتی در موارد شیوع بیماری های طاعون، وبا و باد سرخ استفاده می کرده اند. همچنین، این گیاه دارای اثر مقوی، مقوی قلب، مدر، قاعده آور
```


## [2026-09-06T22:17:08.983Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT colo ===\"; grep -n \"^colō\\|^colo,\\|colo, -ere\\|incola\" LAT.txt | head -5 | cut -c1-400; echo \"=== LAT collum ===\"; grep -n \"collum\" LAT.txt | head -4 | cut -c1-400; echo \"=== LEW collum ===\"; grep -n \"collum\" LEW_1910.txt | head -3 | cut -c1-400",
 "description": "Grep Latin etymological dictionaries"
}
```


### [2026-09-06T22:17:09.057Z] TOOL RESULT

```
=== LAT colo ===
3712:dans inquilinus, incola, agricola; dfes lors anculus a ete inanalysable.
12980:coapos 4 s (cf.-uena dans aduena ): accola-, incola : agricola, siluicola,
12988:s' 4 tablir k la place des incolae. Colonus a un f 4 ninin colona, et des
13000:Coapos 4 s: accolo: habiter auprbs de; accola n.(oppos 4 k incola)
13002:incola a.: habitant; dans la 1 . du droit traduit le gr. TOXpoixoc ou
=== LAT collum ===
12931:collum, -i n.(et collus a. chez les archaiques, cf. Thes. III 1658,
12932:73sqq.; le succ&s de collum a pu etre diteraini en partie par le col-
82279:" 33G, sors collum, av. dern. ligne, 1 . xpoyoc;.
=== LEW collum ===
```


## [2026-09-06T22:17:12.326Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D0%BA%D0%BE%D0%BB%D1%8F%D1%81%D0%BA%D0%B0\" --note \"page 291 (book 261), Kwel: Russian koljaska carriage\"; python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%84%D9%86%D8%AF%D8%B1/\" --note \"page 291 (book 261), Kwel: Persian silandar from French\"",
 "description": "Fetch koljaska and silandar"
}
```


### [2026-09-06T22:17:18.334Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a283a1f06e7e999c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ea2225b813299e5c.txt
```


## [2026-09-06T22:17:21.331Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12925,12945p' LAT.txt | cut -c1-300; echo \"=== colo entry\"; sed -n '12970,12995p' LAT.txt | cut -c1-300",
 "description": "Print Ernout-Meillet collum and colo"
}
```


### [2026-09-06T22:17:21.400Z] TOOL RESULT

```
xoXwvoc, xoXuwt| "colline". Iit. kdlnas, qui s'accorde pour 1 ’intonation
avec kelti "ilever", fait supposer *kolan~, k quoi lat. collis ne contre-
dit pas si, coaae en gr., i.-e. a s'est aaui aprfes syllabe comprenant
o; alors le rapport avec columen (v. ce aot), de *kelamen-, deviendrait
clair. V. sajt holm "colline" (et, avec un sens dirivi, v.isl.Aol*r "ile")
est aussi parent. Cf. cello, celsus.
collum, -i n.(et collus a. chez les archaiques, cf. Thes. III 1658,
73sqq.; le succ&s de collum a pu etre diteraini en partie par le col-
lectif pluriel colla qui est frequent et en partie par le fait que
beaucoup de noas de parties dn corps sont neutres en latin): cou (sens
propre et sens figuri, et dirivis). - Ancien (Pl.),usuel. M.L.3053;
irl. coli ?
Derives et coaposes: collaris adj., et subst. n. coi lare (scii .ferrum
ou uinculum ): collier, M.L.3043, v.h.a. chollare-, decollo,-as, M.L.
3506.
Collus est issu de kol-so-s (coaae uelle de uel-se), Cf. got. ha Is
"cou" (aasc.). On s'est demande si ce aot est k rattacher au groupe
de *kel- "en haut", v. celsus, ou k celui de *k w el- "tourner", v. colo.
En faveur de la seconde hypothbse, on peut aentionner gr. Tpa)(T)AoC en
face de xpO)(0£, <^ui est contesti, et lit. kHklas "cou" dont la ressem-
blance avec gr. xuxXoe "cercie", etc. est frappante.
=== colo entry
coluisse Samo, oi Servius note: ueteres colere dicebant, etiam cum
maior minorem diligeret. Puis le sens s'est 4 tendn, et col5 designant
vice—versa le culte et les honneurs que les honaes rendent aux dieux
a signifi 4 "honorer, rendre un culte k n : superior colitur, non colit
inferiorem, a pu 6crire le a£ne Servius, B.3,61.
Colo "cultiver" a pris 4 galeaent le sens aoral que le verbe a en
franqais: colere uirtiitem, artes, etc.; et 1'adj.verbal cultus signifie
le plus souvent "eultiv 4 aoraleaent, 6 l 4 gant, orn6", cf. excultus et
le privatif incultus (avec 1 1 abstrait incultus,-us).Vait4 de tout teaps.
A colo se rattache un substantif en -a, -cola seuleaent dans les
coapos 4 s (cf.-uena dans aduena ): accola-, incola : agricola, siluicola,
caelicola (= ovpoivovypc Esch.); cf. peut-%tre domicilium d 4 riv 4 de
*domicola? . En d 4 rive 4 galeaent:
colonus a.: celui qui tient lieu du propri 4 taire, qui cultive en
son lieu et place "feraier", au sens technique ti 14 gal dn aot (pour
la valeur du suffixe, cf. patronus "celui qui fait fonction de pfere"
en face de pater)-, puis par extension "cultivateur" (par opposition
k pastor ): habitant d'une colonie (= gr. cxtohxoc), qui lui aussi vient
s' 4 tablir k la place des incolae. Colonus a un f 4 ninin colona, et des
d 4 riv 4 s: colSnia "ferae" et "colonie" (sens abstrait et concret), d'oii
gern.: K6ln , britt. Colun-, colonicus; coloniSrius, coidnStus,-us a.
(bb lat. jurid.).
D 4 riv 4 s en cult-: cultio: culture (sens physique et aoral). Classique,
aais rare: Cic 4 ron, et aprbs lui S^-Aabr., Arn .; cui tura: culture (sens
phys. et aor.) M.L.3383; cultus, -us a.: culture (sens propre dans
Cic. et T.L.); aais beancoup plus enploy 4 au sens aoral " 4 ducation,
```


## [2026-09-06T22:17:29.226Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('a283a1f06e7e999c.txt',encoding='utf-8',errors='replace').read()\ni=t.find('From Wiktionary'); print(t[i:i+900])\nEOF\necho \"=== silandar\"; grep -o \"فرانسه.\\{0,200\\}\\|فر\\. \\].\\{0,150\\}\" ea2225b813299e5c.txt | head -4",
 "description": "Read koljaska and silandar"
}
```


### [2026-09-06T22:17:30.936Z] TOOL RESULT

```
From Wiktionary, the free dictionary

 Russian
 [ edit ] 

 Russian Wikipedia has an article on: коляска 

 Wikipedia ru 

 Etymology
 [ edit ] 

 Ultimately from Proto-Slavic *kolo .

 According to Vasmer, this word was documented in Old Russian since 1695 as каслика. It is cognate with Polish kolasa .

 By surface analysis , коло ( kolo , “ a wheel ” ) +‎ -ка ( -ka ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : [kɐˈlʲaskə] 

 Audio : ( file ) 

 Noun
 [ edit ] 

 коля́ска • ( koljáska )  f   inan ( genitive коля́ски , nominative plural коля́ски , genitive plural коля́сок , relational adjective коля́сочный , diminutive коля́сочка ) 

 baby carriage , stroller , perambulator , pram 
 Synonym: де́тская коля́ска ( détskaja koljáska ) 

 carriage (and horse), barouche 

 wheelchair 

 sidecar , buddy seat 

 Declension
 [ edit ] 

 Declension of коля́ска ( inan fem-form velar-stem accent-a 
=== silandar
فر. ] (اِ. ) ۱ - لوله ای است استوانه ای شکل که در موتور اتومبیل تعبیه شده ، در داخل سیلندر پیستون حرکت می کند و گاز موجود در سیلندر را به سمت ته سیلندر - ک
```


## [2026-09-06T22:17:40.743Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\n# find page tags\ntags=re.findall(r'\\[pdf page (\\d+)\\]',t)\nprint('tags',len(tags), tags[:5], tags[-3:] if tags else '')\nfor pat in ['spenta','hunsl','kuklos','hwewula','sventas']:\n    idx=[m.start() for m in re.finditer(pat,t,re.I)][:3]\n    print(pat, idx)\nEOF",
 "description": "Inspect Walde-Pokorny Bd1"
}
```


### [2026-09-06T22:17:43.380Z] TOOL RESULT

```
tags 0 [] 
spenta []
hunsl [2299291, 2465698]
kuklos []
hwewula []
sventas [2298793]
```


## [2026-09-06T22:17:46.492Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nprint(t[2298600:2299700])\nEOF",
 "description": "Print Walde-Pokorny kwen entry"
}
```


### [2026-09-06T22:17:48.390Z] TOOL RESULT

```
              ;




kuen- „feiern; heilig(en)“.
   Verbal in lett. svinet „ feiern, heiligen“ (Schulze KZ. 45, 235); av. spantn-
„heilig   (zur Bed. s. Bartholoraae Airan. Wb. 1619 ff.) = lit. sventas aksl.
             £:
                                                                                                                           ,


svqi7> „heilig“ (hochstufige A-Ableitung wie del-iog     dot are Schulze aaO.),             :
                                                                                                      ,


Komp. Superl. av. span-yah, spanista- ,,heiliger, heiligst“, es-St. av. spfinah-
n.    „Heiligkeit“;                dazu wahrscheinlich got. hunsl                      n.       ,Opfer“, ags. husl                  n.

 „Sakrament (kun-s-lo andere Deutungen verzeichnet Feist Got. Wb. 148).
                        £




 Z. B. Fick 1 4 49, 428 (mit fernzuhaltendem) III 4 93, Persson Beitr.  94                                                     1
```


## [2026-09-06T22:17:56.967Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'kuel-|k\\uu02b7el-|kolos|colere', t):\n    print(m.start(), t[m.start()-100:m.start()+200].replace('\\n',' ')[:300]); print('---')\nEOF",
 "description": "Find kwel in Walde-Pokorny"
}
```


### [2026-09-06T22:17:58.695Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/usr/lib/python3.12/re/__init__.py", line 224, in finditer
    return _compile(pattern, flags).finditer(string)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/re/__init__.py", line 307, in _compile
    p = _compiler.compile(pattern, flags)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/re/_compiler.py", line 745, in compile
    p = _parser.parse(p, flags)
        ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/re/_parser.py", line 979, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/re/_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/re/_parser.py", line 544, in _parse
    code = _escape(source, this, state)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/re/_parser.py", line 392, in _escape
    raise source.error("incomplete escape %s" % escape, len(escape))
re.error: incomplete escape \u at position 7
```


## [2026-09-06T22:18:02.720Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['kuel-','colere','hweogol','collum']:\n    for m in list(re.finditer(re.escape(pat), t))[:3]:\n        print(pat, m.start(), '>>', t[m.start()-250:m.start()+250].replace('\\n',' ')[:500]); print('---')\nEOF",
 "description": "Find kwel-1 in Walde-Pokorny Bd1"
}
```


### [2026-09-06T22:18:04.284Z] TOOL RESULT

```
kuel- 1754092 >>                                                                                          gr.   y.vxvov x ov   aixvov usw.            s.   Yf. LEWb. 2 s. v.   Auf eine Wzf. ku-el- bezieht Petersson LUA 1915, 7f., 1916, 40 arm. setj „IIaufe, Menge" ( *kuel-dh-io oder -gh-(o -), ags. lucylco „Ivrampf- ader", wozu lucelian      eitern"; gegen Zupitzas Gut. 57 Yerbindung                                                ,   mit lett. kvclc „Entziindung einer Wunde", woriiber u. qcu- „anziinden, verbrenn
---
kuel- 2308552 >>  ;   besser nur von einer Parallelwz. suerpjb(h) neben kuerpjb'Ji ) (Falk-Torp u. svaroe). — Ai. carbati (Dhatup) „geht“ und ai. carbhnta-     lat. cucurbita                               ;     (Fick III 4 116) widerstreben im Anlaut q statt qit-.   kuel- „schlammig“.      Arm. Salem „feuchte, benetzte, bereite Mortel", isalax „Lelim, Schlamm, Mortel"         (-al-   =   l   oder t l\,     lit.    svelniis „weich,          sanft          anzufassen"?         [Liden] Petersson         LUA. 1916, 
---
colere 325713 >>                                              arton „pfliigen“                                                                                                                                                                              11  „habitare, colere ), ags. enrd, lent f. „gepflugtes Land, Ertrag                                          11                                                                     anord.                                                                              
---
colere 1404511 >> Garten", aiirtja ..Gartner 1- ags. ortgeard „Baum~                             ,                                  got. udrtigurds                  ,,                                                                   ,            ahd. orzon iGl.i ..excolere -- ivgl. dazu TJhlenbeck Got. Wb. 2 20,                    -- garten                  ,   Liden Anlautges. 23 a, Feist GWb. 37 f., bes. wegen aisl. urt kaum Ent- lehnung aus lat. iiortus nach Kluge Grdz. I 2 339, Loewe KZ. 39, 333); aisl. rot 
---
colere 2136236 >> n")    u.   anderen Worten.          — Arm. hem „bringe, trage, ertrage" (Scbeftelowitz                             BB. 29, 13) bleibt fern.   Ygl. Fick KZ. 20, 355 f., Curtius 5 153, Fick I 4 386 (hier obne Scheidung von qel- „treiben" und q'i.el- „colere"), II 4 84, Zupitza Gutt. 106f. (Lit.), Falk-Torp           u. hals, holm.   2. qel- „stechen“              (s.       qel    und sqel „spalten, ’schlagen"             fiber das Verhaltnis          zu diesen).    Ir.        cymr. celyn, corn. k
---
collum 2133030 >> olomos fiberzeugt mich nicht). Vermutlich hierher Zupitza Gutt. 50, Falk-Torp u. hals m. Lit.); gegen Verb, mit q*el- ,.drehen“ als ,, Saule, Trager des Kopfes" (vgl. ai. cird-  dhura- m. „Iials“; ags. sivcor „Pfosten“ siveorn „FIals“) lat. colitis, collum                                                                    :    „Hals“ = got. aisl. alid. hals „Hals“ (aueh mir. coll „Haupt“? Stokes IF.  12, 187).       Aber abg. klasz „Ahre“ = alb. leal                          ds.      eber zu   q
---
collum 2403166 >> rotz Prellwitz KZ. 47,  302 nicht aus *x/.uf ua, s. qel- „schlagen“; sehr fraglich ist Zugehorigkeit                         l    von xXoiog, xXcgog „Halseisen fur Yerbrecher, Halsband fur Hunde“ als *yJ.coftog, Boisacq s. v. m. Lit.   Nicht zu lat. collum, dt. „Hals‘, s. qel- „ragen").    Lat. cl avis „Schliissel“ (kaum aus dem Gr.), Demin, claviculae „Wickel- ranken des Weins", von Prellwitz KZ. 47, 302 noch als Nachwirkung der \Yzbed. ..anhaken" aufgefaBt, aber wohl bloB „kleines Hakchen", cl
---
collum 2516492 >> ursprgl. „Baumstamm, gestutzter Stamm“ (?) s. qel- „schlagen“      dab coins „Spinnrocken“ der „sich drehende"                                         ;   sei,   stimmt sachlich nicht (s. Vf. LEWb. 2 s. v.); xiber coluber s. Yf. LEWb. 2 s. v., iiber collum, Hals s. qel- „ragen“.    Fiir Osk.-Umbr. ware „drehen“ zu erschlieBen, wenn lat. poples -itis „Kniebeuge, Kniekehle" dorther entlehnt                                     ,   sein sollte, doch s. u.     Aisl. hvel n. „Rad“ (= apr. Icclan ds.; 
---
```


## [2026-09-06T22:18:27.329Z] TOOL CALL #83: Bash

```json
{
 "command": "sed -n '60,140p' tools/verify_check.py",
 "description": "Read rest of verify_check.py"
}
```


### [2026-09-06T22:18:27.365Z] TOOL RESULT

```
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


## [2026-09-06T22:18:39.064Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nfor f,k in [('49f58b4e6beef2e1.txt','Etymology 1'),('82f314bbbf744f53.txt','From Wiktionary')]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    i=t.rfind(k) if f.startswith('49') else t.find(k)\n    print('#####',f); print(t[i:i+900]); print()\nEOF",
 "description": "Read housel and kwekwlos wiktionary"
}
```


### [2026-09-06T22:18:40.998Z] TOOL RESULT

```
##### 49f58b4e6beef2e1.txt
Etymology 1
 [ edit ] 

 From Old English hūsl , hūsel , hūsul , from Proto-West Germanic *hunsl , from Proto-Germanic *hunslą .

 Alternative forms
 [ edit ] 

 hosel , hosil , hosol , housil , housul , housyl , husel 

 husell , husul ( Early Middle English ) 

 hoosyl , hosill , housyll , howsel , howsell , howsill ( Late Middle English ) 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈhuːzəl/ 

 Noun
 [ edit ] 

 housel ( uncountable )

 The Eucharist ( bread and wine taken at Holy Communion ) .

 ( rare ) The ritual or ceremony of Holy Communion .

 ( rare ) Participation or partaking in Holy Communion .

 Related terms
 [ edit ] 

 houselen 

 houselynge 

 Descendants
 [ edit ] 

 English: housel ( archaic ) 

 Scots: hoozle , ouzle ( obsolete ) 

 References
 [ edit ] 

 “ hǒusel, n.(1). ”, in MED Online , Ann Arbor, Mich.: University of Michigan , 2007 , retrieved 23 March 2019 .


##### 82f314bbbf744f53.txt
d
```


## [2026-09-06T22:19:42.388Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"CLOWN [a-zA-Z()ʷ*-]*\" AHD_watkins1985.txt | head -3; echo \"--- ENCYCLOPEDIA/TELEVISION/TELEGRAPH\"; grep -o \"ENCYCLOPEDIA [a-zA-Z()ʷ*-]*\\|TELEVISION [a-zA-Z()ʷ*-]*\\|TELEGRAPH [a-zA-Z()ʷ*-]*\\|TELETYPE [a-zA-Z()ʷ*-]*\" AHD_watkins1985.txt | head -6",
 "description": "Check AHD index for clown and others"
}
```


### [2026-09-06T22:19:42.457Z] TOOL RESULT

```
--- ENCYCLOPEDIA/TELEVISION/TELEGRAPH
ENCYCLOPEDIA pau-
```


## [2026-09-06T22:19:59.290Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && tail -25 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['url'])\"",
 "description": "List archived URLs"
}
```


### [2026-09-06T22:20:00.977Z] TOOL RESULT

```
200 https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%B3%DA%A9%D9%87
200 https://en.wiktionary.org/wiki/%D8%B7%D9%84%D8%B3%D9%85
200 https://en.wiktionary.org/wiki/%E1%BC%80%CF%88%CE%AF%CE%BD%CE%B8%CE%B9%CE%BF%CE%BD
200 https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%AF%DB%8C%D8%A7%D8%B1
-1 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7ek%CA%B7los
200 https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%AF
-1 https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%86%D8%AA%DB%8C%D9%86
-1 https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/s%C3%BCantah
200 https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1
200 https://www.etymonline.com/word/bazaar
200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7el-
200 https://en.wiktionary.org/wiki/bazaar
200 https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%84%D8%A7%DA%A9
200 https://en.wiktionary.org/wiki/%DA%AF%D8%B2%D8%A7%D8%B1%D8%AF%D9%86
200 https://en.wiktionary.org/wiki/%DA%86%D8%A7%D8%B4%D8%AA
200 https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B4%D8%AA%D9%86
200 https://abadis.ir/fatofa/%DA%A9%D8%A7%D9%84%D8%B3%DA%A9%D9%87/
200 https://abadis.ir/fatofa/%D8%A7%D9%81%D8%B3%D9%86%D8%AA%DB%8C%D9%86/
200 https://abadis.ir/fatofa/%D8%B7%D9%84%D8%B3%D9%85/
200 https://en.wiktionary.org/wiki/%D0%BA%D0%BE%D0%BB%D1%8F%D1%81%D0%BA%D0%B0
200 https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%84%D9%86%D8%AF%D8%B1/
200 https://en.wiktionary.org/wiki/%D8%B2%D8%A7%D8%B1
200 https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%AE
200 https://en.wiktionary.org/wiki/%DA%86%D8%B4%D9%85
200 https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%A7%D9%87
```


## [2026-09-06T22:20:07.123Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport json,os\nurl=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7el-\"\nfor l in open('index.jsonl'):\n    d=json.loads(l)\n    if d['url']==url: f=d['file']; break\nt=open(os.path.join('.',os.path.basename(f)),encoding='utf-8',errors='replace').read()\ni=t.find('From Wiktionary')\nprint(t[i:i+1200])\nEOF",
 "description": "Read archived PIE kwel- page"
}
```


### [2026-09-06T22:20:08.823Z] TOOL RESULT

```
From Wiktionary, the free dictionary

 (Redirected from Reconstruction:Proto-Indo-European/kʷel- ) 

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *kʷelh₁- [ 1 ] [ 2 ] 

 to turn ( end-over-end ) 

 to revolve around, and therefore to sojourn, to dwell

 Reconstruction notes
 [ edit ] 

 The root must be reconstructed with -h₁- in order to explain some forms in Greek and Celtic, including:

 Proto-Greek *kʷélh₁-dʰe-ti ( dʰe-present ) > Ancient Greek τελέθω ( teléthō ) 

 Proto-Celtic *kʷalnati ( nasal present ) > Welsh pallu , Old Irish imm·cella 

 This reconstruction, however, contradicts some forms in other languages, e.g.:

 Proto-Italic *kʷl̥-tó-s ( past participle ) > Latin cultus (not **clātus < **kʷl̥h₁-tós)

 However, these apparent laryngeal-free reflexes can be explained by various secondary processes. Also, cultus specifically can be explained according to the proposed change of *ClHC > *ColC when in a labial environment. [ 3 ] 

 Alternative reconstructions
 [ e
```


## [2026-09-06T22:25:38.041Z] TOOL CALL #88: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build291.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_KWEL   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7el-\"\nE_TALIS  = \"https://www.etymonline.com/word/talisman\"\nE_CYCLE  = \"https://www.etymonline.com/word/cycle\"\nE_CYL    = \"https://www.etymonline.com/word/cylinder\"\nE_CLOWN  = \"https://www.etymonline.com/word/clown\"\nE_COLONY = \"https://www.etymonline.com/word/colony\"\nE_COLLAR = \"https://www.etymonline.com/word/collar\"\nE_WHEEL  = \"https://www.etymonline.com/word/wheel\"\nE_TELE   = \"https://www.etymonline.com/word/tele-\"\nE_ABS    = \"https://www.etymonline.com/word/absinthe\"\nW_HOUSEL = \"https://en.wiktionary.org/wiki/housel\"\nW_GUSF   = \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B3%D9%81%D9%86%D8%AF\"\nW_KALES  = \"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%84%D8%B3%DA%A9%D9%87\"\nW_TELESM = \"https://en.wiktionary.org/wiki/%D8%B7%D9%84%D8%B3%D9%85\"\nW_APS    = \"https://en.wiktionary.org/wiki/%E1%BC%80%CF%88%CE%AF%CE%BD%CE%B8%CE%B9%CE%BF%CE%BD\"\nW_ESFY   = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%AF%DB%8C%D8%A7%D8%B1\"\nW_ESF    = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%81%D9%86%D8%AF\"\nW_KOLJ   = \"https://en.wiktionary.org/wiki/%D0%BA%D0%BE%D0%BB%D1%8F%D1%81%D0%BA%D0%B0\"\nA_KALES  = \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D9%84%D8%B3%DA%A9%D9%87/\"\nA_AFS    = \"https://abadis.ir/fatofa/%D8%A7%D9%81%D8%B3%D9%86%D8%AA%DB%8C%D9%86/\"\nA_TELESM = \"https://abadis.ir/fatofa/%D8%B7%D9%84%D8%B3%D9%85/\"\nA_SIL    = \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%84%D9%86%D8%AF%D8%B1/\"\n\nPOK_KWEL = (\"POK_full.txt, block ‘Root/lemma: kʷel-1, kʷelə-’, Meaning ‘to turn; wheel; neck?’, \"\n            \"Page(s): 639-640: ‘Latin colo, -ere “to till, tend, care for, cultivate” (*kʷelo), colonus, incolere “inhabit” … \"\n            \"collum “the neck” (*kʷol-so-, Gothic hals) … Old Church Slavic kolo, Gen. kolese “wheel” … \"\n            \"gr. κυκλος “circle” … Old English hweol (Germanic *hweh(w)ula-)’.\")\nAHD_KWEL = (\"AHD_watkins1985.txt s.v. kʷel-1: ‘To revolve, move around, sojourn, dwell. I. Basic form *kʷel- in Latin colere … \"\n            \"COLONY, CULT, CULTIVATE, (CULTURE) … II. Suffixed form *kʷel-es- in Greek telos, “completion of a cycle” … TALISMAN … \"\n            \"III. Suffixed reduplicated form *kʷ(e)-kʷl-o-, circle. 1. Germanic *hwewlaz in Old English hwēol, wheel: WHEEL. 2. Greek kuklos … CYCLE … \"\n            \"IV. O-grade form *kʷol-. 1. Suffixed form *kʷol-so-, “that on which the head turns”, neck … b. Latin collum, neck: COL, COLLAR … [Pok. 1. kʷel- 639.]’\")\n\ndata = {\n \"pdf_page\": 291,\n \"book_page\": 261,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ------------------------------------------------------------------ ENTRY 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Kwel, Qwel\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *kʷel- / *kʷelh₁- ‘to turn (end over end), revolve, move around; sojourn, dwell’ (Pokorny 1. kʷel-, kʷelə- 639–640)\",\n \"note\": (\"The root is real and the language label is right. Pokorny 639–640 gives 1. kʷel-, kʷelə- ‘drehen, sich drehen, sich herumbewegen, wohnen’ and \"\n   \"Watkins/AHD renders it ‘To revolve, move around, sojourn, dwell’ — Nourai’s gloss follows AHD word for word except that the printed page has lost the verb: \"\n   \"it reads ‘to, move around, dwell’. That is a misprint in the BOOK (verified on the page image), not an extraction error; the correct gloss is ‘to turn, move around, dwell’. \"\n   \"Second, POK:640 is exactly the page where Pokorny’s 1. kʷel- ends and where his separate 2. kʷel- ‘far (in space and time)’ (Greek tḗle) begins; \"\n   \"Nourai’s chart silently merges the two roots (his Greek box glosses telos ‘end of a cycle, far away’ and his English box lists tele-, telescope, television). \"\n   \"Pokorny, Watkins and Etymonline all keep them apart (*kʷel-1 vs *kʷel-2).\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *kʷel- (بازسازی امروزی: *kʷelh₁-) به معنی «چرخیدن، گردیدن، پیرامون چیزی گشتن و در نتیجه ماندن و سکونت گزیدن» است؛ \"\n   \"پوکورنی آن را در صفحهٔ ۶۳۹–۶۴۰ ذیل «۱. kʷel-» و واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ امریکن‌هریتیج با همین معنا آورده‌اند. \"\n   \"پس ریشه، برچسب زبانی و معنی در نمودار درست است. تنها در چاپ کتاب فعلِ turn از معنی افتاده و «to, move around, dwell» چاپ شده که خطای چاپی خودِ کتاب است و نه خطای خوانش اسکن. \"\n   \"نکتهٔ دوم آنکه صفحهٔ ۶۴۰ پوکورنی جایی است که ریشهٔ دومِ kʷel- به معنی «دور، دوردست» (یونانی tḗle) آغاز می‌شود؛ نورایی این دو ریشه را یکی گرفته است، حال آنکه \"\n   \"پوکورنی، واتکینز و اتیمانلاین آن دو را جدا می‌دانند.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"Kwel, Qwel : to, move around, dwell\",\n \"correct_form\": \"Kwel, Qwel : to turn, move around, dwell\",\n \"sources\": [W_KWEL, E_TALIS, E_TELE],\n \"ref_check\": [\n   {\"ref\": \"POK:640\", \"status\": \"supports\",\n    \"note\": (\"Pokorny p.639–640 ‘kʷel-1, kʷelə-’, Meaning ‘to turn; wheel; neck?’ (German original: ‘drehen, sich drehen, sich herumbewegen, wohnen’); \"\n             \"p.640 also carries ‘kʷel-2, Meaning: far (with regard to place and time)’ with Greek τῆλε. Found with grep -n 'Page(s): 64[0-2]' POK_full.txt \"\n             \"and printing the two blocks. Both of Nourai’s meanings sit on that page, but they belong to two different roots.\")}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 514 f. (q̩el- ‘drehen’; cited by Pokorny as ‘WP. I 514 f.’)\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd1_pages.txt, the q̩el- ‘drehen’ article: ‘Aisl. hvel n. ‚Rad‘ (= apr. kelan ds.; …)’; the same article expressly refuses Latin collum, referring it to q̩el- ‘ragen’ (see node 11).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kʷel-1 (= 1976 appendix)\", \"stance\": \"supports\", \"note\": AHD_KWEL},\n   {\"src\": \"SYN\", \"where\": \"Buck 10.76 WHEEL, pp.724–725\", \"stance\": \"supports\",\n    \"note\": \"‘IE *kʷelo-s, *kʷolo-s, redupl. *kʷekʷlo-s, fr. *kʷel- in Skt. car- “move, wander”, Grk. πέλομαι “be in motion”, etc. Walde-P. 1.514 ff.’ (grep -n '10.76 WHEEL' SYN.txt).\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Greek\", \"words\": \"ku-klos; telos; telesma\", \"verdict\": \"plausible\",\n  \"derivation\": (\"Greek kýklos ‘ring, circle, wheel’ is the reduplicated *kʷe-kʷl-o- of the root (Sanskrit cakra-, Avestan caxra-, OE hwēol are the same formation); \"\n   \"télos ‘end, fulfilment, completion’ goes back to a suffixed *kʷel-es-, the ‘turning point’ of a race-course, whence the verb teleîn ‘to perform (a rite), to pay’ and its \"\n   \"noun télesma ‘payment; consecration, completed rite’, which in Byzantine Greek came to mean ‘consecrated object, talisman’ — the sense Nourai glosses ‘mystery’. \"\n   \"So kýklos, télos and télesma are all correctly placed under *kʷel-1 (Watkins II–III). The second half of the gloss on telos, ‘far away’, is not télos but Greek tḗle \"\n   \"‘far off’, which Pokorny (640) and Watkins put under a homonymous root *kʷel-2 ‘far’; the node is therefore right in substance but conflates two roots.\"),\n  \"derivation_fa\": (\"یونانی kýklos «حلقه، چرخ» صورت مضاعف‌شدهٔ *kʷe-kʷl-o- از همین ریشه است (همان ساخت که سنسکریت cakra-، اوستایی caxra- و انگلیسی کهن hwēol را داده است). \"\n   \"télos «پایان، کمال» از *kʷel-es- است، یعنی «نقطهٔ گردش» میدان مسابقه؛ از آن فعل teleîn «آیین به‌جای آوردن، پرداختن» و اسمِ télesma «پرداخت؛ آیین کامل‌شده، تقدیس» ساخته شده که در یونانیِ بیزانسی معنی «طلسم» گرفت. \"\n   \"بنابراین هر سه واژه درست ذیل این ریشه نشسته‌اند. اما بخش دوم معنیِ telos یعنی «دوردست» به tḗle «دور» بازمی‌گردد که پوکورنی (ص ۶۴۰) و واتکینز آن را ریشهٔ جداگانه‌ای می‌دانند؛ \"\n   \"پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n  \"sources\": [E_TALIS, E_TELE, E_CYCLE],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_KWEL + \" — kuklos and telos (with TALISMAN) are both listed under kʷel-1; tḗle, however, is under kʷel-2 ‘Far (in space and time)’.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"639–640 (kʷel-1) and 640 (kʷel-2)\", \"stance\": \"partial\", \"note\": POK_KWEL + \" kʷel-2 p.640: ‘gr. τῆλε, Aeolic πήλυι “afar, wide”’ — a separate lemma.\"},\n    {\"src\": \"KLN\", \"where\": \"p.1596 s.v. talisman (KLN_1966.txt, grep -n '^talisman')\", \"stance\": \"supports\",\n     \"note\": \"‘F. talisman, fr. Sp. talisman, fr. VArab. tilsamān, pl. of tilsam, which corresponds to Classical Arabic ṭilasm, a loan word fr. Late Gk. τέλεσμα “consecration, mystery”, fr. Gk. τέλεσμα “payment”, fr. τελεῖν … fr. τέλος “fulfilment, end”.’\"},\n    {\"src\": \"LKT\", \"where\": \"no. 2077 (Talisman)\", \"stance\": \"supports\",\n     \"note\": \"‘‚Zauberbild‘ [aus gr. τέλεσμα], vulg.-ar. tilsam, pers. tilism, plr. tilismān; hieraus it. talismano, frz. sp. pg. talisman … russ. talisman.’\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Arabic\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Empty pass-through box: the Arabic link is ṭilasm / ṭilsam طلسم (pl. ṭalāsim, ṭilasmāt), a straight loan of Byzantine Greek télesma taken over with the Greek \"\n   \"occult-scientific literature translated in Baghdad in the 8th–10th c. (Ps.-Apollonius, the Ghāyat al-ḥakīm). Arabic re-analysed the unfamiliar noun on the pattern \"\n   \"fiʿlall (ṭ-l-s-m being treated as a quadriliteral root), which is why the word takes an Arabic broken plural although it has no Semitic etymology.\"),\n  \"derivation_fa\": (\"این خانهٔ خالی، حلقهٔ عربیِ زنجیره است: «طِلَسْم / طِلْسَم» وام‌واژهٔ مستقیمِ یونانیِ بیزانسی télesma است که همراه با ادبیات سحر و علوم غریبهٔ یونانی در سدهٔ دوم تا چهارم هجری به عربی ترجمه شد. \"\n   \"عربی این اسم بیگانه را بر وزن «فِعْلَل» تحلیل کرد و ط‑ل‑س‑م را ریشهٔ رباعی انگاشت؛ از همین‌رو جمع مکسر «طلاسم» گرفته است، هرچند ریشهٔ سامی ندارد. ادعای نورایی درست است.\"),\n  \"sources\": [W_TELESM, E_TALIS],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book; Klein p.1596, Lokotsch no.2077 and Wiktionary طلسم were checked instead (see consulted).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p.1596 s.v. talisman\", \"stance\": \"supports\", \"note\": \"‘… VArab. tilsamān, pl. of tilsam, which corresponds to Classical Arabic ṭilasm, a loan word fr. Late Gk. τέλεσμα’.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 2077\", \"stance\": \"supports\", \"note\": \"‘vulg.-ar. tilsam, pers. tilism, plr. tilismān’ — Lokotsch derives the Arabic word from Greek τέλεσμα exactly as the chart does.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"طلسم, Arabic section (etymology tree)\", \"stance\": \"supports\", \"note\": \"Etymology tree ‘Proto-Indo-European *kʷelh₁- > Proto-Hellenic *kʷélos > … τέλεσμα > Arabic طلسم’.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"telesm «طلسم»\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"New Persian طلسم ṭelesm / ṭelsam ‘talisman, spell’ is the Arabic ṭilasm re-borrowed into Persian in the Islamic period — a Greek word reaching Persian through \"\n   \"Arabic, not directly. Moʿin marks it ‘[ع. معر.]’, i.e. Arabic and itself an arabicised foreign word; Dehkhodā says outright that the word is Greek and not Arabic \"\n   \"(‘یونانی است، عربی نیست’, arguing from the impossible Arabic vocalisation ṭilism). The Persian plural طلسمات / طلاسم is taken over with the word.\"),\n  \"derivation_fa\": (\"«طلسم» در فارسی نو وام‌واژهٔ عربیِ «طِلَسْم» است که خود از یونانیِ متأخر télesma گرفته شده؛ یعنی واژه‌ای یونانی که از راه عربی (نه مستقیم) به فارسی رسیده است. \"\n   \"معین آن را با نشانهٔ «[ع. معرّ.]» ثبت کرده است و دهخدا صریح می‌گوید «یونانی است، عربی نیست، چه در تقدیر عربی بودن به کسرتین آمدن این لفظ وجهی ندارد». \"\n   \"جمع مکسر «طلاسم/طلسمات» نیز با خود واژه وام گرفته شده است. ادعای نورایی درست است.\"),\n  \"sources\": [A_TELESM, W_TELESM, E_TALIS],\n  \"ref_check\": [\n    {\"ref\": \"MON:2232\", \"status\": \"supports\",\n     \"note\": \"Moʿin, entry طلسم (local OCR MON_part1.txt, grep -n 'طلسم', lines 92984–92986): ‘[ع. معر.] (ا.) عمل خارق عادت که مبدأ آن را قوای فعال آسمانی … ج. طلسمات، طلاسم’ — the معرّب tag is Moʿin’s way of saying the word is a foreign word arabicised, i.e. Nourai’s Greek>Arabic>Persian route. (The printed page number 2232 cannot be checked: the local Moʿin scan is the 2-vol. abridgement without the 6-vol. pagination.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"abadis.ir طلسم, section فرهنگ معین / لغت‌نامه دهخدا\", \"stance\": \"supports\",\n     \"note\": \"‘یونانی طلسما …’ and ‘یونانی τέλεσμα (telesma) است به معنی «تکمیل، آیین مذهبی، پرداخت»، که از طریق عربی طلسم وارد فارسی شده است’.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 2077\", \"stance\": \"supports\", \"note\": \"explicitly lists ‘pers. tilism’ beside vulgar-Arabic tilsam.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Empty pass-through box standing for the modern French vehicles of the Greek words: cycle, cylindre, encyclopédie, télescope, télévision, télégraphe. \"\n   \"French is historically the right intermediary for Persian: European technical vocabulary entered Persian through French from the Qājār period on (Dār al-Fonūn, founded 1851; \"\n   \"the first telegraph lines in Iran, 1858–64), and Moʿin tags exactly these words ‘[فر.]’ = French.\"),\n  \"derivation_fa\": (\"این خانهٔ خالی نمایندهٔ صورت‌های فرانسویِ همان واژه‌های یونانی است: cycle، cylindre، encyclopédie، télescope، télévision، télégraphe. \"\n   \"از نظر تاریخی فرانسه واسطهٔ درستی است: واژگان فنیِ اروپایی از دورهٔ قاجار (تأسیس دارالفنون در ۱۲۳۰ ش/۱۸۵۱ و کشیدن نخستین خطوط تلگراف در ۱۸۵۸–۶۴) از راه فرانسه وارد فارسی شد \"\n   \"و معین نیز همین واژه‌ها را با نشانهٔ «[فر.]» ثبت کرده است.\"),\n  \"sources\": [A_SIL, E_CYCLE],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The box carries no reference; checked Moʿin (via abadis) on سیلندر and Etymonline instead (see consulted).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"abadis.ir سیلندر, section فرهنگ معین\", \"stance\": \"supports\", \"note\": \"‘[فر. ] (ا. ) ۱ - لوله‌ای است استوانه‌ای شکل که در موتور اتومبیل تعبیه شده …’ — Moʿin’s ‘[فر.]’ tag = borrowed from French.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. cycle / cylinder (KLN_1966)\", \"stance\": \"partial\", \"note\": \"Klein routes cycle through Late Latin cyclus and French, and cylinder through Old French cylindre < Latin cylindrus; the French stage is right, the ultimate root is not the same for both (see node 6).\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Persian\", \"words\": \"سیکل ، سیلندر ، تلسکوپ ، تلویزیون ، تلگراف\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"The five Persian words are 19th–20th-c. French loans, and the French spelling shows through: سیکل sikl < cycle, سیلندر silandr < cylindre \"\n   \"(French -indre, not English -inder), تلسکوپ teleskop < télescope, تلویزیون televizyon < télévision (the -zy- of televizyon renders French -vis-), \"\n   \"تلگراف telegrāf < télégraphe. Moʿin tags them ‘[فر.]’. The chart is right that they came through French; it is only their ultimate PIE root that is mixed \"\n   \"(télé- belongs to *kʷel-2 ‘far’, and cylindre to Greek kulíndein ‘to roll’, of unknown origin — see node 6).\"),\n  \"derivation_fa\": (\"این پنج واژه وام‌واژه‌های فرانسویِ سدهٔ نوزدهم و بیستم‌اند و املای فرانسوی در آنها پیداست: «سیکل» از cycle، «سیلندر» از cylindre (نه انگلیسیِ cylinder)، \"\n   \"«تلسکوپ» از télescope، «تلویزیون» از télévision و «تلگراف» از télégraphe. معین همه را با نشانهٔ «[فر.]» آورده است. \"\n   \"پس در باب راه وام‌گیری ادعای نورایی درست است؛ تنها ریشهٔ نهایی یکدست نیست: جزء télé- به ریشهٔ دومِ kʷel- «دور» بازمی‌گردد و cylindre از kulíndein یونانی «غلتاندن» است که ریشهٔ آن ناشناخته است.\"),\n  \"sources\": [A_SIL, E_CYL, E_TELE],\n  \"ref_check\": [\n    {\"ref\": \"MON\", \"status\": \"supports\",\n     \"note\": \"Moʿin s.v. سیلندر (abadis.ir, فرهنگ معین): ‘[فر.] (ا.)…’ — the French tag is exactly Nourai’s arrow. The citation has no page number, so nothing further can be pinned down.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"abadis.ir سیلندر (فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"‘[فر. ] (ا. )’ = from French.\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. cylinder\", \"stance\": \"partial\", \"note\": \"‘from Old French cylindre (14c.) and directly from Latin cylindrus … from Greek kylindein “to roll”, which is of unknown origin’ — the French stage is right, the root assignment is not.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"English\", \"words\": \"cycle, cylinder, encyclopedia; tele-, teletype, telescope, television, telegraph\", \"verdict\": \"disputed\",\n  \"derivation\": (\"Three claims, of different quality. (a) cycle (late 14c. cicle, via Old French cicle / Late Latin cyclus from kýklos) and encyclopedia (from enkýklios paideía \"\n   \"‘all-round education’, the enkýklios part being kýklos) are correctly from *kʷel-1: Watkins lists CYCLE, CYCLO-, BICYCLE, ENCYCLICAL under kʷel-1. \"\n   \"(b) The tele- words are from Greek tḗle ‘far off’, which Watkins and Pokorny put under the homonym *kʷel-2 ‘far (in space and time)’ (Pok. 640) — related but not the same root; \"\n   \"telescope and telegraph are besides compounds whose second elements belong elsewhere (Watkins files TELESCOPE under spek-). \"\n   \"(c) cylinder is wrong: it is Latin cylindrus < Greek kýlindros, from kulíndein ‘to roll’, ‘which is of unknown origin’ (Etymonline); Watkins files CYLINDER under (s)kel-3, \"\n   \"not under kʷel-. Because one word of the box is referred to a different origin by the standard authorities, the node is scored disputed.\"),\n  \"derivation_fa\": (\"این خانه سه ادعای متفاوت دارد. یکم: cycle (از راه فرانسهٔ کهن و لاتین متأخر cyclus از kýklos) و encyclopedia (از enkýklios paideía «آموزش همه‌جانبه») به‌درستی از همین ریشه‌اند و واتکینز نیز آنها را ذیل kʷel-1 آورده است. \"\n   \"دوم: واژه‌های tele- از tḗle یونانی «دور» است که پوکورنی (ص ۶۴۰) و واتکینز آن را ریشهٔ همنامِ دیگری (kʷel-2 «دور») می‌دانند؛ افزون بر این، جزء دومِ telescope و telegraph ریشهٔ دیگری دارد. \"\n   \"سوم: cylinder نادرست است؛ از لاتین cylindrus و یونانی kýlindros از فعل kulíndein «غلتاندن» است که ریشهٔ آن ناشناخته است و واتکینز آن را ذیل (s)kel- ثبت کرده، نه kʷel-. \"\n   \"پس پژوهش امروزی دست‌کم یکی از واژه‌های این خانه را رد می‌کند.\"),\n  \"sources\": [E_CYCLE, E_CYL, E_TELE],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The English box has no reference of its own; checked Watkins/AHD, Klein and Etymonline instead (see consulted).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, index of English derivatives\", \"stance\": \"contradicts\",\n     \"note\": \"‘CYCLE kʷel-1 … CYCLO- kʷel-1’ and ‘ENCYCLICAL kʷel-1’ but ‘CYLINDER skel-3’, ‘TELE- kʷel-2’, ‘TELESCOPE spek-’, ‘ENCYCLOPEDIA pau-’; CLOWN does not appear in the index at all (grep -o 'CYLINDER [a-z-]*' AHD_watkins1985.txt).\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. cylinder; cycle; tele-\", \"stance\": \"partial\",\n     \"note\": \"cycle ‘from Greek kyklos … from PIE kʷ(e)-kʷl-o-, a suffixed, reduplicated form of the root *kʷel- (1)’; cylinder ‘from Greek kylindein “to roll”, which is of unknown origin’; tele- ‘from Greek tēle “far off” … from PIE root *kʷel- (2) “far”’.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. talisman / tele- (KLN_1966)\", \"stance\": \"partial\", \"note\": \"Klein groups τέλος and τῆλε together (‘fr. τέλος “fulfilment, end”. See tele-’), i.e. the older handbooks did what Nourai does; Pokorny 1959 and Watkins separate them.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Russian\", \"words\": \"koleso; kaljaska\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Russian колесо́ kolesо́ ‘wheel’ continues Old Church Slavonic коло kolo, gen. колесе kolese (an s-stem), from *kʷol-es-/*kʷolo-, the o-grade of the root, \"\n   \"with Slavic *kʷ > k before back vowels; the plural кола kola meant ‘cart’. коля́ска koljáska ‘light carriage’ is a diminutive of the same коло, recorded in Russian from \"\n   \"1695 (Vasmer: каслика) and taken over from Polish kolaska / kolasa ‘carriage’ — so also from *kʷel-, as the chart says, though through a West-Slavic detour.\"),\n  \"derivation_fa\": (\"روسی колесо́ «چرخ» دنبالهٔ اسلاوی کلیسایی kolo با حالت اضافهٔ kolese است، از صورت آواگردیدهٔ *kʷol-es- همین ریشه؛ در اسلاوی kʷ پیش از واکه‌های پسین به k بدل شده است. \"\n   \"коля́ска «کالسکه» مصغّرِ همان kolo است که به گواهی فاسمر از سال ۱۶۹۵ در روسی ثبت شده و از لهستانی kolaska/kolasa گرفته شده است. \"\n   \"پس هر دو واژه به‌درستی از همین ریشه‌اند، هرچند دومی از راه اسلاویِ غربی وارد روسی شده است.\"),\n  \"sources\": [W_KOLJ],\n  \"ref_check\": [\n    {\"ref\": \"SYN:724\", \"status\": \"supports\",\n     \"note\": \"Buck 10.76 WHEEL (pp.724–725): ‘IE *kʷelo-s, *kʷolo-s, redupl. *kʷekʷlo-s … ChSl., SCr., Boh. kolo, Pol. koło, Russ. koleso; Grk. κύκλος …’ (grep -n '10.76 WHEEL' SYN.txt; the page footer of the following column reads ‘… TRANSPORTATION, NAVIGATION 725’).\"},\n    {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins kʷel-1 gives the wheel-word family (*kʷ(e)-kʷl-o-) but has no Russian entry; the Slavic material is in Pokorny and Buck.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"639–640\", \"stance\": \"supports\", \"note\": \"‘Old Church Slavic kolo, Gen. kolese “wheel”, Pl. kola “cart” (mixture from *kʷolo- m. and *kʷeles- n.)’.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"коля́ска\", \"stance\": \"supports\", \"note\": \"‘Ultimately from Proto-Slavic *kolo. According to Vasmer, this word was documented in Old Russian since 1695 as каслика. It is cognate with Polish kolasa.’\"},\n    {\"src\": \"KLN\", \"where\": \"p.222 s.v. calash\", \"stance\": \"partial\", \"note\": \"‘F. calèche, fr. Czech kolesa “wheels, carriage”, pl. of koleso “wheel”, fr. kolo “wheel” … cogn. with Gk. κύκλος’ — same root, Czech rather than Russian for the French word.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"Persian\", \"words\": \"kâleskeh «کالسکه»\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Persian کالسکه kāleske ‘four-wheeled horse carriage’ is a Qājār-period loan of Russian коля́ска koljáska, taken over through the Russian court and army contacts of \"\n   \"the early 19th c.; Russian -яска [-ʲaskə] was rendered ـلسکه -leske and the stressed о- was lengthened to Persian ā-. Wiktionary states flatly ‘From Russian коля́ска’, \"\n   \"Moʿin tags it ‘[روس.]’ and Dehkhodā quotes ‘از کلمه کالسکای روسی گرفته شده است’. The word therefore reaches Persian from the same PIE root by a wholly different road \"\n   \"from طلسم, which is the point of the chart.\"),\n  \"derivation_fa\": (\"«کالسکه» وام‌واژهٔ روسیِ коля́ска است که در دورهٔ قاجار از راه مناسبات درباری و نظامی با روسیه وارد فارسی شد؛ پایانهٔ روسی -яска به «ـلسکه» و واکهٔ تکیه‌دار o به «ا»ی کشیده بدل شده است. \"\n   \"ویکی‌واژه صریح می‌گوید «از روسی коля́ска»، معین آن را «[روس.]» نشانه زده و دهخدا می‌نویسد «از کلمهٔ کالسکای روسی گرفته شده است». \"\n   \"پس این واژه از همان ریشهٔ هندواروپایی است اما از راهی یکسره متفاوت با «طلسم» به فارسی رسیده و ادعای نورایی درست است.\"),\n  \"sources\": [W_KALES, A_KALES],\n  \"ref_check\": [\n    {\"ref\": \"MON:2861\", \"status\": \"supports\",\n     \"note\": \"Moʿin s.v. کالسکه: local OCR MON_part2.txt line 19280 has the headword with a bracketed origin tag and Latin transliteration (OCR-garbled); the same Moʿin entry read on abadis.ir gives ‘[ روس . ] (اِ. ) ۱ - اتاقکی که دارای چهار چرخ می‌باشد …’ — ‘[روس.]’ = from Russian, exactly Nourai’s arrow. Page 2861 itself cannot be checked (local Moʿin scan is the 2-vol. abridgement).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"Wiktionary\", \"where\": \"کالسکه (Persian)\", \"stance\": \"supports\", \"note\": \"‘From Russian коля́ска (koljáska).’ with an etymology tree PIE *kʷelh₁- > Proto-Slavic *kolo > Russian коля́ска > Persian کالسکه.\"},\n    {\"src\": \"MON\", \"where\": \"abadis.ir کالسکه (فرهنگ معین + لغت‌نامه)\", \"stance\": \"supports\", \"note\": \"‘روسی، از کلمه کالسکای روسی گرفته شده است’ (یادداشت مؤلف)؛ ‘مأخوذ از روسی، گردون چهارچرخه اطاق‌دار’ (ناظم‌الاطباء).\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"German\", \"words\": \"hwe-hula\", \"verdict\": \"plausible\",\n  \"derivation\": (\"The form is right but the label is not. ‘hwe-hula’ is Nourai’s spelling of Proto-Germanic *hweh(w)ula- / *hwewlaz ‘wheel’, the regular Germanic outcome of the \"\n   \"reduplicated *kʷe-kʷl-o- (PIE *kʷ > Gmc. *hw by Grimm’s Law, the second *kʷ lost between vowels). That is a reconstructed PROTO-GERMANIC form, not German: \"\n   \"modern German for ‘wheel’ is Rad, from an entirely different root (*Hret-). Nourai himself writes ‘Germanic’ correctly in the Kwen 1 chart on the same page, so the label here is \"\n   \"loose usage in the book, not a mis-scan. With that reservation the derivation is exactly Watkins’ and Pokorny’s.\"),\n  \"derivation_fa\": (\"صورت درست است اما برچسب زبانی نه. «hwe-hula» همان *hweh(w)ula- / *hwewlaz ژرمنیِ آغازین به معنی «چرخ» است که بازتاب قانونمندِ *kʷe-kʷl-o- مضاعف است \"\n   \"(kʷ هندواروپایی بنابر قانون گریم در ژرمنی به hw بدل شده و kʷ دوم میان دو واکه افتاده است). این صورت بازسازی‌شدهٔ ژرمنی آغازین است، نه آلمانی؛ «چرخ» در آلمانیِ امروز Rad است و ریشهٔ دیگری دارد. \"\n   \"خودِ نورایی در نمودار Kwen 1 در همین صفحه درست «Germanic» نوشته است، پس این بی‌دقتی از کتاب است نه از خوانش اسکن. با این قید، اشتقاق دقیقاً همان است که واتکینز و پوکورنی می‌گویند.\"),\n  \"sources\": [E_WHEEL],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins kʷel-1, III.1: ‘Germanic *hwewlaz in Old English hwēol, hweogol, wheel: WHEEL.’ — the reconstruction Nourai writes as hwe-hula; Watkins labels it Germanic, not German.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"639–640\", \"stance\": \"supports\", \"note\": \"‘Old Icelandic hjól, hvel (*kʷekʷelon-, Germanic *hweh(w)ula-) n., Old English hweol … besides hweowol, hweogol (Germanic *hweg(w)ula-)’.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 10.76, p.724\", \"stance\": \"supports\", \"note\": \"lists ON hvel, OE hwēol, ME hwele, NE wheel, Du. wiel under the same *kʷel- family; German rad is listed separately.\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. wheel\", \"stance\": \"supports\", \"note\": \"‘from Old English hweol, hweogol, from Proto-Germanic *hwewlaz … from PIE *kʷ(e)-kʷl-o- “wheel, circle”, suffixed, reduplicated form of root *kʷel- (1)’.\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"English\", \"words\": \"wheel\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Old English hwēol / hweogol > Middle English whele > Modern English wheel, from Proto-Germanic *hwewlaz, PIE *kʷ(e)-kʷl-o-. The English word is thus the exact \"\n   \"cognate of Greek kýklos and Sanskrit cakra-, and the modern spelling wh- preserves the Germanic *hw- of Grimm’s Law.\"),\n  \"derivation_fa\": (\"انگلیسی کهن hwēol/hweogol از راه انگلیسی میانهٔ whele به wheel امروزی رسیده است، از ژرمنی آغازین *hwewlaz و در نهایت از *kʷ(e)-kʷl-o- هندواروپایی. \"\n   \"بنابراین wheel هم‌ریشهٔ مستقیم kýklos یونانی و cakra- سنسکریت است و املای wh- همان hw- ژرمنی (نتیجهٔ قانون گریم) را نگاه داشته است. ادعای نورایی درست است.\"),\n  \"sources\": [E_WHEEL],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no reference on the box; checked Watkins/AHD (‘Old English hwēol, wheel: WHEEL’), Pokorny 639–640 and Buck 10.76 instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kʷel-1 III.1\", \"stance\": \"supports\", \"note\": \"‘Germanic *hwewlaz in Old English hwēol, hweogol, wheel: WHEEL.’\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 10.76 WHEEL p.724\", \"stance\": \"supports\", \"note\": \"‘OE hwéol, ME hwele, whele, NE wheel’ in the *kʷelo-s group.\"}\n  ]\n },\n {\n  \"id\": 11, \"lang\": \"Latin\", \"words\": \"col-ere; col-lum\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Latin colō, colere ‘to till, tend, cultivate; to inhabit, dwell in’ is the plain e-grade *kʷel-o- (with *kʷ > c before a back vowel); the ‘inhabit’ sense that Nourai \"\n   \"glosses is the one preserved in incolere ‘to dwell in’, incola ‘inhabitant’, inquilinus. collum (older collus) ‘neck’ is *kʷol-so-, o-grade + -so-, literally ‘that on which the head \"\n   \"turns’, the exact cognate of Gothic/Old Norse hals. The second etymology is not unanimous: Walde-Pokorny (1927) referred collum to a homonymous *kʷel- ‘ragen, to rise’ \"\n   \"(with collis, celsus), and Ernout-Meillet leave the choice open while leaning to ‘turn’ (‘en faveur de la seconde hypothèse … lit. kaklas “cou” dont la ressemblance avec gr. \"\n   \"κύκλος est frappante’). Pokorny 1959, Watkins and Etymonline all put collum under *kʷel-1, so the chart follows the current standard.\"),\n  \"derivation_fa\": (\"لاتین colō/colere «کِشت کردن، پروردن؛ ساکن بودن» همان درجهٔ آواییِ *kʷel-o- است (kʷ پیش از واکهٔ پسین در لاتین به c بدل شده)؛ معنی «سکونت» که نورایی آورده در incolere «در جایی زیستن»، incola «ساکن» و inquilinus بازمانده است. \"\n   \"collum «گردن» از *kʷol-so- است، یعنی «آنچه سر بر آن می‌چرخد»، و هم‌ریشهٔ دقیقِ hals گوتی و نورس کهن. این اشتقاق دوم یکدست پذیرفته نیست: والده–پوکورنی (۱۹۲۷) collum را به ریشهٔ همنامِ kʷel- «برآمدن» می‌برد و ارنو–مییه میان دو رأی می‌مانند اما به «چرخیدن» گرایش دارند \"\n   \"(با استناد به kaklas لیتوانیایی «گردن» در برابر κύκλος یونانی). پوکورنیِ ۱۹۵۹، واتکینز و اتیمانلاین هر سه collum را ذیل kʷel-1 آورده‌اند، پس نمودار با معیار امروزی هماهنگ است.\"),\n  \"sources\": [E_COLONY, E_COLLAR],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins kʷel-1: ‘I. Basic form *kʷel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUILINE, SILVICOLOUS. … IV.1.b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE, DECOLLETE, MACHICOLATE, TORTICOLLIS.’\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"639–640\", \"stance\": \"supports\", \"note\": \"‘Latin colo, -ere “to till, tend, care for, cultivate” (*kʷelo); colonus; incolere “inhabit”, incola … collus, -ī m. (Old Latin), collum, -ī n. “the neck” (*kʷol-so-, Gothic hals)’.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. collum, colō\", \"stance\": \"partial\",\n     \"note\": \"‘Collus est issu de *kol-so-s … Cf. got. hals “cou”. On s’est demandé si ce mot est à rattacher au groupe de *kel- “en haut” … ou à celui de *kʷel- “tourner” … En faveur de la seconde hypothèse … lit. kaklas “cou” dont la ressemblance avec gr. κύκλος “cercle” est frappante.’ The colo article gives incola, agricola, colonus, colonia, cultura.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 449 (q̩el- ‘ragen’) vs I 514 f. (q̩el- ‘drehen’)\", \"stance\": \"contradicts\",\n     \"note\": \"‘gegen Verb. mit q̩ʷel- ‚drehen‘ als ‚Säule, Träger des Kopfes‘ … lat. collus, collum ‚Hals‘ = got. aisl. ahd. hals’ — Walde-Pokorny deliberately keep collum away from the ‘turn’ root; Pokorny reversed this in 1959.\"}\n  ]\n },\n {\n  \"id\": 12, \"lang\": \"English\", \"words\": \"colony, culture, clown; collar\", \"verdict\": \"disputed\",\n  \"derivation\": (\"colony (late 14c., ‘Roman settlement’, < Latin colonia < colonus < colere) and culture (< cultura, the verbal noun of colere) are straightforwardly from the Latin box, \"\n   \"as is collar (c.1300 coler < Old French coler < Latin collāre ‘band for the neck’ < collum). clown, however, is not: it appears in the 1560s as clowne/cloyne ‘rustic, boor’, \"\n   \"of obscure origin, most probably Scandinavian or Low German (Icelandic klunni ‘clumsy fellow’, Swedish kluns, North Frisian klönne), and the OED glosses the base as ‘clod, clot, lump’. \"\n   \"Etymonline states expressly that ‘the theory that it is from Latin colonus “colonist, farmer” is less likely, but awareness of the Latin word might have influenced the sense development’; \"\n   \"Watkins does not list CLOWN in the index of IE derivatives at all. The node is therefore scored disputed on account of clown.\"),\n  \"derivation_fa\": (\"colony (سدهٔ چهاردهم، از colonia لاتین < colonus < colere) و culture (از cultura، اسم مصدرِ colere) و همچنین collar (از فرانسهٔ کهن coler < لاتین collāre < collum) به‌درستی از خانهٔ لاتینِ بالا می‌آیند. \"\n   \"اما clown چنین نیست: این واژه در دههٔ ۱۵۶۰ به صورت clowne/cloyne به معنی «روستایی، خشن» پیدا می‌شود و ریشهٔ آن ناشناخته است؛ به احتمال زیاد اسکاندیناویایی یا آلمانیِ سفلی است \"\n   \"(ایسلندی klunni «آدم دست‌وپاچلفتی»، سوئدی kluns، فریزیِ شمالی klönne). اتیمانلاین صریح می‌گوید نظریهٔ اشتقاق از colonus لاتین «کم‌احتمال‌تر» است و واتکینز اصلاً CLOWN را در فهرست مشتقات هندواروپایی نیاورده است. \"\n   \"پس پژوهش امروزی این جزء از ادعای نورایی را رد می‌کند و آن را ریشه‌شناسی عامیانه می‌داند.\"),\n  \"sources\": [E_COLONY, E_COLLAR, E_CLOWN],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no reference on the box; checked Watkins/AHD index, Etymonline and Klein instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, index\", \"stance\": \"contradicts\", \"note\": \"‘COLONY kʷel-1’, ‘CULTURE kʷel-1’, ‘CULTIVATE kʷel-1’, ‘COLLAR kʷel-1’ are all there — but CLOWN has no entry in the index at all (grep -o 'CLOWN [A-Za-z-]*' AHD_watkins1985.txt returns nothing).\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.vv. colony, collar, clown\", \"stance\": \"contradicts\",\n     \"note\": \"colony ‘from Latin colonia … from colere … from PIE root *kʷel- (1)’; collar ‘from Latin collāre … from collum “the neck”, from PIE *kʷol-o-’; clown ‘a word of obscure origin … Perhaps from Scandinavian dialect … The theory that it is from Latin colonus “colonist, farmer” is less likely’.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966, grep -n '^clown'\", \"stance\": \"silent\", \"note\": \"the local Klein OCR has no retrievable ‘clown’ headword line (the two-pages-per-leaf scan runs the entries together), so Klein could not be quoted for this word.\"}\n  ]\n }\n]\ndata[\"entries\"].append(e0)\njson.dump(data, open('/tmp/e0-291.json','w'), ensure_ascii=False, indent=1)\nprint(\"entry0 ok\", len(e0[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build291.py",
 "description": "Build entry 0 of verification"
}
```


### [2026-09-06T22:25:42.399Z] TOOL RESULT

```
entry0 ok 12
```


## [2026-09-06T22:25:54.832Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nleaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf\n    leaf+=l.count('\\f')\nfor n,name in [(1241,'absinth'),(6134,'calash'),(18149,'housel'),(38052,'talisman')]:\n    lf=m[n]\n    print(name,'line',n,'leaf',lf,'=> printed p ~',(lf-12)*2,'-',(lf-12)*2+1)\nEOF",
 "description": "Compute Klein printed pages"
}
```


### [2026-09-06T22:25:56.986Z] TOOL RESULT

```
absinth line 1241 leaf 15 => printed p ~ 6 - 7
calash line 6134 leaf 127 => printed p ~ 230 - 231
housel line 18149 leaf 402 => printed p ~ 780 - 781
talisman line 38052 leaf 830 => printed p ~ 1636 - 1637
```


## [2026-09-06T22:26:13.133Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (400,401,402,403):\n    seg=pages[i]\n    print('--- leaf',i,'---', repr(seg[:160]))\n    print('   tail:', repr(seg[-160:]))\nEOF",
 "description": "Look for page numbers in Klein scan"
}
```


### [2026-09-06T22:26:15.429Z] TOOL RESULT

```
--- leaf 400 --- '  —  L.  Horatius  (see  Horace); influenced  in  form  by  It.  Orazio,  which  is  of the  same  origin.\nhorde,  n.,  1)  a  wandering  tribe;  2)  a  multitu'
   tail: 'tatio,  gen. -dnis,  ‘encouragement,  exhortation’,  fr.  hor- tatus,  pp.  of  hortari,  ‘to  urge,  incite,  instigate, encourage,  exhort’,  freq.  of  horio'
--- leaf 401 --- 'r,  gen.  horiri, ‘to  urge,  incite,  encourage,  exhort’,  fr.  I.-E.  base *gher-,  ‘to  desire’,  whence  also  OE.  geornan, giernan,  ‘to  desire’.  See  '
   tail: '’,  and  perh.  also  Russ. suka,  ‘bitch’.  Cp.  Gk.  arnkSaxeq  (Hesychius),\n‘dogs’,  which  seems  to  be  metathesized  fr. *CT7raxa8£4,  fr.  Medean  spdka'
--- leaf 402 --- '.  Cp.  the  second element  in  dachshund,  keeshond.Cp.  also  canaille, Canidae,  canine,  Canis,  chenille,  kennel,  ‘shelter for  a  dog’,  and  the  firs'
   tail: ' origin;  cp.  ON.  haugr,  ‘mound’, OSwed.  hugli,  ‘hill’,  and  see  high.  Cp.  also  how, ‘a  mound’.\nDerivatives:  huge-ous,  adj.,  huge-ous-ly,  adv., h'
--- leaf 403 --- 'uge-ous-ness,  n,,  hug-y,  adj. huggermugger,  adv.,  secretly.  —  Fr.  earlier  hucker mucker-,  of  unknown  origin.\nDerivatives:  huggermugger,  n.,  adj. '
   tail: "berance.  —  Of  LG. origin.  Cp.  MLG.  hump,  ‘bump,  hunch’,  Du. homp,  ‘lump,  chunk’,  Norw.  hump,  'knoll'. These  words  derive  fr.  I.-E.  base  *qum"
```


## [2026-09-06T22:26:30.003Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in (178,380,385,438,439):\n    print('--- leaf',i,'---', repr(pages[i][:120]))\nEOF",
 "description": "Check Klein leaf anchors"
}
```


### [2026-09-06T22:26:32.060Z] TOOL RESULT

```
903
--- leaf 178 --- ' coeno-).  Cp.  1st  con-,  contra-, count,  ‘title  of  nobility’.  Cp.  also  y-. coma,  n.,  a  state  of  insensibil'
--- leaf 380 --- 'eetest,  loveliest’  (superl.  of  obsol.  &Xtco?, SXtvKxf),  fr.  I.-E.  *wjp-,  zero  degree  of  base * welp-,  whenc'
--- leaf 385 --- ' resp.  OFris.  hod,  OHG.  huota,  MHG. huole,  G.  Hut,  ‘protection,  care’,  OE.  hod, ‘hood’.  See  hood.\nheed,  n.'
--- leaf 438 --- ' —  ModL.,  fr.  Gk.  eEpeauovr),  ‘a wreath  of  olive  wound  round  with  wool’,  fr. slpo q,  ‘wool’,  which  is  re'
--- leaf 439 --- 'e,  adj.  —  Formed  with  suff.  -ive  fr.  L.\nirrigatus,  pp.  of  irrigare.  See  irrigate, irriguous,  adj.,  moist,'
```


## [2026-09-06T22:26:50.774Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(378,406):\n    seg=pages[i]\n    hits=[w for w in ('sp^nta','splnta','spenta','hunsl','svetu','svehtas','sventas','Avestic') if w in seg]\n    if hits: print(i, 2*i-23, hits, ' | ', ' '.join(seg.split()[:8]))\nEOF",
 "description": "Search Klein leaves for spenta/hunsl"
}
```


### [2026-09-06T22:26:53.124Z] TOOL RESULT

```
381 739 ['Avestic']  |  aepse. See hasp, n. hassock, n., a small
383 743 ['Avestic']  |  Swed. huvud, OFris. haved, hafd, MDu. ho vet,
385 747 ['Avestic']  |  resp. OFris. hod, OHG. huota, MHG. huole, G.
388 753 ['Avestic']  |  mean lit. ieaper, jumper’, fr. T.-E. base *kaq-,
392 761 ['Avestic']  |  d’, compounded of e^a- (see hexa-) and 77064,
394 765 ['Avestic']  |  r. Hind, ‘India’, fr. OI. Sindhuh, ‘the river
396 769 ['Avestic']  |  hough, hoch, fr. OE. hoh, ‘heel’, rel. to
398 773 ['Avestic']  |  . of opIXsiv, ‘to be together with, converse
399 775 ['Avestic']  |  ed from it). See honey and suck. hong,
400 777 ['Avestic']  |  — L. Horatius (see Horace); influenced in form
401 779 ['Avestic']  |  r, gen. horiri, ‘to urge, incite, encourage, exhort’,
402 781 ['splnta', 'hunsl', 'svetu', 'svehtas', 'Avestic']  |  . Cp. the second element in dachshund, keeshond.Cp.
404 785 ['Avestic']  |  b-, ’to bend, curve', whence also OI. kumbhdh,
405 787 ['Avestic']  |  Formed fr. husk with adj. suff. -y. Derivatives:
```


## [2026-09-06T22:27:15.894Z] TOOL CALL #93: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport re\np='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build291.py'\ns=open(p,encoding='utf-8').read()\ns=s.replace('\"where\": \"p.1596 s.v. talisman (KLN_1966.txt, grep -n \\'^talisman\\')\"','\"where\": \"s.v. talisman, KLN_1966.txt line 38052 = leaf 830 ≈ printed p.1633\"')\ns=s.replace('\"where\": \"p.1596 s.v. talisman\"','\"where\": \"s.v. talisman, KLN_1966.txt leaf 830 ≈ printed p.1633\"')\ns=s.replace('\"where\": \"p.222 s.v. calash\"','\"where\": \"s.v. calash, KLN_1966.txt line 6134 = leaf 127 ≈ printed p.231\"')\ns=s.replace(\"json.dump(data, open('/tmp/e0-291.json','w'), ensure_ascii=False, indent=1)\\nprint(\\\"entry0 ok\\\", len(e0[\\\"nodes\\\"]))\",\"\")\nopen(p,'w',encoding='utf-8').write(s)\nprint('patched')\nPYEOF\ngrep -n \"leaf 830\\|leaf 127\\|json.dump\" /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build291.py",
 "description": "Patch Klein page refs and remove dump"
}
```


### [2026-09-06T22:27:17.650Z] TOOL RESULT

```
patched
99:    {"src": "KLN", "where": "s.v. talisman, KLN_1966.txt line 38052 = leaf 830 ≈ printed p.1633", "stance": "supports",
117:    {"src": "KLN", "where": "s.v. talisman, KLN_1966.txt leaf 830 ≈ printed p.1633", "stance": "supports", "note": "‘… VArab. tilsamān, pl. of tilsam, which corresponds to Classical Arabic ṭilasm, a loan word fr. Late Gk. τέλεσμα’."},
218:    {"src": "KLN", "where": "s.v. calash, KLN_1966.txt line 6134 = leaf 127 ≈ printed p.231", "stance": "partial", "note": "‘F. calèche, fr. Czech kolesa “wheels, carriage”, pl. of koleso “wheel”, fr. kolo “wheel” … cogn. with Gk. κύκλος’ — same root, Czech rather than Russian for the French word."}
```


## [2026-09-06T22:27:19.410Z] AGENT

Now entry 1.


## [2026-09-06T22:30:44.777Z] TOOL CALL #94: Bash

```json
{
 "command": "cat >> /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build291.py <<'PYEOF'\n\n# ------------------------------------------------------------------ ENTRY 1\nKLN746 = (\"KLN_1966.txt line 18149 (leaf 402 ≈ printed p.781) s.v. housel: ‘housel, n., the Eucharist (obsol.) — ME. husel, fr. OE. husel, \"\n \"“the Eucharist”, rel. to ON. husl, of s.m., Goth. hunsl, “sacrifice”, and prob. cogn. with Lith. šventas, OSlav. svętŭ, OPruss. swints, “holy”, \"\n \"Lett. svinēt, “to hallow, celebrate”, Avestic spənta-, “holy”.’ — exactly Nourai’s two arrows (Avestan spənta- and Germanic *hunslam under one root).\")\nPOK630 = (\"POK_full.txt, block ‘Root / lemma: k̑u̯en-’, Meaning ‘to celebrate; saint’, Page(s): 630: ‘Avestan spənta- “holy” (= Lithuanian šventas, \"\n \"Old Church Slavic svętъ “holy”), compounds Superl. Avestan span-yah-, spəništa- “sacred, holiest”, es-stem Avestan spanah- n. “holiness”; \"\n \"probably Gothic hunsl n. “sacrifice, oblation”, Old English husl n. “sacrament” (*k̑un-s-lo-) …’ (grep -n 'Page(s): 63[0-9]' POK_full.txt).\")\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Kwen 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱwen-to- ‘holy’ (root *ḱwen- ‘to celebrate, hallow’; Pokorny k̑u̯en- 630, Walde-Pokorny I 471, Watkins kʷen-)\",\n \"note\": (\"Root, language label, gloss and page are all correct: Pokorny p.630 has k̑u̯en- ‘feiern; heilig(en)’ with precisely the two branches of the chart \"\n   \"(Avestan spənta- ‘holy’ = Lith. šventas, OCS svętъ; Gothic hunsl ‘sacrifice’, OE hūsl ‘sacrament’ < *k̑un-s-lo-). \"\n   \"One notational caveat: the initial is a PALATAL *ḱ, not a labiovelar *kʷ — that is what produces Iranian sp-, Lithuanian šv-, Slavic sv- in the satem languages \"\n   \"(Wiktionary reconstructs Proto-Iranian *ćwantaH < PIE *ḱwen-). Nourai writes ‘Kwen’ because he follows the 1976 AHD appendix, which prints the root as ‘kʷen-’; \"\n   \"the -w- is right, the labiovelar notation is not. Nourai’s numbering ‘Kwen 1’ distinguishes it from his ‘Kwen 2’ elsewhere, as Pokorny distinguishes his homonyms.\"),\n \"note_fa\": (\"ریشه، برچسب زبانی، معنا و شمارهٔ صفحه هر چهار درست است: پوکورنی در صفحهٔ ۶۳۰ ریشهٔ k̑u̯en- «جشن گرفتن، مقدس داشتن» را با همان دو شاخهٔ نمودار آورده است \"\n   \"(اوستایی spənta- «مقدس» برابر با šventas لیتوانیایی و svętъ اسلاوی کلیسایی؛ و گوتی hunsl «قربانی» و انگلیسی کهن hūsl «آیین مقدس» از *k̑un-s-lo-). \"\n   \"تنها نکتهٔ فنی این است که همخوان آغازینِ ریشه، کامیِ *ḱ است نه لبی‌کامیِ *kʷ؛ همین ḱ است که در زبان‌های ساتم به sp- ایرانی، šv- لیتوانیایی و sv- اسلاوی بدل شده است \"\n   \"(ویکی‌واژه ایرانیِ آغازین را *ćwantaH بازسازی می‌کند). نورایی «Kwen» می‌نویسد چون از پیوست فرهنگ امریکن‌هریتیج (۱۹۷۶) پیروی می‌کند که همین املا را دارد. در مجموع ادعای نورایی درست است.\"),\n \"sources\": [W_ESF],\n \"ref_check\": [\n   {\"ref\": \"POK:630\", \"status\": \"supports\", \"note\": POK630}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 471 (WLD_Bd1_pages.txt, the k̑uen- article)\", \"stance\": \"supports\",\n    \"note\": \"‘k̑uen- „feiern; heilig(en)“. Verbal in lett. svinēt „feiern, heiligen“ … av. spənta- „heilig“ (zur Bed. s. Bartholomae Airan. Wb. 1619 ff.) = lit. šventas, aksl. svętъ „heilig“ … dazu wahrscheinlich got. hunsl n. „Opfer“, ags. husl n. „Sakrament“ (*k̑un-s-lo-).’\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kʷen-\", \"stance\": \"supports\",\n    \"note\": \"‘kʷen-. Holy. Suffixed zero-grade form *kʷn̥-s-lo- in Germanic *hunslam in Old English hūsl, hūsel, Eucharist: HOUSEL. [Pok. k̑uen- 630.]’ — note Watkins’ own bracket restores Pokorny’s palatal k̑.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. housel (leaf 402 ≈ p.781)\", \"stance\": \"supports\", \"note\": KLN746}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"spenta; spento-dâto; gao-spenta\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Avestan spəṇta- ‘holy, beneficent’ (Gathic spəntā, the standing epithet of Ahura Mazdā and of the aməṣ̌a spəṇta) is *ḱwen-to-, a to-participle of *ḱwen-, \"\n   \"with satem *ḱw > Proto-Iranian *ćw > Av. sp-; its comparative/superlative spanyah-, spəništa- and the abstract spanah- ‘holiness’ show the bare stem. \"\n   \"spəṇtō.dāta- is a bahuvrīhi/tatpuruṣa ‘created (dāta-, from dā- ‘to give, create’) by the Holy One’, i.e. by Spənta Ārmaiti — the name that becomes MP Spandadāt/Spandiyād and NP Esfandiyār. \"\n   \"gao-spəṇta- (Vīdēvdād 21.1) is ‘the beneficent cow / holy domestic animal’, gao- ‘cow, cattle’ + spəṇta-, which yields MP gōspand and NP gōsfand ‘sheep, small cattle’. \"\n   \"The one loose point is the gloss ‘also an herb’: Avestan spəṇta- means only ‘holy’; the plant sense (Peganum harmala) is a New Persian development from the plant’s use in fumigation against the evil eye.\"),\n  \"derivation_fa\": (\"اوستایی spəṇta- «مقدس، سودبخش» — صفت ثابت اهورامزدا و امشاسپندان — همان *ḱwen-to- است، یعنی صفت مفعولیِ ‑ta از ریشهٔ *ḱwen-؛ در زبان‌های ساتم *ḱw به *ćw ایرانی و سپس به sp- اوستایی بدل شده است. \"\n   \"صورت‌های تفضیلی spanyah- و عالی spəništa- و مصدرِ spanah- «قداست» ستاک بی‌پسوند را نشان می‌دهند. \"\n   \"spəṇtō.dāta- ترکیبی است به معنی «آفریدهٔ آن مقدس» (dāta- از dā- «دادن، آفریدن») که در فارسی میانه Spandadāt/Spandiyād و در فارسی نو «اسفندیار» شده است. \"\n   \"gao-spəṇta- (وندیداد ۲۱٫۱) «گاوِ سودبخش/جانور اهلیِ مقدس» است که فارسی میانهٔ gōspand و فارسی نوِ «گوسفند» از آن آمده است. \"\n   \"تنها بی‌دقتی نمودار، افزودنِ معنی «گیاه» به واژهٔ اوستایی است: spəṇta- در اوستا فقط «مقدس» است و معنی گیاهی (اسفند، Peganum harmala) تحولی فارسیِ نو است، از کاربرد دود کردن این دانه برای دفع چشم‌زخم.\"),\n  \"sources\": [W_ESF, W_GUSF, W_ESFY],\n  \"ref_check\": [\n    {\"ref\": \"KLN:746\", \"status\": \"supports\",\n     \"note\": KLN746 + \" Page caveat: in the 1966 two-volume scan this entry falls on printed p.781 (leaf 402; calibration p = 2·leaf − 23, checked against leaf 15 = p.7 and leaf 438 = p.853), so Nourai’s ‘746’ is ~35 pages off, though the content is exactly his claim.\"},\n    {\"ref\": \"HRN:210\", \"status\": \"supports\",\n     \"note\": \"Horn, Grundriss der neupersischen Etymologie, p.210 (HRN.txt form-feed leaf 231), no. 942: ‘gōspend, gōsfend „Kleinvieh, Schaaf, Widder, Ziege“. aw. gaospenta- (vd. 21, 1); phlv. gōspand.’ — the page number is exact and the entry is exactly Nourai’s gao-spenta arrow.\"},\n    {\"ref\": \"BQT:121\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qāṭeʿ ed. Moʿin, vol.1, printed p.~121-122 (BQT_v1_pages.txt leaf 332; running-head calibration leaf 437 = p.۲۱۷, i.e. leaf = page + 220), Moʿin’s footnote 5 to اسپند/اسفند: ‘در اوستا spəṇta بمعنی مقدس <بارتولمه ۱۶۱۹>. طبری esfand «واژه‌نامه»… Peganum harmala این گیاه در اغلب نقاط ایران خودروست «فرهنگ روستایی»’ — Moʿin gives both halves of Nourai’s box (Av. spəṇta ‘holy’ and the plant).\"},\n    {\"ref\": \"BQT:210\", \"status\": \"not_found\",\n     \"note\": \"Printed p.210 of the same volume is leaf 430 of BQT_v1_pages.txt (same running-head calibration), which is the بادروج / بادزهر stretch of the ب chapter and has nothing to do with spənta; nor does افسنتین fall there (it is at leaf ~365, p.~145). I could not identify what Nourai meant by ‘210’.\"},\n    {\"ref\": \"SYN:1476\", \"status\": \"not_checked\",\n     \"note\": \"Buck’s chapter 22 RELIGION begins on printed p.1462, but the local OCR (SYN.txt, 35 875 lines) breaks off inside chapter 21 (Law) — greps for ‘sacred’, ‘šventas’, ‘hunsl’, ‘sanctus’ return nothing from that chapter. The cited page is not in the copy on disk.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"630\", \"stance\": \"supports\", \"note\": POK630},\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, s.v. gao.spənta- (BRT.txt, the Vīdēvdād citations at lines 2782, 10132, 13299) and spənta- col. 1619 ff.\", \"stance\": \"supports\",\n     \"note\": \"The OCR preserves the compound in its Avestan context, e.g. ‘tumasp tē gaospənta … asaone V. 21. 1’ = Vd. 21.1, the very passage Horn cites; Walde-Pokorny I 471 refers to ‘Bartholomae Airan. Wb. 1619 ff.’ for spənta-, and Moʿin’s Borhan footnote cites the same column.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt), English index ‘cattle gēspand, stōr’\", \"stance\": \"supports\",\n     \"note\": \"MacKenzie’s Pahlavi form gōspand/gēspand ‘sheep, small cattle’ is the Middle Persian link between Av. gao-spəṇta- and NP گوسفند that the chart passes over silently.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"esfand «اسفند»; Esfandîyâr «اسفندیار»; gŭsfand «گوسفند»\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"All three are the New Persian continuations of the Avestan box, through Middle Persian. (1) اسفند esfand / اسپند espand / سپند sepand ‘wild rue, Peganum harmala’ < MP spand \"\n   \"< Proto-Iranian *ćwantaH ‘holy’ (Av. spəṇta-), named from its ritual use as a fumigant against the evil eye; Iranian *sp- is kept, and the prothetic ا- is the regular New Persian \"\n   \"vowel before an initial cluster (cf. اسپست, استخوان). (2) اسفندیار Esfandiyār < MP Spandadāt/Spandiyād < Av. spəṇtō.dāta- ‘created by the Holy (Spənta Ārmaiti)’, with -dāta- > -dād > -yār \"\n   \"by the usual Middle-Persian weakening of intervocalic -d-. (3) گوسفند gōsfand/gūsfand ‘sheep’ < MP gōspand < Av. gao-spəṇta-, with the New Persian shift p > f after s. \"\n   \"Nourai’s ‘holy creation’ for Esfandiyār is the standard reading.\"),\n  \"derivation_fa\": (\"هر سه واژه دنبالهٔ فارسیِ نوِ خانهٔ اوستایی‌اند، از راه فارسی میانه. یکم، «اسفند/اسپند/سپند» (Peganum harmala) از فارسی میانهٔ spand و آن از ایرانیِ آغازینِ *ćwantaH «مقدس» (اوستایی spəṇta-) است؛ \"\n   \"نامِ گیاه از کاربرد آیینیِ دود کردنِ آن برای دفع چشم‌زخم گرفته شده و الفِ آغازی همان الف افزودهٔ فارسی پیش از خوشهٔ آغازین است (مانند «اسپست»). \"\n   \"دوم، «اسفندیار» از فارسی میانهٔ Spandadāt/Spandiyād و آن از اوستایی spəṇtō.dāta- «آفریدهٔ سپندارمذ»؛ جزء ‑dāta- بر اثر سست‌شدن d میان‌واکه‌ای به ‑dād و سپس ‑یار بدل شده است. \"\n   \"سوم، «گوسفند» از فارسی میانهٔ gōspand و آن از gao-spəṇta- اوستایی، با ابدال p به f پس از س. ادعای نورایی در هر سه مورد درست است.\"),\n  \"sources\": [W_ESF, W_ESFY, W_GUSF],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The Persian box carries no reference of its own; checked Wiktionary (three entries), Horn no.942 and Moʿin’s Borhan footnote (BQT p.121) instead — see consulted.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"Wiktionary\", \"where\": \"اسفند (Etymology 2); اسفندیار; گوسفند\", \"stance\": \"supports\",\n     \"note\": \"‘اسفند … From Middle Persian spand, ultimately from Proto-Iranian *ćwantaH (“holy”) (compare Avestan spəṇta “holy”), because the plant is used in fumigation against evil eye. Ultimately from Proto-Indo-European *ḱwen-’; ‘اسفندیار … From Middle Persian /spandadāt/, in turn derived from Avestan spəntōδāta, literally “given by Amesha Spenta”’; ‘گوسفند … From Middle Persian gōspand “sheep, small cattle”, from Avestan gao-spəṇta- “beneficent cow”, a compound of gao- “cow” + spəṇta “holy”’.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 942, p.210\", \"stance\": \"supports\", \"note\": \"‘gōspend, gōsfend „Kleinvieh, Schaaf, Widder, Ziege“. aw. gaospenta- (vd. 21, 1); phlv. gōspand.’\"},\n    {\"src\": \"BQT\", \"where\": \"vol.1 p.~121, Moʿin’s footnote to اسپند\", \"stance\": \"supports\", \"note\": \"‘در اوستا spəṇta بمعنی مقدس <بارتولمه ۱۶۱۹> … Peganum harmala این گیاه در اغلب نقاط ایران خودروست’.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. gēspand/gōspand\", \"stance\": \"supports\", \"note\": \"‘cattle gēspand, stōr’ — the Pahlavi stage of گوسفند.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Greek\", \"words\": \"apsinthion\", \"verdict\": \"disputed\",\n  \"derivation\": (\"Greek ἀψίνθιον apsínthion ‘wormwood, Artemisia absinthium’ (Xenophon, Anabasis 1.5.1, c.370 BCE, of the Mesopotamian steppe) is the source of Latin absinthium and of \"\n   \"European absinthe — that part is uncontested. Its own origin is not. Klein 1966 (the page Nourai cites) says it ‘is of OPers. origin; cp. ModPers. aspand, sipand, of s.m.’, and \"\n   \"Etymonline still writes ‘perhaps from Persian (compare Persian aspand, of the same meaning)’ — this is Nourai’s arrow. But the modern standard, Beekes’ Etymological Dictionary of Greek \"\n   \"(followed by Wiktionary), rejects it: the cluster -ινθ- is a Pre-Greek suffix (cf. τέρμινθος, ἐρέβινθος, ὑάκινθος, λαβύρινθος) and the variant ἀσπίνθιον with /sp/ for /ps/ points the \"\n   \"same way. Two further difficulties: the plants differ (apsínthion is Artemisia absinthium, esfand/spand is Peganum harmala), and an Avestan/Old Persian *spanta- would not give Greek \"\n   \"aps-/asp- with an initial a-. Scored disputed: modern scholarship prefers a Pre-Greek (substrate) origin.\"),\n  \"derivation_fa\": (\"یونانی ἀψίνθιον «افسنطین، Artemisia absinthium» (نخستین بار در آناباسیس گزنفون، حدود ۳۷۰ پیش از میلاد، در وصف دشت میان‌رودان) بی‌گمان سرچشمهٔ absinthium لاتین و absinthe اروپایی است؛ \"\n   \"اما ریشهٔ خودش محل اختلاف است. کلاین در همان صفحه‌ای که نورایی ارجاع می‌دهد می‌نویسد «از اصل پارسی باستان است؛ سنجیده شود با aspand و sipand فارسی» و اتیمانلاین نیز «شاید از فارسی» می‌آورد — یعنی همان ادعای نورایی. \"\n   \"ولی مرجع امروزی، فرهنگ ریشه‌شناختی بیکس (و به پیروی از آن ویکی‌واژه)، این را رد می‌کند: خوشهٔ ‑ινθ- پسوندی پیش‌یونانی است (مانند τέρμινθος، ἐρέβινθος، ὑάκινθος، λαβύρινθος) و گونهٔ ἀσπίνθιον نیز بر همین دلالت دارد. \"\n   \"دو اشکال دیگر: گیاه‌ها یکی نیستند (افسنطین از سردهٔ آرتمیزیا است و اسفند Peganum harmala) و صورت اوستایی spəṇta- الفِ آغازیِ یونانی را توضیح نمی‌دهد. \"\n   \"بنابراین پژوهش امروزی این پیوند را نمی‌پذیرد و واژه را وامی از زیرلایهٔ پیش‌یونانی می‌داند.\"),\n  \"sources\": [W_APS, E_ABS],\n  \"ref_check\": [\n    {\"ref\": \"KLN:7\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 p.7 (KLN_1966.txt line 1241 = leaf 15; calibration p = 2·leaf − 23 gives exactly 7, so the page number is right): ‘absinth, absinthe, n., wormwood. — F. absinthe, fr. Gk. ἀψίνθιον, “wormwood”, which is of OPers. origin; cp. ModPers. aspand, sipand, of s.m.’ — Klein does say what Nourai’s arrow says; he is simply not the current standard on Greek.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"Wiktionary\", \"where\": \"ἀψίνθιον, Etymology (citing Beekes)\", \"stance\": \"contradicts\",\n     \"note\": \"‘According to Beekes, the cluster -ινθ- suggests a Pre-Greek source, as seen in τέρμινθος … λαβύρινθος. Also, the variant ἀσπίνθιον with /sp/ instead of /ps/ may point to borrowing from Pre-Greek.’\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. absinthe\", \"stance\": \"partial\",\n     \"note\": \"‘from Greek apsinthion, which is perhaps from Persian (compare Persian aspand, of the same meaning)’ — keeps the Iranian idea only as a ‘perhaps’.\"},\n    {\"src\": \"TAD\", \"where\": \"Tobia al-ʿUnaysi, leaf 7 of TAD_pages.txt (printed p.3–4)\", \"stance\": \"partial\",\n     \"note\": \"‘إفسنتين — يوناني … معناه لاذع وهو نبات ورقه كورق الصعتر’ — al-ʿUnaysi derives the Arabic word from Greek and stops there; he says nothing about a Persian source of the Greek word.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Arabic\", \"words\": \"afsantîn\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Arabic أفسنتين afsantīn ‘wormwood’ is a Greek medical term taken into Arabic in the translation movement of the 3rd/9th century, when Dioscorides and Galen — in whom \"\n   \"ἀψίνθιον is a standard drug — were rendered into Arabic, largely through Syriac (Syriac ܐܦܣܢܬܝܢ). The Greek neuter ἀψίνθιον was borrowed in a form reflecting the Byzantine \"\n   \"genitive/plural stem apsinth-, with prothetic ʾa- kept, /ps/ > /fs/ (Arabic has no /p/) and the -īn ending of Graeco-Arabic drug names (cf. أفيون, ترياق). \"\n   \"The arrow Greek > Arabic is exactly what Nourai’s reference states.\"),\n  \"derivation_fa\": (\"عربی «أفسنتين» اصطلاحی پزشکی است که در نهضت ترجمهٔ سدهٔ سوم هجری، هنگام برگرداندن آثار دیوسکوریدس و جالینوس (که ἀψίνθιον در آنها دارویی شناخته است) و بیشتر از راه سریانی (ܐܦܣܢܬܝܢ) وارد عربی شد. \"\n   \"یونانی ἀψίνθιον با نگاه‌داشتن الف آغازی، ابدال /ps/ به /fs/ (زیرا عربی واج p ندارد) و پایانهٔ ‑ين که در نام داروهای یونانی‌تبار عربی رایج است (مانند «أفيون») معرّب شده است. \"\n   \"پس پیکان «یونانی ← عربی» در نمودار درست است.\"),\n  \"sources\": [A_AFS, W_APS],\n  \"ref_check\": [\n    {\"ref\": \"TAD:4\", \"status\": \"supports\",\n     \"note\": \"Tobia al-ʿUnaysi, Tafsīr al-alfāẓ al-dākhila, entry ‘إفسنتين ــ يوناني [ἀψίνθιον, OCR-garbled] معناه لاذع وهو نبات ورقه كورق الصعتر’, found on leaf 7 of TAD_pages.txt; the following leaf 9 carries the printed numeral ٥ (=5), so this is printed p.3–4 — Nourai’s ‘4’ is right within one page in this 1932 edition.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qāṭeʿ s.v. افسنتین (BQT_alt_v1.txt lines 22698–22706)\", \"stance\": \"supports\",\n     \"note\": \"‘افسنتین … نوعی از بوی مادران کوهی است. گل آن بابونه و تلخی آن صبر نزدیک است. درد چشم را سود دارد.’ — the plant is the Artemisia of the Greek word, not Peganum harmala.\"},\n    {\"src\": \"MON\", \"where\": \"abadis.ir افسنتین (لغت‌نامه/فرهنگ)\", \"stance\": \"supports\",\n     \"note\": \"‘افسنتین. [ اَ س َ ] ( معرب ، اِ ) اپسنتین …’ — the Persian lexica mark it معرّب, i.e. an arabicised foreign (Greek) word, and even keep the Greek shape اپسنتین beside it.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt)\", \"stance\": \"silent\",\n     \"note\": \"greps for ‘afsant’, ‘absinth’, ‘apsinth’ and ‘Wermut’ return nothing in the local OCR, so Fraenkel could not be used to confirm the Syriac intermediary.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Persian\", \"words\": \"afsantîn «افسنتین»\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Persian افسنتین afsantīn (also افسنطین) ‘wormwood’ is the Arabic أفسنتين re-borrowed with the Arabic-Persian medical literature (Avicenna’s Qānūn and the later \"\n   \"pharmacopoeias such as the Tuḥfat al-Muʾminīn quoted by Dehkhodā); the Persian dictionaries tag it معرّب, i.e. arabicised, and Dehkhodā even glosses it with the Greek shape \"\n   \"اپسنتین. So the road is Greek > Arabic > Persian, exactly as drawn — and note that the word is NOT the same plant as اسفند in the box above, which is why the chart is right to \"\n   \"keep the two Persian boxes apart.\"),\n  \"derivation_fa\": (\"«افسنتین» (و «افسنطین») در فارسی وام‌واژهٔ عربیِ «أفسنتين» است که همراه با ادبیات پزشکیِ عربی‌نویس — قانونِ ابن‌سینا و داروشناسی‌های بعدی مانند تحفةالمؤمنین که دهخدا نقل می‌کند — وارد فارسی شده است. \"\n   \"فرهنگ‌های فارسی آن را «معرّب» نشانه زده‌اند و دهخدا حتی صورت یونانی‌مانندِ «اپسنتین» را در کنارش آورده است. پس راهِ یونانی ← عربی ← فارسی همان است که نمودار نشان می‌دهد. \"\n   \"نکتهٔ درخورِ توجه آنکه این گیاه با «اسفند» خانهٔ بالا یکی نیست و نورایی به‌درستی این دو خانهٔ فارسی را از هم جدا نگه داشته است.\"),\n  \"sources\": [A_AFS],\n  \"ref_check\": [\n    {\"ref\": \"MON:316\", \"status\": \"not_found\",\n     \"note\": \"grep for ‘افسنتین’ in both local Moʿin OCR files (MON_part1.txt, MON_part2.txt) returns 0 hits, and the local Moʿin scan is the 2-volume abridgement whose pagination does not map to the 6-volume edition Nourai cites, so p.316 cannot be located. The same entry was read instead in Dehkhodā/abadis (see consulted), which gives the معرّب tag Nourai’s arrow needs.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"abadis.ir افسنتین\", \"stance\": \"supports\", \"note\": \"‘افسنتین. [ اَ س َ ] ( معرب ، اِ ) اپسنتین. نوعی از بوی مادران کوهی است … ( از برهان ) ( آنندراج ).’\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qāṭeʿ s.v. افسنتین\", \"stance\": \"supports\", \"note\": \"the Persian lexicographic tradition Dehkhodā quotes (‘از برهان’) already has the word with the Artemisia description.\"},\n    {\"src\": \"TAD\", \"where\": \"leaf 7 (printed p.3–4)\", \"stance\": \"supports\", \"note\": \"‘إفسنتين ــ يوناني’ — the Arabic stage from which Persian took it.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Germanic\", \"words\": \"hun-slam\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"‘hun-slam’ is Nourai’s transcription of Watkins’ Proto-Germanic *hunslam (Wiktionary: *hunslą) ‘sacrifice, sacred offering’, from the zero grade *ḱwn̥-s-lo- of the root: \"\n   \"PIE *ḱ > Gmc. *h by Grimm’s Law, syllabic *n̥ > un, and the instrumental suffix -s-lo- (the type of Gothic swumsl, OE ræsl). It is attested as Gothic hunsl ‘θυσία, sacrifice’, \"\n   \"Old Norse húsl and Old English hūsl ‘sacrament, the Eucharist’. The only correction: the gloss should be ‘sacrifice, sacred offering’, not ‘holy’ — ‘holy’ is the meaning of the root, \"\n   \"and of the Avestan cognate, not of this Germanic noun.\"),\n  \"derivation_fa\": (\"«hun-slam» همان *hunslam ژرمنیِ آغازین در پیوست واتکینز است (در ویکی‌واژه *hunslą) به معنی «قربانی، پیشکشِ مقدس»، از درجهٔ صفرِ ریشه یعنی *ḱwn̥-s-lo-: \"\n   \"همخوان *ḱ هندواروپایی بنابر قانون گریم در ژرمنی h شده، *n̥ هجایی به un بدل گشته و پسوند ابزارسازِ ‑s-lo- بدان افزوده شده است. \"\n   \"این صورت در گوتی hunsl «قربانی»، نورس کهن húsl و انگلیسی کهن hūsl «آیین مقدس، عشای ربانی» گواهی شده است. \"\n   \"تنها اصلاح لازم در معنی است: معنی این اسمِ ژرمنی «قربانی» است نه «مقدس»؛ «مقدس» معنیِ خودِ ریشه و همتای اوستایی آن است. در بقیهٔ موارد ادعای نورایی درست است.\"),\n  \"sources\": [W_HOUSEL],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. kʷen-: ‘Holy. Suffixed zero-grade form *kʷn̥-s-lo- in Germanic *hunslam in Old English hūsl, hūsel, Eucharist: HOUSEL. [Pok. k̑uen- 630.]’ — Nourai’s ‘hun-slam’ is letter for letter Watkins’ *hunslam.\"},\n    {\"ref\": \"KLN:746\", \"status\": \"supports\",\n     \"note\": KLN746 + \" (page caveat as at node 1: the entry stands on printed p.781 of the 1966 scan, not 746.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"630\", \"stance\": \"supports\", \"note\": \"‘probably Gothic hunsl n. “sacrifice, oblation”, Old English husl n. “sacrament” (*k̑un-s-lo-)’.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 471\", \"stance\": \"supports\", \"note\": \"‘dazu wahrscheinlich got. hunsl n. „Opfer“, ags. husl n. „Sakrament“ (*k̑un-s-lo-; andere Deutungen verzeichnet Feist Got. Wb. 148)’ — note ‘wahrscheinlich’: Feist listed rival explanations, so the Germanic branch is probable rather than certain.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"housel, Etymology 1\", \"stance\": \"supports\", \"note\": \"‘From Old English hūsl, hūsel, hūsul, from Proto-West Germanic *hunsl, from Proto-Germanic *hunslą.’\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"English\", \"words\": \"housel\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Old English hūsl / hūsel ‘the Eucharist’ (and the denominative hūslian ‘to administer the Eucharist’, cf. Gothic hunsljan ‘to sacrifice’) > Middle English husel, housel \"\n   \"> archaic Modern English housel ‘the Eucharist, Holy Communion’ — the word Shakespeare uses in Hamlet I.v (‘unhous’led’). It is a striking case of a pagan sacrificial term being \"\n   \"taken over for the Christian sacrament in the Anglo-Saxon mission period, and it is genuinely the English cognate of Avestan spəṇta- that the chart claims.\"),\n  \"derivation_fa\": (\"انگلیسی کهن hūsl/hūsel «عشای ربانی» (و فعل برساختهٔ hūslian «عشای ربانی دادن»، همانند hunsljan گوتی «قربانی کردن») از راه انگلیسی میانهٔ husel/housel به housel امروزی رسیده است \"\n   \"که واژه‌ای کهنه و ادبی است (شکسپیر در هملت، پردهٔ اول، صحنهٔ پنجم صورت unhous’led را به کار برده است). \"\n   \"این نمونهٔ گویایی است از کاربردِ یک اصطلاح قربانیِ پیشامسیحی برای آیین مسیحی در دورهٔ تبلیغِ انگلوساکسون، و به‌راستی همان هم‌ریشهٔ انگلیسیِ spəṇta- اوستایی است که نمودار ادعا می‌کند.\"),\n  \"sources\": [W_HOUSEL],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no reference on the box; checked Klein s.v. housel, Watkins s.v. kʷen- and Wiktionary instead (see consulted).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. housel n. and housel v. (leaf 402 ≈ p.781)\", \"stance\": \"supports\",\n     \"note\": \"‘housel, n., the Eucharist (obsol.) — ME. husel, fr. OE. husel … Goth. hunsl “sacrifice”’ and ‘housel, tr. v., to administer the Eucharist to. — ME. huslen, fr. OE. huslian … Cp. ON. húsla … Goth. hunsljan, “to sacrifice”.’\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kʷen-\", \"stance\": \"supports\", \"note\": \"‘… in Old English hūsl, hūsel, Eucharist: HOUSEL.’\"},\n    {\"src\": \"Wiktionary\", \"where\": \"housel\", \"stance\": \"supports\", \"note\": \"‘The Eucharist (bread and wine taken at Holy Communion); (rare) the ritual or ceremony of Holy Communion’, from OE hūsl.\"}\n  ]\n }\n]\ndata[\"entries\"].append(e1)\n\nimport io\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-291.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('written', sum(len(e['nodes']) for e in data['entries']), 'nodes')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build291.py",
 "description": "Build and write page-291.json"
}
```


### [2026-09-06T22:30:46.927Z] TOOL RESULT

```
written 19 nodes
```


## [2026-09-06T22:30:49.404Z] TOOL CALL #95: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-291.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 291",
 "description": "Validate and run verify_check"
}
```


### [2026-09-06T22:30:51.699Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'plausible': 2, 'confirmed': 14, 'disputed': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'not_checked': 8, 'partial': 1, 'not_found': 2}
books consulted: {'partial': 9, 'supports': 37, 'contradicts': 5, 'silent': 2} | by book: {'KLN': 7, 'Wiktionary': 7, 'POK': 6, 'MON': 6, 'Etymonline': 5, 'AHD': 4, 'LKT': 3, 'BQT': 3, 'SYN': 2, 'WLD': 2, 'PHD': 2, 'TAD': 2, 'LAT': 1, 'BRT': 1, 'HRN': 1, 'AFA': 1}
```


## [2026-09-06T22:30:56.661Z] TOOL CALL #96: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg291.png data/verification/sources/refs/ocr/BOOK/291.png && ls -la data/verification/sources/refs/ocr/BOOK/291.png && git status --short data/verification/page-291.json",
 "description": "Archive page image"
}
```


### [2026-09-06T22:30:56.742Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 70592 Sep  6 18:30 data/verification/sources/refs/ocr/BOOK/291.png
?? data/verification/page-291.json
```


## [2026-09-06T22:31:17.553Z] AGENT

Page 291 (book page 261) verified; `verify_check.py 291` reports 19/19 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed. Nodes: 14 confirmed, 2 plausible, 3 disputed. Ref checks: 14 supports, 1 partial, 2 not_found, 8 not_checked (boxes with no citation). 45 `consulted` records across POK, WLD, AHD, SYN, KLN, LKT, LAT, BRT, HRN, PHD, BQT, MON, TAD, AFA, Wiktionary, Etymonline; 22 web pages archived via `fetch_source.py`.

**Disputed**
- Kwel #6 (English `cylinder`): Greek *kylindros* < *kulindein* "to roll", of unknown origin; Watkins files CYLINDER under *(s)kel-3*, not *kʷel-*. Same box also mixes *tele-* words, which belong to Pokorny's separate *kʷel-2 "far" (p. 640).
- Kwel #12 (English `clown`): obscure origin, probably Scandinavian/Low German ("clod, lump"); Etymonline calls the Latin *colonus* theory "less likely", and CLOWN is absent from Watkins' index. *colony, culture, collar* are fine.
- Kwen 1 #3 (Greek `apsinthion`): Klein p. 7 (the page Nourai cites) does say "of OPers. origin, cp. aspand", but Beekes/Wiktionary make it Pre-Greek (-ινθ- suffix, variant *aspinthion*); the plants also differ (Artemisia vs Peganum harmala).

**Plausible**
- Kwel #1 (Greek): *kuklos/telos/telesma* correct under *kʷel-1*, but the gloss "far away" belongs to the homonym *kʷel-2*.
- Kwel #9: "German hwe-hula" is Proto-**Germanic** *hweh(w)ula-/*hwewlaz, not German (German *Rad* is a different root); label is the book's own looseness.

**Book misprint (extraction faithful, confirmed on the page image)**
- Root box prints `Kwel, Qwel : to, move around, dwell`; the verb is missing — AHD/Pokorny read "to turn, move around, dwell" (page 290, Part 1, prints "to move around, dwell"). Recorded with `error_in: "book"`; page PNG saved to `data/verification/sources/refs/ocr/BOOK/291.png`.

**No extraction errors found** — the JSON matches the printed page in all other respects (Persian scripts اسفند/اسفندیار/گوسفند/طلسم/کالسکه/افسنتین and the French-loan list all check out).

**Reference problems worth the owner's note**
- `BQT:210` (Kwen 1, Avestan box): not_found — printed p. 210 of Borhan vol. 1 is the بادروج/بادزهر stretch; only `BQT:121` (Moʿin's اسپند footnote citing Bartholomae 1619) is on point.
- `SYN:1476`: not_checked — the local Buck OCR breaks off inside chapter 21; chapter 22 (pp. 1462+) is missing from the scan on disk.
- `KLN:746` (housel/spənta): content supports exactly, but in the 1966 two-volume scan that entry sits on printed p. 781 (calibration p = 2·leaf − 23, checked against leaf 15 = p. 7, which makes `KLN:7` for absinth exact). Nourai's page number is ~35 off.
- `MON:316` (افسنتین): not_found in the local Moʿin OCR (2-vol. abridgement); read via Dehkhodā/abadis instead.

File written: `/home/sfmqrb/git/rishe/data/verification/page-291.json`.
