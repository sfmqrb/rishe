# Verification process log — verify-page-304


## [2026-09-06T22:52:56.134Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 304 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-304.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-304.json. Write /home/sfmqrb/git/rishe/data/verification/page-304.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 304` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:52:57.365Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:52:58.036Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:52:58.053Z] TOOL RESULT

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


## [2026-09-06T22:52:58.620Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-304.txt"
}
```


### [2026-09-06T22:52:58.635Z] TOOL RESULT

```
1	=== PDF page 304 (book page 274) ===
2	--- entry 0 ---
3	ROOT [Semitic / Syriac] Layh; A.l.h : to be high; to worship  (refs KLN:505; FVQ:66; VDQ:125)  PART 2
4	#1 (parent #0) [Arabic] refs=KLN:505; FVQ:33 | Al-lah, Allah : the God ☞Al 3 ; A.l.h : God
5	  #2 (parent #1) [Persian] refs=FVA:33 | Allâh «الله» : God | extra: الهه ، الهی ، الهیّات
6	  #3 (parent #1) [English] refs=KLN:51; AHD | Allah
7	--- entry 1 ---
8	ROOT [Semitic] L.b.n : to be white  (refs BQT:1886; KFL:430)
9	#1 (parent #0) [Arabic] refs=BQT:308; KLN:164,875 | laban, l.b.n : milk ; luban : the white resin of sandalwood ; luban jâwî : the resin of Java (Sumatra)
10	  #2 (parent #1) [Persian] refs=FVA:363 | labanîyyât «لبنیّات» : dairy products
11	  #3 (parent #1) [Spanish] refs=None | loben jui, benjui : balsamic resin
12	    #4 (parent #3) [French] refs=AHD:124 | benjoin
13	      #5 (parent #4) [Persian] refs=BQT:308 | benzîn «بنزین» : gasoline
14	      #6 (parent #4) [English] refs=AHD:124; OEW:61 | benzoin, benzene
15	--- entry 2 ---
16	ROOT [Indo-European] Lěb : lip  (refs POK:655)
17	#1 (parent #0) [Iranian] refs=BQT:1885 | lap : lip
18	  #2 (parent #1) [Pahlavi] refs=MON:3551 | lab : lip
19	    #3 (parent #2) [Persian] refs=HRN:212; MON:3551 | lab «لب» : lip, also side or edge of anything | extra: لبالب ، لبریز ، لبدیس ، لبخند ، لبچین
20	#4 (parent #0) [Germanic] refs=AHD | lep : lip
21	  #5 (parent #4) [English] refs=None | lip
22	
```


## [2026-09-06T22:53:01.601Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-304.json",
 "description": "Read source JSON for page 304"
}
```


### [2026-09-06T22:53:01.637Z] TOOL RESULT

```
{
  "pdf_page": 304,
  "book_page": 274,
  "entries": [
    {
      "part": 2,
      "root": {
        "name": "Layh; A.l.h",
        "lang": "Semitic / Syriac",
        "refs": "KLN:505; FVQ:66; VDQ:125",
        "gloss": "to be high; to worship"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:505; FVQ:33",
          "words": [
            {"translit": "Al-lah, Allah", "gloss": "the God", "script": null, "see": ["Al 3"]},
            {"translit": "A.l.h", "gloss": "God", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:33",
          "words": [
            {"translit": "Allâh", "gloss": "God", "script": "الله"}
          ],
          "script_extra": "الهه ، الهی ، الهیّات",
          "note": null,
          "quote": {"text": "خوشا آنان که الله یارشان بی - بحمد و قل هوالله کارشان بی", "poet": "Bâbâ Tâher"}
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:51; AHD",
          "words": [
            {"translit": "Allah", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "L.b.n",
        "lang": "Semitic",
        "refs": "BQT:1886; KFL:430",
        "gloss": "to be white"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "BQT:308; KLN:164,875",
          "words": [
            {"translit": "laban, l.b.n", "gloss": "milk", "script": null},
            {"translit": "luban", "gloss": "the white resin of sandalwood", "script": null},
            {"translit": "luban jâwî", "gloss": "the resin of Java (Sumatra)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:363",
          "words": [
            {"translit": "labanîyyât", "gloss": "dairy products", "script": "لبنیّات"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Spanish",
          "refs": null,
          "words": [
            {"translit": "loben jui, benjui", "gloss": "balsamic resin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD:124",
          "words": [
            {"translit": "benjoin", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:308",
          "words": [
            {"translit": "benzîn", "gloss": "gasoline", "script": "بنزین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:124; OEW:61",
          "words": [
            {"translit": "benzoin, benzene", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Lěb",
        "lang": "Indo-European",
        "refs": "POK:655",
        "gloss": "lip"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Iranian",
          "refs": "BQT:1885",
          "words": [
            {"translit": "lap", "gloss": "lip", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:3551",
          "words": [
            {"translit": "lab", "gloss": "lip", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:212; MON:3551",
          "words": [
            {"translit": "lab", "gloss": "lip, also side or edge of anything", "script": "لب"}
          ],
          "script_extra": "لبالب ، لبریز ، لبدیس ، لبخند ، لبچین",
          "note": null,
          "quote": {"text": "بگیرم ادب را ببندم دو لب را - که تا راز گوید لب دُرفشانش", "poet": "Molavî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "lep", "gloss": "lip", "script": null}
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
            {"translit": "lip", "gloss": null, "script": null}
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


## [2026-09-06T22:53:02.090Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:53:02.131Z] TOOL RESULT

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


## [2026-09-06T22:53:25.268Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVQ','VDQ','FVA','AHD','BQT','KFL','POK','MON','HRN','OEW','WLD','SYN','IEC','PHD','NYB','HUB','LKT','PHN','DEV','SKT','ARY','AFM','PLA']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]);print()\n\""
}
```


## [2026-09-06T22:53:25.779Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && sed -n 1,60p data/verification/page-259.json"
}
```


### [2026-09-06T22:53:27.039Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

KFL {"title": "Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885", "kind": "archive_djvu", "url": "https://archive.org/details/20260705_20260705_0657 (an Indian/other printing; OCR poor) ; better: text on shamela.ws (search 'فقه اللغة وسر العربية الثعالبي') with edition page numbers", "lookup_hint": "Look up by chapter/word on shamela; the 1885 Beirut pagination is not reproduced online.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt"], "page_offset": null, "covers_etymology": false, "notes": "Archive OCR of this copy is very poor; use shamela text."}

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
```


### [2026-09-06T22:53:27.075Z] TOOL RESULT

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
          "note": "Pokorny IEW p.579 (bottom) – 580, read in POK_02.txt leaf 239–240 (awk 'BEGIN{RS=\"\\f\"} NR==239'): '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’. Arm. sirt … gr. καρδία (att.), κραδίη (hom.) … lat. cor (aus *cord) … got. hairto, ahd. herza, ags. heorte, anord. hjarta n. ‘Herz’ (*ḱērd-on-)'. Exactly Nourai's root name and gloss."
        },
        {
          "ref": "SYN:251",
          "status": "supports",
          "note": "Buck, Selected Synonyms p.251 = §4.44 HEART (SYN.txt leaf 289, page number '251' printed in the running head above '4.44 HEART'): 'Most of the words for ‘heart’ belong to an inherited group … 1. IE *ḱerd-, etc., with gradation. Walde-P. 1.423 ff. Ernout-M. 219 f.'"
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. kerd-1 (AHD_watkins1985.txt line 621)",
          "stance": "supports",
          "note": "'kerd-1. Heart. 1. Suffixed form *kerd-en- in Germanic *hertōn- in Old English heorte, heart: HEART. 2. Zero-grade form *kr̥d- in: a. Latin cor (stem cord-), heart … b. suffixed form *kr̥d-yā in Greek kardia … 3. Possibly *kred-dhə-, “to place trust” … in Latin crēdere, to believe. [Pok. kered- 579.]' — the whole chart in one entry."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny I 423 f. (cited by POK and by Buck 4.44; only Band III index available locally, WLD_band3.txt line 2965 'kerd- 423')",
          "stance": "supports",
          "note": "Both Pokorny and Buck refer the 'heart' root to WP. I 423 f.; the local library holds only the Register volume, whose index line points to that page."
        },
        {
          "src": "IEC",
          "where": "Mann, s.vv. Kerd- and Kr̥d- (IEC.txt lines 8676, 9088)",
          "stance": "supports",
          "note": "'Kerd- (Kerdis, ā, io) “heart, core, centre”. Cf. Kr̥d-. WP I, 424' and 'Kr̥d- (Kr̥ds, Kr̥diiom, iio) “core, centre, heart” … Hitt. kar-, ds kardi … Gk. kardia; Lat. cor, gs cordis …'"
        },
        {
          "src": "LAT",
          "where": "Ernout–Meillet p.254–255 s.v. cor (LAT.txt leaf 272–273)",
          "stance": "partial",
          "note": "'Le nom du “coeur” … est au fond le même dans toutes les langues indo-européennes. Il est probable que le nominatif-accusatif était de la forme *ḱerd, conservée dans hitt. kir … gr. κῆρ, v.pruss. seyr, et que les autres cas reposaient sur *ḱr̥d-'; but adds 'Pour le rapport qu'on a envisagé, sans raison, avec crēdō, v. ce mot' — i.e. rejects the 'Kred' half."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan",
```


## [2026-09-06T22:53:34.960Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVQ','BQT','POK','MON','HRN','AHD','KFL']:\n    e=d[k]; print(k, '| local:', e.get('local_file'), '| offset:', e.get('page_offset'), '| hint:', e.get('lookup_hint'), '| scans:', e.get('scans')); print()\n\""
}
```


### [2026-09-06T22:53:36.736Z] TOOL RESULT

```
KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages. | scans: None

FVQ | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296). | scans: None

BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor) | scans: [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]

POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config | scans: None

MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks). | scans: None

HRN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann. | scans: None

AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.). | scans: None

KFL | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt'] | offset: None | hint: Look up by chapter/word on shamela; the 1885 Beirut pagination is not reproduced online. | scans: None
```


## [2026-09-06T22:53:44.278Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Allah\" KLN_1966.txt KLN_1971.txt | head\necho \"=== benzoin\"\ngrep -n \"^benzoin\\|^benzene\\|^benzo\" KLN_1966.txt | head\necho \"=== olibanum/luban\"\ngrep -n \"^olibanum\\|luban\\|lubān\" KLN_1966.txt | head -20\necho \"=== lip\"\ngrep -n \"^lip,\" KLN_1966.txt | head"
}
```


### [2026-09-06T22:53:44.387Z] TOOL RESULT

```
KLN_1971.txt:11437:Allah, n.-, Mohammedan name of the Supreme 
KLN_1966.txt:2240:Allah,  n.,  Mohammedan  name  of  the  Supreme Being.  —  Arab.  Alldhu,  contraction  of  al-lldhu, fr.  al-,  ‘the’,  and  lldh.  ‘God’.  See  Elohim.
=== benzoin
4766:benzoin,  n.,  a  balsamic  resin.  —  F.  benjoin,  fr. Sp.  benjui,  which  is  shortened  fr.  lo-benjui  (the first  syllable  having  been  mistaken  for  the  def. article),  fr.  Arab,  lubdn  jawt,  ‘frankincense  of Java’  (Java  is  the  former  name  of  Sumatra). For  the  etymology  of  Arabic  lubdn  see  leban. benzol,  n.,  benzene.  —  Altered  fr.  Benzin  by  the German  chemist  Baron  Justus  von  Liebig  (1803- 73)  in  1834.  —  See  benzene  and  -ol  (representing L.  oleum,  ‘oil’).
4767:benzoyl,  n.,  a  univalent  radical,  C6H5CO,  found in  benzoic  acid.  —  Coined  by  the  German  chem¬ ists  Baron  Justus  von  Liebig  (1803-73)  and Friedrich  Wohler  (1800-82)  fr.  benzo-  and  -yl. bepaint,  tr.  v.  —  Formed  fr.  pref.  be-  and  paint, beplaster,  tr.  v.  —  Formed  fr.  pref.  be-  and plaster.
=== olibanum/luban
21362:leaven,  n.  — -  ME.  levain,  levein,  fr.  F.  levain,  fr. VL.  *levamen,  ‘something  that  raises’  (classical L.  levamen,  means  ‘alleviation,  mitigation’),  fr. levare,  ‘to  lift,  raise;  to  lighten,  alleviate,  miti¬ gate’,  fr.  levis,  ‘light’.  See  level  and  cp.  relieve. Derivatives :  leaven,  tr.  v.,  leaven-ing,  n. leban,  lebban,  also  leben,  n.,  coagulated  sour  milk (an  Arab  beverage).  —  VArab.  laban,  leben, ‘sour  milk’,  fr.  Arab,  laban,  ‘milk’,  which  is  rel. to  Heb.  labhan,  ‘white’,  lebhdnah,  poetic  name for  the  moon  (lit.  ‘the  white  one’),  libhonah, Aram. -Syr.  fbhuntd,  Arab,  luban,  ‘frankincense’ (Gk.  Xtpavo;,  Xipavorc.;,  ‘frankincense’,  are Sem.  loan  words),  Heb.  Lfbhanon,  Akkad.  Lab- nanu,  Aram.  Libhnan,  Arab.  Lubnan,  ‘Mount Lebanon’,  lit.  ‘the  white  one’;  so  called  from the  whiteness  of  its  cliffs.  Cp.  olibanum  and  the first  element  in  benzoin.
26199:olibanum,  n.,  frankincense.  —  ML.,  fr.  L.  libanus (Vulgate),  fr.  Gk.  X^avop,  fr.  Heb.  tlbhdndh, ‘frankincense’,  lit.  ‘the  white  one’,  fr.  Idbhan, ‘white’.  See  leban.
=== lip
```


## [2026-09-06T22:53:45.386Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ allah\"\ngrep -n -i \"allah\" FVQ_pages.txt | head -20\necho \"=== POK leb\"\ngrep -n \"lemma: leb\\|lemma: lēb\\|lemma: lep\" POK_full.txt | head -20"
}
```


### [2026-09-06T22:53:45.459Z] TOOL RESULT

```
=== FVQ allah
622:revelations, and Allah naturally chose to reveal the final revelation in
624:was lacking in the necessary religious vocabulary, and that Allah
2369:" By Allah, Muhammad is no better a raconteur than I am. His stories
2395:period, 2 for in a verse of the Meccan poet 'Abdallah b. az-Ziba'ra,
2741:1,^)1 (Allahumma).
3042:Note also (J^\ creator used of Allah in ii, 51 ; lix, 24 ; and
3411:repentance, and <J^ the relenting, used as a title of Allah.
3739:1 Cor. xiv, 21. Cf. 2 E.sdras, xix, 21, and Mekilta, Beshallah, 9 (ed. Fried nmnn,
4302:by representing Allah as saying to him " Then we told thee by
6827:Allah, whose source had previously eluded us, is here traced to its home." Horovitz,
7360:to the worship of Allah, as Raghib, Mvfradat, 307, recognizes. Men are
7361:warned to '* serve Allah and avoid Taghut " (xvi, 38 ; xxxix, 19) ;
8828:It occurs only in the phrase j*&\ <J*-' used of Allah.
9827:alteration, and in lix, 23, as a title of Allah, the Preserver. There is
10492:Allah caused to grow up over the Prophet. The reference is obviously
10601:in the N., for we find a Yusuf b. 'Abdallah b. Salam in Usd al Ghdba,
=== POK leb
55367:Root / lemma: lep-1 {* lehup-) 
55379:It seems that from Root / lemma: plab-\ (to babble, etc..) derived Root/ lemma: lep-1\ 
55398:Root / lemma: lep-2{*lehup-)
```


## [2026-09-06T22:53:53.084Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport io\np='KLN_1966.txt'\ndata=open(p,encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\n# map line no -> leaf\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i in (2240,4766,4767,21362,26199):\n        print(i,'leaf',leaf,'approx page',(leaf-12)*2,(leaf-12)*2+1)\n    leaf+=l.count('\\f')\nEOF"
}
```


## [2026-09-06T22:53:54.499Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: leb\\|lemma: lēb\\|Page(s): 655\" POK_full.txt | head -20\necho \"=== POK_02 leaf for p655 = 655-344=311\"\nawk 'BEGIN{RS=\"\\f\"} NR==311' POK_02.txt | head -60"
}
```


### [2026-09-06T22:53:55.057Z] TOOL RESULT

```
2240 leaf 38 approx page 52 53
4766 leaf 98 approx page 172 173
4767 leaf 98 approx page 172 173
21362 leaf 470 approx page 916 917
26199 leaf 578 approx page 1132 1133
```


### [2026-09-06T22:53:56.937Z] TOOL RESULT

```
53871:Page(s): 655 
54082:Page(s): 655 
56456:Page(s): 655-657 
56910:Page(s): 655 
=== POK_02 leaf for p655 = 655-344=311
Trautmann  134,   Specht  KZ.  65^  212  f.,  Idg.  Dekl.  45,  181.
]s.^sep-  (?)  und  einigermaßen  anklingende  Worte  für  ^Dunkel^
Ai.   ksdjp,   ksapd  ^Nacht^;   av.   x§ap-   ^Dunkelheif^ ;    gr.  ip€(pag,  ipsq)og  n.
,DunkeP;  xpecpagögy  ipecprjvög  ^dunkel^;   x^f^ag  , Dunkel^ ;  dvöcpog  ^Finsternis';
später  yvöcpog  ds.;  hom.  6voq)eo6g  ;dunkel^;  iadvecprig  ;dunkelviolett^ ;    ^6(pog
;Dunkel^;  i^ocpegög  ;dunkel^
Der  wechselnde  gr.  Anlaut  beruht  auf  Tabu -Vorstellungen. WP.  I  524  f.,  WH.  I  289;  Specht  Idg.  Dekl.  11.
k"pei-  s.  richtiger  oben  S.  487  unter  gV:hdei(9-).
Nachtrag  zu  S.  635:
k"äs-  :  k^QS'  ;husten^ ;  Nominalbildung  mit  -t-  erweitert.
Ai.  kä9-,  käsd-  , Husten',  davon  käsate  ,hustet';  alb.  koUe  , Husten'  {*k^äs-lä);  mir. caasacht{ach)  m.  ,Husten',  cymr.  pas  ds.  {*k^93-t-),  pesychu  .husten*  {^k'A9s-t-isk-),  bret.  yaa jHusten*,  com.  paz  ds.;  aisl.  hosti  m.  , Husten',  Sigs.  hwosta,  mnd.  hoste,  ahd.  Mwsto,  alem. wudSte  ds.;  lit.  kosiu  (alt  kosmi),  köseti  ,husten',  lett.  käseju,  käset  de.,  lit.  kosulys,  lett. kasuUs  , Husten' ;  slav.  '^kas^lh  in  russ.-ksl.  kaSelh  »Husten*,  usw.
WP.  I  506,  Trautmann  119.
■Um-
IT
L.
I.  lä-  und  le-  Schallwurzeln:  Präs.  läiö  und  leiö.
Ai.  räyati  ,he[W  (eventuell  auch  zu  re-  ^schreien');  osset.  ram  ^bellen';
arm.  lam  ^weine*^;  unklar  lor  ^WachteF  (s.  unten  gr.  IccQog);
gr.  XTJQog  m.  ^Geschwätz,  PosseU;  Tand^  (enthält  lä-  oder  le-),  X7]Qi(a ^schwätze^;  unklar  ist  der  Vokalismus  (onomatopoetisch?)  in  IccQog  ,Möwe' (vgl.  arm.  lor  ,Wachtel');
alb.  leh  ,helle^;
lat.  lämentum  ^Wehklage^^  lämentäri  ^wehklagen^,  lätrö,  -äre  ^bellen'; vielleicht  osk.  lamatir  ,soll  verflucht  sein^;
air.  llid  (Heieti)  ,klagt  an^;  cymr.  edliio  {*ate-liu-)  ,tadeln^;
g'ot.  lailöun  ,sie  schmähten^  (Präs.  Haian,  idg.  He-)]  anord.  lö  L,  ,Brach- vogel'^,  PL  ler]  lömr  ^Meertaucher^  laut  schreiender  VogeP,  vgl.  isl.  lömur ^Geschrei;  Wehklage^ ;
lit.  löju,  löti  ,bellenS  lett.  läju,  lät  ^bellen,  fluchen^,  ladet  ^verfluchen'; ladet  ^verfluchen';
aksl.  lajq,  lajati  ^bellen,  schimpfen'  usw.  (lajati  für  *lati  nach  dem Präteritalstamm,  vgl.  lit.  löjo).
Redupliziert  lal(l)a-:  ai.  lalallä  ^»Lallen';  gr.  XdXog  ^.geschwätzig',  Xalla , Geschwätz',  laXico  ^schwatze',  XaXayrj  ,leichtes  Gemurmel';  lat.  lallö,  -äre ,in  den  Schlaf  si
```


## [2026-09-06T22:54:13.026Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4740,4770p' KLN_1966.txt | cat -A | grep -n \"\\^L\" | head\necho \"---- raw context\"\nsed -n '4755,4768p' KLN_1966.txt"
}
```


### [2026-09-06T22:54:13.100Z] TOOL RESULT

```
23:Benthamite,  n.,  a  follower  of  Bentham.  M-bM-^@M-^T  See prec.  word  and  subst.  suff.  -ite. benthos,  n.,  the  fauna  and  flora  of  the  bottom  of the  sea.  M-bM-^@M-^T  Gk.  psvffo!;,  M-bM-^@M-^Xdepth  of  the  seaM-bM-^@M-^Y,  prob. rel.  to ^L ViStoz.  M-bM-^@M-^XdepthM-bM-^@M-^Y,  but  influenced  in  form by  ttsvOoc.  M-bM-^@M-^XgriefM-bM-^@M-^Y.  See  bathos, bentonite,  n.,  a  porous  clayey  mineral.  M-bM-^@M-^T Named after  Fort  Benton  in  Wyoming,  U.S.A.  For  the ending  see  subst.  suff.  -ite. benumb,  tr.  v.  M-bM-^@M-^T  ME.  binomen,  pp.  of  biniman, fr.  OE.  beniman,  M-bM-^@M-^Xto  depriveM-bM-^@M-^Y,  lit.,  M-bM-^@M-^Xto  take  awayM-bM-^@M-^Y.$
---- raw context
berry
‘born,  of  a  certain  nature’,  fr.  I.-E.  base  gn-, ‘to  beget,  bear,  bring  forth’,  whence  also  L. gignere,  ‘to  beget,  bear,  bring  forth’,  W.  geni , ‘to  be  bom’.  See  bene-  and  genus  and  cp.  malign. Derivative:  benign-ly,  adv. benignant,  adj.,  kindly.  —  Formed  fr.  benign  on analogy  of  malignant.  For  the  ending  see  suff. -ant.
Derivative:  benignant-ly,  adv. benignity,  n.,  kindliness.  —  ME.  benignite,  fr.  OF. henignite,  fr.  L.  benignitatem,  acc.  of  benignitas, fr.  benignus.  See  benign  and  -ity. benison,  n.,  blessing,  benediction.  —  ME.,  fr.  OF. beneison,  fr.  L.  benedictidnem,  acc.  of  henedictid. See  benediction.
benitoite,  n.,  a  barium  titanosilicate  (mineral.)  — Named  after  San  Benito  River  in  California. For  the  ending  see  subst.  suff.  -ite.
Benjamin,  masc.  PN. ;  in  the  Bible,  Jacob’s  young¬ est  son.  —  Heb.  Binyamtn,  lit.  ‘son  of  the  right hand’,  fr.  ben  ‘son’,  and  yamtn,  ‘right  hand’; see  Gen.  35: 18.  For  the  first  element  see  ben, ‘son’.  Heb.  yamtn  means  also  ‘south’  (lit.  ‘the right  hand,  the  right  side’,  i.e.,  if  one  faces  east). It  is  rel.  to  Aram.-Syr.  yammin,  Ugar.  ymn, ‘right  hand’,  Arab,  ydman,  ‘right  hand,  right side,  south’,  ydmana,  ‘he  was  happy’,  lit.  ‘he turned  or  went  to  the  right’  (the  right  side  was regarded  as  auspicious),  Ethiop.  yaman,  Akkad. imnu,  ‘right  hand,  right  side’.  Cp.  Yemen,  mai- mon,  monkey.
benjamin,  n.,  gum  benzoin.  — Corruption  of  ben- join,  an  earlier  form  of  benzoin  (q.v.) hennet,  n.,  a  herb.  —  ME,  herbe beneit,  ‘the  bless¬ ed  herb’,  fr.  F.  benoite ,  prop.  fern.  pp.  of  OF. beneir  (F.  benir),  ‘to  bless’,  fr.  L.  henedicere. See  benediction.
bensh,  tr.  and  intr.  v.,  to  bless;  to  say  grace.  — Yiddish  benshen,  fr.  dial.  OF.  *bencheir  (OF. beneir ,  F.  benir),  fr.  L.  henedicere.  See  benediction, bent,  adj.,  curved.  —  Pp.  of  bend, bent,  n.,  inclination.  —  Fr.  prec.  word, bent  grass,  also  bent,  n.  —  OE.  beonot-  (in  place names),  rel.  to  OS.  binut ,  OHG.  binuy,  MHG. hin(e)3,  bin3,  ‘rush’.  G.  Binse  developed  fr.  early MHG.  bintz(e),  pi.  of  MHG.  bin(e)3 . Benthamism,  n.,  utilitarianism,  as  taught  by Bentham  (philos.)  —  Named  after  Jeremy  Bent- ham  (1748-1832),  founder  of  the  English  Util¬ itarian  School  of  Philosophy.  For  the  ending see  suff.  -ism.
Benthamite,  n.,  a  follower  of  Bentham.  —  See prec.  word  and  subst.  suff.  -ite. benthos,  n.,  the  fauna  and  flora  of  the  bottom  of the  sea.  —  Gk.  psvffo!;,  ‘depth  of  the  sea’,  prob. rel.  to  ViStoz.  ‘depth’,  but  influenced  in  form by  ttsvOoc.  ‘grief’.  See  bathos, bentonite,  n.,  a  porous  clayey  mineral.  — Named after  Fort  Benton  in  Wyoming,  U.S.A.  For  the ending  see  subst.  suff.  -ite. benumb,  tr.  v.  —  ME.  binomen,  pp.  of  biniman, fr.  OE.  beniman,  ‘to  deprive’,  lit.,  ‘to  take  away’.
formed  fr.  be-  and  niman,  ‘to  take’.  See  nimble, numb.
Derivatives:  benumb-ed,  adj.,  benumb-ed-ness, n.,  benumb-ing,  adj.,  benumb-ing-ly,  adv. benz-,  form  of  benzo-  before  a  vowel, benzene,  n.  —  Fr.  Benzin,  a  name  coined  by  the German  chemist  Eilhardt  Mitscherlich  (1794- 1863)  in  1833;  so  called  by  him  because  he  ob¬ tained  it  through  the  distillation  of  benzoic  acid with  lime.  The  spelling  benzene  is  due  to  A.  W. Hofmann.  See  benzoin.
benzine,  benzin,  n.,  a  volatile,  inflammable  liquid. —  See  benzene  and  chem.  suff.  -ine,  -in. benzo-,  before  a  vowel  benz-,  combining  form meaning  ‘relating  to  benzene’.  —  See  benzene, benzoic,  adj.,  pertaining  to  benzoin.  —  See  ben¬ zoin  and  -ic.
benzoin,  n.,  a  balsamic  resin.  —  F.  benjoin,  fr. Sp.  benjui,  which  is  shortened  fr.  lo-benjui  (the first  syllable  having  been  mistaken  for  the  def. article),  fr.  Arab,  lubdn  jawt,  ‘frankincense  of Java’  (Java  is  the  former  name  of  Sumatra). For  the  etymology  of  Arabic  lubdn  see  leban. benzol,  n.,  benzene.  —  Altered  fr.  Benzin  by  the German  chemist  Baron  Justus  von  Liebig  (1803- 73)  in  1834.  —  See  benzene  and  -ol  (representing L.  oleum,  ‘oil’).
benzoyl,  n.,  a  univalent  radical,  C6H5CO,  found in  benzoic  acid.  —  Coined  by  the  German  chem¬ ists  Baron  Justus  von  Liebig  (1803-73)  and Friedrich  Wohler  (1800-82)  fr.  benzo-  and  -yl. bepaint,  tr.  v.  —  Formed  fr.  pref.  be-  and  paint, beplaster,  tr.  v.  —  Formed  fr.  pref.  be-  and plaster.
bepowder,  tr.  v.  —  Formed  fr.  pref.  be-  and
```


## [2026-09-06T22:54:26.353Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Elohim\\|^Eloah\\|^Elohist\" KLN_1966.txt | head\necho \"=== leaf calc\"\npython3 - <<'EOF'\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\ntargets=[]\nfor i,l in enumerate(lines,1):\n    if re.match(r'^(Elohim|leban)', l): targets.append(i)\nprint(targets)\nEOF"
}
```


## [2026-09-06T22:54:27.608Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ leaf 83 (printed p.66)\"\nawk 'BEGIN{RS=\"\\f\"} NR==84' FVQ_pages.txt | head -40\necho \"=== FVQ leaf 50 (printed p.33)\"\nawk 'BEGIN{RS=\"\\f\"} NR==51' FVQ_pages.txt | head -40"
}
```


### [2026-09-06T22:54:28.320Z] TOOL RESULT

```
12865:Elohim,  n.,  one  of  the  names  of  God  in  the  Bible.
=== leaf calc
[12865]
```


### [2026-09-06T22:54:29.888Z] TOOL RESULT

```
=== FVQ leaf 83 (printed p.66)
66 FOREIGN VOCABULARY OF THE QUR ? AN
'4J| (Alldh).
Of very frequent occurrence.
God.
One gathers from ar-Razi, Mafdfih, i, 84 (so Abu Hayyan, Bcihr,
i, 15), that certain early Muslim authorities hold that the word was of
Syriac or Hebrew origin. The majority, however, claimed that it was
pure Arabic, though they sot forth various theories as to its derivation. 1
Some held that it has no derivation, being A^ - : the Kufans in
- * *
general derived it from o X * I, while the Basrans derived it from
I , taking d 2/ as a verbal noun from O to be high or to be veiled.
The suggested origins for a 2(] were even more varied, some taking
-/* ^ *
it from 43 1 to worship, some from <) I to be perplexed, some from
(jl A) I to turn to for protection, and others from <)j to be perplexed.
Western scholars are fairly unanimous that the source of the
word must be found in one of the older religions. In the Semitic area
JlvK was a widely used word for deity, cf. Heb. H^K ; Aram. H7K ;
Syr. loi!k ; Sab. V1h and s <> Ar. 4) I is doubtless a genuine old
2
Semitic form. The form 4,\J|, however, is different, and there can be
little doubt that this, like the Mandaean N!"INvX and the Pahlavi
ideogram, 2 goos back to the Syr. loii^ (cf. Griinbaum, ZDMG,
xxxix, 571; Sprenger, Lebcn, i, 287-9; Ahrens, Muhammad, 15;
Rudolph, Abhangigkeit, 26 ; Bell, Origin, 54 ; Cheikho, Nasrdniya,
159 ; Mingana, Syriac Influence, 86). The word, however, came into
use in Arabian heathenism long before Muhammad's time (Wellhausen,
Reste, 217 ; Nielsen in HAA, i, 218 ff.). It occurs frequently in the
N. Arabian inscriptions, 3 and also in those from S. Arabia, as, e.g.,
1 They are discussed in detail by ar-Razi on pp. 81-4, of the first volume of his
Tafsir.
2 Herzfeld, Paikuli, Glossary, 135.
3 Cf. Littmann, Entzifferung der thamudenischen Inschriften, p. 63 IF. ; Sem. Inscr,
p. 113 ff. ; and Ryckmans, Noms propres, i, 2 ; RES, iii, 441.
=== FVQ leaf 50 (printed p.33)
INTRODUCTION 33
IjV^.;* * A . Secondly, there was some difference of opinion among the
exegetes as to whether the one who called was Gabriel, standing at the
foot of the hill, or the babe Jesus. Now it seems clear that when they
felt some difficulty over this cl*^, certain of the exegetes who knew
from Christian sources that the one who called was the babe, and
who hacf probably heard of the legends of Jesus speaking to his mother
before his birth, l assumed that C^ could not be taken here in its usual
Arabic meaning of beneath, but must be a foreign word meaning ^.la;
or womb. The guess of Nabataean, of course, has nothing to
support it, for the Aramaic nflD like the Hebrew finD, Syriac A**2,
and Ethiopia ^vlh'h, has exactly the same meaning as the Arabic C
(ii) In xii, 23, we read that Joseph's mistress says to him ^-
The word occurs only in this passage in the Qur'iin and is a rare
expression even outside the Qur'an, though, as has been pointed out
by Earth, 2 there can be no question that it is genuine Arabic. It
was so rare and unusual a word, however, that it was early taken by
the exegetes as foreign 3 and explained as Coptic, 4 doubtless on the
ground that the Egyptian lady would have spoken to her slave in the
Egyptian tongue, and as the only Egyptian language known to
the Muslim nhilologers was Coptic, this rare word was taken to be
of Coptic origin.
Similarly l*JtL in xii, 25, which is explained as Coptic for l$^J J,
was doubtless a case of the same sort, and likewise two other Coptic
suggestions in the same Sura, viz. SU-J^ and 4 uaj of xii, 88, both of
1 Sec Tha'labi, QIAOS (d-AMyn\ p. 269.
2 Spmohwiss. Untersuch, i, 22, with reference to Ibn Ya'Ish, i, 499, line 7. Cf. also
Reckendorf, Die. aytttuktischen VerMUnisse, d?& Arahiscken, Leiden, 1898, p. 325;
Wright, Arabic Grammar, i, 294 d.
3 Biddiqi, Stodicn, 13.
4 Itq, 325. Others thought it Aramaic (Mutaw, 54) or Hauranic (Muzhir, i, 130),
or Hebrew (Itq, 325).
5 Itq, 322, from Al-Wasiti.
5
```


## [2026-09-06T22:54:42.935Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12862,12872p' KLN_1966.txt\necho \"=== leaf\"\npython3 - <<'EOF'\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i in (12865,21362): print(i,'leaf',leaf,'est page',(leaf-12)*2)\n    leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-06T22:54:45.013Z] TOOL RESULT

```
a  pentameter  (the  usual  meter  of  the  elegy)’, neuter  of  sXEyetoi;,  ‘of  the  elegy’,  fr.  sXsyoc,
‘elegy’,  but  influenced  in  form  by  Gk.  EuXoyta,
‘praise’.  See  elegy  and  cp.  eulogy.  Cp.  also  prec. word.
Elohim,  n.,  one  of  the  names  of  God  in  the  Bible.
—  Heb.  Elohim,  pi.  of  El6ah,  ‘God’,  of  un¬ certain  etymology;  possibly  enlarged  fr.  El.  w
See  El.  Cp.  Aram.  Eldh,  in  the  emphatic  state
Elahd,  Syr.  Allahd;  Arab,  lldh,  with  the  article,
A  llihu  (see  Allah).
eloign,  eloin,  tr.  v.,  to  remove  to  a  distance.  —  F. eloigner,  fr.  OF.  esloignier,  fr.  Late  L.  exlongdre, elongare,  ‘to  remove,  keep  aloof’,  which  is formed  fr.  L.  ex,  e,  ‘out  of’  (see  e-),  and  longe,
‘far  off’,  adv.  of  longus,  ‘long’.  See  long,  adj., and  cp.  elongate.
elongate,  tr.  v.,  to  make  long;  intr.  v.,  to  extend.
=== leaf
12865 leaf 278 est page 532
21362 leaf 470 est page 916
```


## [2026-09-06T22:55:01.004Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 53871 54082 56456 56910; do echo \"--- around $L\"; sed -n \"$((L-30)),$((L+2))p\" POK_full.txt | grep -n \"Root / lemma\\|Meaning\\|Page(s)\"; done"
}
```


### [2026-09-06T22:55:02.847Z] TOOL RESULT

```
--- around 53871
14:Page(s): 654-655 
18:Meaning: throat, jaw 
31:Page(s): 655 
33:Root / lemma: lagh-{*lehug''h-) 
--- around 54082
2:Root / lemma: lau- {*lehu-) 
4:Meaning: to acquire, to make use of smth. 
31:Page(s): 655 
--- around 56456
31:Page(s): 655-657 
33:Root / lemma: lehg(h)-1 : l9hg(h)- 
--- around 56910
4:Page(s): 691 
6:Root / lemma: le[i]-1 : lai- 
7:Meaning: to wish 
27:Page(s): 665 
29:Root / lemma: le- 
31:Page(s): 655 
33:Root / lemma: IF-no-
```


## [2026-09-06T22:55:05.852Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Meaning: lip\" POK_full.txt | head\necho \"===\"\ngrep -n \"lemma: leb\\|lemma: lēb\\|lemma: leb-\" POK_full.txt | head\necho \"=== search 'Lippe'\"\ngrep -n \"Lippe\" POK_02.txt | head -20"
}
```


### [2026-09-06T22:55:05.923Z] TOOL RESULT

```
16300:Meaning: lip, kiss 
===
=== search 'Lippe'
733:aksl.  g^ba  , Schwamm,  Pilz',  skr.  güba  , Schwamm,  Aussatz',  sloven.  ggba , Schwamm,  Pilz'^  göbec  m.  ,Maul',  aöech.  hüba  .Schwamm',  jünger  ,Maul, Lippe',  russ.  gubd  ,Baumschwamm' ;  daneben  güba  ,Lippe' ;  im  Slav.  liegt Intonationswechsel  vor,  die  Bedeutung  ,Maul'  ist  überall  jünger.
789:r.-ksl.  i^uju  i^zjou-)  und  hvo,  Ithvati  (*zßv-),  aöech.  zi/i,  zvdti^  russ.  ^ujü, ^evdtb  ,kauen';  dazu  (aus  baltoslav.  *ziccuna)  bulg.  züna  f.  , Lippe'  und skr.  ivälo  n.  , Rachen,  Engpaß',  zväle  f.  PI.  , Gebiß  am  Zaume';  russ. ^vdkatb  ,kauen',  zvak  ,Lärchenharz  als  Zahnputzmittel';
1378:Arm.  jeiun  »Gaumen»  Plafond'; gr.  x^^^^V  »l-iippe,  Kinnlade',  dazu  vielleicht   auch   x^^^og   ,Lippe*,    äol XS^^og,  wenn  aus  *x^X/og  (Solmsen  KZ.  29,  352);
2088:vielleicht  air.  bei  ,Lippe'  {*giiet-lo-s)j  falls  nicht  aus  "^beklo-s  zu  gall. beccos  , Schnabel' ;
4935:daneben  nhd.  dial.  labbe  , Lippe',  labern  , langsam,  einfältig  reden; leckend  trinken',  skr.  läbatl  , saufen  wie  Hunde  oder  Katzen'  u.  dgl.;
5013:iBb-,  ihb-,  lab-,  leb-  , schlaff  herabhängen',  auch  , Lippe'  (?),  z.  T.  mit  anlaut. s- ;  daneben,  aber  weniger  häufig  (s.  dazu  lep-  , abschälen'  am  Schlüsse) Formen  auf  -p-;  nasaliert  {s)lemb(h)-.  Viele  expressive  Bildungen. Gr.  Xoßög  , Schotenhülse,  Samenkapsel;    Ohrläppchen',  l'Uo/Jog  ,schoten- tragend',   Xs^iVjQlg   , Schlangenhaut,   Bohnenhülse'    Hes.,   Xsßivd-oi   , Erbsen'; lat.  nur  mit  n:  läbö,  -äre  ,wanken,  schwanken',  läbor,  -t,  lapsus  , gleiten, sinken,  fehlgehen*;  läheSj  -is  , Einsinken,  Fall,  Erdrutsch;  Untergang,  Ver- derben' und  , Makel,  Schandfleck';  vielleicht  lahor,  -öris  ,Mühe,  Last;  An- strengung;  dann:   Arbeit',   lahöräre  ,sich  mühen,  geplagt  sein'  (eigentlich
5015:,(ias  müde  Wanken  unter  einer  Last*);    wohl  lahium  (laheum),  lahrum (meist  PL  labia,  lahra)  ,Lippe,  Rand';
5018:von  der  Wurzelform  auf  idg.  p  weiter  aisl.  lafa  ,baumeln,  hangen' mhd.  Partiz.  erlaben  , erschlafft*,  Schweiz,  labe  , Pferd  mit  hängenden  Ohren, Ochse  mit  abwärts  gekehrten  Hörnern* ;  schwed.  dial.  labba  , anhängen', ndd.  labbe  ,(hängende)  Lippe*,  ahd.  (aus  dem  Ndd.)  lappa  f.,  mhd.  läppe f.  m.  , niederhängendes  Stück  Zeug,  Lappen* ;
5019:2.  mit  der  Bedeutung  _,Lippe'  als  ,die  hängende*^  (wie  lat,  labium):  mnl. lippe  i.j  nhd.  Lippe,  afries.  ags.  lippa  m.  , Lippe',  (*lepi-an-),  norw.  lepe (Hep-an-),  ahd.  leffui^^  as.  lepiir  ds.,  ahd.  lefs  ,Lefze^  (*lep-s);
6547:j.  IZ2U-  Schallnachahmung  für  den  mit  gepreßten  Lippen  erzeugten  dumpfen Laut:  jUndeutlich  reden,  unartikuliert  murmeln  (daher  auch  Worte  für ,stumm*);  Mund,  Maul;  den  Mund  geschlossen  halten  oder  schließen'; mü-ko-  , stumm'.
6550:3.  [Ai.  mukhd-  n.  ,Mund'  stammt  aus  dem  Davidischen];  gr.  ^vXXov ^Lippe';  fj,vXXaivo)  , verziehe  den  Mund,  schneide  Gesichter'  (fxvara^  , Ober- lippe, Schnurrbart',  s.  Boisacq  m.  Lit.),  ahd.  mala  f.,  mhd.  mül  n.  ,Maul', mnd.  müle  ,Maul,  Schnauze',  aisl.  müli  ,Maul,  bes.  Oberlippe  an  Tieren, hervorragende  Felsspitze',  got.  faurmüljan  ,das  Maul  zubinden'  (ob  mit anl.  s-  dazu  norw.  smaul,  lett.  smaule  ,Maul'??);  s.  auch  unter  möu-lo- S.  750.
6555:Mit  g:  ai.  münjati,  möjati  ,gibt  einen  Ton  von  sich*  (Dhätup.);  mucchanä »schwellender  Ton* ;  gr.  (j,vKco  ,bringe  mit  geschlossenen  Lippen  einen  Laut hervor,  stöhne*  (daraus  lat.  mussäre),  iivyy,6c,  , Seufzer*;
6559:6.  s-Erw. :  gr.^  ui(o  ,sicli   schließen,  von   den   Lippen  und  den  Auo-e^»  ^" (daher  f^voip  ,die  Augen  zusammenkneifend,  kurzsichtig* ;  (.ivdoj  , beiße  die Lippen  zusammen';  von  *iivai6g  ,verschwiegen' :  i^vozrjg  ,in  die  Mysterien Eingeweihter',  (xvaTLY,6g  ,die  Mysterien   betreffend',  ^vazrjQLOv  , Geheimnis geheime   Zeremonie*,  vgl.  auch  ^vsTv  ,in  die  Mysterien  einweihen';   norw mysa  ,die  Augen  zukneifen' ;  aus  dem  Germ,  hierher  auch  mnd.  mummelerL  ~" engl,  mumhle  ,murmeln',  mump,   norw.  mumpa  ds. ;  mhd.  mupf,  muff  ,Ver- Ziehung   des    Mundes',  mupfen,   muffen,   mnd.  mopen,  engl,  mope  ,gaffeii* engl,  mop  ,Fratze';  vielleicht  nhd.  bair.  mäuen  ,wiederkauen'  u.  dgl. ;
```


## [2026-09-06T22:55:12.641Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i in (5013,5019,5015): print(i,'0-based leaf',leaf,'-> printed page',leaf+344)\n    leaf+=l.count('\\f')\nEOF\necho \"=== full block\"\nsed -n '5010,5030p' POK_02.txt"
}
```


### [2026-09-06T22:55:14.949Z] TOOL RESULT

```
5013 0-based leaf 315 -> printed page 659
5015 0-based leaf 315 -> printed page 659
5019 0-based leaf 316 -> printed page 660
=== full block
Hom.  XavKaviTj  ,Kehle,  Schlund',  lit.  pa-laükis  ,die  Wamme  des  Rindes', wruss.  ikac  (*hkati)j  Iter.  lykac  ,schlucken,  trinken'  usw.  (klr.  iyhaty ,schlucken'  mit  h  aus  ursl.  g,  vgl.  die  wohl  verwandte  Wz.  {s)leug- ,schlucken').
WP.  II  380.
ie-  s.  1.  lä-.
iBb-,  ihb-,  lab-,  leb-  , schlaff  herabhängen',  auch  , Lippe'  (?),  z.  T.  mit  anlaut. s- ;  daneben,  aber  weniger  häufig  (s.  dazu  lep-  , abschälen'  am  Schlüsse) Formen  auf  -p-;  nasaliert  {s)lemb(h)-.  Viele  expressive  Bildungen. Gr.  Xoßög  , Schotenhülse,  Samenkapsel;    Ohrläppchen',  l'Uo/Jog  ,schoten- tragend',   Xs^iVjQlg   , Schlangenhaut,   Bohnenhülse'    Hes.,   Xsßivd-oi   , Erbsen'; lat.  nur  mit  n:  läbö,  -äre  ,wanken,  schwanken',  läbor,  -t,  lapsus  , gleiten, sinken,  fehlgehen*;  läheSj  -is  , Einsinken,  Fall,  Erdrutsch;  Untergang,  Ver- derben' und  , Makel,  Schandfleck';  vielleicht  lahor,  -öris  ,Mühe,  Last;  An- strengung;  dann:   Arbeit',   lahöräre  ,sich  mühen,  geplagt  sein'  (eigentlich
656
,(ias  müde  Wanken  unter  einer  Last*);    wohl  lahium  (laheum),  lahrum (meist  PL  labia,  lahra)  ,Lippe,  Rand';
reich  entwickelt  im  Germ. :
1.  isl.  norw.  lapa  , schlaff  herabhängen',  isl.  lajpi  ,homo  sui  negligens*! mhd.  erlaffen  , erschlaffen*,  nhd.  Za^  , schlaff,  matt*;  geminiert:  aisl.  lepp^ m.  (Happja-)  , Lappen,  Locke*,  as.  lappo  , Zipfel,  Lappen*,  mnd.  lapp^ , Stück,  Lappen,  Wamme*,  ags.  Iceppa,  lappa  m.  , Zipfel,  Lappen*  (eno-j^ lap  , Schoß*),  ags.  ear-liprica,  nhd.  (nd.)  Ohr-läppchen  (mit  einf.  p  mn^ öi'-lepel Äs.,  mhd.  leffel  ,Ohr  des  Hasen*,  nhd.  die  Löffel)]  ndd.  laps,  schlaps läpp  ,läppischer,  dummer  Mensch*,  nhd.  Laffe  (*lapan-)]  daneben  auf  ido-, -p:  holl.  laffaard  , Laffe*  —  zunächst  von  hell,  laf  ,matt,  schlaff,  albern* —  und  mit  germ.  hh  mhd.  läppe  —  auch  lape  —  und  nhd.  Läpp,  läppiseh endlich  dehnstufig  mhd.  luof  ,Tölpel';
von  der  Wurzelform  auf  idg.  p  weiter  aisl.  lafa  ,baumeln,  hangen' mhd.  Partiz.  erlaben  , erschlafft*,  Schweiz,  labe  , Pferd  mit  hängenden  Ohren, Ochse  mit  abwärts  gekehrten  Hörnern* ;  schwed.  dial.  labba  , anhängen', ndd.  labbe  ,(hängende)  Lippe*,  ahd.  (aus  dem  Ndd.)  lappa  f.,  mhd.  läppe f.  m.  , niederhängendes  Stück  Zeug,  Lappen* ;
2.  mit  der  Bedeutung  _,Lippe'  als  ,die  hängende*^  (wie  lat,  labium):  mnl. lippe  i.j  nhd.  Lippe,  afries.  ags.  lippa  m.  , Lippe',  (*lepi-an-),  norw.  lepe (Hep-an-),  ahd.  leffui^^  as.  lepiir  ds.,  ahd.  lefs  ,Lefze^  (*lep-s);
3.  mit  anlaut.  s- :  got.  slepan,  saizlep,  as.  släpan,  ahd.  släfan,  ags.  slcepan , schlafen*,  got.  sleps  usw.  , Schlaf*,  aisl.  släpr  , träger  Mensch*,   ndl.  slaap, ahd.  släf  m.,  nhd.  .Schläfe']  mnd.  ndl.  slap  ,schlaff*,   ahd.  slaf  (ff-),  nhd. schlaff,   isl.   norw.   slapa  (=  lapa)    ,schlaff   herabhängen*;    geminiert  aisl.  ^ slappi  ,langer,  verwachsener  Mensch*,  schwed.  slapp  ,arm,  untätig';  ^
mit  idg.  -p-:  aisl.  slafask  ,  erschlaffen*  und  —  von  der  Vorstellung  - herabhängenden  Schleimes  aus  —  wohl  auch  isl.  slafra  , geifern',  mengl. slaveren,  engl,  slave?-  ds.,  isl.  slevja  f.  , Geifer*,  norw.  slevjen  , schleimig, kotig';  norw.  slabbe,  schwed.  slabba  , sudeln',  mndl.  slabben  , besudeln, schlürfen',  nhd.  schlappen  (auch  ,geifern*),  mengl.  slabben  ,sich  im  Kot wälzen',  nhd.  (ndd.)  schlappern,  schlabbern,  schwed.  dial.  slabb  , Schlamm- wasser*, engl.  dial.  slab  ,schleimig,  schlüpfrig',  Subst.  , Schlammpfütze' ;
lit.    slobstü,    slöbti   ,  seh  wach    werden*,   lit.    iem.    släbnas,    ostlit.    sldbnas , schwach',  lett.  släbet  , zusammenfallen'  (von  einer  Geschwulst);
aksl.  slab^  usw.  , schwach'.
Nasaliert  lemh(h)-:
Ai.    rdmbate,    lambate    ,hängt   herab,   hängt   sich   an',    lambana-   ,herab- hängend',  n.  ,herabhängender  Schmuck,  Phlegma';
lat.  limbus  , Besatz  am  Kleid,  Saum';  über  gr.  Xeiicpog  s.  unten;
657
ags.  (ge)Umjpan  , vonstatten  gehen,  glücken',  alid.  limphan,  limfan,  mhd. limpfen  , angemessen  sein',  ags.  gelirnj)  n.  , Ereignis,  Zufall',  mhd.  g{e)limpf Angemessenheit,  schonungsvolle  Nachricht;  Benehmen',  ablautend  andd. geluinp^^^  , passend',  mhd.  limpfen  , hinken',  engl,  to  limp  ,hinken',  limp schlaff  herabhängend',  ndd.  lumpen  ,hinken',  auch  nhd.  (ndd.)  Lumpen ^Fetzen';  vgl.  von  einer  germ.  Nebenwurzel  lemh-  (wäre  idg.  Hemlh-): nihd.  lampen  (und  slampen),  ndd.  lempen  ,welk  niederhängen',  Schweiz. lampe  , Wamme,  herabhängender  Lappen';  ags.  lemp{i)healt  ^hinkend^;
mit  anlaut.  s-:  norw.  dial.  slampa  , nachlässig  gehen',  engl.  dial.  slamp ^ds.,  hinken',  norw.  dial.  slamsa  ,lose  hängen,  baumeln' 5  norw.  (mnd.)  slump , Zufall',  engl,  slump  ,Morast,  nasse  Stelle',  to  slamp,  slump  , plumpsen, klatschen',  mhd.  slampen  , schlaff  herabhängen',  nhd.  dial.  schlampen , schlaff  herabhängen,  nachlässig  sein',  Schlumpe,  Schlampe  , unordentliches Frauenzimmer'  (wohl  mit  ndd.  p);
aisl.  sleppa,  slapp  , entfallen,  entgleiten'  (*slemp-),  Kaus.  sleppa  {*slampian) ]'  ,  fahren  lassen',  engl.  dial.  slemp  , aus  weichen,  wegschleichen,  sich  herab- senken'; von  einer  Wurzelf.  auf  germ.  h  (vgl.  gr.  leficpog  , Schleim,  Rotz'); mnd.  mhd.  slam  (-mm-),  nhd.  Schlamm  (*slamba-),  spätmhd.  slemmen .schlemmen',  norw.  slemba  f.  , Schlampe',  slemha  ,klatschen',  isl.  ,baumeln'; ferner  vielleicht  die  Gruppe  von  mhd.  slimp  (-mb-),  slim  {-mm-)  , schief, schräg'  u.  dgl. ;  vielleicht  zu  lett.  sllps  aus  *slimpas  , schräg,  steil',  lit. nu-sUmpa  , entschlüpft'.
```


## [2026-09-06T22:55:28.566Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==234' HRN.txt | head -60"
}
```


### [2026-09-06T22:55:30.168Z] TOOL RESULT

```
— 212 —
949. (feU ^Welt\
aw. ga^^ya- 'irdisch'; phlv. getlk^).
Mot savant; die den Lautgesetzen entsprechende
neupersische Form ist gehän (No. 951).
950. ges, gesü 'Locken, öelock'.
aw. ga^sa- 'in zwei oder drei (sc. Locken) geord-
netes Haar (ZBÖL); phlv. g^s^ arm. syr. LW. ges,
ü^: *Haar\
oss. d. yesä, t. qts *Borste*.
951. gehän *Welt\ arab. LW. ßhan, jehän^),
aw. gae^ä' (gaf.&anqm); phlv. gehän, vergl. tahn.
r:} (de La gar de, Semitica I, 59).
L.
952. lfrJ)e, läwe 'Schmeichelei, Bitte', lähidefi,, laf 'Prahlerei*.
skr. l^lap' (ai. rap-), Idpati 'schwatzen', vergl.
ud + lap' 'liebkosen .
siyn. I6w-am, sar. lew-am 'reden, sprechen, sagc^n';
af/. laudal 'sagen, erzählen'.
953. leh 'Lippe*, vergl. lefj^ leföe.
Käs. lew; kauk.-bergjüd. low,
phlv. lap; lat. labium; nhd. lAppe (vgl. Kluge,
Etymolog. Wörterbuch s. v.).
kurd. liw 'Lippe'; bei. lap (216); wa;^. law^ lafc,
sangl. law,
954. listen 'lecken*, Praes. les-em, lestden.
Kää. Z. bSles,
phlv. listan, l(i)stan (AV.); ap. l/^*lais- {V^leig^h- + ,<?);
vergl. ai. [/'reh-^ rehmi, skr. teÄ-, lehnii 'ich lecke*;
arm. lizeniy lizum etc. (H. No. 123); wa/. li/'am.
^) Die Syrer schreiben nach Mitteilung des Herrn Prof. Nöldeke
gethih, und so ist also wohl auch im Pehlevl get(Ofi zu lesen. Np. geil
geht aber jedenfalls auf ein, dann allerdings falsches, phlv. ge Ik zurück.
Ist get(i)h etwa von st(Oh beeinflusst?
*) Eine persische Etymologie (von jehlden) siehe Vis und Rämln,
Seite 83 Vers 17.
```


## [2026-09-06T22:55:43.240Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD lab\"\ngrep -n \"^lab \\|^lab$\\|^lab\\b\" PHD.txt | head -20\necho \"--- PHD context\"\ngrep -n \"lip\" PHD.txt | head -20\necho \"=== NYB\"\ngrep -n \"^lab\\|lap .*lip\\|lip'\" NYB_vol2_glossary.txt | head -20"
}
```


## [2026-09-06T22:55:44.657Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins leb\"\ngrep -n \"^leb-\\|^lep-\\|LIP\" AHD_watkins1985.txt | head -20\necho \"=== IEC\"\ngrep -n \"^Leb-\\|^Lēb-\\|^Lep-\\|Leb- \" IEC.txt | head -20\necho \"=== SYN lip\"\ngrep -n \"LIP\" SYN.txt | head -10"
}
```


### [2026-09-06T22:55:45.114Z] TOOL RESULT

```
=== PHD lab
431:lab [lp | M lb, N ~] lip. labag [Pk | (M ? b), P РЬ, N laba] supplication. lābakkar [Pfkkl] suppliant.
4914:lab «rubāy- lipī, rabih rapihwin
--- PHD context
14:For his good counsel on what to include in the dictionary I am most grateful to my friend Dr. P. Gignoux of Paris, for without him many common words would have slipped through my net. Most of the labour of compiling the English index, which will surely be appreciated, was undertaken by my wife. The debt I owe to the teaching of the late Professor W. B. Henning, in connection with Pahlavi and all things Iranian, cannot be expressed in words.
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
431:lab [lp | M lb, N ~] lip. labag [Pk | (M ? b), P РЬ, N laba] supplication. lābakkar [Pfkkl] suppliant.
435:~igih : soldiering. lawzénag [lwcynk' | N ~ina] almond sweetmeat, marzipan. *lipi [/pyh] a minute (of arc).
2643:lip lab.
2818:minute (of arc) lipi.
4914:lab «rubāy- lipī, rabih rapihwin
=== NYB
2348:lap [SPTYN] lip: kar + ~ a kiss 1013. — NP lab.
7250:lab: lap lāb(ah), lāv(ah): rāpak- karēh
```


### [2026-09-06T22:55:45.183Z] TOOL RESULT

```
=== AHD watkins leb
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
555:gvou-. Ox, bull, cow. Nominative singular form *gvéu-s. 1. Germanic *kéuz (> *kiiz) in Old English ci, cy, cye, cow: COW], (KINE); COWSLIP. 2. Latin bds (stem bov-), ox, bull, cow: BEEF, BOVINE, BUGLE!; OvIBos. 3. Greek bous, ox, bull, cow: BOUSTROPHEDON, BUCEPHALUS, BUCOLIC, BULIMIA, BUPRESTID, BUTTER, (BUTYRIC). 4. Sanskrit go-, gauh, cow: GAYAL. 5. Suffixed form *gv6u-ro- in Sanskrit gaurah, wild ox: GAUR. 6. Zero-grade form *guw-d- in Greek hekatombé, “sacrifice of a hundred oxen” (hekaton, hundred; see dekm): HECATOMB. [Pok. gtou- 482.]
576:kal-2, Beautiful. 1. Suffixed form *kal-wo- in Greek kalos, beautiful: CALLISTO; CALOMEL, CALOYER, KALEIDO- SCOPE. 2. Suffixed form *kal-yo- in Greek kallos, beauty: CALLIGRAPHY, CALLIOPE, CALLIPYGIAN. [Pok. 2. kal- 524.]
664:leb-2. Lip. 1. Germanic */ep- in Old English lippa, lip: Lip. 2. Variant form Jab- in: a. suffixed form */ab-yo- in Latin labium, lip: LABIAL, LABIUM; b. suffixed form */ab-ro- in Latin labrum, lip: LABELLUM, LABRET, LABRUM. Com- pare lab-. [Pok. léb- 655.]
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
687:lep-'. To peel. 1. Greek lepein, to peel (> lemma, husk): LEMMA?2, LEPTO-, LEPTON!; SARCOLEMMA. 2. Suffixed form *lep-i- in Greek lepis, lepos, a scale: LEPER, LEPI- DO-, LEPIDOTE. 3. Suffixed variant form */ap-aro- in Greek /aparos, soft: LAPAROTOMY. 4. O-grade form “Jop- in Greek elops, ellops, a fish (< *en-lopos, having scales; en-, in; see en): ELAPID. [Pok. 2. lep- 678.]
688:lep-2. To be flat; palm, sole, shoulder blade. Lengthened o-grade form */ép- in Germanic */6f6 in: a. Germanic *gal6fo (*ga-, collective prefix; see kom), “covering for the hand,” in Old English gl6f, glove: GLOVE; b. Middle Dutch “doef, windward side of a ship, akin to the prob- able Germanic source of Old French lof, spar: LUFF. [Pok. 2. lép- 679.]
774:ne. Not. 1. Germanic *ne-, *na- in: a. Old English ne (> Middle English ne), not, and nd, no: NAUGHT, (NAUGHTY), NEITHER, NEVER, NILL, NO!, NO2, NONE, (NoR!), NOT, NOTHING; b. Old Norse ne, not: NAY; c. Old High German ne, ni, not: NIx?. 2. Latin ne-, not, and nullus, none (ne- + illus, any; see oi-no-): ANNUL, NEFARIOUS, NESCIENCE, NEUTER, (NICE), NISI, NULL, NULLIFY, NULLIPARA. 3. Latin nimis, too much, exces-
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
878:[pulé. Gate. Greek noun of obscure origin. PYLON, PYLO- RUS; AEOLIPILE, MICROPYLE, PROPYLAEUM, PROPYLON.]
955:5. Suffixed form *lag-no- in Greek lagnos, lustful, lasciv- ious (> lagneia, lust, lasciviousness): ALGOLAGNIA. 6. Variant form */ég- in Greek légein, to leave off: CATALECTIC. [Pok. (s)lég- 959.] sleidh-. To slip, slide. 1. Germanic *s/idan, to slip, slide, in Old English s/idan, to slide: SLIDE. 2. Germanic *slid- in: a. Middle Low German sledde, a sled, sledge: SLED; b. Middle Dutch s/éde, a sled: SLEIGH; C. Middle Dutch sleedse, sleigh: SLEDGE. sleng”h-. To slide, make slide, sling, throw. 1. Germanic strong verb *slingwan and derived suffixed noun form *slingw-6- in Old Frisian slinge, sling, akin to the possi- ble source of Middle English sling, sling: SLING}; (SLING- SHOT). 2. Germanic variant strong verb *slinkan in Old English slincan, to creep: SLINK. 3. Suffixed o-grade form *slongh-ri-ko- in Latin lumbricus, intestinal worm, earthworm: LUMBRICOID. [In Pok. (sjleidh- 960, slenk- 961.] sleu-. Hypothetical base of a group of distantly related Germanic derivatives with various suffixes. 1. Germanic *slii-m- in Old English slima, sleep: SLUMBER. 2. Prob- ably Germanic *slautjan- in Old English “s/léte, sleet: SLEET. 3. Germanic *slus- in Norwegian slusk, sloppy weather, probably akin to the possible Scandinavian source of SLUSH. 4. Germanic *sleura- in Middle High German slier, mud, slime: SCHLIEREN. 5. Extended form *sleug- in Germanic ‘*sluk-, *slug- in: a. Norwegian dialectal slugg and Swedish dialectal slagga, slow-mov- ing animal or person, probably akin to the source of Middle English slugge, a sluggard, and sluggen, to be idle: SLUG?, SLUGGARD; b. Dutch /og, lazy, slack: LOGY. [Pok. (s)leu- 962.] sleubh-. To slide, slip. I. Basic form *sleubh-. 1. Ger- manic *slewb- in Old English s/éf, siif, slief, sleeve (into which the arm slips): SLEEVE. 2. Suffixed form *sleubh- ro- in Latin Jibricus, slippery: LUBRICATE, LUBRICITY, LUBRICIOUS. II. Variant Germanic form *sleup-. 1. Ger- manic *slup- in: a. Old English slypa, slyppe, slipa, slime, slimy substance: SLIP’; COWSLIP, OXLIP; b. Old English *sloppe, liquid food (perhaps > Middle English sloppe, a muddy place): sLoP!; c. Old English (ofer)slop, surplice (perhaps > Middle English sloppe, a kind of garment): SLOP?. 2. Germanic *s/aup- in Dutch sloep, sloop (< “gliding boat”): sLoop. [Pok. sleub(h)- 963.] sli-. Bluish. Contracted from *s/is-. 1. O-grade form *sloi- in Germanic *slaihw6n in Old English s/ah, sla, sloe (< “bluish fruit”): SLOE. 2. Suffixed form *sli-wo- in Latin livére, to be bluish: Livip. 3. Suffixed form *s/i-wd- in Serbo-Croatian sijiva, plum: sLivovitz. [Pok. (s)li- 965.] sloug-. Help, service. Celtic and Balto-Slavic. Suffixed form *sloug-o- in Old Irish slag, slog, army, host, whence Gaelic sluagh, army, host: SLEW!, SLOGAN. [Pok. slougo- 965.] smé-. To smear. Contracted from *smeo-. 1. Extended root *smeid- (< *smea-id-) in Germanic *smitan in Old English smitan, to daub, smear, pollute: SMITE. (2. At- tributed by some to this root, but more likely to be of unknown origin, is the Germanic root *mas-, spot, speck, in: a. Middle Dutch masel, pustule, spot, akin to the source of Middle English masel, measles-spot: MEASLES; b. Old French masere, mazre, knot in wood: MAZER.) 3. Attributed by some to this root, but perhaps distinct, is root *smik-, small, in: a. Latin mica, crumb, small piece, grain: MICA; b. Greek (s)mikros, small: MICRO-, MICRON; CHYLOMICRON, OMICRON. [Pok. smé- 966.] smeg-. To taste. Germanic *smak- in: a. Old English smzxc, flavor, taste: SMACK?; b. Middle Dutch and Mid- dle Low German smacken, to taste, make a sound with the lips while tasting food, akin to the source of SMACK!. [Pok. smeg(h)- 967.] smei-. To laugh, smile. 1. Germanic reshaped forms *smer-, *smar- in Old English smercian (with -k- forma- tive), to smile: SMIRK. 2. Germanic extended form *smil- in Swedish smila, to smile, probably akin to the Scandi-
981:ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
985:spergh-. To move, hasten, spring. Nasalized root form *sprengh-. 1. Germanic *springan in: a. Old English springan, to spring: SPRING; b. Middle Dutch springen (> Dutch springen and Afrikaans spring), to leap: KLIP- SPRINGER, SPRINGBOK; C. Old High German springan, to jump: GELANDESPRUNG. 2. Germanic causative *sprang- Jan in: a. Old English besprengan, to sprinkle, scatter: BESPRENT; b. Old English *sprencg, snare used to catch game: SPRINGE. [Pok. spergh- 998.]
1039:s(w)e-. Pronoun of the third person and reflexive (refer- ring back to the subject of the sentence); further appear- ing in various forms referring to the social group as an entity, “(we our-)selves.” 1. Suffixed extended form *sel-bho- in Germanic “selbaz, self, in Old English self, sylf, self, same: SELF. 2. Suffixed form *s(w)e-bh(o)- in Germanic *sibja-, “one’s own,” blood relation, relative, in Old English sibb, relative: s1B; Gossip. 3. Suffixed form *se-ge in Germanic “sik, self, in Old Norse sik, oneself (reflexive pronoun), whence -sk, reflexive suffix, as in biiask, to make oneself ready: BUSK?, (BUSTLE). 4. Suf- fixed form “swoi-no- in Germanic *swainaz, “one’s own (man),” attendant, servant, in Old Norse sveinn, herds- man, boy: SWAIN. 5. Suffixed form *s(u)w-o-, one’s own, in: a. Latin sui (genitive), of oneself: suICIDE; b. San- skrit sva- (< *swo-), one’s own, whence svdmin, “one’s own master,” owner, prince: SWAMI. 6. Extended form *sed in: a. Latin séd, sé, self, oneself (accusative): FELO- DE-SE, PER SE; b. Latin séd, sé, without, apart (< “on one’s Own”): SECEDE, SECERN, SECLUDE, SECRET, SE- CURE, SEDITION, SEDUCE, SEGREGATE, SELECT, SEPA- RATE, (SURE); Cc. Latin compound sdbrius, not drunk (ébrius, drunk; see egh-): SOBER. 7. Possibly suffixed lengthened o-grade form *sd-/o- in Latin sdlus, by oneself alone: SOLE2, SOLITARY, SOLITUDE, SOLO, SULLEN; DESO- LATE, SOLILOQUY, SOLIPSISM. 8. Extended root *swédh-, “that which is one’s own,” peculiarity, custom, in: a. Lat- in soddlis, companion (< “one’s own,” “relative”): so- DALITY; b. suffixed form *swédh-sko- in Latin suéscere, to get accustomed: (CONSUETUDE), CUSTOM, DESUETUDE, MANSUETUDE, MASTIFF; C. Greek éthos, custom, disposi- tion, trait: ETHIC, ETHOS; CACOETHES; d. suffixed form *swedh-no- in Greek ethnos, band of people living to- gether, nation, people (< “people of one’s own kind”): ETHNIC, ETHNO-. 9. Suffixed extended form *swet-aro- in Greek hetaros, later hetairos, comrade, companion: HETAERA. 10. Suffixed extended form *swed-yo- in Greek idios, personal, private (“particular to oneself”):
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1228:ALERT al-1 ALEURONE al-4 ALEXIA feg-1 ALEXIPHARMIC alek- ALGOLAGNIA  slég- ALIAS al-1 “ ALIBI al-1, kWo- ALIBLE al-3 ALIEN al-1 ALIFORM_ aks- ALIKE fik- ALIMENT al-3 ALIMONY al-3 ALIPHATIC leip- ALIQUOT al-1, kwo- ALL al-5
1330:CALL gal-2 CALLIGRAPHY kal-2 CALLIOPE kal-2, wekw- CALLIPYGIAN  kal-2 CALLISTO kal-2 CALLOSE kal-3 CALLOUS kal-3 CALLOW gal-1 CALLUS kal-3
1375:CLIP? gel-1 CLITELLUM klei- CLoAcA kleu-2 cLop gel-1 CLOISONNE kleu-3 CLOISTER kleu-3 CLONE kel-1 CLONUS kel-3 CLOSE kleu-3 CLOSURE kleu-3 CLOT gel-1
1397:COUPLE ap-! COURAGE kerd-1 COURANTE kers-2 COURIER kers-2 COURSE kers-2 COURT gher-1 COURTEOUS gher-1 COURTESAN gher-1 COURTESY gher-' COURTIER gher-1 COUSIN swesor- COUTH gnd- COUTURE syi- COUVADE keu-2 COVE! ku- COVEN gWa- COVENANT gWa- COVER wer-5 COVET kwép- COVEY keu-2 cow! gWou- cow2 ku- COWER ku- COWSLIP gWou-, sleubh- coxa koksa
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
=== IEC
=== SYN lip
5947:4.25 LIP
10796:6.53 SLIPPER
17336:10.42 SLIDE, SLIP (vb.)
```


## [2026-09-06T22:55:56.336Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5947,5990p' SYN.txt"
}
```


### [2026-09-06T22:55:56.379Z] TOOL RESULT

```
4.25 LIP
Gr. xethos Goth. wairiloém (dat. pl.) ar lipa
ie ck ON vorr tt.  lipa ss ala Dan. abe ChSl. ustina - * Jabbro Sw. léppe SCr. usne fr eure OE weler, lippa Boh. vet (pysk) Sp.  labio ME — lippe Pol. warga Rum. buzd NE lp Russ. guba Ir. bal Du. lip Skt. ostha- Nir. _ béal, puisin OHG leffur, lefs Ay. aosta
W. — guefus (weft) MAG: ieee) Br.  gweuz, muzell NHG lppe
Some of the words for ‘lip’ are from the notion of ‘hanging down’ or ‘pro- jecting’. Several are connected with words for ‘mouth’, the lips being the visible part of the mouth.
1. Grk. xefdos, Dor. xfdos, Aeol. XMos (*xédvos; cf. also xedtvn), NG xe (based on pl. 7& xelAn) : ON gjolnar gills’, root connection? Walde-P. 1.682, Falk-Torp 319.
2. Lat. labrum (> It. labro), pl labra, late as f Fike ae em. sg. (> Fr. lévre), ae Sp. labio) : OB lippa, NE 10) fs leffur, lefs, NHG lippe (fr.
» Cle. (see list), root connection un-
Certain, but more prob. : Skt. lamb-
h St Lat. labare ‘slip’, ete. (on IC side, cf, below, 5) than : Lat
mb re sry ba a cg gue. 2.384, Er- 1808 re * Walde-H, 1.738 f. REW ; 18. Falk-Torp 672.
UM. buz¢ R (Cf. below, 3) or like Alb, buze ‘lip’
3. Ir. bél ‘lip’, pl. béozl ‘lips, mouth’, NIz. béal ‘mouth, lip’, etym.? Walde-P. 1.671. Pedersen 1.117.
W. guwefl ‘lip of animals’ = MBr. guefl ‘mouth of animals’, etym.? Stokes 335 (vs. 175).
Ir. bus ‘lip’ (rare), NIr. pus ‘lips, mouth’ (derogatory term), whence regu- lar word puisin, W. gwefus (fr. *gwe-bus; or *gwef-us : gwefl?), Br. gweuz : Alb. buzé, Rum. buzd ‘lip’, NE buss, NHG bus ‘a kiss’, etc., of imitative orig. Walde-P. 2.113 ff. Thurneysen, Kelto- Rom. 86.
Br. muzell, fr. Prov. muzel (Fr. museau) ‘snout, muzzle’, dim. of *misus, It. muso, etc. Henry 208. REW 5784.
4. OE lippa, etc., above, 2.
Goth. wairilém (dat. pl.), ON verr, OFris. were, OE weler (fr. *werel) : OPruss. warsus ‘lip’, and perh. through notion of ‘protuberance’: OE wearr ‘callous skin’, Lat. verrica ‘height’ and
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
230 SELECTED INDO-EUROPEAN SYNONYMS
‘wart’, Skt. varsman- ‘height’, etc. Walde-P. 1.266 ff. Feist 545.
5. Lith., Lett. lpa : LG lobbe ‘hang- ing lip’, Fris. lobbe ‘hanging lump of flesh’, NE lob (NED lob, sb.?), etc., with common notion of ‘loosely hanging’. Walde-P. 2.710.
6. ChSI. ustina, SCr. usne, deriv. of usta ‘mouth’ : Skt. ostha-, Av. aosta- ‘lip’, Lat. ostium ‘door, entrance, river- mouth’, etc., all derivs. of word for ‘mouth’ (4.24). Walde-P. 1.168 ff.
4.26 TONGUE
Grk.  -yAdooa Goth. tuggd NG yAGooa ON tunga Lat. lingua Dan. - tunge It. lingua Sw. tunga Fr. langue OE lunge Sp. lengua ME tounge Rum. limbd NE longue Ir. lenge Du. tong Nir. teanga OHG zunga W. tafod ; MHG zunge Br. teod NHG zunge
The majority of the words for ‘tongue’ belong to an inherited group, of un- known root connection, Secondary as- sociation with words for ‘lick’ is shown bysome. Most of the words for ‘tongue’ are also used for ‘language’ (see 18.24).
1. TH *dyghwa- or the like, but vari- ous phonetic difficulties involved. Walde-P. 1.792. Ernout-M. 553. Walde-H. 1.806 f.
Lat. lingua (> the Romance words), with dial. 7 (supported by association with lingere ‘lick’) fr. old dingua (quot- ed by grammarians); Ir. tenge, NIr. teanga, W. tafod, Br. teod (all with un- explained init. ¢; Pedersen 1.88 assumes init. zd); Goth. tuggd, OF tunge, OHG zunga, etc., general Gmc.; OPruss. in- zuwis, Lith. liezuvis (re-formed by asso- ciation with leZiu ‘lick’), ChSI. jezyki,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Boh, reé : ChSl. rittz ‘peak’, SCy. rt ‘promontory’, Russ. rot ‘mouth’ (4.24),
Boh. pysk = Pol. pysk ‘snout? - Boh. puchnouti, Pol. puchnaé ‘swell’, Grk. gucaw ‘blow’, etc. Walde-P. 2.81. Briickner 449 f.
Pol. warga, perh. : OPruss. warsus ‘lip’, etc. (above, 4). Briickner 609,
Russ. guba : Pol. geba ‘mouth’, ete, (4.24), with shift to ‘lips’ in pl. guby, whence sg. in same sense.
7. Skt. ostha-, Av. aosta-, see above, 6,
Lith. lLesuvis
Lett. méle
Chl.  jezykit
SCr. jezik
Boh. jazyk
Pol. jezyk
Russ. jazyk
Skt. jihua-
Ay. hizva-, hizi-
```


## [2026-09-06T22:55:56.894Z] TOOL CALL #23: Bash

```json
{
 "command": "ls tools/ && grep -n \"1885\\|1886\" data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt | head"
}
```


### [2026-09-06T22:55:56.945Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
```


## [2026-09-06T22:56:07.532Z] TOOL CALL #24: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T22:56:07.537Z] TOOL RESULT

```


```


## [2026-09-06T22:56:11.052Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A8",
 "prompt": "Give the full Persian section etymology for لب (lab) 'lip' — Middle Persian form, Proto-Iranian/Proto-Indo-European reconstruction, cognates cited, and any sources named (Hasandust, Cheung, MacKenzie)."
}
```


## [2026-09-06T22:56:12.317Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/benzoin",
 "prompt": "Give the full etymology of benzoin, and also of benzene and benzine if shown on the page (dates, coiners, Arabic luban jawi, Catalan/Spanish forms)."
}
```


### [2026-09-06T22:56:18.789Z] TOOL RESULT

```
# Persian Etymology for لب (lab) 'lip'

Based on the Wiktionary entry provided, here is the etymological information:

## Etymology Chain

The entry states the word derives "From [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*lab-](/w/index.php?title=Reconstruction:Proto-Iranian/lab-&action=edit&redlink=1 "Reconstruction:Proto-Iranian/lab- (page does not exist)")_ / _[\*lap-](/w/index.php?title=Reconstruction:Proto-Iranian/lap-&action=edit&redlink=1 "Reconstruction:Proto-Iranian/lap- (page does not exist)")_, from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*leb-](/wiki/Reconstruction:Proto-Indo-European/leb- "Reconstruction:Proto-Indo-European/leb-")_ ("lip, to lick")."

## Reconstructions
- **PIE**: *\*leb-* ("lip, to lick")
- **Proto-Iranian**: *\*lab-* or *\*lap-*
- **Persian**: lab

## Sources Cited

The References section lists one etymology source: "Edelʹman, D. I." (2015), *Etimologičeskij slovarʹ iranskix jazykov* [Etymological Dictionary of Iranian Languages], volume 5.

**Note**: The document does not cite Hasandust, Cheung, or MacKenzie for the Persian etymology.
```


### [2026-09-06T22:56:19.858Z] TOOL RESULT

```
# Etymology of Benzoin, Benzene, and Benzine

**Benzoin (noun, 1560s)**
A balsamic resin from an Indonesian tree (*Styrax benzoin*). The term derives from French *benjoin*, which entered Romance languages via Spanish, Portuguese, or Italian from Arabic *luban jawi*, meaning "incense of Java" (though the resin actually came from Sumatra). The Arabic *lu* was mistakenly interpreted as a definite article by Romance speakers. The English form with *-z-* likely reflects Italian influence (*benzoi*, documented in Venice by 1461).

**Benzene (noun, 1835)**
A colorless liquid solvent initially called *benzine*. German chemist Eilhardt Mitscherlich coined *Benzin* in 1833, combining *Benz(oesäure)* ("benzoic acid") with the suffix *-in* (meaning "derived from"). Mitscherlich obtained it through distillation of benzoic acid extracted from benzoin. The hydrocarbon form *benzene* was proposed in 1835 and gained English usage from 1838 onward, though *benzol* (with an alcohol-derived ending) remained common mid-century.

**Benzine**
The original English term for benzene, appearing as an altered form of the German *Benzin* around 1835.
```


## [2026-09-06T22:56:25.870Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leb-",
 "prompt": "What is the reconstructed meaning, and what descendants are listed (Germanic, Latin, Iranian/Persian)? Any references cited (Pokorny page)?"
}
```


## [2026-09-06T22:56:27.851Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%84%D9%87",
 "prompt": "Give the Arabic etymology of الله (Allāh): the analysis (al- + ilāh), the root ʾ-l-h, any Syriac/Aramaic ܐܠܗܐ alāhā connection, and what the Persian section says."
}
```


### [2026-09-06T22:56:32.267Z] TOOL RESULT

```
# Proto-Indo-European *leb- Root

## Reconstructed Meanings

The root has three proposed senses:
1. To hang down loosely
2. Lip
3. To lick

As noted, "The senses 'to hang loosely, flap' and 'to lick' appear unrelated," though an intermediate sense of "tongue" might bridge them.

## Key Descendants

**Germanic**: *lepô, *lipjô ("lip"); *lepaz; Old Norse *lafa*

**Latin**: *labium, labrum* ("lip"); *lambō* ("to lick")

**Iranian/Persian**: Middle Persian *lab*; Persian *لب* (lab, "lip"); Kurdish *lêv* ("lip"); Zazaki *lew* ("lip")

## References

The article cites only one source: De Vaan, Michiel (2008), "Etymological Dictionary of Latin and the other Italic Languages," Brill, page 319. **No Pokorny page reference is provided** in this entry.

## Notable Caveat

The reconstruction is flagged as uncertain and possibly derived from substrate languages or onomatopoetic origins, as "the Iranian initial l- is irregular."
```


### [2026-09-06T22:56:34.066Z] TOOL RESULT

```
# Arabic Etymology of الله (Allāh)

**Analysis:**
The word is "widely theorized to be a contraction of _الٱِلٰه_ (al-ilāh, 'God')" with loss of the initial hamza after the definite article. The root is listed as **ء ل ه** (ʔ l h).

**Semitic Connections:**
The etymology traces to Proto-Semitic _*ʔil-_, with cognates including Classical Syriac _ܐܰܠܳܗܳܐ_ (ʾalāhā) and Aramaic _אֱלָהָא_ (ʾĕlāhā). These related terms demonstrate shared Semitic linguistic ancestry.

**Persian Section Insight:**
The Persian entry confirms the word was borrowed from Arabic _اَللّٰه_ (allāh), ultimately deriving from Proto-Semitic _*ʾil-_, establishing the borrowing chain from Semitic languages through Persian into other linguistic systems.
```


## [2026-09-06T22:56:40.471Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A8%D8%A7%D9%86",
 "prompt": "Arabic لبان: give the etymologies for lubān 'frankincense' and laban 'milk' and the root ل ب ن (l-b-n) 'to be white'. Also any mention of لبان جاوي lubān jāwī."
}
```


## [2026-09-06T22:56:42.070Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%86%D8%B2%DB%8C%D9%86",
 "prompt": "What does Wiktionary say about Persian بنزین (benzin) — its etymology (from French or German or Russian?) and meaning?"
}
```


### [2026-09-06T22:56:46.419Z] TOOL RESULT

```
# لبان (Lubān) - Etymologies

## Primary Meaning: Frankincense

According to the Wiktionary entry, **lubān** (لُبَان) derives from the Semitic root **ل ب ن (l-b-n)** and means "olibanum, frankincense; any kind of gum or resin; chewing gum."

The entry lists this as "Etymology 1" but does not explicitly detail the root's connection to whiteness or provide etymological development beyond referencing the Semitic root system.

## Secondary Meaning: Milk/Dairy

The second entry shows **libān** (لِبَان) functions as the plural of **laban** (لَبَن), meaning milk in Arabic. The Wiktionary source confirms this is a distinct etymological entry but provides no further explanation of how the root relates to the meaning "milk."

## Javanese Variant

The page does not mention **lubān jāwī** (لبان جاوي) or any Javanese-specific variant of frankincense.

**Note:** The Wiktionary article references the root but omits detailed etymological narratives explaining semantic connections between whiteness, milk, and resin.
```


### [2026-09-06T22:56:46.627Z] TOOL RESULT

```
# Wiktionary on Persian بنزین

**Etymology:** According to the source, the Persian word بنزین is "Borrowed from German _[Benzin](/wiki/Benzin#German 'Benzin')_." The etymology traces back through German to Latin and Proto-Indo-European roots.

**Meaning:** The word means "petrol" or "gasoline" in Persian.

So to clarify your question: the borrowing is from **German**, not French or Russian. The German term itself derives from chemical nomenclature (-in suffix) applied to benzene-related compounds, with roots extending back to Latin and earlier proto-languages.
```


## [2026-09-06T22:57:03.054Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 526 528 530; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -25; done"
}
```


### [2026-09-06T22:57:04.490Z] TOOL RESULT

```
=== leaf 526
تدامیر ۱ ۱ ی
دوافروش ٩‏ - و کرانقروش را ی زکویند - ونم بنشر ح بت اول و تالش مروژن کندو ۰.
مکی از شمرای قدیم است ؟ . نام شهری است در دلایت فرچه - و بفتح اول
بنك‌اهیر ه بندست درحوالی‌شیرا زکه و ثالث بروزن‌لنگر ۰ محلی, باش د که قافلموتجار
نان متا لس ای نم خصی پر أ دق بای و رنه
او ساخت ؛ و بسن یکوبند مُردمافری برد امیر بند رد - ینتح اول و ثالث و سکون
تلم » پاراوه خود این بندرا ست ۴ ۰ ثانی ورایع و زای قظمحار , جوال‌دوزرا گوشد,
پندخت « بن اول و ثالث و سکون و بضم اول نیز آمده است . ۱
رخ عبر وف اجه وش برد مان
تا ثالی و وار و غین‌قطمدار » بندی باشد.کمیلچوب
فك « بنم اول بر وزن گنبد » بمعنی و علف و خا وگل در پیش آب بندند تا آب
اصل و بنیاآد هرچیز پاشد * . بلند شود و بزراعت دود .
۱ - < بنکدار . ۴ - مراد کما الدین ابوالفتح بندار بن ابونسر خاطری
رازی مداح ممعدالد, له دیلمی متوفی بسال۰1: و کونده فپلوبات است. « رود کی. غیسی ح ۳
س ۱۱۸۱ . ۳ ۴ - بند امیر در زمان عندالدولهٌ دیلمی (۳۷۲-۳۳۷) برای
مشروب کردن اراضی کربال علیا وسفلی بنا شده وبگفنة مقدسی وامترن‌درآن‌سنگهای سد بواسطة
سرب بهم متصل کردیده .در
آن مدل سصد چر خ‌ساخته
بودند که هر يك آسیابی را
بحرکت دز میآورده است »
وخود سطح آب را بالا برده
مخزن وسیعی تشکیل داده
مقداری ازبرا برای‌هنگام
خشکی ذخیره‌عیکرده است-
این سد چندین بار تا کنون
=== leaf 528
مصفر بن است ۳ که حبة الخترا و چنلافوج .
باشد , و آن بیثثر در کوهها و جنگلها حاسل
۰ میگردد -ونوعی از قماش زمین اطلس بودکه
برآن کلهای زربفت باشد و کلها ونشانها رائیز
گویند که برروی مهوشان از خوردن شراب بهم
میرسد باعرق برپیشانی ابشان شیندب وبشم اول
مصفر بنه است یعنی درخت کوچك ۴ - وبمعنی
کشان واثرهم هست چنانکه گوند «از فلانی بااز
فلانه چیز بنك نمانده است » اراده آن باشد که
نشان واثر تمانده است - وینم اول وسکون ثانی
بنفشه ۱ هم اول و کر اول هردوآمده
است ۰ گلی باشد ممروف
وطبیعت آن سرد وتراست
دردوم وسوم ؛ وممرب آن
بنفسج باشد- ونام کیاهی‌هم
هست که ات روبث.
بفشه گون‌طار م-
۲۳۳
بشثه گون مهد کنابه از آسان
وزهین هردو باشد .
بنقه - فح اول وفاف و سکون نون ؛
نوعی از غله باشد مانتد عدی » و قوت و منغعت
آهم مانثد عدس است .
ماش « بننح اول وئانی وسکون کاف »
وثالث » پوست بیخ ام غیلان باشد. وآن درختی
=== leaf 530
بن کوهی
ممروف است که زیر ره کوش باشد  -‏ و کتابه
ازاطاعت وانقیاد و صدق وادب تمام بود- و سخن
ع ۰ ۳ یز گویند .
لین کوهی» بنتم اول و کسر ثانی »
کیاهی است بیار چرب, واز آن آش پزند.
شاه - بنم اول وسکون ثانی وفتح‌کاف
فلرسی و اظ هار های حوز ۳ نمعنی شگاه است که
جا ومقام ومنزل باشد ۱ - وجاییرا نیز کون که
نقد وجنس درآن گذارند _ و باخفای ها بمنی
بانگه است که کشیدن واز باشد.
پنالاد- بالام بر ون بنیاد ؛ بععنی
بای عمارت و دیوار باشد - و بشتبان دا پیز
کت
پنهین ۴ با میم بروزن پروین » بلفت
زند و پازند (۱) پسررا گویندکه برادر دخثر
است. وبجای تحثانی فوقانی هم‌بنظر آهده است»
وا اعل .
نی ع بفتح اول وضم انی وسکون واو»
خرمن هرچیز را گوبند اعم از گندم وجو و کاه
وعر آن .
پنوان ۴ - ینتم اول بر وزن دربان »
نگهدار ند زراعت و نگاهبان خرمن را گوشد ‏
وضم اول همآمده است- و نگاهدارنده اسباب
وامواق را یز گفته‌اند.
```


## [2026-09-06T22:57:18.551Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== search بنجاوی / جاوی / لبان in BQT_v1\"\ngrep -n \"جاوی\\|لبان\" BQT_v1_pages.txt | head -20\necho \"=== full leaf 528\"\nawk 'BEGIN{RS=\"\\f\"} NR==529' BQT_v1_pages.txt"
}
```


### [2026-09-06T22:57:20.247Z] TOOL RESULT

```
=== search بنجاوی / جاوی / لبان in BQT_v1
1864:زبان ؛ نوتاش -سرمد وجاوید ؛ نر‌نود< فکر ونظر » وند سارت نقمهةً
4996:تلف تقی‌ین محمدین سعیدالدین محمدبلبانی حسنی اط ونمخه 4 خطی آن در کتاخانه آ فای‌مشکوة
8166:بشوران وناجاویده(۱) فروبردن رانیز گویندوبمبی
10272:بود » و اوحیات جاوید بات و اکنون در بپشت
14472:آهن که فیلبانان فیل رابدان بپرطرف که‌خواهند
14748:خاریدن ؛ ناجاویده فرو بردن را گویشد و بعری
14758:بحئی ناجاویده فروبرد و پلع کرد .
15701:فبلبان , لقب سلاطین مقولاست همچنانکه‌فیسس
17267:ثمر آنرا حب‌البان خوانند و در فارسی تخم
17271:باشد که بعربی‌حصین‌البان گوبند - و «شك بید را
17287:حب‌البان راوشد وآنرا در دواحابکار دارند ٩‏ -
18324:بعربی ملك و جلبان گوبند . #
19698:لبان خوانند 4
21312:قدیم وجاوید وهميشه و-رعدباشد ۷.
22037:که چینبان نیز بنام کنگه می شناخته اند « يك قسم بپشت روی زمین ابرالبان مصوب
22721:مجهول بر وزن فرو باریدن, ناجاویده فرو ,بردترا
22737:جاویده فرو برد و بلم کرد , وبمی مصدر عم
22738:که ناجاویده فرو بردن باشد ؛ و در
23906:وجاوید ردایم و باقی و عدام باشد همچو بهشت
=== full leaf 528
مصفر بن است ۳ که حبة الخترا و چنلافوج .
باشد , و آن بیثثر در کوهها و جنگلها حاسل
۰ میگردد -ونوعی از قماش زمین اطلس بودکه
برآن کلهای زربفت باشد و کلها ونشانها رائیز
گویند که برروی مهوشان از خوردن شراب بهم
میرسد باعرق برپیشانی ابشان شیندب وبشم اول
مصفر بنه است یعنی درخت کوچك ۴ - وبمعنی
کشان واثرهم هست چنانکه گوند «از فلانی بااز
فلانه چیز بنك نمانده است » اراده آن باشد که
نشان واثر تمانده است - وینم اول وسکون ثانی
بنفشه ۱ هم اول و کر اول هردوآمده
است ۰ گلی باشد ممروف
وطبیعت آن سرد وتراست
دردوم وسوم ؛ وممرب آن
بنفسج باشد- ونام کیاهی‌هم
هست که ات روبث.
بفشه گون‌طار م-
۲۳۳
بشثه گون مهد کنابه از آسان
وزهین هردو باشد .
بنقه - فح اول وفاف و سکون نون ؛
نوعی از غله باشد مانتد عدی » و قوت و منغعت
آهم مانثد عدس است .
ماش « بننح اول وئانی وسکون کاف »
وثالث » پوست بیخ ام غیلان باشد. وآن درختی
است صحرانی درولات عصمر ۰
بن کار خوددن.- منم اول رکس:
نانی, کنابه ازاندبشه نمودن بجهت عاقبت وانتها
ویایان کار باشد .3۶
۱ -یهلوی۷20۵)502او نوالام». هرن نرابفتح و کسروض‌اول خوانده«اسفا۷:۱ص۲4»,
طبری ۰۷۵1۱1502 مازندرانی کنونی ۷60۵۵56 « واژه نامه ۸۱۰ کیلکی ۵2086512. یره
بننشه ۷۱۵۱2۳1665 دارای کل های نامنظم و مهمیزدار است و دو جنس دارد : بنفشة عمطر
212 ۷۱۵۱۵ که کل آن بمنوان ملین بکار رود و دیگر بنفشة سه رنك با بنفثةٌ فرنگی
65 کهیرای زشت کاشته میشود. « گل گلاب ۲۱۲. ۴ - رك: بن. ۴ - رل: بنه.
بفبه در صفحهٌ ۳۰۹
بقّه از صفحٌ ۳۰۷
۵ ند گی _ بفتح‌اول‌وسوم, از:بنده (بند گه) + ی(حاصل‌مصدد) . په‌لوی 002811 قط
«اسفا ۱ : ۱ ص ۲۵۷ ؛ بنده و غلام بودن - اطاعت و انقیاد . رلك : بنده .
۵ بنده - بقتح اول وسوم» پهلوی معط «منای 6۲۹۹ «یونکره 6۷ یارسی باستان
2 هبد«بار تولمه »٩۲4‏ ازممدر بستن («. م), جمع‌آن بندگان» در پهلوی 3808127
«یب رکه ۳۲»؛ عبده غلام. مقابل آزاد . رك : داثرغالمعارف اسلام .
۵ بنديی - رد : منف ضم اول. (س۳۰۵ح).
۵ بر - رك : بنذ بنم اول . (سه ۳۰ج) ِ
۵ بترئی - بکر اول. ازفرانسه ۳6۵2186 ازابتالبابی 0602108 (روغن بان), کلم
بان از عربی بلغات ارویایی نقل شد. . درسال ۱۸۲۵ ماده ای که اکنون بنزین مینتاميم توسط
علمای شیمی کشف گردید «تقس». ماد شیمیابی مزبور برای حر کت اتومبیل وهواییسا و موتور
کارخانه‌ها نیز با کردن پارچه‌ها ازچربی وغیره بکار روده
» باهش - بفتح اول و دوم . رنك کبود مانند رنك بنفشه - نوعی از جواهر کریمه
6 نی ود.
```


## [2026-09-06T22:57:35.706Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"\\[pdf page 68[0-9]\\]\" BQT_v3_pages.txt | head\necho \"====\"\nawk '/\\[pdf page 681\\]/,/\\[pdf page 684\\]/' BQT_v3_pages.txt | head -80"
}
```


### [2026-09-06T22:57:37.459Z] TOOL RESULT

```
50275:[pdf page 680]
50362:[pdf page 681]
50447:[pdf page 682]
50487:[pdf page 683]
50583:[pdf page 684]
50649:[pdf page 685]
50723:[pdf page 686]
50798:[pdf page 687]
50869:[pdf page 688]
50945:[pdf page 689]
====
[pdf page 681]
لا ۵۵ ۱ » بروزن ‎she‏ بمعنیلابموچرب
‎hs‏ و تملق ۴ و سخن باشد - و بمعتی قریب
و بازی دادن هم آمده است - و بازی چاليك را
نیز گوبند ‎OT,‏ دو پارچه چوب است که اطفال
بدان بازی کنند ,یکی بقدر سه وجب و دیگری
بمقدار يك قبضه و هر دو سر چوب کوتاه تیز
میباشد ۳ .

لاه ۴ = پر وزن ماه » بمعنی لای باشد
که نوعی از ‎ab‏ ابرشمی سرخ ‎Sy‏ است.

1295 Wass ‏با نون بر‎ - ٩ ‏ور‎ oY
‏بمعنی لاهور است و آن شهری باشدممروف.*#‎
‏لاهوره « بر وزن م‌اشوره » تراشه‎

و برش خریزه و هندوانه است وآنرا بت ‎FES‏

میگویند ‎٩‏ .
‎GY‏ - کون بای حلی ‎san)‏
‏کفتن است حمچوهرزه لای (۷) یمنی‌هرزه گوی
و میلاید بعنی میگوید۷ - و بمعنی تالهکننده
وهرزه کوننده بیز گونند ۷ - و آمی ‎cab‏ معنی
هم‌هنت یعلی ‎AW‏ کن و بگوی ۷ - و نوعی از
‎Sib‏ ابرشمی‌باشد که از چینآورند ودر گجرات

. ‏چك : بسکون با‎ (A)

0

نیز بافند وآن ساده و الوان هردو میباشد ۸ -
وگل تیره وسیاه را یز گوبند که در نه حوضها
و ‎lege‏ شیند - و دردی شراب و امثال ‎AT‏
‏یز گفته‌الد - و تای کاغن و ‎Anke‏ و رسمان را
عم ‎Chey SEB GY Ch gram is Kae‏ لای جامه
و يك ‎UY‏ رسمان و بعربی طاق گویند سویمعتی
درة کوه هم‌آهده است که ‎NAG‏ بين دوکوه
باشد .

‎WY‏ ۲ - بروزن شاید » بعنی ثاله کند
وهرزه ‎WP‏ . ۱

‎Sou‏ = بروزن آینده , ناله کننده
و هرزه کوینده را کویند . ,۲

‎Aly .‏ » بروزن قایمی , جامة کوتاهیرا

‏کویند که دروشان و فقیران پوشند ؛و بسنی
‎Late‏ یتمیرا گفته‌اند خواه دروشان پوشندوخواه

‏!= بروزن ناهید » یعنی‌تاله کرد

‏(۷) چش : هرزلای .

‏۱ - فی: پهلوی ‎rapak‏ (در ‎karth‏ _ ۲80816 بمعنی فرباد » ‎(ols‏ » منانسکریت
‎lap.‏ ( وژوزکردن » پر کوبی کردن ) , ق1218 ( ناله کردن » فربادکردن ) ‎By‏ : نیب رکه
ص۱۹۱ ؛کردی 161۲10 12۷20 ( تهاضا کردن » درخواست کردن ) « ژابا س ۳۷۹ > .

‏۴ « اما عاقلتر ازو در جوال‌افتمال غماز و ‎plas‏ شدماند و بسحال وعشوه و لاوة ایشان

‏مقرو رگشته .» « راحةالسدور راوندی بتقل لفت نامه > .
۴ -لای (کیلکی ‎(His‏ اعد تبدیل می» و «م» .

‏ی لاو ‎(Cem)‏
‏۵ رك : لاهور (هم)

‎٩‏ - جمم که چون خربزه است تا لبری چون خورند

‏۲۷ - رك : لایدن .

‏:۰ - اکسون زرنگار فلك را چوآستر

‎Com) ‏اسم فاعل از «لاییدن»‎ - ٩

‏بشکن و پیدا شود ‎cond‏ لاهوره‌ای .

‏مولوی بلخی رومی « ‎Cad‏ نامه » .

‏بر ابر ‎pine‏ این ‎SY‏ ساده یبن .
سیف اسفرنگگ « لفت نامه > .
```


## [2026-09-06T22:57:42.988Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk '/\\[pdf page 682\\]/,/\\[pdf page 685\\]/' BQT_v3_pages.txt"
}
```


### [2026-09-06T22:57:44.668Z] TOOL RESULT

```
[pdf page 682]
ald ‏وا‎

۴ ‏وهرز هکوبی کردن باشد‎ - ۱ cull

ms oly

در لام با بای ابجد مشتمل ‎ey‏ و سه لغت و کنایت
لب - بنتح اول و سکون ‎lt‏ ۰ ممروف از دهان اوآه ‎Siig‏ و نفرین برآید - و طمنه

است و بعربی شفةکویند؟ زنده را یز گوبند .
- و بمعنی سیلی و گردنی ۰ لباچه پروزن سراچه » بمعنی‌بالاپوش
باشد ۴ - و کنار و اطراف وفرجی باشد ‎٩‏ .
هرچیز را نیز گویند . لباد ۲ = بفتح اول‌بروزن سواد ۰ ‎Mele‏
‏لا - بکسر اور ‎‘all rs,‏ اکوبند ععنی‌چیز ی که در روزهای ‎ANAL‏
‎ots‏ بالف ‎sae tS‏ 5۳ پوشند - ‎Js! pay‏ چوبی که ب رکردن کاوعرابه
آغوز است وآن شیری‌باشد که بار اولاز گوسفند و گاو گردون و کاو زراعت گذارند ۸ - و با ثانی
نوزاییده دوشند و گونند عرسته . مشدد بروزن شداد » استاد نمدمال را گونند .
لب ‎wi‏ فشان - کنابه از د ‎Soo‏ = بقتح اول بروزن کباده»,بممنی
ممشوق است - وکنابه از لب شخصی است که | لباداست که جامّبارانی‌باشد*۷- وم اول,چویی
۱ - وعوعوکردن سکه :
پنجه در صید برده ضیقم را چه تفاوت کندکه سکه ‎BY‏ .

. » ‏نامه‎ cab? ‏شیرازی‎ Gone
. ‏شروع می‌دکنم اندران که تا لطفت  . نگویدم که فلانی دراز می‌لاید‎ - ۴
. » ‏نامه‎ Sad > ‏کمال اسماعیل اصفهالی‎
labium ‏لائبتی‎ » lap_ ‏ابرانی‎ i) ‏بلوچی 120 از‎ lap ‏پهلوی‎ ۰ law ‏پازند‎ ۴
۰180- geet Ls ‏از‎ col ‏محتمل‎ (pe) » ‏فارسی > لفجه‎ Uy. ‏از -0ا16‎ Lippe ‏وآلمانی‎
‏سنگلبچی‎ ۰ 1210 law ‏وخی‎ , 16۷ gus ۰۰ ۹۵۳ ‏هوبشمان‎ « ath ) ‏لب‎ ( lew ‏کردی‎
‎.) ‏اسشق ۰۹۵۴ ؛ و فس: لب ولوچه ( درتداول‎ « law
‏لبکی میکی مزنه بشن نا خان حاکم امه بشن‎ - ۴
+ > ‏مردم خراسان ) « مت نامه‎ Engh ‏(کلامی موزون‎
‏رك: اقرب‌الموارد » قطرالمحیط.‎ col ‏در عریی « لباء » بکسر اول بهمین ممنی‎ - ©
‏در برش.‎ IS TAS ‏صبح است رومیی کله سبز برسرش شب حندوی‎ - ٩
.> ‏بدر جاجرمی « لفت نامه‎
Cpe) ‏لباده‎ = ۲
. ‏لباد ز کاو آهن وکاو جوید مراد‎ wae ‏کشاورز بر گاو‎ A
. © ‏طامی > اشتراج‎ ۱
. ‏عریی است . رك : اقرب‌الموارد » منتهی‌الارب , لفت نامه‎ Cem) ald ٩
. ‏را گویند‎ FAV ‏امروزء « لباده ؟ بفتح اول و بتشدید باه , با‎ -*
[pdf page 683]
لبای‌راهب

که کرد نگاو قلبه وگردون گذارند ۱ .

لباس راهب - ‎Hats‏ لیای ‎elke‏
‏است چه لبای رهبانان پیشتر سیاه میباشد ۳ .

لباس ‎GU jaw = ce pe‏ رهبانان
است که کنابه از لبای ‎cle‏ باشد .

لباشن ۳ - ‎cc‏ اول و شین نقطه دار
بروزن فلاخن » بمعنی لواشه است وآن حلفه‌ای
رسمانی باشد که بر چوبی صب کنند ولب بالای
اسبان و خران بد سل را درآن رسمان نهاده‌تاب
دهند تا عاجز شوند و حرکات تا پسندیده‌لکنند.

‎F OL‏ - پروزن ومعنی‌لواشه است که
برلب اسبان وخران ‎Jair‏ گذارند وپیچند

‏لب [ فتاب - شماع آقتاب را گویند
که متصل ‎aly‏ باشد.

‏یالب * - بستی پر و لب‌ریزومالامال
باشد ‎٩‏ - و بمعتی لب برلب نهادن‌هم‌هت‌همیچو
دوشادو ش که دوش بردوض رفتن باشد ,

‎OW‏ بر وزن شبان , صمفی است که
آنراکندر میگویند ۷
پته میباشد و کل و مبوه وبار و تخم ندارد -
و جمم لب همهت که لبپا باشد برخلاف قیای.

‏و درخت آن ماننددرخت

‎wile‏ خشم توچون زبانه برآرد

‏۴ - لبای راهبان پوشیده روزم

‎۱۸۸

‏لب چرا * ‎dione‏ و جیم فاوسی
بر وزن قهقرا » تخود و کشمش و قل و افسام
‎ogee‏ های خشك را کوبند که مردم بوفت صحبت
داش شتن در ‎ole‏ ریزند و کم کم خورند و صحبت
دارند - و یمعتی خوردنی هم‌آمدد است ت ‎tame‏
‏وعلف چاروا را نیز کوبند .

‏لب خضرا - یک تا ونم اه
تقطه‌دار ‎TL, LATEST:‏ د که کنابه از افق
‎ath‏ .

‏لب را ‎pad dase‏ ساخن -
کنابه از شراب خوردن هميشه است بی فاصلةٌ
شبی با روزی +

‎Obed‏ = بمنیلب ‎cattle‏ چه سان‌بمعنی
‎ath wale‏ ورستنیی را کویند که آنرا بتر کی
قچی خوانند و باماست خورند ؛ و بسضی کویند
لبان خردل سحرائی است ‎٩‏ .

‏لب سفید گردن 2 کنابه از تسم
باشد یعتی یم‌خند شدن .

‏لب کشتگاه - بنتح کاف ۰ ‎WS‏
‏رودخانه را کویند و بعربی معبر خوانند.

‏یالاب - بفتم اول و لام بروزن مپتاب»

‏شیر فلك بر نهد یگاو لباده .
کمال اسماعیل اصفهانی « لفت نامه >.

‏چو راهب زان برآرم هرشب آوا .
‎lit >‏ شروانی ص ۲۶ > .

‎. > ‏لواشه , لباشن » لویشه , لواشه , لباچه « لفت نامه‎ » tad aE

‏۴ رك: لباشن .
۹ > ار همست کم

‎(Olibanus oY) Libanos yu, - ۷‏ ازسامی‌مشتق است
عبری 160608 , آرامی ‎og Jin, . lebotta‏ ب
صمغ کند رکه تازه و لبسته باشد « عفار ۱۸۸ ف >.

‏- از : لب ۱-۲ ( واسطه )لب . قس : سرا ء دماوم .

‏اين بار قدح لباب آمد .

‏خاقانی شروالی « لفت نامه » .
ت :آشوری10201,
بمعتی « سفید بودن ‎٩‏ است » بمناسبت‌رنگه
‎A‏ لب‌چره « لقت نامه ».

‎oT ‏است که در دسقوردس‎ Lam ۳5408 ‏لببان شکل عربی‌کلمةً بونانی‎ - ٩
‏شبرق»‎ OG Wa ‏عقار‎ « ) 5108018 arvensis ‏(فر ) ( . بآ‎ moutarde sauvage

‏حشيشة البزارخفج « لفت نامه >.
[pdf page 684]
oe ۱۸۸۷

که ازروم مپآورند وآنرا میعه میگوند .آنچه
از آن روان و آبکی باشد ‎able hoe‏ خوانند »
وعل لبنی هم میگوبند .گرم وخشاك است دد
اول ودویم © - وهرچیز را نیز گوبند که ازشیر
و ‎cob‏ سازلد ‎٩۷‏ .

میا © پنتح اول بر وزن طیید » بمعنی
سخن و کفتگویلاف و گزاف ‎ath‏ واشاره‌بشاعی
رقصه خوان وسخن گزارهم‌هت چه لبیدی‌بمعنی
شاعری وقصه خوانی وسخن ‎GIS‏ باشد ۷ .

لبیدن 4 © پروژن رسیدن» سخنان لاف
‎rs ۳‏ اف زدن وهرزه ‎oS, oe‏ باشد .

لبیذ یوت ‎٩‏ - بنتح اول و آدس ذال
نقطه‌دار و تحتالی بواو کشیده و بنون 1095 بلفت
بونانی دوامی‌است که آنرا پفارسی شبتره گویند
و بعربی عصاب خوانند و معرب آن شیطرج است
و بتعریب اشتهار دارد و درد دنداترا بفایت نافع
است .

بیش ‎oY‏ بروزن کشیش » بمعنی‌لوآشه

است که برلب اسبان‌وخران بدلمل گذارندوپیچند

‎le‏ خوان و ‎Say - a Fl, Syl‏ اول
عشقه را ۱ وآن کیاهی‌باشد که
بر درخت ‎ame‏ وگاه باشد که
درخت را خشك کند و عربان
‎(pT‏ حبل‌السا کین ‎hing‏ بارده
و ‎Smt‏ بارده خواشد .
‎Sold‏ > نتم هر در
لام , چفندر پشته را گوبند که
‎LTE‏ وسیر بشورند ۴ .

‏لینان ۴ - بانون‌بروزن ‏ لبلاب
عشمان * دام کوهی‌است تزديك حم صکه مسکن
فقرا واولیاء ال و افطاب است .
‎Kid‏ © بروزن پلنگه , کرمی باشد که
‎wile Ips LT‏ و بعربی ارضه گوبند ۴ .
‎did‏ > بنتح اول وتالث » بمعنی‌شپشه(۱)
باشد وآن کرمی‌است که غله را ضابع وتباء ‎AS‏
‏و بضم اول » نام آلتی‌است از اسطرلاب .
لبنی © بروزن مدنی» صمغ درختی‌است
)1( خم۱: شبشه » چك , چش : شيشه .
‎٩‏ - لبلاب (بفتح ‎jy‏ بکس‌اول) نام عربی‌ازسربانی‌حبیلبلا ‎tortiller — )hebilbela‏
[فر] ) است ‎Helix L. ( lierre=‏ ۲۱6۵6۲۵ ) « عقار ۲۰۷ ف ).
۴ - چه برد طفل از لش, که ‎oy‏ مست لبلبو . مولوی بلخی رومیه لغت نامه > .
۴ - نام کوهستان سوربه که بداشتن درختان سدر عالی مشهور است وبموازات دربا بطول
۰ کیلومتر کشیده شده و مرتفع‌ترین قلاآن ۳۰۰۰ متر ارتفاع دارد . باقوت کوبد : نام کوهی
که ازعرج ‎Lei‏ مکه ومدینه است - تا بشام کشیده است و مشرف برحمص است وآن‌قسمت
که به اردن است جبل‌الجلیل وآن فسمت که بدمشق است سنیر» ویهحلب وحماة وحمص,ءلبتان
نام دارد وازآ نجا بانطا ‎AS‏ و مصیسه متصل شود وآنجا لام نام گیرد ... « معجم‌البلدان >.
۴ - « شیاطین کفتند ‎Keyl‏ ارضه است بعنی لبنکه » « تضیرابی‌الفتوح چاپ اول ج4

‏ص ‎LON‏ ۵ لبنی ( بضم اول و قتح سوم والف ) نام سامی برای 6۵6685 ( فر )
‎col‏ «عقار ۲۲۸ ‎OS‏ رك : لفت نامه . ۱ - از : لبن(عر) (شیر) +-ی (سبت) .
۲ رك : لییدن . ۸ ‎٩ sada‏ = لبیدیون , از بونانی

‎. ‏عقار۳۱۷ ف‎ » ) Lepidium latifolium L. ) lepidion
: ‏لواشه < لبیشن < لبیشه (هم.)‎ me ۶
. ted ‏تو بيني که اسب توسن را بگه مل بر نپند‎
. » ‏عنصری بلخی « لفت نامه‎
[pdf page 685]
```


## [2026-09-06T22:58:13.074Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT benzoe/luban\"\ngrep -n -i \"benzoe\\|benjoin\\|lubān\\|luban j\" LKT.txt | head -20\necho \"=== DEV benjoin\"\ngrep -n -i \"^benjoin\\|benjoin\" DEV.txt | head -10\necho \"=== PHN benjoin\"\ngrep -n -i \"benjoin\" PHN.txt | head -10\necho \"=== SKT benzoin\"\ngrep -n -i \"benzoin\" SKT.txt | head -5\necho \"=== KFL laban\"\ngrep -n \"لبن\\|اللبن\" KFL.txt | head -10"
}
```


### [2026-09-06T22:58:13.171Z] TOOL RESULT

```
=== LKT benzoe/luban
626:'Weihrauch,  Wohlgeruch';  hieraus  mit ar.  Art.  pg.  albafar,  albafor  'Parfüm aus  Benzoe,  Lavendel  und  aromatischer Cyperngraswurzel  in  starkem  Essig; wohlriechendes  Cyperngras'.  [Constan- cio  Dicc  43  b.]    [DE  62.
3097:'Javanischer  Weihraucli'  [s.  hier  Nr.  1331 ; obwohl  er  aus  Sumatra  stammt],  mit Imiila  [ä  >>  e]  luben  gäwi;  hieraus  mit Abtall  der  er.sten  Silbe  it.  henju\,  belgiu), gebräuchlicher:  belgioina,  henzoino,  frz. boijoin,  kat.  benjugi,  sp.  benjul,  menjid, pg.  beijoim,  beijuim  'Benzoegummi'; ei\\x\.benjamin,  benjoin,  chemischer  Fach- ausdruck, und  Aisdh.. Benzoe;  russ.  benzoi, poln.  benzoes.  Hieraus  weiter  it.  belztiino, frz.  benzin,  dtsch.  Benzin,  Benzol,  russ. benzin,  poln.  (dial.)  b^dzivim  usw.  [Hob- son-Jobson  86/87.  DE  !239.  Eguilaz  344. Devic  DEt  66.  Lammens  Rem  186/187. Gorjajew  15.    MWiD  86.
5753:Benzoe  1332
5975:benjoin  1332
7642:(na)  balykti  208 baragola  145d barakan  250 haran  219 barasnik  258 barasznik  258 barchan  250 bastramy  261 ias^/(/Ä;  260 fcasa;-  278 *     bedew  164 b§dzwim  1332 benzoes  1332 bezestan  280 bezmian  272 biczak  311 hisurman  1516  a ^>o&a^•  181 bohatyr  IIb boraks  356 borsuk  254 borysz(nik)  258 bronz  1657 6mö/v/L-  337 bugaj  339 buhaj  339 bujurdan  346 butany  350 iM?a<  1672 bunczuczny  354 bunczuk  354 &MrÄ;a  221 burnus  365 bursztyn  1004 ftwara  376 buzdygan  333
=== DEV benjoin
814:Benjoin.  Esp.  benjui,  menjut;  portug.  beipim,  beijuim; ital.  belzuino,  belguino.  De  l'arabe  c^^U^  ylîJ  loiibân  djâwi, encens  javanais.  Cette  étymologie,  donnée  par  Valentijn, est  appuyée  d'arguments  solides  dans  le  Gloss.  de  Dozy (p.  289).  Var  javanais,  il  faut  entendre  de  Sumatra,  car  les Arabes  appelaient  cette  grande  île  Java.  C'est  de  Sumatra que  nous  vient  le  benjoin  le  plus  estimé.
815:Le  Dict.  de  Déterville  donne  benjaoy  comme  synonyme de  benjoin,  ce  qui  confirme  l'étymologie  ci-dessus;  mais qu'est-ce  que  benzoenil,  benjoenil,  pour  lesquels  cet  ouvrage renvoie  à  benjoin  et  à  vandle?
1883:Du  reste,  louhan  est  identique  à  Xi^olvos,  ainsi  que  nous l'avons  dit  au  mot  Benjoin.
3021:Beijoim ,  pg.  voy.  Benjoin,
3022:Beijuim,  pg.  voy.  Benjoin.
3023:Belguino,  ital.  voy.  Benjoin,
3032:Bclzuino,  ital.  vov.  Benjoin,
3036:Benjaov,  voy.  Benjoin,
3038:Benjui,  esp.  voy.  Benjoin.
3907:Menjui,  e.sp.  voy.  Benjoin.
=== PHN benjoin
=== SKT benzoin
23806:p^3<)-      , Benzoin,  a  resinous  substance.     (F.—
23807:Span.  —Arab  )  F.  btfijoin, '  guin  benzoin  or
=== KFL laban
4767:لبن « شاط اج لياو ايا ده جل دزااا مسال :الس 
5757:ه- فى ( ل ) ١:‏ يستحيى » بالبناء للمعلوم. 
7025:ه- البِسّم : النَخمه » يقال : بَتْدمْت من الطعام بالكسر ء وَبَشِْمَ الفصيل من كثره شرب اللبن وقد أبشمةٌ الطعام. الصحاح ( بشم ) ه 
7221:لأ قال للطق »يقد » الأها داك عليه البنكه 33 
7404:الآباء: أول اللبن 
9461:ناقه عَرُوزٌ( )٠١‏ : قليله اللبن . 
9501:-٠‏ فى ( ط ) ١:‏ غروز» » وفى نوادر أبى زيد 78« العزز : الضيقه الإحليل » والإحليل مخرج اللبن » وكذ لكك البول. أبو 
9807:أخوار البنول : 
10833:.) وهذه العباره ليست فى ( ل‎ 1٠7" / يقال : ضَيرّه شَكرى : إذا كانت مَلأى من اللبن ». الصحاح ( شكر ) ؟‎ -١ 
10941:8 العاره لبن جهين ب ااي الأعزاق 11 لست فل
```


## [2026-09-06T22:58:32.683Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndef leafof(path, lineno):\n    lines=open(path,encoding='utf-8',errors='replace').read().split('\\n')\n    leaf=0\n    for i,l in enumerate(lines,1):\n        if i==lineno: return leaf\n        leaf+=l.count('\\f')\nfor p,ln,off in [('LKT.txt',3097,26),('DEV.txt',814,30),('SKT.txt',23806,20),('HRN.txt',0,21)]:\n    if ln:\n        lf=leafof(p,ln); print(p,ln,'leaf',lf,'printed page',lf-off)\nEOF\necho \"=== KFL page markers?\"\ngrep -c $'\\f' KFL.txt; head -3 KFL.txt\necho \"=== MON lab\"\ngrep -n \"لب . \\[په\" MON_part2.txt | head -5\ngrep -o \"لب \\. \\[[^]]*\\]\" MON_part2.txt | head -5"
}
```


### [2026-09-06T22:58:34.513Z] TOOL RESULT

```
LKT.txt 3097 leaf 133 printed page 107
DEV.txt 814 leaf 93 printed page 63
SKT.txt 23806 leaf 643 printed page 623
=== KFL page markers?
0
:ا 5 -35 
ال اصمان 
. 
=== MON lab
```


## [2026-09-06T22:58:42.628Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index lip/leb\"\ngrep -n -i \"^LEB\\|LEB-\\|LIP\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -20\necho \"=== ARY pages لب\"\ngrep -n \"لب (\" incoming/ARY/ARY_pages.txt | head -10\ngrep -n \"labium\\|Lippe\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T22:58:42.696Z] TOOL RESULT

```
=== ARY latin index lip/leb
1149:“9 OL5 IS ppt S Coal 09,5 285) a1 Stag y ces staslSal y GV a lip y gles!
1815:we Slip (ailegy GUL; 9 SY 2 5s cel om
3675:BINDEN DUTCH) scla PEisMA GREEK) slip
6252:GENYS, GNATHOS (GREEK) (lip CHENE, CHENG — (KURDISH) 52,5 !
9425:i DU, DON» (i RIsH) AG y! KHTHON AGREER) lip,
11409:(LITHUANIAN) «gy LIP, LIPATI, LIPYATE
12119:KUKUSHKA, KUKUSA KAUKALIAS, KOKKYX :(GREEK) lip
13143:BARNHART: (LIP) 600 LABBRO H(TALIAN) gisle!
13144:‘MACKENZIE: (LIP) 122 LABIO (PORTUGUESE) J\xi 4
13146:ONIONS: (LIP) $30 LIPPA (OLD FRISIAN) 8 53.3
13147:SKEAT: (LIP) 343 (OLD HIGH GERMAN) iff glST
13459:140s seb oby ‘MENO, MENEIN GREER) lip,
15015:EM aay contd cal clan dly Spo b co gh ool ela y clip lanjly Seal sw SKEAT~}
15464:OSEMDESIAT s(SLOVAK) S\ jst EBDOMHTA GREEK) lip
=== ARY pages لب
```


## [2026-09-06T22:58:44.476Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part1/2 لبنیات\"\ngrep -n \"لبنیات\\|لبنیّات\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON بنزین\"\ngrep -n \"بنزین\" MON_part1.txt | head -5\necho \"=== HUB 953 / lab\"\ngrep -n \"953\" HUB.txt | head -10"
}
```


### [2026-09-06T22:58:44.552Z] TOOL RESULT

```
=== MON part1/2 لبنیات
MON_part2.txt:38758:مونث لبنی. شیری؛ ج. لبنیات. (!.) خورا کی 
MON_part2.txt:42398:خوراکی که از انواع لبنیات که از شیر تهیه 
MON_part2.txt:82631:غذای این گونه افراد بیشتر لبنیات است و 
=== MON بنزین
5140:یکی از ترکسات بنزین است و نشانه آن در 
5142:بنزین و برادهٌ آهن و اسید استیک را تقطیر 
7002:نفت یا بنزین یا هوای متراکم و يا گاز حرکت 
7006:بنزین یا گازوئیل حرکت کنند» اطلاق شود. 
20786:با ک: ۰2۲ (.) (مکد.) مخزن بنزین اتومبیل 
=== HUB 953 / lab
3389:953. Np. lab 'Lippe' = paz. law, phi. lap Shk. 257, bal.
```


## [2026-09-06T22:58:52.338Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3386,3394p' HUB.txt\npython3 - <<'EOF'\ndef leafof(path, lineno):\n    lines=open(path,encoding='utf-8',errors='replace').read().split('\\n')\n    leaf=0\n    for i,l in enumerate(lines,1):\n        if i==lineno: return leaf\n        leaf+=l.count('\\f')\nprint('HUB leaf',leafof('HUB.txt',3389),'printed', leafof('HUB.txt',3389)-10)\nEOF\necho \"=== ARY context\"\nsed -n '13130,13160p' incoming/ARY/ARY_pages.txt\ngrep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F'[][]' '{print NR\": \"$0}' | sed -n '1,2p'"
}
```


### [2026-09-06T22:58:54.193Z] TOOL RESULT

```
das Geiger freilich zur Wrzl. skr. da 'geben' stellt
und von lavdql reden, aussagen' trennt. Die ganze
Zusammenstellung ist wohl nicht besonders sicher.
953. Np. lab 'Lippe' = paz. law, phi. lap Shk. 257, bal.
lap setzt ein iranisches lap- voraus, wahrend lat.
labium und deutsch Lippe auf leh- zuriickgehen. Doch
deutet np. lafSa *dicke Lippe' vielleicht auf alteres lah-
Kurd. /^w? Xippe' bei Socin, kurd. Samml. II, 335.
954. Die Ansetzung eines ap. lais ist falsch, durch die
HUB leaf 106 printed 96
=== ARY context
نررس کهن (۸088 01): ۸ اسلاوی کهن (ع/۲شا5 تت#ناتل ص2ل0):
فریزی کهن (/(مل5ل۶# 2ا۵): 0۳۳ 608۸
آلمانی کهن (/(4/ل058 ۲۲04 صا0): 0۳7 روسی (/۸/551۸): زان
: آلمانی (05701۵(7): 07 لیترانی (/7۸(740ا714ل) ققاجاه
انگلیسی کهن (#لدناه2۸/0 ۰:۱۵ ۲۲۸8 لترنی (لتی) (2ف71ا): ان
انگلیسی (تلوانا8/0): زاره
[pdf page 442]
۹
گند گن (به چم "خایه "و "غده) / ۴۳۴۳
پسگشت‌ها ند کرد ما :57
5و 200800 مق ۵0۷۷۵ هام
1 (00(658) :۲62/28 ۸4 برهان قاطع : ۱۳۶
بادداشت:
چم‌های این واژه در زبان‌های غیرایرانی: کاسه» ظرف گرد و گنبد مانند؛ فرورفتگی گرد به شکل کاسه» سس کله. ۱
ا
پهلری (۲7ماتلمه): نان ایتالیایی ((لله4): کیان
کردی (8013[4): 0 پرتغالی (۳0371010895): ان
سانسکریت (54۸/58077): زان ی
پرنانی 0510): 5 6 (00 پسگشت‌ها ار هن دی دادن
لاتین (71ل): 08 ۶0000 .
فرانسه (ح/۸ظ۳۴): ان ورن 6 1287108 :۸5213
اسپانیایی (5۳۸(۷/54): ه00 برهان قاطع : ۴۱
یادداشت:
واژه‌ی انگلیسی 0081۸80 (به چم "گناد" و "خاپه" و "تخمدان") نیز از همین واجریشه آمده است.
اْ
۱
۱ اوستایی (04۷88742۷: سانسکریت (54۸/577): ه0۸0
مت لا۸ 0۸3 رالان6۸ با7ان6۸ لبتوانی ((فا/(هنال72لل): رانا دی
پارسی باستان (( ۰:65 6۸83۸ لتونی (لتی) (1۵(0 7 مل): زان ان
پهلو ی (1ا7ل[۳۸):
6۸0۸615 ,6۸0 پسگشت‌ها 5
1: 1:[pdf page 1]
2: 10:[pdf page 2]
```


## [2026-09-06T22:59:02.482Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=13100 && NR<=13160' incoming/ARY/ARY_pages.txt | grep -n \"pdf page\"\necho \"---\"\nsed -n '13140,13152p' incoming/ARY/ARY_pages.txt\necho \"=== find nearest pdf page tag before 13143\"\nawk 'NR<=13143 && /\\[pdf page/ {p=$0; n=NR} END{print n, p}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T22:59:04.329Z] TOOL RESULT

```
8:[pdf page 441]
37:[pdf page 442]
---
5و 200800 مق ۵0۷۷۵ هام
1 (00(658) :۲62/28 ۸4 برهان قاطع : ۱۳۶
بادداشت:
چم‌های این واژه در زبان‌های غیرایرانی: کاسه» ظرف گرد و گنبد مانند؛ فرورفتگی گرد به شکل کاسه» سس کله. ۱
ا
پهلری (۲7ماتلمه): نان ایتالیایی ((لله4): کیان
کردی (8013[4): 0 پرتغالی (۳0371010895): ان
سانسکریت (54۸/58077): زان ی
پرنانی 0510): 5 6 (00 پسگشت‌ها ار هن دی دادن
لاتین (71ل): 08 ۶0000 .
فرانسه (ح/۸ظ۳۴): ان ورن 6 1287108 :۸5213
اسپانیایی (5۳۸(۷/54): ه00 برهان قاطع : ۴۱
یادداشت:
=== find nearest pdf page tag before 13143
13136 [pdf page 442]
```


## [2026-09-06T22:59:08.927Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13130,13160p' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== nearest pdf tag\"\nawk 'NR<=13143 && /\\[pdf page/ {p=$0; n=NR} END{print n, p}' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-06T22:59:10.703Z] TOOL RESULT

```
Ait Sli 92 Sly gal ge ot
[pdf page 451]
at | tor
eer ENGLISH) 1S: LAP-, LAB- :(OLD PERSIAN) geal gosh
LABE (DANISH) Sail LAP, LAW, LAB: (PAHLAV!) 6 hy,
LAPPE A (SWEDISH) Sf y+ LEW (KURDISH) (52,5
LEPPE NORWEGIAN) 6353 LaP HBALUCHI) ge ge
up (DUTCH) sacle (SANSKRIT) cy Silo
LOPA LITHUANIAN) gid LAMBATE, RAMBATE
LUPA LATVIAN) (2) 3.33 LABOS H(GREEK) gli
LABIUM, LABRUM (LATIN) 3
REFERENCES bewky] °  LEVRE ERENCH) a
POKORNY; ——=~S*S*~*~*«SSSST LABIO LASPANISH) liye!
BARNHART: (LIP) 600 LABBRO H(TALIAN) gisle!
‘MACKENZIE: (LIP) 122 LABIO (PORTUGUESE) J\xi 4
BUCK: 229-230 LEPOR —(OLD SAXON) ofS pS
ONIONS: (LIP) $30 LIPPA (OLD FRISIAN) 8 53.3
SKEAT: (LIP) 343 (OLD HIGH GERMAN) iff glST
RAMAT: u LEFFUR, LEFS
Aad sab oly LIPPE * (GERMAN) git
LIPPA (OLD ENGLISH) 5 Si)
ewtlool
euaT alyssa Sse 2 03ly lee oh
tlnaal gh y ha Be aly coed Jl jog AKI LOBE y gob" slay -¥
LACHE FRENCH) sil 3 SLAKKAR —.(TOKHARIAN A) A 5)
LASSISTA AITALIAN) pity LANGA (SANSKRIT) oy Sail
(OLD SCANDINAVIAN) 4S sho LEGEIN, LEHO AGREEK) gly
SLAKR LAXUS LATIN) gpa
[pdf page 452]
‘SLAK HOLD SAXON) pF gi pS
‘REFERENCES beth, SLAH +(OLD HIGH GERMAN) oS lll
=== nearest pdf tag
13131 [pdf page 451]
```


## [2026-09-06T22:59:25.110Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Allah",
 "prompt": "Give the full etymology entry for Allah (date of first English use, Arabic allāh, al-ilāh, Aramaic/Syriac alāhā, root)."
}
```


## [2026-09-06T22:59:26.590Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%84%D8%A8",
 "prompt": "What does Mo'in's Farhang-e Farsi entry for لب say — the origin tag (e.g. [په.] Pahlavi) and the definitions?"
}
```


### [2026-09-06T22:59:30.324Z] TOOL RESULT

```
# Etymology of Allah

**First English Use:** 1702

**Etymology:** The word derives from Arabic *Allah*, which is a contraction of *al-Ilah*, literally meaning "the God." This breaks down as *al* ("the") + *Ilah* ("God").

**Cognate Languages:** The Arabic *Ilah* is cognate with:
- Aramaic *elah*
- Hebrew *eloah*

**Source Connection:** These terms relate to *Elohim*, the Hebrew name for God in the Bible, which scholars trace to *Eloh* ("God"), itself possibly derived from *El* ("God"), though the ultimate origin remains unknown.

The entry notes this word was spelled *Alha* in early English usage (1702) before standardizing to *Allah*.
```


### [2026-09-06T22:59:30.862Z] TOOL RESULT

```
# Mo'in's Farhang-e Entry for لب

**Origin:** The entry indicates the word has an Arabic origin, marked as [ع.] (Arabic).

**Definitions:** According to Mo'in's dictionary, لب has three meanings:

1. "خالص و برگزیده از هر چیزی" — the pure, selected essence of something
2. "مغز، مغز چیزی" — the core or substance of a thing
3. "عقل" — intellect or reason

The plural form listed is الباب (al-bāb).
```


## [2026-09-06T22:59:38.699Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%D8%A8/",
 "prompt": "Show the فرهنگ معین (Mo'in) section for لب. Are there two entries — one tagged [په.] (Pahlavi) meaning 'lip' and one tagged [ع.] (Arabic) meaning kernel? Quote the Mo'in text."
}
```


## [2026-09-06T22:59:39.271Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=benzoin",
 "prompt": "Give the American Heritage Dictionary etymology for benzoin (and benzene if shown)."
}
```


### [2026-09-06T22:59:44.589Z] TOOL RESULT

```
# Benzoin Etymology

According to the American Heritage Dictionary, benzoin's etymology traces back through multiple languages: "Earlier _benjoin_, from French _benjoin_ and Italian _benzoino_, both from Arabic _lubān jāwī_, frankincense of Java."

The word ultimately derives from Arabic origins meaning frankincense of Java, passing through Romance languages before entering English.

**Note:** The provided content does not include an entry for benzene, only benzoin.
```


### [2026-09-06T22:59:46.049Z] TOOL RESULT

```
# فرهنگ معین Entry for لب

Yes, there are two distinct entries in the Mo'in dictionary:

**Arabic entry [ع.]:**
"(لُ بّ ) خالص و برگزیده از هر چیزی . مغز، مغز چیزی . عقل"
(Pure and selected essence of anything; kernel/marrow; intellect)

**Pahlavi entry [په.]:**
"(لَ ) کنارة هر چیزی . بخش بیرونی دهان"
(Edge of anything; outer part of the mouth)

The dictionary clearly distinguishes these etymologically different terms—one Arabic-origin meaning the essential core, the other Pahlavi-origin referring to the anatomical feature (lip/edge).
```


## [2026-09-06T23:00:12.748Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB benjamin/benzoin\"\ngrep -n -i \"^BENJAMIN\\|BENZOIN\\|luban jawi\\|lubán\" HJB.txt | head -10\necho \"=== AKD labanu\"\ngrep -n -i \"laban\\|libanu\" AKD.txt | head -10\necho \"=== IEC Leb\"\ngrep -n \"^Leb-\\|^Lēb-\\|^Lep-\\|^Lab-\" IEC.txt | head -10\necho \"=== KLN lip\"\ngrep -n \"^lip,\" KLN_1966.txt KLN_1971.txt | head\ngrep -n \"^lip\\b\" KLN_1966.txt | head"
}
```


### [2026-09-06T23:00:12.859Z] TOOL RESULT

```
=== HJB benjamin/benzoin
162:onr  Anglo-Indian  coUoquiaUsmS)  even  if  eventually  traceable  to  native sources  (and  especially  to  Mahratti,  or  Dravidian  originals)  have  come  to us  throngb  a  Portuguese  medium,  and  often  bear  traces  of  having  passed through  that  alembic.  Not  a  few  of  these  are  familiar  all  over  India,  but the  number  current  in  the  South  is  larger  still.  Some  other  Portuguese woids  also,  though  they  can  hardly  be  said  to  be  recognized  elements  in  the Anglo-Indian  colloquial,  have  been  introduced  either  into  Hindustani generally,  or  into  that  shade  of  it  which  is  in  use  among  natives  in  habitual contact  with  Europeans.  Of  words  which  are  essentially  Portuguese,  among Anglo-Indian  colloquialisms,  persistent  or  obsolete,  we  may  quote  goglet, framy  plantain,  muster^  caste,  peon,  padre,  midry  or  maistry,  almyra,  aya,  cohray masqutlo,  pom/ret,  cartuez,  palmyra,  still  in  general  use ;  picoUa,  rolong,  pial, fogass,  margosa,  preserved  in  the  South  ;  hotel,  brab,  foras,  oart,  veUard  in Bombay  ;  joss,  compradore,  linguist  in  the  ports  of  China  ;  and  among  more or  less  obsolete  terms,  Moor,  for  a  Mahommedan,  still  surviving  under  the modified  form  Moorman,  in  Madras  and  Ceylon  ;  Gentoo,  still  partially  kept up,  I  believe,  at  Madras  in  application  to  the  Telugu  language,  mustees,  castees, bandeja  (*  a  tray '),  Kittysol  (*  an  umbrella,*  and  this  survived  ten  years  ago  in the  Calcutta  customs  tariff),  cuspadore  (^  a  spittoon '),  and  covid  ('  a  cubit  or ell*).  Words  of  native  origin  which  bear  the  mark  of  having  come  to  us through  the  Portuguese  may  be  illustrated  by  such  as  palanquin,  mandarin, nangelin  (a  small  weight  for  pearls,  &c.)  m^onsoon,  typhoon,  mango,  mangosteen^ jack-fruit,  batta,  curry,  chop,  congee,  coir,  cutch,  catamaran,  cassanar,  nabobs avadavat,  betel,  areca,  benzoin,  corge,  copra.*  A  few  examples  of  Hindustani words  borrowed  from  the  Portuguese  are  chdbl  (*a  key'),  bdola  (*a  port- manteau'),  6aft«  (*  a  bucket'),  martol  (*a  hammer*),  tauliya  (*a  towel,' Port. toalha),  sdbun  (*soap'),  bdsan  (* plate'  from  Port,  bctcia),  llldm  and  nlldm  (*an auction'),  besides  a  number  of  terms  used  by  Lascars  on  board  ship.
3391:86         BENJAMIN,  BENZOIN.
3408:BENJAMIN,  BENZOIN,  &c.,s.   A
17047:buy  as  much  gold  as  will  fetch  25  in Calecut,  and  there  is  much  lac  {lacra)  and benzoin.  .  .  ."—Roteirt,  112.
17048:1505.— *' Two  merchants  of  Cochin  took on  them  to  save  two  of  the  ships ;  one  from VtKd  with  a  rich  cargo  of  lac  {lacre)^  benzoin, and  musk,  and  another  with  a  caigo  of drugs  from  Banda,  nutmeg,  mace,  dove, and  sandalwood ;  and  they  embarked  on  the shi^  with  their  people,  leaving  to  chance their  own  vessels,  which  had  cargoes  of  rice, for  the  value  of  which  the  owners  of  the ships  bound  themselves."— C(ott«,  i.  611.
17306:for  cinnamon  tv  additional ;  for  benzoin i  additional,  &c.  See  the  P«90f,  &c- of  A.  Nunes  (1554)  passim.  We  have not  been  able  to  trace  the  origin  of this  term,  nor  any  modem  use.
19326:1514.—" .  .  .  Tannazzari,  Samau,  where is  produced  all  the  finest  white  benzoin, storax,  and  lac  finer  than  that  of  Martaman." — Letter  of  Oio»,  d'Empoli,  in  Arch,  Starico JtcUianOf  App.  80.
23925:Benzol,  Benzoin,  87a,
24147:Benjamin,   Benjuy, 866,  87a
=== AKD labanu
=== IEC Leb
=== KLN lip
KLN_1971.txt:137490:lip, lib, ‘life, body’, G. Leib , ‘body’, prop, ‘con- 
KLN_1971.txt:138539:lip, n. — ME. lippe, fr. OE. lippa, rel. to OFris. 
KLN_1971.txt:138548:lip, tr. v., to touch with the lips, to kiss. — Fr. 
KLN_1971.txt:138549:lip, n. ; first used by Shakespeare.
```


## [2026-09-06T23:00:17.699Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3408,3420p' HJB.txt\necho \"=== KLN 1971 lip\"\nsed -n '138539,138550p' KLN_1971.txt\necho \"=== IEC labium\"\ngrep -n \"labium\\|Lippe\\|lippa\" IEC.txt | head -10"
}
```


### [2026-09-06T23:00:17.786Z] TOOL RESULT

```
BENJAMIN,  BENZOIN,  &c.,s.   A
kind  of  incense,  derived  from  the  resin of  the  Styrax  beneoiny  Dryander,  in Sumatra,  and  from  an  undetermined epecies  in  Siam.  It  got  from  the Arab  traders  the  name  htbdn-J^dvl,  i.e. *  Java  Frankincense,'  corrupted  in  the Middle  Ages  into  such  forms  as  we  give. The  first  syllable  of  the  Arabic  term was  doubtless  tdken  as  an  article — lo  bengioi,  whence  bengiai,  henaoin,  and so  forth.  This  etymolcja^y  is  given correctly  by  De  Orta,  and  1^'  Valentijn, and  suggested  by  Barbosa  in  the  quota* tion  b^w.  Spanish  forms  are  oignjui^ menjui;  Modem  Port,  beijoimy  heijuim; Ital.  behuinOy  &c.  The  terms  Jdwd^ Jdwi  were  applied  by  the  Arabs  to  the Malay  countries  generally  (eq)ecially
BENUA.
87
BERIBERI.
Sumatia^  and  their  products.  (See Maireo  Poloy  ii.  266 ;  [Linkhc/ten^  Hak. Soc  ii.  96J  and  the  first  quotation here.)
o.  1360.— "After  a  voyage  of  26  days we  anrved  at  the  laZand  of  JSwa  (here Sumatra)  which  givee  its  name  to  the  JUmA incense  (al-hihftn  al-J&wX)."— Tftit  iSoiuto, It.  228.
1401.— **^Haye  these  thuiffs  that  I  hare written  to  thee  next  tiiy  heart,  and  God giant  that  we  may  be  always  at  peace.  The presents  (herewith) :  Bfluoi;  rotoli  90.  Leg- no  Alo^  rotoli  20.  Due  paja  di  tapeti.  .  ." — Letter  from  the  SoUUa^  of  Effyjpt  to  the Doge  Pasqiiale  Malipiero^  in  the  Ijves  of  the Doges,  Mtaratarif  JioTim  Italicarum  Scriptoret, xzu.  ooL  117a
1498.— "JTanuncs  .  .  .  is  from  Calecat60 days'  safl  with  a  fair  wind  (see  BABNAU) .  •  •  in  this  land  there  is  much  bcdjoim. which  costs  iii  crusados  the  Jwnuallck,  ana much  aioee  which  costs  xxv  onizados  the faraaaDa"  (see  TUAZAJJi).— Jtoteiro  da Viagem  de  V,  da  Gama,  109110.
1616.— "Bei^iay,  each  farasola  Ix,  and  the rery  good  hex  fanams." — Barbota  (Tariff  of Prices  at  OaUcat),  222.
,,      "Bei^uy,  which  Ib  a  resin  of  trees which  the  Moors  caU  lubanJavL^^Ibid.  188.
16S9.— "Cinco  qnintais  de  b«Uoim  de booinas."*— Piato,  cap.  xiii.
1603. — "And  all  these  species  of  bei^uy  the inhabitants  of  the  oonntry  call  coiHin^m,t but  the  Moors  call  them  lonaa  Jaoy,  t.«. *  incense  of  Java'  ...  for  the  Arabs  call incense  /oium." — Oareia,  f .  29r.
=== KLN 1971 lip
lip, n. — ME. lippe, fr. OE. lippa, rel. to OFris. 
lippa , MDu. lippe (whence F. lippe , ‘thick lower 
lip’), Du. lip, OHG. lefs, MHG. lefs, lefse, dial. 
G. Lefze (G. Lippe is borrowed fr. LG.), Swed. 
Idpp , Dan. Isebe, ‘lip’, and prob. cogn. with L. 
labium , labrumf lip’, and prob. also with Toch. A 
lym-, ‘lip’. Cp. labial, labrum. 

Derivatives: lip, v. (q.v.), lip-less , adj. 
lip, tr. v., to touch with the lips, to kiss. — Fr. 
lip, n. ; first used by Shakespeare. 

=== IEC labium
9372:labiom, io (laburom, labs-) ‘lip’. Cf. labudiom & lobos, & cf. WP II, 431, 714 Per. lab “lip, brink’; OLat. labia, Lat. labium & labrum ‘lip’; Ger. Laffe ‘chatterbox’ beside OHG lefs, leffur, m. ‘lip’; Sw. läpp, m. "lip, spout’; cf. (variant) Kurd lews ‘lower lip, blub- ber-lip and OCS lobüzü ‘kiss’. Verbal deri- vatives: OHG laffen, gi-lepphen ‘lick’; MHG laffen, leffen, id.; Sw. lüppja ‘lick, sup; OE leppan “feed titbits. Long-gde in Cz. lábat, v. Jap up’
```


## [2026-09-06T23:00:29.915Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB Allah\"\ngrep -n \"^Allah\\|Al'lah\" WEB_vol1.txt | head -5\necho \"=== FSD Allah\"\ngrep -n \"^Allah\\|Allah, \" FSD_vol1.txt | head -5\necho \"=== RCH allah / labaniyat\"\ngrep -n \"Allah, God\\|allah, God\" RCH.txt | head -5\necho \"=== AFA alaha\"\ngrep -n -i \"ilah\\|alaha\\|Elohim\" AFA.txt | head -8\necho \"=== SKT lip\"\ngrep -n \"^Lip,\\|^Lip\\.\" SKT.txt | head -5\ngrep -n \"Lip, the\" SKT.txt | head -5"
}
```


### [2026-09-06T23:00:30.034Z] TOOL RESULT

```
=== WEB Allah
=== FSD Allah
91167:bKe-ness**,  n.—  dcs'pl-ca-bly,  adc.  highest  peak,  Mus  Allah,  9,591  ft.  Rhod'o-pc*  [Anc.j.
=== RCH allah / labaniyat
=== AFA alaha
617:Elohim-El Sep. Abdr. IG Auni. 2; ül^^io^ » DurclibrucU"? zur
2650:l^JSLs (Nöldeke, Elohim-£l. Sitzungsber. der Akademie zu
7234:den. Vgl. Noldeke Elohim , JH p. 5 (Sep. Abdr.). Im Ara-
=== SKT lip
```


## [2026-09-06T23:00:45.515Z] TOOL CALL #49: Bash

```json
{
 "command": "ls site/pages/304.jpg 2>/dev/null; pdftoppm -f 304 -l 304 -r 150 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg304 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-06T23:00:45.759Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2645,2660p' AFA.txt"
}
```


### [2026-09-06T23:00:47.448Z] TOOL RESULT

```
site/pages/304.jpg
total 128204
drwx------ 7 sfmqrb sfmqrb    12288 Sep  6 19:00 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   774972 Sep  6 18:54 afm143.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1046357 Sep  6 18:54 afm144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1012 Sep  6 18:57 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    26688 Sep  6 18:20 ary377_bot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71464 Sep  6 18:20 ary377_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71267 Sep  6 18:19 ary378_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25966 Sep  6 18:19 ary378_top_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332775 Sep  6 18:33 bqtv2_289_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9689 Sep  6 18:33 bqtv2_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   726576 Sep  6 18:33 bqtv2_n289.jpg
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
-rw-rw-r-- 1 sfmqrb sfmqrb    28249 Sep  6 18:25 build290a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63778 Sep  6 18:33 build290b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68833 Sep  6 18:30 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2612 Sep  6 18:28 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13418 Sep  6 18:28 c_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8430 Sep  6 18:28 c_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11245 Sep  6 18:28 c_katrang.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6717 Sep  6 18:28 c_katvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28872 Sep  6 18:28 c_katvar_zoom.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb     4311 Sep  6 19:00 crop_loll2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3325 Sep  6 19:00 crop_loll3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3612 Sep  6 19:00 crop_loll.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18514 Sep  6 18:52 crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5359 Sep  6 19:00 crop_skt2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4064 Sep  6 19:00 crop_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14732 Sep  6 18:27 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    51742 Sep  6 18:33 e2.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50446 Sep  6 18:33 mk292b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41011 Sep  6 18:29 mk294.py
-rw-rw-r-- 1 sfmqrb sfmqrb    45170 Sep  6 18:47 mk297.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67312 Sep  6 18:51 mk298.py
-rw-rw-r-- 1 sfmqrb sfmqrb    44967 Sep  6 18:51 mk299.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50897 Sep  6 18:54 mk300.py
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
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:33 p290
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:53 p295
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:49 p296
-rw-rw-r-- 1 sfmqrb sfmqrb     9447 Sep  6 18:41 p297_av2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8787 Sep  6 18:41 p297_cav.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2803 Sep  6 18:41 p297_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8189 Sep  6 18:41 p297_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5216 Sep  6 18:55 p303_n18b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7082 Sep  6 18:55 p303_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7046 Sep  6 18:55 p303_n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2952 Sep  6 19:00 p305_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5794 Sep  6 19:00 p305_lat0.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4047 Sep  6 19:00 p305_lat1.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    28862 Sep  6 18:27 pg289_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91779 Sep  6 18:26 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   187988 Sep  6 18:19 pg290hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36312 Sep  6 18:20 pg294_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24759 Sep  6 18:56 pg295_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80086 Sep  6 18:56 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56184 Sep  6 18:39 pg296.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130247 Sep  6 18:41 pg297hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60960 Sep  6 18:39 pg298.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99543 Sep  6 18:52 pg299hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61588 Sep  6 18:56 pg301.png
-rw-rw-r-- 1 sfmqrb sfmqrb   182431 Sep  6 19:00 pg302hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91158 Sep  6 18:59 pg302.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122418 Sep  6 18:55 pg303hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89589 Sep  6 18:52 pg303.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48728 Sep  6 19:00 pg304.png
-rw-rw-r-- 1 sfmqrb sfmqrb   151120 Sep  6 19:00 pg305hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58313 Sep  6 18:59 pg305.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50721 Sep  6 18:58 pg306.png
-rw-rw-r-- 1 sfmqrb sfmqrb   132637 Sep  6 18:38 sns_n155.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129771 Sep  6 18:38 sns_n156.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   130970 Sep  6 18:38 sns_n90.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   531356 Sep  6 18:38 sns_n90_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   124445 Sep  6 18:38 sns_n92.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   522585 Sep  6 18:38 sns_n92_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   495290 Sep  6 18:38 sns_n92_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   351684 Sep  6 18:35 tad_n59.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   342929 Sep  6 18:35 tad_n59_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   242025 Sep  6 18:34 tad_n60_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   282364 Sep  6 18:34 tad_n60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   335678 Sep  6 18:34 tad_n60_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   276093 Sep  6 18:34 tad_n61.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332662 Sep  6 18:34 tad_n62.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 18:35 tad_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   265879 Sep  6 18:35 tad_n65_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


### [2026-09-06T23:00:47.479Z] TOOL RESULT

```
UiA* Gast, gegenüber arab. SLA^uid athiop. §ahf. Hier ha-
ben aber wohl die nordsemitischen Dialecte das Ursprüng-
liche bewahrt, da die bequemere Ableitung von ^Juo »breit
sein*' ist. — Ein Gefass , das bei den yerschiedenen semiti-
schen Völkern yerschiedenen Zwecken diente ist HOp =
l^JSLs (Nöldeke, Elohim-£l. Sitzungsber. der Akademie zu
1) ÜagrgeB itt 3.^4.^ jedenfalls entlehnt ans ptn. jcL» .Schaale** »Knig*\
und dies wird noch sicherer durch die Nebenform ^U^, welche 6aw41iki,
9
Morrenl. Fonch. 133 ult. überliefert Mit j^Uo »Feit** kannetaagenacheiB-
lich tiichti zu thun haben.64
Berlin, Sep.-Abdr. p. 5) jüd. nlHOp, rf.üDp (Kelim 15, l)
:='iy^u^ Ilthiop. kasüt.
Aus dem Aramilischen in*s Arabische übergegangen
sind eine Reihe von Xameu für Wassergeiasse , Becken
und Krüge. Das echt arabische GeHiss dieser Art scheint
```


## [2026-09-06T23:00:50.992Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg304.png"
}
```


### [2026-09-06T23:00:51.018Z] TOOL RESULT

```

```


## [2026-09-06T23:01:07.267Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lip",
 "prompt": "Give the full etymology of the noun lip (Old English lippa, Proto-Germanic *lepjon, PIE *leb-, Latin labium)."
}
```


## [2026-09-06T23:01:09.386Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%87",
 "prompt": "Arabic إله (ʔilāh) 'god': what does Wiktionary give as its etymology, the root ء ل ه, the verb alaha 'to worship/be perplexed', and Proto-Semitic *ʔil-? Also any Aramaic/Syriac cognates."
}
```


### [2026-09-06T23:01:14.022Z] TOOL RESULT

```
# Etymology of Lip (Noun)

Based on the provided content, here's the documented etymological path:

**Old English → Proto-Germanic → Uncertain earlier origin**

The word "lip" descends from Old English *lippa*, meaning "one of the two sides of the mouth." This traces back to Proto-Germanic *lepjan-, which also produced cognates in other Germanic languages including Old Frisian *lippa*, Dutch *lip*, German *Lefze*, and Swedish *läpp*.

**The older connection remains disputed.** Scholars traditionally linked this Germanic group to Latin *labium* ("lip"), but modern etymologists Boutkan and de Vaan reject this Indo-European derivation, though they acknowledge the Latin and Germanic words are likely related.

The source suggests: "It may be a substratum word," indicating the ultimate origin remains unknown—possibly from a non-Indo-European language substrate underlying both language families.

**Semantic evolution:** The transferred sense of "edge or margin of a cup, etc." emerged in the 1590s, while slang meaning "saucy talk" developed by 1821.
```


### [2026-09-06T23:01:16.231Z] TOOL RESULT

```
# Etymology of اله (ilāh) in Wiktionary

Based on the Wiktionary entry, the etymology provided shows:

**Proto-Semitic origin**: The entry traces اله back to "Proto-Semitic _[\*ʔil-](/wiki/Reconstruction:Proto-Semitic/%CA%94il-)" as the root source.

**Arabic borrowing**: In Persian, اله is listed as "Borrowed from [Arabic](https://en.wikipedia.org/wiki/Arabic) _[إِلٰه](/wiki/%D8%A5%D9%84%D9%87#Arabic "إله")_ (ʔilāh)."

The entry does **not** explicitly mention:
- The verb "alaha" meaning 'to worship/be perplexed'
- The Arabic root ء ل ه as a separate etymology element
- Aramaic or Syriac cognates

The Wiktionary source focuses on the Proto-Semitic reconstructed form as the ultimate origin, with Arabic as the immediate source for the Persian borrowing, but doesn't elaborate on intermediate linguistic developments or related Semitic languages.
```


## [2026-09-06T23:01:24.021Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D9%84%D8%A8' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leb-' \\\n 'https://www.etymonline.com/word/lip' \\\n 'https://www.etymonline.com/word/benzoin' \\\n 'https://www.etymonline.com/word/Allah' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 304 verification (roots Layh/A.l.h, L.b.n, Leb)' 2>&1 | tail -2; done"
}
```


### [2026-09-06T23:01:29.096Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e1258dba92a0d269.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/98aeeae14e130138.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ff6e2af5503b9a8c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f502f02d6b07e69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/54dbc6d77ee0f26c.txt
```


## [2026-09-06T23:01:34.343Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%84%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D9%84%D8%A8%D8%A7%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D9%86%D8%B2%DB%8C%D9%86' \\\n 'https://ahdictionary.com/word/search.html?q=benzoin' \\\n 'https://abadis.ir/fatofa/%D9%84%D8%A8/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 304 verification (Allah, laban/luban, benzin, lab)' 2>&1 | tail -2; done"
}
```


### [2026-09-06T23:01:39.286Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/66d84a572403a6ae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4e004e08cffe076b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2302f6242298cdff.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/57abc24296c7f771.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/55a2ddf4173c8447.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6a70d880f2e355f.txt
```


## [2026-09-06T23:01:42.150Z] TOOL CALL #56: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T23:01:42.188Z] TOOL RESULT

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


## [2026-09-06T23:03:02.084Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndef leafof(path, lineno):\n    lines=open(path,encoding='utf-8',errors='replace').read().split('\\n')\n    leaf=0\n    for i,l in enumerate(lines,1):\n        if i==lineno: return leaf\n        leaf+=l.count('\\f')\nprint('PHD line431 leaf',leafof('PHD.txt',431),'printed',leafof('PHD.txt',431)-21)\nprint('NYB line2348 leaf',leafof('NYB_vol2_glossary.txt',2348),'printed',leafof('NYB_vol2_glossary.txt',2348)-8)\nprint('SYN 5947 leaf',leafof('SYN.txt',5947),'printed',leafof('SYN.txt',5947)-24)\nprint('IEC 9372 leaf',leafof('IEC.txt',9372))\nprint('LKT 3097 leaf',leafof('LKT.txt',3097))\nprint('KLN66 4766 leaf',leafof('KLN_1966.txt',4766))\nEOF\necho \"=== BRT aosta\"\ngrep -n \"aošta\\|aosta\" BRT.txt | head -5"
}
```


### [2026-09-06T23:03:04.190Z] TOOL RESULT

```
PHD line431 leaf 76 printed 55
NYB line2348 leaf 135 printed 127
SYN 5947 leaf 265 printed 241
IEC 9372 leaf 369
LKT 3097 leaf 133
KLN66 4766 leaf 98
=== BRT aosta
2969:fromme,  der  es  zuerst  gelehrt  hat,  dass  •  j.  aosta- m. 'Oberlippe',  Du. 'die  beiden
3148:PPfP.  einer  Basis  jJJJfl'j-,  s-  Erneilcrung (/-Aorist,  vgl.  xlnaosta,  xiiiaosiii)  des  \'.  ilnav-. —  VgL  axsaüla-.
8070:•  j.,  g.  izä-'>  f.  1)  'Stieben,  Eifer",  bes. 'frommer,  Glaub enseifer':  manS  voha  uru- nascä  asiiunqm  n>mascä  yä  ärmaiti/ (sd.) °zäcä  Y.4g.io;  —  mat  vä  padäis  (sd.) yä  frasrütä  (sd.)  -zaya  Y,  50. 8 ;  —  ^vldl- hmnäi  (sd.)  'zäcit  (IS.)  .  .  vahistsm  Y.jr. i;  —  ya%a  'za  (IS.)  viicim  näsima  Y, 70.4.  a)  Plur,  in  Verbindung  väwyaostay- usw.,  Plur.;    °m  yaostayS  fora^tayS  ärma-
10058:mit^ü  i) 'hinzukommen,  gelangen  zu  -' (Akk,):  yat  .  .  masdayasna  päaa  ayatitim (sd.)  vä  . .  nasäum  frajasan  V.  6,  26;  8. 73;  —  hanjamatum  frajasöit  Vd.  17;  — '^raosta  .  .  fräymat  usatffam  sBraya  *vx- vitlm  Yt5. 62;  —  nalmim  Aiyjjw  (sd.) /rajasat  Vd,  2;  15,  17,  18.  3)  'daran
10754:um  die  Herrschaft':  haomB  . .  kmsSnJm apa-xid^rim  (sd.)  nilähaya^  yd  raosta  (sd.) 'mya  (IS.)  Y.p.  24.
```


## [2026-09-06T23:03:14.860Z] TOOL CALL #58: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p304 && echo ok"
}
```


### [2026-09-06T23:03:14.909Z] TOOL RESULT

```
ok
```


## [2026-09-06T23:11:01.210Z] TOOL CALL #59: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p304/build.py",
 "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_LAB   = \"https://en.wiktionary.org/wiki/%D9%84%D8%A8\"\nW_LEB   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/leb-\"\nE_LIP   = \"https://www.etymonline.com/word/lip\"\nE_BENZ  = \"https://www.etymonline.com/word/benzoin\"\nE_ALLAH = \"https://www.etymonline.com/word/Allah\"\nW_ALLAH = \"https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%84%D9%87\"\nW_ILAH  = \"https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%87\"\nW_LUBAN = \"https://en.wiktionary.org/wiki/%D9%84%D8%A8%D8%A7%D9%86\"\nW_BENZ  = \"https://en.wiktionary.org/wiki/%D8%A8%D9%86%D8%B2%DB%8C%D9%86\"\nAHD_BENZ= \"https://ahdictionary.com/word/search.html?q=benzoin\"\nAB_LAB  = \"https://abadis.ir/fatofa/%D9%84%D8%A8/\"\n\ndoc = {\n  \"pdf_page\": 304,\n  \"book_page\": 274,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n  \"entry\": 0,\n  \"root\": \"Layh; A.l.h\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Arabic اللّٰه allāh 'God' < al- + ʾilāh, from Proto-Semitic *ʔil- 'god' (Heb. ʾēl / ʾĕlōah, Aram. ʾĕlāh, Syr. ʾalāhā); the definite form probably taken over from Syriac ʾalāhā\",\n  \"note\": \"Nourai's root box gives two Arabic 'roots' — لاه lāha 'to be high (or veiled)' and أ ل ه ʾ-l-h 'to worship' — with the language label 'Semitic / Syriac'. Both halves come straight from the page he cites, Jeffery, Foreign Vocabulary of the Qur'an p.66, where they are reported as the opinions of the medieval Arab philologists: 'the Kufans in general derived it from al-ilāh, while the Basrans derived it from ilāh, taking lāh as a verbal noun from lāha to be high or to be veiled. The suggested origins for ilāh were even more varied, some taking it from alaha to worship…'. Jeffery himself, on the same page, rejects all of them: 'Western scholars are fairly unanimous that the source of the word must be found in one of the older religions… ilāh is doubtless a genuine old Semitic form. The form allāh, however, is different, and there can be little doubt that this, like the Mandaean and the Pahlavi ideogram, goes back to the Syr. ʾalāhā.' Modern comparative Semitics (Klein s.v. Elohim; Wiktionary) treats ʾilāh as a noun continuing Proto-Semitic *ʔil- 'god', not as a deverbal from a root 'to be high' or 'to worship'; the denominative verb ʾalaha 'to worship' is secondary to the noun. So the 'Syriac' half of the label is well founded and matches Nourai's own source, while the glosses 'to be high; to worship' reproduce the Arab lexicographers rather than modern scholarship — hence plausible, not confirmed.\",\n  \"note_fa\": \"نورایی ریشه را «Layh؛ A.l.h» با معنی «بلند بودن؛ پرستیدن» و برچسب «سامی/سریانی» آورده است. هر دو معنی عیناً از همان صفحه‌ای گرفته شده که خودِ او ارجاع داده، یعنی جفری، «واژه‌های دخیل در قرآن» ص۶۶، آنجا که آرای لغویان قدیم عرب نقل شده است: بصریان «الله» را از «إله» و آن را مصدرِ «لاهَ» به معنی «بلند شدن/پوشیده شدن» می‌دانستند و گروهی «إله» را از «أَلِهَ» به معنی «پرستیدن». اما جفری در همان صفحه این آرا را نمی‌پذیرد و می‌گوید صورتِ معرفهٔ «اللّٰه» به احتمال بسیار از سریانی ʾalāhā گرفته شده و «إله» صورتی کهن و اصیل سامی است. ریشه‌شناسی امروزی (کلاین ذیل Elohim، ویکی‌واژه) «إله» را بازماندهٔ سامی آغازین *ʔil- «خدا» می‌داند نه مشتق از فعل؛ فعلِ «أَلَهَ/أَلِهَ» خودْ اسم‌بنیاد و ثانوی است. بنابراین برچسب «سریانی» درست و مستند است، ولی معناهای «بلند بودن؛ پرستیدن» دیدگاه لغویان کهن است نه پژوهش نو: ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_ALLAH, W_ILAH, E_ALLAH],\n  \"ref_check\": [\n    {\"ref\": \"KLN:505\", \"status\": \"partial\",\n     \"note\": \"Klein 1966 s.v. Elohim (KLN_1966.txt line 12865, leaf 278): 'Elohim, n., one of the names of God in the Bible. — Heb. Elōhīm, pl. of Elōah, \\\"God\\\", of uncertain etymology; possibly enlarged fr. El. See El. Cp. Aram. Elāh, in the emphatic state Elāhā, Syr. Allāhā; Arab. ilāh, with the article Allāhu (see Allah).' The Syriac/Aramaic/Arabic equation Nourai draws is there verbatim, but Klein says the etymology is 'uncertain' and gives no root 'to be high' or 'to worship'.\"},\n    {\"ref\": \"FVQ:66\", \"status\": \"supports\",\n     \"note\": \"Jeffery, FVQ p.66 (FVQ_pages.txt leaf 83, running head '66 FOREIGN VOCABULARY OF THE QURʾAN'), s.v. Allāh: '…the Basrans derived it from ilāh, taking lāh as a verbal noun from lāha to be high or to be veiled. The suggested origins for ilāh were even more varied, some taking it from alaha to worship…'; and 'there can be little doubt that this… goes back to the Syr. ʾalāhā'. This single page is the source of both of Nourai's root glosses and of his 'Semitic / Syriac' label.\"},\n    {\"ref\": \"VDQ:125\", \"status\": \"not_checked\",\n     \"note\": \"Badre'i's Persian translation of Jeffery (noorlib.ir/book/view/12868) is a JavaScript page viewer that WebFetch cannot render; since it is a translation of FVQ the substance was verified on FVQ p.66 instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"FVQ\", \"where\": \"p.66 s.v. Allāh (FVQ_pages.txt leaf 83)\", \"stance\": \"partial\",\n     \"note\": \"Reports the Arab lexicographers' 'lāha = to be high' and 'alaha = to worship' but rejects them: 'Western scholars are fairly unanimous that the source of the word must be found in one of the older religions… ilāh is doubtless a genuine old Semitic form.'\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. Elohim, p.505 (KLN_1966.txt line 12865)\", \"stance\": \"partial\",\n     \"note\": \"'…of uncertain etymology; possibly enlarged fr. El… Aram. Elāh… Syr. Allāhā; Arab. ilāh, with the article Allāhu.'\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter (AFA.txt lines 617, 2650, 7234)\", \"stance\": \"silent\",\n     \"note\": \"Fraenkel only refers to Nöldeke's paper 'Elohim–El' in passing (in a note on vessel-names); he has no article on ilāh/Allāh, so the local Aramaic-loanword handbook is silent on this root.\"},\n    {\"src\": \"KFL\", \"where\": \"Thaʿālibī, Fiqh al-lugha (KFL.txt, grep 'اله')\", \"stance\": \"silent\",\n     \"note\": \"The local OCR of Thaʿālibī is very poor and unpaginated; no usable article on الله was found.\"}\n  ],\n  \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"Al-lah, Allah; A.l.h\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Arabic اللّٰه allāh is the definite form al-ilāh 'the god' with the ʾ of ilāh elided after the article (al-ʾilāh > allāh, with the emphatic 'dark' lām of the divine name); the indefinite noun إله ʾilāh 'a god' continues Proto-Semitic *ʔil- 'god' (Heb. ʾēl, pl. ʾĕlōhīm; Aram. ʾĕlāh, emph. ʾĕlāhā; Syr. ʾalāhā; Ugar. il). The consonantal 'root' ʾ-l-h that Arab grammarians extract, and the verb ʾalaha 'to worship, adore', are back-formations from the noun. Klein and Etymonline give the same analysis (al- 'the' + ilāh 'God'); Jeffery adds that the definite form itself, already current in pre-Islamic North- and South-Arabian inscriptions, most probably reflects Syriac ʾalāhā. Nourai's node — 'Al-lah, Allah: the God' plus the root 'A.l.h: God' — is exactly this.\",\n  \"derivation_fa\": \"«اللّٰه» در عربی همان «الْإله» است که همزهٔ «إله» پس از حرف تعریف افتاده و لامِ مفخّم نام خدا پدید آمده است (al-ʾilāh > allāh). اسمِ «إله» بازماندهٔ سامی آغازین *ʔil- «خدا» است و با عبری ʾēl / ʾĕlōhīm، آرامی ʾĕlāh (حالت مقصور ʾĕlāhā) و سریانی ʾalāhā هم‌ریشه است. ریشهٔ سه‌حرفیِ «أ ل ه» و فعل «أَلَهَ» به معنی «پرستیدن» که نحویان عرب استخراج کرده‌اند، خودْ برساخته از همین اسم‌اند. جفری می‌افزاید که صورت معرفه، که پیش از اسلام هم در کتیبه‌های شمال و جنوب عربستان دیده می‌شود، به احتمال بسیار وام از سریانی ʾalāhā است. ادعای نورایی در این گره درست است.\",\n  \"sources\": [W_ALLAH, W_ILAH, E_ALLAH],\n  \"ref_check\": [\n    {\"ref\": \"KLN:505\", \"status\": \"supports\",\n     \"note\": \"Klein s.v. Elohim (p.505): '…Arab. ilāh, with the article Allāhu (see Allah)' — i.e. Allāh = al- + ilāh, Nourai's arrow exactly. Klein's own Allah entry (p.51) repeats it: 'Arab. Allāhu, contraction of al-ilāhu, fr. al-, \\\"the\\\", and ilāh, \\\"God\\\". See Elohim.'\"},\n    {\"ref\": \"FVQ:33\", \"status\": \"not_found\",\n     \"note\": \"FVQ p.33 (FVQ_pages.txt leaf 50, running head 'INTRODUCTION 33') is part of Jeffery's introduction and discusses supposedly Coptic words in Sura xii (taḥt, hayta lak, ḥāsha lillāh); it says nothing about Allāh. The Allāh article is at FVQ p.66, which Nourai cites correctly in the root box — 'FVQ:33' on this node looks like a slip for 66 (or a stray copy of the neighbouring 'FVA:33').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. Allah, p.51 (KLN_1966.txt line 2240, leaf 38)\", \"stance\": \"supports\",\n     \"note\": \"'Allah, n., Mohammedan name of the Supreme Being. — Arab. Allāhu, contraction of al-ilāhu, fr. al-, \\\"the\\\", and ilāh, \\\"God\\\". See Elohim.'\"},\n    {\"src\": \"FVQ\", \"where\": \"p.66 s.v. Allāh\", \"stance\": \"supports\",\n     \"note\": \"'In the Semitic area ʾl was a widely used word for deity, cf. Heb. ʾl; Aram. ʾlh; Syr. ʾalāhā; Sab. ʾlh… Ar. ilāh is doubtless a genuine old Semitic form.'\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"Addi Shir lists only Persian words arabicised; Allāh is not and could not be in it — no entry found.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"Allâh «الله»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian الله allāh is a straight loan of the Arabic divine name, carried into Persian with the Qur'anic and religious vocabulary from the 2nd/8th century onwards and pronounced in Persian with the same emphatic lām (allāh). It is unassimilated: Persian keeps the Arabic script, the shadda and the dagger-alif. The derivatives printed in the box are likewise Arabic-shaped formations built on ʾilāh, not on allāh: الهی elāhi 'divine' (Arabic nisba ʾilāhī), الهیّات elāhiyyāt 'theology' (Arabic plural of the nisba, a calque of Greek theologia used in the Islamic philosophical tradition), and الهه elāhe 'goddess' (feminine ʾilāha, in modern Persian used for the goddesses of classical mythology). Mo'in's dictionary marks الله and its family [ع.] 'Arabic'. Bābā Ṭāher's quatrain quoted on the page ('خوشا آنان که الله یارشان بی') shows the word fully at home in Persian folk verse.\",\n  \"derivation_fa\": \"«اللّٰه» در فارسی وام‌واژه‌ای است مستقیم از عربی که همراه با واژگان قرآنی و دینی از سدهٔ دوم هجری به فارسی راه یافته و با همان لامِ مفخّم تلفظ می‌شود؛ واژه اصلاً به دستگاه آوایی فارسی سازگار نشده و املای عربی با تشدید و الف کوتاه را نگه داشته است. مشتقاتی که در جدول آمده نیز ساخت عربی‌اند و بر پایهٔ «إله» ساخته شده‌اند نه «الله»: «الهی» (نسبتِ عربی ʾilāhī)، «الهیّات» (جمع همان نسبت، برابرنهادِ theologia یونانی در سنّت فلسفی اسلامی) و «الهه» (مؤنث ʾilāha که در فارسی امروز برای ایزدبانوان اساطیری به کار می‌رود). معین نیز این واژه‌ها را با نشانِ [ع.] یعنی عربی می‌آورد. بیت باباطاهر که در جدول نقل شده نشان می‌دهد واژه در شعر عامیانهٔ فارسی کاملاً جاافتاده است. ادعای نورایی درست است.\",\n  \"sources\": [W_ALLAH, W_ILAH],\n  \"ref_check\": [\n    {\"ref\": \"FVA:33\", \"status\": \"not_checked\",\n     \"note\": \"S.M. Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi (1368/1989): refs_online.json records that no digital copy exists on archive.org, ketabnak or noorlib, and a fresh search in 2026-09 found none either; the claim (a plain Arabic loan) was checked against Mo'in and Wiktionary instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. لب / اله family, read at abadis.ir (فرهنگ معین section)\", \"stance\": \"supports\",\n     \"note\": \"Mo'in tags the Arabic-origin words of this family [ع.]; the same page shows he keeps [ع.] and [په.] strictly apart (لُبّ [ع.] 'خالص و برگزیده از هر چیزی' vs لَب [په.] 'کنارهٔ هر چیزی'), so the [ع.] tag is a real etymological statement, not a default.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, vols 1–3 (BQT_v1_pages.txt / v3)\", \"stance\": \"silent\",\n     \"note\": \"Borhān is a dictionary of Persian/Dari words and deliberately excludes ordinary Arabic religious vocabulary; grep finds no الله headword, so it neither supports nor contradicts.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt, alef section)\", \"stance\": \"silent\",\n     \"note\": \"Horn treats only inherited Iranian material; Arabic loans such as الله are outside his scope — no entry.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"English\", \"words\": \"Allah\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English Allah is a direct learned borrowing of the Arabic divine name, first recorded in 1702 in the form Alha and standardised as Allah in 18th-century accounts of Islam (earlier English writers used 'Alla' via Latin and Italian travel literature). It never passed through Persian; the arrow on the chart runs from the Arabic box, not from the Persian one, which is right. Klein p.51 and the AHD both simply give 'Arab. Allāh, contraction of al-ilāh'.\",\n  \"derivation_fa\": \"«Allah» در انگلیسی وام‌واژه‌ای است مستقیم و کتابی از نام عربیِ خداوند که نخستین بار در سال ۱۷۰۲ به صورت Alha ثبت شده و در سدهٔ هجدهم در نوشته‌های مربوط به اسلام به شکل Allah تثبیت شده است؛ پیش از آن نویسندگان انگلیسی صورت Alla را از راه لاتین و ایتالیایی به کار می‌بردند. این واژه از مسیر فارسی نگذشته است و پیکانِ جدول هم درست از خانهٔ عربی کشیده شده نه از خانهٔ فارسی. کلاین (ص۵۱) و فرهنگ American Heritage نیز همین را می‌گویند. ادعای نورایی درست است.\",\n  \"sources\": [E_ALLAH, W_ALLAH],\n  \"ref_check\": [\n    {\"ref\": \"KLN:51\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt line 2240 (leaf 38, i.e. printed p.51 on Klein's two-pages-per-leaf scan): 'Allah, n., Mohammedan name of the Supreme Being. — Arab. Allāhu, contraction of al-ilāhu, fr. al-, \\\"the\\\", and ilāh, \\\"God\\\". See Elohim.'\"},\n    {\"ref\": \"AHD\", \"status\": \"not_checked\",\n     \"note\": \"Nourai's bare 'AHD' here points to the main-dictionary entry of the 1975/76 New College Edition, whose scans on archive.org are lending-only (djvu.txt returns 401); ahdictionary.com serves the IE-root appendix and current entries but Allah is not an IE-root word. The substance was checked on Klein and Etymonline instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. Allah p.51\", \"stance\": \"supports\", \"note\": \"See ref_check above — same wording.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard (FSD_vol1.txt, grep '^Allah')\", \"stance\": \"silent\",\n     \"note\": \"The OCR of vol. 1 yields only the gazetteer line 'highest peak, Mus Allah, 9,591 ft. Rhodope' (line 91167); the dictionary article itself was not recoverable from this scan.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century (WEB_vol1.txt, grep '^Allah')\", \"stance\": \"silent\",\n     \"note\": \"No hit in the local OCR of vol. 1.\"}\n  ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 1\ne1 = {\n  \"entry\": 1,\n  \"root\": \"L.b.n\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Semitic root *l-b-n 'to be white' (Akkadian labānu; Heb. lābhān 'white', lebhōnāh 'frankincense'; Arabic laban 'milk', lubān 'frankincense')\",\n  \"note\": \"The root is real and the gloss is right. Klein sets out the whole family under 'leban': Arab. laban 'milk' is 'rel. to Heb. lābhān, \\\"white\\\", lebhānāh, poetic name for the moon (lit. \\\"the white one\\\"), lebhōnāh, Aram.-Syr. lebhūntā, Arab. lubān, \\\"frankincense\\\"… Heb. Lebhānōn, Akkad. Labnānu, Aram. Libhnān, Arab. Lubnān, \\\"Mount Lebanon\\\", lit. \\\"the white one\\\"; so called from the whiteness of its cliffs.' Mo'in's footnote at the page Nourai cites, Borhān-e Qāṭeʿ p.1886 s.v. لبان, says the same thing in Persian: the Greek libanos / Latin olibanum is 'از سامی مشتق است' (of Semitic origin), Heb. lebonah, Aram. lebota, and 'آشوری labanu بمعنی سفید بودن است، بمناسبت رنگ…' — Assyrian labānu 'to be white', named from the colour of the resin. The only qualification is that 'milk' and 'white resin' are two independent nominal derivatives of the same root, not a chain, which is how Nourai draws them (all three words in one node).\",\n  \"note_fa\": \"ریشهٔ سامی «ل ب ن» به معنی «سفید بودن» ریشه‌ای واقعی است و معنایی که نورایی داده درست است. کلاین ذیل leban همهٔ خانواده را گرد آورده است: «لَبَن» عربی «شیر»، عبری lābhān «سفید»، lebhānāh «ماه» (یعنی «سپید»)، lebhōnāh و آرامی–سریانی lebhūntā و عربی «لُبان» یعنی کندر، و نیز نام «لبنان» به معنی «سپید» به مناسبت سپیدی صخره‌هایش. معین نیز در حاشیهٔ برهان قاطع ص۱۸۸۶ ذیل «لبان» می‌نویسد که Libanos یونانی (یا Olibanus) «از سامی مشتق است»، عبری lebonah، آرامی lebota، و «آشوری labanu بمعنی سفید بودن است، بمناسبت رنگ…». تنها نکته آن است که «شیر» و «صمغ سپید» دو مشتق مستقل از یک ریشه‌اند نه زنجیره‌ای پیوسته، حال آنکه نورایی هر سه واژه را در یک خانه کنار هم نهاده است.\",\n  \"sources\": [W_LUBAN, E_BENZ],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1886\", \"status\": \"supports\",\n     \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, printed p.1886 = BQT_v3_pages.txt '[pdf page 683]' (running head ۱۸۸۶; the neighbouring pdf 684 carries ۱۸۸۷), s.v. لبان: footnote 7 'Libanos یونانی (یا Olibanus) از سامی مشتق است، عبری lebonah، آرامی lebota… صمغ کندر که تازه و بسته باشد «عقار ۱۸۸ ف»' and the etymological note 'آشوری labanu بمعنی «سفید بودن» است، بمناسبت رنگ…'. Exactly Nourai's root and gloss.\"},\n    {\"ref\": \"KFL:430\", \"status\": \"not_checked\",\n     \"note\": \"Thaʿālibī, Fiqh al-lugha, Beirut 1885: the local copy (KFL.txt) is an OCR of a different, unpaginated printing (no form-feeds at all — `grep -c $'\\\\f' KFL.txt` = 0), so p.430 of the 1885 Beirut edition cannot be located; grepping 'لبن' returns only incidental occurrences in other chapters.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. leban, p.875 (KLN_1966.txt line 21362)\", \"stance\": \"supports\",\n     \"note\": \"'leban… VArab. laban, leben, \\\"sour milk\\\", fr. Arab. laban, \\\"milk\\\", which is rel. to Heb. lābhān, \\\"white\\\", lebhānāh, poetic name for the moon (lit. \\\"the white one\\\"), lebhōnāh, Aram.-Syr. lebhūntā, Arab. lubān, \\\"frankincense\\\" (Gk. λίβανος, λιβανωτός, \\\"frankincense\\\", are Sem. loan words)… Cp. olibanum and the first element in benzoin.'\"},\n    {\"src\": \"BQT\", \"where\": \"vol. 3 p.1886 s.v. لبان (Moʿin's footnote 7)\", \"stance\": \"supports\",\n     \"note\": \"See ref_check — Assyrian labānu 'to be white'.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1331/1332 (LKT.txt lines 626, 3097, leaf 133)\", \"stance\": \"supports\",\n     \"note\": \"Lokotsch derives the European Benzoe words from Arab. lubān ǧāwī and (no. 1331) lubān 'Weihrauch, Wohlgeruch', the Semitic 'white' word.\"}\n  ],\n  \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"laban, l.b.n; luban; luban jâwî\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"All three forms are real Arabic and all three belong to the root l-b-n 'to be white': لَبَن laban 'milk' (Syrian-Arabic laban 'sour milk', the source of English leban/leben), and لُبَان lubān 'frankincense, olibanum' — a resin named from its whiteness, the Greek λίβανος libanos and Late Latin olibanum being Semitic loans of the same word. لُبان جاوي lubān jāwī is the Arab traders' name for a different, cheaper resin, 'frankincense of Java', ǧāwī being the Arabic adjective from Jāwa, which for the Arabs covered the Malay lands and in this phrase means Sumatra; Nourai's gloss 'the resin of Java (Sumatra)' is exactly right. What is wrong is the gloss on lubān: he writes 'the white resin of sandalwood'. Frankincense is the gum of Boswellia (and the Java sort is the balsam of Styrax benzoin Dryander, a Sumatran tree) — sandalwood (Santalum) yields an oil, not this resin. Hobson-Jobson s.v. BENJAMIN, BENZOIN: 'A kind of incense, derived from the resin of the Styrax benzoin, Dryander, in Sumatra… It got from the Arab traders the name lubān-jāwī, i.e. \\\"Java Frankincense\\\".' The node is therefore right in its forms and its root, wrong in one botanical gloss — hence plausible.\",\n  \"derivation_fa\": \"هر سه صورت عربیِ درست‌اند و هر سه به ریشهٔ «ل ب ن» با معنی «سفید بودن» بازمی‌گردند: «لَبَن» یعنی شیر (در عربی شامی «ماست/شیر ترش» که انگلیسی leban از آن است) و «لُبان» یعنی کندر، صمغی که از سپیدی‌اش چنین نام گرفته و واژهٔ یونانی λίβανος و لاتینی olibanum نیز وام از همین کلمهٔ سامی‌اند. «لُبان جاوی» نام بازرگانان عرب برای صمغی دیگر و ارزان‌تر است، یعنی «کندرِ جاوه»؛ عرب‌ها «جاوه» را بر همهٔ سرزمین‌های مالایی اطلاق می‌کردند و در این ترکیب مقصود سوماترا است — پس ترجمهٔ نورایی «صمغ جاوه (سوماترا)» درست است. اما معنایی که برای «لُبان» آورده («صمغ سفید صندل») نادرست است: کندر صمغ درخت بوسولیا است و «لُبان جاوی» بلسانِ درخت Styrax benzoin سوماترایی، نه صندل؛ صندل روغن می‌دهد نه این صمغ. یول و برنل در Hobson-Jobson ص۸۶ همین را تصریح کرده‌اند. بنابراین صورت‌ها و ریشه درست است و تنها یک معنیِ گیاه‌شناختی خطاست: با احتیاط پذیرفتنی.\",\n  \"sources\": [W_LUBAN, E_BENZ, AHD_BENZ],\n  \"ref_check\": [\n    {\"ref\": \"BQT:308\", \"status\": \"partial\",\n     \"note\": \"Borhān-e Qāṭeʿ printed p.308 = BQT_v1_pages.txt leaf 528 (confirmed by the page-foot continuation notes 'بقیه در صفحهٔ ۳۰۹' / 'بقیه از صفحهٔ ۳۰۷'). The relevant matter is Moʿin's added entry at the foot: '◊ بنزین – بکسر اول. از فرانسه benzine از ایتالیایی benzoin (روغن بان)، کلمهٔ بان از عربی بلغات اروپایی نقل شد…'. It confirms that the word travelled from Arabic into the European languages, but Moʿin's Arabic etymon is بان (ben-oil, Moringa) rather than لبان, so the page only partly supports Nourai's Arabic node.\"},\n    {\"ref\": \"KLN:164\", \"status\": \"supports\",\n     \"note\": \"Klein s.v. benzoin (KLN_1966.txt line 4766, leaf 98): 'benzoin, n., a balsamic resin. — F. benjoin, fr. Sp. benjui, which is shortened fr. lo-benjui (the first syllable having been mistaken for the def. article), fr. Arab. lubān jāwī, \\\"frankincense of Java\\\" (Java is the former name of Sumatra). For the etymology of Arabic lubān see leban.'\"},\n    {\"ref\": \"KLN:875\", \"status\": \"supports\",\n     \"note\": \"Klein s.v. leban (line 21362): 'Arab. laban, \\\"milk\\\", which is rel. to Heb. lābhān, \\\"white\\\"… Arab. lubān, \\\"frankincense\\\"… Cp. olibanum and the first element in benzoin.' — the two page numbers Nourai gives (164 and 875) are precisely the benzoin and leban articles.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. BENJAMIN, BENZOIN, p.86 (HJB.txt line 3408)\", \"stance\": \"partial\",\n     \"note\": \"'A kind of incense, derived from the resin of the Styrax benzoin, Dryander, in Sumatra, and from an undetermined species in Siam. It got from the Arab traders the name lubān-jāwī, i.e. \\\"Java Frankincense\\\"… The terms Jāwa, Jāwī were applied by the Arabs to the Malay countries generally (especially Sumatra).' Supports the forms, contradicts the 'sandalwood' gloss.\"},\n    {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale, s.v. Benjoin, p.63 (DEV.txt line 814, leaf 93)\", \"stance\": \"supports\",\n     \"note\": \"'Benjoin. Esp. benjui, menjui; portug. beijoim, beijuim; ital. belzuino, belguino. De l'arabe لبان جاوي loubân djâwi, encens javanais… Par javanais, il faut entendre de Sumatra, car les Arabes appelaient cette grande île Java.'\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1332 (LKT.txt line 3097)\", \"stance\": \"supports\",\n     \"note\": \"'lubān ǧāwī \\\"Javanischer Weihrauch\\\" [obwohl er aus Sumatra stammt], mit Imāla luben ǧāwī…'\"},\n    {\"src\": \"KLN\", \"where\": \"s.vv. benzoin p.164, leban p.875, olibanum p.1133\", \"stance\": \"supports\",\n     \"note\": \"'olibanum, n., frankincense. — ML., fr. L. libanus (Vulgate), fr. Gk. λίβανος, fr. Heb. lebhōnāh, \\\"frankincense\\\", lit. \\\"the white one\\\", fr. lābhān, \\\"white\\\". See leban.' (KLN_1966.txt line 26199)\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"labanîyyât «لبنیّات»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"لبنیّات labaniyyāt 'dairy products' is an Arabic-shaped loan in Persian: Arabic لَبَن laban 'milk' → nisba adjective لَبَنِيّ labanī 'milky, of milk' → its sound feminine plural لَبَنِيَّات labaniyyāt, used substantively for milk products. Persian took the plural over ready-made (as it did صنایع, مرکبات, حبوبات …) and treats it as a collective singular; the shadda is retained in writing but not in Persian pronunciation, which says labaniyyāt/labaniyât. Mo'in's Farhang-e Fārsi has the base form: 'مؤنث لبنی. شیری؛ ج. لبنیات' ('feminine of labanī; milky; pl. labaniyyāt'). The arrow from the Arabic box is therefore correct, and the word is a modern commercial/administrative borrowing, not an old one.\",\n  \"derivation_fa\": \"«لبنیّات» وام‌واژه‌ای عربی‌ساخت در فارسی است: از «لَبَن» عربی به معنی شیر، صفت نسبیِ «لَبَنی» و سپس جمع مؤنث سالمِ آن «لَبَنیّات» ساخته شده که به‌جای اسم برای فرآورده‌های شیری به کار می‌رود. فارسی این جمع را یکجا وام گرفته است — چنانکه «صنایع»، «مرکّبات»، «حبوبات» را — و آن را همچون اسم جمع به کار می‌برد؛ تشدید در نوشتار می‌ماند ولی در تلفظ فارسی معمولاً ادا نمی‌شود. معین نیز ذیل «لبنی» می‌آورد: «مؤنث لبنی. شیری؛ ج. لبنیات». پس پیکانِ جدول از خانهٔ عربی درست کشیده شده و این واژه وام‌گیری نوِ اداری–بازرگانی است نه کهن. ادعای نورایی درست است.\",\n  \"sources\": [W_LUBAN],\n  \"ref_check\": [\n    {\"ref\": \"FVA:363\", \"status\": \"not_checked\",\n     \"note\": \"Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi — no digital copy exists (see refs_online.json, 'RE-SEARCH 2026-09: still no digital copy on any permitted platform'); checked against Mo'in instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. لبنی (MON_part2.txt line 38758)\", \"stance\": \"supports\",\n     \"note\": \"'مونث لبنی. شیری؛ ج. لبنیات' — Mo'in gives labaniyyāt explicitly as the Arabic plural of labanī.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ vol. 3, لب– section (pdf pages 682–684)\", \"stance\": \"silent\",\n     \"note\": \"Borhān lists لبن (a Persian plant/gum sense) and لبنی 'صمغ درختی که از روم می‌آورند و آنرا میعه می‌گویند' but has no لبنیات; the modern dairy word is later than the dictionary (1062/1652).\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi (ARY_pages.txt / ARY_latin_index_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"Aryanpur covers only Indo-European material; an Arabic loan such as لبنیات is outside his scope — no entry.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Spanish\", \"words\": \"loben jui, benjui\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The attested Ibero-Romance forms are Spanish benjuí (also menjuí), Catalan benjuí, Portuguese beijoim/beijuim; 'loben jui' is not an attested Spanish word but the reconstructed intermediate stage, and Nourai is reproducing his sources' formula. Klein: 'F. benjoin, fr. Sp. benjui, which is shortened fr. lo-benjui (the first syllable having been mistaken for the def. article), fr. Arab. lubān jāwī'; Hobson-Jobson p.86: 'The first syllable of the Arabic term was doubtless taken as an article — lo bengioi, whence bengiai, benzoin, and so forth.' The mechanism is a false division: Romance speakers heard lu-/lo- of lubān as their own article lo, and kept only ben(g)jui. The one point on which the sources part company is which Romance language handed the word to French: Klein and Devic say Spanish (Nourai's route), Lokotsch no. 1332 makes Italian benjuì/belgiuì the earliest form, and the AHD says 'from French benjoin and Italian benzoino'. The Spanish link is therefore possible but not established — plausible.\",\n  \"derivation_fa\": \"صورت‌های گواهی‌شدهٔ ایبریایی «benjuí» (و menjuí) در اسپانیایی، «benjuí» در کاتالان و «beijoim/beijuim» در پرتغالی است؛ «loben jui» واژه‌ای واقعی در اسپانیایی نیست بلکه مرحلهٔ بازسازی‌شدهٔ میانی است و نورایی همان فرمول منابع خود را نقل کرده است. کلاین می‌نویسد فرانسهٔ benjoin از اسپانیایی benjui است که خود کوتاه‌شدهٔ lo-benjui است، زیرا هجای نخست را به‌خطا حرف تعریف پنداشته‌اند؛ یول و برنل نیز همین را می‌گویند. سازوکار کار «تقطیع نادرست» است: گویشوران رومی‌زبان lu-/lo- آغازِ «لُبان» را حرف تعریفِ زبان خود گرفتند و تنها ben(g)jui را نگه داشتند. اما در اینکه کدام زبان رومی واژه را به فرانسه رسانده اختلاف هست: کلاین و دویک اسپانیایی می‌گویند (همان مسیر نورایی)، لوکوچ صورت ایتالیایی را کهن‌تر می‌داند و فرهنگ American Heritage «از فرانسهٔ benjoin و ایتالیایی benzoino» می‌نویسد. پس این حلقه ممکن است ولی قطعی نیست.\",\n  \"sources\": [E_BENZ, AHD_BENZ],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n     \"note\": \"Nourai gives no reference for this node; the Spanish link was checked against Klein p.164, Devic p.63, Lokotsch 1332 and Hobson-Jobson p.86 (see consulted).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. benzoin p.164\", \"stance\": \"supports\",\n     \"note\": \"'F. benjoin, fr. Sp. benjui, which is shortened fr. lo-benjui (the first syllable having been mistaken for the def. article), fr. Arab. lubān jāwī.'\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.86\", \"stance\": \"supports\",\n     \"note\": \"'The first syllable of the Arabic term was doubtless taken as an article — lo bengioi… Spanish forms are benjui, menjui; Modern Port. beijoim, beijuim; Ital. belzuino.'\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1332 (LKT.txt line 3097)\", \"stance\": \"partial\",\n     \"note\": \"'…mit Abfall der ersten Silbe it. benjuì, belgiuì, gebräuchlicher belgioina, benzoino, frz. benjoin, kat. benjuí, sp. benjuí, menjuí, pg. beijoim, beijuim' — Lokotsch puts Italian first in the list, not Spanish.\"},\n    {\"src\": \"DEV\", \"where\": \"Devic p.63 s.v. Benjoin\", \"stance\": \"supports\",\n     \"note\": \"'Esp. benjui, menjui; portug. beijoim, beijuim; ital. belzuino, belguino. De l'arabe لبان جاوي loubân djâwi.'\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"French\", \"words\": \"benjoin\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"French benjoin 'gum benzoin' is first recorded in the 15th century (benjuyn 1479, benjoin from the 16th c.), taken over from the Ibero-Romance/Italian traders' word (benjuí, belzuino) that had come from Arabic lubān jāwī by the false division described above; the -oin spelling is a French adaptation of the final -uí. From French the word passed into English (benjamin, later benzoin) and, in its chemical descendants, back across Europe. The AHD entry for benzoin — the very page Nourai cites — reads 'Earlier benjoin, from French benjoin and Italian benzoino, both from Arabic lubān jāwī, frankincense of Java'.\",\n  \"derivation_fa\": \"«benjoin» فرانسه به معنی صمغ کندرِ جاوی نخستین بار در سدهٔ پانزدهم میلادی (benjuyn ۱۴۷۹) ثبت شده و از واژهٔ بازرگانیِ ایبریایی–ایتالیایی (benjuí، belzuino) گرفته شده است که خود از «لُبان جاوی» عربی با همان تقطیع نادرست پدید آمده بود؛ املای -oin سازگارسازیِ فرانسویِ پایانهٔ -uí است. از فرانسه این واژه به انگلیسی رفت (نخست benjamin و سپس benzoin) و مشتقات شیمیایی‌اش دوباره در سراسر اروپا پخش شد. فرهنگ American Heritage — همان مأخذی که نورایی ارجاع داده — می‌نویسد: «Earlier benjoin, from French benjoin and Italian benzoino, both from Arabic lubān jāwī, frankincense of Java». ادعای نورایی درست است.\",\n  \"sources\": [AHD_BENZ, E_BENZ],\n  \"ref_check\": [\n    {\"ref\": \"AHD:124\", \"status\": \"supports\",\n     \"note\": \"Nourai's page 124 is the main-dictionary page of the 1975/76 New College Edition (b- words), whose scans on archive.org are lending-only; the same article in the current online AHD (ahdictionary.com/word/search.html?q=benzoin, archived by fetch_source.py) reads 'Earlier benjoin, from French benjoin and Italian benzoino, both from Arabic lubān jāwī, frankincense of Java' — exactly the arrow Arabic → Romance → French that Nourai draws.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"DEV\", \"where\": \"Devic p.63 s.v. Benjoin\", \"stance\": \"supports\",\n     \"note\": \"The whole article is devoted to French benjoin < Arabic loubân djâwi; 'Cette étymologie, donnée par Valentijn, est appuyée d'arguments solides dans le Gloss. de Dozy (p. 289).'\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1332\", \"stance\": \"supports\",\n     \"note\": \"'…frz. benjoin, kat. benjuí, sp. benjuí…' listed among the direct continuations of lubān ǧāwī.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. benzoin p.164\", \"stance\": \"supports\",\n     \"note\": \"'benzoin… — F. benjoin, fr. Sp. benjui…'\"},\n    {\"src\": \"PHN\", \"where\": \"Pihan, Dict. étym. des mots français dérivés de l'arabe (PHN.txt, grep 'benjoin')\", \"stance\": \"silent\",\n     \"note\": \"No hit for benjoin in the local OCR of Pihan.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Persian\", \"words\": \"benzîn «بنزین»\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Persian بنزین benzin 'petrol, gasoline' does descend ultimately from the same Arabic lubān jāwī, but not from French benjoin directly: the intervening step is a 19th-century chemical coinage. In 1833 Eilhardt Mitscherlich obtained a hydrocarbon by distilling benzoic acid (Benzoesäure, itself named from Benzoe = gum benzoin) with lime and called it Benzin; from that came French benzine, English benzine/benzene and German Benzin, and it is the fuel sense of that word that Persian borrowed in the early 20th century. Nourai's own reference says so: Moʿin's added entry at Borhān-e Qāṭeʿ p.308 reads 'بنزین… از فرانسه benzine از ایتالیایی benzoin (روغن بان)، کلمهٔ بان از عربی بلغات اروپایی نقل شد. در سال ۱۸۲۵ ماده‌ای که اکنون بنزین می‌نامیم توسط علمای شیمی کشف گردید' — i.e. French benzine, not benjoin. Wiktionary makes the donor German Benzin rather than French, and Lokotsch 1332 lists 'frz. benzin, dtsch. Benzin, Benzol, russ. benzin' as a second, later wave out of benzoin. The arrow's ultimate origin is therefore right and well attested, but its immediate parent should be the chemical term benzine/Benzin, not the resin word benjoin — hence plausible, not confirmed. (Moʿin's own Arabic etymon, بان 'ben-oil' of the Moringa tree, is a further confusion and is not followed here.)\",\n  \"derivation_fa\": \"«بنزین» فارسی سرانجام به همان «لُبان جاوی» عربی بازمی‌گردد، اما نه یکراست از benjoin فرانسه: میان این دو یک نام‌گذاری شیمیایی سدهٔ نوزدهم قرار دارد. در سال ۱۸۳۳ آیلهارت میچرلیش با تقطیر اسید بنزوئیک (Benzoesäure، خود برگرفته از Benzoe یعنی همان صمغ بنجوی) با آهک هیدروکربنی به دست آورد و آن را Benzin نامید؛ از آن، benzine فرانسه، benzine/benzene انگلیسی و Benzin آلمانی پدید آمد و فارسی در آغاز سدهٔ بیستم همین واژه را در معنی سوخت وام گرفت. مأخذ خودِ نورایی هم همین را می‌گوید: معین در حاشیهٔ برهان قاطع ص۳۰۸ می‌نویسد «بنزین… از فرانسه benzine از ایتالیایی benzoin (روغن بان)…» یعنی از benzine نه از benjoin. ویکی‌واژه زبانِ وام‌دهنده را آلمانی (Benzin) می‌داند و لوکوچ نیز «frz. benzin, dtsch. Benzin, Benzol, russ. benzin» را موج دوم و متأخرِ برآمده از benzoin می‌شمارد. پس خاستگاه دور درست است ولی پدرِ بی‌واسطهٔ این واژه اصطلاح شیمیایی benzine/Benzin است نه نام صمغ: با احتیاط پذیرفتنی. (اشتقاقی که معین از «بان» عربی می‌آورد خطاست و پذیرفته نیست.)\",\n  \"sources\": [W_BENZ, E_BENZ],\n  \"ref_check\": [\n    {\"ref\": \"BQT:308\", \"status\": \"partial\",\n     \"note\": \"Borhān-e Qāṭeʿ p.308 (BQT_v1_pages.txt leaf 528, page-foot addenda by Moʿin, verified by the 'بقیه در صفحهٔ ۳۰۹ / بقیه از صفحهٔ ۳۰۷' continuation lines): '◊ بنزین – بکسر اول. از فرانسه benzine از ایتالیایی benzoin (روغن بان)، کلمه بان از عربی بلغات اروپایی نقل شد. در سال ۱۸۲۵ ماده‌ای که اکنون بنزین مینامیم توسط علمای شیمی کشف گردید «نفس»…'. It supports a French donor and an Arabic ultimate origin, but names benzine (not benjoin) as the French form and بان (not لبان) as the Arabic word.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1332 (LKT.txt line 3097)\", \"stance\": \"supports\",\n     \"note\": \"'…engl. benjamin, benzoin, chemischer Fachausdruck, und dtsch. Benzoe; russ. benzoi, poln. benzoes. Hieraus weiter it. belzuino, frz. benzin, dtsch. Benzin, Benzol, russ. benzin, poln. będzwim usw.' — the fuel word is explicitly a later derivative of benzoin, not benzoin itself.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (MON_part1.txt lines 5140–5142, 7002–7006)\", \"stance\": \"partial\",\n     \"note\": \"The 2-vol abridgement uses بنزین only inside definitions ('نفت یا بنزین… حرکت کند') and gives no etymology; Mo'in's etymological statement is the one printed in the Borhān addenda quoted above.\"},\n    {\"src\": \"BQT\", \"where\": \"vol. 1 p.308, Moʿin's addendum\", \"stance\": \"partial\",\n     \"note\": \"See ref_check.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"English\", \"words\": \"benzoin, benzene\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English benzoin 'balsamic resin' is recorded from the 1560s, taken from French benjoin (the older English form was benjamin, a folk-etymological reshaping after the personal name — Hobson-Jobson heads its article 'BENJAMIN, BENZOIN'); the -z- probably reflects the Italian benzoi attested at Venice by 1461. Benzene is a 19th-century chemical term derived from it: Mitscherlich coined Benzin in 1833 from Benz(oesäure) 'benzoic acid' + -in, the acid being got from gum benzoin, and A. W. Hofmann substituted the ending -ene in 1835 to mark the hydrocarbon; English took benzine c.1835 and benzene from 1838. Klein gives both: 'benzoin… F. benjoin, fr. Sp. benjui… fr. Arab. lubān jāwī' and 'benzene… Fr. Benzin, a name coined by the German chemist Eilhardt Mitscherlich (1794–1863) in 1833… The spelling benzene is due to A. W. Hofmann.'\",\n  \"derivation_fa\": \"«benzoin» انگلیسی به معنی صمغ بلسانی از دههٔ ۱۵۶۰ ثبت شده و از benjoin فرانسه گرفته شده است؛ صورت کهن‌ترِ انگلیسی benjamin بود که با ریشه‌شناسی عامیانه به نام خاصِ بنیامین شبیه شده بود (یول و برنل هم مدخل خود را «BENJAMIN, BENZOIN» نامیده‌اند)، و «ز» در آن احتمالاً از صورت ایتالیایی benzoi (ونیز، ۱۴۶۱) آمده است. «benzene» اصطلاحی شیمیایی و متأخر است: میچرلیش در ۱۸۳۳ از Benz(oesäure) «اسید بنزوئیک» به‌علاوهٔ پسوند -in واژهٔ Benzin را ساخت و هوفمان در ۱۸۳۵ پایانهٔ -ene را به‌جای آن نهاد تا هیدروکربن بودن آن را نشان دهد؛ انگلیسی benzine را حدود ۱۸۳۵ و benzene را از ۱۸۳۸ به کار برد. کلاین هر دو را چنین می‌آورد و ادعای نورایی درست است.\",\n  \"sources\": [E_BENZ, AHD_BENZ],\n  \"ref_check\": [\n    {\"ref\": \"AHD:124\", \"status\": \"supports\",\n     \"note\": \"The AHD article on benzoin (current online text, archived) is exactly Nourai's chain: 'Earlier benjoin, from French benjoin and Italian benzoino, both from Arabic lubān jāwī, frankincense of Java.' The 1976 New College page 124 itself is lending-only on archive.org.\"},\n    {\"ref\": \"OEW:61\", \"status\": \"not_checked\",\n     \"note\": \"Shipley, The Origins of English Words (1984) is borrow-only on the Internet Archive (originsofenglish0000ship / originsofenglish00jose; djvu.txt returns 401), so p.61 could not be read; nothing in the claim depends on it.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.vv. benzoin, benzene, benzol, benjamin p.164 (KLN_1966.txt lines 4765–4767)\", \"stance\": \"supports\",\n     \"note\": \"'benjamin, n., gum benzoin. — Corruption of benjoin, an earlier form of benzoin'; 'benzene, n. — Fr. Benzin, a name coined by the German chemist Eilhardt Mitscherlich (1794-1863) in 1833; so called by him because he obtained it through the distillation of benzoic acid with lime. The spelling benzene is due to A. W. Hofmann.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Benzoin (SKT.txt lines 23806-23807)\", \"stance\": \"supports\",\n     \"note\": \"'Benzoin, a resinous substance. (F.—Span.—Arab.) F. benjoin, gum benzoin…' — the same F.–Sp.–Arab. route.\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp.86–87 s.v. BENJAMIN, BENZOIN\", \"stance\": \"supports\",\n     \"note\": \"Gives the English form-history with quotations from 1498 ('beijoim'), 1516 ('Beijuy… which is a resin of trees which the Moors call lubanJavi').\"}\n  ]\n})\n\ndoc[\"entries\"].append(e1)\n\n# ---------------------------------------------------------------- entry 2\ne2 = {\n  \"entry\": 2,\n  \"root\": \"Lěb\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"PIE *lēb-/*leb- (Pokorny 'lēb-, lōb-, lab-, leb- \\\"schlaff herabhängen\\\", auch \\\"Lippe\\\" (?)'); Watkins/AHD isolates a separate *leb-2 'lip'\",\n  \"note\": \"The page number is exactly right: Pokorny IEW p.655 (POK_02.txt leaf 315, the entry running over onto p.656) heads the article 'lēb-, lōb-, lab-, leb- \\\"schlaff herabhängen\\\", auch \\\"Lippe\\\" (?)'. But Nourai's gloss compresses it: for Pokorny the root means 'to hang down limply' and 'lip' is a secondary sense, explicitly marked with a question mark and explained under §2 'mit der Bedeutung \\\"Lippe\\\" als \\\"die hängende\\\" (wie lat. labium)'. Watkins/AHD does treat 'leb-2. Lip' as a root of its own — 'Germanic *lep- in Old English lippa, lip: LIP. 2. Variant form *lab-… Latin labium… [Pok. lēb- 655]' — and that is plainly what Nourai copied. Modern scholarship is more sceptical still: de Vaan 2008:319 (cited by Wiktionary) and Boutkan reject an inherited IE derivation for the Latin–Germanic 'lip' group and suspect a substrate word, and Buck §4.25 (pp.229-230) says the 'root connection [is] uncertain, but more prob. : Skt. lamb-, Lat. labare \\\"slip\\\"'. Note also that Pokorny lists no Iranian material at all under this root: the Iranian branch of the chart comes from Horn/Hübschmann, not from POK.\",\n  \"note_fa\": \"شمارهٔ صفحه دقیقاً درست است: پوکورنی در فرهنگ ریشه‌شناسی هندواروپایی، ص۶۵۵، سرواژه را چنین آورده است: «lēb-, lōb-, lab-, leb- ‹سست آویختن›، و نیز ‹لب› (؟)». اما نورایی معنی را فشرده کرده است: نزد پوکورنی معنی اصلی «سست فروآویختن» است و «لب» معنایی ثانوی و همراه با علامت پرسش، که در بند ۲ چنین توضیح داده شده: «با معنی ‹لب› یعنی ‹آنچه می‌آویزد›، مانند labium لاتینی». در برابر، واتکینز در پیوستِ فرهنگ American Heritage ریشهٔ جداگانه‌ای با عنوان «leb-2. Lip» آورده و همان است که نورایی رونویسی کرده است. پژوهش امروزی محتاط‌تر است: دِ وان (۲۰۰۸، ص۳۱۹) و بوتکان پیوند هندواروپاییِ گروهِ لاتینی–ژرمنیِ «لب» را نمی‌پذیرند و آن را احتمالاً واژه‌ای زیرلایه‌ای می‌دانند، و باک نیز در بند ۴٫۲۵ می‌گوید پیوندِ ریشه‌ای «نامطمئن» است. نکتهٔ مهم دیگر آنکه پوکورنی هیچ صورت ایرانی زیر این ریشه نیاورده است؛ شاخهٔ ایرانیِ این نمودار از هرن و هوبشمان می‌آید نه از پوکورنی.\",\n  \"sources\": [W_LEB, E_LIP, W_LAB],\n  \"ref_check\": [\n    {\"ref\": \"POK:655\", \"status\": \"partial\",\n     \"note\": \"Pokorny p.655 (POK_02.txt line 5013, leaf 315; the printed '656' appears a few lines further down, so the article begins on 655 as cited): 'lēb-, lōb-, lab-, leb- \\\"schlaff herabhängen\\\", auch \\\"Lippe\\\" (?), z. T. mit anlaut. s-… Viele expressive Bildungen'; then '2. mit der Bedeutung \\\"Lippe\\\" als \\\"die hängende\\\" (wie lat. labium): mnl. lippe, nhd. Lippe, afries. ags. lippa m. \\\"Lippe\\\" (*lepi-an-)…'. The page is right; the gloss 'lip' alone is Nourai's simplification (via AHD) of Pokorny's primary 'hang down limply'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leb-2 (AHD_watkins1985.txt line 664)\", \"stance\": \"supports\",\n     \"note\": \"'leb-2. Lip. 1. Germanic *lep- in Old English lippa, lip: LIP. 2. Variant form *lab- in: a. suffixed form *lab-yo- in Latin labium, lip: LABIAL, LABIUM; b. suffixed form *lab-ro- in Latin labrum, lip… [Pok. lēb- 655.]' — Nourai's root name, gloss and both branches in one line.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §4.25 LIP, pp.229-230 (SYN.txt leaf 265)\", \"stance\": \"partial\",\n     \"note\": \"'Lat. labrum… labia… : OE lippa, NE lip, OHG leffur, lefs, NHG lippe…, root connection uncertain, but more prob. : Skt. lamb-, Lat. labare \\\"slip\\\", etc.'; Buck also notes 'Some of the words for \\\"lip\\\" are from the notion of \\\"hanging down\\\" or \\\"projecting\\\"', and lists the inherited Iranian word as Av. aosta-, not lab.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, An IE Comparative Dictionary s.v. labiom (IEC.txt line 9372, leaf 369)\", \"stance\": \"supports\",\n     \"note\": \"'labiom, io (laburom, labs-) \\\"lip\\\". Cf. labudiom & lobos, & cf. WP II, 431, 714. Per. lab \\\"lip, brink\\\"; OLat. labia, Lat. labium & labrum \\\"lip\\\"; Ger. Laffe… OHG lefs, leffur m. \\\"lip\\\"; Sw. läpp… Kurd lews \\\"lower lip\\\"…' — Mann explicitly includes Persian lab in the IE etymon, i.e. Nourai's whole chart.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 431, 714 (cited by Mann; locally only the Register vol., WLD_band3.txt)\", \"stance\": \"partial\",\n     \"note\": \"Bände I–II are not available locally; Mann's cross-reference 'WP II, 431, 714' and Pokorny's own 'WP II 380 ff.' place the material there, so the reference chain is intact but the pages could not be read.\"}\n  ],\n  \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Iranian\", \"words\": \"lap\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"An Iranian *lap- 'lip' is a real reconstruction, made from Book-Pahlavi <lp'>, Pazand law, Balochi lap, Kurdish lêv/liw, Wakhi law/lafč and Sanglechi law; Hübschmann, Persische Studien no. 953 (p.96) puts it in so many words: 'bal. lap setzt ein iranisches lap- voraus, während lat. labium und deutsch Lippe auf leb- zurückgehen'. Mo'in's footnote at the page Nourai cites (Borhān-e Qāṭeʿ p.1885) repeats it, and Wiktionary reconstructs Proto-Iranian *lab-/*lap-. Two reservations keep this from being 'confirmed'. First, the derivation from PIE *leb- is phonologically irregular: Proto-Indo-Iranian merged *l with *r, so an inherited Iranian word should not begin with l-; Wiktionary flags exactly this ('the Iranian initial l- is irregular'), and the words are usually taken as expressive/onomatopoeic or as a substrate word shared with Latin and Germanic. Second, the inherited Iranian word for 'lip' is a different one — Avestan aosta- 'Oberlippe' (Bartholomae), Skt. oṣṭha-, listed by Buck §4.25 — so *lap- is at best a parallel expressive formation, not the regular continuant of the root. Note also that Nourai's 'Iranian lap' and his 'Pahlavi lab' are really one and the same attestation, the Book-Pahlavi spelling <lp'> read two ways.\",\n  \"derivation_fa\": \"بازسازیِ ایرانیِ *lap- «لب» بازسازی واقعی است و بر پایهٔ املای پهلوی <lp'>، پازند law، بلوچی lap، کردی lêv/liw، وخی law/lafč و سنگلیچی law انجام گرفته است؛ هوبشمان در «مطالعات فارسی» شمارهٔ ۹۵۳ (ص۹۶) صریح می‌گوید: «bal. lap صورتی ایرانی *lap- را پیش‌فرض می‌گیرد، حال آنکه labium لاتینی و Lippe آلمانی به *leb- بازمی‌گردند». معین نیز در حاشیهٔ همان صفحه‌ای که نورایی ارجاع داده (برهان قاطع ص۱۸۸۵) همین را می‌آورد و ویکی‌واژه ایرانی آغازین *lab-/*lap- را بازسازی می‌کند. اما دو نکته مانع از پذیرش قطعی است: نخست آنکه برآمدن این صورت از *leb- هندواروپایی از نظر آوایی قاعده‌مند نیست، زیرا در هندوایرانی آغازین «ل» با «ر» یکی شده و واژهٔ موروثی نباید با l- آغاز شود؛ دوم آنکه واژهٔ موروثیِ ایرانی برای «لب» چیز دیگری است: اوستایی aosta- «لب زبرین» (بارتولومه) و سنسکریت oṣṭha-. پس *lap- در بهترین حالت ساختی موازی و احتمالاً واژه‌ای زیرلایه‌ای یا صوت‌نماست. افزون بر این، «ایرانی lap» و «پهلوی lab» در نمودار نورایی در حقیقت یک گواهِ واحدند: همان املای <lp'> که دو گونه خوانده شده است.\",\n  \"sources\": [W_LAB, W_LEB],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1885\", \"status\": \"supports\",\n     \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, printed p.1885 = BQT_v3_pages.txt '[pdf page 682]', s.v. لب; Moʿin's footnote 3 reads (OCR): 'پازند law، پهلوی lap، بلوچی lap از ایرانی *lap-، لاتینی labium و آلمانی Lippe از *leb-… کردی lew (لب)، هوبشمان ۹۵۳، … lev، وخی law lafč، سنگلیچی law…'. That is Nourai's Iranian node verbatim, and it is where he took the reference-chain (Hübschmann 953) from.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 953, p.96 (HUB.txt line 3389, leaf 106)\", \"stance\": \"supports\",\n     \"note\": \"'953. Np. lab \\\"Lippe\\\" = paz. law, phl. lap Shk. 257, bal. lap setzt ein iranisches lap- voraus, während lat. labium und deutsch Lippe auf leb- zurückgehen. Doch deutet np. lafča \\\"dicke Lippe\\\" vielleicht auf älteres lab-. Kurd. lew \\\"Lippe\\\" bei Socin, kurd. Samml. II, 335.'\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 953, p.212 (HRN.txt leaf 234)\", \"stance\": \"supports\",\n     \"note\": \"'953. leb \\\"Lippe\\\", vergl. lef, lefče. Kāš. lew; kauk.-bergjüd. low, phlv. lap; lat. labium; nhd. Lippe… kurd. liw \\\"Lippe\\\"; bel. lap (216); waχ. law, lafč, sangl. law.'\"},\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch s.v. aošta- (BRT.txt line 2969)\", \"stance\": \"contradicts\",\n     \"note\": \"'j. aosta- m. \\\"Oberlippe\\\", Du. \\\"die beiden [Lippen]\\\"' — the Avestan, i.e. genuinely Old Iranian, word for 'lip' is aošta- (: Skt. oṣṭha-), not anything from *lap-; there is no Avestan or Old Persian attestation of Nourai's 'Iranian lap'.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, printed p.452 (ARY_latin_index_pages.txt lines 13133-13148, pdf page 451)\", \"stance\": \"supports\",\n     \"note\": \"The لب entry lists 'LAP-, LAB- (OLD PERSIAN)', 'LAP, LAW, LAB (PAHLAVI)', 'LEW (KURDISH)', 'LAP (BALUCHI)', 'LAMBATE, RAMBATE (SANSKRIT)', 'LABOS (GREEK)', 'LABIUM, LABRUM (LATIN)', 'LIPPA (OLD ENGLISH)', with references POKORNY, MACKENZIE (LIP) 122, BUCK 229-230, SKEAT (LIP) 343 — an independent modern Persian handbook giving the same tree as Nourai.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"lab\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian lab 'lip' is well attested. MacKenzie's Concise Pahlavi Dictionary p.50 f. has 'lab [lp | M lb, N ~] lip' — i.e. Book Pahlavi spells it <lp'>, Manichaean Middle Persian writes <lb>, and New Persian continues it unchanged. The Manichaean spelling is decisive for the reading: the stop is voiced, so the Book-Pahlavi <p> is merely the historical grapheme and the word was pronounced lab already in Sasanian times (Nyberg, who reads the ideographic/traditional form, prints 'lap [SPTYN] lip: kar + ~ a kiss… — NP lab'). Nourai's chart, which puts 'lap' in the Iranian box and 'lab' in the Pahlavi box, thus in effect splits one attestation into two nodes, but the Pahlavi form itself is exactly right.\",\n  \"derivation_fa\": \"«لب» در فارسی میانه به‌خوبی گواهی شده است. مکنزی در «فرهنگ کوچک پهلوی» می‌آورد: «lab [lp | M lb, N ~] lip»، یعنی در پهلویِ کتابی <lp'> نوشته می‌شود، در فارسی میانهٔ مانوی <lb> و در فارسی نو بی‌تغییر می‌ماند. املای مانوی برای خواندن قطعی است: همخوان پایانی واکدار است، پس <p> در پهلوی کتابی تنها نویسه‌ای تاریخی است و واژه در دورهٔ ساسانی نیز lab تلفظ می‌شده. نیبرگ که خوانش سنتی را به کار می‌برد «lap» می‌نویسد و می‌افزاید «— NP lab». نمودار نورایی که «lap» را در خانهٔ ایرانی و «lab» را در خانهٔ پهلوی نهاده، در واقع یک گواه را دو گره کرده است، ولی خودِ صورت پهلوی کاملاً درست است.\",\n  \"sources\": [W_LAB, AB_LAB],\n  \"ref_check\": [\n    {\"ref\": \"MON:3551\", \"status\": \"not_checked\",\n     \"note\": \"The 6-volume Amir Kabir Farhang-e Fārsi is not online with its pagination (refs_online.json: 'Page numbers cannot be mapped online'; the local MON_part1/part2 are OCR of the 2-vol Adena abridgement without page breaks), so p.3551 itself could not be opened. The content was verified instead in Mo'in's entry as served by abadis.ir, where لَب is tagged '[په.]' (Pahlavi) — i.e. Mo'in does derive the word from Pahlavi, as Nourai says.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, s.v. lab (PHD.txt line 431, leaf 76)\", \"stance\": \"supports\",\n     \"note\": \"'lab [lp | M lb, N ~] lip.' — Book Pahlavi <lp'>, Manichaean <lb>, New Persian identical.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) s.v. lap (NYB_vol2_glossary.txt line 2348)\", \"stance\": \"supports\",\n     \"note\": \"'lap [SPTYN] lip: kar + ~ a kiss 1013. — NP lab.' Nyberg reads the grapheme as lap and expressly equates it with New Persian lab.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. لب, read at abadis.ir\", \"stance\": \"supports\",\n     \"note\": \"Two separate entries: '(لُ بّ) [ع.] خالص و برگزیده از هر چیزی. مغز… عقل' and '(لَ) [په.] کنارهٔ هر چیزی. بخش بیرونی دهان' — the second is tagged Pahlavi.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"lab «لب»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian لب lab continues Middle Persian lab without change (MacKenzie's 'N ~' means the New Persian form is identical); Wiktionary derives it from Proto-Iranian *lab-/*lap- after Edelman, ESIJa V. Nourai's gloss is Mo'in's: 'lip, also side or edge of anything' answers exactly to Mo'in's 'کنارهٔ هر چیزی. بخش بیرونی دهان'. The compounds printed under it are all transparent Persian formations on this word: لبالب labālab 'brim-full' (lab-ā-lab, the intensifying reduplication with the linking -ā- as in سراسر, دوشادوش), لبریز labriz 'overflowing' (lab + present stem of ریختن), لبخند labxand 'smile' (lab + xand, i.e. 'lip-laugh'), لبچین labčin, لبدیس labdis. The Mowlavi line quoted on the page ('بگیرم ادب را ببندم دو لب را') shows the classical usage.\",\n  \"derivation_fa\": \"«لب» فارسی نو بی هیچ دگرگونی از فارسی میانهٔ lab برجای مانده است؛ مکنزی با نشانهٔ «N ~» همین یکسانی را نشان می‌دهد و ویکی‌واژه به پیروی از ادلمان (فرهنگ ریشه‌شناختی زبان‌های ایرانی، ج۵) آن را از ایرانی آغازین *lab-/*lap- می‌گیرد. معنایی که نورایی داده همان معنیِ معین است: «لب، و نیز کناره یا لبهٔ هر چیز» برابر است با «کنارهٔ هر چیزی. بخش بیرونی دهان». ترکیب‌هایی که در جدول آمده همه ساخت‌های شفاف فارسی بر پایهٔ همین واژه‌اند: «لبالب» (تکرارِ تأکیدی با میانوندِ ـاـ مانند سراسر و دوشادوش)، «لبریز» (لب + ستاک حالِ ریختن)، «لبخند» (لب + خند)، «لبچین» و «لبدیس». بیت مولوی که در صفحه نقل شده کاربرد کلاسیک واژه را نشان می‌دهد. ادعای نورایی درست است.\",\n  \"sources\": [W_LAB, AB_LAB, W_LEB],\n  \"ref_check\": [\n    {\"ref\": \"HRN:212\", \"status\": \"supports\",\n     \"note\": \"Horn, Grundriss der neupersischen Etymologie p.212 (HRN.txt leaf 234, running head '— 212 —'), entry no. 953: 'leb \\\"Lippe\\\", vergl. lef, lefče… phlv. lap; lat. labium; nhd. Lippe (vgl. Kluge, Etymolog. Wörterbuch s. v.). kurd. liw \\\"Lippe\\\"; bel. lap (216); waχ. law, lafč, sangl. law.' The page number is exact and the article covers Nourai's whole Iranian-plus-Western chain.\"},\n    {\"ref\": \"MON:3551\", \"status\": \"not_checked\",\n     \"note\": \"Pagination of the 6-vol Mo'in is not reproducible online (see node #2); the entry's content — '[په.] کنارهٔ هر چیزی. بخش بیرونی دهان' — was read on abadis.ir and matches Nourai's gloss 'lip, also side or edge of anything'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. لَب [په.] (abadis.ir)\", \"stance\": \"supports\",\n     \"note\": \"'(لَ) [په.] کنارهٔ هر چیزی. بخش بیرونی دهان' — Pahlavi origin plus the 'edge of anything' sense that Nourai translates.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ p.1885 s.v. لب (BQT_v3 pdf 682)\", \"stance\": \"supports\",\n     \"note\": \"'لب – بفتح اول و سکون ثانی، معروف است و بعربی شفه گویند… و کنار و اطراف هر چیز را نیز گویند' — the same double sense; Moʿin's footnote adds the Pahlavi/Iranian etymology.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 953 p.96\", \"stance\": \"supports\",\n     \"note\": \"'Np. lab \\\"Lippe\\\" = paz. law, phl. lap…'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. labiom (IEC.txt line 9372)\", \"stance\": \"supports\",\n     \"note\": \"'Per. lab \\\"lip, brink\\\"' listed among the direct reflexes of the IE etymon.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Germanic\", \"words\": \"lep\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Germanic *lepjō(n)-/*lipjō(n)- 'lip' is securely reconstructed from Old English lippa, Old Frisian lippa, Middle Dutch lippe (whence French lippe 'thick lower lip'), Dutch lip, Swedish läpp, Danish læbe; beside it stands an s-stem variant *lep-s- in Old High German lefs, Middle High German lefse, German Lefze (modern German Lippe is itself borrowed from Low German). Pokorny p.656 §2 gathers exactly this group: 'mit der Bedeutung \\\"Lippe\\\" als \\\"die hängende\\\" (wie lat. labium): mnl. lippe, nhd. Lippe, afries. ags. lippa m. \\\"Lippe\\\" (*lepi-an-), norw. lepe (*lep-an-), ahd. leffur, as. lepur ds., ahd. lefs \\\"Lefze\\\" (*lep-s)'. Nourai's citation of AHD is apt: Watkins writes 'Germanic *lep- in Old English lippa, lip: LIP'. The gemination of -pp- in OE lippa is the regular West Germanic result before *-j-.\",\n  \"derivation_fa\": \"صورت ژرمنی آغازینِ *lepjō(n)-/*lipjō(n)- «لب» بازسازی‌ای استوار است و بر پایهٔ انگلیسی کهن lippa، فریزی کهن lippa، هلندی میانه lippe (که lippe فرانسه «لب زیرینِ کلفت» از آن است)، هلندی lip، سوئدی läpp و دانمارکی læbe به دست می‌آید؛ در کنار آن گونه‌ای با پسوند -s- هست: آلمانی علیای کهن lefs، آلمانی میانه lefse و Lefze آلمانی امروز (خودِ Lippe آلمانی وام از آلمانی سفلی است). پوکورنی در ص۶۵۶ بند ۲ همین گروه را گرد آورده و می‌نویسد معنی «لب» یعنی «آنچه آویزان است»، همچون labium لاتینی. ارجاع نورایی به فرهنگ American Heritage بجاست، زیرا واتکینز می‌نویسد «Germanic *lep- in Old English lippa». مشدد شدنِ -pp- در lippa نتیجهٔ قاعده‌مندِ ژرمنی باختری پیش از *-j- است. ادعای نورایی درست است.\",\n  \"sources\": [W_LEB, E_LIP],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. leb-2 (AHD_watkins1985.txt line 664): 'leb-2. Lip. 1. Germanic *lep- in Old English lippa, lip: LIP.' — Nourai's Germanic node with its very form 'lep'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny p.656 §2 (POK_02.txt line 5019, leaf 316)\", \"stance\": \"supports\",\n     \"note\": \"'2. mit der Bedeutung \\\"Lippe\\\" als \\\"die hängende\\\" (wie lat. labium): mnl. lippe, nhd. Lippe, afries. ags. lippa m. \\\"Lippe\\\" (*lepi-an-), norw. lepe (*lep-an-), ahd. leffur, as. lepur ds., ahd. lefs \\\"Lefze\\\" (*lep-s).'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. lip (KLN_1971.txt line 138539)\", \"stance\": \"supports\",\n     \"note\": \"'lip, n. — ME. lippe, fr. OE. lippa, rel. to OFris. lippa, MDu. lippe (whence F. lippe, \\\"thick lower lip\\\"), Du. lip, OHG. lefs, MHG. lefs, lefse, dial. G. Lefze (G. Lippe is borrowed fr. LG.), Swed. läpp, Dan. læbe, \\\"lip\\\", and prob. cogn. with L. labium, labrum, \\\"lip\\\", and prob. also with Toch. A lym-, \\\"lip\\\".'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §4.25, p.229\", \"stance\": \"supports\",\n     \"note\": \"Lists 'OE weler, lippa | ME lippe | NE lip | Du. lip | OHG leffur, lefs | NHG lippe' as one group with Lat. labrum/labium.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"English\", \"words\": \"lip\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Old English lippa (masc. n-stem) 'one of the two sides of the mouth' > Middle English lippe > modern lip; the vowel is the regular shortening/lowering of the OE i, and the final -a of the weak declension was lost in Middle English as everywhere. The word has been used of the rim or edge of a vessel since the 1590s. Klein and Etymonline agree on the Germanic history; both note that the further link to Latin labium is only probable (Etymonline: 'Boutkan and de Vaan reject the IE derivation… It may be a substratum word'), but nothing in this node depends on that.\",\n  \"derivation_fa\": \"«lip» انگلیسی بازماندهٔ lippa در انگلیسی کهن است («یکی از دو کنارهٔ دهان»)، که در انگلیسی میانه lippe شد و سپس lip؛ افتادن -a پایانی همان سرنوشت عمومیِ صرف ضعیف در انگلیسی میانه است. از دههٔ ۱۵۹۰ برای لبهٔ ظرف هم به کار رفته است. کلاین و اتیمآنلاین در تاریخچهٔ ژرمنیِ واژه هم‌داستان‌اند؛ هر دو یادآور می‌شوند که پیوند بیشتر با labium لاتینی تنها «محتمل» است (اتیمآنلاین: بوتکان و دِ وان اشتقاق هندواروپایی را نمی‌پذیرند و آن را شاید واژه‌ای زیرلایه‌ای می‌دانند)، اما این نکته به درستیِ خودِ این گره آسیبی نمی‌زند. ادعای نورایی درست است.\",\n  \"sources\": [E_LIP, W_LEB],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n     \"note\": \"Nourai cites no reference on this node; the chain OE lippa > ME lippe > NE lip was checked against Klein s.v. lip, Watkins/AHD s.v. leb-2 and Etymonline (see consulted).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. lip (KLN_1971.txt line 138539)\", \"stance\": \"supports\",\n     \"note\": \"'lip, n. — ME. lippe, fr. OE. lippa…' (with 'lip, tr. v., to touch with the lips, to kiss. — Fr. lip, n.; first used by Shakespeare').\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. leb-2\", \"stance\": \"supports\",\n     \"note\": \"'…Germanic *lep- in Old English lippa, lip: LIP.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt)\", \"stance\": \"silent\",\n     \"note\": \"The local OCR of Skeat yields no readable 'Lip' headword (the scan's L section is damaged); Klein and Watkins were used instead.\"}\n  ]\n})\n\ndoc[\"entries\"].append(e2)\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-304.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", out)\n"
}
```


### [2026-09-06T23:11:01.239Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p304/build.py (file state is current in your context — no need to Read it back)
```


## [2026-09-06T23:11:07.405Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p304/build.py && python3 -m json.tool data/verification/page-304.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 304"
}
```


### [2026-09-06T23:11:11.294Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-304.json
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 10, 'plausible': 4}
root verdicts: {'plausible': 2, 'confirmed': 1}
ref checks: {'supports': 9, 'not_found': 1, 'not_checked': 8, 'partial': 2}
books consulted: {'supports': 33, 'silent': 9, 'partial': 4, 'contradicts': 1} | by book: {'KLN': 8, 'MON': 5, 'BQT': 4, 'LKT': 4, 'HJB': 3, 'DEV': 3, 'HRN': 2, 'ARY': 2, 'SKT': 2, 'HUB': 2, 'FVQ': 1, 'AFM': 1, 'FSD': 1, 'WEB': 1, 'PHN': 1, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'IEC': 1, 'POK': 1, 'SYN': 1, 'AHD': 1}
```


## [2026-09-06T23:11:34.059Z] AGENT

Verification of PDF page 304 (book page 274) is complete: `/home/sfmqrb/git/rishe/data/verification/page-304.json`, `python3 tools/verify_check.py 304` → 14/14 nodes, **0 PROBLEM lines**.

**Counts** — nodes: 10 confirmed, 4 plausible. Roots: 1 confirmed, 2 plausible. Ref checks: 9 supports, 2 partial, 1 not_found, 8 not_checked. 46 `consulted` entries across 22 books.

**Not `confirmed` (no `disputed`, no `transcription_suspect`):**
- ROOT `Layh; A.l.h` (plausible) — the glosses "to be high; to worship" are the medieval Arab grammarians' guesses reported on Jeffery FVQ p.66, which Jeffery himself rejects; modern view: ʾilāh < Proto-Semitic *ʔil-, allāh = al-ilāh / Syriac ʾalāhā.
- ROOT `Lěb` (plausible) — POK:655 is the right page but Pokorny heads it "*lēb- 'schlaff herabhängen', auch 'Lippe' (?)"; de Vaan/Boutkan reject an IE origin for the lip-group (possible substrate); Pokorny lists no Iranian forms.
- #1 Arabic `luban` (plausible) — forms and root correct, but the gloss "the white resin of sandalwood" is wrong: benzoin is the resin of *Styrax benzoin* (Sumatra), frankincense that of Boswellia (Hobson-Jobson p.86). **Book error, extraction faithful.**
- #3 Spanish `loben jui` (plausible) — not an attested Spanish word but the reconstructed pre-form (Klein "lo-benjui"); attested Sp. is *benjuí/menjuí*, and AHD/Lokotsch route the word through Italian, not Spanish.
- #5 Persian `benzîn` (plausible) — ultimate origin right, but the immediate parent is the 1833 chemical coinage *Benzin/benzine* (Mitscherlich), not French *benjoin*. Nourai's own source says so: Mo'in at Borhān p.308 "از فرانسه benzine"; Wiktionary makes the donor German *Benzin*.
- #1 Iranian `lap` (plausible) — real reconstruction (Hübschmann no. 953, Mo'in at Borhān 1885), but Iranian initial *l-* is irregular for PIE *leb-*, and the inherited Old Iranian word for 'lip' is Av. *aošta-* (Bartholomae).

**Reference problem for the owner:** node #1 of entry 0 cites `FVQ:33`, but FVQ p.33 is introduction matter on Coptic words in Sura xii — the Allāh article is at FVQ p.66 (correctly cited in the root box). Looks like a slip in the book (possibly a stray copy of the neighbouring `FVA:33`).

**Extraction errors: none.** I rendered the printed page and checked every form, script and ref string against the JSON — all faithful (including "loben jui", "the white resin of sandalwood", لبنیّات, بنزین, and the لب compounds).

11 web pages archived via `fetch_source.py`; local books quoted with file/line/leaf in every `ref_check`/`consulted` note. Nothing committed — the working tree now has the new `page-304.json` plus the new `sources/web/` files.
